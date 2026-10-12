# NOTES — SVT L05 (auteur gisement) — chapitre 12-takawwun-al-janin, fichiers 07 a 10
Demarre: 2026-10-12 ~08:08 UTC.

## Mission (prompt-svt-L05.md + assign-svt-L05.md)
- 07: 2026 ex2 (d2, 5 etapes) displayOrder 7  -> examen-2026-ex2-<slug>.json  (lieu formation/maturation gametes ; legender gametes+embryon)
- 08: 2022 ex1 (d2, 1 etape) displayOrder 8   -> examen-2022-ex1-<slug>.json  (choisir enonce exact reproduction/vision/excretion)
- 09: 2025 ex3 (d3, 4 etapes) displayOrder 9  -> examen-2025-ex3-<slug>.json  (ovulation/fecondation/nidation lieux/dates)
- 10: 2024 ex4 (d4, 5 etapes) displayOrder 10 -> examen-2024-ex4-<slug>.json  (courbes de temperature: ovulation, fecondation, gestation)
- PDF officiels: scratchpad/gisement/9eme-sciences-vie-terre/snapshots/9web.edunet.tn/ (C01=2026, C02=2025, C03=2024, C04=2022, C05=2021, C06=2020) LECTURE SEULE
- Registre etiquettes: git -C /home/user/yahia-quest-content show origin/main:content/misconceptions.json
- Gates: source scratchpad/engine-env.sh && cd /home/user/yahia-quest-arena && npm run -s content:gates -- --tranche
- lot-lint: node /home/user/yahia-quest-content/FableEtudes/36-gisement-examens-devoirs/outils/lot-lint.mjs <fichiers>
- Pas de commit/push. N'editer que mes 4 fichiers + chapter.json sources[].

## Avancement
- [x] prompt + consigne gisement-auteur-examen.md lus; skills prof-svt-9eme, content-ecole-tn charges
- [x] Transcriptions lues (2026 ex2, 2022 ex1, 2025 ex3, 2024 ex4). PDF rendus dans svt-l05-work/pdf (110 dpi) et hi/ (300 dpi).
- 2026 ex2 Doc1 vu sur PDF: (a) spermatozoide [fleche 1 -> debut de la portion spiralee derriere la tete = piece intermediaire], (b) ovocyte II + 1 globule polaire (fleche 2: petit corps brun-rouge entre enveloppe et cellule) + cellules folliculaires en couronne (fleche 3 x2), noyau bleu dans moitie haute, (c) morula dans enveloppe grise epaisse (« غلاف محيط », « خلية »). Q: nommer a,b,c ; legendes 1-3 ; tableau lieu naissance/maturation (a,b) ; 4a source de (c)+etapes ; 4b devenir de (c) apres 4 jours.

## Constats de lecture (08:5x)
- Registre origin/main copie: svt-l05-work/misc-origin-main.json (bio.* tags utiles: repro.lieux-des-gametes-confondus, repro.fecondation-dans-l-uterus, repro.fecondation-reduite-a-l-entree, repro.pieces-du-spermatozoide, repro.durees-de-vie-inversees, cycle.regles-signe-de-fecondation, cycle.ovulation-au-milieu-du-cycle, gros.sangs-melanges-au-placenta, gros.barriere-placentaire-absolue, excr.etape-du-nephron-confondue, vis.cornee-quatrieme-membrane, vis.recepteurs-hors-retine, lecture.valeur-d-une-autre-grandeur)
- Cours ch.12: fecondation 4 stades (entoure, 1 entre, rapprochement des 2 noyaux, fusion), haut 1/3 oviducte; jour0 cellule-oeuf, j1 2 cell, j2 4 cell, j4 TOUTETIA (morula 64 cellules, « الغلاف المحيط »), j6 perd enveloppe -> MUDGHA (cavite), j7 nidation; placenta 4 fonctions; vie des gametes: spz 3-4 j, ovule ~24 h (ou 1-2 j)
- Cours ch.10: spz tete (noyau, acrosome) / piece intermediaire (mitochondries) / flagelle; formation tubes seminiferes (testicule), maturation epididyme; ovule: formation ovaire, « ينتهي نضجها إثر دخول حيوان منوي »; glandes annexes (vesicules seminales, prostate), gonades (testicules, ovaires = gametes + hormones)
- Cours ch.11: cycle 28 j (24-32), phase lutéale fixe 14 j -> ovulation = longueur-14; courbe thermique 36,5-36,7 puis ~37,1 apres ovulation jusqu'a la fin du cycle; si fecondation corps jaune ne regresse pas, endometre maintenu, pas de regles
- Cours ch.09: nephron 4 fonctions: filtration, reabsorption, SECRETION (« إفراز » ex. NH3 par tubule), EXCRETION (« إخراج » uree, acide urique) -> 2022 ex1 Q4 « يفرز النيفرون » = النشادر (cle probable)
- Cours ch.03: cristallin = « عدسة مرنة محدّبة الوجهين » ; cornée = « طبقة شفّافة بالوجه الأمامي » ; iris regle la lumiere (pupille)
- AUCUN cours n'enseigne: « الكرية القطبية » (globule polaire), « الخلايا الجريبية » (cellules folliculaires/couronne) -> a donner dans chaque enonce qui les emploie. Aussi 'deuxieme globule polaire n'apparait qu'apres entree du spz' = a donner.
- Missions voisines EN COURS (arbre de travail, hors origin/main): ch.10 07 (2021 ex1: Q4 'يكتمل نضج البويضة إثر دخول حيوان منوي' -> NE PAS dupliquer), ch.11 07-09 (09: matching spz/ovule, pieces du spz, lieux/durees gametes, calendrier ; 08: structures ovariennes), ch.09 07 Q4 (ou NH3 est secrete: tubule), ch.09 09 (nephron legendes), ch.03 09/11 (oeil, iris).
- Missions publiees ch.12: 01..06 (tamrin x2, boss placenta 4 fonctions, defi, tadrib, defi-concours). Deja couverts: lieu fecondation (quiz Q1, 01 Q2), 4 stades, jours 0-7, nidation j7, placenta 4 fonctions/barriere/melange, antics maternels.
- Regles de forme (session): pas de lettres arabes dans <text> des figures, reperes numerotes 1,2,3.., pas de lettre latine comme repere; enonces portent les donnees de leur session; ramp non decroissante (lot-lint); cle jamais la plus longue; explications sans lettres d'options; Q suivante ne fuit pas.
- 2024 courbes: ticks axe x = 1(avr) 14 | 1(mai) 12 | 1(juin) 9 ; y ticks 36,5 37,0 37,5 ; A: rises 14 avr, 12 mai, 9 juin (28 j exacts: 30-14+12=28 ; 31-12+9=28), chute vers 1er mai et ~fin mai; B: identique jusqu'au 12 mai puis plateau 37,1-37,3 sans chute (au-dela du 1er et du 9 juin). Doc 5: ovocyte, UN noyau central, 2 globules polaires, cellules folliculaires en couronne (gouttes).
- 2025 doc3: 3 evenements: (1) follicule eclate + ovule qui sort ; (2) cellule + 2 masses sombres accolees (pronuclei) + 2 globules polaires (1ere, 2eme) + couronne de cellules ; (3) petit sac creux (blastocyste) avec amas cellulaire (« المضغة ») enfonce dans muqueuse « بطانة الرحم ». Tableau: nom+justification / lieu / date (cycle de 28 j) ; Q2: deux fonctions du placenta.
