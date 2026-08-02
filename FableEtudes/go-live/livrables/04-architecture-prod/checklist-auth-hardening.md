# Checklist hardening Auth production (GAP-023)

> Livrable S2 du chantier [04](../../04-architecture-prod-deploiement.md). Réglages **dashboard
> Supabase prod** (`fasrenmmrkqjoobrztbp`) — non auditables par code, à dérouler toi-même (~15 min).
> Source : constat C3 (F-306). Cocher au fur et à mesure ; me dire quand c'est fait → je mets à
> jour GAP-023.

## Authentication → Sign In / Up

- [ ] **Email confirmations : ON** (un compte non confirmé ne doit pas accéder à l'app).
      ⚠️ Tant que le SMTP custom n'est pas posé (checklist domaine/SMTP §C), le SMTP par défaut
      est limité à quelques mails/heure — si la beta recrute activement, séquencer : SMTP d'abord.
- [ ] **Minimum password length : 8+** (l'UI cliente valide déjà 8 — aligner le serveur).
- [ ] **Password requirements** : exiger lettres + chiffres (bon compromis collégiens).
- [ ] **Leaked password protection (HIBP) : ON** si disponible sur le plan Free — sinon noter
      pour le passage Pro (palier 2).
- [ ] **Provider Google** : trancher. C3 a noté un bouton Google dans l'UI avec provider
      potentiellement non configuré côté prod → soit configurer OAuth Google proprement
      (Console Google Cloud + redirect URLs), soit me demander de **retirer le bouton** (5 min,
      évite un bouton mort en beta). → décision à me communiquer.

## Authentication → Rate Limits (défauts Supabase OK, vérifier)

- [ ] Token (connexions) : laisser le défaut (~30/5 min/IP) — cohérent avec ce qu'on a observé en
      charge (le 429 sur l'endpoint token est apparu vers ~35 logins rapides d'une même IP).
- [ ] Sign-ups / OTP : défauts OK pour la beta ; resserrer si abus constaté (alertes UptimeRobot +
      Sentry les rendront visibles).

## Authentication → Sessions / JWT

- [ ] JWT expiry : défaut 3600 s OK (l'app rafraîchit via supabase-js).
- [ ] **Refresh token rotation : ON** (défaut récent — vérifier qu'il est actif).

## Authentication → URL Configuration

- [ ] **Site URL** = `https://yahia-quest-arena.vercel.app` (→ à mettre à jour au domaine custom).
- [ ] **Redirect URLs** : ne contenir QUE l'URL prod (+ `http://localhost:8080` si tu veux garder
      le dev local connecté à prod — sinon retirer, le dev se fait sur TEST via dev-on-test).

## Hors dashboard (rappels liés)

- [ ] MFA : **non** au lancement (public collégiens) — décision actée, rien à faire.
- [ ] Les clés `service_role` ne vivent QUE dans : GitHub Secrets (e2e/backup) + ta machine
      (`.env.test`). Jamais dans Vercel (l'app n'en a pas besoin) — vérifier qu'aucune variable
      `SUPABASE_SERVICE_ROLE_KEY` n'existe côté Vercel prod.
- [ ] Au passage en palier 1/2 : re-dérouler cette checklist (HIBP, SMTP, Site URL domaine).
