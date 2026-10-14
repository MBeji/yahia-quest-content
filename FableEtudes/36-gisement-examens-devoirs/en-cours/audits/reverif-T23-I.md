# Re-vérification ciblée — tranche T23-I (maths 9ᵉ, ch. 09, missions 42 → 46)

Auditeur : celui de `audit-T23-I.md`. Périmètre : `/home/user/wt-m22/content/math/09-triangle-rectangle-trigo/exercices/42…46-devoir-*.json`
(fichiers du 12/10 19:08, inchangés depuis). Référence publiée : `origin/main` `cb46c2a8` (09/47–51 et ch. 04 devoirs compris).
Moteur de rendu : `/home/user/eng-m22`. Aucun fichier audité modifié, aucune écriture git.

## 1. Application du § 7, mot pour mot

Comparaison champ par champ (script) des cinq fichiers avec les copies vérifiées de l'audit :
- **22 blocs appliqués à l'identique** (énoncés, options, `id`, étiquettes, explications, SVG43, SVG44 retouchés, SVG46, titre de 45).
- Écarts, tous déclarés :
  1. 44 `title` = « ⚔️ زعيم الفرض ⭐⭐⭐: مربّعات الأضلاع ثمّ مركز ثقل ومساحة » (variante m7) — conforme, aucun résultat livré.
  2. 46 Q5 : SVG46 à la place de la figure 4 × 4 × 7 — octet pour octet SVG46, texte de l'énoncé inchangé ; Q5 ne porte aucun
     nombre, la base reste carrée (6 × 6), la figure est vraie.
  3. 46 Q4 option a et explication (§ 2).

## 2. L'écart 46 Q4 — jugement

- **L'auteur a raison** : mon option « 0 ≤ x² < 13 » était un encadrement VRAI (x² ∈ [0 ; 9[ ⊂ [0 ; 13[) — deux bonnes
  réponses. Erreur de mon texte, corrigée à juste titre.
- Remplacement « −2 < x² < 3 » (bornes de x recopiées sur x²) : FAUX (x = 2,5 donne x² = 6,25 > 3), erreur réelle d'élève,
  muette. Re-résolu à l'aveugle : clé b « 0 ≤ x² < 9 » seule juste ; c faux (x = 0), d faux (x = 2,5). Longueurs : a 11,
  b 10, c 10, d 10 signes → clé non la plus longue. Aucun vote ne désigne b.
- **Défaut restant (majeur, explication fausse)** : la nouvelle phrase dit « فيخرج −2 < x² < 3، وهو مستحيل لأنّ المربّع لا
  يكون سالبًا ». C'est faux : « −2 < x² » est toujours vrai et l'encadrement n'est pas impossible (x = 1 donne x² = 1, dedans) ;
  il est faux parce que x² peut dépasser 3. Texte de remplacement exact (seule cette phrase change) :
  - ancien : `أو نقل حدّي الحصر كما هما إلى x² فيخرج −2 < x² < 3، وهو مستحيل لأنّ المربّع لا يكون سالبًا.`
  - nouveau : `أو نقل حدّي الحصر كما هما إلى x² فيخرج −2 < x² < 3، وهو خطأ لأنّ x = 2,5 يعطي x² = 6,25 وهو أكبر من 3.`
  - Vérifié : 2,5² = 6,25 ; copie corrigée passée au banc Chromium `dir=rtl` (0 formule brouillée) et à `lot-lint` (0 point) ;
    la valeur 2,5 est déjà celle de l'argument contre d, aucune fuite.
- Mineur (accepté) : a est la seule option à borne négative ; un élève peut l'écarter parce qu'un carré n'est jamais négatif.
  C'est la connaissance visée, pas un indice de forme : on la garde.

## 3. Re-résolution à l'aveugle des questions retouchées et de leurs voisines

Clés lues dans les fichiers après résolution, toutes identiques :
- 42 : (37 − 33)(37 + 33) · 28 · (−9 ; −12) · 18 · 7√2 · 7√3 · √3/3.
- 43 : 5 · 15 < BH < 17 · 25/17 < CH < 5/3 · 162 + 36√14 · 6 + 3√14 · 3√14 − 6 · 90 · 18 + 6√14 (43 contrôles sympy,
  tous verts ; SVG43 : produit scalaire en A ≈ 10⁻¹², BH/BC et AH à l'échelle 280/18).
- 44 : « …= 2025 = BC²، قائم في A » · 21,6 · 486 · 22,5 · 15 · 7,2 · 162 (27² + 36² = 45² ; figures 3-4-5 : AB/AC/BC = 6 px/cm).
- 45 : 18 · 24 · 75 · 9 · 5√5 · « AB² + BC² = AC²، قائم في B » (carrés 25, 100, 125 recalculés).
- 46 : 6√3 · 11 · x² > 4 · 0 ≤ x² < 9 · AB² + BC² + CG² · 11 (SVG46 : 20 px/unité, fuyante (10 ; −7)/unité, cohérente).

**Clés fausses : 0.**

## 4. Contrôles transverses

- Fuites : aucune évitable restante ; seules subsistent les fuites structurelles déjà classées m4 (énoncé redonnant la valeur
  dont l'étape a besoin, donjon seulement). Note : 46 Q2 et 46 Q6 ont toutes deux la clé 11 — coïncidence, aucune question
  ne livre l'autre.
- Vote et longueurs : `lot-lint` 0 point sur les cinq fichiers ; aucune option somme de deux autres.
- Rendu `dir=rtl` : 0 formule brouillée sur les 34 questions.
- Doublons : `dupscan` (ch. 09) contre tout le publié de maths d'`origin/main` `cb46c2a8`, 09/47–51 et ch. 04 devoirs
  compris : aucune paire à options communes ; restent les parallèles de formulation déjà classés m8.

## 5. Bilan

- Clés fausses : 0. Majeurs restants : **1** — explication de 46 Q4 (texte au § 2). Mineurs : ceux de l'audit (m4 à m12),
  plus la borne négative de 46 Q4 a, acceptée.
- **Verdict : livrable après le remplacement d'une phrase dans 46 Q4** (aucune nouvelle re-vérification nécessaire au-delà
  d'un contrôle de ce remplacement).
