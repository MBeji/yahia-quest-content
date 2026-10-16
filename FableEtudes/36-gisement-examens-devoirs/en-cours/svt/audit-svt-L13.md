# Audit indépendant — gisement SVT 9ᵉ, vague 2, lot L13 (m038–m043)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills `content-audit` puis
`prof-svt-9eme`). Périmètre : 6 missions, `08-at-tanaffus` 12–14 et `09-al-ikhraj` 10–12, branche
`wip/gisement-svt-9eme-sessions` (commit `818fdb66`). Aucun fichier audité n'est modifié.

Sources lues : transcriptions officielles des sessions citées ; PDF officiels (2010, 2015, 2016, 2018, 2019 ;
2002 et 2005 : l'URL renvoie une page HTML, pas de PDF) ; `cours.md` des chapitres 07, 08, 09 sur `origin/main`.

Rapport écrit au fil de l’eau (état : terminé).

## m038 — `08-at-tanaffus/exercices/12-examens-2019-ex3-et-annales-alveole-frottis-hemoglobine.json`

Étage annoncé d2 (`practice` 75/15) ; 10 questions. Données comparées aux transcriptions 2019 ex.3, 2005 ex.3,
2006 ex.2, 2002 ex.3, 2016 ex.2, 2010 ex.1 et au PDF 2019 (page 2, document 3, rendu à 300 dpi).

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2019 | c (شعيبة / سنخ) | c | OK, réserve | repère 1 déplacé par rapport au PDF (voir « faits signalés ») ; univoque sur la figure de la mission |
| 2 | 2019 | d (paroi mince) | d | réserve (majeur) | clé = rappel du nombre de 08/02-tamrin Q6 ; seule option chiffrée et la plus courte |
| 3 | 2019 | b (réaction 1, O₂ monte) | b | OK, réserve | plan 2×2 propre ; les valeurs 10 → 20 mL viennent du cours, pas de 2019 |
| 4 | 2019 | a (dissociation, consommation) | a | réserve (majeur) | explication qui donne la clé de Q3 ; valeurs 20 → 2 mL = quiz 08 Q9, pas 2019 |
| 5 | 2005 | 1 hématie, 2 plasma, 3 leucocyte | idem | OK, réserve (mineur) | pointe de la flèche 2 à 4–5 unités de deux hématies |
| 6 | 2005 | GR → gaz, plasma → nutriments, GB → défense | idem | OK, réserve (mineur) | trois faits du chapitre 06 (01-tamrin Q5, 03-boss Q3, Q6) |
| 7 | 2006 | d (paroi mince, organes → cœur) | d | OK | 2×2 propre, fidèle |
| 8 | 2010 | c (أسناخ) | c | réserve (majeur) | doublon interne avec Q1 (élément 2) : fuites croisées des explications |
| 9 | 2002 | a (1 et 4) | a | OK | figure fidèle, sens de circulation lisible |
| 10 | 2016 | b | b | OK, réserve (mineur) | `difficulty: 3` dans une mission d2 ; étiquette exacte |

Re-résolution : 10/10 clés justes, aucune ambiguïté de clé.

### Faits signalés

**Repère 1 de 2019 (شعيبة ou bronche ?) — شعيبة هوائيّة, clé `c` juste.** Sur le PDF (page 2, document 3, 300 dpi),
la flèche « 1 » vise l'extrémité supérieure d'un tube gris qui se divise en tubes plus fins, chacun terminé par une
grappe ; « 2 » touche une sphère au bord d'une grappe (سنخ) ; l'accolade « 3 » embrasse une grappe entière
(حويصلة). Le tube porte, collées, les légendes « شريان رئوي » et « وريد رئوي » : c'est la شعيبة du schéma classique
du manuel, pas une شعبة (qui porterait plusieurs lobules). Sur le PDF, le tube visé se ramifie encore, ce qui, au
regard du cours 08 (« شعيبات … تنتهي كلّ واحدة بحويصلة »), aurait rendu « شعبة » défendable ; la mission place
la flèche 1 sur un tube **terminal** qui finit sur une grappe (rendu vérifié à 232 px), ce qui rend la clé
univoque. Écart de figure à **déclarer** dans le rapport d'auteur (repère 1 déplacé d'un cran vers l'aval ;
légendes des vaisseaux et repère 3 retirés). Les deux vaisseaux de la figure ne portent pas de nom : la couleur
inversée du PDF (artère pulmonaire en rouge) ne peut plus induire en erreur ; la consigne « redessiner l'artère en
bleu » est sans objet.

**Équation de l'hémoglobine donnée dans l'énoncé (Q3, Q4) — acceptable.** Le sujet 2019 q3-b fait compléter
« ……… ⇄ ……… + أكسيجين », flèche du haut « 1 » vers l'oxyhémoglobine, flèche du bas « 2 » vers la dissociation
(lu sur le PDF, page 3). La mission donne les deux réactions écrites séparément avec cette même numérotation et
fait trouver le lieu de chacune (q3-c) : l'équation n'est pas demandée seule (plan ; 08/07 Q6 et quiz Q8 posent
déjà une équation à compléter), et la donner ne livre ni la clé de Q3 ni celle de Q4. Rendu RTL vérifié : la
flèche « ← » pointe dans le sens de lecture, vers le produit.


### Défauts

**[MAJOR] m038 Q8 ↔ Q1 : doublon interne et fuites croisées.** Q1 fait distinguer le سنخ (un sac) de la
حويصلة (la grappe) ; Q8 demande de quoi la حويصلة est faite. L'explication de Q1 dit « الحويصلة الرئويّة هي العنقود
الذي تنتهي به الشّعيبة », celle de Q8 dit « تنتهي كلّ شعيبة بحويصلة رئويّة، وتحمل هذه الحويصلة … الأسناخ » : chacune
résout l'autre (le donjon tire au hasard). Correctif : **retirer Q8** (item 2010-3, ajout de fusion ; la mission
passe à 9 questions, au-dessus du plancher de 6). À défaut, garder Q8 et retirer de l'explication de Q1 les deux
dernières phrases (à partir de « بينما الحويصلة ») : la fuite Q8 → Q1 demeure, d'où la préférence pour le retrait.

**[MAJOR] m038 Q2 : forme et doublon.** La clé « جدار رقيق لا يتجاوز سمكه 0,5 ميكرون » est la seule option
chiffrée, la plus courte (35 contre 37–40), et reprend la donnée que 08/02-tamrin Q6 fait déjà rappeler (« كم يبلغ
سمك جدار السنخ؟ »). Le sujet 2019 demande la propriété, pas la valeur. Remplacer le texte de l'option `d` par :
`جدار رقيق جدًّا يقصّر مسافة عبور الغازين` (40 caractères, à égalité avec `c` : ni la plus longue ni la plus
courte ; même gabarit « structure + fonction » que les trois distracteurs ; une seule réponse juste).
L'explication garde sa valeur 0,5 ميكرون (elle n'est donnée qu'après réponse et ne résout aucune autre question).

**[MAJOR] m038 Q4 : fuite vers Q3.** L'explication finit par « فالتفاعل نفسه يسير في الرئتين في اتّجاه (1) وفي
الأعضاء في اتّجاه (2) » : c'est la clé de Q3. Remplacer cette phrase par :
`فالأكسي هيموغلوبين يتفكّك حيث يُستهلك الأكسيجين.` (aucune mention des poumons ni du sens (1)).

**[MINOR] m038 Q3 et Q4 : attribution des données.** Le sujet 2019 ne donne aucun volume ; 10 → 20 mL est la
donnée du cours 08 (§ échanges) et 20 → 2 mL celle du quiz 08 Q9. Les deux questions restent justes et autonomes,
mais l'étiquette « (مناظرة 2019) » couvre des chiffres qui n'y sont pas. Correctif : préfixe
`(مناظرة 2019، بمعطيات الدّرس)` sur Q3 et Q4, et une ligne dans le rapport d'auteur.

**[MINOR] m038 Q5 : flèche 2.** Elle finit en `L148 62`, la pointe à 4–5 unités des hématies (150.2 ; 45.8) et
(163.2 ; 67.0) : à 232 px, on peut la lire sur une hématie. Aucune trajectoire droite depuis l'étiquette « 2 » ne
trouve une plage de plasma dégagée (recherche exhaustive). Correctif : **retirer** l'hématie (163.2 ; 67.0) (ses
deux `<circle cx="163.2" cy="67.0" …>`). Dégagement vérifié après retrait : 7,8 unités au bout du trait, 9,1 à la
pointe. La clé ne change pas.

**[MINOR] m038 Q10 : étage.** `difficulty: 3` dans une mission annoncée d2 (assignation et `difficulty: 2` du
fichier). Soit Q10 passe à `difficulty: 2` (recommandé : la difficulté réelle est celle de Q9), soit la mission
monte d3 (`boss` 120/30), ce que l'assignation n'a pas prévu.

**[MINOR] m038 Q6 et Q7 : recouvrement.** Q6 reprend trois faits posés au chapitre 06 (01-tamrin Q5, 03-boss Q3
et Q6), Q7 la moitié de 07/02-tamrin Q5 (paroi). Ces questions sont prévues par le plan (2005 q3 et 2006 q3) et
leur forme (appariement, 2×2 avec le sens du sang) est neuve : aucun correctif exigé.

**[MINOR] m038 : titre.** « من السّنخ الرّئويّ إلى الكريّة الحمراء » met « السّنخ » sous les yeux de l'élève avant
Q1 (élément 2 : سنخ ou حويصلة) et Q8 (أسناخ). Titre de remplacement :
`🏛️ مناظرات 2002–2019 · من الرّئة إلى الكريّة الحمراء ⭐⭐`.

Observations sans défaut : Q8 garde le distracteur « النّيفرونات » du sujet 2010 (notion du chapitre 09, mais
c'est l'option d'origine et elle reste fausse) ; « الأساخ » → « الأسناخ » est une coquille corrigée, pas une
modernisation : pas de mention dans l'énoncé nécessaire. Q9 : « ما رقما الوعاءين » au duel, mais toutes les
options sont des paires : rien n'est trahi. Q10 : étiquette `bio.circ.artere-sang-oxygene` sur `a` exécute
exactement « artère = sang riche en oxygène » (1 et 4 quanis → artères) ; `d` (deux erreurs) reste muette.

## m039 — `08-at-tanaffus/exercices/13-examens-2018-ex2-2016-qcm-modele-cloche-mouvements-respiratoires.json`

Étage annoncé d2 (`practice` 75/15) ; 6 questions. Comparé à la transcription 2018 ex.2, 2016 ex.1 item 7, et
au PDF 2018 (page 2, dessin (أ), rendu à 200 dpi).

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2018 | tube ↔ trachée/bronches, ballons ↔ poumons, membrane ↔ diaphragme | idem | OK | |
| 2 | 2018 | c (expiration) | c | réserve (majeur) | figure contraire au PDF (membrane bombée vers le bas, ballons gonflés) ; étiquette sur la mauvaise option |
| 3 | 2018 | d (diminue, diaphragme relâché qui monte) | d | OK, réserve | recouvre 08/05-tadrib Q1 pour la cause ; plan 2×2 propre |
| 4 | 2018 | b (supérieure, l'air sort) | b | OK, réserve (majeur) | explication qui résout Q6 |
| 5 | 2018 | a + b | a + b | OK, réserve (mineur) | deux distracteurs de remplissage |
| 6 | 2016 | a (les poumons se distendent) | a | réserve (majeur) | doublon de fait du quiz 08 Q1 ; résolue par les explications de Q2, Q3, Q4 |

Re-résolution : 6/6 clés justes.

### Faits signalés : le dessin (أ) de 2018 lu comme une expiration — **confirmé**

Sur le PDF, la membrane est **bombée vers le haut, dans la cloche**, la flèche noire pousse vers le haut et les
deux ballons sont **petits et fripés** : c'est l'expiration (le cours 08, § méthode, le dit aussi : remonter la
membrane vide les ballons). La clé `c` est juste.

### Défauts

**[MAJOR] m039 Q1 et Q2 : figure contraire au document et à la clé.** Le SVG (le même dans Q1 et Q2) dessine la
membrane **bombée vers le bas** (`M66 136 Q140 150 214 136 …`, position d'inspiration), deux ballons pleins
(`rx 15 ry 24`), un fond rigide (le trait `L70 136 L210 136` ferme la cloche au-dessus de la membrane) et une
cloche **ouverte en haut** de part et d'autre du bouchon (aucun trait de 70 à 116 ni de 164 à 210 à y = 40),
alors que l'énoncé dit « مغلق في الأعلى ». Avec des ballons gonflés, le distracteur `a` (« الشهيق ، لأنّ البالونين
يمتلئان بالهواء ») devient défendable sur la figure. Correctif : remplacer les deux `<svg>` par le dessin
ci-dessous (marqueur `c1` dans Q1, `c2` dans Q2 ; rendu vérifié dans Chromium à 232 px : cloche fermée, membrane
bombée vers le haut, ballons dégonflés, flèche vers le haut, aucun texte qui donne la phase) :

```
<svg viewBox="0 0 280 190"><title>رسم جهاز تجريبيّ: ناقوس زجاجيّ مغلق في الأعلى بسدّادة يعبرها أنبوب زجاجيّ على شكل Y ينتهي ببالونين داخل الناقوس، وقاعدة الناقوس مغلقة بغشاء مطّاطيّ يشير سهم أسود تحته إلى الأعلى</title><rect x="0" y="0" width="280" height="190" fill="#ffffff"/><defs><marker id="c2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#0f172a"/></marker></defs><path d="M70 40 L210 40 L210 136 Q140 112 70 136 Z" fill="#f1f5f9" stroke="none"/><path d="M116 40 L70 40 L70 136 M164 40 L210 40 L210 136" fill="none" stroke="#0f172a" stroke-width="2.4"/><rect x="116" y="26" width="48" height="16" rx="3" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/><path d="M140 8 L140 56 M140 56 L116 74 M140 56 L164 74" fill="none" stroke="#0f172a" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><path d="M140 8 L140 56 M140 56 L116 74 M140 56 L164 74" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="116" cy="89" rx="11" ry="15" fill="#fbcfe8" stroke="#0f172a" stroke-width="2"/><ellipse cx="164" cy="89" rx="11" ry="15" fill="#fbcfe8" stroke="#0f172a" stroke-width="2"/><path d="M66 136 Q140 112 214 136 L214 146 Q140 122 66 146 Z" fill="#fdba74" stroke="#0f172a" stroke-width="2"/><path d="M140 184 L140 150" stroke="#0f172a" stroke-width="3" marker-end="url(#c2)"/></svg>
```

**[MAJOR] m039 Q2 : étiquette mal placée.** `bio.resp.mecanique-ventilatoire-inversee` (« à l'inspiration, le
diaphragme se contracte et descend… ») est posée sur `a`, dont l'erreur est une lecture des ballons. L'erreur du
libellé est exactement celle de `b` (« الغشاء يرتفع كما يرتفع الحجاب الحاجز عند تقلّصه »). Correctif : déplacer
l'étiquette de `a` vers `b` ; `a` reste muette.

**[MAJOR] m039 Q6 : doublon et fuites.** « أثناء الشهيق : تتمطّط الرئتان » est le fait du quiz 08 Q1 (« زيادة حجم
الرئتين وانخفاض الضغط داخلهما ») ; ses distracteurs `b` et `d` sont éliminés par les explications de Q3 (« وفي
الشّهيق يحدث العكس: يتقلّص الحجاب فينخفض ويكبر القفص ») et de Q4 (« انخفاض الضّغط … يُدخل الهواء في الشّهيق »), et `c`
par le « الخطأ الشائع » de Q4 (les poumons qui « aspirent ») — toutes deux avant Q6 dans `displayOrder`. Le plan
ne gardait l'item 2016 que « sans répéter … quiz Q1 ». Le retirer ferait tomber la mission à 5 questions (sous le
plancher de 6 de R5). Correctif retenu : garder Q6 et couper les fuites :
- Q3, explication : supprimer la phrase « وفي الشّهيق يحدث العكس: يتقلّص الحجاب فينخفض ويكبر القفص. » ;
- Q4, explication : supprimer « أمّا انخفاض الضّغط داخل الرئتين عن الضّغط الجوّيّ فهو ما يُدخل الهواء في الشّهيق. »
  et remplacer le « الخطأ الشائع » par `الخطأ الشائع: عكس اتّجاه الضّغط، فيُظنّ أنّ الهواء يخرج حين ينخفض الضّغط داخل الرئتين.`
  (c'est l'erreur de `d`, étiquetée) ;
- Q2, explication : remplacer « هذا ما يحدث في الزفير، حين يرتخي الحجاب الحاجز فيرتفع. » par
  `هذا ما يجسّمه الجهاز في الزفير.` et le « الخطأ الشائع » par
  `الخطأ الشائع: الحكم على الطّور من شكل البالونين دون النظر إلى اتّجاه حركة الغشاء.`
  (sinon Q2 donne la cause de Q3 et le distracteur `b` de Q6).
Le recouvrement de fond avec le quiz Q1 demeure : **[MINOR]** résiduel, à arbitrer par l'orchestrateur (garder
pour atteindre 6 questions, ou remplacer par une question neuve tirée de 2018).

**[MINOR] m039 Q5 : distracteurs de remplissage.** « فصيلة الدم » et « لون البشرة » ne correspondent à aucune
erreur d'élève. Proposition : remplacer `e` par `نسبة الأزوت في الهواء المستنشق` (le cours montre que l'azote
ne participe pas aux échanges : faux, et lié au chapitre) ; `c` et `d` peuvent rester. Le nombre de bonnes
réponses (2) reste non annoncé par l'énoncé.

**[MINOR] m039 Q3 : recouvrement partiel** avec 08/05-tadrib Q1 (la cause « يرتخي الحجاب الحاجز فيرتفع ») ; la
moitié « volume » est neuve et la 2×2 est propre : sans correctif.

## m040 — `08-at-tanaffus/exercices/14-examen-2005-ex4-repos-effort-muscle-coeur-respiration.json`

Étage d3 (`boss` 120/30) ; 7 questions (d2 ×4 puis d3 ×3 : rampe honnête). Comparé à la transcription 2005 ex.4
(le PDF 2005 n'est pas servi : l'URL rend une page HTML).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c (180/70 ≈ 2,6 ; 56/12 ≈ 4,7) | c | OK | 2×2 propre ; étiquette exacte sur `b` (valeurs permutées) |
| 2 | d | d | OK, réserve | clé strictement la plus courte (48 contre 52–58) |
| 3 | b (44,08/2,04 ≈ 21,6) | b | réserve (majeur) | distracteur « 10 » impossible à obtenir : l'oxygène n'est pas dans l'énoncé |
| 4 | a | a | OK | |
| 5 | d | d | réserve (majeur) | clé strictement la plus courte (49 contre 56–60) ; ligne de données brouillée au rendu RTL |
| 6 | c | c | réserve (majeur) | clé imprécise (« طرح الفائض », poumons qui « font » les mouvements) ; la plus courte ; accord fautif en `b` |
| 7 | a → b → c → d → e | idem | OK | ordre unique ; les sept mots imposés du sujet sont présents |

Re-résolution : 7/7 clés justes. Calculs des explications revérifiés (180/70 = 2,57 ; 56/12 = 4,67 ;
44,08/2,04 = 21,6 ; 3000 mL/min = 180 L/h ; 15 → 27 = ×1,8 pour une vitesse ×4).

### Faits signalés : les unités de 2005 normalisées — **conformes**

Chaque grandeur garde l'unité du sujet, déclarée dans l'énoncé qui l'emploie : battements par minute ; litres
de sang par kg et par heure ; mL d'O₂ par kg et par minute (doc. 3) ; g de glucose par kg et par heure ;
mouvements par minute et L d'O₂ par heure (doc. 4). « ملّلتر » → « مل » et « 1كغ » → « 1 كغ » sont des
normalisations d'écriture. Aucune valeur n'est changée ; aucune question ne compare deux grandeurs d'unités
différentes sans conversion (la seule conversion, dans l'explication de Q3, est juste).

### Défauts

**[MAJOR] m040 Q3 : distracteur impossible.** L'option `c` « نحو 10 مرّات » est étiquetée
`bio.lecture.valeur-d-une-autre-grandeur` (« valeur juste d'une autre grandeur »), mais l'énoncé ne donne que le
glucose : l'élève ne peut pas l'obtenir, et l'explication cite des valeurs d'oxygène absentes. Correctif :
remplacer l'énoncé par
`(مناظرة 2005) قيس لدى رياضيّ استهلاك 1 كغ من النّسيج العضليّ للأكسيجين فكان 300 مل في الدقيقة في الراحة و3000 مل في الدقيقة أثناء النشاط، واستهلاكه للجليكوز فكان 2,04 غ في الساعة في الراحة و44,08 غ في الساعة أثناء النشاط.\nكم مرّة تضاعف استهلاك الجليكوز ؟`
Clé inchangée (`b`, 21,6) ; `c` devient la valeur exacte de l'autre grandeur (3000/300 = 10), l'étiquette est
alors exacte ; aucune fuite : les valeurs de repos sont déjà dans l'énoncé de Q4 et Q4 ne demande pas de rapport.

**[MAJOR] m040 : clé la plus courte de façon répétée** (Q2, Q5, Q6 : 3 sur 6 QCM, strictement). Correctifs vérifiés :
- Q2 `d` → `يسرّع القلب نسقه فيصل إلى العضلة النشيطة دم أكثر كلّ ساعة` (57 ; options 58, 52, 54 : ni la plus
  longue ni la plus courte ; reprend l'unité « par heure » du document) ;
- Q5 `d` → `يرتفع الإيقاع مع السرعة، لكنّه لا يتضاعف كلّما تضاعفت السرعة` (60, à égalité avec `a` ; vrai : ×4 pour
  la vitesse, ×1,8 pour le rythme) ;
- Q6 `c` → `تستهلك العضلات أكسيجينًا أكثر فتتسارع الحركات التنفّسيّة كي تجدّد أكسيجين الدم` (78, à égalité avec `a` et
  `d`). Ce texte corrige aussi deux défauts de fond de la clé actuelle : « فتكثّف الرئتان حركاتهما » prête un
  mouvement propre aux poumons, ce que le cours 08 réfute (« الرّئة ليس فيها عضلة ») et que le distracteur `b`
  sanctionne ; « وطرح الفائض » ne dit pas de quoi (l'oxygène « en trop » est une lecture possible).
  Dans l'explication de Q6, remplacer « فتزيد الرئتان من عدد حركات الشّهيق والزّفير لتجدّد الأكسيجين في الدم وتتخلّص من
  الفائض » par `فتتسارع حركات الشّهيق والزّفير لتجدّد الأكسيجين في الدم وتطرح ثنائي أكسيد الكربون الزائد`.

**[MAJOR] m040 Q5 et Q6 : ligne de données brouillée au rendu.** La ligne
« 2 ← 15 ؛ 4 ← 19 ؛ 6 ← 22 ؛ 8 ← 27 » est isolée en un seul bloc LTR par `isolateLtrRuns` ; rendue dans Chromium
`dir=rtl`, elle s'affiche « 8 ← 27؛ 6 ← 22 ؛ 4 ← 19 ؛2 ← 15 » : un lecteur arabe lit d'abord « 15 », puis la flèche,
puis « 2 » — soit l'inverse de l'en-tête « (سرعة المشي … ← الإيقاع …) », qui s'affiche, lui, en RTL. Les couples
vitesse / rythme se lisent à l'envers. Correctif vérifié (rendu Chromium, `isolateLtrRuns`, ordre affiché = ordre
source) : dans Q5 et Q6, remplacer les deux premières lignes de l'énoncé par
`(مناظرة 2005) الوثيقة 4 : رياضيّ يمشي بسرعة متزايدة، وقيس إيقاعه التنفّسي :`
puis quatre lignes `عند 2 كم/س : 15 حركة في الدقيقة` · `عند 4 كم/س : 19 حركة في الدقيقة` ·
`عند 6 كم/س : 22 حركة في الدقيقة` · `عند 8 كم/س : 27 حركة في الدقيقة` (Q6 garde ensuite sa ligne sur l'oxygène).

**[MINOR] m040 Q6 `b` : accord.** « تكثّف الرئتان حركاتها » → `تكثّف الرئتان حركاتهما` (80 caractères ; l'option
reste fausse et plus longue que la clé corrigée d'au plus 2 caractères, sans en être une marque).

Doublons : Q5 et Q6 ne redemandent pas la proportionnalité O₂ / énergie de 08/11 Q7 ; l'équation n'est pas
demandée seule ; Q2 et Q4 sont neuves au chapitre. Aucun défaut de figure (aucune figure).

## m041 — `09-al-ikhraj/exercices/10-examen-2015-ex4-gaz-glucose-arteres-veines-muscle-intestin-rein.json`

Étage annoncé d4 (`challenge` 300/60) ; 8 questions. Données comparées à la transcription 2015 ex.4 et au PDF
2015 : toutes fidèles (15/53, 20/49 mL pour 100 mL ; glucose 1/0,8, 1/2,3, 1/0,8 g/L, deux heures après un repas).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c (artère pulmonaire : plus pauvre en O₂, plus riche en CO₂) | c | OK, réserve | 2×2 propre ; étiquette exacte sur `b` |
| 2 | d (échanges dans les capillaires alvéolaires) | d | réserve (majeur) | doublon de fait avec Q3 |
| 3 | b (le sang s'y enrichit en O₂ et perd du CO₂) | b | réserve (majeur) | doublon de Q2 ; explication qui résout Q1 |
| 4 | a + d + e | a + d + e | réserve (majeur) | une seule écriture juste par organe : le nombre de bonnes réponses (3) se déduit |
| 5 | a | a | OK, réserve (mineur) | l'explication donne le lien O₂–glucose de Q8 |
| 6 | d | d | OK | étiquette exacte sur `b` |
| 7 | c (consommation par les cellules rénales ; le filtré est réabsorbé) | c | OK | clé conforme au cours 09 (réabsorption totale), aucune clé « urine » |
| 8 | a | a | OK, réserve (mineur) | étiquette de `c` approximative |

Re-résolution : 8/8 clés justes. Le rein : la clé de Q7 attribue la baisse à la consommation des cellules
rénales et rappelle que le glucose filtré est réabsorbé en totalité (cours 09, l. 212 et 253) ; aucune option
juste ne dit l'inverse ; le distracteur `a` (« يُطرح … في البول ») exécute le piège du lecteur.

### Faits signalés : les gaz de 2015 (15/53 et 20/49) contre le cours 08 (10/60 et 20/50)

Les valeurs de la mission sont exactement celles du sujet (tableau du 1)) : on les **garde** (le sujet garde ses
données). L'écart ne change aucune clé : le sens est le même (sang de l'artère pulmonaire plus pauvre en O₂ et
plus riche en CO₂). Il n'est pas signalé à l'élève ; un élève qui a appris 10/60 peut croire à une erreur.
**[MINOR]** Correctif : ajouter à la fin de l'explication de Q1
`وقيم هذا الموضوع غير قيم الدّرس (10 و60 ثمّ 20 و50)، لكنّ الاتّجاه نفسه.`
(n'ajoute rien qui résolve une autre question).

### Défauts

**[MAJOR] m041 Q2 ↔ Q3 : doublon interne et fuites croisées.** La clé de Q2 (« يمرّ الدم في شعيرات الأسناخ
فيتبادل الغازين مع هواء الأسناخ ») et celle de Q3 (« الرئتان موضع يغتني فيه الدم بالأكسيجين ويتخلّص من ثنائي أكسيد
الكربون ») disent le même fait ; l'explication de Q2 résout Q3 et inversement. De plus l'explication de Q3
(« يخرج الدم من الرئتين بـ 20 مل … بعد أن دخلها بـ 15 مل ») dit que l'échantillon 1 entre dans les poumons : c'est la
clé de Q1. Correctif : **retirer Q3** (la mission passe à 7 questions ; le sujet 2015 q1-c « استنتج دور الرّئتين »
reste couvert par l'explication de Q2). L'étiquette `bio.resp.appareil-fabrique-l-oxygene` disparaît avec elle.
Résiduel **[MINOR]** inévitable : la clé de Q2 suppose que l'échantillon 2 a traversé les poumons, ce qui oriente
Q1 ; c'est la structure du sujet (1-b présuppose 1-a).

**[MAJOR] m041 Q4 : nombre de bonnes réponses déductible.** Le muscle a une écriture, l'intestin deux
écritures exclusives (`b` / `e`), le rein deux (`c` / `d`) : une seule est juste par organe, donc 3 bonnes
réponses. Correctif : remplacer `c` par
`في المعي الدقيق : يزيد الجليكوز في الوريد على الشّريان بأكثر من 1 غ/ل` (vrai : 2,3 − 1 = 1,3) ;
`correct` devient `["a", "c", "d", "e"]` ; l'intestin porte alors deux écritures justes et une fausse. Explication
de remplacement :
`تُقرأ المقارنة عضوًا عضوًا: في العضلة 0,8 في الوريد مقابل 1 في الشّريان، فالجليكوز ينقص. وفي الكلية الأرقام نفسها (0,8 و1) فهو ينقص أيضًا. وفي المعي الدقيق 2,3 في الوريد مقابل 1 في الشّريان، فهو يزيد بـ 1,3 غ/ل، أي بأكثر من 1 غ/ل. أمّا القول بأنّه ينقص في المعي فلا تسنده القياسات.`

**[MAJOR] m041 : étage sans question d4.** La mission est `difficulty: 4`, `challenge` 300/60, titre ⭐⭐⭐⭐, mais
ses questions vont de d2 à d3 : aucune n'est d4 (R8 : l'étage est celui de la ligne la plus haute). Correctif :
passer Q7 (rein : consommation + réabsorption totale, deux mécanismes à combiner) et Q8 (chasse à l'erreur sur le
sens de la réaction) à `difficulty: 4` — c'est leur difficulté réelle et la rampe devient 2-2-2-3-3-4-4 (après
retrait de Q3) ; sinon, descendre la mission à d3 (`boss` 120/30, ⭐⭐⭐), contre l'assignation.

**[MINOR] m041 Q5 → Q8.** L'explication de Q5 (« أخذته وأكسدته بالأكسيجين لإنتاج الطّاقة ») donne le lien que Q8
fait trouver. Remplacer « أخذته وأكسدته بالأكسيجين لإنتاج الطّاقة التي تحتاجها » par
`أخذته واستعملته في تنفّسها الخلويّ لإنتاج الطّاقة التي تحتاجها`.

**[MINOR] m041 Q8 `c` : étiquette approximative.** « الجليكوز يُصنع … انطلاقًا من الأكسيجين والماء » n'est pas la
réaction de la photosynthèse (CO₂ + eau) que nomme `bio.resp.respiration-photosynthese-confondues` ; c'est un
renversement de la respiration aux réactifs faux. Correctif : rendre `c` muette (l'étiquette reste exacte en Q6,
où les cellules « fabriquent le glucose à partir du CO₂ et de l'eau »).

**[MINOR] m041 Q5–Q7 → Q4.** Les énoncés de Q5, Q6 et Q7 disent « انخفاض » / « ارتفاع » pour chaque organe, ce qui
donne les comparaisons de Q4 si le donjon les tire avant. Q4 contient ses propres valeurs et n'est qu'une
lecture : aucune correction exigée, mais à garder en tête si Q4 est enrichie.

## m042 — `09-al-ikhraj/exercices/11-examens-2010-ex4-2008-ex3-liquides-renaux-fonctions-nephron.json`

Étage d3 (`boss` 120/30) ; 9 questions (d2 ×7 puis d3 ×2 : rampe honnête). Comparé aux transcriptions 2010 ex.4,
2008 ex.3, 2019 ex.1 item 4, 2012 ex.1 item 4, 2013 ex.1 item 7, et aux PDF 2010 et 2019.

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2010 | 1 veine cave inf., 2 artère rénale, 3 veine rénale, 4 uretère | idem | OK | figure univoque (2 part de l'aorte A, 3 de la veine cave) |
| 2 | 2010 | c (échantillon 2) | c | OK | données fidèles (70/0/70 ; 0,03/0,6/0,1 g/L) |
| 3 | 2008 | a | a | OK | 2×2 propre |
| 4 | 2019 | d (flèche 2) | d | OK | figure fidèle ; étiquettes exactes sur `a` et `c` |
| 5 | 2012 | c (urée) | c | OK | étiquette exacte sur `a` |
| 6 | 2013 | a (tube urinaire) | a | OK | étiquettes exactes sur `b`, `c` ; « الحويض » enseigné (cours 09 l. 65) |
| 7 | 2008 | b | b | réserve (majeur) | étiquette sur l'option à deux erreurs `d`, absente de `c` (une erreur) |
| 8 | 2010 | d (artère = ع, 0,1 ; veine = س, 0,03) | d | réserve (majeur) | deux options incohérentes, éliminées à vue |
| 9 | 2010 | b | b | OK, réserve (mineur) | conforme au cours 09 (« إخراج … الحمض البوليّ ») ; simplification de niveau |

Re-résolution : 9/9 clés justes. L'acide urique n'est jamais dit « sécrété » : la clé de Q9 dit « يُخرَج … ولا
يُعاد امتصاصه », conforme au cours 09 (fonction 4, « إخراج »). Aucun item écarté (2006 n°2, 2013 n°6, 2018 n°3,
2015 n°4, 2010 n°1, 2005 n°8) n'est devenu une question.

### Faits signalés : les vaisseaux rénaux de 2010 renumérotés — **acceptable**

Le sujet numérote six repères sur un schéma de la circulation entière (1–3 au poumon, 4 un gros vaisseau
descendant, 5 et 6 deux vaisseaux qui entrent dans chacun des reins). La mission ne garde qu'un rein et
renumérote 1–4 (veine cave, artère rénale, veine rénale, uretère), avec l'aorte nommée « A ». Aucune question ne
renvoie aux numéros du sujet (Q2 et Q8 nomment les vaisseaux en toutes lettres) : la renumérotation ne crée ni
ambiguïté ni infidélité de donnée. À déclarer dans le rapport d'auteur, pas dans l'énoncé.

### Défauts

**[MAJOR] m042 Q8 : deux options s'éliminent à vue.** La 2×2 croise l'attribution (س ou ع à l'artère) et la
raison (« تضيف » / « تخلّص »). Or `b` (artère ع à 0,1, veine س à 0,03, « le rein ajoute de l’acide urique ») et `c`
(artère س, veine ع, « le rein en débarrasse le sang ») se contredisent elles-mêmes : il reste `a` contre `d`.
Correctif (clé inchangée `d`, quatre options cohérentes, attribution à 2 contre 2, raisons toutes distinctes) :
- `a` inchangée : `الشريان : العيّنة س ، والوريد : العيّنة ع ، لأنّ الكلية تضيف الحمض البولي إلى الدم` (82) ;
- `b` → `الشريان : العيّنة س ، والوريد : العيّنة ع ، لأنّ الدم يفقد ماءه في الكلية فيتركّز حمضه البولي` (93) ;
- `c` → `الشريان : العيّنة ع ، والوريد : العيّنة س ، لأنّ خلايا الكلية تستهلك الحمض البولي غذاءً` (87) ;
- `d` inchangée (clé) : `الشريان : العيّنة ع ، والوريد : العيّنة س ، لأنّ الكلية تخلّص الدم من الحمض البولي` (82,
  à égalité avec `a` : ni la plus longue ni strictement la plus courte).
`c` donne la bonne attribution avec une fausse raison (le piège « consommation » de m041 Q7 appliqué à un déchet) ;
`b` la mauvaise attribution avec une raison qui serait juste pour l'urine. Ajouter à l'explication :
`ولا تستهلك خلايا الكلية الحمض البوليّ، فهو فضلة لا غذاء، والدم لا يتركّز في الكلية بل البول.`
Aucune fuite : Q9 dit seulement que l'urine est six fois plus concentrée que le sang artériel, sans valeur.

**[MAJOR] m042 Q7 : étiquettes.** `bio.excr.etape-du-nephron-confondue` est sur `a` (une erreur : ammoniac
« filtré », exact) et sur `d` (deux erreurs : urée « sécrétée » ET ammoniac « filtré ») ; `c` (une erreur : urée
« sécrétée ») n'en a pas. Correctif : retirer l'étiquette de `d` (option à deux erreurs, muette) et la poser sur
`c`.

**[MINOR] m042 Q9 : niveau de simplification.** « لا يُعاد امتصاصه » est la thèse du cours 09 (« إخراج مواد سامّة
كالبولة والحمض البوليّ ») ; en physiologie réelle l'acide urique est en partie réabsorbé. La clé est juste au niveau
du manuel ; aucune correction de l'item, mais ne pas réemployer `c` comme distracteur hors de ce cadre.

## m043 — `09-al-ikhraj/exercices/12-examens-2005-ex2-2007-ex1-2001-ex3-unites-structurales-fonctionnelles.json`

Étage d2 (`practice` 75/15) ; 7 questions, toutes d2. Comparé aux transcriptions 2005 ex.2, 2007 ex.1, 2001 ex.3
(PDF 2005 non servi). Figure commune à Q1–Q3 : fidèle au document 1 de 2005 (sac à paroi cellulaire avec les
flèches « خروج دم غني بـ 1 » / « دخول دم غني بـ 2 », neurone étoilé à prolongement unique, néphron en peloton) ;
lisible à 232 px.

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2005 | A alvéole, B neurone, C néphron | idem | OK | |
| 2 | 2005 | 1 O₂, 2 CO₂, 3 axone, 4 dendrites | idem | réserve (majeur) | l'énoncé nomme « السنخ » : clé de Q1 ; moitié « neurone » = 01/07 Q1 (L11) |
| 3 | 2005 | A respiration, B influx, C urine | idem | OK | |
| 4 | 2007 | a + b + c | a + b + c | réserve (majeur) | une option par organe, toutes justes ; `d`, `e` inverses du cours : 3 se déduit |
| 5 | 2007 | c (absorption, cavité → sang) | c | OK | 2×2 propre ; étiquette exacte sur `d` |
| 6 | 2007 | d (déchets toxiques, constance) | d | OK | 2×2 propre |
| 7 | 2001 | excrétion ↔ rein : néphron ; influx ↔ moelle : neurone ; gaz ↔ poumon : alvéole | idem | réserve (majeur) | mêmes trois couples unité ↔ fonction que Q3 |

Re-résolution : 7/7 clés justes. « قرابة المليون » néphrons par rein et « 700 مليون » alvéoles : cours 09 l. 111 et
cours 08 l. 177. « المحور », « التغصّنات » : cours 01.

### Défauts

**[MAJOR] m043 Q2 → Q1 : l'énoncé donne la clé.** « السّهم 1 يمثّل خروج دم غنيّ بغاز من السنخ » nomme l'unité A,
que Q1 fait reconnaître. Remplacer par
`السّهم 1 يمثّل خروج دم غنيّ بغاز من جدار الوحدة A، والسّهم 2 يمثّل دخول دم غنيّ بغاز آخر إليه.`
et, dans l'explication, « الدم الذي يخرج من السنخ » → `الدم الذي يخرج من جدار الوحدة A` et « يدخل جدار السنخ » →
`يدخل جدارها`. Résiduel inévitable (**[MINOR]**) : les options « المحور » / « التغصّنات » désignent un neurone.

**[MAJOR] m043 Q7 ↔ Q3 : doublon interne.** Q3 apparie dessin ↔ « fonction : système », Q7 apparie fonction ↔
« organe : unité » ; ce sont les mêmes trois couples unité ↔ fonction (alvéole / échanges gazeux, neurone /
influx, néphron / urine), et chacune résout l'autre dès que Q1 est faite. Le plan demandait que chaque question
parte d'un dessin ou d'une fonction ; Q7 part bien d'une fonction mais n'ajoute que l'organe. Correctif : **retirer
Q7** (la mission passe à 6 questions, au plancher de R5) ; le titre devient
`🏛️ مناظرتا 2005 و2007 · الوحدات التّركيبيّة والوظيفيّة ⭐⭐` et la ligne de registre de la mission perd la source
2001 ex.3. À défaut (si l'orchestrateur veut garder 2001), réduire Q3 au seul appariement dessin ↔ système, ce
qui laisse à Q7 la fonction : mais Q3 devient alors une conséquence directe de Q1 ; le retrait est préférable.

**[MAJOR] m043 Q4 : nombre de bonnes réponses déductible.** Chaque organe a une option (`a` poumon, `b` intestin,
`c` rein), toutes justes ; `d` et `e` sont les contraires mot pour mot de la triade du cours (« رقّة الجدار »,
« شبكة كثيفة من الشعيرات ») : on élimine à vue et on compte 3. Correctif : remplacer `e` par
`سعة المثانة التي يتجمّع فيها البول` (fausse : la vessie stocke, elle n'échange pas ; cours 09 l. 67, « خزن
مؤقّت ») ; le système urinaire porte alors une option juste et une fausse, le décompte ne se lit plus par organe.
`correct` inchangé (`a`, `b`, `c`). Explication : remplacer la dernière phrase par
`أمّا غلظ الجدار فيعيق التبادل لأنّ الجدار الفاصل يكون رقيقًا، والمثانة تخزن البول مؤقّتًا ولا يتمّ فيها أيّ تبادل مع الدم.`

**[MINOR] m043 Q2 ↔ 01/07 Q1 (L11, même vague) : recouvrement.** La moitié « neurone » (المحور, التغصّنات sur un
dessin) est demandée par 01/07 Q1. Elle reste ici parce que le sujet 2005 l'impose (repères 3–4) et qu'elle est
mêlée aux gaz : à garder, mais l'orchestrateur doit savoir que les deux lots posent ce couple.

## Transversal

### Étiquettes

Toutes les étiquettes employées existent sur `origin/main:content/misconceptions.json` (le `misconceptions.json` de
la branche a 43 lignes de retard sur `main` : à rebaser avant la PR, sans effet sur ce lot). Libellés relus un à
un ; écarts : m039 Q2 (à déplacer de `a` vers `b`), m042 Q7 (de `d`, deux erreurs, vers `c`), m041 Q8 `c` (à rendre
muette). Les autres nomment exactement l'erreur exécutée.

**Les deux familles proposées par l'auteur.** Je n'ouvre pas les notes d'auteur (consigne) ; je juge sur les
distracteurs non étiquetés du lot, où deux erreurs reviennent, et qui correspondent aux pièges du lecteur :
1. « un organe s'accélère de lui-même, sans lien avec la demande du muscle » : m040 Q2 `b` (le cœur), m040 Q6 `b`
   (les poumons) et `d` — **2 questions distinctes** ;
2. « ce que perd le sang du rein part dans l'urine / le rein élimine le glucose » : m041 Q7 `a`, m042 Q3 `c` et `d`
   — **2 questions distinctes**.
Aucune n'atteint 3 questions distinctes dans le lot : **pas de création** sur ce seul lot. La famille 2 recouvre en
partie `bio.excr.etape-du-nephron-confondue` (pour m042 Q3 `c`/`d`, qui disent « يُرشَّح ثمّ يُخرَج في البول » :
c'est la réabsorption ignorée, donc une étape oubliée) ; la famille 1 n'a pas d'équivalent au registre. Si l'auteur
en montre une troisième occurrence ailleurs (patron 07 ou 08), la famille 1 est la plus défendable ; son libellé
devra nommer l'erreur exacte (« تظنّ أنّ القلب أو الرّئتين تسرّع نشاطها من تلقاء نفسها: إنّما يتبع تسارعها حاجة العضلات
إلى الأكسيجين والجليكوز »). Si les familles proposées sont autres, l'orchestrateur me les renvoie.

### Doublons

- Internes : m038 Q1 ↔ Q8, m041 Q2 ↔ Q3, m043 Q3 ↔ Q7 (majeurs, ci-dessus).
- Vers le publié : m038 Q2 ↔ 08/02-tamrin Q6 (corrigé par le texte de clé), m039 Q6 ↔ quiz 08 Q1 (résiduel
  mineur), m039 Q3 ↔ 08/05-tadrib Q1 (moitié), m038 Q6 ↔ chapitre 06, m038 Q7 ↔ 07/02-tamrin Q5 (moitié).
- Vers la vague 2, autres lots : m043 Q2 ↔ 01/07 Q1 (L11).
- Entre missions du lot : aucun gabarit commun (`content:tranche` : 0 groupe gabarit, une paire proche hors lot :
  quiz 08 #4 ↔ 08/02-tamrin #5). Les données 2005 ex.4 (m040) et 2010 ex.4 q4 ne sont posées qu'une fois.

### Gates et rendu

`content:check` vert (0 erreur) ; `content:qa:strict` : 0 erreur, aucun avertissement sur les six fichiers ;
`content:tranche --chapters 08,09` : clé strictement la plus longue 0/165. Toutes les chaînes chiffrées du lot
passées dans `isolateLtrRuns` et rendues dans Chromium `dir=rtl` : un seul brouillage (m040 Q5–Q6, corrigé
ci-dessus). Figures rendues à 232 px : deux défauts (m039 cloche, m038 Q5 flèche 2), corrigés ci-dessus.

### Divers

- `sources[]` des `chapter.json` 08 et 09 : la ligne « Sujets officiels de l'examen national … transcriptions :
  programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/ » est déjà présente (vague 1) et couvre
  les sessions du lot : OK.
- Étages : m038 Q10 d3 dans une d2 (mineur), m041 d4 sans question d4 (majeur) ; m039, m040, m042, m043 honnêtes.
- Titres : conformes au patron (« مناظرة / مناظرتا / مناظرات », étoiles de l'étage) ; m038 à reprendre (mineur) ;
  m043 à reprendre si Q7 est retirée.
- Notions : rien hors du chapitre ou d'un chapitre antérieur, sauf « النّيفرونات » en distracteur de m038 Q8
  (option d'origine du sujet 2010, notion du 09) — sans objet si Q8 est retirée.

## Bilan

| mission | questions | clés fausses | majeurs | mineurs |
| --- | ---: | ---: | ---: | ---: |
| m038 (08/12) | 10 | 0 | 3 | 6 |
| m039 (08/13) | 6 | 0 | 3 | 3 |
| m040 (08/14) | 7 | 0 | 4 | 1 |
| m041 (09/10) | 8 | 0 | 3 | 4 |
| m042 (09/11) | 9 | 0 | 2 | 1 |
| m043 (09/12) | 7 | 0 | 3 | 2 |
| **total** | **47** | **0** | **18** | **17** |

Questions à reprendre (texte, figure, étiquette ou retrait) : m038 Q2, Q3, Q4, Q5, Q8 (retrait), Q10 et le titre ;
m039 Q1, Q2, Q3, Q4, Q5, Q6 ; m040 Q2, Q3, Q5, Q6 ; m041 Q1, Q3 (retrait), Q4, Q5, Q7, Q8 ; m042 Q7, Q8 ;
m043 Q2, Q4, Q7 (retrait) et le titre — **26 questions** (dont 3 retraits) sur 47.

**Verdict : à corriger avant publication** (aucune clé fausse ; 18 majeurs, tous avec texte de remplacement
vérifié). Après retraits : m038 9 questions, m041 7, m043 6 (au plancher).

