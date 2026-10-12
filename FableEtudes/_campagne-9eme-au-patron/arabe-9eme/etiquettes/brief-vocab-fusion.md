# Mandat — FUSION et COMPLÉMENT du vocabulaire d'erreurs de l'arabe 9ᵉ (phase 1 des tags, 2026-10-12)

Tu es un relecteur indépendant (opus). Corpus `/home/user/wt-arabe` (branche `wip/arabe-9eme-patron`, 19 chapitres `content/arabic/`), moteur `/home/user/eng-arabe` (lien `content` → corpus). Dossier de travail : `/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/` (noté `E/`). Tu ne modifies AUCUN fichier sous `content/`. Aucune écriture git.

## Ce qui existe
- **Partie A** (`E/vocab-arabe9-A.json`, 63 ids ; `E/map-arabe9-A.md` ; brouillons `E/work-A/`) : mandat `E/brief-vocab-A.md` — 8 chapitres prévus, mais **seuls 15, 04, 16, 17, 18 ont été faits** (l'agent a été coupé) : **02-an-nawasikh, 03-al-mansoubat, 19-al-adad-wal-madud manquent** (brouillon `work-A/ch02_labels_draft.json`).
- **Partie B** (`E/vocab-arabe9-B.json`, 119 ids neufs + 15 réutilisés ; `E/map-arabe9-B.md` ; scripts et données `E/work-B/`, dont `build.py` qui génère carte et JSON d'un jeu unique d'affectations) : chapitres 12, 05, 13, 14, 09, 10, 07, 08, 01, 06, 11. Doutes de l'agent B : `E/map-arabe9-B.md` §7 et ci-dessous.
- Règles : `.claude/skills/content-engine/references/content-schema.md` §« Optional `misconceptionTag` per distractor » et « La règle de décision — tagger ou laisser muet » (R1/R2/R3, seuil ≥ 3 questions distinctes, une phrase adressée à l'élève, 100 % n'est pas la cible) ; `course-explanation.md` (C-5 : chaque `::: piege` nomme une erreur déclarée dans `coursePitfalls` et portée par au moins un distracteur du chapitre). Registre : `content/misconceptions.json` (122 `arabe.*` du 6ᵉ). Métalangage : celui des manuels 101908 / 101909 (notes `…/arabe-9eme/lecture-101908/`, `lecture-101909/`).

## Travail
1. **Compléter 02, 03, 19** comme l'aurait fait A (lis cours + tous les items ; réutilise d'abord les ids A, B, puis du registre ; ids neufs seulement pour une erreur qu'aucun ne dit).
2. **Fusionner A + B + compléments** en UN vocabulaire, et le RELIRE avec sévérité :
   - doublons ou quasi-doublons de sens (entre A, B, et avec les 122 `arabe.*` existants : p. ex. `arabe.hijaj.istidrak-khalt` / `arabe.rabt.istidrak-bi-ma-yuwafiq`, `arabe.hijaj.mu2ashshir-ghayr-munasib` / `arabe.rabt.natija-bi-ghayr-al-fa`) → un seul id ;
   - ids sous le seuil : un id neuf doit être porté par ≥ 3 questions distinctes OU énoncé par un `piege` de cours (C-5) ; sinon il disparaît et ses options deviennent muettes ;
   - ids trop larges (p. ex. `arabe.mazid.ma3na-bila-nazar-fil-jidhr`, ~35 options) : garder s'il dit exactement chaque erreur, sinon scinder ou rendre muettes les options qu'il ne décrit pas ;
   - réutilisations approximatives du 6ᵉ (doute B-4 : `arabe.ishtiqaq.mazid-haraka-al-3ayn`, `arabe.fi3l.hukm-bil-haraka`, `arabe.sard.a3mal-at-tahawwul`) : une étiquette posée doit dire EXACTEMENT l'erreur de l'option — sinon id neuf (si seuil) ou muette ;
   - chaque libellé : une phrase à la 2ᵉ personne, précise, l'erreur ET la règle juste, métalangage du manuel, ≤ 160 caractères par langue, ar/fr/en équivalents.
   - Doute B-2 : `06/exercices/04*#2` (حَذِر rangé parmi les intensifs, contre le tableau du cours) — tranche (manuel ou usage), dis si l'item ou l'explication est faux.
3. **Vérifier un échantillon d'affectations** (au moins 60 options réparties sur les 19 chapitres, dont toutes celles des ids larges) : l'option est-elle fausse, et l'id dit-il exactement son erreur ?

## Livrables (écrits AU FIL DE L'EAU)
- `E/vocab-arabe9.json` : les SEULS ids neufs retenus, `{ "<id>": { "subject": "arabe", "labels": { "ar", "fr", "en" } } }`, JSON valide, 2 espaces, ordre alphabétique.
- `E/affectations-arabe9.json` : la liste MACHINE complète des poses, `[ { "chapitre": "<slug>", "fichier": "quiz.json" | "exercices/<nom>.json", "q": <index 1-based>, "opt": "<id d'option>", "tag": "<id>" } … ]` pour les 19 chapitres (y compris les ids existants réutilisés), une option au plus une fois, jamais la clé (vérifie-le par script contre les fichiers).
- `E/coursePitfalls-arabe9.json` : `{ "<slug>": ["<id>", …] }` pour les 19 chapitres, chaque id énoncé par un `piege` du cours du chapitre ET porté par une affectation du chapitre (C-5) — vérifie-le par script ; signale tout chapitre sans `piege` taggable.
- `E/rapport-fusion.md` : décisions (fusions, retraits, scissions, libellés réécrits, avant → après), chiffres finaux (ids neufs, réutilisés, options posées, % de distracteurs), échantillon vérifié, doutes restants.

Rapport final court, en français.
