# Re-vérification — lot L06, français 9ᵉ (devoirs, salle blanche)

Auditeur indépendant, 2026-10-16.

Commit vérifié : `4e3765f7` (`wip/gisement-francais-9eme`), contre l'état d'avant audit `9dc08eb7`. Journal lu : `auteurs-notes/fr-L06/CORRECTIONS.md`. Rien n'a été écrit dans `content/` ni dans git.

Le diff du commit touche aussi des fichiers d'autres lots : 03/06, 08/06, 13/xx et le `06-examens` du ch. 04/09. Ils sont hors périmètre et n'ont pas été jugés ici.

## Gates

- `content:check` : vert (29 623 questions, soit −2 suppressions ; 1 067 étiquettes).
- `content:qa:strict` : 0 erreur ; aucun avertissement sur les chapitres 02, 03, 06, 11 et 15, cours et résumé du ch. 11 compris.
- `content:tranche --subject french --chapters 02,03,06,11,15` :
  - clé strictement la plus longue : 2/258, hors lot ;
  - positions des clés : 26/24/25/24 % ;
  - 6 paires proches, **aucune dans le lot** (toutes préexistantes, hors fichiers `devoir`).
- `content:gisement:controle` : 38 textes, 0 plage de 6 ou 8 mots, 0 donnée commune ✓.

## Majeurs : application et justesse

Chaque question modifiée a été re-résolue à l'aveugle avant de lire la clé.

| # | lieu | appliqué | re-résolution / contrôle |
| --- | --- | --- | --- |
| M1 | 02/10 Q4 supprimée | ✓ | 6 q., rampe 2-2-2-3-3-3 |
| M2 | 02/11 Q3 (Tarek, *ne* explétif) | ✓ | « … de peur que la pluie n'entre. » = clé c ✓ ; longueurs 56/47/52*/52 ; étiquettes justes |
| M3 | 02/11 Q4 (« de leur mère » retiré) | ✓ | clé b ✓ ; 69/72*/69/72 ; vote nul |
| M4 | 06/09 Q2 supprimée | ✓ | 7 q. |
| M5 | 06/09 Q4 (cinéma) | ✓ | « avait commencé » = clé c ✓ ; « venait de commencer » muette ; explication juste |
| M6 | 06/09 Q5 (conseil, condition sans « si », futur du passé) | ✓ | l1→r3, l2→r1, l3→r2 ✓ ; aucune fuite vers Q7 |
| M7 | 06/09 Q6 (déjà / encore) | ✓ | « avait terminé ; terminait » = clé d ✓ ; grille 2×2, vote nul ; seule c porte une étiquette, et elle est juste |
| M8 | 03/07 Q1 (manquer) | ✓ | « manqué le penalty » = clé a ✓ ; 30*/30/30/29 |
| M9 | 03/07 Q6 (succéder à) | ✓ | « pas de COD » = clé a ✓ ; plus de fuite depuis Q3 |
| M10 | 03/07 Q4 b « prévenues » | ✓ | clé c ✓ ; vote sur le participe : prévenues ×2, pas la clé |
| M11 | 03/07 Q5 (auraient été) | ✓ | clé d ✓ ; grille 2×2 exacte ; 51/49/50/50* |
| M12 | 15/06 Q7 d–e (programmer) | ✓ | ordre c d e b a unique ✓ ; plus de copie de la clé de Q2 |
| M13 | 15/06 Q4 a (« Un samedi pas comme les autres ») | ✓ | la clé d (47) n'est plus la plus courte |
| M14 | 15/06 Q4–Q5 (Jebel Zaghouan, au sud de Tunis) | ✓ | fiche, options et explication cohérentes ; Q5 : clé 116 < c 118 |
| M15 | 15/06 Q5, explication | ✓ | plus aucun rang cité |
| M16 | 11/07 Q4 (fêtes familiales) | ✓ | « familiales » = clé c ✓ ; 19/19/20*/20 |
| M17 | ligne nature/fonction, ch. 11 | ✓ | voir plus bas |

(* = clé)

## Mineurs demandés

- **m1** — 02/11 Q5 (Nadia, imprimante) ✓. La clé d (84) est sous b (85) ; b porte `subjonctif-abusif`.
- **m2** — 02/11 Q6 : la liste du rappel comprend « moins… plus… » ✓. La clé reste a, unique.
- **m5** — 11/07 Q6 d « une assiette soupe » ✓. La clé (20) n'est plus la plus courte, et l'explication est conforme.

## Étiquette `fr.mode.subjonctif-abusif`

- Libellés fr, en et ar élargis dans `content/misconceptions.json`, conformes au texte de l'audit. L'arabe est juste : « subjonctif … indicatif », et non « صيغة شرطية ».
- L'emploi existant en `05/06` reste couvert par le libellé.
- Posée sur les 4 placements, chacun à une seule erreur :
  - 02/10 Q4 c (ex-Q5) « Après que le car soit arrivé » ;
  - 02/11 Q5 b ;
  - 06/09 Q1 d « fasse » ;
  - 06/09 Q2 c (ex-Q3) « prenne ; pleuve ».
- 02/10 Q5 a (deux erreurs) reste muette ✓.

## Ligne de cours, ch. 11

- `cours.md` : la ligne est insérée après « Chaque expansion se rattache à un nom… » ; `resume.md` : la puce est ajoutée en 2ᵉ position. Les deux sont conformes au texte proposé.
- Q2 de 11/07 est désormais couverte, et l'exemple « de la voiture » ne livre pas « de laine ».
- Remarque de forme, sans effet : la ligne de `cours.md` tient sur une seule ligne, alors que le fichier coupe ses lignes vers 100 caractères. `qa:strict` ne relève rien.

## Salle blanche, sur les remplacements

Mots recherchés dans les 8 instantanés : Tarek, pluie, Nadia, imprimante, exposé, cinéma, film, vaudrait, puzzle, Samia, manquer, penalty, succéder, tante, Zaghouan, programmer, familial, fêtes, « n'entre », « plus on ». Aucun n'y figure. Occurrences fortuites, sans rapport :
- « fenêtre » apparaît dans un texte littéraire de D06 ;
- « parcours » dans D07, au sens sportif ;
- « Tunisie » et « tunisienne » dans D07.

Un seul rapprochement : **« terminer ses devoirs »** figure dans le texte littéraire de D01 (l. 38), et 06/09 Q6 a « son frère ___ (terminer) déjà ses devoirs ».
- C'est une collocation banale de 3 mots, dans un texte (pas un exercice) d'un devoir qui ne relève pas de la carte 06/09 ; l'outil ne relève rien.
- **Non bloquant.** Variante facultative, si le pilote veut zéro recoupement :
  - Énoncé : `Dans un récit au passé : « Quand Salma rentra, son frère ___ (ranger) déjà sa chambre, et sa sœur ___ (ranger) encore la sienne. » Quelles formes conviennent, dans l'ordre ?`
  - a (22, muette) `rangeait ; avait rangé`
  - b (25, muette) `avait rangé ; avait rangé`
  - c (19, `fr.temps.anteriorite-non-marquee`) `rangeait ; rangeait`
  - d (clé, 22) `avait rangé ; rangeait`
  - Dans l'explication, remplacer « terminé » par « rangé » et « terminait » par « rangeait ».

## Nouveaux défauts introduits par les corrections

Aucun. J'ai vérifié sur toutes les questions retouchées :
- l'autonomie de chaque énoncé ;
- l'absence de fuite entre questions (les explications de 06/09 Q4 et Q6 énoncent la règle du plus-que-parfait, sans clé) ;
- les étiquettes sur les options à deux erreurs ;
- l'absence de marqueur ;
- la clé jamais strictement la plus longue.

## Verdict

**Prêt à livrer.** Les 17 majeurs et les mineurs m1, m2 et m5 sont appliqués et justes. L'étiquette est élargie et posée, la ligne de cours est ajoutée, et les gates sont verts sur le lot. Seule réserve, facultative : « terminer ses devoirs » en 06/09 Q6.
