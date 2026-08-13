# Étude 27 — Enrichissement par sources web tierces (veille, lien sortant curé, génération inspirée)

> **Statut** : brouillon
> **Priorité** : 27 · **Valeur** : 🌐 le gisement web tunisien (devoirs de contrôle/synthèse, séries, corrigés alignés sur le programme réel) devient exploitable **sans copier une ligne** — et la ligne rouge du plagiat cesse d'être une promesse pour devenir un **gate déterministe** · **Complexité** : moyenne (doctrine + un petit registre ; **zéro moteur pédagogique nouveau**)
> **Architecte** : session Claude Code / 2026-08-13 · **Exécuteur cible** : Sonnet (lots 2 et 4) + opéré (lots 1, 3, 5)
> **Dépend de** : é23 (le patron du lien externe curé — lots 1-4 livrés : allowlist par source, registre versionné, aucune URL libre côté app) · é13 ScribeKit (livrée) · la méthode (§ Profils de source) · **ne dégèle PAS é12** (studio d'ingestion, gelée le 2026-07-20) · **Bloque** : rien
> **Docs normatifs liés** : AGENTS.md, `LICENSE-CONTENT.md`, [`METHODE-GENERATION-CONTENU.md`](../METHODE-GENERATION-CONTENU.md) (§ Profils de source), [`23-videos-explicatives/ETUDE.md`](../23-videos-explicatives/ETUDE.md) (D-2/D-6/D-10, R-2/R-3/R-11), [`12-studio-ingestion/ETUDE.md`](../12-studio-ingestion/ETUDE.md) (R-1/R-2), `.claude/skills/content-ingest/SKILL.md` (R-1…R-7), `docs/xss-rendering-policy.md`

---

## 1. Contexte & objectif produit

### Le besoin

Il existe en Tunisie un écosystème de sites gratuits qui publient, par année du secondaire, des
**devoirs de contrôle et de synthèse, des séries d'exercices par chapitre, des cours et des
corrigés** en PDF — produits par des enseignants, alignés sur ce qui est réellement évalué en
classe. C'est le seul gisement qui dise, sans intermédiaire, **à quel niveau d'exigence un
chapitre tombe vraiment** : le manuel officiel donne le périmètre, le devoir de prof donne le
plafond.

La demande d'origine (« enrichir la plate-forme à partir des liens web ») se heurte à une
ambiguïté qu'il faut lever avant toute ligne de code : **qu'est-ce qu'on prend, exactement, à un
lien ?** Selon la réponse, on est dans du calibrage sans risque ou dans de la contrefaçon. Cette
étude installe la réponse — quatre tiers, dont **un seul** exige une autorisation — et la rend
**vérifiable** plutôt que promise.

### Le trou que ça sert, mesuré sur le dépôt (2026-08-13)

| axe                     | état réel                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| contenu physique-chimie | `physique-1ere-sec` **17 chapitres**, `chimie-1ere-sec` **2** — **rien** en 2ᵉ, 3ᵉ, bac                                |
| fiches programme        | `1ere-sec/sciences-physiques.md` + `1ere-sec/chimie.md` — **aucune fiche physique/chimie au-delà de la 1ᵉ sec**         |
| collège                 | `sciences-physiques-7eme` 6 chapitres, `-8eme` 6 chapitres                                                             |
| liens externes          | `chapter.sources[]` = `z.string().min(3)` — **une citation en texte libre**, non validée, non sondable, jamais affichée |
| registre vidéo (é23)    | `content/videos.json` = `{}` — le patron du lien curé est **construit et jamais utilisé** (lot 5 non lancé)             |
| profils de source       | **quatre** (`ecole-cnp`, `ecole-secondaire`, `document-libre`, `sans-source`) — **aucun pour une source web**           |
| ingestion               | `content-ingest` R-2 **refuse déjà** un document sous droits sans autorisation ; é12 est **gelée**                      |

Autrement dit : la doctrine existante répond déjà « non » à la lecture naïve de la demande
(aspirer un site), et il n'existe aucun chemin outillé pour ce qu'elle autoriserait.

### KPI

- chapitres physique-chimie lycée livrés / mois (le gisement sert à ça, ou il ne sert à rien) ;
- **zéro** énoncé généré détecté en recouvrement verbatim avec une source non autorisée (gate R-8) ;
- taux de rejet en `content-audit` des chapitres calibrés par une source web vs les autres ;
- (si T1) part des chapitres portant ≥1 ressource externe, et `resource_open` par chapitre.

### Non-objectifs (explicites)

Scraping ou aspiration de site · ré-hébergement d'un PDF tiers · `iframe` d'un site tiers ·
recherche plein-texte dans les sites · crawler · dégel de é12 · **faire d'un site tiers une
référence de programme** · partenariat contractuel (T2, lot 6 gelé).

---

## 2. Spécification fonctionnelle

### Acteurs & parcours

- **US-1 (architecte/opérateur)** — je qualifie une source web : j'ouvre le site, je remplis une
  **fiche de qualification** (annexe B) et j'en sors un **verdict de tier** (T0 / T1 / T2′ / T2)
  opposable pour toute session ultérieure.
- **US-2 (architecte)** — depuis la fiche, je produis une **fiche de veille** (typologie des
  évaluations, plafond de difficulté, vocabulaire employé) qui calibre `curriculum-architect` et
  les skills `prof-*`. Aucun fichier de la source n'entre dans le dépôt.
- **US-3 (élève, tier T1 uniquement)** — en fin de cours, une section « Pour aller plus loin »
  propose **au plus 2** liens sortants vers des ressources gratuites, étiquetés « site externe »,
  ouverts dans un nouvel onglet après un interstitiel « tu quittes l'application ».
- **US-4 (auteur/CI)** — quand je génère du contenu calibré par une source non autorisée, un gate
  **échoue** si un énoncé ou une explication recouvre la source en verbatim.

### Règles métier

- **R-1 — Quatre tiers, une seule autorisation.** Ce qu'on prend à un lien est **toujours** l'un
  de ces quatre gestes, et le tier est déclaré avant le premier token dépensé :

  | tier      | ce qu'on prend                                                                            | copie        | autorisation écrite |
  | --------- | ----------------------------------------------------------------------------------------- | ------------ | ------------------- |
  | **T0**    | des **faits** : années servies, typologie DC1/DC2/DS, plafond de difficulté, vocabulaire | aucune       | non                 |
  | **T1**    | **rien** — on pointe (lien sortant curé)                                                  | aucune       | non                 |
  | **T2′**   | la **carte notionnelle et typologique**, puis les `prof-*` écrivent des énoncés neufs     | aucune       | non                 |
  | **T2**    | le **contenu** (énoncés, corrigés) — transcription fidèle                                 | intégrale    | **OUI, bloquante**  |

- **R-2 — La ligne T2′, énoncée une fois pour toutes.** Un **énoncé est une expression protégée,
  une notion ne l'est pas**. « Calculer la résultante de deux forces concourantes » se reprend
  librement ; la phrase de l'auteur, ses valeurs numériques, son contexte narratif et la
  formulation de son corrigé, non. Contexte et nombres sont **réinventés**, jamais transposés.
- **R-3 — Un site tiers n'est JAMAIS une référence de programme.** Extension de R-3 de
  `content-ingest` : le manuel/guide officiel fait foi ; un devoir de prof reflète ce qu'un
  établissement a choisi d'évaluer, pas le périmètre officiel. **Aucune source officielle
  trouvable ⇒ STOP** (profil `ecole-secondaire`), une source web ne comble pas ce STOP.
- **R-4 — L'allowlist autorise un SITE, jamais une URL** (repris tel quel de é23).
- **R-5 — Un lien = une vérification humaine intégrale.** Pendant du visionnage intégral R-3 de
  é23 : ouvrir la ressource, confirmer gratuité réelle (pas de mur après deux clics), adéquation
  au chapitre, complétude (corrigé inclus si annoncé), absence de contenu inapproprié et de
  publicité agressive. Public mineur : pas de délégation, pas d'échantillonnage.
- **R-6 — Lien SORTANT, jamais un embed.** Pas d'`iframe`, pas de PDF réhébergé, pas de hotlink
  vers le fichier : on pointe la **page**, pas le fichier.
  `target="_blank" rel="noopener noreferrer nofollow"` + interstitiel.
- **R-7 — Aucune URL libre ne franchit la frontière contenu→app** (D-10 de é23) : `site` (enum
  fermé) + `path` validé, jamais une URL rédigée à la main dans du contenu.
- **R-8 — L'anti-verbatim est un gate, pas une intention.** Un check **déterministe** compare les
  énoncés/explications générés à la transcription de toute source marquée
  `autorisation: aucune` ; recouvrement ⇒ **échec**. C'est la seule chose qui distingue T2′ de T2
  en pratique.
- **R-9 — Traçabilité.** `chapter.sources[]` cite la source consultée ; la fiche porte URL, date
  de consultation et empreinte du snapshot.
- **R-10 — Le snapshot ne rentre pas dans le dépôt.** Le PDF/HTML consulté vit dans le wrapper
  hors git (D-10), **jamais** sous `content/` ni dans `FableEtudes/` — même en dépôt privé. Un
  corpus tiers dans notre git est exactement ce que `leak:check` protège dans l'autre sens.
- **R-11 — Borne : ≤2 ressources externes par chapitre** (analogue à R-11 de é23), en **fin** de
  cours seulement — jamais dans le flux d'un exercice ni dans un écran d'échec.
- **R-12 — Santé des liens.** Sonde hebdomadaire ; `status: dead` ⇒ retrait. Jamais un 404 servi
  à un élève.
- **R-13 — Robots & CGU.** Un site qui interdit l'accès automatisé se lit **à la main** ou pas du
  tout. Aucun contournement de WAF, jamais (le piège CNP 403 est déjà documenté dans la méthode).
- **R-14 — Réciprocité.** `LICENSE-CONTENT.md` interdit contre notre contenu précisément ce qu'une
  aspiration ferait à celui d'autrui (reproduction, œuvres dérivées, extraction de banques de
  questions, entraînement ML). Toute décision de cette étude qui violerait notre propre licence
  si on l'appliquait à nous est **refusée** — c'est le test à appliquer en cas de doute.

### i18n

Étiquette « site externe » + interstitiel en FR/EN/AR (RTL) ; le titre de la ressource est
affiché dans **sa** langue avec `dir="auto"` (même règle que le titre de vidéo, é23).

### Hors périmètre (v1)

T2 (transcription autorisée) · ingestion automatisée · crawler · partenariat contractuel ·
recherche dans les sites · ressource externe sur un écran de correction (é23 occupe ce moment).

---

## 3. Architecture technique (décisions fermées)

- **D-1 — T0 et T2′ ne touchent PAS le moteur.** Ce sont des gestes de méthode : une fiche, un
  calibrage, des skills existants. Seul **T1** ouvre du code. C'est ce qui rend les lots 1-3
  livrables même si é12 reste gelée.
- **D-2 — Cinquième profil de source : `source-web`.** Ajouté à la table des profils de la
  méthode. Fiche sous
  `programmes-officiels/sources-externes/web-<slug>/fiche.md` (école) ou
  `content/_sources/<theme>/web-<slug>/fiche.md` (hors école) — **même gabarit `_TEMPLATE.md`**,
  en-tête de provenance **étendu** (annexe B : 8 champs, dont `tier` et `autorisation`).
- **D-3 — Registre `content/ressources.json`**, calqué sur `videos.json` :
  `Record<resourceId, entry>`, `resourceId` namespacé `famille.slug`
  (`physique.dc1-forces-1ere-sec`). Entrée :
  `{ site, path, title, lang, kind: "serie"|"devoir"|"cours"|"corrige"|"autre", level, free, checkedAt, checkedBy, status: "active"|"dead"|"retired", notes? }`.
- **D-4 — `chapter.resources[]`** (≤2, ids uniques, résolus dans le registre, `lang` croisé avec
  le `contentLanguage` du sujet par `content:qa`) → compilé en `chapters.resources` JSONB.
- **D-5 — `site` est un enum fermé, pas une URL.** `RESOURCE_SITES` dans `schema.ts` +
  constructeur d'URL par site côté app (le pendant exact de `VIDEO_ID_PATTERNS`). Ajouter un site
  = éditer l'enum = passer par une PR et l'arbitrage Q-1.
- **D-6 — Aucune ouverture de CSP.** Contrairement à é23 (qui a dû ouvrir `frame-src` d'un host),
  un lien sortant ne demande **rien** : pas d'iframe, donc pas d'élargissement de la surface.
  C'est un gain net de sécurité par rapport au patron dont on hérite.
- **D-7 — Gate anti-verbatim déterministe** — ⚠️ _amendé à l'exécution, voir le journal du
  2026-08-13 : livré en `scripts/content/verbatim-checks.ts` (TypeScript) appelé par `content:qa`,
  et non en `.mjs` autonome._ n-grammes de
  mots normalisés (casse, accents, ponctuation, espaces ; notation mathématique et formules
  **exclues** du calcul, sinon toute équation est un faux positif) entre les champs textuels
  générés et les transcriptions déclarées `autorisation: aucune`. Branché dans `content:qa`.
  **Rejeté** : un juge LLM — coût par run, non reproductible, et l'étude « IA → déterministe » a
  déjà tranché ce type d'arbitrage en faveur du script.
- **D-8 — Rejeté : réutiliser `chapter.sources[]` pour porter les liens.** Texte libre
  (`z.string().min(3)`), non validé, non sondable, jamais affiché à l'élève : il reste ce qu'il
  est — une **citation de provenance**, pas un lien.
- **D-9 — Rejeté : un `provider: "web"` dans `videos.json`.** Un document n'est pas une vidéo :
  ni durée, ni extrait (`startSec`/`endSec`), ni `madeForKids`. Mélanger les deux registres
  casserait les invariants de é23.
- **D-10 — Le snapshot vit hors git**, dans le wrapper `YahiaAcademy/sources-web/<slug>/` (même
  statut que `cnp-officiel/`). Seule la **fiche** est versionnée.
- **Observabilité** : événement `resource_open` (pendant de `video_open`) — mesurer avant
  d'élargir, exactement comme é23 le fait pour sa phase B.
- **Sécurité** : R-6/R-7 sont les invariants ; aucune donnée élève ne transite vers le site tiers
  (pas de referrer utile — `rel="noreferrer"`), et l'interstitiel est la frontière assumée.

---

## 4. Plan d'exécution en lots

| lot | contenu (résumé)                                                                                        | fichiers/objets créés                                                                | tests exigés                                                             | dépend de       |
| --- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------------- |
| 1   | **Doctrine** : profil `source-web` (D-2) + les 4 tiers (R-1/R-2) dans la méthode + gabarit de fiche      | amendement `METHODE-GENERATION-CONTENU.md` ; annexe B promue en gabarit               | relecture humaine ; `programme:check` vert                               | —               |
| 2   | **Gate anti-verbatim** (D-7)                                                                            | `scripts/content/verbatim-checks.ts` + branchement `content:qa` (dépôt **moteur**)    | Vitest : cas positifs/négatifs, **0 faux positif sur le corpus existant** | 1               |
| 3   | **Pilote T0+T2′** : qualification de la source d'appel + 1 chapitre 2ᵉ sc. généré, coût mesuré           | `sources-externes/web-<slug>/fiche.md` + 1 chapitre `content/`                        | gates contenu + `content-audit` sur la sortie                            | 1, 2            |
| 4   | **T1 moteur** : registre + `chapter.resources[]` + compilation + UI « Pour aller plus loin »            | `content/ressources.json`, `schema.ts`, `sql-builder.ts`, migration, composant        | Vitest schéma/loader/UI ; pgTAP si colonne ; `content:qa` croisé lang     | 3 + **GO** Q-2  |
| 5   | **T1 campagne** : allowlist validée (Q-1) + curation sur les chapitres pilotes + sonde de santé (R-12)   | entrées de registre + `scripts/content/check-resources.mjs`                            | sonde verte ; `content:check`                                            | 4               |
| 6   | **T2 (GELÉ)** : partenariat + transcription autorisée                                                   | —                                                                                    | —                                                                        | Q-3 + écrit signé |

- [x] Lot 1 — doctrine (profil + tiers + gabarit) — méthode + `content-ingest` R-2, 2026-08-13
- [x] Lot 2 — gate anti-verbatim — moteur [arena#722](https://github.com/MBeji/yahia-quest-arena/pull/722), mergé le 2026-08-13
- [ ] Lot 3 — pilote T0+T2′ mesuré
- [ ] Lot 4 — T1 moteur (GO humain)
- [ ] Lot 5 — T1 campagne
- [ ] Lot 6 — gelé

**Stop-points.** R-8 est absolu (pas de génération calibrée sans le gate du lot 2 en place). Le
lot 4 ne démarre pas sans l'arbitrage Q-2 — envoyer un élève hors de l'app est une décision
produit, pas technique. Le lot 6 ne démarre **jamais** sans autorisation écrite en main ; en cas
de doute sur les droits, STOP (R-2 de `content-ingest`). Les lots 1, 3, 5 sont opérés/architecte
(doctrine et contenu) ; l'exécuteur Sonnet ne prend que 2 et 4.

---

## 5. Stratégie de test

- **Lot 2** — Vitest sur le script : deux textes identiques ⇒ détecté ; paraphrase lointaine ⇒ non
  détecté ; énoncé contenant la même formule mais un contexte différent ⇒ **non** détecté (le
  faux positif à ne pas produire) ; **plus un test qui lance le vrai `content:qa --strict`** sur un
  corpus jouet — la logique prouve qu'on détecte, seul le câblage prouve que le gate est branché
  dessus. La non-régression du corpus réel (aucun drapeau sur les chapitres existants) se mesure
  dans la **Content CI privée**, pas dans le moteur : le corpus n'y est pas, et avec zéro fiche
  surveillée le contrôle y est un no-op.
- **Lot 4** — Vitest : schéma (`resourceId` mal formé, `site` hors enum, 3 ressources, ids
  dupliqués, `lang` divergente) ; loader ; `sql-builder` (JSONB émis) ; composant (état vide,
  interstitiel, `rel`/`target`, RTL). pgTAP si une colonne est ajoutée (grants explicites —
  piège documenté d'AGENTS.md). `smoke:shell` si le bundle public est touché.
- **Lot 5** — la sonde `check-resources.mjs` en CI hebdo (patron `check-videos.mjs`).
- **Ce qui prouve la non-régression** : `content:check` + `content:qa:strict` +
  `content:audit:strict` + `programme:check` restent verts à chaque lot ; le corpus existant ne
  bouge pas au lot 2.

---

## 6. Risques & mitigations

- **RISK-1 — Plagiat involontaire en T2′** (probable / **critique**) → R-8 (gate déterministe,
  lot 2 **avant** le lot 3) + R-10 (le snapshot n'entre pas dans le contexte de génération
  autrement que par la fiche, qui est déjà une reformulation).
- **RISK-2 — Le contenu change sous le lien** (probable / moyen) → R-12 sonde + `status` +
  `checkedAt` daté dans le registre.
- **RISK-3 — L'élève quitte l'app** (certain / faible) → R-11 (≤2, fin de cours seulement) +
  mesure `resource_open` avant tout élargissement.
- **RISK-4 — Glissement : le site devient une référence de programme** (possible / majeur) → R-3
  + le verdict de tier écrit dans la fiche, opposable en revue.
- **RISK-5 — Contenu inapproprié ou pub agressive derrière un lien** (possible / majeur, public
  mineur) → R-5 (vérification intégrale, aucune délégation) + R-4 (allowlist par site).
- **RISK-6 — Un auteur se reconnaît dans un énoncé** (possible / majeur, réputationnel) → R-2 +
  R-9 (traçabilité : on sait quoi a été consulté, quand) + procédure de retrait sous 48 h à la
  première demande, sans discuter le fond.
- **RISK-7 — Accès réseau** (**constaté** le 2026-08-13 / opérationnel) → l'egress d'une session
  cloud **bloque** ces domaines (`EGRESS_BLOCKED`). La qualification et la lecture se font depuis
  le poste Windows, ou en autorisant le domaine dans la politique réseau de l'environnement ;
  **jamais** en contournant le proxy (R-13).

---

## 7. Questions ouvertes (pour l'humain)

- **Q-1 — Allowlist des sites** (annexe A) : lesquels sont autorisés ? L'annexe A est une liste
  **à qualifier**, pas une allowlist — aucun site n'y a été inspecté (RISK-7).
- **Q-2 — GO du tier T1** (lot 4) : accepte-t-on d'envoyer un élève hors de l'app en phase bêta ?
  Recommandation de l'architecte : **oui, mais après la rentrée** — le lot 4 est du code sur le
  chemin critique d'un jalon à ~J-19, pour un gain qui n'est pas du contenu.
- **Q-3 — Écrit-on aux sites** pour une autorisation T2 ? Lesquels, et contre quoi (crédit
  nominatif, lien retour, co-branding) ? Sans réponse, le lot 6 reste gelé — ce qui est un état
  parfaitement tenable.
- **Q-4 — Seuil du gate anti-verbatim** : n-grammes de 8 mots ou de 10 ? À trancher **après** le
  lot 2, sur les faux positifs mesurés du corpus réel, pas à l'avance.
- **Q-5 — Position dans le gel.** é12 est gelée par la doctrine verticale. Cette étude
  n'ouvre aucun canal d'ingestion (lots 1-3 = doctrine + un script + un chapitre), donc
  l'architecte recommande de **dégeler les lots 1-3 seulement** et de laisser 4-6 derrière Q-2/Q-3.
  Sa place dans la ROADMAP découle de cet arbitrage — elle n'y a **pas** été inscrite d'office.

---

## 8. Journal d'exécution

- **2026-08-13 — Étude ouverte.** Née d'une question (« comment enrichir la plate-forme à partir
  des liens web ? », premier exemple `devoirphysiquechimie.tn`). Trois constats l'ont façonnée :
  (1) **la doctrine existante répondait déjà « non »** à la lecture naïve (R-2 de
  `content-ingest`, profil `document-libre` : « autorisation écrite […] sinon refus »), et
  `LICENSE-CONTENT.md` interdit contre nous exactement ce geste — d'où R-14 ;
  (2) **le patron du lien externe curé existe déjà**, construit par é23 pour la vidéo et **jamais
  utilisé** (`content/videos.json` = `{}`) : T1 est une transposition, pas une invention — et une
  transposition **moins risquée** que l'originale, puisqu'elle n'ouvre pas la CSP (D-6) ;
  (3) **la source d'appel n'a pas pu être inspectée** — `devoirphysiquechimie.tn` est bloqué par
  l'egress de la session (`EGRESS_BLOCKED`), et l'index de recherche disponible ne le remonte pas.
  L'annexe A est donc une liste à qualifier et non une allowlist ; c'est aussi ce qui a produit
  RISK-7, qui vaut pour toute campagne future de sources web depuis une session cloud.

- **2026-08-13 — Lot 2 écrit et vert, en attente de Q-5** : moteur
  [arena#722](https://github.com/MBeji/yahia-quest-arena/pull/722), **volontairement en draft** —
  le push l'avait ouverte ready avec l'auto-merge armé, or c'est Q-5 qui dit si ce lot sort du gel.
  Trois notes qui appartiennent à l'étude, pas seulement à la PR :

  - **Écart sur D-7, assumé et non silencieux** : livré en `scripts/content/verbatim-checks.ts`
    (TypeScript, à côté de `qa-checks.ts`) appelé par `content:qa`, et non en `check-verbatim.mjs`
    autonome. Deux motifs : un `.mjs` sans types ne s'importe dans `qa.ts` qu'au prix d'un
    `@ts-expect-error` en code de production (DoD §2 le proscrit), et le corpus a **déjà** une
    porte — lui en ajouter une seconde à armer séparément est la meilleure façon de n'en armer
    aucune. La règle d'exécution n° 3 demande de remonter l'écart plutôt que de re-designer en
    silence : c'est cette entrée.
  - **Un piège de câblage qui aurait désarmé un tiers du contrôle** : les options de question sont
    des objets `{ id, text }`. Le premier branchement les épandait telles quelles et produisait
    `[object Object]` — aucun type levé, aucun test rouge, et les options hors surveillance sans
    que rien ne le dise. D'où `questionTextSurface`, fonction à part et testée. À retenir pour le
    lot 4, qui touchera les mêmes structures.
  - **Ce que le lot ne prouve pas** : l'absence de faux positif sur le corpus réel. Le seuil
    (Q-4) reste donc ouvert de droit **et** de fait — la première mesure viendra de la Content CI
    privée le jour où une fiche existe.

- **2026-08-13 — Lot 1 livré : la doctrine quitte l'étude pour la méthode.** Le profil
  `source-web` est le **cinquième** de `METHODE-GENERATION-CONTENU.md` (table + section dédiée :
  les quatre tiers, la ligne T2′, les cinq règles, le gabarit d'en-tête en 8 champs), R-2 du socle
  y renvoie, et `content-ingest` R-2 porte la règle sous la forme qui l'intéresse : **il n'est
  appelé que pour T2, donc sans autorisation en main il ne transcrit pas** — il produit une fiche
  de veille et passe la main. Deux choix de rédaction valent d'être notés :

  - **Les deux pièges d'un T2 sont écrits là où on les rencontre**, pas seulement ici : un site
    qui ré-héberge des PDF tiers n'a pas les droits à céder (plafond T2′ même s'il signe), et
    l'accès n'est pas acquis (egress bloqué en session cloud). Une méthode qui tait ses
    impasses les fait redécouvrir une campagne sur deux.
  - **La méthode annonce que le gate vérifie**, et ne se contente pas d'interdire. La phrase
    « ce n'est pas une consigne d'honneur » est là exprès : un agent qui sait que `content:qa`
    mesure le recouvrement ne tente pas la paraphrase minimale.

  Restent ouverts : Q-1 (allowlist), Q-2 (GO du T1, lot 4), Q-3 (courrier aux sites), Q-4 (seuil,
  mesurable seulement quand une fiche existera). Le lot 3 (pilote T0+T2′) est débloqué.

---

## Annexe A — Sites de l'écosystème à qualifier (⚠️ **PAS une allowlist**)

Aucun de ces sites n'a été inspecté (RISK-7) : ce tableau liste ce qu'il faut aller vérifier,
site par site, avant tout usage. Le tier proposé est une **hypothèse** de départ.

| site                                                   | ce qui est annoncé                                                  | à vérifier avant tout usage                                                     | tier hypothèse |
| ------------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------- |
| `devoirphysiquechimie.tn` (**la source d'appel**)      | physique-chimie, devoirs/séries/corrigés                            | titulaire, CGU, `robots.txt`, gratuité réelle, PDF d'auteurs tiers réhébergés ? | T0 → T2′       |
| `devoirat.net`                                         | devoirs, séries, cours physique-chimie 1ᵉ-3ᵉ sec, par trimestre     | idem + ancienneté/stabilité des URL                                             | T0 → T2′       |
| `devoir.tn`                                            | cours et devoirs, secondaire et primaire, toutes matières           | idem + frontière gratuit/payant (déjà notée à surveiller par é23 pour la vidéo)  | T0 → T2′       |
| `mathinfo.tn`                                          | physique 1ᵉ/2ᵉ/3ᵉ sciences, devoirs et séries corrigés PDF          | idem                                                                            | T0 → T2′       |

**Le point de vigilance qui décide de tout** : si un site **ré-héberge des PDF d'enseignants
tiers** — cas très fréquent dans cet écosystème — alors **il n'a pas les droits à céder**, et
aucune autorisation qu'il donnerait ne vaudrait pour T2. Le tier plafonne alors à T2′, quelle que
soit la bonne volonté de l'exploitant.

## Annexe B — Gabarit d'en-tête de fiche `source-web` (8 champs, tous obligatoires)

```yaml
# en-tête de provenance — profil source-web (étude 27, D-2)
url: https://<domaine>/<chemin>        # la PAGE consultée, jamais le fichier
titulaire: <personne morale ou physique identifiée, ou "inconnu">
consulte_le: 2026-08-13                # date de consultation (le web bouge)
cgu: <URL des CGU/mentions légales, ou "absentes">
robots: <"autorise" | "interdit" | "absent">   # R-13
autorisation: <"aucune" | "demandee le JJ/MM" | "accordee le JJ/MM par <qui>">
tier: <"T0" | "T1" | "T2-prime" | "T2">        # R-1 — opposable
snapshot: YahiaAcademy/sources-web/<slug>/     # hors git (R-10) + empreinte
```

Un champ manquant ⇒ la fiche n'est pas exploitable, la session s'arrête (même sévérité que la
checklist droits du profil `document-libre`).

## Annexe C — Ce qu'un lien web ne donnera jamais

À garder sous les yeux quand la tentation d'élargir revient : un site tiers ne donne **ni le
périmètre officiel** (R-3 — c'est le manuel), **ni la clé de réponse vérifiée** (nos corrigés sont
re-résolus par `content-audit`, un corrigé tiers n'est pas une preuve), **ni la calibration
d'âge** (un devoir de prof n'est pas calibré pour un élève seul devant un écran), **ni les
misconceptions** (`distractor_tags` viennent de notre taxonomie). Le gisement est **le plafond
d'exigence réel** — précieux, et strictement borné à ça.
