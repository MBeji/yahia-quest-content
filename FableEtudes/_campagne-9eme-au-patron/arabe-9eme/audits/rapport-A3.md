# Rapport d'audit A3 — arabe 9ᵉ, chapitres 12, 05, 13, 14

Auditeur indépendant. Sources : notes L129, L134, L140, L148, L154, L164, L169, ecart-4 ; pages du manuel
101908 relues à l'image quand une note laissait un doute (p. 131, 146, 158, 169, 170, 171, 172). Rapports des
rédacteurs non lus. Contrôles lancés depuis le moteur.

Ligne de base avant toute correction : `content:check` vert ; `content:qa` sans aucune ligne pour 12, 05, 13, 14 ;
`content:tranche` : 0/140 clé strictement la plus longue, positions a 39 · b 37 · c 33 · d 31, 0 paire proche,
1 gabarit (05-tadrib#5 / 06-al-mushtaqqat 05-tadrib#3) ; Prettier vert sur les 24 `.json` (vérifié par le
chemin `content/` du moteur, qui porte sa configuration).

---

## 12 — `12-al-maqsur-wal-manqus-wal-mamdud` (L129, L134, L140)

**Questions re-résolues : 35/35** (quiz 5 + 5 × 6), clés toutes justes. Re-dérivés aussi : les 10 `exemple`,
les 7 `piege` et les 10 `verifie` du cours.

### Erreurs corrigées (avant → après)

1. **`cours.md` §🌙, piège** — « التنوينُ يظهرُ عليه **كلَّما** كان نكرةً » → « … **إذا** كان نكرةً » (formule
   du manuel), et une phrase ajoutée à l'encadré 🚀 : « ومنه ما خُتمَ بألفِ تأنيثٍ مقصورةٍ (ذِكرى، سَلْمى،
   حَيرى)، فلا يُنوَّنُ ولو ورد نكرةً ». « كلّما » était faux pour ذِكرى, سَلْمى, يُسرى, حَيرى, فَدْوى — que le
   chapitre cite lui-même comme مقصور.
2. **`cours.md` §🔥 (définition + exemple, pas 3) et `resume.md`** — « تنوبُ الفتحةُ عن الكسرةِ … فيما كانت
   همزتُه همزةَ تأنيثٍ » / « لأنّ ما لا يُنوَّنُ يُجرُّ بالفتحةِ » → ajout de la condition « فإن دخلته «أل» أو
   أُضيفَ جُرَّ بالكسرةِ: مررتُ بالصّحراءِ » / « … إذا خلا من «أل» والإضافةِ ». Telle quelle, la règle
   menait à « في الصّحراءَ ».
3. **`cours.md` §🔥 (tableau) et §🎯 (énoncé, méthode)** — « أكفاءُ » → « أكفاءٌ ». أكفاء = أفعال de كُفْء
   (hamza radicale) : il est مصروف. Coquille de vocalisation du manuel (p. 146, vérifiée à l'image) que le
   chapitre reprenait, et que son propre tableau contredisait (« بِناءٌ » à la ligne au-dessus).
4. **`cours.md` §🧪, exemple, pas 1 (+ ligne du tableau, `resume.md`, `02-boss` q0 explication)** —
   « مؤنّثُ أفعلَ … على فَعْلاء إذا دلّ على لونٍ أو عيبٍ، وعلى فُعْلى **فيما سواه** » → « … على لونٍ أو
   **صفةٍ** (حمراء، عرجاء، حوراء)، وعلى فُعْلى **إذا دلّ على التّفضيلِ** (الكُبرى، الصُّغرى) » ; « أيسرُ … ليس
   للّونِ ولا للعيبِ » → « … للتّفضيلِ (الأسهلُ) لا للّونِ ولا للصّفةِ ». La règle « فيما سواه » donnait
   *حُورى pour أحور et *شُمّى pour أشمّ — alors que « الشَّمّاء » ouvre la section 🔥 ; le manuel dit
   « الدّالّة على اللّون أو الصّفة ».
5. **Patron** — `propriete` replacée après l'exemple (et le piège) dans §⚔️, §🌊, §🗝️ (avec sa `ملاحظة`) ;
   `methode` replacée après le piège dans §🎯. Blocs déplacés tels quels.

### Remarques (non corrigées)

- quiz q2 et §⚔️ exemple, pas 2 : l'origine واو de « عصا » est prouvée « بدليلِ جمعِها «عَصَوات» » —
  raisonnement circulaire (عَصَوات se forme par la même règle que عَصَوان). Preuve sûre : « عَصَوْتُه
  بالعصا ».
- §⚔️, tableau : « مُستشفى … الجمعُ السالمُ — », alors que « مستشفيات » est courant.
- Définition du ممدود « همزةٌ بعد ألفٍ » sans « ألف **زائدة** » : « ماء », « داء » y entrent (le manuel glisse
  « الماء » en piège, p. 142). Aucun item n'en dépend.
- جُبناءُ, أتقياءُ, أصدقاءُ (فُعَلاء / أَفْعِلاء) ont une hamza d'تأنيث (non nunatés) ; l'étape 1 de la méthode
  §🗝️ (seul « فَعْلاء مؤنّث أفعل ») ne permet pas de les classer. Aucun item ne les met au جرّ ni au duel.
- `01-pratique` q4 : distracteur « قواضي » mal formé (indéfini : قواضٍ) et attesté comme pluriel de قاضٍ au sens
  « tranchant » (سيوفٌ قواضٍ). Le sens « juge » rend قُضاة sûr ; à remplacer à l'occasion.
- `02-boss` q0 « يَسراء » : vérifié non défendable (les lexiques refusent « عَسْراء يَسْراء » ; l'usage dit يُسرى).
- Étapes d'exemple sans « لأنّ » (mineur) : §🏰 pas 1, §⚔️ pas 1–2, §🌊 pas 1 et 3.
- §🧬, méthode : « الميمَ والتاءَ في أوّلِ المشتقِّ » (la تاء d'افتعل n'est pas en tête : مُرتجى, مُعتدٍ) ;
  « الألفَ الأخيرةَ في مؤنّثِ أفعلَ وفَعلانَ » n'englobe pas سَلْمى / سُعدى, traités dans la même section.
  Le `verifie` §🧬 (مُعتدٍ) reprend un mot déjà résolu dans le tableau : pas un vrai jumeau.
- Cohérence 12 ↔ 14 : au duel, 12 suit le manuel (منقلبة : إبقاء أو إرجاع إلى الأصل → بِنايان) ; à la نسبة,
  14 suit la règle classique (الهمزة أو الواو → انتقاويّ, jamais *انتقاييّ). Deux opérations différentes, pas
  une contradiction, mais un élève peut transposer « بنايان » : une phrase de liaison dans 14 aiderait.
- R-13 : 10 sections (> 8 notions) — question de curriculum déjà notée dans la fiche §6.
- Couverture (ecart-4) : les trous sont comblés (فُعْلى / فَعْلى, جذر, صيغة imposée, 12 mots p. 146, بِنايان
  réhabilité). Absent : remettre un منقوص au نصب après كان / ما زال / صار (p. 137, ex. 5).

**Contrôles après correction** : `content:check` vert ; `content:qa` : 0 ligne pour 12 ; Prettier vert.
**Verdict : conforme après corrections.** **Clarté : 4/5.**

---

## 05 — `05-sarf-al-mizan` (L148, L154 ; tableau p. 158 relu à l'image)

**Questions re-résolues : 35/35** (quiz 5 + 5 × 6), clés toutes justes. Re-dérivés : les 13 `exemple`,
13 `piege` et 13 `verifie`.

### Erreur corrigée (avant → après)

1. **`cours.md` §🍳 (tableau et `verifie`)** — « افْتَرَشَ المسافرُ **ردائَهُ** » → « … **رداءَهُ** » (2
   occurrences) : hamza après alif, مفتوحة (مفعول به), donc sur la ligne.

### Points du mandat vérifiés

- **Sens des onze أوزان** conformes aux خلاصات p. 151 et 157 et au جدول تأليفي p. 158 : أفعل 3, فعّل 4, تفعّل 6,
  فاعل 1, تفاعل 4, افتعل 4, انفعل 2, افعلّ 1, استفعل 4, افعوعل 2 ; افعالّ attribué au seul tableau.
- **« لا تتّضح إلّا بالسّياق »** : aucun item où deux sens restent défendables. تحوّل / تشبّه : `06` q0
  (اسْتَحْجَرَ) n'offre pas التّشبّه. مطاوعة / مشاركة : `06` q3 (تَباعَدَ) est tranché par le verbe premier.
  جعليّة / تكثير : `02` q2 (كَسَّرَ) et `01` q3 (فَرَّحَتْني) sont nets.
- **« تَعَلَّمَ » = تضعيف العين** partout (cours l. 35 et 42, résumé) : l'erreur signalée par ecart-4 est corrigée.
- **مصادر et مشتقّات des onze أوزان** : tableau conforme à la p. 150. La note « × » est attribuée au livre,
  avec « مُحْمَرّ » des grammaires dans l'encadré 🚀, et aucun item ne la teste. **Coquille p. 150** non
  reprise : « افْعِيلال (احْمِيرار) », la coquille étant signalée comme telle.
- **Métalangage** : عناصر الزّيادة, الجعليّة, بذل الجهد, التّظاهر. التّعدية, التّكلّف et سألتمونيها ne figurent que
  dans l'encadré 🚀 ; aucun item ne les emploie.
- **Gabarit 05 ↔ 06** — tranché : **on garde les deux**. `05-tadrib` q4 (#5) porte sur le nom de patient
  d'اسْتَفْعَلَ (مُسْتَفْعَل), lu dans le tableau p. 150. `06/05-tadrib` q2 (#3) porte sur le ثلاثي (مَفْعول).
  Les notions et les clés diffèrent : ce n'est pas un doublon, rien n'est changé.

### Remarques (non corrigées)

- L'heuristique « نوعُ الجذرِ يختارُ المعنى » (فعل ← جعليّة ; اسم شيء ← صيرورة ; مكان / زمان ← دخول) est
  celle du chapitre, pas du manuel, qui dit « بحسب الجذر الّذي يتّصل به » et renvoie au contexte. Elle tient
  sur tous les exemples et items du chapitre, mais a des contre-exemples (أسرع, أقبل : جذر فعل sans جعليّة).
  Le manuel lui-même donne « أقحل » pour الصّيرورة. À nuancer (« في الغالب ») à la prochaine passe.
- §🧭, tableau intitulé « (جدولُ كتابِك) » : deux cases ne reprennent pas la p. 158. Pour الصّيرورة, le
  manuel a « أقحل », le chapitre « أثمر » (pris au مدخل p. 149). Pour بذل الجهد, le manuel a « تخطّ… » à
  moitié sous le filigrane, le chapitre « تصبّر » (pris au مدخل). L'attribution est à nuancer.
- §🚪, cas-limite de la méthode : « إذا غابَ الفاعلُ من الجملةِ » vise l'auteur du fait, pas le فاعل
  d'« انكسر » (الزّجاج), qui est bien là. La formulation prête à confusion.
- §🤝, tableau : « تَلاعَبَ الأبُ وابنُهُ » — « تلاعب » se lit aujourd'hui surtout « manipuler ». Il est
  classique au sens de « jouer ensemble », mais un autre exemple serait plus sûr.
- §🌱 : الدّخول « في مكانٍ أو زمانٍ أو دينٍ » ; le manuel ajoute « أو المذهب ».
- R-13 : 13 sections (> 8 notions) pour deux leçons du manuel — question de curriculum.
- Métadonnées laissées telles quelles (hors mandat) : titres sans ⭐ (quiz, `01`, `02`, `04`, `05-tadrib`),
  `01-pratique` en d2 (75/15).

**Contrôles après correction** : `content:qa` : 0 ligne pour 05.
**Verdict : conforme après correction.** **Clarté : 4/5** (dense, 860 lignes, mais chaque section suit le
patron et chaque pas d'exemple dit « لأنّ »).

---

## 13 — `13-at-tasghir` (L164)

**Questions re-résolues : 35/35**, clés toutes justes. Re-dérivés : les 9 `exemple`, 7 `piege` et
9 `verifie` du cours.

### Erreurs corrigées (avant → après)

1. **`exercices/04-defi.json` q5, explication** — « فيصيرُ «**حُدَيْقة**» » → « فيصيرُ «**حُدَيِّقة**» (تُدغَمُ
   ياؤُه الثّالثةُ في ياءِ التّصغيرِ كما في «كُتَيِّب») ». حديقة a une lettre de prolongation en 3ᵉ position :
   d'après la règle du chapitre lui-même (§🔀, كِتاب ← كُتَيِّب) et la grammaire (سَعِيد ← سُعَيِّد, صَحِيفة ←
   صُحَيِّفة), le diminutif est حُدَيِّقة.
2. **`cours.md` §🔎, méthode, étape 2** — « الياءَ المنقلبةَ **إلى ألفٍ** (كُتَيِّب ← كِتاب) » → « … **إلى
   أصلِها من حروفِ اللّينِ** (ألفٌ في كُتَيِّب ← كِتاب) ». Comme règle générale, « إلى ألف » est faux :
   عُجَيِّز ← عَجُوز, سُعَيِّد ← سَعِيد.
3. **Patron** — `propriete` replacée après l'exemple et le piège dans §📏, §🔀 et §💗 ; `methode`
   replacée après le piège dans §🎯. Blocs déplacés tels quels ; l'exemple de §🎯 (« طبِّقْ ») s'appuie sur
   la méthode en trois pas de l'exemple de §💗, qui le précède.

### Points du mandat vérifiés

- **Trois أوزان** (فُعَيْل / فُعَيْعِل / فُعَيْعِيل) conformes à la خلاصة p. 166–167 (quiz q2, `01` q4, `02` q0,
  `05` q3).
- **Six sens lus dans le contexte** : chaque item porte l'indice qui tranche. « على الأكثر » → تقليل ;
  « وفجعتَ قلبي » → حسرة, sans التّودّد parmi les options ; « بصوتٍ هادئٍ حزينٍ » → تودّد ; « ما … إلّا » →
  تحقير ou تقليل selon le nom ; قُبَيْل / دُوَيْن → تقريب. Aucun item n'a deux sens défendables.
- **Sections neuves** : أُخَيّ, أُبَيّ, أُخَيّة, دُبَيْب (فُعَيْل), دُوَيْبّة (فُعَيْعِل) sont justes. L'opération
  inverse est juste (كُلَيْب, سُمَيْكة, دُفَيْتِر, كُتَيِّب, قُطَيْط, هُرَيْرة ← هِرّة). Les أعلام aussi
  (هُرَيْرة, حُسَيْن contre الوَلِيد, أَمِين, الحدّاد).
- L'opposition « بُنَيّ tendre / méprisant » a disparu : le تحقير est porté par عُوَيْلِم (p. 165), شُوَيْعِر et
  الخُوَيْدِم (p. 168).

### Remarques (non corrigées)

- §🔀, piège : « التاءُ والهمزةُ الممدودةُ خارجَ العدِّ **دائمًا** ». Il faudrait dire « ألفُ التأنيثِ
  الممدودةُ », car سماء, بناء, كساء (hamza non féminine) n'obéissent pas à cette règle. Aucun item ne les met
  au diminutif.
- §📏 : l'exemple (ساعة ← سُوَيْعة) anticipe la règle de §🔀 (المنقلبة ترجع إلى أصلها) et ne reprend pas
  les mots du T1 (قلم, كوكب, عصفور).
- Étapes d'exemple sans « لأنّ » : l'exemple de §🏰 n'en a aucune (« لكنّها » seulement) ; §🔧 pas 1.
- §🎯 : la question du T1 (عُوَيْلِم) n'est pas résolue dans la section (l'exemple traite شُوَيْهَتي, la
  vérification الخُوَيْدِم) ; la réponse, تحقير, n'apparaît qu'au piège de §💗.
- « قال أعرابيٌّ لمن ذبحَ شاتَه » (§🎯 et `02-boss` q4) : dans l'anecdote, c'est le louveteau nourri par la
  brebis (« وأنتَ لشاتِنا ولدٌ رَبيبُ ») qui l'a tuée. Paraphrase lâche, sans effet sur la clé.
- كُرَة ← كُرَيَّة est expliqué comme « حرف اللّين الثّالث » d'un « أصل كُرْو ». Il s'agit plutôt de rendre
  la lettre supprimée (comme أب / أخ). Simplification admissible.
- `resume.md` : « سِرْوال ← سُرَيْوِيل » (forme juste, du manuel p. 166) n'apparaît pas dans le cours.
- R-13 : 9 sections (> 8 notions).

**Contrôles après correction** : `content:qa` : 0 ligne pour 13 ; Prettier vert.
**Verdict : conforme après corrections.** **Clarté : 5/5** (le plus net des quatre : progression simple,
tableaux de passage, chaque piège est une vraie erreur d'élève).

---

## 14 — `14-an-nisba-wal-masdar-as-sinai` (L169 ; p. 169–172 relues à l'image)

**Questions re-résolues : 35/35.** Les clés sont justes, mais **cinq items avaient un distracteur défendable**
(corrigés ci-dessous, clés inchangées). Re-dérivés : les 6 `exemple`, 4 `piege` et 6 `verifie` du cours.

### Erreurs corrigées (avant → après)

Items
1. **`03-revision` q2** (يَد) — distracteur « **يَدِيّ** » → « **يَداويّ** », avec une phrase d'explication sur
   les distracteurs. « يَدِيّ » est correct : pour يد, دم, شفة, لثة, rendre la lettre finale supprimée est
   facultatif (Alfiyya : « واجبُرْ بردِّ اللّامِ ما منه حُذِفْ * جوازًا اِنْ لم يكُ ردُّه أُلِفْ * في جمعَي
   التّصحيحِ أو في التّثنيهْ » ; Ibn ʿAqīl : يَدِيّ ويَدَوِيّ). L'item avait donc deux bonnes réponses.
2. **`02-boss` q1** (سماء) — distracteur « **سَماءيّ** » → « **سَماءَويّ** ». « سَماءيّ » se prononce comme
   « سَمائيّ », que le cours et l'item admettent (« يجوزُ الوجهانِ »), seule l'orthographe diffère. Or
   l'explication l'écartait comme « collé sans préparation ». L'explication nomme maintenant les deux formes
   permises et dit pourquoi « سَماءَويّ » (les deux procédés cumulés) est fausse.
3. **quiz q2 ; `01-pratique` q0 et q2** — le distracteur féminin (« فاطميّة », « كُوفيّة », « حريريّة ») est la
   même نسبة au féminin, donc une forme juste. Ajouté au prompt : « … نعتًا لـ«عهد» » / « لـ«خطّ» » /
   « لـ«ثوب» », plus une clause d'explication (« مؤنّثةٌ لا تكونُ نعتًا لـ«عهد» المذكّرِ »).
4. **`02-boss` q4, explication** — « «السّلفيّة» لا تقعُ نعتًا » → « جاءت هنا قائمةً بنفسِها لا نعتًا ».
   « الحركةُ السّلفيّةُ » existe : le critère est la fonction ici, comme le cours le pose.

Cours et résumé
5. **§🔧 propriété + `resume.md`** — « ضَوْء (ض و ء) ← ضَوْئيّ » rangé parmi les **ممدود** → conservé comme
   cas où la hamza reste, mais « … وليس ممدودًا: لا ألفَ قبلَ همزتِه » (contredisait la définition du 12).
6. **§🔧 piège** — « «فاطمةيّ» أو «**يَديّ**» » (forme admise, voir 1) → « «فاطمةيّ» أو «**أبِيّ**» ». Pour أب,
   le retour de la lettre supprimée est obligatoire (أبَوان → أبَويّ).
7. **§🔧 vérification** — « بُنْدُقيّ (سقطت تاءُ التأنيثِ) » → ajout de « وحلّت ياءُ النّسبةِ محلَّ الياءِ
   المشدّدةِ التي في الاسمِ ». Ne faire tomber que la تاء donnait *بُنْدُقيّيّ.
8. **§🔁 exemple, pas 3** — « «العلوم» **جمعُ مؤنّثٍ** … لأنّ النّعتَ يتبعُ منعوتَه في التعريفِ والإعرابِ
   **والعددِ** » → « جمعُ تكسيرٍ لغيرِ العاقلِ … في التعريفِ والإعرابِ، ونعتُ جمعِ غيرِ العاقلِ يأتي غالبًا
   مفردًا مؤنّثًا ». علوم est le pluriel brisé de عِلْم (masculin) et الطّبّيّة est au singulier.
9. **§🔁 méthode, étape 3** — « مطابقًا له في التعريفِ **والتّذكيرِ** والإعرابِ » → « في التعريفِ
   والإعرابِ ». Ses propres exemples ne s'accordent pas en genre : الكتبُ الهنديّةُ, أعمدةٌ رُخاميّةٌ.
10. **§🔁 vérification** — réponse « الرّخامُ ورديٌّ أو «لونُ الرّخامِ ورديٌّ» » : deux phrases nominales
    (ورديّ y est خبر), alors que la question demande un مركّب نعتيّ. Remplacée par « **الرّخامُ الورديُّ** …
    وجُعلت نعتًا لـ«الرّخام» ».
11. **§🧪 vérification** — « السّلفيّةُ … **لا يقعُ نعتًا** … وتُطابقُه في التعريفِ **والعددِ** » →
    « … جاءَ هنا قائمًا بنفسِه لا نعتًا … في التعريفِ والإعرابِ ». الأعمدة est pluriel, الرّخاميّة singulier.
12. **`resume.md`** — « والنّعتُ يُطابقُ منعوتَه تعريفًا **وعددًا** وإعرابًا » → « تعريفًا وإعرابًا، ونعتُ
    جمعِ غيرِ العاقلِ مفردٌ مؤنّثٌ غالبًا ».
13. **§🏰 T1** — citation fausse « سَمْراءُ **القامةِ** » → « سَمْراءُ **اللّونِ** … نَجْلاوَيْنِ **ساحرتَينِ** »
    (texte p. 169 : « ممشوقةَ القامةِ سمراءَ اللّونِ … بعينين نجلاوين ساحرتين ») ; « **خمسُ** كلماتٍ » →
    « **أربعُ** » (quatre نسب en gras).
14. **Patron** — `propriete` de §🔧 replacée après le piège ; `methode` de §🔁 après l'exemple, `methode` de
    §⚠️ après le piège.

### Points du mandat vérifiés

- « لِثَة ← لِثَويّ » dans le cours et dans `04-defi` q0 ; la coquille « لَثَة » du manuel n'est pas reprise.
- المتنبّي est justifié comme « اسمُ فاعلٍ من «تنبّأ»، ياؤُه ليست ياءَ نسبةٍ », et non plus comme « منقوص ».
  الرّاعي, الصّحاري et الكُرْسيّ sont bien rangés hors نسبة.
- ⚠️ **Le mandat range « المعرّي » parmi les non-نسبة : c'est une erreur du mandat.** « المَعَرّي » se rattache à
  مَعَرّة النّعمان. La liste de la p. 172 (relue) est une liste de noms propres, et la fiche avait corrigé ce
  partage à l'image le 2026-09-20 (4 نسبة / 4 non). Le chapitre a raison : non modifié.
- « فَعِيلة ← فَعَليّ » : aucun item n'offre مدينيّ, قبيليّ ou طبيعيّ. `05` q1 propose مَدينةيّ, مُدَيْنيّ, مَدْنيّ ;
  `04` q4 propose قَبيلةيّ, قُبَيْليّ, قَبْليّ. Le cas-limite « الطّبيعيّة » est écrit dans la propriété.
- Les définitions (نسبة, ياء النّسبة, المصدر الصّناعيّ) sont les خلاصات verbatim de la p. 171.

### Remarques (non corrigées)

- §🏙️, piège : « مدينيّ » et « قبيليّ » présentés comme « الخطأ الشائع ». La norme classique est مَدَنيّ, mais
  مدينيّ est attesté et l'Académie du Caire admet فَعِيليّ (« l'usage dit aussi مدينيّ », dit le mandat).
  Écrire « والأفصحُ » au lieu de « والصوابُ على قاعدةِ الكتابِ » (le livre n'écrit aucune règle ici).
- §🔧, propriété : « الثلاثيُّ المحذوفُ الآخِرِ يستردُّ محذوفَه » est présenté comme absolu. C'est obligatoire
  pour أب, أخ, سنة, facultatif pour يد, دم, شفة, لثة. Et « شَفَة ← شَفَويّ » est seul donné, alors que
  l'exemple pose l'origine « شَفَه », qui donne « شَفَهيّ », la forme moderne la plus courante. Même
  nuance pour « بابٌ مطّردٌ » (`01` q3, explication).
- §⚠️, vérification (مَرْوَزيّ / مَرْوِيّ) : elle introduit une notion neuve (نسبة irrégulière), testée par
  `04-defi` q2 et reprise au résumé, mais enseignée seulement là. Mieux vaut un court paragraphe enseigné.
- §🧪 (T1, tableau) : « الأوّليّة » ; le manuel (p. 171) a « الأولويّة ». Ce n'est pas une faute.
- §🔁 : le tableau titré « المركّبُ الإضافيُّ » contient 4 lignes sur 5 de جارّ ومجرور.
- §🏙️, définition : « «فَعِيلة»: اسمٌ ثلاثيٌّ ثالثُه ياءٌ » mêle racine et mot. À reformuler.
- Non servis (exercices du manuel) : نسبة de ماء, عَداء, عُدْوان, أمّ, حَمّ (p. 172, ex. 2) ; la fonction de la
  نسبة (ex. 7) ; la production « cinq نسب par matière » (ex. 1). Mineur.

**Contrôles après correction** : `content:qa` : 0 ligne pour 14 ; Prettier vert.
**Verdict : conforme après corrections.** **Clarté : 4/5.**

---

## Synthèse

| Chapitre | Questions re-résolues | Erreurs corrigées | Verdict | Clarté |
| --- | --- | --- | --- | --- |
| 12 المقصور والمنقوص والممدود | 35 | 4 de fond (règles) + 4 blocs déplacés | conforme après corrections | 4/5 |
| 05 معاني صيغ الزّيادة | 35 | 1 (orthographe de la hamza, ×2) | conforme après correction | 4/5 |
| 13 التّصغير ومعانيه | 35 | 2 de fond + 4 blocs déplacés | conforme après corrections | 5/5 |
| 14 النّسبة والمصدر الصّناعيّ | 35 | 5 distracteurs défendables, 1 explication d'item, 9 de cours et résumé + 3 blocs déplacés | conforme après corrections | 4/5 |

**140 questions re-résolues** : aucune clé fausse. Six items de 14 avaient un distracteur défendable ou une
explication fausse, tous corrigés sans changer de clé : cinq distracteurs (يَدِيّ, سَماءيّ et trois féminins) et
une explication (السّلفيّة, `02-boss` q4).

**Contrôles finaux** (depuis le moteur, après toutes les corrections) :
- `content:check` vert (arabic : 19 chapitres, 94 exercices, 562 questions).
- `content:qa` : 0 erreur, aucune ligne pour 12, 05, 13, 14. Une erreur `math/02-racines-carrees` (C-5) est
  apparue un moment pendant l'audit puis a disparu : c'est le travail d'un autre agent, hors de mon lot.
- `content:tranche --chapters 12,05,13,14` : 0/140 clé strictement la plus longue ; positions a 39 · b 37 ·
  c 33 · d 31 ; 0 paire proche ; 1 gabarit (05 ↔ 06), tranché ci-dessus : on garde les deux.
- Prettier `--check` vert sur les 24 `.json`. Aucun Prettier sur les `.md` ; les fermetures `:::` après une
  liste gardent leur ligne vide.

**Fichiers modifiés** (aucune écriture git, nombre de questions et métadonnées inchangés) :
- `content/arabic/12-al-maqsur-wal-manqus-wal-mamdud/` : `cours.md`, `resume.md`, `exercices/02-boss.json`.
- `content/arabic/05-sarf-al-mizan/cours.md`.
- `content/arabic/13-at-tasghir/` : `cours.md`, `exercices/04-defi.json`.
- `content/arabic/14-an-nisba-wal-masdar-as-sinai/` : `cours.md`, `resume.md`, `quiz.json`,
  `exercices/01-pratique.json`, `02-boss.json`, `03-revision.json`.

**À arbitrer par un humain** (doutes listés, non tranchés par moi) :
- 14 : nuancer le piège « مدينيّ / قبيليّ » (أفصح plutôt que صواب) et la règle de retour de la lettre
  supprimée (facultatif pour يد, دم, شفة, لثة).
- 05 : nuancer l'heuristique « نوع الجذر » (le manuel donne « أقحل » pour الصّيرورة).
- Le mandat range المعرّي parmi les non-نسبة : c'est faux, le chapitre et la fiche ont raison.
