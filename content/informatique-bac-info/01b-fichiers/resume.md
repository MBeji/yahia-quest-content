# 📜 Résumé : Les fichiers

- **Notion de fichier** : un fichier est un ensemble de données de même type, nommé et enregistré sur un support ; ses éléments sont numérotés à partir de 0 et le pointeur est le numéro du prochain élément lu ou écrit ; un fichier de 5 éléments a les numéros 0 à 4.
- **Accès séquentiel ou direct** : en séquentiel on lit tout ce qui précède l'élément voulu, en direct on donne son numéro d'ordre ; le choix revient au programme, pas au fichier ; pour traiter tous les éléments, le séquentiel suffit.
- **Déclaration et association** : `Fichier de` (Pascal `File Of`) suivi du type des composants, tous de même type (un enregistrement pour mêler plusieurs types) ; Associer (`Assign`) relie le nom logique du programme au nom physique du disque, sans ouvrir ni créer.
- **Ouvrir, écrire, lire, fermer** : Recréer (`Rewrite`) crée ou efface, Ouvrir (`Reset`) rouvre un fichier existant et remet le pointeur à 0 ; Ecrire (`Write`) et Lire (`Read`) avancent le pointeur d'une position ; on ferme avec Fermer (`Close`).
- **Parcours séquentiel** : `Tant que Non Fin_fichier (f)` avec le test avant la lecture, ce qui couvre le fichier vide ; `{$I-}`, `Reset` et `IOResult <> 0` permettent de créer le fichier s'il n'existe pas.
- **Accès direct** : Pointer (`Seek`) place le pointeur sur un numéro, Taille_fichier (`FileSize`) donne le nombre d'éléments, Position_fichier (`FilePos`) le numéro pointé ; un numéro est valide si (num ≥ 0) ET (num < taille) ; on ajoute en pointant la taille.
- **Gérer le fichier** : Effacer (`Erase`) supprime, Renommer (`Rename`) change le nom physique d'un fichier fermé, Tronquer (`Truncate`) ne garde que les éléments situés avant le pointeur.
- **Fichiers texte** : déclarés par `Text`, faits de lignes lues par Lire_nl (`ReadLn`) et écrites par Ecrire_nl (`WriteLn`) ; Ajouter (`Append`) écrit à la suite sans effacer ; Fin_ligne ne teste que la ligne courante, et Position_fichier ne s'applique pas à un fichier texte.
