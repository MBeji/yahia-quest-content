# Journal de lecture — gisement 9ᵉ × arabe (étude 36, G2), lot C29–C40 (2010 à 2001)

Tenu au fil de l'eau par le lecteur (2026-10-18). Sources, rendus et snapshots hors dépôt : `/tmp/claude-0/arlec2/`.

## Téléchargement (`curl -g`, http) et sha256

| id | session | sha256 (préfixe) | pages | état |
| --- | --- | --- | --- | --- |
| C29 | 2010 générale | 8a28935d | 1 | sha = registre |
| C30 | 2010 technique | 76ac13fa | 2 | sha = registre |
| C31 | 2009 générale | 507874c3 | 1 | sha = registre |
| C32 | 2009 technique | 36b93e50 | 2 | sha = registre |
| C33 | 2008 unique | 3da1ee3e | 1 | sha = registre |
| C34 | 2007 unique | 0d1b5df8 | 1 | sha = registre |
| C35 | 2006 unique | 76497be3 | 1 | sha = registre |
| C36 | 2005 unique | 979169a9 | 3 | sha = registre |
| C37 | 2004 unique | — | — | INTROUVABLE (confirmé) |
| C38 | 2003 unique | 47bffb69 | 1 | sha = registre |
| C39 | 2002 unique | 9e60f7be | 1 | sha = registre |
| C40 | 2001 unique | — | — | INTROUVABLE (confirmé) |

Tous les documents lus sont des scans : `pdftotext` vide ou quasi vide → vision, 150 DPI (suffisant : textes gros et nets).

## Documents introuvables, retentés depuis la page du portail

- **C37 (2004)** : la page du portail (`http://9web.edunet.tn/`) porte bien le lien `…/2004/arabe.pdf`, mais le serveur répond 404 en http comme en https (variantes de casse, `www.` : 404). Le lien voisin `…/2004/arabe_c.pdf` répond 200 : c'est le **corrigé** (« إصلاح الموضوع », 3 pages, barème 6 pts pour la partie compréhension/développement, sujet « الإنشاء العربي » de type dialogue argumentatif). Ce n'est pas le sujet : corrigé non repris (règle R-2), aucune ligne, aucune transcription. Statut gardé : introuvable.
- **C40 (2001)** : le lien `…/2001/arabe.pdf` existe sur le portail et répond 200, mais le fichier fait 0 octet (`Last-Modified` 2007, `Content-Length` absent, sha256 = celui du vide e3b0c442…). Rien à lire. Statut gardé : introuvable (fichier vide côté portail).

## Lecture

- **C29 (2010 générale)** — LU. Épreuve « الإنشاء العربي » (2 h, coef 2), une page, un sujet unique de dialogue argumentatif (convaincre un camarade de répondre à un appel à la solidarité) ; ni texte, ni compréhension, ni langue ; barème non imprimé. **Une ligne** (n°exo 1, chapitre 09).
- **C30 (2010 technique)** — LU. 1 h, coef 1, 2 pages ; texte narratif (extrait « العَبيثة », ~13 lignes) puis 6 questions : titre (2), remplacement de trois expressions soulignées (3), cause d'un choix (2), relevé d'indices de caractère (4), but second (3), تحرير فقرة de 10 lignes — un rapport d'activité (6) ; total 20. Aucune question de langue (ni grammaire ni morphologie) : compréhension et production seulement. **6 lignes** (chapitres 10 et 09). Transcription sans texte intégral (résumé + une citation).
- **C31 (2009 générale)** — LU. « الإنشاء العربي », une page, dialogue argumentatif (convaincre un voisin négligent). **1 ligne**.
- **C32 (2009 technique)** — LU. 1 h, coef 1 ; texte narratif à la première personne (extrait « عيد المساعيد », ~12 lignes) ; 6 questions : titre (2), emploi de trois mots dans des phrases (3), effet sur le narrateur (3), conditions de réussite d'un projet (3), explication d'une crainte + avis (3), فقرة 7-10 lignes sur un projet rêvé (6) ; total 20. La question sur l'emploi de trois mots est du lexique, hors manifeste : `HP:lexique`. **6 lignes**.
- **C33 (2008 unique)** — LU. Intitulée « العربية » (et non « الإنشاء »), mais même nature : un seul sujet (relater un échange sur l'ouverture aux cultures, puis transcrire le dialogue). **1 ligne**.
- **C34 (2007 unique)** — LU. « الإنشاء », une page, dialogue : deux avis opposés (fidélité aux martyrs) à transcrire en appuyant le sien. **1 ligne**.
- **C35 (2006 unique)** — LU. « الإنشاء », une page, dialogue (convaincre un ami hostile à Internet). **1 ligne**.
- **C36 (2005 unique)** — LU. « الإنشاء », sujet en page 1 (récit puis dialogue avec un parent autour de l'engagement d'une mère) ; les pages 2-3 du PDF sont le **corrigé officiel** (grille : 6 + 6 + 7 + 1 = 20, partie compréhension/développement/construction/langue/présentation). Corrigé consigné au snapshot seulement, non repris dans la transcription. **1 ligne** (barème `-` : non imprimé au sujet).
- **C38 (2003 unique)** — LU. « الإنشاء », une page, dialogue (convaincre un proche de l'intérêt de la musique). **1 ligne**.
- **C39 (2002 unique)** — LU. « الإنشاء العربي », une page, sujet unique : décrire un comportement (recours à des charlatans) et son effet, puis exposer les arguments de persuasion. `pdfinfo` rapporte 0 page (xref atypique) mais `pdftoppm` rend la page ; sha = registre. **1 ligne**.

## Bilan

- 10 documents lus (C29–C36, C38, C39), sha256 tous conformes ; C37 et C40 restent introuvables (retentés).
- 10 transcriptions sous `content/programmes-officiels/examens-nationaux/9eme-base/arabic/` : `2010-generale`, `2010-technique`, `2009-generale`, `2009-technique`, `2008`, `2007`, `2006`, `2005`, `2003`, `2002` (les épreuves « unique » n'ont pas de suffixe de filière).
- 20 lignes (C29 1, C30 6, C31 1, C32 6, C33 1, C34 1, C35 1, C36 1, C38 1, C39 1) + 10 `.meta` ; validateur : 20 valides, 0 fautive.
- Épreuves « الإنشاء العربي » seul : huit (2010 G, 2009 G, 2008, 2007, 2006, 2005, 2003, 2002), toutes de type dialogue argumentatif, une ligne chacune au chapitre `09-al-intaj-al-kitabi` (étage d3, barème `-`).
- Part HP : 1 ligne sur 20 (`HP:lexique`, C32 Q2). « Programme ancien » : les huit épreuves de production seule (format antérieur au manuel révisé) ; les deux techniques 2010 et 2009 ne contiennent aucune notion de langue.
- Notions par chapitre : `09-al-intaj-al-kitabi` 10 lignes (8 productions, 2 paragraphes techniques) + 1 en association ; `10-fahm-wa-intaj` 9 lignes (titre, synonymes en contexte, relevé d'indices, avis) ; aucune ligne sur les chapitres de langue (15 à 19, 02-05, 07, 08, 12-14).
- Difficultés : aucun problème de lisibilité (scans propres) ; vocalisation des consignes transcrite telle qu'imprimée (partielle) ; les consignes du texte technique (guillemets « سعيدة », noms de personnages) sont dans le snapshot hors dépôt, les transcriptions n'en gardent que résumé et une citation courte. Convention n°exo = rang, `HP:mushtaqqat` / `HP:i3rab-wal-bina` du correctif du coordinateur : sans objet ici (aucune notion de ces dossiers dans le lot).
