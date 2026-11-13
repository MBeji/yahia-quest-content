# Étude 40 — Revenir après la première visite : les fils de retour du visiteur, du nouvel élève et du parent

> **Statut** : **brouillon** (2026-11-12) — rédigée depuis une session cloud, sur un relevé du jour :
> code du moteur à `b25edd6` (#1257), bundle servi par `www.na9ranal3ab.tn`, base de production lue
> en agrégats (lecture seule, aucune ligne nominative), parcours visiteur joué dans Chromium en
> émulation Pixel 7. Cinq questions au propriétaire (§7). Deux familles de lots (§4) : 0, 1, 3, 4 et 5 ne dépendent
> d'aucun geste du propriétaire ; le lot 2 attend, pour son effet, le geste Vercel (prérequis P-0).
> **Priorité** : 40 · **Valeur** : 🔁 la commande du propriétaire, mot pour mot — « je veux que les
> utilisateurs reviennent après une première visite ». Le relevé dit pourquoi ils ne reviennent
> pas : **le canal de retour construit par l'étude 31 est éteint en production** (la clé publique
> VAPID manque au build : zéro souscription push, jamais), **le visiteur sans compte — l'audience
> principale depuis le 11 novembre — n'a aucun fil de retour**, et **six élèves sur dix n'ont jamais
> joué après avoir créé leur compte**, ce qui les place hors de toutes les audiences de rappel. Cette
> étude mesure, rend la panne du push visible (son rallumage est un geste du propriétaire, P-0), puis
> pose trois fils sobres : l'invitation à installer, le lien de reprise
> que l'on s'envoie, et le rappel proposé après une victoire · **Complexité** : moyenne — une
> sonde de santé, deux migrations additives (une lecture d'admin, une audience de push),
> quatre événements produit, trois composants ; aucun prestataire nouveau, aucune donnée
> personnelle nouvelle
> **Architecte** : Fable (session Claude Code), 2026-11-12 · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : é31 (push, pipeline de priorité, liste fermée d'événements, R-4 et R-20) · é38
> (lot 0 : tunnel sans compte ; lot 2 : accueil sans péage, #1257 ; **lot 5 : carte « Reprendre »,
> en cours d'exécution le 2026-11-12 — non re-spécifiée ici**) · é39 (partage du test de niveau,
> mémoire d'appareil) · é08 lot 2 (digest parent — fusionné le 2026-11-12, moteur #1265, en ligne
> à la reprise du déploiement ; non re-spécifié) · chantier « être
> trouvé » (#1246, #1247) · **Bloque** : rien ; **informe** é06 (gelée) sans la dégeler — Q-5
> **Docs normatifs liés** : AGENTS.md, ARCHITECTURE.md, `docs/doctrine-verticale.md`,
> `docs/content-voice-and-composition.md`, `docs/inventaire-traitements-inpdp.md`,
> `docs/environment-variables.md` (§ push), `docs/suivi-parental-quotidien.md`, `e2e/README.md`
>
> **Fiche de verticalité** (doctrine verticale, é26 D-2) :
> **Verticale** : V1 « apprendre & maîtriser » — **approfondissement** de trois capacités LIVE :
> « Notifications push » (STATUS §3 : 🟢 M3 — **faux en production**, voir T-1), « Plateforme
> publique sans login » (🟢 M2) et « PWA » (🟠 M1 : manifeste et service worker servis, aucune
> invitation). Le lot 0 est une **fondation** (mesure), hors arbre de décision ·
> **Maturité visée** : **M3** pour les notifications (aujourd'hui M1 de fait : la mécanique existe,
> l'expérience n'existe pas) ; M3 pour le retour du visiteur dans la plateforme publique (critères
> DoE 1, 2 et 6). Pas de M4 ·
> **Boucles** : l'étude **referme** (a) le canal de retour de é31 lot 4 — six audiences, un cron
> quotidien, trois langues, payés et jamais reçus par personne ; (b) le manifeste et le service
> worker, servis à chaque visiteur depuis le go-live sans qu'aucun écran propose l'installation ;
> (c) le `distinct_id` par navigateur de PostHog, qui survit d'une visite à l'autre et que rien ne
> lit comme un retour ; (d) le partage, construit deux fois (bilan parent, test de niveau) et
> absent de l'écran où l'élève réussit. **OUVRE** : quatre événements produit, consommés dès le
> lot 0 par `/admin/engagement` et par le relevé hebdomadaire (#962) ; rien d'autre. Les deux
> ouvertures de capacité que le sujet appelle — un rendez-vous hebdomadaire public, un canal
> e-mail — sont **gelées par défaut** (P-7) et posées en questions (Q-3, Q-4) ·
> **Apport IA** : **rejeté** — qui rappeler, quand, et avec quels mots est déterministe (é31 R-16,
> P-5a). La prose d'El Ostedh n'entre dans aucun rappel de cette étude.

## 0. TL;DR

**La question.** Entre la fin d'une première visite et une deuxième, qu'est-ce qui ramène la
personne ? L'étude la pose pour trois publics — le visiteur sans compte, l'élève qui vient de
créer son compte, le parent — et répond par des faits, pas par un inventaire d'idées.

**Ce que le relevé dit** (§1.2, chaque ligne a sa preuve) :

1. **Le push est éteint en production.** Le chunk `enable-push-card-*.js` servi le 2026-11-12
   contient `usePush` réduit par le compilateur à `g() ? t("unconfigured") : t("unsupported")` :
   `VITE_VAPID_PUBLIC_KEY` est absente du build. La carte d'activation se masque donc pour tout le
   monde (`enable-push-card.tsx:16`). En base : `push_subscriptions` **0 ligne**,
   `push_consent_events` **0 ligne**. Les six notifications de é31 et le bilan parent du dimanche
   n'ont jamais atteint un seul appareil. STATUS §3 écrit « Notifications push 🟢 M3 ».
2. **Le visiteur sans compte n'a aucun fil.** En production, la fin d'un quiz anonyme propose
   « Recommencer · Retour à la matière · Créer mon compte » et rien d'autre ; après la visite,
   l'appareil ne garde que `na9ra.ph_did` et `nn:outbox:v1`. Aucun `beforeinstallprompt` dans
   `src/`, aucun lien à s'envoyer, aucun partage hors test de niveau, aucun rendez-vous visible
   (ligue, classement, arène vivent sous `_authenticated`). La carte « Reprendre » (é38 lot 5) lui
   donnera une raison de rester **s'il revient** ; elle ne le fait pas revenir.
3. **Le compte créé n'est pas un compte joué.** 36 élèves sur 60 ont `last_active_date` NULL — 7
   des 13 inscrits des trente derniers jours. Or les six audiences de `push_daily_audiences`
   exigent toutes une activité passée : ce public-là n'est dans **aucune** audience, push rallumé
   ou non. 10 comptes sur 78 n'ont jamais confirmé leur e-mail.
4. **Le rappel est proposé au mauvais endroit, avec le mauvais mot.** Hall, tout en bas (« zone
   calme », `dashboard.tsx:654`), et paramétrage ; texte : « Reçois une alerte quand ta série est
   en danger » — la perte, là où é31 R-20 demande le gain. Jamais après une victoire.
5. **Sur iPhone le fil n'existe pas** : pas de push dans Safari hors application installée
   (`isPushSupported` y est faux), et rien n'invite à installer.
6. **Le rendez-vous hebdomadaire est vide** : aucune ligne dans `duel_league_awards` sur quatre
   semaines. Les deux récapitulatifs de la semaine (« Ta semaine », bilan d'El Ostedh) ne se
   voient qu'en revenant de soi-même.
7. **Le parent** : 17 comptes, 2 liens actifs. Le bilan part du parent vers WhatsApp, jamais vers
   lui ; l'élève n'a qu'un bouton « copier » pour son code Alliance, au fond du paramétrage.
8. **Rien ne lit « revenu » pour un visiteur.** Côté compte, D1/D7/D30 existent
   (`admin_engagement_overview`) mais ne séparent pas « jamais joué » de « joué une fois ».

**Ce que l'étude décide** : sept lots, chacun une PR verte utile seule.
**0** la mesure du retour (deux événements, une lecture d'admin) · **1** le push se prouve (sonde
de santé, garde de build, garde nocturne — le geste Vercel lui-même est un prérequis du
propriétaire, P-0) · **2** le rappel proposé après une victoire,
dit en gain, plus l'audience « pas encore joué » · **3** l'invitation à installer après une
réussite (Android natif, iPhone guidé) · **4** le lien de reprise et le partage d'une réussite
(WhatsApp, zéro donnée) · **5** le parent dans la boucle (l'élève invite son parent en un geste) ·
**6** _gelé_ — un défi de la semaine visible avant le compte (Q-3). Un canal e-mail pour les
parents reste une question (Q-4), pas un lot.

## 1. Contexte & objectif produit

### 1.1 Lecture du besoin

La commande : « je veux aussi des axes métiers fonctionnels qui améliorent l'adhésion et l'usage,
je veux que les utilisateurs reviennent après une première visite ». Le contexte chiffré : 1 171
cours et 6 648 missions en ligne (compteur de la page d'accueil, lu le 2026-11-12) ; relevé
hebdomadaire du 2026-11-09 (#962) : 3 actifs la semaine du 26/10, aucun revenu la suivante. Depuis
le 2026-11-11 les pages de contenu sont lisibles par les moteurs de recherche et les aperçus de
partage (sitemap : 6 815 URL, dont 1 171 `/chapitre/` et 5 477 `/exercice/`) : **la première
visite type sera une page de cours ou d'exercice, sur téléphone, sans compte**.

Un produit fait revenir par trois mécanismes, et seulement trois : un **déclencheur externe** (un
message arrive : notification, lien dans une conversation, icône sur l'écran d'accueil), une
**raison interne** (quelque chose m'attend : ma série, ma place, mon chapitre en cours) et un
**rendez-vous** (ça se passe à une date : lundi, la ligue). L'étude 31 a construit les raisons
internes et les rendez-vous d'un élève **connecté et déjà actif**. Le relevé montre que les
déclencheurs externes, eux, n'existent pour personne aujourd'hui.

### 1.2 Le relevé — l'état réel au 2026-11-12

Sources : **[code]** `MBeji/yahia-quest-arena` à `b25edd6` · **[bundle]** fichiers servis par
`https://www.na9ranal3ab.tn` · **[prod-db]** agrégats lus en lecture seule sur le projet Supabase
de production · **[nav]** Chromium (Playwright, profil Pixel 7, visiteur, aucun compte créé).

#### T-1 — Le canal push, de bout en bout

| Maillon                                                                                     | État             | Preuve                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service worker, événements `push` et `notificationclick`                                    | en place         | **[code]** `public/sw.js` ; **[nav]** `sw.js` enregistré sur une page de chapitre                                                                                                                           |
| Cron quotidien 18:00 UTC (~19:00 Tunis)                                                     | déclaré          | **[code]** `vercel.json` `crons` → `/api/cron/notify` → `handlePushCron`                                                                                                                                    |
| Six audiences d'élève, au plus un push par jour                                             | en place         | **[code]** `push_daily_audiences` (`20260902160000`), `resolveDailyPushPlan`                                                                                                                                |
| Textes FR/EN/AR, ton sans reproche                                                          | en place         | **[code]** `push-copy.ts`                                                                                                                                                                                   |
| Souscription : exige un compte                                                              | par construction | **[code]** `push_subscriptions.user_id NOT NULL`, `save_push_subscription` lève `Unauthorized` sans `auth.uid()`                                                                                            |
| **Clé publique dans le build de production**                                                | **ABSENTE**      | **[bundle]** `assets/enable-push-card-0jvXA2Bl.js` : `useEffect(()=>{g()?t("unconfigured"):t("unsupported")},[])` et `enable: async()=>{g()}` — la branche « clé présente » a été éliminée à la compilation |
| Carte d'activation visible                                                                  | **jamais**       | **[code]** `enable-push-card.tsx:16` : `unconfigured` ⇒ `return null`                                                                                                                                       |
| Souscriptions enregistrées                                                                  | **0**            | **[prod-db]** `push_subscriptions` : 0 ligne ; `push_consent_events` : 0 ligne                                                                                                                              |
| Variables serveur (`VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_SUBJECT`, `CRON_SECRET`) | **non constaté** | l'accès Vercel de la session a été refusé (403 sur le périmètre de l'équipe) — constaté par le propriétaire au prérequis P-0 (§4)                                                                           |

Conséquence : **aucun des rappels décrits comme livrés n'a jamais été reçu**. Ce n'est pas un trou
de conception, c'est une panne muette — exactement ce que la leçon de STATUS §8 nomme « un
interrupteur qu'on croit avoir ».

Deux défauts de second rang, visibles dans le code et sans effet tant que T-1 dure :

- `streak-at-risk` et `streak-lost` interpolent `{n} jours` sans singulier : une série d'un jour —
  le cas du lendemain de la première quête, donc **le** rappel de la deuxième visite — donne
  « tes 1 jours continuent » (`push-copy.ts`, seul `tutor-daily-plan` a un singulier).
- Tous les rappels d'élève ramènent à `/dashboard` (sauf la ligue : `/duel`). Aucun ne ramène à la
  quête ou au chapitre en cours.

#### T-2 — Le visiteur sans compte

| Moment                                   | Ce qui se passe                                                                                                                                                                                    | Preuve                                                                                                                                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arrivée sur un cours                     | lecture libre ; en-tête : Programme · Extras · Test de niveau · Suivi parent · Connexion · Créer mon compte                                                                                        | **[nav]** `/chapitre/2bd52d30-…`                                                                                                                                                                      |
| Bas du cours                             | étapes « Cours → Quiz → Missions », bouton du quiz, puis l'invitation « Apprends en jouant — Crée ton compte gratuit pour gagner des XP, garder tes chapitres débloqués et suivre ta progression » | **[nav]** ; **[code]** `lesson-reader.tsx:483`                                                                                                                                                        |
| Fin d'un quiz ou d'une mission           | score, « Recommencer », « Retour à la matière », puis « Avec un compte, cette mission vaut jusqu'à 20 XP. — Créer mon compte »                                                                     | **[nav]** `/exercice/6c069575-…` ; **[code]** `exercice.$exerciseId.tsx:200-265`                                                                                                                      |
| Ce que l'appareil garde                  | `na9ra.ph_did` (compteur PostHog) et `nn:outbox:v1` ; le quiz réussi vit en `sessionStorage` (`na9ra.anonQuizPassed`) jusqu'au lot 5 de é38                                                        | **[nav]** clés lues après le parcours ; **[code]**                                                                                                                                                    |
| Invitation à installer                   | aucune                                                                                                                                                                                             | **[code]** zéro occurrence de `beforeinstallprompt`, `appinstalled`, `display-mode` dans `src/` ; le manifeste (`display: standalone`, icônes 192/512/maskable) et l'icône Apple sont pourtant servis |
| Notification                             | impossible                                                                                                                                                                                         | T-1 ; et la souscription exige un compte                                                                                                                                                              |
| Lien à s'envoyer, partage d'une réussite | aucun sur le cours ni sur le résultat ; le partage n'existe que sur le bilan du test de niveau et le bilan parent                                                                                  | **[code]** `navigator.share` : `placement-bilan.ts`, `suivi.tsx`, `parent-report.tsx` seulement                                                                                                       |
| Rendez-vous visible                      | aucun : ligue, classement, arène, donjon sont sous `_authenticated` ; la page d'accueil ne porte aucune date                                                                                       | **[code]** `src/routes/_public/*` ; **[nav]** `/`                                                                                                                                                     |
| Seule raison de revenir déjà en chantier | la carte « Reprendre » (30 jours, é38 lot 5)                                                                                                                                                       | étude 38 §4, lot 5                                                                                                                                                                                    |

**L'hypothèse de départ est confirmée** : le visiteur sans compte n'a aucun fil de retour. Le seul
geste que la première visite lui propose pour « garder » quelque chose est de créer un compte —
c'est-à-dire un formulaire, à l'instant où il vient de finir ce qu'il était venu faire.

#### T-3 — L'élève qui vient de créer son compte

| Fil                                                                                  | Condition pour qu'il s'active                                                                                                                        | Quand la première visite le propose                                          | Preuve                                                                                                                                                     |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Confirmation d'e-mail (inscription par mot de passe)                                 | ouvrir le lien reçu                                                                                                                                  | écran « e-mail envoyé », avec renvoi                                         | **[code]** `auth.tsx:212,252`, `auth-sent-screens.tsx` ; **[prod-db]** 10 comptes sur 78 jamais confirmés ni connectés (33 comptes sont passés par Google) |
| Classe choisie                                                                       | assistant d'accueil, ou la carte en un geste depuis une quête (é38 lot 2)                                                                            | à l'arrivée                                                                  | **[prod-db]** 27 élèves sur 60 sans classe                                                                                                                 |
| Série (`current_streak`)                                                             | avoir fini **une** quête                                                                                                                             | —                                                                            | **[code]** `award_xp` ; **[prod-db]** 36 élèves sur 60 n'ont jamais été actifs ; 15 ne l'ont été que le jour de l'inscription                              |
| Missions du jour, pack de bienvenue, « Ta semaine »                                  | revenir de soi-même au hall                                                                                                                          | visibles au hall                                                             | **[code]** `dashboard.tsx` zones 1-2                                                                                                                       |
| Push : série en danger, série perdue, jalon, plan du jour, ligue, « reprends » à J+7 | T-1 réparé **et** permission accordée **et**, pour chacune, une activité passée (`current_streak > 0`, ou `last_active_date` renseignée, ou un duel) | carte au bas du hall et dans le paramétrage — jamais sur l'écran de résultat | **[code]** `push_daily_audiences`, `dashboard.tsx:649-655`, `parametrage.tsx:468`                                                                          |
| E-mail                                                                               | —                                                                                                                                                    | —                                                                            | **[code]** aucun envoi hors authentification Supabase (ni prestataire, ni gabarit)                                                                         |

Trois constats :

1. **L'élève qui s'inscrit sans jouer n'a aucun fil**, et c'est le cas majoritaire (36/60). Aucune
   audience ne le couvre : `comeback` exige `last_active_date = jour − 7`, donc une activité.
2. **L'élève qui joue une fois a un seul fil possible** — le rappel de série du lendemain — et ce
   fil exige une permission que rien ne lui a demandée au moment où il aurait dit oui.
3. Sans push ni e-mail, **un compte n'a aucun déclencheur externe**. Tout ce que é31 a livré
   suppose que l'élève rouvre le site de lui-même.

Ce que l'élève retrouve **quand il revient** est en revanche riche et n'appelle rien : salut après
absence (`daysAwayFrom`, `dashboard.tsx:409`), prochaine action unique (é22), « Ta semaine » (é31
lot 5), rachat de série, bilan de départ (é39). Cette étude n'y ajoute pas d'écran.

#### T-4 — Le parent

| Fil                                              | Condition                                                                                             | Preuve                                                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Suivi sans compte par code Alliance              | recevoir le code de l'enfant ; `/suivi?code=…` le pré-remplit                                         | **[code]** `suivi.tsx:32`                                                                    |
| « Se souvenir de ce code sur cet appareil »      | case cochée par défaut                                                                                | **[code]** `remembered-code.ts` ; **[nav]** `/suivi`                                         |
| Partage du bilan (WhatsApp / feuille de partage) | bilan affiché — le parent **envoie**, il ne reçoit pas                                                | **[code]** `suivi.tsx:287-292`                                                               |
| Push « bilan famille » du dimanche               | compte parent + lien actif + permission ; **T-1**                                                     | **[code]** `dispatchParentDigest` ; **[prod-db]** 17 parents, 2 liens actifs, 0 souscription |
| Comment le parent apprend que le site existe     | la page d'accueil (« Je suis parent ») ; côté élève, le code se copie depuis Paramétrage › Mon compte | **[code]** `parametrage.tsx:397-410` (bouton « copier », aucun partage)                      |

Le parent est le seul public adulte, joignable par WhatsApp, et celui dont le retour entraîne
celui de l'enfant. Aujourd'hui **rien ne part de l'élève vers lui** en moins de cinq gestes.

#### T-5 — La mesure

- **Compte** : `admin_engagement_overview` calcule la CURR hebdomadaire (KPI-A) et la rétention
  D1/D7/D30 par cohorte d'inscription (KPI-B), lues dans `/admin/engagement` et dans l'issue
  hebdomadaire `engagement-releve` (#962). Elle ne dit pas combien d'inscrits ont **joué une
  première fois** : la cohorte mélange ceux qui ne sont jamais partis et ceux qui ne sont jamais
  arrivés.
- **Visiteur** : PostHog reçoit `$pageview` et les trois événements de é38 avec un `distinct_id`
  aléatoire par navigateur (`na9ra.ph_did`, `localStorage`), profils de personne désactivés. Le
  même identifiant porte la visite du lundi et celle du jeudi : un retour **par navigateur** est
  lisible sans identifier personne. Aucun événement ni aucune lecture ne le nomme.
- **Push** : `push_optin` / `push_optout` existent au catalogue ; avec T-1 ils ne peuvent pas
  partir.
- **Installation** : rien.

#### T-5 bis — Ce que la première visite elle-même coûte (relevé voisin, même jour)

Le relevé « première visite » est sur `main` du moteur
(`docs/audit-premiere-visite-2026-11-12.md`). Deux de ses chiffres bornent ce que cette étude peut
espérer : **4 657 des 5 477 pages d'exercice du sitemap (85 %)** s'ouvrent sur la porte du quiz, et
le premier verdict demande **14 touchers et 40 s** sur une mission scolaire contre **2 touchers et
7 s** sur une mission non scolaire. Or les invitations de cette étude (installer, s'envoyer la
suite, partager) sont accrochées à une **réussite** : un visiteur qui n'atteint pas de verdict ne
les verra pas. Trois décisions de cet audit sont **en arbitrage** devant le propriétaire (aperçu de
deux questions avant la porte ; dire lesquelles étaient justes après un quiz raté) : cette étude ne
les rouvre pas, elle en dépend pour sa portée. L'audit a aussi posé « Quête suivante » en premier
bouton de l'écran de résultat sans compte (son C-3, `exercice.$exerciseId.tsx`) : les lots 3 et 4
s'insèrent **sous** ce bouton, jamais avant.

Événements déjà entrés dans la liste fermée ce jour, sur lesquels le lot 0 **s'appuie** sans les
re-spécifier : `resume_card_clicked{surface, days_since}` (é38 lot 5, moteur #1268 — `days_since
≥ 1` est déjà un retour constaté du visiteur sans compte, mais seulement de celui qui clique la
carte) ; `public_practice_started{exercise_id, is_quiz}` et `public_gate_shown{exercise_id}`
(session « première visite », autorisés le 2026-11-12, PR à venir).

#### T-6 — Le volume, pour garder les proportions

**[prod-db]** Sur les quatorze jours du 2026-10-30 au 2026-11-12 : 5 comptes créés (4 élèves),
31 tentatives enregistrées, et jamais plus de 2 comptes actifs le même jour ; aucune activité de
compte les 9, 10, 11 et 12 novembre (à l'heure du relevé). L'effet du chantier « être trouvé » du
11 novembre ne se lit pas encore dans les comptes — il ne peut se lire, avant le lot 0, que dans
la Search Console et les pages vues.

### 1.3 Les trous, classés par ce qu'ils coûtent

| #       | Trou                                                                                               | Qui                                 | À quel moment                            | Preuve           |
| ------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------- | ---------------- |
| **G-1** | Le push est éteint : la carte ne s'affiche jamais                                                  | tout compte, élève et parent        | toute la vie du compte                   | T-1              |
| **G-2** | Aucun fil de retour sans compte                                                                    | le visiteur — l'audience principale | à la fin de la première visite           | T-2              |
| **G-3** | Inscrit, jamais joué : dans aucune audience                                                        | 36 élèves sur 60                    | entre l'inscription et la première quête | T-3              |
| **G-4** | Le rappel n'est jamais proposé après une victoire, et son texte dit la perte                       | l'élève qui vient de jouer          | écran de résultat de la première quête   | T-3, `fr.ts:810` |
| **G-5** | iPhone : ni push sans installation, ni invitation à installer                                      | tout utilisateur iOS                | —                                        | T-1, T-2         |
| **G-6** | Rien ne part de l'élève vers son parent                                                            | l'élève, donc le parent             | après une réussite ; au paramétrage      | T-4              |
| **G-7** | « Revenu » n'est lu nulle part pour un visiteur ; « a joué » n'est pas séparé de « s'est inscrit » | l'équipe                            | chaque décision de ce plan               | T-5              |
| **G-8** | Le rendez-vous de la semaine est vide et invisible avant le compte                                 | tous                                | le lundi                                 | T-2, TL;DR 6     |
| **G-9** | Aucun canal vers un adulte qui n'a pas accordé le push                                             | le parent                           | —                                        | T-3, T-4         |

G-1 passe devant G-2 bien qu'il touche moins de monde : il coûte cinq variables et un redéploiement, et tant
qu'il dure le lot 2 et le digest parent de é08 n'ont aucun effet. G-7 n'est pas « moins grave » que les autres : il est traité
**en premier** (lot 0) parce qu'il décide de tout le reste (P-6).

### 1.4 Résultat attendu

- Un visiteur qui vient de réussir peut **garder le site** (icône sur l'écran d'accueil) ou
  **s'envoyer la suite** (WhatsApp) en un geste, sans formulaire, sans donnée.
- Un élève qui vient de gagner se voit proposer le rappel **à cet instant**, en gain ; celui qui
  s'est inscrit sans jouer reçoit **une** invitation à sa première quête, puis plus rien.
- Un élève peut inviter son parent en un geste ; le parent arrive sur le bilan, code pré-rempli.
- Le canal push est **prouvé vivant** chaque nuit, et son extinction se voit dans l'heure.
- « Revenu après une première visite » se lit, pour un compte et pour un navigateur.

### 1.5 Indicateurs (P-6)

| KPI                          | Définition                                                                                                                                                                                 | Où on le lit                                                          | Départ (2026-11-12)                        | Cible                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| **KPI-1** retour du visiteur | navigateurs émettant `visit_first` une semaine N qui émettent `visit_returned` dans les 7 jours ; recoupé par `resume_card_clicked{days_since ≥ 1}` (é38 lot 5), borne basse déjà en place | PostHog (insight posé au lot 0) ; ligne du relevé hebdomadaire si Q-2 | non mesuré                                 | **instrument d'abord** ; la cible se fixe après quatre semaines |
| **KPI-2** première quête     | inscrits de la semaine N ayant un jour d'activité dans les 7 jours                                                                                                                         | `admin_return_overview` → `/admin/engagement` et #962                 | 24/60 depuis l'origine ; 6/13 sur 30 jours | ≥ 70 %                                                          |
| **KPI-3** portée du push     | élèves actifs sur 30 jours ayant ≥ 1 souscription                                                                                                                                          | idem                                                                  | 0/8                                        | ≥ 30 %                                                          |
| **KPI-4** D7 des comptes     | KPI-B de é31, inchangé                                                                                                                                                                     | `/admin/engagement`                                                   | bruit (`n` de 1 à 5)                       | lu, pas ciblé, tant que `n` < 20                                |
| **KPI-5** installation       | `install_invite{action:"accepted"}` / `{action:"shown"}`                                                                                                                                   | PostHog                                                               | non mesuré                                 | instrument d'abord                                              |

Garde-fou lu avec KPI-3 : `push_optout` / `push_optin` sur la même période. Au-delà de 25 %, le
lot 2 est suspect et se relit avant tout ajout d'audience (R-8).

### 1.6 Ce que l'étude ne cherche PAS à faire

- **Re-spécifier** la carte « Reprendre » (é38 lot 5), le digest parent enrichi (é08 lot 2), le
  bandeau réseau (é38 lot 4), le test de niveau (é39). Elle s'y appuie.
- **Lire hors ligne** : é06, gelée. L'invitation à installer n'ajoute aucun cache (Q-5).
- **Souscrire un visiteur sans compte au push** : rejeté (D-3).
- **Ajouter des écrans au hall** ou de nouvelles récompenses : é31 est livrée, et aucune mécanique
  de rareté, de compte à rebours ou de hasard n'entre ici.
- **Envoyer des e-mails à des élèves** : hors de question dans cette étude (Q-4 ne concerne que
  les parents).
- **Acquérir** : comment le visiteur arrive est le chantier « être trouvé » et é39.

## 2. Spécification fonctionnelle

### 2.1 Acteurs & parcours

Acteurs : **visiteur** (sans compte — élève, parent ou enseignant, indiscernables), **élève**
connecté, **parent** (avec ou sans compte), **admin**.

- **US-1** (admin) — je lis chaque lundi combien de navigateurs sont revenus dans la semaine qui a
  suivi leur première visite, combien d'inscrits ont joué leur première quête, et combien d'élèves
  actifs peuvent recevoir un rappel.
- **US-2** (admin) — si le push s'éteint (clé absente du build, variables serveur manquantes), une
  garde le dit le lendemain matin au plus tard.
- **US-3** (élève) — je viens de réussir une quête : on me propose d'être prévenu quand mon plan du
  jour est prêt. J'accepte en un geste, ou je dis « plus tard » et on ne me le redemande pas avant
  longtemps.
- **US-4** (élève inscrit sans avoir joué, push accordé) — le lendemain, je reçois une invitation
  à ma première quête ; trois jours plus tard une seconde ; ensuite plus rien.
- **US-5** (visiteur ou élève, Android) — je viens de réussir : on me propose de mettre Na9ra
  Nal3ab sur mon écran d'accueil ; un geste ouvre la fenêtre du navigateur.
- **US-6** (visiteur ou élève, iPhone) — même moment : on me montre les deux gestes de Safari.
- **US-7** (visiteur) — à la fin d'un cours ou d'un entraînement, je m'envoie la suite sur
  WhatsApp ; le lien me ramène au chapitre.
- **US-8** (visiteur ou élève) — j'ai réussi : je partage ma réussite ; le lien montre l'aperçu du
  chapitre.
- **US-9** (élève) — j'invite mon parent en un geste : il reçoit un message qui ouvre mon bilan,
  code déjà rempli.
- **US-10** (parent sans compte) — mon bilan affiché, on me propose de garder le suivi sur mon
  écran d'accueil.

#### Flux écran par écran

**Écran de résultat connecté** (`quest-result-screen` via `quest.$exerciseId.tsx`) — sous les
actions existantes, **une seule** carte d'invitation au plus, choisie dans cet ordre : rappel
(US-3) → installation (US-5/6) → inviter son parent (US-9). États : `loading` du push ⇒ rien ;
permission `denied` ⇒ la carte de rappel n'apparaît pas (le paramétrage explique déjà comment
débloquer) ; erreur d'enregistrement ⇒ toast `pushNotifications.errorGeneric`, carte refermée.

**Écran de résultat sans compte** (`exercice.$exerciseId.tsx`) — entre les boutons « Recommencer ·
Retour à la matière » et l'invitation au compte : une rangée **« Garder ce chapitre »** avec au
plus deux gestes — « M'envoyer la suite » (US-7) et, sur réussite, « Partager ma réussite »
(US-8) — puis, sur réussite seulement et si elle est proposable, la carte d'installation
(US-5/6). L'invitation au compte reste en dernier, inchangée.

**Bas d'un cours sans compte** (`lesson-reader.tsx`) — « M'envoyer ce cours » au-dessus de
l'invitation au compte (US-7). Pas de carte d'installation ici : lire n'est pas une réussite.

**`/suivi`, bilan affiché** — carte d'installation, texte parent (US-10).

**Hall et Paramétrage** — la carte de rappel du hall change de texte (R-5) ; la ligne « Code
Alliance » du paramétrage gagne « Inviter mon parent » (US-9).

Tout est mobile d'abord ; en RTL les icônes directionnelles se retournent (`rtl:-scale-x-100`,
`check-rtl-classes`).

### 2.2 Règles métier

**La mesure**

- **R-1** — La mémoire de visite vit **sur l'appareil** : `localStorage["na9ra.visit"] =
{ first: "AAAA-MM-JJ", last: "AAAA-MM-JJ" }` (jour de Tunis, `appLocalDate`). Elle n'est jamais
  envoyée. Stockage indisponible ⇒ aucun événement de visite (sens sûr : on sous-compte).
- **R-2** — Au premier rendu client d'une session de navigation : mémoire absente ⇒ écrire
  `first = last = aujourd'hui` et émettre `visit_first{entry_surface, standalone}` ; mémoire
  présente et `last < aujourd'hui` ⇒ émettre `visit_returned{days_bucket, has_account, entry,
standalone}` puis `last = aujourd'hui`. Au plus un événement de visite par jour et par appareil.
- **R-3** — `days_bucket` ∈ `"1" | "2-7" | "8-30" | "31+"` : jamais le nombre exact, jamais la
  date. `entry_surface` ∈ `chapitre | exercice | matiere | niveau | accueil | test | suivi |
compte | autre` (déduit du chemin, jamais l'URL). `entry` ∈ `pwa | push | resume_link | share |
direct` (paramètre `?src=` lu puis retiré de l'URL par `history.replaceState`). `has_account`
  est un booléen de session.
- **R-4** — Zéro donnée personnelle : aucune propriété ne porte d'identifiant de compte, de
  chapitre, de score ou de texte saisi. Le test de propriétés de é31 (liste blanche de types) est
  étendu aux quatre événements neufs.

**Le rappel**

- **R-5** — Un rappel se propose **en gain** (é31 R-20). Texte de la carte : titre « Ton plan du
  jour, sans y penser », corps « El Ostedh te prévient une fois par jour au plus : ton plan est
  prêt, ta série continue, ta ligue est comptée. Tu coupes quand tu veux. » Le mot « danger »
  quitte `pushNotifications.cardDesc`.
- **R-6** — Sur l'écran de résultat, la carte de rappel n'apparaît que si **toutes** ces
  conditions tiennent : la quête est réussie (seuil de réussite de l'écran, pas de nouveau
  seuil) ; `usePush().state === "default"` ; elle n'a pas été montrée depuis 7 jours ; elle n'a
  pas été refusée deux fois. Deux « Plus tard » ⇒ elle ne revient **jamais** sur cet écran (elle
  reste au paramétrage). Mémoire : `localStorage["na9ra.nudge"]` (R-12).
- **R-7** — Le premier push qu'un élève reçoit après avoir accepté ne peut pas être un reproche :
  l'ordre de `PUSH_PRIORITY` est inchangé, et l'audience neuve `first-quest` se range en
  **avant-dernière** position (devant `comeback`).
- **R-8** — Garde-fou de harcèlement, inchangé et réaffirmé : au plus un push par élève et par
  jour (é31 R-4), tenu par `resolveDailyPushPlan`. `first-quest` part à J+1 et à J+3 de
  l'inscription, **jamais après** ; un élève qui a joué n'y est plus. Aucune audience ne se
  répète au-delà de ce que son ancrage sur une date exacte permet.
- **R-9** — Singulier : `{n} = 1` donne « ta série d'un jour continue » / « elle s'est arrêtée à
  un jour » dans les trois langues ; `payloadFor` porte la règle, comme pour `tutor-daily-plan`.
- **R-10** — `first-quest` ramène à `/dashboard` (la prochaine action y est unique, é22) ; texte
  FR : « 🎯 Ta première quête est prête — Cinq questions, quelques minutes, et tes premiers XP. »
  Jamais « tu n'as pas encore… ».

**L'installation**

- **R-11** — L'invitation à installer n'apparaît qu'**après une réussite** (quiz ou mission
  réussis, connecté ou non) ou sur un bilan parent affiché ; jamais à l'arrivée, jamais sur un
  échec, jamais si l'application tourne déjà installée (`display-mode: standalone` ou
  `navigator.standalone`).
- **R-12** — Mémoire commune des invitations : `localStorage["na9ra.nudge"] = { [kind]: { shown:
"AAAA-MM-JJ", dismissed: n } }`, `kind` ∈ `push | install | parent`. Règle unique : pas deux
  fois en 14 jours (7 pour `push`), deux refus ⇒ plus jamais, et **une seule invitation par
  écran** (ordre : rappel, installation, parent). Stockage indisponible ⇒ aucune invitation.
- **R-13** — Android / Chromium : l'événement `beforeinstallprompt` est retenu à son passage ; la
  carte n'existe que s'il a été reçu ; le bouton appelle `prompt()`. iPhone / iPad Safari : la
  carte montre les deux gestes (« Partager », puis « Sur l'écran d'accueil »), sans bouton
  d'action. Tout autre cas (navigateur intégré d'une messagerie, bureau sans événement) : rien.
- **R-14** — Le manifeste déclare `start_url: "/?src=pwa"`, un `id` stable (`"/"`) et une
  description à jour (elle parle encore des seuls concours 6ᵉ et 9ᵉ). `scope` inchangé.

**Le lien et le partage**

- **R-15** — « M'envoyer la suite » ouvre la feuille de partage du système, ou à défaut
  `https://wa.me/?text=…` : le visiteur choisit lui-même le destinataire (lui, son parent, un
  camarade). **Rien n'atteint nos serveurs** ; aucun numéro, aucune adresse n'est demandé.
- **R-16** — Le lien partagé est l'URL canonique du chapitre (jamais celle de l'exercice : un
  lien doit ramener à un endroit qui a du sens à froid) suivie de `?src=resume_link` ou
  `?src=share`. Texte « reprise » : « 📚 {chapitre} — {matière}. Je reprends ici : {url} ».
  Texte « réussite » : « ✅ {chapitre} — {bonnes}/{total} au quiz sur Na9ra Nal3ab. À toi : {url} ».
- **R-17** — « Partager ma réussite » n'existe que sur une réussite ; un échec ne se partage pas,
  et aucun texte ne compare l'élève à un autre. Aucun prénom, aucun pseudo dans le texte.
- **R-18** — Une seule implémentation du geste : `shareText` (feuille de partage → WhatsApp →
  copie) remplace les trois copies existantes (`suivi.tsx`, `parent-report.tsx`,
  `placement-bilan.ts`), sans changer leur comportement.

**Le parent**

- **R-19** — « Inviter mon parent » partage : « 👋 Je révise sur Na9ra Nal3ab. Tu peux suivre mon
  travail ici, sans compte : {SITE_URL}/suivi?code={code}&src=share ». Le code Alliance est une
  clé au porteur, déjà transmise ainsi aujourd'hui (copier-coller) ; le texte d'aide le redit
  (« ce lien ouvre ton bilan : envoie-le seulement à ton parent »).
- **R-20** — La carte « Inviter mon parent » sur l'écran de résultat n'apparaît qu'à un élève
  **sans lien parent actif**, après la carte de rappel et celle d'installation dans l'ordre de
  R-12 ; elle est permanente au paramétrage.

**Transverse**

- **R-21** — Aucun mot « premium », « abonnement », « payant » ; aucun compte à rebours, aucune
  rareté, aucun tirage. Aucune invitation ne bloque l'écran ni ne retarde une action.

### 2.3 i18n

FR / EN / AR pour chaque chaîne. Les chaînes publiques vont dans `fr-public.ts` / `en-public.ts` /
`ar-public.ts` (`public.keep.*`, `public.install.*`) ; celles du rappel restent sous
`pushNotifications.*` ; « Inviter mon parent » sous `settings.*`. Les textes de push vivent dans
`push-copy.ts` (type `Record<PushTag, Record<Locale, Copy>>` : une langue manquante ne compile
pas). **Budget** : `i18n-fr-` est à 60,94 Ko pour 64 — l'exécuteur mesure avant et après
(`build:check`) ; si le lot 3 ou 4 déborde, il sort les chaînes d'installation dans un catalogue
`install` chargé avec le composant, sur le modèle de `placement/`, plutôt que de relever le
plafond. RTL : les deux pictogrammes iOS sont des icônes, pas des flèches de direction.

### 2.4 Hors périmètre (v1)

Push sans compte · e-mail · SMS · WhatsApp Business / envoi serveur · cache hors ligne · badge
d'application (`setAppBadge`) · raccourcis de manifeste · page publique de résultat partagé ·
classement public · toute nouvelle récompense liée à l'installation ou au partage (un geste payé
devient une tâche — é31 R-18).

## 3. Architecture technique (décisions fermées)

### 3.1 Modèle de données

**Aucune table nouvelle.** Deux migrations additives, à trier après la dernière de `main`.

**Migration A (lot 0) — `admin_return_overview()`.**

```sql
CREATE OR REPLACE FUNCTION public.admin_return_overview()
RETURNS JSONB
LANGUAGE plpgsql STABLE SECURITY DEFINER SET search_path = public
AS $$
-- Garde : IF NOT public.is_admin() THEN RAISE EXCEPTION 'Unauthorized'; END IF;
-- Rend :
-- { "cohorts": [ { "week": date, "signups": int, "confirmed": int,
--                  "played_7d": int, "played_7d_base": int,
--                  "back_7d": int, "back_7d_base": int } … 8 semaines ],
--   "never_played": int,              -- élèves sans aucun jour d'activité
--   "push": { "students_active_30d": int, "students_reachable": int,
--             "parents_linked": int, "parents_reachable": int } }
$$;
REVOKE EXECUTE ON FUNCTION public.admin_return_overview() FROM PUBLIC, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.admin_return_overview() TO authenticated; -- la garde is_admin() tranche
```

Définitions arrêtées : cohorte = semaine d'inscription (lundi, jour de Tunis), rôle `student`,
huit semaines ; `confirmed` = `auth.users.email_confirmed_at IS NOT NULL` ; `played_7d` = au moins
un jour dans `eng_activity_days` entre J et J+7 **inclus le jour J** (c'est la première quête, pas
un retour) ; `back_7d` = au moins un jour entre J+1 et J+7 (la définition de KPI-B, reprise telle
quelle) ; les `_base` ne comptent que les comptes dont la fenêtre est écoulée ; `reachable` = au
moins une ligne dans `push_subscriptions`. Fonction **séparée** de `admin_engagement_overview`, à
dessein : celle-ci fait quatre cents lignes et trois études l'ont déjà ré-émise (é34 §3.7).

**Migration B (lot 2) — `push_daily_audiences` gagne une branche.** Ré-émission par script depuis
la révision vivante (`20260902160000`), une `UNION ALL` ajoutée, rien de retiré :

```sql
  UNION ALL
  -- 7) LA PREMIÈRE QUÊTE — inscrit hier ou il y a trois jours, jamais actif.
  SELECT pr.id, 'first-quest'::TEXT, pr.locale, NULL, NULL
    FROM public.profiles pr
   WHERE pr.role = 'student'
     AND pr.last_active_date IS NULL
     AND (pr.created_at AT TIME ZONE 'Africa/Tunis')::date IN (p_today - 1, p_today - 3)
```

L'ancrage sur deux dates exactes tient « deux fois, puis plus jamais » sans colonne d'état — le
patron de `comeback`.

**Mémoire d'appareil** (aucune n'atteint le serveur) :

| Clé           | Contenu                                                             | Durée                                          | Écrite par   |
| ------------- | ------------------------------------------------------------------- | ---------------------------------------------- | ------------ |
| `na9ra.visit` | `{ first, last }` — deux jours civils                               | sans limite ; effacée avec les données du site | lot 0        |
| `na9ra.nudge` | `{ push?, install?, parent? }` — dernier affichage, nombre de refus | idem                                           | lots 2, 3, 5 |

L'exécuteur du lot 0 décrit la « mémoire de visite » dans `docs/inventaire-traitements-inpdp.md`,
à la suite du paragraphe qui décrit déjà la mémoire d'appareil du test de niveau (même statut :
hors serveur, sans identité).

### 3.2 Server

- `getReturnOverview` — `createServerFn` + `requireSupabaseAuth`, appelle `admin_return_overview`,
  valide par zod, dans `src/features/dashboard/engagement.server.ts` (à côté de la lecture
  existante). Pas d'entrée.
- `/api/health` gagne un champ `push: "configured" | "unconfigured"` : `configured` si les trois
  variables serveur VAPID et `CRON_SECRET` sont présentes. Aucune valeur n'est rendue.
- `handlePushCron` : inchangé, hors l'arrivée du tag `first-quest` dans `PUSH_PRIORITY` et
  `PUSH_COPY`.
- Script `reports:engagement` : lit `admin_return_overview` en plus, ajoute trois lignes au
  relevé (#962) : première quête, portée du push, jamais joué.

### 3.3 Client

```
src/shared/lib/visit-memory.ts           R-1…R-3 : lire, écrire, classer (pur, testable, horloge injectée)
src/shared/lib/nudge-memory.ts           R-12 : canShow(kind, today) · markShown · markDismissed
src/shared/lib/install-prompt.ts         R-13 : retient beforeinstallprompt, expose getInstallMode()
                                         → "native" | "ios" | "none" ; promptInstall()
src/shared/lib/share-text.ts             R-18 : shareText(text) → "share" | "whatsapp" | "copy" | "none"
src/shared/lib/entry-source.ts           R-3 : lit ?src=, le retire de l'URL, le rend à visit-memory
src/components/public/install-invite.tsx la carte (variantes native / ios ; textes élève / parent)
src/components/public/keep-row.tsx       « M'envoyer la suite » · « Partager ma réussite »
src/features/notifications/components/enable-push-card.tsx   variante `moment="victory"` (R-6)
src/features/quest/components/quest-result-nudges.tsx        choisit UNE carte (R-12) ; reçoit en
                                         props les cartes déjà montées par la route (aucun import
                                         entre features)
```

- Le déclenchement de la mesure (R-2) part de `__root.tsx`, à côté de l'enregistrement du service
  worker, **après** l'hydratation, par un import dynamique : zéro octet dans `index-` au-delà de
  l'appel (budget #1250, RISK-5).
- `install-prompt.ts` pose son écouteur dès le chargement du module partagé de la coquille
  publique **et** de la coquille connectée (l'événement ne passe qu'une fois par page).
- `quest.$exerciseId.tsx` (route) compose : `EnablePushCard moment="victory"` (feature
  notifications), `InstallInvite` (composant), la carte parent ; c'est la route qui importe les
  deux features, comme aujourd'hui pour `TutorPanel`.
- `/admin/engagement` : un bloc « Le retour » (cohortes première quête / retour, portée du push,
  jamais joué), états vide et erreur par bloc.

### 3.4 Sécurité & anti-abus

- Le paramètre `?src=` est comparé à une liste fermée de cinq valeurs ; toute autre valeur vaut
  `direct`. Il n'est jamais rendu dans la page.
- Les textes partagés sont construits à partir de titres de catalogue et de compteurs ; aucun
  texte saisi par l'utilisateur n'y entre. `encodeURIComponent` sur tout ce qui va dans `wa.me`.
- `/suivi?code=` existe déjà (lien au porteur assumé, `suivi.tsx:22-33`) ; R-19 ne change pas sa
  surface, il rend le geste accessible.
- `admin_return_overview` : `SECURITY DEFINER` + garde `is_admin()`, révoquée d'`anon`.
- CSP : aucun hôte nouveau (`wa.me` est une navigation, pas un `connect-src`).
- Mineurs : aucune invitation ne collecte quoi que ce soit ; la permission de notification reste
  le dialogue du navigateur, demandé **après** un geste explicite sur notre carte, jamais au
  chargement.

### 3.5 Intégrations & env

`VITE_VAPID_PUBLIC_KEY` (build) doit égaler `VAPID_PUBLIC_KEY` (serveur) — déjà documenté
(`docs/environment-variables.md` §push), jamais posé en production. Aucune variable nouvelle.
Aucun prestataire nouveau. Optionnel, Q-2 : `POSTHOG_PERSONAL_API_KEY` en secret GitHub pour que
le relevé hebdomadaire lise KPI-1 et KPI-5.

### 3.6 Observabilité

Quatre événements entrent dans la liste fermée (`product-events.ts`), chacun avec son
consommateur daté :

| Événement        | Propriétés                                                                                              | Consommateur                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `visit_first`    | `entry_surface`, `standalone`                                                                           | KPI-1 (dénominateur), dès le lot 0                      |
| `visit_returned` | `days_bucket`, `has_account`, `entry`, `standalone`                                                     | KPI-1 ; lecture par `entry` pour juger les lots 3, 4, 5 |
| `install_invite` | `action` (`shown`/`accepted`/`dismissed`), `platform` (`native`/`ios`), `audience` (`student`/`parent`) | KPI-5, lot 3                                            |
| `content_shared` | `intent` (`resume`/`success`/`parent`), `surface`, `method`                                             | lots 4 et 5 ; rapproché de `visit_returned{entry}`      |

`push_optin` gagne une propriété `moment` (`victory` / `hall` / `settings` / `parent`).
Journal serveur : `Push cron complete` porte déjà `byTag` ; rien à ajouter.

### 3.7 Décisions d'architecture (ADR)

- **D-1 — Le retour du visiteur se mesure par un fait calculé sur l'appareil, pas par une
  identité.** L'appareil sait s'il est déjà venu ; il envoie « je reviens, 2 à 7 jours » et rien
  d'autre. Rejeté : activer les profils PostHog (décision de protection des mineurs, é31 D-1) ;
  un compteur en base alimenté par un point d'écriture public (une table, une surface d'abus, et
  les robots gonflent le chiffre) ; GA4 « utilisateurs connus » (dépend d'un cookie tiers à la
  politique duquel on ne commande pas).
- **D-2 — Une fonction d'admin neuve plutôt qu'une sixième ré-émission de
  `admin_engagement_overview`.** Le coût d'une ré-émission est documenté (é34) ; la lecture neuve
  est indépendante et se teste seule.
- **D-3 — Pas de push sans compte.** Il faudrait rendre `push_subscriptions.user_id` nullable et
  garder l'identifiant de notification d'un mineur qui n'a rien signé ni rien confirmé : une
  donnée personnelle de plus, sans personne à qui la rattacher pour l'effacer (GAP-024), pendant
  que le dossier INPDP est en cours. L'installation et le lien de reprise couvrent le même besoin
  sans rien stocker.
- **D-4 — Le lien de reprise ne passe par aucun serveur.** Rejeté : un champ « ton numéro » ou
  « ton e-mail » (collecte chez des mineurs, envoi à payer, canal à administrer). La feuille de
  partage du téléphone fait le travail, et « s'envoyer un message à soi-même » est un usage
  courant de WhatsApp.
- **D-5 — Une invitation par écran, mémoire commune.** Trois cartes empilées sous un résultat
  seraient exactement le harcèlement que le garde-fou interdit. Rejeté : laisser chaque carte
  gérer sa propre fréquence (trois règles qui divergent — la leçon d'`auth-refusals.ts`).
- **D-6 — `beforeinstallprompt` sans dépendance.** Rejeté : `vite-plugin-pwa` (c'est é06) ; une
  bibliothèque d'invitation (octets dans `index-`). Vingt lignes suffisent.
- **D-7 — `first-quest` est une audience, pas un e-mail.** Elle ne touche que ceux qui ont
  accordé le push avant de jouer — peu de monde. C'est assumé : le vrai remède de G-3 est en
  amont (é38 lots 1 et 2, qui ramènent l'inscrit sur la quête qu'il a quittée) et se **lit** par
  KPI-2. Si KPI-2 reste sous 50 % quatre semaines après le lot 0, la suite est Q-4, pas une
  audience de plus.
- **D-8 — Le lien partagé pointe le chapitre, pas l'exercice.** Un exercice ouvert à froid, sans
  le cours, est une impasse pour celui qui reçoit le lien ; le chapitre porte l'aperçu de partage
  (#1247) et la règle « cours → quiz → missions ».

## 4. Plan d'exécution en lots

| lot | contenu (résumé)                                                                                                                   | fichiers/objets créés ou touchés                                                                                                                                                                    | tests exigés                                                                                                                                                                                  | dépend de       |
| --- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 0   | La mesure du retour : `visit_first` / `visit_returned`, `admin_return_overview`, bloc console, trois lignes au relevé              | `visit-memory.ts`, `entry-source.ts`, `product-events.ts`, `__root.tsx`, migration A, `engagement.server.ts`, `engagement-admin.tsx`, script `reports:engagement`, inventaire INPDP                 | Vitest : classement des jours, un événement par jour, stockage absent, `?src=` hostile, zéro PII ; pgTAP : garde admin, cohortes, fenêtres non écoulées ; `db:check-chain`                    | —               |
| 1   | Le push se prouve : `push` dans `/api/health`, garde de build, assertion nocturne (le geste Vercel est le prérequis P-0, hors lot) | `src/server.ts` (santé), script de garde de build, workflow nocturne public, `docs/environment-variables.md` (le constat après coup)                                                                | Vitest : santé ; garde de build (échoue si la clé manque en production)                                                                                                                       | —               |
| 2   | Le rappel après une victoire, en gain ; singulier ; audience `first-quest` — **famille B**                                         | `nudge-memory.ts`, `enable-push-card.tsx`, `use-push.ts` (`moment`), `quest-result-nudges.tsx`, `quest.$exerciseId.tsx`, `push-copy.ts`, `push-audience.ts`, migration B, i18n                      | Vitest : R-6 (quatre conditions), deux refus, R-9, priorité de `first-quest` ; pgTAP : J+1, J+3, jamais J+2 ni J+4, jamais un élève actif                                                     | 1 ; effet : P-0 |
| 3   | L'invitation à installer après une réussite                                                                                        | `install-prompt.ts`, `install-invite.tsx`, `exercice.$exerciseId.tsx`, `quest.$exerciseId.tsx`, `suivi.tsx`, `_public.tsx`, `_authenticated.tsx`, `manifest.webmanifest`, `product-events.ts`, i18n | Vitest : modes native / ios / none, standalone, R-11, R-12 ; e2e `public-anon` : événement simulé ⇒ carte après réussite, absente après échec ; `build:check` + `smoke:shell`                 | 0               |
| 4   | Le lien de reprise et le partage d'une réussite                                                                                    | `share-text.ts`, `keep-row.tsx`, `exercice.$exerciseId.tsx`, `lesson-reader.tsx`, `suivi.tsx`, `parent-report.tsx`, `placement-bilan.ts`, `product-events.ts`, i18n                                 | Vitest : textes R-16 dans les trois langues, R-17, repli partage → WhatsApp → copie, non-régression des trois appelants ; e2e `public-anon` : lien ouvert ⇒ chapitre, `?src=` retiré de l'URL | 0               |
| 5   | Le parent dans la boucle : « Inviter mon parent », installation sur `/suivi`                                                       | `parametrage.tsx`, `quest-result-nudges.tsx`, `quest.$exerciseId.tsx`, `suivi.tsx`, i18n                                                                                                            | Vitest : R-19 (texte, lien), R-20 (lien actif ⇒ pas de carte), ordre R-12 ; e2e `authed` : le lien ouvre `/suivi` avec le bilan                                                               | 3, 4            |
| 6   | _Gelé (doctrine verticale)_ — un défi de la semaine visible avant le compte                                                        | —                                                                                                                                                                                                   | —                                                                                                                                                                                             | Q-3             |

#### Le prérequis P-0 — le geste Vercel (propriétaire, remonté le 2026-11-12)

> ✅ **Fait le 2026-11-13** (accès Vercel accordé par le propriétaire à la session de l'étude) —
> voir le journal §8. Les cinq variables sont posées dans le projet `na9ranal3ab` (celui qui sert
> `www`) ; la production les sert depuis 09:13 UTC.

Ce n'est pas un lot : aucune session du jour n'a l'accès à l'équipe Vercel (403), et
`zero-intervention.md` range ce cas parmi les gestes qui restent au propriétaire. Il conditionne
**l'effet** — pas la fusion — de tout ce qui repose sur le push.

- **Le geste** : Vercel → Settings → Environment Variables, environnement Production — les cinq
  variables de `docs/environment-variables.md` § Web Push : `VAPID_PUBLIC_KEY`,
  `VAPID_PRIVATE_KEY`, `VAPID_SUBJECT`, `CRON_SECRET`, et `VITE_VAPID_PUBLIC_KEY` **égale à**
  `VAPID_PUBLIC_KEY` (paire absente : `npx web-push generate-vapid-keys`, une fois) ; puis
  **redéployer sans cache de build** — la clé publique s'incruste à la compilation.
- **La cible et le plafond** (rapporté par la session orchestratrice le 2026-11-12, non constaté
  par celle-ci, qui n'a pas l'accès Vercel) : le dépôt du moteur se déploie dans **deux** projets
  Vercel (`na9ranal3ab` et `yahia-quest-arena`). Le geste vise **celui qui sert
  `www.na9ranal3ab.tn`** — poser la clé dans l'autre ne change rien. Et le redéploiement compte
  dans le plafond du plan (100 déploiements par jour, épuisé le 2026-11-12 à 09:06 UTC par la
  vague de sessions : production figée sur l'état de ~08:55 UTC jusqu'à la reprise) : P-0 se fait
  **après** la reprise, en un seul redéploiement.
- **Le constat après coup**, dans cet ordre : (1) le chunk `assets/enable-push-card-*.js` servi par
  `www` ne contient plus `useEffect(()=>{g()?t("unconfigured")…` mais la branche qui lit la
  permission ; (2) connecté, la carte « Rappels » est visible au bas du hall ; (3) après une
  activation réelle, `push_subscriptions` et `push_consent_events` comptent chacune une ligne
  (agrégat, lecture seule) ; (4) la réponse du cron du soir porte `audience` ≥ 1. Une fois le
  lot 1 fusionné, `/api/health` rend `push:"configured"` et le nightly le vérifie chaque nuit.

#### Deux familles de lots

| Famille                                                                                  | Lots                                                                                                                                                                                                                        | Ce qui les distingue                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **A — aucun geste du propriétaire** : exécutables et **utiles** dès la fusion de l'étude | **0** (mesure du retour) · **1** (sonde et gardes du push — elles disent « éteint » tant que P-0 n'est pas fait, et c'est leur rôle) · **3** (installation) · **4** (lien de reprise, partage) · **5** (inviter son parent) | rien n'y dépend d'une variable, d'un prestataire ni d'une question ouverte                                                                                                                                   |
| **B — attendent le push (P-0)** pour avoir un effet                                      | **2** (rappel après une victoire, singulier, audience `first-quest`)                                                                                                                                                        | fusionnable avant P-0 sans risque — la carte reste masquée tant que la clé manque, l'audience ne trouve aucune souscription — mais **sans effet** ; ses critères en production ne se constatent qu'après P-0 |
| **Gelé**                                                                                 | **6** (défi de la semaine avant le compte)                                                                                                                                                                                  | attend Q-3 — une ouverture de capacité ne se lance pas sans arbitrage (P-7)                                                                                                                                  |

L'audience « compte créé, jamais joué » (`first-quest`, migration B) est de la famille B par son
effet : elle ne joint que des élèves ayant accordé le push. Sa partie **mesure** — combien
d'inscrits n'ont jamais joué — est dans le lot 0 (KPI-2), famille A.

**Contrainte de livraison (incident du 2026-11-12).** Chaque push au moteur crée un déploiement
dans chacun des deux projets Vercel, sous un plafond quotidien que dix sessions simultanées ont
épuisé en une matinée. Ce plan se livre donc en **peu de PR, complètes** : un lot = une PR = un
push final (les points de sauvegarde restent locaux, ou sur une branche `wip/` si elle ne
déclenche pas de prévisualisation) ; au plus deux lots en vol à la fois ; et **une vérification en
production groupée** par vague, une fois les PR de la vague fusionnées et le déploiement constaté
— pas une sonde par session. Un lot fusionné n'est dit « en ligne » qu'après ce constat ; d'ici
là il est « fusionné le AAAA-MM-JJ, en ligne à la reprise du déploiement ».

**Ordre.** 0 et 1 partent ensemble (fichiers disjoints). 2 suit 1 (et P-0 pour son effet). 3 et 4 suivent 0 et peuvent
aller en parallèle **si** `exercice.$exerciseId.tsx` est réparti : le lot 4 y monte `KeepRow`, le
lot 3 y monte `InstallInvite` — deux insertions voisines dans `renderResultFooter` ; le second à
fusionner rebase. 5 en dernier.

**Collisions à connaître le 2026-11-12** : é38 lot 5 (moteur #1268, en cours de fusion ce jour)
touche `index.tsx`, `programme.tsx`,
`chapitre.$chapterId.tsx`, `subject-hub.tsx`, `anon-quiz-gate.ts` — **aucun** fichier des lots 0 à
2 ; `exercice.$exerciseId.tsx` et `lesson-reader.tsx` (lots 3 et 4) sont à vérifier contre sa PR.
é08 lot 2 touche `notifications.cron.server.ts` et `parent-report.tsx` : le lot 2 d'ici ne touche
que `push-copy.ts` / `push-audience.ts`, et le lot 4 retouche `parent-report.tsx` (une ligne :
l'appel à `shareText`) — à passer après la fusion de é08 lot 2.

- [x] **Lot 0 — La mesure du retour** (livré, moteur #1294).
      **Périmètre** : R-1 à R-4 ; migration A ; `getReturnOverview` ; bloc « Le retour » de
      `/admin/engagement` ; trois lignes au relevé hebdomadaire ; les quatre événements déclarés
      au catalogue — `visit_first` et `visit_returned` en `live: true`, `install_invite` et
      `content_shared` en `live: false` avec le lot qui les câblera ; ligne à l'inventaire INPDP.
      **Critères** (US-1) : première ouverture d'un navigateur neuf ⇒ un `visit_first`, aucun
      `visit_returned` ; réouverture le même jour ⇒ rien ; le lendemain ⇒ un `visit_returned
  {days_bucket:"1"}` ; `localStorage` jeté ⇒ rien n'est émis et rien ne casse ;
      `/?src=pwa` ⇒ `entry:"pwa"` et l'URL affichée redevient `/` ; `/admin/engagement` affiche
      huit cohortes avec « mesurable » distingué de « perdu » ; le relevé dit « première quête :
      x/y ». `index-` ne grossit pas de plus de 1 Ko.
      **Tests** : ceux du tableau ; pgTAP avec une cohorte dont la fenêtre n'est pas écoulée (elle
      ne compte pas comme perdue) et un compte non confirmé.
      **Stop-point** : aucune carte, aucun bouton, aucun changement d'écran hors la console admin ;
      `resume_card_clicked`, `public_practice_started` et `public_gate_shown` ne sont ni
      redéclarés ni modifiés — le lot ajoute ses quatre lignes au catalogue tel qu'il le trouve.
- [ ] **Lot 1 — Le push se prouve** (famille A).
      **Périmètre** : (a) `push` dans `/api/health` — `configured` si les quatre variables
      serveur sont présentes, aucune valeur rendue ; (b) une garde de build — `build:check`
      échoue quand `VERCEL_ENV=production` et que `VITE_VAPID_PUBLIC_KEY` est vide ; (c) une
      assertion dans le nightly public : `/api/health` rend `push:"configured"` — elle tient
      l'issue du nightly ouverte tant que P-0 n'est pas fait, puis veille ; (d) le « constat
      après coup » de P-0 recopié dans `docs/environment-variables.md` § Web Push, et la panne
      aux leçons de `STATUS.md` §8 (la ligne du §3 est corrigée par la session orchestratrice du
      2026-11-12).
      **Critères** (US-2) : `/api/health` dit `unconfigured` avant P-0 et `configured` après ;
      retirer la clé d'un build de production fait rougir `build:check` ; le nightly porte
      l'assertion.
      **Tests** : Vitest sur le champ de santé (quatre variables présentes / une absente) ; test
      du script de garde.
      **Stop-point** : aucun texte, aucun emplacement de carte ne change (c'est le lot 2) ; le lot
      ne pose aucune variable et ne contourne pas P-0. ⚠️ La garde (b) rougit le déploiement de
      production tant que P-0 n'est pas fait : elle se fusionne **après** P-0, ou en
      avertissement d'abord puis en échec — à l'exécuteur de constater l'état de P-0 avant de
      choisir, et de l'écrire dans sa PR.
- [ ] **Lot 2 — Le rappel après une victoire** (famille B — effet après P-0).
      **Périmètre** : R-5 à R-10, R-12 pour `push` ; migration B ; `first-quest` dans
      `PUSH_PRIORITY` (avant-dernier) et `PUSH_COPY` (trois langues) ; `push_optin{moment}`.
      **Critères** (US-3, US-4) : quête réussie, permission jamais demandée ⇒ la carte paraît sous
      les actions ; « Activer » ⇒ dialogue du navigateur ⇒ carte en état « activé » ; « Plus
      tard » deux fois ⇒ elle ne revient plus sur cet écran et reste au paramétrage ; quête ratée
      ⇒ jamais de carte ; permission `denied` ⇒ jamais de carte ; série d'un jour ⇒ texte au
      singulier dans les trois langues ; un inscrit de la veille sans activité est candidat
      `first-quest`, plus celui d'il y a deux jours ni celui qui a joué ; un élève candidat à
      `first-quest` et à autre chose reçoit l'autre.
      **Tests** : ceux du tableau, plus `enable-push-card.test.tsx` étendu au `moment`.
      **Stop-point** : pas de carte d'installation, pas de carte parent ; `quest-result-nudges`
      n'accueille que le rappel et **prévoit** les deux emplacements suivants sans les remplir.
- [x] **Lot 3 — L'invitation à installer** (livré, moteur #1298, #1299).
      **Périmètre** : R-11 à R-14 ; `install_invite` passe `live: true`.
      **Critères** (US-5, US-6, US-10) : Chromium Android, événement reçu, quiz anonyme réussi ⇒
      carte ; bouton ⇒ `prompt()` ; acceptation ⇒ `install_invite{action:"accepted"}` et la carte
      disparaît pour toujours ; refus ⇒ `dismissed`, pas avant 14 jours ; agent iPhone Safari,
      non installé ⇒ carte en deux gestes, sans bouton ; application déjà installée ⇒ rien ; quiz
      raté ⇒ rien ; `/suivi` avec bilan ⇒ carte au texte parent ; écran de résultat connecté :
      la carte d'installation ne paraît que si celle du rappel ne paraît pas ; le manifeste rend
      `start_url:"/?src=pwa"`.
      **Tests** : ceux du tableau ; `smoke:shell` (le manifeste et la coquille changent).
      **Stop-point** : aucune ligne dans `sw.js` au-delà de ce que le lot 4 de é38 y fait ; aucun
      cache ; pas de `vite-plugin-pwa`.
- [x] **Lot 4 — Le lien de reprise et le partage d'une réussite** (livré, moteur #1301).
      **Périmètre** : R-15 à R-18 ; `content_shared` passe `live: true`.
      **Critères** (US-7, US-8) : fin de quiz anonyme ⇒ « M'envoyer la suite » ; réussite ⇒
      « Partager ma réussite » en plus ; échec ⇒ pas de partage de réussite ; le texte porte le
      titre du chapitre dans la langue de l'interface et l'URL canonique `www` du **chapitre** ;
      sans feuille de partage ⇒ `wa.me` ; ni l'un ni l'autre ⇒ copie et confirmation ; ouvrir le
      lien ⇒ le chapitre, `visit_returned{entry:"resume_link"}` si l'appareil est déjà venu,
      `?src=` retiré de l'URL ; les trois appelants historiques se comportent comme avant.
      **Tests** : ceux du tableau.
      **Stop-point** : rien n'atteint le serveur ; aucun champ de saisie ; pas de page de résultat
      partagé.
- [ ] **Lot 5 — Le parent dans la boucle.**
      **Périmètre** : R-19, R-20 ; troisième emplacement de `quest-result-nudges`.
      **Critères** (US-9) : paramétrage ⇒ « Inviter mon parent » à côté de « Copier » ; le message
      porte `/suivi?code=…&src=share` ; un élève avec lien parent actif ne voit pas la carte sur
      l'écran de résultat ; ouvrir le lien sans compte ⇒ bilan affiché, code proposé à la
      mémorisation ; `content_shared{intent:"parent"}` part.
      **Tests** : ceux du tableau.
      **Stop-point** : rien sur le digest (é08 lot 2), rien sur l'inscription parent.
- [ ] **Lot 6 — gelé.** Attend Q-3.

## 5. Stratégie de test

- **Vitest, co-localisés** : `visit-memory`, `nudge-memory`, `install-prompt`, `share-text`,
  `entry-source` sont des modules purs à horloge et stockage injectés — chaque règle R-x y a son
  test nommé. Les composants se testent sur leurs états (rien / native / ios ; activé / plus tard).
- **pgTAP** : `admin_return_overview` (garde, définitions, fenêtres) ; `push_daily_audiences`
  (les sept branches, dont la neuve, et la non-régression des six autres par un jeu de données
  commun).
- **e2e (projet TEST, jamais la production)** : `public-anon` pour les lots 3 et 4
  (`beforeinstallprompt` simulé par `page.evaluate`, `navigator.share` absent ⇒ lien `wa.me`
  intercepté) ; `authed` pour les lots 2 et 5 (permission accordée par
  `context.grantPermissions`).
- **`build:check` + `smoke:shell`** : lots 1 et 3. **`check-rtl-classes`** : lots 2 à 5.
- **Non-régression** : `enable-push-card.test.tsx`, `use-push.test.ts`, `push-audience.test.ts`,
  `notifications.cron.test.ts`, `report-share.test.ts`, `placement-summary.test.tsx`, e2e
  `public-anon` existants restent verts sans retouche de leurs attentes.
- **Constat en production** (P-0 seulement, lecture seule plus une souscription de test par le
  propriétaire ou un compte de test) : c'est le seul critère de ce plan qu'aucune CI ne peut
  porter, et c'est celui qui a manqué : la table existe depuis le 2026-06-13 et n'a jamais reçu
  une ligne.

## 6. Risques & mitigations

- **RISK-1 — Le push rallumé, les rappels partent pour la première fois : un texte maladroit
  coupe le canal.** Probable / fort. Mitigation : le lot 2 corrige le singulier **avant** que le
  volume existe ; KPI-3 se lit avec le taux de coupure ; au-delà de 25 %, on relit avant d'ajouter.
- **RISK-2 — L'invitation à installer agace.** Possible / moyen. Mitigation : jamais avant une
  réussite, une invitation par écran, deux refus définitifs (R-11, R-12, D-5).
- **RISK-3 — Les navigateurs intégrés des messageries** (lien ouvert depuis Facebook, Instagram)
  n'émettent pas `beforeinstallprompt` et isolent leur stockage : ni invitation ni mémoire.
  Certain / moyen. Mitigation : sens sûr (rien ne s'affiche) ; `visit_first{entry_surface}` et
  `standalone` permettent de chiffrer la part concernée avant d'y investir.
- **RISK-4 — Le code Alliance circule dans un lien.** Possible / moyen. C'est déjà le cas
  (`/suivi?code=` existe, le code se copie) ; mitigation : le texte d'aide de R-19, et le fait que
  le lien n'ouvre qu'un bilan en lecture.
- **RISK-5 — Budget `index-`** (413 Ko pour 456, #1250). Faible / fort. Mitigation : import
  dynamique après hydratation pour la mesure ; les composants vivent dans les chunks de route ;
  critère chiffré au lot 0.
- **RISK-6 — `n` trop petit pour conclure.** Certain. Mitigation : les cibles de KPI-1 et KPI-5
  sont « instrument d'abord » ; aucun lot n'est jugé sur une semaine ; la décision de poursuivre
  se prend à quatre semaines, sur KPI-2 et KPI-3 qui se comptent en personnes.
- **RISK-7 — Deux sessions touchent le même écran de résultat le même jour.** Probable le
  2026-11-12. Mitigation : la table des collisions du §4 ; les lots 3 et 4 ne partent qu'après la
  fusion de é38 lot 5.
- **RISK-9 — Le plafond de déploiement fige la production pendant l'exécution du plan.** Constaté
  le 2026-11-12. Mitigation : la contrainte de livraison du §4 ; P-0 après la reprise.
- **RISK-8 — La mémoire de visite est lue comme un traceur.** Faible / fort (INPDP). Mitigation :
  elle ne quitte pas l'appareil, ne porte que deux jours civils, et entre à l'inventaire au lot 0.

## 7. Questions ouvertes (pour l'humain)

- **Q-1 — Le geste Vercel (P-0, §4).** Aucune session n'a l'accès à l'équipe Vercel : le geste
  est remonté au propriétaire le 2026-11-12 par la session orchestratrice. **Recommandation** : le
  faire avant tout le reste — cinq variables, un redéploiement sans cache, et le constat en quatre
  points du §4 ; ou autoriser le connecteur Vercel d'une session sur l'équipe, qui le fera.
  **Débloque** : l'effet du lot 2 et le bilan parent du dimanche de é08. Ne bloque aucun lot de
  la famille A.
- **Q-2 — Une clé de lecture PostHog en secret GitHub (`POSTHOG_PERSONAL_API_KEY`) ?**
  **Recommandation : oui**, en lecture seule sur le projet : le relevé du lundi (#962) dira alors
  KPI-1 et KPI-5 sans que personne ouvre PostHog. Sans elle, ces deux chiffres se lisent à la
  main dans PostHog. **Débloque** : rien d'obligatoire ; ferme la boucle du lot 0 (P-2).
- **Q-3 — Un rendez-vous hebdomadaire visible avant le compte (lot 6) ?** Forme sobre : « le défi
  de la semaine » — une mission du catalogue par classe de concours, tirée de façon déterministe
  du numéro de semaine, affichée sur l'accueil et sur la carte « Reprendre », du lundi au
  dimanche, sans classement ni donnée. C'est une **ouverture** de capacité. **Recommandation :
  geler** jusqu'à quatre semaines de KPI-1 ; la dégeler si le retour à 7 jours reste sous 10 %
  une fois les lots 3 et 4 en ligne. **Débloque** : le lot 6.
- **Q-4 — Un e-mail hebdomadaire pour les parents (opt-in, adultes seulement) ?** C'est le seul
  canal qui atteint un parent sans permission de notification ; il exige un prestataire d'envoi
  (un sous-traitant de plus à l'inventaire INPDP), un lien de désinscription et un gabarit.
  **Recommandation : pas maintenant** — décider après quatre semaines de KPI-3 côté parents ; si
  moins d'un parent lié sur trois est joignable par push, ouvrir une étude courte. Jamais pour
  les élèves. **Débloque** : rien dans ce plan.
- **Q-5 — Dégel partiel de é06 pour « l'application installée s'ouvre sans réseau sur le dernier
  cours lu » ?** L'installation (lot 3) rend ce manque visible : une icône qui ouvre une page
  « hors connexion ». **Recommandation : non pour l'instant** — lire d'abord KPI-5 ; si plus d'un
  visiteur sur dix accepte l'installation, rouvrir é06 sur ce seul périmètre. **Débloque** : rien
  dans ce plan.

## 8. Journal d'exécution

- **2026-11-12** — étude rédigée (brouillon). Relevé envoyé à la session orchestratrice du jour,
  qui répartit l'exécution des lots. Constat hors étude remonté le même jour : `STATUS.md` §3
  déclare les notifications push « 🟢 M3 » alors que la clé publique manque au build de production
  (T-1) — corrigé par la session orchestratrice, pas par celle-ci (qui ne modifie ni `STATUS.md` ni le
  code du moteur) ; le geste Vercel est remonté au propriétaire (P-0).
- **2026-11-12** — sur demande de la session orchestratrice : les lots sont classés en deux
  familles (§4), le geste Vercel devient le prérequis P-0, hors lot. Versés aussi : les deux
  projets Vercel et le plafond de déploiement atteint à 09:06 UTC (contrainte de livraison, §4),
  le volume sur quatorze jours (T-6), le relevé « première visite » et les trois événements déjà
  entrés au catalogue (T-5 bis).

- **2026-11-12 — lot 0 livré (moteur #1294).** La mesure du retour. Côté appareil (R-1 à R-4) :
  `visit-memory.ts` (`localStorage["na9ra.visit"] = { first, last }`, deux jours civils de Tunis,
  jamais envoyés ; stockage indisponible, plein ou illisible ⇒ aucun événement), `entry-source.ts`
  (`?src=` lu puis retiré de l'adresse ; surface d'arrivée déduite du chemin), `visit-beacon.ts`
  importé dynamiquement après l'hydratation depuis `__root` — `visit_first{entry_surface,
standalone}` ou `visit_returned{days_bucket, has_account, entry, standalone}`, au plus un par jour
  et par appareil. Catalogue : quatre lignes ajoutées après les existantes, `visit_first` et
  `visit_returned` câblés, `install_invite` (lot 3) et `content_shared` (lot 4) déclarés non câblés.
  Côté comptes : migration `20261112160000_admin_return_overview` (fonction neuve, `SECURITY
DEFINER`, garde `is_admin()`, séparée de `admin_engagement_overview`), `getReturnOverview`, le bloc
  « Le retour » de `/admin/engagement` (« mesurable », « en attente » et « perdu » sont trois
  colonnes), trois lignes au relevé hebdomadaire (première quête x/y, portée du push, jamais joué),
  la mémoire de visite à l'inventaire INPDP. pgTAP 112 (25 assertions). Stop-point tenu : aucun écran
  ne change hors la console admin.
  **Vérifié en production le 2026-11-13 (00:22 UTC, production sur `995c372`)**, Chromium, Pixel 7
  émulé, requêtes de mesure d'audience interceptées et bloquées par la sonde : un navigateur neuf
  arrivant sur `/programme?src=pwa` voit son adresse redevenir `/programme`, écrit `na9ra.visit` au
  jour de Tunis et émet un `visit_first`, un seul ; un rechargement n'émet rien ; la mémoire reculée
  de trois jours, l'ouverture de `/` émet un `visit_returned`. La migration est appliquée
  (`db-migrate-prod` vert sur le commit du lot, 20:30 UTC). **Non vérifié** : le bloc de la console
  et les valeurs de `admin_return_overview()` en production — pas de compte administrateur en
  session ; à la première lecture, attendre de l'ordre de 60 élèves, 36 sans aucun jour d'activité,
  0 élève et 0 parent joignables par push, 2 liens parent actifs (agrégats du 2026-11-12).
  Écarts acceptés : (a) le retrait de `?src=` passe par le `replaceState` NATIF et non par celui du
  routeur, qui re-résolvait la page et émettait une seconde page vue ; (b) **un plafond du budget
  runtime est relevé d'une unité** — `/programme`, 40 → 41 requêtes : `main` était à 40/40 avant le
  lot, la requête de plus est le chunk différé `visit-beacon` (3,4 Ko, chargé après l'hydratation) ;
  la ligne qui le justifie est dans `perf/runtime/budget.mjs`, aucun plafond d'octets ne bouge, et
  une seconde requête a été évitée en faisant calculer le jour de Tunis par la racine ; `index-`
  238,60 → 238,97 Ko (+0,37, pour 1 Ko permis) ; (c) la migration porte l'horodatage `160000` et non
  `150000`, pris entre-temps par la révocation de sécurité (#1287) ; (d) l'exécuteur n'a pas pu lire
  ni écrire ce dépôt (accès refusé à sa session) : il a travaillé sur les sections recopiées par la
  session qui orchestre, et cette entrée est posée par elle.
  Suite : les lots 3 et 4 se jugent sur `visit_returned{entry}` — ils partent un par un.
- **2026-11-13 — lot 3 livré (moteur #1298, puis #1299 pour un test e2e).** Carte d'installation
  après une réussite (résultat sans compte, résultat connecté) et sous le bilan de `/suivi` (texte
  parent) ; mémoire commune `na9ra.nudge` (14 jours, 7 pour `push`, deux refus ⇒ jamais, une seule
  invitation par écran, ordre rappel → installation → parent) ; `NudgeSlot` prêt pour les lots 2 et
  5 ; manifeste `start_url: "/?src=pwa"`, `id: "/"` ; `install_invite` câblé. Aucune migration.
  Mesures : `index-` 238,61 → 239,26 Ko (+0,65, pour 242) ; `i18n-fr`, `i18n-en`, `i18n-ar`,
  `dashboard-` inchangés ; aucun plafond relevé ; décalage de mise en page de la carte nul (0,076
  pendant le jeu, 0 après l'écran de résultat, identique avec et sans carte).
  **Vérifié en production le 2026-11-13** (navigateur émulé, mesure d'audience bloquée et lue par la
  sonde) : manifeste à jour ; Android avec l'événement simulé, mission réussie sans compte ⇒ carte,
  bouton ⇒ `prompt()` appelé une fois, acceptation ⇒ carte disparue, `install_invite` `shown` puis
  `accepted` `{native, student}` ; iPhone ⇒ deux gestes sans bouton, `shown {ios, student}` ; mission
  ratée ⇒ rien, aucun événement. Recoupé par la session qui orchestre : le manifeste servi porte
  `id: "/"` et `start_url: "/?src=pwa"`. **Non vérifié en production** : l'écran de résultat connecté
  et `/suivi` (ni compte ni code de test) — tests unitaires seulement ; aucun appareil réel.
  La suite e2e connectée, lancée sur la branche : 104 réussis et 1 échec au premier passage (un test
  neuf du lot, « quiz raté ⇒ rien », délai dépassé), verte après #1299.
  Écarts acceptés : (a) l'écouteur vit dans `install-signals.ts`, pas dans `install-prompt.ts` — seul
  morceau du chunk d'entrée ; `isStandaloneDisplay` y a quitté `entry-source.ts` (lot 0) pour ne pas
  ouvrir un chunk partagé ; (b) les chaînes sont dans un catalogue `i18n/install` chargé avec la
  carte, pas sous `public.install.*` (budget `i18n-fr`) ; (c) une invitation acceptée s'écrit
  `dismissed: 2` (forme de mémoire inchangée) ; (d) un événement d'installation arrivé APRÈS l'écran
  de résultat n'y insère pas de carte (zéro décalage), sauf sous le bilan de `/suivi` ; (e) la carte
  suit le sens de l'interface, pas celui du contenu ; (f) l'exécuteur n'a pas accès à ce dépôt :
  cette entrée est son texte, posé par la session qui orchestre.
  Dettes : pas d'essai sur appareil réel ; résultat connecté et `/suivi` non constatés en
  production ; l'écran de résultat entier passe en RTL quand le contenu est arabe et l'interface
  française (préexistant, hors lot) ; instabilité du test `authed/responsive` sur iPhone SE
  (débordement de l'en-tête connecté, vert au deuxième essai) ; `perf:budget` compte en local 42
  requêtes sur `/programme` pour un plafond de 41, avec ou sans le lot, alors que la CI est verte.
- **2026-11-13 — Lot 4 livré (moteur #1301, `ae350a5`).** Livré : R-15 à R-18. Rangée « Garder ce
  chapitre » (`src/components/public/keep-row.tsx`) sur l'écran de résultat sans compte — entre les
  actions et l'invitation à installer, le compte restant en dernier — et en bas d'un cours sans
  compte : « M'envoyer la suite » / « M'envoyer ce cours » toujours, « Partager ma réussite » sur
  réussite seulement. Geste unique `shareText` (`src/shared/lib/share-text.ts`) : feuille de
  partage → `wa.me` sans destinataire → copie avec confirmation ; les trois appelants historiques
  (`/suivi`, `/parent-report`, bilan du test de niveau) y passent, comportement fixé par test et
  inchangé. Lien = URL canonique `www` du chapitre + `?src=resume_link|share`. `content_shared`
  passe `live: true`.
  Mesures : `content_shared{intent: resume|success, surface: practice|reader, method:
  share|whatsapp|copy}` à l'envoi ; au retour `visit_returned{entry: resume_link|share}` (lot 0).
  Ni titre, ni score, ni identifiant dans les événements.
  Tests : Vitest (`share-text` par règle, états de la rangée, route, lecteur, geste des bilans),
  e2e `public-anon` (3 scénarios), suite e2e connectée verte sur la branche (108 réussis, 2 sautés,
  1 instable hors lot : `authed/responsive` sur iPhone SE).
  **Vérifié en production** (`/api/health` = `ae350a5`, navigateur émulé, mesure d'audience et
  WhatsApp coupés) : quiz raté ⇒ « M'envoyer la suite » seul ; quiz réussi 5/5 ⇒ les deux gestes ;
  sans feuille de partage ⇒ `wa.me/?text=` avec les textes de R-16 et l'URL `www` du chapitre ; le
  lien ouvert ailleurs ⇒ le chapitre, `?src=` retiré, `visit_returned{entry:"resume_link"}`.
  **Non vérifié en production** : la feuille de partage native d'un vrai téléphone, le repli copie,
  le rendu anglais et arabe, les deux bilans parent après leur passage à `shareText`, la carte
  d'installation sous la rangée.
  Écarts acceptés : (a) chaînes dans un catalogue à part (`i18n/keep`) plutôt que `public.keep.*` ;
  (b) +0,09 Ko sur `index-` et +0,03 Ko sur `dashboard-` (noms de chunks) ; (c) le titre du
  chapitre et le nom de la matière sont ceux du contenu (une seule langue en base), seul le gabarit
  suit la langue de l'interface ; (d) « au quiz » figure aussi dans le texte d'une mission réussie
  (gabarit de R-16 repris mot pour mot) ; (e) l'exécuteur n'a pas accès à ce dépôt : cette entrée
  est son texte, posé par la session qui orchestre.
  Dettes : une fenêtre WhatsApp bloquée par le navigateur n'est pas détectable (`noopener`) — le
  repli copie ne joue que si `window.open` est absent ou lève ; `intent: parent` déclaré mais non
  émis (le lot 5 l'émet) ; écran de résultat connecté sans rangée (US-8 dit « visiteur ou élève » :
  question ouverte au propriétaire) ; une feuille de partage refermée n'ouvre rien d'autre, à
  dessein.
  Suite : le lot 5 (le parent dans la boucle) part seul ; il émet `content_shared{intent:"parent"}`.
- **2026-11-13 — prérequis P-0 fait.** Accès Vercel accordé par le propriétaire. Constat d'abord :
  le projet `na9ranal3ab` (domaines `www.na9ranal3ab.tn`, apex et `*.vercel.app` en redirection)
  n'avait **aucune** des cinq variables Web Push — ni la paire VAPID, ni `CRON_SECRET` : le cron
  du soir répondait donc 401 depuis toujours, en plus de la clé absente du build. Fait : paire VAPID
  P-256 générée (vérifiée par signature) ; `VITE_VAPID_PUBLIC_KEY` = `VAPID_PUBLIC_KEY` et
  `VAPID_SUBJECT` = `mailto:contact@na9ranal3ab.tn` (l'adresse publique du site) en production et
  prévisualisation ; `VAPID_PRIVATE_KEY` et `CRON_SECRET` en production seulement, type
  « sensitive » ; aucune copie conservée hors de Vercel. Redéploiement de production depuis
  `a1384de`. Constaté : `www` sert `enable-push-card-DMw7W6GB.js`, qui porte la clé publique ;
  `/api/cron/notify` sans secret répond 401. **Reste à constater** : la carte au hall d'un compte
  connecté, une première ligne dans `push_subscriptions`, la réponse du cron de 18:00 UTC. Le
  projet `yahia-quest-arena` (sans domaine propre) n'a pas été touché.
