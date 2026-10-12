# Audit indépendant — lot SVT-L02 (gisement 9ᵉ, SVT, ch. 03-al-ibsar, missions 07 à 11)

## État d'avancement

- [x] Prompt, consigne `gisement-auditeur.md`, skill `content-audit` et références lus.
- [x] Cours 01, 02, 03 (`origin/main`), transcriptions 2020/2021/2022/2025/2026, PDF officiels C04, C06, C01, C02, C05 lus et mesurés.
- [x] Re-résolution À L'AVEUGLE des 23 questions **avant** lecture des clés : **23/23 concordent avec les clés du fichier** (0 clé fausse).
- [x] Section 07 (2022 ex.2) — écrite
- [x] Section 08 (2020 ex.2) — écrite
- [x] Section 09 (2026 ex.3) — écrite
- [x] Section 10 (2025 ex.4) — écrite
- [x] Section 11 (2021 ex.5) — écrite
- [x] Étiquettes nouvelles, doublons, synthèse et chiffre final — écrits (audit terminé)

Réponses à l'aveugle (notées avant ouverture des clés) :
07 : Q1 c · Q2 {a,c,e} · Q3 b · Q4 {a,b,c,f} — 08 : Q1 d · Q2 l1-r5 l2-r3 l3-r2 l4-r6 l5-r4 l6-r1 · Q3 a · Q4 {a,b,e} —
09 : Q1 b · Q2 d · Q3 a · Q4 l1-r1 l2-r2 l3-r3 · Q5 d — 10 : Q1 b · Q2 c · Q3 a · Q4 {a,b,d,f} —
11 : Q1 {b,e,f} · Q2 c · Q3 d · Q4 {b,d} · Q5 b · Q6 c.

Méthode commune aux cinq sections : clés re-résolues à l'aveugle (script qui masque `correctOption`,
`answerKey`, `explanation`, `misconceptionTag`), figures rendues dans Chromium à 232 px (harnais qui
reproduit `RichField` : `splitMathRuns`/`isDisplayEquation` d'`origin/main` du moteur, DOMPurify au
profil de `sanitizeSvg`), `check-figures.mjs` et `check-overflow.mjs` du moteur passés sur les cinq
fichiers (**17 figures : 0 défaut de structure, 0 texte hors viewBox**), balayage notation (chiffres
indo-arabes, LaTeX, `\d \d{3}`, virgule arabe dans un groupe, renvoi à une lettre d'option,
« على الشكل التالي », « السؤال السابق ») : **0 occurrence**. `splitMathRuns` n'isole que « (1) » et
« (2) » (09 Q2 et Q4), rendus correctement. Longueurs : **0 clé mcq strictement la plus longue sur 15**.
Mesures des scans faites au pixel sur les PDF rendus à 300–600 dpi.

---

## 07 — 2022 ex.2 · fibres nerveuses, coupes, nerf sciatique et nerf optique (d2 practice 75/15)

| Q | type · d | ma réponse (aveugle) | clé du fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| Q1 | mcq · d1 | c | c | OK | 1 = 2 = غمد, 3 = محور ; figure fidèle |
| Q2 | multi 3/6 · d2 | a, c, e | a, c, e | réserve | recoupe Q1 (la clé de Q1 donne a, c, e) — inhérent au sujet (1أ ⇒ 1ب) |
| Q3 | mcq · d2 | b | b | OK (réserve mineure) | définitions données dans l'énoncé ; « محور الليف » ambigu (axe/axone) |
| Q4 | multi 4/6 · d2 | a, b, c, f | a, b, c, f | réserve mineure | « ألياف » objet direct sans tanwīn (a, b, e) |

**Fidélité (C04.pdf, p. 2, Document 1)**. Q1 = 1أ, Q2 = 1ب, Q3 = 1ج, Q4 = 2 : aucune sous-question
perdue. Figure refaite conforme au scan : deux rangées de cinq manchons traversés par un axone continu,
noyaux sur renflements pointus aux 2ᵉ (haut) et 4ᵉ (bas) éléments de chaque rangée **comme au scan** ;
repère 1 à deux flèches sur le **3ᵉ** élément (une au contour externe, une dans le manchon), comme au
scan ; trois cercles à double contour et point central, accolade sur le cercle haut-gauche, 2 → anneau,
3 → point. Écart minime : la pointe de la flèche 2 touche le bord EXTERNE de l'anneau (à 14,3 u du
centre pour un rayon 13) alors qu'au scan elle entre dans l'anneau — sans conséquence. Lecture de 1ج :
« حدّد في أيّ مستوى من النّسيج العصبيّ يوجد كلّ من الليفين » admet deux lectures (plan de coupe, ou
« où se trouvent ces fibres » : substance blanche / nerf) ; celle de l'auteur (plan de coupe) est
soutenue par la phrase d'ouverture « مقطعين أُنجزا في مستويين مختلفين » et rend 1ب/1ج distincts — je la
retiens. L'omission de « في مستويين مختلفين » ne rend vrai aucun distracteur (a et d sont réfutés par la
figure : le ليف (أ) montre un axone en trait, le ليف (ب) un point). Définitions des plans données dans
l'énoncé de la seule question qui les emploie (Q3) : conforme (aucun cours 01–03 ne les enseigne).

**Programme / cours** : غمد دهنيّ, محور عصبيّ, نواة (ch. 01) ; nerf mixte, sens جاذب/نابذ (ch. 01–02) ;
nerf optique rétine → cerveau (ch. 03). « العصب البصريّ … ألياف حسّيّة فقط » n'est écrit tel quel dans
aucun cours : il se déduit de l'étape 3 du ch. 03 et de la classification du ch. 01 (acceptable,
l'explication le dit).

**Étage et rampe** : 1,2,2,2 non décroissante ; d2 honnête (étiquetage, comparaison, application d'une
définition donnée — Q3 est à la limite d1/d2, la lecture spatiale point ↔ coupe transversale justifie d2).
Titre conforme (« 🏛️ مناظرة 2022 · التمرين 2 ⭐⭐: … »), n'annonce aucun résultat ; `displayOrder` 7.

**Formes** : Q1 longueurs 49/57/**56**/64 ; Q3 4×43 (plan 2×2 exact, c double erreur muette ✓) ;
Q2 vrais 78/78/83, faux 65/66/81 (b faux à 81 casse tout tri par longueur) ; Q4 vrais 31/37/74/76,
faux 65/73. Nombre de bonnes réponses non déductible de la forme (Q2 : 2 ou 3 selon la connaissance ;
Q4 : seule b/e est une paire exclusive). Aucune option étiquetée ; aucune étiquette existante ne nomme
exactement « point pris pour un noyau » ni « plans inversés » : options muettes correctes.

**Doublons** : publiés — 02/07 Q5–Q6 (L01 : عصب النّسا مزدوج, sens des fibres) recoupent 07 Q4 a, d, f
par le thème, format et énoncés différents : acceptable ; quiz/missions du ch. 01 (أغمدة دهنيّة, عصب
مزدوج) : pas de quasi-doublon. Tranche : 07 Q4 c ≈ 10 Q4 d (« le nerf optique porte la سيالة de la
rétine au cerveau ») — un énoncé commun à deux multi, acceptable.

**Fuites** : la clé et l'explication de Q1 (« الرّقمان 1 و2 يشيران إلى العنصر نفسه في الليفين: الغمد
الدّهنيّ الذي يحيط بالمحور ») donnent a, c, e de Q2 (émis juste après, d1 → d2) ; Q2 ne garde en propre
que la continuité de l'axone (b/c). C'est la redondance du sujet officiel (1أ étiqueter ⇒ 1ب « mêmes
constituants »), pas une maladresse de rédaction : à arbitrer, pas de correctif imposé. L'explication de
Q3 (« والعنصران نفسهما موجودان في الرّسمين ») redit Q2 a — sens rétrograde, sans effet sur la route quête.

### Défauts 07

- **Mineur — Q4 a, b, e (langue)** : objet direct indéterminé sans tanwīn.
  a « يضمّ عصب النّسا ألياف حسّيّة وألياف حركيّة » → « يضمّ عصب النّسا أليافًا حسّيّة وأليافًا حركيّة » ;
  b « يضمّ العصب البصريّ ألياف حسّيّة فقط » → « يضمّ العصب البصريّ أليافًا حسّيّة فقط » ;
  e « يضمّ العصب البصريّ ألياف حسّيّة وألياف حركيّة، فهو مزدوج مثل عصب النّسا » → « يضمّ العصب البصريّ أليافًا
  حسّيّة وأليافًا حركيّة، فهو مزدوج مثل عصب النّسا ». (Le publié 01 écrit déjà « يحمل أليافا حسّيّة ».)
  Longueurs après correctif : vrais 32/39/74/76, faux 67/73 — aucun indice créé.
- **Mineur — Q3 (clarté)** : « المقطع الطّوليّ مستواه موازٍ لمحور الليف، والمقطع العرضيّ مستواه عموديّ على
  محوره » — « محور » est aussi le mot du cours pour l'axone (محور عصبيّ, options de Q1). Remplacer par
  « المقطع الطّوليّ مستواه موازٍ لطول الليف، والمقطع العرضيّ مستواه عموديّ على طوله. » (même sens, plus
  d'homonymie ; aucune option ne change).
- **Mineur — Q1 explication (piège mal diagnostiqué)** : « عكس العنصرين لأنّ المحور هو الأغمق في الرّسم
  فيُسمّى غمدًا » ne décrit aucun mécanisme (pourquoi le plus sombre serait-il « la gaine » ?). Remplacer la
  phrase du piège par : « الخطأ الشّائع: عكس العنصرين، أي تسمية الحلقة محورًا والنّقطة السّوداء غمدًا، مع أنّ
  الغمد هو الذي يحيط بالمحور ؛ أو تسمية العنصر 3 نواة، والمحور امتداد طويل للخليّة العصبيّة وليس نواة. »
- **Mineur — figures Q1–Q3 (règle « arabe seulement dans `<title>` »)** : les `<text>` « أ » et « ب » sont
  de l'arabe dans le dessin (aucune figure SVT publiée sur `origin/main` n'en contient). Retirer ces deux
  `<text>` (sans rien déplacer, accolades conservées) et dire la position dans l'énoncé : Q1 « تمثّل الوثيقة
  التّالية رسمين مبسّطين لليفين عصبيّين من النّسيج العصبيّ: الليف (أ) في الجهة اليمنى من الرّسم والليف (ب) في
  الجهة اليسرى، وقد رُقّمت فيهما ثلاثة عناصر. ما البيانات الصّحيحة للأرقام 1 و2 و3؟ » ; Q2 et Q3 : insérer
  « (الليف (أ) في الجهة اليمنى من الرّسم والليف (ب) في الجهة اليسرى) » après la première mention des fibres.

**Verdict 07 : réserve mineure** (0 clé fausse, 0 défaut majeur ; 4 mineurs ; redondance Q1→Q2 signalée,
inhérente au sujet).

---

## 08 — 2020 ex.2 · arc réflexe et voie visuelle : récepteur, centre, trajets (d2 practice 75/15)

| Q | type · d | ma réponse (aveugle) | clé du fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| Q1 | mcq · d1 | d | d | OK (réserve mineure) | distracteur a éliminé par la légende de l'énoncé (« 4: العينان » est en (ب)) |
| Q2 | matching 6 · d2 | l1-r5 l2-r3 l3-r2 l4-r6 l5-r4 l6-r1 | idem | **défaut majeur** | l'énoncé renvoie à « الجدول المطلوب », tableau absent de la question |
| Q3 | mcq · d2 | a | a | OK | plan 2×2 exact (b double muette), étiquette d exacte |
| Q4 | multi 3/6 · d2 | a, b, e | a, b, e | **défaut majeur** | trois paires miroir (a/d, b/f, c/e) : le nombre 3 se déduit ; dans chaque paire la clé est la plus longue et la plus détaillée ; les 3 clés = les 3 options les plus longues |

**Fidélité (C06.pdf, p. 2, Document 1)**. Q1 = 1 (titres), Q2 + Q3 = 2 (tableau 4 lignes × 2 : six cases
en appariement, le centre en mcq), Q4 = 3 (« جسّم بلونين … ») : aucune case perdue. Figure (أ) conforme au
scan : coupe de moelle à substance grise en papillon, racine dorsale avec ganglion (petit ovale noir) qui
entre dans la corne dorsale jusqu'à la خليّة رابطة (petit cercle, dans la corne dorsale), motoneurone étoilé
dans la corne ventrale d'où part la racine ventrale, tronc commun, fibre vers la peau (point récepteur) et
fibre vers le muscle (terminaison ramifiée) — tout y est, coordonnées vérifiées (خليّة رابطة à
(79,73) dans la corne dorsale, étoile à (88,101) dans la corne ventrale). Figure (ب) conforme : deux yeux,
arc sombre au fond (rétine), nerfs croisés en X, terminaisons sur des zones bleues ; le scan dessine des
hémisphères beiges, l'auteur des arcs beiges — simplification admissible. Les deux panneaux, côte à côte
au scan, sont empilés et l'énoncé le dit. Légendes arabes → repères 1–4 avec légende dans l'énoncé de Q1
(conforme au scan : جلد، عضلة، خليّة عصبيّة رابطة، عين) ; **Q2–Q4 sans repères** (point 4 de l'auteur) :
perte d'information réelle mais sans effet sur la résolubilité (les options de Q2 nomment peau, rétine,
nerfs ; Q3–Q4 se résolvent par la structure et le cours). Facultatif : remettre la figure de Q1 et sa
ligne de légende dans Q2–Q4 (le repère 3 sur la moelle oriente Q3, mais le scan officiel le porte aussi).

**Programme / cours** : الفعل الانعكاسيّ/الإراديّ (ch. 01–02), منبّه، مستقبل، ناقل، مركز (ch. 02), voie
visuelle et مراكز الإبصار (ch. 03). Rien de non enseigné ; le chiasma dessiné n'est jamais interrogé.

**Étage et rampe** : 1,2,2,2 ; d2 honnête. Titre conforme ; `displayOrder` 8.

**Formes** : Q1 47/45/53/**47** ; Q3 **51**/42/51/42 (a et c à 51 : clé non strictement la plus longue) ;
Q2 : chaque élément de droite a deux partenaires plausibles (même dessin, catégorie voisine) — appariement
unique, non devinable par simple élimination ✓. Étiquettes : 08 Q1 b `bio.nerv.reflexe-pris-pour-volontaire`
exacte (titrer « إراديّ » l'arc réflexe) ; 08 Q3 d `bio.nerv.cerveau-dans-l-arc-reflexe` exacte. Muettes
correctes : Q1 a, c ; Q3 b (double), c.

**Doublons** : missions et quiz publiés du ch. 02 (ordre des éléments de l'arc, سيالة جاذبة/نابذة) et du
ch. 03 (quiz Q9 « أين توجد مراكز الإبصار ») : même vocabulaire, aucune question quasi identique.

**Fuites** : l'explication de Q1 (« مسار الخبر البصريّ من العينين إلى منطقة من الدّماغ ») donne la moitié (ب)
de Q3 (émis après, d1 → d2) ; c'est déjà impliqué par la clé de Q1 (« الإبصار »), inhérent au sujet : Q3
teste en propre la moitié (أ) (moelle / cerveau), qui porte l'étiquette. Les explications de Q2 et Q3
redisent des définitions (le ناقل حسّي porte vers le centre ; le centre émet la سيالة حركيّة) que Q4 interroge :
recoupement de cours, pas de clé non triviale livrée.

### Défauts 08

- **MAJEUR — Q2 (autonomie)** : « أنسب كلّ عنصر من الجدول المطلوب إلى ما يوافقه في الرّسم المعنيّ » renvoie au
  tableau du sujet officiel, absent de la question. Remplacer la seconde ligne de l'énoncé par :
  « أنسب كلّ عنصر من العناصر التّالية إلى ما يوافقه في الرّسم المعنيّ. » (rendu Chromium vérifié ; aucune
  option ni paire ne change).
- **MAJEUR — Q4 (indice de forme, multi)** : vrais a 86 · e 80 · b 70 ; faux d 69 · f 69 · c 65 → trier par
  longueur rend la clé ; les paires a/d, b/f, c/e (une vraie par paire) rendent le compte 3 ; la clé porte
  dans sa paire le détail en plus (« من المستقبلات الحسّيّة للجلد », « وحده، ») et c est la seule option à
  l'indéfini (« سيالة عصبيّة حركيّة »). Correctif (vérifié par script et Chromium) — clé `["a","b","d","e"]` :
  - a « في الرّسم (أ) تنتقل السّيالة العصبيّة الحسّيّة من الجلد نحو المركز العصبيّ » (V, 68)
  - b inchangée « في الرّسم (أ) تنتقل السّيالة العصبيّة الحركيّة من المركز العصبيّ نحو العضلة » (V, 70)
  - c « في الرّسم (ب) تنتقل السّيالة العصبيّة الحركيّة من المركز العصبيّ نحو العينين » (F, 71)
  - d « في الرّسمين معًا تنشأ السّيالة العصبيّة الحسّيّة في مستقبلات حسّيّة » (V, 59 — remplace l'ancien d)
  - e « في الرّسم (ب) تنتقل السّيالة العصبيّة الحسّيّة من العينين نحو المركز العصبيّ » (V, 70)
  - f inchangée « في الرّسم (أ) تنتقل السّيالة العصبيّة الحركيّة من الجلد نحو المركز العصبيّ » (F, 69)
  Vrais 59/68/70/70 (moy. 66,8), faux 69/71 (moy. 70) ; 4/6, plus de partition en paires exclusives
  (c et e ne s'excluent plus logiquement : il faut savoir que (ب) n'a pas de trajet moteur) ; aucune
  prémisse niée ; d vrai par les cours 02 (« الوخز يُنبّه المستقبلات الحسّيّة ») et 03 (étape 2), ne nomme ni la
  peau ni la rétine (pas de fuite vers Q2). Explication de remplacement : « في الرّسم (أ) مساران: السّيالة
  الحسّيّة جاذبة، تنشأ في مستقبلات الجلد وتتّجه نحو المركز العصبيّ ؛ والسّيالة الحركيّة نابذة، تبدأ من المركز
  العصبيّ وتتّجه نحو العضلة التي هي العضو المنفّذ. وفي الرّسم (ب) تتّجه السّيالة الحسّيّة من العينين نحو
  المركز العصبيّ، ولا يظهر فيه مسار حركيّ لأنّه لا عضو منفّذ فيه. ففي الرّسمين معًا تنشأ السّيالة الحسّيّة في
  مستقبلات حسّيّة يُنبّهها المنبّه. ولا تسير السّيالة الحركيّة من الجلد نحو المركز، فتلك وجهة السّيالة الحسّيّة.
  الخطأ الشّائع: عكس اتّجاه السّيالتين الحسّيّة والحركيّة ؛ أو رسم مسار حركيّ في الرّسم (ب) ولا عضو منفّذ فيه. »
- **Mineur — Q1 a (distracteur éliminé à vue)** : « الرّسم (أ): الإبصار ؛ الرّسم (ب): الفعل الانعكاسيّ » est
  réfuté par l'énoncé lui-même (« الرّقم 4: العينان » est dans (ب), la peau et le muscle dans (أ)). Remplacer a par
  « الرّسم (أ): الفعل الانعكاسيّ ؛ الرّسم (ب): الفعل الانعكاسيّ » (muette). Grille recomptée : (أ) انعكاسيّ a, d /
  إراديّ b, c ; (ب) انعكاسيّ a, c / إبصار b, d — chaque valeur deux fois ; c reste la double erreur muette ; b
  garde son étiquette ; clé d (47) non la plus longue (a 55, c 53, b 45). Dans l'explication, remplacer
  « ؛ أو عكس العنوانين. » par « ؛ أو عدّ الرّسم السّفليّ فعلًا انعكاسيًّا، وهو مسار إحساس شعوريّ: الإبصار. »
  (ne dit rien du trajet moteur : pas de fuite vers Q4).
- **Mineur — figures Q1–Q4 (arabe hors `<title>`)** : retirer les `<text>` « أ » et « ب » (les énoncés disent déjà
  « الرّسم (أ) في الأعلى والرّسم (ب) في الأسفل »), sans rien déplacer.
- **Mineur — style** : « يمثّل الرّسم رسمين مبسّطين » (le dessin représente deux dessins) → « تمثّل الوثيقة رسمين
  مبسّطين » dans les quatre énoncés.

**Verdict 08 : défaut majeur** (2 majeurs : Q2, Q4 ; 0 clé fausse).

---

## 09 — 2026 ex.3 · téléphone et œil : défaut, image, lentille, iris (d3 boss 120/30)

| Q | type · d | ma réponse (aveugle) | clé du fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| Q1 | mcq · d2 | b | b | OK (réserve) | figure : changement reporté de la cornée au globe (voir fidélité) |
| Q2 | mcq · d2 | d | d | OK | pas un plan 2×2 (axe « loin » à trois valeurs), sans fuite de clé |
| Q3 | mcq · d2 | a | a | **défaut majeur** | d nie la prémisse « عينًا سليمة (الرّسم 1) » (image devant la rétine dans l'œil sain) ; 3 cases changées |
| Q4 | matching 3 · d3 | l1-r1 l2-r2 l3-r3 | idem | réserve mineure | paire l1–r1 imposée, l2/l3 complémentaires : une seule décision binaire → d2 réel |
| Q5 | mcq · d3 | d | d | OK | rôle de l'iris conforme au cours (الحدقة تتّسع في الظّلام) |

**Fidélité — figure (C01.pdf, p. 2, Document 2), mesurée au pixel (400 dpi) puis superposée sur le
cristallin.** Scan, avant → après, sur l'axe : longueur totale apex cornéen → fond du globe 512 → 542 px
(**+5,9 %**) ; apex cornéen → face antérieure du cristallin 80 → 107 (**+34 %**) ; cristallin 45 → 46 ;
face postérieure du cristallin → fond du globe 387 → 389 (**+0,5 %**) ; hauteur du globe 462 → 455. Le
dessin officiel montre donc **une cornée nettement plus bombée, le globe proprement dit inchangé** (les
contours postérieurs se superposent). Figure de l'auteur (calcul sur le SVG) : longueur totale 88 → 100,5
(**+14,2 %**) ; ellipse sclérale rx 40 → 44,5 (+11,3 %) ; segment antérieur 22,2 → 25,7 (+15,8 %) ;
segment postérieur 54,2 → 63,2 (**+16,6 %**) ; hauteur 80 → 80. L'auteur a donc **déplacé le changement de
la cornée vers le fond du globe** et atténué le bombement cornéen ; sa mesure déclarée « ≈ +7 % sur le
scan » pour l'allongement du globe est inexacte (les +6 % du scan sont entièrement cornéens). Effet sur
les clés : aucun — « القطر الأماميّ الخلفيّ ازداد » est vrai sur le scan (+5,9 %) comme sur la figure — et le
choix aligne la figure sur la seule cause enseignée (allongement), la courbure de la cornée n'étant pas une
cause du cours. Réserve de fidélité à consigner (ou à arbitrer), pas de correctif de clé.

**Points demandés par l'auteur.** (1) Cornée citée « en renfort » dans l'explication de Q1 : acceptable,
à condition de la rattacher au cours (le laser « يجعل الجزء المركزي من القرنيّة أكثر تسطّحًا ») — correctif
mineur ci-dessous. (2) « شمعة بعيدة » : ajout nécessaire, pas une déformation : sans lui, l'œil myope peut
former sur la rétine l'image d'un objet proche, et la clé ne serait plus unique ; le cours ne place
« أمام الشّبكيّة » que l'image des objets éloignés. La bougie est dessinée près de l'œil (schéma non à
l'échelle) : sans effet sur la réponse. Énoncé officiel 3 (« بالاعتماد على دور القزحيّة ») fidèlement repris
en Q5 ; la phrase officielle sur les rayons qui « تخترق الأوساط الشفّافة … وتُحدث تلفًا » est redonnée.
4e sous-question (« type de lentille ») : l'ajout d'une « عين ثالثة » plus courte ne déforme rien (la paire
officielle l2–r2 est là) ; il ajoute l'hypermétropie, enseignée.

**Programme / cours** : causes et propriétés de قصر/طول البصر, position de l'image, image renversée,
lentilles, rôle de l'iris et de la pupille (ch. 03) : tout est enseigné ; ni accommodation, ni sens de
lecture de la pupille hors cours.

**Étage et rampe** : 2,2,2,3,3 non décroissante. Q4 est un d2 réel (la paire saine est donnée par
« لا تحتاج إلى عدسة تصحيحيّة », puis savoir une des deux lentilles donne l'autre) ; Q1–Q3 sont des lectures
de figure + rappel (d2 francs) ; seule Q5 enchaîne deux notions (pupille dilatée à l'obscurité → plus de
rayons → plus de cellules lésées). Avis : **en-tête d3/boss généreux** — d2/practice 75/15 serait l'étage
honnête (rampe 2,2,2,2,3) ; à défaut, garder d3 en retaguant Q4 d2 (rampe 2,2,2,2,3, une seule question
d3 : à arbitrer). Titre conforme, n'annonce pas « قصر البصر » ; `displayOrder` 9.

**Formes et étiquettes** : longueurs Q1 45/**47**/47/45, Q2 38/40/39/**38**, Q3 **82**/81/82/82, Q5 92/91/88/**91** :
aucune clé strictement la plus longue. Q1 : plan 2×2 exact (d double erreur muette ✓). Q2 : l'axe « loin »
a trois valeurs (يرى بوضوح a ; لا يرى بوضوح b, d ; لا يرى إطلاقًا c) — la valeur majoritaire est celle de la
clé, l'axe « près » est à égalité : le vote ne rend pas la clé ; a (deux cases inversées) porte
`myopie-hypermetropie-inversees`, légitimement (c'est UNE erreur, la propriété du طامس) — il n'y a pas
d'« option à deux erreurs muette » dans cette question, contrairement à ce que dit l'auteur. Étiquettes :
Q1 c, Q2 a, Q3 b `bio.vis.myopie-hypermetropie-inversees` exactes ; Q3 c `bio.vis.image-redressee-par-l-oeil`
exacte. Q1 a (قصر البصر + القطر نقص) muette : défendable (erreur de lecture ou d'association, ambiguë).

**Doublons** : quiz Q6 et 03/03 Q1–Q4, 03/06 Q1 (même notion, données chiffrées ou verbales) ; 03/02 Q4
(pupille à l'obscurité) : pas de quasi-doublon. Avec 11 : 09 Q1 ≈ 11 Q2 (même gabarit 2×2 défaut × raison,
même étiquette sur « طول البصر … القطر … أكبر ») et 09 Q4 ≈ 11 Q6 (قصر → مفرّقة) — annales voisines qui
recyclent la notion, figures et options différentes : recoupement acceptable, à ne pas étendre.

**Fuites** : les explications de Q2, Q3, Q4 redisent « العين في الرّسم 2 أطول » (ce que montre la figure) ;
aucune explication ne livre une clé suivante : Q1 ne dit ni la propriété près/loin, ni la position de
l'image, ni la lentille ; Q2 ne dit ni l'image ni la lentille ; Q3 ne nomme aucune lentille.

### Défauts 09

- **MAJEUR — Q3 d (prémisse niée)** : « يتشكّل الخيال في الرّسم 1 أمام الشّبكيّة وفي الرّسم 2 خلف الشّبكيّة،
  وهو معتدل في الرّسمين » place devant la rétine l'image d'un œil que l'énoncé déclare sain : éliminée à vue,
  et elle change trois cases (le plan 2×2 annoncé n'existe pas). Remplacer d par « يتشكّل الخيال في الرّسم 1
  على الشّبكيّة وفي الرّسم 2 خلف الشّبكيّة، وهو معتدل في الرّسمين » (muette). Grille recomptée : رسم 1 = على
  dans les quatre (donné par la prémisse) ; رسم 2 أمام a, c / خلف b, d ; مقلوب a, b / معتدل c, d — chaque valeur
  deux fois ; d devient la double erreur muette ; longueurs 82/81/82/81 (clé non strictement la plus longue) ;
  l'explication actuelle couvre déjà les deux erreurs.
- **Mineur — Q3 énoncé (langue)** : « يمثّل الرّسمان عينًا سليمة (الرّسم 1) وعينها نفسها بعد استعمال مفرط… »
  (« son œil à elle-même ») → « يمثّل الرّسمان عينًا سليمة (الرّسم 1) والعينَ نفسها بعد استعمال مفرط للهاتف
  الجوّال (الرّسم 2)، وعلى محور كلّ منهما شمعة بعيدة. » (rendu vérifié ; « (1) »/« (2) » non concernés).
- **Mineur — Q4 (difficulté)** : retaguer `difficulty` 2 (rampe 2,2,2,2,3, ordre inchangé) ; voir l'avis
  d'étage ci-dessus.
- **Mineur — Q1 explication (point 1)** : remplacer « وتبدو القرنيّة أكثر تحدّبًا قليلًا، وهو ما يعزّز الحكم نفسه. »
  par « وتبدو القرنيّة أكثر تحدّبًا قليلًا، وهو ما يعزّز الحكم نفسه: فالإصلاح الحديث لقصر البصر يجعل الجزء
  المركزيّ من القرنيّة أكثر تسطّحًا. » (rattache le renfort au tableau du cours ; ne livre ni lentille ni
  propriété).
- **Mineur — Q2 explication (phrase bancale)** : « وليست هذه الخاصّيّة هي المعاكسة، فالإبصار الجيّد عن بعد وغير
  الواضح عن قرب يخصّ العين التي نقص قطرها. » → « أمّا الإبصار الجيّد عن بعد وغير الواضح عن قرب فخاصّيّة العين
  التي نقص قطرها. »
- **Mineur — fidélité figure (déclaration)** : corriger la note de livraison : le scan montre une cornée plus
  bombée (+34 % de profondeur antérieure) et un globe postérieur inchangé (+0,5 %) ; la figure de l'auteur
  allonge le segment postérieur de 16,6 % (total +14,2 %, et non +11 %).

**Verdict 09 : défaut majeur** (1 majeur : Q3 d ; 0 clé fausse).

---

## 10 — 2025 ex.4 · perte de la vision de l'œil gauche : hypothèses, examens, rétine, nerf (d3 boss 120/30)

| Q | type · d | ma réponse (aveugle) | clé du fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| Q1 | mcq · d2 | b | b | **défaut majeur** | a et d proposent « مراكز الإبصار », déclarés sains par l'énoncé ; a propose aussi le cristallin (milieu transparent déclaré sain) : la question se réduit à « la cornée est-elle un milieu transparent ? » |
| Q2 | mcq · d3 | c | c | OK | vrai d3 (suffisance d'une preuve) ; étiquettes exactes |
| Q3 | mcq · d3 | a | a | OK (réserve mineure) | d « … في المخّ » se réfute par sa propre formulation |
| Q4 | multi 4/6 · d3 | a, b, d, f | a, b, d, f | OK (réserve mineure) | b, d (et f) déjà énoncés par les explications de Q2/Q3 — chaînage du sujet |

**Fidélité (C02.pdf, p. 3 ; transcription 2025.md, ex.4)**. Pas de figure : les deux tableaux officiels
sont redonnés en lignes de texte (Q2) et en prose (Q3, Q4), mot pour mot quant au sens (« عدم وجود سيالة »
→ « لا توجد سيالة », « انفصال تامّ للشبكيّة », « شبكيّة سليمة وفي موقعها الأصليّ », « فحصا إضافيّا أظهر سلامة العصب
البصريّ المتّصل بالعين اليسرى »). Q1 = 1 (deux hypothèses → couples, prémisse officielle gardée), Q2 = 2,
Q3 = 3 (« استنتج سبب فقدان البصر » reformulé en « quel rôle la rétine gauche n'assure plus » : la cause —
le décollement — étant dans l'énoncé, la question porte sur le mécanisme ; reformulation fidèle à
l'intention), Q4 = 4. Rien de perdu.

**Programme / cours** : milieux transparents (dont cornée et cristallin), مراكز الإبصار, rôle de la
rétine, de l'iris, du cerveau, quatre étapes du إبصار (ch. 03) ; démarche « une seule différence »
(ch. 02). Rien de non enseigné.

**Étage et rampe** : 2,3,3,3. Q2 est un vrai d3 ; Q3 est un d3 de justesse (une fois les données lues, c'est
le rôle de la rétine contre trois autres rôles) ; Q4 rappelle les quatre étapes (tout-ou-rien sur 6
énoncés). Retaguer Q3 en d2 la ferait émettre AVANT Q2, et son énoncé (« فحص إضافيّ », décollement) livrerait
alors la conclusion de Q2 : garder l'ordre et l'étage. En-tête d3/boss : justifié par Q2. Titre conforme
(« فرضيّات وفحصان ومراحل الإبصار » : notions, pas de résultat) ; `displayOrder` 10.

**Formes et étiquettes** : longueurs Q1 69/**50**/50/63, Q2 48/60/**50**/68, Q3 **44**/44/51/49 ; Q4 vrais
60/67/75/91, faux 69/86 : aucun indice de longueur ; nombre de bonnes réponses non déductible de la forme
(b/c et a/e exclusives, d et f indépendantes). Q2 a, b, d `bio.demarche.cause-sans-temoin` : exactes (l'œil
droit sert de témoin mais diffère de l'œil gauche par deux facteurs possibles — rétine ou nerf — : aucun
des deux ne peut être accusé ; d « ترجّح » aussi une cause sans comparaison valable). Muettes : Q1 a, c, d ;
Q3 b, c, d (aucune étiquette existante ne nomme « rôle d'un autre maillon attribué à la rétine »).

**Doublons** : 10 Q3 reprend le menu de rôles du quiz Q1 et de 01-tamrin Q2 publiés (« تحويل الضّوء إلى سيالة »,
« تعديل كمّيّة الضّوء … الحدقة », « تجميع الأشعّة ») avec un autre organe et une autre clé : gabarit miroir à
travers le chapitre, pas de clé livrée — acceptable, à ne pas multiplier. 10 Q4 ≈ 03/03 Q5 publié (les
quatre étapes, en ordre) : même contenu, format différent — acceptable. 10 Q4 d ≈ 07 Q4 c (tranche).

**Fuites (point 5 de l'auteur)** : l'énoncé de Q2 redonne mot pour mot les deux hypothèses = la clé de Q1
(sens rétrograde, inévitable : c'est la donnée de Q2). L'explication de Q2 (« عند تسليط الضّوء تنشأ السّيالة
في الشّبكيّة ثمّ ينقلها العصب البصريّ ») énonce la clé de Q3 et les énoncés b, d de Q4, émis après — chaînage
inhérent au sujet (10 Q2 → Q3), sans rédaction possible qui l'évite. L'explication de Q3 ajoute f
(« وتحليل السّيالة عمل مراكز الإبصار بالمخّ ») et réfute c : là, la fuite est évitable. L'affirmation de
l'auteur « aucune clé de multi n'est reprise telle quelle » est vraie à la lettre, pas en substance : Q4 ne
garde en propre que a/e (et f si l'on corrige Q3).

### Défauts 10

- **MAJEUR — Q1 (prémisse niée par deux distracteurs)** : a « تلف الجسم البلّوريّ الأيسر، أو تلف مراكز الإبصار
  بالجهة الخلفيّة من المخّ » et d « تلف الشّبكيّة اليسرى، أو تلف مراكز الإبصار … » proposent ce que l'énoncé
  déclare sain (l'explication le dit : « وقد قيل إنّها سليمة ») ; ils s'éliminent à vue, il ne reste que b/c.
  Correctif (grille recomptée case par case, prémisse gardée vraie, aucune option ne la nie) :
  - a « تلف القزحيّة اليسرى، أو تلف العضلات المحرّكة للعين اليسرى » (double erreur, muette)
  - b inchangée (clé) « تلف الشّبكيّة اليسرى، أو تلف العصب البصريّ المتّصل بها »
  - c « تلف القزحيّة اليسرى، أو تلف العصب البصريّ المتّصل بها »
  - d « تلف الشّبكيّة اليسرى، أو تلف العضلات المحرّكة للعين اليسرى »
  1ʳᵉ case : الشّبكيّة b, d / القزحيّة a, c ; 2ᵉ case : العصب b, c / العضلات a, d — chaque valeur deux fois.
  Longueurs 55/50/50/55 (clé non la plus longue). Iris (« تعدّل كمّيّة الضّوء ») et muscles (« تربط العين
  بالمحجر وتوجّهها ») sont au cours ; leur lésion ne prive pas la rétine de lumière : hypothèses fausses, non
  exclues par la prémisse, réfutables seulement par le savoir. Explication de remplacement : « بما أنّ الأوساط
  الشّفّافة والمركز العصبيّ للإبصار في حالة جيّدة، فالعطب يمسّ ما بينهما على مسار الإبصار: الشّبكيّة اليسرى أو
  العصب البصريّ المتّصل بها، وهما الفرضيّتان اللّتان يمكن اختبارهما. أمّا القزحيّة فتعدّل كمّيّة الضّوء الدّاخل
  فقط، والعضلات توجّه العين فقط: تلفهما لا يمنع الضّوء من بلوغ الشّبكيّة. الخطأ الشّائع: اقتراح عنصر من العين لا
  يقع على مسار الإبصار، لأنّ الحادث أصاب العين. » (ne dit pas le rôle de la rétine : pas de fuite vers Q3/Q4 ;
  rendu Chromium vérifié).
- **Mineur — Q3 d (se réfute par sa formulation)** : « تحليل السّيالة العصبيّة في المخّ والتّعرّف على الأشياء »
  ne peut pas être un rôle de la rétine puisqu'il est situé « في المخّ ». → « تحليل السّيالة العصبيّة الحسّيّة
  والتّعرّف على الأشياء » (48 car. ; clé a 44, b 44, c 51 : pas d'indice).
- **Mineur — Q3 explication (fuite évitable vers Q4 f)** : remplacer « وتحليل السّيالة عمل مراكز الإبصار بالمخّ »
  par « وتحليل السّيالة ليس من عمل الشّبكيّة » ; et « فإذا عجزت عن ذلك لم تنشأ سيالة، ولم يجد العصب السّليم ما
  ينقله، فغابت السّيالة في مستواه وغاب الإبصار » par « فإذا عجزت عن ذلك لم تنشأ سيالة، فغابت في العصب السّليم
  وغاب الإبصار » (le reste inchangé ; Q4 garde alors a/e et f en propre).

**Verdict 10 : défaut majeur** (1 majeur : Q1 ; 0 clé fausse).

---

## 11 — 2021 ex.5 · coupes de l'œil de deux jeunes, défauts de vision, correction (d3 boss 120/30)

| Q | type · d | ma réponse (aveugle) | clé du fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| Q1 | multi 3/6 · d2 | b, e, f | b, e, f | OK | comparaison (أ) : globe droit plus long, cristallins égaux, hauteurs voisines |
| Q2 | mcq · d2 | c | c | OK | plan 2×2 exact (a double muette) ; d étiquetée exactement |
| Q3 | mcq · d2 | d | d | OK | plan 2×2 exact (b double muette) |
| Q4 | multi 2/6 · d3 | b, d | b, d | OK | les deux hypothèses officielles (2ب) |
| Q5 | mcq · d3 | b | b | OK | « غير واضح عن بعد » ⇒ قصر ⇒ œil gauche (2ج) ; plan 2×2 exact |
| Q6 | mcq · d3 | c | c | OK (réserve mineure) | duel « مقطعين » pour quatre coupes |

**Fidélité — tableau de quatre dessins (C05.pdf, p. 4), mesuré à 600 dpi.** Rangée (أ) au scan : œil gauche
(sain) 463 px de l'apex cornéen au fond, œil droit 531 (**+14,7 %**), hauteurs 422/416, cristallins 39/38
(égaux). Auteur : 79,0 → 93,0 (**+17,7 %**, légère accentuation), hauteurs 72/70, cristallins rx 4,2/4,2 —
fidèle. Rangée (ب) au scan : longueurs 484/482 (égales), cristallin gauche 72–75 px contre 49–51 à droite :
rapport **1,46** dans la rangée ; le cristallin droit de (ب) est lui-même ~28 % plus épais que ceux de (أ)
(rapport gauche (ب) / (أ) = 1,87). Auteur : longueurs 83/83, cristallin gauche rx 8 contre 4,2 (rapport
**1,90**, contour compris 1,78), cristallin droit de (ب) identique à ceux de (أ). L'accentuation (1,46 →
1,9) sert la lisibilité à 232 px et ne change aucune clé, mais la mesure déclarée « ≈ 1,8 sur le scan » est
le rapport gauche (ب) / (أ), pas le rapport gauche/droit de la rangée (ب) que la question compare (1,46) :
à corriger dans la note de livraison. Dispositions conformes : cornée à gauche, œil droit dans la colonne
de droite comme au scan, chaque question redonne sa figure (rangée (أ) pour Q1–Q2, (ب) pour Q3–Q5, les deux
pour Q6). Six sous-questions officielles (1أ, 1ب, 2أ, 2ب, 2ج, 3) → six questions ; « الطّرق المناسبة » réduit au
type de verre, le laser n'étant cité qu'en explication de Q6 : réduction acceptable (rien de faux).

**Point 3 de l'auteur** : oui, c'est la logique du sujet — 2ب « أدلِ بالفرضيّات الممكنة » : (œil gauche, cristallin
trop bombé ⇒ قصر) ou (œil droit, cristallin pas assez bombé ⇒ طول) ; 2ج « غير واضح عن بعد » ⇒ قصر ⇒ la première.
**Point 5** : vérifié — aucune explication émise avant Q5 (Q1–Q4) ne donne la propriété près/loin (Q2 dit
« يتشكّل الخيال أمامها: هذا هو قصر البصر », sans distance) ; aucune clé de multi n'est reprise telle quelle
plus tôt : l'explication de Q3 (émise avant Q4) donne la LECTURE de la rangée (ب) (même longueur, cristallin
gauche plus épais), qui écarte c et e de Q4 — c'est la donnée de 2أ, chaînage inhérent ; Q4 garde en propre
l'association cause ↔ défaut (a/f contre b/d).

**Programme / cours** : causes (القطر الأماميّ الخلفيّ, تحدّب الجسم البلّوريّ), propriétés, lentilles, laser
(ch. 03) : tout est enseigné. « القطر العموديّ » (Q1 f) est une lecture géométrique, sans notion nouvelle.

**Étage et rampe** : 2,2,2,3,3,3 non décroissante ; d3 honnête (Q4, Q5, Q6 combinent lecture, cause et
propriété ou deux diagnostics). Titre conforme (notions seulement) ; `displayOrder` 11.

**Formes et étiquettes** : longueurs Q2 74/74/**73**/73, Q3 83/83/80/**80**, Q5 4×30, Q6 41/24/**25**/41 ;
Q1 vrais 33/42/61, faux 51/61/67 ; Q4 vrais 59/61, faux 59/61/68/70 : aucun indice. Plans 2×2 recomptés :
Q2 (قصر b, c / طول a, d ; عدسة a, b / قطر c, d), Q3 (قطر أكبر a, b / متقارب c, d ; يسرى a, d / يمنى b, c), Q5
(يمنى a, d / يسرى b, c ; قصر a, b / طول c, d), Q6 ((أ) لامّة a, b / مفرّقة c, d ; (ب) مفرّقة a, c / لامّة b, d) :
chaque valeur deux fois, double erreur muette (Q2 a, Q3 b, Q5 d, Q6 b). Étiquettes
`bio.vis.myopie-hypermetropie-inversees` sur Q2 d, Q5 c, Q6 a, Q6 d : exactes (en Q6, l'autre moitié de
chaque option montre que l'élève connaît la lentille du قصر : l'erreur exécutée est bien l'inversion du
défaut — œil long ou flou de loin pris pour du طول). Q4 : six énoncés homogènes, compte 2 non déductible de
la forme. Q2 b et Q3 a, muettes : voir la famille (a) ci-dessous.

**Doublons** : 11 Q2 ≈ 09 Q1 (gabarit 2×2) et 11 Q6 ≈ 09 Q4 (قصر → مفرّقة) — annales voisines, figures et
options différentes : acceptable ; 03/06 Q1 publié (2,7 cm au lieu de 2,5 → قصر, مفرّقة) et 03/03 Q4 (causes
du طول) : même notion, autre support — acceptable.

### Défauts 11

- **Mineur — Q6 énoncé (langue, duel sur quatre référents)** : « يبيّن الرّسم مقطعين أماميّين خلفيّين لعيني
  شابّين » pour une figure de quatre coupes → « يبيّن الرّسم مقاطع أماميّة خلفيّة لأعين شابّين: الصّفّ العلويّ للشّابّ (أ)
  والصّفّ السّفليّ للشّابّ (ب)، والعين اليمنى في الجهة اليمنى من الرّسم. » (suite de l'énoncé inchangée ; rendu
  vérifié) ; et dans le `<title>` de la figure, « مقطعات » → « مقاطع ».
- **Mineur — figures Q1–Q6 (arabe hors `<title>`)** : retirer les `<text>` « أ » / « ب » (sans rien déplacer) ;
  les énoncés nomment déjà le jeune et, en Q6, la rangée de chacun.
- **Mineur — fidélité (déclaration)** : rapport d'épaisseur des cristallins de (ب) : 1,46 au scan dans la
  rangée, 1,9 dans la figure ; corriger la note « ≈ 1,8 sur le scan ».

**Verdict 11 : réserve mineure** (0 majeur, 0 clé fausse).

---

## Étiquettes — placements de l'auteur et familles « manquantes » (libellés lus sur `origin/main`)

**Placements vérifiés, tous exacts** : `bio.vis.myopie-hypermetropie-inversees` 09 Q1 c, 09 Q2 a, 09 Q3 b,
11 Q2 d, 11 Q5 c, 11 Q6 a et d ; `bio.vis.image-redressee-par-l-oeil` 09 Q3 c ;
`bio.nerv.reflexe-pris-pour-volontaire` 08 Q1 b ; `bio.nerv.cerveau-dans-l-arc-reflexe` 08 Q3 d ;
`bio.demarche.cause-sans-temoin` 10 Q2 a, b, d. Aucune option à deux erreurs n'est étiquetée (09 Q2 a change
deux cases mais exécute UNE erreur, la propriété du طامس : étiquette légitime). Aucune option muette ne
mériterait une étiquette existante (vérifié sur les 15 mcq ; multi et matching non étiquetables).

**Familles signalées par l'auteur — comptées par grep sur la tranche + les 151 fichiers SVT de `origin/main`** :

- **(a) « cause du cours invoquée que le document ne montre pas »** — au sens strict (le libellé proposé par
  l'auteur, « Tu invoques une cause vue en cours… ») : 11 Q2 b, 11 Q4 c et e → **2 questions** ; publié : 0.
  Sous ce libellé, la famille reste **muette** (et 11 Q3 a, qui n'invoque aucune cause, n'y entrerait pas).
  Au sens large « différence lue entre les deux dessins qu'ils ne montrent pas » : 11 Q1 a, 11 Q2 b, 11 Q3 a,
  11 Q4 c/e → **4 questions** (une seule mission) ; publié : aucune option mcq (02/08 Q4 e et 05/08 Q6 d sont
  des lectures inversées dans des multi, non étiquetables). Elle atteint le seuil : **étiquette nouvelle
  recommandée sous un libellé élargi**, qui nomme exactement l'erreur des deux placements mcq :
  - id `bio.vis.difference-non-montree`
  - fr « Tu lis entre les deux dessins une différence qu'ils ne montrent pas : compare-les élément par élément
    (longueur du globe, épaisseur du cristallin) avant de conclure. »
  - en « You read a difference between the two drawings that they do not show: compare them part by part
    (eyeball length, lens thickness) before concluding. »
  - ar « تقرأ بين الرّسمين فرقًا لا يُظهرانه: قارن بينهما عنصرًا عنصرًا (طول الكرة، سمك الجسم البلّوريّ) قبل أن
    تستنتج. »
  - placements : **11 Q2 b**, **11 Q3 a** ; aucun placement publié à reprendre. (11 Q3 c — œil inversé — et
    09 Q1 a — lecture « نقص » — restent muettes : mécanisme différent ou ambigu.)
- **(b) « sens de la pupille inversé »** : 09 Q5 a + 03/05-tadrib Q5 a publié → **2 questions** (aucune autre
  dans le corpus SVT) → **muette**, d'accord avec l'auteur.
- **(c) « rôle d'un autre maillon attribué à la rétine »** : 10 Q3 (b, c, d) seulement → **1 question**.
  09 Q5 c n'en est pas : elle prête à l'IRIS le rôle de rassembler les rayons (milieux transparents), pas un
  rôle à la rétine — le compte de l'auteur (2) est erroné. Les publiés quiz Q5 a et 03/02 Q2 b (« la rétine
  redresse l'image ») portent déjà l'étiquette exacte `image-redressee-par-l-oeil`. → **muette**.

## Doublons — synthèse

- Avec les missions publiées du ch. 03 : notions partagées (quiz Q6, 03/03, 03/06 Q1, 03/02 Q4, 03/03 Q5),
  aucun quasi-doublon (supports, options, pièges différents). 10 Q3 reprend en miroir le menu de rôles du
  quiz Q1 et de 01-tamrin Q2 (autre organe, autre clé) : gabarit à ne pas multiplier.
- Entre missions de la tranche : 09 Q1 ≈ 11 Q2 (gabarit 2×2 défaut × raison) ; 09 Q4 ≈ 11 Q6 (قصر → مفرّقة) ;
  07 Q4 c ≈ 10 Q4 d — recoupements de notion entre annales voisines, jamais mêmes options/pièges/explications.
  Aucune mission ne diffère d'une autre par ses seules données.
- Avec L01 (02/07, 02/08) et les autres chapitres : 07 Q4 recoupe 02/07 Q5–Q6 par le thème (nerf mixte, sens
  des fibres), formats différents. Aucune option identique à celle d'une mission publiée d'un autre chapitre.

## Défauts classés (récapitulatif — correctifs exacts dans chaque section)

**Critiques (clé fausse, ambiguïté, distracteur devenu vrai)** : aucun.

**Majeurs (4)** :
1. 08 Q2 — l'énoncé renvoie à « الجدول المطلوب », absent de la question (autonomie).
2. 08 Q4 — multi en trois paires miroir : compte 3 déductible, et les 3 clés sont les 3 options les plus
   longues (86/80/70 contre 69/69/65).
3. 09 Q3 d — nie la prémisse « عينًا سليمة (الرّسم 1) » (image devant la rétine de l'œil sain) ; plan 2×2 annoncé
   inexistant.
4. 10 Q1 — a et d proposent « مراكز الإبصار », déclarés sains par l'énoncé (a aussi le cristallin) : éliminés à vue.

**Mineurs** : 07 Q4 a/b/e « ألياف » → « أليافًا » ; 07 Q3 « محور الليف » → « طول الليف » ; 07 Q1 explication du
piège ; 08 Q1 a éliminé par la légende de l'énoncé ; 08 « يمثّل الرّسم رسمين » ; 09 Q3 « وعينها نفسها » ; 09 Q4
d3 → d2 (et avis d'étage 09) ; 09 Q1 explication (rattacher la cornée au laser du cours) ; 09 Q2 phrase
bancale ; 10 Q3 d « في المخّ » ; 10 Q3 explication (fuite évitable vers Q4 f) ; 11 Q6 duel « مقطعين » et
`<title>` « مقطعات » ; lettres arabes « أ »/« ب » dans les `<text>` des figures de 07, 08, 11 ; notes de livraison
à corriger (09 : changement cornéen reporté sur le globe, « +7 % » inexact ; 11 : « ≈ 1,8 » = rapport (ب)/(أ),
1,46 dans la rangée).

**Réserves sans correctif imposé** : 07 Q1 → Q2 (la clé de 1أ donne l'essentiel de 1ب) et 10 Q2 → Q3/Q4
(rôle de la rétine) : chaînage inhérent aux sujets officiels ; 08 Q2–Q4 sans repères (perte d'information
sans effet sur la résolubilité) ; 09 étage d3 généreux (une seule vraie d3).

## Chiffre final

- **Questions auditées : 23** (5 fichiers ; 15 mcq, 6 multi, 2 matching).
- **Clés fausses : 0** (23/23 re-résolues à l'aveugle, concordantes).
- **Défauts critiques : 0 · majeurs : 4 · mineurs : 17** (07 : 4 · 08 : 3 · 09 : 5 · 10 : 2 · 11 : 3).
- **Questions à reprendre : 13 distinctes** — 4 pour défaut majeur (08 Q2, 08 Q4, 09 Q3, 10 Q1) + 9 pour
  retouche mineure de texte (07 Q1, Q3, Q4 ; 08 Q1 ; 09 Q1, Q2, Q4 ; 10 Q3 ; 11 Q6 — 09 Q3 a aussi son
  énoncé à corriger) ; plus la retouche mécanique de 13 figures (lettres arabes : 07 Q1–Q3, 08 Q1–Q4,
  11 Q1–Q6) et deux notes de livraison (09, 11).
- **Verdicts** : 07 réserve mineure · 08 défaut majeur · 09 défaut majeur · 10 défaut majeur · 11 réserve mineure.
- **Étiquette nouvelle proposée : 1** (`bio.vis.difference-non-montree`, placements 11 Q2 b et 11 Q3 a) ;
  familles (b) et (c) : muettes.
