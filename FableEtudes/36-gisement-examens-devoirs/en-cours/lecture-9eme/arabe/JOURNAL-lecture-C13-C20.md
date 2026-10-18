# Journal de lecture — gisement 9ᵉ × arabe (étude 36, G2), lot C13–C20 (sessions 2019 à 2016)

Tenu au fil de l'eau par le lecteur, 2026-10-18. Rendus et sources hors dépôt : `/tmp/claude-0/arlec2/` (`src/`, `render/`, `snapshots/`).

- Téléchargement (`curl -g`, http) des huit PDF : les huit sha256 = registre `docs.json`. `pdftotext` : 1 caractère (scans) → vision 150 DPI pour tout (les huit documents sont nets ; aucune page n'a eu besoin de 220 DPI, le texte support des techniques n'étant pas transcrit).
- Correctif reçu en cours de lecture : `HP:mushtaqqat` / `HP:i3rab-wal-bina` à la place des slugs hors manifeste ; n°exo = rang, lettre de sous-question permise. Appliqué (aucune ligne ne porte `06-` ni `01-`).

| id | session | sha256 (préfixe) | pages | mode | format | lignes |
| --- | --- | --- | --- | --- | --- | --- |
| C13 | 2019 générale | 841486f5 | 1 | vision | « الإنشاء العربي » seul | 1 |
| C14 | 2019 technique | 022c4f74 | 2 | vision | 14 + 6 | 10 |
| C15 | 2018 générale | f476c2c2 | 1 | vision | « الإنشاء العربي » seul | 1 |
| C16 | 2018 technique | 0faff4b7 | 2 | vision | 14 + 6 | 11 |
| C17 | 2017 générale | 93717033 | 1 | vision | « الإنشاء العربي » seul | 1 |
| C18 | 2017 technique | a8abfe2d | 2 | vision | 14 + 6 | 11 |
| C19 | 2016 générale | cde2f06f | 1 | vision | « الإنشاء العربي » seul | 1 |
| C20 | 2016 technique | 58803f63 | 2 | vision | 14 + 6 | 10 |

## Constats

- **Générales 2016-2019 (C13, C15, C17, C19)** : toutes sur le format ancien, comme C11 (2020) : une page, 2 h, ضارب 2, un sujet unique de production (dialogue argumentatif : réfuter ou faire changer d'avis un proche), sans texte, sans compréhension, sans langue, sans barème. Une ligne chacune (n°exo 1, chapitre `09-al-intaj-al-kitabi`, étage d3). Programme : ancien (production seule). Transcription = consigne en entier, vocalisation telle qu'imprimée (graphies d'origine conservées : « أَخَاكَ » après « مَا إِنْ بَلَغَ » en 2018, « تَلْفَزِيًّا » en 2019).
- **Techniques 2016-2019 (C14, C16, C18, C20)** : ossature 14 + 6 (« الأسئلة » 14 pts mêlant compréhension et langue, « تحرير فقرة » 6 pts, 1 h, ضارب 1, deux pages `2/1`, `2/2`), identique à 2020-2023. Texte narratif (aucun argumentatif). Barèmes recoupés : chaque technique totalise 14 + 6 = 20. Deux barèmes de 1.5 (C18 2b et 6) conservés tels qu'imprimés.
- **Notions par chapitre** : `10-fahm-wa-intaj` (titre, synonymes/contraires en contexte, relevés d'indices, explications, avis) sur toutes les techniques ; `09-al-intaj-al-kitabi` (production, et justification d'avis) ; `03-al-mansoubat` seulement en C14 (الحال). Aucune des notions de langue de ces quatre techniques n'est au manifeste hors الحال.
- **HP / programme ancien** : duel et accord (`HP:i3rab-wal-bina`, C14 3a, C16 3b, C18 3b), conjugaison avec les pronoms et impératif (`HP:tasrif-al-fi3l-ma3a-ad-damair` C14 3b, C18 3a ; `HP:isnad-ila-ad-damair` C20 3b), pluriel (`HP:jam3` C16 3a, C18 3b, C20 3a), complément absolu (`HP:maf3ul-mutlaq` C14 3c, C16 3c, C20 3c), expression figée (`HP:mufradat` C18 2c). Programme ancien : notions HP dominantes en C14, C16, C18, C20. Aucune ligne `HP:mushtaqqat` (pas de question sur المشتقّات dans ce lot).
- **Conventions** : n°exo = rang, avec lettre pour 2a/2b/3a/3b/3c ; production écrite = dernière ligne (n°7 en technique, 1 en générale) ; barème `-` partout en générale (non imprimé).

## Difficultés

- C18 3a : la voyelle finale de la première personne du tableau de conjugaison n'est pas lisible à 150 DPI ; transcrite `أَنْتَ` avec une note `[illisible]` ; sans effet sur les lignes TSV.
- C14 3a : l'ensemble exact des mots soulignés de la phrase à mettre au duel est difficile à distinguer (quatre mots rendus : تَتَحَوَّلُ، طَاوِلَةً، إِطَارًا، لِصُورَةٍ) ; à confirmer par l'orchestrateur si la reprise en dépend.
- Texte support non transcrit (règle du 2026-10-16) : référence, longueur estimée (« environ 20-25 lignes », comptage non fait), résumé neutre ; mention « النصّ كاملاً : الوثيقة الرسمية، sha256 في السجلّ ».
- Snapshots `/tmp/claude-0/arlec2/snapshots/C13…C20.txt` = copie des transcriptions (hors dépôt).

## Bilan

Huit documents lus, huit sha conformes, huit transcriptions (`2016/2017/2018/2019-generale.md` et `-technique.md` sous `content/programmes-officiels/examens-nationaux/9eme-base/arabic/` dans `/home/user/wt-ar2`), 46 lignes (C13 1, C14 10, C15 1, C16 11, C17 1, C18 11, C19 1, C20 10) + huit `.meta`. Validation `content:gisement:lignes` : 46 valides, 0 fautive.
