# Audit indépendant : gisement maths 9ᵉ, ch. 17, exercice 2 des examens 2001 à 2011

**Verdict : aucune clé fausse (46/46 re-résolues à l'aveugle), mais la tranche ne part pas en l'état.** Il reste 1 défaut critique (une question libre à deux réponses défendables) et 6 familles de défauts majeurs : des fuites de clé, des indices de fréquence et des doublons.

**Périmètre.** 8 missions (09→16), 46 questions (44 QCM, 1 multi, 1 `short_answer`), plus la ligne `sources[]` du `chapter.json`.
- Méthode à l'aveugle : pour chaque question, j'ai extrait l'énoncé et les options sans clé, explication ni étiquette, j'ai résolu, puis comparé à la clé et à la transcription.
- Lu sur `origin/main` : les 8 transcriptions (identiques à l'arbre), le cours du ch. 17 et ceux des ch. 15, 01, 19, 02 et 16, les missions publiées 01 à 08 et le quiz, les deux registres. Je n'ai rien ouvert sous `/tmp/claude-0/`. Aucun fichier modifié.

**Gates** (lecture seule, lancés depuis `/home/user/yahia-quest-arena`, dont `content` pointe sur l'arbre audité) :
- `content:check` (`build.ts --check`) sur math : ✓.
- `content:qa` : 0 erreur, aucun avertissement sur la tranche.
- `content:tranche` : 0 clé strictement la plus longue sur 44 (ma mesure donne pareil, avec 14 égalités, admises).
  - L'outil signale une paire proche inter-chapitres : 12#2 ↔ `03-calcul-litteral/…/18-examen-2005-ex2…#5`. C'est l'autre tranche, hors de mon périmètre : je ne l'ai pas ouverte.
- Notation : 0 chiffre arabo-indien, 0 tiret ASCII, 0 LaTeX ou `$`, 0 groupe de chiffres séparé par une espace simple, 0 virgule arabe dans des crochets, 0 radicande arabe. Un seul signe espacé (m1).

**Fidélité au sujet**
- Toutes les données sont celles de la transcription, et toutes les sous-questions sont présentes, dans l'ordre. Aucune n'est perdue : la nature « entier naturel » passe dans l'explication en 13 Q7, 15 Q6 et 16 Q7.
- Fusions acceptables :
  - 12 Q6 = 2a + 2b du sujet ;
  - 16 Q3 = 1b ;
  - 10 Q5 porte valeur + nature ;
  - 15 Q3 montre « B = 1/A » par l'inversion du dénominateur (إنطاق) au lieu du produit, ce qui est légitime.
- En revanche, les étapes « signe » ne sont **pas** fusionnées en 12, 13 et 14 (voir M4).

**Programme**
- Tout ce qui est testé est enseigné dans les ch. 15 → 17 :
  - radicaux, مرافق et إنطاق, √(x²) = |x| : ch. 02 ;
  - |x| : ch. 19 ;
  - (ab)ⁿ : ch. 16 ;
  - ordre, carrés, inverses : ch. 17.
- Les identités sont données en 13 Q4, 15 Q6, 16 Q1 et Q6. Ni équation, ni notation d'intervalle, ni vecteur.

**En-têtes**
- Les 8 missions : boss, difficulté 3, 120 XP / 30 pièces. Titres au format demandé, `displayOrder` de 9 à 16, rampes non décroissantes.
- La ligne `sources[]` ajoutée est identique à celle déjà publiée sur main (ch. 13) ✓.

## Tableaux par fichier

**09 — 2001**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | c | c | OK | m1 |
| 2 | a | a | réserve | M6 ([c]) ; m2 |
| 3 | d | d | OK | — |
| 4 (multi) | {a,b} | {a,b} | OK | m3 |
| 5 | b | b | OK | — |

**10 — 2002**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve | M3 : le verdict « > » est dans 2 options sur 4 |
| 2 | a | a | OK | m4 |
| 3 | d | d | OK | — |
| 4 | c | c | réserve | M1 : fuite vers Q5 ; M3 : « a × b = 1 » dans 2 options ; M5 |
| 5 | b | b | réserve | M3 : « عدد صحيح طبيعي » dans 2 options |

**11 — 2006**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve | M6 ([c]) |
| 2 | d | d | OK | m5 |
| 3 | a | a | OK | m12 ; m16 |
| 4 | c | c | OK | m13 ; m15 |
| 5 | d | d | OK | — |

**12 — 2007**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | c | c | réserve | M2 : fuite vers Q2/Q3 ; M6 ([d]) |
| 2 | a | a | réserve | M4 (avec Q3) |
| 3 | d | d | réserve | M4 : redemande Q2 ; m6 |
| 4 | b | b | réserve | M2 : fuite vers Q6 |
| 5 | c | c | réserve | M2 : fuite vers Q6 ; m15 |
| 6 | b | b | OK | m14 |

**13 — 2008**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve | M2 : fuite vers Q2/Q3 |
| 2 | c | c | réserve | M4 (avec Q3) |
| 3 | a | a | réserve | M4 ; m6 |
| 4 | d | d | OK | m6, m7 |
| 5 | b | b | réserve | M6 ([c]) ; m11 |
| 6 | c | c | OK | m8, m11, m13 |
| 7 | a | a | OK | — |

**14 — 2009 générale**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | d | d | OK | — |
| 2 | b | b | réserve | M3 : « موجب » dans 2 options ; M4 ; m6 |
| 3 | a | a | réserve | M6 ([d]) ; m11 |
| 4 (libre) | المقلوب | المقلوب | **CRITIQUE** | C1 : ambiguïté ; m16, m17 |
| 5 | c | c | réserve | M3 : « = −b » dans 2 options |

**15 — 2010 générale**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | c | c | OK | m9 |
| 2 | a | a | réserve | M2 : fuite vers Q4 ; M6 ([b]) |
| 3 | d | d | réserve | M5 (doublon de 10 Q4) ; M2 |
| 4 | b | b | réserve | M5 (doublon de 10 Q1) |
| 5 | a | a | réserve | M1 : fuite vers Q6 ; m10 |
| 6 | c | c | OK | — |

**16 — 2011 générale**
| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | a | a | OK | m11 |
| 2 | d | d | OK | m11 |
| 3 | c | c | OK | m11, m12 |
| 4 | b | b | OK | m15 |
| 5 | a | a | OK | — |
| 6 | d | d | réserve | M1 : fuite vers Q7 |
| 7 | c | c | OK | m14 |

Toutes les options « bon verdict, mauvais appui » portent une affirmation numérique réellement fausse : 10Q1c, 12Q3c, 12Q6c, 13Q2b, 13Q3b, 14Q2d, 16Q3b. Aucune option n'est défendable, sauf C1.

## Défauts

### CRITIQUE

**C1 — 14 Q4 (question libre) : deux réponses défendables.**
- b = 5√2 + 7 est aussi le **مرافق** (conjugué) de a = 5√2 − 7. Le terme est enseigné au ch. 02 et employé dans la tranche même (12 Q4, 15 Q3).
- Avec l'énoncé « نحسب الجداء a × b ثمّ نسمّي العدد b بالنسبة إلى العدد a. ما هذا الاسم؟ », un élève qui tape « مرافق » dit vrai et serait refusé.
- **Énoncé de remplacement :** « نعتبر العددين:\na = 5√2 − 7\nb = 5√2 + 7\nاحسب الجداء a × b. قيمة هذا الجداء تُثبت أنّ العدد b هو … العدد a. ما الكلمة الناقصة؟ »
- `answerKey` « المقلوب », les `acceptedAnswers` (toutes justes) et `expectedMistakes` « المقابل » restent inchangés.

### MAJEURS

**M1 — Une explication donne la valeur-clé de la question suivante.**
- **10 Q4 → Q5 (clé 6).** L'explication de Q4 dit « بينما هنا a + b = 6 ». Explication complète proposée (compatible avec M3b) :
  « الجداء من الشكل (u − v)(u + v) = u² − v² مع u = 3 و v = 2√2: a × b = 3² − (2√2)² = 9 − 8 = 1 ✓ لأنّ (2√2)² = 2² × (√2)² = 4 × 2 = 8. وعددان جداؤهما 1 يكون كلّ منهما مقلوب الآخر، أي b = 1/a. الخطأ الشائع تربيع الجذر وحده فيُكتب (2√2)² = 2 × 2 = 4 ويخرج 9 − 4 = 5 ؛ أو جمع المربّعين بدل طرحهما فيخرج 9 + 8 = 17 ؛ أو طرح المربّعين بالترتيب المعكوس فيخرج 8 − 9 = −1. »
  - Si [a] est gardée, remplacer seulement « بينما هنا a + b = 6 » par « والعدد b موجب مثل a فلا يمكن أن يكون مقابله ».
- **15 Q5 → Q6 (clé 34).**
  - Remplacer « (تحقّق: A/B + B/A ≈ 34,000) »
  - par « (وبطريق آخر: A/B + B/A = (A² + B²)/(A × B) = A² + B² لأنّ A × B = 1) ».
- **16 Q6 → Q7 (clé 14).** L'explication donne (a + c)² = 196, ainsi que 194 et 192. Nouvelle explication :
  « بما أنّ a × c = 1 فإنّ 1/c = a و 1/a = c، إذن a/c = a × (1/c) = a² و c/a = c². ونكتب 2 = 2ac لأنّ ac = 1، فيصبح a/c + c/a + 2 = a² + c² + 2ac = (a + c)² ✓. الخطأ الشائع نسيان الحدّ 2 فيبقى a² + c² ؛ أو استعمال متطابقة الفرق مع أنّ الحدّ 2ac مضاف لا مطروح فيخرج (a − c)² ؛ أو تحويل القسمة إلى ضرب فيُكتب a/c = a × c = 1 ومنه 1 + 1 + 2 = 4. »

**M2 — Les vérifications décimales « (تحقّق: … ≈ …) » livrent le signe ou le verdict demandé ensuite.**
- **12 Q1 :** supprimer « (تحقّق: a ≈ 0,243) ». Avec a > 0, la clé de Q2 est la seule option « < » et Q3 se réduit à [c]/[d].
- **13 Q1 :** supprimer « (تحقّق: a ≈ 1,528 و 6 − 2√5 ≈ 1,528) ». Cette valeur donne Q3 et la moitié de Q2.
- **15 Q2 :** supprimer « (تحقّق: B ≈ 0,172) ».
- **15 Q3 :** remplacer « (تحقّق: 1/A ≈ 0,172) » par « (تحقّق: A × B = 9 − 8 = 1 ✓) ».
  - Avec B > 0, la seule option « > » de Q4 est la clé.
- **12 Q4 :** remplacer « (تحقّق: x ≈ 2,899) » par « (تحقّق: (7√2 − 7)(√2 + 1) = 14 + 7√2 − 7√2 − 7 = 7 ✓) ».
- **12 Q5 :**
  - remplacer « (تحقّق: y ≈ 2,414 و √2 + 1 ≈ 2,414) » par « (تحقّق: (√2 + 1)(√2 − 1) = 2 − 1 = 1 ✓) » ;
  - remplacer « فيخرج √2 − 1 ≈ 0,414 » par « فيخرج √2 − 1 ».
  - Motif : avec x ≈ 2,899 et y ≈ 2,414, on obtient x − y ≈ 0,485, ce qui désigne 6√2 − 8 et donc la clé de Q6.

**M3 — Indice de fréquence : la valeur décisive de la clé est la seule qui apparaît deux fois.**
- **10 Q1.**
  - [c] devient « 3 < 2√2 ، لأنّ 3² = 9 و (2√2)² = 2² × 2² = 16 », étiquette `math.num.racine-et-carre-confondus`.
  - Dans l'explication, « ومن ربّع الجذر وحده وجد (2√2)² = 2 × 2 = 4 خطأً، وإن بقي حكمه صحيحًا بالمصادفة » devient « ومن كتب (√2)² = 2² = 4 وجد (2√2)² = 4 × 4 = 16 فقلب المقارنة ».
- **10 Q4.** [a] devient « a × b = −1 ، ومنه b = −1/a », sans étiquette ; l'explication est celle de M1.
- **10 Q5.**
  - [d] devient « 1/a + 1/b = 1/6 ، وهو عدد ناطق غير عشري », sans étiquette.
  - Dans l'explication, « ومن اعتبر المجموع مساويًا لمقلوب الجداء كتب 1/a + 1/b = 1/(a × b) = 1 » devient « ومن جعل مجموع المقلوبين مقلوبَ المجموع كتب 1/a + 1/b = 1/(a + b) = 1/6 ».
- **14 Q2.**
  - [d] devient « سالب ، لأنّ العدد a يتضمّن طرح 7 ».
  - Dans l'explication, « (نتيجة المقارنة السابقة) » devient « (لأنّ (5√2)² = 50 > 49 = 7²) ».
  - Et « ومن أسقط الجذر فكتب 5√2 = 5 × 2 = 10 حصل على النتيجة الموجبة بحجّة باطلة » devient « ومن حكم من إشارة الطرح الظاهرة في الكتابة نسي أنّ إشارة الفرق تتوقّف على أيّ الحدّين أكبر ».
- **14 Q5.**
  - [a] devient « b(a − 1) − 1 = 1 − b ، فمجموع العددين يساوي 1 », sans étiquette. La confusion inverse/opposé reste testée en Q4.
  - Dans l'explication, « الخطأ الشائع وصف العددين بأنّهما مقلوبان: المقلوبان جداؤهما 1، أمّا هنا فجداؤهما b × (−b) = −b² ≈ −198 » devient « الخطأ الشائع نسيان الحدّ −1 الأخير فيُكتب ab − b = 1 − b ، ومجموعه مع b يساوي 1 لا 0 ؛ ولا يكون b و −b مقلوبين لأنّ جداءهما −b² سالب ».

Toutes les longueurs ont été vérifiées : aucune clé ne devient strictement la plus longue.

**M4 — Doublon dans la même mission : la question « signe » redemande la comparaison.** Sa clé recopie celle de la question précédente.
- **12 : fusionner Q2 et Q3** (difficulté 2 ; la mission passe à 5 questions).
  - Énoncé : « نعتبر العدد:\na = 3√2 − 4\nما إشارة a ، وما الحجّة الصحيحة؟ »
  - Options :
    - [a] clé : « موجب ، لأنّ (3√2)² = 18 و 4² = 16 »
    - [b] « سالب ، لأنّ (3√2)² = 3 × 2 = 6 و 4² = 16 » — étiquette `exposant-porte-sur-un-seul-facteur`
    - [c] « معدوم ، لأنّ 3√2 ≈ 4,24 و 4,24 ≈ 4 » — étiquette `comparaison-radical-et-entier`
    - [d] « سالب ، لأنّ العدد a يتضمّن طرح 4 »
  - Explication : « العددان 3√2 و 4 موجبان، فنقارن مربّعيهما: (3√2)² = 3² × (√2)² = 9 × 2 = 18 و 4² = 16. وبما أنّ 18 > 16 فإنّ 3√2 > 4 ، إذن الفرق a = 3√2 − 4 موجب ✓. الخطأ الشائع تربيع الجذر وحده مع ترك المعامل فيخرج (3√2)² = 3 × 2 = 6 ويُحكم بالسالب ؛ ومن قرّب 3√2 إلى 4 ظنّ الفرق معدومًا مع أنّه ليس صفرًا ؛ ومن حكم من إشارة الطرح الظاهرة في الكتابة نسي أنّ إشارة الفرق تتوقّف على أيّ الحدّين أكبر. »
- **13 : fusionner Q2 et Q3** (difficulté 2 ; la mission passe à 6 questions).
  - Énoncé : « نعتبر العدد:\na = 6 − 2√5\nما إشارة a ، وما الحجّة الصحيحة؟ »
  - Options :
    - [a] clé : « موجب ، لأنّ 6² = 36 و (2√5)² = 20 »
    - [b] « سالب ، لأنّ 6² = 36 و (2√5)² = 2² × 5² = 100 » — étiquette `racine-et-carre-confondus`
    - [c] « سالب ، لأنّ 2√5 = 2 × 5 = 10 وهو أكبر من 6 »
    - [d] « موجب ، لأنّ √5 < 2 فيكون 2√5 < 4 » — étiquette `comparaison-radical-et-entier`
  - Explication : « العددان 6 و 2√5 موجبان، فنقارن مربّعيهما: 6² = 36 و (2√5)² = 2² × (√5)² = 4 × 5 = 20. وبما أنّ 36 > 20 فإنّ 6 > 2√5 ، إذن الفرق a = 6 − 2√5 موجب ✓. الخطأ الشائع تربيع الجذر كأنّه العدد 5 نفسه: (√5)² = 5² = 25 فيخرج (2√5)² = 100 وتنقلب المقارنة ؛ ومن كتب 2√5 = 2 × 5 = 10 أسقط الجذر فحكم بالسالب ؛ ومن قدّر √5 < 2 أخطأ، لأنّ (√5)² = 5 > 4 = 2² ، فحكمه الموجب صحيح بحجّة باطلة. »
- **14 Q1 et Q2 : garder les deux.** Fusionner laisserait 4 questions. Appliquer M3 à Q2 ; le recoupement restant est mineur.

**M5 — Vrais doublons entre missions : mêmes nombres, 3 ± 2√2.**
- **15 Q3 ≈ 10 Q4.** Même fait (3 ± 2√2 sont inverses) et mêmes trois erreurs : l'opposé, /5 et 17.
  - [c] « (3 − 2√2)/5 » devient « 1/3 + √2/4 ».
  - Dans l'explication, « أو تربيع الجذر وحده فيُكتب (2√2)² = 2 × 2 = 4 ويخرج المقام 9 − 4 = 5 » devient « أو تقسيم الكسر على حدّي المقام: 1/(3 + 2√2) = 1/3 + 1/(2√2) = 1/3 + √2/4 ، والمقام لا يُقسَّم على حدّيه ».
- **15 Q4 ≈ 10 Q1.** Même fait (3 > 2√2), deux distracteurs quasi identiques, et le verdict seul suffit pour répondre.
  - [c] devient « 3 > 2√2 ، لأنّ B مقلوب عدد أكبر من 1 فهو أكبر من 1 », étiquette `math.num.inverse-conserve-l-ordre`.
  - [d] devient « 3 < 2√2 ، لأنّ (2√2)² = 2² × 2² = 16 وهو أكبر من 9 », étiquette `racine-et-carre-confondus`.
  - Dans l'explication, « ومن اكتفى بالتقريب … حكم بأنّ 3 أصغر » devient « ومن ظنّ أنّ المقلوب يحفظ الترتيب استنتج من A > 1 أنّ B > 1 ، والصحيح B = 1/A < 1 ، فحكمه صحيح بحجّة باطلة ؛ ومن كتب (√2)² = 2² = 4 وجد (2√2)² = 16 فقلب المقارنة ».

**M6 — Étiquette ambiguë sur 6 options : `math.num.racine-extraction-facteur-inversee`.**
- Options concernées : 09Q2[c], 11Q1[c], 12Q1[d], 13Q5[c], 14Q3[d], 15Q2[b].
- Pourquoi c'est ambigu :
  - Le chemin décrit par l'auteur, « √18 = 2√9 = 6 », suit l'exemple du cours ch. 02 (« √50 = 2√25 »). Le libellé du registre donne pourtant un autre exemple (« 2√5 »).
  - Chaque valeur sort aussi de « a√b lu a × b » (3√2 → 6, 2√3 → 6, 4√5 → 20, 5√2 → 10, 4√2 → 8).
  - Pour 12Q1[d], elle sort aussi de √8 = 8 ÷ 2 (étiquette `racine-confondue-avec-moitie`).
  - La doctrine é30 veut qu'une option ambiguë reste muette.
- **Correctif :** retirer l'étiquette des six options et réécrire la phrase de diagnostic.

| Option | Phrase actuelle | Phrase de remplacement |
|---|---|---|
| 09 Q2 [c] | « ومن عكس العاملين عند الإخراج كتب √18 = 2√9 = 6 فوجد … » | « ومن جعل √18 = 6 — بقراءة 3√2 على أنّه 3 × 2 أو بكتابة √18 = 2√9 — وجد 6√2 − 6 + 1 = 6√2 − 5 » |
| 11 Q1 [c] | la phrase « عكس العاملين… = 6 » | « الخطأ الشائع إسقاط الجذر بقراءة 2√3 على أنّه 2 × 3 فيخرج 6 (والقيمة نفسها تخرج من √75 = 3√25 و √12 = 3√4) » |
| 12 Q1 [d] | la phrase « عكس العاملين عند إخراج √8… » | « ومن جعل √8 = 4 — بأخذ نصفه أو بقراءة 2√2 على أنّه 2 × 2 — وجد 5√2 − 4(√2 + 1) = √2 − 4 » |
| 13 Q5 [c] | la phrase sur √245 = 5√49 | « أو إسقاط الجذر بقراءة 4√5 على أنّه 4 × 5 = 20 » |
| 14 Q3 [d] | la phrase sur √200 = 2√100 | « أو إسقاط الجذر بقراءة 5√2 على أنّه 5 × 2 = 10 فيخرج 10 + 7 = 17 » |
| 15 Q2 [b] | la phrase sur √32 = 2√16 | « الخطأ الشائع إسقاط الجذر بقراءة 4√2 على أنّه 8 و 2√2 على أنّه 4 فيخرج 3 + 8 − 3 × 4 = −1 » |

### MINEURS

- **m1.** 09 Q1, explication : « الحدّ − 2 » → « الحدّ −2 » (nombre signé serré).
- **m2.** 09 Q2, énoncé : « بسّط الجذر الظاهر في العدد التالي ثمّ اختزل: » → « بسّط √18 ثمّ اختزل العدد التالي: ».
- **m3.** 09 Q4 [c] « b − a = √2 − √3 » : l'erreur n'est pas plausible, et le diagnostic « لا نطرح المعاملين » ne produit pas cette option.
  - Option → « الفرق b − a = √(18 − 12) = √6 وهو موجب ».
  - Explication → « أمّا b − a = √6 فخطأ: 3√2 − 2√3 = √18 − √12 والجذر لا يُوزَّع على الطرح (القيمة الحقيقية ≈ 0,779 بينما √6 ≈ 2,449) ».
- **m4.** 10 Q2, explication : « ومن جمع 2√2 مع 3 كأنّهما متشابهان كتب |2√2 − 3| = √2 » → « ومن عامل 2√2 و 3 كحدّين متشابهين كتب 2√2 − 3 = −√2 فوجد |2√2 − 3| = √2 ».
- **m5.** 11 Q2, fuite partielle vers Q3 (le signe, pas le sens) : « (تحقّق: b − a ≈ 0,268 و 2 − √3 ≈ 0,268) » → « (تحقّق: a + (2 − √3) = 2√3 + 2 − √3 = 2 + √3 = b ✓) ».
- **m6.** Explications qui renvoient à « la question précédente » alors que chaque énoncé doit se lire seul : 12 Q3 et 13 Q3 (réglé par la fusion), 14 Q2 (dans M3), 13 Q4 : « وهو العدد a السابق نفسه » → « وهو العدد a = 6 − 2√5 نفسه ».
- **m7.** 13 Q4 : la clé 6 − 2√5 est la valeur de a, déjà validée en Q1 et Q3. Indice de reconnaissance inhérent au « montrer que » du sujet ; aucun changement requis.
- **m8.** 13 Q6 :
  - explication : « نسيان تغيير إشارة الحدّين معًا » → « تغيير إشارة الحدّ الثاني وحده » ;
  - énoncé : « احسب الفرق ثمّ اختزله » → « احسب الفرق b − a ثمّ اختزله ».
- **m9.** 15 Q1, énoncé : supprimer « مع احترام أولوية الضرب » (l'indice désamorce le distracteur [b]).
- **m10.** 15 Q5 [d] « C = A² − B² » est un remplissage (aucun geste plausible).
  - Option → « C = (A + B)² », étiquette `math.alg.carre-somme-sans-double-produit`.
  - Explication : « أو طرح المربّعين بدل جمعهما C = A² − B² » → « أو كتابة A² + B² = (A + B)² بإسقاط الجداء المضاعف ».
- **m11.** Décimales qui fuient partiellement, par un calcul : supprimer les parenthèses suivantes.
  - 16 Q1 « (تحقّق: a ≈ 13,928) », 16 Q2 « (تحقّق: b ≈ 14,071) », 16 Q3 « (تحقّق: a ≈ 13,928 و b ≈ 14,071) » : donnent le verdict de Q3 et, par b/a ≈ 1,01, la clé de Q5.
  - 14 Q2 « (a ≈ 0,071) » et 14 Q3 « (تحقّق: b ≈ 14,071) » : ab ≈ 1 donne Q4.
  - 13 Q5 « (تحقّق: b ≈ 8,944) » et 13 Q6 « (تحقّق: b − a ≈ 7,416 …) » : Q6 et Q7 se trouvent par comparaison numérique.
- **m12.** Cohérence des étiquettes.
  - `math.num.comparaison-radical-et-entier` (« au jugé ») couvre déjà l'approximation prise pour une égalité. Elle est posée en 10Q1[a] et 14Q1[a], mais manque en 11Q3[d], 12Q2[c], 14Q2[a] et 15Q4[c] (si gardée) : l'ajouter.
  - 16Q3[b] ((4√3)² = 16) est l'exemple même du libellé de `exposant-porte-sur-un-seul-facteur` : l'étiqueter.
- **m13.** Calibrage.
  - 11 Q4 et 13 Q6 sont un seul geste : passer de d3 à d2 (l'ordre ne change pas).
  - 15 Q3 est en d2 alors que 12 Q4/Q5, même geste, sont en d3 : aligner.
- **m14.** Fréquence légère : « 6√2 − 8 » dans 3 options de 12 Q6 ; « 14 » dans 2 options de 16 Q7. Facultatif.
- **m15.** Gabarits : 11 Q4 ≈ 16 Q4 (même produit conjugué = 1, mêmes types d'erreurs) ; 12 Q4 ≈ Q5 (imposé par le sujet). Diversifier un distracteur si possible.
- **m16.** Recoupements avec les missions publiées :
  - 14 Q4 a la même clé libre « المقلوب » que 06-defi-concours Q7. Option : porter la question libre sur Q5, avec la clé « المقابل ».
  - 11 Q3 porte le même fait que 01-pratique Q1 (a − b = √3 − 2, donc a < b) ; c'est imposé par le sujet.
- **m17.** 14 Q4 : ajouter « مقلوبه » aux `acceptedAnswers`.

## Doublons entre les huit missions

- **Aucune mission ne diffère des autres par ses seuls nombres** : chaque sujet enchaîne une chaîne propre.
- **Vrais doublons de question :**
  - 10 Q4 ↔ 15 Q3 et 10 Q1 ↔ 15 Q4 (M5) : même paire 3 ± 2√2, mêmes faits.
  - Dans une même mission : 12 Q2/Q3, 13 Q2/Q3, 14 Q1/Q2 (M4).
- **Annales légitimement voisines, à garder :**
  - Comparaisons par les carrés : 09Q3, 10Q1, 12Q2, 13Q2, 14Q1, 16Q3. Le piège « exposant sur un seul facteur » revient dans les six ; on peut le varier.
  - Réductions de radicaux : 14 Q3 et 16 Q2 donnent tous deux 7 + 5√2 ; 10 Q3 et 15 Q1 donnent tous deux 3 + 2√2.
  - Ordre des inverses : 09Q5, 11Q5, 16Q5.
  - Entiers obtenus : 10Q5, 13Q7, 15Q5–6, 16Q6–7.
  - Identités : 13Q4, 15Q6, 16Q1.

## Les trois erreurs sans étiquette (pour ta décision)

1. **a√b écrit a × b.**
   - Explicite dans 6 questions : 10Q1[d], 12Q3[c], 13Q2[d], 13Q3[d], 14Q2[d], 15Q4[d].
   - Même valeur, de façon ambiguë, dans les 6 options de M6.
   - Le seuil de 3 est atteint.
   - Après mes correctifs (M3d, M4, M5b), il restera 10Q1[d] et l'option [c] de la question 13 fusionnée, plus les 6 options ambiguës.
2. **Approximation prise pour l'égalité ou la valeur exacte.**
   - Radical comparé à un entier (l'étiquette existante `comparaison-radical-et-entier` suffit) : 10Q1[a] et 14Q1[a] (étiquetées) ; 11Q3[d], 12Q2[c], 14Q2[a], 15Q4[c] (muettes).
   - Hors radical-entier (étiquette neuve utile) : 09Q3[b], 11Q5[b], 11Q5[c], 16Q5[b], soit 3 questions.
3. **Signe perdu en distribuant k(a − b).**
   - 10Q3[a], 13Q1[c], 14Q5[b] : le seuil de 3 est atteint.
   - À ne pas confondre avec `moins-devant-parenthese`, déjà posée en 12Q1[a], 12Q6[c] et 13Q6[a]. Sa variante miroir 13Q6[d] est muette.

Deux autres erreurs récurrentes restent sous le seuil (2 occurrences chacune) :
- comparer les seuls radicandes : 09Q3[c], 16Q3[d] ;
- faire entrer le coefficient sous la racine sans l'élever au carré : 14Q1[c], 16Q2[c].

**Observation hors tranche.** 13, 15 et 16 exigent des identités du ch. 03 et restent au ch. 17, identités données. Une autre tranche a placé 2005 Ex2 au ch. 03 : la règle de placement est à trancher.

## Chiffre final

- **Questions auditées :** 46, toutes re-résolues à l'aveugle.
- **Clés fausses :** 0.
- **Questions à reprendre :** 23, soit 1 critique (14 Q4) et 22 majeures.
  - 11 de ces reprises ne touchent que l'explication ou l'étiquette : 09Q2, 11Q1, 12Q1, 12Q4, 12Q5, 13Q1, 13Q5, 14Q3, 15Q2, 15Q5, 16Q6.
- **Retouches mineures :** 15 autres questions.
- **Questions sans constat :** 8 (09Q3, 09Q5, 10Q3, 11Q5, 13Q7, 14Q1, 15Q6, 16Q5).

Aucun fichier modifié.