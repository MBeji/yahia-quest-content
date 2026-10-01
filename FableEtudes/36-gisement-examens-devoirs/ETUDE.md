# Étude 36 — Le gisement : examens nationaux et devoirs en ligne → exercices (fusion des études 12 et 27)

> **Statut** : **en exécution** — ouverte le 2026-09-28 sur arbitrage écrit du propriétaire (§8) :
> l'étude 12 est **dégelée pour son volet ingestion** et fusionnée avec l'étude 27 en **un seul
> pipeline**, exécuté sur toutes les classes et tous les chapitres, **la 9ᵉ d'abord, puis la 6ᵉ**.
> **Priorité** : 36 · **Valeur** : 📚 chaque sujet officiel d'examen national et chaque devoir en
> ligne lu devient des exercices du portail, les premiers **repris fidèlement et cités**, les
> seconds **réécrits en salle blanche**, par une chaîne reprenable d'une session à l'autre,
> mesurée, et sans une ligne copiée d'un tiers · **Complexité** : moyenne (une doctrine, trois
> scripts du moteur, et surtout de l'exécution opérée, couple après couple)
> **Architecte** : session Claude Code, 2026-09-28 · **Exécuteur cible** : opéré (sessions de
> campagne) pour les lots de contenu ; Sonnet ou équivalent pour l'outillage (lot 2)
> **Dépend de** : é12 lot 1 (`content-ingest`, registre `suivi/`, livraison par tranches T-10) ·
> é13 (ScribeKit, livrée) · é27 lots 1-3 (profil `source-web`, quatre tiers, garde anti-verbatim,
> chaîne en salle blanche, pilote maths 9ᵉ) · décision Q-6 du 2026-09-28 (les examens nationaux
> sont du corpus officiel) · **Bloque** : rien
> **Docs normatifs liés** : [`METHODE-GENERATION-CONTENU.md`](../METHODE-GENERATION-CONTENU.md)
> (§ Profils de source, § Le gisement) · `.claude/skills/content-ingest/` (mode gisement et ses
> consignes) · `.claude/skills/campagne/` · moteur : `scripts/content/verbatim-checks.ts`
>
> **Fiche de verticalité** : **Verticale** : V1 « apprendre & maîtriser » (profondeur des
> chapitres existants) · **Maturité visée** : M3 · **Boucles** : elle **referme** le pilote de
> l'é27, dont la chaîne mesurée devient le chemin normal (ses lignes de lecture et sa carte servent
> telles quelles) ; elle **ouvre** un registre par couple, que consomme la session de campagne
> suivante, dès le merge de la tranche précédente · **Apport IA** : retenu, pour lire (vision des
> scans), écrire (`prof-*`) et relire à l'aveugle (`content-audit`), ancré sur des transcriptions
> officielles versionnées et sur des vocabulaires fermés ; tout ce qu'un script peut vérifier l'est
> par un script (gates, contrôle local, placement).
>
> **Ce que deviennent les études 12 et 27.** Le volet ingestion de l'é12 (lots 1-2 : la fiche, le
> skill, le pilote chiffré) vit désormais **ici** ; son canal enseignant in-app (lot 3) reste chez
> elle, gelé derrière sa Q-2. La doctrine de l'é27 (lots 1-2) et son pilote (lot 3) alimentent ce
> pipeline ; ses lots de lien sortant et de partenariat (4-6) restent chez elle, derrière Q-2/Q-3.

---

## 1. Contexte & objectif produit

**Ce que le pilote a mesuré** (é27 lot 3, maths 9ᵉ, 2026-09-28). 33 documents lus (5 sujets
d'examen, 18 devoirs, 10 séries), 166 exercices, **1,52 M de jetons de lecture** (46 000 par
document, 22 minutes à six lecteurs). La carte a trouvé **trois trous, dont deux de programme** :
le manuel enseignait les relations métriques et le centre de gravité, le contenu non. Trois
auteurs ont écrit 36 questions et trois sections de cours ; contrôle local : **0 recouvrement** ;
audit à l'aveugle : **0 clé fausse**. La tranche des chapitres 08 et 09 est en production
(privé#570, publication du 2026-09-28). Deux constats décident de ce pipeline :

- **l'écriture coûte plus que la lecture** : ~600 000 jetons par auteur pour 12 questions, dont
  l'essentiel part au chargement des skills. On optimise donc la taille des lots d'auteur avant
  la lecture ;
- **la règle « combler les trous » laisse le gisement presque intact** : 166 exercices lus pour
  36 questions écrites. Le propriétaire demande le **maximum d'exercices** : chaque archétype
  distinct d'un devoir devient une mission, et chaque exercice d'examen aussi.

**La demande** (propriétaire, 2026-09-28) : « Il faut utiliser l'étude 12 et l'optimiser si
nécessaire. Il faut fusionner étude 12 et 27 et faire un pipeline complet qui va être exécuté sur
tous les chapitres et tous les niveaux, commençant par 9ème année puis 6ème année, pour générer
maximum d'exercices à partir des concours et des devoirs en ligne. »

**Deux régimes, deux sorties** — la règle qui décide de tout se lit ici, une fois :

| source                                         | statut                          | ce qu'on prend                                        | sortie                                                                                  |
| ---------------------------------------------- | ------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **sujet d'examen national** (concours 6ᵉ, concours 9ᵉ, bac) | corpus officiel (Q-6, méthode R-2) | tout : énoncé, données, figure, **cités**            | transcription versionnée (D-2) + **une mission par exercice**, énoncé repris            |
| **devoir, série** d'un site en ligne            | `source-web`, tier **T2′**       | la **carte** : archétype, étapes, piège, étage        | **une mission neuve par archétype distinct**, contexte et nombres inventés (salle blanche) |

**KPI** : missions publiées par couple et par session ; **coût par mission publiée** (jetons) ;
taux de reprise à l'audit ; **0 recouvrement** au contrôle local ; **0 clé fausse** ; publication
le jour du merge (issue `content-drift` close).

**Non-objectifs** : crawler, aspiration de site, snapshot tiers dans git, corrigé d'un tiers
repris, canal enseignant in-app (é12 lot 3), liens sortants (é27 T1), transcription autorisée
d'un tiers (é27 T2).

---

## 2. Le pipeline — neuf étages, un registre par couple

L'unité de campagne est le **couple** classe × matière (`9eme-base` × `math`). Chaque étage a un
seul rôle, une sortie persistée et une preuve. Ce qui n'est pas dans git est perdu avec le
conteneur : **tout ce qui sert à reprendre est versionné**, sauf les snapshots tiers (R-10 de
l'é27), qu'on retélécharge et dont l'empreinte dit si c'est le même document.

| étage | rôle | sortie (persistée) | preuve |
| ----- | ---- | ------------------ | ------ |
| **G0 — Qualifier** | sites des devoirs : fiche de site en 8 champs (réutilisée d'un couple à l'autre) ; archive officielle des examens (Ministère) | `sources-externes/web-<site>/fiche.md` | en-tête complet, robots et CGU lus (R-13) |
| **G1 — Fixer l'échantillon** | **avant toute lecture** : sessions d'examen, devoirs par créneau (D-4), séries | la fiche du couple (§ échantillon), mergée avant lecture | la date du commit précède la lecture |
| **G2 — Lire** | un lecteur par lot de ≤6 documents : texte d'abord, vision sinon (D-8), SHA-256, snapshot hors git, une ligne par exercice | `lignes.tsv` du couple ; pour un examen, **aussi** sa transcription fidèle (D-2) | format fermé des lignes (lot 2) |
| **G3 — Carte & écart** | agréger par chapitre ; croiser avec les questions existantes | fiche du couple (§ carte, § écart) | contrôle local appliqué à la carte |
| **G4 — Planifier** | placer chaque exercice (D-5), dédoublonner, former les lots d'auteur, réserver les numéros de fichiers | `gisement.json` du couple (missions à l'état `planifiee`) | plan rejouable : même entrée, même plan |
| **G5 — Écrire** | auteurs `prof-<matière>-<classe>` en parallèle, **un chapitre = un auteur à la fois** : salle blanche pour un devoir, reprise citée pour un examen | fichiers `content/<matière>/<chapitre>/exercices/NN-*.json` | double résolution, `content:gates -- --tranche` |
| **G6 — Prouver** | contrôle local contre les snapshots (devoirs) ; relecture à l'aveugle de la tranche | fiche du couple (§ mesures) | 0 plage ≥ 8 mots, < 3 données communes, 0 clé fausse |
| **G7 — Livrer** | tranche de ≤4 chapitres d'une matière (T-10), depuis un worktree frais d'`origin/main` ; PR → merge → `apply-content` (`subjects` = la matière) | PR mergée, release journalisée | « Appliquer », « Vérifier en base », « Journaliser » verts ; `content-drift` close |
| **G8 — Mesurer & tenir** | statuts du registre, coûts, journal | `gisement.json`, fiche § mesures, journal de cette étude | la session suivante reprend sans relire |

**La salle blanche tient pour les devoirs, pas pour les examens.** Celui qui lit un devoir
n'écrit pas ; celui qui écrit n'a vu qu'une ligne anonyme (créneau, étage, étapes, compétences,
archétype, piège). Un sujet d'examen, lui, est du corpus officiel : son auteur **le reçoit** et le
reprend, données comprises, en le citant. Les deux consignes d'auteur sont distinctes
(`content-ingest/references/gisement-auteur-devoir.md` et `gisement-auteur-examen.md`).

---

## 3. Architecture (décisions fermées)

- **D-1 — La fusion.** Un seul pipeline, décrit ici et dans la méthode (§ Le gisement), exécuté par
  le skill `content-ingest` (le skill de l'é12) en **mode gisement** — pas de nouveau skill :
  l'orchestration d'ingestion existe, on lui ajoute la chaîne de l'é27. `/campagne` y renvoie
  pour ce mode.
- **D-2 — Sixième profil de source : `examen-national`, et la place de ses transcriptions.**
  Le point laissé ouvert par Q-6 (« où versionner la transcription d'un sujet officiel ») se ferme
  ainsi : `content/programmes-officiels/examens-nationaux/<classe>/<matière>/<session>.md`, une
  session par fichier, en-tête de provenance (`source: officiel`, page du Ministère, URL du
  fichier, session, date de consultation, SHA-256, mode de lecture). Hors de `sources-externes/`,
  donc **hors de la garde anti-verbatim** (elle n'indexe que `sources-externes/` et `_sources/`) :
  la reprise est permise, la garde n'a pas à la signaler. R-3 tient : un item d'un programme
  ancien y est marqué `[hors programme en vigueur]`, il ne s'enseigne pas.
- **D-3 — Le registre du couple.** Sous `programmes-officiels/sources-externes/web-<classe>-<matière>/`,
  à côté de la fiche du couple (le modèle est `web-9eme-base-math`) : `lignes.tsv` (les lignes du
  lecteur, dans nos mots) et `gisement.json` (documents : id, nature, session ou créneau, page,
  fichier, SHA-256, mode de lecture ; missions : exercice(s) source, chapitre, fichier, étage,
  lot d'auteur, tranche, statut `planifiee` → `ecrite` → `auditee` → `mergee` → `publiee`). Le
  dossier est déjà interdit aux auteurs par la consigne de salle blanche ; la fiche y reste sous
  la garde anti-verbatim.
- **D-4 — La saturation plutôt qu'un quota** (optimisation O-1). Les examens se lisent **tous**
  (chaque session est un corpus officiel distinct). Les devoirs se lisent **par vagues de neuf**,
  un par créneau (DC1 … DS3), collège pilote et ordinaire en alternance ; après chaque vague, la
  part des **signatures neuves** (chapitre + compétences + archétype) décide : au-dessous de 30 %,
  on s'arrête ; au plus quatre vagues par couple. Les séries viennent en dernier, une par
  chapitre, si la dernière vague a encore trouvé du neuf. Seuils à calibrer sur les trois
  premiers couples (Q-1).
- **D-5 — L'unité d'écriture** (O-4). Un devoir donne **une mission par signature distincte**
  dans son chapitre : un archétype vu dans six devoirs donne une mission, pas six (sa fréquence
  pèse sur l'étage et l'ordre, pas sur le nombre). Un examen donne **une mission par exercice**.
  Placement : le chapitre le **plus avancé**, dans l'ordre du manifeste de la classe, parmi ceux
  que l'exercice mobilise ; ainsi tout ce qu'il teste est enseigné avant ou dans ce chapitre.
  Lots d'auteur : **5 à 8 missions**, pour amortir le chargement des skills ; un chapitre n'a
  qu'un auteur à la fois, et chaque lot reçoit sa plage de numéros de fichiers.
- **D-6 — L'outillage déterministe passe au moteur** (lot 2). Les trois scripts de session du
  pilote deviennent des commandes testées : `content:gisement:lignes` (format fermé, vocabulaire
  des compétences, étage, **aucun chiffre** dans l'archétype ni le piège : un nombre de la source
  n'y a pas sa place), `content:gisement:plan` (placement, dédoublonnage, lots, plages de
  numéros) et `content:gisement:controle` (contrôle local contre les snapshots : n-grammes de la
  garde, données communes). Avant leur merge, l'orchestrateur applique les mêmes règles à la main.
- **D-7 — Livrer sans déranger** (O-6). Les auteurs écrivent dans l'arbre de travail ; chaque
  tranche se livre depuis un **worktree frais d'`origin/main`** où l'on copie ses fichiers. On ne
  change jamais de branche sous un auteur qui écrit.
- **D-8 — Lire moins cher** (O-2, charte T-1/T-2). Couche texte d'abord (`pdftotext`), vision
  seulement si elle est absente ou cassée (fréquent en arabe), rendu à 150 DPI ; un lecteur par
  lot de ≤6 documents ; pour un examen, la transcription et les lignes sortent **de la même
  lecture** (une page n'est lue qu'une fois).
- **D-9 — L'ordre d'exécution.** Arbitrage du propriétaire : la **9ᵉ**, puis la **6ᵉ**, puis les
  autres classes. Dans une classe, toutes les matières de son examen passent (D-10) ; l'ordre est
  celui de la table du §4 (choix de l'architecte, réversible par le propriétaire).
- **D-10 — Le périmètre d'une classe à examen est celui de son examen.** Arbitrage du
  propriétaire (2026-09-29) : « pour la 9ᵉ année il ne faut pas faire sciences physiques dans le
  pipeline, car la matière n'est pas dans le concours ; SVT est dans le concours national, pas la
  physique ». Le gisement d'une classe à examen national ne traite que les matières de ses
  épreuves : en 9ᵉ, math, SVT (`sciences-vie-terre`), arabe, français et anglais. Les sciences
  physiques (`svt`, l'identifiant historique) en sortent — seule la filière technique a une
  épreuve de physique — et leur registre, fixé avant toute lecture, est retiré. La 6ᵉ suit la
  même règle, sur la liste des épreuves de son archive.

---

## 4. Plan d'exécution en lots

| lot | couple ou contenu | sortie | preuve | dépend de |
| --- | ----------------- | ------ | ------ | --------- |
| 1 | **Doctrine** : cette étude ; méthode (profil `examen-national`, § Le gisement) ; `content-ingest` mode gisement et ses consignes ; renvoi de `/campagne` ; statuts de l'é12 et de l'é27 ; index ; `STATUS.md` du moteur | PR privée + PR moteur | relecture ; Content CI verte | — |
| 2 | **Outillage** (D-6) | `scripts/content/gisement/*` + tests + commandes npm | Vitest ; `npm run verify` | 1 |
| 3 | **9ᵉ math** : les 67 exercices de devoirs lus au pilote, puis les sujets d'examen de toutes les sessions | missions `content/math/**` | G6 par tranche | 1 |
| 4 | ~~9ᵉ sciences physiques (`svt`)~~ — **écarté** (D-10) : pas d'épreuve au concours | — | — | — |
| 5 | 9ᵉ SVT (`sciences-vie-terre`) | idem | idem | 1 |
| 6 | 9ᵉ arabe (`arabic`) | idem | idem | 1 |
| 7 | 9ᵉ français (`french`) | idem | idem | 1 |
| 8 | 9ᵉ anglais (`english`) | idem | idem | 1 |
| 9 | 6ᵉ math (`math-6eme`) | idem | idem | 1 |
| 10 | 6ᵉ arabe (`arabic-6eme`) | idem | idem | 1 |
| 11 | 6ᵉ éveil scientifique (`eveil-scientifique-6eme`) | idem | idem | 1 |
| 12 | 6ᵉ anglais (`english-6eme`) | idem | idem | 1 |
| 13 | 6ᵉ français : **la matière n'existe pas** (Q-2) | LOT A de la méthode d'abord | — | Q-2 |
| 14+ | les autres classes (7ᵉ, 8ᵉ, primaire, lycée, bac compris) | idem | idem | 3-12 |

- [ ] Lot 1 — doctrine
- [ ] Lot 2 — outillage
- [ ] Lot 3 — 9ᵉ math (en cours : devoirs des trois trimestres)
- [ ] Lots 5-8 — 9ᵉ, autres matières du concours (lot 4 écarté, D-10)
- [ ] Lots 9-13 — 6ᵉ
- [ ] Lots 14+ — autres classes

**Stop-points.** Pas d'écriture calibrée sur un devoir sans la garde anti-verbatim (é27 R-8) ni
sans contrôle local ; pas de lecture sans échantillon mergé ; une tranche non publiée n'est pas
finie ; un doute de droits sur un document ⇒ il sort de l'échantillon, sans discussion.

---

## 5. Stratégie de test

- **Lot 2** : Vitest sur chaque commande. Lignes : colonne manquante, étage hors d'échelle,
  compétence hors registre, chiffre dans l'archétype ⇒ rejet. Plan : placement au chapitre le
  plus avancé du manifeste, deux signatures identiques ⇒ une mission, plages de numéros disjointes
  et à la suite de l'existant. Contrôle : deux textes identiques ⇒ plage détectée ; trois nombres
  non triviaux communs ⇒ signalé ; coordonnées d'une figure SVG ⇒ ignorées (le faux positif du
  pilote).
- **Lots de contenu** : `content:gates -- --tranche`, contrôle local, `content-audit` à l'aveugle,
  à **chaque tranche** ; les KPI vont dans la fiche du couple.

---

## 6. Risques & mitigations

- **RISK-1 — Le volume écrase la qualité** (probable / majeur) : le doublon de gabarit est le
  défaut dominant de l'écriture parallèle (méthode B2). → D-5 (une mission par signature), les
  mesures `--tranche`, l'audit à l'aveugle de chaque tranche.
- **RISK-2 — Copie d'un devoir** (possible / critique) → salle blanche, garde de CI (R-8),
  contrôle local contre les snapshots, aucun chiffre dans les lignes (D-6).
- **RISK-3 — Un sujet ancien sort du programme en vigueur** (certain / moyen) → le lecteur marque
  le document et l'item ; l'auteur écarte ou adapte l'étape et le dit (R-3).
- **RISK-4 — Perte du conteneur** (possible / majeur) → registre versionné (D-3), tranches de
  ≤4 chapitres, sauvegarde `wip/` en cas d'arrêt au milieu d'une tranche (T-10).
- **RISK-5 — Coût** (certain / moyen) → saturation (D-4), lots d'auteur de 5-8 missions (D-5),
  texte avant vision (D-8), coût mesuré par lot (T-9).
- **RISK-6 — Un enseignant se reconnaît dans une mission** (possible / majeur) → procédure de
  retrait sous 48 h de l'é27 (RISK-6), traçabilité par la fiche du couple.
- **RISK-7 — Accès aux sites** (possible / opérationnel) → R-13 de l'é27, jamais de
  contournement ; l'archive du Ministère d'abord.

---

## 7. Questions ouvertes (pour l'humain)

- **Q-1 — Seuils de saturation** (30 %, quatre vagues de neuf devoirs). Défaut appliqué d'ici là ;
  à revoir sur les mesures des trois premiers couples.
- **Q-2 — Le français de 6ᵉ.** Le concours de 6ᵉ l'évalue, le portail n'a pas la matière.
  L'ouvrir, c'est d'abord un LOT A (transcription du manuel CNP), puis ce pipeline. Défaut
  proposé : oui, après les autres matières de 6ᵉ.
- **Q-3 — Après la 6ᵉ, quel ordre ?** Défaut proposé : 7ᵉ et 8ᵉ (les devoirs y abondent), puis le
  lycée, bac compris (le bac est un examen national : ses sujets sont du corpus officiel).

---

## 8. Journal d'exécution

- **2026-09-28 — Étude ouverte : l'é12 est dégelée et fusionnée avec l'é27.** L'arbitrage du
  propriétaire est cité au §1 ; il vaut arbitrage écrit au sens de la doctrine verticale (P-7), et
  lève pour ce pipeline le gel de l'é12 (é26 Q-3). État au moment de l'ouverture : la tranche
  08/09 du pilote est publiée (privé#570) ; le chapitre 04 (racine admissible) finit sa reprise
  d'audit ; les devoirs du 1ᵉʳ trimestre sont en écriture (quatre auteurs), ceux des 2ᵉ et
  3ᵉ trimestres planifiés (43 exercices, huit lots d'auteur, placement rejoué à l'identique sur le
  1ᵉʳ trimestre).
- **2026-09-29 — La physique sort du gisement de 9ᵉ (D-10).** Arbitrage du propriétaire : la
  matière n'est pas au concours. Le registre `web-9eme-base-svt` est retiré ; aucun de ses
  documents n'avait été lu. Côté maths, deux tranches sont publiées : le chapitre 04
  (privé#575) et les chapitres 08, 09 et 12 (privé#577). La tranche 20/07 est livrée avec
  cette décision. Les devoirs des 2ᵉ et 3ᵉ trimestres sont en écriture ou en audit, sur les
  chapitres 02, 03, 04, 16, 17 et 18.
- **2026-10-01 — Synchronisation avec la campagne « 9ᵉ au patron » (autre session, arbitrage du
  propriétaire du 2026-09-28 : finir la 9ᵉ avant tout le reste).** Ce que cette campagne a changé
  sous les pieds du gisement, et ce qu'elle attend de lui :
  - **SVT 9ᵉ (`sciences-vie-terre`) — publiée (privé#569).** Les 7 anciens chapitres hors programme
    sont passés en fin de liste (displayOrder **15–21**, optionnels) ; les 14 chapitres du programme
    gardent 01–14. Une **famille d'étiquettes `bio.*` existe désormais (95 ids)** et tous les chapitres
    déclarent leurs `coursePitfalls` ; **`coursePattern: "notion"` est armé**. ⇒ La ligne « Pas de
    famille d'étiquettes SVT : distracteurs muets » de l'état de reprise est **périmée** : les missions
    SVT du gisement se placent dans les chapitres **01–14** et étiquettent leurs distracteurs avec
    `bio.*` (règles R1/R2/R3 ; nouvel id seulement s'il manque, à ajouter au registre).
  - **Français 9ᵉ (`french`) — publié (privé#569).** Réaligné sur le manuel élève **121905** (lu en
    entier) : **15 chapitres + annales** (`10-annales-sujets-types` en displayOrder 16), métalangage du
    manuel (forme passive, élément modificateur / résolution du problème, articulateurs logiques),
    famille **`fr.*` (102 ids)**, patron **armé**. ⇒ Les missions de français suivent ce métalangage et
    ces chapitres ; les notions « Pour aller plus loin » n'ont pas d'item.
  - **Arabe 9ᵉ (`arabic`) — EN RÉALIGNEMENT, ne pas y placer de missions pour l'instant.** Le contenu
    suivait le guide d'avant la réforme de 2006 ; le manuel révisé **101908** est en cours de lecture
    intégrale (LOT A), et le découpage des chapitres va changer (le الشّرط, par exemple, n'a aucun
    chapitre ; l'interrogation est très incomplète). Le lot 6 du gisement attend la fusion de ce
    réalignement, qui sera signalée ici.
  - **Maths 9ᵉ** : la campagne ne touchera que **01-nombres-reels et 02-racines-carrees** (recentrage
    sur leur chapitre officiel, arbitrage du 2026-09-28), après les lots en cours du gisement ; aucun
    lot du gisement n'est sur 01/02.
  - **Moteur** : l'italique `_…_` et les `\*` échappés s'affichent désormais (moteur #1144) — inutile
    de les contourner dans les missions.
