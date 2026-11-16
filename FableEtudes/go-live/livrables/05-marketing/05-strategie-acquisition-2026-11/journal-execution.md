# Journal d'exécution — stratégie d'acquisition S4

Une ligne par action vue à l'écran, avec sa date (heure de Tunis) et son lien. Puis la revue de chaque lundi.
Dépôt public : aucun nom de parent, d'élève ou de commentateur, aucun message privé.

## Actions

| Date | Action | Où | État vu à l'écran |
| --- | --- | --- | --- |
| 2026-11-14 | Relevé base de production (agrégats) : 1 compte actif sur 7 jours, 78 comptes, 2 créés sur 7 jours, 4 tests commencés et 2 terminés en cumul, dernière réponse le 8 novembre | Supabase `fasrenmmrkqjoobrztbp` | lu |
| 2026-11-14 | Relevé GA4 : 305 sessions, 288 nouveaux utilisateurs sur 7 jours | Google Analytics, propriété Na9raNal3ab | lu |
| 2026-11-14 | Présentation de la Page remplacée : « تمارين مع الإصلاح في كامل البرنامج التونسي، من السنة الأولى إلى الباكالوريا. مجانًا ودون تسجيل. » | https://www.facebook.com/na9ranal3ab | fait |
| 2026-11-14 | Bouton de la Page : « Nous contacter » vers l'ancienne adresse vercel.app remplacé par « En savoir plus » vers `/test-de-niveau?utm_source=facebook&utm_medium=page&utm_campaign=bouton` | Page, Outils professionnels → Bouton d'action | fait |
| 2026-11-14 | Bio Instagram remplacée : « Tout le programme tunisien en exercices corrigés. Gratuit, sans inscription. » | https://www.instagram.com/na9ranal3ab/ | fait |
| 2026-11-14 | Lien de la bio Instagram : non modifiable depuis l'ordinateur (Instagram le réserve à l'application mobile) | Instagram, Modifier le profil | fait par le propriétaire le 2026-11-14, vu à l'écran : `/test-de-niveau?utm_source=instagram&utm_medium=bio` |
| 2026-11-14 | Trois réponses au nom de la Page sous des commentaires de juillet et d'août (un merci, avec le lien `utm_campaign=commentaires&utm_content=c01` pour l'un d'eux) | Meta Business Suite, Commentaires Facebook | fait |
| 2026-11-14 | Programmée : lundi 16 novembre 19:00, Facebook + Instagram, visuel 08, `utm_content=presentation` | Meta Business Suite, Contenu → Programmé | programmé |
| 2026-11-14 | Programmée : mercredi 18 novembre 19:00, Facebook, visuel 01, `utm_content=test-6e` | idem | programmé |
| 2026-11-14 | Programmée : vendredi 20 novembre 18:00, Facebook + Instagram, visuel 05, `utm_content=defi-9e` | idem | programmé |
| 2026-11-14 | Programmée : dimanche 22 novembre 20:00, Facebook, visuel 12, `utm_content=plan-6e` | idem | programmé |
| 2026-11-14 | Second administrateur invité par le propriétaire : contrôle total sur la Page et sur Instagram, accès partiel au portefeuille ; invitation en attente d'acceptation | Paramètres du portefeuille → Personnes | lu, en attente |
| 2026-11-14 | Essai du parcours par le propriétaire depuis l'application Facebook (campagne `essai`, à exclure des chiffres) : « tout passe ». Base, 2 dernières heures : 5 tests commencés, 4 terminés, 1 compte créé, 0 test rattaché à un compte | Supabase (agrégats) | lu, rattachement à vérifier |
| 2026-11-14 | Metricool ouvert par le propriétaire : marque « na9ranal3ab », Page et Instagram reliés, fuseau Africa/Tunis ; connecteur lu avec succès | Metricool | lu |
| 2026-11-14 | git et gh installés et authentifiés (MBeji, administrateur des deux dépôts) ; dépôts clonés dans `depots/` | poste local | vu |
| 2026-11-14 | Rattachement du test au compte : fonctionne (1 test rattaché en base), mais le propriétaire voit d'abord un écran d'erreur « chargement impossible » au retour de l'inscription, puis le bilan après un clic sur « Réessayer ». Cause probable : course entre la lecture du bilan et le rattachement (`test-de-niveau_.$sessionId.tsx`, `use-claim-placement-sessions.ts`). Chantier à arbitrer | Supabase (agrégats), code du site | constaté |
| 2026-11-14 | Correctif du bilan du test de niveau (`insightsLocked` nul au retour d'inscription) poussé | https://github.com/MBeji/yahia-quest-arena/pull/1338 | fusionné le 2026-11-14, migration appliquée en production (fonction relue en base) |
| 2026-11-14 | Nouvelle identité des réseaux, sur feu vert du propriétaire : logo « N9 · نقرا نلعب » vert et ambre, couverture « راجع وأنت تلعب » aux couleurs et polices du site. Photo de profil et couverture de la Page, photo de profil Instagram. Sources dans `marque/` | https://www.facebook.com/na9ranal3ab · https://www.instagram.com/na9ranal3ab/ | fait, vu à l'écran |
| 2026-11-14 | Icônes extérieures du site alignées sur le logo N9 vert (onglet, icônes d'installation) ; la couronne reste l'emblème de l'interface connectée | https://github.com/MBeji/yahia-quest-arena/pull/1339 | fusionné |
| 2026-11-14 | Fiche de la Page : compte Instagram ajouté aux réseaux sociaux | https://www.facebook.com/na9ranal3ab/about | fait |
| 2026-11-14 | Story Instagram du mercredi 18 novembre 19:05 (visuel 09, sans autocollant de lien : l'interface ne le permet pas) programmée par Metricool | Metricool, planificateur | programmé |
| 2026-11-14 | Constat : les « 11 publications identiques » du 18 octobre ne sont pas sur le fil de la Page (une seule y est) ; les autres sont des publications faites au nom de la Page dans des groupes. Rien archivé ni supprimé | Bibliothèque de contenu de la Page | constaté, à arbitrer |
| 2026-11-14 | Facebook a publié seul deux messages « a changé sa photo de profil / de couverture » | fil de la Page | constaté |
| 2026-11-14 | Semaines 2 à 4 programmées dans Metricool, textes validés du lot du 14 novembre : 23, 25, 27, 29 et 30 novembre ; 2, 4, 6, 7, 9, 11 et 13 décembre (Facebook, et Instagram pour les publications prévues sur les deux réseaux ; légende Instagram « lien en bio » ; premiers commentaires des 27 novembre et 2 décembre ; story Instagram du 27 novembre). 18 entrées relues dans le planificateur | Metricool, planificateur | programmé |
| 2026-11-14 | Nouveau visuel 17 « fin des examens » pour le 4 décembre (le visuel 02 sert déjà le 27 novembre), tiré du texte validé | https://github.com/MBeji/yahia-quest-content/pull/865 | fusionné |
| 2026-11-14 | Hashtags Instagram validés par le propriétaire (5 par publication, jeux 6ᵉ, 9ᵉ, Bac, Tous ; Instagram seulement) ajoutés à 9 publications : 16 et 20 novembre (Meta Business Suite), 23, 25, 30 novembre, 2, 4, 7, 11 décembre (Metricool). Les questions du lundi, communes aux deux réseaux, ont été séparées en une publication Facebook sans hashtag et une Instagram avec | Metricool · Meta Business Suite | fait, relu |
| 2026-11-15 | Animation programmée, sur feu vert d'autonomie du propriétaire : 12 défis du jour (17, 19, 21, 24, 26, 28 novembre ; 1er, 3, 5, 8, 10, 12 décembre ; Facebook et Instagram, `utm_campaign=animation`, réponse dans les commentaires et en story le lendemain) et 28 stories quotidiennes à 13 h (16 novembre → 13 décembre ; Facebook et Instagram : réponse du défi de la veille ou conseil de révision). Facebook passe à une publication par jour, sans rafale. 52 entrées créées | Metricool · visuels https://github.com/MBeji/yahia-quest-content/pull/866 | programmé, PR fusionnée |
| 2026-11-14 | Déclaration INPDP (GAP-003) : mise de côté par le propriétaire pour le moment ; publicité payante, écoles, formulaires et concours restent bloqués d'ici là | — | reporté |
| 2026-11-14 | Six tâches planifiées créées : ouverture du soir (18 h 30), réponse du soir du lundi (21 h 05), revue du lundi (9 h), lot du vendredi (10 h), épinglage du 16 novembre (19 h 30), premier commentaire du 18 novembre (19 h 15) | Application Claude, section Planifiées | créé |
| 2026-11-15 | Ouverture du soir : Meta Business Suite reste une page blanche (3 chargements : Contenu → Publié, calendrier, accueil). Publications, programmation Meta, commentaires et messages non relevés ; rien republié | Meta Business Suite, Chrome du propriétaire | non relevé |
| 2026-11-15 | Metricool, 15 → 17 novembre : rien prévu le 15 ; en attente, story FB + IG du 16 à 13:00, story FB + IG du 17 à 13:00, défi du 17 à 19:00 (FB et IG) | Metricool, planificateur (connecteur) | lu, programmé |
| 2026-11-15 | Quart d'heure « groupes » du 16 novembre préparé (5 situations, liens g01 à g05) | `groupes-quart-heure-2026-11-16.md` | préparé |

## Revues du lundi

### Lundi 16 novembre 2026 (lu vers 18 h 25, heure de Tunis)

Première revue. La campagne commence ce soir (première publication à 19:00) : cette semaine sert de point zéro.

**En une ligne : 0 apprenant actif sur 7 jours, pour une cible de 100 au 12 décembre (26 jours) et de 500 au 14 février 2027.**

| Indicateur | Relevé | Source |
| --- | --- | --- |
| Comptes ayant répondu à au moins une question, 7 jours | 0 (dernière réponse le 8 novembre) | Supabase `fasrenmmrkqjoobrztbp`, agrégats |
| Comptes créés, 7 jours | 2 (11 et 14 novembre ; celui du 14 tombe le jour de l'essai du propriétaire) ; 79 en tout | idem |
| Tests de niveau, 7 jours | 5 commencés, 4 terminés, 1 rattaché à un compte, tous le 14 novembre, jour de l'essai du propriétaire : **0 commencé, 0 terminé hors essai** | idem |
| Tests de niveau, cumul | 9 commencés, 6 terminés, 1 rattaché, 5 restés anonymes ; hors essai du 14 novembre : 4 commencés, 2 terminés | idem |
| Sessions et utilisateurs, 9 → 15 novembre | 316 sessions, 298 utilisateurs, 292 nouveaux ; 60 sessions avec engagement | Google Analytics 4, Acquisition de trafic et d'utilisateurs |
| Par source / support | (direct) 257 sessions (9 % d'engagement, 1 s en moyenne) ; facebook / page 13 (62 %, 2 min 40 s) ; lm.facebook.com 12 ; facebook.com 7 ; m.facebook.com 7 ; vercel.com 7 ; accounts.google.tn 4 ; bing 4 ; instagram / bio 3 ; google 2 | idem |
| Par campagne (`utm_campaign`) | `essai` 6 sessions (propriétaire, à exclure) ; `examens-t1` 4 ; `commentaires` 3 | idem |
| Par `utm_content` | non relevé (dimension non affichée dans le rapport) | — |
| PostHog | non relevé (page de connexion) | PostHog EU, projet 233369 |
| Search Console, 7 jours | 0 clic, 11 impressions, position moyenne 3 | Search Console `sc-domain:na9ranal3ab.tn`, Performances |
| Pages indexées | 1 dans l'index, 11 non indexées (9 « explorée, actuellement non indexée », 2 « page avec redirection ») ; rapport mis à jour le 13 novembre | Search Console, Indexation des pages |

**Publications de la semaine** (Meta Business Suite, Contenu → Publié, recoupé avec Metricool). Trois seulement, toutes du 14 novembre : pas de classement à trois contre trois.

| Publication | Vues | Spectateurs | Interactions | Clics sur le lien |
| --- | --- | --- | --- | --- |
| 14 nov. 12:40, texte avec lien pour les parents (suivi par code, sans compte) | 78 | 41 | 3 (2 réactions, 1 commentaire) | 2 |
| 14 nov. 21:03, changement de photo de profil (message automatique) | 11 | 6 | 0 | 0 |
| 14 nov. 21:04, changement de photo de couverture (message automatique) | 0 | 0 | 1 | 0 |

Instagram : aucune publication sur la période (Metricool).

**Lecture.** Les 257 sessions « direct » durent une seconde en moyenne : elles ressemblent à du trafic automatique et ne comptent pas comme audience. Le trafic utile de la semaine tient en une quarantaine de sessions venues de Facebook, dont 13 par nos liens tracés ; ce sont elles qui restent le plus longtemps. Aucune n'a commencé un test hors essai.

**Décision.**
- On double : rien encore, aucun format n'a amené de test terminé. Le calendrier validé (16 publications, 12 défis, 28 stories) part tel quel ; le premier tri se fera lundi 23 novembre sur une semaine pleine, au nombre de tests terminés par `utm_content`.
- On arrête : rien. On cesse seulement de lire le total des sessions GA4 comme une audience ; le chiffre suivi est le nombre de tests commencés et terminés hors essai, puis les apprenants actifs.
- Écart à la cible : 0 sur 100 à 26 jours. Les seuls leviers ouverts sont la Page et le quart d'heure « groupes » du propriétaire ; les écoles, la publicité et les concours restent fermés tant que la déclaration INPDP n'est pas déposée.

**Constats à arbitrer.**
- La publication du 14 novembre à 12:40 ne figure ni au calendrier ni au lot validé ; elle est la seule à avoir amené des clics cette semaine.
- Recherche Google : 9 pages explorées mais non indexées, 1 seule dans l'index. Chantier sur le site, à décider.
- PostHog : session fermée dans le navigateur, relevé impossible tant qu'elle n'est pas rouverte.
