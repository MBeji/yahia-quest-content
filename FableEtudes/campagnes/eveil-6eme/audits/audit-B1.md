# Audit B1 — `09-oeil-vision` · `12-dhaw` · `01-air`

> Auditeur indépendant (opus), 2026-10-20. Branche `wip/eveil-6eme-un-passage` @ `33a161ec`.
> Valide pour ce commit : ré-auditer si les fichiers ont bougé.
> Lus en entier avant l'audit : `content-audit`, `course-quality.md`, `course-explanation.md`,
> `prof-eveil-primaire`, la fiche `6eme-base/eveil.md` (§ 1.7, § 2 و1–و2, § 4 bis, § 6.0–6.1,
> § 7.1–7.13, 7.16–7.21), PLAN § 3 (V1–V5, E-7a, E-7b). Manuel `103604` relu **à l'image**
> p.7–28 (و1) et p.30–60 (و2) ; guide `503604` p.53–54, 77, 83, 86, 129–130. Re-résolution à
> l'aveugle de toutes les questions faite AVANT la lecture des notes et du rapport de l'auteur.

## Bilan

| chapitre | questions re-résolues | critique | majeur | mineur |
| --- | --: | --: | --: | --: |
| 09-oeil-vision | 49 (quiz 7 + 9/8/8/9/8) | 0 | 2 | 5 |
| 12-dhaw | 43 (quiz 5 + 8/7/8/8/7) | 0 | 7 | 2 |
| 01-air | 45 (quiz 6 + 8/8/8/8/7) | 0 | 7 | 4 |
| **total** | **137** | **0** | **16** | **11** |

Aucune clé fausse, aucune question à deux réponses, aucune erreur scientifique ; aucune erreur du
manuel reprise (cornée, lentille concave pour l'hypermétropie, vitré pris pour la lentille, « CO₂
سامّ », bougie mesurant le 1/5, suie de la flamme bleue du réchaud). V1 tenu (aucun chiffre du ملفّ
en clé ; 1/5 et 1,3 g sont des valeurs du manuel). Les défauts majeurs sont presque tous du même
type : **une question qui redonne la scène d'un exemple résolu du cours** (13 questions), deux
doublons dans un même exercice, un distracteur éliminé par l'énoncé, et l'arbitrage **E-7a**
(monoxyde de carbone) pas encore appliqué au ch. `01`.

**Verdict : à corriger.** Tous les remplacements ci-dessous sont vérifiés : une seule réponse
défendable, aucune fuite, clé jamais strictement la plus longue (longueurs mesurées entre
crochets, dans l'ordre des options), étiquettes = libellés réels de `misconceptions.json`.

### Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

- `content:check` ✓ (121 matières) · `content:qa -- --subject eveil-scientifique-6eme` ✓ 0 erreur,
  0 avertissement sur B1 · `content:figures:check` ✓.
- `content:tranche -- --chapters 09-oeil-vision,12-dhaw,01-air --fresh --strict-longest
  --strict-lessons` ✓ : clé strictement la plus longue 0/18, paires proches 0, patron de notion
  0 en recul. Mesure maison sur **toutes** les QCM : 1/41 (09), 0/39 (12), 0/41 (01).
- Notation (hors `<svg>`) : 0 chiffre indo-arabe, 0 LaTeX, 0 `$…$`, 0 groupe `\d \d{3}`.
- Rendu : `renderLesson`/`renderSummary` (vitest jetable, supprimé) puis Chromium 360 px : largeur
  de page 360 (aucun débordement), tableaux ≤ 328 px, 8 figures de cours et 5 figures de questions
  rendues et vérifiées à l'œil et par leurs coordonnées (œil : 9 repères sur la bonne structure ;
  défauts de vision : foyer sur / devant / derrière la rétine ; réfraction air→eau et pièce : rapport
  des sinus 1,33 ; miroir et 12/04 q8 : incidence 38,2° = réflexion «ج» ; flamme : 3 zones à la
  bonne place). 7 `::: verifie` par cours, repliés.

## 1. Doute n°1 de l'auteur — zones de la flamme : TRANCHÉ, le cours est juste, la fiche doit être corrigée

Relu à l'image :

- **manuel p.57** (أجرّب 4, essai 3) : figure légendée **منطقة مضيئة** (haut) · **منطقة داكنة**
  (milieu, autour de la mèche) · **منطقة زرقاء** (bas) ; essai 4 : trois fils dans les trois zones.
- **manuel p.58** (أستنتج 5, mots imposés : زرقاء · قاتمة · صفراء…) : « منطقة [..] حيث يكون الاحتراق
  تامًّا وحرارتها شديدة » · « منطقة [..] متكوّنة من غاز لم تبدأ فيه عمليّة الاحتراق وهو غاز الشّمع »
  · « منطقة [..] **ومضيئة** حيث يكون الاحتراق غير تامّ وبها هباب الفحم ». « ومضيئة » + la figure
  p.57 imposent : **jaune lumineuse = incomplète + suie**, donc bleue = complète et très chaude.
- **manuel p.59** (أقيّم 7) : fil de cuivre **يحمرّ** في الزّرقاء · **لا يحمرّ** في القاتمة · **يسودّ**
  في الصّفراء.
- **guide p.77** (ملفّ) : jaune lumineuse en haut, fil couvert de noir (هباب) ; sombre au milieu, fil
  qui ne rougit pas, température basse ; bleue en bas, température très élevée. **Concorde.**
- **guide p.83** (استنتاج 6 de la جذاذة) : « منطقة مضيئة (احتراق تامّ)… منطقة زرقاء بها هباب الفحم
  (احتراق غير تامّ) » — **seule page inversée**, coquille du guide.
- La « suie attribuée à la flamme bleue » du § 4 bis n'est **pas** la bougie : c'est le **réchaud à
  gaz** du manuel p.55 (أطبّق 6 أ : « يحترق غاز الموقد في الهواء بلهب مضيء لونه أزرق فينتج عن ذلك
  … وهباب الفحم »). La fiche (§ 6.1-12) rapproche à tort cette erreur des zones de la bougie.

**Décision** : le cours `01` (§ 🕯️, figure, tableau, fil qui rougit/ne rougit pas/noircit) et
`04-defi` q5–q6 sont justes et conformes au manuel ; ils restent. La fiche doit être corrigée
(fichier `content/programmes-officiels/programme/6eme-base/eveil.md`, texte exact proposé) :

1. § 2 و2, ligne « ◐ RENCONTRÉ » — remplacer
   « ; les trois zones de la flamme (p.77 vs p.83 : **contradictoires**, cf. §7.20 — pas de clé) »
   par « » (supprimer), et ajouter à la ligne « ✅ INCLUS », après « la bougie (manuel p.56–60) » :
   « ; **les trois zones de la flamme** — bleue : احتراق تامّ, très chaude, fil de cuivre rougi ;
   sombre : غاز الشّمع non brûlé, fil non rougi ; jaune lumineuse : احتراق غير تامّ, هباب الفحم, fil
   noirci (manuel p.57–59 ; guide p.77 ; le استنتاج 6 du guide p.83 inverse bleue et lumineuse —
   coquille, à ne pas reprendre) ».
2. § 6.1, point 12 — remplacer tout le point par :
   « 12. **Zones de la flamme** : le استنتاج 6 de la جذاذة (p.83) inverse la zone lumineuse et la zone
   bleue ; le ملفّ (p.77) **et le manuel élève** (p.57 figure, p.58 أستنتج 5, p.59 أقيّم 7) disent
   tous : bleue = complète et très chaude (fil rougi), sombre = gaz de cire (fil non rougi), jaune
   lumineuse = incomplète avec suie (fil noirci). Le manuel fait foi : **clé possible** (relu à
   l'image, audit B1). Erreur distincte, à ne pas reprendre : le manuel p.55 (أطبّق 6 أ) attribue la
   suie à la flamme **bleue du réchaud à gaz**. »
3. § 4 bis, point 1 — remplacer « la suie attribuée à la flamme bleue » par « la suie attribuée à la
   flamme bleue du réchaud à gaz (p.55) ».
4. § 7.20, fin de l'encadré ⚠️ — remplacer « Conséquence pratique : ce point, malgré son intérêt
   pédagogique signalé en §7.17, **n'a pas de clé fiable** dans ce volume — ne pas en faire un item à
   réponse unique. » par « **Levé (audit B1, 2026-10-20)** : le manuel élève (p.57–59) tranche dans
   le sens du ملفّ p.77 ; seule la p.83 est inversée. Clé fiable : celle du manuel. »

## 2. Arbitrage E-7a — le monoxyde de carbone au ch. `01` : texte vérifié à ajouter

Constat préalable : le manuel n'est pas muet — il **nomme** le gaz (p.56, المفاهيم : « أحادي أكسيد
الكربون » ; p.59, أطبّق 6 ب : dans la liste de mots) et pose la situation du كانون dans une maison
fermée (p.56, 1 ب : « ما هي الأخطار… ؟ ») sans jamais l'expliquer. « Absent du manuel » (PLAN § 3)
est donc à lire « nommé, non enseigné ». Le guide l'enseigne p.73 (« أوّل أكسيد الكربون ») et le
corrigé p.86 (« أحادي أكسيد الكربون »). Le ch. `02` en dit déjà : احتراق غير تامّ en lieu fermé →
أحادي أكسيد الكربون, سامّ, لا لون له ولا رائحة, يمنع الجسم من الاستفادة من الأكسجين ; distinct du
CO₂ du زفير ; aérer ; scène du كانون familial. La section ci-dessous emploie **les mêmes mots**, ne
reprend **pas** la scène du كانون (réservée au `02`), ne donne **aucun seuil** (V1), ne dit jamais que
le CO₂ est سامّ (erreur du manuel p.42), et corrige au passage l'erreur p.55 (le bleu = complet).

### 2.1 `01-air/cours.md` — nouvelle section, insérée après le `::: retenir` de « 🕯️ احتراق الشمعة
ومناطق لهبها » (ligne 421), avant la ligne `> 🏆` (≈ 45 lignes, patron complet T1–T7)

```markdown
## ☠️ الاحتراق غير التامّ: غاز سامّ لا نراه ولا نشمّه

في المطبخ صار لهب موقد الغاز أصفر بعد أن كان أزرق، واسودّ قعر القدر. أسرع الأب ففتح النّافذة
وقال: «الخطر ليس في السّواد وحده». السّواد نعرفه: هو هباب الفحم. فما الخطر الآخر الّذي لا نراه؟

::: definition
حين لا تجد المادّة المحترقة ما يكفيها من الأكسجين يكون **الاحتراق غير تامّ**. ينتج عنه، زيادة
على ثاني أكسيد الكربون وبخار الماء، **هباب الفحم** وغاز سامّ هو **أحادي أكسيد الكربون**
(monoxyde de carbone): لا لون له ولا رائحة، ويمنع الجسم من الاستفادة من الأكسجين.
:::

| الاحتراق | الأكسجين حول النّار | ما ينتج عنه                                   | لهب موقد الغاز       |
| -------- | ------------------- | --------------------------------------------- | -------------------- |
| تامّ     | كافٍ                | ثاني أكسيد الكربون، بخار الماء، حرارة، ضوء    | أزرق، لا يسوّد القدر |
| غير تامّ | قليل                | ما سبق، ومعه هباب الفحم وأحادي أكسيد الكربون | أصفر، يسوّد القدر    |

السّطر الثاني هو الأوّل وقد زيد عليه ناتجان: هباب الفحم نراه سوادًا، وأحادي أكسيد الكربون لا نراه
ولا نشمّه.

::: exemple لماذا فتح الأب النّافذة؟

1. صار اللّهب أصفر واسودّ القدر — لأنّ هباب الفحم لا ينتج إلّا حين يكون الاحتراق غير تامّ.
2. إذن لم يجد الغاز ما يكفيه من الأكسجين — لأنّ الاحتراق يصير غير تامّ حين يقلّ الأكسجين.
3. فينتج أيضًا أحادي أكسيد الكربون — لأنّ الاحتراق غير التامّ ينتجه مع هباب الفحم.
4. لا يراه أحد ولا يشمّه — لأنّه غاز لا لون له ولا رائحة.
5. النّافذة المفتوحة تُدخل هواءً جديدًا — فيتجدّد الأكسجين ويخرج الغاز السّامّ.

:::

::: piege الخطأ الشائع
«الغاز السّامّ الّذي ينتج عن النّار هو ثاني أكسيد الكربون.» يغرّنا تشابه الاسمين. والصواب: ثاني
أكسيد الكربون ينتج عن كلّ احتراق، ونطرحه مع زفيرنا في كلّ لحظة، ونكشفه بماء الجير؛ أمّا الغاز
السّامّ فهو **أحادي أكسيد الكربون**، وينتج حين يكون الاحتراق غير تامّ.
:::

::: propriete
كلّ نار تشتعل في مكان مغلق قد تُنتج أحادي أكسيد الكربون: الفحم في الكانون، والحطب في المدفأة،
والغاز في الموقد أو في سخّان الماء. لذلك نهوّي كلّ مكان فيه نار، ولا ننام قرب نار مشتعلة في غرفة
مغلقة، ونُخرج من يحسّ بصداع أو دوار أو نعاس إلى الهواء الطّلق. حالة تستحقّ الانتباه: غياب
الرّائحة لا يعني غياب الخطر، لأنّ هذا الغاز لا رائحة له.
:::

::: verifie
في حمّام صغير نافذته مغلقة يعمل سخّان ماء بالغاز، فصار لهبه أصفر. بمَ تنصح، ولماذا؟

---

أنصح بفتح النّافذة وإطفاء السّخّان حتّى يُصلَح، لأنّ اللّهب الأصفر علامة احتراق غير تامّ لقلّة
الأكسجين، وهذا الاحتراق ينتج أحادي أكسيد الكربون، غازًا سامًّا لا لون له ولا رائحة؛ والتّهوئة
تجدّد الأكسجين وتُخرج الغاز.
:::

::: retenir
حين يقلّ الأكسجين يكون الاحتراق غير تامّ فينتج هباب الفحم وأحادي أكسيد الكربون، غازًا سامًّا لا لون له ولا رائحة؛ فنهوّي كلّ مكان فيه نار.
:::

> 📚 **تكملة لكتابك المدرسي**: يذكر كتاب التّلميذ اسم هذا الغاز ويسأل عن خطر كانون مشتعل في بيت
> مغلق، لكنّه لا يشرحه؛ وقد طرحته أسئلة المناظرة في سنوات عدّة، فنتعلّمه هنا.
```

Vérifié : chaque étape de l'exemple est vraie et cohérente avec le tableau ; la flamme bleue d'un
réchaud bien réglé = combustion complète (guide p.75, « الهوّاية ») ; « قد تُنتج » est la bonne
prudence (une flamme bien aérée n'en produit pas de quantité dangereuse) ; le piège n'affirme pas
que le CO₂ est inoffensif, seulement qu'il n'est pas « le » gaz toxique. Le `verifie` est un jumeau
(autre appareil, autre pièce) qui n'introduit aucune notion neuve. Le `> 📚` suit la convention du
ch. `03` (plaquettes, V2). Blanc avant chaque `:::` qui suit une liste (piège Prettier). Facultatif :
`> 🏆` → « … وكيف يُشعل الأكسجين النار، ولماذا نهوّي كلّ مكان فيه نار. التالي: … ».

### 2.2 `01-air/resume.md` — 8ᵉ puce, à la fin

```markdown
- **الاحتراق غير التامّ وأحادي أكسيد الكربون (تكملة للكتاب)**: حين يقلّ الأكسجين يصير لهب الموقد أصفر ويسودّ القدر، وينتج مع هباب الفحم غاز سامّ لا لون له ولا رائحة هو أحادي أكسيد الكربون (غير ثاني أكسيد الكربون الّذي نطرحه مع الزفير)؛ نهوّي كلّ مكان فيه نار.
```

### 2.3 `01-air/chapter.json`

- `description` : ajouter à la fin « ؛ الاحتراق غير التامّ وغاز أحادي أكسيد الكربون السّامّ (تكملة للكتاب) ».
- `sources[1]` (guide) : « الملفّ العلمي للوحدة 2: الهواء (ص 63–67) » → « الملفّ العلمي للوحدة 2: الهواء
  (ص 63–67) ووقاية الجهاز التنفّسي وغاز أوّل أكسيد الكربون (ص 73) ».
- `coursePitfalls` : ajouter `"eveil.air.co-et-co2-confondus"`.
- **Nouvelle étiquette** à créer dans `content/misconceptions.json` (avant tout le reste, sinon C-5
  échoue) :

```json
"eveil.air.co-et-co2-confondus": {
  "subject": "eveil",
  "labels": {
    "fr": "Tu confonds les deux oxydes de carbone : le dioxyde de carbone sort de toute combustion et de notre expiration et trouble l'eau de chaux ; le gaz toxique et inodore est le monoxyde de carbone, produit quand la combustion est incomplète",
    "en": "You mix up the two carbon oxides: carbon dioxide comes from every burning and from our breath and turns limewater cloudy; the toxic, odourless gas is carbon monoxide, produced when burning is incomplete",
    "ar": "تخلط بين أكسيدَي الكربون: ثاني أكسيد الكربون ينتج عن كلّ احتراق ونطرحه مع الزفير ويعكّر ماء الجير، أمّا الغاز السّامّ الّذي لا رائحة له فهو أحادي أكسيد الكربون، وينتج حين يكون الاحتراق غير تامّ"
  }
}
```

### 2.4 Les deux questions (vérifiées)

**CO-1 — `01-air/quiz.json`, ajoutée en fin (q7), difficulté 2.**

```json
{
  "prompt": "في كوخ مغلق تحترق قطع من الحطب بلهب أصفر، وتسودّ جدرانه بالدّخان. أيّ غاز سامّ ينتج في هذه الحالة ولا ينتج حين يكون الاحتراق تامًّا؟",
  "options": [
    { "id": "a", "text": "أحادي أكسيد الكربون" },
    { "id": "b", "text": "ثاني أكسيد الكربون", "misconceptionTag": "eveil.air.co-et-co2-confondus" },
    { "id": "c", "text": "بخار الماء السّاخن" },
    { "id": "d", "text": "الأكسجين الّذي نتنفّسه", "misconceptionTag": "eveil.air.reactifs-et-produits-inverses" }
  ],
  "correctOption": "a",
  "explanation": "الدّخان الأسود هباب الفحم، وهو علامة احتراق غير تامّ لأنّ الأكسجين لم يكفِ الحطب في الكوخ المغلق؛ وفي هذه الحالة ينتج أيضًا أحادي أكسيد الكربون، وهو غاز سامّ لا لون له ولا رائحة. أمّا ثاني أكسيد الكربون وبخار الماء فينتجان في الاحتراق التامّ وغير التامّ معًا، والأكسجين يُستهلك في الاحتراق ولا ينتج عنه.",
  "difficulty": 2
}
```

Longueurs [19, 18, 18, 22] — clé non la plus longue. Une seule réponse : le CO₂ et la vapeur
naissent aussi d'une combustion complète, l'O₂ est consommé ; seul le CO répond aux deux conditions
(سامّ + propre à l'incomplète). Scène différente de l'exemple (cuisine) et du `verifie` (salle de
bain). Raisonnement en deux pas (suie → incomplète → CO), au niveau d2.

**CO-2 — `01-air/exercices/05-entrainement.json`, ajoutée en fin (q8), difficulté 3** (≥ max du
fichier ; le fichier passe à 8 questions).

```json
{
  "prompt": "كتب تلميذ: «الغاز السّامّ الّذي ينتج حين يكون الاحتراق غير تامّ هو ثاني أكسيد الكربون، ونكشفه برائحته». كيف نصحّح عبارته؟",
  "options": [
    { "id": "a", "text": "هو أحادي أكسيد الكربون، وهو غاز لا رائحة له" },
    { "id": "b", "text": "هو ثاني أكسيد الكربون فعلًا، لكنّه لا رائحة له", "misconceptionTag": "eveil.air.co-et-co2-confondus" },
    { "id": "c", "text": "هو أحادي أكسيد الكربون، ونكشفه برائحته القويّة" },
    { "id": "d", "text": "هو بخار الماء، ونكشفه بقطيرات على جدار بارد" }
  ],
  "correctOption": "a",
  "explanation": "الغاز السّامّ الّذي ينتج عن الاحتراق غير التامّ هو أحادي أكسيد الكربون، ولا لون له ولا رائحة، لذلك لا ننتبه إليه ونهوّي كلّ مكان فيه نار. أمّا ثاني أكسيد الكربون فينتج عن كلّ احتراق ونطرحه مع زفيرنا ونكشفه بماء الجير، وبخار الماء يتكثّف قطيرات على جدار بارد وليس غازًا سامًّا.",
  "difficulty": 3
}
```

Longueurs [43, 46, 46, 43]. Chasse à l'erreur à deux fautes (nom du gaz, odeur), au format مع3 du
guide : la clé corrige les deux, b ne corrige que l'odeur, c que le nom, d remplace par un autre gaz
— chaque distracteur porte **une** erreur ; c reste muet (aucune étiquette « détecté à l'odeur » au
registre).

**Retouche liée** — `01-air/exercices/05-entrainement.json` q4 (kanoun, fenêtres fermées), clé
inchangée, `explanation` → « الفحم يستهلك الأكسجين، والغرفة مغلقة فلا يتجدّد الهواء، فيقلّ الأكسجين
ويصير الاحتراق غير تامّ فينتج أحادي أكسيد الكربون، غازًا سامًّا لا رائحة له، ويحدث الاختناق. لذلك
نهوّي الغرفة ولا نترك الكانون في مكان مغلق. والاحتراق لا يزيد الأكسجين، بل يستهلكه. »

Cohérence avec `02` : mêmes termes ; `02` garde sa scène (كانون familial) et son piège (« pas
d'odeur donc pas de danger ») ; `01` porte le piège CO/CO₂. Aucune question ne doit désormais avoir
« أحادي أكسيد الكربون » comme **distracteur** d'une liste de produits de la bougie (manuel p.59 6 ب)
puisque la zone jaune est une combustion incomplète.

## 3. Défauts — `09-oeil-vision`

Cours : patron complet dans les 7 sections (T1→T7 + retenir, exemples re-résolus justes, pièges
justes et étiquetés, 7 `coursePitfalls` tous montrés et portés), figures vraies, cavités conformes au
manuel p.8 (doute n°2 de l'auteur : le cours suit le manuel, aucune clé n'en dépend — accepté).

**[MAJEUR] `exercices/03-revision.json` q6** — redonne l'exemple résolu « نظّارة صفوان » (même scène :
il rapproche le livre → concaves). Remplacer le `prompt` seulement (options, clé `d`, étiquettes
inchangées ; longueurs [47, 46, 46, 47]) :
- prompt : « لا يقرأ سامي لافتات الشّارع إلّا إذا اقترب منها كثيرًا. أيّ نظّارة يُرجَّح أن يحتاج إليها، ولماذا؟ »
- explanation : « من لا يرى البعيد بوضوح إلّا إذا اقترب منه مصاب بقصر النّظر: صورة اللافتة البعيدة ترتسم في عينه أمام الشبكيّة؛ فيحتاج إلى عدستين مقعّرتين تُبعدان الأشعّة حتّى تبلغ الصورة الشبكيّة. أمّا العدسة المحدّبة فتُصلح طول النّظر، حين ترتسم الصورة خلف الشبكيّة. »

**[MAJEUR] `exercices/05-entrainement.json` q2** — redonne la scène de la section 🩺 (رمد dans le
قسم + exemple « ماذا يفعل صديق التلميذ المصاب؟ »). Nouveau texte (clé `b`, c étiquetée
`eveil.vision.linge-d-autrui-sans-risque` ; [35, 30, 31, 31]) :
- prompt : « عادت سلمى من المسبح وعيناها محمرّتان، فشخّص الطّبيب الرّمد. أيّ سلوك يحمي أخاها من العدوى؟ »
- a « أن يحكّ عينيه بيديه كلّما شعر بحكّة » · b « ألّا يستعمل منشفتها أو منديلها » · c « أن يستعمل منشفتها إذا بدت نظيفة » · d « أن يجلس بجانبها ويستعمل أدواتها »
- explanation : « الرّمد مرض معدٍ ينتقل بالمناشف والمناديل والأيدي، لذلك لا يستعمل منشفة أخته أو منديلها مهما بدت نظيفة، ولا يشاركها أدواتها حتّى تُشفى. وحكّ العين باليد ينقل إليها العدوى بدل أن يحميها. »

**[MINEUR] `exercices/04-defi.json` q5** — même scène que `03-revision` q8 (« ترى السبّورة بوضوح
لكنّها تُبعد الكتاب ») et que le `verifie` « عليّ يُبعد الكتاب ». Nouveau prompt (options/clé
inchangées) : « يرى يوسف اللافتات البعيدة بوضوح، لكنّ الحروف تبدو له غير واضحة حين يقرّب الكتاب من عينيه. أين ترتسم صورة الكتاب في عينه قبل الإصلاح؟ » ; explanation : « من يرى البعيد بوضوح ولا يرى القريب بوضوح مصاب بطول النّظر، وفي عينه ترتسم صورة الكتاب القريب خلف الشبكيّة. الخطأ الشائع ربط كلمة «طول» بالعجز عن رؤية البعيد: الصورة أمام الشبكيّة هي حال قصر النّظر. »

**[MINEUR] `exercices/04-defi.json` q8 (short_answer)** — (1) l'explication (indice payant)
contient « عدسة تقرّب الأشعّة », quasi littéralement la réponse acceptée « عدسة مقربة » : remplacer
« فيحتاج إلى عدسة تقرّب الأشعّة حتّى تتقدّم الصورة إلى الشبكيّة » par « فيحتاج إلى عدسة تُقدِّم الصورة حتّى تبلغ الشبكيّة ». (2) `acceptedAnswers` incomplets (la normalisation ne retire pas
l'article ni le duel) : ajouter « العدسة المقربة », « العدسة اللامة », « عدستين محدبتين »,
« عدستان محدبتان », « محدبتين », « نظارة ذات عدستين محدبتين ».

**[MINEUR] `exercices/03-revision.json` q8 (short_answer)** — `acceptedAnswers` : ajouter « طمس »,
« طول البصر », « بعد النظر », « مد البصر », « مصابة بطول النظر » (synonymes usuels ; « الطمس »
seul est déjà là).

**[MINEUR] étiquettes** — `02-boss` q3 c « يرسل الضوء نحو الأشياء » (le **cerveau**) et `04-defi`
q2 d « المخّ يرسل الأشعّة… » portent `eveil.lum.oeil-emet-la-lumiere`, dont le libellé dit « l'œil
envoie de la lumière » : l'option n'exécute pas exactement cette erreur → retirer l'étiquette (muettes).

**[MINEUR] `chapter.json` description** — la liste des « أعضاء داخليّة » omet « الخلط المائي »,
enseigné : ajouter « والخلط المائي » après « الخلط الزجاجي ».

## 4. Défauts — `12-dhaw`

Cours : patron complet dans les 7 sections ; les 4 figures sont vraies (sinus 1,33 ; image de la
pièce à 0,67 de la profondeur ; réflexion symétrique) ; tracé qualitatif du rayon réfléchi (manuel
p.19) et « زاوية الورود = زاوية الانعكاس » en `للاستزادة` ◐ — conforme ; doute n°3 de l'auteur levé
(figure de 12/04 q8 rendue au pixel, juste).

**[MAJEUR] six questions redonnent la scène d'un exemple résolu** (et `02-boss` q6 double en plus
`02-boss` q7 — même tâche « classer trois scènes » dans le même exercice). Remplacements :

1. **`quiz.json` q5** (= exemple « نرى الكتاب… ») — clé `a` ; [44, 44, 35, 37]
   - prompt : « في القسم المضاء يرى كلّ التّلاميذ السّبّورة من أماكنهم المختلفة، مع أنّها لا تُرسل ضوءًا من نفسها. لماذا؟ »
   - a « لأنّها تنثر الضّوء الّذي يصلها في كلّ الجهات » · b « لأنّ أعين التّلاميذ ترسل إليها ضوءًا فيرونها » (`eveil.lum.oeil-emet-la-lumiere`) · c « لأنّها تُصدر ضوءًا ضعيفًا لا نلاحظه » (`eveil.lum.objet-eclaire-pris-pour-source`) · d « لأنّها تعكس الضّوء في اتّجاه واحد فقط » (`eveil.lum.phenomenes-lumineux-confondus`)
   - explanation : « يصل ضوء القسم إلى السّبّورة، وهي جسم عاتم غير مصقول، فتنثره في جميع الاتّجاهات، فيصل جزء منه إلى عين كلّ تلميذ أينما جلس. لو عكسته في اتّجاه واحد لما رآها إلّا من يجلس في ذلك الاتّجاه، والعين لا ترسل ضوءًا، والسّبّورة لا تضيء بنفسها. »
2. **`01-pratique` q4** (= ancrage + exemple « المحفظة تحت الطاولة ») — clé `a` ; [38, 37, 42, 36] ;
   retirer du champ `manuel` l'item « ص 10 · ألاحظ 2 » (pages → « 18 ») : un ألاحظ est l'ancrage du
   cours, la variante ne porte pas le champ.
   - prompt : « تضيء الشّمس ساحة المدرسة، لكنّ الرّكن الواقع خلف جدار القسم يبقى مظلّلًا. لماذا؟ »
   - a « لأنّ الجدار جسم عاتم يوقف أشعّة الشّمس » · b « لأنّ الشّمس بعيدة جدًّا عن ذلك الرّكن » (`eveil.lum.ombre-expliquee-par-la-distance`) · c « لأنّ السّاحة واسعة جدًّا فيضعف فيها الضّوء » (même étiquette) · d « لأنّ أرض الرّكن شفّافة يعبرها الضّوء »
   - explanation : « ينتشر ضوء الشّمس وفق خطوط مستقيمة، والجدار جسم عاتم واقع في طريق الأشعّة، فلا يصل الضّوء مباشرة إلى ما خلفه. البعد ليس السّبب: بقيّة السّاحة، على البعد نفسه من الشّمس، مضاءة. »
3. **`01-pratique` q8** (ordering = les 4 pas de l'exemple « الكتاب ») — même clé `a,b,c,d` ;
   - prompt : « ليلًا، يرى صيّاد صخرةً على الشّاطئ يضيئها ضوء المنارة. رتّب ما يحدث من الأوّل إلى الأخير: »
   - a « ينطلق الضّوء من المنارة نحو الصّخرة » · b « يصطدم الضّوء بالصّخرة فينتثر في جميع الاتّجاهات » · c « يصل جزء من الضّوء المنتثر إلى عين الصّيّاد » · d « يرى الصّيّاد الصّخرة »
   - explanation : « تبدأ السّلسلة عند المصدر: ينطلق الضّوء من المنارة فيصل إلى الصّخرة، وهي جسم عاتم غير مصقول فتنثره في كلّ الجهات. ثمّ يصل جزء من الضّوء المنتثر إلى عين الصّيّاد، فتتمّ الرّؤية في الأخير. »
4. **`02-boss` q2** (= exemple « رشا ») — clé `b` ; [39, 34, 37, 34] ; retirer l'item « ص 18 · ألاحظ 2 ».
   - prompt : « في غرفة مظلمة يوجّه سامي ضوء مكشاف نحو مرآة، فتظهر بقعة مضيئة على السّقف. من أين جاء ضوء البقعة؟ »
   - a « المرآة أصدرت أشعّةً من عندها نحو السّقف » (`eveil.lum.objet-eclaire-pris-pour-source`) · b « المرآة عكست ضوء المكشاف نحو السّقف » · c « السّقف وجّه أشعّةً ضوئيّةً نحو المرآة » · d « المرآة كسرت ضوء المكشاف نحو السّقف » (`eveil.lum.phenomenes-lumineux-confondus`)
   - explanation : « الضّوء جاء من المكشاف، والمرآة عكسته لأنّ سطحها مصقول فارتدّ في اتّجاه محدّد نحو السّقف. المرآة ليست مصدرًا ضوئيًّا: لو أطفأنا المكشاف لاختفت البقعة. والانكسار لا يكون إلّا عند عبور الضّوء إلى وسط شفّاف آخر. »
5. **`02-boss` q4** (= section « أين القطعة النقديّة؟ ») — clé `a` ; [35, 41, 34, 36] ; retirer l'item
   « ص 27 · أطبّق 6 ب » (le champ garde « ص 19 · أجرّب 4 », pages « 19 »).
   - prompt : « ينظر صيّاد من زورقه مائلًا إلى سمكة ساكنة في الماء الصّافي، فيراها أقرب إلى السّطح ممّا هي عليه. لماذا؟ »
   - a « لأنّ ضوءها ينكسر عند خروجه من الماء » · b « لأنّ الماء يرفع السّمكة قليلًا نحو السّطح » (`eveil.lum.objet-croit-deforme-par-l-eau`) · c « لأنّ سطح الماء يعكس صورتها كالمرآة » (`eveil.lum.phenomenes-lumineux-confondus`) · d « لأنّ الماء ينثر ضوءها فيكبّر السّمكة »
   - explanation : « الضّوء الآتي من السّمكة يخرج مائلًا من الماء إلى الهواء فيغيّر اتّجاهه عند السّطح، والعين تراه على امتداد الشّعاع الّذي وصلها، فتبدو السّمكة أقرب إلى السّطح. السّمكة باقية في مكانها: الّذي تغيّر هو اتّجاه الضّوء. »
6. **`02-boss` q6** (= exemple « ما الظّاهرة في كلّ حالة؟ » + doublon de q7) — remplacer par une
   chasse à l'erreur sur la source (clé `b` ; [47, 53, 51, 56]) :
   - prompt : « قال أحمد: «القمر مصدر ضوئيّ طبيعيّ مثل الشّمس، لأنّه يضيء طريقنا ليلًا». كيف نصحّح قوله؟ »
   - a « قوله صحيح: كلّ جسم يضيء طريقنا ليلًا مصدر ضوئيّ » (`eveil.lum.objet-eclaire-pris-pour-source`) · b « القمر لا يضيء بنفسه: ينثر نحونا ضوء الشّمس الّذي يصله » · c « القمر مصدر ضوئيّ اصطناعيّ، لأنّه لا يضيء في النّهار » · d « القمر لا يضيء بنفسه: يمرّر ضوء الشّمس كما يمرّره الزّجاج »
   - explanation : « القمر جسم عاتم لا يضيء بنفسه: يصله ضوء الشّمس فينثره في جميع الاتّجاهات، فيصل جزء منه إلى أعيننا. الخطأ الشائع أن نعدّ كلّ جسم يبدو مضيئًا مصدرًا ضوئيًّا؛ والقمر ليس مصدرًا اصطناعيًّا، ولا يمرّر الضّوء لأنّه عاتم. »
   - **à enseigner** (règle d'or, sert aussi `01-pratique` q7 dont le distracteur « القمر » n'est appuyé
     sur aucune ligne du cours) : dans `cours.md` § 🌫️, `::: propriete`, après « فتنعدمُ الرّؤية. »
     ajouter « والقمرُ مثالٌ على ذلك: لا يضيءُ بنفسه، بل ينثرُ نحونا ضوءَ الشّمس الّذي يصلُه، فليس مصدرًا ضوئيًّا. » ; et dans `resume.md`, puce 3, après « نرى الأجسامَ من حولنا. » : « والقمرُ لا يضيءُ بنفسه، بل ينثرُ ضوءَ الشّمس. »

**[MAJEUR] `01-pratique` q5 ↔ exemple § 🪟** — les quatre options (ماء حوض السّباحة، البلّور
الأماميّ للسّيّارة، البلّور المطروق، الكتاب) sont **les quatre objets de l'exemple résolu**. La
question est la reprise déclarée « ص 18 · أتعهّد 1 » (liste du manuel) : on garde la reprise et on
change l'exemple du cours. Dans `cours.md`, `::: exemple نصنّفُ أجسامًا من محيطنا`, remplacer les
quatre lignes par :

```markdown
1. ماءُ الكأس الصّافي **شفّاف**، **لأنّ** الضّوءَ يعبرُه فنرى الملعقةَ داخلَه بوضوح.
2. زجاجُ النّظّارات **شفّاف**، **لأنّ** صاحبَها يرى الأشياءَ من خلاله بوضوح.
3. بلّورُ باب الحمّام المطروق **شافّ**، **لأنّه** يمرّرُ جزءًا من الضّوء فقط.
4. الكرسيُّ الخشبيّ **عاتم**، **لأنّ** الضّوءَ لا يعبرُه: لا نرى ما وراءه.
```

**[MINEUR] `05-entrainement` q7** — reprise du guide p.54 (3ب) : Ahmed sort de **chez l'opticien**
(« محلّ صنع النّظّارات الطّبّيّة »), pas « من عند الصّيدليّ » → remplacer par « خرج أحمد من محلّ
النّظّارات ». Et l'option c (« قوله صحيح، لأنّ الضّوء يعبر هيكل السيّارة إلى وسط شفّاف آخر ») porte
`eveil.lum.reflexion-par-opacite` sans exécuter l'erreur du libellé (« le miroir réfléchit parce
qu'il est transparent ») et cumule deux erreurs → la rendre muette.

**[MINEUR] `03-revision` q8 (short_answer)** — `acceptedAnswers` : ajouter « شبه شفاف », « جسم شبه
شفاف », « الاجسام الشافة », « جسم نصف الشفاف ».

## 5. Défauts — `01-air`

Cours : patron complet dans les 7 sections ; exemples et pièges re-résolus justes ; décision « environ
un cinquième » tenue (« الّذي قلّ هو الأكسجين وحده ») ; zones de la flamme justes (§ 1).

**[MAJEUR] E-7a non appliqué** — voir § 2 (section, résumé, chapter.json, étiquette, 2 questions).

**[MAJEUR] quatre questions redonnent un exemple résolu** :

1. **`01-pratique` q2** (= exemple « الهواء في المحقنة ») — options/clé `b` inchangées ; retirer
   l'item « ص 34 · أجرّب 4 » (pages → « 31, 35, 39 »).
   - prompt : « نسدّ بإصبعنا فتحة منفاخ الدّرّاجة ونضغط ذراعه، فينزل قليلًا ونحسّ بمقاومة. أيّ خاصّية للهواء تظهر؟ »
   - explanation : « ينزل الذّراع رغم أنّ الفتحة مسدودة، فالهواء لم يخرج بل صغر حجمه: هذا الانضغاط. أمّا الانتشار فهو أن يملأ الهواء كلّ الإناء، والتّمدّد زيادة حجمه بالحرارة ولا تسخين هنا، والكتلة يكشفها الميزان. »
2. **`02-boss` q2** (= exemple « حوض طفت عليه طبقة زيت », reprise p.31 6 أ) — remplacé par la
   reprise **p.31 أطبّق 6 ب** (aérateur du مربّى) ; dans le champ `manuel`, « ص 31 · أطبّق 6 أ » →
   « ص 31 · أطبّق 6 ب ». Clé `a` ; [30, 39, 37, 41].
   - prompt : « في مربّى الأسماك بالقسم نضع مضخّة صغيرة تُدخل فقاقيع هواء في الماء باستمرار. لماذا؟ »
   - a « لتجدّد الهواء الذّائب في الماء » · b « لتحرّك ماء الحوض فتسبح فيه الأسماك أسرع » · c « لتدفّئ الماء في ليالي الشّتاء الباردة » · d « للزّينة فقط، لأنّ الأسماك لا تحتاج الهواء » (`eveil.air.vivant-aquatique-sans-air`)
   - explanation : « الأسماك تتنفّس الهواء الذّائب في الماء وتستهلكه، والمضخّة تُدخل هواءً جديدًا باستمرار فيتجدّد. فقاقيعها لا تدفّئ الماء، وليست للزّينة: الحيوان المائيّ يحتاج الهواء كغيره من الكائنات الحيّة. »
3. **`02-boss` q6** (= exemple « لافتات محطّة الوقود », reprise p.55 6 ب) — options/clé `c`
   inchangées ; retirer l'item « ص 55 · أطبّق 6 ب ».
   - prompt : « في مخزن للتّبن والقمح عُلّقت لافتة «ممنوع إشعال النّار والتّدخين». أيّ عنصر من عناصر الاحتراق تمنعه هذه اللافتة؟ »
   - explanation : « عود الثّقاب والسّيجارة المشتعلة مصدران للحرارة. أمّا التّبن والقمح فمادّة قابلة للاحتراق موجودة في المخزن، والأكسجين في الهواء ولا نستطيع إبعاده، فنمنع العنصر الثّالث لأنّ الاحتراق يحتاج العناصر الثّلاثة معًا. وثاني أكسيد الكربون ينتج عن الاحتراق ولا يدخل فيه. »
4. **`03-revision` q3** (= ancrage + exemple « سرّ الكانون ») — clé `a` ; [42, 43, 42, 36].
   - prompt : « في أسفل المدفأة الحطبيّة فتحة صغيرة يمكن توسيعها. لماذا يتأجّج اللّهب حين نوسّعها؟ »
   - a « لأنّها تُدخل هواءً جديدًا فيتجدّد الأكسجين » · b « لأنّها تُخرج الرّماد فيصير الحطب أخفّ وزنًا » · c « لأنّها تُدخل النّتروجين الّذي يؤجّج النّار » (`eveil.air.azote-entretient-combustion`) · d « لأنّها تبرّد جدران الموقد فلا تتشقّق »
   - explanation : « الحطب يحتاج الأكسجين ليحترق، والفتحة الواسعة تُدخل هواءً جديدًا أكثر، فيتجدّد الأكسجين ويتأجّج اللّهب. إخراج الرّماد لا يؤجّج اللّهب، والنّتروجين لا يساعد على الاحتراق، وتبريد الجدران لا يزيد النّار. »

**[MAJEUR] `02-boss` q4 ↔ q8** — même fait dans le même exercice (la plus petite cloche s'éteint
d'abord), et q4 redonne le `verifie` de la section 🔥. Remplacer q4 (clé `a` ; [51, 47, 53, 46]) :
- prompt : « نُدخل شمعة مشتعلة في قارورة كبيرة ونسدّها، فتنطفئ بعد مدّة. نرفع السّدّادة ونُدخل بسرعة شمعة ثانية مشتعلة. ماذا يحدث لها، ولماذا؟ »
- a « تنطفئ بسرعة، لأنّ الأكسجين الباقي لا يكفي لاحتراقها » · b « تشتعل مدّة طويلة، لأنّ في القارورة هواءً كثيرًا » (`eveil.air.air-confondu-avec-oxygene`) · c « تشتعل أقوى، لأنّ النّتروجين الباقي يساعد على الاحتراق » (`eveil.air.azote-entretient-combustion`) · d « تشتعل كالأولى تمامًا، لأنّ الشّمعتين متماثلتان »
- explanation : « انطفأت الشّمعة الأولى لأنّ الأكسجين قلّ في القارورة ولم يتجدّد، فالباقي منه لا يكفي لاحتراق شمعة ثانية، فتنطفئ بسرعة. في القارورة ما يزال هواء، لكنّ النّتروجين الّذي فيه لا يساعد على الاحتراق، وتماثل الشّمعتين لا يغيّر شيئًا ما دام الأكسجين ناقصًا. »
(Conforme à la décision « environ un cinquième, sans dire que la bougie consomme tout l'oxygène ».)

**[MAJEUR] `03-revision` q2 option a** « الأكسجين وحده دون غيره » — un seul gaz alors que l'énoncé
demande « أيّ غازين » : éliminé à vue. Remplacer par « الأكسجين وبخار الماء » [20, 29, 19, 33] (faux
pour une seule raison : l'oxygène aide la combustion).

**[MINEUR] `04-defi` q6** options b « بخار الماء، والاحتراق هناك تامّ » et c « ثاني أكسيد الكربون،
والاحتراق هناك تامّ » portent `eveil.gaz.test-mal-associe` mais cumulent deux erreurs (gaz et
« تامّ ») → muettes.

**[MINEUR] `04-defi` champ `manuel`** — « ص 58 · أجرّب 5 » : à la p.58, le 5 est « أستنتج » ; la
ligne reprise (assiette blanche) est l'essai 5 du tableau « أجرّب 4 » commencé p.57 → « ص 58 · أجرّب 4 (5) ».

**[MINEUR] cours § 🌍, tableau** — « نبتة فول… في صندوق بلّوري مغلق مدّة أسبوع ← تذبل » reprend le
manuel p.31, mais une plante éclairée dans une boîte transparente fermée survit souvent une semaine
(photosynthèse) : aucune clé n'en dépend ; ne pas en faire une question de prédiction.

**[MINEUR] `03-revision` q7** — reprise de T3-أ (guide p.129) avec une option remplacée
(« غير قابل للانحلال في الماء » → « حجمه ثابت… »), déclarée par l'auteur : accepté, à noter comme
variante partielle dans le rapport de campagne.

## 6. Notes et rapport de l'auteur (lus après)

Mes constats rejoignent ses doutes 1–3 (tous levés ci-dessus). Ses étiquettes proposées (§ 4 du
rapport) sont pertinentes ; j'y ajoute `eveil.air.co-et-co2-confondus` (§ 2.3), nécessaire à la
section E-7a. L'auteur n'avait pas vu le recouvrement exemples ↔ questions (son outil de paires
proches compare les questions entre elles, pas au cours) ni le doublon 01/`02-boss` q4–q8.
