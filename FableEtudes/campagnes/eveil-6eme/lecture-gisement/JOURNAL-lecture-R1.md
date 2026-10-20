# Journal du lecteur R1 — éveil scientifique 6ᵉ, concours C01 (2026) à C09 (2018)

Étape G2 (étude 36). Lecture du 2026-10-20. Les neuf PDF (`/tmp/claude-0/ev6g/src/<année>-svt.pdf`) sont des scans sans couche
texte (`pdftotext` rend 2 à 4 octets) : lecture en vision, 150 DPI (200 pour 2018, texte plus petit), une fois par page, zooms
ponctuels sur les tableaux et figures denses. Les neuf sha256 des copies locales égalent ceux de `docs.json`, du registre
`gisement.json` et des en-têtes des transcriptions. Aucune écriture git, rien sous `content/eveil-scientifique-6eme/`,
`gisement.json` intact. Fiche programme lue telle quelle (bornes ✅/◐/⛔ du 2026-10-20), non modifiée.

## 0. CONVENTIONS FIXÉES (à reprendre par les lecteurs C10–C19)

Reprises de l'anglais 6ᵉ et de la SVT 9ᵉ : n°exo `\d+[a-z]?` ; créneau `concours` ; compétences `-` ; barème décimal toléré (`1.5`) ;
étages `d1` à `d4` ; `HP:` jamais seul, jetons kebab après les slugs, slugs dans l'ordre du manifeste.

**Grain des lignes** : une ligne par **question notée** (une `التعليمة`, sous-lettres `أ`/`ب`/`ج` comprises, chacune notée à part).
Le **n°exo est le rang d'ordre dans le document** (1, 2, 3 …), PAS le numéro imprimé : les numéros imprimés recommencent à 1 dans
chaque situation (`الوضعيّة` / `السّند`), ils se retrouvent donc dans la table de correspondance de chaque §. Une question qui
porte plusieurs consignes courtes (deux énoncés à corriger, trois cases) reste UNE ligne tant qu'elle n'a qu'une `التعليمة` et un
seul barème imprimé ; si le barème est imprimé par sous-question (`2-1`, `2-2`, `3-1-أ`…), une ligne par sous-question.

**Barème** : le total imprimé de la question ; `-` quand le sujet n'en imprime pas (2024, 2023, 2019, 2018 : seules des cases de
notation en marge, « مع N » = critère 1, 2 ou 3 ; je n'ai pas déduit de points de leur nombre). Quand une question porte deux
barèmes partiels (« 0,5 » puis « 0,75 »), ligne = leur somme (C01 n°10 : 1.25).

**Format de l'épreuve** : une heure (9 h 30–10 h 30 en 2018 et 2019 ; « ساعة » ensuite), coefficient 1, 20 points, **quatre pages**
(deux grandes pages en 2018), trois blocs : **الوضعيّة الأولى (ou عدد 1) + الثانية (عدد 2) + الإدماجيّة** (2018 : quatre supports
numérotés sans titres de situation). Quasi aucun texte à lire : chaque situation est une mise en scène de 2–4 lignes (la
famille, un club, un voyage) suivie de consignes de type **« أصلح كلّ خطأ ورد في الإفادة »**, **« أعلّل / أفسّر »**, **« أكتب
صواب/خطأ »**, **« أربط بسهم »**, **« أكمل الجدول »**, **« أصنّف »**. Marge de notation « مع 1 / 2 / 3 » à chaque consigne.

**Transcription** (`examens-nationaux/6eme-base/eveil/<année>-unique.md`) : en-tête YAML de l'anglais 6ᵉ (`examen` = intitulé du registre
suivi de l'intitulé arabe, `filiere: unique`, `consulte_le: 2026-10-20`, `lecture: vision`). **Les supports (`السّند`) sont
résumés** (neutre, 2–3 lignes, citation seulement quand une question la reprend), **consignes, énoncés à corriger ou à
classer, données de tableaux et diagrammes, barèmes sont mot pour mot**. Les figures sont décrites entre crochets avec toutes
leurs données et légendes imprimées. La case de marge « مع N » est notée entre crochets devant la consigne.

**Placement** : le chapitre de la notion testée, avec la table de la fiche §4 bis ; air et combustion → `01-air` (échange pulmonaire
→ `02-respiration`) ; sang, vaisseaux, trajet → `03` ; maladies de malnutrition, vitamines, groupes d'aliments → `04` ;
chaîne alimentaire, pollution de l'eau, maladies hydriques (typhoïde, choléra, jaunisse) → `05` ; boussole, aimants,
directions → `07` ; poids → `08` ; œil → `09` ; vaccination, microbes → `10` ; effets du courant, électrolyse → `11`.

**Jetons HP fixés** (un jeton par notion absente des bornes ✅ de la fiche ; l'item reste dans le plan, c'est à l'orchestrateur de
trancher) :
- `HP:plaquettes` : les صفيحات (4ᵉ composant, ◐ de la fiche : « manuel et جذاذات n'en ont que trois ») ;
- `HP:sang-decante` : الدّم المترسّب (sang laissé à décanter, ◐ du ملفّ) ;
- `HP:huit-directions` : directions intermédiaires (nord-est, sud-ouest…) ; le manuel a quatre directions, la rose à huit est ◐ (ملفّ p.176) ;
- `HP:fer`, `HP:moelle-osseuse`, `HP:cecite-nocturne` (vitamine A), `HP:analyses-sanguines` (tableau chiffré de vitamines, ◐),
  `HP:proportion-plasma` (55 %), `HP:pourcentage-azote` (78 %, ◐), `HP:arteriosclerose`, `HP:potabilisation` (chaîne de
  potabilisation, ◐ « extension »), `HP:pesticides`, `HP:nutrition-vegetale` (plante qui fabrique son aliment : absent des deux
  sources), `HP:condensation` (condensation de la vapeur : absente des bornes).
- **Non HP** (à tort ou à raison, à arbitrer) : l'électrolyse de l'eau (✅ du manuel p.122–125), la combustion incomplète et
  le monoxyde (guide, corrigé d'évaluation), le trajet cœur-poumons-cœur (✅ « trajet … en schéma »), « consommateur de
  troisième ordre » (✅), le litre d'air ≈ 1,3 g (✅), le quart de l'azote par rapport à l'oxygène (dérivé du 1/5, non nommé).

**Étages** : `d1` choix, vrai/faux, mot à relever, correction d'un seul mot ; `d2` correction à deux erreurs, justification,
classement, tableau à compléter ; `d3` lecture de schéma à orientation inhabituelle, expérience à interpréter en trois temps,
tableau d'expériences à concevoir ; aucun `d4`.

## 1. Documents lus

| id | session | sha256 (= registre ?) | pages | lecture | lignes | dont HP | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 2026 | 2dea1b5360589428ae038e50539f33a69db1e1e7469ff28c620b1fcb27288244 (oui) | 4 | vision | 15 | 3 | `eveil/2026-unique.md` |
| C02 | 2025 | 374b069e5161c4d3a07c5321e1359a3faac8eb145564d54b57fc06878b2b375b (oui) | 4 | vision | 15 | 4 | `eveil/2025-unique.md` |
| C03 | 2024 | d286918b7b8b26e01f7416cb9664ff73558c6067a37b0f572893eebd426beef2 (oui) | 4 | vision | 15 | 3 | `eveil/2024-unique.md` |
| C04 | 2023 | 035bf4388123805a6197bcdd5ac5d2a078cc93e76559aa2d89fb9f4e3cea6616 (oui) | 4 | vision | 18 | 3 | `eveil/2023-unique.md` |
| C05 | 2022 | 3f47f0811678761c92eb34baea040df77616648937d61e29f22b2d48809df5a2 (oui) | 4 | vision | 15 | 3 | `eveil/2022-unique.md` |
| C06 | 2021 | 47ba2754ee6cfcd44e6b6bc353323a8612ff7cc07b9dd88d3517767b08dbf499 (oui) | 4 | vision | 14 | 4 | `eveil/2021-unique.md` |
| C07 | 2020 | c2190a70e1b572c4a121b2dd6eb5a25356e0d5354cb7efe4bd26ea1d2506892b (oui) | 4 | vision | 12 | 3 | `eveil/2020-unique.md` |
| C08 | 2019 | 1b8bcc58f75171fe64c69ef9607fdb720d4f3024a557e5c8a2f6ea6b0466b363 (oui) | 4 | vision | 16 | 2 | `eveil/2019-unique.md` |
| C09 | 2018 | 43103c616375263c72c0574e450a6f4b75cebcae65d05a9bdc5332c37f8cb2ba (oui) | 2 | vision | 12 | 0 | `eveil/2018-unique.md` |

Total : **132 lignes** (25 portent au moins un jeton `HP:`), 9 `.meta`, 9 transcriptions. Validation : 132 valides, 0 fautive.

## C01 — 2026 (4 pages, bonne lisibilité)

- **Format** : 3 situations, 20 points : 1ʳᵉ 5 (feu de brûleur + aimant brisé), 2ᵉ 6,25 (analyse de sang, typhoïde), intégrative 8,75
  (désert : chaîne, respiration, repas, boussole).
- **Correspondance** : rang → imprimé : 1 = S1 A1 ت1 ; 2 = ت2 ; 3 = ت3-أ ; 4 = ت3-ب ; 5 = S2 ت1-أ ; 6 = ت1-ب ; 7 = ت2 ; 8 = ت3 ;
  9 = int. S1 ت1 ; 10 = S2 ت2-1 ; 11 = ت2-2 ; 12 = ت2-3 ; 13 = S3 ت3-1-أ ; 14 = ت3-1-ب ; 15 = ت3-2.
- **Notions** : `01-air` (combustion, flamme) 1–2, 11 ; `07` 3, 4, 13–15 ; `03` 5, 6, 8 ; `10`+`05` 7 ; `05` 9 ; `02` 10 ; `04` 12.
- **HP** : plaquettes nommées dans l'énoncé (5, 6) ; directions intermédiaires (13).
- **Difficultés** : 1ʳᵉ affirmation de ت1 (suie en flamme bleue) rejoint l'erreur du manuel signalée par la fiche ; la chaîne
  (n°9) demande cinq maillons alors que quatre animaux sont photographiés, le producteur est à inventer ; la rose de la boussole
  place le nord (ش) à droite de la page ; barème partiel `(0,5)(0,75)` en n°10 ; l'ordre de grandeur de la 2ᵉ situation (6,25) est le
  plus élevé du lot.

## C02 — 2025 (4 pages, bonne lisibilité)

- **Format** : 3 situations : 1ʳᵉ 4,25 (deux bocaux, bougie, refroidissement), 2ᵉ 5,25 (don du sang, circulation), intégrative 10,5
  (figuier de Barbarie, cochenille, aimants, boussole artisanale).
- **Correspondance** : 1 = S1 ت1 ; 2 = ت2-أ ; 3 = ت2-ب ; 4 = ت3 ; 5 = S2 ت1-أ ; 6 = ت1-ب ; 7 = ت2 ; 8 = ت3 ; 9 = int. ت1-أ ; 10 = ت1-ب ;
  11 = S2 ت ; 12 = S3 ت ; 13 = S4 ت4-1 ; 14 = ت4-2 ; 15 = S5 ت.
- **Notions** : `01-air` 1–4 ; `03`+`02` 5–7 ; `03` 8, 12 ; `05` 9–11 ; `04` 10 ; `07` 13–15.
- **HP** : moelle-osseuse (8), nutrition-vegetale (10), pesticides (11), plaquettes + sang-decante (12).
- **Difficultés** : la mesure du cinquième d'oxygène par l'eau montée après extinction d'une bougie (n°3) est la mesure que la fiche
  signale comme erreur du manuel ; « هباب الفحم » comme produit de la bougie (n°4) : clé à arbitrer ; une valeur de volume (100)
  est imprimée à l'énoncé ; la chaîne de cinq maillons (n°9) mélange quatre photos et un maillon donné par le texte (la cochenille) ;
  le n°15 (boussole artisanale) donne trois montages dont un à support de fer, à trancher puis à justifier (3 points, deux critères).

## C03 — 2024 (4 pages, bonne lisibilité) — **aucun barème imprimé**

- **Format** : 3 situations, 20 points non ventilés : 1ʳᵉ (pizza, plaie : repas équilibré, sang, fer), 2ᵉ (aimants, bougie dans un tube
  gradué), intégrative (protection civile, forêt : combustion, boussole, chaîne, pollution, typhoïde).
- **Correspondance** : 1 = S1 ت ; 2 = S2 ت2-1-أ ; 3 = ت2-1-ب ; 4 = ت2-2 ; 5 = S2 ت1 ; 6 = ت2 ; 7 = ت3-أ ; 8 = ت3-ب ; 9 = int. S1 ت ;
  10 = S2 ت2-1 ; 11 = ت2-2 ; 12 = S3 ت3-1-أ ; 13 = ت3-1-ب ; 14 = ت3-2 ; 15 = ت3-3.
- **Notions** : `04` 1, 4 ; `03`/`02` 2, 3 ; `07` 5, 6, 10, 11 ; `01-air` 7–9 ; `05` 12–15.
- **HP** : fer (4), sang-decante (2 : plasma « 55 % du sang décanté »), potabilisation (15).
- **Difficultés** : la relation de la chaîne est « غذاء لـ » (flèche de l'aliment vers le mangeur), l'inverse de « يتغذّى على » en 2025/2026 :
  sens des flèches à normaliser avant reprise ; le plan de la 3ᵉ situation de l'intégrative (n°10, 11) suppose de réorienter la boussole : le sud est donné vers la droite de la page ;
  « الهزال الرزي » (faute d'impression reprise du guide, cf. fiche §6) ; question sur le niveau de l'eau où la bougie s'éteint :
  même mesure d'oxygène que l'erreur du manuel.

## C04 — 2023 (4 pages, bonne lisibilité) — **aucun barème imprimé**

- **Format** : 3 situations : 1 (effort, circulation, repas équilibré, vitamine), 2 (voyage : buée, pompe, boussole), intégrative (ferme :
  chaîne, typhoïde, anémie, air, brûleur) ; **18 lignes**, la plus riche du lot.
- **Correspondance** : 1–3 = S1 ت1-أ, ب, ج ; 4–6 = ت2-أ, ب, ج ; 7–8 = S2 ت1-أ, ب ; 9 = ت2 ; 10–11 = ت3-أ, ب ; 12–13 = int. ت1-أ, ب ;
  14 = ت2 ; 15 = ت3 ; 16–17 = ت4-أ, ب ; 18 = ت5.
- **Notions** : `03`/`02` 1–3 ; `04` 4–6 ; `01-air` 7–9, 16–18 ; `07` 10, 11 ; `05` 12–14.
- **HP** : cecite-nocturne (6), condensation (8), arteriosclerose (15).
- **Difficultés** : la chaîne imprimée (n°12) contient plusieurs erreurs imbriquées (sens des flèches, ordre, intrus) : barème de 3 critères
  à une seule case ; 4-أ demande « un quart de l'azote » (dérivé du 1/5, valeur non donnée) ; 4-ب « décris une expérience »
  attend la bougie sous cloche (mesure du cinquième d'oxygène erronée au manuel) ; le brûleur du n°18 a une légende « ضابط هواء ».

## C05 — 2022 (4 pages, bonne lisibilité) — barèmes imprimés

- **Format** : 3 situations : 5 (prise de sang, circulation) + 4,5 (club : air, aimants) + 10,5 (sebkha : pollution, boussole, repas,
  combustion). **L'en-tête ministériel est en haut de la page 4/4** (feuille recto-verso, première page sans en-tête).
- **Correspondance** : 1 = S1 ت1 ; 2 = ت2-أ ; 3 = ت2-ب ; 4 = ت3 ; 5 = S2 ت ; 6 = ت2-1 ; 7 = ت2-2 ; 8 = int. ت1-1 ; 9 = ت1-2 ; 10 = S2 ت2-1 ;
  11 = ت2-2 ; 12 = S3 ت3-1-أ ; 13 = ت3-1-ب ; 14 = ت3-2-أ ; 15 = ت3-2-ب.
- **HP** : sang-decante (3), huit-directions (10), fer (13).
- **Difficultés** : la rose de la boussole a huit flèches avec « شمال » à gauche ; 2-1 (clous) dessine l'aimant en U avec un dessin
  à compléter, la correction est un dessin ; 1-2 « consommateur de troisième ordre » à partir de trois images (flamant, zooplancton, huître).

## C06 — 2021 (4 pages, bonne lisibilité) — barèmes imprimés

- **Format** : 3 situations : 4 (analyses d'une personne âgée) + 5,5 (sortie en voiture : boussole, buée) + 10,5 (journée de
  l'environnement : air, vaisseaux, décomposeurs, pôles).
- **Correspondance** : 1–3 = S1 ت1–3 ; 4–6 = S2 ت1–3 ; 7–8 = int. ت1-أ, ب ; 9–10 = ت2-أ, ب ; 11 = ت3 ; 12 = S2 ت1 ; 13 = ت2 ; 14 = ت3.
- **HP** : analyses-sanguines (1), plaquettes (2), huit-directions (4, 5), condensation (5).
- **Difficultés** : tableau de résultats chiffré (vitamines B12, D, B1 en ng/L, plaquettes) : le bilan est hors fiche, seule la vitamine D / le
  rachitisme (✅ maladies de malnutrition) est dans les bornes ; la cible de la flèche inférieure gauche du tableau du frottis est ambiguë
  (fond clair, pas un élément) ; mesure du litre d'air (n°11) conforme au manuel (1,3 g) ; 5 donne « تكثّف CO₂ » à corriger.

## C07 — 2020 (4 pages, bonne lisibilité) — barèmes imprimés

- **Format** : 3 situations : 5 (grossesse : sang, fer, vitamine A, trajet) + 4,75 (bougie, combustion, litre d'air) + 10,25 (air, tube
  gradué, alvéole, aliments). Rédigée sans titre de partie entre S2 et int.
- **Correspondance** : 1 = S1 ت ; 2–3 = ت1, ت2 ; 4–6 = S2 ت1–3 ; 7–9 = int. ت1–3 ; 10 = ت4 ; 11 = ت5 ; 12 = ت6.
- **HP** : moelle-osseuse + proportion-plasma (1), fer + cecite-nocturne (2), pourcentage-azote (7).
- **Difficultés** : 78 % et « 80 % » à corriger : la fiche ne retient que le cinquième d'oxygène ; trajet du sang des poumons au cœur
  avec la chaîne `الأوردة الرئوية ← البطين الأيسر ← الأذينة اليمنى ← الشريان الأبهر` (anatomie cardiaque de 5ᵉ, ⛔ de la fiche reprise
  de façon fonctionnelle) ; 5 classe cinq aliments en quatre colonnes (le persil comme source de sels minéraux est ◐ de la fiche).

## C08 — 2019 (4 pages, bonne lisibilité) — **aucun barème imprimé**

- **Format** : 3 situations ; épreuve de 9 h 30 à 10 h 30 ; 20 points non ventilés ; 16 lignes. La 2ᵉ situation commence en bas de la page 1 et se poursuit page 2.
- **Correspondance** : 1 = S1 ت1 ; 2 = ت2 ; 3 = S2 ت ; 4 = S2' ت ; 5 = ت1-أ ; 6 = ت1-ب ; 7 = ت2 ; 8 = int. ت1 ; 9 = ت2 ; 10 = S2 ت1-أ ;
  11 = ت1-ب ; 12 = S3 ت1 ; 13 = ت2-أ ; 14 = ت2-ب ; 15 = ت2-ج ; 16 = ت3.
- **HP** : plaquettes (1), huit-directions (4).
- **Difficultés** : le plan du scout met le nord (ش) à gauche de la boussole et demande le « sud-ouest » ; le n°12 propose des symptômes
  à choisir parmi quatre dont « فشل عضلي » ; les barèmes sont absents, la marge ne donne que le critère.

## C09 — 2018 (2 grandes pages, bonne lisibilité) — **aucun barème imprimé**

- **Format** : sans titres de situations ; 4 supports `(1)` à `(4)` ; 12 lignes ; seule session du lot qui touche l'électricité.
- **Correspondance** : 1–3 = S1 ت1–3 ; 4–5 = S2 ت1, ت2 ; 6–10 = S3 ت1–5 ; 11–12 = S4 ت1–2.
- **HP** : aucun jeton (l'électrolyse de l'eau et le test de l'hydrogène sont ✅ du manuel p.122–125).
- **Difficultés** : la lentille correctrice du défaut de vision rejoint l'erreur du manuel (lentille concave pour l'hypermétropie) que la
  fiche signale ; le titre de l'exercice sur la chute d'un fruit confond masse et poids (`الكتلة`) : clé à arbitrer avec la fiche ;
  `طول النظر` = hypermétropie (ambigu pour un élève qui connaît la myopie).

## 2. Bilan

- **Lignes** : 132 (15 + 15 + 15 + 18 + 15 + 14 + 12 + 16 + 12), 25 avec jeton `HP:`, soit 19 %. **« Programme ancien »** : aucune
  session ne l'est entièrement ; 2018–2020 touchent l'électricité et des pourcentages chiffrés (2020) que la fiche classe ◐.
- **Répartition des chapitres** (n° de lignes où le slug figure) : `01-air` 35, `07-aimants-boussole` 26, `03-sang-circulation` 23,
  `05-milieu-chaines-alimentaires` 22, `04-nutrition` 16, `02-respiration` 15, `10-microbes-defense` 3, `09-oeil-vision` 3,
  `06-reproduction-florale` 2, `11-effets-courant-electrique` 2, `08-poids` 1, `12-dhaw` 1 (une ligne peut citer plusieurs slugs ;
  `06`, `08`, `09`, `11`, `12` ne sortent qu'en 2018 : œil, lumière, électricité, poids et reproduction florale
  sont absents des sessions 2019–2026 de ce lot).
- **Récurrences** : **les plaquettes sont nommées dans cinq lignes (2019, 2021, 2025, 2026 ×2)** alors que le manuel n'a que trois composants :
  la fiche les classe ◐ ; l'examen les teste. Les directions intermédiaires (huit directions) reviennent quatre années. Le sang
  décanté et le fer reviennent trois fois chacun. Le format « corriger l'erreur / justifier / classer » (pas de QCM) domine.
- **Rien d'illisible**, aucune page manquante ; deux ambiguïtés de figure notées (cible d'une flèche en 2021, anatomie du dessin du
  cœur en 2020). Aucun document introuvable dans mon lot.
