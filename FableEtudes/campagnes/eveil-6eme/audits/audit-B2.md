# Audit B2 — `02-respiration`, `03-sang-circulation`, `10-microbes-defense`

> Auditeur indépendant (opus), 2026-10-20. Branche `wip/eveil-6eme-un-passage` @ `33a161ec`.
> Valide pour ce commit : ré-auditer si les fichiers ont bougé.
> Ordre suivi : re-résolution à l'aveugle de toutes les questions, lecture des cours contre la fiche
> (§ 1.7, § 2 و2–و3, § 4 bis, § 6.0–6.1, § 7.14–7.16, 7.18–7.22, 7.26–7.30, 7.33–7.35), V1–V5,
> confrontation au PDF (manuel p.47–51, 62–83 ; guide p.109, 114–116, 129, 130, 135, rendus à
> 110 dpi), rendu, gates. Notes et rapport de l'auteur lus **après**.

## Bilan

| chapitre | questions re-résolues | critique | majeur | mineur |
| --- | --: | --: | --: | --: |
| 02-respiration | 46 (quiz 8 + 8/7/8/7/8) | 0 | 6 | 7 |
| 03-sang-circulation | 49 (quiz 8 + 8/8/9/8/8) | 1 | 6 | 5 |
| 10-microbes-defense | 48 (quiz 8 + 9/7/9/7/8) | 0 | 5 | 7 |
| **total** | **143** | **1** | **17** | **19** |

Aucune clé fausse au sens strict. Une question a deux réponses défendables (03 `02-boss` q7). Les
autres défauts sont des questions qui redonnent un exemple résolu du cours, des distracteurs absurdes
ou qui se recouvrent, des étiquettes inexactes, une clé qui suppose un fait absent de l'énoncé, et
deux figures dont les légendes recouvrent le dessin.

**Verdict : à corriger.** Une fois les remplacements ci-dessous appliqués, les trois chapitres
sont prêts. Tous les textes de remplacement ont été vérifiés : une seule réponse défendable, aucune
fuite, et la clé n'est jamais strictement la plus longue (longueurs mesurées et données entre
crochets).

### Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets).
- `content:qa -- --subject eveil-scientifique-6eme` ✓ : aucune clé suspecte.
- `content:figures:check` ✓.
- `content:tranche … --chapters 02-respiration,03-sang-circulation,10-microbes-defense --fresh --strict-longest --strict-lessons` ✓ : clé strictement la plus longue 0/32, aucune paire proche, patron de notion sans recul (code de sortie 0).
- Scans (hors `<svg>`) : aucun chiffre arabe-indien, aucun `\d \d{3}`, aucun LaTeX. Aucune explication ne désigne une option par sa lettre ou son rang.
- Rendu : `renderLesson` / `renderSummary` via un vitest jetable, puis Chromium à 360 px. Aucun `:::` résiduel, les `verifie` sont repliés (`<details>`), aucun débordement horizontal (`scrollWidth` = 360), tableaux ≤ 328 px. Les 10 figures ont été regardées une par une : voir M-1. Fichiers jetables supprimés.

### Contrôles transverses (conformes)

- **V1** : les chiffres du ملفّ ne servent jamais de réponse attendue. Ils restent dans les encadrés « للاستزادة » (15 mouvements/min ; 5 millions, 300 000 et 7 000 ; groupes ABO ; calendrier vaccinal). « 120 jours » est une valeur du manuel (p.64), donc admise.
- **V2** : les plaquettes sont enseignées au ch. 03 (section, figure, piège, mention « تكملة لكتابك ») et exercées (quiz q1 et q6 ; `01` q7 ; `02-boss` q7 ; `04-defi` q8 ; `05` q7). **V3, V4 et V5** ne concernent pas ce lot.
- **§ 4 bis** : aucune des erreurs du manuel n'est reprise. Le CO₂ n'est pas dit « سامّ » (alors que le manuel p.51 l'écrit). L'inflammation n'est pas appelée « مناعة طبيعيّة » (manuel p.75), elle est présentée comme une manifestation de la défense. Le tableau des voies de vaccination n'associe ni le BCG au الكشط ni la polio à l'التجرّع.
- **Étiquettes** : aucune étiquette sur les `multi`, `ordering` ou `matching`. Chaque `coursePitfalls` est montré dans un `::: piege` et porté par au moins un distracteur (vérifié tag par tag pour les 18).
- **Reprises (`manuel`), confrontées au PDF** :
  - 02 `03-revision` q7 = guide p.129, T2 : mêmes trois options ✓.
  - 03 `03-revision` q7 = guide p.109 (sel sur le sang de l'Aïd) ✓ et q8 = p.135, علاج 5-أ ✓. L'intitulé du premier item est à corriger (m-9).
  - 10 `01-pratique` q9 = guide p.115, وضعيّة 3 ✓.
  - 10 `03-revision` : q7 = p.114 ✓, q8 = p.115 ✓, q9 = p.130, T6 ✓.
  - Données identiques à chaque fois.
- **Couverture** :
  - Toutes les notions des دروس 11, 14–19 sont enseignées et exercées, ainsi que les حواجز p.79, p.108 et p.132 (1–6) et les تصوّرات p.80, p.109, p.111 et p.115.
  - Seule exception : العقد اللّمفاويّة (m-13).
- **Résumés** : bijection section ↔ puce respectée (7/7, 8/8, 7/7). Aucun `verifie` dans un résumé.

---

## Défauts — critique

### C-1 · 03 `exercices/02-boss.json` q7 : deux réponses défendables

**Énoncé actuel** : « رأى تلميذ تحت المجهر نقاطًا بنفسجيّة صغيرة جدًّا بلا نواة، متجمّعة عند طرف جرح. ما هي؟ »

- **Le défaut.** L'option « جراثيم تسرّبت إلى الجرح » répond aussi à la description.
  - Les bactéries sont minuscules, sans noyau, et s'amassent au bord d'une plaie. Colorées au Gram, elles sont même violettes.
  - Le cours ne donne à l'élève aucun moyen de les écarter : le ch. 10 vient après le ch. 03, et le noyau des microbes n'est jamais enseigné.
- **Ce qui désigne la clé.** Seul « بنفسجيّة » la départage, c'est-à-dire la couleur arbitraire de la figure du cours.
- **Le décor.** Un microscope posé sur le bord d'une plaie n'est pas une situation réaliste.

**Remplacement** (clé `c` conservée, `difficulty` 3) :
- `prompt` : `عنصر من عناصر الدّم أصغر من الكريّة الحمراء، ليس خليّة كاملة بل جزء صغير من خليّة، ويتجمّع عند جرح الوعاء الدّمويّ. ما هو؟`
- options :
  - `a` `كريّة حمراء هرمة` [16]
  - `b` `كريّة بيضاء صغيرة` [17]
  - `c` `صفيحة دمويّة` [12]
  - `d` `قطرة من البلازما` [16]
  - Toutes sans étiquette : `a` portait `caracteres-globules-inverses`, qui ne correspond pas à cette option. Si le libellé proposé en M-6 est créé, `b` prendra `eveil.sang.plaquettes-prises-pour-globules-blancs`.
- `explanation` : `الصّفيحات الدّمويّة أصغر من الكريّات الحمراء، وهي أجزاء صغيرة من خلايا لا خلايا كاملة، وتتجمّع عند الجرح فتساعد الدّم على التخثّر. أمّا الكريّة الحمراء والكريّة البيضاء فخليّتان كاملتان، والكريّة البيضاء تقاوم الجراثيم ولا تسدّ الجرح، والبلازما سائل لا عنصر صغير يتجمّع.`

Vérifié. Une seule option est « جزء من خليّة ». La clé est la plus courte. La question est enseignée (définition et `propriete` de la section « الصّفيحات »). Elle ne doublonne pas `04-defi` q8 (`multi`) ni le quiz q6, qui porte sur le rôle.

---

## Défauts — majeur

### M-1 · 02 `cours.md`, figures 1 et 3 : légendes posées sur le dessin

**Le défaut.** Neuf `<text … text-anchor="start">` sont placés en arabe dans une page RTL. Le bord d'ancrage s'inverse (course-figures.md, règle 3) et le texte part vers la gauche de `x`. Les légendes recouvrent donc le dessin :
- figure 1 : « البلعوم », « الحنجرة », « القصبة الهوائيّة » et « الشّعبتان » sont écrites sur la trachée ;
- figure 3 : « دم أحمر قانٍ / إلى الأعضاء » et « دم قاتم / من الأعضاء » sont écrites sur le vaisseau, et illisibles à 360 px.

**Remplacement.** Dans `02-respiration/cours.md`, remplacer les **9** occurrences de `text-anchor="start"` par `text-anchor="end"`. Rendu vérifié à 360 px sur la copie patchée : toutes les légendes passent à droite des structures, sans sortir du `viewBox`.

**Hors lot, à signaler.** Le même attribut existe déjà sur `main` et se retrouve dans `04-nutrition` (1), `06-reproduction-florale` (4) et `08-poids` (3). Ces chapitres sont à regarder par leurs auditeurs.

### M-2 · Questions qui redonnent l'exemple résolu du cours

Les questions ci-dessous reprennent l'exemple résolu de la section, avec le même décor et la même demande. On garde la notion et on change la situation (jumeau de transfert).

**a) 02 `02-boss` q2** (exemple « بأيّ هواء انتفخت رئتا الخروف؟ »).
- `prompt` : `نفخ طبيب بيطريّ بأنبوب في رئتَي عجل مذبوح فانتفختا. بأيّ هواء انتفختا؟`
- options :
  - `a` `بهواء شهيق الطّبيب` [18] (étiquette `inspiration-expiration-confondues` conservée)
  - `c` `بهواء زفير الطّبيب` [18]
  - `b` et `d` inchangées
- `explanation` : `الطّبيب أخرج الهواء من صدره ليدفعه في الرّئتين، والهواء الخارج من الصّدر هو هواء الزّفير. الخطأ الشائع أن نقول هواء الشّهيق، والشّهيق دخول الهواء إلى رئتي الطّبيب لا خروجه منهما.`

**b) 02 `02-boss` q3** (exemple de يوسف et de l'eau de chaux).
- `prompt` : `يُخرج غوّاص هواء زفيره فقاقيعَ في الماء. جمعنا هذه الفقاقيع ومرّرناها في ماء جير صافٍ فتعكّر. ماذا نستنتج؟`
- Options et explication inchangées. Situation tirée du guide, p.84.

**c) 02 `02-boss` q7** (exemple du كانون).
- Le défaut est double :
  - la question redonne l'exemple ;
  - le piège du cours, « pas d'odeur, donc pas de danger », n'est porté par aucun distracteur. C'est un défaut d'axe 2.
- Les distracteurs actuels sont faibles : « أسكرهم » n'est pas un mot pour un élève de 11 ans, « رئاتهم » est maladroit.
- `prompt` : `في ليلة باردة، أغلق حارس كشك كلّ النّوافذ وأشعل فحمًا في موقد، ولم يشمّ رائحة غريبة. بعد ساعة أحسّ بدوار ونعاس شديد. ما التّفسير؟`
- options (clé `d`, sans étiquette tant que M-6 n'est pas fait) :
  - `a` `الفحم زاد الأكسجين في الكشك فأثقل جفنيه وأصابه بالدّوار` [55]
  - `b` `الدّفء وحده سبّب النّعاس، فلا غاز سامّ ما دام لا رائحة له` [57] (prendra `eveil.resp.monoxyde-sans-odeur-sans-danger` si le libellé est créé)
  - `c` `دخان الفحم دخل معدته مع الهواء فسبّب له الدّوار والنّعاس` [56]
  - `d` `احتراق الفحم غير التّامّ أنتج غازًا سامًّا لا رائحة له` [54]
- `explanation` : `في كشك مغلق لا يصل إلى الفحم أكسجين كافٍ، فيحترق احتراقًا غير تامّ وينتج أحادي أكسيد الكربون، وهو غاز سامّ لا رائحة له. الخطأ الشائع أن نظنّ أنّ غياب الرّائحة يعني غياب الخطر. والفحم يستهلك الأكسجين ولا يزيده، والهواء يدخل الرّئتين لا المعدة. الحلّ تهوئة المكان وإخراج الموقد منه.`

**d) 03 `04-defi` q1** (exemple « رأى أحمد تحت المجهر خليّة كبيرة، شكلها غير منتظم، وفي وسطها نواة »).
- `prompt` : `في سحبة دمويّة تحت المجهر، عدّ تلميذ مئة كريّة مستديرة بلا نواة، ولم يجد إلّا خليّة واحدة غير منتظمة الشكل لها نواة. ما هذه الخليّة، ولماذا وجد منها واحدة فقط؟`
- options (clé `a`) :
  - `a` `كريّة بيضاء، لأنّها أقلّ عددًا بكثير` [36]
  - `b` `كريّة حمراء هرمة، لأنّها تعيش 120 يومًا` [39] (`eveil.sang.caracteres-globules-inverses`)
  - `c` `كريّة بيضاء، لأنّ حجمها الكبير يخفي غيرها` [41]
  - `d` `صفيحة دمويّة، لأنّها جزء صغير من خليّة` [38]
- `explanation` : `النّواة والشكل غير المنتظم صفتان للكريّة البيضاء، والكريّات البيضاء أقلّ عددًا بكثير من الكريّات الحمراء، لذلك لا نرى منها إلّا قليلًا بين كريّات حمراء كثيرة. والكريّة الحمراء، هرمة كانت أو فتيّة، عديمة النّواة، والصّفيحة جزء صغير من خليّة لا نواة له، وحجم الكريّة البيضاء لا يفسّر قلّة عددها.`
- La question est double et toutes les options ont la même structure (nature + raison). Une seule est vraie sur les deux axes.

**e) 03 `05-entrainement` q5.**
- Elle redonne l'exemple « لماذا توقّف دم يوسف؟ » et fait doublon avec `01-pratique` q6 (même question, même clé « العلقة »).
- `prompt` : `جرح صغير في الإصبع يتوقّف سيلانه بعد دقائق، أمّا جرح كبير فيبقى ينزف. لماذا؟`
- options (clé `b`) :
  - `a` `لأنّ الدّم لا يتخثّر أبدًا خارج الجسم` [37]
  - `b` `لأنّ العلقة لا تكفي لسدّ فتحته الكبيرة` [38]
  - `c` `لأنّ الكريّات البيضاء تمنع الدّم من التخثّر` [43]
  - `d` `لأنّ البلازما لا تسدّ إلّا الجروح الصغيرة` [41]
- `explanation` : `الدّم الّذي يسيل من الجرح يتخثّر فتتكوّن علقة؛ وهي تسدّ الجرح البسيط فيتوقّف السيلان، لكنّها لا تكفي لسدّ فتحة كبيرة، فيبقى الجرح ينزف ويحتاج إلى إسعاف. والدّم يتخثّر خارج الجسم، والكريّات البيضاء تقاوم الجراثيم ولا تمنع التخثّر، والبلازما سائل لا يسدّ جرحًا.`
- Enseigné par le cas limite de la `propriete` (« … فيسدّه إن كان **بسيطًا** ») ; c'est aussi la question du manuel p.64, 6-ب.

**f) 10 `03-revision` q1** (exemple « لماذا لا يدخل ماء الحمّام إلى الجسم؟ »).
- `prompt` : `يغمس صيّاد يديه في ماء البحر ساعات، ولا يدخل الماء إلى جسمه. لماذا؟`
- option `c` → `لأنّ ماء البحر مالح فلا يتسرّب إلى الجسم` [40]. L'option actuelle « الماء يتبخّر قبل أن يلامس الجلد » serait contredite par l'énoncé.
- Clé `d` [37] ; `a` et `b` inchangées.
- `explanation` : `البشرة طبقة متقرّنة تكوّن حاجزًا، والجلد يفرز مادّة دهنيّة تحول دون تسرّب الماء. أمّا الشعيرات الخارجة من المسامّ فلا تسدّ الطريق أمام الماء، والعظام بعيدة تحت الجلد، وملوحة الماء لا دخل لها: الماء العذب لا يعبر الجلد السليم أيضًا.`

**g) 10 `02-boss` q4** (exemple de ريم).
- `prompt` : `جُرح إصبع أنس بحافّة علبة من الصفيح فغسله بالماء فقط، وفي الغد صار أحمر ومنتفخًا وساخنًا. ما التفسير الصحيح؟`
- option `a` → `الماء الّذي غسل به الجرح سبّب الانتفاخ` (accord au masculin ; étiquette conservée).
- Le reste est inchangé, explication comprise.

### M-3 · 03 `01-pratique` q3 : deux options qui disent la même chose

- **Le défaut.** `a` « الكريّات البيضاء » et `c` « البيضاء لأنّها أكبر حجمًا » affirment la même chose. Si l'une était juste, l'autre le serait aussi : l'élève les écarte toutes les deux sans rien savoir.
- **Remplacement** (3 options, clé `d`) :
  - `a` `الكريّات البيضاء، لأنّها أكبر حجمًا` [35] (`eveil.sang.globules-blancs-plus-nombreux`)
  - `b` `لهما العدد نفسه` [15]
  - `d` `الكريّات الحمراء` [16]
  - option `c` supprimée.
- Explication inchangée : elle traite déjà l'argument de la taille.

### M-4 · 03 `05-entrainement` q3 : `a` et `b` décrivent le même sang

- **Le défaut.** « الدّم الداكن الّذي يعود من أعضاء الجسم » et « الدّم الداكن الّذي يدخل الرّئتين » désignent le même sang. Le mot « الداكن », porté par deux options sur quatre, les élimine à vue.
- **Remplacement** (clé `d`) :
  - `a` `الدّم الّذي يعود من أعضاء الجسم إلى القلب` [41]
  - `b` `الدّم الّذي يضخّه القلب إلى الرّئتين` [36]
  - `c` inchangée
  - `d` `الدّم الّذي يعود من الرّئتين إلى القلب` [38]
- `explanation` : `الدّم الّذي يعود من الرّئتين إلى القلب أخذ الأكسجين في الحويصلات فصار أحمر قانيًا. أمّا الدّم العائد من الأعضاء فقد أعطاها جزءًا من أكسجينه وحمل منها ثاني أكسيد الكربون، وهو نفسه الدّم القاتم الّذي يضخّه القلب إلى الرّئتين.`

### M-5 · 03 `01-pratique` q7 : trois étiquettes fausses

- `b` « الكريّات الحمراء الكثيرة » et `c` « الكريّات البيضاء الكبيرة » portent `roles-globules-rouges-blancs-inverses`. Mais choisir l'une ou l'autre pour boucher une plaie n'inverse pas les rôles des globules rouges et blancs.
- `d` « المصل الأصفر » porte `plasma-et-serum-confondus`. Mais choisir le sérum pour boucher une plaie ne revient pas à confondre plasma et sérum.
- **Correction** : supprimer les trois `misconceptionTag`. Une fois M-6 fait, `c` prendra `eveil.sang.plaquettes-prises-pour-globules-blancs`.

### M-6 · Pièges sans étiquette au registre (axe 2) — `content/misconceptions.json`

Trois pièges des cours n'ont aucune étiquette dans le registre :
- 02, « التنفّس عمل إراديّ » : le cours le montre, et quiz q7 `a` et `04-defi` q7 `e` le portent ;
- 02, monoxyde « لا رائحة فلا خطر » : aucun distracteur ne le porte avant M-2c ;
- 03, « الصّفيحات كريّات بيضاء » : quiz q6 `b` et `02-boss` q7 `b` le portent.

Les distracteurs concernés sont muets aujourd'hui. **Ajouter** au registre (format des entrées `eveil.*` existantes) :

```json
"eveil.resp.respiration-volontaire": {
  "subject": "eveil",
  "labels": {
    "fr": "Tu crois que respirer est volontaire et qu'on peut s'arrêter quand on veut : les mouvements respiratoires sont involontaires et continuent pendant le sommeil",
    "en": "You think breathing is voluntary and can be stopped at will: breathing movements are involuntary and go on during sleep",
    "ar": "تظنّ أنّ التّنفّس عمل إراديّ نوقفه متى شئنا: الحركات التّنفّسيّة لا إراديّة وتستمرّ ونحن نيام"
  }
},
"eveil.resp.monoxyde-sans-odeur-sans-danger": {
  "subject": "eveil",
  "labels": {
    "fr": "Tu crois qu'un feu de charbon dans une pièce fermée est sans danger tant qu'on ne sent rien : le monoxyde de carbone est un gaz toxique sans odeur",
    "en": "You think burning charcoal in a closed room is safe as long as nothing smells: carbon monoxide is a toxic, odourless gas",
    "ar": "تظنّ أنّ الفحم المشتعل في غرفة مغلقة لا خطر منه ما دامت لا رائحة فيها: أحادي أكسيد الكربون غاز سامّ لا رائحة له"
  }
},
"eveil.sang.plaquettes-prises-pour-globules-blancs": {
  "subject": "eveil",
  "labels": {
    "fr": "Tu prends les plaquettes pour de petits globules blancs qui combattent les microbes : ce sont des fragments de cellules qui aident le sang à coaguler",
    "en": "You take platelets for small white blood cells that fight germs: they are cell fragments that help blood clot",
    "ar": "تظنّ أنّ الصّفيحات كريّات بيضاء صغيرة تقاوم الجراثيم: الصّفيحات أجزاء من خلايا تساعد الدّم على التخثّر"
  }
}
```

Puis :
- **Étiqueter** :
  - 02 quiz q7 `a` → `eveil.resp.respiration-volontaire` (`04-defi` q7 est un `multi` : pas d'étiquette) ;
  - 02 `02-boss` q7 `b` (version M-2c) → `eveil.resp.monoxyde-sans-odeur-sans-danger` ;
  - 03 quiz q6 `b`, 03 `02-boss` q7 `b` (version C-1) et 03 `01-pratique` q7 `c` → `eveil.sang.plaquettes-prises-pour-globules-blancs`.
- **Ajouter les trois ids** aux `coursePitfalls` du ch. 02 (les deux premiers) et du ch. 03 (le dernier).

Le piège « الشّرايين تحمل دائمًا دمًا قانيًا » du ch. 03 reste sans étiquette : aucun distracteur ne l'exécute exactement. C'est un point mineur, voir m-11.

### M-7 · 03 cours : le sel de `03-revision` q7 n'est enseigné nulle part

- **Le défaut.** `03-revision` q7 (reprise du guide p.109) demande pourquoi on met du sel sur le sang du mouton de l'Aïd. Le cours dit seulement « مادّة تمنع الدّم من أن يتخثّر » : le sel n'y apparaît jamais. La règle d'or n'est pas tenue.
- **Remplacement** dans `03-sang-circulation/cours.md` (chaîne unique) :
  - ancien : `مادّة تمنع الدّم من أن يتخثّر، وتركته`
  - nouveau : `مادّة تمنع الدّم من أن يتخثّر، كما يفعل الملح الّذي نضعه على دم خروف العيد، وتركته`

### M-8 · 10 `04-defi` q4 : la clé suppose un fait que l'énoncé ne donne pas

- **Le défaut.**
  - La clé dit « … ولم يُلقَّح ضدّ الكزاز », mais l'énoncé ne dit rien de la vaccination.
  - La clé relie l'تسمّم à l'absence de vaccin antitétanique, ce qui n'est pas une cause.
  - Ce lien vient de la liste d'hypothèses du manuel (p.80, « أفترض »), transformée en certitude.
- **Ailleurs dans la question** :
  - `b` (« نجحت كريّاته البيضاء… ») et `d` (« طريقة تطهير جرحه سليمة… ») sont contredites par l'énoncé et s'éliminent à vue ;
  - la situation reprend en plus celle de la section 7 du cours (anchor et exemple du clou).
- **Remplacement** (clé `c`, `difficulty` 3) :
  - `prompt` : `خدشت قطّة يد سلمى فغسلتها بالماء فقط. بعد أيّام انتشر الاحمرار في ذراعها وارتفعت حرارتها كثيرًا. ما التفسير الصحيح؟`
  - options :
    - `a` `لم تعصر الخدش ليخرج الدم ومعه الجراثيم` [38] (`eveil.microbes.eau-suffit-pour-la-plaie`)
    - `b` `الماء الّذي غسلت به الخدش هو سبب ما حدث` [39] (`eveil.microbes.infection-attribuee-au-dernier-geste`)
    - `c` `لم يُطهَّر الخدش فتكاثرت فيه الجراثيم وانتشرت` [45]
    - `d` `حالتها عاديّة، فالكريّات البيضاء تنتصر دائمًا على الجراثيم` [58] (`eveil.microbes.globules-blancs-gagnent-toujours`)
  - `explanation` : `الخدش منفذ في الجلد، والماء وحده لا يطهّره، فتكاثرت الجراثيم وتغلّبت على الكريّات البيضاء، فاستفحل التعفّن وانتشر الاحمرار وارتفعت الحرارة: حالة تتطلّب الطبيب فورًا. والخطأ الشائع أن نعصر الجرح لإخراج الجراثيم مع الدم، أو أن نتّهم الماء لأنّه آخر ما لمس الخدش، أو أن نظنّ أنّ الكريّات البيضاء تنتصر دائمًا.`

### M-9 · 10 `03-revision` q8 (صفوان, reprise p.115) : distracteurs absurdes et clé hors du cours

- **Les distracteurs.**
  - `b` (« … الأفضل ألّا يذهب إليه أبدًا مهما ساءت حالته ») est absurde.
  - `a` et `c` ne tiennent pas non plus face à l'énoncé.
  - Résultat : la clé se trouve par élimination.
- **La clé.** Elle exige « لم يستشر الطبيب ولم يتأكّد من تلقيحه ضدّ الكزاز ». Pour une plaie « بسيط », le cours enseigne : nettoyer, désinfecter, isoler par un pansement. Le sérum et le médecin sont réservés à la plaie profonde souillée de terre.
- **Remplacement** (énoncé inchangé, clé `d`) :
  - options :
    - `a` `الكحول الّذي طهّر به جرحه هو سبب تعكّر حالته` [44] (`eveil.microbes.infection-attribuee-au-dernier-geste`)
    - `b` `استعمل الكحول، والصواب أن يغسل الجرح بالماء فقط` [47] (`eveil.microbes.eau-suffit-pour-la-plaie`)
    - `c` `طهّر جرحه، والأفضل أن يترك الكريّات البيضاء تقاوم وحدها` [55] (`eveil.microbes.globules-blancs-gagnent-toujours`)
    - `d` `اكتفى بالتطهير وواصل العمل دون أن يعزل جرحه بضمادة` [50]
  - `explanation` : `إسعاف الجرح تنظيف ثمّ تطهير ثمّ عزل بضمادة. صفوان اكتفى بالتطهير وواصل العمل في الورشة وجرحه مكشوف، فدخلته جراثيم جديدة وتكاثرت فتعكّرت حالته، ولذلك عالجه الطبيب ولقّحه ضدّ الكزاز. والكحول مطهّر لا سبب للتعفّن، والماء وحده لا يطهّر الجرح، والكريّات البيضاء لا تنتصر دائمًا.`
- Le champ `manuel` reste juste : mêmes données, p.115.

### M-10 · 02 `04-defi` q5 : distracteurs de remplissage dans un défi d4

- « يُدفئ الهواء وينقّيه » et « يحوّل هواء الشّهيق كلّه إلى بخار ماء » n'exécutent aucune idée fausse plausible.
- **Remplacement** (clé `d` inchangée [38]) :
  - `a` `لأنّه يسدّ القصبة فلا يمرّ فيها الهواء` [38]
  - `b` `لأنّ رائحته الكريهة تلتصق بجدار القصبة` [38]
  - `c` `لأنّه يزيد الأكسجين في هواء الشّهيق` [35]
- `explanation` : `دخان التّبغ فيه موادّ سامّة أهمّها النّيكوتين، وهي تشلّ حركة الأهداب الّتي تبطّن القصبة الهوائيّة. والضّرر لا يأتي من رائحته، والدّخان لا يسدّ القصبة فالهواء يمرّ فيها، ولا يزيد الأكسجين في هواء الشّهيق.`
- Contrôle : les cils et la nicotine viennent bien du manuel, p.51 (« أضيف إلى معارفي »).

### M-11 · 02 `04-defi` q1 : doublon de fait du quiz q4

- **Le défaut.** Même question (« où se fait l'échange gazeux »), même clé, trois options communes. `03-revision` q7 pose aussi la question, mais c'est une reprise officielle : on la garde.
- **Remplacement** (clé `b`, `difficulty` 2) :
  - `prompt` : `أين يذهب ثاني أكسيد الكربون الّذي يطرحه الدّم في الحويصلات الرّئويّة؟`
  - options :
    - `a` `يبقى محبوسًا في الحويصلات الرّئويّة إلى الأبد` [45]
    - `b` `يخرج مع هواء الزّفير إلى المحيط الخارجي` [39]
    - `c` `يحمله الدّم القاني معه إلى كلّ أعضاء الجسم` [42] (`eveil.resp.sens-echanges-gazeux-inverse`)
    - `d` `يتحوّل في الرّئتين إلى أكسجين جديد` [34] (`eveil.resp.poumons-fabriquent-oxygene`)
  - `explanation` : `الدّم يطرح ثاني أكسيد الكربون في هواء الحويصلات، ثمّ يخرج هذا الهواء مع الزّفير عبر المجاري التّنفّسيّة إلى المحيط الخارجي. والدّم القاني يحمل الأكسجين إلى الأعضاء لا ثاني أكسيد الكربون، والرّئتان لا تصنعان الأكسجين، ولا يبقى الغاز محبوسًا لأنّ الهواء يتجدّد مع كلّ شهيق وزفير.`
- Enseigné : `propriete` de la section « التّبادل الغازي ».

### M-12 · 10 `01-pratique` q7 : option `c` incohérente

- **Le défaut.** « المسامّ تسدّها الشعيرات فلا يدخل منها الماء وحده أبدًا » ne se lit pas clairement : « الماء وحده » n'a pas de référent et l'énoncé parle de microbes.
- **Remplacement** : `c` → `صحيح، لكنّ الشعيرات الّتي تخرج من المسامّ تمنع بعضها` [52]. C'est l'hypothèse du manuel p.68, et la clé `b` [49] n'est pas la plus longue.

---

## Défauts — mineur

**m-1 · Étiquettes inexactes, à supprimer**
- 02 `02-boss` q6 `d` (« يحميه تنفّسه بالأنف… ») : la fumée passive est reconnue, l'erreur porte sur le filtre nasal.
- 10 `02-boss` q7 `c` (gonflement post-vaccinal jugé urgent) : ce n'est pas « vaccin = médicament ».
- 10 `03-revision` q9 `a` (« دواء… ليقيه من الكزاز ») : c'est l'erreur inverse, médicament pris pour vaccin.

**m-2 · Rampe qui redescend.**
- Fichiers concernés :
  - 02 `03-revision` : q7 d1 après q6 d3 ;
  - 03 `03-revision` : q8 d1 ;
  - 03 `05-entrainement` : q7 et q8 d2 après des d3 ;
  - 10 `01-pratique` : q7 et q8 d1 après des d2 ;
  - 10 `05-entrainement` : q7 d2 après des d3.
- Correction : déplacer ces questions dans le fichier jusqu'à leur place triée.
- Les UUID restent stables : le compilateur émet déjà les questions dans l'ordre trié par `difficulty`, et l'ordre d'écriture départage les égalités.

**m-3 · Un `::: verifie` du cours reposé mot pour mot**

La réponse est déjà repliée dans le cours. On change la situation :
- 02 `03-revision` q6 → `prompt` : `مرّرنا هواء الملعب مدّة قصيرة في كأس ماء جير، ونفخ عدّاء هواء زفيره في كأس ثانية. ماذا نلاحظ؟` Le reste inchangé.
- 02 `03-revision` q2 → `prompt` : `رسم تلميذ الرّئتين فجعل في كلّ رئة ثلاثة فصوص. كم فصًّا كان عليه أن يرسم في الرّئتين معًا؟` Le reste inchangé ; le distracteur « ستّة » exécute alors l'erreur dessinée.
- 02 quiz q7 :
  - `prompt` : `تواصل الرّضيعة التّنفّس وهي نائمة دون أن يعلّمها أحد. لماذا؟`
  - `a` → `لأنّها قرّرت أن تتنفّس قبل أن تنام` [34] ;
  - `c` → `لأنّ القلب يتنفّس عنها أثناء النّوم` [35] ;
  - clé `b` [35] et `d` [35] inchangées.
- 10 `02-boss` q3 :
  - `prompt` : `لُقّحت أختك الرّضيعة أمس، واليوم احمرّ موضع الإبرة وانتفخ قليلًا. بماذا تفسّر ذلك؟` ;
  - `b` → `أصيبت بالمرض الّذي لُقّحت ضدّه` ;
  - `c` → `اللقاح دواء لم ينجح في شفائها` ;
  - `d` → `تسرّبت إليها جراثيم الكزاز من الإبرة`.
- 02 `05` q4 (manuel p.50, 6-ب-2) et 10 `04-defi` q3 (manuel p.82, 7-ب) sont des questions du manuel : à garder.

**m-4 · 02 `05-entrainement` q5 : le conseil arrive après coup**

L'énoncé conseille Salma alors qu'elle est déjà sortie. `prompt` → `ستخرج سلمى من قاعة مكيّفة باردة إلى حرارة الصّيف. ما النّصيحة الصّحيحة؟`

**m-5 · 10 cours, exemple « نعالج ركبة الأخ الصغير » : « الماء المغلّى » sans ancrage**

L'étape 4 cite « الماء المغلّى », absent de l'ancrage (le geste vient du manuel p.82).
- ancien : `أمامكما قطن، وشاش معقّم، وملقط،`
- nouveau : `أمامكما ماء مغلّى، وقطن، وشاش معقّم، وملقط،`

**m-6 · Reprises verbatim du manuel sans champ `manuel`** (traçabilité seulement)
- manuel p.50, 6-ب : 02 `02-boss` q1, `03-revision` q3, `05-entrainement` q4 ;
- manuel p.65 : 03 `04-defi` q6 ;
- manuel p.82 : 10 `04-defi` q2 et q3.

**m-7 · 03 cours, section « تحت المجهر » : nouvelle notion dans la `propriete`**

La `propriete` introduit le lieu de formation, la durée de vie et la rate. Ce n'est pas la généralisation de l'exemple, et rien ne la vérifie (T6 sans T4). Ces faits sont testés (`02-boss` q2 et q3, `05` q2), mais ils viennent bien du manuel p.64. Aucun texte à changer d'urgence.

**m-8 · 03 cours, section « 🚚 » : deux notions dans une seule section**

Elle traite la plasma et les globules blancs. Acceptable, car la section suit le tableau de rôles du manuel p.67.

**m-9 · 03 `03-revision`, champ `manuel.items[0]` : référence imprécise**

« جذاذة 3، النشاط الأوّل » → `جذاذة الوحدة 3 عدد 1، وضعيّة مشكل 1، النشاط الأوّل`. Le guide p.109 est la « جذاذة تنشيط عدد 1 » de la و3.

**m-10 · 10 `04-defi` q2 : options miroirs**

`a` et `d` sont l'une le miroir de l'autre (sens du nettoyage), ce qui désigne la paire. Les deux phrases sont celles du manuel p.82 (7-أ). Admissible, signalé.

**m-11 · 03 : le piège « الشّرايين تحمل دائمًا دمًا قانيًا » n'a pas d'étiquette**

`04-defi` q7 l'exerce, mais aucun distracteur ne l'exécute exactement. Option : étiqueter après création d'un libellé et réécriture d'un distracteur. Non bloquant.

**m-12 · 10 `01-pratique` q8 `a` : mot non enseigné**

« الدّمّلة » n'est pas défini dans le cours (seul « القيح » l'est). Remplacer par `عصر الجرح المتقيّح بالأصابع لإخراج ما فيه` [41].

**m-13 · 10 cours : العقد اللّمفاويّة absentes**

- Le manuel p.72 les range parmi les المفاهيم du درس « التعفّن الجرثومي ». La fiche § 2 les dit « absentes du manuel » : c'est **faux**, à corriger dans la fiche.
- La p.73-ج et le guide p.114 (النشاط الخامس) les font intervenir dans la propagation, mais le cours ne les nomme pas.
- **Remplacement** dans `10-microbes-defense/cours.md` (ligne 183, chaîne unique) :
  - ancien : `وينتشر في الجسم، ولا يكفي عندها دفاعه وحده، وقد يحدث **التسمّم**`
  - nouveau : `وينتشر في الجسم، فتتدخّل **العقد اللّمفاويّة** للحدّ منه؛ فإن عجزت لم يكفِ دفاع الجسم وحده، وحدث **التسمّم**`
- Dans `resume.md` (puce 3) :
  - ancien : `إذا انتصرت الجراثيم استفحل التعفّن وحدث **التسمّم**`
  - nouveau : `إذا انتصرت الجراثيم استفحل التعفّن وتدخّلت العقد اللّمفاويّة، فإن عجزت حدث **التسمّم**`

---

## Axes cours (une ligne par axe)

**02 — 7 sections.**
- **Clarté** ✓.
- **Patron** : T1→T2→(T3)→T4→T5→T6→T7→retenir dans les 7 sections. Exemples, pièges et vérifications re-résolus, tous justes.
- **Exhaustivité** ✓ :
  - le درس 11 est couvert ;
  - les تصوّرات p.80 sont couvertes ;
  - le monoxyde (E-7a) est enseigné ;
  - les règles de prévention suivent le manuel p.51.
- **Expérience** ✓.
- **Illustration** : M-1. La figure 2 (شهيق/زفير : diaphragme plat ou en coupole, côtes) est juste.

**03 — 8 sections.**
- **Clarté** ✓.
- **Patron** : complet dans les 8 sections, sauf m-7. Tout est re-résolu et juste, y compris le circuit cœur → poumons → cœur → organes de la figure 5.
- **Exhaustivité** ✓ : les دروس 14–15, V2, l'éval. n° 2 T5 et le حاجز 5 sont couverts, plus M-7.
- **Expérience** ✓.
- **Illustration** ✓ : 5 figures justes (frottis, tubes « sédimenté à droite / coagulé à gauche » conformes à la légende, plaquettes, alvéole, circuit).

**10 — 7 sections.**
- **Clarté** ✓.
- **Patron** : complet. « البشرة… والأدمة الطبقة الحيّة » reprend le libellé du manuel p.69. C'est une simplification, pas une erreur à corriger ici.
- **Exhaustivité** : les دروس 16–19 sont couverts, sauf m-13.
- **Expérience** ✓.
- **Illustration** ✓ : coupe de peau et البلعمة en 4 temps, lecture de droite à gauche conforme à la légende.

## Après lecture des notes et du rapport de l'auteur

- **Concordances.** Mes constats recoupent les doutes de l'auteur :
  - doute 6, figures jamais vues dans un navigateur : M-1 le confirme ;
  - doute 5 : l'erreur « coton » est ambiguë, la retirer du `multi` est juste ;
  - doute 3 : V2 lu strictement (plaquettes seulement) ; je l'approuve.
- **Écart d'appréciation.** Les étiquettes proposées par l'auteur (9 ids) sont reprises, mais limitées aux trois dont un distracteur exécute exactement l'erreur (M-6).
- **Manqués par l'auteur** :
  - C-1 ;
  - les exemples du cours reposés (M-2) ;
  - les options qui se recouvrent (M-3, M-4) ;
  - les étiquettes fausses (M-5, m-1) ;
  - la clé à prémisse absente (M-8) ;
  - la notion du sel non enseignée (M-7) ;
  - le constat erroné de la fiche sur les العقد اللّمفاويّة (m-13).
- **Doute 1 de l'auteur** (`manuel.code` = 503604) : ne relève pas de l'audit. Le gate l'accepte et le PDF confirme les pages.
