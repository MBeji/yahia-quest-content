# Re-vérification ciblée — lot SVT-L05

Auditeur de SVT-L05, 2026-10-12. Écrit au fil de l'eau. Aucun fichier modifié, aucune écriture git.

## Cadre

- Arbre `/home/user/wt-svt5` tel quel : 4 missions du ch.12 (non suivies) + `09-al-ikhraj/exercices/07-examen-2026-ex1-…-ammoniac.json` modifié (Q4 : énoncé + explication). Empreintes au début : `/tmp/claude-0/svt-l05-audit-work/rv/sha-start.txt`.
- Re-résolution à l'aveugle (extraction sans clé, sans explication, sans étiquette : `rv/blind.txt`) de chaque question retouchée et de ses voisines, AVANT la lecture des clés.
- Figures : les 13 SVG ont la même empreinte md5 qu'à l'audit (10 Q3 reprend tel quel le SVG de Q1/Q2) → jugement de l'audit inchangé.
- Gates (lecture seule) : `content:check` ✓ ; `content:qa:strict` 0 erreur, aucun avertissement sur ch.09/12 ; `content:figures:check` ✓ ; `content:tranche --chapters 09,12 --fresh` : 24 questions, clé strictement la plus longue 0/19, positions 5/4/6/4, 0 paire proche, 0 candidat gabarit.

## 1. Questions retouchées — re-résolution et vérification des textes

| question | ma réponse (aveugle) | clé | texte de l'audit appliqué | verdict |
| --- | --- | --- | --- | --- |
| 07 Q4 | c | c | énoncé mot pour mot ✓ | OK — plus de « 24 ساعة » ni d'indice |
| 07 Q5 (expl.) | a | a | « تضمحلّ ولا تنقسم » ✓ | OK |
| 07 Q3 (expl.) | a | a | mot pour mot ✓ | OK — « غدّة ملحقة » n'y figure plus |
| 07 Q6 | b, d, a, c | idem | restée d2 (décision) | OK (réserve m-07-2 maintenue, sans texte) |
| 07 Q7 | d | d | énoncé + explication mot pour mot ✓ | OK — d aux deux lectures (jour 7 ou 8) |
| 08 Q1 | b | b | d étiquetée `lieux-des-gametes-confondus` ✓ (c aussi, a muette) | OK |
| 08 Q4 | b | b | énoncé + début d'explication mot pour mot ✓ | OK clé ; **mon texte gardait une fuite** — m-R2 |
| 09 Q2 | a | a | énoncé, options b et c, explication mot pour mot ✓ | OK — b, c vraies sur la figure mais non probantes ; plus de renvoi à un document absent ; longueurs 31/36/33/39 |
| 09 Q4 (expl.) | d | d | piège réécrit mot pour mot ✓ | OK |
| 10 Q1 (expl.) | a | a | mot pour mot ✓ | OK |
| 10 Q2 | 28 | c | — (passée d2) | OK, d2 honnête |
| 10 Q3 | d | d | explication ✓ ; énoncé = écart de l'auteur (voir § 2) | OK |
| 10 Q4 | b | b | — | OK |
| 10 Q5 | c | c | énoncé mot pour mot ✓ ; explication à une graphie près (« المرأة ب » au lieu de « (ب) ») | OK |
| 10 Q6 | d | d | énoncé avec « جسم المرأة (ب) القادرة » au lieu de « امرأة (ب) قادرة » ; b et c étiquetées `bio.cycle.uterus-autonome` ✓, a muette | OK |
| 10 Q7 | b | b | « كريّات قطبيّة يظهر عددها في الرّسم » ✓ (le dessin en montre deux) | OK |
| 09/07 Q4 (publiée) | c | c | — (décision de l'orchestrateur) | OK clé ; réserve m-R1 |

Clés : 17/17 identiques à ma résolution aveugle.

## 2. Écarts de l'auteur

- **10 Q3, énoncé raccourci** (« يمثّل المنحنى التّالي حرارة جسم المرأة (أ) بالدّرجة المئويّة (التّواريخ بصيغة اليوم/الشهر، فـ 14/4 هو 14 أفريل). … ») : accepté. Il se lit seul (la figure porte tout), ne donne ni valeur ni date, ne fuit ni vers Q1 ni vers Q2. Ordre visuel mesuré en Chromium `dir=rtl` : « 14/4 » d'un seul tenant, parenthèses à leur place ✓. Passée en d2 : honnête.
- **10 Q6** « المرأة (ب) القادرة » et **10 Q5 expl.** « المرأة ب » : variantes sans effet, acceptées.
- **Mission 10 en d3 boss 120/30**, titre « ⭐⭐⭐ » : conforme ; rampe 2,2,2,3,3,3,3 non décroissante ✓. Étage honnête : Q4 à Q7 sont de vrais d3 une fois les fuites retirées.
- **07 Q6 restée d2** : décision, pas un défaut bloquant (le d1 réel reste noté).

## 3. Fuites vers toute la 9ᵉ (le donjon tire dans toutes les missions non-quiz de la classe ; il ne transmet pas le titre des missions : `get_dungeon_questions` renvoie prompt, options, type, explication, difficulté et matière seulement)

- 10 Q3/Q5/Q6 : plus aucune valeur ni comparaison recopiée ✓. Explications de 10 Q3/Q5 : plus de « 28 » ✓. 07 Q4/Q5 : plus de « 24 ساعة » ✓. 07 Q7 : plus de « اليوم الرّابع » ✓.
- 08 Q4 : l'énoncé ne nomme plus le lieu ✓. **Mais l'explication garde « لم يكن موجودًا في البلازما ولا في البول الأوّليّ ثمّ ظهر في البول النّهائيّ، وهذا دليل على الإفراز »**, qui est la clé (b, « لم يُرشَّح أصلًا بل أُفرِز … وهو البرهان على وظيفة الإفراز ») de la mission publiée 09/02 Q4 (d2, même pool). Mon texte M-08-1 avait laissé cette phrase : défaut de mon propre correctif → m-R2.
- **09/07 Q4 reformulée** : clé unique (c, `الأنبوب البولي`) — a et b exclues par la donnée « لا توجد في بلازما الكبيبة ولا في البول الأوّليّ », d exclue par le cours (sécrétion par les cellules du tube urinaire). Elle ne nomme plus l'ammoniac, ni dans l'énoncé ni dans l'explication (« هذه المادّة ») : plus de fuite vers 08 Q4 ✓ ; 08 Q4 ne donne plus son lieu ✓. Deux réserves : (i) « في أيّ مستوى **من النّيفرون** » élimine d par simple définition — le cours ch.09 compose le néphron de la glomérule, de la capsule et du tube urinaire, « الأنبوب الجامع » est hors néphron —, la question se résout alors sans savoir où a lieu la sécrétion → m-R1 ; (ii) l'explication (« وهذا هو الإفراز ») redonne, comme avant la reformulation, la clé de 09/02 Q4 : préexistant, hors du lot.
- **Titre de 09/07** « … وأنزيمات العصارات الهاضمة وإفراز النّشادر » : absent du donjon, mais affiché sur la route de quête du ch.09, avant le ch.12 ; il énonce un résultat (« l'ammoniac est sécrété »), qui est la clé de 08 Q4 → m-R3.
- Résiduel, hors périmètre et préexistant : l'option vraie e et l'explication de 09/09 Q3 (« إفراز مواد كالنّشادر في الأنبوب البوليّ ») et les données de 09/02 Q4 rendent 08 Q4 déductible. C'est le prix du maintien de 08 Q4 (décision de l'orchestrateur) : quatre items de la 9ᵉ portent le même fait.
- 09 Q2 → 10 Q7 : l'explication de 09 Q2 (« الخلايا الجريبيّة … لا يحدّدان الحدث ») écarte la composante « خلايا جريبيّة » des options a et d de 10 Q7. Sans conséquence : la règle donnée dans 10 Q7 désigne déjà la clé (réserve m-10-6 de l'audit).
- Chaîne 10 Q5 / Q7 : inchangée, réserve de l'audit maintenue (inférence, pas recopie).

## 4. Mineurs restants, avec texte

- **m-R1 — 09/07 Q4 (publiée)** : `prompt` → « تظهر في البول النّهائيّ مادّة لا توجد في بلازما الكبيبة ولا في البول الأوّليّ. في أيّ مستوى تُضاف هذه المادّة إلى البول؟ » Vérifié : clé c inchangée et unique par le cours ; a et b restent exclues par la donnée, d par le savoir « الإفراز في الأنبوب البوليّ » et non plus par la définition du néphron ; aucune substance n'est nommée.
- **m-R2 — 08 Q4 explication** (correction de mon texte M-08-1) : remplacer « يفرز النّيفرون النّشادر: لم يكن موجودًا في البلازما ولا في البول الأوّليّ ثمّ ظهر في البول النّهائيّ، وهذا دليل على الإفراز. » par « يفرز النّيفرون النّشادر، وهو المثال الذي يقدّمه الدّرس على وظيفة الإفراز. » ; le reste est inchangé (« أمّا البولة والحمض البوليّ … الخطأ الشائع: عدّ كلّ مادّة تخرج في البول مادّة مفرَزة. »). Vérifié : la nouvelle phrase ne dit ni le lieu (09/07 Q4) ni la preuve par les données (09/02 Q4), et elle ne contredit pas le cours ch.09 (« إفراز بعض المواد كالنّشادر »).
- **m-R3 — titre de 09/07** : remplacer par « 🏛️ مناظرة 2026 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — الانقباض البطينيّ والأعصاب الشّوكيّة وأنزيمات العصارات الهاضمة ووظائف النّيفرون ». Le motif est conforme et le titre ne nomme que des notions. Le slug (`…-ammoniac`), qui fait l'identité de la mission, reste inchangé.
- Rappels de l'audit, sans texte, inchangés : m-07-2 (07 Q6 d1 réel), m-10-4 (28 = durée canonique), m-10-6 (règle qui désigne la clé de 10 Q7).

## 5. Bilan

- Clés fausses : **0** (17 questions re-résolues à l'aveugle).
- Majeurs : **0** (les 5 de l'audit sont corrigés et vérifiés mot pour mot ; écart de 10 Q3 accepté).
- Mineurs restants avec texte : **3** (m-R1, m-R2, m-R3) ; 3 réserves sans texte maintenues.
- Étiquettes neuves : 08 Q1 d et 10 Q6 b, c exactes, et les doubles erreurs restent muettes.
- Rendu `dir=rtl` : conforme ; figures inchangées.
- **Verdict : livrable** une fois m-R2 appliqué (fuite réelle vers 09/02 Q4, introduite par mon propre texte) ; m-R1 et m-R3 sont recommandés, non bloquants.
