# Re-vérification ciblée — gisement arabe 9ᵉ, lot L04

> Auditeur indépendant, 2026-10-14. Objet : application de `audit-arabe-L04.md` par le commit
> `b8e45fb4` (avec `bb07f349`) de `/home/user/wt-argis`. Diff lu : `bb07f349^..b8e45fb4` sur les 7
> missions et sur `cours.md`/`resume.md` des ch. 03 et 18. Journal de l'auteur :
> `auteurs-notes/L04/CORRECTIONS.md`. Aucune écriture dans `content/` ni dans git.
> Rapport rédigé au fil de l'eau.

Contrôles outillés (état `b8e45fb4`) :
- `content:check` ✓ (29 082 questions).
- `content:tranche` sur 03, 04, 15–19 : 0/282 clé strictement la plus longue et 0 paire proche.
- Clé strictement la **plus courte** : 8 items sur 44 (18 %, sous le hasard de 25 %). Les écarts sont de 1 à 3 caractères, ou il s'agit de mots seuls (03 Q2 « غَدًا » face à « أَمْسِ »). Ce n'est pas un indice exploitable.
- `isolateLtrRuns` : aucune chaîne n'est modifiée ; il ne reste aucun « ( …… ) ».
- Chromium `dir=rtl` (`/opt/pw-browsers/chromium-1194`), captures de 19 Q2–Q5, 15 Q1, 16 Q2, 17 Q5, 18 Q5 et 04 Q3 : ordre affiché = ordre source. Les chiffres, les « … » et les guillemets sont bien placés.

## 1. Mission 15/06 — 6 questions, rampe 2-2-2-3-3-3

- **Q1 (M-1)** : mon texte est repris mot pour mot pour l'énoncé, b, d et l'explication.
  - Écart 1 (a et c deviennent « … مبتدأٌ جديدٌ ») : **accepté**. Je mesurais les longueurs sans voyelles ; en caractères bruts, ma clé était bien la plus longue. L'auteur a eu raison de corriger.
  - Les longueurs sont maintenant 40/37/39/38, avec une clé à 38. « جديد » ne marque que des distracteurs, et les votes restent à 2/2.
  - Re-résolu : **d**. L'explication ne dit plus « لا وظيفة لها », qui est la clé de Q2.
- **Q4 c (écart 4)** : « لأنّ فيه فعلًا، والجملة الاعتراضيّة لا تكون إلّا اسميّةً لا فعليّةً » est **accepté**.
  - L'option est fausse selon le cours (« أكرمه الله » est une incise verbale) et n'est contredite par aucune prémisse. Elle est muette, et c'est le distracteur le plus long (67).
  - Re-résolu : **d**.
- **Q5 b (M-2)** : mon texte, mot pour mot. Re-résolu : **c**.
- Q2, Q3 et Q6 sont inchangés : OK. Aucune fuite.

## 2. Mission 04/07 — 5 questions, rampe 1-1-2-2-2

- **Q2 (M-4)** : mon énoncé, mot pour mot.
  - Écart 4 (d « مجزومٌ وعلامة جزمه الكسرة ») : **accepté**. L'option est fausse et vient d'une confusion plausible, puisque la mission montre aussi « اتْرُكِ القِمَارَ ».
  - L'explication de l'auteur est juste.
  - Re-résolu : **a**. La sukun visible sur « تُفَرِّطْ » écarte b, c et d : c'est un trait d'item de niveau d1 qui existait déjà, accepté.
- **Q3 (ex-Q4, M-6)** : la réplique est vérifiée mot pour mot contre 2022 technique, § 2 : « اتْرُكُوا الْأَشْجَارَ أَيُّهَا الرِّجَالُ، إِنَّهَا لَا تَعْنِي شَيْئًا لَكُمْ » ; « ولكنّهم أصرّوا » ✓.
  - La prémisse « جاء الرجال … يريدون أن يراهنوا على أشجار » est fidèle (« فَجَاءَ إِلَيَّ الرِّجَالُ … لَنْ نُرَاهِنَ إِلَّا عَلَى الْأَشْجَارِ »).
  - Options, clé c, étiquettes et explication : mon texte.
  - Re-résolu : **c**. Les énoncés des Q1, Q4 et Q5 parlent du père (النصح) : aucune fuite vers الالتماس.
- Q1, Q4 et Q5 sont inchangés : OK.

## 3. Mission 16/06 — 7 questions, rampe 1-2-2-2-2-3-3

- **Q2** : les « … » sont posés ; l'ordre RTL est vérifié en Chromium. Appariement re-résolu : l1-r3, l2-r1, l3-r2 ✓.
- **Q3 (M-7)** : options et explication sont mon texte. Re-résolu : **d**. Plus aucun « بِمَاذَا » (clé de Q4).
- **Q7 (ex-Q8, M-9)** : mon texte, et la coquille est corrigée. Re-résolu : **c**. Votes à 2/2.
- **Voisines** :
  - Q4 : **b** ✓.
  - Q5 : **c** ✓. Fuite résiduelle par l'explication de Q3 (« بلى » après une question négative) : mineur déjà accepté, deux items officiels.
  - Q6 : **b** ✓.

## 4. Mission 17/06 — 7 questions, rampe 1-2-2-3-3-3-3

- **Q1 (M-11)** : l'énoncé et les options sont mon texte. Re-résolu : **b**.
  - Écart 2 (explication sans « العشرة » ni « زمان ») : **accepté sur le fond**, mais la raison donnée est inexacte. Le cours 17 enseigne bien « أسماءُ الشّرطِ عشرةٌ ».
  - Ce qui reste — « وهي اسمٌ لا حرف » — affirme sans justifier : **mineur r-2** ci-dessous.
- **Q3 (écart 3)** : « والثانية تفعل ذلك أيضًا فيستقيم بها المعنى مع «كُلَّمَا» » est **accepté**. La fuite du sens « زمان » vers Q6 est supprimée (je l'avais manquée au premier tour). Re-résolu : **a, b**.
- **Q5 (M-12)** ✓, re-résolu **c**. **Q6 (m-5)** ✓, re-résolu **b** : rien dans les Q1 à Q5 ne livre « متى = زمان ».

## 5. Mission 18/06 — 6 questions, inchangée hors explications et Q5

- **Q5 (C-1)** : clé **a** ✓, re-résolu **a**. L'explication est mon texte ; étiquettes b et c `harf-ma3na-khalt`, d muette ✓.
- **Q1 (M-14)** : mon texte ✓. **Q2 (m-6)** : ✓.
- Q3 est re-résolu **d**. Il est maintenant enseigné par le cours (§ 7).

## 6. Mission 03/07 — 8 questions

- **Q4 (M-16)** : la vocalisation et l'explication sont mon texte ✓. Re-résolu : **c**.
- **Q2 (m-7, écart 6 : d1)** : la rampe d1 est acceptée. Mais « الكلمات » est **inexact**, puisque « مُنْذُ سَاعَةٍ » et « فِي المَقْهَى » font deux mots ; c'était ma propre suggestion, elle était fausse. → **r-3**.
- **Q8 (ex-Q9, m-8 : d3 → d2) — FUITE CRÉÉE (majeur R-1).** Le compilateur trie par étage, donc Q8 (d2) sort maintenant avant Q7 (d3, ordering). Son explication (« القالب «فعل … وقد فعل» يدلّ على حالةٍ انقضتْ قبيل فعلٍ منقضٍ ») livre la clé de Q7 (« وقد تركت » précède « خرجت »).
  - Dans l'autre sens, l'explication de Q7 (« حالةٌ انقضتْ قبيل الخروج ») livrait déjà la clé de Q9 dans la version d'origine : je l'avais manqué au premier tour.
  - Mon m-8 était une erreur. → **R-1**.
- Q1, Q3, Q5 et Q6 : re-résolus **b, d, a/b/c, d** ✓. Q7 : **c, a, b** ✓.

## 7. Les deux ajouts de cours

- **18 `cours.md` l. 431**, bloc « 🗡️ » sous le tableau لم / لمّا / لن.
  - Exact : nasb après « لن » ; chute de la nûn devant و الجماعة, ألف الاثنين et ياء المخاطَبة ; la سين et سوف sans effet.
  - Il est bien placé, juste après le paragraphe qui commente le tableau.
  - `renderLesson` le rend en bloc `lesson-blk--astuce` (« حيلة ») ; la puce du `resume.md` est présente dans `renderSummary`.
  - Aucune clé livrée : l'exemple « يحضرون » n'est pas « يتآمرون ».
  - Écart 5 (pas de « ← ») : accepté.
- **03 `cours.md` l. 246**, bloc « 🗡️ » après la définition de الحال.
  - Exact : la حال mot unique est منصوبة et s'accorde en genre.
  - Rendu en « حيلة » ; présent dans `renderSummary` (puce 3).
  - Aucune clé livrée : « مراقبةً » n'est pas « مبكّرةً ».
- **Mineur r-1, commun aux deux ajouts** :
  - Une règle normative s'affiche sous l'étiquette « حيلة » (astuce). Selon la grille du cours, une règle relève de `::: propriete` ou de `> 🏆`.
  - Dans le 03, le bloc s'intercale entre la définition et le tableau « القالب » qui l'illustre. Mieux vaut le placer après ce tableau, avant le `::: piege`.
  - Non bloquant.

## 8. Défauts restants et textes exacts

**R-1 (majeur) · 03 Q8 et Q7, fuite mutuelle.**
- Remettre Q8 à `difficulty: 3`, après Q7 dans le fichier : mon m-8 est annulé.
- Remplacer l'explication de Q7 par : « «قَبْلَ أَنْ تَشْتَدَّ» أداةٌ تفيد أسبقيّة الحدث الرئيسيّ على الحدث الثاني: الخروج سابقٌ لاشتداد الحرارة. و«وَقَدْ تَرَكَتِ الحَيَّ» حالٌ فعلها ماضٍ مسبوقٌ بـ«قد»، فهي حالةٌ منقضيةٌ سبقت الخروج. فالترتيب: ترك الحيّ، ثمّ الخروج، ثمّ اشتداد الحرارة؛ والعبرة بالأداة والحال لا بترتيب ذكرها في الجملة. »
- Elle ne nomme plus « قبيل » : la distinction قبيل / قبل, qui est le cœur de Q8, n'est plus livrée.
- Rampe obtenue : 1-1-2-2-2-2-3-3.

**r-2 (mineur) · 17 Q1, explication.** Remplacer « فهي أداة شرط، وهي اسمٌ لا حرف؛ » par « فهي أداة شرط، وهي من أسماء الشرط مثل «مَنْ» و«مَا» و«أَيْنَمَا»؛ ». Le sens de « أينما » n'y figure pas, donc rien ne fuit vers Q6.

**r-3 (mineur) · 03 Q2, énoncé.** Remplacer « أيّ الكلمات التالية يحقّق ذلك؟ » par « أيّ العبارات التالية تحقّق ذلك؟ ».

**r-1 (mineur)** : étiquette « حيلة » et placement des deux ajouts de cours (§ 7).

## 9. Bilan

- Questions re-résolues à l'aveugle : 44 (toutes les retouchées et leurs voisines).
- Clés fausses : **0**. La clé de 18 Q5 est corrigée.
- Majeurs : **1** (R-1, fuite créée par un étage abaissé sur ma propre recommandation).
- Mineurs : **3** (r-1 à r-3).
- Écarts de l'auteur : les six sont acceptés. Pour l'écart 2, la justification « العشرة non enseigné » est fausse, mais la retouche reste sans dommage.
- **Verdict : livrable après R-1** (deux retouches dans le seul fichier 03/07). r-2 et r-3 sont recommandés, sans être bloquants.

## Suite donnée par le pilote (2026-10-14)

R-1 appliqué (03/07 Q8 remise à `difficulty: 3` ; explication de Q7 remplacée mot pour mot, sans « قبيل »).
r-1 : les deux règles ajoutées passent de `> 🗡️` (astuce) à `::: propriete` (`> 🏆` est la clôture
« retenir » du chapitre dans `lesson-blocks.ts`, inadapté) ; bloc du 03 laissé avant le tableau (la règle
porte sur la حال définie juste au-dessus). r-2 et r-3 appliqués. `content:check` vert, prettier propre.
**L04 prêt à livrer.**
