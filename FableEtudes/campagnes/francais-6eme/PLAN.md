# Français 6ᵉ (`french-6eme`) — plan du passage unique (patron + étiquettes + armement + gisement)

> Ouvert le 2026-10-19, après le LOT A (fiche `programme/6eme-base/francais.md`, `validee-r7`, PR #726).
> Branche de travail : `wip/francais-6eme-un-passage` (worktree `wt-fr6b`). Modèle : la campagne
> `FableEtudes/campagnes/anglais-6eme/` (PLAN, décisions D1–D8, E1–E8).

## 0. Ce qui diffère de l'anglais 6ᵉ

- **La matière n'existe pas** : `content/french-6eme/` est écrit de zéro (8 chapitres = 8 modules du
  manifeste), cours au patron dès la première écriture — pas de « mise au patron » d'un existant.
- **La fiche est riche** (≈ 3 500 lignes) : chaque module y décrit fiche-contrat, encadrés du manuel
  121614 verbatim, exercices du cahier 121615 un par un, textes et questions, projet d'écriture,
  dictée, fiches du Fichier-classe 521616. Les auteurs génèrent **depuis la fiche**, sans rouvrir
  les PDF (T-3).
- **Étiquettes** : l'espace `fr.*` existe (103 ids, 9ᵉ) ; on le réutilise et on l'étend.

## 1. Les lots, dans l'ordre

| Lot | Qui | Quoi | Sortie |
| --- | --- | --- | --- |
| D0 | sonnet | registre du gisement : 17 sujets du concours (2008–2026 ; 2011, 2014 introuvables), vague 1 de 9 devoirs (3 par trimestre) | `sources-externes/web-6eme-base-french/` |
| A | opus | vocabulaire d'étiquettes `fr.*` pour la 6ᵉ (réutiliser, élargir, ids neufs fr/en/ar) | `misconceptions.json`, `etiquettes/` |
| B1–B4 | sonnet ×4 | 2 chapitres chacun, écrits de zéro au patron : `chapter.json`, `cours.md`, `resume.md`, `quiz.json`, 5 exercices, étiquettes posées, `coursePitfalls` | `content/french-6eme/0N-*` |
| D1 | sonnet ×3–4 | lecture des 17 sujets (transcription, lignes) et des 9 devoirs (salle blanche) | transcriptions + `lecture-6eme/francais/` |
| D2 | sonnet | carte, écart, plan des missions (examens + devoirs) | `PLAN-gisement.md`, registre `missions` |
| C | sonnet ×4 | missions d'examen et de devoirs, par les auteurs des chapitres | `exercices/NN-exam*`, `NN-devoir-*` |
| Audit | opus, par lot | re-résolution à l'aveugle, fidélité à la fiche, étiquettes, rendu | `audits/` |
| E | pilote | armement (`subject.json`, `coursePattern`), gates, livraison, publication `french-6eme`, drift, registre `publiee` | PR |

## 2. Décisions (pilote, 2026-10-19)

| | Question | Décision |
| --- | --- | --- |
| **F1** | Faits de langue exercés par le seul Fichier-classe (fiche §2.10 tableau C : pronoms compléments, démonstratifs, gérondif, relatives, ne…rien…) | **(b) s'en tenir au guide** : ni cours ni question qui les cible ; ils peuvent apparaître dans un texte support. Décision par défaut (le propriétaire, consulté, a dit « continue » sans trancher) — révisable. |
| **F2** | Chapitrage | 8 chapitres = 8 modules, slugs du manifeste ; pas de chapitre de phonétique (pas d'audio). |
| **F3** | Espace d'étiquettes | `fr.*` partagé avec la 9ᵉ (précédent `math.*`, `english.*`) ; libellés élargis par un exemple de 6ᵉ, ids neufs pour les erreurs propres au primaire. |
| **F4** | Placement des missions | langue → chapitre qui enseigne la notion ; lecture et production → chapitre du module dont relève le thème ; déclaré dans la note. |
| **F5** | Accord du participe passé avec *avoir* | ⛔ (le guide fait foi) malgré l'encadré du manuel p.125 : jamais ciblé. |
| **F6** | Manuels | `subject.json` `manuels` : 121614 (lecture) et 121615 (cahier d'activités) ; `manuel` de chaque chapitre = 121614 + pages du module (manifeste). |
| **F7** | Livraison | deux PR (01–04, puis 05–08 + armement) si le volume l'exige ; sinon une. |
