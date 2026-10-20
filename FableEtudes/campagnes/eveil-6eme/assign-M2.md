# Carte d’affectation M2 — éveil scientifique 6ᵉ, chapitres `02`, `03`, `10` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 10 missions (8 d’examen, 2 de devoir), 90 questions ; 1 auteur (ou 2 : `03` d’un côté, `02` + `10` de l’autre). Skills : `content-ecole-tn`, puis `prof-eveil-primaire` (calibre les étages, jamais plus que le programme de 6ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/eveil/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend un support (ou une situation) et ses consignes, découpés en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne la phrase OFFICIELLE de la transcription qu'elle lit (consigne et énoncé tels qu'imprimés, coquilles incluses sauf celles que la carte nomme) ; une consigne ouverte (« أفسّر », « أعلّل », « أصلح كلّ خطأ », « أقترح تجربة ») devient un QCM de l'explication ou de la correction, un `ordering` (étapes d'un protocole, trajet), un `matching` (légende ↔ nom, tableau) ou un `multi` (relevés, vrai/faux motivés) ; `short_answer` seulement pour UN terme du معجم avec ses `acceptedAnswers` ; aucun tracé n'est demandé à la main : un tracé de rayon, de flèche ou d'aiguille devient « quel dessin est exact ? » (QCM visuel) ; figures, schémas d'expériences et tableaux refaits en SVG, vrais, SANS donner la clé ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Chiffres du ملفّ du guide (78 %, 21 %, 2 : 1, 55 %, 1/6, 5 millions…) : enrichissement seulement, JAMAIS une clé ni un distracteur (V1) ; les quatre valeurs permises sont 1/5 d'oxygène, 1 L d'air ≈ 1,3 g, eau = 2/3 du corps, 120 jours (fiche §4 bis, point 4). Sont enseignés, donc exerçables : les plaquettes (V2 révisé), les huit directions (V5) ; l'« intensité » du courant n'est pas exigible (V3) ; la potabilisation est une lecture de schéma sans clé de mémorisation (V4). Chaque DÉFAUT d'énoncé que la carte nomme est corrigé dans la reprise, comme la carte le dit, et l'explication le signale. Étiquettes : `misconceptionTag` du registre `eveil.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/eveil/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-eveil/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject eveil-scientifique-6eme` (0 erreur), `content:tranche -- --subject eveil-scientifique-6eme --changed --fresh --strict-longest`.

**🔁 À REVÉRIFIER AU LANCEMENT (E-12).** Les 12 chapitres d'éveil seront mis à niveau sur la fiche programme APRÈS ce plan (cours au patron, exercices, étiquettes). Tous les « Ne pas redemander » de cette carte sont établis sur les exercices TELS QU'ILS SONT AU 2026-10-20 (état du 28 septembre : 5 fichiers de 6 questions à choix + un quiz de 5 questions par chapitre, tous des QCM) : ils sont PROVISOIRES. Au lancement de chaque mission, relis les exercices et le cours du chapitre tel qu'il sera alors, refais le croisement question par question, et mets la liste à jour avant d'écrire. Les numéros de fichiers (`06`, `07`, …) supposent que les chapitres ont `01`–`05` : si la mise à niveau ajoute un fichier, décale. Si un item que la carte cible (plaquettes, huit directions, sang décanté, sonnerie, monoxyde de carbone…) n'est pas enseigné par le chapitre mis à niveau, arrête-toi et signale-le : la mission ne part pas avant le cours.

**Ordre de travail** : (1) les ids d’étiquette neufs que tu poses ; (2) les missions du chapitre, dans l’ordre de la carte ; (3) les gates. **Départ du lot** : seulement quand ses chapitres ont été mis à niveau sur la fiche (E-11).


## Chapitre `02-respiration` — التّبادل الغازي في مستوى الرّئتين

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.resp.inspiration-expiration-confondues` (Tu confonds inspiration et expiration : l'air qui entre dans) | `eveil.gaz.test-mal-associe` (Tu associes un gaz au mauvais test : l'eau de chaux se troub) | `eveil.resp.echanges-dans-les-voies-respiratoires` (Tu places les échanges gazeux dans le nez, la trachée ou les) | `eveil.resp.sens-echanges-gazeux-inverse` (Tu inverses le trajet des gaz : dans les poumons le sang pre) | `eveil.resp.tabagisme-passif-ignore` (Tu crois que la fumée de tabac ne nuit qu'au fumeur : celui ) | `eveil.resp.poumons-fabriquent-oxygene` (Tu crois que les poumons fabriquent l'oxygène : le sang le p) | `eveil.resp.air-expire-sans-oxygene` (Tu crois que l'air expiré ne contient plus d'oxygène : le co) | `eveil.resp.coeur-organe-respiration` (Tu crois que le cœur sert à respirer ou que l'air y passe : )

### m013 → `exercices/06-exam-2016-de-lair-aux-cellules-le-trajet-de-loxygene.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2016 ⭐⭐⭐: … ») : Concours 2016 · de l'air du milieu aux cellules : le trajet de l'oxygène
- Registre : id `C11#1a` ; sources `C11#1a, C11#1b, C11#2a, C11#2b`
- Sources : C11 (session 2016), supports 1 et 2 entiers — transcriptions `2016-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - سجّل العدّاد نقصا في نسبة مكوّن من مكوّنات الهواء نتيجة عمليّة التنفّس داخل الوعاء من 21 بالمائة إلى 13 بالمائة. أ- أذكر اسم هذا المكوّن ........ ب- أعلّل إجابتي ........ (cloche, souris, coupelle « ماء الجير », capteur : 21.0 % puis 13.0 % après 20 min)
  - أحدّد بسهم مسار الأكسجين من هواء المحيط إلى خلايا العضلة على الرّسم (ب) :
  - ألاحظ الرّسم (أ) وأذكر اسم الغازين. (غاز 1 ........ غاز 2 ........ ; « التبادل الغازي في مستوى الخليّة »)
- Étapes prévues :
  - support 1-أ : le gaz dont la part baisse dans la cloche où respire la souris : l'oxygène — QCM — 1 q
  - support 1-ب : la justification (la souris respire : elle consomme de l'oxygène et rejette du dioxyde de carbone, que l'eau de chaux trouble) — QCM de la cause, QCM du rôle de l'eau de chaux — 2 q
  - support 2, consigne 1 : le trajet de l'oxygène de l'air aux cellules du muscle (poumon, sang, cœur, artère, muscle) — ordering des étapes, QCM visuel du trajet fléché sur le dessin (ب) (figure refaite, le cœur légendé « البطين الأيسر ») — 3 q
  - support 2, consigne 2 : au niveau de la cellule, l'oxygène entre et le dioxyde de carbone sort — matching gaz ↔ sens, QCM du changement de couleur du sang — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - nommer le gaz produit au lieu du gaz consommé — ligne C11#1a (d1)
  - invoquer le seul rôle de l'eau de chaux — ligne C11#1b (d2)
  - omettre le passage par le sang ou le cœur — ligne C11#2a (d3)
  - inverser les deux gaz — ligne C11#2b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `02/quiz#3`, `02/quiz#5`, `02/02-boss#1`, `02/02-boss#3`, `02/04-defi#2`, `02/04-defi#4`, `02/05-entrainement#4`, `03/02-boss#4`, `03/02-boss#5`, `03/02-boss#6`
- Note : Les pourcentages 21 % et 13 % sont des lectures d'un capteur imprimées dans le sujet : donnée, jamais clé (V1). Le « cœur » du dessin (ب) ne sert qu'à passer le sang des poumons aux organes ; ne pas demander l'anatomie des cavités (acquis de 5ᵉ). Placement au `02` (étape neuve : l'oxygène consommé par le vivant, puis le trajet).

### m014 → `exercices/07-exams-2010-2026-alveole-air-expire-et-dioxyde-de-carbone.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2010–2026 ⭐⭐: … ») : Concours 2010 · 2015 · 2018 · 2020 · 2026 · l'alvéole, l'air expiré, le dioxyde de carbone
- Registre : id `C01#10` ; sources `C01#10, C01#11, C07#10, C12#4a, C17#6a, C09#12`
- Sources : C01 (session 2026), situation intégrative, support 2, consignes 2-1 et 2-2 ; C07 (session 2020), situation intégrative, consigne 4 ; C12 (session 2015), support 4 ; C17 (session 2010), support 6 ; C09 (session 2018), support 4, consigne 2 — transcriptions `2026-unique.md`, `2020-unique.md`, `2018-unique.md`, `2015-unique.md`, `2010-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · أصلحْ كلّ خطأ ورد في الإفادة التّالية : يدخلُ هواءُ الشّهيق إلى الرّئتين محمّلا بثاني أكسيد الكربون، ويخرج منهما الدّم أحمرَ قاتما ومحمّلا بثاني أكسيد الكربون.
  - 2026 · اِقترحْ تجربة تبيّن وجود ثاني أكسيد الكربون في هواء الزّفير.
  - 2020 · أكتب تفسيرا مناسبا للظّاهرة العلميّة المبيّنة في الرّسم التّالي. (coupe d'une alvéole et de son capillaire : هواء الشّهيق، هواء الزّفير، دم غنيّ بالأكسجين، دم غنيّ بثاني أكسيد الكربون)
  - 2015 · أتأمّل الرّسم وأكمل بما يناسب : « يدخل الدم مشبعا بـ ........ » / « يخرج الهواء مشبعا بـ ........ » (التبادل الغازي في مستوى الحويصلات الرئويّة)
  - 2010 · أضع العلامة (×) أمام الإفادة الخاطئة. (يتمّ التّبادل الغازي بين الجسم وهواء المحيط في مستوى الحويصلات الرّئويّة. / أتنفّس بأنفي لأنّ أغشيته تُنقّي الهواء من ثنائي أكسيد الكربون. / يمرّ الدّم من الرّئتين إلى القلب محمّلا بالأكسجين. / تقوم الكريّات الحمراء بنقل الغذاء إلى أعضاء الجسم.)
  - 2018 · أصلح الخطأ في الإفادة التّالية مبيّنا سبب اختناق مريم. « تمتلئ الأوعية الدّمويّة بهواء مشبع بالأكسجين وهباب الفحم ممّا يسبّب صعوبة في التّنفّس. »
- Étapes prévues :
  - 2026 (2-1) : deux erreurs dans l'énoncé (l'air inspiré est riche en oxygène ; le sang qui sort des poumons est rouge vif, chargé d'oxygène) — deux QCM d'erreur, un QCM de la phrase corrigée — 3 q
  - 2026 (2-2) : l'expérience qui montre le dioxyde de carbone dans l'air expiré : souffler dans l'eau de chaux qui se trouble — ordering du protocole, QCM du résultat — 2 q
  - 2020 (4) et 2015 (4) : le sens des gaz à travers la paroi de l'alvéole (l'oxygène passe de l'air au sang, le dioxyde de carbone du sang à l'air) — QCM de l'explication, matching gaz ↔ sens — 2 q
  - 2010 (6) : parmi quatre énoncés, repérer les deux faux (le nez n'enlève pas le dioxyde de carbone ; les globules rouges ne transportent pas les aliments) — multi, QCM « qui transporte les aliments ? » (le plasma) — 2 q
  - 2018 (4-2) : la suffocation près d'un feu de branches : la fumée irrite et encombre les voies respiratoires, l'air est pauvre en oxygène ; le sang ne se remplit pas de suie — QCM de l'erreur, QCM de la cause — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - faire entrer du dioxyde de carbone à l'inspiration / inverser rouge clair et rouge foncé — ligne C01#10 (d2)
  - oublier le réactif ou son résultat attendu — ligne C01#11 (d2)
  - inverser le sens de passage de chaque gaz — ligne C07#10 (d2)
  - inverser les gaz entrant et sortant — ligne C12#4a (d2)
  - attribuer le transport des aliments aux globules rouges — ligne C17#6a (d2)
  - dire que le sang se remplit de suie — ligne C09#12 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `02/quiz#3`, `02/quiz#4`, `02/quiz#5`, `02/02-boss#1`, `02/02-boss#3`, `02/02-boss#5`, `02/03-revision#4`, `02/03-revision#6`, `02/04-defi#2`, `02/04-defi#3`, `02/04-defi#4`, `02/05-entrainement#1`, `02/05-entrainement#4`, `02/01-pratique#4`
- Note : Le patron est déjà riche sur l'échange alvéolaire et l'eau de chaux : le gain de la mission est la forme d'examen (énoncé à corriger, deux erreurs imbriquées, quatre énoncés dont deux faux). 2018 (4-2) est un item `01+02` du registre : on le garde ici pour l'explication de la suffocation ; la preuve de la suie est dans la mission « éléments, produits et preuves » du `01`. Barème du 2026 (2-1) : (0,5) puis (0,75), à ne pas reprendre.


## Chapitre `03-sang-circulation` — الدّم: تركيبته ووظيفته

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.sang.plasma-rouge` (Tu crois que le plasma est rouge et donne sa couleur au sang) | `eveil.sang.globules-blancs-plus-nombreux` (Tu crois que les globules blancs sont plus nombreux que les ) | `eveil.sang.transport-attribue-aux-globules` (Tu crois que ce sont les globules qui transportent les alime) | `eveil.sang.roles-globules-rouges-blancs-inverses` (Tu inverses les rôles des globules : les rouges transportent) | `eveil.sang.caracteres-globules-inverses` (Tu donnes au globule blanc les traits du rouge, ou l'inverse) | `eveil.resp.sens-echanges-gazeux-inverse` (Tu inverses le trajet des gaz : dans les poumons le sang pre) | `eveil.sang.plasma-et-serum-confondus` (Tu confonds plasma et sérum : le plasma est le liquide du sa)

### m015 → `exercices/06-exam-2025-le-depliant-du-don-de-sang.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2025 ⭐⭐⭐: … ») : Concours 2025 · situation 2 · le dépliant du don de sang
- Registre : id `C02#5` ; sources `C02#5, C02#6, C02#7, C02#8`
- Sources : C02 (session 2025), situation 2 entière — transcriptions `2025-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - اُشطب العبارة الخاطئة في كلّ خانة لتحصل على الإفادة الصّحيحة. (في هذا الوعاء دم أحمر: قان / قاتم ; دم محمّل بـ: الأكسجين / ثاني أكسيد الكربون ; يتمّ التّبادل الغازيّ في مستوى: خلايا الجسم / الرّئتين ; هذا: وريد / شريان)
  - أرسم مكان النّقاط أسهما تحدّد اتّجاه مسار الدّم في الأوعية الدّمويّة.
  - بيّن الفرق بين عمليّة التّبادل الغازيّ في مستوى الرّئة وفي مستوى أحد أعضاء الجسم.
  - أصلحْ كلّ خطأ ورد في الإفادة التّالية. الكريّات الحمراء عديمة الشّكل والنّوى وتتكوّن في النّخاع الشّوكيّ.
- Étapes prévues :
  - consigne 1-أ : les quatre cadres pour un vaisseau du schéma (couleur du sang, gaz porté, lieu de l'échange, artère ou veine) — trois QCM (un vaisseau qui quitte le cœur vers l'organe 1, un vaisseau qui en revient) — 3 q
  - consigne 1-ب : le sens du sang dans le circuit (oreillette droite, poumon, cœur, organe, cœur) — ordering, QCM visuel des flèches (figure refaite sans cœur détaillé) — 2 q
  - consigne 2 : à l'échange du poumon l'oxygène entre dans le sang et le dioxyde de carbone en sort ; à l'échange d'un organe c'est le contraire — matching, QCM «ce qui change de couleur» — 2 q
  - consigne 3 : le globule rouge a une forme (disque à deux faces creuses), n'a pas de noyau, et se forme dans l'os (moelle osseuse, pas épinière) — QCM de l'erreur sur la forme, QCM de la phrase corrigée. HP du lecteur (`moelle-osseuse`) : le patron l'enseigne déjà (03/02-boss#2), voir E-7 — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - inverser couleur du sang et gaz transporté selon le vaisseau — ligne C02#5 (d2)
  - partir du mauvais côté du cœur — ligne C02#6 (d2)
  - dire que les deux échanges vont dans le même sens — ligne C02#7 (d3)
  - dire sans forme et sans noyau / situer la formation dans la moelle épinière — ligne C02#8 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/02-boss#1`, `03/02-boss#2`, `03/02-boss#4`, `03/02-boss#5`, `03/quiz#2`, `03/quiz#3`, `03/03-revision#6`, `03/05-entrainement#3`, `02/02-boss#1`, `02/04-defi#2`
- Note : Le sujet donne un schéma de circulation « à deux organes » (العضو 1 et 2) : l'auteur le refait avec un organe qui est le poumon et un autre qui est un muscle, sans donner la clé. Les flèches sont à dessiner par l'élève : la mission les transforme en ordering. Placement au `03` (le vaisseau et le sens du sang sont l'étape neuve).

### m016 → `exercices/07-exams-2015-2024-deux-circuits-deux-couleurs.json` · d2 practice 75/15 · 11 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2015–2024 ⭐⭐: … ») : Concours 2015 · 2022 · 2024 · deux circuits, deux couleurs
- Registre : id `C05#1` ; sources `C05#1, C05#2, C05#3, C05#4, C03#3, C12#5a`
- Sources : C05 (session 2022), situation 1 entière ; C03 (session 2024), situation 2, support 2, consigne 2-1-ب ; C12 (session 2015), support 5, consigne 1 — transcriptions `2024-unique.md`, `2022-unique.md`, `2015-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2022 · في الوثيقة التّالية رسمان يمثّلان مسار الدّم في كلّ من الدّورتين الكبرى والصّغرى. أتأمّلهما ثمّ أكمل الفراغات بما يناسب. (في الوعاء الدّمويّ 1 يكون الدّم غنيّا بـ ........ / في الوعاء الدّمويّ 2 ... / لون الدّم في الوعاء الدّمويّ 3 يكون ........)
  - 2022 · أفسّر سبب تغيّر لون الدّم من الأحمر القاتم إلى الأحمر القاني خلال دورته بين القلب والرّئتين.
  - 2022 · كيف أميّز من خلال الملاحظة بالعين المجرّدة بين الدّم المتخثّر والدّم المترسّب؟
  - 2022 · أصلح كلّ خطأ ورد في الإفادة التّالية. يضخّ البطين الأيمن الدّم المحمّل بالأكسجين إلى الرّئتين عبر الوريد الرّئويّ.
  - 2024 · بيّن الفرق بين الدّم الصّادر من القلب نحو الرّئتين والدّم العائد منهما نحو القلب بذكر خاصّيتين مميّزتين لكلّ منهما.
  - 2015 · أصلح الخطأ إن وُجد : يمرّ هواء الشهيق عبر القصبة الهوائيّة فيُنقِص السائل المخاطيّ والشعيرات من الجراثيم والغبار. – يخرج الدم من القلب محمّلا بالأكسيجين لتغذية الرئتين، ويغادرهما محمّلا بثاني أكسيد الكربون.
- Étapes prévues :
  - 2022 (1) : deux circuits, quatre vaisseaux ; richesse en gaz des vaisseaux 1 et 2 (poumon) et couleur du vaisseau 3 (muscle) — matching trois lignes, QCM de contrôle (grande et petite circulation) — 2 q
  - 2022 (2-أ) : le sang passe du rouge sombre au rouge vif entre le cœur et les poumons : il prend de l'oxygène et rejette du dioxyde de carbone — QCM — 1 q
  - 2022 (2-ب) : sang coagulé (un caillot et un liquide jaune clair) et sang décanté (le plasma jaune au-dessus, les cellules au fond) — QCM de description, QCM de l'aspect de chaque tube. HP du lecteur (`sang-decante`) : voir E-7 — 2 q
  - 2022 (3) : le ventricule droit envoie vers les poumons du sang pauvre en oxygène par l'artère pulmonaire (deux erreurs) — QCM de l'erreur sur le sang, QCM de l'erreur sur le vaisseau — 2 q
  - 2024 (2-1-ب) : deux propriétés distinctives du sang qui va aux poumons et de celui qui en revient (couleur, gaz porté) — matching — 2 q
  - 2015 (5-1) : le premier énoncé (le mucus et les poils retiennent poussières et germes) est JUSTE (« si besoin » : ne pas inventer d'erreur) ; le second inverse la charge du sang à la sortie du cœur — QCM de l'énoncé juste, QCM de l'erreur — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - inverser les deux circuits / confondre rouge clair et foncé — ligne C05#1 (d2)
  - oublier l'entrée d'oxygène dans le sang — ligne C05#2 (d2)
  - confondre caillot et dépôt des cellules — ligne C05#3 (d2)
  - faire partir du sang oxygéné vers les poumons — ligne C05#4 (d2)
  - inverser couleur et gaz porté — ligne C03#3 (d2)
  - inverser la charge du sang avant et après les poumons — ligne C12#5a (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/02-boss#4`, `03/02-boss#5`, `03/05-entrainement#3`, `03/01-pratique#1`, `03/01-pratique#2`, `03/03-revision#2`, `02/02-boss#1`, `02/04-defi#2`, `02/05-entrainement#4`
- Note : Les noms « الدّورة الكبرى / الصّغرى » viennent du sujet ; le patron dit déjà « les poumons » et « les organes ». L'auteur garde « الوريد الرّئويّ » dans l'énoncé fautif (l'erreur est le vaisseau). L'item du sang décanté (E-7) est le seul ◐ de la mission.

### m017 → `exercices/08-exams-2019-2026-vaisseaux-sens-du-sang-et-trajet.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2019–2026 ⭐⭐: … ») : Concours 2019 · 2020 · 2021 · 2023 · 2026 · les vaisseaux, le sens du sang, le trajet vers le cœur
- Registre : id `C04#1` ; sources `C04#1, C04#2, C04#3, C06#12, C07#3, C08#2, C01#8`
- Sources : C01 (session 2026), situation 2, consigne 3 ; C04 (session 2023), situation 1, support 1 ; C06 (session 2021), situation intégrative, support 2, consigne 1 ; C07 (session 2020), situation 1, support 2, consigne 2 ; C08 (session 2019), situation 1, support 1, consigne 2 — transcriptions `2026-unique.md`, `2023-unique.md`, `2021-unique.md`, `2020-unique.md`, `2019-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2023 · (« عند بذل نشاط تتسارع دقّات القلب ويزداد تدفّق الدّم الغنيّ بالأكسجين إلى مختلف أعضاء الجسم عبر أوعية دمويّة ») أذكر نوع الأوعية الدّمويّة التي أشار إليها أحمد. / أعلّل إجابتي. / أفسّر تغيّر لون الدّم في عمليّة التّبادل الغازيّ بين الدّم وخلايا الجسم.
  - 2021 · أكمل صياغة الاستنتاج لتفسير مسار الدّم : تحمل ......... الدّم الغنيّ بثنائي أكسيد الكربون من الجسم إلى الأذين الأيمن، كما تقوم ......... بنقل الدّم الغنيّ بالأكسجين من الرّئتين إلى الأذين الأيسر.
  - 2020 · أصلح مسار الدّم القادم من الرّئتين إلى القلب : (الأوردة الرّئويّة ← البطين الأيسر ← الأذينة اليمنى ← الشّريان الأبهر)
  - 2019 · أصلح كلّ خطإ ورد في الإفادة التّالية : يخرج الدّم من الرّئتين محمّلا بالأكسجين في اتّجاه خلايا الجسم عبر الأوردة.
  - 2026 · أصلحُ كلّ خطأ ورد بالإفادة التّالية. تنقل الأوردة الرّئويّة الدّم الغنيّ بثاني أكسيد الكربون إلى الرّئتين.
- Étapes prévues :
  - 2023 (1-أ, 1-ب) : le sang riche en oxygène qui va du cœur vers les organes circule dans des artères ; le justifier par le sens du trajet et le contenu — QCM du vaisseau, QCM de la justification — 2 q
  - 2023 (1-ج) : le sang perd son oxygène et prend du dioxyde de carbone au contact des cellules, il passe du rouge vif au rouge sombre — QCM — 1 q
  - 2021 (1) : les deux blancs : les veines (du corps vers l'oreillette droite) et les veines pulmonaires (des poumons vers l'oreillette gauche) — matching — 2 q
  - 2020 (2) : rétablir l'ordre du trajet du sang depuis les poumons (veines pulmonaires, oreillette gauche, ventricule gauche, aorte) : quatre étapes — ordering — 1 q
  - 2019 (2) : le sang quitte les poumons chargé d'oxygène, vers le cœur et non vers les cellules, par les veines pulmonaires — QCM de l'erreur sur la direction, QCM de l'erreur sur le vaisseau — 2 q
  - 2026 (3) : les veines pulmonaires ramènent au cœur le sang riche en oxygène (le sang riche en dioxyde de carbone va au poumon par l'artère pulmonaire) — QCM de l'erreur sur le gaz, QCM sur le sens — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - répondre veines — ligne C04#1 (d1)
  - oublier le sens du trajet par rapport au cœur — ligne C04#2 (d2)
  - inverser le gaz cédé et le gaz reçu — ligne C04#3 (d2)
  - confondre veines du corps et veines des poumons — ligne C06#12 (d2)
  - passer directement à l'oreillette droite — ligne C07#3 (d2)
  - nommer artères les vaisseaux qui arrivent aux poumons — ligne C08#2 (d2)
  - inverser dioxyde de carbone et oxygène selon le sens du trajet — ligne C01#8 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/02-boss#4`, `03/02-boss#5`, `03/02-boss#6`, `03/05-entrainement#3`, `02/02-boss#1`, `02/04-defi#2`, `02/05-entrainement#4`, `03/04-defi#5`
- Note : Le sujet 2020 imprime une chaîne FAUSSE à corriger (« ← البطين الأيسر ← الأذينة اليمنى ← ») : la mission demande l'ordre juste (veines pulmonaires, oreillette gauche, ventricule gauche, aorte). L'anatomie du cœur est un acquis de 5ᵉ (⛔ de la fiche pour l'approfondir) : l'auteur n'emploie que les noms qui figurent dans le sujet. Les couleurs et le sens (vers le cœur / vers les organes) sont le vrai geste neuf.

### m018 → `exercices/09-exams-2019-2026-composants-du-sang-frottis-et-fonctions.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2019–2026 ⭐⭐: … ») : Concours 2019 · 2020 · 2021 · 2026 · les composants du sang : le frottis et leurs fonctions
- Registre : id `C01#5` ; sources `C01#5, C01#6, C06#2, C08#1, C07#1`
- Sources : C01 (session 2026), situation 2, consignes 1-أ et 1-ب ; C06 (session 2021), situation 1, consigne 2 ; C08 (session 2019), situation 1, support 1, consigne 1 ; C07 (session 2020), situation 1, support 1 — transcriptions `2026-unique.md`, `2021-unique.md`, `2020-unique.md`, `2019-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · شاهدْ رسمَ السّحبة الدّمويّة ثمّ سمِّ مكوّنات الدّم 1 و 3 و4. (la légende 2 est imprimée : « صُفَيحات »)
  - 2026 · أكمِلْ كلّ إفادة برقم مكوّن الدّم المناسب. (نقلُ المغذّيات والأدوية / مقاومةُ الجرثومة والدّفاع عن الجسم / المساعدةُ على التئام جرح الإبرة / ضمانُ التّبادل الغازيّ بين الجسم وهواء المحيط)
  - 2021 · أتمّ تعمير فراغات الجدول التّالي بما يناسب. (مكوّن الدّم | مشاهدة مجهريّة لسحبة دمويّة | الوظيفة)
  - 2019 · أكمل تعمير الجدول بما يناسب : (مكوّن الدّم : ... / البلازما / ... ; وظيفته : تخثّر الدّم / ... / الدّفاع عن الجسم)
  - 2020 · أكتب أمام كلّ إفادة مكوّنَ الدّم المناسب من بين المكوّنات التّالية : البلازما، الكريّات الحمراء، الكريّات البيضاء. (تتكوّن في نخاع العظم / ذات نواة / تمثّل حوالي 55 % من الدّم)
- Étapes prévues :
  - 2026 (1-أ) : nommer trois éléments d'un frottis (globule blanc, globule rouge, plasma) ; les plaquettes sont déjà nommées dans le sujet — matching numéro ↔ nom — 1 q
  - 2026 (1-ب) : relier quatre fonctions au numéro du composant (transport des nutriments : plasma ; défense : globule blanc ; cicatrisation : plaquettes ; gaz : globule rouge) — matching, QCM du leurre « les gaz portés par le plasma» — 2 q
  - 2021 (2) : le globule blanc d'une photo de frottis (noyau) et la fonction de deux éléments (plaquettes : coagulation ; fond clair : plasma, transport) — QCM du nom, QCM de la fonction des plaquettes, QCM du fond clair — 3 q
  - 2019 (1) : tableau composant ↔ fonction à trois cases vides (globule rouge, coagulation, globule blanc) — matching — 1 q
  - 2020 (1) : trois propriétés rattachées à leur composant (nées dans l'os ; à noyau ; le liquide jaune pâle). La valeur « 55 % » est remplacée par « le liquide jaune pâle qui occupe la plus grande part » (V1) — matching — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre plasma et globule / ne pas reconnaître le fond du dessin comme un composant — ligne C01#5 (d2)
  - attribuer le transport des gaz au plasma — ligne C01#6 (d2)
  - confondre globule blanc et plaquette — ligne C06#2 (d2)
  - attribuer la coagulation aux globules blancs — ligne C08#1 (d2)
  - confondre globule blanc et globule rouge — ligne C07#1 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/quiz#1`, `03/quiz#2`, `03/quiz#3`, `03/quiz#4`, `03/01-pratique#1`, `03/01-pratique#3`, `03/01-pratique#4`, `03/02-boss#1`, `03/03-revision#1`, `03/03-revision#3`, `03/03-revision#5`, `03/04-defi#1`, `03/04-defi#4`
- Note : V2 révisé : les plaquettes sont enseignées et exercées (« complément au manuel »). Le 2026 et le 2021 les nomment : l'auteur peut les poser comme bonne réponse à la fonction « coagulation ». Le tableau d'analyses chiffrées du sujet 2021 (consigne 1, vitamines) n'est PAS dans cette mission : il est au `04`. La photo du frottis (2021) a une cible de flèche ambiguë (fond clair) : l'auteur refait un dessin net.

### m019 → `exercices/10-exams-2008-2025-globules-coagulation-et-anemie.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2025 ⭐⭐: … ») : Concours 2008 · 2012 · 2013 · 2023 · 2024 · 2025 · les globules, la coagulation, l'anémie
- Registre : id `C15#1a` ; sources `C15#1a, C19#1a, C19#1b, C14#3a, C02#12, C03#2, C04#15`
- Sources : C15 (session 2012), support 1 ; C19 (session 2008), support 1 ; C14 (session 2013), support 3, consigne 1 ; C02 (session 2025), situation intégrative, support 3 ; C03 (session 2024), situation 2, consigne 2-1-أ ; C04 (session 2023), situation intégrative, support 3 — transcriptions `2025-unique.md`, `2024-unique.md`, `2023-unique.md`, `2013-unique.md`, `2012-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2012 · أضَعُ العلامة (x) في الخانة المناسبة : (الكريات الحمراء / الكريات البيضاء × غير منتظمة الشكل · عديمة اللون · غنيّة بمادّة الحديد · بها نواة · عمرها حوالي 120 يوما · مقعّرة الوجهين)
  - 2008 · عمّر الجدول التّالي وفق المطلوب. (مكوّنات الدّمّ | وظيفة كلّ مكوّن) / أُكتب "صواب" أو "خطأ" في التّربيعة المناسبة. (في الجسم أعضاء لا يصلها الدّمّ · الكريّات البيضاء أكثر عددا من الكريّات الحمراء · الدّمّ المتخثّر يتكوّن من علقة ومصل · يتخلّص الدّمّ من ثنائي أكسيد الكربون في مستوى الرّئتين)
  - 2013 · أكمل بالتفسير المناسب : عند الإصابة بجرح خفيف ينزف الدم ثمّ يتوقّف لأنّ ........
  - 2025 · أجب بـ "صواب" أو "خطأ". (يتكوّن الدّم المتخثّر من بلازما وعلقة. · الكريّات البيضاء هي التي أوقفت نزف الدّم في إصبع حازم. · في الدّم المترسّب، تفوق نسبةُ الكريّات البيضاء والصّفيحات الدّمويّة نسبةَ الكريّات الحمراء.)
  - 2024 · أكمل الجدول التالي بتحديد مكوّن الدّم المناسب. (سائل يعلو العلقة في الدّم المتخثّر · سائل تمثّل نسبته 55 % من الدّم المترسّب · سائل ينقل الفضلات من أنحاء الجسم إلى الكليتين)
  - 2023 · أكتب "صواب" أو "خطأ" أمام ما يفسّر الأعراض التي ظهرت على شادٍ. (نقص في عدد الكريّات الحمراء · إصابة بمرض تصلّب الشّرايين)
- Étapes prévues :
  - 2012 : six propriétés à répartir entre globules rouges et globules blancs (noyau, forme, couleur, fer, durée de vie, creux) — matching, QCM sur une propriété piège (le noyau) — 2 q
  - 2008 (1) : tableau composants ↔ fonctions — matching ; (2) quatre énoncés vrai/faux (« les globules blancs plus nombreux » est faux) — multi — 2 q
  - 2013 (3-1) : une petite plaie cesse de saigner parce que le sang se coagule (un caillot bouche la plaie) — QCM — 1 q
  - 2025 (support 3) : trois énoncés sur le sang coagulé et le sang décanté — multi, QCM sur le rôle des plaquettes (bouchon) ; HP du lecteur (`sang-decante`, `plaquettes`) : E-7 — 2 q
  - 2024 (2-1-أ) : trois liquides à rattacher (sérum au-dessus du caillot, plasma au-dessus des cellules, plasma qui transporte les déchets) ; « 55 % » est remplacé par « le liquide jaune qui surmonte les cellules » (V1) — matching, QCM sérum/plasma — 2 q
  - 2023 (3) : fatigue et pâleur : trop peu de globules rouges est une explication juste ; la maladie des artères n'en est pas une — QCM. HP du lecteur (`arteriosclerose`) : le mot est donné, jamais enseigné (E-8) — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - attribuer le noyau aux globules rouges — ligne C15#1a (d2)
  - intervertir les rôles des cellules du sang — ligne C19#1a (d1)
  - croire que le sang n'atteint pas certains organes — ligne C19#1b (d1)
  - décrire l'arrêt sans nommer la formation du caillot — ligne C14#3a (d1)
  - confondre caillot et sérum / attribuer l'arrêt du saignement aux globules blancs — ligne C02#12 (d2)
  - confondre sérum et plasma — ligne C03#2 (d2)
  - retenir la maladie des artères — ligne C04#15 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/01-pratique#1`, `03/01-pratique#2`, `03/01-pratique#3`, `03/01-pratique#6`, `03/02-boss#1`, `03/02-boss#6`, `03/03-revision#2`, `03/03-revision#3`, `03/04-defi#1`, `03/04-defi#6`, `03/05-entrainement#2`, `03/05-entrainement#5`, `03/05-entrainement#6`, `03/quiz#3`, `03/quiz#5`
- Note : Mission de synthèse sur les cellules et la coagulation. L'échantillon 2008 contient des énoncés à nombre (« plus nombreuses ») qui restent qualitatifs. « عمرها حوالي 120 يوما » est une des quatre valeurs permises du manuel (fiche §4 bis, point 4). Le piège « caillot/sérum/plasma » est le plus dense du chapitre (3 sessions).

### m020 → `exercices/11-devoir-sang-coeur-tubes-et-fonctions.json` · d2 practice 75/15 · 8 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐: … ») : Le sang : le cœur, deux tubes, les constituants et leurs fonctions
- Registre : id `D04#1` ; sources `D04#1, D04#2, D04#7, D04#8, D04#10, D05#2`
- Cartes : devoir D (T2, école primaire), exercices 1, 2, 7, 8, 10 ; devoir E (T2, école primaire), exercice 2 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D04#1 (d2) : identifier deux vaisseaux d'un schéma du cœur et cocher leurs caractéristiques
  - D04#2 (d2) : colorier et compléter les constituants d'un sang coagulé et d'un sang décanté
  - D04#7 (d1) : nommer le constituant qui fait coaguler le sang
  - D04#8 (d1) : situer l'absorption des nutriments transportés par le plasma
  - D04#10 (d2) : associer éléments et fonctions : transport de gaz, valve, énergie, carence, défense, eau
  - D05#2 (d2) : cocher les caractéristiques propres aux globules rouges et blancs dans un tableau
- Étapes prévues :
  - Un schéma du cœur : repérer deux vaisseaux et cocher leurs caractéristiques (contenu, couleur, sens) — QCM, QCM — 2 q
  - Deux tubes de sang, l'un coagulé, l'autre décanté : colorier et nommer ce qui occupe le haut et le bas de chacun — QCM visuel, QCM — 2 q
  - Le constituant qui fait coaguler le sang (les plaquettes) ; l'endroit où les aliments passent dans le sang (l'intestin grêle) — QCM, QCM — 2 q
  - Associer six éléments et leurs fonctions (transport des gaz, valve, énergie, carence, défense, eau) — matching — 1 q
  - Un tableau à six cases : les caractéristiques des globules rouges et des globules blancs — matching — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre artère et veine pulmonaires — ligne D04#1 (d2)
  - intervertir plasma et cellules — ligne D04#2 (d2)
  - nommer le plasma — ligne D04#7 (d1)
  - citer l'estomac — ligne D04#8 (d1)
  - confondre vitamine et sel minéral — ligne D04#10 (d2)
  - attribuer le fer aux globules blancs — ligne D05#2 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `03/01-pratique#1`, `03/01-pratique#2`, `03/01-pratique#3`, `03/02-boss#1`, `03/03-revision#3`, `03/04-defi#1`, `03/05-entrainement#4`
- Note : Salle blanche. Les gestes neufs sont le schéma du cœur à cocher et les deux tubes à colorier. La ligne D04#12 (classer trois types d'hémorragie par gravité) n'est pas reprise : savoir du maître, hors manuel (◐, E-8). D04#3, D04#4 et D04#9 (mêmes gestes que les autres missions du chapitre) non plus.


## Chapitre `10-microbes-defense` — الجراثيم ووقاية الجسم

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.microbes.epaisseur-peau-mal-expliquee` (Tu expliques l'épaisseur de la peau par l'embonpoint ou les ) | `eveil.microbes.eau-suffit-pour-la-plaie` (Tu crois que laver la plaie à l'eau, ou la presser pour fair) | `eveil.microbes.vaccin-pris-pour-medicament` (Tu prends le vaccin pour un médicament qui guérit un malade ) | `eveil.microbes.infection-attribuee-au-dernier-geste` (Tu accuses le dernier geste fait (le lavage à l'eau) d'avoir) | `eveil.microbes.maladie-reconnue-au-symptome-commun` (Tu reconnais une maladie à un symptôme commun (gêne à respir) | `eveil.microbes.globules-blancs-gagnent-toujours` (Tu crois que les globules blancs gagnent toujours contre les) | `eveil.microbes.pus-seulement-microbes` (Tu crois que le pus n'est fait que de microbes : il est fait)

### m021 → `exercices/06-exams-2013-2018-plaie-vaccin-serum-et-defense.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2013–2018 ⭐⭐: … ») : Concours 2013 · 2015 · 2017 · 2018 · la plaie, le vaccin, le sérum, la défense du corps
- Registre : id `C10#2a` ; sources `C10#2a, C09#5, C14#3b, C12#5b`
- Sources : C10 (session 2017), support 2, consigne 1 ; C09 (session 2018), support 2, consigne 2 ; C14 (session 2013), support 3, consigne 2 ; C12 (session 2015), support 5, consigne 2 — transcriptions `2018-unique.md`, `2017-unique.md`, `2015-unique.md`, `2013-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2017 · أكمل الفراغات الواردة بالنصّ التالي للحصول على استنتاج حول مقاومة الجسم للجراثيم. (تنفذ الجراثيم إلى داخل الجلد عبر موضع الوخز حيث يتوفّر ........ و........ فتتكاثر متسبّبة في ........ فتتدخّل الكريّات البيضاء لمقاومتها.)
  - 2018 · أصلح الإفادة التّالية : « يتمثّل التّلقيح في تنشيط الكريّات الحمراء وهو إجراء يتمّ بعد الإصابة. لذلك يندرج التّلقيح ضمن المناعة الطبيعيّة للجسم. »
  - 2013 · أصلح الخطأ في الإفادات التالية : يستعمل زيدان المصل للوقاية من الأمراض الجرثوميّة. · يحتاج زيدان في هذه الحال للحقن بمصل مضادّ للشلل. · يستعمل زيدان التلقيح لعلاج الأمراض الجرثوميّة.
  - 2015 · أربط بما يناسب : (الأمصال · العقد اللمفاويّة · التلاقيح ↔ المناعة الطبيعية · المناعة المكتسبة · العلاج)
- Étapes prévues :
  - 2017 : le texte à trous (les germes trouvent des aliments et de la chaleur, se multiplient, causent l'infection ; alors interviennent les globules blancs) — deux QCM sur les blancs — 2 q
  - 2018 : la vaccination ne stimule pas les globules rouges, se fait avant l'infection, et donne une immunité acquise (non naturelle) — trois QCM sur les trois erreurs — 3 q
  - 2013 : trois énoncés à corriger (le sérum soigne, le vaccin protège ; pour une plaie souillée de terre, le sérum antitétanique). DÉFAUT : « مصل مضادّ للشلل » est imprimé pour le cas d'une plaie ; la mission écrit « مصل مضادّ للكزاز » (le patron enseigne le tétanos) — trois QCM — 3 q
  - 2015 : relier le sérum, la vaccination (et les globules blancs à la place des ganglions) à la catégorie de défense — matching. HP : les ganglions lymphatiques (◐) sont remplacés par un élément du manuel — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - oublier le rôle des globules blancs — ligne C10#2a (d2)
  - la croire curative et naturelle — ligne C09#5 (d2)
  - confondre prévention et traitement — ligne C14#3b (d2)
  - confondre prévention par vaccin et traitement par sérum — ligne C12#5b (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `10/quiz#2`, `10/quiz#3`, `10/quiz#4`, `10/02-boss#1`, `10/02-boss#2`, `10/02-boss#4`, `10/02-boss#5`, `10/03-revision#2`, `10/03-revision#6`, `10/05-entrainement#1`, `10/05-entrainement#3`, `10/05-entrainement#5`, `10/05-entrainement#6`
- Note : Le patron dit « التلقيح » pour la vaccination (le manuel aussi : en 6ᵉ, التلقيح ≠ التأبير). Les erreurs du manuel (vaccins par scarification, immunité « naturelle » de l'inflammation) ne sont pas reprises. Ne pas redemander la définition du vaccin déjà posée en 10/quiz#4 : la mission demande ce que le vaccin n'est PAS (globules rouges, après l'infection, immunité naturelle).

### m022 → `exercices/07-devoir-plaie-infection-et-conseils.json` · d2 practice 75/15 · 7 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐: … ») : Une plaie : l'hygiène, les phases de l'infection, vaccin ou sérum, des conseils de santé
- Registre : id `D05#3` ; sources `D05#3, D05#4, D06#3, D07#5, D08#3`
- Cartes : devoir E (T2, école primaire), exercices 3, 4 ; devoir F (T2, école primaire), exercice 3 ; devoir G (T3, école primaire), exercice 5 ; devoir H (T3, école primaire), exercice 3 ; la copie de G dans un lot de matières n'est pas comptée — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D05#3 (d2) : nommer le geste d'hygiène sur une plaie et justifier le pansement
  - D05#4 (d2) : remettre en ordre les phases de l'infection d'une plaie
  - D06#3 (d1) : énumérer les phases de l'infection d'une plaie
  - D07#5 (d2) : cocher les propriétés d'un vaccin et d'un sérum dans un tableau
  - D08#3 (d2) : justifier trois conseils de santé par leur effet
- Étapes prévues :
  - Le geste d'hygiène sur une plaie et le rôle du pansement (une barrière contre les microbes) — QCM, QCM — 2 q
  - Les phases de l'infection d'une plaie, dans l'ordre (rougeur, gonflement, arrivée des globules blancs, pus) : trois à quatre temps ; ne pas oublier l'intervention des cellules de défense — ordering, QCM — 2 q
  - Vaccin et sérum : un tableau à cocher (prévention ou traitement, avant ou après l'infection) — matching — 1 q
  - Deux conseils de santé à justifier par leur effet (manger des aliments de construction pour grandir, se faire vacciner) ; le conseil sur l'eau est laissé à la mission des maladies hydriques du `05` — deux QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - oublier la barrière contre les microbes — ligne D05#3 (d2)
  - placer la phagocytose avant la rougeur — ligne D05#4 (d2)
  - omettre l'intervention des cellules de défense — ligne D06#3 (d1)
  - confondre prévention et traitement — ligne D07#5 (d2)
  - donner un effet sans lien avec le conseil — ligne D08#3 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `10/01-pratique#4`, `10/01-pratique#5`, `10/01-pratique#6`, `10/02-boss#2`, `10/02-boss#4`, `10/03-revision#3`, `10/03-revision#5`, `10/05-entrainement#3`, `10/05-entrainement#6`, `10/quiz#5`
- Note : Salle blanche. Gestes absents des examens : l'ordre des phases de l'infection, l'hygiène de la plaie, les conseils de santé justifiés. L'ordering du patron (10/05-entrainement#6) a cinq temps de la plaie ; ici, trois à quatre temps d'un autre découpage. Le conseil sur l'eau recoupe la mission « eau polluée » du `05` : un seul des trois conseils s'y rapporte.
