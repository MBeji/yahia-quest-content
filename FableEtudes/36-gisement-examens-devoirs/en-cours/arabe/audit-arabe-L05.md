# Audit indépendant — gisement arabe 9ᵉ, lot L05 (morphologie et révision)

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills `content-audit` +
> `content-accepted-answers`), 2026-10-14. Périmètre : 7 missions, 49 questions, dans `/home/user/wt-argis`
> (branche `wip/gisement-arabe-9eme`), état du disque au moment de l'audit. **Aucun fichier audité n'a été
> modifié** ; notes d'auteurs non ouvertes.
>
> Sources lues : transcriptions officielles `examens-nationaux/9eme-base/arabic/` 2021-T, 2022-T, 2023-G, 2023-T,
> 2024-G, 2024-T, 2025-G, 2025-T, 2026-G, 2026-T ; `assign-arabe-L05.md`, `PLAN.md` (règle de placement : 01 et 06
> « antérieurs à tous ») ; `cours.md` des chapitres 01, 05, 06, 12, 13, 14 ; notes de lecture 101908 L164, L169 ;
> `misconceptions.json` ; manifeste `9eme-base.json` ; moteur `free-answer.ts` (normalisation `short_answer`).
> PDF officiel 2026 générale téléchargé (sha256 `9b5c567c…` = celui de la transcription), page 1 rendue à 200 dpi.
>
> Gates (moteur `eng-argis`, corpus lié) : `content:check` ✓ ; `content:qa:strict` 0 erreur ; `content:tranche`
> (ch. 01, 05, 06, 12, 13, 14) : aucune paire proche ni candidat gabarit ne touche les 7 fichiers ; clé strictement
> la plus longue : **0 / 37 QCM** du lot.

Légende verdict : OK · **ERREUR** (clé fausse ou double réponse) · réserve (défaut hors clé).

---

## 1. `12-al-maqsur-wal-manqus-wal-mamdud/exercices/06-examens-2025-2026-maqsur-mamdud-muthanna-jam3.json` (d3, 6 q.)

Données : 2026-G Q4 (paragraphe entre crochets) et 2025-G Q6 أ — fidèles à la transcription. « المَهْبطِ » : vérifié
sur le PDF officiel, le ب y est bien non vocalisé (« المهبطِ ») — **pas une coquille**, la mission est fidèle.

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | السّماء | b | OK | seul ممدود du paragraphe |
| 2 | الأدنى + الأعلى | b,d | OK | « إلى » mabni, bon piège |
| 3 | الأَدْنَوْنَ | c | OK | étiquette `hamza-fi-muthanna-wal-jam3` exacte ; gabarit voisin de 02-boss Q5 (المصطفَون), justifié : c'est la demande officielle 2026 |
| 4 | السّماءان + السّماوان | a,c | réserve (m) | juste (cours l. 311/344 : exemple « سماء » du cours lui-même) → étage d2 honnête, pas d3 |
| 5 | خطوتين أوليين | a | réserve (M) | clé juste, plan 2×2 propre (b muet) ; « أُوْلَوَيْنِ » = distracteur légitime, étiquette exacte ; mais son explication donne la clé de Q6 |
| 6 | تُقلب ياءً (>3 lettres) | d | réserve (M) | doublon de fait de Q5 + fuite en avant (Q5 d3 → Q6 d3, ordre stable) |

## 2. `05-sarf-al-mizan/exercices/07-examens-2024-2026-maani-az-ziyada-istahala-tujammil.json` (d3, 7 q.)

Données : 2024-G Q5 (استحال / حمل → بذل الجهد), 2026-G Q5 (تُجمّل, يترفّع) — fidèles.

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | استفعل, 3 éléments | b | OK | a = erreur nommée par le libellé même de `wazn-qarib-khalt` |
| 2 | التحوّل | c | OK | |
| 3 | تَحَمَّلَ | a | réserve (M) | explication : fuite vers Q5 (« حمّل … للجعليّة ») + affirmation lexicale fragile sur « تحامل » |
| 4 | تُفَعِّلُ / الجعليّة | d | OK | 2×2, c muet |
| 5 | d | d | OK | clé donnée par l'explication de Q3 (voir M2) |
| 6 | يَتَفَعَّلُ | c | OK | |
| 7 | مُجَمِّل, تَجْمِيل, مُجَمَّل | b,d,e | OK | point auteur : rien à reprendre — « أَجْمَلُ » est un اسم تفضيل (ch. 06, antérieur), « مُجَمَّل » régulier |

## 3. `05-sarf-al-mizan/exercices/08-examens-2022-2025-maani-tafa3ul-iftia3l-mamdud.json` (d2, 7 q.)

Données : 2022-T Q5 ج (liste officielle de 7 mots), 2023-G Q4 أ et Q5, 2025-G Q6 ب, 2023-G texte (ارتقى) — fidèles ;
« مُؤْتَمَرٌ » retiré de la liste officielle de 2022 : **retrait justifié** (ائْتَمَرُوا بِهِ = تآمروا, il serait défendable).

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | مُسَاهَمَةٌ | b | réserve (M) | doublon de gabarit avec 06/07 Q3 (« مصدر غادر (فاعل) » → مغادرة, item officiel) dans la même tranche |
| 2 | تفاعل / المشاركة | c | OK | 2×2 propre |
| 3 | افتعل | a | OK | point auteur : racine (ه ز ز) donnée dans l'énoncé, et le sujet 2023-G Q4 أ demande lui-même ce poids → soluble, rien à reprendre |
| 4 | تعاونّا | d | réserve (m) | explication : « جمّلنا … جعل الشيء جميلا » livre la clé de 05/07 Q4 (autre mission, même chapitre) |
| 5 | اكْتِفَاءٌ | (sa) | réserve (M) | clé juste ; normalisation : « اكتفاء/الاكتفاء/إكتفاء » acceptés, « كفاية » refusé ; aucune variante juste manquante ; mais l'explication livre le mécanisme de Q7 |
| 6 | مؤامرة, تآمر, تآمرت | b,d,f | réserve (m) | clé = corrigé officiel ; l'énoncé et l'explication présentent « مؤامرة » comme dérivé de « تآمر » (c'est le مصدر de « آمَرَ », مُفاعَلة — Q1 l'enseigne) |
| 7 | منقلبة عن ياء | d | OK | (ر ق ي) |

## 4. `13-at-tasghir/exercices/06-examens-2025-2026-tasghir-qubayl-fann-shair.json` (d2, 7 q.)

Données : 2025-G Q5 (قبلَ), 2026-G Q6 (فنّ, شاعر) — fidèles.

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | قُبَيْلَ | b | réserve (M) | explication nomme « فُعَيْل » = clé de Q2 (fuite en avant) |
| 2 | فُعَيْلَ | c | OK | |
| 3 | فُنَيْنٌ | (sa) | réserve (M) | clé juste, `expectedMistakes` propres (فُنَيّ, فُنَيْنة) ; explication nomme « فُعَيْل » = clé de Q4 |
| 4 | فُعَيْلٌ | a | réserve (m) | explication : « فُعَيِّل … كِتاب ← كُتَيِّب » contredit le cours (l. 289 : كُتَيِّب est sur فُعَيْعِل) |
| 5 | بُعَيْدَ الظّهر | d | réserve (m) | juste ; item non tiré du sujet, gabarit proche de 03-revision (قُبَيْل الفجر) et 05-entrainement (دُوَيْن) |
| 6 | شُوَيْعِرٌ | (sa) | réserve (M) | clé juste ; explication nomme « فُعَيْعِل » = clé de Q7 |
| 7 | فُعَيْعِل (صيغة التصغير) | d | **ERREUR (double réponse)** | « فُوَيْعِلٌ » (b) est le **ميزان صرفي** exact de شُوَيْعِر selon la règle du ch. 05 (les زوائد s'écrivent telles quelles dans le poids) ; le manuel lui-même range كُوَيْتِب/خُوَيْلِد/شُوَيْعِر dans un groupe à part de دُرَيْهِم (L164, مدخل 3) |

## 5. `14-an-nisba-wal-masdar-as-sinai/exercices/06-examens-2023-2024-nisba-masdar-sinai-inna.json` (d3, 6 q.)

Données : 2023-G Q4 ب (الجميل), 2024-G Q6 أ et ب, texte 2024 — fidèles.

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | جَمِيلِيَّةٌ | b | réserve (m) | point auteur tranché ci-dessous ; explication appelle « جمالية » « منسوبة » |
| 2 | « الوطنيّةُ شعورٌ » | c | OK | |
| 3 | « بالأعلام الوطنيّة » | a | réserve (M) | question miroir de Q2 (même discrimination, clé inversée) : l'explication de Q2 la résout |
| 4 | المدنيّة, الفلسطينيّة, العسكريّة | b,d,e | **ERREUR (double réponse)** | « تتضمّن ياءَ نسبةٍ » : « هُوِيَّة » contient la ياء مضاعفة مسبوقة بكسرة que le manuel appelle **ياء النّسبة** (خلاصة p. 171) — le مصدر صناعي se forme avec elle ; cocher a est défendable. + explication « (إلى المدينة) » = clé de Q5 |
| 5 | مَدِينَةٌ | (sa) | réserve (M) | clé juste (« المدينة » ajouté par le Tier A) ; l'explication ne nomme jamais la clé (« مؤنّث مفرد كبير يسكنه الناس ») ; inverse de 05-entrainement Q2 (m) |
| 6 | إنّ موقفَه تحدٍّ | d | OK | rappel de « إنّ » nécessaire (HP), manqus = vrai enjeu ; 2×2 |

**Point auteur 14 Q1** : la clé « جَمِيلِيَّةٌ » est juste **sous la contrainte de l'énoncé** (« من لفظ «الجميل»
نفسه ») et conforme à la définition du manuel (اسم + ـيّة) ; « جَمَالِيَّةٌ » est le mot usuel mais il est formé sur
« جمال » : ce n'est pas une seconde réponse ici, et l'étiquette `nisba.min-kalima-ukhra` nomme exactement l'erreur. À
garder, avec l'explication corrigée (m8) pour ne pas laisser croire que « جمالية » est fautif en soi. (Corrigé
officiel 2023 introuvable en ligne : si l'orchestrateur le retrouve et qu'il donne « الجماليّة », reprendre la question.)

## 6. `06-al-mushtaqqat/exercices/07-examens-2024-2026-mushtaqqat-mazid.json` (d3, 10 q.)

Données : 2024-T Q6 (tableau : **مصدر** de أحلم et غادر, اسم الفاعل de خفّف, اسم المفعول de التقط), 2025-T Q6 ب
(تبادل), 2026-T Q7 (معتمد, زاحم, تحصيل, المتألّمون).

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | مُخَفِّفٌ | b | OK | |
| 2 | مُلْتَقَطٌ | c | OK | |
| 3 | مُغَادَرَةٌ | (sa) | réserve (M) | clé juste, `إغدار` refusé ; mais مصدر du مزيد enseigné au ch. 05 seulement (voir M10) |
| 4 | حَالِمٌ | a | réserve (M) | juste, mais **infidèle** : le sujet demande le **مصدر** de « أحلم » ; sa réponse officielle (« حُلْم ») est ici un distracteur |
| 5 | l1-r3, l2-r1, l3-r2 | idem | OK | (l3 : voir M10) |
| 6 | مُزَاحِمٌ / مُزَاحَمَةٌ | d | OK | point auteur : « زَحْمٌ » est bien le مصدر attesté de « زَحَمَ », étiquette `masdar.wazn-fi3l-akhar` exacte ; « زِحام » (2ᵉ مصدر de زاحم) absent des options → pas d'ambiguïté |
| 7 | مُعْتَمَدٌ | d | OK | |
| 8 | اعْتِمَادٌ | (sa) | OK | `تعمّد` refusé ; rien à ajouter |
| 9 | مُحَصَّلٌ | c | OK | |
| 10 | تَأَلُّمٌ | b | OK | |

## 7. `01-i3rab-wal-bina/exercices/07-examens-2021-2026-i3rab-muthanna-asma-khamsa.json` (d3, 7 q.)

Données : 2021-T Q3 أ, 2023-T Q5 أ et Q6 ب, 2026-T Q6 أ — fidèles ; accord donné en prémisse (HP), conforme au plan.

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | وَحِيدَتَيْنِ | b | réserve (m) | d « وحيدات … لثلاث فأكثر » s'élimine par la prémisse « الفتاتين » |
| 2 | c | c | réserve (M) | doublon de 01/06-defi-concours Q6 (« قال تلميذ: الماضي معرب لأنّ آخره يتغيّر… ») |
| 3 | لن تمشيا | a | réserve (m) | point auteur : la règle est donnée puis appliquée → **d1**, pas d2 (rappel indispensable : الأفعال الخمسة non enseignés au ch. 01) |
| 4 | الياء | d | OK | |
| 5 | الألف | d | OK | |
| 6 | c | c | réserve (M) | énoncé double (« في العدد وعلامة الرفع ») : la clé ne donne pas la marque, seule option sans elle |
| 7 | b,d | b,d | réserve (M) | `multi` à paires : une seule forme juste par case → nombre de réponses déductible ; « الموصولَ والفعلَ والضميرَ يتبعانِ » = duel pour trois sujets |

---

## Défauts classés et correctifs

Toutes les options proposées ont été mesurées par script (clé jamais strictement la plus longue ; tableau en fin
de section) ; aucune ne nie une prémisse ni ne fuit vers une autre question du fichier.

### Critiques — double réponse (2)

**C-1 · 13 Q7** — « فُوَيْعِلٌ » est le poids morphologique exact de شُوَيْعِر selon le ميزان du ch. 05.
Remplacer l'option b et l'énoncé, réécrire l'explication :
- énoncé : `أيُّ هذه الأوزانِ هو وزنُ صيغةِ التصغيرِ من «شَاعِرٌ» الواردِ في مناظرة 2026؟`
- b : `فُعَيِّلٌ` — `misconceptionTag: arabe.tasghir.alif-hukm-khalt`
- explication : `لصيغةِ التصغيرِ ثلاثةُ أوزانٍ يختارُها عددُ حروفِ الاسمِ: ثلاثةٌ ← «فُعَيْل»، أربعةٌ ← «فُعَيْعِل»، خمسةٌ ← «فُعَيْعِيل». و«شَاعِرٌ» أربعةُ أحرفٍ (ش ا ع ر)، والألفُ الزائدةُ تُعَدُّ حرفًا، فوزنُ صيغةِ تصغيرِه «فُعَيْعِل». و«فُعَيِّل» ليس من الأوزانِ الثلاثةِ: من اختارَه جعلَ ألفَ «شاعر» ياءً مدغمةً كما في «كُتَيِّب»، وهذا حكمُ حرفِ اللّينِ الثالثِ لا الثاني. و«فُعَيْل» لثلاثيٍّ، و«فُعَيْعِيل» لخماسيٍّ.`

**C-2 · 14 Q4** — « هُوِيَّة » contient la ياء النسبة du manuel. Remplacer l'énoncé et l'explication (supprime aussi la
fuite vers Q5) :
- énoncé : `في نصّ مناظرة 2024 وردت التراكيبُ الآتيةُ: «حَيَاتِهِ المَدَنِيَّةِ»، «المُقَاوَمَةِ الفِلَسْطِينِيَّةِ»، «البِذْلَةَ العَسْكَرِيَّةَ»، «مَسْأَلَةَ انْتِمَاءٍ وَهُوِيَّةٍ»، «كَمْ مِنَ المُهَجَّرِينَ وَالمُشَرَّدِينَ فِي هَذِهِ الدُّنْيَا حَبَسُوا مَآقِيهِمْ». اختر كلَّ كلمةٍ هي صفةُ نسبةٍ.`
- explication : `صفةُ النسبةِ اسمٌ لحقته ياءٌ مضاعفةٌ مسبوقةٌ بكسرةٍ تدلُّ على الانتسابِ، ويقعُ نعتًا: «المَدَنِيَّةِ» و«الفِلَسْطِينِيَّةِ» و«العَسْكَرِيَّةَ» صفاتٌ تنعتُ ما قبلَها وتدلُّ على انتسابِه. أمّا «هُوِيَّةٍ» فاسمُ معنًى مجرّدٍ، أي مصدرٌ صناعيٌّ، معطوفٌ على «انْتِمَاءٍ» لا نعتٌ؛ و«مَآقِيهِمْ» جمعُ «مَأْقٍ» ياؤُه من بنيةِ الجمعِ ولا ياءَ مضاعفةَ فيه. والاختبارُ: انزعِ الياءَ، فإن بقيَ اسمٌ يُنتسَبُ إليه وكانت الكلمةُ صفةً لما قبلَها فهي صفةُ نسبةٍ.`

### Majeurs (13)

**M1 · 12 Q5/Q6** — Q6 redemande la règle que l'explication de Q5 énonce (doublon de fait + fuite). Remplacer Q6 par
la mise au duel de l'autre مقصور du sujet 2026, et la **placer avant** l'actuelle Q5 (échanger les positions 5 et 6) :
- énoncé : `في نصّ مناظرة 2026 (أحمد حسن الزيّات، وحي الرسالة): «أَيَظَلُّ في المصْعَدِ الأَعْلَى مِنَ السّمَاءِ …». الاسمُ المقصورُ «الأَعْلَى» من الجذرِ (ع ل و). ما مثنّاه في حالةِ الرفعِ؟`
- options : a `الأَعْلَيَانِ` (clé) · b `الأَعْلَوَانِ` — `arabe.maqsur.radd-alif-bila-3add` · c `الأَعْلَاءَانِ` — `arabe.maqsur.hamza-fi-muthanna-wal-jam3` · d `الأَعْلَيَيْنِ` (sans étiquette)
- explication : `«الأَعْلَى» على أربعةِ أحرفٍ (أ، ع، ل، ى)، والمقصورُ الزائدُ على ثلاثةِ أحرفٍ تُقلبُ ألفُه ياءً في المثنّى مهما كان أصلُها، فلا يُنظرُ إلى واوِ الجذرِ (ع ل و): «الأَعْلَيَانِ» في الرفعِ. فمن كتبَ «الأَعْلَوَانِ» ردَّ الألفَ إلى أصلِها كما يُفعلُ في الثلاثيِّ وحدَه (عصا ← عصوان)، ومن كتبَ «الأَعْلَاءَانِ» زادَ همزةً لا تلحقُ المقصورَ، و«الأَعْلَيَيْنِ» صورةُ النصبِ والجرِّ لا الرفعِ.`
(La Q5 actuelle garde ses deux dimensions propres — accord de « خطوة » et cas — après cette règle.)

**M2 · 05/07 Q3** — l'explication livre la clé de Q5 et affirme que « تحامل » n'a pas le sens d'effort (il l'a :
« تحامل على نفسه »). Explication de remplacement :
`الذي يفيدُ بذلَ الجهدِ في القيامِ بالفعلِ هو «تَفَعَّلَ»، وعنصراه التاءُ وتضعيفُ العينِ، كما في «تَصَبَّرَ» و«تَجَلَّدَ»، فنقولُ «تَحَمَّلَ الفِلَسْطِينِيُّونَ وَيْلَاتِ الحَرْبِ». أمّا «تَحَامَلَ» فعلى «تَفَاعَلَ» (التاءُ والألفُ)، ومعاني هذا الوزنِ في كتابِك المشاركةُ والمطاوعةُ والتتالي والتظاهرُ، ولا يتعدّى إلى «وَيْلَاتِ» بنفسِه بل يُقالُ «تَحَامَلَ على نفسِه»؛ و«حَمَّلَ» فيه عنصرٌ واحدٌ هو التضعيفُ والمطلوبُ عنصرانِ؛ و«اسْتَحْمَلَ» فيه ثلاثةُ عناصرَ.`

**M3 · 05/08 Q5** — l'explication (« اللام ياءٌ … فتنقلب همزة ») donne la clé de Q7. Explication de remplacement :
`الفعلُ الواردُ بين المعقوفَيْنِ «تَكْتَفِي» ماضيه «اكْتَفَى» على «افْتَعَلَ»، ومصدرُ «افْتَعَلَ» على «افْتِعَال»: «اكْتِفَاءٌ»، وآخرُه همزةٌ بعدَ ألفٍ فهو ممدودٌ، كما في «اهْتِدَاء» من «اهْتَدَى». والمطلوبُ مصدرُ هذا الفعلِ المزيدِ نفسِه لا مصدرُ الفعلِ المجرّدِ «كَفَى» (كِفَايَةٌ)، وهو ليس ممدودًا.`

**M4 · 05/08 Q1** — même gabarit que 06/07 Q3 (مصدر d'un فاعَلَ → مُفاعَلة), qui est, lui, l'item officiel. Remplacer
05/08 Q1 (reste d1, sur la notion du chapitre) :
- énoncé : `في مناظرة 2023 (أحمد أمين، إلى ولدي): «ساهمتَ وأصدقاؤكَ في تجميلِ شوارعِ المدينةِ». ما المعنى الذي أفادَهُ وزنُ «فَاعَلَ» في الفعلِ «سَاهَمَ»؟`
- options : a `المشاركةُ` (clé) · b `المطاوعةُ` — `arabe.mazid.mutawa3a-bila-fi3l-sabiq` · c `التظاهرُ` · d `الجعليّةُ`
- explication : `«سَاهَمَ» على «فَاعَلَ» بزيادةِ الألفِ بعدَ الفاءِ، ومعناه المشاركةُ: أنتَ وأصدقاؤكَ أطرافٌ يُسهمُ كلٌّ منكم مع الآخرِ في العملِ نفسِه، كما في «لاعَبَ الأبُ ابنَهُ». وليس مطاوعةً لأنّه لا فعلَ سابقًا وقعَ عليكم فقبلتموه، ولا تظاهرًا لأنّكم ساهمتم حقًّا ولم تُظهروا ما ليس فيكم، ولا جعليّةً لأنّه ليس في الجملةِ مفعولٌ صارَ فاعلًا للجذرِ.`

**M5 · 13 Q1, Q3, Q6** — chaque explication nomme le poids que demande la question suivante (Q2, Q4, Q7). Explications
de remplacement :
- Q1 : `يُصاغُ التصغيرُ بضمِّ الحرفِ الأوّلِ وزيادةِ ياءٍ ساكنةٍ بعدَ الحرفِ الثاني: «قَبْلَ» ← «قُبَيْلَ» (وتبقى فتحةُ الآخِرِ لأنّه ظرفٌ منصوبٌ). أمّا «قَبِيلَ» ففتحٌ فكسرٌ فياءُ مدٍّ، وتلك صيغةُ «فَعِيل» التي لا تصغيرَ فيها؛ و«قِبَيْلَ» يكسرُ الأوّلَ والمطلوبُ ضمُّه؛ و«قُبَيْقِلَ» يزيدُ حرفًا ليس في الاسمِ.`
- Q3 : `الحرفُ المشدَّدُ حرفانِ: «فَنٌّ» أصلُه (ف ن ن). يُضمُّ أوّلُه وتُزادُ ياءٌ ساكنةٌ بعدَ حرفِه الثاني، فيظهرُ الحرفانِ المتماثلانِ تفصلُ بينَهما الياءُ ولا يُدغَمانِ: «فُنَيْنٌ». ومن كتبَ «فُنَيٌّ» عدَّ المشدَّدَ حرفًا واحدًا كمن يصغّرُ «دُبّ» على «دُبَيّ»، ومن كتبَ «فُنَيْنَةٌ» زادَ علامةَ تأنيثٍ على مذكّرٍ.`
- Q6 : `يُضمُّ أوّلُ «شَاعِرٌ»، وألفُه الثانيةُ زائدةٌ (ألفُ «فاعِل») فلا تثبتُ بل تصيرُ واوًا كما في «عامِل ← عُوَيْمِل»، ثمّ تأتي ياءُ التصغيرِ الساكنةُ، ثمّ العينُ مكسورةً فالراءُ: «شُوَيْعِرٌ». ومن كتبَ «شُيَيْعِرٌ» جعلَ الألفَ الزائدةَ ياءً، وهذا حكمُ حرفِ اللّينِ الثالثِ (كِتاب ← كُتَيِّب) لا الثاني؛ ومن كتبَ «شُوَيْعِيرٌ» زادَ ياءً قبلَ الآخِرِ لا يقتضيها الاسمُ.`

**M6 · 14 Q3** — miroir de Q2. Remplacer par l'emploi correct de la nisba (le sujet demande de **produire** une phrase
où « وطنيّة » est nisba : le piège réel est le نعت qui ne s'accorde pas) :
- énoncé : `طُلب في مناظرة 2024 (جنى فوّاز الحسن، طابق 99) استعمالُ «وَطَنِيَّة» في جملةٍ تكونُ فيها اسمَ نسبةٍ. أيُّ الجملِ الآتيةِ استُعملت فيها «وَطَنِيَّة» اسمَ نسبةٍ استعمالًا صحيحًا؟`
- options : a `زَيَّنَ التَّلَامِيذُ القَاعَةَ بِالأَعْلَامِ الوَطَنِيَّةِ` (clé) · b `رَفَعَ التَّلَامِيذُ العَلَمَ الوَطَنِيَّةَ فَوْقَ القَاعَةِ` (sans étiquette) · c `الوَطَنِيَّةُ تَعْنِي حُبَّ الأَرْضِ وَالدِّفَاعَ عَنْهَا` — `arabe.nisba.masdar-sina3i-nisba-khalt` · d `تَرَبَّى الجِيلُ عَلَى الوَطَنِيَّةِ وَحُبِّ الخَيْرِ` — `arabe.nisba.masdar-sina3i-nisba-khalt`
- explication : `اسمُ النسبةِ صفةٌ تقعُ نعتًا وتطابقُ منعوتَها: «الأَعْلَامِ الوَطَنِيَّةِ» (نعتُ جمعِ غيرِ العاقلِ يأتي مفردًا مؤنّثًا). أمّا «العَلَمَ الوَطَنِيَّةَ» فنعتٌ مؤنّثٌ لمنعوتٍ مفردٍ مذكّرٍ، والصوابُ «العَلَمَ الوَطَنِيَّ». وفي «الوَطَنِيَّةُ تَعْنِي …» و«عَلَى الوَطَنِيَّةِ» اسمُ معنًى مجرّدٍ يقومُ بنفسِه (مبتدأٌ أو مجرورٌ بحرفٍ)، فهو مصدرٌ صناعيٌّ لا صفةُ نسبةٍ.`
(Accord du نعت : enseigné au ch. 14, méthode « مطابقًا له » et « طبّيّ، ومؤنّثها طبّيّة ».)

**M7 · 14 Q4** — fuite « (إلى المدينة) » vers Q5 : corrigée par l'explication de C-2.

**M8 · 14 Q5** — l'explication ne nomme pas la clé. Remplacement :
`تُنزَعُ ياءُ النسبةِ وتاءُ التأنيثِ من «المَدَنِيَّةُ» فيبقى «مَدَن» بفتحِ الثاني، وهذا أثرُ قاعدةِ «فَعِيلة»: عند النسبةِ إلى اسمٍ ثلاثيٍّ على «فَعِيلة» تسقطُ التاءُ والياءُ ويُفتحُ الثاني. فنردُّ الياءَ والتاءَ: الاسمُ المنسوبُ إليه «مَدِينَةٌ». ومن كتبَ «مُدُنٌ» نسبَ إلى الجمعِ، والنسبةُ إلى المفردِ.`

**M9 · 06 Q4** — fidélité : rétablir la demande officielle (مصدر de « أحلم »).
- énoncé : `في نصّ مناظرة 2024 التقنيّة (صالح الدمس، المرايا القديمة): «كُنْتُ رَغْمَ فَقْرِي تِلْمِيذًا مُجْتَهِدًا جِدًّا أَحْلُمُ بِأَنْ تُزَغْرِدَ أُمِّي يَوْمَ نَجَاحِي». ما مصدرُ الفعلِ «أَحْلُمُ» (ماضيه الثلاثيُّ «حَلَمَ»)؟`
- options : a `حَالِمٌ` · b `مَحْلُومٌ` — `arabe.ishtiqaq.fa3il-maf3ul-ma3na` retiré (laisser sans étiquette) · c `حُلْمٌ` (clé) · d `تَحَلُّمٌ` — `arabe.masdar.wazn-fi3l-akhar`
- explication : `«أَحْلُمُ» مضارعُ الفعلِ الثلاثيِّ المجرّدِ «حَلَمَ»، ومصدرُه «حُلْمٌ» (ويُقالُ «حُلُمٌ»)، ومصادرُ الثلاثيِّ تُعرَفُ بالاستعمالِ لا بوزنٍ واحدٍ. أمّا «حَالِمٌ» فاسمُ فاعلٍ يدلُّ على من يحلمُ، و«مَحْلُومٌ» اسمُ مفعولٍ، و«تَحَلُّمٌ» مصدرُ فعلٍ مزيدٍ آخرَ هو «تَحَلَّمَ» على «تَفَعَّلَ».`

**M10 · 06 Q3, Q5 (l3), Q6, Q8, Q10 — arbitrage de l'orchestrateur.** Le مصدر du verbe augmenté n'est enseigné qu'au
ch. 05 (tableau « المعنى يسكن المشتقّات ») ; le ch. 06 ne l'enseigne pas, et `PLAN.md` fait de 06 un chapitre
« antérieur à tous ». Ces items mêlent 06 et 05 : par la règle du plan ils vont au plus avancé (05). Deux issues :
(a) déplacer ces cinq items dans une mission du ch. 05 ; (b) les garder (le sujet 2026-T Q7 est un seul tableau) et
le consigner comme exception au registre. Aucun texte d'item à changer.

**M11 · 01 Q2** — doublon de 01/06-defi-concours Q6. Remplacer (texte 2026-T, notion du chapitre, plan 2×2) :
- énoncé : `في نصّ مناظرة 2026 التقنيّة (مصطفى لطفي المنفلوطي، النظرات والعبرات): «فَرْقٌ بَيْنَ الغَنِيِّ الَّذِي يَعْمَلُ لِتَنْمِيَةِ ثَرْوَتِهِ». ما حكمُ الكلمتَيْنِ «الَّذِي» و«يَعْمَلُ» من حيثُ الإعرابُ والبناءُ؟`
- options : a `«الَّذِي» مبنيٌّ، و«يَعْمَلُ» مُعرَبٌ` (clé) · b `«الَّذِي» مُعرَبٌ، و«يَعْمَلُ» مُعرَبٌ` — `arabe.i3rab.mabni-mu3rab-khalt` · c `«الَّذِي» مبنيٌّ، و«يَعْمَلُ» مبنيٌّ` — `arabe.i3rab.mabni-mu3rab-khalt` · d `«الَّذِي» مُعرَبٌ، و«يَعْمَلُ» مبنيٌّ` (muette)
- explication : `«الَّذِي» اسمٌ موصولٌ، والأسماءُ الموصولةُ من المبنيّاتِ: يلزمُ آخرُه حالةً واحدةً (جاءَ الذي، رأيتُ الذي، مررتُ بالذي). و«يَعْمَلُ» فعلٌ مضارعٌ لم تتّصلْ به نونُ التوكيدِ ولا نونُ النسوةِ، فهو مُعرَبٌ يتغيّرُ آخرُه: يعملُ، لن يعملَ، لم يعملْ. فمن جعلَ الموصولَ مُعرَبًا نسيَ أنّه من المبنيّاتِ، ومن جعلَ المضارعَ مبنيًّا عمّمَ بناءَ الماضي على الأفعالِ كلِّها.`
(Q7 du même fichier cite la même phrase sans rien dire de البناء : pas de fuite.)

**M12 · 01 Q6** — clé qui ne répond qu'à la moitié de l'énoncé. Remplacer l'option c :
`«أَخُوكَ» مفردٌ رُفعَ بالواوِ، و«أَخَوَاكَ» مثنّى رُفعَ بالألفِ` (l'explication actuelle reste juste).

**M13 · 01 Q7** — `multi` à paires (deux réponses déductibles) + « يتبعانِ » pour trois sujets. Passer en QCM 2×2 :
- `type` : qcm (supprimer `answerKey`, mettre `correctOption: "a"`)
- énoncé : `في نصّ مناظرة 2026 التقنيّة (مصطفى لطفي المنفلوطي، النظرات والعبرات): «فَرْقٌ بَيْنَ الغَنِيِّ الَّذِي يَعْمَلُ لِتَنْمِيَةِ ثَرْوَتِهِ وَبَيْنَ الفَقِيرِ الَّذِي يَعْمَلُ لِتَحْصِيلِ قُوتِهِ». عوّضنا «الغَنِيّ» و«الفَقِير» بمثنّى مؤنّثٍ (ونسلّمُ بأنّ الموصولَ والفعلَ والضميرَ تتبعُه كلُّها). أيُّ العباراتِ الآتيةِ مضبوطةٌ ضبطًا صحيحًا؟`
- options : a `فَرْقٌ بَيْنَ الغَنِيَّتَيْنِ … وَبَيْنَ الفَقِيرَتَيْنِ` (clé) · b `فَرْقٌ بَيْنَ الغَنِيَّتَانِ … وَبَيْنَ الفَقِيرَتَيْنِ` — `arabe.i3rab.muthanna-ana` · c `فَرْقٌ بَيْنَ الغَنِيَّتَيْنِ … وَبَيْنَ الفَقِيرَتَانِ` — `arabe.i3rab.muthanna-ana` · d `فَرْقٌ بَيْنَ الغَنِيَّتَانِ … وَبَيْنَ الفَقِيرَتَانِ` (muette)
- explication : garder l'actuelle.

### Mineurs (10)

- **m1 · 12 Q4** : `difficulty` 3 → 2 (application de l'exemple « سماء » du cours).
- **m2 · 05/08 Q4** : explication, remplacer « أمّا «جَمَّلْنَا» فعلى «فَعَّلَ» ومعناه جعلُ الشيءِ جميلًا لا الاشتراكُ؛ » par `أمّا «جَمَّلْنَا» فعلى «فَعَّلَ»، وليس من معانيه المشاركةُ؛` (sinon clé de 05/07 Q4).
- **m3 · 05/08 Q6** : énoncé, supprimer « يبقى معنى الفعلِ المزيدِ في مشتقّاتِه. » ; explication de remplacement : `«تَآمُرٌ» مصدرُ «تَآمَرَ» نفسِه، و«تَآمَرْتُ» هو الفعلُ نفسُه مسندًا إلى تاءِ المتكلّمِ، و«مُؤَامَرَةٌ» مصدرٌ على «مُفاعَلة» يدلُّ في الاستعمالِ على الاتّفاقِ على تدبيرِ أمرٍ في الخفاءِ: فالثلاثةُ تشتركُ في هذا المعنى. أمّا «مَأْمُورٌ» (من وقعَ عليه الأمرُ) و«أَمَرَ» (طلبَ أن يُفعلَ شيءٌ) و«إِمَارَةٌ» (ولايةُ الأميرِ) فمن الجذرِ نفسِه (أ م ر) لكنّ معانيَها أخرى، والاشتراكُ في الجذرِ لا يعني الاشتراكَ في المعنى.`
- **m4 · 13 Q4** : explication, remplacer la phrase « أمّا «فُعَيِّل» فياؤُه المشدَّدةُ تدلُّ … وليس هذا حالَ «فَنٌّ». » par `أمّا «فُعَيِّل» فليس من أوزانِ التصغيرِ الثلاثةِ: ياؤُه المشدّدةُ توهمُ إدغامَ النونَيْنِ في ياءِ التصغيرِ، والصوابُ أنّ المتماثلَيْنِ يظهرانِ.`
- **m5 · 13 Q5** : item non tiré du sujet et proche de 03-revision / 05-entrainement ; acceptable (format inverse), à consigner.
- **m6 · 14 Q1** : explication, remplacer « و«جَمَالِيَّةٌ» منسوبةٌ إلى كلمةٍ أخرى هي «جَمَال» لا إلى «الجميل» المطلوبِ. » par `و«جَمَالِيَّةٌ» مصدرٌ صناعيٌّ مستعملٌ، لكنّه مصوغٌ من كلمةٍ أخرى هي «جَمَال»، والمطلوبُ ما يُصاغُ من لفظِ «الجميل» نفسِه.`
- **m7 · 14 Q5** : inverse de 14/05-entrainement Q2 (مدينة → مَدَنيّ) ; acceptable, à consigner.
- **m8 · 12 Q3** : gabarit de 12/02-boss Q5 ; justifié (demande officielle 2026).
- **m9 · 01 Q1** : remplacer d par `«وَحِيدَتَانِ»: مثنّى منصوبٌ بالألفِ` — `arabe.i3rab.harf-ghayr-munasib` ; dans l'explication, remplacer « و«وَحِيدَاتٍ» جمعُ مؤنّثٍ لثلاثٍ فأكثرَ. » par `ومن جعلَ الألفَ علامةَ نصبٍ للمثنّى خلطَه بالأسماءِ الخمسةِ التي تُنصبُ بالألفِ.`
- **m10 · 01 Q3** : `difficulty` 2 → 1 (règle rappelée puis appliquée) et la placer en tête du fichier.

### Contrôle des options proposées (longueur sans tashkīl)

| item | longueurs (clé en gras) |
|---|---|
| 12 nouvelle Q (الأعلى) | **8**, 8, 9, 8 |
| 13 Q7 | 4, 4, 6, **5** |
| 14 Q3 | **36**, 37, 34, 32 |
| 06 Q4 | 4, 5, **3**, 4 |
| 01 Q1 | 28, **28**, 44, 28 |
| 01 Q2 | **25**, 25, 25, 25 |
| 01 Q6 | 57, 46, **48**, 53 |
| 01 Q7 | **33**, 33, 33, 33 |
| 05/08 Q1 | **8**, 8, 7, 7 |

## Étiquettes

Les 27 étiquettes posées existent dans `misconceptions.json` et nomment l'erreur exécutée (vérifié une à une, y
compris `wazn-qarib-khalt` en 05/07 Q1, dont le libellé cite « افْتَعَلَ بدلَ اسْتَفْعَلَ »). Options à deux erreurs :
toutes muettes. Seul ajout : les étiquettes des options neuves ci-dessus.

## Rendu

Aucun chiffre indo-arabe, aucun LaTeX, aucune formule ; seuls des millésimes en prose arabe et « … » : aucun cas
bidi à signaler.

## Bilan

| fichier | q. | clés fausses | critiques | majeurs | mineurs |
|---|---|---|---|---|---|
| 12 / 06 | 6 | 0 | 0 | 1 (M1) | 2 |
| 05 / 07 | 7 | 0 | 0 | 1 (M2) | 0 |
| 05 / 08 | 7 | 0 | 0 | 2 (M3, M4) | 2 |
| 13 / 06 | 7 | 0 | 1 (C-1) | 1 (M5, ×3 items) | 2 |
| 14 / 06 | 6 | 0 | 1 (C-2) | 3 (M6–M8) | 2 |
| 06 / 07 | 10 | 0 | 0 | 2 (M9, M10 arbitrage) | 0 |
| 01 / 07 | 7 | 0 | 0 | 3 (M11–M13) | 2 |
| **total** | **49** | **0** | **2** | **13** | **10** |

Questions auditées : 49, toutes résolues à l'aveugle. Clés fausses : 0. Questions à reprendre : 21 (dont 5 de M10
qui relèvent d'un arbitrage de placement, sans changement de texte).
**Verdict : à corriger avant fusion** (deux items à double réponse, fuites en avant systématiques au 13, et un
doublon au 01).
