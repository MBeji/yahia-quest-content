# Audit B5 — maths 6ᵉ, chapitres 20, 21, 23 et 25 (neuf) — auditeur indépendant, opus

> Valide pour `content/math-6eme/{20,21,23,25}-*` (cours, résumé, quiz, exercices **01–05**) tels qu'au commit
> `bbb33ffe` (branche `wip/maths-6eme-un-passage` ; dernier commit qui touche ces fichiers : `be50aee6` ; aucun
> changement non commité au moment de l'audit). Les fichiers `06-…` et suivants (missions en cours d'écriture) sont
> **hors périmètre** et leurs erreurs de gate ignorées. Ré-auditer si ces fichiers bougent. 2026-10-20.
>
> Le rapport est écrit chapitre par chapitre ; la synthèse et le verdict sont en fin de fichier. « Q1 » désigne la
> première question du fichier. Dans les remplacements, les options sont listées a…d dans l'ordre, **(clé)** marque la
> bonne réponse et « muette » une option sans `misconceptionTag`. J'ai recalculé toutes les valeurs. Aucune clé
> proposée n'est strictement la plus longue, et aucun nombre groupé (`\d \d{3}`) n'y figure.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : **0 erreur et 0 avertissement dans le lot 01–05.** Les 13 erreurs NBSP signalées
  (dont `20/06-exam-2025-…`) et les avertissements des ch. 14 et 16 sont hors périmètre.
- `content:figures:check` ✓.
- `content:tranche --chapters <4 slugs> --fresh --strict-longest --strict-lessons` ✓. Clé strictement la plus longue :
  0/105. Patron de notion : 0 en recul. Positions des clés « fraîches » : a 19 % · b 39 % · c 28 % · d 14 %. Le ch. 25
  est à **b 58 %** (18/31), ce qui est mineur puisque l'ordre est mélangé à l'affichage (point signalé par l'auteur).
- **Sans `--fresh`** (232 questions) : clé la plus longue 13/198 = 7 %, toutes sur des questions anciennes. **54 paires
  proches** : 0 au ch. 25 (neuf), 4 au ch. 20, ~24 au ch. 21, ~16 au ch. 23 (les autres touchent les `06+`). Les plus
  fortes : 21 `quiz` Q5 ↔ `03` Q5 (**1,00**, identiques) ; 23 `quiz` Q3 ↔ `03` Q5 (0,91) ↔ `01` Q4 (0,82) ; 21 `02` Q6 ↔
  `03` Q2 (0,82, miroir) ; trois **miroirs** au ch. 23 (même cube, latérale/totale inversées) ; 21 `01` Q5 ↔ `05` Q5
  (0,69, **même cercle, même clé 43,96**). Le traitement est fait par chapitre ci-dessous. Les paires restantes (même
  savoir-faire avec d'autres données, par exemple aire de disques de rayons 3, 4, 6) sont des exercices parallèles que je
  justifie.
- **Rendu.** Les 4 cours et 4 résumés passent par `renderLesson`/`renderSummary` (vitest jetable, supprimé ; `git status`
  du moteur propre), puis par Chromium (`/opt/pw-browsers/chromium-1194`) à 360 px, avec la règle de cellule
  `unicode-bidi: plaintext`. Aucun débordement (`scrollWidth` = 360), aucun `:::` brut. Les figures sont toutes rendues
  (11/10/14/8 dans les cours, 84 dans les questions). Les `<details>` (vérifie) sont 9/9/8/6, un par section. Les
  tableaux sont lisibles. Chaque figure a été **re-vérifiée contre son énoncé** (coordonnées, proportions, codage) :
  aucune figure fausse. Il y a deux défauts mineurs de lisibilité (m20-6).
- **Notation** : 0 chiffre arabe-indien, 0 groupe `\d \d{3}` dans le lot, 0 LaTeX, 0 `،` dans une notation. Les
  étiquettes latines « cm / m / m² » de quelques figures sont conformes à `course-figures.md` (unités SI dans le dessin).
- **Longueurs** : toutes les sections font entre 32 et 46 lignes de prose (aucune au-delà de 60). Nombre de sections :
  9 / 9 / 8 / 6.

## Points imposés

- **M2 (couronne, ch. 21)** : **tenu**. La section 🍩 suit le patron complet (ancrage → définition → figure vraie 6/4 →
  exemple → piège « largeur prise pour rayon » → propriété avec sens inverse → vérifie). Le mot officiel الإكليل est
  employé. C'est testé par `quiz` Q6, `02` Q9 et `04` Q3 (reprise L46 ex. 10, juste). Seul défaut : `quiz` Q6 redonne
  l'exemple du cours (M21-1).
- **Volume ⛔ (ch. 23)** : **le cours et les questions sont tenus.** Aucune formule, aucune unité cube, aucun
  dénombrement de cubes. Le piège « 40 × 20 × 25 = 20 000 » parle de « مقدارًا آخر ستدرسه في السنوات القادمة » sans nommer
  le volume, ce qui est acceptable. **En revanche, l'étiquette affichée à l'élève fuit** : `math.mes.volume-utilise-comme-aire`
  (7 options + `coursePitfalls`) dit « تعطي حجمًا … والحجم بـ cm³ ». Le mot حجم et l'unité cm³ sont ⛔ et en caractères
  latins (M23-1). Même défaut au ch. 21 : `math.mes.rayon-non-eleve-au-carre` montre « حجم الأسطوانة πr²h » (M21-3).
- **Ch. 21 à 9 sections — avis : garder les 9, ne pas scinder.** Chaque section reste dans la bande R-13 (32–39 lignes).
  Le dépassement de « ~8 notions » vient de l'ajout arbitré M2 (الإكليل) et de deux notions courtes et distinctes (🆚
  objet dessiné, ⚖️ choix de la formule) dont le chapitre a besoin dans cet ordre. Une scission couperait le chapitre au
  milieu des formules du disque. Si un jour il faut réduire, la seule fusion défendable est ⚖️ dans 🧩/🚲, et ce
  n'est pas nécessaire.
- **21 `02-boss` Q5 (« أيّ مقدار يخصّ القرص ؟ »)** : confirmé, **majeur** sans être bloquant. La seule réponse est
  « المساحة », mais « نصف القطر » appartient aussi au disque (le cours le dit), et c'est le marqueur « فقط », porté par
  deux distracteurs seulement, qui les écarte : un indice de forme. « الزاوية » est un remplissage. C'est aussi la 3ᵉ
  copie de la question cercle/disque (`01` Q6, `04` Q6). Remplacement en M21-2.
- **M3 (somme des angles)** : sans objet dans ce lot ; elle n'est ni énoncée ni demandée.
- **Défaut dominant recherché systématiquement** (question qui redonne un exemple, un piège ou un `verifie` du cours) :
  **18 cas** (ch. 20 : 1, ch. 21 : 11, ch. 23 : 4, ch. 25 : 2). La cause est la même qu'en B4 : le cours prend les
  nombres des items existants ou ceux du manuel, et la question garde ces nombres. Pour chaque cas j'ai choisi le remède
  le moins coûteux (changer un `verifie` du cours, ou écrire une variante). Une variante **perd le champ `manuel`** si
  elle en portait un.

---

## Ch. 20 — `20-aires-polygones` (55 questions re-résolues)

**Clés : 55/55 justes**, aucune lettre ni ordinal dans les explications. Le cours a été re-résolu en entier (15 et 16 ;
1 600 sm² et 0,16 m² ; 4 100 m² et 0,41 ha ; 600 et 75 vaches ; 48 ; 2 400 et 50 × 48 ; 19,5, 224,250 et 1 121,250 ;
12 m, 7, 70, 50, 15 ; 480 et 720 ; 4 400 m² = 44 آر). Tout est juste. Les 11 figures sont vraies : obtusangle de pied
extérieur, découpage du parallélogramme, losange inscrit 80 × 60, trapèze partagé, hexagone.

**Reprises.** `04` (L38 ex. 1, L33 ex. 12, L41 ex. 5, L38 ex. 6) et `05` (L2 ex. 1, L33 ex. 7, L33 ex. 3, L38 ex. 3) sont
fidèles à la fiche, avec les errata 38, 51, 52 appliqués. Exclusions respectées : pas de disque, pas de Pythagore.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (9 sections, T1 → T2 → T3 → T4 → T5 → T6 → T7 → retenir) ;
- exhaustivité ✓ (fiche §2 septies points 1–5 enseignés ; le losange est maintenant **testé** : quiz Q7, `02` Q7, `04` Q10) ;
- expérience ✓ ;
- illustration ✓.

### Majeurs

**M20-1 — 1 question redonne le cours, 4 sont des doublons (même calcul ou même question).**

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `01` Q1 | ancrage § 🧱 mot pour mot : 5 × 3 = 15, avec ses deux pièges 16 et 53 | « مستطيلٌ طولُه 8 سم وعرضُه 3 سم. ما مساحتُه؟ » · SVG : `<rect x="40" y="30" width="90" height="54"` → `<rect x="30" y="34" width="120" height="45"` ; 1er `<text x="85" y="19"` → `x="90" y="25"`, contenu `8 سم` ; 2e `<text x="55" y="61"` → `x="60" y="61"` (le libellé ne chevauche plus le bord) · a `24 سم²` (clé) · b `11 سم²` (`math.mes.aire-et-perimetre-confondus`) · c `22 سم²` (même étiquette) · d `83 سم²` (`math.num.chiffres-juxtaposes-au-lieu-du-produit`) · exp. « مساحةُ المستطيل = الطول × العرض = 8 × 3 = 24 سم². أمّا 8 + 3 = 11 و 2 × (8 + 3) = 22 فأطوال حول الشكل، و83 كتابةٌ للعددين جنبًا إلى جنب لا جداؤهما. » |
| `01` Q9 | même calcul que `01` Q6 (6 × 4 ÷ 2 = 12, mêmes distracteurs 10 et 24) | énoncé « … علمًا أنّ ب ج = 7 سم … » · SVG : `L275 150` → `L300 150` (2 fois), `cx="275"` → `cx="300"`, `<text x="275" y="172"` → `x="300"`, `<text x="200" y="174" …>6<` → `x="212" …>7<` · a `11 سم²` (`aire-et-perimetre-confondus`) · b `14 سم²` (clé) · c `17,5 سم²` muette · d `28 سم²` (`math.mes.aire-triangle-sans-moitie`) · exp. « القاعدة ب ج = 7 والارتفاع 4 (قدمه خارج المثلّث على امتداد القاعدة، وهذا لا يغيّر الصيغة): المساحة = (7 × 4) ÷ 2 = 14 سم². الضلع المائل 5 ليس عموديًّا على القاعدة فلا نستعمله؛ ومن استعمله وجد (7 × 5) ÷ 2 = 17,5. » |
| `03` Q8 | même calcul et mêmes distracteurs que `04` Q1 (12 × 5 ÷ 2 = 30 ; 60 ; 17) | SVG : `L60 75 Z` → `L60 15 Z` (2 fois), `cy="75"` → `cy="15"`, `<text x="40" y="116" …>5<` → `y="86" …>9<`, `<text x="166" y="104" …>13<` → `y="74" …>15<` · a `21 سم²` (`aire-et-perimetre-confondus`) · b `54 سم²` (clé) · c `90 سم²` muette · d `108 سم²` (`aire-triangle-sans-moitie`) · exp. « في المثلّث القائم ضلعا الزاوية القائمة 12 و 9 هما قاعدة وارتفاع كلّ منهما للآخر: المساحة = (12 × 9) ÷ 2 = 108 ÷ 2 = 54 سم². الضلع 15 مائل على الضلعين فليس ارتفاعًا؛ ومن ضربه في 12 وجد (12 × 15) ÷ 2 = 90، ومن نسي القسمة على 2 وجد 108. » |
| `01` Q4 | doublon de `quiz` Q4 (0,62 ; même énoncé, mêmes 3 options) | « مثلّث ومتوازي أضلاع لهما القاعدة نفسها والارتفاع نفسه. كيف تقارن مساحتيهما؟ » · a `مساحة المثلّث نصف مساحة متوازي الأضلاع` (clé) · b `المساحتان متساويتان` (`math.mes.aire-triangle-sans-moitie`) · c `مساحة المثلّث ضعف مساحة متوازي الأضلاع` (`math.mes.aire-division-par-deux-appliquee-a-tort`) · d `لا يمكن المقارنة دون معرفة الأضلاع المائلة` muette · d1 · exp. « مساحة متوازي الأضلاع = القاعدة × الارتفاع، ومساحة المثلّث = (القاعدة × الارتفاع) ÷ 2: فالمثلّث نصف متوازي الأضلاع الذي له القاعدة نفسها والارتفاع نفسه، ولا دور للأضلاع المائلة. » |
| `05` Q1 | doublon de `quiz` Q1 (unité de référence, mêmes options) | « أيُّ هذه القياسات قيسُ مساحة؟ » · a `12 سم²` (clé) · b `12 سم` (`aire-et-perimetre-confondus`) · c `12 ل` muette · d `12 كغ` muette · d1 · exp. « المساحة تُقاس بوحدة مربّعة مثل سم²؛ أمّا السنتيمتر فوحدة طول، واللتر وحدة سعة، والكيلوغرام وحدة كتلة. » |

**M20-2 — `competencies` absent de 21 des 55 questions** (toutes les nouvelles). Les chapitres B1–B4 en ont 100 %. À
ajouter : `["math.mes.aires"]`. Le défaut est le même dans les quatre chapitres du lot (voir la synthèse).

### Mineurs

- **m20-1** — `03` Q7, option `25 000 هكتار` : deux erreurs (sens inversé ET facteur 10), elle doit donc être muette.
- **m20-2** — `04` Q8, le distracteur `1 200 م²` n'est expliqué nulle part. Mettre `9 600 م²` (le double de la grande
  aire, 2 × 4 800) muette, ou dire d'où vient 1 200.
- **m20-3** — `05` Q9 (reprise de L33 ex. 3) pose exactement la question d'ancrage de § 📐, que la propriété résout en
  toutes lettres (« لهذا تعذّر الحساب في التمرين … »). Ce n'est pas un calcul redonné, mais c'est du rappel pur. À
  accepter, ou à passer en d2.
- **m20-4** — Gabarit « terrain moins maison carrée, réponse en آر » trois fois : `verifie` § 🧩 (80 × 60 − 20²),
  `02` Q9 (24 × 15 − 6²) et `04` Q7 (L38 ex. 1). Les données diffèrent, c'est justifié comme exercice parallèle.
- **m20-5** — `02-boss` : la difficulté n'est pas monotone (Q6 d2 après Q5 d3). Ancien.
- **m20-6** — Rendu : dans `01` Q1 (corrigé ci-dessus) et `03` Q2 (ancien), le libellé « 3 سم » / « 4 سم » chevauche le
  bord gauche du rectangle. Pour `03` Q2 : `<text x="55"` → `x="62"`.

---

## Ch. 21 — `21-cercle-disque` (54 questions re-résolues)

**Clés : 54/54 justes.** Le cours a été re-résolu (188,4 ; 376,8 ; 47,1 → 15 ; 113,04 ; 78,5 ; 176,625 ; 530,66 ; 314 ;
62,8 et 314 ; 12,56/12,56 ; 6,57, 3,14 et 5,14 ; 47,1 et 235,5 ; 12,56, 6,28 et 14,28 ; 62,8 ; 12,56 = 62,8/5 ; 6 m ;
75,36). Tout est juste. Les 10 figures sont vraies : déroulé ≈ 3,1 d, roue ≈ 3,17 d, porte 2 × 2,5, couronne 6/4.

**Reprises.** `03` (L20 ex. 6, 9) et `04` (L46 ex. 10, L20 ex. 8 avec erratum n° 21 « قوس », L46 ex. 9 réduit à l'aire,
L20 ex. 11) sont confrontés au PDF ص 135 et à la fiche : données justes. La coquille 92,4 de L20 ex. 2 n'est pas
reprise ✓.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (9 sections au patron ; dans § 📏, la figure d'ancrage précède la définition, ce qui est admis) ;
- exhaustivité ✓ (points inside/outside, sens inverse depuis le périmètre et depuis l'aire, demi, quart, ¾, couronne) ;
- expérience ✓ ;
- illustration ✓.

### Majeurs

**M21-1 — 11 questions redonnent un exemple, un piège, une propriété ou un `verifie` du cours.** Deux d'entre elles se
règlent dans le cours (voir M21-1 bis).

| fichier · Q | ce qu'elle redonne | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q6 | ancrage § 🍩 (rayons 4 et 6) et son piège (« 3,14 × 2 × 2 », largeur 2) | énoncé « حوض مستدير نصف قطره 3 م يحيط به رصيف مستدير نصف قطره الخارجي 7 م. كيف نحسب مساحة الرصيف (الإكليل)؟ » · SVG : 2e cercle `r="63"` → `r="41"` · option c → `π × 4 × 4 لأنّ عرض الرصيف 4 م` · exp. : « …وعرض الرصيف 2 م… » → « …وعرض الرصيف 4 م… » ; le reste est inchangé, la clé reste a |
| `01` Q9 | `verifie` § 🧭 (س/ع/ل sur, dans, hors de la dichotomie, mêmes lettres) | « دائرة مركزها م وقطرها 10 سم. النقطة هـ تبعد 5 سم عن م، والنقطة ك تبعد 8 سم، والنقطة ن تبعد 10 سم. أيّ النقاط تقع على الدائرة؟ » · a `هـ وحدها` (clé) · b `ن وحدها` (`math.geo.rayon-et-diametre-confondus`) · c `ك وحدها` muette · d `ك و ن معًا` muette · exp. « نصف القطر 10 ÷ 2 = 5 سم، والنقطة على الدائرة إذا كان بعدها عن المركز يساوي نصف القطر بالضبط: هـ وحدها. ك (8 سم) و ن (10 سم) خارجها؛ ومن أخذ 10 نصفَ قطر خلط بين القطر ونصف القطر. » |
| `02` Q2 | propriété § 🚲 (« نصف قطرها 5 سم محيطها 31,4 ») et 1re boîte de l'ancrage π (d = 10) | « ما محيطُ دائرةٍ نصفُ قطرها 12 سم؟ (π ≈ 3,14) » · a `75,36 سم` (clé) · b `37,68 سم` (`math.geo.perimetre-cercle-facteur-deux-omis-ou-en-trop`) · c `452,16 سم` (`math.geo.formules-cercle-perimetre-et-aire-confondues`) · d `24 سم` (`math.geo.facteur-pi-omis`) · exp. « المحيط = 2 × π × ر = 2 × 3,14 × 12 = 75,36 سم. من نسي العدد 2 وجد 37,68، ومن حسب 3,14 × 12 × 12 وجد 452,16 وهي مساحة القرص، ومن توقّف عند 2 × 12 = 24 نسي π. » |
| `02` Q4 | cas limite § ⚖️ (ر = 2 : 12,56 سم et 12,56 سم², y compris l'option « 12,56 سم ») | « ما مساحةُ قرصٍ نصفُ قطره 0,5 سم؟ (π ≈ 3,14) » · a `0,785 سم²` (clé) · b `3,14 سم²` (`formules-cercle-perimetre-et-aire-confondues`) · c `1,57 سم²` (étiquette de M21-3) · d `0,25 سم²` (`facteur-pi-omis`) · exp. « مساحة القرص = π × ر × ر = 3,14 × 0,5 × 0,5 = 3,14 × 0,25 = 0,785 سم². من حسب 2 × 3,14 × 0,5 = 3,14 أخذ صيغة المحيط، ومن ضرب في ر مرّة واحدة وجد 1,57، ومن نسي π وجد 0,25. » |
| `02` Q6 | piège § 📏 mot pour mot (« قطر 14 → ر = 28 خطأ، 7 »), miroir de `03` Q2 (0,82) | « دائرةٌ قطرُها 18 سم. ما طولُ نصف قطرها؟ » · a `9 سم` (clé) · b `36 سم` (`rayon-et-diametre-confondus`) · c `18 سم` (même étiquette) · d `4,5 سم` muette · exp. « نصفُ القطر = القطر ÷ 2 = 18 ÷ 2 = 9 سم: المركز يقسم القطر إلى نصفين. من ضاعف وجد 36، ومن أعاد القطر نفسه وجد 18. » |
| `04` Q2 | exemple § 🧩 (ر = 5 → 78,5) avec ses deux pièges 15,7 et 25 | « قرصٌ قطرُه 18 سم. ما مساحتُه؟ (π ≈ 3,14) » · a `254,34 سم²` (clé) · b `56,52 سم²` (`formules-cercle-perimetre-et-aire-confondues`) · c `28,26 سم²` (étiquette de M21-3) · d `81 سم²` (`facteur-pi-omis`) · exp. « نصف القطر 18 ÷ 2 = 9 سم، فالمساحة = 3,14 × 9 × 9 = 3,14 × 81 = 254,34 سم². من حسب 3,14 × 18 وجد 56,52 وهو محيط الدائرة، ومن ضرب في ر مرّة واحدة وجد 28,26، ومن نسي π وجد 81. » |
| `05` Q3 | piège § 🧩 (cercle d'Amal ر = 7,5 : 47,1 / 176,625) et cas limite § 🚲 (47,1 → 15) | « ما محيطُ دائرةٍ قطرُها 13 سم؟ (π ≈ 3,14) » · a `20,41 سم` (`rayon-et-diametre-confondus`) · b `40,82 سم` (clé) · c `81,64 سم` (`perimetre-cercle-facteur-deux-omis-ou-en-trop`) · d `132,665 سم` (`formules-cercle-perimetre-et-aire-confondues`) · exp. « المحيط = π × القطر = 3,14 × 13 = 40,82 سم. من ضرب أيضًا في 2 وجد 81,64، ومن أخذ نصف القطر 6,5 في π × ق وجد 20,41، ومن حسب مساحة قرص نصف قطره 6,5 وجد 132,665. » |
| `05` Q9 | cas limite § ⚖️ mot pour mot (ر = 2, 12,56 = 12,56) | « قرص نصف قطره 8 سم. ماذا نجد لمحيط دائرته ولمساحة قرصه؟ (π ≈ 3,14) » · a `المحيط 50,24 سم والمساحة 200,96 سم²` (clé) · b `المحيط 200,96 سم والمساحة 50,24 سم²` (`formules-cercle-perimetre-et-aire-confondues`) · c `المحيط 25,12 سم والمساحة 200,96 سم²` (`perimetre-cercle-facteur-deux-omis-ou-en-trop`) · d `المحيط 50,24 سم والمساحة 25,12 سم²` (étiquette de M21-3) · exp. « المحيط = 2 × 3,14 × 8 = 50,24 سم، والمساحة = 3,14 × 8 × 8 = 200,96 سم². من بدّل الصيغتين وضع كلّ عدد مكان الآخر، ومن نسي العدد 2 وجد للمحيط 25,12، ومن ضرب في ر مرّة واحدة وجد للمساحة 25,12. الوحدة تشهد: سم للمحيط و سم² للمساحة. » |
| `01` Q5 | **même cercle et même clé** que `05` Q5 (d 14 = ر 7 → 43,96 ; distracteur 21,98 commun) | « ما محيطُ دائرةٍ قطرُها 19 سم؟ (π ≈ 3,14) » · a `22,14 سم` muette · b `29,83 سم` (`rayon-et-diametre-confondus`) · c `59,66 سم` (clé) · d `119,32 سم` (`perimetre-cercle-facteur-deux-omis-ou-en-trop`) · exp. « المحيط = π × القطر = 3,14 × 19 = 59,66 سم. من ضرب أيضًا في 2 وجد 119,32، ومن أخذ نصف القطر 9,5 في π × ق وجد 29,83، ومن جمع 19 مع 3,14 وجد 22,14. » |
| `04` Q4 | `verifie` § 🔮 (d = 8 → 25,12) | **réglé dans le cours** (M21-1 bis a) ; la question est conservée |
| `03` Q6, `02` Q3 | `verifie` § ⚖️ (ر = 3 : 18,84 et 28,26 ; `03` Q6 reprend même l'option 18,84) | **réglé dans le cours** (M21-1 bis b) ; les questions sont conservées |

**M21-1 bis — trois `verifie` du cours à renuméroter, et le résumé à recaler sur le piège du cours.**

- a) § 🔮 : « لففنا حول قاعدة علبةٍ قطرها 8 سم خيطًا طوله 25,12 سم. » → « …قطرها 9 سم خيطًا طوله 28,26 سم. » ; et
  « 25,12 ÷ 8 = 3,14، لأنّ 8 × 3,14 = 25,12. » → « 28,26 ÷ 9 = 3,14، لأنّ 9 × 3,14 = 28,26. »
- b) § ⚖️ : « قرصٌ نصف قطره 3 سم. » → « قرصٌ نصف قطره 3,5 سم. ». Réponse : « المحيط = 2 × 3,14 × 3,5 = 21,98 سم، لأنّه طول
  الحافّة فنضرب نصف القطر في 2 ثمّ في π. المساحة = 3,14 × 3,5 × 3,5 = 38,465 سم²، لأنّها قيس السطح فنضرب نصف القطر في
  نفسه ثمّ في π. »
- c) § 🚪 : le `verifie` ر = 4 calcule en route « 3,14 × 4 × 4 = 50,24 », c'est-à-dire `05` Q6 avec ses distracteurs. On
  passe à ر = 2 : « ربعُ قرصٍ نصف قطره 2 سم… » → « القرص الكامل 3,14 × 2 × 2 = 12,56 سم²، وربعه 12,56 ÷ 4 = 3,14 سم².
  الدائرة الكاملة 2 × 3,14 × 2 = 12,56 سم، فالقوس 12,56 ÷ 4 = 3,14 سم. ومحيط ربع القرص يضيف نصفَي القطر اللذين يحدّانه:
  3,14 + 2 + 2 = 7,14 سم. ». Le résultat rappelle la leçon des unités : même nombre, sm et sm².
- d) `resume.md`, puce « القطر » : « ر = 7 سم ⟵ ق = 14 سم لا 3,5 » invente le sens inverse du piège et redonne `03` Q2. →
  « ق = 14 سم ⟵ ر = 7 سم لا 28 », qui est le piège du cours (bijection).

**M21-2 — doublons et question bancale.**

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `02` Q5 | voir « Points imposés » : « فقط » est un indice de forme, « الزاوية » un remplissage, et c'est la 3e copie cercle/disque | « أيّ هذه الأشياء يمثّل قرصًا لا دائرة؟ » · a `سطح قطعة نقديّة` (clé) · b `الخطّ الذي يرسمه البركار على الورقة` (`math.geo.cercle-et-disque-confondus`) · c `حافّة صحن مستدير` (même étiquette) · d `خيط ملفوف حول علبة أسطوانيّة` muette · d2 · exp. « القرص سطحٌ ممتلئ يُغطّي، وسطح القطعة النقديّة كذلك: له مساحة. أمّا خطّ البركار وحافّة الصحن والخيط الملفوف فخطوط منحنية مغلقة لا تملأ شيئًا: هي دوائر، لها محيط لا مساحة. » |
| `03` Q5 | **identique** à `quiz` Q5 (Jaccard 1,00) | « أيّ عمليّة تعطي مساحة قرص نصف قطره 7 سم؟ » · a `3,14 × 7 × 7` (clé) · b `2 × 3,14 × 7` (`formules-cercle-perimetre-et-aire-confondues`) · c `3,14 × 14 × 14` (`rayon-et-diametre-confondus`) · d `3,14 × 7` (étiquette de M21-3) · exp. « مساحة القرص = π × ر × ر: نصف القطر 7 مرّتين و π مرّة واحدة. أمّا 2 × 3,14 × 7 فمحيط الدائرة، و 3,14 × 14 × 14 يضع القطر مكان نصف القطر، و 3,14 × 7 يضرب في ر مرّة واحدة. » |
| `03` Q1 | 3e copie de « قيمة π » (`quiz` Q2, `01` Q4) | « قسمنا محيط دائرة على قطرها. ماذا نجد؟ » · a `3,14 تقريبًا، مهما كانت الدائرة` (clé) · b `عددًا يكبر كلّما كبرت الدائرة` muette · c `2 دائمًا، لأنّ القطر ضعف نصف القطر` muette · d `3,41 تقريبًا` (`math.geo.valeur-de-pi-erronee`) · d1 · exp. « في كلّ دائرة، صغيرةً كانت أو كبيرة، خارج قسمة المحيط على القطر هو العدد نفسه π ≈ 3,14، فلا يتعلّق بحجم الدائرة. و3,41 قلبٌ للرقمين بعد الفاصلة، و2 هو خارج قسمة القطر على نصف القطر لا المحيط على القطر. » |
| `01` Q1 | doublon de `quiz` Q1 (0,69) et 3e « ق = 2 × ر » | « قطعة طرفاها على الدائرة ولا تمرّ بالمركز. هل هي قطر؟ » · a `لا، لأنّها لا تمرّ بالمركز` (clé) · b `نعم، لأنّ طرفيها على الدائرة` muette · c `نعم، إذا كانت أطول من نصف القطر` muette · d `لا، بل هي نصف قطر` (`rayon-et-diametre-confondus`) · d1 · exp. « القطر قطعة تمرّ بالمركز وطرفاها على الدائرة، والشرطان معًا لازمان. هذه القطعة لا تمرّ بالمركز فليست قطرًا، وهي أقصر منه. ولا هي نصف قطر، لأنّ نصف القطر يبدأ من المركز. » |
| `05` Q2 | 5e « نصف قطر → قطر » (`quiz` Q4, `01` Q3, `02` Q1, `03` Q2 ; 0,67) | « نريد رسم دائرة قطرها 9 سم. كم نفتح البركار؟ » · a `4,5 سم` (clé) · b `9 سم` (`rayon-et-diametre-confondus`) · c `18 سم` (même étiquette) · d `3 سم` muette · exp. « فتحة البركار هي نصف القطر، ونصف القطر = القطر ÷ 2 = 9 ÷ 2 = 4,5 سم. من فتح البركار 9 سم رسم دائرة قطرها 18 سم. » |
| `04` Q6 | 3e cercle/disque, trivial pour un défi d3 | « دائرة وقرصها نصف قطرهما 1 م. أيّ جملة صحيحة؟ (π ≈ 3,14) » · a `للقرص مساحة 3,14 م²، ولدائرته محيط 6,28 م` (clé) · b `للدائرة مساحة 3,14 م²، ولقرصها محيط 6,28 م` (`cercle-et-disque-confondus`) · c `للقرص مساحة 6,28 م²، ولدائرته محيط 3,14 م` (`formules-cercle-perimetre-et-aire-confondues`) · d `للدائرة وللقرص مساحة واحدة 3,14 م²` (`cercle-et-disque-confondus`) · exp. « القرص سطح فله مساحة: 3,14 × 1 × 1 = 3,14 م²؛ والدائرة خطّ فلها محيط: 2 × 3,14 × 1 = 6,28 م. ليس للدائرة مساحة لأنّها لا تملأ شيئًا، ومن بدّل العددين خلط بين صيغتي المحيط والمساحة. » |

**M21-3 — l'étiquette `math.mes.rayon-non-eleve-au-carre` est hors programme pour la 6ᵉ.** Elle est affichée à l'élève et
dit « تنسى تربيع نصف القطر: مساحة القرص πr²، فحجم الأسطوانة πr²h لا πrh » : volume du cylindre (⛔) et notation πr² que
le chapitre n'emploie jamais. Elle porte 5 options (`03` Q9 a, `05` Q4 c, `05` Q6 c, `05` Q7 a, et `04` Q2 c avant
remplacement) ainsi que `coursePitfalls`. **À ajouter au registre**, puis à substituer partout dans le ch. 21 :

```json
"math.geo.disque-rayon-une-seule-fois": {"subject": "math", "labels": {"fr": "Tu multiplies π par le rayon une seule fois : l'aire du disque est π × r × r — le rayon deux fois", "en": "You multiply π by the radius only once: the disc area is π × r × r — the radius twice", "ar": "ضربتَ π في نصف القطر مرّةً واحدة: مساحةُ القرص = π × ر × ر، نصفُ القطر مرّتين"}, "competency": "math.geo.cercle"}
```

**M21-4 — `competencies` absent de 24 des 54 questions** (les nouvelles). À ajouter : `math.geo.cercle`, ou
`math.mes.perimetres` / `math.mes.aires` comme dans les anciennes.

### Mineurs

- **m21-1** — `03` Q7, option `78,5 سم` : deux erreurs (5 pris pour rayon ET formule d'aire), elle doit donc être muette.
- **m21-2** — `01` Q7, option `75,36 سم` : c'est « 12 pris pour un rayon ». L'étiquette juste est
  `rayon-et-diametre-confondus`, pas `facteur-deux…`.
- **m21-3** — Clôture : « بقيت المُدَدُ الزمنيّةُ لإتمام برنامج القيس » est faux, puisque les ch. 23 et 25 suivent. →
  « التالي: المُدَدُ الزمنيّة. »
- **m21-4** — `02-boss` : la difficulté n'est pas monotone (Q5 d2 après Q4 d3 ; Q6 « 14 ÷ 2 » étiqueté d3). C'est réglé
  par M21-1 si `02` Q6 passe en d2.
- **m21-5** — Paires parallèles restantes (aires ر = 3/4/6, périmètres d = 4/6/8) : même savoir-faire avec d'autres
  données, c'est justifié.

---

## Ch. 23 — `23-solides-cube-pave` (54 questions re-résolues)

**Clés : 54/54 justes** ; le `multi` `05` Q7 = {a, d} est juste. Le cours a été re-résolu (1 600 ; 0,25 → 1 ; 5 400,
0,54 et 7,560 ; 96 → 4 ; 225, 900 et 1 350 ; 3 000 et 1 500 ; 20 000 ; 4 600 → 0,46 → 6,440 ; 3 800 ; 64 et 94 ; 138 ;
62,5 et 75 ; 110 ; 200 ; 3,06 et 4,26 ; perspective 3 faces, 9 arêtes, 7 sommets visibles). Tout est juste. Les 14
figures sont vraies, et deux points ont été vérifiés au pliage : le dé (2↔5, 1↔6, 3↔4) et le non-patron (le 2e carré
empilé retombe sur le 1er de la rangée).

**Reprises.** `04` Q7–Q8 (L58 ex. 10, PDF ص 168 relu : 104 m², 1 664, 70 boîtes, 2 520 د) et `04` Q9 (L58 ex. 7, ligne 4)
sont fidèles. Les exercices interdits (58-4, 58-6, 58-9) ne sont pas repris ✓.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (8 sections au patron) ;
- exhaustivité : réserve m23-1 ;
- expérience : clôture fausse, m23-2 ;
- illustration ✓.

### Majeurs

**M23-1 — Volume : l'étiquette `math.mes.volume-utilise-comme-aire` nomme le volume.** Son libellé ar « تعطي حجمًا حيث
تُطلب مساحة: المساحة بـ cm² والحجم بـ cm³ » nomme حجم et cm³, qui sont ⛔ et en caractères latins dans un libellé arabe.
Il est montré après chaque erreur sur `quiz` Q5 b, `02` Q4 c, `02` Q5 c, `03` Q6 c, `04` Q2 c, `04` Q4 b, `05` Q5 b, et
il est déclaré dans `coursePitfalls`. Le cours, lui, a pris soin de ne pas nommer le volume. **À ajouter au registre**,
puis à substituer partout dans le ch. 23 :

```json
"math.mes.solide-trois-dimensions-multipliees": {"subject": "math", "labels": {"fr": "Tu multiplies les trois dimensions : ce produit ne mesure aucune surface ; l'aire latérale est le périmètre de la base × la hauteur", "en": "You multiply the three dimensions: that product measures no surface; the lateral area is the base perimeter × the height", "ar": "ضربتَ الأبعاد الثلاثة: هذا الجداء لا يقيس أيّ سطح، والمساحة الجانبيّة = محيط القاعدة × الارتفاع"}, "competency": "math.esp.cube-pave"}
```

Il faut aussi la poser sur les deux produits des trois dimensions qui sont muets aujourd'hui : `03` Q8 `42 سم²` (7 × 3 × 2)
et `04` Q6 `48 سم²` (6 × 4 × 2).

**M23-2 — 4 questions redonnent le cours.**

| fichier · Q | ce qu'elle redonne | remplacement vérifié |
| --- | --- | --- |
| `01` Q8 | cas limite § 🧱 mot pour mot (« قالب أبعاده 8 و 3 و 3 ») | « قالب خشبي له 6 أوجه: وجهان مربّعان ضلع كلّ منهما 4 سم، وأربعة أوجه مستطيلة 10 سم × 4 سم. ما اسمه؟ » (le SVG n'a pas de cote) · options et clé inchangées · exp. : « وهنا أربعة أوجه 8 × 3 » → « وهنا أربعة أوجه 10 × 4 » |
| `01` Q9 | figure du piège § 📦 **identique** (rangée de 4 + 2 carrés empilés sur le 3e) | SVG : `<svg viewBox="0 0 360 160"><g fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"><path d="M70 102 L114 102 L114 146 L70 146 Z"/><path d="M114 102 L158 102 L158 146 L114 146 Z"/><path d="M158 102 L202 102 L202 146 L158 146 Z"/><path d="M202 102 L246 102 L246 146 L202 146 Z"/><path d="M246 102 L290 102 L290 146 L246 146 Z"/><path d="M114 58 L158 58 L158 102 L114 102 Z"/></g></svg>` (rangée de 5 + un carré au-dessus du 2e) · même énoncé · b → `نعم، لأنّ الصفّ يلتفّ حول المكعّب عند الطيّ` · clé d inchangée · exp. « نطوي الصفّ الأفقيّ حول المكعّب: أربعة مربّعات تكفي لتصنع الأوجه الجانبيّة الأربعة، فيسقط المربّع الخامس على الأوّل ويتراكبان. المربّع الذي فوق الصفّ يصير الوجه العلويّ، ويبقى الوجه السفليّ مفتوحًا. ليست كلّ ستّة مربّعات متلاصقة نشرًا، وللمكعّب أكثر من نشر صحيح غير الصليب. » |
| `05` Q7 (`multi`) | exemple § 🧱 mot pour mot (tronc de pyramide « 4 أشباه منحرف », pièce en marche « 8 أوجه ») | « أيّ المجسّمات الآتية يُعدّ متوازي مستطيلات؟ اختر كلّ الصحيح. » · a `علبة أحذية أوجهها الستّة مستطيلات، كلّ وجهين متقابلين متقايسان` · b `قطعة جبن لها 5 أوجه، اثنان منها مثلّثان` · c `علبة لها 6 أوجه: وجهان على شكل معيّن وأربعة مستطيلات` · d `نرد أوجهه الستّة مربّعات متقايسة` · `answerKey.correct` [a, d] · exp. « علبة الأحذية لها 6 أوجه مستطيلة متقايسة مثنى مثنى: متوازي مستطيلات. والنرد حالة خاصّة منه لأنّ المربّع مستطيل. قطعة الجبن لها 5 أوجه فقط. والعلبة الثالثة لها 6 أوجه، لكنّ وجهين منها معيّنان لا مستطيلان: عدد الأوجه وحده لا يكفي. » |
| `01` Q7 | 1re question du `verifie` § ✏️ (« كم حرفًا ترسم متقطّعًا؟ » → 3) | **dans le cours** : « ارسم بالمنظور المائل مكعّبًا طول حرفه 3 سم. كم حرفًا ترسم متقطّعًا؟ وما شكل وجهه العلويّ في رسمك؟ » → « ارسم بالمنظور المائل مكعّبًا طول حرفه 3 سم، واختصر العمق إلى نصفه. ما طول القطع المائلة في رسمك؟ وما شكل وجهه العلويّ؟ » ; réponse : supprimer « نرسم 3 أحرف متقطّعة تلتقي في الرأس المخفيّ. » (le reste dit déjà 1,5 سم et متوازي أضلاع) |

**M23-3 — doublons et miroirs** (le ch. 23 en a le plus : 16 paires).

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `03` Q2 | miroir de `quiz` Q4 (cube 3 : 36 ↔ 54 inversés, 0,73) | « مكعّبٌ طولُ حرفه 1,2 م. ما مساحتُه الجانبيّة؟ » · a `5,76 م²` (clé) · b `8,64 م²` (`math.mes.cube-coefficient-quatre-et-six-echanges`) · c `1,44 م²` (`math.mes.solide-une-seule-face-comptee`) · d `4,8 م²` (`math.mes.arete-non-elevee-au-carre`) · exp. « الجانبيّة = 4 × (الحرف × الحرف) = 4 × (1,2 × 1,2) = 4 × 1,44 = 5,76 م². من ضرب في 6 وجد الجمليّة 8,64، ومن حسب وجهًا واحدًا وجد 1,44، ومن نسي ضرب الحرف في نفسه وجد 4 × 1,2 = 4,8. » |
| `05` Q2 | miroir de `01` Q5 (cube 5 : 100 ↔ 150, 0,73) | « مكعّبٌ طولُ حرفه 1,5 سم. ما مساحتُه الجانبيّة؟ » · a `9 سم²` (clé) · b `13,5 سم²` (`cube-coefficient-quatre-et-six-echanges`) · c `2,25 سم²` (`solide-une-seule-face-comptee`) · d `6 سم²` (`arete-non-elevee-au-carre`) · exp. « الجانبيّة = 4 × (1,5 × 1,5) = 4 × 2,25 = 9 سم². ومن ضرب في 6 وجد 13,5، ومن حسب وجهًا واحدًا وجد 2,25، ومن نسي تربيع الحرف وجد 4 × 1,5 = 6. » |
| `05` Q3 | miroir de `02` Q2 (cube 4 : 64 ↔ 96, 0,73) | « مكعّبٌ طولُ حرفه 8 سم. ما مساحتُه الجمليّة؟ » · a `384 سم²` (clé) · b `256 سم²` (`cube-coefficient-quatre-et-six-echanges`) · c `64 سم²` (`solide-une-seule-face-comptee`) · d `48 سم²` (`arete-non-elevee-au-carre`) · exp. « الجمليّة = 6 × (8 × 8) = 6 × 64 = 384 سم². من ضرب في 4 وجد الجانبيّة 256، ومن حسب وجهًا واحدًا وجد 64، ومن نسي تربيع الحرف وجد 6 × 8 = 48. » |
| `05` Q8 (`numeric`) | **même cube que `05` Q2 et `01` Q5** (150 → 100) ; le champ `manuel` « L58 ex. 7 » du fichier ne couvre qu'une variante | « مكعّب مساحته الجمليّة 0,24 م². ما مساحته الجانبيّة بالمتر المربّع؟ » · `value` 0.16 · exp. « مساحة الوجه 0,24 ÷ 6 = 0,04 م² (وحرفه 0,2 م لأنّ 0,2 × 0,2 = 0,04). والجانبيّة 4 × 0,04 = 0,16 م². التحقّق: 0,16 + 2 × 0,04 = 0,24 ✓. » · **retirer `manuel` de `05-entrainement.json`** : aucune question n'y reprend L58 ex. 7 telle quelle |
| `01` Q4 | 3e « صيغة الجمليّة للمكعّب » (`quiz` Q3, `03` Q5 ; 0,82) | « ما صيغةُ المساحة الجانبيّة للمكعّب؟ » · a `4 × (الحرف × الحرف)` (clé) · b `6 × (الحرف × الحرف)` (`cube-coefficient-quatre-et-six-echanges`) · c `الحرف × الحرف` (`solide-une-seule-face-comptee`) · d `4 × الحرف` (`arete-non-elevee-au-carre`) · exp. « الجانبيّة تجمع الأوجه الأربعة الجانبيّة، وكلّ وجه مربّع مساحته الحرف × الحرف: 4 × (الحرف × الحرف). العدد 6 للجمليّة. » |
| `03` Q5 | même formule (0,91 avec `quiz` Q3) | « المساحة الجمليّة للمكعّب تساوي مساحته الجانبيّة زائد: » · a `مساحة وجهين` (clé) · b `مساحة وجه واحد` muette · c `مساحة أربعة أوجه` muette · d `لا شيء، فهما متساويتان` (`math.mes.aire-laterale-et-totale-confondues`) · exp. « الجانبيّة تضمّ الأوجه الأربعة الجانبيّة، والجمليّة الأوجه الستّة كلّها: الفرق وجهان، هما القاعدتان (6 = 4 + 2). » |
| `01` Q1 | doublon de `quiz` Q1 (mêmes options) | « صندوق مكعّب حرفه 10 سم، نلصق شريطًا على أحرفه كلّها. كم سنتيمترًا من الشريط يلزم؟ » · a `120 سم` (clé) · b `80 سم` (`math.geo.solide-faces-aretes-sommets-confondus`) · c `60 سم` (même étiquette) · d `40 سم` muette · d1 · exp. « للمكعّب 12 حرفًا متقايسة، طول كلّ منها 10 سم، فالشريط 12 × 10 = 120 سم. من عدّ 8 خلط الأحرف بالرؤوس، ومن عدّ 6 خلطها بالأوجه. » |

**M23-4 — `competencies` absent de 25 des 54 questions.** À ajouter : `math.esp.cube-pave`.

### Mineurs

- **m23-1** — `04` Q8 demande d'arrondir à la boîte entière (69,33 → 70). Le cours de 23 ne le dit nulle part (c'est le
  ch. 25, placé **après**, qui l'enseigne). À ajouter à la liste des cas limites de § 🧮 : « - **علب كاملة**: لا نشتري
  جزءًا من علبة، فإذا احتجنا 12,4 علبة اشترينا 13. »
- **m23-2** — Clôture : « بهذا الفصل يكتمل برنامج الهندسة والقيس للسنة السادسة » est faux, puisque les ch. 25 et 26
  suivent (displayOrder 25, 26). → « …وتحسب سطحها وكلفته. التالي: محيط الشكل المركّب — تعود فيه إلى الأشكال المستوية
  لتدور حول حدودها. » (le reste de la phrase est inchangé)
- **m23-3** — Distracteurs muets qui exécutent un piège déclaré : `02` Q4 `50` (6 + 4 non doublé), `03` Q6 `39`, `04` Q4
  `70`. Leur poser `math.mes.perimetre-rectangle-somme-non-doublee`.
- **m23-4** — `03` Q7 d `45 000 د` (aucune conversion) porte `conversion-aire-facteur-errone`, qui dit « par 100 et non
  par 10 ». Ce n'est pas l'erreur exécutée : la rendre muette.
- **m23-5** — `04` Q8 : « بدلاط … دلاطة » → « ببلاط … بلاطة » (le manuel dit بلاطات).
- **m23-6** — `03` Q6 et `05` Q4 (anciens) dessinent un pavé 8 × 5 × 3 / 6 × 3 × 4 comme un cube non coté. À coter ou à
  allonger.
- **m23-7** — Piège non-patron § 📦 : « فوق الثالث … المربّع الأوّل » se compte de gauche à droite, à l'inverse du sens
  de lecture arabe. La figure marque les deux carrés « ? », ce qui lève l'ambiguïté. Préciser « من اليسار » est optionnel.

---

## Ch. 25 — `25-perimetre-figure-composee`, NEUF (35 questions re-résolues)

**Clés : 35/35 justes** ; le `multi` `04` Q6 = {a, b} est juste. Le cours a été re-résolu (40, 56 et 48 ; 40 au coin ;
34 ; 21 ; L de 44 ; 31 ; 5,57, 6,57 et 7,14 ; 30,28 ; 142,8 par deux voies ; ¼ 30,71 ; 103,96 ; 22,28 → 111,4 → 3
rouleaux ; 37,2 → 2 ; 16 et 17 ; 150). Tout est juste. Les 8 figures sont vraies : codage, L proportionné, encoche
concave, coin arrondi convexe, 9 points / 8 intervalles et 8 / 8.

**Programme.** Leçon 24 (ص 67–69) couverte, M4 ✓. Toutes ses notions sont enseignées : côté commun, codage, demi-cercle,
arc ajouté ou retranché, quart, échelle avec arrondi par excès, contour fermé. Prérequis bien placés (ch. 14 échelle,
ch. 21 circonférence, tous avant 25).

**Reprises confrontées au PDF ص 67–69 (relu à l'image).** `02` Q3 (ex. 4 : 110 × 90 → 502,6 ✓), `02` Q4 (ex. 5 : 120 × 60,
arc ajouté et arc creusé → 428,4 ✓), `04` Q2 (ex. 2 : 4,8 / 8, 1/750, carré + losange + demi-disque → 356,52 m → 8
rouleaux ✓) et `04` Q3 (ex. 9 : 17 côtés × 5 m → 170 plants ✓). Pour ce dernier, les losanges du manuel ne sont pas
dessinés à l'échelle, mais « أشكال متقايسة الأضلاع » plus les côtés communs rendent toutes les longueurs égales, donc la
lecture de la fiche tient. La correction de la fiche (16,71 pour l'ex. 7) n'est pas utilisée : `05` Q3 est une variante
(6 sm) sans champ `manuel` ✓.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (6 sections au patron) ;
- exhaustivité ✓ ;
- expérience ✓ ;
- illustration ✓. Le résumé n'a pas de figure (mineur).

### Majeurs

**M25-1 — Les pièges du cours sont mal étiquetés ou pas étiquetés du tout (C-5, et « chaque étiquette nomme EXACTEMENT
l'erreur »).**

- Le piège central (§ 🧵 : côté commun compté) et sa variante (§ 🪟 : diamètre accolé compté) portent
  `math.mes.perimetre-nombre-de-cotes-errone`. Son libellé, « تضرب في عددٍ خاطئ من الأضلاع: للمربّع والمعيّن 4 أضلاع،
  وللمثلّث متساوي الأضلاع 3 », ne parle pas de côté commun : l'élève qui a additionné deux périmètres reçoit un rappel sur
  les côtés du carré. Le diamètre compté est **muet** partout (`quiz` Q4 c, `01` Q4 c, `02` Q3 c d, `03` Q3 c, `05` Q3 c d,
  `05` Q5 c).
- `math.num.arrondi-par-troncature` (`03` Q4 a, `04` Q2 b, `05` Q5 a) dit « الرقمُ الذي يلي رتبةَ التدوير هو الذي يُقرّر
  الصعود ». Appliquée à 2,125, cette règle **donne 2**, c'est-à-dire qu'elle valide l'erreur. Or le cours enseigne
  « toujours l'entier supérieur ». C'est contradictoire.
- Les pièges § ➕➖ (arc creusé retranché : `03` Q6 a, `02` Q5 b) et § 🌱 (+1 plant sur contour fermé : `quiz` Q5 c,
  `01` Q5 c, `02` Q6 d, `04` Q3 c, `05` Q6 b) n'ont aucune étiquette.

**À ajouter au registre** :

```json
"math.mes.perimetre-compose-cote-commun-compte": {"subject": "math", "labels": {"fr": "Tu comptes dans le périmètre le côté commun à deux pièces accolées (ou le diamètre d'un demi-cercle accolé) : il est à l'intérieur de la figure, seul le contour extérieur compte", "en": "You count the side shared by two joined pieces (or the diameter of a joined semicircle) in the perimeter: it lies inside the figure, only the outer outline counts", "ar": "تعدّ في المحيط الضلعَ المشترك بين قطعتين ملتصقتين (أو قطرَ نصف دائرة ملتصقة): هو داخل الشكل، والمحيط هو الحدّ الخارجيّ وحده"}, "competency": "math.mes.perimetres"},
"math.mes.perimetre-arc-retranche-soustrait": {"subject": "math", "labels": {"fr": "Tu retranches la longueur d'un arc creusé dans la figure : l'arc d'une encoche est sur le contour, sa longueur s'ajoute au périmètre comme celle d'un arc ajouté", "en": "You subtract the length of an arc cut into the figure: a notch's arc lies on the outline, so its length is added like an added arc", "ar": "تطرح طولَ قوسٍ مقتطعٍ من الشكل: قوسُ التجويف على الحدّ، فيُجمع طوله في المحيط كالقوس المضاف"}, "competency": "math.mes.perimetres"},
"math.mes.plantation-contour-ferme-plus-un": {"subject": "math", "labels": {"fr": "Tu ajoutes un plant (ou un poteau) sur un contour fermé : le dernier rejoint le premier, il y a autant de plants que d'intervalles", "en": "You add one plant (or post) on a closed outline: the last one meets the first, so there are as many plants as gaps", "ar": "تضيف غرسةً (أو عمودًا) على حدٍّ مغلق: الأخيرةُ تلتقي بالأولى، فعددُ الغرسات يساوي عددَ المسافات"}, "competency": "math.mes.perimetres"},
"math.num.arrondi-par-exces-oublie": {"subject": "math", "labels": {"fr": "Tu arrondis vers le bas alors qu'il faut des objets entiers pour tout couvrir : avoir besoin de 2,1 rouleaux, c'est en acheter 3", "en": "You round down when whole items must cover everything: needing 2.1 rolls means buying 3", "ar": "تدوّر نحو الأصغر والمطلوبُ أشياءُ كاملةٌ تغطّي الكلّ: الحاجةُ إلى 2,1 لفّة تعني شراءَ 3 لفائف"}, "competency": "math.num.ordre-encadrement"}
```

**Substitutions** :
- `cote-commun-compte` remplace `perimetre-nombre-de-cotes-errone` sur `quiz` Q2 c, d ; `01` Q1 c, d ; `01` Q2 c, d ;
  `02` Q1 d ; `03` Q2 c, d ; `05` Q6 c. Il se pose aussi sur les options « diamètre compté » listées ci-dessus.
- `04` Q1 garde `perimetre-nombre-de-cotes-errone` (÷ 6, ÷ 4 : un mauvais nombre de côtés, qui est bien son libellé).
- `arrondi-par-exces-oublie` remplace `arrondi-par-troncature` sur les 3 options concernées.
- Les deux autres étiquettes se posent sur les options listées ci-dessus.
- `coursePitfalls` → `["math.mes.perimetre-compose-cote-commun-compte", "math.mes.perimetre-rectangle-somme-non-doublee",
  "math.mes.perimetre-arc-retranche-soustrait", "math.num.arrondi-par-exces-oublie",
  "math.mes.plantation-contour-ferme-plus-un"]`.

**M25-2 — Redites et gabarits.**

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `03` Q1 | redonne l'étape 3 de l'exemple § 🧵 et le résumé (« la maison : 5 côtés ») ; maison ×4 dans le chapitre | « شكل مكوّن من مستطيل، ألصقنا بكلّ من ضلعيه القصيرين مثلّثًا متقايس الأضلاع من الخارج. كم ضلعًا على الحدّ الخارجيّ للشكل؟ » + `<svg viewBox="0 0 360 240"><path d="M120 90 L240 90 L240 150 L120 150 Z" fill="#0f6e56" fill-opacity="0.1" stroke="none"/><path d="M120 90 L68 120 L120 150 Z M240 90 L292 120 L240 150 Z" fill="#0f6e56" fill-opacity="0.22" stroke="none"/><path d="M120 90 L240 90 L292 120 L240 150 L120 150 L68 120 Z" fill="none" stroke="#0f6e56" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M120 90 L120 150 M240 90 L240 150" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-dasharray="6 4"/></svg>` (triangles équilatéraux de côté 60, vérifié : √(52² + 30²) = 60) · a `6 أضلاع` (clé) · b `8 أضلاع` (`cote-commun-compte`) · c `10 أضلاع` (même étiquette) · d `4 أضلاع` muette · d1 · exp. « للمستطيل 4 أضلاع ولكلّ مثلّث 3، أي 10. الضلعان القصيران للمستطيل مشتركان مع المثلّثين فهما داخل الشكل، ويُحذف كلّ منهما من القطعتين معًا: يبقى من المستطيل ضلعاه الطويلان، ومن كلّ مثلّث ضلعان، أي 2 + 2 + 2 = 6 أضلاع. من وجد 10 عدّ كلّ ضلع مشترك مرّتين، ومن وجد 8 حذف كلًّا منهما من قطعة واحدة فقط. » |
| `01` Q4 | exemple § 🪟 à une donnée près (largeur 1 → arc 1,57, mêmes pièges « +1 » et « cercle entier ») | « نافذة عرضها 2 م وارتفاع جزئها المستطيل 3 م… » · SVG : 1er et 2e `path` `M145 76 L145 216 L215 216 L215 76 A35 35 0 0 0 145 76` → `M130 66 L130 216 L230 216 L230 66 A50 50 0 0 0 130 66` ; pointillé `M145 76 L215 76` → `M130 66 L230 66` ; `…>1<` → `…>2<` ; `<text x="133" y="151" …>2<` → `x="118" y="146" …>3<` · a `8 م` muette · b `11,14 م` (clé) · c `13,14 م` (`cote-commun-compte`) · d `14,28 م` muette · exp. « على الحدود ضلعان عموديّان 3 + 3 والقاعدة 2، أي 8 م، ثمّ القوس 3,14 × 2 ÷ 2 = 3,14 م: 8 + 3,14 = 11,14 م. القطر العلويّ داخل النافذة فلا يُضاف (وإلّا وجدنا 13,14)، ولا نضع دائرة كاملة (وإلّا وجدنا 8 + 6,28 = 14,28). » |
| `03` Q3 | 3e « fenêtre rectangle + demi-cercle de la largeur » (avec `quiz` Q4 et `01` Q4) en plus de l'exemple et du `verifie` § 🪟 | « زخرفة مكوّنة من مربّع ضلعه 6 سم، ألصقنا بكلّ ضلع من أضلاعه الأربعة نصف دائرة قطرها ضلع المربّع، من الخارج. ما محيط الزخرفة بالسنتيمتر؟ (π ≈ 3,14) » + `<svg viewBox="0 0 360 240"><path d="M150 90 A30 30 0 0 1 210 90 A30 30 0 0 1 210 150 A30 30 0 0 1 150 150 A30 30 0 0 1 150 90 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f6e56" stroke-width="3.6" stroke-linejoin="round"/><path d="M150 90 L210 90 L210 150 L150 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="6 4"/><text x="180" y="146" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">6 cm</text></svg>` (4 arcs extérieurs vérifiés : haut, droite, bas, gauche) · a `18,84 سم` muette · b `24 سم` muette · c `37,68 سم` (clé) · d `61,68 سم` (`cote-commun-compte`) · exp. « أضلاع المربّع الأربعة مشتركة مع أنصاف الدوائر فهي داخل الشكل، والحدّ هو الأقواس الأربعة وحدها. كلّ قوس 3,14 × 6 ÷ 2 = 9,42 سم، والأربعة 4 × 9,42 = 37,68 سم، أي دائرتان كاملتان قطرهما 6. من أضاف أضلاع المربّع 24 وجد 61,68، ومن حسب دائرة واحدة وجد 18,84، ومن اكتفى بمحيط المربّع وجد 24. » |
| `05` Q2 | doublon de `03` Q5 (route droite, un poteau tous les 3 m, poteaux aux deux bouts) | « نغرس أعمدة كلّ 3 م: على جانب طريق مستقيم طوله 36 م مع عمود عند كلّ من طرفيه، وعلى حدّ ساحة مغلقة محيطها 36 م. كم عمودًا نغرس في المجموع؟ » · a `24 عمودًا` muette · b `25 عمودًا` (clé) · c `26 عمودًا` (`plantation-contour-ferme-plus-un`) · d `72 عمودًا` muette · exp. « في الحالتين 36 ÷ 3 = 12 مسافة. على الطريق المستقيم بداية ونهاية فنزيد عمودًا: 13. وعلى الحدّ المغلق عدد الأعمدة يساوي عدد المسافات: 12. المجموع 13 + 12 = 25. من أضاف عمودًا في الحالتين وجد 26، ومن لم يضفه في أيّ منهما وجد 24. » |

Avec ces remplacements, la « maison » reste sous forme d'exemple (§ 🧵), de jumeau (`quiz` Q2) et de sens inverse
(`04` Q1). C'est justifié. Les autres jumeaux à données changées (`02` Q1 ↔ exemple § 🔖, `02` Q2 ↔ L de § 🔖, `02` Q5 ↔
quart de § ➕➖) sont admis.

**M25-3 — `competencies` absent des 35 questions** du chapitre neuf. À ajouter : `["math.mes.perimetres"]`.

### Mineurs

- **m25-1** — `02` Q5, explication : « أو طرحه فنجد 33,72 » est faux tel qu'écrit (40 − 8 − 6,28 = 25,72). 33,72 = 40 −
  6,28. → « أو طرح القوس من محيط المستطيل دون حذف الضلعين فنجد 40 − 6,28 = 33,72 ».
- **m25-2** — `03` Q6, explication : « الضلع القصير المنتزع نصفه » se lit « dont la moitié est retirée », alors que tout
  le côté disparaît. → « الضلع القصير الذي انتُزع منه نصف القرص حلّ محلّه قوس… ».
- **m25-3** — `04` Q3 : « و معيّنين » → « ومعيّنين ».
- **m25-4** — `resume.md` n'a aucune figure pour un chapitre spatial. Reprendre la maison de § 🧵 (côté commun en
  pointillé) en tête du résumé.
- **m25-5** — Clés à b 58 % (18/31) : mineur, l'affichage mélange les options. À rééquilibrer au passage des
  remplacements.

---

## Synthèse

| chapitre | questions re-résolues | bloquants | majeurs | mineurs | verdict |
| --- | --- | --- | --- | --- | --- |
| 20 aires | 55 | 0 | 2 (M20-1 : 5 questions ; M20-2) | 6 | à corriger |
| 21 cercle | 54 | 0 | 4 (M21-1 : 11 questions + 4 retouches de cours/résumé ; M21-2 : 6 questions ; M21-3 étiquette ; M21-4) | 5 | à corriger |
| 23 solides | 54 | 0 | 4 (M23-1 étiquette volume ; M23-2 : 4 ; M23-3 : 7 ; M23-4) | 7 | à corriger |
| 25 périmètre (neuf) | 35 | 0 | 3 (M25-1 étiquettes ; M25-2 : 4 ; M25-3) | 5 | à corriger |
| **lot B5** | **198** | **0** | **13** | **23** | **à corriger** |

**En bref.** Aucune clé fausse, aucune double réponse. Les 4 cours sont justes, au patron, sans figure fausse. M2 est
tenu et le volume reste hors du cours. Le chapitre neuf 25 couvre fidèlement la leçon 24 avec des reprises exactes.

Trois familles de défauts restent à corriger :
1. **18 questions redonnent un exemple, un piège ou un `verifie` du cours.** Le ch. 21 est le plus touché : les petits
   rayons 2, 3, 4, 5 sont partagés entre le cours et les items. Il y a aussi les doublons et miroirs anciens que la
   tranche sans `--fresh` fait remonter (21 : `quiz` Q5 = `03` Q5 ; 23 : trois miroirs latérale/totale).
2. **Les étiquettes affichées à l'élève ne nomment pas l'erreur, ou sortent du programme.** Elles font entrer le volume
   (حجم, cm³, cylindre) aux ch. 21 et 23 et contredisent la règle d'arrondi au ch. 25. Six étiquettes sont à ajouter au
   registre (JSON prêt ci-dessus).
3. **`competencies` absent des 105 nouvelles questions du lot**, alors que B1–B4 sont à 100 %.

Tous les remplacements sont prêts à coller, recalculés, et une seule option par question y est défendable. Après
application, relancer `content:check`, `content:qa` et `content:tranche` (avec et sans `--fresh`) sur les 4 chapitres :
les paires ≥ 0,6 du lot doivent tomber à 0.

---

## Re-vérification (2026-10-20, après les « Corrections après audit » de `rapports/rapport-B5.md`)

> Valide au commit `480be63a` (arbre propre). Le lot ne change pas : 20, 21, 23, 25 — cours, résumés, `chapter.json`,
> quiz et exercices 01–05. Les missions `06+` restent hors périmètre. J'ai repris chaque question modifiée depuis
> `bbb33ffe` (diff question par question) et je l'ai **re-résolue** : 74 questions remplacées ou retouchées, et 4 blocs
> de cours ou de résumé.

### Les décisions du pilote

- **Étiquettes.** Mon JSON n'est pas appliqué, et c'est accepté. J'ai vérifié les ids de `vocab-math-6eme.md` dans le
  registre. Leur libellé nomme bien l'erreur exécutée :
  - `perimetre-segment-interieur-compte` couvre le côté commun et le diamètre accolé ;
  - `reste-ignore-dans-le-probleme` (« un rouleau de plus ») supprime la contradiction de `arrondi-par-troncature` ;
  - `arc-retranche-compte-en-moins` ;
  - `plantations-ferme-et-ouvert-confondus` ;
  - en complément, `perimetre-partie-du-bord-oubliee`, `arc-circonference-entiere-prise-pour-l-arc`,
    `couronne-largeur-prise-pour-rayon`, `aire-cote-oblique-pris-pour-hauteur`,
    `aire-composee-somme-au-lieu-de-difference` et `unites-non-converties`.

  `volume-utilise-comme-aire` et `rayon-non-eleve-au-carre` n'apparaissent plus nulle part dans le lot (grep : 0) : la fuite
  « حجم / cm³ / أسطوانة » est fermée. Conséquence acceptée : les pièges « 3,14 × 5 = 15,7 » (21 § 🧩) et
  « 40 × 20 × 25 » (23 § 🎀) restent montrés dans le cours sans étiquette, et leurs options sont muettes.
  `content:qa` n'en dit rien.
- **5 clés numériques strictement les plus longues** (20/05#1, 21/02#4, 21/04#2, 21/05#2, 23/01#1, soit 3 %) :
  **acceptées.** Ce sont des nombres plus longs (« 0,785 », « 254,34 », « 120 سم ») parmi des distracteurs numériques
  de même forme. Aucune ne porte de justification ni de marqueur, et le taux est très en dessous du hasard (25 %).
- **21 `02-boss` Q6 laissée en d3** (calcul 18 ÷ 2) : **acceptée** comme résidu de calibration mineur, pour garder
  l'identifiant stable. Elle est dans un boss, et la question est bien remplacée.

### 1. Défauts de l'audit : tous corrigés, sauf ce qui est listé au § 4

- **Ch. 20.** Les 5 remplacements de M20-1 sont appliqués et justes (24 ; 14 ; 54 ; comparaison triangle/parallélogramme ;
  « 12 سم² »). Les figures de `01` Q9 (base 7, sommet ج en 300) et de `03` Q8 (côtés de l'angle droit 12 et 9) ont été
  re-vérifiées sur les coordonnées. `competencies` est présent partout. m20-1, m20-2 (9 600 expliqué), m20-6 (`03` Q2)
  sont corrigés. Ajouts justes : `03` Q1 (12 × 5 → 60) et `05` Q2 (cour de 8 m → 64).
- **Ch. 21.** Les 11 redites sont traitées (8 remplacements, 3 `verifie` renumérotés : 28,26 ÷ 9 ; ر = 3,5 → 21,98 et
  38,465 ; quart ر = 2 → 3,14, 3,14 et 7,14 — tout est juste). Le résumé suit le piège (« ق = 14 ⟵ ر = 7 لا 28 »). Les
  6 remplacements de M21-2 sont faits. La couronne de `quiz` Q6 est passée à 3/7 avec le cercle intérieur à `r="41"`.
  m21-1 à m21-3 sont corrigés, et la clôture dit « التالي: المُدَدُ الزمنيّة ». Ajouts justes :
  - `02` Q7 : 379,94 → ر = 11 ;
  - `03` Q4 : d = 1,5 → 4,71 (distracteurs 2,355, 9,42, 4,64) ;
  - `04` Q1 : d = 21 → 65,94 (32,97, 131,88, 346,185).
- **Ch. 23.** M23-2 (4) et M23-3 (7) sont appliqués et justes : 120 ; 4 × (ح × ح) ; 10 × 4 ; rangée de 5 + 1 ; 5,76 ;
  « مساحة وجهين » ; 9 ; 384 ; 0,24 → 0,16 ; `multi` {a, d}. Le champ `manuel` est retiré de `05`. Le `verifie` sur la
  perspective est corrigé, « علب كاملة » ajouté, la clôture corrigée. m23-3 à m23-6 sont faits : « بلاط », pavés cotés
  8 × 5 × 3 et 6 × 3 × 4. Ajouts justes :
  - `02` Q2 : 4,5 → 81 (18, 20,25, 121,5) ;
  - `04` Q4 : murs 10 × 4 × 5 → 140 (70, 120, 200) ;
  - `04` Q6 : 6 × 4 × 2 → 88.
- **Ch. 25.** Les 4 remplacements de M25-2 sont appliqués et justes (6 côtés ; 11,14 ; quadrilobe 37,68 ; 25 poteaux).
  Les étiquettes sont posées (M25-1). Les 35 questions ont maintenant des `competencies`. m25-1 à m25-4 sont faits : le
  résumé a maintenant la figure de la maison.

### 2. Questions remplacées ou retouchées : 74/74 re-résolues, clés justes

Aucune n'a deux réponses défendables, et aucune option n'est désignée par sa lettre. Les explications redisent la valeur
attendue.

### 3. Pas de régression de gate ni de rendu

- `content:check` ✓.
- `content:qa -- --subject math-6eme` : **0 erreur**. Les 5 avertissements restants sont hors lot (ch. 14 et 16).
- `content:figures:check` ✓.
- `content:tranche --fresh --strict-longest --strict-lessons` ✓ : clé la plus longue 5/177 = 3 % ; positions
  24/28/30/18 % (le b à 58 % du ch. 25 est résorbé) ; patron 0 en recul.
- **Paires proches internes sans `--fresh`, hors `06+` : 0 au-dessus de 0,6** (la plus haute est 0,59 : 21 `02` Q2 ↔ Q3,
  périmètres ر = 12 et d = 6, un exercice parallèle justifié).
- **Rendu refait à 360 px** après les derniers changements (vitest jetable supprimé, moteur propre ; Chromium) :
  `scrollWidth` = 360 partout, 0 `:::` brut. Figures : 11/10/14/8 dans les cours, 84 dans les questions, 1 dans le
  résumé du 25. Les `<details>` sont 9/9/8/6. Les 12 figures neuves ou modifiées ont été regardées une à une : toutes sont
  vraies (20 `01` Q1, Q9, `03` Q2, Q8 ; 21 `quiz` Q6 ; 23 `01` Q9, `03` Q6, `05` Q4 ; 25 `01` Q4, `03` Q1, `03` Q3 ;
  résumé 25).

### 4. Défauts restants (texte exact)

**R-1 (majeur, régression) — 21 `05-entrainement` Q4 redonne l'exemple résolu § 🧩.** La question est réécrite (« ساحة
مستديرة قطرها 10 م … ») mais garde ر = 5 → 78,5, avec 25 (le piège « ينسى π » du cours), 31,4 (l'exemple de la
propriété § 🚲) et 314 (le `verifie` de § 🧩). Remplacement :

« ساحة مستديرة قطرها 30 م تُغطّى كلّها بالعشب. كم مترًا مربّعًا من العشب؟ (π ≈ 3,14) »
- a `225 م²` (`math.geo.facteur-pi-omis`)
- b `94,2 م²` (`math.geo.formules-cercle-perimetre-et-aire-confondues`)
- c `706,5 م²` (clé)
- d `2 826 م²` (`math.geo.rayon-et-diametre-confondus`) ⚠️ l'espace entre 2 et 826 doit être une **U+00A0**
- exp. « العشب يغطّي السطح فهو مساحة القرص: نصف القطر 30 ÷ 2 = 15 م، والمساحة 3,14 × 15 × 15 = 3,14 × 225 = 706,5 م². من
  أخذ القطر 30 نصفَ قطر وجد 2 826، ومن حسب المحيط π × 30 وجد 94,2، ومن نسي π وجد 225. » (même U+00A0 dans « 2 826 »)

Vérifié : 3,14 × 225 = 706,5 ; 3,14 × 900 = 2 826 ; 3,14 × 30 = 94,2. La clé n'est pas la plus longue, et la question ne
coïncide avec aucune autre question ni aucun exemple du cours.

**Mineurs :**
- **r-2** — 20 `03` Q1, option d `125 سم²` : c'est « 12 et 5 écrits côte à côte ». Lui poser
  `math.num.chiffres-juxtaposes-au-lieu-du-produit` et ajouter à l'explication « …ومن كتب العددين جنبًا إلى جنب وجد 125. »
- **r-3** — 20 `01` Q1 : le libellé « 3 سم » (`<text x="46" y="80" text-anchor="middle"`) déborde sur le bord gauche
  du rectangle (x = 60). → `<text x="54" y="80" text-anchor="end"`.
- **r-4** — 25 `02` Q5, option b `33,72 م` (= 40 − 6,28) exécute **deux** erreurs : les deux segments de 4 m sont gardés
  ET l'arc est retranché. Elle doit donc être muette, plutôt que porter `arc-retranche-compte-en-moins`.
- **r-5** — 25 `03` Q3, option d `61,68 سم` (les 4 côtés intérieurs ajoutés) n'a pas d'étiquette. Lui poser
  `math.mes.perimetre-segment-interieur-compte`.
- **r-6** (accepté, pas d'action) — 21 `02` Q7 (379,94 → ر = 11) et le distracteur 379,94 de `quiz` Q7 (demi-cercle
  d = 22) portent sur le même cercle. Les calculs sont différents, ce n'est pas un doublon.

### Verdict de la re-vérification

**Prêt après R-1.** Il reste une seule question à remplacer (texte ci-dessus), plus 4 retouches mineures facultatives.
Aucune clé n'est fausse, aucune régression de gate ou de rendu, et aucune paire interne ne dépasse 0,6. Si l'on veut se
contenter de « prêt » tel quel, R-1 reste un défaut majeur : la question redonne l'exemple résolu du cours.
