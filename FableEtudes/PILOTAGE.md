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
| maths (`math`) | ✅ 102905 lu | ✅ armé ; 01–02 recentrés, audités et publiés le 2026-10-12 (privé#660) | ✅ | ✅ (01–02 : audit opus du 2026-10-12, `_campagne-9eme-au-patron/maths-9eme/rapport-audit-recentrage.md`) | ✅ plan d'examens complet : L01–L21 publiés (195 missions ; L17 privé#664, L21 privé#666) ; **L22** (ch. 07/12/18, 3 missions, 21 q) audité (0 clé fausse, 8 majeurs), corrigé, re-vérifié et livré le 2026-10-12 | ⏳ devoirs du 1ᵉʳ trimestre publiés ; G2 (ch. 04) et I (ch. 09, après L21) planifiés — 10 missions `planifiee` | **réservé** session unique (2026-10-12) : devoirs **G2** (ch. 04, 5 missions, 38 q) audité (0 clé fausse, 10 majeurs), corrigé, re-vérifié et livré le 2026-10-12, contrôle anti-copie propre ; **I** (ch. 09) en tour de corrections (cartes régénérées depuis `lignes.tsv` ; transcriptions locales des devoirs refaites pour le contrôle anti-copie) ; lots : `wip/gisement-9eme-lots-en-ecriture` (PR #607), mode d'emploi dans `36-gisement-examens-devoirs/en-cours/ETAT-REPRISE.md` § « PASSAGE DE RELAIS » |
| SVT (`sciences-vie-terre`) | ✅ 105905 lu | ✅ armé le 2026-10-01 (14 ch. + 7 optionnels) | ✅ `bio.*` | ✅ | ⏳ L01–L04 publiés (23 missions `publiee`) ; **L05** (4 missions, ch. 12, 19 q) audité (0 clé fausse, 5 majeurs), corrigé, re-vérifié et livré le 2026-10-12 — **le plan d'examens SVT 2020–2026 (27 missions) est complet** ; sessions 2019→2001 (C07–C24) à lire | ❌ D01–D06 | **dette « clé la plus longue »** en cours de correction (correcteur sonnet → audit opus par lot, rapports dans `36-gisement-examens-devoirs/cle-longue-svt-9eme/`) : **12, 13, 14 corrigés le 2026-10-12** (58–87 % → 0 %), 09–11 en cours, 01–08 à faire ; puis lecture des sessions 2019→2001 (C07–C24) et devoirs D01–D06 ; ⚠️ **dette mesurée le 2026-10-12** : sur `main`, la clé est strictement l'option la plus longue dans **665/1025 questions (65 %)** de la SVT 9ᵉ (positions a 34 % · b 47 % · c 14 % · d 5 %) — les items d'origine des cours (quiz, `01`–`06`), pas les missions d'examen ; passe de correction (`correction-cle-longue.md`) à faire dans le même passage du couple ; même branche et même ETAT-REPRISE que les maths |
| physique-chimie (`svt`) | ✅ 103902 lu | ✅ armé le 2026-09-28 | ✅ | ✅ | — écarté (é36 D-10 : pas d'épreuve en filière générale) | — | — |
| arabe (`arabic`) | ✅ 101908 lu en entier, 101909 aux pages utiles (fiche `partielle` à dessein) | ✅ 19 chapitres réalignés (5 neufs), armé `notion` le 2026-10-12 | ✅ 197 ids `arabe.*` neufs + 17 réutilisés, 1 446 options (73 %), `coursePitfalls` sur les 19 ch. | ✅ A1–A4 + A4b (07–08) ; fusion du vocabulaire relue (opus) | ❌ 46 documents échantillonnés, 0 mission (chapitre 11 = annales) | ❌ | livré le 2026-10-12 (PR « arabe 9ᵉ au patron ») ; **prochaine action : gisement arabe 9ᵉ en un passage** ; doutes ouverts : `etiquettes/rapport-fusion.md` §6 (12 pièges sans distracteur qui les porte), relecture native des 38 libellés neufs ou réécrits souhaitée |
| français (`french`) | ✅ 121905 lu | ✅ armé le 2026-10-01 | ✅ `fr.*` | ✅ | ❌ 50 documents échantillonnés, 0 mission | ❌ | prochain couple du gisement après l'arabe |
| anglais (`english`) | ✅ 141906 + 141907 lus | ✅ armé le 2026-09-28 | ✅ | ✅ | ❌ 48 documents échantillonnés, 0 mission | ❌ | après le français |

### 6ᵉ (concours de 6ᵉ — après la 9ᵉ)

| Couple | Fiche / manuel | Cours au patron | Étiquettes | Audit | Gisement | En cours · prochaine action |
| --- | --- | --- | --- | --- | --- | --- |
| maths (`math-6eme`) | ⚠️ fiche `partielle/mixte`, 23 % (502603 et 102609 à trous) — `programme:etat` : génération interdite, contenu généré sous la barre R-5 | ✅ armé | ✅ | ✅ | ❌ | **LOT A d'abord** (compléter la fiche), puis gisement en un passage |
| arabe (`arabic-6eme`) | ⚠️ fiche `partielle/generation`, 100 % mais pas en profondeur R-5 — génération interdite | ✅ armé (19 ch.) | ✅ | ✅ | ❌ | profondeur R-5 de la fiche, puis gisement en un passage |
| éveil scientifique | ⚠️ fiche `partielle/mixte`, 57 % (503604 p. 103–180 à trous) — génération interdite | ✅ armé | ✅ | ✅ | ❌ | **LOT A d'abord**, puis gisement en un passage |
| anglais (`english-6eme`) | ✅ `validee-r7`, 100 % — génération autorisée | ⏳ écrit (7/7 ch.), pas armé | ❌ | ❌ | ❌ | patron + étiquettes + armement + gisement **en un seul passage** |
| français 6ᵉ | ❌ fiche `partielle/mixte`, 14 % | ❌ la matière n'existe pas | — | — | ❌ | LOT A, puis tout le reste en un passage |

## 3. File d'attente (ordre arbitré par le propriétaire : la 9ᵉ finie avant tout, puis la 6ᵉ)

1. ~~**Arabe 9ᵉ — finir et publier le patron**~~ livré le 2026-10-12 : A4 (07–08), vocabulaire A + B fusionné et
   complété (02, 03, 19), 1 446 étiquettes, armement `notion`, gates vertes, rendu des 19 cours propre ; reste
   la publication `subjects=arabic`, `content-drift` clos, fermer #634 et #637, `STATUS.md` du moteur ;
   5. puis le **gisement arabe 9ᵉ en un passage** (chapitre 11 annales + missions par chapitre ;
      registre `web-9eme-base-arabic/gisement.json`). ⚠️ le contexte lecteur
      `en-cours/lecture-9eme/arabe/reader-context.md` (étude 36) liste l'ANCIEN chapitrage : le
      régénérer depuis `manifest/9eme-base.json`.
2. ~~**Maths 9ᵉ 01–02**~~ audité, livré et publié le 2026-10-12 (§4) ; était : audit indépendant opus du recentrage, puis PR séparée (`content/math/01-*`,
   `02-*` seulement), `apply-content` `subjects=math`. Rapport du recentrage au §4.
3. **Gisement 9ᵉ restant**, chaque couple en un passage : maths (10 missions planifiées), SVT (correction de la clé la plus longue (65 %), lecture C07–C24, devoirs D01–D06), puis français, puis anglais.
4. **6ᵉ** : `english-6eme` puis `french-6eme`, puis le gisement des couples 6ᵉ déjà armés. ⚠️ Mesure du 2026-10-12 : les fiches de maths (23 %), d'éveil (57 %) et d'arabe 6ᵉ (pas en profondeur R-5) sont sous la barre — `programme:etat` y interdit la génération ; leur gisement passe d'abord par le LOT A (compléter la fiche), à confirmer avec le propriétaire avant de l'ouvrir.

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

- **2026-10-12 — fusion** demandée par le propriétaire : fermeture des sessions « corriger 9eme cours
  programme » (campagne 9ᵉ au patron, `session_017DVMtmHBncdZ2yhRVykbu9`) et
  « 36-gisement-examens-devoirs » (`session_0121C1nDUtcSUvXYZ6KNzYNz`, état poussé sur
  `wip/gisement-9eme-lots-en-ecriture` à 17 h 06 UTC) ; une seule session reprend l'ensemble à partir
  de ce fichier : « Contenu scolaire — campagne unique (patron + gisement) »
  (`session_01V4SP7MGyz9eESCxWQs7CSZ`).
