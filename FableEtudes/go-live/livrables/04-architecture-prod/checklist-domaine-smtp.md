# Checklist domaine + e-mails transactionnels (GAP-006)

> Livrable S1 du chantier [04](../../04-architecture-prod-deploiement.md) — **à dérouler quand le
> nom est choisi** (choix lié au naming/branding → C5 marketing). Toi aux manettes (achats +
> dashboards) ; ~1 h au total, coût ~12–15 $/an. Prérequis du **palier 1** (la vente exige des
> e-mails fiables, et DKIM exige un domaine).

## A. Choisir & acheter le domaine (15 min)

1. **Nom** : 2-3 candidats côté C5 (ex. `xpscholars.com`). Mon conseil : un **.com** d'abord
   (achat 5 min, gestion simple) ; le `.tn` (~30–60 TND/an, registrar agréé ATI, dossier) peut
   s'ajouter **plus tard** en redirection — ne bloque rien.
2. **Registrar** : Cloudflare Registrar (prix coûtant, ~10–12 $/an, DNS inclus — et prépare
   l'option B du dossier §3) ou Namecheap. Éviter les offres « gratuites la 1ère année ».
3. Activer le **renouvellement automatique** + verrou de transfert. Garder le compte registrar
   sous TON e-mail principal avec 2FA.

## B. Brancher le domaine sur Vercel (10 min)

1. Vercel → projet `yahia-quest-arena` → **Settings → Domains** → Add → `tondomaine.com`
   (+ `www.tondomaine.com` en redirect vers l'apex).
2. Poser les enregistrements DNS indiqués par Vercel chez le registrar :
   apex `A 76.76.21.21`, `www` `CNAME cname.vercel-dns.com` (valeurs affichées par Vercel —
   suivre ce qu'il dit, elles priment).
3. Attendre la propagation (minutes → quelques heures). **SSL automatique** (Let's Encrypt) —
   rien à faire.
4. Vérifier : `https://tondomaine.com` sert l'app, le cadenas est valide,
   `https://yahia-quest-arena.vercel.app` continue de marcher (alias conservé).

## C. E-mails transactionnels — Resend + Supabase Auth (20 min)

> Pourquoi : le SMTP par défaut de Supabase est très limité (quelques mails/heure, expéditeur
> générique) — inutilisable dès qu'on a de vrais inscrits.

1. Créer un compte **Resend** (free : 3 000 mails/mois, 100/jour — large pour la beta).
2. Resend → **Domains** → Add `tondomaine.com` → poser les 3 enregistrements DNS donnés
   (DKIM ×2 + SPF/Return-Path) chez le registrar → attendre « Verified ».
3. Resend → **API Keys** → créer une clé `supabase-auth` (scope sending).
4. Supabase (projet **prod** `fasrenmmrkqjoobrztbp`) → **Authentication → Emails → SMTP Settings** :
   - Host `smtp.resend.com` · Port `465` · User `resend` · Password = la clé API
   - Sender : `no-reply@tondomaine.com` · Nom : `Na9ra Nal3ab`
5. **Tester** : créer un compte jetable → l'e-mail de confirmation doit arriver en boîte de
   réception (pas spam) avec le bon expéditeur. Tester aussi « mot de passe oublié ».
6. Adapter les **templates e-mail** Supabase (Authentication → Emails) : FR, ton de l'app.

## D. Adresses de contact (10 min)

1. `support@tondomaine.com` (+ `contact@`) en **alias de réception** vers ta boîte : gratuit via
   Cloudflare **Email Routing** (si DNS chez Cloudflare) — Email Routing → Enable → route
   `support@…` → `bejimed@gmail.com`.
2. Pour RÉPONDRE depuis `support@…` : Gmail → Paramètres → Comptes → « Envoyer des e-mails en
   tant que » → SMTP Resend (même clé) ou laisser tel quel pour la beta (répondre depuis Gmail).
3. Mettre l'adresse support dans le footer de l'app + (à terme) pages légales (GAP-024).

## E. Après bascule (5 min)

- [ ] Vercel : le domaine custom est « Primary » ; `*.vercel.app` reste en alias.
- [ ] Vérifier `og:url`/metas si elles citent l'URL (recherche `vercel.app` dans le repo : aucune
      occurrence à date — rien à changer côté code).
- [ ] Me le dire → je mets à jour GAP-006 et la mesure TTFB/Lighthouse (GAP-029) se fera sur le
      domaine final.
