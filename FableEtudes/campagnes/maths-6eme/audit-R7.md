# Audit R-7 — fiche `programme/6eme-base/maths.md` (6ᵉ × mathématiques)

> Auditeur R-7 indépendant (contexte vierge, opus), 2026-10-19. Protocole : méthode § A5.2 / T-8.
> Vérification **contre les PDF sources** (`502603P00` guide, `102609P00` manuel élève), à l'image
> (`pdftoppm`, 130–220 dpi, recadrages), jamais contre les notes des lecteurs (`lecture/L*.md`).
> Légende : **OK** = conforme ; **FORME** = écart de forme corrigé sans escalade ; **SUBST** =
> erreur substantielle (invention, contresens, omission d'items, donnée fausse), corrigée.

## 1. Partie 100 %

### 1.1 Les 61 titres (§2) et le relevé des pages (§2 ter) — manuel, 61 bandeaux + فهرس ص 174 ; guide p.59

- 61 bandeaux recadrés (130 dpi) sur les pages de début données au §2 ter : **les 61 numéros tombent
  exactement sur la page annoncée** (4, 8, 10, 14, 16, 19, 21, 24, 27, 31, 33, 34, 35, 38, 42, 46, 47,
  50, 55, 59, 63, 65, 66, 67, 70, 74, 78, 80, 85, 89, 90, 93, 98, 102, 104, 106, 107, 111, 115, 117,
  122, 126, 129, 131, 132, 133, 136, 139, 140, 142, 147, 151, 153, 157, 161, 162, 163, 165, 169, 171,
  173) → §2 ter **OK** (bornes hautes = page suivante − 1 ; ص 174 = فهرس).
- فهرس ص 174 (220 dpi, pivoté) et خارطة الكتاب p.59 du guide (200 dpi) relus.
- Recoupement titre par titre (bandeaux ↔ §2) : **59 conformes**, 2 écarts de forme :
  - **L7** — **FORME** : le §2 donne « 90−45−60−30−15−120 » (texte de p.59 et du فهرس) sans dire
    que le bandeau ص 21 imprime « 120 - 90 - 60 - 30 - 15 », **sans 45** (le §2 septies le disait,
    pas le §2 ni le thème « الزوايا » qui citait un ordre réarrangé entre guillemets). Annoté aux deux
    endroits.
  - **L38** — **FORME** : le §2 portait « (متوازي الأضلاع، المعيّن، المستطيل، المربّع) » (ordre de
    p.59) alors que sa propre table de corrections annonce l'ordre du bandeau ; le bandeau ص 111
    imprime « (متوازي الأضلاع، المستطيل، المعيّن المربّع) ». Corrigé.
  - Vérifié en passant : L15 parenthèse (bandeau) ✓ ; L40 sans « مجموعة » au bandeau, avec au فهرس
    et à p.59 ✓ ; L58 « الجمليّة » d'abord au bandeau, « الجانبيّة » d'abord au فهرس et à p.59 ✓ ;
    L11 « وأقيّمها » au bandeau, tronqué à p.59 ✓ ; L31 « الكسريّة والعشريّة » à p.59 (avec و),
    « الكسريّة العشريّة » au bandeau ✓ (le contresens relevé au §2 ter est réel).

### 1.2 Chapitrage §4 et `manifest/6eme-base.json` (sujet `math-6eme`)

- 24 slugs, ordre = displayOrder des `chapter.json` (1→24, `24-decomposition-fractions` en 9ᵉ) ✓ ;
  les plages `manuel.pages` du manifeste = celles du §4 et = bornes des leçons du §2 ter
  (bandeaux vérifiés ci-dessus) ✓ ; code `102609` ✓. **OK, aucune correction.**

### 1.3 Errata officiels (guide p.200–204) contre la table §6.1

- p.200 (entrées 1–23), p.201 (24–42), p.202 (43–60), p.203 (61–66), p.204 (figure de
  remplacement, « بصفحة 121 تمرين عدد 2 مذكّرة عدد 55 ») lus à 170 dpi, n° 16 zoomé à 400 dpi :
  **66 entrées** ✓, colonnes leçon / ex. / ص / ligne / خطأ / صواب conformes, sauf :
  - **n° 16 — FORME** : le sommet est **ت** (« ق ن ت̂ = 45° » → « ف ن ت̂ = 45° »), la fiche écrivait
    ك (table §6.1 et note de la leçon 17 au §2 septies). Corrigé aux deux endroits.
  - **§6.4 — FORME** : « étiquettes 350–750 à supprimer (erratum n° 43) » → c'est le **n° 44**.
    Corrigé.

### 1.4 Épreuves trimestrielles, barèmes et corrigés (guide p.169–199, 31 pages, 150 dpi ; p.180 zoomée à 300 dpi)

- **T1** p.169 (énoncé, brochure 3 offres, 981 د / 19,350 / 342,750 / 6 أقساط / 5,750 / 12 / 1/10) ✓ ;
  p.170 (horaires 8 س 30 / 4 س 45 / 19 / 8 س 30 دق) ✓ ; p.171 (trapèze ج د / ب هـ أ, consignes
  3-1…3-3, barème : مع 1 2·4 / 5 / 7,5 ; مع 2 0,25…1,75 / 2 / 2,25…3 ; مع 4 1,5 / 3 / 4,5) ✓ ;
  p.172 (référentiel, 4 / 12 / 3 occasions, « 6 عتبات ») ✓ ; p.173–176 (corrigés 196,200 · 784,8 ·
  638,25 · 112,125 · 1015,5 · « 891 » · 98,1 · 1079,1 · 81,75 · 8,175 · 230,7 · 294,3 · 63,6 ; 13 س
  15 دق · 3 س 45 دق · 15 س 15 دق ; triangles équilatéraux / شبه منحرف متقايس الضّلعين) ✓ ;
  p.177–178 grilles vierges ✓.
  - **FORME (×3)** : la fiche marquait `[sic]` « imprimé à l'envers » les expressions
    « 196,200 = 5 : 981 », « 638,25 = 342,750 − 981 » et les trois soustractions de 5-1 : elles se
    **lisent de droite à gauche** (convention de tout le guide, que la fiche reconnaît au §6.4) —
    ce ne sont pas des coquilles. Annotations corrigées (et §6.4). Seul « 891 » (pour 981) est une
    coquille réelle ✓.
- **T2** p.179 (35 % / 40 %, axe « عدد التلاميذ » 0–50, barres ≈ 35 et ≈ 40) ✓ ; p.180 (37,5 م, 3/5,
  plans 65/39 (6,5 × 3,9), 5 × 4, 75 × 4,5 aux échelles 1/1000, 1/750, 1/500 ; 35 د, 6 %, 2 %) ✓ ;
  p.181 (parallélogramme, ب ج ك / ك ج ع / أ ك ع د, أب = 6 صم, ب ج = 3 صم, 60° ; barème complet) ✓ ;
  p.182 ✓ ; p.183 (25 %, 21 / 24 / 15 mm) ✓ ; p.184–185 (6500 صم = 65 م, 3750 صم = 37,5 م, 3,75 /
  5 / 7,5, 22,5, 843,75, 29531,25) ✓ ; p.186 (1771,875 · 590,625 · 31893,75 ; أ ك ج د) ✓ ; p.187–188 ✓.
  - **FORME** : numéros des consignes de la situation 2 transcrits « 2-1 / 2-2 / 2-3 » alors que
    p.180 imprime « 1-2 / 2-2 / 3-2 » (même convention que le T1 : question puis situation) ; d'où un
    faux `[sic]` « numérotation inversée » (énoncé « 2-3 » vs corrigé « 3-2 ») — **p.180 imprime
    elle aussi 3-2**. Corrigé (énoncé, corrigé, §6.4).
- **T3** p.189 (2/7, 1/3, 125 م² ; terrains 36,75 / 5/3 / 40 et 44 / 5/8 ; offres 31,5 · 29,750 · 35,5 ·
  34 et 36,250 · 34,750 · 36,7) ✓ ; p.190 (1500 د, 5/7 ; رقع 45° / 5 صم et 6, 4, 3) ✓ ; p.191 (barème :
  مع 1 1,5·3 / 4 / 5,5 ; مع 2 0,5…3 / 3,5 / 4…5,5 ; مع 4 0,5·1,5 / 2,5 / 4 ; مع 5 0…5) ✓ ; p.192
  (référentiel ; مع 3 et مع 5 grisés ; « 4 مراحل ») ✓ ; p.193–194 (6/21, 7/21, 8/21, 750, 875, 1000,
  2625) ✓ ; p.195–196 (61,25 · 1960 · 69580 · 27,5 · 1210 · 44407 · 68080 · « 60808 » · 27232 · 95312)
  ✓ ; p.196–197 (losange 5 cm / 45°, triangle 3-4-6, 3 cas de parallélogramme, notes de marge) ✓ ;
  p.198–199 ✓.
  - **FORME** : mêmes faux `[sic]` d'ordre (« 1500 − 69580 », « 7 × (5 : 68080) »,
    « 68080 − 95312 ») — lecture de droite à gauche. Corrigé ; « 60808 » reste une coquille réelle ✓.
- p.153 (D1, table « تطوّر معايير التقييم عبر الثلاثيّات », paysage) relue : 5 critères × 3 trimestres ✓,
  inversion des intitulés 3/4 au T1 ✓ (fidèle à l'imprimé).

## 2. Manuel élève — lot L1 (§2 octies), pages lues ce jour par les lecteurs

Lus à 110 dpi (zooms 250–400 dpi) : ص 1, 3, 19, 20, 31, 32, 33, 34, 46, 63, 64, 65, 66, 67, 68, 69, 78, 79, 89.

| ص | verdict | détail |
| --- | --- | --- |
| 1 | OK | auteurs البرثاوي, محمّد علي الوسلاتي ✓ |
| 3 | OK | 5 rubriques et définitions ✓ (« آستكشاف » ✓) |
| 19 | OK | tableaux miel (107/143/133 ; 6,25/4,75/5,5 ; 13,250/15,250/17,800 ; 0,190 ; 31338,530) ✓ |
| 20 | OK | tableau des 8 pays, cases vides et valeurs ✓ ; 17/100 ; 201557,449 ✓ |
| 31 | OK | tableau du projet agricole ✓ |
| 32 | OK | 28,5 kg · 20 kg · 36 € · 1537,2 · 1,560 · 94496,4 ; malade (2,5 صل, 20 صل, 66, 88 دسغ, 5,5) ✓ |
| 33 | FORME | titre de section « le train **Nabeul**/banlieue » : la page dit « مدينة النّورس », pas Nabeul — titre corrigé. Données (120, 0,900, 0,650, 6 h, 30 دق, 6 h 36, 0 h 36 ; 5 صم, 45°, ½ ج د ; « عيد ») ✓ ; erratum n° 6 : forme corrigée imprimée ✓ |
| 34 | OK | énoncé ✓ ; horloges zoomées 400 dpi : aiguille des heures juste à gauche de 12 (réelle), juste à droite au miroir — compatible avec la lecture `[?]` 11 h / 1 h |
| 46 | OK | 1/800, 20,5 × 16, « 5240 < مضاعف لـ 41 < 5250 », 4,5 ; 4,8 × 5, 1/200, 2 549760, « متساوية » imprimé (erratum n° 13 déjà corrigé) ; 101,834 · 48,621 · 4,645 · 0,396 ; 415,300 ✓ |
| 63 | FORME (`[?]` levé) | ligne (3) : « شعاع » **vide sans pointillés**, « محيط » en pointillés — le `[?]` est levé ; erratum n° 23 imprimé corrigé ✓ ; 371/389, 340/350, 260, 26,568 ✓ |
| 64 | OK | parcelles 1/400 (22/18/20 ; 5,5/4,5 ; 24/16 ; 10/5 ; 24 ; 400/396/192 imprimés — erratum n° 24 déjà corrigé) ; 128 د ; 25 % ✓ |
| 65 | OK | élections (27 pages, 7, 20) ; gâteau (20 cm, 40 g, 60 g, 200 مل, 1,030, 3 cm, 5,41/5,42) ✓ |
| 66 | OK | « 8 . + 8 × . 8 = 8 . 8 », 2004 / 18, 35 têtes / 116 pattes ✓ |
| 67 | OK | 1/750, 8 صم, 4,8 صم, marques d'égalité du losange, demi-disque ✓ |
| 68 | OK | ex. 3–7 (2 / 2,5 ; 110 / 90 ; 120 / 60 ; 3 / 0,9 ; 3 صم + clés) ✓ |
| 69 | **SUBST** | ex. 8 (circuit cycliste) : la figure (relue à 250 dpi) a un **côté bas continu de 120 + 84 = 204 m** jusqu'au bord droit du petit carré 84 × 84 ; le « déduit » de la fiche ne comptait que 120 m ⇒ tour **968,28 m / 24207 m** faux → **1052,28 m / 26307 m** (l'heure d'arrivée 11 h 18 min 20 s est juste). Corrigé. Ex. 9 (25 م², 5 دسم, 17 côtés ⇒ 170 plants) ✓ |
| 78 | OK | place 12 × 8 cm, 1/500, cercles r = 1, 0,5 / 1,5 / 2,9 / 2 / 4, « 1357 » imprimé (incohérence 744,5 ≠ 1357 réelle, bien signalée) ✓ |
| 79 | OK | tableau س 1 → س 6 (48 · 60 · 90 · 87 · 102 ; 8 / 12 / 14 / 11 / 12 ; 37–41 ; 50–55), 1/3 ✓ |
| 89 | OK | 2005, 11 ل, **1/5** imprimé (erratum n° 34 déjà corrigé ✓), 0,520, 1,030, 1/8, 4,800 ; 1344 ل, 32 ل / 3 دق, 64 ل / 5 دق, 24 ل ✓ |

## 3. Manuel élève — lot L2 (§2 nonies), pages lues ce jour par les lecteurs

Lus à 110 dpi (zooms 300–400 dpi pour les diagrammes et figures) : ص 102, 103, 104, 105, 106, 117, 118, 119,
120, 121, 129, 130, 131, 132, 139, 140, 141, 151, 152, 161, 162, 169, 170, 171, 172, 173 (+ فهرس ص 174, §1.1).

| ص | verdict | détail |
| --- | --- | --- |
| 102 | **SUBST** | diagramme des étudiants (zoom 300 dpi) : sur la graduation régulière (ligne forte tous les 100), les bâtons valent **rouge 900 / 750 / 600 / 500 ; bleu 650 / 500 / 450 / 300**. La fiche lisait rouge 900/**650**/600/500 et bleu **550**/500/**350**/300 — le lecteur a lu trois bâtons sur les **étiquettes parasites** que l'erratum n° 44 fait supprimer (« 650 » est posée à hauteur 750, « 550 » à 650, « 350 » à 450). Totaux 2650/1700 → **2750/1900** ; taux de l'année précédente 61,11/76,92/58,33/60 → **72,22/66,67/75/60**. Corrigé (§2 nonies et §6.4). Énoncés, tableau 80/80/85/90 %, 45 % / 23 %, 9 × 8,1 cm, 1/1000, 210 m, 15 m, 9000 د, 4 % ✓ |
| 103 | OK | tableau 2004/2005 (950/900/650/650 ; 760/675/533/546) ✓ |
| 104–105 | OK | 12 × 8 cm, 1/500, 7,5 م, 2 م, 56250 ل, 500 ل, 367,75 ; tableaux mobilier (1500/1380 ; 152/1748 ; 1000/50 ; 1680/12/180/140 ; 2128/16/228 ; 10/100/110) ✓ ; « المسألة عدد 2 » déjà corrigé dans ce PDF |
| 106 | OK | quadrillage 5 × 5 (sommet commun en (3 ; 2), bases 0–1 / 4–5) ✓ ; 5 % / 15 % / 6 د ; 29 د / 16 % ; 12 / 7 / 2004 → 2005 ✓ ; « الأحجية » ✓ |
| 117–119 | OK | ex. 1–13 : toutes les séries de fractions, dans l'ordre imprimé ✓ (« أُوجِدُ » déjà corrigé) |
| 120 | OK | 7/3 دسل, 3 دسل, 7,800, 2,250, 25 % ; diagramme des âges (zoom 300 dpi) : 9 / 13 / 5 / 3 ✓ |
| 121 | OK | 1/9 ; 1/2, 4/21, 1/6, 1/7 ; 16 د ✓ |
| 129 | OK | 3,5 / 2 / 1,5 د ; 1/3, 1/2 ; 94,500 ; 2/5 ; 21,924 ; 1,924 ✓ |
| 130 | OK | 1/500, 28,6 / 30,2 / 14,4 cm ; و/هـ et س/كـ (zoom 400 dpi : و et س à gauche, هـ et كـ à droite) ✓ ; 25 % = 8 ق ; phrase inachevée « أثبت أنّ عرض المسلك الغابيّ المقتطع من الأرض. » ✓ |
| 131 | OK | 36 م, 21 م, 5/4, 4/5, 50 د ; points هـ (2ᵉ graduation sur 4) et كـ (3ᵉ sur 5) ✓ ; 2/3, 1/2, 25 د, 15 د, 43,5 م ✓ |
| 132 | OK | 34, 2, 7 ; ordre des points ص د أ س / ن ب ج ع ✓ ; 24, 8 ; « م قاله » ✓ ; 126 د, 7 ✓ |
| 139 | OK | 1/2, 1/4, 1/6, « المساحة المتبقّية » sans 0,18 (erratum n° 58 : fautif dans ce PDF, ✓) ; 2,6/7,8/5,2 ; 1/4, 2/5, 1/8, 202,500, 218700 ✓ |
| 140–141 | OK | 100 / 50 / 100 م, 58 آر, 45 د, 3/5, 8 % ; tissu 20/40/10 cm, 10 صم² / 4 ساعات ✓ |
| 151–152 | OK | 3/2, 4 م, 9515, 27,5, 2/3, 40 د ; 127/95/105 كم, 2 س 7 دق…, 84 كم/س, 10 ل/100 كم, 0,580, 1 س 20 دق, 25,056 ✓ |
| 161 | OK | 6 س 55, 5 ل/100 كم, 30 ل, 1 س 15, 20 ل, 80 كم/س, 16 ل, 680 كم, 4 س 40 ; plaque 120 × 80, 30/10/40/20/30 cm, 4 م, 2/3, 96 د, 15,91, 70 %, 336 ✓ (figure fautive, remplacée p.204 ✓) |
| 162 | OK | 1/1000, 3,5 / 13,2 / 2/3 / 9,6, 18/37 ; « أ د هـ ك » déjà corrigé ; 39600 ل, 3/4, 1/2, 36 ل/دق, 10 دق, 7 س 45, 108 ل/دق ✓ |
| 169–170 | OK | tableau peinture (4/3,5/3 ; 6/4/3 ; 4,5/4/3 ; 3,4/4,6/3,2), 0,3 كغ, 20 كغ, 32 د, 3 أيّام, 18 د ; 4 مشرفين, 2/7, 4/9, 161, 35, 765, 20 %, 5, 555 ✓ |
| 171 | FORME (`[?]` levé) | champ (100/157/300/140/20/100 م), 30 ق/هـآ, 60 كغ, 1/31, 50, 15/24 كم/س, 227304/227556, 9,3 ✓ ; renvoi imprimé « صفحة 31 على كرّاس الرّياضيات » : la lecture de L2 est juste, le `[?]` de l'erratum n° 65 est levé (ce PDF ne porte ni « صفحة 28 » ni la forme corrigée) ; table §6.1 et note mises à jour |
| 172 | OK | 384 د, 5 أقساط, 1920 د ; 65/40/20 صم, 35 صم ✓ |
| 173 | OK | tunnels (zoom 300 dpi : avant col. 2 rang 2 ; droite prof. 2 rang 2 ; dessus col. 3 rang 3) ✓ ; 5 × 5 × 5 ; escalier ; 5 patrons أ → هـ ✓ ; « أركانا » fautif ✓ |

## 4. Guide — les مذكرات (§2 decies, règles institutionnalisées : 100 %)

Lus à 120 dpi : p.106, 108, 109, 110, 117, 118, 120, 121, 122, 123, 128, 131, 132, 133, 137.

| p. | verdict | détail |
| --- | --- | --- |
| 106 | OK | فهرس des 5 مذكرات (8, 18, 32, 46, 48) ✓ |
| 108 | OK | en-tête مذكرة 8 (إنماء, 180 دق, المعينات) ; أستحضر 1 / أستكشف 2 ✓ |
| 109–110 | OK | 1ʳᵉ méthode (« يرسم الأوّل بالمسطرة ثمّ … البركار ») p.109 ; 2ᵉ, 3ᵉ, ملاحظة 1 et 2 p.110 — verbatim ✓ ; bloc أتدرّب ✓ |
| 117 | OK | **encadré** « كلّ خارج صحيح لعمليّة قسمة … ومقامه هو القاسم في عمليّة القسمة » verbatim ✓ ; 11/5 = 22/10 = 2,2 ; 11/5, 22/7, 18/4, 5/7, 28/9 ; « لامارتيناز » ✓ |
| 118 | OK | 19/3, 3/11, 22/3, 4/3 ✓ |
| 120 | FORME | somme des familles : faux `[sic]` — l'imprimé est **une** somme sur trois lignes de cellule (« 50 + 300 + 200 + / 50 + 100 + 600 = / 1300 عائلة »), juste. Note corrigée |
| 121 | OK | التقييم, « اعتماد البيداغوجيا الفارقيّة », encadré final verbatim ✓ |
| 122 | OK | en-tête مذكرة 32 (pas de التّوقيت ✓) ; « توظيف التّناسب في حساب الرّابع التّناسبي » ✓ |
| 123 | OK | **définition** « نسمّي النسبة الّتي مقامها 100 بالنّسبة المائويّة » verbatim ✓ |
| 128 | OK | en-tête مذكرة 46, الهدف المميّز « … شكل مركّب … : قيس مساحة القرص الدائري », 180 دق ✓ |
| 131 | FORME | résultats escomptés « … = 3,12 », « < من قيس مساحة المربّعات الأربعة … », « 3,12 قريب جدّا من العدد π… » verbatim ✓ ; formule non imprimée ✓. Le bloc التدرّب n'est **pas** coupé (fin « كل حسب حاجته. ») : `[?]` levé (§2 decies et §6.4) |
| 132–133 | OK | table des هدف 3 → 10 ✓ (« … والعكس », « … مساحة الإكليل المحيط به ») — fonde la borne ✅ couronne (§3.2) ✓ |
| 137 | OK | arbre de solutions (2 méthodes) ✓ |

## 5. Échantillon hors critique — passes 2026-09 (§2 quater → §2 septies), révisions, théorie maître

| page(s) | verdict | détail |
| --- | --- | --- |
| ص 4–5 (L1) | OK | concours de promotion (18,5/19,75/29 ; 17/19,25/59,25 ; 19/19,25/24 ; 18,25/27/65), 100,5 − 8,96 (91,66 / 10,9 / 91,54), 93,78 + 18,9, € → د (4,680 / 6,240) ✓ |
| ص 8, 136, 163 (L2, L47, L57) | FORME | la rubrique imprimée est **« أتعهّد مكتسباتي »** (logo violet) ; la fiche écrivait « أعتمد مكتسباتي » à 8 endroits (L3, L5, L2, L57, §1) — corrigé partout, avec une note au §1 |
| ص 10–11 (L3) | OK | 17,75 × 14,5 ; 407/22 ; 90,5/20,5 ; **540** (erratum n° 1 corrigé ✓) ; produits et quotients posés (86,45 : 18,2 ; 15 : 0,1 ; 107 : 0,01 …) ; 44 × 36 = 1584 ; milles (4,5 / 10,186 / 10,649 / 3,25 / 18,52) ✓ |
| ص 16 (L5, haut) | OK | 6 h 45 → 9 h 30 ; 12 h 30 → 17 ✓ |
| ص 21–23 (L7) | FORME (errata) | bandeau sans 45 ✓ ; ex. 1–11 ✓ (50°/80°, 8 → 12 couleurs, 45°, 120°, 150 غراد, 150°, 75°, pendentif, mât 30°/45°, 100 غراد) ; état des errata : n° 3 (« بالنّسبة إلى القطعة ») et n° 5 (« إلى الفترة ») **corrigés** dans ce PDF ; n° 4 (fusion 9-أ/9-ب) **fautif** (un seul « 9) -أ ») — table §6.1 mise à jour |
| ص 35–37 (L13) | FORME (errata) | 7 × < 50, {14 … 56}, 400–430, 6/12/30, 15/20/25 ; tableau d'أمل (12 absent) ; 4, 6, 8 < 130 ; paires 3-5, 8-12, 5-20, 150-200 ; 300–400 ; 144 / 288 ; 7, 12, 42 < 200 ; 5/8, reste 3, 70–90 ; 3/4 h – 5/6 h, 4 et 6 دق ; bus 40/30 دق, 4 h ✓. Errata : n° 7 **fautif**, n° 8 **corrigé** (colonne 30/25 imprimée), n° 10 ni l'un ni l'autre (« يمكن عدّ خرفان قطيع ») — table §6.1 |
| ص 39–40 (L14) | OK | tableaux d'échelle (80/4/20 ; 1,50/15 ; 150/3 ; 35/7 ; 1/200 8 ; 1/10000 400 ; 1/1000 18 ; 2 صم / 50 دكم), 40 كم ↔ 4 صم, 25 × 20 au 1/500, 7 صم au 1/200 000, trapèze 30/24/22 au 1/400, mur 21 م / 15 صم / 2,80, 60 × 40 et 30 × 21 ✓ |
| ص 42, 48–49 (L15, L17) | OK | « بالغراد 50 » (erratum n° 12 ✓) ; 7 figures ; losange 3 et 5 ; 30° / 6 صم ; 120° / 4 / 6 ; carré ع و ف ط ; 4 / 6 ; 16 / 3 ; « أ س ب ج » (n° 15 fautif ✓) ; 75° / 3 ; ف ن ت = 45°, 4, 6 (n° 16–17 corrigés ✓) ; 40/30, 60°, 1/1000, 5 صم ✓ |
| ص 70–71 (L25) | FORME (errata) | toutes les listes et le jeu des pancartes ✓ ; « قسمته على 5 » imprimé : n° 25–26 **corrigés** — table §6.1 |
| ص 107–110 (L37) | FORME (errata) | 31/25 … 5/13 ; 360, 30/25/10/35 %, 18/54/72/216 ; 2 % de 2400 …; 15/24/72/7,500 et 30/25/20/50 % ; soldes ; 432/504/484/545 ; 800/1100/?/175 ; facture 145,800 / 32,400 / 324,000 / 72,900 / 19,440 / **184,680** (n° 48 corrigé ✓) ; 60 م, 90 د, 15 %, 2/3, 275 د, 29700 ; 50 %, 36 ألف, 70 %/25 %, 192 د, 15 ans ✓. Errata n° 47, 49, 50 **corrigés** dans ce PDF — table §6.1 |
| ص 113, 124 (L38, L41) | OK | 50/30 م, 28 د ; 25/24 ; tableau 50/20, 120/70, 2400/80/50 (**2400**, Q-E1 ✓) ; 1/20 ; tableau du trapèze ; 997,35 / 21,8 ; 210/175/85, 8 %, 13800, 23, 10 د, 654,50 (n° 57 corrigé ✓) |
| ص 135 (L46) | OK | 7,5 / 47,1 ; 6,4 ; porte 2,4 × 2,4, 65 د ; couronne 314 / 5024 ; 15 صم, 4/5, 12 secteurs ✓ |
| ص 142–146 (L50) | FORME | tableau 25/16, 14, 40/13/9,5 ; 180 د ; 67,5 × 95,5 ; parcelle 1 (90/20/40/30) ; stade 110 × 75 ; ex. 4 : les seules cotes imprimées sont 50 م, 40 م et 20 م — « cercle de diamètre 30 » n'est pas imprimé (note ajoutée ; l'exercice était déjà « non repris ») ; hexagone 10/24 ; 1,5 / 6 ; flèche 50/40 ; salle 100 × 48, 52, 12, 24, 0,27 م², 10 %, 2340 ; toit 5/6/10, 95 د, 1425 د (n° 59 corrigé ✓) |
| p.42–43 | **FORME** (verbatim) | remarque 5 : l'imprimé est « **المقام المشترك الأصغر** … » ; la fiche omettait « المشترك » et y collait un faux `[sic]`. Corrigé. Le reste de p.42–43 (règle du produit en croix, 9 remarques, 4 figures 3/4, 6/8, 9/12, 18/24) verbatim ✓ |
| p.44–51 | FORME | résumées aux thèmes du §2 (non transcrites) : contenu conforme (𝔻, structure de corps, échelle 1/1000000 et exemple 800 هم / 200 هم, pourcentage) ; « 5/4 + 2/3 = 23/12 » est p.**45**, non p.46 (corrigé dans l'en-tête) ; p.51 imprime « ثلاّجة … 340 » pour 840 (coquille non relevée, ajoutée au §6.4) |
| p.52–55 | OK | 840/84, 10 %, deux méthodes ; solides : définitions, 12 أحرف, 8 رؤوس, encadrés « المساحة الجانبيّة = محيط القاعدة × الارتفاع », « المساحة الجمليّة = المساحة الجانبيّة + مساحة القاعدة × 2 », cube × 4 / × 6 ✓ |
| p.60, 64 | OK | 28 nombres de la table p.60 ✓ ; 160 س = 60 + 50 + 50, 43 س / 117 س ✓ |
| p.86–87 | FORME (`[?]` levé) | toutes les divisions sont imprimées de droite à gauche (« 3 : 12,9 », « 0,25 : 16,40 ») — le `[?]` « ordre bidi à confirmer » est levé (§2 undecies et §6.4) ; 31,5/7 … 15,2/3,8 ; fractions/décimaux ; 87,5/7 ; 60,75/2,25 ; 4 × 3,5 / 0,25 ✓ |
| p.93 | OK | révision 7 : 6 صم, 120°, « أبحث عن بأهـ حسابيّا », 5,5 / 60°, 3-5-8 « ما الشّرط … », 18, 6 دسم — fonde Q-3 et la borne « inégalité triangulaire » ✓ |
| p.99–100 | OK | 9 ل/دق, 900/60, 2700/120 ; table blé/couscous ; 1,7 كغ ; confiture ; 420 مي / 4, 18,900 د, 30 يوما ✓ |
| p.141, 150 | OK | حلول أتسلّى 12 (الخامسة / الحادية عشرة ; السّابعة / الواحدة ; السّادسة / منتصف النهار ; الرّابعة / الثّانية) et 61 (16, 64, 11, 53 ; 125, 39 + 24 = 63, 62 ; 0+1+3+6 = 10 ; « الحالة عدد 5 ») ✓ |
| p.157, 163, 165 | OK | test d'orientation : 45,5/26/42,25/28 ; 59,2/44,4/54,76/48 ; 60,3 ; critères (1, 2, 2) ✓ ; corrigé 1183, 2628,48, 104,7 ; 705,6 / 7056 / 70560 m², 7,0560 آر / 70,56 آر / 7,0560 هـآ ; tolérances ± 2 مم / ± 2° ; « هام جدّا » 60 دق + 60 دق ✓ |

## 6. Bilan

- **Pages vérifiées : 158 pages lues en entier** — partie 100 % : guide p.59, 153, 169–204 (38 p.) +
  les 61 bandeaux de titre du manuel et son فهرس ص 174 ; échantillon : **79 pages du manuel** (dont
  la totalité des lots L1 et L2 transcrits ce jour : ص 1, 3, 19–20, 31–34, 46, 63–69, 78–79, 89,
  102–106, 117–121, 129–132, 139–141, 151–152, 161–162, 169–174) et **41 pages du guide** hors
  critique (p.42–55, 60, 64, 86–87, 93, 99–100, 106–110, 117–123, 128, 131–133, 137, 141, 150, 157,
  163, 165), réparties début / milieu / fin des deux sources — soit ≈ 35 % des 344 pages hors
  critique (seuil 15 %, minimum 25 pages).
- **Corrections : 34** — **2 substantielles** (L24 ex. 8 : tour du circuit ; L34 pb 2 : valeurs du
  diagramme lues sur les étiquettes parasites), **32 de forme** (dont 5 `[?]` levés, 12 états
  d'errata établis, 6 faux `[sic]` retirés). Les deux erreurs substantielles portent sur des
  **« déduit »** (valeurs non imprimées) et non sur des données imprimées ; les zones touchées (lots
  L1 et L2) ont été **relues en entier**. Seuil d'escalade (≥ 3) **non atteint**.
- **Aucun classement de scope** (§3.2 ✅/◐/⛔, Q-1…Q-10, Q-E1) n'est modifié : les pages qui les
  fondent et qui ont été ouvertes (p.93, 133, 153–154, 182, 192 ; ص 23, 33, 35–37, 107–110, 135)
  disent ce que la fiche leur fait dire.
- **Chapitrage §4 / manifeste** : conformes, aucune correction.

**Verdict : R-7 2026-10-19, sondage 158 pages, 34 corrections** — fiche fidèle aux sources, à la
barre R-5 : statut `validee-r7`.
