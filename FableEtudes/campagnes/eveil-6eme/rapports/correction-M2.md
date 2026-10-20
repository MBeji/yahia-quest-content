# Correction M2 — missions du gisement, éveil 6ᵉ (`02` 07, `03` 06–10 et 12, `10` 06–07)

Décisions du pilote appliquées en totalité. Aucun défaut refusé. Pas de git.

## Défauts par défaut

| défaut | sort | détail |
| --- | --- | --- |
| C-1 (m015 Q1, explication) | appliqué | texte de l'auditeur |
| C-2 (m015 Q1/Q5, numéros d'organes) | appliqué | Q1 : عضلة (العضو 1) والرّئتين (العضو 2) ; Q5 : العضو 1 ; consigne 1-أ rétablie telle qu'imprimée (« اُشطب العبارة الخاطئة… ») |
| C-3 (m019 Q4 option b + explication) | appliqué | texte de l'auditeur |
| M-1 (m013) | appliqué, décision du pilote | fichier déplacé et renommé `03/exercices/12-exam-2016-de-lair-aux-cellules-le-trajet-de-loxygene.json`, `displayOrder` 12, 7 q ; supprimé du `02` ; la ligne « Sujets officiels… » du `chapter.json` du `02` est gardée (m014 reste) ; `gisement.json` : chapitre, fichier, nn 12, etapes 7. Q4, Q6, Q7 gardées : cœur, artères et vaisseaux sont au cours `03` (§ « القلب يضخّ الدّم »). Dans Q6, « (البطين الأيسر) » retiré de l'énoncé (non enseigné) |
| M-2 (m013 Q3) | appliqué | remplacement de l'auditeur |
| M-3 (m013 Q4 → Q6) | adapté | le pilote garde Q4 : j'ai retiré de son explication l'enchaînement complet cœur → artères → muscle. L'ordering et le QCM visuel restent deux formes d'un même trajet : résidu assumé par la décision du pilote |
| M-4 (m014 Q3) | appliqué | supprimée |
| M-5 (m014 Q5) | appliqué | supprimée |
| M-6 (m014 Q6) | appliqué | remplacé par le QCM de l'auditeur, avec la graphie imprimée « ثنائي » (option b), qui suit la transcription 2010 ; toutes les options muettes |
| M-7 (m015 Q3) | appliqué | supprimée |
| M-8 (m016 Q2) | appliqué | supprimée |
| M-9 (m016 Q4) | appliqué | supprimée |
| M-10 (m017 Q6, Q4) | appliqué | Q6 remplacé par le QCM (clé a, options muettes) ; Q4 retouchée |
| M-11 (m018) | appliqué | Q4 et Q5 supprimées |
| M-12 (m021 Q3) | appliqué | supprimée |
| M-13 (m022 Q3, Q7) | appliqué | supprimées (5 q restent) |
| M-14 à M-17 (m020) | sans objet | m020 coupée en entier (voir plus bas) |
| M-18 (ids) | appliqué | options muettes, ids proposés ci-dessous |
| Gabarit 2×2 | appliqué | m016 Q4 (M-9) et Q5 supprimées, m020 Q2 avec la mission |
| m-1 (m013 Q2 a) | appliqué | `eveil.gaz.test-mal-associe` posée ; Q1 b muette |
| m-2 (m013 Q5) | appliqué | « (أعدنا رسم السّند) » ajouté aussi à Q6 |
| m-3 (m014 Q7 d) | appliqué | gardé ; graphie « ثنائي » rétablie dans l'item 2010 cité |
| m-4 (m014 Q8 c, m017 Q5 d et Q7 d) | appliqué | « ولا خطأ… » retiré |
| m-5 (m016 Q3 figure) | appliqué | deux `<text>` en `x="22"` `text-anchor="middle"` |
| m-6 (m019 Q3) | appliqué | phrase ajoutée à l'explication |
| m-7, m-8, m-9 | gardés | tolérés par l'auditeur |
| m-10 (m021 Q5) | appliqué | b et e retirés, g et h ajoutés, clé a/c/f/h, phrase ajoutée |
| m-11 | sans objet | Q3 de m022 supprimée |
| m-12 | à acter par le pilote | 69 q au lieu de 90 ; maintenant 45 q |
| m-13 | sans objet | rien à corriger |

## m020 (devoir `03/11`) : coupée (E-1)

Après les corrections il ne restait que Q1, Q3 et Q7 (3 q, sous le seuil de 5). Fichier supprimé ; `gisement.json` : m020 (`D04#1`) passée à `ecartee` (forme des missions), sans champ `fichier`, note « coupée à l'audit M2 : trop mince après retrait des redites (E-1) ». Il ne reste aucun devoir au `03` : la ligne « Calibré sur des devoirs publics… » est retirée de son `chapter.json`.

## Graphie ثنائي / ثاني

Suivie la transcription officielle : « ثنائي » en 2008, 2010, 2021 (m014 Q6 b, m019 Q2 d, m017 Q4 déjà conformes) ; « ثاني » en 2015, 2020, 2026 (inchangé).

## Tailles finales

m013 (03/12) 7 · m014 6 · m015 6 · m016 5 · m017 7 · m018 4 · m019 6 · m021 4 · m022 5 = 50 questions. m018 (4 q) et m021 (4 q) sont sous 5 : l'auditeur les avait acceptées, pas de coupe demandée par le pilote.

## Ids proposés (registre non touché, options muettes)

- `eveil.sang.nom-du-vaisseau-par-la-couleur` — « Tu nommes le vaisseau d'après la couleur de son sang : on dit artère ou veine selon le sens, du cœur ou vers le cœur ». Occurrences : m015 Q2 a et d, m017 Q2 b.
- `eveil.sang.coagule-et-decante-confondus` — « Tu confonds sang coagulé et sang décanté (caillot contre dépôt) ». Occurrence : m016 Q1 a.

## Gates (depuis `/home/user/eng-deliver`)

- `content:check` ✓ (121 sujets, 31 645 q) ; `content:qa -- --subject eveil-scientifique-6eme` ✓ ; `content:figures:check` ✓.
- `content:tranche … --chapters 02-respiration,03-sang-circulation,10-microbes-defense --fresh --strict-longest --strict-lessons` ✓ : clé la plus longue 0/97, positions 21/26/29/24 %, 0 cours en recul, 0 gabarit. Une paire proche non bloquante : `02/07` Q1 ↔ Q6 (0,49) — deux corrections de la même phrase officielle 2026 (air inspiré, puis sang sortant), qui portent sur deux savoirs distincts ; gardée, comme l'auditeur l'avait laissé.
- `content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/eveil-scientifique-6eme` sur le devoir restant (`10/07`) ✓ : 0 plage ≥ 8 mots, 0 exercice repris à 3 données. (`03/11` n'existe plus.)
- `npm run -s programme:check` ✓ (26 avertissements préexistants, étrangers au lot).
- Prettier `--write` puis `--check` ✓.

## Non vérifié

Rendu Chromium de la figure de m016 Q3 corrigée (valeurs prescrites par l'auditeur, qui les avait vérifiées). Le plan `plan-missions-v1.json` n'a pas été mis à jour (hors consigne).
