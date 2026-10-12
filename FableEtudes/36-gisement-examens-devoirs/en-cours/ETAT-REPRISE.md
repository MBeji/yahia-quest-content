# État de reprise du gisement 9ᵉ (point de sauvegarde — passage de relais du 2026-10-12 ~17 h UTC ; journal chronologique en bas)

> Ce fichier est écrit pour la session qui reprend sans relire l'historique. La source de vérité de l'état
> des missions reste `content/programmes-officiels/sources-externes/web-9eme-base-<matière>/gisement.json`
> (registre) sur `main` ; ce qui suit dit **où l'on en est des lots** et **comment on avance**.

## ⭐ PASSAGE DE RELAIS — 2026-10-12 ~17h UTC (À LIRE D'ABORD)

**Ce bloc remplace les « à faire » des entrées chronologiques plus bas** (elles restent comme journal).

Contexte : un message relayé par la routine « Étude 36 — pousser l'état avant fusion des sessions » (session « corriger 9eme cours
programme », campagne « 9ᵉ au patron », « à la demande du propriétaire ») demande de fusionner la session étude 36 / gisement et la
sienne en UNE nouvelle session. Cette branche
(`wip/gisement-9eme-lots-en-ecriture`, PR draft privé#607) et ce fichier sont le point d'entrée. Rien de neuf n'a été lancé
par l'ancienne session après réception de la demande.

**Les agents de l'ancienne session ne sont pas reprenables depuis une autre session** (`SendMessage` ne les atteint pas) :
la nouvelle session relance de NOUVEAUX agents avec les prompts de `plan/` et les notes de `auteurs-notes/`.
Les trois auteurs en vol (SVT-L04 `a5e717…`, L17 `aac804…`, SVT-L05 `a7d82b…`) ont été coupés par la limite de session
le 10-12 entre 08h19 et 08h22 UTC (« resets 12:10pm UTC », 5ᵉ coupure, quota `five_hour`) : aucun agent ne tourne.

### Tableau des lots (état exact au 2026-10-12 17h UTC)

| Lot | Contenu | État | Référence | Prochaine action |
| --- | --- | --- | --- | --- |
| Math L01–L16, L18, L19, L20 | maths 9ᵉ, examens | **publiés et vérifiés** | dernier : L16 = privé#644 (apply-content run 38073564538) | rien |
| Registre math (`main`) | 195 entrées | 184 `publiee` · 10 `planifiee` (devoirs G2/I) · 1 `ecartee` | — | L17, L21, L22 ne sont pas encore au registre |
| **Math L17** | ch.18 NN36–41 (2013 ex4 · 2016 ex4 · 2018 ex4 · 2019 ex3 · 2019 ex4 · 2020 ex5), 63 q | **en écriture, quasi fini** : les 6 fichiers sont écrits (lot-lint 0, bench-rtl 0, double résolution) ; il manque les gates officielles `content:gates -- --tranche`, `pending-tags/L17.json` (aucune étiquette neuve : toutes existent sur `main` ; seulement d'éventuels placements hors lot) et le rapport | `EN-VOL.md`, `auteurs-notes/l17/NOTES.md` (les « À vérifier par l'auditeur » de chaque mission y sont) | lancer les gates ; créer `auditspec/L17.json` (modèle : `plan/auditspec/L16.json`) et le prompt par `outils/gen-prompt-audit.py` ; audit opus en aveugle ; arbitrage ; tour de corrections ; re-vérification ; `deliver-lot.sh L17 18-quadrilateres 36 37 38 39 40 41` |
| Math L21 | ch.09 NN47–48 | planifié (prêt à lancer : L14, même chapitre, est publié) | `plan/prompt-L21.md`, `plan/assign-L21.md` | lancer un auteur (sonnet) |
| Math L22 | ch.07 NN25, ch.12 NN22, ch.18 NN42 | planifié | `plan/prompt-L22.md`, `plan/assign-L22.md` | après L17 (ch.18 NN42 : un seul auteur par chapitre à la fois) |
| Devoirs G2 / I | ch.04 NN29–33 ; ch.09 NN42–46 | planifiés (10 missions `planifiee`) | `plan/prompt-G2.md`, `plan/prompt-I.md` | G2 : prêt (ch.04 libre) ; I : après L21 (même chapitre) |
| SVT L01 (6 missions), L02 (5) | ch.02/05/07 ; ch.03 | **publiés** | privé#640, privé#652 | rien |
| **SVT L03** | ch.08 NN07–11, 5 missions, 31 q | **publié et vérifié** : privé#654 mergé (`df5936e2`), apply-content run 38221872005 (étapes 19–21 vertes), content-drift run 38280128839 vert, 0 issue `content-drift` | `outils/spec-pub-SVT-L03.json` (pr privé#654) | **basculer les 5 missions `mergee` → `publiee`** à la prochaine livraison SVT : `registre-set.py <gisement.json SVT> spec-pub-SVT-L03.json` |
| **SVT L04** | ch.09 NN07–09, ch.10 NN07, ch.11 NN07–09 : 7 missions, 31 q | **audité, arbitré, tour de corrections NON COMMENCÉ dans les fichiers** (voir ci-dessous) | `audits/audit-SVT-L04.md` (opus `abd023…`, 0 clé fausse, 2 majeurs, 16 mineurs), `plan/arbitrage-SVT-L04.md` (consigne d'arbitrage mot pour mot), `auteurs-notes/svt-l04/` (NOTES + générateurs) | voir « SVT-L04, marche à suivre » |
| **SVT L05** | ch.12 NN07–10 (2026 ex2 · 2022 ex1 · 2025 ex3 · 2024 ex4), 4 missions | **rien d'écrit** : l'auteur n'a fait que lire (sujets, PDF, cours) | `plan/prompt-svt-L05.md`, `plan/assign-svt-L05.md`, `auteurs-notes/svt-l05/NOTES.md` (constats de lecture utiles : tags `bio.*` pertinents, notions absentes des cours à donner dans chaque énoncé, relevés des figures 2024/2025) | lancer un auteur (sonnet) ; c'est le dernier lot du plan SVT (27 missions) |
| Registre SVT (`main`) | 16 entrées | 11 `publiee` (L01, L02) · 5 `mergee` (L03) | — | L04 (7) et L05 (4) à ajouter par `deliver-lot-svt.sh` (via `gen-spec-lot.py`) |
| Arabe 9ᵉ | — | **en réalignement par l'autre session (manuel 101908) : ne rien y placer** tant que la fusion n'est pas signalée dans l'`ETUDE.md` §8 | — | — |
| Français, anglais 9ᵉ | — | lecture des sessions non commencée ; registres sur `main` (échantillons fixés) | `lecture-9eme/<matière>/` (docs.json, machine-list.tsv, contexte lecteur) | après SVT |
| 6ᵉ | — | rien de lancé | sondes dans l'ancien scratchpad (perdues) | après la 9ᵉ |

**Dans cette branche, seuls les fichiers `content/**` listés dans `EN-VOL.md` sont vivants.** Les autres copies de
`content/**` (math 03/04/07/08/09/12/18/20, SVT 02/03/05/07/08) sont d'anciennes versions pré-correction de lots déjà
publiés : la bonne version est sur `main` — ne jamais les reprendre (la branche est basée sur un ancien `main`).

### SVT-L04, marche à suivre

1. L'état des fichiers : les 7 fichiers de `content/sciences-vie-terre/{09-al-ikhraj,10-an-nudj-al-jinsi,11-ad-dawra-al-jinsiya}/exercices/`
   sur cette branche sont **la version auditée (avant corrections)**. Ils sont la sortie exacte des générateurs
   `auteurs-notes/svt-l04/gen_m1..7.py` (+ `figs_*.py`, `lib.py`) : l'auteur a vérifié que la régénération redonne
   les mêmes empreintes (`sha_before_regen.txt`) juste avant la coupure, sans avoir encore modifié un générateur.
   Le plus sûr : modifier les générateurs, régénérer, puis `lot-lint` + gates + rendu Chromium `dir=rtl`.
2. Les corrections à appliquer sont dans `plan/arbitrage-SVT-L04.md` (2 majeurs + 16 mineurs de l'audit, étiquettes existantes à
   changer, deux familles neuves A `bio.nerv.substances-grise-blanche-confondues` et B `bio.circ.capillaire-comme-l-artere`
   avec leurs placements hors lot, terme « الكريّة القطبيّة », préfixe « العنصر X: », pas de lettre latine comme repère de figure).
   **Règle d'or** : un texte de remplacement fourni par un audit s'est révélé défectueux cinq lots de suite — vérifier chaque
   texte (énoncé, PDF officiel, cours, vote option par option et case par case, longueurs, fuites vers les autres questions,
   rendu Chromium) avant de l'écrire.
3. Écrire `pending-tags/SVT-L04.json` au format de `etiquettes/SVT-L03.json` (`matiere: "sciences-vie-terre"`, `nouvelles`,
   `options`, `hors_lot` avec `remplace` lu sur `origin/main`).
4. Re-vérification ciblée par un auditeur opus (l'ancien, `abd023…`, n'est pas atteignable : lui donner `audits/audit-SVT-L04.md`
   et les fichiers corrigés, et lui demander de re-résoudre chaque question retouchée) — elle trouve toujours du neuf.
5. Livraison : `deliver-lot-svt.sh SVT-L04 09-al-ikhraj:07,08,09 10-an-nudj-al-jinsi:07 11-ad-dawra-al-jinsiya:07,08,09`,
   `mk-pending.py SVT-L04`, `apply-tags.py <worktree> pending-tags/SVT-L04-deliver.json pending-tags/SVT-L04-extras-NN.json --write`
   (puis restaurer les fichiers publiés au format Prettier — voir « Pièges »), `registre-set.py` avec `spec-pub-SVT-L03.json`,
   CATALOGUE.md régénéré **et committé**, gates, PR (branche désignée), publication `sciences-vie-terre`, content-drift.
   Créer `spec-pub-SVT-L04.json` (numéro de PR) pour la bascule à la livraison de L05.
6. **À livrer dans le même commit (tâche #69, hors périmètre de l'audit §12)** :
   - `content/sciences-vie-terre/11-ad-dawra-al-jinsiya/cours.md`, ligne 49 — l'exemple est faux (le cycle fait 28 jours) :
     remplacer `من يوم 5 إلى نهاية الشّهر: 30 − 5 = 25 يومًا، ثمّ يومان (1 و2) من الشّهر الموالي ← **27 يومًا**.`
     par `من يوم 5 إلى نهاية الشّهر: 30 − 5 + 1 = 26 يومًا، ثمّ يومان (1 و2) من الشّهر الموالي ← **28 يومًا**.`
     (la ligne 32, « 28 − 1 = 27 », est juste : ne pas y toucher) ;
   - `content/misconceptions.json`, étiquette `bio.cycle.ovulation-au-milieu-du-cycle` (15 options publiées) : libellés à
     harmoniser avec le cours et la clé de 13/quiz Q3 (jour 12 pour un cycle de 26 jours) —
     fr « Tu places toujours l'ovulation au milieu du cycle : elle a lieu 14 jours avant la fin du cycle, soit le jour « durée du cycle moins 14 ». » ;
     en « You always put ovulation mid-cycle: it happens 14 days before the end of the cycle, i.e. on day cycle length minus 14. » ;
     ar « تضع الإباضة دائمًا في منتصف الدّورة: تقع قبل نهاية الدّورة بـ14 يومًا، أي في اليوم «طول الدّورة ناقص 14». »

### Suites moteur (dépôt public `yahia-quest-arena`, tâche #70 — priorité basse)

- Le bloc « question fatale » du donjon (`src/routes/_authenticated/dungeon.tsx` ~l.424, `t.dungeon.fatalQuestion`) et les résultats d'examen
  ne posent pas `dir` d'après `hasArabicLetters` (la carte de question, l. ~516, le fait).
- QA : ajouter le motif « الوثيقة » (et variantes) à `FIGURE_REFERENCE` (`scripts/content/qa-checks.ts` l.160, utilisé l.542 ;
  `qa-lesson-checks.ts`) pour attraper un énoncé qui renvoie à une figure qu'il ne porte pas — **lancer d'abord sur tout le corpus
  pour mesurer les faux positifs** (le donjon tire les questions seules).

### Autres suites ouvertes (inchangées)

- Refaire le devoir 14 de ch.09 (copie les données de l'examen 2015, tâche #33) ; corriger les devoirs 11 et 12 de ch.09 (#35).
- Cours : 04 (valeur absolue et intervalles, #23), 07 (étendue, classe modale, cumuls, médiane graphique, #25), 08 (partage d'un
  segment en parties égales par Thalès, #27) ; math ch.12 enseigne les vecteurs alors que R-3 n'en veut pas en 9ᵉ (#24, arbitrage du propriétaire).
- La garde `content-audit` (jeton `CLAUDE_CODE_OAUTH_TOKEN`, privé#614) : voir privé#651 (étude 37 : abonnement suspendu du 2 au 8 octobre) avant d'escalader.
- Entrée de journal `ETUDE.md` §8 et ligne `STATUS.md` (moteur) pour les événements du 10-11 et 10-12 (SVT-L02, SVT-L03 publiés ; 4ᵉ et 5ᵉ coupures) : non faites.
- Issue `garde-rouge` privé#656 ouverte le 10-12 : 2 runs « Content CI » rouges sur la PR #637 de l'autre session
  (`wip/arabe-9eme-patron`, étape `content:catalogue` : CATALOGUE.md périmé). Pas un défaut de l'étude 36 ; se referme seule
  quand une fenêtre de 8 h est verte.

### Pièges du jour et d'environnement

- **Les scripts de `outils/` codent en dur le scratchpad de l'ancienne session** (`SP=/tmp/claude-0/-home-user/b03814da-…/scratchpad`) et un moteur
  local `/home/user/eng-gisement` : poser `SP` au début de chaque script et recréer le moteur (clone d'`yahia-quest-arena`,
  `git checkout --detach origin/main`, `npm ci`, lien `content` → worktree du corpus ; les CA sont posées par le hook de session du moteur).
  `engine-env.sh` montre les variables utilisées.
- **Ne jamais committer l'arbre partagé `/home/user/yahia-quest-content`** de l'ancienne session (périmé, 415 fichiers modifiés) ;
  tout ce qui comptait est copié ici.
- Le quota est `five_hour` : plusieurs coupures depuis le 10-01 (la 5ᵉ numérotée dans ce fichier le 10-12), toujours avec 3 ou 4 agents lourds
  (auditeurs opus) en parallèle ; à la coupure, les agents meurent. Demander aux agents d'écrire notes et rapports au fil de l'eau (un agent coupé avant d'avoir écrit perd son travail apparent).
- `apply-tags.py` réécrit les fichiers publiés au format canonique : restaurer les fichiers Prettier (SVT 08 `01-tamrin`, `04-defi`, `06-defi-concours`,
  `quiz.json` ; math 18/03-revision, 20/02-boss, 09/06-defi-concours) par `git show HEAD:` + édition chirurgicale de la seule valeur
  `misconceptionTag`, et vérifier `json.loads(nouveau) == json.loads(version apply-tags)`.
- Le portail pose des pastilles A–D sur les options mélangées : jamais de lettre latine comme repère de figure dans une question à options (numéroter 1–4).
- Les figures SVG sont `dir="ltr"` (arena#1154) ; la bidi du moteur est dans `src/shared/lib/bidi.ts` (correctifs arena#1159, #1160 mergés).
- Les consignes `.claude/skills/content-ingest/references/gisement-auteur-examen.md` et `gisement-auditeur.md` (pièges L14/L16 : grille 2×2 complète
  par case, prémisses vraies, retirer plutôt que déplacer un repère de figure…) sont sur `main` depuis privé#647 — les donner aux nouveaux agents.

## Le geste d'un lot d'examen (math, validé sur dix lots)

1. `gen-exam-assign.py` (math) ou `gen-exam-assign-subj.py` (autres matières) → `assign-<lot>.md` ;
   prompt d'auteur (`prompt-L*.md`, `prompt-svt-L*.md` via `gen-prompt-svt.py`) ; **un auteur par chapitre à la fois**,
   plages de NN explicites, ≤ 4 agents en parallèle ; auteurs/lecteurs sonnet, auditeurs opus.
2. `lot-lint.mjs` sur les fichiers de l'auteur → audit en aveugle (prompt-audit-*.md, consigne `gisement-auditeur.md`)
   → l'auteur applique → **re-vérification ciblée par le même auditeur** (elle trouve toujours du neuf, surtout dans
   les textes de remplacement fournis par l'audit) → livraison.
3. Livraison : `deliver-lot.sh <lot> <chapitre> <NN…>` (worktree frais d'`origin/main`, copie, ligne `sources[]`,
   registre `mergee`, gates), `apply-tags.py` + `mk-pending.py` pour les étiquettes, `registre-set.py` pour
   passer les missions précédentes à `publiee` (specs `spec-pub-*.json`), CATALOGUE.md régénéré **et committé**,
   dernier commit descriptif (le titre du squash = dernier commit), branche `claude/upbeat-knuth-hot71t`,
   une seule PR privée ouverte à la fois.
4. Après le merge : `apply-content.yml` en `workflow_dispatch` `{"subjects":"<matière>","dry_run":"false"}` ;
   vérifier « Appliquer le contenu », « Vérifier que le contenu est bien en base », « Journaliser la release » ;
   puis `content-drift.yml` ; l'issue `content-drift` doit être close.

## Lots math 9ᵉ (au 2026-10-02 07h40 UTC)

- publiés et vérifiés (3 étapes apply-content + content-drift) : L01–L13 sauf L09 flip, L15, L18, L19 ; registre : 161 missions `publiee`.
  Reste à FLIPPER dans le registre (à la prochaine livraison) : L18 → `spec-pub-L18.json` (privé#628 publié). (L09 et L13 sont déjà flippés.)
- REPRISE 2026-10-09 13h20 UTC : les quatre agents (auditeurs L14 a0755e58afc4f234e, L16 a91e1972bd3cca321, L20 a40053c95bd3fbf21 ; auteur SVT-L01 af789b7b2beb04d47) ont été coupés le 10-02 ~08h57 UTC par la limite de session (« resets 12pm UTC ») ; renvoyés par SendMessage le 10-09 ~13h20 avec leurs rapports partiels (audit-L14.md 36 ; audit-L16.md 29-31 ; audit-L20.md 27-30 ; SVT : 02/07, 02/08, 05/07 corrigés, reste 05/08, 07/08, ancres, lot-lint, gates, rapport). Aucun commit sur les deux `main` entre-temps. arena#1154 (figures dir=ltr) mergé le 10-02.
- ÉTAT 2026-10-10 ~17h UTC : L20 LIVRÉ (wt-L20 / t-L20, commit 8d23a869 poussé sur la branche désignée : 5 missions, 26 questions, étiquette neuve math.alg.carre-difference-ecrit-difference-carres + réétiquetage de 03/22 Q1 c et 09/24 Q5 b ; registre : L18 → publiee (166), L20 → mergee). Après fusion : apply-content math (subjects "math", dry_run "false"), vérifier les 3 étapes, content-drift ; basculer L20 → publiee à la prochaine livraison (créer `spec-pub-L20.json` avec la PR). Agents repris le 10-10 après une 2ᵉ coupure (« resets 6:10pm ») : auteurs L14 (a703138…), L16 (a86e1a…), SVT-L01 (af789b7…, dernier tour) ; nouvel auteur SVT-L02 (aefa6b9…, ch.03 NN07–11). À faire ensuite : re-vérification L14/L16 par les MÊMES auditeurs (L14 a0755e58…, L16 a91e1972…) puis livraison ; SVT-L01 : `deliver-lot-svt.sh SVT-L01 02-al-af3al-al-in3ikasiya:07,08 05-al-hadm:07,08 07-ad-dawaran:07,08`, `mk-pending.py SVT-L01`, `apply-tags.py <wt> pending-tags/SVT-L01-deliver.json --write`. Moteur : arena#1159 (lockfile) et #1160 (π et « ° ») mergés le 10-09.
- ÉTAT 2026-10-12 ~09h UTC (15) : SVT-L03 LIVRÉ (commit 0777fcd7 poussé ; re-vérification a46772… : 0 clé fausse, 0 majeur ; 3 retouches finales appliquées ; 2 étiquettes neuves bio.resp.* + 4 placements hors lot sur ch.08 publié, fichiers publiés Prettier restaurés par édition chirurgicale ; L02 → publiee dans le même commit). À faire : PR auto-ouverte → abonner → merge → `apply-content` {subjects: sciences-vie-terre} → 3 étapes → content-drift ; `spec-pub-SVT-L03.json` créé (remplacer PR_A_REMPLIR) pour la bascule à la prochaine livraison SVT. Agents encore actifs : audit SVT-L04 abd02… , auteur L17 aac80… . SVT-L05 (ch.12 NN07–10) à lancer maintenant (2 slots libres).
- ÉTAT 2026-10-12 ~07h45 UTC (14) : SVT-L02 PUBLIÉ ET VÉRIFIÉ (privé#652, 6891f416 ; apply-content run 38218185921 étapes 19–21 vertes ; drift propre). À basculer avec la prochaine livraison SVT : L02 → publiee (`registre-set.py <registre SVT> spec-pub-SVT-L02.json`, pr privé#652 ; ids C04#2, C06#2, C01#3, C02#4, C05#5). SVT-L03 : tour de corrections FINI (auteur aa59a1d…, pending-tags/SVT-L03.json) ; RE-VÉRIFICATION demandée à a46772… (reverif-SVT-L03.md). Autres agents : audit SVT-L04 abd02… , auteur L17 aac80… (36–38 écrits).
- ÉTAT 2026-10-12 ~08h UTC (13) : SVT-L02 LIVRÉ (commit b534ec79 poussé sur claude/upbeat-knuth-hot71t ; re-vérification af899… : 0 clé fausse, 0 majeur, dernier correctif 10 Q1 b/c appliqué ; 1 étiquette neuve bio.vis.difference-non-montree). À faire : PR auto-ouverte → abonner → merge → `apply-content` {subjects: sciences-vie-terre} → 3 étapes → content-drift ; flip L02 → publiee à la prochaine livraison SVT (`spec-pub-SVT-L02.json` créé, remplacer PR_A_REMPLIR). Les 3 autres agents (SVT-L03 corrections, SVT-L04 audit, L17 auteur) tournent.
- ÉTAT 2026-10-12 ~07h30 UTC (12) : 4ᵉ COUPURE le 10-11 vers 10h42 UTC (« resets 2:50pm UTC ») ; session reprise le 10-12 07h24 UTC (modèle repassé à Sonnet 5.5 : attribution « Co-Authored-By: Claude Sonnet 5.5 »). Les 4 agents repris par SendMessage à 07h25 : re-vérification SVT-L02 af899… (reverif-SVT-L02.md 11 Ko), audit SVT-L04 abd02… (rapport 765 o), tour de corrections SVT-L03 aa59a1d… (NOTES 10 Ko), auteur L17 aac80… (36, 37, 38 écrits ; 39–41 à écrire). Un autre agent (session étude 37) a mergé privé#651 sur main entre-temps (docs étude 37 seulement : aucun conflit attendu avec les lots). Plan ensuite : re-vérif SVT-L02 → livraison SVT-L02 ; fin du tour SVT-L03 → re-vérif a46772… → livraison ; audit SVT-L04 → arbitrage ; L17 → audit opus → arbitrage ; SVT-L05 (ch.12 NN07–10) à lancer quand un slot se libère.
- ÉTAT 2026-10-11 ~11h25 UTC (11) : SVT-L04 : auteur a5e71… a RENDU (7 missions, 31 q) ; audit opus abd02398a35369a49 LANCÉ (auditspec/SVT-L04.json, prompt-audit-SVT-L04.md, rapport audit-SVT-L04.md). Agents (4) : re-vérification SVT-L02 af899…, tour de corrections SVT-L03 aa59a1d…, audit SVT-L04 abd02…, auteur L17 aac80…. SVT-L05 (ch.12 NN07–10) toujours pas lancé (prompt prêt) : au prochain rendu.
- ÉTAT 2026-10-11 ~10h55 UTC (10) : SVT-L02 : tour de corrections FINI (auteur aefa6b9… ; pending-tags/SVT-L02.json écrit : bio.vis.difference-non-montree sur 11 Q2 b, 11 Q3 a) ; RE-VÉRIFICATION demandée à af899… (reverif-SVT-L02.md ; version auditée = wt-sav2 99ae05ba). Arbitré : figures 09 (allongement postérieur) et 11 (rapport 1,9) acceptées comme accentuations ; NOTE DE LIVRAISON 09 : le scan montre surtout une cornée plus bombée (+5,9 % au total), la figure reporte l'allongement sur le globe (+14 %). Ensuite : `deliver-lot-svt.sh SVT-L02 03-al-ibsar:07,08,09,10,11`, `mk-pending.py SVT-L02`, `apply-tags.py <wt> pending-tags/SVT-L02-deliver.json --write`, contrôle des diffs (format Prettier), gates, PR, publication sciences-vie-terre, drift.
- ÉTAT 2026-10-11 ~10h40 UTC (9) : privé#647 (journal + consignes + registre L16 → 184 publiee) et arena#1163 (ligne STATUS 2026-10-10) MERGÉS ; drift propre. AUDITS RENDUS : SVT-L02 (af899… : 0 clé fausse, 4 majeurs, 17 mineurs ; étiquette neuve bio.vis.difference-non-montree acceptée sur 11 Q2 b et 11 Q3 a ; 09 reste boss d3, Q4 → d2) ; SVT-L03 (a46772… : 0 clé fausse, 9 majeurs, 15 mineurs ; 2 étiquettes neuves acceptées bio.resp.appareil-fabrique-l-oxygene et bio.resp.respiration-photosynthese-confondues, avec placements hors lot sur ch.08 publié). TOURS DE CORRECTIONS EN COURS : auteur SVT-L02 aefa6b9… (pending-tags/SVT-L02.json), auteur SVT-L03 aa59a1d… (pending-tags/SVT-L03.json). Puis re-vérification par les MÊMES auditeurs (af899… pour L02, a46772… pour L03) → livraisons SVT (deliver-lot-svt.sh) une par une, avec bascule L16/L14 déjà faites ; à la prochaine livraison SVT rien à basculer côté maths. Auteurs SVT-L04 a5e71… et L17 aac80… toujours en écriture.
- ÉTAT 2026-10-11 ~10h05 UTC (8) : 3ᵉ COUPURE le 10-10 vers 18h15 UTC (« resets 10pm (UTC) ») : les 4 agents repris par SendMessage le 10-11 à 09h58 UTC (auditeur SVT-L02 af899… : rapport pas encore créé ; auditeur SVT-L03 a46772… : rapport avec fichier 07 ; auteur SVT-L04 a5e71… : NOTES seulement ; auteur L17 aac80… : NOTES seulement). Modèle de la session principale passé à Opus 5.5 par le propriétaire (attribution des commits : « Co-Authored-By: Claude Opus 5.5 »). PR privée #647 (journal §8 du 10-10, consignes auteur/auditeur L14-L16, registre L16 → publiee : 184 publiee) ouverte, abonnée. PR moteur à venir : ligne STATUS.md 2026-10-10 (worktree wt-arena-status, branche t-status-1010, node_modules liés depuis eng-gisement ; verify en cours, log verify-status-1010.log) — à pousser sur claude/upbeat-knuth-hot71t, PR draft puis suivi.
- ÉTAT 2026-10-10 ~18h07 UTC (7) : L16 PUBLIÉ ET VÉRIFIÉ (apply-content run 38073564538 étapes 19–21 vertes ; drift : issue #645 close ; 0 issue content-drift ouverte). À basculer à la prochaine livraison : L16 → publiee (`registre-set.py <registre math> spec-pub-L16.json`, 7 missions C01#4, C05#4, C06#4, C08#4, C09#5, C10#4, C11#5). Math 9ᵉ : registre = 177 publiee + 7 (L16, à basculer), restent planifiées : L17 (auteur en cours), L21, L22, + devoirs G2 et I.
- ÉTAT 2026-10-10 ~18h UTC (6) : L16 MERGÉ (privé#644, aa74db87) ; apply-content math run 38073564538 en cours (dispatché 17:53) ; check-in programmé 18:02 → étapes 19–21, content-drift, puis rien d'autre (flip L16 = prochaine livraison, spec-pub-L16.json prêt, pr privé#644). AGENTS (4) : auditeur SVT-L02 af89908212766f1a6 (audit-SVT-L02.md), auditeur SVT-L03 a4677275eb7730d12 (audit-SVT-L03.md ; l'auteur aa59a1d… a rendu : 31 q ch.08 ; deux familles à juger : bio.resp.equation-respiration-a-l-envers et bio.resp.appareil-fabrique-l-oxygene), auteur SVT-L04 a5e717497cfd50810 (svt-l04-work), auteur math L17 aac8042869f2a3aec (l17-work ; pending-tags/L17.json). Guides gisement-auteur-examen.md et gisement-auditeur.md COMPLÉTÉS le 10-10 (pièges L14/L16 : grille 2×2 par case, retirer une figure plutôt que déplacer, étiquettes angle-droit-mauvais-sommet / fonction-trigo-mal-choisie) dans l'arbre partagé : À COMMITER avec la prochaine livraison (copier les deux fichiers de /home/user/yahia-quest-content/.claude/skills/content-ingest/references/ dans le worktree). Sauvegardes avant modif : scratchpad/*.md.avant-10-10.
- ÉTAT 2026-10-10 ~18h10 UTC (5) : L16 = privé#644 ouverte (auto-pr), abonnée ; spec-pub-L16.json prêt (pr privé#644). SVT-L02 : l'auteur (aefa6b9…) a rendu (5 fichiers ch.03 NN07–11, 23 questions) ; audit opus af89908212766f1a6 LANCÉ (prompt-audit-SVT-L02.md ; auditspec/SVT-L02.json ; rapport audit-SVT-L02.md). SVT-L04 : auteur a5e717497cfd50810 LANCÉ (prompt-svt-L04.md, dossier svt-l04-work). SVT-L03 : auteur aa59a1d7c1b4872f1 toujours en cours (fichiers ch.08 NN07–11 écrits). SVT-L05 (ch.12 NN07–10) pas lancé (prompt prêt) : attendre un rendu pour rester à 4 agents. Cartes PDF SVT : C01=2026, C02=2025, C03=2024, C04=2022, C05=2021, C06=2020.
- ÉTAT 2026-10-10 ~18h UTC (4) : L16 LIVRÉ (commit 3f267c62 poussé sur claude/upbeat-knuth-hot71t, PR auto-ouverte par auto-pr.yml ; 1 étiquette neuve math.geo.fonction-trigo-mal-choisie ; L14 → publiee dans le même commit ; 30 Q2 c et 32 Q4 d relabellisés angle-droit-mauvais-sommet). À faire : abonner la PR, après merge dispatcher apply-content math + 3 étapes + content-drift ; basculer L16 → publiee à la prochaine livraison (`spec-pub-L16.json` créé, remplacer PR_A_REMPLIR par le numéro de la PR). Les deux auteurs SVT n'ont pas encore rendu (fichiers NN07–11 écrits).
- ÉTAT 2026-10-10 ~17h45 UTC (3) : L14 LIVRÉ ET PUBLIÉ (privé#642, commit f9fdfeb5 ; apply-content math run 38072038557 étapes 19–21 vertes ; content-drift run 38072720009, issue #643 close). Le même merge a basculé SVT-L01 → publiee (6 missions). RESTE : basculer L14 → publiee à la prochaine livraison (`registre-set.py <registre math> spec-pub-L14.json`, prêt, pr privé#642 : C03#4, C07#4, C12#4, C14#4, C16#4, C20#3). Livraison suivante : L16 (re-vérification a91e1972… presque finie : reverif-L16.md a ses 7 sections) puis SVT-L02 / SVT-L03 (auteurs ont écrit NN07–11, rapports attendus). Moteur local /home/user/eng-gisement remis à origin/main bffcca85 + npm ci le 10-10 17h20.
- ÉTAT 2026-10-10 ~17h UTC (2) : SVT-L01 LIVRÉ ET PUBLIÉ (privé#640, commit 18c8a7ac ; apply-content run 38069021133, étapes 19–21 vertes ; content-drift run 38069455296 vert, issue #641 close, 0 issue ouverte). Reste à faire pour SVT-L01 : basculer les 6 missions `mergee` → `publiee` à la prochaine livraison (`registre-set.py <registre SVT> spec-pub-SVT-L01.json`, déjà créé, pr privé#640). L14 : l'auteur (a703138…) a rendu (tout l'audit appliqué sauf 41 Q2, décision motivée) ; pending-tags/L14.json écrit (2 étiquettes neuves : math.geo.angle-droit-mauvais-sommet, math.geo.droites-remarquables-confondues ; 17 options dans le lot, 12 hors lot) ; RE-VÉRIFICATION demandée au MÊME auditeur a0755e58afc4f234e (rapport attendu : author/exam/reverif-L14.md) → puis `deliver-lot.sh L14 09-triangle-rectangle-trigo 36 37 38 39 40 41`, `mk-pending.py L14`, `apply-tags.py <wt> pending-tags/L14-deliver.json pending-tags/L14-extras-NN.json --write`, gates, PR, apply-content math, content-drift, flip L14 (spec-pub-L14.json). L16 : l'auteur (a86e1ad…) a rendu (tout l'audit appliqué sauf 33-Q3 facultative ; pending-tags/L16.json écrit : étiquette neuve math.geo.fonction-trigo-mal-choisie, 2 options dans le lot + 3 hors lot ch.09) ; RE-VÉRIFICATION demandée au MÊME auditeur a91e1972bd3cca321 (reverif-L16.md attendu ; version auditée = `git -C wt-sav2 show 9bcf5e2b:content/math/18-quadrilateres/exercices/<fichier>`) → puis `deliver-lot.sh L16 18-quadrilateres 29 30 31 32 33 34 35`. Points à trancher laissés à l'auditeur : 32-Q6 a/b/c étiquetés condition-suffisante-supposee (l'auteur a désobéi à la consigne « muets » car les nouveaux textes exécutent exactement l'erreur), 31 en challenge d4 avec 4 vraies d3. Toujours en cours : auteurs SVT-L02 (aefa6b9ce5518cd50) et SVT-L03 (aa59a1d7c1b4872f1) + les deux auditeurs en re-vérification. Cap de 4 agents atteint : ne pas en lancer d'autre avant un rendu. Tâches suivies : #58 (L16), #61 (L14), #64 (SVT-L02), #65 (SVT-L03).
- ÉTAT 2026-10-09 ~14h UTC : audits rendus et arbitrés → tours de corrections EN COURS chez les auteurs : SVT-L01 (corrigé par l'auteur af789…, re-vérification par ac850… en cours, reverif-SVT-L01.md), L20 (auteur a6b508… : 4 majeurs, reprend aussi le fichier 31, écrit pending-tags/L20.json pour la nouvelle étiquette `math.alg.carre-difference-ecrit-difference-carres` + réétiquetage hors-lot 03/22 Q1 c et 09/24 Q5 b), L16 (auteur a86e1a… : 21 questions à reprendre, 33/34 → boss d3, 31 selon le recompte ; pending-tags/L16.json pour `math.geo.fonction-trigo-mal-choisie` + hors-lot 09/03-Q6, 09/06-Q1, 09/06-Q6) ; L14 : audit opus encore en cours (a0755e… ; audit-L14.md ~41 Ko). Chaque tour se termine par : re-vérification du MÊME auditeur → `deliver-lot.sh` (math) / `deliver-lot-svt.sh` (SVT) → apply-tags (`mk-pending.py` garde `remplace`) → CATALOGUE → PR privée → apply-content.
  Moteur : arena#1154 (figures dir=ltr), #1159 (journal STATUS + lockfile : dompurify 3.4.16, seroval 1.6.9, source-map-js 1.2.2 — avis npm du 10-02..09 ; `npm update` ciblé, PAS `npm audit fix` qui tire miniflare 5 alpha) mergés ; #1160 en cours (π/lettres grecques et « ° » dans DIGIT_FIRST_FORMULA). Statut Vercel « failure » sur 2fc46458 (non requis, cause inconnue, build local OK) : à vérifier sur main et sur #1160.
- en cours au 2026-10-02 08h30 UTC : les trois auteurs ont rendu (L14 ch.09 NN36–41 62 Q ; L16 ch.18 NN29–35 73 Q ; L20 ch.03 NN27–31 29 Q dont 31 = ex-L18) ; les trois audits opus en aveugle tournent
  (L14 a0755e58afc4f234e, L16 a91e1972bd3cca321, L20 a40053c95bd3fbf21 ; prompts `prompt-audit-L*.md`, rapports `audit-L*.md` dans author/exam ; specs `auditspec/L*.json`).
  À l'audit rendu : arbitrage → SendMessage à l'auteur (L14 a703138b8a79595c8, L16 a86e1adf6dd7a4114, L20 a6b508df10501b321 : ils sont terminés, un envoi les reprend avec leur contexte) → re-vérification ciblée du MÊME auditeur → `deliver-lot.sh` → fusion → apply-content → drift.
  Livraison L20 : créer aussi l'entrée de registre C34#1 (fichier 31) — `gen-spec-lot.py` la prend du plan v6 (lot L20 = m119 + m123..m130) ; basculer L18 → publiee (`spec-pub-L18.json`).
- à lancer : L17 (ch.18 NN36–41, après L16), L21 (ch.09 NN47–48, après L14), L22 (ch.07 NN25, ch.12 NN22, ch.18 NN42 : après
  L16/L17) ; devoirs G2 (ch.04 NN29–33), I (ch.09 NN42–46, après L14/L21).
- suites : refaire le devoir 14 de ch.09, corriger les devoirs 11 et 12 de ch.09 ; cours ch.12 (faux : « repère orthonormé exigé
  pour le milieu » ; (O, I, J) jamais nommé ; enseigne vecteurs et translation) ; cours 04/07/08.
- moteur (arena) : correctif en cours `dir=ltr` sur les figures SVG (ancres text-anchor start/end inversées dans une page arabe ; branche t-fig-ltr, worktree wt-arena-fig, verify dans verify-fig.log) ; 3 correctifs d'affichage livrés le 10-02 (#1150 coefficients et lettres primées, #1149 dungeon RTL par la
  langue du contenu le 10-01, #1152 coche ✓ hors isolat).

## SVT 9ᵉ (matière `sciences-vie-terre`)

- Lecture faite : 6 sessions (2020, 2021, 2022, 2024, 2025, 2026) — transcriptions dans `en-cours/lecture-9eme/svt/officiel/`
  (à versionner sous `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/<année>.md` à la
  première livraison SVT), lignes dans `lines/`.
- SVT, lecture versionnée : privé#630 (six transcriptions `2020…2026-generale.md`, `lignes.tsv` 27 lignes, documents C01–C06 `lu/versionnee`, fiche). Outils SVT prêts : `deliver-lot-svt.sh <lot> <chapitre>:<NN,NN> …` (copie, ligne sources[], registre mergee via `MATIERE=sciences-vie-terre gen-spec-lot.py`, gates), `apply-tags.py` (champ `matiere` du pending : `sciences-vie-terre` → sujet `bio`, sans compétence), `add-source-line-svt.py`.
- Lot SVT-L01 (ch.02/05/07 NN7–8, six missions, 36 questions) : auteur FINI (af789b7b2beb04d47), audit opus en cours (ac850d2e96ca57dd5, prompt-audit-SVT-L01.md : l'auditeur peut lire les PDF officiels C03–C06 sous scratchpad/gisement/9eme-sciences-vie-terre/snapshots). À la livraison : `deliver-lot-svt.sh`, puis `apply-tags.py` avec `"matiere":"sciences-vie-terre"` dans le pending, CATALOGUE.md régénéré et committé ; publier avec apply-content `subjects=sciences-vie-terre`. Plan : 27 missions, 5 lots (`gisement/9eme-svt-plan/plan-examens-v1.json`)
  prompts `prompt-svt-L01..L05.md`, affectations `assign-svt-L01..L05.md`.
- Campagne « 9ᵉ au patron » (autre session, privé#569/#620, entrée de synchronisation de l'ETUDE.md §8) : SVT publiée — 14 chapitres
  du programme en 01–14 (les 7 anciens en 15–21, optionnels), famille d'étiquettes **`bio.*` (95 ids)** disponible : les distracteurs
  SVT s'étiquettent avec `bio.*` (nouvel id seulement s'il manque). Le plan SVT rejoué sur ces chapitres est inchangé (27 missions).
  **Arabe 9ᵉ : en réalignement (manuel 101908) — ne rien y placer** tant que la fusion n'est pas signalée dans §8. Français 9ᵉ :
  réaligné sur le manuel 121905, famille `fr.*` (102 ids). Maths : la campagne ne touche que les chapitres 01 et 02.
- Reste à lire : C07–C24 (2019 à 2001, vérifier d'abord « programme en vigueur »), 6 devoirs (D01–D06, lots S1–S5).

## Arabe, français, anglais 9ᵉ

- Arabe : EN RÉALIGNEMENT, ne rien placer. Français et anglais : lecture des sessions non commencée (listes `docs.json`, `machine-list.tsv`, contexte lecteur dans `lecture-9eme/<matière>/`) ; les registres des couples sont sur `main` (échantillons fixés, privé#574).

## 6ᵉ

- Rien de lancé ; sondes dans `gisement/6eme-probe` (scratchpad).

## Limites de session (constat du 2026-10-01)

- La limite est « five_hour », par quota consommé et non par durée : quatre agents (deux auditeurs opus + deux auteurs sonnet)
  l'ont épuisée en ~1 h (09:22 → 10:30 UTC), réouverture à 14:20 UTC. La fenêtre précédente avait tenu 01:10 → 05:20.
- À la coupure, tous les agents meurent avec « You've hit your session limit · resets <heure> » : les reprendre par
  `SendMessage` (leur contexte est conservé) APRÈS l'heure de réouverture, en leur demandant d'écrire leurs résultats
  dans les fichiers de rapport au fil de l'eau (un auditeur coupé avant d'avoir écrit perd tout son travail apparent).
- Garder le contexte principal léger : pas de sondage, un tour par événement.

## Pièges à ne pas oublier
- `apply-tags.py` réécrit les fichiers publiés au format canonique (`json.dumps(indent=2)`) : les vieux fichiers formatés par Prettier (ex. 18/03-revision.json, 20/02-boss.json : objets d'options sur une ligne) en sortent avec 100+ lignes de diff. Après `--write`, lancer `git diff --stat` dans le worktree : pour un fichier au diff gonflé, `git checkout` puis remplacer à la main (script chirurgical) la seule valeur `misconceptionTag`, et vérifier `json.loads(nouveau) == json.loads(version apply-tags)` (fait pour L14).
- Avant une livraison : `git -C /home/user/eng-gisement checkout --detach origin/main && npm ci` (le moteur local était en retard de deux commits, dont le correctif bidi π/° ; fait le 10-10 17h20 UTC, moteur bffcca85).
- Une re-vérification peut encore livrer un correctif de dernière minute (L14 : suppression de deux traits de codage en 37 Q9, « 6 » → « 3√2 » en 41 Q2, retrait de 40 Q6 d et ajout de 18/25 Q1 d dans le pending) : l'appliquer dans l'arbre partagé AVANT `deliver-lot.sh` puis `mk-pending.py` à nouveau.

- Le pre-push husky ne tourne pas dans un worktree sans `.husky/_` : lancer soi-même lint + typecheck + tests avant de pousser.
- Ne jamais committer ni pousser l'arbre partagé `/home/user/yahia-quest-content` (périmé) : lire/copier seulement.
- Aucun `supabase db push/reset`, aucun dispatch de `db-migrate-prod.yml` ni de `release.yml`.
