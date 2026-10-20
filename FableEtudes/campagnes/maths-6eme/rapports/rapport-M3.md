# Rapport — lot M3 (maths 6ᵉ) : missions d'examen des chapitres 21 et 22

## Relecture au lancement (🔁 B5)

- Rapport B5 relu ; empreintes SHA-256 des 9 fichiers de `21-cercle-disque` identiques à `b5-etat-au-plan.json` (cours, quiz, exercices 01–05 inchangés depuis 23 h 36). Plus grand `NN` : `21` = 05, `22` = 05 → plages de la carte valables (06–08 et 06–11).
- « Ne pas redemander » revérifiés question par question contre le cours (sections : couronne, demi-cercle/quart/trois quarts, rayon retrouvé) et les exercices actuels : listes exactes. `21/02-boss#5` (« أيّ مقدار يخصّ القرص ») reste ambiguë, non touchée, non reprise.
- Croisement avec les missions déjà écrites par M1/M2 (13, 14, 15) : aucune donnée reprise deux fois.

## Fichiers (9 missions, 77 questions ; carte : 80)

| NN | fichier | session · problème | q. | formats |
| --- | --- | --- | ---: | --- |
| 21/06 | `06-exam-2023-p2-cerf-volant-fil-demi-cercles` | 2023 P2 | 7 | 3 numeric, 4 QCM (dont aire par les deux triangles) |
| 21/07 | `07-exam-2022-p3-parc-carre-parallelogramme-secteur` | 2022 P3 | 12 | 5 numeric, 6 QCM, 1 ordering (construction au 1/2000) |
| 21/08 | `08-exam-2008-p2-fontaine-losange-dans-le-disque` | 2008 P2 | 7 | 2 numeric, 5 QCM (dont 2 chasses à l'erreur) |
| 22/06 | `06-exam-2025-p3-bus-quatre-tours` | 2025 P3 | 10 (carte : 12) | 6 numeric, 4 QCM |
| 22/07 | `07-exam-2022-p2-piscine-deux-pompes` | 2022 P2 | 10 | 5 numeric, 5 QCM |
| 22/08 | `08-exam-2020-p1-ouvrier-bus-toutes-les-demi-heures` | 2020 P1 | 9 | 3 numeric, 6 QCM |
| 22/09 | `09-exam-2019-p2-voiture-retour-au-depart-reservoir` | 2019 P2 | 8 (carte : 9) | 3 numeric, 5 QCM |
| 22/10 | `10-exam-2015-p2-excursion-aller-retour` | 2015 P2 | 7 | 3 numeric, 4 QCM (tableau officiel refait en tableau) |
| 22/11 | `11-exam-2010-p2-trajet-de-nuit-passage-de-minuit` | 2010 P2 | 7 | 4 numeric, 3 QCM |

Toutes : d3 `boss` 120/30, en-tête « 🏛️ مناظرة <année> · المسألة N ⭐⭐⭐ », `displayOrder` = NN, chaque question dit sa session et redonne ses données, rampe non décroissante (d2 d'abord, puis d3). Clés : a 10 · b 10 · c 11 · d 10. `chapter.json` (21 et 22) : seule la ligne `sources[]` « Sujets officiels du concours d'entrée aux collèges pilotes… » ajoutée.

## Problèmes repris, données données dans l'énoncé

- **2023 P2** : fil de 47,100 d à 20 d le mètre ; π = 3,14 ; diagonales du cerf-volant. Figures SVG : la queue de trois demi-cercles (sans cote) et le cerf-volant (cote 1,5 portée sur une ligne de cote extérieure, traits d'égalité). Pour l'aire, la décomposition en deux triangles de même base est donnée dans l'énoncé de la Q6 (le programme ne donne l'aire que du losange par ses diagonales).
- **2022 P3** : arc de 282,6 m lu comme trois quarts depuis la figure (la Q4 ne donne pas la fraction) ; la figure est à l'échelle vraie (côté 60 m, hauteur 70 m, angle 60°). Les données de la Q3 officielle (60°, 70 m) sont données, la construction est convertie en conversions d'échelle, angle conservé et `ordering` (E-5), aucun dessin.
- **2008 P2** : le titre ne dit pas « losange inscrit » (les sommets verticaux sont dans le disque, seule la diagonale horizontale est un diamètre). Cotes sur lignes extérieures.
- **2025 P3** : figure du secteur (sans cote). On admet, comme le sujet, un arrêt de 5 min à A entre deux tours (4 × 40 + 3 × 5 = 175 min, 8 h 55) ; l'arrivée à 9 h 05 donne 10 min de retard.
- **2022 P2** : 60 hl/h et 80 hl/h déduits (somme 140 donnée par le sujet) ; 1 hl par minute exploité.
- **2020 P1** : durée de marche finale 9 min donnée dans la Q9 (sortie de la Q1 officielle).
- **2019 P2** : « التاسعة إلا الربع » = 8 h 45 posé en Q1 ; 126 km = 1 + 1 + 124.
- **2015 P2** : lecture « 300 km aller et retour, même route » (150 km chacun) ; retour de 13 h 55 à 16 h 55.
- **2010 P2** : ajouts de la carte (jour demandé en plus de l'heure).
- Rien de ◐/⛔ : ni intérêt, ni somme-écart/rapport, ni 180°, ni Pythagore, ni volume. Aucun item `[hors programme]`, aucun `[illisible]` rencontré. L'échelle n'est jamais appliquée à une aire : la Q3 de 2008 est un diagnostic (échelle sur longueurs seulement), sans facteur k².

## Étiquettes

Employées (registre `math.*`, toutes valides) : `geo.rayon-et-diametre-confondus`, `mes.aire-triangle-sans-moitie`, `mes.aire-et-perimetre-confondus`, `mes.aire-losange-sans-moitie`, `mes.echelle-aire-rapport-non-carre`, `frac.fraction-d-un-nombre-multipliee-au-lieu-de-divisee`, `frac.fraction-d-un-nombre-etape-oubliee`, `frac.numerateur-denominateur-inverses`, `num.operation-inverse-appliquee`, `num.soustraction-colonne-petit-du-grand`, `mes.duree-convertie-en-base-cent`, `mes.duree-retenue-de-soixante-non-faite`, `prop.formule-vitesse-inversee`. Posées seulement sur des options à erreur unique ; options à deux erreurs et grilles 2×2 (21/07 Q10, 21/08 Q1) laissées muettes.

**Manquantes (options laissées muettes), ids proposés** : `math.geo.arc-circonference-entiere-prise-pour-l-arc` (C04#2a, C05#3a) · `math.mes.fraction-appliquee-au-disque-entier` (C05#3b) · `math.mes.echelle-unites-non-uniformisees` (C05#3c, déjà proposé par B3 ; plan 1/2000 lu en cm sans convertir) · `math.mes.arret-compte-en-trop-ou-en-moins` (C02#3a/b) · `math.mes.attente-du-prochain-depart-ignoree` (C07#1a) · `math.mes.retard-ajoute-a-l-arrivee` (C07#1b) · `math.mes.changement-de-jour-oublie` (C17#2a) · `math.mes.ravitaillement-oublie` (C08#2b, C17#2b) · `math.mes.trajet-aller-retour-ignore` (C08#2a).

## Vérifications

- Double résolution de chaque valeur par deux chemins, rejouée par script (clés, distracteurs, cohérence 4 200 m² = 60 × 70, 42 L, 580 + 700 = 1 280 hl, etc.) : tout concorde.
- `content:check` ✓ · `content:qa -- --subject math-6eme` : 0 erreur ni avertissement sur mes fichiers (les 4 erreurs restantes sont dans `19-quadrilateres/06-07-devoir-*`, séparateurs de milliers, lot M4) · `content:figures:check` ✓ · `content:tranche --chapters 21,22 --fresh --strict-longest` : clé strictement la plus longue 0/93 ✓, patron de notion 0 en recul ✓ · `lot-lint` : rien à signaler · `prettier --check` ✓ (milliers en U+00A0 hors des valeurs de clé numeric, ré-écrites sans séparateur dans l'explication pour l'écho de la valeur).
- Figures rendues dans Chromium et relues (parc à l'échelle, secteur, cerf-volant, fontaine).

## Doutes pour l'auditeur

- **Paires proches** (30 signalées, non bloquantes) : surtout intra-mission, étapes d'un même problème qui redonnent chacune sa donnée (voulu par la règle R1) ; élaguées au minimum nécessaire par question.
- **22/06 Q9–Q10** : « 8 km en 20 min → 24 km/h » rejoint `15/05#10` (Sami, 8 km en 20 min) ; c'est la donnée officielle, le contexte diffère.
- **22/06 Q1** : l'arrêt à A n'est pas dans la première sortie ; lecture identique à la carte et à la correction attendue (40 min).
- **21/07 Q8** redonne 11 304 m² (clé de Q6) et **21/06 Q5/Q7** les valeurs des étapes précédentes : fuites inhérentes à des étapes qui doivent se lire seules.
- Nombres de questions inférieurs à la carte pour `22/06` (10 au lieu de 12) et `22/09` (8 au lieu de 9) : étapes triviales ou doublons de `15/quiz#7` (20 min = 1/3 h) et d'une seconde sous-étape de capacité écartées.
