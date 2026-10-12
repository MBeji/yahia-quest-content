# Rapport — audit indépendant du recentrage maths 9ᵉ `01-nombres-reels` / `02-racines-carrees` (2026-10-12)

Auditeur indépendant (n'a rien écrit du recentrage). Mandat : `audit-recentrage.md` (même dossier).
Rapport écrit au fil de l'eau, chapitre après chapitre.

## Contrôles mécaniques (état initial, avant toute correction de l'auditeur)

- `content:check` : vert (120 matières, 0 erreur).
- `content:qa | grep math/(01|02)-` : **0 ligne** (0 erreur, 0 avertissement).
- `content:tranche --subject math --chapters 01,02` : clé strictement la plus longue **0/101** ;
  positions a 28 · b 27 · c 27 · d 18 ; 2 paires proches (voir chapitre 01) ; 1 candidat gabarit
  (01/02-boss#2 ↔ 16-puissances/02-boss#5, « أيّ من الأعداد التالية عدد ناطق » : même cadre, savoirs
  différents — admis).

## Chapitre `01-nombres-reels` (manuel 102905, ch. 2 « مجموعة الأعداد الحقيقية IR », p. 18–30)

**Questions re-résolues à l'aveugle : 47** (quiz 5 + exercices 01–06 × 7). Toutes les clés sont
justes et uniques ; aucun distracteur défendable ; aucune explication fausse.
Vérifications chiffrées notables : 8/33 = 0,(24) ; 1/27 = 0,(037) et rang 19 → 0 ; 19/6 = 3,1(6) ;
CD = 47/20 = 2,35 ; (3,3)² = 10,89 < 11 < 11,56 = (3,4)² ; −1,74 < −√3 < −1,73 ;
2,64 < √7 < 2,65 ; 22/7 = 3,(142857) ; figure de 03-revision#4 : abscisses SVG exactes
(−√5 → x = 85,8 ; √2 → x = 304,9, échelle 60 px/unité).

**Cours** : chaque exemple, `verifie` et règle refait — tout est exact (1/11 = 0,(09) et rang 15 → 0 ;
1/7 rang 20 → 4 ; √5 entre 2,2 et 2,3 ; C′A = 4,4 ; preuve de l'irrationalité de √2 conforme à la
p. 23). Patron (amorce → définition/propriété → exemple → piège → verifie → retenir) présent dans les
cinq sections ; `resume.md` en miroir (8 puces + encadré للتوسّع).

**Périmètre** : aucune question ne teste une notion d'un chapitre ultérieur. Le débordement signalé
par la fiche §6.2 bis (valeur absolue, écriture scientifique, ordre, intervalles) est bien absent.
L'encadré « 🚀 للتوسّع » (somme rationnel + irrationnel, ch. 3) est final, sans `piege`, sans `verifie`,
sans item. ℝ+ / ℝ−, 2√2, −2√2, √((−8)²), (√20)² sont **dans** le manuel (p. 21, 25, 30 ex. 11).
Remarque (non bloquante) : 02-boss#1, 03-revision#5, 05-entrainement#1 sont du pur calcul sur les
relatifs (acquis de 7ᵉ) — pas un débordement au sens du mandat, mais ils ne testent aucun savoir du
chapitre ; le manuel p. 19 (استحضر) ne les rappelle pas sous cette forme.

**Étiquettes** : toutes conformes au libellé du registre. `coursePitfalls` (5 ids) : chacun énoncé par
un piège du cours et porté par au moins un distracteur (C-5 ✓). Nuances non bloquantes :
04-defi#3 b « 400 و −8 » cumule deux erreurs (carré au lieu de racine + racine négative), étiquetée
par la seconde seulement ; 06-defi-concours#4 a « 2,6 » mêle confusion défaut/excès et mauvaise
précision.

**Paires proches** (tranche) : quiz#1 ↔ 03-revision#3 (chaîne entière vs une inclusion) et
01-pratique#2 ↔ 02-boss#2 (« lequel est irrationnel » vs « lequel est rationnel ») — exercices
parallèles voulus, admis.

**Erreurs corrigées : aucune.**
**Verdict : conforme.** Clarté : 5/5.

Remarques de patron (non bloquantes, antérieures au recentrage) : section 1, la figure (T3) précède
la définition (T2) ; section « الجذر التربيعي », le paragraphe « من أين يأتي √2 » + figure (T3) vient
après le piège (T5) ; section « تدريج مستقيم » sans piège (T5 seulement recommandé).

## Chapitre `02-racines-carrees` (manuel 102905, ch. 3 §IV p. 39–40, déf. p. 27)

**Questions re-résolues à l'aveugle : 45** (quiz 5 + 01-pratique 6 + 02-pratique 6 + 03-revision 7 +
04-defi 7 + 05-entrainement 7 + 06-defi-concours 7). Toutes les clés sont justes et uniques.
Vérifications notables : (√48 − √12)/√3 = 2 ; √50 + √8 − √18 = 4√2, A² = 32 ; √((√5 − 3)²) = 3 − √5 ;
périmètre 2(3√3 + 4√3) = 14√3 ; 3/(√7 − 2) = √7 + 2 ; (5√3)/((2√27)/5) = 25/6 (= ex. 16 b p. 46) ;
(3 + √5)(3 − √5) = 4 ; (√13)² + √((−7)²) = 20 ; √18 × √8 = 12.

**Cours** : tous les exemples, `verifie` et règles refaits — exacts. `√(a²) = |a|` est bien dans §IV
(encadré p. 39) ; |a| lui-même est enseigné au ch. 3 §III = `19-valeur-absolue`, dont le
`displayOrder` (3) précède celui de `02` (4) : acquis antérieur, admis.

### Erreurs corrigées (correction minimale, aucune métadonnée ni nombre de questions changé)

1. `exercices/04-defi.json#4` (1/(√5 + 2)), option c et explication : distracteur incohérent avec
   l'erreur qu'il prétend porter (`math.alg.difference-carres-second-terme-non-eleve-au-carre`) —
   multiplier par le conjugué √5 − 2 et calculer le dénominateur 5 − 2 = 3 donne (√5 − 2)/3, pas
   (√5 + 2)/3 ; l'explication affirmait le contraire.
   Avant : `(√5 + 2) / 3` (option et explication) → Après : `(√5 − 2) / 3` (option et explication).
   L'étiquette dit maintenant exactement l'erreur ; la clé (`√5 − 2`) reste la plus courte.
2. `cours.md`, section « تبسيط الجذور », piège : les exemples de « l'échange des deux facteurs »
   étaient faux ou hors sujet (`√50 = 2√25` ; `√8 = 4√2` est l'erreur « sortir le carré sans en
   prendre la racine », pas l'échange).
   Avant : `فيُكتب √50 = 2√25 أو √8 = 4√2` → Après : `فيُكتب √50 = 2√5 بدل 5√2، أو √75 = 3√5 بدل 5√3`
   (exactement les distracteurs 01-pratique#3 b et 02-pratique#3 a, et le libellé du registre).
3. `cours.md`, même section, encadré 🗡️ : l'affirmation « √50 = √(2 × 25) : en commençant par le petit
   facteur il faudrait une étape de plus » est fausse (l'ordre des facteurs ne change rien).
   Avant : `√50 = √(25 × 2) = 5√2 في خطوة واحدة، بينما √50 = √(2 × 25) لو بدأت بالعامل الصغير لاحتجت خطوة إضافية`
   → Après : `√72 = √(36 × 2) = 6√2 في خطوة واحدة، بينما لو بدأت بالمربّع الأصغر 4 لوجدت √72 = √(4 × 18) = 2√18 ولاحتجت خطوة إضافية: √18 = 3√2`.

### Périmètre

- Aucune question sur Pythagore, identité remarquable nommée, puissances, ordre/intervalles :
  les réécritures du rédacteur tiennent. L'encadré « 🚀 للتوسّع » (Pythagore, a² − b²) est final, sans
  `piege` / `verifie` / item ; `resume.md` en miroir.
- Reste à arbitrer (voir plus bas) : les items de **rationalisation** — quiz#4 ; 02-pratique#1, #6 ;
  03-revision#2, #7 ; 04-defi#2 (consigne seulement), #4 ; 05-entrainement#3 ; 06-defi-concours#4,
  et l'explication de 06#7 (10 items, dont 2 `short_answer` qui font nommer « إنطاق المقام » et
  « المرافق », termes absents du manuel).
- Mentions hors encadré (non testées) : l'épigraphe (« … ونظرية فيثاغورس ») et la ligne finale 🏆
  (« مع فيثاغورس ») nomment Pythagore hors de l'encadré للتوسّع — à reformuler éventuellement.
- Le `verifie` de la section 1 utilise √(25/49) = √25/√49 (« الجذر يوزَّع على البسط والمقام ») avant
  que la section 3 n'enseigne la règle du quotient ; à corriger en « لأنّ (5/7)² = 25/49 » seulement.

### Étiquettes et `coursePitfalls`

`coursePitfalls` (8 ids) : chacun énoncé par un piège du cours ET porté par au moins un distracteur
(C-5 ✓, y compris après ma correction de 04-defi#4, qui garde son étiquette). Le retrait de
`math.geo.pythagore-sans-carres` et l'ajout de `math.num.radicaux-semblables-radicande-additionne`
sont justes. Candidat à l'ajout (facultatif) : `math.num.racine-negatif-existe` — énoncé par le piège
« لا يوجد جذر تربيعي لعدد سالب » et porté par 01-pratique#5 c et 04-defi#3 c.
Nuance non corrigée : 04-defi#7 `expectedMistakes` « المقابل » est étiqueté
`racine-carre-sans-valeur-absolue` ; `valeur-absolue-toujours-oppose` (utilisé pour « −a » au quiz#2 b
et 04-defi#3 d) serait plus exact et cohérent — défendable dans les deux cas, donc listé seulement.

### Remarques

- `chapter.json` `manuel.pages = "27, 39-40"` : les items de produit de conjugués et de
  rationalisation s'appuient sur p. 37 (n° 4, n° 7) et p. 46–47 (n° 11, 12, 16, 17) — à élargir si
  l'arbitrage garde la rationalisation.
- quiz#2 et 05-entrainement#4 portent la compétence `math.num.ordre-encadrement` sans rapport avec
  l'item (métadonnée, laissée).
- 05-entrainement#3, explication : « التحقّق: 2√5 = 2√5 » est une tautologie (le contrôle par les
  carrés qui suit est juste).
- Clés réparties (tranche : a 28 · b 27 · c 27 · d 18 sur les deux chapitres), aucune clé
  strictement la plus longue.

**Verdict : conforme après corrections** (3 corrections), sous réserve de l'arbitrage
« rationalisation ». Clarté : 4/5 (cours clair ; les deux scories ci-dessus et le vocabulaire
non officiel « إنطاق المقام » coûtent un point).

## Contrôles après corrections (depuis `/home/user/eng-arabe`)

- `content:check` : vert. `content:qa` : 0 ligne pour `math/01-` et `math/02-` (le `grep` du mandat
  attrape aussi `french-bac-math/01-…` et `math-bac-math/02-…` : sans rapport).
- `content:tranche` : 0/101 clé la plus longue ; 2 paires proches (ch. 01, admises).
- Prettier `--check` sur les `.json` : les fichiers du recentrage et ma correction sont propres ; **3
  fichiers échouent, tous des missions de l'étude 36** non touchées : `01/07-devoir-…`,
  `01/08-devoir-…`, `02/07-devoir-…` (à reformater par la session qui les possède).
- Rendu `renderLesson` / `renderSummary` des quatre fichiers : 0 `**`, 0 `:::` résiduel ; un seul
  `&gt;` (« b &gt; 0 », texte légitime). Artefact moteur constaté (pas de contenu) : chaque liste dans un
  bloc `:::` se ferme par `<p></ul></p>` (10 fois dans 01/cours, 9 dans 02/cours).

## Les deux points d'arbitrage

### 1. « إنطاق المقام / المرافق » — recommandation : **GARDER la technique, retirer le vocabulaire**

Preuve (manuel lu, pagination imprimée = pagination PDF, vérifiée sur p. 46 et 47) :
- p. 47, ex. **17** : « أحسب a = 2/(√2 + 1) − 1/(√2 − 1) ; b = 3/(√3 + 2) − 4/(√3 − 2) ;
  c = √7/(√7 + √5) − √5/(√7 − √5) » — impossible sans multiplier par le conjugué (ou réduire au
  dénominateur commun, qui est le même produit de conjugués) ;
- p. 46, ex. **16 c** : ((1 − √2)/(1 + √2) − (1 + √2)/(1 − √2))/(2√2) — même geste ;
- p. 46, ex. **11–12** (a = √12 + √11 inverse de b = √12 − √11 ; 2 − √3 inverse de 2 + √3) et p. 37,
  أطبق n° 4 (3 − 2√2 inverse de 3 + 2√2), n° 7 ((√2 + 1)(√2 − 1)) : le produit de conjugués par
  double distributivité est au programme.
- Mais : **ni le terme « إنطاق المقام » ni « المرافق » n'apparaissent** dans le manuel ; aucun encadré,
  aucune méthode (fiche §6 « ABSENT », confirmée sur les pages).

Donc la compétence est exigée, le nom ne l'est pas. Je recommande : garder les items de calcul
(quiz#4 reformulé, 02-pratique#1, 03-revision#2, 04-defi#2, #4, 05-entrainement#3, 06#4) ;
**réécrire les deux `short_answer` qui font nommer un terme hors manuel** (02-pratique#6 « المرافق »,
03-revision#7 « إنطاق المقام ») en items de calcul ; dans le cours, présenter la section comme
« كسر مقامه به جذر : كيف نتخلّص من الجذر » avec le terme en incise (« ويسمّى ذلك أحيانًا إنطاق
المقام ») ; élargir `manuel.pages` à « 27, 37, 39-40, 46-47 ».

### 2. Missions de l'étude 36 hors chapitre — constat seulement (non touchées)

- `01/08-devoir#6` : 3²⁰²¹/(3²⁰²⁰ + 3²⁰¹⁹) — **puissances, ch. 4** (`16-puissances`) : hors chapitre,
  confirmé.
- `01/08-devoir#7` : réutilise ce résultat, mais **donné** dans l'énoncé (« ونعلم أنّ … = 9/4 ») ; la
  tâche (E ∩ ℚ) est du ch. 2. L'explication utilise √(14/9) = √14/3 (règle du quotient, ch. 3).
  Hors chapitre par dépendance à #6 seulement — léger.
- `01/08-devoir#1` : la question (√(27/12) = √(9/4) = 3/2) est du ch. 2 ; seule **l'explication** d'un
  distracteur passe par √27 = 3√3 (forme a√b, ch. 3). Léger : reformuler l'explication suffit.
- `02/07-devoir` porte surtout sur les ensembles (ch. 2, chapitre antérieur) : pas un débordement,
  mais un décentrage du chapitre « racines ». `01/07-devoir#5` mobilise la divisibilité (acquis 7ᵉ) :
  admis.
- Les trois missions échouent au `prettier --check` (voir contrôles).

## Suites appliquées (rédacteur, 2026-10-12)

Arbitrage 1 retenu : garder les items de calcul de rationalisation, retirer le vocabulaire non officiel
(« إنطاق المقام » / « المرافق » absents du manuel 102905).

- `02-pratique#6` (nommait « المرافق ») → item de calcul, type `numeric` (le validateur refuse un
  `short_answer` à réponse numérique) : « احسب المقام الجديد (√7 − 2)(√7 + 2) » = 3 (7 − 4), re-résolu
  deux fois ; difficulté 3 et compétence inchangées, 6 questions.
- `03-revision#7` (nommait « إنطاق المقام ») → `numeric` : « 5/√10 = √10/k, احسب k » = 2
  (5√10/10 = √10/2), re-résolu deux fois ; difficulté 3 et compétence inchangées, 7 questions.
- `cours.md` : titre de section « إنطاق المقام » → « كسر مقامه جذر: كيف نتخلّص منه » ; le terme n'apparaît
  plus qu'une fois, en incise (« ما يُسمّى أحيانًا… ») ; « مرافق / conjugué » remplacé par « العبارة √a − b » ;
  exemple, méthode, `verifie`, `retenir` reformulés sans le terme ; patron intact. `resume.md` : même
  traitement (puce renommée, incise unique).
- Pythagore : épigraphe → « … وحساب الأطوال في الهندسة » ; ligne 🏆 → « … في الهندسة وحساب الأطوال ».
  L'encadré 🚀 (final, sans item) garde son nom.
- `chapter.json` : `manuel.pages` « 27, 39-40 » → « 27, 37, 39-40, 46-47 » ; description « إنطاق المقام » →
  « التخلّص من الجذر في المقام ».
- `04-defi#7` : étiquette de « المقابل » `racine-carre-sans-valeur-absolue` →
  `math.num.valeur-absolue-toujours-oppose` (id existant ; libellé « tu prends l'opposé dans tous les cas »
  = l'erreur exacte).
- Passe complémentaire (tous les items du ch. 02 hors devoirs) : « إنطاق المقام » / « المرافق » / « اُنطق » retirés
  des énoncés, explications et titre, sans toucher clés, options ni métadonnées : `quiz#4` (« ما الهدف من كتابة
  كسر مثل 1/√3 بمقام خالٍ من الجذر؟ »), `02-pratique` (titre + #1), `03-revision#2` et `05-entrainement#3`
  (« اكتب الكسر … بدون جذر في المقام »), `04-defi#2` et `#4` (« تخلّص من الجذر في مقام… », indice « اضرب في
  √5 − 2 »), `06-defi-concours#4` et l'explication de `#7`. Reste : l'incise unique de `cours.md` et celle de `resume.md`.
- Contrôles : `content:check` vert ; `content:qa` 0 ligne `math/01-` et `math/02-` ; `content:tranche` clé la
  plus longue 0/101 ; Prettier `--check` propre sur les `.json` touchés ; rendu : 0 `**`, 0 `:::`,
  un seul `&gt;` (cours.md, comparaison mathématique).
