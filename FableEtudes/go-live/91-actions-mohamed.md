# 91 — Actions Mohamed (consolidé)

> ⛔ **Figé le 2026-09-23.** La liste vivante du reste-à-faire est la feuille de route de
> [`STATUS.md` §6](https://github.com/MBeji/yahia-quest-arena/blob/main/STATUS.md) (§6.2 : ce qui
> attend le propriétaire). Ce fichier reste comme trace datée du programme go-live.

> Liste unique des actions **côté Mohamed** sur tout le programme go-live, par priorité.
> Légende : 🟦 action 100 % toi · 🟨 toi → tu me donnes X → je code · ⏳ pas urgent.
> Mise à jour : 2026-06-13 · revue 2026-07-11 (pivot gratuité : section C gelée ; E2 automatisé) ·
> **revue 2026-07-27** : A2/A3/A4/A5/B1/B4 soldés, A10/A11 ajoutés. Source : chantiers C4-C7 +
> [Go/No-Go 2 portes](./livrables/07-gouvernance/02-roadmap-pilotage-gonogo.md).
>
> ⚠️ **Méthode, apprise à ses dépens le 2026-07-27** : trois lignes de ce fichier annonçaient
> « à faire » des actions faites depuis des semaines (domaine câblé, DSN Sentry posé, Search
> Console vérifiée). Une action réalisée **hors du repo n'y laisse aucune trace** — donc avant
> de la déclarer en attente, on la **sonde** (`nslookup` pour le DNS, le bundle prod pour une
> variable `VITE_*`, l'API GitHub pour un secret ou un ruleset). Ce qui reste insondable se
> rapporte « **non vérifiable d'ici** », jamais « pas fait ».

---

## ✅ 0. Migration prod `na9ranal3ab.vercel.app` — FAIT & vérifié (14/06)

| # | Action | État |
|---|---|---|
| 0A | Redirect URLs Supabase Auth (wildcard `/**`) | ✅ posé & vérifié (dashboard) |
| 0B | Cron de l'ancien `xpscholars-app` désactivé | ✅ confirmé (API) |
| 0C | Site URL Supabase = `na9ranal3ab.vercel.app` | ✅ posé |

> Rien à faire ici. Reste seulement : **acheter `na9ranal3ab.tn`** (section B) — d'autant que la
> nouvelle URL `*.vercel.app` déclenche un **faux positif de l'extension WOT** (Google Safe Browsing
> est clean) → le **domaine `.tn` (réputation propre) est la vraie correction**, à faire **avant**
> toute pub aux parents.

---

## 🚪 A. Chemin critique « Porte 1 » — ouvrir la beta (cible : rentrée sept 2026)

| # | Action | Type | Temps | Débloque |
|---|---|---|---|---|
| ~~A1~~ | ✅ **FAIT (14/06)** — monitor UptimeRobot UP sur `https://na9ranal3ab.vercel.app` (5 min) + alerte e-mail branchée (`mohamed.beji@sofrecom.com`). Vérifié via API. | ✅ | — | A6 ✅ |
| ~~A2~~ | ✅ **FAIT** — `VITE_SENTRY_DSN` posée en env Vercel. **Vérifié le 2026-07-27** autrement que sur parole : le DSN (`ingest.de.sentry.io`) est inliné dans le bundle prod. | ✅ | — | A7 ✅ |
| ~~A3~~ | ✅ **FAIT (2026-07-27)** — projet **PostHog EU `233369`** créé, clé fournie, intégration mergée (**PR #639**) : envoi maison sans SDK (budget bundle), en **complément de GA4** qui existait déjà (`G-H0JRQ7192V`). Ni autocapture ni **session replay** (décision protection des données, public mineur), aucune PII. Reste éventuellement à filtrer `traffic_type = production` dans les insights. | ✅ | — | analytics |
| ~~A4~~ | ✅ **FAIT (2026-07-27)** — checklist auth hardening déroulée. **Vérifié** : `mailer_autoconfirm=false` (les confirmations d'e-mail étaient **désactivées**, elles ne le sont plus). **Bouton Google : rien à trancher** — la sonde `/auth/v1/settings` montre le provider **configuré et actif** (`google: true`). | ✅ | — | A8/A9/B2 |
| ~~A5~~ | ✅ **FAIT** — ruleset **`main-protection` actif** (vérifié via l'API GitHub le 2026-07-27). | ✅ | — | protection prod |
| A6 | **Vercel** : activer Analytics + previews par PR (gratuit) | 🟦 | 2 min | B4/B5 |
| **A10** | **Secrets du kill-switch** ✅ posés le 2026-07-27 (`VERCEL_TOKEN`/`VERCEL_PROJECT_ID`/`VERCEL_ORG_ID`) — `rollback-prod.yml` était **inopérant** depuis son écriture. ⚠️ **Reste le test à blanc** (`freeze-only` puis `unfreeze`) : un kill-switch jamais déclenché reste une promesse. Faisable par l'agent depuis la PR #640. | 🟨 | 5 min | incident prod |
| **A11** | **Coller les 3 gabarits d'e-mail en français** (confirmation, mot de passe oublié, changement d'adresse) dans Supabase → Authentication → Email Templates. Rédigés le 2026-07-27, prêts à coller. Aujourd'hui les e-mails partent **en anglais** — c'est le premier contact du produit avec un parent. | 🟦 | 10 min | qualité perçue |

> **Porte 1 infra : GO** au 2026-07-27 (monitoring, ruleset, domaine, auth, SMTP). Ce qui bloque
> encore la Porte 1 n'est plus technique : ce sont les **pages légales** et la **conformité
> mineurs/INPDP** (section C4 ci-dessous).

---

## 🏷️ B. Marque & domaine (à amorcer vite — la dispo peut partir)

| # | Action | Type | Temps |
|---|---|---|---|
| ~~B1~~ | ✅ **FAIT** — `www.na9ranal3ab.tn` sert l'app en **200**, l'apex redirige en 308. La propriété **Search Console était déjà vérifiée** (TXT `google-site-verification` sur l'apex) et le sitemap répond 200 à Googlebot. ⚠️ La zone DNS est chez **TuNet**, pas chez Vercel : tout enregistrement se pose dans l'espace client du registrar. Variantes `.com`/typos : à décider. | ✅ | — |
| B2 | **Réserver les pseudos `@na9ranal3ab`** : Facebook · Instagram · TikTok | 🟦 | 15 min |
| B3 | **Check marque INNORPI** (pas de conflit) + recherche Google/FB | 🟦 | 20 min |
| ~~B4~~ | ✅ **FAIT (2026-07-27)** — [checklist domaine/SMTP](./livrables/04-architecture-prod/checklist-domaine-smtp.md) déroulée : **Resend** sur le **sous-domaine d'envoi `send.na9ranal3ab.tn`** (Irlande/eu-west-1), DKIM + SPF + MX de return-path posés chez TuNet et **vérifiés au DNS**, MX Ooredoo de la racine intacts, SMTP branché sur Supabase Auth (`smtp.resend.com:465`), chaîne **prouvée de bout en bout**. Reste A11 (gabarits FR) et, plus tard, une adresse de contact `contact@`. | ✅ | — |

---

## 💳 C. Avant le lancement PAYANT « Porte 2 » — ⏸️ **GELÉ (2026-07-11)**

> Pivot « gratuité de phase » (C8 2026-06-21 + étude 15 Q-2 2026-07-10) : **aucune monétisation**
> en phase actuelle. C1/C2/C3/C5 ne redeviendront pertinents qu'au **dégel de l'étude 01**
> (paiement en ligne) — décision humaine. ⚠️ **C4 (conformité mineurs / INPDP) reste ACTIF**
> ci-dessous : c'est un prérequis légal du lancement **gratuit** aussi.

| # | Action | Type |
|---|---|---|
| ~~C1~~ | ⏸️ Ouvrir le statut auto-entrepreneur (prérequis pour encaisser) — **au dégel étude 01** | 🟦 |
| ~~C2~~ | ⏸️ Tester 2-3 points de prix → figer la grille — **au dégel étude 01** | 🟦 |
| ~~C3~~ | ⏸️ `close-premium.sql` avant toute vente — **au dégel étude 01** (note : depuis la migration `20260711100000`, tout est `is_premium=false` ; la réactivation est l'UPDATE inverse documenté dans la migration) | 🟨 |
| **C4** | **ACTIF — Conformité mineurs / INPDP** : décisions (consentement parental, registre des traitements) — GAP-003. Prérequis du lancement même gratuit | 🟦 + conseil |
| ~~C5~~ | ⏸️ Sortie Vercel Hobby « à la 1ʳᵉ vente » — re-déclencheur à définir hors ventes (ToS Hobby : usage commercial) | 🟦 |

---

## 📣 D. Marketing / lancement — 🔴 **CHEMIN CRITIQUE RENTRÉE** (requalifié le 2026-08-13, étude 28 lot 1)

> **Ce bloc n'est plus « marketing », c'est le goulot du projet.** Les trois actions sont
> ouvertes depuis le 2026-06-13, donc **aucun canal d'acquisition n'est actif** — le produit est
> prêt à recevoir des élèves qu'aucun mécanisme ne lui envoie. Le reste du programme (infra,
> monitoring, domaine, SEO, analytics) est vert : ce bloc-ci est ce qui sépare une mise en ligne
> d'un lancement, et il est devenu une **condition de la Porte 1** ([master plan](./00-MASTER-PLAN.md) §3bis/§6).
>
> ⏳ **La fenêtre est étroite** : rentrée le 1ᵉʳ septembre, soit **J-19 au 2026-08-13**. La
> suivante est le pic de révisions de **janvier-mars**. Rien ici ne demande de code.

| # | Action | Type | Temps | Note |
|---|---|---|---|---|
| **D1** | Créer la **page Facebook** « Na9ra Nal3ab » + **WhatsApp Business** | 🟦 | ~1 h | Le canal parent n° 1 en Tunisie. Rien ne le bloque — ni code, ni décision, ni budget. À faire en premier : c'est le seul des trois qui ne dépend de personne d'autre |
| **D2** | **Pitcher l'école pilote** (la tienne) avec le [playbook](./livrables/05-marketing/02-plan-acquisition.md) | 🟦 | — | Canal **CAC ≈ 0** : un enseignant qui donne un chapitre en devoir apporte 30 élèves **et** 30 parents, avec une légitimité que la publicité n'achète pas (é28 M-3). ⛔ **PRÉCONDITION DURE (é28 D-5) : ne rien engager avant `GAP-024` livré** (suppression de compte + export/portabilité — **absents de `src/`**) **et `GAP-003` tranché**. Démarcher un établissement sans chemin de suppression des données d'un mineur est une faute, pas un raccourci — et c'est la première question d'un directeur |
| **D3** | Recruter les **premiers beta-testeurs** (réseau perso) | 🟦 | — | 20-30 suffisent. Leur vraie valeur n'est pas le volume mais **la première mesure de rétention S(N)→S(N+1)** — le KPI-4 de é26, défini le 2026-07-19 et **jamais publié depuis**. Sans lui, « référence » reste une opinion |

---

## 🔁 E. Récurrent / exploitation

| # | Action | Cadence |
|---|---|---|
| E1 | **Drill backup** (`gh workflow run db-backup.yml -f target=prod -f drill=true`) | mensuel |
| E2 | ✅ **Automatisé** — `db-migrate-prod.yml` applique les migrations au merge (backup + garde + réconciliation horaire). **Ne plus rien appliquer à la main** (DoD §7) | — |
| E3 | Support (WhatsApp/Messenger) + triage `content_reports` | hebdo léger |

---

## ⌛ Ce qui est de MON côté (rappel, pas tes actions)
Lots code en attente de tes clés/feu vert : **Sentry + PostHog** (après A2/A3) · **pages légales** CGU/confidentialité (je drafte, tu valides) · **CSP nonce ✅ déjà fait** · migration **Nitro** + tag `v1.0.0` (avant palier 1).
