# Anglais 6ᵉ (`english-6eme`) — plan du passage unique (patron + étiquettes + armement + gisement)

> Écrit le **2026-10-18** par le planificateur, sur l'état mesuré dans [`ETAT.md`](./ETAT.md). À
> valider par le pilote (§ 6) avant toute écriture. Méthode : `PILOTAGE.md` § 1 (un seul passage,
> un seul auteur par chapitre, ≤ 4 agents, auteurs sonnet, auditeurs opus) ; gisement :
> `content-ingest/references/gisement.md` (G0–G8). Modèle : l'anglais 9ᵉ (cours au patron du
> 2026-09-28, gisement `36-…/en-cours/anglais/PLAN.md` sur `wip/gisement-9eme-lots-en-ecriture`).

## 0. Le constat qui fixe l'ordre

Les cours passent déjà le patron en régime strict : on **ne réécrit pas** les sept cours, on les
**complète** de ce que le gisement exigera et des pièges qui manquent. Le travail lourd est ailleurs :
le **vocabulaire d'étiquettes**, la **pose sur 735 distracteurs**, la **qualité d'items**
(clé la plus longue 16 %, 20 paires proches, 3 gabarits) et le **gisement** (17 sujets officiels
scannés, 41 devoirs). Comme les missions d'examen apporteront des distracteurs, et que lecture et
étiquettes doivent tenir en une passe (PILOTAGE § 1, étapes 1 et 3), l'ordre est :
**lecture (D1) → vocabulaire (A) → chapitres (B + C + missions, un auteur par chapitre) → audit →
armement et livraison (E)**.

## 1. Les lots, dans l'ordre

### Lot D0 — Qualifier et fixer l'échantillon (orchestrateur, ≈ 1 h) — AVANT toute lecture

- Registre neuf `content/programmes-officiels/sources-externes/web-6eme-base-english/`
  (`fiche.md`, `gisement.json`, `lignes.tsv` vide) sur le modèle de `web-9eme-base-english`.
- Fiche `web-echoexam-edunet-tn` : ajouter l'archive **`6web.edunet.tn`** (concours 6ᵉ, depuis 2008)
  et le portail de session `index-sujet-6eme.php`.
- Fiche `web-devoir-tn` : étendre au primaire (rubrique `primaire/السـ6ـنة/Anglais/Devoirs/`,
  rangement par trimestre, robots relu).
- **Échantillon** : examens = **les 17 sessions** (2008–2010, 2012–2013, 2015–2026 ; 2011 et 2014
  en 404, notées introuvables) ; devoirs = **vague 1 de neuf** (trois par trimestre, au plus deux par
  auteur, signés d'abord, les plus récents d'abord ; les anonymes complètent) — règle adaptée au
  primaire à faire valider (D4).
- **Livrable / gate** : fiche et registre mergés avant la première lecture (G1) ;
  `programme:check` vert ; PILOTAGE § 2 ligne 6ᵉ anglais « En cours » renseignée (réservation déjà
  posée sur `claude/reservation-anglais-6eme`).

### Lot D1 — Lire (≤ 4 lecteurs sonnet, en parallèle ; ≤ 6 documents chacun)

- Examens : 17 sessions **en vision** (scans), ≈ 42 pages → **3 lots** (2008–2013 · 2015–2020 ·
  2021–2026). Chaque lecteur rend la transcription fidèle
  `content/programmes-officiels/examens-nationaux/6eme-base/english/<année>.md` (en-tête YAML, sha256),
  les lignes `lines/<id>.tsv` et **marque le programme** de chaque item (scope des 35 encadrés de la
  fiche ; `HP:` sinon). Le texte support des readings est **résumé** au registre (référence + sha256),
  pas transcrit dans un fichier de mission (règle de l'anglais 9ᵉ).
- Devoirs : 9 documents → **2 lots** (salle blanche : lignes sans phrase, sans nombre de la source).
- Un 4ᵉ lecteur peut prendre le second lot de devoirs ; sinon il suit.
- **Livrable / gate** : 17 transcriptions versionnées, `lignes.tsv` (10 colonnes, contrôle « aucun
  nombre de deux chiffres dans l'archétype »), registre `documents` à l'état `lu` ;
  `programme:check` ; notes de lecture versionnées sous `FableEtudes/campagnes/anglais-6eme/lecture/`
  (jamais seulement dans le scratchpad).

### Lot D2 — Carte, écart et plan des missions (planificateur, une session)

- Carte par chapitre (G3) croisée avec les 245 questions (règle R4 du plan 9ᵉ : rien de ce que le
  patron pose déjà) ; plan (G4) au grain de l'item pour la langue (R1 du 9ᵉ : une mission par famille
  et par chapitre, sessions fusionnées), **une mission par texte** pour quelques readings récents
  (R2), **writing converti en préparation fermée** (R3).
- Placement : au chapitre de l'unité dont relève la notion (01–07). **Reading et writing n'ont pas de
  chapitre** dans le manifeste 6ᵉ : décision D2.
- Estimation (à confirmer à la carte) : 14–20 missions d'examen (≈ 150–220 questions), 2–4 missions
  de devoirs ; lots d'auteur de 5–8 missions par chapitre ; plages de numéros à la suite de
  `05-entrainement` (`06-…` et au-delà).
- **Livrable / gate** : `PLAN-gisement.md` + `plan-examens.json` versionnés ici ; registre : missions
  `planifiee` ; affectations anonymes `assign-*.md`.

### Lot A — Vocabulaire d'étiquettes `english.*` (un agent opus, après D2 ; ≈ ½ journée)

- **Réutiliser d'abord** les 67 ids de l'anglais 9ᵉ (liste ETAT § 4) — même espace `english.*`,
  même `subject: "english"` (précédent `math.*` partagé 6ᵉ/9ᵉ) ; **élargir** un libellé fr/en/ar par
  un exemple de 6ᵉ quand il ne cite que des tournures de 9ᵉ (ex. `verb.ing-oublie` : ajouter
  *How about*, *like*, *enjoy* ; `modal.to-en-trop` : *Let's to go*).
- **Ids neufs proposés** (≈ 15, textes fr/en/ar à écrire, chaque libellé à la 2ᵉ personne comme
  l'existant) :

| id proposé | erreur |
| --- | --- |
| `english.article.a-an-selon-la-lettre` | a/an choisi d'après la lettre et non le son (*a amphitheatre*, *an cape*) |
| `english.article.article-oublie-ou-en-trop` | article omis ou ajouté (*I am pupil*, *the Tunisia*) — à confirmer sur les distracteurs |
| `english.pron.possessif-accorde-a-l-objet` | possessif accordé à l'objet ou au mauvais possesseur (*Nadia and his kite*) |
| `english.pron.sujet-au-lieu-du-possessif` | pronom sujet devant un nom (*she bag*, *they house*) |
| `english.adv.frequence-mal-placee` | adverbe de fréquence après le verbe lexical (*goes never*) |
| `english.quant.many-much-confondus` | How many / How much sans regarder si le nom se compte |
| `english.health.be-et-have-confondus` | *I am a headache*, *I have sick* |
| `english.word.nom-au-lieu-de-l-adjectif` | nom pour adjectif (*a cloud day*, *It's sun*) |
| `english.word.nom-d-agent-force` | -er collé partout ou sur une base inventée (*a carpent*, *a doctorer*) |
| `english.verb.imperatif-mal-forme` | impératif avec sujet ou négation par *not* seul (*You close*, *Not close*) |
| `english.pron.ed-toujours-syllabe` | -ed prononcé /ɪd/ partout |
| `english.num.hundreds-au-pluriel` | *four hundreds*, *and* oublié dans 468 |
| `english.func.like-au-lieu-de-would-like` | *I like a croissant* pour commander |
| `english.question.ordre-du-prix` | *How much it is?* — à fusionner avec `question.auxiliaire-ou-ordre-oublie` si son libellé suffit |
| `english.vocab.paires-de-sens-proche` | buy/sell, fit/suit, win/lose : le mot de la paire inverse |
| `english.prep.by-to-at-confondus` | *travel by Italy*, *in/on the corner* — ou élargir `prep.preposition-calquee` |

- Les cas « couverts ? » (*she have the right* → `verb.auxiliaire-mal-accorde` ; *we was* → idem ;
  *will goes* → `verb.base-verbale-deformee`) se tranchent **par l'élargissement**, pas par un id neuf.
- **Livrable / gate** : `content/misconceptions.json` (ids neufs + libellés élargis), rapport
  `etiquettes/rapport-vocabulaire.md` (chaque id : piège du cours ou distracteur qui le porte) ;
  `content:check` (registre valide), `content:qa` (tags connus) ; relecture opus du vocabulaire
  (fusions, doublons avec l'existant).

### Lots B + C (+ missions) — chapitre par chapitre, **un auteur par chapitre** (sonnet)

Un même auteur, dans la même passe, sur son chapitre : (B) compléments du cours, (C) étiquetage des
options existantes et réparation des défauts d'items, (D3) missions du gisement rattachées.

| lot | chapitres | B — cours (ce qu'il faut faire) | C — items existants | missions |
| --- | --- | --- | --- | --- |
| **B1** | 01, 02 | **bon, à garder** ; ajouter ce que la carte d'examen exige (ex. appariements question/réponse, *because*) ; `coursePitfalls` (≥ 3, d'après les `piege`) | étiqueter 210 distracteurs ; clé longue 6 + 5 ; gabarit « three of these suggestions… » (01/04-defi#1, 02/04-defi#1) | celles de D2 |
| **B2** | 03, 04 | bon ; **04 : section ou encadré /ʃ/–/ʧ/** si le pilote le veut (D6) | 210 ; clé longue 4 + **8** ; paires 04 (quiz#4↔04-defi#1, 02-boss#6↔05-entrainement#6) ; gabarit 03/04-defi#1 | idem |
| **B3** | 05, 06 | bon ; 06 a 8 sections (plafond é35 R-13 « ~8 notions ») : rien à ajouter sans retirer | 210 ; clé longue 3 + **9** ; paires 05 (5 paires dont quiz#1↔01-pratique#3 à 0,64) ; gabarit 06/04-defi#1 | idem |
| **B4** | 07 | **ajouter « Let's pronounce »** (/s/–/z/ du pluriel, L2 ; /i/–/ai/, L4 — fiche § 3.4) : 9ᵉ section → au-delà de ~8 notions, à arbitrer (D6) ; sinon la placer en encadré du 04/06 | 105 ; clé longue 5 ; **5 paires** dont 04-defi#4↔05-entrainement#4 (0,68) ; gabarits 02-boss#1, 04-defi#1 | idem |

Pour chaque chapitre, quoi qu'il arrive :

- `chapter.json` : `coursePitfalls` (chaque tag porté par au moins un distracteur du chapitre, C-5) ;
  `sources[]` complétées (sujets officiels du concours 6ᵉ, transcriptions
  `programmes-officiels/examens-nationaux/6eme-base/english/`) ; `manuel` selon D1.
- Étiquetage : **cible ≥ 60 %** des distracteurs (niveau de l'anglais 9ᵉ hors chapitre de lecture) ;
  un distracteur « bruit » reste muet plutôt que mal étiqueté. Contrôler le `git diff --stat` si un
  script réécrit les JSON (piège `apply-tags.py`, PILOTAGE § 5).
- Items : faire tomber la clé la plus longue à **0** sur les questions touchées
  (`content:tranche --changed --fresh --strict-longest`) ; réécrire ou justifier chaque paire proche ;
  les gabarits passent à l'auditeur.
- Types natifs : introduire `matching` / `ordering` / `multi` là où l'épreuve nationale les impose
  (missions d'examen d'abord ; pas de conversion massive des QCM existants).
- **Gates par chapitre** : `content:check`, `content:qa -- --subject english-6eme` (0 erreur),
  `content:tranche -- --subject english-6eme --changed --fresh --strict-longest`, contrôle local
  anti-verbatim des missions de devoirs (`content:gisement:controle`) ; rendu `renderLesson` /
  `renderSummary` propre (pas de `&gt;`, `**`, `:::` résiduels — PILOTAGE § 1 règle 5).

### Audit — un auditeur opus par paire de lots (≤ 2 en parallèle), à l'aveugle

- Sur tout : cours touchés, 245 items existants **et** missions — re-résolution avant lecture de la
  clé, fidélité au guide 541608 (scope des 35 encadrés, divergence U-II L3), justesse de chaque
  étiquette, rendu. Rapports versionnés `audits/rapport-B1.md` … `rapport-B4.md`, écrits au fil de
  l'eau ; corrections renvoyées à l'auteur du chapitre (SendMessage), re-vérification par l'auditeur.
- **Stop** : une clé fausse ⇒ la tranche ne part pas.

### Lot E — Armement, livraison, publication (orchestrateur)

1. `subject.json` : `coursePattern: "notion"` ; `manuels` selon D1 ; description à revoir si D7
   (« First year of English »).
2. `npm run content:gates -- --tranche` depuis le moteur (les sept étages) : vert ; `content:qa`
   montre 0 erreur sous le régime `error` (C-5 levé par les `coursePitfalls`) ; `CATALOGUE.md`
   régénéré et committé.
3. Livraison depuis un worktree frais d'`origin/main` (G7) — une tranche = ≤ 4 chapitres : **deux PR
   successives** (01–04 puis 05–07 + armement), ou une seule si le pilote préfère (le drapeau
   `coursePattern` ne part qu'avec le dernier chapitre) ; commits thématiques (registre et
   transcriptions ; étiquettes ; un commit par chapitre ; armement).
4. Après le merge réel : `apply-content.yml` en `workflow_dispatch`, **`subjects=english-6eme`**,
   `dry_run=false` ; vérifier « Appliquer », « Vérifier en base », « Journaliser » ; issue
   `content-drift` close ; registre → `publiee` (numéro de PR) ; **PILOTAGE § 2** (ligne 6ᵉ anglais)
   et § 3 mis à jour **dans la PR** ; une ligne au journal de l'étude 36 (G8, mesures).
5. Moteur : `rm content` avant tout `git push` côté moteur, le recréer après (PILOTAGE § 5).

## 2. Parallélisme (≤ 4 agents)

| phase | agents simultanés |
| --- | --- |
| D1 lecture | 3 lecteurs examens + 1 lecteur devoirs (puis le 2ᵉ lot de devoirs) |
| D2 plan | orchestrateur seul (ou 1 planificateur) |
| A vocabulaire | 1 agent opus (peut tourner pendant D2 sur les `piege` et distracteurs existants ; se clôt après D2 pour les erreurs que les examens ajoutent) |
| B1–B4 | 4 auteurs sonnet en parallèle (chapitres disjoints) |
| audit | 2 auditeurs opus (B1+B2, B3+B4) ; les auteurs corrigent à la suite |
| E | orchestrateur seul |

Si le quota « five_hour » tombe : reprendre chaque agent par `SendMessage` (contexte conservé).

## 3. Volume et coût (ordre de grandeur)

17 sujets × 2–4 pages scannées (≈ 42 pages vision) ; 9 devoirs ; ≈ 15 étiquettes neuves ; 735
distracteurs existants + ceux des missions ; ≈ 150–250 questions de missions ; 7 `chapter.json` ;
1 section de cours au 07 (selon D6). Deux PR de livraison, une publication.

## 4. Ce qui ne se fait pas

- Pas de réécriture des cours (ils tiennent le patron) ; pas de notion hors des 35 encadrés (pas de
  *going to*, de passé continu, de *more/most* — fiche § 2 « EXCLU »).
- Pas de reprise d'un texte ou d'un audio du guide (borne de la fiche, `suivi/6eme-base.json`).
- Pas de transcription intégrale d'un texte de reading d'examen dans une mission (résumé + sha256).

## 5. Gates récapitulatifs

`programme:check` (D0, D1) · `content:check` · `content:qa -- --subject english-6eme` (0 erreur, puis
0 erreur sous `notion`) · `content:tranche --changed --fresh --strict-longest` · `content:gisement:controle`
(devoirs) · `content:audit:strict` (couverture 7/7 conservée) · `content:gates -- --tranche` · rendu
`renderLesson` · `apply-content` (trois étapes vertes) · `content-drift` clos.

## 6. Décisions à soumettre au pilote

| # | question | options | défaut proposé |
| --- | --- | --- | --- |
| **D1** | `manuel` des chapitres : le manuel élève « Learn and Grow » n'est **pas** au corpus CNP (404) | (a) pas de `manuel` ni de `manuels` (le guide reste cité dans `sources`) ; (b) pointer le **guide enseignant** `541608` avec les pages de l'unité (affiche des corrigés aux élèves) ; (c) chercher le livre élève hors CNP | **(a)**, et suivi « livre élève à trouver » |
| **D2** | Reading et writing de l'examen n'ont pas de chapitre (manifeste 6ᵉ = 7 unités) | (a) missions placées au chapitre de l'unité dont relève le **thème** du texte (2026 *Caring* → 04) ; (b) un chapitre neuf `08-exam-papers` (change le manifeste : décision propriétaire) | **(a)** |
| **D3** | Sessions antérieures à « Learn and Grow » (date d'entrée non établie) | lire les 17 et marquer `HP:` ce qui sort du scope ; ou ne lire que 2023–2026 | **lire les 17** (G1 : toutes les sessions), le lecteur marque |
| **D4** | Règle d'échantillon des devoirs au primaire (pas de DC/DS ; 34 sur 41 anonymes et non datés) | vagues de neuf = 3 par trimestre, signés et récents d'abord, ≤ 2 par auteur, anonymes en complément | **oui** ; règle des 30 % pour une vague 2 |
| **D5** | Ids d'étiquettes : réutiliser `english.*` (`subject: "english"`) pour la 6ᵉ, ids neufs dans le même espace, libellés élargis | ou un espace `english6.*` séparé | **même espace** (précédent `math.*`) |
| **D6** | Prononciation manquante au 07 (/s/–/z/ pluriel, /i/–/ai/) et au 04 (/ʃ/–/ʧ/) | (a) 9ᵉ section « Let's pronounce » au 07 (au-delà de ~8 notions) ; (b) encadré dans une section existante ; (c) rien (déjà vus en 01 et ailleurs) | **(a) pour le 07** (seul chapitre sans prononciation), **(c) pour le 04** |
| **D7** | `subject.json` dit « First year of English » ; un guide d'anglais de 4ᵉ année circule | vérifier avant l'armement ; corriger la description si l'anglais commence plus tôt | vérifier (lecture rapide du catalogue CNP / ministère) |
| **D8** | Une ou deux PR de livraison | 01–04 puis 05–07 + armement ; ou une PR de 7 chapitres (au-delà de la tranche ≤ 4 de G7) | **deux** |

## Décisions du pilote (2026-10-18)

- D1 : pas de champ `manuel` (manuel élève absent du corpus CNP) ; le guide 541608 reste dans `sources[]`.
- D2 : reading et writing des sujets placés au chapitre de l'unité dont relève le thème du texte (pas de chapitre 08).
- D3 : lire les 17 sessions disponibles ; items d'un ancien programme marqués `[hors programme en vigueur]` / `HP:`.
- D4 : échantillon de devoirs adapté au primaire : trois par trimestre, deux au plus par auteur.
- D5 : même espace d'étiquettes `english.*` que la 9ᵉ (libellés élargis à des exemples de 6ᵉ quand il le faut, ids neufs nommés au plan).
- D6 : section « Let's pronounce » ajoutée au 07 (/s/–/z/, /i/–/ai/).
- D7 : « First year of English » — vérifié par le lot D0 (guide de 4ᵉ année en ligne) avant de fixer la date du programme.
- D8 : livraison en deux PR (registre/échantillon d'abord, contenu ensuite).
