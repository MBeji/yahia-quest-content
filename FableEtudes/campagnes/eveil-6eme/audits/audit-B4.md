# Audit indépendant — lot B4 (`07-aimants-boussole` · `11-effets-courant-electrique` · `08-poids`)

Auditeur opus, contexte vierge, branche `wip/eveil-6eme-un-passage` (worktree `/home/user/wt-ev6`), 2026-10-20.
Re-résolution à l'aveugle faite AVANT lecture de `auteurs-notes/B4/NOTES.md` et `rapports/rapport-B4.md`.
PDF relus à l'image : manuel 103604 p.123–125, 127, 131, 132, 134, 137, 138, 144, 145 ; guide 503604 p.175.

## Verdict : **À CORRIGER** (aucune clé fausse, aucune erreur scientifique bloquante ; une série de majeurs à reprendre)

| chapitre | questions re-résolues | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- |
| 07-aimants-boussole | 46 (quiz 6 + 8 + 8 + 8 + 7 + 9) | 0 | 6 | 6 |
| 11-effets-courant-electrique | 45 (quiz 6 + 8 + 8 + 8 + 8 + 7) | 0 | 5 (dont E-7b absent) | 7 |
| 08-poids | 42 (quiz 5 + 8 + 8 + 7 + 7 + 7) | 0 | 14 | 6 |

**Ce qui est bon** : 133 clés justes sur 133, une seule réponse défendable partout, science juste, aucune
étiquette fausse (libellés réels vérifiés), aucun chiffre arabe-indien, aucun LaTeX, aucun groupe de
chiffres bidi-fragile. V1 tenu (2 : 1 et 1/6 seulement en « للاستزادة », jamais une clé), V3 tenu (spires
et piles, jamais « شدّة/intensité » : grep 0), V5 tenu (8 directions enseignées, figure juste, 4 items).
Avertissements « points at an option by its letter » sur `07` : **0 restant** (`content:qa` propre ; mon
balayage des lettres `(a)…(d)`, `(أ)…(د)` et des ordinaux dans les 133 explications : 0). Le manuel fait
l'électrolyse au **sel** (p.123 — erreur de fond : chlore à l'anode) ; le cours l'évite en électrolysant
la **soude** : c'est juste, à garder.

**Ce qui ne va pas** : (1) **réemploi du cours** — 19 questions redonnent tel quel un `::: exemple`, un
`::: verifie`, un `::: piege` ou un cas limite du cours (mêmes données, même demande) : 08 en concentre 13 ;
(2) **figures de 08 cassées en RTL** (étiquettes arabes `text-anchor="start"` qui chevauchent le dessin) ;
(3) **E-7b non fait** (sonnette absente du ch. 11) — texte complet fourni ci-dessous ; (4) trois
`::: piege` sans étiquette du registre.

Gates (depuis `/home/user/eng-deliver`, lien `content` → `wt-ev6/content` inchangé) : `content:check` ✓ ·
`content:qa -- --subject eveil-scientifique-6eme` ✓ « no suspicious answer keys », 0 avertissement ·
`content:figures:check` ✓ · `content:tranche … --fresh --strict-longest --strict-lessons` ✓ (clé la plus
longue 0/12, paires proches 0, patron 0 en recul). Rendu : `renderLesson`/`renderSummary` (vitest jetable)
sur les 3 cours + 3 résumés : 0 `**`, 0 `:::`, 0 `*` résiduel, `<details>` = nombre de `verifie` ; Chromium
360 px : `scrollWidth` = 360 partout (pas de scroll horizontal), tableaux OK. Fichiers jetables supprimés
(`src/__audit_b4_tmp/`).

Toutes les questions de remplacement ci-dessous ont été **validées par `questionSchema`** (zod, vitest
jetable), mesurées (clé jamais strictement la plus longue), re-résolues (une seule réponse), sans renvoi
par lettre. Elles gardent leur place et leur `difficulty` (ids d'option libres de changer en place).

---

## 07-aimants-boussole

**Cours** (8 sections, patron T1→T7 complet dans chacune ; exemples, pièges et vérifications re-résolus :
tous justes ; figures vérifiées : U ouvert, barreau à limaille aux pôles, pôles ش/ج et flèches d'attraction
/ répulsion cohérentes, boussole 5 parties (renvois 1–5 tombent sur la bonne pièce), rose 8 directions
juste). Aimant cassé : la question est au manuel (p.132 « أتعهّد 1 ») — dans le scope. « خفّاف » = terme du
manuel (p.131). « حجم » et « مادّة » de l'aimant : manuel p.131 item 7-2.

### MAJEURS

**M07-1 · `quiz.json` Q4 — question miroir de `01-pratique` Q4** (l'une demande où va le pôle nord, l'autre
comment s'appelle le bout qui va au nord ; le mot « الشماليّ » de l'énoncé donne la clé). Remplacer Q4 par :
```json
{
  "prompt": "وضعنا مغنطًا قضيبيًّا على قطعة خفّاف تطفو فوق ماء في إناء، وطرفاه نحو الشرق والغرب. ماذا يحدث له؟",
  "options": [
    {
      "id": "a",
      "text": "يدور ثمّ يستقرّ وأحد قطبيه نحو الشمال"
    },
    {
      "id": "b",
      "text": "يبقى في الاتّجاه الّذي وضعناه فيه تمامًا"
    },
    {
      "id": "c",
      "text": "يدور حول نفسه دون أن يستقرّ أبدًا"
    },
    {
      "id": "d",
      "text": "يتّجه نحو أقرب جدار من جدران القسم"
    }
  ],
  "correctOption": "a",
  "difficulty": 2,
  "explanation": "المغنط الطافي على الخفّاف حرّ الحركة، فيدور ثمّ يستقرّ وأحد قطبيه نحو الشمال، وهو قطبه الشماليّ «ش». لا يبقى كما وضعناه لأنّه حرّ الدوران، ولا يدور بلا توقّف، ولا تجذبه الجدران لأنّها ليست موادّ حديديّة."
}
```
**M07-2 · `exercices/01-pratique.json` Q1 — redonne le `::: verifie` de la section 1** (mêmes deux
mélanges « رمل وبراغٍ من حديد » / « حبوب قمح وزوان », même clé ; et encore une fois dans `03-revision` Q7).
Remplacer par :
```json
{
  "prompt": "أيّ هذه الخلائط نستطيع أن نفصل مكوّنيه بالمغنط؟",
  "options": [
    {
      "id": "a",
      "text": "ملح وسكّر"
    },
    {
      "id": "b",
      "text": "دقيق وحبوب عدس"
    },
    {
      "id": "c",
      "text": "رمل وقطع صغيرة من الزجاج"
    },
    {
      "id": "d",
      "text": "أرز ومشابك ورق حديديّة"
    }
  ],
  "correctOption": "d",
  "difficulty": 1,
  "explanation": "مشابك الورق الحديديّة تنجذب إلى المغنط ويبقى الأرزّ في مكانه، فينفصل الخليط. أمّا الخلائط الأخرى فليس فيها أيّ مادّة حديديّة، فلا يجذب المغنط منها شيئًا."
}
```
**M07-3 · `exercices/02-boss.json` Q6 — redonne l'`::: exemple` « العمّ الهادي »** (face au nord, l'ouest est
à gauche). Remplacer par une lecture de boussole **dont le nord n'est pas en haut** (ce que le concours
demande, PLAN-gisement « le nord déplacé ») ; figure rendue et vérifiée (aiguille rouge vers 4 ⇒ 4 = N,
2 = S, 1 = O, 3 = E) :
```json
{
  "prompt": "في هذه البوصلة المستقرّة، يتّجه طرف الإبرة الأحمر نحو الشمال. أيّ رقم يقع في جهة الغرب؟ <svg viewBox=\"0 0 100 100\"><circle cx=\"50\" cy=\"50\" r=\"34\" fill=\"#f1f5f9\" stroke=\"currentColor\" stroke-width=\"2.5\"/><polygon points=\"76,50 50,45 50,55\" fill=\"#dc2626\" stroke=\"currentColor\" stroke-width=\"1\"/><polygon points=\"24,50 50,45 50,55\" fill=\"#64748b\" stroke=\"currentColor\" stroke-width=\"1\"/><circle cx=\"50\" cy=\"50\" r=\"2.5\" fill=\"currentColor\"/><g font-size=\"11\" font-weight=\"700\" fill=\"#0f172a\" text-anchor=\"middle\"><text x=\"50\" y=\"12\">1</text><text x=\"8\" y=\"54\">2</text><text x=\"50\" y=\"97\">3</text><text x=\"92\" y=\"54\">4</text></g></svg>",
  "options": [
    {
      "id": "a",
      "text": "الرقم 1"
    },
    {
      "id": "b",
      "text": "الرقم 2"
    },
    {
      "id": "c",
      "text": "الرقم 3"
    },
    {
      "id": "d",
      "text": "الرقم 4"
    }
  ],
  "correctOption": "a",
  "difficulty": 3,
  "explanation": "الطرف الأحمر يتّجه نحو الرقم 4، فالرقم 4 هو الشمال والرقم 2 المقابل له هو الجنوب. ومن يواجه الشمال يجد الشرق عن يمينه والغرب عن يساره: إذا أدرنا الرسم حتّى يصير الرقم 4 في الأعلى، صار الرقم 1 عن اليسار فهو الغرب، والرقم 3 عن اليمين فهو الشرق. الخطأ الشائع أن نحسب الغرب في أعلى الرسم أو عن يساره دائمًا، والشمال هنا ليس في الأعلى."
}
```
**M07-4 · `exercices/03-revision.json` Q5 — copie mot pour mot du `::: verifie` de la section 3**
(« ثبّتت مريم ورقة على باب الثلّاجة… »). Remplacer par :
```json
{
  "prompt": "وضعنا مسمارًا حديديًّا داخل كأس من الزجاج، ثمّ قرّبنا مغنطًا من جدار الكأس من الخارج. ماذا يحدث للمسمار؟",
  "options": [
    {
      "id": "a",
      "text": "يتحرّك نحو المغنط عبر الزجاج"
    },
    {
      "id": "b",
      "text": "لا يتحرّك، فالزجاج يقطع تأثير المغنط",
      "misconceptionTag": "eveil.aim.attire-seulement-au-contact"
    },
    {
      "id": "c",
      "text": "يبتعد عن المغنط نحو الجهة الأخرى"
    },
    {
      "id": "d",
      "text": "ينجذب الكأس كلّه ومعه المسمار"
    }
  ],
  "correctOption": "a",
  "difficulty": 2,
  "explanation": "المغنط يجذب عن بعد، ويؤثّر عبر الموادّ الرقيقة الّتي لا تنجذب إليه كالزجاج؛ فيتحرّك المسمار الحديديّ نحوه. الزجاج نفسه لا ينجذب، والمسمار العاديّ لا يبتعد عن المغنط: التنافر لا يحدث إلّا بين مغنطين."
}
```
**M07-5 · `exercices/04-defi.json` Q3 — redonne l'`::: exemple` « نعيّن قطبي إبرة ممغنطة بمغنط معروف
القطبين »** (ش approché, le bout s'éloigne ⇒ ش). Remplacer par la version à deux étapes :
```json
{
  "prompt": "قرّبت سلمى القطب الجنوبيّ (ج) لمغنط من طرفي إبرة ممغنطة، واحدًا بعد الآخر: جذب الطرفَ الأوّل ودفع الطرفَ الثاني. ما الطرف الأوّل؟",
  "options": [
    {
      "id": "a",
      "text": "قطبها الجنوبيّ (ج)",
      "misconceptionTag": "eveil.aim.poles-identiques-s-attirent"
    },
    {
      "id": "b",
      "text": "قطبها الشماليّ (ش)"
    },
    {
      "id": "c",
      "text": "طرف غير ممغنط منها"
    },
    {
      "id": "d",
      "text": "لا يُعرف إلّا بتعليقها"
    }
  ],
  "correctOption": "b",
  "difficulty": 3,
  "explanation": "الطرف الثاني ابتعد عن «ج»: هذا تنافر، والتنافر لا يحدث إلّا بين قطبين متماثلين، فالطرف الثاني «ج». وللإبرة الممغنطة قطبان مختلفان، فالطرف الأوّل «ش»، ولذلك جذبه «ج»: المختلفان يتجاذبان. الخطأ الشائع أن نظنّ أنّ الطرف الّذي انجذب إلى «ج» هو «ج» مثله."
}
```
**M07-6 · piège sans étiquette** — le `::: piege` « الشرق عن اليسار والغرب عن اليمين… » (section 🌹) ne
correspond à aucun id de `coursePitfalls`/du registre (course-quality : « classic mistake with no registry
tag » = majeur). Créer `eveil.aim.est-ouest-inverses` (libellé ar de l'auteur, à compléter fr/en), le
déclarer dans `coursePitfalls` et le poser sur : quiz Q6 option « ج ق », 03-revision Q8 option « الرقم 6 »,
et sur l'option « الرقم 3 » de la nouvelle 02-boss Q6.

### MINEURS
- `01-pratique` Q8 (`short_answer` « القطبان ») : `acceptedAnswers` incomplets → `["قطبا المغنط", "القطبين", "قطبين", "قطبان", "قطبا المغناطيس"]`. L'explication ne contient pas la réponse ✓ ; sa dernière phrase est fausse dans les mots (« وهما اسمان نميّز بهما جهتين ») → remplacer par « وأحدهما يتّجه نحو الشمال والآخر نحو الجنوب إذا تُرك المغنط حرّ الحركة. ».
- `03-revision` Q8 et `05-entrainement` Q9 : même figure numérotée, même fait (4 = ج ق) — doublon de fait ; acceptable dans une révision, à varier si l'on retouche.
- `04-defi` Q6 (pourquoi le خفّاف) redonne l'étape 1 de l'exemple « بوصلة سلمى » — tolérable (une étape, pas l'exemple).
- `03-revision` Q7 (reprise p.127 5-أ) : le manuel écrit « خليط من الحبوب والزّوان (أو التّوابل) » ; « (أو التّوابل) » omis — sans effet sur la clé.
- Notation de l'Est : le cours choisit « ق » ; le guide p.176 imprime « شـ », le manuel p.134 laisse des blancs, et l'arbitrage V5 ne fixe **pas** de lettre (contrairement à ce que dit le rapport auteur). Choix défendable (usage scolaire courant ش/ج/ق/غ) ; à confirmer sur une session de concours.
- `quiz` Q6 : explication qui mélange «ج» et (غ) — homogénéiser les guillemets.

---

## 11-effets-courant-electrique

**Cours** (7 sections ; exemples, pièges et vérifications re-résolus : justes ; figures : circuit fermé
cohérent, électrolyse juste — tube de gauche ≈ 2× plus de gaz, relié au −, électroaimant juste).
« القرافيت » = graphie du manuel (p.123). V3 ✓. V1 ✓ (« للاستزادة » 2 : 1).

### MAJEURS

**M11-1 · E-7b non appliqué : la sonnette électrique est absente** (grep « جرس » : 0). Texte complet fourni
au § E-7b ci-dessous (section de cours + figure + puce de résumé + 2 questions).

**M11-2 · `exercices/02-boss.json` Q4 = le `::: verifie` de la section 🫧** (pile sans étiquette, tube le plus
rempli ⇒ quel pôle) — les deux reprennent le manuel p.125 item 7. Garder Q4 (reprise) et **remplacer le
`::: verifie`** de la section « 🫧 التأثير الكيميائيّ » par :

```markdown
::: verifie
في المحلال، جمع الأنبوب الأيسر غازًا أقلّ من الأيمن. ما الغاز في الأنبوب الأيسر؟ وبأيّ قطب يتّصل قضيبه؟

---

هو الأكسيجين، وقضيبه موصول بالقطب الموجب (+)، لأنّ الغاز الأصغر حجمًا هو الأكسيجين، والأكسيجين
يتصاعد عند المصعد الموصول بالقطب الموجب.
:::
```

Et, dans Q4, l'énoncé ne demande que le pôle alors que les options portent pôle + raison (l'option d a le
bon pôle) : ajouter « ، ولماذا؟ » → `… بأيّ قطب يتّصل القضيب تحت الأنبوب 1، ولماذا؟ <svg…>`.

**M11-3 · `exercices/04-defi.json` Q4 = l'`::: exemple` « نسمّي وجهي الوشيعة »** (le nord de l'aiguille
attiré ⇒ face sud). Remplacer par la version répulsion :
```json
{
  "prompt": "قرّبنا القطب الجنوبيّ لإبرة ممغنطة من أحد وجهي وشيعة يجتازها تيّار، فابتعد عنه. ما هذا الوجه، ولماذا؟",
  "options": [
    {
      "id": "a",
      "text": "وجه شماليّ لأنّ المختلفين يتنافران",
      "misconceptionTag": "eveil.aim.poles-identiques-s-attirent"
    },
    {
      "id": "b",
      "text": "لا نعرفه لأنّ الإبرة لم تلمس الوشيعة",
      "misconceptionTag": "eveil.aim.attire-seulement-au-contact"
    },
    {
      "id": "c",
      "text": "وجه جنوبيّ لأنّ المتماثلين يتنافران"
    },
    {
      "id": "d",
      "text": "لا وجه له لأنّ الوشيعة ليست مغنطًا"
    }
  ],
  "correctOption": "c",
  "difficulty": 3,
  "explanation": "ابتعد القطب الجنوبيّ للإبرة عن الوجه: هذا تنافر، والتنافر لا يحدث إلّا بين قطبين متماثلين، فالوجه جنوبيّ ✓. والوشيعة الّتي يجتازها تيّار تماثل مغنطًا بوجهين، وتؤثّر في الإبرة عن بعد دون أن تلمسها. الخطأ الشائع أن نعكس القاعدة فنقول إنّ المختلفين يتنافران."
}
```
**M11-4 · `exercices/02-boss.json` Q6 (reprise p.138 6-3) — données non fidèles et figure qui confond deux
facteurs.** Le manuel parle de **مسامير** (pas de دبابيس) et dessine deux **bobines sans noyau** ; la figure
ajoute deux noyaux gris de longueurs différentes (96 et 48), si bien que la bobine (1) diffère par ses spires
**et** par son noyau — or l'explication dit « le seul écart est le nombre de spires ». Corrections exactes :
- dans `prompt`, supprimer les deux chaînes
  `<rect x="62" y="134" width="96" height="12" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>` et
  `<rect x="202" y="134" width="48" height="12" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>` ;
- dans `prompt` : « وقد قرّبنا الوشيعتين من دبابيس. جذبت الوشيعة (1) عددًا أكبر من الدبابيس. » →
  « وقد قرّبنا الوشيعتين من مسامير صغيرة. جذبت الوشيعة (1) عددًا أكبر من المسامير. » ;
- dans `explanation` : « فتجذب دبابيس أكثر » → « فتجذب مسامير أكثر ».

**M11-5 · pièges sans étiquette** : « لا يضيء المصباح إلّا بوجود خليّة » (section 🔌, conception n° 6 du guide
p.31), et « قارنتُ وشيعة بـ 10 لفّات وخليّة… » (section 💪). Créer `eveil.elec.lampe-seulement-avec-cellule`
et `eveil.elec.deux-facteurs-a-la-fois` (libellés ar de l'auteur), les déclarer dans `coursePitfalls`, les
poser sur 04-defi Q7 option « خليّة مخفيّة داخل المصباح تدفع التيّار » et 02-boss Q8 option « وشيعة بـ 10
لفّات وخليّة، ثمّ وشيعة بـ 20 لفّة وخليّتين ». (La phrase « الضوء ≠ التيّار » du piège 🔥 peut rester sous
l'étiquette existante `eveil.elec.lampe-ne-chauffe-pas` ; `eveil.elec.lumiere-egale-courant` est optionnel.)

### MINEURS
- `02-boss` Q7 : « رتّب ما يحدث في **هذه** الدارة » sans figure (renvoi à un objet absent) → « رتّب ما يحدث في دارة المغنط الكهربائيّ، من البداية: ».
- `03-revision` Q1 : l'explication commente « الوشيعة », qui n'est pas une option, et ne dit rien des distracteurs → « المغنط الكهربائيّ يسمّى أيضًا الكهرمغناطيس. البوصلة إبرة ممغنطة، والمحلال إناء لتحليل الماء، والمغنط الدائم يبقى مغنطًا دون تيّار، بخلاف المغنط الكهربائيّ المؤقّت. »
- `05-entrainement` Q7 (`short_answer` « الحلكبة ») : `acceptedAnswers` → `["حلكبة الماء", "حلكبة", "التحليل الكهربائيّ", "التحليل الكهربائيّ للماء"]` (synonymes exacts).
- `01-pratique` Q8 (« المحلال ») : ajouter « محلال كهربائيّ ».
- `04-defi` Q7 (dynamo) : redonne le scénario du piège 🔌 et porte une clé sur un contenu ◐ (manuel p.139, lecture) ; gardé parce qu'il est le seul distracteur de la conception n° 6 — à étiqueter (M11-5).
- `> 🏆` final : « المغنط الكهربائيّ يفتح لك الطريق إلى عالم المغانط والبوصلة » — faux dans l'ordre (07 = displayOrder 10 est AVANT 11 ; le suivant est 08-poids). Remplacement au § E-7b.
- `02-boss` : `manuel.items` ne cite que p.138 6-3 alors que Q4 reprend p.125 item 7 (pile sans enveloppe) ; soit ajouter `"أقيّم تعلّمي الجديد 7 (ص 125)"` et `pages: "125, 138"`, soit considérer Q4 comme variante.

---

## 08-poids

**Cours** (6 sections au patron ; exemples, pièges, vérifications re-résolus : justes — 2 kg − 500 g =
1,5 kg ✓ ; dynamomètre lu à 15 N ✓ ; récipient incliné : côtés ⟂ fond (produit scalaire ≈ 0), surface
horizontale, fil vertical, angle droit ✓). V1 ✓ (1/6 en « للاستزادة »). Reprises p.144 6-1 (4 dessins,
dont la « مركبة فضائيّة » du manuel) et p.145 8 (tableau) : données conformes au PDF.

### MAJEURS

**M08-1 · figures du cours illisibles en RTL** (rendu Chromium, `dir="rtl"`, vérifié à 360 px) : les 13
étiquettes `text-anchor="start"` des trois figures (« الدّيناموتر », « المؤشّر », « كيس برتقال », « مسمار »,
« خيط », « حجر », « منحى شاقوليّ », « من أعلى إلى أسفل », « قطعة طباشير », « 90° », « سطح الماء أفقيّ »,
« خيط المطمار », « إناء مائل ») s'ancrent par leur bord **droit** et chevauchent le dessin (« حجر » sur la
pierre, « كيس برتقال » sur l'orange, « سطح الماء… » et « إناء مائل » coupés au bord) — règle 3 de
`course-figures.md`. Correction **vérifiée au rendu** : dans `cours.md`, remplacer chacune des 13
occurrences ` text-anchor="start"` par ` text-anchor="start" direction="ltr"`, et chacune des 5
occurrences ` text-anchor="end"` par ` text-anchor="end" direction="ltr"` (graduations 0–20 du
dynamomètre, qui mordent sur les traits). Même correction dans `exercices/01-pratique.json` Q6 (5
` text-anchor="end"` des graduations : « 10 », « 15 », « 20 » mordent sur le tube — c'est la lecture
demandée).

**M08-2 · quiz Q5 = le `::: verifie` de la section 🌋** (« رمى كريم كرة إلى أعلى… لماذا عادت؟ » / « رمى
أحمد حجرًا… لماذا عاد؟ »). Garder la question, **remplacer le `::: verifie`** par un jumeau de l'exemple
(lecture du dynamomètre) :

```markdown
::: verifie
علّقت سلمى محفظتها في طرف الدّيناموتر، فتوقّف المؤشّر عند التدريجة 20. ما وزن المحفظة؟ ولماذا لا نكتبه
بالكيلوغرام؟

---

وزن المحفظة 20 N: اللّولب استطال حتّى وازن جذب الأرض للمحفظة، والمؤشّر يقف عند وزنها. ولا نكتبه
بالكيلوغرام، لأنّ الوزن قوّة ووحدة قيسه النّيوتن؛ أمّا الكيلوغرام فوحدة الكتلة.
:::
```

**M08-3 · `01-pratique` Q5 = le `::: piege` (pâte à modeler 200 g → serpent).** Remplacer par :
```json
{
  "prompt": "ورقة ألمنيوم كتلتها 50 g، كوّرها سامي فصارت كرة صغيرة. ما كتلة الكرة؟",
  "options": [
    {
      "id": "a",
      "text": "أكثر من 50 g",
      "misconceptionTag": "eveil.poids.masse-change-avec-forme-ou-etat"
    },
    {
      "id": "b",
      "text": "أقلّ من 50 g",
      "misconceptionTag": "eveil.poids.masse-change-avec-forme-ou-etat"
    },
    {
      "id": "c",
      "text": "50 g"
    },
    {
      "id": "d",
      "text": "100 g",
      "misconceptionTag": "eveil.poids.masse-change-avec-forme-ou-etat"
    }
  ],
  "correctOption": "c",
  "difficulty": 2,
  "explanation": "لم يُضف سامي إلى الورقة شيئًا ولم ينزع منها شيئًا، والكتلة لا تتغيّر بتغيّر شكل الجسم؛ فكتلة الكرة 50 g. صِغر الكرة يوهمنا بأنّ كتلتها نقصت."
}
```
**M08-4 · `02-boss` Q2 = l'`::: exemple` (tomates, 2 kg, 500 g, 1,5 kg).** Remplacer par :
```json
{
  "prompt": "في الكفّة الأولى من ميزان ذي كفّتين عياران: 1 kg و500 g. وضع البائع في الكفّة الثانية الجزر ومعه عيار 200 g، فتوازنت الكفّتان. ما كتلة الجزر؟",
  "options": [
    {
      "id": "a",
      "text": "1 kg"
    },
    {
      "id": "b",
      "text": "1,3 kg"
    },
    {
      "id": "c",
      "text": "1,5 kg"
    },
    {
      "id": "d",
      "text": "1,7 kg"
    }
  ],
  "correctOption": "b",
  "difficulty": 2,
  "explanation": "توازن الكفّتين يعني أنّ الكتلة فيهما متساوية: في الكفّة الأولى 1 kg + 500 g = 1500 g، وفي الثانية كتلة الجزر + 200 g. إذن كتلة الجزر 1500 g − 200 g = 1300 g = 1,3 kg. من يجمع العيار الصغير بدل أن يطرحه يجد 1,7 kg، ومن ينساه يجد 1,5 kg، ومن ينسى عيار 500 g يجد 1 kg."
}
```
**M08-5 · `02-boss` Q3 = la question d'ancrage résolue par l'exemple (étape 4).** Remplacer par :
```json
{
  "prompt": "في الميزان الرّومانيّ، ماذا نفعل بعد تعليق الجسم حتّى نقرأ كتلته؟",
  "options": [
    {
      "id": "a",
      "text": "نزلق العيار على الذراع"
    },
    {
      "id": "b",
      "text": "نضع عيارات في كفّة ثانية"
    },
    {
      "id": "c",
      "text": "نقرأ كتلته على الشاشة"
    },
    {
      "id": "d",
      "text": "ننتظر حتّى يستطيل اللّولب",
      "misconceptionTag": "eveil.poids.masse-et-poids-confondus"
    }
  ],
  "correctOption": "a",
  "difficulty": 2,
  "explanation": "في الميزان الرّومانيّ نعلّق الجسم ثمّ نزلق عيارًا على ذراع مدرّجة حتّى تستوي الذراع، فنقرأ الكتلة على التدريجة. العيارات في كفّة ثانية للميزان ذي الكفّتين، والشاشة للميزان الإلكترونيّ، واللّولب الّذي يستطيل للدّيناموتر الّذي يقيس الوزن لا الكتلة."
}
```
**M08-6 · `02-boss` Q8 (reprise p.144 6-1) — deux distracteurs éliminés à l'œil** : « سهم من أسفل إلى
أعلى » et « المسار أفقيًّا » sont démentis par la figure (toutes les flèches descendent, aucune n'est
horizontale) ; la question se réduit à deux options. Énoncé et figure inchangés, options et explication :
```json
{
  "prompt": "(énoncé et figure inchangés)",
  "options": [
    {
      "id": "a",
      "text": "رسم المسار مائلًا بدل الخطّ الشاقوليّ"
    },
    {
      "id": "b",
      "text": "رسم المسار مستقيمًا بدل خطّ منحنٍ",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    },
    {
      "id": "c",
      "text": "رسم الأجسام الخفيفة تسقط وهي بلا وزن",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "d",
      "text": "رسم المسار قليل الميل والصواب أن يميل أكثر",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    }
  ],
  "correctOption": "a",
  "difficulty": 3,
  "explanation": "في الرسوم الأربعة رسم أحمد مسار الجسم خطًّا مائلًا. والصواب أنّ الجسم في سقوط حرّ ينزل بفعل وزنه في خطّ مستقيم شاقوليّ من أعلى إلى أسفل، تحت المكان الّذي تُرك فيه مباشرة: لا منحنيًا ولا أكثر ميلًا. والأجسام كلّها، خفيفة أو ثقيلة، لها وزن، فهي تسقط."
}
```
**M08-7 · `03-revision` Q2 = le `::: verifie` de la section ⚖️** (glaçon en sac fermé qui fond). Remplacer par :
```json
{
  "prompt": "أذبنا في وعاء مغلق قطعة شمع كتلتها 100 g، ثمّ تركناها تبرد فتجمّدت في شكل الوعاء. ما كتلة الشمع الآن؟",
  "options": [
    {
      "id": "a",
      "text": "أقلّ من 100 g",
      "misconceptionTag": "eveil.poids.masse-change-avec-forme-ou-etat"
    },
    {
      "id": "b",
      "text": "أكثر من 100 g",
      "misconceptionTag": "eveil.poids.masse-change-avec-forme-ou-etat"
    },
    {
      "id": "c",
      "text": "100 g"
    },
    {
      "id": "d",
      "text": "0 g"
    }
  ],
  "correctOption": "c",
  "difficulty": 2,
  "explanation": "تغيّرت حالة الشمع (صلب ثمّ سائل ثمّ صلب) وتغيّر شكله، لكنّ الوعاء مغلق فلم يُضف إليه شيء ولم يخرج منه شيء، والكتلة لا تتغيّر بتغيّر الحالة أو الشكل؛ فكتلة الشمع 100 g."
}
```
**M08-8 · `03-revision` Q5 = l'`::: exemple` (pierre au-dessus de la craie, fil brûlé).** Remplacer par :
```json
{
  "prompt": "صنبور يقطر فوق حوض، والهواء ساكن. أين تسقط كلّ قطرة؟",
  "options": [
    {
      "id": "a",
      "text": "بعيدًا عن الصنبور، في خطّ مائل",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    },
    {
      "id": "b",
      "text": "تحت الصنبور مباشرة"
    },
    {
      "id": "c",
      "text": "في خطّ متعرّج حول الصنبور"
    },
    {
      "id": "d",
      "text": "تبقى معلّقة لأنّها خفيفة جدًّا",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    }
  ],
  "correctOption": "b",
  "difficulty": 2,
  "explanation": "القطرة الّتي تنفصل عن الصنبور في سقوط حرّ: تنزل بفعل وزنها في المنحى الشاقوليّ، من أعلى إلى أسفل، فتقع تحت الصنبور مباشرة. والقطرة الخفيفة لها وزن أيضًا، فتسقط."
}
```
**M08-9 · `04-defi` Q1 = le `::: verifie` de la section 🆚, mot pour mot** (« على كيس سكّر كُتب «1 kg» »).
Remplacer par :
```json
{
  "prompt": "علّق سامي جسمًا في الدّيناموتر فأشار إلى 30 N، ثمّ وضعه على ميزان إلكترونيّ فبيّن 3 kg. أيّ العددين يدلّ على كتلة الجسم؟",
  "options": [
    {
      "id": "a",
      "text": "3 kg، لأنّ الميزان يقيس الكتلة"
    },
    {
      "id": "b",
      "text": "30 N، لأنّ الدّيناموتر يقيس الكتلة",
      "misconceptionTag": "eveil.poids.masse-et-poids-confondus"
    },
    {
      "id": "c",
      "text": "العددان معًا، فهما اسمان لمقدار واحد",
      "misconceptionTag": "eveil.poids.masse-et-poids-confondus"
    },
    {
      "id": "d",
      "text": "30 N، لأنّه العدد الأكبر"
    }
  ],
  "correctOption": "a",
  "difficulty": 2,
  "explanation": "الميزان يقيس الكتلة ووحدتها الكيلوغرام، فكتلة الجسم 3 kg. أمّا الدّيناموتر فمقياس القوّة: يقيس الوزن، فوزن الجسم 30 N. الكتلة والوزن مقداران مختلفان، لكلّ منهما أداته ووحدته."
}
```
**M08-10 · `04-defi` Q2 = le `::: verifie` de la section 🌙, mot pour mot** (grimpeur, sac 2 kg).
Remplacer par (contexte du manuel p.144 item 7, sans la mécanique orbitale) :
```json
{
  "prompt": "يحمل صاروخ قمرًا صناعيًّا كتلته 100 kg ويبتعد به عن الأرض. ماذا يحدث لكتلة القمر الصناعيّ ووزنه كلّما ابتعد؟",
  "options": [
    {
      "id": "a",
      "text": "تصغر كتلته ويبقى وزنه كما هو",
      "misconceptionTag": "eveil.poids.masse-change-avec-le-lieu"
    },
    {
      "id": "b",
      "text": "تبقى كتلته ووزنه كما كانا تمامًا"
    },
    {
      "id": "c",
      "text": "تبقى كتلته 100 kg ويصغر وزنه"
    },
    {
      "id": "d",
      "text": "تكبر كتلته ووزنه لأنّه يرتفع"
    }
  ],
  "correctOption": "c",
  "difficulty": 3,
  "explanation": "الكتلة لا تتغيّر بتغيّر المكان، فتبقى 100 kg. والوزن ينقص كلّما ابتعد الجسم عن مركز الأرض، فيصغر وزن القمر الصناعيّ كلّما ابتعد. الخطأ أن نقلب الدورين فنجعل الكتلة هي الّتي تتغيّر."
}
```
**M08-11 · `04-defi` Q3 = le `::: verifie` de la section ⬇️** (ريم lâche une balle du balcon).
Remplacer par :
```json
{
  "prompt": "أفلت سامي حصاة وهو واقف على جسر فوق نهر هادئ، فرسم مسارها خطًّا مائلًا نحو الماء. ما الرسم الصحيح؟",
  "options": [
    {
      "id": "a",
      "text": "خطّ مائل أكثر نحو الأمام",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    },
    {
      "id": "b",
      "text": "خطّ أفقيّ أوّلًا ثمّ نزول شاقوليّ"
    },
    {
      "id": "c",
      "text": "خطّ منحنٍ يبتعد عن الجسر",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    },
    {
      "id": "d",
      "text": "خطّ شاقوليّ من يده إلى الماء"
    }
  ],
  "correctOption": "d",
  "difficulty": 3,
  "explanation": "الحصاة في سقوط حرّ، تنزل بفعل وزنها، والوزن منحاه شاقوليّ واتّجاهه من أعلى إلى أسفل؛ فمسارها خطّ مستقيم شاقوليّ تحت يده مباشرة حتّى سطح الماء. كلّ مسار مائل أو منحنٍ هو خطأ سامي نفسه."
}
```
**M08-12 · `04-defi` Q4 doublonne `01-pratique` Q4** (pourquoi la lave retombe ⇒ son poids, même clé).
Remplacer `04-defi` Q4 par :
```json
{
  "prompt": "قذف لاعب كرة إلى أعلى، فتوقّفت لحظة في أعلى مسارها ثمّ نزلت. هل للكرة وزن في تلك اللحظة؟",
  "options": [
    {
      "id": "a",
      "text": "نعم، فالأرض تجذبها في كلّ مكان"
    },
    {
      "id": "b",
      "text": "لا، فوزنها ينعدم حين تتوقّف",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "c",
      "text": "لا، فالوزن لا يظهر إلّا حين تسقط",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "d",
      "text": "نعم، لكنّه يتّجه إلى أعلى ما دامت تصعد"
    }
  ],
  "correctOption": "a",
  "difficulty": 3,
  "explanation": "لكلّ جسم بجوار الأرض وزن، في كلّ لحظة ✓: الأرض تجذب الكرة وهي تصعد، وحين تتوقّف، وحين تنزل، ولذلك تعود إلى الأرض. ووزنها منحاه شاقوليّ واتّجاهه دائمًا من أعلى إلى أسفل، حتّى حين تصعد."
}
```
**M08-13 · `04-defi` Q6 = le `::: verifie` de la section 📐, mot pour mot** (trois vases, un droit, deux
inclinés). Remplacer par :
```json
{
  "prompt": "وضع سامي قارورة شفّافة فيها ماء على جنبها فوق طاولة مائلة، وانتظر حتّى سكن الماء. كيف يكون سطح الماء داخلها؟",
  "options": [
    {
      "id": "a",
      "text": "أفقيًّا رغم ميلان الطاولة"
    },
    {
      "id": "b",
      "text": "مائلًا مثل ميلان الطاولة",
      "misconceptionTag": "eveil.poids.surface-eau-suit-le-recipient"
    },
    {
      "id": "c",
      "text": "موازيًا لجدار القارورة",
      "misconceptionTag": "eveil.poids.surface-eau-suit-le-recipient"
    },
    {
      "id": "d",
      "text": "شاقوليًّا من أعلى إلى أسفل"
    }
  ],
  "correctOption": "a",
  "difficulty": 3,
  "explanation": "سطح الماء الرّاكد يبقى أفقيًّا مهما مال الإناء أو الطاولة ✓، ويصنع مع خيط المطمار زاوية قائمة. الماء يأخذ شكل القارورة من جوانبها، لكنّ سطحه لا يميل معها. الشاقوليّ منحى خيط المطمار، لا منحى سطح الماء."
}
```
**M08-14 · `05-entrainement` Q4, Q5, Q6 redonnent le cours** : Q4 cite le `::: piege` 🌋 mot pour mot
(« الحجر يسقط لأنّه ثقيل… ») ; Q5 = étape 1 de l'`::: exemple` 🌙 (150 kg) ; Q6 = le cas limite de la
`::: propriete` 🌋 (livre sur la table). Remplacer respectivement par :
Q4 :
```json
{
  "prompt": "قالت مريم: «ريشة العصفور لا وزن لها لأنّها خفيفة جدًّا». ما الصواب؟",
  "options": [
    {
      "id": "a",
      "text": "صدقت، فالأجسام الخفيفة لا وزن لها",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "b",
      "text": "للريشة وزن، فالأرض تجذب كلّ جسم"
    },
    {
      "id": "c",
      "text": "لها وزن ما دامت على جسم العصفور",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "d",
      "text": "لا وزن لها لأنّها تطير في الهواء",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    }
  ],
  "correctOption": "b",
  "difficulty": 3,
  "explanation": "الأرض تجذب كلّ جسم بجوارها، خفيفًا أو ثقيلًا، حيًّا أو غير حيّ؛ فللريشة وزن صغير، ولذلك تنزل في النهاية إلى الأرض ولو تمايلت في الهواء. فكرة مريم تصوّر شائع: الخفّة لا تلغي الوزن."
}
```
Q5 :
```json
{
  "prompt": "جلب رائد فضاء من القمر حجرًا كتلته هناك 3 kg. كم تكون كتلة الحجر على الأرض؟",
  "options": [
    {
      "id": "a",
      "text": "أقلّ من 3 kg",
      "misconceptionTag": "eveil.poids.masse-change-avec-le-lieu"
    },
    {
      "id": "b",
      "text": "3 kg"
    },
    {
      "id": "c",
      "text": "أكثر من 3 kg",
      "misconceptionTag": "eveil.poids.masse-change-avec-le-lieu"
    },
    {
      "id": "d",
      "text": "تتضاعف لأنّ الأرض أكبر",
      "misconceptionTag": "eveil.poids.masse-change-avec-le-lieu"
    }
  ],
  "correctOption": "b",
  "difficulty": 3,
  "explanation": "الكتلة لا تتغيّر بتغيّر المكان: لم يُضف إلى الحجر شيء ولم يُنزع منه شيء، فكتلته على الأرض 3 kg كما كانت على القمر. الّذي يتغيّر هو وزنه: على الأرض يصير أكبر منه على القمر. الخطأ الشائع أن نعطي الكتلة تغيّر الوزن."
}
```
Q6 :
```json
{
  "prompt": "تفّاحة معلّقة بغصنها لا تسقط. هل لها وزن؟",
  "options": [
    {
      "id": "a",
      "text": "لا، لأنّها ساكنة لا تسقط",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "b",
      "text": "لا، لأنّها ما زالت جزءًا من الشجرة",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    },
    {
      "id": "c",
      "text": "نعم، والغصن يمسكها فلا تسقط"
    },
    {
      "id": "d",
      "text": "نعم، لكن حين تنفصل عنه فقط",
      "misconceptionTag": "eveil.poids.certains-objets-sans-poids"
    }
  ],
  "correctOption": "c",
  "difficulty": 3,
  "explanation": "لكلّ جسم بجوار الأرض وزن، حتّى لو لم يسقط: الغصن يمسك التفّاحة فلا تسقط، والأرض تواصل جذبها، ولذلك ينحني الغصن تحت ثقلها. ووزنها موجود قبل أن تنفصل وبعده."
}
```
### MINEURS
- `01-pratique` Q3 (pomme qui tombe) redonne le scénario du `::: piege` ⬇️ et cite « أحمد في رسومه » (personnage inconnu de l'élève hors cours). Remplacement proposé :
```json
{
  "prompt": "انفصلت قطرة ماء عن طرف سقف الدار في يوم بلا ريح. كيف يكون مسارها حتّى الأرض؟",
  "options": [
    {
      "id": "a",
      "text": "خطّ شاقوليّ نحو الأسفل"
    },
    {
      "id": "b",
      "text": "خطّ مائل يبتعد عن الدار",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    },
    {
      "id": "c",
      "text": "خطّ أفقيّ ثمّ نزول"
    },
    {
      "id": "d",
      "text": "خطّ مائل يقترب من الحائط",
      "misconceptionTag": "eveil.poids.chute-en-ligne-oblique"
    }
  ],
  "correctOption": "a",
  "difficulty": 1,
  "explanation": "القطرة في سقوط حرّ، تنزل بفعل وزنها، والوزن منحاه شاقوليّ واتّجاهه من أعلى إلى أسفل؛ فتقع تحت المكان الّذي انفصلت فيه مباشرة. رسم المسار مائلًا هو الخطأ الشائع."
}
```
- `01-pratique` Q8 (`short_answer` « خيط المطمار ») : ajouter « الشاقول », « خيط الشاقول ».
- `02-boss` Q5 (astronaute sur la Lune) = manuel p.144 6-3 et l'exemple 🌙 ; gardé (reprise), mais `manuel.items` ne cite pas 6-3 (ni 6-2 pour Q4) : ajouter `"أطبّق وأوظّف 6-2 (ص 144)"`, `"أطبّق وأوظّف 6-3 (ص 144)"` si ces items sont tenus pour repris.
- Figures du cours : mots arabes dans le dessin (« الدّيناموتر », « منحى شاقوليّ »…) contraires à `course-figures.md` (« a label is a glyph ») — la correction M08-1 suffit au rendu ; les reporter en légende serait mieux.
- Tableau 🆚, ligne « ما هو؟ » : « مقدار مقيس » n'oppose rien (le poids aussi est mesuré) alors que la phrase de pont dit « جواب الكتلة يختلف دائمًا ».
- Le terme « الدّيناموتر » (cours, fiche) et « دينامومتر » (`04-defi` Q7) coexistent ; le manuel p.145 imprime « الدّينامومتر ». Uniformiser sur le terme du cours.

---

## E-7b — la sonnette électrique au ch. `11` (texte VÉRIFIÉ, prêt à coller)

Source relue à l'image : guide 503604 p.175 (« الجرس الكهربائي » : قطعة الحديد (م)، السّاعد (س)، رأس
السّاعد (ر)، الصّحن النحاسي (ص) ; fermeture → (م) s'aimante, attire (س), (ر) frappe (ص), la coupure
ouvre la دارة, (م) perd son aimantation, le ressort ramène, « ضربات متلاحقة »). Notion = **usage de
l'électroaimant**, scope ◐ du guide rendu ✅ par E-7b ; rien n'y est neuf hors du ch. 11 (électroaimant
temporaire, attraction du fer, cuivre non attiré — ch. 07).

**Place** : nouvelle section **entre la section « 💪 ما الّذي يقوّي المغنط الكهربائيّ؟ » (fin au `::: retenir`
« نقوّي المغنط الكهربائيّ… ») et le `> 🏆` final**. Patron : T1 ancrage-question → T3 figure + phrase de pont
→ T4 exemple (lecture du schéma, chaque pas avec son pourquoi) → T7 vérification (jumeau : le relâchement)
→ retenir ; aucun bloc de règle, donc C-1 sans objet ; C-2 (2+ lignes de prose avant tout bloc) ✓, C-3 ✓.
Le `:::` fermant de l'exemple est précédé d'une ligne vide (piège Prettier). ~33 lignes de prose (bande 18–40).

**Figure — vérifiée** : noyau (م) horizontal sous le gong, bobine 9 spires ; le levier (س) à 16 px du bout du
noyau, pivot en bas, ressort qui le tire vers la vis de contact (circuit fermé au repos, bouton ouvert) ;
le marteau (ر) en haut du levier à 8,7 px du bord du gong (centre 158,55 r 36 ; bord à y = 62 : x = 193,3 ;
marteau 202–218) : attiré vers la gauche, il frappe le gong, et le levier quitte la vis ⇒ la دارة s'ouvre —
le schéma dit vrai. Encre sombre en dur, `viewBox` sans `width/height`, étiquettes d'une lettre centrées
(`text-anchor="middle"`, halo), aucune prose arabe dans le dessin. Rendu Chromium `dir="rtl"` à 360 px :
lisible, pas de débord. Aucune des lettres م/س/ر/ص n'est une lettre d'option (أ/ب/ج/د) : pas de faux
« renvoi par lettre ».

### Section de cours (à insérer dans `11-effets-courant-electrique/cours.md`)

````markdown
## 🔔 الجرس الكهربائيّ — مغنط كهربائيّ يدقّ

ضغط ياسين على زرّ جرس الدار فدقّ دقّات متلاحقة، ثمّ رفع إصبعه فسكت. فتح أبوه علبة الجرس فوجد
فيها سلكًا ملفوفًا حول قطعة حديد، وقطعة حديد أخرى في أعلاها رأس صغير قرب صحن من النحاس. كيف
يصنع المغنط الكهربائيّ هذه الدقّات؟

::: figure حين يسري التيّار في الوشيعة تصير الحديدة (م) مغنطًا كهربائيًّا يجذب الساعد (س)، فيضرب رأسه (ر) الصحن النحاسيّ (ص)
<svg viewBox="0 0 340 240">
<circle cx="158" cy="55" r="36" fill="#fbbf24" stroke="#0f172a" stroke-width="2.5"/>
<circle cx="158" cy="55" r="10" fill="#f59e0b" stroke="#0f172a" stroke-width="2"/>
<rect x="70" y="123" width="120" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>
<g fill="none" stroke="#b45309" stroke-width="2.5"><ellipse cx="90" cy="130" rx="4" ry="16"/><ellipse cx="100" cy="130" rx="4" ry="16"/><ellipse cx="110" cy="130" rx="4" ry="16"/><ellipse cx="120" cy="130" rx="4" ry="16"/><ellipse cx="130" cy="130" rx="4" ry="16"/><ellipse cx="140" cy="130" rx="4" ry="16"/><ellipse cx="150" cy="130" rx="4" ry="16"/><ellipse cx="160" cy="130" rx="4" ry="16"/><ellipse cx="170" cy="130" rx="4" ry="16"/></g>
<rect x="206" y="70" width="8" height="120" fill="#64748b" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="210" cy="62" r="8" fill="#475569" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="202,200 218,200 210,190" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>
<polyline points="214,180 218,174 222,186 226,174 230,186 234,174 238,186 242,180 246,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<rect x="246" y="168" width="6" height="24" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>
<rect x="214" y="135" width="26" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.5"/>
<path d="M90 146 V215 H128 M162 215 H230 M170 146 V170 H206 M240 139 H300 V215 H270" fill="none" stroke="#0f172a" stroke-width="2.5"/>
<circle cx="128" cy="215" r="3.5" fill="#0f172a"/><circle cx="162" cy="215" r="3.5" fill="#0f172a"/>
<path d="M124 205 H166 M145 205 V193" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<rect x="230" y="203" width="40" height="24" fill="#f59e0b" stroke="#0f172a" stroke-width="2"/>
<g font-size="16" font-weight="700" fill="#0f172a" text-anchor="middle"><text x="241" y="221">−</text><text x="259" y="221">+</text></g>
<g font-size="16" font-weight="700" fill="#0f172a" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="158" y="36">ص</text><text x="232" y="56">ر</text><text x="232" y="112">س</text><text x="56" y="135">م</text></g>
</svg>
:::

في الرسم، الوشيعة الملفوفة حول الحديدة (م) هي المغنط الكهربائيّ. والساعد (س) قطعة حديد يشدّها
نابض فتلمس نقطة التماسّ، وفي أعلاه الرأس (ر) قرب الصحن (ص). والزرّ في أسفل الرسم قاطعة: حين
نضغط عليه تنغلق الدارة.

::: exemple نقرأ رسم الجرس

1. نضغط على الزرّ فيسري التيّار في الوشيعة — لأنّ الزرّ قاطعة تغلق الدارة.
2. تصير الحديدة (م) مغنطًا كهربائيًّا فتجذب الساعد (س) — لأنّ الساعد من حديد، والمغنط يجذب
   الموادّ الحديديّة.
3. يضرب الرأس (ر) الصحن (ص) فنسمع دقّة — لأنّ الرأس مثبّت في أعلى الساعد الّذي انجذب.
4. حين ينجذب الساعد يبتعد عن نقطة التماسّ فتنفتح الدارة، فتفقد (م) مغنطتها ويُرجع النابض الساعد
   فتنغلق الدارة من جديد — لأنّ المغنط الكهربائيّ مؤقّت؛ وهكذا تتلاحق الدقّات ما دام الإصبع على
   الزرّ.

:::

::: verifie
رفع ياسين إصبعه عن الزرّ فسكت الجرس. لماذا؟

---

لأنّ الزرّ لم يعد يغلق الدارة، فلا يسري التيّار في الوشيعة، فلا تبقى الحديدة (م) مغنطًا: المغنط
الكهربائيّ مؤقّت. فلا يُجذب الساعد (س)، ولا يضرب الرأس (ر) الصحن (ص).
:::

::: retenir
الجرس الكهربائيّ يستعمل مغنطًا كهربائيًّا يجذب ساعدًا من حديد فيضرب رأسُه الصحن، ما دام التيّار يسري.
:::
````

### `> 🏆` final (remplace les deux lignes actuelles)

```markdown
> 🏆 عبرتَ بوّابة التيّار: صرت تعرف آثاره الثلاثة، الحراريّ والكيميائيّ والمغناطيسيّ، وتركّب لكلّ
> منها دارته، وتقرأ رسم الجرس الكهربائيّ. وفي الفصل القادم: وزن الأجسام والسّقوط الحرّ.
```

### Puce de résumé (ajouter en dernière ligne de `resume.md`, bijection section ↔ puce)

```markdown
- **الجرس الكهربائيّ**: نضغط الزرّ فيسري التيّار في الوشيعة، فتصير الحديدة داخلها مغنطًا كهربائيًّا يجذب الساعد الحديديّ، فيضرب رأسه الصحن النحاسيّ؛ وحين ينجذب الساعد تنفتح الدارة لحظة ويُرجعه النابض، فتتلاحق الدقّات ما دام الإصبع على الزرّ.
```

`chapter.json` → `description` : ajouter « ؛ الجرس الكهربائيّ (قراءة رسم) » en fin de chaîne (les
`sources[]` citent déjà le guide « ص 170–175 »).

Rendu vérifié (vitest jetable, `renderLesson`/`renderSummary`, ar) : la section produit 1 figure numérotée
(« الشكل 4 »), 1 `<details>`, 0 `**`/`:::` résiduel ; le résumé 8 cartes.

### Deux questions de lecture de schéma — `exercices/05-entrainement.json`, **ajoutées en fin de fichier** (Q8, Q9), `difficulty` 3

Place choisie : le fichier de révision `boss` du chapitre, dont le maximum est 3 → rampe non décroissante,
ids existants intacts. Les deux questions font **lire** le schéma (numéros neutres, attribution différente
d'une figure à l'autre et de celle du cours, pour qu'aucune ne donne la clé de l'autre) ; aucune ne
demande de réciter le cycle. Pas de champ `manuel` (variante du guide, pas du manuel). Re-résolues :
Q8 = seul le n° 2 est entouré de spires ; Q9 = le n° 1 est le levier, un levier en cuivre n'est pas attiré ⇒
pas de son (le circuit reste fermé par le cuivre conducteur : aucune autre réponse défendable).
Clé jamais strictement la plus longue (Q9 : 33 / 32 / 34 / 28).

Q8 :
```json
{
  "prompt": "هذا رسم جرس كهربائيّ. أيّ رقم يدلّ على المغنط الكهربائيّ فيه؟ <svg viewBox=\"0 0 340 240\"><circle cx=\"158\" cy=\"55\" r=\"36\" fill=\"#fbbf24\" stroke=\"#0f172a\" stroke-width=\"2.5\"/><circle cx=\"158\" cy=\"55\" r=\"10\" fill=\"#f59e0b\" stroke=\"#0f172a\" stroke-width=\"2\"/><rect x=\"70\" y=\"123\" width=\"120\" height=\"14\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><g fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.5\"><ellipse cx=\"90\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"100\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"110\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"120\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"130\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"140\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"150\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"160\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"170\" cy=\"130\" rx=\"4\" ry=\"16\"/></g><rect x=\"206\" y=\"70\" width=\"8\" height=\"120\" fill=\"#64748b\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><circle cx=\"210\" cy=\"62\" r=\"8\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><polygon points=\"202,200 218,200 210,190\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><polyline points=\"214,180 218,174 222,186 226,174 230,186 234,174 238,186 242,180 246,180\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"1.8\"/><rect x=\"246\" y=\"168\" width=\"6\" height=\"24\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><rect x=\"214\" y=\"135\" width=\"26\" height=\"8\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><path d=\"M90 146 V215 H128 M162 215 H230 M170 146 V170 H206 M240 139 H300 V215 H270\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2.5\"/><circle cx=\"128\" cy=\"215\" r=\"3.5\" fill=\"#0f172a\"/><circle cx=\"162\" cy=\"215\" r=\"3.5\" fill=\"#0f172a\"/><path d=\"M124 205 H166 M145 205 V193\" fill=\"none\" stroke=\"#0f6e56\" stroke-width=\"3\" stroke-linecap=\"round\"/><rect x=\"230\" y=\"203\" width=\"40\" height=\"24\" fill=\"#f59e0b\" stroke=\"#0f172a\" stroke-width=\"2\"/><g font-size=\"16\" font-weight=\"700\" fill=\"#0f172a\" text-anchor=\"middle\"><text x=\"241\" y=\"221\">−</text><text x=\"259\" y=\"221\">+</text></g><g font-size=\"16\" font-weight=\"700\" fill=\"#0f172a\" text-anchor=\"middle\" paint-order=\"stroke\" stroke=\"#ffffff\" stroke-width=\"4\" stroke-linejoin=\"round\"><text x=\"158\" y=\"36\">1</text><text x=\"56\" y=\"135\">2</text><text x=\"232\" y=\"112\">3</text><text x=\"232\" y=\"56\">4</text></g></svg>",
  "options": [
    {
      "id": "a",
      "text": "الرقم 1"
    },
    {
      "id": "b",
      "text": "الرقم 2"
    },
    {
      "id": "c",
      "text": "الرقم 3"
    },
    {
      "id": "d",
      "text": "الرقم 4"
    }
  ],
  "correctOption": "b",
  "difficulty": 3,
  "explanation": "المغنط الكهربائيّ قطعة حديد تلفّها وشيعة يسري فيها التيّار، وفي الرسم هي القطعة 2 الّتي يلتفّ حولها السلك. القطعة 3 ساعد من حديد يجذبه المغنط الكهربائيّ، وفي أعلاه الرأس 4 الّذي يضرب الصحن 1 فنسمع الدقّة."
}
```
Q9 :
```json
{
  "prompt": "في هذا الجرس الكهربائيّ صنعنا القطعة 1 من النحاس بدل الحديد. ماذا يحدث حين نضغط على الزرّ؟ <svg viewBox=\"0 0 340 240\"><circle cx=\"158\" cy=\"55\" r=\"36\" fill=\"#fbbf24\" stroke=\"#0f172a\" stroke-width=\"2.5\"/><circle cx=\"158\" cy=\"55\" r=\"10\" fill=\"#f59e0b\" stroke=\"#0f172a\" stroke-width=\"2\"/><rect x=\"70\" y=\"123\" width=\"120\" height=\"14\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><g fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.5\"><ellipse cx=\"90\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"100\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"110\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"120\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"130\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"140\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"150\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"160\" cy=\"130\" rx=\"4\" ry=\"16\"/><ellipse cx=\"170\" cy=\"130\" rx=\"4\" ry=\"16\"/></g><rect x=\"206\" y=\"70\" width=\"8\" height=\"120\" fill=\"#64748b\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><circle cx=\"210\" cy=\"62\" r=\"8\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><polygon points=\"202,200 218,200 210,190\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><polyline points=\"214,180 218,174 222,186 226,174 230,186 234,174 238,186 242,180 246,180\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"1.8\"/><rect x=\"246\" y=\"168\" width=\"6\" height=\"24\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><rect x=\"214\" y=\"135\" width=\"26\" height=\"8\" fill=\"#94a3b8\" stroke=\"#0f172a\" stroke-width=\"1.5\"/><path d=\"M90 146 V215 H128 M162 215 H230 M170 146 V170 H206 M240 139 H300 V215 H270\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2.5\"/><circle cx=\"128\" cy=\"215\" r=\"3.5\" fill=\"#0f172a\"/><circle cx=\"162\" cy=\"215\" r=\"3.5\" fill=\"#0f172a\"/><path d=\"M124 205 H166 M145 205 V193\" fill=\"none\" stroke=\"#0f6e56\" stroke-width=\"3\" stroke-linecap=\"round\"/><rect x=\"230\" y=\"203\" width=\"40\" height=\"24\" fill=\"#f59e0b\" stroke=\"#0f172a\" stroke-width=\"2\"/><g font-size=\"16\" font-weight=\"700\" fill=\"#0f172a\" text-anchor=\"middle\"><text x=\"241\" y=\"221\">−</text><text x=\"259\" y=\"221\">+</text></g><g font-size=\"16\" font-weight=\"700\" fill=\"#0f172a\" text-anchor=\"middle\" paint-order=\"stroke\" stroke=\"#ffffff\" stroke-width=\"4\" stroke-linejoin=\"round\"><text x=\"158\" y=\"36\">3</text><text x=\"56\" y=\"135\">4</text><text x=\"232\" y=\"112\">1</text><text x=\"232\" y=\"56\">2</text></g></svg>",
  "options": [
    {
      "id": "a",
      "text": "لا تنجذب القطعة 1، فلا يدقّ الجرس"
    },
    {
      "id": "b",
      "text": "يدقّ الجرس كالعادة، فالنحاس معدن",
      "misconceptionTag": "eveil.aim.attire-tous-les-metaux"
    },
    {
      "id": "c",
      "text": "يدقّ الجرس أقوى، فالنحاس ناقل جيّد"
    },
    {
      "id": "d",
      "text": "تسخن القطعة 1 وتحمرّ دون صوت",
      "misconceptionTag": "eveil.elec.effets-du-courant-confondus"
    }
  ],
  "correctOption": "a",
  "difficulty": 3,
  "explanation": "القطعة 1 هي الساعد، والقطعة 4 الّتي تلفّها الوشيعة تصير مغنطًا كهربائيًّا حين نضغط على الزرّ. المغنط يجذب الموادّ الحديديّة ولا يجذب النحاس، فلا يتحرّك الساعد ولا يضرب رأسه 2 الصحن 3، فلا يدقّ الجرس. الخطأ الشائع أن نظنّ أنّ المغنط يجذب كلّ المعادن."
}
```
---

## Notes de l'auteur relues après coup (doutes)

1. « ق » pour l'Est : voir mineur 07 — l'arbitrage V5 ne fixe pas la lettre ; le choix tient.
2. Satellite p.144 item 7 non repris : d'accord (mécanique orbitale) ; M08-10 n'en prend que le cadre (le poids diminue en s'éloignant).
3. « مصابيح البيت تضيء دون خليّة » : fait juste, hors manuel, sans clé — OK.
4. Eau pure isolante (manuel) vs « ناقل ضعيف » (guide) : le cours suit le manuel — OK.
5. Électroaimant « temporaire » : le cours dit « مسمار من حديد » — OK pour la 6ᵉ.
6. Balance « ذاتي » comptée parmi les balances de masse : convention du manuel p.143 — OK.
7. Reprises redessinées : p.138 — voir M11-4 (noyaux ajoutés, objets changés) ; p.144 — conforme.
8. Figures « relues dans Chromium en RTL » : vrai pour 07/11, **faux pour 08** (M08-1).
9. Étiquettes proposées : j'en retiens trois comme nécessaires (M07-6, M11-5).
