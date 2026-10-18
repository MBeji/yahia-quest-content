# Anglais 6ᵉ (`english-6eme`) — état des lieux avant le passage unique

> Mesuré le **2026-10-18** par le planificateur (aucune écriture sous `content/`), sur la branche
> `wip/anglais-6eme-un-passage` (tête `a2308074`, = `main` `c7286779` + la consigne). Moteur :
> `/home/user/eng-deliver` (`c6cee3c`), lien `content` → `/home/user/wt-en6/content`.
> Modèle de couple armé : l'anglais 9ᵉ (`content/english/`). Plan : [`PLAN.md`](./PLAN.md).

## 0. En une phrase

Les sept cours sont **déjà écrits à la forme du patron** (0 constat é35 en régime strict, 0
avertissement `content:qa`) : ce qui manque pour « armer » est **l'étiquetage** (0 option
étiquetée sur 735), les **`coursePitfalls`** (0/7), le **`manuel`** (0/7 — et le manuel élève
n'existe pas au corpus CNP), le drapeau **`coursePattern: "notion"`** et le **gisement** : l'anglais
**est** une épreuve du concours de 6ᵉ (**17 sessions** officielles disponibles, 2008–2026), et
devoir.tn publie **41 épreuves** de 6ᵉ anglais.

## 1. Contrôles (chiffres bruts)

| commande | résultat |
| --- | --- |
| `content:check` | ✓ — 120 matières, 1 058 chapitres, 4 885 exercices, 29 928 questions ; 1 071 étiquettes au registre |
| `content:qa -- --subject english-6eme` | ✓ — **0 erreur, 0 avertissement** (aucune clé suspecte ; garde anti-verbatim : 9 sources, 8 180 séquences) |
| `content:tranche -- --subject english-6eme` | ✓ sortie 0 — 245 questions ; **clé strictement la plus longue 40/245 = 16 %** (hasard 25 %, viser 0) ; positions a 24 % · b 28 % · c 25 % · d 23 % ; ⚠ **20 paires proches** (Jaccard ≥ 0,45, max 0,68) ; **3 groupes « gabarit »** (×6 « three of these suggestions are correct… », ×3 « read… which sentence about … is true », ×2 « … completely correct ») |
| `content:audit:strict` | ✓ sortie 0 — 6ᵉ : `english-6eme` couverture **7/7 (100 %)** ; niveau 6ᵉ : 4/6 matières (`french-6eme`, `education-islamique-6eme` manquantes — hors couple) ; `english-6eme` absent de la couverture des manuels élèves (aucun `manuels` déclaré) |
| `programme:check` | ✓ registre cohérent (26 avertissements, **aucun** sur `6eme-base/anglais`) |
| `programme:etat` | 6ᵉ, fiche anglais : **`validee-r7` / `generation`, couverture 100 %, R-7 2026-09-19 (intégrale, 7 corr.) — génération autorisée** ; `english-6eme : 7/7 ch` ; prod `concours-6eme : available` |
| patron é35, régime **strict** (`auditLesson … pattern: "error"`, script jetable) | **0 erreur, 0 avertissement sur les 7 cours** (même mesure sur l'anglais 9ᵉ : 0/10) |
| armement simulé | poser `coursePattern: "notion"` aujourd'hui donnerait **7 erreurs C-5** (« declares no coursePitfalls ») et rien d'autre |

Mesures de la tranche par chapitre (clé la plus longue) : 01 → 6, 02 → 5, 03 → 4, 04 → 8, 05 → 3,
06 → 9, 07 → 5. Paires proches les plus fortes : `07/04-defi#4 ↔ 07/05-entrainement#4` (0,68),
`05/quiz#1 ↔ 05/01-pratique#3` (0,64), `04/quiz#4 ↔ 04/04-defi#1` (0,64), `07/01-pratique#1 ↔
07/05-entrainement#1` (0,58), `04/02-boss#6 ↔ 04/05-entrainement#6` (0,57) — elles se concentrent
sur 04, 05 et 07.

## 2. Matière (`subject.json`)

| champ | `english-6eme` | `english` (9ᵉ, armé) |
| --- | --- | --- |
| `coursePattern` | **absent** | `"notion"` |
| `manuels` | **absent** | `141906P00` Student's Book, `141907P00` Activity Book |
| `themeId` / `gradeSlug` / `contentLanguage` | `ecole-tn` / `6eme-base` / `en` | `ecole-tn` / `9eme-base` / `en` |

**Le manuel élève « Learn and Grow — Year 6 » n'est pas au corpus CNP** : `corpus-cnp.json` (346
documents) ne liste en 6ᵉ anglais que le guide enseignant `541608P00` ; une sonde
`cnp.com.tn/arabic/PDF/<code>.pdf` répond **206** pour `541608P00` et **404** pour `141605`–`141610`
(P00, `141608P01`). Le `manuel` des chapitres ne peut donc pas pointer un livre élève : décision au
pilote (PLAN § 6, D1).

## 3. Chapitre par chapitre

Commun aux 7 : `cours.md` 386–501 lignes, 7–8 sections `##` (une notion chacune, la dernière
« Let's pronounce » sauf au 07), blocs `definition`/`propriete` → `exemple` → (`piege`) → `verifie`
→ `retenir`, une à trois figures SVG ; `resume.md` 10 lignes (une puce par section) ; **35 questions**
(quiz 5 + `01-pratique` d1 6 + `02-boss` d3 6 + `03-revision` d2 6 + `04-defi` d4 6 +
`05-entrainement` d3 6), **toutes `mcq`**, 105 distracteurs, **0 étiqueté** ; `manuel` absent ;
`coursePitfalls` absent ; `sources` = le guide `541608P00` (pages de l'unité) + la fiche (2 ou 3
entrées) ; aucune vidéo. Aucun rendu fautif repéré (`> -`, `>` seul, tableau collé à `:::`) — à
confirmer par `renderLesson` (règle 5 du PILOTAGE) ; les tableaux du cours relèvent du suivi S5 de
l'anglais 9ᵉ.

| ch. | guide | sections du cours | `piege` (erreur visée) | écart à la fiche | q. (d1/d2/d3) | clé + longue |
| --- | --- | --- | --- | --- | --- | ---: |
| 01 Entertaining Myself | p.9–17 | activités ; like/enjoy/hate/dislike + -ing, because/and/but ; adverbes de fréquence (+ -s) ; on/in ; Let's / How about / What about ; Would you like to ; adjectifs possessifs ; /s/–/z/ | 3 : *enjoy to swim* ; *Let's to go / How about go* ; *Nadia and his kite* | conforme (linkers and/but présents, L4 ; « Because » en tête, L1) | 35 (8/16/11) | 6 |
| 02 Keeping Fit | p.18–25 | sain/malsain ; should ; must ; can/can't (divergence L3 tranchée pour can, déclarée en `sources`) ; have a + ailment / to be + adj. ; How many/How much ; /ɪ/–/iː/ | 3 : *should to / shoulds* ; *cans / can to* ; *I am a headache / I have sick* | conforme | 35 (9/15/11) | 5 |
| 03 Seasons | p.26–32 | saisons et mois ; Noun + y ; What's the weather like? ; will/won't + mots du futur ; -er + than ; Verb + ing = activité ; /ð/ | 3 : *a cloud day* ; *will goes* ; *more warm / -er that* | conforme (« to be on holidays » en incise) | 35 (9/15/11) | 4 |
| 04 Caring | p.33–41 | vocabulaire de l'entraide, each other ; possessifs ; superlatif -est ; verb + er = métier ; will/won't ; impératif et Don't ; h prononcé / muet | 5 : *she bag* ; *the cleaner street* ; *-er partout (a carpent)* ; *will cleans* ; *Not close / You close* | conforme ; /ʃ/–/ʧ/ (L4) non traité (le guide le nomme) | 35 (8/16/11) | 8 |
| 05 Celebrations | p.42–50 | fêtes ; have/has the right to ; simple past ; orthographe -ed ; irréguliers ; was/were ; -ed /t/ /d/ /id/ | 5 : *she have the right* ; *playeds* ; *buyed / maked* ; *we was* ; *-ed toujours syllabe* | conforme | 35 (7/17/11) | 3 |
| 06 Going Shopping | p.51–58 | boutiques ; would like ; How much is it? ; centaines ; simple past des achats ; essayer (try on / fit / suit) ; in/on the corner ; /ʒ/–/ʤ/ | 7 : *buy/sell* ; *I like (= would like)* ; *How much it is?* ; *four hundreds* ; *buyed* ; *suit/fit* ; *usually* | conforme ; /ai/–/i/ (L1), -ed (L2), /ʃ/–/ʧ/ (L5) non repris (déjà en 04/05 ou absents) | 35 (7/16/12) | 9 |
| 07 Around the World | p.59–70 | points cardinaux ; Let's travel / How about ; salutations ; a/an/the ; travel by/to + prefer ; comparatif ; superlatif et monuments ; coutumes | 8 : *on the right of the map* ; *How about travel* ; *salutation « polie »* ; *a amphitheatre / an cape* ; *travel by Italy* ; *more fast* ; *tallest than* ; *are eating (habitude)* | **pas de section « Let's pronounce »** (le guide nomme /s/–/z/ en L2, /i/–/ai/ en L4) | 35 (7/16/12) | 5 |

**Lecture des écarts** : le contenu colle à la fiche (scope des 35 encadrés, divergence U-II L3
tranchée et déclarée, pas de notion de 9ᵉ). Les seuls manques de fond sont la prononciation du 07
(et, accessoirement, /ʃ/–/ʧ/ au 04) ; tout le reste est de l'**armement** et de la **qualité
d'items** (clé longue, paires proches, gabarits). Les 245 questions sont toutes des QCM : aucun type
natif (`matching`, `ordering`, `multi`, `short_answer`) alors que l'épreuve nationale est faite
d'appariements, de vrai/faux et de remises en ordre (§ 4).

**Le modèle 9ᵉ, par comparaison** : 10 chapitres, 545 questions (26–151 par chapitre, types
natifs présents), **798 options étiquetées sur 1 676 (48 % ; 61 % hors chapitre 09)**,
`coursePitfalls` 4–9 par chapitre, `manuel` sur les 10, `sources` 3–14 (manuel + examens + sites).

## 4. Étiquettes

- Registre : **67 ids `english.*`** (`subject: "english"`), aucun propre à la 6ᵉ. Précédent de
  partage entre niveaux : `math-6eme` porte 1 347 étiquettes `math.*` (même espace que la 9ᵉ) ;
  `arabic-6eme` 847 `arabe.*` ; `eveil-scientifique-6eme` 425 `eveil.*`.
- **Réutilisables tels quels** (relevé sur les `piege` et les distracteurs lus) :
  `english.verb.ing-oublie`, `…verb.base-verbale-deformee`, `…verb.s-oublie-3e-personne`,
  `…verb.auxiliaire-mal-accorde`, `…verb.be-avec-base-verbale`, `…modal.to-en-trop`,
  `…modal.s-sur-le-modal`, `…modal.fonction-confondue`, `…comp.forme-selon-longueur`,
  `…comp.double-marque`, `…comp.superlatif-sans-the`, `…comp.comparatif-et-superlatif-confondus`,
  `…comp.egalite-fermee-par-than` (à vérifier : *-er that*), `…spell.suffixe-sans-regle-orthographique`,
  `…tense.present-avec-marqueur-passe`, `…tense.ed-sur-verbe-irregulier`,
  `…tense.continu-pour-habitude`, `…question.mot-interrogatif-inadapte`,
  `…link.connecteur-de-mauvais-type`, `…func.fonction-mal-identifiee`, `…prep.preposition-calquee`,
  `…read.*` (missions de lecture). Certains libellés ne citent que des exemples de 9ᵉ (*mind*,
  *regret*, *whereas*) : à **élargir** (ajouter un exemple de 6ᵉ), pas à dupliquer.
- **Sans id existant** (à créer, PLAN lot A) : article a/an selon le son ; possessif choisi d'après
  l'objet et non le possesseur (*Nadia and his kite*) ; pronom sujet à la place du possessif
  (*she bag*) ; Let's / How about + forme fausse (couvert en partie par `ing-oublie` et
  `base-verbale-deformee`) ; place de l'adverbe de fréquence ; How many / How much (dénombrable) ;
  *I am a headache* / *I have sick* ; nom pour adjectif (*a cloud day*) ; nom d'agent forgé ;
  impératif / prohibition (*Not close*, *You close*) ; *have* pour *has* (the right to) — couvert par
  `auxiliaire-mal-accorde` ? à trancher ; *was/were* (idem) ; -ed en syllabe partout ; *hundreds*
  au pluriel ; *I like* pour *I would like* ; *How much it is?* ; buy/sell, fit/suit ; in/on the
  corner ; travel by / to ; points cardinaux droite/gauche. Estimation : **12 à 18 ids neufs**.

## 5. Sources du gisement

### 5.1 Examens — **oui** : le concours d'entrée aux collèges pilotes a une épreuve d'anglais

- Portail du Ministère : `http://www.echoexam.edunet.tn/index-sujet-6eme.php` (session 2026 : lundi
  22 juin 2026, 2ᵉ séance « الأنقليزية » ; cinq épreuves : arabe, anglais, français, éveil
  scientifique, maths) et l'archive **`http://6web.edunet.tn/`** (« مواضيع المناظرات الوطنية منذ
  2008 — الالتحاق بالمدارس الإعدادية النموذجية »), un PDF par matière et par session
  (`/<année>/anglais.pdf`). Lien pour l'anglais : 19 sessions 2008–2026.
- Téléchargés **pour compter seulement** (scratchpad, hors git) : **17 PDF valides**, **2 manquants**
  (2011 et 2014 : HTTP 404). Pages : 2008–2022 = 2 p., 2023 = 3 p., 2024–2026 = 4 p. Le PDF 2026 de
  l'archive est identique (sha256) à celui du portail de session. **Tous scannés** : aucune couche
  texte (sauf 2008 partielle, 401 mots) → lecture **vision** (é36 D-8, 150 dpi).

| session | p. | sha256 (16 premiers) | | session | p. | sha256 (16 premiers) |
| --- | --: | --- | --- | --- | --: | --- |
| 2008 | 2 | `34e75d1421c92157` | | 2018 | 2 | `b9a14850851fbabd` |
| 2009 | 2 | `133c97e3fe8347d3` | | 2019 | 2 | `92e9369b29260496` |
| 2010 | 2 | `cca8ab53e113e482` | | 2020 | 2 | `dee952d2b0b28584` |
| 2012 | 2 | `9e6a536218d4a78b` | | 2021 | 2 | `6b748fc4f1371ad1` |
| 2013 | 2 | `30ad6092b776fcfa` | | 2022 | 2 | `ff6341c0bdb0a376` |
| 2015 | 2 | `8d48f3e3fb75d279` | | 2023 | 3 | `883a5e762564e706` |
| 2016 | 2 | `af93240f8a25ccfe` | | 2024 | 4 | `a5c7b22f24874f7f` |
| 2017 | 2 | `b806efb38a02845c` | | 2025 | 4 | `4cfa12a00e848fa7` |
| | | | | 2026 | 4 | `a4920ef83df6f901` |

- Forme (vue sur 2022 et 2026, première page seulement) : **Reading comprehension 6 pts** (texte
  court + vrai/faux, choix, complétion), **Language 8 pts** (appariement A/B, textes à trous),
  **Writing 6 pts** ; sur 20. Le texte 2026 (*World Caring Day*, cadeaux faits main, hôpital)
  recoupe l'unité IV « Caring » de « Learn and Grow » ; le texte 2022 (*Carole*, voisine, marché)
  est plus général. **Date d'entrée en vigueur de « Learn and Grow » non établie** (la recherche
  web n'a rien donné ; le changement de format 2023–2024 en est un indice, pas une preuve) : le
  lecteur marquera les sessions d'un programme ancien (gisement.md G1).

### 5.2 Devoirs — devoir.tn (fiche `web-devoir-tn` existante, à étendre au primaire)

- Rubrique `primaire/السـ6ـنة/Anglais/Devoirs/` : **41 épreuves** — 1ᵉʳ trimestre **13**, 2ᵉ **13**,
  3ᵉ **15** (PDF, souvent doublés d'un `.doc/.docx`). `robots.txt` : `Allow: /` (aucune règle
  contre ce chemin). Listées, **pas téléchargées**.
- Auteurs et années : **34 anonymes et non datés** (« Epreuve n° NN ») ; **7 signés** —
  Khaled Mansouri, école primaire « le pilote », 2018-2019 (**×2**, 3ᵉ trim.) ; Sabrine Bhar,
  Alfawz Teboulba, 2019-2020 ; Nawel Mathlouthi, 2020-2021 ; école primaire de Birine, 2020-2021 ;
  Faten Msdi, 2020-2021 (1ᵉʳ trim.).
- Le primaire n'a pas de créneaux DC1…DS3 : les « créneaux » sont les **trois trimestres**. Les
  années signées (2018–2021) sont **peut-être antérieures** au programme « Learn and Grow ».
- Autres sites (tunitests, tunisiecollege) : non qualifiés pour la 6ᵉ anglais dans cette passe.

### 5.3 Ce que dit la doctrine

- ETUDE 36 D-10 : « le gisement d'une classe à examen ne traite que les matières de ses épreuves » ;
  l'anglais **est** une épreuve du concours de 6ᵉ → le couple est **dans** le périmètre, examens
  compris. (La consigne prévoyait le cas contraire « gisement réduit aux devoirs » : il ne
  s'applique pas.)
- Reprise : sujets officiels **repris et cités** (corpus officiel, Q-6) ; devoirs en **salle
  blanche** (T2′).

## 6. Autres constats (hors couple, à signaler)

- La fiche dit « l'anglais **démarre** en 6ᵉ » ; un guide « Have Fun, Learn English » de **4ᵉ année**
  circule (Scribd), ce qui suggère un anglais commencé avant la 6ᵉ dans le programme actuel. Le
  corpus CNP n'a aucun document d'anglais en 4ᵉ/5ᵉ. Sans effet sur le scope de la 6ᵉ (le guide
  fait foi), mais à vérifier avant d'écrire « first year of English » (`subject.json`).
- `programme:check` : 4 fiches « partielle mais 100 % — promouvoir ? » (5ᵉ arabe, 6ᵉ arabe, 7ᵉ
  français, 8ᵉ anglais), sans lien avec ce couple.
