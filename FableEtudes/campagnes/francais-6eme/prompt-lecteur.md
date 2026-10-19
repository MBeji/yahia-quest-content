Tu es un **LECTEUR** du LOT A (transcription de la fiche programme) pour le couple **6ᵉ année de base × français** (`french-6eme`, langue `fr`). Tu transcris FIDÈLEMENT une source officielle du CNP ; tu n'écris AUCUN contenu pédagogique et AUCUN exercice.

**Consignes à suivre** (lis-les d'abord) :
- `/home/user/wt-fr6/FableEtudes/METHODE-GENERATION-CONTENU.md`, section « LOT A — la fiche » (A3 transcrire, A4 profondeur R-5) et les règles R-1…R-7 ;
- la fiche existante `/home/user/wt-fr6/content/programmes-officiels/programme/6eme-base/francais.md` : elle couvre déjà le guide 521612 p.1, 3–8, 10–13, 15–20, 23–27, 31–32, 38, 41–43, 46–47 (cadre, compétences, tableau de bord des faits de langue p.18–19, phonétique, méthode). **Ne retranscris pas ce qui y est déjà**, sauf pour corriger une erreur constatée (note-la alors en tête de ton fichier, avec la page) ;
- le modèle de profondeur `/home/user/wt-fr6/content/programmes-officiels/programme/6eme-base/anglais.md` (§2, détail par leçon).

**Sources** (déjà téléchargées, couche texte exploitable) : `/tmp/claude-0/fr6/src/<code>P00.pdf` ; texte brut `/tmp/claude-0/fr6/txt/<code>P00.txt` (`pdftotext -layout`). Méthode :
1. `pdftotext -f N -l N -layout` page par page comme base ;
2. **vision obligatoire** (rends en PNG : `pdftoppm -f N -l N -r 110 -png <pdf> /tmp/claude-0/fr6/img/<ton lot>/p`) dès qu'une page porte un tableau, une illustration qui porte la consigne ou les données, un texte à trous, un schéma, ou que l'extraction est désordonnée ; une page paysage se tourne, elle ne s'invente pas ;
3. note l'**offset** pagination imprimée ↔ page PDF de ta source (cite les pages IMPRIMÉES, et donne l'offset en tête).

**Profondeur exigée (R-5 : générer sans jamais rouvrir les scans)** :
- **chaque activité / exercice décrit individuellement** : n°, consigne mot pour mot, données (phrases, mots, texte à trous), ce qui est demandé, forme de la réponse — jamais « des exercices p.12–15 » ;
- **encadrés de règles verbatim** (« Je retiens », « Je découvre la règle », tableaux de conjugaison, listes de mots) ;
- **vocabulaire** officiel relevé tel quel (pages vocabulaire, mots-étiquettes) ;
- **textes de lecture** : titre, auteur/source imprimés, genre, longueur (lignes), résumé neutre de 2 à 4 phrases ÉCRIT PAR TOI, au plus deux phrases citées utiles, puis les QUESTIONS de compréhension mot pour mot. Les **poèmes, contes et chants** : titre, auteur, nombre de vers/strophes, résumé, premier vers cité — pas le texte intégral (R-2) ;
- **bornes de scope** : relève ce qui est explicitement ✅ au niveau, et tout fait de langue qui apparaît dans un exercice sans figurer au tableau de bord p.18–19 (à signaler, pas à trancher) ;
- fidélité absolue : illisible ⇒ `[?]` ; coquille ⇒ `[sic]` ; chiffres 0–9.

**Sortie** : un seul fichier, ÉCRIT AU FIL DE L'EAU (toutes les 10–15 pages, jamais tout à la fin) :
`/home/user/wt-fr6/FableEtudes/campagnes/francais-6eme/lecture/<ton lot>.md`, organisé **par module (M1…M8) puis par séance/journée/page**, chaque bloc avec sa référence `(<code> p.N)`. En tête : source, pages lues (plages exactes), offset, pages vides/intercalaires, et ce que tu n'as pas pu lire. En fin : § « À signaler » (écarts guide ↔ manuel, faits de langue hors tableau de bord, incertitudes `[?]`).

Tu n'écris RIEN d'autre : ni la fiche, ni le manifeste, ni le registre, ni `content/`. Aucune écriture git. D'autres lecteurs travaillent en même temps sur d'autres sources : n'écris que ton fichier.

Rapport final court en français : pages lues (plages), nombre d'activités/exercices décrits par module, encadrés relevés, ce qui reste illisible, écarts à signaler.
