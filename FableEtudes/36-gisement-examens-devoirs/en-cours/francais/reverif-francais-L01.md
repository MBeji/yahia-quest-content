# Re-vérification ciblée — lot L01, français 9ᵉ, chapitre 09

Auditeur, 2026-10-16. Commit `a0be086e` (`/home/user/wt-fr`), fichiers `09/exercices/06…11` et la question publiée
`09/05 Q2`. Journal de l'auteur lu (`auteurs-notes/fr-L01/CORRECTIONS.md`). Aucune écriture dans `content/` ni
dans git.

Gates sur ce commit : `content:check` vert ; `content:tranche --chapters 09` : clé strictement la plus longue 0/68,
0 paire proche, **0 groupe gabarit** (le doublon 08/05 × 09/05 a disparu) ; `content:qa --strict` : **0 erreur**
(l'erreur anti-verbatim de `french-1ere-sec` est levée par a6b823e5).

Toutes les questions retouchées ou fusionnées, et leurs voisines, ont été re-résolues à l'aveugle (45 questions
dans les six missions, plus 09/05 Q2) : **0 clé fausse**. Les 2×2 sont conformes (chaque case deux fois, clés
déplacées, ni la plus longue ni la plus courte).

## Écarts déclarés par l'auteur

1. **m001 Q7 (ex-Q8), clé sans « En »** : **accepté.** Fragment littéral (« m'efforçant d'ignorer autant que possible
   le trac »), 76 caractères, à égalité avec d : pas strictement la plus longue.
2. **m006, étiquettes non posées** : **accepté, c'est mon erreur.** `schema.ts` l. 778–781 : les options
   `multi`/`ordering`/`matching` sont `.strict()` (`id`, `text` seulement). Ces distracteurs restent muets.
3. **m005 « côte à côte », citation sans l'appel ²** : **accepté** (un appel de note n'est pas du texte).
4. **m004 Q5 « Frank = l'entraîneur »** : **à retirer.** J'ai vérifié sur le PDF officiel (page 1, rendue) : le nom
   « Frank » n'apparaît qu'une fois, dans « Depuis que Frank a parlé du stage », juste après une coupure « […] » du
   sujet. Aucune phrase imprimée ne dit qui est Frank. Dans le texte, l'entraîneur annonce le stage, mais Loïc
   « parle » aussi du stage (« Qui suivra le stage ? »), et la coupure peut cacher un autre personnage. La lecture
   « Frank = l'entraîneur » est très probable, mais c'est une déduction. Par ta règle, elle ne doit pas porter une
   clé. Autre défaut : les énoncés de Q4 et de Q6 posent tous deux « L'entraîneur annonce … un stage », ce qui
   fournit la prémisse. **Correctif : supprimer Q5.** m004 passe à 6 questions (dans R7).
5. **m006 Q3, infirmier** : **refusé, c'est mon correctif qui était défectueux.** 08/04 Q5 (publiée) contient le
   message « on soigne des malades. Ensuite, on travaille dans un hôpital. Enfin, on porte une blouse blanche » : il
   sert justement de leurre « description sans argument », face à « j'aime aider les malades ». Notre Q3 reprend
   l'hôpital, la blouse blanche et « soigner les malades » pour le même contraste raison/description : c'est un
   doublon de contenu, **majeur**. Correctif vérifié ci-dessous (métier : agriculteur, absent des exercices de
   `french`).

## Nouveaux défauts relevés (texte exact)

### m002 — `07-…-portrait-serveuse.json`

- **Q7, majeur (fuite vers Q5, qui m'avait échappé au premier passage).** L'énoncé « terminer ses études « ne
  pressait pas » pour Tania » dit qu'elle terminera ses études un jour : c'est le contenu de la clé de Q5 (« elle
  finira probablement ses études un jour »), et cela réfute le leurre « très vite ». Remplacement :
  - énoncé : « D'après la dernière phrase du texte, que le travail au Madelinot apporte-t-il à Tania, pour
    l'instant ? »
  - options : a `"Un salaire plus élevé que celui d'un étudiant."` (46, `fr.lecture.deduction-sans-indice`) ;
    b `"La fatigue de servir tant de clients chaque midi."` (49, `fr.lecture.deduction-sans-indice`) ;
    c `"Une heureuse sensation d'équilibre et d'harmonie."` (49, clé) ; d `"La promesse de diriger bientôt le
    restaurant."` (45, `fr.lecture.deduction-sans-indice`) ; difficulté 3 inchangée.
  - explication : « La dernière phrase le dit : pour l'instant, travailler au Madelinot lui procure « une heureuse
    sensation d'équilibre, d'harmonie avec l'Univers ». Le texte ne parle ni de salaire, ni de fatigue (Tania est au
    contraire « rayonnante »), ni d'une promotion. »
  (Citations littérales, clé à égalité de longueur avec b, aucune mention des études : plus de fuite vers Q5 ni
  vers Q6.)
- **Q6, mineur (accepté tel quel)** : l'énoncé « Tania a arrêté des études à l'université » laisse deviner qu'elle
  pourrait les reprendre. La clé de Q5 demande en plus la nuance « probablement » : pas de correctif exigé.

### m003 — `08-…-enfant-face-a-l-incendie.json`

- **Q1, majeur (introduit par mon correctif).** Les options b et d citent « Il faut sauver le gardien ! » : cette
  réplique donne la clé de Q3 (« Il sait le gardien en danger dans la remise »). La même citation est aussi
  l'option e de Q2 (fuite déjà présente au premier passage, que je n'avais pas vue). Remplacements :
  - Q1 b → `"Il avance vers la remise : « Je fixais cette porte »"` (52) ; Q1 d → `"Il fuit loin de la remise : « Je
    fixais cette porte »"` (53) ; a (72) et c (clé, 71) inchangées. Explication → « Il avance malgré la peur :
    « J'avais peur mais j'avançais quand même. » Cette phrase dit l'action elle-même. « Je fixais cette porte » dit
    où va son regard, pas ce qu'il fait. Fuir est le contraire de ce que raconte le texte. »
  - Q2 e → `"« la chaleur était devenue insupportable »"`. Fin de l'explication → « …l'arrivée des pompiers est une
    autre scène ; la chaleur décrit la situation, pas un geste de Mme Schaeffer. »
  (Citations littérales ; « Il faut sauver le gardien ! » n'apparaît plus nulle part dans la mission.)
- **Q6, majeur : rang d'option dans l'explication.** « la troisième phrase raconte… » → « « Ils ont éteint
  l'incendie, puis ils ont emmené Yves » raconte l'intervention des pompiers, sans rien dire de ce que le chef pense
  de l'enfant. » (L'ancien « ce que les pompiers font pour tous » ne correspond plus à l'option c retenue.)

### m004 — `09-…-reve-de-footballeur.json`

- **Q5 (Frank) : supprimer** (écart 4). Le reste est vérifié : 2×2 rêve (clé c), « redescend sur terre » (clé b,
  sens figuré), 2×2 silence (clé a), réaction, participants (d corrigé, ne nie plus la prémisse), activités
  (`multi`, d « tournoi en Auvergne »). Aucune fuite restante : l'explication de Q3 (« annoncée par l'entraîneur »)
  ne gêne plus une fois Q5 supprimée.

### m006 — `11-…-projet-metier-justifier.json`

- **Q3, majeur (écart 5)** : dans l'énoncé, remplacer « infirmier » par « agriculteur ». Options →
  a `"Je cultiverai des légumes sur la terre de mon grand-père."` (57) ;
  b `"Je ferai deux ans de formation dans un lycée agricole."` (54) ;
  c `"Nourrir les gens avec mes récoltes me rend très fier."` (53, clé) ;
  d `"Je me lèverai chaque jour avant le lever du soleil."` (51). La clé n'est ni la plus longue ni la plus courte ;
  options muettes. Explication → « Une raison dit pourquoi on choisit ce métier : la fierté de nourrir les gens.
  Ce que l'on cultivera, la formation et l'heure du lever décrivent le projet, sans le justifier. La consigne attend
  les deux, mais il faut savoir les distinguer. » J'évite « oliviers » (exemple du cours 12) ; « agricult… »
  n'apparaît dans aucun exercice de `french`.

## Question publiée 09/05 Q2 (réécrite)

Conforme au texte proposé. Re-résolue : clé a. Elle partage la longueur maximale (57) avec c. Plus de gabarit avec
08/05 Q1. Seule **réserve mineure** : « sans faire de blessé » va un peu au-delà du texte, qui dit seulement que le
chauffeur est « sorti indemne ». Remplacement possible : a `"Un camion s'est renversé à Kairouan, chauffeur
indemne."` (55 ; b 52, c 57, d 55). Optionnel.

## Autres vérifications

- Mes textes d'audit sont repris fidèlement dans m001, m002 (Q5, Q6), m003 (Q3–Q5), m004, m005 et m006
  (Q1, Q4, Q5, Q8, Q9). Toutes les citations ont été revérifiées littérales.
- Autonomie : aucun énoncé ne renvoie à une autre question (m005 Q6 dit les « deux hypothèses » en propre).
- Explications par rang : il n'en reste qu'une, m003 Q6 (ci-dessus).
- **07/06 Q5 (lot L04)** : son énoncé « …rapproché de lui au collège : « Son père était une personnalité de la
  ville. » » donne la clé de m005 Q1 (« au collège ») et la phrase-leurre de m005 Q2. **Rien dans L01 n'en dépend.**
  m005 ne cite pas 07/06, et la correction de L04 (retirer « au collège » de son énoncé) suffit, sans retouche de
  L01. Si L04 cite encore « personnalité de la ville », cela reste sans effet sur L01 : dans m005 Q2, cette phrase
  est la mauvaise preuve, et la clé est « ne se fréquentaient pas ».

## Résumé

- **Clés fausses : 0.**
- **Majeurs restants : 5.**
  - m002 Q7 : l'énoncé donne la clé de Q5.
  - m003 Q1 et Q2 : la citation « Il faut sauver le gardien ! » donne la clé de Q3.
  - m003 Q6 : l'explication désigne une option par son rang (« la troisième phrase »).
  - m004 Q5 : la clé « Frank = l'entraîneur » est une déduction, pas un fait du texte ; à supprimer.
  - m006 Q3 : doublon de contenu avec 08/04 Q5 (infirmier, hôpital, blouse blanche).
  Textes de remplacement exacts ci-dessus.
- **Mineurs : 2**, sans correctif exigé : m002 Q6 (léger indice vers Q5) ; 09/05 Q2 « sans faire de blessé »
  (remplacement optionnel donné).
- **Écarts de l'auteur** : 1, 2 et 3 acceptés ; 4 : supprimer la question ; 5 : refusé, nouveau texte agriculteur.
- **Verdict : à corriger, puis prêt.** Il ne reste que des correctifs de texte, sans nouvel audit complet ; un
  contrôle rapide des cinq points suffit.

## Suite donnée par le pilote (2026-10-16)

Les 5 majeurs et le mineur optionnel (09/05 Q2) appliqués mot pour mot par l'auteur ; écart accepté : m006 Q7,
clé de conclusion allongée (82 → 88 car.) pour ne plus être strictement la plus courte, sens inchangé. Gates verts
(`content:check`, `qa:strict` 0 erreur, tranche 09 : 0/67). **L01 prêt à livrer.**
