# Pilotage unique du contenu scolaire — campagne fusionnée « patron + gisement »

> **Seul point d'entrée de toute session de contenu.** À lire avant toute action ; à mettre à jour
> **dans la PR même** qui fait avancer une ligne (jamais « après »). Depuis le 2026-10-12, une seule
> session porte à la fois la campagne « 9ᵉ au patron » (cours réécrits sur le manuel, étiquetés,
> armés) et l'étude 36 « gisement » (exercices tirés des sujets d'examen nationaux et des devoirs en
> ligne). Les deux campagnes visitaient les mêmes chapitres deux fois — deux lectures, deux passes
> d'étiquettes, deux audits, deux publications : on ne le fait plus.
>
> **Ordre de vérité** en cas de désaccord : le contenu sur `main` et ses registres
> (`sources-externes/<couple>/gisement.json` pour les missions, `programmes-officiels/suivi/*.json`
> pour les fiches, `misconceptions.json` pour les étiquettes) > ce fichier > tout journal. Un écart
> trouvé se corrige ICI dans la PR qui le constate.

## 1. La méthode — un seul passage par couple (niveau × matière)

| # | Étape | Produit | Preuve |
| --- | --- | --- | --- |
| 1 | **Lecture unique** : manuel élève (fiche R-5) **et** sujets d'examen nationaux **et** devoirs du registre du couple, dans la même passe | notes versionnées sous `FableEtudes/` (jamais seulement dans un scratchpad) ; registre `gisement.json` (documents `lu`) ; `suivi/*.json` | `programme:check` |
| 2 | **Chapitre par chapitre, un seul auteur** : le cours au patron (s'il n'est pas déjà armé), les items du chapitre, **et** les missions du gisement rattachées à ce chapitre (examens repris et cités, devoirs réécrits en salle blanche) | `content/<matière>/<chapitre>/` ; registre `planifiee` → `mergee` | `content:check`, `content:qa`, `content:tranche --changed --fresh --strict-longest` |
| 3 | **Une seule passe d'étiquettes** par couple : vocabulaire d'erreurs (phase 1), pose sur les distracteurs + `coursePitfalls` (phase 2, C-5) | `misconceptions.json`, `misconceptionTag`, `chapter.json` | `content:qa` (tags connus, C-5) |
| 4 | **Un seul audit indépendant** (opus) par lot de chapitres, sur tout : cours, items, missions — re-résolution à l'aveugle, fidélité au manuel, rendu | rapport versionné, corrections appliquées | rendu `renderLesson` / `renderSummary` propre |
| 5 | **Armement et livraison** : `coursePattern: "notion"`, `content:gates`, PR propre, merge, `apply-content.yml` (`subjects` renseigné), issue `content-drift` close, registre → `publiee`, ce fichier mis à jour | prod | les trois étapes « Appliquer », « Vérifier en base », « Journaliser » |

Règles qui empêchent le double travail :

1. **Une ligne du §2 = un couple.** Avant de commencer une étape, regarder la colonne « En cours » :
   ce qui y figure n'est repris par personne d'autre. Réserver (branche + date) dans le premier
   point de sauvegarde.
2. **Un chapitre n'a qu'un auteur à la fois** et une étape ne se refait pas : une lecture faite se
   cite (notes versionnées), un audit fait se cite (rapport versionné), un vocabulaire fait se réutilise.
3. **Savepoints** sur une branche `wip/<couple>` (jamais d'automerge), **livraison** recomposée en
   quelques commits thématiques sur la branche désignée de la session (le titre du squash = le dernier
   commit) ; une seule PR privée ouverte à la fois par couple.
4. **≤ 4 agents** en parallèle (quota « five_hour » consommé, pas une durée) ; auteurs sonnet,
   auditeurs opus ; chaque agent écrit ses fichiers au fil de l'eau ; après une coupure, le reprendre
   par `SendMessage` (contexte conservé) une fois le quota rouvert.
5. **Rendu vérifié avant toute PR de cours** : le moteur n'affiche ni une liste dans une citation
   (`> - …`), ni une ligne `>` seule, ni un gras qui enjambe un retour à la ligne, ni un tableau collé
   à un `:::` (Prettier le casse) — rendre chaque cours touché avec `renderLesson` et chercher
   `&gt;`, `**`, `:::` résiduels.

## 2. Tableau de bord (état mesuré le 2026-10-12 ; colonne « Fiche » de la 6ᵉ re-mesurée par `programme:etat` le 2026-10-12 à 17 h UTC)

Légende : ✅ fait · ⏳ en cours · ❌ à faire · — sans objet.

### 9ᵉ (année de concours — à finir avant tout le reste)

| Couple | Fiche / manuel | Cours au patron | Étiquettes | Audit | Gisement : examens | Gisement : devoirs | En cours · prochaine action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| maths (`math`) | ✅ 102905 lu | ✅ armé ; 01–02 recentrés, audités et publiés le 2026-10-12 (privé#660) | ✅ | ✅ (01–02 : audit opus du 2026-10-12, `_campagne-9eme-au-patron/maths-9eme/rapport-audit-recentrage.md`) | ✅ L01–L22 publiés (L17 privé#664, L21 privé#666) ; L22 (ch. 07/12/18) publié le 2026-10-12 (privé#670) — **le plan d'examens maths est publié en entier (198 missions)** | ✅ devoirs vague 1 publiés en entier (G2 privé#673, I privé#675 ; registre : 208 `publiee`, 1 `ecartee`, 0 planifiée) ; **devoir `D34`** (contrôle 1, collège pilote, fourni par le propriétaire le 2026-10-14, hors vagues) : 5 missions (ch. 02, 03, 15, 16, 18 ; 34 questions) écrites en salle blanche, auditées à l'aveugle (opus : 0 clé fausse, 12 majeurs corrigés, re-vérifiées), cours 19 complété (|expression| = r), 3 étiquettes neuves — livrées et **publiées** le 2026-10-14 (privé#691, registre `publiee`) | **réservé** session unique (2026-10-12) : devoirs G2 (ch. 04) publiés le 2026-10-12 (privé#673) ; **I** (ch. 09, 5 missions, 34 q) audité (0 clé fausse, 10 majeurs), corrigé, re-vérifié, livré et publié le 2026-10-14 (privé#675) ; registre maths : **plus aucune mission planifiée** (vague 1 des devoirs épuisée ; une vague 2 se décide sur la règle des 30 % de signatures neuves) (cartes régénérées depuis `lignes.tsv` ; transcriptions locales des devoirs refaites pour le contrôle anti-copie) ; lots : `wip/gisement-9eme-lots-en-ecriture` (PR #607), mode d'emploi dans `36-gisement-examens-devoirs/en-cours/ETAT-REPRISE.md` § « PASSAGE DE RELAIS » |
| SVT (`sciences-vie-terre`) | ✅ 105905 lu | ✅ armé le 2026-10-01 (14 ch. + 7 optionnels) | ✅ `bio.*` | ✅ | ✅ vague 1 (2020–2026) : 27 missions `publiee` ; **vague 2** (2001–2019 : 17 sessions lues, 2004 introuvable, génétique hors programme écartée) : 16 missions fusionnées en 3 lots (L11–L13), auditées à l'aveugle (opus), corrigées, re-vérifiées, livrées le 2026-10-16 — **toutes les sessions disponibles sont exploitées** | ✅ vague 1 lue (D01–D06 ; D02 et D04 écartés : plafond de deux devoirs par auteur) : 6 missions en salle blanche (L14), auditées, livrées le 2026-10-16 ; ~22–31 % de signatures neuves : **pas de vague 2** (profondeur avant volume) | cours 01 (structure du nerf) et 02 (exemple de réflexe) complétés, `02/01-tamrin` Q5 et quiz Q8 alignés ; étiquette neuve `bio.contra.regles-supprimees-par-la-pilule`, `bio.circ.artere-sang-oxygene` élargie ; **publiés** le 2026-10-16 (privé#695 ; registre : 49 missions `publiee`) ; rapports dans `36-gisement-examens-devoirs/en-cours/svt/` (branche `wip/gisement-9eme-lots-en-ecriture`) |
| physique-chimie (`svt`) | ✅ 103902 lu | ✅ armé le 2026-09-28 | ✅ | ✅ | — écarté (é36 D-10 : pas d'épreuve en filière générale) | — | — |
| arabe (`arabic`) | ✅ 101908 lu en entier, 101909 aux pages utiles (fiche `partielle` à dessein) | ✅ 19 chapitres réalignés (5 neufs), armé `notion` le 2026-10-12 | ✅ 197 ids `arabe.*` neufs + 17 réutilisés, 1 446 options (73 %), `coursePitfalls` sur les 19 ch. | ✅ A1–A4 + A4b (07–08) ; fusion du vocabulaire relue (opus) | ✅ sessions 2020–2026 (C01–C12) : 32 missions publiées le 2026-10-14 (privé#687) ; **vague 2** (2002–2019, C13–C39 ; 2004 et 2001 introuvables) : 16 générales/uniques = dialogue argumentatif seul, 10 techniques = compréhension narrative + paragraphe, langue d'acquis 7ᵉ-8ᵉ écartée (HP) — 6 missions (3 préparations de production au 09, 3 compréhensions au 10), auditées à l'aveugle, corrigées, re-vérifiées, livrées le 2026-10-18 ; lignes C01–C12 converties au format valide, `lignes.tsv` du registre complet | ✅ vague 1 lue (D01–D06 ; 5 antérieures au programme révisé, gardées) : 1 mission en salle blanche (12, nom manqus), auditée, livrée le 2026-10-18 ; 25 % / 5 % de signatures neuves : **pas de vague 3** | cours 09 complété (نصيحة / رسالة) ; patron livré le 2026-10-12 ; gisement examens publié ; suites : exemple résolu et `verifie` pour « العنوان المضمونيّ » et « تطوّر الموقف » (ch. 10), correctif moteur `isolateLtrRuns` (« » ← » et « «(1) » brouillés) : PR moteur #1170 ; doutes ouverts : `etiquettes/rapport-fusion.md` §6 (12 pièges sans distracteur qui les porte), relecture native des 38 libellés neufs ou réécrits souhaitée — vague 2 **publiée** le 2026-10-18 (privé#714 ; registre : 39 missions `publiee`) |
| français (`french`) | ✅ 121905 lu | ✅ armé le 2026-10-01 | ✅ `fr.*` | ✅ | ✅ 41 sessions d'examen lues (2001–2026, 1 introuvable) : **27 missions** fusionnées en 5 lots (L01–L05), chacun audité à l'aveugle (opus), corrigé et re-vérifié, livrées le 2026-10-16 ; texte support des compréhensions résumé (référence, sha256 au registre), jamais transcrit en entier | ✅ vague 1 lue (D01–D08) : 6 missions en salle blanche (L06), auditées, corrigées, re-vérifiées, livrées le 2026-10-16 ; **pas de vague 2** (décision du pilote) | cours 01, 02, 05 et 11 complétés de ce que les sujets exigent ; étiquette neuve `fr.mode.subjonctif-abusif` (élargie aux conjonctions) ; suivi moteur : italique contenant du gras (`36-…/en-cours/francais/SUIVIS.md`) ; rapports dans `36-gisement-examens-devoirs/en-cours/francais/` (branche `wip/gisement-9eme-lots-en-ecriture`) — **publiés** le 2026-10-16 (privé#701 ; registre : 33 missions `publiee`) |
| anglais (`english`) | ✅ 141906 + 141907 lus | ✅ armé le 2026-09-28 | ✅ | ✅ | ✅ 41 sessions d'examen lues (2001–2026, 2004 introuvable) : **24 missions** fusionnées en 5 lots (L01–L04, L06), chacune auditée à l'aveugle (opus), corrigée et re-vérifiée, livrées le 2026-10-17 ; texte support des readings résumé (sha256 au registre), passif écarté (non enseigné) | ✅ vague 1 lue (D01–D06 ; écoute des contrôles sans objet) : 2 missions en salle blanche (L05), auditées, livrées le 2026-10-17 ; **pas de vague 2** (19–28 % de signatures neuves) | cours 07 (gérondif + to + base, pronoms compléments, « own », dérivation par suffixes) et 09 (prépositions, connecteurs) complétés de ce que les sujets exigent ; 4 étiquettes neuves `english.*`, 2 élargies ; suivis : noms des chapitres 06/07 du manifeste ≠ contenu (`36-…/en-cours/anglais/SUIVIS.md` S1), rendu des tableaux (S5) ; rapports dans `36-gisement-examens-devoirs/en-cours/anglais/` — **publiés** le 2026-10-17 (privé#706 ; registre : 26 missions `publiee`) |

### 6ᵉ (concours de 6ᵉ — après la 9ᵉ)

| Couple | Fiche / manuel | Cours au patron | Étiquettes | Audit | Gisement | En cours · prochaine action |
| --- | --- | --- | --- | --- | --- | --- |
| maths (`math-6eme`) | ⚠️ fiche `partielle/mixte`, 23 % (502603 et 102609 à trous) — `programme:etat` : génération interdite, contenu généré sous la barre R-5 | ✅ armé | ✅ | ✅ | ❌ | **LOT A d'abord** (compléter la fiche), puis gisement en un passage |
| arabe (`arabic-6eme`) | ⚠️ fiche `partielle/generation`, 100 % mais pas en profondeur R-5 — génération interdite | ✅ armé (19 ch.) | ✅ | ✅ | ❌ | profondeur R-5 de la fiche, puis gisement en un passage |
| éveil scientifique | ⚠️ fiche `partielle/mixte`, 57 % (503604 p. 103–180 à trous) — génération interdite | ✅ armé | ✅ | ✅ | ❌ | **LOT A d'abord**, puis gisement en un passage |
| anglais (`english-6eme`) | ✅ `validee-r7`, 100 % ; guide 541608 (manuel élève absent du corpus CNP, D1) ; 6ᵉ = **3ᵉ année d'anglais** (D7, corrigé) | ✅ armé le 2026-10-18 (7 ch., section « Let's pronounce » au 07) | ✅ patron entier étiqueté (51–65 % des distracteurs selon le chapitre, muets à raison, E7) ; 19 étiquettes neuves `english.*`, 6 élargies | ✅ 4 lots audités à l'aveugle (opus), corrigés, re-vérifiés | ✅ 17 sessions du concours lues (2008–2026 ; 2011 et 2014 introuvables) : **19 missions** d'examen ; 2 missions de devoirs en salle blanche (9 devoirs lus) | rapports dans `FableEtudes/campagnes/anglais-6eme/` — **publication en cours** |
| français 6ᵉ | ❌ fiche `partielle/mixte`, 14 % | ❌ la matière n'existe pas | — | — | ❌ | LOT A, puis tout le reste en un passage |

## 3. File d'attente (ordre arbitré par le propriétaire : la 9ᵉ finie avant tout, puis la 6ᵉ)

1. ~~**Arabe 9ᵉ — finir et publier le patron**~~ livré le 2026-10-12 : A4 (07–08), vocabulaire A + B fusionné et
   complété (02, 03, 19), 1 446 étiquettes, armement `notion`, gates vertes, rendu des 19 cours propre ; reste
   la publication `subjects=arabic`, `content-drift` clos, fermer #634 et #637, `STATUS.md` du moteur ;
   5. ~~puis le **gisement arabe 9ᵉ en un passage**~~ examens 2020–2026 livrés le 2026-10-14 (32 missions) (chapitre 11 annales + missions par chapitre ;
      registre `web-9eme-base-arabic/gisement.json`). ⚠️ le contexte lecteur
      `en-cours/lecture-9eme/arabe/reader-context.md` (étude 36) liste l'ANCIEN chapitrage : le
      régénérer depuis `manifest/9eme-base.json`.
2. ~~**Maths 9ᵉ 01–02**~~ audité, livré et publié le 2026-10-12 (§4) ; était : audit indépendant opus du recentrage, puis PR séparée (`content/math/01-*`,
   `02-*` seulement), `apply-content` `subjects=math`. Rapport du recentrage au §4.
3. **Gisement 9ᵉ restant**, chaque couple en un passage : ~~maths~~ (plan d'examens et devoirs vague 1 publiés), ~~SVT~~ (examens 2001–2026 et devoirs livrés le 2026-10-16), ~~français~~ (examens et devoirs livrés le 2026-10-16), ~~anglais~~ (examens et devoirs livrés le 2026-10-17).
4. **6ᵉ** : ~~`english-6eme`~~ (livré le 2026-10-18), puis `french-6eme`, puis le gisement des couples 6ᵉ déjà armés. ⚠️ Mesure du 2026-10-12 : les fiches de maths (23 %), d'éveil (57 %) et d'arabe 6ᵉ (pas en profondeur R-5) sont sous la barre — `programme:etat` y interdit la génération ; leur gisement passe d'abord par le LOT A (compléter la fiche), à confirmer avec le propriétaire avant de l'ouvrir.

## 4. Rapport du recentrage maths 9ᵉ (2026-10-12, audité et livré le même jour)

- `01-nombres-reels` (ch. 2 du manuel, p. 18–30) : 47 questions, 44 dans le chapitre, 3 hors (calcul
  dans ℝ, identité nommée) réécrites (02-boss#6, #7, 04-defi#5) ; le gros débordement signalé par la
  fiche §6.2 bis (valeur absolue, écriture scientifique, ordre, intervalles) n'était plus dans les
  fichiers ; un encadré « للتوسّع » renvoie au ch. 3.
- `02-racines-carrees` (ch. 3 §IV, p. 39–40, déf. p. 27) : 45 questions, 39 dans, 6 hors (Pythagore,
  trinôme carré parfait, carré d'une somme) réécrites ; vocabulaire d'identité retiré (le produit de
  conjugués reste, par double distributivité, p. 37) ; `coursePitfalls` : retrait de
  `math.geo.pythagore-sans-carres`, ajout de `math.num.radicaux-semblables-radicande-additionne`.
- Contrôles : `content:qa` 0 erreur 0 avertissement sur math/01–02 ; tranche 0/101 clé la plus longue.
- **Audit indépendant (opus, 2026-10-12)** : 92 questions re-résolues, 0 clé fausse ; 3 corrections dans 02
  (04-defi#4 c « (√5 − 2) / 3 » ; piège de la simplification : « √50 = 2√5 بدل 5√2 » ; encadré 🗡️ sur
  l'ordre des facteurs). Verdicts : 01 conforme, 02 conforme après corrections.
- **« إنطاق المقام / المرافق » — tranché par la règle du métalangage du manuel** : le manuel exige la
  technique (p. 37 n° 4 et 7, p. 46 ex. 16, p. 47 ex. 17) sans jamais nommer ces termes → la technique
  reste (items de calcul), les termes ne figurent plus qu'en incise (cours, résumé) ; les deux
  `short_answer` qui les faisaient nommer deviennent des `numeric` (02-pratique#6, 03-revision#7) ;
  `manuel.pages` = « 27, 37, 39-40, 46-47 ».
- Missions de l'étude 36 hors chapitre (constat, non touchées) : 01/08-devoir#6 (puissances 3²⁰²¹ → ch. 4)
  hors chapitre ; #7 et #1 débordent légèrement (résultat donné / explication par √27 = 3√3). À reprendre
  au prochain passage du gisement maths sur le ch. 01.

## 5. Pièges connus (cumul des deux campagnes)

- Prettier : depuis le moteur, par le lien `content/…` seulement (un chemin absolu côté corpus ne
  trouve pas `.prettierrc` → faux positifs) ; jamais `--write` sur un `.md` de cours qui a un tableau
  collé à un `:::`.
- `apply-tags.py` (é36) réécrit les JSON au format canonique : contrôler `git diff --stat`, et pour un
  diff gonflé remplacer à la main la seule valeur `misconceptionTag`.
- Un auditeur coupé avant d'avoir écrit perd tout : rapports au fil de l'eau, toujours.
- Moteur : `rm content` avant `git push` (le test `verbatim-checks` échoue avec le lien), le recréer après.
- Autres pièges de l'étude 36 : `ETAT-REPRISE.md` § « Pièges à ne pas oublier ».

## 6. Historique des sessions

- **2026-10-14 — devoir D34** (session `session_018x5pAMz22vU4Pyc9g78NUm`) : un devoir de contrôle 1 photographié et transmis
  par le propriétaire (« génère les exercices dans la plate-forme ») passe par la salle blanche du gisement : lecture (orchestrateur),
  5 lignes, plan `content:gisement:plan`, auteur sonnet, audit opus à l'aveugle, livraison ; point de sauvegarde
  `wip/math-9eme-devoir-d34`.
- **2026-10-12 — fusion** demandée par le propriétaire : fermeture des sessions « corriger 9eme cours
  programme » (campagne 9ᵉ au patron, `session_017DVMtmHBncdZ2yhRVykbu9`) et
  « 36-gisement-examens-devoirs » (`session_0121C1nDUtcSUvXYZ6KNzYNz`, état poussé sur
  `wip/gisement-9eme-lots-en-ecriture` à 17 h 06 UTC) ; une seule session reprend l'ensemble à partir
  de ce fichier : « Contenu scolaire — campagne unique (patron + gisement) »
  (`session_01V4SP7MGyz9eESCxWQs7CSZ`).
