# S4 — Stratégie d'acquisition et plan d'action Facebook / Instagram (14 novembre 2026)

> Suite du [chantier 05](../../../05-plan-marketing-commercial.md). Les livrables S1 à S3 et le
> kit de démarrage de la Page datent de juin 2026 ; ce dossier les met à jour avec ce qui a été
> **constaté** le 14 novembre 2026 : l'usage réel dans la base de production, le trafic lu dans
> Google Analytics et Search Console, l'état de la Page et d'Instagram, le calendrier scolaire
> 2026-2027 et la concurrence.
>
> C'est la **copie versionnée** d'un document de travail tenu hors dépôt et qui continue
> d'évoluer. Elle fige l'état du 14 novembre 2026.

## Ce que contient le dossier

| Fichier                                                                | Contenu                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`01-strategie.md`](./01-strategie.md)                                 | La stratégie : diagnostic, marché et calendrier, cibles, positionnement et messages, offre d'appel, canaux, ligne éditoriale, groupes, partenariats, mesure, garde-fous, plan 90 jours, budget, accès. En fin de fichier, l'annexe D : le relevé Google Analytics, Search Console, Page Facebook et Instagram |
| [`02-calendrier-editorial.md`](./02-calendrier-editorial.md)           | Les seize publications du 16 novembre au 13 décembre 2026, rédigées, avec leur visuel et leur lien tracé                                                                                                                                                                                                      |
| [`03-kit-groupes-partenariats.pdf`](./03-kit-groupes-partenariats.pdf) | Les messages prêts pour les administrateurs de groupes, les enseignants et les médias, et dix réponses types                                                                                                                                                                                                  |
| [`04-sources-et-reperes.pdf`](./04-sources-et-reperes.pdf)             | Les pages Facebook relevées, le vocabulaire des parents, le calendrier scolaire détaillé, les sources                                                                                                                                                                                                         |
| [`05-mise-en-route.pdf`](./05-mise-en-route.pdf)                       | La consigne de mise en route : régler la Page et Instagram, répondre aux commentaires en attente, programmer la première semaine                                                                                                                                                                              |
| [`figures/`](./figures/)                                               | Les quatre figures de la stratégie                                                                                                                                                                                                                                                                            |
| [`visuels/`](./visuels/)                                               | Les dix-huit visuels prêts à publier : 1080 × 1350, et une story 1080 × 1920                                                                                                                                                                                                                                  |
| [`outil/visuels.js`](./outil/visuels.js)                               | Le gabarit qui a produit les visuels                                                                                                                                                                                                                                                                          |

## Ce qui change par rapport au plan de juin

- **Un appel à l'action unique : le test de niveau** (étude 39), qui n'existait pas en juin.
  En 28 jours, 570 sessions sont arrivées sur la page d'accueil et 9 sur le test.
- **Des données réelles.** Environ 850 visiteurs sur 28 jours, la moitié par Facebook ; jamais
  plus de 6 comptes actifs la même semaine depuis juin ; une seule page indexée par Google au
  14 novembre.
- **Le gratuit ne distingue plus.** Deux offres gratuites occupent le terrain : la plateforme
  de soutien du ministère et un site centré sur la 6ᵉ et la 9ᵉ. Le message devient « ici on
  s'entraîne », la position D5 du chantier.
- **Le départ est daté** : le 23 novembre 2026, premier jour des examens du premier trimestre.
- **D1, constat du 14 novembre** : la Page existe (155 abonnés), le compte Instagram aussi
  (12 abonnés, à l'arrêt depuis le 22 août). WhatsApp Business n'a pas été vérifié. Restent
  le second administrateur et la présentation de la Page.

## Ce qui ne change pas

- Dans les groupes de parents : la valeur d'abord, pas de spam, une présence utile dans
  quelques groupes choisis. C'était la règle d'or de S2 ; elle est reprise telle quelle, avec
  ses raisons (règles de Meta, profil unique administrateur de la Page).
- La position de référence (D5) et la soutenabilité par l'établissement (D6), toujours sous
  la précondition de la déclaration INPDP.

## À savoir avant de s'en servir

- Les textes arabes sont à relire par le propriétaire avant toute publication.
- Les objectifs chiffrés sont des hypothèses de travail, à recaler après deux semaines de
  données.
- La partie sur la loi n° 2004-63 n'est pas un avis juridique.
- Les fichiers 03 à 05 sont en PDF : leur texte modifiable est dans le document de travail.
- Dans l'annexe D, la liste des groupes déjà rejoints ne garde que les groupes scolaires.

## Refaire ou ajouter un visuel

```bash
# depuis ce dossier, avec le dépôt du moteur cloné à côté
node outil/visuels.js ../../../../../../yahia-quest-arena/public/fonts ./visuels
```

Le gabarit lit les polices de la marque dans `public/fonts` du moteur et demande Playwright.
Un visuel de plus est une entrée de plus dans son tableau `cards`.
