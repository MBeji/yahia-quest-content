<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source : manuel élève officiel CNP « Algorithmique et programmation », 4ème année de
     l'enseignement secondaire, Sciences de l'informatique (248 p. ; auteurs A. Abidi, N. Agrebi
     Dekhil, N. Zouari ; évaluateurs H. Smei, R. Douari). Aucun guide enseignant au corpus ⇒ le
     manuel élève fait référence. ⚠️ Fichier déposé par Mohamed le 2026-11-07 sous le nom
     `4sci_AP.pdf` (dossier Drive « Enregistré depuis Chrome », hors `cnp-officiel`) : son code CNP
     n'est pas imprimé dans le PDF [?] ; la source est déclarée en `sourcesLibres` du registre (aucun code inventé).
     Lu le 2026-11-07 : couche texte (L1, `pdftotext -layout` page par page) puis sondage image par
     quatre lecteurs indépendants (opus) ; PDF = page imprimée (offset 0).
     Statut : relecture R-7 faite le 2026-11-07 (voir §6 et le registre). -->

# Informatique (algorithmique et programmation) — Bac Sciences de l'informatique (`bac-info`) · manuel officiel CNP

> **Source** : manuel élève « Algorithmique et programmation », 4ème année secondaire, section
> Sciences de l'informatique — `4sci_AP.pdf`, 248 p. (p.1 titre, p.2-6 préface/légende/sommaire,
> p.7-245 les 7 chapitres, p.246-247 bibliographie/webographie). **Langue** : fr.
> **subject id** : `informatique-bac-info` · **gradeSlug** : `bac-info`. **Langage de programmation** : Pascal
> (Turbo Pascal) ; pseudo-langage algorithmique du programme tunisien (TDO/TDNT, Début/Fin, Tant que…).
> **Notation** : chiffres occidentaux ; la couche texte aplatit exposants, indices, ≤/≥, π et fractions :
> ces éléments viennent de l'image de la page.

## 1. Cadre & compétences

Préface (p.2) : la matière « repose essentiellement sur l'algorithmique et la résolution de problèmes »
et exige deux qualités, l'**intuition** et la **rigueur** (« se mettre mentalement à la place de la machine »).
Le manuel, « conforme aux nouveaux programmes », vise à : apprendre à résoudre des problèmes et à écrire
des algorithmes ; acquérir les algorithmes courants (récurrence, arithmétique, approximation, tris…) ;
Pascal. Il prolonge le manuel de 3ème année de la même section (non au corpus) : enregistrements et
fichiers (ch.1) sont « deux nouvelles structures de données » absentes de la 3ème année. Chaque chapitre :
objectifs, plan, activités préliminaires, étude de la notion (syntaxe algorithmique **et** Pascal),
applications résolues, série d'exercices, partie « Lecture » (culture informatique).

**Légende des pictogrammes (p.5, vérifiée sur l'image)** : remarque importante (panneau stop) ; idée
(bougie, = « Une idée ») ; solution d'une application/activité (clé) ; série d'exercices non corrigés ; lecture ;
points à retenir ; **quatre silhouettes de difficulté : simple, moyen, assez élevé, élevé**.
Rattachement aux exercices : **fiable et vérifié sur l'image pour les ch.1 à 3** (p.68-71, 90-92, 119-121) ;
`[?]` **non relevé pour les ch.4 à 7** (les lecteurs y notent des icônes sans leur niveau) : ne pas calibrer la
difficulté de ces chapitres sur les silhouettes.

## 2. Plan annuel (sommaire p.5-6)

| Ch. | Titre du manuel | Pages |
| --- | --- | --- |
| 1 | Les enregistrements et les fichiers | 7-72 |
| 2 | La récursivité | 73-94 |
| 3 | Les algorithmes de tri | 95-122 |
| 4 | Les algorithmes récurrents | 123-150 |
| 5 | Les algorithmes d'arithmétique | 151-186 |
| 6 | Les algorithmes d'approximation | 187-212 |
| 7 | Les algorithmes avancés | 213-245 |

## 3. Notes pédagogiques / méthode

- **Erreurs du manuel — à ne jamais reprendre dans une question, un corrigé ou un cours** (relevées par
  les lecteurs, détail `[sic]` dans chaque section) : ch.1 p.58 condition `OU` au lieu de `ET`, p.52
  Création ouvre avec Ouvrir au lieu de Recréer ; ch.2-3 coquille `Enreg1.Moy > Enreg1.Moy` (classement),
  `Rechercher_Rang` ne compare rien, `Tri_Sel_Rec` non défini pour n = 1 ; ch.6 `Epsilon = 10E-4` vaut 10⁻³
  (le tableau annonce 10⁻⁴), « point gauche » du Retenons contre point milieu codé, formule de Wallis
  écrite avec des « + », série du sinus de l'exercice Bac 2001 sans signes alternés ; ch.7 **l'algorithme du
  tri rapide p.220 est faux** (tester le principe et la première partition p.215-216, jamais ce code ni la suite de la trace p.217) et le voyageur de
  commerce compare depuis le rang de l'étape au lieu de la ville courante.
- **Absents du manuel** (⛔ à ne pas introduire) : balayage et méthode de Newton (le ch.6 est le point fixe, π, e,
  aires), crible, PGCD d'Euclide (le PGCD est la seule méthode par différences). **Présents seulement en partie** :
  la dichotomie est une méthode de *recherche* (ch.2 App.4 p.86-88, ch.3 p.98), jamais une méthode d'approximation ;
  le PPCM et la décomposition en facteurs premiers ne sont que des exercices non corrigés (ch.2 Ex.9-10 p.92) ;
  tri par sélection et à bulles : pas de Pascal itératif dans le cours (Pascal *récursif* de la sélection au ch.2
  p.85 ; algorithmes `pos_min` et `TRI_Bulles` dans les Ex.1-2 p.119). « Calcul de PGCD et PPCM » n'est cité qu'au préambule
  p.152 du ch.5, sans algorithme du PPCM.
- Plusieurs exercices sont des sujets de baccalauréat pratique/théorique (Bac TP 2001, 2004, 2005 ; Bac 1992,
  1995) : repris fidèlement ou adaptés, avec la source citée.

## 4. Transcription par chapitre

### Chapitre 1 — Les enregistrements et les fichiers (p.7–72)

Source : manuel élève CNP « Algorithmique et programmation », 4ème année secondaire, Sciences de l'informatique (PDF local, décalage 0 : page PDF = page imprimée). Aucun guide enseignant.

#### Plan du chapitre (avec pages)

- p.7 — page d'ouverture : objectifs + plan.
- **A. Les enregistrements** (p.8–31)
  - I. Introduction — Activité 1 (p.8–9)
  - II. Définition et déclaration — Activités 2, 3 (p.10–13)
  - III. Utilisation des enregistrements (p.13–31)
    - III.1 Affectation — Activité 4 (p.13–16)
    - III.2 Lecture — Activité 5 (p.16–17)
    - III.3 Ecriture — Activité 6 (p.17–18)
    - III.4 Structure Avec .. Faire — Activités 7, 8 (p.18–22)
    - III.5 Vecteur d'enregistrements — Activités 9, 10, 11 (p.23–31)
- **B. Les fichiers** (p.32–65)
  - I. Introduction + définition (p.32)
  - II. Organisation des fichiers (pointeur, organisation séquentielle / relative) (p.32–33)
  - III. Types d'accès — Activités 1, 2, 3 (p.34–36)
  - IV. Les fichiers à accès séquentiel (p.36–54)
    - IV.1 Présentation, déclaration — Activités 4, 5 (p.36–39)
    - IV.2 Traitement sur les fichiers : étape 1 Association (p.39–40, Act. 6) ; étape 2 Ouverture (p.41–42, Act. 7, 8) ; étape 3 Ecriture (p.42–43, Act. 9, 10) ; étape 4 Lecture (p.44–45, Act. 11, 12) ; étape 5 Fermeture (p.45, Act. 13) ; étape intermédiaire Test de fin du fichier (p.46, Act. 14) ; encadré « Vérification des Entrées/Sorties en Pascal » (p.47) ; Activités 15 et 16 (programmes complets, p.47–54)
  - V. Les fichiers à accès direct (p.54–58)
    - V.1 Définition (Pointer/Seek, Taille_fichier/FileSize) — Activité 17 (p.54–55)
    - V.2 Autres fonctions et procédures prédéfinies (Position_fichier, Effacer, Renommer, Tronquer) (p.56–57)
    - V.3 Application (procédure Lecture en accès direct) (p.57–58)
  - VI. Les fichiers texte (p.58–65)
    - VI.1 Définition ; VI.2 Présentation — Activité 18 (p.58–60)
    - VI.3 Procédures et fonctions prédéfinies (Fin_ligne, Ajouter, Lire_nl, Ecrire_nl) (p.60–61)
    - VI.4 Applications 1, 2, 3 (p.61–65)
- Retenons (p.66–67) ; Exercices 1 à 14 (p.68–71) ; Lecture « Notion de fichier » (p.72).

#### Objectifs officiels (p.7, verbatim)

- Définir la structure enregistrement
- Définir les fichiers et les modes d'accès
- Mettre à profit les structures enregistrement et fichiers pour résoudre des problèmes.

#### Pictogrammes (lecture image)

Légende p.5 (vérifiée sur l'image) : **P1 = simple, P2 = moyen, P3 = assez élevé, P4 = élevé**. Rattachement relevé sur les pages 68-71 :
- **P1** personnage « rayonnant » (traits autour de la tête) : activités d'introduction/application directe ; exercices 1, 2, 3, 7, 8.
- **P2** personnage pensif, main au menton, « ? » : B-Activité 15, Applications 1-2-3 ; exercices 4, 5, 9, 10, 11.
- **P3** personnage qui se gratte la tête, « ? » et notes : A-Activités 8 et 11, B-Activité 16 ; exercices 6, 12, 13.
- **P4** personnage qui s'arrache les cheveux : exercice 14 (seul).
- Autres pictos : panneau **STOP** = remarque à retenir ; **bougie** = « Une idée » (légende p.5 ; p.47 IOResult, p.55 FileSize pour ajout) ; **quatre personnages portant une clé** = solution d'une application ou d'une activité / réponse aux questions (légende p.5).

#### Activités, applications, exercices résolus

**A. Enregistrements**
- **A-Act.1 (p.8–9)** — Liste d'une classe (N°, Code, Nom & Prénom, Moyenne, Observations ; ex. « C0120 Cherni Selim 14.25 Néant », 30 lignes, max 40 élèves). Demande : structure de données et déclaration. Solution : 5 tableaux séparés (Num, Code, Nom, Moy, Obser), puis constat qu'un tableau ne peut regrouper des types différents ⇒ introduction de l'ENREGISTREMENT (ARTICLE, RECORD en Pascal).
- **A-Act.2 (p.11–12)** — Déclarer (algo + Pascal) un enregistrement `complexe` (p_réelle, p_imaginaire : Réel) et une variable z.
- **A-Act.3 (p.12–13)** — Enregistrement `date` : jj : 1..31 (intervalle), mm : mois (type énuméré des 12 mois), aa : Entier ; variable `calendrier`.
- **A-Act.4 (p.13–15)** — Fiche étudiant (nom, prénom : Chaîne ; sexe : Caractère ; date_nais : Chaîne ; moy : Réel) ; affecter "Kéfi", "Nour", "F", "27/11/1983", 13.25. Suivi de remarques (affectation globale, enregistrement imbriqué : date_nais devient un enregistrement Date jour/mois/année).
- **A-Act.5 (p.16–17)** — Saisir au clavier les champs d'Etudiant (analyse : `variable.champ = Donnée(...)`, algorithme, Pascal ReadLn).
- **A-Act.6 (p.17–18)** — Afficher les champs d'Etudiant.
- **A-Act.7 (p.18–19)** — Réécrire affectation/lecture/écriture avec Avec..Faire / With..Do.
- **A-Act.8 (p.19–22) [P3]** — Structure Personne (nom ≤ 30 car., numéro fiscal entier, téléphone ≤ 10 car., carte bancaire entier non signé). Programme modulaire `Fiche` : procédures Saisir (paramètre Var) et Afficher ; Pascal `Enreg_1` (String[30], Integer, String[10], Word). Remarque Uses Crt / Uses WinCrt.
- **A-Act.9 (p.23)** — Peut-on déclarer un tableau d'enregistrements ? Oui (éléments de même type).
- **A-Act.10 (p.23–24)** — N étudiants (4 ≤ N ≤ 30) : `Tab = Tableau de 30 Fiches`, Fiches avec champ Date_nais : Date.
- **A-Act.11 (p.24–31) [P3]** — Gestion d'employés (nom & prénom, grade G1..G4, code fiscal entier non signé, assurance maladie O/N), 4 ≤ N ≤ 120. Programme `GESTION` / `Enreg_2` : Saisie (contrôle N Dans [4..120], Avec T[i] Faire, Majuscule(am) Dans ["O","N"]), Affichage (une fiche par écran : ReadLn ; ClrScr), Lecture (grade valide), fonction Cherche (comptage des occurrences d'un grade), Result (pourcentage P = (Nb_G * 100) / N, affiché P:6:2). Types : Gr = String[2], Tab = Array[1..120] Of Fiche.

**B. Fichiers**
- **B-Act.1 (p.34–35)** — 4 disques empilés sur un support (image : rouge en bas, puis vert, bleu, jaune en haut) ; pour atteindre le vert il faut retirer jaune puis bleu ⇒ **accès séquentiel** ; STOP : « le premier entrant est le dernier sortant ».
- **B-Act.2 (p.35–36)** — 4 disques sur 4 supports distincts (image : jaune, bleu, rouge, vert) ; on prend directement le rouge ⇒ **accès direct (dit aussi accès aléatoire)**.
- **B-Act.3 (p.36)** — Analogie magnétophone (cassette = séquentiel) / CD Audio (direct) pour écouter la 4ème chanson.
- **B-Act.4 (p.37–38)** — Fichier de réels pour les notes : `notes_élève = Fichier de réels` / `File Of Real`.
- **B-Act.5 (p.38–39)** — Fichier CARNET de fiches (nom_prénom : Chaîne[30], sexe, date_naissance, note1..note3) : nécessité du type enregistrement ; `Carnet = Fichier de Fiche`, objets info (Fiche) et élève (Carnet).
- **B-Act.6 (p.40)** — Associer élève à "C:\Archive\Fichier_eleve.dat".
- **B-Act.7 (p.41)** — Recréer (élève) / ReWrite (eleve).
- **B-Act.8 (p.42)** — Ouvrir (élève) / ReSet (eleve).
- **B-Act.9 (p.42)** — Lire un entier N et l'écrire dans le fichier Valeurs.
- **B-Act.10 (p.43)** — Saisir un enregistrement fiche et l'écrire dans élève : 2 solutions (sans / avec Avec..Faire).
- **B-Act.11 (p.44)** — Lire l'entier V pointé dans Valeurs.
- **B-Act.12 (p.44–45)** — Lire info depuis élève et afficher ses champs (2 solutions).
- **B-Act.13 (p.45)** — Fermer (élève) / Close (eleve).
- **B-Act.14 (p.46)** — Compter les garçons d'un fichier de taille inconnue (éventuellement vide ⇒ Tant que .. Faire avec Non(Fin_fichier)).
- **Encadré p.47** — Test d'existence avec {$I-} ReSet … IOResult <> 0 ⇒ ReWrite … {$I+}.
- **B-Act.15 (p.47–51) [P2]** — Programme `F_Positif` / `Fichier1` : fichier "C:\4SI\Nombres.FCH" d'entiers positifs saisis jusqu'à un négatif (non enregistré), puis affichage. Procédures Création (Associer + Recréer), Saisie (Tant que V ≥ 0), Affichage (Ouvrir + Tant que Non Fin_fichier) ; Fermer dans le principal.
- **B-Act.16 (p.51–54) [P3]** — Programme `GESTION` / `Fichier2` : fiches du personnel (nom & prénom, N° CIN et matricule entiers non signés, grade A..D, adresse, téléphone, ancienneté Réel) dans "C:\Perso.dat" ; saisie répétée jusqu'à réponse N à « Continuer (O/N) ? », affichage une fiche par page (Effacer l'écran, pause Lire()). Pas de traduction Pascal donnée.
- **B-Act.17 (p.55)** — Ajouter un entier en fin du fichier Liste : Ouvrir ; p ← Taille_fichier(liste) ; Pointer(liste, p) ; Ecrire(liste, v) (variante : Pointer(liste, taille_fichier(liste))).
- **V.3 Application (p.57–58)** — Procédure Lecture en accès direct sur Liste : saisir un numéro d'ordre, « Vous êtes hors du fichier » si invalide, sinon afficher la donnée ; répéter jusqu'à N à « Continuer (O/N) ? ».
- **B-Act.18 (p.59–60)** — Déclarer un fichier texte Ftexte associé à "A:ESSAI.TXT" (disquette).
- **App.1 (p.61–62) [P2]** — Procédure Ecriture_texte : saisir des lignes et les écrire (Ecrire_nl) jusqu'à O à « Quitter (O/N) ? » (rep ← Lire_Touche / ReadKey).
- **App.2 (p.62) [P2]** — Procédure Affichage_texte : Ouvrir puis Lire_nl ligne par ligne jusqu'à Fin_fichier.
- **App.3 (p.63–65) [P2]** — Programme `Ecriture_Lecture` / `Fichier3` : Associer "C:\Lignes.fch", Recréer, Ecriture_Texte, Ouvrir, Affichage_Texte (avec ClrScr en Pascal), Fermer.

#### Exercices non corrigés (p.68–71)

- **Ex.1 (p.68) [P1]** — Vrai/Faux sur le contenu possible d'un tableau, d'une matrice, d'un type enregistrement (plusieurs types / exactement 2 types / même type).
- **Ex.2 (p.68) [P1]** — Déclarer un enregistrement compte en banque (nom, numéro de compte entier, montant réel).
- **Ex.3 (p.68–69) [P1]** — Programme Pascal à trous `Translation` : record Point (absi, ordo : Real), lecture de M, vecteur (x, y), calcul M.absi/M.ordo. Demande : compléter les parties effacées.
- **Ex.4 (p.69) [P2]** — Structure Info (nom ≤ 30, téléphone ≤ 10, carte bancaire entier non signé) : saisir puis afficher 3 personnes.
- **Ex.5 (p.69) [P2]** — Deux complexes z1, z2 : somme z3 affichée sous la forme a + ib.
- **Ex.6 (p.69) [P3]** — Programme BIBLIO : références (titre, auteur, éditeur, année, pages ; ex. « La chartreuse de Parme de Stendhal édité par Gallimard en 1987 … 683 pages ») ; 2 à 150 références dans un tableau ; saisir une année et afficher les livres publiés cette année.
- **Ex.7 (p.70) [P1]** — QCM sur la Lecture : pourquoi des fichiers carton plutôt que des supports magnétiques ? (moins fiables / plus chers / moins pratiques).
- **Ex.8 (p.70) [P1]** — Vrai/Faux : ce que permet l'accès séquentiel, l'accès direct, ce que peut contenir un type fichier.
- **Ex.9 (p.70) [P2]** — Programme POSITIFS : entiers (≤ 100) dans "C:\NOMBRE1.FCH", transfert dans un tableau T1, copie des positifs de T1 dans "C:\NOMBRE2.FCH".
- **Ex.10 (p.70) [P2]** — Fichier texte exercice.txt alimenté au clavier jusqu'à la chaîne FIN (casse indifférente, non stockée) ; effacer l'écran, relire, afficher.
- **Ex.11 (p.71) [P2]** — Fonction Existe (présence d'un fichier de données) avec directives de compilation ({$I-}/IOResult).
- **Ex.12 (p.71) [P3]** — Fichier "pays.txt" (C:\Pays, lignes ≤ 60 caractères) : chercher la première ligne contenant un pays P ; message « Le pays, P, n'existe pas dans le fichier » ou « Le pays, P, existe dans la ligne : … ».
- **Ex.13 (p.71) [P3]** — Fichier à accès direct d'une classe (dossier "Classes", nom saisi, extension FCH ; noms, prénoms, moyennes de N élèves) ; menu 1 Lecture/Ecriture/Quitter, menu 2 Classe/Elève/Retour ; accès à un élève par numéro d'ordre.
- **Ex.14 (p.71) [P4]** — Vidéo-club : fichier base de films ; Menu Fichiers (créer, ouvrir, supprimer, fermer), Menu Edition (ajouter, modifier, chercher, supprimer un film), Menu Quitter (sortir).

#### Encadrés de règles — VERBATIM (vérifiés sur l'image)

**Définition (p.10)** : « Un enregistrement est un type de données défini par l'utilisateur et qui permet de grouper un nombre fini d'éléments (ou champs) de types éventuellement différents. »

**Déclaration d'une structure ENREGISTREMENT (p.10–11)**
```
En algorithmique — Tableau de déclaration des nouveaux types
Type
Nom_type = Enregistrement
        champ 1 : Type 1
          - -        - -
        champ n : Type n
Fin Nom_Type

Tableau de déclaration des objets
Objet                 | Type / Nature | Rôle
Identificateur_objet  | Nom_type      | Enregistrement pour …

En Pascal
TYPE   Nom_type = Record
              champ_1 : type_1 ;
              -   -       - -
              champ_n : type_n ;
       End;
VAR
       identificateur_objet : Nom_type ;
```
Notes (p.11) : « a. Les types (type 1, type 2, .. , type n) peuvent être soit prédéfinis, soit définis par l'utilisateur. »

**Affectation (p.13)** : algo `variable.champ ← valeur` ; Pascal `variable.champ := valeur ;` — STOP : « Remarquez le point entre variable et champ. »
Remarques (p.15) : « a. Il est possible d'affecter une variable enregistrement dans une autre à condition qu'ils aient la même structure. » (ex. `e1 := e2 ;`) ; « b. Un champ a exactement les mêmes propriétés qu'une variable du même type. » ; « c. Le champ d'une variable enregistrement peut être lui-même un enregistrement. »

**Lecture (p.16)** : analyse `variable.champ = Donnée` | algorithme `Lire (variable.champ)` | Pascal `ReadLn (variable.champ);`
**Ecriture (p.17)** : analyse et algorithme `Ecrire (variable.champ)` | Pascal `Write (variable.champ) ;`

**Structure Avec .. Faire (p.18)** — « NB : Cette structure s'utilise avec une opération d'affectation, de lecture ou d'écriture. »
```
Au niveau de l'analyse et de l'algorithme   | Au niveau du Pascal
Avec variable Faire                         | With variable Do
    {ensemble d'actions}                    | Begin
Fin Avec                                    |     {ensemble d'actions}
                                            | End;
```

**Vecteur d'enregistrements (p.23)** : « Un tableau ne peut contenir que des éléments de même type, y compris le type enregistrement. Nous pouvons donc utiliser un tableau ou un vecteur d'enregistrements. »

**Définition fichier (p.32)** : « Un fichier est un ensemble structuré de données de même type, nommé et enregistré sur un support lisible par l'ordinateur (disque dur, disquette, flash disque, CD Rom, ..etc). Un fichier peut contenir des caractères (fichier textes), des programmes, des valeurs (fichier de données). »

**Pointeur (p.33)** : « Le pointeur de fichier est un entier qui indique à partir de quelle position (ou adresse) du fichier la prochaine fonction d'entrée / sortie doit s'effectuer. » ; « Pointer signifie « faire référence à ». » Organisations : « organisation séquentielle : nous ne pouvons accéder aux enregistrements qu'en les parcourant les uns à la suite des autres. » ; « organisation relative (dite aussi directe) : les enregistrements sont contigus et identifiés par un numéro d'ordre. »

**Types d'accès (STOP p.36)** : « – Accès séquentiel : Pour lire une information particulière, il faut lire toutes les informations situées avant. – Accès direct : Nous pouvons accéder directement à l'information désirée, en précisant le numéro d'emplacement (le numéro d'ordre) de cette information. »

**Déclaration fichier (p.37)**
```
En algorithmique — Tableau de déclaration des nouveaux types
Type
nom_fichier = Fichier de type_composants

Codification des objets
Objet        | Type / Nature | Rôle
nom_logique  | nom_fichier   | Fichier pour …

En Pascal
TYPE
       nom_fichier = File Of type_composants ;
VAR
       nom_logique : nom_fichier ;
```
« type_composants représente le type des composants du fichier, ces composants doivent être de même type, exemple : entiers, réels, enregistrements,etc »

**Syntaxes des traitements (tableaux Syntaxe, p.40–46)**
| Algorithmique | Pascal |
|---|---|
| Associer (nom logique, nom physique) | ASSIGN (nom_logique, nom_physique) ; |
| Recréer (nom logique) | ReWrite (nom_logique) ; |
| Ouvrir (nom logique) | ReSet (nom_logique) ; |
| Ecrire (nom logique, variable) | Write (nom_logique, variable) ; |
| Lire (nom logique, variable) | Read (nom_logique, variable) ; |
| Fermer (nom logique) | Close (nom_logique) ; |
| Fin_fichier (nom logique) | Eof (nom_logique); |

STOP p.40 : « La syntaxe algorithmique : Assigner (nom logique, nom physique) est aussi très utilisée. »
p.41 : « L'instruction "Recréer" permet d'ouvrir un fichier et d'effacer son contenu (recréer le fichier), si le fichier n'existe pas, il sera créé. » ; Ouvrir = « Ouvrir un fichier existant et repositionner ou remettre à zéro (ReSet) son pointeur. Cette instruction permet l'ajout ou la modification des enregistrements. »
STOP p.41 : « Il est à noter que le premier élément ou enregistrement d'un fichier occupe la position numéro zéro du fichier (nous commençons à compter à partir de zéro). »
STOP p.42 : « A chaque écriture d'une valeur ou d'un enregistrement, le pointeur du fichier avance automatiquement d'une position. »
p.46 : Fin_fichier = « fonction booléenne … qui retourne VRAI si la fin du fichier est atteinte. »
STOP p.40 : chemin complet impossible sans autres unités : les dossiers doivent exister, sinon « Runtime error … at …. ».

**Vérification des E/S (bougie, p.47)** : « Par défaut la directive est {$I+} … Si une erreur est détectée, le programme s'arrête sur une erreur d'exécution. Avec la directive {$I-}, l'utilisateur doit gérer lui-même ce type d'erreur grâce à la variable IOResult. (IOResult : Input Output Result). »
```
Write ('Nom du fichier : '); ReadLn (nom);
Assign (Classe , nom );
   {$I-}
ReSet ( Classe );
IF IOResult <> 0 THEN ReWrite( Classe) ;
   {$I+}
```

**Accès direct (p.54–57)**
| Algorithmique | Pascal | Rôle (manuel) |
|---|---|---|
| Pointer (nom logique, numéro) | Seek (nom_logique, numero); | accès direct à l'élément de numéro d'ordre donné (0 pour le 1er ; « pour accéder au nième élément il faut pointer l'élément n-1 ») |
| Taille_fichier (nom logique) | FileSize (nom_logique); | « permet de savoir combien d'éléments se trouvent dans un fichier » |
| Position_fichier (nom logique) | FilePos (nom_logique); | « fournit le numéro d'ordre (la position) de l'élément sur lequel se trouve le pointeur du fichier. Ce numéro est un entier qui vaut 0 pour le premier élément » — « Remarque : Cette fonction ne peut pas s'appliquer à un fichier texte. » |
| Effacer (nom logique) | Erase (nom_logique); | « efface le fichier … Celui ci peut être indifféremment ouvert ou fermé avant effacement. » |
| Renommer (nom logique, nouveau nom physique) | Rename (nom_logique, nouveau_nom_physique); | « change le nom physique d'un fichier. » — STOP : « Nous devons fermer le fichier avant de le renommer. » |
| Tronquer (nom logique) | Truncate (nom_logique); | « Tronque le fichier de travail "nom logique" à la position courante du pointeur de fichier. Tout ce qui se trouve au-delà du pointeur est alors perdu. » |

STOP p.55 : « Il faut faire attention de ne pas se positionner (ou demander un élément) après la fin physique du fichier. Ce contrôle de dépassement doit être fait par le programmeur grâce à la fonction <Taille_fichier> (en Pascal FileSize) ». Bougie p.55 : « A l'aide de la fonction FileSize, on peut se positionner à la fin du fichier de manière à rajouter des éléments. » V.2 p.56 : « Ces fonctions et ces procédures sont valables aussi bien pour l'accès direct que pour l'accès séquentiel. » p.57 : unité `USES Crt, Dos ;` (free Pascal / Pascal 7.x) ou `USES WinCrt, WinDos ;` (TPW 1.x).

**Fichiers texte (p.58–61)**
- Définition : « Un fichier texte (ou le plus souvent et abusivement fichier ASCII), est un fichier dont le contenu représente uniquement une suite de caractères. » STOP : « l'espace et le retour à la ligne sont considérés comme des caractères au même titre qu'une lettre alphabétique, un chiffre ou un signe de ponctuation. »
- Présentation : caractères « Retour chariot » (CR) ou « Fin de ligne » (EoLn) et « Fin de texte » (code CTRL-Z) ; déclaré par le mot réservé <TEXT> ; ouvert en lecture par Ouvrir (ReSet), en écriture par Recréer (ReWrite).
- Déclaration : objet `nom_logique` de Type/Nature `Texte` ; Pascal `VAR nom_logique : Text ;`

| Algorithmique | Pascal | Rôle (manuel) |
|---|---|---|
| Fin_ligne (nom logique) | EoLn (nom_logique); | « retourne Vrai (TRUE) si l'on se trouve sur le caractère CR (retour chariot) et Faux (FALSE) dans le cas contraire. » |
| Ajouter (nom logique) | Append (nom_logique); | « ouvre le fichier et positionne son pointeur à la fin de ce dernier. Seul l'ajout d'éléments est alors possible. » |
| Lire_nl (nom logique, variable) | ReadLn (nom_logique, variable); | « lit le contenu d'une ligne, puis pointe la prochaine ligne (nl = nouvelle ligne) … juste après la première marque CR-LF » |
| Ecrire_nl (nom logique, valeur) | WriteLn (nom_logique, valeur); | « introduit dans le fichier texte un contenu puis une séquence CR-LF pour marquer la fin de ligne. » |

**Retenons (p.66, verbatim)**
« ENREGISTREMENT : Un enregistrement est un type de données défini par l'utilisateur qui permet de grouper des éléments de divers types. Contrairement aux tableaux qui ne permettent de grouper que des éléments de même type, les enregistrements nous permettent de combiner différents types de données.
FICHIER : Un fichier est ensemble [sic] de données stockées sur un support d'enregistrement. Un fichier texte est un fichier dont le contenu représente uniquement une suite de caractères informatiques. Un fichier est enregistré sur un support tel que le disque dur, sous la forme "nom_du_fichier.ext". ".ext" représente l'extension du fichier. L'accès à un fichier peut se faire de deux façons : * Accès séquentiel : L'accès au ième élément du fichier ne peut se faire qu'après une lecture des (i-1) éléments précédents. * Accès direct : L'accès direct permet d'accéder directement à un élément du fichier par l'intermédiaire de son numéro d'ordre (sa position dans le fichier). »

**Retenons (p.67, tableau verbatim)**
| Algorithmique | Pascal | Rôle |
|---|---|---|
| Associer (nom logique, nom physique) | Assign (nom_logique, nom_physique ); | Relier ou associer le nom logique d'un fichier à son nom physique |
| Recréer (nom logique) | ReWrite (nom_logique); | Recréer le fichier, s'il n'existe pas, il sera créé |
| Ouvrir (nom logique) | ReSet (nom_logique); | Ouvrir un fichier existant et remettre à zéro son pointeur. |
| Ecrire (nom logique, variable) | Write (nom_logique, variable) ; | Ecrire ou modifier une valeur ou d'un enregistrement dans un fichier |
| Lire (nom logique, variable) | Read (nom_logique, variable) ; | Lire une valeur ou un enregistrement d'un fichier |
| Fermer (nom logique) | Close (nom_logique); | Fermer un fichier |
| Fin_fichier (nom logique) | Eof (nom_logique); | Fonction booléenne vérifiant si la fin du fichier a été atteinte |
| Pointer (nom logique, numéro) | Seek (nom_logique,numero) ; | Accéder à un élément d'un fichier à accès direct |
| Taille_fichier(nom logique) | FileSize (nom_logique); | Retourner la taille d'un fichier à accès direct |
| Effacer (nom logique) | Erase (nom_logique); | Supprimer un fichier |
| Renommer (nom logique, nouveau nom ) | Rename (nom_logique, nouveau_nom); | Changer le nom d'un fichier |
| Fin_ligne (nom logique) | EoLn (nom_logique); | Fonction booléenne testant la fin d'une ligne dans un fichier texte |
| Ajouter (nom logique) | Append (nom_logique); | Ouvrir un fichier et positionner son pointeur à la fin pour ajouter des enregistrements. |

(NB : Position_fichier/FilePos, Tronquer/Truncate, Lire_nl/ReadLn, Ecrire_nl/WriteLn sont enseignés p.56–61 mais absents du tableau Retenons.)

#### Vocabulaire officiel (termes exacts)

enregistrement, article, RECORD, champ, type défini par l'utilisateur, variable (ou objet) enregistrement, notation « variable.champ » (le point), structure Avec .. Faire (With .. Do), vecteur (tableau) d'enregistrements, Tableau de déclaration des nouveaux types (TDNT), Tableau de déclaration des objets (TDO), Codification des nouveaux types / des objets globaux / des objets locaux ; fichier, fichier de données, fichier texte (fichier ASCII), bloc, pointeur de fichier, adresse, numéro d'ordre, organisation séquentielle, organisation relative (dite aussi directe), accès séquentiel, accès direct (dit aussi accès aléatoire), « le premier entrant est le dernier sortant », type_composants, nom logique (nom interne), nom physique (nom externe), extension (.dat = fichier de données), association / assignation, ouverture et création (Recréer), ouverture et remise à zéro (Ouvrir/ReSet), écriture, lecture, fermeture, test de fin du fichier (Fin_fichier), fin physique du fichier, Taille_fichier, Position_fichier, Effacer, Renommer, Tronquer, directive de compilation {$I+}/{$I-}, IOResult, IO Error, Runtime error, retour chariot (CR), fin de ligne (EoLn), CR-LF, fin de texte (CTRL-Z), Fin_ligne, Ajouter, Lire_nl, Ecrire_nl (nl = nouvelle ligne), Lire_Touche (ReadKey), Majuscule (Upcase), unités Crt / WinCrt / Dos / WinDos.

#### Notions testables (12 > 8 ⇒ découpage proposé)

Le chapitre porte 12 notions testables ; il est trop large pour un chapitre de l'app (≤ 8). **Proposition : deux chapitres.**

**Chapitre 1a — Les enregistrements (p.8–31)** — 4 notions
1. Définition et déclaration d'un enregistrement (TDNT `Enregistrement … Fin`, Pascal `Record … End`), champs de types prédéfinis ou définis par l'utilisateur (intervalle, énuméré, chaîne bornée), enregistrement imbriqué.
2. Accès aux champs par la notation pointée : affectation, lecture (Donnée / Lire / ReadLn), écriture ; affectation globale entre deux variables de même structure.
3. Structure Avec .. Faire / With variable Do Begin … End.
4. Vecteur d'enregistrements : déclaration (`Tableau de n Fiches`, `Array [1..n] Of Fiche`), parcours `T[i].champ`, saisie contrôlée, comptage/recherche, pourcentage ; enregistrement en paramètre (Var pour la saisie).

**Chapitre 1b — Les fichiers (p.32–65)** — 8 notions
5. Notion de fichier, organisation (blocs contigus, pointeur, numérotation à partir de 0, organisation séquentielle vs relative).
6. Types d'accès : séquentiel vs direct (analogies disques, cassette/CD) ; choix fait dans le programme.
7. Déclaration (`Fichier de` / `File Of`, composants de même type ⇒ enregistrement), nom logique vs nom physique, Associer/Assign.
8. Ouverture Recréer/ReWrite vs Ouvrir/ReSet ; Ecrire/Write, Lire/Read (avance automatique du pointeur) ; Fermer/Close.
9. Parcours séquentiel avec `Tant que Non (Fin_fichier(f))` / `While Not Eof(f)` ; test d'existence {$I-} / IOResult.
10. Accès direct : Pointer/Seek, Taille_fichier/FileSize (contrôle de dépassement, ajout en fin), Position_fichier/FilePos.
11. Procédures de gestion : Effacer/Erase, Renommer/Rename (fichier fermé), Tronquer/Truncate.
12. Fichiers texte : Text/Texte, CR/EoLn/CTRL-Z, Fin_ligne/EoLn, Ajouter/Append, Lire_nl/ReadLn, Ecrire_nl/WriteLn ; FilePos inapplicable.

(Variante à 3 chapitres si 1b est jugé trop dense : 1b « Fichiers de données — accès séquentiel » = notions 5–9 ; 1c « Accès direct et fichiers texte » = notions 10–12.)

#### Bornes

✅ **INCLUS**
- Type enregistrement (algo + Pascal), champs de tous types vus, enregistrement imbriqué, affectation globale, Avec..Faire, tableaux d'enregistrements.
- Fichiers typés (`File Of` entiers, réels, enregistrements), nom logique/physique, chemins Windows/DOS (C:\…, A:…), extension.
- Assign, ReWrite, ReSet, Write, Read, Close, Eof ; Seek, FileSize, FilePos, Erase, Rename, Truncate ; Text, EoLn, Append, ReadLn, WriteLn sur fichier.
- {$I-}/{$I+} + IOResult (encadré complément p.47, réutilisé dans l'exercice 11).
- Programmes modulaires complets (analyse descendante : Résultat/Traitement, algorithmes numérotés, codification des objets, traduction Pascal), saisies contrôlées par Répéter..Jusqu'à, menus (ex. 13, 14).
- Utilitaires d'écran rencontrés : ClrScr, ReadKey (Lire_Touche), Upcase (Majuscule), format d'affichage P:6:2, Uses Crt/WinCrt/Dos/WinDos.

⛔ **EXCLU / renvoyé**
- Prérequis des années précédentes (« connaissances … acquises les deux dernières années », p.8) — tableaux, types énumérés et intervalles, procédures/fonctions et passage de paramètres, structures Répéter / Tant que / Pour : supposés connus, non réenseignés ici.
- Les traitements avancés sur fichiers et tableaux (tris, recherches dichotomiques, récursivité, etc.) relèvent des autres chapitres du manuel (non lus ; ne pas les injecter ici).
- Non mentionnés dans le chapitre (ne pas en faire des questions) : fichiers non typés (`File` sans `Of`), BlockRead/BlockWrite, SeekEof/SeekEoln, Flush, Reset avec taille d'enregistrement, enregistrements à variantes (`case` dans `Record`), pointeurs/allocation dynamique, gestion des dossiers (MkDir, etc.), `Read` de nombres dans un fichier texte.
- Append n'est présenté **que** pour les fichiers texte ; FilePos ne s'applique **pas** au fichier texte (p.56).

#### Lecture (p.72) — résumé

« Notion de fichier » (d'après info.sio2.be/infobase/18/2.php) : dans les années 1960 les supports magnétiques (disques durs, disquettes) étaient encore très chers ; on enregistrait les informations sur des **cartes perforées** de 80 colonnes (valeurs 0/1 par perforation), soit 80 octets par carte ; un paquet de cartes formait un « fichier informatique » (données à traiter ou programmes). Le nom est resté avec les supports magnétiques : un fichier informatique est donc n'importe quel ensemble d'informations (données, résultats, programme) enregistré sur un support quelconque. Sert de support à l'exercice 7 (réponse attendue au texte : supports magnétiques « plus chers »).

#### Note de lecture

- **Méthode** : couche texte `pdftotext -layout` page par page sur p.7–72 (66 pages), puis sondage image (`pdftoppm`, 70–110 dpi) de **40 pages** : 7, 10, 13, 18, 19, 23–31, 33–37, 40–42, 45–47, 51, 54–56, 58, 60–63, 66–71. Tous les encadrés de syntaxe et les deux pages Retenons ont été confrontés à l'image : conformes.
- **Écarts texte ↔ image : 2**
  1. p.23 (A-Act.10) : texte « N (4 ) N ) 30) » ↔ image « N (4 ≤ N ≤ 30) » (glyphe ≤ perdu). ⇒ sous-section A.III.5 sondée en entier (p.23–31) : aucun autre écart.
  2. p.34–36 (B.III, Activités 1–2) : l'information portée par les schémas (ordre d'empilement : rouge en bas, vert, bleu, jaune en haut ; 4 supports jaune/bleu/rouge/vert ; légende « Accès au disque rouge ») est absente de la couche texte. ⇒ section B.III sondée en entière (p.34–36) ; texte et schémas cohérents.
  Ailleurs, les ≤/≥ de la couche texte (p.24, 49, 58) sont corrects.
- **Coquilles / erreurs du manuel `[sic]`** (à ne pas reproduire ; à corriger dans le contenu généré) :
  - p.12 « varaiable » ; p.14 le tableau des objets est titré « Tableau de déclaration des nouveaux types » ; p.15 « à condition qu'ils aient » ; p.32 « écris » ; p.36 « accèdons », « que l'on choisissons » ; p.40 « crées », p.42 « déjà crée » ; p.41 « en vu d' » ; p.66 « Un fichier est ensemble de données » ; p.68 « V (Vrai) ou (Faux) », « ont étés effacées » ; p.70 « peut importe » ; p.71 « fichier a accès direct », « saisit ».
  - p.59-60 (B-Act.18) : l'algorithme déclare `Ftexte`, le Pascal `VAR Ftext : text` [sic].
  - Numérotation d'algorithmes : p.25 « 3) Fin Gestion » après 5) ; p.29 « 2) Fin Result » après 3) ; p.49 « 2) Fin Saisie » après 2).
  - p.29 guillemets mal appariés dans Ecrire ("Le nombre d'occurrences de ', G, …) ; p.31 « occurrencse » ; p.30 « Entrer le son code fiscal ».
  - p.38 type nommé `notes_élève` puis utilisé `notes_élèves`/`note_élèves` ; Pascal `notes : notes_eleves` sans « ; ».
  - p.46 algorithme : « Alors nbg := nbg +1 » (affectation Pascal dans l'algorithme).
  - p.49 paramètre `Var Liste : F_Entier` alors que le type est `F_Entiers`.
  - p.52 Activité 16 : la procédure **Création** utilise `Ouvrir (Classeur)` (ReSet) et non `Recréer` — incohérent avec « création » (échec si le fichier n'existe pas). p.53 : `Fiche` passé sans Var ; mélange `REP`/`rep` ; condition finale `Jusqu'à (REP = "N")` sans Majuscule alors que l'analyse utilise Majuscule(rep). p.54 en-tête « Objet O ».
  - p.58 V.3 : condition de validité `Jusqu'à ( num < T) OU (num ≥ 0)` — logiquement erronée (devrait être ET) ; à signaler comme erreur, ne pas reprendre.
  - p.62–65 fichiers texte : l'algorithme Affichage_Texte lit `ligne`, le Pascal lit `phrase` (non déclarée dans cette procédure : `phrase` est locale à Ecriture_Texte) ; Pascal Ecriture_Texte `ReadLn (ligne)` puis `WriteLn (Lignes, phrase)` ; p.63 « Affiche_Texte » pour Affichage_Texte ; le principal fait `Ouvrir (Lignes)` alors qu'Affichage_Texte rouvre déjà.
  - p.56 vs p.67 : `Rename (nom_logique, nouveau_nom_physique)` vs `Rename (nom_logique, nouveau_nom)` (même instruction, libellé différent).
  - p.69 Ex.3 : le programme à trous affiche `M.ordi` alors que le champ est `ordo`, et écrit `: =` avec espace (à traiter comme coquille, ou piège involontaire `[?]`).
- **Doutes `[?]`** : aucun sur les pictogrammes (légende p.5 lue et rattachement vérifié par la relecture R-7).

## Fiche de lecture ch.1

- **pagesLues** : 7–72 (66 pages, couche texte L1 intégrale)
- **Pages sondées (image)** : 7, 10, 13, 18, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 45, 46, 47, 51, 54, 55, 56, 58, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71 (40 pages)
- **Nombre d'écarts texte ↔ image** : 2 (p.23 glyphe ≤ perdu ; p.34–36 information portée par les schémas seuls) — sections correspondantes (A.III.5, B.III) sondées en entier, sans autre écart.
Source unique : manuel élève CNP « Algorithmique et programmation », 4ème année secondaire, Sciences de l'informatique (248 p.). PDF = page imprimée (décalage 0). Aucun guide enseignant.
Conventions : `[sic]` coquille de la source ; `[?]` illisible / doute ; « … » = verbatim. Notation algorithmique du manuel conservée (`←`, `Long`, `Sous_chaîne`, `Div`, `FN`, `Proc`).

---

### Chapitre 2 — La récursivité (p.73–94)

#### Plan (p.73)
| § | Titre | Pages |
|---|---|---|
| — | Page de garde (objectifs, plan) | 73 |
| I | Introduction — Activité 1 (factorielle), Activité 2 (palindrome) | 74–80 |
| II.1 | Définitions | 80 |
| II.2 | Principes | 80–81 |
| III | Applications 1 à 4 (somme, puissance, tri par sélection récursif, recherche dichotomique récursive) | 81–88 |
| — | Retenons | 89 |
| — | Exercices 1 à 10 | 90–92 |
| — | Lecture (« La récursivité est un concept naturel » ; « La récursivité pas à pas ») | 93–94 |

#### Objectifs officiels (p.73, verbatim)
- « Définir la récursivité »
- « Reconnaître et identifier des algorithmes récursifs »
- « Résoudre des problèmes faisant appel à la récursivité »

#### Activités du cours (I. Introduction)
- **Activité 1 — Factorielle (p.74–77).** Q1 : analyse + algorithme d'une fonction calculant n! ; nommer le procédé (réponse du manuel : procédé itératif — init `F ← 1`, `Pour i de 2 à n Faire F ← F * i`, type Entier Long, compteur Entier non signé (Mot)). Q2 : proposer un procédé différent → passage de la Formule 1 `factorielle(n) = n * (n-1) * … * 1, factorielle(0) = 1` à la Formule 2 `factorielle(n) = n * factorielle(n-1), factorielle(0) = 1` (« Traitement Récursif ») ; trace détaillée de `Factorielle(4)` en 5 étapes jusqu'au « cas particulier » 0 → `4*3*2*1*1`, « Le résultat final = 24 ». Q3 : traduire et tester en Pascal, programme `Fact_rec`.
- **Activité 2 — Palindrome (p.77–80).** Q1 : algorithme itératif (Répéter … Jusqu'à, `Verif ← (ch[i] = ch[Long(ch) – i + 1])`, arrêt à `(i > Long(ch) Div 2) Ou (Verif = Faux)` ; i Octet, Verif Booléen). Exemples de palindromes : radar, rotor, été. Q2 : dégager une relation récursive — traces sur "radar" (→ "ada" → "d", Vrai) et "exemple" (→ "xempl", `"x" ≠ "l"` → Faux). Q3 : algorithme récursif. Q4 : programme Pascal (nom demandé `ch_Pal`, programme imprimé `PROGRAM palindrome_rec;` [sic : écart de nom]).

Encadré p.75 (verbatim) : « Et si pour résoudre un problème, on réduisait sa taille ? Dans certains cas, la solution d'un problème peut se ramener à résoudre le même problème de taille plus réduite, qui lui-même pourra se ramener à résoudre le même problème de taille encore plus petite ... jusqu'à aboutir à la résolution d'un problème élémentaire. »

**Factorielle récursive (p.76) — algorithme :**
```
0) Fonction Factorielle (n : Entier non signé) : Entier Long
1) Si (n = 0) Alors Factorielle ← 1
   Sinon Factorielle ← n * Factorielle (n-1)
   Fin Si
2) Fin Factorielle
```
Constatations p.76 (verbatim) : « La solution récursive comporte : L'appel récursif en changeant la valeur du paramètre. Dans l'exemple de la fonction Factorielle, le paramètre est décrémenté de 1 à chaque appel, (Factorielle ← n * Factorielle (n-1)) / La condition d'arrêt de l'appel récursif. En effet, nous arrêtons le traitement quand n devient égal à 0 (Si n = 0 Alors Factorielle ← 1) »

**Pascal (p.76–77) :**
```pascal
PROGRAM Fact_rec;
Uses Crt;
Var n : Word;
Function Factorielle (m : Word) : LongInt;
Begin
  If (m = 0) Then Factorielle := 1
  Else Factorielle := m * Factorielle (m - 1);
End;
{Programme Principal}
BEGIN
  Write ('n = '); ReadLn (n);
  Write ('n! = ', Factorielle (n));
END.
```

**Relation récursive du palindrome (p.78, verbatim) :** « Un mot d'un seul caractère est un palindrome, sinon il l'est dès que ses caractères extrêmes sont les mêmes et le mot restant est aussi un palindrome. » — « Si Longueur (ch) < 2 alors ch est un palindrome / Sinon si ch[1] = ch[Long (ch)] alors Palindrome (ch) = Palindrome (ch sans ses premier et dernier caractères) / Sinon ch n'est pas un palindrome. »

**Palindrome récursif (p.79) — algorithme :**
```
0) Fonction Palindrome (ch : Chaîne) : Booléen
1) Si Long (ch) < 2 Alors Palindrome ← Vrai
   Sinon Si ch[1] = ch[Long (ch)]
         Alors Palindrome ← Palindrome (Sous_chaîne (ch, 2, Long (ch) - 2))
         Sinon Palindrome ← Faux
   FinSi
2) Fin Palindrome
```
Encadré « Conclusion » p.79 (verbatim, vérifié sur image) : « La solution récursive comporte : / Un appel récursif en changeant la valeur du paramètre. Dans l'exemple de la fonction Palindrome, le paramètre ch est démuni de son premier et de son dernier caractère s'ils sont identiques, (Palindrome ← Palindrome (Sous_chaîne (ch, 2, Long (ch) - 2))) / Une 1ère condition d'arrêt de l'appel récursif. En effet, nous arrêtons le traitement lorsque les caractères extrêmes du paramètre sont différents (Palindrome ← Faux) / Une 2ème condition d'arrêt de l'appel récursif, lorsque le paramètre est composé d'un seul caractère (Si Long (ch) < 2 Alors Palindrome ← Vrai) »

**Pascal (p.79–80) :**
```pascal
PROGRAM palindrome_rec;
Uses Crt;
Var ch : String;
Function Palindrome (ch : String) : Boolean;
Begin
  If Length(ch) < 2 Then Palindrome := True
  Else If (ch[1] = ch[length(ch)])
       Then Palindrome := Palindrome (Copy (ch, 2, Length (ch) - 2))
       Else Palindrome := False;
End;
{Programme Principal}
BEGIN
  Write ('Donner ch = '); ReadLn (ch);
  If Palindrome (ch) Then WriteLn (ch, ' est un palindrome.')
  Else WriteLn (ch, ' n''est pas un palindrome.');
END.
```

#### Encadrés de règles — II. Définitions et principes (p.80–81, verbatim, p.80 vérifiée sur image)
**II.1 Définitions** : « La **récursivité** est une méthode algorithmique qui consiste à appeler un sous-programme dans son propre corps. Cette méthode permet de résoudre des problèmes où l'on doit itérer un nombre de fois dépendamment du nombre de données.
Un sous-programme récursif est un module qui s'"appelle" [sic] lui-même. A chaque appel, il y a mémorisation d'une valeur différente d'un même paramètre formel.
Le principal avantage d'un algorithme récursif est qu'il est généralement plus simple, plus lisible et naturel à comprendre. Par contre, le principal problème est la définition du ou des cas d'arrêt. Il est important de s'assurer que le programme se termine correctement dans tous les cas.
La limite technique de la récursivité est la mémoire stockant les données intermédiaires des sous-programmes, que nous appelons la "pile". Cette dernière déborde lorsque le nombre des appels devient important. »

Encadré « Remarques » (STOP) : « 1) Les fonctions **récursives** sont appelées depuis leur propre corps, soit directement, soit indirectement à travers une ou plusieurs fonctions relais. Par exemple, si la fonction P appelle directement P, nous disons que la récursivité est directe. Si P appelle une fonction P1, qui appelle une fonction P2, ..., qui appelle une fonction Pn et qui enfin appelle P, nous disons qu'il s'agit d'une récursivité indirecte.
2) La récursivité est dite **croisée** lorsque plusieurs procédures ou fonctions s'appellent mutuellement. »

**II.2 Principes** (illustré par 3 vignettes d'un cube fractal à niveaux croissants, absentes de la couche texte) : « Un programme récursif doit :
➣ traiter un ou plusieurs cas particuliers représentés par une ou plusieurs conditions d'arrêt, sinon il tournera indéfiniment.
➣ traiter un ou plusieurs cas généraux représentés par des appels récursifs. Chaque fois qu'un programme récursif est appelé (par lui-même), un ou plusieurs des arguments qui lui sont transmis doivent converger et arriver à la condition d'arrêt.
C'est à dire que la complexité du problème doit être réduite à chaque nouvel appel récursif. »
Remarque : « L'itération et la récursivité, correspondent à deux modes de pensée différents. Le principe de passage du mode récursif au mode itératif s'appelle : la dérecursification [sic]. »

#### III. Applications (exercices résolus)
- **Application 1 — Somme des n premiers entiers (p.81–82).** Analyse récursive, algorithmes, programme `Somme` (pp. `Somme_N`, `Proc Saisir (n)`). Cas particulier `m = 0 → 0`, cas général `m + Somme (m-1)`.
  ```
  0) Fonction Somme (m : Entier non signé) : Entier Long
  1) Si (m = 0) Alors Somme ← 0
     Sinon Somme ← m + Somme (m - 1)
     Finsi
  2) Fin Somme
  ```
  ```pascal
  Function Somme (m : Word) : LongInt;
  Begin
    If m = 0 Then Somme := 0
    Else Somme := m + Somme (m - 1);
  End;
  ```
- **Application 2 — Puissance aⁿ, a réel, n entier (p.82–83).** Programme `Exposant` (pp. `Puiss`). Un cas particulier + deux cas généraux (exposant négatif).
  ```
  0) Fonction Puissance (a : Réel ; n : Entier) : Réel
  1) Si n = 0 Alors Puissance ← 1
     Sinon Si n < 0 Alors Puissance ← 1 / Puissance (a, -n)
     Sinon Puissance ← a * Puissance (a, n-1)
     Finsi
  2) Fin Puissance
  ```
  ```pascal
  Function Puissance (a : Real; n : Integer) : Real;
  Begin
    If (n = 0) Then Puissance := 1
    Else If (n < 0) Then Puissance := 1 / Puissance (a, -n)
    Else Puissance := a * Puissance (a, n - 1);
  End;
  ```
- **Application 3 — Tri par sélection récursif, ordre décroissant (p.83–85).** Programme `Selection` : `Saisir`, `Remplir`, `Tri_Sel_Rec (1, n, T)`, `Afficher_T` ; type `Tab = Tableau de n entiers`. Chaque appel : recherche de l'indice du maximum (`FN Max`), permutation si ≠ deb, puis appel sur `deb+1` si `deb+1 ≠ fin`. NB : Max et Permuter « ont été l'objet d'un apprentissage au niveau de la 3ème année ».
  ```
  0) Procedure Tri_Sel_Rec (deb, fin : Entier ; Var T : Tab)
  1) Maximum ← FN Max (deb, fin, T)
     Si Maximum ≠ deb Alors Proc Permuter (T, deb, maximum)
     FinSi
  2) Si deb+1 ≠ fin Alors Proc Tri_Sel_Rec (deb+1, fin, T)
     Finsi
  3) Fin Tri_Sel_Rec
  ```
  ```pascal
  Procedure Tri_Sel_Rec (deb, fin : Integer; Var T : Tab);
  Var Maximum : Integer;
    Function Max (deb1, fin1 : Integer; T : Tab) : Integer;
    Var i, M : Integer;
    Begin
      M := deb1;
      For i := deb1+1 To fin1 Do
        If (T[i] > T[M]) Then M := i;
      Max := M
    End;
    Procedure Permuter (Var x, y : Integer);
    Var aux : Integer;
    Begin
      aux := x; x := y; y := aux;
    End;
  Begin
    Maximum := Max (deb, fin, T);
    If (Maximum <> deb) Then Permuter (T[deb], T[Maximum]);
    If (deb+1 <> fin) Then Tri_Sel_Rec (deb+1, fin, T);
  End;
  ```
- *[sic] p.84 : l'analyse écrit une troisième signature `Permuter (deb, maximum, T)`, en plus de l'algorithme `(T, deb, maximum)` et du Pascal `(T[deb], T[Maximum])`.*
- **Application 4 — Recherche dichotomique récursive (p.86–88).** Tableau supposé trié croissant ; programme `Dichotom` (pp. `Recherche`). 4 cas : `m = T[milieu]` ; `m < T[milieu]` et `deb < milieu` → moitié gauche ; `m > T[milieu]` et `fin > milieu` → moitié droite ; sinon absent ; `milieu ← (deb + fin) Div 2`.
  ```
  0) Fonction Dichotomique (deb, fin, m : Entier ; T : Tab ) : Booléen
  1) milieu ← (deb + fin) Div 2
  2) Si m = T[milieu] Alors Dichotomique ← Vrai
     Sinon Si (m < T[milieu]) Et (deb < milieu)
           Alors Dichotomique ← Dichotomique (deb, milieu-1, m, T)
     Sinon Si (m > T[milieu]) Et (fin > milieu)
           Alors Dichotomique ← Dichotomique (milieu+1, fin, m, T)
     Sinon Dichotomique ← Faux
     Finsi
  3) Fin Dichotomique
  ```
  ```pascal
  Function Dichotomique (deb, fin, m : Integer; T : Tab) : Boolean;
  Var milieu : Integer;
  Begin
    milieu := (deb + fin) Div 2;
    If (m = T[milieu]) Then Dichotomique := True
    Else If (m < T[milieu] ) And (deb < milieu)
         Then Dichotomique := Dichotomique (deb, milieu-1, m, T)
    Else If (m > T[milieu] ) And (fin > milieu)
         Then Dichotomique := Dichotomique (milieu+1, fin, m, T)
    Else Dichotomique := False
  End;
  ```

#### Retenons (p.89, verbatim, vérifié sur image)
« – Tout objet est dit **récursif** s'il se définit à partir de lui-même. Ainsi, un sous-programme est dit **récursif** s'il comporte, dans son corps, au moins un appel à lui-même.
– La réalisation d'un module récursif revient toujours à une analyse par cas, dans laquelle nous distinguons les **cas généraux** des **cas particuliers**. »

#### Exercices non corrigés (p.90–92) — difficulté (silhouettes de la légende p.5, vérifiées R-7) : Ex.1-3 simple ; Ex.4-7 moyen ; Ex.8-10 assez élevé
1. **Ex.1 (p.90)** — Vrai/Faux à cases : (a) une procédure est obligatoirement / n'est jamais / peut être récursive ; (b) un module récursif utilise obligatoirement une structure conditionnelle / itérative à condition d'arrêt / itérative complète ; (c) pour la récursivité l'ordinateur utilise une pile / un fichier / un tableau ; (d) quels dessins sont réalisables par un module récursif — 3 figures (image seulement) : carrés emboîtés partageant un coin, arbre à branches ramifiées, cercles concentriques.
2. **Ex.2 (p.90)** — « Que fait la fonction » `inconnue (st : chaîne)` : `Si st = "" Alors inconnue ← "" Sinon inconnue ← st[Long (st)] + FN inconnue (Sous_chaîne (st, 1, Long (st) - 1))` (inversion de chaîne — déduction du transcripteur, exercice non corrigé).
3. **Ex.3 (p.91)** — Trouver l'erreur dans deux fonctions Pascal : (a) `Pair` (`N=0 → True`, `N=1 → False`, sinon `Pair (N - 1)`) ; (b) `Impair` contenant une `Pair` locale, appels mutuels (`Pair := Impair (N - 1)`, `Impair` : `N = 1 → True`, sinon `Pair (N - 1)`).
4. **Ex.4 (p.91)** — Analyse + algorithme d'une fonction récursive `Pair_C` : un mot contient-il un nombre pair d'occurrences d'un caractère C ?
5. **Ex.5 (p.91)** — Fonction récursive : valeur la plus proche d'un entier M dans un tableau T de N entiers.
6. **Ex.6 (p.91)** — Fonction récursive `Contigus` : deux caractères contigus identiques ? Exemples : "passer" → vrai, "fonction" → faux, "b" → faux.
Consigne commune Ex.7–10 (p.92) : analyse modulaire avec procédé récursif + algorithmes, puis traduire et tester.
7. **Ex.7** — Inverser une chaîne (programme `Inverse`).
8. **Ex.8** — Recherche séquentielle récursive de m dans T de n entiers (`Rech_Seq`).
9. **Ex.9** — PPCM de deux entiers (`PPCM`).
10. **Ex.10** — Décomposition de N en produit de facteurs premiers (`Fact_Prem`).

#### Vocabulaire officiel
récursivité ; sous-programme / module récursif ; traitement récursif vs procédé (traitement) itératif ; appel récursif ; condition d'arrêt ; cas particulier(s) / cas général(aux) ; paramètre formel ; pile, débordement (de pile) ; récursivité directe / indirecte / croisée ; fonctions relais ; dérécursification ; analyse par cas ; palindrome ; recherche dichotomique ; `Sous_chaîne` (Pascal `Copy`), `Long` (`Length`). Lecture : « point terminal », « point d'appui », « point d'arrêt ».

#### Notions testables (8)
1. Définition : sous-programme récursif = appel à lui-même dans son corps ; récursivité directe / indirecte / croisée.
2. Structure d'un module récursif : cas particulier(s) = condition(s) d'arrêt, cas général(aux) = appel(s) récursif(s) ; analyse par cas ; structure conditionnelle obligatoire.
3. Convergence : les arguments doivent tendre vers la condition d'arrêt (taille réduite à chaque appel) ; sinon exécution infinie.
4. Trace d'exécution / valeur retournée (Factorielle(4) = 24, Somme, Puissance y compris n < 0, Palindrome, `inconnue`).
5. Pile : mémorisation d'une valeur du paramètre à chaque appel ; débordement ; avantage (lisibilité) vs limite (mémoire).
6. Récursivité sur les chaînes : palindrome (2 conditions d'arrêt), inversion, `Copy (ch, 2, Length (ch) - 2)`.
7. Récursivité sur les tableaux : tri par sélection récursif (Max + Permuter + appel sur deb+1), recherche dichotomique récursive (milieu, 4 cas).
8. Itératif ↔ récursif (dérécursification), traduction Pascal (`Factorielle := m * Factorielle (m - 1)`), détection d'une erreur dans une fonction récursive (Ex.3, **non corrigé par le manuel** ; remarque du transcripteur, à valider avant tout corrigé : a) relation de récurrence erronée `Pair := Pair (N - 1)`, fausse dès N = 2 ; b) récursivité croisée qui ne s'arrête pas pour N pair).

#### Bornes
- ✅ INCLUS : fonctions et procédures récursives simples sur entiers, réels, chaînes et tableaux à une dimension ; récursivité directe, notion de récursivité indirecte/croisée ; condition d'arrêt, pile ; tri par sélection récursif ; recherche dichotomique et séquentielle récursives ; PPCM, facteurs premiers, inversion de chaîne (exercices) ; traduction en Pascal (Turbo Pascal : `Uses Crt`, `Word`, `LongInt`).
- ⛔ EXCLU (non traité dans ces pages) : analyse formelle de complexité des algorithmes récursifs ; récursivité terminale ; arbres d'appels dessinés (le manuel montre des traces linéaires, pas d'arbres) ; Hanoï, Fibonacci, Ackermann (non cités) ; algorithmes de dérécursification (nom seulement) ; structures récursives (listes chaînées, arbres).

#### Lecture (p.93–94) — résumé
- « La récursivité est un concept naturel » (source pauillac.inria.fr) : l'auteur conteste que la récursivité soit difficile à saisir et la traque dans la vie courante — philosophie grecque (« Connais-toi toi-même », Socrate), paradoxe du menteur, La Bruyère, Guy Bedos (blague de la mémoire), dictionnaire, proverbe, superstition, titre de livre de Raymond Smullyan, l'œuf et la poule (récursivité mutuelle) ; mention d'Archimède.
- « La récursivité pas à pas » (source chambily.com) : définition « récursive » plaisante puis sérieuse ; la récursivité utilise toujours la pile du programme (zone mémoire stockant variables locales et paramètres, empilés à chaque appel, risque de « débordement de pile », puis désempilés) ; tout programme récursif comporte un « point terminal » / « point d'appui » / « point d'arrêt ».

#### Note de lecture ch.2
- Pages lues couche texte : 73–94 (22 p.). Pages sondées image : 74, 75, 76, 77, 78, 79, 80 (section I entière + II.1 après écart à p.75), 89, 90.
- Écarts texte↔image : (1) p.75 — partie colorée de la Formule 1 (`(n-1) * (n-2) * (n-3) * … * 1`) et de la Formule 2 (`* factorielle (n-1)`) : la couleur, porteuse du sens de la question, est perdue en L1 ; accolades disloquées. (2) p.80 — 3 vignettes de cube fractal (II.2) absentes du texte. (3) p.90 — Ex.1 d : les 3 dessins n'existent qu'en image. Aucun écart de contenu sur les pages de la section I sondée entièrement (seulement couleurs/gras : mots-clés « cas particulier », « Traitement Récursif »).
- Coquilles `[sic]` : « s'"appelle" » (p.80, présent aussi sur l'image) ; « dérecursification » (p.81) ; Application 1 : objet de la table nommé « S » au lieu de « Somme » (p.81) ; Application 2 : « Donner un entier » pour lire a, déclaré Réel (p.83) ; Application 3 : algorithme `Permuter (T, deb, maximum)` vs Pascal `Permuter (T[deb], T[Maximum])` (signature différente), table « objets globaux » pour des objets locaux (p.85) ; Activité 2 Q4 : nom `ch_Pal` demandé vs `PROGRAM palindrome_rec` ; « Connaîs-toi » (p.93).
- Doutes `[?]` : Tri_Sel_Rec appelé avec n = 1 (deb+1 ≠ fin vrai pour deb=1, fin=1) — cas non traité par le manuel, ne pas en faire une question. Ex.1 d : la réponse attendue n'est pas donnée (exercice non corrigé).

---

### Chapitre 3 — Les algorithmes de tri (p.95–122)

#### Plan (p.95)
| § | Titre | Pages |
|---|---|---|
| — | Page de garde (objectif, plan) | 95 |
| I | Introduction — tris internes/externes ; Activité 1 (sélection), Activité 2 (bulles) | 96–97 |
| II | Tri par insertion : II.1 Principe, II.2 Exemple, II.3 Résolution du problème | 97–102 |
| III | Tri Shell : III.1 Insuffisances du tri par insertion, III.2 Principe, III.3 Exemple, III.4 Résolution | 103–107 |
| IV.1 | Application 1 : Tri par fusion (principe, exemple, résolution) | 107–113 |
| IV.2 | Application 2 : Classement (rangs de 30 élèves) | 113–117 |
| — | Retenons + citation | 118 |
| — | Exercices 1 à 6 | 119–121 |
| — | Lecture « Les tris » | 122 |

#### Objectif officiel (p.95, verbatim)
« Acquérir des habilités [sic] de résolution de problèmes à travers l'apprentissage de quelques algorithmes de tri. »

#### I. Introduction (p.96–97)
Définition (p.96, verbatim) : « De manière plus restrictive, le terme "tri" en algorithmique est souvent attaché au processus de classement d'une suite d'éléments dans un ordre donné. […] D'une façon générale, tout ensemble muni d'un ordre total peut fournir une suite d'éléments à trier.
Il existe deux catégories de tris :
Les tris internes : Méthodes destinées à des masses de données limitées, stockées dans une structure de données se trouvant dans la mémoire centrale (Exemple : tableaux).
Les tris externes : Méthodes destinées à de grandes masses de données, stockées dans des structures de données telle que les fichiers. »
Rappel : « Vous avez utilisé dans le programme de 3ème année les méthodes de tri par sélection et à bulles. »

- **Activité 1 (p.96)** — Donner le principe du tri par sélection ; algorithme de `SELECTION (n : entier; Var T : Tab)` ; programme Pascal (avec l'enseignant) : remplissage aléatoire, tri, affichage. Le manuel ne donne que l'algorithme formel :
  Tri par sélection (verbatim) : « 1- Placer dans l'élément d'indice 1 du tableau T la plus petite valeur présente dans le tableau et mettre à sa place l'ancienne valeur de T[1]. 2- Placer dans l'élément d'indice 2 de T la plus petite valeur présente dans la tranche de tableau T[2..N] 3- Placer dans l'élément d'indice 3 de T la plus petite valeur présente dans la tranche de tableau T[3..N] 4- et ainsi de suite jusqu'à l'étape N-1 »
- **Activité 2 (p.96–97)** — Principe du tri à bulles ; algorithme de `BULLES (n : Entier; Var T : Tab)` ; programme Pascal, ordre croissant. Algorithme formel (verbatim) : « L'algorithme du tri à bulles (bubble sort en anglais) consiste à comparer les différentes valeurs adjacentes du tableau T, et à les permuter s'ils ne sont pas dans le bon ordre. L'algorithme se déroule ainsi : 1- Les deux premiers éléments du tableau sont comparés, si le premier élément est supérieur au second, une permutation est effectuée. 2- Ensuite, sont comparées et éventuellement permutées les valeurs 2 et 3, 3 et 4 jusqu'à (n-1) et n. 3- Une fois cette étape achevée, il est certain que le dernier élément du tableau est le plus grand. L'algorithme reprend donc pour classer les (n-1) éléments qui précédent [sic]. 4- L'algorithme se termine quand il n'y a plus de permutations possibles. »
  Remarques (verbatim) : « 1- Pour classer les n valeurs du tableau T, il faut, au pire des cas, effectuer l'algorithme n fois. 2- Cette méthode porte le nom de tri à bulles car, petit à petit, les plus grands éléments du tableau remontent, par le jeu des permutations, en fin du tableau. »
  ⚠ Le cours ne donne **ni algorithme détaillé ni Pascal** itératif pour la sélection et les bulles (seuls : version récursive de la sélection au ch.2 App.3 ; `pos_min` et `TRI_Bulles` dans les exercices 1–2 p.119).

#### II. Tri par insertion (p.97–102)
Principe (p.97, verbatim) : « Le principe du tri par insertion est d'insérer à la n-ième itération, le n-ième élément à la bonne place dans la liste formée par les (n-1) éléments qui le précèdent. »
Pseudo-code (p.97) :
```
PROCEDURE Tri_Insertion (n : Entier; Var T : Tab)
  Pour i de 2 à n Faire
    INSERER T[i] à sa place dans T[1..(i-1)]
FIN
```
Principe général et processus (p.98, verbatim) : « - Considérer que les (i-1) premiers éléments de la liste sont triés et placer le ième élément à sa place parmi les (i) premières places. - Répéter cette action jusqu'à atteindre la fin de la liste. Le processus d'insertion consiste à : - utiliser une variable intermédiaire Tmp pour conserver la valeur à insérer, - déplacer les éléments T[i-1], T[i-2], ... vers la droite tant que leur valeur est supérieure à celle de tmp. - affecter alors à l'emplacement laissé libre par ce décalage la valeur de Tmp. »
Remarque (p.98, verbatim) : « Une variante du tri par insertion consiste à utiliser une recherche dichotomique. En effet, à la n-ième itération, les éléments de 1 à n-1 sont triés, et nous pouvons donc utiliser un algorithme de recherche dichotomique pour trouver la place où insérer l'élément n. »

**Exemple (p.98–99, vérifié sur image)** — T = [-5, 30, 0, -2, 42, 22, 9] (indices 1..7), ordre croissant. Étape 1 : 30 > -5, rien ne bouge. Étape 2 : Tmp = 0, décalage de T[2] → [-5, 0, 30, -2, 42, 22, 9]. Étape 3 : Tmp = -2, décalage de T[3] et T[2] → [-5, -2, 0, 30, 42, 22, 9].
- **Activité (p.99)** : continuer les étapes jusqu'au tableau trié ; combien d'étapes pour ce tableau ? réponse générale en fonction de n.

**Résolution (p.100–102)** — programme `tri_INS` : `Saisir (n)`, `Remplir (T, n)`, `Trier (T, n)`, `Afficher (T, n)`.
```
0) Début Procédure Trier (n : entier; VAR T : Tab)
1) Pour c de 2 à n Faire
     Si T[c-1] > T[c]
     Alors Tmp ← T[c]
           Proc DECALER (T, c-1, p)
           T[p+1] ← Tmp
     FinSi
   Fin Pour
2) Fin Trier

0) Début Procédure DECALER (VAR T : Tab; deb : Entier; Var fin : Entier)
1) fin ← deb
   Tant que (fin >= 1) ET (T[fin] > Tmp) Faire
     T[fin+1] ← T[fin]
     fin ← fin - 1
   Fin Tant que
2) Fin DECALER
```
Objets : c (compteur), Tmp (variable intermédiaire), p (position d'insertion), DECALER (procédure « Permettant de décaler des éléments d'un tableau d'un nombre de positions »).
```pascal
Procedure Trier (n : Integer; Var T : Tab);
Var c, Tmp, p : Integer;
  Procedure Decaler (Var T : Tab; deb : Integer; Var fin : Integer);
  Begin
    fin := deb;
    While (fin >= 1) And (T[fin] > tmp) Do
    Begin
      T[fin + 1] := T[fin];
      fin := fin - 1;
    End;
  End;
{Procédure Trier}
Begin
  For c := 2 To n Do
    If T[c-1] > T[c] Then
    Begin
      Tmp := T[c];
      Decaler (T, c-1, p);
      T[p+1] := Tmp;
    End;
End;
```
- **Application (p.102)** : proposer une solution récursive du tri par insertion.

#### III. Tri Shell (p.103–107, section entièrement sondée en image)
[sic] ch.3 : le programme principal appelle `Proc Trier (T, n)` (p.100, p.105) alors que l'en-tête est `Trier (n : entier; VAR T : Tab)` (p.101, p.106).
III.1 (verbatim, extrait) : « […] en moyenne, il s'agit d'un algorithme d'ordre n² puisqu'il comporte deux boucles imbriquées d'ordre n chacune. Il est toutefois évident que si le vecteur est initialement presque trié dans le bon ordre, le nombre d'opérations sera beaucoup plus réduit. Si la méthode de tri par insertion est efficace quand la liste est à peu près triée, elle est inefficace en moyenne car elle ne change les valeurs que d'une position par instruction. »
III.2 Principe (verbatim) : « Donald L. Shell proposa, en 1959, une variante du tri par insertion. Ce tri consiste à trier séparément des sous-tableaux du tableau initial objet du tri, formés par les éléments répartis de p éléments. »
Encadré N.B. (verbatim) : « Le tri Shell est une amélioration du tri par insertion. Au lieu de faire une rotation de tous les éléments, nous ferons une rotation par pas de p ce qui permet d'affiner le tri du tableau et de faire moins de déplacements d'éléments. Nous commençons donc par un pas assez élevé et nous le diminuons au fur et à mesure jusqu'à arriver à un pas de 1. Ceci permet d'éliminer les plus grands désordres pour abréger le travail aux étapes suivantes. Le pas est diminué à l'aide d'une suite, mais il faut construire cette suite de manière à ce que les valeurs ne soient pas multiples entre elles sinon nous allons traiter des éléments et pas d'autres. »
Suite des pas (verbatim, indices rétablis d'après l'image) : « Shell propose la suite d'incréments vérifiant p₁ = 1, pₙ₊₁ = 3pₙ+1 en réalisant les tris du plus grand incrément possible vers le plus petit. D'autre part, puisque au dernier stade, p₀ [sic] est égal à 1, nous déterminerons le pas maximal par récurrence en inversant la relation donnée ci-dessus : pₖ₊₁ = 3 * pₖ + 1 et en s'assurant qu'il y a encore un nombre suffisant de composantes dans les sous-vecteurs considérés. »
Remarque (verbatim) : « Le tri Shell trie chaque liste d'éléments séparés de p positions chacun avec le tri par insertion. L'algorithme effectue plusieurs fois cette opération en diminuant p jusqu'à p égal à 1 ce qui équivaut à trier tous les éléments ensemble »

**Exemple (p.104–105, vérifié sur image)** — T de 15 éléments : [-5, 30, 0, -2, 42, 22, 9, -4, 10, 15, 40, -9, 12, 28, 14]. Étape 1 : pas maximal. Étape 2 : avec `p ← p Div 3`, pas successifs 13, 4, 1.
- p = 13 : sous-vecteur {1, 14} = (-5, 28) inchangé ; {2, 15} = (30, 14) → [-5, 14, 0, -2, 42, 22, 9, -4, 10, 15, 40, -9, 12, 28, 30].
- p = 4 : {1, 5, 9, 13} = (-5, 42, 10, 12) → [-5, 14, 0, -2, 10, 22, 9, -4, 12, 15, 40, -9, 42, 28, 30] ; {2, 6, 10, 14} = (14, 22, 15, 28) → [-5, 14, 0, -2, 10, 15, 9, -4, 12, 22, 40, -9, 42, 28, 30].
- Questions posées à l'élève (p.105) : indices du 3ème sous-vecteur et contenu de T après cette étape ; même question pour le 4ème.
- p = 1 : tri par insertion simple sur tout le tableau.
Encadré « Constatations » (p.105, verbatim) : « Il est bien évident que la dernière étape aurait pu suffire, puisqu'il s'agit d'un tri par insertion linéaire simple. Toutefois, dans le contexte où nous nous sommes progressivement placés, nous avons fait déplacer les grandes valeurs vers la fin du tableau et les petites vers le début. Le nombre de comparaisons dans le dernier passage sera très réduit et nous devrons déplacer moins souvent les éléments considérés. »

**Résolution (p.105–107)** — programme `Tri_Shell` (Saisir, Remplir, Trier, Afficher). Pas maximal par `p ← 0 ; Tant que (p < n) Faire p ← 3*p + 1`.
```
0) Début Procédure Trier (n : entier; VAR T : Tab)
1) p ← 0
   Tant que (p < n) Faire
     p ← 3*p + 1
   Fin Tant que
2) Tant que (p ≠ 0) Faire
     p ← p Div 3
     Pour i de p + 1 à n Faire
       valeur ← T[i]
       j ← i
       Tant que (j > p) ET (T[j-p] > valeur) Faire
         T[j] ← T[j-p]
         j ← j-p
       Fin Tant que
       T[j] ← valeur
     Fin pour
   Fin Tant que
3) fin Trier
```
Objets locaux : p (le pas), i, j (compteurs), valeur (variable intermédiaire). Pascal **non donné** : Activité p.107 « Traduisez la solution en un programme Pascal » (`Tri_Shel`).

#### IV.1 Application 1 — Tri par fusion (p.107–113)
Principe (verbatim) : « Il s'agit d'un tri suivant le paradigme "Diviser pour régner". Le principe est le suivant : 1- Nous divisons le tableau à trier en deux sous tableaux (en prenant par exemple, un élément sur deux pour chacun des sous tableaux). 2- Nous trions chacun d'entre eux. 3- Nous fusionnons les deux tableaux obtenus pour reconstituer le tableau trié. […] La fusion construit une liste triée à partir des deux listes triées. »
« étant donnés deux tableaux d'éléments triés, de longueurs respectives L1 et L2, il est facile d'obtenir un troisième tableau d'éléments triés de longueur L1+L2, par « interclassement » (ou fusion) des deux précédents tableaux. »
Remarque (verbatim) : « Nous constatons que la méthode de tri par fusion nécessite un tableau intermédiaire aussi grand que le tableau initial à trier et c'est là où réside le principal inconvénient car cela peut se révéler handicapant dans les situations où la place mémoire est restreinte. »
- **Exemple (p.108–109)** : T1 = [-5, -2, 0, 4, 6, 22, 40] (7), T2 = [-7, 0, 8, 8, 12, 28, 35, 39] (8) ; question : taille de T ? → 15. Étapes 1–3 : -7, -5, -2 placés. **Activité (p.109)** : terminer manuellement.
- **Résolution (p.109–113)** : énoncé « trier un tableau T de b entiers (5 ≤ b ≤ 100) » ; la solution fusionne en fait deux tableaux T1, T2 saisis déjà triés (programme `Tri_Fusion` : `Remplir (T1, n1)`, `Remplir (T2, n2)`, `Fusionner (T1, n1, T2, n2, T)`, `Afficher (T, n1+n2)`). `Remplir` : `Répéter Lire (m) Jusqu'à (m dans [5..100])`, puis `Lire (A[1])` et `Répéter Lire (A[c]) Jusqu'à (A[c] ≥ A[c-1])`. **Activité (p.111)** : que se passe-t-il si T1 est épuisé avant T2 ? → décomposition en 2 parties.
```
0) Début Procédure Fusionner (T1 : Tab; n1 : entier; T2 : Tab; n2 : entier; Var T : Tab)
1) c ← 0, c1 ← 1, c2 ← 1
2) Répéter
     c ← c+1
     Si (T1[c1] < T2[c2]) Alors
        T[c] ← T1[c1]
        c1 ← c1 + 1
     Sinon
        T[c] ← T2[c2]
        c2 ← c2 + 1
     Fin si
   Jusqu'à (c1 > n1) OU (c2 > n2)
3) Si (c1 > n1) Alors
      Pour i de c2 à n2 Faire
        c ← c+1
        T[c] ← T2[i]
      Fin Pour
   Sinon
      Pour i de c1 à n1 Faire
        c ← c+1
        T[c] ← T1[i]
      Fin Pour
   Fin Si
4) Fin Fusionner
```
  Activité : traduire en Pascal (`Tri_Fus1`). Variante à moins de paramètres (p.113), interclassement de T[début..mil] et T[mil+1..fin] via un tableau intermédiaire Temp :
```
0) Début Procédure Fusionner (début, mil, fin : entier ; Var T : Tab)
1) i ← début, j ← mil + 1
2) Pour k de début à fin Faire
     Si ((j > fin) ou ((i ≤ mil) ET (T[i] < T[j]))) Alors
        Temp[k] ← T[i]
        i ← i+1
     Sinon
        Temp[k] ← T[j]
        j ← j+1
     Fin Si
   Fin Pour
3) Pour k de début à fin Faire {copier le contenu de Temp dans T}
     T[k] ← Temp[k]
   Fin pour
4) Fin Fusionner
```
  Activité : traduire en Pascal (`Tri_Fus2`). Pascal non donné.

#### IV.2 Application 2 — Classement (p.113–117)
Énoncé : noms et moyennes de 30 élèves d'une classe 4SI ; afficher sous forme de tableau le rang de chaque élève. Demandes : structures de données, analyse. Choix proposés : tableau d'enregistrements `ELEVE` (Nom chaîne, Moyenne réel, Rang entier) ou trois tableaux parallèles ; retenu : tableau d'enregistrements `TAB_EL`. Programme `Traitement_EL` : `Saisir (TAB_EL)` (moyenne contrôlée dans [0, 20], via un enregistrement intermédiaire `Enreg`), `Rechercher_Rang (TAB_EL)`, `Afficher (TAB_EL)`. Principe du rang : initialiser à 1, puis +1 pour chaque élève ayant une moyenne supérieure (double boucle `Pour i de 1 à 30` / `Pour j de 1 à 30`).
```
0) Début Procédure Rechercher_Rang (Var TAB_EL : Tab)
1) Pour i de 1 à 30 Faire
     Enreg1 ← Tab_el[i]
     Enreg1.Rang ← 1
     Pour j de 1 à 30 Faire
       Enreg2 ← Tab_el[j]
       Si (Enreg1.Moy > Enreg1.Moy) [sic : l'analyse dit Enreg2.Moy > Enreg1.Moy]
       Alors Enreg1.Rang ← Enreg1.Rang + 1
       FinSi
     FinPour
   FinPour
2) Fin Rechercher_Rang
```
⚠ Tel qu'imprimé, `Enreg1` n'est jamais recopié dans `Tab_el[i]` : le rang calculé n'est pas stocké (lacune de la source, `[?]`, ne pas en faire une question « telle quelle »).

#### Retenons (p.118, verbatim, vérifié sur image)
« - **Tri par insertion :** Cet algorithme consiste à traiter une à une les valeurs du tableau et à les insérer, au bon endroit, dans le tableau trié constitué des valeurs précédemment traitées et triées. Les valeurs sont traitées dans l'ordre où elles apparaissent dans le tableau.
- **Tri Shell :** Ce tri, proposé en 1959 par Donald L. Shell, constitue une variante optimisée du tri par insertion. Le tri par insertion provoquait le décalage de tous les éléments plus grands que l'élément à insérer. Dans le tri Shell, les éléments ne sont pas décalés d'un élément à la fois, mais de plusieurs éléments, dont la différence d'indice est appelée "pas". Ainsi, à chaque étape, le tri est dégrossit [sic] puis le pas est réduit. Chaque réduction de pas provoque un affinage du tri.
- **Tri fusion :** La méthode "diviser pour régner" est tout à fait applicable au problème de tri par fusion. Plutôt que de trier le tableau complet, il est possible de trier deux sous tableaux de taille égale, puis de fusionner les résultats.
- **D'autres méthodes de tri** existent telles que le tri par comptage, tri par création, tri radix, tri rapide, tri par permutation, etc. »
Citation : « L'ordre conduit à toutes les vertus mais qu'est-ce qui conduit à l'ordre » — Georg Christoph Lichtenberg.

#### Exercices non corrigés (p.119–121) — difficulté : Ex.1-6 moyen (silhouettes, légende p.5) ; Ex.1–4 étiquetés « (Bac TP 2005) »
1. **Ex.1 (Bac TP 2005, p.119)** — Donnée : algorithme de `pos_min (A : tab ; p, k : entier) : entier` (position du plus petit élément de A à partir de p). Demande : programme Pascal saisissant T de n réels, tri croissant par sélection en utilisant `pos_min`, affichage.
2. **Ex.2 (Bac TP 2005, p.119–120)** — Donnée : `TRI_Bulles (Var T : Tab; n : entier)` : `Pour i de 1 à n-1`, `Pour j de 1 à n-i`, `Si (T[j] < T[j+1]) Alors Proc Permut (T[j], T[j+1])`. Demandes : (1) programme Pascal `Tri` saisissant p entiers dans V et appelant TRI_Bulles ; (2) en commentaire, ordre du tri (croissant/décroissant) ; (3) modifier TRI_Bulles pour éviter les parcours inutiles si V est déjà trié (aucune permutation).
3. **Ex.3 (Bac TP 2005, p.120)** — Programme `Tri` : trier T de N entiers distincts (5 < N < 20) en comptant pour chaque élément le nombre d'éléments inférieurs → position dans un tableau résultat R. Exemple : T = [6, 2, 0, 5, 12, 25, 13, 8, 14, 3] ; 4 valeurs inférieures à 6 → position 5 de R. Distinction non vérifiée par le candidat.
4. **Ex.4 (Bac TP 2005, p.120–121)** — Programme `Tri_permut` : tri croissant de T (5 < N < 20) en effectuant toutes les permutations possibles, en testant avant chaque permutation si T est ordonné, arrêt dès que T est trié ; donnée : procédure `Combinaisons (N : entier; var T : Tab)` (double boucle `Pour i de 1 à N` / `Pour j de 1 à N-1` : `Permut (T[j], T[j+1])`, `Affiche (T, N)`).
5. **Ex.5 (p.121)** — « Tri par rangement ou par création » : trouver le minimum local de la partie restant à trier, le mettre dans un vecteur résultat, recommencer. Demande : analyse modulaire si le vecteur initial peut être modifié / reste inchangé.
6. **Ex.6 (p.121)** — Analyse modulaire récursive, algorithmes, programme Pascal `Fus_Rec` : tri par fusion récursif.
(Application p.102 : tri par insertion récursif ; activités p.96–97 : sélection et bulles en Pascal ; p.107 / p.113 : Pascal du Shell et des deux Fusionner.)

#### Vocabulaire officiel
tri ; ordre croissant / décroissant / alphabétique ; ordre total ; tris internes / tris externes ; tri par sélection ; tri à bulles (bubble sort) ; permutation ; valeurs adjacentes ; tri par insertion (linéaire) ; variable intermédiaire Tmp ; décalage (procédure DECALER) ; position d'insertion ; tri Shell ; pas, suite d'incréments, sous-vecteur / sous-tableau ; « algorithme d'ordre n² » ; tri par fusion, fusion / interclassement, « Diviser pour régner », tableau intermédiaire ; tableau d'enregistrements, rang ; tri par comptage, par création (rangement), radix, rapide, par permutation.

#### Notions testables — 8 (découpage proposé en 2 sous-chapitres si besoin : « insertion & Shell » / « fusion, classement & autres tris »)
1. Définition du tri ; tris internes (mémoire centrale, tableaux) vs externes (fichiers, grandes masses).
2. Tri par sélection (rappel 3ème) : principe (placer le minimum de T[i..N] en i, N-1 étapes), trace ; `pos_min`.
3. Tri à bulles (rappel) : comparaisons adjacentes, plus grand en fin après un passage, au pire n passages, ordre selon le test (Ex.2 : `T[j] < T[j+1]` → décroissant — déduction du transcripteur, exercice non corrigé), arrêt sans permutation.
4. Tri par insertion : principe, rôle de Tmp, décalage à droite, `T[p+1] ← Tmp`, trace sur le tableau à 7 éléments, n-1 étapes pour n éléments [à confirmer : le manuel pose la question sans répondre], variante dichotomique, efficace sur liste presque triée, ordre n² en moyenne.
5. Tri Shell : variante améliorée de l'insertion (Shell, 1959) ; suite `p ← 3*p + 1` jusqu'à `p ≥ n`, puis `p ← p Div 3` ; pas 13, 4, 1 pour n = 15 ; trace par sous-vecteurs ; dernier passage = insertion simple.
6. Fusion / interclassement de deux tableaux triés : taille L1+L2, trace, copie du reste, tableau intermédiaire (inconvénient mémoire), « diviser pour régner ».
7. Classement : rang = 1 + nombre d'élèves de moyenne strictement supérieure ; tableau d'enregistrements vs tableaux parallèles.
8. Tri par comptage / position (Ex.3 : position = nombre d'éléments inférieurs + 1) et tri par rangement (Ex.5) ; reconnaître les noms de méthodes (Retenons, Lecture).

#### Bornes
- ✅ INCLUS : sélection et bulles (rappels, principe + exercices Bac TP 2005) ; insertion (algorithme + Pascal) ; Shell (algorithme, suite 3p+1) ; fusion de deux tableaux triés (deux versions) et tri par fusion récursif (exercice) ; classement par rang ; tri par comptage de position, tri par rangement/création (exercices) ; insertion récursive (application) ; ordre n² cité pour l'insertion.
- ⛔ EXCLU : tri rapide (Quicksort), tri radix, tri par arbre binaire, tri cocktail, tri de Batcher, tri polyphase (cités seulement, Retenons/Lecture) ; calcul formel de complexité (seule mention « ordre n² ») ; tris externes sur fichiers (définis, non traités) ; autres suites de pas que 3p+1 ; stabilité d'un tri (non abordée).

#### Lecture (p.122) — résumé
« Les tris » (source www.chez.com/algo/tri/) : taxonomie. Tris internes — par insertion (insertion linéaire, insertion en double sens, Shell, arbre binaire) ; par échange (bulle, cocktail shaker, méthode de K.E. Batcher, Quicksort) ; par sélection, par fusion, par distribution. Tris externes — tri polyphase.

#### Note de lecture ch.3
- Pages lues couche texte : 95–122 (28 p.). Pages sondées image : 99, 103, 104, 105, 106, 107 (section III Shell entière après écart à p.103), 116, 118, 122.
- Écarts texte↔image : (1) p.103 — indices et exposants aplatis en L1 (`n2` = n², `p1 = 1, pn+1 = 3pn+1` = p₁ = 1, pₙ₊₁ = 3pₙ+1, `p0`, `pk + 1 = 3 * pk + 1`) ; (2) p.104/106 — idem `pk+1 = 3 * pk + 1` ; cases modifiées des tableaux surlignées en couleur (perdu en L1, valeurs identiques). Aucun écart de valeurs dans les tableaux de traces (p.99, p.104).
- Coquilles `[sic]` : « habilités » (p.95) ; « qui précédent » (p.97) ; « DECLARER » pour DECALER (p.101–102, table et titres d'analyse) ; Shell : l'analyse écrit `Pour i de p à n` et `T[c-p], T[c-2*p]` alors que l'algorithme écrit `Pour i de p + 1 à n` et utilise j (p.106) ; titre « b) Algorithme du programme principal » pour la procédure Trier du Shell (p.106) ; « p₀ est égal à 1 » vs p₁ = 1 (p.103) ; Fusionner, analyse partie 2 : `T[c] ← T2[i]; c ← c+1` (ordre inverse de l'algorithme) et commentaire « {copier le reste des éléments de T2} » sur la boucle de T1 (p.112) ; « Temps » pour Temp dans la table (p.113) ; « intérmédiaire(s) » (p.113–117) ; « efféctuée », « condition d'arrê » (p.109–110) ; Rechercher_Rang `Si (Enreg1.Moy > Enreg1.Moy)` (p.116, confirmé sur image) ; phrases d'enchaînement inversées « Détaillons maintenant l'analyse de la procédure Afficher » / « … Rechercher_Rang » (p.115–116) ; table des objets d'Afficher listant « i, j » alors que seul i sert (p.117) ; « dégrossit » (p.118) ; énoncé IV.1.3 « tableau T de b entiers » alors que la solution fusionne T1 et T2 (p.109).
- Doutes `[?]` : Shell — après p = 1, la boucle fait un dernier passage avec p = 0 (sans effet) ; le manuel annonce les pas « 13, 4 et 1 » : s'en tenir à cette liste. Nombre d'étapes de l'Activité p.99 : non donné par le manuel. Rechercher_Rang : rang non réécrit dans Tab_el (voir plus haut).

---

## Fiche de lecture ch.2-3
- **pagesLues** : 73–122 (50 pages, couche texte L1 `pdftotext -layout`, une fois chacune).
- **Pages sondées (image, pdftoppm)** : 74, 75, 76, 77, 78, 79, 80, 89, 90, 99, 103, 104, 105, 106, 107, 116, 118, 122 — 18 pages (36 %), dont deux sections sondées entièrement après écart (ch.2 §I p.74–80 ; ch.3 §III p.103–107).
- **Nombre d'écarts texte↔image : 5** (p.75 partie colorée des formules ; p.80 vignettes du cube fractal ; p.90 dessins de l'Ex.1 d ; p.103 indices/exposants aplatis ; p.104/106 indices de la suite des pas + surlignage des cases modifiées). Aucun écart portant sur une valeur, un mot ou une ligne de code.
Source unique : manuel élève CNP « Algorithmique et programmation », 4ème année secondaire, Sciences de
l'informatique (248 p.). Décalage PDF ↔ page imprimée : 0. Aucun guide enseignant.
Méthode : couche texte L1 (`pdftotext -layout`) page par page, puis sondage image (110 dpi). Des écarts
texte↔image ayant été constatés dès le premier sondage dans chaque chapitre, **les deux sections ont été
sondées en entier** (64/64 pages vues en image). Toutes les formules, encadrés et algorithmes ci-dessous
sont vérifiés sur l'image.

Conventions : `←` affectation (notation du manuel) ; `[sic]` = coquille/incohérence du manuel conservée ;
`[?]` = doute ; « Remarque du transcripteur » = observation hors texte, à ne pas reprendre comme contenu
officiel. Pictogrammes : le manuel n'affiche ni étoiles ni code couleur ; sa légende p.5 définit quatre silhouettes de difficulté (rattachement non relevé ici `[?]`) ; il place une petite icône devant chaque énoncé. Trois icônes distinctes
reviennent, notées ici : **[P?]** personnage tête dans la main + « ? » ; **[P♪]** personnage avec « ? » et
notes de musique ; **[PR]** personnage « à rayons » (traits autour de la tête). Le rattachement des icônes de ces chapitres à la
légende p.5 n'a pas été relevé `[?]` : ne pas en déduire un niveau.

---

### Chapitre 4 — Les algorithmes récurrents (p.123–150)

#### Plan (p.123)
| § | Titre | Pages |
|---|---|---|
| — | Page de garde (objectifs + plan) | 123 |
| I | Introduction (définition, ordre 1/2/3/p) | 124 |
| II | Calcul de somme (Activité 1 : somme d'une matrice carrée) | 124–125 |
| III | Algorithme récurrent sur les chaînes (Activité 2 : suite de Thue-Morse) | 126–129 |
| IV | Triangle de Pascal (Activité 3 : solution itérative puis récursive) | 129–136 |
| V | La suite de Fibonacci (récit des lapins, Activité 4 : 3 solutions) | 136–139 |
| VI | Le nombre d'or (Activités 5 et 6) | 139–142 |
| — | Retenons | 143 |
| — | Exercices (10) | 144–147 |
| — | Lecture (Fibonacci ; historique du nombre d'or) | 148–150 |

#### Objectifs officiels (p.123, verbatim)
- « Acquérir des habilités [sic] de résolution de problèmes à travers l'apprentissage des algorithmes numériques. »
- « Proposer des solutions à quelques problèmes récurrents. »

#### Encadrés de cours (verbatim)

**Introduction (p.124)**
> Un algorithme ou un traitement est dit **récurrent** s'il utilise un procédé itératif ou récursif pour
> engendrer un résultat qui peut dépendre de p résultats précédents, nous parlons alors d'un algorithme ou
> d'un traitement **récurrent d'ordre p.**
> Ordre 1 : Un algorithme récurrent d'ordre 1 est un algorithme donnant un résultat dépendant du résultat précédent.
> Ordre 2 : Un algorithme récurrent d'ordre 2 est un algorithme donnant un résultat dépendant des deux résultats précédents.
> Ordre 3 : Un algorithme récurrent d'ordre 3 est un algorithme donnant un résultat dépendant des trois résultats précédents.
> Ordre p : Un algorithme récurrent d'ordre p est un algorithme donnant un résultat dépendant des p résultats précédents.

**Principe du Triangle de Pascal (énoncé de l'Activité 3, p.129)**
> Pour une ligne donnée :
> Le premier et le dernier éléments sont égaux à 1,
> Les autres éléments sont déterminés en appliquant la formule suivante :
> MAT [ligne, colonne] = MAT [ligne-1, colonne] + MAT [ligne-1, colonne-1]

**Suite de Fibonacci (p.137)**
> La suite de Fibonacci est une suite récurrente dont chaque élément obéit à la relation de récurrence
> suivante : **Un = Un-1 + Un-2**
> avec **U1 = 1 et U2 = 1**
> Donc c'est une suite récurrente d'ordre 2.

**Nombre d'or (p.140)**
> La suite (Vn) définie sur N* par Vn = Fib(n+1) / Fib(n) semble converger vers λ = (1+ √5) / 2 appelé
> nombre d'or, dont une valeur approchée est 1,618.
> **Définition et valeur du nombre d'or**
> Le nombre d'or est la solution positive de l'équation : x² - x - 1 = 0
> C'est à dire le nombre (1+ √5) / 2

(Le manuel désigne le nombre d'or par « λ (phi) » [sic : lettre lambda imprimée, nommée phi], p.140 et p.149-150.)

**Retenons (p.143, verbatim)**
> - Un algorithme ou un traitement est dit récurrent, s'il utilise un traitement itératif ou récursif pour
>   engendrer un résultat qui peut dépendre de p résultats précédents.
> - Un algorithme récurrent d'ordre 1 est un algorithme dont un résultat dépend du résultat précédent.
> - Un algorithme récurrent d'ordre 2 est un algorithme dont un résultat dépend des deux résultats précédents.
> - Un algorithme récurrent d'ordre 3 est un algorithme dont un résultat dépend des trois résultats précédents.
> - Un algorithme récurrent d'ordre p est un algorithme dont un résultat dépend des p résultats précédents.

#### Activités et solutions rédigées (corrigées dans le manuel)

**Activité 1 — Somme d'une matrice (p.124-125)** [icône penseur]
- Énoncé : somme des éléments d'une matrice carrée d'entiers d'ordre n (4 ≤ n ≤ 20). Q1 : le traitement
  est-il récurrent, quel ordre ? Q2 : analyse puis algorithme de la fonction SOMME_MAT.
- Réponse du manuel : cumul dans S initialisé à 0 ; « Puisque ce traitement fait toujours référence à
  l'élément précédent, donc c'est un **traitement récurrent d'ordre 1**. »
- Algorithme (verbatim) :
```
0) Début fonction SOMME_MAT (M : MAT ; N : Entier non signé) : Entier
1) S ← 0
   Pour ligne de 1 à N Faire
        Pour colonne de 1 à N Faire
              S ← S + M [ligne, colonne]
        Fin Pour
   Fin Pour
2) SOMME_MAT ← S
3) Fin SOMME_MAT
```
- TDOL : S Entier (variable de cumul), Ligne, Colonne Entier (compteurs).
- Pascal (verbatim) :
```pascal
FUNCTION SOMME_MAT (M : MAT; N : Word) : Integer ;
VAR       S, ligne, colonne : Integer ;
Begin
      S := 0;
      For ligne := 1 To N Do
              For colonne := 1 To N Do
                                S := S + M[ligne, colonne] ;
        SOMME_MAT := S ;
End;
```

**Activité 2 — Suite de Thue-Morse (suites de chaînes de caractères) (p.126-129)** [icône penseur]
- Donnée : sur les chaînes de 0 et 1 (« chaînes ou mots binaires »), remplacer chaque "0" par "01" et
  chaque "1" par "10", en partant de "0" : U0 → "0", U1 → "01", U2 → "0110", U3 → "01101001",
  U4 → "0110100110010110".
- Demande : Q1 ordre de récurrence ; Q2 analyse + algorithmes pour calculer et afficher le Nème terme à
  partir d'un caractère A ("0" ou "1") ; Q3 traduire, tester, enregistrer sous **Thue_Morse**.
- Réponse : « une suite récurrente d'ordre 1 ».
- Programme principal : `0) Début Suite_Thue_Morse  1) Proc Saisie (N, A)  2) Ecrire ("La suite de
  Thue-morse à partir de ", A, " Est ", FN Thue_Morse (N, A))  3) Fin Suite_Thue_Morse`. TDOG : N Entier non
  signé (« Ordre du terme à calculer »), A Caractère ("0" ou "1"), Thue_Morse Fonction.
- Algorithme de la fonction (verbatim) :
```
0) Début Fonction Thue_Morse (N : Entier non signé ; A: Caractère) : Chaîne
1) CH ← A
   Pour i de 1 à N Faire
          j ← 1
          Répéter
                 Si CH[j] = "0" Alors insère ("1", CH, j+1)
                                Sinon insère ("0", CH, j+1)
                 Fin Si
                 L ← Longueur (CH)
                 j ← j + 2
          Jusqu'à j > L
   Fin Pour
2) Thue_Morse ← CH
3) Fin Thue_Morse
```
- TDOL : j, i Entier non signé (compteurs) ; CH Chaîne ; L Entier non signé (longueur de la chaîne).
- Pascal : Saisie avec `Repeat … Until N In [2 .. 100]` et `Until A In ['0', '1']` ; fonction :
```pascal
FUNCTION Thue_Morse (N: Word; A : Char ) : String ;
VAR   Ch : String ;
      i, j, L : Word ;
Begin
      Ch := A ;
      For i := 1 To N Do
      Begin
            j := 1 ;
            Repeat
                   If Ch [j] = '0' Then Insert ('1', Ch, j+1)
                   Else Insert ('0', Ch, j+1);
                   L := Length (Ch) ;
                   j := j+ 2;
            Until j > L ;
      End;
      Thue_Morse := Ch ;
End;
```
- Remarque du transcripteur : la saisie accepte N jusqu'à 100 alors qu'un String Pascal plafonne à 255
  caractères (la longueur double à chaque itération) ; le manuel ne le signale pas. Ne pas bâtir de
  question sur un N > 7.

**Activité 3 — Triangle de Pascal (p.129-136)** [icône penseur]
- Énoncé : afficher les n premières lignes du Triangle de Pascal (2 ≤ n ≤ 100) [sic : la solution fixe
  Max = 20 et saisit N dans [3..max]]. Exemple de 5 lignes : 1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1.
- Questions : 1- traitement récurrent ? « donnez son rang » [sic : ordre] ; 2- analyse itérative ;
  3- algorithmes ; 4- analyse récursive ; 5- algorithmes.
- Réponse 1 (p.130) : figures n = 3 (MAT[3,2] = MAT[2,2] + MAT[2,1]) et n = 5 (MAT[5,4] = MAT[4,4] +
  MAT[4,3]) ; « C'est un traitement récurrent d'ordre 2. »
- **Solution itérative** : PP `Saisir (N) / Remplir_MAT (N, MAT) / Afficher_Triangle (N, MAT)`. TDNT :
  `Matrice = Tableau de max lignes et max colonnes d'entiers`. TDOG : Max Constante = 20, N Entier non signé,
  MAT Matrice, Saisir / Remplir_MAT / Afficher_Triangle Procédures.
```
0) Début procédure Remplir_MAT (N : Entier; VAR MAT : Matrice);
1) MAT [1,1] ← 1
2) MAT [2,1] ← 1
3) MAT [2,2] ← 1
4) Pour ligne de 3 à N Faire
      MAT [ligne, 1] ← 1
      MAT [ligne, ligne] ← 1
      Pour colonne de 2 à ligne-1 Faire
         MAT [ligne, colonne] ← MAT [ligne-1, colonne] + MAT [ligne-1, colonne-1]
      Fin Pour
   Fin Pour
5) Fin Remplir_MAT

0) Procédure Afficher_Triangle (n : Entier non signé ; mat : matrice)
1) Pour ligne de 1 à N Faire
      Ecrire ( )                         {avec retour à la ligne}
      Pour colonne de 1 à ligne Faire
           Ecrire (Mat [ligne, colonne]," ")   {sans retour à la ligne}
      FinPour
   FinPour
2) Fin Afficher_Triangle
```
  Pascal complet p.133-134 (`const Max = 20; TYPE Matrice = ARRAY[1.. max, 1.. max] Of Integer;`, Saisir
  `Until N In [3.. max]`, affichage `Write(Mat [ligne, colonne]:2,'   ')`).
- **Solution récursive** (p.134-136) : PP identique avec `Remplir_Triangle` ; appel
  `Mat [ligne, colonne] ← FN Val_Triangle (colonne, ligne)` pour ligne de 1 à n, colonne de 1 à ligne.
```
0) Fonction Val_Triangle (x, y : Entier) : Entier
1) Si (x = 1) OU (y = x) Alors Val_Triangle ← 1
   Sinon Val_Triangle ← FN Val_Triangle (x, y-1) + FN Val_Triangle (x - 1, y - 1)
   Finsi
2) Fin Val_Triangle
```
```pascal
FUNCTION Val_Triangle (x, y : Integer) : Integer ;
Begin
 If (x = 1) OR (y = x) Then Val_Triangle := 1
 Else Val_Triangle := Val_Triangle (x, y-1) + Val_Triangle (x-1, y-1) ;
End;
```
  [sic] p.135 : l'analyse dit « selon la ligne (x) et la colonne (y) » alors que l'appel passe
  (colonne, ligne) et que la suite du texte parle de « la colonne x et de la ligne y-1 » : x = colonne,
  y = ligne. p.136 : « procédures Saisie [sic : Saisir] et Afficher_Triangle ».

**Suite de Fibonacci — récit (p.136-137)** : schéma des couples de lapins saison 1 à 7 (couple jeune ○,
couple adulte ●, « donne naissance à… ») ; suite 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ;
rapports (image) : 21/13 ≅ 1,615 ; 34/21 ≅ 1,619 ; 144/89 ≅ 1,617 ; 610/377 ≅ 1,618 ; justification de
Un = Un-1 + Un-2 (adultes de la saison n-1 + jeunes = adultes de la saison n-2).

**Activité 4 — n-ième terme de Fibonacci (p.137-139)** [icône penseur] « suite de Fibonnaci » [sic]
- Demande : 1) FIBO_IT1 itérative sans tableau ; 2) FIBO_IT2 itérative avec tableau ; 3) FIBO_REC récursive.
```
0) Début fonction FIBO_IT1 (N : Entier) : Entier
1) u1 ← 1, u2 ← 1
   Si N ≤ 2 Alors F ← 1
   Sinon
      Pour i de 3 à N Faire
         F ← u1 + u2
         u1 ← u2
         u2 ← F
      Fin Pour
   Fin Si
2) FIBO_IT1 ← F
3) Fin FIBO_IT1

0) Début fonction FIBO_IT2 (N : Entier ; T : Tab) : Entier
1) T[1] ← 1, T[2] ← 1
   Si N ≤ 2 Alors F ← 1
   Sinon
      Pour i de 3 à N Faire
         T[i] ← T[i-1] + T[i-2]
      Fin Pour
      F ← T[n]
   Fin Si
2) FIBO_IT2 ← F
3) Fin FIBO_IT2

0) Début fonction FIBO_REC (N : Entier ) : Entier
1) Si N ≤ 2 Alors FIBO_REC ← 1
   Sinon FIBO_REC ← FN FIBO_REC (N-1) + FN FIBO_REC (N-2)
   Fin Si
2) Fin FIBO_REC
```
  Analyse récursive : « Cas particulier : Si N ≤ 2 alors FIBO_REC ← 1 » / « Cas général : Sinon FIBO_REC ←
  FN FIBO_REC (N-1) + FN FIBO_REC (N-2) ». [sic] l'analyse de FIBO_IT2 (p.138) omet le « Sinon » que
  l'algorithme contient. Pas de traduction Pascal pour l'Activité 4.

**Activité 5 — Tableau Fib(n+1)/Fib(n) (p.139)** [PR]
- Demande : compléter le tableau (n = 1 à 13, Fib(n) = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233)
  par Fib(n+1)/Fib(n) et sa valeur approchée ; « Que déduisez-vous ? ». Lignes fournies : 1 → 1 ; 2 → 2 ;
  3/2 → 1,5 ; 5/3 → 1,666 ; 8/5 → 1,6 ; 13/8 → 1,625 ; 21/13 → 1,615 ; lignes n = 8 à 13 vides.
- Réponse p.140 : convergence vers λ = (1+√5)/2 ≈ 1,618 ; « 100 premières décimales » 1,618 033 988 749 894
  848 204 586 834 365 638 117 720 309 179 805 762 862 135 448 622 705 260 462 189 024 497 072 072 041 [sic :
  30 groupes de 3 chiffres, soit 90 décimales imprimées et non 100 — ne pas en faire une question] ; suite présentée
  ici comme « 0, 1, 1, 2, 3, 5, … » [sic : départ 0 contre U1 = U2 = 1 plus haut] ; liste 1/0 = n'existe
  pas, 1/1 = 1, 2/1 = 2, 3/2 = 1,5, 5/3 = 1,6666…, 8/5 = 1,6, 13/8 = 1,625, 21/13 = 1,61538…,
  34/21 = 1,61904….

**Activité 6 — Nombre d'or à 10⁻⁴ près (p.141-142), « Bac pratique 2004 »** [icône penseur]
- Données : U1 = 1 et U2 = 2 ; Ui = Ui-1 + Ui-2 « pour U ≥ 3 » [sic : i ≥ 3] ; Vi = Ui / Ui-1 pour tout
  i ≥ 2. Vn approche le nombre d'or « avec une précision e dès que |Vn - Vn-1| < e ».
- Demande : programme Pascal **Nombre_Or** qui cherche Vn à 10⁻⁴ près et son rang.
- Corrigé Pascal : `TAB_E = ARRAY[1..1000] OF Integer ; TAB_R = ARRAY[1..100] OF Real` ; Init (U[1] := 1 ;
  U[2] := 2 ; i := 2) ; puis
```pascal
PROCEDURE Calcul (VAR u : TAB_E ; VAR V : TAB_R; VAR i : Integer);
BEGIN
  Repeat
       i := i+1;
       U[i] := U[i-1] + U[i-2];
       V[i] := U[i] / U[i-1];
  Until ABS(V[i] - V[i-1]) < 0.0001 ;
END;
```
  Affiche : `Writeln('Nbre d''or : ', V[i]); Writeln('Rang : ', i);` ; PP : Init (U) ; Calcul (U, V, i) ;
  Affiche (V, i). Remarque du transcripteur : V[2] n'est jamais affecté avant le premier test (i = 3) ; le
  manuel ne le relève pas.

#### Exercices (p.144-147) — non corrigés
| N° | Icône | Énoncé (données → demande) | p. |
|---|---|---|---|
| 1 | [PR] | V/F (cases à cocher). a. Un traitement récurrent d'ordre 1 fait référence : au premier / au dernier / à l'élément du milieu de la suite. b. Ordre 2 : « Au [sic] deux premiers » / « Au deux derniers » / à l'élément du milieu et à l'élément de fin. c. Que fait `A :='Fi' ; B :='bonacci' ; FIBO :=1 ; For i :=1 To LENGTH ( Copy (A+B,6,3) ) * 4 Do FIBO := FIBO * (i-1) + FIBO * (i-2) ;` : calcule un terme de Fibonacci / la somme des 12 premiers termes / une somme quelconque. | 144 |
| 2 | [P?] | Programme : somme des carrés des n premiers entiers impairs ; exemple n = 5 → « n = 5 , la suite est : 1² + 3² + 5² + 7² + 9² = 165. » | 144 |
| 3 | [P?] | Programme : triangle isocèle d'étoiles de N lignes (N au clavier) ; exemple 8 lignes (1, 3, 5, …, 15 étoiles centrées). | 145 |
| 4 | [P?] | Suite (xn), n ∈ N : x0 = a et xn+1 = 4xn (1 - xn) ; calculer xn en fonction de a et n donnés. | 145 |
| 5 | [P?] | « Calcul de la suite de Heron » : U0 = x ; Un+1 = (Un /2) + (x / 2Un), x réel positif ; calculer les n premiers termes. | 145 |
| 6 | [P♪] | Rappel : Random(i) renvoie un entier aléatoire entre 0 et i-1, RANDOMIZE initialise. Programme `mystere` donné (T : array[1..20001] rempli par 1+Random(20000) ; boucle Repeat/While cherchant le premier i tel que T[i] coïncide avec un T[S], S < i). 1/ contenu final de S et U ; 2/ rôle du programme ; 3/ vérifier l'hypothèse en ajoutant du code. | 145-146 |
| 7 | [P♪] | « Deux suites » : U0 = 1, Un+1 = (Un + Vn) / 2 ; V0 = 2, Vn+1 = √(Un+1 * Vn) ; suites adjacentes « de limite √27 /π » (tel qu'imprimé) ; lire n, afficher l'approximation de π obtenue à partir de Vn. | 146-147 |
| 8 | [P♪] | Fibonacci U1 = 1, U2 = 1, Un = Un-1 + Un-2 (pour N > 2) : calculer le Nème terme ; déterminer le rang N et la valeur du terme maximal calculable avec le type entier, puis entier long. | 147 |
| 9 | [P♪] | « Formule de Viète » : V0 = 0, Vn+1 = √((1+Vn)/2) ; U0 = 2, Un+1 = Un / Vn+1 ; « Vérifiez par un programme cette assertion. » [?] : l'assertion (limite de Un) n'est pas énoncée dans la page. | 147 |
| 10 | [P♪] | « Suite convergeant vers la racine de N » : U0 = N/2, Un+1 = (Un + N / Un) / 2, N entier naturel ; vérifier que la limite est √N ; calculer tant que \|Un+1 - Un\| > 10⁻⁶ ; afficher le nombre d'itérations. | 147 |

#### Vocabulaire officiel
algorithme / traitement récurrent ; récurrent d'ordre 1, 2, 3, p ; procédé itératif / procédé récursif ;
variable de cumul ; suite récurrente ; suite de Thue-Morse ; chaînes ou mots binaires ; Triangle de
Pascal ; cas particulier / cas général (récursivité) ; suite de Fibonacci ; nombre d'or ; converger ;
précision e ; rang ; solution itérative sans tableau / utilisant un tableau / solution récursive ;
tableau de codification des objets (globaux, locaux), des nouveaux types ; insère, Longueur (fonctions
prédéfinies en algorithmique) ; Insert, Length (Pascal).

#### Notions testables (8)
1. Définition d'un traitement récurrent et identification de son **ordre** (1, 2, 3, p) sur un exemple (somme, Thue-Morse, Pascal, Fibonacci).
2. **Calcul de somme / cumul** comme récurrence d'ordre 1 (SOMME_MAT, double boucle).
3. **Récurrence sur les chaînes** : Thue-Morse (règle de substitution, termes U0…U4, algorithme insère/pas de 2).
4. **Triangle de Pascal itératif** : formule MAT[l,c] = MAT[l-1,c] + MAT[l-1,c-1], bords à 1, ordre 2, trace d'un remplissage.
5. **Triangle de Pascal récursif** : Val_Triangle (condition d'arrêt x = 1 ou y = x).
6. **Fibonacci** : relation Un = Un-1 + Un-2, U1 = U2 = 1 ; trois versions (variables u1/u2, tableau T, récursive) ; trace/valeurs de termes.
7. **Nombre d'or** : Fib(n+1)/Fib(n) → (1+√5)/2 ≈ 1,618, solution positive de x² - x - 1 = 0 ; arrêt sur |Vn - Vn-1| < e (Bac pratique 2004).
8. **Suites numériques convergentes et condition d'arrêt de précision** (exercices : Héron, racine de N, x(n+1) = 4x(n)(1-x(n)), suites adjacentes, Viète, débordement entier/entier long).

#### Bornes
- ✅ INCLUS : définitions et ordre ; somme matricielle ; Thue-Morse ; Triangle de Pascal itératif et récursif ;
  Fibonacci (3 solutions, algorithme ; Pascal seulement pour le Triangle, Thue-Morse, SOMME_MAT, Nombre_Or) ;
  nombre d'or (définition, valeur approchée, équation, programme à 10⁻⁴) ; suites des exercices
  (Héron, racine de N, logistique 4x(1-x), suites adjacentes, Viète, somme des carrés d'impairs, triangle
  d'étoiles, limites de types entier / entier long, Random/Randomize).
- ⛔ EXCLU (absent du chapitre) : démonstrations mathématiques de convergence ; complexité / coût de la
  récursivité ; formule de Binet ; suites arithmétiques et géométriques en tant que notions ; tout
  algorithme d'arithmétique (ch.5). La lecture historique (dates, Phidias, Kheops…) n'est pas du programme
  testable.

#### Page « Lecture » (p.148-150), résumé
- « Leonardo Pisano » (d'après techno-science.net) : Fibonacci (Pise, v. 1170 - v. 1250), dit Léonard de
  Pise ou Leonardo Bigollo, de son vrai nom Leonardo Guilielmi ; éduqué en Afrique du Nord (son père gérait
  les marchés de Pise en Algérie, Tunisie, Maroc) ; *Liber Abaci* (1202, « Le livres [sic] des calculs »)
  introduit en Europe la notation indienne / chiffres arabes ; Florence interdit les chiffres arabes aux
  banquiers en 1280 ; « cifra » = « code secret » ; le nom « fils de Bonacci » est posthume.
- « Un petit historique du nombre d'or » (d'après trucsmaths.free.fr) : notation λ (phi) [sic] en hommage
  à Phidias, introduite par Théodore Cook (1914) ; jalons : pyramide de Khéops, Parthénon, Euclide
  (« extrême et moyenne raison »), Pacioli *De divina proportione* (1498), Zeising, Ghyka, Le Corbusier
  (Modulor, 1945). « Où rencontre-t-on le nombre d'or » : rapport hauteur/demi-base de Khéops, rectangle
  doré du Parthénon (DC/DE = λ, GF/GI = λ, rectangle GBFH « rectangle Parthénon ») ; ton sceptique
  (« Et s'il avait [sic] cherché 2, l'auraient-ils trouvé ?? »). Illustration « L'amour vache, Géricault ».

#### Note de lecture — ch.4
- Pages lues (texte) : 123-150 (28). Pages sondées en image : 123-150 (28/28 — sondage étendu à toute la section après écarts).
- Écarts texte↔image (9 pages) : p.124 et p.129 « ≤ » rendu « ) » (« 4 ) n ) 20 », « 2 ) n ) 100 ») ;
  p.137 rapports de Fibonacci permutés par la couche texte (texte : 34/21 ≅ 1,617, 610/377 ≅ 1,619,
  144/89 ≅ 1,618 ; image : 34/21 ≅ 1,619, 144/89 ≅ 1,617, 610/377 ≅ 1,618) ; p.137-139 exposants « ème »
  aplatis ; p.140 fraction Fib(n+1)/Fib(n) et √5 éclatés, x² rendu « x2 » ; p.141 « ≥ » rendu « * »
  (« U * 3 », « i * 2 ») et 10⁻⁴ rendu « 10-4 » ; p.144 exposants des carrés perdus (« 12 + 32 + … ») ;
  p.145 indices xn, Un aplatis ; p.146 portée de la racine de Vn+1 perdue ; p.147 formule de Viète
  (Vn+1 = √((1+Vn)/2)) absente de la couche texte, 10⁻⁶ rendu « 10-6 ».
- Coquilles / incohérences [sic] : « habilités » (objectifs) ; « donnez son rang » (Act. 3) ; « 100 premières
  décimales » pour 90 imprimées (p.140) ; bornes
  2 ≤ n ≤ 100 vs Max = 20 et N ∈ [3..max] ; « ligne (x) et colonne (y) » vs appel (colonne, ligne) ;
  « Saisie » pour Saisir (p.136) ; « Fibonnaci » (Act. 4) ; « Sinon » manquant dans l'analyse de FIBO_IT2 ;
  suite débutant par 0 (p.140) vs U1 = U2 = 1 ; « λ (phi) » ; « pour U ≥ 3 » (Act. 6) ; « Au deux » (Ex. 1) ;
  « Le livres des calculs », « s'il avait cherché » (Lecture).
- Doutes [?] : Ex. 9, assertion non énoncée ; Ex. 7, limite imprimée « √27 /π » reprise telle quelle (non vérifiée mathématiquement).

---

### Chapitre 5 — Les algorithmes d'arithmétique (p.151–186)

#### Plan (p.151)
| § | Titre | Pages |
|---|---|---|
| — | Page de garde (objectifs + plan) | 151 |
| I | Préambule | 152 |
| II | Calcul du PGCD (solution récursive) — II.1 Activité 1 ; II.2 Application | 152–154 |
| III | Calcul de Aⁿₚ et Cⁿₚ (notés A(n,p), C(n,p) ci-dessous) — III.1 Présentation ; III.2 Calcul de A (Activité 1) ; III.3 Calcul de C (Activité 2) ; III.4 Application (C récursif) | 154–159 |
| IV | Quelques règles de divisibilité — IV.1 Définitions ; IV.2 par 3 ; IV.3 par 4 ; IV.4 par 5 ; IV.5 autres règles | 159–166 |
| V | Conversions entre bases de numération — V.1 Définition ; V.2 Exemples de bases (+ Activité décimal→binaire) ; V.3 hexadécimal→binaire ; V.4 octal→décimal ; V.5 binaire→octal ; V.6 base B1→base B2 | 166–180 |
| — | Retenons (+ citation) | 181 |
| — | Exercices (16) | 182–185 |
| — | Lecture (Quelques règles de divisibilité) | 186 |

(Notation : le manuel écrit A^p_n et C^p_n — p en exposant, n en indice ; on écrit ici A(n,p) et C(n,p).
Attention : la Présentation p.155 écrit « A(2,3) = 6 » et « C(2,3) = 3 » avec l'ordre (p, n), alors que les
affichages des programmes utilisent « A(n, p) » et « C(n,p) » [sic].)

#### Objectifs officiels (p.151, verbatim)
- « Acquérir des habilités [sic] de résolution de problèmes à travers l'apprentissage des algorithmes de calcul numérique, »
- « Proposer des solutions récursives à quelques problèmes arithmétiques. »

#### Préambule (p.152), résumé
Arithmétique : branche des mathématiques qui étudie les relations entre les nombres ; étymologie grec
*arithmétiké* (arithmos : nombre ; techné : art), latin *arithmetica* ; base 2 universelle pour les
ordinateurs, base 12 pour les heures, base 60 pour angles et durées. « Exemples d'études arithmétiques » :
test de primalité, nombres parfaits, test de parité, somme de puissances, calcul de la factorielle,
calcul de PGCD et PPCM (simple liste — seul le PGCD est traité ici).

#### Encadrés de cours (verbatim)

**Relation récursive du PGCD (p.153)**
> Si a = b alors PGCD (a, b) = a
>   Sinon si a > b alors PGCD (a, b) = PGCD (a-b, b)
>   Sinon PGCD (a, b) = PGCD (a, b-a).

**Présentation de la combinatoire (tableau p.155, image)**
| COMBINATOIRE DE P OBJETS PARMI N — Exemple : p = 3 et n = 5 | | | |
|---|---|---|---|
| PERMUTATIONS | Ordre | Per = p! | 6 |
| ARRANGEMENTS | Ordre | A = n! / (n-p)! | 60 |
| COMBINAISONS | Sans ordre | C = A/P = n!/(n-p)!p! | 10 |
> **Arrangement de p éléments parmi n** : C'est le nombre de permutations ordonnées possibles de p éléments
> parmi n. Exemple avec {a,b,c}: A(2,3) = 6 — {a,b}, {b,a}, {a,c}, {c,a}, {b,c}, {c,b}
> **Combinaison de p éléments parmi n** : C'est le nombre de permutations sans ordre possibles de p éléments
> parmi n. Exemple avec {a,b,c}: C(2,3) = 3 — {a,b}, {a,c}, {b,c}

**Arrangements (Activité 1, p.155)**
> Un arrangement de p éléments d'un ensemble E à n éléments est un p-uplet d'éléments distincts de E.
> Le nombre d'arrangements de p éléments de l'ensemble E est représenté par la notation suivante :
> A^p_n = n(n-1)(n-2)…(n-p+1)   Ou encore   A^p_n = n! / (n-p)!
> n et p sont des entiers qui vérifient la condition suivante : 1 ≤ p ≤ n

**Combinaisons (Activité 2, p.157)**
> Une combinaison de p éléments d'un ensemble E de n éléments est une partie de E formée par p éléments.
> Le nombre de combinaisons de p éléments de l'ensemble E est représenté par la notation suivante :
> C^p_n = A^p_n / p! = n! / (p!(n-p)!)
> n et p sont des entiers qui vérifient la condition suivante : 0 ≤ p ≤ n

**Relation récursive de C (III.4, p.159)**
> Si p = 0 ou p = n alors C^p_n = 1
> Sinon C^p_n = C^(p-1)_(n-1) + C^p_(n-1)

**Divisibilité (p.159-160, 163-166)**
> IV.1 Un entier n est **divisible** par un entier m, si le reste de la division euclidienne de n par m est nul.
> Une règle **de divisibilité** est une séquence d'opérations simples qui permet de reconnaître rapidement si
> un entier est divisible par un autre sans qu'il soit nécessaire d'effectuer la division. Ces règles sont
> généralement applicables pour les grands nombres.
> **Conclusion** (par 3) : Un entier est divisible par 3, si la somme des chiffres qui le composent est divisible par 3.
> (par 4) Un entier est divisible par 4, si le nombre composé des deux derniers chiffres est divisible par 4.
> (par 5) Un entier est divisible par 5, si son chiffre des unités est égal à 0 ou à 5.
> (par 2) Un entier est divisible par 2, si son chiffre des unités est divisible par 2.
> (par 9) Un entier est divisible par 9, si la somme de ses chiffres est divisible par 9.
> (par 10) Un entier est divisible par 10, si son chiffre des unités est égal à 0.
> (par 25) Un entier est divisible par 25, si le nombre composé des deux derniers chiffres est divisible par 25…

Exemples du manuel : 6287 non divisible par 4 (87), 4120 divisible (20 = 5 x 4) ; 6287 non divisible par 5
(7 ∉ {0, 5}), 4120 (0 ∈ {0, 5}) et 3635 (5 ∈ {0, 5}) divisibles ; 5287 non divisible par 2, 136 et 94618
divisibles.

**Systèmes de numération (V.1-V.2, p.166)**
> Un **système de numération** est une méthode de comptage fondée sur une base de numération qui est un
> entier supérieur ou égal à 2. Soit N une base de numération, le système sera doté de N chiffres allant de 0 à N-1.
> Base 2 : … représenter les nombres avec 2 chiffres. Les chiffres utilisés sont 0 et 1.
> Base 8 : Dans le système octal, seuls les chiffres 0, 1, 2, 3, 4, 5, 6 et 7 sont utilisés pour coder un triplet de bits.
> Base 10 : … 10 symboles : 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9. C'est le système couramment utilisé.
> Base 16 : Les nombres binaires étant de plus en plus longs, il a fallu introduire une nouvelle base : la
> base hexadécimale. … Les chiffres utilisés sont 0, 1, …, 9, ainsi que les lettres A, B, C, D, E et F pour
> représenter respectivement les valeurs de 10, 11, 12, 13, 14 et 15.

**Principes de conversion (exemples résolus, images)**
- Hex → bin (p.168) : 29AF → 2 = 0010, 9 = 1001, A = 1010, F = 1111 ; « Chaque chiffre de n sera représenté
  sur 4 bits » ; résultat **10100110101111** ; « un chiffre hexadécimal correspond à 4 bits. Il suffit donc,
  de convertir un à un chaque chiffre hexadécimal en binaire et de les mettre les uns à la suite des autres. »
- Oct → déc (p.172) : 175 → 1 * 8² + 7 * 8¹ + 5 * 8⁰ ; « Le nombre décimal obtenu est : 125 ».
- Bin → oct (p.175) : 1110101 découpé depuis la droite : 1ère partie 101 → 1*2² + 0*2¹ + 1*2⁰ = 5 ;
  2ème partie 110 → 1*2² + 1*2¹ + 0*2⁰ = 6 ; 3ème partie (bits restants) 1 → 1*2⁰ = 1 ; « Le nombre octal
  obtenu est : 165 ».
- Valeur d'une lettre hexadécimale (p.170) : « Code Ascii de la lettre - 55 » ; « A = Ord('A') - 55 = 65 - 55 = 10 ».

**Retenons (p.181, verbatim)**
> - Le PGCD de deux entiers positifs non nuls a et b est le Plus Grand Commun Diviseur. Parmi les méthodes
>   utilisées pour rechercher le PGCD, nous citons la méthode de la différence.
> - Le nombre d'arrangements dans un ensemble de n éléments noté A^p_n est égal à n! / (n-p)!
> - Le nombre de combinaisons de p éléments parmi n noté C^p_n est égal à n! / (p! (n-p)!)
> - Un entier est divisible par un autre, si le reste de sa division entière par ce dernier est nul.
> - Une règle de divisibilité est une séquence d'opérations simples qui permet de reconnaître rapidement si
>   un entier est divisible par un autre, sans qu'il soit nécessaire d'effectuer la division directe.
> - La numération désigne les techniques de représentation des nombres. Les représentations écrites au moyen
>   de signes constituent des systèmes de numération.
> - De nombreuses bases de numération ont été employées tels que le système binaire (base 2) utilisé par les
>   ordinateurs, le système octal (base 8), le système décimal (base 10), il est de loin le plus répandu de
>   nos jours, le système duodécimal (base 12), le système hexadécimal (base 16) utilisé en électronique et
>   en informatique car la conversion binaire-hexadécimale est très simple, etc.
> - La représentation d'un nombre dans une base plus grande devient plus compacte.
> - Il est possible de convertir un nombre appartenant à une base B1 donnée, dans une autre base B2.

Citation du chapitre : « Compter en octal, c'est comme compter en décimal, si on n'utilise pas ses pouces » — Tom Lehrer.

#### Activités, applications et solutions rédigées

**II.1 Activité 1 — PGCD par la méthode de la différence (p.152-153)** [PR pour Q1, penseur pour Q2-Q3]
- Q1 : analyse + algorithme d'une fonction PGCD de deux entiers positifs non nuls a et b, méthode de la
  différence. Trace donnée : PGCD(22, 6) = PGCD(16, 6) car 22 > 6 = PGCD(10, 6) = PGCD(4, 6) = PGCD(4, 2)
  car 4 < 6 = PGCD(2, 2) car 4 > 2 = 2 car 2 = 2.
```
0) Fonction PGCD (a, b : Entier) : Entier        {solution itérative}
1) Tant que (a ≠ b) Faire
      Si (a > b) Alors a ← a - b
      Sinon b ← b - a
      Fin Si
   Fin Tant que
2) PGCD ← a
3) Fin PGCD
```
  « Nous continuons à remplacer la plus grande valeur parmi a et b par la différence jusqu'à a = b »
- Q2 : dégager une relation récursive (encadré ci-dessus). Q3 : algorithme récursif :
```
0) Fonction PGCD (a, b : Entier) : Entier
1) Si (a = b) Alors PGCD ← a
   Sinon Si (a > b) Alors PGCD ← FN PGCD (a-b,b)
   Sinon PGCD ← FN PGCD (a,b-a)
   Fin Si
2) Fin PGCD
```
**II.2 Application (p.154)** [penseur] — traduire et tester la solution récursive, enregistrer sous
**PGCD_rec** [le programme imprimé s'appelle `Pgcd_diff`, sic] :
```pascal
Function pgcd(n, m : Integer) : Integer;
 Begin
   If (n = m) Then pgcd := m
   Else If (n > m) Then pgcd := pgcd(n - m, m)
   Else pgcd := pgcd(n, m - n);
 End;
```
  Saisie : `Repeat … Until (z>0)` ; PP : Saisie(a) ; Saisie(b) ; `Write('pgcd(',a,',',b,')= ', pgcd(a,b));`

**III.2 Activité 1 — Arrangements (p.155-157)** [sans icône pour les questions de cours]
- Questions 1-3 (cours) : définition, formule, condition 1 ≤ p ≤ n (encadré). Question 4 : analyse +
  algorithmes pour chercher puis afficher A(n,p), 1 ≤ p ≤ n. Affichage `Ecrire ("A(", n, ",", p, ") = ", FN Arrange (n,p))`.
```
0) Fonction Arrange (a, b : Entier) : Réel
1) ar ← 1
   Pour i de a à a-b+1 (pas = -1) Faire
      ar ← ar * i
   FinPour
2) Arrange ← ar
3) Fin Arrange
```
  (« Structure itérative complète utilisée pour calculer le résultat de l'opération a(a-1)(a-2)…(a-b+1) »)
```pascal
Function Arrange (a, b : Integer) : Real;
Var
  i, ar : Integer;
Begin
   ar := 1;
   For i := a Downto a-b+1 Do
      ar := ar*i;
   Arrange := ar;
End;
```
  [sic] ar déclaré Integer alors que la fonction est Real (débordement possible non signalé).
- Questions (p.157) : 1) traduire et tester, enregistrer sous **Arrang_1** ; 2) exécuter pour A(5,3),
  A(7,4), A(10,2), A(13,1) (cases à remplir) ; 3) « Ecrivez plus simplement la valeur A(n,1) » ; « Comparez
  les valeurs A(n,n) et A(n,n-1) ».

**III.3 Activité 2 — Combinaisons (p.157-158)** [penseur]
- Cours (encadré) puis demande : analyse + algorithmes pour C(n,p), 0 ≤ p ≤ n ; programme Combinaison_1,
  affichage `Ecrire ("C(", n, ",", p, ") = ", FN Comb (n,p))`.
```
0) Fonction Comb (n, p : Entier) : Réel
1) Comb ← FN Factorielle (n) / (FN Factorielle (p) * FN Factorielle (n-p))
2) Fin Comb
```
  « NB : La fonction Factorielle a été déjà l'objet d'un apprentissage précédent. » (non redonnée)
- Questions : 1) traduire et tester, **Comb_1** ; 2) « Faîtes [sic] les modifications nécessaires pour
  proposer une solution utilisant la fonction Arrange » → **Comb_2** ; 3) exécuter pour C(11,1), C(32,0),
  C(21,21), C(9,8).

**III.4 Application — C récursif (p.159)** [penseur] — analyse, algorithme, Pascal, **Comb_rec** :
```
0) Fonction Comb (n, p : Entier) : Réel
1) Si (p = 0) ou (p = n) alors Comb ← 1
   Sinon Comb ← FN Comb (n-1, p) + FN Comb (n-1, p-1)
   FinSi
2) Fin Comb
```
```pascal
Function Comb(n, p : integer) : real;
Begin
      If (p = 0) Or (p = n) Then Comb := 1
      Else Comb := Comb(n-1,p) + Comb(n-1,p-1);
End;
```

**IV — Préambule de la partie (p.159, verbatim)** : « Dans cette partie du chapitre, les problèmes ne seront
pas résolus directement avec l'opérateur arithmétique **Mod**. Nous allons, par contre, analyser quelques
problèmes répondant aux règles de divisibilité appropriées. » (Remarque du transcripteur : les fonctions
corrigées utilisent néanmoins Mod sur la somme des chiffres, sur m Mod 100 ou sur 2*m.)

**IV.2 Activité 3 — Divisibilité par 3 (p.160-163)** [sans icône ; Application : penseur]
- Données : « 6, 42, 191, 39, 41, 30, 20, 13 et 8 » ; entourer ceux divisibles par 3. Réponse (image) :
  6, 42, 39, 30 entourés ; la ligne réponse réécrit « 19 » au lieu de 191 [sic]. Constatation : somme des
  chiffres divisible par 3 (4 + 2 = 6 ; 3 + 9 = 12 ⇒ 1 + 2 = 3 ; 3 + 0 = 3) ; contre-exemples
  « 1 + 9 + 1 = 1 + 1 = 2 » [sic : étape 11 omise], 4 + 1 = 5, « et de même pour 20, 13 et 8 ». → Conclusion (encadré).
- Application : vérifier si n est divisible par 3 avec la règle — analyse modulaire, algorithmes,
  Pascal, **Divi_3**. Le nombre est saisi comme **chaîne** s (contrôle `Val(ch, Num, e) … Until (e = 0)`).
```
0) Fonction Div_3 (ch : Chaîne) : Chaîne
1) Somme ← 0
   Pour i de 1 à Long (ch) Faire
       Valeur (ch[i], nb, e)
       Somme ← Somme + nb
   FinPour
2) Si Somme Mod 3 = 0 alors Div_3 ← " est divisible par 3."
   Sinon Div_3 ← " n'est pas divisible par 3."
   Finsi
3) Fin Div_3
```
  TDOL : Somme, nb, e (indicateur d'erreurs de conversion), i : Entier. Pascal : `Val(ch[i], nb, e); somme := somme + nb` ; PP `Saisie(s); Write(s, Div_3(s));`.

**IV.3 Divisibilité par 4 — Application (p.163-164)** [PR] — **Divi_4** ; n Entier Long.
```
0) Fonction Div_4 (m : Entier Long) : Chaîne
1) Si (m Mod 100) Mod 4 = 0 Alors Div_4 ← " est divisible par 4."
   Sinon Div_4 ← " n'est pas divisible par 4."
   Finsi
2) Fin Div_4
```
  Pascal : `If ((m Mod 100) Mod 4) = 0 Then div_4 := ' est divisible par 4.' Else div_4 := ' n''est pas divisible par 4.';`

**IV.4 Divisibilité par 5 — Application (p.164-165)** [penseur] — **Divi_5** ; n Entier Long.
```
0) Fonction Div_5 (m : Entier Long) : Chaîne
1) Si (2*m) Mod 10 = 0 Alors Div_5 ← " est divisible par 5."
   Sinon Div_5 ← " n'est pas divisible par 5."
   Finsi
2) Fin Div_5
```
  Pascal : `If (2*m) Mod 10 = 0 Then div_5 := ' est divisible par 5.' Else div_5 := ' n''est pas divisible par 5.';`

**IV.5 Autres règles — Questions (p.166)** (non corrigées)
1) Chercher d'autres règles de divisibilité. 2) n = 571u (u chiffre des unités) : programme Pascal
affichant u et n pour lesquels n est divisible par 4. 3) n = 10c8u (c centaines, u unités) : programme
affichant les couples (c, u) et n divisible par 3. 4) Programme affichant tous les diviseurs d'un entier
naturel non nul n.

**V.2 Activité — Décimal → binaire (p.167-168)** [penseur] — « Nous avons vu en 3ème année comment
convertir un nombre décimal en binaire » ; analyse modulaire + algorithmes. PP `Conversion_10_2` :
Saisir (N) ; Chercher (N, T, C) ; Afficher (T, C). TDNT : `Binaire = 0,1` ; `Tab = Tableau de 100 binaire`.
TDOG : N Entier ; C Entier (nombre de divisions par 2) ; T Tab (restes successifs).
```
0) Procédure Chercher (n : entier ; Var Reste : Tab ; Var C : entier)
1) C ← 0
   Répéter
      C ← C + 1
      Reste [C] ← n mod 2
      n ← n div 2
   Jusqu'à (n = 0)
2) Fin Chercher
```
  (Afficher n'est pas détaillée ; pas de Pascal.)

**V.3 Hexadécimal → binaire (p.168-171)** — questions : analyse modulaire, algorithmes, Pascal, **Hex_Bin**.
Affichage `Ecrire ("(", Hex, ")16 = (", FN Conv_Bin(Hex), ")2")` ; Hex : chiffres 0-9 et lettres A-F.
```
0) Fonction Conv_Bin (CH_Hex : Chaîne) : Chaîne
1) CH_Bin ← ""
   Pour i de 1 à Long (CH_Hex) Faire
      CH_Bin ← CH_Bin + FN Bin_Car (CH_Hex[i])
   FinPour
2) Tant que CH_Bin[1] = "0" Faire          {zéros superflus du début}
      Efface (CH_Bin,1,1)
   Fin Tant Que
3) Conv_Bin ← CH_Bin
4) Fin Conv_Bin

0) Fonction Bin_Car (Symb : Caractère) : Chaîne
1) Si Non (Symb Dans ["0".."9"])
   Alors N ← Ord (Symb) - 55
   Sinon Valeur (Symb, N, E)
   FinSi
2) CH ← "0000"
   i ← 4
   Répéter
      R ← N Mod 2
      Convch (R, Ch_R)
      Ch[i] ← Ch_R[1]
      N ← N Div 2
      i ← i-1
   Jusqu'à N = 0
3) Bin_Car ← CH
4) Fin Bin_Car
```
  TDOL Bin_Car : CH Chaîne[4], Ch_R Chaîne[1], i, N, E, R Entier. Pascal Bin_Car (p.171) : identique avec
  `N := Ord (Upcase(Symb)) - 55`, `Val(Symb, N, E)`, `Str (R, Ch_R)` (l'algorithme n'a pas Majuscule).

**V.4 Octal → décimal (p.172-174)** — **Oct_Dec**. [sic] Résultat et PP écrivent `FN Conv_Bin(Oct)` alors que
la fonction est Conv_Dec ; tableau titré « objets locaux » pour des objets globaux. Oct : Entier Long, chiffres 0-7.
```
0) Fonction Conv_Dec (N_Oct : Entier Long) : Entier Long
1) ConvCh (N_Oct, CH_Oct)
2) Dec ← 0
   Pour i de Long (CH_Oct) à 1 (pas = -1) Faire
      Valeur (Ch_Oct[i], N, e)
      Dec ← Dec + N * FN Puiss_8 (Long (Ch_Oct) - i)
   FinPour
3) Conv_Dec ← Dec
4) Fin Conv_Dec
```
  Pascal complet : Saisie (boucle `While trouve` qui relit tant qu'un chiffre n'est pas dans ['0'..'7']) ;
```pascal
Function Puiss_8 (M : Integer) : Longint;
Var
  P : Longint;
  j : Integer;
Begin
  P := 1;
  For j := 1 To M Do P := P * 8;
     Puiss_8 := P;
End;
```
  Conv_Dec : `Str(N_Oct, Ch_Oct); Dec := 0; For i := Length(CH_Oct) DownTo 1 Do Begin Val(Ch_Oct[i],N,e);
  Dec := Dec + N * Puiss_8(Length(Ch_Oct) - i); End; Conv_Dec := Dec;` ; PP `Write('(', Oct, ')8 = (', Conv_Dec(Oct), ')10');`

**V.5 Binaire → octal (p.175-177)** — **Bin_Oct** ; Bin chaîne de "0"/"1". [sic] Conv_Oct décrite comme
« retourner un entier » alors qu'elle renvoie une chaîne ; tableau « objets locaux » pour des globaux.
```
0) Fonction Conv_Oct (Ch_Bin : Chaîne) : chaîne
1) Tant Que Long (Ch_Bin) Mod 3 ≠ 0 Faire
      Ch_Bin ← "0" + Ch_Bin
   Fin Tant Que
2) N ← Long (Ch_Bin) Div 3
   Oct ← "", L ← Long (Ch_Bin)
   Pour i de 1 à N Faire
      Ch1 ← Sous_chaîne (Ch_Bin, L-2, 3)
      A_oct ← 0
      Pour j de 1 à 3 Faire
         Valeur (ch1[j], a, e)
         A_oct ← A_oct + a * FN Puiss_2 (3-j)
      FinPour
      Convch (A_oct, ch2)
      Oct ← ch2 + Oct
      L ← L - 3
   FinPour
3) Conv_Oct ← Oct
4) Fin Conv_Oct
```
  Pascal Conv_Oct (p.177) : même structure (`Copy (Ch_Bin, L - 2,3)`, `Str(A_oct, ch2)`). Puiss_2 n'est pas
  détaillée.

**V.6 Base B1 → base B2 (p.177-180)** [P♪] — 2 ≤ b1 ≤ 16 et 2 ≤ b2 ≤ 16 ; analyse modulaire, algorithmes,
Pascal, **B1_B2**. Données : N_B1 chaîne « ne peut contenir que des chiffres de la base B1 (commençant
obligatoirement par le chiffre 0) » [sic ? phrase telle qu'imprimée] ; Saisie_Base, Saisie_Nombre (non
détaillées). PP numéroté « 4) Ecrire … / 3) Fin B1_B2 » [sic]. Principe : passage B1 → base 10 (Conv_10)
puis base 10 → B2 (Conv_B2).
```
0) Fonction Conversion_B2 (Ch_B1 : Chaîne; B1, B2 : Entier) : Chaîne
1) N_10 ← FN Conv_10 (CH_B1, B1)
2) CH_B2 ← FN Conv_B2 (N_10, B2)
3) Conversion_B2 ← CH_B2
4) Fin Conversion_B2

0) Fonction Conv_10 (Ch_B1 : Chaîne; B1 : Entier) : Entier Long
1) Dec ← 0
   Pour i de Long (Ch_B1) à 1 (pas = -1) Faire
      Si Majuscule (Ch_B1[i]) Dans ["A".."F"]
      Alors N ← Ord (Majuscule (Ch_B1[i])) - 55
      Sinon Val (Ch_B1[i],N,e)
      FinSi
      Dec ← Dec + N * FN Puiss_B1 (Long (Ch_B1) - i, B1)
   FinPour
2) Conv_10 ← Dec
3) Fin Conv_10

0) Fonction Conv_B2 (N_10 : Entier Long; B2 : Entier) : Chaîne
1) Ch ← " "
   Répéter
      R ← N_10 Mod B2
      Si R ≥ 10
      Alors Ch_R ← Majuscule (Chr (55 + R))
      Sinon Convch (R, Ch_R)
      FinSi
      Ch ← Ch_R + Ch
      N_10 ← N_10 Div B2
   Jusqu'à N_10 = 0
2) Conv_B2 ← Ch
3) Fin Conv_B2
```
  Pascal fourni pour Conv_10 seulement (p.180 : `If Upcase(Ch_B1[i]) In ['A'..'F'] Then N := Ord(Upcase(Ch_B1[i])) - 55 Else Val(Ch_B1[i],N,e); Dec := Dec + N * Puiss_B1(Length(Ch_B1) - i,B1);`).
  [sic] « Val » (Pascal) dans l'algorithme Conv_10 au lieu de « Valeur » ; Ch initialisé à " " (espace) dans
  Conv_B2 ; tableau « objets globaux » p.179 pour des objets locaux de Conversion_B2 ; Puiss_B1 non détaillée.

#### Exercices (p.182-185) — non corrigés
| N° | Icône | Énoncé (données → demande) | p. |
|---|---|---|---|
| 1 | [PR] | V/F (cases). a. 245025 + 9171 est divisible par 2 / 3 / 4. b. B43 peut être un nombre décimal / duodécimal (base 12) / hexadécimal. c. L'entier a+1 est représenté dans la base a (a >= 2) par 10 / 11 / « Cela dépend de a ». d. La conversion du décimal 3243 en hexadécimal est ABC / BAC / CAB. | 182 |
| 2 | [PR] | « Dans un contexte informatique », définir : a) base de numération ; b) diviseur d'un entier ; c) multiple d'un entier. | 182 |
| 3 | [P♪] | Anagramme = mot de même longueur, formé des mêmes lettres (sens ou non). 1. Programme affichant le nombre d'anagrammes d'un mot (lettres seulement) ; 2. nombre d'anagrammes commençant par une voyelle. | 182 |
| 4 | [P♪] | a, b réels, n entier naturel non nul : vérifier la formule du binôme (a + b)ⁿ = C(n,0)aⁿ + C(n,1)aⁿ⁻¹b¹ + C(n,2)aⁿ⁻²b² + … + C(n,n-1)a¹bⁿ⁻¹ + C(n,n)bⁿ. | 183 |
| 5 | [P♪] | n entier naturel non nul : calculer et afficher C(n,0) - C(n,1) + C(n,2) - C(n,3) + … + (-1)ⁿ C(n,n). | 183 |
| 6 | [P♪] | n = 61d1 (d chiffre des dizaines) : afficher d et n pour lesquels n est divisible par 9. | 183 |
| 7 | [P♪] | n = m97u (m milliers, u unités) : afficher les couples (m, u) et n divisible par 5 et par 9. | 183 |
| 8 | [P?] | Afficher l'ensemble des entiers naturels n entre 1 et 100 tels que n divise n + 8. | 183 |
| 9 | [P?] | **Bac 1995 « Conversion entre bases »** : décimal N > 0 → base B par divisions euclidiennes, restes dans RESTES (RMAX = 15). 1) algo SAISIE-DEC ; 2) SAISIE-BASE (2 ≤ B ≤ 16) ; 3) a- RANGER (N, B, RESTES, R) (ranger les restes, compter R), b- Pascal ; 4) RENVERSER (RESTES, R) (permuter RESTES[1]↔RESTES[R], RESTES[2]↔RESTES[R-1]…) ; 5) a- fonction CONVERT (C) (0 ≤ C ≤ 15 ; CONVERT(0) = "0", CONVERT(9) = "9", CONVERT(10) = "A", CONVERT(15) = "F"), b- Pascal ; 6) CONCATENATION (résultat, RESTES) avec CONVERT ; 7) programme principal CONVERSION. | 183-184 |
| — | — | Consigne commune aux ex. 10-16 : « a) Proposez une analyse modulaire au problème, b) Déduisez les algorithmes des modules dégagés ». | 184 |
| 10 | [P?] | Divisibilité par 7 : « si le nombre mcdu est divisible par 7, alors : mcd-2*u est divisible par 7, et réciproquement » ; exemple 7241 → 724-2*1 = 722 → 72-2*2 = 68, non divisible donc 7241 non plus ; **Div_7**. | 184 |
| 11 | [P?] | Divisibilité par 11 : différence entre somme des chiffres de rang pair et de rang impair divisible par 11 ; exemples 651 ((6+1)-5 = 2, non) et 41679 ((4+6+9)-(1+7) = 11, oui) ; **Div_11**. | 185 |
| 12 | [P?] | Divisibilité par 6 (divisible à la fois par 2 et par 3) ; « NB : Ne pas utiliser directement l'opérateur arithmétique Mod » ; **Div_6**. | 185 |
| 13 | [P?] | Convertir un nombre octal en base 2 ; **Oct_Bin**. | 185 |
| 14 | [P?] | Convertir un nombre binaire en base 16 ; **Bin_Hex**. | 185 |
| 15 | [P?] | Convertir un nombre décimal en base binaire ; **DecBin_R**. | 185 |
| 16 | [P?] | Lire deux nombres binaires et vérifier si l'un est divisible par l'autre ; **Div_Bin**. | 185 |

#### Vocabulaire officiel
arithmétique ; PGCD (Plus Grand Commun Diviseur) ; méthode de la différence ; relation récursive ;
solution itérative / récursive ; permutation, arrangement (p-uplet d'éléments distincts), combinaison
(partie de E formée par p éléments) ; factorielle ; divisible ; division euclidienne ; reste ; règle de
divisibilité ; chiffre des unités / dizaines / centaines / milliers ; somme des chiffres ; analyse
modulaire ; module ; système de numération ; base de numération ; binaire, octal, décimal, duodécimal,
hexadécimal ; triplet de bits, 4 bits ; divisions successives ; zéros superflus ; code ASCII ; fonctions
et procédures prédéfinies (algorithmique : Valeur, Convch, Long, Efface, Sous_chaîne, Majuscule, Ord, Chr ;
Pascal : Val, Str, Length, Delete implicite, Copy, Upcase, Ord, Chr) ; Mod, Div.

#### Notions testables (8 — chapitre dense, découpage proposé ci-dessous)
1. **PGCD par la méthode de la différence** : trace, version itérative (Tant que a ≠ b), relation et version récursive.
2. **Arrangements A(n,p)** : définition, formules n(n-1)…(n-p+1) = n!/(n-p)!, condition 1 ≤ p ≤ n, boucle décroissante Arrange, cas A(n,1) et A(n,n) vs A(n,n-1).
3. **Combinaisons C(n,p)** : définition, C = A/p! = n!/(p!(n-p)!), 0 ≤ p ≤ n, version factorielle, via Arrange, version récursive C(n-1,p) + C(n-1,p-1) avec cas p = 0 ou p = n.
4. **Divisibilité par la somme des chiffres** (3, 9) : nombre traité en chaîne, cumul des chiffres par Valeur.
5. **Divisibilité par le(s) dernier(s) chiffre(s)** (2, 4, 5, 10, 25) : (m Mod 100) Mod 4, (2*m) Mod 10 ; règles 7, 11, 6 (exercices / lecture) ; recherche de chiffres inconnus (571u, 10c8u, 61d1, m97u).
6. **Systèmes de numération** : définition (base ≥ 2, chiffres 0 à N-1), bases 2/8/10/16 (et 12), valeurs A-F, « base plus grande = plus compacte ».
7. **Conversions par regroupement de bits** : hex → bin (4 bits par chiffre, Ord - 55, suppression des zéros de tête), bin → oct (groupes de 3 depuis la droite, complément par des "0"), oct → bin et bin → hex (exercices).
8. **Conversions par puissances / divisions successives** : base B → décimal (Σ chiffre × B^rang, Puiss_8, Conv_10), décimal → base B (restes successifs, Chr(55 + R), Chercher, Conv_B2), B1 → B2 via la base 10 (Bac 1995).
- Découpage proposé (si un chapitre de l'app ne doit pas dépasser ~8 notions et pour équilibrer la charge) :
  **5a « Arithmétique : PGCD, dénombrement, divisibilité »** (notions 1-5, p.152-166) et
  **5b « Conversions entre bases de numération »** (notions 6-8, p.166-180), les exercices 1-8 et 10-12
  allant à 5a, 9 et 13-16 à 5b (l'ex. 1 est mixte : a → 5a ; b, c, d → 5b).

#### Bornes
- ✅ INCLUS : PGCD par différence (itératif + récursif, Pascal) ; A(n,p) itératif (Pascal) ; C(n,p) par
  factorielles, par Arrange, récursif (Pascal) ; permutations p! (tableau de présentation) ; définitions de
  divisibilité ; règles par 2, 3, 4, 5, 9, 10, 25 (cours), 7, 11, 6 (exercices + lecture) ; saisie d'un entier
  comme chaîne ; numération bases 2, 8, 10, 12 (cité), 16 ; conversions déc→bin, hex→bin, oct→déc, bin→oct,
  B1→B2 (cours), oct→bin, bin→hex, déc→bin, division de binaires (exercices) ; formule du binôme (p.183) et somme
  alternée des C(n,k) (exercices) ; dénombrement d'anagrammes (exercice) ; recherche des diviseurs d'un
  entier (question IV.5).
- ⛔ EXCLU (cité au préambule mais non traité, ou absent du chapitre) : test de primalité, nombres premiers,
  **crible d'Ératosthène**, décomposition en facteurs premiers, nombres parfaits, PPCM, somme de puissances,
  test de parité en tant qu'algorithme ; PGCD par l'algorithme d'Euclide (divisions/modulo) — seule la
  méthode de la différence figure ici [?: d'autres méthodes peuvent exister ailleurs dans le manuel, hors
  périmètre] ; algorithme de la factorielle (supposé acquis, non redonné) ; nombres négatifs / à virgule
  dans les conversions ; complément à 2 ; bases > 16.

#### Page « Lecture » (p.186), résumé — « Quelques règles de divisibilité »
Par 2 : dernier chiffre 0, 2, 4, 6 ou 8 (5287 non ; 136 et 94618 oui). Par 3 : somme des chiffres (734 :
14, non ; 81234 : 18, oui). Par 4 : deux derniers chiffres (61934 : 34, non ; 2028 : 28 = 4x7, oui). Par 5 :
dernier chiffre 0 ou 5 (2497 non ; 625 et 4800 oui). Par 7 : « si le nombre abcd est divisible par 7, alors :
abc-2d est divisible par 7, et réciproquement » (7241 → 722 → 68, non ; 30086 → 2996 → 287 → 14, oui). Par 9 :
somme des chiffres (5019 : 15, non ; 837 : 18, oui). Par 11 : différence des sommes des chiffres de rang pair
et impair (651 non ; 41679 oui). Par 25 : deux derniers chiffres (6287 non ; 4150 : 50 = 25x2, oui). Cette
page fournit donc des exemples supplémentaires réutilisables (7, 9, 25 non illustrés dans le cours).

#### Note de lecture — ch.5
- Pages lues (texte) : 151-186 (36). Pages sondées en image : 151-186 (36/36 — sondage étendu à toute la section après écarts).
- Écarts texte↔image (11 pages) : p.151, 154-159, 181 exposants/indices de A^p_n et C^p_n éclatés sur
  plusieurs lignes ; p.157, 159 et 177 « ≤ » rendu « ) » (« 0 ) p ) n », « 2 ) b1 ) 16 ») ; p.155 tableau de
  combinatoire restitué sans structure ; p.160 cercles de la réponse (6, 42, 39, 30) invisibles en texte ;
  p.168, 172, 175 schémas de conversion (flèches, puissances 8², 2²…) aplatis (« 1 * 82 + 7 * 81 + 5 * 80 ») ;
  p.182 cases à cocher perdues ; p.183 formule du binôme et somme alternée éclatées (indices C^k_n dispersés).
  Aucun écart sur les blocs de code Pascal (couche texte fidèle).
- Coquilles / incohérences [sic] : « habilités » (objectifs) ; A(2,3)/C(2,3) en ordre (p, n) vs A(n,p) ;
  ar Integer dans une fonction Real ; « Faîtes » ; « 191 » devenu « 19 » ; « 1 + 9 + 1 = 1 + 1 = 2 » ;
  programme `Pgcd_diff` au lieu de PGCD_rec ; « FN Conv_Bin(Oct) » pour Conv_Dec ; tableaux « locaux » /
  « globaux » inversés (p.172, 175, 179) ; Conv_Oct « retourne un entier » ; numérotation « 4) … 3) Fin
  B1_B2 » ; « Val » dans un algorithme ; Ch ← " " dans Conv_B2 ; Ord(Symb) - 55 sans Majuscule dans
  l'algorithme Bin_Car (Upcase dans le Pascal).
- Doutes [?] : p.178 « commençant obligatoirement par le chiffre 0 » (sens incertain, repris tel quel) ;
  Puiss_2, Puiss_B1, Saisie_Base, Saisie_Nombre, Afficher (déc→bin) et Factorielle non fournis par le manuel.

---

## Fiche de lecture ch.4-5
- **pagesLues** : 123-186 (64 pages ; ch.4 : 123-150 = 28 ; ch.5 : 151-186 = 36), couche texte L1, une lecture par page.
- **Pages sondées (image 110 dpi)** : 64/64. Sondage initial (16 pages : 124, 136, 137, 140, 141, 144, 147,
  155, 157, 160, 168, 172, 175, 181, 182, 183) ; des écarts relevés dans chacun des deux chapitres ont
  entraîné le sondage intégral des deux sections, conformément à la règle « ≥ 1 écart ⇒ sonder la section
  entière ».
- **Nombre d'écarts texte↔image** : 20 pages concernées (ch.4 : 9 ; ch.5 : 11), tous de nature
  typographique (≤ → « ) », ≥ → « * », exposants/indices aplatis, fractions/racines éclatées, schémas et
  cases perdus) plus 1 écart de contenu (p.137 : valeurs des rapports de Fibonacci permutées dans la couche
  texte) et 1 formule absente de la couche texte (p.147, Viète). Toutes les formules et tous les encadrés de
  la fiche sont repris de l'image. Aucun écart sur le code Pascal.
- Aucune copie du PDF dans git ; fichiers intermédiaires (txt/png) dans le scratchpad uniquement.
Source unique : manuel élève CNP « Algorithmique et programmation », 4e année secondaire, Sciences de l'informatique (248 p.), décalage PDF/page imprimée = 0.

**Pictogrammes observés** (la légende p.5 définit quatre silhouettes de difficulté ; leur correspondance avec ces icônes n'a pas été établie : `[?]`) :
- **[P-?]** : personnage pensif seul avec un « ? » ; il accompagne la plupart des encadrés gris d'activité et les exercices 1 à 4 du ch.6 ;
- **[P-??]** : personnage avec « ? » et deux crochets ; on le trouve sur l'Activité 2 du ch.6, les exercices 5 et 6 du ch.6 et tous les exercices du ch.7 ;
- **[clé]** : quatre personnages qui portent une clé ; il marque le début de la solution rédigée qui suit un encadré.

Les silhouettes de difficulté de la légende p.5 sont présentes mais leur rattachement à un niveau n'a pas été relevé `[?]` (ni étoiles ni code couleur). Les seuls repères sont les mentions « Bac Tp 2001 » (ch.6, ex.2 et 3) et « Sujet de baccalauréat 1992 » (ch.7, ex.3).

**Forme des solutions.** Toutes les solutions du manuel suivent le même patron : a) analyse (Résultat / Traitement / Données), b) algorithme numéroté `0) Début … n) Fin`, accompagné d'un tableau de codification des objets (globaux, locaux, nouveaux types), puis c) traduction en Pascal (Turbo Pascal / Free Pascal, `Uses Crt`).

---

### Chapitre 6 — Les algorithmes d'approximation (p.187–212)

**Objectif officiel (p.187, verbatim)** : « Acquérir des habilités [sic] de résolution de problèmes à travers l'apprentissage d'algorithmes d'approximation »

#### Plan

| § | Titre | Pages |
|---|---|---|
| — | Page de garde (plan + objectif) | 187 |
| I | Introduction | 188 |
| II | Recherche du point fixe d'une fonction (présentation + Activité 1 `Pt_Fixe`) | 188–190 |
| III | Calcul de valeurs approchées de constantes connues | 190–197 |
| 1) (numérotation du manuel ; notée III.1 ici) | Valeur approchée de π : présentation (Archimède), formule d'Euler (`Pi_Euler`), applications, formule de Wallis (`Pi_Wallis`), application | 191–195 |
| 2) (numérotation du manuel ; notée III.2 ici) | Valeur approchée de e : présentation, factorielles (`e_Fact`), applications | 195–197 |
| IV | Calcul d'aires : introduction, méthode des rectangles (`Meth_Rec`), méthode des trapèzes (`Meth_Tra`), questions | 197–203 |
| — | Retenons | 204–205 (citation de B. Russell p.205) |
| — | Exercices 1 à 6 | 206–207 |
| — | Lecture : « L'historique de π », notation, nature, décimales, valeurs approchées ; tables de constantes | 208–212 |

#### Contenu du cours, paragraphe par paragraphe

- **I. Introduction (p.188).** Une résolution exacte de la plupart des problèmes d'optimisation demanderait un temps de calcul prohibitif. Les algorithmes d'approximation donnent, en temps polynomial, des solutions « quasi-optimales » dont l'écart à l'optimum est borné. Le texte est culturel (arrondi de programmes linéaires, programmation semi-définie, plongement d'espaces métriques) et ne donne aucun algorithme.

- **II. Point fixe (p.188–190).**
  - Définition : « un élément x de E est un point fixe de f si f(x) = x ».
  - Exemples : la symétrie de centre A a pour unique point fixe A ; l'application inverse a deux points fixes, −1 et 1 ; f(x) = x+1 n'a aucun point fixe.
  - Suite récurrente : U(n+1) = f(U(n)) ; « Dans le cas où (Un) converge, elle le fait nécessairement vers un point fixe de f ».
  - **Activité 1 [P-?] (p.189)** : résoudre sin(x) = 1−x. Demande : a) analyse modulaire, b) algorithmes, c) traduction Pascal, programme `Pt_fixe`.
  - Solution : l'équation se réécrit f(x) = 1 − sin(x) = x, avec xact ← 1 « {choix arbitraire} » et i ← 0. On répète {xpre ← xact ; xact ← f(xact) ; i ← i+1} jusqu'à Abs(xact−xpre) < Epsilon.
  - Codification : Epsilon constante = 10⁻⁵ ; i entier non signé (`word`) ; xact, xpre réels ; f fonction.
  - Pascal p.190 : `Const Epsilon = 1E-5;`, fonction locale `f := 1 - sin(x)`, boucle `Repeat … Until (abs(xact-xpre) < Epsilon)`, affichage `xact:10:6`.
  - **Capture Free Pascal p.190 (visible seulement sur l'image)** : « Le point fixe est : 0.51097, trouvé après : 83 itérations. » La simulation du transcripteur donne x ≈ 0,510969 après 83 itérations, ce qui confirme la capture.

- **III. Constantes (p.190–197).**
  - **Activité 2 [P-??] (p.190)** : « Citez quelques constantes numériques ? Donnez leurs valeurs respectives ? »
  - Réponse en tableau : e = 2,718… (« Le nombre de neper ») ; π = 3,1416… ; g = 9,80665 (« L'accélération normale de la pesanteur »).

  - **III.1 Valeur approchée de π.**
    - a) Présentation (p.191) : 3,14 n'est qu'une approximation. Méthode d'Archimède : on encadre le périmètre du cercle entre les polygones réguliers inscrit et circonscrit. L'inscrit donne une approximation par défaut, le circonscrit une approximation par excès.
    - b) **Formule d'Euler [P-?] (p.191–192)** : π²/6 = 1 + 1/2² + 1/3² + … + 1/n² + … ; programme `Pi_Euler`.
      - Analyse : S2 ← 1, i ← 2 ; Répéter {S1 ← S2 ; S2 ← S1 + 1/Carré(i) ; i ← i+1} Jusqu'à RacineCarrée(6*S2) − RacineCarrée(6*S1) < Epsilon ; on affiche RacineCarrée(6*S2).
      - Codification : i entier long ; S1, S2 réels ; Epsilon constante = 10⁻⁴.
      - Pascal : `Const Epsilon = 10E-4;` [sic], `S2 := S1 + 1/sqr(i)`, `Sqrt(6*S2):10:6`.
    - c) **Application 1 (p.193)** : exécuter `Pi_Euler` et remplir le tableau Epsilon → valeur approchée de π pour 10⁻⁶, 10⁻⁷, 10⁻⁸, 10⁻⁹, 10⁻¹⁰.
    - **Application 2 (p.193)** : proposer une solution **récursive** du calcul de π par la formule d'Euler.
    - d) **Formule de Wallis [P-?] (p.193–194)** : π/2 = (2/1)·(2/3)·(4/3)·(4/5)·(6/5)·(6/7)·(…) ; programme `Pi_Wallis`.
      - Algorithme : P2 ← 2, i ← 2, Num ← 2, Den ← 3 ; Répéter {P1 ← P2 ; P2 ← P1*(Num/Den) ; Si i Mod 2 = 0 Alors Num ← Num+2 Sinon Den ← Den+2 FinSi ; i ← i+1} Jusqu'à Abs(2*P2 − 2*P1) < Epsilon ; on affiche 2*P2.
      - Codification : i, Num, Den entiers ; P1, P2 réels ; Epsilon = 10⁻⁴. Pascal `Epsilon = 10E-4` [sic].
    - e) **Application (p.195)** : exécuter `Pi_Wallis`, tableau Epsilon de 10⁻⁴ à 10⁻⁹.

  - **III.2 Valeur approchée de e.**
    - a) Présentation (p.195) : nombre de Neper, base du logarithme népérien, valeur 2,7182818284 5904523536 … ; « C'est un nombre irrationnel » ; formule 1 + 1/1! + 1/2! + …
    - b) **Factorielles [P-?] (p.195–196)** : calculer e à 10⁻⁴ avec e = 1 + 1/1! + … + 1/6! + … ; programme `e_Fact`.
      - Algorithme : S2 ← 1, i ← 0 ; Répéter {S1 ← S2 ; i ← i+1 ; S2 ← S2 + 1/FN Fact(i)} Jusqu'à S2 − S1 < Epsilon.
      - Codification : i entier long ; S1, S2 réels ; Fact fonction ; Epsilon = 10⁻⁴.
      - Pascal : `Function Fact(Nb : Longint) : Longint` itérative (boucle `For j := 1 To Nb Do F := F * j`), affichage `S2:12:11`, `Epsilon = 10E-4` [sic].
    - c) **Application 1 (p.197)** : tableau Epsilon de 10⁻⁴ à 10⁻⁹ pour `e_Fact`. **Application 2** : solution **récursive** pour e.

- **IV. Calcul d'aires (p.197–203).**
  - **Introduction.**
    - Cadre : f continue et croissante sur [a,b]. Sans primitive connue, on ne peut pas calculer ∫ₐᵇ f(t)dt, d'où la recherche d'une valeur approchée.
    - Figure « Représentation graphique d'une intégrale ». L'intégrale d'une fonction positive est l'aire entre l'axe des abscisses et la courbe ; on parle d'aire algébrique si la fonction est négative.
    - Principe (p.198) : on subdivise [a,b] en n intervalles de diamètre (b−a)/n, avec a₁ = a et aₙ₊₁ = b et h = aᵢ₊₁ − aᵢ. Sur chaque intervalle, l'aire sous la courbe est remplacée par une aire plus simple. Plus n est grand, plus le résultat converge.
    - Méthodes citées : rectangles, trapèzes, Simpson, Romberg.
  - **2) Rectangles, principe (p.198)** : sur [aᵢ, aᵢ₊₁], un rectangle de largeur aᵢ₊₁ − aᵢ. Trois hauteurs possibles, chacune illustrée par une figure (figures seulement sur l'image) :
    - f(aᵢ) : « Rectangles à gauche » ;
    - f(aᵢ₊₁) : « Rectangles à droite » ;
    - f((aᵢ + aᵢ₊₁)/2) : « Rectangles du point milieu ».
  - **b) Application [P-?] (p.199–201)** : aire sous f(x) = 1/(1+x²) sur [a,b] par les rectangles ; programme `Meth_Rec`.
    - Modules : procédure `Lecture(a, b, n)`, avec contrôles de saisie `Until b1>a1` et `Until n1>0` ; fonction `Rectangles(a1, b1 : Réel ; n1 : Entier) : Réel`.
    - Algorithme de Rectangles : Somme ← 0 ; h ← (b1−a1)/n1 ; x ← a1 + h/2 ; Pour k de 1 à n1 {Somme ← Somme + f(x) ; x ← x+h} ; Rectangles ← Somme*h.
    - **C'est la méthode du point milieu** : le commentaire Pascal p.201 dit « {Programme Principal_ Méthode du point milieu} ».
    - Fonction f locale dans Rectangles : `f := 1/(1+sqr(x1))`.
  - **3) Trapèzes, principe (p.201, avec figure)** : h = (b−a)/n, aᵢ = a + i·h ; aire d'un trapèze = h·((f(a₀)+f(a₁))/2) ; l'intégrale vaut la somme des h·((f(aᵢ)+f(aᵢ₊₁))/2).
  - **b) Application [P-?] (p.201–203)** : même f, programme `Meth_Tra` (en-tête algorithmique « Début Meth_Trap »).
    - Algorithme de Trapezes : h ← (a1+b1)/n1 [sic, le Pascal fait (b1−a1)/n1] ; Somme ← (f(a1)+f(a1+h))/2 ; x ← a1 ; Pour k de 1 à n1−1 {x ← x+h ; Somme ← Somme + (f(x)+f(x+h))/2} ; Trapezes ← Somme*h.
    - Codification : n et k entiers non signés (`Word`).
  - **Questions (p.203)** : exécuter `Meth_rec` et `Meth_tra` avec a = 1 et b = 5, pour n = 2, 4, 5, 6, 7, 8 ; remplir le tableau et répondre à « Que remarquez-vous ? ».

#### Encadrés « Retenons » (verbatim, p.204–205)

> A) Un **algorithme d'approximation** calcule une solution approximative d'un problème en un temps raisonnable (en général polynomial).
>
> B) Les racines d'une équation de la forme f(x) = x sont appelées des **points fixes**. En faisant varier x, nous pouvons déterminer une approximation du point fixe.
>
> C) π est un nombre irrationnel. En effet, il est impossible de l'exprimer avec un nombre fini d'entiers, de fractions rationnelles et de leurs racines.
> Il n'y a donc pas de développement décimal simple de π.
> π/2 = 2/1 + 2/3 + 4/3 + 4/5 +...... [sic : des « + » au lieu de produits ; la p.193 donne bien un produit]
> π²/6 = 1/1² + 1/2² + 1/3² + 1/4² +.... + 1/k² +.... (formule d'Euler)
>
> Nous appelons constante de Neper, et nous notons e, l'unique réel tel que ln e = 1. C'est la base des logarithmes naturels. Il est appelé nombre exponentiel par Euler en 1761 et il vaut approximativement : e ≈ 2,718 281 828 459 045 235 360 287 4…
> La formule la plus connue approchant la valeur de e est : 1 + (1/1!) + (1/2!) + (1/3!) + …
>
> D) La mesure de **l'aire algébrique** se trouvant entre la courbe f(x), les droites x = a, x = b et y = 0, est représentée par **l'intégrale** "de a à b" de f(x).

> 1- **La méthode des rectangles** consiste à approcher l'intégrale ∫ₐᵇ f(t)dt par la somme des aires des n rectangles de base [aᵢ, aᵢ₊₁] et de hauteur f(aᵢ), i variant de 0 à n-1. Nous appelons aussi cette formule : formule du "point gauche".
>
> 2 - **La méthode des trapèzes** consiste à remplacer les arcs de courbe (MᵢMᵢ₊₁) par les segments [MᵢMᵢ₊₁]. Nous obtenons, sur [aᵢ , aᵢ₊₁], une approximation de l'aire sous la courbe par l'aire du trapèze : de hauteur (aᵢ₊₁ - aᵢ) et de bases f(aᵢ) et f(aᵢ₊₁).

Citation (p.205) : « Bien que cela puisse paraître paradoxal, toute science exacte est dominée par la notion d'approximation » — Bertrand Russel [sic] (1872–1970).

#### Exercices non corrigés (p.206–207)

1. **Ex.1 [P-?] (p.206)** : π/4 est approché par la somme des n premiers termes de Uₙ = (−1)ⁿ/(2n+1), avec U₀ = 1. Demande : 1/ analyse et algorithme de la fonction Un qui renvoie le nᵉ terme ; 2/ analyse et algorithme de la fonction app_pi(n) qui renvoie l'approximation de π.
2. **Ex.2 « Bac Tp 2001 » [P-?] (p.206)** : programme Pascal qui affiche sin(x) pour x proche de 0 avec la formule imprimée « sin(x) = x + (x³/3!) + (x⁵/5!) + (x⁷/7!) + ... » [sic : signes alternés absents, sur l'image comme dans le texte]. Arrêt quand la différence entre deux termes consécutifs est ≤ 10⁻⁴. Le sujet fournit `DEFFN FACT(a : entier) : entier` en 5 lignes.
3. **Ex.3 « Bac Tp 2001 » [P-?] (p.207)** : π/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − … ; programme Pascal qui donne π à 10⁻⁴ près. Arrêt quand la différence entre deux valeurs consécutives est strictement < 10⁻⁴.

Consigne commune aux ex.4 à 6 : « a) Proposez une analyse modulaire au problème, b) Déduisez les algorithmes correspondants. »

4. **Ex.4 [P-?] (p.207)** : suite U₀ = U₁ = 1, Uₙ₊₂ = Uₙ₊₁ + Uₙ (Fibonacci, mot non employé). Demande : 1) calculer les n premiers termes et approcher Uₙ₊₁/Uₙ ; 2) faire le lien avec le nombre d'or φ = (1+√5)/2.
5. **Ex.5 [P-??] (p.207)** : point fixe de f(x) = √(1+x) ; traduire et tester ; programme `Pt_fixe2`.
6. **Ex.6 [P-??] (p.207)** : valeur approchée de ∫₁⁵ (x + 3 sin x) dx par les trapèzes ; programme `Trapeze`.

#### Vocabulaire officiel

algorithme d'approximation ; temps polynomial ; solution « quasi-optimale » ; point fixe ; suite récurrente / relation de récurrence ; convergence ; Epsilon (« Différence entre deux termes consécutifs », « Erreur de l'approximation ») ; deux termes consécutifs ; itérations ; approximation par défaut / par excès ; polygone régulier inscrit / circonscrit ; formule d'Euler ; formule de Wallis ; nombre de Neper / nombre exponentiel ; factorielle ; nombre irrationnel ; intégrale ; aire algébrique ; primitive ; subdivision régulière ; sous-intervalle ; diamètre (longueur) h ; méthode des rectangles (à gauche / à droite / du point milieu ; formule du « point gauche ») ; méthode des trapèzes ; Simpson, Romberg (cités seulement) ; analyse modulaire ; tableau de codification des objets.

#### Notions testables (8)

1. **Point fixe** : définition f(x) = x, réécriture d'une équation g(x) = 0 sous la forme x = f(x), suite Uₙ₊₁ = f(Uₙ), critère d'arrêt |xact − xpre| < ε, compteur d'itérations (`Pt_Fixe`, ex.5).
2. **Schéma général d'approximation par suite** : deux termes consécutifs (S1/S2, P1/P2, xpre/xact), boucle Répéter…Jusqu'à, rôle d'Epsilon, initialisation.
3. **π par Euler** : somme des 1/i², initialisation S2 ← 1, i ← 2, résultat √(6·S2), critère sur √(6S2) − √(6S1).
4. **π par Wallis** : produit, alternance Num/Den gouvernée par i Mod 2, résultat 2·P2.
5. **π par séries alternées** (ex.1, ex.3 Bac) : (−1)ⁿ/(2n+1), π = 4·somme.
6. **e par les factorielles** : fonction Fact, somme 1/i!, critère S2 − S1 < ε ; variante récursive (Application 2).
7. **Rectangles** : variantes gauche / droite / point milieu, h = (b−a)/n, x initial a + h/2 pour le point milieu, avancement x ← x + h, résultat Somme·h.
8. **Trapèzes** : aire h·(f(aᵢ)+f(aᵢ₊₁))/2, boucle sur n sous-intervalles, comparaison avec les rectangles selon n.

Les séries de Fibonacci et du nombre d'or (ex.4) et du sinus (ex.2) peuvent servir d'exercices d'application de la notion 2, sans nouvelle notion.

#### Bornes

- ✅ **INCLUS** :
  - point fixe par itération ;
  - π (Euler, Wallis, série alternée de Leibniz en exercice) ;
  - e (factorielles, itératif et récursif) ;
  - sin(x) par série (exercice Bac) ;
  - suite de Fibonacci et nombre d'or (exercice) ;
  - intégration numérique par les rectangles (gauche, droite, point milieu) et par les trapèzes ;
  - analyse modulaire, algorithme et Pascal de chacun ;
  - tableaux de mesure Epsilon → valeur.
- ⛔ **EXCLU** (cité sans être enseigné, ou absent) :
  - méthodes de Simpson et de Romberg (seulement nommées p.198) ;
  - méthode d'Archimède (décrite sans algorithme) ;
  - dichotomie, balayage et Newton/tangente : **absents de ce chapitre** dans ce manuel ;
  - programmation semi-définie, programmes linéaires (culture, p.188) ;
  - majoration d'erreur théorique et vitesse de convergence (non traitées) ;
  - contenu des pages Lecture (culture).

#### Pages « Lecture » (p.208–212), résumé

- **« L'historique de π » (p.208)** : les valeurs historiques et leurs auteurs sont détaillés dans la note de lecture plus bas.
- **Notation (p.209)** : π est la 1re lettre de « périmètre » en grec, symbole apparu vers 1600 et imposé par Euler (1737 puis 1748).
- **Nature (p.209)** : π n'est pas décimal ; il est irrationnel (Lambert, 1761) et transcendant (Lindemann, 1881).
- **Utilité des décimales (p.209)** : tester la précision des ordinateurs (erreurs détectées sur IBM 590 et R8000) et faire progresser les algorithmes. La page donne les 100 premières décimales.
- **Valeurs approchées célèbres (p.209–210)** : 3,14 ; 22/7 (2 décimales exactes, première réduite de la fraction continue) ; 355/113 (6 décimales exactes). Source citée : http://trucsmaths.free.fr.
- **« Constantes » (p.211)** : tableau Nom / valeur à 4 décimales / description.
  - Constantes listées : i, 0, Champernowne, Copeland-Erdös, Artin, Thue-Morse, oméga, Euler 0,5772, Gompertz, Ramanujan, Catalan 0,9159, 1, lemniscate, φ 1,6180, √2, √3, e 2,7182, π 3,1416, nombre d'argent, Feigenbaum.
- **« Liste d'autres constantes » (p.212)** : 18 constantes physiques (g = 9,8066 m/s², G, c, Avogadro, Planck…). Source : Perso.orange.fr.

#### Note de lecture ch.6

- **Pages sondées en image** : 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, soit 24 pages sur 26. Le chapitre entier a été sondé à cause des écarts. Les p.187–188 n'ont été lues qu'en texte, elles ne contiennent que de la prose.

- **Écarts texte ↔ image (7)** :
  1. p.190 : la capture d'exécution (0.51097, 83 itérations) est absente de la couche texte.
  2. p.191 : dans la formule d'Euler, les dénominateurs 2², 3², n² sont aplatis en « 1 + 1 + 1 / 22 32 n2 ».
  3. p.197 : la figure de l'intégrale est absente du texte ; sur l'image, son étiquette est ∫₀ᵃ f(x)dx, et non ∫ₐᵇ.
  4. p.198 : les trois figures des rectangles (gauche, droite, milieu) n'existent que sur l'image.
  5. p.204 : la formule d'Euler du Retenons perd ses carrés (« 6 12 22 32 42 »).
  6. p.208–211 : le glyphe π est perdu dans la couche texte (« / » ou vide, dans « L'historique de / », « Nature algébrique de / », la ligne π du tableau p.211).
  7. p.211 : la série de Catalan devient « 1/12 - 1/32 » au lieu de 1/1² − 1/3² + 1/5² − …
- Aucun écart sur le code Pascal : il est fidèle partout.

- **Coquilles du manuel `[sic]`, présentes sur l'image comme dans le texte** :
  - p.187 « habilités » ;
  - p.192, 194, 196 : `Epsilon = 10E-4` en Pascal vaut 10⁻³, alors que le tableau de codification annonce 10⁻⁴. Par simulation, `Pi_Euler` s'arrête alors vers 3,112 et `Pi_Wallis` vers 3,1411 ;
  - p.202 : h ← (a1 + b1/n1) dans l'analyse et h ← (a1+b1)/n1 dans l'algorithme, alors que le Pascal p.203 fait (b1−a1)/n1. L'en-tête algorithmique porte « n » et le corps « n1 » ;
  - p.204 : formule de Wallis écrite avec des « + » ;
  - p.205 : le Retenons définit les rectangles par le « point gauche », alors que le programme `Meth_Rec` code le point milieu ;
  - p.206 : série du sinus sans signes alternés ;
  - p.198 contre p.201 : notation des bornes incohérente (a₁ = a … aₙ₊₁ = b, puis a₀, aᵢ = a + i·h) ;
  - p.205 « Russel ».

- **Doutes `[?]`** : aucun. Tout est lisible, et le « 83 » de la capture est confirmé par simulation.

- **Note de génération** : pour les questions de valeur numérique, ne pas reprendre `10E-4` comme s'il signifiait 10⁻⁴. Distinguer clairement point milieu et point gauche, puisque le manuel se contredit sur ce point.

---

### Chapitre 7 — Les algorithmes avancés (p.213–245)

**Objectif officiel (p.213, verbatim)** : « Résoudre des problèmes présentant des degrés de difficultés croissants. »

#### Plan

| § | Titre | Pages |
|---|---|---|
| — | Page de garde | 213 |
| I | Introduction | 214 |
| II | Algorithme de tri : Tri rapide (QuickSort) — II.1 Définitions, II.2 Principes (choix du pivot, partition), Activités 1-3 | 214–220 |
| III | Les tours de Hanoï — III.1 Définition, III.2 Principe, Activités 1-5 | 221–226 |
| IV | Le problème du voyageur de commerce (PVC) — IV.1 Présentation, IV.2 Résolution, Activités 1-5 | 226–234 |
| V | Le problème des huit dames (titre de page de garde : « huits » [sic]) — V.1 Présentation, V.2 Résolution, Activités 1-5 | 234–240 |
| — | Retenons | 241 |
| — | Exercices 1 à 5 | 242–244 |
| — | Lecture : « Le problème du voyageur de commerce : Historique » | 245 |

#### Contenu du cours, paragraphe par paragraphe

- **I. Introduction (p.214)** : le chapitre reprend des domaines déjà vus (tri, optimisation, **backtracking**) à un niveau avancé.

- **II. Tri rapide (p.214–220).**
  - **II.1 Définitions** : aussi appelé « Tri de Hoare », tri **récursif** « dont l'efficacité est une fonction croissante du désordre » du tableau.
  - **II.2 Principe** : on choisit un **pivot** et on le place à sa place définitive par permutations, les éléments inférieurs (ou égaux) à sa gauche et les supérieurs (ou égaux) à sa droite. Cette opération s'appelle **partition**. On recommence récursivement sur chaque sous-tableau tant qu'il n'est pas réduit à un élément.
  - **Choix du pivot** : l'idéal est un pivot qui coupe le tableau en deux moitiés. On peut prendre l'élément du milieu ou le premier élément ; le premier élément représente le **pire cas** quand la séquence est déjà triée.
  - **Partition, pivot en première position (p.215)** : on cherche depuis le 2ᵉ élément un élément plus grand que le pivot (G), puis depuis la fin, en descendant, un plus petit (P), et on les permute. On continue ; quand les indices montant et descendant se rencontrent, on permute le pivot avec l'élément de cet indice.
  - Remarques : « 1- Le pivot est toujours le premier élément » ; « 2- Le tableau est divisé en deux parties », avec un schéma.
  - **Activité 1 (p.215–217), trace détaillée et colorée** : N = 10, T = [10, 6, 13, 8, 19, 2, 1, 31, 3, 11], pivot 10.
    - Échange T[3]=13 ↔ T[9]=3, puis T[5]=19 ↔ T[7]=1, ce qui donne [10, 6, 3, 8, 1, 2, 19, 31, 13, 11].
    - Le pivot est permuté avec la position 6 : [2, 6, 3, 8, 1, 10, 19, 31, 13, 11].
    - Partie gauche (pivot 2) : 6 ↔ 1, ce qui donne [2, 1, 3, 8, 6, …]. Le 3 reste en place (« aucun échange ») ; la position 3 est déclarée définitive. [sic : le pivot 2 n'est pas permuté (il reste en position 1) ; selon le principe de la p.215, il devrait être échangé avec T[2] = 1 et c'est la position 2 qui devient définitive.]
    - Sous-partie 1..2 : on obtient [1, 2, 3, 8, 6, 10, 19, 31, 13, 11].
  - **Activité 2 [P-?] (p.218)** : « Donnez la suite des étapes pour trier tout le tableau T. »
  - **Problème rédigé [P-?] (p.218–220)** : trier par tri rapide un tableau T de n entiers.
    - Programme principal : Proc Remplir(T, n) ; Proc Tri(T, 1, n) ; Proc Afficher(T, n). Le tableau de codification nomme la dernière procédure « Affiche ».
    - Nouveau type : Tab = Tableau de n entiers.
    - Analyse de Tri (p.219) : g et d sont les points de départ gauche et droit, avec arrêt quand d − g = 0. Le pivot est T[g] ; deux compteurs L ← g+1 et M ← d.
  - **Algorithme de la procédure Tri (p.220)**, transcrit verbatim avec les FinTantque / FinSi du manuel :
    ```
    0) Procédure Tri (d, g : Entier)
    1) Si d-g > 0 Alors
        L ← g+1, M ← d
        Répéter
          Tant que (L < M) ET (T[g] > T[L]) Faire L ← L+1 Fin Tant que
          Tant que (L ≤ M) ET (T[g] ≤ T[M]) Faire M ← M-1 Fin Tant que
          Si (L < M) Alors aux ← T[L] ; T[L] ← T[M] ; T[M] ← Aux Fin Si
          L ← L+1 , M ← M-1
        Jusqu'à (M < L)
        aux ← T[g] ; T[g] ← T[M] ; T[M] ← aux
        Proc Tri (g, M-1)
        Proc Tri (M+1, d)
       Fin Si
    2) Fin Tri
    ```
  - **Activité 3 [P-?] (p.220)** : traduire Tri en Pascal et l'intégrer dans un programme `tri_rap`. **Le manuel ne donne aucun code Pascal pour le tri rapide.**

- **III. Tours de Hanoï (p.221–226).**
  - **III.1 Définition** : 3 piquets, n disques de diamètres distincts empilés du plus grand au plus petit, à faire passer au piquet B en s'aidant du troisième. Règles : un seul disque à la fois, uniquement sur un disque plus grand. Une photo accompagne le texte.
  - **III.2 Principe** : on ne peut pas déplacer un disque situé sous un autre, et il faut un **minimum de déplacements**.
  - « Constatation » : déplacer n−1 disques de A vers C, le grand disque de A vers B, puis les n−1 de C vers B. Le schéma place A à gauche, B au milieu et C à droite.
  - **Activité 1 [P-?] (p.222–223)** : n = 2, de A vers B via C ; représenter les étapes en 4 figures et compter. Solution : A→C, A→B, C→B, soit 3 déplacements.
  - **Activité 2 [P-?] (p.223)** : n = 3 ; donner les déplacements, puis généraliser.
    - Solution en 7 déplacements : d1 A→B, d2 A→C, d1 B→C, d3 A→B, d1 C→A, d2 C→B, d1 A→B.
    - Tableau pour n = 1 à 9 : 1, 3, 7, 15, 31, 63, 127, 255, 511, avec la ligne de constatations 2¹−1 … 2⁹−1. Conclusion : **2ⁿ − 1**.
  - **Activité 3 [P-?] (p.224–225)** : procédure récursive Hanoï pour n ∈ [1, 64].
    - Algorithme : `0) Algorithme Procédure Hanoï (n : octet ; départ, cible, intermédiaire : octet)` ; `1) Si (n > 0) Alors Proc Hanoï (n-1, départ, intermédiaire, cible) ; Ecrire ("Disque du piquet ", départ " vers le piquet ", intermédiaire) ; Proc Hanoï (n-1, cible, départ, intermédiaire) Fin Si` ; `2) Fin Hanoï`.
    - Pascal `Tours_Hanoi` : `Procedure Hanoi (n: Byte ; depart, but, inter : Byte)`, saisie contrôlée par `Until n IN [1 .. 64]`, appel `Hanoi (n, 1, 3, 2)`.
  - **Activité 4 [P-?] (p.225)** : modifier le programme pour afficher le nombre de déplacements.
  - **Activité 5 « La légende » [P-?] (p.225–226)** : 64 disques sacrés et la prophétie « Le temple s'écroulera avant que les disques soient mis en place. » Question : « Qu'en pensez-vous? »

- **IV. Voyageur de commerce (p.226–234).**
  - **IV.1 Présentation** : visiter n villes une et une seule fois et revenir au départ en minimisant la distance (ou le temps, ou le coût). Illustration par une carte du Nord-Est tunisien : Tunis, Bizerte, Nabeul, Hammamet…
  - Les solutions exactes demandent graphes et arbres, « qui ne font pas partie de votre programme ». **Stratégie retenue : aller à chaque étape à la ville non visitée la plus proche** de la ville en cours Vc (heuristique gloutonne du plus proche voisin, terme non employé par le manuel).
  - **Activité 1 [P-?] (p.227–231)** : analyse et algorithmes pour afficher l'itinéraire de n ≤ 20 villes.
    - Structures de données :
      - constante nbmaxville = 20 ;
      - vecteur Nom_Ville(s) de chaînes (type NV) ;
      - matrice carrée Distance de réels (type Dist) ;
      - vecteur Visite de booléens (type Visit, initialisé à Faux) ;
      - vecteur Trajet d'entiers (type Traj) ;
      - v_départ ;
      - n.
    - Les villes sont repérées par leurs indices 1..n.
    - Programme principal : Saisie_liste(n, Nom_Ville, Distance) ; Saisie_ville_départ(v_départ) ; Former_Trajet(n, Distance, v_départ, Visite, Trajet) ; Affichage_Trajet(Trajet, n, Nom_Villes).
    - Saisie_liste : n ∈ [1..nbmaxville] par Répéter ; boucles imbriquées de lecture des noms et de Distance[i,c].
    - Former_Trajet : Visite[i] ← Faux ; Trajet[1] ← v_départ ; Pour i de 2 à n {j ← FN Ville_proche_non_visit(i, Distance, Visite, n) ; Trajet[i] ← j ; Visite[j] ← Vrai}.
    - Ville_proche_non_visit : ind ← première ville non visitée (Tant que Visite[j] = Vrai : j ← j+1), puis Pour j de j+1 à n, Si Visite[j] = Faux et Distance[i,j] < Distance[i,ind] Alors ind ← j.
    - Affichage_Trajet : affiche Nom_Villes[Trajet[i]] pour i = 1..n, puis **Nom_Villes[Trajet[1]]** (retour au départ).
  - **Activité 2 [P-?] (p.231–233)** : programme Pascal `voyageur` complet, avec les types NV = Array[1..Nbmaxville] of String[20], Dist, Visit, Traj.
  - **Activité 3 [P-?] (p.233)** : accepter plus de 20 villes et comparer les temps d'exécution.
  - **Activité 4 [P-?] (p.234)** : dossier de recherche Internet sur le PVC.
  - **Activité 5 [P-?] (p.234)** : autre solution avec la même stratégie mais une structure **enregistrement** par ville (nom, distances), en Pascal.

- **V. Huit dames (p.234–240).**
  - **V.1 Présentation** : placer 8 reines sur un échiquier 8×8 sans menace mutuelle (même rangée, colonne ou diagonale) ; cas général n dames sur n×n.
  - Histoire : problème posé en 1850 par Franz Nauck ; méthode de S. Gunther en 1874 par les déterminants, affinée par J.W.L. Glaisher.
  - **Tableau du nombre de solutions (p.235)** : n = 1 → 1 ; 2 → 0 ; 3 → 0 ; 4 → 2 ; 5 → 10 ; 6 → 4 ; 7 → 40 ; **8 → 92** ; 9 → 352 ; 10 → 724 ; 11 → 2680 ; 12 → 14200 ; 13 → 73712 ; 14 → 365596 ; 15 → 2279184.
  - « Le problème des huit dames a 92 solutions distinctes. »
  - Deux échiquiers solutions sont dessinés (image seulement, colonnes a–h, rangées 1–8).
  - **Activité 1 [P-?] (p.235)** : représenter d'autres solutions sous forme d'échiquier.
  - **Activité 2 [P-?] (p.235–238)** : afficher les positions et le nombre de solutions.
    - Programme principal : solution ← 0 ; Proc Init(TD, nbd) ; Proc Place_dame(TD, 1) ; Ecrire(« Nombre de solutions = », solution).
    - Codification : nbd constante = 8 ; Tab = tableau de nbd entiers ; TD ; solution.
    - Représentation : l'indice i donne la ligne et T[i] la colonne.
    - Test de menace : `Si ((T[j] = i) ou (Abs(T[j] - i) = Abs(j - ndames)))` → `Aller à Suivant` (GoTo vers l'étiquette `suivant`), avec la procédure prédéfinie **Continue** « disponible dans les versions 5, 6 et 7 de Turbo Pascal ».
    - Sinon T[ndames] ← i et appel récursif Place_dame(T, ndames+1) ; quand ndames = nbd+1, Proc Affiche puis solution ← solution + 1.
    - Affiche : grille de « 1 » (dame) et de « 0 ».
  - **Algorithme de Place_dame (p.238)**, transcrit verbatim avec les Fin Si / Fin Pour du manuel :
    ```
    0) Procedure Place_dame (T : Tab ; ndames : Entier)
    1) Si (ndames = nbd+1) Alors Proc Affiche (T, nbd) ; solution ← solution + 1 Fin Si
    2) Pour i de 1 à nbd Faire
         Pour j de 1 à ndames Faire
           Si ((T[j] = i) ou (Abs (T[j] - i) = Abs (j - ndames))) Alors Aller à Suivant Fin Si
         Fin Pour
         T[ndames] ← i
         Proc Place_dame (T, ndames+1)
         suivant : Continue
       Fin pour
    3) Fin Place_dame
    ```
  - **Activité 3 [P-?] (p.238–240)** : programme Pascal `huitdames` complet (`Label suivant`, `GoTo suivant`, `suivant : continue;`).
  - **Activité 4 [P-?] (p.240)** : faire varier le nombre de dames et comparer le temps d'exécution et le nombre de solutions.
  - **Activité 5 [P-?] (p.240)** : dossier de recherche Internet sur le problème.

#### Encadré « Retenons » (verbatim, p.241)

> • Les algorithmes cités dans ce chapitre sont d'un degré de difficultés élevé, à savoir :
> - Une méthode de tri : Le tri rapide (en anglais QuickSort),
> - Des algorithmes avancés d'optimisation tels que les tours de Hanoï et le voyageur du commerce,
> - Un algorithme faisant appel à la technique du retour sur trace (backtracking) tel que le problème des huits dames,
>
> • Le tri rapide consiste à trier un tableau en le découpant récursivement en 2 sous tableaux, où les éléments du premier tableau sont inférieurs aux éléments du second. Le tableau initial est donc découpé en sous tableaux de plus en plus petits, jusqu'à arriver à un sous tableau à un seul élément, qui est donc forcément trié. Ensuite, en remontant, les éléments sont triés petit à petit.
>
> • Le problème des tours de Hanoï est un jeu de réflexion imaginé par le mathématicien français Édouard Lucas, et consistant à déplacer des disques de diamètres différents d'une tour de «départ» à une tour d'« arrivée » en passant par une tour « intermédiaire » et ceci en un minimum de coups.
>
> • Le voyageur de commerce souhaite passer par toutes les villes d'un parcours, c'est à dire par le trajet le plus court, sans passer deux fois au même endroit. La solution de ce problème répond à la question suivante : Quel est le trajet le plus court qui passe par toutes les villes?
>
> • Le retour sur trace, (en anglais backtracking), consiste à revenir légèrement en arrière sur des décisions prises afin de sortir d'un blocage.
>
> • Le problème des huit dames consiste à placer huit dames sur un échiquier sans qu'elles puissent se prendre entre elles.

#### Exercices non corrigés (p.242–244)

1. **Ex.1 [P-??] (p.242)**, tri comptage (ou « tri casier ») : on crée un tableau intermédiaire des occurrences, indicé par les valeurs, puis on reconstruit le tableau.
   - Exemple : T = [10, 2, 13, 8, 9, 2, 13, 3, 13, 11] ; T_intermediaire[0..13] = [0, 0, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 3] ; résultat [2, 2, 3, 8, 9, 10, 11, 13, 13, 13].
   - Q1 : appliquer la méthode au tableau de 26 valeurs [2, 12, 3, 18, 9, 10, 1, 13, 3, 13, 1, 9, 9, 22, 11, 6, 12, 3, 4, 5, 6, 5, 5, 3, 5, 6].
   - Q2 : a) découpage en modules et algorithmes ; b) programme Pascal `TRI_COMPTAGE`.
2. **Ex.2 [P-??] (p.242)** : chercher sur Internet les algorithmes du tri par création, du tri radix et du tri par permutation, puis donner analyse et Pascal pour chacun.
3. **Ex.3 « Sujet de baccalauréat 1992 » [P-??] (p.243)**, permutations de n objets dans l'ordre lexicographique. L'algorithme en 4 étapes fourni par le sujet :
   1. plus grand i tel que T(i−1) < T(i) ;
   2. plus grand j tel que T(i−1) < T(j) ;
   3. permuter T(i−1) et T(j) ;
   4. renverser T(i)…T(n).

   On part de l'identité (1, …, n), et la dernière permutation est (n, …, 1). Questions :
   - A) n = 4 : 1) prouver que (1,2,3,4) donne (1,2,4,3) ; 2) transformer (1,4,3,2) et (4,3,2,1) ;
   - B) fonctions PGI (renvoie 0 si aucun i ne convient) et PGJ(r), procédures PERMUT(k, L) et RENVERSE(k), programme principal qui affiche toutes les permutations ;
   - C) traduction Pascal.
4. **Ex.4 [P-??] (p.244)**, PVC par insertion : partir de l'itinéraire 1–2, insérer chaque ville Pᵢ (i = 3..N) à la position qui minimise la longueur ; en cas d'égalité, prendre la dernière dans une exploration gauche-droite. Demande : 1) mise en œuvre, 2) structures de données, 3) analyse et algorithmes, 4) Pascal.
5. **Ex.5 [P-??] (p.244)**, PVC par énumération des permutations : un chemin est une permutation de (0, …, n−1) ; sa longueur est la somme des d(Pᵢₖ, Pᵢₖ₊₁) avec iₙ = i₀. Renvoie à l'ex.3. Demande : 1) recherche Internet d'un algorithme de permutations, 2) analyse et algorithmes, 3) Pascal.

#### Vocabulaire officiel

tri rapide / QuickSort / tri de Hoare ; pivot ; partition ; permutation (échange) ; sous-tableau ; récursivité / procédure récursive ; pire des cas ; tours de Hanoï ; piquet de départ / cible (arrivée) / intermédiaire ; disque ; minimum de déplacements ; 2ⁿ − 1 ; problème du voyageur de commerce (PVC) ; itinéraire / trajet ; ville la plus proche non encore visitée ; matrice des distances ; vecteur Visite (booléen) ; optimisation ; problème des huit dames (reines) / n dames ; échiquier ; rangée, colonne, diagonale ; retour sur trace / backtracking ; étiquette (Label), branchement inconditionnel Aller à / GoTo, procédure Continue ; tri comptage / tri casier ; tableau intermédiaire (occurrences) ; permutations de n objets.

#### Notions testables

Il y a plus de 8 notions possibles : découpage proposé en 2 chapitres :

**7a — Tri rapide et Hanoï (récursivité « diviser pour régner »)**
1. Principe du tri rapide : pivot (premier élément), partition, placement définitif, appels récursifs sur g..M−1 et M+1..d.
2. Trace d'une partition sur un tableau donné (modèle de la première partition p.215–216, pivot 10 — la suite p.217 est incohérente : indices i/j, échanges successifs, position finale du pivot).
3. Choix du pivot : milieu ou premier ; pire cas quand le tableau est déjà trié ; efficacité croissante avec le désordre.
4. Hanoï : décomposition récursive (n−1 vers l'intermédiaire, le grand disque vers la cible, n−1 vers la cible), séquence des déplacements pour n = 2 et n = 3.
5. Nombre de déplacements 2ⁿ − 1 (tableau de n = 1 à 9 ; légende des 64 disques).
6. Tri comptage (exercice) : tableau des occurrences et reconstruction.

**7b — Optimisation gloutonne et backtracking**
1. PVC : énoncé (cycle hamiltonien de longueur minimale, mot « hamiltonien » non employé dans le cours), stratégie de la ville non visitée la plus proche, structures (matrice Distance, vecteurs Visite et Trajet), retour au départ dans l'affichage.
2. Fonction Ville_proche_non_visit : recherche d'un minimum sous condition.
3. Autres approches du PVC (exercices) : insertion, énumération des permutations (successeur lexicographique, Bac 1992).
4. Huit dames : contrainte ligne/colonne/diagonale, représentation T[i] = colonne de la dame de la ligne i, test |T[j] − i| = |j − ndames|.
5. Backtracking : définition du Retenons, placement récursif, abandon d'une branche (GoTo suivant / Continue), comptage des solutions (92 pour n = 8 ; tableau n = 1..15).

#### Bornes

- ✅ **INCLUS** :
  - tri rapide (algorithme + trace ; Pascal à écrire par l'élève) ;
  - Hanoï (algorithme + Pascal + formule 2ⁿ−1) ;
  - PVC par plus proche voisin (algorithme + Pascal complet) ;
  - n dames par backtracking (algorithme + Pascal complet) ;
  - en exercices : tri comptage, permutations lexicographiques (Bac 1992), PVC par insertion et par permutations.
- ⛔ **EXCLU** :
  - graphes et arbres (déclarés hors programme p.226) ;
  - solutions exactes ou optimales du PVC et méthode cutting-plane (Lecture seulement) ;
  - méthode des déterminants pour les dames (historique) ;
  - analyse de complexité formelle (O(n log n), etc. : jamais énoncée) ;
  - tri radix, par création et par permutation (renvoyés à une recherche Internet, ex.2) ;
  - pivot du milieu en algorithme (évoqué seulement, aucun code) ;
  - **dichotomie, balayage, Newton : absents de ce chapitre également.**

#### Page « Lecture » (p.245), résumé

« Le problème du voyageur de commerce : Historique » :
- 19ᵉ siècle : Hamilton et Kirkman ; « Hamilton's Icosian game », une tournée par 20 points ;
- 1930 : Karl Menger (Harvard), puis Hassler Whitney et Merril Flood (Princeton) ;
- 1954 : 49 villes résolues par Dantzig, Fulkerson et Johnson (cutting-plane) ;
- 1975 : 100 villes (Camerini, Fratta, Maffioli) ;
- 1987 : 532 puis 2392 villes (Padberg, Rinaldi) ;
- 1998 : les 13 509 villes des États-Unis ;
- 2001 : 15 112 villes d'Allemagne (Applegate, Bixby, Chvàtal, Cook ; universités de Rice et Princeton).

#### Note de lecture ch.7

- **Pages sondées en image** : 215, 217, 221, 222, 223, 226, 234, 235, 236, 237, 238, 239, 240, 242, soit 14 pages sur 33.
  - La section V a été sondée en entier (p.234–240) à cause d'un écart.
  - Pour les sections II à IV, les traces, les figures et la carte ont été sondées, sans aucun écart sur le texte.
  - Lues en texte seulement : 213, 214, 216, 218–220, 224, 225, 227–233, 241, 243–245.
- **Écarts texte ↔ image (3)** :
  1. p.235 : les deux échiquiers solutions n'existent que sur l'image (positions : voir les figures ; non transcrites case par case) ;
  2. p.242 : la mise en page du tableau de 26 valeurs de la Q1 est disloquée en texte, insérée au milieu de la Q2a. L'image a la même mise en page ; c'est l'image qui permet de rattacher le tableau à la Q1 ;
  3. p.221–223 : les figures des piquets et des étapes (A à gauche, B au milieu, C à droite ; état final sur B) ne sont que sur l'image.
- **Coquilles et incohérences `[sic]`** :
  - p.213 et p.241 « huits dames » ; p.214 « à ses problèmes », « vous alliez » ;
  - p.217 « la partie droite dont les indices allant de 3 à 5 » : ce devrait être 4 à 5 ; « et maintenant triée » ;
  - p.218 : programme principal « Afficher » contre « Affiche » dans le tableau ; appel Tri(T, 1, n) à 3 arguments contre en-tête p.220 « Tri (d, g : Entier) » (ordre inversé, T absent) ;
  - p.224 : l'algorithme Hanoï écrit « vers le piquet », intermédiaire, et appelle Hanoï(n−1, départ, intermédiaire, cible). En pratique, le 3ᵉ paramètre effectif joue le rôle de cible, et les noms sont permutés. Le Pascal (`depart, but, inter`, appel `Hanoi(n,1,3,2)`) envoie bien la tour sur le piquet 2, mais avec des noms trompeurs ;
  - p.229–230 : l'analyse appelle Ville_proche_non_visit(i, Distance, n) avec 3 arguments, l'algorithme avec 4. L'algorithme de Former_Trajet oublie Visite[v_départ] ← Vrai, que le Pascal p.233 contient ;
  - **p.230–232, défaut de fond** : la fonction compare Distance[i, j], où i est le **rang** dans Trajet, et non la ville courante Trajet[i−1]. L'heuristique décrite (« ville la plus proche de la ville en cours ») n'est donc pas celle que code le manuel ;
  - p.237–240 : la boucle « Pour j de 1 à ndames » inclut j = ndames, et à ndames = 9 elle lit T[9] hors bornes. C'est sans effet sur le résultat (92), mais le code n'est pas propre ;
  - p.229 « Pour de c de 1 à n » ; p.244 « procèdons ».
- **⚠️ Défaut algorithmique majeur, p.220 (Tri)**, vérifié par simulation fidèle de l'algorithme transcrit :
  - [2, 1] reste [2, 1] (non trié) ;
  - pour [1, 2], M tombe à g−1 = 0, ce qui donne un accès hors tableau (T[0]) ;
  - sur le tableau même de l'Activité 1, l'algorithme finit par accéder à T[0].
  - **Seule la première partition (pivot 10, p.215–216) sert de trace de référence** ; la suite de la p.217 est incohérente avec le principe (voir le [sic] de la partie gauche, pivot 2).
  - **Recommandation pour la génération** : tester le **principe** et la **trace** de la première partition, mais ne pas présenter l'algorithme p.220 comme une référence correcte, et ne pas fabriquer de questions « que produit ce code ? » à partir de lui.
- **Doutes `[?]`** : aucun.

---

### Bibliographie / Webographie (p.246–247)

- **Bibliographie** (10 titres) : Mathématiques 3ᵉ SI (CNP 2006) ; Mastering C (G. Bolon, 1988) ; Programmation Pascal avec TP (B.S. Gottfried, Schaum) ; Computer studies for you (S. Doyle, 1987) ; A practical introduction to Pascal (Wilson & Addyman, 1982) ; A structured programming approach to data (D. Coleman, 1982) ; Initiation à l'analyse et à la programmation (J.P. Laurent, Dunod 1985) ; Aide-mémoire de Turbo Pascal (De Groote & Virga, Marabout) ; Understanding computer science for advanced level (R. Bradley, 1987) ; L'informatique en Sup et en Spé (B. Petazzoni, Ellipses).
- **Webographie** (17 URL) : wikipedia, univ-paris12 (récursivité Ada), publimath, lesfractales, supinfo-projects, journaldunet, AlgAnim (Auckland), fh-flensburg, mathworld, physinfo.ulb, recreomath, mathgoodies, Petrequin, ac-creteil, f.nicolier, pi314.net, techno-science.net.

---

## Fiche de lecture ch.6-7

- **pagesLues** : 187–247, soit 61 pages, couche texte L1 pour toutes. La préface et la légende (p.2–6) n'ont pas été relues, comme demandé.
- **Pages sondées en image** (110 dpi), 38 pages :
  - ch.6 : 189–212, soit 24 pages ;
  - ch.7 : 215, 217, 221, 222, 223, 226, 234, 235, 236, 237, 238, 239, 240, 242, soit 14 pages.
  - Taux : 38/61, soit 62 % (≥ 1 page sur 10).
  - Sondage étendu à toute la section là où un écart a été trouvé : ch.6 en entier, ch.7 §V en entier.
- **Nombre d'écarts texte ↔ image** : 10 (7 au ch.6, 3 au ch.7).
  - Ils portent tous sur des formules aplaties, des exposants perdus, le glyphe π perdu ou des figures absentes de la couche texte.
  - **Aucun écart sur le code Pascal ni sur les algorithmes.**
- **Coquilles `[sic]` relevées** : environ 20, dont 3 de fond à signaler au générateur :
  - `10E-4` ≠ 10⁻⁴ (ch.6) ;
  - rectangles « point gauche » dans le Retenons contre « point milieu » dans le programme (ch.6) ;
  - **algorithme Tri rapide p.220 incorrect** (ch.7), et heuristique PVC codée sur le rang au lieu de la ville courante (ch.7).
- **Fichiers temporaires** : couche texte et PNG dans `/tmp/claude-0/-home-user/557356fe-6efe-5bc8-99c5-51f1e0914df0/scratchpad/ch67/`. Rien n'a été copié dans git.

## 5. Chapitrage retenu (→ `manifest/bac-info.json`)

Règle : ≤ 8 notions par chapitre (`campagne`, étape 4). Les chapitres 1, 5 et 7 du manuel dépassent 8 notions
(12, 8 « au plus juste », 11) : ils sont scindés selon le découpage proposé par leurs lecteurs. Les exercices de
fin de chapitre se répartissent selon la notion qu'ils mobilisent (ch.1 ex.1-14 p.68-71 ; ch.5 ex.1-8 et 10-12 → 5a,
ex.9 et 13-16 → 5b, ex.1 mixte : a → 5a, b-d → 5b ; ch.7 ex.1-2 → 7a, ex.3-5 → 7b).

| # | slug | notion | pages |
| --- | --- | --- | --- |
| 1 | `01a-enregistrements` | Les enregistrements (ch.1 A) | 7-31 |
| 2 | `01b-fichiers` | Les fichiers (ch.1 B) | 32-72 |
| 3 | `02-recursivite` | La récursivité (ch.2) | 73-94 |
| 4 | `03-algorithmes-de-tri` | Les algorithmes de tri (ch.3) | 95-122 |
| 5 | `04-algorithmes-recurrents` | Les algorithmes récurrents (ch.4) | 123-150 |
| 6 | `05a-arithmetique` | PGCD, dénombrement, divisibilité (ch.5) | 151-166 |
| 7 | `05b-bases-de-numeration` | Conversions entre bases (ch.5) | 166-186 |
| 8 | `06-algorithmes-approximation` | Les algorithmes d'approximation (ch.6) | 187-212 |
| 9 | `07a-tri-rapide-hanoi` | Tri rapide, Hanoï, tri comptage (ch.7) | 213-226 |
| 10 | `07b-voyageur-huit-dames` | Voyageur de commerce, huit dames, retour sur trace (ch.7) | 226-245 |

> `[?]` Les chapitres 2 et 3 portent chacun 8 notions : gardés entiers ; le ch.3 a un découpage possible
> (« insertion & Shell » / « fusion, classement & autres tris »). Choix éditorial à confirmer par Mohamed.

## 6. Sources croisées et incertitudes

- **Source unique** : `4sci_AP.pdf` (voir l'en-tête). Aucun guide enseignant, aucun programme officiel ministériel
  au corpus (R-3) : le manuel prime. Bibliographie/webographie p.246-247 : résumées en fin de section ch.7.
- **Lecture** : p.7-247 lues en couche texte ; sondage image — ch.1 40/66 p. (2 écarts) ; ch.2-3 18/50 (5) ;
  ch.4-5 64/64 (20 pages touchées) ; ch.6-7 38/61 (10). Les écarts portent sur des formules, exposants, symboles
  ou figures ; **aucun sur le code Pascal ni sur les algorithmes**. Détail dans la « Fiche de lecture » de
  chaque section.
- **À valider** : (1) ~~relecture R-7~~ faite le 2026-11-07 (2 auditeurs opus indépendants, 0 BLOCKER, 16 constats corrigés puis revérifiés) ; (2) code CNP du manuel ; (3) niveaux de
  difficulté par exercice ; (4) sujets d'examen du Bac informatique (non au Drive à ce jour).
