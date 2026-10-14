# Audit indépendant — gisement arabe 9ᵉ, lot L03 (production convertie, ch. 09, 7 missions, 53 questions)

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill
> `content-audit`), 2026-10-14. Périmètre : dans `/home/user/wt-argis` (branche
> `wip/gisement-arabe-9eme`, missions écrites au commit `d656e7e9`, inchangées à `adcdf30c`),
> `content/arabic/09-al-intaj-al-kitabi/exercices/07-*` à `13-*` et la ligne `sources[]` ajoutée au
> `chapter.json` du 09. Aucun fichier audité n'a été modifié ; les notes des auteurs n'ont pas été
> ouvertes.
>
> Sources lues : transcriptions officielles `examens-nationaux/9eme-base/arabic/` (2020, 2023, 2024,
> 2025, 2026 générale ; 2020 à 2026 technique) ; `PLAN.md` (R1–R5), `assign-arabe-L03.md`,
> `etiquettes-L03.json` ; `cours.md` et `resume.md` du 09 (en entier) et diff du `cours.md` du 10 ;
> note de lecture `lecture-101909/appareil.md` (définition du الحجاج, encadrés p. 313–315) ;
> `misconceptions.json` ; missions publiées `01…06` et `quiz.json` du 09.
>
> Contrôles outillés (moteur `eng-argis`, lien `content → wt-argis/content`) : `content:check` ✓ ;
> `content:qa --subject arabic` 0 erreur ; `content:tranche --chapters 09` : clé strictement la plus
> longue 0/71, 0 paire proche ; mesure maison sur les 37 QCM du lot : clé strictement la plus longue
> 0/37, strictement la plus courte 11/37 (30 %, hasard 25 %) — concentrée sur les items « formuler
> la thèse / la question » (11 Q2, 12 Q5, 13 Q3, 13 Q5) ; chiffres indo-arabes 0, LaTeX 0, `HP:` 0 ;
> `isolateLtrRuns` sur toutes les chaînes à chiffres + rendu Chromium `dir=rtl`
> (« مناظرات 2020–2022 (تقنيّ) », « (مناظرة 2024 تقنيّ) », « 40 من 50 », « 2020 و2021 و2022 ») :
> ordre affiché = ordre source ; citations « … » vocalisées comparées aux transcriptions (exactes).

Légende : **OK** · **ERREUR** (clé fausse) · **réserve** (défaut à corriger, clé juste). (M) majeur, (m) mineur.

---

## 1. `07-examen-2020-generale-intaj-hiwar-hijaji.json` — d3 boss 120/30, 7 q., rampe 1-2-2-2-3-3-3

Fidélité : 2020 générale, sujet unique (« الإنشاء العربي ») ; énoncé et consigne cités à
l'identique, « اُنْقُلِ » conforme.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | OK | — |
| 2 | d | d | OK | c (titre) / d (phrase) : bonne paire minimale |
| 3 | c | c | réserve (M) | gabarit « حجّة / تجريح / معك حق / تكرار » (§ G-1) ; l'énoncé énumère les catégories des distracteurs |
| 4 | b | b | réserve (M) | **a défendable** : « الفرد » lu comme le citoyen dont le dossier traîne → a couvre « فرد + مجتمع » |
| 5 (ordering) | b e d a c | b e d a c | OK | ordre unique (d « يخالف أخاه » et a « يردّ حجّة أخيه » exigent le tour du frère avant) |
| 6 (multi) | a b e | a b e | réserve (m) | 3 justes sur 6, comme les 6 autres `multi` du lot (§ G-3) |
| 7 | c | c | réserve (m) | gabarit de clôture « موضوع آخر يستحقّ » commun à 09 Q7 et 13 Q9 (§ G-4) |

**Point de l'auteur « 07 Q6, unicité de l'ordre »** : l'`ordering` de 07 est la **Q5** dans le
fichier (Q6 est le `multi`). Ordre unique — tranché OK. Le `multi` Q6 est juste lui aussi.

**C-07-1 (M) — 07 Q4, ambiguïté.** L'explication classe « مصالح المواطنين » (b) au compte de la
société mais « مصالح الناس » (a) aussi ; un élève qui lit « الفرد » = l'usager touché tient a pour
juste. Correctif (énoncé seul, options inchangées, clé b 73 car. non vocalisés, a 76, c 87, d 78) :

> طُلبَ من الراوي في مناظرة 2020 (عامّ) أن يُبرزَ مخاطرَ مغادرةِ الموظّفينَ مقرَّ العملِ قبلَ الوقتِ القانونيِّ «عَلَى الفَرْدِ وَالمُجْتَمَعِ». أيُّ الفقراتِ الآتيةِ تُبرزُ الخطرَ على الموظّفِ نفسِهِ (الفردِ) وعلى المجتمعِ معًا؟

Explication : remplacer « الخطرُ على الفردِ أن يفقدَ الموظّفُ ثقةَ رؤسائِه » par « الخطرُ على
الموظّفِ نفسِه (الفردِ) أن يفقدَ ثقةَ رؤسائِه » ; le reste tient.

## 2. `08-examen-2023-generale-intaj-iqna3-bi-athar-al-funun.json` — d3 boss, 7 q., rampe 1-2-2-2-2-3-3

Fidélité : 2023 générale, II- إنتاج نصّ حجاجي ; citations exactes.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 (multi) | a c e | a c e | OK | 3/6 (§ G-3) ; f « نصح … » = famille neuve 2 (§ E) |
| 2 (matching) | l1-r4 l2-r2 l3-r1 l4-r3 | idem | réserve (m) | l1 et l2 sont dans l'énoncé (d2 : acceptable) |
| 3 | c | c | OK | gabarit G-1 (variante sans injure) |
| 4 | b | b | OK | « قد يبدو … غيرَ أنّ » = exemple du cours § الإنتاج (2) |
| 5 | a | a | réserve (M) | **doublon de fait de `04-defi` Q1** (mêmes quatre options/justifications : تاريخيّة / واقعيّة / سلطة / عقليّة, même clé) |
| 6 | d | d | réserve (m) | grille 2×2 propre (chaque valeur deux fois) ; explication : « فالجوابانِ الآخرانِ » alors qu'il reste trois distracteurs, et c (inversion) n'est pas traité |
| 7 (ordering) | d c f a e b | idem | réserve (M) | f contient « والأهمُّ من ذلك » = **clé de 12 Q6** (fuite inter-questions, donjon) ; plan identique à `06-defi-concours` Q6 (m) |

**Point de l'auteur « 08 Q5 (أناشيد حركات التحرّر = تاريخيّة) »** : la clé est juste — événement
daté (le XXᵉ siècle) d'un passé que l'élève n'a pas vu ; ni قول مرجع ni observation. Mais l'item
duplique `04-defi` Q1. **Correctif C-08-1** — garder la donnée, ajouter la dimension « قرينة »
(grille 2×2, chaque valeur deux fois ; longueurs 40/41/42/39) :

> في مناظرة 2023 (عامّ) استشهدَ المُحاجُّ بما يلي دفاعًا عن أنّ الفنونَ تؤثّرُ في الشعوبِ: «في أثناءِ حركاتِ التحرّرِ في القرنِ العشرينَ رددتِ الشعوبُ أناشيدَ وطنيّةً شدّتْ عزائمَها ووحّدتْ صفوفَها». ما نوعُ هذه الحجّةِ، وما القرينةُ التي تحدّدُه؟

- a (clé) « حجّةٌ تاريخيّةٌ، وقرينتُها «في القرنِ العشرينَ» »
- b « حجّةٌ واقعيّةٌ، وقرينتُها «رددتِ الشعوبُ أناشيدَ» » — muette (deux erreurs)
- c « حجّةٌ تاريخيّةٌ، وقرينتُها «رددتِ الشعوبُ أناشيدَ» » — `arabe.hijaj.tarikhi-waqi3i-khalt` (le passé du verbe pris pour la marque historique : c'est la seconde moitié du libellé)
- d « حجّةٌ واقعيّةٌ، وقرينتُها «في القرنِ العشرينَ» » — `arabe.hijaj.tarikhi-waqi3i-khalt`

Explication : « الحجّةُ تاريخيّةٌ لأنّ دليلَها حدثٌ مؤرَّخٌ من الماضي، وقرينتُها الإطارُ الزمنيُّ «في القرنِ العشرينَ» الذي يضعُ الحدثَ في التاريخِ. أمّا «رددتِ الشعوبُ أناشيدَ» فوصفٌ للحدثِ بفعلٍ ماضٍ، وصيغةُ الماضي وحدَها لا تجعلُ الحجّةَ تاريخيّةً؛ وليستِ الحجّةُ واقعيّةً لأنّ المتكلّمَ لم يشاهدْ ما جرى في القرنِ الماضي ولم يجرّبْه. »

**C-08-2 (M)** — 08 Q7 f : « حجّةٌ داحضةٌ ثانيةٌ أقوى من الأولى يسندُها مثالٌ » (l'ordre reste
unique par « أولى / ثانية » ; explication : retirer la parenthèse « (وعبارةُ «والأهمُّ من ذلك» تعلنُ الأقوى) »).

**C-08-3 (m)** — 08 Q6 explication, dernière phrase : « ولا تدعمُ حجّةٌ واحدةٌ أطروحتَينِ متقابلتَينِ معًا ولا تدحضُهما معًا، وعكسُ الوظيفتَينِ يجعلُ الحجّةَ في خدمةِ الصديقِ وهي تهدمُ رأيَه. »

## 3. `09-examen-2024-generale-intaj-ankar-al-ananiyya.json` — d3 boss, 7 q., rampe 1-2-2-2-2-3-3

Fidélité : 2024 générale ; la phrase citée en Q1 est exacte (« فَرَفَض » sans voyelle finale = source).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | réserve (m) | d porte deux erreurs (thèse, et de l'autre partie) : la rendre muette |
| 2 | b | b | réserve (M) | gabarit G-1 (injure + « معكَ حقٌّ » + répétition), énoncé qui énumère les distracteurs ; « احتمى بقولِه «لا يمسّني» » partagé avec Q6 l1 (fuite de forme) |
| 3 (multi) | a c e | a c e | réserve (m) | 3/6 (§ G-3) |
| 4 | d | d | réserve (M) | **doublon de fait de `04-defi` Q2** (proverbe = سلطة ; « نوع مستقلّ », « تاريخيّة لأنّه قديم ») ; 13 Q4 l1 reteste le même fait ; b étiquetée `tarikhi-waqi3i-khalt` alors que l'erreur est « قديم ⇒ تاريخيّ » |
| 5 | c | c | réserve (m) | « يدافعُ المُحاجُّ عن هذه الحجّةِ » : on défend une thèse, on avance une حجّة → « يسوقُ المُحاجُّ هذه الحجّةَ » |
| 6 (matching) | l1-r3 l2-r1 l3-r4 l4-r2 | idem | réserve (m) | l1 reprend la formule-clé de Q2 |
| 7 | a | a | réserve (m) | gabarit de clôture G-4 |

**C-09-1 (M) — Q2.** Énoncé :

> في مناظرة 2024 (عامّ) يُطلبُ من المُحاجِّ أن يُنكرَ على صديقِهِ «أنانيّتَهُ» لأنّه يرى أنّ ما يجري في فلسطينَ لا يمسُّهُ شخصيًّا. أيُّ العباراتِ الآتيةِ تُنكرُ عليهِ أنانيّتَهُ بحجّةٍ عامّةٍ تردُّ تعليلَهُ؟

Options (b et d inchangées ; longueurs a 74, **b 72**, c 72, d 71 — clé ni la plus longue ni la plus courte) :
- a « رأيتُ في الأخبارِ أطفالًا يبحثونَ عن الماءِ بينَ الأنقاضِ، وما زالَ قلبي يتألّمُ لهم » — `arabe.hijaj.mithal-hujja-kafiya`
- c « التبرّعُ يحتاجُ إلى تنظيمٍ دقيقٍ يا صديقي حتّى تصلَ المساعداتُ كلُّها إلى مستحقّيها » — muette (حجّة hors cible)
Explication : « الإنكارُ الصالحُ حجّةٌ عامّةٌ تُبطلُ تعليلَ الصديقِ: من يقولُ «لا يمسّني» يغفلُ أنّ الظلمَ إذا لم يُردَعِ امتدَّ إلى غيرِ أهلِهِ. أمّا مشهدُ الأطفالِ في الأخبارِ فواقعةٌ تحرّكُ الشعورَ ولا تقدّمُ سببًا عامًّا يردُّ «لا يمسّني»، وتنظيمُ التبرّعاتِ حجّةٌ في مسألةٍ أخرى لا تمسُّ أنانيّةَ الصديقِ، و«يجبُ ألّا نكونَ أنانيّينَ» ترديدٌ للمطلوبِ بألفاظٍ أخرى دونَ سببٍ يسندُهُ. »

**C-09-2 (M) — Q4, remplacement** (on teste le قياس, enseigné § أنواع الحجج et absent des
missions publiées ; longueurs **a 54**, b 61, c 51, d 56) :

> في مناظرة 2024 (عامّ) استدلَّ المُحاجُّ على ضرورةِ التضامنِ بقولِه: «كلُّ محنةٍ تخفُّ إذا تقاسمَها الناسُ، والحربُ في فلسطينَ محنةٌ، فهي تخفُّ إذا تقاسمْناها بالتضامنِ». ما نوعُ هذه الحجّةِ؟

- a (clé) « حجّةٌ عقليّةٌ منطقيّةٌ (قياسٌ)، لأنّها تستخلصُ نتيجةً من مقدّمتَينِ »
- b « حجّةٌ عقليّةٌ منطقيّةٌ (استقراءٌ)، لأنّها تجمعُ حالاتٍ كثيرةً في حكمٍ عامٍّ » — muette
- c « حجّةُ سلطةٍ، لأنّها حكمةٌ مأثورةٌ يردّدُها الناسُ ويثقونَ بها » — `arabe.hijaj.naw3-al-hujja-khalt`
- d « حجّةٌ واقعيّةٌ، لأنّها تصفُ ما يشاهدُهُ المتكلّمُ في حياتِهِ اليوميّةِ » — `arabe.hijaj.naw3-al-hujja-khalt`
Explication : « الدليلُ استدلالٌ: مقدّمةٌ عامّةٌ («كلُّ محنةٍ تخفُّ إذا تقاسمَها الناسُ») ومقدّمةٌ خاصّةٌ («الحربُ في فلسطينَ محنةٌ») تُستخلَصُ منهما نتيجةٌ، فهي حجّةٌ عقليّةٌ منطقيّةٌ في صورةِ القياسِ. وليستِ استقراءً لأنّها لا تجمعُ حالاتٍ كثيرةً، ولا حجّةَ سلطةٍ لأنّ المُحاجَّ لا يستندُ إلى قولِ مرجعٍ ولا إلى مثلٍ، ولا واقعيّةً إذ لا مشاهدةَ فيها ولا تجربةَ. »
(Vérifié : aucune autre question du 09 ne porte de قياس à deux prémisses ; le titre ne livre rien.)

**C-09-3 (m) — Q6 l1** : « ليسَ من الإنصافِ أن يُغمضَ المرءُ عينَيهِ عن ألمِ غيرِهِ لأنّه بعيدٌ عنه » ;
explication : « الجملةُ الأولى تنفي أن يكونَ بُعدُ الألمِ عذرًا للإعراضِ عنه، فهي إنكارٌ لأنانيّةِ الصديقِ. »

## 4. `10-examen-2025-generale-intaj-ta3dil-al-mawqif.json` — d4 challenge 300/60, 8 q., rampe 1-2-2-3-3-3-3-3

Fidélité : 2025 générale ; énoncé et consigne exacts (« أُكْتُبْ », voir § F).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | réserve (M) | l'explication donne la clé de Q2 (et Q3) : fuite en avant |
| 2 | a | a | réserve (m) | son explication donne la clé de Q3 |
| 3 | c | c | réserve (M) | **doublon de Q2** (le « ما يُقرّ » = « حقّ المتخرّج في الكسب » dans les deux clés) ; injure (G-1) |
| 4 | b | b | OK | grille 2×2 (قد/ليس × غيرَ أنّ/بناءً على ذلك) propre |
| 5 | b | b | réserve (M) | doublon de fait de Q4 (même clé « للكسب مكانة + لكنّ ») ; d (« بناءُ الذاتِ ورقيُّ المجتمعِ في العملِ الحقيقيِّ … ») se lit comme une phrase nominale = la thèse officielle |
| 6 | d | d | réserve (M) | G-1 (injure + « معكَ حقٌّ ») ; réplique « قالَ الأخُ في مناظرة 2025 » inventée et attribuée au sujet (m) ; Q7 e redit la clé |
| 7 (multi) | a c e | a c e | réserve (M) | e ≈ clé de Q6 (fuite) ; 3/6 (G-3) |
| 8 (ordering) | d f b e a c | idem | réserve (M) | b + f donnent la clé de Q2 ; ordre unique seulement si le plan du تعديل est enseigné (il ne l'est pas) |

**Points de l'auteur.**
- **10 Q4 (« ليس… غيرَ أنّ » fausse faute d'إقرار)** : tranché OK. « ليسَ … أيُّ مكانةٍ » nie tout
  le موقف ; le استدراك qui suit ne contredit aucune attente (rien n'a été concédé) ; c est un ردّ
  كلّيّ, pas un تعديل. Étiquettes 2×2 : a muette (deux erreurs), c famille neuve 1, d
  `mu2ashshir-ghayr-munasib`.
- **10 Q8 (étapes 4/5)** : e (thèse corrigée) avant a (son argument) est l'ordre du plan de دحض du
  cours (« أقمْ أطروحتَكَ البديلةَ بحجّةٍ داعمةٍ ») et de 08 Q7, mais le plan du تعديل n'est écrit
  nulle part : un élève peut défendre d f b a e c (argument puis thèse) ou d e f b a c. Unique
  **après** la ligne de cours C-10-0 ci-dessous.
- **« تعديل الموقف », définition dans les énoncés** : « أن يُقرَّ المُحاجُّ بما فيه من صوابٍ ثمّ
  يصحّحَ ما فيه من خللٍ » est juste et suffit à résoudre chaque item (le manuel 101909 p. 12 nomme
  « تعديل موقفه » dans la définition du الحجاج et p. 315 « نتيجة : إثبات الأطروحة أو نفيها أو
  تعديلها »). Mais une notion que l'examen 2025 demande en production mérite le cours : **une ligne de
  cours vaut mieux** (C-10-0) ; la parenthèse peut alors rester en Q1 seule et tomber de Q2–Q8
  (charge de lecture : elle répète 7 fois 60 caractères).

**C-10-0 (M) — cours 09, § « ✍️ الإنتاجُ (2) »**, après le `::: retenir` de ce paragraphe, ajouter :

```
::: propriete
**تعديلُ الموقفِ** (قد يطلبُه الموضوعُ بدلَ الدحضِ: «تُعَدِّلُ فِيهِ هَذَا المَوْقِفَ»): لا تردُّ الرأيَ كلَّه ولا تقبلُه كلَّه، بل **تُقرُّ** بما فيه من صوابٍ ثمّ **تصحّحُ** ما فيه من خللٍ باستدراكٍ («قد … غيرَ أنّ …»)، فتصلُ إلى **أطروحةٍ معدَّلةٍ** تسندُها بحججٍ. ترتيبُه: عرضُ الموقفِ بأمانةٍ ← الإقرارُ بصوابِه ← الاستدراكُ ببيانِ خللِه ← الأطروحةُ المعدَّلةُ ← حججُها بأمثلتِها ← الاستنتاجُ. مثالٌ: «قد يكونُ السهرُ نافعًا في مراجعةٍ عاجلةٍ، غيرَ أنّ الاعتمادَ عليه وحدَه يُنهكُ الذهنَ؛ فالمراجعةُ المنتظمةُ هي الأساسُ.»
:::
```

et dans `resume.md`, après la puce du دحض : « - **تعديلُ الموقفِ**: إقرارٌ بصوابِه ثمّ استدراكٌ
يصحّحُ خللَه، فأطروحةٌ معدَّلةٌ بحججِها. ⚠️ ليس ردًّا كلّيًّا ولا قبولًا كلّيًّا. » (Exemple hors du
thème des missions, ne livre aucune clé.)

**C-10-1 (M) — Q1, explication** : « تطلبُ التعليمةُ «تُعَدِّلُ فِيهِ هَذَا المَوْقِفَ»، والتعديلُ إقرارٌ بما في الموقفِ من صوابٍ ثمّ تصحيحٌ لما فيه من خللٍ. فردُّ الموقفِ كلِّهِ دحضٌ لا تعديلٌ، وقبولُهُ كلِّهِ تأييدٌ لا تعديلٌ، والإقرارُ بلا تصحيحٍ يبقي الموقفَ على حالِه فلا يُقنَعُ الأخُ بأنّ العملَ الحقيقيَّ يبني الذاتَ والمجتمعَ. »

**C-10-2 (M) — supprimer Q3** (doublon de Q2 ; la mission passe à 7 questions, R2 respectée ; la
famille neuve 1 garde 4 questions). À défaut de suppression : il faudrait une autre compétence, et
toutes les voisines (thèse, connecteur, argument, ordre) sont déjà prises dans la mission.

**C-10-3 (M) — Q5** (options a et c inchangées ; longueurs a 76, **b 71**, c 71, d 68) :
- b (clé) « قيمةُ العملِ الحقيقيّةُ في بناءِ الذاتِ ورقيِّ المجتمعِ، لا في الكسبِ السريعِ وحدَهُ »
- d « العملُ الحقيقيُّ ودورُهُ في بناءِ الذاتِ وفي رقيِّ المجتمعِ وفي حياةِ المتخرّجينَ » (titre sans prédicat)
Explication : « الأطروحةُ المعدَّلةُ جملةٌ تُبقي للكسبِ مكانَه ولا تجعلُه وحدَه قيمةَ العملِ: «لا في الكسبِ السريعِ وحدَه» تُقرُّ به وتصحّحُ حصرَ القيمةِ فيه. فـ«قيمةُ العملِ هي الكسبُ …» رأيُ الأخِ نفسُه، و«لا ينبغي … على الإطلاقِ» ردٌّ كلّيٌّ لا تعديلٌ، و«العملُ الحقيقيُّ ودورُه …» عنوانٌ لا رأيَ فيه يُقبَلُ أو يُردُّ. »
Étiquettes : a `mahdhuda-muthbata-khalt`, c famille neuve 1 (au lieu de `sigha-ghayr-amina`), d `utruha-ism-aw-su2al`.

**C-10-4 (M) — Q6** (longueurs a 68, b 78, c 81, **d 74**) :

> لو اعترضَ الأخُ في موضوعِ مناظرة 2025 (عامّ) قائلًا: «ما دامَ الكسبُ السريعُ الوفيرُ يحلُّ مشاكلي اليومَ فما حاجتي إلى عملٍ يبني الذاتَ؟»، فأيُّ الردودِ الآتيةِ يسندُ أطروحتَكَ «العملُ الحقيقيُّ هو الذي يبني الذاتَ ويحقّقُ رقيَّ المجتمعِ» بحجّةٍ عامّةٍ تجيبُ عن اعتراضِه؟

- a « الشبكةُ مليئةٌ بفرصِ الربحِ السريعِ لمن يعرفُ كيف يغتنمُها في الوقتِ المناسبِ » — `arabe.hijaj.da3ima-dahida-khalt`
- b inchangée ; c « العملُ الحقيقيُّ هو الذي يبني الذاتَ، لأنّ قيمةَ العملِ في أنّه يبني ذاتَ صاحبِهِ قبلَ كلِّ شيءٍ » — `arabe.hijaj.i3adat-al-utruha-hujja` ; d inchangée (clé).
Explication : « الردُّ الصالحُ حجّةٌ عامّةٌ من خارجِ الأطروحةِ تجيبُ عن الاعتراضِ: الكسبُ الذي لا يقومُ على جهدٍ يزولُ سريعًا، وما يبنيه العملُ في صاحبِه من خبرةٍ يبقى. أمّا «الشبكةُ مليئةٌ بفرصِ الربحِ» فتسندُ رأيَ الأخِ لا أطروحتَكَ، و«لأنّ قيمةَ العملِ في أنّه يبني ذاتَ صاحبِه» تعيدُ الأطروحةَ بألفاظٍ أخرى ولا تضيفُ سببًا، وعبارةُ مواقعِ التواصلِ تنتقلُ إلى موضوعٍ آخرَ. »

**C-10-5 (M) — Q7** (multi, 4 justes sur 6) : e « من أتقنَ عملًا نافعًا اكتسبَ مكانةً بينَ الناسِ
لا يمنحُها المالُ وحدَهُ » ; f « العملُ المنتجُ يربطُ صاحبَهُ بالناسِ فيشعرُ بأنّه نافعٌ لمجتمعِهِ » ;
`answerKey.correct` = a, c, e, f. Explication : « تصلحُ حجّةً في التعديلِ كلُّ عبارةٍ تسندُ أنّ العملَ الحقيقيَّ يبني الذاتَ ويرقى بالمجتمعِ دونَ أن تنفيَ حقَّ الكسبِ: نموُّ المهاراتِ والثقةِ، ورقيُّ المجتمعاتِ بسواعدِ المنتجينَ، والمكانةُ التي لا يمنحُها المالُ وحدَه، والشعورُ بالنفعِ للمجتمعِ. أمّا «لا قيمةَ للكسبِ على الإطلاقِ» فيردُّ الموقفَ كلَّه، و«الأعمالُ على الشبكةِ أسهلُ» تسندُ رأيَ الأخِ. »

**C-10-6 (M) — Q8** : f « إقرارٌ بما في موقفِ الأخِ من صوابٍ » ; b « استدراكٌ بـ«غيرَ أنّ» يبيّنُ
موضعَ الخللِ في موقفِه » (ordre inchangé, unique avec C-10-0).

## 5. `11-examen-2026-generale-intaj-dahd-i3tiqad.json` — d3 boss, 7 q., rampe 1-2-2-2-2-3-3

Fidélité : 2026 générale ; citations exactes.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | OK | — |
| 2 | c | c | réserve (m) | clé strictement la plus courte (52 / 56–63) dans un gabarit où c'est récurrent (§ G-2) |
| 3 | c | c | réserve (M) | **doublon de `05-tadrib` Q6** (même cadre « أيُّ الافتتاحيّاتِ … تعرضُ … عرضًا أمينًا قبلَ الشروعِ في دحضِه », mêmes types d'options : injure-déformation, dahd d'emblée, clé, hors sujet) ; Q7 (1) redit la clé |
| 4 | a | a | réserve (M) | G-1 ; énoncé « لا بتجريحٍ ولا بتأييدٍ ولا بواقعةٍ وحدَها » = les trois distracteurs nommés |
| 5 (matching) | l1-r2 l2-r4 l3-r1 l4-r3 | idem | OK | — |
| 6 (multi) | a c e | a c e | réserve (M) | ses trois dangers individuels (قلق، استدانة، ثقة بالنفس) sont ceux du paragraphe de Q7 et l'explication les classe « فرد » → donne la clé de Q7 |
| 7 | b | b | réserve (M) | fuite depuis Q6 (voir ci-dessus) |

**Point de l'auteur « 11 Q7 (chasse à l'erreur) »** : clé unique et juste — (1) présente la
croyance, (2)(3) argumentent, (4) exemple, (5) conclusion par « إذن » ; seuls manquent les dangers
pour la société. Défaut : la fuite depuis Q6. **C-11-1 (M)** — dans le paragraphe, remplacer (3) et (4) par :
« (3) وأوّلُ ما يصيبُكَ أن تنشغلَ بصورتِكَ عن دروسِكَ، لأنّ الوقتَ الذي تُنفقُه في التمثيلِ يضيعُ من المراجعةِ. (4) وقد رأيتُ زميلًا ادّعى التفوّقَ شهورًا، فلمّا جاءَ الامتحانُ لم يجدْ في ذهنِه ما يكتبُه. »
Explication, fin : « … لكنّ ما تُبرزُهُ في (3) و(4) من أخطارٍ (الانشغالُ عن الدروسِ، والإخفاقُ في الامتحانِ) يقعُ على الفردِ وحدَهُ، ولا شيءَ فيها عمّا يصيبُ المجتمعَ. »
(Vérifié : aucune option de Q6 ni de Q4 ne porte ces dangers ; options de Q7 inchangées.)

**C-11-2 (M) — Q3, remplacement** (compétence de la consigne « خاطِبْ صديقَكَ » + إشراك القارئ,
enseigné § الصيغ التعبيريّة ; longueurs **a 65**, b 66, c 65, d 64) :

> تطلبُ تعليمةُ مناظرة 2026 (عامّ): «خاطِبْ صديقَكَ في نصٍّ حِجاجيٍّ منْ خمسةٍ وعشرِين سطرًا». أيُّ الجملِ الآتيةِ تخاطبُ الصديقَ وتُشركُه في الحكمِ كما يقتضي هذا المطلبُ؟

- a (clé) « ألا ترى معي يا صديقي أنّ من يُعرَفُ بصدقِهِ يُحترَمُ أطولَ ممّن يُعرَفُ بمظهرِهِ؟ »
- b « يرى بعضُ الشبابِ أنّ المظهرَ يضمنُ الاحترامَ، وهم مخطئونَ في ذلكَ كلَّ الخطأِ »
- c « كتبَ أحدُ الأدباءِ أنّ المظهرَ الزائفَ قناعٌ لا يدومُ طويلًا على وجهِ صاحبِهِ »
- d « أيّها الناسُ، احذروا كلَّ من يتظاهرُ بالغنى والتفوّقِ أمامَكم في المجالسِ »
Explication : « تطلبُ التعليمةُ «خاطِبْ صديقَكَ»، فالنصُّ موجَّهٌ إليه بضميرِ المخاطَبِ والنداءِ، ومن صيغِ ذلك إشراكُ القارئِ بالاستفهامِ «ألا ترى معي يا صديقي…؟» الذي يدعوه إلى التسليمِ بالحكمِ. أمّا «يرى بعضُ الشبابِ…» و«كتبَ أحدُ الأدباءِ…» فتتحدّثانِ عن غائبٍ ولا تخاطبانِ الصديقَ، و«أيّها الناسُ» نداءٌ لجمهورٍ عامٍّ لا للصديقِ. » (Options sans étiquette.)

**C-11-3 (M) — Q4, énoncé** : « في مناظرة 2026 (عامّ) أيُّ العباراتِ الآتيةِ تدحضُ اعتقادَ الصديقِ بأنّ التظاهرَ بالغنى والتفوّقِ يضمنُ الاحترامَ والتقديرَ، بحجّةٍ عامّةٍ؟ » (options inchangées ; « عامّة » écarte l'exemple c).

## 6. `12-examens-2020-2022-technique-tahrir-faqra.json` — d2 practice 75/15, 8 q., rampe 1-2-2-2-2-2-2-2

Fidélité : 2020, 2021, 2022 technique ; citations exactes (« أُكْتُبْ » 2020, « اُكْتُبْ » 2021/2022 = sources).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | OK | d « نصيحة … دون ذكر أسباب » → famille neuve 2 |
| 2 (multi) | a c e | a c e | réserve (m) | 3/6 (G-3) |
| 3 | d | d | OK | — |
| 4 | c | c | réserve (m) | distracteurs faibles (café, re-tenter, se plaindre) — acceptable en d2 |
| 5 | d | d | réserve (M) | la clé recopie mot pour mot la consigne citée dans l'énoncé (application directe) et est la plus courte (44 / 57–66) |
| 6 | d | d | réserve (M) | **doublon de `02-boss` Q1** (« والأهمُّ من ذلك » annonce l'argument le plus fort, et la clé de 02-boss le dit) + 08 Q7 f ; « وخلاصةُ القولِ كلِّهِ » forcé |
| 7 (ordering) | b d a c | idem | réserve (m) | trivial (ordinaux) ; b recopie la clé de Q5 |
| 8 (matching) | l1-r3 l2-r1 l3-r2 | idem | réserve (m) | chaque paire se fait par écho lexical (« أسباب أخرى », « حلول بديلة », « القمار ») |

**Point de l'auteur « 12 Q6 (« والأهمّ من ذلك » contre « معنى ذلك ») »** : la clé tient
(« ومعنى ذلك » serait un تفسير : perdre le respect de soi ne réexplique pas la perte de confiance des
proches) ; mais l'item duplique 02-boss Q1. **C-12-1 (M) — remplacement** (cœur de la consigne 2022 :
خسارة معنويّة vs مادّيّة ; longueurs **a 54**, b 52, c 57, d 56) :

> في مناظرة 2022 (تقنيّ) طُلبَ إقناعُ الصديقِ «بِأَنَّ الْقِمَارَ يَتَسَبَّبُ فِي خَسَائِرَ مَعْنَوِيَّةٍ لَا يُعَوِّضُهَا الْمَالُ». أيُّ الحججِ الآتيةِ تبيّنُ خسارةً من هذا النوعِ؟

- a (clé) « يخسرُ المقامرُ ثقةَ أهلِهِ به، فلا يصدّقونَ وعدَهُ بعدَ ذلكَ أبدًا »
- b « يخسرُ المقامرُ مدّخراتِهِ في ليلةٍ، فيعجزُ عن دفعِ ثمنِ كرائِهِ » — muette
- c « يربحُ المقامرُ أحيانًا مبالغَ كبيرةً، فيظنُّ أنّ الحظَّ حليفُهُ دائمًا » — `arabe.hijaj.da3ima-dahida-khalt`
- d « يبيعُ المقامرُ أثاثَ بيتِهِ ليسدّدَ ديونَهُ، ثمّ يشتري غيرَهُ إن ربحَ » — muette
Explication : « الخسارةُ المعنويّةُ ما يصيبُ النفسَ والعلاقاتِ ولا يُقاسُ بالمالِ: ثقةُ الأهلِ إذا ضاعتْ لم يردَّها ربحٌ. أمّا ضياعُ المدّخراتِ وبيعُ الأثاثِ فخسارتانِ مادّيّتانِ يمكنُ أن يعوّضَهما المالُ، وربحُ المقامرِ أحيانًا لا يبيّنُ خسارةً أصلًا بل يسندُ وهمَ الصديقِ. »

**C-12-2 (M) — Q5, clé d** : « ما يخسرُهُ المقامرُ في نفسِهِ وفي أسرتِهِ لا يردُّهُ إليه أيُّ ربحٍ مهما كبرَ »
(≈ 62 car., entre 57 et 66 ; ne nomme pas la « ثقة » de C-12-1). Explication : remplacer
« وهو هنا ما طلبتْهُ التعليمةُ: القمارُ يتسبّبُ … » par « وهو هنا أنّ ما يخسرُه المقامرُ في نفسِه وأسرتِه لا يعوّضُه ربحٌ ».
**C-12-3 (m) — Q7 b** : « جملةُ الأطروحةِ التي تفتتحُ الفقرةَ ».
**C-12-4 (m) — Q2** (2 justes sur 6) : e « رغبةُ العمّالِ في الراحةِ وتفضيلُهم البقاءَ في بيوتِهم » ;
`correct` = a, c ; explication : « … وضعفُ الأجرِ … وغيابُ الضمانِ الاجتماعيِّ. أمّا الكسلُ والتواكلُ والاستخفافُ وحبُّ الراحةِ فهي تفسيرُ الصديقِ نفسُه بألفاظٍ أخرى … » (supprimer « وبعدُ الحقولِ وغيابُ النقلِ »).

## 7. `13-examens-2023-2026-technique-tahrir-faqra.json` — d2 practice 75/15, 9 q., rampe 1-2-…-2

Fidélité : 2023–2026 technique ; citations exactes, coquilles d'origine reprises (§ F).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | OK | a = famille neuve 2 |
| 2 | b | b | réserve (m) | G-1 (variante) ; c « ممنوعٌ … يُعاقَبُ » = famille neuve 2 |
| 3 | d | d | réserve (m) | b (« التعلّمُ والتضحيةُ … من أجلِ النجاحِ … ») se lit aussi comme phrase nominale (خبر « من أجل النجاح ») ; clé la plus courte |
| 4 (matching) | l1-r2 l2-r4 l3-r1 l4-r3 | idem | réserve (m) | l1 (proverbe = سلطة) refait 04-defi Q2 / 09 Q4 |
| 5 | c | c | réserve (M) | clé = la consigne recopiée, la plus courte (51 / 63–65) |
| 6 (multi) | a c e | a c e | réserve (m) | 3/6 (G-3) |
| 7 | d | d | réserve (M) | G-1 ; énoncé identique à 11 Q4 (« لا بتجريحٍ ولا بتأييدٍ ولا بواقعةٍ وحدَها ») |
| 8 | c | c | OK | — |
| 9 | a | a | réserve (m) | G-4 (« وتجدرُ الإشارةُ إلى أنّ … يستحقُّ بحثًا ») |

**Point de l'auteur « 13 Q4 (« تعليم مجّاني بعد الاستقلال » = تاريخيّة) »** : tranché OK — fait
daté (la réforme qui suit l'indépendance), exactement le cas du cours « صدورُ مجلّةِ الأحوالِ
الشخصيّةِ سنةَ 1956 ». Paires uniques.

**C-13-1 (m) — Q3 b** : « الحرصُ على التعلّمِ والتضحيةُ في سبيلِهِ والنجاحُ والخروجُ من حالِ الفقرِ »
(suite de noms coordonnés, aucun prédicat ; paire minimale avec la clé : « و » / « طريقُ » ; 63 = 63).
**C-13-2 (M) — Q5 c** : « توعيةُ المستهلكينَ بخطرِ الإشهارِ عليهم حمايةً لمصالحِ الأسرةِ والمجتمعِ » (64 ; a 63, b 65, d 65).
**C-13-3 (M) — Q7** : énoncé « … أيُّ العباراتِ الآتيةِ تردُّ تعلّلَ الصديقِ بحجّةٍ عامّةٍ؟ » ; b « المالُ وإن كثرَ فمآلُهُ الزوالُ يا صديقي، لأنّ كلَّ مالٍ كثيرٍ يزولُ مهما كثرَ » — `arabe.hijaj.i3adat-al-utruha-hujja` (longueurs a 72, b 66, c 77, **d 77** : ni plus longue stricte ni plus courte). Explication : « … و«لأنّ كلَّ مالٍ كثيرٍ يزولُ» تعيدُ الأطروحةَ بألفاظٍ أخرى ولا تضيفُ سببًا … ».
**C-13-4 (m) — Q9 b** : « وهكذا انتهى حديثي مع صديقي في المقهى، فدفعَ ثمنَ القهوةِ وافترقْنا عندَ البابِ » — `arabe.hijaj.khutta-la-tuwafiq-al-matlub` (clôture narrative d'un dialogue à la place de la conclusion d'une فقرة ; 72 ; clé a 71).
**C-13-5 (m) — Q6** (2 justes) : e « التخفيضاتُ الموسميّةُ فرصةٌ يغتنمُها الجميعُ لشراءِ ما يعرضُهُ الإشهارُ » ; `correct` = a, c ; retirer « وترشيدُ الاستهلاكِ … » de l'explication et ajouter « والدعوةُ إلى اغتنامِ التخفيضاتِ تخدمُ الإشهارَ لا التوعيةَ ».

---

## G. Gabarits entre missions

- **G-1 (M) — « حجّة contre injure / تأييد / تكرار / مثال »** : 07 Q3, 08 Q3, 09 Q2, 10 Q3, 10 Q6,
  11 Q4, 13 Q2, 13 Q7 (+ publié 05-tadrib Q6). L'injure revient 7 fois (« كلامُكَ ساذجٌ », « أنتَ
  أنانيٌّ », « كلامُ الكسالى », « مدّعٍ مهرّجٌ », « عالةٌ وكسولٌ »…) et « معكَ حقٌّ يا أخي/صديقي » 3 fois :
  deux distracteurs s'éliminent à vue dans tout le lot. Correction : garder le gabarit complet en
  07 Q3 et 11 Q4 seulement, sans énumération dans l'énoncé (C-11-3 ; 07 Q3 : « … أيُّ الردودِ الآتيةِ
  يدحضُ حجّةَ الأخِ بحجّةٍ عامّةٍ؟ ») ; ailleurs C-09-1, C-10-2, C-10-4, C-13-3. Garder « عامّة » dans
  tout énoncé « بحجّة » qui a un exemple parmi les options : sans lui, une واقعة seule est une
  « حجّة واقعيّة » au sens du cours (§ أنواع الحجج).
- **G-2 (m) — formulation de la thèse** (07 Q2, 11 Q2, 12 Q5, 13 Q3 ; + 10 Q5, 13 Q5) : même plan
  (thèse adverse / généralisation / titre / clé) ; acceptable car les données changent, mais la clé
  est la plus courte dans 4 cas ; C-12-2, C-13-1, C-13-2 ramènent la clé dans la plage.
- **G-3 (M) — `multi`** : les 7 `multi` ont 3 justes sur 6 → le nombre se déduit. C-10-5 (4),
  C-12-4 (2), C-13-5 (2), et 07 Q6 f « تخصيصُ وقتٍ للراحةِ وللأسرةِ بعدَ الدوامِ يجدّدُ طاقةَ الموظّفِ »
  (4 justes : a, b, e, f ; explication : ajouter « وتخصيصُ وقتٍ للراحةِ والأسرةِ »).
- **G-4 (m) — clôtures** 07 Q7, 09 Q7, 13 Q9 : même distracteur « sujet nouveau » ; C-13-4 suffit.

## E. Étiquettes

Posées (`misconceptions.json`) : 16 ids, tous existants ; libellés exacts sauf :
- 09 Q4 b `tarikhi-waqi3i-khalt` (moot si C-09-2) ; 09 Q1 d à rendre muette (deux erreurs) ;
- 10 Q1 a `khutta-la-tuwafiq-al-matlub` et 10 Q5 c `sigha-ghayr-amina` → famille neuve 1 ;
- 12 Q6 (si conservé) : `tadarruj-wa-rawabit-khalt` nomme « والأهمُّ من ذلك », mieux que le générique ;
- 12 Q3 a `mahdhuda-bila-badila` (« thèse de remplacement ») pour un plan sans « حلول بديلة » : analogie lâche, (m).

Familles neuves (`etiquettes-L03.json`) :
1. `arabe.hijaj.ta3dil-ila-radd-aw-taqrir` — **à adopter**, avec C-10-0 (sinon elle cite une notion
   non enseignée). Une seule erreur (ne pas nuancer, dans un sens ou l'autre). À poser sur 10 Q1 a, c ;
   Q2 c, d ; Q4 c ; Q5 c ; Q7 b → 5 questions distinctes (Q3 supprimée).
2. `arabe.hijaj.nawahi-bila-ta3lil` — **atteint le seuil dans le lot** : 13 Q1 a, 13 Q2 c, 12 Q1 d
   (« نصيحةٌ للعمّالِ … دونَ ذكرِ أسبابِ نفورِهم »), 08 Q1 f (« نصحُ صديقِكَ بحضورِ العروضِ ») =
   4 questions, une erreur (prescrire sans justifier). À adopter.

## F. Fidélité, coquilles, sources

- Citations : toutes exactes ; les répliques inventées sont introduites comme hypothèses
  (« استشهدَ », « كتبتَ »), sauf 10 Q6 (« قالَ الأخُ في مناظرة 2025 ») → C-10-4.
- Coquilles d'origine : **les corriger**, ce sont des fautes que le programme enseigne et pas des
  données : « أُكْتُبْ » → « اُكْتُبْ » (10 Q1, 12 Q1, 13 Q5 ; همزة وصل), « أَهَمِّيَةَ » → « أَهَمِّيَّةَ »
  (13 Q5 ×2, Q6), « لِلإِشْهَارِ . » / « وَالمُجْتَمَعِ . » → sans espace (13 Q5 ; l'espace laisse le
  point seul en début de ligne au retour), « و الخُرُوجِ » → « والخُرُوجِ » (13 Q3). Les variantes non
  fautives (« مُقْتَرِحاً », « لاَ ») restent.
- **`chapter.json`, sources (M)** : la ligne « … — الصيغ فقط، ولا نصّ ولا جملة منها » contredit la
  reprise citée des missions 07–13, et est fausse sur les faits (2020 générale est encore « الإنشاء » ;
  la technique va de 2020 à 2026, pas « دورة 2022 » seule). Texte proposé :
  « مواضيعُ الإنتاجِ في امتحانِ شهادةِ ختمِ التعليمِ الأساسيِّ، نسختُه العامّةُ (الإنشاءُ حتّى دورةِ 2020، ثمّ إنتاجُ نصٍّ حجاجيٍّ من خمسةٍ وعشرينَ سطرًا من 2023 إلى 2026) ونسختُه التقنيّةُ (تحريرُ فقرةٍ من عشرةِ أسطرٍ، من 2020 إلى 2026): في الدرسِ صيغُها فقط، وفي المهامِّ 07 إلى 13 تُنقلُ تعليماتُها حرفيًّا بينَ «…» مع ذكرِ الدورةِ (مدوّنةٌ رسميّةٌ، إعادةُ استعمالٍ موثّقةٌ) »
  et compléter la ligne suivante : « … دونَ اقتباسٍ، عدا تعليماتِ الامتحانِ المنقولةِ في المهامِّ 07 إلى 13 ».
  La ligne neuve en français peut rester (même forme que les autres chapitres du gisement).

## Étages

07, 08, 09, 11 : d3 boss 120/30 ; 10 : d4 challenge 300/60 ; 12, 13 : d2 practice 75/15 —
conformes à l'assignation ; rampes non décroissantes ; titres ⭐ justes, aucun ne livre de clé.

## Chiffre final

53 questions auditées (37 QCM, 7 `multi`, 5 `matching`, 4 `ordering`) re-résolues à l'aveugle :
**0 clé fausse**. **1 distracteur défendable** (07 Q4). 19 questions à reprendre en majeur
(07 Q3, 07 Q4, 08 Q5, 08 Q7, 09 Q2, 09 Q4, 10 Q1, 10 Q3 [supprimer], 10 Q5, 10 Q6, 10 Q7, 10 Q8, 11 Q3,
11 Q4, 11 Q7 [via son paragraphe], 12 Q5, 12 Q6, 13 Q5, 13 Q7) + 07 Q6 (G-3) ; une quinzaine de
mineurs (tableaux) ; 1 ligne de cours + 1 puce de résumé (C-10-0) ; `chapter.json` sources ; coquilles
d'origine à corriger. Verdict : **corriger d'abord**.
