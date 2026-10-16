# Re-vérification ciblée — lot L04, français 9ᵉ

Auditeur indépendant, 2026-10-16. J'ai relu le commit `2b5fdf51` (`/home/user/wt-fr`, branche
`wip/gisement-francais-9eme`) et le journal `auteurs-notes/fr-L04/CORRECTIONS.md`. Je n'ai rien écrit
dans `content/` ni dans git. Décision du pilote prise en compte : la famille « -ment au masculin »
n'est pas créée.

**Gates.** Moteur `/home/user/eng-svtses`, lié à `wt-fr/content` :
- `content:check` : vert ;
- `content:qa:strict` : 0 erreur, aucune alerte sur les fichiers du lot ;
- `content:tranche --chapters 07,12,14` : 138 q., clé strictement la plus longue 0 %, positions
  24/26/25/25 %, 0 paire proche.

## 1. Renommage et registre

| mission | fichier | titre | `etapes` (registre / fichier) | verdict |
| --- | --- | --- | --- | --- |
| m018 | `07/06-examens-2019-2026-sens-d-un-mot-en-contexte.json` | 2019–2026 | 12 / 12 | OK |
| m019 | `07/07-examens-2019-2026-synonyme-en-contexte-et-autre-sens.json` | 2019–2026 | 10 / 10 | OK |
| m020 | `14/06-examens-2002-2025-former-l-adverbe-en-ment.json` | 2002–2025 | 10 / 10 | OK |
| m021 | `14/07-examens-2007-2026-homophones-en-contexte.json` | 2007–2026 | 8 / 8 | OK (voir R2 : passerait à 7) |
| m022 | `12/06-examens-2003-2021-le-pronom-qui-remplace-le-groupe.json` | 2003–2021 | 11 / 11 | OK |

Les anciens noms ont disparu de l'arbre et de `git ls-files`. Ce qui reste est mineur :

- **Commit d'un autre lot.** Les deux renommages du ch. 07 sont partis dans le commit de L02
  (`6b2f2d03`, R100), pas dans celui de L04. C'est sans effet sur le contenu ; je le note pour la
  traçabilité.
- **Plan.** `plan-examens-v1.json` (l. 567, 613, 731) garde les anciens noms. C'est un document de plan,
  sans effet en CI.
- **Sessions sans question.** `sources` du registre liste encore des sessions qui ne donnent plus
  aucune question :
  - m018 : 2018 T ;
  - m019 : 2020 G, 2018 G, 2016 G, 2016 T, 2015 G ;
  - m021 : 2011 G, 2019 G, 2018 G ;
  - m022 : 2001, 2015 T, 2010 T, 2012 T.

  Soit les retirer, soit dire dans `note` qu'elles ont été « lues, écartées ».

## 2. Mes correctifs, vérifiés tels qu'appliqués

Les textes sont ceux que j'avais fournis, appliqués à la lettre :
- critique C1 ;
- majeurs M1, M2, M3, M4, M5, M6, M7, M10, M11 ;
- mineurs m2, m4, m5, m6, m8, m10.

M8 et M12 sont revus en R2 et R3 ci-dessous.

**Mon correctif M8 était défectueux** (la question 2009 G de m021, Q7 du fichier) : voir R2.

## 3. Re-résolution à l'aveugle (questions retouchées et voisines)

| fichier · Q | ma réponse | clé | verdict |
| --- | --- | --- | --- |
| 07/06 · Q4–Q6 | passer · personne connue · gonfler | d · a · b | OK |
| 07/06 · Q7 (couronne) | conclut | d | OK — plus d'option éliminée par l'énoncé |
| 07/06 · Q10–Q12 | correction · prix réduit · coup de foudre | b · d · c | OK |
| 07/07 · Q1–Q5 | discrète · usage · résolu · en plein travail · la remplacer | b a c d c | OK |
| 07/07 · Q9, Q10 | « proposer un emploi » · « table réservée » | b · c | OK — plus de fuite vers Q1/Q2 |
| 14/06 · Q1–Q10 | chaleureusement, régulièrement, rapidement, fréquemment, quotidiennement, absolument, constamment, profondément, nettement, impatiemment | d b d c a d b c a b | OK — **mais voir R1** |
| 14/07 · Q1 | Quand … Quant | c | OK |
| 14/07 · Q2 (fusion ni / n'y) | n'y / Ni / ni | a | OK — vote nul à chaque position |
| 14/07 · Q3–Q6 | Quand … qu'en · qu'en · Sans s'en · s'en | d b a c | OK |
| 14/07 · Q7 (2009 G) | qu'elle … quelle | b | **défaut R2** |
| 14/07 · Q8 (2008) | quels | b | réserve R3 |
| 12/06 · Q1–Q11 | l'ont · le cacher · Nous le · de lui · lui a demandé · y · y · en · la laissent · à les réciter · le mettre | b d c a c b a d b a c | OK |

**Votes recalculés (14/06).**
- Q1, Q2, Q3, Q5, Q7 et Q9 : le vote est nul ou désigne un distracteur.
- Q4 et Q6 hésitent entre la clé et un distracteur.
- Q10 était déjà en 2×2.

**Fuites.**
- Les explications de 14/06 Q6 et Q9 ne nomment plus « profond ».
- L'explication de 07/07 Q9 ne donne plus « usage ».
- Le rappel de 14/07 Q2 est symétrique.
- Aucune explication d1 ne livre une clé d2.

## 4. Défauts restants

### R1 — MAJEUR — 14/06 Q1, Q4, Q6, Q7 : « Dans le même texte » (autonomie)

Je l'avais manqué au premier audit pour Q4, Q6 et Q7 (anciennes Q3, Q5, Q6). Avec la nouvelle tête de
mission, Q1 renvoie maintenant à une question qui n'existe plus. Le donjon tire au hasard : la question
doit se suffire. Énoncés de remplacement (phrases conformes à 2025 G et 2024 G ; le reste est
inchangé) :

- Q1 → `(Examen 2025 générale) Dans un restaurant de Montréal, on parle du personnel : « Le personnel les accueille (chaleureux) … et leur sert des plats. » Quel adverbe en -ment forme-t-on sur l'adjectif « chaleureux » ?`
- Q4 → `(Examen 2025 générale) Dans un restaurant de Montréal : « Les clients viennent (fréquent) … au Madelinot. » Quel adverbe en -ment forme-t-on sur l'adjectif « fréquent » ?`
- Q6 → `(Examen 2024 générale) Une adolescente raconte : « … alors que je voulais (absolu) … étudier le solfège. » Quel adverbe en -ment forme-t-on sur l'adjectif « absolu » ?`
- Q7 → `(Examen 2024 générale) Une adolescente raconte : « Quant à moi, j'étais (constant) … amenée à les suivre. » Quel adverbe en -ment forme-t-on sur l'adjectif « constant » ?`

Ces énoncés ne touchent pas aux options : les longueurs de clé restent celles qui sont vérifiées
(aucune n'est la plus longue). Aucune fuite : aucun n'emploie un autre adverbe du lot.

### R2 — MAJEUR — 14/07 Q7 (2009 G) : mon correctif M8 vide la question

Le rappel nomme la locution « quel que soit ». Le second blanc (« … que soit la responsabilité ») est
donc tranché par l'énoncé lui-même : il ne reste que les options b et d. La question se réduit alors au
premier blanc, « sait déjà … réussira », c'est-à-dire « qu'elle » devant un verbe. C'est le geste de
14 quiz Q1 et de 14/05 Q6, tous deux sur la liste « ne pas redemander ».

Sans le rappel, la locution n'est enseignée nulle part. Rien ne reste à poser sur cette phrase qui ne
fasse doublon : le premier blanc de 2009 G (« … métier choisir ») est le « quel » interrogatif, que
13 quiz Q5 pose déjà.

Correctif : **supprimer Q7** (m021 passe à 7 questions, dans la fourchette R7). Mettre à jour `etapes`
à 7 dans le registre. 2009 G sort alors de la mission ; le titre 2007–2026 reste juste.

### R3 — MINEUR — 14/07 Q8 (2008) : clé reconstituable au vote

Le rappel élimine « qu'ils » à vue. Restent `quelles` / `quels` / `quel` : le vote donne masculin
(2 contre 1) et pluriel (2 contre 1), donc `quels`. Correctif : option c `qu'ils` → `quelle`,
muette. Le plan devient 2×2 genre × nombre.

| option | forme | longueur |
| --- | --- | ---: |
| a | quelles | 7 |
| b (clé) | quels | 5 |
| c | quelle | 6 |
| d | quel | 4 |

La clé n'est ni la plus longue ni la plus courte. Explication, dernière phrase →
`« Quelles » et « quelle » sont au féminin, « quel » reste au singulier : seul « quels » s'accorde avec « mes défauts ».`

### R4 — MINEUR — distracteurs ajoutés presque synonymes d'un autre

- 07/07 Q3 : « lent » double « traînant ».
- 07/07 Q5 : « la saluer » double « lui dire au revoir ».

Chaque paire s'élimine d'un bloc, sans ambiguïté sur la clé. C'est toléré : le texte peut rester.
Si l'auteur veut le corriger : Q5 `la saluer` → `la gronder` (10 caractères, clé « la remplacer » 12,
la plus longue reste « l'aider à se relever »).

## 5. Écarts déclarés par l'auteur — jugés

1. **12/06 Q6 et Q7, clé « y » strictement la plus courte.** Accepté. C'est inhérent à un pronom d'une
   lettre : 2 items sur 11, aucun indice ailleurs dans la mission, et la mesure de tranche est à 0 %.
2. **14/06 régulièrement et rapidement, ex aequo avec l'option la plus courte.** Accepté : ce n'est pas
   « strictement », et le vote est nul (plan 2×2).
3. **Faux synonymes ajoutés.** Tous sont faux sans ambiguïté et n'exécutent aucune erreur défendable :
   - « une personne âgée » (07/06 Q5) ;
   - « à crédit » (07/06 Q11) ;
   - « lent » (07/07 Q3) ;
   - « au repos » (07/07 Q4) ;
   - « la saluer » (07/07 Q5) ;
   - « y ont réconforté » (12/06 Q1, `y-pour-personne` exact).

   Réserve de fidélité sur 07/06 Q5 : « une personne étrangère » était une option officielle, et une
   clé une seule fois la plus courte n'est pas un défaut. Le remplacement est déclaré et acceptable ;
   rétablir l'option officielle est possible mais pas nécessaire. Doublons internes : voir R4.
4. **12/06 Q4 d, « d'elle » gardé.** Accepté. Mon « de le » rendait la clé strictement la plus longue :
   la raison est bonne. Le distracteur reste faible (genre d'André), mais il ne rend pas la clé
   ambiguë.
5. **m3, m7 et m9 laissés tels quels.** Accepté, conformément à mon premier audit (« à garder »).

## Résumé

- **Clés fausses :** 0. Questions re-résolues : 51 (12 + 10 + 10 + 8 + 11).
- **Majeurs restants : 2.**
  - R1 — 14/06 Q1, Q4, Q6, Q7 : « Dans le même texte » ; remplacer par les quatre énoncés de R1.
  - R2 — 14/07 Q7 (2009 G) : supprimer ; m021 passe à 7, `etapes` à 7.
- **Mineurs restants :**
  - R3 — 14/07 Q8 : `qu'ils` → `quelle` ; explication, dernière phrase → « « Quelles » et « quelle »
    sont au féminin, « quel » reste au singulier : seul « quels » s'accorde avec « mes défauts ». »
  - R4 — 07/07 Q3 et Q5 : distracteurs presque synonymes, toléré ; option `la saluer` → `la gronder`.
  - Registre : `sources` liste des sessions sans question (§ 1).
  - Commit et plan : renommages du ch. 07 partis dans le commit de L02 ; anciens noms encore dans
    `plan-examens-v1.json`.
- **Verdict : à corriger** (deux majeurs simples, sans nouvelle rédaction). Une fois R1 et R2 appliqués,
  le lot est bon pour fusion.
