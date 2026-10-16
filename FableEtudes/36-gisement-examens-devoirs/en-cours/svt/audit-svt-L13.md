# Audit indépendant — gisement SVT 9ᵉ, vague 2, lot L13 (m038–m043)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills `content-audit` puis
`prof-svt-9eme`). Périmètre : 6 missions, `08-at-tanaffus` 12–14 et `09-al-ikhraj` 10–12, branche
`wip/gisement-svt-9eme-sessions` (commit `818fdb66`). Aucun fichier audité n'est modifié.

Sources lues : transcriptions officielles des sessions citées ; PDF officiels (2010, 2015, 2016, 2018, 2019 ;
2002 et 2005 : l'URL renvoie une page HTML, pas de PDF) ; `cours.md` des chapitres 07, 08, 09 sur `origin/main`.

Rapport écrit au fil de l'eau (état : en cours).

## m038 — `08-at-tanaffus/exercices/12-examens-2019-ex3-et-annales-alveole-frottis-hemoglobine.json`

Étage annoncé d2 (`practice` 75/15) ; 10 questions. Données comparées aux transcriptions 2019 ex.3, 2005 ex.3,
2006 ex.2, 2002 ex.3, 2016 ex.2, 2010 ex.1 et au PDF 2019 (page 2, document 3, rendu à 300 dpi).

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2019 | c (شعيبة / سنخ) | c | OK, réserve | repère 1 déplacé par rapport au PDF (voir « faits signalés ») ; univoque sur la figure de la mission |
| 2 | 2019 | d (paroi mince) | d | réserve (majeur) | clé = rappel du nombre de 08/02-tamrin Q6 ; seule option chiffrée et la plus courte |
| 3 | 2019 | b (réaction 1, O₂ monte) | b | OK, réserve | plan 2×2 propre ; les valeurs 10 → 20 mL viennent du cours, pas de 2019 |
| 4 | 2019 | a (dissociation, consommation) | a | réserve (majeur) | explication qui donne la clé de Q3 ; valeurs 20 → 2 mL = quiz 08 Q9, pas 2019 |
| 5 | 2005 | 1 hématie, 2 plasma, 3 leucocyte | idem | OK, réserve (mineur) | pointe de la flèche 2 à 4–5 unités de deux hématies |
| 6 | 2005 | GR → gaz, plasma → nutriments, GB → défense | idem | OK, réserve (mineur) | trois faits du chapitre 06 (01-tamrin Q5, 03-boss Q3, Q6) |
| 7 | 2006 | d (paroi mince, organes → cœur) | d | OK | 2×2 propre, fidèle |
| 8 | 2010 | c (أسناخ) | c | réserve (majeur) | doublon interne avec Q1 (élément 2) : fuites croisées des explications |
| 9 | 2002 | a (1 et 4) | a | OK | figure fidèle, sens de circulation lisible |
| 10 | 2016 | b | b | OK, réserve (mineur) | `difficulty: 3` dans une mission d2 ; étiquette exacte |

Re-résolution : 10/10 clés justes, aucune ambiguïté de clé.

### Défauts

**[MAJOR] m038 Q8 ↔ Q1 : doublon interne et fuites croisées.** Q1 fait distinguer le سنخ (un sac) de la
حويصلة (la grappe) ; Q8 demande de quoi la حويصلة est faite. L'explication de Q1 dit « الحويصلة الرئويّة هي العنقود
الذي تنتهي به الشّعيبة », celle de Q8 dit « تنتهي كلّ شعيبة بحويصلة رئويّة، وتحمل هذه الحويصلة … الأسناخ » : chacune
résout l'autre (le donjon tire au hasard). Correctif : **retirer Q8** (item 2010-3, ajout de fusion ; la mission
passe à 9 questions, au-dessus du plancher de 6). À défaut, garder Q8 et retirer de l'explication de Q1 les deux
dernières phrases (à partir de « بينما الحويصلة ») : la fuite Q8 → Q1 demeure, d'où la préférence pour le retrait.

**[MAJOR] m038 Q2 : forme et doublon.** La clé « جدار رقيق لا يتجاوز سمكه 0,5 ميكرون » est la seule option
chiffrée, la plus courte (35 contre 37–40), et reprend la donnée que 08/02-tamrin Q6 fait déjà rappeler (« كم يبلغ
سمك جدار السنخ؟ »). Le sujet 2019 demande la propriété, pas la valeur. Remplacer le texte de l'option `d` par :
`جدار رقيق جدًّا يقصّر مسافة عبور الغازين` (40 caractères, à égalité avec `c` : ni la plus longue ni la plus
courte ; même gabarit « structure + fonction » que les trois distracteurs ; une seule réponse juste).
L'explication garde sa valeur 0,5 ميكرون (elle n'est donnée qu'après réponse et ne résout aucune autre question).

**[MAJOR] m038 Q4 : fuite vers Q3.** L'explication finit par « فالتفاعل نفسه يسير في الرئتين في اتّجاه (1) وفي
الأعضاء في اتّجاه (2) » : c'est la clé de Q3. Remplacer cette phrase par :
`فالأكسي هيموغلوبين يتفكّك حيث يُستهلك الأكسيجين.` (aucune mention des poumons ni du sens (1)).

**[MINOR] m038 Q3 et Q4 : attribution des données.** Le sujet 2019 ne donne aucun volume ; 10 → 20 mL est la
donnée du cours 08 (§ échanges) et 20 → 2 mL celle du quiz 08 Q9. Les deux questions restent justes et autonomes,
mais l'étiquette « (مناظرة 2019) » couvre des chiffres qui n'y sont pas. Correctif : préfixe
`(مناظرة 2019، بمعطيات الدّرس)` sur Q3 et Q4, et une ligne dans le rapport d'auteur.

**[MINOR] m038 Q5 : flèche 2.** Elle finit en `L148 62`, la pointe à 4–5 unités des hématies (150.2 ; 45.8) et
(163.2 ; 67.0) : à 232 px, on peut la lire sur une hématie. Aucune trajectoire droite depuis l'étiquette « 2 » ne
trouve une plage de plasma dégagée (recherche exhaustive). Correctif : **retirer** l'hématie (163.2 ; 67.0) (ses
deux `<circle cx="163.2" cy="67.0" …>`). Dégagement vérifié après retrait : 7,8 unités au bout du trait, 9,1 à la
pointe. La clé ne change pas.

**[MINOR] m038 Q10 : étage.** `difficulty: 3` dans une mission annoncée d2 (assignation et `difficulty: 2` du
fichier). Soit Q10 passe à `difficulty: 2` (recommandé : la difficulté réelle est celle de Q9), soit la mission
monte d3 (`boss` 120/30), ce que l'assignation n'a pas prévu.

**[MINOR] m038 Q6 et Q7 : recouvrement.** Q6 reprend trois faits posés au chapitre 06 (01-tamrin Q5, 03-boss Q3
et Q6), Q7 la moitié de 07/02-tamrin Q5 (paroi). Ces questions sont prévues par le plan (2005 q3 et 2006 q3) et
leur forme (appariement, 2×2 avec le sens du sang) est neuve : aucun correctif exigé.

Observations sans défaut : Q8 garde le distracteur « النّيفرونات » du sujet 2010 (notion du chapitre 09, mais
c'est l'option d'origine et elle reste fausse) ; « الأساخ » → « الأسناخ » est une coquille corrigée, pas une
modernisation : pas de mention dans l'énoncé nécessaire. Q9 : « ما رقما الوعاءين » au duel, mais toutes les
options sont des paires : rien n'est trahi. Q10 : étiquette `bio.circ.artere-sang-oxygene` sur `a` exécute
exactement « artère = sang riche en oxygène » (1 et 4 quanis → artères) ; `d` (deux erreurs) reste muette.

