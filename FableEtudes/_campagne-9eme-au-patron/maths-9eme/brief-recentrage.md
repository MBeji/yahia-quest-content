# Mandat — maths 9ᵉ : RECENTRER `01-nombres-reels` et `02-racines-carrees` sur leur chapitre officiel

Corpus `/home/user/yahia-quest-content` (moteur `/home/user/yahia-quest-arena`, lien `content` → corpus ; les contrôles se lancent DEPUIS LE MOTEUR). Matière `math` (maths 9ᵉ de base, Tunisie, cours et items en arabe, élèves de 14–15 ans, année du concours). La matière est **armée** (`coursePattern: "notion"` → le patron est vérifié en ERREUR) et **étiquetée** (`misconceptionTag` sur les distracteurs, `coursePitfalls` dans `chapter.json`, registre `content/misconceptions.json`, ids `math.*`).

## Arbitrage du propriétaire (2026-09-28)
« Maths 9ᵉ 01 et 02 recentrés sur leur chapitre officiel, le débordement en "pour aller plus loin" sans item. »

## Sources (lis-les AVANT d'écrire)
- Fiche `content/programmes-officiels/programme/9eme-base/maths.md` (transcription fidèle du manuel 102905) :
  - **chapitre 02 « مجموعة الأعداد الحقيقية IR » (p. 18–30)** = le périmètre de `01-nombres-reels` : lignes ~589–1148 (bornes de scope §6 vers la ligne 1091) ;
  - **chapitre 03 « العمليات في مجموعة الأعداد الحقيقية » (p. 31–48)**, dont **§IV « حساب عبارات بها جذور تربيعية » (p. 39–40)** et la définition p. 27 = le périmètre de `02-racines-carrees` : lignes ~1149–1869 (§IV vers 1221, 1465, 1689 ; bornes de scope vers 1805) ;
  - **§6.2 bis** (vers la ligne 11002) : le constat des audits — 01 déborde (équations / inéquations à valeur absolue, écriture scientifique, ordre, مجالات, valeur absolue), 02 nomme des identités remarquables (« الفرق بين مربّعين », `04-defi` q.4).
- Le manuel lui-même en cas de doute : `/root/.cache/yqa-manuels/102905P00.pdf` (`pdftoppm -r 150 -f N -l N -png … /tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/m9/p` puis lis l'image).
- Les chapitres qui enseignent le débordement (pour y renvoyer, jamais pour les modifier) : `19-valeur-absolue` (ch.3 §III), `17-ordre-et-comparaison` (ch.5), `16-puissances` (ch.4), `04-equations-inequations` (ch.7), `03-calcul-litteral` (ch.6 : الجذاءات المعتبرة).
- Référentiels : `.claude/skills/content-cours/SKILL.md`, `.claude/skills/content-engine/references/course-explanation.md` (LE PATRON), `course-quality.md`, `math-and-notation.md`, `correction-cle-longue.md`, `content-schema.md` (tags : règle R1/R2/R3 ; C-5).

## Travail
1. **Re-résous et classe chaque question** de `quiz.json` et `exercices/01…06-*.json` des deux chapitres : DANS le chapitre officiel, ou HORS (notion d'un autre chapitre du manuel). Une notion « utilisée en passant » qui est un acquis antérieur (7ᵉ / 8ᵉ, ou un chapitre précédent du manuel) n'est pas un débordement ; une notion ENSEIGNÉE par un chapitre ultérieur, si.
2. **Chaque question HORS** : réécris-la sur une notion du chapitre officiel (mêmes métadonnées, même difficulté, même type, nombre de questions par fichier INCHANGÉ ; clé jamais strictement la plus longue ; clés réparties ; distracteurs = erreurs réelles). Étiquettes : pose sur ses distracteurs les `misconceptionTag` `math.*` du registre quand la règle R1/R2/R3 le permet (sinon muet) ; n'invente aucun id.
3. **`cours.md`** : toute section ou partie de section qui enseigne une notion HORS va dans UN encadré final « 🚀 للتوسّع (خارج هذا الفصل) » — reconnaissance seulement, sans `piege` ni `verifie`, avec le renvoi au chapitre qui l'enseigne. Le reste garde le patron (le gate le vérifie en erreur). `resume.md` en miroir.
4. **`chapter.json`** : `coursePitfalls` ne doit déclarer que des ids énoncés par un piège du cours ET portés par un distracteur du chapitre (C-5) — vérifie-le après tes réécritures ; retire un id qui n'est plus porté, ajoute-en un si un piège neuf l'exige. Titre et description : ajuste-les s'ils annoncent un contenu retiré ; **ne change jamais un slug**.
5. **NE TOUCHE PAS** aux missions de l'étude 36 (`07-devoir-*.json`, `08-devoir-*.json`) : elles appartiennent à une autre session. Signale seulement si l'une d'elles sort du chapitre.

## Contrôles (depuis `/home/user/yahia-quest-arena`)
`npm run -s content:check` ; `npm run -s content:qa 2>&1 | grep -E "math/(01|02)-"` → zéro erreur ; `npm run -s content:tranche -- --subject math --chapters 01,02` → clé strictement la plus longue ≤ 1 par chapitre, pas de paire proche neuve ; `npx prettier --ignore-path /dev/null --write` puis `--check` sur les `.json` SEULEMENT (Prettier casse les tableaux placés dans un bloc `:::` des `.md`). D'autres agents travaillent en parallèle sur `content/arabic/` : n'y touche pas. Aucune écriture git.

Écris tes fichiers AU FIL DE L'EAU (un fichier dès qu'il est prêt) : le quota est partagé, une coupure ne doit rien perdre.

## Rapport final (court, en français)
Par chapitre : questions classées DANS / HORS (liste des HORS : fichier#q → notion → chapitre qui l'enseigne) ; questions réécrites ; ce qui est passé en « للتوسّع » ; coursePitfalls avant → après ; contrôles ; doutes.
