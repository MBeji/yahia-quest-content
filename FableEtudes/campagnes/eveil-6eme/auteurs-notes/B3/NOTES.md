# Notes de l'auteur B3 — 04-nutrition · 06-reproduction-florale · 05-milieu-chaines-alimentaires

Lu en entier : prompt auteur, skills (content-ecole-tn, content-engine + références, content-cours, content-interactif, prof-eveil-primaire), fiche (en-tête, §1 dont §1.7, §2 unités 3 et 4, §4, §4 bis, §6.0–6.5, §7.23–7.25, §7.28, §7.31–7.35, §7.36–7.42), PLAN V1–V5, manuel 103604 p.84–95 (nutrition), 96–107 (fleur), 108–117 (milieu) **à l'image**.

## Table des écarts

### 04-nutrition
| # | écart | traitement |
|---|---|---|
| N1 | « سلامة الغذاء / قواعد صحّية » (guide p.99, جذاذة 4 تقييم ج, manuel p.95 6-ب et 7) : une phrase dans le cours, aucune règle enseignée ni exercée | nouvelle section 9 au patron + quiz + exercices (multi, mcq) |
| N2 | السكّري et ضغط الدّم (manuel p.93–94, مفاهيم p.93) cités sans signe ni exercice | lignes du tableau « إفراط », exemple, questions |
| N3 | conception « الأغذية = فطور / غداء / عشاء » (جذاذة 4, p.118) sans piège ni distracteur | piège dans la section « الوجبة المتوازنة » + distracteur muet (id proposé) |
| N4 | confusion entre maladies de carence : tag utilisé par des distracteurs mais absent de `coursePitfalls` et sans `::: piege` | piège ajouté + `coursePitfalls` |
| N5 | النشويات / السكّريات : le manuel (p.86) range le pain, la pomme de terre… sous « السكّريات » ; le cours les sépare sans le dire | une phrase (النشويات نوع من السكّريات) |
| N6 | évaluation n° 2, T1-أ / T1-ب (guide p.128–129) et tableau الخطأ/الصواب (guide p.98), manuel p.95 6-أ et 7 : non repris | questions reprises, `manuel` déclaré |
| N7 | formes : 100 % QCM | multi, matching, document, une question libre |
| N8 | erreurs à ne pas reprendre : « الهزال الرّزي » comme clé, vitamine D « يكسب مناعة » (guide p.133), lait rangé côté énergie (guide p.97), eau « avant le repas » | rien de tout cela n'est repris |

### 06-reproduction-florale
| # | écart | traitement |
|---|---|---|
| F1 | حاجز p.152 « الخلط بين التأبير والإخصاب » : distracteurs partout, mais aucun `::: piege` et tag absent de `coursePitfalls` | piège dans la section الإخصاب + `coursePitfalls` |
| F2 | التأبير par l'**homme** (palmier, manuel p.100, 107 ; guide p.153) : cité, jamais montré ni exercé | exemple + question |
| F3 | vocabulaire التأبير ≠ التلقيح (التلقيح = vaccination en 6ᵉ) et conception § 1.7 n° 5 (« la fleur devient fruit par التلقيح, des parties de la fleur portées par le vent ») | `> ⚠️` + question libre + distracteurs |
| F4 | expérience de la fleur sous sachet (manuel p.103 « أقيّم », guide p.153) : une seule question en mots | question visuelle SVG (reprise) |
| F5 | ordre des étapes du cycle (manuel p.97, 108 1-أ) et légende des organes (manuel p.99 6, p.100 1-ب) : absents en forme native | ordering + matching sur figure SVG numérotée |
| F6 | ثمرة كاذبة (manuel p.107 « معجمي ») posée en cas limite d'une section déjà chargée | déplacée dans une section propre « الثمرة الحقيقيّة والكاذبة » |
| F7 | classification حوليّة/دائمة : liste du manuel p.106 (اللفت، الفجل، الثوم، الخرشوف) ambiguë | jamais utilisée comme clé |

### 05-milieu-chaines-alimentaires
| # | écart | traitement |
|---|---|---|
| M1 | **V4** : le cours pose « تركيد ← ترشيح ← تغلية ← تعقيم » comme règle ordonnée et la 03-revision Q6 en demande l'ordre | section réécrite : « ماء صافٍ ≠ ماء صالح », deux gestes (إزالة الشوائب / قتل الجراثيم), schéma de la station de traitement à **lire** (guide p.166) ; Q6 remplacée par une lecture de schéma |
| M2 | « ماذا يحدث si une maillon disparaît » (guide p.162 تقييم أ, وضعيّة مشكل du criquet, manuel p.108 1-ب pesticides → pollinisation) : absent | nouvelle section 9 + piège + exercices |
| M3 | chaîne aquatique (manuel p.112 1-ب, guide p.145 : عوالق نباتيّة → حيوانيّة → يرقات → أسماك) : absente | exemple + ordering |
| M4 | conception « l'eau polluée = eau avec de la terre » (guide p.163) ; crue de 1969 | piège/exemple |
| M5 | manuel p.116–117 : 7-أ (diagnostic par symptômes) et 7-ب (choix des solutions) | matching et multi, `manuel` déclaré |
| M6 | formes : 100 % QCM | ordering, matching, multi, document SVG, question libre |

## Fait

- **Cours** : 04 (+ section 9 « سلامة الغذاء », piège repas≠groupes, piège carences, tableau السكّري / ضغط الدم, phrase النشويات⊂السكّريات) · 06 (+ section « الثمرة الحقيقيّة والكاذبة », piège التأبير≠الإخصاب, التأبير par l'homme, `> ⚠️` التلقيح) · 05 (+ section « حلقة تغيب », section potabilisation réécrite avec le schéma de la station à lire, plancton).
- **Défaut hérité corrigé** : six gras coupés par un retour à la ligne (`**…\n…**`) laissaient des `**` affichés (rendu `renderLesson`) dans les trois cours ; recollés.
- **Quiz** : +1 question (d2) dans chacun des trois chapitres. **Exercices** : 28 questions ajoutées en fin de tri (difficulté ≥ max du fichier, ids stables), 4 remplacées à rang et difficulté égaux, 2 reformulées. Reprises déclarées (`manuel` au niveau du fichier) : voir le rapport.
- Contrôles passés : `content:check`, `content:qa` (0 erreur, 0 avertissement sur B3), `content:figures:check`, `content:tranche --fresh --strict-longest` (0/20 clé la plus longue, 0 paire proche, 0 recul de patron), `prettier --check`, rendu (`renderLesson`/`renderSummary`, vitest jetable supprimé).
