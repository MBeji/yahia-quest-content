# Audit indépendant — lot M4 (missions du gisement, éveil 6ᵉ : `07` 06–09, `11` 06–09, `08` 06)

> Auditeur opus, 2026-10-20. Consigne : `prompt-auditeur-missions.md`. Rapport écrit au fil de l'eau
> (une session précédente a été coupée). Aucune écriture dans `content/`, aucune écriture git.
> Rapport de l'auteur (`rapports/rapport-M4.md`) lu seulement APRÈS la re-résolution.

## État : EN COURS

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

