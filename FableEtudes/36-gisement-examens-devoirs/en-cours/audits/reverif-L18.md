# Re-vérification ciblée — lot L18 (maths 9ᵉ, ch. 20, missions 22 à 26), après application de l'audit

> **Valide pour** : arbre de travail lu le 2026-10-02, md5 22 `78de2d62`, 23 `abf66347`, 24 `d624afea`, 25 `9f5399f8`, 26 `a33a0fca`
> (identiques à l'annonce) ; registre et missions publiées sur `origin/main` = `700cddc9` (#626 inclus) ; rendu avec le `bidi.ts` du
> moteur `a6fc5400` (= `dc19a816` + arena#1152, la coche ✓ hors de l'isolat — mergé depuis). Aucun fichier du dépôt modifié.
>
> **Méthode** : énoncés et options relus SANS clé ni étiquette ni explication, chaque question modifiée re-résolue (résultats déjà
> recalculés par sympy/coordonnées au premier audit, énoncés inchangés) ; clés lues ensuite ; chaque texte de remplacement comparé
> mot à mot à la version proposée (le fichier rendu = mes textes + les trois différences annoncées par l'auteur), re-démontré et
> rendu en Chromium `dir=rtl` ; `lot-lint` (moteur `a6fc5400`) : **0 point** sur les cinq fichiers ; DOMPurify et `viewBox` des
> figures modifiées ; les 40 étiquettes relues contre les libellés d'`origin/main`.

## Mission 22 — RAS sur les correctifs ; une étiquette à mettre à jour (#626)

| Q | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q1 | 48 | 48 | OK — la phrase qui préparait Q5 est retirée |
| Q2 | 45 | 45 | OK — figure ajoutée (carré ABCD et [BD], A–B–C–D dans l'ordre, rien de marqué, boîte 22–178 × 12–170 dans 200 × 180) |
| Q3 | O (d) | d | OK — étiquettes posées ; voir M-22 |
| Q6 | (ACQ) (a) | a | OK — rappel faux supprimé ; raisonnement complet |

- **Q6** : la chaîne est complète et ne mobilise que le cours : O ∈ (AC) ⊂ (ACQ) ; (BD) ⟂ (AC) en O (diagonales du carré) ; QB = QD
  (diagonales de deux faces carrées égales) ⇒ QBD isocèle en Q ; **l'ajout de l'auteur « وبما أنّ O منتصف [BD] »** est juste et rend
  explicite le fait qu'utilise la propriété « médiane issue du sommet = hauteur » ⇒ (BD) ⟂ (QO) en O ; (AC) et (QO) sécantes EN O, et
  (BD) passe par O : règle 2 du أحوصل (deux sécantes au même point). Les trois réfutations sont conformes (intersection de (BD) avec
  (BCQ) et (BAS) en B, avec (ACR) en O ; triangle ODR rectangle en D ⇒ angle DOR aigu). Coche après « هذا المستوي » : bien placée.
- **Q2** : la figure montre l'angle de 45° comme toute figure vraie d'un carré — c'est le fait enseigné, pas une mesure lisible qu'on
  pourrait fausser sans rendre la figure fausse : pas de fuite.
- **M-22 (mineur) — Q3 a et b : une étiquette plus exacte existe depuis #626.** `math.vec.symetrie-regle-confondue` (« Tu appliques la
  règle d'une autre symétrie : par rapport à (OI), seule l'ordonnée change de signe ; par rapport à (OJ), seule l'abscisse ; par rapport
  à O, les deux ») nomme exactement l'erreur exécutée (prendre une symétrie axiale pour la symétrie centrale) ; c'est l'étiquette que
  12/21 Q2, publiée par #626, pose sur l'option « المستقيم (OI) » d'un QCM de reconnaissance identique dans sa forme.
  `symetrie-axiale-signe-mal-place` (posée ici sur mon conseil, faute de mieux sur `65b25590`) vise d'abord le signe changé sur la
  mauvaise coordonnée. Correctif : options `a` et `b` → `"misconceptionTag": "math.vec.symetrie-regle-confondue"` (présente dans le
  registre de l'arbre de travail et sur `origin/main` ; vérifié sur copie : `lot-lint` muet). Pour b, une seconde lecture existe (√2 − 1
  pris pour 1 − √2) ; l'explication nomme la confusion axe/centre (porte R1) : l'étiquette tient.
- **Doublons nouveaux** : #626 publie 12/21 Q2 (M(3/2 ; 2), N(−3/2 ; 2), clé (OJ)) et 12/20 Q4 (A(2 ; 3), B(−2 ; −3), vrai/faux sur O) ;
  avec 14/04 Q4, la famille « reconnaître la symétrie » compte trois items publiés. 22 Q3 en diffère par les données (radicaux), la clé (O)
  et la forme (élément à choisir, sans rappel) : voisinage, pas doublon de fait.

## Mission 23 — RAS sur les correctifs ; un indice de forme préexistant (facultatif)

| Q | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q3 | c | c | OK — explication sans rang d'option ; a, b, d étiquetées exactement ; voir O-23 |
| Q4 | b | b | OK — explication sans rang d'option ; elle nomme chaque option par son contenu |
| Q5 | {a, d, e} | {a, d, e} | OK — plus aucune bonne réponse annoncée par Q3 ou Q4 |

- **Q5** : « (CD) ⟂ (AOD) » : (AB) ⟂ (AOD) (règle 2) ; par D passe une seule perpendiculaire à (AOD) (règle 6) ; elle est parallèle à
  (AB) (règle 3) ; la parallèle à (AB) par D est (DC) ⇒ (CD) ⟂ (AOD). « (BC) ⟂ (OB) » : (AD) ⟂ (AOB) ⇒ la perpendiculaire à (AOB) par B
  est (BC) (règles 6 et 3) ⇒ (BC) ⟂ (OB), droite de (AOB) passant par B (règle 1). Tout est démontrable avec le seul cours ; seul le
  pas « (AB) ⟂ (AOD) » figure dans l'énoncé de Q4, qui précède Q5 (étape redonnée, pas la clé). Vrai/faux recalculés en coordonnées ;
  trois vraies (deux « droite ⟂ plan », une « droite ⟂ droite ») et trois fausses (une et deux) : nombre non déductible. d3 justifié.
- **Q3 d** (« المتوازيين (AB) و(DC) ») : faux comme argument, étiquette `perpendiculaire-au-plan-deux-secantes` exacte (« ou à deux droites
  parallèles ») ; clé non la plus longue (c 72 car., d 93).
- **O-23 (mineur, préexistant, accentué par mon correctif de d) — Q3 : la clé est la seule option qui emploie la donnée de l'énoncé**
  « (AO) ⟂ (ABD) ». Un élève rusé la choisit sans la notion ; et depuis mon correctif, d partage avec la clé son premier membre « (AC) مستقيم
  من المستوي (ABD) », si bien que seul le second membre (la donnée) discrimine. Correctif proposé (facultatif) — plan 2×2 où chaque membre
  juste figure dans exactement deux options (clé ; b = bon premier membre, second faux ; d = donnée, généralisation fausse ; a = double
  erreur), vérifié sur copie : clé inchangée, c 72 car. < b 80 / d 76, `lot-lint` muet, rendu conforme (guillemets « » bien orientés) :
  - option `b` → `(AC) مستقيم من المستوي (ABD) يمرّ من A، و(AO) عمودي على (AB) وحده من هذا المستوي` (étiquette inchangée `math.esp.perpendiculaire-au-plan-deux-secantes`) ;
  - option `d` → `(AO) عمودي على المستوي (ABD) في A، فهو عمودي على كلّ المستقيمات المارّة من A` (**retirer** son étiquette : aucune entrée ne nomme cette généralisation) ;
  - explication : remplacer `وحجّة المستقيمين المتوازيين (AB) و(DC) لا تكفي كذلك: المتوازيان لا يعطيان إلّا اتّجاهًا واحدًا.` par
    `وحجّة «كلّ المستقيمات المارّة من A» خاطئة: العمودي على مستوٍ يعامد مستقيمات هذا المستوي المارّة من قدمه، لا كلّ مستقيم يمرّ من A، و(AO) نفسه يمرّ من A.`
  (Vérifié : la règle de d est fausse — (AO) passe par A et ne s'est pas perpendiculaire — ; b n'établit qu'une perpendicularité ; aucune
  option ne nie une prémisse.)

## Mission 24 — RAS sur les correctifs ; une réserve nouvelle (Q4 face à 20/07 Q6)

En-tête « 🏛️ مناظرة 2012 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — متراجحة وقابلية القسمة ومثلّث في مكعّب » : conforme, plus de notion annoncée
sans question ; d2, `practice`, 75/15, `displayOrder` 24 ; 4 questions, rampe 1,2,2,2 : honnête (en-tête d2, questions d1–d2).

| Q | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q2 | ]−∞ ; 3[ (b) | b | OK — mécanisme de c exact, étiquette `int.produit-signes-negatifs` exacte |
| Q3 | 14 (c) | c | OK — phrase de l'auteur juste |
| Q4 (ex-Q5) | قائم في H (b) | b | réserve R-24 (doublon voisin) ; d2 et étiquette de d conformes |

- **Q2** re-dérivé : 6x − 5 < 4x + 1 ⇔ −6 < −2x (x rassemblés à droite) ⇔ 3 > x ; (−6) ÷ (−2) pris pour −3 avec changement de sens ⇒
  x < −3 (option c) ; sans changement de sens ⇒ x > −3 (option d, double erreur muette) ; « قلب … دون سبب » ⇒ ]3 ; +∞[ (a). Le plan 2×2
  reste équilibré (bornes 2-2, valeurs 2-2). La coche suit la clé.
- **Q3 (différence de l'auteur)** : « ينقصه العامل 5 ليقبل القسمة على 10، والعامل 3 ليقبل القسمة على 12 » est juste (10 = 2 × 5,
  12 = 4 × 3). NB : l'ancienne tournure « في الحالة الأولى … في الثانية » renvoyait à l'ordre des deux nombres cités dans la même phrase
  (« على 10 وعلى 12 »), pas au rang des options — ce n'était pas le défaut de 23 ; la nouvelle est néanmoins plus claire.
- **Q4 d** `math.geo.hypotenuse-mal-choisie` : conforme à l'usage du chapitre (02 Q2, 03 Q6, 07 Q6, 08 Q3) et nommé par l'explication (R1).
- **Slug** : le fichier s'appelle encore `…-qcm-inequation-puissances-symetrie-cube.json` ; invisible pour l'élève, corrigible tant qu'il
  n'est pas publié (le slug fait l'identité des UUID).
- **R-24 (réserve, non relevée à mon premier passage) — Q4 répète, à une isométrie du cube près, la question publiée 20/07 Q6** (« ABCDEFGH
  مكعّب، والمستقيم (AB) عمودي على المستوي (BCG). ما طبيعة المثلّث ABG ؟ », d1) : même triangle arête / diagonale de face / diagonale du
  cube (côtés a, a√2, a√3), angle droit au même type de sommet, mêmes familles d'options (« متقايس الأضلاع », angle droit au mauvais sommet
  étiqueté `hypotenuse-mal-choisie`, variante isocèle), même explication. Seule différence de fond : 20/07 donne la perpendicularité
  (application de la règle 1), 24 la fait établir (règle 2 puis règle 1, ou longueurs et réciproque de Pythagore). `content:tranche` ne
  la relève pas (Jaccard < 0,45). Arbitrage proposé : la garder et la **justifier au rapport de livraison comme exercice parallèle voulu**
  (version non échafaudée du d1 de 20/07, sujet officiel 2012, seul item d'espace de la mission ; d2 la distingue du d1) ; l'écarter
  viderait la mission 24 de tout item d'espace et l'obligerait à quitter le ch. 20 (cas de la mission 27). À noter aussi : 24 et 20/07
  ont la même ossature (inéquation en deux étapes + nature d'un triangle du cube), avec d'autres données et d'autres pièges.

## Mission 25 — RAS

| Q | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q4 | (1/2 ; −1/2) (d) | d | OK — b `int.signe-ignore-dans-somme` exacte ((−1 + 0)/2 lu (1 + 0)/2) |
| Q6 | 15 (c) | c | OK — critère de 25 juste et suffisant |
| Q7 | a√2/2 (a) | a | OK — figure hors échelle, étiquettes conformes |

- **Q6** : « يقبلها عدد إذا كان العدد المكوّن من رقمَي عشراته وآحاده 00 أو 25 أو 50 أو 75 » est le critère exact ; les deux derniers chiffres
  de N ne dépendent que de ceux de 20172017 : 17² − 4 = 285 ⇒ 85 (recalculé : N mod 100 = 85) ⇒ N non divisible par 25. La ligne
  « 17² − 4 = 289 − 4 = 285 » est reconnue par `isDisplayEquation` (bloc LTR). Le passage « ؛ » → « . » + paragraphe : sans effet de sens.
- **Q7 figure** : S en (157,5 ; 63) ⇒ SO = 102 px pour AB = 130 px, rapport 0,785, à égale distance de a√2/2 (0,707) et de a√3/2 (0,866) :
  plus lisible à l'échelle ; figure vraie (S à la verticale de O, centre des deux diagonales) ; boîte 52–265 × 40–207 dans 300 × 232 ;
  étiquette « a » de [SA] à 10,5 px de [SA] et 21,7 px de [SD] (sans ambiguïté). Étiquettes `reponse-a-l-autre-inconnue` : c (hauteur de
  face) = précédent 20/04 Q5 ; d (a√2 = AC, résultat intermédiaire) = libellé littéral ; b (a = arête donnée) = précédent 20/19 Q4
  (option « 4 » = SC donnée) : exactes au sens de l'usage du chapitre.

## Mission 26 — RAS

| Q | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q1 | 5 | 5 | OK — « الدليل السالب » |
| Q3 | \|2π − 2\| (b) | b | OK — a `num.comparaison-radical-et-entier` exacte, phrase d'explication juste (27 > 25) |
| Q6 | (HFG) (c) | c | OK — réfutation de (ACG) conforme au cours |

- **Q6** : B(1,0,0) et F(1,0,1) hors du plan diagonal (ACG) (x = y), (BF) ∥ (CG) ⊂ (ACG) ⇒ (BF) ne coupe pas (ACG) ; « المستقيم العمودي على
  مستوٍ يقطعه في نقطة » reprend la définition du cours. Les étiquettes a (deux parallèles (AB), (FE)) et b (une seule droite (FG)) restent exactes.
- **Doublons** : #626 publie 12/20 Q7 ((1 + √3)² = 4 + 2√3) — c'est l'étape de calcul de l'option d de 26 Q3, pas la même question.

## Bilan de la re-vérification

- **28 questions** dans la tranche (24 en a perdu une), **0 clé fausse** ; les 16 questions reprises sont conformes aux correctifs.
- **0 défaut introduit** par les correctifs, ni par mes textes ni par les trois différences de l'auteur (toutes justes) : aucune prémisse
  niée, aucun distracteur devenu vrai, aucun nombre contredit, aucun vote reconstituable, aucune clé strictement la plus longue, coches
  toutes après la clé, aucune ligne de formule non reconnue, aucune paire à virgule arabe, figures vraies et sans fuite.
- **À trancher / appliquer** :
  1. M-22 (mineur) : 22 Q3 a, b → `math.vec.symetrie-regle-confondue` (étiquette de #626, plus exacte) ;
  2. O-23 (mineur, facultatif) : 23 Q3, plan 2×2 pour que la clé ne soit plus la seule à employer la donnée (textes ci-dessus, vérifiés) ;
  3. R-24 (réserve) : 24 Q4 ≈ 20/07 Q6 à une isométrie près — garder en la justifiant comme exercice parallèle (recommandé) ou écarter et
     sortir la mission 24 du ch. 20.
