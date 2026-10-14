# Audit indépendant — gisement arabe 9ᵉ, lot L04 (grammaire, 7 missions, 51 questions)

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill
> `content-audit`), 2026-10-14. Périmètre : dans `/home/user/wt-argis` (branche
> `wip/gisement-arabe-9eme`), les sept missions
> `15/06-examens-2024-2025-rabt-wa-i3tirad`, `04/07-examen-2022-amr-wa-nahy`,
> `16/06-examens-2023-2026-istifham`, `17/06-examens-2023-2026-shart`,
> `18/06-examens-2022-2026-zaman`, `03/07-examens-2020-2026-mafoul-fihi-wal-hal`,
> `19/06-examen-2025-adad-wal-madud`. Aucun fichier audité n'a été modifié ; les notes des auteurs
> n'ont pas été ouvertes.
>
> Sources lues : transcriptions officielles `examens-nationaux/9eme-base/arabic/{2020,2021,2022,2023,2024,2025,2026}-technique.md`
> et `{2023,2024,2025,2026}-generale.md` ; `assign-arabe-L04.md`, `etiquettes-L04.json` ;
> `cours.md` des chapitres 15, 04, 16, 17, 18, 03, 19 ; notes de lecture 101908 `L15.md`, `L3.md`,
> `L110.md` (copie `wt-argis/FableEtudes/_campagne-9eme-au-patron/…/lecture-101908/`, le chemin
> `wt-gis/…` n'existe pas) ; manifeste `9eme-base.json` (ordre : 15, 04, 16, 17, 18, 02, 03, 19…) ;
> `misconceptions.json` ; missions publiées `01…05/06` de chaque chapitre.
>
> Contrôles outillés : `content:check` ✓ ; `content:qa --subject arabic` 0 erreur ;
> `content:tranche` (ch. 03, 04, 15–19) : clé strictement la plus longue 0/288, 0 paire proche ;
> chiffres indo-arabes 0, LaTeX 0, `HP:` 0 ; simulation `isolateLtrRuns` sur toutes les chaînes
> avec chiffres (moteur `eng-argis`) ; vérification des citations contre les transcriptions
> (normalisation sans voyelles).

Légende des verdicts : **OK** · **ERREUR** (clé fausse) · **réserve** (défaut à corriger, clé juste).

---

## 1. `15-al-alaqat-bayna-al-jumal/exercices/06-examens-2024-2025-rabt-wa-i3tirad.json` — d3 boss 120/30, 7 q., rampe 1-2-2-3-3-3-3

Fidélité : 2024 générale, ❖ اللّغة Q1 (incise : type + fonctions des deux constituants) et Q2
(ثمّ et بل : outil + sens) ; 2025 générale Q1 ب (connecteur de استدراك). Citations exactes.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | d | d | réserve (M) | se résout en lisant les tirets ; la vraie demande officielle (fonctions des constituants) n'est pas posée ; recoupe 03-revision Q5 |
| 2 | b | b | OK | étiquette a juste |
| 3 | d | d | OK | l'examen dit « أداة الاستئناف » : استئناف + ترتيب وتراخٍ ; grille 2×2, c muette |
| 4 | d | d | OK | c faible (règle inventée) — mineur |
| 5 | c | c | réserve (M) | b « الأولى مثبتة » nie la négation visible « لَمْ يَكُنْ » : éliminée à vue |
| 6 | b | b | OK | — |
| 7 | d | d | réserve (M) | doublon de fait de `05-entrainement` Q5 (même énoncé, même structure, clé « إلّا أنّ ») ; hors examen ; « الطَّلِبِيَّة » mal vocalisée |

Points de l'auteur tranchés :
- **15 Q1/Q2 (type de l'incise non demandé)** : ne pas demander « نوعها » est défendable (le
  manuel ne type pas les incises ; « يا رجل » ferait débat). Mais Q1 doit porter la **fonction des
  deux constituants**, que l'examen demande et que le cours enseigne (« ناسخ + اسمه + خبره »,
  § 1). → correctif M-1.
- **15 Q7** : doublon (M-3) → supprimer.

## 2. `04-al-asalib/exercices/07-examen-2022-amr-wa-nahy.json` — d2 practice 75/15, 6 q., rampe 1-1-2-2-2-2

Fidélité : 2022 technique Q6 أ (أمر + نهي على لسان الأب). Les deux répliques « لَا تُفَرِّطْ فِي
أَشْجَارِكَ يَا بُنَيَّ » (Q2) et « لَا تُرَاهِنْ بِمَا لَا تَمْلِكُ يَا بُنَيَّ » (Q4) **ne sont pas dans le
texte** mais sont introduites par « قال الأب لابنه » : attribution au texte officiel d'une phrase inventée.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | OK | gabarit voisin de 01-pratique Q4 / 05-tadrib Q4 (clé différente) — mineur |
| 2 | a | a | réserve (M) | citation inventée attribuée au texte |
| 3 | d | d | réserve (M) | redondant avec Q6 (même opposition لا + مجزوم / لا + مرفوع) et doublon de fait de 05-tadrib Q2 |
| 4 | b | b | réserve (M) | « بلطفٍ وشفقةٍ ليرشده » donne la clé ; Q1 (« ينصح »), Q5 (« معنى النصح »), Q6 (« ناصحًا ») la donnent aussi ; c/d éliminées par le rang ; citation inventée |
| 5 | a,b,d | a,b,d | OK | énoncé au pluriel (multi) — mineur |
| 6 | d | d | OK | fidèle ; grille 2×2, c muette ; a non étiquetée (acceptable) |

## 3. `16-al-istifham/exercices/06-examens-2023-2026-istifham.json` — d3 boss 120/30, 9 q., rampe 1-2-2-2-2-2-3-3-3

Fidélité : 2023 générale Q3 أ/ب ; 2024 générale Q3 ; 2025 générale Q3 ; 2026 générale Q1 ب.
Q2 cite deux phrases **abrégées sans points de suspension** (« … وَعَنْ عَمَلِهِ السَّابِقِ » et
« … وَكُوفِيَّتُهُ » omis entre guillemets).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | OK | a filler (mineur) |
| 2 | l1-r3, l2-r1, l3-r2 | idem | réserve (m) | « عن » de « يتخلّى عن » = مفعوليّة : conforme au cours (« يفرض الفعل حرفه ») ✓ ; réserve : « تحوّل إلى » impose aussi son حرف, mais l'appariement bijectif lève l'ambiguïté ; citations à marquer « … » |
| 3 | d | d | réserve (M) | doublon de fait de 03-revision Q3 (هل / ماذا / ألم / أ → بلى) ; l'option b « بِمَاذَا تَأْخُذُ…؟ » est la clé de Q4 |
| 4 | b | b | OK | fidèle (2023 Q3 ب, « المفعوليّة ») |
| 5 | c | c | OK | fidèle (2026 Q1 ب) ; grille 2×2, a (deux erreurs) muette ✓ |
| 6 | d | d | réserve (M) | hors examen ; même grille نعم/بلى × إثبات/نفي que 02-boss Q1 et que Q5 → supprimer |
| 7 | b | b | OK | gabarit voisin de 01-pratique Q4 (contexte argumentatif, d3) — mineur |
| 8 | c | c | réserve (M) | vote : « الفعل » 3/4, « الفاعل » 2/4, « المفعول به » 2/4 → la clé sort par vote ; d cite le passif (« البناء للمجهول », marqué HP dans 2023 technique) ; coquille « ولا تُسمّى المنجَزُ » |
| 9 | d | d | réserve (M) | « كيف » = حال : défendable (إعراب usuel, cours § « كيف خبر أو حال أو مفعول مطلق ») ; mais doublon de fait de 01-pratique Q6 (mêmes quatre fonctions, clé حال) et l'examen 2026 Q1 أ demandait la réponse elliptique + fonctions des omis, pas la fonction de « كيف » → supprimer |

Point 16 Q8 (éléments omis) : **juste** — « لِلسَّيْطَرَةِ … » répond à « لِمَ », omis = يكتسب (فعل),
العامل (فاعل), المعرفة التكنولوجيّة (مفعول به).

## 4. `17-ash-shart/exercices/06-examens-2023-2026-shart.json` — d3 boss 120/30, 8 q., rampe 1-2-2-3-3-3-3-3

Fidélité : 2023 générale Q1 (كلّما → أداة جازمة) et Q2 (لولا) ; 2024 générale Q4 (deux phrases) ;
2025 générale Q2 ; 2026 générale Q2 (1ʳᵉ ligne). Citations exactes.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | réserve (M) | doublon exact de 05-entrainement Q1 (mêmes 4 options, même clé) ; l'item et son explication (« متى … الظرفيّة الزمانيّة ») donnent la clé de Q6 |
| 2 | c | c | OK | — |
| 3 | a,b | a,b | OK | « إنْ » et « متى » pour « كلّما » : les deux gardent le sens ; لو/إذا non جازمتان (cours l. 272), أينما = lieu ✓ |
| 4 | c | c | OK | kasra de التقاء الساكنين expliquée dans l'explication ✓ ; a, d : étiquette proposée inadmissible (→ muettes) |
| 5 | c | c | réserve (M) | définition « بوجود **الاسم** الذي يليها » élimine d (verbe) à vue ; « لولا » définie dans l'énoncé ✓ (non enseignée par le cours) |
| 6 | b | b | OK | kasra non commentée dans l'explication (mineur) |
| 7 | d | d | OK | — |
| 8 | d | d | réserve (M) | hors examen ; doublon de fait de 01-pratique Q2 (mêmes quatre « réalités », clé « لم … ولم … ») → supprimer |

Points de l'auteur : **Q2/Q4/Q6 kasra** — Q2 n'en a pas ; Q4 l'explique ; Q6 : toutes les options
la portent, elle ne décide rien → ajout d'une demi-phrase (m-5). **Q5 لولا** : définition dans
l'énoncé suffisante, à un mot près (M-11).

## 5. `18-dalalat-az-zaman/exercices/06-examens-2022-2026-zaman.json` — d2 practice 75/15, 6 q., rampe 1-2-2-2-2-3

Fidélité : 2022 technique Q5 ب ; 2025 générale Q1 أ ; 2026 générale Q3. Citations exactes.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | réserve (M) | l'explication donne « سوف = يقين بعيد » et « لن = عدم الوقوع » : clés de Q2 (l2, l4) et de Q4 (fuite en avant) |
| 2 | r2, r4, r1, r3 | idem | OK | explication « لن تنصب » → Q3 (mineur, déjà visible dans r3) |
| 3 | d | d | réserve (M) | nasb des cinq verbes (حذف النون) **enseigné nulle part** avant (cours 15, 04, 16, 17, 18) ; étiquettes proposées inadmissibles |
| 4 | b | b | OK | — |
| 5 | **a** | d | **ERREUR** | « لِـ » ouvre une phrase indépendante : lam du **أمر** (le texte porte « فَلْنَطْمَئِنَّ ») ; la fatha de « نَطْمَئِنَّ » ne prouve pas le نصب (مضعّف) |
| 6 | b,c | b,c | OK | حتّى = إمكان selon le manuel (tableau l. 252) ✓ |

## 6. `03-al-mansoubat/exercices/07-examens-2020-2026-mafoul-fihi-wal-hal.json` — d2 practice 75/15, 9 q., rampe 1-2-2-2-2-2-2-3-3

Fidélité : 2020 tech. Q3 ج (2ᵉ ligne), 2021 tech. Q3 ج (حال), 2023 tech. Q5 ب / Q6 ج (2ᵉ ligne),
2024 tech. Q7 (حال), 2025 tech. Q7 (حال, مفعول فيه), 2026 tech. Q5 أ. Aucun item HP (مطلق/لأجله
écartés ✓). Q7 et Q8 sont des enrichissements déclarés (« أُثريت », « بتصرّف ») : ✓.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | OK | — |
| 2 | c | c | réserve (m) | l'énoncé dit « سيقع في المستقبل » : clé quasi donnée (d2 → d1) ; « المركّبات » pour des mots seuls |
| 3 | d | d | réserve (M) | nasb + accord en genre de la حال **non enseignés** (cours 03 et lecture L110 : « aucune définition morphosyntaxique ») |
| 4 | c | c | réserve (M) | « وَقَدْ ابْتَسَمَ », « وَكَانَ قَدْ ابْتَسَمَ » mal vocalisés (→ « قَدِ ابْتَسَمَ ») ; l'explication donne « قبيل » / « قبل », clé de Q9 |
| 5 | a,b,c | a,b,c | OK | — |
| 6 | d | d | OK | fidèle (2026 Q5 أ) ; c muette ✓ |
| 7 | d | d | réserve (M) | doublon de fait de 06-defi-concours Q4 (même case « يفعل … وقد فعل », trois options identiques) → supprimer |
| 8 | c, a, b | c, a, b | OK | conforme au cours (« الحال المنقضية تسبق فعلها ») |
| 9 | c | c | OK | lecture directe du tableau (d2 réel, mineur) |

Points de l'auteur : **03 Q3** — l'acquis antérieur n'est pas enseigné dans l'app → M-15 (cours).
**03 Q9** — les options « وقد / وكان قد » de Q4 (d2) ne gênent pas ; c'est **l'explication** de Q4
qui livre Q9 → M-16.

## 7. `19-al-adad-wal-madud/exercices/06-examen-2025-adad-wal-madud.json` — d3 boss 120/30, 6 q., rampe 2-2-3-3-3-3

Fidélité : 2025 générale Q4 (19 تخصّصًا ; 12 وحدة بحث متخصّصة). Q5 (« تقول الشركة ») et Q6
inventés sur le patron, déclarés.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | réserve (M) | l'explication donne « تِسْعَ عَشْرَةَ = صورة المؤنّث » (Q6) ; recouvre la moitié de 02-boss Q1 (mineur, item officiel) |
| 2 | c | c | réserve (M) | l'énoncé affiche « تِسْعَةَ عَشَرَ تَخَصُّصًا » = clé de Q1 ; d « مفعول به ثانٍ » notion non enseignée (mineur) |
| 3 | d | d | réserve (m) | doublon de fait de 04-defi Q5 (12 + féminin + accusatif, même clé) — gardé car item officiel |
| 4 | a,b | a,b | réserve (M) | 02-boss Q1 avec un autre nombre ; recouvre Q1 + Q6 ; son explication résout Q6 → supprimer |
| 5 | d | d | réserve (M) | vote terme à terme : « ثَلَاثَةَ » 3/4, « خَبِيرًا » 2/4 → clé par vote |
| 6 | c | c | réserve (M) | vote : « تِسْعَ عَشْرَةَ » 3/4 → a éliminée par vote, c seule majoritaire |

Point **19 Q1/Q3** : Q1 recoupe 02-boss Q1 (qui pose les deux genres à la fois) → accepté (mineur,
item officiel). Q3 est un doublon de fait de 04-defi Q5 → **gardé** parce qu'il est la phrase
officielle ; si l'orchestrateur veut zéro doublon, c'est 04-defi Q5 (publié, inventé) qu'il faut
changer, pas l'item d'examen.

Rendu : « تَتَطَلَّبُ 19 ( …… ) تَخَصُّصًا » (Q3, Q4, Q6) est isolé en bloc LTR par `isolateLtrRuns`
→ l'ordre « nombre / blanc » s'inverse à la lecture RTL (mineur) ; sans la parenthèse, chaîne
inchangée (vérifié).

---

## 8. Défauts classés et correctifs (textes vérifiés : longueurs, votes, prémisses, fuites)

### CRITIQUE

**C-1 · 18 Q5 — clé fausse.** « لِنَطْمَئِنَّ عَلَى أَنَّ الدَّعْوَةَ … لَنْ تَجِدَ لَهَا سَمِيعًا » est une
phrase indépendante (début de paragraphe) : aucune action avant elle dont elle dirait la cause, et le
texte de la session porte « **فَلْنَطْمَئِنَّ** » (lam sākina après الفاء, forme de لام الأمر). Le sens
est « rassurons-nous » : طلب. L'argument de l'explication (« آخر المضارع مفتوح فهو منصوب ») ne
tient pas : le مضارع مضعّف au جزم se prononce aussi avec fatha (لِنَطْمَئِنَّ).
- `correctOption` : `d` → **`a`**.
- Étiquettes : a aucune ; b `arabe.zaman.harf-ma3na-khalt` (garder) ; **c `arabe.zaman.harf-ma3na-khalt`** (ajouter : lam du أمر avec le sens de lam التعليل) ; d **muette** (deux erreurs).
- `explanation` : « «لِـ» في أوّل جملةٍ مستقلّةٍ لا تعلّل حدثًا قبلها، فهي لام الأمر: يطلب الكاتب من نفسه ومن قرّائه أن يطمئنّوا، وفي النصّ نفسه «فَلْنَطْمَئِنَّ» بلامٍ ساكنةٍ بعد الفاء كما تُسكَّن لام الأمر. ودلالتها الزمانيّة طلب القيام بالفعل في المستقبل، لأنّ الطلب لا يكون إلّا لما لم يقع. أمّا لام التعليل فتأتي بعد حدثٍ تذكر غايته («ادّخر ماله ليشتري درّاجةً») وتضع تلك الغاية في المستقبل على جهة الإمكان، ولا حدث قبل اللام هنا تكون غايةً له. »

### MAJEURS

**M-1 · 15 Q1 — trivial et infidèle à la demande officielle.** Remplacer (garder l'id de clé `d`, `difficulty` 1 → **2**) :
- `prompt` : « في نصّ مناظرة 2024 تقول الأمّ لزوجها: «إِنَّ القِتَالَ -يا رَجُلُ- حِرْفَةٌ تَحتَاجُ إلى مَهَارَاتٍ خاصّةٍ». وقعتِ الجملةُ الاعتراضيّةُ «يا رَجُلُ» بين مكوّنين من مكوّنات الجملة. ما وظيفتا هذين المكوّنين؟ »
- options : a « الأوّل اسمُ «إنّ»، والثّاني مبتدأٌ » · b « الأوّل مفعولٌ به، والثّاني خبرُ «إنّ» » · c « الأوّل مفعولٌ به، والثّاني مبتدأٌ » (muette) · d « الأوّل اسمُ «إنّ»، والثّاني خبرُ «إنّ» » (clé).
- `explanation` : « إذا حذفنا «يا رَجُلُ» بقيت «إِنَّ القِتَالَ حِرْفَةٌ …»: جملةٌ اسميّةٌ دخل عليها النّاسخ «إنّ»، فـ«القِتَالَ» اسمُه منصوبٌ و«حِرْفَةٌ» خبرُه مرفوعٌ. وليس في الجملة فعلٌ يقع عليه «القِتَالَ» فيكون مفعولًا به، و«حِرْفَةٌ» تُتمّ «إنّ» واسمَها فهي خبرُها لا مبتدأٌ جديد. »
- Vérifié : longueurs 29/32/29/32 (clé non strictement la plus longue), chaque valeur deux fois, aucune mention de la non-fonction de l'incise (clé de Q2).

**M-2 · 15 Q5 b nie une prémisse.** b → « تأكيدٌ: الجملة الأولى تبقى صحيحةً، والثانية تقول معناها نفسَه بأقوى منه » (fausse ici : la 2ᵉ phrase ne renforce pas la 1ʳᵉ, elle dit autre chose ; longueurs 62/68/60/48, clé c non la plus longue).

**M-3 · 15 Q7 — doublon de fait de `15/05-entrainement` Q5** (même énoncé « في أيّ الجمل استُعملت أداة الاستدراك استعمالًا سليمًا؟ », même patron, clé « إلّا أنّ » + issue inattendue), hors examen, redondant avec Q6. **Supprimer Q7** (mission à 6). Si elle est gardée : « الطَّلِبِيَّةَ » → « الطَّلَبِيَّةَ » (option d et explication).

**M-4 · 04 Q2 — citation inventée attribuée au texte.** `prompt` → « صاغ تلميذٌ على لسان الأب الذي تراءى للراوي حزينًا في الحلم (نصّ مناظرة 2022، الاختبار التقني) هذه الجملة: «لَا تُفَرِّطْ فِي أَشْجَارِكَ يَا بُنَيَّ». ما إعراب المضارع «تُفَرِّطْ» وعلامته؟ »

**M-5 · 04 Q3 — redondant** avec Q6 (même opposition لا + مجزوم / لا + مرفوع) et doublon de fait de `04/05-tadrib` Q2 (« أيّ الجمل الآتية نهي؟ », mêmes quatre types). **Supprimer Q3** (mission à 5).

**M-6 · 04 Q4 — clé donnée par l'énoncé et par Q1/Q5/Q6.** Remplacer par la réplique **authentique** du texte (aucun item publié du ch. 04 ne vise الالتماس) :
- `prompt` : « في نصّ مناظرة 2022 (الاختبار التقني) جاء الرجال إلى الراوي يريدون أن يراهنوا على أشجار بستانه، فقال لهم: «اتْرُكُوا الْأَشْجَارَ أَيُّهَا الرِّجَالُ، إِنَّهَا لَا تَعْنِي شَيْئًا لَكُمْ»، ولكنّهم أصرّوا. ما المعنى السّياقيّ للأمر في «اتْرُكُوا»؟ »
- options : a « التّهديد والوعيد » · b « النّصح والإرشاد » · c « الالتماس » (clé) · d « الدّعاء » ; `correctOption` **c** ; a, b, d `arabe.talab.ma3na-bila-maqam`.
- `explanation` : « يعيّن المقامُ معنى الأمر: الراوي شابٌّ يخاطب رجالًا يقامرون معه، فهم نظراؤه لا يملك أن يُلزمهم، وهو يطلب منهم أن يتركوا الأشجار طلبًا لا إلزام فيه، ولذلك أصرّوا فلم يُلزمهم طلبُه؛ فالمعنى الالتماس. وليس نصحًا لأنّه لا يدلّهم على ما فيه صلاحهم بل يطلب ما ينفعه هو، ولا تهديدًا لأنّه لا يتوعّدهم، ولا دعاءً لأنّ المخاطَب ليس الله. »
- Vérifié : longueurs 15/14/8/6 (clé non la plus longue — avec des mots seuls, « الالتماس » aurait été strictement la plus longue) ; le cours (« متساويان يطلب أحدهما من الآخر … التماس ») suffit ; aucun autre énoncé de la mission ne nomme الالتماس.

**M-7 · 16 Q3 — doublon de fait de `16/03-revision` Q3 ; option b = clé de Q4.** Garder l'énoncé officiel, remplacer les distracteurs par une grille 2×2 (négation × contenu) :
- a « أَتَأْخُذُ بِالأَشْعَارِ بِمَجَامِعِ القُلُوبِ؟ » · b « أَلَا تَأْخُذُ بِالأَلْحَانِ بِمَجَامِعِ القُلُوبِ؟ » · c « أَتَأْخُذُ بِالأَلْحَانِ بِمَجَامِعِ القُلُوبِ؟ » (muette) · d clé inchangée. Étiquettes : toutes muettes (aucune existante n'est exacte ; la famille proposée est inadmissible).
- `explanation` : « «بَلَى» لا تأتي إلّا بعد سؤالٍ منفيٍّ تُبطل نفيَه، ويُثبت ما بعدها مضمونَ السؤال نفسَه؛ فالسؤال المناسب «أَلَا تَأْخُذُ بِالأَشْعَارِ بِمَجَامِعِ القُلُوبِ؟». أمّا السؤال بالهمزة وحدها فغير منفيٍّ، فجوابه «نَعَمْ» أو «لَا»؛ وأمّا «أَلَا تَأْخُذُ بِالأَلْحَانِ …؟» فمنفيٌّ، لكنّ الجواب «بِالأَشْعَارِ» لا يُثبت ما سُئل عنه. وفي النصّ أنّ الألحان تُحدث الشجن والأشعار تأخذ بمجامع القلوب. »
- Vérifié : longueurs 29/32/29/32, chaque valeur deux fois ; « بِالأَلْحَانِ » tirée du texte (« بِالأَلْحَانِ العِذَابِ تُحْدِثُ الشَّجَنَ ») ; plus aucune option ne contient « بِمَاذَا ».

**M-8 · 16 Q6 — hors examen, même grille نعم/بلى que 02-boss Q1 et que Q5.** **Supprimer Q6.**

**M-9 · 16 Q8 — clé par vote ; distracteur HP (passif).** b → « الفعل والمفعول به » ; d → « الفعل والمفعول فيه » (muette). Ajouter à l'explication : « … أمّا «الفعل والفاعل والمفعول فيه» فيجعل محذوفًا ما ليس في السؤال، و«الفعل والمفعول به» يُغفل الفاعل «العَامِلُ» وهو محذوفٌ كذلك. » et corriger « ولا تُسمّى المنجَزُ » → « ولا يُسمّى المنجَزُ ». Vérifié : longueurs 26/17/25/18 ; « فاعل » 2/4, « مفعول به » 2/4, « مفعول فيه » 2/4.

**M-10 · 16 Q9 — doublon de fait de `16/01-pratique` Q6** (خبر / مفعول مطلق / مبتدأ-مفعول به / حال, clé حال) et infidèle à 2026 Q1 أ (qui demandait la réponse elliptique et les fonctions des omis — gabarit de Q8). **Supprimer Q9** (mission à 7 avec M-8). Le « كيف = حال » de l'auteur est juste.

**M-11 · 17 Q1 — doublon exact de `17/05-entrainement` Q1 et fuite vers Q6.** Remplacer (clé `b`, d1) :
- `prompt` : « ورد في نصّ مناظرة 2026: «مَتَى أُوتِيَهُ إِنْسَانٌ سَمَا عَلَى النَّاسِ». ما «مَتَى» في هذه الجملة؟ »
- options : a « حرفُ شرطٍ » · b « اسمُ شرطٍ » (clé) · c « اسمُ استفهامٍ » · d « حرفُ استئنافٍ ».
- `explanation` : « «مَتَى» في صدر الجملة تعلّق حدثًا (السموّ على الناس) بحدثٍ ممكنٍ (أن يُؤتى الإنسانُ الإلهامَ)، فهي أداة شرط، وهي من أسماء الشرط العشرة؛ أمّا حرفا الشرط فـ«إنْ» و«لو». وليست اسم استفهامٍ لأنّ المتكلّم لا يسأل ولا ينتظر جوابًا، ولا حرف استئنافٍ لأنّها لا تربط الجملة بجملةٍ قبلها. »
- Vérifié : longueurs 7/7/11/11 ; aucune mention du sens « زمان » (clé de Q6) ; n'existe dans aucune mission publiée du ch. 17.

**M-12 · 17 Q5 — d éliminée par la définition.** Dans l'énoncé, « تعلّق امتناع الجواب بوجود الاسم الذي يليها » → « تعلّق امتناع الجواب بوجود ما يليها » (l'exemple « لَوْلَا الجِسْرُ » montre seul le nom au nominatif). Étiquettes b, d : muettes (famille proposée inadmissible).

**M-13 · 17 Q8 — hors examen, doublon de fait de `17/01-pratique` Q2** (et du gabarit de 02-boss Q3, 04-defi Q4). **Supprimer Q8** (mission à 7).

**M-14 · 18 Q1 — fuite en avant vers Q2 et Q4.** Dernière phrase de l'explication → « أمّا اليقين، وقوعًا أو عدمَ وقوعٍ، فلا تعبّر عنه «أَنْ»، ولا تدلّ «أَنْ» على حدثٍ انقضى في الماضي. »

**M-15 · 18 Q3 et 03 Q3 — notions testées non enseignées.** (a) Le نصب des cinq verbes par حذف النون (18 Q3, question officielle) n'est enseigné dans aucun cours antérieur dans l'ordre du manifeste ; (b) la حال mot unique **منصوبة** et **accordée en genre** (03 Q3) n'est enseignée ni par le cours 03 ni par le manuel (L110 : « aucune définition morphosyntaxique »). Correctif côté **cours** (les items restent) :
- `18-dalalat-az-zaman/cours.md`, sous le tableau des حروف « لم، لمّا، لن » (après la ligne `| لن | — | — | ✗ | لن يحضرَ سامي |` et sa phrase de commentaire) : « > 🗡️ بعدَ «لن» يُنصَبُ المضارعُ: «لن يحضرَ»؛ وإذا اتّصلتْ به واوُ الجماعةِ أو ألفُ الاثنينِ أو ياءُ المخاطَبةِ حُذفتْ نونُه: «يحضرونَ» ← «لن يحضروا». أمّا السّينُ وسوفَ فلا تغيّرانِ آخرَه: «سيحضرونَ». » (+ une demi-ligne dans `resume.md`).
- `03-al-mansoubat/cours.md`, après le bloc `::: definition` de « ## 🎭 الحالُ » : « > 🗡️ الحالُ المفردةُ (كلمةٌ واحدةٌ مثلُ «مراقبًا») **منصوبةٌ**، وتطابقُ صاحبَها في التّذكيرِ والتّأنيثِ: «وقفَ الحارسُ مراقبًا»، «وقفتِ الحارسةُ مراقبةً». » (+ `resume.md` l. 7).
- Variante si l'on refuse de toucher aux cours : définir la règle dans l'énoncé — mais l'item devient une application directe (étage à baisser à d1).

**M-16 · 03 Q4 — vocalisation fautive et fuite vers Q9.** Options a/b : « وَقَدْ ابْتَسَمَ » → « وَقَدِ ابْتَسَمَ », « وَكَانَ قَدْ ابْتَسَمَ » → « وَكَانَ قَدِ ابْتَسَمَ ». Explication, phrase du milieu → « أمّا «وَقَدِ ابْتَسَمَ» و«وَكَانَ قَدِ ابْتَسَمَ» ففعلهما ماضٍ بعد «قد»، فالحالة فيهما منقضيةٌ لا مزامنةٌ، و«بَعْدَ أَنِ ابْتَسَمَ» ليس حالًا بل مفعولٌ فيه يفيد لاحقيّة الاقتلاع. » (plus de « قبيل / قبل », clé de Q9).

**M-17 · 03 Q7 — doublon de fait de `03/06-defi-concours` Q4** (case « يفعل … وقد فعل », options a/c/d identiques au mot près, même clé) et de 04-defi Q4. **Supprimer Q7** (mission à 8 ; 2025 reste représentée par Q2).

**M-18 · 19 Q2 — l'énoncé affiche la clé de Q1.** `prompt` → « في الجملة «تَتَطَلَّبُ 19 تَخَصُّصًا لِلسَّيْطَرَةِ عَلَى فُنُونٍ جَدِيدَةٍ لِلْعَمَلِ» (مناظرة 2025) جاء المعدود «تَخَصُّصًا» مفردًا منصوبًا. ما سبب ذلك؟ » (chaîne inchangée par `isolateLtrRuns` : rendu sûr).

**M-19 · 19 Q4 — doublon de gabarit** (02-boss Q1 avec 14 au lieu de 19 ; somme de Q1 + Q6 ; son explication résout Q6). **Supprimer Q4** (mission à 5).

**M-20 · 19 Q5 — vote terme à terme.** c → « تَسْتَعِينُ بِثَلَاثَةِ عَشَرَ خَبِيرٍ » (muette) ; explication, fin → « … فلا نجرّ الجزء الأوّل «ثَلَاثَةِ»، ولا نجرّ المعدود «خَبِيرٍ» لأنّ الجرّ بعد المئات والآلاف لا بعد المركّب، ومن جرّهما معًا جمع الخطأين. » Vérifié : « ثلاثةِ / ثلاثةَ » 2/2, « خبيرًا / خبيرٍ » 2/2 ; longueurs 23/22/22/23.

**M-21 · 19 Q6 — vote.** d → « تَتَطَلَّبُ تِسْعَةَ عَشَرَ مَهَارَاتٍ » (muette) ; explication, fin → « … أمّا «تِسْعَةَ عَشَرَ» فصورة المذكّر، و«مَهَارَاتٍ» جمعٌ يعطي المعدود حكم مجالٍ آخر: الجمع لا يكون إلّا بعد 3 إلى 10. » Vérifié : chaque forme du nombre et du معدود deux fois ; longueurs 20/21/20/21.

**M-22 · 19 Q1 — fuite vers Q6.** Explication, fin → « … أمّا «تِسْعَ عَشْرَةَ» فتجعل الجزء الأوّل مطابقًا والثاني مخالفًا، وهو عكس القاعدة، و«تِسْعَةَ عَشْرَةَ» تجعل المخالفة في الجزأين معًا. »

### MINEURS

- m-1 · 15 Q4 c « لا تقع إلّا بعد فاصلةٍ واحدة » : règle inventée, faible.
- m-2 · 16 Q2 : citations abrégées → « قَرَّرَ أَبِي أَنْ يَتَخَلَّى عَنْ حَيَاتِهِ المَدَنِيَّةِ … لِيَنْضَمَّ إِلَى المُقَاوَمَةِ » et « تَحَوَّلَ زِيُّهُ العَسْكَرِيُّ … إِلَى مَصْدَرٍ لِلأَمَانِ » ; réserve sur l2 (« تحوّل إلى » = verbe à préposition imposée) levée par la bijection.
- m-3 · 16 Q1 a filler ; 16 Q3/Q5 testent la même règle بلى (deux items officiels, accepté).
- m-4 · 04 Q5 / 16 Q5 : énoncés au pluriel (multi : normal).
- m-5 · 17 Q6 : ajouter à l'explication « (وكُسر آخرهما لأنّ ما بعدهما ساكن) » après « «تَتَصَاعَدِ» و«يَقْتَرِبِ» ».
- m-6 · 18 Q2 : retirer « وتنصب المضارع بعدها («يَزِيدَ») » de l'explication (touche Q3).
- m-7 · 03 Q2 : clé presque donnée par « سيقع في المستقبل » ; « المركّبات » pour des mots seuls → « الكلمات ».
- m-8 · 03 Q9 : lecture directe du tableau, d2 plutôt que d3.
- m-9 · 19 Q3 / 04-defi Q5, 19 Q1 / 02-boss Q1 : recouvrements acceptés (items officiels).
- m-10 · 19 Q3, Q4, Q6 : « 19 ( …… ) » isolé en LTR (ordre nombre/blanc inversé) → retirer « ( …… ) » des énoncés.
- m-11 · 19 Q2 d « مفعولٌ به ثانٍ » : notion non enseignée dans un distracteur.
- m-12 · 04 Q2 d « حذف النون » : notion de ch. ultérieur (02) dans un distracteur.

## 9. Étiquettes

- Toutes les étiquettes posées existent au registre et nomment l'erreur exécutée (31 contrôlées).
- **Familles neuves proposées (`etiquettes-L04.json`) : aucune n'atteint 3 questions distinctes.**
  `zaman.lan-sans-nasb` (18 Q3 seule), `zaman.sin-ma3a-hadhf-nun` (18 Q3), `istifham.mantufiya-bila-nafy`
  (16 Q3 [+ Q5] : 2, et 16 Q3 change avec M-7), `shart.mudari3-mansub-ba3d-in` (17 Q4 seule ; libellé
  fusionnant deux erreurs : subjonctif ET passé gardé — option a n'exécute pas le subjonctif),
  `shart.fi3l-ba3d-lawla` (17 Q5 ; libellé fusionnant verbe et accusatif), `zaman.hal-marfu3a-aw-bila-mutabaqa`
  (03 Q3 ; libellé fusionnant cas et genre, et préfixe `zaman` pour une erreur de cas). → **Ne rien
  créer ; options correspondantes muettes.** Seule pose nouvelle : 18 Q5 c → `arabe.zaman.harf-ma3na-khalt`
  (existante).

## 10. Doublons avec les missions publiées

| item L04 | publié | nature | décision |
| --- | --- | --- | --- |
| 15 Q7 | 15/05-entrainement Q5 | même énoncé, même patron | supprimer |
| 15 Q1 | 15/03-revision Q5 | même gabarit (constituants) | remplacé (M-1, contenu ناسخ distinct) |
| 04 Q3 | 04/05-tadrib Q2 | mêmes 4 types d'options | supprimer |
| 16 Q3 | 16/03-revision Q3 | mêmes 4 types, même clé | distracteurs refaits (M-7) |
| 16 Q6 | 16/02-boss Q1 | même grille نعم/بلى | supprimer |
| 16 Q9 | 16/01-pratique Q6 | mêmes fonctions, clé حال | supprimer |
| 17 Q1 | 17/05-entrainement Q1 | options identiques, même clé | remplacé (M-11) |
| 17 Q8 | 17/01-pratique Q2 | mêmes 4 « réalités » | supprimer |
| 03 Q7 | 03/06-defi-concours Q4 | 3 options identiques, même clé | supprimer |
| 19 Q4 | 19/02-boss Q1 | même gabarit, autre nombre | supprimer |
| 19 Q3 | 19/04-defi Q5 | même clé | gardé (officiel) |
| 19 Q1 | 19/02-boss Q1 (moitié) | recouvrement | gardé (officiel) |
| 18 Q1 | 18/05-entrainement Q3 | même fait (أن = إمكان) | gardé (officiel) |

## 11. Bilan

- Questions auditées : **51** (re-résolues à l'aveugle ; multi énoncé par énoncé, matching paire par paire, ordering).
- Clés fausses : **1** (18 Q5 : `d` → `a`).
- Majeurs : **22** (M-1 … M-22) : 7 suppressions (15 Q7, 04 Q3, 16 Q6, 16 Q9, 17 Q8, 03 Q7, 19 Q4), 3 remplacements complets (15 Q1, 04 Q4, 17 Q1), 2 ajouts de cours (M-15), le reste en retouches d'options, d'énoncés ou d'explications.
- Mineurs : **12**.
- Questions à reprendre : **24** (dont 7 à supprimer ; 18 Q3 et 03 Q3 se règlent par le cours, items inchangés).
- Après correctifs : 15 → 6 q., 04 → 5, 16 → 7, 17 → 7, 18 → 6, 03 → 8, 19 → 5 (44 questions).
- **Verdict : à corriger avant fusion** (une clé fausse, fuites et doublons de fait). Les textes de
  remplacement ci-dessus ont été vérifiés (longueur stricte, votes, prémisses, fuites, rendu bidi).
