# Audit B3 — maths 6ᵉ, chapitres 13, 14, 15, 22, 24 et 26 (auditeur indépendant, opus)

> Valide pour les fichiers de `content/math-6eme/{13,14,15,22,24,26}-*` tels qu'au commit `915ee40f` (branche
> `wip/maths-6eme-un-passage` ; dernier commit qui les touche : `5bacae6c` ; aucun changement non commité dans le lot
> au moment de l'audit). Ré-auditer si ces fichiers bougent. 2026-10-19.
>
> ⚠️ Hors périmètre : pendant l'audit, `16f230da` (missions M2) a ajouté au ch. 14 les exercices `06`–`10` et au ch. 15
> les exercices `06`–`09`, et deux lignes `sources[]` aux `chapter.json`. Ces fichiers ne sont **pas** audités ici ;
> le cours, le résumé, le quiz et les exercices `01`–`05` des six chapitres sont inchangés depuis `915ee40f`.
>
> Protocole : re-résolution à l'aveugle de **chaque** question (312 : 6 quiz + 30 exercices) avant de lire clés et
> explications ; lecture intégrale des 6 cours et 6 résumés, chaque exemple, piège et `verifie` recalculé ; figures
> re-dérivées sur leurs coordonnées ; reprises confrontées au PDF (`102609` ص 53, 81, 120, 136–137, 148–149, 154–155 ;
> `502603` p.180) ou à la fiche lue à l'image (ص 16–18, 55–58) ; rendu vitest + Chromium 360 px ; les quatre gates.
> Rapport de l'auteur lu **après** la re-résolution et l'écriture des constats (réponses en fin de fichier).

## Verdict : **à corriger** (1 critique, 96 majeurs, 23 mineurs)

**312/312 clés justes**, une seule réponse défendable partout, aucune option désignée par sa place, aucune notion ⛔
(ni calcul littéral, ni ÷ de fractions, ni produit en croix, ni volume ; M3 sans objet dans ce lot : aucun angle),
notation propre, rendu propre, gates verts. **M1 tenu** (× de deux fractions enseigné et exercé au ch. 13) ; ch. 14 :
échelle, quatrième proportionnelle sans produit en croix et pourcentage à base inconnue par 1 % **tenus** ; **avis
défavorable à la scission de « السلّم » seule** (raisons et couture alternative au ch. 14) ; paires proches du ch. 26
**justifiées**, sauf un vrai miroir. Ce qui bloque :

1. **Une affirmation fausse dans un exemple résolu** (ch. 14, C14-1) : « 8 cm est le plus court côté », contredit par
   la figure (6 cm). Une ligne à changer.
2. **Des questions qui redonnent un calcul résolu du cours** : 18 au ch. 13, 4 au ch. 14, 5 au ch. 15, 10 au ch. 22
   (plus 5 copies conformes entre exercices), 28 au ch. 24 — où le cours est écrit avec les exercices mêmes de la
   leçon 19 : on change les nombres du cours (M24-1) plutôt que les reprises — et 3 au ch. 26.
3. **Des étiquettes qui nomment une autre erreur** (13 au ch. 24, 3 au ch. 14) et **six pièges du cours sans
   étiquette du registre** (ch. 13, 15, 26 : libellés proposés).
4. Deux clés reconnaissables à leur longueur hors du périmètre de la tranche (ch. 13, ch. 24), un miroir et un
   distracteur auto-réfuté au ch. 26, la réponse d'une reprise imprimée dans le cours (ch. 22).

Toutes les corrections sont des remplacements **au même rang et à la même difficulté** (aucun identifiant ne bouge) ;
chaque texte a été recalculé, la clé n'est jamais strictement la plus longue, une seule réponse, aucune fuite ; les
nombres à plusieurs classes s'écrivent avec U+00A0.

| chapitre | questions re-résolues | clés fausses | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- | --- |
| 13-multiplication-fraction-entier | 56 | 0 | 0 | 20 | 3 |
| 14-proportionnalite-pourcentage | 58 | 0 | 1 | 7 | 7 |
| 15-vitesse-distance-temps | 56 | 0 | 0 | 6 | 4 |
| 22-durees | 56 | 0 | 0 | 16 | 4 |
| 24-decomposition-fractions | 51 | 0 | 0 | 42 | 2 |
| 26-diagrammes-batons | 35 | 0 | 0 | 5 | 3 |
| **total** | **312** | **0** | **1** | **96** | **23** |

(Majeurs comptés par question touchée ; un défaut de cours compte pour un.)

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : 0 erreur ; 3 avertissements, tous au ch. 14 (valeur canonique non reprise
  dans l'explication : `03-revision` Q7, `04-defi` Q9, Q10 — traités au ch. 14 ci-dessous).
- `content:figures:check` ✓.
- `content:tranche -- --chapters <6 slugs> --fresh --strict-longest --strict-lessons` ✓ : clé strictement la plus
  longue 0/97 ; positions de clé 22/25/30/24 % ; patron de notion 0 en recul ; **23 paires proches** (les 12 affichées :
  11 au ch. 26, 1 au ch. 14 — jugées dans leurs chapitres).
- Mesure complémentaire de l'auditeur, sur **tous** les QCM du lot (inchangés compris) : clé strictement la plus
  longue 7/271 ; trois vrais indices de forme (`13` pratique Q3, `24` entraînement Q5, plus boss Q6, quiz Q5 et défi
  Q3 du ch. 24 réglés par M24-2) ; les deux autres sont des nombres à un chiffre de plus (`15` pratique Q5 `160 km`,
  `24` défi Q4), sans indice.
- Scans de notation (hors `<svg>`) : 0 chiffre arabo-indien, 0 LaTeX, 0 `$…$`, 0 `\d \d{3}` en espace simple, 0 virgule
  arabe dans une notation entre crochets.

## Rendu

`renderLesson` / `renderSummary` (vitest jetable, lang `ar`) : 0 résidu `**`, `:::`, `$$`, 0 `<em>` parasite sur les
12 fichiers ; sections 7/10/8/8/7/5, `verifie` repliés 7/10/8/8/7/5, figures 5/4/3/3/4/5. Chromium 360 px :
`scrollWidth` = 360 sur les 12 pages, aucun tableau ni figure > 330 px. Les 24 figures de cours capturées et
re-dérivées : toutes justes **sauf** l'usage qu'en fait le texte au ch. 14 (C14-1). Fichiers jetables supprimés.

---

## Ch. 13 — `13-multiplication-fraction-entier` (56 questions re-résolues)

**Clés : 56/56 justes**, une seule réponse défendable partout, explications justes, aucune lettre ni ordinal.
**M1 tenu** : كسر × كسر enseigné (section 🧩, figure de l'aire 3 × 4 juste : 3 colonnes sur 4 ombrées, 2 rangées
sur 3 foncées → 6/12) et exercé dans 10 questions (quiz Q7, pratique Q8, boss Q8 Q10, révision Q10, défi Q8 Q9 Q10,
entraînement Q9 Q10). Aucun ⛔ : le « tout à partir de la partie » passe par la part unité (P : a puis × b), jamais
par « ÷ كسر ». Cours re-résolu en entier (6/5 ; 12/5 = 2,4 ; 7/5 = 1,4 < 1,8 ; 6/4 = 3/2 ; 15/6 = 5/2 ;
27 : 9 × 2 = 6, 21 ; 121,5 ; 119 ; 1,2 ; 180 ; 6/12 = 1/2 ; 3/10 ; 1/6 ; 12/40 = 3/10 ; 45 ; 40 ; 750 ; 108 ;
300/9 ≈ 33 ; 45 ; 6 ; 48) : tout est juste. Patron : 7 sections, chacune T1 → T2/T3 → T4 → T5 → T6 → T7 → retenir.

Reprises (`03-revision`, `manuel.items`) confrontées au PDF `102609` ص 136–137 : ex. 4 (2/3 × 3,45 = 2,3), ex. 5 ب
(4/5 كم = 800 م), ex. 9 (5/3 de la largeur, 8 م de plus → largeur 12 م) — données identiques. L'ex. 9 du manuel
demande l'aire (240 م²) ; Q9 demande la largeur, étape intermédiaire du même énoncé : acceptable sous le champ.

### Majeurs

**M13-1 — 18 questions redonnent un exemple résolu du cours** (mêmes nombres, souvent le distracteur du piège).
Remplacements au même rang et à la même difficulté ; chaque valeur recalculée, clé jamais strictement la plus longue,
une seule réponse, explication au même gabarit que l'original.

| fichier · Q | redonne (cours) | remplacement vérifié (prompt · options `a`…`d` · clé · étiquettes · explication) |
| --- | --- | --- |
| `quiz` Q1 | ex. 2/5 × 3 = 6/5, piège 2/15 | « ما ناتج 4/5 × 2؟ » · a `8/5` (clé) · b `8/10` (`math.frac.multiplication-les-deux-termes-multiplies`) · c `5/8` (`math.frac.numerateur-denominateur-inverses`) · d `4/10` (`math.frac.multiplication-denominateur-multiplie`) · exp. « نضرب البسطَ في العدد الصحيح ونُبقي المقام: 4/5 × 2 = (4×2)/5 = 8/5. » |
| `quiz` Q2 | propriété 1/7 × 3 = 3/7 | « ما ناتج 1/10 × 3؟ » · a `1/30` (denominateur-multiplie) · b `3/10` (clé) · c `3/30` (les-deux-termes) · d `4/10` (`math.num.operation-inverse-appliquee`) · exp. « نضرب البسطَ في 3 ونُبقي المقام: 1/10 × 3 = (1×3)/10 = 3/10. » |
| `quiz` Q3 | ex. 3/4 × 2 = 6/4 = 3/2, piège 6/8 | « ما ناتج 5/4 × 2 (مع الاختزال)؟ » · a `7/4` (operation-inverse) · b `10/8` (les-deux-termes) · c `5/2` (clé) · d `5/8` (denominateur-multiplie) · exp. « 5/4 × 2 = 10/4، وبالاختزال على 2: 10/4 = 5/2. » |
| `quiz` Q5 | propriété 1/6 × 6 = 1 | « ما ناتج 3/7 × 7؟ » · a `3` (clé) · b `21/49` (les-deux-termes) · c `3/49` (denominateur-multiplie) · d `10/7` (operation-inverse) · exp. « 3/7 × 7 = 21/7؛ وبما أنّ 21 = 3 × 7 فإنّ 21/7 = 3: الضربُ في المقام يعطي البسط. » |
| `01-pratique` Q4 | `verifie` 2/9 × 4 = 8/9, distracteur 2/36 | « ما ناتج 4/9 × 2؟ » · a `4/18` (denominateur-multiplie) · b `8/18` (les-deux-termes) · c `6/9` (operation-inverse) · d `8/9` (clé) · exp. « نضرب البسطَ في 2 ونُبقي المقام: 4/9 × 2 = (4×2)/9 = 8/9. » |
| `01-pratique` Q8 | propriété 1/2 × 3/4 = 3/8 | « ما ناتج 1/3 × 2/5؟ » · a `3/8` (`math.frac.add-numerators-and-denominators`) · b `3/15` (sans étiquette) · c `2/15` (clé) · d `2/3` (sans étiquette) · exp. « نضرب البسطين 1 × 2 = 2 ونضرب المقامين 3 × 5 = 15، فالجداء 2/15. وهو أصغر من 2/5 لأنّنا أخذنا ثلثه. » |
| `01-pratique` Q9 | ex. 3/4 سا = 45 د, piège 75 د | « كم دقيقة في 2/5 سا؟ » · a `24 د` (clé) · b `40 د` (`math.mes.duree-convertie-en-base-cent`) · c `12 د` (`math.frac.fraction-d-un-nombre-etape-oubliee`) · d `120 د` (fraction-d-un-nombre-etape-oubliee) · exp. « الساعة 60 دقيقة. نقسمها على المقام 5: 60 : 5 = 12 د، ثمّ نضرب في البسط 2: 12 × 2 = 24 د. » |
| `02-boss` Q2 | tableau 3/10 × 5 = 15/10 = 3/2 | « ما ناتج 7/12 × 3 (مع الاختزال)؟ » · a `21/36` (les-deux-termes) · b `7/4` (clé) · c `10/12` (operation-inverse) · d `7/36` (denominateur-multiplie) · exp. « 7/12 × 3 = 21/12، وبالاختزال على 3: 21/12 = 7/4. » |
| `02-boss` Q4 | propriété 1/4 × 8 = 2 | « ما ناتج 1/5 × 15؟ » · a `15/75` (les-deux-termes) · b `1/3` (sans étiquette) · c `16/5` (operation-inverse) · d `3` (clé) · exp. « 1/5 × 15 = 15/5؛ وبالاختزال على 5: 15/5 = 3. » |
| `02-boss` Q5 | propriété 5 × 3/4 = 15/4 | « اشترى 7 أكياسٍ في كلٍّ منها 2/5 kg سكّر. ما الكتلةُ الإجمالية؟ » · a `14/5 kg` (clé) · b `9/5 kg` (operation-inverse) · c `14/35 kg` (les-deux-termes) · d `2/35 kg` (denominateur-multiplie) · exp. « الكتلة = 7 × 2/5 = 14/5 kg (أي 2,8 kg). » |
| `02-boss` Q10 | ex. 2/3 × 3/4 = 6/12 = 1/2 (facteurs permutés) | « مستطيلٌ طوله 4/5 m وعرضه 3/4 m. ما مساحته؟ » · a `3/5 m²` (clé) · b `7/9 m²` (add-numerators-and-denominators) · c `12/5 m²` (sans étiquette) · d `31/20 m²` (sans étiquette) · exp. « مساحة المستطيل جداء بعديه: 4/5 × 3/4 = 12/20، وبالاختزال على 4 نجد 3/5 m². » |
| `03-revision` Q4 | propriété 3 × 2/7 = 6/7 | « ما ناتج 5 × 1/8؟ » · a `6/8` (operation-inverse) · b `5/40` (les-deux-termes) · c `1/40` (denominateur-multiplie) · d `5/8` (clé) · exp. « الضربُ تبديليّ: 5 × 1/8 = (1×5)/8 = 5/8. » |
| `04-defi` Q1 | tableau 3/4 × 4 = 12/4 = 3 | « ما ناتج 3/4 × 12؟ » · a `9` (clé) · b `36/48` (les-deux-termes) · c `15/4` (operation-inverse) · d `3/48` (denominateur-multiplie) · exp. « 3/4 × 12 = 36/4؛ وبالاختزال على 4: 36/4 = 9. » |
| `04-defi` Q4 | méthode n × 2/3 = 4 → 6 (cas limite) | « ما العددُ الصحيح الذي إذا ضربناه في 3/4 كان الناتجُ 6؟ » · a `6` · b `9/2` (operation-inverse) · c `2` · d `8` (clé) · exp. « نبحث عن n حيث n × 3/4 = 6. الأرباعُ الثلاثة تساوي 6، فالربعُ الواحد 6 : 3 = 2، والعددُ كلّه أربعة أرباع: 2 × 4 = 8. تحقّق: 8 × 3/4 = 24/4 = 6. » |
| `04-defi` Q5 | propriété 9 × 2/9 = 2 | « ما ناتج 8 × 3/8؟ » · a `3` (clé) · b `24/64` (les-deux-termes) · c `11/8` (operation-inverse) · d `1/3` (sans étiquette) · exp. « 8 × 3/8 = 24/8؛ وبالاختزال على 8: 24/8 = 3. » |
| `05-entrainement` Q2 | propriété 3/5 × 4 = 12/5 | « ما ناتج 5/7 × 3؟ » · a `8/7` (operation-inverse) · b `15/7` (clé) · c `15/21` (les-deux-termes) · d `5/21` (denominateur-multiplie) · exp. « نضرب البسطَ في 3 ونُبقي المقام: 5/7 × 3 = (5×3)/7 = 15/7. » |
| `05-entrainement` Q8 | tableau 3/5 L = 60 cl | « كم سنتيلترًا (cl) في 2/5 L؟ » · a `20 cl` (fraction-d-un-nombre-etape-oubliee) · b `200 cl` (fraction-d-un-nombre-etape-oubliee) · c `400 cl` (sans étiquette) · d `40 cl` (clé) · exp. « اللتر الواحد 100 cl. نقسمها على المقام 5: 100 : 5 = 20 cl، ثمّ نضرب في البسط 2: 20 × 2 = 40 cl. » |
| `03-revision` Q8 (reprise 5 ب) | tableau 4/5 km = 800 m | **garder la question** (reprise fidèle) et changer le **cours** : dans le tableau de la `::: methode` de la section ⏱️, remplacer la ligne `\| 4/5 km    \| (1000 : 5) × 4 m  \| 800 m   \|` par `\| 3/8 km    \| (1000 : 8) × 3 m  \| 375 m   \|` (1000 : 8 = 125, × 3 = 375). |

**M13-2 — piège de la section 🧩 sans étiquette du registre** (et l'erreur étiquetée par 7 distracteurs du
chapitre, `math.frac.add-numerators-and-denominators`, n'est montrée nulle part). Le piège « garder le dénominateur »
(2/3 × 3/4 = 6/3) n'a pas d'étiquette au registre. Remplacer le bloc `> ⚠️` de la section 🧩 par :

> \> ⚠️ **الخطأ الشائع**: جمعُ البسطين وجمعُ المقامين بدل ضربهما، فيكتب التلميذ 2/3 × 3/4 = (2 + 3)/(3 + 4) = 5/7. يغري هذا الخطأ
> \> لأنّنا نعالج الحدّين «بسطًا مع بسط ومقامًا مع مقام» كما في الضرب. لكنّ 5/7 أكبر من 2/3، ونادر أخذ جزءًا ممّا بقي فقط،
> \> فنصيبه أصغر من 3/4 ومن 2/3! في الضرب نضرب البسطين ونضرب المقامين: 2/3 × 3/4 = 6/12 = 1/2.

(5/7 ≈ 0,714 > 2/3 ≈ 0,667 ✓.) Ajouter `math.frac.add-numerators-and-denominators` à `coursePitfalls` ; dans
`resume.md`, puce « ضرب كسر في كسر », remplacer `، لا 6/3.` par `، لا 5/7.` L'erreur « on garde un dénominateur »
reste dite dans la réponse du `verifie` (12/5), ce qui suffit.

**M13-3 — clé reconnaissable à sa longueur** : `01-pratique` Q3 (« كيف نضرب كسرًا في عددٍ صحيح؟ »), clé 34 caractères
contre 21 au plus (question inchangée depuis `origin/main`, donc hors du périmètre mesuré par la tranche). Options
homogènes : a `نضرب المقامَ في العدد ونُبقي البسط` (denominateur-multiplie) · b `نضرب البسطَ والمقامَ كليهما في العدد`
(les-deux-termes) · c `نضرب البسطَ في العدد ونُبقي المقام` (clé, inchangée) · d `نجمع العددَ مع البسط ونُبقي المقام`
(operation-inverse) — longueurs 34/36/34/34.

### Mineurs

- **m13-1** `04-defi` Q8 : la première étape (3/4 × 2/3 = 6/12 = 1/2) est l'exemple résolu du cours, permuté. Prompt
  « ما العدد الذي إذا أخذنا 2/5 من 3/4 منه كان الناتج 6؟ اكتب العدد فقط. » · `answerKey.value` 20 · exp. « 2/5 من 3/4 هو
  2/5 × 3/4 = 6/20 = 3/10. إذن 3/10 من العدد يساوي 6: العُشرُ الواحد 6 : 3 = 2، والعددُ كلّه عشرة أعشار: 2 × 10 = 20.
  تحقّق: 3/4 من 20 هو 15، و 2/5 من 15 هو 6. »
- **m13-2** `04-defi` Q10 (ordering) : deux des quatre produits sont ceux du cours (2/3 × 3/4, 1/2 × 3/4). Remplacer
  l'item `a` par `3/4 × 4/5` et l'item `c` par `1/2 × 3/5` ; l'ordre `b, d, c, a` est inchangé (1/6 < 1/4 < 3/10 <
  3/5). Exp. « نحسب كلّ جداء: 1/2 × 1/3 = 1/6 ، و 1/2 × 1/2 = 1/4 ، و 1/2 × 3/5 = 3/10 ، و 3/4 × 4/5 = 12/20 = 3/5.
  نقارن بتوحيد المقامات على 60: 10/60 < 15/60 < 18/60 < 36/60، فيأتي الجداء 1/6 أوّلًا ثمّ 1/4 ثمّ 3/10 ثمّ 3/5. »
- **m13-3** trois « a/n × n = 1 » quasi jumeaux (quiz Q5 avant correction, `01-pratique` Q5 1/3 × 3, `03-revision`
  Q3 1/5 × 5) : M13-1 en retire un ; les deux autres, dans deux exercices différents, sont tolérables.

---
## Ch. 14 — `14-proportionnalite-pourcentage` (58 questions re-résolues)

**Clés : 58/58 justes**, une seule réponse défendable, explications justes, aucune lettre ni ordinal. Les trois
avertissements de `content:qa` (`03-revision` Q7, `04-defi` Q9, Q10) sont des faux positifs de format : la valeur
est bien écrite dans l'explication, avec l'espace insécable U+00A0 (`800 000`, `29 531,25`, `31 893,75`) que le
contrôle ne reconnaît pas — rien à corriger.

**Points de la consigne.**
- **Échelle** : enseignée (section 🗺️ : définition « بالوحدة نفسها », figure, exemple 120 m → 12 cm → 1/1000,
  piège de la division, méthode à trois formules, cas limite de l'unité 4 cm / 40 km) et exercée 6 fois (quiz Q6,
  pratique Q7, boss Q7, révision Q7 Q10, entraînement Q7) dans les deux sens. Aucune aire à l'échelle (◐ au §3.2) :
  boss Q7 porte sur un **périmètre** ✓.
- **Quatrième proportionnelle sans produit en croix comme règle** : tenu. Le terme officiel « الرّابع التّناسبي » est
  enseigné, par le coefficient, le facteur entre colonnes ou une colonne intermédiaire ; ni le cours ni aucune
  explication n'écrit « (a × b)/c » ni « produit en croix ».
- **Pourcentage à base inconnue** : enseigné (section 🔙) par le passage à 1 % — jamais « ÷ 0,8 » ou « ÷ 1,08 » ;
  exercé au quiz Q7, boss Q8 (hausse), défi Q11 ; le cas limite « 15 % = 45 élèves → 300 » couvre la base inconnue
  hors prix.
- **Avis sur la scission de « السلّم » (10 notions)** — **ne pas sortir l'échelle seule.** Raisons : (1) l'échelle est
  une **application** des trois sections qui la précèdent (coefficient, retour à l'unité, quatrième proportionnelle) ;
  la sortir l'orpheline de son outil et laisserait un ch. 14 à 9 notions, toujours au-dessus du seuil de ~8 — la
  scission ne résoudrait pas ce qu'elle vise. (2) La couture naturelle du chapitre est celle du **manuel** : leçon 14
  (« التّناسب في السّلّم », période 2) d'un côté, leçons 32 et 37 (« التّناسب … النّسبة المائويّة », périodes 3 et 4)
  de l'autre — soit **proportionnalité + échelle (4 notions)** et **pourcentage (6 notions)**, deux chapitres sous le
  seuil, chacun avec ses leçons codifiées. (3) Le T2 (situation 2, p.180) mêle échelle et pourcentage sur un seul
  terrain : rien n'interdit qu'un exercice d'intégration mobilise deux chapitres. Si l'humain veut scinder, c'est
  donc à cette couture-là, avec un slug neuf pour la partie pourcentage (le `chapterId` du ch. 14 garde l'échelle,
  qui appartient à son titre « تناسب ») — décision de cursus, hors de cet audit. En l'état, 10 sections de 47 à 61
  lignes toutes au patron : le chapitre est long mais pas confus, et **la scission n'est pas un prérequis à la
  publication**.

Cours re-résolu en entier (0,3 ; 48 ; 3,6 ; 45 ≠ 26,25 ; 57 ; 1,4 ; 7 ; 12,6 ; 7 kg ; 1,2 ; 9,6 ; 15 ; 0,4 ; 20 par
les trois voies ; 38 → 95 ; 50 ; 30 ; 1/1000 ; 80 m ; 67 km ; 1/1 000 000 ; 5 m ; 4 cm ; 1/4 ; 2/5 ; 0,1875 ; 3/5 ;
1/20 ; 108 ; 10 800 ; 861 ; 0,36 ; 126 ; 10 ; 45 ; 9 ; 4,5 ; 3 ; 25 % ; 18 % ; 125 % ; 57,14 % ; 40 % ; 60 % ; 30 ;
19,5 ; 400 ; 397,44 ; 86,4 ; 60 ; 57,6 → 46,08 ; 40 ; 300 ; 440 ; 435,6) : tous les calculs sont justes ;
une affirmation est fausse — « 8 cm est le côté le plus court » de l'exemple 🗺️, contredite par la figure (C14-1). Les six `coursePitfalls`
sont montrés en `> ⚠️` et portés par au moins un distracteur. `resume.md` : 10 puces, une par section, dans l'ordre.

Reprise (`04-defi`, `manuel` 502603 p.180, 184–186) confrontée au PDF : 37,5 m ; largeur 3/5 → 22,5 m ; 843,75 m² ;
35 د/m² → 29 531,25 د ; 6 % + 2 % → 31 893,75 د — données et résultats identiques au corrigé.

### Critique

**C14-1 — exemple résolu faux contre sa propre figure** (`cours.md`, section 🗺️, `::: exemple سلّم تصميم الحديقة`,
étape 4) : « 8 cm على التصميم تمثّل 8 × 1000 = 8000 cm = 80 m، وهو فعلًا الضلع الأقصر للحديقة ✓ ». La figure (re-dérivée
sur ses coordonnées : base 240 px = 12 cm, soit 20 px/cm) a un côté de **6 cm** (hauteur, 120 px ↔ 60 m) et un côté
oblique de 7,2 cm (144 px) : le côté de 8 cm n'est **pas** le plus court. Le cours affirme un fait faux, coché ✓.
Remplacer l'étape 4 par : « 4. نتحقّق بضلع آخر: 6 cm على التصميم تمثّل 6 × 1000 = 6000 cm = 60 m، وهو فعلًا الضلع
الأقصر للحديقة ✓ — لأنّ كلّ أبعاد التصميم صُغّرت بالعدد نفسه. » (6 cm est bien le plus court des quatre côtés :
6 < 7,2 < 8 < 12.)

### Majeurs

**M14-1 — 4 questions redonnent un exemple résolu du cours.**

| fichier · Q | redonne (cours) | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q2 | ex. 25 % = 25/100, piège 100/25 | « ما النسبةُ المئوية 35% على شكل كسر؟ » · a `35/10` · b `35/100` (clé) · c `100/35` (`math.frac.numerateur-denominateur-inverses`) · d `35` · exp. « النسبةُ المئوية مقامُها 100، فإنّ 35% = 35/100 (ويُختزل إلى 7/20). » |
| `quiz` Q3 | ex. 20 % de 50 = 10 | « ما قيمةُ 20% من 35؟ » · a `20` (`math.prop.pourcentage-recopie-comme-resultat`) · b `15` · c `7` (clé) · d `55` (`math.num.operation-inverse-appliquee`) · exp. « 20% من 35 = (20/100) × 35 = 7، أو 20% هي الخُمس: 35 ÷ 5 = 7. » |
| `04-defi` Q2 | ex. 20 % de 50 = 10 (d3 !) | « بلوزةٌ ثمنُها 70 دينارًا، خُفّض السعرُ بنسبة 20%. ما قيمةُ التخفيض؟ » · a `20 دينارًا` (pourcentage-recopie) · b `14 دينارًا` (clé) · c `50 دينارًا` · d `56 دينارًا` · exp. « قيمةُ التخفيض = 20% من 70 = (20/100) × 70 = 14 دينارًا، أو 20% هي الخُمس: 70 ÷ 5 = 14. » |
| `04-defi` Q3 | suite de Q2 (même donnée) | « البلوزة نفسُها (70 دينارًا، تخفيض 20%): ما الثمنُ بعد التخفيض؟ » · a `50 دينارًا` · b `14 دينارًا` · c `56 دينارًا` (clé) · d `84 دينارًا` (operation-inverse) · exp. « الثمنُ بعد التخفيض = 70 − 14 = 56 دينارًا. نتحقّق: 100% − 20% = 80%، و 80% من 70 = 56. » |

(70 et non 45 ou 60 : 20 % de 45 est déjà `05-entrainement` Q10, et « 20 % → 48 » est l'exemple de la section 🔙.)

**M14-2 — trois étiquettes qui nomment une autre erreur que celle exécutée.**
- `02-boss` Q3, option b `11,5 دينارًا`, étiquetée `math.prop.additive-au-lieu-de-multiplicative` : ajouter la
  différence donne 7,5 + (8 − 3) = **12,5**, pas 11,5 (qui n'exécute aucune erreur identifiable). Remplacer le texte
  par `12,5 دينارًا` (garder l'étiquette).
- `01-pratique` Q4, option a `8 دنانير` (= 5 + 3), étiquetée `additive-au-lieu-de-multiplicative` : 3 est la quantité,
  pas une différence ; l'erreur est « une somme au lieu d'un produit ». Ré-étiqueter
  `math.num.operation-inverse-appliquee`.
- `05-entrainement` Q3, option d `5`, étiquetée `math.prop.pourcentage-recopie-comme-resultat` : 5 n'est pas dans
  l'énoncé, c'est 100/20, la fraction retournée. Ré-étiqueter `math.frac.numerateur-denominateur-inverses`.

### Mineurs

- **m14-1 — étiquette « pourcentage recopié » sur des questions sans pourcentage** (le libellé montré à l'élève parle
  de « 20 % de 80 ») : quiz Q1 b, `01-pratique` Q1 b et Q4 b, `02-boss` Q1 b, `03-revision` Q1 b, `05-entrainement`
  Q1 b et d — rendre ces options **muettes**. `02-boss` Q10 d (`40`) : 40 % est calculé, pas recopié — muette aussi.
- **m14-2 — options à deux erreurs étiquetées** : quiz Q7 d `32 د` (base finale ET réduction réappliquée) et boss Q8 c
  `37,5 د` (base finale ET hausse réappliquée) portent `operation-inverse-appliquee` — les rendre muettes.
  quiz Q6 c `0,015 m` : 3 ÷ 200 = 0,015 **cm** ; écrit en m, l'option ajoute une erreur d'unité à la division —
  remplacer le texte par `0,015 cm` (même forme que `01-pratique` Q7 c `0,005 cm`), garder l'étiquette.
- **m14-3 — langue des montants** : `01-pratique` Q6, options a `2 دينارًا` et c `1 دينارًا` → `2 دنانير` et
  `1 دينار` (accord du تمييز, comme partout ailleurs dans le chapitre).
- **m14-4 — contexte adulte** : `::: verifie` de la section 🔙 (« أجر عامل 484 د »). Remplacer la question par « بعد
  زيادة 10% صار عدد كتب مكتبة القسم 484 كتابًا. كم كان عددها قبل الزيادة؟ » et la réponse par « بعد الزيادة صار العدد
  100% + 10% = 110% من العدد الأصليّ. 110% تقابل 484 كتابًا، فـ 1% تقابل 484 ÷ 110 = 4,4، و 100% تقابل 4,4 × 100 =
  440 كتابًا. نتحقّق: 10% من 440 هي 44، و 440 + 44 = 484 ✓. من طرح 10% من 484 وجد 435,6 لأنّه حسب النسبة من العدد
  الجديد لا من الأصليّ. » (Le T2 « وكيل عقّاري / مصاريف التسجيل » de `04-defi` Q7–Q10 est une reprise officielle :
  on la garde.)
- **m14-5 — champ `manuel` du défi** : `items` annonce « T2 situation 2 (1-2 à 3-2) », mais la consigne 1-2 (choisir
  le plan à l'échelle parmi trois) n'est pas reprise ; Q7 (largeur) est la première étape de 2-2. Écrire
  « T2 situation 2 (2-2, 3-2) ». La paire proche Q7 ↔ Q8 (0,71) est la suite officielle d'un même terrain, chaque
  question une étape distincte : justifiée, rien à réécrire.
- **m14-6 — trois méthodes côte à côte (R-7)** dans l'exemple de la section 🔢 : non majeur, car deux des trois sont
  déjà possédées (coefficient : section ⚖️ ; colonne intermédiaire = retour à l'unité généralisé : section 🧮) ; seule
  « العامل بين العمودين » est neuve. Rien à réécrire ; à garder en tête si la section est retouchée.
- **m14-7** `01-pratique` Q2 (50 % = 1/2) et `03-revision` Q3 (75 % = 3/4) récitent le tableau des « نسب مفيدة » :
  tolérable pour du d1–d2 (fait de référence, pas exemple résolu).

---
## Ch. 15 — `15-vitesse-distance-temps` (56 questions re-résolues)

**Clés : 56/56 justes**, une seule réponse défendable, explications justes, aucune lettre ni ordinal. Le cours (inchangé
sur l'essentiel depuis `origin/main`) est re-résolu en entier (12 m ; 0,6 ; 18 ; 37 ; 15 د ; 30,6 ; 80 ; 0,0125 ;
60 ; 36 ; 12 ; 360 ; 123 ; 40 ; 60 ; 180 ; 4 ; 25 600 سا ≈ 2,9 ans ; 1,8 = 1 سا 48 ; 3,75 = 3 سا 45 ; 30 ; 18 ;
12 د ; 600 ; 9 ; 5,4 ; 4,5 ; 0,075 ; 70 ; 1224 ; 192 → 75 ; 19,5 / 18 ; 3 سا / 2,5 سا ; 3,25 / 3 ; 32 ; 36 ;
16 سا 15 ; 9 سا 30 ; 80 ≠ 90) : tout est juste. Huit sections au patron ; aucune division par une fraction (la
section 🔁 complète à 60 min, conforme à §3.2). `resume.md` : 8 puces, une par section.

Reprises confrontées au PDF `102609` : `03-revision` « ex. 7 (51) » (ص 149 : المحمديّة 7 س 45 → زغوان 9 س 10, 36 km/h
→ 51 km) ✓ ; `04-defi` « ex. 6 (53) » (ص 154 : 30 km = 2/5, 50 puis 75 km/h → 72 د) ✓ ; `05-entrainement`
« ex. 5 (53) » (ص 154 : 27 km en 1 س 30, 7,5 km → 25 د) ✓. Erratum n° 60 (80 كم/س) appliqué au cours ✓.

### Majeurs

**M15-1 — 5 questions redonnent un exemple résolu du cours.**

| fichier · Q | redonne (cours) | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q7 | ex. et tableau 20 د = 1/3 سا, piège 0,2 | « كم ساعةً تساويها 40 د؟ » · a `0,4 سا` (`math.mes.duree-convertie-en-base-cent`) · b `1/2 سا` · c `2/3 سا` (clé) · d `1/4 سا` · exp. « الساعة 60 د، فنكتب 40 د = 40/60 سا، وبالاختزال على 20 نجد 2/3 سا. الكتابة 0,4 سا تساوي 24 د فقط. » |
| `01-pratique` Q9 | ex. de l'escargot 3 m en 5 د, `verifie` 9 m en 15 د | « تقطع آلةٌ 4 m في 6 د، و 8 m في 12 د بسرعة ثابتة. كم مترًا تقطع في 30 د؟ » · a `28 m` (`math.prop.additive-au-lieu-de-multiplicative` : 4 + (30 − 6)) · b `120 m` (`math.num.operation-inverse-appliquee` : 4 × 30) · c `20 m` (clé) · d `5 m` · exp. « 30 د = 5 × 6 د، فالمسافة 5 × 4 = 20 m. وطريق ثانية: 30 د = 2,5 × 12 د، فالمسافة 2,5 × 8 = 20 m. » |
| `02-boss` Q5 | cas limite 900 km en 1 سا 30 → 600 km/h | « قطعت طائرةٌ 750 km في ساعةٍ ونصف (1,5 ساعة). ما سرعتها؟ » · a `500 km/h` (clé) · b `1125 km/h` (operation-inverse) · c `375 km/h` · d `751,5 km/h` (`math.prop.vitesse-grandeurs-additionnees`) · exp. « السرعة = المسافة ÷ الزمن = 750 ÷ 1,5 = 500 km/h. » |
| `03-revision` Q1 | cas limite 90 km en 1 سا → 90 km/h | « قطعت سيّارةٌ 85 km في ساعةٍ واحدة. ما سرعتها؟ » · a `85 km/h` (clé) · b `8,5 km/h` · c `86 km/h` (vitesse-grandeurs-additionnees) · d `42,5 km/h` · exp. « السرعة = المسافة ÷ الزمن = 85 ÷ 1 = 85 km/h. » |
| `04-defi` Q4 | ex. 90 km/h pendant 20 د → 30 km (d3 !) | « سيّارةٌ سرعتُها 66 km/h. كم km تقطع في 20 دقيقة (ثلثِ ساعة)؟ » · a `66 km` · b `198 km` (operation-inverse) · c `33 km` · d `22 km` (clé) · exp. « 20 دقيقة = 1/3 ساعة؛ المسافة = 66 × 1/3 = 66 ÷ 3 = 22 km. » |

**M15-2 — trois pièges du cours sans étiquette du registre** (§ C-5 du patron) : section 🔁 (diviser par le nombre
de minutes et lire le résultat en km/h), section ⚖️ (juger le plus rapide à la distance seule), section 🗺️
(moyenne des deux vitesses). Les deux derniers sont pourtant exécutés par des distracteurs (`02-boss` Q7 a `22,5`,
`03-revision` Q8 a `18` ; le premier par quiz Q6 b `0,2 km/h` = 4 ÷ 20). Proposition pour l'auteur (registre
`content/misconceptions.json`, puis étiquettes et `coursePitfalls`) :
- `math.prop.vitesse-moyenne-des-vitesses` — fr « Tu fais la moyenne des deux vitesses : la vitesse moyenne d'un
  trajet est la distance totale divisée par la durée totale » ; ar « تحسب منتصف السرعتين: معدّل سرعة الرحلة هو
  المسافة الكلّيّة مقسومةً على الزمن الكلّيّ » → `02-boss` Q7 a, `03-revision` Q8 a ;
- `math.prop.vitesse-unite-de-temps-non-convertie` — fr « Tu divises par le nombre de minutes : tu obtiens la distance
  d'une minute, pas d'une heure » ; ar « تقسم على عدد الدقائق: تحصل على مسافة دقيقة واحدة لا ساعة » → quiz Q6 b.
Le piège « distance seule » n'a pas de distracteur QCM (boss Q10 est numérique) : il peut rester sans étiquette si
l'on retire son `> ⚠️` en prose ordinaire, ou recevoir un troisième libellé — au choix de l'auteur. Ajouter aussi
`math.prop.additive-au-lieu-de-multiplicative` à `coursePitfalls` : le piège de la section 🐌 (3 + 15 = 18) l'exécute
et `01-pratique` Q9 a le porte.

### Mineurs

- **m15-1 — reprise devenue variante** : `04-defi` Q9 porte « ex. 9 (53) », mais le manuel (ص 155) donne l'horaire
  (départ 6 س, Béja 7 س 30) et demande la **vitesse** ; la question donne la vitesse et demande la durée, et change la
  voiture en حافلة. Retirer « ex. 9 (53) » de `manuel.items` (une variante ne porte pas le champ).
- **m15-2 — quasi-doublon dans le quiz** : Q1 (120 km en 2 سا) et Q5 (180 km en 3 سا) ont la même clé 60 km/h et la
  même forme. Q5 → « قطعت حافلةٌ 195 km في 3 ساعات. ما سرعتها؟ » · a `65 km/h` (clé) · b `585 km/h`
  (operation-inverse) · c `198 km/h` (vitesse-grandeurs-additionnees) · d `97,5 km/h` · exp. « السرعة = المسافة ÷
  الزمن = 195 ÷ 3 = 65 km/h. »
- **m15-3 — langue** : « 2 ساعة » (quiz Q4 c, `01-pratique` Q6 b et son explication, `04-defi` Q2 « لمدّة 2 ساعة ») →
  « ساعتان » / « ساعتين » ; `04-defi` Q2 « سار شخصان … بسرعة 60 km/h » (on ne marche pas à 60 km/h) → « سافر شخصان
  بالسيّارة: الأوّل بسرعة 60 km/h لمدّة ساعتين، والثاني بسرعة 40 km/h لمدّة 4 ساعات. مَن قطع مسافةً أطول؟ ».
- **m15-4** `02-boss` Q6 (12 km/h pendant 0,5 سا → 6 km) est le `verifie` de la section ⚡ pris à l'envers (6 km en
  0,5 سا → 12 km/h) : tolérable (autre inconnue), à varier si l'exercice est retouché.

---
## Ch. 22 — `22-durees` (56 questions re-résolues)

**Clés : 56/56 justes**, une seule réponse défendable, explications justes, aucune lettre ni ordinal. Les trois
horloges re-lues sur leurs coordonnées : `01-pratique` Q3 (aiguille rouge, 24 unités, vers 3 ; noire, 30 unités, vers
12 → 3 سا ✓), Q7 (petite aiguille à 82,5° = 2 h 45, grande vers 9 → 2 سا 45 د ✓), `03-revision` Q7 (petite à 250° =
8 h 20, grande à 120° → 8 سا 20 د, + 1 سا 50 د = 10 سا 10 د ✓). Le cours (inchangé depuis `origin/main`) est
re-résolu en entier (7 سا 40 ; 168 سا ; 9 سا 15 ; 5 د ; 2 سا 30 ; 195 د ; 4 د ; 3 سا 20 ; 2,25 سا ; 50 د ; 1,5 سا ;
4 سا 15 ; 9 سا 26 د 12 ثا ; 3 سا 30 ; 6 سا 18 ; 2 سا 14 د 30 ثا ; 1 سا 45 ; 4 سا 35 ; 4 سا 20 ; 30 سا ; 9 سا 15 ;
7 سا 30 ; 14 سا ; 1 سا ; 7 سا 35 ; 43 سا 30 ; 21 سا 5 د 15 ثا ; 2 سا 55 ; 9 سا 48) : tout est juste. Huit sections au
patron, quatre `coursePitfalls` montrés et portés. `resume.md` : 8 puces.

Reprises (`04-defi`, « ex. 5 », « ex. 8 », leçon 5, ص 16–18, d'après la fiche §2 sexies) : Q7 (horloge qui retarde
de 10 ثا/سا, 10 سا → 16 سا le lendemain → 5 د) ✓ ; Q10 (80 آر/سا, 10 سا 30 د → 840 آر) ✓ — voir m22-2.

### Majeurs

**M22-1 — 15 questions en double** : cinq copies conformes d'une autre question du chapitre (quiz ↔ pratique,
boss ↔ entraînement — héritées de `origin/main`, que la tranche ne compare pas) et dix reprises d'un exemple résolu
du cours. Remplacements au même rang ; chaque valeur recalculée ; clé jamais strictement la plus longue ; aucun
nouveau couple miroir entre eux.

| fichier · Q | double de | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q3 | `01-pratique` Q5 et définition « 2 سا = 120 د » | « كم دقيقةً في 7 ساعات (7 سا)؟ » · a `420 د` (clé) · b `60 د` · c `700 د` (`math.mes.duree-convertie-en-base-cent`) · d `168 د` (`math.mes.constante-de-temps-attribuee-a-la-mauvaise-unite`) · exp. « 7 سا = 7 × 60 = 420 دقيقة. » |
| `quiz` Q4 | méthode « 180 ثا = 3 د » | « 780 ثانية تساوي كم دقيقة؟ » · a `13 د` (clé) · b `78 د` (base-cent) · c `60 د` · d `7,8 د` (base-cent) · exp. « نقسمُ على 60: 780 ÷ 60 = 13 دقيقة. » |
| `01-pratique` Q1 | quiz Q1 | « كم ثانيةً في دقيقتين؟ » · a `120 ثا` (clé) · b `200 ثا` (base-cent) · c `20 ثا` (base-cent) · d `48 ثا` (constante-mauvaise-unite) · exp. « الدقيقةُ الواحدة = 60 ثانية، فدقيقتان = 2 × 60 = 120 ثانية؛ التحويلُ في الزمن يكون بـ 60. » |
| `01-pratique` Q2 | quiz Q2 | « كم ساعةً في 540 دقيقة؟ » · a `9 سا` (clé) · b `5,4 سا` (base-cent) · c `22,5 سا` (constante-mauvaise-unite) · d `54 سا` (base-cent) · exp. « الساعة 60 د، فنقسم على 60: 540 ÷ 60 = 9 سا. » |
| `01-pratique` Q4 | quiz Q5 | « كم يومًا في 96 ساعة؟ » · a `4 أيّام` (clé) · b `1,6 يوم` (constante-mauvaise-unite) · c `9,6 أيّام` (base-cent) · d `8 أيّام` (constante-mauvaise-unite) · exp. « اليومُ الواحد 24 ساعة، فنقسم على 24: 96 ÷ 24 = 4 أيّام. » |
| `01-pratique` Q5 | quiz Q3 et définition « 2 سا = 120 د » | « كم دقيقةً في 6 ساعات (6 سا)؟ » · a `360 د` (clé) · b `60 د` · c `600 د` (base-cent) · d `144 د` (constante-mauvaise-unite) · exp. « 6 سا = 6 × 60 = 360 دقيقة. » |
| `02-boss` Q2 | méthode « 3 سا = 180 د » ; = `05-entrainement` Q2 | « كم دقيقةً في 8 ساعات (8 سا)؟ » · a `480 د` (clé) · b `192 د` (constante-mauvaise-unite) · c `800 د` (base-cent) · d `240 د` · exp. « 8 سا = 8 × 60 = 480 دقيقة. » |
| `02-boss` Q3 | `verifie` « 240 ثا = 4 د » | « 660 ثانية تساوي كم دقيقة؟ » · a `11 د` (clé) · b `66 د` (base-cent) · c `110 د` · d `6,6 د` (base-cent) · exp. « نقسمُ على 60: 660 ÷ 60 = 11 دقيقة. » |
| `03-revision` Q2 | exemple « نصف الساعة = 30 د » | « ثلثُ ساعةٍ يساوي كم دقيقة؟ » · a `20 د` (clé) · b `33 د` (base-cent : le tiers de 100) · c `15 د` · d `180 د` · exp. « ثلثُ الساعة = 60 ÷ 3 = 20 دقيقة، لأنّ الساعة 60 د لا 100. » |
| `03-revision` Q4 | exemple « 300 ثا = 5 د » | « 360 ثانية تساوي كم دقيقة؟ » · a `6 د` (clé) · b `36 د` (base-cent) · c `3,6 د` (base-cent) · d `15 د` (constante-mauvaise-unite) · exp. « نقسمُ على 60: 360 ÷ 60 = 6 دقائق. » |
| `04-defi` Q2 | exemple « 2 سا 40 د + 1 سا 35 د » (d3 !) | « احسب: 3 سا 45 د + 1 سا 50 د. » · a `5 سا 35 د` (clé) · b `4 سا 95 د` (`math.mes.duree-retenue-de-soixante-non-faite`) · c `6 سا 35 د` · d `4 سا 35 د` (retenue-non-faite) · exp. « المجموع = 4 سا 95 د، ونحوّلُ 95 د = 1 سا 35 د، فالنتيجة = 5 سا 35 د. » |
| `04-defi` Q5 | piège « 1 سا 30 د = 90 د, pas 130 » | « 2 سا 40 د تساوي كم دقيقة؟ » · a `160 د` (clé) · b `240 د` (base-cent) · c `120 د` · d `180 د` · exp. « 1 سا = 60 د، فإنّ 2 سا 40 د = 2 × 60 + 40 = 120 + 40 = 160 دقيقة. » |
| `04-defi` Q6 | méthode « اليومان = 48 سا » | « كم ساعةً في 3 أيّام؟ » · a `72 سا` (clé) · b `36 سا` (constante-mauvaise-unite) · c `24 سا` · d `180 سا` (constante-mauvaise-unite) · exp. « اليومُ = 24 سا، فإنّ 3 أيّام = 3 × 24 = 72 ساعة. » |
| `05-entrainement` Q2 | `02-boss` Q2 (copie) | « كم دقيقةً في 2 سا 15 د؟ » · a `135 د` (clé) · b `215 د` (base-cent) · c `75 د` · d `120 د` · exp. « 2 سا = 2 × 60 = 120 د، ثمّ 120 + 15 = 135 د. » |
| `05-entrainement` Q3 | exemple « الربع: 60 : 4 = 15 د » | « كم دقيقةً في 1/5 سا؟ » · a `12 د` (clé) · b `20 د` (base-cent : le cinquième de 100) · c `5 د` · d `300 د` · exp. « نقسم الساعة على المقام 5: 60 ÷ 5 = 12 دقيقة، لأنّ الساعة 60 د لا 100. » |

**M22-2 — la réponse de la reprise `04-defi` Q7 (manuel ex. 5) est imprimée dans le cours** : propriété de la section
⏳, « من 10 سا صباحًا إلى 16 سا من اليوم الموالي تمرّ 24 سا + 16 سا − 10 سا = 30 سا » — soit l'étape-clé de Q7 avec
ses données exactes. Garder la reprise, changer le cas limite du cours : remplacer cette phrase par « من 9 سا صباحًا
إلى 14 سا من اليوم الموالي تمرّ 24 سا + 14 سا − 9 سا = 29 سا. » (24 + 14 − 9 = 29 ✓).

### Mineurs

- **m22-1 — rappel pur sur-représenté** : même après M22-1, le chapitre garde six questions de pur rappel d'une
  constante (quiz Q1, Q2, Q5 ; `02-boss` Q1, Q5 ; `03-revision` Q1, Q5 ; `05-entrainement` Q1). `02-boss` Q5
  (« 1 سا = 3 600 ثا ») est étiqueté d3 dans un boss : le ramener à d2. `03-revision` Q1 et `05-entrainement` Q1
  redisent quiz Q2 et Q1 : acceptable dans des exercices de révision, à varier si on y retouche.
- **m22-2 — reprise simplifiée** : `04-defi` Q10 porte « ex. 8 », mais le manuel donne l'horaire (6 سا 30 د → 17 سا
  45 د, 45 د de repos) et c'est l'élève qui trouve 10 سا 30 د ; la question donne directement 10 سا 30 د. Soit
  rétablir l'énoncé du manuel (« بدأ فلاحٌ الحراثة على الساعة 6 سا 30 د وأنهاها على الساعة 17 سا 45 د، واستراح 45 د.
  يحرث 80 آر في كلّ ساعة عمل. كم آرًا حرث؟ » — 17 سا 45 د − 6 سا 30 د = 11 سا 15 د, − 45 د = 10 سا 30 د = 10,5 سا,
  × 80 = 840 ✓), soit retirer « ex. 8 » de `manuel.items`.
- **m22-3** `01-pratique` Q3 : les deux aiguilles ont la même épaisseur (2,5) et l'énoncé ne dit pas laquelle est la
  petite, alors que les deux autres horloges du chapitre le disent. Passer l'aiguille rouge à `stroke-width="4"` et
  ajouter « العقرب القصير هو الغليظ. » à l'énoncé.
- **m22-4 — contexte adulte léger** : propriété de la section 🍰, « حين نضرب مدّة في أجر ساعة » → « حين نضرب مدّة في
  ما يُنجَز في ساعة » (la suite de la phrase dit déjà « أو في ما يُنجَز في ساعة » : supprimer « في أجر ساعة، أو »).

---
## Ch. 24 — `24-decomposition-fractions` (51 questions re-résolues)

**Clés : 51/51 justes** (dont deux `multi` : `03-revision` Q7 {a, b, e}, `04-defi` Q7 {a, b, e}), une seule réponse
défendable, explications justes, aucune lettre ni ordinal. Le cours est re-résolu en entier (20/20 ; 7/5 > 1 ; 5/9 →
2 tafkīk ; 13/15 ; 28/28 ; 28/112 ; 7/9 ; 30/30 ; 10/8 ; 25/25 et 25/100 ; 2 000 → 5, 4, 11 → 22 000 ; 47/20 ; 9/20 ;
35/40 ; 5/5 ; 6/15 et 22/15 ; 43/5 ; 15/4 → 3/4 ; 2/7 ; 5/6 ; 1 + 4/7 ; 41/9 et 45/9 ; 6 + 1/3 ; 8 + 2/11 ; 3 ;
5 + 3/4 ; 7/53 ; 53/53 ; 1 + 1 = 2 ; 8/50 vs 8/25 ; 8/53 ; 24/20 ; 20/20 ; 18/20 et 2/20) : tout est juste, et
l'ancrage المنارة passe bien par 20 parts de 2 000 د, sans addition à dénominateurs différents (la leçon 19 précède la
42). Sept sections au patron, huit `coursePitfalls` montrés.

**Le défaut de fond du chapitre** : le cours est écrit avec les **exercices** de la leçon 19 (أتدرّب 3–7 : 12/10,
13/15, 4/12 + 3/12, 1/9 + 4/9 + 2/9, 30/30, 10/8, 28/20, 5/40, 4/5 + … = 9/5, 3/5 + 8, … + 4 = 19/4, 9/7, 11/7,
49/9, 19/3, 90/11) **et** les questions reprennent ces mêmes exercices. Résultat : **28 questions sur 51** redonnent
un calcul résolu dans le cours. La règle R-2 permet d'ancrer le cours sur les **activités** du manuel (أستحضر 1
« المنارة », أستكشف 2 « le test », أوظّف 8 « la galette », أقيّم 9 « le budget ») ; les **exercices** reviennent aux
questions. D'où deux remèdes : (A) **changer les nombres du cours** là où il emprunte un exercice — les questions,
reprises fidèles, restent ; (B) **remplacer les questions** qui refont une activité du manuel, que le cours garde
comme ancre.

### Majeurs

**M24-1 (A) — le cours change ses nombres** (14 remplacements dans `cours.md`, 5 dans `resume.md` ; chaque égalité
recalculée ; aucun nombre neuf ne figure dans une question du chapitre).

| section · bloc | ancien texte (extrait exact) | nouveau texte |
| --- | --- | --- |
| 🥧 · `> ⚠️` | `كأن نكتب 7/10 = 4/5 + 3/5 لأنّ 10 = 5 + 5` … `لكنّ 4/5 + 3/5 = 7/5، وهو أكبر من 1 لأنّ بسطه أكبر من مقامه، أمّا 7/10 فأصغر من 1.` … `المقام يسمّي حجم القطعة، ولا يتوزّع: 7/10 = 4/10 + 3/10.` | `كأن نكتب 9/14 = 5/7 + 4/7 لأنّ 14 = 7 + 7` … `لكنّ 5/7 + 4/7 = 9/7، وهو أكبر من 1 لأنّ بسطه أكبر من مقامه، أمّا 9/14 فأصغر من 1.` … `المقام يسمّي حجم القطعة، ولا يتوزّع: 9/14 = 5/14 + 4/14.` |
| 🥧 · `propriete` | `7/10 = 4/10 + 3/10 = 2/10 + 2/10 + 3/10 = 1/10 + 6/10` | `9/14 = 5/14 + 4/14 = 2/14 + 3/14 + 4/14 = 1/14 + 8/14` |
| 🥧 · `propriete` | `12/10 = 5/10 + 4/10 + 3/10` | `11/8 = 6/8 + 3/8 + 2/8` |
| 🥧 · `propriete` | `للعدد 5/9 في حدّين ببسطين غير منعدمين تفكيكان فقط، دون اعتبار الترتيب: 1/9 + 4/9 و 2/9 + 3/9.` | `للعدد 9/13 في حدّين ببسطين غير منعدمين أربعة تفكيكات فقط، دون اعتبار الترتيب: 1/13 + 8/13 و 2/13 + 7/13 و 3/13 + 6/13 و 4/13 + 5/13.` |
| 🥧 · `verifie` | question `فكّك 13/15 …` ; réponse `13/15 = 6/15 + 7/15، أو 13/15 = 10/15 + 3/15، لأنّ 6 + 7 = 13 و 10 + 3 = 13. ومن كتب مقامين مختلفين، مثل 6/7 + 7/8` | question `فكّك 11/12 إلى حدّين بطريقتين مختلفتين.` ; réponse `نبحث عن بسطين مجموعهما 11، ونُبقي المقام 12 في الحدّين: 11/12 = 5/12 + 6/12، أو 11/12 = 8/12 + 3/12، لأنّ 5 + 6 = 11 و 8 + 3 = 11. ومن كتب مقامين مختلفين، مثل 5/6 + 6/6، قسم المقام بدل أن يُبقيه.` |
| 🧩 · `> ⚠️` | `كأن نكتب 4/12 + 3/12 = 7/24` … `المقام لا يُجمع: 4/12 + 3/12 = 7/12.` | `كأن نكتب 5/16 + 6/16 = 11/32` … `المقام لا يُجمع: 5/16 + 6/16 = 11/16.` |
| 🧩 · `propriete` | `1/9 + 4/9 + 2/9 = 7/9` ; `2/30 + 8/30 + 15/30 + 4/30 + 1/30 = 30/30 = 1` ; `1/8 + 4/8 + 3/8 + 2/8 = 10/8 البسط 10 أكبر من المقام 8` | `2/11 + 3/11 + 5/11 = 10/11` ; `7/25 + 6/25 + 12/25 = 25/25 = 1` ; `3/6 + 2/6 + 4/6 = 9/6 البسط 9 أكبر من المقام 6` |
| 🔍 · `> ⚠️` | `في …/20 + 4/20 + 15/20 = 28/20، من جمع 28 + 4 + 15 وجد 47/20، وهو أكبر وحده من المجموع كلّه 28/20` … `28 − 4 − 15 = 9، فالحدّ الناقص 9/20.` | `في …/16 + 3/16 + 7/16 = 19/16، من جمع 19 + 3 + 7 وجد 29/16، وهو أكبر وحده من المجموع كلّه 19/16` … `19 − 3 − 7 = 9، فالحدّ الناقص 9/16.` |
| 🔍 · `propriete` | `في 5/40 + …/40 + …/40 + …/40 = 40/40 مجموع الحدود الناقصة 35/40، مثلًا 10/40 + 12/40 + 13/40. وقد يكون الحدّ الناقص عددًا صحيحًا: في 4/5 + … = 9/5 نجد 5/5، أي 1.` | `في 6/30 + …/30 + …/30 + …/30 = 30/30 مجموع الحدود الناقصة 24/30، مثلًا 7/30 + 8/30 + 9/30. وقد يكون الحدّ الناقص عددًا صحيحًا: في 3/7 + … = 10/7 نجد 7/7، أي 1.` |
| 🔢 · ancre + `definition` + `exemple` | `8 فطائر كاملة و 3/5 فطيرة` ; `العدد 3/5 + 8` ; `8 = (8 × 5)/5 = 40/5` ; ex. `8 فطائر هي 8 × 5 = 40 قطعة، أي 40/5` ; `3/5 + 8 = 3/5 + 40/5 = 43/5` | `6 فطائر كاملة و 2/5 فطيرة` ; `العدد 2/5 + 6` ; `6 = (6 × 5)/5 = 30/5` ; ex. `6 فطائر هي 6 × 5 = 30 قطعة، أي 30/5` ; `2/5 + 6 = 2/5 + 30/5 = 32/5` |
| 🔢 · tableau | lignes `\| 1 \| 7 \| 7/7 \|`, `\| 4 \| 4 \| 16/4 \|`, `\| 8 \| 5 \| 40/5 \|` | `\| 1 \| 9 \| 9/9 \|`, `\| 3 \| 4 \| 12/4 \|`, `\| 6 \| 5 \| 30/5 \|` |
| 🔢 · `> ⚠️` | `في … + 4 = 19/4، من كتب 4 = 4/4 وجد الحدّ الناقص 15/4. لكنّ 4/4 يساوي 1 لا 4، لأنّ البسط يساوي المقام. الصواب 4 = 16/4، فالحدّ الناقص 19/4 − 16/4 = 3/4.` | `في … + 5 = 27/5، من كتب 5 = 5/5 وجد الحدّ الناقص 22/5. لكنّ 5/5 يساوي 1 لا 5، لأنّ البسط يساوي المقام. الصواب 5 = 25/5، فالحدّ الناقص 27/5 − 25/5 = 2/5.` |
| 🔢 · `propriete` | `1 = 7/7، ففي 9/7 = …/7 + 1 نجد 9/7 − 7/7 = 2/7.` | `1 = 9/9، ففي 13/9 = …/9 + 1 نجد 13/9 − 9/9 = 4/9.` |
| ✂️ · `> ⚠️` | `في 49/9، حيث 49 = (9 × 5) + 4، كتابة 4 + 5/9 تبادل … وكتابة 5 وحده …` `4 + 5/9 = 36/9 + 5/9 = 41/9، و 5 = 45/9، ولا أحد منهما 49/9. الصواب 49/9 = 5 + 4/9، لأنّ 45/9 + 4/9 = 49/9.` | `في 29/4، حيث 29 = (4 × 7) + 1، كتابة 1 + 7/4 تبادل … وكتابة 7 وحده …` `1 + 7/4 = 4/4 + 7/4 = 11/4، و 7 = 28/4، ولا أحد منهما 29/4. الصواب 29/4 = 7 + 1/4، لأنّ 28/4 + 1/4 = 29/4.` |
| ✂️ · `propriete` | `19/3 = 6 + 1/3 لأنّ 19 = (3 × 6) + 1، و 90/11 = 8 + 2/11 لأنّ 90 = (11 × 8) + 2` | `17/3 = 5 + 2/3 لأنّ 17 = (3 × 5) + 2، و 75/11 = 6 + 9/11 لأنّ 75 = (11 × 6) + 9` |
| `resume.md` | puces 1–5 : `و 7/10 لا يساوي 4/5 + 3/5` ; `4/12 + 3/12 = 7/12 لا 7/24؛ وقد يساوي المجموع 1 (30/30) أو يتجاوزه (10/8)` ; `…/20 + 4/20 + 15/20 = 28/20 يعطي 9/20` ; `8 = 40/5، فـ 3/5 + 8 = 43/5؛ و 4 = 16/4 لا 4/4` ; `49 = (9 × 5) + 4، فـ 49/9 = 5 + 4/9، لا 4 + 5/9 ولا 5 وحده` | `و 9/14 لا يساوي 5/7 + 4/7` ; `5/16 + 6/16 = 11/16 لا 11/32؛ وقد يساوي المجموع 1 (25/25) أو يتجاوزه (9/6)` ; `…/16 + 3/16 + 7/16 = 19/16 يعطي 9/16` ; `6 = 30/5، فـ 2/5 + 6 = 32/5؛ و 5 = 25/5 لا 5/5` ; `29 = (4 × 7) + 1، فـ 29/4 = 7 + 1/4، لا 1 + 7/4 ولا 7 وحده` |

Après (A), les questions qui reprennent un exercice — quiz Q1 Q2 Q3 Q6 ; pratique Q2 Q6 ; boss Q1 Q2 Q3 Q5 ;
révision Q1 Q3 Q4 Q5 Q6 Q7 ; défi Q1 Q5 ; entraînement Q1 Q3 Q5 — ne redisent plus le cours. **Seul l'exemple
11/7 reste partagé** (il porte la figure de la section ✂️) : c'est la question qui change, voir (B).

**M24-2 (B) — 7 questions remplacées** (elles refont une activité ancrée dans le cours, ou l'exemple 11/7).

| fichier · Q | redonne | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q4 | ex. 11/7 = 1 + 4/7 | « اكتب 13/5 عددًا صحيحًا طبيعيًّا وجزءًا كسريًّا بسطُه أصغر من مقامه. » · a `2 + 3/5` (clé) · b `3 + 2/5` (`math.frac.partie-entiere-quotient-et-reste-inverses`) · c `2` (`math.frac.partie-entiere-reste-oublie`) · d `13 + 3/5` · exp. « نقسم 13 على 5: الخارج 2 والباقي 3، فيكون 13/5 = 10/5 + 3/5 = 2 + 3/5. » |
| `quiz` Q5 | activité « budget » (24/20) | « ميزانيّة رحلة القسم: النقل 7/20، الأكل 6/20، الدخول 5/20، الهدايا 4/20. ماذا نستنتج؟ » · a `المجموع 22/20، وهو أكبر من الميزانيّة` (clé) · b `المجموع 22/80، وهو أصغر من الميزانيّة` (`math.frac.add-denominators`) · c `المجموع 22/20، وهو أصغر من الميزانيّة` (`math.frac.comparaison-a-l-unite-inversee`) · d `المجموع يساوي الميزانيّة بالضبط` · exp. « نركّب الحصص: 7 + 6 + 5 + 4 = 22، أي 22/20؛ والميزانيّة كاملةً هي 20/20، فالمقترح يتجاوزها لأنّ البسط 22 أكبر من المقام 20. » (longueurs 37/37/37/31 : la clé n'est plus la plus longue.) |
| `02-boss` Q6 | ancre et piège de la section 👥 (4/28 + 3/25 ≠ 7/53) | « في نادي الرسم 5 بنات من 12 عضوًا، وفي نادي المسرح 4 بنات من 15 عضوًا؛ وفي الناديين معًا 9 بنات من 27. فهل هذا يعني أنّ 5/12 + 4/15 = 9/27؟ » · a `لا: 9/27 عددٌ جديد، لا جمعُ كسرين` (clé) · b `نعم: نجمع البُسُط معًا ونجمع المقامات معًا` (`math.frac.add-numerators-and-denominators`) · c `نعم: المقامان مختلفان، فنجمعهما مع البسطين` (`math.frac.add-denominators`) · d `لا: كسران مختلفا المقام لا يُجمعان أبدًا` (muette : `comparaison-jugee-impossible` parle de comparer, pas d'additionner) · exp. « المقام يدلّ على الوحدة المرجعيّة: مرّةً نادٍ من 12، ومرّةً نادٍ من 15، ومرّةً مجموعةٌ من 27. عددنا البنات من جديد (5 + 4 = 9) وعددنا الأعضاء من جديد (12 + 15 = 27)؛ أمّا جمع كسرين فلا يجمع المقامات أبدًا. » (longueurs 33/42/42/40 ; l'ancienne clé faisait 66 contre 37.) |
| `04-defi` Q3 | exemple « budget », étape 3 (24/20 − 4/20) | « بلغت ميزانيّة رحلة القسم المقترحة 22/20، فاقترح المعلّم حذف الهدايا (4/20). هل يكفي اقتراحه؟ » · a `نعم: يصير المجموع 18/20، وهو أصغر من 1` (clé) · b `لا: يبقى المجموع أكبر من الميزانيّة كلّها` · c `نعم: يصير المجموع 18/0 بطرح المقامين` (`math.frac.soustraction-denominateurs`) · d `لا: يصير المجموع 26/20، وهو أكبر من 1` (`math.num.operation-inverse-appliquee`) · exp. « نطرح البُسُط ونُبقي المقام: 22 − 4 = 18، فيصير المجموع 18/20، وهو أصغر من 1 لأنّ البسط أصغر من المقام: تكفي الميزانيّة ويبقى 2/20. » (longueurs 38/41/36/37.) |
| `04-defi` Q4 | exemple « المنارة » (11/20), et prémisse manquante (« مجلس الولاية » n'est pas dit payer le reste) | « بلغت كلفة رحلة مدرسيّة 3 000 د: دفعت الجمعيّةُ نصفَ المبلغ، ودفعت البلديّةُ خُمسَه، وتكفّل الأولياء بالباقي. ما العدد الكسريّ الذي يمثّل نصيب الأولياء؟ » (espace insécable dans `3 000`) · a `3/10` (clé) · b `7/10` (operation-inverse : la part payée au lieu du reste) · c `5/7` (`math.frac.add-numerators-and-denominators` : 1/2 + 1/5 « = » 2/7, reste 5/7) · d `1/10` · exp. « نقسم الكلفة إلى 10 حصص من 300 د: النصف 1 500 د أي 5 حصص، والخُمس 600 د أي حصّتان. فالباقي 10 − 5 − 2 = 3 حصص، أي 3/10 (وهو 900 د). » |
| `04-defi` Q6 | tableau de la section 👥 (ligne « التملّك الأقصى » : 11, 8, **19**) | « يرتدي النظّارات 3 تلاميذ من 24 في السادسة «ج» و 2 من 26 في السادسة «د». ما العدد الكسريّ الذي يمثّلهم في القسمين معًا؟ » · a `5/50` (clé) · b `5/24` · c `1/50` (operation-inverse) · d `6/624` (`math.frac.multiplication-les-deux-termes-multiplies`) · exp. « نعدّ من جديد في المجموعة الكاملة: 3 + 2 = 5 تلاميذ من 24 + 26 = 50 تلميذًا، أي 5/50 — وهذا ليس جمعَ الكسرين 3/24 و 2/26. » |
| `05-entrainement` Q6 | définition de la section 🔍 (`20/20 = 5/20 + 4/20 + …/20`) | « أكمل: 20/20 = 6/20 + 7/20 + …/20. ما الحدّ الناقص؟ » · a `7/20` (clé) · b `7/60` (add-denominators) · c `33/20` (operation-inverse) · d `13/20` · exp. « الحدّان المعلومان يعطيان 13/20، فالباقي هو 20/20 ناقص 13/20 أي 7/20. » |

**M24-3 — 13 étiquettes qui nomment une autre erreur que celle exécutée.** `decomposition-denominateur-partage`
(« tu partages le dénominateur ») est posé sur des options qui **ajoutent** les dénominateurs (16 + 16 = 32,
10 × 3 = 30…). Ré-étiqueter `math.frac.add-denominators` : quiz Q2 c `2/18 + 3/18`, `01-pratique` Q1 b `7/32`, Q2 b
`3/30`, `02-boss` Q3 b `9/60`, Q4 c `4/34`, `03-revision` Q4 b `35/120`, `05-entrainement` Q3 d `5/10`. Rendre
**muettes** (aucune erreur nommable, ou deux) : `01-pratique` Q3 b `3/8 + 5/16`, Q6 c `2/1`, `02-boss` Q2 d
`5 + 4/45`, Q5 d `3/16`, `03-revision` Q2 d `7 + 1/15`. (`04-defi` Q3 c et Q4 c sont refaits par M24-2.)

**M24-4 — clé reconnaissable à sa longueur** : `05-entrainement` Q5, clé 54 caractères contre 38 au plus. Remplacer
le texte de `a` par `نعم، ما دام مجموع البُسُط 7 والمقام 10` (38 ; les autres 37, 38, 37). (quiz Q5, boss Q6, défi
Q3, les trois autres cas du chapitre, sont réglés par M24-2.)

### Mineurs

- **m24-1 — reprises sans champ `manuel`** : presque tous les items numériques sont les exercices 3 à 9 de la leçon
  19 (ص 56–58), mais aucun exercice ne porte `manuel`. Ajouter, par fichier, `"manuel": {"items": [...]}` :
  `01-pratique` [« ex. 3 », « ex. 4 », « ex. 7 », « ex. 8 ب »] ; `02-boss` [« ex. 4 », « ex. 5 », « ex. 6 »,
  « ex. 7 »] ; `03-revision` [« ex. 3 », « ex. 4 », « ex. 5 », « ex. 6 », « ex. 7 »] ; `04-defi` [« ex. 6 »,
  « ex. 8 ب »] ; `05-entrainement` [« ex. 4 », « ex. 5 », « ex. 7 »]. Données confrontées à la fiche §2 sexies
  (lecture à l'image de ص 55–58) : toutes identiques.
- **m24-2** quatre questions tournent autour du même 7/10 (quiz Q1, `03-revision` Q5, `05-entrainement` Q1, Q5) :
  tolérable après M24-1 (le cours passe à 9/14), à varier si on y retouche.

---
## Ch. 26 — `26-diagrammes-batons` (chapitre neuf, 35 questions re-résolues)

**Clés : 35/35 justes**, une seule réponse défendable, explications justes, aucune lettre ni ordinal. Chaque diagramme
re-lu sur ses coordonnées SVG (hauteur × pas de l'axe) et confronté au PDF : `01-pratique` = ص 81 ex. 2 (pluies 50,
80, 160, 180, 240, 200, 220, 140, 40) ✓ ; `02-boss` = ص 53 ex. 9 (familles 50, 300, 200, 600, 100, 50) ✓ ;
`03-revision` = ص 120 ex. 15 (âges 9, 13, 5, 3 ; 13 filles) ✓ ; `04-defi` = ص 102–103 pb 2 (900/750/600/500 et
650/500/450/300, erratum n° 44 appliqué ; 45 % / 23 % ; 950/760 ; 650/546 ; 90 %) ✓ ; `05-entrainement` = guide
502603 p.179/183 (35 %, 40 %, 21 mm ≙ 35 %) ✓. Le cours est re-résolu en entier (14 ; 22 ; 8 ; 30 ; 92 ; 22 − 8 ;
6 + 12 + 9 + 3 = 30 ; 2/5 = 40 % ; 71,43 % ; 3/10 = 30 % ; 25 % ; 0,4 mm ; 10 mm ; 18 mm ; 7 mm et 2 mm ; 6 mm ;
5 / 4 / 3 / 2 cm ; 900 cm ; 3,33 ; 2 / 3,5 / 5 cm ; 75 / 70 / 70 % ; 75 % → +5) et ses cinq figures re-dérivées
(rendu 360 px ci-dessous) : tout est juste. Cinq sections au patron, chacune avec figure, exemple, piège, `verifie`,
`retenir` ; `resume.md` : 5 puces. Notion conforme au §3.2 (critère مع 1 du T2 : lire, compléter, construire) ;
aucun ⛔.

**Les ~21 paires proches** (tranche) : **justifiées**. Chaque question est affichée seule, avec sa propre figure ; le
préambule (« المخطّط يمثّل … ») et le SVG sont donc répétés, et c'est eux qui font la similarité de Jaccard. Les
tâches, elles, sont distinctes dans chaque exercice (lire une barre, sommer, rapport, seuil, étendue ; partie/tout
puis partie/partie au boss Q3 ↔ Q4 — contraste voulu). Une seule paire est un vrai doublon : `03-revision` Q5 ↔ Q6
(M26-4).

### Majeurs

**M26-1 — quiz Q1 redonne l'exemple de la section 📖** (barre lue « 10 + 2 × 2 = 14 », piège « on compte les
divisions » : distracteur 7). Monter la barre du jour 2 à 16 : dans le SVG, remplacer
`<rect x="129.2" y="68.6" width="42.6" height="127.4"` par `<rect x="129.2" y="50.4" width="42.6" height="145.6"`
(pas 182 px / 20 = 9,1 px par unité ; 16 × 9,1 = 145,6 ; 196 − 145,6 = 50,4). Options a `8` · b `16` (clé) · c `10` ·
d `18` ; exp. « بين 0 و 10 خمسة أقسام صغيرة، فكلّ قسم يساوي 2. عصا اليوم 2 تنتهي بعد 10 بثلاثة أقسام: 10 + 3 × 2 =
16. ومن عدّ 8 أقسام وكتب 8 نسي أنّ القسم يساوي 2. »

**M26-2 — quiz Q4 refait l'exemple de la section ✏️** : même part restante (25 %), même longueur unitaire (0,4 mm
pour 1 %), même réponse (10 mm). Nouveau texte : « رُسمت عصيّ لـ 40% و 35% بطولي 32 mm و 28 mm، وبقيت عصا الفئة
الثالثة. ما طولها بالتدريج نفسه؟ » · a `18 mm` (`math.prop.additive-au-lieu-de-multiplicative` : 28 − 10) · b `20 mm`
(clé) · c `25 mm` (`math.prop.pourcentage-recopie-comme-resultat`) · d `8 mm` · exp. « نسبة الفئة الثالثة 100% −
40% − 35% = 25%. طول 1% هو 32 ÷ 40 = 0,8 mm، فطول عصا 25% هو 25 × 0,8 = 20 mm. » (28 ÷ 35 = 0,8 ✓ ; 0,6 mm
est pris par `05-entrainement`.)

**M26-3 — `05-entrainement` Q6 : deux distracteurs qui se réfutent d'eux-mêmes**, et des données reprises du
`verifie` de la section 🔵 (80 élèves, 60 reçus). c « متساويتان لأنّ الفرق … 10 و 20 » conclut à l'égalité sur deux
écarts différents ; d « السنة 2، فنسبتها 75% مقابل 80% » choisit l'année au plus petit taux — éliminés à vue. Nouveau
texte : « في السنة 1: 50 تلميذًا منهم 40 ناجحًا. وفي السنة 2: 90 تلميذًا منهم 63 ناجحًا. في أيّ سنة كانت النتيجة
أفضل؟ » · a `السنة 2، لأنّ 63 ناجحًا أكثر من 40` · b `السنة 1، لأنّ نسبة نجاحها 80% مقابل 70%` (clé) · c `السنة 2،
لأنّ نسبة نجاحها 63% مقابل 40%` (pourcentage-recopie) · d `السنتان متساويتان، لأنّ الناجحين أكثر من النصف في
السنتين` · exp. « نقارن النسب لا الأعداد: السنة 1: 40/50 = 80% ، السنة 2: 63/90 = 7/10 = 70%. فالنتيجة الأفضل في
السنة 1 مع أنّ عدد الناجحين فيها أقلّ. » (longueurs 34/39/39/57.)

**M26-4 — doublon miroir `03-revision` Q5 ↔ Q6** : Q5 demande le % des 13 élèves de 12 ans, Q6 le % des garçons
(30 − 13 filles = 17) ; 43,33 + 56,67 = 100, et l'explication de Q6 le dit. Le 13 filles est celui du manuel (garder
Q6) ; changer Q5 : « … ما النسبة المئويّة التقريبيّة (برقمين بعد الفاصل) لتلاميذ 13 سنة من مجموع تلاميذ القسم؟ اكتب
العدد فقط. » · `answerKey.value` 16.67 (tolérance et unité inchangées) · exp. « عصا 13 سنة تبلغ 5 من 30. نقسم: 5 ÷ 30
≈ 0,1667، ثمّ نضرب في 100: النسبة ≈ 16,67%، أي 16,67. » ; et dans l'explication de Q6, remplacer « والتحقّق: 56,67% +
43,33% = 100%. » par « والتحقّق: نسبة الإناث 13/30 ≈ 43,33%، و 56,67% + 43,33% = 100%. »

**M26-5 — deux pièges du cours sans étiquette du registre** : section 📖 (« on compte les petites divisions comme des
unités », exécuté par quiz Q1 a) et section 🔵 (« on juge aux effectifs, pas aux taux », exécuté par `04-defi` Q3 a
et `05-entrainement` Q6 a). Proposition au registre (puis étiquettes et `coursePitfalls`) :
`math.stat.graduation-comptee-comme-unite` — fr « Tu comptes les petites divisions comme des unités : lis
d'abord combien vaut une division de l'axe » ; ar « تعدّ الأقسام الصغيرة كأنّ كلّ قسم وحدة: اقرأ أوّلًا كم يساوي القسم
على المحور » ; `math.stat.comparaison-par-effectifs` — fr « Tu compares les effectifs au lieu des taux : deux séries
de tailles différentes se comparent par leurs pourcentages » ; ar « تقارن الأعداد بدل النسب: سلسلتان مختلفتا الحجم
تُقارنان بنسبهما المئويّة ».

### Mineurs

- **m26-1** `04-defi` Q6 : « السنة 4 » (650 / 546) n'est pas l'année 4 du diagramme affiché dans l'exercice (500 /
  300) mais celle de l'année universitaire suivante (manuel ب). Écrire « في السنة الجامعيّة الموالية كانت النسبة
  المأمولة لنجاح السنة 4 هي 90%، وبلغ عدد طلبتها 650 وناجحوها 546. هل بلغت النتيجة المستوى المأمول؟ », comme Q5.
- **m26-2** `05-entrainement` Q5 : les quatre diagrammes-réponses n'ont ni axe ni graduation ; seul l'ordre des
  hauteurs discrimine, le « 1 cm لكلّ 20 » n'est pas vérifiable. Acceptable (lecture de l'ordre), mais le titre de la
  compétence promet plus : ajouter un axe gradué 0–3 cm aux quatre options si l'on veut tester l'échelle.
- **m26-3** exemple de la section 📖, étape 3 : « تنتهي قبل 10 بعد 4 أقسام » se lit mal → « تنتهي عند القسم الرابع،
  قبل 10 ».

---

## Après lecture du rapport de l'auteur (`rapports/rapport-B3.md`, lu une fois l'audit écrit)

- **Ids d'étiquettes proposés par l'auteur** : M15-2 et M26-5 reprennent désormais ses ids
  (`math.prop.vitesse-moyenne-des-vitesses`, `math.prop.vitesse-unite-de-temps-non-convertie`,
  `math.stat.graduation-comptee-comme-unite`) — un seul jeu de noms à créer au registre. Pour M13-2, son id
  `math.frac.produit-fractions-denominateur-conserve` est **l'autre remède valable** : le créer au registre, le porter
  sur les distracteurs « dénominateur gardé » (quiz Q7 a `6/3`, `01-pratique` Q8 d `3/2`…) et dans `coursePitfalls`,
  et garder le piège actuel. Dans ce cas, ajouter quand même `math.frac.add-numerators-and-denominators` à
  `coursePitfalls` serait faux (aucun piège ne le montre) : c'est l'un **ou** l'autre. Son
  `math.mes.echelle-unites-non-uniformisees` (ch. 14) est facultatif : les pièges du ch. 14 sont tous étiquetés.
- **Ch. 13, `02-boss` Q10 « ≈ cours, volontaire (rappel) »** : maintenu en majeur (M13-1) — la consigne interdit une
  question qui redonne l'exemple résolu ; un rappel se fait sur d'autres nombres.
- **Ch. 14, 10 sections** : avis donné (ne pas sortir l'échelle seule ; couture du manuel si scission).
- **Ch. 26** : paires proches jugées (justifiées, sauf M26-4) ; lectures R-7 du diagramme ص 102 vérifiées au PDF ;
  compétence `math.stat.effectifs-frequences` empruntée : `content:check` l'accepte, rien à redire.
- **Ch. 22, horloges** : les deux horloges dessinées par script sont justes (2 h 45 et 8 h 20 re-dérivées) ; la
  troisième, héritée (`01-pratique` Q3), ne dit pas quelle aiguille est la petite (m22-3).
- **`displayOrder` 26 du ch. 26** : sans objet pour l'audit.

