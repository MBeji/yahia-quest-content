# Carte d’affectation M4 — éveil scientifique 6ᵉ, chapitres `07`, `11`, `08` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 9 missions (8 d’examen, 1 de devoir), 86 questions ; 2 auteurs : `07` d’un côté, `11` + `08` de l’autre. Skills : `content-ecole-tn`, puis `prof-eveil-primaire` (calibre les étages, jamais plus que le programme de 6ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/eveil/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend un support (ou une situation) et ses consignes, découpés en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne la phrase OFFICIELLE de la transcription qu'elle lit (consigne et énoncé tels qu'imprimés, coquilles incluses sauf celles que la carte nomme) ; une consigne ouverte (« أفسّر », « أعلّل », « أصلح كلّ خطأ », « أقترح تجربة ») devient un QCM de l'explication ou de la correction, un `ordering` (étapes d'un protocole, trajet), un `matching` (légende ↔ nom, tableau) ou un `multi` (relevés, vrai/faux motivés) ; `short_answer` seulement pour UN terme du معجم avec ses `acceptedAnswers` ; aucun tracé n'est demandé à la main : un tracé de rayon, de flèche ou d'aiguille devient « quel dessin est exact ? » (QCM visuel) ; figures, schémas d'expériences et tableaux refaits en SVG, vrais, SANS donner la clé ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Chiffres du ملفّ du guide (78 %, 21 %, 2 : 1, 55 %, 1/6, 5 millions…) : enrichissement seulement, JAMAIS une clé ni un distracteur (V1) ; les quatre valeurs permises sont 1/5 d'oxygène, 1 L d'air ≈ 1,3 g, eau = 2/3 du corps, 120 jours (fiche §4 bis, point 4). Sont enseignés, donc exerçables : les plaquettes (V2 révisé), les huit directions (V5) ; l'« intensité » du courant n'est pas exigible (V3) ; la potabilisation est une lecture de schéma sans clé de mémorisation (V4). Chaque DÉFAUT d'énoncé que la carte nomme est corrigé dans la reprise, comme la carte le dit, et l'explication le signale. Étiquettes : `misconceptionTag` du registre `eveil.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/eveil/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-eveil/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject eveil-scientifique-6eme` (0 erreur), `content:tranche -- --subject eveil-scientifique-6eme --changed --fresh --strict-longest`.

**🔁 À REVÉRIFIER AU LANCEMENT (E-12).** Les 12 chapitres d'éveil seront mis à niveau sur la fiche programme APRÈS ce plan (cours au patron, exercices, étiquettes). Tous les « Ne pas redemander » de cette carte sont établis sur les exercices TELS QU'ILS SONT AU 2026-10-20 (état du 28 septembre : 5 fichiers de 6 questions à choix + un quiz de 5 questions par chapitre, tous des QCM) : ils sont PROVISOIRES. Au lancement de chaque mission, relis les exercices et le cours du chapitre tel qu'il sera alors, refais le croisement question par question, et mets la liste à jour avant d'écrire. Les numéros de fichiers (`06`, `07`, …) supposent que les chapitres ont `01`–`05` : si la mise à niveau ajoute un fichier, décale. Si un item que la carte cible (plaquettes, huit directions, sang décanté, sonnerie, monoxyde de carbone…) n'est pas enseigné par le chapitre mis à niveau, arrête-toi et signale-le : la mission ne part pas avant le cours.

**Ordre de travail** : (1) les ids d’étiquette neufs que tu poses ; (2) les missions du chapitre, dans l’ordre de la carte ; (3) les gates. **Départ du lot** : seulement quand ses chapitres ont été mis à niveau sur la fiche (E-11).


## Chapitre `07-aimants-boussole` — المغانط والبوصلة

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.aim.attire-tous-les-metaux` (Tu crois que l'aimant attire tous les métaux : il n'attire q) | `eveil.aim.attraction-forte-au-milieu` (Tu crois que l'attraction est forte au milieu de l'aimant ou) | `eveil.aim.poles-identiques-s-attirent` (Tu inverses la règle des pôles : deux pôles de même nom se r) | `eveil.aim.juge-par-forme-couleur-legerete` (Tu juges un aimant, ou ce qu'il attire, à la forme, à la cou) | `eveil.aim.aiguille-tourne-avec-la-boussole` (Tu crois que l'aiguille de la boussole tourne avec le boîtie) | `eveil.aim.attire-seulement-au-contact` (Tu crois que l'aimant n'agit qu'au contact ou qu'une feuille)

### m033 → `exercices/06-exams-2017-2026-poles-force-attraction-et-repulsion.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2017–2026 ⭐⭐: … ») : Concours 2017 · 2019 · 2024 · 2026 · les pôles, la force d'un aimant, l'attraction et la répulsion
- Registre : id `C01#3` ; sources `C01#3, C01#4, C03#5, C03#6, C08#5, C08#6, C10#4b`
- Sources : C01 (session 2026), situation 1, activité 2 ; C03 (session 2024), situation 2, expérience 1 ; C08 (session 2019), situation 2, support 2, consignes 1-أ et 1-ب ; C10 (session 2017), support 4, consigne 2 — transcriptions `2026-unique.md`, `2024-unique.md`, `2019-unique.md`, `2017-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · أصلحُ خطأ التلميذ على الصّورة 3 مستعملا العلامة (x). (un aimant coupé en deux ; les « x » marquent les pôles)
  - 2026 · أصلحُ الخطأ الوارد بالإفادة التّالية. تتجمّع برادة الحديد بوفرة عند وسط المغنط لأنّ قوّة الجذب تقلّ كلّما اقتربنا من طرفيه.
  - 2024 · أكمل تعمير الجدول بـ "تنافر" أو "تجاذب" معلّلا إجابتك. (مغنط 1 : أ، ب ; مغنط 2 : ك، ن ; ب و ن يتنافران) / أصلح كلّ خطإ ورد في الإفادة التالية : تزداد قوّة جذب المغنط في وسطه و تضعف في أحد طرفيه.
  - 2019 · أتأمّل الرسم التالي وأضع في إطار رقم الإبرة التي تمّ رسمها بشكل خاطئ. / أعلّل إجابتي.
  - 2017 · أعيد كتابة الإفادة وأصلح الخطأ إن وجد. يشتدّ التأثير المغناطيسيّ للمغنط في وسطه.
- Étapes prévues :
  - 2026 (3-أ) : l'aimant coupé en deux : chaque morceau a ses deux pôles, pas un seul — QCM visuel (où mettre les marques) — 1 q
  - « La force est maximale au milieu » (2026 3-ب, 2024 consigne 2, 2017) : la même erreur sous trois habits, une question par habit — la limaille se rassemble aux extrémités et non au milieu ; la force est la plus grande aux deux extrémités (pas « faible à l'une d'elles ») ; le magnétisme est le plus fort aux extrémités — trois QCM de formulations différentes — 3 q
  - 2024 (consigne 1) : un tableau à deux cases à remplir (attraction ou répulsion) avec la raison (des pôles de même nom se repoussent, des pôles de noms contraires s'attirent) — deux QCM + QCM de la raison — 3 q
  - 2019 (1-أ, 1-ب) : trois aiguilles aimantées près d'un barreau ; l'une est mal dessinée ; la justifier par les pôles qui s'attirent — QCM visuel, QCM de la justification — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - croire qu'un morceau n'a qu'un seul pôle — ligne C01#3 (d2)
  - situer la force maximale au milieu — ligne C01#4 (d1)
  - oublier que deux pôles de même nom se repoussent — ligne C03#5 (d2)
  - situer la force maximale au milieu — ligne C03#6 (d1)
  - oublier que les pôles contraires s'attirent — ligne C08#5 (d2)
  - parler de la couleur plutôt que des pôles — ligne C08#6 (d2)
  - placer la force maximale au milieu du barreau — ligne C10#4b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `07/quiz#2`, `07/quiz#3`, `07/01-pratique#4`, `07/01-pratique#5`, `07/02-boss#2`, `07/02-boss#3`, `07/02-boss#4`, `07/03-revision#4`, `07/04-defi#2`, `07/04-defi#3`, `07/04-defi#4`, `07/05-entrainement#6`
- Note : Le geste « force maximale au milieu » revient dans cinq lignes (2026, 2024, 2019, 2017, plus l'écran de 2025) : la mission n'en garde que trois habits et laisse C08#7 de côté. Les pôles du sujet 2024 sont des lettres (أ ب ك ن) : les garder ; ne pas introduire « ش/ج » dans la même figure. Le patron a déjà « les pôles de même nom se repoussent » (07/quiz#3) : la nouveauté est le tableau et la justification.

### m034 → `exercices/07-exams-2009-2025-types-de-poles-aiguille-formes-et-matieres.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2009–2025 ⭐⭐⭐: … ») : Concours 2009 · 2021 · 2022 · 2023 · 2025 · nommer les pôles, l'aiguille, les formes, les matières
- Registre : id `C06#14` ; sources `C06#14, C18#3b, C04#10, C04#11, C02#13, C05#6, C05#7, C02#14`
- Sources : C06 (session 2021), situation intégrative, support 2, consigne 3 ; C18 (session 2009), support 3, consigne 2 ; C04 (session 2023), situation 2, support 3 ; C02 (session 2025), situation intégrative, support 4 ; C05 (session 2022), situation 2, support 2 — transcriptions `2025-unique.md`, `2023-unique.md`, `2022-unique.md`, `2021-unique.md`, `2009-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2021 · أحدّد نوع كلّ قطب من المغانط بملء الفراغات معتمدا المعطيات المصاحبة للرّسم التّالي : القطب الشّماليّ للمغنط الأوّل والقطب (م) للمغنط الثّالث يتنافران. · القطبان (ل) و(م) يتجاذبان. · القطبان (ل) و(ن) يتنافران.
  - 2009 · أتمّم بما يناسب في كلّ وضعيّة : الوضعيّة (1) : يتنافر المغنطان لأنّ ........ · الوضعيّة (2) : يتجاذب المغنطان لأنّ ........ · الوضعيّة (3) : ........ المغنطان لأنّ قطبيهما المتقابلين متماثلان.
  - 2023 · (« تتكوّن البوصلة من علبة بها إبرة لها قطب واحد يشير إلى الشّمال ») أصلح كلّ خطإ ورد في قول شذى. / أعلّل إجابتي.
  - 2025 · كمّل بذكر شكل المغنط أو رسمه. (قضيب · نضويّ · ...)
  - 2022 · أصلح الخطأ الوارد بإجابة التّلميذ على الرّسم 3. · أعلّل إجابتي. (aimant en U ; mélange de clous de fer et de cuivre)
  - 2025 · أصلح الخطأ في الإفادة التّالية. تزداد قوّة جذب المغنط لجسم حديديّ كلّما ازداد سمك الحاجز الفاصل بينهما أو صغرت المسافة التي تفصلهما.
- Étapes prévues :
  - 2021 (3) : quatre barreaux, lettres aux extrémités (ش، ن، م، ل) ; déduire le nom de trois pôles à partir de répulsions et d'attractions — trois QCM (le premier pôle est donné : شمالي) — 3 q
  - 2009 (3-2) : la cause d'une attraction ou d'une répulsion (pôles de noms contraires ou de même nom) pour trois dispositions — un QCM de la cause de la répulsion et de l'attraction (deux dispositions), un QCM du mot manquant de la troisième (« يتنافر ») — 2 q
  - 2023 (3-أ, 3-ب) : l'aiguille de la boussole a deux pôles, c'est son pôle nord qui se tourne vers le nord ; le justifier — QCM de l'erreur, QCM de la phrase corrigée, QCM de la justification — 3 q
  - 2025 (4-1) : nommer ou reconnaître trois formes d'aimants (barreau, U/نضويّ, cylindre ou anneau au choix de l'auteur dans les formes du manuel) — QCM visuel — 1 q
  - 2022 (2-1, 2-2) : un aimant en U près d'un mélange de clous de fer et de cuivre : seuls les clous de fer sont attirés ; le justifier par la nature du métal — QCM visuel, QCM — 2 q
  - 2025 (4-2) : la force d'attraction diminue quand la distance ou l'épaisseur d'un écran augmente — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre pôles de même nom et pôles contraires — ligne C06#14 (d3)
  - confondre pôles identiques et pôles opposés — ligne C18#3b (d2)
  - dire que l'aiguille n'a qu'un pôle — ligne C04#10 (d1)
  - oublier que tout aimant a deux pôles — ligne C04#11 (d2)
  - ne pas connaître la forme en U — ligne C02#13 (d1)
  - croire que l'aimant attire tous les métaux — ligne C05#6 (d2)
  - oublier que seuls les objets ferreux sont attirés — ligne C05#7 (d2)
  - faire croire que l'écran épais renforce la force — ligne C02#14 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `07/quiz#1`, `07/quiz#3`, `07/quiz#4`, `07/01-pratique#1`, `07/01-pratique#2`, `07/01-pratique#3`, `07/02-boss#1`, `07/02-boss#5`, `07/02-boss#6`, `07/03-revision#1`, `07/03-revision#2`, `07/03-revision#4`, `07/03-revision#5`, `07/04-defi#1`, `07/04-defi#3`, `07/04-defi#4`, `07/05-entrainement#1`, `07/05-entrainement#3`, `07/05-entrainement#4`
- Note : Huit lignes, douze questions : la mission est la synthèse « qu'est-ce qu'un aimant ». L'aimant « en anneau » (haut-parleur, 2025) n'est pas dans la liste du manuel (قضيب، نضويّ، اسطوانيّ، إبرة) : l'auteur dessine un cylindre. Le patron a déjà « les clous de fer et de cuivre » (07/02-boss#1) : le geste neuf est l'aimant en U et le dessin du mélange (figure). Les pôles du sujet 2021 sont des lettres (ش ن م ل) : les garder.

### m035 → `exercices/08-exams-2019-2026-directions-le-nord-nest-pas-en-haut.json` · d3 boss 120/30 · 11 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2019–2026 ⭐⭐⭐: … ») : Concours 2019 · 2022 · 2024 · 2026 · les directions : le nord n'est pas en haut de la page
- Registre : id `C01#13` ; sources `C01#13, C01#14, C03#10, C03#11, C05#10, C08#4`
- Sources : C01 (session 2026), situation intégrative, support 3, consignes 3-1-أ et 3-1-ب ; C03 (session 2024), situation intégrative, support 2 ; C05 (session 2022), situation intégrative, support 2, consigne 2-1 ; C08 (session 2019), situation 2, support 1 — transcriptions `2026-unique.md`, `2024-unique.md`, `2022-unique.md`, `2019-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · إذا كان منير قد انطلق من النّصب التّذكاري ووصل إلى الفندق، حدّد الاتّجاهات المشار إليها بالأسهم. (boussole : « ش » à droite, « ج » à gauche)
  - 2026 · عندما غادر منير وأبوه وجدّه الفندق، اتّجهوا شمالا، أرسم سهما يبيّن اتّجاههم انطلاقا من العلامة (x).
  - 2024 · أصلح الخطأ الوارد في رسم البوصلة 1 على البوصلة 2. / أكمل الفراغ بما يناسب. (يقع مستودع الحماية المدنيّة ......... المنطقة الغابيّة. · ... مركز الحماية المدنيّة. · تقع المنطقة الغابيّة ......... مركز الحماية المدنيّة) (l'école est au sud du centre)
  - 2022 · أتأمّل الرّسم وأحدّد الاتّجاه النّاقص مكان الفراغ. (rose à huit flèches ; « شمال » à gauche, « جنوب » à droite)
  - 2019 · أكمل الفراغ بتحديد الموقع أو الاتّجاه مستعينا بالرّسم التّالي. (تقع الغابة ......... فريق الكشّافة. · يقع ......... في الجنوب الغربيّ لفريق الكشّافة. · يقع المخيّم في ......... لفريق الكشّافة. ; « ش » à gauche de la boussole)
- Étapes prévues :
  - 2026 (3-1-أ) : trois segments fléchés ; dire leur direction avec une boussole dont le nord est à droite de la page — trois QCM (figure refaite ; le nord est marqué par la lettre ش) — 3 q
  - 2026 (3-1-ب) : tracer la flèche vers le nord depuis le repère × — QCM visuel — 1 q
  - 2024 (2-1) : redessiner la boussole sachant que l'école est au sud du centre (le sud est à droite, donc le nord à gauche) — QCM visuel ; (2-2) trois phrases de position — deux QCM — 3 q
  - 2022 (2-1) : compléter la rose à huit flèches dont le nord est à gauche (trois directions manquantes) — matching ou ordering — 2 q
  - 2019 (1) : trois positions d'après une boussole dont le nord est à gauche (la forêt, le sud-ouest, le camp) — deux QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - lire le haut de la feuille comme le nord — ligne C01#13 (d3)
  - tracer vers le haut au lieu de suivre la boussole — ligne C01#14 (d1)
  - dessiner le nord vers le haut de la page — ligne C03#10 (d3)
  - orienter le plan avec le nord en haut — ligne C03#11 (d3)
  - placer le nord en haut — ligne C05#10 (d3)
  - orienter le plan avec le nord en haut — ligne C08#4 (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `07/quiz#4`, `07/quiz#5`, `07/01-pratique#4`, `07/02-boss#6`, `07/03-revision#3`, `07/04-defi#5`, `07/05-entrainement#2`, `07/05-entrainement#5`
- Note : V5 (arbitrage du propriétaire) : les huit directions (nord-est, sud-ouest…) sont ENSEIGNÉES au `07` ; le patron n'en a que quatre (07/02-boss#6, 07/03-revision#3) : ces lignes sont donc neuves pour le chapitre, et le nouveau cours doit les porter avant la mission. La boussole du sujet n'a pas le nord en haut : les figures sont gardées telles (nord à droite en 2026, à gauche en 2022 et 2019), SIGNALÉES par la lettre ش ; jamais « le haut = le nord ».

### m036 → `exercices/09-exams-2010-2026-boussole-en-voiture-et-boussole-artisanale.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2010–2026 ⭐⭐⭐: … ») : Concours 2010 · 2021 · 2022 · 2025 · 2026 · la boussole en voiture, la boussole faite maison
- Registre : id `C06#4` ; sources `C06#4, C06#5, C06#6, C17#1a, C05#11, C01#15, C02#15`
- Sources : C06 (session 2021), situation 2, consignes 1 à 3 ; C17 (session 2010), support 1 ; C05 (session 2022), situation intégrative, support 2, consigne 2-2 ; C01 (session 2026), situation intégrative, support 3, consigne 3-2 ; C02 (session 2025), situation intégrative, support 5 — transcriptions `2026-unique.md`, `2025-unique.md`, `2022-unique.md`, `2021-unique.md`, `2010-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2021 · أتأمّل الرّسم وأعمّر الفراغات بتحديد الاتّجاهات الّتي سلكتها العائلة انطلاقا من المنزل وصولا إلى مدينة الألعاب. (boussole : « الشّمال » écrit sous le cercle)
  - 2021 · أصلح الخطأ الوارد في كلّ من الإفادتين التّاليتين. بالاستناد إلى الرّسم السّابق، يقع المتحف شمال المنزل. · ازدادت صعوبة الرّؤية بوجود قطرات من الماء على الجدار الدّاخلي لبلّور السّيّارة النّاتج عن تكثّف غاز ثاني أكسيد الكربون.
  - 2021 · أفسّر سبب اختلاف ريّان مع والده في تحديد الاتّجاهات داخل السّيّارة رغم اعتماده على البوصلة.
  - 2010 · أتأمّل الرّسم وأكتب في الخانات الفارغة الاتّجاهات التي سار وفقها فريق الكشافة من نقطة الانطلاق إلى النّقطة "أ" ومنها إلى النقطة "ب" ثمّ الرجوع إلى نقطة الانطلاق عبر الغابة.
  - 2022 · أصلح كلّ خطأ ورد في الإفادة التّالية. ترتكز إبرة البوصلة على ميناء مدرّج حتّى تكون حرّة الدّوران، وتستقرّ حسب المنحى الشّماليّ-الشّرقيّ إذا كانت بعيدة عن أيّ مغنط أو جسم حديديّ.
  - 2026 · بيّن الطّريقة السّليمة لاستخدام البوصلة في تحديد الاتّجاه الصّحيح.
  - 2025 · أشطبُ العبارة الخاطئة في كلّ إفادة ثمّ علّل. (الإبرة في الحالة ① (تحدّد / لا تحدّد) الاتّجاه السّليم. لأنّ ........ ; ① ممغنطة على « حديد » ; ② غير ممغنطة على « خشب » ; ③ ممغنطة على « خشب »)
- Étapes prévues :
  - 2021 (1) : trois segments de la route, boussole dont le nord est en bas ; direction de chaque segment — trois QCM — 3 q
  - 2021 (2) : le musée n'est pas au nord de la maison (sa vraie position se lit sur la boussole du dessin, nord en bas : l'auteur la fixe sur la figure refaite) ; la buée vient de la vapeur d'eau (non du dioxyde de carbone) — QCM, QCM — 2 q
  - 2021 (3) : dans la voiture la boussole est faussée par les pièces de fer — QCM — 1 q
  - 2010 (1) : un itinéraire à quatre segments avec des diagonales sur un schéma à axes N-S et E-O : dire les directions — deux QCM ; V5 : la rose à huit directions est enseignée — 2 q
  - 2022 (2-2) : l'aiguille s'oriente nord-sud (pas nord-est) quand rien de ferreux n'est près ; elle repose sur un pivot et un cadran — QCM de l'erreur, QCM de la correction — 1 q
  - 2026 (3-2) : utiliser une boussole : la poser à plat, loin du fer et des aimants, attendre que l'aiguille se stabilise, lire — ordering — 1 q
  - 2025 (5) : trois aiguilles ; seule l'aiguille aimantée sur un support non magnétique indique la bonne direction ; justification de chaque cas — QCM par cas (deux QCM : ①, ②) — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - lire le haut de la feuille comme le nord — ligne C06#4 (d3)
  - confondre vapeur d'eau et dioxyde de carbone / nord en haut — ligne C06#5 (d2)
  - oublier l'effet des pièces ferreuses sur l'aiguille — ligne C06#6 (d3)
  - confondre est et ouest — ligne C17#1a (d2)
  - dire que l'aiguille s'oriente vers le nord-est — ligne C05#11 (d2)
  - omettre d'attendre la stabilisation de l'aiguille / éloigner les objets magnétiques oublié — ligne C01#15 (d2)
  - oublier que le support doit être non magnétique — ligne C02#15 (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `07/quiz#4`, `07/quiz#5`, `07/02-boss#4`, `07/02-boss#6`, `07/03-revision#3`, `07/03-revision#6`, `07/04-defi#3`, `07/04-defi#5`, `07/04-defi#6`, `07/05-entrainement#2`, `07/05-entrainement#5`, `07/05-entrainement#6`, `01/01-pratique#4`
- Note : Beaucoup d'items (douze questions pour sept lignes) : la mission est le cas d'usage de la boussole (voiture, support, méthode). 2021 (2) cumule une direction et la condensation (item `01+07` du registre) ; les deux erreurs sont corrigées dans la même mission. « Vers le nord-est » (2022) : le sujet l'emploie comme FAUX (l'aiguille va vers le nord) ; ne pas en faire une clé. Les deux sujets 2021 et 2010 contiennent des diagonales : V5.


## Chapitre `11-effets-courant-electrique` — آثار التيّار الكهربائيّ

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.elec.effets-du-courant-confondus` (Tu confonds les effets du courant : thermique (chaleur), chi) | `eveil.gaz.test-mal-associe` (Tu associes un gaz au mauvais test : l'eau de chaux se troub) | `eveil.elec.fermer-et-ouvrir-confondus` (Tu confonds fermer et ouvrir un circuit : circuit fermé, le ) | `eveil.elec.conducteurs-liquides-confondus` (Tu te trompes sur les liquides qui conduisent : l'eau pure e) | `eveil.elec.gaz-viennent-de-la-soude` (Tu crois que les gaz de l'électrolyse viennent de la soude :) | `eveil.elec.gaz-electrolyse-inverses` (Tu inverses les gaz de l'électrolyse : l'oxygène se dégage à) | `eveil.elec.electroaimant-permanent` (Tu crois que l'électroaimant reste un aimant quand on coupe ) | `eveil.aim.poles-identiques-s-attirent` (Tu inverses la règle des pôles : deux pôles de même nom se r) | `eveil.elec.lampe-ne-chauffe-pas` (Tu crois qu'une lampe donne de la lumière sans chauffer : so) | `eveil.elec.fil-de-cuivre-est-un-aimant` (Tu crois que le fil de cuivre est un aimant qui dévie l'aigu)

### m037 → `exercices/06-exams-2008-2018-quel-effet-du-courant.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2018 ⭐⭐: … ») : Concours 2008 · 2012 · 2013 · 2017 · 2018 · quel effet du courant électrique ?
- Registre : id `C10#4a` ; sources `C10#4a, C19#5a, C09#9, C14#4a, C15#4b`
- Sources : C10 (session 2017), support 4, consigne 1 ; C19 (session 2008), support 5 ; C09 (session 2018), support 3, consigne 4 ; C14 (session 2013), support 4, consigne 1 ; C15 (session 2012), support 4, consigne 2 — transcriptions `2018-unique.md`, `2017-unique.md`, `2013-unique.md`, `2012-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2017 · أسمّي نوع مفعول التيّار الكهربائي. رنين الهاتف : ......... · حلكبة الماء : ......... · كيّ الثّياب : .........
  - 2008 · أصلح الخطأ الوارد في الإفادة الآتية : اشتغال الجرس الكهربائي ناتج عن التّأثير الحراري للتّيّار الكهربائي. الإصلاح : اشتغال الجرس الكهربائي ناتج عن التّأثير ........
  - 2018 · حدّد نوع تأثير التّيّار الكهربائيّ المتسبّب في رنين الهاتف.
  - 2013 · أجيب بـ "نعم" أو "لا" : يُضيء المصباح عندما يكون في دارة كهربائيّة مفتوحة. · احمرار السليك في المصباح ينتج بمفعول التأثير المغناطيسيّ للتيّار الكهربائيّ. · يختلف التأثير الحراريّ للتيّار الكهربائيّ باختلاف مادّة السلك الناقل.
  - 2012 · أكتُبُ "صواب" أو "خطأ" في الخانة المناسبة : عند فتح الدّارة لا يتمغنط المسمار في الوشيعة. · عند غلق الدّارة وتقريب بُرادة الحديد من الوشيعة يَحْدُثُ تنافر. · يَنْتُجُ رنين الجرس عن التأثير الحراري للتيّار الكهربائي.
- Étapes prévues :
  - 2017 : trois appareils (sonnerie ou sonnette ; électrolyse de l'eau ; fer à repasser) — matching appareil ↔ effet (magnétique, chimique, thermique), QCM sur le plus piégeux (la sonnerie) — 2 q
  - 2008 et 2018 : le fonctionnement d'une sonnette électrique est un effet magnétique, non thermique — deux QCM, de formulations différentes (corriger l'énoncé ; nommer l'effet) — 2 q
  - 2013 (4-1) : trois énoncés oui/non : un circuit ouvert n'allume pas ; le filament rougit par l'effet thermique ; l'effet thermique dépend du fil — multi, QCM — 2 q
  - 2012 (4-2) : trois énoncés vrai/faux : un circuit ouvert ne magnétise pas le clou de la bobine ; la limaille est attirée (non repoussée) par la bobine ; la sonnerie vient de l'effet magnétique — multi, QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre effet thermique et effet magnétique — ligne C10#4a (d1)
  - citer l'effet thermique — ligne C19#5a (d2)
  - citer l'effet thermique — ligne C09#9 (d1)
  - confondre effet thermique et effet magnétique — ligne C14#4a (d1)
  - confondre effet magnétique et effet thermique — ligne C15#4b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `11/quiz#1`, `11/quiz#2`, `11/quiz#5`, `11/01-pratique#1`, `11/01-pratique#3`, `11/01-pratique#5`, `11/02-boss#1`, `11/02-boss#5`, `11/03-revision#1`, `11/03-revision#2`, `11/03-revision#5`, `11/05-entrainement#2`, `11/05-entrainement#3`, `11/05-entrainement#5`, `11/05-entrainement#6`
- Note : La sonnerie/le téléphone/la sonnette (4 sessions : 2008, 2012, 2017, 2018) est dans le ملفّ du guide (p.175) et dans le projet « جرس كهربائي » : le patron n'a que l'écouteur du téléphone (11/04-defi#5). À traiter comme enseigné (E-7). Étage d2 (aucune ligne d3). Le sujet 2017 écrit « حلكبة الماء » (mot du معجم, électrolyse) pour l'électrolyse de l'eau.

### m038 → `exercices/07-exams-2012-2016-depot-metallique-la-cuillere-et-la-plaque.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2012–2016 ⭐⭐⭐: … ») : Concours 2012 · 2015 · 2016 · le dépôt métallique : la cuillère, la plaque, le montage
- Registre : id `C11#5a` ; sources `C11#5a, C11#5b, C11#5c, C15#4a, C12#3b`
- Sources : C11 (session 2016), support 5 ; C15 (session 2012), support 4, consigne 1 ; C12 (session 2015), support 3, consigne 2 — transcriptions `2016-unique.md`, `2015-unique.md`, `2012-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2016 · ما هو نوع تأثير التيّار الكهربائي الذي يمكن استثماره من خلال هذه التجربة ؟ (dépôt d'argent) / عند تشغيل المولّد الكهربائي، لم يحصل أيّ تفاعل. أفسّر لماذا ؟ / أصلح الخطأ على الرّسم (ب) ليتحقّق التفاعل.
  - 2012 · أُكمِلُ الفراغات بما يناسب : طلاء الملعقة ناتج عن ........ أحدثه مرور ........ في الدارة. · تُمثّل الملعقة المسرى السّالب في المحلال لأنّها ........
  - 2015 · أصلح الخطأ، إن وُجد، في كلّ من الإفادة والرّسم الآتيين : للتيّار الكهربائيّ تأثير حراريّ يُستثمَر في طلاء الأواني المعدنيّة وحمايتها من الصدإ. (schéma avant/après la modification, « محلول السكّر » → à remplacer)
- Étapes prévues :
  - 2016 (5-1) : l'effet exploité par un dépôt métallique est l'effet chimique — QCM — 1 q
  - 2016 (5-2) : aucune réaction : la plaque et la cuillère ne sont pas reliées aux bons pôles (la pièce à recouvrir doit être au pôle négatif) — QCM de la cause ; 5-3 : choisir le montage corrigé — QCM visuel. DÉFAUT : le sujet emploie le nitrate d'argent ; la mission pose le sulfate de cuivre du manuel (même effet chimique, E-5) — 2 q
  - 2012 (4-1) : trois blancs : effet chimique ; courant ; la cuillère est au pôle négatif (cathode) parce que le métal se dépose sur le pôle négatif — trois QCM — 3 q
  - 2015 (3-2) : l'énoncé « effet thermique » est faux (effet chimique) ; le schéma avec une solution de sucre est faux (le sucre ne conduit pas ; il faut une solution de sel ou de soude) — QCM de l'énoncé, QCM de l'erreur du schéma, QCM du schéma corrigé. DÉFAUT du sujet : voir E-5 — 3 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre effet chimique et effet thermique — ligne C11#5a (d1)
  - ignorer le branchement des pôles du générateur — ligne C11#5b (d2)
  - garder le mauvais branchement du pôle — ligne C11#5c (d2)
  - confondre électrode reliée au pôle positif et au pôle négatif — ligne C15#4a (d2)
  - citer l'effet thermique pour un dépôt métallique — ligne C12#3b (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `11/quiz#3`, `11/quiz#4`, `11/01-pratique#4`, `11/01-pratique#6`, `11/02-boss#2`, `11/02-boss#3`, `11/02-boss#4`, `11/03-revision#4`, `11/03-revision#6`, `11/04-defi#3`, `11/05-entrainement#2`, `11/05-entrainement#4`
- Note : Le dépôt de cuivre (cuillère au pôle −, plaque de cuivre au +, كبريتات النّحاس) est la forme du manuel p.125. Le « ملفّ » (guide) ajoute le principe de la purification des métaux : ◐, non repris. Les figures des trois sujets (2016, 2012, 2015) sont refaites avec les légendes du manuel (محلال، مصعد، مهبط, قاطعة). Sucre = non conducteur : déjà au manuel (11/03-revision#4) ; le nouveau est la lecture d'un schéma d'électrolyse fautif.

### m039 → `exercices/08-exams-2009-2018-electrolyse-de-leau-gaz-et-electrodes.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2009–2018 ⭐⭐⭐: … ») : Concours 2009 · 2013 · 2018 · l'électrolyse de l'eau : les gaz, les électrodes, la preuve
- Registre : id `C14#5a` ; sources `C14#5a, C18#3a, C09#10`
- Sources : C14 (session 2013), support 5 ; C18 (session 2009), support 3, consigne 1 ; C09 (session 2018), support 3, consigne 5 — transcriptions `2018-unique.md`, `2013-unique.md`, `2009-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2013 · ألاحظ التجربة الموالية وأعيد كتابة الإفادات مع إصلاح الخطأ إن وُجد : الغاز المتجمّع في الأنبوب عدد ① هو غاز الأكسجين. · يرتبط المصعد بالقطب السالب للخليّة. (ماء البحر ; l'éprouvette ② contient plus de gaz que la ①)
  - 2009 · أتخيّر ممّا يلي ما أراه مناسبا لملء الفراغات المشار إليها بأسهم في الرّسم التّالي : نتروجين – ماء نقيّ – أكسجين – محلول الصّودا – ثنائي أكسيد الكربون – هيدروجين.
  - 2018 · أذكر ثلاثة مؤشّرات تبيّن أنّ الغاز الموجود بالأنبوب رقم 1 في التّجربة الموالية، هو غاز الهيدروجين. (محلول الصّودا ; بطّارية « − » et « + »)
- Étapes prévues :
  - 2013 : l'éprouvette ② contient plus de gaz que la ① : ② recueille l'hydrogène et ① l'oxygène (le premier énoncé est donc JUSTE : ne pas inventer d'erreur) ; l'anode (مصعد) est reliée au pôle POSITIF (le second énoncé est faux) — QCM de l'énoncé juste, QCM de l'énoncé faux, QCM visuel du tube de l'hydrogène — 3 q
  - 2009 : remplir trois blancs du schéma (le liquide : solution de soude ; les deux gaz : oxygène et hydrogène) avec les mots de la liste, les leurres étant azote, eau pure, dioxyde de carbone — deux QCM — 2 q
  - 2018 : trois indices que le gaz est de l'hydrogène (il est recueilli en plus grand volume ; au pôle négatif ; il détonne à l'allumette) — multi, QCM du leurre (le brin incandescent est l'oxygène) — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - associer le gaz au mauvais tube ou le pôle à la mauvaise électrode — ligne C14#5a (d3)
  - citer un gaz ou un liquide non conducteur — ligne C18#3a (d2)
  - oublier le volume double ou le test à la flamme — ligne C09#10 (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `11/quiz#3`, `11/quiz#4`, `11/01-pratique#4`, `11/01-pratique#6`, `11/02-boss#2`, `11/02-boss#3`, `11/02-boss#4`, `11/03-revision#4`, `11/04-defi#3`, `11/05-entrainement#4`
- Note : Trois lignes d3 (2013 et 2018) : la mission est la plus dure du chapitre. Le sujet 2013 emploie « ماء البحر » (nom du liquide hors de la fiche) : l'auteur écrit « محلول ملح الطعام » (manuel). Le rapport chiffré 2 : 1 est ◐ (E-8) : on compare seulement les volumes (« plus grand », « plus petit »). Électrolyse de l'eau : ✅ du manuel p.122–125 (le lecteur des devoirs la jetonne `HP:electrolyse` à tort ; voir E-7).

### m040 → `exercices/09-devoir-circuit-en-panne-et-electroaimants.json` · d3 boss 120/30 · 8 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐⭐: … ») : Un circuit en panne, des électroaimants à classer, les effets du courant
- Registre : id `D07#6` ; sources `D07#6, D07#8, D07#10, D08#5`
- Cartes : devoir G (T3, école primaire), exercices 6, 8, 10 ; devoir H (T3, école primaire), exercice 5 ; la copie de G incluse dans un lot de matières n'est pas comptée — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D07#6 (d2) : nommer l'effet du courant correspondant à quatre observations
  - D07#8 (d2) : classer quatre électroaimants par effet magnétique croissant
  - D07#10 (d3) : chercher les causes d'une lampe éteinte dans un circuit avec solution et interrupteur
  - D08#5 (d2) : chercher pourquoi une lampe ne s'allume pas dans un circuit dont le texte manque
- Étapes prévues :
  - Nommer l'effet du courant correspondant à quatre observations (chaleur, dépôt, aimantation, bulles de gaz) — matching — 1 q
  - Classer quatre électroaimants par effet magnétique croissant selon le nombre de spires (le nombre de piles reste égal) — ordering, QCM sur le leurre « la taille du clou » — 2 q
  - Une lampe éteinte dans un circuit qui comprend un interrupteur et une solution : chercher les causes (interrupteur ouvert, solution non conductrice, fil coupé) et ne pas incriminer un composant en bon état — trois QCM — 3 q
  - Un circuit dont le schéma manque : la méthode pour chercher pourquoi une lampe ne s'allume pas (circuit fermé ? générateur en état ? fil bien branché ? lampe) — deux QCM — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - confondre effet chimique et effet thermique — ligne D07#6 (d2)
  - ignorer le nombre de spires — ligne D07#8 (d2)
  - incriminer un composant en bon état — ligne D07#10 (d3)
  - incriminer la lampe elle-même — ligne D08#5 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `11/01-pratique#1`, `11/01-pratique#2`, `11/01-pratique#3`, `11/02-boss#1`, `11/02-boss#2`, `11/02-boss#6`, `11/03-revision#3`, `11/03-revision#4`, `11/03-revision#5`, `11/04-defi#1`, `11/04-defi#2`, `11/04-defi#6`, `11/05-entrainement#1`, `11/05-entrainement#6`
- Note : Salle blanche. Source : un seul devoir complet (G, juin, que le lecteur classe « programme ancien ») plus un devoir partiel (H, dont la dernière consigne est illisible et sans schéma) ; D09 contient G à l'identique et n'est pas comptée. L'électrolyse (`HP:electrolyse` du lecteur) est dans le programme (E-7). L'intensité du courant n'est PAS exigible (V3) : on classe les électroaimants par spires seulement. Le lecteur des devoirs note la dernière consigne de D08 sans énoncé : elle n'est pas reprise.


## Chapitre `08-poids` — وزن الأجسام والسّقوط الحرّ

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.poids.masse-et-poids-confondus` (Tu confonds masse et poids : la masse se mesure à la balance) | `eveil.poids.chute-en-ligne-oblique` (Tu dessines la chute libre en ligne oblique ou courbe : l'ob) | `eveil.poids.masse-change-avec-forme-ou-etat` (Tu crois que la masse change quand on change la forme ou l'é) | `eveil.poids.surface-eau-suit-le-recipient` (Tu crois que la surface de l'eau penche avec le récipient : ) | `eveil.poids.masse-change-avec-le-lieu` (Tu crois que la masse change avec le lieu (Lune, sommet d'un) | `eveil.poids.certains-objets-sans-poids` (Tu crois que seuls les objets lourds, non vivants ou qui tom)

### m041 → `exercices/06-exams-2010-2018-chute-poids-et-masse.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2010–2018 ⭐⭐: … ») : Concours 2010 · 2015 · 2016 · 2018 · la chute des corps, le poids et la masse
- Registre : id `C09#3` ; sources `C09#3, C17#3a, C17#3b, C12#3a, C11#6b`
- Sources : C09 (session 2018), support 1, consigne 3 ; C17 (session 2010), support 3 ; C12 (session 2015), support 3, consigne 1 ; C11 (session 2016), support 6, consigne 2 — transcriptions `2018-unique.md`, `2016-unique.md`, `2015-unique.md`, `2010-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2018 · أصلح الخطأ في إفادة مريم حول تفسيرها ظاهرة سقوط ثمار التّفّاح تحت الأشجار. قالت مريم : « تسقط الأجسام وفق منحىً مائل نتيجة تأثير داخليّ تسلّطه الأرض عليها يسمّى : الكتلة »
  - 2010 · أرسم اتّجاه سقوط الثّمرة في الرّسم التّالي. / أسمّي منحى سقوط الثّمرة والقوّة المتسبّبة في ذلك : منحى سقوط الثّمرة ........ لأنّ الأرض تسلّط على كلّ الأجسام التي توجد بجوارها وتسقط سقوطا حرّا قوّةً تسمّى ........
  - 2015 · أكتب داخل كلّ إطار "نعم" أو "لا" : بعضُ الأجسام ليس لها ثِقل بالرّغم من وجودها داخل مجال جاذبيّة الأرض. · كلّما ارتفع رائد الفضاء عن سطح الأرض انخفض وزنُه وكتلتُه. · الوزن مقدار قابل للقياس وحدة قيسه النيوتن.
  - 2016 · لاحظ الأطفال أنّ رائد الفضاء يتنقّل فوق سطح القمر بسهولة رغم ما يحمله من أجهزة ثقيلة. أفسّر ذلك.
- Étapes prévues :
  - 2018 (3) : trois erreurs dans l'explication de la chute (trajectoire oblique → verticale ; « inner » → exercée par la Terre ; « masse » → poids) — trois QCM — 3 q
  - 2010 (3-أ) : dessiner la direction de chute d'un fruit — QCM visuel ; (3-ب) nommer la trajectoire (verticale) et la force (le poids) — deux QCM — 3 q
  - 2015 (3-1) : trois énoncés oui/non (tout corps a un poids près de la Terre ; la masse ne change pas avec l'altitude, le poids oui ; le poids se mesure en newtons) — multi, QCM sur la masse — 2 q
  - 2016 (6-2) : sur la Lune l'astronaute pèse moins, sa masse est la même : il se déplace plus facilement avec ses appareils — QCM, QCM. Le facteur 1/6 n'est pas donné (V1) — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - parler de masse au lieu de poids — ligne C09#3 (d2)
  - tracer une trajectoire oblique — ligne C17#3a (d1)
  - confondre poids et masse — ligne C17#3b (d1)
  - confondre masse et poids — ligne C12#3a (d2)
  - confondre masse et poids — ligne C11#6b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `08/quiz#1`, `08/quiz#2`, `08/quiz#3`, `08/quiz#4`, `08/quiz#5`, `08/01-pratique#3`, `08/01-pratique#4`, `08/02-boss#5`, `08/02-boss#6`, `08/03-revision#3`, `08/04-defi#3`, `08/04-defi#4`, `08/04-defi#5`, `08/05-entrainement#1`, `08/05-entrainement#2`, `08/05-entrainement#4`, `08/05-entrainement#5`
- Note : Le patron est déjà très complet sur le poids (les 30 questions couvrent la chute, la masse et le newton) : une seule mission, et à couper la première si la mise à niveau du `08` en absorbe les gestes (E-1). La ligne C11#6a (satellites en orbite) est écartée : `HP:satellite-orbite`, jamais enseigné. Les trois propositions de 2016 6-1 ne sont pas reprises. Le sujet 2018 écrit « الكتلة » à corriger en « الثقل/الوزن » ; en 2016 et 2015 la masse et le poids sont les deux pôles de la confusion.
