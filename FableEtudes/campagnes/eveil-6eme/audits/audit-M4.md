# Audit indépendant — lot M4 (missions du gisement, éveil 6ᵉ : `07` 06–09, `11` 06–09, `08` 06)

> Auditeur opus, 2026-10-20. Consigne : `prompt-auditeur-missions.md`. Rapport écrit au fil de l'eau
> (une session précédente a été coupée). Aucune écriture dans `content/`, aucune écriture git.
> Rapport de l'auteur (`rapports/rapport-M4.md`) lu seulement APRÈS la re-résolution.

## État : TERMINÉ (voir synthèse en fin de rapport)

## Méthode

Chaque question re-résolue à l'aveugle avant lecture de la clé ; chaque mission d'examen confrontée à la
transcription `<année>-unique.md` ET au PDF (`pdftoppm`, zoom sur les figures) ; chaque figure rendue dans
Chromium (`/opt/pw-browsers/chromium-1194`, page `dir=rtl`, 360 px, texte passé par `isolateLtrRuns`) ;
boussoles re-résolues par rotation du repère (nord à droite : est en bas, ouest en haut ; nord à gauche : est
en haut, ouest en bas ; nord en bas : est à gauche, ouest à droite). Croisement « ne pas redemander » refait
contre le quiz et les exercices 01–05 ACTUELS de chaque chapitre (E-12).

## Chapitre `07-aimants-boussole`

### 07/06 — `06-exams-2017-2026-poles-force-attraction-et-repulsion.json` (d2 practice 75/15, 9 q) — fidélité OK (2017, 2019, 2024, 2026 conformes au PDF : aiguille 2 de 2019 fausse, lettres أ ب ك ن de 2024)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | OK | |
| 2 | a | a | OK | |
| 3 | d (1 et 5) | d | réserve | même fait que q1, q2 et que `07/quiz#2`, `07/01-pratique#5` |
| 4 | b | b | OK (mineur) | option a = le dessin fautif de l'élève (s'élimine à vue) ; même fait que `07/02-boss#8` |
| 5 | b | b | ERREUR d'étiquette | option c (deux erreurs : noms mal déduits + règle inversée) étiquetée |
| 6 | d | d | réserve | « (الجدول نفسه) » renvoie à une autre question |
| 7 | a | a | ERREUR (fuite) | l'énoncé donne les clés de q5 et q6 |
| 8 | c (aiguille 2) | c | OK | figure fidèle au PDF 2019 |
| 9 | d | d | ERREUR (fuite) | l'énoncé décrit l'aiguille fautive : donne la clé de q8 |

**Défauts**
- **[MAJEUR] q7 — fuite vers q5 et q6.** « وجدنا أنّ (أ) و(ن) يتجاذبان وأنّ (ب) و(ك) يتجاذبان » est la clé de q5 et celle de q6 ; dans le donjon (tirage aléatoire) q7 peut sortir avant. La justification est déjà portée par les options de q5 (« لأنّ … من اسمين مختلفين »). **Correctif : supprimer q7.**
- **[MAJEUR] q9 — fuite vers q8.** « رُسمت الإبرة بحيث يقابل طرفُها الرماديّ الجزءَ الرماديّ من المغنط، وقيل إنّ هذا الرسم خاطئ » donne le critère qui désigne l'aiguille 2 de q8. L'explication de q8 porte déjà la justification (pôles de même nom → répulsion). **Correctif : supprimer q9.**
- **[MAJEUR] q3 — troisième habit du même fait dans la mission, et doublon de `07/quiz#2` (« أين تكون قوّة الجذب أكبر ؟ — عند طرفيه »)** : q1 (2026) et q2 (2024) portent déjà la correction « force maximale aux extrémités ». **Correctif : supprimer q3** (la session 2017 reste servie par m037).
- **[MAJEUR] q5 — option à deux erreurs étiquetée.** Option c « يتجاذبان لأنّ (أ) و(ن) من الاسم نفسه » cumule deux erreurs (noms mal déduits ET règle inversée) qui se compensent dans le verdict : elle doit rester muette ; d (une erreur : règle inversée) garde l'étiquette. **Correctif exact :** dans l'option c de q5, retirer `"misconceptionTag": "eveil.aim.poles-identiques-s-attirent"`.
- **[MINEUR] q6** : retirer « (الجدول نفسه) » de l'énoncé → « مناظرة 2024: في الرسم القطبان (ب) و(ن) يتنافران. مع أيّ قطب من قطبي المغنط 1 يتجاذب القطب (ك)؟ » + la même figure.
- **[MINEUR] q4** : l'option a reproduit le dessin fautif décrit par l'énoncé (« عند الطرفين المتقابلين فقط ») : elle s'élimine à vue. Correctif possible : supprimer l'option a (3 options restent, l'explication reste juste car elle cite l'erreur de l'élève, pas l'option). Le fait (chaque morceau a deux pôles) est celui de `07/02-boss#8` : la forme visuelle seule est neuve (carte), accepté.

Après correctifs : 6 questions (q1, q2, q4, q5, q6, q8) ; étage d2 inchangé.

### 07/07 — `07-exams-2009-2025-types-de-poles-aiguille-formes-et-matieres.json` (d3 boss 120/30, 12 q) — fidélité OK (2009 ✓, 2021 ✓ lettres et relations, 2022 ✓ erreur de l'élève, 2023 ✓, 2025 ✓ ; anneau → cylindre signalé dans l'explication)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c (يتنافر) | c | réserve | doublon de `07/quiz#3` et `07/03-revision#4`, et même règle que q7 |
| 2 | 1→اسطوانيّ, 2→إبرة, 3→قضيبيّ, 4→نضويّ | idem | réserve | doublon de `07/01-pratique#7` (même appariement, mêmes quatre noms) |
| 3 | a | a | ERREUR (fuite) | q4 (toutes ses options « لها قطبان ») et q11 (« لماذا نقول إنّ لإبرة البوصلة قطبين ») donnent la clé |
| 4 | d | d | OK | |
| 5 | b | b | ERREUR (fuite + doublon) | l'énoncé « فانجذبت مسامير الحديد وحدها » donne la clé de q9 ; doublon de `07/05-entrainement#1`, `07/02-boss#1` |
| 6 | d | d | OK (mineur) | option a = l'énoncé fautif lui-même, inévitable dans le plan 2×2 (votes neutres) : accepté |
| 7 | a | a | OK | plan 2×2 correct : b (deux erreurs) muette, c et d étiquetées |
| 8 | c (ش) | c | OK | |
| 9 | b | b | OK (mineur) | option a = le dessin fautif de l'élève |
| 10 | d | d | ERREUR (fuite) | son explication (« ل جنوبيّ … ن جنوبيّ ») donne la clé du multi q12 (même figure, émis avant) |
| 11 | b | b | OK | |
| 12 | b, d, e | b, d, e | OK | ن et ل jnoubiyy, sommet de 3 jnoubiyy ; م et sommet de 4 chamaliyy |

**Défauts**
- **[MAJEUR] q3 — fuite.** Les quatre options de q4 portent « لها قطبان » et l'énoncé de q11 pose « لإبرة البوصلة قطبين لا قطبًا واحدًا » : la clé de q3 (« أنّ للإبرة قطبًا واحدًا ») est lue ailleurs. q4 (phrase corrigée) contient déjà la détection de l'erreur. **Correctif : supprimer q3.**
- **[MAJEUR] q5 — fuite vers q9 et doublon.** L'énoncé dit que seuls les clous de fer sont attirés (= clé de q9) ; la question re-pose `07/05-entrainement#1` (« ما الّذي يحدّد أنّ جسمًا ينجذب ؟ — مادّته ») et `07/02-boss#1`. La justification est déjà dans l'explication de q9. **Correctif : supprimer q5.**
- **[MAJEUR] q10 — fuite vers q12.** Même figure 2021 ; l'explication déduit م شماليّ, ل جنوبيّ, ن جنوبيّ : c'est le corrigé du multi q12 (q10 sort avant q12 au tri stable). q12 couvre tout le raisonnement. **Correctif : supprimer q10.**
- **[MAJEUR] q1 — doublon.** « ……… المغنطان لأنّ قطبيهما المتقابلين متماثلان » → « يتنافر » re-pose `07/quiz#3` (ج devant ج → يتنافران) et `07/03-revision#4` ; q7 applique la même règle aux deux autres situations du même sujet 2009. **Correctif : supprimer q1.**
- **[MAJEUR] q2 — doublon** de `07/01-pratique#7` (appariement des quatre mêmes formes : نضويّ، قضيبيّ، اسطوانيّ، إبرة ممغنطة) et de `07/01-pratique#3` (nommer l'aimant en U dessiné). La carte prévoyait ce QCM visuel, mais le chapitre mis à niveau l'a absorbé (E-12). **Correctif : supprimer q2.**
- **[MINEUR] q9** : l'option a (cuivre au pôle haut, fer au pôle bas) est le dessin fautif décrit dans l'énoncé. Correctif possible : supprimer l'option a et, dans l'explication, remplacer « وتوزيع المعدنين على القطبين، أو انجذاب النحاس، يخالفان ذلك. » par « وانجذاب النحاس، مع الحديد أو وحده، يخالف ذلك. »
- **Étiquette manquante (à proposer, signalé)** : q6 (écran épais qui renforcerait l'attraction, piège C02#14) n'a aucun distracteur étiqueté ; aucun id du registre ne décrit l'erreur — `eveil.aim.attire-seulement-au-contact` en est l'inverse. Id à proposer par l'auteur (p. ex. `eveil.aim.distance-ou-ecran-renforce`) ; pas de défaut bloquant.

Après correctifs : 7 questions (q4, q6, q7, q8, q9, q11, q12), toutes d2–d3 : l'étage d3 reste porté par q9, q11, q12 (lignes C06#14 d3). Si le pilote veut garder 2025 (formes) et 2009 (situation 3), il faut une forme qui ne recoupe pas `07/01-pratique#7` / `07/quiz#3` : aucune proposée ici.

### 07/08 — `08-exams-2019-2026-directions-le-nord-nest-pas-en-haut.json` (d3 boss 120/30, 11 q)

Rotations refaites : 2026 (ش à droite) → ق en bas, غ en haut, ج à gauche ; 2024 (l'école, au sud du centre, à droite) → ق en haut, غ en bas ; 2022 et 2019 (ش à gauche) → ق en haut, ج à droite, غ en bas.

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | ج (flèche 2 vers la gauche) | a ج | OK / mineur | « (السند نفسه) » et « مسير الأب والابن » : le sujet 2026 parle de منير seul |
| 2 | flèche vers la droite | b | OK | |
| 3 | غ (dépôt sous la forêt) | d غ | OK | |
| 4 | **الشلّال (sujet officiel)** | b الجبل | **ERREUR CRITIQUE (infidélité de donnée)** | figure refaite fausse : la montagne et la cascade ont été déplacées |
| 5 | ج غ (flèche 1 en haut à gauche) | c | OK | |
| 6 | ش ق (flèche 3 en bas à droite) | d | OK | |
| 7 | ش à gauche | b | OK (mineur) | option c = la boussole 1 fautive (nord en haut) |
| 8 | ج ق ثمّ ج غ | a | OK | |
| 9 | 1→ش ق, 2→ق, 3→غ, 4→ج غ | idem | OK | |
| 10 | flèche 6 (ش غ) | c | ERREUR (fuite + doublon de figure) | même rose que q9 ; son explication donne la clé l1 de q9 ; numérotation des flèches différente de q9 |
| 11 | ق ثمّ ش ق | d | OK | |

**Défauts**
- **[CRITIQUE] q4 (et figure partagée avec q11) — infidélité de donnée.** PDF 2019 p.1 (zoom 200 dpi) : la montagne (جبل) est À DROITE, sur l'axe horizontal, et la cascade (شلّال) EN BAS À DROITE, en diagonale. Nord à gauche → droite = sud, bas = ouest : la montagne est au **sud**, la cascade au **sud-ouest** — la réponse officielle de « يقع ……… في الجنوب الغربيّ » est **الشلّال**. La figure de la mission met la montagne en bas à droite (sud-ouest) et la cascade à gauche (= nord), deux positions absentes du sujet : la clé « الجبل » contredit la session citée. **Correctif exact (q4 et q11, même SVG) :** dans le SVG, remplacer
  - `<polygon points="250,190 224,232 276,232"` → `<polygon points="290,108 264,150 316,150"`
  - `<text x="290" y="226" font-size` → `<text x="290" y="172" font-size`
  - `<path d="M62 118 V152 M72 118 V152 M82 118 V152"` → `<path d="M240 198 V232 M250 198 V232 M260 198 V232"`
  - `<text x="72" y="175" font-size` → `<text x="280" y="222" font-size`

  (rendu vérifié à 360 px : montagne sur l'axe à droite, cascade en diagonale en bas à droite, aucune étiquette chevauchée ; fichier `…/scratchpad/aud-M4/fix2019.min.svg`). Puis q4 : `correctOption` **d** (الشلّال) ; explication de remplacement : « الشمال جهة اليسار، فالجنوب جهة اليمين؛ ومن يواجه الشمال يكون الشرق عن يمينه، أي نحو أعلى الصفحة، والغرب عن يساره، أي نحو أسفلها. والجنوب الغربيّ بين الجنوب (اليمين) والغرب (الأسفل)، أي في أسفل اليمين، وهناك الشلّال. أمّا الجبل فعلى المحور الأفقيّ جهة اليمين، فهو في الجنوب لا في الجنوب الغربيّ. والخطأ الشائع أن نقرأ الأسفل جنوبًا لأنّ الشمال يكون في الأعلى عادةً. » q11 est inchangée (forêt en haut = ق, campement en haut à gauche = ش ق : positions conformes au PDF).
- **[MAJEUR] q4 — fuite vers q11.** L'explication actuelle dit « الغابة فهي شرق الفريق، والمخيّم في الشمال الشرقيّ » : c'est la clé de q11 (émise après). L'explication de remplacement ci-dessus ne nomme ni la forêt ni le campement.
- **[MAJEUR] q10 — même rose que q9 (sujet 2022), fuite et numérotation contradictoire.** L'explication « أمّا السهم 1 في أعلى اليسار فهو … ش ق » donne la paire l1 de q9 ; q9 et q10 portent deux numérotations différentes des mêmes flèches (le « 3 » est en bas dans q9, en haut à droite dans q10). **Correctif : supprimer q10** (q9 couvre le geste « compléter la rose à huit flèches »).
- **[MINEUR] q1** — retirer la référence et rétablir le personnage du sujet : énoncé de remplacement « مناظرة 2026: «إذا كان منير قد انطلق من النّصب التّذكاري ووصل إلى الفندق، حدّد الاتّجاهات المشار إليها بالأسهم.» في البوصلة المرسومة الشمال (ش) جهة اليمين من الصفحة. في أيّ جهة يسير السهم 2، من القلعة نحو العين الساخنة؟ » + la même figure.
- **[MINEUR] q7** : l'option c (nord en haut) est la boussole 1 que l'énoncé déclare fausse ; supprimable (3 options).
- **[MINEUR, général]** les explications de q1/q5/q6 (2026) et q3/q7/q8 (2024) redonnent chacune le repère tourné complet (« الشرق … نحو أسفل الصفحة، والغرب … نحو أعلى الصفحة ») qui résout les questions sœurs ; c'est la méthode enseignée (cours § 🗺️), accepté, mais trois questions par figure suffisent.
- **Étiquettes** : aucune — le registre n'a pas d'id « nord lu en haut de la page » (pièges C01#13, C03#10, C05#10, C08#4). Id à proposer (p. ex. `eveil.aim.nord-toujours-en-haut`) ; il servirait les distracteurs ش غ (q5), ج ق (q6), ش ثمّ ش غ (q11), ش ق ثمّ ج ق (q8), a (q2).

Après correctifs : 10 questions.

### 07/09 — `09-exams-2010-2026-boussole-en-voiture-et-boussole-artisanale.json` (d3 boss 120/30, 12 q)

Rotation 2021 vérifiée au zoom 400 dpi : moitié noire de l'aiguille vers le bas, « الشّمال » sous le cercle → nord en bas, est à gauche, ouest à droite. 2010 : nord en haut, est à droite.

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | ش غ | c | OK | |
| 2 | ج غ | a | OK / mineur | « (الرسم نفسه) » |
| 3 | غ | a | OK | |
| 4 | بخار الماء | d | OK | notion du `01` (condensation), item `01+07` de la carte |
| 5 | **ش ق ثمّ ش (sujet officiel)** | b ش ق ثمّ ش غ | **ERREUR CRITIQUE (infidélité)** | figure 2010 refaite en losange symétrique : la flèche A→B est VERTICALE dans le sujet |
| 6 | d | d | OK | plan 2×2 (c = énoncé d'origine, deux erreurs, muette) |
| 7 | ج ق | c | OK | |
| 8 | b, d, e | b, d, e | ERREUR (doublon) | même fait que `07/03-revision#6` (boussole dans la voiture : les pièces de fer dévient l'aiguille) |
| 9 | **ج غ ثمّ ج (sujet officiel)** | b ج غ ثمّ ج ق | **ERREUR CRITIQUE (infidélité)** | la flèche forêt → départ est VERTICALE dans le sujet |
| 10 | b, d, a, c | idem | OK | méthode du cours (§ 🗺️), ordre unique |
| 11 | a | a | OK | |
| 12 | c | c | OK | |

**Défauts**
- **[CRITIQUE] q5 et q9 — infidélité de donnée (figure 2010).** PDF 2010 p.1 : « النّقطة ب » est exactement au-dessus de « النّقطة أ » (flèche A→B verticale, vers le nord) et « الغابة » exactement au-dessus de « نقطة الانطلاق » (flèche forêt→départ verticale, vers le sud). Directions officielles : 1 = ش ق, 2 = **ش**, 3 = ج غ, 4 = **ج**. La mission dessine un losange (2 = ش غ, 4 = ج ق) : les clés de q5 et q9 ne sont pas celles du sujet cité. **Correctif exact :** remplacer le SVG de q5 et q9 par le contenu de `/tmp/claude-0/-home-user/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/aud-M4/fix2010.min.svg` (même `viewBox`, mêmes axes, mêmes styles ; départ (120,200), أ (200,120), ب (200,40), forêt (120,120) ; rendu vérifié à 360 px RTL) ; puis
  - q5 : options a « ش غ ثمّ ش », b « ش ق ثمّ ش » (clé), c « ش ق ثمّ ش ق », d « ش غ ثمّ ش ق » (plan 2×2 : votes neutres, d à deux erreurs muette) ; explication : « في هذا الرسم الشمال في الأعلى والشرق عن اليمين. السهم 1 يصعد مائلًا نحو اليمين، أي بين الشمال والشرق: الشمال الشرقيّ ش ق. والسهم 2 يصعد مستقيمًا نحو الأعلى، فهو نحو الشمال ش، لا نحو جهة وسيطة. والخطأ الشائع أن نخلط بين الشرق والغرب، أو أن نسمّي كلّ سهم جهةً وسيطة. »
  - q9 : options a « ج غ ثمّ ج » (clé), b « ج ق ثمّ ج », c « ج غ ثمّ ج غ », d « ج ق ثمّ ج غ » ; énoncé sans renvoi : « مناظرة 2010: في الرسم الشمال في الأعلى والشرق عن اليمين. يعود الفريق من النقطة ب إلى الغابة (السهم 3) ثمّ منها إلى نقطة الانطلاق (السهم 4). ما اتّجاها السهمين 3 و4 على الترتيب؟ » ; explication : « الشمال في الأعلى والشرق عن اليمين. السهم 3 ينزل مائلًا نحو اليسار، أي بين الجنوب والغرب: الجنوب الغربيّ ج غ. والسهم 4 ينزل مستقيمًا نحو الأسفل، فهو نحو الجنوب ج. والخطأ الشائع أن نخلط بين الشرق والغرب، أو أن نسمّي كلّ سهم جهةً وسيطة. » (clé a, non la plus longue).
- **[MAJEUR] q8 — doublon** de `07/03-revision#6` (« أراد سليم أن يستعمل البوصلة داخل السيّارة … الأجزاء الحديديّة للسيّارة تحرف الإبرة »). **Correctif : supprimer q8.**
- **[MINEUR] q2** : retirer « (الرسم نفسه) » → « مناظرة 2021: من الغابة إلى المتحف تسير العائلة وفق السهم 2، والشمال (ش) في البوصلة المرسومة نحو أسفل الصفحة. في أيّ جهة تسير؟ ».
- **[MINEUR] q4** : « في يوم بارد » n'est pas dans l'énoncé (l'explication l'ajoute) ; le sujet parle de brouillard matinal : remplacer « في يوم بارد يتكوّن بخار الماء من زفير ركّاب السيّارة » par « في صباح بارد كثير الضباب يخرج بخار الماء مع زفير ركّاب السيّارة ».
- **Étiquettes** : comme 07/08, aucun id « nord en haut » ni « est/ouest inversés » au registre (pièges C06#4, C17#1a) : à proposer. `eveil.gaz.test-mal-associe` sur « ثاني أكسيد الكربون » (q4) : exact.

Après correctifs : 11 questions.

## Chapitre `11-effets-courant-electrique`

Croisement E-12 refait contre le `11` mis à niveau : le cours a désormais une section 🔔 « الجرس الكهربائيّ » (E-7b), le quiz porte `quiz#1` (dارة مغلقة), `quiz#2` (حرارة), `quiz#4` (أكسيجين عند المصعد) ; `01-pratique#7` apparie déjà observation ↔ effet ; `02-boss#2` (محلال، ملح، قاطعة مفتوحة), `03-revision#2` (احمرار السلك = حراريّ), `03-revision#4` (محلول السكّر), `03-revision#6` (montage du cuivrage), `05-entrainement#2` (cuivrage = كيميائيّ), `05-entrainement#4` (قبس → أكسيجين، +).

### 11/06 — `06-exams-2008-2018-quel-effet-du-courant.json` (d2 practice 75/15, 7 q ; la carte en prévoyait 8) — fidélité OK (2008, 2012, 2013, 2017, 2018 : phrases officielles exactes)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | هاتف→مغناطيسيّ, حلكبة→كيميائيّ, كيّ→حراريّ | idem | OK | |
| 2 | مغناطيسيّ | c | ERREUR (doublon interne) | même fait que q1 (l1), q3 et l'option c de q6 : la sonnerie = effet magnétique, quatre fois dans 7 questions |
| 3 | a | a | OK | |
| 4 | d | d | ERREUR (doublon) | re-pose `11/03-revision#2` (« احمرار سلك المصباح وسخونته » = حراريّ) et `11/quiz#2` |
| 5 | b, d, e | b, d, e | ERREUR (doublon) | re-pose `11/quiz#1` et `11/02-boss#1` (la lampe ne s'allume qu'en circuit fermé) |
| 6 | b, d | b, d | ERREUR (fuite) | son explication (« البرادة ليست مغنطًا فتنجذب ولا تتنافر ») et son option a donnent la clé de q7 |
| 7 | b | b | ERREUR (doublon interne) | juge la même phrase que l'option a de q6 |

**Défauts**
- **[MAJEUR] q2 — doublon interne.** « رنين الهاتف → التأثير المغناطيسيّ » est déjà la paire l1 de q1 (2017), la clé de q3 (2008) et l'option c de q6 (2012). La session 2018 est servie par m039 (11/08 q6). **Correctif : supprimer q2.**
- **[MAJEUR] q7 — doublon de l'option a de q6, et fuite de q6 vers q7.** **Correctif : supprimer q7** (q6 couvre les trois phrases 2012).
- **[MAJEUR] q4 — doublon** de `11/03-revision#2`. **[MAJEUR] q5 — doublon** de `11/quiz#1` / `11/02-boss#1`. La seule phrase 2013 non servie par le patron est la troisième (« يختلف التأثير الحراريّ للتيّار الكهربائيّ باختلاف مادّة السلك الناقل ») ; le cours du `11` ne l'enseigne pas (§ 🔥 : « مرور التيّار في ناقل ينتج حرارة », rien sur la matière du fil) : elle ne peut pas devenir une clé. **Correctif : supprimer q4 et q5.**
- **[MINEUR] q4 option c** (« نعم، فكلّ آثار التيّار تُحمرّ بها الأسلاك ») est un distracteur de remplissage — sans objet si q4 est coupée.

Après correctifs : 3 questions (q1, q3, q6) : la mission devient trop mince pour exister seule. **Recommandation : la fusionner** avec ce qui reste de 11/07 (dépôt) ou la couper, l'essentiel du gisement 2008–2018 « quel effet » étant absorbé par la mise à niveau du `11` (E-1 : ordre de coupe). À trancher par le pilote.

### 11/07 — `07-exams-2012-2016-depot-metallique-la-cuillere-et-la-plaque.json` (d3 boss 120/30, 8 q ; la carte en prévoyait 9) — fidélité OK (2016 nitrate d'argent → sulfate de cuivre et 2015 sucre → sel, E-5, signalés ; montage inversé de 2016 conforme)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | ERREUR (doublon) | = `11/05-entrainement#2` (« أيّ استعمال يعتمد على التأثير الكيميائيّ ؟ — طلاء ملعقة بالنحاس ») et = q2, q3 |
| 2 | a | a | ERREUR (doublon interne) | troisième habit de « dépôt = effet chimique » |
| 3 | d | d | OK | garde la forme « correction d'énoncé » (ligne C12#3b d3) |
| 4 | b | b | OK / mineur | la cathode = l'électrode reliée au − : définition du cours |
| 5 | b | b | OK | figure : plaque au −, cuillère au + ✓ |
| 6 | d | d | ERREUR (fuite) | la clé de q5 (« الملعقة موصولة بالقطب الموجب والصفيحة بالسالب، والصحيح عكس ذلك ») est le dessin corrigé de q6 ; et q6 re-pose `11/03-revision#6` |
| 7 | a | a | OK / mineur | option d (« قضيبان من الخشب أو البلاستيك ») de remplissage |
| 8 | c | c | ERREUR (vote) | la clé se reconstruit par vote terme à terme |

**Défauts**
- **[MAJEUR] q1 et q2 — doublons** (q1 = `11/05-entrainement#2` ; q1, q2, q3 posent trois fois « le dépôt vient de l'effet chimique »). **Correctif : supprimer q1 et q2** ; garder q3 (2015, d3). La note E-5 sur le nitrate d'argent reste portée par q5.
- **[MAJEUR] q6 — fuite depuis q5 et doublon de `11/03-revision#6`.** **Correctif : supprimer q6.**
- **[MAJEUR] q8 — vote terme à terme.** Liquide : « ملح » 2 fois (c, d), « سكّر » 1, « ماء نقيّ » 1 ; gaz : ordre juste 3 fois sur 4 → le vote rend la clé c. **Correctif exact (plan 2×2)** : remplacer l'option b par « محلول السكّر؛ الغاز الأكبر حجمًا، وهو الأكسيجين، فوق المهبط (−) والهيدروجين فوق المصعد (+) » **sans étiquette** (deux erreurs, muette). Votes : ملح 2 / سكّر 2 ; ordre juste 2 / inversé 2. La clé c et l'option d ont la même longueur (permutation de deux mots) : la clé n'est pas strictement la plus longue. L'explication reste juste ; y remplacer « ولا نستعمل السكّر ولا الماء النقيّ » par « ولا نستعمل محلول السكّر العازل ».
- **[MINEUR] q7 option d** : distracteur de remplissage (des électrodes en bois : personne ne le pense). Remplacement proposé : « ينبغي أن يكون القضيبان من النحاس لا من القرافيت » (erreur plausible : croire que l'électrode doit être en métal).
- **[MINEUR] q5** : la note « (ورد في المناظرة محلول نيترات الفضّة …) » est placée dans l'énoncé, après la figure ; sa place est l'explication (comme en q1).
- **[MINEUR] figures q5/q6** : les légendes du manuel (محلال، مصعد، مهبط) annoncées par la carte manquent ; sans effet sur la clé.

Après correctifs : 5 questions (q3, q4, q5, q7, q8), d3.

### 11/08 — `08-exams-2009-2018-electrolyse-de-leau-gaz-et-electrodes.json` (d3 boss 120/30, 7 q) — fidélité OK (2013 : tube ② plus rempli, « ماء البحر » → محلول ملح الطعام signalé ; 2009 liste de mots exacte ; 2018 محلول الصّودا)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | OK | énoncé juste, aucune erreur inventée ✓ |
| 2 | a | a | OK / mineur | options c (« غير موصول بأيّ قطب ») et d (« بالقطبين معًا ») de remplissage |
| 3 | b | b | OK | |
| 4 | d | d | ERREUR (doublon) | même fait que q1 et q5, et que `11/02-boss#4` (tube le plus rempli → pôle −) |
| 5 | b | b | OK | |
| 6 | b, d, e | b, d, e | OK | volume comparé, jamais 2 : 1 (E-8) ✓ |
| 7 | d | d | ERREUR (fuite + doublon) | l'explication de q6 (« فرقعة » ↔ hydrogène ↔ pôle −, « إنعاش العود » ↔ oxygène) résout q7 ; q7 re-pose `11/05-entrainement#4` |

**Défauts**
- **[MAJEUR] q4** — doublon de q1/q5 et de `11/02-boss#4`. **Correctif : supprimer q4.**
- **[MAJEUR] q7** — fuite depuis q6 et doublon de `11/05-entrainement#4` (« قبس اتّقد → الأكسيجين، والقطب الموجب »). **Correctif : supprimer q7.**
- **[MINEUR] q2** : options c et d de remplissage. Remplacements proposés : c « خطأ: المصعد هو القضيب الذي يتصاعد عنده الهيدروجين » (étiquette `eveil.elec.gaz-electrolyse-inverses`), d « صحيحة: المصعد هو القضيب الذي يتجمّع فوقه الغاز الأكبر حجمًا » (même étiquette) ; la clé a reste la plus courte.

Après correctifs : 5 questions (q1, q2, q3, q5, q6), d3.

### 11/09 — `09-devoir-circuit-en-panne-et-electroaimants.json` (d3 boss 120/30, 8 q, devoir)

**Salle blanche** : `npm run -s content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/eveil-scientifique-6eme content/eveil-scientifique-6eme/11-effets-courant-electrique/exercices/09-devoir-circuit-en-panne-et-electroaimants.json` lancé par l'auditeur : 8 textes contrôlés, **0 plage ≥ 8 mots**, 0 plage ≥ 6 mots, 0 exercice source à ≥ 2 données communes. ✓ (snapshots non lus.)

| q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | مدفأة→حراريّ, نحاس→ترسّب, دبابيس→مغناطيسيّ, فقاقيع→غاز | idem | ERREUR (doublon) | = `11/01-pratique#7` (même geste ; « سلك يحمرّ » et « فقاقيع غاز حول قضيبين » y sont déjà) |
| 2 | 4, 1, 3, 2 | d, c, a, b | **ERREUR CRITIQUE (figure contraire à l'énoncé)** | « لها المسمار نفسه » mais les clous dessinés ont quatre longueurs, croissant avec les spires : ranger par la taille du clou donne la même clé |
| 3 | a | a | ERREUR (doublon) | = `11/02-boss#2` (محلال، ملح الطعام، مصباح مطفأ → القاطعة مفتوحة) |
| 4 | b | b | OK | |
| 5 | c | c | OK / mineur | explication trop absolue sur le clou |
| 6 | d | d | OK / réserve | le fait (sucre isolant) est `11/03-revision#4`, mais le geste « ne pas incriminer un composant sain » est neuf (D07#10) |
| 7 | b | b | OK | |
| 8 | d | d | OK / mineur | l'énoncé (« القاطعة مغلقة وكلّ الأسلاك موصولة ») est la clé de q4 |

**Défauts**
- **[CRITIQUE] q2 — figure qui contredit l'énoncé.** Clous de 70, 110, 100 et 60 unités pour 4, 8, 6 et 2 spires : l'énoncé dit « لها المسمار نفسه » et la longueur du clou suit l'ordre des spires, si bien que le leurre « la taille du clou » (piège D07#8) donne la clé. **Correctif exact** (même SVG, clous tous de 110 ; rendu vérifié, `…/scratchpad/aud-M4/fixspires.min.svg`) :
  - `<rect x="30" y="18" width="70" height="10"` → `<rect x="30" y="18" width="110" height="10"` ; `<polygon points="100,18 110,23 100,28"` → `<polygon points="140,18 150,23 140,28"`
  - `<rect x="30" y="126" width="100" height="10"` → `<rect x="30" y="126" width="110" height="10"` ; `<polygon points="130,126 140,131 130,136"` → `<polygon points="140,126 150,131 140,136"`
  - `<rect x="200" y="126" width="60" height="10"` → `<rect x="200" y="126" width="110" height="10"` ; `<polygon points="260,126 270,131 260,136"` → `<polygon points="310,126 320,131 310,136"`
- **[MAJEUR] q1 — doublon** de `11/01-pratique#7`. **Correctif : supprimer q1** (ou, si le pilote veut garder D07#6, ne garder que les deux observations neuves — dépôt et clou — dans un QCM ; non proposé ici).
- **[MAJEUR] q3 — doublon** de `11/02-boss#2`. **Correctif : supprimer q3** (q6 et q7 portent le geste D07#10).
- **[MINEUR] q5** : « وطول المسمار ليس سبب القوّة » est trop absolu (la taille du noyau compte aussi) ; remplacer par « وليس طول المسمار هو ما يفرّق بينهما هنا: الوشيعة أ أقصر مسمارًا وأكثر لفّات، وهي الأقوى ».
- **[MINEUR, accepté] q8** : l'énoncé (« القاطعة مغلقة وكلّ الأسلاك موصولة ») suppose fait le contrôle que q4 demande ; c'est la prémisse nécessaire de la question suivante du diagnostic, et q4 reste résoluble sans elle : pas de correctif.
- Titre « 📝 ⚔️ زعيم الفرض ⭐⭐⭐: … » : conforme (📝, sans clé). V3 respectée (spires seulement, piles égales).

Après correctifs : 6 questions (q2, q4, q5, q6, q7, q8), d3.

## Chapitre `08-poids`

### 08/06 — `06-exams-2010-2018-chute-poids-et-masse.json` (d2 practice 75/15, 10 q) — **E-1 : à couper**

Fidélité OK (2010, 2015, 2016, 2018 exacts ; 1/6 non donné, V1 ✓ ; C11#6a écartée ✓). Toutes les clés sont justes (re-résolues : q1 d, q2 b, q3 b, q4 b·d·e, q5 c, q6 a, q7 b·d, q8 d, q9 a, q10 c). Mais **chaque question re-pose une question du patron mis à niveau** :

| q | geste | déjà posé par |
|---|---|---|
| 1 | dessin de la chute verticale du fruit | `08/02-boss#8` (même fruit, même erreur oblique), `08/04-defi#3`, `08/03-revision#5`, `08/01-pratique#3` |
| 2 | منحى السقوط = شاقوليّ | `08/quiz#2`, `08/02-boss#1` |
| 3 | nom de la force = الوزن | `08/quiz#1` (énoncé presque identique : « القوّة الّتي تسلّطها الأرض على الأجسام الموجودة بجوارها ») |
| 4, 5 | erreurs de Maryam (oblique, intérieur, masse) | `08/05-entrainement#7` (source de la masse / du poids), `08/02-boss#8` ; et q5 nomme les trois cases d'erreur (« المنحى، التأثير، اسم التأثير ») : elle donne la clé du multi q4 |
| 6 | le poids vient de la Terre, pas de la matière | `08/05-entrainement#7` (même distinction, mêmes mots) |
| 7 | tout corps a un poids ; newton | `08/05-entrainement#4` (la plume a un poids), `08/05-entrainement#2`, `08/quiz#3` |
| 8 | altitude : poids ↓, masse = | `08/04-defi#2` (fusée : masse 100 kg, poids ↓), `08/03-revision#3` |
| 9 | astronaute sur la Lune | `08/02-boss#5` (même scène, même clé) |
| 10 | balance vs dynamomètre sur la Lune | `08/04-defi#7`, `08/04-defi#1`, `08/05-entrainement#5` |

**[MAJEUR] — réponse à la question E-1 : oui, m041 fait doublon au point de devoir être coupée.** La mise à niveau du `08` a absorbé tous ses gestes ; seule la forme d'examen (« corriger la phrase de Maryam ») est neuve, et elle ne porte que des faits déjà interrogés dix fois. Il n'y a pas de réécriture sauvable sans redemander. **Correctif : supprimer le fichier** et retirer de `08/chapter.json` la source « Sujets officiels … » si aucune autre mission du `08` ne la justifie ; consigner C09#3, C17#3a, C17#3b, C12#3a, C11#6b comme « absorbées par le patron » dans le registre du gisement.

Défaut accessoire (si le pilote la garde malgré tout) : **[MAJEUR] q5 → q4** fuite (l'énoncé de q5 désigne les trois mots fautifs que q4 demande de trouver) ; supprimer q5.

## Gates (lancés par l'auditeur depuis `/home/user/eng-deliver`, lien `content` → `/home/user/wt-ev6/content`)

`content:check` ✓ (121 sujets) · `content:qa -- --subject eveil-scientifique-6eme` ✓ (aucune clé suspecte) · `content:figures:check` ✓ · `content:tranche -- --subject eveil-scientifique-6eme --chapters 07-aimants-boussole,11-effets-courant-electrique,08-poids --fresh --strict-longest --strict-lessons` ✓ (clé strictement la plus longue 0/107 ; positions 27/27/19/26 % ; patron de notion 0 en recul ; 6 paires proches, toutes sur des questions que ce rapport coupe ou qui partagent une figure : 07/08 #3↔#8, #4↔#11, #7↔#8 ; 07/09 #1↔#2, #2↔#7 ; 11/08 #1↔#2) · `content:gisement:controle` (devoir m040) ✓ 0 plage ≥ 8 mots. Notation : aucun chiffre indien, aucun LaTeX ; les seules séquences « chiffre espace 3 chiffres » sont des coordonnées SVG. `sources[]` présent dans les trois `chapter.json` (examens ×3, devoir au `11`). Aucun gate ne voit les défauts critiques ci-dessus (figures infidèles au sujet, figure contraire à l'énoncé).

## Après lecture du rapport de l'auteur (`rapports/rapport-M4.md`)

- L'auteur annonce « figures exactes à 45° » et des boussoles vérifiées : c'est précisément la source des deux infidélités 2010 et 2019 — le sujet 2010 a deux flèches **verticales** (A→B au nord, forêt→départ au sud) et le sujet 2019 place la montagne **à droite** et la cascade **en bas à droite** (la transcription le dit aussi : « جبل (à droite), شلّال (en bas) ») ; la régularisation en losange a changé trois clés (07/08 q4, 07/09 q5, q9).
- « Options à deux erreurs muettes » : contredit par 07/06 q5 (option c).
- L'auteur assume des recoupements avec le patron (« les faits partagés sont redemandés sous une autre forme ») ; la consigne d'audit (point 4) les interdit : d'où les coupes proposées (07/03-revision#6 n'est pas « remplacé » par le multi 07/09 q8, il est redemandé).
- Ids d'étiquettes proposés par l'auteur (`eveil.aim.nord-lu-en-haut-de-la-page`, `eveil.aim.un-seul-pole`, `eveil.aim.support-magnetique-ignore`, `eveil.elec.electrode-pole-confondus`, `eveil.elec.lampe-accusee-a-tort`) : pertinents, je les appuie, et j'ajoute un id pour l'écran épais (07/07 q6, C02#14). `eveil.aim.est-ouest-inverses` cité par l'auteur « déjà proposé (B4) » n'existe pas dans `content/misconceptions.json` : il reste à créer.
- Doute de l'auteur « lettre ق pour l'est » : conforme au cours du `07` (§ 🌹), aucune objection.

## Synthèse

| mission | fichier | q. | ma re-résolution : clés fausses | critiques | majeurs | mineurs | après correctifs |
|---|---|---:|---:|---:|---:|---:|---:|
| m033 | 07/06 | 9 | 0 | 0 | 4 | 2 | 6 q |
| m034 | 07/07 | 12 | 0 | 0 | 5 | 1 (+1 id) | 7 q |
| m035 | 07/08 | 11 | 1 (q4, contre le sujet) | 1 | 2 | 3 | 10 q |
| m036 | 07/09 | 12 | 2 (q5, q9, contre le sujet) | 1 (2 q) | 1 | 2 | 11 q |
| m037 | 11/06 | 7 | 0 | 0 | 4 | 1 | 3 q → fusion ou coupe |
| m038 | 11/07 | 8 | 0 | 0 | 3 | 3 | 5 q |
| m039 | 11/08 | 7 | 0 | 0 | 2 | 1 | 5 q |
| m040 | 11/09 (devoir) | 8 | 0 | 1 | 2 | 2 | 6 q |
| m041 | 08/06 | 10 | 0 | 0 | 1 (mission entière) | — | **coupée (E-1)** |
| **total** | | **84** | **3** (clés justes sur la figure de la mission, fausses contre la session citée) | **3 défauts / 4 q** | **24** | **15** | 53 q + 3 à trancher |

84 questions re-résolues à l'aveugle (dont 17 de directions sur boussole ou rose, rotation du repère refaite pour chacune). Aucune clé n'est fausse **par rapport à la figure que la mission montre** ; trois clés le sont **par rapport au sujet officiel cité** (figures 2019 et 2010 mal refaites), et une figure (m040 q2) contredit son énoncé. La science est juste partout (aucune explication fausse ; une formulation trop absolue, m040 q5). Rendu RTL 360 px : toutes les figures lisibles, aucune légende chevauchée, aucune inversion bidi observée.

**Réponse à la question E-1 (m041)** : oui — chacune des 10 questions re-pose un item du `08` mis à niveau (tableau ci-dessus) ; la mission est à couper.

**Verdict : À CORRIGER.** Bloquants avant tout merge : les trois figures (07/08 q4·q11 SVG 2019 ; 07/09 q5·q9 SVG 2010 ; 11/09 q2 clous égaux) avec les clés et explications données plus haut, puis les fuites (07/06 q7, q9 ; 07/07 q3, q5, q10 ; 07/08 q4 explication, q10 ; 11/06 q7 ; 11/07 q6 ; 11/08 q7) et les doublons du patron (07/06 q3 ; 07/07 q1, q2 ; 07/09 q8 ; 11/06 q2, q4, q5 ; 11/07 q1, q2 ; 11/08 q4 ; 11/09 q1, q3 ; m041 entière). Le volume baisse fortement (84 → ~53) : c'est la conséquence attendue de E-12 (le patron mis à niveau a absorbé une large part des gestes que la carte croyait neufs) ; le pilote tranche le sort de m037 (3 questions restantes).
