1. [MAJOR] content/CATALOGUE.md — l.73, ligne svt-3eme-sec-sciences-exp (constat 16, écarté par le correcteur)
   Problème : Le catalogue reste périmé : il affiche 4 chapitres et 16 exercices, alors que content:check en compte 8 et 32. Si la PR part sans régénération, le contrôle git diff de content-ci échouera. Le report est voulu, car les autres chapitres sont encore en correction, mais la tâche reste à faire.
   Correction : Quand les correcteurs des chapitres 05 à 08 auront fini, lancer une seule fois `npm run content:catalogue` depuis /home/user/engine. Committer CATALOGUE.md dans la même PR que PILOTAGE.md.

2. [MINOR] content/svt-3eme-sec-sciences-exp/07-milieu-interieur/cours.md — l.43, phrase de liaison de la figure 1 (accolades l.38)
   Problème : Le constat 2 n'est que partiellement clos. La phrase dit que le contenu des cellules n'est souligné par aucune accolade. Or l'accolade du liquide interstitiel (de x=118 à x=214) couvre en largeur les deux cellules dessinées (de x=111 à x=214). Le texte décrit donc encore le schéma de façon inexacte, sur le point précis de la conception erronée n°1.
   Correction : Faire porter la phrase sur les étiquettes : « chaque accolade souligne le nom d'un des trois liquides, et un trait les réunit sous milieu intérieur ; le liquide contenu dans les cellules jaunes n'a pas d'étiquette, il n'en fait pas partie ». On peut aussi raccourcir cette accolade sous la seule étiquette, ou marquer une cellule « hors milieu intérieur ».

3. [MINOR] content/svt-3eme-sec-sciences-exp/07-milieu-interieur/exercices/03-revision.json — q6, explanation
   Problème : La phrase réécrite au titre du constat 8 est agrammaticale : « le diabète relève du glucose et le rachitisme la calcification des os ». Le verbe sous-entendu (relève de) ne peut pas régir « la calcification » sans préposition.
   Correction : Écrire : « le diabète relève du glucose et le rachitisme concerne la calcification des os, sans lien avec l'hémoglobine ».

4. [MINOR] content/svt-3eme-sec-sciences-exp/07-milieu-interieur/exercices/04-defi.json — q1, option c
   Problème : La question a été réécrite pour le constat 4, mais un autre distracteur garde le même défaut d'indice de forme (form clue n°3). L'option c dit : « Les valeurs ne sont pas des constantes : elles varient librement ». Or l'énoncé affirme que les constantes restent dans leurs limites, donc la seule lecture de l'énoncé élimine cette option.
   Correction : La remplacer par un distracteur compatible avec l'énoncé et porteur du tag constante-valeur-fixe, par exemple : « Les constantes ont une valeur fixe, que les déchets ne peuvent pas modifier ».

