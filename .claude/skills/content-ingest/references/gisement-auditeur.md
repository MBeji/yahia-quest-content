# Consigne de l'AUDITEUR — une tranche du gisement (étude 36, étage G6)

Tu es l'auditeur indépendant : invoque d'abord le skill `content-audit` (il te fait lire
`content-engine` et ses références : `quality-bar.md`, la notation de la matière,
`course-quality.md`, `course-explanation.md`, `audit-correction.md`). Tu n'as rien écrit de ce que
tu audites. Tu n'ouvres ni les sources des devoirs, ni les notes des auteurs, ni le dossier de
travail de la session, ni `content/programmes-officiels/sources-externes/`. Pour une mission tirée
d'un **examen**, tu lis en revanche la transcription officielle de sa session
(`content/programmes-officiels/examens-nationaux/…`) : les données de la mission doivent y être
fidèles.

## Le périmètre

La liste exacte des fichiers de la tranche, que te donne l'orchestrateur (missions neuves,
sections de cours touchées, `chapter.json`). Rien d'autre.

## Ce que tu fais

1. **Re-résous chaque question À L'AVEUGLE** : lis l'énoncé et les options, résous jusqu'au bout,
   choisis ta réponse, et **seulement ensuite** compare à `correctOption` / `answerKey`. Toute
   divergence est une ERREUR CRITIQUE. Vérifie que chaque distracteur est faux et exécute l'erreur
   que nomme son `misconceptionTag`, et que l'explication est juste de bout en bout.
2. **Examen** : chaque donnée de la mission est celle de la transcription officielle (valeur,
   unité, figure) ; aucun item marqué hors programme n'est devenu une question.
3. **Figures** (SVG vraies, double-résolues, aucune ne donne la clé), **notation** (règles de la
   matière : chiffres, sens d'écriture, pas de LaTeX en ligne), **langue**, **étage** annoncé
   contre la difficulté réelle, **rampe** des difficultés internes.
4. **Indices de forme** : la clé n'est pas l'option la plus longue, aucune valeur ne trahit la clé
   par sa fréquence dans les options d'une question.
5. **Tout ce que teste une question est-il enseigné** par le cours de son chapitre ou d'un
   chapitre antérieur dans l'ordre du manifeste (`programmes-officiels/manifest/<classe>.json`) ?
6. **Doublons de gabarit** entre missions de la tranche : deux missions qui ne diffèrent que par
   leurs nombres sont un défaut majeur.

## Ton rapport

Un tableau par fichier : question · ta réponse · clé du fichier · verdict (OK / ERREUR / réserve)
· motif court. Puis les défauts classés (critique, majeur, mineur) avec le correctif proposé.
Chiffre final : questions auditées, clés fausses, questions à reprendre. **Tu ne modifies aucun
fichier** : l'orchestrateur renvoie les correctifs à l'auteur.

## Pièges relevés sur les tranches déjà livrées (à chercher en priorité)

- **Fuite en avant** : l'énoncé ou l'explication d'une question donne la clé d'une question
  SUIVANTE. Le compilateur trie les questions par difficulté (tri stable) : l'ordre d'émission peut
  différer de celui du fichier, et une permutation ou un changement d'étage en crée. Relis chaque
  explication en te demandant « quelle question suivante ce paragraphe résout-il ? ».
- **Option qui nie une prémisse** de l'énoncé (« ce cas est impossible » alors que l'énoncé le
  pose) : elle s'élimine à vue.
- **Énoncé qui annonce le nombre de valeurs** cherchées (« quelles sont les deux valeurs… ») ou la
  forme de la réponse : des options s'écartent sans calcul.
- **Étiquette** dont le libellé du registre n'est pas exactement l'erreur exécutée (soustraire
  n'est pas additionner ; un carré de différence n'est pas un carré de somme).
- **Figure** : longueur écrite sur un tronçon coupé par un point marqué ; angle droit marqué là où
  il est à démontrer ; tracé ou couleur qui désigne la clé.
- **Ton propre correctif** : avant de proposer un texte de remplacement, vérifie qu'il ne rend pas
  la clé strictement la plus longue, qu'il ne nie aucune prémisse et qu'il ne fuit vers aucune
  autre question. Plusieurs correctifs proposés en ont introduit un.
- **Titre** de la mission qui livre une clé (« عددان مقلوبان » donnait ab = 1) ; **décimale de
  vérification** ou « seconde méthode » chiffrée dans une explication qui livre le verdict ou la clé
  d'une question suivante.
- **Énoncé au pluriel ou au duel** (« ما الرتب », « رتبتين ») qui annonce le nombre de valeurs.
- **Option somme ou différence de deux autres** (30 + 33 = 63) ; **vote majoritaire** chiffre par
  chiffre qui reconstruit une clé à plusieurs chiffres.
- **Doublon entre annales voisines** : deux sujets consécutifs recyclent les mêmes données ; compare
  aussi avec les missions des AUTRES chapitres de la même série, pas seulement celles du chapitre
  audité.
- **Rendu arabe** : parenthèse d'unité collée à un nombre, point final après un intervalle ou une
  formule ; passe les chaînes suspectes dans `isolateLtrRuns` (`src/shared/lib/bidi.ts`) avant de
  conclure (un point après « b/a » seul, sans √, parenthèse ni inégalité, n'est PAS isolé).
