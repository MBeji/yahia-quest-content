# MÉTHODE — Génération de contenu : la référence (source → fiche → contenu → prod)

> **LA méthode.** Toute production de contenu pédagogique à partir d'une source — corpus CNP,
> manuel du secondaire, PDF d'enseignant, polycopié, annales papier — suit ce document, de la
> transcription à la mise en prod, quel que soit l'exécutant : session Claude Code interne (le
> skill `content-ingest` l'applique nativement), agent IA d'un contributeur externe, campagne
> opérée. Elle est **générique** (quatre profils de source, § Profils), **résumable** (elle
> reprend exactement où la work-list en est) et **budgétée** (charte tokens T-1…T-10 : le coût
> par chapitre publié est un KPI mesuré, pas un hasard — et rien ne reste longtemps non poussé).
>
> Ce document **remplace** `PROMPT-TRANSCRIPTION-CNP.md` (consolidation du 2026-07-17) et porte
> le processus des études [12 — Studio d'ingestion](./12-studio-ingestion/ETUDE.md) (le canal)
> et [13 — Moteur de transcription ScribeKit](./EtudeRealisé/13-moteur-transcription/ETUDE.md) (le moteur,
> **livrée**).
>
> **Périmètre d'autorité.** Cette méthode est la référence du **processus** : la boucle, les
> lots, les gates, l'économie de tokens. Les règles d'**authoring** (schéma, barre de qualité,
> récompenses, notation, sélection des skills) restent chez les skills — carte canonique :
> `.claude/skills/content-engine/references/generation-pipeline.md`, consommée par le LOT B.
> Hiérarchie en cas de désaccord : **AGENTS.md (dépôt moteur) → skills & docs normatifs →
> cette méthode**.
>
> **Pour qui ?** Un agent IA avec vision + accès fichiers + git (Claude Code ou équivalent),
> piloté par un contributeur qui peut ne rien connaître du projet : copier ce document **en
> entier**, INPUT rempli, dans l'agent — et laisser la campagne se dérouler. Un accès
> **collaborateur (write)** au dépôt **privé** `MBeji/yahia-quest-content` est requis pour
> pousser (le demander à Mohamed) ; le dépôt public `MBeji/yahia-quest-arena` se clone en
> lecture seule, on n'y pousse rien pendant une campagne.
>
> ⚠️ **Deux dépôts depuis l'étude 24 (2026-07-20)** — à intégrer avant la première commande :
>
> - **`yahia-quest-content` (privé) = le corpus.** Tout ce que cette méthode écrit vit ici :
>   fiches `programmes-officiels/`, registre `suivi/`, `content/`, les 41 skills pédagogiques,
>   cette méthode. **Toutes les branches et toutes les PR de la campagne sont ici.**
> - **`yahia-quest-arena` (public) = le moteur.** Aucun corpus dedans : les scripts
>   (`npm run content:*`, `programme:*`), le schéma Zod, le compilateur SQL, `docs/`, AGENTS.md.
>   **Toutes les commandes `npm` de cette méthode s'exécutent depuis ce clone-là** (le corpus y
>   est branché par lien — § Phase 0.1) : le dépôt privé n'a pas de `package.json`.
> - **Le contenu ne voyage plus en migrations.** Il se compile en `sql/content/<subject>.sql`
>   et s'applique par le workflow `apply-content.yml` du dépôt privé (§ B3). Un agent qui
>   commite une migration `supabase/migrations/*_generated_*_content.sql` s'est trompé de
>   décennie — et de dépôt.
>
> Panorama complet de la scission :
> [`docs/content-generation-pipeline.md`](https://github.com/MBeji/yahia-quest-arena/blob/main/docs/content-generation-pipeline.md)
> (moteur) et [`24-protection-ip-contenu/ETUDE.md`](./24-protection-ip-contenu/ETUDE.md).

---

## INPUT (l'unique chose à renseigner)

```
PORTEE     : tout               # défaut — tous les couples manquants ; l'ORDRE de traitement
                                # reste l'arbitrage humain (§ Phase 0.4). Restreindre :
                                # "1ere-sec" (une classe/section),
                                # "lycee" (le cycle), "9eme-base / math" (un couple).
PROFIL     : auto               # auto (défaut) = déduit du niveau et des sources ; sinon forcer :
                                # ecole-cnp | ecole-secondaire | document-libre | sans-source
FICHIERS   : <chemins locaux>   # optionnel — PDF déjà en local (guide et/ou manuel élève, ou le
                                # document libre), séparés par des espaces. Vide = téléchargement
                                # depuis le site du CNP, couple par couple.
GENERATION : oui                # oui (défaut) = LOT B (contenu) après chaque fiche mergée ;
                                # non = s'arrêter aux fiches (couche de persistance seule).
PSEUDO     : <pseudo GitHub>    # traçabilité (_INDEX.md + commits).
BUDGET     : <optionnel>        # plafond de la session (tokens ou temps) ; la campagne s'arrête
                                # proprement en fin de lot à l'approche du plafond (T-9).
```

> 🚀 **Sous Claude Code, tu n'as pas à remplir ce bloc à la main : `/campagne`** (skill
> `.claude/skills/campagne/`) établit l'état des lieux, **te demande** quel couple lancer, puis
> déroule ce document pour toi — en appelant les bons skills et en passant les gates. Il ne
> choisit jamais le couple : la priorité reste ton arbitrage (§ Phase 0.4). Le reste de ce
> document est ce qu'il applique, et ce qu'un autre agent applique à la main.

## La boucle (vue d'ensemble)

```
PHASE 0 (une fois par campagne) : setup 2 dépôts + cadrage + file de travail (priorité)
pour chaque UNITÉ de la file (couple niveau × matière, ou document libre) :
  LOT A — LA FICHE   : A1 existant → A2 sources → A3 transcription (ScribeKit + vision)
                       → A4 profondeur de génération → A5 audits (QA, R-7, _INDEX)
                       → A6 push → 1 PR → Content CI verte → merge confirmé
  si GENERATION = oui :
  LOT B — LE CONTENU : B1 brief + skills → puis PAR TRANCHE de ≤4 chapitres complets :
                       B2 génération (commit local par chapitre) → B3 gates + push
                       → 1 PR → merge → apply-content dispatché + prod vérifiée
                       → issue `content-drift` close (sinon la prod est en retard)
                       → tranche suivante, jusqu'à la matière complète
  contexte frais → on re-présente l'état et on DEMANDE l'unité suivante (§ Phase 0.4)
fin : PORTEE épuisée, ou arrêt propre (BUDGET) → rapport de campagne
```

Règles de boucle (non négociables) :

- **Une PR = UNE matière, jamais deux** (ni push groupé « 10 fiches d'un coup » — c'est le
  signe qu'on va trop vite, R-6). Le LOT A tient en une PR ; le LOT B se livre en **plusieurs
  PRs par tranches de chapitres** (T-10, B2/B3) — plusieurs PRs pour une matière, jamais
  plusieurs matières dans une PR.
- **Un lot = un contexte frais** : si le harnais le permet (sous-agents/Task), déléguer chaque
  lot à un sous-agent au contexte vierge et garder le rôle d'orchestrateur mince ; sinon,
  traiter strictement en séquence (T-4).
- **Resynchroniser à chaque lot** : branche fraîche depuis `origin/main` fetchée (commandes
  exactes en A1 / B1), puis relire **depuis main** la ligne `_INDEX.md` du couple — un autre
  contributeur a pu avancer pendant le lot précédent.
- **Ouverture en production dès le premier lot** (règle de mise en prod, révisée 2026-07-19) : on
  **n'attend plus la matière complète** pour rendre la classe visible aux utilisateurs — dès que le
  **premier lot de chapitres complet** (première tranche : cours + résumé + quiz + d1 + d2 par
  chapitre) est mergé, on ouvre la classe/section en production ; les chapitres suivants, d3/d4 et
  annales s'ajoutent en continu sans bloquer. Détail et bascule `coming_soon → available` : **R-8**
  de [`FableEtudes/16-ouverture-lycee/ETUDE.md`](./16-ouverture-lycee/ETUDE.md). Applicable à toute
  session de génération, en cours ou future. ⚠️ **La bascule elle-même n'est pas un geste de
  campagne** : c'est une **migration `open_*` du dépôt moteur** (une par section) accompagnée de son
  test pgTAP — donc une **PR distincte sur le dépôt public**, jamais un fichier de la PR de campagne
  (§ B3). Une tranche mergée et appliquée dont le parcours reste `coming_soon` est **invisible aux
  élèves** et aucun gate ne le dit : si la session ne porte pas cette PR moteur, elle inscrit
  l'ouverture au **rapport de campagne** comme reste à faire, nommément.
- **Attendre le merge réel** d'un lot avant d'entamer le suivant (le LOT B dépend de la fiche
  mergée ; deux PR simultanées sur le registre `suivi/` se marchent dessus). ⚠️ Le dépôt de
  contenu a sa **chaîne de merge** (`.github/workflows/automerge.yml`, depuis le 2026-07-26) :
  une PR dont **tous** les checks sont verts est mergée en squash toute seule, sans que
  personne ne la lise. Ne pousser qu'un lot fini. S'y soustraire — comme sur le moteur — par
  une PR **draft**, une branche préfixée `wip/`/`draft/`/`rescue/`, ou le label `no-automerge`.
  Nuance qui compte : faute de rulesets sur un dépôt privé Free, **aucun check n'est
  _requis_** — le workflow automatise le bon geste, il n'interdit pas le mauvais. La session
  qui pousse reste donc de garde jusqu'au **merge réel** (§ A6).

## Le socle R (hérité du skill `content-ingest` — condensé, non négociable)

- **R-1 — Rien ne contourne le pipeline.** Sortie = TOUJOURS des fichiers versionnés sur une
  branche + gates + revue humaine. Aucune écriture DB directe, aucun skip d'audit.
- **R-2 — Provenance & droits.** Le corpus officiel (CNP / manuels scolaires) est la source
  prévue ; tout autre document porte auteur / origine / autorisation, sinon **refus**. Doute ⇒
  STOP. Pas de verbatim d'œuvres périphériques sous droits (chansons, textes littéraires
  longs) : résumer + citer la référence. **Une source du web se qualifie en plus par son
  _tier_** (§ Profils → `source-web`) : ce qu'on prend à un lien décide de tout, et un seul des
  quatre tiers exige une autorisation.
- **R-3 — Programme d'abord.** Pour une matière scolaire, confronter la fiche à la
  transcription CNP du couple si elle existe ; divergence de scope ⇒ le **programme officiel
  gagne**, écart signalé.
- **R-4 — Vérifier l'existant AVANT, dans le REGISTRE.** L'état de la transcription vit dans le
  **registre machine-vérifiable** `programmes-officiels/suivi/` (`corpus-cnp.json` +
  `affectations.json` + `<grade>.json`), validé en CI par `npm run programme:check` —
  `programme/_INDEX.md` n'est qu'une **vue générée** (⛔ ne jamais l'éditer à la main). Une
  entrée `complete`/`validee-r7`/`promue` = **déjà fait** ; `partielle` = **compléter** (les
  plages de pages manquantes sont listées), jamais refaire en parallèle ; **`en-cours` = couple
  réservé** par une autre session — on ne le lance pas et on ne touche pas son entrée (c'est le
  seul statut qui peut précéder la fiche sur disque). Poser `en-cours` est le geste d'une session
  qui réserve un couple dont la fiche n'existe pas encore ; **aucune session ne laisse un
  `en-cours` derrière elle** : au dernier push, l'entrée repasse à `partielle` (palier honnête,
  T-10) ou `complete`, sinon le couple reste fermé aux autres. Un PDF ne peut être
  revendiqué que par UNE fiche — le doublon est une **erreur CI**, plus un risque.
- **R-5 — Profondeur de génération, jamais un résumé.** Chaque activité/exercice décrit
  individuellement, encadrés officiels verbatim, vocabulaire officiel, bornes ✅/⛔. Modèle de
  référence : `programme/1ere-sec/mathematiques.md`. Une « first-pass » s'étiquette comme telle
  et ne se génère pas.
  **La barre se lit au CHAPITRE, pas à la fiche entière** (décision du 2026-07-29). Ce qu'une
  génération consomme, c'est la **section** de son chapitre : une fiche trouée peut donc nourrir
  les chapitres qu'elle a réellement transcrits en profondeur, et eux seuls. Le mécanisme est
  déclaratif et vérifié — l'entrée de registre liste ces chapitres dans `chapitresGeneration`,
  `programme:check` refuse tout slug absent du chapitrage du manifeste, sans `sujets` déclarés,
  ou posé sur une fiche `en-cours`, et `programme:etat` prescrit alors un **LOT B2 restreint**
  (l'intersection « ce que la fiche autorise ∩ ce qui manque au contenu »), non bloquant.
  Ce qui n'a pas changé : le reste de la fiche exige toujours le LOT A, et une section mince ou
  non lue ne se génère toujours pas. La levée **ouvre une classe** — elle n'achève pas une
  matière. Motif : sur 2ème sec sciences, 12 chapitres sur 19 étaient transcrits en profondeur
  et les 19 restaient bloqués, gardant la classe fermée sur de la transcription déjà payée.
- **R-6 — Une session = une matière, lecture intégrale.** Jamais de plafond arbitraire de
  lecture (l'incident du 2026-07-10 : lectures tronquées à 70 k ⇒ fiches truffées
  d'inventions). Partiel honnêtement étiqueté > complet bâclé.
- **R-7 — Vérification indépendante avant promotion.** Un second agent re-vérifie la fiche
  **contre la source** (jamais contre la fiche) — protocole de sondage dirigé en A5.2.
- **Fidélité ≠ génération.** LOT A : on transcrit ce qui est imprimé, rien d'autre. LOT B : on
  génère **avec les skills du dépôt**, jamais sa propre recette.

## La charte tokens (T-1…T-10) — l'économie de la méthode

Le coût d'une campagne se joue sur une poignée de comportements. Chaque règle T ci-dessous est
aussi contraignante que les règles R : un agent qui les viole gaspille le budget qui aurait
publié le chapitre suivant.

- **T-1 — Le déterministe est gratuit : ne le refais jamais au LLM.** ScribeKit extrait les
  couches-texte, échafaude, valide (`qa`), trace (`status`/ledger) ; les scripts du **moteur**
  valident et compilent le contenu. Re-lire en vision un PDF à couche-texte saine, re-vérifier
  à l'œil ce que `scribekit qa`/`content:qa` vérifie, ou écrire du SQL à la main = brûler du
  budget pour rien.
- **T-2 — Une page source n'est lue qu'une fois.** Transcrire **par tranches de 10–20 pages** :
  lire la tranche → écrire immédiatement sa transcription **au format final** (le gabarit) —
  jamais de notes intermédiaires jetables, jamais « tout lire puis rédiger » (c'est la double
  lecture assurée, et la troncature de l'incident 2026-07-10). DPI utile : 150 par défaut, 300
  seulement pour petits caractères / figures denses.
- **T-3 — La fiche est le capital.** Tout le coût vision est capitalisé dans la fiche ; après
  son merge, les PDF ne sont **plus jamais rouverts** — génération, corrections et audits de
  contenu se font depuis la fiche. (Seule re-lecture de source légitime : le R-7 du LOT A.)
- **T-4 — Un lot = une matière = un contexte frais.** Deux matières dans une même fenêtre =
  le budget de lecture de chacune dilué + le cadrage payé deux fois. Sous-agents pour les lots,
  orchestrateur mince pour la boucle.
- **T-5 — En génération, l'unité de travail = le chapitre.** Chaque chapitre est généré avec :
  le **brief matière** (T-6) + **LA section de la fiche** couvrant ce chapitre (le chapitrage
  §4 / le manifeste découpent la fiche exprès pour ça) — jamais la fiche entière (70–200 k)
  dans le contexte de chaque chapitre.
- **T-6 — Le cadrage se paie une fois.** Par **campagne** : les docs de cadrage se lisent en
  Phase 0, pas à chaque lot. Par **matière** : préparer une fois un **brief matière** (~1 page :
  scope exact, terminologie officielle, calibrage âge, langue, pièges connus, conventions du
  sujet) réutilisé par tous les chapitres. Par **lot** : ne relire que la ligne `_INDEX.md` du
  couple + la fiche cible.
- **T-7 — Charger une règle quand elle sert.** La carte (`generation-pipeline.md`) d'abord ;
  chaque `references/*` seulement au besoin réel du chapitre en cours (`interactive-formats.md`
  si mission interactive ; `expert-exercises.md` si d3–4 / `prof-*` ; `course-figures.md` quand
  on illustre).
- **T-8 — R-7 par sondage dirigé, pas par re-lecture intégrale.** 100 % du critique + ≥15 % du
  reste, escalade en re-lecture intégrale dès 3 erreurs substantielles (protocole A5.2). Une
  re-lecture complète par défaut doublerait le coût vision de la campagne ; un skip viderait la
  garantie.
- **T-9 — Budget déclaré, arrêt propre, coût mesuré.** À l'approche du plafond (BUDGET, ou la
  fenêtre de contexte) : finir proprement le lot en cours, étiqueter la profondeur atteinte,
  pousser, s'arrêter — la campagne reprend où `_INDEX.md` / le ledger en sont. Chaque lot
  **rapporte son coût** (tokens in/out si le harnais les expose, sinon pages lues / volume
  écrit) : le coût par chapitre publié est le KPI de l'étude 12 — il se mesure, il ne s'estime
  pas.
- **T-10 — Des livrables courts et fréquents : jamais une longue session sans PR.** Le travail
  d'une session coupée avant son push est perdu à 100 % — la pire dépense token possible. En
  **LOT B** : commit local après **chaque chapitre complet**, push en PR par **tranche de ≤4
  chapitres** (B2/B3) — on ne retient jamais une matière entière non poussée. En **LOT A** :
  quand la session doit finir, la fiche partielle **honnêtement étiquetée se pousse** (arrêt
  propre, A3.4) plutôt que de viser le « tout » dans une session à risque. Interruption
  imminente au milieu d'un chapitre ou d'une tranche ⇒ push de sauvegarde en branche `wip/…`
  (le préfixe `wip/` et la PR draft exemptent tous deux de la chaîne de merge), que la session
  suivante reprend.

## Profils de source

| Profil               | Quand                                                                | Sources                                                                                                                   | Livrable fiche (LOT A)                                                                                                                                                              | Work-list                                                                                                |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **ecole-cnp**        | cycle de base (`1ere-base` → `9eme-base`)                            | guide enseignant CNP (`5…`) **+** manuel élève (`1…`), **combinés**                                                       | `programme/<niveau>/<matière>.md` + `manifest/<niveau>.json`                                                                                                                        | `programme/_INDEX.md` (couples `[ ]`)                                                                    |
| **ecole-secondaire** | lycée (`1ere-sec` → `bac-*`)                                         | manuel élève du secondaire (`2…`) + programme officiel du ministère s'il est publié ; **manuel seul ⇒ il fait référence** | idem ecole-cnp (les sections sont des nœuds `grades` ; slugs de [`docs/lycee-architecture.md`](https://github.com/MBeji/yahia-quest-arena/blob/main/docs/lycee-architecture.md))    | matrice sections × matières de `docs/lycee-architecture.md` ; **créer** la ligne `_INDEX.md` dans le lot |
| **document-libre**   | PDF d'enseignant, polycopié, annales papier — tout doc hors corpus   | le document lui-même (**droits R-2 vérifiés** : auteur, origine, autorisation)                                            | école : `programmes-officiels/sources-externes/<slug>/fiche.md` ; hors école : `content/_sources/<theme>/<slug>/fiche.md` — **même gabarit** `_TEMPLATE.md` + en-tête de provenance | — (la PR trace ; pas de ligne `_INDEX.md`)                                                               |
| **source-web**       | une source **en ligne** : site de devoirs/séries, blog d'enseignant, portail d'annales | la page publique elle-même (**tier déclaré avant tout token**, étude 27 R-1)                                              | école : `programmes-officiels/sources-externes/web-<slug>/fiche.md` ; hors école : `content/_sources/<theme>/web-<slug>/fiche.md` — gabarit `_TEMPLATE.md` + **en-tête de provenance en 8 champs** | — (la PR trace ; jamais de ligne `_INDEX.md` : une source web n'est pas un programme)                     |
| **sans-source**      | la fiche existe (`[~]`/`[x]`) mais le contenu manque sous `content/` | aucune (la fiche mergée)                                                                                                  | — (sauter le LOT A)                                                                                                                                                                 | `content/CATALOGUE.md` (sujets existants)                                                                |

Notes par profil :

- **ecole-cnp.** Guide enseignant = le **programme** (scope, compétences, progression, bornes) ;
  manuel élève = le **contenu enseigné** (leçons, exemples, exercices). Divergence ⇒ le guide
  fait foi (signaler §5). Décodage du code à 6 chiffres : 1er chiffre = rôle/cycle (`5` guide
  base, `1` manuel base, `2` secondaire) · chiffres 2-3 = matière · chiffre 4 = classe (guide
  `502304` ↔ manuel `102304`). Téléchargement :
  `https://www.cnp.com.tn/arabic/PDF/<code>P00.pdf` (parfois `P01`/`P02`, multi-tomes) ; corpus
  local déjà téléchargé : `cnp-officiel/CATALOGUE.md`. ⚠️ Le site CNP bloque parfois les
  requêtes automatisées (403/WAF) : demander les PDF au contributeur (champ `FICHIERS`) et
  **continuer la campagne** avec les couples suivants.
- **ecole-secondaire.** Le corpus secondaire n'est pas indexé par les codes guides du cycle de
  base : chercher d'abord `cnp-officiel/CATALOGUE.md`, puis le site CNP, sinon `FICHIERS`.
  Manuel élève seul ⇒ il fait référence — le signaler explicitement dans la fiche. **Aucune
  source officielle trouvable ⇒ STOP** (jamais d'invention). En LOT B, les matières
  scientifiques s'écrivent en **français natif, dans le jargon des manuels officiels — jamais
  une traduction** (décision 2026-07-13) ; sections, slugs et ids : `docs/lycee-architecture.md`
  (**dépôt moteur** — `engine/docs/…` une fois le clone en place, § Phase 0.1).
- **document-libre.** Checklist droits **avant tout token** : auteur identifié, origine,
  autorisation écrite (ou corpus officiel) — sinon refus (R-2). La fiche porte un en-tête de
  provenance (auteur, origine, autorisation, date) ; les `sources[]` du chapitre généré
  citeront le document. R-3 : si une transcription CNP du couple existe, confronter — le
  programme gagne.
- **source-web.** Voir la section dédiée ci-dessous : le tier se déclare **avant** le premier
  token, et il est opposable pour toute session ultérieure.
- **sans-source.** Vérifier que la fiche est bien à **profondeur de génération** (R-5 — une
  first-pass ne se génère pas), puis dérouler directement le LOT B.

### Le profil `source-web` — ce qu'on prend, exactement, à un lien (étude 27)

Il existe un écosystème tunisien de sites gratuits qui publient devoirs de contrôle et de
synthèse, séries par chapitre et corrigés. C'est le seul gisement qui dise **à quel niveau
d'exigence un chapitre tombe vraiment** : le manuel officiel donne le périmètre, le devoir de
prof donne le plafond. Mais selon ce qu'on y prend, on est dans du calibrage sans risque ou dans
de la contrefaçon — d'où **quatre tiers, dont un seul exige une autorisation** :

| tier      | ce qu'on prend                                                                       | copie     | autorisation écrite |
| --------- | ------------------------------------------------------------------------------------ | --------- | ------------------- |
| **T0**    | des **faits** : années servies, typologie DC1/DC2/DS, plafond d'exigence, vocabulaire | aucune    | non                 |
| **T1**    | **rien** — on pointe (lien sortant curé, si la feature existe)                       | aucune    | non                 |
| **T2′**   | la **carte notionnelle et typologique**, puis les `prof-*` écrivent des énoncés neufs | aucune    | non                 |
| **T2**    | le **contenu** (énoncés, corrigés) — transcription fidèle                            | intégrale | **OUI, bloquante**  |

**La ligne T2′, à connaître par cœur** : *un énoncé est une expression protégée, une notion ne
l'est pas.* « Calculer la résultante de deux forces concourantes » se reprend librement ; la
phrase de l'auteur, ses valeurs numériques, son contexte narratif et la formulation de son
corrigé, non. Contexte et nombres sont **réinventés**, jamais transposés. `content:qa` le
**vérifie** (recouvrement de 8 mots avec toute fiche non autorisée ⇒ `[error]`) — ce n'est pas
une consigne d'honneur.

Cinq règles qui s'ajoutent au socle R :

- **Un site tiers n'est JAMAIS une référence de programme.** Extension de R-3 : le
  manuel/guide officiel fait foi ; un devoir reflète ce qu'un établissement a choisi d'évaluer,
  pas le périmètre officiel. « Aucune source officielle trouvable ⇒ STOP » reste entier — une
  source web ne comble pas ce STOP.
- **Le défaut est la surveillance.** Fiche sans en-tête, autorisation `aucune` ou `demandée` :
  surveillée. Seule une autorisation `accordée` la lève.
- **Le snapshot ne rentre pas dans le dépôt.** Le PDF/HTML consulté vit dans le wrapper hors git
  (`YahiaAcademy/sources-web/<slug>/`), jamais sous `content/`. Un corpus tiers dans notre git
  est exactement ce que `leak:check` protège dans l'autre sens.
- **Robots & CGU.** Un site qui interdit l'accès automatisé se lit **à la main** ou pas du tout.
  Aucun contournement de WAF, jamais (même réflexe que le 403 du site CNP).
- **Réciprocité.** `LICENSE-CONTENT.md` interdit contre notre contenu ce qu'une aspiration ferait
  à celui d'autrui. En cas de doute, applique la décision à nous-mêmes : si elle nous
  scandaliserait, elle est refusée.

**En-tête de provenance — 8 champs, tous obligatoires.** Un champ manquant ⇒ la fiche n'est pas
exploitable et la session s'arrête (même sévérité que la checklist droits de `document-libre`) :

```yaml
url: https://<domaine>/<chemin>        # la PAGE consultée, jamais le fichier
titulaire: <personne morale ou physique identifiée, ou "inconnu">
consulte_le: 2026-08-13                # date de consultation (le web bouge)
cgu: <URL des CGU/mentions légales, ou "absentes">
robots: <"autorise" | "interdit" | "absent">
autorisation: <"aucune" | "demandee le JJ/MM" | "accordee le JJ/MM par <qui>">
tier: <"T0" | "T1" | "T2-prime" | "T2">        # opposable
snapshot: YahiaAcademy/sources-web/<slug>/     # hors git + empreinte
```

⚠️ **Deux pièges avant d'espérer un T2.** Un site qui **ré-héberge des PDF d'enseignants tiers**
— cas dominant dans cet écosystème — **n'a pas les droits à céder** : son tier plafonne à T2′
quelle que soit sa bonne volonté. Et l'accès lui-même n'est pas acquis : une session cloud voit
ces domaines **bloqués par la politique d'egress** (constaté le 2026-08-13) — la qualification se
fait depuis le poste Windows, ou en autorisant le domaine dans l'environnement.

## Phase 0 — bootstrap (une fois par campagne, T-6)

1. **Cloner les deux dépôts côte à côte, installer le moteur, brancher le corpus dedans.** Le
   corpus est l'espace de travail (branches, commits, PR) ; le moteur fournit les commandes.
   Depuis le répertoire parent qui accueillera les deux :

   ```bash
   git clone https://github.com/MBeji/yahia-quest-content.git corpus   # privé  — l'espace de travail
   git clone https://github.com/MBeji/yahia-quest-arena.git   engine   # public — le moteur
   (cd engine && npm ci)                                               # Node 22 / npm 10
   ```

   Les scripts du moteur résolvent `content/` **et**
   `.claude/skills/content-ecole-tn/references/programmes-officiels/` **relativement à leur
   propre racine** : sans les deux liens ci-dessous, `content:*` ne voit aucun corpus et
   `programme:check`/`content:audit` échouent avant même de le lire. C'est exactement ce que
   fait la CI privée (`.github/workflows/content-ci.yml`) :

   ```bash
   rm -rf engine/content engine/.claude/skills
   ln -s "$PWD/corpus/content"        engine/content
   ln -s "$PWD/corpus/.claude/skills" engine/.claude/skills
   ```

   Windows sans mode développeur (`ln -s` inopérant) — jonctions, mêmes chemins :

   ```powershell
   Remove-Item -Recurse -Force engine\content, engine\.claude\skills -ErrorAction Ignore
   New-Item -ItemType Junction -Path engine\content        -Target $PWD\corpus\content
   New-Item -ItemType Junction -Path engine\.claude\skills -Target $PWD\corpus\.claude\skills
   ```

   Contrôle avant d'aller plus loin (les deux assertions de la CI) :

   ```bash
   test -f engine/content/misconceptions.json &&
   test -d engine/.claude/skills/content-ecole-tn/references/programmes-officiels/manifest &&
   echo "corpus + skills branchés"
   ```

   Trois choses à savoir, sinon on casse quelque chose :
   - **Toutes les commandes `npm run …`** de cette méthode se lancent depuis **`engine/`** ;
     **tous les `git`/`gh`** (branche, commit, PR) depuis **`corpus/`**. Le dépôt de contenu n'a
     ni `package.json`, ni husky, ni Prettier — **rien ne s'y formate au commit**.
   - `engine/` est un **clone de service** : le lien écrase ses 5 skills techniques et son
     `git status` devient bruyant. On n'y commite ni n'y pousse **jamais** pendant une campagne.
   - ⚠️ Un lien/jonction ne se supprime **jamais** par `rm -rf` (ça viderait la cible, donc le
     corpus) : `rm` sur le lien en POSIX, `(Get-Item <lien> -Force).Delete()` en PowerShell.

2. **Cloner + builder ScribeKit** (moteur déterministe — 0 LLM, 0 clé API) :

   ```bash
   git clone https://github.com/MBeji/ScribeKit.git ../ScribeKit
   (cd ../ScribeKit && npm install && npm run build)
   alias scribekit="node $(pwd)/../ScribeKit/dist/bin.js"
   ```

3. **Lire le cadrage — maintenant, pas à chaque lot.** Tout est dans `corpus/`, sauf mention
   contraire :
   - `programmes-officiels/programme/README.md` (spec de la couche de persistance + « Recette »
     de génération — la procédure normative du LOT B) ;
   - `programme/_TEMPLATE.md` (le gabarit de fiche) + un modèle abouti :
     `programme/1ere-sec/mathematiques.md` ;
   - `.claude/skills/content-ingest/SKILL.md` (les règles R intégrales — elles s'appliquent à
     toi) ;
   - si `GENERATION: oui` : `.claude/skills/content-engine/references/generation-pipeline.md`
     (la carte des skills du LOT B) ;
   - **dépôt moteur** : `engine/AGENTS.md` § « Content pipeline » (la hiérarchie qui gagne) et
     `engine/docs/content-generation-pipeline.md` (le flux complet fichiers → SQL → prod).

   L'espace de travail des fiches, dans le dépôt de **contenu** :

   ```
   .claude/skills/content-ecole-tn/references/programmes-officiels/
   ├── suivi/corpus-cnp.json                    ← corpus CNP exhaustif (346 PDF — généré, ne pas éditer)
   ├── suivi/affectations.json                  ← catégorie de chaque matière/PDF (décisions)
   ├── suivi/<grade>.json                       ← REGISTRE d'état des fiches (LA source de vérité)
   ├── programme/_INDEX.md                      ← vue GÉNÉRÉE du registre (⛔ ne pas éditer)
   ├── programme/_TEMPLATE.md                   ← gabarit de la fiche
   ├── programme/README.md                      ← spec + « Recette » (LOT B)
   ├── programme/<niveau>/<matière>.md          ← livrable LOT A (profils ecole-*)
   ├── sources-externes/<slug>/fiche.md         ← livrable LOT A (document-libre, école)
   └── manifest/<niveau>.json                   ← chapitrage machine-vérifiable (Zod)
   ```

   Trois commandes gouvernent le registre — **depuis `engine/`**, comme toutes les autres :
   `npm run programme:check` (le gate — schémas + anti-doublon + cohérence disque↔registre↔index,
   exécuté par la Content CI), `npm run programme:index` (régénère la vue), `npm run
programme:corpus` (resynchronise le snapshot corpus depuis le `cnp-officiel/catalogue.csv`
   voisin du clone moteur — `--catalogue <chemin>` pour le pointer ailleurs ; machine locale
   uniquement). Elles écrivent **dans le corpus**, à travers le lien : le diff apparaît dans
   `corpus/`, c'est là qu'on le commite. Une quatrième, `npm run programme:etat`, n'est **pas**
   un gate mais le **rapport** d'état du couple (fiche × programme × contenu) — c'est elle qu'on
   lance en A1, et elle ne classe jamais les couples par priorité (§ Phase 0.4).

4. **Construire la file de travail** — puis la **présenter et demander** par quoi commencer.
   L'ordre ci-dessous est la **priorité par défaut proposée** (décision 2026-07-14 — le lycée
   d'abord : c'est le gros trou du corpus, le cycle de base est largement couvert) ; **le choix du
   couple à lancer reste l'arbitrage humain** (décision 2026-07-26) : ni l'outillage
   (`programme:etat`, qui ne classe rien) ni l'agent ne recommandent, ne réordonnent, ni ne
   démarrent sans réponse.
   1. **`1ere-sec`** — tronc commun, pas de section : le plus fort levier ; la finir avant la
      suite ;
   2. **`2eme-sec-*`**, section par section (`sciences` · `lettres` · `eco-services` · `info`) —
      une section entièrement terminée avant d'ouvrir la suivante ;
   3. **`3eme-sec-*`** (`math` · `sciences-exp` · `lettres` · `eco-gestion` · `techniques` ·
      `info`) ;
   4. **`bac-*`** (`math` · `sciences-exp` · `lettres` · `eco-gestion` · `techniques` · `info`) ;
   5. seulement ensuite, le **reliquat du cycle de base** (`1ere-base` → `9eme-base`).
   - Source de la file : le § « **À transcrire (dérivé du corpus)** » de l'`_INDEX.md` généré —
     la liste **exhaustive** des œuvres principales non rattachées, calculée depuis
     `suivi/corpus-cnp.json` (au secondaire, préciser la section avec la matrice de
     `docs/lycee-architecture.md`) ; les entrées `partielle` du registre (trous listés) font
     aussi partie de la file.
   - **Matières annexes hors périmètre pour le moment** : musique, éducation artistique/dessin,
     EPS/sport, la section sport, les 3èmes langues (allemand, espagnol, italien). Les sauter
     même si leur ligne est `[ ]` ; un `PORTEE` qui les cible explicitement se **refuse** avec
     rappel de cette règle.
   - **Annoncer la file** au contributeur (nombre de lots, ordre par défaut, couples sautés et
     pourquoi), **lui demander par quoi commencer**, et ne démarrer la boucle qu'avec sa réponse.

---

## LOT A — la fiche (phases 1-2)

### A1 — Vérifier l'existant (R-4)

Branche fraîche — **dans `corpus/`** (toute la campagne se branche et se pousse là) :

```bash
git fetch origin main && git checkout -B feat/transcription-<niveau>-<matiere> origin/main
```

L'état du couple ne se reconstitue plus à la main — **depuis `engine/`** :

```bash
npm run programme:etat -- --grade <niveau>     # --json pour un traitement automatique
```

Il rapporte, pour chaque couple du niveau : statut, profondeur, **couverture calculée**, plages
non lues, verdict R-7 et génération autorisée ou non côté **fiche** ; sujet présent, chapitres
couverts/attendus et incomplets côté **contenu** ; plus le corpus principal encore non rattaché.
⚠️ Il **n'ordonne rien** : le choix du couple à lancer reste au contributeur (§ Phase 0.4) — la
commande donne les faits, jamais le classement.

Reste à vérifier ce que le registre ne sait pas toujours (une réservation `en-cours` n'est visible
qu'une fois poussée) : qu'**aucune autre session ne travaille déjà le couple** —
`gh pr list --search "<niveau> <matière>"` + branches distantes
`feat/transcription-<niveau>-*` (une PR/branche ouverte sur le couple ⇒ couple pris, passer au
suivant). Puis, dans le registre frais (`suivi/<grade>.json`) :

- entrée `en-cours` ⇒ **couple réservé** par une autre session (R-4) : ne rien lancer, ne pas
  toucher son entrée, passer au couple suivant.
- entrée `complete` / `validee-r7` / `promue` ⇒ **déjà fait**. Si `GENERATION: oui` et que le
  sujet n'existe pas sous `content/` (vérifier `content/CATALOGUE.md`) ⇒ passer directement au
  **LOT B** (profil sans-source) ; sinon couple suivant.
- entrée `partielle` ⇒ la **compléter** — le registre liste les **plages de pages manquantes**
  et la profondeur atteinte ; jamais refaire en parallèle, jamais relire les pages déjà à
  profondeur (T-2/T-3).
- **aucune entrée** (vrai manquant — le § « À transcrire » de l'_INDEX généré liste les PDF
  disponibles du couple) ⇒ continuer ; l'entrée sera créée en A5.4.

### A2 — Obtenir les sources

Selon le profil (§ Profils) : **combiner toutes les sources officielles disponibles** (guide
enseignant + manuel élève) ; une seule disponible ⇒ elle fait référence (le signaler dans la
fiche). `FICHIERS` fournis ⇒ identifier qui est guide / qui est manuel par le code à 6
chiffres. Téléchargement bloqué ⇒ demander les PDF et continuer avec les couples suivants.
**Jamais de contenu inventé faute de source.**

### A3 — Transcrire (phase 1 : ScribeKit + ta vision)

1. **ScribeKit d'abord** (T-1 — il extrait le déterministe, échafaude au gabarit, crée/valide le
   manifeste) :

   ```bash
   # depuis corpus/ — les chemins -o sont relatifs au dépôt de contenu
   # profils ecole-* :
   scribekit app-cnp <guide.pdf> [<manuel.pdf>] --grade <niveau> --subject <subject-id> \
     --lang <ar|fr|en> -o .claude/skills/content-ecole-tn/references/programmes-officiels
   # profil document-libre :
   scribekit transcribe <doc…> -o <emplacement de la fiche> --profile markdown
   ```

   (`<subject-id>` : convention du README programmes-officiels § identifiants — ex. `math-3eme`,
   `arabic-5eme` ; en cas de doute, proposer + signaler dans la fiche.)

2. `scribekit status <cible>` liste les unités **`pending`** (scans à couche-texte cassée — le
   cas général du corpus CNP). Pour chacune : lire les pages **en vision** et transcrire **par
   tranches de 10–20 pages, écriture immédiate au format final** (T-2). DPI 150 par défaut
   (`render.sh` → PNG si besoin de le maîtriser). ⚠️ **Pas de clé API** : l'OCR passe par TA
   vision d'agent (abonnement) ; le `--provider anthropic` de ScribeKit est un mode batch
   **facturé** — uniquement si le contributeur fournit une clé et le demande.

3. **Fidélité absolue** : transcrire **ce qui est imprimé**, rien d'autre. Illisible ⇒ `[?]` +
   note en § Incertitudes, jamais deviné ; coquille source ⇒ `[sic]`. **Chiffres occidentaux
   (0-9) partout** — y compris dans le texte arabe, jamais ٠١٢٣ — équations LTR, unités SI,
   Markdown arabe bidi-safe. **Citer les pages, par source** (guide vs manuel) : la fiche doit
   rester revérifiable. Œuvres périphériques sous droits ⇒ résumer + référencer (R-2).

4. **Lecture intégrale (R-6)** : la source **en entier** avant de clore la phase. Budget court ⇒
   arrêt propre en fin de section + étiquette honnête de profondeur (« modules 1–4 en
   profondeur, 5–7 en first-pass ») — puis **pousser ce palier** (A5→A6 : PR normale, ligne
   `[~]` avec la profondeur) plutôt que de garder des heures de transcription non poussées
   (T-10) ; la session suivante **complète** la fiche, ne la refait pas (R-4).

### A4 — Enrichir (phase 2 : profondeur de génération, R-5)

Une fiche « résumé » ne sert à rien : la cible est le standard qui permet de générer cours et
exercices **sans jamais rouvrir les scans** (T-3). Compléter §1–§6 du gabarit en combinant
guide + manuel :

- **chaque activité / exercice du manuel décrit individuellement** (énoncé, données, ce qui est
  demandé) — jamais « des exercices d'application p.12-15 » ;
- **encadrés de règles/lois officiels verbatim** (« Retenir », « Repère », l'essentiel du
  cours…) ;
- **vocabulaire et terminologie officielle** relevés tels quels ;
- **bornes de scope** explicites : ✅ INCLUS au niveau / ⛔ EXCLU (relève d'un autre niveau) ;
- **§4 Chapitrage** rempli (slug, notion, pages du manuel élève), puis **codifié dans
  `manifest/<niveau>.json`** (champ `manuel = { code, pages }` par chapitre ; JSON valide —
  schéma Zod de l'app). Ce chapitrage est l'ossature du LOT B (T-5) ;
- divergence guide ↔ manuel ⇒ le **guide enseignant fait foi** pour le scope ; signaler l'écart
  avec la page (§5).

### A5 — Auditer (rien ne part sans ça)

1. **QA déterministe** (T-1) — 0 erreur exigé :

   ```bash
   # depuis corpus/
   scribekit qa .claude/skills/content-ecole-tn/references/programmes-officiels
   scribekit status .claude/skills/content-ecole-tn/references/programmes-officiels  # plus aucun pending
   ```

2. **R-7 — relecture indépendante par sondage dirigé (T-8)** : un second agent/sous-agent au
   **contexte vierge** re-vérifie la fiche **contre les PDF sources** (pas contre le travail du
   premier) :
   - **100 %** : les encadrés verbatim, le chapitrage/manifeste (existence, ordre, plages de
     pages), toutes les zones `[?]` / § Incertitudes, les titres et la numérotation des
     modules ;
   - **échantillon** : ≥15 % des pages restantes (minimum 10 pages), tirées sur toute l'étendue
     (début / milieu / fin) — re-vérifier fidélité, notation 0-9/LTR, rien d'inventé ;
   - **escalade** : ≥3 erreurs **substantielles** (invention, contresens, omission d'items) ⇒
     la fiche est sous la barre — re-lecture intégrale contre la source. Erreurs de forme
     (typo, notation) ⇒ corriger, pas d'escalade ;
   - **verdict consigné** : fiche § Incertitudes + `_INDEX.md`
     (« R-7 AAAA-MM-JJ, sondage N pages, X corrections »).

3. **Gate du dépôt de contenu** — depuis `engine/`, 0 erreur exigé :
   `npm run programme:check` (et, si le lot a aussi touché `content/`, `content:check` +
   `content:qa:strict`). Le `npm run verify` du **moteur** (lint + typecheck + tests de l'app)
   **ne concerne pas** un LOT A : le corpus ne porte ni code ni hooks git — rien ne s'y formate
   au commit, il n'y a pas de `--no-verify` à contourner. La Content CI rejouera exactement ces
   gates sur la PR.

4. **Mettre à jour le REGISTRE `suivi/<grade>.json`** (⛔ jamais `_INDEX.md` à la main — c'est
   une vue générée) : créer/actualiser l'entrée du couple avec le **statut normé** (`partielle`
   si trous de lecture ou de profondeur, `complete` si 100 % + profondeur de génération —
   **jamais `promue`**, réservé à l'humain), la **profondeur** (`first-pass`/`mixte`/
   `generation`), les **sources par code corpus** avec `pagesTotal` et les **plages exactes
   `pagesLues`** (le % est calculé — fini les « ~48 % » déclarés), le verdict `r7`, `maj`/`par`
   (PSEUDO) et des notes courtes. Grade lycée sans fichier de suivi ⇒ créer
   `suivi/<gradeSlug>.json` (slugs de `docs/lycee-architecture.md`).

   **Déclarer aussi `sujets`** — les ids de sujets de `content/` dont cette fiche est la source
   de scope (ex. `["math-1ere-sec"]`). C'est le seul lien fiche → contenu : personne ne le
   devine (`mathematiques` alimente `math-1ere-sec`, `chimie` n'alimente aucun sujet propre), et
   sans lui `programme:etat` ne peut pas dire si le contenu du couple existe. Les ids attendus au
   niveau sont ceux du manifeste — `programme:check` refuse un id qui n'y figure pas. Aucun sujet
   correspondant (matière transcrite mais hors programme codifié) ⇒ laisser `[]` et le dire en
   note. Puis :

   ```bash
   # depuis engine/ — l'écriture atterrit dans corpus/ via le lien
   npm run programme:index    # régénère la vue _INDEX.md
   npm run programme:check    # 0 erreur exigé — doublons, plages, cohérence disque↔registre
   ```

### A6 — Pousser le LOT A

À committer — et **rien d'autre** : la fiche, le manifeste, le **registre**
`suivi/<grade>.json` et la vue `_INDEX.md` régénérée (+ sorties YAML du profil générique si
demandées). ⛔ Jamais : `.scribekit/ledger.json`, `AVANCEMENT.md`, les PDF sources, ni quoi que
ce soit sous `content/` (ça, c'est le LOT B) — seule exception : la fiche
`content/_sources/<theme>/<slug>/fiche.md` du profil document-libre non scolaire, qui est un
livrable du LOT A. Aucun SQL, aucune migration : le corpus n'en porte pas (§ B3).

```bash
# depuis corpus/
git add .claude/skills/content-ecole-tn/references/programmes-officiels/   # document-libre hors école : content/_sources/<theme>/<slug>/
git commit -m "feat(programme): transcription <matière> <niveau> — <codes sources> (FableEtudes/12#persistance)"
git push -u origin feat/transcription-<niveau>-<matiere>
gh pr create --fill
```

La chaîne de merge prend le relais : PR verte ⇒ **squash-mergée toute seule**. La session qui a
poussé reste néanmoins de garde — surveiller la Content CI (`gh pr checks <n> --watch`),
corriger tout rouge et re-pousser, puis **confirmer que le merge a réellement eu lieu** avant le
LOT B (ou le couple suivant). Un déclenchement manqué se rattrape par
`gh workflow run automerge.yml -f pr=<n>`.

---

## LOT B — le contenu (phase 3)

> Seulement si `GENERATION: oui` **et** la fiche du couple mergée sur `main` — une fiche restée
> first-pass ne se génère pas (repasser par A3–A4). Ici on change de casquette : on ne
> transcrit plus, on **génère avec les skills du dépôt**, qui font foi. Ne réinventer aucune
> règle.

### B1 — Brief + skills (T-6, T-7)

1. Branche fraîche, **dans `corpus/`** : `git fetch origin main`, puis
   `git checkout -B feat/content-<subject-id> origin/main`.
2. La procédure normative de cette phase est la **« Recette »** de
   `programmes-officiels/README.md`. Sa règle d'or (= T-3) : **la fiche
   `programme/<niveau>/<matière>.md` est la source de scope ET de contenu — ne jamais rouvrir
   les PDF.**
3. Préparer le **brief matière** (~1 page, T-6) depuis la fiche : scope exact, terminologie
   officielle, **calibrage âge** (§ « Adapter à l'âge » du README programmes-officiels),
   **langue du contenu** (matière arabe ⇒ tout en arabe, `nameFr` inclus ; lycée scientifique ⇒
   français natif, jargon des manuels — décision 2026-07-13), pièges/erreurs types, conventions
   du sujet (`id`, `themeId`, `gradeSlug` — slugs pris : `content/CATALOGUE.md`).
4. Charger **la carte** (`content-engine/references/generation-pipeline.md`), puis au besoin
   réel (T-7) : `content-ecole-tn` (fidélité programme — le wrapper de tout contenu scolaire),
   `content-cours` (cours/résumé), `content-interactif` (formats variés),
   **`prof-<matière>-<cycle>`** s'il existe (exercices durs d3–4). Sous Claude Code les skills
   s'invoquent nativement ; autre agent : lire chaque `SKILL.md` + la référence utile, et les
   appliquer à la lettre.

### B2 — Générer par tranches de chapitres (T-5, T-10)

Dans l'**ordre du chapitrage** (§4 de la fiche / `manifest/<niveau>.json`), par **tranches de
3 chapitres complets par défaut — jamais plus de 4 non poussés**. Pour chaque chapitre —
contexte : **brief matière + la section de la fiche de CE chapitre** :

- produire `chapter.json`, `cours.md`, `resume.md`, `quiz.json`, `exercices/*.json` (ladder
  standard — voir les skills). Sujet absent de `content/` ⇒ créer `subject.json` dans la
  **première tranche**, selon la convention d'identifiants ;
- **Illustration (axe 5 — s'applique à toute campagne depuis l'étude 18)** : toute notion
  spatiale/visuelle se **dessine** (cours `::: figure` ; question `<svg>` inline), figures
  **vraies** (double-résolues sur la figure) qui ne fuitent pas la clé ; petites classes
  (1ère–3ème) ⇒ presque tout illustré, coloré ;
- auto-vérification par chapitre : re-résolution à l'aveugle, distracteurs = erreurs exécutées,
  équilibre des clés, notation standard (0-9, LTR ; milliers arabes en U+00A0 **cohérent**) ;
- **périmètre nommé par agent, et interdiction du gabarit** : les fichiers d'un chapitre
  s'écrivent en parallèle par des agents qui ne se voient pas. Donner à chacun (a) la liste
  **exacte** des fichiers qu'il écrit, (b) le périmètre enseigné par le cours, (c) le chemin des
  chapitres **déjà publiés** de la matière, avec l'ordre d'y aller avant d'écrire. Sans (c), le
  moule d'un item se rejoue d'un chapitre à l'autre — voir « le doublon de gabarit » ci-dessous ;
- **commit local après chaque chapitre complet** (fichiers `content/` seulement — il n'y a
  aucun SQL à committer, § B3). Un chapitre part **complet ou pas du tout** dans une PR ready
  (cours + résumé + quiz + ≥1 mission) : un chapitre entamé mais pas fini reste hors tranche
  (ou part en `wip/` si la session s'interrompt, T-10).

Tranche pleine — ou budget/fenêtre qui approche de sa fin — ⇒ passer en B3 pour la livrer. La
matière est **finie** quand `content:audit` ne signale plus ni chapitre manquant ni chapitre
incomplet pour ce sujet vs le manifeste.

#### Le doublon de gabarit — le défaut dominant de l'écriture parallèle

Mesuré sur les deux premières tranches d'`english-1ere-sec` (corpus #117 et #120, 138 questions) :
**138/138 clés justes**, et pourtant **10 doublons de gabarit sur 33 constats MAJOR**, dont 5
**inter-chapitres**. C'est le mode de défaut n°1, et il est **invisible partout** : les quatre
gates ne le voient pas, et une mesure de similarité lexicale (Jaccard sur énoncé + options) a
rendu **0 paire** sur les deux tranches.

Il est invisible parce que ce n'est pas le lexique qui se répète, c'est la **forme de la tâche** :
même structure d'énoncé, même type de question, même jeu de distracteurs — décor changé. Exemple
réel, servi **quatre fois** dans la même matière dont une déjà publiée deux tranches plus tôt :
« _Read this passage. \<Nom\> tient un commerce à \<ville\> depuis \<durée\>… à quoi renvoie ce
pronom ?_ ». Un auteur ne peut pas le voir — il n'a que son chapitre. Seul un relecteur qui lit
les chapitres **publiés** le voit.

Deux parades, l'une en amont, l'autre en aval (§ B3) :

- dans le brief de chaque auteur, le point (c) ci-dessus — le chemin des chapitres publiés et
  l'ordre d'y aller **avant** d'écrire ; et la consigne explicite « change la **tâche**, pas
  seulement le décor » ;
- **les trois mesures muettes, à faire AVANT le commit** (un script jetable de ~40 lignes sur
  `quiz.json` + `exercices/*.json` suffit ; aucun gate ne les porte encore) :

  | mesure                                                    | seuil                            | ce qu'elle attrape                                                                     |
  | --------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- |
  | la clé est-elle l'option **strictement la plus longue** ? | viser 0 % ; le hasard est à 25 % | la fuite par la forme — mesurée à 57–76 % sur des lots antérieurs                      |
  | distribution des clés **a/b/c/d**                         | ≈ 25 % chacune                   | l'écriture au gabarit (clé rédigée d'abord, distracteurs en remplissage)               |
  | paires de questions proches (Jaccard ≥ 0,45)              | 0                                | les doublons **littéraux** — pas les doublons de gabarit, qui échappent à cette mesure |

  Les deux premières se corrigent sans déplacer aucune clé. La troisième ne remplace **jamais**
  l'audit humain : elle ne voit que ce qui se répète en mots.

### B3 — Gates, push, prod (à chaque tranche)

```bash
# depuis engine/ (le corpus y est branché — § Phase 0.1)
npm run content:check          # validation Zod de tout le contenu
npm run content:qa:strict      # QA stricte — 0 [error]
npm run content:audit          # conformité au programme + couverture vs manifeste
```

(`content:audit` sur une tranche intermédiaire : les chapitres des tranches **suivantes**
apparaissent « manquants » — c'est attendu tant que la matière n'est pas finie ; à la
**dernière** tranche, 0 manquant / 0 incomplet exigé pour ce sujet.)

Puis **audit pédagogique** : appliquer le skill `content-audit` sur les **chapitres de la
tranche** (re-résoudre chaque question à l'aveugle, clés/distracteurs/calibrage) et corriger
avant de pousser. **Un auditeur par chapitre, en contexte vierge, qui n'a écrit aucune ligne de
ce qu'il relit** — l'auto-relecture de l'auteur ne compte pas : elle confirme les clés, et passe
à côté de tout le reste. Quatre points à mettre dans son mandat, chacun payé par une campagne :

1. **le chemin des chapitres déjà publiés**, avec l'ordre de croiser — sans ça, les doublons
   inter-chapitres ne sont pas trouvables (§ B2, « le doublon de gabarit ») ;
2. **les paires que l'orchestrateur a déjà repérées à la main**, nommément à trancher : c'est en
   cherchant autour qu'il trouve les autres ;
3. **quels fichiers n'ont pas de rapport d'auteur** — un sous-agent tué par la limite de session
   laisse des fichiers complets mais jamais relus. Ils ne sont pas faux (0 clé fausse sur les 24
   items concernés en #120), mais ils ont porté **11 des 16 constats** de leur chapitre : le dire
   à l'auditeur change ce qu'il cherche ;
4. le mandat lui-même : **« trouve ce qui est faux, pas ce qui est bon »**, et il ne modifie aucun
   fichier — il rend des corrections prêtes à appliquer (ancien texte → nouveau texte).

L'orchestrateur **arbitre** ensuite constat par constat (ce qu'on applique, ce qu'on écarte et
pourquoi), puis fait appliquer. ⚠️ **La correction prescrite peut elle-même être fautive** :
quatre correcteurs sur six l'ont attrapée en deux tranches — une consigne introduisait un verbe
hors du périmètre de la leçon, une autre rendait la clé strictement l'option la plus longue.
Donc, dans le brief du correcteur : **re-résoudre à l'aveugle chaque item touché** et **re-mesurer
les trois métriques** (§ B2) après application, pas seulement appliquer.

Correction **sur place, toujours** : jamais de réordonnancement de questions, jamais de renommage
d'id d'option — l'identité en base dépend de la position et des slugs (§ « Slugs are identity »).

**Rien à compiler à la main** (étude 24 D-3) : le contenu **ne voyage plus en migrations**. Il
est compilé par `content:emit` en un fichier **stable par matière** `sql/content/<subject>.sql`,
et c'est le workflow d'application qui l'émet au moment d'appliquer. Un auteur ne commite donc
**que des fichiers `content/`** — jamais de SQL.

> ⚠️ **Ne jamais lancer `npm run content:build`.** Sans `--sql-dir`, il écrit des migrations
> horodatées dans `engine/supabase/migrations/` : un canal **mort** depuis l'étude 24, et une
> fuite de corpus dans le dépôt **public** que son gate `leak:check` bloque. Pour inspecter le
> SQL localement (facultatif, jamais committé), émettre dans un répertoire jetable :
> `node --experimental-strip-types scripts/content/build.ts --subject <id> --sql-dir /tmp/sql-check`.

**Commit de tranche** — les chapitres de la tranche, rien d'autre :

```bash
# depuis corpus/
git add content/<subject-id>
git commit -m "feat(content): <subject-id> ch.NN-MM — génération depuis la fiche (FableEtudes/12#generation)"
git push -u origin feat/content-<subject-id>-chNN-MM
gh pr create --fill
```

Comme au LOT A : surveiller la Content CI, corriger tout rouge, et confirmer le merge (la
chaîne de merge s'en charge dès que tout est vert).

**Puis la mise en prod, qui est un geste délibéré.** Contrairement au canal schéma du moteur
(`db-migrate-prod`, automatique au merge), `apply-content.yml` est en **`workflow_dispatch`
uniquement** — le déclencheur automatique prévu par l'étude 24 est **désarmé** : _un merge
n'applique rien_. Il faut le dispatcher (write requis sur le dépôt privé) :

```bash
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=true    # le plan d'abord
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=false   # puis l'application
```

Le run garde la cible (refus si l'URL n'est pas la prod), prend un `pg_dump` avant écriture,
applique chaque sujet en une transaction (`ON_ERROR_STOP`, idempotent : rejouer est sûr) et
**journalise** dans `content_releases`. Vérifier le run vert **et** la ligne du journal, puis
**tranche suivante** (branche fraîche depuis `origin/main` mergé, B2) — et quand la matière est
finie, **reprendre la boucle** au couple suivant. Un contributeur externe sans droit de
dispatch s'arrête au merge et le signale : la publication reste au responsable du dépôt.

## Retoucher du contenu déjà écrit (ajouter un champ en masse)

Ajouter un champ à des questions **déjà écrites** — le `competencies` du tagging de
compétences (étude 07 lot 3, PR #51→#61), demain un autre — n'est pas de la génération :
c'est un **patch**. Il se fait par insertion textuelle, jamais par réécriture du fichier.

**Ce qui casse (mesuré le 2026-07-27).** Les JSON du corpus sont formatés par Prettier, dont
l'heuristique d'objet **préserve l'état replié/déplié de la source** : un objet dont
l'accolade ouvrante n'est pas suivie d'un retour à la ligne reste sur une ligne. C'est ce qui
garde les options compactes et lisibles (`{ "id": "a", "text": "…" }`). Un script qui charge
le fichier par `JSON.parse` puis le réécrit par `JSON.stringify(json, null, 2)` **perd cette
information** : toutes les options ressortent dépliées, une clé par ligne — et un
`prettier --write` derrière ne les recolle **jamais** (il n'y a plus d'objet sur une ligne à
préserver). Le tagging de 41 questions a ainsi produit un diff de **~2 500 lignes au lieu de
~250** : la PR devient illisible, donc non revue.

**La règle.** Repérer les bornes de chaque objet du tableau `questions` par comptage
d'accolades (en ignorant celles qui sont **à l'intérieur des chaînes**), insérer la ligne du
nouveau champ juste avant l'accolade fermante de l'objet (et la virgule sur la ligne
précédente), réécrire le fichier tel quel. Puis `prettier --write`, qui ne normalise alors que
la ligne ajoutée. Diff attendu : **2 lignes par question touchée**, rien d'autre. Un diff dix
fois plus gros est le symptôme d'une réécriture complète — on repart du fichier d'origine et
on repatche, on ne « reformate » pas après coup.

---

## Rapport de campagne

Quand la file est épuisée (ou à l'arrêt propre), rapporter au contributeur :

- par couple traité : lien PR LOT A / LOT B, profondeur atteinte, verdict R-7 (taille du
  sondage, corrections), **coût du lot** (T-9 — tokens in/out si exposés, sinon pages lues /
  volume écrit) ;
- l'état de la **publication** (`apply-content` dispatché, run vert, ligne `content_releases`) et
  celui de l'**ouverture** (migration `open_*` du dépôt moteur portée, ou restant à faire — R-8) :
  ce sont les deux gestes qui rendent le travail visible aux élèves. Depuis le 2026-08-03, la
  publication a **une** garde — `content-drift.yml` tient une issue `content-drift` ouverte tant
  qu'un sujet de `main` n'est pas en prod, et la referme d'elle-même : la question de fin de
  session n'est plus « la PR est-elle mergée ? » mais **« l'issue est-elle close ? »**. Elle
  constate, elle n'empêche pas — entre le merge et son passage suivant (push sur `content/`, ou
  06:40 UTC), la prod reste en retard. L'**ouverture**, elle, n'a toujours aucune garde ;
- couples sautés et pourquoi (déjà `[~]`, source indisponible, matière annexe…) ;
- ce qui reste dans `_INDEX.md` / la matrice lycée pour la campagne suivante.

Le **coût par chapitre publié** est le KPI de l'étude 12 : il se mesure à chaque campagne, il
ne s'estime pas.

## STOP (escalade — ne jamais improviser)

- Couple déjà `[~]`/`[x]` ⇒ on ne re-transcrit pas (A1) ; sauter, ou LOT B seul si le contenu
  manque.
- Source introuvable / téléchargement CNP bloqué sans `FICHIERS` ⇒ demander les PDF au
  contributeur et **continuer la campagne** avec les couples suivants.
- Doute sur les **droits** d'une source hors corpus officiel ⇒ STOP (R-2).
- Scan **illisible** ou manuscrit ⇒ transcrire le lisible, signaler le reste, ne jamais
  deviner.
- Divergence fiche ↔ programme officiel, ou gabarit/manifeste qui ne colle pas au réel ⇒ STOP
  et documenter (commentaire de PR ou issue), jamais d'adaptation silencieuse.
- LOT B sans fiche mergée, ou chapitre dont la section n'atteint pas la profondeur R-5 ⇒ **ne
  pas générer CE chapitre** ; repasser par A3–A4. Une fiche globalement `partielle` n'est plus
  un STOP en soi : elle l'est pour les chapitres hors de son `chapitresGeneration` (R-5, lu au
  chapitre). Ce qui reste un STOP franc : générer un chapitre que la fiche ne déclare pas, ou
  ajouter un slug à `chapitresGeneration` sans avoir lu la section correspondante.
- Un chapitre appelle un **format de contenu inexistant** dans le moteur ⇒ signalement (issue)
  vers l'étude 03 / le catalogue de formats, jamais un format ad hoc.
- **Rien ne s'applique à la main en base** : ni `psql`, ni l'éditeur SQL Supabase, ni
  `supabase db push`. Le seul canal du contenu, c'est `apply-content.yml` (§ B3). Un run rouge
  ou coupé ⇒ lire son résumé et **le redispatcher** (l'application est idempotente), jamais
  compenser à la main.
- Une **migration** ou un fichier `sql/` dans un commit de campagne ⇒ erreur de canal (§ B3) :
  retirer le fichier, ne jamais le pousser — a fortiori dans le dépôt public.
- Budget insuffisant ⇒ arrêt propre **au dernier palier poussable** (fin de tranche en LOT B,
  fiche partielle étiquetée en LOT A) + étiquetage honnête (T-9/T-10) ; interruption imminente
  au milieu d'un chapitre ⇒ sauvegarde `wip/…` (PR draft). La campagne reprendra où
  `_INDEX.md` en est. Jamais de bâclage.

---

_Cette méthode applique les règles du skill `content-ingest` (R-1…R-7), la « Recette » de
`programmes-officiels/README.md` et les études 12/13 ; sa topologie deux dépôts vient de
l'étude 24. En cas de désaccord : **AGENTS.md** (racine du dépôt **moteur**) gagne, puis les
skills et docs normatifs, puis cette méthode._
