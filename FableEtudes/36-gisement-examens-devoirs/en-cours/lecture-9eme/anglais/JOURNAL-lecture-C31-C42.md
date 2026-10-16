# Journal du lecteur — anglais 9ᵉ, lot C31 à C42 (2010 et 2009 générale/technique ; 2008 à 2001 filière unique)

Étape G2. Lecture du 2026-10-16. Conventions : § 0 de `JOURNAL-lecture-C01-C06.md`, reprises à la lettre (grain, n°exo, barème, étages, chapitres, jeton HP) ; les écarts sont notés au § 4.
Les onze PDF lus sont des scans sans couche texte (`pdftotext` rend 4 à 512 octets) : lecture en vision, 150 DPI, une fois par page. Téléchargements `curl -g`, http, sans `-k`. Aucune écriture git, rien sous `content/english/` hors les transcriptions.

## 1. Documents lus

| id | session | filière | sha256 (= registre ?) | pages | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- |
| C31 | 2010 | générale | 75886150…5e86 (oui) | 4 | 5 | `english/2010-generale.md` |
| C32 | 2010 | technique | 7d1741ef…1129 (oui) | 4 | 5 | `english/2010-technique.md` |
| C33 | 2009 | générale | e8682bca…3e03 (oui) | 4 | 5 | `english/2009-generale.md` |
| C34 | 2009 | technique | 0444c4bc…5544 (oui) | 4 | 5 | `english/2009-technique.md` |
| C35 | 2008 | unique | 88358309…5e52 (oui) | 4 | 5 | `english/2008-unique.md` |
| C36 | 2007 | unique | 754de247…80f (oui) | 4 | 5 | `english/2007-unique.md` |
| C37 | 2006 | unique | 7e5a32b9…8d48 (oui) | 4 | 5 | `english/2006-unique.md` |
| C38 | 2005 | unique | 9181ae21…293f (oui) | **8** (confirmé) | 5 | `english/2005-unique.md` |
| C39 | 2004 | unique | — (aucun fichier) | — | 0 | aucune |
| C40 | 2003 | unique | cbbd5ff4…ee39d (oui) | 4 | 5 | `english/2003-unique.md` |
| C41 | 2002 | unique | 26607889…bf6 (oui) | 4 | 5 | `english/2002-unique.md` |
| C42 | 2001 | unique | e01d6c98…a42a (oui) | 4 | 5 | `english/2001-unique.md` |

(sha complets = ceux de `docs.json`, comparés un à un par `sha256sum` : onze identiques.) Transcriptions sous `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/`.
Snapshots locaux : `/tmp/claude-0/enlec/snapshots/C3{1..8}.txt`, `C4{0..2}.txt` (copie de la transcription : le texte support complet n'est pas conservé, filtre du 2026-10-16). Lignes : `lines/C3{1..8}.tsv`, `lines/C4{0..2}.tsv` + `.meta` (**55 lignes** ; `content:gisement:lignes --subject english --grade 9eme-base --content /home/user/wt-en/content` : 55 valides, 0 fautive).

## 2. C39 (2004) : statut proposé = « introuvable » (sujet), corrigé officiel partiel disponible

- `http://9web.edunet.tn/2004/anglais.pdf` répond **404** (testé aussi `Anglais.pdf`, `.PDF`, `/2004/general/…`) ; la page d'accueil de `9web.edunet.tn` liste pourtant ce lien, mort. Pages non connues, aucun sha : rien n'est inventé, **aucune ligne, aucune transcription** pour C39.
- Le portail liste à côté `http://9web.edunet.tn/2004/anglais_c.pdf` (200, 559 408 octets, 2 pages, titre PDF « an_corrige.doc », sha256 `355b7b8cc75c687a4daa45bf27382723f7ce353920d8c5171901f1aaa7b5fdf9`) : c'est un **corrigé** (réponses en gras) qui n'est pas le sujet. Il confirme la structure de l'épreuve 2004 — compréhension 7 (vrai/faux 3 × 0,5 ; trois synonymes ; appariement énoncé/fonction ; deux référents ; paragraphe à compléter par quatre mots du texte), langue 8 (3 : banque de sept mots pour six lacunes ; 3 : choix de six mots ; 2 : appariement de quatre items, un intrus), écriture 5 (grille 2 + 2 + 1) — mais **ni le texte, ni les consignes complètes, ni les options du choix, ni le sujet d'écriture**. Insuffisant pour écrire des lignes fidèles : proposition de laisser C39 « introuvable » ; si le pilote veut une trace, un statut du type « corrigé seul » est le plus proche. Des corrigés `anglais_c.pdf` existent aussi pour 2003, 2005, 2006 (hors registre, non lus ; celui de 2005 est reproduit dans la copie manuscrite du PDF C38).

## 3. Format de l'épreuve, session par session

Toutes : durée imprimée 1 h (absente des PDF 2006 et 2003), coefficient 1, barème 20 = compréhension + langue (3 exercices) + écriture, texte support en 3 à 5 paragraphes (presse ou récit adapté, 190 à 300 mots). Aucune session n'a plus ni moins de trois exercices de langue.

| session | reading | langue (ordre imprimé) | writing |
| --- | --- | --- | --- |
| 2010 G | 6 (4 q : 1+2+2+1) | banque 3 ; appariement 2 ; choix 3 | article d'Earth Day, conseils (6) |
| 2010 T | 7 (4 q : 1+4+1+1) | banque 3 ; choix 3 ; appariement 2 | courriel de présentation à une correspondante (5) |
| 2009 G | 6 (5 q) | banque 3 ; appariement 2 ; options en marge 3 | lettre pour mettre en garde un fumeur (6) |
| 2009 T | 7 (3 q : 2+4+1) | banque 3 ; options en marge 3 ; appariement 2 | dépliant de règles de sécurité (5) |
| 2008 | 7 (5 q) | banque 3 ; options en marge 2.5 ; appariement 2.5 (5 items) | message de fête des mères (5) |
| 2007 | 7 (4 q, dont réponses courtes) | banque 2.5 ; appariement 3 (6 items) ; options en marge 2.5 | réponse conseillère à une lettre de lecteur (5) |
| 2006 | 7 (5 q) | banque 3 ; options en marge 3 ; appariement 2 (exemple donné) | lettre à un correspondant : les tenues en Tunisie (5) |
| 2005 | 7 (5 q, réponses brèves complètes) | choix en marge 3 ; appariement 2 (exemple donné) ; banque 3 | lettre de plainte sur la vie en ville (5) ; +4 pages de corrigé manuscrit |
| 2003 | 7 (5 q) | banque (2 en trop) 3 ; appariement 2 ; options en marge 3 | article de moyens de rester en forme (5) |
| 2002 | 7 (5 q, dont fonctions d'énoncés) | banque (2 en trop) 3 ; dialogue à compléter par choix 2.5 ; choix dans un texte 2.5 | récit d'un accident guidé par un tableau de notes (5) |
| 2001 | 7 (5 q) | choix dans un paragraphe 3 ; banque (2 en trop) 3 ; interview à compléter par liste 2 | préférence ville/campagne justifiée (5) |

Évolutions : le format 2024-2026 (reading 6 en générale, 8 en technique, 5 questions ; langue banque/choix/appariement ; 6 ou 5 en écriture) est déjà en place dès 2009-2010 (reading 6/7, 8 de langue) ; **avant 2009 il n'y a qu'une épreuve** (filière « unique »). Les sessions 2002 à 2005 n'ont **pas** d'exercice « mots à mettre en forme » ; 2002 et 2001 introduisent des formes de langue absentes ensuite (dialogue fonctionnel, interview, tableau de notes pour un récit). Le coefficient est 1 partout ; le texte est toujours un récit ou un reportage de la vie courante (famille, métier, école).

## 4. Conventions : écarts et ajouts

- **Aucun écart de grain** : n°exo 1 (reading), 2-4 (langue, rang d'ordre), 5 (writing) ; reading = une ligne, `09` seul ; barèmes 2.5 conservés (**6 lignes décimales** sur 55 : C35#3, C35#4, C36#2, C36#4, C41#3, C41#4).
- **Étages** : reading d1 si guidé sans production (C31, C32, C33, C34, C37), d2 si réponses courtes à rédiger, inférence ou valeur d'énoncé (C35, C36, C38, C40, C41, C42) ; cloze à banque d1 quand tout est lexical (C31#2, C36#2, C38#4, C40#2), d2 sinon ; writing 6 pts en générale d3, 5 pts d2. Aucun d4.
- **Nouveaux mots-clés HP** (au plus proche des deux fixés) :
  - `HP:reflexive-pronoun` (himself, myself : C34#3, C35#2), aligné sur le singulier déjà employé par C23 ;
  - `HP:object-pronoun` (me, him/his, it, them : C31#2, C36#2, C36#4, C41#4), aligné sur C26 et C28 ; je range donc les pronoms/possessifs qui sont la clé d'un item sous ce mot-clé, et non en `09` comme les déterminants (these/those) ;
  - `HP:language-functions` (C41#3 : choisir la réplique qui salue, répond à un compliment, invite, refuse) : fonction de communication, notion absente des dix chapitres ;
  - `HP:gerund` : C40#4 (« likes reading »), C41#4 (« enjoys helping ») ; le cas « let children cross » (C41#4, infinitif sans to) est de la même famille (schéma de complémentation du verbe), non scindé.
  - `HP:word-formation` : C31#4 (physically/physics/physical) seul.
- **Appariements** : `09` seul comme prescrit. Signal noté, non compté : C40#3 « He said ... she had the flu » (concordance pronom/discours rapporté simple), C37#4 « he'd be handicapped » (conditionnel), C38#3 « had to go » (modal).
- **Dialogue ou interview à compléter** (C41#3, C42#4) : C41#3 traité comme texte support (résumé + options mot pour mot, car le dialogue dépasse 8 lignes) ; C42#4 transcrit en entier (huit répliques, tableau). C42#4 classé `09` seul (questions/réponses d'information, pas de fonction à identifier).
- **Reading qui teste des fonctions** (C41 q4 : accord, incapacité/interdiction, suggestion ; C32 aucun) : noté, `09` seul comme C02 q3.
- **Writing** : C32 (courriel de présentation : nom, âge, école, matières, futur métier) en `09` seul — le « future job » mentionné n'impose pas le futur ; C35 (message affectueux) et C37, C42 (description ou opinion) en `09` seul ; `+04-modals` pour C31, C33, C34, C36, C40 (conseiller, avertir, règles, moyens d'agir) ; `+02-past-tenses` pour C41 (récit au passé) — première occurrence d'un writing `+02` dans le corpus des six premiers lots ; jamais 05/06.
- **Cloze ambigus** : C38#4 `04+09` (« can » ; « tall/taller » est un distracteur de degré, non compté pour 08) ; C35#3 `03+04+08+09` (« are dying / will die / must die » puis « the most important ») ; C37#3 `01+02+09` (« is leaving » vs « left », « have been … since ») ; C33#2 `04+08+09` (could, newest) ; C32#2 `01+02+09` (trains, has … been).

## 5. Notions par chapitre (lot C31-C42, 55 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 present tenses | C32#2 (trains), C37#3 (is leaving), C42#3 (take, meets) |
| 02 past tenses (+ present perfect) | C31#4 (used to spend), C32#2 (has been), C32#3 (has written, lasted), C34#2 (have, changed), C35#2 (suffered, hit), C37#3, C38#2 (ran, jumped, were), C40#4 (never married), C41#5 (récit), C42#2 (died) |
| 03 future | C35#3 (will die) seul |
| 04 modals | C31#5, C33#2 (could), C33#5, C34#5, C35#3 (must die), C36#5, C38#4 (can), C40#5, C42#2 (could) |
| 05 conditionals | jamais testé ; C37#4 (« he'd be handicapped ») dans un appariement |
| 06 passive voice | jamais |
| 07 reported speech | jamais testé en langue ; C40#3 (« He said she had the flu ») dans un appariement |
| 08 relatives & comparatives | C31#4 (more … than), C33#2 (newest), C35#3 (the most), C37#2 (easiest), C40#4 (who), C41#2 (largest, that, more) |
| 09 reading & writing | 11 readings, 11 writings, tous les appariements et lexicaux |
| 10 exam-style | non employé |

**Part HP** : aucune ligne entièrement HP ; **9 lignes sur 55** portent un jeton HP en complément (10 jetons : word-formation 1, reflexive-pronoun 2, object-pronoun 4, language-functions 1, gerund 2 ; C41#4 en porte deux) ; les mots-clés fixés par le pilote (word-formation, gerund) n'interviennent que 3 fois : les sessions anciennes testent moins la dérivation (une occurrence en 2010) que les pronoms et le lexique.
Programme : toutes les notions testées (temps, modaux, relatifs, comparatifs, superlatifs) restent dans le champ du guide 9ᵉ en vigueur ; aucune marque `[hors programme en vigueur]` posée dans les transcriptions. Le formatage « filière unique » (2008 à 2001) a disparu depuis 2009 ; ce n'est pas un changement de programme.
Chapitres jamais testés en langue sur 2001-2010 : 05, 06, 07 ; le futur une seule fois (C35#3) — comme sur 2024-2026 (01, 03, 05, 07), mais le **présent simple** y est un peu plus présent.

## 6. Difficultés et coquilles imprimées

Onze scans lisibles, aucune zone illisible, aucun `[illisible]`. Particularités : 2009 à 2008 portent un bandeau violet « edunet.tn » (ajout du site) ; 2007 à 2001 ont des PDF de sujets sans cadre d'en-tête complet (2006 et 2003 : ni durée, ni coefficient, ni pagination — 1 h présumée, notée au `.meta`) ; C38 (8 pages) : pages 1-4 vierges, 5-8 = copie remplie à la main (corrigé et grille de notation 2 + 2 + 1), transcrite en fin de document ; la banque de C37 compte huit mots pour six lacunes, celle de C36 six pour cinq.
Coquilles conservées : pagination « 4/1 … 4/4 » à l'envers (C32) ; « fourty-five » (C32) ; « Answer he letter » (C36 writing) ; « paragraphs 2 et 3 » (C37 q4) ; « Sami(a) @ gmail.com / Linda; white @ yahoo.co.uk » (C32) ; « 0,5 » avec virgule et « points/pts » (2003, 2002, 2001 : « 0.5 » avec point en 2001) ; « Be careful ! » (2003, 2002) ; consigne « Number ① is an example » avec exemple barré (C37, C38).
Une date d'impression du site « [04-06-2002] » figure en pied de la page 4 de C41.
Rien n'a vieilli dans les consignes : toutes les notions testées restent au programme actuel ; seuls changent la durée du texte et l'absence de l'exercice « mots à mettre en forme » avant 2025.
