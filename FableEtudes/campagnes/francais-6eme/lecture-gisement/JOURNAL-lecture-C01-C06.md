# Journal du lecteur — français 6ᵉ, lot pilote C01 à C06 (sessions 2026 à 2021, épreuve unique)

Étape G2. Premier lot : les conventions du § 0 valent pour les autres lots d'examens de la 6ᵉ (français). Lecture du
2026-10-19. Les six PDF sont des scans sans couche texte (`pdftotext` rend 4 octets) : lecture en vision, 150 DPI, une
fois par page. Les six sha256 des copies de `/tmp/claude-0/fr6g/src/` égalent ceux de `docs.json` et du registre
`gisement.json`. Aucune écriture git, rien sous `content/french-6eme/`, `gisement.json` intact.

## 0. CONVENTIONS FIXÉES (à reprendre par les autres lots)

Reprises de l'anglais 6ᵉ : créneau `concours`, compétences `-` (aucun registre), texte support jamais transcrit en entier
(référence imprimée, nombre de lignes, résumé neutre, une citation courte, « texte intégral : document officiel, sha256
au registre »), consignes, items et barèmes mot pour mot dans la transcription, coquilles imprimées conservées.

**Format de l'épreuve** : 1 h (« الحصة : ساعة »), coefficient 1, 20 points, 4 pages, un seul texte narratif (page 1, 28 à
38 lignes, source imprimée, souvent un dialogue ou un récit à la première personne). Quatre parties, toujours dans cet
ordre : Compréhension 6 + Grammaire 3 + Conjugaison 3 + Production écrite 8 (intitulée « Expression écrite » en 2025,
2024, 2023, 2022 et 2021, « Production écrite » en 2026). 2022 et 2021 numérotent I, II (Langue = Grammaire + Conjugaison),
III ; 2026 à 2023 n'ont pas cette numérotation. Chaque partie porte une case « Total … sur N ». Pas d'orthographe ni de
dictée : l'orthographe n'est testée qu'à travers l'accord dans les items de grammaire et de conjugaison.

**Grain des lignes** (une ligne = une question numérotée imprimée) :
- Compréhension : UNE ligne par question numérotée (n°1 à 4 ou 5) ; une question à sous-parties a/b reste UNE ligne ;
  les sous-questions n'ont pas de suffixe. Étapes = nombre de réponses à produire (ou d'items remplis).
- Grammaire puis Conjugaison : UNE ligne par question numérotée (3 + 3) ; un tableau à compléter est une ligne.
- Production écrite : UNE ligne, la dernière, barème 8.
- **n°exo = rang d'ordre dans l'épreuve** (compréhension 1…n, puis grammaire n+1…n+3, conjugaison n+4…n+6, production
  en dernier) ; le validateur exige un numéro unique par document. La numérotation imprimée (Grammaire 1-3, Conjugaison 1-3)
  est donc décalée. Total : 4 questions de compréhension → 11 lignes ; 5 questions → 12 lignes.
- **Barème** : le barème de question n'est imprimé qu'en 2024, 2022 et 2021 (« (1 point) » par question ou par sous-partie,
  additionné quand a + b : 1 + 1 = 2). Quand il n'est pas imprimé (2026, 2025, 2023), la colonne vaut `-` pour toutes les
  questions de compréhension et de langue ; la production vaut toujours 8. Les totaux de partie (6, 3, 3) sont imprimés
  dans tous les sujets et fixent le contrôle : 2024 = 1+1+2+2, 2022 = 1+1+1+2+1, 2021 = 1+1+1+2+1 en compréhension,
  1+1+1 en grammaire et en conjugaison.

**Chapitres** (jamais `HP:` seul sans notion nommée ; slugs dans l'ordre du manifeste, jetons HP après) :
- *Compréhension* : UN seul slug pour toutes les questions, celui du module dont relève le thème du texte (règle F4) :
  écrans et projet de classe → `02`, voyage et site à découvrir → `08`, animaux menacés et filets → `05`, handicap,
  opération, rééducation → `06`, club de théâtre → `07`, chat recueilli et partage → `04`. Une question de lexique
  (synonymes, contraires) ou d'avis personnel suit le texte et n'ajoute aucun chapitre de langue.
- *Production écrite* : chapitre du thème de la consigne, pas du type de récit ; la structure imposée (dialogue, description,
  réactions) n'ajoute rien (elle est dite à l'archétype). Elle coïncide donc avec le chapitre du texte de la session.
- *Grammaire et conjugaison*, item par item, cumul des notions testées :
  complément essentiel ou non essentiel `05`, de lieu `06`, de temps `07`, de manière `08` ; un tableau qui les nomme les
  cumule tous ; forme négative ne… plus/jamais `04` ; démonstratif et possessif `02` ; accord sujet-verbe `05` ;
  pronoms personnels sujets `01` ; adjectif épithète/attribut `03` ; accord de l'adjectif : `06` par défaut (modèles
  heureux/heureuse, mûr/mûre, fier/fière), `07` pour la consonne doublée (nul/nulle, neuf/neuve, gentil/gentille) ;
  verbes : le **temps** (présent, passé composé, futur) et les verbes en -er → `01` ; chaque verbe-type porte son chapitre
  (être/avoir `03`, finir et verbes en -ir `04`, prendre/mettre et dérivés `05`, aller/faire `06`, dire/lire/écrire `07`,
  vouloir/pouvoir et participe passé avec être `08`) ; impératif `02` (venir, dire, verbes en -er, 3ᵉ groupe usuel).
  On ajoute `01` quand le **temps** est l'objet (présent des verbes, passé composé de verbes réguliers, futur de verbes
  en -er) ; pas pour l'impératif ni pour une transformation sans changement de temps.
- **Jetons HP fixés (mots-clés)** : `HP:negation-personne` (« plus personne ne… », ⛔ au § 2.10 D) ; `HP:accord-tout`
  (tableau C) ; `HP:pc-pronominal` (passé composé des pronominaux, rencontré non enseigné) ; `HP:adjectif-if-ive`
  (alternance -if/-ive, tableau C). Autres jetons déjà fixés par la fiche à employer tels quels : `HP:pronom-complement`,
  `HP:imparfait`, `HP:passe-simple`, `HP:discours-indirect`, `HP:subordonnee`, `HP:prerequis-5e`, `HP:theme-hors-modules`.
  Un cas nouveau : le noter ici, au plus proche.

**Étages** (échelle du portail, aucun `d4`) : compréhension `d1` si coche ou relevé direct sans inférence (une seule fois,
2024 Q1) ; `d2` dès qu'il y a une justification, une inférence, un synonyme ou un contraire, un avis ; langue `d1`
pour une opération unique, `d2` pour une à trois réponses ou deux notions simples ; `d3` pour au moins trois réponses
mêlant au moins deux notions ; production écrite `d3`. Une question de négation par remplacement de l'adverbe est `d2`.

**En-tête de transcription** : `examen` = intitulé de `docs.json` suivi de l'intitulé arabe imprimé ; `matiere: Français` ;
`session` ; `filiere: unique` ; `consulte_le: 2026-10-19` ; `lecture: vision` ; fichier `<année>-unique.md`. Cases `[case]`,
pointillés `........`, mot souligné `__mot__`. Le texte support est résumé (voir ci-dessus) ; chaque item de langue,
lacunaire ou non, est un énoncé de consigne transcrit mot pour mot.

**Accents imprimés** : le sujet 2025 imprime « apparait », « disparait » (orthographe rectifiée, sans circonflexe) ;
transcrits tels quels.

## 1. Documents lus

| id | session | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | 2026 | 6b79ca9c3b6ef8793b6fe25b9808dd95e7a0e027239d0900662089297d1bcd89 (oui) | 4 | vision | 12 | `french/2026-unique.md` |
| C02 | 2025 | 2fd17f3288c78f1acc48206fa3dda244b58fe1c7afe541fd61325bd099f0999a (oui) | 4 | vision | 11 | `french/2025-unique.md` |
| C03 | 2024 | 83fb56f7080b0d47a115acf73ff8a4d3b4bf0db1fae8c5cf1ce0eb6fd83f827a (oui) | 4 | vision | 11 | `french/2024-unique.md` |
| C04 | 2023 | 32b0b845936e3c75f864a5667e0dd695ede5e76951979d7d2cc7e87a52b866c5 (oui) | 4 | vision | 11 | `french/2023-unique.md` |
| C05 | 2022 | e18c3afe3d547b68e31873825c1ad0489eb8ac74a03f4b89253171d596eae544 (oui) | 4 | vision | 12 | `french/2022-unique.md` |
| C06 | 2021 | 7bb4c022993f81f0b14a3db7ab7410d8581a9b3b98b892f12a7fc2fa29be2420 (oui) | 4 | vision | 12 | `french/2021-unique.md` |

Transcriptions sous `/home/user/wt-fr6b/content/programmes-officiels/examens-nationaux/6eme-base/french/`. Lignes :
`lines/C0{1..6}.tsv` + `.meta`. Validation : `content:gisement:lignes --subject french-6eme --grade 6eme-base` : 6 fichiers,
69 lignes, 69 valides, 0 fautive (manifeste de 8 chapitres). Aucun corrigé n'est publié : les transcriptions ne donnent
aucune réponse. Pas de snapshot hors git pour les examens (la transcription fait foi, le texte support seul n'est pas conservé).

## 2. Format par session

| session | texte (thème, module) | compréhension (6) | grammaire (3) | conjugaison (3) | production (8) |
| --- | --- | --- | --- | --- | --- |
| 2026 | défi sans écrans en classe (02) | 5 q. : cocher, 2 relevés de détails, lexique a/b, avis | compléments non essentiels ; forme affirmative ; démonstratif + adjectif | passé composé ; impératif pluriel ; présent et accord, sujet pluriel | récit ≥ 8 phrases, répliques, réactions |
| 2025 | visite d'un site maya (08) | 4 q. : vrai/faux + 2 détails, comparaison, lexique a/b, avis | tableau de 4 fonctions ; accord d'adjectifs ; possessifs et verbe au pluriel | présent « nous » ; futur imposé par « bientôt » ; passé composé | récit ≥ 8 phrases, gardien décrit, dialogue rapporté |
| 2024 | phoque et amitié (05) | 4 q. : 2 différences, 2 sentiments justifiés, lexique a/b, causes | compléments non essentiels ; changements de personne ; négation | pluriel au passé composé ; présent ; impératif | récit ≥ 8 phrases, émotions, court dialogue |
| 2023 | handicap et rééducation (06) | 4 q. : avant/après, 2 indices, lexique a/b, avis | complément de temps + manière ; changements ; accord Gaston | futur ; présent ; impératif | récit ≥ 8 phrases, réaction des camarades, dialogue |
| 2022 | club de théâtre (07) | 5 q. : oui/non + 2 indices, 1 phrase, réaction, lexique a/b, avis | tableau de 4 fonctions ; démonstratifs ; adjectifs au masculin | présent pluriel ; impératif ; futur | récit ≥ 8 phrases, projet de festival, dialogue |
| 2021 | chat adopté (04) | 5 q. : 1 phrase, idée, oui/non + 2 indices, lexique a/b, paroles | genre du sujet ; négation ; tableau de 4 compléments | futur ; passé composé ; vous au présent et futur | récit ≥ 8 phrases, dialogue avec un propriétaire |

La production demande toujours un récit d'au moins huit phrases avec dialogue ou répliques, parfois avec description
(2026 et 2025 : réactions ou gardien, 2024 : émotions, 2023 : réaction des camarades). La partie « Langue » n'a jamais
de question de vocabulaire ni de dictée ; les lexiques (synonymes, contraires) sont dans la compréhension (question a/b).

## 3. Notions par chapitre (69 lignes)

Nombre de lignes portant le chapitre : 01 : 12 ; 02 : 15 ; 03 : 5 ; 04 : 13 ; 05 : 19 ; 06 : 16 ; 07 : 11 ; 08 : 13.
Compréhensions et productions : 02 (2026), 08 (2025), 05 (2024), 06 (2023), 07 (2022), 04 (2021) ; chaque chapitre est
représenté une fois, `03` n'a jamais de texte. En langue : `05` (compléments, accord sujet-verbe, prendre/mettre) est le
plus sollicité, puis `06` et `02` ; `03` (être au futur, adjectif épithète) est le moins sollicité. Jamais testés : l'homophonie (a/à,
son/sont, et/est), l'infinitif après à/de/par/pour/sans, dire/lire/écrire, le complément de lieu isolé (seulement dans
un tableau en 2021), avoir au passé composé ; la conjugaison est toujours en phrases à transposer, sans verbe à l'infinitif
à conjuguer.

**Part HP** : 5 lignes sur 69 portent un jeton HP (2026 : 1 ; 2025 : 0 ; 2024 : 0 ; 2023 : 2 ; 2022 : 1 ; 2021 : 1) ; aucune
n'est HP seule. **Programme ancien** : aucune session du lot ne sort nettement du manuel ; les six sont `en vigueur`
(les notions HP relèvent du tableau C, non enseignées en 6ᵉ, et non d'un programme antérieur).

## 4. Difficultés et doutes

- **Barème par question** : imprimé en 2024, 2022, 2021 seulement ; ailleurs `-`, sans répartir arbitrairement le total.
- **Thème du texte** : 2024 (amitié entre deux enfants puis mort d'un phoque : classé `05` d'après la question d'ouverture et
  la production, `03` possible) ; 2023 (handicap et regard des autres : `06`, `03` possible) ; 2021 (chat recueilli : aucun
  module ne l'annonce, rangé `04` par le partage du goûter et par la production, dont le dialogue avec un propriétaire relève de la
  structure « récit avec dialogue » ; `HP:theme-hors-modules` écarté) ; 2025 (voyage : `08`).
- **2025 conjugaison 2** : l'énoncé donne les verbes au présent et demande « le temps qui convient » ; l'adverbe « Bientôt »
  appelle le futur (01+05) ; le passé simple du texte n'est pas exigé. Clé non publiée.
- **2024 grammaire 1** : « dans l'eau sombre des profondeurs » est-il essentiel ou non ? Ambiguïté de la consigne, rangée `05`.
- **2024 grammaire 2** : l'item opère des changements de personne, jamais du discours indirect ; l'imparfait de la
  complétive est donné. Aucun `HP:discours-indirect`, aucun `HP:imparfait`.
- **2026 grammaire 2** : « plus personne ne rit » est une négation ⛔ (`ne… personne`) ; l'affirmatif attendu change le sujet
  (`HP:negation-personne`, `04` pour la forme négative).
- **2026 conjugaison 3 et 2021 conjugaison 3** : changement de personne avec présent de pouvoir `08` ; le futur du verbe
  pronominal « s'occuper » (2021) est un pronominal en filage, non étiqueté.
- **Accord de « tout »** (2023 grammaire 2 : « tous les jours » → « … les matinées ») : tableau C, `HP:accord-tout`.
- **Pronominaux** (2023 grammaire 3, 2021 grammaire 1) : le participe « senti » ou « approché(e) » s'accorde avec le sujet ;
  le passé composé des pronominaux est rencontré non enseigné, `HP:pc-pronominal` sans `08`.
- **Coquilles imprimées** conservées : 2022 « à son professeure », « (1point) » sans espace, « Emerveillée » sans accent
  en 2021, « apparait » et « disparait » en 2025, 2021 sans cadre « السلسلة » ; 2026 et 2025 sans barème par question.
- Aucune consigne n'a vieilli. Les sujets 2021 à 2026 sont tous conformes à un manuel de 6ᵉ actuel (fonctions, trois temps,
  impératif, négation).
