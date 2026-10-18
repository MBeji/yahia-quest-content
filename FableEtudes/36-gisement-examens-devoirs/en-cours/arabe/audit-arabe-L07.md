# Audit L07 — arabe 9ᵉ, devoir en salle blanche (carte D02#11 + D02#12)

Auditeur indépendant. Périmètre : `content/arabic/12-al-maqsur-wal-manqus-wal-mamdud/exercices/07-devoir-al-ism-al-manqus.json`
(arbre `/home/user/wt-ar2`, branche `wip/gisement-arabe-9eme-anciennes`, commit `11f2f8c5`), et la ligne `sources[]`
de `12/chapter.json`. Chapitres 09 et 10 ignorés. Notes des auteurs non ouvertes.

Grille : `prompt-arabe-auditeur-v2.md` → `francais/prompt-francais-auditeur.md` → `content-ingest/references/gisement-auditeur.md`,
skills `content-audit` puis `prof-arabe-9eme`. Références : `12/cours.md` (§ « الاسمُ المنقوصُ — ياءٌ تَظهرُ وتَختفي »,
§ « أشتقُّ بحسبِ المطلوبِ »), `06/cours.md` (§ اسم الفاعل, § اسم المفعول), missions publiées du 12 (01–06), quiz du 12,
`06/07` (`m031`), libellés `arabe.*` sur `origin/main:content/misconceptions.json`.

## 0. Contrôles outillés

| contrôle | résultat |
|---|---|
| `content:gisement:controle -- --sources …/devoirs-snapshots/arabic <fichier>` | 7 textes contrôlés ; plage ≥ 8 mots : 0 ; ≥ 6 mots : 0 ; données communes : 0. ✓ |
| `content:check` | 0 erreur (120 matières validées) |
| `content:qa:strict` | 0 erreur ; aucun avertissement sur `arabic/12` |
| `content:tranche -- --subject arabic --chapters 12` | clé strictement la plus longue 0/42 ; positions équilibrées ; paires proches 0 ; gabarits 0 |
| normalisation du moteur (`normalizeRecallText`, réplique TS du SQL) | voir § 2 |

## 1. Re-résolution à l'aveugle

| Q | type · étage | ma réponse | clé du fichier | verdict | motif |
|---|---|---|---|---|---|
| 1 | short_answer · d2 | بانٍ | بانٍ | OK, réserve (m) | nakira au génitif après بـ : la ya tombe. Réserve : « ببانٍ » refusé (voir m-4) |
| 2 | mcq · d2 | a | a | **réserve (M)** | clé juste, distracteurs faux. Mais c'est une question déjà posée : la clé réunit celle de `12/01` Q6 et celle de `12 quiz` Q4, deux questions de la liste « ne pas redemander » (M-1) |
| 3 | matching · d3 | l1-غازٍ, l2-غازيًا, l3-الغازي, l4-الغازيَ | idem | OK, réserve (m) | appariement unique (seul r2 porte la fatha). L'explication emploie « مقدَّرة », terme que le cours range « خارج كتاب التّاسعة » (m-2) |
| 4 | short_answer · d3 | مُهتدٍ | مُهتدٍ | **réserve (M)** | clé juste. Erreur de vocalisation dans l'énoncé : « اشتُقَّ اسمَ » (M-2). Normalisation : voir § 2 |
| 5 | mcq · d3 | b | b | OK, réserve (m) | plan 2×2 propre (c a deux erreurs et ne porte pas d'étiquette ; votes 2/2 sur chaque moitié ; quatre options de 36 caractères). Le distracteur a n'a pas d'étiquette (voir § 4). Même gabarit que le `verifie` du cours (« اكتفى ») (m-3) |
| 6 | multi · d3 | a, d, f | a, d, f | **réserve (M)** | clé juste. Doublon de fait de Q5 : même règle, kasra pour le participe actif donc manqus, fatha pour le passif donc maqsur. L'explication de Q5 résout Q6. « مُعطٍ / مُعطًى » (schème أفعل) donne aussi par analogie Q7 (« مُلقٍ / مُلقًى »). Racine د ع و de « المُستدعِي » = celle du mot du devoir (M-3) |
| 7 | mcq · d3 | a | a | **réserve (M)** | clé juste. Le distracteur c « رأينا مُلقيٍ بارعٍ » s'élimine sur l'adjectif au génitif après « رأينا ». Sa forme n'est ni l'erreur de l'étiquette, ni « la forme du génitif » que dit l'explication (le génitif est « مُلقٍ ») (M-4) |

**7 questions re-résolues, 0 clé fausse.** Les autres distracteurs sont tous faux et chacun exécute une erreur réelle.

## 2. Questions `short_answer` : normalisation du moteur

La normalisation retire tashkīl et tanwīn, puis remplace ى par ي, أ/إ/آ par ا et ة par ه. Elle a été vérifiée par script sur
`src/shared/content/free-answer.ts`, miroir de `public.normalize_recall_text`.

| saisie | forme normalisée | Q1 (clé « بان ») | Q4 (clé « مهتد ») |
|---|---|---|---|
| بانٍ / بان / بانٌ | بان | accepté | — |
| باني | باني | refusé, diagnostiqué `manqus-ya` ✓ | — |
| بانًا | بانا | refusé | — |
| ببانٍ | ببان | **refusé** (juste, mais la consigne interdit la préposition) | — |
| مُهتدٍ / مُهْتَدٍ / مهتد / مُهتدٌ | مهتد | — | accepté |
| مُهتدي / مهتديٌ | **مهتدي** | — | refusé, `manqus-ya` ✓ |
| **مُهتدًى** | **مهتدي** | — | refusé, mais **diagnostiqué `manqus-ya`** |
| مُهتدًا | مهتدا | — | refusé |

- **Aucune réponse juste n'est refusée**, sauf « ببانٍ » au Q1 : la consigne exclut la préposition, mais la forme est juste.
- **Aucune réponse fausse n'est acceptée pour ce que la question teste**, la présence de la ya. Un tanwīn de mauvaise voyelle
  (« بانٌ » au génitif, « مُهتدٌ ») passe, parce que le moteur ne voit pas le tanwīn. C'est une limite connue et assumée du
  moteur, pas un défaut du fichier.
- **Cas signalé : « مُهتدًى » et « مُهتدي » se normalisent tous deux en « مهتدي ».** Les deux sont refusés, la clé reste donc
  sûre. En revanche, l'élève qui a formé le participe passif est diagnostiqué « tu as gardé la ya ». Son erreur réelle est
  celle de `arabe.ishtiqaq.fa3il-maf3ul-ma3na`. Le fichier ne peut pas le corriger : `content:qa` refuse deux
  `expectedMistakes` qui se normalisent en une même forme. Il ne faut pas non plus le dire dans l'explication : citer
  « مُهتدًى اسمُ مفعولٍ مقصورٌ » donnerait Q5 et Q6 en avance (Q4 précède Q5 dans l'ordre d'émission). Décision : on garde
  l'étiquette `manqus-ya`, qui couvre l'erreur dominante, et on consigne que la télémétrie de Q4 mêle les deux erreurs (m-5).
- La carte demandait des `acceptedAnswers` vocalisés et non vocalisés. Ils seraient superflus : la normalisation rend déjà
  les deux équivalents. Leur absence n'est pas un défaut.

## 3. Points demandés en plus de la grille

**Salle blanche.** Le contrôle outillé donne 0 partout. La comparaison à la main avec `D02.txt` porte sur les lignes 5ب (« الداعين » au
singulier, au duel, au singulier indéfini) et 5ج (les participes de « يضاهي » et leur classe). Le fichier ne reprend ni ces mots
ni le thème du texte (un entretien sur l'émancipation des femmes). Il ne reprend pas non plus le duel, et son schème n'est jamais
مُفاعِل. Les contextes (village, champ, salle) sont inventés. Seul rapprochement : « المُستدعِي » (Q6) a la même racine
د ع و que « الداعين ». Le mot n'est pas repris, mais le correctif M-3 l'écarte de toute façon. Le geste de 5ج (participe actif manqus,
participe passif non manqus) est celui de la carte, ce qui est attendu en T2′. **Conforme.**

**Participe passif des verbes augmentés, enseigné au 06 et au 12 : oui.**
- `06/cours.md` § اسم الفاعل : « من غير الثلاثيّ بضمّ أوّله وكسر ما قبل آخره ». § اسم المفعول : « بضمّ أوّله و**فتح** ما
  قبل آخره », avec la mise en garde « فرق حركة واحدة » (مُكرِم / مُكرَم).
- `12/cours.md` § « أشتقُّ بحسبِ المطلوبِ » : on y lit « اسمُ المفعولِ من «التقى» … مُلتقًى », « مُلتقٍ » (actif) manqus contre
  « مُلتقًى » (passif) maqsur, avec ce piège : « كسرةٌ للفاعلِ فيصيرُ منقوصًا، وفتحةٌ للمفعولِ فيصيرُ مقصورًا ». Le `verifie`
  « اكتفى ← مُكتفٍ / مُكتفًى » y est aussi.
- Le 06 vient après le 12 dans l'ordre d'affichage (révision hors du livre de 9ᵉ), mais le 12 enseigne lui-même la notion. Rien
  n'est donc testé sans avoir été enseigné. Remarque sans suite : « ارتقى » est intransitif, et en toute rigueur on dit
  « مُرتقًى إليه ». Le cours fait pourtant de même avec « التقى » et « اكتفى ». Le fichier suit son cours, ce n'est pas un défaut.

**Liste « ne pas redemander ».**
- `m026` (12/06 : duel et pluriel) : respecté. `m031` (06/07) et patron 06 (participes de verbes sains) : respecté, le participe
  ne sert ici qu'à arriver au manqus.
- 12/01 Q1 (reconnaître un manqus parmi des mots) : respecté, Q6 travaille sur des dérivés.
- 12/03 Q1 (définition) et Q5 (racine de « ساهٍ ») : respectés.
- 12/05 Q3 (« وقى ← واقٍ », nakira au nominatif) : réserve légère. Q4 refait le dernier geste (nakira au nominatif), mais à partir d'un verbe
  **augmenté** et en réponse libre, comme la carte le demande. Accepté.
- 12/05 Q5 (le test de « أل ») : respecté. Le test n'apparaît que dans les explications.
- **12/01 Q6 et 12 quiz Q4 : NON respectés par Q2** → M-1.

## 4. Étiquettes

| question / option | étiquette | verdict |
|---|---|---|
| Q1 mistake « باني » | `arabe.ishtiqaq.manqus-ya` | exacte : ya gardée au génitif indéfini d'un nom d'agent |
| Q4 mistake « مُهتدي » | `arabe.ishtiqaq.manqus-ya` | exacte (avec la confusion de télémétrie du § 2) |
| Q5 d (les deux maqsur) | `arabe.manqus.maqsur-bi-hadhf-ya` | exacte : « مُرتقٍ » pris pour un maqsur parce que la ya ne se voit pas |
| Q5 a (les deux manqus) | — | **à étiqueter `arabe.sinf.akhir-khalt`** (voir ci-dessous) |
| Q5 c | — | muette, à raison : elle cumule les deux erreurs |
| Q7 b « مُلقيٌ » | `arabe.ishtiqaq.manqus-ya` | exacte : ya gardée au nominatif indéfini |
| Q7 c | `arabe.ishtiqaq.manqus-ya` | **inexacte en l'état** (« مُلقيٍ » n'est aucune des deux branches du libellé). Exacte après M-4 (« مُلقٍ » à l'accusatif = « tu l'enlèves à l'accusatif ») |
| Q7 d « مُلقًى » | `arabe.ishtiqaq.fa3il-maf3ul-ma3na` | acceptable. `arabe.ishtiqaq.mazid-haraka-al-3ayn` (« la voyelle avant la dernière lettre décide ») serait plus précise pour un verbe augmenté (m, facultatif) |
| Q3 matching, Q6 multi | aucune | conforme : pas d'étiquette sur `matching` et `multi` |

**Étiquette proposée par l'auteur, « croire manqus le participe passif d'un verbe défectueux » : REJET.**
- *Règle des 3 questions distinctes.* Une seule question exécute cette erreur sous forme d'option étiquetable : Q5 a. Q6 est un `multi`
  et n'admet pas d'étiquette. Q7 d exécute une autre erreur : prendre la forme passive pour le participe actif, c'est-à-dire
  confondre agent et patient. Ailleurs dans le corpus, `12/05` Q4 a (« مُلتقٍ » donné pour le passif) est déjà étiqueté
  `fa3il-maf3ul-ma3na`, et c'est la confusion des deux formes, pas la croyance visée. Total : 1 question, loin des 3 exigées.
- *Doublon d'une étiquette existante.* L'élève qui classe « مُرتقًى » parmi les manqus juge d'après le verbe (défectueux) et
  non d'après la fin du mot. C'est l'erreur exacte de `arabe.sinf.akhir-khalt` : « تخلطُ بين أصنافِ الآخِرِ: ألفٌ ثابتةٌ ←
  مقصورٌ، ياءٌ مسبوقةٌ بكسرٍ ← منقوصٌ … فانظرْ إلى الآخِرِ لا إلى المعنى ». Elle est déjà employée au 12 (01 Q1).
- **Correctif** : ajouter `"misconceptionTag": "arabe.sinf.akhir-khalt"` à l'option a de Q5. Aucun texte fr/en/ar nouveau.

## 5. Défauts classés et correctifs

Les textes de remplacement ci-dessous ont été vérifiés : longueurs sans diacritiques mesurées par script, votes option par option,
prémisses gardées, aucune fuite vers une question suivante. Le texte est arabe sans chiffres et le rendu bidi ne pose pas
de problème.

### Critique
Aucun.

### Majeurs

**M-1 · Q2 — question de la liste « ne pas redemander ».** La clé (« في الأولى نصبٌ فثبتت الياءُ وظهرت الفتحةُ، وفي الثانيةِ
رفعٌ لنكرةٍ فسقطت الياءُ ») réunit les clés de `12/01` Q6 (« رأيتُ قاضيًا » : la ya reste parce que nasb, fatha visible) et de
`12 quiz` Q4 (« جاء قاضٍ » : nakira au nominatif). Le distracteur b (« selon que le mot est فاعل ou مفعول ») est la variante
du distracteur a de 01 Q6 (« رأى متعدٍّ ») et du distracteur d du quiz Q4 (« جاء يقتضي »). Les cases nasb indéfini et raf'
indéfini sont en outre déjà travaillées par Q3 (l2), Q4 et Q7. **Correctif : supprimer Q2.** Le fichier passe à 6 questions,
le minimum de `prof-arabe-9eme` pour un boss d3. La rampe 2→3 reste assurée par Q1 (d2). Je n'ai trouvé aucune question de
remplacement qui ne redemande une case déjà prise par Q3 ou un item publié (12/02 Q4, 12/03 Q6). Si l'orchestrateur tient
aux 7 questions de la carte, il faut un geste neuf, à commander à l'auteur.

**M-2 · Q4 — vocalisation fautive.** « اشتُقَّ اسمَ الفاعلِ » mélange un passif et un complément à l'accusatif. Il faut
l'impératif, celui du cours (« اشتقَّ اسمَ مكانٍ … »). Prompt →
« اشتقَّ اسمَ الفاعلِ من الفعلِ «اهتدى»، واكتبْه نكرةً في حالةِ الرفعِ. »
Q5 et Q7 (« اشتُقَّ … اسمُ ») sont justes : passif suivi du nominatif.

**M-3 · Q6 — doublon de fait de Q5, avec fuite en avant (Q5 précède Q6 en d3, tri stable) et fuite vers Q7.** Remplacer la
question entière (garder `type: multi`, `difficulty: 3`) :

- prompt : « اخترِ الأفعالَ التي يكونُ اسمُ الفاعلِ منها اسمًا منقوصًا. »
- options : a « «استقصى» » · b « «استقامَ» » · c « «نجا» » · d « «اشتدَّ» » · e « «انتصرَ» » · f « «اشترى» »
- answerKey : `{"correct": ["a", "c", "f"]}`
- explanation : « يكونُ اسمُ الفاعلِ منقوصًا إذا كان الفعلُ ناقصًا، أي آخرُه حرفُ علّةٍ: «استقصى» ← مُستقصٍ، و«اشترى» ←
  مُشترٍ، و«نجا» ← ناجٍ؛ فألفُ «نجا» في آخرِه، والصنفُ يُقرأُ من آخرِ الناتجِ لا من رسمِ الفعلِ. أمّا «استقامَ» فحرفُ العلّةِ
  في وسطِه، فاسمُ الفاعلِ منه مُستقيمٌ آخرُه ميمٌ؛ و«اشتدَّ» مضاعفٌ ← مُشتدٌّ، و«انتصرَ» صحيحُ الآخِرِ ← مُنتصِرٌ، فلا منقوصَ
  فيها. »

Vérifications. Clé juste : مُستقصٍ, مُشترٍ, ناجٍ sont manqus ; مُستقيم, مُشتدّ, مُنتصِر ne le sont pas. Les options font 5 à 8
caractères et la clé n'est pas la plus longue de façon répétée (« «نجا» » est la plus courte). Deux options par schème
(استفعل : a/b ; افتعل : d/e/f), donc le schème ne désigne pas la clé. Deux pièges qui n'existaient pas : la ya de
« نجا » s'écrit alif, et « استقام » (أجوف) a sa lettre faible au milieu. Avec 3 bonnes réponses sur 6, le nombre ne se devine pas. Le passif
n'y figure plus, ce qui supprime le doublon avec Q5 ; il reste traité par Q5 et Q7 d. Aucune option n'est de schème أفعل, donc
plus de fuite par analogie vers « ألقى ← مُلقٍ » (Q7). Le root د ع و disparaît. « استقصى » et « مضاعف » sont des mots du cours
(12 § أشتقّ ; 7ᵉ–8ᵉ). Pas d'étiquette, puisque c'est un `multi`.

**M-4 · Q7 — distracteur c éliminable à vue, étiquette inexacte, explication fausse sur ce point.** « رأينا مُلقيٍ بارعٍ »
porte un adjectif au génitif après un verbe transitif, ce qui le fait tomber sans réfléchir au manqus. « مُلقيٍ » n'est pas
non plus « la forme du génitif » que décrit l'explication. Remplacer :
- c → « رأينا مُلقٍ بارعًا في القاعةِ الكبرى » (`arabe.ishtiqaq.manqus-ya`, ya supprimée à l'accusatif : seconde branche du libellé) ;
- d → « وقفَ أمامَنا مُلقًى بارعٌ في القاعةِ الكبرى » (`arabe.ishtiqaq.fa3il-maf3ul-ma3na` gardée). Ce changement casse le vote :
  avec le seul c corrigé, « استمعنا إلى » (a, d) et « مُلقٍ » (a, c) désignaient a ;
- a et b inchangés ;
- explanation → « اسمُ الفاعلِ من «ألقى» يُصاغُ من المضارعِ «يُلقي» بميمٍ مضمومةٍ وكسرِ ما قبلَ الآخِرِ: مُلقِي، وهو منقوصٌ.
  وبعدَ حرفِ الجرِّ هو نكرةٌ مجرورةٌ، فتسقطُ ياؤُه ويبقى التنوينُ: مُلقٍ. وإبقاءُ الياءِ في الرفعِ خطأٌ، فالنكرةُ المرفوعةُ
  تُحذفُ ياؤُها كالمجرورةِ؛ وحذفُها في النصبِ خطأٌ أيضًا، فالمنصوبةُ تثبتُ ياؤُها وتظهرُ عليها الفتحةُ: رأينا مُلقيًا بارعًا.
  أمّا الصيغةُ التي فتحت ما قبلَ الآخِرِ فهي اسمُ المفعولِ، وهو مقصورٌ لا يؤدّي معنى الفاعلِ. »

Vérifications. Longueurs sans diacritiques : a 37, b 30, c 32, d 37. La clé n'est pas *strictement* la plus longue (égalité
avec d). Votes : le cadre est différent pour chaque option ; la forme « مُلقٍ » est en a et c ; le cas nominatif est en b et d.
Aucun vote ne désigne a. Une seule réponse juste. Q7 est la dernière question dans l'ordre d'émission, son explication ne fuit
donc vers aucune question suivante.

### Mineurs

- **m-1 · `chapter.json` — ligne `sources[]` absente.** `gisement-auteur-devoir.md` § chapter.json impose d'ajouter
  « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-9eme-base-arabic/fiche.md »
  (même forme qu'en math, français et anglais). Le fichier n'est pas modifié sur la branche.
- **m-2 · Q3 explanation — terme hors du livre.** Remplacer « في الرفعِ ← الغازي بضمّةٍ مقدَّرةٍ على الياءِ » par
  « في الرفعِ ← الغازي، ولا تظهرُ الضمّةُ على يائِه ». Le cours range « مقدّرة » dans un encadré « خارج كتاب التّاسعة … دونَ أسئلةٍ عليها ».
- **m-3 · Q5 — même gabarit que le `verifie` du cours** (« اكتفى ← مُكتفٍ / مُكتفًى، صنّفْ »). Accepté : c'est le geste D02#12
  demandé, et Q5 donne les formes au lieu de les faire dériver. À noter pour le pilote, rien à changer.
- **m-4 · Q1 — « ببانٍ » refusé.** Optionnel : ajouter `"acceptedAnswers": ["ببانٍ"]`. La forme normalisée « ببان » ne
  correspond à aucune forme fausse (« بباني » reste refusé).
- **m-5 · Q4 — télémétrie qui mêle deux erreurs** (§ 2) : « مُهتدًى » est classé `manqus-ya`. Aucun correctif n'est
  possible dans le fichier. À consigner.
- **m-6 · Q7 d — étiquette plus précise disponible** (`mazid-haraka-al-3ayn`). Facultatif.
- **m-7 · Recoupements de case.** Le génitif indéfini est la clé de Q1, de Q3 l1 et de Q7. C'est assumé, car Q7 ajoute la
  dérivation et le piège du passif. Rien à changer.

### Divers vérifiés sans défaut

Titre « ⚔️ زعيم الفرض ⭐⭐⭐: الاسمُ المنقوصُ في الاستعمالِ » : au patron du chapitre, ne livre aucune clé. Étage : d3, `boss`,
120/30, `displayOrder` 7. Rampe 2 → 3. Les explications ne désignent aucune option par sa lettre ou sa place. Aucun chiffre,
aucune notation à rendre, aucune figure. La langue est correcte, hors M-2. Aucun « اكتب » de production convertie : les
« اكتبْ » de Q1 et Q4 sont des consignes de `short_answer` demandées par la carte. Indices de forme : Q5 a quatre options
de même longueur, Q2 a sa clé à 86 contre une option à 88.

## 6. Résumé

7 questions auditées, **0 clé fausse**, 0 critique, **4 majeurs** : Q2 redemande des items de la liste interdite (12/01 Q6 et
quiz Q4) ; Q4 « اشتُقَّ اسمَ » est mal vocalisé ; Q6 est un doublon de fait de Q5, avec fuite vers Q6 et vers Q7 ; le
distracteur c de Q7 s'élimine à vue et son étiquette et son explication sont inexactes. **7 mineurs**, dont la ligne
`sources[]` manquante et le terme « مقدّرة » dans une explication.

Salle blanche : conforme (0 au contrôle, aucun mot ni thème de D02 repris). La notion de participe passif des verbes augmentés
est enseignée au 06 et au 12. `short_answer` : aucune réponse juste refusée hors « ببانٍ », aucune réponse fausse acceptée
pour la ya. « مُهتدًى » et « مُهتدي » donnent tous deux « مهتدي » : ils sont refusés tous les deux, mais la télémétrie les
confond. Étiquette proposée par l'auteur : **rejetée** (1 question, pas 3 ; erreur déjà nommée par `arabe.sinf.akhir-khalt`,
à poser sur Q5 a).

**Verdict : à corriger avant publication.** M-1 à M-4, l'étiquette de Q5 a, m-1 et m-2. Il faut ensuite re-vérifier Q6 et Q7
dans leur nouvelle forme.
