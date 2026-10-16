# Re-vérification — lot L05, français 9ᵉ (gisement, étude 36)

Auditeur indépendant, 2026-10-16. Branche `wip/gisement-francais-9eme`, commit `6fb3f194` (« L05
corrections d'audit appliquées »). Base : `audit-francais-L05.md` et le journal
`auteurs-notes/fr-L05/CORRECTIONS.md`. Les fichiers `*-devoir-*` sont hors périmètre.

Méthode :

- diff `HEAD~1..HEAD` sur les 5 fichiers du lot ;
- re-résolution à l'aveugle des 11 questions de m023 et de chaque question modifiée ;
- vote recompté case par case ;
- longueurs mesurées par script.

## Gates

| gate | résultat |
| --- | --- |
| `content:check` | vert (29 625 questions : la Q3 de m024 a été retirée) |
| `content:qa:strict` | 0 erreur ; aucun avertissement sur `french/` |
| `content:tranche` (03, 04, 08, 13) | clé strictement la plus longue 0/161 ; positions 25/24/27/24 % ; paires proches et candidats gabarit tous hors lot (01, 03/01–04, 08 quiz) |

## Critiques

| défaut | vérification | verdict |
| --- | --- | --- |
| C1 m026 Q7 | texte appliqué à l'identique | **corrigé** |
| C2 m026 Q10 | texte appliqué à l'identique | **corrigé** |
| C3 m027 Q9 | texte appliqué à l'identique | **corrigé** |

Détail :

- **C1 — m026 Q7.**
  - L'énoncé fixe la narration au passé simple et à l'imparfait ; la question ne porte plus que sur
    les répliques.
  - Ma réponse : « Au présent, au passé composé ou au futur, selon le moment où l'on parle. » C'est la
    clé c. La règle est celle du cours 04 (« les temps sont ceux de celui qui parle, au moment où il
    parle »).
  - Distracteurs indéfendables :
    - le passé simple et l'imparfait de la narration, étiquette `fr.temps.recit-discours-melanges` ;
    - le plus-que-parfait et le conditionnel, muette ;
    - le passé simple seul, muette.
  - Longueurs 69 / 72 / 72 (clé) / 71.
- **C2 — m026 Q10.**
  - « Oui, j'en suis sûr : … » ne peut suivre qu'une question : celle de e.
  - b ouvre l'échange et d répond au « Pourquoi ». a tombe donc en 3ᵉ position.
  - Ordre unique b d a e c = `answerKey`. L'explication est conforme.
- **C3 — m027 Q9.**
  - « Monté sur cette estrade » impose b avant e ; « Après son discours » impose e avant a.
  - Ordre unique d b e a c = `answerKey`.
  - « participé aux travaux » et « À ta grande joie » sont corrigés.

## Majeurs

| défaut | verdict |
| --- | --- |
| M1 et M6 — m023 | **corrigé** (détail ci-dessous) |
| M2 — m024 Q3 supprimée, matching à 4 paires | **corrigé** |
| M3 — m025 Q3, explication | **corrigé** (texte du rapport ; ne livre pas la règle du féminin de Q8) |
| M4 — m025 Q4 | **corrigé** (citation complète, options en minuscule au 1ᵉʳ blanc, explication) |
| M5 — m025 Q7 | **corrigé** |

**M5 — m025 Q7, contrôle.**

- Grille genre × nombre : rattrapé / rattrapée / rattrapées / rattrapés.
- Le vote est nul ; la clé d reste juste.
- « rattrapé » garde `pp-avoir-cod-avant-oublie` ; les autres options sont muettes.
- Longueurs 31 / 32 / 33 / 32.

**M2 — m024, matching (ex-Q7, aujourd'hui Q6).**

- 4 paires : imagination–débordante, heures–longues, bateau–unique, Tous ceux–émerveillés.
- L'appariement est unique. « unique » est la seule forme possible pour « bateau », ce qui envoie
  « débordante » à « imagination ».
- m024 compte 7 questions, étages 2, 2, 3, 3, 3, 3, 3.

**Ajout hors rapport : « l'adjectif, déjà accordé ».** Il ne désigne aucune clé.

- Il dit seulement que les formes ne sont pas à modifier, ce qui est la consigne officielle de 2020 T
  (« choisis l'adjectif qui convient », formes imprimées accordées).
- Les quatre adjectifs restent à placer par le genre et le nombre.
- Aucune option n'en sort éliminée ou désignée. **Accepté.**

### m023, re-résolue en entier

| Q | ma réponse | clé | grille 2×2 (vote) | énoncé ↔ options | longueurs (clé en gras) |
| --- | --- | --- | --- | --- | --- |
| 1 | a été dévorée | b | temps × accord : nul | OK | 39 / **40** / 44 / 43 |
| 2 | On a secouru | d | temps × accord : nul | les 4 ont « on » pour sujet : la prémisse est respectée (M6) | 28 / 29 / 25 / **24** |
| 3 | a été … par | a | temps × par/de : nul | OK | **48** / 52 / 48 / 44 |
| 4 | bouleverse | c | temps × rôles : nul | OK | 53 / 51 / **51** / 53 |
| 5 | est mal expliquée | d | accord × temps : nul | OK | 43 / 46 / 45 / **44** |
| 6 | était caché | a | temps × par on : nul | OK | **60** / 67 / 60 / 67 |
| 7 | était encerclé | b | temps × rôles : nul | le cadre (« perd connaissance ») ne montre plus la forme passive | 59 / **59** / 60 / 60 |
| 8 | est doucement caressée | c | accord × temps : nul | OK | 62 / 64 / **62** / 64 |
| 9 | on m'a ridiculisé | d | temps × on/pronominal : nul | OK | 30 / 30 / 33 / **29** |
| 10 | ont été lues | a | accord × temps : nul | OK | **42** / 40 / 44 / 46 |
| 11 | J'ai été enthousiasmé | c | temps × genre : nul | cadre juste (le conteur, Pierre l'informaticien) | 45 / 47 / **46** / 46 |

Bilan m023 :

- 11 clés justes, 11 votes nuls ;
- aucune option qui contredit l'énoncé ;
- aucune clé strictement la plus longue ;
- la clé est la plus courte en Q2 et Q9 seulement : c'est la langue, pas un indice de forme.

Étiquettes :

- chaque option à deux erreurs est muette ;
- `place-apres-verbe` est retirée ;
- les étiquettes restantes (`temps-non-conserve`, `pp-etre-non-accorde`, `roles-inverses`, `par-on`,
  `nom-le-plus-proche`) nomment exactement l'erreur de leur option.

Les explications reprennent le texte du rapport. Aucune ne cite une lettre ou un rang, et aucune ne
livre la clé d'une autre question.

## Mineurs appliqués

| mineur | vérification |
| --- | --- |
| m1 — m024 Q1 | « Sami », un prénom de garçon ; « Sami est un homme » dans l'explication |
| m6 — m025 Q1 | « […] » marque la coupe |
| m6 — m025 Q5 | « (phrase adaptée du sujet) » ajouté |
| m7 — m026 Q1 a | « fait parler ton père et toi » ; explication alignée |
| m8 — m026 Q4 | « ses parents s'y opposent » |
| m8 — m026 Q8 | coupes marquées « […] » |
| m8 — m026 Q9 | explication sans « schéma narratif » |
| m9 — m027 Q10 | relative « qui est devenue mon amie » rétablie ; explication avec les mots du cours 02, sans « intervalle » ; appariement inchangé et unique |

## Écarts non appliqués (m2, m3, m4, m5, m10, m11)

Ce sont exactement les points que l'audit classait « à garder » ou « rien à corriger » :

- **m2** : la seule correction possible rendait la clé la plus longue ;
- **m3, m5, m10** : items assignés par la consigne de tri ;
- **m4** : paire miroir inhérente à l'item ;
- **m11** : étages et notion d'argument assumés par PLAN.md R5.

Les laisser en l'état est conforme à l'audit.

## Verdict

- Clés fausses : 0.
- Critiques corrigés : 3/3.
- Majeurs corrigés : 6/6.
- Mineurs : ceux à appliquer le sont ; les autres sont écartés comme prévu.
- Aucun défaut nouveau.

**Prêt à livrer.**
