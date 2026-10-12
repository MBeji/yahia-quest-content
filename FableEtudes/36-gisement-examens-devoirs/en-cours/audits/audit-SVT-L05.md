# Audit en aveugle — lot SVT-L05 (gisement 9ᵉ, SVT, examens nationaux, ch. 12)

Auditeur indépendant : je n'ai rien écrit de ce que j'audite. Audit du 2026-10-12, écrit au fil de l'eau.

## État d'avancement

- [x] Prompt lu ; skill `content-audit` invoqué ; consigne `gisement-auditeur.md` lue en entier (pièges L14/L16 compris)
- [x] Contexte : cours ch.03, 09, 10, 11, 12 (`cours.md`) lus ; registre `bio.*` lu sur `origin/main` ; transcriptions 2022, 2024, 2025, 2026 lues
- [x] PDF officiels 2026, 2025, 2024, 2022 téléchargés (sha256 conformes à `gisement.json`), pages des figures regardées
- [x] Figures de l'auteur rendues en Chromium dans le conteneur réel de l'app (`<span dir="ltr">`, 232 px utiles, `SvgFigure`)
- [x] 07 (2026 ex.2)
- [x] 08 (2022 ex.1)
- [x] 09 (2025 ex.3)
- [x] 10 (2024 ex.4)
- [x] Transversal : étiquettes, doublons, fuites, rendu arabe, étages
- [x] Chiffre final

## Cadre

- Arbre audité : `/home/user/wt-svt5`, HEAD = `9a3090c9` = `origin/main` (fetch du 12-10) ; les quatre fichiers sont non suivis (neufs). Empreintes sha256 prises au début : `/tmp/claude-0/svt-l05-audit-work/sha-start.txt`.
- Résolution à l'aveugle : extraction sans clé, sans explication, sans étiquette (`blind.py`), réponses consignées AVANT la levée des clés dans `/tmp/claude-0/svt-l05-audit-work/blind-answers.txt`.
- Gates (moteur `/home/user/eng-svt5`, lien `content → wt-svt5/content`, lecture seule) : `content:check` ✓ ; `content:qa:strict` 0 erreur, aucun avertissement sur `sciences-vie-terre/12` ; `content:figures:check` ✓ ; `content:tranche --chapters 12 --fresh` : 23 questions neuves, clé strictement la plus longue 0/18, positions a 5 · b 4 · c 5 · d 4, 0 paire proche, 0 candidat gabarit. `content:overflow:check` ne démarre pas (navigateur Playwright absent) : remplacé par un contrôle maison (boîtes écran de chaque élément contre le `viewBox`, Chromium 1194) — 0 débordement sur les 8 figures distinctes.
- Portée du donjon (fait qui pèse sur les fuites) : `get_dungeon_questions` (migration `20260720200000`) tire `ORDER BY random()` dans TOUTES les missions non-quiz de la CLASSE (toutes matières et tous chapitres de la 9ᵉ), filtrées par la seule difficulté de mission. Un énoncé du ch.12 qui livre la clé d'une mission des ch.09 ou 11 (ou l'inverse) est donc une vraie fuite ; le `quiz.json`, exclu du donjon, ne compte pas.

---

## 1. `07-examen-2026-ex2-…-maturation.json` (2026 ex.2 — d2 practice 75/15, displayOrder 7)

En-tête : `🏛️ مناظرة 2026 · التمرين 2 ⭐⭐: بنى مجهريّة في الجهاز التّناسلي — تسميتها وبياناتها ومكان نشأتها ونضجها ومصيرها` — conforme, aucune clé dans le titre. Rampe 1,2,2,2,2,2,2 ✓.

Fidélité : figure 07 Q1 = document 1 (spermatozoïde à droite, ovule au milieu avec UNE seule globule polaire et couronne de cellules folliculaires, morula à gauche dans son enveloppe) ✓ ; figure 07 Q2 = repères 1 (pièce intermédiaire, flèche sur le début de la partie spiralée), 2 (globule polaire), 3 (deux flèches vers les cellules folliculaires) ✓, plus le repère 4 (acrosome) déclaré. Aucune étiquette arabe dans le dessin, aucun élément interdit, rien hors `viewBox`. Q3/Q4 = tableau officiel coupé en deux ; Q5/Q6 = 4-أ coupé en deux ; Q7 = 4-ب.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1) appariement | (أ)→ حيوان منويّ, (ب)→ بويضة, (ج)→ توتيّة | idem | OK | trois structures très distinctes ; d1 honnête |
| Q2 (d2) appariement | 1→ قطعة وسطى, 2→ كريّة قطبيّة, 3→ خلايا جريبيّة, 4→ أكروزوم | idem | OK | 2 et 3 par les définitions données ; 1 et 4 exigent le cours ch.10 (« رأس بالنّواة والأكروزوم، قطعة وسطى بالميتوكندريا ») : pas de paire par élimination triviale. Le repère 4 ajouté ne perd rien de 2-ب officielle |
| Q3 (d2) spermatozoïde | a (tubes / épididyme) | a | OK | plan 2×2 propre (chaque terme 2 fois, c à deux erreurs muette) |
| Q4 (d2) ovule | c (ovaire / trompe à l'entrée du spermatozoïde) | c | réserve | clé juste (cours ch.10 : « ينتهي نضجها إثر دخول حيوان منويّ ») ; phrase ajoutée à l'énoncé qui fuit — M-07-1 |
| Q5 (d2) origine de la morula | a | a | OK | |
| Q6 (d2) remise en ordre | b, d, a, c | b, d, a, c | réserve | ordre lisible sur les seuls nombres (1 → 2 → 4 → 64) : d1 réel — m-07-2 |
| Q7 (d2) devenir de la morula | d | d | réserve | clé juste aux deux lectures (jour 7 ou jour 8) ; la donnée « التّوتيّة في اليوم الرّابع » ajoutée fuit — m-07-3 |

Étiquettes : Q3 b et d `bio.repro.lieux-des-gametes-confondus` — le libellé (« formation dans les tubes séminifères, maturation dans l'épididyme ; vésicules séminales et prostate sont des glandes annexes ») nomme exactement l'erreur ✓ ; c à deux erreurs muette ✓. Q5 c `bio.repro.plusieurs-spermatozoides-entrent` exact ✓. Q4 muette : aucune étiquette existante ne nomme « ovule mûr dès l'ovulation » (`ovulation-produit-un-ovule` = stock, `fecondation-reduite-a-l-entree` = fusion des noyaux) ; elle revient en 07 Q4 et 10/07 Q4 seulement (2 questions < 3) : pas de famille neuve ✓.

Verdict partiel 07 : 7/7 clés justes ; 1 majeur (M-07-1), 2 mineurs.

## 2. `08-examen-2022-ex1-…-nephron.json` (2022 ex.1 — d2 practice 75/15, displayOrder 8)

En-tête conforme ; rampe 2,2,2,2 ✓. Fidélité : les quatre QCM officiels ; Q1 réécrit en plan 2×2 nature × rôle (clé officielle « ملحقة » conservée et complétée par le rôle, enseigné ch.10) ; Q3 d complété (« قرص تتوسّطه الحدقة ») ; Q4 précédé d'une définition ajoutée.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d2) prostate | b (glande annexe, partie du liquide séminal) | b | OK | 2×2 propre ; a à deux erreurs muette |
| Q2 (d2) lieu de la fécondation | a (tiers supérieur de la trompe) | a | OK | |
| Q3 (d2) cristallin | c (milieu transparent qui participe à l'image) | c | OK | a « مقعّرة » faux (cours ch.03 : « محدّبة الوجهين »), b = cornée, d = iris |
| Q4 (d2) sécrétion du néphron | b (ammoniac) | b | réserve | définition ajoutée à l'énoncé qui livre la clé de 09/07 Q4 — M-08-1 ; doublon fonctionnel avec 09/07 Q4 — R-1 |

Étiquettes : Q1 c `lieux-des-gametes-confondus` acceptable (le libellé dit « prostate … glandes annexes ») ; mais d (« غدّة ملحقة تنتج الحيوانات المنويّة »), à UNE erreur, exécute plus exactement encore l'erreur du libellé (production des spermatozoïdes hors des tubes séminifères) et reste muette — m-08-2. Q2 b `fecondation-dans-l-uterus` exact ✓ ; c et d muettes (pas d'étiquette « fécondation dans l'ovaire / le pavillon ») ✓. Q3 muette : `bio.vis.*` n'a rien pour « cristallin pris pour la cornée/l'iris/biconcave » (`cornee-quatrieme-membrane`, `recepteurs-hors-retine` ne conviennent pas) ✓. Q4 muette : `bio.excr.etape-du-nephron-confondue` (« attribue une variation à la mauvaise étape ») ne nomme pas « toute substance de l'urine est sécrétée » ; une seule question → pas de famille neuve ✓.

Verdict partiel 08 : 4/4 clés justes ; 1 majeur (M-08-1), 1 mineur, 1 réserve d'orchestration.

## 3. `09-examen-2025-ex3-…-placenta.json` (2025 ex.3 — d3 boss 120/30, displayOrder 9)

En-tête `🏛️ مناظرة 2025 · التمرين 3 ⭐⭐⭐: ثلاثة أحداث في الجهاز التّناسلي لامرأة دورتها 28 يومًا — أسماؤها وبياناتها ووظائف المشيمة` conforme ; rampe 2,2,2,3,3 ✓.

Figure (même SVG en Q1, Q3, Q4) contre le document 3 du PDF : ordre droite → gauche respecté (1 à droite, 3 à gauche), numéros 1-2-3 sous les cases. Événement 1 : ovule rayonnant au-dessus d'un follicule ouvert (« coupe » à paroi pointillée) — reconnaissable, plus schématique que l'officiel (pas de rupture dessinée) ; événement 2 : ovule à couronne, DEUX noyaux accolés au centre, DEUX globules polaires sous l'enveloppe ✓ (officiel : deux masses sombres accolées, « الكريّة القطبيّة الأولى / الثانية ») ; événement 3 : blastocyste creux, masse cellulaire interne, logé dans la muqueuse utérine ✓. Les légendes officielles (« جريب منفجر », « المضغة », « بطانة الرحم », noms des globules polaires) sont retirées : bien, elles livraient Q1. Figure Q2 = événement 2 seul, fidèle. Aucune clé marquée, aucun arabe hors `<title>`, rien hors `viewBox`.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d2) appariement | 1→ إباضة, 2→ إلقاح, 3→ تعشيش | idem | OK | |
| Q2 (d2) observation qui fonde la nature de l'événement 2 | a (deux noyaux voisins) | a | ERREUR de forme | b et c décrivent les événements 1 et 3 : absents de la figure ET hors de « في داخل الخليّة » posé par l'énoncé → éliminés à vue ; le piège nommé par l'explication (cellules folliculaires) n'est dans aucune option — M-09-1 |
| Q3 (d2) lieux | c (ovaire ; tiers sup. de la trompe ; endomètre) | c | OK | plan à trois composantes, chaque valeur exactement 2 fois, aucun vote ; chaque distracteur diffère de la clé sur 2 composantes (muets à juste titre) |
| Q4 (d3) dates | d (14 ; 14 ou 15 ; 21 ou 22) | d | OK | recalculé : ovulation 28 − 14 = 14 (cours ch.11) ; ovule ~24 h → fécondation 14-15 ; nidation au 7ᵉ jour après fécondation (cours ch.12) → 21-22. Chaque valeur 2 fois par position. Explication : le piège « اليوم 7 من الدّورة » n'est encodé par aucune option — m-09-2 |
| Q5 (d3) multi, fonctions du placenta | {a, c, e, f} | {a, c, e, f} | OK | énoncé par énoncé contre le cours ch.12 (§ وظائفها الأربع) : a vrai (CO₂, urée fœtus → mère), b faux (pas de mélange), c vrai, d faux (« كلّ »), e vrai, f vrai (texte du cours : « منع أغلب الجراثيم والأدوية »). Énoncé au pluriel standard d'un multi ; nombre de vraies non déductible |

Chaîne Q1/Q2 : Q2 ne nomme pas l'événement ; l'explication de Q1 nomme les trois événements mais ne dit pas « deux noyaux » : pas de fuite vers Q2. L'explication de Q1 donne l'identité des événements dont Q3 et Q4 ont besoin, pas leurs lieux ni leurs dates : chaîne saine.

Étiquettes : aucune. Q2 à Q4 : distracteurs à deux erreurs ou lectures de figure, muets à juste titre. Q5 est un `multi` : le schéma ne porte d'étiquette que sur les QCM (`qa.ts` l.137) — b et d exécutent pourtant exactement `bio.gros.sangs-melanges-au-placenta` et `bio.gros.barriere-placentaire-absolue` ; rien à faire dans ce type.

Étage : d3 boss défendable — Q4 est un vrai d3 (trois identifications + calendrier) ; Q5 relève plutôt du d2 (rappel du cours, piège « كلّ / أغلب » en miroir) ; Q1 d2 au plus.

Verdict partiel 09 : 5/5 clés justes ; 1 majeur (M-09-1), 1 mineur.

## 4. `10-examen-2024-ex4-…-corps-jaune.json` (2024 ex.4 — d4 challenge 300/60, displayOrder 10)

En-tête `🏛️ مناظرة 2024 · التمرين 4 ⭐⭐⭐⭐: منحنيا درجة حرارة الجسم لامرأتين وبنية مجهريّة في قناة البيض` conforme (aucun résultat) ; rampe 2,3,3,3,3,3,3 ✓.

Figures contre les documents 3, 4, 5 du PDF. Courbes : axe des dates en « jour/mois » (1/4, 14/4, 1/5, 12/5, 1/6, 9/6), échelle UNIFORME vérifiée par script (2,2 unités/jour sur les six repères ; celle du PDF varie de 6,4 à 10 px/jour) — amélioration, sans fuite : l'écart de 28 jours se lit sur les étiquettes de dates, que la question donne de toute façon. Courbe A recalculée sur les 171 points : bas 36,50–36,90 (moyenne 36,63), haut 36,95–37,29 (moyenne 37,19) ; montées juste après 14/4, 12/5, 9/6, descentes au 1/5 et au 1/6 ✓ transcription. Courbe B identique jusqu'au 12/5 puis haute (37,03–37,29) jusqu'au bout ✓. Q4 : A en haut, B en bas, l'énoncé le dit ✓. Document 5 (Q7) : ovule, UN noyau central, couronne folliculaire, DEUX globules polaires ✓. Graduations : `text-anchor="end"` à gauche de l'axe — correct dans l'app (le conteneur `SvgFigure` pose `dir="ltr"`) ; rendues dans un parent `rtl` sans ce conteneur, elles chevaucheraient l'axe : rien à corriger. Plateau chaud de 17 jours (14/4 → 1/5) et 20 jours (12/5 → 1/6) contre 14 jours de phase lutéale au cours ch.11 : aucune question n'en demande la durée ; 17 et 20 comme distracteurs de Q2 sont sains (valeurs vraies d'une AUTRE grandeur, exactement le libellé de `bio.lecture.valeur-d-une-autre-grandeur`).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d2) analyse de la courbe A | a | a | OK | 2×2 (alternance / reste haute) × (36,6→37,2 / 36,1→36,6) ; c muette |
| Q2 (d3) jours entre deux montées | 28 | c = 28 | réserve | 16 + 12 = 28 et 19 + 9 = 28 ✓ ; 29 = avril compté 31 j ou comptage inclusif. La clé est la durée canonique du cycle : devinable sans calcul — m-10-4 |
| Q3 (d3) événement + caractère | d (ovulation, périodique) | d | ERREUR de forme | l'énoncé recopie la clé de Q1 (« من نحو 36,6 إلى نحو 37,2 … ثمّ تنخفض ») — M-10-1 |
| Q4 (d3) comparaison A/B | b | b | OK | c à deux erreurs muette ; d tronquée (sans la partie A) mais fausse par sa 1ʳᵉ composante |
| Q5 (d3) hypothèse sur B dès le 13 mai | c (enceinte) | c | ERREUR de forme | l'énoncé recopie la clé de Q4 (« مطابقة … إلى غاية 12 ماي … بقيت بين 37,1 و37,3 ») — M-10-1 |
| Q6 (d3) corps jaune + endomètre | d | d | ERREUR de forme | l'énoncé redonne la moitié B de la clé de Q4 — M-10-1 ; étiquettes b, c — m-10-5 |
| Q7 (d3) événement 12-13 mai + preuve | b (fécondation ; 2ᵉ globule polaire) | b | réserve | clé juste et fidèle ; la règle donnée (indispensable : aucun cours n'enseigne les globules polaires) désigne la clé, c nie cette règle : d2 réel — m-10-6 |

Explications : celle de Q3 (« إذا تكرّر الارتفاع كلّ 28 يومًا ») et celle de Q5 (« بعد 28 يومًا من الارتفاع السّابق ») livrent la clé calculée de Q2 — M-10-2. Celle de Q1 (« فالتّغيّر دوريّ ») donne la moitié « دوريّ » de Q3 — m-10-3.

Chaînes déclarées : Q5/Q7 — l'énoncé de Q7 (structure de la trompe de B le 13 mai + règle du 2ᵉ globule polaire) mène en une inférence de cours (« الحمل يبدأ يوم الإخصاب ») à la clé de Q5, et l'explication de Q7 (« وقع الإلقاح بين 12 و13 ماي ») aussi ; l'explication de Q5 (« يفسّره الحمل ») mène à l'événement de Q7. C'est la chaîne même du sujet officiel (3 demande l'événement ET l'état physiologique) : réserve, pas défaut (inférence, pas recopie). Q6/Q7 : rien de l'une ne donne l'autre ✓.

Étiquettes : Q2 a (17) et d (20) `valeur-d-une-autre-grandeur` exactes (« autre période ») ✓ ; 29 muette ✓. Q3 muette : « montée attribuée aux règles » n'a pas d'étiquette (`regles-par-hausse-hormonale` parle d'hormones, `regles-signe-de-fecondation` d'autre chose) ; elle revient en Q3 et Q5 a seulement (2 questions) → pas de famille neuve ✓. Q5 muette ✓ (b = lecture de la montée du 12 mai, d = lecture des oscillations). Q6 : voir m-10-5.

Étage : la difficulté réelle des questions est 2,3,2,2-3,2,3,2 (Q3 rappel de cours une fois la périodicité visible, Q5 aux distracteurs faibles, Q7 règle donnée). Le d4 « challenge » ne tient que par la longueur de la chaîne (7 étapes, 3 documents), comme 2026 ex.4 (SVT-L03, 9 étapes / 4 documents) qui était déjà « au bord haut ». Avec les fuites M-10-1 non corrigées, chaque étape est donnée par la suivante et le d4 n'est pas honnête ; corrigées, d4 au bord haut, d3 boss 120/30 serait plus juste — m-10-7.

Verdict partiel 10 : 7/7 clés justes ; 2 majeurs (M-10-1, M-10-2), 5 mineurs.

## 5. Transversal

### 5.1 Rendu arabe et notation

- Chiffres indo-arabes : 0. LaTeX / `$` : 0. Espace entre groupes de chiffres : 0. Lettre latine dans une option : 0. Virgule arabe dans une notation : 0. « على الشكل التالي » : 0 occurrence. Question sans figure qui renvoie à une figure : 0 (10 Q3 ne dit ni « الوثيقة » ni « المنحنى »).
- Chaînes suspectes passées dans `isolateLtrRuns` / `splitMathRuns` (`src/shared/lib/bidi.ts`, identique à `origin/main` de l'arène) puis ordre visuel mesuré caractère par caractère dans Chromium `dir=rtl` : « 14/4 تعني 14 أفريل » (Q1, Q2), « (14/4 تعني 14 أفريل) » (Q4), « 28 − 14 = 14 » (09 Q4 expl.), « 16 + 12 = 28 » (10 Q2 expl.), « (اليوم 0) » (07 Q6 expl.), « 36,6 », « 37,1 و37,3 » : ordre affiché conforme à la doctrine du moteur (arithmétique simple laissée au bidi natif, nombres décimaux et dates d'un seul tenant, parenthèses de prose bien placées). Aucune ligne de formule seule. Aucun défaut.
- Options à composantes séparées par « ؛ » entre mots arabes : correct.

### 5.2 Figures

Toutes vraies contre le PDF (§ 1, 3, 4), aucune ne marque la clé, arabe seulement dans `<title>`, aucun élément ni attribut interdit (`content:figures:check` ✓), aucun débordement (contrôle maison). Rendu dans le conteneur réel (232 px) : lisible ; événement 1 de 09 très petit mais identifiable.

### 5.3 Doublons et fuites inter-missions (le donjon tire dans toute la 9ᵉ)

| paire | jugement |
| --- | --- |
| 07 Q4 ↔ 10/07 Q4 (2021) | partiel : même fait (« ينتهي النّضج إثر دخول حيوان منويّ », même libellé), mais 07 Q4 ajoute l'origine en plan 2×2 et ses distracteurs diffèrent ; deux sujets officiels distincts → réserve, acceptable |
| 07 Q2 ↔ 11/09 Q2-Q3 (2021) | partiel : même phrase de définition de la globule polaire, même cadre d'appariement ; le repère 4 ajouté (acrosome) refait la paire « 4 → الأكروزوم » de 11/09 Q2. Options d'ensemble différentes → réserve |
| 08 Q2 ↔ 12/01 Q2 et 10/01 Q6 | même fait, options et piège (utérus étiqueté) proches, sans le « pourquoi » de 12/01 → réserve |
| 08 Q4 ↔ 09/07 Q4 (2026 ex.1, publiée) | **fuite mutuelle** : l'énoncé PUBLIÉ de 09/07 Q4 (« يتمّ إفراز النّشادر في مستوى ») donne la clé de 08 Q4 ; et l'énoncé de 08 Q4 (définition ajoutée « تنقل خلايا الأنبوب البوليّ … ») donne la clé de 09/07 Q4. Le second sens est corrigeable ici (M-08-1) ; le premier ne l'est qu'en retirant 08 Q4 ou en retouchant 09/07 (hors périmètre) — R-1 |
| 08 Q3 ↔ 03/05 Q3 | même amorce « الجسم البلّوريّ: » ; options différentes (la clé de 03/05 est la négation du distracteur a de 08) → réserve |
| 09 Q5 ↔ 12/03 Q2 et quiz 12 Q6 | mêmes idées et mêmes pièges (mélange des sangs, barrière absolue) sous un autre format (multi) ; le quiz est hors donjon → réserve |
| 09 Q2 ↔ 10 Q7 (dans la tranche) | même cadre « ovule fécondé dessiné → quelle observation prouve l'événement », SVG de même facture ; clés différentes (deux noyaux / 2ᵉ globule polaire), options différentes → réserve |
| 09 Q4 ↔ 12/02 Q5, 07 Q7 ↔ 12/02 Q1 | faits de cours (nidation au 7ᵉ jour, morula de 64 cellules au 4ᵉ jour) redits dans des énoncés ou explications — m-07-3 pour la seule donnée ajoutée par l'auteur |
| dans la tranche | aucun gabarit répété (`content:tranche` : 0 paire proche, 0 candidat gabarit) |

### 5.4 Étiquettes (libellés lus sur `origin/main`)

Posées : toutes exactes (`lieux-des-gametes-confondus` 07 Q3 b, d et 08 Q1 c ; `plusieurs-spermatozoides-entrent` 07 Q5 c ; `fecondation-dans-l-uterus` 08 Q2 b ; `valeur-d-une-autre-grandeur` 10 Q2 a, d). Muettes déclarées : justes, sauf 08 Q1 d (m-08-2) et 10 Q6 b, c (m-10-5). Aucune famille neuve justifiée (aucune erreur muette ne revient dans ≥ 3 questions distinctes).

---

## 6. Défauts classés et correctifs exacts

### Critiques

Aucun : 23/23 clés justes (re-résolues à l'aveugle), aucune explication qui contredit sa clé, aucune figure fausse.

### Majeurs

**M-07-1 — 07 Q4 (et 07 Q5 explication) : donnée ajoutée qui fuit vers le ch.11 et oriente la clé.** « وتبقى حيّة نحو 24 ساعة بعد الإباضة إن لم يدخلها حيوان منويّ » n'est pas dans le sujet ; elle donne la moitié « البويضة … تعيش نحو 24 ساعة » de la clé de 11/09 Q4 et la moitié « تضمحلّ بعد نحو 24 ساعة » de 11/08 Q5 (même pool de donjon), et « إن لم يدخلها حيوان منويّ » désigne la composante « إثر دخول حيوان منويّ » de la clé de Q4 elle-même. L'explication de 07 Q5 redit « تضمحلّ بعد نحو 24 ساعة ».
- 07 Q4 `prompt` → « البويضة خليّة جنسيّة تنتجها المرأة. أين تتكوّن هذه الخليّة (النّشأة) وأين ينتهي نضجها؟ » (même forme que Q3 ; les quatre options restent justes/fausses comme avant : a et d placent la fin de la maturation dans l'ovaire, b et d l'origine dans la trompe).
- 07 Q5 `explanation` : remplacer « فالبويضة غير المخصّبة تضمحلّ بعد نحو 24 ساعة ولا تنقسم » par « فالبويضة غير المخصّبة تضمحلّ ولا تنقسم ».

**M-08-1 — 08 Q4 : définition ajoutée qui livre la clé de 09/07 Q4.** « تنقل خلايا الأنبوب البوليّ مادّة من الدّم إلى داخل الأنبوب » donne « الأنبوب البولي », clé de 09/07 Q4 ; l'explication le redit. La notion de « إفراز » est enseignée au ch.09 (§ « إعادة الامتصاص والإفراز ») : la définition est inutile.
- `prompt` → « من وظائف النّيفرون الإفراز. أيّ المواد التّالية يفرزها النّيفرون؟ »
- `explanation` : remplacer « تفرز خلايا الأنبوب البوليّ النّشادر: » par « يفرز النّيفرون النّشادر: » (le reste inchangé).

**M-09-1 — 09 Q2 : deux distracteurs éliminés à vue et renvoi à une figure absente.** b (« جريب جداره مفتوح تخرج منه الخليّة ») et c (« كتلة خلايا مجوّفة منغرسة في سطح الرّحم ») décrivent les événements 1 et 3 : absents de la figure de Q2 et contraires à « في داخل الخليّة » posé par l'énoncé — la question se réduit à a contre d. L'énoncé dit « الحدث 2 من الوثيقة » alors que Q2 ne montre qu'un dessin (renvoi à la figure d'une autre question, tirée seule au donjon). L'énoncé décrit en outre tout ce qui n'est pas la clé (couronne, enveloppe, globules polaires), si bien que la clé est la seule observation intérieure non citée. Le piège de l'explication (cellules folliculaires) n'est porté par aucune option.
- `prompt` (figure inchangée) → « يبيّن الرّسم التّالي حدثًا يمكن مشاهدته في الجهاز التّناسليّ لامرأة. الخلايا الجريبيّة خلايا صغيرة نشأت في الجريب وبقيت محيطة بالبويضة. ما الملاحظة في الرّسم التي تحدّد طبيعة هذا الحدث؟ »
- options : a inchangée « نواتان متجاورتان في وسط الخليّة » (clé) ; b → « خلايا جريبيّة تحيط بالغلاف من الخارج » ; c → « غلاف سميك يحيط بسيتوبلازم الخليّة » ; d inchangée « خليّتان متماثلتان متلاصقتان داخل الغلاف ».
- `explanation` → « يُظهر الرّسم خليّة واحدة في وسطها نواتان متجاورتان: إحداهما أصلها من الحيوان المنويّ والأخرى من البويضة، وهما تقتربان من بعضهما قبل أن تنصهرا في نواة واحدة. وهذه مرحلة من مراحل اندماج المشيجين. أمّا الخلايا الجريبيّة والغلاف فيحيطان بالبويضة قبل دخول الحيوان المنويّ وبعده، فلا يحدّدان الحدث، والخليّتان المتماثلتان لا تظهران إلّا بعد انصهار النّواتين، وليستا في هذا الرّسم الذي فيه خليّة واحدة. الخطأ الشائع: قراءة الخلايا المحيطة بالغلاف على أنّها العلامة الفاصلة، وهي توجد قبل الإباضة وبعدها. »
- Vérifié : b et c sont des observations VRAIES de la figure mais non spécifiques (présentes sur l'ovule non fécondé de 07 Q1) — aucune n'est une seconde bonne réponse ; aucune option ne parle des globules polaires (qui, avec la règle donnée en 10 Q7, seraient aussi probantes) ; longueurs a 31 · b 36 · c 33 · d 39 : clé non la plus longue ; plus de renvoi à un document absent ; aucune nouvelle fuite (l'explication ne nomme ni lieu ni date, rien de Q3/Q4).

**M-10-1 — 10 Q3, Q5, Q6 : les énoncés recopient les clés de Q1 et Q4.** Q3 : « ترتفع … فجأة من نحو 36,6 إلى نحو 37,2 درجة … وتبقى مرتفعة عدّة أيّام ثمّ تنخفض » = les deux composantes de la clé de Q1 (b, c, d de Q1 réfutées par simple lecture de Q3). Q5 : « مطابقة لحرارة المرأة (أ) إلى غاية 12 ماي … وبقيت بين 37,1 و37,3 درجة إلى آخر التّسجيل » = la clé de Q4 presque mot pour mot. Q6 : « بقيت بين 37,1 و37,3 درجة منذ 12 ماي … دون أن تنخفض » = la moitié B de la clé de Q4. Au donjon, Q3/Q5/Q6 tirées avant Q1/Q4 les résolvent. Correctif : donner le DOCUMENT au lieu de sa lecture.
- 10 Q3 `prompt` → « تبيّن الوثيقة التّالية تغيّر درجة حرارة جسم امرأة (أ) قادرة على الإنجاب خلال ثلاثة أشهر، والتّواريخ على المحور الأفقيّ مكتوبة بصيغة اليوم/الشهر: 14/4 تعني 14 أفريل. ما الحدث الذي يتزامن مع الارتفاع الفجائيّ لدرجة حرارة جسمها، وماذا يبيّن المنحنى عن نشاط الجهاز التّناسلي للمرأة؟ » suivi, après un saut de ligne, du SVG de Q1 tel quel (courbe A seule). Options et clé inchangées. « فجائيّ » figure dans les quatre options de Q1 : aucune fuite.
- 10 Q5 `prompt` → « تبيّن الوثيقة التّالية تغيّر درجة حرارة جسم امرأة (ب) قادرة على الإنجاب خلال ثلاثة أشهر، والتّواريخ بصيغة اليوم/الشهر (14/4 تعني 14 أفريل). ما الفرضيّة التي تفسّر حالتها الفيزيولوجيّة ابتداء من 13 ماي؟ » + SVG actuel de Q5 (courbe B seule). Toujours résoluble seule : montée du 12/5 (ovulation), pas de baisse ensuite alors que la baisse d'avril est venue 17 jours après la montée → pas de règles → grossesse ; b réfutée par la montée du 12/5.
- 10 Q6 `prompt` → « تبيّن الوثيقة التّالية تغيّر درجة حرارة جسم امرأة (ب) قادرة على الإنجاب خلال ثلاثة أشهر، والتّواريخ بصيغة اليوم/الشهر (14/4 تعني 14 أفريل). ما مصير الجسم الأصفر وبطانة الرّحم عندها ابتداء من 20 ماي؟ » + SVG actuel de Q6.
- 10 Q5 `explanation` (sa première phrase citait l'A absente du nouvel énoncé et le « 28 » de M-10-2) → « بعد الإباضة ترتفع الحرارة وتبقى مرتفعة، وفي دورة عاديّة، كما في أفريل عند المرأة (ب) نفسها، تنخفض عند نهاية الدّورة ثمّ تعاود الارتفاع في الدّورة الموالية. أمّا بعد ارتفاع 12 ماي فلم تنخفض حرارتها عند الموعد المنتظر، ممّا يوحي بأنّ الحيض لم يحدث، وهذا يفسّره الحمل. فالحيض يقع في حرارة منخفضة، وارتفاع الحرارة يوم 12 ماي دليل على إباضة وقعت، والإباضة لا تتكرّر كلّ أسبوع بل مرّة في الدّورة. الخطأ الشائع: عدّ الحرارة المرتفعة علامة على الحيض، أو على غياب الإباضة. »
- Vérifié : les trois nouveaux énoncés ne contiennent aucune valeur ni date lue sur la courbe ; « (14/4 تعني 14 أفريل) » est la chaîne déjà rendue correctement en Q4 ; aucun ne nie une prémisse ni ne rend un distracteur vrai (Q5 b reste fausse : la montée du 12 mai est visible).

**M-10-2 — 10 Q3 et Q5 explications : la clé calculée de Q2 (28 jours) en clair.**
- 10 Q3 `explanation` : remplacer « وإذا تكرّر الارتفاع كلّ 28 يومًا فمعنى ذلك » par « وإذا تكرّر الارتفاع بانتظام من دورة إلى أخرى فمعنى ذلك ».
- 10 Q5 `explanation` : réglé par le texte de M-10-1.

### Mineurs

- **m-07-2 — 07 Q6 (d2)** : l'ordre se lit sur les nombres des options (1 → 2 → 4 → 64) ; difficulté réelle d1. Pas de correctif de texte (la remise en ordre est la forme de 4-أ officielle) ; noter d1 si l'orchestrateur veut une étiquette honnête.
- **m-07-3 — 07 Q7** : la donnée ajoutée « تتكوّن التّوتيّة في اليوم الرّابع بعد الإلقاح » + « أي في اليوم الثّامن » n'est pas utile : la formulation officielle n'est PAS ambiguë pour les options proposées (jour 7 ou jour 8 → embryon implanté, enveloppe perdue au jour 6 : d dans les deux lectures ; b et c fausses dans les deux). Avec l'énoncé de 07 Q5 (« 64 خليّة »), elle livre aussi la clé de 12/02 Q1 (« 64 خليّة في اليوم الرّابع »). `prompt` → « ما مصير التّوتيّة بعد 4 أيّام من تكوّنها؟ » ; `explanation` : remplacer « فتكون في اليوم 8 قد صارت مضغة منغرسة. » par « فبعد 4 أيّام من تكوّن التّوتيّة تكون قد صارت مضغة منغرسة. »
- **m-07-4 — 07 Q3 explication → 08 Q1** : « فغدّتان ملحقتان تفرزان مكوّنات من السّائل المنويّ » énonce la clé de 08 Q1 (même chapitre, même pool). Remplacer « أمّا الحويصلتان المنويّتان والبروستات فغدّتان ملحقتان تفرزان مكوّنات من السّائل المنويّ، ولا يتكوّن فيهما حيوان منويّ ولا ينضج. الخطأ الشائع: نسبة النّشأة أو النّضج إلى غدّة ملحقة لأنّ سائلها يرافق الحيوانات المنويّة. » par « أمّا الحويصلتان المنويّتان والبروستات فلا يتكوّن فيهما حيوان منويّ ولا ينضج. الخطأ الشائع: نسبة النّشأة أو النّضج إلى الحويصلة المنويّة أو البروستات لأنّ سائلهما يرافق الحيوانات المنويّة. » (Le libellé de l'étiquette, affiché sur erreur, dit aussi « glandes annexes » : fuite résiduelle inévitable, sans gravité.)
- **m-08-2 — 08 Q1 d** : poser `"misconceptionTag": "bio.repro.lieux-des-gametes-confondus"` sur d (« غدّة ملحقة تنتج الحيوانات المنويّة », une seule erreur : production des spermatozoïdes hors des tubes séminifères) ; garder c étiquetée ; a (deux erreurs) muette.
- **m-09-2 — 09 Q4 explication** : le piège « اليوم السّابع … اليوم 7 من الدّورة » n'est encodé par aucune option. Remplacer « الخطأ الشائع: قراءة «اليوم السّابع» على أنّه اليوم 7 من الدّورة، أو وضع الإباضة عند نهاية الدّورة، أو تبديل تاريخي الإلقاح والانغراس. » par « الخطأ الشائع: وضع الإباضة عند نهاية الدّورة، أو إعطاء الإلقاح والانغراس اليوم نفسه، أو تبديل تاريخيهما. » (vérifié : a et b donnent le même jour aux événements 2 et 3, a et b placent l'ovulation au jour 28, c les échange).
- **m-10-3 — 10 Q1 explication** : « فالتّغيّر دوريّ » donne la moitié « دوريّ » de la clé de Q3. Remplacer « ثمّ يتكرّر الارتفاع يوم 12 ماي ويوم 9 جوان: فالتّغيّر دوريّ، ويتناوب فيه طوران من الحرارة، » par « ثمّ يتكرّر الارتفاع يوم 12 ماي ويوم 9 جوان، فيتناوب طوران من الحرارة، ».
- **m-10-4 — 10 Q2** : la clé (28) est la durée canonique du cycle ; un élève la choisit sans compter. Inhérent aux données officielles ; pas de correctif de texte ; difficulté réelle d2.
- **m-10-5 — 10 Q6 étiquettes** : b (« الجسم الأصفر يواصل إفراز الهرمونات ؛ بطانة الرّحم تتهدّم ») et c (« يضمر ؛ تبقى سميكة ») découplent l'utérus des hormones ovariennes : exactement `bio.cycle.uterus-autonome` (« Tu crois que l'utérus règle son propre cycle … : c'est l'ovaire qui le commande, par des hormones portées par le sang »). Poser cette étiquette sur b et sur c ; a (deux erreurs) reste muette.
- **m-10-6 — 10 Q7** : la règle donnée (indispensable, aucun cours n'enseigne les globules polaires) désigne la clé, et c (« الإباضة ؛ ظهور الكريّة القطبيّة الثّانية ») contredit cette règle : d2 réel. Pour obliger au moins la lecture du dessin : remplacer « وتلتصق بها خارج سيتوبلازمها كريّتان قطبيّتان. » par « وتلتصق بها خارج سيتوبلازمها كريّات قطبيّة يظهر عددها في الرّسم. » (le dessin en montre deux ; clé inchangée). Chaîne Q5/Q7 : voir § 4, réserve.
- **m-10-7 — étage de 10** : d4 challenge au bord haut ; défendable par la longueur de la chaîne une fois M-10-1 corrigé, sinon non. Option honnête : d3 boss 120/30.

### Réserves d'orchestration

- **R-1 — 08 Q4 ↔ 09/07 Q4** : après M-08-1, il reste que l'énoncé publié de 09/07 Q4 (« يتمّ إفراز النّشادر في مستوى ») livre la clé de 08 Q4 dans le même pool. À trancher par l'orchestrateur : garder (fidélité au sujet 2022, précédent SVT-L04 sur le triplet ammoniac) ou retirer 08 Q4.
- Doublons partiels du § 5.3 : acceptables (items officiels distincts, options différentes).

---

## 7. Chiffre final

| fichier | questions | clés fausses | majeurs | mineurs |
| --- | --- | --- | --- | --- |
| 07 (2026 ex.2) | 7 | 0 | 1 (M-07-1) | 3 (m-07-2, m-07-3, m-07-4) |
| 08 (2022 ex.1) | 4 | 0 | 1 (M-08-1) | 1 (m-08-2) + R-1 |
| 09 (2025 ex.3) | 5 | 0 | 1 (M-09-1) | 1 (m-09-2) |
| 10 (2024 ex.4) | 7 | 0 | 2 (M-10-1, M-10-2) | 5 (m-10-3 à m-10-7) |
| **total** | **23** | **0** | **5** | **10** |

Questions à reprendre pour les majeurs : 07 Q4 (+ explication de 07 Q5), 08 Q4, 09 Q2, 10 Q3, 10 Q5, 10 Q6 — 7 questions. Étiquettes : 6 posées toutes exactes ; 3 à ajouter (08 Q1 d, 10 Q6 b et c) ; aucune famille neuve. Doublons : aucun gabarit dans la tranche ; une fuite mutuelle avec une mission publiée (R-1) ; doublons partiels déclarés acceptables.

**Verdict : à corriger avant livraison** (aucune clé fausse ; cinq majeurs de fuite ou de forme, tous corrigeables par les textes ci-dessus).
