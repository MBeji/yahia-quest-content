# go-live — le programme POC → production

**Entrée : [`00-MASTER-PLAN.md`](./00-MASTER-PLAN.md).** Tableau de bord des chantiers,
Go/No-Go, protocole de session.

## Pourquoi ce dossier est ici

Il a vécu jusqu'au 2026-08-02 dans le wrapper `YahiaAcademy/go-live/`, **hors de tout dépôt
git** : pas d'historique, pas de revue, aucune sauvegarde qu'une copie sur un disque — et
91 MB dont 90 de binaire k6. Il rejoint `FableEtudes/` parce que c'est la même nature de
travail : de la conception qui se planifie, s'arbitre et se journalise. Les études disent
_quelle capacité produit construire_ ; le go-live dit _à quelles conditions on la met en
production_. Ils partagent la feuille de route ([`STATUS.md` §6](https://github.com/MBeji/yahia-quest-arena/blob/main/STATUS.md)) et le même jalon de rentrée.

## Ce qui a été élagué au versement

| Retiré                                                              | Pourquoi                                                                                                        |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `livrables/02-audit-technique/charge/bin/` (k6.exe + zip, **90 MB**) | Un binaire ne va pas dans git — le `.gitignore` du dossier le disait déjà. k6 se réinstalle en une commande.     |
| `livrables/02-audit-technique/charge/data/` (runs k6)               | Exclu par le même `.gitignore` : les jeux de données de charge peuvent contenir des clés de réponses extraites. |
| `_sauvegarde-2026-07-11/`                                           | Copie pré-édition d'avant la passe de rationalisation. Git fait ce travail mieux, maintenant.                    |
| `.obsidian/`                                                        | Configuration d'éditeur.                                                                                        |

**Rien de documentaire n'a été supprimé.** Deux journaux ont été **sortis**, pas coupés :
le §7 du master plan (46 événements) et l'historique du backlog (23 mouvements) vivent
désormais dans [`journal.md`](./journal.md), intacts. Le tableau de bord et le backlog ont
été **compressés** : un chantier clos tient en une ligne, un GAP soldé aussi. 292 KB → 43 KB
pour les trois fichiers de pilotage.

## Carte

| Fichier                                                          | Rôle                                                                                    |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [`00-MASTER-PLAN.md`](./00-MASTER-PLAN.md)                       | **Entrée** — tableau de bord, ce qui bloque la Porte 1, phasage, Go/No-Go, protocole     |
| [`90-backlog-remediation.md`](./90-backlog-remediation.md)       | Entonnoir unique des constats actionnables — 34 ouverts, 20 soldés, GAP-NNN jamais réutilisé |
| [`91-actions-mohamed.md`](./91-actions-mohamed.md)               | Ce qui ne peut pas se faire depuis un dépôt : DNS, comptes tiers, démarches               |
| [`journal.md`](./journal.md)                                     | Mémoire append-only du programme (événements + mouvements de backlog)                     |
| [`PASSATION.md`](./PASSATION.md)                                 | Dossier de passation global — le projet entier en un document                             |
| `01`…`08`                                                        | Un fichier par chantier ; les clos gardent leur détail, ils ne se racontent plus dans le tableau de bord |
| `livrables/`                                                     | Rapports, checklists et outils produits par les chantiers                                 |

## Règle de tenue

Inchangée : une session = **un** chantier, plan validé avant exécution, et avant de s'arrêter
on met à jour la « Prochaine action » du chantier **et** le tableau de bord. Une décision
structurante s'ajoute au [journal](./journal.md) ; elle ne se réécrit pas.

Une chose de plus depuis le 2026-08-02, apprise en re-vérifiant les P1 : **un statut se
constate, il ne se déduit pas.** GAP-024 était réputé traité parce qu'une PR le citait dans
son titre — la moitié du gap (suppression de compte, export des données) n'existait pas.
Avant de cocher, aller lire la ligne de code.
