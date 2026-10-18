# Suivis — anglais 9ᵉ (gisement, étude 36)

## S1 — Noms des chapitres 06 et 07 du manifeste ≠ contenu publié (relevé le 2026-10-16, planificateur)

`content/programmes-officiels/manifest/9eme-base.json` (sujet `english`) nomme le 06 « Passive voice » et le 07
« Reported speech » ; les chapitres publiés `content/english/06-passive-voice/` et `07-reported-speech/` portent en
réalité « Communicative Functions » et « Word Building & Linking Words ». Conséquences : les lecteurs ont rangé hors
chapitres (HP) le gérondif, les réfléchis et les possessifs que le 07 enseigne, et au 06 des passifs que rien
n'enseigne. Le gisement suit le contenu publié (décision du pilote : P1–P3 placés au 07, passif écarté) et ne
touche ni au manifeste ni aux slugs.

**Tranché par le propriétaire le 2026-10-18** : on garde le nommage du programme officiel et on ajoute un
commentaire sur le contenu réel. Fait : champ `commentaire` des chapitres 06 et 07 du manifeste
`9eme-base.json` (PR `claude/manifeste-anglais-06-07-commentaire`) ; aucun slug ni titre ne change.

## S2 — Dérivation par suffixes (P3)

Section de cours ajoutée au 07 sur décision du pilote : 15 sessions d'examen l'exigent alors que le manuel (SB
p. 78) ne traite que les noms composés. Réversible : la section cite les sujets officiels comme source de
l'exigence.

## S3 — Livraison : étiquettes existantes modifiées

Le script de livraison ne recopie de la wip que les étiquettes NEUVES (absentes de la base commune). L02 élargit
le libellé d'une étiquette déjà sur `main` : `english.tense.present-avec-marqueur-passe`. La livraison doit
recopier aussi les entrées MODIFIÉES `english.*` (diff de valeur entre base commune et wip), et seulement elles.

## S4 — Fuites entre lots à solder avant la livraison commune

Chaque correctif est vérifié par la re-vérification du lot qui porte le fichier.
- L03 m014 Q1 → L02 m008 Q4–Q5 : effacé par le retrait de m014 Q1 (audit L03).
- L04 m017 Q9 → m007 Q6 ; L04 m017 Q12 → m006 Q12 / m007 Q8 (re-vérif L02 § 3) : à l'audit L04.
- L06 m024 Q3 → m010 Q1 ; L06 m023 Q5 → m008 Q6 (re-vérif L02 § 3) : à l'audit L06.
- L03 m011 Q1 (« passion for working ») → L06 m022 Q4 : correctif dans l'audit L03.
- L02 m006 (01/06) Q6 et L06 m023 (07/07) Q2 (« her daughter, who… ») → L03 m013 Q4 : textes dans l'audit L03 ;
  m006 Q6 (lot L02, déclaré prêt) à reprendre par le pilote avec le texte de l'audit L03, puis contrôle.

## S5 — Moteur (relevé par l'audit L06, hors lot)

`renderLesson` ajoute `<p></table></p>` après chaque tableau ; la section « The gerund » publiée du 07 affiche des
soulignés bruts. À reprendre côté moteur (arena), pas dans le gisement.

## S6 — Décisions du pilote sur les audits L04 et L06 (2026-10-17)

- L04 : lignes de cours au 09 (prépositions dans « Word meaning from context » ; « Linking ideas » : although,
  however, besides), m018 Q12 « I wish » remplacée, étages revus, étiquette `english.prep.preposition-calquee` créée.
- L06 : C3 réécrit (rendu, règle), ligne de cours « own », étiquette `english.pron.sujet-apres-verbe-ou-preposition`
  créée ; famille « -ing ou base après decide… » rejetée, `english.modal.to-oublie` NON élargi (options muettes).
