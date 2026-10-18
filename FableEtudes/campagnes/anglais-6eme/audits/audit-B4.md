# Audit B4 — anglais 6ᵉ, chapitre `07-around-the-world` (2026-10-18)

Auditeur indépendant. Branche `wip/anglais-6eme-un-passage`, HEAD `e2346436`. Périmètre : carte `assign-B4.md` — `quiz.json`, `exercices/01…05` (étiquettes, réécritures), `06` (m018), `07` (m019), `08` (m021, devoir), `09` (D6), section `## 🔊 Let's pronounce` du `cours.md` + puce du `resume.md`, `chapter.json`. Re-résolution à l'aveugle de toutes les questions AVANT la lecture du rapport et des notes de l'auteur. Aucun fichier de `content/` modifié, aucune écriture git.

Gates rejoués (moteur `/home/user/eng-deliver`) : `content:check` ✓ ; `content:qa -- --subject english-6eme` ✓ (0 erreur) ; `content:tranche -- --subject english-6eme --chapters 07 --fresh --strict-longest` : clé strictement la plus longue 0/28, paires proches 0, gabarits 0 ; `content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/english-6eme …/08-devoir-a-postcard-from-my-town.json` : aucune plage ≥ 8 mots, aucune donnée commune.

## 1. Re-résolution (55 questions)

| Fichier | Questions | Ma réponse = clé | Verdict |
| --- | --- | --- | --- |
| quiz | 5 | 5/5 | OK |
| 01-pratique | 6 | 6/6 | #1 réserve (dessin absent) |
| 02-boss | 6 | 6/6 | #4 étiquette sur l'option à deux erreurs |
| 03-revision | 6 | 6/6 | #3, #6 réserves mineures |
| 04-defi | 6 | 6/6 | **#3 : deux réponses défendables** |
| 05-entrainement | 6 | 6/6 | **#1 : deux réponses défendables** ; #2 doublon du quiz#2 |
| 06 m018 (reading 2025) | 6 | 6/6 (ordering b-d-a-c conforme au PDF) | #2 clé livrée par la citation ; #4 sans données |
| 07 m019 (examens) | 5 | 5/5 | OK |
| 08 m021 (devoir) | 6 | 6/6 (matching unique, multi a-b-d-f) | OK |
| 09 prononciation | 4 | 4/4 | #3 « key » juste selon la règle du cours |

**Clés fausses : 0.**

Fidélité examen (PDF 2025 p. 1 et transcriptions 2013, 2015, 2016, 2018) : texte de m018 relu sur le PDF ; ordre des événements, « countries », « won », « e-mail » conformes ; 2013 « a old garage », 2015 « on / of / from », 2016 « many new ≠ … houses », 2018 « (t n h r o) of England », 2025 W1c conformes. « There is five rooms » rendu « There are » (hors guide) : déclaré, accepté.

Salle blanche m021 : comparée à la main à D07 (Tunis, Dear Victoria, hotels, shops and restaurants, train station, weather, post office) et D08 (New York, Dear Aly, main park, cinemas, supermarkets) : aucun nom, aucun thème, aucune phrase repris (Leila / Omar / Port Salma / castle / harbour, « See you soon », formules générales). Outil : 0 plage. **Propre.**

## 2. Défauts

### Critiques — double réponse (à corriger avant merge)

**C1. `exercices/04-defi.json` #3** — l'option b « How about travelling by plane in Spain? » est une phrase correcte (voyager en avion À L'INTÉRIEUR de l'Espagne) : deux phrases « completely correct ». Remplacement (vérifié : clé 39 car., option b 39 car., la clé n'est pas strictement la plus longue) :
- b → `"text": "How about travelling by plane by Spain?", "misconceptionTag": "english.prep.travel-by-to-confondus"`
- explication → « Three rules meet here: after How about the verb takes -ing, the plane is a vehicle so it takes by, and Spain is a place so it takes to. Each of the other sentences breaks one of them: the bare travel after How about, the word by in front of the country, or the -ing form after Let's, which always wants the bare verb. »

**C2. `exercices/05-entrainement.json` #1** (réécrit par B4) — « On a map of the Mediterranean, where is Tunisia compared with Spain? » : sur la vraie carte, la Tunisie est à droite ET en dessous de l'Espagne ; « Below Spain. » est vrai. En outre, le geste (direction → place sur la carte) est celui de m021#2. Remplacement (contexte inventé, sans géographie réelle ; geste « relation inverse » enseigné par l'exemple du cours ; clé 5 car. = north 5 car.) :
- prompt : « On Sami's treasure map, the old well is north of the palm tree. Complete: "The palm tree is ___ of the old well." »
- options : a `west` (`english.vocab.directions-confondues`) · b `north` (`english.vocab.directions-confondues`) · c `south` (clé) · d `east` (`english.vocab.directions-confondues`) ; `correctOption: "c"`
- explication : « North is the top of the map, so the well is above the palm tree and the palm tree is below it: the palm tree is south of the old well. North would put the tree above the well, and east and west are the right and left sides of the map, which the sentence about the well does not use. »

### Majeurs

**M1. Libellé de `english.article.a-an-selon-la-lettre` (doute 1 de l'auteur).** Le libellé dit « Tu choisis a ou an d'après la lettre écrite et non d'après le son » — or sur *a egg*, *an cape*, *a old garage*, *a Indian*, *a amphitheatre*, *an big*, *an flamenco*, *an country*, la lettre et le son coïncident : l'élève qui suit la lettre répond JUSTE. L'étiquette ne nomme donc pas l'erreur exécutée sur ses 9 options (quiz#4 a-d, 02#5 c, 03#6 b, 04#1 a-b-d, m019#3 b-c), et le libellé contredit le cours, qui enseigne la règle de la lettre (« the first letter of the next word »). L'id n'est employé que par le 07. Correctif : garder l'id et les 9 étiquettes, **réécrire le libellé** dans `content/misconceptions.json` (sans *an hour* / *a uniform*, que le cours n'enseigne pas et qui contredisent sa règle) :
- fr : « Tu mets a devant un mot qui commence par une voyelle, ou an devant un mot qui commence par une consonne : an devant un son de voyelle (an amphitheatre, an old garage, an egg), a devant un son de consonne (a cape, a big garden). »
- en : « You put a before a word that begins with a vowel, or an before a word that begins with a consonant: an before a vowel sound (an amphitheatre, an old garage, an egg), a before a consonant sound (a cape, a big garden). »
- ar : « تضع a قبل كلمة تبدأ بحرف علّة، أو an قبل كلمة تبدأ بحرف ساكن: an قبل صوت حرف علّة (an amphitheatre, an old garage, an egg) وa قبل صوت حرف ساكن (a cape, a big garden). »
(Reporter le texte dans `vocab-english-6eme.json` et `map-vocab.md`.)

**M2. `09-lets-pronounce…` #3 — « key » (doute 6).** Le cours enseigne « y final : mot court d'une syllabe → /ai/ ». *key* est un mot d'une syllabe terminé par y : la règle du cours le désigne comme réponse, à côté de *cry*. Remplacement (clé 3 car., non la plus longue) : b → `"text": "very", "misconceptionTag": "english.sound.lettre-pour-son"` ; explication → « Cry is a short word, and the y at the end of a short word says /ai/, like fly and try. Very, happy and windy are long words, so their y says /i/. »

**M3. `06-exam-2025…` #2 — la citation livre la clé.** L'énoncé ne cite que « She won the prize. » : *won* est la seule option présente dans l'extrait, *felt / worked / waiting* s'éliminent sans lire. Remplacement de la ligne de citation (fidèle au PDF p. 1, les quatre options y figurent, aucune fuite nouvelle : la phrase de l'e-mail est élidée) : « Paragraph 2 says: "Annie felt excited to participate. She worked hard, reading every book about Tunisia. […] She won the prize. The little girl started to imagine all the great experiences waiting for her." » Options, clé et explication inchangées.

**M4. `06-exam-2025…` #4 (ordering) — question sans données.** Aucun passage du texte n'est donné : l'ordre « loved visiting museums » / « wanted to spend more time » n'est pas déductible seul (le donjon tire la question isolément). Remplacement du prompt : « (Exam 2025 — reading, question 1)\nParagraph 3 ends: "She also enjoyed visiting different museums. Annie loved every moment of her trip and wished she could stay longer."\n\nAnnie's story has four events. Put them in the order in which they happen in the text. » (citation conforme au PDF ; b avant d se déduit : on gagne après avoir répondu.)

**M5. `01-pratique.json` #1 — renvoi à un dessin absent** (« at the bottom of the drawing », aucune figure). Prompt → « On a map, Tunisia is at the bottom and Italy is above it. Choose the correct sentence. » (options, clé, explication inchangées).

**M6. `05-entrainement.json` #2 — doublon de `quiz#2`** (Japon → bow, mêmes quatre gestes, même clé ; non levé par la tranche). Remplacement (clé 26 car. = option a 26 car.) :
- prompt : « A traveller arrives in New Zealand and visits a Maori family for the first time. How do they greet him? »
- options : a `They shake hands with him.` · b `They kiss him on each cheek.` · c `They bow to him.` · d `They touch noses with him.` (clé) ; `correctOption: "d"`
- explication : « A good traveller meets the greeting of the country he is in, and the Maori of New Zealand greet each other by touching noses and foreheads gently. Shaking hands belongs to England and the USA, the kiss on each cheek to Tunisia, France and Spain, and the bow to Japan. »

**M7. Rendu de la section « Let's pronounce » en Chromium (360 px).** Rendu par `renderLesson` (vitest jetable, supprimé) puis Chromium 1194 à 360 et 800 px : pas de débordement horizontal (tables 289/289 px), mais à 360 px la colonne « Sound » se coupe en « So / un / d » et **« /ai/ » se coupe en « /ai » + « / »** (le symbole phonétique est brisé) ; de plus le bloc commence par « **1 · …** », que le moteur ne met pas en `<p>` : l'étiquette s'affiche collée « PROPERTY1 · The s of the plural ». Remplacement VÉRIFIÉ (rendu Chromium 360 px : 2 colonnes lisibles, symboles entiers, étiquette séparée) — dans le bloc `::: propriete`, remplacer les deux paragraphes « **1 · The s of the plural** … » et « **2 · The y at the end of a word** … » et leurs tableaux par :

```
The first letter: the **s** of the plural says **/s/** or **/z/**, and the sound just before it decides.

| **/s/** — after a quiet sound: p, t, k | **/z/** — after a sound that shakes the throat, or a vowel |
| -------------------------------------- | ---------------------------------------------------------- |
| books · cats · cups · students         | cars · bags · stars · friends · greetings                  |

The test is the same as in Unit I: put your hand on your throat — with **/z/** it shakes, with **/s/** it stays quiet.

The second letter: the **y** at the end of a word says **/i/** or **/ai/**, and the length of the word decides.

| **/i/** — a long word (two syllables or more)                         | **/ai/** — a short word (one syllable)                          |
| --------------------------------------------------------------------- | --------------------------------------------------------------- |
| study · sunny · funny · puppy · cloudy · country · family · many · very | try · fly · my · sky · why — and **July**, the one long word that joins them |
```

(La phrase « Your teacher's book writes these two sounds… » reste après.) Contenu de la section par ailleurs juste : exemples (pigs /z/, ducks /s/, silly /i/, by /ai/) et `verifie` (bags ; my) re-résolus ; patron complet (ancrage, propriété, exemple, vérifie, retenir) ; puce du résumé fidèle.

**M8 (hors lot, préexistant — à signaler au pilote).** `cours.md`, section a/an/the, `::: verifie` : « …and ___ festival began at midnight » → la réponse impose *the* au motif que le festival est « already known », alors qu'il est mentionné pour la première fois (*a festival* est aussi juste). Remplacement : énoncé « Complete: "In Rome I saw ___ old bridge and ___ fountain. ___ fountain was full of coins." » ; réponse « _In Rome I saw **an** old bridge and **a** fountain. **The** fountain was full of coins._ — _old_ begins with the vowel o, so it takes **an**; _fountain_ begins with a consonant and is new for the listener, so it takes **a**; the second time the fountain is already known, so it takes **the**. » (aucun recouvrement avec 02#5 ni m019#3).

### Mineurs

- **m1. `06` #1** : la citation ne contient pas *different*, que l'explication dit « from the same paragraph ». Citation → « Paragraph 1 says: "Annie's favourite hobby is reading, especially about the history of countries. She spends hours in the school library discovering different cultures." » (conforme au PDF).
- **m2. `02-boss.json` #4 b** « We travelled by Italy to boat. » : deux erreurs (by et to permutés) → l'option doit rester muette (plan 2×2) : retirer le `misconceptionTag`.
- **m3. `03-revision.json` #3 d** « wearing a blazer to go to school … not the custom of any country » : faux pour les écoles anglaises. d → `wearing a coat when it is cold` ; fin d'explication → « …and wearing a coat when it is cold is what people do everywhere, not the custom of one country. » (clé 31 car., a 41 car.)
- **m4. `03-revision.json` #6** : « Spain is the country in the south-west of Europe » se défend à la lecture. Prompt → « Complete: "Last summer I visited ___ country in Europe: Spain." » ; explication → « Spain is one country among the many countries of Europe, and the word country begins with the consonant c, so the little word is a. The form an waits for a vowel, the would point at the only country of Europe, and of does not stand in front of a noun like this one. »
- **m5. `07` m019 #4** (`short_answer` north) : `expectedMistakes` south / east / west étiquetées `directions-confondues` — l'anagramme les exclut, l'élève qui les tape n'a pas confondu deux directions de la carte (aucune carte donnée). Retirer le bloc `expectedMistakes` (ou le garder sans étiquette si le schéma le permet).
- **m6. Taux d'étiquetage** : existants 55/105 = 52 % (après m2 : 54/105), sous l'objectif de 60 % ; justification de l'auteur acceptée (E7 : pas d'étiquette forcée). Deux étiquettes EXACTES du registre restent possibles hors de la liste de la carte : `01-pratique` #6 b « Let's to travel to Italy. » → `english.modal.to-en-trop` ; `02-boss` #6 b « easyer than » → `english.spell.suffixe-sans-regle-orthographique` (→ 56/105 = 53 %). À trancher par le pilote.
- **m7. Diff gonflé** : dans `quiz.json` et `05-entrainement.json`, des options `{ "id", "text" }` sur une ligne ont été éclatées sur quatre (contraire à la consigne « ne changer que les misconceptionTag ») ; sans effet sur le contenu.
- **m8 (hors lot)** : `cours.md`, comparatif : « Three spellings to watch » devant un tableau de quatre lignes.

## 3. Doutes de l'auteur — tranchés

1. **`a-an-selon-la-lettre` sur « a egg » / « an cape »** : le plan d'options est bon (une erreur = étiquette, deux erreurs = muette), mais le **libellé** ne dit pas l'erreur → M1 (réécrire le libellé, garder l'id et les étiquettes).
2. **`directions-confondues`** : juste sur quiz#1, 01#1, 03#1 (E/N/S), 04#6 (north pour south), m021#2 (2×2 correct, « top right » muette). Retrait seulement sur les `expectedMistakes` de m019#4 (m5).
3. **bow / touch / kiss pour « greet »** (`mot-voisin-du-meme-champ`) : **accepté** — mots du même champ, indice « in any country and in any way » dans l'énoncé (E7 respecté). *young* (m019#1, indice « houses ») accepté aussi.
4. **`fonction-mal-identifiee`** sur « Let's go swimming » / « How about a picnic » pris pour une formule d'adieu (m021#1) : **accepté** — une suggestion lue comme un adieu, c'est exactement le libellé.
5. **Options à deux erreurs muettes** (m019#3 d, m021#2 c) : conformes. Seule exception relevée : 02#4 b (m2).
6. **« key » en 09#3** : **rejeté** → M2 (la règle du cours en fait une seconde réponse).
7. **Règle du y final** (long → /i/, court → /ai/, July exception du guide) : acceptable à 11–12 ans ; aucune question ne pose d'autre exception une fois M2 corrigé.
8. **m019 réduite à 5 questions** : **accepté** — la carte liste cinq items, un sixième aurait fui vers le `short_answer` ou l'`ordering` ; titre « 2013–2025 » correct (sessions réellement fusionnées).

Autres contrôles sans défaut : âge et vocabulaire (Leila, Omar, port, château, carte au trésor) adaptés ; aucune notion hors guide en cible ; étiquettes `english.read.*` de m018 conformes à leurs libellés ; aucune étiquette sur `multi` / `ordering` / `matching` ; `coursePitfalls` (7) tous enseignés par une section `::: piege` et portés par au moins un distracteur ; ligne `sources[]` (guide 541608, fiche, sujets officiels, devoirs « aucune reprise ») présente ; étages et récompenses conformes (m018/m019/m021 d2 75/15, 09 d1 50/10) ; gabarit « three of these… » levé.

## 4. Résumé

55 questions re-résolues : **0 clé fausse**, **2 critiques** (04#3 et 05#1 : deux réponses défendables), **8 majeurs** (libellé a/an qui ne dit pas l'erreur, « key » en 09#3, deux défauts de m018 — clé livrée par la citation et ordering sans données —, dessin absent en 01#1, doublon 05#2 / quiz#2, tableaux de prononciation brisés à 360 px, plus un `verifie` faux hors lot), **8 mineurs**. Salle blanche m021 propre (outil + comparaison à la main avec D07 et D08). Étiquetage des existants à 52 % (justifié). Chaque texte de remplacement a été vérifié : longueur de la clé, une seule réponse, aucune fuite, et rendu Chromium pour M7.

**Verdict : à corriger avant armement** (C1, C2, M1–M7). Après correction, une relecture ciblée de ces items suffit.
