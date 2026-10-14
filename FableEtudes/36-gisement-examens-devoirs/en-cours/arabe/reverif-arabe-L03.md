# Re-vérification ciblée — gisement arabe 9ᵉ, lot L03 (après corrections, commit `275dbbc8`)

> Auditeur indépendant, 2026-10-14. Base : `audit-arabe-L03.md` (même auteur) et le journal
> `auteurs-notes/L03/CORRECTIONS.md`. Périmètre : `content/arabic/09-al-intaj-al-kitabi/` (missions
> 07–13, `cours.md`, `resume.md`, `chapter.json`) et les deux familles neuves de
> `content/misconceptions.json`, dans `/home/user/wt-argis` (branche `wip/gisement-arabe-9eme`).
> Aucune écriture dans `content/` ni dans git.
>
> Contrôles outillés (moteur `eng-argis`) : `content:check` passe ; `content:qa --subject arabic
> --strict` : 0 erreur ; `content:tranche --chapters 09` : clé strictement la plus longue 0/70, 0 paire
> proche. Mesure maison sur les 36 QCM du lot : clé la plus longue 0 (avec ou sans diacritiques), la plus
> courte 0 sans diacritiques et 4 avec (10 Q1, 10 Q3, 11 Q7, 13 Q5). Coquilles d'origine : 0 restante.
> Rendu : `isolateLtrRuns` et Chromium `dir=rtl` sur les chaînes à chiffres et sur le paragraphe numéroté
> de 11 Q7 (« «(1) … (2) … » », « في (3) و(4) ») : l'ordre affiché suit le texte source.
> `renderLesson` / `renderSummary` : le bloc `propriete` « تعديلُ الموقفِ » sort bien en
> `lesson-blk--propriete`, et la puce est présente dans le résumé.

## 1. Re-résolution à l'aveugle (questions retouchées et leurs voisines)

Les 52 questions des sept missions ont été re-résolues, 10 Q3 ayant été supprimée. Mes réponses
coïncident avec chaque `correctOption` / `answerKey`, ce qui donne **0 clé fausse** :

| Mission | Clés retrouvées |
| --- | --- |
| 07 | Q1 a · Q2 d · Q3 c · Q4 b · Q5 b-e-d-a-c · Q6 {a,b,e,f} · Q7 c |
| 08 | Q1 {a,c,e} · Q2 l1-r4/l2-r2/l3-r1/l4-r3 · Q3 c · Q4 b · Q5 d · Q6 d · Q7 d-c-f-a-e-b |
| 09 | Q1 a · Q2 b · Q3 {a,c,e} · Q4 a · Q5 c · Q6 l1-r3/l2-r1/l3-r4/l4-r2 · Q7 a |
| 10 | Q1 d · Q2 a · Q3 b · Q4 b · Q5 d · Q6 {a,c,e,f} · Q7 d-f-b-e-a-c |
| 11 | Q1 a · Q2 c · Q3 c · Q4 a · Q5 l1-r2/l2-r4/l3-r1/l4-r3 · Q6 {a,c,e} · Q7 b |
| 12 | Q1 a · Q2 {a,c} · Q3 d · Q4 c · Q5 d · Q6 b · Q7 b-d-a-c · Q8 l1-r3/l2-r1/l3-r2 |
| 13 | Q1 b · Q2 b · Q3 d · Q4 l1-r2/l2-r4/l3-r1/l4-r3 · Q5 c · Q6 {a,c} · Q7 d · Q8 c · Q9 a |

Mes textes de l'audit ont été appliqués à l'identique : 07 Q4 et Q6 f, 08 Q5 / Q6 / Q7 f, 09 Q2, Q4
et Q6 l1, 10 Q1, Q4, Q5, Q6 et Q7, 11 Q3, Q4 et Q7, 12 Q2, Q5, Q6 et Q7 b, 13 Q3 b, Q5 c, Q6, Q7 et
Q9 b. Je les ai revérifiés en place :
- chacun a une seule réponse juste ;
- aucun distracteur n'est défendable ;
- les étiquettes posées sont exactes ;
- 08 Q5 forme une grille 2×2 où chaque valeur figure deux fois.

## 2. Écarts déclarés par l'auteur

1. **Clé la plus courte 4/36 avec diacritiques, 0 sans.** Accepté. 4 cas sur 36 font 11 %, sous le
   hasard (25 %), et les quatre items sont de types différents : il n'y a pas de motif. La mesure
   pertinente est celle sans diacritiques, qui donne 0.
2. **Bloc de cours qui donne l'ordre du plan (10 Q3, 10 Q7).** C'est un **enseignement légitime**,
   pas une fuite. Une fuite est un énoncé ou une explication qui livre la clé d'un *autre item*. Ici
   le cours enseigne un plan, comme il le fait déjà pour le دحض (08 Q7) et le حوار (07 Q5). 10 Q3
   reste discriminant, car sa grille 2×2 (قد/ليس × غيرَ أنّ/بناءً على ذلك) exige de reconnaître à la
   fois la concession et le connecteur. 10 Q7 est une application du plan enseigné, au même niveau
   que 08 Q7. L'exemple du cours, sur le thème « السهر », ne reprend aucun item.
3. **Non appliqués (08 Q2, 12 Q4, 12 Q8 ; `multi` 08 Q1, 09 Q3, 11 Q6 à 3 justes sur 6).**
   - **`multi`** : rien n'est nécessaire. Les nombres de bonnes réponses sont désormais 4, 3, 3, 4,
     3, 2 et 2 : le nombre ne se déduit plus.
   - **08 Q2** : rien n'est nécessaire. Que l1 et l2 soient dans l'énoncé convient à un d2, car le
     geste demandé est justement de rattacher la consigne aux rôles.
   - **12 Q4** : rien n'est nécessaire. Les distracteurs faibles restent acceptables en d2.
   - **12 Q8** : la retouche est facultative. Si on la fait, voici le texte vérifié (paires
     inchangées l1-r3, l2-r1, l3-r2 ; chaque paire reste unique, et l'écho lexical diminue) :
     - r1 « تعدادُ الأخطارِ ثمّ السكوتُ عمّا يفعلُه الشابُّ بدلَ ذلك »
     - r2 « رسمُ مشهدِ اللاعبينَ حولَ الطاولةِ بلا سببٍ يُقنعُ »
     - r3 « ترديدُ الاتّهامِ الذي نشرَه الصديقُ دونَ تفسيرٍ جديدٍ »
4. **13 Q4 l1 « قالَ أحدُ علماءِ الاجتماعِ: لا نهضةَ لأمّةٍ بغيرِ تعليمٍ ».** Accepté. C'est bien une
   حجّة سلطة (مرجع معرفيّ), et le texte retire le proverbe qui faisait triple emploi avec 04-defi Q2 et
   l'ancien 09 Q4. Reste un recoupement mineur, sans gravité dans un appariement des quatre types :
   « قول مختصّ = سلطة » est déjà testé par `quiz` Q4 et `06-defi` Q2.
5. **Étiquette ta3dil non posable sur un `multi` (10 Q6 b).** Accepté : c'est une contrainte du
   format.
6. **Textes allongés.** Je les ai relus et ils sont grammaticaux et justes : 11 Q3 c « الصادقَ في
   قولِهِ » et d « والأسواقِ », 12 Q6 b « بهِ », 09 Q4 et 08 Q5 « تحدّدُهُ », de même que 07 Q1 a/d,
   07 Q4 b, 08 Q3 c, 11 Q2 a/c, 11 Q4 a et 13 Q2 b/c. **Une exception, 08 Q4** : voir R-1.

## 3. Familles neuves (`misconceptions.json`)

- `arabe.hijaj.ta3dil-ila-radd-aw-taqrir` :
  - **Libellé** : « تردُّ الموقفَ كلَّه أو تقبلُه كلَّه بدلَ تعديلِه… ». Il nomme une seule erreur,
    ne pas nuancer, dans l'un ou l'autre sens. Les libellés fr et en sont fidèles.
  - **Pose** : 10 Q1 a et b, Q2 c et d, Q3 c, Q4 c, soit **4 questions distinctes**. Chaque option
    exécute exactement cette erreur.
  - **Options laissées muettes à juste titre** : 10 Q3 a (deux erreurs) et 10 Q1 c (concession sans
    correction).
- `arabe.hijaj.nawahi-bila-ta3lil` :
  - **Libellé** : « تسردُ نواهيَ ونصائحَ بلا تعليلٍ… ». Il nomme une seule erreur.
  - **Pose** : 12 Q1 d, 13 Q1 a, 13 Q2 c, soit **3 questions**, ce qui atteint le seuil. 08 Q1 f
    n'est pas posable, car c'est un `multi`.
- Les deux ids sont cités par le cours : le bloc C-10-0 couvre la première famille, et les sections
  الفقرة / الحجّة couvrent la seconde.

## 4. Fuites et indices de forme

- Les fuites relevées à l'audit sont fermées :
  - Q8 → Q2 du 10 (b et f reformulées) ;
  - explication de 10 Q1 → Q2 ;
  - 10 Q7 e → Q6 ;
  - 11 Q6 → Q7 (paragraphe refait : « الانشغالُ عن الدروسِ », « الإخفاقُ في الامتحانِ » n'apparaissent
    dans aucune option de 11 Q4 ni de 11 Q6) ;
  - 08 Q7 f → 12 Q6 ;
  - 09 Q6 l1 → Q2 ;
  - 12 Q7 b → Q5.
- Résiduel accepté : l'explication de 10 Q2 (« رغبتُه … مشروعةٌ فتُقَرُّ … حصرُ القيمةِ … فيُصحَّحُ »)
  oriente Q3 et Q4. C'est la justification même de la clé de Q2, que le cours enseigne désormais ;
  Q3 exige encore le choix du connecteur, et Q4 celui de la forme de phrase. Aucune action.
- **R-1 (indice de forme, à corriger)** : en **08 Q4**, la clé b est la seule option à porter
  « طويلًا » (« … يبقى طويلًا بعدَ انتهائِهِ »). Les trois distracteurs partagent un second membre
  identique, et la clé est l'intruse. C'est le marqueur « présent dans la clé seule » de
  `quality-bar.md`. Correctif : mettre « طويلًا » dans les quatre options.
  - a « قد يبدو العرضُ المسرحيُّ تسليةً، وخلاصةُ القولِ أنّ أثرَهُ في المتفرّجينَ يبقى طويلًا بعدَ انتهائِهِ »
  - c « قد يبدو العرضُ المسرحيُّ تسليةً، ومعنى ذلكَ أنّ أثرَهُ في المتفرّجينَ يبقى طويلًا بعدَ انتهائِهِ »
  - d « قد يبدو العرضُ المسرحيُّ تسليةً، وذلكَ لأنّ أثرَهُ في المتفرّجينَ يبقى طويلًا بعدَ انتهائِهِ »
  - b est inchangée.
  - Longueurs sans diacritiques : a 85, **b 76**, c 82, d 78. La clé redevient la plus courte, mais
    de 2 caractères seulement, et cela tient au connecteur « غيرَ أنّ », plus court par nature : c'est
    le seul cas du lot, au niveau du hasard. Explication inchangée ; étiquettes inchangées.

## 5. Bloc de cours « تعديلُ الموقفِ »

- **Exactitude** : juste. Le bloc couvre la concession, puis le استدراك, puis la thèse corrigée.
  L'exemple « قد يكونُ السهرُ نافعًا … غيرَ أنّ … فالمراجعةُ المنتظمةُ هي الأساسُ » exécute exactement
  le plan. « قد » + mudāriʿ y sert de concession (possibilité), ce qui est cohérent avec la mise en
  garde du cours 10 (« قد » + mudāriʿ n'est pas un توكيد). Le bloc est conforme au manuel 101909
  (p. 12 « تعديل موقفه », p. 315 « إثبات الأطروحة أو نفيها أو تعديلها »).
- **Patron (R-2, mineur)** : le bloc est placé **après** le `::: retenir` qui clôt la section
  « ✍️ الإنتاجُ (2) ». Le retenir n'est donc plus le dernier mot de la section, et ne mentionne pas
  la notion. Correctif :
  - déplacer le bloc `propriete` tel quel juste avant le `::: verifie` de la même section ;
  - compléter le retenir de cette section par la phrase suivante, à ajouter en fin de paragraphe :
    « وإن طُلبَ تعديلُ الموقفِ فإقرارٌ بصوابِه ثمّ استدراكٌ يصحّحُ خللَه فأطروحةٌ معدَّلةٌ. »
- **HTML** : le bloc est présent, rendu en `lesson-blk--propriete`. Les flèches « ← » sont dans le
  sens de lecture RTL, comme ailleurs dans le cours.
- **`chapter.json`** : la source corrigée dit vrai (« الإنشاءُ حتّى دورةِ 2020 », technique 2020–2026,
  « مع تصحيحِ الأخطاءِ الطباعيّةِ »), conformément à la décision du pilote ; la ligne suivante est
  complétée.

## 6. Mineur restant

- **R-3 — explication de 13 Q3** : elle cite encore l'ancien texte de b.
  - Remplacer : « و«التعلّمُ والتضحيةُ …» عنوانٌ لا رأيَ فيه »
  - Par : « و«الحرصُ على التعلّمِ … والنجاحُ والخروجُ …» أسماءٌ معطوفةٌ بلا خبرٍ، فهي عنوانٌ لا رأيَ فيه »

## Bilan

| Constat | Résultat |
| --- | --- |
| Questions re-résolues | 52 |
| Clés fausses | 0 |
| Défauts critiques | 0 |
| Majeurs | 0 |
| Mineurs restants | 3 : R-1 (08 Q4, marqueur « طويلًا » dans la clé seule), R-2 (placement du bloc de cours et retenir), R-3 (citation périmée dans l'explication de 13 Q3) |
| Facultatif | 12 Q8 (texte au § 2.3) |
| Étiquettes | les deux familles sont conformes, leurs seuils atteints |
| Doublons et fuites relevés à l'audit | fermés |

**Verdict : livrable une fois R-1 appliqué** (une ligne par option). R-2 et R-3 sont recommandés dans
le même passage.

## Suite donnée par le pilote (2026-10-14)

R-1 (« طويلًا » ajouté à 08 Q4 a, c, d), R-2 (bloc « تعديلُ الموقفِ » déplacé avant le `verifie` de la section,
phrase ajoutée au `retenir`) et R-3 (explication de 13 Q3) appliqués mot pour mot ; 12 Q8 facultatif non pris.
`content:check` vert, prettier propre. **L03 prêt à livrer.**
