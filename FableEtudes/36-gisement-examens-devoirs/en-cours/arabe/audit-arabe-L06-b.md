# Audit L06-b — gisement arabe 9ᵉ, vague 2 : m036–m038 (ch. 10, compréhensions techniques)

Auditeur indépendant. Branche `wip/gisement-arabe-9eme-anciennes`, commit `70453271`, arbre `/home/user/wt-ar2`.
Fichiers : `content/arabic/10-fahm-wa-intaj/exercices/18-examen-2015-technique-fahm-fakhkhar.json` (m036),
`19-examen-2017-technique-fahm-istihlak.json` (m037), `20-examen-2011-technique-fahm-bitala.json` (m038).
Sources lues en vision : PDF officiels `C22` (2015 T), `C18` (2017 T), `C28` (2011 T), plus les transcriptions
`2015-technique.md`, `2017-technique.md` et `2011-technique.md`. Je n'ai pas ouvert les notes des auteurs.

Gates (moteur `/home/user/eng-ar`) :
- `content:check` : vert.
- `content:qa:strict` : 0 erreur, et aucun avertissement sur ces trois fichiers.
- `content:tranche --chapters 10` : la clé est strictement la plus longue dans 0/123 questions, les positions de clé sont équilibrées, aucune paire proche, aucun candidat gabarit.

Rendu `dir=rtl` : contrôlé en Chromium 1194 à 360 px, les 24 questions avec leurs options et explications passées par
`isolateLtrRuns` (aucune chaîne n'est modifiée). Les `ordering` (m036 Q6), les `matching` (m036 Q3, m037 Q3, m038 Q2),
les options avec « ؛ » (m036 Q7, m037 Q8), les parenthèses (m038 Q2 r3), les « … » dans les citations et les années dans
« (مناظرة 2015، تقنيّ) » s'affichent tous dans l'ordre du texte source. **Aucun défaut de rendu.**

---

## 1. Re-résolution à l'aveugle

### m036 — 2015 T « نجل الفقير »

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | QCM | صناعة الفخّار | b | OK | le texte entier porte sur le travail du طين ; الصوف n'y est qu'une mention |
| 2 | QCM | تشعران بالارتياح | c | OK | sens contextuel, options officielles plus un contraire |
| 3 | matching | خزف→فخّار, خلق→إبداع, كومة→رزمة, مكتظّة→ممتلئة | idem | OK (réserve graphie) | paires de l'officiel |
| 4 | QCM | « من مكان يبعد… كيلومترات » | d | OK (réserve citations) | seul effort physique parmi les options |
| 5 | QCM | « فما بقي من العمل لهو ممتع لذيذ » | a | OK (réserve citation) | |
| 6 | ordering | جلب، طرح، خلط، عجن، تشكيل، تزيين | f d b e c a | OK | conforme au PDF (§ 7) |
| 7 | QCM 2×2 | سحق entre طرح et خلط ; تجفيف entre تشكيل et تزيين | c | OK, mais **réserve majeure** | la clé se lit dans les extraits cités (§ 2) |
| 8 | multi | a, c, e | a, c, e | OK, mais **réserve majeure** | l'énoncé et deux options fuient vers Q4 (§ 1) |

### m037 — 2017 T « حدّ السكّين على العنق »

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | QCM | طلبات كثيرة | c | OK, mais **réserve majeure** | l'énoncé désigne les deux leurres officiels comme des détails |
| 2 | QCM | بلا منفعة | b | OK (mineur) | |
| 3 | matching | ترهق↔تريح, الجوّال↔القارّ, تمتدح↔تذمّ | idem | OK | |
| 4 | multi | مماطلة، ألم، مسؤوليّة | a, c, e | OK, mais **majeur** | forme une paire miroir avec Q5 (§ 1) |
| 5 | multi | تقليد، كثرة الطلبات، انبهار، شكوى | b, c, d, f | OK, mais **majeur** | idem |
| 6 | QCM | « أريد آخر ملوّنا متطوّرا » | a | OK | |
| 7 | QCM | قلّة المال وكثرة الطلبات… | d | OK (mineur) | |
| 8 | QCM | التقليد + تذمّر الابنين | c | OK, mais **réserve** | trois leurres s'éliminent à vue (§ 4) |

### m038 — 2011 T « البطالة »

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | QCM | ارتفاع البطالة بسبب إحلال الآلات | d | OK | trop large, trop étroit, solution : leurres justes |
| 2 | matching | عويصة→معقّدة, مفضية→موصلة, أنوال→مناسج | idem | OK (note graphie) | |
| 3 | QCM | الأسباب المفضية… | b | OK (mineur) | |
| 4 | QCM | التغيّر التكنولوجي | a | OK | lecture directe, comme l'officiel |
| 5 | QCM | « كلّما ازدادت… ازدادت نسبة البطالة » | c | OK (mineur) | « صريحة » rend la clé unique (§ 5) |
| 6 | multi | نسيج، زراعة، بريد | a, c, e | OK | |
| 7 | multi | طبّ، تعليم، بنوك | b, d, f | OK, mais **majeur** | les parenthèses ne figurent que sur les clés (§ 5) |
| 8 | multi | a, d, f | a, d, f | OK (mineur) | deux options à reformuler |

**Bilan : 24 questions re-résolues, 0 clé fausse.**

---

## 2. Points prioritaires de l'auteur : décisions

### § 1 — Fuites entre questions

- **m036 Q8 → Q4 : MAJEUR, à corriger.** L'énoncé de Q8 définit le عناء : جلب الطين… من مكان بعيد. Les options a (« من مكانه البعيد ») et f (« مكان أبعد ») le redisent. Or la clé de Q4 est justement « من مكان يبعد عن القرية… ».
  - L'explication de Q6 fuit aussi vers Q4 (« يُجلَبُ الطينُ أوّلًا من مكانِه البعيدِ »).
  - Correctifs C1 et C2 ci-dessous.
- **m036 Q3 / Q1 : acceptable, rien à changer.** L'explication de Q3 dit que الخزف = الفخّار, ce qui aide Q1. Mais l'énoncé de Q1 donne déjà le travail بالطين, et la paire vient de l'officiel, où les deux questions coexistent.
- **m037 Q4 / Q5 : MAJEUR, à corriger.** C'est une paire miroir : les deux questions tirent leurs options de la même liste de 8 traits, avec un classement binaire.
  - Q4 a pour clés مماطلة et مسؤوليّة. Q5 les reprend comme distracteurs, et réciproquement pour تقليد, انبهار et كثرة الطلبات.
  - Le retour de l'une résout l'autre. L'explication de Q4 le dit même en toutes lettres (« أمّا بقيّةُ الصفاتِ… فتصدرُ عن الأسرةِ »).
  - De plus, l'énoncé de Q5 cite l'extrait des ابني وابنتي يتذمّران, qui est la justification-clé de Q8.
  - Correctif C5 : deux `multi` à options **disjointes** (2 clés sur 4 chacune, les 8 traits officiels répartis). Cela supprime aussi la 3ᵉ citation.
- **m038 Q1 / Q4 / Q5 (« التغيّر التكنولوجي ») : fuite inhérente au sujet, acceptée.**
  - Le sujet du texte, la cause principale et la قرينة sont la même idée dans l'officiel : Q1 et Q4 se recoupent forcément.
  - Q4 se résout de toute façon par sa propre citation (« العامل الأساسي »).
  - La clé de Q5 n'est citée dans aucune autre question, et la phrase « يُعدّ… العاملَ الأساسيَّ », qui serait une seconde قرينة juste, n'est pas parmi les options de Q5 : c'est bien.
  - Rien de bloquant. Optionnel : un leurre interne au texte en Q4 (voir C12).
- **m038 Q6 / Q7 : acceptable.** Seul un distracteur s'élimine d'une question à l'autre (تعليم, صيدلة, زراعة), et Q6 est une lecture directe de ses propres citations.
- **m037 Q7 → Q1 : inhérent, accepté.** La citation officielle contient « طلبات كثيرة في البيت », et la liste officielle de 4أ contient « كثرة الطلبات ». La question de titre de 2017 est facile par construction.

### § 2 — m036 Q7 : la clé se lit dans les extraits : MAJEUR, à corriger (C3)

- La citation contient « ثمّ تُسحَق…، يُخلَط بالماء » : la place du سحق est recopiée, et la question est étiquetée d3.
- Correctif : couper la citation après « غُبَارًا ». Le placement du سحق avant le خلط devient alors une inférence (le غبار est sec, on ne broie pas une pâte mouillée).
- Le تجفيف garde une moitié lue (« فإذا جفّت… تزيينها ») et une moitié inférée (après le تشكيل : il n'y a pas de مواعين avant).
- La structure 2×2 est saine : chaque demi-réponse figure deux fois, et l'option à deux erreurs est sans étiquette.

### § 3 — Citations à 3 fragments

- **m037 Q4 : réglé par C5**, qui ne garde que deux fragments.
- **m038 Q6 : acceptable.** Ce sont trois exemples courts, élidés par « … » (une trentaine de mots), pris dans un texte expositif de 17 lignes. Il n'y a pas de recopie longue, et le `multi` ne se pose pas sans eux.

### § 4 — m037 Q4 et Q8

- **« المسؤولية » chez le père : exacte.** Le tableau officiel 4أ compte 4 lignes de chaque côté. Les seuls traits du père sont الحيرة، المماطلة، الألم et المسؤوليّة (« أَوَدُّ أَنْ أُلَبِّيَ لَهُمْ… »).
- **m037 Q8 : la clé reposant sur la justification est acceptable**, et l'explication le dit. Défaut : b (« الأسرة لا تشاهد التلفاز ») et d (« إشهار يدعو إلى السلع الوطنية ») contredisent la citation de l'énoncé, et a est hors texte. La clé sort par élimination à vue, ce qui ne vaut pas un d3.
- Correctif C6 : un vrai 2×2 facteur × justification. Le leurre clé est « الإشهار » appuyé sur la bonne citation, qui ne le prouve pas.

### § 5 — m038 Q5 et Q7

- **Q5 : clé unique.**
  - Les exemples du نسيج et du بريد prouvent un remplacement d'ouvriers, et « دون أن يواكب » une absence d'emplois. Aucun ne lie **explicitement** la technologie au **taux** de chômage.
  - Mineur : l'élision « … » de la clé retire précisément « واستخدام التكنولوجيا المتطوّرة », que l'énoncé paraphrase (« الاعتماد على التكنولوجيا »). C'est aussi la seule option élidée, donc un marqueur de forme.
  - Restituer la phrase entière rendrait la clé strictement la plus longue (84 contre 80, mesuré). D'où le correctif C10 : énoncé recalé sur « تسارع التغيّر التكنولوجي », et « … » marqué dans l'option a, qui coupe le texte sans le signaler.
- **Q7 : « خدمية » au sens large.** Médecine, enseignement et banque sont des services. Le critère « لا ترد بلفظها » sauve la clé, mais l'explication doit le dire.
- **Défaut réel de Q7 : MAJEUR.** Seules les trois clés portent une parenthèse d'exemple (« (كالجراحة…) », « (كالتعلّم…) », « (كالصرّاف…) ») ; les leurres sont un mot nu. Correctif C9.

### § 6 — Écarts de graphie (vérifiés sur le PDF)

- **« كُومَةٌ » (m036 Q3 l3) : coquille de la transcription.** Le PDF porte **« كَوْمَةٌ »**, dans le texte comme dans la question 2ب. Le fichier est incohérent : Q3 écrit كُومة, Q4 a écrit كَوْمة. À aligner sur le PDF (C4), et `2015-technique.md` ligne 51 à corriger.
- **« المُفْضِيَةُ » (m038 Q2) : conforme à l'officiel.** La question imprimée porte « المفضية » (féminin), le texte « المُفْضِيَ » (masculin, épithète de العاملَ). La mission cite les deux fidèlement. Mineur : une glose dans l'explication (C11).
- **« بَذَلْتُ جُهْدِي » (m037 Q2) : phrase de la question 2أ, pas du texte.** Le texte dit « وأنا أَبْذُلُ قُصَارَى جَهْدِي…، دون جدوى ». Le PDF vocalise **« جَهدي »** (fatha) ; la transcription écrit جُهْدِي. Les deux lectures sont correctes en arabe, mais la fidélité veut « جَهْدِي ». La question présente la phrase sous « من نصّ… » : préciser qu'il s'agit de la phrase du sujet (C7).
- **Autres écarts de citation trouvés (m036) :**
  - Q4 a : « وَهُنَاكَ » au lieu de « **وَهُنَالِكَ** ».
  - Q4 b et Q5 c : « وَتُصْنَعُ مِنْهُ عَجِينَةٌ مُتَمَاسِكَةٌ » (passif, reconstruit) au lieu de « **وَتَصْنَعُ مِنْهُ خَالَتَايَ عَجِينَةً مُتَمَاسِكَةً** ». Une phrase donnée « من النصّ » doit être celle du texte (C4).
  - Q5 b : « وَكَانَتِ » contre « وَكَانَتْ » au PDF. C'est une coquille d'origine, à juste titre corrigée : à signaler seulement.

### § 7 — Ordre des étapes 2015 : conforme

- La liste imprimée de la question 5 compte huit étapes : تزيين، خلط بالماء، تشكيل، طرح في الشمس، عجن، تجفيف، سحق، جلب.
- Ordre du texte : جلب → طرح في الشمس → سحق → خلط بالماء → عجن (« تصنع منه… عجينة ») → تشكيل → تجفيف → تزيين.
- Q6 (6 étapes, sans سحق ni تجفيف) donne f d b e c a : exact. Q7 place les deux étapes absentes : exact. L'ordre est unique.

### § 8 — Rendu `dir=rtl` : RAS (voir en tête)

---

## 3. Défauts classés et correctifs exacts

Toutes les longueurs ont été mesurées par script, sans vocalisation. Aucun correctif ne rend une clé strictement la plus longue.

### Majeurs

**C1 — m036 Q8 (fuite vers Q4).**
- `prompt` : `من نصّ «نجل الفقير» لمولود فرعون (مناظرة 2015، تقنيّ):\n\n«يُمْكِنُ تَطْوِيرُ صِنَاعَةِ الخَزَفِ لِلتَّخْفِيفِ مِنْ عَنَاءِ الخَالَتَيْنِ».\n\nاخترْ كلَّ الاقتراحاتِ التي تخفّفُ عناءَ الخالتَينِ في صنعتِهما.`
- option a : `استعمالُ عربةٍ لنقلِ الطينِ بدلَ حملِه في القِفافِ`
- option f : `سحقُ الطينِ باليدِ مرّتَينِ ليصيرَ أنعمَ`
- clé inchangée : a, c, e.
- `explanation` : `ما يخفّفُ العناءَ ما يُبدِلُ جهدَ اليدِ والقدمِ بوسيلةٍ تقومُ به: عربةٌ تنقلُ الطينَ بدلَ القِفافِ، وآلةٌ تسحقُه، وعجلةٌ كهربائيّةٌ تشكّلُ الأواني. أمّا مضاعفةُ رحلاتِ الجلبِ، وتشكيلُ كلِّ الأواني في يومٍ بلا راحةٍ، وتكرارُ السحقِ باليدِ فكلُّها تزيدُ الجهدَ فتضاعفُ العناءَ ولا تخفّفُه.`

**C2 — m036 Q6, `explanation` (fuite vers Q4).** Remplacer `يُجلَبُ الطينُ أوّلًا من مكانِه البعيدِ، ثمّ` par `يُجلَبُ الطينُ أوّلًا، ثمّ`.

**C3 — m036 Q7 (lecture directe).**
- Dans `prompt`, remplacer `ثُمَّ تُسْحَقُ حَتَّى تَصِيرَ غُبَارًا، يُخْلَطُ بِالْمَاءِ»` par `ثُمَّ تُسْحَقُ حَتَّى تَصِيرَ غُبَارًا»`.
- `explanation` : `«ثمّ تُسحَقُ حتّى تصيرَ غبارًا» تأتي بعدَ طرحِ القطعِ في الشمسِ؛ والغبارُ يابسٌ، فالسحقُ يسبقُ الخلطَ بالماءِ ولا يأتي بعدَه، إذ لا يُسحَقُ طينٌ مبلولٌ. وتجفيفُ المواعينِ يأتي بعدَ تشكيلِها، فلا مواعينَ قبلَه، وقبلَ تزيينِها لأنّ النصَّ يقولُ: «فإذا جفّتِ المواعينُ وجبَ تزيينُها». ومن وضعَ السحقَ بعدَ الخلطِ أو التجفيفَ بعدَ التزيينِ خالفَ النصَّ.`
- `difficulty` 3 conservé : il y a désormais une inférence.

**C5 — m037 Q4 et Q5 (paire miroir).**
- **Q4** :
  - `prompt` : `من نصّ «حدّ السكّين على العنق» لبوراوي عجينة (مناظرة 2017، تقنيّ):\n\nيقولُ الراوي: «وَأَنَا أُمَاطِلُ مُتَعَلِّلًا أَنَّ الأَشْهُرَ الْقَادِمَةَ سَتَكُونُ أَفْضَلَ…»، و«أَظَلُّ صَامِتًا بَيْنَمَا الأَوْجَاعُ بِدَاخِلِي تَصْطَخِبُ وَتَتَلَاطَمُ».\n\nاخترْ كلَّ الصفاتِ التي تصدقُ على الأبِ لا على بقيّةِ أفرادِ الأسرةِ.`
  - options : a `المُمَاطَلَةُ`, b `التَّقْلِيدُ`, c `الأَلَمُ`, d `الانْبِهَارُ`.
  - `answerKey.correct` : `["a","c"]`.
  - `explanation` : `تُنسَبُ الصفةُ بقرينةٍ من النصِّ: الأبُ يماطلُ ويتعلّلُ بقدومِ أشهرٍ أفضلَ، ويكتمُ أوجاعًا تصطخبُ في داخلِه فهو في ألمٍ. أمّا التقليدُ والانبهارُ فلا قرينةَ عليهما في كلامِ الأبِ عن نفسِه.`
- **Q5** :
  - `prompt` : `من نصّ «حدّ السكّين على العنق» لبوراوي عجينة (مناظرة 2017، تقنيّ):\n\nينقلُ الراوي كلامَ أسرتِه: «أَبْدِلْ لَنَا السَّيَّارَةَ فَقَدْ قَدُمَتْ… أَوَانِي الْمَطْبَخِ مَضَتْ عَلَيْهَا سَنَوَاتٌ وَلَا بُدَّ مِنْ تَجْدِيدِهَا»، ثمّ يقولُ عن نفسِه: «أُنْصِتُ إِلَى الشَّكَاوَى وَالتَّأَوُّهَاتِ».\n\nاخترْ كلَّ الصفاتِ التي تصدقُ على بقيّةِ أفرادِ الأسرةِ لا على الأبِ.`
  - options : a `كَثْرَةُ الطَّلَبَاتِ`, b `الحَيْرَةُ`, c `الشَّكْوَى`, d `المَسْؤُولِيَّةُ`.
  - `answerKey.correct` : `["a","c"]`.
  - `explanation` : `أفرادُ الأسرةِ يطلبونَ تبديلَ السيّارةِ وتجديدَ أواني المطبخِ وغيرَ ذلك فطلباتُهم كثيرةٌ، والأبُ «يُنصتُ إلى الشكاوى» فالشكوى منهم. أمّا الحيرةُ والمسؤوليّةُ فصفتانِ للأبِ الذي يُطلَبُ منه ولا يقدرُ على التلبيةِ.`
- Pourquoi c'est sûr :
  - Les options des deux questions sont disjointes : aucun retour ne résout l'autre question.
  - Les 8 traits officiels sont tous employés.
  - Le leurre الألم n'est **pas** placé en Q5, où « التأوّهات » le rendrait défendable pour la famille.
  - Aucune citation n'est la justification de Q8, ni la clé de Q6.

**C6 — m037 Q8 (élimination à vue).**
- option b : `الإِشْهَارُ؛ لِأَنَّ الابْنَ وَالابْنَةَ يَتَذَمَّرَانِ لَمَّا يَرَيَانِ أَبْنَاءَ الحَيِّ بِمَلَابِسَ أَجْنَبِيَّةٍ`. Longueurs : 85 / 69 / 69 (clé) / 66. Le plan 2×2 est équilibré, et d (deux erreurs) reste sans étiquette.
- `explanation` : `المطلوبُ عاملٌ وتعليلٌ يسندُه النصُّ. العاملانِ كلاهما يمكنُ الدفاعُ عنه (فالإشهارُ يُعلَّلُ بإعلاناتِ التلفازِ التي تعرضُ أحدثَ السيّاراتِ والآلاتِ)، فالمعوَّلُ عليه أن يسندَ التعليلُ العاملَ المختارَ: تذمّرُ الابنِ والابنةِ إذ يريانِ ثيابَ أبناءِ الحيِّ يُثبتُ التقليدَ ولا يُثبتُ الإشهارَ. أمّا تقليدُ الأبِ جيرانَه فلا يقولُه النصُّ، وإشهارٌ يدعو إلى السلعِ الوطنيّةِ يناقضُه.`

**C8 — m037 Q1 (l'énoncé désigne les leurres comme des détails).** `prompt` : `من نصّ «حدّ السكّين على العنق» لبوراوي عجينة (مناظرة 2017، تقنيّ):\n\nيتكلّمُ الراوي، وهو أبٌ، عن أسرتِه: ابنُه وابنتُه يريدانِ ملابسَ بعلاماتٍ أجنبيّةٍ وهو يدعوهما إلى سلعٍ وطنيّةٍ، وزوجتُه تمتدحُ جاراتِها اللاتي يشترينَ من المغازاتِ الكبيرةِ، ولكلٍّ منهم حاجاتٌ يعجزُ الأبُ عن قضائِها.\n\nأيُّ العناوينِ الآتيةِ أنسبُ للنصِّ كلِّه؟` Le mot « طلبات » n'y figure pas, et rien ne fuit vers Q3 ni vers Q6.

**C9 — m038 Q7 (marqueur de forme).**
- options : b `الطبُّ`, d `التعليمُ`, f `البنوكُ`.
- `explanation` : `الجملةُ تسمّي الصناعةَ والزراعةَ والتجارةَ والخدماتِ، فهذه واردةٌ بلفظِها وليستْ جوابًا. وتبقى مجالاتٌ لم تُسمَّ بلفظِها، وإن دخلَ بعضُها في الخدماتِ بالمعنى الواسعِ، ويمكنُ أن تتأثّرَ بدخولِ الآلاتِ: الطبُّ حين يُجرى بعضُ العملِ بالإنسانِ الآليِّ، والتعليمُ حين يحلُّ الحاسوبُ محلَّ بعضِ المهامِّ، والبنوكُ حين يؤدّي الصرّافُ الآليُّ عملَ الموظّفِ.`
- Mineur : avec le critère « بلفظها », la tâche est lexicale. Je propose `difficulty` 2.

### Mineurs

- **C4 — fidélité des citations (m036).**
  - Q3 l3 : `كَوْمَةٌ`.
  - Q4 a : `وَهُنَالِكَ، فِي زَاوِيَةِ الْبَوَّابَةِ، كَوْمَةٌ ضَخْمَةٌ مِنَ الْحَطَبِ`.
  - Q4 b et Q5 c : `وَتَصْنَعُ مِنْهُ خَالَتَايَ عَجِينَةً مُتَمَاسِكَةً`. Longueurs vérifiées : Q4 44 / 30 / 39 / 36 (clé) ; Q5 30 (clé) / 49 / 30 / 30.
  - Corriger aussi la transcription `2015-technique.md` l. 51 (`كُومَةٌ` → `كَوْمَةٌ`).
- **C7 — m037 Q2.** Dans `prompt`, remplacer `\n\n«بَذَلْتُ جُهْدِي` par `\n\nجملةُ الامتحانِ: «بَذَلْتُ جَهْدِي`. Transcription `2017-technique.md` l. 44–45 : `جُهْدِي` → `جَهْدِي` (PDF).
- **C10 — m038 Q5.**
  - Dans `prompt`, remplacer `بين تزايدِ الاعتمادِ على التكنولوجيا وارتفاعِ نسبةِ البطالةِ` par `بين تسارعِ التغيّرِ التكنولوجيِّ وارتفاعِ نسبةِ البطالةِ`.
  - Option a : `فَكَمِّيَّةُ الْمَنْسُوجَاتِ الَّتِي كَانَ يُنْتِجُهَا عَدَدٌ مِنَ الْعُمَّالِ… أَصْبَحَ يُنْتِجُهَا عَامِلٌ وَاحِدٌ`. L'élision est ainsi marquée comme au PDF, et le « … » n'est plus propre à la clé.
- **C11 — m038 Q2.** Ajouter à la fin de l'`explanation` : ` (ووردتْ «المفضيةُ» في النصِّ بالتذكيرِ: «العاملَ الأساسيَّ المفضيَ»).`
- **C12 — m038 Q8.**
  - option d : `النموُّ السكّانيُّ السريعُ وتزايدُ الوافدينَ على سوقِ الشغلِ`. La version actuelle est presque la définition du chômage.
  - option e : `تراجعُ دخلِ الأسرِ التي فقدَ أفرادُها عملَهم`. « الفقر » peut se défendre comme cause, via la déscolarisation.
  - Dans l'`explanation`, remplacer `وزيادةُ الباحثينَ عن العملِ على الوظائفِ المعروضةِ` par `والنموُّ السكّانيُّ السريعُ الذي يزيدُ الوافدينَ على سوقِ الشغلِ`, et `والجريمةُ والانحرافُ والفقرُ نتائجُ للبطالةِ` par `والجريمةُ والانحرافُ وتراجعُ دخلِ الأسرِ نتائجُ للبطالةِ`.
  - Optionnel, m038 Q4 : remplacer le leurre d (hors texte) par `غِيَابُ وَظَائِفَ جَدِيدَةٍ تُعَادِلُ الوَظَائِفَ المُلْغَاةَ`, une condition secondaire du texte, ce qui correspond au piège de la carte. Contrepartie : il fait tomber un leurre de Q5.
- **m036 Q1 d** « تربية الماشية » : leurre de remplissage. Remplacer par `حَيَاةُ القَرْيَةِ` (trop large ; 11 contre 12 caractères pour la clé).
- **m036 Q2** : « من أصعبِ مراحلِ تشكيلِ الأواني » ajoute « أصعب », absent du texte, ce qui pousse vers la clé. Remplacer par `من تشكيلِ الأواني، وهو عملٌ يتطلّبُ انتباهًا شديدًا،`.
- **m037 Q7** :
  - Le leurre a (hors texte) est sans étiquette alors que b et c l'ont : ajouter `"misconceptionTag": "arabe.fahm.jawab-min-kharij-al-nass"`.
  - Les options a et c de l'officiel sont paraphrasées et allongées. C'est tolérable (cela évite que la clé soit la plus longue) ; à signaler au rapport d'auteur.
- **m038 Q4 d** : même incohérence d'étiquette que m037 Q7 a ; même correctif.
- **m038 Q3** : les leurres « أكلتُ الأنوالَ » et « زهرة عويصة » sont absurdes, mais ils testent bien le sens ; on peut les laisser.

### Étiquettes

- `arabe.fahm.tafsil-ka-fikra-amma` (m036 Q1 c, m037 Q1 a/b, m038 Q1 b) : exacte, le libellé « تفصيلة أو مثال… الفكرة العامّة » correspond.
- `arabe.lugha.ma3na-mashhur-bila-siyaq` (m036 Q2 a/b) : acceptable. C'est une lecture littérale d'une expression figée, proche du « sens le plus connu ».
- `arabe.fahm.jawab-min-kharij-al-nass` (m037 Q7, m038 Q4) : exacte.
- Aucune étiquette sur un `multi`, un `ordering` ou un `matching`, ni sur l'option à deux erreurs de m036 Q7.

### Doublons, notions, « ne pas redemander »

- Aucun doublon de gabarit (`content:tranche` : 0 groupe).
- Titre, synonymes et indice reviennent dans toutes les compréhensions du ch. 10 : c'est le format de l'examen, sur d'autres textes, ce qui ne constitue pas un doublon.
- Aucune notion hors programme (aucun item `HP` : 2015 Q3 et 2017 Q2ج/Q3 sont bien écartés).
- Étages d2 practice 75/15, rampe 1 → 3 : honnêtes.
- `sources[]` : la ligne générique des examens nationaux suffit.

---

## Résumé

- **24 questions re-résolues, 0 clé fausse.**
- **Majeurs : 7**, à corriger avant merge :
  1. m036 Q8 fuit vers Q4.
  2. L'explication de m036 Q6 fuit vers Q4.
  3. m036 Q7 se lit dans sa citation.
  4. m037 Q4/Q5 forment une paire miroir.
  5. m037 Q8 s'élimine à vue.
  6. L'énoncé de m037 Q1 désigne les leurres.
  7. Les parenthèses de m038 Q7 marquent les clés.
- **Mineurs : 10** — citations m036 (كَوْمَة, هنالك, عجينة active), m037 Q2 (جَهْدي et attribution), m038 Q5 (élision), Q2 (glose المفضية), Q8 (deux options), m036 Q1 d, m036 Q2, deux étiquettes manquantes.
- **Étiquettes justes.** Rendu RTL sans défaut. Gates verts.
- **Verdict : à corriger d'abord (fix-first).** Les correctifs C1 à C12 sont fournis tels quels, avec les longueurs vérifiées ; puis une re-vérification ciblée des trois fichiers.
