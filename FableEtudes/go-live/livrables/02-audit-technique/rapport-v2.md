# Rapport d'audit technique v2 — yahia-quest-arena

> Chantier [02 — Audit technique & architecture](../../02-audit-technique-architecture.md).
> Construit en 3 sessions : **S1** (réconciliation + revue statique, 2026-06-11 — ce document §1–4),
> **S2** (perf/charge/résilience — §5–6, à venir), **S3** (radar + synthèse — §7–8, à venir).
> Référentiel comparatif : audits du 2026-06-01 (run de référence : RUN2, commit `21a5042`) —
> voir [reconciliation-2026-06-01.md](./reconciliation-2026-06-01.md).

## 1. Contexte & méthode

- Périmètre : repo `yahia-quest-arena` (`main`), 2026-06-11 — état post-C1/C3 (intégrité scoring,
  i18n FR-first, récompenses, leaderboard parcours).
- La réconciliation montre que **15/29 constats du 01/06 sont soldés** (lint, CI, couverture 93 %
  scopée, DOMPurify, e2e, authz) : ce rapport v2 ne re-traite pas ces points, il évalue l'état
  **actuel** et le reste-à-faire.
- Outils S1 : scan de frontières (imports), `git cherry`/`--merged` (branches), `npm outdated` /
  `npm run audit:deps` (supply chain), lecture du pipeline de build/deploy.

## 2. Photographie du système (2026-06-11)

| Axe | Mesure |
|---|---|
| Code | ~170 fichiers de prod sous `src/` ; 10 features isolées + `shared/` + `lib/` |
| Server functions | **39** `createServerFn` répartis dans **10 modules** `*.server.ts` |
| Logique SQL | **47 fonctions** distinctes définies dans l'historique de migrations (certaines retirées depuis, ex. RPCs `subscription_*` supprimées le 09/06) ; RPCs privilégiées `SECURITY DEFINER` + `REVOKE` |
| Routes | 21 fichiers (15 sous `_authenticated/`) |
| Tests | Vitest ≈93 % stmts (scope possédé, seuils 80 %) ; Playwright public+authed ; pgTAP (5 suites) |
| CI | 6 workflows (gate complet + e2e + DB + nightly + migration-gate) |
| Bundle | index 399,76 kB < 450 ; i18n 59,2 kB < 80 ; budgets par chunk en CI |
| Vulnérabilités | `npm audit` (prod, high) : **0** |

## 3. Architecture — revue statique (S1)

### 3.1 Frontières : discipline excellente (vérifiée outil en main)

Scan exhaustif des imports sous `src/` :

- **0** import cross-feature (`features/X` → `features/Y`) — la règle CLAUDE.md est réellement tenue.
- **0** inversion de couche (`shared/`/`lib/` → `features/`).
- **0** import direct de module `*.server.ts` côté client — tout passe par `useServerFn()` + barrels.
- `any` réel : **1 occurrence** hors fichiers générés (`shared/content/schema.ts`).
- Dette commentée : **3 TODO**, tous trackés sur des reviews (#6 nonce CSP, #8 cookie locale, #18 vue
  `subject_stats`, #32 soldé par GAP-010) — zéro FIXME/HACK.

### 3.2 Points de vigilance structurels

1. **Routes monolithiques (F05, restant)** — `quest.$exerciseId.tsx` 819 L, `dashboard.tsx` 793 L,
   `dungeon.tsx` 640 L (brut). La logique serveur en est déjà extraite ; c'est l'UI/orchestration
   React qui grossit. Gate `max-lines: 750` (hors blancs/commentaires) = filet anti-aggravation,
   mais une extraction en composants/hooks par écran reste la vraie correction. → backlog S3.
2. **Pipeline de build custom = le vrai SPOF logiciel.** La prod est construite par
   `scripts/build-vercel.mjs` : build Vite **cible Cloudflare Workers** (plugin du méta-package
   `@lovable.dev/vite-tanstack-config`), puis re-packagé à la main au format Vercel Build Output v3
   avec un **adaptateur Worker→Node écrit maison** (~100 lignes : bridge Request/Response,
   `nodejs22.x`, `maxDuration: 30`). Fonctionne, mais : non supporté upstream, sensible aux
   majeures (Vite 8, lovable 2.x), et il duplique la responsabilité de déploiement entre deux
   mondes (wrangler + Vercel). **Décision documentée (S1) : on garde tel quel jusqu'à C4** —
   c'est le chantier d'archi prod (C4) qui tranchera (préset Vercel natif vs Cloudflare natif). Voir §4.3.
3. **Mono-région assumée** : fonction SSR épinglée `arn1` (Stockholm) pour co-localisation avec
   Supabase (eu-north-1) — bon choix latence DB, mais plan Hobby = pas de multi-région, et les
   élèves tunisiens paient l'aller-retour TN↔Suède sur chaque navigation SSR. À mesurer en S2
   (TTFB réel) et dimensionner en C4.
4. **Supabase = SPOF de données** (une instance, pas de réplica) — standard à ce stade ; le
   comportement en panne est au programme de S2 (résilience).
5. **Headers de sécurité** posés au routing Vercel (HSTS, XFO, CSP…) mais CSP `script-src
   'unsafe-inline'` (TODO #6 : nonce impossible en headers statiques, à injecter depuis
   `src/server.ts`) — porté par GAP-022/C4.

### 3.3 Délta vs ARCHITECTURE.md

Rien de contradictoire détecté en S1 : le document reflète la réalité (features, middleware auth,
RPC SQL, content pipeline). Les ajouts récents (parcours premium, i18n chunk, RPC
`start_exercise_session`) y figurent ou sont cohérents avec lui.

## 4. Dépendances & supply chain (S1)

### 4.1 État

- `npm run audit:deps` (prod, `--audit-level=high`) : **0 vulnérabilité** (local + CI).
- `npm outdated` : ~40 retards **mineurs/patch** (vague Radix, supabase-js, TanStack, react 19.2.7,
  prettier, vitest…) + ~12 **majeures** disponibles.
- Cadence : dependabot actif + `docs/dependency-maintenance.md` (F14 ✅).

### 4.2 Triage des 6 PRs dependabot (décision D2 — appliquer hors chantier)

| PR | Actuel → cible | Recommandation | Motif |
|---|---|---|---|
| `@types/node` 25.9.1 | 22.19.19 → 25 | **Rejeter (fermer la PR)** | Le runtime prod est `nodejs22.x` (`.vc-config.json`) — les types doivent suivre le runtime, pas l'inverse. Rester en 22.x. |
| `vite` 8.0.16 | 7.3.3 → 8 | **Différer — lot dédié « Vite 8 »** | Majeure d'infra build ; doit attendre la compat du méta-plugin lovable + `@cloudflare/vite-plugin` + TanStack Start. Le patch 7.3.5 (mineur) couvre l'intérim. |
| `@vitejs/plugin-react` 6.0.2 | 5.2.0 → 6 | **Différer — même lot que Vite 8** | Couplé à la majeure Vite. |
| `zod` 4.4.3 | 3.25.76 → 4 | **Différer — lot dédié « Zod 4 »** | API d'erreurs remaniée ; zod valide *toutes* les server fns + le schéma contenu. Migration mécanique mais à tester en bloc. |
| `recharts` 3.8.1 | 2.15.4 → 3 | **Différer — lot dédié** | Consommé via le wrapper shadcn `chart.tsx` (écrit pour recharts 2) + radar du suivi parental. |
| `@lovable.dev/vite-tanstack-config` 2.2.0 | 1.7.0 → 2.2 | **Fermer la PR (cible obsolète : 2.4.0 existe) + étudier 2.4 en C4** | C'est le méta-plugin qui possède tout le scaffold build ; une 2.x peut changer le pipeline de déploiement — à instruire avec la décision d'infra C4 (peut potentiellement remplacer `build-vercel.mjs`). |

### 4.3 Décision « vestige Cloudflare » (S1)

`wrangler.jsonc` + le plugin Cloudflare **ne sont pas un vestige** : le build de prod EST un build
Worker, adapté ensuite à Vercel (§3.2). Les retirer aujourd'hui casserait le déploiement.
**Décision : garder, documenté ici ; la simplification (préset natif d'un seul fournisseur) est un
livrable C4**, idéalement combinée à l'étude lovable-config 2.4.

### 4.4 Majeures hors PRs (à planifier, aucune urgence sécurité)

- Lot « ESLint 10 » : `eslint` + `@eslint/js` 10, `globals` 17, `eslint-plugin-react-hooks` 7,
  `react-refresh` 0.5 — tooling pur, à faire groupé.
- `typescript` 6.0.3 : attendre le support officiel `typescript-eslint`.
- `lucide-react` 1.x, `react-day-picker` 10, `three` 0.184 : majeures UI isolées, lots opportunistes.

### 4.5 Minors sûrs (fin de C2, après S2)

En fin de chantier : `npm update` (respecte les ranges semver → colonne *Wanted* : Radix, supabase-js
2.108, TanStack patches, react 19.2.7, dompurify 3.4.9, vite 7.3.5, vitest 4.1.8…) puis gate complet
`ci:verify` + e2e smoke. Un commit unique « chore(deps): minors wave ».

## 5. Performance & charge (S2 — fait le 2026-06-12)

Détail complet + reproduction : [charge/charge-resultats.md](./charge/charge-resultats.md). k6 v2.0.0
**contre TEST uniquement**, 2 scénarios (browse = dashboard 4 lectures // + leaderboard ; quest =
start → lecture ≥4 s/q → submit).

> **🔴 Découverte majeure : un P0 prod.** Le 1er appel réel à `start_exercise_session` a révélé
> que la RPC échoue à chaque appel (`42702 started_at ambiguous`) → **démarrage de quête cassé en
> prod** depuis le 10/06. Cf. GAP-026 + §8. Campagnes lancées après correctif sur TEST.

**Campagne `target` (validation D1 — navigation → 100 VU, quêtes ~540/h)** : cibles tenues avec
~9–17× de marge, **0 échec / 25 977 requêtes**, 100 % des checks.

| Opération | p95 mesuré | seuil D1 |
|---|---|---|
| submit (écriture) | **114 ms** | < 1 000 ms ✅ |
| dashboard (4 lectures //) | **116 ms** | < 2 000 ms ✅ |
| leaderboard | **100 ms** | < 2 000 ms ✅ |

**Campagne `stress` (×5 le débit d'écriture ≈ 2 500/h, 100 VU constants)** : **0 échec / 22 439
requêtes** ; submit p95 → 1,89 s (lectures encore < 200 ms). **Dégradation par la latence, pas par
l'erreur.** Le plafond « p95 submit < 1 s » est entre 1× et 5× ; la tête de distribution (p99 4–5 s)
pointe une **saturation ponctuelle du pool Supabase** sous rafale → 1er levier de dimensionnement C4
(pool PgBouncer / plan Supabase / cold starts Vercel). Reste non couvert en S2 (→ C4) : Lighthouse/
Web Vitals & TTFB réel depuis la Tunisie (mono-région `arn1`, §3.2.3) — mesure terrain à faire sur le
domaine de prod.

## 6. Résilience (S2 — fait le 2026-06-12)

Sondes de chemins d'erreur sur TEST — comportement conforme et fail-closed :

| Sonde | Résultat |
|---|---|
| JWT invalide/expiré | `401 — JWT cryptographic operation failed` (rejet fail-closed) |
| `start_exercise_session(null)` | `400 — Exercise not found` (RAISE gracieux) |
| `submit` sur session forgée | `400 — Invalid quest session.` (contrôle de propriété) |
| Anti-rush : submit instantané | `tooFast=true, xpEarned=0` (gate appliqué même hors UI) |

Aucune fuite de 5xx sur 48 000+ requêtes cumulées (3 campagnes). Les server fns enveloppent les
erreurs RPC (mapping de tokens `PARCOURS_LOCKED`/`QUIZ_LOCKED`…) et `src/server.ts` normalise les 500
catastrophiques h3 en page d'erreur de marque. **Non testé en S2** (candidat backlog) : panne
Supabase totale simulée + timeouts/retries explicites des server fns.

## 7. Radar v2 & delta vs 01/06 (S3)

Échelle /4, 8 dimensions. Référence = **RUN2** (le run le plus détaillé du 01/06, 44 sous-scores).
Score v2 = état au 2026-06-12 après C1+C3 + cette session C2 (S1/S2). Chaque note est justifiée par
une preuve mesurée, pas une impression.

| Dimension | 01/06 (RUN2) | v2 (12/06) | Δ | Justification du delta |
|---|:---:|:---:|:---:|---|
| Versioning | 2,5 | **3,0** | +0,5 | CI mûre (6 workflows), branch-protection, husky, conventional commits **+ hygiène branches faite** (35 obsolètes purgées, D3). Plafond : **toujours 0 tag de release** (F03). |
| Stack technologique | 3,5 | **3,5** | = | 0 vuln, stack moderne (React 19/Vite 7/TanStack), dependabot + politique de maj, triage majeures documenté (D2). Plafond : pipeline build custom Worker→Vercel (SPOF) + double config. |
| Architecture | 3,5 | **3,5** | = | Discipline **prouvée** (scan : 0 violation de frontières, 1 seul `any`, 3 TODO trackés) — passe de « supposée » à « vérifiée ». Plafond : 3 routes monolithiques (pire en brut), SPOF build, mono-région. |
| Qualité de code | 3,0 | **3,0** | = | lint 0/0, gate `max-lines`, DOMPurify, logger structuré, dette commentée quasi nulle. Plafond inchangé : routes monolithiques, pas de règle `complexity`, micro-dette (F18 `console.error`, F26 `noUnusedLocals`). |
| **Tests & couverture** | 2,0 | **3,0** | **+1,0** | Saut majeur : 8 % → **~93 % scopé** (seuils 80 %), 585 tests, Playwright public+authed, **pgTAP 6 suites** (+1 ce jour). **Tempéré par GAP-026** : le chemin de quête déployé n'était exécuté par **aucun** environnement (unit = mock, e2e authed pas rejoué, seed cassé GAP-011) → un P0 SQL a atteint la prod. Repassera ≥ 3,5 quand GAP-011/025 (e2e authed réellement joué) sera levé. |
| Performance | 3,0 | **3,5** | +0,5 | **Preuve de charge** : D1 tenue 9–17× à 100 VU, 0 erreur / 25 977 req ; budgets bundle en CI (+ fix cycle chunk #87). Plafond : plafond d'écriture entre 1×–5× (pool Supabase), **pas encore** de Lighthouse/TTFB terrain (mono-région) → C4. |
| Logging & erreurs | 3,5 | **3,5** | = | Logger JSON + redaction, error boundaries client+SSR, **résilience prouvée** (4 chemins d'erreur fail-closed, 0 fuite 5xx sur 48 k req). Plafond : pas de correlation/request ID (F17), 2 `console.error` résiduels. |
| **Sécurité** | 3,0 | **3,5** | +0,5 | Chantier C3 livré : **toutes les failles d'intégrité closes en prod** (GAP-016/020/021), P0 admin levé, REVOKEs, RPC server-authoritative, pgTAP sécu (escalade/RLS/entitlements). Plafond : CSP `unsafe-inline` + pas de validation headers en CI (GAP-022→C4), conformité mineurs (GAP-003/024, plutôt juridique). |
| **Moyenne** | **3,0** | **3,31** | **+0,31** | Progrès tiré par Tests (+1,0), Sécurité/Performance/Versioning (+0,5). |

**Lecture du delta.** En 11 jours, le produit passe de « bon mais non vendable » (P0 admin, i18n cassée,
intégrité trouée, couverture 8 %) à un socle **3,31/4** où aucun axe n'est sous 3. Les deux moteurs
sont **Tests** (industrialisés) et **Sécurité** (intégrité verrouillée). Le radar ne monte pas plus
haut pour une raison saine : C2 a **mesuré au lieu de supposer**, et la mesure a révélé un P0 réel
(GAP-026) + des angles morts honnêtes (e2e authed non rejoué, charge en écriture à dimensionner,
TTFB terrain non mesuré). Ce sont des leviers identifiés, pas des inconnues.

## 8. Synthèse & backlog (S3)

**Verdict technique.** Le socle est **sain et prêt pour une beta** : architecture disciplinée
(vérifiée), sécurité d'intégrité verrouillée, tests industrialisés, et **charge largement au-dessus
des cibles beta** (0 erreur à 100 VU). Aucun bloquant technique de lancement ne subsiste après la
clôture de GAP-026. La dette restante est **ciblée et priorisée**, pas diffuse.

**3 axes structurants pour C4** (architecture prod) : (1) **dimensionnement** du chemin d'écriture
(pool Supabase / plan / cold starts — plafond submit entre 1× et 5×) ; (2) **simplification du
pipeline de build** (préset mono-fournisseur, étude lovable-config 2.4) + **mono-région** (TTFB
terrain TN à mesurer) ; (3) **headers/CSP** (nonce, validation CI).

**Versement au backlog 90** (candidats C2 promus en GAP — détail et statuts dans le backlog) :

| GAP | Sujet | Sév. | Cible |
|---|---|:---:|---|
| GAP-005 | Tests de charge | — | **🟢 fait en C2/S2** (D1 tenue, dimensionnement → C4) |
| GAP-007 | Double config deploy → en fait pipeline build porteur | P2 | **Décidé** : garder ; simplification = C4 |
| GAP-009 | Tri branches + PRs dependabot | P3 | **🟡** branches faites (D3) ; PRs dependabot = D2 |
| GAP-027 | Dimensionnement charge écriture / pool Supabase | P2 | → C4 |
| GAP-028 | Exécuter la politique de release (tag `v1.0.0` + changelog) | P2 | avant go-live |
| GAP-029 | Lighthouse/Web Vitals en CI + TTFB terrain Tunisie | P3 | → C4 (mesure) + CI |
| GAP-030 | Correlation/request ID dans le logger | P3 | repo |
| GAP-031 | Extraction des 3 routes monolithiques (quest/dashboard/dungeon) | P3 | repo |
| GAP-032 | Micro-dette : `console.error`→logger, `noUnusedLocals/Parameters: true` | P3 | repo (fin de C2) |
| GAP-034 | Résilience : panne Supabase totale simulée + timeouts/retries server fns | P3 | repo |

(CSP nonce + cache HTTP = déjà GAP-022, porté par C4. Conformité mineurs = GAP-003/024.)

**Action de clôture C2** (D2) : vague de minors sûrs (`npm update` dans les ranges semver + gate
`ci:verify` + e2e smoke), un commit `chore(deps)`. À faire quand la machine n'est pas sous charge.
