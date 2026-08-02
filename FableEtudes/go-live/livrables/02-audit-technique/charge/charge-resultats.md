# Tests de charge & résilience — résultats (C2/S2)

> Livrable S2 du chantier [02](../../02-audit-technique-architecture.md). **Exécuté contre le projet
> TEST `pqegdnwdtbjtplcthxyp` uniquement** (jamais la prod). Outil : k6 v2.0.0 (binaire standalone,
> `./bin/k6.exe`). Scénarios : [`k6-main.js`](./k6-main.js) · données : [`prep.py`](./prep.py)
> (40 comptes de charge + tokens + 30 exercices culture-générale avec corrigés).
> Date : 2026-06-12.

## ⚠️ Constat majeur en préparant la charge : un P0 prod (GAP-026)

Le **tout premier appel REST réel** à `start_exercise_session` a renvoyé
`42702 « column reference "started_at" is ambiguous »` — la RPC, déployée le 10/06, **échoue à
chaque appel**, et comme la révocation compagnon `…190000` a fermé l'INSERT direct, **le démarrage
de quête est cassé en production**. Détail + correctif : GAP-026 (backlog 90) + migration
`20260612090000`. Les campagnes ci-dessous ont été lancées **après application du correctif sur
TEST**. C'est la valeur d'un test en environnement réel : le mock `supabase.rpc` des tests unitaires
ne pouvait pas l'attraper.

## Cibles (décision D1)

| Métrique | Cible |
|---|---|
| Utilisateurs simultanés (navigation) | 100 |
| Pic de soumissions de quête | 500 / h |
| p95 `submit_exercise_attempt` | < 1 000 ms |
| p95 lectures dashboard | < 2 000 ms |

## Scénarios

- **browse** — reproduit `getDashboardPrimary` (4 requêtes PostgREST en parallèle : profil, subjects,
  attempts récents, attempts agrégés) + leaderboard (profils triés par xp, limit 50), avec temps de
  réflexion réalistes (1–5 s).
- **quest** — parcours complet : `start_exercise_session` → temps de lecture ≥ 4 s/question (pour
  passer le gate anti-rush) → `submit_exercise_attempt` (réponses correctes).

## Résultats

### Campagne 1 — `target` (validation D1) : ramp navigation → 100 VU, quêtes ~540/h, 4 min 30

| Opération | p95 | p99 | max | seuil D1 | verdict |
|---|---|---|---|---|---|
| **submit** (écriture, RPC scoring) | **114 ms** | 856 ms | 1,30 s | < 1 000 ms | ✅ ~9× de marge |
| **dashboard** (4 lectures //) | **116 ms** | 601 ms | 1,61 s | < 2 000 ms | ✅ ~17× de marge |
| **leaderboard** | **100 ms** | 604 ms | 1,45 s | < 2 000 ms | ✅ |

- **25 977 requêtes, 0 échec (0,00 %)** · **15 660 checks, 100 % réussis** · 89,9 req/s soutenu.
- Tous les seuils k6 franchis. La p99 (~600 ms) trahit des pics ponctuels (pooler/cold), sans jamais
  approcher les cibles.

**→ Les cibles D1 sont tenues très confortablement.** À l'échelle d'une beta TN (100 utilisateurs
simultanés, 500 soumissions/h), l'empilement Vercel `arn1` + Supabase eu-north-1 ne transpire pas.

### Campagne 2 — `stress` (×5 le débit d'écriture D1 ≈ 2 500/h, 100 VU navigation constants), 3 min 30

| Opération | p95 | p99 | max | observation |
|---|---|---|---|---|
| **submit** | **1,89 s** | 4,71 s | 5,81 s | dépasse le seuil 1 s (attendu à ×5) |
| **dashboard** | 182 ms | 4,69 s | 6,44 s | lectures encore saines en p95 |
| **leaderboard** | 104 ms | 2,57 s | 6,48 s | idem |

- **22 439 requêtes, 0 échec (0,00 %)** · **13 728 checks, 100 % réussis** · 94,8 req/s.
- **Dégradation gracieuse par la latence, pas par l'erreur** : à 5× le débit d'écriture cible, le
  système ne renvoie toujours aucun 5xx — il ralentit (submit p95 1× = 114 ms → 5× = 1,89 s). Les
  lectures restent rapides ; c'est le **chemin d'écriture** (RPC scoring + pooler) qui sature en
  premier.

**Lecture sizing (→ C4)** : le plafond « p95 submit < 1 s » se situe **entre 1× (540/h) et 5×
(2 500/h)**. Aucune erreur jusqu'à ×5 ; la tête de distribution (p99 4–5 s, `iteration_duration`
max ~30 s) pointe une **saturation ponctuelle du pool de connexions Supabase** sous rafale — premier
levier à dimensionner en C4 (taille du pool PgBouncer / plan Supabase / cold starts Vercel).

## Résilience — sondes de chemins d'erreur (TEST)

| Sonde | Résultat | Attendu |
|---|---|---|
| JWT invalide/expiré sur RPC | `401 — JWT cryptographic operation failed` | Rejet fail-closed ✅ |
| `start_exercise_session(null)` | `400 — Exercise not found` | RAISE gracieux ✅ |
| `submit` sur session forgée (UUID zéro) | `400 — Invalid quest session.` | Contrôle de propriété ✅ |
| Anti-rush : submit instantané (0 s) | `tooFast=true, xpEarned=0` | Gate tient même en appel API direct ✅ |

Comportement conforme : authentification fail-closed, entrées malformées rejetées proprement,
gates métier (propriété de session, anti-rush) appliqués côté serveur même hors UI. Aucune fuite de
5xx observée sur 48 000+ requêtes cumulées des 3 campagnes.

## Reproduire

```bash
cd go-live/livrables/02-audit-technique/charge
python prep.py                                  # (TTL tokens 1 h — relancer avant chaque campagne)
./bin/k6.exe run -e MODE=smoke   k6-main.js      # sanité ~40 s
./bin/k6.exe run -e MODE=target  --summary-export data/summary-target.json  k6-main.js   # D1
./bin/k6.exe run -e MODE=stress  --summary-export data/summary-stress.json  k6-main.js   # ×5
```

Le binaire k6 (`bin/k6.exe`) et `data/` (tokens, corrigés) sont locaux/gitignorables — ne pas
committer les tokens. `k6-main.js` refuse de tourner si l'URL pointe sur la prod.
