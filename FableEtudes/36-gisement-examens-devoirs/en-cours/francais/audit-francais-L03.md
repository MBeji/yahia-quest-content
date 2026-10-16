# Audit indépendant — gisement français 9ᵉ, lot L03 (m013–m017)

Auditeur indépendant, 2026-10-16. Branche `wip/gisement-francais-9eme`, commit `736f1e05` (« L03 écrit »).
Consigne : `content-ingest/references/gisement-auditeur.md` (en entier), skills `content-audit` puis
`prof-francais-9eme`. Je n'ai ouvert aucune note d'auteur. Aucun fichier audité n'a été modifié.

Périmètre (52 questions) :

| mission | fichier | étage | q. |
| --- | --- | --- | ---: |
| m013 | `05-modes-et-temps-verbaux/exercices/06-examens-2003-2018-mode-apres-le-verbe-introducteur.json` | d3 boss 120/30 | 11 |
| m014 | `05-modes-et-temps-verbaux/exercices/07-examens-2009-2016-transposer-present-imparfait-futur.json` | d2 practice 75/15 | 10 |
| m015 | `06-concordance-des-temps/exercices/06-examens-2010-2026-imparfait-passe-simple-plus-que-parfait.json` | d2 practice 75/15 | 12 |
| m016 | `06-concordance-des-temps/exercices/07-examens-2006-2026-futur-simple-ou-futur-anterieur.json` | d3 boss 120/30 | 10 |
| m017 | `06-concordance-des-temps/exercices/08-examens-2002-2026-present-ou-passe-compose.json` | d2 practice 75/15 | 9 |

Sources lues : les transcriptions de toutes les sessions citées ; le PDF officiel 2009 G, page 1 (sha256
conforme au registre), pour vérifier une glose ; les `cours.md` et `resume.md` des chapitres 01 à 06 et 13, ainsi que
le cours du 12, sur `origin/main` ; les quiz et les exercices 01, 02, 04 et 05 des chapitres 05 et 06 ; 12 quiz
Q5 et 12/01 Q6 ; `content/misconceptions.json` (`fr.*`) et le manifeste `9eme-base.json`.

Contrôles moteur (copie des seuls chapitres 05 et 06, car le chapitre 09 du lot L01 bloque le chargement de tout
`french` : `questions.4.options.3: Unrecognized key "misconceptionTag"` dans
`09/.../11-examens-2009-2025-production-projet-metier-justifier.json` — ce n'est pas mon lot, mais le signaler à
L01) : `content:check` ✓, `content:qa --strict` ✓ (aucune clé suspecte, aucune séquence anti-verbatim),
`content:tranche --chapters 05,06` : 1 clé strictement la plus longue sur 110 (m017 Q3), 0 paire proche,
0 candidat gabarit ; positions a 25 · b 29 · c 27 · d 29.

## 1. Re-résolution à l'aveugle

J'ai résolu chaque question avant de lire la clé. Les 2×2 sont vérifiés case par case. **Aucune clé n'est fausse.**
« réserve » = clé juste, mais la question doit être reprise (§ 2).

### m013 — 05/06, le mode après le verbe introducteur

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | ouvre ; soient | b | OK | 2×2 sain ; étiquettes justes |
| 2 | battra | d | réserve | le rappel « espérer + indicatif » élimine « batte » à vue (M1) |
| 3 | sera | a | OK | « croire » affirmatif est enseigné ; la reformulation est déclarée (formule à ajuster, m4) |
| 4 | comprenne | c | OK | même déclencheur que Q9 (facultatif, m6) |
| 5 | saisisse | d | OK | coupe non déclarée (m2) |
| 6 | feront | b | réserve | même mécanique que Q2 ; le rappel tue « fassent » (M1, M4) |
| 7 | je sois | a | OK | |
| 8 | revienne | c | réserve | doublon de geste avec 05/02 Q2 « vienne », publié (M3) |
| 9 | soit | b | OK | |
| 10 | remportera ; puissent ; fasse | d | réserve | le rappel « être sûr + indicatif » élimine « remporterait », donc b et c (M1) |
| 11 | est capable ; s'en aperçoive | c | réserve | le rappel élimine « soit capable », donc a et d (M1) |

### m014 — 05/07, transposer : présent, imparfait, futur

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | viennent | c | OK | |
| 2 | s'étalent | a | OK | étiquette `nom-le-plus-proche` juste |
| 3 | font | d | OK | |
| 4 | C'est … viens de recevoir | b | réserve | le vote reconstruit la clé : « C'est » 3 fois sur 4 (m7) |
| 5 | suffisait | c | OK | |
| 6 | se mettaient ; rugissaient | d | réserve | **glose fausse** : « elles » ne désigne pas les voitures (M5) |
| 7 | se sentira ; s'endormira | a | OK | |
| 8 | continuera | b | OK | formule de la déclaration à adoucir (m8) |
| 9 | dis ; veux ; hurle | d | OK | 3 cases 2/2 |
| 10 | était caché ; allait | c | OK | |

### m015 — 06/06, imparfait, passé simple ou plus-que-parfait

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | avais ; venait | a | OK | |
| 2 | présenta | c | réserve | consigne « imparfait ou passé simple » : « avait présenté » et « présentera » morts (M6) |
| 3 | se rendit ; découvrit | b | OK | clé la plus courte (structurel, m9) |
| 4 | allais ; aimais | d | OK | |
| 5 | pris ; étais | b | OK | |
| 6 | hurla ; rougit | a | OK | clé la plus courte (m9) |
| 7 | entra ; engagea | d | OK | clé la plus courte (m9) |
| 8 | entendis ; se rapprochait | c | OK | |
| 9 | souffrait ; fournissait | a | OK | |
| 10 | se mettaient | d | réserve | consigne non officielle, qui tue b et c ; « annonça » donné sans le dire (M6) |
| 11 | avait ; avait hérité | b | réserve | consigne « imparfait ou plus-que-parfait » : les trois distracteurs (eut, aurait hérité) sont morts, et le piège du plan n'est pas posé (M6) |
| 12 | répétait ; avait apprises | c | OK | accord avec le COD placé avant, enseigné au ch. 02 |

### m016 — 06/07, futur simple ou futur antérieur

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | aura fini ; montera | d | réserve | l'énoncé donne la règle (« la première action est achevée… ») (M7) |
| 2 | aura ; aura réalisé | b | réserve | « quelle que soit sa place dans la phrase » désamorce le piège (M7) |
| 3 | aura préparé | a | réserve | « au temps du futur » tue c et d ; même verbe et même clé que Q4 (M7) |
| 4 | aura préparé ; fera | c | réserve | « futur simple ou futur antérieur » tue « ferait », donc b et d (M7) |
| 5 | sera ; publiera | b | réserve | « au futur » tue les trois distracteurs (tous au conditionnel) ; aucun futur antérieur en jeu (M7) |
| 6 | aura rattrapé | d | réserve | « quel temps du futur » tue b et c (M7) |
| 7 | rapportera ; aura vécu | a | réserve | cadre réécrit sans le dire : « vivra » devient défendable ; « futur simple ou antérieur » tue b et d (M7) |
| 8 | aurons évalué ; pourrez | c | réserve | « au futur » tue « évaluions » et « avez pu » ; l'énoncé donne la règle (M7) |
| 9 | irai ; sera sorti | d | OK | auxiliaire : notion non enseignée (M2) |
| 10 | ouvrirai ; aurai obtenu | b | réserve | « au futur » tue « ouvrirais » et « avais obtenu » (M7) |

### m017 — 06/08, présent ou passé composé

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a participé ; a joué | b | réserve | « au passé composé » tue les trois distracteurs (M8) |
| 2 | l'ont félicité ; lui ont fait | d | réserve | idem : seule d contient deux passés composés (M8) |
| 3 | ont mené ; ont travaillé | c | OK | clé la plus longue, mais c'est structurel : la garder (§ 4) |
| 4 | aide ; sont | a | réserve | les distracteurs « a aidé » oublient l'accord avec « les » (M8) |
| 5 | ont réussi ; sont venus | d | OK | auxiliaire (M2) |
| 6 | dès qu'on a ouvert … a invité | b | réserve | l'énoncé ajoute « au passé composé », absent du sujet officiel, et tue a, c, d (M8) |
| 7 | nous a regardés ; a dit | c | réserve | « au passé composé » tue a, b, d ; « verbes soulignés » renvoie à un soulignement absent (M8) |
| 8 | a excellé ; s'est passionné ; a remporté | a | OK | 3 cases 2/2 ; auxiliaire (M2) |
| 9 | Je lui ai embrassé … je suis allé | b | OK | auxiliaire (M2) |

**Bilan : 52 questions re-résolues, 0 clé fausse, 23 questions à reprendre** (m013 : 5 ; m014 : 2 ; m015 : 3 ;
m016 : 8 ; m017 : 6 ; m013 Q8, m016 Q3, m016 Q5 et m017 Q1 sont à retirer).

## 2. Défauts

### Critiques

Aucun : pas de clé fausse, pas d'explication qui contredise sa clé.

### Majeurs

**M1 — cours 05 : « espérer que » et « être sûr que » ne sont pas enseignés, et le cours pousse à l'erreur
(m013 Q2, Q6, Q10, Q11).** Le cours range au subjonctif le « fait voulu, **souhaité** » et le « sentiment » :
l'élève qui l'applique met le subjonctif après « espérer ». Les énoncés corrigent cela par un rappel (« On
rappelle que… est suivi de l'indicatif »), mais ce rappel élimine à vue le distracteur au subjonctif (Q2
« batte », Q6 « fassent », Q11 « soit capable ») ou au conditionnel (Q10 « remporterait », qui n'est pas un
indicatif). La seule erreur que ces questions devaient tester devient impossible. **Réponse au point de
l'auteur : oui, une ligne de cours vaut mieux.** Ensuite, il faut retirer les rappels des énoncés.

- `05-modes-et-temps-verbaux/cours.md`, § « 📐 Le subjonctif présent », bloc `::: propriete`. Remplacer :
  `garde l'indicatif : _Je pense qu'il **a** raison_ / _Je ne pense pas qu'il **ait** raison._`
  par :
  `garde l'indicatif : _Je pense qu'il **a** raison_ / _Je ne pense pas qu'il **ait** raison._ Deux verbes
  trompeurs gardent eux aussi l'**indicatif**, parce qu'ils donnent le fait pour attendu ou pour certain :
  _espérer que_ et _être sûr que_ — _J'espère qu'il **viendra**_ (mais _Je souhaite qu'il **vienne**_), _Je
  suis sûr qu'il **viendra**._`
  (Aucune forme d'une question du lot ; « vienne » est la clé de m013 Q8, que M3 retire.)
- `05-modes-et-temps-verbaux/resume.md`, puce « Subjonctif présent ». Remplacer `opinion négative ou
  interrogative ;` par `opinion négative ou interrogative (mais _espérer que_, _être sûr que_ et l'opinion
  affirmative gardent l'indicatif : _j'espère qu'il **viendra**_) ;`
- Énoncés, une fois la ligne de cours en place :
  - Q2 : supprimer `On rappelle que « espérer que » est suivi de l'indicatif. ` et garder `Quelle forme du
    verbe entre parenthèses convient ?`, puis la phrase, puis `Ces records ne sont pas encore battus.`
  - Q10 : supprimer `On rappelle que « être sûr que » est suivi de l'indicatif. ` et garder `La compétition
    n'a pas encore eu lieu.`
  - Q11 : supprimer `On admet que « être sûr que » est suivi de l'indicatif. ` et garder `La maîtresse
    constate les capacités de l'élève en ce moment même.`
  - Q6 : remplacée par M4.
  - Les explications restent justes : elles nomment déjà la règle.

**M2 — cours 05 : le choix de l'auxiliaire n'est enseigné ni au chapitre 06 ni avant (m016 Q9, m017 Q5, Q8,
Q9).** Quatre questions se jouent sur « être » ou « avoir » : verbe de mouvement, verbe pronominal. Le 05
définit le temps composé comme « avoir **ou** être + participe » sans dire lequel choisir ; le 13, qui parle des
pronominaux, vient après le 06 dans le manifeste. Le patron a le même angle mort (06/05 Q2, « avait parti »).
`05-modes-et-temps-verbaux/cours.md`, § « ⚡ Les temps simples et les temps composés » : après le paragraphe
`Le temps de l'auxiliaire donne le nom du temps composé : … au plus-que-parfait.`, insérer :

```
::: propriete
Le choix de l'auxiliaire : la plupart des verbes prennent _avoir_ (_j'ai couru_, _il a marché_) ;
prennent _être_ les verbes **pronominaux** (_il s'est levé_) et quelques verbes de **mouvement** ou de
changement d'état : _aller, venir, arriver, partir, entrer, sortir, monter, descendre, tomber, rester,
naître, mourir, devenir_ — _je suis allé_, _elles sont venues_. Cas-limite : avec un COD, _sortir_,
_monter_ et _descendre_ reprennent _avoir_ : _il a sorti la voiture_.
:::
```

Ajouter dans `resume.md`, à la fin de la puce « Temps simples / composés » : ` Auxiliaire _être_ pour les
pronominaux et quelques verbes de mouvement (_aller, venir, sortir…_), _avoir_ pour les autres.`

**M3 — m013 Q8 (2005 b, « souhaite que … revienne ») : doublon de geste, à retirer.** C'est le même geste
(subjonctif de « venir » après la volonté) et le même jeu de formes (vient / viendra / venait / vienne) que
05/02 Q2, publié, qui figure sur la liste « ne pas redemander ». La volonté est déjà posée par Q1, Q5 et Q10.
Supprimer Q8 et le dire au rapport d'auteur. Les deux autres items de 2005 (Q7, Q9) restent.

**M4 — m013 Q6 (2003 c) : même mécanique que Q2 (« espérer » + futur, mêmes quatre formes) ; à remplacer
par 2003 a.** 2003 a était dans la consigne de tri et a été perdu : sentiment, « pouvoir » irrégulier, et le
« ne » de la négation. Texte exact (on garde l'id de clé « b ») :

- prompt : `(Examen 2003) Quelle forme du verbe entre parenthèses convient ?\n« Le garçon regrette que ses
  parents ne (pouvoir) pas l'accompagner à Conakry. »`
- options : a `peuvent` (`fr.mode.subjonctif-oublie`) · b `puissent` · c `pourront`
  (`fr.mode.subjonctif-oublie`) · d `pourraient` (`fr.mode.subjonctif-oublie`) ; longueurs 7/**8**/8/10, la
  clé n'est ni la plus longue ni la plus courte.
- explication : `« Regretter que » exprime un sentiment : la subordonnée est au subjonctif présent.
  « Pouvoir » fait partie des verbes irréguliers : on n'écrit pas « qu'ils peuvent », mais « qu'ils
  puissent ». « Peuvent » est un indicatif présent, « pourront » un futur, « pourraient » un conditionnel :
  tous trois donneraient l'absence des parents pour un simple fait. Le piège courant : garder l'indicatif
  parce que ce qu'on regrette est réel ; c'est le sentiment qui commande le mode.`
- reste de forme : Q10 affiche « puissent » dans ses options et son explication. Le choix du mode reste
  entier, et la forme figure dans le tableau des irréguliers du cours. Accepté.

**M5 — m014 Q6 (2009 G) : glose fausse.** `(le sujet « elles » désigne les voitures)` est inexact. Dans le
texte officiel (PDF, page 1), « elles » reprend « ces milliers de pièces de métal » d'un moteur, qui « font
tourner les roues d'une voiture ». Remplacer par `(le sujet « elles » désigne les pièces de métal d'un
moteur)`. Le pluriel, seul point utile à la question, ne change pas.

**M6 — m015 : consignes qui éliminent les distracteurs.**

- **Q2 (2024 G)** : avec « à l'imparfait ou au passé simple », « avait présenté » et « présentera » tombent à
  vue. Remplacer la première ligne par `(Examen 2024, générale) Conjugue le verbe entre parenthèses au temps
  qui convient.` Les options et l'explication ne changent pas.
- **Q10 (2023 G)** : la consigne officielle est « aux temps qui conviennent » ; celle de la mission tue « s'étaient
  mis » et « se mettront ». De plus, « annonça » est donné sans être déclaré. Remplacer la première ligne par
  `(Examen 2023, générale) Conjugue le verbe entre parenthèses au temps qui convient. Le sujet officiel faisait
  aussi conjuguer « annoncer », donné ici ; il porte la coquille « dans la cours », reprise avec [sic].` Le
  reste ne change pas.
- **Q11 (2015 G b)** : la consigne officielle « à l'imparfait ou au plus-que-parfait » élimine les trois
  distracteurs (« eut » est un passé simple, « aurait hérité » un conditionnel passé). En outre, le piège
  annoncé par le plan, « imparfait pour l'action antérieure », n'est posé nulle part dans la mission (Q12 ne
  propose aucun « apprenait »). Options de remplacement (la clé reste « b ») : a `avait eu ; avait hérité` ·
  b `avait ; avait hérité` · c `avait ; héritait` (`fr.temps.anteriorite-non-marquee`) · d `avait eu ;
  héritait` (muet). Longueurs 23/**20**/16/19 ; chaque case vaut 2/2. Explication : `L'inconnu tient le
  baluchon au moment du récit : c'est un état qui dure, à l'imparfait, « avait » ; « avait eu » le placerait
  avant ce moment. L'héritage, lui, est achevé avant : plus-que-parfait, « avait hérité » (auxiliaire
  « avoir » à l'imparfait + participe passé). « Héritait » ferait de l'héritage une action en cours au même
  moment. Le piège courant : un temps simple pour l'action déjà accomplie ; c'est le temps composé qui marque
  l'antériorité.` (Aucune fuite vers Q12, dont toutes les options sont au plus-que-parfait.) Solution de
  rechange si l'auteur préfère : 2019 G, « Une année auparavant, mon grand-père m'(apprendre) la menuiserie »
  (→ « m'avait appris »), item de plus-que-parfait neuf, écarté sans motif.

**M7 — m016 : consignes « au futur » qui éliminent les distracteurs, indices dans les énoncés, deux
questions à retirer.**

- **Q1** : première ligne → `(Examen 2025, générale) Conjugue les verbes entre parenthèses au futur simple ou au
  futur antérieur, selon le cas.` (consigne officielle). On retire la règle donnée.
- **Q2** : première ligne → la même consigne officielle. On retire « quelle que soit sa place dans la phrase »,
  qui désamorce le piège même que l'item teste.
- **Q3 (2015 G a) : à retirer.** Même verbe (« préparer »), même clé (« aura préparé ») et même geste que Q4,
  et « au temps du futur » tue « aurait préparé » et « avait préparé ». (2015 G reste cité en 06/06 Q11.)
- **Q4** : première ligne → `(Examen 2026, générale) Conjugue les verbes entre parenthèses au mode et aux temps
  qui conviennent.` (consigne officielle) ; « ferait » redevient un distracteur.
- **Q5 (2011 G, premier demi-item) : à retirer.** Les trois distracteurs contiennent un conditionnel, exclu par
  « au futur », et aucun futur antérieur n'est en jeu. C'est la moitié de la « Q3 coupée en deux ».
- **Q6** : première ligne → `(Examen 2006) Quelle forme du verbe entre parenthèses convient ?` (le sujet
  officiel dit « au mode et au temps qui conviennent »).
- **Q7 (2011 G, second demi-item)** : le cadre « Un jour, elle écrira un livre : dans ce livre… » est une
  réécriture non déclarée. Sans « sera de retour », rien ne dit que le séjour précède le livre, et « vivra »
  devient défendable. Rétablir la phrase officielle, avec les deux premiers verbes donnés :
  `(Examen 2011, générale) Conjugue les verbes entre parenthèses aux temps qui conviennent ; les deux premiers
  verbes sont donnés.\n« Quand Gilberte Favre sera de retour en France, elle publiera son livre dans lequel
  elle (rapporter) ce qu'elle (vivre) au cours de son séjour au Liban. »\nQuelles formes conviennent, dans
  l'ordre ?` Options inchangées ; étiqueter c `rapportera ; vivra` avec `fr.temps.anteriorite-non-marquee`.
  Explication : `Le séjour au Liban sera terminé quand Gilberte Favre rentrera en France, donc avant le livre :
  « ce qu'elle aura vécu » (futur antérieur, action achevée avant une autre action future). Le récit se fera
  dans le livre publié : « elle rapportera » (futur simple). « Vivra » ne marquerait pas que le séjour est
  achevé ; le conditionnel « rapporterait » supposerait une condition qu'aucun mot de la phrase n'exprime. Le
  piège courant : deux futurs simples, qui effacent l'ordre des événements.`
- **Q8** : première ligne → `(Examen 2023, générale) Conjugue les verbes entre parenthèses aux temps qui
  conviennent.` (consigne officielle). « Évaluions », le subjonctif après « après que », redevient le vrai
  piège (règle enseignée au ch. 02, § postériorité).
- **Q10** : première ligne → `(Examen 2019, générale) Conjugue les verbes entre parenthèses aux temps qui
  conviennent.` (consigne officielle). Ne pas étiqueter a avec `fr.conj.futur-conditionnel-1re-personne` : ce
  libellé décrit l'erreur inverse (le futur écrit pour le conditionnel).
- Après ces changements, la mission compte 8 questions (Q1, Q2, Q4, Q6–Q10), avec une rampe 2 → 3 ; elle reste
  d3 et garde le titre 2006–2026.

**M8 — m017 : consigne « au passé composé » qui élimine les distracteurs, et accord oublié.**

- **Q1 (2026 T, participer / jouer) : à retirer.** Les trois distracteurs contiennent un passé simple ou un
  imparfait, exclus par la consigne, et les deux verbes réguliers n'apportent rien que Q2 ne pose.
- **Q2 (2026 T)** : options de remplacement, toutes au passé composé (la clé reste « d ») : a `Ses camarades
  l'ont félicités et lui ont fait un cadeau.` (`fr.accord.pp-avoir-avec-sujet`) · b `Ses camarades l'ont
  félicité et lui a fait un cadeau.` (muet) · c `Ses camarades l'ont félicités et lui a fait un cadeau.` (muet,
  deux erreurs) · d `Ses camarades l'ont félicité et lui ont fait un cadeau.` Longueurs 56/53/54/**55** ;
  chaque case vaut 2/2 ; pronoms avant l'auxiliaire partout (la neutralisation est gardée). Prompt :
  `(Examen 2026, technique) Conjugue les verbes au passé composé : « Ses camarades le félicitent et lui font un
  cadeau. »\nQuelle phrase est correcte ?` (inchangé). Explication : `Au passé composé, l'auxiliaire « avoir »
  s'accorde avec le sujet « ses camarades » (pluriel) : « ont félicité », « ont fait ». Le participe, lui, ne
  s'accorde jamais avec le sujet quand l'auxiliaire est « avoir » : le COD « l' » (Angel, masculin singulier)
  ne demande aucune marque, d'où « félicité » ; « lui » est un COI et ne commande aucun accord, d'où « fait ».
  Le piège courant : accorder le participe avec le sujet pluriel, ou accorder l'auxiliaire avec le pronom
  « lui » placé juste devant.`
- **Q4 (2025 T)** : « Léna les (aider) » au passé composé donne « les a **aidés** » ; les distracteurs `a aidé ;
  sont` et `a aidé ; ont été` portent une seconde erreur, qui n'est pas celle qu'on teste. Remplacer par
  `a aidés ; sont` et `a aidés ; ont été`. La clé, `aide ; sont`, est la plus courte (11 contre 14/14/17) :
  c'est structurel, comme pour Q3 (§ 4).
- **Q6 (2019 T)** : la consigne officielle ne donne pas le temps. Remplacer `Il faut la réécrire en la
  commençant par « Hier soir, » et en mettant les deux verbes au passé composé.` par `Il faut la réécrire en la
  commençant par « Hier soir, ».`. Les options ne changent pas : aucune n'est tout au passé simple, comme le
  voulait le plan ; « hier » est un repère du discours, enseigné (06, § « Deux systèmes »).
- **Q7 (2017 T)** : prompt → `(Examen 2017, technique) Les élèves de la classe sont des garçons. On met les
  verbes « regarda » et « dit » au passé composé :\n« À la fin de la dictée, il nous regarda pendant un moment
  et il dit, tout lentement… »\nQuelles formes conviennent, dans l'ordre ?` (« soulignés » renvoyait à un
  soulignement absent). Options (la clé reste « c ») : a `nous a regardé ; a dit`
  (`fr.accord.pp-avoir-cod-avant-oublie`) · b `nous a regardés ; a dis` · c `nous a regardés ; a dit` · d `nous
  a regardé ; a dis` ; longueurs 22/23/**23**/22, cases 2/2. Explication : `Au passé composé, l'auxiliaire
  « avoir » est au présent, suivi du participe passé : « il nous a regardés », « il a dit ». Le COD « nous »,
  placé avant le verbe, désigne les élèves, des garçons : le participe s'accorde au masculin pluriel,
  « regardés ». Le participe de « dire » s'écrit « dit » ; « dis » est la forme du présent avec « je ». Le
  piège courant : oublier l'accord avec le COD placé avant, en cherchant l'accord du côté du sujet « il ».`
- Après ces changements, la mission compte 8 questions.

### Mineurs

- **m1 — m013, titre** : aucune clé n'est au conditionnel (2003 b est écarté). Remplacer par `🏛️ Examens
  2003–2018 · le mode après le verbe introducteur : subjonctif ou indicatif ⭐⭐⭐`.
- **m2 — m013 Q5 (2006 a)** : la phrase est coupée sans le dire (« désire qu'André fasse des progrès et
  qu'il… »). La coupe est utile, puisque « fasse » donnerait le mode. La déclarer : `(Examen 2006, phrase
  abrégée)`.
- **m3 — m013 Q2 (2017 G b)** : « et (améliorer) ses performances… » est coupé. Rien de neuf n'est perdu, même
  geste. Accepté.
- **m4 — m013 Q3 (2013 G b)** : `Le sujet officiel laisse le temps libre` est inexact, car la consigne dit
  « aux temps qui conviennent ». Remplacer par `Dans le sujet officiel, le présent et le futur conviennent tous
  deux ; on précise ici que l'enfant n'est pas encore placé chez Madame Huber : son bonheur est à venir.`
- **m5 — m013 Q6, explication** : « (la forme de « souhaiter que ») » annonçait le « fasse » de Q10 ; le
  défaut tombe avec M4. **m013 Q3, explication** : « je ne crois pas que » est le déclencheur de Q10, mais
  c'est la règle du cours ; accepté.
- **m6 — m013 Q4 / Q9** : deux fois « douter que ». Q4 est une complétion libre (2010 G) que l'auteur a fermée.
  On peut la retirer pour alléger, sans obligation.
- **m7 — m014 Q4** : le vote reconstruit la clé (« C'est » 3 fois sur 4, « viens » 2 fois). Remplacer d par
  `C'était une lettre de Jacques que je viendrai de recevoir.` : la première case passe à 2/2. La clé reste la
  plus courte (53), ce qui est structurel (forme au présent) et n'arrive qu'une fois dans la mission.
- **m8 — m014 Q8 (2009 T)** : `ce qui est incohérent` juge le sujet officiel. Remplacer la phrase par `Dans le
  sujet officiel, les verbes entre parenthèses sont donnés à l'imparfait ou au passé composé ; ici, on part de
  l'infinitif.`
- **m9 — m015, clé la plus courte** : Q3, Q6 et Q7 (et Q2 avant M6), soit 3 ou 4 sur 12. C'est structurel : le
  couple « passé simple ; passé simple » est toujours le plus court de son 2×2. La fréquence est proche du
  hasard et la plus longue n'arrive jamais. Accepté et signalé.

## 3. Étiquettes

Les étiquettes en place sont exactes : `fr.mode.subjonctif-oublie` (m013), `fr.accord.nom-le-plus-proche`
(m014 Q2), `fr.temps.passe-simple-imparfait` (m015), `fr.accord.pp-avoir-cod-avant-oublie` (m015 Q12),
`fr.temps.anteriorite-non-marquee` (m016) et `fr.temps.recit-discours-melanges` (m017 Q1, Q2, Q6). Les options
à deux erreurs sont muettes.

**Étiquette proposée par l'auteur, « subjonctif après un verbe d'espoir ou de certitude » (m013 Q2, Q3, Q6, Q10,
Q11).**

- Le libellé ne nomme qu'une erreur, mais il ne couvre pas Q3 : « croire », à la forme affirmative, est un verbe
  d'opinion, ni d'espoir ni de certitude.
- **Q10 n'a aucune option qui exécute cette erreur** (aucun « remporte » au subjonctif) : on ne peut pas
  l'étiqueter.
- Q6 est remplacée (M4).
- Famille restante : Q2 (`batte`), Q3 (`soit`), Q11 a (`soit capable ; s'en aperçoive`), soit **3 questions
  distinctes**. Le seuil est tenu, à condition que M1 soit appliqué : tant que le rappel reste dans l'énoncé,
  l'option étiquetée est morte.
- Libellé élargi pour couvrir Q3, sur le modèle exact de `fr.mode.subjonctif-oublie` (id proposé :
  `fr.mode.subjonctif-abusif`, `"subject": "fr"`) :
  - fr : `Tu mets le subjonctif après un verbe qui appelle l'indicatif (espérer que, être sûr que, penser que
    ou croire que à la forme affirmative) : ces verbes présentent le fait comme attendu ou réel.`
  - en : `You use the subjunctive after a verb that takes the indicative (espérer que, être sûr que,
    affirmative penser que or croire que): these verbs present the fact as expected or real.`
  - ar : `تستعمل subjonctif بعد ما يستدعي indicatif (espérer que، être sûr que، penser que وcroire que في
    الإثبات): هذه الأفعال تقدّم الحدث منتظرًا أو واقعًا.`
  - Le libellé arabe proposé par l'auteur parlait de « صيغة الشرط », c'est-à-dire du conditionnel. C'est faux :
    l'erreur porte sur le subjonctif. La version ci-dessus reprend la tournure du libellé arabe de
    `fr.mode.subjonctif-oublie`, avec les termes français en caractères latins.
- Si l'on garde le libellé étroit (« espoir ou certitude »), Q3 reste muette et la famille tombe à 2 (Q2,
  Q11) : sous le seuil.

## 4. Points signalés par l'auteur — arbitrages

- **Notion absente du cours 05** : oui, une ligne de cours (texte exact en M1), plus une ligne de résumé, puis
  on retire les rappels des énoncés.
- **Étiquette** : voir § 3. Libellé élargi ; arabe corrigé ; Q10 et Q6 hors famille ; famille = 3.
- **m013 Q8 « revienne » / 05/02 Q2 « vienne »** : doublon de geste et de verbe, à retirer (M3). **Mécanique
  répétée** : Q6 recopie Q2, à remplacer par 2003 a (M4) ; Q4/Q9, facultatif (m6).
- **m017 Q3, clé la plus longue** : **garder**. La longueur est structurelle (le couple « passé composé ;
  passé composé » est forcément le plus long du 2×2). Allonger un distracteur imposerait une seconde erreur que
  le vote case par case reconstruirait. Dans la même mission, Q4, de même structure, a la clé la plus courte :
  la stratégie « la plus longue » échoue. Une seule clé la plus longue sur 110 dans la tranche.
- **Reformulations déclarées** :
  - 2013 G b : acceptée ; formule à corriger (m4).
  - 2009 T : acceptée ; formule à adoucir (m8).
  - 2023 G, « annonça » donné : il faut le déclarer **et** rétablir la consigne officielle (M6, Q10).
  - 2011 G Q3 coupée en deux : retirer la première moitié (m016 Q5) ; pour la seconde (Q7), rétablir le cadre
    officiel, dont le cadre réécrit rendait « vivra » défendable (M7).
  - Placement des pronoms neutralisé en m017 : **approuvé**. C'est une notion du chapitre 12, postérieur au 06
    dans le manifeste, et 12 quiz Q5 pose déjà les placements après l'auxiliaire en distracteurs.
    Les remplacements de M8 la tiennent neutre.
- **Items écartés — rien de neuf perdu, sauf deux** :
  - 2003 a, « regrette que … ne (pouvoir) pas », était dans la consigne de tri et a disparu : il est réintégré
    par M4.
  - 2019 G, « Une année auparavant, mon grand-père m'(apprendre) », plus-que-parfait d'antériorité : le plan
    l'envoyait en 06/06 « s'il apporte du neuf ». C'est le cas, puisque la mission ne posait pas ce piège ; il
    sert de solution de rechange pour M6 Q11.
  - Les autres écarts sont justifiés :
    - 2003 b (si → conditionnel) : sur la liste « ne pas redemander ».
    - 2013 G a et c : même geste que Q3 et Q2.
    - 2006 « venir en aide » : doublon de 05/02 Q2.
    - 2017 G « améliorera » : même geste que « battra ».
    - 2020 T « Depuis toujours (rêver) » : « rêvent » et « ont rêvé » sont tous deux défendables, l'écart
      est donc justifié.
    - 2024 G « expliquer » : « expliquait » est défendable dans la relative.
    - 2016 G, fin du passage : verbes réguliers et « Ce (être) » ambigu.
    - 2012 G « (Arriver)-t-il » : futur, hors famille.
    - Les formes régulières de m014 : répétitives.

## 5. Divers

- **Étages et rampe** : honnêtes. m013 et m016 sont d3, avec des d2 puis des d3 ; m014, m015 et m017 sont d2,
  avec deux d3 en fin. Les en-têtes sont conformes (boss 120/30, practice 75/15). Après M1, m013 reste un vrai
  d3.
- **Titres** : conformes au format « 🏛️ Examens <années> · <sujet> » + étoiles ; m013 à corriger (m1).
- **`sources[]`** : la ligne R8 est ajoutée, mot pour mot, aux `chapter.json` du 05 et du 06.
- **Notation, langue** : aucun chiffre non latin, aucun LaTeX, aucune figure ; aucune faute dans les énoncés ;
  coquilles imprimées signalées par [sic] (2023 G).
- **Autonomie** : chaque question donne sa phrase et sa session ; seul défaut, « verbes soulignés » (m017 Q7,
  M8).
- **« Ne pas redemander »** : respecté, sauf m013 Q8 (M3).
- **Fuites** : aucune clé d'une question n'est livrée par une autre, hormis la forme « puissent » (M4, accepté)
  et l'explication de m013 Q6 (m5, résolu par M4).

## Résumé

52 questions auditées.

- **Clés fausses : 0.**
- **Majeurs : 8 familles, 23 questions à reprendre.**
  - Deux lignes de cours au 05 : « espérer / être sûr » + indicatif, et le choix de l'auxiliaire.
  - Une glose factuellement fausse : m014 Q6, où « elles » désigne les pièces d'un moteur.
  - Surtout, un défaut récurrent : une consigne qui fixe le temps (« au futur », « au passé composé »,
    « imparfait ou passé simple »), ou un rappel de règle, tue les distracteurs. C'est le cas de m013 Q2, Q6,
    Q10, Q11, de m015 Q2, Q10, Q11, de m016 Q1–Q8 et Q10, et de m017 Q1, Q2, Q6, Q7.
  - Quatre questions à retirer : m013 Q8, m016 Q3, m016 Q5, m017 Q1. Une à remplacer : m013 Q6 → 2003 a.
- **Mineurs : 9.**
- **Étiquettes** : celles en place sont justes. L'étiquette neuve est à élargir pour couvrir « croire » ; son
  arabe est corrigé ; elle ne s'applique pas à Q10 ; famille de 3 (Q2, Q3, Q11), à condition d'appliquer M1.
- **Doublons** : m013 Q8 avec 05/02 Q2 (publié) ; m013 Q6 avec Q2 ; m016 Q3 avec Q4.
- **Verdict : à corriger avant publication.** Aucune clé fausse, mais tous les correctifs ci-dessus sont fournis
  mot pour mot. Pour chacun, j'ai vérifié par script la longueur de la clé (ni strictement la plus longue, ni la
  plus courte, sauf m014 Q4 et m017 Q4, structurels et déclarés), j'ai vérifié qu'une seule réponse est juste
  et qu'aucune prémisse n'élimine une option. Après correction : m013 10 q., m014 10, m015 12, m016 8, m017 8.
