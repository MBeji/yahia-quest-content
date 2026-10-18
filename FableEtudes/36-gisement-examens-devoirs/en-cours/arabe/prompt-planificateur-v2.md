Tu es le **PLANIFICATEUR** du gisement (étude 36) pour le couple 9ᵉ × arabe (matière `arabic`), **vague 2** : sessions anciennes C13–C40 (2002–2019 ; 2004 et 2001 introuvables) et devoirs D01–D06. Étapes G3–G4 : carte et écart, puis plan. Tu n'écris AUCUN exercice.

**Entrées**
- Consignes : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement.md` (G3, G4, missions fusionnées, « ne pas redemander », plafond par mission, règle des 30 % de signatures neuves) et `references/gisement-lecteur.md`.
- **Vague 1, déjà publiée (à ne pas redemander)** : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/PLAN.md` (règles R1–R…), `plan-examens-v1.json` (32 missions m001–m032), et les missions publiées `content/arabic/*/exercices/*` (sur `origin/main` du dépôt `/home/user/yahia-quest-content`, ou dans `/home/user/wt-ar2/content/arabic/`, identique).
- Sujets lus de la vague 2 : transcriptions `/home/user/wt-ar2/content/programmes-officiels/examens-nationaux/9eme-base/arabic/` (2002–2019 ; texte support RÉSUMÉ, intégral dans le PDF officiel, URL au registre) ; lignes et journaux `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/lecture-9eme/arabe/` (`lines/C13…C39.tsv`, `lines/D01…D06.tsv`, `JOURNAL-lecture-C13-C20.md`, `-C21-C28.md`, `-C29-C40.md`, `-devoirs.md`). Les lignes C01–C12 ont été converties au format valide (même dossier).
- Contenu : `content/arabic/` (17 chapitres au manifeste + `01-i3rab-wal-bina` et `06-al-mushtaqqat` hors manifeste ; dans les lignes, ces deux dossiers sont notés `HP:i3rab-wal-bina` et `HP:mushtaqqat`), manifeste `9eme-base.json`, `cours.md` de chaque chapitre.
- Registre `/home/user/wt-ar2/content/programmes-officiels/sources-externes/web-9eme-base-arabic/gisement.json` (missions m001–m032 `publiee` ; documents à jour) ; fiche `…/fiche.md`.
- Modèles de forme : le plan arabe v1 ci-dessus, et le plan anglais `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/PLAN.md` (missions fusionnées multi-sessions, liste « ne pas redemander », lot devoirs en salle blanche).

**Ce que les lecteurs ont constaté (à vérifier, puis à exploiter)** :
- Générales et épreuves uniques 2002–2019 (16 sujets) : **production seule** (« الإنشاء العربي », 2 h, coef 2), toujours un **dialogue argumentatif** à rédiger, sans texte, compréhension ni langue, sans barème.
- Techniques 2009–2019 (10 sujets) : compréhension d'un **texte narratif** + « تحرير فقرة » ; langue presque entièrement d'acquis 7ᵉ-8ᵉ (`HP:`) : duel, pluriel, conjugaison, مفعول مطلق ; seul الحال (03) au manifeste.
- Devoirs (6) : notions du manuel révisé (18 dalalat az-zaman, 03, 17, 19, 15, 16, 12, 13, 14, 05, 04) — c'est la seule source de la vague 2 pour la grammaire au programme.

**Décisions du pilote déjà prises** :
- Les 5 devoirs antérieurs au programme révisé sont **gardés** (notions au manifeste) ; plafond par auteur tenu (Chabbi D03+D05).
- Notions `HP:` d'acquis 7ᵉ-8ᵉ : **aucune mission** (programme ancien), sauf si elles tombent exactement dans un dossier existant (`01-i3rab-wal-bina`, `06-al-mushtaqqat`) ET qu'aucune mission ne les y pose déjà — propose-le alors au pilote, ne le planifie pas d'office.
- **Profondeur avant volume** : une session ancienne qui ne fait que redire ce que la vague 1 pose déjà ne donne rien. Le plan peut légitimement être court.

**Questions auxquelles le plan répond (avec chiffres)** :
1. **Productions** : les 16 sujets de dialogue argumentatif (+ les paragraphes des techniques) apportent-ils un archétype que les missions de production de la vague 1 (chapitre 09) ne couvrent pas ? Si oui : combien de missions de **préparation fermée** (thèse de chaque interlocuteur, arguments pertinents `multi`, ordre des répliques `ordering`, connecteurs, ponctuation du dialogue, formule de clôture…), regroupées par archétype, sujets cités.
2. **Compréhension** : quels textes techniques valent une mission (au plus 3, les plus riches et non redondants avec les 11 textes de la vague 1), au chapitre 10 ou au chapitre dont la notion domine ; une mission par texte, une à deux phrases citées par question.
3. **Devoirs** : cartes D0x#n, missions de devoirs `NN-devoir-<slug>.json` en salle blanche, avec liste « ne pas redemander » (vague 1 + missions planifiées ici) ; mesure des signatures neuves (règle des 30 %) et recommandation sur une vague 3.
4. Registre de ce qui est écarté et pourquoi (sessions entières comprises).

**Sorties** :
- `…/web-9eme-base-arabic/fiche.md` § 3 (ajout « vague 2 »), sans réécrire la vague 1 ;
- `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/PLAN-v2.md` et `plan-examens-v2.json` (ids `m033`…) ;
- registre : nouvelles missions `planifiee` (id = source de base, `sources`, `chapitre`, `fichier` proposé dont le n° suit les fichiers existants du chapitre, `etage`, `etapes`, `lot` `L06`…, `nn`, `note`) ; ne touche ni aux missions publiées ni à `documents` ;
- affectations `assign-arabe-L06.md`… (4 à 6 missions par lot) et `assign-arabe-devoirs.md`, cartes complètes (sources, phrases officielles à reprendre, piège, « ne pas redemander », étage, nombre de questions).

**Contrôles** : `content:gisement:controle` (depuis `/home/user/eng-svtses`, après `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh`, avec `--content /home/user/wt-ar2/content` si accepté) contre les transcriptions et `/tmp/claude-0/devoirs-snapshots/arabic/` : 0 plage de 8 mots contre les devoirs dans tes sorties ; `content:check -- --content …` (ou équivalent) vert.

Écris au fil de l'eau. Aucune écriture git, rien sous `content/arabic/`. Rapport final court en français : missions par lot et par chapitre, ce qui est écarté et pourquoi, propositions soumises au pilote, mesure des signatures neuves.
