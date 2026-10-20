# Carte d’affectation M3 — éveil scientifique 6ᵉ, chapitres `04`, `06`, `05` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 10 missions (8 d’examen, 2 de devoir), 99 questions ; 2 auteurs : `04` + `06` d’un côté, `05` de l’autre. Skills : `content-ecole-tn`, puis `prof-eveil-primaire` (calibre les étages, jamais plus que le programme de 6ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/eveil/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend un support (ou une situation) et ses consignes, découpés en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne la phrase OFFICIELLE de la transcription qu'elle lit (consigne et énoncé tels qu'imprimés, coquilles incluses sauf celles que la carte nomme) ; une consigne ouverte (« أفسّر », « أعلّل », « أصلح كلّ خطأ », « أقترح تجربة ») devient un QCM de l'explication ou de la correction, un `ordering` (étapes d'un protocole, trajet), un `matching` (légende ↔ nom, tableau) ou un `multi` (relevés, vrai/faux motivés) ; `short_answer` seulement pour UN terme du معجم avec ses `acceptedAnswers` ; aucun tracé n'est demandé à la main : un tracé de rayon, de flèche ou d'aiguille devient « quel dessin est exact ? » (QCM visuel) ; figures, schémas d'expériences et tableaux refaits en SVG, vrais, SANS donner la clé ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Chiffres du ملفّ du guide (78 %, 21 %, 2 : 1, 55 %, 1/6, 5 millions…) : enrichissement seulement, JAMAIS une clé ni un distracteur (V1) ; les quatre valeurs permises sont 1/5 d'oxygène, 1 L d'air ≈ 1,3 g, eau = 2/3 du corps, 120 jours (fiche §4 bis, point 4). Sont enseignés, donc exerçables : les plaquettes (V2 révisé), les huit directions (V5) ; l'« intensité » du courant n'est pas exigible (V3) ; la potabilisation est une lecture de schéma sans clé de mémorisation (V4). Chaque DÉFAUT d'énoncé que la carte nomme est corrigé dans la reprise, comme la carte le dit, et l'explication le signale. Étiquettes : `misconceptionTag` du registre `eveil.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/eveil/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-eveil/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject eveil-scientifique-6eme` (0 erreur), `content:tranche -- --subject eveil-scientifique-6eme --changed --fresh --strict-longest`.

**🔁 À REVÉRIFIER AU LANCEMENT (E-12).** Les 12 chapitres d'éveil seront mis à niveau sur la fiche programme APRÈS ce plan (cours au patron, exercices, étiquettes). Tous les « Ne pas redemander » de cette carte sont établis sur les exercices TELS QU'ILS SONT AU 2026-10-20 (état du 28 septembre : 5 fichiers de 6 questions à choix + un quiz de 5 questions par chapitre, tous des QCM) : ils sont PROVISOIRES. Au lancement de chaque mission, relis les exercices et le cours du chapitre tel qu'il sera alors, refais le croisement question par question, et mets la liste à jour avant d'écrire. Les numéros de fichiers (`06`, `07`, …) supposent que les chapitres ont `01`–`05` : si la mise à niveau ajoute un fichier, décale. Si un item que la carte cible (plaquettes, huit directions, sang décanté, sonnerie, monoxyde de carbone…) n'est pas enseigné par le chapitre mis à niveau, arrête-toi et signale-le : la mission ne part pas avant le cours.

**Ordre de travail** : (1) les ids d’étiquette neufs que tu poses ; (2) les missions du chapitre, dans l’ordre de la carte ; (3) les gates. **Départ du lot** : seulement quand ses chapitres ont été mis à niveau sur la fiche (E-11).


## Chapitre `04-nutrition` — التغذية عند الإنسان

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.nutri.origine-et-groupe-confondus` (Tu mélanges l'origine d'un aliment (animale ou végétale) et ) | `eveil.nutri.maladies-de-carence-confondues` (Tu confonds les maladies de carence : scorbut = vitamine C () | `eveil.nutri.quantite-au-lieu-de-variete` (Tu crois que manger beaucoup suffit : c'est la présence des ) | `eveil.nutri.vitamines-donnent-energie` (Tu crois que les vitamines et les sels minéraux donnent de l) | `eveil.nutri.un-seul-groupe-suffit` (Tu crois qu'un seul groupe d'aliments suffit selon le besoin) | `eveil.nutri.malnutrition-seulement-par-manque` (Tu crois que la malnutrition, c'est seulement manquer de nou) | `eveil.nutri.eau-moins-vitale-que-nourriture` (Tu crois qu'on tient plus longtemps sans eau que sans nourri)

### m023 → `exercices/06-exams-2018-2026-le-repas-equilibre-composer-et-justifier.json` · d3 boss 120/30 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2018–2026 ⭐⭐⭐: … ») : Concours 2018 · 2019 · 2022 · 2024 · 2026 · le repas équilibré : composer, justifier, lire un diagramme
- Registre : id `C03#1` ; sources `C03#1, C08#3, C09#4, C01#12, C05#12`
- Sources : C03 (session 2024), situation 1, support 1 ; C08 (session 2019), situation 1, support 2 ; C09 (session 2018), support 2, consigne 1 ; C01 (session 2026), situation intégrative, support 2, consigne 2-3 ; C05 (session 2022), situation intégrative, support 3, consigne 3-1-أ — transcriptions `2026-unique.md`, `2024-unique.md`, `2022-unique.md`, `2019-unique.md`, `2018-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2024 · بيّن من خلال السّند السّابق أنّ الوجبة التي أعدّتها أمّي وجبة متوازنة. (pâte à pizza, huile d'olive, tomates, poivron, champignons, thon, fromage)
  - 2019 · أعلّل سبب عدم توازن وجبة غداء ريم بذكر المجموعة الغذائيّة النّاقصة. (une salade et un poisson grillé)
  - 2018 · كوّن وجبة غذاء مناسبة للجدّ ممّا يلي : كسكسي بلحم الضّأن – سلطة خضر – سمك مشويّ – زبدة – برتقال
  - 2026 · يبيّن هذا المخطّطُ نسبة كلّ مجموعة غذائيّة في كلّ وجبة من وجبات الغداء التي تناولها منيرٌ وأبوه وجدُّه. بيّنْ الخلل في كلٍّ من وجبة منير ووجبة جدّه. (وجبة الجد : 90 %, 5 %, 5 % ; وجبة منير : 50 %, 50 %, 0 % ; وجبة الأب : 45 %, 20 %, 35 % — طاقة / نمو / وقاية)
  - 2022 · أعمّر الفراغ بالإفادة المناسبة. يحتاج أعضاء الفريق إلى وجبة غداء تكون فيها أغذية ......... متوفّرة بنسبة أكبر. / ......... ناتج عن نقص في تناول الأغذية أو إفراط في استهلاك نوع منها.
- Étapes prévues :
  - 2024 : montrer que le repas contient les trois groupes (énergie : pâte, huile ; construction : thon, fromage ; protection : tomates, poivron) — multi des aliments par groupe, QCM de la conclusion « donc équilibré » — 2 q
  - 2019 : un déjeuner sans l'un des groupes ; nommer le groupe manquant (le groupe d'énergie, pour une salade et un poisson) — QCM (le leurre est un aliment, pas un groupe) — 1 q
  - 2018 : composer le repas du grand-père à partir de cinq aliments (au moins un de chaque groupe, sans excès de graisse) — multi, QCM de la justification — 2 q
  - 2026 : lire le diagramme à barres ; chaque repas de Munir (pas d'aliments de protection) et du grand-père (presque uniquement de l'énergie) : nommer le groupe en défaut — trois QCM (diagramme refait en SVG, avec les trois séries ; la valeur exacte n'est jamais la clé) — 3 q
  - 2022 : après un effort on a besoin des aliments d'énergie ; la malnutrition vient d'un manque ou d'un excès — deux QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - citer des aliments sans les rattacher à leur groupe — ligne C03#1 (d2)
  - citer un aliment au lieu du groupe — ligne C08#3 (d2)
  - omettre un groupe d'aliments — ligne C09#4 (d2)
  - décrire les barres sans nommer le groupe en défaut — ligne C01#12 (d3)
  - confondre carence et excès — ligne C05#12 (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `04/quiz#1`, `04/quiz#2`, `04/quiz#3`, `04/quiz#4`, `04/02-boss#6`, `04/03-revision#4`, `04/03-revision#5`, `04/03-revision#6`, `04/04-defi#4`, `04/04-defi#5`, `04/04-defi#6`, `04/05-entrainement#4`, `04/05-entrainement#6`
- Note : Le diagramme 2026 montre des pourcentages de groupes : ils sont un support à lire, jamais un fait à retenir (V1). Les trois groupes du manuel sont البناء، الطاقة، الوقاية (manuel p.88) ; les six rubriques d'origine du درس 20 ne sont pas des groupes. Placement au `04` pour les cinq lignes (aucune ne dépasse la nutrition).

### m024 → `exercices/07-exams-2010-2023-classer-les-aliments-et-leurs-roles.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2010–2023 ⭐⭐: … ») : Concours 2010 · 2020 · 2021 · 2023 · classer les aliments et dire leur rôle
- Registre : id `C04#4` ; sources `C04#4, C04#5, C07#11, C07#12, C17#4a, C06#3`
- Sources : C04 (session 2023), situation 1, support 2, consignes 2-أ et 2-ب ; C07 (session 2020), situation intégrative, consignes 5 et 6 ; C17 (session 2010), support 4 ; C06 (session 2021), situation 1, consigne 3 — transcriptions `2023-unique.md`, `2021-unique.md`, `2020-unique.md`, `2010-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2023 · أصنّف ثلاثة أغذية من السّند حسب وظائف الأغذية الثّلاث في الجدول. (les six aliments du sujet : fromage blanc, pain, beurre, laitue, orange, huile d'olive — les noms arabes sont ceux de la transcription)
  - 2023 · أفسّر قول المشرف : « يجب أن تتناولوا وجبة غذائيّة متوازنة ».
  - 2020 · أصنّف في الجدول الأغذية التّالية : الحمّص – المعدنوس – زيت الزّيتون – الأرزّ – البيض. (غنيّ بالزّلاليّات · بالسّكّريّات · بالأملاح المعدنيّة · بالدّهنيّات)
  - 2020 · أصلح كلّ خطأ ورد في الإفادة التّالية : أغذية الطّاقة غنيّة بالزّلاليّات الّتي تقي الجسم من الأمراض.
  - 2010 · أتأمّل الجدول التّالي وأكمل خاناته الفارغة بـ : البرتقال – البيض – الجبن – البقول الجافّة – الخبز (من أغذية الطّاقة · النمو والبناء · الوقاية)
  - 2021 · أكمل الإفادات التّالية بالتّفسير الملائم : يتناول المسنّ الخضروات والفواكه لأنّها توفّر ......... و ......... لوقاية الجسم. · يحتاج الطّفل إلى الزّلاليّات لأنّها تساعد الجسم على .........
- Étapes prévues :
  - 2023 (2-أ) : trois aliments choisis dans la liste et leur fonction (construction, énergie, protection) — matching — 1 q
  - 2023 (2-ب) : pourquoi un repas équilibré (les trois groupes réunis) — QCM — 1 q
  - 2020 (5) : cinq aliments à répartir en quatre colonnes de nutriments (les pois chiches : protéines ; le riz : sucres ; l'huile : graisses ; le persil : sels minéraux ; l'œuf : protéines) — matching, QCM sur le persil et sur le pois chiche — 2 q
  - 2020 (6) : « les aliments d'énergie sont riches en protéines qui protègent » : deux erreurs (énergie ≠ protéines ; protéines ≠ protection) — QCM de l'erreur, QCM de la phrase corrigée — 2 q
  - 2010 : cinq aliments répartis entre les trois groupes (orange : protection ; œuf et fromage et légumineuses : construction ; pain : énergie) — matching, QCM sur une légumineuse — 2 q
  - 2021 : les fruits et légumes apportent des vitamines et des sels minéraux (protection) ; les protéines servent à la croissance (construction) — deux QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - ranger un aliment dans la mauvaise fonction — ligne C04#4 (d2)
  - répondre « manger beaucoup » — ligne C04#5 (d2)
  - ranger un légume dans les sucres — ligne C07#11 (d2)
  - attribuer la protection aux protéines — ligne C07#12 (d1)
  - classer un aliment polyvalent dans un seul groupe — ligne C17#4a (d1)
  - attribuer aux protéines le rôle d'énergie — ligne C06#3 (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `04/quiz#1`, `04/quiz#2`, `04/quiz#3`, `04/02-boss#1`, `04/02-boss#2`, `04/02-boss#3`, `04/03-revision#1`, `04/03-revision#2`, `04/05-entrainement#1`, `04/05-entrainement#2`, `04/05-entrainement#4`
- Note : Le sujet 2020 classe par nutriment (quatre colonnes) alors que 2023 et 2010 classent par fonction (trois groupes) : la mission garde les deux gestes. Le persil comme source de sels minéraux : un légume frais, déjà dans « fruits et légumes = vitamines et sels minéraux » du patron — rien de ◐. Un « aliment polyvalent » (2010) n'est rangé que dans un groupe.

### m025 → `exercices/08-exams-2008-2024-carences-fer-vitamines-et-malnutrition.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2024 ⭐⭐⭐: … ») : Concours 2008 · 2020 · 2021 · 2022 · 2023 · 2024 · les carences : le fer, les vitamines, la malnutrition
- Registre : id `C04#6` ; sources `C04#6, C05#13, C19#3a, C03#4, C07#2, C06#1`
- Sources : C04 (session 2023), situation 1, support 2, consigne 2-ج ; C05 (session 2022), situation intégrative, support 3, consigne 3-1-ب ; C19 (session 2008), support 3 ; C03 (session 2024), situation 1, support 2, consigne 2-2 ; C07 (session 2020), situation 1, support 2, consigne 1 ; C06 (session 2021), situation 1, consigne 1 — transcriptions `2024-unique.md`, `2023-unique.md`, `2022-unique.md`, `2021-unique.md`, `2020-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2023 · أصلح الخطأ الوارد في الإفادة التّالية محافظا على العبارة المسطّرة. نقص الأملاح المعدنيّة في الطّعام يتسبّب في الإصابة __بضعف البصر (العشى اللّيليّ)__.
  - 2022 · أصلح كلّ خطأ ورد في الإفادة التّالية. أملاح الحديد أغذية عضويّة ضروريّة للوقاية من الأمراض، ونقصانها يسبّب تسوّس الأسنان.
  - 2008 · أصلح الخطأ الوارد في قول مراد. (مراد : « أمّي مصابة بفقر الدّمّ بسبب نقص فيتامين د ») الإصلاح : إنّ سبب إصابة أمّي بفقر الدّمّ هو ........
  - 2024 · أصلح الخطأ في الإفادة التّالية. الحديد يدخل في تركيبة الكريّات البيضاء ونقصانه يسبّب الهزال الرّزّي.
  - 2020 · أبيّن الأمراض الّتي تشتكي منها الخالة فوزيّة استنادا إلى وصفة الطّبيب. (دواءان : أحدهما أملاح الحديد، الآخر فيتامين « أ »)
  - 2021 · أصلح الأخطاء الواردة في الإفادة التّالية : حسب نتائج التّحاليل، تحتاج الحالة فاطمة إلى تناول أغذية توفّر على الفيتامين "ب 1" في إطار علاج مرض الهزال الرّزّي. (جدول : كريّات حمراء، بيضاء، صفيحات، فيتامين ب 12، فيتامين د، فيتامين ب 1)
- Étapes prévues :
  - 2023 : le trouble de la vue vient d'une carence en vitamines, et non en sels minéraux ; le nom du trouble est donné dans l'énoncé (jamais demandé) — QCM — 2 q
  - 2022 : les sels de fer sont minéraux (pas organiques) ; leur manque cause l'anémie (pas les caries) — deux QCM — 2 q
  - 2008 : l'anémie vient d'un manque de fer (pas de vitamine D) ; pourquoi : le fer entre dans le globule rouge — deux QCM — 2 q
  - 2024 : le fer est dans les globules rouges, pas les blancs ; la phrase corrigée dit « anémie » (le mot « الهزال الرزّي » est une coquille du sujet, jamais reprise) — QCM, QCM — 2 q
  - 2020 : de l'ordonnance (fer, vitamine) déduire une anémie et une carence en vitamine — la vitamine est nommée « vitamine A » dans l'énoncé seulement ; ne pas demander le nom du trouble de la vue — QCM, QCM — 2 q
  - 2021 : le tableau d'analyses refait lisible, une seule valeur sous la norme (la vitamine D) ; la carence en vitamine D cause le rachitisme (الكساح) ; les autres lignes sont données dans la norme — QCM de la valeur, QCM de la maladie — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - accuser les sels minéraux au lieu d'une vitamine — ligne C04#6 (d2)
  - dire que le fer est une substance organique — ligne C05#13 (d2)
  - confondre carence en fer et carence vitaminique — ligne C19#3a (d2)
  - rattacher le fer aux globules blancs — ligne C03#4 (d1)
  - ne retenir que l'anémie — ligne C07#2 (d3)
  - choisir la vitamine d'une autre valeur / confondre deux maladies carentielles — ligne C06#1 (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `04/04-defi#1`, `04/04-defi#6`, `04/05-entrainement#5`, `04/03-revision#3`, `03/04-defi#5`, `03/04-defi#6`, `03/02-boss#6`, `03/05-entrainement#6`
- Note : Quatre HP du lecteur (`fer`, `cecite-nocturne`, `analyses-sanguines`, `moelle-osseuse`) : le fer et l'anémie sont déjà dans le patron et dans le ملفّ (E-7) ; la cécité nocturne n'est qu'un nom donné ; le tableau d'analyses chiffré n'est qu'un support (E-8). « الهزال الرزّي » (2021, 2024) est une coquille du guide aussi (fiche §6.3) : ne jamais la reprendre. Le tableau 2021 imprime « ≤ 30 » pour la valeur usuelle de la vitamine D, ce qui rend toutes les lignes normales : c'est sans doute un « ≥ 30 » mal lu ; relire le PDF (sha256 au registre) avant de refaire le tableau lisible, avec une seule valeur sous la norme.

### m026 → `exercices/09-devoir-petit-dejeuner-croissance-carence.json` · d2 practice 75/15 · 7 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐: … ») : Petit déjeuner et croissance : classer, définir, corriger
- Registre : id `D04#5` ; sources `D04#5, D04#6, D04#9, D04#11, D06#1, D06#2, D06#8`
- Cartes : devoir D (T2, école primaire), exercices 5, 6, 9, 11 ; devoir F (T2, école primaire), exercices 1, 2, 8 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D04#5 (d1) : justifier qu'un menu ne soit pas équilibré
  - D04#6 (d1) : nommer la cause d'une carence à symptômes bien connus
  - D04#9 (d1) : définir quand un repas est équilibré
  - D04#11 (d1) : corriger le besoin alimentaire principal d'un enfant en croissance
  - D06#1 (d1) : classer les aliments d'un petit déjeuner en trois catégories fonctionnelles
  - D06#2 (d1) : corriger une définition erronée du rôle des aliments énergétiques
  - D06#8 (d2) : corriger une répartition erronée des nutriments entre catégories d'aliments
- Étapes prévues :
  - Les aliments d'un petit déjeuner à classer en trois catégories fonctionnelles — matching — 1 q
  - Un menu qui n'est pas équilibré : nommer les groupes manquants (pas les aliments) ; définir quand un repas est équilibré — deux QCM — 2 q
  - Corriger une définition du rôle des aliments énergétiques (ils fournissent l'énergie, ils ne servent pas à la croissance) ; le besoin principal d'un enfant en croissance (les aliments de construction, pas les graisses) — deux QCM — 2 q
  - Corriger une répartition des nutriments entre catégories (vitamines et protéines intervertis) — QCM — 1 q
  - Une carence aux symptômes bien connus : nommer sa cause (la vitamine, pas le sel minéral) — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - ne pas nommer les groupes d'aliments manquants — ligne D04#5 (d1)
  - confondre deux carences — ligne D04#6 (d1)
  - croire que les graisses priment — ligne D04#11 (d1)
  - ranger un laitage parmi les aliments d'énergie — ligne D06#1 (d1)
  - attribuer aux énergétiques le rôle de croissance — ligne D06#2 (d1)
  - intervertir vitamines et protéines — ligne D06#8 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `04/quiz#1`, `04/quiz#2`, `04/quiz#3`, `04/quiz#4`, `04/02-boss#1`, `04/02-boss#2`, `04/02-boss#3`, `04/02-boss#6`, `04/03-revision#2`, `04/03-revision#4`, `04/03-revision#5`, `04/05-entrainement#1`, `04/05-entrainement#2`, `04/05-entrainement#4`
- Note : Salle blanche. Cette mission recoupe beaucoup le patron : le geste neuf est la CORRECTION d'une définition erronée en deux étapes (trouver l'erreur, choisir la phrase juste) et le classement d'un petit déjeuner. À revérifier de très près au lancement : si la mise à niveau du `04` absorbe ces gestes, couper cette mission avant les autres (E-1).


## Chapitre `06-reproduction-florale` — التّكاثر الزّهريّ

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.flor.organes-protecteurs-et-reproducteurs-confondus` (Tu confonds les organes de la fleur : sépales et pétales pro) | `eveil.flor.type-pollinisation-par-l-agent` (Tu décides du type de pollinisation par l'agent (insecte, ve) | `eveil.flor.pollinisation-et-fecondation-confondues` (Tu confonds pollinisation et fécondation : la pollinisation ) | `eveil.flor.fruit-sans-pollinisation` (Tu crois que l'ovaire devient un fruit sans pollinisation ni) | `eveil.flor.fleur-entiere-devient-fruit` (Tu crois que la fleur entière, le calice ou l'ovule devient ) | `eveil.flor.plante-nait-du-pollen` (Tu crois que la nouvelle plante naît du grain de pollen : el) | `eveil.flor.annuelle-ne-se-reproduit-pas` (Tu crois qu'une plante annuelle meurt parce qu'elle ne se re)

### m027 → `exercices/06-exams-2009-2017-pollinisation-abeille-fleur-et-protection.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2009–2017 ⭐⭐: … ») : Concours 2009 · 2012 · 2013 · 2015 · 2017 · la pollinisation : l'abeille, la fleur, la protection
- Registre : id `C10#1b` ; sources `C10#1b, C14#1a, C12#7a, C15#3a, C18#1b`
- Sources : C10 (session 2017), support 1, consigne 2 ; C14 (session 2013), support 1, consigne 1 ; C12 (session 2015), support 7 ; C15 (session 2012), support 3 ; C18 (session 2009), support 1, consigne 2 — transcriptions `2017-unique.md`, `2015-unique.md`, `2013-unique.md`, `2012-unique.md`, `2009-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2017 · أتأمّل الرسم وأتمّم الفراغات بالعبارات المناسبة. (تحطّ النحلة على الزهرة ........ فيحتك جسمها بالمئبر ثمّ تطير وتحطّ على الزهرة ........ فتنتقل بواسطتها حبّات الطلع إلى ميسم الزهرة الأخرى ويسمّى هذا النوع من التأبير ........)
  - 2013 · ألاحظ الرسم وأجيب. يتمّ التأبير في الزهرة رقم : ........ أعلّل إجابتي ........ (deux fleurs ; la fleur 2 est enfermée dans « غطاء بلاستيكي »)
  - 2015 · أتأمّل الرّسوم الآتية وأكتب رقم الوضعيّة التي يتمّ فيها التأبير والإخصاب مع التعليل المناسب. (الوضعيّة 1 : fleur ouverte ; 2 : fleur dans un « كيس من البلاستيك » ; 3 : fleur sans étamines)
  - 2012 · أختارُ التعليل الصحيح بوضع علامة (x) في الخانة المناسبة : يتدخّل الفلاّح في تأبير زهرة النخيل لأنها ناقصة تشتمل على مدقّة فقط · النّبات هو منتج لأنه يصنع المــواد العضويّــة · يتمّ الإخصاب لأنّ حبّات الطلع تنتقل من الميسم إلى المئبر
  - 2009 · أصلح الخطأ في إفادة الأخ إن وُجد. (يساهم النّحل في عمليّة التّأبير الذّاتي.)
- Étapes prévues :
  - 2017 (1-ب) : le texte à trous de l'abeille entre la fleur A (pistil seul) et la fleur B (étamines) : le type de pollinisation est croisée — deux QCM de blancs, un QCM du mot final — 2 q
  - 2013 (1) : laquelle des deux fleurs est pollinisée (celle qui n'est pas sous le plastique) et pourquoi (le plastique empêche l'abeille d'atteindre le pollen et le stigmate) — QCM, QCM — 2 q
  - 2015 (7) : trois situations ; celle où pollinisation et fécondation sont possibles (fleur ouverte avec étamines et pistil) et pourquoi les deux autres échouent — QCM visuel, QCM de la justification — 2 q
  - 2012 (3) : trois énoncés accompagnés d'explications, à juger un par un d'après le manuel : celle qui inverse le sens du pollen (de l'étamine au stigmate, jamais l'inverse) est fausse ; celle du palmier est ◐ (fleur sans étamines : le pollen vient d'ailleurs, sans « fleur incomplète » comme clé) ; celle du producteur relève du `05` — multi, QCM — 2 q
  - 2009 (1-2) : l'abeille assure la pollinisation croisée, jamais directe — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre pollinisation et fécondation — ligne C10#1b (d2)
  - ignorer la protection qui bloque l'accès à l'insecte — ligne C14#1a (d2)
  - croire que le pistil seul suffit sans pollen — ligne C12#7a (d2)
  - inverser le sens du transport du pollen — ligne C15#3a (d2)
  - confondre pollinisation directe et croisée — ligne C18#1b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `06/02-boss#1`, `06/02-boss#2`, `06/02-boss#3`, `06/02-boss#4`, `06/02-boss#5`, `06/02-boss#6`, `06/03-revision#2`, `06/03-revision#3`, `06/04-defi#1`, `06/04-defi#2`, `06/04-defi#3`, `06/quiz#3`, `06/quiz#5`
- Note : « التأبير » est le mot du manuel (en 6ᵉ, التلقيح = vaccination) : si un sujet écrit autrement, l'auteur emploie التأبير. La « fleur incomplète » du palmier est ◐ (E-8) : ne pas faire de « fleur incomplète/unisexuée » une clé, seulement « fleur sans étamines : le pollen vient d'ailleurs ». La 2ᵉ proposition de 2012 (producteur) est un item de `05` : on la garde ici car elle appartient à la même consigne.

### m028 → `exercices/07-exams-2009-2018-la-fleur-le-fruit-et-le-cycle.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2009–2018 ⭐⭐: … ») : Concours 2009 · 2010 · 2017 · 2018 · la fleur, le fruit et le cycle de vie
- Registre : id `C17#2a` ; sources `C17#2a, C18#1a, C09#1, C09#2, C10#1a`
- Sources : C17 (session 2010), support 2 ; C18 (session 2009), support 1, consigne 1 ; C09 (session 2018), support 1, consignes 1 et 2 ; C10 (session 2017), support 1, consigne 1 — transcriptions `2018-unique.md`, `2017-unique.md`, `2010-unique.md`, `2009-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2010 · أعيد كتابة كلّ إفادة مع إصلاح الخطأ إن وجد. أ- تقوم الرّياح بتأبير العديد من النّباتات والأشجار. ب- تمثّل الأسدية العضو الأنثوي في الزّهرة والمدقّة العضو الذكري فيها. ج- بعد عمليّة الإخصاب يتحوّل المبيض إلى بذرة والبويضة إلى ثمرة.
  - 2009 · أربط بسهم كلّ عنصر من عناصر الزّهرة بوظيفته. (السّداة · التويج · حبّات الطّلع ↔ تخصيب البويضات · حماية الأعضاء الدّاخليّة للزّهرة · حمل المئبر)
  - 2018 · تعرّف الظّاهرة واكتبها داخل الإطار : تنتقل حبّات الطّلع من متبر زهرة إلى ميسم زهرة أخرى. · تستقرّ حبّة الطّلع على الميسم فتنبت أنبوب الإخصاب.
  - 2018 · أكتب أسماء مراحل الدّورة الحياتيّة المحدّدة أسفله لنبتة زهريّة. (بذرة → نبتة → زهرة → بذرة)
  - 2017 · أجيب بـ "صواب" أو "خطأ" في الخانة المناسبة. للنحل دور هام في حياة الزهرة. · يصنّف العسل ضمن أغذية الطاقة. · النحل كائن منتج في علاقته ببعض الكائنات الحيّة.
- Étapes prévues :
  - 2010 : trois énoncés dont deux sont faux (les étamines sont l'organe mâle, le pistil l'organe femelle ; le fruit vient de l'ovaire et la graine de l'ovule) ; le premier (le vent pollinise) est juste — trois QCM — 3 q
  - 2009 : relier trois éléments à leur fonction (étamine : porte l'anthère ; corolle : protège ; grain de pollen : féconde les ovules) — matching — 1 q
  - 2018 (1) : nommer deux phénomènes (pollinisation croisée ; fécondation après la germination du tube) — deux QCM ; (2) nommer les trois étapes d'un cycle fléché (graine, plante, fleur) — ordering ou matching — 3 q
  - 2017 (1) : trois énoncés sur l'abeille, le miel et le producteur (l'abeille aide la fleur ; le miel est un aliment d'énergie ; l'abeille est un consommateur, pas un producteur) — multi, QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - échanger organe mâle et organe femelle — ligne C17#2a (d2)
  - confondre protection et reproduction — ligne C18#1a (d1)
  - confondre transport du pollen et fécondation — ligne C09#1 (d1)
  - oublier la fructification — ligne C09#2 (d1)
  - confondre producteur et consommateur — ligne C10#1a (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `06/01-pratique#1`, `06/01-pratique#2`, `06/01-pratique#3`, `06/01-pratique#4`, `06/01-pratique#5`, `06/01-pratique#6`, `06/02-boss#2`, `06/02-boss#3`, `06/03-revision#1`, `06/03-revision#3`, `06/03-revision#4`, `06/03-revision#5`, `06/05-entrainement#1`, `06/05-entrainement#3`, `06/05-entrainement#4`
- Note : La fleur et ses parties sont très largement servies par le patron : la mission apporte la forme d'examen (énoncés à corriger, appariement, cycle fléché) et les confusions de genre (organe mâle/femelle, ovule/ovaire). « متبر » (2018) est une coquille pour « مئبر » : ne pas la reprendre. « أنبوب الإخصاب » : à vérifier au manuel avant de le poser en clé.


## Chapitre `05-milieu-chaines-alimentaires` — الوسط البيئي: السلسلة الغذائيّة وتلوّث المياه

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.eco.plante-sans-lumiere` (Tu crois qu'une plante verte peut vivre sans lumière si on l) | `eveil.eco.fleche-lue-a-l-envers` (Tu lis la flèche de la chaîne alimentaire à l'envers : elle ) | `eveil.eco.rang-du-consommateur-mal-compte` (Tu comptes mal le rang d'un consommateur : on part de la pla) | `eveil.eco.champignon-producteur` (Tu crois que le champignon est un producteur comme la plante) | `eveil.eco.origine-pollution-par-arrivee` (Tu juges l'origine d'une pollution par l'endroit où elle arr) | `eveil.eco.eau-limpide-donc-potable` (Tu crois qu'une eau limpide ou filtrée est sans microbes : l) | `eveil.eco.virus-et-bacterie-confondus` (Tu confonds les causes : le choléra et la fièvre typhoïde so) | `eveil.eco.eau-polluee-seulement-si-bue` (Tu crois que l'eau polluée ne rend malade que celui qui la b)

### m029 → `exercices/06-exams-2016-2026-construire-et-corriger-une-chaine-alimentaire.json` · d3 boss 120/30 · 11 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2016–2026 ⭐⭐⭐: … ») : Concours 2016 · 2019 · 2023 · 2024 · 2025 · 2026 · construire et corriger une chaîne alimentaire
- Registre : id `C01#9` ; sources `C01#9, C02#9, C04#12, C11#3a, C11#3b, C03#12, C08#13`
- Sources : C01 (session 2026), situation intégrative, support 1 ; C02 (session 2025), situation intégrative, support 1, consigne 1-أ ; C04 (session 2023), situation intégrative, support 1, consigne 1-أ ; C11 (session 2016), support 3 ; C03 (session 2024), situation intégrative, support 3, consigne 3-1-أ ; C08 (session 2019), situation intégrative, support 3, consigne 2-أ — transcriptions `2026-unique.md`, `2025-unique.md`, `2024-unique.md`, `2023-unique.md`, `2019-unique.md`, `2016-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · هذا مشهد لوسط بيئيّ صحراويّ. كوّنْ سلسلة غذائيّة تضمّ خمسَ حلقات معتمدا العلاقة " .. يتغذّى على.. " ولا تنسَ الأسهم المبيّنة لهذه العلاقة. (عُقاب، فنك، يربوع، أفعى)
  - 2025 · كوّن سلسلة غذائيّة وفق العلاقة (... يتغذّى على ...) بواسطة كلّ الكائنات الحيّة التي تبيّنها الصّور التالية وبالرّجوع إلى السّند، لا تنسَ وضع الأسهم. (حرباء، بومة، تين شوكيّ، دعسوقة ; la cochenille est dans le texte)
  - 2023 · أصلح كلّ خطإ ورد في السّلسلة الغذائيّة الّتي كوّنها شادي باعتماد السّند. (ضِفْدَعَة, شَقَائِقُ النُّعْمانِ, ثُعْبَانٌ, جَرَادَةٌ, فَرَاشَةٌ, قَمْحٌ, دُودَةٌ ; chaîne imprimée : دودة — ثعبان — ضفدعة — فراشة)
  - 2016 · أصلح الخطأ في السلسلة الغذائية التالية : (بكتيريا ← فأر ← أفعى ← سنبلة) · أعلّل إجابتي.
  - 2024 · صِلْ بأسهم بين عناصر السّلسلة الغذائيّة التّالية معتمدا العلاقة : (..غذاء لـ..) (نسر، صنوبر، ثعبان، فأر الحقول)
  - 2019 · أربط بسهم بين الكائنات الحيّة التّالية وفقا للعلاقة "... يتغذّى على ..." للحصول على سلسلة غذائيّة : (بكتيريا، صنوبر حلبيّ، سنجاب، صقر)
- Étapes prévues :
  - 2026 : cinq maillons à partir de quatre animaux photographiés : le producteur (une plante de l'oasis) manque et doit être choisi — ordering des cinq maillons, QCM du maillon manquant — 2 q
  - 2025 : chaîne à cinq maillons avec la cochenille citée dans le texte (figuier de Barbarie, cochenille, coccinelle, caméléon, chouette) — ordering, QCM du maillon donné par le texte — 2 q
  - 2023 : sept êtres vivants et une chaîne fautive (flèches, ordre, intrus) : repérer les erreurs et rétablir la chaîne — QCM de l'erreur sur le sens, QCM de l'intrus, QCM de la chaîne juste — 3 q
  - 2016 : une chaîne écrite à l'envers (bactéries en tête) : la rétablir et dire pourquoi la bactérie est en dernier maillon — QCM de la chaîne juste, QCM de la justification (la flèche suit « se nourrit de ») : voir E-5 — 2 q
  - 2024 : relier quatre êtres vivants par des flèches. Le sujet emploie « غذاء لـ » (flèche de l'aliment vers le mangeur) ; la mission est NORMALISÉE sur le sens du manuel « يتغذّى على » (flèche du mangeur vers l'aliment) — matching ; QCM du sens des flèches — 1 q
  - 2019 : relier quatre êtres (les bactéries sont le dernier maillon) — ordering — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - inverser le sens des flèches / oublier le producteur non photographié — ligne C01#9 (d2)
  - oublier le maillon cité dans le texte / flèches à l'envers — ligne C02#9 (d2)
  - flèches à l'envers / maillons dans un ordre faux / intrus — ligne C04#12 (d3)
  - orienter les flèches dans le mauvais sens — ligne C11#3a (d2)
  - confondre le sens de la flèche avec la direction du transfert — ligne C11#3b (d2)
  - tracer les flèches du mangeur vers l'aliment — ligne C03#12 (d2)
  - flèches à l'envers / placer les bactéries au début — ligne C08#13 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `05/quiz#1`, `05/quiz#2`, `05/quiz#3`, `05/01-pratique#2`, `05/01-pratique#4`, `05/01-pratique#5`, `05/02-boss#1`, `05/02-boss#2`, `05/02-boss#3`, `05/02-boss#6`, `05/05-entrainement#2`, `05/05-entrainement#3`
- Note : Le sens des flèches est le piège de la mission (sept lignes, six sessions) : le manuel et le patron écrivent la flèche du mangeur vers sa nourriture (« يتغذّى على »). Le maillon absent (producteur en 2026, texte en 2025) est donné dans les options. La figure de 2023 se lit de droite à gauche : l'auteur la refait lisible. Les noms d'animaux du sujet 2026 (فنك, يربوع) sont des animaux du désert tunisien.

### m030 → `exercices/07-exams-2013-2024-producteurs-consommateurs-decomposeurs-et-milieu.json` · d2 practice 75/15 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2013–2024 ⭐⭐: … ») : Concours 2013 · 2019 · 2021 · 2022 · 2023 · 2024 · producteurs, consommateurs, décomposeurs et milieu
- Registre : id `C05#9` ; sources `C05#9, C08#14, C08#15, C14#1b, C04#13, C06#13, C06#7, C08#16, C03#13`
- Sources : C05 (session 2022), situation intégrative, support 1, consigne 1-2 ; C08 (session 2019), situation intégrative, support 3, consignes 2-ب, 2-ج et 3 ; C14 (session 2013), support 1, consigne 2 ; C04 (session 2023), situation intégrative, support 1, consigne 1-ب ; C06 (session 2021), situation intégrative, support 1 (1 أ) et support 2 (consigne 2) ; C03 (session 2024), situation intégrative, support 3, consigne 3-1-ب — transcriptions `2024-unique.md`, `2023-unique.md`, `2022-unique.md`, `2021-unique.md`, `2019-unique.md`, `2013-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2022 · أبيّن أنّ طائر النّحام كائن مستهلك من الدّرجة الثّالثة. (محار، عوالق حيوانيّة، طائر النّحام)
  - 2019 · أسمّي الحلقة الّتي يمثّلها الصّنوبر الحلبيّ في هذه السّلسلة الغذائيّة. / أفسّر علاقة البكتيريا بالحلقات المكوّنة لهذه السّلسلة الغذائيّة. / أصلح كلّ خطإ ورد في الإفادة التّالية : الوسط البيئيّ هو مجموعة الكائنات الحيّة المستقلّة عن بعضها البعض.
  - 2013 · أكمل الإفادات التالية بما يناسب : يعتبر النحل مستهلكا من الدّرجة [........] لأنّ ........
  - 2023 · أصلح الخطأ الوارد في قول شادٍ. (« تُعْرَفُ الكائنات الحيّة التي تصنع المادّة العضويّة عند توفّر ضوء الشّمس بالكائنات المستهلكة من الدّرجة الثّانية »)
  - 2021 · أضع العلامة (x) أمام الإفادة السّليمة. (تُعْرَفُ الكائنات الّتي تقوم بتحليل بقايا الكائنات الحيّة وتحويلها إلى أملاح معدنيّة بالكائنات المفكّكة.) / أربط عناصر الوسط البيئيّ التّالية بالمجموعة الّتي تنتمي إليها : ماء · بكتيريا · عوالق نباتيّة ↔ عناصر حيّة · عناصر غير حيّة
  - 2024 · فسّر دور الكائنات الدّقيقة في الوسط البيئي.
- Étapes prévues :
  - 2022 : le flamant est consommateur de 3ᵉ ordre dans la chaîne phytoplancton, zooplancton, huître, flamant, lue du producteur au dernier consommateur (le producteur est donné dans l'énoncé) — ordering, QCM de la justification (le compte à partir du producteur) — 2 q
  - 2019 (2-ب, 2-ج) : le pin d'Alep est le producteur ; les bactéries se nourrissent des restes de tous les maillons — deux QCM — 2 q
  - 2013 : l'abeille est consommateur de 1ᵉʳ ordre (elle se nourrit de nectar, de plantes) — QCM du rang, QCM de la raison — 2 q
  - 2023 : le producteur fabrique la matière organique à la lumière (le producteur n'est pas un consommateur de 2ᵉ ordre) — QCM de l'erreur, QCM de la phrase corrigée — 2 q
  - 2021 : les décomposeurs transforment les restes en sels minéraux ; classer eau, bactéries et plancton végétal en vivant/non vivant — QCM, matching — 2 q
  - 2019 (3) : le milieu est l'ensemble des êtres vivants ET des éléments non vivants, liés les uns aux autres — QCM — 1 q
  - 2024 : le rôle des êtres microscopiques (décomposer les restes, rendre les sels minéraux) — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - compter à partir du mauvais maillon — ligne C05#9 (d2)
  - répondre consommateur — ligne C08#14 (d1)
  - les croire absentes de la chaîne — ligne C08#15 (d2)
  - confondre consommateur de premier et de deuxième degré — ligne C14#1b (d2)
  - parler de consommateurs de second ordre — ligne C04#13 (d1)
  - attribuer aux décomposeurs la fabrication de matière organique — ligne C06#13 (d2)
  - classer les bactéries parmi les éléments non vivants — ligne C06#7 (d1)
  - oublier les éléments non vivants — ligne C08#16 (d1)
  - limiter leur rôle aux maladies — ligne C03#13 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `05/quiz#1`, `05/quiz#3`, `05/quiz#4`, `05/01-pratique#1`, `05/01-pratique#2`, `05/01-pratique#5`, `05/01-pratique#6`, `05/02-boss#3`, `05/02-boss#5`, `05/02-boss#6`, `05/05-entrainement#1`, `05/05-entrainement#2`, `05/05-entrainement#3`, `05/05-entrainement#5`
- Note : Le patron est riche sur ces notions : la mission apporte la forme (consigne sous deux angles : justifier un rang, corriger une définition du sujet). Le sujet 2022 ne montre que trois images pour établir un rang 3 ; le producteur est donné dans l'énoncé de la mission. Le rôle du décomposeur d'après le sujet 2021 s'écrit « المفكّكة » (manuel). Ce lot recoupe l'item `HP:nutrition-vegetale` (C02#10), non repris ici : voir E-7.

### m031 → `exercices/08-exams-2009-2026-eau-polluee-et-maladies-hydriques.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2009–2026 ⭐⭐⭐: … ») : Concours 2009 · 2019 · 2021 · 2022 · 2023 · 2024 · 2026 · l'eau polluée et les maladies hydriques
- Registre : id `C05#8` ; sources `C05#8, C03#14, C03#15, C01#7, C04#14, C08#12, C06#8, C18#2a`
- Sources : C05 (session 2022), situation intégrative, support 1, consigne 1-1 ; C03 (session 2024), situation intégrative, support 3, consignes 3-2 et 3-3 ; C01 (session 2026), situation 2, consigne 2 ; C04 (session 2023), situation intégrative, support 2 ; C08 (session 2019), situation intégrative, support 3, consigne 1 ; C06 (session 2021), situation intégrative, support 1, consigne 1 ب ; C18 (session 2009), support 2, consigne 1 — transcriptions `2026-unique.md`, `2024-unique.md`, `2023-unique.md`, `2022-unique.md`, `2021-unique.md`, `2019-unique.md`, `2009-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2022 · أصنّف الملوّثات التّالية في الجدول المبيّن أسفله. (فضلات مستشفى – فضلات مداجن – زيوت مراكب الصّيد – طماطم فاسدة ; فضلات بحريّة المنشأ / فضلات برّيّة المنشأ)
  - 2024 · أذكر ثلاثة ملوّثات للأوساط المائيّة.
  - 2024 · أصلحْ كلَّ خطإ ورد في الإفادتين التّاليتين. يمكن شرب مياه الأمطار بعد اتّباع المراحل التّالية مرتّبة : التّعقيم - التّرشيح – التّرسيب. · من الأعراض المشتركة بين الحمّى التّيفيّة ومرض البوصفير اصفرار العينين وآلام في الأمعاء.
  - 2026 · إذا كانت التّحاليل قد أثبتت أنّ الجرثومة الّتي عكّرت صحّة المريضة هي جرثومة الحمّى التيفيّة، أكتبُ نصّا تفسيريّا حول هذه الجرثومة مسترشدا بالمعطيات التالية : كيفيّةِ انتقالها إلى جسم المريض / وبعضِ أعراضها / وطرقِ الوقاية منها.
  - 2023 · أفسّر ظاهرة تفشّي مرض الحمّى التّيفيّة بالمنطقة التي يسكنها الفلّاح.
  - 2019 · أحدّد عرضين لمرض الحمّى التّيفيّة من بين الإفادات التّالية بوضع العلامة (x) في الخانة المناسبة : آلام حادّة في الظهر والأطراف · آلام شديدة في الأمعاء · صداع وحرارة مرتفعة في الجسم · فشل عضليّ
  - 2021 · أساعد ندى على إصلاح الأخطاء الواردة في الإفادتين التّاليتين قبل إدراجهما بالمجلّة : من بين الأمراض النّاتجة عن سوء التّغذية، الأمراض الثّلاثة التّالية : الحمّى التّيفيّة والكساح والكوليرا. · لمرض البوصفير النّاتج عن شرب المياه الملوّثة ثلاثة أعراض وهي اصفرار البشرة والعينين والصّداع وآلام في الأمعاء.
  - 2009 · أكتب في الخانات الفارغة أسماء الأمراض التّالية استنادا إلى أعراضها : الكوليرا، البوصفير، الحمّى التيفيّة.
- Étapes prévues :
  - 2022 : quatre polluants à ranger entre origine marine et origine terrestre (les déchets d'hôpital : terrestre ; l'huile des bateaux de pêche : marine) — matching — 1 q
  - 2024 (3-2) : trois polluants des milieux aquatiques (pas des polluants de l'air) — multi — 1 q
  - 2024 (3-3) : la potabilisation est donnée en ordre juste (décanter, filtrer, désinfecter) dans l'énoncé ; la question est de LIRE le schéma (V4 : aucune question n'exige de connaître les étapes). Les symptômes COMMUNS à la typhoïde et à la jaunisse ne sont pas la jaunisse elle-même (« اصفرار العينين » est propre à la jaunisse) : corriger l'énoncé, la clé étant à établir d'après les symptômes du manuel (fièvre, maux de tête) — QCM de lecture, QCM de l'erreur, QCM de la correction — 3 q
  - 2026 : le texte explicatif sur la typhoïde est converti : choisir les trois éléments (transmission par l'eau et les aliments souillés ; fièvre, maux de tête, douleurs intestinales ; hygiène, eau contrôlée, lavage des légumes) — multi, QCM de l'élément oublié (la prévention) — 2 q
  - 2023 : la typhoïde se propage par l'eau souillée par des matières fécales et par les légumes irrigués avec elle — QCM — 1 q
  - 2019 : deux symptômes de la typhoïde parmi quatre — multi — 1 q
  - 2021 : le rachitisme (الكساح) est une maladie de malnutrition, la typhoïde et le choléra sont hydriques ; les symptômes de la jaunisse — deux QCM d'erreur, deux QCM de correction — 2 q
  - 2009 : nommer trois maladies d'après leurs symptômes (choléra, jaunisse, typhoïde) — matching — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - ranger les déchets d'hôpital dans la mauvaise origine — ligne C05#8 (d2)
  - citer des polluants de l'air — ligne C03#14 (d1)
  - placer la stérilisation avant le filtrage — ligne C03#15 (d2)
  - oublier un des trois axes demandés / écrire une liste sans explication — ligne C01#7 (d3)
  - oublier l'eau souillée comme vecteur — ligne C04#14 (d2)
  - retenir un signe d'une autre maladie — ligne C08#12 (d1)
  - ranger une maladie hydrique parmi celles de la malnutrition — ligne C06#8 (d2)
  - confondre les symptômes de maladies voisines — ligne C18#2a (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `05/quiz#5`, `05/03-revision#1`, `05/03-revision#2`, `05/03-revision#3`, `05/03-revision#4`, `05/03-revision#5`, `05/03-revision#6`, `05/04-defi#1`, `05/04-defi#2`, `05/04-defi#3`, `05/04-defi#4`, `05/04-defi#5`, `05/04-defi#6`, `05/05-entrainement#4`, `05/05-entrainement#6`
- Note : Le chapitre `05` est le plus lourd en pollution/maladies : 8 lignes de 7 sessions fusionnées. Étage d2 (aucune ligne d3). Le nom du mal de 2021 « الهزال الرزّي » n'est PAS dans cette mission. Le sujet 2024 propose l'ordre de potabilisation : il est DONNÉ juste dans l'énoncé (V4, E-5). L'item `HP:pesticides` (C02#11) n'est pas repris (E-8). La quiz 05 #5 dit que la jaunisse vient d'un « فيروس » : cohérent avec le sujet (البوصفير).

### m032 → `exercices/09-devoir-chaines-avec-lhomme-et-protection-du-milieu.json` · d2 practice 75/15 · 7 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐: … ») : Des chaînes qui comptent l'homme et la protection de l'eau et du sol
- Registre : id `D07#1` ; sources `D07#1, D07#2, D07#3`
- Cartes : devoir G (T3, école primaire), exercices 1, 2, 3 (la copie de G incluse dans un lot de matières n'est pas comptée) — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D07#1 (d2) : construire trois chaînes alimentaires avec l'humain à un rang demandé
  - D07#2 (d1) : corriger les symptômes attribués à une maladie hydrique
  - D07#3 (d1) : corriger une mesure de protection de l'eau et du sol
- Étapes prévues :
  - Construire trois chaînes alimentaires avec l'homme à un rang demandé (consommateur de 1ᵉʳ, 2ᵉ, 3ᵉ ordre) : ne pas placer l'homme avant le producteur — ordering, ordering, QCM de contrôle — 3 q
  - Corriger les signes attribués à une maladie hydrique (choisir les signes de la maladie visée) — QCM, QCM — 2 q
  - Corriger une mesure de protection de l'eau et du sol (rejeter les déchets dans le sol est une pratique polluante) — QCM, QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - placer l'humain avant le producteur — ligne D07#1 (d2)
  - attribuer les signes d'une autre maladie — ligne D07#2 (d1)
  - proposer une pratique polluante — ligne D07#3 (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `05/quiz#3`, `05/01-pratique#5`, `05/02-boss#6`, `05/03-revision#1`, `05/05-entrainement#4`, `05/05-entrainement#6`, `05/04-defi#1`
- Note : Salle blanche. Source unique (devoir G, T3) ; D09 contient D07 à l'identique (copie dans un lot de cinq matières) et n'est pas comptée (E-10). L'homme n'est pas un chaînon central du patron : la mission lui donne un rang demandé. Devoir classé « programme ancien » (2008) par le lecteur : ses trois lignes sont dans le programme.
