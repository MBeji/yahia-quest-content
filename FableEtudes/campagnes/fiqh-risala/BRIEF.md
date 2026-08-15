# BRIEF — chapitres de la sous-rubrique فقه (matière `fiqh`)

Tu écris **un chapitre complet** de la matière `fiqh` pour l'académie **Na9ra Nal3ab**.
La matière suit **الرسالة d'ابن أبي زيد القيرواني** (m. 386 h.), le précis de fiqh malikite
écrit à Kairouan. Un باب du livre = un chapitre de l'app.

## 0. À lire AVANT d'écrire (dans cet ordre, non négociable)

1. `D:/11-coding/YahiaAcademy/yahia-quest-content/.claude/skills/content-engine/SKILL.md`
   et ses références, en particulier :
   - `references/content-schema.md` (forme exacte des fichiers)
   - `references/quality-bar.md` et `references/expert-exercises.md` (barre de qualité)
   - `references/course-quality.md` (structure d'un cours)
   - `references/rewards-and-modes.md` (échelle des missions)
   - `references/style-guide.md`
2. **Le chapitre modèle** — même langue, même domaine, même maison :
   `D:/11-coding/YahiaAcademy/yahia-quest-content/content/education-islamique-5eme/05-al-wudoo/`
   (lis `chapter.json`, `cours.md`, `resume.md`, `quiz.json` et les 5 `exercices/*.json`).
   Ton livrable doit avoir **la même forme et le même niveau de finition**.
3. **Ta source** : le fichier de matn qu'on te donne. C'est le texte d'Ibn Abî Zayd,
   domaine public, extrait de shamela.ws/book/11373.

## 1. La règle qui prime sur tout : tu écris SUR le matn

- Tout ce que tu affirmes doit être **dans le matn de ton باب**. Tu ne complètes pas de
  mémoire, tu n'importes pas d'un autre madhhab, tu n'ajoutes pas de règle absente.
- Quand le matn est bref ou silencieux sur un point, **tu le dis** (« لم يفصّل المؤلّف هنا »)
  au lieu de combler.
- Le matn est écrit **sans ponctuation ni découpage** : ton travail est de le **découper,
  ordonner et expliquer**, pas de le réécrire.
- **« … » est RÉSERVÉ au matn.** Les guillemets français ne servent à rien d'autre : ni à un
  locuteur fictif (« يقول التلميذ: … »), ni à une paraphrase, ni à une formule de ton cru.
  Sinon le contrôle de fidélité mesure autre chose que ce qu'on croit, et l'élève ne sait plus
  ce qui vient du livre. Pour ta propre voix : pas de guillemets.
- Tu **cites** le matn (phrases courtes, entre guillemets « … ») puis tu expliques en
  langue d'aujourd'hui. Le lecteur doit toujours voir ce que dit l'auteur ET ce que ça veut dire.
- ⚠️ Si un verset coranique apparaît : **رواية قالون عن نافع** (مصحف الجمهورية التونسية),
  copié caractère par caractère depuis le matn — **jamais de mémoire** (la mémoire produit
  حفص par défaut, ce serait une faute).

## 2. Public visé — « tous publics 10+ »

- Arabe standard **simple et clair**, phrases courtes, pas de jargon non expliqué.
- Chaque terme technique (فرض، سنّة، مستحبّ، مكروه، نافلة، إقامة…) est **introduit puis
  défini la première fois**, en une ligne.
- Vocalisation (الشكل) : **sur les termes techniques et les mots ambigus uniquement**,
  pas sur tout le texte.
- Ni infantilisant, ni savant : un élève de 10 ans doit suivre, un adulte ne doit pas s'ennuyer.
- Des exemples concrets de la vie d'aujourd'hui (l'école, la maison, le voyage, le ramadan).

## 3. Chapitres à sujet adulte (on te dira si le tien en fait partie)

Certains أبواب relèvent du droit adulte : mariage/divorce, `العدّة`, peines (`الحدود`),
`الجهاد`, l'affranchissement et le statut servile, les successions.
Pour ceux-là, **traitement sobre et général** :

- tu expliques **de quoi le باب traite et quels principes il pose** (la justice, le droit des
  personnes, la preuve, la responsabilité, la protection des faibles, le partage équitable) ;
- **aucun détail procédural** sur les peines corporelles, aucun détail intime, aucun cas cru ;
- les institutions historiques (l'esclavage, la capture) sont présentées **au passé et dans
  leur contexte historique**, jamais comme un modèle de vie actuel ;
- les questions portent sur le **vocabulaire, les principes et la logique juridique**,
  jamais sur l'application d'une peine ni sur l'intime ;
- ton neutre, factuel, éducatif — c'est de l'histoire du droit musulman.

## 4. Les fichiers à produire

Dans `D:/11-coding/YahiaAcademy/yahia-quest-content/content/fiqh/<DIR>/` :

```
chapter.json
cours.md
resume.md
quiz.json
exercices/01-pratique.json
exercices/02-boss.json
exercices/03-revision.json
exercices/04-defi.json
exercices/05-tathbit.json
```

### chapter.json

```json
{
  "title": "<titre court en arabe, PAS le titre long du باب>",
  "description": "<2–4 lignes en arabe : ce que l'élève va apprendre, concret>",
  "displayOrder": <numéro du باب>,
  "sources": [
    "الرسالة لابن أبي زيد القيرواني (ت 386 هـ) — <titre du باب> — https://shamela.ws/book/11373 — الصفحات <pages>"
  ]
}
```

N'ajoute **ni** `manuel`, **ni** `videos`, **ni** `gradeSlugs`.

### cours.md

Le cours complet, en markdown. **Sa longueur suit celle du باب, pas une cible fixe** :
~6 000–10 000 caractères pour un باب de 2–3 pages, jusqu'à ~14 000 pour un باب de 5 pages
ou plus. (Mesuré sur les 24 premiers chapitres : la cible unique de 10 000 était fausse —
les longs أبواب la dépassaient tous, et la tenir aurait coûté des citations ou un tableau.)
Au-delà de 14 000, c'est possible mais tu le **justifies** dans ton rapport : dis quel
matériau tu as refusé de couper et pourquoi. Structure attendue
(inspire-toi du modèle, adapte les titres au sujet) :

- un titre `#` et une accroche d'une ou deux phrases (pourquoi ce باب) ;
- `## نصّ الباب` : le matn **découpé en segments courts** cités entre « … », dans l'ordre
  du livre — c'est la colonne vertébrale du chapitre ;
- après chaque segment, `### الشرح` ou un paragraphe d'explication simple ;
- des **tableaux markdown** pour tout ce qui s'énumère (فرائض / سنن / مستحبّات / مكروهات /
  نواقض, les cas, les délais…) — c'est ce qui rend le cours mémorisable ;
- des exemples concrets ;
- une section finale `## خلاصة` en quelques puces.

Markdown standard uniquement (titres, listes, tableaux, gras, citations `>`), pas de HTML.

### resume.md

~2 000–3 500 caractères : la fiche de révision. Les définitions, les listes essentielles
(en tableau), les pièges. Il doit se suffire à lui-même pour réviser avant un contrôle.

### quiz.json

```json
{ "title": "⭐ فهم: <sujet>", "questions": [ … 5 questions … ] }
```

5 questions de compréhension, difficulté 1–2, sur les idées **centrales** du chapitre.

### Les 5 missions (`exercices/`)

| fichier         | mode        | difficulty | xpReward | rewardCoins | displayOrder | rôle                       |
| --------------- | ----------- | ---------- | -------- | ----------- | ------------ | -------------------------- |
| `01-pratique`   | `practice`  | 1          | 50       | 10          | 1            | application directe        |
| `02-boss`       | `boss`      | 3          | 120      | 30          | 2            | boss du chapitre           |
| `03-revision`   | `practice`  | 2          | 70       | 15          | 3            | révision                   |
| `04-defi`       | `challenge` | 4          | 300      | 60          | 4            | défi élite                 |
| `05-tathbit`    | `boss`      | 3          | 120      | 30          | 5            | second boss, consolidation |

- **6 questions par mission**, **4 options** chacune.
- Titre de chaque mission : les ⭐ + un libellé arabe, ex.
  `"⭐ تمرين: ..."` (1) · `"⭐⭐⭐ الزعيم: ..."` (3) · `"⭐⭐ مراجعة: ..."` (2) ·
  `"⭐⭐⭐⭐ تحدّي النخبة: ..."` (4) · `"⭐⭐⭐ تثبيت: ..."` (5).
- Aucune question répétée d'un fichier à l'autre : **30 questions distinctes** par chapitre,
  plus les 5 du quiz.

## 5. Règles d'écriture des questions — les pièges qui font échouer

1. **`difficulty` d'une QUESTION ne dépasse jamais 3** (1, 2 ou 3), même dans `04-defi`
   (c'est l'exercice qui est en 4, pas ses questions). Ordre croissant dans le fichier.
2. **Ne jamais désigner une option par sa lettre.** Les options sont mélangées à l'affichage :
   « الجواب هو ب » ne veut rien dire. L'explication **redit le contenu** de la bonne réponse.
3. **La bonne réponse ne doit pas être la plus longue.** Écris les 4 options à des longueurs
   comparables ; sinon la clé se devine sans lire. Vérifie-le fichier par fichier.
4. **L'énoncé ne contient jamais la réponse** (ni un synonyme évident).
5. **Les distracteurs sont plausibles** : des confusions réelles (confondre فرض et سنّة,
   confondre deux délais, inverser deux étapes) — jamais du remplissage absurde.
6. **`explanation` obligatoire sur chaque question** : 1–3 phrases qui expliquent *pourquoi*,
   en s'appuyant sur le matn (cite le bout de phrase concerné). Ce n'est pas une paraphrase
   de l'option.
7. **N'utilise ni `misconceptionTag` ni `competencies` ni `acceptedAnswers`** : les registres
   ne couvrent pas cette matière, un tag inconnu fait échouer le gate.
8. **Aucun Markdown dans les champs d'une question.** `prompt`, `explanation` et le `text`
   d'une option sont rendus par `RichField` en **nœud de texte brut** : un double-astérisque
   arrive à l'élève **avec ses astérisques**. Le Markdown ne vaut que pour `cours.md` et
   `resume.md`. (Piège n°6 du pipeline — 22 champs à nettoyer sur la première vague.)
9. Type : `mcq` uniquement (n'écris pas de champ `type`, c'est le défaut). `options` : ids
   `"a"`, `"b"`, `"c"`, `"d"` ; `correctOption` pointe l'un d'eux. **Varie la position de la
   bonne réponse** d'une question à l'autre.
10. Les nombres restent en chiffres standards (٥ → 5).
11. Pas de contenu polémique, pas de takfīr, pas d'attaque d'un autre madhhab. On enseigne
    le malikite **tel que le livre l'expose**, sereinement.

## 6. Avant de rendre

- Relis tes 35 questions : une clé fausse est le pire défaut possible ici. Chaque clé doit
  être **justifiable par une phrase du matn** que tu peux citer.
- Vérifie que le JSON est valide (pas de virgule finale) et que les 9 fichiers existent.
- **N'exécute aucune commande git.** Tu écris des fichiers, c'est tout.

## 7. Ce que tu renvoies

Un rapport court (10 lignes max) : le chapitre traité, le nombre de questions, les points
où le matn était ambigu et ce que tu as décidé, et tout ce dont tu n'es pas sûr.
Ton texte final est un rapport machine, pas un message à un humain.
