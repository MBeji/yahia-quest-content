# Campagne `fiqh` — « الرسالة » d'Ibn Abî Zayd al-Qayrawânî

Matériel de la campagne qui alimente la sous-rubrique **فقه** de la rubrique **Éducation
islamique** (thème `education-islamique`, parcours libre des extras, **ouvert aux élèves**
depuis le 2026-08-15).

**Le principe** : un **باب du livre = un chapitre de l'app**. Le livre en compte **45**.
`displayOrder` = le numéro du باب, jamais la position dans la matière — les trous sont les
أبواب restant à écrire, et ils se logeront à leur place exacte sans rien renuméroter
(renuméroter re-clèrerait les UUID v5, piège n°2 du pipeline). L'élève ne voit pas ces
numéros : `subject-hub` étiquette les chapitres par leur **rang dans la liste**, donc la
numérotation qu'il lit est continue.

## État au 2026-08-15

**29 chapitres écrits** — 1 à 29, sans trou. Les 26 premiers sont **appliqués en production**.

**16 restants** : 30 → 45.

| Bloc | أبواب | Sujet |
| --- | --- | --- |
| **Sujet adulte** ⚠️ | 30, 32, 33, 35, 37, 39 | الجهاد · النكاح والطلاق · العدّة · العتق · الدماء والحدود · الفرائض |
| Serments | 31 | الأيمان والنذور |
| Transactions | 34, 36 | البيوع · الشفعة والهبة والرهن والعارية واللقطة |
| Justice | 38 | الأقضية والشهادات |
| Récapitulatif | 40 | جمل من الفرائض والسنن الواجبة والرغائب |
| Les آداب | 41 → 45 | اللباس · الطعام · السلام والاستئذان · التعالج والرقى · الرؤيا والسبق |

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
#    ⚠️ Par lots de 4. Au-delà, la limite d'usage de session tue les agents en vol.

# 3. Fidélité au matn — le contrôle qui compte
node FableEtudes/campagnes/fiqh-risala/verify-citations.mjs

# 4. Audit structurel (échelle des missions, fuite par la longueur, doublons, plafond)
node FableEtudes/campagnes/fiqh-risala/audit-fiqh.mjs

# 5. Gates du moteur (depuis la racine du corpus, moteur checkouté à côté)
node --experimental-strip-types <engine>/scripts/content/build.ts --check --content-dir content
node --experimental-strip-types <engine>/scripts/content/qa.ts --strict --subject fiqh
```

## Ce que cette campagne a appris, et qui a coûté cher

**L'audit indépendant n'est pas optionnel.** Sur trois vagues d'audit, les gates étaient
verts à chaque fois et les auditeurs ont quand même trouvé **cinq affirmations fausses** —
dont un chapitre qui enseignait trois fois une règle démentie par sa propre question boss, et
un renvoi de chapitre faux dans la première ligne de contenu du chapitre le plus lu.
**Aucune clé fausse sur 420 questions re-résolues** : le risque n'est pas la clé, c'est la
prose autour.

**Le vrai passif est l'usage des guillemets.** « … » doit désigner le matn et rien d'autre.
Des gloses de l'auteur du cours passaient pour du texte du livre — quatre au seul chapitre 15,
dont deux devenues des clés de question. Un guillemet fermant mal placé au chapitre 01 a
transformé 47 caractères de commentaire en apparente citation.

**Le contrôle de fidélité a eu trois défauts, tous trouvés par d'autres que son auteur** :
seuil de 12 caractères (il laissait passer «أربع فأقلّ», contraction de «أربع ركعات فأقل»),
chapitre au matn manquant **sauté en silence** et compté 0 écart, et périmètre limité au cours
et au résumé alors que **la moitié des emplois fautifs vivent dans les questions**. Les seuils
et le périmètre actuels sont bas et larges à dessein — ne les resserrez pas « par propreté ».

**Écrire de mémoire est le danger n°1, et il est invisible.** Le chapitre 26 (barèmes de la
zakat du bétail) l'a montré : **cette recension donne les âges des chameaux une année
au-dessus** des valeurs les plus répandues. Un agent écrivant ces barèmes de tête — le
réflexe naturel, ils sont archi-connus — aurait produit un chapitre faux et parfaitement
crédible. Même piège désamorcé au chapitre 28, où `طواف القدوم` et `أيام التشريق` ont été
écartés parce qu'absents du matn.

**Le matn a ses propres défauts.** La transcription shamela ampute un mot coranique page 63
(`وَضُحَاهَ` au lieu de `وَضُحَاهَا`, vérifié dans leur HTML) et porte six coquilles OCR au باب 11.
Un doute se tranche contre un **commentaire indépendant** qui cite le matn : `الثمر الداني`
([book/7441](https://shamela.ws/book/7441)) a servi deux fois. Les corrections de coquilles se
**déclarent** dans `chapter.json` — sinon un auditeur ultérieur compte des écarts sans savoir
pourquoi.

**Une omission assumée, au chapitre 29.** Le matn dit «الختان سنة في الذكور واجبة **والخفاض
في النساء مكرمة**». Seule la première moitié est enseignée, et la phrase du cours est scopée
« sur les garçons » pour ne rien affirmer de faux. L'excision est interdite en Tunisie et
reconnue comme une mutilation : elle n'a pas sa place dans un contenu destiné à des enfants.
C'est la seule exception à la règle de fidélité, et elle est délibérée.

## La source

[shamela.ws/book/11373](https://shamela.ws/book/11373) — texte du Xᵉ siècle (l'auteur meurt
en 386 h.), domaine public. L'extraction ne prend que le matn, jamais l'appareil éditorial,
et **ne se versionne pas** : `risala/` est gitignoré, il se reproduit par le script.
