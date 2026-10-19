# Audit B3 — maths 6ᵉ, chapitres 13, 14, 15, 22, 24 et 26 (auditeur indépendant, opus)

> Valide pour les fichiers de `content/math-6eme/{13,14,15,22,24,26}-*` tels qu'au commit `915ee40f` (branche
> `wip/maths-6eme-un-passage` ; dernier commit qui les touche : `5bacae6c` ; aucun changement non commité dans le lot
> au moment de l'audit). Ré-auditer si ces fichiers bougent. 2026-10-19.
>
> Rapport écrit au fil de l'eau, chapitre après chapitre. Synthèse et verdict en fin de fichier.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : 0 erreur ; 3 avertissements, tous au ch. 14 (valeur canonique non reprise
  dans l'explication : `03-revision` Q7, `04-defi` Q9, Q10 — traités au ch. 14 ci-dessous).
- `content:figures:check` ✓.
- `content:tranche -- --chapters <6 slugs> --fresh --strict-longest --strict-lessons` ✓ : clé strictement la plus
  longue 0/97 ; positions de clé 22/25/30/24 % ; patron de notion 0 en recul ; **23 paires proches** (21 au ch. 26,
  1 au ch. 14 — jugées dans leurs chapitres).

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
