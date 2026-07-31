---
name: content-accepted-answers
description: >-
  Écrit les réponses ACCEPTÉES (`acceptedAnswers`) d'une question de content/ —
  les autres formulations JUSTES qu'un élève peut taper en mode Rappel ou dans
  une question libre `short_answer` : paraphrases, synonymes exacts, positions
  équivalentes, translittérations latines de l'arabe. À utiliser quand on veut
  « accepter les autres formulations », « corriger les faux négatifs du Rappel »,
  « ajouter des réponses acceptées », lancer une campagne acceptedAnswers sur une
  matière, ou traiter un signalement « ma réponse était juste et refusée »
  (étude 20, Tier B). Le skill RE-RÉSOUT chaque question avant d'écrire et
  écarte toute variante qui égale un élément déclaré faux — mieux vaut refuser
  une paraphrase rare qu'accepter une réponse ambiguë. Il écrit des FICHIERS
  uniquement, jamais de SQL ni d'écriture en base. Défère à content-engine pour
  le schéma, la barre de qualité et la validation.
---

# Réponses acceptées — le Tier B (étude 20)

## Le problème, en une phrase

En mode Rappel, l'élève tape sa réponse au lieu de la choisir. Le moteur ne
valide que la **réponse canonique** et les variantes de l'ensemble accepté. Tout
le reste est refusé — y compris ce qui est **juste**.

Le cas fondateur, observé en production le 2026-07-15 sur la mission
« التموقع في الفضاء » : l'énoncé dit *« الطائر يطير فوق الشجرة »*, la réponse
attendue est **« فوقها »**, et l'enfant tape **« فوق الشجرة »**. Il a raison. Il
est marqué faux.

## Ce que ce skill fait — et ne fait pas

**Il fait** : ajouter à une question les formulations **également justes**.

**Il ne fait pas** :

- il n'invente pas de quasi-synonyme qui déplace le sens (« فوق » ≠ « في السماء ») ;
- il ne touche **jamais** à la réponse canonique ni aux distracteurs ;
- il n'écrit **aucun** SQL et ne parle **jamais** à la base ;
- il ne fait pas le Tier A (article défini, contractions) : celui-là est
  **mécanique**, appliqué au build par `withMorphologicalVariants`. En écrire les
  variantes à la main serait du bruit — et un doublon que la QA rejette.

## Les quatre familles à écrire (Tier B)

| famille               | exemple                                        |
| --------------------- | ---------------------------------------------- |
| position équivalente  | « فوقها » → « فوق الشجرة »                     |
| pronom ⇄ nom explicite | « داخل الصندوق » → « داخله »                   |
| synonyme exact        | « الكرز » ⇄ « حبّة الكرز »                     |
| translittération      | « النملة » → « namla » (mono-mot par défaut)   |

**Cible prioritaire** : les réponses **positionnelles** ou de **≥ 2 mots**. Une
réponse d'un seul mot lexical n'a souvent qu'une translittération à gagner.

## La règle qui prime sur toutes les autres — R-4

> Une variante ne doit **jamais** égaler, une fois normalisée, un élément
> **déclaré faux** de la même question : un distracteur, ou une erreur attendue
> (`expectedMistakes`) d'une `short_answer`.

Mieux vaut refuser une paraphrase rare qu'accepter une réponse ambiguë : le jour
où un distracteur devient acceptable, la question ne mesure plus rien.

`content:qa` rejette la collision — mais **ne comptez pas dessus** : vérifiez
avant d'écrire. Le gate est le filet, pas la méthode.

## Procédure

1. **Ne travailler que sur des questions qui CONSOMMENT l'ensemble** — une `mcq`
   éligible au Rappel, ou une `short_answer`. Sur les autres, `content:qa`
   avertit et le scoring ignore. L'éligibilité se calcule, elle ne se devine pas :

   ```bash
   # depuis le moteur, corpus branché
   node --experimental-strip-types -e "
     import('./src/shared/content/free-answer.ts').then(F => { /* isRecallEligible */ })"
   ```

2. **Re-résoudre la question** — à l'aveugle, sans regarder la clé. Si votre
   réponse diffère de la canonique, ce n'est pas une variante à ajouter : c'est
   un défaut de la question, à signaler.

3. **Écrire les variantes**, dans la langue du contenu, en respectant :
   - ≤ 24 entrées (le schéma le borne, mais 2 à 4 suffisent presque toujours) ;
   - jamais la canonique elle-même (elle est acceptée d'office) ;
   - jamais un doublon interne une fois normalisé (la vocalisation, la casse et
     les espaces sont déjà pliés — « تحت الكرسيّ » et « تحت الكرسي » sont **le
     même mot** pour le moteur : en ajouter un est un doublon, pas une variante) ;
   - jamais une variante qui sort du charset tapable `^[a-z0-9.ء-ي]+$`.

4. **Passer les gates**, dans cet ordre :

   ```bash
   npm run content:check && npm run content:qa:strict
   ```

5. **Relire le diff** avant de compiler. Aucune mise en base d'un ensemble non
   relu (R-7) : la génération est hors-ligne, jamais au runtime.

## Translittérations arabes

Arbitrage Q-1 : **tous les niveaux**, pas seulement les petites classes — un
élève sans clavier arabe existe à tout âge.

- **mono-mot** : par défaut (« النملة » → `namla`, `nemla`) ;
- **multi-mot** : seulement si une **seule** romanisation est raisonnable. Dans
  le doute, s'abstenir : deux graphies concurrentes valent mieux qu'une fausse.

⚠️ La translittération ne remplace pas le clavier d'appoint (étude 20 lot 5) :
elle le complète, pour l'élève qui préfère écrire en lettres latines.

## Ce qui reste à un humain

Le skill propose ; la **revue de diff** valide. Sur du contenu destiné à des
enfants, une variante acceptée à tort est une erreur qu'on apprend — c'est le
sens du stop-point R-7 de l'étude.

Défère à **content-engine** pour le schéma des fichiers, la barre de qualité et
la validation ; à **content-audit** pour la re-résolution en profondeur d'une
matière entière.
