# Notes de l'auteur B4 — 07-aimants-boussole · 11-effets-courant-electrique · 08-poids

Lu en entier : prompt auteur, skills (content-ecole-tn, content-engine + références, content-cours, content-interactif, prof-eveil-primaire), fiche (en-tête, § 1 dont § 1.7, § 2 unité 5, § 4 bis, § 6.0–6.5, § 7.43–7.47), PLAN V1–V5, PLAN-passage, manuel 103604 p.119–145 **à l'image** (toutes les pages des trois chapitres).

## Table des écarts

### 07-aimants-boussole
| # | écart | traitement |
|---|---|---|
| A1 | **V5** : 8 directions (ش ج ق غ + ش ق، ش غ، ج ق، ج غ) et rose des vents SVG : absentes du cours et des exercices (manuel p.134 « أقيّم تعلّمي 7 », guide p.176) | nouvelle section 7 au patron + figure + 6 questions |
| A2 | procédé d'orientation (guide p.176 : tourner la boîte jusqu'à ce que ش soit sous la pointe nord de l'aiguille) absent | étape de l'exemple de la section 7 |
| A3 | inversion Est/Ouest (se lit déjà en filigrane à 02-boss Q6) : pas de `::: piege`, pas de distracteur | piège de la section 7 + distracteurs muets (id proposé) |
| A4 | aimant cassé : chaque morceau garde ses deux pôles (manuel p.132 « أتعهّد » 1 ; guide p.171 « ثنائي القطب ») : non enseigné, non exercé | cas limite de la section « قطبا المغنط » + question |
| A5 | manuel p.131 6-3 (tableau pôle de l'aiguille × pôle du barreau) et p.127 5-أ (quatre mélanges) non repris | `multi` + `multi`, `manuel` déclaré |
| A6 | formes : 100 % QCM | matching, short_answer, multi, ordering, deux matching sur rose, QCM sur figure |
| A7 | `chapter.json` : sources sans la fiche ni le guide | ajoutés |

### 11-effets-courant-electrique
| # | écart | traitement |
|---|---|---|
| B1 | **V3** : le cours ne donne que le nombre de spires ; le nombre de piles (guide p.174) absent ; « intensité » à ne jamais exiger | nouvelle section 7 « ce qui renforce l'électroaimant » (spires ET piles), jamais le mot « intensité » |
| B2 | § 1.7 n° 6 « المصباح لا يضيء إلا بخليّة » : ni `::: piege` ni distracteur | piège dans la section 1 (le générateur n'est pas toujours une pile : dynamo de vélo, manuel p.139) + question |
| B3 | حاجز p.182 « confusion lumière / courant électrique » (et « le courant ne sert qu'à éclairer ») : seul le second est piégé | phrase ajoutée au piège de la section 2 + question |
| B4 | V1 : rapport 2 : 1 des volumes (guide p.170) absent | encadré « للاستزادة », jamais une clé |
| B5 | piège « deux facteurs à la fois » (démarche expérimentale) absent | piège de la section 7 + distracteur muet (id proposé) |
| B6 | manuel p.138 6-3 (deux bobines, laquelle attire plus) : en mots seulement | QCM sur figure SVG, `manuel` déclaré ; remplace 02-boss Q6 (même place, même difficulté) |
| B7 | formes : 100 % QCM | matching ×2, short_answer ×2, multi, ordering |
| B8 | `chapter.json` : fiche et guide p.170–175/182 absents des sources | ajoutés |

### 08-poids
| # | écart | traitement |
|---|---|---|
| C1 | tableau masse/poids du manuel p.145 (remise en ordre) : jamais sous forme native ; propriété « عامل خارجيّ » (manuel p.145, guide p.180) absente du tableau du cours | ligne ajoutée au tableau + étape de l'exemple + `multi` repris |
| C2 | manuel p.144 6-1 : quatre dessins d'Ahmed (chute oblique) à corriger | QCM sur figure SVG (4 vignettes), repris et déclaré |
| C3 | **V1** : Lune = 1/6 (guide p.180) | encadré « للاستزادة », jamais une réponse |
| C4 | poids qui diminue avec l'éloignement (manuel p.144 6-3) : question de choix, pas d'ordre | `ordering` de trois situations |
| C5 | formes : 100 % QCM | numeric, short_answer, multi, ordering, figure |
| C6 | manuel p.144 7 (satellite / fusée) : explication du manuel simpliste (orbite) | **non reprise**, signalée à l'auditeur |
| C7 | `chapter.json` : sources | fiche et guide p.177–180 ajoutés |

## Ce qui a été fait

- **07** : section 7 « وردة الرياح : ثماني جهات » (ancrage, définition, figure SVG rose à 8 directions, exemple à 4 pas avec le procédé d'orientation du guide p.176, piège E/O, propriété avec cas limite « l'aiguille ne montre que le nord », `::: verifie`, `::: retenir`) ; cas limite de l'aimant cassé dans « قطبا المغنط » ; résumé : +1 puce, 1 puce complétée. 11 questions ajoutées (quiz 1, 01 : matching + libre, 02 : multi + QCM, 03 : multi + QCM sur figure, 04 : QCM, 05 : ordering + 2 matching sur la rose). `manuel` déclaré sur 02 (p.131), 03 (p.127), 05 (p.134).
- **11** : piège § 1.7 n° 6 (section 1), phrase « lumière ≠ courant » (section 2), encadré V1 (section 4), section 6 recentrée sur « temporaire », **section 7 neuve** « ما الّذي يقوّي المغنط الكهربائيّ؟ » (spires ET piles, piège « deux facteurs à la fois »), jamais « intensité ». 10 questions ajoutées + 1 remplacée (02-boss Q6, même rang, même difficulté) ; `manuel` déclaré sur 02 (p.138).
- **08** : ligne « من أين يأتي؟ » du tableau + étape 5 de l'exemple + question de la méthode ; « عن بعد » (lien avec l'aimant) ; encadré V1 (Lune ≈ 1/6) ; 7 questions ajoutées ; `manuel` déclaré sur 02 (p.144–145).
- `chapter.json` des trois : `sources[]` + fiche (§ cités) + guide 503604 ; `description` de 07 et 11 complétée ; `coursePitfalls` inchangés (aucun id nouveau).
- **Défaut de rendu trouvé et corrigé** : cinq `**gras**` coupés par un retour à la ligne (le moteur rend les `**` en clair) — trois en 07 (dont un à moi), un en 11, un en 08 ; les lignes ont été rejointes.
- Gates : `content:check` ✓ · `content:qa` 0 avertissement sur le sujet · `content:figures:check` ✓ · `content:tranche --strict-longest` ✓ (clé la plus longue 0/12, paires proches 0, patron 0 en recul) · prettier ✓ · rendu `renderLesson`/`renderSummary` (ar) : aucun `*`, `_`, `:::` résiduel.
