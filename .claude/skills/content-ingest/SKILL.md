---
name: content-ingest
description: >-
  Règles de fidélité (R-1…R-7) et consignes de rôle des sous-agents qui lisent une
  source (manuel ou guide CNP du Drive cnp-officiel, sujet d'examen national, devoir
  en ligne) et en tirent des missions. Le DÉROULÉ n'est plus ici : toute demande
  d'ingestion (« ingérer un PDF », « transcrire un manuel », « exploiter les anciens
  examens / les devoirs en ligne », « gisement ») suit la procédure unique du skill
  `campagne` (étapes 3 à 6), qui charge ce skill pour ses règles et ses consignes de
  rôle. Transcrit fidèlement, ne génère jamais ; sortie = fichiers content/ sur une
  branche + gates + revue, jamais d'écriture en base.
---

# content-ingest — règles de fidélité et consignes de rôle

## La procédure n'est plus ici

**Depuis le 2026-11-03, le déroulé complet — source Drive, lecture au moindre coût (L0 → L3, sondage
image), fiche, examens nationaux, écriture, audit, livraison — est dans le skill
[`campagne`](../campagne/SKILL.md), la procédure unique** (étapes 3 à 6). Ce skill ne garde que :

- les **règles de fidélité** R-1…R-7 ci-dessous, que la procédure applique ;
- les **consignes de rôle** à passer telles quelles aux sous-agents :
  [`gisement-lecteur.md`](references/gisement-lecteur.md) (lire un sujet ou un devoir),
  [`gisement-auteur-examen.md`](references/gisement-auteur-examen.md) (mission reprise d'un examen
  national, citée), [`gisement-auteur-devoir.md`](references/gisement-auteur-devoir.md) (mission neuve
  en salle blanche, sur demande seulement), [`gisement-auditeur.md`](references/gisement-auditeur.md) ;
- les règles propres au gisement (échantillon, contrôle local, registre) :
  [`references/gisement.md`](references/gisement.md).

Tu **transcris fidèlement, tu ne génères jamais** ; la génération pédagogique reste aux skills
d'écriture (`content-ecole-tn`, `content-cours`, `content-interactif`, `prof-*`).

## Règles (non négociables)

- **R-1 — Rien ne contourne le pipeline.** Sortie = TOUJOURS des fichiers `content/` (ou une transcription
  `programme/…`) sur une branche + gates (`content:check` / `content:qa:strict` / `content:audit`) + revue
  humaine. **Aucune écriture DB**, aucun skip d'audit.
- **R-2 — Provenance & droits.** Chaque source porte auteur / origine / autorisation ; un document sous
  droits sans autorisation est **refusé**. Les `chapter.sources[]` citent le document. Doute ⇒ **STOP**.
  **Les sujets officiels des examens nationaux** (concours de 6ᵉ, concours de 9ᵉ, baccalauréat, toutes
  sessions) sont du **corpus officiel** (décision du 2026-09-28, étude 27 Q-6) : tu les transcris comme
  un manuel CNP, sans autorisation à demander, et tu les cites. D'un site qui les ré-héberge, tu ne
  prends que le sujet ; son corrigé et ses commentaires, comme le devoir d'un établissement, restent une
  source web.
  **Source du WEB** (site de devoirs, blog d'enseignant, portail d'annales) : profil `source-web` de la
  méthode — déclare le **tier** avant le premier token. T0 (veille), T1 (lien sortant) et T2′ (génération
  inspirée) ne demandent aucune autorisation ; seule la **transcription (T2)** en exige une, écrite. Tu
  n'es appelé que pour T2 : sans autorisation en main, **tu ne transcris pas** — tu produis une fiche de
  veille et tu passes la main aux skills de génération. `content:qa` vérifie l'absence de reprise verbatim
  (étude 27 R-8), donc une copie « discrète » échouera le gate, pas la revue.
- **R-3 — Programme d'abord.** Pour une matière scolaire, confronter la fiche à la **transcription CNP**
  (`programme/<grade>/<matière>.md`) si elle existe ; divergence de scope ⇒ le **programme officiel gagne**,
  signaler l'écart (règle `content-ecole-tn`).
- **R-4 — Vérifie l'existant AVANT toute campagne, dans le REGISTRE.** L'état de transcription vit dans
  `programmes-officiels/suivi/<grade>.json` (statuts normés, couverture en plages de pages, profondeur),
  validé en CI par `npm run programme:check` — `programme/_INDEX.md` n'est qu'une **vue générée**
  (`programme:index`), ⛔ jamais éditée à la main. Une entrée `complete`/`validee-r7`/`promue` = **déjà
  fait** ; `partielle` = **compléter** (les plages manquantes sont listées), jamais refaire. Vérifie aussi
  qu'aucune autre session ne tient déjà le couple — par le **scan à trois pattes** du skill `campagne`
  (§ 1 bis : worktrees, branches non mergées, PR ouvertes, en grepant le nom FR **et** le préfixe de
  sujet) ; un grep sur un préfixe de branche comme `feat/transcription-*` rend vide à tort. Le check CI
  rejette un même PDF revendiqué par deux fiches — les incidents de doublons (2026-07-12 collège,
  2026-07-17 vague-A) ne peuvent plus passer. En cas de doublon hérité : comparer, garder la meilleure
  copie, documenter dans le registre.
- **R-5 — Standard de fiche : « profondeur de génération », jamais un résumé.** Une fiche destinée à
  alimenter la génération pédagogique doit décrire **chaque activité/exercice individuellement** (énoncé,
  données, ce qui est demandé), reproduire **verbatim** les encadrés de règles/lois officielles, relever le
  vocabulaire officiel, et poser des bornes de scope INCLUS/EXCLU — modèle de référence :
  `programme/1ere-sec/mathematiques.md`. Une fiche « first-pass » (structure + objectifs seulement, sans ce
  niveau de détail) doit être étiquetée comme telle et **jamais confondue avec une fiche prête pour la
  génération** — l'écart de qualité entre les deux est la cause directe d'un contenu généré médiocre.
- **R-6 — Une session = une matière, lecture intégrale obligatoire.** Ne jamais plafonner arbitrairement
  la lecture d'une source (l'incident du 2026-07-10 a lu 15-76 % des sources avant d'écrire, plafonné à
  70 000 caractères par manuel, produisant une fiche truffée d'inventions). Traiter plusieurs matières dans
  la même fenêtre de contexte dilue le budget de lecture par matière et bâcle chaque fiche — un lot batch
  de 10 fiches en une nuit est le signe qu'on va trop vite. Une matière incomplète mais honnêtement étiquetée
  (« profondeur : modules 1-4 faits, 5-7 en first-pass ») vaut mieux qu'un lot complet mais bâclé.
- **R-7 — Vérification indépendante avant promotion.** Une fiche produite par une session/agent ne devient
  la référence canonique (`programme/<grade>/<matière>.md`, cochée dans `_INDEX.md`) qu'après relecture par
  un second agent qui re-vérifie contre la source elle-même (pas contre la fiche) — pas seulement contre son
  propre travail. Protocole (sondage dirigé, règle T-8 de la méthode) : 100 % du critique (encadrés
  verbatim, chapitrage/manifeste, zones `[?]`) + ≥15 % des pages restantes ; ≥3 erreurs substantielles ⇒
  re-lecture intégrale.
- **Fidélité, pas de génération.** La lecture (texte ou vision) **transcrit** ; difficulté / calibrage / QCM
  / cours = **génération** (couche 3), jamais ici.

## STOP (escalade — ne re-designe jamais en silence)

- Doute sur les **droits** d'une source ⇒ STOP (R-2).
- Scan **illisible** / manuscrit ⇒ signaler, **ne pas deviner** (fidélité).
- Divergence transcription ↔ programme officiel ⇒ le **programme gagne**, signaler (R-3).
- Tentation d'utiliser une **clé API** alors que l'abonnement suffit ⇒ ne pas le faire ; rester
  **agent-in-the-loop**.
- Besoin d'un **format de contenu inexistant** ⇒ signalement vers l'étude 03 / le catalogue, jamais un
  format ad hoc.
- Budget de lecture/contexte insuffisant pour finir une matière en profondeur ⇒ **STOP proprement** à la
  fin de la dernière section traitée, étiquette clairement ce qui reste en first-pass (R-6) ; ne bâcle
  jamais le reste pour "finir".

Défère toujours à **CLAUDE.md** / **ARCHITECTURE.md** et aux `docs/*.md` normatifs.
