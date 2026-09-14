# Étude 34 — Étoiles de chapitre & sceaux de matière : une progression qui ne recule jamais

> **Statut** : **brouillon** — écrite le 2026-09-14 ; Q-1…Q-5 ouvertes (§7). Le numéro 33 est
> pris par « la porte des questions ouvertes » (arena#1026, migrations `20260913120000` /
> `20260913130000`), dont le dossier n'est pas encore déposé ici.
> **Priorité** : 34 · **Valeur** : 🎯 l'élève ne voit plus jamais sa progression **reculer**
> quand du contenu arrive — plateforme, IA, parent ou lui-même ; il lit d'un coup d'œil ce
> qu'il a **acquis** par chapitre et par matière (étoiles, sceaux), ce que ça lui a **coûté**
> (effort), et ce qui reste **à découvrir** (nouveautés) — et son parent lit exactement la
> même chose · **Complexité** : moyenne+
> **Architecte** : Fable / 2026-09-14 · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : é22 (livrée — possède la doctrine du parcours ; **cette étude amende ses
> R-15/R-16/D-4**), é31 (livrée — badges vivants, primitives de célébration, catalogue i18n
> paresseux), é09 (en exécution — possède toute valeur d'économie : **aucune n'est touchée**),
> arena#987 (« 3/20 chapitres » — `student_chapter_gaps`), arena#1005 (porte du quiz définie
> une fois — `chapter_quiz_cleared`) · **Bloque** : rien de dur ; informe é08 volet enseignant
> (« taux de réussite par chapitre » devra lire les étoiles, pas un ratio) et le backlog go-live
> **GAP-037** (échelle de 50 niveaux nommés — lot 5, optionnel)
> **Docs normatifs liés** : AGENTS.md, ARCHITECTURE.md §8, `docs/doctrine-verticale.md`,
> `docs/suivi-parental-quotidien.md` § « Couverture du programme », `docs/content-voice-and-composition.md`
> (lexique, gabarits Hub / QG / Rapport), `docs/design-surfaces.md`,
> `content-engine/references/rewards-and-modes.md` (échelle ⭐ → ⭐⭐⭐⭐ du contenu)
>
> **Fiche de verticalité** (é26 D-2) :
> **Verticale** : V1 « apprendre & maîtriser » — **approfondissement** de la capacité
> « parcours élève & progression » (é22, 🟢 M2 dans STATUS §3), pas une ouverture : aucune
> surface nouvelle, aucun verrou, aucune économie ·
> **Maturité visée** : **M3** (pas signature — le plancher de tout ce qui est LIVE) ·
> **Boucles** : REFERME (a) la couverture parent « 3/20 chapitres », dont le chiffre était juste
> et illisible (arena#987) et qui **recule à chaque campagne de contenu** ; (b) l'injection de
> contenu, qui n'atteint aujourd'hui **aucun écran élève** (`content_releases` est privée,
> `exercises` n'a pas de date) — elle devient « ✨ nouveauté » ; (c) la métrique de garde
> KPI-E de é31 (« chapitres complétés / actif »), qui baisse mécaniquement quand le corpus
> grandit. OUVRE : aucune boucle sans consommateur — les deux tables du grand livre sont lues
> par quatre écrans (hub, carte, QG, suivi parental) dès les lots 2-3, et par `/admin/engagement`
> au lot 3 ·
> **Apport IA** : **rejeté motivé** (P-5a) — aucun LLM ne décide d'une étoile, d'un sceau ni
> d'un badge ; les mini-biographies de l'échelle nommée (lot 5) sont du **contenu hors ligne
> relu** (P-5c), pas une génération à l'exécution. Rien à l'exécution « pour l'instant ».

## 1. Contexte & objectif produit

### 1.1 Le problème, mesuré sur le code et le corpus

**La complétion recule quand le contenu avance.** Depuis é22 (R-15/R-16, 2026-07-20), un
chapitre est « complété » quand son quiz est validé **et que toutes ses missions de catalogue
sont réussies** ; la progression d'une matière est « chapitres complétés / chapitres publiés ».
Les deux nombres sont recalculés **à chaque lecture** sur la table `exercises` vivante
(`student_parcours_progress`, dernière révision `20260905130000` ; miroir client
`src/shared/lib/chapter-completion.ts`). Aucune colonne ne date une mission, aucune ne fige un
état atteint. Conséquences vérifiées :

1. **Ajouter une mission à un chapitre complété le dé-complète** pour tous les élèves qui
   l'avaient fini : le hub repasse de « Terminé ✓ » à « 5/6 », le nœud de `/parcours` perd son
   état `done`, la colonne « Programme » du parent baisse, et `chapters_per_active` de
   `/admin/engagement` — la métrique de garde de é31 R-1 — recule.
2. **Ajouter un chapitre** à une matière fait chuter le pourcentage de tous ceux qui
   l'avaient à 100 %.
3. **Ajouter un quiz** à un chapitre scolaire qui n'en avait pas rallume la porte
   rétroactivement : tous les chapitres complétés redeviennent incomplets.
4. **Retirer ou re-clé une mission** (`sql-builder` élague `source='admin'` puis ré-insère ;
   une mission renommée change d'UUID) supprime en cascade les tentatives qui la
   concernaient : ce que l'élève avait réussi n'existe plus nulle part.

Or le contenu **est fait pour grandir** : c'est la doctrine (é26 §6, « la largeur catalogue
est de la profondeur »), les campagnes tournent chaque semaine (`programme:etat`,
`/campagne`), et trois autres sources sont déjà là ou annoncées — les missions de la famille
(`source='parent'`, exclues des comptes depuis é22 mais présentes dans le chapitre), la Forge
IA (é29 — éphémère, jamais au catalogue), et demain l'élève lui-même. Un système de
progression qui **punit** l'ajout de contenu est en contradiction avec le produit.

**La barre est réglée sur l'élite.** Compté dans le corpus le 2026-09-14 (94 matières,
773 chapitres — tous avec quiz —, 3 574 missions) : **56 %** des missions sont ⭐⭐⭐ (boss,
1 211) ou ⭐⭐⭐⭐ (défi élite, 782) ; l'échelle dominante d'un chapitre est
⭐ · ⭐⭐ · ⭐⭐⭐ · ⭐⭐⭐ · ⭐⭐⭐⭐ (268 chapitres, 35 %) ; la médiane est 5 missions par chapitre.
La doctrine du contenu dit pourtant l'inverse de la règle de complétion :
`rewards-and-modes.md` — « keep **core progression at difficulty 1–2** ; reserve 3–4 for
boss/challenge ». Un chapitre n'est aujourd'hui « terminé » qu'au **défi élite**. C'est ce
qui a produit le « 3/20 chapitres » du 2026-09-04 : l'enfant du propriétaire avait « fait tous
les cours et tous les exercices » et le suivi ne lui comptait que trois chapitres — le calcul
était juste (4/6 missions → 0, quiz expédié → 0), le **sens** était faux, et arena#987 a dû
ajouter une liste de « ce qui manque » pour rendre le verdict lisible. Il reste un verdict.

**Il n'existe aucun jalon intermédiaire par matière.** Entre « une mission réussie » (XP,
immédiat) et « toute la matière à 100 % » (des mois), rien ne s'obtient et rien ne se garde :
pas d'étape « j'ai fait le socle de tous les chapitres », pas de trophée de matière, rien qui
distingue l'effort de l'exhaustivité. Les trois systèmes de maîtrise existants ne répondent pas
à cette question : la complétion (binaire, par chapitre, régressive), la maîtrise EWMA de é07
et les quatre états de croyance de é30 sont **par compétence**, taggés sur `math` seulement, et
volontairement sans pourcentage côté élève (é30 D-1). Aucun n'est clé sur (élève, chapitre) ni
(élève, matière).

**Ce qui est solide, et qu'on garde** : la porte du quiz définie une fois
(`chapter_quiz_gated` / `chapter_quiz_cleared`, arena#1005) ; « réussie ≥ 60 % / maîtrisée
100 % » (é22 R-14) ; « mission de catalogue = `source='admin'` hors quiz » ; la liste des
manques du parent (arena#987) ; les primitives de célébration et les badges vivants de é31 ;
la règle « le finalizer qui possède le fait décerne » ; l'échelle ⭐ → ⭐⭐⭐⭐ que **tout le
corpus porte déjà** dans ses titres et sa colonne `difficulty`.

### 1.2 Objectif produit

Qu'un élève — et son parent — lise en un écran, dans le même vocabulaire partout :

- **ce qu'il a acquis** : des **étoiles de chapitre** (1 à 4, une par palier de difficulté
  franchi) et des **sceaux de matière** (⭐ à ⭐⭐⭐⭐, quand **tous** les chapitres ont
  l'étoile), inscrits dans un **grand livre** dont **rien ne s'efface** ;
- **ce que ça lui a coûté** : des compteurs d'effort qui **montent** (missions réussies, XP de
  la matière, chapitres commencés et terminés) — jamais un pourcentage qui descend ;
- **ce qui reste à découvrir** : les **nouveautés ✨** — les missions et chapitres arrivés
  après ses étoiles, présentés comme une opportunité, jamais comme une dette ;
- **pourquoi un chapitre n'a pas encore sa prochaine étoile**, et le geste qui la donne.

Le tout **sans nouveau verrou** (é22 R-10), **sans nouvelle économie** (é22 R-28 → é09),
**sans nouvelle surface** (é26 P-7), et **sans reprendre quoi que ce soit à personne** au
passage (R-15).

### 1.3 Indicateurs de succès (P-6 — mesurés, ou dits « dette »)

| KPI       | Définition                                                                                                                                                                           | Où on le lit                                                                                | Cible                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **KPI-1** | **Zéro régression affichée** : aucun statut acquis (étoile, sceau, « terminé ») ne disparaît d'un écran après une application de contenu                                             | pgTAP (invariant sur décor), + compteur **« étoiles préservées »** (grand livre > vivant) sur `/admin/engagement` | 0 régression ; le compteur est la preuve visible que la promesse a servi           |
| **KPI-2** | Part des actifs 30 j ayant ≥ 1 chapitre **maîtrisé** (étoile ≥ 3) ; médiane de l'étoile des chapitres touchés                                                                        | `/admin/engagement` (lot 3)                                                                 | référence à établir au lot 3 (aucun chiffre n'existe)                             |
| **KPI-3** | Part des actifs 30 j ayant ≥ 1 **sceau** ; délai médian premier sceau                                                                                                                | `/admin/engagement`                                                                         | référence à établir — attendu faible en cours d'année (les sceaux sont **larges**) |
| **KPI-4** | **Garde** (é31 R-1) : précision moyenne et médiane des tentatives ne baissent pas après le lot 2                                                                                     | `/admin/engagement` (existant)                                                              | ≥ niveau d'avant (une étoile ne doit pas inciter à expédier — d'où R-3)            |
| **KPI-5** | « 3/20 » ne se reproduit pas : aucun signalement de lecture erronée de la couverture (`bug_reports`, retour propriétaire)                                                            | triage `report-triage` ; STATUS §6                                                          | 0 sur les 60 jours suivant le lot 3                                               |

### 1.4 Ce que l'epic ne cherche PAS à faire

- **Pas de nouveau verrou ni de prérequis** : étoiles et sceaux **décrivent**, ils
  n'ouvrent ni ne ferment rien (é22 R-10 reste entière).
- **Pas d'économie** : aucune XP, aucune pièce attachée à une étoile ou un sceau (R-11) ;
  registre é09 vide (§3.10).
- **Pas de refonte du hub** (GAP-043) ni de nouvelle route : on remplace des chiffres dans des
  blocs existants (gabarits Hub / QG / Rapport, é15).
- **Pas de modèle de compétence** : é07/é30 restent les seuls juges de « ce que tu sais » ;
  cette étude juge « ce que tu as **fait** » (R-19).
- **Pas de création de contenu** par l'élève ou l'IA : l'étude écrit la **règle** qui les
  accueillera (R-2), elle ne construit aucun canal (P-7).
- **Pas de classement par sceaux**, pas de push (é31 R-4), pas de saison.

## 2. Spécification fonctionnelle

### 2.1 Le modèle en une image

```
mission          ⭐        ⭐⭐        ⭐⭐⭐  ⭐⭐⭐      ⭐⭐⭐⭐          ← la difficulté que le contenu porte déjà
chapitre         [★]───────[★]─────────[★]─────────────[☆ ✨]            ← 4 étoiles max, une par palier franchi
                 étoile 1  étoile 2   étoile 3 (maîtrisé)  étoile 4 (terminé) — ici : 3 acquises, la 4ᵉ est une nouveauté
matière          Sceau ⭐ ✓ · Sceau ⭐⭐ ✓ · prochain : ⭐⭐⭐ (14/20 chapitres prêts, dont 1 nouveau)
effort           42 missions réussies · 1 240 XP · 18 chapitres commencés · 5 terminés   ← ça ne descend jamais
```

- **Étoile r d'un chapitre** = toutes les missions de catalogue de difficulté **≤ r** sont
  réussies (+ le quiz s'il gate). Les étoiles se gagnent dans l'ordre. **Une étoile acquise
  est inscrite au grand livre et n'est jamais retirée.**
- **Sceau r d'une matière** = **tous** ses chapitres publiés ont l'étoile r. Inscrit, jamais
  retiré.
- **Nouveauté ✨** = une mission (ou un chapitre, ou un quiz) arrivée **après** ce que l'élève
  avait acquis là. Elle explique pourquoi une jauge « terminée » a un cran de plus.

### 2.2 Analyse comparative — quel modèle de progression ?

| Modèle                                              | Ce qu'il fait                                                                            | Ce qui régresse quand le contenu arrive                                        | Verdict                                                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **A. Ratio vivant** (statu quo é22)                 | `x/y` missions, `n/N` chapitres, %                                                       | **tout** — c'est le défaut constaté                                            | ❌                                                                                                                           |
| **B. Instantané de contenu par élève**              | figer la liste des missions d'un chapitre au premier contact, compter contre elle        | rien — mais **le reste-à-faire aussi est figé** : l'élève ne voit jamais le neuf | ❌ sépare mal acquis et nouveautés ; une table de listes par élève à invalider                                                |
| **C. Compter seulement ce qui a été tenté**         | dénominateur = missions vues                                                             | rien                                                                           | ❌ récompense l'évitement : ne pas ouvrir la mission dure, c'est être à 100 %                                                 |
| **D. Paliers cumulés + grand livre + nouveautés**   | seuils par difficulté (≤ r), **statut inscrit** quand atteint, le vivant ne sert qu'à monter et à décrire ✨ | rien — un seuil cumulé ne fait que s'atteindre ; le neuf est **nommé** | ✅ **Retenu (D-1, D-2)** : c'est le modèle des jeux (étoiles par niveau, jamais reprises) **et** celui des diplômes           |
| **E. Maîtrise par compétence comme progression**    | la carte à 4 états de é30 devient LA progression                                         | n/a                                                                            | ❌ ne couvre que `math` taggé ; mesure « savoir », pas « couvert » ; volontairement sans chiffre côté élève (é30 D-1) — **orthogonal**, gardé tel quel (R-19) |

**Références** (non normatives) : les étoiles par niveau (Super Mario, Angry Birds, Duolingo
« couronnes » — jamais reprises, un niveau ajouté n'en retire aucune) ; la mastery
non-bloquante de Khan Academy (les niveaux de maîtrise s'acquièrent, le contenu ajouté
apparaît comme « new », le niveau tenu n'est pas rétrogradé par l'ajout) ; côté motivation,
la théorie de l'autodétermination déjà mobilisée par é22 §2.6 et é31 annexe — **compétence
perçue** (paliers atteignables, jamais retirés), **autonomie** (aucun ordre imposé),
**transparence** (une jauge qui grandit dit pourquoi).

### 2.3 Acteurs & user stories

**Élève connecté** (cœur) · **parent** (lecteur du même grand livre) · **visiteur anonyme**
(promesse) · **admin** (mesure) · **auteur de contenu** (aucune action nouvelle : le pipeline
émet, la date se pose seule).

- **US-1 — Le chapitre qui grandit.** J'avais « Terminé ✓ » sur *Théorème de Thalès* ; une
  campagne ajoute une mission ⭐⭐⭐. À ma prochaine visite le chapitre affiche **toujours**
  « Terminé ✓ », plus un cran nouveau avec **✨ 1 nouvelle mission ⭐⭐⭐** ; ma matière garde
  son sceau ; rien n'a baissé nulle part. Quand je réussis la nouvelle mission, la ✨ s'éteint
  et le cran s'allume.
- **US-2 — L'élève de milieu d'année.** J'ai le quiz et la mission ⭐ des 12 premiers
  chapitres : chacun porte **★☆☆☆** (étoile 1), la matière me dit « Sceau ⭐ : 12/20 chapitres
  prêts ». Je ne suis pas « à 0 % » : je vois **ce que j'ai** (12 étoiles, 26 missions
  réussies, 1 540 XP) et ce qui manque pour le premier sceau, chapitre par chapitre.
- **US-3 — Le premier sceau.** Je réussis la mission ⭐ du 20ᵉ chapitre : l'écran de
  résultat célèbre l'étoile du chapitre **puis** le **Sceau ⭐ de Mathématiques 9ᵉ** (modale,
  confettis, son) ; le badge *Premier sceau* tombe. Le sceau reste dans ma collection, daté,
  même l'an prochain.
- **US-4 — L'élève qui pousse.** Mon chapitre est **★★★☆** : je sais qu'il me manque le défi
  élite ⭐⭐⭐⭐ pour « Terminé », et que **maîtrisé** (★★★) est déjà acquis — le parent le lit
  pareil. Rien ne m'oblige ; l'étoile 4 est un dépassement, comme le Rappel.
- **US-5 — Le chapitre qui n'a que deux missions.** *Repérage* n'a que ⭐ et ⭐⭐ : sa jauge
  a **deux crans**, pas quatre ; les deux réussis, il est **Terminé ✓**. Si un boss arrive
  un jour, la jauge gagne un cran ✨ et le « Terminé ✓ » reste.
- **US-6 — L'élève dont le parent crée des missions.** Les missions de ma famille
  apparaissent dans le chapitre sur leur propre ligne « Missions de la famille 1/2 » : elles
  me rapportent des XP, elles ne touchent ni mes étoiles ni mon sceau — et mon parent ne peut
  pas non plus me les « retirer » en en ajoutant.
- **US-7 — Le parent.** La colonne « Programme » ne dit plus « 3/20 » : elle montre la
  distribution des 20 chapitres par étoile (barre empilée), **« 12 maîtrisés · 5 terminés »**,
  et sous la matière, les chapitres les plus proches de leur **prochaine étoile** avec le geste
  exact (« refaire le quiz posément », « 1 mission ⭐⭐ »). Après une campagne, ce tableau ne
  recule pas ; il gagne une ligne « ✨ 1 chapitre ajouté ».
- **US-8 — L'anonyme.** Sur le hub public, la jauge de chaque chapitre est vide et les sceaux
  sont gris : « Connecte-toi pour garder tes étoiles ». Rien ne se calcule sans compte ; rien
  n'est verrouillé de plus (é22 R-5/US-8).
- **US-9 — L'admin.** Sur `/admin/engagement`, je lis la distribution des étoiles, les sceaux
  par actif, et **« étoiles préservées : n »** — le nombre de (élève, chapitre) dont le grand
  livre est au-dessus du vivant : la promesse KPI-1 en un chiffre.
- **US-10 — Le héros (optionnel, lot 5, GAP-037).** À chaque niveau de héros, un **nom** et
  une mini-biographie (un savant arabe / un non-arabe en alternance) : « Niveau 12 —
  Al-Khawarizmi ». Rien ne change au calcul du niveau.

### 2.4 Règles métier

#### Vocabulaire & périmètre

- **R-1 (vocabulaire — normatif, i18n)** : **étoile(s) de chapitre** (1 à 4) · **sceau de
  matière** (⭐ à ⭐⭐⭐⭐) · **nouveauté ✨** · **terminé** (chapitre : toutes les étoiles
  présentes) · **maîtrisé** (chapitre : étoile ≥ 3 — registre parent) · **réussie / maîtrisée**
  pour une mission (é22 R-14, inchangé). EN : *chapter stars · subject seal · new · finished ·
  mastered* ; AR : **نجوم الفصل · ختم المادة · جديد · مكتمل · متقَن**. Interdits : « niveau »
  pour une étoile (é22 R-27), « palier » (réservé à l'avatar, `dashboard.avatarTierLabel`),
  « rang » (classement), « or / platine / diamant » (ligue é31 R-14), et toute formule de
  perte (« tu as perdu », « régression », « en retard »).
- **R-2 (ce qui compte)** : une **mission de catalogue** est `source='admin'` et
  `mode <> 'quiz'` (é22 R-15, inchangé). **Toute mission hors catalogue — `parent`
  aujourd'hui ; `student` / `ai` si un jour une source naît — ne compte jamais pour une étoile
  ni un sceau**, quelle que soit son origine, et compte pour l'effort (XP sous l'anti-farm
  existant ; compteur « missions de la famille »). La règle est écrite pour l'avenir ; **aucune
  valeur de `source` n'est ajoutée** tant qu'aucune source n'existe (P-7).
- **R-3 (mission comptée)** : une mission compte pour une étoile quand sa **meilleure
  tentative `variant='classic'`** a `score_pct >= 60` **et** `duration_seconds >= total_count × 4`
  (non précipitée). C'est le prédicat que le moteur applique déjà à l'XP (`v_too_fast`) et à la
  porte du quiz ; é22 R-14 l'omettait pour la complétion (D-8).

#### Étoiles

- **R-4 (étoile r d'un chapitre, r ∈ 1..4)** : le chapitre est **publié** (≥ 1 mission de
  catalogue) **et** son quiz est validé s'il gate (`chapter_quiz_cleared`, arena#1005) **et**
  au moins une mission de catalogue est comptée **et** toutes les missions de catalogue de
  difficulté `LEAST(GREATEST(difficulty,1),4) <= r` sont comptées. Les étoiles se gagnent dans
  l'ordre (r ⇒ r−1). Un cran de difficulté **absent** du chapitre est **franchi par vacuité**
  (D-3) : un chapitre ⭐ · ⭐⭐ entièrement réussi a ses 4 étoiles ; un chapitre ⭐⭐⭐ · ⭐⭐⭐⭐
  reçoit directement l'étoile 3 au premier boss réussi.
- **R-5 (lecture)** : **terminé** ⇔ étoile 4 ; **maîtrisé** ⇔ étoile ≥ 3 ; **commencé** ⇔
  ≥ 1 tentative (quiz compris) dans le chapitre.
- **R-6 (monotonie — la règle qui fonde l'étude)** : une étoile ou un sceau atteint est
  **inscrit au grand livre** (`user_chapter_stars`, `user_subject_seals`) à l'instant où le
  fait se produit, et **n'en sort jamais** — ni par l'ajout de contenu, ni par une suppression
  ou un re-clé, ni par un changement de règle. **Tout statut affiché se lit au grand livre** ;
  le calcul vivant ne sert qu'à **monter** (inscrire ce qui vient d'être atteint) et à
  **décrire le reste-à-faire**.
- **R-7 (nouveauté ✨)** : une mission de catalogue **jamais tentée** dont `created_at` est
  postérieur à la **référence** de l'élève sur le chapitre — `GREATEST(dernière étoile
  inscrite, dernière tentative dans le chapitre)` ; sans référence (chapitre jamais touché),
  rien n'est ✨. Même règle pour un **quiz** ajouté à un chapitre scolaire (chip « quiz ✨ »)
  et pour un **chapitre** publié après le dernier sceau (ou la dernière tentative) de la
  matière. La ✨ s'éteint à la première tentative.
- **R-8 (la jauge)** : autant de crans que de niveaux de difficulté **présents** dans le
  chapitre (1 à 4, jamais 0 — un chapitre non publié n'a pas de jauge) ; un cran est **allumé**
  si l'étoile correspondante est au grand livre ; un cran présent non allumé porte `n/m`
  missions comptées ; un cran arrivé après une étoile porte ✨. **« Terminé ✓ »** se lit au
  grand livre (étoile 4) et devient « Terminé ✓ · ✨ n nouveauté(s) » si le vivant a grandi.
  Légende accessible partout (« Gagne la 3ᵉ étoile en réussissant toutes les missions jusqu'à
  ⭐⭐⭐ »).

#### Sceaux

- **R-9 (sceau r d'une matière)** : **tous** les chapitres publiés de la matière ont
  l'étoile r **au grand livre** (D-5). Une matière sans chapitre publié n'a pas de sceau. Le
  sceau est inscrit, daté, jamais retiré. Sous le dernier sceau, la matière affiche
  « Prochain sceau ⭐⭐⭐ : k/N chapitres prêts » (k = chapitres avec l'étoile r+1, N =
  chapitres publiés, vivant) **et** « dont n nouveaux » quand des chapitres ✨ existent —
  c'est la seule fraction de l'étude, et elle nomme ce qui l'a fait bouger.
- **R-10 (effort — jamais un pourcentage)** : par matière, **missions réussies** (comptées,
  distinctes), **XP gagnés**, **chapitres commencés** et **terminés**. Des compteurs qui
  montent (une purge de contenu peut les faire baisser — assumé, marginal, jamais un statut).
- **R-11 (aucune récompense d'économie)** : ni XP ni pièces pour une étoile, un sceau ou un
  badge de cette étude (é22 R-28 → é09 ; D-10). Trois badges, famille `maitrise` (é31 R-13 :
  chacun décernable, condition en clair) : `first_seal` (premier sceau, toute matière),
  `subject_elite` (un sceau ⭐⭐⭐⭐), `parcours_covered` (toutes les matières du parcours
  actif ont le sceau ⭐).
- **R-12 (célébration)** : une étoile → **bloc** sur l'écran de résultat (jauge du chapitre
  animée, son `unlock`) ; un sceau → **modale** plein écran sur le modèle du level-up
  (confettis, son `victory`), une seule à la fois (le sceau le plus haut) ; badges par le bloc
  existant. Jamais de push (é31 R-4), jamais d'enchaînement automatique depuis la célébration
  (é31 R-6), respect de `prefers-reduced-motion` (primitive existante).

#### Le parent, l'anonyme, l'admin

- **R-13 (le parent lit le même grand livre)** : colonne « Programme » = distribution des
  chapitres publiés par étoile (barre empilée 0 → 4) + **« m maîtrisés · t terminés »** ;
  « ce qui manque » = par chapitre non terminé, la **prochaine étoile** et le geste qui la
  donne (« quiz à refaire posément » · « n missions ⭐⭐ »), le plus proche d'abord ; après
  une campagne, une ligne « ✨ n chapitre(s) / mission(s) ajouté(s) ». Une matière sans
  chapitre publié affiche « — » (inchangé).
- **R-14 (aucun verrou nouveau)** : étoiles et sceaux ne conditionnent **aucun** accès,
  aucune récompense, aucun classement (é22 R-10). Tout écran qui les afficherait comme une
  condition est un bug de doctrine.
- **R-15 (rejeu initial — on ne reprend rien à personne)** : la migration inscrit, pour
  chaque (élève, chapitre), les étoiles R-4 sur le contenu actuel, datées de la dernière
  tentative contributive (`attempt_id` NULL = rejoué) ; **grand-père** : tout chapitre complet
  au sens de é22 R-15 (règle antérieure — précipitation comprise) reçoit l'étoile 4. Les
  sceaux se déduisent des étoiles inscrites. La migration journalise (NOTICE) le nombre
  d'étoiles inscrites et le nombre de grand-pères — un chiffre attendu proche de zéro.
- **R-16 (anonyme)** : jauges vides, sceaux gris, promesse « Connecte-toi pour garder tes
  étoiles » (modèle é17 R-9 / é31 US-10) ; aucune donnée calculée sans compte, aucune
  régression de l'expérience publique.
- **R-17 (i18n)** : toute chaîne naît FR/EN/AR ; RTL vérifié au rendu (la jauge se remplit
  de droite à gauche en AR) ; chiffres occidentaux ; les chaînes vivent dans un **catalogue
  paresseux `progress/`** (règle du budget i18n, `scripts/check-bundle-budget.mjs`).
- **R-18 (mesure)** : `/admin/engagement` publie la distribution des étoiles par actif, les
  sceaux par actif, et **« étoiles préservées »** ; KPI-E de é31 (`chapters_per_active`)
  devient « chapitres **maîtrisés** (étoile ≥ 3) par actif », série **datée** (rupture
  assumée, écrite dans STATUS §1bis et dans la console).
- **R-19 (compétences — orthogonales)** : une étoile ne se déduit jamais d'une croyance
  BKT (é30) ni d'une maîtrise EWMA (é07), et réciproquement ; le hub parle d'étoiles, le
  tableau de bord parle de compétences ; une étoile **ne se dégrade pas par l'oubli** — la
  révision est le métier de SM-2, de la frontière et de la Révision du jour. Un chapitre
  ★★★ avec une compétence « fragile » est un état normal, pas une contradiction.
- **R-20 (niveau de héros — inchangé)** : XP/200, sept classes, `avatar_tier` : rien ne
  bouge. L'**échelle nommée** (GAP-037, lot 5) est une **peau** : un nom + une mini-biographie
  par niveau 1..50, trilingue, contenu hors ligne relu (P-5c) ; au-delà de 50, le numéro seul.

### 2.5 i18n

- Catalogue paresseux **`src/lib/i18n/progress/{fr,en,ar}.ts`** + `progress.types.ts` +
  `useProgressT()`, sur le modèle exact de `badges/` (é31 lot 2) ; budget dédié
  `i18n-progress-` (16 KB) dans `scripts/check-bundle-budget.mjs` et entrée `manualChunks`
  dans `vite.config.ts`. Les seules clés app-wide autorisées : le libellé court du nœud de
  `/parcours` et de la carte matière du QG (« Sceau ⭐⭐ », « Prochain sceau : 14/20 »), parce
  que ces surfaces ne sont pas paresseuses vis-à-vis du dashboard.
- Clés (préfixe `progress.`) : `chapterStars.legend`, `chapterStars.star{1..4}` (nom du
  palier : « socle », « pratique », « boss », « élite » — à confirmer en Q-1),
  `chapterStars.finished`, `chapterStars.finishedWithNew`, `chapterStars.mastered`,
  `chapterStars.rungCount` (`{done}/{total}`), `newMission`, `newQuiz`, `newChapter`,
  `familyMissions` (`{done}/{total}`), `seal.title` (`Sceau {stars} — {subject}`),
  `seal.next` (`{ready}/{total} chapitres prêts`), `seal.nextWithNew` (`… dont {n} nouveaux`),
  `seal.none`, `seal.earnedOn`, `effort.missions`, `effort.xp`, `effort.chapters`,
  `anon.promise`, `celebration.star.title/body`, `celebration.seal.title/body`,
  `parent.mastered`, `parent.finished`, `parent.nextStar`, `parent.gestureQuiz`,
  `parent.gestureMissions` (`{n} mission(s) {stars}`), `parent.added`.
- Badges : trois lignes `badgeCollection.labels.{first_seal,subject_elite,parcours_covered}`
  dans `src/lib/i18n/badges/{fr,en,ar}.ts` (sans elles `tsc` refuse — `Record<BadgeCode>`).
- Lexique : `docs/content-voice-and-composition.md` §2 gagne les lignes « étoile de
  chapitre », « sceau de matière », « nouveauté » (lot 2).

### 2.6 Hors périmètre (v1)

Sceaux par **domaine** (`chapters.domain` — inerte en prod, le corpus n'en déclare aucun ;
extension naturelle quand il vivra) · migration de la progression anonyme · classement ou
ligue par sceaux · notifications d'étoile ou de sceau · « mode discipline » parental
(é22 Q-4) · refonte visuelle du hub connecté (GAP-043) · narration IA des célébrations (une
phrase d'El Ostedh pourra **enrichir** la modale quand le pilote é29 Q-9 aura rendu son
verdict — jamais la conditionner) · toute campagne de contenu (l'étude ne demande aucun
rééquilibrage du corpus ; les 57 chapitres sans ⭐ restent un fait de `programme:etat`).

## 3. Architecture technique (décisions fermées)

### 3.1 Modèle de données (migrations additives, ordre DoD §7, grants explicites)

```sql
-- 1) Dater le contenu — la seule donnée qui distingue « il a régressé » de « on a ajouté ».
--    DEFAULT now() date les lignes futures à l'application (`apply-content.yml`) ; l'existant
--    reçoit l'époque du catalogue pour ne JAMAIS passer pour une nouveauté (R-7).
ALTER TABLE public.exercises ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ NOT NULL DEFAULT now();
UPDATE public.exercises SET created_at = '2026-05-22T00:00:00Z';   -- l'existant = l'époque du catalogue
ALTER TABLE public.chapters  ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ NOT NULL DEFAULT now();
UPDATE public.chapters  SET created_at = '2026-05-22T00:00:00Z';   -- idem (sauter si la colonne existait déjà)

-- 2) Le grand livre des étoiles — insert-only, une ligne par étoile inscrite.
CREATE TABLE public.user_chapter_stars (
  user_id           UUID     NOT NULL REFERENCES auth.users(id)        ON DELETE CASCADE,
  chapter_id        UUID     NOT NULL REFERENCES public.chapters(id)   ON DELETE CASCADE,
  star              SMALLINT NOT NULL CHECK (star BETWEEN 1 AND 4),
  reached_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  attempt_id        UUID     REFERENCES public.attempts(id) ON DELETE SET NULL,  -- NULL = rejeu initial
  missions_at_reach INT      NOT NULL,   -- missions de catalogue du chapitre à cet instant (audit)
  PRIMARY KEY (user_id, chapter_id, star)
);
CREATE INDEX idx_user_chapter_stars_user_reached ON public.user_chapter_stars (user_id, reached_at DESC);

-- 3) Le grand livre des sceaux.
CREATE TABLE public.user_subject_seals (
  user_id           UUID     NOT NULL REFERENCES auth.users(id)        ON DELETE CASCADE,
  subject_id        TEXT     NOT NULL REFERENCES public.subjects(id)   ON DELETE CASCADE,
  star              SMALLINT NOT NULL CHECK (star BETWEEN 1 AND 4),
  reached_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  attempt_id        UUID     REFERENCES public.attempts(id) ON DELETE SET NULL,
  chapters_at_reach INT      NOT NULL,
  PRIMARY KEY (user_id, subject_id, star)
);

-- RLS (patron `user_competency_mastery`, 20260721100000) : SELECT pour le propriétaire, un
-- parent lié ACTIF (`parent_student_links`), et l'admin ; AUCUNE écriture cliente.
ALTER TABLE public.user_chapter_stars  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_subject_seals  ENABLE ROW LEVEL SECURITY;
GRANT SELECT ON public.user_chapter_stars, public.user_subject_seals TO authenticated;
REVOKE ALL   ON public.user_chapter_stars, public.user_subject_seals FROM anon;
REVOKE INSERT, UPDATE, DELETE ON public.user_chapter_stars, public.user_subject_seals FROM authenticated;
```

Notes de conception :

- **`attempt_id … ON DELETE SET NULL`, jamais CASCADE** : quand le pipeline élague une
  mission, ses tentatives partent en cascade (`attempts.exercise_id … ON DELETE CASCADE`) ; la
  ligne du grand livre **reste** — c'est tout l'objet de la table. Le CASCADE sur `chapters`
  et `subjects` est voulu : un chapitre supprimé du corpus n'a plus d'étoile à montrer ; le
  **sceau**, lui, survit à la suppression d'un chapitre.
- **Backfill de `created_at`** : les deux `UPDATE` ci-dessus tournent dans la **même**
  migration que l'`ADD COLUMN`, avant tout rejeu — toute ligne existante porte l'époque du
  catalogue (date de la première migration de contenu), donc aucune ne passera pour une
  nouveauté. Le `sql-builder`
  (`ON CONFLICT (id) DO UPDATE SET <colonnes explicites>`) **ne touche pas** `created_at` :
  une ré-application conserve la date, une insertion la pose. Aucun changement du moteur de
  contenu.
- **Aucune table pour les nouveautés** : ✨ se calcule (`created_at` vs référence R-7) — c'est
  du vivant, pas un acquis.
- Colonnes et fonctions en anglais, commentaires en français (convention du dépôt) ;
  `npm run db:gen-types` après la migration (arena#1029) — **aucun cast manuscrit** de plus
  (dette A-4 de l'audit du 2026-09-12).

### 3.2 Server — fonctions SQL

Toutes `SET search_path = public`, `STABLE` pour les lectures, `REVOKE … FROM PUBLIC, anon`
puis `GRANT EXECUTE TO authenticated` seulement pour les deux RPC élève ; les fonctions
`student_*` restent internes (patron `student_parcours_progress`, `20260816200000`).

1. **`mission_is_counted(p_user UUID, p_exercise UUID) RETURNS BOOLEAN`** — R-3, écrit une
   fois : meilleure tentative `classic`, `score_pct >= 60`, `duration_seconds >= total_count*4`.
2. **`chapter_star_rungs(p_user UUID, p_chapter UUID) RETURNS TABLE (difficulty SMALLINT,
   missions_total INT, missions_counted INT, missions_new INT)`** — une ligne par niveau de
   difficulté **présent** (R-8) ; `missions_new` selon R-7.
3. **`chapter_star_live(p_user UUID, p_chapter UUID) RETURNS SMALLINT`** — R-4, 0..4, sur le
   vivant, en appelant `chapter_quiz_cleared` (jamais un prédicat recopié — L-4).
4. **`record_progress_stars() RETURNS TRIGGER`** — `AFTER INSERT ON public.attempts FOR EACH
   ROW`, `SECURITY DEFINER` (D-4). Retour immédiat si `NEW.variant <> 'classic'` ou si
   l'exercice n'est ni de catalogue ni un quiz. Sinon : calcule `chapter_star_live` ; insère
   les étoiles `1..live` manquantes (`ON CONFLICT DO NOTHING`, `attempt_id = NEW.id`,
   `missions_at_reach`) ; **si au moins une étoile a été inscrite**, vérifie les sceaux de la
   matière (R-9, sur le grand livre) et insère ceux qui manquent ; puis décerne les trois
   badges R-11 via `award_badge_if_new(user, code, 'stars:' || NEW.id)` — la raison porte
   l'id de tentative, c'est ce qui permet au delta (fn 8) de les retrouver. Coût borné : une
   requête sur ≤ 9 missions × l'index `(user_id, exercise_id, variant)`, puis ≤ 41 chapitres
   seulement quand une étoile tombe.
5. **`student_subject_stars(p_user UUID, p_subject_ids TEXT[] DEFAULT NULL) RETURNS TABLE
   (subject_id TEXT, chapters_total INT, chapters_started INT, chapters_star1 INT,
   chapters_star2 INT, chapters_star3 INT, chapters_star4 INT, seal_star SMALLINT, seal_at
   TIMESTAMPTZ, new_chapters INT, new_missions INT)`** — **grand livre** pour les comptes
   `chapters_star*` et `seal_*` ; vivant pour `chapters_total`, `chapters_started`, `new_*`.
   Interne (parent, carte, QG, admin).
6. **`student_parcours_progress(p_user, p_subject_ids)`** — **conservée avec sa signature**,
   redéfinie comme une projection de (5) : `chapters_completed := chapters_star4`. Ses trois
   consommateurs (`get_user_parcours_progress`, `_student_report_json`,
   `_student_daily_report_json`) ne changent pas de forme et **deviennent monotones**.
   `get_user_parcours_progress` reste le wrapper élève.
7. **`get_subject_progress(p_subject_id TEXT) RETURNS JSONB`** — RPC élève, self-scopée
   `(SELECT auth.uid())`, la charge du hub :

   ```jsonc
   {
     "subjectId": "math",
     "seals": [{ "star": 1, "reachedAt": "…" }, { "star": 2, "reachedAt": "…" }],
     "nextSeal": { "star": 3, "chaptersReady": 14, "chaptersTotal": 20, "newChapters": 1 }, // null au-delà de 4
     "effort": { "missionsCounted": 42, "xp": 1240, "chaptersStarted": 18, "chaptersFinished": 5 },
     "chapters": [{
       "chapterId": "…", "star": 3, "starLive": 2, "finished": false, "isNew": false,
       "quiz": { "gated": true, "cleared": true, "isNew": false },
       "rungs": [{ "difficulty": 1, "total": 1, "counted": 1, "new": 0 },
                 { "difficulty": 3, "total": 2, "counted": 1, "new": 1 }],
       "family": { "total": 2, "counted": 1 },
       "newMissions": 1
     }],
     "missions": [{ "exerciseId": "…", "counted": true, "bestClassic": 83, "mastered": false, "isNew": false }]
   }
   ```

   `missions` devient la **source unique** des états ✓ / 💯 / ✨ du hub : il remplace
   `get_best_scores_by_exercise` pour cet usage — cette RPC **ignore `variant`** (constat de
   la cartographie, §A.3), donc une reprise en Rappel à ≥ 60 % cochait au hub une mission que
   le serveur ne comptait pas. La divergence disparaît par construction.
8. **`get_attempt_progress(p_attempt_id UUID) RETURNS JSONB`** — RPC élève, propriétaire de
   la tentative seulement : `{ chapterId, starBefore, starAfter, newStars: [3], newSeals:
   [{subjectId, star}], newBadges: [{code,name,rarity,iconName}], rungs }` —
   `starBefore = COALESCE(MAX(star) FILTER (WHERE attempt_id IS DISTINCT FROM p_attempt_id), 0)`,
   `newBadges` = `student_badges WHERE awarded_reason = 'stars:' || p_attempt_id`. Lue par
   l'écran de résultat **après** `submit_exercise_attempt` (D-4).
9. **`student_chapter_gaps`** (arena#987) — étendue de deux colonnes additives `next_star
   SMALLINT` et `missing_for_next INT` ; tri « le plus proche de sa prochaine étoile
   d'abord » ; l'enveloppe `_daily_report_with_scopes` les fait voyager (patron `||`, sans
   rouvrir le rapport). Le prédicat « comptée » passe par `mission_is_counted` (R-3) — **une**
   définition, et l'assertion pgTAP de #987 qui confronte gaps et progression sur le même
   décor reste, étendue aux étoiles.
10. **`admin_engagement_overview`** — + `stars_distribution` (chapitres touchés par étoile
    0..4, actifs 30 j), `seals_per_active`, `stars_preserved` (lignes du grand livre dont
    `star > chapter_star_live`), et `chapters_per_active` redéfini sur l'étoile ≥ 3 (R-18).
    Substitution **par script** sur la révision vivante (L-3), jamais retapée.
11. **Rejeu initial** (R-15) — bloc `DO $$ … $$` dans la migration des tables : pour chaque
    (élève, chapitre) avec ≥ 1 tentative classic, inscrit `1..chapter_star_live` datées
    `MAX(completed_at)` des tentatives comptées ; grand-père é22 R-15 → étoile 4 ; puis les
    sceaux ; `RAISE NOTICE` des compteurs.

**Ce qui n'est PAS touché** : `submit_exercise_attempt` (D-4), `award_xp`, la porte du quiz,
`resolve_exercise_access`, les RPC de duel / donjon / examen / Rappel, `get_daily_plan`,
le moteur de contenu (`sql-builder`, `build`).

### 3.3 Client

- **`src/shared/types/progress.ts`** — lignes de base (snake_case côté RPC, camelCase dans
  le JSONB ci-dessus, zod dans les server fns).
- **`src/features/quest/quest.server.ts`** — `getSubject` appelle `get_subject_progress`
  (connecté) et n'appelle plus `get_best_scores_by_exercise` pour le hub ; nouvelle server fn
  `getAttemptProgress` (`requireSupabaseAuth` + zod `{ attemptId: uuid }`).
- **`src/shared/lib/chapter-completion.ts`** et son test : **retirés** (DoD §3 — la règle vit
  au serveur, le client rend des faits ; é30 D-1 avait posé le même geste pour les
  compétences). `src/shared/lib/next-action.ts` : `nextOnPath` lit `starLive < 4` au lieu de
  `isChapterComplete` — **priorité et ordre inchangés** (é22 R-31, D-11).
- **Primitives** : `src/components/game/star-gauge.tsx` (jauge à crans variables, états
  allumé / présent / ✨, RTL, `aria-label` complet), `src/components/game/seal-mark.tsx`
  (glyphe de sceau ⭐..⭐⭐⭐⭐ + date en tooltip).
- **Hub** (`src/features/quest/components/subject-hub.tsx`, gabarit Hub — même budget de
  blocs) : bloc d'ancrage + **sceaux et prochain sceau** + ligne d'effort ; accordéon de
  chapitre : titre + jauge + « Terminé ✓ / ✨ n » ; missions : chips ✓ réussie · 💯 maîtrisée
  · ✨ nouvelle · ○, ligne « Missions de la famille n/m » quand il y en a ; anonyme : R-16.
  Composants dédiés `chapter-stars.tsx`, `subject-seals.tsx` dans `quest/components/`.
- **Carte** (`src/features/parcours/journey.ts`, `journey-map.tsx`, `path-node.tsx`) :
  `done` ⇔ sceau ⭐⭐⭐⭐ ; sous-libellé = sceau + « Prochain : k/N » ; `progressionPct` **retiré**
  (é22 R-16 amendée). `getDashboard` lit `student_subject_stars` via le wrapper élève.
- **QG** (`src/routes/_authenticated/dashboard.tsx`, cartes matières) : le pourcentage cède
  la place au glyphe de sceau + barre « prochain sceau ». ⚠️ le chunk `dashboard` est à
  **34,4 / 36 KB** (audit du 2026-09-12) : on **remplace**, on n'ajoute pas ; la mesure
  `build:check` fait partie du lot.
- **Résultat** (`quest-result-screen.tsx`, `exercise-player.tsx`) : après le résultat,
  `getAttemptProgress` ; bloc « Étoile du chapitre » (jauge animée) ; `SealCelebration`
  (`src/components/ui/seal-celebration.tsx`, jumeau de `level-up-celebration.tsx`) ; ordre des
  blocs du gabarit Player respecté (score → gains → **étoile** → badges → correction).
- **Collection** (`/boutique`, `badge-collection.tsx`) : section « Sceaux » (toutes les
  matières où l'élève en a) au-dessus des familles de badges ; `badge-medal.tsx` gagne les
  trois glyphes (le test GLYPHS ↔ migrations l'exige).
- **Parent** (`src/features/parent-report/components/daily-insights.tsx` `CoverageCell`,
  `report-content.tsx`, `insights/chapter-gaps.ts`, `insights/daily-report.ts`) : barre
  empilée + « m maîtrisés · t terminés », gaps par prochaine étoile, ligne ✨ ; catalogue
  `parent/` pour les chaînes parent (déjà paresseux).
- **Admin** (`engagement-admin.tsx`, `engagement.server.ts`) : trois tuiles + note de rupture
  de série datée.
- **« Ta semaine »** (`weekly-recap-card.tsx`) : une ligne « n étoiles · s sceaux cette
  semaine » lue dans le grand livre (dates) — sans récompense (é31 R-18).

### 3.4 Sécurité & anti-abus

- Rien de nouveau n'est exposé : aucune clé de réponse, aucun `user_id` tiers ; les deux RPC
  élève sont self-scopées ; les tables ne s'écrivent que par le trigger `SECURITY DEFINER` ;
  RLS propriétaire / parent lié actif / admin ; `anon` n'a rien.
- Une étoile exige des tentatives **non précipitées** (R-3) : la « ferme d'étoiles » par
  QCM expédié au hasard est fermée par la même règle que la ferme d'XP.
- Les missions hors catalogue ne comptent jamais (R-2) : un parent — ou demain un élève ou une
  IA — ne peut ni donner ni retirer une étoile.
- Le grand livre est insert-only ; un `UPDATE`/`DELETE` par un client est refusé par grant
  et par RLS (pgTAP).
- L'exclusion silencieuse des comptes triche (é22 R-26) s'appliquera à toute surface
  classante — il n'y en a aucune ici.

### 3.5 Intégrations & env

Aucune variable d'env, aucun service. `docs/environment-variables.md` inchangé.

### 3.6 Observabilité

- Événements produit (liste fermée, `product-events.ts` + catalogue, sans PII) :
  `chapter_star_reached` `{subject_id, star}` et `subject_seal_earned` `{subject_id, star}`.
- Logger structuré : `progress.attempt_delta` (durée de `getAttemptProgress`) ;
  `progress.hub_loaded` (nombre de chapitres, ✨ présents — mesure la fréquence réelle des
  nouveautés vues).
- `/admin/engagement` : les trois tuiles R-18 ; la migration de rejeu journalise ses
  compteurs.

### 3.7 Décisions d'architecture (ADR)

- **D-1 — Le grand livre remplace le calcul** (amende é22 D-4 « la complétion se calcule, ne
  se stocke pas »). D-4 était juste tant que le contenu était stable ; il est **la cause** de
  la régression dès qu'il grandit. Rejetés : recalcul vivant (statu quo), instantané de
  contenu par élève (modèle B — fige aussi le neuf), compter le tenté (modèle C — récompense
  l'évitement).
- **D-2 — Une étoile est un seuil cumulé sur la difficulté (≤ r), pas un ratio.** Un ratio
  régresse quand le dénominateur bouge ; un seuil cumulé ne fait que s'atteindre, et il
  raconte quelque chose (« tout le socle », « tous les boss »). Rejeté : `x/y` pondéré par
  difficulté — un pourcentage de plus, illisible.
- **D-3 — La vacuité est assumée** : un cran absent est franchi, la jauge n'a que les crans
  présents. Rejetée : échelle fixe à 4 pour tous — 57 chapitres n'ont pas de ⭐, 35 n'ont pas
  de ⭐⭐ ; une étoile qu'aucun contenu ne permet d'obtenir est une promesse fausse, l'inverse
  de é22 R-30.
- **D-4 — Un trigger sur `attempts`, pas une greffe dans `submit_exercise_attempt`.** La RPC
  fait 570 lignes et a été ré-émise par trois études en trois semaines (é31, é33) ; la greffer
  encore, c'est le risque L-3 à chaque fois. Le fait « une tentative existe » est possédé par
  la table ; le trigger est le finalizer (doctrine é31 §3.2, patron `record_competency_mastery`).
  Le delta se lit par `get_attempt_progress(attempt_id)` — un aller-retour de plus sur l'écran
  de résultat, zéro substitution. Rejetés : greffe ; cron (« jamais un balayage périodique »).
- **D-5 — Le sceau se calcule sur le grand livre des chapitres**, pas sur le vivant : la
  promesse est cohérente d'un étage à l'autre, et le vivant est dit par ✨ (« dont n
  nouveaux »). Rejeté : sceau sur le vivant — « 19/20 prêts » retomberait à 18/20 après une
  campagne, la régression qu'on vient de supprimer, un étage plus haut.
- **D-6 — `created_at` sur `exercises` et `chapters`.** La cartographie l'a établi :
  **rien** ne date une mission aujourd'hui, et `content_releases` est à la maille matière, en
  RLS privée. Sans date, « ✨ » est impossible et « il a régressé » est indistinguable de « on
  a ajouté ». Rejeté : dériver de `content_releases`.
- **D-7 — Étoiles et sceaux ne sont pas des badges.** 94 matières × 4 sceaux, 773 chapitres
  × 4 étoiles : le patron `Record<BadgeCode, …>` (un libellé par code et par langue — la
  garantie `tsc` de é31) et le budget `i18n-badges` (12 KB) ne survivraient pas. Deux tables,
  un composant générique qui compose « Sceau {⭐} — {matière} », et **trois** badges méta
  seulement. Rejeté : un badge par sceau.
- **D-8 — La précipitation exclut** (R-3). « Réussie ≥ 60 % » sans durée (é22 R-14) laissait
  une tentative que le moteur juge « trop rapide pour être réelle » compter pour la
  complétion. Une étoile est une preuve ; la définition d'« acquis » rejoint celle de l'XP et
  du quiz. Rejeté : garder R-14 telle quelle — ferme d'étoiles au hasard des QCM (≈ 4 % par
  essai expédié sur 6 questions, illimité). Le grand-père R-15 empêche que ce durcissement
  reprenne quoi que ce soit.
- **D-9 — Vocabulaire : « étoiles » (chapitre) et « sceau » (matière)**, une seule échelle —
  celle que le contenu porte déjà (⭐ → ⭐⭐⭐⭐, `rewards-and-modes.md`) ; « palier » reste à
  l'avatar, « niveau » au héros (é22 R-27), « rang » au classement, « or / platine / diamant »
  à la ligue (é31 R-14). Rejetés : métaux (collision ligue), lettres D→S (collision `s_rank`),
  noms de classe (collision `guerrier`/`maitre`/`elite`).
- **D-10 — Aucune récompense d'économie.** La reconnaissance (célébration, collection,
  datation) suffit à la compétence perçue ; é09 garde seule la main sur toute valeur, et A16
  rappelle qu'une valeur ajoutée sans mesure devient un signal faux. Rejeté : « 20 pièces par
  sceau » — Q-3 le rouvre si l'humain le veut.
- **D-11 — La recommandation « prochaine action » ne change pas** (é22 R-31, profondeur
  d'abord). Le sceau est **large** (tous les chapitres), l'année scolaire est **séquentielle** :
  pousser un élève d'octobre vers la mission ⭐ du chapitre 15 serait faux. La barre « k/N
  chapitres prêts » suffit ; le sceau vient au rythme du programme.
- **D-12 — L'échelle nommée (GAP-037) est un lot optionnel et une peau** : ni la courbe
  XP/200, ni les sept classes, ni `avatar_tier` ne bougent ; le lot ne dépend d'aucun autre
  et ne bloque rien. Il attend une décision humaine (Q-4) et un contenu (la liste).

### 3.8 Ce que l'étude amende explicitement

| Texte      | Avant                                                                  | Après (cette étude)                                                                                 |
| ---------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| é22 R-14   | réussie ≥ 60 % (durée ignorée) ; maîtrisée 100 % non précipité         | inchangé pour la **récompense** ; pour une **étoile**, R-3 exige en plus « non précipitée »          |
| é22 R-15   | chapitre complété = quiz + **toutes** les missions réussies            | **terminé** = étoile 4 (même contenu, mais monotone et vacuité assumée) ; **maîtrisé** = étoile ≥ 3 |
| é22 R-16   | progression = chapitres complétés / publiés (%), métrique officielle   | métrique officielle = **distribution des étoiles** + sceau ; le % disparaît des écrans (R-9, R-13)  |
| é22 D-4    | la complétion se calcule, ne se stocke pas                             | les **acquis** se stockent (grand livre), le **reste-à-faire** se calcule (D-1)                     |
| é31 KPI-E  | chapitres complétés / actif                                            | chapitres **maîtrisés** (étoile ≥ 3) / actif, série datée (R-18)                                    |
| arena#987  | gaps = missions manquantes vers « complet »                            | gaps = manques vers la **prochaine étoile**, même fonction, deux colonnes de plus                    |

### 3.9 Ce que l'étude réutilise sans y toucher

`chapter_quiz_gated` / `chapter_quiz_cleared` (arena#1005) · `award_badge_if_new` ·
`get_user_subject_stats` (XP par matière, si le calcul d'effort ne le refait pas) ·
`content_releases` (lecture admin seulement) · `LevelUpCelebration`, `Confetti`, `StatTile`,
`BadgeMedal`, le moteur de sons · les catalogues i18n paresseux et `manualChunks` ·
`admin_engagement_overview` (enrichie) · le patron d'enveloppe `||` de #987.

### 3.10 Registre économie (é22 R-28 → é09)

**Vide.** Aucune XP, aucune pièce, aucun prix, aucun multiplicateur n'est créé ni modifié ;
`gamification.ts` n'est pas touché ; `economy:check` (é09 R-4) n'a rien à rejouer. Si Q-3
tranche autrement, la valeur entre ici **et** dans la console `/admin/economie` avant tout code.

## 4. Plan d'exécution en lots

Chaque lot = une PR mergeable, gate verte, utile seul. Seuls liens durs : 1 → 2 → 3 → 4 ;
le lot 5 est indépendant et **optionnel**.

| lot | contenu (résumé)                                                                                                                                                  | fichiers/objets principaux                                                                                                                                                                                           | tests exigés                                                                                                                                                                                       | dépend de |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1   | **La règle et le grand livre** : `created_at`, deux tables + RLS/grants, fonctions 1→11, rejeu initial, doc normative                                             | migrations additives (colonnes · tables · fonctions · trigger · rejeu), `docs/etoiles-et-sceaux.md`, ARCHITECTURE.md §8, `types.ts` régénéré                                                                          | pgTAP : R-3/R-4 sur les 6 échelles réelles (vacuité comprise), quiz gate, parent/recall/précipité exclus, monotonie (injection → grand livre intact, vivant baisse, ✨), sceau, rejeu = trigger sur même décor, grand-père, RLS/grants, gaps ⇔ étoiles sur même décor | —         |
| 2   | **Le hub matière** : jauge, sceaux, effort, états de mission, ✨, famille, anonyme ; catalogue `progress/` ; retrait de `chapter-completion.ts`                     | `star-gauge.tsx`, `seal-mark.tsx`, `chapter-stars.tsx`, `subject-seals.tsx`, `subject-hub.tsx`, `quest.server.ts`, `next-action.ts`, `i18n/progress/*`, `check-bundle-budget.mjs`, `vite.config.ts`, lexique §2 | Vitest : jauge (crans variables, RTL, ✨), états, anonyme, i18n 3 langues complet, next-action inchangé ; e2e : hub connecté montre une étoile ; `smoke:shell`                                        | 1         |
| 3   | **La carte, le QG, le parent, l'admin** : `done` = sceau 4, cartes matières, colonne Programme empilée + gaps par étoile, KPI-E redéfini + 3 tuiles, docs         | `journey.ts`, `journey-map.tsx`, `dashboard.tsx`, `dashboard.server.ts`, `daily-insights.tsx`, `report-content.tsx`, `chapter-gaps.ts`, `daily-report.ts`, `engagement-admin.tsx`, `suivi-parental-quotidien.md`, STATUS §3/§1bis | Vitest : journey sans %, cartes, CoverageCell, gaps ; pgTAP : `admin_engagement_overview` (tuiles, `stars_preserved`), non-régression des specs parent ; `build:check` (budget dashboard)             | 1         |
| 4   | **Célébrer et collectionner** : delta après résultat, bloc étoile, modale sceau, 3 badges, section Sceaux, 2 événements produit, ligne « Ta semaine »             | `getAttemptProgress`, `quest-result-screen.tsx`, `exercise-player.tsx`, `seal-celebration.tsx`, migrations badges (seed + trigger), `badges.ts`, `i18n/badges/*`, `badge-medal.tsx`, `badge-collection.tsx`, `product-events.ts`, `weekly-recap-card.tsx` | pgTAP : chaque badge décerné (87 structurel passe), idempotence, delta exact ; Vitest : ordre des blocs, une modale max, reduced-motion, GLYPHS ↔ migrations, événements ; e2e : première étoile célébrée | 1, 2      |
| 5   | **(optionnel, Q-4) L'échelle nommée des 50 niveaux** (GAP-037) : noms + mini-bios FR/EN/AR, level-up et en-têtes                                                  | `i18n/hero-levels/*` (chunk `i18n-hero-levels-`), `level-up-celebration.tsx`, `hero-stat-chips.tsx`, `journey-header.tsx`                                                                                            | Vitest : 50 × 3 langues complets, alternance arabe / non-arabe, niveau > 50 → numéro seul, aucun changement de courbe ; `build:check`                                                                  | —         |

- [ ] **Lot 1 — La règle et le grand livre.** R-2…R-9, R-15, D-1…D-8. Migration(s)
      additives uniquement ; `student_parcours_progress` redéfinie **sans changer de
      signature** ; `admin_engagement_overview` **non touchée** (lot 3). **Stop-points** :
      aucune UI ; aucun badge (lot 4) ; ne pas éditer `submit_exercise_attempt` ; la
      redéfinition d'une fonction vivante se fait **par script sur son texte extrait** (L-3) ;
      si `chapters` porte déjà un `created_at`, ne pas le recréer ; si le rejeu journalise
      plus de **1 %** de grand-pères, STOP et remonter (le durcissement R-3 aurait un coût
      réel). Doc normative `docs/etoiles-et-sceaux.md` (règle, vocabulaire, exemples
      chiffrés, « ce qui n'est pas un verrou ») écrite dans ce lot.
- [ ] **Lot 2 — Le hub matière.** US-1, US-2, US-5, US-6, US-8, R-1, R-8, R-10, R-16,
      R-17. **Stop-points** : ne pas toucher la carte, le QG, le parent (lot 3) ; ne pas
      célébrer (lot 4) ; `get_best_scores_by_exercise` reste en base (ses autres lecteurs sont
      à inventorier — si le hub était le dernier, la dépose est une migration **destructive**
      → merge séparé, après ce lot, DoD §7) ; aucun relèvement du budget `i18n-` (catalogue
      paresseux obligatoire) ; le gabarit Hub garde son budget de blocs.
- [ ] **Lot 3 — La carte, le QG, le parent, l'admin.** US-7, US-9, R-9, R-13, R-18, D-5,
      D-11. **Stop-points** : `resolveNextAction` ne change ni d'ordre ni de priorité ; le
      chunk `dashboard` ne dépasse pas son budget (remplacer, pas ajouter — sinon STOP et
      proposer le découpage) ; la rupture de série KPI-E est **écrite** (STATUS §1bis + note
      dans la console) le jour du merge ; aucun push.
- [ ] **Lot 4 — Célébrer et collectionner.** US-3, US-4, R-11, R-12, D-7, D-10.
      **Stop-points** : trois badges, pas un de plus ; aucune XP/pièce ; une seule modale par
      résultat ; la modale n'enchaîne rien (é31 R-6) ; les événements produit restent sans PII.
- [ ] **Lot 5 — L'échelle nommée (optionnel).** US-10, R-20, D-12 — **ne démarre que sur
      Q-4 tranchée ET la liste des 50 livrée** (noms + bios trilingues, relus). **Stop-points** :
      aucune modification de `award_xp`, des classes, de `avatar_tier` ; chunk paresseux
      dédié ; aucun texte en dur.

## 5. Stratégie de test

- **pgTAP (toute logique SQL — DoD)** : `99_etoiles_regle.test.sql` (R-3/R-4 sur les six
  échelles réelles du corpus : 1·2·3·3·4, 1·2·3·3·4·4, 1·2·3, 1·2·2·3·4, 1·2·3·4, 1·2 — et
  les deux dégénérées 3·4 et 1 ; quiz gaté / non gaté ; parent, recall, précipité exclus) ;
  `100_etoiles_grand_livre.test.sql` (**l'invariant KPI-1** : décor à étoile 4, `INSERT` d'une
  mission ⭐ puis ⭐⭐⭐, puis d'un quiz, puis `DELETE` d'une mission : le grand livre ne bouge
  pas, `chapter_star_live` baisse, `missions_new` / `isNew` disent pourquoi ; `UPDATE`/`DELETE`
  client refusés) ; `101_sceaux.test.sql` (tous les chapitres → sceau, un chapitre ajouté →
  sceau intact + `new_chapters`, matière vide → aucun) ; `102_rejeu_initial.test.sql` (rejeu ≡
  trigger sur le même décor ; grand-père) ; `103_gaps_etoiles.test.sql` (gaps ⇔ étoiles sur
  le même décor — l'assertion de #987 étendue) ; `104_progress_rpcs.test.sql`
  (`get_subject_progress`, `get_attempt_progress` : forme, self-scope, propriétaire seul) ;
  lot 3 : `admin_engagement_overview` (tuiles, `stars_preserved`) ; lot 4 : badges (87
  structurel + conditions + idempotence + `awarded_reason`).
- **Vitest (co-localisés)** : `star-gauge` (crans variables, allumé/présent/✨, RTL, aria) ;
  `chapter-stars` / `subject-seals` (états, anonyme, copy « Terminé ✓ · ✨ n ») ; `journey`
  (plus aucun `%`, `done` = sceau 4) ; `CoverageCell` (barre empilée, « — » sans chapitre) ;
  `chapter-gaps` (prochaine étoile, geste) ; `next-action` (**inchangé** : mêmes 4 priorités,
  mêmes cas) ; `seal-celebration` (une seule, reduced-motion) ; i18n : trois langues
  complètes dans `progress/`, `badges/` et `hero-levels/` ; `product-events` (catalogue) ;
  `badge-medal` (GLYPHS ↔ migrations).
- **e2e (projet TEST)** : hub connecté après une mission ⭐ réussie → cran allumé ; écran de
  résultat → bloc étoile ; specs publiques existantes **inchangées** (US-8 : rien de nouveau
  pour l'anonyme).
- **`smoke:shell` + `build:check`** sur tout lot qui touche le bundle (2 à 5) ; les budgets
  `i18n-progress-` (16 KB) et `i18n-hero-levels-` (lot 5) sont ajoutés **avec** leur chunk.
- **Non-régression clé** : les specs du quiz gate (serveur + hub + anonyme), du Rappel et de
  l'anti-farm passent inchangées — l'étude n'a touché aucun verrou ni aucune récompense.
- **Le harnais pgTAP local** (leçon é31 : deux défauts trouvés avant la CI) : `db-tests.yml`
  n'est pas requis sur les PR ; chaque lot SQL se rejoue en local **avant** de pousser.

## 6. Risques & mitigations

- **RISK-1 — Le sceau est trop loin** (20 chapitres pour la première reconnaissance de
  matière) : probabilité haute, impact motivationnel. Mitigation : les étoiles de chapitre
  (jusqu'à 4 jalons par chapitre, célébrés), la barre « k/N chapitres prêts », la ligne « Ta
  semaine », et KPI-3 qui **mesure** le délai au premier sceau — si la médiane dépasse un
  trimestre, l'extension « sceaux par domaine » (§2.6) est la réponse, pas un abaissement.
- **RISK-2 — La vacuité déroute** (« Terminé ✓ » avec deux crans) : mitigation D-3 (jauge à
  crans présents seulement), légende partout, et pgTAP sur les échelles réelles. Si un
  signalement le montre mal lu, le copy change, pas la règle.
- **RISK-3 — Grand livre et vivant divergent sans explication** : mitigation R-7/R-8 — toute
  divergence est **nommée** par ✨ au cran, au chapitre et à la matière ; test dédié sur la
  copy « Terminé ✓ · ✨ n ».
- **RISK-4 — Budgets de bundle** (`dashboard` 34,4/36 KB, `i18n-` 186/188 KB) : mitigation —
  catalogue paresseux obligatoire (R-17), remplacement à iso-poids sur le QG, `build:check`
  dans chaque lot ; un dépassement est un STOP, pas un relèvement silencieux.
- **RISK-5 — Rupture des séries** (KPI-E, colonne parent) : mitigation — « terminés » garde
  l'ancienne sémantique (désormais monotone) à côté de « maîtrisés » ; la date de rupture est
  écrite dans STATUS §1bis et dans la console ; aucune comparaison avant/après n'est
  présentée comme continue.
- **RISK-6 — Le trigger alourdit la soumission** : requête bornée (≤ 9 missions, index
  existants), vérification de sceau seulement quand une étoile tombe ; mesure par le logger
  de `getAttemptProgress` et par la latence de `submit` déjà journalisée ; si > 100 ms au p95,
  différer la vérification de sceau à la lecture (le grand livre des sceaux s'écrirait alors
  par `get_subject_progress` — décision architecte).
- **RISK-7 — Dates de rejeu approximatives** (`reached_at` = dernière tentative contributive,
  pas l'instant réel) : mitigation — `attempt_id NULL` marque les lignes rejouées, la doc le
  dit, et R-7 utilise `GREATEST(étoile, dernière tentative)` pour que la référence soit juste
  quand même.
- **RISK-8 — Collision avec une étude qui ré-émet `submit_exercise_attempt`** : nulle par
  construction (D-4 : trigger + lecture), c'est la raison de D-4.
- **RISK-9 — Le durcissement R-3 « reprend » des chapitres au rejeu** : mitigation R-15
  (grand-père) + compteur journalisé + stop-point du lot 1 à 1 %.

## 7. Questions ouvertes (pour l'humain)

- **Q-1 — Le vocabulaire.** « étoiles de chapitre » + « sceau de matière » sur l'échelle ⭐
  du contenu (D-9), avec les quatre paliers nommés **socle · pratique · boss · élite** dans la
  légende ? Recommandation : **oui** — une seule échelle, celle que les titres de missions
  portent déjà, trilingue par construction ; les alternatives (métaux, lettres, noms de
  classe) entrent toutes en collision avec un vocabulaire existant.
- **Q-2 — Le mot du parent.** « **maîtrisé** » = étoile ≥ 3 (tous les boss réussis, l'élite
  restant un dépassement) — c'est ce qui aurait dit « 12/20 » au lieu de « 3/20 » le
  2026-09-04 ; « **terminé** » = étoile 4 reste affiché à côté. Recommandation : **oui**,
  conforme à la doctrine du contenu (« core progression at 1–2, reserve 3–4 »). Alternative :
  maîtrisé = étoile 4 (statu quo sémantique, monotone désormais).
- **Q-3 — Une récompense d'économie ?** Recommandation : **aucune** (D-10) — reconnaissance,
  célébration, collection ; é09 pourra attacher une valeur plus tard, mesurée. Si oui : la
  valeur entre au §3.10 et dans `/admin/economie` avant le code.
- **Q-4 — L'échelle nommée des 50 niveaux (GAP-037, lot 5).** La commander maintenant (elle
  attend une **liste** : 50 savants en alternance arabe / non-arabe, trois langues, mini-bios
  relues — un travail de contenu, à produire au dépôt privé puis compilé dans un chunk
  paresseux) ou la laisser au backlog ? Recommandation : **la commander comme lot 5,
  optionnel et dernier** — elle sert l'axe « effort » sans toucher au calcul, et le lot est
  borné ; la liste peut être rédigée par une session de contenu pendant les lots 1-4.
- **Q-5 — Les missions de la famille.** Confirmer qu'elles restent **hors** étoiles et
  sceaux (R-2), sur leur propre ligne, avec XP — et que la même règle vaudra pour toute
  source future (élève, IA) ? Recommandation : **oui** — c'est la seule façon que les étoiles
  restent comparables et qu'aucun tiers ne puisse en donner ni en retirer.

## 8. Journal d'exécution

- **2026-09-14 — Création (Fable).** Brouillon ; Q-1…Q-5 ouvertes. Base factuelle : la
  cartographie du code (annexe A, vérifiée sur `main` arena en `31e17e1`) et le comptage du
  corpus (annexe B, `content/` au tip du privé). Aucun lot commencé.

---

## Annexe A — État des lieux du code (2026-09-14)

### A.1 Où vit la règle aujourd'hui, et ce qu'elle lit

| Endroit                                                                     | Rôle                                                                              | Dénominateur                                                                         |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `student_parcours_progress(p_user, p_subject_ids)` (`20260905130000`)       | **la** règle (chapitres complétés / publiés) — parent, carte, QG                  | `exercises` vivante : `source='admin' AND mode <> 'quiz'`, aucune date, aucun statut  |
| `get_user_parcours_progress` (`20260816200000`)                             | wrapper élève                                                                     | idem                                                                                 |
| `chapter_quiz_gated` / `chapter_quiz_cleared` (`20260905130000`, #1005)     | la porte du quiz, définie une fois                                                | —                                                                                    |
| `student_chapter_gaps` (`20260904120000`, #987)                             | « ce qui manque » (parent)                                                        | `missions_total` vivant                                                              |
| `admin_engagement_overview` (`20260902130000` → `20260905130000`)           | KPI-E `chapters_per_active`                                                       | chapitres touchés, règle recopiée                                                    |
| `src/shared/lib/chapter-completion.ts`                                      | miroir client (hub `x/y`, ✓, `next-action`)                                       | exercices déjà chargés par `getSubject`                                              |
| `src/features/parcours/journey.ts`                                          | nœud `done` ⇔ 100 %, sous-libellé `%`                                             | idem, via RPC                                                                        |
| `daily-insights.tsx` `CoverageCell`, `report-content.tsx`                   | parent : `{done}/{total}` + jauge                                                 | idem                                                                                 |

### A.2 Ce qui manque

- **Aucune date sur `exercises` ni `chapters`** (colonnes vivantes : `chapter_id,
  correction_video, created_by, difficulty, display_order, id, manuel_ref, mode,
  reward_coins, source, subject_id, target_student_id, title, xp_reward`) ;
  `content_releases(applied_at, git_sha, subjects[], actor)` est à la maille matière, RLS sans
  policy. **Rien ne peut distinguer « il a régressé » de « on a ajouté ».**
- **Aucun état figé** : ni table, ni vue, ni colonne de complétion — tout est recalculé.
- **Aucune clé (élève, chapitre) ni (élève, matière)** dans les trois systèmes de maîtrise
  (`user_competency_mastery` EWMA + `p_known` BKT sont par **compétence**, `math` seulement).
- `exercises.source ∈ ('admin','parent')` ; la Forge IA (`ai_forged_quizzes`) est hors
  `exercises`, éphémère, non notée ; aucune notion d'élève-auteur.

### A.3 Divergences trouvées en cartographiant (traitées ou notées)

1. **`get_best_scores_by_exercise` ignore `variant`** (`20260603110000`) alors que la règle
   exige `classic` ; le commentaire de `chapter-completion.ts` affirme le contraire. Une
   reprise en Rappel ≥ 60 % coche au hub une mission que le serveur ne compte pas. →
   **traitée** par le lot 2 (le hub lit `get_subject_progress`).
2. **`get_user_parcours_progress` passe par un cast manuscrit** (`dashboard.server.ts:31-50`)
   et dégrade en silence à « 0 % » sur erreur. → traitée par `db:gen-types` (arena#1029) et
   par le retrait du `%`.
3. **La courbe de niveau vit en quatre exemplaires** (`award_xp`, `award_duel_rewards`,
   `XP_PER_LEVEL`, vue économie). → hors périmètre, **notée** pour `docs/dette-technique.md`
   (R-20 : on n'y touche pas).
4. La complétion compte une réussite **précipitée** ; l'XP et le quiz la refusent. →
   **traitée** (R-3, D-8, R-15).

## Annexe B — Le corpus, compté (2026-09-14, `content/` du dépôt privé)

| Mesure                                                        | Valeur                                                                                                                     |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Matières / chapitres / missions                               | **94 / 773 / 3 574** — tous les chapitres ont un `quiz.json`                                                               |
| Scolaire vs libre                                             | 533 chapitres · 2 574 missions vs 240 · 1 000                                                                              |
| Missions par chapitre                                         | min 1 · p25 4 · **médiane 5** · p75 5 · max 9 (380 chapitres à 5, 132 à 6, 116 à 3, 64 à 4, 55 à 2)                       |
| Difficulté des missions                                       | ⭐ 717 (20 %) · ⭐⭐ 864 (24 %) · ⭐⭐⭐ 1 211 (34 %) · ⭐⭐⭐⭐ 782 (22 %) → **56 % de boss et d'élite**                          |
| Échelles dominantes (difficultés triées)                      | 1·2·3·3·4 **268** (35 %) · 1·2·3·3·4·4 120 · 1·2·3 98 · 1·2·2·3·4 87 · 1·2·3·4 42 · 1·2 35 · 2·3·3·4 18 · 1·2·2·3·3·4·4 18 |
| Chapitres **sans ⭐** / **sans ⭐⭐**                            | **57** (ex. tout `arabic` 9ᵉ hors ch. 01/09) / **35** → la vacuité de D-3 n'est pas un cas d'école                          |
| Matières les plus denses                                      | `fiqh` 41 ch · 205 missions · `math-bac-math` 19 · 133 · `math` (9ᵉ) 20 · 126 · `math-6eme` 23 · 115                          |

**Exemple chiffré — `math` 9ᵉ (20 chapitres, 126 missions, échelle 1·2·3·3·4 majoritaire)** :

| Situation de l'élève                                                | Aujourd'hui (é22)                                   | Avec l'étude                                                                                          |
| ------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| quiz + ⭐ + ⭐⭐ + les deux ⭐⭐⭐ réussis sur les 20 chapitres, aucun défi | **0/20 complété**, carte à 0 %, parent « 0/20 »     | 20 chapitres **★★★☆ maîtrisés**, **Sceau ⭐⭐⭐**, parent « 20 maîtrisés · 0 terminé », effort 100 missions |
| idem + 5 défis élite                                                | 5/20, 25 %                                          | 5 terminés, 15 maîtrisés, sceau ⭐⭐⭐ ; « Prochain sceau ⭐⭐⭐⭐ : 5/20 »                                   |
| une campagne ajoute une mission ⭐⭐⭐ à 8 chapitres                    | les 5 terminés qui sont touchés **retombent** ; parent baisse | **rien ne baisse** ; 8 chapitres montrent « ✨ 1 nouvelle mission ⭐⭐⭐ » ; « étoiles préservées : 8 » côté admin |
| un quiz est ajouté à un chapitre scolaire qui n'en avait pas        | **ce** chapitre retombe à « non complété » : la porte se referme rétroactivement | les étoiles restent ; chip « quiz ✨ » ; la porte ne s'applique qu'aux missions **non encore réussies** (é22 R-7 inchangée) |
