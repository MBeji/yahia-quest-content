# Gisement 9ᵉ × arabe — plan des missions d'examen (G3–G4, étude 36)

Écrit le 2026-10-14 par le planificateur. Entrées : les 12 sujets lus (C01–C12, 2020–2026, 118
lignes), le contenu de `content/arabic/` (identique à `main`), le manifeste `9eme-base.json`.
Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-9eme-base-arabic/fiche.md` § 3 ;
- plan : [`plan-examens-v1.json`](./plan-examens-v1.json) (32 missions, 5 lots) ;
- registre : `…/web-9eme-base-arabic/gisement.json` — C01–C12 passés à `lu` (`transcription: "versionnee"`),
  32 missions `planifiee` (id `m001`…`m032`, comme le plan) ;
- affectations : [`assign-arabe-L01.md`](./assign-arabe-L01.md) … [`assign-arabe-L05.md`](./assign-arabe-L05.md).

## 1. Règles retenues

**R1 — L'unité est la question officielle (السّؤال), pas la partie imprimée.** En arabe, une partie
du sujet n'est pas un exercice cohérent comme en maths : « ❖ الوعي بنظام اللّغة » aligne six
questions à 1 point sur six leçons différentes ; « الأسئلة » de la technique mêle compréhension et
langue. Placer une partie entière au chapitre « le plus avancé » l'enverrait au 13 ou au 14 (le
diminutif, la relation) — un non-sens pour l'élève. La règle du chapitre le plus avancé s'applique
donc **à chaque question**, puis les questions se regroupent en missions :

- **Compréhension** (questions de la partie ❖ الفهم وبناء المعنى, ou premières questions de
  « الأسئلة » en technique, avis compris) : **une mission par texte, au chapitre 10**. Les questions
  d'un texte ne se séparent pas : elles ne se lisent qu'avec lui. 11 textes → 11 missions.
- **Langue** : chaque question va au chapitre de sa notion (le plus avancé du manifeste si elle en
  mêle deux ; `01` et `06`, chapitres de révision hors manifeste, comptent comme antérieurs à tous) ;
  dans un chapitre, les questions de **toutes les sessions** se regroupent en une mission (deux au
  05, qui en a trop). C'est le seul moyen d'atteindre 6 à 12 questions : une question de langue
  vaut 1 à 3 items. 14 missions.
- **Production** : chapitre 09 (R3).

**R2 — Taille 6 à 12 questions.** Une sous-question à plusieurs gestes se découpe en deux ou trois
questions fermées (former, vocaliser, justifier la règle, employer), toujours sur les phrases de la
session. Quand une source reste trop courte (`04`, `19`, compréhension 2024 technique), on complète
par des questions **fidèles au même texte officiel** et à une consigne de même type que celles du
sujet — jamais par une matière d'ailleurs. La colonne `etapes` du plan est ce nombre de questions visé.

**R3 — La production écrite se convertit en préparation fermée, elle ne s'écarte pas.** Elle vaut
la moitié de la note (10/20 en générale, 6/20 en technique) et le chapitre 09 n'a **aucune**
question sur une consigne d'examen (fiche § 3.3). On reprend la consigne officielle telle quelle,
puis des questions fermées sur ce qui se décide avant d'écrire : la tâche exacte (réfuter, nuancer,
blâmer et convaincre, dialogue, billet), la thèse à rejeter et celle à défendre, l'argument pertinent
contre l'argument hors sujet ou favorable à la thèse adverse (`multi`), l'exemple adéquat, le
connecteur, l'ordre du plan (`ordering`), la conclusion. Rien n'y note la rédaction.
- générale (2020, 2023–2026) : une mission par sujet — 5 missions ; chacune a une **opération
  différente** (dialogue et solutions ; nier et convaincre ; blâmer ; nuancer ; réfuter et montrer
  les dangers), ce qui évite le gabarit répété d'une mission à l'autre ;
- technique : sept paragraphes de même moule → **deux missions groupées** (2020–2022, 2023–2026),
  deux ou trois questions par sujet. Sept missions identiques de forme seraient des gabarits.
- Les **avis justifiés** des compréhensions suivent la même conversion : choisir la justification
  la plus solide, l'argument qui appuie une position nuancée, l'avis que le texte permet de défendre.

**R4 — HP (décision de l'orchestrateur).** Une question entièrement `HP:` n'est pas placée
(13 questions, toutes en technique, § 3). Dans une question mêlée, la partie `HP` ne donne aucun
item ; si la partie au programme en dépend (accord du duel au `01`), sa forme se donne dans
l'énoncé (« on admet… ») et l'item porte sur ce que le chapitre enseigne (signe de déclinaison).

**R5 — Pas de « سبر » complet au chapitre 11.** Toutes les questions des sujets sont déjà placées
(R1) : un sujet complet en reprendrait les items mot pour mot — doublons au contrôle « paires
proches » et pour l'élève. Le mode examen et le donjon composent déjà des épreuves mêlées à partir
des chapitres. Le 11 garde ses trois sujets types.

**R6 — Étage.** Celui de la ligne la plus haute de la mission (comme `plan-builder.ts`), sauf la
production générale, ramenée de d4 à **d3** une fois convertie (on n'écrit plus), hormis 2025
(nuancer : la distinction la plus fine) gardée **d4**. Bilan : 15 d2, 16 d3, 1 d4.

## 2. Missions par chapitre

| chapitre | missions | fichiers (NN = displayOrder) | sources |
| --- | --- | --- | --- |
| `10-fahm-wa-intaj` | 11 | 07–17 | compréhension des 11 textes (2020–2026, sauf 2020 générale, sans texte) |
| `09-al-intaj-al-kitabi` | 7 | 07–13 | 5 productions générales + 2 missions groupées de la technique |
| `05-sarf-al-mizan` | 2 | 07–08 | 2024 + 2026 ; 2022 T + 2023 + 2025 |
| `16-al-istifham` | 1 | 06 | 2023, 2024, 2025, 2026 (5 questions) |
| `17-ash-shart` | 1 | 06 | 2023 (2 questions), 2024, 2025, 2026 |
| `18-dalalat-az-zaman` | 1 | 06 | 2022 T, 2025, 2026 |
| `15-al-alaqat-bayna-al-jumal` | 1 | 06 | 2024 (2 questions), 2025 |
| `12-al-maqsur-wal-manqus-wal-mamdud` | 1 | 06 | 2025, 2026 |
| `13-at-tasghir` | 1 | 06 | 2025, 2026 |
| `14-an-nisba-wal-masdar-as-sinai` | 1 | 06 | 2023, 2024 (dont la partie النّواسخ de 2024) |
| `19-al-adad-wal-madud` | 1 | 06 | 2025 |
| `04-al-asalib` | 1 | 07 | 2022 T |
| `03-al-mansoubat` | 1 | 07 | technique 2020–2026 (7 questions, parties `HP` retirées) |
| `06-al-mushtaqqat` | 1 | 07 | technique 2024–2026 |
| `01-i3rab-wal-bina` | 1 | 07 | technique 2021, 2023, 2026 |
| `02`, `07`, `08`, `11` | 0 | — | `02` : sa seule question (2024) est placée au 14 avec la partie qui l'accompagne ; `07`, `08` : jamais interrogés ; `11` : R5 |

**32 missions, environ 233 questions.**

## 3. Lots

| lot | chapitres (NN) | missions | parallélisme |
| --- | --- | --- | --- |
| L01 | `10` (07–12) : compréhension générale 2023–2026 + technique 2025–2026 | 6 | avec L03, L04, L05 |
| L02 | `10` (13–17) : compréhension technique 2020–2024 | 5 | **après L01** (même chapitre, un auteur à la fois) |
| L03 | `09` (07–13) : production convertie | 7 | avec L01, L04, L05 |
| L04 | `15` (06), `04` (07), `16` (06), `17` (06), `18` (06), `03` (07), `19` (06) — نحو | 7 | avec L01, L03, L05 |
| L05 | `12` (06), `05` (07–08), `13` (06), `14` (06), `06` (07), `01` (07) — صرف et révision | 7 | avec L01, L03, L04 |

Quatre auteurs en parallèle (L01, L03, L04, L05), puis L02. Skill à charger : `prof-arabe-9eme`
(puis `content-ecole-tn`) ; consigne `gisement-auteur-examen.md` (reprise citée).

**Pour les prompts d'auteur** (à reprendre du modèle SVT, adaptés) :
- titre : celui de la ligne d'affectation, suivi des étoiles de l'étage ; en-tête d2 practice 75/15,
  d3 boss 120/30, d4 challenge 300/60 ;
- chaque question d'une mission multi-sessions **dit sa session** dans l'énoncé (« مناظرة 2025 ») et
  redonne la phrase officielle qu'elle travaille ; les textes longs se citent par extrait, avec la
  référence de l'auteur telle qu'imprimée ;
- types natifs attendus là où la consigne l'appelle : `matching` (« صِلْ »), `ordering` (« قسّم
  النّصّ », plan d'une production), `multi` (« اختر ثلاث كلمات », arguments pertinents),
  `short_answer` seulement pour une forme courte et unique (un diminutif, un schème), avec ses
  `acceptedAnswers` vocalisées et non vocalisées ;
- `chapter.json`, `sources[]` : « Sujets officiels de l'examen national de fin d'études de
  l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36)
  — transcriptions : programmes-officiels/examens-nationaux/9eme-base/arabic/ » ;
- la vocalisation et les graphies se reprennent telles que transcrites (dont « نطرقع », 2023 T) ;
  une coquille d'origine se signale au rapport, elle ne se corrige pas en silence ;
- registre des étiquettes d'erreur : vérifier sur `origin/main` qu'une famille arabe existe avant
  d'étiqueter ; sinon distracteurs muets et erreurs décrites au rapport.

## 4. Ce qui est écarté, et pourquoi

| écarté | quoi | pourquoi |
| --- | --- | --- |
| 13 questions entièrement `HP` | C02 Q5 ب, Q6 ب ; C04 Q5, Q6 أ ; C06 Q4, Q5 ; C08 Q5 ج, Q6 أ ; C09 Q5 أ, Q6 ب ; C10 Q3 ب ; C12 Q3 أ, Q3 ب (numéros de la partie « الأسئلة ») | acquis de 7ᵉ–8ᵉ (compléments absolu et de but, pluriels, conjugaison et accord avec les pronoms, passif, prépositions, adjectif) qu'aucun chapitre de 9ᵉ n'enseigne — décision de l'orchestrateur |
| parties `HP` de 8 questions mêlées | compléments absolu et de but dans les consignes « أثرِ / أغنِ » (03) ; accord du verbe, du relatif et des pronoms au duel (01) | même règle ; la partie au programme reste un item |
| l'étiquette `07` de 2024 Q1.3 (générale) | la phrase finale symbolique | le 07 vient après le 10 au manifeste : la question se garde en compréhension (le sens), sans nommer de figure |
| un « سبر » complet au 11 | — | R5 : doublons |
| rien de la générale 2020 | — | son seul sujet (dialogue argumentatif, format ancien « الإنشاء العربي ») est **placé** au 09 : le cours y enseigne le dialogue argumentatif encadré par le récit |
| sessions 2002–2019 (C13–C40), devoirs D01–D06 | non lus | hors du périmètre de cette passe (l'orchestrateur a fixé les 12 sujets 2020–2026) ; ils restent `echantillon` au registre |

## 5. Arbitrage

Aucun de fond. Les deux choix les plus engageants sont tranchés ici et réversibles par lot :
la conversion de la production (R3 — si le propriétaire préfère l'écarter, L03 tombe sans toucher
aux autres lots) et le regroupement de la langue par notion sur plusieurs sessions (R1).
