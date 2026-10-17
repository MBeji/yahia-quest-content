# Re-vérification — lot L06 (anglais 9ᵉ, chapitre `07-reported-speech`)

Auditeur indépendant, 2026-10-17. Objet : le commit `01dfcbec` (« L06 corrections d'audit appliquées »), comparé à
`audit-anglais-L06.md`. Décisions du pilote prises en compte : l'étiquette (a) est créée ; `english.modal.to-oublie`
n'est pas élargie. Je n'ai rien écrit dans `content/` et je n'ai fait aucune opération git. Les fichiers du chapitre 09
modifiés par L04, en cours d'écriture, ne sont lus que pour les fuites.

## 1. Gates (moteur `/home/user/eng-en`, état courant)

- `content:check` : vert (english : 66 exercices, 491 questions).
- `content:qa:strict -- --subject english` : code 0, aucune erreur, aucune clé suspecte.
- `content:tranche -- --subject english --chapters 07-reported-speech` : clé strictement la plus longue **0/61**
  (contre 3/61 avant), 0 paire proche, 0 gabarit. Positions des clés : 29 / 25 / 27 / 20 %.

## 2. Cours et résumé

| point | état | contrôle |
| --- | --- | --- |
| D1 — rendu C3 | **levé** | `renderLesson` : plus aucun souligné brut dans le texte de C3 (amorce, exemple en trois étapes, cas limite). Seuls les blancs `___` restent, voulus. |
| D2 — `propriete` C3 | **levé** | texte identique au correctif. « a ___ pupil » est désormais un adjectif selon la règle ; « the ___ industry » et « ___ opportunities » relèvent du cas limite « a noun can also say what kind ». |
| D8 — ligne « own » (§ Possessives) | **levé** | insérée dans le bloc `propriete` après le cas limite, rendue en `<em>Lina has her <strong>own</strong> room.</em>` |
| Ajout de l'auteur au résumé : « **own** stresses "nobody else's" (_her own room_) » | **accepté** | il reprend exactement la ligne du cours, sans notion nouvelle, et l'exemple n'est pas un item d'examen. Le rendu dans la carte Possessives est correct. Le mot commence la phrase en minuscule, comme « **its** » juste avant : cohérent. |

## 3. Questions modifiées, re-résolues à l'aveugle

| fichier | Q | correctif | ma réponse | clé | verdict |
| --- | --- | --- | --- | --- | --- |
| m022 (07/06) | 1 | m2 « A pupil describes Aunt Emily… » | reading | b | OK |
| m022 | 7 | D9 « To being » (muet) + explication | Being | a | OK. Being (5) n'est pas la plus longue (To being, 8) ; aucun indice de forme |
| m022 | 11 | m1 : explication sans la liste des verbes | to protect | a | OK, ne donne plus « need » à Q12 |
| m022 | 12 | D11 « wake » (muet) + explication | to wake | a | OK, plan 2×2 exact (to / ∅ × base / -ing) |
| m023 (07/07) | 1 | D12 + étiquette (a) sur « he » | him | a | OK, l'explication est juste |
| m023 | 2 | D5 « A parent writes about a teenage daughter… » + (a) sur « they », themselves muet | them | b | OK |
| m023 | 4 | (a) sur « they » | them | a | OK |
| m023 | 5 | D4 « …She says: "That job made ___…" » + explication | me | d | OK, « her » ne se défend pas (elle parle d'elle-même) |
| m023 | 6 | (a) sur « they » | them | b | OK |
| m023 | 7 | D8 : sans glose, sans « ourselves » (own / one / self) | own | a | OK, solvable par la ligne du cours |
| m023 | 8 | D7 « I » + (a) | me | c | OK, aucun distracteur ne se défend |
| m024 (07/08) | 3 | D3 (fin « then… ») + m5 (sans advisor) | advise | b | OK |
| m024 | 5 | D10 + « constructively » | construction | a | OK, 12 < 14 |
| m024 | 6 | D10 + « employments » | employment | c | OK, 10 < 11 |
| m024 | 8 | D10 + « environmentalism » | environmentalist | b | OK, égalité à 16 |
| m024 | 9 | correctif de L04 (« …her ___ and has become… ») + m6 | choice | b | OK, réserve r1 |
| m024 | 10 | m7 `acceptedAnswers: ["famed"]` | famous | — | OK, la variante est juste et n'égale aucune erreur déclarée |
| m024 | 11 | m8 expectedMistake `exciteing` + étiquette spell | exciting | — | OK, l'étiquette est exacte |

Les questions non modifiées (m022 Q2–Q6, Q8–Q10 ; m023 Q3, Q9–Q12 ; m024 Q1, Q2, Q4, Q7, Q12) sont identiques à
l'état audité. Leur verdict ne change pas.

**Étiquette (a) `english.pron.sujet-apres-verbe-ou-preposition`.** Les libellés fr, en et ar sont ceux du correctif.
Elle a 5 placements, tous exacts : m023 Q1, Q2, Q4, Q6, Q8. m023 Q3 « he » reste muet, à raison : le blanc demande
un possessif. **`to-oublie` non élargie** : m022 Q11 « protect » et Q12 « wake » sont muets, ce qui est conforme.

## 4. Fuites, dans les deux sens

J'ai relancé un script qui confronte chaque phrase officielle et sa clé à tous les énoncés et explications des missions
et des quiz de `content/english/` :
- **D3** (m024 Q3 vers m010 Q1, « will regret ») : **levée**.
- **D4** (m023 Q5 vers m008 Q6, « gained ») : **levée**.
- **m011 Q1 vers m022 Q4** (« passion for working ») : **levée** (corrigée côté L03).
- **D5** (m023 Q2 vers m013 Q4, « her daughter, who ») : **levée**. L'énoncé ne contient plus « who ». L'item 2012 T
  de m013 (08/06, « My daughter, ___ is 15 ») est intact.
- **D6** (09/13 Q11 vers m023 Q11, « help themselves ») : **levée** par L04. L'énoncé s'arrête à « …in someone else's
  life. », et « role » reste la seule réponse.
- **m024 Q9 vers 09/11 Q12** (« proud of her » donnait la clé « of ») : **levée** par le correctif de L04.
- Une seule occurrence reste : « all of them » dans l'explication de 08/07 Q3 (comparatifs). C'est une tournure
  générique, sans lien avec la phrase de 2018 T : ce n'est pas une fuite.
- Dans le lot, entre questions : aucune fuite.

## 5. Réserve (mineure, sans correctif exigé)

- **r1** — m024 Q9 : depuis la coupe de L04, la citation est un fragment sans verbe principal (« …her ___ and has
  become an active member in her community. »). La clé reste unique : après *her*, il faut un nom, et le contexte
  « left her job… to follow a training program » donne le sens de décision. La phrase se lit un peu moins bien, mais
  elle est acceptable. On ne peut pas rétablir « proud of » sans rouvrir la fuite vers 09/11 Q12.
- Remarque, hors lot : la même lettre de 2012 T est présentée par « A mother » (01/06), « A father » (08/06) et
  « A parent » (07/07). La transcription ne précise pas qui écrit. C'est sans effet sur les clés.

## 6. Verdict

D1 à D12 et les mineurs m1 à m8 sont levés ; m9 à m11 étaient de simple signalement. Aucune clé fausse sur les
36 questions. Les gates sont verts et la tranche est à 0 % de clé la plus longue. Les fuites sont toutes levées dans
les deux sens. L'étiquette (a) est en place avec 5 placements exacts. Seule reste la réserve mineure r1, qui
n'appelle pas de correctif.

**L06 : bon pour livraison.**
