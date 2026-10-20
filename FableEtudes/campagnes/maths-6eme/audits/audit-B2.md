# Audit B2 — maths 6ᵉ, chapitres 07 à 12 (auditeur indépendant, opus)

> Valide pour `content/math-6eme/{07-criteres-divisibilite, 08-fractions-sens-lecture, 09-fractions-equivalentes,
> 10-comparaison-fractions, 11-addition-soustraction-fractions, 12-fractions-decimales}` tels qu'au commit
> `a0e47daa` (branche `wip/maths-6eme-un-passage`, aucun changement non commité dans le lot). Ré-auditer si ces
> fichiers bougent. 2026-10-19.
>
> Protocole : re-résolution à l'aveugle de **chaque** question (306 : 6 quiz + 30 exercices) avant de lire clés et
> explications ; lecture intégrale des 6 cours et 6 résumés, chaque exemple, piège et `verifie` recalculé ; reprises
> confrontées à la fiche et au PDF (`102609` ص 71, 76, 84, 88, 127, vision 90 dpi) ; rendu vitest
> (`renderLesson` / `renderSummary`) + Chromium 360 px avec les règles bidi de `src/styles.css` ; les quatre gates.
> Rapport et notes de l'auteur lus **après** la re-résolution. Rien n'a été écrit dans `content/`, aucune écriture git ;
> fichiers jetables supprimés (test vitest dans `eng-deliver`).

## Verdict : **à corriger** (0 critique, 100 majeurs, 37 mineurs)

**306/306 clés justes**, une seule réponse défendable partout sauf un cas d'ambiguïté de lecture (09 quiz Q6),
aucune option désignée par sa lettre ou son rang, cours justes en mathématiques et en arabe (une égalité
trompeuse au ch. 10), aucune notion ⛔ (le PGCD du ch. 09 est **dans la borne**, voir § Point tranché),
`coursePitfalls` tous montrés dans un piège ET portés par un distracteur, figures vraies, gates verts.

Ce qui bloque est la même famille que l'audit B1, en plus massif :

1. **Questions qui redonnent un exemple, un piège ou un `verifie` du cours** (mêmes nombres, souvent le même
   distracteur que le piège) : **~75 questions**. Deux origines :
   - *questions de l'auteur* qui recopient le cours (ch. 11 : 20 questions sur 52 ; ch. 12 : 16) → **la question
     est remplacée** (variante, même rang, même difficulté) ;
   - *reprises du manuel* (`manuel.items`) dont le cours a pris **les mêmes données** pour ses exemples (le cours
     a puisé dans les exercices du manuel au lieu de ses activités) → **le cours change de nombres**, la reprise
     reste (ch. 07, 09, 12) ; ou, quand le cours est bâti sur l'activité entière, **la question devient une variante
     et l'item sort de `manuel`** (ch. 08, 10).
2. **Notation cassée au rendu** : 8 énoncés écrivent l'inconnue `؟` **dans** la formule (`2/3 = ؟/12`) — le `؟`
   est un caractère arabe fort, la formule se retourne (`55/؟ = 11/3` s'affiche `11/3 = ؟/55`, constaté dans
   Chromium). Le cours, qui écrit `…`, s'affiche juste.
3. **Doublons internes** (07, 08, 09, 10, 11) et **quatrième option hors sujet** dans « أيّ الكسرين أكبر: x أم y ? »
   (ch. 10, 5 questions : une fraction qui n'est aucun des deux candidats, éliminée à vue).
4. Quelques étiquettes inexactes, deux reprises non déclarées (09/03, 09/04-Q7), une égalité trompeuse du cours 10,
   une explication fausse (10/05-Q7).

| chapitre | questions re-résolues | clés fausses | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- | --- |
| 07-criteres-divisibilite | 52 | 0 | 0 | 11 | 7 |
| 08-fractions-sens-lecture | 52 | 0 | 0 | 14 | 6 |
| 09-fractions-equivalentes | 50 | 0 | 0 | 14 | 7 |
| 10-comparaison-fractions | 48 | 0 | 0 | 19 | 5 |
| 11-addition-soustraction-fractions | 52 | 0 | 0 | 20 | 6 |
| 12-fractions-decimales | 52 | 0 | 0 | 22 | 6 |
| **total** | **306** | **0** | **0** | **100** | **37** |

Toutes les corrections proposées sont des remplacements **au même rang, même difficulté, même id de clé** (aucun
identifiant ne bouge, aucun ajout). Chaque valeur a été recalculée (`fractions.Fraction`) ; pour les 70 jeux
d'options neufs, la clé n'est **jamais strictement la plus longue** (mesuré) ; une seule réponse défendable ;
aucune fuite dans les explications ; distracteurs étiquetés seulement quand l'option exécute exactement l'erreur.
Les nombres à plusieurs classes gardent l'espace insécable U+00A0.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : 0 erreur ; 3 avertissements, tous en `14-…` (hors lot).
- `content:figures:check` ✓.
- `content:tranche -- --subject math-6eme --chapters <6 slugs> --fresh --strict-longest --strict-lessons` ✓ :
  clé strictement la plus longue **0/81** ; 11 paires proches (10 en 07, 1 en 10) — jugées ci-dessous ; patron
  de notion 0 en recul.
- Scans (hors `<svg>`) : 0 chiffre arabo-indien, 0 LaTeX, 0 `$…$`, 0 groupe `\d \d{3}` en espace simple, 0 virgule
  arabe en notation. Lettres latines côté élève : voir mineurs 08 et 09.

## Rendu

vitest jetable (`renderLesson`/`renderSummary` sur les 12 fichiers + toutes les questions à figure), Chromium
1194 à 360 px avec les règles `.lesson-table … unicode-bidi: plaintext`, `.math-run`, `.lesson-math` de
`src/styles.css` : `scrollWidth` = 360 sur les 18 pages ; tableaux lisibles (`8 ÷ 4`, `2/3 < 1` dans le bon sens
une fois la règle `plaintext` appliquée). Figures re-dérivées, **toutes vraies** : 07 (471 → 12) ; 08 (3/4 en
bande ; quarts 0→1 ; 3/4, 4/4, 5/4 ; 20 → 4 × 5 ; questions : carré en 8 triangles congruents dont 3 colorés,
rectangle 9 parts **inégales** (colonnes et lignes de largeurs différentes), diagramme 50/300/200/600/100/50 =
1300, 7/4 au 3ᵉ quart après 1, 9/12 colorés, grille 6 × 6) ; 09 (1/2, 2/4, 3/6 ; 2/3 = 8/12 ; 6/8 = 3/4 ;
bordure 4 × 4 = 12) ; 10 (11/9 et 13/9 au 2ᵉ et 4ᵉ neuvième après 1 ; 5/6 vs 5/7 ; 24/3…27/3 ; 5/8, 2/3, 5/6 aux
graduations 15, 16, 20 de 24) ; 11 (5/20 + 3/20 ; 7/4 ; 2/8 + 3/8 + 3/8 ; 7/9 + 2/9) ; 12 (25/100 en 2 colonnes +
5 ; 6/100, 1/4, 0,75, 0,85, 1, 3/2 ; 35/100).

- **Défaut de rendu confirmé (contenu)** : `؟` dans une formule → voir 09 M-13 et 12.
- **Défaut de rendu du MOTEUR (hors lot, à signaler au pilote)** : un `> ⚠️` de plusieurs lignes est rendu en
  **un fragment + un `<p>` par ligne suivante** (`renderLesson` : `…لأنّه ضرب البسط 3 في 5، وهو` puis
  `<p>العدد الظاهر في المقام القديم…</p>`). Chaque piège promu du corpus se lit coupé au milieu d'une phrase. Rien à
  corriger dans le contenu ; c'est le passage de promotion des `> ⚠️` dans `src/shared/lib/markdown.ts`.

## Point tranché — « القاسم المشترك الأكبر » au ch. 09 (question du pilote)

**Ce que dit la fiche, mot pour mot** — §3.2, ligne « Fraction irréductible ; PPCM » : classement « ✅ (réduire
jusqu'au bout …) — ⛔ la définition par « nombres أوّليّين فيما بينهما » et **le PGCD formalisé** » ; colonne
« conséquence » : « inchangé (« **le plus grand diviseur commun cherché parmi les diviseurs** » ✅, 2026-09-23) ».
Le §2 quinquies précise : « ✅ simplifier « en une fois » par **le plus grand diviseur commun, cherché parmi les
diviseurs** — sans algorithme ni décomposition (le « PGCD formalisé » reste ⛔) ». §3.3 : ⛔ « décomposition en
facteurs premiers et PGCD formalisé ».

**Ce que fait le chapitre** : section 5 du cours, méthode « قواسم أصغر العددين من الأكبر نزولًا، أوّلُ قاسم يقسم
الآخر » ; aucun algorithme d'Euclide, aucune décomposition, aucune notation PGCD(a ; b), aucune propriété ;
04-defi Q2 demande le nombre (12 pour 24/36), 12 explications l'emploient. **C'est exactement la technique
✅ de la fiche → dans la borne ; aucun item ne sort.**

Ce qui frôle la « formalisation », et que je corrige (mineur, 09 m-4) : le cours en fait un **terme défini** dans un
bloc `::: definition` avec la glose française « (plus grand commun diviseur) » — c'est le nom du PGCD, que le
manuel ne prononce jamais (fiche §2 quinquies, écart 2). Remplacer le bloc par une description :

```
::: definition
Parmi القواسم المشتركة لعددين نبحث عن **أكبرها**: أكبر عدد يقسم كلًّا منهما. نسمّيه القاسم المشترك الأكبر،
ونجده بين القواسم كما في المثال. إذا قسمنا عليه البسط والمقام وصلنا إلى أبسط صورة في خطوة واحدة:
$$ 48/36 = (48 ÷ 12)/(36 ÷ 12) = 4/3 $$
:::
```

(au lieu de `**القاسم المشترك الأكبر** (plus grand commun diviseur) لعددين هو أكبر عدد يقسم كلًّا منهما. إذا قسمنا`
+ `عليه البسط والمقام وصلنا إلى أبسط صورة في خطوة واحدة:`). L'item 04-defi Q2 reste ; son explication est
enrichie (09 M-12). Si le pilote préfère ne pas nommer du tout la notion, l'item se reformule : « ما أكبرُ عددٍ يقسم
24 و36 معًا، فنختزل به 24/36 دفعةً واحدة إلى أبسط صورة؟ » (mêmes options, même clé).

## Reprises (champ `manuel`) — confrontées

Fiche §2 quinquies / nonies (relue R-7) + PDF `102609` ouvert à ص 71 (L25 ex. 3–7), 76 (L26 ex. 5–7), 84 (L28
ex. 11–14), 88 (L29 ex. 8–10), 127 (L42 ex. 3–6, notation RTL relue) ; guide `502603` p.189/193–194 via la fiche
(T3 sit. 1). **Données conformes** pour toutes les reprises déclarées (2170 ; 1003–1025 ; 995 ; 2607/5014/1204/189 ;
1035 ; 75 420 ; 40/60 ; 7/24 ; 40 دكل/75 ل ; 14/11 & 2/3 ; 26/53 & 2/5 ; (7/5 − 3/5) + 2/9 lu RTL ; 3/2 + 1/3 ; 5/8 − 4/7 ;
9,600 د/45 m ; 3/5 & 5/7 ; 209 ل ; 3,5/10 ; 21/300 ; 405/100 ; 8 frères 2/7 & 1/3 → 8/21, 125 m² → 1000 m²).
Errata : n° 25–28 (L25), 29–33 (L28), 56 (L29), 58 (L42) sans effet sur les items repris ; L31 ex. 12 repris
**avec** l'erratum p.201 (2/5). Écarts d'étiquetage (déclaration) : 07/04 (M/m), 09/03 et 09/04-Q7 (M), 10/05
et 12/04 (m) — détaillés par chapitre.

---

## 07-criteres-divisibilite — 52 questions, 0 clé fausse, 11 majeurs, 7 mineurs

Cours : 8 sections au patron (T1→T2→T3→T4→T5→T6→T7→retenir), chaque exemple, piège et `verifie` recalculé
(314 = 5 × 62 + 4 ; 1040 = 3 × 346 + 2 ; 2318 = 9 × 257 + 5 ; 360 ; …) : justes. Résumé 8 puces ↔ 8 sections.

### Majeurs

**07 M-1 à M-4 — reprises dont le cours imprime déjà la réponse** (corriger le **cours**, les reprises restent) :

| question (reprise) | cours | remplacement exact dans `cours.md` |
| --- | --- | --- |
| 02-boss Q8 (L26 ex. 7ب, 2607 → 6) | l. 368 | `نفسه: 2607 مجموع أرقامه 15، وباقيه على 9 هو 6 لا 15 (2607 = 9 × 289 + 6).` → `نفسه: 3508 مجموع أرقامه 16، وباقيه على 9 هو 7 لا 16 (3508 = 9 × 389 + 7).` |
| 02-boss Q10 (L25 ex. 7, 995) | l. 323–324 | `وأكبر عدد من ثلاثة أرقام يقبل` / `القسمة على 5 هو 995، لأنّ 999 و998 و997 و996 لا تنتهي بـ 0 ولا بـ 5.` → l. 324 : `القسمة على 2 هو 998، لأنّ 999 فرديّ.` |
| 04-defi Q5 (L26 ex. 4, 45▢0 → 2) | l. 323 | `45▢0 يعطي 4500 و4590` → `72▢0 يعطي 7200 و7290` (7 + 2 + 0 = 9 ⇒ ▢ = 0 ou 9 ✓) |
| 02-boss Q9 (L25 ex. 9, 3054) | l. 130 | `ومثله 3054: زوجيّ` → `ومثله 5034: زوجيّ` |

**07 M-5 — 05-entrainement Q8 doublonne 02-boss Q9** (mêmes quatre nombres 4053/3054/3045/3450, même fait).
Remplacer 05-Q8 par une variante et retirer `"L25 ex. 9"` de `05-entrainement.json › manuel.items` :
- prompt : `اربط كلَّ عددٍ بالجملة التي تصفه، علمًا أنّ هذه الأعداد كوّنّاها بالأرقام 1 و6 و5 و0:`
- gauche : l1 `5061`, l2 `1056`, l3 `1605`, l4 `1650` (droite et paires inchangées : r1 ni 2 ni 5, r2 2 seulement,
  r3 5 seulement, r4 les deux).
- explication : `نقرأ رقم الآحاد: 5061 آحاده 1 فلا يقبل أيًّا منهما، و1056 آحاده 6 زوجيّ غير 0 فيقبل القسمة على 2 فقط، و1605 آحاده 5 فيقبل القسمة على 5 فقط، و1650 آحاده 0 فيقبلهما معًا.`

**07 M-6 — 01-pratique Q6 : indice de forme** (trois « لا » contre un seul « نعم » : si la réponse était « non »,
deux options seraient justes ⇒ la clé se devine) **et** le nombre 234 est celui du piège du cours. Remplacer Q5 et
Q6 (même nombre, chaînés) par 438 :
- Q5 prompt `ما مجموعُ أرقام العدد 438؟` ; a `13`, b `14`, c `16`, **d `15`** ; explication
  `مجموعُ أرقام 438 هو 4 + 3 + 8 = 15 (نستعمله لاختبار القسمة على 3 و9).`
- Q6 prompt `هل يقبل العددُ 438 القسمةَ على 3؟` ; a `لا، لأنّ آحاده ليس 0 ولا 5` [critere-divisibilite-mal-choisi],
  b `لا، لأنّ آحاده 8 لا 3` [critere-divisibilite-mal-choisi], c `نعم، لأنّه عددٌ زوجيّ` [critere-divisibilite-mal-choisi],
  **d `نعم، لأنّ مجموع أرقامه 15`** ; explication `مجموعُ أرقام 438 هو 4 + 3 + 8 = 15، و15 مضاعفٌ للعدد 3، فالعددُ 438 يقبل القسمة على 3: 438 = 3 × 146. رقمُ الآحاد لا يكفي هنا، وكونُ العدد زوجيًّا يخصّ القسمة على 2 لا على 3.`

**07 M-7 — 03-revision Q2 : même indice de forme** (trois « لا »). Options : a `لا، لأنّه عددٌ زوجيّ`
[critere-divisibilite-mal-choisi], b `لا، لأنّه ينتهي بالرقم 0` [critere-divisibilite-mal-choisi], c `نعم، لأنّه ينتهي بالرقم 0`
[critere-divisibilite-mal-choisi], **d `نعم، لأنّ مجموع أرقامه 9`** ; explication inchangée + `ورقم الآحاد 0 يخصّ القسمة على 10 لا على 9.`

**07 M-8 — 02-boss Q5 redonne le cas limite du cours** (« 42 زوجيّ، و4 + 2 = 6 »). Options : a `25`, b `33`
[divisibilite-un-seul-critere], c `44` [divisibilite-un-seul-critere], **d `78`** ; explication
`العددُ 78 زوجيّ (يقبل القسمة على 2) ومجموعُ أرقامه 7 + 8 = 15 (يقبل القسمة على 3)، فهو يقبل القسمة على 2 و3 معًا: 78 = 6 × 13.`

**07 M-9 — 03-revision Q3 redonne le cas limite du cours** (65). Remplacer c `65` → **c `85`** ; explication
`آحادُ 85 هو 5 فيقبل القسمة على 5 (85 = 5 × 17)، وهو فرديّ فلا يقبلها على 2.`

**07 M-10 — 03-revision Q6 redonne le cas limite du cours** (250). Options : a `475` [divisibilite-un-seul-critere],
b `704` [divisibilite-un-seul-critere], **c `470`**, d `74` [divisibilite-un-seul-critere] ; explication
`العددُ يقبل القسمة على 2 و5 و10 معًا إذا كان آحاده 0؛ آحادُ 470 هو 0، فهو يقبلها جميعًا (470 = 10 × 47).`

**07 M-11 — 01-pratique Q1, étiquette fausse** : b `أن ينتهي بالرقم 1` porte `critere-divisibilite-mal-choisi`
(« le critère d'un autre diviseur ») ; « finir par 1 » n'est le critère d'aucun diviseur → **retirer l'étiquette**.

### Mineurs

- **m-1** 02-boss Q4 b `9 فقط` : deux erreurs (affirme 9, oublie 5 et 3) → étiquette à retirer (option muette).
- **m-2** 05-entrainement Q6 d `على 9 فقط` : deux erreurs → aucune étiquette (déjà muette ✓) ; b reste étiquetée ✓.
- **m-3** 04-defi : `manuel.items` cite `L26 ex. 7ب` mais aucune question n'en reprend les données (Q7 7481 est une
  variante) → retirer `"L26 ex. 7ب"`.
- **m-4** Cours l. 322, cas limite « العدد لا يبدأ بالصفر » illustré par ▢71, où 0 ne convient de toute façon pas
  (8 + 0 = 8). Remplacer `ففي ▢71 للقسمة على 3 تصلح 1 و4 و7 فقط (171 و471 و771).` →
  `ففي ▢51 للقسمة على 3 تصلح 3 و6 و9 فقط (351 و651 و951)، لأنّ 051 ليس عددًا من ثلاثة أرقام.`
- **m-5** 02-boss Q3 (24) = contre-exemple « (93 و24) » du cours ; 01-pratique Q7 contient 207, exemple résolu
  du cours (reprise L26 ex. 3أ : tolérable, une option sur quatre).
- **m-6** Paires proches de la tranche (02-Q6 ↔ 04-Q2 ↔ 05-Q5 « plus grand / plus petit chiffre » ; quiz Q3 ↔
  01-Q6 ; quiz Q6 ↔ 02-Q8 ↔ 04-Q7 « reste ») : savoir-faire parallèles à données différentes dans des
  missions distinctes — **justifiées**, sauf celles corrigées en M-5/M-6.
- **m-7** Contexte : la section 6 compte les « تلاميذ السنة التاسعة » (manuel L26 ex. 11) — conforme au manuel.

---

## 08-fractions-sens-lecture — 52 questions, 0 clé fausse, 14 majeurs, 6 mineurs

Cours : 7 sections au patron ; accords nombre–nom vérifiés (تسعة أخماس، سبعة عشر تسعًا، ثلاثون سدسًا، ثلاثة
وعشرون نصفًا, règle 3–10 pluriel / 11–99 singulier ✓) ; calculs justes (7 × 1,3 = 9,1 ; 0,34 × 4 = 1,36 ; 18/5 = 3,6 ;
600/300 = 2 ; 50 + 15 + 10 + 25 = 100). Résumé 7 ↔ 7.

### Majeurs

**08 M-1 — le « sens inverse » (le tout à partir d'une partie) n'est enseigné que dans deux phrases d'un cas
limite** (`::: methode`, « وبالعكس، إذا كان 1/5 من عدد يساوي 7 … وإذا كان 3/4 من قسم 18 تلميذًا … ») et il est
testé deux fois à d3 (02-Q5, 04-Q2) : règle sans exemple résolu. Dans le `::: methode`, remplacer les lignes 347–348
`حالتان حدّيّتان: 4/4 من 20 هي 20 كلّها. وبالعكس، إذا كان 1/5 من عدد يساوي 7، فالعدد خمسة أخماس:` /
`7 × 5 = 35. وإذا كان 3/4 من قسم 18 تلميذًا، فالربع 18 ÷ 3 = 6، والقسم كلّه 6 × 4 = 24 تلميذًا.` par la seule ligne
`حالة حدّيّة: 4/4 من 20 هي 20 كلّها. والعكس، من الجزء إلى الكلّ، في المثال الموالي.` ; puis insérer, entre la fin du
`::: methode` et le `::: verifie` (l. 352), une ligne vide puis :

```
::: exemple من الجزء إلى الكلّ

1. في قسم، 3/4 التلاميذ هم 18 تلميذًا — نعرف قيمة ثلاثة أرباع، ونبحث عن الأرباع الأربعة.
2. الربع الواحد: 18 ÷ 3 = 6 تلاميذ — لأنّ الأرباع الثلاثة أجزاء متساوية، فنقسم على البسط.
3. القسم كلّه أربعة أرباع: 6 × 4 = 24 تلميذًا — لأنّ الكلّ 4/4، فنضرب في المقام.
4. نتحقّق: 3/4 من 24 = (24 ÷ 4) × 3 = 18 ✓.

:::
```

Résumé, puce 7 : `وبالعكس، إذا كان 1/5 من عدد 7 فالعدد 35.` → `وبالعكس، إذا كان 3/4 القسم 18 تلميذًا فالربع 6 والقسم 24.`
(les questions 02-Q5 et 04-Q2 changent de nombres, M-6 et M-10).

**08 M-2 — quiz Q3 = exemple résolu du cours** (3/4 de 20 = 15, mêmes distracteurs 5 et 80). Prompt
`ما قيمةُ 3/4 من 28؟` ; **a `21`**, b `7` [fraction-d-un-nombre-etape-oubliee], c `24`, d `112`
[fraction-d-un-nombre-multipliee-au-lieu-de-divisee] ; explication `نقسم على المقام ثمّ نضرب في البسط: (28 ÷ 4) × 3 = 7 × 3 = 21. إذن 3/4 من 28 = 21.`

**08 M-3 — quiz Q6 = ancrage du cours** (9 L / 7 clients → 9/7) **et doublon de 02-boss Q10**. Prompt
`وزّع بائع عطور 5 لترات بالتساوي على 3 حرفاء. ما الكمية المضبوطة التي ينالها كلّ حريف؟` ; a `3/5 لتر`
[numerateur-denominateur-inverses], b `2 لتر`, c `1,6 لتر`, **d `5/3 لتر`** ; explication
`الخارج المضبوط لقسمة 5 على 3 هو الكسر 5/3: المقسوم 5 بسط والقاسم 3 مقام. القسمة لا تنتهي (1,666…)، فالكتابة 1,6 تقريبيّة وليست مضبوطة، والكسر 3/5 يقلب البسط والمقام.`

**08 M-4 — 02-boss Q10 (9 ÷ 7)**, même défaut. Prompt `أيّ كتابة تعطي الخارج المضبوط للقسمة التالية؟\n13 ÷ 6` ;
**a `13/6`**, b `6/13` [numerateur-denominateur-inverses], c `2,1`, d `2,17` ; explication
`القسمة 13 ÷ 6 لا تنتهي (2,1666…)، فالكتابتان العشريّتان 2,1 و2,17 تقريبيّتان. الخارج المضبوط هو الكسر 13/6: المقسوم بسط والقاسم مقام. الكسر 6/13 يقلبهما.`

**08 M-5 — 02-boss Q4 = piège du cours** (3/4 = 0,75 contre 0,34 / 0,43). Prompt `ما القيمةُ العشرية للكسر 3/5؟` ;
a `0,35` [ecriture-decimale-chiffres-recopies], b `1,6`, **c `0,6`**, d `0,53` [ecriture-decimale-chiffres-recopies] ;
explication `الكسرُ حاصلُ قسمة: 3/5 = 3 ÷ 5 = 0,6، والتحقّق 0,6 × 5 = 3. أمّا 0,35 و0,53 فتنقلان الرقمين حول الفاصلة دون قسمة.`

**08 M-6 — 02-boss Q5 = cas limite du cours** (1/5 → 7 → 35). Prompt `إذا كان 1/6 من عددٍ يساوي 9، فما هذا العدد؟` ;
a `3`, b `15`, **c `54`**, d `96` ; explication `العددُ يتكوّن من 6 أسداس؛ فإذا كان السُّدس (1/6) يساوي 9، فالعددُ = 9 × 6 = 54. تحقّق: 54 ÷ 6 = 9.`

**08 M-7 — 02-boss Q7 (reprise L18 ex. 8) = section 6 du cours mot pour mot** (100 élèves, 60 garçons → 40/60).
Le cours est bâti sur cette activité : la question devient une variante, retirer `"L18 ex. 8"` de
`02-boss.json › manuel.items` (reste `["L40 ex. 1"]`). Prompt `في مدرسة 80 تلميذًا، منهم 45 ولدًا. ما الكسر الممثّل لعدد البنات بالنسبة إلى عدد الأولاد؟` ;
a `35/80`, b `45/80`, c `45/35` [numerateur-denominateur-inverses], **d `35/45`** ; explication
`عدد البنات 80 − 45 = 35. نتحدّث عن البنات فالبسط 35، ونقارن بالأولاد فالمقام 45، أي 35/45. الكسر 35/80 يقارن بجميع التلاميذ، والكسر 45/35 هو الأولاد بالنسبة إلى البنات.`

**08 M-8 — 01-pratique Q9 (reprise L18 ex. 4) : les quatre lectures sont les exemples du cours** (9/5, 10/3, 30/6,
11/5). Variante, retirer `"L18 ex. 4"` (reste `["L18 ex. 7"]`) : gauche l1 `ثمانية أخماس`, l2 `خمسة أثمان`, l3 `عشرون تسعًا`,
l4 `اثنا عشر خمسًا` ; droite r1 `8/5`, r2 `5/8`, r3 `20/9`, r4 `12/5` (paires l1–r1 … l4–r4) ; explication
`البسط يُقرأ عددًا والمقام يُقرأ اسمَ جزء: ثمانية أخماس 8/5، وخمسة أثمان 5/8، وعشرون تسعًا 20/9، واثنا عشر خمسًا 12/5. الكتابتان الأوليان تتبادلان العددين: «أخماس» تجعل 5 مقامًا، و«أثمان» تجعل 8 مقامًا.`

**08 M-9 — 03-revision Q1 = piège du cours** (3/4 « أربعة أثلاث »). Prompt `كيف نقرأ الكسر 5/8؟` ; **a `خمسةُ أثمان`**,
b `خمسةُ أسداس`, c `ثلاثةُ أثمان`, d `ثمانيةُ أخماس` [numerateur-denominateur-inverses] ; explication
`البسطُ 5 يُقرأ عددًا، والمقامُ 8 يُقرأ اسمَ جزء (أثمان)، فيُقرأ الكسرُ «خمسةُ أثمان». أمّا «ثمانيةُ أخماس» فهي 8/5: تقلب البسط والمقام.`

**08 M-10 — 03-revision Q5 = exemple du cours** (3/4 sur la demi-droite en quarts). Prompt
`على نصف المستقيم المدرّج التالي قُسّمت كلّ وحدة إلى 5 أجزاء متساوية. ما العدد الكسريّ الذي تمثّله النقطة أ؟` +
la figure ci-dessous (graduations à 40/60/80/100 et 140/160/180/200, point à x = 80 = 3/5, vérifié) ; a `1/5`,
b `3/6`, **c `3/5`**, d `5/3` [numerateur-denominateur-inverses] ; explication
`المقام عدد الأجزاء المتساوية بين 0 و1، وهو 5 لا عدد التدريجات. النقطة أ بعد ثلاثة أجزاء من 0، فالبسط 3 والعدد 3/5. الكسر 5/3 يقلب البسط والمقام، و3/6 يعدّ التدريجات الستّ بدل الأجزاء.`

```
<svg viewBox="0 0 270 100"><path d="M20 60 H234" stroke="#0f172a" stroke-width="2" fill="none"/><path d="M228 54 L240 60 L228 66 Z" fill="#0f172a"/><path d="M20 51 V69" stroke="#0f172a" stroke-width="2"/><text x="20" y="90" font-size="15" font-weight="700" text-anchor="middle" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><path d="M40 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M60 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M80 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M100 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M120 51 V69" stroke="#0f172a" stroke-width="2"/><text x="120" y="90" font-size="15" font-weight="700" text-anchor="middle" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><path d="M140 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M160 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M180 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M200 54 V66" stroke="#0f172a" stroke-width="2"/><path d="M220 51 V69" stroke="#0f172a" stroke-width="2"/><text x="220" y="90" font-size="15" font-weight="700" text-anchor="middle" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text><circle cx="80" cy="60" r="5" fill="#0f6e56"/><text x="80" y="42" font-size="16" font-weight="700" text-anchor="middle" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">أ</text></svg>
```

**08 M-11 — 04-defi Q2 = cas limite du cours** (3/4 d'un groupe = 18 → 24). Prompt
`إذا كان 3/5 من صفٍّ يساوي 15 تلميذًا، فكم تلميذًا في الصفّ كلّه؟` ; a `9`, **b `25`**, c `75`, d `18` ; explication
`إذا كان 3/5 = 15 تلميذًا، فإنّ 1/5 = 15 ÷ 3 = 5، والصفُّ كلُّه (5/5) = 5 × 5 = 25 تلميذًا. تحقّق: 3/5 من 25 = (25 ÷ 5) × 3 = 15. العدد 9 هو 3/5 من 15، أي العمليّة في الاتّجاه الخطأ.`

**08 M-12 — 04-defi Q3 = cas limite du cours** (8/4 = 2). Options : a `5/10` [numerateur-denominateur-inverses],
b `2/2`, **c `10/5`**, d `2/5` ; explication `الكسرُ يساوي 2 إذا كان بسطُه ضِعفَ مقامه؛ 10/5 = 10 ÷ 5 = 2. أمّا 5/10 فيقلب البسط والمقام ويساوي نصفًا، و2/2 يساوي 1.`

**08 M-13 — 05-entrainement Q4 doublonne 03-revision Q3** (« 6/6 يساوي » / « 4/4 يساوي », mêmes options). Prompt
`الكسرُ 15/5 يساوي:` ; a `10`, b `1/3` [numerateur-denominateur-inverses], c `20`, **d `3`** ; explication
`الكسرُ حاصلُ قسمة: 15/5 = 15 ÷ 5 = 3، لأنّ 3 × 5 = 15. أمّا 1/3 فهو 5/15، أي الكسر مقلوبًا.`

**08 M-14 — 01-pratique Q5, étiquette fausse** : b `4` porte `numerateur-denominateur-inverses` ; prendre 1/4 de
12 en échangeant les termes donnerait 48 ou 12 × 4, pas 4 → **retirer l'étiquette**.

### Mineurs

- **m-1** 01-pratique Q6, explication : `(لأنّ a ÷ b = a/b)` — lettres latines côté élève, inutiles. →
  `(المقسوم بسط والقاسم مقام)`.
- **m-2** Instances du cours reprises dans des questions faciles (sans même distracteur) : quiz Q4 (7/7), Q5 (5/4),
  01-Q4 (2/3), 02-Q3 (8/5), 03-Q4 (1/2 = 0,5), 04-Q1 (7/4 = 1,75), 05-Q3 (1/4 = 0,25). Tolérable à d1–d2 ;
  variantes recommandées au prochain passage.
- **m-3** 04-defi Q7 (L18 ex. 9) : la propriété du cours affiche 600/300 (même activité) — la question demande
  600/1300, différente ✓ ; à garder.
- **m-4** Cours, `::: methode` de la section 7 : « حالتان حدّيّتان » annonce deux cas et en donne trois (corrigé par M-1).
- **m-5** Texte arabe à l'intérieur des SVG du cours (figures 1, 4 : « الوحدة مقسومةٌ… », « ثلاثةُ أرباع ») :
  `course-figures.md` veut la prose dans la légende. Systémique au lot (07, 09, 11) ; pas bloquant.
- **m-6** `1,2857…` dans le tableau rendu `…1,2857` en cellule arabe (points de suspension neutres poussés à gauche).
  Écrire `1,2857… (لا تنتهي)` — la cellule commence alors par un chiffre et `plaintext` la rend LTR.

---

## 09-fractions-equivalentes — 50 questions, 0 clé fausse, 14 majeurs, 7 mineurs

Cours : 7 sections au patron, tous les calculs justes (180/240 → 3/4 ; 72/56 = 9/7 ; 48/36 = 4/3, 48 = 18 × 2 + 12 ;
45/60 → 3/4 ; 400 L → 100 + 200 + 75 + 25 ; 13/7 = 65/35, 12/5 = 84/35 ; 27/21 → 18/14 ; 2/3 → 5 fractions).
Résumé 7 ↔ 7.

### Majeurs

**09 M-1 à M-3 — reprises dont le cours imprime la réponse** (corriger le **cours**) :

| question (reprise) | remplacement exact dans `cours.md` |
| --- | --- |
| 02-boss Q7 (L28 ex. 5, 72/56) | l. 154 `(72/56 = 9/7)` → `(63/49 = 9/7)` |
| 02-boss Q8 (L28 ex. 7, 55/… = 11/3) | l. 105 `أكمل: 5/6 = …/30، ثمّ 55/… = 11/3.` → `أكمل: 5/6 = …/30، ثمّ 36/… = 9/4.` ; l. 110 `في الثانية المعطى هو البسط: العامل 55 ÷ 11 = 5، فالمقام 3 × 5 = 15، و 55/15 = 11/3.` → `في الثانية المعطى هو البسط: العامل 36 ÷ 9 = 4، فالمقام 4 × 4 = 16، و 36/16 = 9/4.` |
| 04-defi Q8 (L28 ex. 13, 75 ل sur 400 ل = 3/16) | l. 267 `جنى فلّاح 400 L` → `جنى فلّاح 320 L` ; l. 283 `4. نتحقّق باللترات: 100 + 200 + 75 + 25 = 400 L ✓.` → `4. نتحقّق باللترات: 80 + 160 + 60 + 20 = 320 L ✓.` |

**09 M-4 — quiz Q4 = exemple résolu du cours** (2/3 = …/12 → 8) ; et b `4` (le facteur lui-même) porte à tort
`equivalence-facteur-errone`. Prompt `ما العددُ المفقود: 2/3 = …/15؟` ; a `6` [equivalence-facteur-errone],
b `5`, c `30` [equivalence-facteur-errone], **d `10`** ; explication `بما أنّ 3 × 5 = 15، نضرب البسطَ أيضًا في 5: 2 × 5 = 10، إذن 2/3 = 10/15.`

**09 M-5 — quiz Q6 : deux lectures possibles** — b `2/6 و 3/6` et c `3/6 و 2/6` sont **le même couple**
dans un autre ordre ; lu comme ensemble, b est juste aussi. Prompt `نكتب 1/2 و 1/3 بمقامٍ مشترك. أيّ كتابة صحيحة؟` ;
a `1/2 = 1/6 و 1/3 = 1/6` [equivalence-un-seul-terme-multiplie], b `1/2 = 2/6 و 1/3 = 3/6`, **c `1/2 = 3/6 و 1/3 = 2/6`**,
d `1/2 = 3/5 و 1/3 = 2/5` ; explication inchangée.

**09 M-6 — 03-revision Q4 doublonne quiz Q5 et le `verifie` du cours** (3/4 = 6/8). Prompt `ما البسطُ المفقود: 3/4 = …/28؟` ;
a `7`, b `28`, c `12` [equivalence-facteur-errone], **d `21`** ; explication `بما أنّ 4 × 7 = 28، نضرب البسطَ أيضًا في 7: 3 × 7 = 21، إذن 3/4 = 21/28.`

**09 M-7 — 03-revision Q6 = exemple résolu du cours** (18/24 → 3/4). Prompt `اختزل الكسر 18/30 إلى أبسط صورة.` ;
a `9/15` [reduction-incomplete], **b `3/5`**, c `6/10` [reduction-incomplete], d `2/5` ; explication
`القاسمُ المشترك الأكبر للعددين 18 و30 هو 6: 18/30 = (18÷6)/(30÷6) = 3/5. الكسران 9/15 و6/10 يتوقّفان قبل أبسط صورة.`

**09 M-8 — 03-revision Q7 = cas limite du cours** (2 et 3/5 → 10/5) et reprise non déclarée (L28 ex. 11ب).
Prompt `وحّد مقامي العددين 3 و 2/7.` ; a `3/7 و 2/7`, b `3/21 و 2/7`, **c `21/7 و 2/7`**, d `3/3 و 2/7`
[entier-converti-en-n-sur-n] ; explication `العدد الصحيح كسر مقامه 1، ونريد مقامه 7: العامل 7، فنضرب البسط أيضًا: 3 = (3 × 7)/(1 × 7) = 21/7. إذن الكسران 21/7 و2/7. كتابة 3/3 تساوي 1 لا 3، وكتابة 3/21 تساوي 1/7، وكتابة 3/7 تبقي المقام 7 دون ضرب البسط.`

**09 M-9 — 03-revision : reprises non déclarées** (Q8 = L28 ex. 11أ 14/11 & 2/3 ; Q9 = L28 ex. 8ب, vérifiés au PDF
ص 84 / fiche) et pas de champ `manuel`. Ajouter `"manuel": { "code": "102609", "pages": "80-84", "items": ["L28 ex. 8ب", "L28 ex. 11أ"] }`.

**09 M-10 — 04-defi Q7 = ancrage de la section 7 du cours** (3/50, 6/100, 9/150, 12/200) et reprise non déclarée
(L28 ex. 14). Prompt `أيّ كتابة من الكتابات التالية هي الدخيلة، أي التي لا تساوي 4/25؟` ; a `8/50`, b `12/75`,
c `16/100`, **d `12/100`** ; explication `الكسور المساوية لـ 4/25 تضرب حدّيها في العامل نفسه: 8/50 (العامل 2) و12/75 (العامل 3) و16/100 (العامل 4). أمّا 12/100 فمقامه 100 يحتاج العامل 4 والبسط 16، وقد جاء 12 فهو يساوي 3/25.`

**09 M-11 — 04-defi Q9 = les exemples du cours** (5/7, 8/9, 4/17). Options : **a `7/9`**, b `6/15`, **c `9/10`**,
d `18/24`, **e `5/12`** (clé a, c, e inchangée) ; explication `الكسر غير القابل للاختزال لا يشترك بسطه ومقامه في قاسم غير 1. 7/9 و9/10 و5/12 كذلك (9/10 رغم أنّ لكلّ من 9 و10 قواسم غير 1، لا قاسم مشترك لهما). أمّا 6/15 فيقسمهما 3، و18/24 يقسمهما 6.`

**09 M-12 — 04-defi Q2, explication qui n'enseigne pas** (d3 : « هو 12 » sans méthode). Explication
`قواسم 24 من الأكبر نزولًا: 24 لا يقسم 36، و12 يقسمه لأنّ 36 = 12 × 3. فالقاسم المشترك الأكبر 12، و24/36 = (24 ÷ 12)/(36 ÷ 12) = 2/3 دفعةً واحدة. الأعداد 6 و4 و2 قواسم مشتركة أيضًا لكنّها أصغر، فتُبقي اختزالًا لم ينتهِ.`

**09 M-13 — `؟` dans la formule : l'équation s'affiche retournée** (Chromium, `dir=rtl` : `55/؟ = 11/3` → `11/3 = ؟/55` ;
`2/3 = ؟/12` → `؟12/؟ = 2/3`). Remplacer `؟` par `…` **dans la formule** (le `؟` final de phrase reste) :
quiz Q4 (couvert par M-4), 01-Q4 `1/5 = …/10؟`, 02-Q4 `5/6 = …/24؟`, 02-Q8 `\n55/… = 11/3`, 03-Q4 (couvert par
M-6), 04-Q3 `7/8 = …/40؟`, 05-Q4 `1/2 = …/14؟`. Rendu de `…` vérifié dans le cours : juste.

**09 M-14 — 05-entrainement Q2, étiquette fausse** : c `3/15` (le facteur 3 pris pour le numérateur) porte
`equivalence-facteur-errone` → **retirer l'étiquette** (d `10/15` = × 5, ancien dénominateur, reste étiquetée ✓).

### Mineurs

- **m-1** Options « fraction recopiée telle quelle » étiquetées `reduction-incomplete` (réduction en zéro étape,
  option qui recopie l'énoncé) : 01-Q5 c `10/15`→`10/3`, 02-Q2 c `9/12`→`9/4`, 02-Q5 d `12/16`→`12/4`, 03-Q1 d
  `4/8`→`4/2`, 03-Q3 d `15/20`→`15/4`, 04-Q1 d `14/21`→`14/3`, 04-Q4 b `16/20`→`4/20`, 05-Q1 b `3/6`→`3/2`, 05-Q3 b
  `8/12`→`2/12`, 05-Q6 c `20/25`→`4/25`, toutes avec `reduction-un-seul-terme-divise` (un seul terme divisé —
  recalculé ; aucune ne vaut la clé). (05-Q7 d `12/16` reste : c'est la lecture brute de la figure.)
- **m-2** quiz Q1 (1/2 → /4, distracteur 1/4) = piège du cours ; quiz Q3 (6/8 → 3/4) = figure du cours ; quiz Q5
  (3/4 = 6/8) = `verifie`. Variantes : Q1 prompt `ما الكسرُ المساوي لـ 1/3 بمقامٍ يساوي 9؟` a `1/9`
  [equivalence-un-seul-terme-multiplie], b `9/3` [numerateur-denominateur-inverses], **c `3/9`**, d `2/9` ; Q3 prompt
  `اختزل الكسر 14/18.` **a `7/9`**, b `7/18` [reduction-un-seul-terme-divise], c `14/9` [reduction-un-seul-terme-divise],
  d `2/3`, explication `نقسم البسطَ والمقامَ على القاسم المشترك 2: 14/18 = (14÷2)/(18÷2) = 7/9.`
- **m-3** 02-Q5 (12/16) et 02-Q6 (1/2 ; 2/4 ; 3/6) reprennent un `verifie` et la définition du cours ; d2–d3, tolérable.
- **m-4** Point PGCD : bloc `::: definition` + glose « (plus grand commun diviseur) » → texte du § Point tranché.
- **m-5** Résumé, puce 5 : `أوّلِ قاسمٍ للعدد الأصغر يقسم الآخر` → `أوّلِ قاسمٍ للعدد الأصغر، من الأكبر نزولًا، يقسم الآخر` (sinon « le premier » est 1).
- **m-6** Lettres `a/b = (a × k)/(b × k)` (cours l. 46, 153, 335 ; résumé puce 7) : la fiche emploie la même notation
  et l'audit B1 l'a admise ; signalé seulement (« jamais de lettre côté élève », §3.2 calcul littéral, vise les inconnues).
- **m-7** Dans le cours, le « فلّاح » de la section 2 et celui de l'huile (M-3) ; rien à faire — noté pour cohérence.

---

## 10-comparaison-fractions — 48 questions, 0 clé fausse, 19 majeurs, 5 mineurs

Cours : 8 sections au patron, calculs justes (35/56 > 32/56 ; 21/28 > 20/28 ; 24/3 ; 20/5 ; 44/11 ; PPCM 168 ;
compléments 1/7, 1/4, 1/3, 1/8), sauf M-1. Résumé 8 ↔ 8.

### Majeurs

**10 M-1 — égalité trompeuse dans le cours** (l. 334) : « كتبناه كسرًا على **المقام المشترك**، فـ 1 = 24/24 و 4 = **24/6** » —
24/6 n'est pas sur le dénominateur commun 24. Remplacer `فـ 1 = 24/24 و 4 = 24/6؛` par `فـ 1 = 24/24 و 4 = 96/24؛`.

**10 M-2 à M-6 — quatrième option hors sujet** dans « أيُّ الكسرين أكبر: x أم y ? » (une fraction qui n'est aucun des
deux candidats, éliminée à vue) : quiz Q2 d `2/8`, 01-Q2 d `1/6`, 02-Q2 d `3/11`, 03-Q2 d `5/12`, 05-Q2 d `4/7` →
remplacer chacune par `لا يمكن المقارنة` [comparaison-jugee-impossible].

**10 M-7 — quiz Q1 = `verifie` du cours** (5/7 et 3/7). Prompt `قارن بين 5/12 و 7/12.` ; a `5/12 > 7/12`
[comparaison-a-meme-denominateur-inversee], **b `5/12 < 7/12`**, c `متساويان`, d `لا يمكن المقارنة`
[comparaison-jugee-impossible] ; explication `عند تساوي المقام، الأكبرُ بسطًا هو الأكبر؛ وبما أنّ 5 < 7 فإنّ 5/12 < 7/12.`

**10 M-8 — quiz Q4 = exemple résolu** (5/8 et 7/4 parmi les options). Options : a `5/9`
[comparaison-a-l-unite-inversee], **b `9/5`**, c `4/5` [comparaison-a-l-unite-inversee], d `2/7`
[comparaison-a-l-unite-inversee] ; explication `الكسرُ أكبرُ من 1 إذا كان بسطُه أكبرَ من مقامه؛ في 9/5 البسطُ 9 > المقام 5.`

**10 M-9 — quiz Q6 = `verifie` du cours** (45/11 et 4). Prompt `أيّ العددين أكبر: 3 أم 22/7؟` ; a `3`, **b `22/7`**,
c `متساويان`, d `لا يمكن المقارنة` [comparaison-jugee-impossible] ; explication
`نكتب 3 كسرًا مقامه 7: 3 = 21/7. المقامان متساويان فنقارن البسطين: 22 > 21، إذن 22/7 > 3. تحقّق: 22 ÷ 7 = 3,14… وهو أكبر من 3.`

**10 M-10 — quiz Q7 doublonne 02-boss Q5** (4/5 et 6/7 par le complément). Prompt
`ينقص الكسرَ 2/3 جزءٌ مقداره 1/3 حتّى يبلغ 1، وينقص الكسرَ 4/5 جزءٌ مقداره 1/5. أيّ الكسرين أكبر؟` ; a `2/3`,
b `متساويان`, **c `4/5`**, d `لا يمكن المقارنة` [comparaison-jugee-impossible] ; explication
`الجزءان الناقصان بسطاهما 1، والأكبر منهما صاحب المقام الأصغر: 1/3 > 1/5. الكسر الذي ينقصه جزء أكبر هو الأصغر، فـ 2/3 < 4/5، أي أنّ 4/5 هو الأكبر.`

**10 M-11 — 01-pratique Q7 = exemple et figure de la section 2** (5/6 vs 5/7). Prompt
`الشريطان متقايسان: لُوّنت في الأوّل 3 أجزاء من 4، وفي الثاني 3 أجزاء من 5. أيّ الكسرين أكبر؟` + figure ci-dessous
(4 × 60 et 5 × 48, 3 colorés chacun, vérifiée) ; a `متساويان`, b `3/5` [comparaison-par-denominateur], **c `3/4`**,
d `لا يمكن المقارنة` [comparaison-jugee-impossible] ; explication
`البسطان متساويان (3)، فالأكبر صاحب المقام الأصغر لأنّ أجزاءه أكبر: 4 < 5، إذن 3/4 > 3/5. في الشكل ثلاثة أرباع أطول من ثلاثة أخماس.`

```
<svg viewBox="0 0 260 88"><rect x="10" y="8" width="60" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="70" y="8" width="60" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="130" y="8" width="60" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="190" y="8" width="60" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><rect x="10" y="50" width="48" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="58" y="50" width="48" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="106" y="50" width="48" height="30" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="154" y="50" width="48" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><rect x="202" y="50" width="48" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/></svg>
```

**10 M-12 — 02-boss Q3 doublonne 04-defi Q9** (5/6 vs 7/8). Prompt `قارن بين 5/6 و 4/5 (وحّد على 30).` ; a `5/6 < 4/5`
[comparaison-a-meme-denominateur-inversee], b `متساويان`, c `لا يمكن المقارنة` [comparaison-jugee-impossible],
**d `5/6 > 4/5`** ; explication `نوحّد على 30: 5/6 = 25/30 و 4/5 = 24/30؛ وبما أنّ 25 > 24 فإنّ 5/6 > 4/5.`

**10 M-13 — 02-boss Q7 (L40 ex. 8ب) : les trois comparaisons sont l'exemple, le piège et le `verifie` du cours.**
Variante ; retirer `"L40 ex. 8ب"` (reste `["L40 ex. 9", "L40 ex. 10"]`). Options : a `29/7 < 4`, b `17/2 < 8`,
c `22/5 > 5`, **d `22/5 < 5`** ; explication `نكتب العدد الصحيح كسرًا بمقام الكسر: 5 = 25/5 و22 < 25، إذن 22/5 < 5 (22 ÷ 5 = 4,4). أمّا 29/7 > 4 لأنّ 4 = 28/7، و17/2 > 8 لأنّ 8 = 16/2، وكتابة 22/5 > 5 تقارن البسط 22 وحده بالعدد 5.`

**10 M-14 — 03-revision Q7 (L29 ex. 7) : le `verifie` du cours en est un sous-cas** (3/4 vs 6/7). Corriger le cours
l. 383 `قرأ ضياء 3/4 من قصّة، وقرأت أمل 6/7 من القصّة نفسها. من قرأ أكثر؟` → `قرأ ضياء 4/5 من قصّة، وقرأت أمل 7/8 من القصّة نفسها. من قرأ أكثر؟` ;
l. 387–388 → `ينقص 4/5 خُمسٌ واحد (1/5)، وينقص 7/8 ثُمنٌ واحد (1/8). البسطان 1، و 5 < 8، إذن 1/5 > 1/8: ما بقي لضياء`
/ `أكبر. إذن 7/8 > 4/5، وأمل قرأت أكثر.` (Résumé puce 8 inchangé : il cite l'exemple 6/7 > 3/4.)

**10 M-15 — 03-revision Q8 : énoncé confus** (« ملأ تاجر قارورة » puis « الثانية », « الثالثة » ; le manuel dit trois
flacons, le premier plein — ص 88). Prompt `ملأ تاجر ثلاث قوارير بماء الزهر: ملأ الأولى كلّها، ووضع في الثانية 3/5 من سعة الأولى، وفي الثالثة 5/7 من سعة الأولى. أيّ جملة صحيحة؟` (options, clé, explication inchangées).

**10 M-16 — 04-defi Q5 (L29 ex. 2) = exemple résolu de la section 8** (6/7, 3/4, 2/3, 7/8). Variante ; retirer
`"L29 ex. 2"` (reste `["L40 ex. 13", "L29 ex. 9"]`). Prompt `صرفت أسرة في آخر أربعة أشهر 9/10 ثمّ 4/5 ثمّ 5/6 ثمّ 7/8 من دخلها. ما أصغر كسر بينها؟` ;
a `9/10` [comparaison-par-denominateur], b `5/6`, **c `4/5`**, d `7/8` ; explication
`نكتب ما ينقص كلّ كسر حتّى 1: 1/10 و1/5 و1/6 و1/8. بسوطها كلّها 1، فالأكبر منها صاحب المقام الأصغر: 1/5. الكسر الذي ينقصه أكبر جزء هو الأصغر، فأصغر الكسور 4/5.`

**10 M-17 — 04-defi Q6 = exemple résolu de la section 6** (6/8 et 9/12). Prompt `قارن بين 10/15 و 14/21 بعد اختزالهما.` ;
a `10/15 > 14/21`, **b `متساويان`**, c `10/15 < 14/21`, d `لا يمكن المقارنة` [comparaison-jugee-impossible] (a et c
sans étiquette : ni l'une ni l'autre n'inverse un ordre à même dénominateur) ; explication
`نختزل: 10/15 = 2/3 (÷ 5) و14/21 = 2/3 (÷ 7)؛ فالكسران متساويان، ولا نقارن البسطين 10 و14 قبل أن يتوحّد المقام.`

**10 M-18 — 05-entrainement Q4 = cas limite du cours** (3/4 et 5/8). Prompt `قارن بين 2/3 و 7/12 (وحّد على 12).` ;
a `2/3 < 7/12` [comparaison-a-meme-denominateur-inversee], b `متساويان`, c `لا يمكن المقارنة`
[comparaison-jugee-impossible], **d `2/3 > 7/12`** ; explication `نوحّد على 12: 2/3 = 8/12؛ وبما أنّ 8 > 7 فإنّ 2/3 > 7/12.`

**10 M-19 — 05-entrainement Q7, explication fausse** : « الثلاثة الأخرى أكبر من 4 » (4 en fait partie). Remplacer
`نلاحظ أنّ 3/4 أصغر من 1 وأنّ الثلاثة الأخرى أكبر من 4.` par `نلاحظ أنّ 3/4 أصغر من 1، وأنّ 25/6 و9/2 أكبر من 4.`

### Mineurs

- **m-1** 04-defi Q7 : `رولو قماش` (emprunt dialectal) → `لفيفة قماش` (mot du manuel, ص 88).
- **m-2** 05-entrainement : `L40 ex. 8د` déclaré pour Q8, variante (ajoute 1/2, se résout en unifiant) → retirer l'item.
- **m-3** quiz Q2 (2/3 vs 2/5) = formule de la propriété du cours ; d1 — variante recommandée (`2/5` ou `2/9`).
- **m-4** quiz Q3 / 04-Q2 / 04-Q4 gardent l'indice « (وحّد على N) » jusqu'à d3 — admis par l'auteur, à retirer au d4 seulement (04-Q2, 04-Q4).
- **m-5** Étiquettes proposées par l'auteur (`complement-lu-a-l-envers`, `numerateur-compare-a-l-entier`) : seuil
  atteint pour la première (3 questions) ; décision du pilote (registre).

---

## 11-addition-soustraction-fractions — 52 questions, 0 clé fausse, 20 majeurs, 6 mineurs

Cours : 8 sections au patron, tout recalculé juste (3/20 + 1/4 = 2/5 ; 13/24 ; 19/12 ; 7/4 ; 13/6 ; 160 ha →
40/60/60 ; 31/30 ; 1/18 ; 675 ; 17 280 L ; 840 m²). Aucune ÷ par une fraction (retour à la part unité ✓).
Reprises RTL relues au PDF ص 127 (ex. 3–6) : toutes écrites LTR avec un résultat positif ✓. Résumé 8 ↔ 8.

### Majeurs — questions de l'auteur qui recopient le cours (20)

| question | dans le cours | remplacement exact (prompt ; options a–d, clé **en gras** ; explication) |
| --- | --- | --- |
| quiz Q1 | exemple résolu + piège (5/14, 5/49) | `ما ناتج 3/11 + 5/11؟` ; **a `8/11`**, b `8/22` [add-denominators], c `2/11` [operation-inverse-appliquee], d `8/121` [denominateurs-multiplies] ; `عند تساوي المقام نجمع البُسُط ونُبقي المقام: 3/11 + 5/11 = (3+5)/11 = 8/11.` |
| quiz Q3 = 05-Q3 (doublon mot pour mot) | — | 05-Q3 : `ما ناتج 1/3 + 1/4 (وحّد على 12)؟` ; a `2/7` [add-numerators-and-denominators], b `2/12`, **c `7/12`**, d `1/12` ; `نوحّد على 12: 1/3 = 4/12 و 1/4 = 3/12؛ ثمّ 4/12 + 3/12 = 7/12.` |
| quiz Q4 | méthode (3/4 − 1/2) | `ما ناتج 5/6 − 2/3 (وحّد على 6)؟` ; a `3/3` [soustraction-denominateurs], b `3/6`, c `9/6` [operation-inverse-appliquee], **d `1/6`** ; `نوحّد على 6: 2/3 = 4/6؛ ثمّ 5/6 − 4/6 = 1/6.` |
| quiz Q5 | propriété (1 + 1/4) | `ما ناتج 1 + 2/7؟` ; **a `9/7`**, b `3/7`, c `3/8` [add-numerators-and-denominators], d `7/7` [entier-converti-mais-operation-oubliee] ; `نكتب العددَ الصحيح 1 = 7/7؛ ثمّ 7/7 + 2/7 = 9/7.` |
| 01-Q2 | `verifie` (4/9 − 1/9) | `ما ناتج 8/9 − 3/9؟` ; a `11/9` [operation-inverse-appliquee], **b `5/9`**, c `5/18` [add-denominators], d `3/9` ; `عند تساوي المقام نطرح البُسُط ونُبقي المقام: 8/9 − 3/9 = (8−3)/9 = 5/9.` |
| 01-Q3 | `verifie` (3/8 + 4/8) | `ما ناتج 4/11 + 5/11؟` ; a `9/22` [add-denominators], b `1/11`, **c `9/11`**, d `20/11` ; `عند تساوي المقام نجمع البُسُط: 4/11 + 5/11 = (4+5)/11 = 9/11.` |
| 01-Q5 | exemple résolu (1/6 + 2/6 → 1/2) | `ما ناتج 1/8 + 5/8 (مع الاختزال)؟` ; **a `3/4`**, b `6/16` [add-denominators], c `1/2`, d `3/8` ; `1/8 + 5/8 = 6/8، وبالاختزال على 2: 6/8 = 3/4.` |
| 01-Q6 | piège (1/2 + 1/4, 2/6) | `ما ناتج 1/2 + 3/8 (وحّد على 8)؟` ; a `4/10` [add-numerators-and-denominators], **b `7/8`**, c `4/8`, d `3/8` ; `نوحّد على 8: 1/2 = 4/8؛ ثمّ 4/8 + 3/8 = 7/8.` |
| 02-Q2 | méthode (1/3 + 1/6) | `ما ناتج 1/4 + 1/12 (وحّد على 12)؟` ; a `2/16` [add-numerators-and-denominators], **b `1/3`**, c `2/12`, d `1/12` ; `نوحّد على 12: 1/4 = 3/12؛ ثمّ 3/12 + 1/12 = 4/12 = 1/3 (بعد الاختزال على 4).` |
| 02-Q4 | exemple résolu (2 − 1/4) | `ما ناتج 4 − 3/4؟` ; a `1/4`, b `16/4` [entier-converti-mais-operation-oubliee], c `19/4` [operation-inverse-appliquee], **d `13/4`** ; `نكتب العددَ الصحيح 4 = 16/4؛ ثمّ 16/4 − 3/4 = 13/4.` |
| 02-Q5 | piège (2/3 + 3/4, 17/24) | `ما ناتج 3/4 + 1/6 (وحّد على 12)؟` ; **a `11/12`**, b `4/10` [add-numerators-and-denominators], c `4/12`, d `11/24` [add-denominators] ; `نوحّد على 12: 3/4 = 9/12 و 1/6 = 2/12؛ ثمّ 9/12 + 2/12 = 11/12.` |
| 02-Q6 | `verifie` (7/8 − 1/2) | `ما ناتج 11/12 − 1/3 (وحّد على 12)؟` ; a `10/9` [soustraction-denominateurs], **b `7/12`**, c `10/12`, d `15/12` [operation-inverse-appliquee] ; `نوحّد على 12: 1/3 = 4/12؛ ثمّ 11/12 − 4/12 = 7/12.` |
| 03-Q3 | piège + doublon de 01-Q6 | `ما ناتج 1/3 + 5/9 (وحّد على 9)؟` ; a `6/12` [add-numerators-and-denominators], b `6/9`, **c `8/9`**, d `8/18` [add-denominators] ; `نوحّد على 9: 1/3 = 3/9؛ ثمّ 3/9 + 5/9 = 8/9.` |
| 03-Q4 | propriété (1 − 1/3) | `ما ناتج 1 − 3/8؟` ; a `3/8`, b `8/8` [entier-converti-mais-operation-oubliee], c `1/8`, **d `5/8`** ; `نكتب العددَ الصحيح 1 = 8/8؛ ثمّ 8/8 − 3/8 = 5/8.` |
| 03-Q5 | propriété (5/12 + 1/12) | `ما ناتج 7/15 + 2/15 (مع الاختزال)؟` ; **a `3/5`**, b `9/30` [add-denominators], c `1/3`, d `5/15` [operation-inverse-appliquee] ; `7/15 + 2/15 = 9/15، وبالاختزال على 3: 9/15 = 3/5.` |
| 04-Q2 | propriété (3/4 + 5/6 = 19/12) | `ما ناتج 5/6 + 3/8؟` ; a `8/14` [add-numerators-and-denominators], **b `29/24`**, c `29/48` [add-denominators], d `8/24` ; `نوحّد على 24: 5/6 = 20/24 و 3/8 = 9/24؛ ثمّ 20/24 + 9/24 = 29/24.` |
| 04-Q3 | `verifie` (2 − 3/5) | `ما ناتج 3 − 4/7؟` ; a `25/7` [operation-inverse-appliquee], b `21/7` [entier-converti-mais-operation-oubliee], **c `17/7`**, d `17/14` [add-denominators] ; `نكتب العددَ الصحيح 3 = 21/7؛ ثمّ 21/7 − 4/7 = 17/7.` |
| 04-Q4 | propriété (1/3 + 2/5 = 11/15) | `شربَ خالدٌ 1/4 من قارورة ماءٍ صباحًا و 2/5 منها ظهرًا. كم شرب إجمالًا؟` ; a `3/9` [add-numerators-and-denominators], b `3/20`, c `13/40` [add-denominators], **d `13/20`** ; `نوحّد على 20: 1/4 = 5/20 و 2/5 = 8/20؛ ثمّ 5/20 + 8/20 = 13/20.` |
| 04-Q6 | piège (jardin 2/5 + 1/4 → 7/20) | `في بستان، 1/3 منه ورودٌ و 2/5 منه أشجار. ما الكسرُ المتبقّي للعشب؟` ; a `11/15` [reponse-a-l-autre-inconnue], **b `4/15`**, c `3/8` [add-numerators-and-denominators], d `5/8` ; `نوحّد على 15: 1/3 = 5/15 و 2/5 = 6/15؛ المستعمل = 11/15؛ والباقي = 15/15 − 11/15 = 4/15. الكسر 11/15 هو المستعمل لا الباقي.` |
| 05-Q2 | piège (8/9 − 2/9, 6/18) | `ما ناتج 11/12 − 5/12 (مع الاختزال)؟` ; a `6/24` [add-denominators], **b `1/2`**, c `16/12` [operation-inverse-appliquee], d `5/12` ; `11/12 − 5/12 = 6/12، وبالاختزال على 6: 6/12 = 1/2.` |

(L'étiquette `soustraction-denominateurs` sur `3/3` = (5−2)/(6−3) et `10/9` = (11−1)/(12−3) exécute exactement « طرح
المقامين ».)

### Mineurs

- **m-1** quiz Q2 (5/8 − 2/8) et 04-Q1 (5/6 + 1/6) = exemples de propriétés du cours ; variante pour quiz Q2 :
  `ما ناتج 9/10 − 2/10؟` ; a `11/10` [operation-inverse-appliquee], **b `7/10`**, c `7/20` [add-denominators], d `6/10`.
- **m-2** 03-Q7 (L42 ex. 2) : ses deux premiers termes (3/20 + 1/4) sont l'exemple de la section 2 ; la reprise
  ajoute 2/5 et demande la forme réduite — tolérable.
- **m-3** 02-Q9 b : `ويكتمل التغطية` → `وتكتمل التغطية`.
- **m-4** 04-Q9 : `كم متّرًا مربّعًا` → `كم مترًا مربّعًا`.
- **m-5** Contextes adultes (salaire, loyer, « موظّف », « عامل … كراء المسكن ») : ceux du manuel (L42 ex. 10,
  L57 ex. 5, L48 pb 2) — conformes à la source ; la règle d'âge de `prof-math-6eme` est en tension avec le manuel.
- **m-6** Figure 1 du cours : étiquette `2 أسباع` → `سُبعان` (duel).

---

## 12-fractions-decimales — 52 questions, 0 clé fausse, 22 majeurs, 6 mineurs

Cours : 7 sections, tout juste (815/100 = 8,15 ; 4500/1000 = 4,5 ; 92/100 = 23/25 ; 7/8 = 875/1000 ; 2/15 non
convertible, argument par le critère de 3 sans facteurs premiers ✓ ; rangement 1,5 > … > 0,06). Résumé 7 ↔ 7.

### Majeurs

**12 M-1 à M-6 — reprises (L31) dont le cours a pris les données comme exemples** → corriger le **cours** :

| reprise | remplacement exact |
| --- | --- |
| 01-Q8 (ex. 7, 3,5 m) et 05-Q10 (ex. 7, 209 L) | cours l. 104 `طول حبل 3 أمتار ونصف، أي 3,5 m.` → `طول حبل 4 أمتار ونصف، أي 4,5 m.` ; l. 109 `1. للعدد 3,5 رقم` → `1. للعدد 4,5 رقم` ; l. 110 `3 أمتار = 30 عُشرًا، مع 5 أعشار تصبح 35 عُشرًا` → `4 أمتار = 40 عُشرًا، مع 5 أعشار تصبح 45 عُشرًا` ; l. 111 `3. إذن 3,5 m = 35/10 m. نتحقّق: 35/10 فيه صفر واحد، فرقم واحد بعد الفاصلة: 3,5 ✓.` → `3. إذن 4,5 m = 45/10 m. نتحقّق: 45/10 فيه صفر واحد، فرقم واحد بعد الفاصلة: 4,5 ✓.` ; l. 112 `مع 2,09 hl: … و 2,09 hl = 209/100 hl.` → `مع 1,07 hl: رقمان بعد الفاصلة، فالمقام 100، و 1,07 hl = 107/100 hl.` ; résumé puce 3 `3,5 = 35/10` → `4,5 = 45/10` |
| 02-Q8 (ex. 8, 3,5/10) | l. 39–40 `3,5/10 ليس كسرًا عشريًّا، ونكتبه` / `35/100 لأنّ 3,5/10 = 0,35.` → `6,5/10 ليس كسرًا عشريًّا، ونكتبه` / `65/100 لأنّ 6,5/10 = 0,65.` |
| 05-Q7 (ex. 6أ, 3/10 000) | l. 85 `حالة حدّيّة: 3/10000 = 0,0003، أربعة` → `حالة حدّيّة: 9/10000 = 0,0009، أربعة` |
| 03-Q7 (ex. 3, 7/8) | l. 205 `ففي 7/8 نحتاج إلى 1000: 8 × 125 = 1000، و 7/8 = 875/1000 = 0,875.` → `ففي 9/40 نحتاج إلى 1000: 40 × 25 = 1000، و 9/40 = 225/1000 = 0,225.` |
| 03-Q8 (ex. 4 : 3/12, 4/30…) | l. 224 `في قائمة من الكسور: 3/12 و 4/30 و 5/8. لا يقسم 12 ولا 30` → `في قائمة من الكسور: 9/36 و 6/45 و 7/40. لا يقسم 36 ولا 45` ; l. 229 `1. 3/12: نختزل أوّلًا على 3 فنجد 1/4` → `1. 9/36: نختزل أوّلًا على 9 فنجد 1/4` ; l. 230 `2. 4/30: نختزل على 2 فنجد 2/15` → `2. 6/45: نختزل على 3 فنجد 2/15` ; l. 231 → `3. 7/40 غير قابل للاختزال، و 40 يقسم 1000 (1000 = 40 × 25) — إذن 7/40 = 175/1000: التحويل ممكن.` ; résumé puce 6 `3/12 = 1/4، … أمّا 4/30 = 2/15` → `9/36 = 1/4، … أمّا 6/45 = 2/15` |

**12 M-7 à M-22 — questions de l'auteur qui recopient le cours** :

| question | dans le cours | remplacement exact |
| --- | --- | --- |
| quiz Q3 | exemple résolu 25/100 | `ما القيمةُ العشرية للكسر 64/100؟` ; a `6,4` [puissance-de-dix-rangs-mal-comptes], **b `0,64`**, c `0,064` [puissance-de-dix-rangs-mal-comptes], d `64` [virgule-ignoree-nombre-lu-entier] ; `مقامُ الكسر 100، فله رقمان بعد الفاصلة: 64/100 = 0,64.` |
| quiz Q4 | piège 0,09 | `اكتب العددَ 0,03 على شكل كسرٍ عشريّ.` ; a `3/10`, b `3/1000`, c `30/100` (les trois [decimale-rang-du-denominateur-errone]), **d `3/100`** ; `للعدد 0,03 رقمان بعد الفاصلة، فهو 3 أجزاء من المئة: 0,03 = 3/100.` |
| quiz Q5 | piège 1,5 = 1/5 | `ما الكسرُ العشريّ المساوي للعدد 2,7؟` ; **a `27/10`**, b `27/100` [decimale-rang-du-denominateur-errone], c `2/7` [ecriture-decimale-chiffres-recopies], d `270` ; `للعدد 2,7 رقمٌ واحدٌ بعد الفاصلة: 2,7 = 27/10.` |
| quiz Q7 | exemple section 6 (5/8, 4/30) | options a `13/7`, b `5/12`, **c `9/20`**, d `2/9` ; `9/20 غير قابل للاختزال، و20 يقسم 100 (20 × 5 = 100)، فـ 9/20 = 45/100 = 0,45. أمّا 13/7 و2/9 فمقاماهما 7 و9 لا يقسمان 10 ولا 100 ولا 1000، و5/12 غير قابل للاختزال ومقامه 12 يقبل القسمة على 3 فلا يقسم أيًّا منها.` |
| 01-Q2 | piège 0,3 = 1/3 | `اكتب العددَ 0,2 على شكل كسرٍ عشريّ.` ; a `2/100` [decimale-rang-du-denominateur-errone], **b `2/10`**, c `20`, d `1/2` [ecriture-decimale-chiffres-recopies] ; `للعدد 0,2 رقمٌ واحدٌ بعد الفاصلة، فهو عُشران: 0,2 = 2/10.` |
| 01-Q3 | piège 7/100 = 0,7 | `ما القيمةُ العشرية للكسر 9/100؟` ; a `0,9` [puissance-de-dix-rangs-mal-comptes], b `9` [virgule-ignoree-nombre-lu-entier], **c `0,09`**, d `0,009` [puissance-de-dix-rangs-mal-comptes] ; `مقامُ الكسر 100، فله رقمان بعد الفاصلة: 9/100 = 0,09.` |
| 02-Q2 | `verifie` 0,45 | `اكتب العددَ 0,58 على شكل كسرٍ عشريّ.` ; a `58/10` [decimale-rang-du-denominateur-errone], **b `58/100`**, c `58/1000` [decimale-rang-du-denominateur-errone], d `5,8` ; `للعدد 0,58 رقمان بعد الفاصلة، فهو 58 جزءًا من المئة: 0,58 = 58/100.` |
| 02-Q3 | `verifie` 8/1000 | `ما القيمةُ العشرية للكسر 6/1000؟` ; a `0,6`, b `0,06`, **c `0,006`**, d `0,0006` (a, b, d [puissance-de-dix-rangs-mal-comptes]) ; `مقامُ الكسر 1000، فله ثلاثةُ أرقامٍ بعد الفاصلة: 6/1000 = 0,006.` |
| 02-Q4 | propriété 25/100 = 1/4 | `اختزل الكسرَ العشريّ 75/100.` ; a `75/10`, b `4/3` [numerateur-denominateur-inverses], c `7,5`, **d `3/4`** ; `75/100 = 0,75؛ وبالاختزال على 25: 75/100 = 3/4.` |
| 02-Q5 | exemple résolu 3/4 → 75/100 (+ ses deux pièges) | `اكتب الكسر 2/5 على شكل كسرٍ عشريّ بمقامٍ 100.` ; **a `40/100`**, b `25/100` [ecriture-decimale-chiffres-recopies], c `7/100`, d `2/100` [equivalence-un-seul-terme-multiplie] ; `5 × 20 = 100، فنضرب البسطَ والمقامَ في 20: 2/5 = 40/100 (وهو 0,4).` |
| 02-Q6 | `verifie` 250/100 | `ما القيمةُ العشرية للكسر 370/100؟` ; a `37` [puissance-de-dix-rangs-mal-comptes], **b `3,7`**, c `0,37` [puissance-de-dix-rangs-mal-comptes], d `370` [virgule-ignoree-nombre-lu-entier] ; `مقامُ الكسر 100، فله رقمان بعد الفاصلة: 370/100 = 3,70 = 3,7.` |
| 04-Q2 | `verifie` 1/4 → 0,25 | `اكتب الكسر 3/20 بمقامٍ 100، ما قيمتُه العشرية؟` ; a `0,32` [ecriture-decimale-chiffres-recopies], **b `0,15`**, c `0,03` [equivalence-un-seul-terme-multiplie], d `0,015` ; `20 × 5 = 100، فنضرب البسطَ والمقامَ في 5: 3/20 = 15/100 = 0,15.` |
| 04-Q3 | `verifie` 0,125 → 1/8 | `اكتب العددَ 0,625 على شكل كسرٍ عشريّ ثمّ اختزله.` ; a `625/100` [decimale-rang-du-denominateur-errone], b `1/625` [ecriture-decimale-chiffres-recopies], **c `5/8`**, d `625/10` [decimale-rang-du-denominateur-errone] ; `0,625 = 625/1000، وبالاختزال على 125: 625/1000 = 5/8 (625 = 125 × 5 و1000 = 125 × 8).` |
| 04-Q5 | méthode 0,4 = 40/100 | `كم جزءًا من المئة في العدد 0,7؟` ; **a `70`**, b `7`, c `700`, d `0,07` ; `0,7 = 0,70 = 70/100، أي 70 جزءًا من المئة.` |
| 04-Q6 | méthode 7/20 = 35/100 | `ما الكسرُ العشريّ بمقامٍ 100 المساوي للكسر 9/25؟` ; a `9/100` [equivalence-un-seul-terme-multiplie], **b `36/100`**, c `34/100`, d `925` ; `نضرب البسطَ والمقامَ في 4: 9/25 = 36/100 (وهو 0,36).` |
| 05-Q5 | méthode 3/5 = 6/10 | `اكتب الكسر 1/5 بمقامٍ 10، ما قيمتُه العشرية؟` ; **a `0,2`**, b `0,15` [ecriture-decimale-chiffres-recopies], c `0,5`, d `0,02` [puissance-de-dix-rangs-mal-comptes] ; `نضرب البسطَ والمقامَ في 2: 1/5 = 2/10 = 0,2.` |

### Mineurs

- **m-1** 05-Q9 : `25/500 يساوي ؟/100.` → `25/500 = …/100. ما العدد الناقص؟` (le `؟` dans la formule se retourne, cf. 09 M-13).
- **m-2** 04-defi Q8 = L31 ex. 12 **avec** l'erratum p.201 (2/5) et la lecture 3/10 : c'est une reprise, pas une
  variante → ajouter `"L31 ex. 12"` à `04-defi.json › manuel.items`.
- **m-3** Gabarit d1 « القيمة العشرية للكسر n/10 » répété en ouverture des cinq fichiers (quiz Q1, 01-Q1, 02-Q1,
  03-Q1, 05-Q1, mêmes types de distracteurs) : échauffements parallèles de missions distinctes — justifié.
- **m-4** 01-Q5 (5/10 = 1/2), 03-Q6 (1/2 = 5/10) : exemples de la propriété / méthode ; d2–d3, tolérable.
- **m-5** Section 7 : la figure (T3) vient **après** l'exemple résolu (T4) ; la déplacer avant `::: exemple ترتيب الأعداد الستّة`.
- **m-6** 02-Q7 (21/300) : le cas est cité dans la propriété de la section 1 (« 21/300 ليست عشريّة كما هي مكتوبة »),
  sans la conversion — tolérable.

---

## Pour le pilote

- **Engine** : piège `> ⚠️` multi-lignes rendu coupé en paragraphes (voir § Rendu) — à ouvrir côté moteur.
- **Registre** : l'étiquette proposée par l'auteur `math.frac.complement-lu-a-l-envers` atteint le seuil au ch. 10
  (quiz Q7 option a après correction, 02-Q5 options a et c, 04-Q9 option b) ; les trois autres restent sous le seuil.
- **Méthode** : le défaut dominant (B1 comme B2) vient de ce que le cours puise ses exemples dans les **exercices**
  du manuel que les fichiers reprennent ensuite. Consigne suggérée pour les lots suivants : ancrer le cours sur
  l'activité أستكشف, et réserver les exercices أتدرّب/أوظّف/أقيّم aux questions.

---

## Re-vérification (2026-10-20, commit `71bdf13c`)

> Périmètre : ch. 07–12, quiz + exercices `01`–`05`, cours, résumés (les missions `06-…` du ch. 07 sont hors
> périmètre). Comparaison question par question `a0e47daa` → `71bdf13c` ; chaque question remplacée re-résolue
> à l'aveugle ; paires proches recalculées avec l'algorithme exact de `tranche-checks.ts` (jetons de surface,
> seuil court 0,8 sous 10 jetons, figures différentes exclues — 41 paires ≥ 0,6 reproduites à l'identique avant
> correction), sans `--fresh`.

### Verdict : **prêt après 23 remplacements de questions et 1 retouche de cours, ci-dessous** (0 critique, 0 majeur restant de l'audit ; 3 mineurs r-1 à r-3 ; 20 réécritures pour les paires proches)

**(1) Défauts de l'audit : 137/137 corrigés.** Les 100 majeurs et 37 mineurs sont appliqués tels que proposés
(textes, options, étiquettes, clés, explications, `manuel.items`, cours, résumés, deux SVG). Contrôles :
- cours 07 (3508, 998, 72▢0, 5034, ▢51), 08 (exemple « من الجزء إلى الكلّ » inséré entre `methode` et `verifie`, tableau
  `1,2857… (لا تنتهي)`), 09 (63/49, 36/16 = 9/4, 320 L, bloc PGCD descriptif sans glose), 10 (96/24, `verifie`
  4/5–7/8), 11 (`سُبعان`), 12 (4,5 m, 1,07 hl, 6,5/10, 9/10000, 9/40, 9/36–6/45–7/40, figure avant l'exemple) :
  recalculés, justes ;
- aucun `؟` dans une formule ; aucun nouveau nombre du cours ne revient dans une question (recherche des 23
  nombres modifiés dans les 30 fichiers) ;
- l'écart de l'auteur (résumé 10 aligné sur le `verifie` corrigé) est cohérent.

**(2) Remplacements re-résolus : 154/154 justes**, une seule réponse partout, aucune option désignée par sa place,
aucun exemple du cours redonné.

**(3) Régressions : aucune bloquante.** Gates : `content:check` ✓ ; `content:qa` 0 erreur (5 avertissements,
tous en 14 et 16, hors lot) ; `content:figures:check` ✓ ; `content:tranche --fresh --strict-longest --strict-lessons` :
0/156, patron 0 en recul. Trois défauts nouveaux ou résiduels :

- **r-1 (mineur, régression de l'application)** `10/04-defi` Q7 : `لفيفة` est féminin. Prompt →
  `لفيفة قماش طولها 45 m. باع التاجر منها لحريف أوّل 2/5 ولحريف ثانٍ 4/9. كم مترًا يزيد ما اشتراه الثاني على ما اشتراه الأوّل؟`
- **r-2 (mineur, mesuré sans `--fresh`, préexistant)** clé strictement la plus longue :
  - `07/05-entrainement` Q6 : d `على 9 فقط` → `على 9 نعم وعلى 3 لا` (sans étiquette : deux erreurs). Longueurs 19/11/18/19.
  - `09/04-defi` Q2 : d `2` → `24` ; explication → `قواسم 24 من الأكبر نزولًا: 24 لا يقسم 36، و12 يقسمه لأنّ 36 = 12 × 3. فالقاسم المشترك الأكبر 12، و24/36 = (24 ÷ 12)/(36 ÷ 12) = 2/3 دفعةً واحدة. العددان 6 و4 قاسمان مشتركان أيضًا لكنّهما أصغر، فيُبقيان اختزالًا لم ينتهِ؛ أمّا 24 فلا يقسم 36.`
- **r-3 (mineur)** le `verifie` corrigé du cours 10 (4/5 contre 7/8) recoupe `04-defi` Q5 (9/10, 4/5, 5/6, 7/8 → 4/5).
  Cours l. 383 → `قرأ ضياء 8/9 من قصّة، وقرأت أمل 10/11 من القصّة نفسها. من قرأ أكثر؟` ; l. 387–388 →
  `ينقص 8/9 تُسعٌ واحد (1/9)، وينقص 10/11 جزءٌ واحد من 11 (1/11). البسطان 1، و 9 < 11، إذن 1/9 > 1/11: ما بقي لضياء`
  / `أكبر. إذن 10/11 > 8/9، وأمل قرأت أكثر.` ; résumé puce 8 → retour à l'exemple résolu de la section, qui reste
  dans le cours : `… الكسر الذي ينقصه أصغر جزء هو الأكبر: 6/7 ينقصه 1/7 و 3/4 ينقصه 1/4، إذن 6/7 > 3/4.`

**(4) Paires proches : 41 paires ≥ 0,6 → 0** avec les 20 réécritures ci-dessous (+ les 3 de r-1/r-2) (mesure sur le corpus entier de
`math-6eme` après remplacement). Il reste 24 paires dans [0,45 ; 0,6[ : savoir-faire parallèles à données
différentes dans des missions distinctes, justifiées. Trois de mes propres jeux de remplacement étaient en cause
(09 quiz Q1 ↔ 02-Q1, 11 02-Q2 ↔ 05-Q3, 07 quiz Q3 ↔ 01-Q6). Le reste vient du gabarit du ch. 10 (« قارن بين x و y »,
« أيُّ الكسرين أكبر » répétés dans les cinq fichiers avec les mêmes options « متساويان / لا يمكن المقارنة »).
Le remède : contextualiser une question sur deux et varier le format (signe à placer, rangement, petite situation).
Même rang, même difficulté, même id de clé (**en gras**). Clé jamais strictement la plus longue (mesuré). Étiquettes
telles qu'indiquées, les autres options sans étiquette.

| question | prompt | options a–d | explication |
| --- | --- | --- | --- |
| 07/01-pratique Q3 | `اختار طفل لافتة يقبل رقمها القسمة على 5. أيّ لافتة اختار؟` | a `52`, b `38`, **c `60`**, d `41` | inchangée |
| 07/01-pratique Q6 | `يقبل العددُ 438 القسمةَ على 3. ما الدليل على ذلك؟` | a `رقم آحاده 8` [critere-divisibilite-mal-choisi], b `لأنّه عددٌ زوجيّ ينتهي بـ 8` [critere-divisibilite-mal-choisi], c `رقم عشراته 3`, **d `مجموع أرقامه 15`** | `مجموعُ أرقام 438 هو 4 + 3 + 8 = 15، و15 مضاعفٌ للعدد 3، فالعددُ 438 يقبل القسمة على 3: 438 = 3 × 146. رقمُ الآحاد ورقمُ العشرات لا يُثبتان شيئًا عن 3، وكونُ العدد زوجيًّا يخصّ القسمة على 2.` |
| 07/02-boss Q6 | `ما أكبرُ عددٍ من رقمين آحادُه 3 ويقبل القسمة على 3؟` | a `33` [extremum-demande-ignore], b `63` [extremum-demande-ignore], c `73`, **d `93`** | `نريد عددًا آحاده 3 ومجموع رقميه مضاعف لـ 3: رقم العشرات 3 أو 6 أو 9 (الصفر لا يصلح في خانة العشرات). الأعداد 33 و63 و93 تصلح، وأكبرها 93 = 3 × 31. العدد 73 مجموع رقميه 10 فلا يقبل القسمة على 3.` |
| 09/quiz Q1 | `ما الكسرُ المساوي لـ 1/4 بمقامٍ يساوي 20؟` | a `1/20` [equivalence-un-seul-terme-multiplie], b `20/4` [numerateur-denominateur-inverses], **c `5/20`**, d `4/20` [equivalence-facteur-errone] | `بما أنّ 4 × 5 = 20، نضرب البسطَ أيضًا في 5: 1/4 = (1×5)/(4×5) = 5/20.` |
| 10/01-pratique Q2 | `قُسّمت فطيرتان متقايستان: الأولى إلى نصفين، والثانية إلى أربعة أرباع. أيّ قطعة أكبر: 1/2 أم 1/4؟` | **a `1/2`**, b `1/4` [comparaison-par-denominateur], c `القطعتان متساويتان`, d `لا يمكن المقارنة دون قياس` [comparaison-jugee-impossible] | `البسطان متساويان (1)، فالأكبر صاحب المقام الأصغر: الفطيرة الأولى قُسّمت إلى أجزاء أقلّ، فأجزاؤها أكبر، إذن 1/2 > 1/4.` |
| 10/01-pratique Q3 | `في علبة حلوى، أكل وليد 2/7 منها وأكلت أخته 4/7 منها. مَن أكل أقلّ؟` | a `أخته` [comparaison-a-meme-denominateur-inversee], **b `وليد`**, c `أكلا القدر نفسه`, d `لا نعرف دون عدّ` [comparaison-jugee-impossible] | `المقام نفسه (7)، فالأصغر صاحب البسط الأصغر: 2 < 4، إذن 2/7 < 4/7، فوليد أكل أقلّ.` |
| 10/01-pratique Q6 | `شربت نادية 1/2 لتر من العصير، وشرب كريم 3/5 لتر. مَن شرب أكثر؟ (اكتب الكسرين على المقام 10)` | a `نادية` [comparaison-a-meme-denominateur-inversee], b `شربا القدر نفسه`, c `لا يمكن المقارنة` [comparaison-jugee-impossible], **d `كريم`** | `نوحّد على 10: 1/2 = 5/10 و 3/5 = 6/10؛ وبما أنّ 5 < 6 فإنّ 1/2 < 3/5، وكريم شرب أكثر.` |
| 10/02-boss Q1 | `أكلت سلمى 4/9 من فطيرة، وأكل سامي 7/9 من فطيرة مثلها. مَن أكل أكثر؟` | a `سلمى` [comparaison-a-meme-denominateur-inversee], **b `سامي`**, c `أكلا القدر نفسه`, d `لا نعرف دون رسم` [comparaison-jugee-impossible] | `الكسران لهما المقام نفسه (9)، فالأكبر صاحب البسط الأكبر: 7 > 4، إذن 7/9 > 4/9، وسامي أكل أكثر.` |
| 10/02-boss Q2 | `حلّ ياسين 3/4 من تمارين الكرّاس، وحلّت هالة 3/7 من التمارين نفسها. مَن حلّ أكثر؟` | **a `ياسين`**, b `هالة` [comparaison-par-denominateur], c `حلّا القدر نفسه`, d `لا نعرف لأنّ المقامين مختلفان` [comparaison-jugee-impossible] | `البسطان متساويان (3)، فالأكبر صاحب المقام الأصغر: 4 < 7، إذن 3/4 > 3/7، فياسين حلّ أكثر.` |
| 10/02-boss Q6 | `أكمل بالعلامة المناسبة بعد كتابة الكسرين على المقام 6: 2/3 … 5/6` | a `>` [comparaison-a-meme-denominateur-inversee], **b `<`**, c `=`, d `لا علامة تصلح` [comparaison-jugee-impossible] | inchangée |
| 10/03-revision Q1 | `قطع أمين 2/5 من الطريق، وقطعت مريم 1/5 منه. أيّ جملة صحيحة؟` | **a `قطع أمين أكثر من مريم`**, b `قطعت مريم أكثر من أمين` [comparaison-a-meme-denominateur-inversee], c `قطعا المسافة نفسها`, d `لا يمكن الحكم لأنّ الكسرين مختلفان` [comparaison-jugee-impossible] | `المقام نفسه (5)، فنقارن البسطين: 2 > 1، إذن 2/5 > 1/5، وأمين قطع أكثر.` |
| 10/03-revision Q2 | `أيّ كتابة صحيحة؟` | a `5/6 < 5/9` [comparaison-par-denominateur], **b `5/6 > 5/9`**, c `5/6 = 5/9`, d `لا يمكن المقارنة` [comparaison-jugee-impossible] | inchangée |
| 10/03-revision Q3 | `أكلت ريم 1/3 خبزة، وأكل أخوها 1/2 خبزة مثلها. أيّ جملة صحيحة؟` | a `أكلت ريم أكثر من أخيها` [comparaison-a-meme-denominateur-inversee], b `أكلا القدر نفسه`, c `لا يمكن المقارنة لأنّ المقامين مختلفان` [comparaison-jugee-impossible], **d `أكل أخوها أكثر منها`** | `نوحّد على 6: 1/3 = 2/6 و 1/2 = 3/6؛ وبما أنّ 2 < 3 فإنّ 1/3 < 1/2، فأخوها أكل أكثر.` |
| 10/04-defi Q1 | `رتّب تصاعديًّا العددين 7/10 و 3/5.` | **a `3/5 < 7/10`**, b `7/10 < 3/5` [comparaison-a-meme-denominateur-inversee], c `3/5 = 7/10`, d `لا يمكن ترتيبهما` [comparaison-jugee-impossible] | `نوحّد على 10: 3/5 = 6/10؛ وبما أنّ 6 < 7 فإنّ 3/5 < 7/10، وهذا هو الترتيب التصاعديّ.` |
| 10/04-defi Q6 | `بعد الاختزال، أيّ جملة صحيحة عن الكسرين 10/15 و 14/21؟` | a `الكسر 10/15 هو الأكبر`, **b `الكسران متساويان`**, c `الكسر 14/21 هو الأكبر`, d `لا يمكن الحكم` [comparaison-jugee-impossible] | inchangée |
| 10/05-entrainement Q1 | `ضع العلامة المناسبة مكان النقاط: 6/11 … 9/11` | a `>` [comparaison-a-meme-denominateur-inversee], **b `<`**, c `=`, d `لا علامة تصلح` [comparaison-jugee-impossible] | `عند تساوي المقام، الأكبرُ بسطًا هو الأكبر؛ 6 < 9، إذن 6/11 < 9/11.` |
| 10/05-entrainement Q2 | `قطعتا قماش متقايستان: قُسّمت الأولى إلى 5 أجزاء متساوية والثانية إلى 9. أخذت ليلى 4 أجزاء من الأولى، وأخذت سارة 4 أجزاء من الثانية. مَن أخذت أكثر؟` | **a `ليلى`**, b `سارة` [comparaison-par-denominateur], c `أخذتا القدر نفسه`, d `لا نعرف دون قياس` [comparaison-jugee-impossible] | `أخذت ليلى 4/5 وسارة 4/9. البسطان متساويان، فالأكبر صاحب المقام الأصغر: 5 < 9، إذن 4/5 > 4/9، وليلى أخذت أكثر.` |
| 11/05-entrainement Q3 | `قرأ سامي 1/3 كتاب يوم السبت، و1/4 منه يوم الأحد. أيّ كسر من الكتاب قرأ في اليومين؟` | a `2/7` [add-numerators-and-denominators], b `2/12`, **c `7/12`**, d `1/12` | `نوحّد على 12: 1/3 = 4/12 و 1/4 = 3/12؛ ثمّ 4/12 + 3/12 = 7/12 من الكتاب.` |
| 11/05-entrainement Q5 | `في قارورة 5/6 لتر من الحليب، شرب منها أنس 1/2 لتر. كم لترًا بقي؟` | **a `1/3`**, b `4/6`, c `1/4`, d `4/4` [soustraction-denominateurs] | `نوحّد على 6: 1/2 = 3/6؛ ثمّ 5/6 − 3/6 = 2/6، وبالاختزال على 2 يبقى 1/3 لتر.` |
| 12/05-entrainement Q3 | `ما القيمةُ العشرية للكسر 80/100؟` | a `8` [virgule-ignoree-nombre-lu-entier], b `0,08` [puissance-de-dix-rangs-mal-comptes], **c `0,8`**, d `80` [virgule-ignoree-nombre-lu-entier] | `مقامُ الكسر 100، فله رقمان بعد الفاصلة: 80/100 = 0,80 = 0,8.` |

Ajouter à ces 20 lignes : 07/05-entrainement Q6 et 09/04-defi Q2 (r-2) et 10/04-defi Q7 (r-1), qui sont mesurés
dans le même calcul. Valeurs re-vérifiées : 33, 63, 93 ÷ 3 ; 5/20 ; 7/9 > 4/9 ; 3/4 > 3/7 ; 2/5 > 1/5 ; 1/3 < 1/2 ;
3/5 = 6/10 < 7/10 ; 10/15 = 14/21 = 2/3 ; 6/11 < 9/11 ; 4/5 > 4/9 ; 1/2 = 5/10 < 6/10 ; 2/7 < 4/7 ;
1/3 + 1/4 = 7/12 ; 5/6 − 1/2 = 1/3 ; 80/100 = 0,8. **Résultat sur le corpus entier après remplacement : 0 paire
≥ 0,6** (24 paires dans [0,45 ; 0,6[, toutes des exercices parallèles voulus).
