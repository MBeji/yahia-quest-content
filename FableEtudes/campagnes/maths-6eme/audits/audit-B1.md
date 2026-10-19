# Audit B1 — maths 6ᵉ, chapitres 01 à 06 (auditeur indépendant, opus)

> Valide pour les fichiers de `content/math-6eme/0[1-6]-*` tels qu'au commit `7aab9311` (branche
> `wip/maths-6eme-un-passage`; dernier commit qui les touche : `44bad0b4`; aucun changement non commité dans
> le lot au moment de l'audit). Ré-auditer si ces fichiers bougent. 2026-10-19.
>
> Protocole : re-résolution à l'aveugle de **chaque** question (217 : 6 quiz + 30 exercices) avant de lire clés et
> explications ; lecture intégrale des 6 cours et 6 résumés, chaque exemple, piège et `verifie` recalculé ; reprises
> confrontées au PDF (`102609` ص 4, 5, 7, 10, 11, 12, 36 ; `502603` p.169) ; rendu vitest + Chromium 360 px ;
> les quatre gates. Notes et rapport de l'auteur lus **après** la re-résolution.

## Verdict : **à corriger** (0 critique, 47 majeurs, 16 mineurs)

Toutes les clés sont justes (217/217), une seule réponse défendable partout, explications justes, aucune lettre
ni ordinal, cours justes en maths et en arabe, aucune notion ⛔, reprises conformes au PDF, gates verts, rendu
propre à 360 px. Ce qui bloque, ce sont trois familles de défauts que seule une lecture croisée cours ↔ questions
voit :

1. **Des questions qui redonnent un exemple résolu du cours** (mêmes nombres, souvent même distracteur que le
   piège du cours) : **35 questions**, dont 13 au ch. 06, 8 au ch. 03, 7 au ch. 05. L'élève qui a lu le cours
   répond par mémoire, pas par raisonnement — et la consigne l'interdit expressément.
2. **Des étiquettes qui nomment une autre erreur que celle exécutée** (9 questions) et deux options équivalentes
   (ch. 03 quiz Q4).
3. **Deux `coursePitfalls` du ch. 04 sans `::: piege`** et la reprise `أقيّم 10` (ch. 04) dont la réponse est
   imprimée dans le cours (doute n° 1 de l'auteur : confirmé).

Toutes les corrections ci-dessous sont des remplacements **au même rang et à la même difficulté** (aucun
identifiant ne bouge). Chaque texte a été recalculé ; clé jamais strictement la plus longue ; une seule réponse ;
aucune option désignée par sa place. Les nombres à plusieurs classes s'écrivent avec l'espace insécable U+00A0,
comme dans les fichiers (ce rapport l'emploie déjà).

| chapitre | questions re-résolues | clés fausses | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- | --- |
| 01-entiers-naturels | 35 | 0 | 0 | 1 | 4 |
| 02-operations-naturels | 38 | 0 | 0 | 6 | 2 |
| 03-nombres-decimaux | 35 | 0 | 0 | 15 | 2 |
| 04-addition-soustraction-decimaux | 36 | 0 | 0 | 5 | 1 |
| 05-multiplication-division-decimaux | 36 | 0 | 0 | 7 | 1 |
| 06-multiples-communs | 37 | 0 | 0 | 13 | 6 |
| **total** | **217** | **0** | **0** | **47** | **16** |

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : 0 erreur ; 3 avertissements, tous en `14-…` (hors lot).
- `content:figures:check` ✓.
- `content:tranche -- --subject math-6eme --chapters <6 slugs> --fresh --strict-longest --strict-lessons` ✓ : clé
  strictement la plus longue 0/47 questions modifiées ; mesure complémentaire de l'auditeur sur les 211 QCM du lot :
  **0/211**. Paires proches 0 ; patron de notion : 0 en recul.
- Scans de notation (hors `<svg>`) : 0 chiffre arabo-indien, 0 LaTeX, 0 `\d \d{3}` en espace simple, 0 `$…$`.

## Rendu

`renderLesson` / `renderSummary` (vitest jetable) : 0 résidu `**`, `:::`, `$$`, 0 `<em>` parasite sur les 12
fichiers. Chromium 360 px : `scrollWidth` = 360 sur les 6 pages, aucun tableau ni figure > 330 px. Figures
re-dérivées : 01 (27 381 à x = 131,4 sur [40 ; 280], milieu 160 ✓), 03 (14,62 à x = 191,2 ✓ ; rangs de 4,286 ✓),
04 (18,50 + 19,75 ✓ ; 100,5 − 8,96 : virgules alignées à droite, désalignées à gauche, 10,9 sous la virgule du
haut ✓), 06 (14 + 21 = 7 × 5 ✓ ; 0, 12, 24 communs à 4 et 6 ✓). Fichiers jetables supprimés.

## Reprises (champ `manuel`) — confrontées au PDF

| fichier | item déclaré | PDF | verdict |
| --- | --- | --- | --- |
| 04 `03-revision` | أقيّم 2 : 100,1 − 99,98 ; 9,9 + 91,09 | ص 4 | ✓ mêmes données (le manuel écrit RTL) |
| 04 `04-defi` | ex. 4 : 9,13 = … + 8,09 | ص 5 | ✓ |
| 04 `05-entrainement` | أقيّم 10 (la balance) | ص 7 | données ✓ (126,75 / 88,25 / 81,25) — **mais réponse imprimée dans le cours** → B1-04-1 |
| 05 `01-pratique` | ex. 2 أ (22,18 × 0,01) ; 2 ب (15 : 0,1) | ص 10 | ✓ |
| 05 `02-boss` | ex. 2 ب (48,36 : 12) ; ex. 5 (1584 : 4,4) | ص 10, 11 | ✓ (360) |
| 05 `04-defi` | ex. 7 (10,186 km = 5,5 ميل) | ص 11 | ✓ |
| 05 `05-entrainement` | T1 sit. 1, offre 2 | guide p.169, corrigé 1015,5 (fiche §1 bis) | ✓ (342,750 ; 6 أقساط ; + 5,750) |
| 06 `04-defi` | ex. 4 (4, 6, 8 sous 130) | ص 36 | ✓ (erratum n° 9 appliqué : « 4 و 6 و 8 ») ; tâche reformulée (dénombrer) |
| 06 `05-entrainement` | ex. 6 (150 et 200) | ص 36 | ✓ (600) |

Errata : n° 7 (« دون أن يبقى منها شيء ») appliqué dans le cours 06 (« دون أن تبقى بيضة خارج العلب ») ✓ ; n° 1
(540) sans objet dans le lot. Les variantes (bus, coureurs, troupeau, ch. 06) ne portent pas le champ ✓.

---

## 01-entiers-naturels

**Cours** — 7 sections au patron (ancrage → nom → représentation → exemple → piège → règle avec cas limite →
`verifie` → `retenir`), tous les calculs recalculés justes ; les 7 `coursePitfalls` ont leur `> ⚠️` et un distracteur ;
résumé 7 puces ↔ 7 sections. Fiche (§2, §3.2 « milliards : vocabulaire ») respectée.

**B1-01-1 · majeur · `exercices/02-boss.json` Q5 — doublon de Q4 dans le même exercice.** Q4 (28 617) et Q5
(38 920) demandent toutes deux « arrondir au millier », même cadre, mêmes distracteurs (troncature, mauvais rang).
Remplacer Q5 (d3) :

```json
{
  "prompt": "نكوّن أعدادًا من أربعة أرقام بالأرقام 5 و 0 و 8 و 3 (كلّ رقمٍ مرّةً واحدة). ما أقربُ هذه الأعداد إلى 5 000؟",
  "options": [
    { "id": "a", "text": "5 038" },
    { "id": "b", "text": "5 083" },
    { "id": "c", "text": "5 308" },
    { "id": "d", "text": "3 850" }
  ],
  "correctOption": "a",
  "explanation": "لنقترب من 5 000 نبدأ بالرقم 5، ثمّ نضع الأرقام الباقية تصاعديًّا لنبقى أقرب ما يمكن: 5 038، وهو يبعد عن 5 000 بـ 38 فقط. أمّا 5 083 فيبعد بـ 83، و 5 308 بـ 308. وأكبر عددٍ يبدأ بـ 3 هو 3 850، ويبعد عن 5 000 بـ 1 150.",
  "difficulty": 3
}
```

(Vérifié : parmi les 18 permutations sans 0 en tête, distances minimales 38, 83, 308, 380 → une seule réponse.)

**B1-01-2 · mineur · `quiz.json` Q1 et cours § 1 — le nombre −1.** Les relatifs sont ⛔ (fiche §2) : l'option « −1 »
et la ligne de propriété « والعدد −1 ليس عددًا طبيعيًّا، لأنّنا لا نعدّ به » introduisent un objet hors programme.
Option c → `{ "id": "c", "text": "10" }` ; explication → « أصغر عددٍ طبيعيّ هو 0: به نبدأ العدّ قبل 1، ثمّ تتوالى الأعداد 1، 2، 3… بلا نهاية، فلكلّ عددٍ تالٍ، لكنّ 0 ليس له سابق. » ; dans le cours, supprimer « والعدد −1 ليس
عددًا طبيعيًّا، لأنّنا لا نعدّ به » (la ligne devient « حالة حدّية: العدد 0 **ليس له سابق**. »).

**B1-01-3 · mineur · étiquettes `rang-du-chiffre-decale` sur un écart de DEUX rangs** (le libellé dit « d'un cran ») :
`quiz.json` Q3 a (العشرات pour الآلاف), `02-boss` Q1 a (الآلاف pour مئات الآلاف), `04-defi` Q1 a (3 000 pour 300 000) →
rendre ces trois options muettes. `01-pratique` Q4 a (« 2×100 + 5×10 + 3 » = 253 : le zéro est tombé) et
`05-entrainement` Q3 d (30 740 : zéro perdu) → `math.num.zero-intercalaire-oublie`.

**B1-01-4 · mineur · `04-defi` sans problème « sens inverse »** (exigé en d4 par `prof-math-6eme`). Remplacer Q4
(6 970, jumeau du cas limite 3 960 du cours) :

```json
{
  "prompt": "عددٌ طبيعيّ قيمتُه المقرّبة إلى أقرب ألف هي 7 000. ما أصغرُ قيمةٍ ممكنةٍ له؟",
  "options": [
    { "id": "a", "text": "6 499" },
    { "id": "b", "text": "6 000" },
    { "id": "c", "text": "7 499" },
    { "id": "d", "text": "6 500" }
  ],
  "correctOption": "d",
  "explanation": "تُدوَّر إلى 7 000 كلّ الأعداد من 6 500 إلى 7 499: رقم المئات 5 أو أكثر يفرض الصعود من 6 000 إلى 7 000، ورقم المئات أقلّ من 5 يُبقي 7 000. أصغرها 6 500. أمّا 6 499 فرقم مئاته 4 فيُدوَّر إلى 6 000، و 7 499 أكبرها لا أصغرها.",
  "difficulty": 3
}
```

**B1-01-5 · mineur · cours § 5** : l'ancrage « مزاد لبيع سيّارة » (enchère de voiture) est un contexte adulte ;
« في مزادٍ لبيع درّاجة » avec 985 / 958 / 1 050 garderait la même structure (laisser les nombres actuels si l'on
préfère ne pas toucher l'exemple : le défaut est de registre, pas de calcul).

---

## 02-operations-naturels

**Cours** — 9 sections au patron (la dernière, « خلاصة », est une synthèse sans `retenir`, acceptable) ; tous les
calculs justes (2 343, 3 426, 1 404, 900, 91, 87 = 6 × 14 + 3, 9, 78, 4 225, 3 236, 1 400, 1 300, 2 800, 936, 374,
133 = 9 × 14 + 7, 24, 220, 820) ; 7 pièges, 7 `coursePitfalls` portés ; résumé 9 ↔ 9.

**B1-02-1 · majeur ×5 · questions qui redonnent le cours.**

- `quiz.json` Q5 = méthode « 8 × 10 + 8 × 3 = 8 × (10 + 3) = 8 × 13 = 104 ». Remplacer par :
  prompt « أيُّ مساواةٍ تُترجم خاصّيّةَ التوزيعيّة على الجمع؟ » ; options
  a « 6 × (10 + 4) = 6 × 10 + 4 », b « 6 × (10 + 4) = 6 × 10 + 6 × 4 », c « 6 × (10 + 4) = 6 + 10 + 4 »,
  d « 6 × (10 + 4) = 6 × 10 + 10 × 4 » ; clé b ; explication « التوزيعيّة: a × (b + c) = a × b + a × c، إذن 6 × (10 + 4) = 6 × 10 + 6 × 4 = 60 + 24 = 84: نضرب 6 في الحدّين معًا. »
- `02-boss` Q3 (23 × 11) = cas limite de la méthode « 23 × 11 = 230 + 23 = 253 ». Remplacer par :
  prompt « ما ناتجُ 36 × 11؟ » ; options a « 371 », b « 386 », c « 406 », d « 396 » ; clé d ;
  explication « 36 × 11 = 36 × (10 + 1) = 36 × 10 + 36 × 1 = 360 + 36 = 396. من يكتب 36 × 10 + 11 = 371 لم يضرب 36 في الحدّ الثاني. »
- `02-boss` Q6 (6 × 102) = méthode « 6 × 102 = 600 + 12 = 612 ». Remplacer par :
  prompt « احسب 8 × 103 باستعمال التوزيعيّة. » ; options a « 824 », b « 8 024 », c « 803 »,
  d « 111 » (`math.num.operation-inverse-appliquee`) ; clé a ;
  explication « 8 × 103 = 8 × (100 + 3) = 8 × 100 + 8 × 3 = 800 + 24 = 824. أمّا 803 فنسي ضرب 8 في الحدّ 3، و 111 هو المجموع 8 + 103 لا الجداء. »
- `05-entrainement` Q3 (50 × 60) = propriété « 50 × 60 = 5 × 6 × 100 = 3 000 ». Remplacer par :
  prompt « ما ناتجُ 30 × 80؟ » ; options a « 240 », b « 2 400 », c « 110 » (`math.num.operation-inverse-appliquee`),
  d « 24 000 » ; clé b ; explication « 30 × 80 = (3 × 8) × 100 = 24 × 100 = 2 400: نضرب الأرقام ثمّ نضيف الصفرين معًا. »
- `05-entrainement` Q5 (100 − 4 × 9 + 6) = cas limite « 100 − 36 + 6 = 70، لا 100 − 42 = 58 » (même 58 en
  distracteur). Remplacer par : prompt « ما قيمةُ 90 − 7 × 8 + 5؟ » ; options a « 39 », b « 29 »,
  c « 669 » (`math.num.priorite-operations-ignoree`), d « 34 » ; clé a ;
  explication « الضربُ أوّلًا: 7 × 8 = 56، ثمّ من اليسار إلى اليمين: 90 − 56 = 34 ثمّ 34 + 5 = 39. من حسب من اليسار دون أولويّة وجد (90 − 7) × 8 + 5 = 669. »

**B1-02-2 · majeur · `05-entrainement` Q2 b « 8 089 » étiquetée `retenue-oubliee`** : 7 200 + 899 sans la retenue
donne 7 099, pas 8 089 (qui n'exécute aucune erreur identifiable). Option b → `{ "id": "b", "text": "7 099", "misconceptionTag": "math.num.retenue-oubliee" }`
(distinct de d « 7 999 » ; même longueur que la clé « 8 099 »).

**B1-02-3 · mineur · `03-revision` Q4 (125 × 8) et `01-pratique` Q6 (25 × 4)** reprennent deux cases du tableau
« زوج ذهبيّ » du cours. Acceptable en d1–d2 ; pour Q4 (d2), préférer « ما ناتجُ 125 × 16؟ » (2 000 ; distracteurs
1 250, 2 016, 141).

**B1-02-4 · mineur · cours § 2** : le piège étiqueté « نسيان الاستلاف » montre en fait « le petit chiffre ôté du
grand » (4 574), c.-à-d. `math.num.soustraction-colonne-petit-du-grand`. Renommer l'en-tête du piège
« **الخطأ الشائع — طرح الأصغر من الأكبر في كلّ عمود** » ; `emprunt-oublie` reste porté par les distracteurs et
pourrait recevoir son propre piège (5 000 − 1 764 = 4 236 : emprunt fait mais millier non diminué).

---

## 03-nombres-decimaux

**Cours** — 8 sections au patron ; tous les calculs justes (4 286 m, 1,852, 9,006, 4,050 د = 4 د 50 مي,
12,375, 5,204, 3,061, podium 4,1 > 3,8 > 3,75 > 3,09, 2,405 < 2,45 < 2,5 < 2,54, 9 nombres entre 4,6 et 4,7, 6,352
→ 6,35 / 6,4 / 6) ; 9 `coursePitfalls` portés ; résumé 8 ↔ 8.

**B1-03-1 · majeur · `quiz.json` Q4 — deux options équivalentes.** a « 3,7 < 3,65 » et d « 3,65 > 3,7 » disent la
même chose : l'une fausse, l'autre l'est aussi, éliminées ensemble. d →
`{ "id": "d", "text": "3,07 > 3,65", "misconceptionTag": "math.num.zero-apres-virgule-ignore" }` (qui lit 3,07
comme 3,7 la croit vraie). Explication inchangée.

**B1-03-2 · majeur ×8 · questions qui redonnent le cours.**

- `quiz.json` Q1 (25,84 → 25) = ligne du tableau § 1. Prompt « في العدد 47,21 ما الجزءُ الصحيح؟ » ; options
  a « 47 », b « 21 » (`partie-entiere-et-decimale-confondues`), c « 4 721 » (`virgule-ignoree-nombre-lu-entier`),
  d « 0,21 » (`partie-entiere-et-decimale-confondues`) ; clé a ; explication « الجزءُ الصحيح هو ما يسبق الفاصلة: 47؛ أمّا 21 فهو الجزءُ العشريّ، وقيمته 0,21. ».
- `03-revision` Q1 (« ثلاثة فاصل سبعة », 0,37) = piège § 3. Prompt « كيف نكتب بالأرقام «خمسة فاصل تسعة أعشار»؟ » ;
  options a « 5,9 », b « 59 » (`virgule-ignoree-nombre-lu-entier`), c « 0,59 » (`virgule-mal-placee`),
  d « 5,09 » (`rang-decimal-confondu`) ; clé a ; explication « «خمسة» هو الجزء الصحيح، فنكتب 5 ثمّ الفاصلة مباشرةً بعد رقم الآحاد؛ و«تسعة أعشار» رتبةٌ واحدة بعد الفاصلة: 5,9. أمّا 5,09 فتسعة أجزاء من المئة. ».
- `03-revision` Q4 (5,07) = cas limite « 5,07 = 5 + 0,07 ». Prompt « ما تفكيكُ العدد 8,09؟ » ; options
  a « 8 + 0,9 » (`rang-decimal-confondu`), b « 8 + 0,009 » (`rang-decimal-confondu`), c « 800 + 9 »
  (`virgule-ignoree-nombre-lu-entier`), d « 8 + 0,09 » ; clé d ; explication « 8,09 فيه 0 أعشار و 9 أجزاء من المئة، أي 8 + 0,09؛ والرتبة التي رقمها 0 لا تظهر في المجموع. » (au passage, l'option actuelle « 50 + 7 » = 57 n'exécutait
  pas « virgule ignorée », qui donne 507).
- `03-revision` Q5 (14,62 à l'unité) = exemple résolu § 8. Prompt « ما تدويرُ 23,71 إلى أقرب وحدة؟ » ; options
  a « 24 », b « 23 » (`arrondi-par-troncature`), c « 23,7 » (`arrondi-au-mauvais-rang`), d « 20 »
  (`arrondi-au-mauvais-rang`) ; clé a ; explication « الرقم الذي يلي الآحاد هو 7 (≥ 5) فنصعد: 23,71 ≈ 24. أمّا 23 فقطعٌ عند الفاصلة، و 23,7 تدويرٌ إلى العُشر، و 20 تدويرٌ إلى العشرة. ».
- `03-revision` Q6 (0,3 = 30 centièmes) = propriété § 4 « 0,3 = 0,30، أي … 30 جزءًا من المئة ». Prompt
  « العدد 0,8 يساوي كم جزءًا من الألف؟ » ; options a « 8 », b « 80 », c « 800 », d « 0,008 » (a, b, d :
  `rang-decimal-confondu`) ; clé c ; explication « 0,8 = 0,80 = 0,800: نضيف صفرين على اليمين فلا تتغيّر القيمة، ويصير الرقم الأخير في رتبة الأجزاء من الألف. إذن 0,8 = 800 جزء من الألف. ».
- `02-boss` Q3 (12,4 / 12,40) = cas limite de la méthode § 6. Prompt « قارن بين 7,08 و 7,8. » ; options
  a « 7,08 > 7,8 » (`math.dec.compare-by-length`), b « 7,08 = 7,8 » (`zero-apres-virgule-ignore`),
  c « 7,08 < 7,8 », d « لا يمكن المقارنة » ; clé c ; explication « نساوي الطول: 7,08 و 7,80. الجزءان الصحيحان متساويان (7)، ثمّ الأعشار: 0 < 8، إذن 7,08 < 7,8. الصفر بين الفاصلة والرقم يغيّر العدد. ».
- `04-defi` Q1 (7,1) = cas limite § 7 « أصغر عدد برقم واحد بعد الفاصلة أكبر من 7 هو 7,1 ». Prompt « ما أكبرُ عددٍ عشريّ أصغرَ من 3 وله رقمان فقط بعد الفاصلة؟ » ; options a « 2,99 », b « 2,9 », c « 3,01 », d « 2,999 » ;
  clé a ; explication « برقمين بعد الفاصلة نكتب 3 = 3,00، والعدد الذي يسبقه بجزءٍ واحد من المئة هو 2,99. أمّا 2,999 فله ثلاثة أرقام بعد الفاصلة، و 2,9 = 2,90 أصغر من 2,99، و 3,01 أكبر من 3. ».
- `04-defi` Q4 (« plus grand à un chiffre qui s'arrondit à 5 » → 5,4) = cas limite § 8 « من 4,5 إلى أقلّ من 5,5 ».
  Prompt « عددٌ عشريّ برقمٍ واحدٍ بعد الفاصلة، تدويرُه إلى أقرب وحدةٍ يساوي 8. ما أصغرُ قيمةٍ ممكنةٍ له؟ » ;
  options a « 7,4 », b « 8,4 », c « 7,5 », d « 8,5 » ; clé c ; explication « يُدوَّر إلى 8 كلّ عددٍ من 7,5 إلى أقلّ من 8,5. أصغرها برقمٍ واحد بعد الفاصلة 7,5، لأنّ الرقم 5 يفرض الصعود. أمّا 7,4 فيُدوَّر إلى 7، و 8,4 أكبرها لا أصغرها، و 8,5 يُدوَّر إلى 9. ».

**B1-03-3 · majeur ×2 · doublons de `quiz.json` Q3 (4,5 = 4,50)** : `01-pratique` Q4 (2,3 = 2,30 ; mêmes
distracteurs 2,03 / 23 / 0,23) et `05-entrainement` Q3 (6,30 = 6,3 ; 6,03 / 63 / 0,63) — même question trois fois.

- `01-pratique` Q4 (d1) : prompt « أيُّ الأعداد التالية يساوي 2,06؟ » ; options a « 2,060 », b « 2,6 »
  (`zero-apres-virgule-ignore`), c « 2,600 » (`zero-apres-virgule-ignore`), d « 20,6 » (`virgule-mal-placee`) ;
  clé a ; explication « الصفر على يمين آخر رقمٍ عشريّ لا يغيّر العدد: 2,06 = 2,060. أمّا الصفر بين الفاصلة والرقم 6 فيحفظ رتبة الأعشار الخالية: 2,6 و 2,600 فيهما ستّة أعشار لا ستّة أجزاء من المئة. ».
- `05-entrainement` Q3 (d2) : prompt « ما الكتابة التي تساوي 6,3 وفيها ثلاثة أرقام بعد الفاصلة؟ » ; options
  a « 6,003 », b « 6,300 », c « 6,030 » (a, c : `rang-decimal-confondu`), d « 63,000 » (`virgule-mal-placee`) ;
  clé b ; explication « نضيف صفرين على يمين الجزء العشريّ فلا تتغيّر القيمة: 6,3 = 6,30 = 6,300، ويبقى 3 في رتبة الأعشار. أمّا 6,030 و 6,003 فينقلان 3 إلى رتبة الأجزاء من المئة أو من الألف. ».

**B1-03-4 · majeur ×4 · étiquettes qui n'exécutent pas l'erreur nommée** (`math.dec.compare-by-length` =
« le plus long est le plus grand »).

- `02-boss` Q4 (rangement décroissant de 5,6 ; 5,56 ; 5,65 ; 5,605) : ni a « 5,65 > 5,6 > 5,605 > 5,56 » ni
  b « 5,6 > 5,65 > … » n'appliquent « le plus long est le plus grand » ; c « 5,56 > 5,6 > 5,605 > 5,65 » est l'ordre
  croissant écrit avec « > ». → a devient « 5,605 > 5,65 > 5,56 > 5,6 » (`math.dec.compare-by-length` : 3 chiffres,
  puis 2, puis 1 — exécution exacte) ; b muette ; c → `math.num.ordre-croissant-decroissant-confondus`.
- `04-defi` Q3 : a « 0,9 < 1,01 < 0,99 < 1,1 » et c « 0,99 < 0,9 < 1,1 < 1,01 » n'exécutent pas la règle (c fait
  même l'inverse pour 0,99/0,9) → muettes (d garde son étiquette, cohérente).
- `04-defi` Q6 d « 3,04 < 3,44 < 3,4 < 4,3 » (3,44 < 3,4 : l'inverse de la règle) → muette.
- `01-pratique` Q6 c « 0,45 < 0,54 < 0,5 » (0,5 le plus grand : l'inverse de la règle) → muette.

**B1-03-5 · mineur · figure § 2 (rangs de 4,286)** : à 360 px les libellés « أجزاء من مئة » et « أجزاء من ألف »
se touchent (police 10, cases de 48 sur un pas de 56), et la phrase « الفاصلة تفصل الجزء الصحيح عن الجزء العشري »
est de la prose arabe dans le dessin (elle appartient à la légende, `course-figures.md`). Supprimer le `<text>`
de y = 132 et passer les trois libellés de rangs à `font-size="9"`.

**B1-03-6 · mineur · cours § 6** : le second piège (« الخلط بين الاتّجاهين ») n'est que nommé, sans exemple fautif
ni correction ; ajouter « من يُطلب منه الترتيب التنازليّ فيكتب 3,09 > 3,75 > 3,8 > 4,1 كتب الترتيب التصاعديّ بالرمز المعاكس: كلّ علاقة فيه خاطئة. ».

---

## 04-addition-soustraction-decimaux

**Cours** — 8 sections au patron ; tous les calculs justes (38,25, 9,95, 0,666, 67,25, 0,909, 84, 20, 91,54, 22,35,
4,55, 0,99, 7,250, 126,75, 17,75 / 13,25, 23, 3,6, 7,25, 8,4, 4,65, 112,68 encadré 112–113, 27,75, 45,615,
1,560 / 10,920 / 7,800, 4,950) ; résumé 8 ↔ 8.

**B1-04-1 · majeur · `exercices/05-entrainement.json` Q7 (balance, reprise أقيّم 10)** : les §§ 2 et 5 du cours
impriment « سلمى 38,5 kg ونادر 42,75 kg وأنيس 45,5 kg » et « 126,75 » — la réponse demandée (42,75) est dans le
cours. Garder la reprise dans le cours et passer l'exercice en **variante** : supprimer le champ `manuel` du fichier
(c'est son seul item) et remplacer Q7 par :

```json
{
  "type": "numeric",
  "prompt": "وقف ثلاثة أطفال معًا على ميزان فبلغت كتلتهم 98,5 kg. كتلة أنيس ونادر معًا 67,25 kg، وكتلة سلمى ونادر معًا 64,75 kg. ما كتلة نادر بالكيلوغرام؟ اكتب العدد فقط.",
  "answerKey": { "value": 33.5, "unit": "kg" },
  "explanation": "نبدأ بكتلة سلمى: 98,5 − 67,25 = 31,25 kg، لأنّ الثلاثة هم سلمى مع أنيس ونادر. ثمّ كتلة نادر هي ما يبقى من كتلة سلمى ونادر معًا: 64,75 − 31,25 = 33,5 kg. تحقّق: 31,25 + 33,5 = 64,75 ✓، وكتلة أنيس 67,25 − 33,5 = 33,75 kg، والمجموع 31,25 + 33,5 + 33,75 = 98,5 ✓.",
  "difficulty": 3
}
```

(Garder les champs `competencies` actuels de Q7.)

**B1-04-2 · majeur ×2 · deux `coursePitfalls` sans `::: piege`** : `math.num.virgule-perdue-dans-le-resultat` et
`math.num.zero-apres-virgule-ignore` ne sont montrés que dans le cas limite d'une `::: methode` (§ 1), jamais
diagnostiqués. Ajouter au § 1, juste après le `> ⚠️` existant (avant `::: methode`) :

```markdown
> ⚠️ **خطأ ثانٍ**: نسيان إنزال الفاصلة في النتيجة. من يجمع 1,2 + 4,3 عموديًّا فيجد الرقمين 5 و 5 ثمّ لا
> يكتب الفاصلة، يجيب 55 بدل 5,5. يغري لأنّ الحساب بعد الرصّ هو حساب الأعداد الطبيعيّة نفسه. والتقدير يكشفه:
> 1 + 4 = 5، و 55 أكبر منه بعشر مرّات.

> ⚠️ **خطأ ثالث**: إضافة الصفر في غير موضعه. من يُكمل 5,4 فيكتب 5,04 بدل 5,40 نقل الرقم 4 من الأعشار إلى
> الأجزاء من المئة فصغّر العدد. الصفر المكمّل يُكتب على يمين آخر رقم، لا بعد الفاصلة.
```

(Les distracteurs existent déjà : 01 Q4 b « 3,02 », quiz Q2 d « 38 », etc.)

**B1-04-3 · majeur ×2 · étiquettes inexactes** : `05-entrainement` Q3 d « 15,25 » (30,40 − 15,65 : le « petit du
grand » colonne par colonne donne 25,25) et Q5 d « 7,6 » (20 − 13,6 : donne 13,6) portent
`soustraction-colonne-petit-du-grand` sans l'exécuter → muettes, ou remplacer Q5 d par « 13,6 »
(`math.num.soustraction-colonne-petit-du-grand` : |0 − 6| = 6, |0 − 3| = 3, 2 − 1 = 1 — exact).

**B1-04-4 · mineur · cinq additions d1 identiques** (quiz Q2 1,5 + 2,3 ; 01 Q1 2,1 + 3,4 ; boss Q1 10,2 + 5,3 ;
03 Q1 7,2 + 2,7 ; 05 Q1 4,4 + 4,4), toutes sans retenue avec le même distracteur « virgule perdue ». Dans les deux
fichiers d3, varier : `02-boss` Q1 → « ما ناتجُ 12,6 + 7,4؟ » (20 ; distracteurs 19,10 `retenue-oubliee`, 200
`virgule-perdue-dans-le-resultat`, 20,10) ; `05-entrainement` Q1 → « ما ناتجُ 3,25 + 4,7؟ » (7,95 ; distracteurs
3,72 `decimaux-alignes-a-droite`, 795 `virgule-perdue-dans-le-resultat`, 7,32).

---

## 05-multiplication-division-decimaux

**Cours** — 7 sections au patron ; tous les calculs justes (19,5, 9,4, 6,482, 0,18, 0,035, 105 m², 350 / 45 / 450,
1 250, 700, 2,54 / 0,254, 4,56, 0,06, 36,548, 2,5, 0,375, 0,008, 8,9, 4,2, 1,75, 0,9, 3,75, 256, 36, 42 / 300 /
500, 86,45 ÷ 18,2 = 4,75 pas à pas, 164,372 encadré 150–176, 15,84, 44, 16,328) ; division par un décimal enseignée
et exercée (7 questions) conformément à §3.2 ; 6 `coursePitfalls` portés ; résumé 7 ↔ 7.

**B1-05-1 · majeur ×7 · questions qui redonnent le cours** (même calcul, même distracteur que le piège ou le cas
limite) :

- `quiz.json` Q4 (8,4 ÷ 2 ; 4,02) = piège § 5. Prompt « ما ناتجُ 8,8 ÷ 4؟ » ; options a « 2,02 »
  (`zero-intercale-dans-le-resultat`), b « 22 » (`virgule-perdue-dans-le-resultat`), c « 4,8 », d « 2,2 » ; clé d ;
  explication « نقسم الجزء الصحيح: 8 ÷ 4 = 2، ثمّ ننزل الرقم العشريّ 8 فنضع الفاصلة في الخارج: 8 أعشار ÷ 4 = 2 من الأعشار. إذن 8,8 ÷ 4 = 2,2 (نتحقّق: 4 × 2,2 = 8,8). ».
- `01-pratique` Q6 (45,6 ÷ 10 ; 456) = piège § 4. Prompt « ما ناتجُ 72,3 ÷ 10؟ » ; options a « 723 »
  (`puissance-de-dix-sens-inverse`), b « 0,723 » (`puissance-de-dix-rangs-mal-comptes`), c « 7,23 », d « 72,3 » ;
  clé c ; explication « القسمةُ على 10 تُزحزح الفاصلةَ رتبةً واحدة نحو اليسار، والعدد يصغر: 72,3 ÷ 10 = 7,23 (تحقّق: 7,23 × 10 = 72,3). ».
- `02-boss` Q1 (5,2 × 2 ; 7,2) = piège § 7. Prompt « ما ناتجُ 6,3 × 3؟ » ; options a « 18,9 », b « 189 »
  (`virgule-perdue-dans-le-resultat`), c « 9,3 » (`operation-inverse-appliquee`), d « 18,09 »
  (`zero-intercale-dans-le-resultat`) ; clé a ; explication « نحسب 63 × 3 = 189، وفي العامل 6,3 رقمٌ عشريٌّ واحد، فالجداء 18,9. والتقدير يؤكّد: 6 × 3 = 18. أمّا 9,3 فهو المجموع 6,3 + 3 لا الجداء. ».
- `02-boss` Q4 (7 ÷ 4) = cas limite § 5. Prompt « ما ناتجُ 9 ÷ 4؟ » ; options a « 2,1 », b « 2,2 », c « 0,44 »,
  d « 2,25 » ; clé d ; explication « نقسم: 9 ÷ 4 = 2 والباقي 1؛ نضع الفاصلة ونضيف صفرًا: 10 ÷ 4 = 2 والباقي 2؛ ونضيف صفرًا آخر: 20 ÷ 4 = 5. الخارج 2,25 (تحقّق: 4 × 2,25 = 9). أمّا 2,1 فيكتب الباقي بعد الفاصلة، و 2,2 يتوقّف قبل أن يصير الباقي 0. ».
- `02-boss` Q5 (12,5 × 100 ; 125) = piège § 3. Prompt « ما ناتجُ 3,75 × 1000؟ » ; options a « 3 750 »,
  b « 375 » et c « 37 500 » (`puissance-de-dix-rangs-mal-comptes`), d « 0,00375 » (`puissance-de-dix-sens-inverse`) ;
  clé a ; explication « للعدد 1000 ثلاثة أصفار، فنحرّك الفاصلة ثلاث رتب نحو اليمين ونُكمل بصفر: 3,75 → 37,5 → 375 → 3 750. ».
- `04-defi` Q4 (7,2 L ÷ 8) = cas limite § 5 « 7,2 ÷ 8 = 0,9 ». Prompt « وُزّعت 6,3 لترات من العصير بالتساوي على 9 قوارير. كم في كلّ قارورة؟ » ; options a « 7 لترات » (`virgule-perdue-dans-le-resultat`), b « 0,07 لترٍ »
  (`zero-intercale-dans-le-resultat`), c « 2,7 لترٍ », d « 0,7 لترٍ » ; clé d ; explication « المقسوم 6,3 أصغر من القاسم 9، فيبدأ الخارج بـ 0 قبل الفاصلة: 6 ÷ 9 = 0، ننزل الرقم العشريّ 3 فنضع الفاصلة، و 63 ÷ 9 = 7. إذن 6,3 ÷ 9 = 0,7 لترٍ في كلّ قارورة (تحقّق: 9 × 0,7 = 6,3). ».
- `04-defi` Q6 (« ×100 → 250 ») = propriété § 4 « 250 ÷ 100 = 2,5 ». Prompt « عددٌ قسمناه على 1000 فصار 0,045. ما هذا العدد؟ » ; options a « 4,5 » et d « 450 » (`puissance-de-dix-rangs-mal-comptes`), b « 45 »,
  c « 0,000045 » (`puissance-de-dix-sens-inverse`) ; clé b ; explication « نعكس العمليّة: القسمة على 1000 يُلغيها الضرب في 1000، فنحرّك الفاصلة ثلاث رتب نحو اليمين: 0,045 × 1000 = 45. تحقّق: 45 ÷ 1000 = 0,045 ✓. ».

**B1-05-2 · mineur · `operation-inverse-appliquee` sur une soustraction prise pour une division** (quiz Q4 c
« 6,4 » = 8,4 − 2 ; `05-entrainement` Q3 d « 8,4 » = 14,4 − 6) : le libellé énumère + / −, + / ×, × / ÷ ; − pour ÷
n'y est pas → muettes (quiz Q4 disparaît avec B1-05-1).

---

## 06-multiples-communs

**Cours** — 7 sections au patron ; tous les calculs justes (8 multiples de 7 sous 50, 420 = 12 × 35, 420 = 8 × 52 + 4,
91 = 7 × 13, 50 = 7 × 7 + 1, 35, 21, 42, 45, 42 / 6 / 48 / 20, {0, 12, 24}, 15 et 30, 12, 120 min → 10 h, 312 / 336 /
360 / 384, 67 multiples de 6 de 0 à 396, troupeau 83, 60 et 80, œufs 420 = 70 × 6 = 35 × 12 = 14 × 30, 84, 0 / 24 / 48 /
72 / 96) ; erratum n° 7 appliqué ; 6 `coursePitfalls` portés ; résumé 7 ↔ 7. C'est le chapitre où le cours, très
riche en cas limites, a été le plus souvent recopié par les questions.

**B1-06-1 · majeur ×13 · questions qui redonnent le cours.**

| question | redonne | remplacement (prompt · options · clé · explication) |
| --- | --- | --- |
| `quiz.json` Q2 | propriété § 2 « 18 = 3 × 6، لا 3 + 15 » | « هل العددُ 32 مضاعفٌ للعدد 4؟ » · a « لا » · b « نعم لأنّ 32 = 4 + 28 » · c « نعم لأنّ 32 = 4 × 8 » · d « لا لأنّ 32 لا ينتهي بالرقم 4 » · **c** · « 32 = 4 × 8، فالعدد 32 مضاعفٌ للعدد 4 (و 4 قاسمٌ له). العلاقة ضربٌ لا جمع: كتابة 32 = 4 + 28 لا تثبت شيئًا. ولا يُعرف مضاعفُ 4 من رقم آحاده: 4 × 8 = 32 ينتهي بالرقم 2. » |
| `01-pratique` Q4 | `verifie` § 1 (« الموالي للعدد 18 … 24 ») | « ما المضاعفُ الموالي للعدد 45 في مضاعفات 9؟ » · a « 46 » (`multiple-suivant-pas-ignore`) · b « 36 » (`multiple-precedent-au-lieu-du-suivant`) · c « 54 » · d « 55 » · **c** · « مضاعفاتُ 9 تزيد بـ 9 في كلّ مرّة: …، 36، 45، 54…؛ فالموالي للعدد 45 هو 45 + 9 = 54. أمّا 46 فليس مضاعفًا لـ 9، و 36 هو المضاعف السابق. » |
| `01-pratique` Q6 | cas limite § 5 (3 et 4 → 12) | « ما أصغرُ مضاعفٍ مشترك غيرِ معدوم للعددين 5 و 6؟ » · a « 30 » · b « 11 » (`ppmc-par-addition`) · c « 60 » · d « 1 » (`multiple-et-diviseur-confondus`) · **a** · « نكتب مضاعفات الأكبر 6 ونختبرها بالعدد 5: 6 و 12 و 18 و 24 ليست مضاعفات لـ 5، و 30 = 5 × 6 نعم. أمّا 11 فمجموع العددين، و 60 مضاعفٌ مشترك لكنّه الثاني، و 1 قاسمٌ لا مضاعف. » |
| `02-boss` Q2 | méthode § 4 (30 et 25 pour 2 et 5) | « أيُّ الأعداد التالية مضاعفٌ للعددين 3 و 5 معًا؟ » · a « 25 » · b « 21 » · c « 45 » · d « 50 » (a, b, d : `divisibilite-un-seul-critere`) · **c** · « العدد مضاعفٌ للعددين 3 و 5 معًا إذا كان مضاعفًا لكلٍّ منهما: 45 = 3 × 15 = 5 × 9. أمّا 25 و 50 فمضاعفان لـ 5 فقط، و 21 مضاعفٌ لـ 3 فقط. » |
| `02-boss` Q5 | propriété § 2 « 15 = 3 × 5 مضاعف لـ 3 ولـ 5 » | « أيُّ عبارةٍ صحيحة؟ » · a « 21 مضاعفٌ للعدد 3 والعدد 4 » (`divisibilite-un-seul-critere`) · b « 21 قاسمٌ للعدد 7 » (`multiple-et-diviseur-confondus`) · c « 21 مضاعفٌ للعدد 3 والعدد 7 » · d « 21 مضاعفٌ للعدد 6 » · **c** · « بما أنّ 21 = 3 × 7، فإنّ 21 مضاعفٌ للعدد 3 وللعدد 7 معًا، و 7 قاسمٌ له لا العكس. وليس 21 مضاعفًا لـ 4 (21 = 4 × 5 + 1) ولا لـ 6 (21 = 6 × 3 + 3). » |
| `03-revision` Q3 | cas limite § 5 « لـ 5 و 10 هو 10، لا 50 ولا 15 » (mêmes distracteurs) | « ما أصغرُ مضاعفٍ مشترك غيرِ معدوم للعددين 4 و 12؟ » · a « 48 » (`ppmc-remplace-par-le-produit`) · b « 4 » (`multiple-et-diviseur-confondus`) · c « 12 » · d « 16 » (`ppmc-par-addition`) · **c** · « 12 = 4 × 3، فالعدد 12 مضاعفٌ للعدد 4 وللعدد 12 معًا، ولا مضاعف غير معدوم لـ 12 أصغر منه. أمّا 48 فجداء العددين، و 16 مجموعهما، و 4 قاسمٌ مشترك لا مضاعف. » |
| `03-revision` Q5 | piège § 2 (« 7 قاسم 28 → 28 قاسم 7 ») | « إذا كان 9 قاسمًا للعدد 63، فإنّ 63 ...؟ » · a « قاسمٌ للعدد 9 » (`multiple-et-diviseur-confondus`) · b « مضاعفٌ للعدد 9 » · c « مضاعفٌ للعدد 18 » · d « لا علاقة له بالعدد 9 » · **b** · « إذا كان 9 قاسمًا للعدد 63 فإنّ 63 = 9 × 7، أي إنّ 63 مضاعفٌ للعدد 9: القاسم هو الذي يدخل في الآخر، والمضاعف هو الذي يحتويه. وليس 63 مضاعفًا لـ 18، لأنّ 63 = 18 × 3 + 9. » |
| `04-defi` Q1 | `verifie` § 4 (3 et 5 entre 1 et 40 → 15 et 30) | « ما المضاعفاتُ المشتركة للعددين 4 و 6 المحصورة بين 30 و 60؟ » · a « 48 فقط » (`ppmc-remplace-par-le-produit`) · b « 36 و 48 » · c « 36 و 48 و 60 » · d « 40 و 50 » (`ppmc-par-addition`) · **b** · « أصغر مضاعفٍ مشترك غير معدوم لـ 4 و 6 هو 12، والمضاعفات المشتركة هي مضاعفات 12: 12، 24، 36، 48، 60… وبين 30 و 60 تمامًا: 36 و 48. القفز بالجداء 24 يُسقط 36، والعدد 60 هو الحدّ نفسه فلا يُحسب. » |
| `04-defi` Q4 | propriété § 3 « كلّ مضاعف لـ 9 مضاعف لـ 3 » | « إذا كان العددُ مضاعفًا للعدد 20، فهو حتمًا مضاعفٌ للعدد: » · a « 3 » · b « 6 » · c « 8 » · d « 5 » · **d** · « بما أنّ 20 = 5 × 4، فكلّ مضاعف لـ 20 مضاعفٌ لـ 5 حتمًا: مضاعف المضاعف مضاعف. أمّا 8 فلا: العدد 20 نفسه مضاعفٌ لـ 20 وليس مضاعفًا لـ 8 (20 = 8 × 2 + 4). » |
| `04-defi` Q5 | piège § 7 (coureurs 2, 3, 4 ; mêmes 24 / 9) | « ثلاثة أجراسٍ تدقّ معًا، ثمّ يدقّ الأوّل كلّ 3 دقائق والثاني كلّ 5 دقائق والثالث كلّ 6 دقائق. بعد كم دقيقةً تدقّ الثلاثة معًا من جديد؟ » · a « 90 » (`ppmc-remplace-par-le-produit`) · b « 14 » (`ppmc-par-addition`) · c « 15 » · d « 30 » · **d** · « نحذف 3 لأنّ 6 = 3 × 2. نختبر مضاعفات 6 بالعدد 5: 6 و 12 و 18 و 24 لا، و 30 = 5 × 6 نعم. فتدقّ الأجراس معًا بعد 30 دقيقة. أمّا 90 فجداء الأعداد الثلاثة، و 14 مجموعها، و 15 مضاعفٌ لـ 3 و 5 فقط وليس مضاعفًا لـ 6. » |
| `04-defi` Q6 | propriété § 1 (« مضاعفات 7 بين 1 و 30 … 4 أعداد ») | « عددٌ محصورٌ بين 40 و 60: إذا عددناه ثلاثةً ثلاثةً بقي 2، وإذا عددناه أربعةً أربعةً بقي 2 أيضًا. ما هذا العدد؟ » · a « 48 » (`math.alg.reponse-a-l-autre-inconnue`) · b « 46 » · c « 50 » · d « 56 » · **c** · « إذا أبعدنا الباقي 2 صار العدد مضاعفًا لـ 3 ولـ 4 معًا، أي مضاعفًا لـ 12، وهو محصور بين 38 و 58: مضاعف 12 الوحيد هناك هو 48. فالعدد 48 + 2 = 50. تحقّق: 50 = 3 × 16 + 2 = 4 × 12 + 2 ✓. أمّا 48 فهو العدد بعد إبعاد الباقي، و 56 = 4 × 14 لا يترك الباقي 2. » (problème « sens inverse » : comble l'absence en d4) |
| `05-entrainement` Q4 | propriété § 1 « الرابع غير المعدوم للعدد 7 هو 28 » | « ما المضاعفُ الخامسُ غيرُ المعدوم للعدد 8؟ » · a « 32 » · b « 40 » · c « 48 » · d « 13 » (`operation-inverse-appliquee`) · **b** · « المضاعفات غير المعدومة للعدد 8 هي 8، 16، 24، 32، 40…؛ فالخامس هو 8 × 5 = 40. أمّا 32 فالرابع و 48 السادس، و 13 مجموع 8 و 5 لا جداؤهما. » |
| `05-entrainement` Q6 | propriété § 3 « كلّ مضاعف لـ 6 مضاعف لـ 2 ولـ 3 » | « إذا كان 10 قاسمًا لعددٍ، فإنّ هذا العددَ مضاعفٌ للعدد 10 وأيضًا للعددين: » · a « 2 و 5 » · b « 3 و 7 » · c « 4 و 6 » · d « 20 و 30 » (`multiple-et-diviseur-confondus`) · **a** · « بما أنّ 10 = 2 × 5، فكلّ مضاعف للعدد 10 مضاعفٌ للعددين 2 و 5 أيضًا: مضاعف المضاعف مضاعف. أمّا 20 و 30 فمضاعفان للعدد 10 لا قاسمان له: العدد 10 نفسه ليس مضاعفًا لـ 20. » |

Vérifications : 32 = 4 × 8 ; 9 + 45 = 54 ; ppcm(5, 6) = 30 ; 45 = 3 × 15 = 5 × 9 ; ppcm(4, 12) = 12 ; 63 = 9 × 7 =
18 × 3 + 9 ; multiples de 12 dans ]30 ; 60[ = {36, 48} ; ppcm(3, 5, 6) = 30 ; seul n ∈ ]40 ; 60[ avec n ≡ 2 (mod 3)
et (mod 4) : 50 ; 8 × 5 = 40. Aucune clé strictement la plus longue.

**B1-06-2 · mineur · `quiz.json` Q3** : « 1 » est une option de remplissage (l'explication l'avoue : « لا يظهران في
أيّ من القائمتين ») et « 5 » = 2 + 3 exécute `ppmc-par-addition` sans l'étiquette. b → « 2 » ; c →
`{ "id": "c", "text": "5", "misconceptionTag": "math.num.ppmc-par-addition" }` ; fin d'explication → « أمّا 12 فمضاعفٌ مشترك ثانٍ، و 5 مجموع العددين ولا يظهر في القائمتين، و 2 لا يظهر في قائمة مضاعفات 3. ».

**B1-06-3 · mineur · `01-pratique` Q1** : b « 0، 1، 2، 3، 4 » (on avance de 1) exécute
`math.num.multiple-suivant-pas-ignore` sans l'étiquette ; c « 0، 3، 5، 9، 12 » est du remplissage → « 0، 3، 6، 9 » (liste
tronquée à quatre, muette).

**B1-06-4 · mineur · `02-boss` Q1** (« 0 مضاعف لـ … كلّ الأعداد ») récite le cas limite du § 2 ; acceptable en d1
d'ouverture, à varier si l'on retouche le fichier.

**B1-06-5 · mineur · `03-revision` Q4** : énoncé négatif non souligné (« ليس من مضاعفات 4 ») → « أيُّ الأعداد التالية **ليس** من مضاعفات 4؟ ».

**B1-06-6 · mineur · cours § 2** : « b قاسم للعدد a ⟺ a مضاعف للعدد b ⟺ … » — le symbole ⟺ n'est pas de la 6ᵉ ;
écrire « b قاسم للعدد a، أي إنّ a مضاعف للعدد b، أي إنّ a يقبل القسمة على b. » (les lettres a, b, k sont celles de la
fiche §2, pas du calcul littéral : rien à changer).

**B1-06-7 · mineur · `04-defi` sans « sens inverse »** : réglé par le remplacement de Q6 ci-dessus.

---

## Ce que l'audit n'a pas trouvé (vérifié)

- Aucune clé fausse, aucune question à deux réponses, aucune explication qui contredit sa clé, aucune `short_answer`
  (donc aucune fuite d'indice), réponses `numeric` au format nombre seul (virgule ou point acceptés par le moteur).
- Aucune notion ⛔ (volume, calcul littéral, ÷ de fractions, produit en croix), aucune somme des angles (M3 sans
  objet dans le lot), « milliards » en vocabulaire seulement (§3.2).
- Division par un décimal enseignée (§ 6 du cours 05) et exercée — l'écart principal de la fiche (§2 quater) est comblé.
- Aucune option désignée par sa lettre ou son rang dans les explications (« الاختيار «…» » nomme le contenu).
- Doutes de l'auteur : n° 1 confirmé (B1-04-1) ; n° 2 (code `502603` au niveau de l'exercice) conforme ; n° 3 :
  les variantes 06 ne redonnent plus les données du manuel… mais d'autres items redonnent le cours (B1-06-1) ; n° 4
  (◐ non exercés) conforme à §3.2.
