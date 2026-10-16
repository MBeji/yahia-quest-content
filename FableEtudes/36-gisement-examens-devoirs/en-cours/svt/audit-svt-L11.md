# Audit indépendant — gisement SVT 9ᵉ, vague 2, lot L11 (m028–m032)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills
`content-audit` + `prof-svt-9eme`). Branche `wip/gisement-svt-9eme-sessions`, commit `818fdb66`
(valide à ce commit — ré-auditer si les fichiers ont bougé). Lecture seule : aucun fichier audité
modifié, aucune écriture git. Rapport écrit au fil de l'eau.

Sources lues : transcriptions officielles `…/examens-nationaux/9eme-base/sciences-vie-terre/<session>-generale.md`,
PDF officiels (9web.edunet.tn) pour les figures, `cours.md`/`resume.md` des chapitres (origin/main),
missions publiées + quiz des chapitres, `misconceptions.json` (origin/main), PLAN-v2 § 1.

---

## m028 — `01-wadhifat-al-ittisal/exercices/07-examens-2018-ex3-et-qcm-coupes-tissu-nerveux-neurone.json`

Étage d2 (9 questions, toutes d2) : honnête. Titre conforme. Données 2018 ex. 3 fidèles à la
transcription et au PDF (vérifié à 300 dpi) ; items 2019-1, 2016-5, 2013-4, 2002-1 fidèles (2002-1 :
propositions a, b, d réécrites comme le demandait le plan).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 1→corps cellulaire, 2→dendrite, 3→axone | idem | OK | |
| 2 | 4→tissu conjonctif, 5→faisceau, 6→fibre | idem | **ERREUR (majeur)** | l'énoncé donne les trois paires |
| 3 | (أ) grise, (ب) nerf, (ج) blanche | idem | réserve (majeur) | « nerf = fibres en faisceaux » non enseigné au cours 01 |
| 4 | c | c | réserve (majeur) | explication = clé de Q3 |
| 5 | a | a | réserve (majeur) | doublon de quiz Q8 / 05-tadrib Q1 (« ne pas redemander ») |
| 6 | d (3→1) | d | OK | |
| 7 | b | b | OK | |
| 8 | b | b | réserve (majeur) | notion du chapitre 02 (arc réflexe) |
| 9 | d | d | réserve (majeur) | notion du chapitre 02 (rôle du récepteur) |

**Repères 2018 identifiés par position (point signalé) — TRANCHÉ.** PDF 2018 p. 2 relu à 300 dpi :
le trait du repère 4 aboutit dans la travée sombre entre les trois faisceaux (au voisinage d'un petit
vaisseau, mais sur la travée) → « tissu conjonctif » (نسيج رابط/ضامّ) est la lecture juste ; aucune
option « vaisseau » n'est proposée, donc pas d'ambiguïté. Le repère 5 est une flèche à deux pointes
placée sous le faisceau du bas, d'un bord à l'autre → elle désigne **le faisceau** (حزمة ألياف
عصبيّة). L'option « عرض حزمة من الألياف » est défendable mais maladroite : la légende attendue est
« حزمة من الألياف العصبيّة » (correctif ci-dessous).

### Défauts m028

- **[MAJOR] Q2 — l'énoncé livre les trois paires.** « ويملأ الحيّز الذي يفصل بينها نسيج رابط » +
  « الرقم 4 يشير إلى الحيّز الفاصل بين الحزم » → 4 = نسيج رابط ; « 5 سهم … يمتدّ عرض إحدى الحزم » →
  « عرض حزمة » ; « مقاطع الألياف » + « 6 … أحد المقاطع الدّائريّة » → 6 = مقطع ليف. Rien à
  résoudre. Par ailleurs « حزمة » et « نسيج رابط » ne sont enseignés par aucun cours de 01 (grep :
  0 occurrence dans `cours.md`/`resume.md` de 01 ; « نسيج رابط » n'apparaît qu'au cours 09) : il
  faut les définir sans désigner le repère. **Énoncé de remplacement (vérifié : aucune paire
  lisible, notions définies) :**
  > (مناظرة 2018) يبيّن الرّسم مقطعين عرضيّين مجهريّين أُجريا في مستوى الجهاز العصبيّ عند الإنسان: المقطع (ب) في اليمين والمقطع (ج) في اليسار. رُقّمت ثلاثة عناصر: الرقم 4 يشير إلى الحيّز الدّاكن بين الكتل المستديرة في المقطع (ب)، والرقم 5 سهم ذو رأسين طوله عرض إحدى هذه الكتل، والرقم 6 يشير إلى إحدى الدّوائر الصّغيرة ذات النّقطة المركزيّة في المقطع (ج). نذكّر بأنّ الحزمة مجموعة من الألياف العصبيّة المتجمّعة معًا، وأنّ النّسيج الرّابط نسيج يشدّ أجزاء العضو بعضها إلى بعض. أنسب كلّ رقم إلى ما يمثّله.

  Option `r1` : « عرض حزمة من الألياف » → « حزمة من الألياف العصبيّة » (clé inchangée : l1–r3,
  l2–r1, l3–r2). Explication : remplacer « والسّهم 5 يقيس عرض كتلة مستديرة واحدة من مقاطع الألياف،
  أي حزمة » par « والسّهم 5 يمتدّ على عرض كتلة مستديرة واحدة من مقاطع الألياف، فهو يدلّ على حزمة ».
  Titre SVG (`<title>`) : retirer « يفصل بينها نسيج داكن » → « تفصل بينها مساحة داكنة ».
- **[MINOR] Q2 — figure.** La flèche 5 (`M7 57 L49 57`) a exactement la largeur du faisceau
  haut-gauche (cx 28, rx 22) mais flotte 8 unités sous lui, dans la travée sombre, là où pointe aussi
  le 4 : à 232 px elle se lit comme « largeur de la travée ». Ajouter deux taquets verticaux aux bouts,
  alignés sur les bords du faisceau : `<path d="M7 47 v14 M49 47 v14" stroke="#0f172a" stroke-width="1"/>`
  (ne déplace rien, rend la portée lisible).
- **[MAJOR] Q3 — notion non enseignée.** Distinguer (ب) nerf de (ج) substance blanche exige « dans
  le nerf, les fibres sont groupées en faisceaux entourés de tissu conjonctif » : le cours 01 ne
  l'enseigne pas (il définit la substance blanche = fibres à gaine, et le nerf seulement comme
  « ناقل »). Correctif minimal dans l'énoncé, après « … لا جسم خلويّ بينها. » : ajouter
  « علمًا أنّ ألياف العصب تتجمّع في حزم يحيط بها نسيج رابط، بخلاف ألياف المراكز العصبيّة. »
  (la tâche reste : grise vs blanche vs nerf ; la paire (ب)↔nerf devient une application de la règle
  donnée, acceptable en d2). Correctif de fond (hors lot, à l'orchestrateur) : ajouter au cours 01,
  § « المادّة السّنجابيّة والمادّة البيضاء », une ligne sur la structure du nerf (le sujet 2018 la
  suppose).
- **[MINOR] Q3/Q4 — figure sans lettres.** Les trois cases n'ont pas de lettre (أ)(ب)(ج) ; seul
  l'énoncé dit « (أ) في اليمين… ». Ajouter sous chaque case un `<text>` « (أ) », « (ب) », « (ج) »
  (pied de case, comme le PDF).
- **[MAJOR] Q4 — fuite vers Q3.** L'explication « فالأجسام الخلويّة في المادّة السّنجابيّة، ومحاورها
  ألياف تكوّن المادّة البيضاء وتنتظم في حزم داخل العصب » rend, avec l'énoncé de Q4 qui redécrit les
  trois coupes, la clé entière de Q3 (donjon : tirage au hasard). **Explication de remplacement :**
  > الجسم الخلويّ والتّغصّنات والألياف أجزاء من خليّة واحدة هي الخليّة العصبيّة: جسمها الخلويّ في مركز عصبيّ، ومحورها ليف طويل يمتدّ بعيدًا عنه. فالخليّة العصبيّة هي الوحدة التّركيبيّة، وهي أيضًا الوحدة الوظيفيّة لأنّها تنقل السّيالة العصبيّة. الخطأ الشائع: عدّ العصب وحدة تركيبيّة، والعصب مجموعة ألياف أي أجزاء من خلايا كثيرة؛ ونسبة الحماية إلى الخليّة العصبيّة، والحماية دور السّحايا والسّائل الدّماغيّ الشّوكيّ.
- **[MAJOR] Q5 — doublon du publié.** « كيف تسير السّيالة … على العنصر 1 (تغصّنات) … على العنصر 2
  (محور) » est le sens dendrites → corps → axone que la liste interdit de redemander (quiz Q8,
  05-tadrib Q1) ; l'énoncé nomme lui-même « تفرّعاتها القصيرة » / « ليفها الطّويل », il ne reste que
  la règle du quiz. Q6 (2019) applique la même règle avec une donnée neuve (deux neurones).
  Correctif : **supprimer Q5** (la question 3b du sujet 2018 est couverte par Q6). Son explication
  rendait d'ailleurs la règle qui résout Q6.
- **[MAJOR] Q8 et Q9 — notions du chapitre 02.** « تنشأ السّيالة الحركيّة في المركز العصبيّ » et
  « المستقبل يحوّل المنبّه إلى سيالة حسّيّة » sont enseignés par le cours 02 (§ القوس الانعكاسي,
  l. 104–149) ; le cours 01 ne nomme jamais le récepteur ni l'arc (une seule occurrence de
  « المستقبلات الحسّيّة », au § hygiène). En chapitre 01 (premier du manifeste) l'élève ne peut
  pas les résoudre. Correctif : **déplacer Q8 et Q9 dans m029** (chapitre 02), telles quelles
  (aucun doublon dans 02 : vérifié contre quiz et 01–08). m028 tombe alors à 6 questions (Q1, Q2,
  Q3, Q4, Q6, Q7) : conforme à R5.
- Étiquettes m028 : toutes existantes sur `origin/main`, libellés conformes (Q6 a « في الاتّجاهين » =
  « ou dans les deux sens » du libellé ; Q7 a/c = nerf rachidien pris pour crânien ; Q8 a/d = origine
  du message moteur placée côté sensitif). Q7 d « المخيخ » muette : acceptable.
- Indices de forme : aucune clé strictement la plus longue ; Q7 clé 16 car. ex aequo avec
  « البصلة الشّوكيّة ». OK.
- Rendu : figures Q1–Q6 rendues en Chromium (232 px) : lisibles, aucune ne marque la clé.

---

## m029 — `02-al-af3al-al-in3ikasiya/exercices/09-examens-2013-ex2-et-annales-proprietes-reflexe-sensation-consciente.json`

(en cours)
