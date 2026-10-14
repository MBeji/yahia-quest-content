# Journal de lecture — gisement 9ᵉ × arabe (étude 36, G2), examens C01–C06

Tenu au fil de l'eau par le lecteur. Snapshots et rendus hors dépôt : `/tmp/claude-0/argis/`.

## 2026-10-14 — reprise après coupure de quota

- État constaté à la reprise : rien d'écrit (ni reader-context régénéré, ni transcription, ni ligne, ni snapshot).
- Téléchargement (`curl -g`, http, pas de TLS) des six PDF dans `/tmp/claude-0/argis/src/` : les six sha256 = registre.

| id | session | sha256 (préfixe) | pages | mode | état |
| --- | --- | --- | --- | --- | --- |
| C01 | 2026 générale | 9b5c567c | 5 | à lire | téléchargé, sha OK |
| C02 | 2026 technique | 116a929a | 4 | à lire | téléchargé, sha OK |
| C03 | 2025 générale | f966db25 | 5 | à lire | téléchargé, sha OK |
| C04 | 2025 technique | 7400fbb2 | 4 | à lire | téléchargé, sha OK |
| C05 | 2024 générale | 237979c8 | 5 | à lire | téléchargé, sha OK |
| C06 | 2024 technique | 166cfe18 | 4 | à lire | téléchargé, sha OK |

- C01 (2026 générale) — LU. sha 9b5c567c… OK ; 5 pages ; pdftotext vide (scan) → vision 150 DPI, page du texte relue à 220 DPI en deux bandes (vocalisation). Transcription `2026-generale.md` écrite ; 11 lignes (3 parties : F 4 pts / langue 6 pts / production 10 pts). Lisibilité bonne. Soulignés rendus `<u>…</u>`.
- C02 (2026 technique) — LU. sha 116a929a… OK ; 4 pages ; scan → vision 150 DPI, texte relu à 220 DPI, segments soulignés de la Q5 relus à 250 DPI. Transcription `2026-technique.md` ; 10 lignes. Format technique : 1 h, coef 1, « الأسئلة » 14 pts (compréhension + langue mêlées) + « تحرير فقرة » 6 pts. Notions d'acquis 7ᵉ-8ᵉ (مفعول مطلق/لأجله, أنواع الجمع) marquées HP ; المشتقّات et المثنّى rattachés aux chapitres hors manifeste 06 et 01.
- C03 (2025 générale) — LU. sha f966db25… OK ; 5 pages ; scan → vision 150 DPI, texte relu à 220 DPI. Transcription `2025-generale.md` ; 13 lignes. Texte presque entièrement vocalisé, transcrit tel quel. Deux nombres de l'énoncé (exercice du nombre) conservés en chiffres comme imprimés.
- C04 (2025 technique) — LU. sha 7400fbb2… OK ; 4 pages ; scan → vision 150 DPI, texte (dense, soulignés) relu à 220 DPI. Transcription `2025-technique.md` ; 9 lignes. Texte support narratif (pas argumentatif) ; notions de langue surtout d'acquis 7ᵉ-8ᵉ (المفاعيل، الإسناد) → HP.
- C05 (2024 générale) — LU. sha 237979c8… OK ; 5 pages ; scan → vision 150 DPI, texte relu à 220 DPI. Transcription `2024-generale.md` ; 11 lignes. Partie langue titrée « اللّغة » (6 pts) ; texte narratif à visée argumentative.
- C06 (2024 technique) — LU. sha 166cfe18… OK ; 4 pages ; scan → vision 150 DPI, texte relu à 220 DPI. Transcription `2024-technique.md` ; 8 lignes. Langue presque entièrement sur acquis 7ᵉ-8ᵉ (جمع، إسناد إلى الضّمائر، مشتقّات، مفاعيل).

## Bilan du lot (2026-10-14)

- Six documents lus (C01–C06), six sha256 conformes au registre, tous en vision (scans, pdftotext vide).
- Six transcriptions fidèles sous `content/programmes-officiels/examens-nationaux/9eme-base/arabic/` (2024/2025/2026 × generale/technique) ; snapshots dans `/tmp/claude-0/argis/snapshots/9web.edunet.tn/`.
- 62 lignes (C01 11, C02 10, C03 13, C04 9, C05 11, C06 8) + six `.meta` dans `lines/` ; contrôle : 10 colonnes, aucun nombre à deux chiffres en archétype/piège, archétype ≤ 12 mots.
- `reader-context.md` régénéré (17 chapitres du manifeste + 2 dossiers hors manifeste, carte des épreuves 2024-2026).
- Choix de découpage : une ligne par question notée (n°exo `partie.question`) ; quand le barème n'est donné que pour la question entière, ses sous-parties portent `-`.
- Points d'attention : (1) les sous-parties a/b de certaines questions n'ont pas de barème propre ; (2) les épreuves techniques interrogent des acquis de 7ᵉ-8ᵉ (مفعول مطلق/لأجله، الجمع، الإسناد) marqués `HP:` et `[hors programme en vigueur : …]` — à arbitrer : hors programme de la classe mais au programme de l'examen ; (3) vocalisation transcrite telle que visible à 220 DPI, sans correction (ex. graphies fautives d'origine conservées).

## 2026-10-14 — lot 2 : C07–C12 (2023 à 2020)

- Téléchargement (`curl -g`, http) des six PDF dans `/tmp/claude-0/argis/src/` : les six sha256 = registre ; pdftotext vide partout (scans) → vision 150 DPI, texte support et tableaux denses relus à 220 DPI.

| id | session | sha256 (préfixe) | pages | mode | état |
| --- | --- | --- | --- | --- | --- |
| C07 | 2023 générale | fa566115 | 4 | vision | lu, sha OK |
| C08 | 2023 technique | 1677ff10 | 4 | vision | lu, sha OK |
| C09 | 2022 technique | 81f58b1f | 3 | vision | lu, sha OK |
| C10 | 2021 technique | 4acf7b88 | 3 | vision | lu, sha OK |
| C11 | 2020 générale | dc7cec04 | 1 | vision | lu, sha OK |
| C12 | 2020 technique | b2de6b28 | 3 | vision | lu, sha OK |

- C07 (2023 générale) — LU. Transcription `2023-generale.md` ; 12 lignes (n°exo `partie.question` comme C01 : 1.x compréhension 4 pts, 2.x langue 6 pts, 3 production 10 pts ; le sujet imprime deux grandes parties I/II de 10 pts, la partie I contenant compréhension + langue). Format ACTUEL (فهم حجاجيّ / اللغة / إنتاج حجاجيّ) : la carte du reader-context vaut aussi pour 2023 (confirmée). Texte argumentatif, vocalisé, transcrit à 220 DPI. Toutes les notions de langue au programme (شرط، استفهام، معاني المزيد، النسبة والمصدر الصناعي).
- C08 (2023 technique) — LU. Transcription `2023-technique.md` ; 12 lignes. Format technique identique à 2024-2026 (1 h, coef 1, الأسئلة 14 + تحرير فقرة 6). Texte narratif (récit). Langue : البناء للمجهول، حروف الجرّ ومعانيها, المفعول المطلق, accord/duel marqués `HP:` et `[hors programme en vigueur : …]` ; seuls الحال et المفعول فيه rattachés au manifeste (03).
- C09 (2022 technique) — LU. Transcription `2022-technique.md` ; 11 lignes. Même ossature 14 + 6, texte narratif. Langue mêlée : أمر/نهي (04) et دلالة الزمان (لن، س) au programme ; conjugaison, النعت, المفعول لأجله `HP:`. Format : mixte (ossature technique actuelle, contenu de langue ancien).
- C10 (2021 technique) — LU. Transcription `2021-technique.md` ; 10 lignes. Même ossature, texte narratif. Programme ancien (notions HP dominantes) : المثنّى + accord (01 + HP), conjugaison, المفعول لأجله ; seul الحال (03) au manifeste. Distinction : la question de compréhension 1.1 est un choix de phrase-résumé, la 1.4 demande des قرائن.
- C11 (2020 générale) — LU. Transcription `2020-generale.md` ; 1 ligne. Format ANCIEN : l'épreuve s'intitule « الإنشاء العربي » (2 h, coef 2), une seule page, un sujet unique de production (dialogue argumentatif à transcrire), sans texte, sans compréhension, sans langue ; barème non imprimé (noté `-`). Seule notion mobilisée : le chapitre 09 (production argumentative).
- C12 (2020 technique) — LU. Transcription `2020-technique.md` ; 10 lignes. Ossature 14 + 6 ; texte dialogué (extrait de roman). Programme ancien (HP dominantes) : تصريف avec les pronoms, الجمع المؤنث, المفعول المطلق ; seul المفعول فيه للزمان (03) au manifeste. La technique 2020 mêle déjà compréhension et langue en une seule partie « الأسئلة ».

### Bilan du lot 2 (2026-10-14)

- Six documents lus (C07–C12), six sha256 conformes, six transcriptions sous `content/programmes-officiels/examens-nationaux/9eme-base/arabic/` (`2023-generale`, `2023-technique`, `2022-technique`, `2021-technique`, `2020-generale`, `2020-technique`), six snapshots dans `/tmp/claude-0/argis/snapshots/9web.edunet.tn/`.
- 56 lignes (C07 12, C08 12, C09 11, C10 10, C11 1, C12 10) + six `.meta` ; contrôle : 10 colonnes, aucun nombre à deux chiffres en archétype/piège, archétype ≤ 12 mots. Barèmes recoupés : chaque épreuve totalise 20 (C11 : non imprimé).
- Points d'attention : (1) pour les techniques 2020-2023, les acquis de 7ᵉ-8ᵉ sont plus nombreux qu'en 2024-2026 (passif, prépositions, conjugaison) ; (2) C11 n'a aucune partie de langue ni de compréhension : seule la production compte pour le chapitre 09 ; (3) les C09 à C12 n'ont pas de manuel révisé à citer : les notions sont rattachées aux slugs du manifeste quand elles y existent (أمر/نهي, دلالة الزمان, الحال, المفعول فيه), sinon `HP:` ; (4) les mots soulignés rendus `<u>…</u>` ; vocalisation transcrite telle qu'imprimée (quelques graphies d'origine conservées, par ex. « نطرقع »).
