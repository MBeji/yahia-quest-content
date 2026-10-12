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

## 2. Tableau de bord (état mesuré le 2026-10-12)

Légende : ✅ fait · ⏳ en cours · ❌ à faire · — sans objet.

### 9ᵉ (année de concours — à finir avant tout le reste)

| Couple | Fiche / manuel | Cours au patron | Étiquettes | Audit | Gisement : examens | Gisement : devoirs | En cours · prochaine action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| maths (`math`) | ✅ 102905 lu | ✅ armé ; ⏳ 01–02 recentrés le 2026-10-12 (pas encore audités ni mergés) | ✅ | ✅ (01–02 : ❌) | ⏳ 184 missions publiées · 10 planifiées (L17, L21, L22 + devoirs G2, I) | ⏳ devoirs du 1ᵉʳ trimestre publiés | recentrage : branche `wip/arabe-9eme-patron` (chemins `content/math/01-*`, `02-*`) → audit puis PR à part · lots : état exact dans `36-gisement-examens-devoirs/en-cours/ETAT-REPRISE.md` (branche `wip/gisement-9eme-lots-en-ecriture`, PR #607) |
| SVT (`sciences-vie-terre`) | ✅ 105905 lu | ✅ armé le 2026-10-01 (14 ch. + 7 optionnels) | ✅ `bio.*` | ✅ | ⏳ 16 missions (11 publiées, 5 mergées) sur un plan de 27 ; 6 sessions lues (2020–2026), C07–C24 à lire | ❌ D01–D06 | lots SVT-L04 (en écriture au 2026-10-10), SVT-L05 (prêt) : voir ETAT-REPRISE |
| physique-chimie (`svt`) | ✅ 103902 lu | ✅ armé le 2026-09-28 | ✅ | ✅ | — écarté (é36 D-10 : pas d'épreuve en filière générale) | — | — |
| arabe (`arabic`) | ✅ 101908 lu en entier, 101909 aux pages utiles (fiche `partielle` à dessein) | ⏳ 19 chapitres réalignés (5 neufs) ; rendu corrigé | ⏳ partie A prête (63 ids, 8 ch. de grammaire) ; partie B ❌ ; 01, 06, 11 ❌ | ⏳ A1, A2, A3 ✅ ; A4 : 09–10 ✅, 07–08 ❌ | ❌ 46 documents échantillonnés, 0 mission (chapitre 11 = annales) | ❌ | branche `wip/arabe-9eme-patron` (PR #637 brouillon) ; notes : `FableEtudes/_campagne-9eme-au-patron/arabe-9eme/` |
| français (`french`) | ✅ 121905 lu | ✅ armé le 2026-10-01 | ✅ `fr.*` | ✅ | ❌ 50 documents échantillonnés, 0 mission | ❌ | prochain couple du gisement après l'arabe |
| anglais (`english`) | ✅ 141906 + 141907 lus | ✅ armé le 2026-09-28 | ✅ | ✅ | ❌ 48 documents échantillonnés, 0 mission | ❌ | après le français |

### 6ᵉ (concours de 6ᵉ — après la 9ᵉ)

| Couple | Fiche / manuel | Cours au patron | Étiquettes | Audit | Gisement | En cours · prochaine action |
| --- | --- | --- | --- | --- | --- | --- |
| maths (`math-6eme`) | ✅ (73 %) | ✅ armé | ✅ | ✅ | ❌ | gisement en un passage |
| arabe (`arabic-6eme`) | ✅ | ✅ armé (19 ch.) | ✅ | ✅ | ❌ | gisement en un passage |
| éveil scientifique | ✅ | ✅ armé | ✅ | ✅ | ❌ | gisement en un passage |
| anglais (`english-6eme`) | à vérifier (`programme:etat`) | ⏳ écrit, pas armé | ❌ | ❌ | ❌ | patron + étiquettes + armement + gisement **en un seul passage** |
| français 6ᵉ | ❌ fiche partielle | ❌ la matière n'existe pas | — | — | ❌ | LOT A, puis tout le reste en un passage |

## 3. File d'attente (ordre arbitré par le propriétaire : la 9ᵉ finie avant tout, puis la 6ᵉ)

1. **Arabe 9ᵉ — finir et publier le patron** (`wip/arabe-9eme-patron`) :
   1. audit A4 des chapitres **07 et 08** (mandat `audits/audit-A4.md` ; 09 et 10 sont faits, voir
      `rapport-A4.md`) ;
   2. étiquettes : fusionner `vocab-arabe9-A.json` dans `misconceptions.json` (vérifier les doublons
      avec les 122 `arabe.*` existants), lancer la partie B (`brief-vocab-B.md` : 12, 05, 13, 14, 09,
      10, 07, 08) **et y ajouter 01, 06, 11** : l'essai d'armement du 2026-10-12 donne 19 erreurs, toutes
      « pas de `coursePitfalls` » (C-5), aucune erreur de forme — les 19 chapitres doivent être tagués ;
      puis la pose par lots (modèle : les mandats `tag-*.md` du français) ;
   3. armer `coursePattern: "notion"` dans `content/arabic/subject.json`, `content:gates`,
      `content:catalogue` (committer `CATALOGUE.md`) ;
   4. livraison propre sur la branche désignée (recomposer : chapitres, programme, registre
      d'étiquettes, tags, armement, notes), merge, `apply-content` `subjects=arabic`, `content-drift`
      clos, fermer #634 et #637, ligne arabe 9ᵉ de `STATUS.md` (moteur) et de ce fichier ;
   5. puis le **gisement arabe 9ᵉ en un passage** (chapitre 11 annales + missions par chapitre ;
      registre `web-9eme-base-arabic/gisement.json`). ⚠️ le contexte lecteur
      `en-cours/lecture-9eme/arabe/reader-context.md` (étude 36) liste l'ANCIEN chapitrage : le
      régénérer depuis `manifest/9eme-base.json`.
2. **Maths 9ᵉ 01–02** : audit indépendant opus du recentrage, puis PR séparée (`content/math/01-*`,
   `02-*` seulement), `apply-content` `subjects=math`. Rapport du recentrage au §4.
3. **Gisement 9ᵉ restant**, chaque couple en un passage : maths (10 missions planifiées), SVT (L04,
   L05, lecture C07–C24, devoirs D01–D06), puis français, puis anglais.
4. **6ᵉ** : `english-6eme` puis `french-6eme`, puis le gisement des couples 6ᵉ déjà armés.

## 4. Rapport du recentrage maths 9ᵉ (2026-10-12, non mergé)

- `01-nombres-reels` (ch. 2 du manuel, p. 18–30) : 47 questions, 44 dans le chapitre, 3 hors (calcul
  dans ℝ, identité nommée) réécrites (02-boss#6, #7, 04-defi#5) ; le gros débordement signalé par la
  fiche §6.2 bis (valeur absolue, écriture scientifique, ordre, intervalles) n'était plus dans les
  fichiers ; un encadré « للتوسّع » renvoie au ch. 3.
- `02-racines-carrees` (ch. 3 §IV, p. 39–40, déf. p. 27) : 45 questions, 39 dans, 6 hors (Pythagore,
  trinôme carré parfait, carré d'une somme) réécrites ; vocabulaire d'identité retiré (le produit de
  conjugués reste, par double distributivité, p. 37) ; `coursePitfalls` : retrait de
  `math.geo.pythagore-sans-carres`, ajout de `math.num.radicaux-semblables-radicande-additionne`.
- Contrôles : `content:qa` 0 erreur 0 avertissement sur math/01–02 ; tranche 0/101 clé la plus longue.
- **À arbitrer** : « إنطاق المقام / المرافق » gardés (les ex. 16–17 p. 46–47 l'exigent, sans terme ni
  encadré dans le manuel, ≈ 10 questions) ; missions de l'étude 36 hors chapitre : 01/08-devoir#6 et #7
  (puissances 3²⁰²¹ → ch. 4), 01/08-devoir#1 (√27 = 3√3, forme a√b du ch. 3).

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
  programme » (campagne 9ᵉ au patron) et « 36-gisement-examens-devoirs » ; une seule session reprend
  l'ensemble à partir de ce fichier.
