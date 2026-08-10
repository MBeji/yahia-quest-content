# Étude 27 — Stratégie de référence : de la profondeur technique à la position de marché

> **Statut** : brouillon — Q-1…Q-5 ouvertes, aucune n'est arbitrable par un exécuteur
> **Priorité** : transverse (gouvernance de position — elle ne construit rien, elle ordonne) ·
> **Valeur** : 🏁 le projet a une avance d'ingénierie réelle et **aucun canal d'acquisition
> actif** ; cette étude nomme la position défendable, mesure l'écart qui l'en sépare, et
> séquence les cinq mouvements qui la transforment en position de marché ·
> **Complexité** : faible (exécution documentaire) — portée stratégique majeure
> **Architecte** : Claude Opus 5, 2026-08-10 · **Exécuteur cible** : Sonnet (ou équiv.) pour les
> lots documentaires ; les arbitrages restent humains
> **Dépend de** : rien (exécutable immédiatement) · **Bloque** : rien mécaniquement — mais son
> Q-2 **amende un arbitrage rendu** (é26 A1-Q2, cible de couverture rentrée), et son Q-4
> déplace é02 hors de la file différée V2
> **Docs normatifs liés** : AGENTS.md, STATUS.md, `FableEtudes/ROADMAP.md`, étude 26 (doctrine
> verticale — cette étude en est le pendant **externe** : é26 regarde le produit, é27 regarde
> le marché), `go-live/05-plan-marketing-commercial.md`, `go-live/91-actions-mohamed.md`

**Fiche de verticalité** (é26 D-2) — **Verticale** : transverse (gouvernance) ·
**Maturité visée** : sans objet (étude documentaire ; les capacités qu'elle mandate visent M3,
l'examen blanc M4 par é26 D-7) · **Boucles** : elle ne referme aucune boucle technique — elle
referme la boucle **produit → marché**, la seule que le portefeuille n'ait jamais ouverte ·
**Apport IA** : aucun runtime propre ; l'IA est retenue comme **argument de position** (le
diagnostic d'erreur, é04/é07/é11), pas comme surface nouvelle.

---

## 1. Contexte & objectif produit

### 1.1 La commande humaine (mandat du 2026-08-10)

Mohamed pose la question en une phrase : **« comment rendre le projet la plate-forme e-learning
de référence en Tunisie ? »**

Ce n'est pas une demande de fonctionnalité. C'est une demande de **position** — donc une étude
qui doit répondre à trois choses qu'aucune étude existante ne traite : quelle référence est
réellement gagnable, quel écart mesuré nous en sépare, et dans quel ordre le combler.

L'étude 26 a répondu à la question **interne** (« comment construire bien ») et l'a bien fait.
Elle a un angle mort assumé — §1.4 : « ce que cette étude n'est PAS » — : elle ne dit rien de
qui utilise le produit. Cette étude-ci est son pendant externe. Elle ne remplace pas é26 ; elle
lui ajoute le seul juge qu'une doctrine de qualité ne contient pas — **quelqu'un d'autre que
nous**.

### 1.2 Le problème mesuré (audit du 2026-08-10, `main` à e8dce7f / arena #716)

**(a) L'avance d'ingénierie est réelle et vérifiée.** SM-2 refermé (é22 lot 2), graphe de
**59 compétences** avec maîtrise EWMA, rappel actif, duels temps réel + ligues, 6 types de
questions natifs, trilingue FR/EN/AR avec RTL, CI à trois étages, migrations auto-appliquées,
prod live sur `www.na9ranal3ab.tn`. Corpus mesuré sur disque ce jour : **89 matières,
659 chapitres, 22 146 questions** (les ~18 700 cités partout datent de la scission é24 —
l'écart est de la production réelle, pas une erreur).

**(b) Le canal d'acquisition n'existe pas.** Dans `go-live/91-actions-mohamed.md`, **D1** (page
Facebook), **D2** (école pilote), **D3** (beta-testeurs) et **B2** (pseudos sociaux) sont tous
les quatre **ouverts**. GA4 et PostHog sont câblés et instrumentent un entonnoir dans lequel
personne n'entre par un canal choisi. Le produit est prêt à recevoir des élèves qu'aucun
mécanisme ne lui envoie. **C'est le goulot du projet, et il n'est traité par aucune étude.**

**(c) Le différenciateur est construit et éteint.** Quatre lots mergés sur `main` — correction
riche A1.2a/A1.2b, geste « m'entraîner », terme misconception de `get_daily_plan` — sont
inertes pour cause de **0 tag de misconception sur 22 146 questions** (re-mesuré ce jour,
inchangé depuis le 2026-07-31). La promesse « la plateforme qui nomme ton erreur et te la fait
travailler » n'existe aujourd'hui pour **aucun élève**. C'est C4bis dans la ROADMAP §5, déjà
identifié comme première ligne — cette étude ne le redécouvre pas, elle en tire la conséquence
de position : **notre argument n°1 n'est pas démontrable en démo.**

**(d) La couverture des classes de concours a un trou nommé.** Mesure par niveau ce jour :

| niveau | matières avec contenu | chapitres | fiches programme transcrites |
| --- | ---: | ---: | --- |
| 6ᵉ **(concours)** | **3** (math, arabe, éveil) | 45 | **6** (arabe ✅ complète ; 5 partielles) |
| 9ᵉ **(concours)** | 6 | 61 | 3 (toutes partielles) |
| 1ère sec | 6 | 56 | 8 (5 complètes/R-7) |
| 2ᵉ sec | 2 (3 ch chacune) | 6 | 1 (partielle) |
| 3ᵉ sec | 1 (anglais) | 6 | 1 (complète) |
| **Bac** | **3** (math 19 ch · anglais 6 · français 3) | 28 | **section `bac-math` uniquement** |

Deux faits qu'il faut lire ensemble et ne pas confondre :

1. **Le français de 6ᵉ n'existe pas** — alors que sa fiche de programme **est transcrite** et
   que, depuis l'amendement R-5 du 2026-07-29, une fiche `partielle` ne bloque plus la matière
   (génération chapitre par chapitre sur les sections transcrites à profondeur de génération).
   Une classe de **concours** à qui il manque une matière de concours. Le blocage n'est pas la
   source : c'est qu'aucune session ne l'a prise.
2. **Le Bac est un problème d'une autre nature.** Le dépôt déclare **six sections de Bac**
   (`manifest/bac-{math,sciences-exp,lettres,eco-gestion,info,techniques}.json`) ; seule
   `bac-math` a des fiches transcrites et un registre de suivi. **Cinq sections sur six n'ont
   aucune fiche.** Le Bac ne se rattrape donc pas par une campagne de génération —
   il demande d'abord un LOT A de transcription. **C'est un chantier de septembre→janvier, pas
   de la rentrée**, et toute planification qui l'oublie se ment.

**(e) Deux verrous légaux, dont un est du code.** GAP-003 (conformité mineurs / INPDP) est une
décision humaine. **GAP-024 est du code et n'existe pas** : `deleteAccount` et
`export_user_data` — zéro occurrence dans `src/`. Servir des données de mineurs sans chemin de
suppression ni portabilité est le seul risque **existentiel** du portefeuille, et c'est la
première question que pose un directeur d'établissement.

### 1.3 Objectif & indicateurs de succès

**Objectif** : que l'avance d'ingénierie cesse d'être invisible — qu'elle devienne une position
tenue sur un segment nommé, mesurée par des utilisateurs réels et non par des gates verts.

KPI mesurables (tous vérifiables sans instrumentation nouvelle) :

- **KPI-1 — un canal actif.** Au moins un canal d'acquisition ouvert et mesuré dans PostHog
  avant le 1ᵉʳ septembre 2026 (aujourd'hui : zéro). Mesure : D1/D2/D3 de `91-actions-mohamed.md`.
- **KPI-2 — la rétention est publiée.** La métrique de retour hebdomadaire (part des élèves
  actifs de la semaine N revenus en N+1) est **calculée et publiée** dans la scorecard. C'est
  le KPI-4 de l'étude 26 — défini le 2026-07-19, **jamais publié depuis**. Sans lui, « référence »
  reste une opinion.
- **KPI-3 — zéro différenciateur éteint.** Aucune capacité revendiquée comme différenciante
  n'est inerte en production. Mesure : C4bis livré et appliqué ⇒ `user_misconceptions` non vide.
- **KPI-4 — les classes de concours sont entières.** 6ᵉ à 4 matières de concours sur 4 ; 9ᵉ tenue
  à la barre é18. Mesure : `npm run programme:etat`.
- **KPI-5 — les verrous légaux sont levés.** GAP-024 livré (code) et GAP-003 tranché (humain).

### 1.4 Ce que cette étude n'est PAS

- **Pas une remise en cause de l'étude 26.** La doctrine verticale est juste et le reste. Cette
  étude en conteste **une seule application** — la cible de couverture contenu (Q-2) — et
  motive pourquoi.
- **Pas un plan marketing.** `go-live/05` existe, ses livrables sont complets (positionnement,
  segments, plan 90 j, kit commercial, KPIs). Le problème de C5 n'est pas qu'il manque un plan :
  c'est qu'il est **terminé à 100 % et exécuté à 0 %**. Cette étude ne le réécrit pas, elle le
  requalifie en chemin critique.
- **Pas une étude d'exécution.** Elle ne spécifie ni table, ni RPC, ni écran. Les capacités
  qu'elle mandate appartiennent à des études propriétaires (é02, é08, é04/é07) ou au moteur
  (GAP-024). Elle fixe leur **rang** et leur **motif**, jamais leur design.
- **Pas un dégel du premium.** La soutenabilité est posée en Q-5 comme une question, pas
  tranchée ici. é01 reste gelée jusqu'à décision humaine explicite.

---

## 2. Le diagnostic de position

### 2.1 La carte du marché (sources et réserves en annexe B)

| acteur | position tenue | ce qu'il détient |
| --- | --- | --- |
| **TakiAcademy** (2013, 150 000+ élèves, 4ᵉ primaire → Bac) | **le cours** | vidéos, profs à notoriété, sessions live, marque que les parents citent spontanément, modèle payant établi |
| **Classera / Tunis Future School** | **l'institution** | accord ministériel, 2,5 M élèves visés, 500 établissements en phase 1 |
| **Thabet Academy** (7ᵉ → Bac) | le cours, second rang | catalogue vidéo aligné programme |
| **Sghartoon** | l'évaluation IA | évaluations gamifiées, présence MENA |
| **Class Quiz** | le primaire ludique | quiz gamifiés 6-12 ans |

### 2.2 La position vacante (P-1 … P-4)

- **P-1 — On ne gagne pas « le cours ».** Treize ans d'avance, des studios, des enseignants
  connus et une marque installée. Toute stratégie qui met Na9ra Nal3ab en concurrence frontale
  avec TakiAcademy sur la vidéo de cours perd, et perd cher (production vidéo = le poste de coût
  que le projet n'a pas).
- **P-2 — On ne gagne pas « l'institution ».** Le canal ministériel est pris. En revanche il est
  pris **au niveau ministère**, pas au niveau **enseignant** — et ce second niveau est vide.
- **P-3 — La position vacante est la pratique.** *Chez Taki on regarde ; ici on s'entraîne.*
  Ce n'est pas un slogan de repositionnement : c'est la description littérale du code déjà
  écrit — révision espacée SM-2, graphe de compétences, maîtrise EWMA, rappel actif, duels,
  6 types de questions. **Aucun acteur tunisien n'a cette boucle.** C'est le seul avantage non
  rattrapable à court terme.
- **P-4 — Un avantage éteint n'est pas un avantage.** P-3 est vrai dans le dépôt et faux dans
  l'application (§1.2c). Tant que C4bis n'a pas tourné, la position revendiquée n'est pas
  démontrable — ni à un parent, ni à un directeur d'école, ni dans une capture d'écran.

### 2.3 Les cinq mouvements (M-1 … M-5, ordre = rendement décroissant)

- **M-1 — Allumer ce qui est construit.** C4bis (tagging misconceptions, pilote `math` 9ᵉ).
  Quatre lots déjà sur `main` s'allument d'un coup. Meilleur ratio valeur/effort du portefeuille,
  et prérequis de P-4. *Propriétaire : ROADMAP §5 C4bis — déjà première ligne, rien à créer.*
- **M-2 — Le concours comme preuve.** Un parent tunisien ne juge pas sur le plaisir de jeu, il
  juge sur *« est-ce que ça prépare au concours »*. Le produit n'a **ni examen blanc, ni annale,
  ni percentile** : é02 est en brouillon et **différée en file V2** derrière une porte
  (« annales transcrites ») qui n'est pas près de s'ouvrir. C'est le plus gros écart produit
  face au marché, et le format le plus partageable qui existe (« j'ai eu 14 au blanc, et toi ? »).
  *Propriétaire : é02, à re-scoper — Q-4.*
- **M-3 — Le canal enseignant, seul CAC ≈ 0 au budget réel.** Le budget d'acquisition arbitré
  est de **1 000–2 000 TND/an** : la publicité n'y construit rien de durable. Un enseignant qui
  donne un chapitre en devoir apporte 30 élèves **et** 30 parents, avec une légitimité que la
  publicité n'achète pas. Or il n'existe **aucun produit enseignant** (L3 est resté en post-MVP
  de C8). Le minimum viable est petit — code de classe, liste d'élèves, taux de réussite par
  chapitre — et la mécanique existe déjà (le rapport parent par code alliance est le même objet).
  *Propriétaire : é08, à re-scoper et sortir de sa porte V4 — Q-3.*
- **M-4 — Lever les deux verrous légaux, parce qu'une école les demandera avant de signer.**
  GAP-024 (code : suppression de compte + export) et GAP-003 (humain : consentement parental,
  registre des traitements). M-3 est **conditionné** par M-4 : démarcher un établissement sans
  chemin de suppression est une faute, pas un raccourci. *Propriétaire : go-live C4/C7 + moteur.*
- **M-5 — Trancher la soutenabilité.** La gratuité est une **phase**, pas un modèle ; une
  référence doit tenir cinq ans. Deux voies compatibles avec P-3 : **B2B établissement**
  (l'école paie, l'élève reste gratuit — cohérent avec M-3) ou **freemium concours** (la
  pratique gratuite, l'examen blanc et le suivi payants). *Propriétaire : é01, gelée — Q-5.*

### 2.4 Hors périmètre (v1)

Production vidéo propre (P-1) · toute démarche ministérielle (P-2) · l'international/MENA
(le trilinguisme le permettra, la position se gagne d'abord chez soi) · la refonte du
positionnement de marque (`go-live/05` S1 est bon et validé, il est **inexécuté**, pas faux).

---

## 3. Décisions fermées (D-1 … D-6)

> Aucun runtime, aucune table, aucun secret. Les objets de cette étude sont des documents
> normatifs, des rangs de file et des critères.

- **D-1 — Où vit la position.** La position P-3 (« la pratique et la maîtrise mesurée ») est
  inscrite comme **décision datée** dans `go-live/05-plan-marketing-commercial.md` (tableau
  Décisions, à la suite de D1-D4), pas dans un document nouveau. _Rejeté_ : un
  `POSITIONNEMENT.md` séparé — C5 est déjà le propriétaire du sujet, un second fichier créerait
  exactement la fragmentation que STATUS.md a dû réparer le 2026-08-02.
- **D-2 — Le go-live gagne une porte, il n'en perd aucune.** Les deux portes existantes (C7)
  sont inchangées. Cette étude ajoute une **condition de position** à la Porte 1 : *au moins un
  canal d'acquisition actif et mesuré* (KPI-1). Une Porte 1 franchie sans utilisateur n'est pas
  un lancement, c'est une mise en ligne. _Rejeté_ : une troisième porte (bureaucratie).
- **D-3 — La file CONTENU se pilote par la valeur de marché, pas par la consolidation.** La
  règle é26 D-6 (« largeur catalogue ≠ largeur capacités », gouvernance propre au contenu) est
  **confirmée** ; ce qui change est le **critère de priorité à l'intérieur** de cette file :
  concours d'abord (classe de concours **entière** avant tout élargissement), puis profondeur.
  La barre é18 reste **non négociable** — on n'ouvre pas plus vite en ouvrant moins bien
  (RISK-4). Sous réserve Q-2.
- **D-4 — Une classe de concours incomplète est un défaut, pas un manque.** Un élève de 6ᵉ qui
  ne trouve pas le français ne conclut pas « le français arrive » : il conclut « ce site ne
  couvre pas mon concours » et ne revient pas. La complétude d'une classe de concours prime donc
  sur l'ouverture d'une classe nouvelle. _Conséquence directe_ : `french-6eme` passe devant
  toute autre ligne de la file contenu après C4bis.
- **D-5 — M-3 est conditionné par M-4.** Aucune démarche d'établissement (D2 de
  `91-actions-mohamed.md`, produit enseignant) n'est engagée avant que GAP-024 soit livré et
  GAP-003 tranché. C'est une **précondition dure**, pas une recommandation.
- **D-6 — Le Bac est un chantier de transcription, pas de génération.** Six sections de Bac sur
  sept n'ont aucune fiche de programme (§1.2d). Toute cible Bac est donc datée
  **septembre→janvier** et passe par un LOT A (METHODE, ScribeKit). Aucune promesse Bac n'est
  portée par le jalon rentrée. _Rejeté_ : une « classe vitrine » Bac sous la barre é18 —
  c'est précisément ce que é26 A1-Q2 interdit, et il a raison sur ce point.

---

## 4. Plan d'exécution en lots

> ⚠️ **Chaque lot vit dans UN dépôt** — aucune PR ne touche les deux (règle é24). Le dépôt est
> indiqué par lot.

| lot | contenu (résumé) | dépôt | fichiers touchés | tests exigés | dépend de |
| --- | --- | --- | --- | --- | --- |
| 1 | **La position + la fenêtre rentrée** : décision D-1 inscrite dans C5 ; D-2 (condition de position sur la Porte 1) dans le master plan ; D1/D2/D3 requalifiés « chemin critique rentrée » dans les actions Mohamed, avec la précondition D-5 écrite sur D2 | privé | `go-live/05-plan-marketing-commercial.md`, `go-live/00-MASTER-PLAN.md`, `go-live/91-actions-mohamed.md` | liens/références valides ; cohérence avec C7 (portes inchangées) | **rien** — arbitrage-indépendant |
| 2 | **Le re-séquencement des files** : ROADMAP §5 repriorisée (C4bis → `french-6eme` → reste) ; é02 sortie de la file différée §6 ; é08 re-scopée et sortie de sa porte V4 ; index `FableEtudes/README.md` resynchronisé | privé | `FableEtudes/ROADMAP.md`, `FableEtudes/README.md`, en-têtes `02-*/ETUDE.md` et `08-*/ETUDE.md` | cohérence index ↔ en-têtes ; `check-roadmap-sync` vert | Q-2, Q-3, Q-4 |
| 3 | **La scorecard de position** : STATUS.md gagne un bloc court « position » (les 5 KPI de §1.3, datés) — pas un fichier de plus (règle du topo, 2026-08-02) | **public** | `STATUS.md` | `npm run verify` vert | lot 1 |

- [ ] Lot 1 — la position + la fenêtre rentrée (privé, exécutable immédiatement)
- [ ] Lot 2 — le re-séquencement des files (privé, après Q-2/Q-3/Q-4)
- [ ] Lot 3 — la scorecard de position (public)

**Stop-points.** Le lot 1 **ne touche à aucune file** et ne préjuge d'aucun arbitrage : il
inscrit la position et requalifie des actions déjà écrites. Le lot 2 ne déplace **que** ce que
Q-2/Q-3/Q-4 ont tranché, et ne modifie **pas** le corps des études é02/é08 (en-tête et rang
seulement — leur re-scopage est un travail d'architecte, hors lots). Le lot 3 n'ajoute **aucune
colonne** au tableau des features (é26 D-3 y pose déjà une colonne « M » ; deux grilles dans un
même tableau le rendraient illisible).

**Hors lots** (travail d'architecte, post-arbitrage) : le re-scopage de é02 « examen blanc »
sans wording premium et sans dépendance aux annales ; le re-scopage de é08 en volet enseignant
(code de classe, liste, taux de réussite) ; la fiche LOT A des sections de Bac non transcrites.

---

## 5. Stratégie de test

Étude documentaire — aucun code produit. Par lot : les références croisées existent et pointent
juste (chaque doc cité, chaque GAP, chaque étude au bon statut) ; le lot 3 exige `npm run verify`
vert côté moteur (preuve d'impact nul sur le build). **Le vrai test est ailleurs** et c'est
assumé : une stratégie ne se valide pas par un gate mais par KPI-1 et KPI-2 — un canal actif et
une courbe de retour publiée. Tant que KPI-2 n'est pas publié, cette étude reste une hypothèse
argumentée, et son §1.3 doit être relu à la première mesure réelle.

---

## 6. Risques & mitigations

- **RISK-1 — L'étude devient un document qui ne change rien.** Probable / impact fort. C'est
  exactement l'histoire de C5 : livrables 100 %, exécution 0 %. _Mitigation_ : le lot 1 est
  **arbitrage-indépendant** et modifie les fichiers d'action, pas seulement les fichiers de
  pensée ; D-2 attache la position à une porte qui, elle, bloque.
- **RISK-2 — Le re-séquencement contenu cannibalise la file V1.** Moyen / moyen. _Mitigation_ :
  les files restent parallèles (ROADMAP §0.2) ; l'arbitrage porte sur le **budget de sessions**,
  posé explicitement en Q-2 — pas laissé au hasard des sessions.
- **RISK-3 — Démarchage d'école sans conformité.** Faible probabilité / **impact existentiel**.
  _Mitigation_ : D-5, précondition dure, écrite sur l'action D2 elle-même par le lot 1.
- **RISK-4 — On ouvre large et mal.** Moyen / fort — l'inverse exact de l'effet recherché : une
  matière bâclée sur une classe de concours détruit la confiance qu'on cherchait à gagner.
  _Mitigation_ : la barre é18 reste non négociable (D-3) ; la largeur se gagne **par matière
  entière**, jamais par échantillon (D-6 rejette la classe vitrine).
- **RISK-5 — La fenêtre rentrée est manquée.** **Élevé** (J-22) / fort — la fenêtre suivante est
  janvier-mars (pic de révisions). _Mitigation_ : le lot 1 est exécutable aujourd'hui, et §7 du
  jalon distingue ce qui tient en 22 jours de ce qui n'y tient pas. **Une cible qui ne tient pas
  dans la fenêtre doit être datée de janvier, pas espérée en septembre.**
- **RISK-6 — La position P-3 est juste et invérifiable.** Moyen / moyen : « personne d'autre n'a
  cette boucle » repose sur des sources publiques, pas sur un audit des concurrents.
  _Mitigation_ : annexe B déclare ses réserves ; la position ne dépend pas de l'exclusivité mais
  de **notre** capacité à la démontrer (P-4, KPI-3).

---

## 7. Questions ouvertes (pour l'humain)

> Aucune n'est arbitrable par un exécuteur. L'étude passe `validée` quand cette section est
> arbitrée. **Seul Q-1 conditionne le lot 1** — et il ne le bloque pas : le lot 1 est écrit pour
> être exécutable même si Q-2…Q-5 restent ouvertes.

- **Q-1 — La position revendiquée.** Valider P-3 — « la plateforme où l'élève tunisien
  s'entraîne et mesure sa maîtrise » — comme position de référence, et acter **le renoncement
  explicite** à concurrencer TakiAcademy sur le cours vidéo (P-1). _Recommandation : oui. C'est
  la seule position que le code déjà écrit permet de tenir, et le renoncement à P-1 est ce qui
  la rend finançable._

- **Q-2 — Amender la cible de couverture rentrée (é26 A1-Q2).** L'arbitrage du 2026-07-20 fixe
  « statu quo consolidé à la barre é18, aucune classe vitrine ». Il produit une rentrée où la
  **6ᵉ, classe de concours, reste amputée du français** alors que sa fiche est transcrite.
  Proposition : garder la barre é18 et le refus de la classe vitrine (tous deux justes), mais
  remplacer le critère de priorité « consolider l'existant » par **« classe de concours entière
  d'abord »** (D-3/D-4). Second volet, à trancher explicitement : **quelle part du budget de
  sessions** va à la file contenu face à la file V1 d'ici au 1ᵉʳ septembre.
  _Recommandation : amender sur le critère ; sur le budget, majorité à la file contenu jusqu'au
  1ᵉʳ septembre (V1 n'a plus de ligne prenable avant C4bis, ROADMAP §0.4 le constate déjà)._

- **Q-3 — Le canal enseignant.** Ouvrir le volet enseignant en re-scopant **é08** (qui
  s'intitule déjà « Analytics parents & enseignants ») et en la sortant de sa porte V4, ou
  ouvrir une étude dédiée é28 ? _Recommandation : re-scoper é08 — le sujet est le sien, une
  étude de plus disperserait un portefeuille que é26 KPI-3 cherche à resserrer. Sous réserve
  D-5 (rien ne s'engage avant GAP-024/GAP-003)._

- **Q-4 — L'examen blanc maintenant ou après les annales ?** é02 est différée derrière
  « annales transcrites ». Or un examen blanc **v1** n'a pas besoin d'annales : un assemblage
  chronométré du corpus existant + un rang relatif suffit à créer la preuve et le partage ; les
  annales l'enrichissent ensuite. Sortir é02 de la file V2 et la re-scoper maintenant ?
  _Recommandation : oui, avec un v1 sans annales explicitement borné. C'est M-2, le plus gros
  écart produit face au marché._

- **Q-5 — La soutenabilité.** Trois voies : **(a)** B2B établissement (l'école paie, l'élève
  reste gratuit) · **(b)** freemium concours (pratique gratuite, examen blanc + suivi payants) ·
  **(c)** gratuité prolongée financée hors produit. _Recommandation : (a)_ — cohérente avec M-3,
  elle ne remet pas la gratuité élève en cause (donc ne réveille aucune surface « premium »
  interdite en phase gratuite) et transforme le canal d'acquisition en canal de revenu.
  ⚠️ Aucune des trois ne se met en œuvre sans dégel de é01, qui reste une décision humaine
  distincte de celle-ci.

---

## 8. Journal d'exécution

| date | lot | PR | écarts acceptés / dettes notées |
| --- | --- | --- | --- |
| 2026-08-10 | — | (cette PR) | Étude créée. Statut `brouillon` : Q-1…Q-5 ouvertes. Aucun lot exécuté — le lot 1 est exécutable dès Q-1 arbitrée. |

---

## Annexe A — Mesure de couverture du corpus (2026-08-10, `main` = e8dce7f)

Comptage direct sur disque (chapitre = dossier avec `chapter.json` ; question = entrée
`questions[]` de tout fichier de quiz ou d'exercice) : **89 matières · 659 chapitres ·
22 146 questions**.

| niveau / thème | matières | chapitres | questions |
| --- | ---: | ---: | ---: |
| 1ère base | 4 | 34 | 1 136 |
| 2ᵉ base | 4 | 35 | 1 189 |
| 3ᵉ base | 5 | 41 | 1 315 |
| 4ᵉ base | 5 | 55 | 1 853 |
| 5ᵉ base | 5 | 50 | 1 654 |
| **6ᵉ base (concours)** | **3** | 45 | 1 588 |
| 7ᵉ base | 6 | 54 | 2 214 |
| 8ᵉ base | 6 | 53 | 2 173 |
| **9ᵉ base (concours)** | 6 | 61 | 2 128 |
| 1ère sec | 6 | 56 | 1 072 |
| 2ᵉ sec (lettres) | 1 | 3 | 69 |
| **Bac math** | 1 | 19 | 992 |
| hors niveau (`french-bac`, `english-bac`, `english-3eme-sec`, `math-2eme-sec-sciences-info`) | 4 | 18 | 414 |
| thème anglais (A1→C2) | 7 | 48 | 1 644 |
| thème français (A1→C2) | 8 | 57 | 1 922 |
| thème culture générale | 15 | 15 | 399 |
| thème muscle-cerveau | 3 | 15 | 384 |

**Fiches de programme transcrites** (`programmes-officiels/_INDEX.md`) pour les niveaux
sensibles — statut `complète`/`validée R-7` = génération ouverte ; `partielle` = génération
**par chapitre** depuis l'amendement R-5 du 2026-07-29 :

- **6ᵉ** : arabe ✅ complète · anglais, éveil, **français**, islamique, maths 🚧 partielles.
  → 6 fiches, **3 matières générées**. Le français a une fiche et zéro contenu.
- **9ᵉ** : anglais, arabe, français 🚧 partielles (les 6 matières ont du contenu).
- **1ère sec** : anglais/chimie/français/svt ✅ R-7, maths/sciences-physiques ✅ complètes,
  arabe + histoire-géo 🚧 partielles.
- **Bac** : `bac-math` seulement — mathématiques ✅ R-7, français ✅ complète, anglais et
  philosophie 🚧 partielles. Le dépôt déclare six sections (`manifest/bac-*.json`) : **cinq
  n'ont aucune fiche** et aucun registre `suivi/`.

Écarts avec les chiffres circulant dans les docs : « ~18 700 questions / 566 chapitres » date de
la scission é24 (2026-07-20) ; la production de trois semaines explique l'écart. `CATALOGUE.md`
(59 matières / 393 chapitres) est **périmé** — régénérer avec `npm run content:catalogue`.

---

## Annexe B — Carte concurrentielle : sources et réserves

**Sources consultées le 2026-08-10** (recherche web, pas d'audit produit) :

- TakiAcademy — [DisrupTunisia](https://www.disruptunisia.com/startup-tunisie/taki-academy-13264),
  [Google Play](https://play.google.com/store/apps/details?id=com.softylines.takiacademy) :
  fondée en 2013, 4ᵉ primaire → Bac toutes sections, **150 000+ élèves**, modèle payant.
- Thabet Academy — [thabetacademy.com](https://thabetacademy.com/) : 7ᵉ → Bac, catalogue en ligne.
- Classera / Tunis Future School —
  [Global Partnership for Education](https://www.globalpartnership.org/blog/tunisia-class-quiz-platform-offers-gamified-educational-content) :
  partenariat ministère, 2,5 M élèves visés / 500 établissements en phase 1.
- Sghartoon — [Nucamp](https://www.nucamp.co/blog/top-10-tech-startups-hiring-junior-developers-in-tunisia-in-2026) :
  évaluations gamifiées pilotées par IA, portée MENA.
- Marché — [IMARC, Africa EdTech](https://www.imarcgroup.com/africa-edtech-market) : la Tunisie
  pèse 8,6 % du marché e-learning nord-africain, taux d'alphabétisation le plus élevé de la région.

**Réserves, à lire avant de citer ces chiffres.**

1. Les volumes (150 000 élèves, 2,5 M visés) sont **déclaratifs** — communication d'entreprise
   ou de partenariat, non audités. Ils donnent un ordre de grandeur, pas une mesure.
2. Aucun des cinq produits n'a été **essayé**. L'affirmation « aucun n'a la boucle de maîtrise »
   (P-3) repose sur leur communication publique, où une telle boucle serait mise en avant si
   elle existait — c'est un indice fort, pas une preuve. RISK-6 en tire la conséquence.
3. La part de marché tunisienne est un chiffre **de marché**, pas de segment scolaire.
4. Ces sources ont été lues en août 2026 ; toute réutilisation ultérieure doit les resonder —
   la règle « sonder, pas déduire » (STATUS.md §2, 2026-07-27) vaut ici comme pour le DNS.
