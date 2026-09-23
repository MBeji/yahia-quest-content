# ROADMAP — le reste-à-faire, trié

<!-- roadmap-sync: since-pr=1007 -->

> **Refonte du 2026-09-23** : 531 lignes / 113 Ko → cette version. Motif : **trop de chantiers
> démarrés, pas assez de finis.** Au 2026-09-23, sept études étaient « en exécution » en même
> temps, dont trois dont le travail restant n'était plus que de la mesure ou du rangement, et ce
> fichier annonçait encore comme à faire une campagne livrée cinq jours plus tôt (é35, concours 9ᵉ).
> Chaque ligne ouverte a donc été **triée** : finir, attendre un humain, basculer au contenu, ou
> geler. Il n'y a plus de ligne sans décision. L'ancienne version se lit par
> `git show HEAD~1:FableEtudes/ROADMAP.md` ; ses leçons sont gardées, condensées, au §6.
>
> L'état de référence reste
> [STATUS.md](https://github.com/MBeji/yahia-quest-arena/blob/main/STATUS.md) et l'[index des études](./README.md).
> Le **contenu** se suit avec des commandes, pas ici : `npm run programme:etat` (ce qui manque),
> l'issue `content-drift` (mergé mais pas en prod), `/campagne` (par quoi commencer).

---

## 0. Les quatre règles

1. **Finir avant d'ouvrir.** Au plus **deux** chantiers de code ouverts en même temps. Tant que la
   §2 n'est pas vide, on n'écrit pas de nouvelle étude et on ne commence aucun lot du §5.
   Pour le contenu, la règle est la même : on ne lance pas de campagne sur un nouveau couple
   niveau × matière tant qu'une campagne du §4 reste ouverte.
2. **Une ligne = une session = une PR**, suivie jusqu'au merge réel (et, pour du contenu,
   jusqu'à la prod).
3. **Un statut se vérifie en lançant la commande ou en lisant l'issue.** On ne se fie jamais à
   la ligne qui en parle. Trente secondes avant de prendre une ligne (L-1, L-7).
4. **Une ligne livrée est retirée de ce fichier** dans la PR qui la livre, avec une entrée au
   journal (§7) qui cite la PR. Une ligne cochée n'est jamais gardée : c'est elle qui périme.

## 1. En un coup d'œil

| Rang  | Quoi                                                           | Qui     | Section |
| ----- | -------------------------------------------------------------- | ------- | ------- |
| **1** | é35 lot 7 (mesure) puis lot 8 (bilan), puis clôture de l'étude | session | §2      |
| **2** | é20 : mesure du pilote `short_answer` puis clôture de l'étude  | session | §2      |
| **3** | Clôtures administratives : é34, é09, é11                       | session | §2      |
| ⏰    | Renouveler `GH_AUTOMATION_PAT` **avant le 2026-10-04** (#1078) | Mohamed | §3      |
| ⚖️    | Verdict du pilote IA Q-9 (en retard depuis le 2026-09-15)      | Mohamed | §3      |
| ⚖️    | Trois arbitrages sur l'arabe 1ʳᵉ→8ᵉ (audit privé#522)          | Mohamed | §3      |
| 🔒    | GAP-003 / INPDP, le seul verrou restant du canal enseignant    | Mohamed | §3      |

**Chemin critique vers l'acquisition** (inchangé) : GAP-003 (humain) → é28 D-5 levée →
é08 volet enseignant (§5) → premier canal actif (KPI-1, 🔴 à zéro depuis le 2026-06-13). Il ne
reste **rien de codable** avant GAP-003.

## 2. FINIR — ce qu'une session prend, dans cet ordre

- [ ] **2.1 — é35 lot 7 : la mesure.** Au moteur : `admin_lesson_to_quiz_outcome` (lit
      `learning_pulses`, `attempts`, `content_releases`) et sa carte console, grisée sous
      30 lectures. Additif, un seul merge, pgTAP. Aucune surface élève. Périmètre : §4 de l'étude.
      _État vérifié le 2026-09-23_ : lots 1 à 6 livrés (arena#1050, privé#403, #406, #407, #411,
      #413), extension au concours 9ᵉ (`arabic`, `french`, `sciences-vie-terre`) **terminée
      le 2026-09-18** (privé#420 → #437). C-7 livré (arena#1054).
- [ ] **2.2 — é35 lot 8 : le bilan, puis la clôture.** KPI §1.4 relus, sweep `content-audit`,
      recommandation pour **Q-5** (quelle matière passe ensuite au patron), en-tête → `livrée`,
      dossier → `EtudeRealisé/`, index + `STATUS.md` §4 dans deux PR coordonnées (`etudes:check`).
      Un bilan écrit avant que la mesure ait du trafic dit « trafic insuffisant » et clôt quand
      même : la mesure reste en console, l'étude n'a pas à l'attendre.
      ⚠️ Le drapeau `coursePattern` ne peut pas être posé hors `math`/`math-6eme` tant que les
      distracteurs n'y sont pas tagués (C-5). C'est le sujet d'une campagne de contenu, pas
      un reste de l'étude.
- [ ] **2.3 — é20 : mesurer le pilote `short_answer`, puis clore l'étude.** Le corpus est en prod
      depuis le 2026-09-01 (119 questions libres, `math` 9ᵉ). Relever les signalements
      `content_reports` sur ces questions et le dernier sweep `content-audit`, puis écrire le
      verdict au §8 de l'étude. Ensuite : **lot 4** (campagne Tier B `acceptedAnswers`) sort
      de l'étude et devient une campagne de contenu (§4) ; **lot 6** (boucle du refus contesté,
      optionnel) passe au §5. L'étude est alors `livrée`.
      Dette à consigner en une ligne dans `docs/dette-technique.md` : Tier A produit
      « الفوقها » (préfixe « ال » inconditionnel), ce qui consomme la borne des 24 variantes.
- [ ] **2.4 — Trois clôtures administratives** (une PR privée + une PR moteur pour `STATUS.md` §4) :
      **é34** : lots 1 à 4 livrés (arena#1036, #1040, #1041, #1042, #1043, #1044, #1045) ; le
      lot 5, optionnel, attend une liste de contenu → §5. L'étude est livrée.
      **é09** : lots 1-2 livrés (instrumentation, simulateur) ; lot 3 conditionnel ; ne reste
      que A16, qui est un arbitrage (§3). À clore **après** A16.
      **é11** : déjà rangée dans `EtudeRealisé/`, mais son §4/§8 est vide. À resynchroniser
      **après** le verdict Q-9.

## 3. Ce qui attend Mohamed

Rien ici n'est codable. Chaque ligne dit ce qu'il faut décider et ce que la décision débloque.

| Priorité | Geste / décision                                                                                                                                                                                                                                      | Débloque                                                  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| ⏰ daté  | **Renouveler `GH_AUTOMATION_PAT` avant le 2026-10-04** (#1078, #1002)                                                                                                                                                                                 | toute l'automatisation des deux dépôts                    |
| 1        | **Verdict du pilote IA Q-9.** Mesure relevée chaque lundi dans #1087. Premier relevé : 1 famille, 0,078 $. Le coût n'est pas la question, **le volume** l'est. Options : clore « armé, sans volume » ou prolonger avec une date de fin                | clôture de é11 (§2.4), KPI-3                              |
| 2        | **Arabe 1ʳᵉ→8ᵉ : trois arbitrages** (`content/programmes-officiels/audit/2026-09-22-arabe-base-huit-niveaux.md`) : les ~10 chapitres écrits sur des éditions antérieures à 2006, le canal نصوص servi à 0 %, les مدوّنات القسم à compter comme sources | la campagne arabe de base (§4)                            |
| 3        | **GAP-003 / INPDP** : identité de l'éditeur, consentement parental, durées de conservation, « FR seul ou trilingue » pour les textes juridiques                                                                                                       | é28 D-5, donc é08 enseignant, donc le canal d'acquisition |
| 4        | **A16** : le rachat de série couvre **53 %** des jours manqués (garde-fou G-4 ≤ 20 %, corrigé par arena#947). Desserrer le seuil ou renchérir le shield                                                                                               | `economy:check` vert, clôture de é09                      |
| 5        | **é25 L7** : drill de portabilité, une session avec Mohamed                                                                                                                                                                                           | clôture de é25                                            |
| 6        | **Deux gestes de console** : coller les 3 gabarits d'e-mail FR dans Supabase, et vérifier qu'un `web_vitals` arrive dans PostHog                                                                                                                      | premier contact parent en français ; perf mesurée         |
| 7        | Démarches externes : é23 Q-3 (app child-directed auprès de Google), é24 Q-4 (OTDAV/INNORPI)                                                                                                                                                           | —                                                         |

## 4. Contenu : campagnes ouvertes, à finir avant d'en ouvrir d'autres

Leur état se vérifie avec `programme:etat` et `/campagne`. Cette liste dit seulement **ce qui est
ouvert**, pas où chaque campagne en est.

1. **Arabe de base 1ʳᵉ→8ᵉ**. Fiches R-5 portées (privé#495 → #521). Attend les trois arbitrages du §3.
2. **é23 lot 5 : vidéos `math` 9ᵉ** (registre `videos.json` vide au 2026-09-23). Chaînes AR/TN (R-8).
   Visionnage intégral obligatoire (R-3).
3. **é16 vague A** : les quatre matières lycée restantes.
4. **é20 lot 4** : `acceptedAnswers` Tier B, une matière par PR (après §2.3).

Tout autre couple (nouvelle matière, patron é35 hors 9ᵉ, tagging é30 d'une nouvelle matière,
é19 questions illustrées) attend qu'une de ces quatre campagnes soit close.

## 5. Gelé, bloqué ou différé : on ne lance rien avant que la condition d'entrée soit remplie

| Quoi                                                                                                         | Condition d'entrée                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **é08 volet enseignant** (lots 4·5·6 : classes, liste, devoir)                                               | é28 D-5 levée (GAP-003). Q-4 de l'étude à trancher avant le lot 4   |
| é08 : trois lots parent sans précondition (examen blanc au rapport, digest hebdo opt-in, comparatif seuillé) | §2 vide : ce sont les premiers lots de code à prendre ensuite       |
| é34 lot 5 : l'échelle nommée des 50 niveaux                                                                  | la liste des 50 savants, livrée et relue (contenu)                  |
| é20 lot 6 : boucle du refus contesté (optionnel)                                                             | un signalement réel « réponse juste refusée » au pilote             |
| é09 lot 3 : snapshot `economy_daily_stats`                                                                   | un constat mesuré (RPC > 2 s ou écart de coins gênant)              |
| é30 lots 5-9                                                                                                 | volume réel de `user_misconceptions` (toujours vide en prod)        |
| é19 questions illustrées (validée, jamais démarrée)                                                          | une place libre au §4                                               |
| é24 lot 5 : purge de l'historique git public                                                                 | une fenêtre calme constatée. Lot 6 : reste la tier e2e authentifiée |
| #660 : `typescript` v7                                                                                       | `typescript-eslint` compatible en amont. Ne rien forcer             |
| é27 sources web tierces (brouillon)                                                                          | Q-1…Q-5 arbitrées                                                   |
| é06 PWA offline · é10 anti-fraude · é12 studio d'ingestion                                                   | dégel explicite par Mohamed (é10 : au volume réel)                  |
| é01 paiement en ligne                                                                                        | sortie de la phase gratuite                                         |

## 6. Leçons de méthode (condensées ; le texte complet est dans l'historique git)

- **L-1** : une priorité écrite le jour J et mergée à J+6 est un instantané déjà périmé. Relire
  l'issue ou le code avant de prendre une ligne (C11 et F10, 2026-08-10).
- **L-2** : une garde qui échoue en silence ne se distingue pas d'une garde qui passe. Ce qui
  manque n'est jamais la garde, c'est que sa panne atteigne quelqu'un (douze jours de campagne
  sans filet pédagogique ; `video-health` ; la sonde des manuels qui refermait son issue).
- **L-3** : une fonction SQL vivante se **substitue** à partir de son texte extrait, elle ne se
  retape pas (`get_daily_plan`, arena#818).
- **L-4** : un seuil dupliqué devient faux à plusieurs endroits. Ne jamais recopier une RPC
  existante : cela crée un second juge sur la même question.
- **L-5** : la prod ne juge pas si la base se reconstruit, et un gate vert veut seulement dire
  « rien de ce que je sais lire ne manque ».
- **L-6** : c'est le contenu qui commande le produit. Avant de conclure qu'une ligne de code est
  bloquée, lancer `programme:etat` (dix-huit jours d'arrêt levés par privé#219).
- **L-7** : un chiffre vit à plusieurs endroits d'un même document. Après l'avoir changé,
  `grep` le chiffre avant de committer.
- **L-8** _(2026-09-23)_ : **une horloge sans relève n'est pas une horloge.** Le verdict de Q-9
  était « attendu ≈ 2026-09-15 » ; la date est passée sans que personne ne relève la mesure
  (arena#1086 l'a automatisée depuis). Et une campagne finie le 2026-09-18 était encore donnée
  « à faire » le 2026-09-23. Le remède est la règle 1 du §0 : moins de chantiers ouverts, donc
  moins de lignes à tenir à jour. Une échéance sans relève automatique doit avoir un porteur
  nommé.

## 7. Journal

> Une ligne par événement, qui cite ses PR. Le récit détaillé des entrées antérieures au
> 2026-09-23 est dans `git show HEAD~1:FableEtudes/ROADMAP.md`.

| Date       | Événement                                                                                                                                                                                                                                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-23 | **Refonte « finir avant d'ouvrir »** : 531 → ~170 lignes. Tri de toutes les lignes ouvertes. Statuts corrigés après vérification : é35 campagne 9ᵉ finie (privé#437), é34 lots 1-4 livrés, arena#673/#595/#1092 fermées, verdict Q-9 en retard (mesure dans #1087, arena#1086/#1088). Règle de WIP ajoutée (§0.1), leçon L-8 |
| 2026-09-17 | é35 : regroupement de `07` et `18` (privé#417), glose française R-14 (privé#414), C-7 (arena#1054, privé#419), extension au concours 9ᵉ (privé#420)                                                                                                                                                                          |
| 2026-09-16 | é35 validée (topo : arena#1049, #1051) ; lot 1 (arena#1050), lot 2 (privé#403), lots 3-6 (privé#406, #407, #411, #413). C-6 corrigé (arena#1052)                                                                                                                                                                             |
| 2026-09-14 | é34 écrite, validée (Q-2 contre la recommandation), lots 1 (arena#1036), 2 (arena#1040, #1041), 3 (arena#1042, #1043), 4 (arena#1044, #1045)                                                                                                                                                                                 |
| 2026-09-07 | Le fil CONTENU sort de ce fichier (privé#381) ; 880 → 369 lignes                                                                                                                                                                                                                                                             |
| 2026-09-06 | é21 close (lot 6) ; `math-6eme` tagué de bout en bout (privé#374, #376)                                                                                                                                                                                                                                                      |
| 2026-09-05 | é21 lots 1, 2, 4 (arena#992, privé#356) et 5 (privé#358, #360, #361, #362) ; é26 close (arena#990, privé#354)                                                                                                                                                                                                                |
| 2026-09-03 | A17 livré (arena#958) ; A15 constaté fait                                                                                                                                                                                                                                                                                    |
| 2026-09-02 | `export_user_data` livré (arena#948) : D-5 n'attend plus que GAP-003                                                                                                                                                                                                                                                         |
| 2026-09-01 | é11 : 8 lots livrés (arena#844). Le pilote Q-9 démarre avec les deux clés                                                                                                                                                                                                                                                    |
| 2026-08-30 | é30 : périmètre retenu livré (arena#856 → #860, #910, #911, #912)                                                                                                                                                                                                                                                            |
| 2026-08-24 | Élagage et recadrage : graphe, horloges contre chantiers, chemin critique du goulot                                                                                                                                                                                                                                          |
| 2026-08-23 | é04 finie (arena#818) ; é30 validée                                                                                                                                                                                                                                                                                          |
| 2026-08-22 | é29 livrée (arena#807) ; é11 lot 1 (arena#816) ; C4bis étape 1 (privé#219)                                                                                                                                                                                                                                                   |
| 2026-08-16 | é02 livrée (arena#743, #746)                                                                                                                                                                                                                                                                                                 |
| 2026-08-13 | é28 arbitrée                                                                                                                                                                                                                                                                                                                 |
| 2026-07-20 | Création. Arbitrages A1→A8, doctrine verticale é26, scission du corpus (é24)                                                                                                                                                                                                                                                 |
