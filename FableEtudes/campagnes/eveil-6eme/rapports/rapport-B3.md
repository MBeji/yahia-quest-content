# Rapport auteur — lot B3 (`04-nutrition`, `06-reproduction-florale`, `05-milieu-chaines-alimentaires`)

Lu avant d'écrire : prompt auteur, skills (`content-ecole-tn`, `content-engine` + références, `content-cours`, `content-interactif`, `prof-eveil-primaire`), fiche (en-tête, §1 dont §1.7, §2 unités 3 et 4, §4, §4 bis, §6.0–6.5, §7.23–7.25, 7.28, 7.31–7.35, 7.36–7.42), `PLAN.md` § 3, et **à l'image** les pages du manuel 103604 p.84–95, 96–107, 108–117. Aucun slug, `displayOrder`, id ou nom de fichier d'exercice n'a changé. Notes : `auteurs-notes/B3/NOTES.md` (table des écarts).

## Résultat des contrôles
`content:check` vert · `content:qa` 0 erreur, 0 avertissement sur B3 · `content:figures:check` vert · `content:tranche --fresh --strict-longest` : 0/20 clé la plus longue, 0 paire proche, 0 recul de patron · `prettier --check` vert · rendu `renderLesson`/`renderSummary` des 3 cours et 3 résumés propre (aucun `_`, `**`, `:::` résiduel).

## 04-nutrition
**Écarts trouvés et corrigés**
- Salubrité des aliments (guide p.99, جذاذة 4 تقييم ج, manuel p.95 6-ب et 7) : une phrase seulement → **section 9 « سلامة الغذاء »** au patron (ancrer, nommer, tableau règle/danger, exemple, piège « متوازنة ⇒ سليمة », règle, `verifie`, `retenir`), résumé et quiz alignés.
- السكّري et ضغط الدّم cités sans signe ni exercice → second tableau (علامة السكّري : جرح qui ne cicatrise pas vite ; تصلّب الشرايين : pression qui monte), exemple, questions.
- Conception de la جذاذة 4 « les groupes = fatour / déjeuner / dîner » : piège ajouté + distracteur.
- Confusion des maladies de carence : tag présent dans des distracteurs mais absent de `coursePitfalls` et sans `::: piege` → piège ajouté, tag déclaré.
- النشويات : le manuel range le pain et la pomme de terre sous « السكّريات » ; une phrase le dit.
- Erreurs du manuel / du guide **non reprises** : « الهزال الرّزي » jamais clé ; vitamine D « يكسب مناعة » (guide p.133) ; lait côté énergie (guide p.97) ; « boire avant le repas » ; six groupes et tableau des vitamines (ملفّ, ◐) absents des clés ; question 02-boss Q4 : le café d'un enfant remplacé par un verre d'eau (registre d'âge) ; 01-pratique Q3 reformulée (« كم يكوّن الماء… »).
**Questions** (+11, 1 remplacée) : quiz Q6 ; 01 Q7 (les trois groupes), Q8 (matching), Q9 (date de péremption) ; 02 Q7 (multi, petit-déjeuner d'Ahmed), Q8 (affirmation fausse d'Ahmed) ; 03 Q7 (diabète), Q8 (équilibré mais pas sain) ; 04 Q7 (multi salubrité), Q8 (excès + aliment à l'étal) ; 05 Q5 → matching (manuel p.95 6-أ, même rang d3), Q7 (question libre « اسم المرض… »).
**Reprises déclarées** : `02-boss` → `503604` p.128–129, `تقييم 2 · 1-أ`, `1-ب` (adaptée : 6 aliments sur 8, la contrainte du `multi` est ≤ 6 options) ; `05-entrainement` → `103604` p.95, `أطبّق 6-أ`.

## 06-reproduction-florale
**Écarts trouvés et corrigés**
- حاجز p.152 التأبير ≠ الإخصاب : distracteurs partout mais ni piège ni tag déclaré → piège dans la section الإخصاب, tag déclaré.
- التأبير par l'homme (palmier, manuel p.100 et 107, guide p.153) cité jamais montré → 4ᵉ exemple et question.
- Vocabulaire التأبير ≠ التلقيح (التلقيح = vaccination) et conception § 1.7 n° 5 → `> ⚠️`, quiz Q6, question libre, distracteurs.
- Expérience du sachet (manuel p.103, guide p.153) : une question en mots → question visuelle SVG.
- ثمرة حقيقيّة / كاذبة (manuel p.107) : cas limite d'une section déjà à 55 lignes → **section propre** (résumé : 6 puces / 6 sections).
- Ordre du cycle (manuel p.106 6-أ) et légende des organes (p.99 6, p.100 1-ب) : plus de forme native → `ordering` et `matching` sur figure SVG numérotée (sans étiquette qui donne la clé).
- Pas de clé sur la liste du manuel p.106 6-ج (اللفت، الفجل، الثوم، الخرشوف : حوليّة/دائمة contestables) : seuls القمح، الفول، الجلبّان (حوليّة) et الزيتون، النخيل، المشمش، الرمان (دائمة) servent.
**Questions** (+10) : quiz Q6 ; 01 Q7 (matching figure), Q8 (ce que porte l'insecte), Q9 (libre : اسم الإخصاب) ; 02 Q7 (sachet, SVG), Q8 (palmier) ; 03 Q7 (ordering), Q8 (correction du « تلقيح ») ; 04 Q7 (pesticide, pollinisateurs), Q8 (multi خلطي).
**Reprises déclarées** : `02-boss` → `103604` p.103 `أقيّم 7` ; `03-revision` → p.106 `أطبّق 6-أ`.

## 05-milieu-chaines-alimentaires
**Écarts trouvés et corrigés**
- **V4** : le cours posait « تركيد ← ترشيح ← تغلية ← تعقيم » comme règle ordonnée (le manuel p.115 3 ne le donne que comme *hypothèse* d'élève) et `03-revision` Q6 en demandait l'ordre → section réécrite : « ماء صافٍ ≠ صالح », deux gestes (إزالة الشوائب / قتل الجراثيم), **schéma de la station (guide p.166) à lire** ; Q6 remplacée par une pure lecture du schéma (« أيّ حوض بعد الترشيح ? »). Plus aucune question ne demande les étapes. Plus de conseil d'ajouter de l'eau de Javel soi-même (ni dans le cours ni ailleurs).
- « Que se passe-t-il si une maillon disparaît » (guide p.162 تقييم أ, وضعيّة du criquet ; manuel p.108 1-ب) : absent → **section 6 « حلقة تغيب »** + piège + quiz Q6 + 02 Q7/Q8.
- Chaîne aquatique et plancton (manuel p.112 1-ب ; guide p.145) : producteurs étendus aux algues et عوالق نباتيّة, exemple, 01 Q7/Q8.
- Conception « l'eau polluée = l'eau avec de la terre » (guide p.163) → intégrée au piège « eau limpide » ; crue de 1969 → `verifie`.
- Reprises du manuel p.117 7-أ (diagnostic par symptômes) et 7-ب (solutions) → matching et multi.
**Questions** (+7, 3 remplacées) : quiz Q6 ; 01 Q7 (ordering de la chaîne du lac), Q8 ; 02 Q7, Q8 (multi, mort des lapins) ; 03 Q6 → lecture de schéma (d2, même rang) ; 04 Q1 → matching 7-أ (d2, même rang), Q7 (crue) ; 05 Q4 → multi 7-ب (d3, même rang), Q7 (libre : اسم المرض dû à un virus).
**Reprises déclarées** : `01-pratique` → p.112 `1-ب` ; `04-defi` → p.117 `7-أ` ; `05-entrainement` → p.117 `7-ب`.

## Défaut hérité corrigé (hors consigne, trouvé au rendu)
Six gras coupés par un retour à la ligne (`**…\n…**`) dans les trois cours laissaient des `**` visibles à l'écran (le moteur ne ferme pas un gras sur deux lignes). Recollés. **À balayer sur les 9 autres chapitres** et probablement sur d'autres matières.

## Ids d'étiquettes proposés (rien n'est inventé dans les fichiers : les options concernées sont muettes)
- `eveil.eco.maillon-retire-sans-effet` — « تظنّ أنّ غياب حلقة لا يؤثّر في غيرها » (05 : quiz Q6 d, 02 Q7 b/c/d, Q8 d : ≥ 3 questions).
- `eveil.nutri.equilibre-sans-salubrite` — « تظنّ أنّ الوجبة المتوازنة سليمة دائمًا » (04 : quiz Q6 b, 03 Q8 a ; + piège du cours).
- `eveil.flor.parties-de-la-fleur-transportees` — « تظنّ أنّ الرياح تحمل بتلات أو بويضات لا حبّات الطلع » (06 : 01 Q8 a/c, 03 Q8 c/d).
- `eveil.flor.talqih-pour-tabir` — « تسمّي التأبير تلقيحًا » (06 : quiz Q6 a, 03 Q8 d ; seuil ≥ 3 non atteint).
- `eveil.nutri.groupes-confondus-avec-repas` — « تظنّ أنّ المجموعات الغذائيّة هي الفطور والغداء والعشاء » (04 : 01 Q7 a ; 1 question + piège ; seuil non atteint).

## Doutes pour l'auditeur
1. **Nombre de notions** : 04 = 9 sections, 05 = 9 sections (au-delà de ~8 : question de programme, pas de coupe silencieuse). 05 couvre trois دروس (27, 28, 29) ; un partage « chaîne alimentaire / pollution et maladies de l'eau » est à arbitrer par l'humain.
2. **`manuel.code` du guide** : `02-boss` de 04 déclare `503604` (guide enseignant) pour reprendre deux تعليمات d'évaluation. `content:check`/`qa` l'acceptent ; la galerie « pages du manuel » n'est alimentée que par le `chapter.json`, mais si le rapport de couverture ne sait pas lire ce code, le retirer.
3. **Règles de salubrité** (04, section 9) : elles viennent du guide p.99 et de la جذاذة 4 (« قواعد صحّية ») ; le manuel p.95 n'en donne que le principe. Volontairement écartés : l'eau de Javel pour laver les légumes (conseil risqué pour un élève de 11 ans) et la ligne « sel en été » du tableau الخطأ/الصواب (discutable hors contexte, guide p.98).
4. **Classement du lait** : le manuel (p.88) et la جذاذة le rangent côté بناء ; le tableau à six groupes du guide (p.97) le range côté énergie. Le cours suit le manuel.
5. **Schéma de la station (05)** : fidèle à l'ordre du guide p.166 (مضخّة → ترسيب → ترشيح → كلور → تهوئة → خزّان) ; le texte `[?]` p.166 (« نواد ») n'est pas repris. Le vocabulaire du guide est « ترسيب » (le chapitre disait « تركيد »).
6. **Chaîne du lac** : « اليرقات تتغذّى على العوالق الحيوانيّة » est ma lecture des quatre noms du manuel p.112 1-ب (le guide p.145 donne la même chaîne : أسماك كبيرة ← أسماك ويرقات ← عوالق حيوانيّة ← عوالق نباتيّة). Le manuel n'imprime pas de corrigé.
7. **Sachet (06)** : figure dessinée par moi (pollen sur les anthères seulement, jamais sur le stigmate, pour ne pas fuiter la clé). La clé « زهرة 1 » est ma lecture du manuel p.103 (pas de corrigé imprimé).
8. **ثمرة كاذبة** (06) : savoir du manuel p.107 (« معجمي في العلوم »), enseigné ; le piège de la section n'a pas d'étiquette du registre (la plus proche, `fruit-sans-pollinisation`, dit autre chose) — donc non déclaré dans `coursePitfalls`.
9. **Matching à 3 paires** (04 01 Q8, 05 04 Q1) : bijections minimales imposées par le format ; la richesse est dans les termes à relier.
10. Questions libres : réponses canoniques sans variante (l'article et la vocalisation sont repliés par le moteur) ; `expectedMistakes` taguées ; explications sans la réponse.
