# Audit indépendant — lots M3 + M4 (missions du gisement, maths 6ᵉ)

Auditeur : opus, 2026-10-20. Périmètre : 20 missions, **177 questions** — `21/06–08`, `22/06–11`, `19/06–07`,
`20/06–09`, `25/06–10`, et les `chapter.json` (sources) des chapitres 19, 20, 21, 22 et 25. Méthode : chaque question
re-résolue à l'aveugle, puis comparée à la clé ; ensuite seulement, lecture des rapports `rapport-M3/M4a/M4b`. Missions
d'examen confrontées à la transcription `…/6eme-base/math/<année>-unique.md` et au PDF officiel (pages rendues à 150 dpi) ;
toutes les figures SVG rendues dans Chromium (page `dir="rtl"`, 360 px) ; les chaînes d'énoncé à formule passées par
`isolateLtrRuns` (bundle de `src/shared/lib/bidi.ts`) puis rendues dans Chromium. Aucun fichier de `content/` touché, aucune
écriture git.

## Verdict : **à corriger** (1 critique, 20 majeurs, mineurs ci-dessous)

Aucune clé fausse sur 177. Le défaut principal du lot M4b est structurel : la rampe d2 → d3 a été obtenue en **avançant
des étapes d2 qui redonnent la clé d'une étape d3 suivante** (5 cas). M4a a des figures dont les cotes se lisent à
l'envers en arabe et deux étiquettes de libellé ou d'explication inexacts. M3 est propre sur les clés ; ses défauts sont
une donnée infidèle (2019 P2), un nombre négatif (2010), des options qui nient une prémisse, et un doublon d'un quiz publié.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

| gate | résultat |
| --- | --- |
| `content:check` | ✓ (121 matières, 31 223 questions) |
| `content:qa -- --subject math-6eme` | 0 erreur, 5 avertissements (14 et 16, hors périmètre) |
| `content:figures:check` | ✓ |
| `content:tranche --chapters 19,20,21,22,25 --fresh --strict-longest` | clé strictement la plus longue 0/224 ; positions a 28 % · b 29 % · c 24 % · d 19 % ; 38 paires proches (intra-mission, étapes d'un même problème : voulues) ; 0 groupe gabarit |
| `content:gisement:controle` (19/06, 19/07, 25/10) | 0 plage ≥ 8 mots, 0 ≥ 6 mots ; 25/10 q5 : 2 données communes (sous le seuil de 3) |

Les gates ne voient aucun des défauts ci-dessous.

## Les points signalés par les auteurs

| point | jugement |
| --- | --- |
| 2023 cerf-volant : découpe en deux triangles donnée dans l'énoncé (21/06 Q6) | **Accepté** : le cours n'enseigne l'aire par les diagonales que pour le losange. Mais la Q7, qui calcule la même aire, ne redonne pas la découpe → majeur M-1 |
| 2022 arc 3/4 lu sur la figure (21/07 Q1, Q4) | **Accepté** : l'angle droit de l'angle ① en و rend « 3/4 » démontrable (360° − 90°), comme au PDF |
| 2025 arrêt de 5 min à أ entre deux tours | **Accepté** : lecture cohérente avec les 40 min « à prouver » du sujet (pas d'arrêt en أ dans un tour) ; « تتخلّله » de 22/06 Q1 lève l'ambiguïté |
| 2015 « 300 km aller-retour » | **Accepté**, fidèle au tableau officiel (« ذهابا و إيابا … (نفس الطريق) ») |
| 2026 P3 : E-4 (ج و = 5 donné) ; ج م = 4,8 par les aires | **Accepté** : 5 est donné en Q8, Q9 et Q10 ; ج م = 4,8 par (15,36 − 12) × 2 ÷ 1,4 sans algèbre ni Pythagore. Mais la Q3 (d2) redonne 4,8 avant la Q7 qui le calcule → majeur M-17 |
| 2016 Q8 soufflée par Q7 | **Non soufflée** : l'explication de Q7 ne donne pas 274 ; Q8 est un diagnostic sain. Elle recoupe la notion de Q3 (côté commun) → mineur |
| « oui/non + raison » 19/06 Q6 | **Accepté** : une seule raison vraie et suffisante (م n'est pas le milieu de [ب د]) |
| « oui/non + raison » 20/06 Q8 | Deux distracteurs absurdes (« 30 + 30 = 60 », « الارتفاع أصغر من القاعدة ») et doublon de Q7 → majeur M-10 |
| trois jugements d'étiquette de M4a | `pourcentage-base-erronee` (20/06 Q4) **accepté** (le libellé dit « le pourcentage (ou la fraction) sur la mauvaise base ») ; `operation-inverse-appliquee` pour × au lieu de ÷ par l'échelle **accepté** (le libellé couvre « une division au lieu d'une multiplication (ou l'inverse) ») ; `numerateur-denominateur-inverses` (20/09 Q6) **refusé** → majeur M-14 |
| figures M4a non vues | rendues : voir M-12 et M-13 |

## Tableaux de re-résolution

Notation : « réponse » = ma valeur trouvée à l'aveugle ; « clé » = la clé du fichier ; OK / ERREUR / réserve.

### 21/06 — 2023 P2 (7 q.) — fidèle (47,100 d, 20 d/m, أ ج = 1,5, و ب = و د = ج هـ, 75 d)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 2,355 | 2,355 | OK |
| 2 | 1,5 fois | 1,5 | OK (le distracteur « 3 مرّات », piège C04#2a, reste muet : aucun id) |
| 3 | 1,57 | 1,57 | OK |
| 4 | 0,5 | 0,5 | OK |
| 5 | 1 m | 1 م | OK |
| 6 | 0,75 m² | 0,75 | OK |
| 7 | 100 d | 100 | réserve (M-1) |

### 21/07 — 2022 P3 (12 q.) — fidèle (282,6 ; 1374 ; 1/2000 ; 60° ; 70 m)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 3/4 | 3/4 | OK |
| 2 | 376,8 | 376,8 | OK |
| 3 | 120 | 120 | OK |
| 4 | 60 m | 60 | OK |
| 5 | ثلث ③ + 1374 | idem | OK |
| 6 | 11 304 | 11 304 | OK |
| 7 | 8478 | 8478 | OK |
| 8 | 2826 | 2826 | OK |
| 9 | 4200 | 4200 | OK |
| 10 | 3 cm et 3,5 cm | idem | OK (grille 2 × 2 muette) |
| 11 | reste 60° | idem | réserve (mineur : notion non écrite au cours ; doublon de 19/07 Q6, voir M-11) |
| 12 | convertir, [أ ب], angle, parallèle à la hauteur, parallèle par أ | idem | OK |

### 21/08 — 2008 P2 (7 q.) — fidèle (1/150, 6 cm, 4 cm)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 9 m et 6 m | idem | OK |
| 2 | 27 | 27 | OK |
| 3 | « l'échelle porte sur les longueurs » | idem | OK |
| 4 | 4,5 m | 4,5 | OK |
| 5 | 63,585 | 63,585 | OK |
| 6 | 36,585 | 36,585 | OK |
| 7 | diamètre pris pour rayon (3,14 × 81 − 27 = 227,34) | idem | OK (mineur : l'explication n'écrit pas ce calcul) |

### 22/06 — 2025 P3 (10 q.) — fidèle

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 2 arrêts | توقّفان | OK |
| 2 | 10 | 10 | OK |
| 3 | 40 | 40 | OK |
| 4 | 3 | 3 | OK |
| 5 | 175 | 175 | OK |
| 6 | 8 h 55 | 8 h 55 | réserve (étiquette, M-2) |
| 7 | 10 | 10 | OK |
| 8 | ج → أ du 4ᵉ tour | idem | réserve (M-3) |
| 9 | 20 | 20 | OK |
| 10 | 24 | 24 | OK |

### 22/07 — 2022 P2 (10 q.) — fidèle (1280 hl ; 2 h 40 ; 8 h) ; les 140 hl/h du sujet ne sont pas repris (80 hl/h par 640 ÷ 8 : juste)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 10 h 40 | idem | OK (mineur : « 10 سا 80 د » distracteur sans mécanisme) |
| 2 | 640 | 640 | OK |
| 3 | 10 2/3 h | idem | réserve (doublon, M-4) |
| 4 | 60 | 60 | OK |
| 5 | 9 h 40 | idem | OK (mineur : « 10 سا 39 د » remplissage) |
| 6 | 580 | 580 | OK |
| 7 | 700 | 700 | OK |
| 8 | 80 | 80 | OK |
| 9 | 8 h 45 | idem | OK |
| 10 | 1 h 45 | idem | OK (mineur : « التاريخين » → « الموعدين ») |

### 22/08 — 2020 P1 (9 q.) — fidèle

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 6 h 50 | idem | OK |
| 2 | 7 h | idem | OK (mineur : option « 6 سا 50 د », bus inexistant) |
| 3 | 10 | 10 | OK |
| 4 | 7 h 36 | idem | OK (mineur : d1 réel, annoncé d3) |
| 5 | 9 | 9 | OK (idem) |
| 6 | 7 h 05 | idem | OK |
| 7 | bus de 7 h 30 | idem | réserve (M-5) |
| 8 | 25 | 25 | OK |
| 9 | 8 h 15 | idem | OK |

### 22/09 — 2019 P2 (8 q.)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 8 h 45 | idem | OK |
| 2 | 126 km | idem | OK |
| 3 | 108 | 108 | OK |
| 4 | 10 h 38 | idem | OK |
| 5 | 9 L | idem | OK |
| 6 | indéterminé tel qu'écrit (14 seulement si les 2 km du détour ne consomment rien) | 14 | **ERREUR de donnée** (C-1) |
| 7 | 42 | 42 | OK |
| 8 | n'a pas retranché les 10 L | idem | réserve (M-6) |

### 22/10 — 2015 P2 (7 q.) — fidèle (tableau officiel refait)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 150 km | idem | OK |
| 2 | 150 | 150 | OK |
| 3 | 6 h 40 | idem | OK |
| 4 | 13 h 55 | idem | OK |
| 5 | 180 | 180 | OK |
| 6 | 50 | 50 | OK |
| 7 | distance aller-retour pour le seul retour | idem | OK (mineur : option « ضرب » contredite par le calcul affiché) |

### 22/11 — 2010 P2 (7 q.) — fidèle

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 150 | 150 | OK |
| 2 | 170 | 170 | OK |
| 3 | 90 | 90 | OK |
| 4 | vendredi 1 h 20 | idem | OK |
| 5 | 20 | 20 | OK |
| 6 | 7 L | idem | OK |
| 7 | oubli des 15 L | idem | réserve (M-7) |

### 19/06 — devoir, trapèze rectangle et losange (7 q.)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 4 cm | idem | OK (mineur : redit la propriété du cours « الضلع العموديّ … هو نفسه ارتفاع ») |
| 2 | a b c d e f | idem | réserve (M-8) |
| 3 | 9 dm | 9 | OK (mineur : hauteur 4 dm inutile) |
| 4 | arc de centre ب, rayon 5, intersection côté د (ج = (6 ; 4)) | idem | OK (figure vérifiée : 4/9 au pixel) |
| 5 | 6 cm | idem | OK |
| 6 | non : م n'est pas le milieu de [ب د] (cerf-volant 5 ; 5 ; 5,66 ; 5,66) | idem | OK |
| 7 | a b c d e | idem | réserve (M-8) |

### 19/07 — devoir, constructions avec un angle (7 q.)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | centre en ب, zéro sur [ب أ), 110° | idem | OK |
| 2 | 5 cm et 5 cm | idem | OK |
| 3 | a b c d e | idem | OK |
| 4 | 5 cm | idem | OK (mineur : d1 réel) |
| 5 | 4 cm et 3 cm | idem | OK (figure vraie : 40/30, 69,9° ; cotes : M-12) |
| 6 | l'angle reste 70° | idem | réserve (doublon de 21/07 Q11, M-11) |
| 7 | ب ج = 5 cm | idem | OK |

### 20/06 — 2025 P2 (8 q.) — fidèle (le « trapèze isocèle » vient de la figure officielle : accepté)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 10,44 kg | idem | OK (mineur : « 12 كغ », « 1,56 كغ » sans mécanisme) |
| 2 | 5800 | 5800 | OK |
| 3 | 145 | 145 | OK |
| 4 | 4000 | idem | OK |
| 5 | 60 | 60 | OK |
| 6 | 40 cm | idem | OK |
| 7 | hauteur et petite base | idem | réserve (M-10) |
| 8 | oui (30 < 40 et 30 < 60) | idem | réserve (M-10) |

### 20/07 — 2018 P3 (10 q.) — figure relue au PDF : ج, ب, ن alignés sur la diagonale [ب د] ; hauteurs [أ ن] et [س ن] justes

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | [أ ن] | idem | OK (figure : M-13) |
| 2 | 43 750 | 43750 | OK |
| 3 | 250 m | idem | OK |
| 4 | 87 500 | idem | OK |
| 5 | 25,625 ha | idem | OK |
| 6 | 1,35 | idem | OK |
| 7 | 90 740 | 90740 | OK |
| 8 | 22 685 | idem | OK |
| 9 | 6 ; 3,5 ; 2,5 cm (ج ن = 250 + 350 = 600) | idem | OK |
| 10 | a b c d | idem | OK (mineur : ordre trivial, redit Q9) |

### 20/08 — 2013 P3 (9 q.) — fidèle (figure conforme au PDF)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 150 et 200 | idem | OK |
| 2 | 15 000 | 15000 | OK |
| 3 | 25 000 | idem | OK |
| 4 | 4 | 4 | OK |
| 5 | 1000 | 1000 | OK |
| 6 | 70 000 kg | idem | réserve (M-9) |
| 7 | 24 500 | idem | OK |
| 8 | 4900 | idem | OK |
| 9 | 16 000 | 16000 | OK |

### 20/09 — 2012 P3 (9 q.) — fidèle

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 42 m | idem | OK |
| 2 | 68 | 68 | OK |
| 3 | 1650 | idem | OK |
| 4 | 16,5 a | idem | OK |
| 5 | 39 600 | idem | OK |
| 6 | 39 600 ÷ 2 × 7 | idem | réserve (étiquette, M-14) |
| 7 | 138 600 | 138600 | OK |
| 8 | 178 200 | idem | OK |
| 9 | 12,5 | 12,5 | OK |

### 25/06 — 2026 P3 (10 q.) — figure vraie (demi-diagonales 6,4 / 4,8 ; و و أ à 1,4 de م ; côté 8)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 61,44 | idem | OK |
| 2 | 24 | idem | OK |
| 3 | 5 | 5 | réserve (fuite, M-17) |
| 4 | même base, même hauteur [ج م] | idem | réserve (M-18) |
| 5 | 12 | 12 | OK |
| 6 | losange ج و ن أ | idem | réserve (M-18) |
| 7 | 4,8 | 4,8 | OK |
| 8 | a b c d | idem | OK |
| 9 | 8 | 8 | OK |
| 10 | 32 | idem | OK |

### 25/07 — 2021 P3 (12 q.) — figure redessinée tournée d'un quart de tour, vraie au pixel (0,33 px/m partout)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | somme des trois pièces | idem | OK |
| 2 | 21/10 | idem | OK |
| 3 | 314 000 | idem | OK |
| 4 | 500 | 500 | OK |
| 5 | 3140 | 3140 | réserve (M-19) |
| 6 | 3 tours | idem | réserve (fuite, M-19) |
| 7 | 1962,5 | idem | OK |
| 8 | 471 | 471 | OK |
| 9 | 29 | 29 | OK |
| 10 | 392,5 | idem | OK |
| 11 | 1599 | 1599 | OK |
| 12 | en ج (5611 = 3 × 1599 + 814) | idem | OK |

### 25/08 — 2019 P3 (12 q.) — figure vraie (ج د = 102,5 ; د م = 82 ; أ هـ = 33)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | [د م], 82 m | idem | OK |
| 2 | 1353 | idem | OK |
| 3 | 3/10 | idem | OK |
| 4 | 236 775 | idem | réserve (fuite, M-20) |
| 5 | 369 | 369 | réserve (M-20) |
| 6 | 3382,5 | idem | OK |
| 7 | 102,5 | idem | OK |
| 8 | 101 475 | 101475 | OK |
| 9 | 338 250 | 338250 | OK |
| 10 | a b c d | idem | OK |
| 11 | 363 | 363 | OK |
| 12 | 2 × (102,5 + 82) − 6 | idem | OK |

### 25/09 — 2016 P3 (9 q.) — figure vraie (80/60, ن au pied de la hauteur 48)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 60 | idem | OK |
| 2 | 2400 | idem | OK |
| 3 | [أ ب], [أ د], [ج د] | idem | OK |
| 4 | 8 et 6 cm | idem | OK |
| 5 | 2400 ÷ 48 | idem | OK |
| 6 | 50 | 50 | OK |
| 7 | 224 | 224 | OK |
| 8 | quatre côtés comptés (274) | idem | OK |
| 9 | a b c d | idem | OK |

### 25/10 — devoir, périmètre réel sur plan (7 q.) — figure vraie (3 × 2, triangle 2-2-3, demi-disque de 2)

| q | réponse | clé | verdict |
| --- | --- | --- | --- |
| 1 | 1 cm ↔ 50 m | idem | OK |
| 2 | 100 | 100 | OK |
| 3 | 157 | idem | OK |
| 4 | haut du rectangle et diamètre | idem | OK |
| 5 | 607 | 607 | OK |
| 6 | 6,07 hm | idem | OK (mineur : redit Q5 dans une autre unité) |
| 7 | a b c d | idem | OK |

## Défauts

Tous les textes de remplacement ci-dessous ont été vérifiés : valeur recalculée, longueur de la clé contre chaque option
(aucune clé strictement la plus longue), aucune prémisse niée, aucune fuite vers une question suivante. Les correctifs de
figure ont été appliqués à une copie et rendus dans Chromium à 360 px.

### Critique

**C-1 · `22-durees/exercices/09-exam-2019-p2-voiture-retour-au-depart-reservoir.json` Q6 — donnée infidèle, problème
indéterminé.** Le sujet dit que la quantité consommée vaut les 3/5 du reste, sur tout le trajet (9 L). La mission écrit
« وكانت الكمّية المستهلكة منذ مغادرة المحطّة 9 ل » : la consommation des 2 km du détour sort de l'énoncé, et 14 L n'est
la réponse que si ce détour ne consomme rien. L'explication (« عند استئناف السير بعد التزوّد كان بالخزّان 24 ل ») et
celle de la Q8 reposent sur la même lecture.
- prompt : remplacer `وكانت الكمّية المستهلكة منذ مغادرة المحطّة 9 ل.` par `وكانت كمّية البنزين المستهلكة في التنقّل كلّه 9 ل.`
- explication Q6 (remplacement entier) : `ما دخل الخزّان كلّه، أي ما كان فيه عند المغادرة مع الـ 10 ل المضافة، يساوي الباقي مع المستهلك: 15 + 9 = 24 ل. فعند المغادرة الأولى كان بالخزّان 24 − 10 = 14 ل.`
- explication Q8 : remplacer `الـ 24 ل هي كلّ ما كان بالخزّان بعد التزوّد، وتشمل 10 ل أُضيفت في المحطّة.` par `الـ 24 ل هي ما كان بالخزّان عند المغادرة مع الـ 10 ل المضافة في المحطّة.`

### Majeurs

**M-1 · 21/06 Q7 — technique non enseignée, absente de l'énoncé.** L'aire du cerf-volant (rhombe non) n'est pas au cours ;
la Q6 donne la découpe, la Q7 ne la donne pas, alors que le donjon tire les questions au hasard. Prompt : remplacer
`وأ ج = 1,5 م و ب د = 1 م — برخامٍ` par
`وأ ج = 1,5 م و ب د = 1 م، ويقسمه [ب د] إلى مثلّثين قاعدتهما المشتركة [ب د] ومجموع ارتفاعيهما يساوي [أ ج] — برخامٍ`.

**M-2 · 22/06 Q6 — étiquette.** L'option « 7 سا 75 د » vient de 175 min lues « 1 h 75 min » (l'explication le dit) :
c'est la conversion en base cent, pas la retenue oubliée (suivre ce libellé donne 8 h 15, encore faux). Remplacer
`math.mes.duree-retenue-de-soixante-non-faite` par `math.mes.duree-convertie-en-base-cent`.

**M-3 · 22/06 Q8 — options qui nient la prémisse.** L'énoncé dit « وقع بين المحطّتين ج وأ فقط » et la clé le recopie ;
les trois autres options contredisent ce « فقط ». Toute conversion de 20 min en heure redoublerait `15/quiz#7` (l'auteur l'a
écartée à raison). **Supprimer la Q8** (la mission passe à 9 questions ; Q9 et Q10 restent autonomes).

**M-4 · 22/07 Q3 — doublon d'un quiz publié.** « 10 سا 40 د = ? ساعة », options 10,4 / 10 و 1/2 / 10 و 2/3 / 10 و 3/4,
reproduit `15-vitesse-distance-temps/quiz#7` (« 40 د = ? », options 0,4 / 1/2 / 2/3 / 1/4) à 10 h près. L'explication de
Q4 travaille en minutes (640 hl en 640 min) et n'en a pas besoin. **Supprimer la Q3** (9 questions).

**M-5 · 22/08 Q7 — deux options niées par la prémisse.** « حافلة 7 سا 5 د » et « حافلة 7 سا 35 د » n'existent pas
(bus toutes les demi-heures, rappelé dans l'énoncé) : il reste deux options.
- option c : `حافلة 8 سا` ; option d : `حافلة 6 سا 30 د` (longueurs 15 / 10 / 10 / 15 : clé non strictement la plus longue)
- explication : remplacer `ولا توجد حافلة على 7 سا 5 د ولا على 7 سا 35 د: الحافلات تنطلق كلّ نصف ساعة بالضبط.` par
  `وحافلة 6 سا 30 د انطلقت قبل وصوله، وحافلة 8 سا تنطلق بعد حافلة 7 سا 30 د فليست أوّل حافلة يلحقها.`

**M-6 · 22/09 Q8 — deux options éliminées à vue.** a (« نسي أن يضيف 9 ل ») contredit le calcul affiché « 15 + 9 » ;
d (« كان الخزّان ممتلئًا ») nie la prémisse « مملوءًا إلى ثلث سعته ».
- a : `كان عليه أن يطرح 9 ل من 15 ل لا أن يضيفها` ; c (clé) : `لم يطرح الـ 10 ل المضافة` ; d : `كان عليه أن يضرب 15 ل وحدها في 3` (longueurs 41 / 38 / 24 / 32)
- explication : ajouter à la fin `أمّا طرح 9 ل فيعطي (15 − 9) × 3 = 18 ل، والقسمة على 3 تعطي 24 ÷ 3 = 8 ل، ولا يساوي أيّ منهما 42 ل.`

**M-7 · 22/11 Q7 — nombre négatif hors programme, options niées, explication fausse.** « 12 − 20 = −8 ل » (les relatifs
ne sont pas au programme de 6ᵉ) ; a contredit le calcul affiché (il a bien retranché), c nie la donnée « استهلكت 20 ل » ;
l'explication affirme « ولا يغيّر ترتيب الطرح شيئًا في المعنى », ce qui est faux.
- prompt : remplacer `حسب تلميذٌ الباقي هكذا: 12 − 20 = −8 ل، فقال إنّ السيّارة لا تصل.` par `قال تلميذ: «12 ل أقلّ من 20 ل، فالوقود لا يكفي والسيّارة لا تصل».`
- options : a `كان عليه أن يقارن 12 ل باستهلاك 100 km وحده، أي 10 ل` ; b (clé) inchangée `نسي إضافة الـ 15 ل إلى الـ 12 ل` ; c `كان عليه أن يطرح الـ 15 ل المضافة من الـ 12 ل` ; d `كان عليه أن يضيف الـ 20 ل المستهلكة إلى الـ 12 ل` (longueurs 52 / 31 / 45 / 48)
- explication : `الوقود المتوفّر ليس الـ 12 ل وحدها، بل تضاف إليها الـ 15 ل التي تزوّد بها في الطريق: 12 + 15 = 27 ل، وهي أكثر من 20 ل، فتصل السيّارة ويبقى 27 − 20 = 7 ل. و20 ل هي استهلاك السفرة كلّها، فلا نكتفي باستهلاك 100 km، ولا نطرح الوقود المضاف ولا نضيف إليه المستهلك.`

**M-8 · 19/06 Q2 et Q7 — redonnent le cours.** Q2 déroule, dans le même ordre, les étapes de l'`exemple` « رسم شبه منحرف
قائم » du cours du 19 (seuls les nombres changent) ; Q7 déroule la méthode de la `propriete` du cours (« نرسم قطعتين
متعامدتين لهما المنتصف نفسه… ») et double en outre `25/09 Q9` (même construction ordonnée, mission d'examen qui la porte
au titre de E-5). **Supprimer Q2 et Q7** (la mission garde 5 questions : Q1, Q3, Q4, Q5, Q6).

**M-9 · 20/08 Q6 — distracteur au mécanisme faux.** « 71 000 كغ » est dit « يجمع بدل أن يضرب », or 1 000 + 70 = 1 070.
Option c : `1 070 كغ` (avec U+00A0), étiquette `math.num.operation-inverse-appliquee` conservée ; explication : remplacer
`والعدد 71 000 كغ يجمع بدل أن يضرب.` par `والعدد 1 070 كغ يجمع 1 000 و 70 بدل أن يضربهما.` (U+00A0 dans les milliers).

**M-10 · 20/06 Q7–Q8 — explication fausse et doublon.** Au sujet, la grande base [أ ب] est EN HAUT : le trapèze se
rétrécit vers le bas. Les explications disent « ولا تضمن شيئًا عند الأعلى » (Q7) et « العرض يضيق في الأعلى » (Q8) :
faux pour la figure. Q8 redit la clé de Q7 (hauteur et petite base) ; ses distracteurs b et d sont absurdes.
- **supprimer la Q7** (7 questions) ;
- Q8 option b : `نعم، لأنّ مساحة المربّع 900 صم² أصغر من مساحة الجزء ① 4 000 صم²` (U+00A0 ; étiquette `math.geo.condition-suffisante-supposee`) ; option d : `لا، لأنّ الضلعين المائلين يضيّقان الشكل نحو الأسفل فلا يتّسع لمربّع` (longueurs 70 / 63 / 63 / 67 : clé non strictement la plus longue) ;
- Q8 explication : `المربّع يتّسع إذا كان ضلعه أصغر من الارتفاع 40 صم ومن أضيق عرض للشكل وهو القاعدة الصغرى 60 صم، وهذا محقّق لأنّ 30 < 40 و 30 < 60. المقارنة بالقاعدة الكبرى وحدها لا تكفي لأنّ العرض يضيق نحو الأسفل حتّى القاعدة الصغرى، ومقارنة المساحتين لا تكفي لأنّ شكلًا واسع المساحة قد يكون أضيق من ضلع المربّع، وتضيّق الشكل لا يمنع المربّع ما دام أضيق عرض فيه 60 صم.`
- si la Q7 est gardée : y remplacer `ولا تضمن شيئًا عند الأعلى` par `ولا تضمن شيئًا في الأسفل حيث يضيق الشكل`.

**M-11 · 19/07 Q6 ↔ 21/07 Q11 — même question dans deux missions.** « Que devient l'angle à l'échelle ? », réponse
« il reste », distracteur « divisé par l'échelle (0,07° / 0,03°) ». Garder celle de l'examen ; **supprimer 19/07 Q6**
(6 questions).

**M-12 · Figures M4a — cotes qui se lisent à l'envers.** Les nœuds `<text>` qui mêlent nombre et unité arabe portent
`direction="ltr" unicode-bidi="isolate"` (interdit par `course-figures.md`, règle 2) : en Chromium `dir=rtl`, « 8,4 سم »
s'affiche nombre à gauche, unité à droite, et se lit « سم 8,4 ». Fichiers : 19/07 (« 40 م », « 30 م », « 5 سم »), 20/07
(« 250 م », « 350 م »), 20/08 (« 150 م », « 200 م », « 250 م », « 75 م », « 125 م »), 20/09 (« 8,4 سم », « 13,6 سم »,
« 6 سم »). Correctif vérifié au rendu : retirer ` direction="ltr" unicode-bidi="isolate"` de ces seuls nœuds (les lettres
seules et les nombres nus peuvent garder l'isolat). Dans 20/09, déplacer en plus `6 سم` de `x="44"` à `x="82"` (sinon le
côté oblique le barre). Mineur associé : aucune des figures M4a n'a le halo `paint-order="stroke" stroke="#ffffff"
stroke-width="4"` des autres lots.

**M-13 · Figures 20/07 et 20/06 — étiquettes illisibles à 360 px (vérifié au rendu).**
- 20/07 (les deux SVG, Q1 et Q3) : `ب` posé sur le segment [ج ب] (`x="124" y="116"` → `x="144" y="118"`) ; `ن` barré par la
  diagonale (`x="205" y="213"` → `x="216" y="200"`) ; `250 م` barré par [أ ن] : le supprimer (la donnée « أ ن = 250 م » est
  dans chaque énoncé qui en a besoin ; le sujet la donne en légende, pas sur le segment).
- 20/06 : `و` recouvre ① (`و` : `x="130" y="136"` → `x="140" y="135"` ; ① : `y="152"` → `y="162"`).

**M-14 · 20/09 Q6 — étiquette.** « 39 600 ÷ 7 × 2 » calcule les 2/7 du prix du terrain au lieu de retrouver le tout dont
il est les 2/7 : erreur de base, pas d'écriture (numérateur au-dessus du trait). Remplacer
`math.frac.numerateur-denominateur-inverses` par `math.prop.pourcentage-base-erronee` (« le pourcentage (ou la fraction)
sur la mauvaise base »).

**M-15 · 25/07 figure (les deux SVG, 8 occurrences) — cote et sommet coupés par le bord.** `628` centré en `x="10"`
déborde à gauche (`x="44"`) ; `أ` en `x="357.4" y="304.2"` déborde à droite (`x="346" y="318"`). Vérifié au rendu.

**M-16 · `25-perimetre-figure-composee/chapter.json` — `sources[]` sans les deux lignes de l'étude 36.** Le rapport M4b dit
les avoir ajoutées ; le fichier a été réécrit à 00 h 39 (même minute que les exercices 01–05, passe de correction B5) et
ne les contient plus. Rajouter :
« Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel,
reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/math/ » et « Calibré sur des
devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-math/fiche.md ».

**M-17 · 25/06 Q3 — fuite en avant.** La Q3 (d2, émise avant les d3) donne « ج م = 4,8 », clé de la Q7, et « مساحته 12 »,
clé de la Q5. Passer la Q3 en `"difficulty": 3` et la placer **après la Q7** dans le fichier (le tri stable la garde
alors derrière Q5 et Q7).

**M-18 · 25/06 Q4 et Q6 — marqueurs de forme et option défendable.** Les trois distracteurs de Q4 portent « فقط دون النظر
إلى … » et ceux de Q6 « بالضرورة وفي كلّ حالة » / « وحده يكفي » : la clé est la seule sans marqueur. En Q6, l'option c
(« [د و] = [أ ب] ») se défend en contexte (م milieu de [د ب], diagonales du losange ب ج د ن) ; l'explication dit à tort
qu'elle « لا يتعلّق بـ [و أ] ». En Q4, toute option « bases égales » est vraie en contexte (même sommet ج, bases sur
(د ب)) : les distracteurs ne doivent pas la contenir.
- Q4 options : a `لأنّ لهما الرأس نفسه ج، ولكلّ منهما ضلع على القطر [د ب]` (étiquette `math.geo.condition-suffisante-supposee`) ; b `لأنّ ضلعيهما [ج د] و [ج ب] متقايسان، وهما ضلعان من المعيّن` (muette) ; c `لأنّ [ج م] عموديّ على [د ب]، فكلّ المثلّثات التي رأسها ج لها المساحة نفسها` (étiquette `math.geo.condition-suffisante-supposee`) ; d (clé) `لأنّ قاعدتيهما [د و] و [أ ب] متقايستان، وارتفاعهما المشترك هو [ج م]` (longueurs 55 / 58 / 74 / 67). Explication : remplacer `ومشاركة الرأس وحدها لا تكفي، فالقاعدتان قد تختلفان.` par `ومشاركة الرأس ج وحدها لا تكفي، فالقاعدتان قد تختلفان، وتقايس [ج د] و [ج ب] لا يقول شيئًا عن القاعدتين، وكلّ مثلّث رأسه ج وقاعدته على (د ب) له الارتفاع [ج م] لكنّ مساحته تتغيّر بتغيّر قاعدته.`
- Q6 options : a `لأنّ القطر [ج ن] عموديّ على [و أ]، وكلّ مستقيم عموديّ على قطعة يمرّ بمنتصفها` (étiquette `math.geo.condition-suffisante-supposee`) ; b (clé) `لأنّ ج و ن أ معيّن، وقطرا المعيّن يتقاطعان في منتصف كلّ منهما` ; c `لأنّ [ج م] و [م ن] متقايستان، فالنقطة م منتصف كلّ قطعة تمرّ بها` ; d `لأنّ قطري الرباعيّ ج و ن أ متقايسان، وتقاطع قطرين متقايسين يكون في منتصفيهما` (étiquette `math.geo.diagonales-proprietes-mal-attribuees`) (longueurs 76 / 61 / 63 / 76). Explication : remplacer `تعامد القطرين وحده لا يعطي المنتصف، وتساوي [د و] و [أ ب] أو [ج م] و [م ن] لا يتعلّق بـ [و أ].` par `تعامد القطرين وحده لا يعطي المنتصف، وكون م منتصف [ج ن] لا يجعلها منتصف كلّ قطعة تمرّ بها، وقطرا ج و ن أ غير متقايسين: [و أ] أقصر بكثير من [ج ن].`

**M-19 · 25/07 Q5 et Q6 — fuites en avant.** Q5 (d2) redonne « 1962,5 », clé de la Q7, et sa propre clé 3140 est écrite
dans les énoncés des Q3 et Q4 (d2, émises avant) : **supprimer la Q5** (11 questions). Q6 (d2) donne « 1599 », clé de la
Q11 : la passer en `"difficulty": 3` et la placer **entre Q11 et Q12**.

**M-20 · 25/08 Q4 et Q5 — fuites en avant et doublon.** Q4 (d2) donne « 101475 », clé de la Q8 : la passer en
`"difficulty": 3` et la placer **après la Q9**. Q5 (d2) donne « ج د = 102,5 », clé de la Q7, et son périmètre 369 est
redemandé par Q11 (369 − 6) et Q12 (l'expression) : **supprimer la Q5** (11 questions).

### Mineurs

- 21/06 Q6 : le distracteur « 5 م² » (= 2 × (1 + 1,5)) porte `aire-et-perimetre-confondus` ; même usage étendu en 20/07 Q4
  (600), 25/08 Q2 (115), 25/09 Q2 (140) : somme de deux dimensions, pas un périmètre. Accepté par précédent (B5), à
  harmoniser au registre.
- 21/07 Q11 : « l'échelle garde les angles » n'est écrit dans aucun cours (14 dit seulement que la réduction est la même
  pour les trois côtés) ; l'explication l'enseigne. À ajouter au cours du 14, ou garder la question en l'état.
- 21/08 Q7 : explication à compléter par `3,14 × 9 × 9 = 254,34، ثمّ 254,34 − 27 = 227,34`. Figure : cotes « 6 » et « 4 »
  sans unité (le sujet porte « صم »).
- 22/06 Q1 : lecture « deux arrêts par tour » juste mais à un mot près (« تتخلّله ») ; garder.
- 22/07 : Q1 « 10 سا 80 د » et Q5 « 10 سا 39 د » sont des remplissages ; Q10 « الفرق بين التاريخين » → « الفرق بين الموعدين ».
  Les 140 hl/h du sujet ne servent pas (80 hl/h obtenu par 640 ÷ 8 : juste).
- 22/08 Q2 : option « 6 سا 50 د » (aucun bus à cette heure) ; Q4 et Q5 sont des additions d'une étape annoncées d3.
- 22/06 Q10 : 8 km en 20 min recoupe une étape de `15/05#10` (donnée officielle : accepté, signalé par l'auteur).
- 22/10 Q7 : option « ضرب المسافة في الزمن » contredite par le calcul affiché.
- 19/06 Q1 : redit la phrase du cours (« الضلع العموديّ … هو نفسه ارتفاع ») ; Q3 : la hauteur 4 dm est une donnée inutile.
- 19/07 Q4 : d1 réel ; Q5 : l'option « 0,4 سم و 0,3 سم » n'est pas expliquée.
- 20/06 Q1 : options « 12 كغ » et « 1,56 كغ » sans mécanisme.
- 20/07 Q10 : ordre trivial, qui redit la Q9.
- 20/09 Q6 explication : « هي المصاريف كلّها » → « هي مصاريف التهيئة والتجهيز » (le terrain n'en fait pas partie).
- 25/07 figure : `ز` presque masqué par la diagonale (`x="106.7"` → `x="118"`).
- 25/09 Q8 recoupe la notion de Q3 (côté commun hors du contour) ; elle n'est pas soufflée par Q7.
- 25/10 Q6 redit Q5 en hectomètres ; la figure laisse vide la moitié haute de son `viewBox`.
- Gabarit transversal (non bloquant) : la conversion d'échelle « options juste / × N / sans m → cm / facteur 10 » revient
  en 21/07 Q10, 21/08 Q1, 19/06 Q5, 19/07 Q5, 20/07 Q9, 20/09 Q1, 25/09 Q4, 25/10 Q1–Q2 ; c'est le geste voulu par E-5,
  mais l'id manquant `math.mes.echelle-unites-non-uniformisees` (déjà demandé par B3, M3 et M4a) le laisse muet partout.

## Ne pas redemander

Recherche de proximité (Jaccard ≥ 0,33 sur les mots et nombres) de chaque question contre toutes les questions de
`math-6eme` (quiz, exercices, missions) et tous les blocs `exemple` / `verifie` des cours : aucun recoupement avec les
exercices 01–05 des chapitres audités dans leur état actuel (20, 21 et 25 ont été réécrits par la passe B5 après
l'écriture des missions ; la recherche porte sur l'état courant). Recoupements relevés à la main : 19/06 Q2 et Q7 (cours,
M-8), 22/07 Q3 (`15/quiz#7`, M-4), 19/07 Q6 ↔ 21/07 Q11 (M-11), 19/06 Q7 ↔ 25/09 Q9 (M-8).

## Étiquettes manquantes (à proposer au registre, rien n'est inventé)

Celles des rapports M3, M4a et M4b sont confirmées. Les plus utiles, par nombre d'options qu'elles feraient parler :
échelle sans uniformiser m/cm (≥ 8 options), arc compté comme circonférence entière (21/06 Q2, 21/07), côté commun ou
diamètre compté dans le contour (25/09 Q3, 25/10 Q3–Q5), arrêt ou ravitaillement oublié (22/06, 22/09, 22/11),
changement de jour oublié (22/11 Q4).

## Chiffres

| | 21 | 22 | 19 | 20 | 25 | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| questions auditées | 26 | 51 | 14 | 36 | 50 | **177** |
| clés fausses | 0 | 0 | 0 | 0 | 0 | **0** |
| critiques | 0 | 1 | 0 | 0 | 0 | **1** |
| majeurs | 1 | 6 | 2 | 5 (dont M-12, partagé avec 19/07) | 6 | **20** |
| questions à reprendre (texte, étiquette, ordre ou suppression) | 1 | 7 | 4 | 4 | 7 | **23** |

Questions à reprendre : 21/06 Q7 ; 22/06 Q6, Q8 ; 22/07 Q3 ; 22/08 Q7 ; 22/09 Q6, Q8 ; 22/11 Q7 ; 19/06 Q2, Q7 ;
19/07 Q5 (figure), Q6 ; 20/06 Q7, Q8 ; 20/08 Q6 ; 20/09 Q6 ; 25/06 Q3, Q4, Q6 ; 25/07 Q5, Q6 ; 25/08 Q4, Q5 ;
plus les figures de 19/07, 20/06, 20/07, 20/08, 20/09, 25/07 et le `chapter.json` du 25. Suppressions proposées : 8
questions (22/06 Q8, 22/07 Q3, 19/06 Q2 et Q7, 19/07 Q6, 20/06 Q7, 25/07 Q5, 25/08 Q5) ; le lot passe de 177 à 169
questions, aucune mission sous 5 questions.
