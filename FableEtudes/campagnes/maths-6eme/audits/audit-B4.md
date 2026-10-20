# Audit B4 — maths 6ᵉ, chapitres 16, 17, 18 et 19 (auditeur indépendant, opus)

> Valide pour les fichiers de `content/math-6eme/{16,17,18,19}-*` tels qu'au commit `ee2f55af` (branche
> `wip/maths-6eme-un-passage` ; dernier commit qui les touche : `5c7457dc` ; aucun changement non commité dans le lot
> au moment de l'audit). Ré-auditer si ces fichiers bougent. 2026-10-19.
>
> Rapport écrit chapitre après chapitre. Synthèse et verdict en fin de fichier. Les questions sont numérotées dans leur
> fichier (`quiz` Q1 = première question de `quiz.json`). Pour chaque remplacement : options `a`…`d` dans l'ordre,
> **(clé)** marque la bonne option, « muette » = sans `misconceptionTag`.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 sujets, exit 0).
- `content:qa -- --subject math-6eme` : 0 erreur ; 3 avertissements, tous hors lot (ch. 14).
- `content:figures:check` ✓.
- `content:tranche -- --chapters <4 slugs> --fresh --strict-longest --strict-lessons` ✓ : clé strictement la plus
  longue 0/57 (questions modifiées) ; positions 21/28/28/23 % ; patron de notion 0 en recul ; 0 paire proche
  **dans la tranche fraîche**.
- Le même `content:tranche` **sans `--fresh`** (les 166 questions du lot) : clé strictement la plus longue 21/143 = 15 %
  (sous le hasard) ; **27 paires proches**, toutes internes au lot sauf une. Elles sont traitées par chapitre plus bas.
  Les plus fortes : ch. 17, quatre copies d'une même question (Jaccard 1,00) ; ch. 18, cinq variantes du gabarit
  « مثلّث أطوال أضلاعه … نوعه » (0,65–0,80) ; ch. 18 `02-boss` Q6 ↔ `04-defi` Q4 (0,81) ; ch. 16 `quiz` Q3 ↔ `02-boss`
  Q1 (0,77, même figure). Un groupe gabarit inter-chapitres (×5, « مستطيل طوله … ما محيطه ») a trois membres au ch. 19 et
  deux au ch. 20.
- **Rendu** : les 4 cours et 4 résumés rendus par `renderLesson`/`renderSummary` (vitest jetable, supprimé), puis
  Chromium à 360 px avec les règles CSS de cellule de l'app (`unicode-bidi: plaintext`). Aucun débordement horizontal
  (`scrollWidth` = 360). Pas de `:::` laissé brut. Toutes les figures sont rendues (12/10/11/14). Il y a autant de
  `<details>` (vérifie repliés) que de sections (9/9/9/11). Tableaux lisibles, sauf un mineur au ch. 19 (m19-4).
  Fichiers jetables supprimés ; `git status` du moteur est propre.
- Notation : 0 chiffre arabe-indien, 0 groupe `\d \d{3}`, 0 LaTeX. Les seuls `،` entre crochets sont les noms d'angle du
  manuel `[بأ، بج]`, faits de lettres arabes, donc conformes.

**Points imposés.** M3 est tenu dans les 4 chapitres : la somme des angles = 180° n'est jamais énoncée ni demandée. Le
60° du triangle équilatéral (ch. 17) est un constat vérifié à la منقلة, le 45° du demi-carré (ch. 18) vient de la
diagonale qui partage l'angle droit, et le 3ᵉ angle du ch. 18 § 9 est **mesuré**. D-1 est jugé au ch. 19, avec un
défaut d'énoncé. D-2 est respecté : rien ne demande de scinder (sections : 9, 9, 9, 11).

**Reprises.** Je les ai confrontées à la fiche et au PDF `102609` (ص 25 et 49 relues à l'image) : données et items
justes. Les errata n° 2, 14, 15, 16, 17 et 64 sont appliqués. Le défaut dominant est ailleurs : **les cours prennent
pour ancrage l'activité même du manuel** (R-2), et la question qui reprend cette activité **redonne l'exemple résolu**.
Pour chaque cas, je choisis le moins coûteux des deux remèdes : soit changer les nombres du cours quand c'est une
propriété ou un `verifie` sans figure, soit écrire une variante. La variante **perd le champ `manuel`**, et j'indique
chaque fois la mise à jour de ce champ.

---

## Ch. 16 — `16-perpendicularite-parallelisme` (41 questions re-résolues)

**Clés : 41/41 justes**, aucune lettre ni ordinal dans les explications. Le cours a été re-résolu en entier : 20 : 2 = 10,
12 : 2 = 6 ; 5 cm ; 4 cm > 3 ; 5 > 4, triangle 5-5-8 ; 90 : 2 = 45 ; 45 : 2 = 22,5 ; 180 : 2 = 90. Tout est juste.
Les 12 figures sont vraies (codage ⊥/∥, médiatrice, construction au compas, bissectrice).
Patron : 9 sections, chacune T1 → T2 → T3 → T4 → T5 → T6 → T7 → retenir.
Reprises (`03-revision`, rév. 6 ex. 1 et ex. 3ج, guide p.89–90) fidèles.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (9 sections au patron) ;
- exhaustivité ✓, à une réserve près : « deux parallèles à distance donnée » (`03` Q2) n'est pas dit, voir m16-3 ;
- expérience ✓ ;
- illustration ✓ (12 figures vraies).

### Majeurs

**M16-1 — 13 questions redonnent un exemple, un piège ou un `verifie` du cours, ou en sont des doublons.**

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q4 | `verifie` § 🧭 (منصّف 180° → 90°) | « رسمنا منصّف زاوية قيسها 70°. ما قيس كلّ من الزاويتين الناتجتين؟ » · a `140°` (`math.num.operation-inverse-appliquee`) · b `20°` muette · c `35°` (clé) · d `70°` muette · exp. « المنصّف يقسم الزاوية نصفين متقايسين: 70° ÷ 2 = 35°. من كتب 140° ضرب في 2 بدل أن يقسم. » |
| `01-pratique` Q4 | propriété § ∥ (« حافّتا المسطرة ») | « أيُّ مثالٍ من الحياة يمثّل التوازي؟ » · a `حافّتا سطح الطاولة المتقابلتان` (clé) · b `حافّتا سطح الطاولة المتجاورتان` (`math.geo.perpendiculaire-et-parallele-confondus`) · c `عقربا الساعة عند الثالثة` (même étiquette) · d `طريقان يلتقيان في مفترق` muette · exp. « الحافّتان المتقابلتان لسطح الطاولة المستطيل لا تلتقيان مهما امتدّتا، والبُعد بينهما ثابت: متوازيتان. أمّا الحافّتان المتجاورتان فتلتقيان في الركن بزاوية قائمة، وعقربا الساعة عند الثالثة كذلك: متعامدان. » |
| `02-boss` Q1 | même figure et mêmes options que `quiz` Q3 (Jaccard 0,77) | « ما وضعيّة المستقيمين في هذا الشكل؟ » + figure tournée (ci-dessous) · a `متوازيان` (`perpendiculaire-et-parallele-confondus`) · b `متعامدان` (clé) · c `متقاطعان غير متعامدين` muette · d `لا نحكم لأنّ الرسم مائل` muette · exp. « المربّع الصغير عند نقطة التقاطع علامة الزاوية القائمة، فالمستقيمان متعامدان. ميلُ الرسم على الورقة لا يغيّر شيئًا: نقرأ العلامة لا اتّجاه الخطوط. » |
| `02-boss` Q5 | cas limite mot pour mot de la propriété § 🚆 (mêmes lettres) | « في رسمٍ لغرفة، حافّة الرفّ (ر) توازي خطّ الأرض (ل)، والجدار (ج) عموديّ على (ل). ما وضعيّة (ج) بالنسبة إلى (ر)؟ » · a `(ج) ∥ (ر)` (`math.geo.regle-perpendiculaire-parallele-inversee`) · b `(ج) ⊥ (ر)` (clé) · c `منطبقان` muette · d `لا نحكم دون قيس` muette · exp. « (ر) ∥ (ل) و (ج) ⊥ (ل)، والعموديّ على أحد متوازيين عموديّ على الآخر: (ج) ⊥ (ر). ولا يمكن أن يوازيه، لأنّ (ج) يقطع (ر). » |
| `03-revision` Q6 | doublon de sens de `quiz` Q5 (même règle, mêmes options) | type `numeric`, difficulté 2 : « ن نقطة من الموسّط العمودي للقطعة [أب] ولا تقع عليها، و نأ = 7 سم. ما طول [نب] بالسنتيمتر؟ » · `answerKey.value` 7 · exp. « كلّ نقطة من الموسّط العمودي لـ [أب] تبعد عن أ بقدر ما تبعد عن ب، فـ نب = نأ = 7 سم. » |
| `04-defi` Q1 | exemple § 📏 (أب = 6, فتحة 4 → متساوي الساقين), aussi L4 ex. 1 | « ن نقطة من الموسّط العمودي لـ [أب] ولا تقع على (أب). قسنا نأ فوجدنا 6 سم، وقيس أب 6 سم أيضًا. ما الاسم الأدقّ للمثلّث أ ن ب حسب أضلاعه؟ » + figure équilatérale (ci-dessous) · a `قائم الزاوية` (`math.geo.classements-triangle-melanges`) · b `متساوي الساقين` (`math.geo.description-la-plus-precise-manquee`) · c `متساوي الأضلاع` (clé) · d `مختلف الأضلاع` (`math.geo.classement-triangle-par-cotes-errone`) · difficulté 3 · exp. « ن على الموسّط العمودي لـ [أب]، فتبعد عن أ وعن ب البعد نفسه: نب = نأ = 6 سم. والضلع الثالث أب = 6 سم أيضًا: الأضلاع الثلاثة متساوية، فالاسم الأدقّ متساوي الأضلاع. «متساوي الساقين» صحيح لكنّه ليس الأدقّ. » |
| `04-defi` Q2 | exemple § 🔣 étape 4 (« في المربّع المتجاوران متعامدان ») ; miroir de Q3 | « في الرباعيّ أبجد: (أب) ⊥ (بج) و (جد) ⊥ (بج). ما وضعيّة (أب) بالنسبة إلى (جد)؟ » · a `(أب) ∥ (جد)` (clé) · b `(أب) ⊥ (جد)` (`regle-perpendiculaire-parallele-inversee`) · c `متقاطعان في ب` muette · d `لا نستطيع الحكم دون قيس` muette · exp. « (أب) و (جد) كلاهما عموديّ على المستقيم نفسه (بج)، والعموديّان على مستقيم واحد متوازيان: (أب) ∥ (جد). » |
| `04-defi` Q3 | même exemple (« المتقابلان متوازيان ») | « (د1) ⊥ (د) و (د2) ⊥ (د)، و (د3) ⊥ (د2). ما وضعيّة (د3) بالنسبة إلى (د1)؟ » · a `(د3) ∥ (د1)` (`regle-perpendiculaire-parallele-inversee`) · b `منطبقان` muette · c `(د3) ⊥ (د1)` (clé) · d `لا علاقة بينهما` muette · exp. « (د1) و (د2) عموديّان على (د) نفسه، فهما متوازيان: (د1) ∥ (د2). و (د3) عموديّ على (د2)، والعموديّ على أحد متوازيين عموديّ على الآخر: (د3) ⊥ (د1). » |
| `04-defi` Q4 | propriété § 🚆 mot pour mot (mêmes lettres) ; paire 0,65 avec `02` Q5 | « (د1) ∥ (د2) و (د3) ⊥ (د1)، ثمّ رسمنا (د4) ⊥ (د3). ما وضعيّة (د4) بالنسبة إلى (د2)؟ » · a `(د4) ∥ (د2)` (clé) · b `(د4) ⊥ (د2)` (`regle-perpendiculaire-parallele-inversee`) · c `(د4) ⊥ (د1)` (même étiquette) · d `لا نستطيع الحكم` muette · exp. « (د3) ⊥ (د1) و (د1) ∥ (د2)، فـ (د3) ⊥ (د2) أيضًا: العموديّ على أحد متوازيين عموديّ على الآخر. ثمّ (د4) و (د2) كلاهما عموديّ على (د3)، فهما متوازيان: (د4) ∥ (د2). » |
| `04-defi` Q6 | `verifie` § ⊥ (« كم زاوية قائمة عند ب » → 4) | type `numeric` : « (د1) ⊥ (د2)، و (د3) يوازي (د1) ويقطع (د2) في نقطة ثانية. كم زاويةً قائمةً تتكوّن في المجموع عند نقطتي التقاطع؟ » · `value` 8 · exp. « (د3) ∥ (د1) و (د2) ⊥ (د1)، فـ (د2) ⊥ (د3): العموديّ على أحد متوازيين عموديّ على الآخر. وعند كلّ نقطة تقاطع بين مستقيمين متعامدين أربع زوايا قائمة، فالمجموع 4 + 4 = 8. » |
| `04-defi` Q7 | exemple § 🧭 étape 4 (ملاك, 45 : 2 = 22,5) | type `numeric` : « مستقيمان متعامدان يلتقيان في م، ورسمنا [مك) منصّف إحدى الزوايا القائمة الأربع. ما قيس الزاوية المنفرجة التي يصنعها [مك) مع أحد المستقيمين، بالدرجة؟ » · `value` 135 · exp. « المنصّف يقسم الزاوية القائمة إلى 45° و45°. الزاوية المنفرجة تبدأ من [مك)، تعبر نصف القائمة المنصَّفة (45°) ثمّ قائمة كاملة مجاورة لها (90°): 45 + 90 = 135°. » (avec une droite, [مك) fait 45° ou 135° : une seule obtuse.) |
| `04-defi` Q8 | `verifie` § 🏛️ (médiatrice de la longueur → 5 cm) | type `numeric` : « قاعة مستطيلة أبجد بُعداها 20 م و 12 م، رُسم مخطّطها بمقياس 1 سم لكلّ 2 م. مركز الحوض هو نقطة تقاطع الموسّط العمودي للطول [أب] والموسّط العمودي للعرض [بج]. كم سنتيمترًا يبعد هذا المركز عن الطول [أب] على المخطّط؟ » · `value` 3 · exp. « العرض على المخطّط 12 ÷ 2 = 6 سم. الموسّط العمودي للعرض [بج] يمرّ بمنتصفه، على بُعد 6 ÷ 2 = 3 سم من ب. وهو عموديّ على (بج) مثل (أب)، فهو يوازي (أب)، والبُعد بين متوازيين ثابت: المركز يبعد 3 سم عن الطول [أب]. » |
| `05-entrainement` Q2 | piège § 📏 mot pour mot (droite par le milieu à 60°) | « [أب] قطعة طولها 6 سم. رسم تلميذ مستقيمًا عموديًّا عليها في نقطة تبعد 2 سم عن أ. هل هو الموسّط العمودي لـ [أب]؟ » · a `لا، لأنّه لا يمرّ بمنتصفها` (clé) · b `نعم، لأنّه يعامدها وهذا يكفيه` muette · c `نعم، لأنّه يقطعها في نقطة واحدة` muette · d `لا، لأنّ الزاوية بينهما ليست قائمة` muette · exp. « منتصف [أب] يبعد 6 ÷ 2 = 3 سم عن أ، والمستقيم يقطعها على بُعد 2 سم من أ. هو عموديّ عليها لكنّه لا يمرّ بمنتصفها، والموسّط العمودي يطلب الشرطين معًا. » |
| `05-entrainement` Q3 | doublon de `01` Q3 (« لا يتقاطعان مهما امتدّا ») | « (د1) ∥ (د2)، والمستقيم (د3) يقطع (د1). ماذا نستنتج عن (د3) و (د2)؟ » · a `(د3) ∥ (د2)` muette · b `(د3) يقطع (د2) أيضًا` (clé) · c `(د3) ⊥ (د2) دائمًا` muette · d `(د3) ⊥ (د1) دائمًا` muette · exp. « (د2) له اتّجاه (د1) نفسه، فمن قطع أحدهما قطع الآخر: (د3) يقطع (د2). ولا نعرف أنّ الزاوية قائمة، لأنّ (د3) لم يُعطَ عموديًّا على (د1). » |

Figure de `02-boss` Q1. L'angle droit est exact : les directions 30° et 120° sont perpendiculaires. Rendu vérifié :

```html
<svg viewBox="0 0 100 100"><line x1="15.4" y1="75" x2="84.6" y2="35" stroke="currentColor" stroke-width="2.5"/><line x1="30" y1="20.4" x2="70" y2="89.6" stroke="currentColor" stroke-width="2.5"/><polygon points="50,55 56.93,51 52.93,44.07 46,48.07" fill="none" stroke="#ef4444" stroke-width="1.5"/></svg>
```

Figure de `04-defi` Q1. Le triangle (20,78), (80,78), (50,26) a trois côtés de 60,0 et son sommet est sur la médiatrice
x = 50. Rendu vérifié :

```html
<svg viewBox="0 0 100 100"><line x1="12" y1="78" x2="88" y2="78" stroke="currentColor" stroke-width="2.5"/><line x1="50" y1="8" x2="50" y2="96" stroke="#0f6e56" stroke-width="2" stroke-dasharray="4 3"/><polygon points="20,78 80,78 50,26" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><polyline points="50,71 57,71 57,78" fill="none" stroke="#ef4444" stroke-width="1.5"/><text x="17" y="93" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">أ</text><text x="83" y="93" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">ب</text><text x="40" y="22" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">ن</text><text x="62" y="92" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56">م</text></svg>
```

Champ `manuel` de `04-defi` : `items` devient `["L4 ex. 2"]`. L4 ex. 1 et ex. 5 sont devenus des variantes ; Q8 garde
les données de L4 ex. 2.

**M16-2 — `quiz` Q1 : deux options synonymes.** « إذا لم يتقاطعا أبدًا » et « إذا كانا متوازيين » disent la même chose.
Remplacer l'option d par `إذا تقاطعا مكوّنَين زاوية حادّة` (muette). L'effet secondaire est utile : la clé n'est plus
la plus longue.

### Mineurs

- **m16-1 — étiquette qui ne nomme pas l'erreur exécutée.** L'option « متقاطعان بزاوية حادّة » porte
  `intersection-prise-pour-perpendicularite` alors que l'erreur faite est l'inverse : ne pas voir l'angle droit codé.
  Cas : `quiz` Q3 c, `03` Q1 d, `03` Q5 a, `05` Q5 b. Les rendre **muettes**.
- **m16-2 — distracteurs de remplissage.** « الميزان » dans `01` Q6 c et `05` Q4 b, « لا يمكن قياسه / معدوم » dans `03`
  Q4. Remplacer `01` Q6 c par `المنقلة والفرجار`, `05` Q4 b par `الكوس وحده`, et `03` Q4 d par
  `يتغيّر من جهة إلى أخرى`. Tous muets.
- **m16-3** `03` Q2 (deux parallèles à 3,5 cm, reprise de rév. 6 ex. 3ج) : le fait « une de chaque côté » n'est écrit
  nulle part. La question reste résoluble par raisonnement. Ajouter au cas limite de la propriété § ∥ : « ولمستقيمٍ
  (د) موازيان اثنان على بُعدٍ معلوم منه، واحدٌ من كلّ جهة. »
- **m16-4** `01` Q7 (منصّف القائمة = 45°) est la valeur canonique de la règle : on ne peut pas l'éviter, elle reste.
  Seule sa copie au ch. 17 (`02-boss` Q6) est retirée (M17-1).
- **m16-5** `04-defi` Q5 (« quelle marque indique ∥ ») est une récitation de niveau 1 dans un défi. Calibration à
  revoir si le défi est retouché.
- **m16-6** Le cours § ⊥ (propriété) utilise « angle plat = 180° » avant le ch. 17. C'est un acquis de 5ᵉ, tolérable.

---

## Ch. 17 — `17-angles` (42 questions re-résolues)

**Clés : 42/42 justes.** Le cours (inchangé contre `origin/main`) a été re-résolu : 50 et pas 130 ; 120 ; 110 > 70 ;
89/91/180 ; 50 + 80 = 130 ; 35 + 55 = 90 ; 180 − 65 = 115 ; 90 − 30 = 60 ; 80 : 2 = 40 et 50 + 40 = 90 ; 120 : 2 = 60 ;
la construction de 60° ; le tableau 30/15/45/120/75/150 ; 150 gr = 90 + 45 = 135° ; 100 gr : 2 = 50 gr = 45°. Tout est
juste. Les 10 figures sont vraies : en SVG#5, les rayons sont à 0°, 50° et 130°.
Patron : 9 sections, chacune complète.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ ;
- exhaustivité ✓ : grade, bissectrice, constructions au compas, angles adjacents ;
- expérience ✓ ;
- illustration ✓.

Tableaux à 360 px : la cellule de notation pure (`60 ÷ 2`) est protégée par `unicode-bidi: plaintext` ✓.

### Majeurs

**M17-1 — 19 questions redonnent le cours ou sont des doublons.**

Corrections côté cours, d'abord. Elles rendent leur fidélité aux reprises `02-boss` Q8 (L7 ex. 8) et `04-defi` Q8
(L7 ex. 7), qui sont gardées :

- **tableau de la propriété § 🔵** : remplacer la ligne `| 75°   | 60 + 15      |` par `| 105°  | 90 + 15      |`, et la
  ligne `| 150°  | 90 + 60      |` par `| 135°  | 90 + 45      |` ;
- **`verifie` § 🔵** : la question devient « صف مراحل بناء زاوية قيسها 165° بالمسطرة والفرجار. » et la réponse « نمدّد
  [أب) من جهة الرأس أ فنحصل على زاوية مستقيمة قيسها 180°. نبني بالفرجار 60° وننصّفها مرّتين: 60 ÷ 2 = 30 ثمّ 30 ÷ 2 = 15،
  فنحصل على زاوية 15° ملاصقة للامتداد. الزاويتان متجاورتان على مستقيم، فالزاوية المتبقّية بين [أب) والضلع الجديد
  قيسها 180 − 15 = 165°. » C'est le jumeau du cas limite « 120 = 180 − 60 » ;
- **`resume.md`**, puce « البناء بالمسطرة والفرجار » : remplacer `75 = 60 + 15، 150 = 90 + 60` par
  `105 = 90 + 15، 135 = 90 + 45`.

Remplacements de questions :

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q4 | exemple § ✂️ (80 : 2 = 40) | « منصّف زاوية قيسها 140° يقسمها إلى زاويتين، قيس كلّ منهما: » · a `280°` (`math.num.operation-inverse-appliquee`) · b `40°` muette · c `70°` (clé) · d `140°` muette · exp. « المنصّف يقسم الزاوية نصفين متقايسين: 140° ÷ 2 = 70°. من كتب 280° ضرب في 2 بدل القسمة. » |
| `quiz` Q5 | exemple § ➕ (50 + 80 = 130) | « زاويتان متجاورتان قيساهما 70° و 45°. ما قيس الزاوية التي تضمّهما معًا؟ » · a `25°` (`operation-inverse-appliquee`) · b `90°` muette · c `115°` (clé) · d `180°` muette · exp. « الزاوية الكلّيّة تتكوّن من الزاويتين معًا، فقيسها مجموع القيسين: 70° + 45° = 115°. أمّا الطرح 70 − 45 = 25 فيعطي الفرق بين الزاويتين لا الزاوية التي تضمّهما. » |
| `01-pratique` Q3 | même figure et mêmes options que `quiz` Q3 (1,00) | supprimer la figure : « ما نوعُ زاويةٍ قيسُها 95°؟ » · a `حادّة` (`math.geo.type-d-angle-confondu`) · b `قائمة` (idem) · c `منفرجة` (clé) · d `مستقيمة` (idem) · exp. « 95 > 90 و 95 < 180، فالزاوية منفرجة؛ قربُها من 90 لا يجعلها قائمة: القائمة 90° بالضبط. » |
| `01-pratique` Q8 | piège § 🧭 (120 lu 60, point ج) | même question avec **140** : « نبني بالمنقلة زاوية قيسها 140°، فنعلّم النقطة ج أمام العدد 140. على أيّ سلّم نقرأ هذا العدد؟ » · options inchangées · exp. « نقرأ على السلّم الذي يبدأ من صفرٍ موضوعٍ على الضلع الأوّل، كما في القياس. فلو اخترنا السلّم الآخر لخرجت زاوية قيسها 40° بدل 140°، أي زاوية حادّة بدل المنفرجة. » |
| `02-boss` Q1 | copie de `quiz` Q3 (1,00) | type `numeric`, difficulté 2 : « من بين الأقيسة 30° و90° و89° و120°، كم قيسًا لزاويةٍ حادّة؟ » · `value` 2 · exp. « الحادّة أصغر من 90°: 30° و 89° فقط. أمّا 90° فقائمة و120° منفرجة. العدد 2. » |
| `02-boss` Q4 | `verifie` § ⚖️ (70° longs / 110° courts) | « زاويةٌ قيسُها 95° ضلعاها قصيران، وزاويةٌ قائمة ضلعاها طويلان. أيّهما أكبر؟ » · a `زاوية 95°` (clé) · b `الزاوية القائمة` muette · c `متساويتان` muette · d `لا يمكن المقارنة` muette · exp. « نقارن القيسين وحدهما: 95 > 90، فالزاوية التي قيسها 95° أكبر. طول الضلعين لا يدخل في القيس. » |
| `02-boss` Q5 | exemple § ✂️ (50/80 → قائمة), aussi L7 ex. 1 | « في الشكل: قيس الزاوية [أج، أد] = 40°، وقيس الزاوية [أد، أب] = 120°. رسمنا [أس) منصّف الزاوية [أد، أب]. ما نوع الزاوية [أج، أس]؟ » + figure ci-dessous · a `قائمة` muette · b `منفرجة` (clé) · c `مستقيمة` (`type-d-angle-confondu`) · d `حادّة` muette · exp. « المنصّف يقسم الزاوية [أد، أب] نصفين: 120° ÷ 2 = 60°. الزاويتان [أج، أد] و [أد، أس] متجاورتان، فقيس [أج، أس] = 40° + 60° = 100°. وبما أنّ 100 أكبر من 90 وأصغر من 180، فهي زاوية منفرجة. » |
| `02-boss` Q6 | piège § ✂️ (نصف القائمة) ; copie de ch. 16 `01` Q7 | « قُسّمت زاوية مستقيمة إلى ثلاث زوايا متجاورة متقايسة. كم قيسُ كلٍّ منها؟ » · a `60°` (clé) · b `90°` muette · c `120°` muette · d `30°` (`math.geo.valeur-angle-de-reference-confondue`) · exp. « الزاوية المستقيمة 180°، والزوايا الثلاث المتجاورة تتقاسمها بالتساوي: 180 ÷ 3 = 60°. من وجد 30° قسم 90 على 3، أي أخذ القائمة مكان المستقيمة. » |
| `02-boss` Q7 | ordre des étapes de l'exemple § 🧭 (mêmes lettres, 120°) | « رتّب خطوات بناء زاوية [كل، كم] قيسها 35° بالمنقلة. » · a `نرسم نصف المستقيم [كل) بالمسطرة` · b `نضع مركز المنقلة على ك وصفرها على [كل)` · c `نعلّم النقطة م أمام 35 على السلّم الذي صفره على [كل)` · d `نرفع المنقلة ونرسم [كم) بالمسطرة` · ordre a, b, c, d · exp. « نرسم أوّلًا الضلع الأوّل لأنّه يحمل الصفر، ثمّ نضع المنقلة عليه، فنعلّم النقطة أمام العدد المطلوب، وبعد رفع المنقلة نصل الرأس بالنقطة. نتحقّق في الأخير أنّ الزاوية حادّة، لأنّ 35 < 90. » |
| `03-revision` Q1 | doublon de `quiz` Q2 (قيس القائمة) | « كم قيسُ الزاوية المستقيمة بالغراد؟ » · a `200 غراد` (clé) · b `180 غراد` (`valeur-angle-de-reference-confondue`) · c `100 غراد` (idem) · d `360 غراد` (idem) · exp. « الغراد وحدة ثانية: القائمة 100 غراد، والمستقيمة قائمتان، أي 200 غراد (وتساوي 180°). العدد 180 هو قيسها بالدرجة لا بالغراد. » |
| `03-revision` Q5 | exemple § 🔵 (palette, 60 : 2 = 30), aussi L7 ex. 2 | type `numeric` : « لوحة الدهّان مقسّمة إلى 12 قطعة متقايسة، زاوية كلّ قطعة 30°. يريد 24 قطعة، فينصّف كلّ قطعة. ما قيس زاوية القطعة الجديدة بالدرجة؟ » · `value` 15 · exp. « التنصيف يقسم كلّ زاوية نصفين متقايسين: 30 ÷ 2 = 15، فزاوية القطعة الجديدة 15°. » |
| `03-revision` Q6 | figure SVG#6 et cas limite § ➕ (180 − 120 = 60) | « زاويتان متجاورتان تكوّنان زاوية مستقيمة (180°). إذا كانت إحداهما 145°، فالأخرى: » + figure ci-dessous · a `35°` (clé) · b `55°` (`valeur-angle-de-reference-confondue`) · c `215°` (idem) · d `45°` muette · exp. « مجموعهما 180°: نعرف الكلّ ونبحث عن جزء، فالأخرى = 180° − 145° = 35°. من وجد 55° طرح من 90 بدل 180 (145 − 90)، ومن وجد 215° طرح 145 من 360. » |
| `04-defi` Q2 | `verifie` du ch. 16 et piège § ✂️ (نصف المستقيمة = 90) ; doublon de ch. 16 `quiz` Q4 | « زاوية منفرجة رسمنا منصّفها. ما نوع كلّ من الزاويتين الناتجتين؟ » · a `حادّة` (clé) · b `قائمة` muette · c `منفرجة` muette · d `حادّة أو منفرجة حسب قيسها` muette · exp. « المنفرجة أكبر من 90° وأصغر من 180°، فنصفها أكبر من 90 ÷ 2 = 45° وأصغر من 180 ÷ 2 = 90°. كلّ زاوية ناتجة أصغر من 90°: حادّة. مثلًا منصّف 170° يعطي 85°. » |
| `04-defi` Q3 | `verifie` § ➕ (65 → 115) | « زاويتان متتامّتان (مجموعهما 90°)، إحداهما 35°. ما قيس الأخرى؟ » · a `145°` (`valeur-angle-de-reference-confondue`) · b `55°` (clé) · c `65°` muette · d `325°` (idem a) · exp. « المتتامّتان مجموعهما 90°: الأخرى = 90° − 35° = 55°. من وجد 145° طرح من 180 كأنّهما متكاملتان، ومن وجد 325° طرح من 360. » |
| `04-defi` Q4 | options = cas limite de la propriété § 🗂️ (« 30° و90° و150° ») | garder énoncé et figure (angle tracé ≈ 30°) ; options : a `منفرجة، 160°` (`type-d-angle-confondu`) · b `حادّة، 30°` (clé) · c `قائمة، 90°` (idem a) · d `حادّة، 80°` muette · exp. « الفتحة أضيق بوضوح من نصف القائمة (45°)، فالزاوية حادّة وقيسها قريب من 30° لا من 80°: زاوية 80° تكاد تكون قائمة. » |
| `04-defi` Q6 | exemple § 🌐 (150 gr = 135°), aussi L7 ex. 6 | type `numeric` : « زاويتان متجاورتان: الأولى قيسها 100 غراد والثانية قيسها 50°. ما قيس الزاوية التي تضمّهما، بالدرجة؟ » · `value` 140 · exp. « 100 غراد = 90°. نجمع القيسين بالوحدة نفسها: 90° + 50° = 140°. من جمع 100 + 50 = 150 خلط الغراد بالدرجة. » |
| `04-defi` Q7 | appariement = le tableau § 🔵 ligne pour ligne | gauche : l1 `22,5°` · l2 `90°` · l3 `45°` · l4 `135°` ; droite : r1 `45° ÷ 2` · r2 `180° ÷ 2` · r3 `15° + 30°` · r4 `180° − 45°` ; paires l1–r1, l2–r2, l3–r3, l4–r4. Chaque côté droit a une seule valeur : 22,5 / 90 / 45 / 135 · exp. « 45° ÷ 2 = 22,5°: منصّف نصف القائمة. 180° ÷ 2 = 90°: منصّف الزاوية المستقيمة قائمة. 15° + 30° = 45°: زاويتان متجاورتان نجمع قيسيهما، طريقة ثانية لبناء 45°. 180° − 45° = 135°: المجاورة لزاوية 45° على مستقيم، لأنّ المتجاورتين على مستقيم مجموعهما 180°. » |
| `05-entrainement` Q1 | copie de `quiz` Q3 (1,00) | supprimer la figure : « أيُّ قيسٍ من الآتي لزاويةٍ حادّة؟ » · a `95°` (`type-d-angle-confondu`) · b `85°` (clé) · c `90°` (idem) · d `180°` (idem) · exp. « الحادّة أصغر من 90°: من بين الأقيسة لا يحقّق ذلك إلّا 85°. 90° قائمة، و95° منفرجة، و180° مستقيمة. » |
| `05-entrainement` Q5 | piège § ➕ mot pour mot (35 + 55, erreur 20) | « زاويتان متجاورتان قيسُهما 65° و 25°. ما قيسُ الزاوية الكلّية الناتجة؟ » · a `90°` (clé) · b `40°` (`operation-inverse-appliquee`) · c `80°` muette · d `100°` muette · exp. « نجمع قيسَي الزاويتين المتجاورتين: 65° + 25° = 90°، زاوية قائمة. الطرح 65 − 25 = 40 يعطي الفرق لا الزاوية الكلّية. » |

Figure de `02-boss` Q5. Rayons à 0°, 40° (د, longueur 52) et 160° (ب, longueur 40) ; arcs de 0° à 40° (r = 16) et de 40° à
160° (r = 22). Rendu vérifié :

```html
<svg viewBox="0 0 100 100"><line x1="50" y1="82" x2="92" y2="82" stroke="currentColor" stroke-width="2.5"/><line x1="50" y1="82" x2="89.8" y2="48.6" stroke="currentColor" stroke-width="2.5"/><line x1="50" y1="82" x2="12.4" y2="68.3" stroke="currentColor" stroke-width="2.5"/><path d="M66 82 A16 16 0 0 0 62.26 71.72" fill="none" stroke="#ef4444" stroke-width="1.5"/><path d="M66.85 67.86 A22 22 0 0 0 29.33 74.48" fill="none" stroke="#ef4444" stroke-width="1.5"/><text x="50" y="96" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">أ</text><text x="97" y="86" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">ج</text><text x="94" y="45" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">د</text><text x="7" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="currentColor">ب</text></svg>
```

Figure de `03-revision` Q6. Rayon à 145° ; arc rouge de 0° à 145° (r = 34) ; arc noir de 145° à 180° (r = 22). Rendu
vérifié :

```html
<svg viewBox="0 0 220 150">
<title>زاويتان متجاورتان على مستقيم</title>
<line x1="22" y1="112" x2="198" y2="112" stroke="#0f172a" stroke-width="2.4"/><line x1="110" y1="112" x2="46.1" y2="67.3" stroke="#0f172a" stroke-width="2.4"/><circle cx="110" cy="112" r="2.4" fill="#0f172a"/><path d="M 144 112 A 34 34 0 0 0 82.15 92.5" fill="none" stroke="#ef4444" stroke-width="1.8"/><path d="M 91.98 99.38 A 22 22 0 0 0 88 112" fill="none" stroke="#0f172a" stroke-width="1.6"/><text x="150" y="72" text-anchor="middle" fill="#ef4444" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">145°</text><text x="62" y="104" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">؟</text>
</svg>
```

Champs `manuel` :
- `02-boss` : `items` devient `["L7 ex. 8"]` ;
- `03-revision` : **supprimer le champ** (son seul item, L7 ex. 2, est devenu une variante) ;
- `04-defi` : `items` devient `["L4 ex. 4", "L7 ex. 7"]`.

**M17-2 — `quiz` Q1 : la clé se repère à sa forme.** La clé est la seule option développée, et les distracteurs sont
du remplissage (« من دائرة », « من نقطةٍ واحدة »). Options : a `من نصفَي مستقيم لهما المبدأ نفسه` (clé) · b
`من نصفَي مستقيم متوازيين` · c `من قطعتين لا تلتقيان` · d `من مستقيم ونقطة خارجه`, toutes muettes. Explication
inchangée.

### Mineurs

- **m17-1 — étiquette `valeur-angle-de-reference-confondue` sur 45°.** 45° est une moitié, pas une confusion de mesures
  de référence. Rendre muettes `quiz` Q2 c et `01` Q4 c. À l'inverse, `01` Q7 c (`200 غراد` pour l'angle droit) exécute
  bien cette erreur : lui ajouter l'étiquette.
- **m17-2 — calibration.** `02-boss` Q2 (outil = منقلة, d2 dans un boss), `05` Q6 (« 120° est-elle plus grande que
  90° », d3) et `05` Q4 (récitation de la propriété « 60° au compas ») sont des items de niveau 1. À relever si
  l'exercice est retouché.
- **m17-3** `03` Q7 (45 + 60 = 105) a le même résultat que la nouvelle ligne du tableau (90 + 15), mais par une autre
  décomposition. Aucune fuite.

---

## Ch. 18 — `18-triangles` (42 questions re-résolues)

**Clés : 42/42 conformes, mais `quiz` Q2 a deux réponses défendables** (C18-1). Cours re-résolu :
- classements 6-6-6 / 6-6-5 / 6-4-3 ; 7-7-10 ; 8-5-8 et 2-4-5 ; 90-60-30, 120-40-20, 45-60-75 ; 50-35-95 ;
- 6-8-10 rectangle et scalène ; demi-carré : 6/√2 ≈ 4,2 ;
- périmètres 18, 18, 6, 6, 6, 5, 15 ;
- existence : 6-4-3 oui, 2-2-6 non, 4-2-6 aligné, 3-4-8 non, 5-4-3 oui ;
- constructions 5-4-75°, 6-3-120°, 8 avec 45°/60° (3ᵉ angle **mesuré**), 7 avec 90°/45°.

Tout est juste. Les 11 figures sont vraies, et `02-boss` Q7 a été vérifiée par calcul : ع est exactement le symétrique de
أ par rapport à (ب‌ج) (بع = بأ = 60,0) et l'équerre est au pied. M3 est tenu.
Reprises : L8 ex. 4–11 (ص 24–26, relue à l'image), rév. 7 ex. 2 et 5, T3 sit. 3 (`03`) — données fidèles.

Axes du cours :
- clarté ✓ ;
- compréhension ✓ (9 sections au patron) ;
- exhaustivité ✓ : existence, périmètre direct et inverse, trois constructions ;
- expérience ✓ ;
- illustration ✓.

### Critique

**C18-1 — `quiz` Q2 (« 5 سم، 5 سم، 5 سم. ما نوعُه؟ ») : deux réponses défendables.** Le cours écrit lui-même « إذا تساوت
الأضلاع الثلاثة فالمثلّث متساوي الساقين أيضًا » et, dans le piège, « ليس خطأً ». L'option « متساوي الساقين » est donc
vraie et pourtant comptée fausse. La question redonne en plus les nombres de deux pièges du cours. Remplacement :
« مثلّثٌ أطوالُ أضلاعه 4 سم، 4 سم، 4 سم. ما اسمُه الأدقّ حسب أضلاعه؟ » · a `متساوي الساقين`
(`math.geo.description-la-plus-precise-manquee`) · b `متساوي الأضلاع` (clé) · c `مختلف الأضلاع`
(`classement-triangle-par-cotes-errone`) · d `قائم الزاوية` (`classements-triangle-melanges`) · exp. « أضلاعه الثلاثة
متساوية (4 = 4 = 4)، فهو متساوي الأضلاع. هو متساوي الساقين أيضًا، لكنّ الاسم الأدقّ هو متساوي الأضلاع. »

### Majeurs

**M18-1 — 19 questions redonnent le cours, ou en sont des doublons, ou forment des paires proches.**

Corrections côté cours. Elles retirent la redite de `04-defi` Q1, Q3, Q5 (reprise L8 ex. 5, gardée) et de `05` Q5 :

- **propriété § 🧮**, remplacer le bloc depuis `القاعدة؛ فمثلّث ساقاه 7 سم` jusqu'à `7 + 7 + 6 = 20 ✓.` par :
  « القاعدة؛ فمثلّث ساقاه 8 سم وقاعدته 5 سم محيطه 8 + 8 + 5 = 21 سم. حالة حدّيّة، العكس في متساوي الساقين:
  محيطه 22 سم وقاعدته 8 سم، فنطرح القاعدة ثمّ نقسم على 2: » ; puis la ligne `$$ (22 − 8) : 2 = 7 $$` ; puis « فكلّ ساق
  7 سم، ونتحقّق: 7 + 7 + 8 = 22 ✓. وإذا أعطينا الساق بدل القاعدة، فنطرح الساقين من المحيط: محيطه 25 سم وساقه 9 سم،
  فالقاعدة 25 − 9 − 9 = 7 سم، ونتحقّق: 9 + 9 + 7 = 25 ✓. »
  Contrôle : 22 − 8 = 14 et 14 : 2 = 7 ; 25 − 18 = 7 ; 9 + 9 > 7 ✓.
- **`verifie` § 🧮**, troisième question : `ضلعه 5 سم` devient `ضلعه 4 سم`. Dans la réponse, remplacer
  `ومحيط الثالث 3 × 5 = 15 سم، لأنّ له ثلاثة أضلاع متساوية؛ من كتب 10 سم نسي ضلعًا، ومن كتب 25 سم ضرب 5 في 5.` par
  `ومحيط الثالث 3 × 4 = 12 سم، لأنّ له ثلاثة أضلاع متساوية؛ من كتب 8 سم نسي ضلعًا، ومن كتب 16 سم ضرب في 4 كأنّه مربّع.`
- **`resume.md`**, puce « المحيط » : `(17 − 5) : 2 = 6 سم لكلّ ساق` devient `(22 − 8) : 2 = 7 سم لكلّ ساق`, et
  `(20 − 7 − 7 = 6 سم)` devient `(25 − 9 − 9 = 7 سم)`.

Remplacements de questions :

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q3 | exemple et piège § 📐 (90-60-30) | « مثلّث زواياه 40° و90° و50°. ما نوعه حسب زواياه؟ » · options et étiquettes inchangées · exp. « أكبر زاوية 90°، وهي قائمة، فهو قائم الزاوية. وجود زاويتين حادّتين لا يجعله حادّ الزوايا: الذي يقرّر هو أكبر زاوية. أمّا متساوي الأضلاع فتصنيف حسب الأضلاع لا حسب الزوايا. » |
| `quiz` Q5 | exemple § 🧭 (6-4-3) | `6 سم و4 سم و3 سم` devient `7 سم و5 سم و4 سم` dans l'énoncé ; options et explication inchangées |
| `01-pratique` Q2 | même calcul que `04-defi` Q2 (3 + 4 + 5 = 12) | « ما محيط مثلّث أضلاعه 4 سم و5 سم و6 سم؟ » · a `9 سم` muette · b `15 سم` (clé) · c `20 سم` muette · d `120 سم` (`operation-inverse-appliquee`) · exp. « المحيط مجموع الأضلاع الثلاثة: 4 + 5 + 6 = 15 سم. من كتب 9 سم نسي ضلعًا، ومن كتب 120 سم ضرب بدل أن يجمع. » |
| `01-pratique` Q7 | exemple § 📐 (ق‌ع‌ن 5-4-75°), aussi L8 ex. 7 | « نريد بناء مثلّث ر‌م‌ل فيه م‌ر = 6 سم و م‌ل = 5 سم وقيس الزاوية ر‌م‌ل = 70°. عند أيّ رأس نرسم الزاوية 70°؟ » · figure : garder les coordonnées, changer seulement les textes `ع`→`م`, `ق`→`ر`, `ن`→`ل`, `5`→`6`, `4`→`5` · a `عند الرأس ل` · b `عند منتصف [ر‌ل]` · c `عند الرأس ر` · d `عند الرأس م` (clé), toutes muettes · exp. « الزاوية المعلومة هي ر‌م‌ل، ورأسها حرفها الأوسط م، وهو الرأس المشترك بين الضلعين المعلومين [م‌ر] و[م‌ل]. لو رسمنا 70° عند ر أو عند ل لحصلنا على مثلّث آخر. » |
| `01-pratique` Q8 | exemple § 🧮 (هالة, 18 → 6), aussi L8 ex. 4 ; « أراد هالة » est fautif (accord) | « بنى سامي مثلّثًا متساوي الأضلاع محيطه 21 سم. ما طول ضلعه بالسنتيمتر؟ » · `value` 7 · exp. « الأضلاع الثلاثة متساوية، فالضلع = المحيط ÷ 3 = 21 ÷ 3 = 7 سم؛ ونتحقّق: 7 + 7 + 7 = 21. » |
| `01-pratique` Q9 | exemple § 🎯 (ك‌ن‌د 8-45-60), aussi L8 ex. 6 | « مثلّث ط‌ر‌م فيه ر‌م = 7 سم، وقيس الزاوية ط‌ر‌م = 30° وقيس الزاوية ط‌م‌ر = 70°. عند أيّ رأسين نرسم الزاويتين بالمنقلة بعد رسم [ر‌م]؟ » · a `عند الرأسين ر و م` (clé) · b `عند الرأسين ط و م` · c `عند الرأس ط وحده` · d `عند الرأسين ط و ر` · exp. « الضلع المعلوم هو [ر‌م]، والزاويتان المعلومتان رأساهما ر وَ م: الحرف الأوسط في ط‌ر‌م هو ر، وفي ط‌م‌ر هو م. فنرسم 30° عند ر و70° عند م في الجهة نفسها، ويلتقي الضلعان الجديدان في الرأس ط. » |
| `02-boss` Q2 | piège § 📏 (7-7-10) | « في المثلّث أ‌ب‌ج: أ‌ب = 7 سم و ب‌ج = 10 سم، ومحيطه 24 سم. ما نوعه حسب أضلاعه؟ » · a `متساوي الساقين` (clé) · b `متساوي الأضلاع` (`classement-triangle-par-cotes-errone`) · c `مختلف الأضلاع` (idem) · d `قائم الزاوية` (`classements-triangle-melanges`) · exp. « الضلع الثالث أ‌ج = 24 − 7 − 10 = 7 سم. الأطوال 7 و10 و7: ضلعان فقط متساويان (أ‌ب = أ‌ج = 7 سم)، فهو متساوي الساقين، قمّته الرئيسيّة أ وقاعدته [ب‌ج] = 10 سم. » |
| `02-boss` Q5 | figure SVG#6 et définition § 🍰 (les 8 parts), aussi L8 ex. 9 | « قطعت السيّدة نور كعكة مستطيلة (ليست مربّعة) بخطّ مستقيم من ركن إلى الركن المقابل، فصارت قطعتين مثلّثتين متقايستين. ما نوع كلّ قطعة؟ » + figure ci-dessous · a `قائم الزاوية ومختلف الأضلاع` (clé) · b `قائم الزاوية ومتساوي الساقين` (`classement-triangle-par-cotes-errone`) · c `حادّ الزوايا ومختلف الأضلاع` (`classement-triangle-par-angles-errone`) · d `منفرج الزاوية ومختلف الأضلاع` (idem c) · exp. « زاوية المستطيل قائمة، فالقطعة قائمة الزاوية عند ركنه. ضلعاها القائمان طول المستطيل وعرضه، وهما غير متساويين، والضلع الثالث، خطّ القطع، أطول منهما: لا زوج متساوٍ، فهي مختلفة الأضلاع. في المربّع وحده يتساوى الضلعان القائمان. » |
| `02-boss` Q6 | cas limite de la propriété § 📐 ; paire 0,81 avec `04` Q4 | « مثلّث قيس إحدى زواياه 100°. ما نوعه حسب زواياه، وما نوع زاويتيه الأخريين؟ » · a `منفرج الزاوية، وزاويتاه الأخريان حادّتان` (clé) · b `منفرج الزاوية، وإحدى زاويتيه الأخريين قائمة` muette · c `حادّ الزوايا، لأنّ فيه زاويتين حادّتين` (`classement-triangle-par-angles-errone`) · d `منفرج الزاوية، وزاويتاه الأخريان منفرجتان` muette · exp. « أكبر زاوية 100°، وهي منفرجة، فالمثلّث منفرج الزاوية. وفي المثلّث زاوية واحدة على الأكثر ليست حادّة، فالزاويتان الأخريان حادّتان: لو كانت إحداهما قائمة أو منفرجة لمال ضلعاها بعيدًا ولم يلتقيا. » |
| `02-boss` Q8 | ordre des étapes de l'exemple § 🍰 (ق‌ن 6, 45°), aussi L8 ex. 8 | « رتّب مراحل بناء مثلّث م‌ن‌ر فيه م‌ن = 7 سم و م‌ر = 4 سم وقيس الزاوية ن‌م‌ر = 50°. » · a `نرسم [م‌ن] = 7 سم بالمسطرة` · b `نضع مركز المنقلة على م وصفرها على [م‌ن] ونعلّم 50` · c `نرسم نصف مستقيم من م يمرّ بالعلامة ونقيس عليه م‌ر = 4 سم` · d `نصل ر بـ ن بالمسطرة` · ordre a, b, c, d (ordre strict : chaque étape a besoin de la précédente) · exp. « نبدأ بضلع معلوم، ثمّ نرسم الزاوية المعلومة عند الرأس المشترك م، فنقيس عليها الضلع الثاني، وفي الأخير نصل طرفي الضلعين: الضلع الثالث لا يحتاج إلى قياس. » |
| `03-revision` Q4 | `verifie` § 📏 (2-4-5) ; 5ᵉ copie du gabarit | « أيّ مثلّث من الآتي مختلف الأضلاع؟ » · a `3 سم و3 سم و4 سم` (`classement-triangle-par-cotes-errone`) · b `6 سم و6 سم و6 سم` (idem) · c `4 سم و6 سم و9 سم` (clé) · d `5 سم و7 سم و5 سم` (idem) · exp. « نقارن الأزواج في كلّ مثلّث: 3 = 3، و6 = 6 = 6، و5 = 5؛ أمّا 4 و6 و9 فلا زوج متساوٍ فيها (4 ≠ 6، 4 ≠ 9، 6 ≠ 9)، فهو مختلف الأضلاع. » (4 + 6 = 10 > 9, triangle constructible.) |
| `04-defi` Q4 | cas limite § 📐 ; paire 0,81 | type `numeric` : « مثلّث متساوي الساقين ساقاه 8 سم، وطول قاعدته عدد صحيح من السنتيمترات. ما أكبر طول ممكن لقاعدته؟ » · `value` 15 · exp. « القاعدة هي أطول الأضلاع هنا، ويجب أن تكون أصغر من مجموع الضلعين الآخرين: 8 + 8 = 16. أكبر عدد صحيح أصغر من 16 هو 15 سم. مع 16 سم تقع الرؤوس الثلاثة على استقامة واحدة. » |
| `04-defi` Q6 | propriété § 🧭 mot pour mot (2-3-10) ; b `نعم` et c `نعم دائمًا` sont du remplissage | « هل يمكن بناء مثلّث أضلاعه 4 سم و6 سم و11 سم؟ » · a `لا، لأنّ 4 + 6 = 10 أصغر من 11` (clé) · b `نعم، لأنّ 4 + 11 أكبر من 6` muette · c `نعم، لأنّ الأضلاع الثلاثة مختلفة` muette · d `لا، لأنّ الأضلاع الثلاثة مختلفة` muette · exp. « نقارن أطول ضلع بمجموع الآخرين: 11 و 4 + 6 = 10. بما أنّ 10 أصغر من 11، يبقى بين القوسين فراغ 11 − 10 = 1 سم، فلا يُبنى المثلّث. مقارنة 4 + 11 بـ 6 لا تكفي: الشرط يخصّ أطول ضلع. » |
| `05-entrainement` Q3 | exemple et `verifie` § 🍰 (angle au وتر 45°) | même énoncé, même figure, mais l'angle demandé est `ب‌ج‌د` : « قطعنا المربّع أ‌ب‌ج‌د بالقطر [أ‌ج] إلى مثلّثين. ما قيس الزاوية ب‌ج‌د بالدرجة؟ » · `value` 90 · exp. « الزاوية ب‌ج‌د رأسها ج وضلعاها [ج‌ب] و [ج‌د]، وهما ضلعا المربّع: هي زاوية المربّع كاملة، قائمة، 90°. القطر [ج‌أ] يمرّ داخلها ويقسمها إلى زاويتين من 45°، لكنّ السؤال عن الزاوية كلّها. » |
| `05-entrainement` Q4 | cas limite de la méthode § 📏 (5-8-5) ; même triangle que Q6 | « في مثلّث متساوي الساقين قاعدته [ب‌ج]، القمّة الرئيسيّة هي: » · a `الرأس أ` (clé) · b `الرأس ب` · c `الرأس ج` · d `منتصف [ب‌ج]`, toutes muettes · exp. « القاعدة هي الضلع المقابل للقمّة الرئيسيّة، و[ب‌ج] تصل الرأسين ب و ج، فالقمّة الرئيسيّة هي الرأس الثالث أ، حيث يلتقي الساقان [أ‌ب] و [أ‌ج]. » |
| `05-entrainement` Q6 | figure 5-5-8 = méthode § 📏 | dans la figure, textes `5`→`4`, `5`→`4`, `8`→`7` (base plus longue que les côtés, la forme reste vraie ; 4 + 4 > 7) ; exp. « ضلعان متساويان (4 و4) والقاعدة مختلفة (7)، فهو متساوي الساقين. » |

Figure de `02-boss` Q5. Partie ombrée (8,24), (92,24), (92,76), angle droit en (92,24). Rendu vérifié :

```html
<svg viewBox="0 0 100 100"><path d="M8 24 L92 24 L92 76 Z" fill="#0f6e56" opacity="0.25"/><polygon points="8,24 92,24 92,76 8,76" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><line x1="8" y1="24" x2="92" y2="76" stroke="currentColor" stroke-width="1.8"/><polyline points="84,24 84,32 92,32" fill="none" stroke="#ef4444" stroke-width="1.5"/></svg>
```

Champs `manuel` :
- `01-pratique` : **supprimer le champ** (L8 ex. 4, 6 et 7 sont devenus des variantes) ;
- `02-boss` : `items` devient `["L8 ex. 11"]` ;
- `03-revision` et `04-defi` : inchangés.

### Mineurs

- **m18-1** `03-revision` Q5 (T3 sit. 3, 6-4-3) : la reprise officielle est fidèle, mais ses nombres sont ceux de L8 ex. 3,
  l'exemple du § 🧭. Garder la question et changer seulement la propriété : `فالأطوال 6 و4 و3 تصلح لأنّ 4 + 3 = 7 أكبر
  من 6` devient `فالأطوال 7 و5 و4 تصلح لأنّ 5 + 4 = 9 أكبر من 7`. La redite de l'exemple qui reste est assumée : deux
  sources officielles partagent ces données.
- **m18-2 — étiquettes.** `02-boss` Q3 d (`قائم الزاوية ومتساوي الأضلاع`) porte `melanges` alors que l'erreur porte sur
  les côtés : passer à `classement-triangle-par-cotes-errone`. `02-boss` Q7 d porte `melanges` alors que l'énoncé ne
  précise pas le classement : la rendre muette.
- **m18-3** `03-revision` Q2 d (`الضلع 8 سم أطول من الورقة`) est absurde. La remplacer par
  `أطول ضلع أكبر من مجموع الضلعين الآخرين` (muette, fausse car 8 = 3 + 5).
- **m18-4** `quiz` Q1 et `03` Q1 (« كم ضلعًا / زاوية ») sont triviaux et leurs distracteurs 4, 2, 5 / 4, 2, 1 du
  remplissage. Tolérable en d1.
- **m18-5** Dans le piège du § 📐, « في كلّ مثلّث زاويتان حادّتان على الأقلّ » est affirmé avant la propriété qui le
  justifie (il vient dans la propriété, juste après). Rien à corriger.

---

## Ch. 19 — `19-quadrilateres` (41 questions re-résolues)

**Clés : 41/41 justes.** Cours re-résolu :
- 5 et 3 ; 16 × 8 ; 7 et 4 ; 12 et 7 ;
- (14 − 5) : 2 = 4,5 et (20 − 6) : 2 = 7 ; 8 : 2 = 4 ;
- 16 − 2 − 2 = 12 ; 9 et 5 ; 3,5 < 4 ; 6 − 2 − 2 = 4 ;
- diagonales 6 et 8 ; 88/132/36 ; construction 4/6/45° (arcs ف 4, ت 6 justes ; le piège donne bien un cerf-volant
  4-4-6-6) ; 3 cm et 75° ;
- 48 et 4,8 m ; 26, 24, 36, 16 ; 16 : 4 = 4 ; 18 et 34.

Tout est juste. Les 14 figures sont vraies : en `03` Q2, les côtés 37 / 49,4 et la diagonale 74 respectent 3 : 4 : 6.
Reprises fidèles : L17 ex. 1, 6, 7, 8, 9 (erratum 15), 11 (errata 16–17), L9 ex. 3, L15 ex. 2, 3, 9, L56 pb 1
(erratum 64), T1 et T3 sit. 3, test d'orientation sit. 4.

**D-1 (section « كيف نُثبت أنّ رباعيًّا متوازي أضلاع؟ »).** Les quatre critères sont justes pour un quadrilatère non
croisé dont on lit les sommets dans l'ordre : deux paires parallèles ; une paire parallèle **et** égale ; deux paires
égales ; diagonales de même milieu. Ils sont posés comme **outils** (« شرط كافٍ، نستعمله ونسمّيه في الإثبات »), jamais
démontrés ✓. Le piège (trapèze isocèle : égalité seule, parallélisme seul) est juste ✓. Un défaut d'énoncé subsiste
dans le `retenir` (M19-1).

Axes du cours :
- clarté ✓, sauf M19-1 ;
- compréhension ✓ (11 sections au patron) ;
- exhaustivité ✓ : diagonales, hauteur, trapèzes particuliers, construction, périmètre ;
- expérience ✓ ;
- illustration ✓.

### Majeurs

**M19-1 — le `retenir` du § 🧾 a une lecture qui enseigne un critère faux.** La phrase « أو كلّ ضلعين متقابلين متوازيان
أو متساويان » se lit aussi « chaque paire de côtés opposés est parallèle **ou** égale ». Le trapèze isocèle (une paire
parallèle, l'autre égale) passe alors pour un parallélogramme : c'est exactement le piège de la section. Remplacer la
ligne par : « رباعيّ متوازي أضلاع بشرط واحد كافٍ: زوجا أضلاعه المتقابلة متوازيان، أو زوجاها متساويان، أو ضلعان
متقابلان متوازيان ومتساويان معًا، أو قطران لهما المنتصف نفسه. »
(`resume.md` n'a pas cette ambiguïté : rien à changer.)

**M19-2 — le piège du § ✖️ affirme une implication fausse en général, et elle redonne `02-boss` Q5.** « رباعيّ قطراه
متعامدان وغير متقايسين → المعيّن » est faux pour un quadrilatère quelconque : le cerf-volant a lui aussi des diagonales
perpendiculaires et inégales. C'est précisément l'erreur que décrit le libellé de `math.geo.condition-suffisante-supposee`,
déclarée par le chapitre. La devinette, restreinte aux parallélogrammes, est en outre la reprise `02-boss` Q5 (L15 ex. 2).
Remplacer les trois lignes du `> ⚠️` par :
« \> ⚠️ **الخطأ الشائع**: في لغز «متوازي أضلاع قطراه متقايسان» يجيب تلميذ: المربّع. تقايس القطرين معيارٌ
\> واحد، ونراجع الثاني: هل هما متعامدان؟ اللغز لا يقول ذلك. الجواب **المستطيل**: قطراه متقايسان، ولا يتعامدان إلّا
\> إذا كان مربّعًا. »

**M19-3 — huit questions redonnent le cours ou forment des doublons de gabarit.**

Corrections côté cours. Elles retirent la redite de `01-pratique` Q8 (reprise L17 ex. 8), de `03-revision` Q5 (test
d'orientation sit. 4) et de `04-defi` Q3 (L17 ex. 1), qui sont gardées :

- **`verifie` § ✖️**, question : « نرسم دائرة مركزها م ونصف قطرها 5 سم، وقطرين لها [أج] و[بد] يصنعان بينهما زاوية
  60°. ما نوع الرباعيّ أبجد؟ وما طول كلّ قطر؟ » ; réponse : « مستطيل. مأ = مج = مب = مد = 5 سم لأنّ النقاط الأربع على
  الدائرة، فللقطرين المنتصف نفسه م، وهما متقايسان (10 سم كلٌّ منهما). لكنّهما غير متعامدين (60° لا 90°)، فهو مستطيل
  وليس مربّعًا. » C'est le jumeau de l'exemple (R-8) ;
- **cas limite § 📐** : `معيّن محيطه 16 سم، ضلعه 16 : 4 = 4 سم` devient `معيّن محيطه 20 سم، ضلعه 20 : 4 = 5 سم` ;
- **`verifie` § 📐** : `ما محيط المعيّن أبدج الذي ضلعه 4,5 سم؟` devient `ما محيط معيّن ضلعه 6,5 سم؟`, et dans la
  réponse `4 × 4,5 = 18 سم` devient `4 × 6,5 = 26 سم`.

Remplacements de questions :

| fichier · Q | défaut | remplacement vérifié |
| --- | --- | --- |
| `quiz` Q4 | tableau § 📐 (9 et 4 → 26) ; gabarit ×3 dans le chapitre | « ما محيط مستطيل طوله 11 سم وعرضه 4 سم؟ » · a `15 سم` (`math.mes.perimetre-rectangle-somme-non-doublee`) · b `44 سم` (`math.mes.aire-et-perimetre-confondus`) · c `30 سم` (clé) · d `19 سم` muette · exp. « للمستطيل طولان وعرضان: المحيط = 2 × (11 + 4) = 2 × 15 = 30 سم. من كتب 15 سم حسب نصف الدورة، ومن كتب 44 سم ضرب الطول في العرض فحسب المساحة. » |
| `04-defi` Q1 | récitation 4 × 5 en défi ; paire 0,64 avec ch. 20 `quiz` Q3 | « مربّع محيطه 36 سم. ما طول ضلعه؟ » + figure existante, texte `5 سم` remplacé par `؟` · a `9 سم` (clé) · b `12 سم` (`math.mes.perimetre-nombre-de-cotes-errone`) · c `18 سم` muette · d `6 سم` (`math.mes.aire-et-perimetre-confondus`) · exp. « للمربّع 4 أضلاع متساوية، فالضلع = 36 ÷ 4 = 9 سم. ونتحقّق: 4 × 9 = 36. من قسم على 3 عدّ أضلاع المثلّث، ومن وجد 6 سم بحث عن عدد مضروب في نفسه يعطي 36، كأنّ المحيط مساحة. » |
| `04-defi` Q2 | gabarit « مستطيل … ما محيطه » (×5) | garder la figure 8 × 3 : « مستطيلٌ طولُه 8 سم وعرضُه 3 سم، ومربّعٌ له المحيط نفسه. ما طولُ ضلع المربّع؟ » · a `5,5 سم` (clé) · b `11 سم` (`perimetre-rectangle-somme-non-doublee`) · c `2,75 سم` muette · d `22 سم` muette · exp. « محيط المستطيل = 2 × (8 + 3) = 2 × 11 = 22 سم. للمربّع المحيط نفسه 22 سم وأضلاعه الأربعة متساوية: الضلع = 22 ÷ 4 = 5,5 سم. ونتحقّق: 4 × 5,5 = 22. » |
| `04-defi` Q4 | récitation 4 × 7 en défi | type `numeric` : « معيّن ضلعه 7 سم، ومستطيل له المحيط نفسه وطوله 9 سم. ما عرض المستطيل بالسنتيمتر؟ » · `value` 5 · exp. « محيط المعيّن = 4 × 7 = 28 سم. للمستطيل المحيط نفسه، ونصفه الطول + العرض: 28 ÷ 2 = 14 سم، فالعرض = 14 − 9 = 5 سم. ونتحقّق: 2 × (9 + 5) = 28. » |
| `04-defi` Q7 | exemple § 🧾 mot pour mot (أدهـك, 36), aussi L56 pb 1 | « في الرباعيّ س‌ص‌ع‌و: س‌ص = ع‌و = 5 سم و ص‌ع = و‌س = 3 سم. ما نوعه؟ » · a `متوازي أضلاع، لأنّ كلّ ضلعين متقابلين متساويان` (clé) · b `شبه منحرف متقايس الضلعين، لأنّ له ضلعين متساويين` (`math.geo.condition-suffisante-supposee`) · c `معيّن، لأنّ أضلاعه المتقابلة متساوية` (`math.geo.quadrilatere-mal-identifie`) · d `لا نحكم قبل قيس زواياه بالكوس` muette · exp. « الأضلاع بالترتيب س‌ص، ص‌ع، ع‌و، و‌س: [س‌ص] يقابل [ع‌و] وكلاهما 5 سم، و[ص‌ع] يقابل [و‌س] وكلاهما 3 سم. كلّ ضلعين متقابلين متساويان: هذا شرط كافٍ، فالرباعيّ متوازي أضلاع. وليس معيّنًا لأنّ 5 ≠ 3، ولا شبه منحرف لأنّ له زوجين من الأضلاع المتوازية لا زوجًا واحدًا. » (Clé moins longue que b.) |
| `05-entrainement` Q3 | exemple et piège § 🛠️ (نتقف 4/6) | « نبني متوازي أضلاع أ‌ب‌ج‌د فيه أب = 5 سم و أد = 3 سم، وقد رسمنا الضلعين [أب] و[أد]. ما فتحتا الفرجار لتعيين الرأس ج؟ » · a `مركز ب ومركز د بفتحة 4 سم` · b `مركز ب بفتحة 3 سم، ومركز د بفتحة 5 سم` (clé) · c `مركز ب بفتحة 5 سم، ومركز د بفتحة 3 سم` · d `مركز أ بفتحة 3 سم، ومركز أ بفتحة 5 سم`, toutes muettes · exp. « ج تقابل أ. الضلع [بج] يقابل [أد] فيساويه 3 سم، والضلع [دج] يقابل [أب] فيساويه 5 سم. فنركّز في ب بفتحة 3 سم وفي د بفتحة 5 سم. تبديل الفتحتين يعطي رباعيًّا ليس متوازي أضلاع. » |
| `05-entrainement` Q4 | gabarit « مستطيل … ما محيطه » | « ما محيطُ متوازي أضلاعٍ ضلعاه المتجاوران 7 سم و 4 سم؟ » · a `22 سم` (clé) · b `11 سم` · c `28 سم` · d `44 سم`, toutes muettes · exp. « في متوازي الأضلاع كلّ ضلعين متقابلين متساويان: الأضلاع 7 و4 و7 و4، والمحيط = 2 × (7 + 4) = 2 × 11 = 22 سم. من كتب 11 سم حسب نصف الدورة فقط. » |

Champ `manuel` de `04-defi` : `items` devient `["L17 ex. 1", "L17 ex. 6", "L17 ex. 9", "L17 ex. 11"]`.

**M19-4 — la clé se repère à sa forme, et deux questions ont des distracteurs de remplissage.**

- `quiz` Q5. La clé est la seule option développée. Options : a `لمتوازي الأضلاع زوجٌ واحد، ولشبه المنحرف زوجان` · b
  `لكلٍّ منهما زوجان من الأضلاع المتوازية` · c `لكلٍّ منهما زوجٌ واحد من الأضلاع المتوازية` · d
  `لمتوازي الأضلاع زوجان، ولشبه المنحرف زوجٌ واحد` (clé). a, b et c portent
  `math.geo.paires-de-cotes-paralleles-mal-comptees`. Explication inchangée.
- `02-boss` Q2. « مثلّث » et « بلا تصنيف » sont du remplissage. Options : a `مستطيلٌ ومعيّن` (clé) · b `مستطيلٌ لا معيّن`
  (`quadrilatere-mal-identifie`) · c `معيّنٌ لا مستطيل` (idem) · d `شبه منحرف ومتوازي أضلاع`
  (`paires-de-cotes-paralleles-mal-comptees`). Explication inchangée.
- `02-boss` Q6. La clé est la plus longue et « أضلاعَه مختلفة » est du remplissage. Options : a
  `له زوجٌ واحدٌ فقط من الأضلاع المتوازية` (`paires-de-cotes-paralleles-mal-comptees`) · b `قطراه متعامدان`
  (`math.geo.diagonales-proprietes-mal-attribuees`) · c `لا أضلاع متوازية فيه` (`paires-…`) · d
  `أضلاعه المتقابلة متوازية` (clé) · exp. « المستطيل كلّ ضلعين متقابلين فيه متوازيان، وهذا تعريف متوازي الأضلاع؛ وتضيف
  له زواياه القائمة اسمه الأدقّ. وقطراه متقايسان لا متعامدان. »

### Mineurs

- **m19-1** `02-boss` Q3 (« ماذا تمثّل [قن] », reprise de L9 ex. 3) : le cours prend cet exercice pour ancrage, avec les
  mêmes lettres. C'est un rappel de définition en d2. Tolérable, à changer si le boss est retouché : prendre la reprise
  L15 ex. 5 (hauteur du parallélogramme, avec sa figure).
- **m19-2** L'exemple du § ✖️ passe des diagonales à la nature (« لهما المنتصف نفسه ← متوازي أضلاع »,
  « متقايسان ← مستطيل ») avant que le § 🧾 ne pose ces sens réciproques comme critères. Il le fait sous forme de constat
  vérifié au كوس, ce qui est conforme à D-1. Ajouter si on retouche : « وبالعكس، قطران لهما المنتصف نفسه ومتقايسان
  يعطيان مستطيلًا. »
- **m19-3 — étiquettes.** `04-defi` Q5 d et `04-defi` Q8 b portent une étiquette qui ne nomme pas l'erreur exécutée :
  les rendre muettes.
- **m19-4 — rendu à 360 px.** Dans le tableau du § 📐, la colonne « مثال » coupe les formules en deux lignes
  (`… 2` / `× 13 = 26 سم`). Remplacer les quatre cellules par `2 × (9 + 4) = 26`, `4 × 6 = 24`, `4 × 9 = 36` et
  `2 × (5 + 3) = 16`, avec l'en-tête `مثال (سم)`.
- **m19-5** `03` Q6 (« أيّ العبارات خطأ ») et `05` Q2 (la méthode du trapèze rectangle) recoupent le `verifie` § 🟩 et
  la méthode du § ✏️. Ce sont des rappels, tolérables.

---

## Synthèse

| chapitre | questions re-résolues | clés fausses | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- | --- |
| 16 | 41 | 0 | 0 | 2 (M16-1 : 13 questions ; M16-2) | 6 |
| 17 | 42 | 0 | 0 | 2 (M17-1 : 19 questions + 3 retouches de cours ; M17-2) | 3 |
| 18 | 42 | 0 | 1 (`quiz` Q2, deux réponses) | 1 (M18-1 : 19 questions + 3 retouches de cours) | 5 |
| 19 | 41 | 0 | 0 | 4 (M19-1 `retenir` ambigu ; M19-2 piège faux ; M19-3 : 7 questions + 3 retouches de cours ; M19-4) | 5 |
| **lot** | **166** | **0** | **1** | **9** | **19** |

**Ce qui est solide.** Les 166 clés sont justes. Les 47 figures de cours et toutes celles des questions sont vraies. Le
patron de notion est complet dans les 38 sections. M3 et D-2 sont tenus. Les critères de parallélogramme (D-1) sont
justes et posés comme outils. Les reprises sont fidèles au manuel, errata compris. Le rendu à 360 px est propre.

**Ce qui ne l'est pas.** Le défaut dominant annoncé est massif. **58 questions** redonnent un exemple, un piège, un
`verifie` ou une propriété du cours, ou en sont des doublons ou des copies de gabarit. Au ch. 17, une même question
existe quatre fois ; les défis des ch. 16 et 19 récitent le cours. Les autres défauts :
- 1 question à deux réponses (C18-1) ;
- 2 énoncés de cours mathématiquement fautifs en lecture littérale (M19-1, M19-2) ;
- quelques clés qui se repèrent à leur forme, et des distracteurs de remplissage.

Chaque correction est donnée avec un texte exact vérifié. Dans 9 cas, c'est le **cours** qui change de nombres (tableau
du ch. 17, propriétés et `verifie` des ch. 18 et 19), ce qui permet de garder les reprises officielles. Les champs
`manuel` sont à mettre à jour dans 5 fichiers. Les nouvelles figures (6 SVG) ont été rendues et contrôlées par calcul.

**Verdict : à corriger.** C18-1 et M19-1/M19-2 d'abord, puis les remplacements M16-1, M17-1, M18-1 et M19-3. Après
correction : `content:check`, `content:qa`, `content:figures:check`, puis `content:tranche` **sans `--fresh`** (il doit
tomber à 0 paire proche interne au lot, hors paires justifiées), et une relecture des 6 SVG rendus.
