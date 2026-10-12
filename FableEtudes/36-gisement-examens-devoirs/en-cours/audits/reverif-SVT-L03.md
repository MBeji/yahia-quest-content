# Re-vérification ciblée — lot SVT-L03 (ch. 08-at-tanaffus, missions 07 à 11), après correctifs

## État d'avancement

- [x] Version auditée identifiée (`wt-sav2` 99ae05ba : tailles 30377/18333/6563/39068/23696 octets, identiques aux fichiers audités ; recoupé avec mes extraits d'audit — questions de 10 et 11, onze SVG — : identiques)
- [x] Diff structurel aveugle (auditée → arbre actuel du 2026-10-12 ~07:37) — écrit
- [x] Section 07 — écrite
- [x] Section 08 — écrite
- [x] Section 09 — écrite
- [x] Section 10 — écrite
- [x] Section 11 — écrite
- [x] Étiquettes neuves (en attente) et existantes — écrites
- [x] Gates — écrits
- [x] Synthèse et verdicts — écrites (re-vérification terminée)

Auditeur indépendant, même consigne que `audit-SVT-L03.md`. Rien n'est modifié dans le dépôt (les gates lancés
en lecture seule n'ont écrit aucun fichier : contrôlé par `find -newer` sur les deux dépôts).

## Méthode

- **Diff structurel AVEUGLE** (énoncés, options, figures, type, difficulté ; clés, explications et étiquettes
  signalées seulement comme « changées », sans contenu), puis diff profond de tout le JSON (aucun autre champ
  touché : en-têtes, difficultés et ordre d'émission inchangés dans les cinq fichiers).
  - Côté visible : 07 Q6 (énoncé + 4 options) ; 08 Q1 (figure : `viewBox` seul ; options c, d), 08 Q3 (type
    `matching` → `mcq`, énoncé, figure, 4 options) ; 09 Q3 (a, b), 09 Q4 (b) ; 10 Q1 (énoncé), 10 Q2 (b, c, d),
    10 Q9 (énoncé, c) ; 11 Q8 (énoncé).
  - Côté caché seulement : explications 07 Q3, 11 Q7 ; étiquettes 07 Q2, 09 Q2, 10 Q7, 11 Q3.
- **Re-résolution à l'aveugle** des neuf questions dont le côté visible a bougé, avant lecture de leur clé :
  07 Q6 b · 08 Q1 b · 08 Q3 c · 09 Q3 d · 09 Q4 b · 10 Q1 c · 10 Q2 b · 10 Q9 b · 11 Q8 c — **9/9 = les clés**.
- **Textes appliqués comparés par script à mes correctifs** (recherche verbatim dans `audit-SVT-L03.md`,
  lettres A–D ramenées aux chiffres pour 08 Q3) : verbatim partout, sauf les six écarts déclarés par l'auteur
  (traités nommément ci-dessous). **Aucun écart non déclaré.**
- **Rendu Chromium `dir=rtl`** (`bidi.ts` d'arena `origin/main`, harnais de l'audit) des onze questions qui ont
  bougé (07 Q3, Q6 ; 08 Q1, Q3 ; 09 Q3, Q4 ; 10 Q1, Q2, Q9 ; 11 Q7, Q8) et des deux figures de 08 : ordre de
  lecture correct partout (chiffres des cavités et « ؛ », flèche « ← » de l'équation, « أذينيّ-بطينيّ ») ;
  `splitMathRuns` n'isole que la flèche de 07 Q6 ; figures : **0 débordement** (`overflow.cjs`), filtre DOMPurify
  de l'application **intact** (`sanitize.cjs`).
- Faits contrôlés sur les cours d'`origin/main` (05 l. 302 ; 06 l. 270, 283, 294-295, 326 ; 07 l. 296-302, 316 ;
  08 l. 169-221, 249, 271, 302-304, 324, 346), registre `content/misconceptions.json` d'`origin/main` (edb6e79 ;
  le seul commit arrivé depuis sur `main`, 6891f41 — lot L02, chapitre 03 —, n'ajoute que
  `bio.vis.difference-non-montree` et ne touche ni le chapitre 08 ni les étiquettes ci-dessous).

## 07 (6 questions, practice d2, rampe 1,1,2,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 c (étiquette ajoutée) | — (côté visible inchangé) | d | OK |
| Q3 (explication, écart 3) | — (côté visible inchangé) | a | réserve mineure |
| Q6 (lacune, écart 4) | b « الماء » | b | OK |

- **Q2 c — `bio.dig.absorption-dans-la-digestion` : exacte.** « البنية 1 : هضم الأغذية بمفعول الأنزيمات » donne
  la digestion enzymatique à la structure qui absorbe : c'est l'erreur du libellé (« تعدّ الامتصاص جزءًا من
  الهضم ») ; une seule erreur (structure 2 juste) ; porte R1 ouverte (« الخطأ الشائع: عدّ الامتصاص هضمًا »).
  Grille 2×2 recomptée : structure 1 {absorption a, d / digestion b, c}, structure 2 {fabrique O₂ a, b / échange
  c, d} ; b à deux erreurs, muette ; longueurs 83/86/86/83, la clé d n'est pas la plus longue.
- **Q3 — écart 3 (explication limitée à la villosité) : juste, et l'accord est corrigé.** Phrase à phrase :
  - « لكلّ من البنيتين جدار رقيق من طبقة خلايا واحدة … وجدار السّنخ الذي لا يتجاوز سمكه 0,5 ميكرون » : cours 08
    l. 169, 176, 199, 221 (« سمك جدار الواحد منها 0,5 ميكرون », « جدار لا يتجاوز 0,5 ميكرون ») ;
  - « ففي الخملة لا يفصل ما يُتبادل عن الدّم إلّا طبقتان من الخلايا … أي نحو 0,05 مم » : conforme au cours 05
    l. 302-303 (« نحو 0,05 مم، إذ لا توجد بينهما إلّا طبقتان »). Restreindre les deux couches à la villosité est plus prudent que mon texte : le cours 08
    attribue 0,5 µm tantôt au seul « جدار السّنخ », tantôt à toute la paroi traversée ; mon « هذا الجدار وجدار
    الشّعيرة » pour l'alvéole ne s'appuyait sur aucune ligne du cours ;
  - « وتجاور كلًّا منهما شبكة كثيفة » : accord juste (verbe au féminin, sujet « شبكة » ; « كلًّا » objet
    antéposé) ; le reste (« يبطؤ », cœur et artères, gros vaisseaux) inchangé et juste.
  - **Réserve mineure (référent ambigu, déjà présent dans MON texte et accentué par la restructuration)** :
    « كلًّا منهما » suit désormais immédiatement le duel « الخلايا الظّهاريّة وجدار الشّعيرة » ; on peut lire
    « un réseau de capillaires borde chacune des deux couches », dont la paroi du capillaire elle-même. Correctif
    exact (vérifié par script — une seule occurrence remplacée — et rendu Chromium `dir=rtl` conforme) :
    « وتجاور كلًّا منهما شبكة كثيفة » → « وتجاور كلًّا من البنيتين شبكة كثيفة ».
- **Q6 — lacune « الماء » : une seule bonne réponse.** Les trois distracteurs tombent tous (urée : déchet azoté que
  le sang porte au rein, cours 06 l. 270, 283 ; azote : 79 % → 79 %, cours 08 l. 249, 271 ; glycogène : réserve
  hépatique, cours 06 l. 294-295) ; aucun ne peut sortir de glucose + O₂. Clé la plus courte (5 contre 6/6/10).
  - **Écart 4 « الغليكوجين » : juste.** C'est la graphie du cours 06 (« في شكل غليكوجين », « غليكوجينًا ») et la
    seule du SVT publié (7 occurrences de « غليكوجين », 0 de « جليكوجين ») ; « الجليكوز » en ج est lui aussi la
    graphie du corpus. Mon « الجليكوجين » était l'écart.
  - **Fuites.** Route quête (ordre d'émission = ordre du fichier, Q4 → Q5 → Q6) : ni l'explication de Q4
    (« تأخذ … الجليكوز والأكسيجين، وتطرح فيه ثنائي أكسيد الكربون ») ni celle de Q5 ne nomment l'eau ; seul reste
    l'indice faible déjà accepté (m-07-2 : Q5 d « صنع الجليكوز من ثنائي أكسيد الكربون والماء »). Dans l'autre
    sens, Q6 ne livre pas Q4 sur la route quête (Q4 passe avant). Donjon (tirage au hasard) : l'équation montrée
    par Q6 laisse déduire le sens des échanges de Q4 et écarte c, d de Q5 — résidu documenté à l'audit
    (inévitable dès qu'on montre l'équation, contenu même du cours et de la sous-question officielle), non
    aggravé.
  - Mon explication relue ligne à ligne : conforme aux cours cités, rendu correct (flèche « ← » isolée, lue dans
    le bon sens).
- Grilles inchangées et recomptées : Q1 {خملة a, b / شعيرة c, d} × {شعيبة a, d / سنخ b, c} ; Q3 {رقيق a, b /
  سميك c, d} × {شبكة a, c / جريان سريع b, d} — chaque valeur deux fois, option à deux erreurs muette, clé jamais
  strictement la plus longue (Q3 : 66/57/71/62).

**Verdict 07 : réserve mineure** (référent « كلًّا منهما » de l'explication de Q3 ; correctif exact ci-dessus) ;
0 clé fausse ; écarts 3 et 4 validés.

## 08 (4 questions, practice d2, rampe 2,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (options c, d ; explication ; figure : `viewBox`, écart 6) | b | b | OK |
| Q3 (dessin incomplet, QCM 2×2, cavités 1–4, étiquette a ; écarts 1 et 2) | c | c | OK |

- **Q1.** c, d et l'explication sont mes textes, verbatim. Grille recomptée : identification {1 = sigmoïde : b, c /
  1 = AV : a, d} × rôle {« يمنع رجوع » : a, b / « يدفع بانقباضه » : c, d} ; d à deux erreurs, muette ; longueurs
  132/132/140/140 (clé b non la plus longue) ; aucune option ne se réfute plus à la lecture de son propre nom.
  L'explication ne nomme plus « الشّريان الرّئويّ » (maillon de Q2).
  - **Écart 6 (`viewBox="0 -4 280 194"` au lieu de `stroke-linecap="butt"`) : juste, et meilleur que mon
    correctif.** C'est la seule modification du SVG (diff caractère à caractère) ; le bord bas ne bouge pas
    (−4 + 194 = 190), la marge de 4 unités en haut contient les capuchons ronds (débordement 0), qui restent
    arrondis comme sur le dessin officiel au lieu d'être tranchés net ; filtre intact ; rendu vu.
  - **Retouche facultative, préexistante (phrase de l'auteur conservée par mon correctif)** : « فلكلّ صمّام اسم
    موضعه » dit que chaque valvule porte le nom de sa position, ce qui est vrai de l'AV mais pas de la sigmoïde,
    nommée d'après sa forme — l'explication vient d'ailleurs de dire « سينيّ هلاليّ الشّكل ». Texte exact (vérifié
    par script et rendu Chromium) : « فلكلّ صمّام اسم موضعه ودور واحد: فرض اتّجاه واحد على الدّم. » → « فلكلّ
    موضع صمّامه، ولكلّ صمّام دور واحد: فرض اتّجاه واحد على الدّم. » (la phrase suivante, « تبديل الاسمين بين
    الموضعين », reste cohérente).
- **Q3 — écart 1 (cavités 1 à 4, clé en c, `viewBox` recadré) : juste et nécessaire.** Le portail affiche les
  options mélangées sous des pastilles `DISPLAY_LABELS = ["A", "B", "C", "D", "E", "F"]` (arena `origin/main`,
  `src/shared/lib/question-utils.ts` l. 18) : « التجويف C » aurait pu s'afficher dans la pastille « B ». Les
  chiffres ne heurtent rien (aucun autre chiffre dans la question ; les repères 1–4 des vaisseaux de l'ancienne
  version ont disparu). Énoncé, options, `<title>` et explication = mes textes avec A→1, B→2, C→3, D→4 (vérifié
  par script), plus « أي التجويف 3 » / « أي التجويف 4 » dans l'explication, nécessaires (« الأذينة اليسرى 3 » se
  lirait mal). Options réordonnées : a = 1/4 (étiquetée), b = 3/2, **c = 3/4 (clé)**, d = 1/2 ; grille {veines → 1 :
  a, d / → 3 : b, c} × {aorte depuis 4 : a, c / depuis 2 : b, d}, chaque valeur deux fois, d à deux erreurs et
  muette, quatre options de 79 caractères. Rendu : « والتجويف 1 ؛ الشّريان … التجويف 4 والعضلة » dans le bon ordre.
  - Figure (rendue en grand) : « 1 » dans l'oreillette du côté gauche du dessin, « 2 » dans le ventricule
    au-dessous, « 3 » et « 4 » en face ; le vaisseau venu du muscle entre dans 1, celui de 2 monte au poumon
    gauche ; vraie, conforme à l'énoncé et à l'explication (« القلب الأيمن على يسار الرّسم ») ; aucun vestige des
    vaisseaux retirés (pas d'amorce, paroi externe intacte au-dessus de 3 et à droite de 4) ; recadrage 300 → 270 :
    rien au-delà de x ≈ 254 (poumon droit), débordement 0, filtre intact.
  - **Écart 2 — `bio.circ.oreillettes-inversees` sur a : exacte, à garder.** a envoie les veines pulmonaires dans
    la cavité 1, où arrive la veine cave (oreillette droite), aorte juste : une seule erreur, celle-là même que le
    registre étiquette déjà ainsi dans la publiée `07-ad-dawaran/exercices/01-tamrin.json` Q5 a (« إلى أين تصبّ
    الأوردة الرّئويّة الأربعة؟ » → « الأذينة اليمنى ») ; la correction du libellé (« والأوردة الرّئويّة في الأذينة
    اليسرى ») est exactement ce que a manque ; porte R1 ouverte (« الخطأ الشائع: إيصال الأوردة الرّئويّة بالأذينة
    اليمنى »). Le diagnostic « تعكس مصبّات الأوردة » est plus large que a (les veines caves sont imposées par le
    dessin), mais c'est la lecture du placement publié. Pas d'ambiguïté : l'erreur d'orientation (prendre 1 pour
    l'oreillette gauche) mène à d (1 et 2), pas à a. b (aorte depuis le ventricule droit) : aucune étiquette exacte,
    muette ; d : deux erreurs, muette.
  - Fuites : la correction de Q2 (ordering, émise avant) donne encore « veines pulmonaires → oreillette gauche »,
    reste à lire le dessin (accepté à l'audit) ; l'explication de Q3 ne dit rien des flux gazeux de Q4.
  - **Retouche cosmétique facultative, préexistante (je l'avais manquée à l'audit)** : le rectangle blanc qui
    ouvre l'oreillette 3 sur le ventricule 4 (`<rect x="138" y="74" width="46" height="18" fill="#fff1f2"
    stroke="none"/>`, groupe `translate(50 104)`) dépasse de 2 unités le bord interne du ventricule gauche
    (x = 182) et entaille le haut de la paroi épaisse (≈ 2 px à la largeur d'affichage). Aucun indice (paroi
    externe intacte), déjà dans la figure auditée. Texte exact : `width="46"` → `width="43"` sur ce seul `rect`
    (il s'arrête à x = 181, avant le trait de 1,8) — vérifié : débordement 0, filtre intact, rendu Chromium net.
  - Style, mon texte, laissé tel quel : « يمثّل الرسم التالي رسمًا مبسّطًا » répète « رسم » sans gêner la lecture.

**Verdict 08 : OK** ; 0 clé fausse ; écarts 1, 2 et 6 validés ; deux retouches facultatives et préexistantes
(phrase « اسم موضعه » de l'explication de Q1 ; entaille du `rect` de la figure de Q3).

## 09 (4 questions, practice d2, rampe 1,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 c (étiquette retirée) | — (côté visible inchangé) | a | OK |
| Q3 (a, b ; écart 5) | d | d | OK |
| Q4 (b « وحدهما ») | b | b | OK |

- **Q2 c** : `bio.dig.specificite-enzyme-ignoree` retirée comme demandé (m-09-1) — l'option fait digérer les aliments
  MINÉRAUX, erreur sans entrée au registre : muette. b et d gardent des étiquettes exactes.
- **Q3 — écart 5 (« أغلبُه منحلّ في البلازما وقليله متّحد بالهيموغلوبين ») : juste, plus clair que mon texte.**
  Dans mon « منحلًّا أغلبُه في البلازما، وقليله مع الهيموغلوبين », le حال « منحلًّا » pouvait se lire sur tout le
  gaz, y compris la part liée à l'hémoglobine (objection de l'auteur, fondée) ; la phrase nominale lève
  l'ambiguïté et se construit normalement après « يُنقل الأكسيجين في الدّم : » (جملة حاليّة reliée par le pronom).
  Vocabulaire du cours 08 (« منحلًّا في البلازما » l. 302, « اتّحاده مع الهيموغلوبين » l. 304) ; fausse (au plus
  1,5 % dissous, l. 324) ; exécute exactement `bio.sang.plasma-transporte-l-oxygene` (« l'essentiel de
  l'oxygène »), porte R1 (« ظنّ أنّ البلازما تنقل أغلب الأكسيجين »). Forme : « هيموغلوبين » en a, c, d, « متّحد »
  en a et d — aucun marqueur propre à la clé ; clé d = 36 caractères, a = 51 (la plus longue).
  b (« بواسطة الكريّات البيضاء التي تحمله إلى الخلايا », mon texte, verbatim) ne porte plus de glose qui la
  réfute ; `bio.sang.fonctions-des-cellules-confondues` exacte. c inchangée, muette (le carboxy-hémoglobine est la
  forme du CO₂ dans le cours 08, l. 304). L'explication, inchangée, reste juste (sa mention des plaquettes,
  héritée de l'ancienne b, est vraie et sans effet).
- **Q4 b** (mon texte, verbatim) : vraie selon le cours 07 (l. 299-302 : la part extracellulaire, 30 %, « وهي
  الوسط الدّاخليّ », comprend la vasculaire 9 % — sang et lymphe dans les vaisseaux — et l'interstitielle 21 % :
  9 + 21 = 30, les deux compartiments l'épuisent, « وحدهما » est exact et ne retranche pas la lymphe, comptée dans
  la vasculaire comme le dit l'explication). Qualificatifs : a « وحدها », b « وحدهما », c « وحده », d « كافّة » —
  la clé n'est plus la seule option non absolue ; longueurs 23/45/20/62.

**Verdict 09 : OK** ; 0 clé fausse ; écart 5 validé.

## 10 (9 questions, challenge d4 300/60, rampe 2,3,3,3,3,3,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (énoncé : convention du dessin) | c | c | OK |
| Q2 (b, c, d : queue commune) | b | b | OK |
| Q7 c (étiquette retirée) | — (côté visible inchangé) | d | OK |
| Q9 (énoncé neutre, c, explication) | b | b | OK |

- **Q1** : « وقد رُسم ماء الجير داكنًا في الرسم الأيسر دلالةً على تعكّره. » = m-10-1 verbatim, rien d'autre ne bouge.
- **Q2** : b, c, d = mes textes, verbatim. Queue « فنقص حجم الغاز في الوعاء » dans les quatre options, « ماء الجير »
  en b et c ; longueurs 84/102/101/108 ; une seule bonne réponse (a : l'azote ne participe pas ; c : le muscle
  rejette le CO₂ ; d : le CO₂ n'est pas consommé). L'explication, inchangée, réfute toujours a, c et d. L'énoncé ne
  livre pas Q1 (« ماء الجير يثبّت ثنائي أكسيد الكربون الذي يصله » ne dit pas d'où il vient), et Q1 passe avant.
- **Q7 c** : `bio.lecture.valeur-d-une-autre-grandeur` retirée (m-10-2) ; c ne donne aucune valeur, elle tire une
  conclusion fausse d'une concentration de sortie, comme b et Q8 d, muettes : cohérent.
- **Q9** : énoncé et c = mes textes, verbatim ; l'explication = l'ancienne moins « وتشتدّ معًا لأنّ النّشاط يرفع
  حاجة العضلة إلى الطّاقة » (virgule devenue point), rien d'autre (vérifié par reconstruction). Plus de contraste
  repos/activité dans l'énoncé : Q7 n'est plus livrée dans le donjon. Longueurs 90/106/77/111. La réfutation de c
  (« أمّا تسارع الجريان فلا يفسّر تغيّر التّراكيز في اتّجاهين متعاكسين ») colle au nouveau c (« دون أن تتدخّل
  خلاياها »). Résidu non introduit, propre au sujet : comme les données de Q5-Q7 (documents 3 et 4 du même
  exercice officiel), l'énoncé montre un sang qui sort du muscle appauvri en O₂ et enrichi en CO₂.
- Grilles 2×2 inchangées, recomptées : Q5 {O₂ par les hématies a, c / par le plasma b, d} × {CO₂ par les hématies
  a, b / par le plasma c, d}, b à deux erreurs et muette, d (O₂ seul faux) `plasma-transporte-l-oxygene` exacte,
  67/84/84/59 ; Q6 {O₂ 150/20 a, b / 50/180 c, d} × {CO₂ 530/650 a, c / 40/160 b, d}, a à deux erreurs et muette,
  b et c `valeur-d-une-autre-grandeur` exactes, 133/132/133/132. Clé jamais strictement la plus longue.

**Verdict 10 : OK** ; 0 clé fausse.

## 11 (8 questions, challenge d4 300/60, rampe 2,2,3,3,3,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 c, d (étiquettes ajoutées) | — (côté visible inchangé) | a | OK |
| Q7 (explication) | — (côté visible inchangé) | a | OK |
| Q8 (énoncé, explication) | c | c | OK |

- **Q3 c, d — `bio.alim.valeurs-energetiques-confondues`** (m-11-3) : porte R1 (« بتطبيق قيمة واحدة على الأصناف
  أو تبديل القيم بينها فتبدو الوجبتان كلتاهما دون الحاجة أو فوقها ») ; recalcul : 4 kcal/g partout → 2320 et
  1800, toutes deux sous 3000 (c) ; glucides à 9 et lipides à 4 → 4195 et 3300, toutes deux au-dessus (d) ;
  valeurs justes 3020 et 2300 (clé a). Usage conforme au registre (04/02-tamrin Q1 a ; 11 Q1 b, Q2 c).
- **Q7** : seule la phrase de m-11-1 a bougé (reconstruction exacte) ; 110/40 = 2,75 ; 500/210 ≈ 2,38 → « نحو
  2,4 ». Juste.
- **Q8** : énoncé « كيف تُنتَج الطّاقة في مستوى خلايا الجسم ؟ » verbatim ; explication = l'ancienne moins « ولهذا
  ترتفع … كما بيّن الجدول والمنحنيات. » (reconstruction exacte) : plus de renvoi à des documents absents ni de
  conclusion de Q6/Q7 dans l'énoncé (Q8 reste la dernière émise). Options inchangées, 96/84/97/97 ; a
  `respiration-combustion` exacte.
- Grille 2×2 de Q5 inchangée, recomptée : conseil 1 {réduire les lipides et augmenter les protides a, c / garder
  b, d} × conseil 2 {lipides seuls a, d / énergie et proportions b, c} ; d à deux erreurs, muette ; b
  `quantite-sans-qualite` exacte ; a muette ; 147/155/149/153.

**Verdict 11 : OK** ; 0 clé fausse.

## Étiquettes

### Neuves, en attente et non posées (`scratchpad/pending-tags/SVT-L03.json`)

- Libellés fr/en/ar = mes libellés d'audit, **verbatim** (script) ; les deux identifiants sont **absents** du
  registre d'`origin/main` (et de celui de l'arbre) et ne figurent **nulle part** dans `content/` (grep : 0) ; les
  deux options du lot (07 Q2 a, 07 Q5 d) sont **muettes** dans les fichiers, textes identiques à ceux du JSON.
- `hors_lot` relu sur `origin/main` (edb6e79 ; 6891f41 ne touche pas ces fichiers) : les quatre textes sont exacts
  et les quatre options **sans étiquette** aujourd'hui → `remplace: null` juste.
- **`bio.resp.appareil-fabrique-l-oxygene`** — « تظنّ أنّ المسالك التنفّسيّة أو الرّئة تصنع الأكسيجين … » —
  **3 questions distinctes, chacune exacte** :
  - 07 Q2 a « … البنية 2 : صنع الأكسيجين الذي تحتاجه الخلايا » : une seule erreur (structure 1 juste), porte R1
    (« والظنّ أنّ الرّئة تنتج الأكسيجين الذي تحتاجه الخلايا ») ; b, qui la porte avec la digestion, reste muette ;
  - `08-at-tanaffus/exercices/01-tamrin.json` Q6 c (« ما دور الغشاء المخاطيّ والأهداب في الأنف؟ » → « تحويل
    الهواء إلى أكسيجين ») : les voies respiratoires « font » l'oxygène, ce que le libellé corrige (« إنّما تأخذه
    من الهواء (21 %) ») ;
  - `08-at-tanaffus/exercices/06-defi-concours.json` Q3 b (« لأنّ رئته تصنع الأكسيجين ») : le poumon fabrique
    l'oxygène, mot pour mot.
  - Les explications des deux publiées donnent la bonne réponse sans nommer l'erreur : même régime que les placements
    SVT déjà publiés (p. ex. `bio.circ.oreillettes-inversees` en 07/01-tamrin Q5, 05-tadrib Q3, quiz Q6), le
    chemin est l'énoncé littéral de l'option — pas de réserve.
- **`bio.resp.respiration-photosynthese-confondues`** — « تخلط بين التنفّس الخلويّ والتركيب الضوئيّ، وهو التفاعل
  المعاكس له … » — **3 questions distinctes, chacune exacte** :
  - 07 Q5 d « التركيب الضوئيّ : صنع الجليكوز من ثنائي أكسيد الكربون والماء » donné pour la réaction qui produit
    l'énergie dans chaque cellule ; l'explication la réfute (« والتّركيب الضّوئيّ عمليّة النّبات الأخضر … ») ;
  - `quiz.json` Q8 b (« ما معادلة الأكسدة الخلويّة؟ ») et `04-defi.json` Q3 b (« ما معادلة التنفّس الخلويّ؟ ») :
    « ثنائي أكسيد الكربون + ماء ← جليكوز + أكسيجين », l'équation renversée, celle de la photosynthèse
    (l'explication de 04-defi le dit : « والاتّجاه المعاكس يصف التّركيب الضّوئيّ ») ;
  - quiz Q8 d (« أكسيجين + ماء ← جليكوز + ثنائي أكسيد الكربون ») n'est pas l'équation de la photosynthèse : muette,
    juste ; 07 Q6 c n'existe plus (lacune) : pas de placement, juste.
- **Seuil de 3 questions distinctes : atteint pour chacune** (3 et 3). Balayage de toutes les options du SVT publié
  (motifs « صنع/تنتج/تحويل … أكسيجين », « إلى أكسيجين », « التركيب الضوئيّ », « ← جليكوز ») : 6 occurrences = les
  4 placements + 06-defi-concours Q3 c (« دمه لا يحتاج إلى أكسيجين », autre erreur) + quiz Q8 d (muette) — aucun
  membre oublié.

### Existantes, ajoutées et retirées

- Ajoutées : 07 Q2 c `bio.dig.absorption-dans-la-digestion`, 11 Q3 c et d `bio.alim.valeurs-energetiques-confondues`,
  08 Q3 a `bio.circ.oreillettes-inversees` — **exactes** (voir 07, 11, 08). Retirées : 09 Q2 c
  `bio.dig.specificite-enzyme-ignoree`, 10 Q7 c `bio.lecture.valeur-d-une-autre-grandeur` — **justes**.
- Inventaire des cinq fichiers = celui de la note du JSON en attente, placement pour placement : **28 placements**
  (26 de l'auteur − 2 retirés + 4 ajoutés), 10 étiquettes, aucune sur une clé ni hors `mcq`, toutes au registre.

## Gates (lecture seule ; aucun fichier écrit dans les deux dépôts)

- `content:check` : vert (120 matières ; registre de l'arbre 853 étiquettes, toutes celles du lot présentes).
- `content:qa -- --subject sciences-vie-terre` : **0 erreur**, 7 avertissements, **aucun dans 08-at-tanaffus**
  (domaine de 07-annales-subur ; lettres d'options dans des explications de 02-manaa, 04-zalazil, 05-barakin).
- `content:tranche -- --subject sciences-vie-terre --chapters 08` (sortie JSON) : 77 questions (46 publiées + 31 du
  lot), 75 QCM mesurés ; « clé strictement la plus longue » 36/75, **toutes publiées (quiz, 01 à 06), 0 dans le
  lot** ; paires proches 2, **toutes deux entre publiées** (quiz#8 ↔ 04-defi#3, quiz#4 ↔ 02-tamrin#5), 0 avec le
  lot ; candidats gabarit 0. La répartition des positions de clé (a 25, b 33, c 10, d 7) est sans effet : les
  options sont mélangées à l'affichage.
- Non lancés à dessein : `content:catalogue` / `content:gates` (ils régénèrent `content/CATALOGUE.md`).

## Synthèse et chiffre final

- **Clés fausses : 0.** 9/9 re-résolutions aveugles = les clés ; aucune option devenue vraie, aucune grille 2×2
  cassée (07 Q1-Q3, 08 Q1, Q3, 10 Q5, Q6, 11 Q5 recomptées).
- **Correctifs de l'audit** : les 9 majeurs et les 8 mineurs à correctif (m-07-1, m-08-2, m-08-3, m-09-1, m-10-1,
  m-10-2, m-11-1, m-11-3) sont appliqués, verbatim ou par l'un des six écarts déclarés ; les 7 autres mineurs
  étaient des constats sans correctif. **Aucun écart non déclaré.**
- **Les six écarts, nommément** : (1) cavités 1–4 en 08 Q3, clé c, `viewBox` 270 — **validé, nécessaire**
  (pastilles A–F du portail) ; (2) `oreillettes-inversees` sur 08 Q3 a — **exacte, à garder** ; (3) explication de
  07 Q3 limitée à la villosité — **validé** (accord juste ; une réserve de référent, ci-dessous) ; (4)
  « الغليكوجين » — **validé** (graphie du cours 06 et du corpus) ; (5) phrase nominale de 09 Q3 a — **validé**,
  plus claire que mon حال ; (6) `viewBox` « 0 -4 280 194 » en 08 Q1 — **validé**, meilleur que mon `butt`.
- **Défauts introduits par les correctifs : 1, mineur** — 07 Q3, référent « كلًّا منهما » (déjà présent dans mon
  texte, accentué par la restructuration) : « وتجاور كلًّا منهما شبكة كثيفة » → « وتجاور كلًّا من البنيتين شبكة
  كثيفة » (vérifié par script et en Chromium).
- **Retouches facultatives, préexistantes** : 08 Q1, « فلكلّ صمّام اسم موضعه ودور واحد: فرض اتّجاه واحد على
  الدّم. » → « فلكلّ موضع صمّامه، ولكلّ صمّام دور واحد: فرض اتّجاه واحد على الدّم. » ; 08 Q3, figure, `<rect
  x="138" y="74" width="46" height="18" fill="#fff1f2" stroke="none"/>` → `width="43"` (vérifiés par script et en
  Chromium ; figure : débordement 0, filtre intact).
- Étiquettes : deux neuves exactes, seuil atteint (3 + 3), non posées, absentes du registre ; existantes ajoutées et
  retirées toutes justes.

| fichier | verdict |
| --- | --- |
| 07 | réserve mineure (07 Q3, référent « كلًّا منهما ») |
| 08 | OK (deux retouches facultatives, préexistantes) |
| 09 | OK |
| 10 | OK |
| 11 | OK |

**Verdict global : livrable une fois la réserve de 07 Q3 levée (un mot) ; aucune clé fausse, aucun défaut majeur.**
