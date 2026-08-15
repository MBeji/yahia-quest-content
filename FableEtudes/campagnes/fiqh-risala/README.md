# Campagne `fiqh` — « الرسالة » d'Ibn Abî Zayd al-Qayrawânî

Matériel de la campagne qui alimente la sous-rubrique **فقه** de la rubrique
**Éducation islamique** (thème `education-islamique`, parcours libre des extras).

**Le principe** : un **باب du livre = un chapitre de l'app**. Le livre en compte **45**.
`displayOrder` = le numéro du باب, jamais la position dans le dossier — les trous sont les
أبواب restant à écrire, et ils se logeront à leur place exacte sans rien renuméroter
(renuméroter re-clèrerait les UUID v5 = suppression + recréation, cf. piège n°2 du pipeline).

## État au 2026-08-15

**12 chapitres livrés** (PR #172) : 1, 2, 3, 4, 5, 6, 7, 9, 14, 15, 16, 17 —
360 questions de missions + 60 de quiz.

**33 restants** : 8, 10, 11, 12, 13, puis 18 → 45.

| Bloc | أبواب | Sujet |
| --- | --- | --- |
| صلاة (reste) | 8, 10, 11, 12, 13, 18, 19 | الأوقات · صفة الصلاة · الإمامة · باب جامع · سجود القرآن · الخسوف · الاستسقاء |
| الجنائز | 20, 21, 22 | المحتضر والغسل · الصلاة على الجنائز · الطفل |
| الصيام | 23, 24 | الصيام · الاعتكاف |
| الزكاة | 25, 26, 27 | زكاة العين والحرث · الماشية · الفطر |
| الحجّ | 28 | الحجّ والعمرة |
| المعاملات & الآداب | 29, 31, 34, 36, 38, 41 → 45 | الذبائح · الأيمان · البيوع · الشفعة والهبة · الأقضية · الآداب |
| **Sujet adulte** ⚠️ | 30, 32, 33, 35, 37, 39 | الجهاد · النكاح والطلاق · العدّة · العتق · الدماء والحدود · الفرائض |

Les six أبواب marqués **sujet adulte** se traitent sobrement et au passé historique :
principes et vocabulaire juridique, **aucun détail procédural** sur les peines, aucun détail
intime, les institutions historiques (statut servile, capture) présentées dans leur contexte
et jamais comme un modèle. C'est la consigne §3 du [`BRIEF.md`](./BRIEF.md), arbitrée par
Mohamed le 2026-08-14 (avec « les 45 أبواب intégralement » et le registre « tous publics 10+ »).

## Comment reprendre

```bash
# 1. Ré-extraire le matn (202 pages → 45 fichiers par باب + manifest.json)
node FableEtudes/campagnes/fiqh-risala/extract-risala.mjs

# 2. Un agent par chapitre, à qui on donne le BRIEF + son fichier de matn.
#    ⚠️ Par lots de 4 à 6 : au-delà, la limite d'usage de session tue les agents
#    en vol (vécu le 2026-08-14 : 9 agents perdus, dont 5 à mi-chapitre).

# 3. Audit structurel (échelle des missions, fuite par la longueur, doublons,
#    options citées par lettre, plafond de difficulté)
node FableEtudes/campagnes/fiqh-risala/audit-fiqh.mjs

# 4. Gates du moteur (depuis la racine du corpus, moteur checkouté à côté)
node --experimental-strip-types <engine>/scripts/content/build.ts --check --content-dir content
node --experimental-strip-types <engine>/scripts/content/qa.ts --strict --subject fiqh
```

**L'audit indépendant n'est pas optionnel.** Sur les 6 premiers chapitres, les gates étaient
verts et deux auditeurs qui n'avaient rien écrit ont quand même trouvé trois affirmations
fausses et plusieurs débordements du matn. L'auto-relecture de l'auteur ne les avait pas vus.

## Ce qui reste à faire une fois les 45 écrits

Basculer le parcours `education-islamique` de `coming_soon` à `available` par une migration
de l'arena — **après** que `apply-content.yml` ait appliqué le corpus en prod. Tant que la
bascule n'est pas faite, la carte s'affiche dans les extras sans être navigable.

## La source

[shamela.ws/book/11373](https://shamela.ws/book/11373) — texte du Xᵉ siècle (l'auteur meurt
en 386 h.), domaine public. L'extraction ne prend que le matn, jamais l'appareil éditorial.
Un doute sur la fidélité de la transcription se tranche contre un **commentaire indépendant**
qui cite le matn : `الثمر الداني` ([book/7441](https://shamela.ws/book/7441)) a servi une fois,
sur `دم الاستحاضة` — lecture identique, transcription confirmée.
