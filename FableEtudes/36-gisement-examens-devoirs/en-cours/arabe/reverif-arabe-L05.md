# Re-vérification ciblée — gisement arabe 9ᵉ, lot L05

> Auditeur indépendant, 2026-10-14. Objet : l'état de `/home/user/wt-argis` au commit `ec5dd594`, plus les retouches
> L05 déjà présentes depuis `4998ca60`, comparé à `audit-arabe-L05.md`. Journal de l'auteur lu :
> `auteurs-notes/L05/CORRECTIONS.md`. Aucune écriture dans `content/` ni dans git.
> Contrôles : les 7 fichiers relus en entier ; questions retouchées et voisines résolues de nouveau à l'aveugle ;
> mesure des clés strictement les plus longues et les plus courtes, sans tashkīl et en brut ; `renderLesson` et
> `renderSummary` du ch. 06 exécutés (jiti + alias `@`) ; page `dir=rtl` rendue dans Chromium 1194 : questions
> retouchées après `isolateLtrRuns`, nouvelle section du cours, carte du résumé.

## 1. Mes textes, mot pour mot

| défaut | état | remarque |
|---|---|---|
| C-1 13 Q7 | ✓ conforme | énoncé, option b, étiquette, explication |
| C-2 14 Q4 | ✓ conforme | |
| M1 12 (الأعلى, placée en Q5) | ✓ conforme | Q4 en d2 (m1) ✓ |
| M2 05/07 Q3 | ✓ conforme | |
| M3 05/08 Q5 | écart 1 | voir § 2 |
| M4 05/08 Q1 | écart 2 | voir § 2 |
| M5 13 Q1 / Q3 / Q6 | ✓ (variantes) | Q1 : « صيغةٌ لا تصغيرَ فيها » sans « فَعِيل » — c'est mieux (évite d'écarter une option de Q2) ; Q3 et Q6 : écart 3 |
| M6 14 Q3 | ✓ conforme | options réordonnées, clé a |
| M8 14 Q5 | écart 1 | |
| M9 06 Q4 | ✓ conforme | étiquette de « مَحْلُومٌ » retirée (juste) — mais voir R-2 |
| M11 01 Q3 (ex-Q2) | ✓ conforme | options réordonnées |
| M12 01 Q6 | ✓ conforme | |
| M13 01 Q7 | écart 4 | |
| m2, m3 (+ énoncé), m4, m6 | ✓ conformes | |
| m10 01 Q1 (ex-Q3) en d1 et en tête | ✓ | |
| m9 01 Q2 (ex-Q1) | écart 5 : non appliqué | voir § 2 |

## 2. Écarts déclarés par l'auteur — jugement

1. **Explications de `short_answer` sans la réponse littérale (05/08 Q5, 14 Q5, et 13 Q3/Q6) — ACCEPTÉ.**
   Le motif est fondé : `quest-hint-button.tsx` révèle l'explication **avant** la réponse (indice payant). Pour un
   QCM l'élève doit encore choisir ; pour une réponse à taper, une explication qui contient la clé la donne à
   recopier. Les quatre explications enseignent toujours la méthode jusqu'à un pas de la clé, et la fuite de 05/08
   Q5 vers Q7 (« الياء تنقلب همزة ») a bien disparu. Vérifié : 05/08 Q5, 14 Q5, 13 Q3 et 13 Q6 — aucune n'écrit
   la clé, aucune ne contredit une erreur attendue (`expectedMistakes`).
2. **05/08 Q1 devient le وزن de « سَاهَمَ » (d1) — ACCEPTÉ.** L'objection est juste : l'énoncé de Q4 (« عن هذا
   الاشتراك … يدلّ على المشاركة ») aurait donné la clé de mon item sur le sens, pour quiconque le rencontre après Q4
   au donjon. La nouvelle Q1 est résolue de nouveau à l'aveugle : فَاعَلَ, clé b ✓ ; racine donnée, étage d1
   honnête ; étiquette `wazn-qarib-khalt` exacte sur تَفَاعَلَ. L'explication dit « «تَفَاعَلَ» يزيدُ تاءً في أوّلِه », ce qui
   aide un peu Q2 (تَآمَرَ = تَفَاعَلَ) ; mais Q2 demande aussi le sens et la lecture de « آ » : indice tolérable, pas
   une fuite de clé. Aucun doublon avec le publié du ch. 05.
3. **13 Q3 et Q6 : clés retirées des explications — ACCEPTÉ** (même motif qu'au point 1). Les fuites vers Q4 et Q7
   restent fermées : aucun poids n'est nommé.
4. **01 Q7 : QCM 2×2 avec un suffixe descriptif par option — ACCEPTÉ.** Re-résolu : b ✓. Chaque suffixe décrit
   exactement la forme qu'il suit, donc aucun indice n'y est ajouté. Le plan reste 2×2 : une option muette (a, deux
   erreurs) et deux options étiquetées `muthanna-ana`. Ni clé la plus longue ni clé la plus courte, en brut comme
   sans tashkīl. La phrase d'accord est corrigée (« تتبعُه كلُّها »).
5. **01 Q2 (ex-Q1) : m9 non appliqué — REFUSÉ en partie.** L'objection (« le mot de l'option a serait doublé ») ne
   tient pas : une forme fausse présente deux fois ne désigne aucune clé. Le défaut demeure : « وَحِيدَاتٍ … لثلاثٍ
   فأكثرَ » s'élimine par la prémisse « الفتاتين ». Pour lever l'objection, je propose une autre forme, sans mot
   répété (R-4).

## 3. Questions retouchées et voisines, résolues de nouveau à l'aveugle

| fichier | questions | résultat |
|---|---|---|
| 12 / 06 | Q1–Q6 | toutes justes (Q5 الأَعْلَيَانِ ; Q6 « خُطْوَتَيْنِ أُوْلَيَيْنِ », clé d) |
| 05 / 07 | Q3, Q5 | justes |
| 05 / 08 | Q1, Q2, Q4, Q5, Q6, Q7 | justes |
| 13 / 06 | Q1–Q7 | justes |
| 14 / 06 | Q2–Q5 | justes ; plus de double réponse en Q4 |
| 06 / 07 | Q3, Q4, Q5, Q6 | justes (Q4 حُلْمٌ) |
| 01 / 07 | Q1–Q7 | justes |

**Clés fausses : 0.**

## 4. Fuites et indices de forme — constats

- **R-1 [MAJEUR] Cours du 06 → mission.** L'exemple de la nouvelle section (« غَادَرَ ← مُغَادَرَةٌ ») est mot pour mot
  la clé de 06/07 Q3. La question `verifie` (« تَبَادَلَ ← تَبَادُلٌ ») est la clé de 06/07 Q5 l3. Les deux items de
  l'examen deviennent un simple rappel du cours. Correctif en § 5.
- **R-2 [MINEUR] Clé strictement la plus courte en 06 Q4** (حُلْمٌ, 3 lettres ; les autres 4, 5 et 4). Remplacer
  « تَحَلُّمٌ » par « حِلْمٌ » (texte en § 6). C'est le مصدر d'un autre verbe de la même racine (« حَلُمَ », être
  indulgent) : la clé n'est plus isolée par sa longueur, et le piège porte sur la voyelle.
- **R-3 [MINEUR] Clé strictement la plus courte en 01 Q5** (« الألفُ؛ لأنّه مثنّى مرفوعٌ » : 22 lettres contre 35, 29 et
  29) et **en 05/08 Q4** (« تَعَاوَنَّا … » : 30 contre 37, 32 et 33). Ces items n'ont pas été retouchés ; je ne les
  avais pas mesurés au premier passage.
- **R-5 [MINEUR] Exemples des explications égaux aux clés de missions publiées du même chapitre :**
  - 12 Q5 : « (عصا ← عصوان) » est la clé de `12/quiz` Q3 ;
  - 13 Q6 : « عامِل ← عُوَيْمِل » et « كِتاب ← كُتَيِّب » sont les clés de `13/04-defi` Q2 et Q3 ;
  - 13 Q7 : « كُتَيِّب » est la clé de `13/04-defi` Q3. Ce texte vient de mon C-1.
- **R-6 [MINEUR] 14 Q2 → Q3.** L'explication de Q2 (« تنعتُ مؤنّثًا وتطابقُه … ») donne le critère qui départage a
  et b en Q3 (accord du نعت).
- Le reste est propre : 0 clé strictement la plus longue sur les 7 fichiers, en brut comme sans tashkīl. Aucune
  autre fuite vers une question suivante ni vers le publié (recherches dans quiz et missions des ch. 05, 06, 12,
  13 et 14 ; les mots proposés ci-dessous n'y figurent pas).

## 5. Nouvelle section du cours du 06 (« 📎 تذكير: مصدر الفعل المزيد ») et ligne du résumé

- **Exactitude :** conforme au tableau du manuel tel que le transcrit le ch. 05 (فَعَّلَ تَفْعِيل, أَفْعَلَ إِفْعَال,
  فَاعَلَ مُفَاعَلَة, تَفَعَّلَ تَفَعُّل, تَفَاعَلَ تَفَاعُل, افْتَعَلَ افْتِعَال). Le manuel ne donne que مُفاعَلة pour فاعَلَ
  (« فِعال » est en « للتوسّع » au ch. 05). Aucune clé de la mission n'en dépend : « زِحام » n'est pas proposé en
  06 Q6.
- **Présence dans le HTML :** ✓. `renderLesson` émet `<h2 id="section-8">📎 تذكير: مصدر الفعل المزيد</h2>`, le bloc
  `lesson-blk--exemple` et le bloc `lesson-blk--verifie` (réponse dans `<details>`). Les flèches « ← » sont isolées
  (U+2066/2069). `renderSummary` émet une carte « مصدر الفعل المزيد ». Rendu Chromium `dir=rtl` : ordre correct.
- **Patron :**
  - la règle est en prose, sans bloc typé ([MINEUR] R-8) ;
  - la section n'a pas d'ancrage. C'est acceptable pour un rappel, comme l'a décidé le pilote ;
  - « (الفصل الخامس) » renvoie au numéro de dossier, alors que l'élève voit les chapitres dans l'ordre du manifeste,
    où ce chapitre n'est pas le 5ᵉ ([MINEUR]) ;
  - la carte du résumé commence par « (تذكير من الفصل الخامس): … » : l'essence s'ouvre sur une parenthèse
    ([MINEUR]).

## 6. Correctifs (textes vérifiés : longueurs mesurées, rendu Chromium, absence des mots dans le publié)

**R-1 · `06-al-mushtaqqat/cours.md`, section « 📎 تذكير: مصدر الفعل المزيد »** — remplacer tout le corps de la section par :

```
::: propriete
**مصدرُ الفعلِ المزيدِ** يُصاغُ على وزنٍ معلومٍ بحسبِ وزنِ فعلِه، كما درستَ في درسِ «معاني صيغِ الزّيادةِ»: فَعَّلَ ← تَفْعِيل، أَفْعَلَ ← إِفْعَال، فَاعَلَ ← مُفَاعَلَة، تَفَعَّلَ ← تَفَعُّل، تَفَاعَلَ ← تَفَاعُل، افْتَعَلَ ← افْتِعَال.
:::

::: exemple مصدرُ «حَاوَرَ»

«حَاوَرَ» على «فَاعَلَ»، فمصدرُه على «مُفَاعَلَة»: **مُحَاوَرَةٌ**، **لأنّ** مصدرَ المزيدِ يتبعُ وزنَ فعلِه.

:::

::: verifie
ما مصدرُ «تَعَارَفَ» (على «تَفَاعَلَ»)؟

---

**تَعَارُفٌ**: مصدرُ «تَفَاعَلَ» على «تَفَاعُل» بضمِّ ما قبلَ الآخِرِ.
:::
```

**Ligne de `06-al-mushtaqqat/resume.md`** — remplacer par :
`- **مصدر الفعل المزيد**: على وزنٍ معلومٍ بحسبِ وزنِ الفعل (تذكيرٌ من درسِ «معاني صيغ الزّيادة») — فَعَّلَ ← تَفْعِيل، فَاعَلَ ← مُفَاعَلَة، تَفَعَّلَ ← تَفَعُّل، افْتَعَلَ ← افْتِعَال.`

**R-2 · 06/07 Q4** — option d : `حِلْمٌ`, étiquette `arabe.masdar.wazn-fi3l-akhar` (inchangée). Dans l'explication,
remplacer « و«تَحَلُّمٌ» مصدرُ فعلٍ مزيدٍ آخرَ هو «تَحَلَّمَ» على «تَفَعَّلَ». » par
`و«حِلْمٌ» بكسرِ الحاءِ مصدرُ فعلٍ آخرَ من الجذرِ نفسِه هو «حَلُمَ» (صارَ حليمًا لا يغضبُ سريعًا)، لا مصدرُ «حَلَمَ».`
Longueurs : 3, 4, 5, 3. La clé n'est plus isolée.

**R-3 · 01 Q5** — option d : `الألفُ؛ لأنّه مثنّى مرفوعٌ حُذفت نونُه` (32 contre 35, 29 et 29 ; l'explication dit déjà
« حُذفتِ النونُ »). **05/08 Q4** — option d : `تَعَاوَنَّا عَلَى تَجْمِيلِ شَوَارِعِ المَدِينَةِ كُلِّهَا` (35 contre 37, 32
et 33 ; l'option c finit déjà par « كُلِّهَا »).

**R-4 · 01 Q2 (ex-Q1)** — option d : `«وَحِيدَتَا»: مثنّى منصوبٌ بحذفِ النونِ` (sans étiquette ; c'est la règle de
Q1 — les cinq verbes — transportée à tort sur le nom ; longueurs 28, 44, 28, 31). Dans l'explication, remplacer
« و«وَحِيدَاتٍ» جمعُ مؤنّثٍ لثلاثٍ فأكثرَ. » par
`و«وَحِيدَتَا» تحذفُ النونَ كما تُحذفُ من الأفعالِ الخمسةِ في النصبِ، ونونُ المثنّى في الأسماءِ لا تُحذفُ إلّا عندَ الإضافةِ.`

**R-5** — 12 Q5, explication : « (عصا ← عصوان) » → `(قَفا ← قَفَوانِ)`.
13 Q6, explication : « كما في «عامِل ← عُوَيْمِل» » → `كما في «حاجِب ← حُوَيْجِب»`, et « (كِتاب ← كُتَيِّب) » →
`(غَزال ← غُزَيِّل)`.
13 Q7, explication : « كما في «كُتَيِّب» » → `كما في «غُزَيِّل»`.

**R-6 · 14 Q2**, explication : « صفةُ نسبةٍ تنعتُ مؤنّثًا وتطابقُه في التعريفِ والإعرابِ » → `صفةُ نسبةٍ تنعتُ ما قبلَها`.

## Bilan

- **Clés fausses :** 0.
- **Majeur restant :** 1, R-1 (le cours du 06 donne deux clés de la mission).
- **Mineurs restants :** 7 —
  - R-2 et R-3 : clé strictement la plus courte (06 Q4, 01 Q5, 05/08 Q4) ;
  - R-4 : distracteur éliminé par la prémisse (01 Q2) ;
  - R-5 : exemples d'explication égaux à des clés publiées (12 Q5, 13 Q6, 13 Q7) ;
  - R-6 : critère de 14 Q3 donné par l'explication de 14 Q2 ;
  - patron de la section du 06 : règle sans bloc typé et renvoi « الفصل الخامس » (corrigés par le texte R-1) ;
  - carte du résumé du 06.
- **Écarts de l'auteur :** 1 à 4 acceptés ; 5 refusé en partie (R-4 en donne un texte qui lève l'objection).
- **Rendu :** propre (Chromium `dir=rtl`).
- **Verdict :** à fusionner après R-1 ; les mineurs peuvent passer dans la même retouche.

## Suite donnée par le pilote (2026-10-14)

R-1 à R-6 et ligne du résumé appliqués mot pour mot par l'auteur. Écart accepté : ancrage de deux
paragraphes (« سَاعَدَ ») avant le bloc `propriete`, exigé par le gate qa (é35 C-2) ; « سَاعَدَ »/« مُسَاعَدَة »
n'apparaissent dans aucune mission des ch. 05–06 (grep). Tranche 01, 05, 06, 12–14 : aucune clé
strictement la plus longue dans les missions d'examen ; les 36/84 du 01+06 sont la dette des missions
publiées (patron), hors lot. Paire 0,45 01/07#3 ↔ 06/07#9 (seuil) : même savoir-faire, autres données,
gardée. **L05 prêt à livrer.**
