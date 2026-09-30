# Audit indépendant de la tranche L03 : chapitre 03, missions d'examen 21 à 26 (rapport de l'auditeur a088fedf468c38de9, copie de travail)

**Verdict : 0 clé fausse sur 38 questions, mais la tranche ne part pas en l'état.** 7 défauts majeurs (indice qui livre la clé sans calcul), 8 mineurs, 6 observations. Aucun critique.

Méthode : re-résolution à l'aveugle + sympy ; registre/cours/missions publiées lus sur origin/main (1bdffbf9) ; chapter.json identique à main ; transcriptions identiques à main. Correctifs testés aux gates sur copie : aucun ne rend la clé strictement la plus longue, ne nie une prémisse, ne fuit, ni ne crée de paire proche.

## Tableaux par fichier
21 (2019 générale ex.2, 7 q) : Q1 a OK (étiquette de b en réserve m1) ; Q2 d OK (b et c muettes candidates à la nouvelle étiquette) ; Q3 a OK (l'énoncé redonne le résultat de Q2) ; Q4 d OK ; Q5 b OK ; **Q6 d MAJEUR M1** (l'option b nie la prémisse b < a) ; Q7 c OK.
22 (2020 générale ex.3, 6 q) : Q1 a OK ; Q2 d OK ; Q3 c réserve (mécanisme faux m3, étiquette de d m2) ; Q4 b (1) OK ; Q5 a réserve (m4) ; **Q6 b (1) MAJEUR M2** (même valeur de B au même x que Q4).
23 (2021 générale ex.2, 7 q) : **Q1 d MAJEUR M3** (vote majoritaire ; option c ambiguë) ; **Q2 b (1) MAJEUR M4** (le rappel « inverses ⟺ produit 1 » désigne la clé) ; Q3 a OK ; Q4 c OK (O5) ; Q5 d OK ; Q6 a OK ; Q7 b (1) OK.
24 (2023 technique ex.2, 6 q) : Q1 c OK (m1) ; Q2 b OK ; Q3 8 numeric OK (tolérance 0) ; Q4 c OK ; **Q5 d MAJEUR M5** (la règle et « ab = 1 » livrent la moitié de la clé) ; Q6 a OK.
25 (2025 technique ex.2, 6 q) : Q1 d OK (m1) ; **Q2 a MAJEUR M6** (b contredit la règle ; « ab = 1 » deux fois) ; Q3 {b,d} multi OK ; Q4 c (14) réserve (m2) ; Q5 d réserve (m5) ; Q6 b (13) OK (m6).
26 (2026 technique ex.2, 6 q) : Q1 c OK ; Q2 a OK (d1) ; Q3 b OK (m1) ; **Q4 {a,b} MAJEUR M7** (le rappel désigne l'ensemble) ; Q5 c (4) OK ; Q6 d (4) réserve (m7).

## Défauts majeurs, avec le texte de remplacement exact

### M1 — 21 Q6, l'option b nie une prémisse
L'énoncé pose b = (3 + √3)², a = (2 + 2√2)² et b < a. L'option b affirme que les deux carrés valent 12, donc b = a.
- Option b. Ancien : « c² = 1 ، لأنّ (3 + √3)² = 3² + (√3)² = 12 و (2 + 2√2)² = 2² + (2√2)² = 12 » (étiquette carre-somme-sans-double-produit). Nouveau : **« c² < 1 ، لأنّ c² = b²/a² و b < a »**, sans étiquette. Elle est fausse : c² ≈ 0,9605 alors que b²/a² ≈ 0,9225. Verdicts équilibrés (deux « < 1 », deux « > 1 »), clé (52 signes) à égalité avec a et c.
- Nouvelle explication : « الأسّ يخصّ البسط والمقام معًا: c² = (3 + √3)²/(2 + 2√2)² = b/a. وبما أنّ 0 < b < a فإنّ البسط b أصغر من المقام a، فالخارج b/a أصغر من 1، أي c² < 1 ✓. الخطأ الشائع قراءة العلاقة بين البسط والمقام بالعكس، فيُظنّ أنّ بسطًا أصغر من المقام يعطي خارجًا أكبر من 1؛ ومن ظنّ أنّ c = b/a ناسيًا أنّ b و a مربّعا البسط والمقام كتب c² = b²/a²، فأصاب في الحكم وأخطأ في الحجّة لأنّ c² = b/a؛ ومن ربّع البسط وحده فكتب c² = (3 + √3)²/(2 + 2√2) حصل على خارج أكبر من 1. »

### M2 — 22 Q6, la clé est celle de Q4
Q4 (méthode 1) et Q6 (méthode 2) demandent la même valeur : B en x = (√5 + √2)/2, clé 1 dans les deux cas. Réécriture de Q6 (garder d3, clé en b) :
- Énoncé : « نعتبر العبارة:\nB = (x − (√2 + 1)/2)(x − (√2 − 1)/2)\nونعوّض x بالعدد:\nx = (√5 + √2)/2\nما قيمة كلٍّ من العاملين x − (√2 + 1)/2 و x − (√2 − 1)/2 على الترتيب ؟ »
- Options : a « (√5 − 1)/2 و (√5 − 1)/2 » (moins-devant-parenthese) ; b « (√5 − 1)/2 و (√5 + 1)/2 » clé ; c « (√5 + 1)/2 و (√5 − 1)/2 » (moins-devant-parenthese) ; d « (√5 + 1)/2 و (√5 + 1)/2 » (moins-devant-parenthese). Vote par position 2 contre 2 ; le produit de c vaut aussi 1.
- Explication : « نحسب العاملين بقلب إشارة كلّ حدّ في البسط المطروح: x − (√2 + 1)/2 = (√5 + √2 − √2 − 1)/2 = (√5 − 1)/2 و x − (√2 − 1)/2 = (√5 + √2 − √2 + 1)/2 = (√5 + 1)/2 ✓. ثمّ B = ((√5 − 1)/2) × ((√5 + 1)/2) = ((√5)² − 1²)/4 = (5 − 1)/4 = 1، وهي القيمة نفسها التي تعطيها العلاقة B = A − 1/4. الخطأ الشائع قلب إشارة الحدّ الأوّل وحده من البسط المطروح: في العامل الأوّل يبقى +1 فيخرج (√5 + 1)/2، وفي العامل الثاني يبقى −1 فيخرج (√5 − 1)/2؛ ومن وقع فيه في العاملين معًا وجد الزوج نفسه مقلوب الترتيب، وجداؤه 1 أيضًا، فلا يكفي أن يساوي الجداء 1 ليكون الزوج صحيحًا. »

### M3 — 23 Q1, vote majoritaire et option ambiguë
b porte les numérateurs de la clé, c ses dénominateurs (clé d reconstruite par vote) ; c est aussi produite par √63 = 9√7 et √112 = 16√7 (facteur-racine-sans-carre) : ambiguë.
- Option c. Ancien : « a = (4 − 3√7)/3 و b = (4 + 4√7)/3 ». Nouveau : **« a = √7 و b = 5√7/3 »**, étiquette math.alg.termes-semblables-par-coefficient (12 − 3√7 écrit 9√7, 16 + 4√7 écrit 20√7). Longueurs : clé 31, b 32, a 26, nouvelle c 18.
- Explication, dernière proposition. Ancien : « أو قسمة الحدّ الأوّل وحده من البسط فيخرج (4 − 3√7)/3 و (4 + 4√7)/3. » Nouveau : « أو جمع العدد مع معامل الجذر كأنّهما حدّان متشابهان: 12 − 3√7 = 9√7 و 16 + 4√7 = 20√7 فيخرج a = √7 و b = 20√7/12 = 5√7/3. »

### M4 — 23 Q2, le rappel désigne la clé
- Nouvel énoncé : « بعد الاختزال صار العددان كسرين لهما المقام 3:\na = (4 − √7)/3\nb = (4 + √7)/3\nما ناتج ضربهما a × b ؟ ». Options et explication inchangées. (La version nue « نعتبر العددين … ما قيمة الجداء » crée des paires proches : 0,52 avec 17/11 Q4, 0,50 avec 03/10 Q3 : ne pas l'utiliser.)

### M5 — 24 Q5, la règle livre la moitié de la clé
- Supprimer la première ligne (« القاعدة: … جداؤهما 1 »). Nouvel énoncé : « نعلم أنّ:\na = 3 − 2√2\nb = 3 + 2√2\nab = 1\nأيّ الاستنتاجات التالية صحيح ؟ ». Options et explication inchangées.

### M6 — 25 Q2, une option contredit la règle, « ab = 1 » deux fois
Correctif (clé en a) :
- Énoncé : « بعد تبسيط الجذور صار العددان:\na = 2 + √3\nb = 2 − √3\nكم يساوي جداؤهما ab ؟ »
- Options : a « 1 » clé ; b « 4 − √3 » (difference-carres-second-terme-non-eleve-au-carre) ; c « 7 » (difference-carres-somme-au-lieu-de-difference) ; d « −5 » (racine-et-carre-confondus).
- Explication : « الجداء من الشكل (u + v)(u − v) = u² − v² مع u = 2 و v = √3: ab = 2² − (√3)² = 4 − 3 = 1 ✓ لأنّ (√3)² = 3؛ ومنه a و b مقلوبان لأنّ جداءهما 1. الخطأ الشائع جمع المربّعين بدل طرحهما فيخرج 4 + 3 = 7؛ أو كتابة (√3)² = 3² = 9 فيخرج 4 − 9 = −5؛ أو طرح √3 دون تربيعه فيخرج 4 − √3. »
- La conclusion officielle 2b (« مقلوبان ») passe dans l'explication et dans l'énoncé de Q6. (Ne pas utiliser « نعتبر العددين … ما قيمة الجداء » : paire proche 0,59 avec 17/11 Q4.)

### M7 — 26 Q4, le rappel désigne l'ensemble correct
Correctif (clé {a, b} inchangée) :
- Énoncé : « نبحث عمّا يربط العددين:\na = √5 + 2\nb = √5 − 2\nاختر كلّ الكتابات الصحيحة. » (sans le rappel).
- Option d : « a/b = 1 » devient **« ab = 9 »** (somme des carrés au lieu de la différence).
- Explication : « نحسب أوّلًا الجداء بالمتطابقة (u + v)(u − v) = u² − v² مع u = √5 و v = 2: ab = (√5)² − 2² = 5 − 4 = 1، لا 5 + 4 = 9. وبما أنّ جداء العددين يساوي 1 فإنّ كلًّا منهما مقلوب الآخر: 1/b = a و 1/a = b ✓. أمّا a + b = 2√5 فلا يساوي 0 (المقابلان هما اللذان مجموعهما 0)؛ وأمّا 1/a = −b فتعني ab = −1 لا ab = 1، فهي خاطئة. »
- (Sans rappel et sans autre changement : paire proche à 0,48 avec 25 Q3 : ne pas utiliser la version « نعتبر العددين … ».)

## Défauts mineurs
- m1. Étiquette racine-distribuee-sur-somme sur une fusion par différence (21 Q1 b : √200 − √8 = √192 ; 24 Q1 b : √50 − √18 = √32 ; 25 Q1 c ; 26 Q3 c). Usage établi sur main (03/17 Q2 b) : laissé. Recommandé : élargir le libellé du registre « … sur une somme ou une différence, dans un sens comme dans l'autre ».
- m2. Deux étiquettes à retirer : 22 Q3 d « A = B − 1/4 » porte reponse-a-l-autre-inconnue (erreur = soustraction inversée 1/4 − 1/2) ; 25 Q4 a « 1 » porte operation-inverse-appliquee (option ambiguë : a²b² ou ab = 1 rappelé depuis Q2).
- m3. 22 Q3, mécanisme faux dans l'explication : « (√2/2)² = 1/4 (نسيان تربيع الجذر) » ne produit pas 1/4 (on obtiendrait √2/4). Remplacer par : « الخطأ الشائع الاكتفاء بتطابق الحدّين x² و −√2 x في العبارتين والحكم بأنّ A = B دون مقارنة الحدّين الثابتين 1/2 و 1/4 ».
- m4. 22 Q5, l'énoncé donne l'étape clé de 2b (pose la réécriture (x − √2/2)² − (1/2)² ; l'option d « (x − 1/2)² » n'est plausible que depuis la forme développée). Énoncé : remplacer « − (1/2)² » par « − 1/4 ». Explication : la faire précéder de « نكتب 1/4 = (1/2)² فتصير B = (x − √2/2)² − (1/2)² فرقَ مربّعين. »
- m5. 25 Q5, une formule par ligne. Nouvel énoncé : « نعتبر العبارة التالية حيث a و b عددان حقيقيّان:\na² − b(a − b)\nما صورتها المنشورة ؟ »
- m6. 25 Q6, options muettes qui méritent une étiquette existante (optionnel) : 14 → math.alg.reponse-a-l-autre-inconnue (résultat intermédiaire a² + b²) ; 15 → math.num.operation-inverse-appliquee (ab ajouté au lieu d'être retranché).
- m7. 26 Q6, la clé 4 est la donnée « a − b = 4 » de l'énoncé. Optionnel : retirer « وأنّ:\na − b = 4 ». Attention, la paire avec 24 Q5 monte alors à 0,43, juste sous le seuil.
- m8. Étage : 21, 22, 23 relèvent bien de d3 ; 24 et 26 relèvent plutôt de d2 (practice 75/15, ⭐⭐), seule leur dernière question enchaîne deux faits ; 25 limite. 24 Q3 et 26 Q2 de niveau d1 (sans fuite). 26 Q5 doit rester d2 (son énoncé montre les clés de Q1 et de Q3).

## Observations (sans action)
O1 fidélité : aucune sous-question perdue (26 perdait 3a, que M7 rétablit). O2 doublons acceptables (données imposées par les annales). O3 24 Q5 grille 2×2. O4 rendu dans les explications : 35/38 placent un point ou une « ( » de parenthèse arabe dans un run isolé (même taux sur les missions publiées 75/79 : chantier corpus). O5 23 Q4 : option a contredit l'ordre visible (distracteur faible inhérent).

## Étiquettes
70 options étiquetées, 29 identifiants distincts, tous présents sur main ; 35 distracteurs muets ; aucune clé étiquetée ; 5 options de #601 exactes (21 Q4 b, 24 Q1 a, 25 Q1 a, 26 Q2 c, 26 Q6 b). Correctifs M3 et M6 posent trois étiquettes existantes.
- **À créer : math.num.comparaison-radicaux-partie-par-partie** (compétence math.num.ordre-encadrement) : 21 Q2 b (radicandes seuls) et 21 Q2 c (coefficients seuls) + sur main muettes 17/09 Q3 c (« لأنّ 2 < 3 ») et 17/16 Q3 d (« لأنّ √3 > √2 ») = 4 options, 3 questions distinctes, 2 chapitres. fr : « Tu compares deux radicaux en ne regardant que les coefficients, ou que les nombres sous la racine : compare leurs CARRÉS » ; en : « You compare two radicals by looking only at the coefficients, or only at the numbers under the root: compare their SQUARES » ; ar : « تقارن عددين جذريّين بالنظر إلى المعاملين وحدهما أو إلى ما تحت الجذرين وحده: قارن مربّعيهما ».
- À ne pas créer : math.frac.reduction-terme-numerateur-oublie (une seule option, ambiguë, remplacée par M3 ; main étiquette déjà cette erreur distribution-partielle : 03/20 Q2 a).

## Règle « inverses » dans les énoncés
Nulle part nécessaire (seul l'inverse 1/x est enseigné en 16 et 17). Là où elle est écrite, elle livre la clé (23 Q2, 26 Q4) ou une moitié (24 Q5) ; en 25 Q2 elle ne va que dans un sens et une option la contredit. Si on veut qu'elle soit enseignée : dans un cours (17 ou 03), hors tranche.

## Programme, rendu, titres, rampes, gates
Programme : tout est enseigné en 03 ou avant. Rendu : 188 champs passés dans splitMathRuns, 0 run isolé fautif ; aucun chiffre arabo-indien/LaTeX/décimale de vérification/renvoi positionnel/méta-option. Titres conformes (« (تقني) » pour 24, 25, 26). En-têtes d3 boss 120/30 displayOrder 21 à 26. Rampes non décroissantes. Gates (copie de main + fichiers) : content:check vert (1601 questions, 632 étiquettes), qa --strict 0 erreur, tranche 0 clé la plus longue, aucune paire proche touchant 21–26 (avec ou sans les correctifs).

## Chiffre final
38 questions (35 QCM, 2 multi, 1 numeric) re-résolues à l'aveugle ; clés fausses 0 ; défauts 0 critique, 7 majeurs, 8 mineurs ; à reprendre : 7 majeurs (21 Q6, 22 Q6, 23 Q1, 23 Q2, 24 Q5, 25 Q2, 26 Q4) + 4 retouches (22 Q3, 22 Q5, 25 Q4, 25 Q5) ; en option 25 Q6, 26 Q6 et l'étage de 24 et 26.
