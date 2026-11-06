<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source : manuel élève officiel CNP 222472P00 (304 p.), mathématiques, 4ème année secondaire
     Sciences de l'informatique (auteurs M. Brahim, M. N. Souibki, M. Ben Mansour, M. Dga ;
     évaluateurs K. Turki, A. Jeridi). Aucun guide enseignant au corpus pour ce couple ⇒ le manuel
     élève fait référence. Lu le 2026-11-05 depuis le Drive `cnp-officiel` : couche texte (L1,
     `pdftotext -layout` page par page), puis vérification sur l'image (110 dpi, zooms 200–250 dpi)
     de TOUTES les pages (304/304 hors pages blanches) ; page PDF = page imprimée (offset 0).
     Fiche DIFFÉRENTIELLE : le contenu généré adapte les chapitres déjà publiés de math-bac-math,
     math-bac-techniques et math-bac-sciences-exp (demande de Mohamed du 2026-11-05 : « utilise ce
     qui est fait sur la branche mathématique ») ; chaque section note l'écart avec sa référence.
     ⚠️ Ce manuel est d'une AUTRE collection CNP que ceux des trois autres sections : l'écart se juge
     sur les notions et les tâches, pas sur la mise en page.
     Relecture R-7 du 2026-11-05 : 4 auditeurs indépendants (opus, contexte vierge) contre le PDF —
     100 % des encadrés et du chapitrage, sondage image 14 à 34 pages par chapitre ; 0 BLOCKER,
     1 MAJOR, ~35 MINOR, tous corrigés puis revérifiés par le même auditeur ; verdict CONFORME sur
     les 13 chapitres. -->

# Mathématiques — Bac Sciences de l'informatique (`bac-info`) · manuel officiel CNP

> **Source (Drive `cnp-officiel`, `manuels/`)** :
>
> - **Manuel élève** : code **222472P00** (304 p. ; p.303–304 blanches) — 13 chapitres en deux
>   parties (analyse : ch.1–8 ; arithmétique, complexes, systèmes linéaires, statistique,
>   probabilités : ch.9–13). Sommaire p.4.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
>   Le programme officiel ministériel n'est pas intégré au corpus (R-3) : le manuel prime.
> - **Langue d'enseignement** : **fr**. **subject id** : `math-bac-info` · **gradeSlug** : `bac-info`.
> - **Notation** : chiffres occidentaux 0-9, équations LTR ; la couche texte dégrade les formules
>   (racines, exposants, valeurs absolues, ≤/≥, ℝ, ∈, vecteurs, fractions, tableaux ; en ch.13 elle
>   remplace les symboles par de l'ASCII : # = Ω, " = ∩, % = ∪, $ = ∅, ! = λ) : toutes les formules,
>   encadrés et tableaux de cette fiche viennent de l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Sciences de l'informatique. La « Présentation et mode d'emploi »
(p.3) dit le manuel « conforme au programme de 4ème année secondaire sciences de l'informatique » et
conçu « dans le même esprit que celui de la 3ème année » : les programmes des deux années « ne peuvent
être lus indépendemment [sic] l'un de l'autre ». Chaque chapitre est découpé en paragraphes qui comportent
en général : **activités préliminaires** (« Préparation et consolidation des acquis antérieurs »),
**activités de découverte**, **« Tout ce qu'on doit savoir »** (légende, p.3, des encadrés de cours « A retenir », présents dans chaque chapitre ; il n'y a pas de page de synthèse de fin de chapitre), **applications**
(« Des applications immédiates pour mettre en pratique les savoirs »), puis en fin de chapitre
**« Apprendre à chercher »** (situations), une page **informatique** (tableur, GEOPLAN ou programme Pascal),
**Exercices et problèmes** et une page de **culture mathématique**.

Spécificités de la section, à garder à l'adaptation : **algorithmique** (programmes Turbo Pascal et
feuilles de tableur dans presque chaque chapitre), un chapitre **Systèmes d'équations linéaires**
(matrices, déterminant, inverse, pivot de Gauss, Cramer) absent des autres sections, une
**arithmétique** en un seul chapitre, des **nombres complexes sans argument** (ni forme
trigonométrique ni exponentielle), et une **statistique à deux caractères** avec ajustements non
affines.

Chaque section ci-dessous donne le plan du chapitre, ses activités et exercices en une ligne, ses
encadrés verbatim (vérifiés sur l'image), l'**écart avec la référence** (ce que le manuel n'a pas ⛔ et
ce qu'il ajoute), les bornes de scope ✅/⛔ et la note de lecture (sondage image, coquilles `[sic]`,
doutes `[?]`).

## 2. Plan annuel (carte des chapitres = sommaire p.4)

> Sommaire p.4 : le ch.13 « PROBABILITE » y est annoncé p.267 [sic] ; il commence en réalité p.269
> (p.267–268 = page de culture du ch.12). Les plages ci-dessous sont celles constatées sur les pages.

> `generation` = transcrit à profondeur de génération (chaque activité et exercice décrit, encadrés
> verbatim). La couverture de pages réelle vit dans `suivi/bac-info.json`. Colonne « référence » :
> chapitre(s) déjà publié(s) à adapter (le premier nommé est la base) ; « — » = à écrire de zéro.

| #   | Chapitre | pages (PDF = imprimées) | référence à adapter | profondeur |
| --- | -------- | ----------------------- | ------------------- | ---------- |
| 1 | Suites réelles | 5–25 | `math-bac-techniques/09`, `math-bac-sciences-exp/02` | `generation` |
| 2 | Limites de fonctions | 26–46 | `math-bac-sciences-exp/01`, `math-bac-techniques/01` (asymptote oblique) | `generation` |
| 3 | Continuité | 47–64 | `math-bac-sciences-exp/01` (I–III), `math-bac-sciences-exp/04` (IV, réciproque) | `generation` |
| 4 | Dérivation – primitives | 65–86 | `math-bac-sciences-exp/03` + `06`, `math-bac-sciences-exp/04` ((f⁻¹)′) | `generation` |
| 5 | Étude de fonctions | 87–108 | `math-bac-sciences-exp/05`, `math-bac-techniques/04` | `generation` |
| 6 | Logarithme népérien | 109–130 | `math-bac-sciences-exp/08` | `generation` |
| 7 | Fonctions exponentielles | 131–148 | `math-bac-sciences-exp/09`, `math-bac-techniques/07` | `generation` |
| 8 | Calcul intégral | 149–163 | `math-bac-sciences-exp/07`, `math-bac-techniques/08` | `generation` |
| 9 | Arithmétique | 164–188 | `math-bac-math/16` + `17` (fusionnés) | `generation` |
| 10 | Nombres complexes | 189–208 | `math-bac-sciences-exp/11` + `12` (très partiel : pas d'argument ici) | `generation` |
| 11 | Systèmes d'équations linéaires | 209–234 | — (aucun chapitre publié ; proches partiels : `math-1ere-sec/15`, `math-bac-sciences-exp/13`) | `generation` |
| 12 | Séries statistiques à deux caractères | 235–268 | `math-bac-techniques/16`, `math-bac-sciences-exp/17` | `generation` |
| 13 | Probabilités | 269–302 | `math-bac-techniques/14` + `15`, `math-bac-sciences-exp/15` + `16` | `generation` |

## 2.1 Chapitre 1 — Suites réelles (manuel 222472, p.5–25)

**Page de garde (p.5)** — « Chapitre 1 », titre « SUITES RÉELLES ». Plan imprimé : « I . Généralités ·
II . Opérations sur les limites · III. Convergence de suites monotones · IV . Suites et fonctions ».
Pas de citation liminaire : une photo légendée « Paul Erdös (1913-1996) Mathématicien hongrois, l'une des
figures marquantes du XXème siècle. » (Erdös reparaît dans l'encadré de l'Application 1 p.14.)

**Plan du chapitre** — phrase liminaire (p.6, en rose) : « Dans tout ce chapitre, s'il n'est pas précisé,
les suites sont définies sur IN. »

- **I. Généralités** (p.6–10) : Activités préliminaires 1–6 (p.6) · Activités de découverte 1–6 (p.6–8)
  · « A retenir » (p.8–9 : opérations sur les suites, suite monotone, majorée/minorée/bornée, suite
  convergente Déf. 1 et 2, Remarques) · « Applications » 1–4 (p.10).
- **II. Opérations sur les limites** (p.11–13) : Activités de découverte 1–3 (p.11) · « A retenir » (p.12 :
  tableaux somme/produit/quotient, Remarques, Théorèmes de comparaison) · « Applications » 1–3 (p.13).
- **III. Convergence de suites monotones** (p.13–14) : Activités de découverte 1–2 (p.13) · « A retenir »
  (p.13–14 : théorème admis + Remarques) · « Applications » 1–5 (p.14).
- **IV. Suites et fonctions** (p.15–16) : Activités de découverte 1–2 (p.15) · « A retenir » (p.15 :
  suite du type uₙ = f(n), image d'une suite par une fonction, Théorèmes 1 et 2) · « Applications » 1–2
  (p.16).
- **Apprendre à chercher** (p.17–18) : Situations 1–4, chacune avec « Vers une solution ».
- **Avec l'outil informatique** (p.19) : suite de Syracuse au tableur.
- **Exercices et problèmes** (p.20–24) : 25 exercices.
- **Maths et culture** (p.25) : « Suites de Farey ».

Pas de rubrique « QCM – Vrai-Faux » de fin de chapitre ni de page de synthèse de fin de chapitre :
le QCM et le Vrai-Faux sont placés dans les Applications du I (p.10). Pas d'exercice résolu.
Numérotation des activités : « préliminaires » 1–6 puis « de découverte » renumérotées à 1 dans chaque partie
(I : 1–6 ; II : 1–3 ; III : 1–2 ; IV : 1–2) ; Applications renumérotées 1… dans chaque partie.

### Cours — Activités (une ligne chacune)

**I. Généralités — Activités préliminaires** (p.6)

- **Act. prél. 1** (p.6) : (uₙ) définie par u₀ = 2 et uₙ₊₁ = 2uₙ − 3 ; démontrer par récurrence que
  uₙ = 3 − 2ⁿ pour tout n.
- **Act. prél. 2** (p.6) : démontrer que, « pour tout entier naturel n , n ≥ 1 », 1³ + 2³ + … + n³ =
  [n(n + 1)/2]².
- **Act. prél. 3** (p.6) : terme général donné, exprimer uₙ₊₁ en fonction de uₙ : a) uₙ = 3n + 2 ;
  b) uₙ = 3ⁿ⁻² ; c) uₙ = 2ⁿ/3ⁿ⁺¹.
- **Act. prél. 4** (p.6) : « Une seule des trois suites (aₙ), (bₙ) et (cₙ) est géométrique. Laquelle? »
  aₙ = 2²ⁿ⁺¹ × 5³⁻ⁿ ; bₙ = n² ; cₙ = √(cₙ₋₁² + 1).
- **Act. prél. 5** (p.6) : (uₙ) arithmétique de raison r = 1,5 et de premier terme u₁ = −30. 1) uₙ en
  fonction de n ; 2) montrer u_p − u_m = (p − m)r ; 3) vérifier u₁₀ = −16,5 et en déduire u₂₀.
- **Act. prél. 6** (p.6) : uₙ₊₁ = 1,2uₙ et u₀ = 100. 1) uₙ en fonction de n, en déduire u₂₀ ; 2) Sₙ = u₀ + u₁ + … + uₙ en fonction de n ; 3) calculer cette somme pour n = 20.

**I. Généralités — Activités de découverte** (p.6–8)

- **Act. 1** (p.6) : xₙ = (−3n² + 5)/(n + 1) sur IN ; yₙ = xₙ + 3n, zₙ = xₙ/n, tₙ = xₙ × yₙ ; pour chaque
  suite, valeurs de n pour lesquelles elle est définie et terme général. ➢ « On peut, comme dans le cas
  des fonctions, effectuer sur les suites les opérations d'addition, de multiplication et de division. »
- **Act. 2** (p.7) : u₀ = 5 et uₙ₊₁ = 2uₙ − 5. 1) démontrer uₙ ≥ 5 pour tout n ∈ IN ; 2) en déduire
  uₙ₊₁ ≥ uₙ. ➢ « On dit que la suite (uₙ) est croissante. »
- **Act. 3** (p.7) : vₙ = 1/n² (n ≥ 1). 1) cinq premiers termes ; 2) les ranger dans l'ordre croissant ; 3) a) exprimer vₙ₊₁/vₙ en fonction de n et le comparer à 1 ; b) en déduire vₙ₊₁ ≤ vₙ. ➢ « décroissante » ;
  ➢ « Une suite croissante ou décroissante est dite monotone. »
- **Act. 4** (p.7–8) : uₙ₊₁ = −0,75uₙ + 21 et u₀ = 4 ; figure (repère orthonormé) : courbe C_f de
  f : x ↦ −0,75x + 21, droite D : y = x, ligne polygonale « dont les cotés sont parallèles alternativement à l'axe des abscisses et à l'axe des
  ordonnées » [sic « cotés »], de sommets (uₙ ; f(uₙ)) et (uₙ ; uₙ), points A₀…A₇, u₀…u₅ placés sur l'axe. 1) refaire le dessin et placer u₆, u₇, u₈, u₉ ; 2) montrer que (uₙ) n'est pas monotone ; conjecturer sa limite ; 3) abscisse du point d'intersection de D
  et C_f ; 4) vₙ = uₙ − 12 : montrer que (vₙ) est géométrique, déterminer sa limite, retrouver celle de
  (uₙ). ➢ « La suite (uₙ) admet une limite réelle: on dit qu'elle est convergente. »
- **Act. 5** (p.8) : uₙ = 3 − 1/n sur IN* ; montrer 2 ≤ uₙ ≤ 3. ➢ majorée par 3 (majorant), minorée par 2
  (minorant) ; ➢ « Une suite majorée et minorée est dite bornée. »
- **Act. 6** (p.8) : uₙ = 2 + 3/n (n ≥ 1). 1) u₁, …, u₁₀ et valeurs approchées à 10⁻² près ; 2) conjecture
  quand n → +∞ ; 3) montrer que si n ≥ 300 alors |uₙ − 2| ≤ 1/100 ; 4) pour quels n a-t-on
  |uₙ − 2| ≤ 1/10⁷ ? Conclusion imprimée : « Plus généralement, on montre que si ε est un réel strictement
  positif, il existe un entier p tel que: si n ∈ IN et n ≥ p alors |uₙ − 2| ≤ ε. ➢ Le résultat précédent
  se traduit par “ pour tout intervalle I contenant 2 il existe un entier p tel que pour tout entier
  n ≥ p , on a uₙ ∈ I “. » (sic : « intervalle » sans « ouvert »).

**II. Opérations sur les limites — Activités de découverte** (p.11)

- **Act. 1** (p.11) : uₙ = −3 + 1/(n + 1) et vₙ = (n − 2)/(2n) sur IN*. 1) montrer, à l'aide de la
  définition, lim uₙ = −3 et lim vₙ = 1/2 ; 2) w = u + v et t = u.v : conjecturer leurs limites. ➢ « Plus
  généralement, on montre que si u et v sont deux suites telles que lim uₙ = ℓ et lim vₙ = ℓ′ alors on a :
  lim (uₙ + vₙ) = ℓ + ℓ′ ; lim (uₙ.vₙ) = ℓ.ℓ′ ».
- **Act. 2** (p.11) : pour n ≥ 2, uₙ = 1/(n + (−1)ⁿ). 1) montrer 1/(n + 1) ≤ uₙ ≤ 1/(n − 1) ; 2) conjecturer
  la limite. ➢ « Plus généralement, on montre que si u , v et w sont trois suites réelles vérifiant :
  { - Pour tout n > n₀, vₙ ≤ uₙ ≤ wₙ et - lim vₙ = lim wₙ = ℓ } alors lim uₙ = ℓ ».
- **Act. 3** (p.11) : 1) uₙ = (n² + 2n + 2)/n (n > 0) : démontrer uₙ > n, conjecturer la limite ; 2) vₙ = (−1 − n)/√n (n > 0) : vérifier vₙ < √n [sic, voir doutes] ; conjecturer la limite de (vₙ).

**III. Convergence de suites monotones — Activités de découverte** (p.13)

- **Act. 1** (p.13) : u₁ = 1,38 ; u₂ = 1,338 ; … ; uₙ = 1,33…38 (n chiffres 3 suivis du chiffre 8). Item 1) vérifier uₙ − 1 = 3 Σ_{i=1}^{n} 10⁻ⁿ + 8 × 10⁻ⁿ⁻¹ [sic, voir doutes] ; 2) montrer que la suite est
  décroissante et minorée ; 3) montrer que pour tout n > 0, 0 ≤ |uₙ − 4/3| ≤ 10⁻ⁿ ; « Que peut-on déduire ? »
- **Act. 2** (p.13) : uₙ = 2ⁿ − n, n ∈ IN. 1) dix premiers termes à la calculatrice, conjecture sur le sens
  de variation et la limite ; 2) montrer uₙ₊₁ − uₙ ≥ 0 pour n ≥ 1 ; 3) montrer par récurrence que pour tout
  « n ≥ I » [sic, pour n ≥ 1] uₙ ≥ 2ⁿ⁻¹. Conclure.

**IV. Suites et fonctions — Activités de découverte** (p.15)

- **Act. 1** (p.15) : 1) uₙ = √(1 + n + n²) sur IN [question sans verbe imprimé] ; 2) limite de
  f(x) = √(x² + x + 1) quand x → +∞ ; 3) en posant uₙ = f(n), que déduire sur la limite de (uₙ) en +∞ ?
- **Act. 2** (p.15) : u₀ = 0 et uₙ₊₁ = √(uₙ + 6). 1) construire la courbe de f(x) = √(x + 6) (x ≥ −6) et la
  droite y = x ; 2) placer sur l'axe des abscisses les 5 premiers termes ; 3) montrer que (uₙ) est
  croissante et majorée par 3, en déduire qu'elle converge ; conjecture sur la limite ; 4) montrer
  0 ≤ 3 − uₙ₊₁ ≤ (1/3)(3 − uₙ), puis par récurrence 0 ≤ 3 − uₙ ≤ 1/3ⁿ⁻¹ ; 5) en déduire la limite et la
  comparer avec la solution de f(x) = x.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Opérations sur les suites** (p.8) — « Soient (u) et (v) deux suites définies pour tout
> entier n ≥ n₀ . La somme de u et v est la suite,notée u+ v, dont le terme général est uₙ+ vₙ(n ≥ n₀)
> Le produit de u et v est la suite notée (u x v) , dont le terme général est uₙ x vₙ (n ≥ n₀)
> Si pour tout n ≥ n₀ , vₙ ≠ 0 le quotient de u par v est la suite, notée u/v , dont le terme général
> est uₙ/vₙ ( n ≥ n₀ ) »

> **Suite monotone — Définitions** (p.8–9) — « Soit (uₙ) une suite numérique définie pour tout entier
> n ≥ n₀ . On dit que : •La suite (uₙ) est croissante lorsque, pour tout entier n ≥ n₀ , uₙ ≤ uₙ₊₁ .
> •La suite (uₙ) est décroissante lorsque, pour tout entier n ≥ n₀ , uₙ ≥ uₙ₊₁ . •La suite (uₙ) est
> monotone lorsqu'elle est croissante ou décroissante. »

> **Suite majorée, suite minorée — Définitions** (p.9) — « Soit (uₙ) une suite numérique définie pour
> tout entier n ≥ n₀. On dit que : •La suite (uₙ) est majorée s'il existe un réel M tel que, pour tout
> entier n ≥ n₀, uₙ ≤ M •La suite(uₙ)est minorée s'il existe un réel m tel que, pour tout entier n ≥ n₀ ,
> uₙ ≥ m •La suite (uₙ) est bornée si elle est à la fois majorée et minorée. »

> **Suite convergente — Définition 1** (p.9) — « • Soit (uₙ) une suite définie pour tout entier n ≥ n₀
> et ℓ un nombre réel. On dit que la suite (uₙ) tend vers ℓ quand n tend vers +∞ si : Pour réel ε > 0,
> il existe p∈IN tel que: (n∈IN et n ≥ p) ⇒ (|uₙ − ℓ| < ε) On écrit : lim_{n→+∞} uₙ = ℓ » (sic :
> « Pour réel » sans « tout ».) Figure : droite réelle R avec ℓ, un intervalle centré en ℓ contenant uₙ,
> et droite N avec 0, 1, p, n.
> « •Une suite non convergente est dite divergente. »

> **Définition 2** (p.9) — « Soit (uₙ) une suite définie pour tout entier n ≥ n₀ . On dit que la suite
> (uₙ) tend vers +∞ (respectivement −∞ ) quand n tend vers +∞ si:Pour tout réel A > 0, il existe p ∈ IN
> tel que: (n∈IN et n ≥ p)⇒ uₙ > A (resp. uₙ < -A) . On écrit : lim_{n→+∞} uₙ = +∞ (resp.
> lim_{n→+∞} uₙ = −∞) »

> **Remarques** (p.9) — « 1. Si une suite est convergente, sa limite est unique. 2. Toute suite
> géométrique de raison q telle que |q| < 1 est convergente vers 0 3. Si q > 1 alors lim_{n→+∞} qⁿ = +∞ 4. Si q < -1 alors la suite (qⁿ) n'a pas de limite »

> **A retenir — Opérations sur les limites — Théorème** (p.12) — « Soit (uₙ) et (vₙ) deux suites
> vérifiant lim_{n→+∞} uₙ = a et lim_{n→+∞} vₙ = b ( a et b désignent des réels ou l'un des symboles +∞
> et −∞ ). On peut conclure sur la limite de la somme, du produit et du quotient dans certains cas,
> consignés dans les tableaux suivants : »
> **1) la somme ( uₙ+ vₙ )** (lignes a, colonnes b) : a réel : b réel → a+b ; +∞ → +∞ ; −∞ → −∞ ·
> a = +∞ : b réel → +∞ ; +∞ → +∞ ; −∞ → case barrée · a = −∞ : b réel → −∞ ; +∞ → case barrée ; −∞ → −∞.
> **2) le produit uₙ . vₙ** : a réel : b réel → ab ; +∞ → ±∞ (a ≠ 0) ; −∞ → ±∞ (a ≠ 0) · a = +∞ : b réel
> → ±∞ (b ≠ 0) ; +∞ → +∞ ; −∞ → −∞ · a = −∞ : b réel → ±∞ (b ≠ 0) ; +∞ → −∞ ; −∞ → +∞.
> **3) Le quotient uₙ/vₙ** : a réel : b réel ≠ 0 → a/b ; +∞ → 0 ; −∞ → 0 · a = +∞ : b réel ≠ 0 → ±∞ ;
> +∞ et −∞ → cases barrées · a = −∞ : b réel ≠ 0 → ±∞ ; +∞ et −∞ → cases barrées.

> **Remarques** (p.12) — « • Si lim uₙ = +∞ et, lim vₙ = −∞ alors on ne peut pas conclure pour
> lim (uₙ + vₙ) • Si lim uₙ = ∞ et, lim vₙ = 0 , alors on ne peut pas conclure pour lim (uₙvₙ) • Si
> lim uₙ = ∞ et, lim vₙ = ∞ , ou si lim uₙ = 0 et, lim vₙ = 0 alors on ne peut pas conclure pour
> lim (uₙ/vₙ) » (toutes les limites en n → +∞.)

> **Théorèmes de comparaison** (p.12) — « Nous admettons les résultats énoncés dans le tableau suivant :
> -les quatre premiers permettent de déterminer le comportement à l'infini d'une suite par comparaison
> à d'autres suites dont le comportement est connu ; -le dernier résultat autorise le passage à la
> limite dans une inégalité. »
> Tableau (hypothèse 1 : « une inégalité (à partir d'un certain rang) » | hypothèse 2 : « Comportement à
> l'infini » | conclusion) :
> uₙ ≤ xₙ | lim uₙ = +∞ | lim xₙ = +∞ ·
> xₙ ≤ uₙ | lim uₙ = −∞ | lim xₙ = −∞ ·
> uₙ ≤ xₙ ≤ vₙ | (uₙ) et (vₙ) convergent vers la même limite ℓ | (xₙ) converge et lim xₙ = ℓ ·
> |xₙ − ℓ| ≤ uₙ | lim uₙ = 0 | (xₙ) converge et lim xₙ = ℓ ·
> xₙ ≤ yₙ | « lim xₙ = ℓ et » [la suite « lim yₙ = ℓ′ » n'est pas imprimée : sic, vérifié à 220 dpi] | ℓ ≤ ℓ′.

> **A retenir — Convergence de suites monotones — Théorème (admis)** (p.13) — « • Si une suite est
> croissante et majorée , alors elle est convergente. • Si une suite est décroissante et minorée, alors
> elle est convergente. »
> **Remarques** (p.14) — « • Si une suite (uₙ) est croissante et non majorée, alors lim_{n→+∞} uₙ = +∞
> • Si une suite (vₙ) est décroissante et non minorée , alors lim_{n→+∞} uₙ = −∞ » (sic : (vₙ) puis uₙ.)

> **A retenir — Suite du type uₙ = f(n) — Théorème** (p.15) — « Soit (uₙ) une suite de terme général
> uₙ = f(n) où f est une fonction. Si lim_{x→+∞} f(x) = l ( fini ou infini), alors lim_{n→+∞} uₙ = l »

> **Image d'une suite par une fonction — Théorème1** (p.15) — « Soit f une fonction définie sur un
> intervalle I et (uₙ) une suite de nombres réels de I. Si lim_{n→∞} uₙ = a et lim_{x→a} f(x) = l ,alors
> lim_{n→+∞} f(uₙ) = l (a,l finis ou infinis) »

> **Théorème2** (p.15) — « I est un intervalle non vide et non réduit à un point de IR . f est une fonction
> définie sur I et (uₙ) une suite de nombres réels de I telle que lim_{n→∞} uₙ = ℓ où ℓ ∈ I • Si f est continue
> en ℓ , alors la suite (f(uₙ)) converge vers f( ℓ ) • Dans le cas où f(I) ⊂ I et la suite (uₙ) est
> définie par u₀ ∈ I et pour tout n ∈ IN; uₙ₊₁ = f(uₙ) on a: Si f est continue en ℓ , alors la suite
> (f(uₙ)) converge vers f(ℓ) et f(ℓ) = ℓ »

### Applications (exercices d'application intégrés au cours)

**Applications du I** (p.10)

- **1 – Q.C.M.** « Trouver la seule bonne réponse. » (réponses non fournies) 1) uₙ = 3 − 2/(n + 1) :
  a. croissante b. décroissante c. non monotone ; 2) uₙ = (5n − 1)/(n + 3) : a. majorée par 5 b. minorée
  par 1 ; 3) u₀ = 4 et uₙ₊₁ = −3 + uₙ : a. croissante b. décroissante c. non monotone ; 4) uₙ = 1,01ⁿ/10⁵ :
  a. converge vers 0 b. a pour limite +∞ c. n'a pas de limite ; 5) uₙ = (2n + 3)/(n + 3) : a. converge vers 0
  b. converge vers 2 c. diverge ; 6) uₙ = 2 − 0,5ⁿ : a. converge vers 0 b. converge vers 2 c. diverge.
- **2 – Vrai ou Faux.** « Corriger les énoncés faux: » 1) u₀ = −1, uₙ₊₁ = uₙ + 0,1 est décroissante ; 2) uₙ = −(2/3)ⁿ est décroissante ; 3) uₙ = 1/n (n > 0) est majorée par 1 et minorée par 0 ; 4) (uₙ)
  (n ∈ IN) décroissante ⇒ majorée par u₀ ; 5) (uₙ) croissante ⇒ minorée par u₀.
- **3** : montrer que uₙ = 1 + (−1)ⁿ/n (sur IN*) n'est pas monotone.
- **4** : 1) montrer à l'aide de la définition que uₙ = 1/n converge vers 0 ; 2) que uₙ = n a pour limite
  +∞. (« On montre de façon générale que si p est un entier strictement positif, la suite de terme général
  (1/nᵖ) converge vers 0 et la suite de terme général (nᵖ) admet pour limite +∞ ».)

**Applications du II** (p.13)

- **1** : limite de (uₙ) : a) 3n² − 1 + 1/n ; b) 1 − 5ⁿ ; c) (1 − 3n)(n² + n − 2) ;
  d) 1 + 1/7 + 1/7² + … + 1/7ⁿ ; e) (−1/2)ⁿ + 3 ; f) 1/(n + 5ⁿ).
- **2** : limite à l'aide d'un théorème de comparaison : a) cos n − n ; b) 2n + (−1)ⁿ ; c) (−1)ⁿ/√n.
- **3** : uₙ = √(n² + n) et vₙ = −n. 1) limites de (uₙ) et (vₙ) ; 2) peut-on déterminer lim (uₙ + vₙ) à partir
  du tableau ? 3) montrer uₙ + vₙ = 1/(1 + √(1 + 1/n)) pour n > 0, en déduire la limite.

**Applications du III** (p.14)

- **1** : u₁ = 0,2 ; u₂ = 0,23 ; u₃ = 0,235 ; … ; u₇ = 0,2357111317 (« uₙ s'écrit 0 virgule, suivi de la
  juxtaposition des n premiers nombres premiers ») ; montrer que (uₙ) converge. Encadré : « La limite l de
  cette suite est un réel mystérieux imaginé par le mathématicien Paul Erdös (mathématicien hongrois, l'une
  des figures marquantes du XXè siècle). »
- **2** : uₙ = 3ⁿ/n². 1) monotonie ; 2) par récurrence, pour n ≥ 13, uₙ ≥ 2ⁿ ; 3) limite.
- **3** : u₀ = 0 et uₙ₊₁ = 3√uₙ + 4. 1) conjecturer graphiquement ; 2) montrer 0 ≤ uₙ ≤ uₙ₊₁ ≤ 16 ; 3) en déduire la convergence.
- **4** : « Que penses-tu des affirmations suivantes ? » 1) une suite non majorée n'a pas nécessairement pour
  limite +∞ (vérifier avec uₙ = [(−1)ⁿ + 1]n) ; 2) 1,999999 est un majorant de vₙ = 2 − 1000/n.
- **5** : uₙ = 1 + 1/2³ + 1/3³ + … + 1/n³ (n ≥ 1). 1) par récurrence uₙ ≤ 2 − 1/n ; 2) en déduire la
  convergence. Encadré : « 1,202056903159594… C'est la limite de la suite (uₙ) de l'exercice 5 . Le français
  Robert Apéry a prouvé, en 1979, que ce nombre est irrationnel. Est-il transcendant ? Nul ne le sait à ce
  jour. (un nombre est transcendant s'il n'est racine d'aucun polynôme à coefficients entiers) »

**Applications du IV** (p.16)

- **1** : figure : courbe C de f(x) = √(x + 3) (x > 0) et droite y = x ; u₀ et u₁ marqués sur l'axe des
  abscisses (u₀ ≈ 8 lu sur le quadrillage, non donné numériquement) ; uₙ₊₁ = f(uₙ). « Quelles conjectures
  peut-on émettre sur cette suite ? Prouver ces conjectures. » (texte : « les 4 premiers termes » ; la
  figure n'en montre que 2 — voir doutes.)
- **2** : u₀ = 1 et uₙ₊₁ = 5uₙ/(3uₙ + 5). 1) a) uₙ > 0 ; b) décroissante, en déduire la convergence ;
  c) limite ; 2) vₙ = 5/uₙ : a) (vₙ) arithmétique ; b) vₙ puis uₙ en fonction de n ; 3) retrouver la limite.

### Apprendre à chercher (p.17–18)

- **Situation 1** (p.17) : demi-cercle de diamètre AB = 1 ; points B₀, B₁, B₂, …, Bₙ définis par B₀B = √2/2,
  B₁B = 1/2, B₂B = 1/3, B₃B = 1/4, …, BₙB = 1/n [sic, voir doutes]. « Démontrer que : AB₁ × AB₂ × AB₃ × … ×
  ABₙ > AB₀ ». Conjecture sur ce produit quand n → ∞. **Vers une solution** : élever au carré ; Pythagore :
  AB₁² × AB₂² × … × ABₙ² = (1 − 1/2²).(1 − 1/3²)….(1 − 1/n²) ; utiliser a² − b² = (a − b)(a + b) ; on obtient
  1/2 × 2/3 × … × (n − 2)/(n − 1) × (n − 1)/n × (n + 1)/n × n/(n − 1) × … × 4/3 × 3/2 ; « Ensuite simplifier. »
- **Situation 2** (p.17) : démontrer que pour tout n ∈ IN* : 1/2 × 3/4 × 5/6 … (2n − 1)/(2n) < 1/√(2n + 1).
  **Vers une solution** : étudier le carré du premier membre et majorer toute fraction (2k − 1)/(2k)
  figurant deux fois par 2k/(2k + 1).
- **Situation 3** (p.18) : aire A du domaine { 0 ≤ x ≤ 1 ; 0 ≤ y ≤ x² } (figure 1). **Vers une solution** :
  partage de [0;1] en n segments de longueur 1/n ; uₙ = somme des aires des rectangles au-dessous de la
  courbe, vₙ = au-dessus ; « L'évidence géométrique nous autorise à écrire que, pour tout entier n ≥ 1,
  uₙ ≤ A ≤ vₙ » ; calculer uₙ et vₙ puis montrer A = 1/3.
- **Situation 4** (p.18) : « Etudier la suite de terme général » uₙ = 1/1² + 1/2² + … + 1/n². **Vers une solution** : uₙ₊₁ − uₙ = 1/(n + 1)² ≥ 0 ;
  question « la suite est-elle ou non majorée ? » ; pour k ≥ 2, 1/k² ≤ 1/(k(k − 1)) = 1/(k − 1) − 1/k ;
  sommer de k = 2 à n : uₙ ≤ 2 − 1/n ou encore uₙ ≤ 2. Conclure.

### Avec l'outil informatique (p.19) — suite de Syracuse

« La suite de Syracuse est définie par u₀ ∈ IN et pour tout n ∈ IN uₙ₊₁ = uₙ/2 si uₙ est pair ; 3uₙ + 1 si
uₙ est impair ». « Le problème que se posent les mathématiciens est le suivant: " Quel que soit le nombre N
choisi au départ, la suite obtenue est-elle finie ? " Aujourd'hui, les mathématiciens pensent qu'il en est
ainsi mais ne l'ont pas démontré, le problème résiste depuis 50 ans. » Tableur : essayer N = 3 ; 4 ; 26 ;
27 ; « Taper en A1 choisir N. Entrer un entier quelconque en B1. En B2, taper la formule
`=SI(OU (B1=1 ;B1= " ") ; " " ;SI(MOD(B1 ;2)=0 ;B1/2 ;3*B1+1))` Recopier cette formule vers le bas. »

### Exercices et problèmes (p.20–24) — 25 exercices

- **Ex. 1** (p.20) : donner un exemple de suite (uₙ) : 1) majorée et non minorée ; 2) strictement positive et
  convergeant vers 0 ; 3) bornée et divergente ; 4) convergeant vers 0 et non monotone ; 5) minorée par 0,
  non constante, convergeant vers 1 ; 6) bornée par 0 et 2, non constante, convergeant vers 1 ; 7) divergeant
  vers +∞ et non croissante ; 8) non majorée et ne divergeant pas vers +∞.
- **Ex. 2** (p.20) : (uₙ) à termes strictement positifs, vₙ = 1/uₙ ; vrai ou faux (justifier / contre-exemple) : item 1) (uₙ)
  croissante ⇒ (vₙ) décroissante ; 2) bornée ⇒ (vₙ) bornée ; 3) minorée par 1 ⇒ (vₙ) majorée par 1 ; item 4) (uₙ) diverge ⇒ (vₙ) converge vers 0 ; 5) (uₙ) converge ⇒ (vₙ) converge.
- **Ex. 3** (p.20) : arithmétique (A), géométrique (G) ou ni l'une ni l'autre (N), justifier : 1) 2ⁿ + 1 ; 2) 1/2ⁿ ; 3) −(n + 3) ; 4) −2n + 3 ; 5) u₀ = 1, uₙ₊₁ = uₙ + n ; 6) u₀ = 1, uₙ₊₁ = 2 + uₙ ; 7) u₀ = 1, uₙ₊₁ = −3uₙ.
- **Ex. 4** (p.20) : monotonie par la technique indiquée : 1) différence uₙ₊₁ − uₙ : a) 1 + 1/√2 + 1/√3 + … +
  1/√n ; b) n² − 5n ; c) 3n + (−1)ⁿ ; d) n − 3ⁿ ; 2) quotient uₙ₊₁/uₙ : a) n/3ⁿ ; b) 0,1ⁿ × n² ;
  c) 1/2 × 3/4 × … × (2n − 1)/(2n) ; 3) fonction f « uₙ = f(n) » : a) n + cos n ; b) (n² − 1)/(n² + 1) ;
  c) n²(3 − n) ; 4) récurrence : a) u₀ = 5, « uₙ = √(uₙ + 2) » [sic, pour uₙ₊₁] ; b) u₀ = 7π/22,
  uₙ₊₁ = uₙ².
- **Ex. 5** (p.20–21) : montrer que la suite est majorée (déterminer un majorant) : a) 1 + 2/7 + … + (2/7)ⁿ ;
  b) 10 + 2cos n ; c) 9 + 3 + 1 + … + 3⁻ⁿ⁺² ; d) 3n/(n + 1) ; e) 1/n − 1/√n.
- **Ex. 6** (p.21) : montrer que uₙ = 1 + 0,6 + 0,6² + … + 0,6ⁿ est majorée.
- **Ex. 7** (p.21) : trouver l'erreur : « On pose: x = 1 + 5/4 + (5/4)² + (5/4)³ + … alors (5/4)x = 5/4 +
  (5/4)² + (5/4)³ + …. Donc : x − (5/4)x = 1 et donc x = −4 ».
- **Ex. 8** (p.21) : uₙ = (−3)ⁿ + 4. 1) 6 premiers termes ; 2) conjecture convergence/divergence ; 3) calculer uₙ₊₁ − uₙ et vérifier |uₙ₊₁ − uₙ| > 1 ; 4) l réel quelconque : trouver un intervalle ouvert de
  centre l qui ne contient pas à la fois uₙ et uₙ₊₁.
- **Ex. 9** (p.21) : uₙ₊₁ = f(uₙ), f représentée par la courbe C (trois graphiques ① ② ③ avec y = x et u₀
  marqué) ; conjecturer sens de variation et limite à l'aide de la représentation graphique.
- **Ex. 10** (p.21) : valeur de uₙ = (1 − 1/4)(1 − 1/9)(1 − 1/16)… ?
- **Ex. 11** (p.21) : u₁ = 0,1 ; u₂ = 0,12 ; u₃ = 0,123 ; … ; u₁₀ = 0,12345678910 (juxtaposition des entiers
  1, 2, …, n après la virgule) ; montrer que (uₙ) converge. Encadré : « La limite l de cette suite est
  appelée le nombre de Champernowne - du nom du mathématicien anglais qui l'a imaginé en 1933. Ce nombre est
  irrationnel, et même transcendant : résultat prouvé par l'allemand Kurt Mahler en 1961…sur son lit
  d'hôpital ! (un nombre est transcendant s'il n'est racine d'aucun polynôme à coefficients entiers) »
- **Ex. 12** (p.22) : (uₙ) positive, u₀ = 10 et (uₙ₊₁)² = 1 + (uₙ − 1)². 1) représentation géométrique de la
  relation définissant u₁ ; 2) carré c₀ de côté u₀ et, à l'intérieur, carré c₁ de côté u₁ ; 3) itérer jusqu'à
  u₁₀ ; conjecturer la limite de (uₙ)² puis de uₙ ; valider algébriquement.
- **Ex. 13** (p.22) : u₀ = 10 et (uₙ₊₁)² = (uₙ)² − 3uₙ + 3. 1) vérifier (uₙ₊₁)² = (uₙ − 1)² + 1 − 2 × (uₙ − 1)
  × cos 60° ; 2) interprétation géométrique de la relation entre u₀ et u₁ ; 3) itérer ; « Que se passe-t-il ? »
  ; revenir à l'étude algébrique.
- **Ex. 14** (p.22) : un carré partagé en quatre, on noircit le carré inférieur gauche, on recommence dans le
  carré en haut à droite, etc. (figure) ; aire finale de la partie noire ?
- **Ex. 15** (p.22) : P₀ carré A₀B₀C₀D₀ de côté 10 cm ; P₁ a ses sommets sur les côtés de P₀ à 1 cm des
  sommets ; P₂, P₃… de même (deux figures) ; le dessin s'arrête-t-il, comment évoluent côtés et aires ?
- **Ex. 16** (p.22) : u₀ = 3, uₙ₊₁ = 2/(1 + uₙ). 1) tous les termes sont positifs ; 2) si la suite converge, sa
  limite est solution de x² + x − 2 = 0 ; 3) vₙ = (uₙ − 1)/(uₙ + 2) : (vₙ) géométrique convergente, limite ; 4) convergence et limite de u.
- **Ex. 17** (p.22–23) : uₙ = n¹⁰/2ⁿ. 1) pour n > 0 : uₙ₊₁/uₙ ≤ 0,95 ⇔ (1 + 1/n)¹⁰ ≤ 1,9 ; 2) f(x) =
  (1 + 1/x)¹⁰ sur [1;+∞[ : a) variation et limite en +∞ ; b) existence de α ∈ [1;+∞[ avec f(α) = 1,9 ;
  c) entier n₀ tel que n₀ − 1 ≤ α ≤ n₀ ; d) pour n ≥ 16, (1 + 1/n)¹⁰ ≤ 1,9 ; 3) a) sens de variation de (uₙ)
  à partir du rang 16 ; b) conséquence ; 4) a) par récurrence, pour n ≥ 16, 0 ≤ uₙ ≤ 0,95ⁿ⁻¹⁶u₁₆ ; b) limite.
- **Ex. 18** (p.23) : 1) v₀ = 1, vₙ₊₁ = vₙ + 2(n + 1) : v₁…v₄ ; démontrer vₙ = n² + n + 1 ; 2) « phénomène
  étrange » : √1 = 1, √(3 + √1) = 2, √(7 + √(3 + √1)) = 3, √(13 + √(7 + √(3 + √1))) = 4 ; avec u₁ = 1 et
  uₙ₊₁ = √(vₙ + √uₙ), démontrer ce phénomène.
- **Ex. 19** (p.23) : u₀ = 1, u₁ = 2 et « pour tout n ≥ 2 » [sic, incohérent avec le calcul de u₂ : n ≥ 0 attendu] uₙ₊₂ = 6uₙ₊₁ − 5uₙ. 1) u₂, u₃, u₄ ; 2) résoudre x² = 6x − 5 ; 3) α et β tels que uₙ = α × 5ⁿ + β ; en déduire u₁₀.
- **Ex. 20** (p.23) : uₙ = √(n² + 6n) − n (n ≥ 0). 1) conjecture à la calculatrice pour n = 10³, 10⁴, …, 10¹⁵ ; 2) établir uₙ = 6/(√(1 + 6/n) + 1), en déduire « lim_{x→+∞} uₙ » [sic x] ; 3) expliquer le comportement
  « anormal » de la calculatrice.
- **Ex. 21** (p.23) : u₀ = 1, uₙ₊₁ = uₙ + 2n + 3. 1) monotonie ; 2) a) uₙ ≥ n² ; b) limite ; 3) conjecturer
  une expression de uₙ et la démontrer.
- **Ex. 22** (p.24) : A₀, B₀ distincts ; A₁ milieu de [A₀B₀], B₁ barycentre de {(A₀;1),(B₀;2)} ; A₂ milieu de
  [A₁B₁], B₂ barycentre de {(A₁;1),(B₁;2)}, etc. 1) placer A₁, B₁, A₂, B₂ pour A₀B₀ = 12 cm, conjecture ; 2) repère (A₀; i⃗) avec i⃗ = (1/12)A₀B₀⃗ ; uₙ, vₙ abscisses de Aₙ, Bₙ : justifier uₙ₊₁ = (uₙ + vₙ)/2 et
  vₙ₊₁ = (uₙ + 2vₙ)/3 ; 3) a₀ = 0, b₀ = 12, aₙ₊₁ = (aₙ + bₙ)/2, bₙ₊₁ = (aₙ + 2bₙ)/3 : a) wₙ = bₙ − aₙ
  géométrique convergente à termes positifs ; b) (aₙ) croissante, (bₙ) décroissante ; c) (aₙ) et (bₙ)
  convergent et ont la même limite ; d) tₙ = 2aₙ + 3bₙ constante ; 4) limite des points Aₙ et Bₙ.
- **Ex. 23** (p.24) : uₙ = 1 − 10⁻ⁿ et vₙ = 1 + 10⁻ⁿ. 1) u₀, v₀, …, u₄, v₄ ; 2) convergence et limite ; 3) « Que peut-on dire du nombre dont l'écriture décimale est 0,9999…(avec une infinité de 9) ? »
- **Ex. 24** (p.24) : Sₙ = 1 + 1/2 + 1/3 + … + 1/n. 1) pour n ≥ 1, S₂ₙ ≥ 1/2 + Sₙ ; 2) par récurrence sur k,
  pour tout k il existe n tel que Sₙ ≥ k ; en déduire que (Sₙ) diverge.
- **Ex. 25** (p.24) : 1) nombre de termes de S = 1! + 2! + … + (n − 1)! ; 2) S ≤ (n − 1) × [(n − 1)]!, puis
  S ≤ n! ; 3) uₙ = (1! + 2! + 3! + … + (n − 1)! + n!)/(n + 1)! (n ≥ 1) : établir 0 ≤ uₙ ≤ 2(n!)/(n + 1)!, puis
  0 ≤ uₙ ≤ 2/(n + 1) ; 4) limite de 2/(n + 1), puis de (uₙ).

### Maths et culture (p.25) — « Suites de Farey »

Texte historique (John Farey 1766-1826, géologue ; Cauchy ; Lester Ford ; Hardy : « Farey est immortel pour
avoir échoué à comprendre un théorème que Haros avait parfaitement démontré quatorze ans plus tôt » ; lettre
de 1816 au Philosophical Magazine « On a curious Property of vulgar Fractions »). Définition : « Pour
construire la suite de Farey Fₙ d'ordre n, on range, en ordre croissant, les fractions irréductibles
comprises entre 0 et 1 dont le dénominateur est inférieur ou égal à n. » F₁ = {0,1}, F₂ = {0, 1/2, 1},
F₃ = {0, 1/3, 1/2, 2/3, 1}, F₄ = {0, 1/4, 1/3, 1/2, 3/4, 1} [sic : 2/3 omis], F₅ = {0, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4,
4/5, 1}. Propriétés : « 1) Si p/q et p′/q′ sont deux fractions consécutives de Fₙ, on a qp′ − pq′ = 1. 2) Si p/q , p″/q″ , p′/q′ sont trois fractions successives de, on a : p″/q″ = (p + p′)/(q + q′) » (sic :
« de » sans Fₙ). Illustrations : cercles de Ford ; illustration tridimensionnelle.

### Écart avec la référence (`math-bac-techniques/09` en priorité, `math-bac-sciences-exp/02`)

**Correspondance corrigée** : le brief proposait sciences-exp/02 puis techniques/09. Sur les notions, ce
chapitre est **plus proche de techniques/09** (sens de variation, majorée/minorée/bornée, limite, opérations,
monotone bornée, point fixe, suite auxiliaire, comparaison — et **ni sous-suites ni suites adjacentes**) ;
sciences-exp/02 reste utile pour les sommes Σ (Σ 1/k² majorée) et uₙ₊₁ = f(uₙ) ; la définition par ε, elle, est absente des deux références.

**Ce que les références enseignent et que ce manuel n'a PAS (à retirer)** :

- sciences-exp/02 : **sous-suites paire et impaire** (théorème des rangs pairs/impairs) et **suites
  adjacentes** (définition + théorème) — absentes du cours ici ; l'Ex. 22 fait établir à la main que (aₙ) et
  (bₙ) « convergent et ont la même limite » sans le mot « adjacentes » ;
- sciences-exp/02 : rappel de la limite usuelle sin x/x et du chapitre de continuité préalable (ici les
  Suites sont le **chapitre 1**, AVANT Limites et Continuité : les théorèmes « fonction » du IV s'appuient sur
  des limites de fonctions vues en 3ᵉ année) ;
- techniques/09 : les **suites d'intégrales** (section comparaison) — le calcul intégral est le chapitre 8
  de ce manuel ; les fils rouges contextualisés (atelier, bassin) ;
- « une suite convergente est bornée » (les deux références) et « lim uₙ₊₁ = lim uₙ » (techniques/09 seulement)
  ne sont pas énoncées
  ici en encadré.

**Ce que ce manuel a en plus (ou autrement)** :

- **définition formelle par ε** de la limite finie (Déf. 1) et par A pour la limite infinie (Déf. 2), avec
  exercices « à l'aide de la définition » (App. I.4, II Act. 1) ;
- **activités préliminaires** de révision 3ᵉ année : récurrence (uₙ = 3 − 2ⁿ ; somme des cubes), suites
  arithmétiques et géométriques (u_p − u_m = (p − m)r, somme Sₙ) ;
- **opérations sur les suites** (somme, produit, quotient) en encadré ;
- tableau des **théorèmes de comparaison** à 5 lignes (minoration, majoration, encadrement, |xₙ − ℓ| ≤ uₙ,
  passage à la limite dans une inégalité) ;
- **Théorème 2** du IV : continuité en ℓ ⇒ f(uₙ) → f(ℓ), et pour uₙ₊₁ = f(uₙ) avec f(I) ⊂ I : f(ℓ) = ℓ ;
- rubriques **« Apprendre à chercher »** (produit de cordes dans un demi-cercle, inégalité de Wallis-type,
  aire sous x² par rectangles = 1/3, Σ 1/k² ≤ 2), **« Avec l'outil informatique »** (Syracuse au tableur,
  formule SI/MOD) et **« Maths et culture »** (Farey, cercles de Ford) — coloration « informatique » de la
  section ;
- nombres « culturels » : Erdös (juxtaposition des premiers), Apéry ζ(3) ≈ 1,202056903159594…,
  Champernowne, le nombre 0,999… (Ex. 23) ;
- **série harmonique divergente** (Ex. 24), factorielles (Ex. 25), récurrence linéaire d'ordre 2
  uₙ₊₂ = 6uₙ₊₁ − 5uₙ via l'équation caractéristique x² = 6x − 5 (Ex. 19), constructions géométriques itérées
  (Ex. 12–15), barycentres (Ex. 22), limite d'un produit télescopique (Ex. 10, Situation 1) ;
- erreur de calcul sur une série divergente (Ex. 7, « x = −4 ») et comportement « anormal » de la
  calculatrice (Ex. 20 : √(n² + 6n) − n pour n jusqu'à 10¹⁵).
- **Vocabulaire / notations** : « IN », « IR » ; « A retenir », « Applications » ; « tend vers ℓ quand n tend
  vers +∞ » ; écriture uₙ.vₙ ; « case barrée » = pas de conclusion (forme indéterminée, le mot
  « indéterminée » n'apparaît pas).

### Bornes de scope (chapitre 1)

- ✅ INCLUS : raisonnement par récurrence ; suites arithmétiques/géométriques, sommes de termes ; opérations
  sur les suites ; monotonie (différence, quotient, fonction uₙ = f(n), récurrence) ; suites majorées,
  minorées, bornées ; limite finie (définition ε) et infinie (définition A), unicité, divergence ; limite de
  qⁿ ; opérations sur les limites (tableaux) et cas où l'on ne peut pas conclure ; théorèmes de comparaison et
  d'encadrement, passage à la limite dans une inégalité ; convergence des suites monotones bornées (admis),
  croissante non majorée → +∞ ; uₙ = f(n) ; f(uₙ) (composition) ; suites récurrentes uₙ₊₁ = f(uₙ),
  représentation graphique en escalier/escargot, point fixe f(ℓ) = ℓ ; suites auxiliaires géométriques ou
  arithmétiques (homographiques) ; sommes télescopiques, Σ 1/k², Σ 1/k³ majorées, série harmonique
  divergente ; récurrence linéaire d'ordre 2 (Ex. 19) ; algorithme/tableur (Syracuse) ; suites de Farey
  (culture).
- ⛔ EXCLU (non traité dans ces pages) : suites adjacentes (nom et théorème) ; sous-suites paire/impaire ;
  suites d'intégrales ; lien avec ln/exp (chapitres 6–7) ; « toute suite convergente est bornée » (non énoncé).

### Lecture

- **Pages lues en L1 (pdftotext)** : p.5 à p.25, toutes.
- **Pages lues sur l'image (110 dpi)** : p.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24, 25 = **21 / 21 (100 %)** ; p.12 relue à 220 dpi (dernière ligne du tableau de comparaison).
- **Écarts texte / image constatés** : L1 perd les signes « − », « ≤/≥ », « ∈ », « → », « ≠ » (p.6 Act. prél.
  1 « 2uₙ 3 » pour 2uₙ − 3 ; p.6 Act. prél. 3 b) « 3n 2 » pour 3ⁿ⁻² ; p.7 « x 8 0,75x + 21 » pour
  x ↦ −0,75x + 21) ; tous les tableaux de p.12 illisibles en L1 ; les exposants (2²ⁿ⁺¹ × 5³⁻ⁿ, 10⁻ⁿ⁻¹,
  0,95ⁿ⁻¹⁶) et racines (Ex. 18) reconstruits sur image ; le « 1) » de l'Ex. 16 est déplacé en L1 comme sur
  l'image (mise en page). **Toute formule de cette section vient de l'image.**
- **Coquilles [sic]** : Déf. 1 p.9 « Pour réel ε > 0 » (sans « tout ») ; Remarque p.14 « (vₙ) … lim uₙ » ;
  III Act. 2 « n ≥ I » ; tableau de comparaison p.12 « lim xₙ = ℓ et » sans lim yₙ = ℓ′ ; Ex. 4 4)a)
  « uₙ = √(uₙ + 2) » pour uₙ₊₁ ; Ex. 20 « lim_{x→+∞} uₙ » ; Farey p.25 « trois fractions successives de, » ;
  Ex. 13 « cos 60° » imprimé avec un glyphe parasite (« 60ϒ » en L1) ; « considére », « repére »,
  « Détérminer », « Considèrons » (accents) ; Syracuse : « la suite obtenue est-elle finie ? » (pour
  « atteint-elle 1 ») ; I Act. 6 « pour tout intervalle I contenant 2 » (sans « ouvert »).
- **Doutes [?]** : (1) III Act. 1 : la somme imprimée « 3 Σ_{i=1}^{n} 10⁻ⁿ » a l'indice n au lieu de i ;
  noté tel quel ; (2) Situation 1 : B₁B = 1/2 et BₙB = 1/n sont incompatibles (B₁B = 1/2 suggère
  BₖB = 1/(k + 1)) et le produit de Pythagore s'arrête à (1 − 1/n²) ; noté tel quel ; (3) II Act. 3 2)
  « vₙ < √n » pour vₙ = (−1 − n)/√n est vraie mais ne permet pas la conjecture de −∞ (sans doute
  « vₙ < −√n ») ; noté tel quel ; (4) IV App. 1 : « les 4 premiers termes » annoncés, seuls u₀ et u₁ figurent
  sur le graphique ; u₀ non donné numériquement ; (5) Théorème 2 p.15, 2ᵉ puce : la conclusion imprimée porte
  sur « (f(uₙ)) converge vers f(ℓ) et f(ℓ) = ℓ » (hypothèse lim uₙ = ℓ reprise de la phrase d'en-tête).
## 2.2 Chapitre 2 — Limites de fonctions (manuel 222472, p.26–46)

**Page de garde (p.26)** — « Chapitre 2 », titre « LIMITES DE FONCTIONS ». Plan imprimé : « I . Généralités
sur les fonctions. · II . Limite d'une fonction. · III . Limites et droites asymptotes. · IV . Limites par
comparaison. » Portrait légendé : « Augustin Cauchy (1789- 1857) La définition actuelle de la limite d'une
fonction en un point lui doit beaucoup ». Pas de citation liminaire.

**Plan du chapitre**

- **I. Généralités sur les fonctions** (p.27–29) : Activités préliminaires 1–3 (p.27) · Activités de
  découverte 1–4 (p.27–28) · « A retenir » (p.28–29 : composée de deux fonctions, sens de variation d'une
  composée, fonctions associées) · « Applications » 1–6 (p.29).
- **II. Limite d'une fonction** (p.30–34) : Activités préliminaires 1–4 (p.30) · Activités de découverte 1–2
  (p.30–31) · « A retenir » (p.31–33 : limite finie en a, à droite, à gauche ; théorèmes ; limite en ±∞ ;
  opérations ; formes indéterminées ; limite d'une composée) · « Applications » 1–5 (p.33–34).
- **III. Limites et droites asymptotes** (p.35–38) : Activités préliminaires 1–2 (p.35) · Activités de
  découverte 1–2 (p.35) · « A retenir » (p.36–37 : asymptotes verticale, horizontale, oblique) · « Méthode »
  (p.37) · « Applications » 1 (p.38, deux volets ; le second est sans doute l'Application 2, dont le « 2 » a
  glissé devant le titre « IV. »).
- **IV. Limites par comparaison** (p.38–39) : Activités de découverte 1–4 (p.38) · « A retenir » (p.39 :
  Théorème 1, Théorème 2, Conséquence) · « Applications » 1–5 (p.39).
- **Apprendre à chercher** (p.40) : Situations 1–3 (expression conjuguée, asymptotes obliques).
- **Avec l'outil informatique** (p.41) : « Fonction composée et limites sous GEOPLAN ».
- **Exercices et problèmes** (p.42–45) : 20 exercices.
- **Maths et culture** (p.46) : « L'asymptote : une notion en évolution » (Montaigne, Jacques Peletier).

Pas d'exercice résolu, pas de page de synthèse de fin de chapitre, pas de QCM/Vrai-Faux de fin de chapitre (un
QCM ouvre les Exercices, Ex. 1, et des QCM sont dans les Applications du II). Mise en page fautive p.38 : le
numéro « 2 » d'application est imprimé devant le titre « IV. Limites par comparaison. » et « Activité 1: »
précède le sous-titre « Activités de découverte » (voir Lecture).

### Cours — Activités (une ligne chacune)

**I. Généralités sur les fonctions — Activités préliminaires** (p.27)

- **Act. prél. 1** (p.27) : figure : courbes de x ↦ x ; x ↦ x² ; x ↦ 1/x ; x ↦ √x. 1) indiquer la courbe de
  chacune ; 2) comparer ces fonctions ; 3) pour x ≥ 0, démontrer que la courbe de f(x) = x² est symétrique de
  celle de g(x) = √x par rapport à Δ : y = x ; 4) autres éléments de symétrie ?
- **Act. prél. 2** (p.27) : QCM (une seule bonne réponse) : 1) f(x) = x⁵(x − 1)³ sur IR : paire / impaire / ni
  paire ni impaire ; 2) g(x) = (3x + 4)/(2x + 1) sur IR ∖ {−1/2} : croissante / décroissante / ni croissante ni
  décroissante ; 3) ensemble des solutions de f(x) = 0 : {−1;0} / [−1;0] / {0;1} / [0;1].
- **Act. prél. 3** (p.27) : courbe d'une fonction f définie sur [−2;1]. 1) tableau de variation ; 2) lire
  f(−1), f(0), f(1/2) ; 3) résoudre graphiquement f(x) = −1 ; f(x) = x.

**I. — Activités de découverte** (p.27–28)

- **Act. 1** (p.27) : f, g : {0;1;2;…;10} → IR données par un tableau (x : 0…10 ; f(x) : 0 2 3 5 7 10 3 4 7 5 3 ;
  g(x) : 0 1 1 2 3 1 4 2 5 3 8) ; compléter les lignes f(g(x)) et g(f(x)).
- **Act. 2** (p.28) : f et g définies sur [−3;4] représentées (lignes brisées C_f, C_g) ; représenter −f ; 3f ;
  f + g ; f − g.
- **Act. 3** (p.28) : fonction f définie sur [−3;4] (ligne brisée) ; pour f₁(x) = −f(x), f₂(x) = f(−x),
  f₃(x) = −f(−x), f₄(x) = |f(x)|, f₅(x) = f(x + 2), f₆(x) = f(x) + 1, f₇(x) = 3f(x), f₈(x) = f(2x) : 1) ensemble
  de définition ; 2) représentation graphique.
- **Act. 4** (p.28) : tableaux de variation de f (−∞ : +∞ ↘ −1/2 en 0 ↗ +∞) et de g (croissante de −∞ à +∞,
  g(−1/2) = 0) sur IR ; en déduire le tableau de variations de f∘g sur IR.

**II. Limite d'une fonction — Activités préliminaires** (p.30)

- **Act. prél. 1** (p.30) : 1) limites en +∞ de x ↦ √x ; x ; x² ; xⁿ (n ∈ IN*) ; 2) limites en +∞ de 1/√x ;
  1/x ; 1/x² ; 1/xⁿ (n ∈ IN*) ; 3) exemple de fonction sans limite en +∞.
- **Act. prél. 2** (p.30) : limite de f : a) 8x³ + 2x² + 1 en +∞ ; −∞ et 0 ; b) (x² − 1)/(x − 1) en +∞ ; −∞ et 1.
- **Act. prél. 3** (p.30) : limites (justifier) : a) lim_{+∞} (1/x + 2x + 3) ; b) lim_{+∞} (3√x + x²) ;
  c) lim_{−∞} (−5/x + x²) ; d) lim_{0⁺} (1/x + 3x² − 2) ; e) lim_{2⁺} (3/(x − 2) + 5x + 7) ;
  f) lim_{2⁺} (2/(x + 2) + 1/2).
- **Act. prél. 4** (p.30) : tracer une courbe vérifiant : 1) f définie sur ]−1;+∞[, lim_{+∞} f = 0,
  lim_{−1⁺} f = +∞, f(0) = −3 ; 2) f définie sur [0;3[ et ]3;+∞[, f(0) = 2, lim_{3⁻} f = −∞, lim_{3⁺} f = +∞,
  lim_{+∞} f = 0.

**II. — Activités de découverte** (p.30–31)

- **Act. 1** (p.30–31) : 1) les théorèmes vus permettent-ils de calculer lim_{+∞} (x − √x) ? montrer que pour
  x > 0, x − √x = x(1 − 1/√x), en déduire la limite ; 2) limite éventuelle de f(x) au point a après
  simplification : a) (3x² − 8x³)/x², a = 0 ; b) (x² + 5x + 6)/(x + 2), a = −2 ; c) (√(x² + 1) − 1)/x, a = 0 ;
  d) √x/(x + 3√x), a = 0 ; e) (x³ − 27)/(x − 3), a = 3 ; f) x − √(x² + 1), a = +∞.
- **Act. 2** (p.31) : 1) écrire u : x ↦ √(1 + x + x²) sous la forme g∘f, en déduire lim_{+∞} u(x) ; 2) limite
  éventuelle : a) √((x + 3)/(x − 1)) en +∞ ; b) sin(1/√x) en +∞ ; 3) a, b, l réels ou ±∞ : si lim_{x→a} f(x) = b
  et lim_{y→b} g(y) = l, conjecture sur lim_{x→a} g∘f(x) ?

**III. Limites et droites asymptotes — Activités préliminaires** (p.35)

- **Act. prél. 1** (p.35) : 1) réduire au même dénominateur (valeurs interdites) : a) 2 − 3/x + 1/x² ;
  b) (2x − 1)/x² + x − 1 ; c) x − 3 + 4/(x² − 1) ; d) 1/(x − 1) − 2/(x + 2) + 1 ; 2) a, b, c tels que pour
  x ∈ IR ∖ {2}, (4x² − 9x)/(x − 2) = ax + b + c/(x − 2) ; 3) f(x) = (−x³ + 3x² − x − 1)/(x² + 1) sur IR :
  a, b, c tels que f(x) = ax + b + c/(x² + 1).
- **Act. prél. 2** (p.35) : trois courbes ①②③ (avec asymptotes en traits fins) ; 1) lire l'ensemble de
  définition et le tableau de variation de chaque fonction ; 2) compléter le tableau par les limites aux bornes.

**III. — Activités de découverte** (p.35)

- **Act. 1** (p.35) : tableau de variations de f (x : −∞, 0, 2, +∞ ; f : −3 ↗ −1 en 0 ↘ −∞ en 2⁻ ‖ −∞ ↗ 0 en
  +∞) ; interpréter graphiquement chaque limite et tracer une allure possible de la courbe.
- **Act. 2** (p.35) : f(x) = (−x³ + 2x² − x − 2)/(x² − 1) sur ]1;+∞[, D : y = −x + 2, C la courbe. 1) calculer
  lim_{+∞} (f(x) + x − 2), interprétation graphique ; 2) position relative de C et D sur ]1;+∞[ ; 3) limite de
  f en 1, interprétation graphique.

**IV. Limites par comparaison — Activités de découverte** (p.38)

- **Act. 1** (p.38) : g(x) = √(1 + x²)/x² ; démontrer g(x) ≥ 1/x² pour tout réel x [non nul] ; peut-on calculer
  la limite de g en 0 ?
- **Act. 2** (p.38) : f croissante sur I = [a;b] : montrer f(a) ≤ f(x) ≤ f(b) ; en déduire que f est bornée.
- **Act. 3** (p.38) : f, u, v définies sur [a;+∞[ : 1) si f(x) ≥ u(x) pour x assez grand et lim_{+∞} u = +∞,
  alors lim_{+∞} f = +∞ ; 2) si f(x) ≤ v(x) pour x assez grand et lim_{+∞} v = −∞, alors lim_{+∞} f = −∞.
- **Act. 4** (p.38) : f, u sur [a;+∞[ : si |f(x) − ℓ| ≤ u(x) pour x assez grand et lim_{+∞} u = 0, alors
  lim_{+∞} f = ℓ.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Composée de deux fonctions — Définition** (p.28) — « Soit f une fonction dont l'ensemble de
> définition est D et g une fonction dont l'ensemble de définition est f(D). On appelle fonction composée de f
> et g, la fonction notée g o f et définie pour tout x ∈ D , par : ( gof ) (x) = g ( f ( x)) »
> **Remarque :** « fog est généralement différente de gof . »

> **Sens de variation d'une composée** (p.28) — « Soit f une fonction définie sur un intervalle I et g une
> fonction définie sur l'ensemble f (I) = {f(x), où x ∈ I }. **Théorème** Si f et g ont même sens de variation,
> alors gof est croissante sur I. Si f et g ont des sens de variation contraires, alors gof est décroissante
> sur I. »

> **Fonctions associées — Théorème admis** (p.28–29) — « Soit C_f la représentation graphique d'une fonction f
> dans un repère orthogonal (O; i⃗, j⃗) • La courbe C_g représentant la fonction g définie par g(x) = f(x) + k ,
> k réel, est l'image de C_f par t_{kj⃗}. • La courbe C_h représentant la fonction h définie par
> h(x) = f(x + λ) , λ réel, est l'image de C_f par t_{−λi⃗}. • La courbe C_k représentant la fonction k définie
> par k(x) = − f(x) est l'image de C_f par la symétrie par rapport à l'axe des abscisses. • La courbe C_l
> représentant la fonction l définie par l(x) = f(−x) est l'image de C_f par la symétrie par rapport à l'axe
> des ordonnées. »

> **A retenir — Limite finie en a (a réel) — Définitions** (p.31) — « 1) Considérons une fonction définie sur
> un intervalle ouvert contenant a (sauf peut - être en a) et L un réel. Une fonction f a pour limite L
> lorsque x tend vers a, si pour tout intervalle ouvert J contenant L , il existe un intervalle ouvert I
> contenant a tel que si x ∈ I ∖ {a} , f(x) ∈ J. On note lim_{x→a} f(x) = L ou lim_a f = L
> 2) Considérons une fonction définie sur un intervalle ouvert de la forme ]a,b[ et L un réel. Une fonction f
> a pour limite L à droite en a si pour tout intervalle ouvert J contenant L, il existe un réel α > a tel que
> si x ∈ ]a,α[, f(x) ∈ J On note lim_{x→a⁺} f(x) = L ou lim_{a⁺} f = L
> 3) Considérons une fonctions définie sur un intervalle ouvert de la forme ]b,a[ et L un réel. Une fonction f
> a pour limite L à gauche en a si pour tout intervalle ouvert J contenant L, il existe un réel α < a tel que
> si x ∈ ]α,a[, f(x) ∈ J. On note lim_{x→a⁻} f(x) = L ou lim_{a⁻} f = L » (figure : courbe C, bandes J autour
> de L et I autour de a.)
> **Remarques** — « • Si une fonction admet une limite en a, cette limite est unique • ( lim_{x→a⁺} f(x) =
> lim_{x→a⁻} f(x) = L) ⇔ (lim_{x→a} f(x) = L) »

> **Théorème** (p.32) — « 1) f étant une fonction polynôme ou l'une des fonctions x ↦ √x , x ↦ cos x ,
> x ↦ sin x , ou encore la somme, le produit, le quotient ou la valeur absolue de telles fonctions, si f est
> définie en a , alors lim_{x→a} f(x) = f(a) où a est un réel . 2) Si, pour x ≠ a, f (x) = g(x), où g est une
> fonction définie en a et telle que lim_{x→a} g(x) = g(a) alors f admet une limite en a, et
> lim_{x→a} f(x) = g(a). »

> **Limite en +∞ ou −∞ — Théorème** (p.32) — « A l'infini, une fonction polynôme a même limite que son terme du
> plus haut degré. A l'infini, une fonction rationnelle a même limite que le quotient simplifié de ses termes
> du plus haut degré. »

> **Opérations sur les limites** (p.32) — « Nous rappelons ci-dessous les résultats algébriques qui nous
> renseignent, dans certains cas, sur la limite d'une somme, d'un produit ou d'un quotient. Dans chaque cas, il
> s'agit de limites au même point a (a réel ou +∞ ou −∞ ). »
> **Théorème 1) Limite d'une somme** — « Les fonctions f et g ayant une limite (finie ou infinie) en a , la
> fonction f + g admet une limite dans chacun des cas décrits par le tableau ci-contre. » Tableau (lignes
> lim_a f, colonnes lim_a g) : ℓ : ℓ′ → ℓ + ℓ′ ; +∞ → +∞ ; −∞ → −∞ · +∞ : ℓ′ → +∞ ; +∞ → +∞ ; −∞ → ? ·
> −∞ : ℓ′ → −∞ ; +∞ → ? ; −∞ → −∞.
> **2) Limite d'un produit** — « Les fonctions f et g ayant une limite (finie ou infinie) en a , la fonction f.g
> admet une limite dans chacun des cas décrits par le tableau ci-contre. » Tableau : ℓ ≠ 0 : ℓ′ ≠ 0 → ℓℓ′ ;
> +∞ → ±∞ ; −∞ → ±∞ · +∞ : ℓ′ ≠ 0 → ±∞ ; +∞ → +∞ ; −∞ → −∞ · −∞ : ℓ′ ≠ 0 → ±∞ ; +∞ → −∞ ; −∞ → +∞.
> **Remarque** — « Si lim_{x→a} f(x) = 0 et lim_{x→a} g(x) = ±∞ on ne peut conclure. »
> **3) Limite d'un quotient** (p.33) — « Les fonctions f et g ayant une limite (finie ou infinie) en a, la
> fonction f/g admet une limite dans chacun des cas décrits par le tableau ci-contre. » Tableau : ℓ : ℓ′ ≠ 0 →
> ℓ/ℓ′ ; +∞ → 0 ; −∞ → 0 · +∞ : ℓ′ ≠ 0 → ±∞ ; +∞ → ? ; −∞ → ? · −∞ : ℓ′ ≠ 0 → ±∞ ; +∞ → ? ; −∞ → ?.
> **Remarque** — « Si ℓ′ = 0 , on ne peut conclure que lorsque g garde un signe constant au voisinage de a.
> Les situations marquées ? sont appelées formes indéterminées. »

> **Limite d'une fonction composée : Théorème** (p.33) — « a, b, l sont chacun un réel ou l'un des symboles +∞
> ou −∞ Si lim_{x→a} f(x) = b et lim_{y→b} g(y) = l , alors lim_{x→a} gof(x) = l »

> **A retenir — Asymptote verticale** (p.36) — « Soit f une fonction définie sur un intervalle ouvert de borne a
> et C sa courbe représentative. **Définition** Si lim_{x→a⁺} f(x) = ±∞ ou lim_{x→a⁻} f(x) = ±∞ alors la droite
> d'équation x = a est une asymptote verticale pour la courbe C » (quatre vignettes : « Si lim_{a⁺} f = +∞ »,
> « Si lim_{a⁺} f = −∞ », « Si lim_{a⁻} f = +∞ », « Si lim_{a⁻} f = −∞ ».)

> **Asymptote horizontale** (p.36) — « Soit f une fonction définie sur un intervalle de borne +∞ ou −∞ et C sa
> courbe représentative. **Définition :** Si la limite de f(x) est un nombre L, quand x tend vers +∞, (ou −∞),
> alors la droite d'équation y = L est asymptote horizontale à C en +∞ ( ou −∞ ) » (deux vignettes.)

> **Asymptote oblique** (p.37) — « Soit f une fonction définie sur un intervalle de borne +∞ ou −∞ , C sa
> courbe représentative et D une droite d'équation y = ax + b dans un repère ( a ≠ 0 ) **Définition :** Si la
> limite de la différence f(x)-(ax+b) est nulle quand x tend vers +∞(ou −∞ ) alors la droite d'équation
> y = ax + b est asymptote oblique à C en +∞ (ou −∞). » (quatre vignettes, droite (Δ) : y = ax + b.)

> **Méthode** (p.37, hors encadré) — « 1) Pour avoir une asymptote verticale, la valeur interdite ne suffit
> pas : il faut aussi que, en cette valeur, la limite à droite ou à gauche soit infinie. 2) a- Pour montrer
> qu'une droite donnée d'équation y = ax+b (avec a ≠ 0 ) est asymptote oblique ; on calcule la différence
> d(x) = f(x) - (ax + b); on étudie la limite à l'infini de d(x) et on doit trouver 0. b- Pour étudier la
> position relative de C et de D, on étudie le signe de d(x) . »

> **A retenir — Théorème 1** (p.39) — « Soient f et g deux fonctions définies sur le même intervalle I. Si
> lim_{x→a} g(x) = +∞ et si pour tout x ∈ I, f(x) ≥ g(x) alors lim_{x→a} f(x) = +∞ »
> **Théorème 2** — « Soient f, u et v des fonctions admettant des limites en un réel a . Si pour tout réel x
> assez proche de a , on a : u(x) ≤ f(x) ≤ v(x) et si lim_{x→a} u(x) = lim_{x→a} v(x) = ℓ alors la fonction f
> admet une limite en a et lim_{x→a} f(x) = ℓ »
> **Conséquence** — « Soient f et g deux fonctions définies sur le même intervalle I. Si lim_{x→a} g(x) = 0 et
> si pour tout x ∈ I, |f(x) − ℓ| ≤ g(x) alors lim_{x→a} f(x) = ℓ Ces résultats s'étendent aux limites en −∞ ,
> +∞ , a⁺ et a⁻ »

### Applications (exercices d'application intégrés au cours)

**Applications du I** (p.29)

- **1** : f₁(x) = x² − 1 (imprimé « f₁ = x² - 1 ») et f₂(x) = √x. 1) domaines ; 2) a) calculer si possible
  f₁∘f₂(3), f₂∘f₁(3), f₁∘f₂(0), f₂∘f₁(0), f₁∘f₂(−2), f₂∘f₁(−2) ; b) les domaines de f₁∘f₂ et f₂∘f₁
  peuvent-ils être identiques ? 3) domaines et expressions de f₁∘f₂ et f₂∘f₁.
- **2** : démontrer que la composée de deux fonctions affines est affine.
- **3** : écrire f comme composée de deux fonctions connues et en déduire son sens de variation : a) f(x) =
  1/(x² + 1) sur IR ; b) f(x) = √(4 − x²) sur [−2;2].
- **4** : f(x) = (3x − 1)/(x − 1) sur IR ∖ {1} ; vérifier f(x) = 3 + 2/(x − 1) ; tableau de variation ; préciser
  la transformation utilisée.
- **5** : f(x) = 2x² − 1 et g(x) = 4x³ − 3x sur IR ; vérifier (fog)(x) = (gof)(x).
- **6** : f(x) = √x (x ∈ IR₊), C_f ; représenter dans le même repère g(x) = √x + 3 ; h(x) = √(x − 2) ;
  k(x) = √(−x).

**Applications du II** (p.33–34)

- **1** (p.33) : « Cocher la seule bonne réponse » : a) lim_{+∞} (x − 3 − 1/x) = +∞ / 0 / −∞ ; b) lim_{0⁻}
  (−x + 4 + 2/x) : +∞ / 0 / −∞ ; c) lim_{3⁺} (2x − 7)/(x − 3) : +∞ / 0 / −∞ / 2.
- **2** (p.33) : lim_{+∞} f = 0 avec f(x) > 0, lim_{+∞} g = −∞ et lim_{+∞} h = −2. a) lim (f + g) ; b) lim f × g ;
  c) lim h × g ; d) lim h/f — choix parmi +∞ / −∞ / 0 (ou 2, −2) / « on peut pas le savoir » [sic].
- **3** (p.34) : « Trouver toutes les bonnes réponses. » u et g données par tableaux (u : +∞ ↘ 3 en −2 ↘ −1 en
  5 ↗ 2 en +∞ ; g : tableau à abscisses imprimées −∞, −2, 5, 2, 3, +∞, voir doutes) ; f = g∘u : f(−2) = 0 ;
  f(−2) = 1 ; f(5) = −1 ; f(2) = 0 ; lim_{+∞} f = 0 ; lim_{−∞} f = −∞ ; lim_{5⁺} f = +∞. (Phrase parasite
  imprimée : « Soit la fonction u dont le tableau des variations est donnée ci-dessous. »)
- **4** (p.34) : tableau de u (x : −∞, 0, 2, 3, +∞ ; u : 4 ↘ 1 en 0 ↗ +∞ en 2⁻ ‖ +∞ ↘ 0 en 3 ↘ −2) ; tableau des
  variations complet de 1/u ; pourquoi le point E(2;0) est-il exclu de la courbe de 1/u ?
- **5** (p.34) : u définie sur [0;6], courbe C_u (minimum 0,5 pour x = 3). 1) tableau de variation de u ; 2) sens de variation et tableau de f = g∘u, g : x ↦ 1/x.

**Applications du III** (p.38)

- **1** : [a)] tableau de variations (x : −∞, 1, +∞ ; f : 0 ↘ −∞ en 1⁻ ‖ 0 ↘ −1 ↗ 2) : interpréter chaque limite et
  tracer une allure ; [b), lecture probable : Application 2, numéro « 2 » imprimé devant le titre « IV. »]
  f(x) = (−x² + 2x + 7)/(x + 1) sur ]−1;+∞[, D : y = −x + 3 : 1) D asymptote à C en +∞ ; 2) position relative de C et D.

**Applications du IV** (p.39)

- **1** : h(x) = √(1 + x) − √x. 1) pour x > 0, h(x) = √x(√(1/x + 1) − 1) ; en déduire lim_{+∞} h ? 2) vérifier,
  pour x ∈ IR*₊ : 0 < h(x) < √(x + 1) ; h(x) = 1/(√(x + 1) + √x) ; 0 < h(x) < 1/√x ; lesquelles permettent de
  déterminer lim_{+∞} h ; la déterminer.
- **2** : limites en +∞ et −∞ de f(x) = x + sin x sur IR.
- **3** : limite en 0 de f(x) = x sin(1/x) sur IR*₊.
- **4** : sur ]0;+∞[, (3x + 4)/(x + 2) ≤ f(x) < 3 + 1/x ; limite de f en +∞.
- **5** : « Corriger les réponses fausses. » h et g données par leurs courbes C et C′ (figure) : a) f ≤ h sur
  ]0;+∞[ ⇒ lim_{+∞} f = −∞ ; b) f ≤ g sur ]0;+∞[ ⇒ lim_{0⁺} f = −∞ ; c) f ≥ g sur ]−∞;0[ ⇒ lim_{−∞} f = +∞ ;
  d) g ≤ f ≤ h sur ]−∞;0[ ⇒ lim_{−∞} f = 0 ; e) f ≥ g sur ]0;+∞[ ⇒ lim_{+∞} f = +∞.

### Apprendre à chercher (p.40)

- **Situation 1** : limite en +∞ et en −∞ de f : x ↦ √(x² + x) − x. **Point méthode** : « Dans le cas de telles
  fonctions, il est parfois efficace d'utiliser la technique de multiplication par l'expression conjuguée,
  lorsque les théorèmes usuels ne permettent pas de conclure directement ». Vérifier, pour x > 0,
  f(x) = x/(√(x² + x) + x) puis f(x) = 1/(√(1 + 1/x) + 1) ; en déduire lim_{+∞} f et l'interpréter ; en −∞ :
  lim f = +∞ ; f(x) + 2x = x/(√(x² + x) − x) ; achever et trouver l'asymptote en −∞.
- **Situation 2** : f(x) = √(2x² + x + 1) sur IR ; démontrer que C admet une asymptote oblique en +∞. Idée
  imprimée : « si , f(x) = √(2x² + 1) intuitivement, « pour les grandes valeurs de x, f(x) se comporte comme
  √(2x²) = (√2)x et donc y = √2x est asymptote ». prouvez-le » ; écrire f sous la forme √(aX² + b) : forme
  canonique, f(x) = √(2(x + 1/4)² + 7/8) ; prouver que y = √2(x + 1/4) est asymptote à C.
- **Situation 3** : f(x) = (√(x + 1) − 2)/(√(2x + 19) − 5). 1) domaine D ; 2) limite en 3, conclure. **Vers une
  solution** : montrer f(x) = (√(2x + 19) + 5)/(2(√(x + 1) + 2)) « (on multiplie le numérateur et le
  dénominateur de f(x) par l'expression conjuguée √(x + 1) − 2 puis par l'expression conjuguée (√(2x + 19) − 5) »
  (sic, voir doutes).

### Avec l'outil informatique (p.41) — « Fonction composée et limites sous GEOPLAN »

u(x) = −3/x + 3 sur ]0;+∞[ (courbe C_u) ; « Travail sur papier » : g(x) = 4 − x² sur IR (C_g), f = g∘u ; sans
calculer f(x), sens de variation de f sur ]0;+∞] [sic] par les fonctions composées. « Création et interprétation
de la figure sous GEOPLAN » : a) créer u, g, C_u, C_g et les points A, B, M dans le repère Roxy ; b) déplacer M
(« Piloter » › « Piloter au clavier », x réel de [0;10]) ; vérifier que la composée est bien définie sur ]0;3] ;
c) position de A pour x = 3 ; coordonnées de A, B, M pour x = 1 puis x = 2 ; d) quand x est proche de 0,
ordonnées de A, B, M ? « Pour aller plus loin » : modifier u (u(x) = 11 − x²), bornes du tracé [−10 ; 10] ;
a) par lecture graphique, tableau complet des variations de g∘u ; b) démontrer tous les éléments du tableau.
(Captures d'écran : fenêtre « Objets de la figure » — A (x, u(x)), B (u(x), g(u(x))), M (x, g(u(x))), etc. ;
boîtes « Modifier/Dupliquer un objet », « Bornes (ex: -5 2/3) ».)

### Exercices et problèmes (p.42–45) — 20 exercices

- **Ex. 1** (p.42) : **Q.C.M.** « Trouver toutes les bonnes réponses. » f définie sur IR ∖ {2}, tableau (x : −∞,
  −1, 1, 2, +∞ ; f : +∞ ↘ −2 ↗ 0 (en 1) ↗ +∞ en 2⁻ ‖ −∞ ↗ 0). a) pour x ∈ ]−∞;2[, f(x) ≥ −2 ; b) dans [−1;1],
  f(x) = −1 admet une unique solution ; c) f(0) > 0 ; f(5) < 0 ; d) x = 0 asymptote à C ; e) lim_{−∞} √f(x) = +∞ ;
  f) lim_{+∞} 1/f(x) = −∞ ; g) lim_{x→2} f(x) = +∞ ; h) lim_{x→1, x>1} 1/f(x) = +∞.
- **Ex. 2** (p.42) : f, g croissantes sur [−1;1] : 1) f + g croissante ? 2) f × g croissante ? (démontrer ou
  contre-exemple).
- **Ex. 3** (p.42) : f croissante et g décroissante sur IR : sens de variation de a) g∘f ; b) f × g ? (énoncer
  et démontrer, ou contre-exemple).
- **Ex. 4** (p.42) : f₀(x) = 1 − 1/x pour x ∈ IR − {0;1} et fₙ(x) = f₀[fₙ₋₁(x)] pour n ∈ {1;2;3;4…} ;
  calculer f₂₀₀₇(2007).
- **Ex. 5** (p.42) : courbes de f(x) = 1 + x² et g(x) = √x et de leur composée h (C_f, C_g, C_h) ; reconnaître h
  et son sens de variation.
- **Ex. 6** (p.42) : courbe 𝒞 d'une fonction f sur ]−3;+∞[ (point A, droite horizontale) ; tableau de variations.
- **Ex. 7** (p.42–43) : f, g, h données par leurs courbes 𝒞_F, 𝒞_G, 𝒞_H. 1) limites de f, g, h en +∞ ; 2) si
  possible, limites en +∞ de f + g ; f + h ; g + h ; f × g ; f × h ; g × h ; 3) limites en −∞ de f + g ; g + h ;
  f × g ; f × h ; g × h ; 4) limites en +∞ et −∞ de f/g ; h/g ; f/h ; 3 + 1/f ; 2h − 1/g.
- **Ex. 8** (p.43) : limites : a) √x − √(x + 1) en +∞ ; b) x/(√(x + 9) − 3) en 0 ; c) √(x² + x + 1) − x en +∞.
- **Ex. 9** (p.43) : u et g représentées par C_u et C_g. 1) tableaux de variations de u et g ; 2) a) justifier que
  f = g∘u est définie sur ]−∞;3[ ∪ ]5;+∞[ ; b) sens de variation de f ; c) (g∘u)(2) et (g∘u)(0) ; 3) a) lire
  lim_{+∞} u et lim_0 g ; lim_{3⁻} u et lim_{−2} g ; lim_{5⁺} u et lim_{−2} g ; lim_{−∞} u et lim_{+∞} g ;
  b) que prévoir pour les limites de f ?
- **Ex. 10** (p.43) : limites en +∞ : a) 2x − 5x³ ; b) (3 + 2x)/(x² − 3) ; c) (x³ − x + 1)/(8x² − 1) ;
  d) (√x + 2x)/(1 − 5x).
- **Ex. 11** (p.43–44) : u donnée par la courbe 𝒞. 1) a) résoudre u(x) = −x + 4 ; b) u(x) < 0 ; c) tableau de
  variations et signe de u(x) ; 2) g donnée par son tableau (t : −∞, −1, 3, +∞ ; g : 3 ↘ 2 ↘ 0 ↗ +∞) : sens de
  variation de f = g∘u définie sur ]−∞;5[.
- **Ex. 12** (p.44) : f(x) = ((50 + x²⁰)² − 2500)/x²⁰. a) à la calculatrice, (50 + x²⁰)² puis f(x) pour x = 0,6 ;
  0,5 ; 0,4 ; 0,3 ; 0,2 ; 0,1 et 0,01 ; conjecture sur la limite en 0 ; b) en développant, simplifier f(x)
  (x ≠ 0), limite en 0 ; c) « Vaincre la tentation de se débarrasser de la calculatrice. »
- **Ex. 13** (p.44) : f(x) = (−x² + 3x)/(x − 2) sur ]2;+∞[. a) limite en +∞ ; b) a, b, c tels que
  f(x) = ax + b + c/(x − 2) ; D : y = −x + 1 asymptote oblique en +∞ ; c) limite en 2, interprétation.
- **Ex. 14** (p.44) : allure d'une courbe C de f définie sur IR ∖ {2} telle que : a) asymptote verticale x = 2 ;
  b) asymptote horizontale y = 3 en +∞ ; c) asymptote horizontale y = −1 en −∞ ; d) f croissante sur ]−∞;2[ et
  sur ]2;+∞[ ; e) f(x) = 0 a pour ensemble de solutions {0;5}.
- **Ex. 15** (p.44) : f(x) = a + (bx + c)/(x² + 4) sur IR ; C passe par A(0;−1) et B(1;1) ; en A, tangente
  parallèle à y = −x. 1) a, b, c ; 2) limites en +∞ et −∞, interprétation ; 3) résoudre f(x) = 0.
- **Ex. 16** (p.44) : f(x) = x − 1 + 1/(x − 2) sur IR ∖ {2}. 1) limites aux bornes ; 2) asymptotes ; 3) Ω(2;1)
  centre de symétrie ; équation de C dans (Ω, i⃗, j⃗) ; construire C.
- **Ex. 17** (p.44–45) : f(x) = 1/x + 1/(x + 2) et g(x) = 1/x − 1/(x + 2) sur IR ∖ {−2,0}. 1) limites aux bornes ;
  C_f et C_g ont les mêmes asymptotes ; 2) Ω(−1;0) centre de symétrie de C_f et (Ω, j⃗) axe de symétrie de C_g ; 3) équations de C_f et C_g dans (Ω, i⃗, j⃗).
- **Ex. 18** (p.45) : courbes C (de f) et C′ (de g) sur IR (figure). 1) si h(x) ≥ f(x) pour tout x, que dire des
  limites de h en +∞ et −∞ ? 2) si k(x) ≤ g(x), limites de k en ±∞ ? Si oui, les donner.
- **Ex. 19** (p.45) : f(x) = √(1 + x) et g(x) = 1 + x/2 sur « ]−1;+∞] » [sic]. 1) f(x) ≥ 0 et g(x) ≥ 0 sur [−1;+∞[ ; 2) (f(x))² et (g(x))², comparer ; 3) comparer f et g sur [−1;+∞[ ; 4) tracer f et g sur [−1;+∞[ ; 5) comparer
  A = 1,0000002 et B = √1,0000004.
- **Ex. 20** (p.45) : 1) plus grand de A = 1,0000002/1,0000004 et B = 0,9999996/0,9999998 ; 2) f(x) = (1 + 2x)/(1 + 4x)
  et g(x) = (1 − 4x)/(1 − 2x) : a) f(10⁻⁷) et g(10⁻⁷) ? b) pour x ≠ 1/2 et x ≠ −1/4, f(x) − g(x) =
  12x²/((1 + 4x)(1 − 2x)) ; c) résoudre f(x) − g(x) > 0 ; signe de f(10⁻⁷) − g(10⁻⁷) ; 3) comparer A et B.

### Maths et culture (p.46) — « L'asymptote : une notion en évolution »

« Donner une définition du mot asymptote n'est pas une chose simple. Les premières rencontres avec la notion en
soulignent le caractère à priori paradoxal. Dans les Essais (II, 2), Montaigne rapporte ainsi les travaux de
Jacques Peletier (1517 - 1582), un érudit proche de Ronsard et de la Pléiade : «Jacques Peletier me disait chez
moi qu'il avait trouvé deux lignes s'acheminant l'une vers l'autre pour se joindre, qu'il vérifiait toutefois ne
pouvoir jamais, jusques à l'infinité, arriver à se toucher.» L'interdiction du contact ayant progressivement
disparu, l'idée générale qui subsiste de nos jours est celle de proximité locale entre deux courbes. »
Illustrations : « Michel Eyquem de Montaigne » ; « «Les Essais» de Montaigne ».

### Écart avec la référence (`math-bac-sciences-exp/01` pour les limites ; `math-bac-techniques/01` § « Comportement asymptotique » pour les asymptotes)

**Correspondance corrigée** : le brief proposait sciences-exp/01 + bac-math/01 (branches infinies). Or le
contenu **publié** de bac-math/01 ne traite que les asymptotes verticales et horizontales (il renvoie
l'oblique au chapitre « étude de fonctions ») ; l'**asymptote oblique** est enseignée dans
**math-bac-techniques/01** (dernière notion) : c'est la meilleure source pour la partie III. sciences-exp/01
reste la référence pour les parties II et IV (opérations, formes indéterminées, composée, comparaison).

**Ce que les références enseignent et que ce manuel n'a PAS (à retirer)** :
- toute la **continuité** (continuité en un point/sur un intervalle, prolongement par continuité), le **TVI**,
  la stricte monotonie/solution unique, la **dichotomie**, l'**image d'un intervalle** : c'est le chapitre 3
  de ce manuel, pas le 2 ;
- **branches paraboliques** et directions asymptotiques, calcul de a = lim f(x)/x (techniques/01) : absents ;
  ici l'asymptote oblique est **donnée** (D : y = ax + b fournie, ou obtenue par division / forme
  ax + b + c/(x − 2)), sauf en « Apprendre à chercher » (Situations 1–2) ;
- la limite usuelle **sin x/x → 1** en 0 (sciences-exp/01) : non énoncée dans ce chapitre (sin apparaît
  seulement dans x + sin x, x sin(1/x), sin(1/√x)) ;
- le théorème de la limite monotone (« fonctions monotones et limites », techniques/01).

**Ce que ce manuel a en plus (ou autrement)** :
- une partie **I. Généralités sur les fonctions** absente des références bac : parité, symétrie des courbes
  de x² et √x par rapport à y = x, **composée g∘f** (domaine f(D)), **sens de variation d'une composée**
  (théorème), **fonctions associées** (translations t_{kj⃗}, t_{−λi⃗}, symétries par rapport aux axes ; −f,
  3f, |f|, f(x + 2), f(2x) en activité) ; support possible : `math-2eme-sec-sciences-info/12` (généralités) ;
- **définition topologique** de la limite finie en a (par intervalles ouverts J et I), à droite, à gauche ;
- **méthode** imprimée pour asymptote verticale (valeur interdite ≠ asymptote) et oblique (d(x) = f(x) −
  (ax + b), signe de d(x) pour la position relative) ;
- **centre et axe de symétrie** d'une courbe par changement de repère (Ex. 16–17) ;
- **expression conjuguée** comme « point méthode » (Situation 1, 3 ; Ex. 8) ;
- comparaison de nombres très proches et pièges de la calculatrice (Ex. 12, 19, 20 : 1,0000002 vs
  √1,0000004) ; itérée f₂₀₀₇ (Ex. 4) ; GEOPLAN ;
- QCM « trouver toutes les bonnes réponses » sur tableau de variation (Ex. 1, App. II.3).
- **Vocabulaire / notations** : « gof », « fog », « g o f » ; « fonctions associées » ; « formes indéterminées »
  signalées par « ? » dans les tableaux ; « asymptote … pour la courbe C » / « à C en +∞ » ; notation lim_a f,
  lim_{a⁺} f.

### Bornes de scope (chapitre 2)

- ✅ INCLUS : parité ; composée g∘f (définition, domaine, calcul) ; sens de variation d'une composée ;
  fonctions associées (f + k, f(x + λ), −f, f(−x), |f|, kf, f(kx)) et translations/symétries ; limites de
  référence (xⁿ, 1/xⁿ, √x, 1/√x) ; définition de la limite finie en a, à droite, à gauche ; unicité ;
  limite en a d'une fonction usuelle définie en a ; limites en ±∞ des polynômes et rationnelles ; opérations
  (somme, produit, quotient) et formes indéterminées ; levée d'indétermination (factorisation, simplification,
  expression conjuguée) ; limite d'une composée ; asymptotes verticale, horizontale, oblique (donnée ou par
  décomposition ax + b + c/(x − a)) ; position relative courbe/asymptote ; centre/axe de symétrie (Ex. 16–17) ;
  théorèmes de comparaison (minoration, encadrement, |f − ℓ| ≤ g) en a, a±, ±∞ ; lectures graphiques et
  tableaux de variations (sans dérivée).
- ⛔ EXCLU (non traité dans ces pages) : continuité, prolongement par continuité, TVI, dichotomie (→ chapitre 3) ; dérivation (→ chapitre 4 ; Ex. 15 mentionne une tangente parallèle à y = −x : voir doutes) ; branches
  paraboliques, directions asymptotiques ; lim sin x/x ; limite d'une fonction monotone ; fonction réciproque.

### Lecture

- **Pages lues en L1 (pdftotext)** : p.26 à p.46, toutes.
- **Pages lues sur l'image (110 dpi)** : p.26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
  44, 45, 46 = **21 / 21 (100 %)**.
- **Écarts texte / image constatés** : L1 perd tous les tableaux de variation (p.28, 34, 35, 38, 42, 44) et les
  tableaux d'opérations (p.32–33) ; flèches « ↦ » rendues par des glyphes vides (p.27) ; « IR ∖ {−1/2} »
  illisible (p.27) ; les translations t_{kj⃗}, t_{−λi⃗} (p.29) dégradées en « tk j », « t '.i » ; racines et
  fractions des Ex. 8, 10, 12, 17, 20 reconstruites sur image ; figures (courbes) non rendues. **Toute
  formule de cette section vient de l'image.**
- **Coquilles [sic]** : en-têtes « Chapitre2 : Limites de fonction » / « Limite de fonction » (p.31, 37, 41–43, 45) ; Act. prél. 2 p.27 « une et une seule réponse correcte, laquelle. » ; App. I.1 « f₁ = x² - 1 » ;
  « q'une » (App. I.1 3) ; Déf. 3) p.31 « Considérons une fonctions » ; App. II.2 « on peut pas le savoir » ;
  App. II.3 phrase parasite « Soit la fonction u dont le tableau des variations est donnée ci-dessous. » ;
  p.38 numéro « 2 » devant le titre « IV. Limites par comparaison. » et « Activité 1: » avant « Activités de
  découverte » ; IV Act. 3 2) « si pour tout si pour tout réel x » ; GEOPLAN « ]0;+∞] » ; Ex. 19 « ]−1;+∞] » ;
  « théoréme », « repére », « considére », « ci-aprés » (accents) ; Situation 2 « f(x) = √(2x² + 1)
  intuitivement » (pour √(2x² + x + 1)) ; Situation 3 : « l'expression conjuguée √(x + 1) − 2 » et
  « (√(2x + 19) − 5) » (les conjuguées sont √(x + 1) + 2 et √(2x + 19) + 5).
- **Doutes [?]** : (1) App. II.3 : le tableau de g a des abscisses imprimées dans l'ordre −∞, −2, 5, 2, 3, +∞
  (non croissant) avec une double barre ; valeurs lues : g : −∞ ↗ 0 (en −2) ↗ +∞ (en 5) ‖ −∞ ↗ 0 (en 2) ↗ 1 (en 3)
  ↗ +∞ ; à confirmer ; (2) Composée p.28 : « g une fonction dont l'ensemble de définition est f(D) » (au lieu de
  « contient f(D) ») — verbatim ; (3) Ex. 15 suppose la tangente (dérivée) alors que la dérivation est le
  chapitre 4 ; (4) [levé, audit R-7] Ex. 11 : tableau de g confirmé sur l'image, 3 (en −∞) ↘ 2 (en −1) ↘ 0 (en 3) ↗ +∞ ;
  (5) IV Act. 1 : « pour tout réel x » alors que g n'est pas définie en 0 ; (6) les théorèmes « Opérations »
  du II rappellent des résultats de 3ᵉ année (« Nous rappelons ») mais les présentent comme « Théorème ».

## 2.3 Chapitre 3 — Continuité (manuel 222472, p.47–64)

**Page de garde (p.47)** — « Chapitre 3 », titre « CONTINUITE ». Plan imprimé : « I . Continuité d'une fonction ·
II . Continuité d'une fonction composée · III . Image d'un intervalle par une fonction continue · IV . Fonction
réciproque d'une fonction continue et strictement monotone sur un intervalle ». Portrait légendé : « Bernhard
BOLZANO (Prague, 5/10/1782- Prague, 18/12/1848) » (sic : p.64 donne « 5 Octobre 1781 »). Pas de citation
liminaire ; encadré d'ouverture p.48 : « La notion de continuité nous est familière : le temps s'écoule d'une
manière continue, on ne passe pas brutalement de 12h à 12h 01s, il n'y a pas de saut. C'est en ce sens que
l'expression fonction continue est employée en mathématiques. »

**Plan du chapitre**

- **I. Continuité d'une fonction** (p.48–51) : Activités préliminaires 1–3 (p.48–49) · Activité de découverte
  (non numérotée, p.49) · « A retenir » (p.49–50 : continuité en un point, à droite, à gauche ; sur un
  intervalle ; prolongement par continuité ; opérations ; conséquences) · « Applications » 1–4 (p.50–51).
- **II. Continuité d'une fonction composée** (p.51–52) : Activité de découverte (non numérotée, p.51) · « A
  retenir » (p.51) · « Exemple » (p.51–52) · « Applications » (un exercice non numéroté, p.52).
- **III. Image d'un intervalle par une fonction continue** (p.52–55) : Activités préliminaires 1–3 (p.52–53) ·
  « A retenir » (p.54 : théorème, TVI, cas particuliers) · Remarque + tableau des images d'intervalles (p.54–55)
  · « Applications » 1–4 (p.55).
- **IV. Fonction réciproque d'une fonction continue et strictement monotone sur un intervalle** (p.55–58) :
  Activités de découverte 1–4 (p.55–57) · encadré « BIJECTION » (p.55) · « Exemple » (p.56) · sous-titre « Cas d'une fonction continue et strictement monotone sur un
  intervalle : » (p.56, avant l'Act. 2) · encadré
  « Fonction réciproque d'une bijection » (p.56) · « A retenir » (p.57 : Théorèmes 1–2, fonction racine nᵉ) ·
  « Applications » 1–4 (p.58).
- **Apprendre à chercher** (p.58) : une situation (x³ + x − 3, encadrement à la calculatrice).
- **Avec l'outil informatique** (p.59) : programme Pascal « Dichotomie ».
- **Exercices et problèmes** (p.60–63) : numérotés 1 à 31, mais le n° 10 n'est pas imprimé et le n° 16 l'est
  deux fois (p.61, colonne gauche puis colonne droite) ⇒ **31 exercices**.
- **Maths et culture** (p.64) : biographie de Bolzano et « Théorème de Bolzano ».

Pas d'exercice résolu, pas de page de synthèse de fin de chapitre, pas de QCM/Vrai-Faux séparé (QCM et Vrai-Faux
inclus dans les exercices : Ex. 7, 8, 24).

### Cours — Activités (une ligne chacune)

**I. Continuité d'une fonction — Activités préliminaires** (p.48–49)

- **Act. prél. 1** (p.48) : trois graphiques de f, g, h définies sur IR₊ (C_f continue passant par A(2;1) ; C_g
  avec un trou en A et un point isolé B(2;2) ; C_h en deux morceaux B₁, B₂ avec saut en 2). 1) f(2), g(2), h(2) ; 2) limite éventuelle en 2 ; 3) lesquelles sont continues en 2 ? 4) choisir un intervalle J contenant f(2) et
  voir s'il existe toujours un intervalle ouvert I contenant 2 tel que f(I) ⊂ J ; idem pour g et h. « Remarquez
  que la courbe C_f peut être tracée au voisinage du point A sans lever la main, ce qui n'est pas possible pour
  C_g et C_h. »
- **Act. prél. 2** (p.48) : 1) continuité au point a de : f(x) = √(x² − x + 1), a = −1 ; g(x) = (x − 1)/(x² − 3x + 2)
  si x ≠ 1, g(1) = 2, a = 1 ; h(x) = 3x − 1 si x ≥ 1, x² + 2 si x < 1, a = 1 ; k(x) = 1/(x + 2) si x < −2,
  −x si x ≥ −2, a = −2 ; 2) limites à droite et à gauche, continuité à droite et à gauche en ce point.
- **Act. prél. 3** (p.49) : a) f : [1,+∞[ → IR, x ↦ √(x − 1) : vérifier que f est continue sur [1,+∞[ ; b) g(x) =
  x² + 1 si x ≥ 0, x − 1 si x < 0 : continue sur [0,+∞[ et ]−∞,0[ ; texte : « On remarque que g n'est pas continue
  sur IR car elle n'est pas continue au point 0 On ne peut pas dire que g est continue sur IR* car IR* n'est pas
  un intervalle, mais on dit qu'elle est continue en tout point de IR* . »

**I. — Activité de découverte** (p.49, non numérotée)

- f(x) = (x² − 4)/(x − 2) pour x ≠ 2. a) lim_{x→2} f(x) ; b) m ∈ IR et g_m(x) = f(x) si x ≠ 2, g_m(2) = m :
  • m ≠ 4 : g_m continue en 2 ? • m = 4 : montrer que g₄ est continue sur IR. « Toutes les fonctions g_m sont
  des prolongements de la fonction f, mais g₄ est le seul prolongement de f qui soit continu au point 2 : on
  l'appelle prolongement par continuité de f au point 2. »

**II. Continuité d'une fonction composée — Activité de découverte** (p.51, non numérotée)

- u : IR → IR, x ↦ x² − 4 et h : IR₊ → IR, x ↦ √x. 1) expression et ensemble de définition de h o u ; 2) u(3), h o u(3) ; continuité de u en 3 et de h en u(3) ; 3) lim_{x→3} (h o u)(x), en déduire la continuité
  de h o u au point 3.

**III. Image d'un intervalle par une fonction continue — Activités préliminaires** (p.52–53)

- **Act. 1** (p.52–53) : courbes de f(x) = x² + 2x ; g(x) = (1/2)x + 1 si x < 0, x + 2 si x ≥ 0 ; h(x) = −x si x < 0,
  −x² + 1 si x ≥ 0. 1) a) images par f de [−3,−1] ; [−2,1] et [0,+∞[ ; b) g([−4,−1]) et g([−1,2]) ; remarque sur
  g([−1,2]) ; g continue sur [−4,−1] ? sur [−1,2] ? c) h([−1,2]) ; h continue sur [−1,2] ? 2) parmi [−4,−2] ;
  [−2,1] ; [−3,1] ; [0,1], ceux où f est monotone ; comparer f([a,b]) et [f(a), f(b)] ; conclure.
- **Act. 2** (p.53) : trois courbes C_f (cubique), C_g (deux segments avec saut en −2), C_h (segment puis arc,
  saut en −1). 1) a) f(−2), f(2), g(−2), g(2), h(−2), h(2) ; b) choisir λ intermédiaire entre f(−2) et f(2) et
  voir s'il existe c ∈ [−2,2] tel que f(c) = λ ; c) idem pour g et h ; 2) a) variations de f sur [−2,1] ;
  b) J = f([−2,1]) ; c) λ ∈ J : nombre de solutions de f(x) = λ, x ∈ [−2,1].
- **Act. 3** (p.53) : f continue sur [1,4] avec f(1).f(4) < 0. a) intersection de la courbe avec l'axe des
  abscisses (dessin) ; b) vérifier graphiquement que f(x) = 0 admet au moins une solution dans [1,4].

**IV. Fonction réciproque — Activités de découverte** (p.55–57)

- **Act. 1** (p.55) : représenter et déterminer les bijections parmi f : IR → IR, x ↦ 2x − 3 ;
  g : IR → [−2,+∞[, x ↦ x² − 2 ; h : IR₊ → IR, x ↦ x² − 2 ; k : [0,π] → [0,1], x ↦ sin x ; l : [0,π/2[ → [0,1],
  x ↦ sin x.
- **Act. 2** (p.56) : f : [1,+∞[ → IR et g : [0,+∞[ → IR, x ↦ x² − 2x. a) représenter f et g ; b) tableau
  OUI/NON : « Strictement monotone » / « Bijective de I sur son image » / « Continue sur I ». Conclusion
  imprimée : « Plus généralement f étant une fonction strictement monotone sur I, on admet que f est une
  bijection de I sur f(I) De plus si f est continue sur I, alors f⁻¹ est continue sur f(I) ».
- **Act. 3** (p.56) : f continue et « stictement » [sic] monotone sur I. 1) f strictement croissante
  (resp. décroissante) ⇒ f⁻¹ aussi ; 2) M(x,y) ∈ (C_f), (D) : y = x, M′ = S_D(M) : coordonnées de M′ et
  M′ ∈ C_{f⁻¹}.
- **Act. 4** (p.57) : f(x) = xⁿ sur IR₊, n ≥ 2 ; montrer que f est une bijection de IR₊ sur IR₊. « • La fonction
  réciproque de f est appelée fonction racine nième. La racine n ième d'un réel positif x est notée ⁿ√x (Lire :
  racine enième de x). Ainsi : x ∈ IR₊ , y ∈ IR₊ ; y = ⁿ√x ⇔ x = yⁿ ; ⁿ√(xⁿ) = x ; (ⁿ√x)ⁿ = x »

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Continuité en un point — Définitions** (p.49) — « Soit f une fonction définie sur un intervalle
> ouvert I et a ∈ I . f est dite continue en a si et seulement si : lim_{x→a} f(x) = f(a) Soit f une fonction
> définie sur un intervalle de type [a,b [(a<b) ou [a,+∞[. On dit que f est continue à droite en a si :
> lim_{x→a⁺} f(x) = f(a) Soit f une fonction définie sur un intervalle de type ]b,a] (b < a) ou ]−∞ , a] On dit
> que f est continue à gauche en a si : lim_{x→a⁻} f(x) = f(a) »
> **Conséquence** — « Une fonction est continue en a si et seulement si elle est continue à droite et à gauche
> en a. »

> **Continuité sur un intervalle** (p.49–50) — « On dit que f est continue sur ]a,b[ si elle est continue en
> tout point de ]a,b[. On dit que f est continue sur [a,b] si elle est continue en tout point de ]a,b[ et si
> elle est continue à droite en a et continue à gauche en b. De la même manière on définit la continuité d'une
> fonction f sur [a,b[ , ]a,b] ,[a,+∞[ ]−∞ , a] ... »

> **Prolongement par continuité d'une fonction** (p.50) — « Soit f une fonction définie sur un intervalle I
> sauf en un point a de I. Si f admet une limite finie ℓ au point a, alors la fonction g définie sur I par :
> { g(x)=f(x) si x ≠ a ; g(a)=ℓ } est continue sur I. On l'appelle prolongement par continuité de f au point a. »

> **Opération sur les fonctions continues** (p.50) — « Si f et g sont deux fonctions définies sur un intervalle
> I et continues sur I, alors • f+g, f.g et |f| sont continues sur I. • Pour tout réel k, la fonction k.f est
> continue sur I. • Si g(x) ≠ 0 pour tout x ∈ I, alors 1/g et f/g sont continues sur I. • Si f (x) ≥ 0 pour
> tout x ∈ I, alors √f est continue sur I. »
> **Conséquences** — « • Toute fonction polynôme est continue sur IR . • Toute fonction rationnelle est continue
> sur chacun des intervalles ouverts déterminés par son ensemble de définition. »

> **A retenir — Continuité d'une composée** (p.51) — « Soit f et g deux fonctions définies respectivement sur
> deux intervalles ouverts I et J et x₀ ∈ I tel que f (x₀) ∈ J. [∈ déplacé à l'impression : « respectivemen∈sur …
> et x₀ I »] Si f est continue en x₀ et g est continue en
> f (x₀) alors gof est continue en x₀. » (schéma : I → J → IR ; x₀ ↦ f(x₀) ↦ (gof)(x₀), flèche « gof ».)
> « Si f est continue sur I, g est continue sur J et f(I) ⊂ J , alors gof est continue sur I. »

> **Exemple** (p.51–52, hors encadré) — « Soit la fonction h : x ↦ √(x² − 5x + 4) Le schéma suivant
> x ↦ x² − 5x + 4 ↦ √(x² − 5x + 4) permet de voir que h = gof où f : IR → IR, x ↦ x² − 5x + 4 et
> g : IR₊ → IR, x ↦ √x f est une fonction polynôme qui s'annule aux points 1 et 4. Le tableau de signe de f est
> le suivant : » (x : −∞, 1, 4, +∞ ; f(x) : + 0 − 0 +) « Ceci nous permet d'affirmer que f ([4,+∞[) ⊂ IR₊ et
> f (]−∞ ,1]) ⊂ IR₊ Comme f est continue sur IR et g continue sur IR₊ , on conclut que h est continue sur chacun
> des intervalles ]−∞ ,1] et [4, +∞[. » (les flèches « ↦ » du schéma sont imprimées comme des carrés vides.)

> **A retenir — Théorème** (p.54) — « L'image d'un intervalle par une fonction continue est un intervalle. »
> **Théorème des valeurs intermédiaires** — « Si f est une fonction continue sur un intervalle [ a , b ], alors
> pour tout réel λ intermédiaire entre f(a) et f(b) il existe au moins un réel c ∈ [a,b] tel que f(c) = λ
> Autrement dit l'équation f(x) = λ admet au moins une solution dans [ a , b] » (figure : C_f, λ, c, f(a), f(b).)
> **Cas particuliers** — « • Si f est continue et strictement monotone sur [a,b] alors pour tout réel λ
> intermédiaire entre f(a) et f(b) il existe un unique réel x ∈ [a,b] tel que f(x) = λ . • Si f(a).f(b) < 0 ,
> alors il existe au moins un réel c ∈ [a,b] tel que f(c) = 0 » (figure.)

> **Remarque** (p.54, hors encadré) — « Le théorème des valeurs intermédiaires permet de donner une valeur
> approchée des solutions d'équations qu'on ne peut pas résoudre par les procédés usuels (discriminant, …) Le
> tableau suivant donne les images des différents types d'intervalles par des fonctions continues et strictement
> monotones : »
> Tableau (p.54–55, vérifié à 200 dpi) — « Si f est croissante alors » | « Si f est décroissante alors » :
> f([a,b]) = [f(a),f(b)] | f([a,b]) = [f(b),f(a)] ·
> f([a,b[) = [f(a), lim_{x→b⁻} f(x)[ | f([a,b[) = ]lim_{x→b⁻} f(x) , f(a)] ·
> f(]a,b]) = ]lim_{x→a⁺} f(x) , f(b)] | f(]a,b]) = [f(b), lim_{x→a⁺} f(x)[ ·
> f(]a,b[) = ]lim_{x→a⁺} f(x) , lim_{x→b⁻} f(x) [ | f(]a,b[) = ]lim_{x→b⁻} f(x) , lim_{x→a⁺} f(x) [ ·
> f(]−∞, a]) = ] lim_{x→−∞} f(x) f(a)] | f(]−∞,a ]) = [f(a), lim_{x→−∞} f(x)[ ·
> f(]−∞ ,a [) = ] lim_{x→−∞} f(x) lim_{x→a⁻} f(x)[ | f(]−∞,a[) = ]lim_{x→a⁻} f(x) , lim_{x→−∞} f(x)[ ·
> f([a,+∞[) = [ f(a), lim_{x→+∞} f(x) [ | f([a, +∞[) = ] lim_{x→+∞} f(x) ,f(a)] ·
> f(]a, +∞ [) = ] lim_{x→a⁺} f(x), lim_{x→+∞} f(x)[ | f(]a, +∞[) = ] lim_{x→+∞} f(x) , lim_{x→a⁺} f(x)[ ·
> f( IR ) = ] lim_{x→−∞} f(x) , lim_{x→+∞} f(x) [ | f( IR) = ] lim_{x→+∞} f(x), lim_{x→−∞} f(x)[.
> (Virgules manquantes imprimées dans les lignes ]−∞, a] et ]−∞, a[ de la colonne « croissante ».)

> **Encadré « BIJECTION »** (p.55) — « f étant une fonction définie sur un intervalle I et à valeurs dans un
> intervalle J, f est une bijection de I vers J si chaque élément de l'intervalle J a un antécédent et un seul
> dans I. On dit alors que la fonction f est une bijection de I sur J. »

> **Exemple** (p.56, hors encadré) — « On considère la fonction f : IR₊ → IR₊, x ↦ x² f est une bijection. En
> effet , Soit y ∈ IR₊ L'equation x² = y admet dans IR₊ une solution unique qui est x = √y Donc il existe un réel
> unique x tel que f (x)=y Pour déterminer l'expression de f⁻¹ il suffit d'exprimer y en fonction de x sachant
> que x = f(y) Donc x=f(y) signifie { x = y² ; x ∈ IR₊, y ∈ IR₊ } signifie { y = √x ; x ∈ IR₊ , y ∈ IR₊ } Donc
> f⁻¹(x) = √x , x ∈ IR₊ »

> **Encadré « Fonction réciproque d'une bijection: »** (p.56) — « Soit f une bijection d'un intervalle I sur un
> intervalle J. La fonction réciproque de f, notée f⁻¹ , est la fonction dénfinie sur J et à valeur dans I telle
> que : x ∈ J, y ∈ I ; (y = f⁻¹(x) signifie x = f(y)) » (sic « dénfinie ».)

> **A retenir — Théorème 1** (p.57) — « Toute fonction f strictement monotone sur un intervalle I, réalise une
> bijection de I sur f(I) ; et si elle est continue sur I alors sa réciproque f⁻¹ est continue sur f(I). »
> **Théorème 2** — « Si f est une bijection de I sur f(I) alors • f et f⁻¹ ont même sens de variation. • Leurs
> courbes représentatives dans un repère orthonormé sont symétriques parrapport à la droite d'équation y = x. »
> (figure : C_f, M(x,y), M(x′,y′) [sic, pour M′], droite y = x.)
> **Fonction racine nième** — « La fonction puissance nième x ↦ xⁿ est une bijection strictement croissante de
> IR₊ sur IR₊ Sa bijection réciproque est la fonction notée ⁿ√ et appelée fonction racine nième ⁿ√ : IR₊ → IR₊,
> x ↦ ⁿ√x On a : pour tout x ≥ 0 et y ≥ 0 : y = ⁿ√x ⇔ x = yⁿ x =( ⁿ√x )ⁿ ; ⁿ√(yⁿ) = y. »

### Applications (exercices d'application intégrés au cours)

**Applications du I** (p.50–51)

- **1** : continuité de f en a : a) f(x) = E(x) − x, a = 2 ; b) f(x) = 2x − 1 si x > 3, x² − x − 1 si x ≤ 3, a = 3.
- **2** : intervalles de continuité de p(x) = 1/(x + 4) ; q(x) = √(x² − 1) ; r(x) = (x + 2)/(x² − 3x + 2) ;
  s(x) = E(x), x ∈ [−1,2] (E partie entière).
- **3** : ensemble de définition et intervalles ouverts de continuité : a) 1/(x − 2) + x² − 4x − 3 ;
  b) x√(x − 3) ; c) (x + 3)/|x² − 3x + 2| ; d) (x² + 1)/(|x| − 3).
- **4** : f(x) = (√(x + 1) − 1)/x pour x ≠ 0 ; montrer que f est prolongeable par continuité en 0.

**Applications du II** (p.52, non numérotée) : ensemble de définition, écriture sous la forme gof et intervalles
de continuité de h₁(x) = √(2x − 1) ; h₂(x) = sin πx ; h₃(x) = (|x| − 1)² ; h₄(x) = cos(2x − π/3).

**Applications du III** (p.55)

- **1** : avec les courbes de l'Act. 1 : f([−3,−1]), f(]−3,1[), f([−1,+∞[), f([−2,0[), g(]−∞,0]), g(]1,2[),
  h([−1/2,0[), h([0,1/2]) et h([1,+∞[).
- **2** : f(x) = x³ − x² + 3x + 1 sur IR. a) f(1) et f(3) ; en déduire un réel c tel que f(c) = 17 ; b) il existe
  au moins un réel a tel que f(a) = −2.
- **3** : x³ + x − 1 = 0 admet une solution dans [0,1] ; valeur approchée à 10⁻¹ près.
- **4** : il existe c ∈ [0, π/2] tel que cos c = c ; valeur approchée à 10⁻¹ près.

**Applications du IV** (p.58)

- **1** : tracer (C_{f⁻¹}) dans deux cas (deux graphiques : C_f et y = x).
- **2** : f : [0, π/2] → IR, x ↦ cos x : montrer que f admet une fonction réciproque, intervalle de définition.
- **3** : f(x) = x² − 4x + 3 sur IR. a) représenter f, déterminer f(IR) ; b) f₁ : [2,+∞[ → [−1,+∞[ et
  f₂ : ]−∞,2] → [−1,+∞[, x ↦ f(x) : bijectivité, f₁⁻¹ et f₂⁻¹.
- **4** : simplifier ⁴√16 , ⁶√64 , ³√27 , ⁵√(7¹⁰) , (⁸√4)⁴.

### Apprendre à chercher (p.58)

f(x) = x³ + x − 3 sur IR. 1) f(x) = 0 admet une solution α dans [1,2] ; 2) a) à la calculatrice f(1,1), f(1,2),
f(1,3) … ; intervalle contenant α ; b) f(1,21), f(1,22), f(1,23) … ; valeur approchée de α par défaut à 10⁻² près.

### Avec l'outil informatique (p.59) — programme Pascal de dichotomie

« Programme de résolution de l'équation f(x) = 0 Soit la fonction f : f(x) = x³ + x - 3. On admet que f admet un
unique solution x₀ dans l'intervalle [1,2]. Le programme suivant permet de déterminer une valeur approchée à
10⁻² près de x₀. » Programme (verbatim, L1 confirmé sur l'image) :

```
Program Dichotomie ;
Uses Wincrt ;
Var a,b:Real; n,c:integer;
 Function f(x : Real) : Real;
   begin
     f:= x*x*x+x-3 end;
 Function Dicotomie(a,b:Real;n:integer): Real;
   Var m ,fm: Real; k:integer;s;boolean;
   Begin
     s:=f(a)<0;
     for k:=1 to n-1 do
       begin
         m:=(a+b)/2;fm:=f(m);
         if fm=0 then
           begin
             dicotomie:=m;
             exit
           end;
         if s=(fm<0) then a:=m else b:=m
       end;
     dicotomie:=(a+b)/2
 End;
Begin
  clrscr;
  writeln(' ****** Résolution de l''équation x3+x-3 = 0 dans [1,2] par DICHOTOMIE ******');
  repeat
    write ('Nombre d''_tapes : '); Readln(n);writeln;
    write ('Nombre de chiffres après la virgule : '); Readln(c);writeln;
  until (n>0) and (c>0);
  a:=1;b:=2;
  Writeln (' La valeur approchée de la solution xo de l''équation x3+x-3 = 0 a 10-',c,' près est= ');
  write('          x0 = ' ,dicotomie(a, b, n) :0:c) ;
End.
```

(sic : « k:integer;s;boolean; » pour « s:boolean » ; « Dicotomie »/« dicotomie » ; « d''_tapes » pour
« d''étapes » ; « un unique solution ».)

### Exercices et problèmes (p.60–63) — 31 exercices (numérotation imprimée 1–31, sans 10, avec 16 en double)

- **Ex. 1** (p.60) : continuité de f en a : a) sin x/x si x ≠ 0, f(0) = 1, a = 0 ; b) √(x³ − 3x + 5), a = 0 ;
  c) √(x − 1) si x > 1, 1 − 1/x si 0 < x < 1, f(1) = 2, a = 1 ; d) (x² + 4x − 5)/(x + 5) si x ≠ −5, f(−5) = −6,
  a = −5 ; e) (x − 1)²/|x − 1| si x ≠ 1, f(1) = 2, a = 1 ; f) (−4 + x²)/(x − 2) si x > 2, √(x² + 12) si x ≤ 2, a = 2.
- **Ex. 2** (p.60) : a, b, c pour que f soit continue en 3 : f(x) = (x² + ax + b)/(x − 3) si x > 3 ;
  (−4 + cx²)/(x − 2) si x < 3 ; f(3) = 2.
- **Ex. 3** (p.60) : h(x) = (x − 2 + λ|x − 2|)/|x − 2| si x ≠ 2, h(2) = −3. a) pour tout λ ∈ IR, h n'est pas continue
  en 2 ; b) λ pour la continuité à droite en 2 ; c) λ pour la continuité à gauche en 2.
- **Ex. 4** (p.60) : f(x) = (√x − 2)/(x − 4) si x ≠ 4, f(4) = λ ; λ pour que f soit continue en 4.
- **Ex. 5** (p.60) : a) ensemble de définition de f : x ↦ x/sin x ; b) prolongement par continuité en 0 ? « Et
  ailleurs ? »
- **Ex. 6** (p.60) : prolongement par continuité en 0 de f : x ↦ x²|1 + 1/x| ; g : x ↦ √(x³ + x²)/x ;
  h : x ↦ x|1 + 1/x| ; k : x ↦ (x³ + |x|)/x ?
- **Ex. 7** (p.60–61) : « Cochez la réponse correcte » : 1) f(x) = x² si x ≥ 2, 2x − 1 si x < 2 : a) continue en
  2 b) continue à droite en 2 c) continue à gauche en 2 ; 2) courbe de f (saut en 1) : a) continue en 1 b) à droite
  en 1 c) à gauche en 1 ; 3) x ↦ E(x) est continue sur a) [2,3] b) ]2,3] c) [2,3[ ; 4) image de [−1,2] par x ↦ x² :
  a) [1,4] b) [0,4] c) [−1,4] ; 5) x³ + 2x + 5 = 0 a une solution dans a) ]0,1[ b) ]−1,2[ c) ]−2,−1[.
- **Ex. 8** (p.61) : « Cochez la case correcte » (Vrai/Faux) : 1) la composée de deux fonctions continues sur IR
  est continue sur IR ; 2) l'image d'un intervalle par une fonction décroissante est un intervalle ; 3) l'image
  d'un intervalle par une fonction continue est un intervalle.
- **Ex. 9** (p.61) : D_f et continuité sur D_f : a) 2x² − 3x + 6 ; b) (x² − 3x + 6)/(x² − 3x − 4) ; c) √(x² − 3x) ;
  d) (3x + 1)/√(x − 3) ; e) x² + sin x.
- **Ex. « 16 » (position du n° 10)** (p.61, colonne gauche) : f(x) = (√(x² + 3) − 2)/(x − 1) si x ≠ 1, f(1) = 1/2 ;
  montrer que f est continue sur IR.
- **Ex. 11** (p.61) : f(x) = (x + |3x|)/x si x ≠ 0, f(0) = −2 sur IR. a) continuité à droite et à gauche en 0 ;
  b) intervalles de continuité.
- **Ex. 12** (p.61) : mêmes questions avec g(x) = (x + 1 + 2|x + 1|)/|x + 1| si x ≠ −1, g(−1) = 3, a = −1.
- **Ex. 13** (p.61) : f(x) = E(x) + (x − E(x))². a) expression sur [0,1[ et [1,2[ ; b) tracer la courbe sur [0,2] ;
  c) f continue sur IR.
- **Ex. 14** (p.61) : f : IR*₊ → IR, x ↦ sin(π/x) ; intervalles de continuité.
- **Ex. 15** (p.61) : « Mêmes questions que l'exercice n° 13 » avec f : IR → IR, x ↦ 1/E(x) (sic, voir doutes).
- **Ex. 16** (p.61, colonne droite) : « Mêmes questions que l'exercice n° 14 » avec f : IR → IR,
  x ↦ x⁴/(x³ − 3x² − x + 3).
- **Ex. 17** (p.62) : (E) : x³ − 2x + 1 = 0. 1) a) une solution α dans [−2,−1] ; b) valeur approchée par défaut à
  10⁻¹ près ; 2) racine évidente, résoudre (E), retrouver le résultat.
- **Ex. 18** (p.62) : f définie sur I = [−1,3], courbe C_f (figure). a) trois réels de I tels que f(x) = 0 ;
  b) valeurs approchées par défaut à 10⁻¹ près.
- **Ex. 19** (p.62) : (E) : x⁴ − 8x² + 4 = 0. 1) a) par le TVI, une solution α dans [2,3] ; b) valeur approchée par
  défaut à 10⁻¹ près ; 2) résoudre (E) et retrouver les résultats.
- **Ex. 20** (p.62) : f(x) = (1/3)x³ − x² + x − 2. a) variations et courbe ; b) f bijection de IR vers IR ;
  c) x³ − 3x² + 3x − 6 = 0 a une solution unique α ; valeur approchée par excès à 10⁻¹ près.
- **Ex. 21** (p.62) : I = [a,b], f continue sur [a,b] avec f(I) = I ; g(x) = f(x) − x ; montrer qu'il existe
  c ∈ [a,b] tel que g(c) = 0 ; que conclure pour f ?
- **Ex. 22** (p.62) : g(x) = (1 + x)³ + x sur IR. a) g(x) = 0 a une unique solution α dans [−1,0] ; b) encadrement
  de α d'amplitude 10⁻¹.
- **Ex. 23** (p.62) : a) 1 − x − sin x = 0 admet une solution dans [0, π/2] ; b) x⁴ − 4/x = x admet une solution
  dans [1,2].
- **Ex. 24** (p.63) : « Répondre par vrai ou faux » : □ si lim_{a⁺} f = lim_{a⁻} f alors f est continue en a ;
  □ si f est strictement croissante sur [a,b] alors f([a,b]) = [f(a),f(b)] ; □ f : IR → IR, x ↦ |x| admet une
  fonction réciproque ; □ sin⁻¹ étant la réciproque de sin : [0;π/2] → IR, x ↦ sin x, alors sin⁻¹(1/2) = π/6.
- **Ex. 25** (p.63) : f : x ↦ √(x − 2) + 1. 1) bijection de son ensemble de définition vers un intervalle à
  déterminer ; 2) f⁻¹ ; 3) tracer (C_f) et (C_{f⁻¹}).
- **Ex. 26** (p.63) : f(x) = x/(1 + |x|). 1) bijection de IR sur f(IR) ; 2) f(IR) et f⁻¹ ; 3) tracer (C_f) et
  (C_{f⁻¹}).
- **Ex. 27** (p.63) : f(x) = x³ + x² + 2x − 4. 1) variations et courbe ; 2) bijection de IR vers IR ; 3) tracer (C_f) et (C_{f⁻¹}).
- **Ex. 28** (p.63) : f(x) = 1 + 1/x sur IR*₊. 1) bijection de IR*₊ sur un intervalle à déterminer ; 2) f⁻¹(x) ; 3) tracer (C_f) et (C_{f⁻¹}).
- **Ex. 29** (p.63) : f(x) = 2x² − x + 1 sur I = [1/4,+∞[. a) bijection de I sur un intervalle J ; b) f⁻¹(x) pour
  x ∈ J.
- **Ex. 30** (p.63) : écrire plus simplement ⁶√729 , (⁴√11)⁸ , ⁵√(7¹⁰) , ⁷√(3²⁸).
- **Ex. 31** (p.63) : a ≥ 0, n, p entiers naturels non nuls : a) ⁿ√(aⁿᵖ) = aᵖ ; b) ⁿᵖ√(aᵖ) = ⁿ√a ;
  c) ⁿ√a ⁿ√b = ⁿ√(ab) ; d) ⁿ√(ᵖ√a) = ⁿᵖ√a ; e) ⁿ√a ᵖ√a = ⁿᵖ√(aⁿ⁺ᵖ).

### Maths et culture (p.64) — Bolzano

« Bernard Placidus Johann Nepomuk Bolzano (5 Octobre 1781 - 18 Décembre 1848) était un mathématicien tchèque de
langue allemande, né en 1781 et mort en 1848 à Prague. Étudiant en philosophie et en mathématiques, il devint
prêtre en 1805. Il enseigna alors les sciences de la religion à Prague et consacra le reste de son temps aux
mathématiques. Ses travaux portèrent essentiellement sur les fonctions, la logique et la théorie des nombres. Il
est considéré comme l'un des principaux contributeurs à la logique telle qu'elle est aujourd'hui établie. Il est
connu pour le théorème de Bolzano, ainsi que pour le théorème de Bolzano-Weierstrass, développé conjointement avec
Karl Weierstrass. **Théorème de Bolzano** Soit f une fonction continue de IR dans IR Si f change de signe entre a
et b, alors il existe x ∈ [a,b] telque f(x)=0 »

### Écart avec la référence (`math-bac-sciences-exp/01` pour I–III ; `math-bac-sciences-exp/04` ou `math-bac-techniques/03` pour IV)

**Correspondance corrigée** : le brief proposait sciences-exp/01 + techniques/01. Le chapitre a en plus une
partie **IV. Fonction réciproque** (bijection, f⁻¹, symétrie par rapport à y = x, racine nᵉ) : elle relève de
**sciences-exp/04 « Fonctions réciproques »** (ou techniques/03), sans la dérivation de f⁻¹.

**Ce que les références enseignent et que ce manuel n'a PAS (à retirer)** :
- sciences-exp/01 : **opérations sur les limites, formes indéterminées, limites et ordre (comparaison)** — déjà
  au chapitre 2 de ce manuel, pas ici ; la limite usuelle **sin x/x → 1** n'est pas énoncée en encadré (elle est
  seulement utilisée implicitement : Ex. 1 a), Ex. 5) ;
- sciences-exp/01 : théorème **« signe constant »** (f continue ne s'annulant pas), image d'un **segment** =
  [m, M] (minimum/maximum) : absents ; techniques/01 : théorème des fonctions monotones (limite monotone) : absent ;
- sciences-exp/04 / techniques/03 : **dérivabilité de f⁻¹** et formule (f⁻¹)′ = 1/f′(f⁻¹), tangentes, dérivée
  de ⁿ√x, **restriction** d'une fonction (le mot n'est pas employé, mais App. IV.3 fait restreindre x² − 4x + 3) ;
  puissances rationnelles (techniques/03) ;
- techniques/01 : asymptotes et branches paraboliques (ici au chapitre 2, sans branches paraboliques).

**Ce que ce manuel a en plus (ou autrement)** :
- **partie entière E(x)** utilisée dans les exercices de continuité (App. I.1 a), I.2, Ex. 7.3, 13, 15) ;
- **définition de la continuité en a** par lim_{x→a} f(x) = f(a) (sans ε) et image f(I) ⊂ J (Act. prél. 1.4) ;
- tableau des **images de 9 types d'intervalles** par une fonction continue strictement monotone (croissante /
  décroissante), y compris ]−∞, a], ]−∞, a[ et IR ;
- **définition de la bijection** (encadré) et de la réciproque (y = f⁻¹(x) ⇔ x = f(y)), exemple x² ↦ √x,
  **sin⁻¹** cité dans un Vrai-Faux (Ex. 24 : sin⁻¹(1/2) = π/6), réciproque de cos sur [0, π/2] (App. IV.2) ;
- **racine nᵉ** et règles de calcul (Ex. 30–31, App. IV.4) ;
- **algorithmique** : programme **Pascal** de dichotomie complet (p.59) — spécifique à la section
  Informatique ; recherche d'encadrement à la calculatrice (Apprendre à chercher) ;
- théorème de **point fixe** (Ex. 21 : f(I) = I ⇒ g(c) = 0) ; Théorème de Bolzano (culture).
- **Vocabulaire / notations** : « gof », « h o u » ; « λ intermédiaire entre f(a) et f(b) » ; « bijection de I
  vers J » / « de I sur J » ; « fonction racine nième », notation ⁿ√x ; S_D (symétrie d'axe D) ; « IR*₊ ».

### Bornes de scope (chapitre 3)

- ✅ INCLUS : continuité en un point, à droite, à gauche ; continuité sur un intervalle ; prolongement par
  continuité ; opérations sur les fonctions continues (somme, produit, |f|, kf, 1/g, f/g, √f) ; continuité des
  polynômes et rationnelles ; fonctions définies par morceaux, valeur absolue, partie entière ; continuité d'une
  composée (en un point, sur un intervalle) ; image d'un intervalle par une fonction continue ; TVI ; cas
  strictement monotone (solution unique) ; f(a).f(b) < 0 ; tableau des images d'intervalles ; valeurs approchées
  (calculatrice, dichotomie, programme Pascal) ; bijection, fonction réciproque, continuité et sens de variation
  de f⁻¹, symétrie des courbes par rapport à y = x ; calcul explicite de f⁻¹ ; fonction racine nᵉ et règles de
  calcul ; point fixe (Ex. 21) ; sin⁻¹ (mention, Ex. 24).
- ⛔ EXCLU (non traité dans ces pages) : dérivabilité de f⁻¹ et de ⁿ√x ; arctan / fonctions trigonométriques
  réciproques comme objet d'étude ; théorème « signe constant » et [m, M] (non énoncés) ; limite monotone ;
  définition ε-δ ; limites/asymptotes (chapitre 2) ; Ex. 20 et 27 demandent des « variations » sans dérivation
  enseignée à ce stade (chapitre 4) — voir doutes.

### Lecture

- **Pages lues en L1 (pdftotext)** : p.47 à p.64, toutes.
- **Pages lues sur l'image (110 dpi)** : p.47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64
  = **18 / 18 (100 %)** ; p.54 relue à 200 dpi (tableau des images d'intervalles).
- **Écarts texte / image constatés** : L1 perd les accolades des fonctions par morceaux (Act. prél. 2, Ex. 1–4,
  11, 12), les flèches de schémas et les symboles ⊂, ∈ ; le tableau des images (p.54–55) et les racines nᵉ
  (p.57–58, 63) sont illisibles en L1 ; le programme Pascal (p.59) est correctement restitué par L1 (confirmé
  sur l'image, indentation reprise de l'image). **Toute formule de cette section vient de l'image.**
- **Coquilles [sic]** : dates de Bolzano « 5/10/1782 » (p.47) vs « 5 Octobre 1781 » (p.64), prénom « Bernhard »
  vs « Bernard » ; n° 10 absent et n° 16 en double (p.61) ; « stictement » (IV Act. 3) ; « dénfinie » (p.56) ;
  « parrapport » (p.57) ; « L'equation » (p.56) ; « M(x′,y′) » sur la figure p.57 pour M′ ; « telque » (p.64) ;
  « un unique solution », « s;boolean », « Dicotomie », « d''_tapes » (Pascal, p.59) ; virgules manquantes dans
  deux lignes du tableau p.54 ; l'Exemple p.56 dit « exprimer y en fonction de x sachant que x = f(y) »
  (cohérent avec l'encadré, noté tel quel).
- **Doutes [?]** : (1) Ex. 15 « Mêmes questions que l'exercice n° 13 » avec 1/E(x) : l'Ex. 13 porte sur une
  fonction précise (E(x) + (x − E(x))²) ; la question attendue est sans doute celle de l'Ex. 14 (« intervalles
  sur lesquels f est continue ») — noté tel quel ; (2) l'exercice imprimé « 16 » en colonne gauche p.61 est
  à la place du n° 10 (à renuméroter 10 à l'adaptation ?) ; (3) Ex. 20 et 27 (« étudier les variations ») et
  Ex. 20 c) / 22 (unicité) supposent un outil de variation (dérivée, chapitre 4) ; (4) IV Act. 1 : l : [0, π/2[
  → [0,1] n'est pas surjective (piège voulu ou coquille pour [0,1[ ?) ; (5) l'Exemple de continuité de h o u
  (p.51) parle d'« intervalles ouverts I et J » mais conclut sur des intervalles fermés ]−∞, 1] et [4, +∞[.

## 2.4 Chapitre 4 — Dérivation – primitives (manuel 222472, p.65–86)

**Page de garde (p.65)** — « Chapitre 4 » ; titre : « DERIVATION - PRIMITIVES ». Plan imprimé :
« I . Dérivabilité - Rappels · II . Fonctions dérivées - Opérations sur les fonctions dérivables ·
III. Théorème des accroissements finis · IV . Dérivée seconde - Point d'inflexion · V . Primitives ».
Portrait et légende : « Gottfried Wilhelm Leibniz (Leibzig [sic] 1646-Hanovre 1716) — Newton et Leibniz
font naissance du calcul différentiel et primitives » [sic, tournure imprimée].

**Plan du chapitre** (bandeau « Cours », numérotation des activités recommencée dans chaque partie et
dans chaque rubrique « préliminaires » / « de découverte ») :

- **I. Dérivabilité - Rappels** (p.66–68) : Activités préliminaires 1–2 (p.66) ; « A retenir » (p.67) ;
  « Applications » 1–4 (p.68).
- **II. Fonction dérivée - Opérations sur les fonctions dérivables** (p.68–71) : Activités préliminaires
  1–2 (p.68–69) ; Activités de découverte 1–2 (p.69) ; « A retenir » + tableau des dérivées (p.70–71) ;
  Applications 1–3 (p.71).
- **III. Théorème des accroissements finis** (p.72–74) : Activités préliminaires 1–4 (p.72–73) ;
  « A retenir » (p.73) ; Applications 1–4 (p.74).
- **IV. Dérivée seconde - Point d'inflexion** (p.74–75) : définition + Exemples, une Activité (p.74) ;
  « A retenir » (p.74) ; Applications 1–2 (p.75).
- **V. Primitives** (p.75–77) : Activité préliminaire (mobile, sans numéro, p.75) ; Activités de
  découverte 1–4 (p.75–76) ; « A retenir » (p.76) ; tableau « Primitives de fonctions usuelles »
  (p.76–77) ; « Formules pratiques pour la recherche des primitives » (p.77) ; Applications 1–2 (p.77).
- **Apprendre à chercher** (p.78) : Situations 1–3 (+ une « Application » dans la Situation 2).
- **Avec l'outil informatique** (p.79) : programme Pascal « Derivation ».
- **Exercices et problèmes** (p.80–85) : 28 exercices.
- **Maths et culture** (p.86) : « Gottfried LEIBNIZ (1646-1716) ».
- Pas de QCM/Vrai-Faux en page séparée (un Vrai-Faux et un QCM figurent dans les Applications de I),
  pas d'exercice résolu, pas de « Tout ce qu'on doit savoir ».

### Cours — Activités (une ligne chacune)

**I. Dérivabilité - Rappels — Activités préliminaires**

- **Act. 1** (p.66) : f(x) = x² − 4 ; a) déterminer lim_{x→2} (f(x) − f(2))/(x − 2) et
  lim_{h→0} (f(−1 + h) − f(−1))/h, en déduire que f est dérivable aux points 2 et −1 ; déterminer f′(2) et
  f′(−1) ; b) g : ℝ → ℝ, x ↦ |x² − 1| est-elle dérivable au point 1 ? Justifier ; c) h : ℝ → ℝ, x ↦ √|x|
  est-elle dérivable au point 0 ? Justifier.
- **Act. 2** (p.66) : p : x ↦ |x² − 4| et r : x ↦ √|x − 1|, avec leurs courbes (C_p avec la tangente (T)
  au point d'abscisse 1 ; C_r avec le point B(1, 0)). 1) équation de la tangente T à C_p au point
  d'abscisse 1 ; 2) a) p non dérivable en 2 ; b) nombres dérivés à droite et à gauche de p en 2 ;
  c) équations des deux demi-tangentes à C_p au point A d'abscisse 2 et les construire ; 3) a) r est-elle
  dérivable à droite en 1 ? à gauche en 1 ? b) existe-t-il une demi-tangente à C_r au point B d'abscisse 1 ?

**II. Fonction dérivée - Opérations — Activités préliminaires**

- **Act. 1** (p.68) : par la formule f′(x) = lim_{h→0} (f(x + h) − f(x))/h, fonction dérivée de
  f(x) = √(2x − 1) ; g(x) = −3/x ; h(x) = √(x − 3) ; k(x) = x² − 3x + 1.
- **Act. 2** (p.68–69) : par les théorèmes (somme, produit, quotient…), f′(x) pour a) 3x⁴ − 2 sin x ;
  b) 1/x + cos 2x − 3 ; c) (x − 2)√x ; d) (2x − 1)/(3x + 5) ; e) √(4x + 1) ; f) (x² − 1)³.

**II. — Activités de découverte**

- **Act. 1** (p.69) : f(x) = x², g(x) = (2x − 1)/(x + 1), h(x) = (2x² − 1)/(x² + 1). a) vérifier h = g∘f ;
  b) calculer f′(x), g′(x), h′(x) puis g′(f(x)) ; c) vérifier (g∘f)′(x) = g′(f(x)) × f′(x) ; d) montrer que
  l'égalité reste vraie pour f(x) = 2x, g(x) = sin x ; e) appliquer c) à h(x) = √(f(x)), f dérivable et
  strictement positive sur I.
- **Act. 2** (p.69) : 1) f : ℝ₊ → ℝ₊, x ↦ x² et f⁻¹ : ℝ₊ → ℝ₊, x ↦ √x ; a) f′(x) et (f⁻¹)′(x) pour x ≠ 0 ;
  b) f′(2) × (f⁻¹)′(4) et f′(3) × (f⁻¹)′(9) ; c) pour tout a ≠ 0, f′(√a) × (f⁻¹)′(a) ; que remarque-t-on ? 2) f bijection de I sur J (schéma I ⇄ J, x = f⁻¹(y), y = f(x)), dérivable sur I ; on admet que si
  f′(x) ≠ 0 alors f⁻¹ est dérivable en y = f(x) ; a) (f⁻¹∘f)(x) = x ; b) en déduire (f⁻¹)′(y) = 1/f′(x) ;
  c) x ∈ J tel que (f⁻¹)′(x) existe : (f⁻¹)′(x) = 1/f′(f⁻¹(x)).

**III. Théorème des accroissements finis — Activités préliminaires**

- **Act. 1** (p.72) : deux courbes : f(x) = −x² + 6x − 5, 1 ≤ x ≤ 4 (corde [AB], A(1, 0), B(4, 3)) et
  g(x) = x² si 1 ≤ x ≤ 2, g(x) = x² − 6x + 12 si 2 ≤ x ≤ 3 (points C(1, 1), E(2, 4), D(3, 3)). a) f continue et
  dérivable sur [1,4] ; b) g dérivable en 2 ? c) pente p₁ de (AB), pente p₂ de (CD) ; d) il existe c ∈ [1,4]
  tel que f′(c) = p₁ ; e) tracer la tangente à (C_f) au point d'abscisse c ; f) f(4) − f(1) = 3f′(c) ;
  g) existe-t-il x ∈ [1,2] (puis x ∈ [2,3]) tel que g′(x) = p₂ ? Interpréter graphiquement. Conclusion
  imprimée : « Plus généralement on admet que si f est une fonction continue sur [a,b] est [sic] dérivable
  sur ]a,b [, alors il existe c ∈ [a,b] [sic, intervalle fermé] tel que : f(b) - f(a) = (b - a) f'(c) ».
- **Act. 2** (p.72) : a) f : [0, π/2] → ℝ, f(x) = sin x ; a < b dans [0, π/2] : il existe c ∈ ]a,b[ tel que
  sin b − sin a = (b − a)cos c ; en déduire (b − a)cos b ≤ sin b − sin a ≤ (b − a)cos a ; b) pour tous
  réels a et b, |sin b − sin a| ≤ |b − a|. Texte de transition imprimé : « Plus généralement l'égalité
  f(b) - f(a) = (b - a)f '(c) s'écrit (f(b) - f(a))/(b - a) = f '(c) et dans le cas où f '(x) est bornée par
  deux réels m et M sur ]a,b[ , on a alors m ≤ (f(b) - f(a))/(b - a) ≤ M. De plus si, pour tout x ∈ ]a,b[,
  on a |f '(x)| ≤ k , alors |f(b) - f(a)| ≤ k|b - a |. »
- **Act. 3** (p.72–73) : f continue sur [a,b], dérivable sur ]a,b[ ; avec (f(b) − f(a))/(b − a) = f′(c),
  c ∈ ]a,b[ : montrer que f′(x) > 0 sur ]a,b[ ⇒ f strictement croissante sur [a,b] ; sens de variation si
  f′ ≥ 0, f′ ≤ 0, f′ < 0, f′ = 0 sur ]a,b[.
- **Act. 4** (p.73) : a) f dérivable sur I, a ∈ I, maximum local en a (« f(x) ≤ f(a) sur un voisinage de
  a ») : montrer f′_g(a) ≥ 0 et f′_d(a) ≤ 0, en déduire f′(a) = 0 ; de même pour un minimum local ;
  b) réciproquement, on admet que si f′(x) s'annule en a en changeant de signe, f présente en a un extrémum
  local.

**IV. Dérivée seconde - Point d'inflexion**

- **Exemples** (p.74) : f(x) = x² − 3x + 4 → f′(x) = 2x − 3 → f″(x) = 2 ; f(x) = sin(2x) → f′(x) = 2cos(2x)
  → f″(x) = −4sin(2x) ; f(x) = 1/x → f′(x) = −1/x² → f″(x) = 2/x³.
- **Activité** (p.74) : courbe de f(x) = x³ − 3x² + 5 ; a) équation de la tangente Δ à (C_f) au point
  A(1,3) ; b) position de Δ et de (C_f) au voisinage de A — texte : « On remarque que la tangente à la
  courbe (C_f) au point A(1,3) **traverse** la courbe. On dit que le point A est **un point d'inflexion**
  de (C_f) » ; c) calculer f″(x), tableau de signe de f″(x) ; que remarque-t-on ?

**V. Primitives**

- **Activité préliminaire** (p.75) : un mobile a la vitesse v(t) = 2t + 1 ; x(0) = 2 ; donner x(t).
- **Act. 1** (découverte, p.75) : F′(x) = x² − 2x + 5, x ∈ ℝ ; déterminer F(x) sachant que la courbe de F
  passe par A(3,0). Texte qui suit : « La fonction x : t ↦ x(t) = t² + t + 2 admet la fonction v : t ↦
  v(t) = 2t + 1 comme fonction dérivée. On dit que la fonction x est une **primitive** de la fonction v.
  De même, dans l'activité 1, la fonction F est une primitive de la fonction f : x ↦ x² - 2x +5 ».
- **Act. 2** (p.75) : f admet sur I une primitive F ; 1) pour tout λ ∈ ℝ, G(x) = F(x) + λ est une
  primitive de f ; 2) H autre primitive : calculer (H − F)′(x) ; conclure.
- **Act. 3** (p.76) : f(x) = cos 2x sur [0, π] ; a) expression générale d'une primitive :
  F(x) = ½ sin 2x + λ ; b) λ pour que F(π/2) = 1.
- **Act. 4** (p.76) : F, G primitives de f, g sur I ; H(x) = αF(x) + βG(x) ; déterminer H′(x) ; forme
  générale d'une primitive de αf + βg.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Dérivabilité en un point** (p.67) — « •Une fonction f définie sur un intervalle ouvert I
> est dite dérivable en x₀ ∈ I si : lim_{x→x₀} (f(x) − f(x₀))/(x − x₀) = ℓ (Limite finie) •Le réel ℓ est
> appelé nombre dérivé de f en x₀ ou dérivée de f en x₀ et est noté f '(x₀). • Autrement dit f '(x₀) =
> lim_{h→0} (f(x₀ + h) − f(x₀))/h »

> **Dérivabilité à droite et dérivabilité à gauche en un point** (p.67) — « •Une fonction définie sur un
> intervalle du type [x₀ ,a[ (x₀ <a) est dérivable à droite en x₀ si : lim_{x→x₀⁺} (f(x) − f(x₀))/(x − x₀)
> = ℓ (Limite finie) Cette limite est appelée dérivée à droite de f en x₀ et est notée : f 'd (x₀)
> •Une fonction définie sur un intervalle du type ]a,x₀] (a < x₀) est dérivable à gauche en x₀ si :
> lim_{x→x₀⁻} (f(x) − f(x₀))/(x − x₀) = ℓ (limite finie) Cette limite est appelée dérivée à gauche de f en
> x₀ et est notée: f 'g (x₀) •Une fonction f est dérivable en x₀ si et seulement si elle est dérivable à
> droite en x₀ , à gauche en x₀ et f 'd (x₀) = f 'g(x₀) »

> **Théorème (admis)** (p.67) — « Toute fonction dérivable en un point x₀ est continue en x₀. »

> **Equation cartésienne de la tangente** (p.67) — « •Si f est dérivable au point x₀ , alors sa courbe
> représentative admet une tangente au point M₀ (x₀,f(x₀)) qui a pour équation : y = f '(x₀)(x − x₀) + f(x₀)
> •Si f est dérivable à droite (resp. à gauche) en x₀, alors sa courbe représentative admet une demi -
> tangente à droite (resp. à gauche) au point M₀(x₀, f(x₀)) d'équation : { y = f 'd(x₀)(x − x₀) + f(x₀) ;
> x ≥ x₀ } (resp. { y = f 'g(x₀)(x − x₀) + f(x₀) ; x ≤ x₀ }) »

> **Dérivabilité sur un intervalle** (p.67) — « • Lorsqu'une fonction f admet un nombre dérivé en tout
> point x₀ d'un intervalle ouvert I, on dit que f est dérivable sur I . • Lorsque f est dérivable sur
> ]a,b[, dérivable à droite en a et à gauche en b, on dit que f est dérivable sur [a,b] . De la même
> manière on définit la dérivabilité d'une fonction f sur [a,b[ ; ]a,b] ; [a, +∞ [ ; ] −∞ ,a ],... »

> **A retenir — Fonction dérivée** (p.70) — « f étant une fonction dérivable sur un intervalle I, la
> fonction dérivée de f notée f ' est la fonction définie sur I et qui à tout réel x de I, associe f ' (x) »

> **Opérations sur les fonctions dérivables** (p.70) — « • f et g étant deux fonctions dérivables sur un
> intervalle I et λ un réel, les fonctions λ f, f + g et fg sont dérivables sur I et l'on a : (λ f)'(x) =
> λ f '(x) ; (f+g)'(x) = f'(x)+g'(x) ; (fg)'(x)=f '(x)g(x)+f(x)g'(x) •En tout point x de I tel que
> g(x) ≠ 0, 1/g et f/g sont dérivables en x et l'on a: (1/g)'(x) = −g'(x)/(g(x))² ;
> (f/g)'(x) = (f '(x)g(x) − f(x)g'(x))/(g(x))² • Si f est dérivable en x et g est dérivable en f(x), alors
> gof est dérivable en x et l'on a : (gof)' (x) = g'(f(x)) x f '(x) •Si f(x) est strictement positif, alors
> √f est dérivable en x et l'on a: (√f)'(x) = f '(x)/(2√f(x)) •Si f admet une fonction réciproque f ⁻¹ et
> si f '(x) ≠ 0 alors f ⁻¹ est dérivable au point f(x) et on a: (f⁻¹)'(f(x)) = 1/f '(x) , autrement dit ,
> (f⁻¹)'(y) = 1/f '(f⁻¹(y)) »

> **Tableau des dérivées** (p.70–71 ; « Le tableau suivant présente quelques formules utiles pour le calcul
> des dérivées et les dérivées de quelques fonctions usuelles. ») — f(x) → f′(x) :
> aU(x)+bV(x) (a ∈ ℝ et b ∈ ℝ) → aU'(x)+bV'(x) ; U(x)V(x) → U'(x)V(x)+ U(x)V'(x) ; U(x)/V(x) →
> (U'(x)V(x) − U(x)V'(x))/[V(x)]² ; 1/V(x) → −V'(x)/[V(x)]² ; (UoV)(x) → U'[V(x)]V'(x) ; √U(x) →
> U'(x)/(2√U(x)) ; [U(x)]ⁿ → n (U(x))ⁿ⁻¹ U'(x) ; ax+b → a ; 1/x → −1/x² ; (ax + b)/(cx + d) →
> (ad − bc)/(cx + d)² ; √x → 1/(2√x) ; √(ax + b) → a/(2√(ax + b)) ; sin(ax+b) → acos(ax+b) ;
> cos(ax+b) → − asin(ax+b) ; tan(ax+b) → a[1+tan²(ax+b)].

> **A retenir — Théorème des accroissements finis** (p.73, figure : courbe entre A(a, f(a)) et B(b, f(b)),
> tangentes parallèles à (AB) en deux points, un seul étiqueté c) — « Si f est une fonction continue sur [a,b] et dérivable sur
> ]a,b[, alors il existe au moins un réel c ∈ ]a,b[ tel que f(b) - f(a) = (b - a)f '(c). »

> **Inégalité des accroissements finis** (p.73) — « Soit f une fonction continue sur [a,b] (a < b) et
> dérivable sur ]a,b[. On suppose qu'il existe deux réels m et M tels que m ≤ f '(x) ≤ M pour tout
> x ∈ ]a,b[. On a alors: m ≤ (f(b) - f(a))/(b - a) ≤ M »

> **Corollaire** (p.73) — « Soit f une fonction dérivable sur un intervalle I. On suppose qu'il existe un
> réel k strictement positif tel que |f '(x)| ≤ k pour tout x ∈ ]a,b[ [sic : « ]a,b[ » alors que
> l'hypothèse porte sur I]. On a alors |f(b) - f(a)| ≤ k|b - a| pour tous réels a et b de I »

> **Dérivée et sens de variation** (p.73) — « Soit f une fonction dérivable sur un intervalle I et f ' sa
> fonction dérivée, alors : • f est croissante (resp. décroissante) sur I si et seulement si f ' ≥ 0 ( resp.
> f ' ≤ 0) • f est strictement croissante(resp.strictement décroissante) sur I si et seulement si f ' > 0
> (resp. f ' < 0 ). • f est constante sur I si et seulement si f ' = 0 » (⚠ la 2ᵉ puce est fausse comme
> équivalence — x ↦ x³ — voir doutes.)

> **Extrémum d'une fonction** (p.73) — « Soit f une fonction dérivable sur un intervalle I et a ∈ I Si f
> présente un extrémum local au point a, alors f '(a) = 0. Si f '(x) s'annule en a en changeant de signe,
> alors f présente en a un extrémum local. »

> **Dérivée seconde** (p.74 ; la 1ʳᵉ phrase « Soit f … dérivable sur I » est l'introduction hors cadre, seules
> les deux lignes « On appelle … (f ')'(x ). » sont dans le cartouche bleu) — « Soit f une fonction dérivable sur un intervalle ouvert I. On
> suppose que f ' est dérivable sur I — On appelle dérivée seconde de f et on noté [sic] f " la fonction
> dérivée de f ' . Pour tout x de I f"(x)=(f ')'(x ). »

> **A retenir — Point d'inflexion** (p.74) — « f étant une fonction deux fois dérivable sur un intervalle I
> et x₀ un réel appartenant à I, le point M₀ (x₀ , f(x₀ )) est un point d'inflexion de (C_f ) si et
> seulement si f"(x) s'annule et change de signe en x₀ »

> **A retenir — Primitives** (p.76) — « **Définition** f étant une fonction définie sur un intervalle I. On
> appelle primitive de f toute fonction F dérivable sur I et telle que F'(x) = f(x) , x ∈ I
> **Théorème (admis)** Toute fonction définie et continue sur un intervalle I, admet une primitive sur I.
> **Théorème** Soit f une fonction définie et continue sur un intervalle I et admettant une primitive F sur
> I. Alors toute autre primitive G de f sur I est de la forme G(x) = F(x) + λ où λ est une constante.
> **Corollaire** Soit f une fonction continue sur un intervalle I, x₀ ∈ I et y₀ ∈ ℝ. Il existe une unique
> primitive F de f telle que F(x₀) = y₀. **Théorème** Si f et g sont deux fonctions définies sur un
> intervalle I, F et G leurs primitives respectives, alors pour tous réels α et β , la fonction αF + βG est
> une primitive de αf + βg. »

> **Primitives de fonctions usuelles** (p.76–77 ; colonnes Fonction f / Fonction primitive F / Intervalle I)
> — f(x) = k (constante) → F(x) = kx + c, ℝ ; f(x) = ax + b → F(x) = ½ ax² + bx + c, ℝ ; f(x) = 1/x² →
> F(x) = −1/x + c, ]0 ; +∞[ ou ]−∞ ; 0[ ; f(x) = xⁿ (n ∈ ℕ*) → F(x) = xⁿ⁺¹/(n + 1) + c, ℝ ; f(x) = xⁿ
> (n ∈ ℤ*₋ et n ≠ −1) → F(x) = xⁿ⁺¹/(n + 1) + c,
> ]−∞ ; 0[ ou ]0 ; +∞[ ; f(x) = 1/√x → F(x) = 2√x + c, ]0 ; +∞[ ; f(x) = cos x → F(x) = sin x + c, ℝ ;
> f(x) = sin x → F(x) = −cos x + c, ℝ ; f(x) = 1 + tan² x = 1/cos² x → F(x) = tan x + c,
> ]−π/2 + kπ ; π/2 + kπ[ ; f(x) = cos(ax + b), a ≠ 0 → F(x) = (1/a) sin(ax + b) + c, ℝ ;
> f(x) = sin(ax + b), a ≠ 0 → F(x) = −(1/a) cos(ax + b) + c, ℝ ; f(x) = √x → F(x) = (2/3)x√x + c, ℝ₊.

> **Formules pratiques pour la recherche des primitives** (p.77 ; « Lorsque u et v sont des fonctions
> continues sur un intervalle I » ; colonnes Fonction / Une primitive / Conditions) — u' + v' → u + v ;
> λ.u' (λ : constante) → λu ; u' uⁿ (n ∈ ℤ et n ≠ −1) → uⁿ⁺¹/(n + 1), « u ≠ 0 dans le cas n ≤ −2 » ;
> u'/√u → 2√u, « u > 0 sur I » ; v'/v² → −1/v, « v ≠ 0 sur I » ; (u'ov).v' → uov.

### Applications (exercices d'application du cours, une ligne chacune)

- **I.1** (p.68) Vrai/faux : a) dérivable en x₀ ⇒ continue en x₀ ; b) continue ⇒ dérivable ; c) non continue
  ⇒ non dérivable ; d) dérivable à droite et à gauche ⇒ dérivable ; e) dérivable ⇒ dérivable à droite ;
  f) tangente au point M₀(x₀, f(x₀)) ⇒ f dérivable en x₀. (Réponses non fournies.)
- **I.2** (p.68) : dérivabilité à droite, à gauche et en 1 de a) f(x) = −2 si x < 1, x − 1 si x ≥ 1 ;
  b) 0 si x < 1, x − 1 si x ≥ 1 ; c) 0 si x < 1, (x − 1)² si x ≥ 1.
- **I.3** (p.68) : f(x) = √(1 + x²) dérivable en 0.
- **I.4** (p.68) QCM « Trouver la (ou les) réponse(s) exacte(s) » : f(x) = x³ − x² + 1, repère orthonormé ;
  a) tangente en A(1,1) : y = −x + 1 / y = x / y = x + 1 ; b) pente de la tangente en B d'abscisse −2 :
  ☐ −1 ☐ 21 ☐ 16 ; c) vecteur directeur de la tangente en C d'abscisse −1 : u⃗₁(1 ; 5), u⃗₂(1 ; −5),
  u⃗₃(−1 ; −5), u⃗₄(2 ; 10) ; • x ↦ |x − 2| est dérivable sur ☐ ℝ ☐ ]−∞, 2[ ☐ [2, +∞[. (Sans corrigé.)
- **II.1** (p.71) : ensemble de définition de f et de f′, et f′(x) : a) (2x + 3)/(x − 1) ; b) (2x + 3)/(x² − 2x − 2) ;
  c) 1/√(x² − 4) ; d) √(x² + 2x − 3) ; e) (3x + 2)⁴ ; f) ((2x − 1)/(x − 3))³ ; g) √(x² + 1)/x ;
  h) cos(2x − π/3) ; i) sin²(3x) ; j) √((x + 1)/(x − 1)) ; k) tan(2x) ; l) √(1 + cos x) ;
  m) (1 + sin x)/(1 − sin x) ; n) 1/(x√x).
- **II.2** (p.71) : f : [0, π/2] → ℝ, x ↦ sin x ; a) f admet une bijection réciproque ; b) ensembles de
  définition de f⁻¹ et de (f⁻¹)′ ; c) f(0) et f(π/4), en déduire (f⁻¹)′(0) et (f⁻¹)′(√2/2).
- **II.3** (p.71) : schéma (repère, droite y = x, courbe bleue (C_f) partant de (2, 0) avec tangente
  verticale, courbe rose symétrique partant de (0, 2) avec tangente horizontale) : f dérivable en 2 ? f⁻¹
  dérivable en f(2) ? Que peut-on conclure ?
- **III.1** (p.74) : f(x) = x² + 2x³ ; réels c vérifiant f(b) − f(a) = (b − a)f′(c) pour a = 1, b = −3 et
  a = 0, b = 2.
- **III.2** (p.74) : TAF pour f(x) = x⁴ + x² − 2x + 5, a = −1, b = 1 ; a) −10 ≤ f′(x) ≤ 2 sur [−1,1] ;
  b) en déduire −10x − 1 ≤ f(x) ≤ 2x + 11 pour x ∈ ]−1,1[.
- **III.3** (p.74) : IAF pour x ↦ cos x sur un intervalle choisi : |cos b − 1| ≤ |b| pour tout réel b.
- **III.4** (p.74) : f(x) = (1/3)x³ − (3/2)x² + 2x + 1 ; variations et point(s) « ou » [sic, pour où] f
  présente un extrémum.
- **IV.1** (p.75) : trois courbes (parabole de sommet A ; courbe à maximum local A avec flèches ; courbe
  croissante avec tangente verticale en A) : A est-il un point d'inflexion ?
- **IV.2** (p.75) : point(s) d'inflexion de a) x³ − x + 1 ; b) (x + 1)⁴ ; c) x² − 5x + 6.
- **V.1** (p.77) : une primitive F de a) (2x + 1)/(x² + x + 2)² ; b) 3/√(2x − 1) ; c) x³ + 2x − 5 ;
  d) 10x⁴ + 6x³ − 1 ; e) (2x)(x² + 1)³ ; f) −3/(2x + 5)² ; g) 1/(2√x) + 4 ; h) 4/√(x − 5) ;
  i) (4x − 6)(x² − 3x + 1) ; j) 1/x² + sin x ; k) (3x² + 5)(x³ + 5x − 2)² ; l) sin x cos² x ; m) (3x − 1)⁴ ;
  n) 4x − 3/x².
- **V.2** (p.77) : f(x) = x/√(x² + 1) sur ℝ ; primitive F telle que F(0) = 2.

### Apprendre à chercher (p.78)

- **Situation 1** : trapèze ABCD, AB = 1, BC = AD = 1, CD variable, x = CH (H projeté orthogonal de B sur
  [CD]) ; 1) aire = (1 + x)√(1 − x²) (« On pourra décomposer sa surface en un rectangle et deux
  triangles ») ; 2) f(x) = (1 + x)√(1 − x²) : a) ensemble de définition ; b) f′(x) = (−2x² − x + 1)/√(1 − x²),
  variations sur [0,1] ; c) x pour lequel l'aire est maximale.
- **Situation 2** : f(x) = √(1 + x) ; 1) f(o) et f′(o) [sic, lettre o pour 0] ; 2) g(x) = f(x) − [f(0) + xf′(0)] :
  a) g(x) en fonction de x ; b) g(x) = −x²/(2(2√(1 + x) + 2 + x)) ; c) pour x positif,
  8 ≤ 2(2√(1 + x) + 2 + x) ; d) « En déduire que tout réel x positif » [sic, « pour » manquant] :
  −x²/8 ≤ √(1 + x) − (1 + x/2) ≤ 0. **Application** : sans calculatrice, valeur approchée à 10⁻² près de √1,2.
- **Situation 3** : f(x) = (2x³ + 5x² − 4x − 11)/(x + 2)² sur ℝ \ {−2} ; on cherche a, b, c tels que
  f(x) = ax + b + c/(x + 2)² ; 1) lim_{x→+∞} f(x)/x → a ; 2) g(x) = (x + 2)² f(x) sous deux expressions,
  lim_{x→−2} g(x) → c ; 3) f(o) [sic] de deux manières → b ; 4) une primitive de f.

### Avec l'outil informatique (p.79)

« On souhaite évaluer f '(x₀) en calculant le taux d'accroissement de f entre x₀ et x₀+h et à faire tendre
h vers 0. On va l'appliquer à la fonction f(x) = √x » — programme Pascal `program Derivation; uses wincrt;
const IterMax=20;` avec `function f(x:real):real; begin f:=sqrt(x) end;` et
`function fprime(x:real):real; begin fprime:=1/(2*sqrt(x)) end;` ; saisie de nbiter (« Nombre d''itération
compris entre 0 et 15 » alors que `IterMax=20` [sic, incohérence]), de x0 et de h > 0 (« valeur initial »
[sic]) ; boucle `for k:=1 to nbiter do begin fp:= (f(x0+h)-f(x0))/h; write(h:10:10,' ',fp:16:16);
writeln; h:=h/2; end`. Aucun tableau de résultats imprimé, aucune question.

### Exercices et problèmes (p.80–85) — 28 exercices

- **Ex. 1** (p.80) : f(x) = x² − 2x + 2 si x < 2 ; 2 si x ≥ 2 ; 1) continue en tout point de ℝ ? 2) dérivable
  en tout point de ℝ ?
- **Ex. 2** (p.80) QCM (« Une et une seule est exacte. On demande de l'entourer ») : courbe (C) de f dérivable
  sur ℝ, (T) tangente en A d'abscisse 1 (A(1, 2), (T) passe par (0, 3) et (3, 0)), y = 0 asymptote en +∞,
  tangente horizontale en x = 0 ; 1) a. f(0) = 0 b. f′(0) = 2 c. f′(0) = 0 d. f(2) = 0 ; 2) f′(1) : a. 0
  b. 1 c. −1 d. −2.
- **Ex. 3** (p.80) oui/non avec démonstration ou contre-exemple : 1) continue en 0 ⇒ dérivable en 0 ? 2) dérivable en 0 ⇒ continue en 0 ? 3) f′(0) = 0 ⇒ extremum en 0 ? 4) f continue sur [0, 1], dérivable
  sur ]0, 1[, maximum en 1 ⇒ f′(1) = 0 ?
- **Ex. 4** (p.80) : 1) f(x) = 4x² − 3x + 1, x₀ = 2 : nombre dérivé par la définition, équation de la
  tangente ; 2) mêmes questions pour a) (x − 1)/(x + 1), x₀ = 2 ; b) √(1/x), x₀ = 1/4.
- **Ex. 5** (p.80–81) : courbe de f (quadrillage ; minimum en −2, flèches de tangentes en −2, 0 et 1) ; 1) compléter f(0), f(−2), f(1), f′(0), f′(−2), f′(1) ; 2) équation de la tangente en x₀ = 1.
- **Ex. 6** (p.81) QCM « Trouver la (ou les) réponse(s) exacte(s) » : 1) droite passant par A(1 ; 2), de
  coefficient directeur −3 : a) y = −3x + 5 b) 6x + 2y − 10 = 0 c) y = 2x − 3 ; 2) f(x) = x³ − x, pente de
  (AB) (abscisses 1 et 2) : a) 5 b) 1 c) 6 ; 3) g(x) = x² + 1, pente de la tangente en M d'abscisse x :
  a) x − 2 b) 2x c) x/2 ; 4) lim_{h→0} (√(2 + h) − √2)/h : a) 0 b) +∞ c) 1/(2√2).
- **Ex. 7** (p.81) : dérivée en x₀ de 1) (1 − 2x²)/(1 + x²), x₀ = 1 ; 2) (1 + √x)/(1 − √x), x₀ = 9 ; 3) √(x² + x + 1), x₀ = 0.
- **Ex. 8** (p.81–82) : C_f sur [0;6], A(−2;0), B(1;5), (AB) tangente à C_f en B ; 1) f′(1) ; 2) laquelle de
  deux courbes (une p.81, une p.82) représente f′ (justifier) ; 3) g(x) = √(f(x)) sur [0 ; 6] : g′ à l'aide de
  f et f′, calculer g′(1).
- **Ex. 9** (p.82) : C : f(x) = x² + 6x + 5, A(−1,0) ; 1) droite D_m par A de coefficient directeur m ; 2) m tel que D_m ∩ C soit un singleton, coordonnées du point ; 3) D_m est alors tangente à C.
- **Ex. 10** (p.82) : courbe C_f (en W, minima vers ±1, maximum local en 0, flèches horizontales) :
  a) tableau de signe de f ; b) tableau de variation ; c) tableau de signe de f′ en justifiant ; d) résoudre
  f′(x) = 0.
- **Ex. 11** (p.82) : ensemble de définition, ensemble de dérivabilité et dérivée : a) x² − 1/x ;
  b) (2x + 3)√(3x⁵) ; c) (x² + 7)/(x² − x − 6) ; d) 1/(5x² − 3)³ ; e) (2x³ + 3x − 1)⁴ ; f) √(x⁴ + x² + 1) ;
  g) sin(1/x).
- **Ex. 12** (p.82) : g(x) = 2x³ + x − 1 ; 1) variations ; 2) g(x) = 0 a une solution unique α, valeur
  approchée à 10⁻¹ ; 3) signe de g, variations de f : x ↦ √(x⁴ + (x − 1)²).
- **Ex. 13** (p.82–83) : f(x) = (x + 2)/(x − 1) sur ℝ − {1} ; 1) f′(x) ; 2) en déduire les dérivées de
  g(x) = (√x + 2)/(√x − 1), h(x) = √((x + 2)/(x − 1)), k(x) = (x² + 2)/(x² − 1), l(x) = (cos x + 2)/(−1 + cos x).
- **Ex. 14** (p.83) : f(x) = x³ + x + 1 ; a) bijection de ℝ vers ℝ ; b) f⁻¹ dérivable sur ℝ ; c) f(1), f(−2),
  en déduire (f⁻¹)′(3), (f⁻¹)′(−9).
- **Ex. 15** (p.83) : f(x) = tan x sur [0, π/2[ ; a) fonction réciproque ; b) ensemble de définition et de
  dérivabilité de f⁻¹ ; c) « Montrer que pour tout x de ℝ » (f⁻¹)′(x) = 1/(1 + x²) [sic : f⁻¹ n'est définie
  que sur [0, +∞[].
- **Ex. 16** (p.83) : f : x ↦ √x ; a) 1/21 ≤ f′(x) ≤ 1/20 si x ∈ [100,101] ; b) 10,047 ≤ √101 ≤ 10,05.
- **Ex. 17** (p.83) : f sur [0, π/4], « f : x = tanx » [sic] ; a) 1 ≤ f′(x) ≤ 2 pour x ∈ [0, π/4] ;
  b) x ≤ tan x ≤ 2x sur [0, π/4].
- **Ex. 18** (p.83–84) : f dérivable sur [−3/2 ; 3], courbe passant par A(1,1), B(0,2), C(2,0), E(−3/2,−3),
  D(3,2) ; tangentes horizontales en B et C ; Δ tangente en A passant par J(3 ; −2) ; 1) a) f′(0), f′(1),
  f′(2) ; b) équation de Δ ; 2) nombre de solutions de f(x) = 1 sur [−3/2 ; 3] (graphique) ; 3) f est la
  dérivée d'une fonction F sur [−3/2 ; 3] : sens de variation de F ; 4) on pose f′(x) = ax(x − 2) :
  a) déterminer a (avec 1.a) ; b) vérifier f′(x) = (3/2)x² − 3x ; déterminer f(x) sur [−3/2 ; 3].
- **Ex. 19** (p.84) : artisan, coût C(x) = x² + 60x + 121, x ∈ [1 ; 30] ; Cm(x) = C(x)/x ; a) C′m, signe,
  tableau ; b) nombre d'objets pour un coût moyen minimal ; c) vente 110 D l'objet : B(x) = −x² + 50x − 121,
  signe de B′, tableau, bénéfice maximal.
- **Ex. 20** (p.84) : f(x) = (|x − 1| + x)/(x² − 1) ; a) continuité sur ℝ [sic, f non définie en ±1] ;
  b) expression sans valeurs absolues ; c) i) dérivabilité sur ℝ, f′(x) selon x ; ii) tableau de variation.
- **Ex. 21** (p.84) : 1) f(x) = ax³ + bx² + cx + d, (C) passe par A(1,8), B(0,3), D(2,9) et admet en B une
  tangente parallèle à y = 5x : a, b, c, d ; 2) g(x) = −x³ + x² + 5x + 3, courbe Γ ; a) tableau de variation
  sur ℝ ; b) g(x) = (x + 1)²(3 − x), signe de g ; c) tangente T à Γ en x₀.
- **Ex. 22** (p.84–85) « Détermination d'une aire maximale des lunules » : figure (cercle de diamètre [AB],
  M sur [AB], deux demi-disques noirs) ; AB = 10 ; l = AM ; A = (π/4)(L² − 10L + 50) [sic, L majuscule pour
  l] ; 1) aire pour l = 4 (« Calcùler » [sic]) ; 2) f(x) = x² − 10x + 50 sur [0 ;10] : a) f′ ; b) f′(x) = 0 ;
  c) tableau ; position de M donnant l'aire maximum, et cette aire.
- **Ex. 23** (p.85) : N(t) = 10⁴(72 − 2t)² microbes/mL, « où t ≥ 10 » [?, borne imprimée telle quelle] ;
  a) temps d'élimination totale ; b) taux de variation à 12 h ; c) taux moyen de variation à la quinzième heure.
- **Ex. 24** (p.85) : une primitive sur un intervalle choisi : a) x³ − 2x + 1 ; b) x + 1/√x ; c) sin x − 2 cos x ;
  d) 1/x² − x² ; e) 1 − 1/cos²x ; g) x/(x² + 2)² ; h) x cos x² ; i) sin 2x − cos 2x ; j) x²(x³ + 2)³ ;
  k) x²/(x³ + 2)³ ; m) sin x/√(cos x + 2) ; n) (√x + 1)²/√x. [sic : pas d'items f) ni l), 12 items.]
- **Ex. 25** (p.85) : f(x) = (x² + 2x)/(x² + x + 1)² ; a) ensemble de définition ; b) a et b tels que
  F(x) = (ax + b)/(x² + x + 1) soit une primitive.
- **Ex. 26** (p.85) : primitive F telle que F(x₀) = y₀ : a) 1 − x + x² − x³, F(1) = 0 ; b) −2 sin 2x,
  F(π/4) = 1 ; c) x + 1/x² − 1/√x, F(1) = 1.
- **Ex. 27** (p.85) : f(x) = (4x − 1)/(2x + 1)³ ; a) a, b tels que f(x) = a/(2x + 1)² + b/(2x + 1)³ sur Df ;
  b) toutes les primitives sur ]−1/2 ; +∞[.
- **Ex. 28** (p.85) : polynôme P avec P′(x) = x² − 5x + 6 dont le maximum relatif est le double du minimum
  relatif.

### Maths et culture (p.86)

« Gottfried LEIBNIZ (1646-1716) » — texte biographique d'une page : grande figure de la civilisation
européenne, machine à calculer, numération binaire, l'un des deux fondateurs de l'Analyse ; venu aux
mathématiques à 26 ans (Paris, 1672) ; dès 1675 (manuscrit du 21 novembre) invente les symboles dx et ∫
(« un S, initiale du mot latin summa, somme ») ; à partir de 1684 publie « dans le [sic] revue qu'il a
fondée à Leipzig, les Acta Eriditorum [sic], les Actes de Erudits » ; « Théorème fondamental de
l'Analyse » ; le mot « fonction » dû à Leibniz ; disciples Jean et Jacques Bernoulli, Marquis de
l'Hospital ; querelle de priorité avec Newton ; travaux sur le binaire, les déterminants, la Logique.

### Écart avec la référence (math-bac-sciences-exp/03-derivabilite + 06-primitives ; et 04-fonctions-reciproques pour (f⁻¹)′)

Correspondance proposée **confirmée**, avec un complément : la dérivée de la réciproque, que ce manuel met
dans ce chapitre (II, Act. 2 + encadré p.70 + App. II.2–3 + Ex. 14–15), est dans la référence au chapitre
sciences-exp/04 (« Dériver la réciproque sans jamais l'expliciter »).

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer à l'adaptation)** :

- le **théorème de Rolle** (section entière de sciences-exp/03 ; aucune occurrence dans p.65–86) ;
- l'**approximation affine** nommée f(a + h) ≈ f(a) + f′(a)h (seule trace : Situation 2 p.78,
  √(1 + x) ≈ 1 + x/2 avec encadrement de l'erreur, sans le mot) ;
- les **dérivées successives / dérivée n-ième** f⁽ⁿ⁾ (ici seulement f″) ;
- la formule (1/fⁿ)′ = −nf′/fⁿ⁺¹ et (1/xⁿ)′ en ligne de tableau (ici [U(x)]ⁿ seulement) ;
- le critère **large** de monotonie (f′ ≥ 0 ne s'annulant sur aucun intervalle ⇒ strictement croissante) et
  le **prolongement aux bornes** ; la **définition formelle** du point d'inflexion (« C_f traverse sa
  tangente ») comme définition séparée du critère f″ (ici, « traverse » est dit en activité, et l'encadré
  donne directement le critère f″ en « si et seulement si ») ; la définition formelle d'extremum local
  (intervalle ouvert J) ;
- pour les primitives : lignes **u′/uⁿ** (forme quotient), **u′√u ↦ (2/3)u√u**, **u′v + v′u ↦ uv**,
  **(u′v − v′u)/v² ↦ u/v** ; la **linéarisation** sin²/cos²/sin³ ; la section « Étudier une primitive sans l'écrire » (signe de f ⇒ variations de F :
  présent seulement en Ex. 18.3) ; les applications physiques à deux remontées (accélération → vitesse →
  position) ; la démonstration de « F − G constante » (ici théorème énoncé, la preuve n'est que l'Act. 2).

**Ce que ce manuel a en plus (ou autrement)** :

- **dérivée de la réciproque** (encadré p.70 : (f⁻¹)′(f(x)) = 1/f′(x)) et applications (sin sur [0, π/2],
  x³ + x + 1, tan avec (f⁻¹)′(x) = 1/(1 + x²)) dans le chapitre de dérivation ;
- **tableau des dérivées** à 15 lignes incluant (ax + b)/(cx + d) → (ad − bc)/(cx + d)² et √(ax + b) ;
- formule de primitive **u′uⁿ pour n ∈ ℤ, n ≠ −1** (une seule ligne couvrant les puissances négatives) et
  **v′/v² ↦ −1/v** ; table usuelle avec **√x ↦ (2/3)x√x** ;
- **Apprendre à chercher** (3 situations : optimisation d'aire d'un trapèze ; encadrement de √(1 + x) et
  valeur approchée de √1,2 ; identification ax + b + c/(x + 2)² par limites, puis primitive) ;
- **décomposition en éléments simples guidée** (forme toujours donnée, coefficients à identifier) :
  ax + b + c/(x + 2)² (Situation 3, p.78), a/(2x + 1)² + b/(2x + 1)³ (Ex. 27, p.85), primitive de la forme
  (ax + b)/(x² + x + 1) (Ex. 25, p.85) — même technique que la référence (06, « Réécrire avant de
  primitiver », ax + b + c/(x − 2)²) : à CONSERVER à l'adaptation ;
- **outil informatique** : programme **Pascal** d'évaluation numérique de f′(x₀) par taux d'accroissement
  (spécifique à la section Sciences de l'informatique) ;
- applications **économiques** (coût moyen, bénéfice, Ex. 19), **biologiques** (microbes, Ex. 23),
  **géométriques** (lunules, Ex. 22 ; tangente comme intersection singleton, Ex. 9), **cinématique**
  (mobile, Act. préliminaire V) ;
- lectures graphiques (Ex. 2, 5, 8, 10, 18), QCM avec **vecteur directeur** de tangente (App. I.4) ;
- IAF appliquée à des **encadrements numériques** (√101, tan x, |sin b − sin a| ≤ |b − a|) — même esprit
  que la référence.

**Vocabulaire / notations propres** : « nombre dérivé » ET « dérivée de f en x₀ » ; f′d(x₀), f′g(x₀) ;
« extrémum » (accent) ; « gof », « UoV », « (u'ov).v' » (o minuscule pour ∘) ; « Dérivée seconde » notée
f" ; constantes d'intégration notées c (tableau) et λ (théorèmes) ; ℝ écrit « IR » ; rubriques « A retenir »,
« Applications », « Apprendre à chercher », « Avec l'outil informatique », « Maths et culture ».

### Bornes de scope

- ✅ INCLUS : nombre dérivé (limite du taux, forme en h), dérivabilité à droite/à gauche, demi-tangentes
  (équation avec x ≥ x₀ / x ≤ x₀), dérivable ⇒ continue (admis), tangente, dérivabilité sur un
  intervalle ; fonction dérivée ; opérations (λf, f + g, fg, 1/g, f/g), composée g∘f, √f, réciproque f⁻¹
  ((f⁻¹)′(y) = 1/f′(f⁻¹(y))) ; tableau des dérivées usuelles (dont (ax + b)/(cx + d), sin/cos/tan(ax + b)) ;
  TAF et IAF (m ≤ (f(b) − f(a))/(b − a) ≤ M, |f(b) − f(a)| ≤ k|b − a|) ; signe de f′ et variations ;
  extrémum local (f′(a) = 0 ; changement de signe) ; dérivée seconde, point d'inflexion par f″ ; primitives
  (définition, existence admise, forme F + λ, unique avec F(x₀) = y₀, linéarité) ; tables de primitives
  usuelles et « formules pratiques » (u′uⁿ, n ∈ ℤ \ {−1} ; u′/√u ; v′/v² ; (u′∘v)·v′) ; identification
  ax + b + c/(x + 2)², a/(2x + 1)² + b/(2x + 1)³, (ax + b)/(x² + x + 1) ; problèmes d'optimisation
  (trapèze, coût moyen, bénéfice, lunule) ; taux de variation instantané/moyen ; évaluation numérique de
  f′(x₀) (Pascal) ; continuité et dérivabilité de fonctions par morceaux / à valeur absolue.
- ⛔ EXCLU : théorème de Rolle ; approximation affine nommée ; dérivées d'ordre n ; convexité/concavité ;
  intégrale, aire sous la courbe, notation ∫ (sauf mention historique p.86) ; ln, exp ; primitives de 1/x,
  u′/u ; intégration par parties ; linéarisation trigonométrique ; Arcsin/Arctan nommées (la réciproque de
  tan apparaît sans nom, Ex. 15) ; racine n-ième ; suites récurrentes (aucun exercice uₙ₊₁ = f(uₙ) ici) ;
  étude complète de fonctions avec branches infinies (chapitre 5).

### Lecture

- **Pages lues en L1 (pdftotext -layout)** : p.65 à p.86, toutes.
- **Pages lues sur l'image (110 dpi)** : p.65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
  82, 83, 84, 85, 86 = **22 pages sur 22** (100 %) ; zooms 250 dpi : p.76 (tableau, ligne xⁿ, n ∈ ℤ*…) et
  p.80 (QCM Ex. 2, choix d).
- **Écarts texte/image constatés** : L1 perd systématiquement les racines (p.68 Act. 1 « 2x − 1 » sans √ ;
  p.66 √|x| et √|x − 1| ; p.71 j), l), n)), les signes moins (p.68 App. I.2 a) « f(x) = 2 » au lieu de −2 ;
  p.81 Ex. 6 « 2 + h − 2 » pour √(2 + h) − √2), les exposants (p.71 tan², p.78 Situation 2) et les
  fractions empilées (tableaux p.70–71, 76–77 totalement désalignés) ; p.80–85 : mise en deux colonnes
  entrelacées par L1 (Ex. 3 mêlé à Ex. 1–2 ; Ex. 18 mêlé à Ex. 14–17 ; Ex. 21–22 mêlés à Ex. 19–20) —
  l'attribution des questions aux exercices a été faite sur l'image ; p.80 Ex. 5 : L1 « f 2 » = image f(−2) ;
  p.79 : les '' du Pascal rendus « " » à l'image (f''(xo) imprimé f"(xo)).
- **Coquilles [sic]** : « Leibzig » (p.65) ; « font naissance du calcul différentiel et primitives » (p.65) ;
  en-tête « Dérivation - promitive » (p.70) ; « continue sur [a,b] est dérivable » et « c ∈ [a,b] » (p.72) ;
  « pour tout x ∈ ]a,b[ » dans le corollaire sur I (p.73) ; « on noté » (p.74) ; « point(s) ou » (p.74) ;
  « f(o) », « f’(o) » (p.78) ; « En déduire que tout réel » (p.78) ; « valeur initial » et « entre 0 et 15 » vs
  IterMax=20 (p.79) ; « f : x = tanx » (Ex. 17) ; « pour tout x de ℝ » (Ex. 15) ; « continuité de f sur ℝ »
  (Ex. 20) ; L vs l et « Calcùler » (Ex. 22) ; Ex. 24 sans f) ni l) ; « le revue », « Acta Eriditorum »,
  « Actes de Erudits » (p.86).
- **Doutes [?] à trancher** : (1) **encadré « Dérivée et sens de variation »** (p.73) : « strictement
  croissante si et seulement si f′ > 0 » est faux en sens réciproque (x³) — à l'adaptation, ne PAS reproduire
  l'équivalence ; garder « si f′ > 0 alors strictement croissante » ; (2) encadré « point d'inflexion »
  (p.74) en « si et seulement si » (faux en général pour une fonction non C²… acceptable au niveau, mais à
  signaler) ; (3) [levé — audit R-7, zoom 250 dpi : p.76 porte sans ambiguïté ℤ*₋] ; (4) Ex. 23 : « t ≥ 10 » tel qu'imprimé (le contexte « 12 heures », « quinzième
  heure » est cohérent) ; (5) Ex. 22 : la formule de l'aire en L, la fonction f(x) = x² − 10x + 50 a un
  minimum en 5 : la question « aire maximum » renvoie aux bornes — transcrit tel quel ; (6) Act. III.1 :
  points A(1,0), B(4,3), C(1,1), E(2,4), D(3,3) lus sur la figure (non écrits en toutes lettres).
## 2.5 Chapitre 5 — Étude de fonctions (manuel 222472, p.87–108)

**Page de garde (p.87)** — « Chapitre 5 » ; titre : « ETUDE DE FONCTIONS ». Plan imprimé : « I . Généralités ·
II . Exemples de fonctions rationnelles · III. Exemples de fonctions de type x ↦ √(ax² + bx + c) ». Portrait :
« Jean-Baptiste Fourier(1768-1830) ».

**Plan du chapitre** :
- **I. Généralités** (p.88–93) : Activités préliminaires 1–7 (p.88–89) ; encadré latéral « Histoire des
  courbes » (p.88) ; « A retenir » (p.90–91 : fonction paire, axe de symétrie, fonction impaire, centre de
  symétrie, périodicité, courbe de |f|) ; Applications 1–4 (p.92–93).
- **II. Exemples de fonctions rationnelles** (p.93–96) : Exemple 1 + Solution (p.93–94) ; Exemple 2 +
  Solution (p.94–96).
- **III. Exemples de fonctions de type x ↦ √(ax² + bx + c)** (p.96–99) : Exemple 1 + Solution (p.96–98) ;
  Exemple 2 + Solution (p.98–99).
- **Applications** (p.100) : 5 exercices (bloc commun aux parties II–III).
- **Apprendre à chercher** (p.101) : Situations 1–2.
- **Avec l'outil informatique** (p.102) : « Situation (Méthode d'Euler) » au tableur.
- **Exercices et problèmes** (p.103–107) : 16 exercices.
- **Maths et culture** (p.108) : biographie de Fourier.
- Pas de « A retenir » sur les asymptotes / branches infinies dans ce chapitre (notions utilisées comme
  acquises, cf. chapitre 2), pas de QCM/Vrai-Faux, pas de plan d'étude en étapes.

### Cours — Activités (une ligne chacune)

**I. Généralités — Activités préliminaires**
- **Act. 1** (p.88) : f(x) = x³ − 3x sur ℝ ; 1) parité, conséquence pour (C_f) ; 2) (C_f) admet un point
  d'inflexion (coordonnées), tangente T en ce point ; déterminer lim_{x→+∞} f(x)/x, interpréter
  graphiquement ; 3) tableau de variation, points à tangente horizontale ; 4) tracer T et (C_f) (repère
  orthogonal).
- **Act. 2** (p.88) : g(x) = (x − 1)/(2x + 3) ; 1) D_g, limites aux bornes ; 2) asymptotes ; 3) si x ∈ D_g,
  alors (−3 − x) ∈ D_g et g(−3 − x) = 1 − g(x) : centre de symétrie ; 4) tableau de variation, tracé.
- **Act. 3** (p.88) : h(x) = ¼(x − 3)²(x + 1)² sur ℝ (repère orthonormé) ; 1) h(2 − x) = h(x), axe de
  symétrie ; 2) a) h′(x) = (x − 3)(x + 1)(x − 1) ; b) tableau de variation ; c) branches infinies ;
  d) tracé.
- **Act. 4** (p.88) : r(x) = √(|x| − 2) ; 1) D_r ; 2) r paire, interprétation ; 3) lim_{x→+∞} f(x)/x [sic,
  « f » pour r] ; allure de (C_r) au voisinage de +∞.
- **Act. 5** (p.89) : f(x) = (2x² − 4x + 4)/(x − 1) ; 1) D_f, limites aux bornes, asymptote verticale Δ ; 2) a) (D) : y = 2x − 2 asymptote oblique ; b) position de (C_f) / (D) ; 3) a) vérifier
  f′(x) = (2x² − 4x)/(x − 1)² ; b) tableau de variations ; c) tracer Δ, (D), (C_f).
- **Act. 6** (p.89) : f(x) = E(x) − x (E partie entière) ; 1) E(x) sur [−1,0[, [0,1[, [2,3[ ; 2) f
  périodique de période 1 ; 3) (C₁), (C₃) parties de la courbe sur [0,1[ et [2,3[ : vecteur de la
  translation qui transforme (C₁) en (C₃).
- **Act. 7** (p.89) : deux courbes (C_f) (parabole de sommet (−1, −3), racines ≈ −2,7 et 0,7) et (C_g)
  (hyperbole d'asymptotes x = 2 et y = 1, tracées sur la figure ; passe par (−1, 0)) : donner les représentations graphiques de
  |f| et |g|.

**Encadré latéral « Histoire des courbes »** (p.88, avec buste) : « C'est le Grec Apollonios de
Perga(262-180 av JC) qui étudie les paraboles, les ellipses et les hyperboles comme sections planes d'un
cône. »

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Fonction paire** (p.90, figure M/M′ symétriques, « f(−x) = f(x) ») — « Soit f une fonction à
> variable réelle et D son ensemble de définition. f est dite paire si et seulement si pour tout x de D on a :
> { -x ∈ D ; f(-x)= f(x) } Sa courbe représentative dans un repère orthogonal admet la droite des ordonnées
> comme axe de symétrie. »

> **Axe de symétrie** (p.90, figure avec Δ : x = a, M, M′, x, 2a − x) — « Soit f une fonction définie sur un
> ensemble D et C_f sa courbe repésentative [sic] relativement à un repère orthogonal (O, i⃗, j⃗) La droite
> Δ d'équation x = a est un axe de symétrie de la courbe C_f ,si et seulement si pour tout x ∈ D on a :
> { (2a - x) ∈ D ; f(2a - x)= f(x) } »

> **Fonction impaire** (p.90, figure « f(−x) = − f(x) ») — « Soit f une fonction à variable réelle et D son
> ensemble de définition. f est dite impaire si et seulement si pour tout x de D on a { -x ∈ D ;
> f(-x)= - f(x) } Sa courbe représentative admet l'origine des coordonnées comme centre de symétrie. »

> **Centre de symétrie** (p.90, figure M′, ω, M, 2a − x, x) — « Le plan est rapporté à un repère (O, i⃗, j⃗)
> Soient I le point de coordonnées (a,b) et C_f la courbe représentative d'une fonction f définie sur un
> ensemble D ⊂ ℝ. Le point ω (a,b) [sic, I puis ω] est un centre de symétrie de la courbe C_f si et seulement
> si pour tout x ∈ D on a : { (2a - x) ∈ D ; f(2a - x)= 2b - f(x) } »

> **Périodicité** (p.91, figure sinusoïde avec « T ») — « Soit f une fonction à variable réelle et D son
> ensemble de définition. f est périodique s'il existe un réel non nul T tel que pour tout x de D on a :
> { x+ T ∈ D ; f(x+ T)= f(x) } Le réel T est dit période de f Sa courbe représentative dans un repère
> (o, i⃗, j⃗) est invariante par la translation de vecteur T i⃗ »

> **Courbe représentative de |f|** (p.91, figure parabole (C_f) et (C|f|)) — « La courbe représentative de
> |f| s'obtient à partir de celle de f en conservant la partie de (C_f) dans le plan (y ≥ 0 ) et en
> remplaçant la partie de (C_f) située dans le demi-plan (y ≤ 0 ) par son symétrique par rapport à l'axe des
> abscisses. »

### Applications de I (p.92–93)

- **App. 1** (p.92) : f(x) = (x² + 3)/(x + 1), repère orthonormé ; a) ensemble de définition ; b) A(−1,−2)
  centre de symétrie ; c) pour x ≠ −1, f(x) = x − 1 + 4/(x + 1) ; asymptote oblique Δ au voisinage de +∞,
  position ; d) variations sur ]−1, +∞[ ; e) branches infinies et asymptotes.
- **App. 2** (p.92) : schéma de (C_f) (maximum A(1, ½), minimum B(−1, −½), points O, I, J, tangentes
  fléchées) ; 1) expliquer que f est dérivable sur ℝ ; 2) tableau de variation ; 3) a) O, I, J points
  d'inflexion ; b) tangente en O ; 4) sachant f(x) = (x + a)/(bx² + c), déterminer a, b, c ; 5) coordonnées
  de I et J.
- **App. 3** (p.93) : solide fixé à un ressort, x(t) = cos(2πt + π) : mouvement périodique, période.
- **App. 4** (p.93) : f(x) = cos((π/2)x) sur ℝ ; a) « Monter » [sic] que f est paire ; b) « Monter » [sic]
  que f est périodique de période 4 ; c) tracer sur [0,2], en déduire la courbe sur ℝ.

### Exemples résolus (avec solution rédigée)

- **II. Exemple 1** (p.93–94) : f(x) = (x² − 2x + 2)/(x² − 2x − 3), repère orthonormé ; 1) D_f ; 2) x = 1 axe
  de symétrie ; 3) variations sur [1, +∞[ ; 4) branches infinies sur [1, +∞[ ; 5) tracer (C_f) sur ℝ.
  **Solution** : D_f = ℝ \ {−1,3} ; « x ∈ D_f alors x ≠ −1 et x ≠ 3 donc (−x) ≠ 1 et (−x) ≠ −3 d'où
  2 − x ≠ 3 et 2 − x ≠ −1 donc 2 − x ∈ D_f » ; f(2 − x) = ((2 − x)² − 2(2 − x) + 2)/((2 − x)² − 2(2 − x) − 3)
  = (4 − 4x + x² − 4 + 2x + 2)/(4 − 4x + x² − 4 + 2x − 3) = f(x) ;
  f′(x) = ((2x − 2)(x² − 2x − 3) − (2x − 2)(x² − 2x + 2))/(x² − 2x − 3)² = 10(1 − x)/(x² − 2x − 3)² ;
  lim_{+∞} f = lim x²/x² = 1 (glyphe « ùlim » [sic]) ; lim_{x→3⁺} f(x) = lim (x² − 2x + 2)/((x + 1)(x − 3))
  = lim 5/(4(x − 3)) = +∞ ; de même lim_{x→3⁻} f(x) = −∞ ; signe : f′(x) ≤ 0 ⇔ 1 − x ≤ 0 ; tableau sur
  [1, +∞[ : f(1) = −1/4 (imprimé « −1/4 » puis « 1/4 » [sic]), décroissante jusqu'à −∞ en 3⁻, puis de +∞ à 1
  (« 2 » parasite dans la ligne des x [sic]) ; asymptotes y = 1 et x = 3 ; courbe tracée (étiquettes
  x = −1, x = 1, x = 3, y = 1).
- **II. Exemple 2** (p.94–96) : f(x) = x/(x² − 4) ; 1) D_f ; 2) parité, interprétation ; 3) limites aux bornes,
  asymptotes ; 4) variations ; 5) point d'inflexion ; 6) tracé. **Solution** : D_f = ℝ \ {−2,2} ;
  f(−x) = −x/((−x)² − 4) = −f(x), f impaire, origine centre de symétrie ; lim_{±∞} f = 0 (y = 0 asymptote
  horizontale) ; lim_{x→2⁻} f(x) = lim x/((x − 2)(x + 2)) = lim 2/(4(x − 2)) = −∞, lim_{x→2⁺} = +∞ (x = 2
  asymptote verticale ; « De même » x = −2) ; f′(x) = (1(x² − 4) − 2x.x)/(x² − 4)² = −(x² + 4)/(x² − 4)²,
  « toujours négative » ; tableau (0 → −∞ ; +∞ → −∞ ; +∞ → 0) ; f″(x) = 2x(x² + 12)/(x² − 4)³ ; « f″ s'annule
  et change de signe pour x = 0 et l'on a : f(0) = 0 Donc le point O(0,0) est un point d'inflexion » ;
  courbe p.96.
- **III. Exemple 1** (p.96–98) : f(x) = √(x² + x + 1) ; 1) D_f ; 2) tableau de variation ; 3) x = −½ axe de
  symétrie ; 4) a) (D) : y = x + ½ asymptote au voisinage de +∞ ; b) position ; c) (D′) : y = −x − ½
  asymptote au voisinage de −∞, position ; 5) tracé. **Solution** : Δ = −3 donc P(x) > 0, D_f = ℝ ;
  f′(x) = (2x + 1)/(2√(x² + x + 1)) ; minimum √3/2 en −½ ; f(−1 − x) = f(x) ; lim_{+∞}[f(x) − (x + ½)] par la
  quantité conjuguée = lim (3/4)/(√(x² + x + 1) + (x + ½)) = 0 ; f(x) − (x + ½) = √((x + ½)² + 3/4) − (x + ½)
  > |x + ½| − (x + ½) ≥ 0 : (C_f) au-dessus de (D) ; idem en −∞ avec (D′) ; courbe (p.98) avec x = −½, (D),
  (D′).
- **III. Exemple 2** (p.98–99) : f(x) = √(−2x² + 2x + 4) ; 1) D_f ; 2) « Montrer que la droite d'équation
  y = ½ [sic, x = ½] est un axe de symétrie », domaine d'étude ; 3) dérivabilité au point 2, interprétation ; 4) tableau de variation sur [½, 2] ; 5) tracé. **Solution** : racines −1 et 2, D_f = [−1,2] ; (1 − x) ∈
  [−1,2] et f(1 − x) = f(x), étude sur [½, 2] ; lim_{x→2⁻} (f(x) − f(2))/(x − 2) = lim √2√(x + 1)/(−√(2 − x))
  = −∞ : non dérivable à gauche en 2, demi-tangente verticale ; f′(x) = (−4x + 2)/(2√(−2x² + 2x + 4)) =
  (−2x + 1)/√(−2x² + 2x + 4) ; tableau : de « 2 » [sic, f(½) = √(9/2) ≈ 2,12] à 0 ; courbe (demi-ellipse sur
  [−1, 2], x = ½, flèches verticales en −1 et 2).

### Applications (p.100) — 5 exercices

- **App. 1** : Δ : x = a axe de symétrie : a) f(x) = (x² + 2x − 4)/(4x² + 8x + 5), a = −1 ;
  b) √(x² − 4x − 5), a = 2 ; c) sin x, a = π/2.
- **App. 2** : A centre de symétrie : a) sin x, A(π,0) ; b) x³ + 3x² + x − 1, A(−1,0) ; c) x³ + 2, A(0,2).
- **App. 3** : branches infinies et nature : a) 3/(x² − 5x + 6) ; b) (4x − 2)/(x − 1) ; c) (2x² − x + 5)/x ;
  d) x√(x − 1) ; e) x + 2 − 1/(x − 2) ; f) (x³ − 4x² + 2x + 5)/(x + 1) ; g) √(4x + 2) ; h) x/√(x + 1).
- **App. 4** : asymptote oblique D : a) (2x² − x + 1)/(x + 2), D : y = 2x − 3 ; b) ((x − 2)² − x + 1)/(x − 2),
  D : y = x − 3 ; c) (2x³ − x² + x − 5)/(x² + 1), D : y = 2x + 1 ; d) √(x² + 4x + 5), D : y = x + 2.
- **App. 5** : f(x) = √(4x² + 4x + 5), D : y = 2x + 1, D′ : y = −2x − 1 ; a) asymptotes ; b) 4x² + 4x + 5 ≥
  (2x + 1)², position ; c) variations ; d) tracé.

### Apprendre à chercher (p.101)

- **Situation 1** : demi-ellipse f(x) = (2/3)√(9 − x²), rectangle inscrit (sommets d'abscisses −x et x) ; 1) aire A(x) = (4/3)x√(9 − x²) ; 2) variations de A, tableau, x pour une aire maximale.
- **Situation 2** : période d'un pendule (tige homogène de masse m, longueur l, axe à la distance x du
  centre de gravité) : T(x) = cm√(l²/(12x) + x), c ≈ 0,64 ; 1) T(x) pour m = 1Kg et l = √12 ; 2) f(x) =
  √((x² + 1)/x) sur ]0, +∞[ (« f définie ]0, +∞[ » [sic]) : a) f′(x) = (x² − 1)/(2x² f(x)) ; b) tableau ;
  c) x pour lequel T(x) est minimale ; 3) lim_{x→+∞} f(x)/x, interprétation ; 4) tracer (C_f).

### Avec l'outil informatique (p.102) — « Situation (Méthode d'Euler) »

f vérifie f(1) = 0 et f′(x) = 1/x pour x > 0 ; « Avec l'approximation f(a+h) ≈ f(a)+f '(a)h on obtient une
valeur approchée de f(x) pour certains x et h voisin de zéro, puis on construit la courbe (C_f). » Tableur :
valeurs initiales ligne 3 : 1 en A3, 1 en B3, 0,01 en C3, 0 en D3 ; formules « = A3+$C$3 en A4 », « = 1/A4
en B4 », « = D3+$C$3 en A4 » [sic : cellule et formule fautives ; les valeurs imprimées (D4 = 0,01,
D5 = 0,01990099, D6 = 0,029704912…) correspondent à D4 = D3 + B3·$C$3] ; tableau imprimé colonnes x,
f′(x) = 1/x, pas : h, « valeur approché [sic] de f(x) » (lignes 3–8 : x = 1 → 1,05) ; extension jusqu'à la
ligne 500 ; nuage de points lissé (courbe de 1 à 6, ordonnée ≈ 1,8 en 6). Encadré : « La fonction f , décrite
dans cette situation, est appelée fonction logarithme népérien Calculatrice touche : ln ». Portrait
« Leonhard Euler (Bâle, 1707-Saint Pétersbourg, 1783 ».

### Exercices et problèmes (p.103–107) — 16 exercices

- **Ex. 1** (p.103) : f(x) = (−x³ + 5x)/(x² + 3), repère orthonormé d'unité 1 cm ; 1) a) f(x) = ax + bx/(x² + 3) ;
  b) f impaire ; 2) a) f′(x) = (x² + 15)(1 − x²)/(x² + 3)² ; b) variations ; 3) D : y = −x asymptote, position ; 4) T tangente en 0 : a) équation réduite ; b) position ; 5) construire D, T, (C), intersections avec l'axe
  des abscisses ; 6) a) (C′) image de (C) par la translation de vecteur 2j⃗ ; b) expression de g.
- **Ex. 2** (p.103) : f(x) = (2x² − 5x + 2)/(3x) sur ℝ \ {0} ; 1) étude (sans tracé) ; 2) a) f(x) = ax + b +
  c/(3x) ; b) y = (2/3)x − 5/3 asymptote ; 3) a) I intersection des deux asymptotes ; b) I centre de
  symétrie ; 4) A, B intersections avec l'axe des abscisses : a) coordonnées ; b) tangentes en A et B ;
  c) D intersection des tangentes « trouvées en (D. b) » [sic] ; 5) a) tracé (unité 2 cm), asymptotes,
  tangentes, D ; b) ABD rectangle en D ; c) aire de ABD en cm².
- **Ex. 3** (p.103–104) : f(x) = (x² + x − 6)/(x² − 3x − 10) sur ℝ \ {−2 ; 5} ; 1) f(x) = a + b/(x + 2) +
  c/(x − 5) ; 2) variations, limites ; 3) (unité 1 cm) a) trois asymptotes ; b) position par rapport à
  l'asymptote horizontale, point I où C la coupe ; c) tangente T en I ; d) T coupe C en J ; e) construire.
- **Ex. 4** (p.104) : f(x) = x − 1 + 2x/(x² + 1) sur ℝ (« représentativede f dans v 0 0 un plan » [sic, texte
  parasite]) ; 1) étude ; 2) y = x − 1 asymptote ; 3) I(0 ; −1) centre ; 4) tangente T en I, position ; 5) points A, B où la tangente est parallèle à y = x − 2 ; 6) x − 2 ≤ f(x) ≤ x ; 7) tracer C, T, D : y = x − 2,
  D′ : y = x.
- **Ex. 5** (p.104) : f(x) = x³ − 3x, g(x) = x − 4/x ; 1) résoudre { f(x) = g(x) ; f′(x) = g′(x) }, C_f et C_g
  « tangentes » en A et B ; 2) positions relatives par rapport à ces tangentes ; 3) C_g et Δ : y = x
  (asymptote) ; 4) tableaux, tracés.
- **Ex. 6** (p.104) : f(x) = (2x² − x)/(x − 1) sur ]1 ; +∞[, repère orthogonal ; 1) limites, conséquence ; 2) Δ : y = 2x + 1, positions ; 3) f′, variations, maximum ? minimum ? ; 4) tangente T parallèle à
  y = 1 − 2x ; 5) tracé (2 cm en abscisse, 1 cm en ordonnée) ; 6) C′ image par la symétrie d'axe (Oy), fonction
  correspondante.
- **Ex. 7** (p.104–105) : f(x) = (−x² + 2x + 1)/(x + 1) sur ]−1, +∞[ ; 1) a) lim_{x→−1⁺} f, conséquence ;
  b) lim_{+∞} f ; 2) a) Δ : y = −x + 3 ; b) positions ; 3) f′, variations ; 4) tangente en 1 ; 5) tracé ; 6) g(x) = (−x² + 6x − 7)/(x − 1) « pour ; x > 1 » [sic] : C_g image de C_f par la translation de vecteur 2i⃗.
- **Ex. 8** (p.105) : f(x) = 1 + x/√(1 + x²) ; 1) a) variations ; b) point d'inflexion I ; c) I centre de
  symétrie ; 2) a) tangente T en I ; b) position ; 3) tracé ; 4) avec g : x ↦ f(x) − x, f(x) = x admet une
  unique solution α ∈ ]1;2[ ; 5) a) f bijection de ℝ sur J ; b) expliciter f⁻¹(x) ; c) tracer C_{f⁻¹} ;
  d) D domaine de dérivabilité de f⁻¹ et (f⁻¹)′(x) « par deux méthodes ».
- **Ex. 9** (p.105–106) : f(x) = x³/(3x² − 6x + 4) ; 1) f dérivable et f′(x) = 3(x(x − 2)/(3x² − 6x + 4))² ; 2) avec f′(x) = (1/3)(1 − 4/(3x² − 6x + 4))², calculer f″, points d'inflexion ; 3) f(x) = ax + b + (cx + d)/
  (3x² − 6x + 4) ; 4) asymptote oblique Δ, position ; 5) I(1,1) centre ; 6) tangente T en I, position ; 7) tracé ; 8) a) bijection de ℝ sur ℝ, g = f⁻¹ ; b) dérivabilité de g ; c) tangente T′ à C_g en I ;
  d) tracer T′ et C_g.
- **Ex. 10** (p.106) : g(x) = √(1 + (x + 1)²) − x ; 1) a) g′(x) < 0 pour x ≤ −1 ; b) 0 ≤ x + 1 ≤ √(1 + (x + 1)²)
  pour x ≥ −1, d'où g′(x) ≤ 0 ; c) limites en ±∞ ; d) tableau ; 2) a) D : y = −2x − 1 asymptote en −∞ ;
  b) tangente en −1 ; g(x) = x admet une unique solution α ∈ ]1,2[ ; 3) a) bijection de ℝ sur J ; b) g⁻¹(x) ;
  c) (g⁻¹)′(2) de deux manières ; 4) tracer g et g⁻¹.
- **Ex. 11** (p.106) : f(x) = (3x² + 4x − 3)/(x² − 1) sur ]−∞;−1[ ∪ ]−1;1[ ∪ ]1;+∞[ ; 1) f(x) = a + b/(x − 1)
  + c/(x + 1) ; 2) limites ; 3) f′, signe, tableau ; 4) asymptotes, tracé (unité 1 cm) ; 5) tangente T en 0 ; 6) centre I(0 ; 3).
- **Ex. 12** (p.106–107) : 1) résoudre dans ℝ³ { x + y + z = 0 ; x − y + z = 8 ; 16x + 4y + z = 3 } ; 2) f(x) = √(ax² + bx + c) : f(1) = 0, f(−1) = √8, f(4) = √3 ; 3) a = 1, b = −4, c = 3 : a) D_f = ]−∞, 1] ∪
  [3, +∞[ ; b) f(4 − x), axe x = 2 ; c) (D) : y = x − 2 asymptote en +∞ ; d) positions ; 4) a) dérivabilité à
  droite en 3 ; b) signe de f′ = signe de (x − 2), tableau ; 5) tracé.
- **Ex. 13** (p.107) : 1) résoudre dans ℝ³ { x + y + z = 1 ; x − y + z = −1 ; 9x − 3y + z = 5 } ; 2) f(x) =
  (ax² + bx + c)/(x + 2), x ≠ −2 : f(1) = 1/3, f(−1) = −1, f(−3) = −5 ; 3) a = b = c = 1 : a) f(x) = x − 1 +
  1/(x + 2) ; b) I(−2,−3) centre ; c) (D) : y = x − 1 asymptote en +∞, positions ; 4) a) f′(x) = (x + 1)(x + 3)/
  (x + 2)² ; b) tableau ; 5) tracé.
- **Ex. 14** (p.107) : f(x) = x + √(x² − 1) ; 1) a) définie sur I = ]−∞,−1] ∪ [1, +∞[ ; b) limites en ±∞ ;
  c) dérivabilité à gauche en −1 et à droite en 1, interprétation ; 2) a) f′(x) > 0 si x > 0 et f′(x) < 0 si
  x < 0 ; b) tableau ; c) (D) : y = 2x asymptote oblique ; d) position ; 3) a) la restriction g de f à
  [1, +∞[ est une bijection, expliciter g⁻¹(x) ; b) tracer (C), (D), (C_{g⁻¹}).
- **Ex. 15** (p.107) : cercle (Γ) de centre O, rayon 1, A(1 ; 0), A′(−1 ; 0) ; H ∈ [AA′], Δ perpendiculaire à
  (AA′) coupe (Γ) en M et M′ ; OH = x ; 1) aire du triangle AMM′ ; 2) f(x) = (1 − x)√(1 − x²) « définie sur
  ℝ » [sic] : variations ; le triangle AMM′ d'aire maximale est équilatéral.
- **Ex. 16** (p.107) : f(x) = x⁴/(x² − 1) sur ]1, +∞[ ; 1) a) f(x) = x² + 1 + 1/(x² − 1) ; b) limites en 1 et
  +∞ ; 2) P : g(x) = x² + 1 ; lim (f − g) en +∞ ; position de C par rapport à P ; 3) f′, variations ; 4) tracer P et C.

### Maths et culture (p.108)

Biographie de Jean-Baptiste (Joseph) Fourier : né le 21 mars 1768 à Auxerre, orphelin à 10 ans, école
militaire d'Auxerre, lecture des 6 tomes du Cours de Bezout, séminaire, enseignant en 1789 ; première
promotion de l'École Normale Supérieure (1794 ; Lagrange, Laplace, Monge) ; 1797 chaire d'analyse et de
mécanique de l'École Polytechnique ; préfet de l'Isère (1801) ; à Grenoble, problème de la chaleur
(1802–1807), « analyse de Fourier » : décomposition en somme infinie de sinus et cosinus.

### Écart avec la référence (math-bac-sciences-exp/05-etudes-de-fonctions ; math-bac-techniques/04-etude-de-fonctions)

Correspondance proposée **confirmée** ; la plus proche par la structure est **techniques/04** (parité, axe,
centre, irrationnelles √u, |f|, translations), la plus proche par la profondeur des exercices est
**sciences-exp/05** (asymptotes obliques, décomposition rationnelle).

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer à l'adaptation)** :
- le cours **« Branche infinie et asymptotes »** et l'**étude par f(x)/x** (branches paraboliques, direction
  asymptotique) comme sections de cours avec encadrés : ici ces notions sont **utilisées** (Act. 1, 4, App. 3,
  Situation 2.3) mais **non énoncées** dans le chapitre (elles relèvent du chapitre 2 de ce manuel) ;
- la **discussion du nombre de solutions de f(x) = k / f(x) = m** (section des deux références) : aucune
  question de ce type ici ;
- l'**étude complète de fonctions trigonométriques** (parité + 2π-périodicité + tracé, section des deux
  références) : ici seulement App. 3–4 (période de cos(2πt + π), de cos(πx/2)) et App. 1c/2a (symétries de
  sin) ;
- le **plan d'étude** explicite (techniques/04), le **changement de repère** Y = F(X) (techniques/04), les
  courbes déduites **f + k, −f** (techniques/04) en cours.

**Ce que ce manuel a en plus (ou autrement)** :
- encadré **périodicité générale** (T quelconque, invariance par translation T i⃗) avec la **partie entière**
  E(x) − x (Act. 6) ;
- **exemples résolus rédigés** (2 rationnels, 2 irrationnels x ↦ √(ax² + bx + c)) : quantité conjuguée pour
  l'asymptote oblique, minoration √((x + ½)² + ¾) > |x + ½| pour la position, demi-tangente verticale ;
- **fonctions réciproques en situation** (Ex. 8, 9, 10, 14 : bijection, f⁻¹ explicite, (f⁻¹)′ « par deux
  méthodes », tangente à C_{f⁻¹}) ;
- **systèmes linéaires 3×3** pour identifier a, b, c (Ex. 12, 13) — lien avec le chapitre 11 de ce manuel ;
- **courbes « tangentes »** (système f = g, f′ = g′, Ex. 5) ; **images de courbes** par translation (2j⃗, 2i⃗)
  et par symétrie d'axe (Oy) (Ex. 1, 6, 7) ;
- **optimisation** : rectangle inscrit dans une demi-ellipse, période minimale d'un pendule, triangle
  équilatéral d'aire maximale (Situation 1–2, Ex. 15) ;
- **méthode d'Euler au tableur** construisant la courbe de ln (outil informatique, annonce du chapitre 6) ;
- **encadrement** x − 2 ≤ f(x) ≤ x (Ex. 4), aire en cm² (Ex. 2).

**Vocabulaire / notations propres** : « Généralités » ; « centre de symétrie » noté I ou ω ; « axe de symétrie
Δ : x = a » ; « branches infinies … déterminer leur nature » ; repère « (o, i⃗, j⃗) » ; « Exemple » + « Solution »
(pas « exercice résolu ») ; « courbe représentative de |f| ».

### Bornes de scope

- ✅ INCLUS : parité (paire/impaire, interprétation graphique) ; axe de symétrie x = a (f(2a − x) = f(x)) ;
  centre de symétrie (f(2a − x) = 2b − f(x)) ; périodicité (définition, translation T i⃗, partie entière) ;
  courbe de |f| ; translations de courbes et symétrie d'axe (Oy) ; point d'inflexion par f″ ; branches
  infinies et asymptotes verticales, horizontales, obliques (utilisées : limite, f(x) − (ax + b), quantité
  conjuguée), lim f(x)/x ; position courbe/asymptote et courbe/tangente ; études complètes de fonctions
  rationnelles (décompositions ax + b + c/…, a + b/(x − 1) + c/(x + 1), ax + b + (cx + d)/(…)) et de
  x ↦ √(ax² + bx + c) (domaine, axe de symétrie, asymptotes obliques en ±∞, demi-tangente verticale) ;
  bijection et réciproque, (f⁻¹)′ ; systèmes 3×3 pour identifier des coefficients ; optimisation ;
  méthode d'Euler (tableur).
- ⛔ EXCLU : discussion graphique du nombre de solutions de f(x) = m ; études complètes de fonctions
  trigonométriques ; plan d'étude formalisé ; changement de repère ; ln, exp (la méthode d'Euler « annonce »
  ln sans l'étudier) ; convexité ; intégrales.

### Lecture

- **Pages lues en L1** : p.87 à p.108, toutes.
- **Pages lues sur l'image (110 dpi)** : p.87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102,
  103, 104, 105, 106, 107, 108 = **22 pages sur 22** (100 %) ; zoom 200 dpi : p.89 (figure de l'Act. 7).
- **Écarts texte/image constatés** : L1 perd les racines (Act. 4 √(|x| − 2) ; III Ex. 1–2 ; App. 4d, 5 ;
  Situation 2), les fractions (Exemple 2 f(x) = x/(x² − 4) lu « x 2 … x − 4 »), les signes (≤, ≥, ≠ rendus par un blanc ou un glyphe vide ;
  « (−x) ≠ 1 » rendu « ( x ) 1 »), les tableaux de variation (p.94, 95, 97, 99 : colonnes et flèches
  illisibles) ; p.103–107 : colonnes entrelacées (Ex. 1–3, 4–7, 8–9, 10–12, 13–16) — attribution faite sur
  l'image ; p.102 : le tableau du tableur absent en L1 (valeurs lues sur l'image) ; p.101 : « c ≈ 0,64 » rendu
  « c " 0, 64 » et l = √12 rendu « 12 ».
- **Coquilles [sic]** : « repésentative » (p.90) ; « I » puis « ω (a,b) » (p.90) ; « (o, i⃗, j⃗) » (p.91) ;
  « Monter que » ×2 (p.93) ; « ùlim » (p.93) ; tableau p.94 (« −1/4 » et « 1/4 », « 2 » parasite) ; « f » pour
  r (Act. 4) ; « droite d'équation y = ½ » axe de symétrie (p.98) ; f(½) imprimé « 2 » (p.99) ; « étudier »,
  « écrire » en minuscule en tête de question (p.96, 103–105) ; « f définie ]0, +∞[ » (p.101) ; formule de
  tableur « = D3+$C$3 en A4 » et « valeur approché » (p.102) ; « (D. b) » (Ex. 2) ; « représentativede f dans
  v 0 0 » (Ex. 4) ; « pour ; x > 1 » (Ex. 7) ; « définie sur ℝ » pour (1 − x)√(1 − x²) (Ex. 15).
- **Doutes [?] à trancher** : (1) Act. 7 : aucune expression de f ni de g n'est donnée (lecture graphique seule ; asymptotes x = 2 et y = 1 de C_g vérifiées au zoom 200 dpi) ; (2) [levé — audit R-7] Ex. 9 : f′(x) = 3(x(x − 2)/(3x² − 6x + 4))² est exacte (f′ = 3x²(x − 2)²/D²,
  D = 3x² − 6x + 4), ainsi que la forme (1/3)(1 − 4/D)² de la question 2 ; (3) Ex. 14.2a :
  « f′(x) > 0 si x > 0 et f′(x) < 0 si x < 0 » sur I = ]−∞,−1] ∪ [1, +∞[ (lire x > 1 / x < −1) ; (4) la
  méthode d'Euler (p.102) **nomme** ln avant le chapitre 6 : à garder comme ouverture, pas comme prérequis.

## 2.6 Chapitre 6 — Logarithme népérien (manuel 222472, p.109–130)

**Page de garde (p.109)** — « Chapitre 6 » ; titre : « LOGARITHME NEPERIEN ». Plan imprimé : « I . Définition
et propriétés. · II . Encadrement de ln (1+x) par des polynômes. · III . Etude de la fonction logarithme
népérien. · IV . Calcul de limites. · V . Etude d'exemples de fonctions de type x ↦ ln(u(x)) · VI . F onction
[sic, espace] logarithme décimal. » Portrait « Al Khawarezmi » et légende : « Le mot LOGARITHME est une
déformation du mot ALGORITHME qui lui même provient du nom du célèbre mathématicien arabe ».

**Plan du chapitre** :
- **I. Définition et propriétés** (p.110–112) : Activités de découverte 1–4 (p.110) ; « A retenir » (p.111) ;
  Applications 1–9 (p.112).
- **II. Encadrement de ln (1+x) par des polynômes** (p.112–113) : une Activité (a–d, dont « Application »).
- **III. Etude de la fonction logarithme népérien** (p.113–115) : Activités 1–3 (p.113) ; « Courbe
  représentative » (p.114) ; Activité 4 (p.114) ; « A retenir » (p.114) ; Applications 1–2 (p.115).
- **IV. Calculs de limites** (p.115–116) : Activités de découverte 1–3 (p.115) ; « A retenir » (p.115) ;
  « Exemples de calcul de limites » 1–3 rédigés (p.116) ; Applications a)–f) (p.116).
- **V. Etude d'exemples de fonctions de type x ↦ ln(u(x))** (p.116–119) : Exemple 1 + Solution
  (p.116–118) ; Exemple 2 + Solution (p.118–119).
- **VI. Fonction logarithme décimal** (p.120) : Activité ; définition ; « Application » (écriture
  scientifique) ; « Exemple » + question.
- **Avec l'outil informatique** (p.121) : deux programmes Pascal « LogDecimal ».
- **Exercices et problèmes** (p.122–129) : 27 exercices (le 27 « D'après BAC »).
- **Maths et culture** (p.130) : histoire des logarithmes.
- Pas de « Apprendre à chercher », pas de QCM/Vrai-Faux.

### Cours — Activités (une ligne chacune)

**I. Définition et propriétés — Activités de découverte**
- **Act. 1** (p.110) : une primitive de x ↦ x² ; x ↦ 1/x⁴ ; x ↦ x⁻³ ; x ↦ 1/x² et x ↦ xⁿ (n ∈ ℤ) ;
  « Etudier le cas n = -1 ».
- **Act. 2** (p.110) : f(x) = 1/x sur ℝ*₊, continue et > 0, « Elle admet donc des primitives définies sur ℝ*₊.
  Parmi ces primitives une seule prend la valeur 0 pour x = 1. Cette primitive est appelée fonction
  **logarithme népérien.** On la note **ln** » ; a) domaine de ln ; b) ln(1) ; c) continuité de ln ; d) sachant
  (ln)′(x) = 1/x, sens de variation sur ]0, +∞[ ; e) comparer ln x et ln 1 pour 0 < x < 1 et x > 1 ; f) ln
  réalise une bijection de ]0, +∞[ sur l'intervalle image ; en déduire ln a = ln b ⇔ a = b et
  ln(a) < ln(b) ⇔ a < b (a > 0, b > 0).
- **Act. 3** (p.110) : k > 0, f(x) = ln kx ; a) domaine, f′(x) ; b) il existe un unique réel α tel que
  f(x) = ln x + α ; déterminer α ; en déduire ln x + ln y = ln(xy) ; c) en déduire ln(1/x) = −ln(x),
  ln(x/y) = ln(x) − ln(y), ln(xⁿ) = n ln(x) (n ∈ ℤ) et ln(√x) = ½ ln(x).
- **Act. 4** (p.110) : 1) f(x) = ln(2x − 3) : ensemble de définition, f′(x) ; 2) g(x) = ln |2x − 3| :
  a) ensemble de définition ; b) g′(x) pour x > 3/2 et x < 3/2 ; que remarque-t-on ? 3) h(x) = 2/(2x − 3)
  sur ]−∞, 3/2[ : primitive de h qui s'annule pour x = 0.

**II. Encadrement de ln (1+x) par des polynômes — Activité** (p.112–113) : f(x) = ln(1 + x) − (x − x²/2),
x > −1 ; a) f′(x) = x²/(x + 1) ; b) par le « théorème des accroissent [sic] finis » sur [0, x] : il existe
c ∈ ]0, x[ tel que ln(1 + x) − (x − x²/2) = xc²/(1 + c) ; c) pour x > 0, x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³ ;
d) **Application** : valeur approchée de ln(1,1) à 10⁻³ près et de ln(1,3) à 10⁻² près.

**III. Etude de la fonction logarithme népérien**
- **Act. 1** (p.113) : compléter le tableau ln x pour x = 100 ; 10000 ; 10¹³ ; 10²⁴ ; 10⁵⁰ ; 10¹⁰⁰ ; 10¹⁰⁰⁰ ;
  texte : « On peut voir que ln x prend des valeurs de plus en plus grandes lorsque x devient de plus en plus
  grand. On admet que ln x tend vers +∞ quand x tend vers +∞ lim_{x→+∞} ln x = +∞ ».
- **Act. 2** (p.113) : en posant X = 1/x et avec lim_{X→+∞} ln X = +∞, montrer lim_{x→0⁺} ln x = −∞.
- **Act. 3** (p.113) : f(x) = ln x − √x sur ]0, +∞[ ; a) f dérivable, f′(x) ≤ 0 pour x ≥ 4 ; b) valeur approchée
  de f(4), en déduire 0 ≤ ln x ≤ √x pour x ≥ 4 ; c) lim_{x→+∞} ln x/x = 0.
- **Courbe représentative** (p.114) : tableau de variations (ln′ > 0 ; −∞ → +∞) et courbe y = ln x (point
  (e, 1) repéré). Texte : « Cette courbe admet l'axe des ordonnées pour asymptote verticale, et admet une
  branche parabolique de direction asymptotique celle de l'axe des abscisses. Comme la fonction ln réalise
  une bijection de ]0,+ ∞ [ sur ℝ , l'équation ln x = 1 admet une unique solution notée e. on a :
  e = 2,718281828… et ln e = 1 ».
- **Act. 4** (p.114) : calculer ln e⁸, ln e³, ln(1/e²), ln eⁿ (n ∈ ℤ) et ln √e ; résoudre ln x = 3, ln x = 8,
  ln x = −2, ln x = n (n ∈ ℤ) et ln x = ½.

**IV. Calculs de limites — Activités de découverte**
- **Act. 1** (p.115) : nombre dérivé de ln en 1 ; en déduire lim_{x→1} ln x/(x − 1) et lim_{h→0} ln(1 + h)/h.
- **Act. 2** (p.115) : a) X = 1/x et lim_{X→+∞} ln X/X = 0 : lim_{x→0⁺} x ln x = 0 ; en déduire pour n ≥ 2
  lim_{x→0⁺} xⁿ ln x = 0 ; b) X = √x : lim_{x→0⁺} √x ln x = 0.
- **Act. 3** (p.115) : a) de lim_{x→+∞} ln x/x = 0, pour n ≥ 2, lim_{x→+∞} ln x/xⁿ = 0 ; b) X = √x :
  lim_{x→+∞} ln x/√x = 0.

**VI. Fonction logarithme décimal — Activité** (p.120) : f(x) = ln x/ln 10 ; domaine ; f(xy) = f(x) + f(y)
pour x > 0, y > 0. (Encadré latéral « Calculatrice : utiliser la touche log ».)

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **A retenir — Définition** (p.111) — « La fonction logarithme népérien, notée ln ou Log , est la primitive de
> la fonction x ↦ 1/x définie sur ]0,+∞ [ et qui s'annule en 1. (ln)'(x)= 1/x , x > 0 ; ln(1) = 0. »

> **Propriétés** (p.111) — « Pour tous réels x > 0 et y > 0 on a : ln( x) = ln(y) ⇔ x = y ;
> ln( x) < ln(y) ⇔ x < y » **En particulier** « ln(x) = 0 ⇔ x = 1 ; ln(x) > 0 ⇔ x > 1 ;
> ln(x) < 0 ⇔ 0 < x < 1 »

> **Propriété fondamentale** (p.111) — « Pour tous réels x > 0 et y > 0 on a : ln (x y) = ln(x) + ln(y) »
> **Conséquences** « ln(1/x)=- ln(x) ; ln(x/y)=ln(x)-ln(y), ; ln(xⁿ)=n ln(x) (n ∈ ℤ) ; ln(√x)=½ ln(x) »

> **Théorème** (p.111) — « Soit u une fonction strictement positive et dérivable sur un intervalle I La
> fonction ln o u est dérivable sur I et l'on a : (ln o u)'(x)= u'(x)/u(x) »

> **Conséquence** (p.111) — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0 pour tout
> x ∈ I Une primitive de u'/u sur I est de la forme x ↦ ln |u(x)| + k »

> **A retenir** (p.114) — « La fonction logarithme népérien est telle que : lim_{x→+∞} ln x = +∞ ;
> lim_{x→0⁺} ln x = -∞ ; lim_{x→+∞} ln x/x = 0 Elle définit une bijection de ]0, + ∞ [ sur ℝ . Le réel e est
> l'unique solution de l'équation ln x = 1. On a : e = 2,718281828… ; ln e = 1 Pour tout entier relatif n
> l'équation ln x = n admet pour unique solution le réel eⁿ . ( ln x = n ⇔ x = eⁿ ) »

> **A retenir** (p.115) — « La fonction logarithme népérien est telle que : lim_{x→1} ln x/(x - 1) = 1 et
> lim_{h→0} ln(1+ h)/h = 1 ; lim_{x→0⁺} x ln x = 0 ; lim_{x→0⁺} xⁿ ln x = 0 (n ≥ 2) ; lim_{x→0⁺} √x ln x = 0 ;
> lim_{x→+∞} ln x/√x = 0 ; lim_{x→+∞} ln x/xⁿ = 0 (n ∈ ℕ*) »

> **Logarithme décimal** (p.120, texte courant hors cadre, termes définis « logarithme décimal » et « log » en gras) — « • La fonction x ↦ ln x/ln10 vérifie toutes les
> propriétés de la fonction ln et vaut 1 pour x = 10. On l'appelle fonction **logarithme décimal** et on la
> note **log**. log x = ln x / ln 10 La calculatrice donne ln10 = 2,302585… et 1/ln10 = 0,434294… On écrit :
> log x = mlnx avec m = 0, 434294… »

> **Application (log)** (p.120) — « La fonction logarithme décimal est d'un usage courant en chimie , en
> physique, en médecine,en astronomie etc … car elle se base sur le système décimal ( base 10). x étant un
> réel strictement positif, son écriture scientifique est : x = a.10ᵖ avec 1 ≤ a < 10 et p ∈ ℤ. On a alors
> log x = log a + log (10ᵖ). Ainsi log x = log a + p Or 0 ≤ log a < 1 et p ∈ ℤ . donc p est la partie entière
> de log (a.10ᵖ) et log a sa partie "décimale". » **Exemple** : « log 2856 = log (2,356.10³ ) = log (2,356) + 3
> [sic, 2856 / 2356] La calculatrice donne log 2,356 = 0,3721... ; donc log 2356 = 3,3721... » Question :
> « Sans calculatrice déterminer la partie entière des nombres suivants : log 42500, log 0,0073 et log 1/8 ».

### Applications et exemples résolus

- **I. App. 1** (p.112) : a) à la calculatrice, ln 2 et ln 5 à 10⁻⁴ près ; b) en déduire ln 4, ln(1/5), ln(2,5),
  ln 10.
- **I. App. 2** : en fonction de ln 2 ou ln 3 : x = ln 8 ; y = ln(1/3) ; z = ln 18 − 3 ln 2 ; t = 3 ln(√3/√2) ;
  u = ln 15 + 2 ln 10 − ln 125.
- **I. App. 3** : simplifier x = ln 36 − 2(ln 2 + ln 3) et y = 2 ln(7/3) + 2 ln 35 − 2 ln 5 − ln(1/9).
- **I. App. 4** : simplifier a = 2 ln(2 + √3) + ln(7 − 4√3) et b = ln ½ + ln ⅔ + ln ¾ + ln ⅘.
- **I. App. 5** : en fonction de ln x, ln y, ln z : A = (1/5) ln x¹⁰, B = ln(x/y) − ln(z/y), C = ln(x⁵/y⁴).
- **I. App. 6** : résoudre ln(3x − 2) = 2 ln x. **App. 7** : résoudre ln(x + 1) > 0.
- **I. App. 8** : dérivée de a) ln(x² − 1) ; b) ln|cos x| ; c) ln(√(x² + 1)).
- **I. App. 9** : une primitive de a) 1/(x − 3) ; b) x/(1 + x²) ; c) tan x ; d) 1/(x ln x).
- **III. App. 1** (p.115) : simplifier A = ln e⁵ − ln e³ ; B = ln(e⁻³) ; C = ln 2 + ln(8e) − ln(4e³) ;
  D = ln(1/e³) − (ln(1/e³))³.
- **III. App. 2** (p.115) : résoudre a) ln(5 − x) = 2 ; b) ln((x − 2)/(2x + 1)) = 0 ; c) (ln x)² + 3 ln x + 2 = 0.
- **IV. Exemples de calcul de limites** (p.116, rédigés) : **Ex. 1** lim_{+∞} ln(x − 1)/(2x + 1) =
  lim [ln(x − 1)/(x − 1)]·[(x − 1)/(2x + 1)] ; X = x − 1 ⇒ premier facteur → 0, second → ½, limite 0 ;
  **Ex. 2** lim_{+∞} (ln x)³/x : x = X³, (ln X³)³/X³ = (3 ln X)³/X³ = 27(ln X/X)³ → 0 ; **Ex. 3**
  lim_{x→0} ln(x² + x + 1)/x = lim [ln(x² + x + 1)/(x + x²)]·(1 + x), u = x + x² → 0, = 1·1 = 1.
- **IV. Applications** (p.116) : a) lim_{+∞} (ln x − x) ; b) lim_{+∞} x/ln x ; c) lim_{0⁺} (1/x² + ln x) ;
  d) lim_{+∞} ln(2x² + x + 1)/x ; e) lim_{0⁺} ln(1 + x²)/x³ ; f) lim_{+∞} (√x − ln x).
- **V. Exemple 1** (p.116–118) : f(x) = ln(x² − 4x + 3), repère orthonormé ; 1) D_f ; 2) a) limites aux bornes ;
  b) lim_{±∞} f(x)/x ; c) branches infinies ; 3) f′(x), tableau ; 4) tracé. **Solution** : D_f = ]−∞,1[ ∪ ]3,+∞[ ;
  limites −∞ en 1⁻ et 3⁺ (« car lim(x² − 4x + 3) = 0⁺ »), +∞ en ±∞ ; f(x)/x = ln x²/x + ln(1 − 4/x + 3/x²)/x
  (imprimé une fois « ln(1 − x/4 + 3/x²) » [sic]) ; « lim ln x²/x = lim 2 ln x/x = 0 » ; en −∞ « 2ln|x|/x » ;
  asymptotes verticales x = 1 et x = 3, « deux branches paraboliques de direction asymptotique celle de la
  droite des abscisses » ; f′(x) = (2x − 4)/(x² − 4x + 3), signe de 2x − 4 ; tableau (+∞ → −∞ sur ]−∞,1[ ;
  −∞ → +∞ sur ]3,+∞[ ; ligne f′ vide et signes « − / + » placés dans la ligne x [sic]) ; courbe.
- **V. Exemple 2** (p.118–119) : f(x) = ln|(x − 4)/x| ; 1) D_f ; 2) « Monter » [sic] que I(2,0) est centre de
  symétrie ; 3) lim_{x→0} f et lim_{x→−∞} f, interprétation ; 4) f′(x), variations sur ]−∞, 2] ; 5) tracé.
  **Solution** : « |(x − 4)/x| ≥ 0 [sic, > 0], donc … est définie pour x ≠ 0 et x ≠ 4 » : D_f = ℝ \ {0,4} ;
  f(4 − x) = ln|−x/(4 − x)| = … = −ln|(4 − x)/x| = −f(x) ; lim_{x→0} f = +∞ (axe des ordonnées asymptote
  verticale) ; lim_{−∞} f = 0 (axe des abscisses asymptote horizontale) ; « On sait que la dérivée de ln|u(x)|
  est u′(x)/u(x) donc f′(x) = (4/x²)/((x − 4)/x) = 4/(x(x − 4)) » ; signe de x(x − 4) ; tableau sur ]−∞, 2] :
  0 ↗ +∞ (en 0⁻) puis +∞ ↘ 0 (en 2) ; courbe complète avec I et x = 4.

### Avec l'outil informatique (p.121)

« Calcul du logarithme décimal log x » : `Program LogDecimal ; Uses Wincrt ; Var x,y:real;` saisie
`repeat … read(x) until x >=0 ;` [sic, x = 0 accepté], `y:=ln(x)/ln(10); writeln('log(',x:4:4,')= ',y:4:10);`.
« Une autre méthode de calcul du logarithme décimal log x » : même saisie ; `if x<1 then begin x:=1/x;
write('-') end; n:=0; while x>=10.0 do begin n:=n+1; x:=x/10.0 end; write(n,'.'); for k:=1 to 10 do begin
x:=sqr(x); x:=x*sqr(sqr(x)); n:=0; while x>=10.0 do begin x:=x/10.0; n:=n+1 end; write(n) end;` (calcul des
décimales par élévation à la puissance 10 : x² · (x²)⁴ = x¹⁰). Aucune question, aucun commentaire.

### Exercices et problèmes (p.122–129) — 27 exercices

- **Ex. 1** (p.122) : en fonction de ln 2 et (ou) ln 5 : ln 10 ; ln 50 ; ln(0,5) ; ln(12,8) ; ln(1/2³) ;
  ln √10 ; ln 0,001.
- **Ex. 2** : simplifier ln 2 − 2 ln 8 − ln(1/16) ; ln 16 − ln 40 + ½ ln √625 − ln 0,625 ; ln(√2 + 1) + ln(√2 − 1) ;
  ln(√3 + 1) + ln(√3 − 1) ; ln 2e − ln e².
- **Ex. 3** : équations : 1) ln x = 2 ; 2) ln x = −1 ; 3) ln(x + 1) = ln(2x − 3) ; 4) ln(x − 2) − ln(x − 3) = 1 ; 5) 2 ln(x + 1) − ln x = ln 2 ; 6) (ln x)² − 2 ln x = 0.
- **Ex. 4** : inéquations : 1) ln x > 10 ; 2) ln x < −50 ; 3) ln(x² − 1) ≤ ln 3 ; 4) ln(x + e) + ln(x − e) ≤
  2 + ln 3 ; 5) ln(1 − 2x) ≤ 1.
- **Ex. 5** : dans ℝ², { x + y = 55 ; ln x + ln y = 700 } [? « 700 » tel qu'imprimé, sans ln].
- **Ex. 6** : dans ℝ², { x + y = 30 ; ln x = 2 ln 12 − ln y }.
- **Ex. 7** (p.122) : dériver a) x ln(x) ; b) ln(x)/x ; c) ln(x² + 1) ; d) ln(x + √(x² + 1)) ; e) ln(x/√(x² + 1)) ;
  f) ln((x + 1)/(x − 1)) ; g) ln(x² − 5x + 6) ; h) ln|4x + 8| ; i) ln(√(x − 1)).
- **Ex. 8** : une primitive de a) x/(x² + 1) ; b) (x + 1)/(x − 1) ; c) tan x.
- **Ex. 9** : f(x) = (−x² + 4x − 3)/(x − 1) sur « ℝ / {1} » ; 1) a, b, c tels que f(x) = ax + b + c/(x − 1) ; 2) primitives de f sur ]1, +∞[.
- **Ex. 10** : limites éventuelles : a) lim_{+∞} ln(7x) ; b) lim_{0⁺} ln(x√2) ; c) lim_{+∞} x/ln x ;
  d) lim_{−∞} ln(−x/3) ; e) lim_{+∞} (x − ln x) ; f) lim_{+∞} ln x/x² ; g) lim_{+∞} ln(0,8x)/x ;
  h) lim_{+∞} ln x/(5x) ; i) lim_{+∞} (¼x² − ln x − 3) ; j) lim_{x→1,5⁻} ln(3 − 2x) ;
  k) lim_{+∞} [ln(2x + 1) − ln(x − 3)] ; l) lim_{0⁺} ln((1 + x)/x).
- **Ex. 11** (p.123, « calculer » [sic, minuscule]) : a) lim_{−∞} ln(−7 + 5x²) ; b) lim_{+∞} (x² − ln x) ;
  c) lim_{+∞} (2x − ln x) ; d) lim_{0⁺} (x⁵ ln x) ; e) lim_{+∞} (ln x)⁶/x ; f) lim_{+∞} ln(x⁵ − x²)/x ;
  g) lim_{0⁺} (1/x + ln x) ; h) lim_{0} ln(1 − x)/x ; i) lim_{+∞} (x² − 1)/(x ln x) ; j) lim_{+∞} (1 + ln x)/(1 − ln x) ;
  k) lim_{+∞} x ln(1 + 1/x) ; l) lim_{0} ln(1 + 2 sin x)/x.
- **Ex. 12** : f(x) = ln(3x² − x − 2) ; 1) domaine ; 2) f′, variations ; 3) tangente en A d'abscisse 8 ; 4) tangente en B d'abscisse −5/6 ; 5) tracé sommaire ; 6) résoudre f(x) = ln(−5x − 3).
- **Ex. 13** : étudier et représenter : a) ln(x² − 4) ; b) ln(x² + x + 1) ; c) ln(x³ − 8) ; d) ln((x − 2)/(x + 1)) ;
  e) ln((x − 2)/(x + 1)) [sic : d) et e) identiques à l'image] ; f) x − ln x ; g) ln(|x|) + x ; h) x ln x.
- **Ex. 14** (p.123) : niveau sonore d(I) = (10/ln10)·ln(I/I₀) (en décibels, « db ») ; 1) voix humaine
  I = 10⁶ I₀ : d(I) ; 2) I₁ ≤ I₂ : a) d(I₂) − d(I₁) = (10/ln10) ln(I₂/I₁) ; b) pour I₂ = 2I₁, arrondi au
  dixième ; c) I₂/I₁ lorsque d(I₂) − d(I₁) = 15 ; justifier « 115 décibels, c'est environ 32 fois plus fort que
  100 décibels » ; 3) I₁/I₀, I₂/I₀, I₂/I₁ lorsque a) I₁ « correspond a » [sic] 90 db (danger de surdité) ;
  b) I₂ correspond à 120 db (« concert des «Who» en 1976 »).
- **Ex. 15** (p.123–124) : f(x) = ½[ln x − ln(1 − x)] sur ]0, 1[, courbe Γ (unité 4 cm) ; 1) limites en 0 et 1,
  asymptotes, variations ; 2) a) centre de symétrie A(½, 0) ; b) tangente (D) en A ; 3) φ(x) = f(x) − 2x + 1 :
  a) variations ; b) positions de Γ et (D) ; 4) tracer Γ et (D) « dans le repère . » [sic].
- **Ex. 16** (p.124) : 1000 D placés le 01/01/2002 à intérêts composés 3,5 % par an ; 1) C₁, C₂, C₃, (Cₙ)
  géométrique, raison ; 2) Cₙ en fonction de n ; 3) avec ln : nombre d'années pour doubler, tripler.
- **Ex. 17** (p.124) : A) g(x) = x² − 1 + ln x sur ]0, +∞[ : 1) variations ; 2) g(1), g(x) ≤ 0 si 0 < x ≤ 1 et
  g(x) ≥ 0 si x ≥ 1 ; B) f(x) = x − ln x/x : 1) limites en +∞ et 0⁺ ; 2) a) (D) : y = x asymptote en +∞ ;
  b) positions ; c) f′(x) = g(x)/x² ; 3) tableau ; 4) tracé ; 5) primitive F de f sur ]0, +∞[ qui s'annule en 1.
- **Ex. 18** (p.124) : mémoire tampon d'un réseau téléinformatique : M(t) = −30/log t − 10, t intensité du trafic
  (0 < t < 1) ; f(x) = −30/log x − 10 sur [0,2 ; 0,8] ; 1) f(x) à l'aide de ln x ; 2) f′(x) = 30 ln10/(x ln²x) ; 3) tableau ; 4) représentation ; 5) intensité du trafic à 0,01 près pour M = 64 (calcul et graphique).
- **Ex. 19** (p.124–125) : repère orthonormé (unité 1 cm), C_f de f(x) = 1 − ln x sur ]0 ; +∞[ (figure) ; 1) a) f monotone ; b) signe de f ; 2) l'une de deux courbes représentées (maximum en e, valeur e ;
  palier horizontal en e) est une primitive de f : justifier que l'une ne peut convenir ; 3) la bonne,
  g(x) = ax ln x + cx + b [sic, ordre des lettres] : a) g′(x) « en fonction de a et b » [sic] ; b) a et b ; 4) g(e) = e lu sur le graphique : c.
- **Ex. 20** (p.125) : f(x) = −2x + 5 + 3 ln(x + 1) sur ]−1 ; +∞[ ; 1) a) limite en −1⁺, interprétation ;
  b) lim_{+∞} f ; 2) a) f′, variations ; b) tableau, valeur exacte du maximum ; 3) branches infinies, tracé ; 4) a) α < 0 < β avec f(α) = f(β) = 0 ; b) valeurs approchées à 10⁻² par défaut ; c) signe de f ; 5) g(x) =
  (x + 1) ln(x + 1) − x : a) g′(x) ; b) primitive de f s'annulant en 0.
- **Ex. 21** (p.125–126) : f(x) = 2/x + ln x sur ]0 ; +∞[, C′ : y = 2/x ; 1) a) f(1) ; b) f(e) et f(½) exacts et à
  10⁻² ; c) f(1/e) « en fonction de ln e » [sic] et f(3/4) en fonction de ln 2 et ln 3 ; 2) lim_{+∞} f ; 3) f′,
  variations, tracé de C ; 4) tangente T en 1 ; 5) position de C et C′, tracé de C′.
- **Ex. 22** (p.126) : A) g(x) = x³ − 1 + 2 ln x : 1) g′, signe ; 2) tableau (« les limites ne sont pas
  demandées ») ; 3) g(1) ; 4) signe de g. B) f(x) = x − 1 − ln x/x², repère orthogonal (3 cm / 2 cm) ; 1) a) limites en +∞ et 0⁺ ; b) D : y = x − 1 asymptote oblique ; autre asymptote ? ; c) f′(x) = g(x)/x³ ;
  d) signe de f′, tableau ; e) intersection de D et C, position ; f) tracé ; 2) H(x) = −(1/x)(1 + ln x) primitive de
  h(x) = ln x/x² sur ]0 ; +∞[ ; en déduire une primitive de f.
- **Ex. 23** (p.126–127) : courbe de f dérivable sur ]0 ; +∞[ et tangente (T) en 1 (minimum lu en 1/e, valeur
  −2/e) ; 1) lecture : a) f(1/e) et f′(1) ; b) signe de f sur ]0 ; 3] ; 2) f(x) = (ax + b) ln x : a) f′(x) ;
  b) a et b (avec 1.a) ; 3) laquelle des courbes 1, 2, 3 est une primitive de f (justifier) ; 4) G(x) =
  (1 − ln x)x² et H(x) = x²(ln x − ½) : laquelle est la primitive choisie ?
- **Ex. 24** (p.127–128) : plaque chauffante (2 éléments de 7 résistors de 330 W ; échanges 7,5 W/°C ; air à
  24 °C) : t(T) = −1000·ln(1 − T/640)/0,9625 (T < 640) ; 1) a) temps de 24 °C à 400 °C ; b) t′(T) ;
  c) variations sur [50 ; 600] ; compléter le tableau T = 50, 100, …, 600 ; 2) a) représentation graphique ;
  b) température atteinte en 20 min (graphique et calcul).
- **Ex. 25** (p.128) : f(x) = ln(1 + x) + 2x/(1 + x) sur ]−1, +∞[ ; 1) a) f′(x) = (x + 3)/(x + 1)² ; b) tableau ; 2) réciproque f⁻¹ ; 3) h(x) = f(x) − x : a) tableau ; b) h(x) = 0 a deux solutions 0 et α, 2 < α < 3 ;
  c) position de C et D : y = x ; 4) a) tracer D, C, tangente T en O (α = 2,8) ; b) C′ de f⁻¹, tangente T′ en O.
- **Ex. 26** (p.128–129) : (C) courbe de ln ; A) tangente T_e au point e, passe par l'origine ; B) a > 0 : 1) tangente T en A d'abscisse a ; 2) g(x) = ln x − (1/a)x + 1 − ln a : a) dérivabilité, g′ ; b) signe ;
  c) variations, signe ; d) « En déduire que la position » [sic] de (C) par rapport à (T) ; C) 1) ln x ≤ x − 1 ; 2) h(x) = ln x − 1 + 1/x : variations, signe ; 3) 1 − 1/x ≤ ln x ≤ x − 1, interprétation graphique (figure
  y = x − 1, y = ln x, y = 1 − 1/x) ; 4) encadrements d'amplitude 10⁻² de ln 0,95 ; ln 0,98 ; ln 1,03 ; ln 1,1.
- **Ex. 27** (p.129, « D'après BAC ») : f(x) = 1/x + ln x sur ]0, +∞[ ; (I) 1) tableau ; 2) a) point d'inflexion I ;
  b) tangente T en I ; 3) a) lim_{+∞} f(x)/x, interprétation ; b) tracé (ln 2 = 0,7) ; (II) g(x) = f(x) − x : 1) bijection de ]0, +∞[ sur ℝ ; 2) g(1), f(x) ≤ x sur [1, +∞[ ; 3) U₀ = 2, Uₙ₊₁ = f(Uₙ) : a) Uₙ > 1 par
  récurrence ; b) U décroissante ; c) convergente, limite.

### Maths et culture (p.130)

Origine du mot (« déformation du mot ALGORITHME … Al Khawarezmi » ; « les euoropéens » [sic]) ; John Napier
(Merchiston Castle), *Mirifici logarithmorum canonis descriptio* (1614) et *… constructio* (1619) ; Henry Briggs
(1561-1630), logarithmes en base 10 (« base vulgaire », logarithmes de Briggs) ; Jost Bürgi (1552-1632), idée
dès 1588 (« On prétend même de [sic] Bürgi a conçu »), *Arithmetische und geometrische Progress-Tabulen*
(Prague, 1620) ; impact sur les calculs des astronomes.

### Écart avec la référence (math-bac-sciences-exp/08-fonction-logarithme-neperien)

Correspondance proposée **confirmée**.

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer à l'adaptation)** :
- la **définition par l'intégrale** ln x = ∫₁ˣ dt/t et la construction par l'aire : ici ln est **la primitive de
  1/x qui s'annule en 1** (le calcul intégral est le chapitre 8, après exp) ; la localisation **e ∈ ]2, 3[**
  (ici seulement e = 2,718281828…) ;
- la **primitive de ln** (x ln x − x) comme théorème (ici seulement en exercice via g(x) = (x + 1) ln(x + 1) − x,
  Ex. 20.5, et G/H, Ex. 23.4) ; les **intégrales, aires, volumes, intégration par parties** ;
- les **croissances comparées générales** lnⁿx/xᵐ et xᵐlnⁿx (ici : ln x/xⁿ, xⁿ ln x, √x ln x, ln x/√x et un
  exemple (ln x)³/x par changement de variable ; (ln x)⁶/x en exercice) ; ln(ᵖ√a) = (1/p) ln a (ici seulement
  ln √x = ½ ln x) ;
- ln|u| énoncé comme **corollaire de dérivation** (ici : pas d'énoncé encadré, seulement « primitive de u′/u =
  ln|u| + k » ; mais la dérivée de ln|u| est découverte en Act. 4.2 p.110 (ln|2x − 3|) et pratiquée en App. I.8 b
  (ln|cos x|), Ex. 7 h (ln|4x + 8|) et Exemple 2 (V)) ;
- une suite contractante |uₙ₊₁ − a| ≤ k|uₙ − a| en exercice défi de la référence (exercices/04-defi.json ; absente
  du cours.md) — ici une seule suite Uₙ₊₁ = f(Uₙ) monotone bornée, Ex. 27.

**Ce que ce manuel a en plus (ou autrement)** :
- **II. Encadrement de ln(1 + x) par des polynômes** via le TAF (x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³) et valeurs
  approchées de ln 1,1, ln 1,3 ; encadrement 1 − 1/x ≤ ln x ≤ x − 1 (Ex. 26) ;
- **VI. Logarithme décimal** log x = ln x/ln 10, écriture scientifique, partie entière / « décimale » de log x
  (la référence l'exclut explicitement) ; exercice d'application en **décibels** (Ex. 14) et en
  **télé-informatique** (mémoire tampon, Ex. 18) ;
- **programmes Pascal** de calcul de log x (dont un algorithme digit par digit) ;
- **intérêts composés** (suite géométrique, Ex. 16), **plaque chauffante** (Ex. 24) ;
- **systèmes** à logarithme (Ex. 5, 6) ; résolution d'équations du second degré en ln x ;
- lecture graphique d'une **primitive** (Ex. 19, 23) ; fonction réciproque et tangente T′ (Ex. 25) ;
- notation « ln ou **Log** » à la définition ; « Propriété fondamentale » ; exemples de limites rédigés
  (changement de variable X = x − 1, x = X³, u = x + x²).

**Vocabulaire / notations propres** : « Log » (majuscule) comme synonyme de ln ; « logarithme décimal » noté log,
« m = 0,434294… » ; « partie "décimale" » de log x ; « Propriété fondamentale » ; « db » pour décibel ;
« Activités de découverte » ; « Exemples de calcul de limites ».

### Bornes de scope

- ✅ INCLUS : ln défini comme primitive de 1/x nulle en 1, (ln)′ = 1/x, ln 1 = 0, monotonie, équivalences
  ln a = ln b, ln a < ln b, signe de ln ; propriété fondamentale ln(xy) et conséquences (1/x, x/y, xⁿ avec
  n ∈ ℤ, √x) ; bijection ]0, +∞[ → ℝ, e (valeur décimale), ln eⁿ = n, ln x = n ⇔ x = eⁿ (n ∈ ℤ) ; équations,
  inéquations, systèmes ; limites de référence (±∞, 0⁺, ln x/(x − 1), ln(1 + h)/h, x ln x, xⁿ ln x, √x ln x,
  ln x/xⁿ, ln x/√x) et changements de variable ; tableau et courbe de ln (asymptote verticale, branche
  parabolique) ; dérivée de ln∘u, primitive u′/u = ln|u| + k ; études de fonctions ln(u(x)), ln|u(x)|,
  x − ln x, x ln x, 1/x + ln x… (asymptotes, branches paraboliques, centre de symétrie, inflexion, fonction
  auxiliaire g pour le signe de f′) ; encadrement de ln(1 + x) par des polynômes (TAF) ; logarithme décimal ;
  applications (décibels, intérêts composés, télé-informatique, thermique) ; suite Uₙ₊₁ = f(Uₙ) (Ex. 27) ;
  réciproque (Ex. 25) ; primitives lues ou vérifiées (Ex. 17.5, 19, 20.5, 22.2, 23).
- ⛔ EXCLU : intégrale ∫₁ˣ dt/t, aire, volume, intégration par parties ; fonction exponentielle et exp comme
  réciproque de ln (eⁿ n'apparaît qu'avec n ∈ ℤ ; √e = e^½ seulement via ln √e) ; aᵇ à exposant réel ;
  croissances comparées (ln x)ⁿ/xᵐ énoncées en général ; équations différentielles ; suites contractantes.

### Lecture

- **Pages lues en L1** : p.109 à p.130, toutes.
- **Pages lues sur l'image (110 dpi)** : p.109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
  123, 124, 125, 126, 127, 128, 129, 130 = **22 pages sur 22** (100 %) ; zoom 250 dpi : p.123 (Ex. 13 d/e).
- **Écarts texte/image constatés** : L1 perd les ⇔ (rendus par un glyphe vide), les ∈ ℤ (« n ») , les racines (App. 2 t, Ex. 1
  ln √10, Ex. 2 ln √625, Ex. 7 d–e–i), les exposants (ln e⁵, e⁻³, 10¹⁰⁰⁰ du tableau p.113 lisibles seulement à
  l'image), les valeurs absolues (Exemple 2 : ln|(x − 4)/x|, absentes de L1), les tableaux de variation (p.114,
  118, 119) ; p.122–129 : deux colonnes entrelacées (Ex. 7–10 mêlés aux Ex. 1–6 ; Ex. 15 à cheval p.123–124 ;
  Ex. 19 à cheval p.124–125 ; Ex. 21 à cheval p.125–126) — attribution faite sur l'image ; les symboles Γ et φ
  de l'Ex. 15 sont absents de L1 (« % » pour φ).
- **Coquilles [sic]** : « F onction » (p.109) ; « Logarithme néperien » en en-tête (p.111) ; « accroissent finis »
  (p.113) ; « ln(1 − x/4 + 3/x²) » (p.117) ; tableau p.118 (ligne f′ vide, signes dans la ligne x) ; « Monter que »
  (p.118) ; « |(x − 4)/x| ≥ 0 » (p.118) ; « log 2856 = log (2,356.10³) » (p.120) ; `until x >=0` (p.121) ;
  « calculer » minuscule (Ex. 11) ; Ex. 13 d) = e) ; « correspond a » (Ex. 14) ; « dans le repère . » (Ex. 15) ;
  « g(x) = ax ln x + cx + b » et « g′ en fonction de a et b » (Ex. 19) ; « f(1/e) en fonction de ln e » (Ex. 21) ;
  « En déduire que la position » (Ex. 26) ; « euoropéens », « On prétend même de Bürgi » (p.130).
- **Doutes [?] à trancher** : (1) Ex. 5 : « ln x + ln y = 700 » imprimé sans ln (probablement ln 700 : xy = 700,
  x + y = 55 donne x, y = 35 et 20) — à confirmer par l'orchestrateur avant réutilisation ; (2) Ex. 19.1b « signe
  de f » : f = 1 − ln x change de signe en e (énoncé cohérent, pas d'erreur) ; (3) II.c : majorant imprimé
  « x − x²/2 + x³ » (cohérent avec xc²/(1 + c) ≤ x³) ; (4) Ex. 13 e) : sans doute ln|(x − 2)/(x + 1)| prévu (doublon
  imprimé de d) — ne pas inventer la valeur absolue, signaler ; (5) Ex. 23 : coordonnées du minimum (1/e ;
  −2/e) lues sur la figure.

## 2.7 Chapitre 7 — Fonctions exponentielles (manuel 222472, p.131–148)

**Page de garde (p.131)** — « Chapitre 7 », titre « FONCTIONS EXPONENTIELLES ». Plan imprimé : « I . Fonction
exponentielle · II . Étude de la fonction exponentielle · III . Puissance rationnelle d'un réel positif. · IV . Fonction
exponentielle de base a · V . Étude de fonctions du type x ↦ e^(u(x)) ». Portrait légendé « EULER Leonard 1707-1783 ».
Pas de citation.

**Plan du chapitre (bandeaux de rubrique de la collection)** : **Cours** p.132–140 — I. Fonction exponentielle (p.132–133 :
Activités 1–2, « A retenir », « Applications » 1–3) · II. Étude de la fonction exponentielle (p.133–135 : Activités 1–5,
« A retenir » Limites / Dérivées et Primitives avec figure, « Applications » 1–3) · III. Puissance rationnelle d'un réel
positif (p.135–136 : Activités 1–4, « A retenir », « Applications » 1–2) · IV. Fonction exponentielle de base a
(p.137–138 : Activités 1–3, « A retenir », « Applications » 1–2) · V. Étude de fonctions du type x ↦ e^(u(x))
(p.138–140 : **Exemple 1** et **Exemple 2** entièrement résolus = exercices résolus) · **Apprendre à chercher**
(p.141 : Situations 1–3) · **Avec l'outil informatique** (p.142 : programme Pascal) · **Exercices et problèmes**
(p.143–147 : **22 exercices**, numérotés 1–22 dans des cases ; p.146 porte par erreur le bandeau « Cours » [sic]) ·
**Maths et culture** (p.148 : « Le nombre "e" »). Ni QCM ni Vrai-Faux en rubrique séparée (un Vrai/Faux est l'Ex. 6),
pas de « Tout ce qu'on doit savoir » : la synthèse est portée par les encadrés « A retenir ».
Activités numérotées à nouveau dans chaque partie (I : 1–2 ; II : 1–5 ; III : 1–4 ; IV : 1–3).

### Cours — Activités (une ligne chacune)

**I. Fonction exponentielle** (p.132) — Introduction : « On sait que la fonction logarithme népérien est une bijection de
]0, +∞[ sur IR. Elle admet une fonction réciproque définie sur IR à valeurs dans ]0, +∞[. Cette fonction est appelée
**fonction exponentielle**, elle est notée **exp**. » Schéma IR →exp→ ]0, +∞[, x ↦ y, retour ln ; « x ∈ IR, y ∈ ]0,+∞[ ;
y = exp(x) ⇔ x = ln y » ; « Ainsi x ∈ ]0,+∞[ exp(ln(x)) = x » ; « x ∈ IR, ln(exp(x)) = x » ; vignette flèches ln/exp.

- **Act. 1** (p.132) : a) déterminer exp(0), exp(1), exp(−1), exp(2), exp(−2), exp(1/2) et exp(−1/3) ; b) montrer que
  pour tout n ∈ ℤ, exp(n) = eⁿ ; c) montrer que pour tout n ∈ IN*, exp(1/n) = ⁿ√e. Puis : « On convient de remplacer
  pour tout x ∈ IR exp(x) par eˣ. ainsi pour tout x ∈ IR, exp(x) = eˣ. Cette nouvelle écriture est une extension des
  propriétés trouvées dans l'activité précédente. »
- **Act. 2** (p.132) : a) x = eᵃ, y = eᵇ, z = e^(a+b) ; déterminer ln z puis ln(xy), en déduire eᵃeᵇ = e^(a+b) ;
  b) en écrivant autrement e^(b−b) = e⁰, montrer e^(−b) = 1/eᵇ ; c) pour n ∈ ℤ et a ∈ IR, (eᵃ)ⁿ = e^(na) ;
  d) pour n ∈ IN*, ⁿ√(eᵃ) = e^(a/n).
- **Applications I** (p.133) : 1. calculatrice, valeur approchée à 10⁻⁴ près de e^(1,2), e^(√3), e^(−1/2) (encadré
  « Calculatrice : Utiliser les 2 touches 2ndF et puis ln ») ; 2. simplifier e^(ln5), e^(−ln2), e^(2+ln3), e^((1/2)ln7) ;
  ln e^(−0,4), ln√(e⁵) et ln e^((1/2)ln3) ; 3. résoudre dans IR : a) eˣ = 5 ; b) eˣ = −3 ; c) e^(2x−3) = e³ ;
  d) eˣ/(e^(2x) + 1) = 1/2.

**II. Étude de la fonction exponentielle**

- **Act. 1** (p.133) : a) tracer dans un repère orthonormé la courbe de ln et en déduire celle de exp ; b) donner
  lim_{x→+∞} eˣ et lim_{x→−∞} eˣ ; c) en posant y = eˣ, déterminer lim_{x→+∞} eˣ/x.
- **Act. 2** (p.133) : a) en posant X = −x, déterminer lim_{x→−∞} x eˣ ; b) montrer que pour tout n ∈ IN*,
  lim_{x→+∞} eˣ/xⁿ = +∞ (« on pourra écrire eˣ = (e^(x/n))ⁿ ») ; en déduire lim_{x→−∞} xⁿeˣ = 0.
- **Act. 3** (p.134) : a) montrer que exp est dérivable sur IR ; b) schéma ln y = x ⇄ y = eˣ : montrer
  (exp)′(x) = 1/((ln)′(y)), en déduire (exp)′(x) = (exp)(x).
- **Act. 4** (p.134) : calculer la dérivée de exp en 0 ; en déduire lim_{x→0} (eˣ − 1)/x = 1.
- **Act. 5** (p.134) : u dérivable sur I, f(x) = e^(u(x)) ; écrire f comme composée de deux fonctions et déterminer f′(x).
- **Applications II** (p.135) : 1. limites a) lim_{x→−∞} (2x − 1)e^(2x) ; b) lim_{x→+∞} eˣ − 2x ; c) lim_{x→+∞} x²e^(−x) ;
  d) lim_{x→0⁻} e^(1/x) ; e) lim_{x→0} (e^(−x) − 1)/x ; f) lim_{x→0} (e^(−x²) − 1)/x. 2. f′(x) pour a) 1/eˣ ;
  b) (2x − 5)e^(2x) ; c) e^(2x)/x² ; d) e^(cos x). 3. une primitive de a) cos x e^(sin x) ; b) e^(3x) ;
  c) x e^(x²−1) ; d) 1/e^(2x).

**III. Puissance rationnelle d'un réel positif**

- **Act. 1** (p.135) : a) x > 0, écrire plus simplement e^(2lnπ) ; e^(−5ln7) ; e^((1/2)ln3) et e^(−4lnx) ; b) x > 0,
  n ∈ IN : écrire xⁿ, x⁻ⁿ et ⁿ√x sous forme d'exponentielle d'un réel. Texte : « x étant un réel strictement positif et n
  un entier relatif, on sait que e^(n lnx) = xⁿ. Si dans l'écriture e^(n lnx) on remplace n par le rationnel r, on obtient
  l'expression e^(n lnx) [sic, pour e^(r lnx)] qui a toujours un sens, ceci suggère de définir xʳ. Ainsi pour tout x > 0
  et pour tout rationnel r, on définit xʳ par l'égalité xʳ = e^(r lnx) (lire x puissance r). xʳ est une **puissance
  rationnelle** de x » ; c) écrire sous forme exponentielle 5^(3/2) et 2^(−3/5).
- **Act. 2** (p.135) : n ∈ IN, x > 0 : a) montrer x^(1/n) = ⁿ√x [sic : n ∈ IN, n = 0 non exclu] ; b) montrer de même que
  si p ∈ ℤ et q ∈ IN*, x^(p/q) = ᵠ√(xᵖ).
- **Act. 3** (p.136) : a, b > 0, r, r′ rationnels : démontrer par la définition ln aʳ = r ln a ; a^(r+r′) = aʳa^(r′) ;
  a^(r−r′) = aʳ/a^(r′) ; (aʳ)^(r′) = a^(rr′) ; (ab)ʳ = aʳbʳ ; (a/b)ʳ = aʳ/bʳ.
- **Act. 4** (p.136) : r rationnel > 0, x > 0. a) en remarquant ln xʳ = r ln x, montrer lim_{x→0⁺} xʳ ln x = 0 et
  lim_{x→+∞} ln x/xʳ = 0 ; b) vérifier eˣ/xʳ = e^(x − r lnx) ; en remarquant x − r ln x = x(1 − r ln x/x), montrer que
  pour tout rationnel positif r, lim_{x→+∞} eˣ/xʳ = +∞ ; c) montrer xⁿeˣ = xⁿ/e^(−x) ; en déduire que pour tout entier
  positif n, lim_{x→−∞} xⁿeˣ = 0.
- **Applications III** (p.136) : 1. simplifier a) 81^(2/3) [sic ? voir doutes] ; b) 16^(3/4) ; c) 121^(3/2) ; d) 5^(3/2)·⁶√125 ; 2. écrire sous la forme aʳ (a > 0) : a) √(√a) ; b) a√a ; c) √a/a² ; d) ³√(a²).

**IV. Fonction exponentielle de base a**

- **Act. 1** (p.137) : a > 0, f(x) = e^(x lna) sur IR. a) f(0), f(1), f(3), f(−1), f(−3), f(1/2), f(−1/2) ; b) pour tout
  n ∈ ℤ, f(n) = aⁿ ; c) pour n ∈ IN*, f(1/n) = a^(1/n) ; d) pour p ∈ IN* et q ∈ IN*, f(p/q) = a^(p/q). Puis : « On convient
  de remplacer, pour tout x ∈ IR, la notation e^(xlna) par aˣ. Ainsi e^(xlna) = aˣ. Pour a ≠ 1, f est appelée **fonction
  exponentielle de base a**. »
- **Act. 2** (p.137) : pour x, x′ réels et a, b > 0 : aˣ·a^(x′) = a^(x+x′), aˣ·bˣ = (ab)ˣ, aˣ·a^(−x) = 1,
  aˣ/a^(x′) = a^(x−x′), (aˣ)^(x′) = a^(xx′).
- **Act. 3** (p.137) : a > 0, f_a(x) = aˣ. a) montrer f′_a(x) = aˣ ln a ; b) a = 2 : tableau de variation de f₂,
  lim_{x→+∞} 2ˣ/x, tracer la courbe de f₂ ; c) a = 1/2 : montrer f_{1/2}(x) = 1/f₂(x), déterminer lim_{x→−∞} f_{1/2}(x)/x,
  tracer la courbe ; d) vérifier f₂(−x) = f_{1/2}(x) et en déduire que les courbes de f₂ et f_{1/2} sont symétriques par
  rapport à la droite des ordonnées.
- **Applications IV** (p.138) : 1. résoudre 3ˣ = 15 ; 10ˣ = 72 ; 7^(x−1) = 5ˣ ; 4ˣ − 3·2ˣ + 2 = 0. 2. nénuphars : « Sur un
  étang (de surface infinie…) une population de nénuphars double chaque jour (au premier jour elle est de un nénuphar).
  Comment modéliser le phénomène ? Au bout de n jours on a 2ⁿ nénuphars (n est un entier). Combien en a-t-on au bout de 16
  jours 12 heures 45 minutes (… soit 16,53125 jours) ? »

**V. Étude de fonctions du type x ↦ e^(u(x))** (exercices résolus)

- **Exemple 1** (p.138–139) : f(x) = e^(−x²). 1) ensemble de définition, parité ; 2) lim_{x→+∞} f(x) ; 3) tableau de
  variation sur [0, +∞[ ; 4) tracer (C_f). **Solution** : 1) définie sur IR ; « Pour tout x ∈ IR on a : (−x) ∈ IR et
  f(−x) = e^(−(−x)²) = e^(−x²) = f(x). Donc f est paire. » 2) lim_{x→+∞} e^(−x²) = 0 car lim_{x→+∞}(−x²) = −∞ ; 3) « f(x) est de la forme e^(u(x)) avec u(x) = −x². Comme la fonction x ↦ −x² est dérivable sur IR, alors f est dérivable
  sur IR. On a : f′(x) = −2x e^(−x²). Comme e^(−x²) est toujours positif, le signe de f′(x) est celui de (−2x). » 4) tableau sur IR₊ : x 0 → +∞, f′ −, f décroît de 1 à 0 (un « +∞ » parasite est imprimé dans la ligne f au-dessus du 0
  d'arrivée [sic]) ; courbe en cloche (C_f) tracée sur [−5, 4].
- **Exemple 2** (p.139–140) : f(x) = (1/2)x + 2 − e^((1/2)x) sur IR, (C) en repère orthonormé. 1) a) lim_{−∞} f ;
  b) montrer lim_{+∞} f = −∞ ; c) lim_{+∞} f(x)/x, interpréter ; d) Δ : y = (1/2)x + 2 asymptote au voisinage de −∞ ; 2) variations ; 3) tracer Δ et (C) ; 4) montrer graphiquement que 2e^((1/2)x) = x + 4 admet deux solutions α et β, et
  les encadrer. **Solution** : 1) a) lim_{−∞} f = lim((1/2)x + 2) − lim e^((1/2)x) = −∞ car lim_{x→−∞} e^((1/2)x) = 0 ;
  b) f(x) = (1/2)x(1 + 4/x − e^((1/2)x)/((1/2)x)) ; e^((1/2)x)/((1/2)x) de la forme eᵘ/u avec u → +∞, donc → +∞, d'où
  lim_{+∞} f = −∞ ; c) f(x)/x = 1/2 + 2/x − e^((1/2)x)/x et e^((1/2)x)/x = (1/2)·e^((1/2)x)/((1/2)x) → +∞, donc
  lim f(x)/x = −∞ : « Il en résulte que la courbe (C) présente au voisinage de +∞ une branche parabolique de direction
  celle de la droite des ordonnées. » ; d) lim_{x→−∞} f(x) − ((1/2)x + 2) = lim(−e^((1/2)x)) = 0, donc Δ asymptote ; 2) f′(x) = 1/2 − (1/2)e^((1/2)x) = (1/2)(1 − e^((1/2)x)) ; f′(x) ≥ 0 ⇔ 1 − e^((1/2)x) ≥ 0 ⇔ e^((1/2)x) ≤ 1 ⇔ x ≤ 0 ;
  tableau : −∞ ↗ 1 (en 0) ↘ −∞ (ligne f′ imprimée « 0 + 0 − », avec un « 0 » parasite sous −∞ [sic]) ; 3) courbe et D
  tracées ; 4) 2e^((1/2)x) = x + 4 ⇔ e^((1/2)x) = (1/2)x + 2 ⇔ e^((1/2)x) − (1/2)x − 2 = 0 ⇔ f(x) = 0 ; « Graphiquement
  on a deux points d'abscisses α et β telles que : −4 < α < −3 et 2 < β < 3 ».

### Cours — Encadrés « A retenir » (VERBATIM, vérifiés sur l'image)

> **Définition** (p.132) — « La fonction exponentielle, notée exp, est la bijection réciproque de la fonction logarithme
> népérien. exp : IR → ]0,+∞[ ; x ↦ exp(x) = eˣ » (suite p.133) « x ∈ IR, y ∈ ]0,+∞[ y = exp(x) ⇔ x = ln y ou encore
> y = eˣ ⇔ x = ln y. On a pour tout x ∈ IR ln(eˣ) = x. Pour tout x > 0 e^(ln x) = x. Pour tous réels a et b on a :
> eᵃ eᵇ = e^(a+b), e^(a−b) = eᵃ/eᵇ et e^(−b) = 1/eᵇ. Pour tout n ∈ ℤ on a : (eᵃ)ⁿ = e^(na) »

> **Limites** (p.134) — « lim_{x→+∞} eˣ = +∞ , lim_{x→−∞} eˣ = 0 , lim_{x→+∞} eˣ/x = +∞ . lim_{x→−∞} xeˣ = 0. Pour tout
> n ∈ IN on a : lim_{x→+∞} eˣ/xⁿ = +∞ , lim_{x→−∞} xⁿeˣ = 0 et lim_{x→0} (eˣ − 1)/x = 1 » (figure : y = eˣ, y = x,
> y = ln(x), symétriques).

> **Dérivées et Primitives** (p.134) — « La fonction exponentielle est dérivable sur IR et on a : exp′(x) = exp(x),
> x ∈ IR. Si u est une fonction définie et dérivable sur un intervalle I, alors la fonction expou est dérivable sur I et on
> a : (exp o u)′(x) = u′(x) exp(u(x)). Une primitive de la fonction x ↦ u′(x) e^(u(x)) est la fonction x ↦ e^(u(x)) »

> **Définition** (p.136) — « x étant un réel strictement positif, et r un rationnel, xʳ est une puissance rationnelle de
> x définie par : xʳ = e^(r lnx) »
> **Propriétés** — « Si a et b sont deux réels strictement positifs, r et r′ sont deux rationnels on a : ln aʳ = r lna ;
> a^(r+r′) = aʳa^(r′) ; a^(r−r′) = aʳ/a^(r′) ; (aʳ)^(r′) = a^(rr′) ; (ab)ʳ = aʳbʳ ; (a/b)ʳ = aʳ/bʳ »

> **Définition et Notation** (p.138) — « a étant un réel strictement positif et x un réel, on appelle fonction
> exponentielle de base a la fonction x ↦ e^(xlna) et on note aˣ le réel e^(xLna) [sic, « Lna »]. aˣ = e^(xlna) »
> **Propriétés** — « Pour tous réels x et x′ et pour tous réels strictement positifs a et b on a : aˣ.a^(x′) = a^(x+x′) ,
> aˣ.bˣ = (ab)ˣ ; aˣ.a^(−x) = 1 , (aˣ)ʸ = a^(xy) » [sic : y non introduit, pour x′]
> **Courbe représentative** — figure : courbes « 0<a<1 » (décroissante), « a > 1 » (croissante), « a = 1 » (droite y = 1),
> passant toutes par (0 ; 1).

_Aucun encadré ne donne la dérivée de aˣ (seulement Act. 3 a) ni celle de xʳ, ni de primitive de xʳ._

### Apprendre à chercher (p.141)

- **Situation 1** : population de 9 millions en 2006, f(t) = 9·e^(0,04t). 1) à partir de quelle année aura-t-elle plus
  que doublé ? 2) ressources limitées à 15 millions : pendant combien d'années la nourriture sera-t-elle suffisante ?
- **Situation 2** : épidémie de grippe, P(t) = 20t/(1 + 19e^(−1,2t)) [sic ? voir doutes], t en semaines, P(t) en milliers
  d'habitants. 1) nombre de personnes initialement atteintes ; 2) si la situation ne change pas, combien en tout ?
- **Situation 3** : F(x) = (ax + b)e^(cx). 1) calculer F′(x), que remarque-t-on ? 2) f(x) = (2x − 3)e^(2x) : en déduire
  une primitive F de f. « Les calculs précédents donnent une méthode de recherche d'une primitive d'une fonction de la
  forme x ↦ (ax + b)e^(cx), dite méthode d'identification. »

### Avec l'outil informatique (p.142)

« Un programme qui donne une approximation de eˣ = 1 + x/1! + x²/2! + x³/3! + …… + xⁿ/n! à epsilon près. Le calcul
s'arrête lorsque |xⁿ/n!| ≤ epsilon. (x et epsilon données) Exemple e² ≈ 7,389 ». Programme Pascal imprimé :
`program exponentielle; uses wincrt; var x,e,s,p,f:real; i:integer; begin write('x= ');readln(x); write('Epsilon = ');readln(e); S:=1; i:=1; p:=1; f:=1; repeat p:=p*x; f:=f*i; S:=S+p/f; i:=i+1; until abs(P/f) <= e; writeln('La valeur approchée d''exponentielle de x = ',S); end.`
(Le développement en série n'est pas justifié dans le cours : simple usage algorithmique.)

### Exercices et problèmes (p.143–147) — 22 exercices

- **Ex. 1** (p.143) : écrire plus simplement a) ln e^(−2/3) ; b) e^(ln3) ; c) e^(5ln3) − 3e^(ln7) ; d) e^(2ln3)/e^(ln8) ;
  e) e³/e^(4+ln3) ; f) ln(e^(−3)/(e²)^(−2)).
- **Ex. 2** (p.143) : résoudre dans IR a) exp(2x − 3) = 1 ; b) eˣ = 2 ; c) e^(−2x) = −2 ; d) exp(3x + 1) = e^(1−5x) ;
  e) e^(4x) + 1 = 3 ; f) e^(2x) = e^(−x) ; g) (eˣ)² − 3eˣ + 2 = 0 ; h) e^(x²−16) = 144 ; i) e^((x−4)(2x−1)) = e ;
  j) e^(−x) + eˣ = 2 ; k) eˣ − 5 + 6/eˣ = 0 ; l) 2eˣ(eˣ − 6e^(−x)) = 5eˣ.
- **Ex. 3** (p.143) : inéquations a) e^(3x+1) > 0 ; b) e^(x−1) ≤ −2 ; c) e^(−5x+2) < 1 ; d) exp(3x + 14) > −3 ;
  e) e^(2x+2) − e^(3x−5) < 0.
- **Ex. 4** (p.143) : limites a) lim_{+∞} 3e^(−2x+6) ; b) lim_{+∞} (eˣ + 3)/eˣ ; c) lim_{+∞} exp(√x − 5) ;
  d) lim_{+∞} (e^(2x) − eˣ + 2) ; e) lim_{+∞} ln(1 + e^(−x)) ; f) lim_{+∞} (e^(3x) − 1)/(3 − eˣ) ; g) lim_{−∞} (e^(3x) − 2eˣ + 4) ;
  h) lim_{−∞} e^(−2x²−x+1) ; i) lim_{−∞} (e^(−x) − 3e^(2x) − 2) ; j) lim_{x→0⁻} 1/(eˣ − 1).
- **Ex. 5** (p.143) : 1) pour x ≠ 0, (eˣ + 1)/(eˣ − 1) = (1 + e^(−x))/(1 − e^(−x)) ; 2) limites de (eˣ + 1)/(eˣ − 1) en
  +∞, −∞, 0⁺, 0⁻ en choisissant l'écriture adaptée.
- **Ex. 6** (p.143) : Vrai ou Faux (9 items) : 1) x ↦ exp(x²) est la dérivée de f(x) = exp(x²) ; 2) x ↦ −e^(−x) dérivée de
  g(x) = e^(−x) ; 3) x ↦ −1/e^(2x) dérivée de h(x) = 1/eˣ ; 4) x ↦ (3x² − 1)exp(x³ − x + 1) dérivée de k(x) = e^(x³−x+1) ; 5) exp est une primitive sur IR de exp ; 6) f : x ↦ e^(−3x) admet pour primitive sur IR la fonction f : x ↦ e^(−3x) [sic,
  même nom] ; 7) G(x) = exp(3x² − 5) primitive de g : x ↦ 6x exp(3x² − 5) ; 8) h : x ↦ (eˣ)³ admet pour primitive
  H : x ↦ (1/3)e^(3x) ; 9) K : x ↦ exp(1/x²) primitive sur ]0 ; +∞[ de k : x ↦ −(2/x³)exp(1/x²). (Réponses non fournies.)
- **Ex. 7** (p.143) : dérivée et ensemble de définition de a) e^(−x) ; b) e^(2x) − 3eˣ + 4 ; c) (x + 1)eˣ ; d) exp(1/x) ;
  e) ln(3 + e^(−x)) ; f) 2eˣ ; g) 2x + eˣ ; h) x·eˣ ; i) x²·eˣ ; j) (2x + 1)eˣ ; k) (x² − 1)eˣ.
- **Ex. 8** (p.143–144) : 1) ensemble de définition puis une primitive de a) 2eˣ ; b) 2x + 1 + eˣ ; c) −eˣ + x² ; 2) F(x) = (x + 1)eˣ primitive sur IR de f(x) = (x + 2)eˣ ; 3) F(x) = (x² − 1)eˣ primitive de (x² + 2x − 1)eˣ.
- **Ex. 9** (p.144) : f(x) = −x + 1 − eˣ. 1) variations, tableau ; 2) branches infinies de C_f ; 3) C_f coupe (Ox) en un
  unique point A, construire C_f ; 4) en déduire la courbe de h(x) = −|x| + 1 − e^(|x|).
- **Ex. 10** (p.144) : f(x) = 2x + 5 − 2eˣ. 1) limites en ±∞ ; 2) a) variations ; b) f(x) = 0 admet deux solutions α et α
  [sic, α et β] (β < 0 et β > 0 [sic, α < 0]) ; c) valeurs arrondies à 10⁻¹ ; 3) construire C_f et faire apparaître α et β ; 4) courbe de
  g(x) = |2x + 5 − 2eˣ|.
- **Ex. 11** (p.144) : f(x) = e^(2x) − eˣ. 1) a) limites aux bornes ; b) équation de l'asymptote ; 2) tableau de
  variation, graphe ; 3) une primitive de f.
- **Ex. 12** (p.144) : f(x) = eˣ/(2(1 − x)) sur IR∖{1}. 1) justifier les éléments du tableau de variation fourni
  (x : −∞, 1, 2, +∞ ; f′ : + | + 0 − ; f : 0 ↗ +∞ ‖ −∞ ↗ −e²/2 ↘ −∞ — signe « − » de e²/2 à peine visible à l'image) ; 2) branche infinie au voisinage de +∞ ; 3) tracer C.
- **Ex. 13** (p.144–145) : **A** f(x) = x + eˣ, unité 1 cm. 1) limites en ±∞ ; 2) variations ; 3) point de C où la
  tangente T a pour coefficient directeur 3 ; 4) a) f(x) = 0 a une solution unique α ; b) α ∈ ]−1, 0[ ; c) signe de f ; 5) a) D : y = x asymptote en −∞ ; b) position de D et C ; c) pour quelles x la distance C–D (parallèlement à (o, j⃗)) est
  < 0,01 cm ; 6) représenter C sur [−3 ; 2], D et T. **B** g(x) = x² + 2eˣ, courbe (C_g) fournie : 1) a) variations de g ;
  b) le point A à tangente horizontale a pour coordonnées (α, α² − 2α) ; 2) limites de g en ±∞ ; 3) discuter selon m le
  nombre de solutions de g(x) = m.
- **Ex. 14** (p.145) : C courbe (fournie) de f(x) = (ax + b)e^(cx) ; C passe par (1 ; 0) et (0, 1/3), tangente horizontale
  au point d'abscisse 2/3. 1) tableau de variation par lecture ; 2) f(0), f(1), f′(2/3) ; 3) f′(x) en fonction de a, b, c ; 4) en déduire a, b, c.
- **Ex. 15** (p.145–146) : courbe Γ de f sur [0 ; 4] et tangentes aux points d'abscisses 1 et 1,5. 1) lire f(1), f′(1),
  f′(1,5) ; 2) parmi trois courbes (1 à 3) laquelle peut représenter f′ (justifier graphiquement) ; 3) f(x) = (ax + b)e^(−x+1) :
  f′(x), déterminer a et b ; 4) F(x) = −(2x + 1)e^(−x+1) : vérifier que F est une primitive de f sur [0 ; 4].
- **Ex. 16** (p.146) : capital C placé le 1/1/2007 à intérêts composés à 5,35 % par an. 1) somme après 1, 2, 3 ans ; 2) après n ans ; 3) graphe point par point de f(x) = 1,0535ˣ sur [0 ; 20] ; 4) au bout de combien d'années la somme
  dépassera le double ; vérifier graphiquement.
- **Ex. 17** (p.146) : pays de 5 000 000 d'habitants, baisse de 2 % par an. 1) après 1, 2, 3 ans ; 2) après n ans ; 3) graphe de g(x) = 0,98ˣ sur [0 ; 20] ; 4) au bout de combien d'années aura-t-il perdu plus du quart de sa population ;
  vérifier graphiquement.
- **Ex. 18** (p.146) : radioactivité, N(t) = e^(−at)N(0). a) demi-vie T (N(t + T) = N(t)/2), T en fonction de a ;
  b) N(nT) = 2⁻ⁿN(0) ; c) temps pour diviser par 1000, par 10⁶ (« On pourra utiliser le fait que 2¹⁰ ≃ 1024, voisin de 1000. »).
- **Ex. 19** (p.146–147) : **I)** φ(x) = eˣ + x + 1. 1) a) limites en ±∞ ; b) variations ; 2) φ(x) = 0 a une unique
  solution α, −1,28 < α < −1,27 ; 3) signe de φ. **II)** f(x) = xeˣ/(eˣ + 1), unité 4 cm. 1) a) f′(x) = eˣφ(x)/(eˣ + 1)² ;
  b) sens de variation ; 2) f(α) = α + 1, encadrement de f(α) ; 3) T tangente en 0 : a) équation ; b) position C/T ; 4) a) limites en ±∞ ; b) D : y = x asymptote ; c) position C/D ; 5) tableau de variations ; 6) tracer C, T, D, abscisses
  dans [−2 ; 4].
- **Ex. 20** (p.147) : f sur ]0 ; +∞[ par f(x′) [sic] = e^(x+2)/(x + 2)². 1) limite en +∞ (poser X = x + 2) ; 2) montrer
  que f(x) [sic, pour f′(x)] = xe^(x+2)/(x + 2)³ ; 3) tableau de variation ; 4) branches infinies, tracer (C_f).
- **Ex. 21** (p.147) : problème f(x) = 2x + (x − 1)eˣ. **A)** g(x) = 2 + xeˣ : 1) variations (limites non demandées) ; 2) signe de g. **B)** 1) a) limites en ±∞ ; b) D : y = 2x asymptote en +∞ [sic ? voir doutes] ; c) position (C)/(D) ; 2) f′(x) et tableau via A ; 3) a) f(x) = 0 a une unique solution x₀ dans [0 ; 1] ; b) nombre de solutions dans IR ;
  c) 0,4 < x₀ < 0,5 ; 4) point A où la tangente est parallèle à (D).
- **Ex. 22** (p.147) : f(x) = (ax + b)eˣ. 1) f′(x) en fonction de a, b ; 2) a, b pour que la courbe passe par E(1, 3e) et
  ait une tangente horizontale au point d'abscisse −3 ; 3) variations et courbe ; 4) F(x) = (cx + d)eˣ : c et d pour que
  F soit une primitive de f s'annulant en 1.

### Maths et culture (p.148)

« Le nombre "e" » — « Les logarithmes sont des nombres artificiels utilisés pour obtenir le résultat de l'opération. Ils
servent d'intermédiaires. Cependant, ces nombres intermédiaires sont transcendants, et, de la même manière que pour le
nombre Pi des siècles auparavant, les mathématiciens vont faire émerger un symbole qui permettra de nommer en une lettre
une infinité de chiffres, c'est le nombre e. Ainsi ln(e) = 1. Même s'il sera étudié par Leibniz, Huygens ou encore
Bernoulli, le nombre e sera nommé conventionnellement par le mathématicien Suisse Leonhard Euler (1707-1783) qui
attribuera cette lettre en rapport, non pas avec son nom, mais avec la fonction exponentielle qu'elle décrit. »

### Écart avec la référence (math-bac-sciences-exp/09 « Fonction exponentielle », manuel 222433 p.142–164 ; voisin : math-bac-techniques/07)

Correspondance **confirmée** : sciences-exp/09 couvre toutes les notions de ce chapitre. techniques/07 (même découpage
« aˣ et xʳ », « étudier e^(u(x)) ») est aussi proche ; sciences-exp/09 reste la référence (plus riche, à élaguer).

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer à l'adaptation)** :

- **intégrales** avec exponentielle (∫u′eᵘ, intégration par parties x eˣ, x²eˣ, e^(−x) sin x, F(X) = ∫₀^X e^(−x²)dx), aires
  et limites d'aires, volume de révolution : le calcul intégral n'arrive qu'au ch. 8 de ce manuel et le ch. 7 ne contient
  aucune intégrale ;
- **suites récurrentes u\_{n+1} = φ(u_n)** par |φ′| ≤ k < 1 (inégalité des accroissements finis) et **suites définies par
  une intégrale** (le « scénario du bac » de la référence) ;
- **dérivée de xʳ** (r x^(r−1)) et **primitive x^(r+1)/(r + 1)** ; limites de xʳ en 0⁺/+∞ selon le signe de r : absentes
  des encadrés (seules les croissances comparées ln x/xʳ, xʳ ln x, eˣ/xʳ sont établies en Act. 4) ;
- **tangente en 0 et position de C_exp par rapport à y = x + 1** (h(x) = eˣ − x − 1) : non traitée ;
- **variations et limites de aˣ selon a ≷ 1 énoncées en encadré** : ici seulement la figure « 0<a<1 / a>1 / a=1 » et
  l'étude des cas a = 2 et a = 1/2 (Act. 3) ; dérivée (ln a)aˣ seulement en activité ;
- point d'inflexion, symétrie centrale, fonctions (eˣ ± e^(−x))/2.

**Ce que ce manuel a en plus (ou autrement)** :

- e^(1/n) = ⁿ√e et ⁿ√(eᵃ) = e^(a/n) en activité (I) ; partie III « **Puissance rationnelle d'un réel positif** » centrée
  sur le **calcul** (81^(2/3), 16^(3/4), 5^(3/2)·⁶√125, √(√a) = a^(1/4)…), xʳ défini avant aˣ ;
- **modélisation** : nénuphars 2ⁿ (Appl. IV.2), population 9e^(0,04t), épidémie logistique, intérêts composés 1,0535ˣ,
  décroissance 0,98ˣ, radioactivité/demi-vie (Situations 1–2, Ex. 16–18) ;
- **méthode d'identification** d'une primitive de (ax + b)e^(cx) (Situation 3, Ex. 8.2–3, 15.4, 22.4) ;
- **outil informatique** : programme Pascal approchant eˣ par 1 + x/1! + … + xⁿ/n! (série non démontrée) ;
- **courbes de |f|** (h(x) = −|x| + 1 − e^(|x|), g(x) = |2x + 5 − 2eˣ|) ; **lecture graphique** f, f′ (Ex. 14–15) ;
  discussion de g(x) = m (Ex. 13 B) ; distance courbe-asymptote < 0,01 cm (Ex. 13 A 5c) ;
- encadré « Pour tout n ∈ IN … lim eˣ/xⁿ = +∞, lim_{−∞} xⁿeˣ = 0 » (puissances entières ; la référence : e^(nx)/x^m).
- Vocabulaire/notations : « exp o u », « expou » ; « IR » pour ℝ ; « bijection réciproque » ; « puissance rationnelle » ;
  « fonction exponentielle de base a » (a ≠ 1) ; rubriques « A retenir », « Applications », « Apprendre à chercher »,
  « Avec l'outil informatique », « Maths et culture ».

### Bornes de scope (chapitre 7, section Sciences de l'informatique)

- ✅ INCLUS : exp = bijection réciproque de ln, notation eˣ, y = eˣ ⇔ x = ln y, ln(eˣ) = x, e^(ln x) = x ; règles
  eᵃeᵇ, e^(a−b), e^(−b), (eᵃ)ⁿ (n ∈ ℤ), ⁿ√(eᵃ) = e^(a/n) ; équations et inéquations exponentielles (dont X = eˣ) ;
  limites lim_{±∞} eˣ, eˣ/x, xeˣ, eˣ/xⁿ, xⁿeˣ, (eˣ − 1)/x ; exp′ = exp ; (e^u)′ = u′e^u ; primitive de u′e^u ;
  puissance rationnelle xʳ = e^(r ln x) et ses 6 propriétés ; x^(1/n) = ⁿ√x, x^(p/q) = ᵠ√(xᵖ) ; croissances comparées
  xʳ ln x → 0 (0⁺), ln x/xʳ → 0, eˣ/xʳ → +∞ ; fonction aˣ = e^(x ln a) (a > 0), propriétés, dérivée aˣ ln a (activité),
  courbes selon a, symétrie de 2ˣ et (1/2)ˣ ; études de fonctions e^(u(x)) et mixtes (asymptotes, branches paraboliques,
  tangentes, TVI, encadrements, |f|, discussion graphique) ; identification de primitives (ax + b)e^(cx) ; modèles de
  croissance/décroissance exponentielle, demi-vie ; approximation de eˣ par programme (usage).
- ⛔ EXCLU (absent de ces pages) : intégrales et aires ; suites récurrentes et suites d'intégrales ; équations
  différentielles ; dérivée/primitive de xʳ ; exposant irrationnel ; logarithme décimal (10ˣ seulement dans une équation) ;
  fonctions hyperboliques ; démonstration de e = Σ 1/k! ou de e = lim(1 + 1/n)ⁿ ; point d'inflexion.

### Lecture

- **Pages lues en L1 (pdftotext -layout)** : p.131 à 148 (18 pages). Prose fiable ; exposants, fractions, racines,
  indices et tableaux dégradés.
- **Pages lues sur l'image (110 dpi)** : p.131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
  147, 148 = **18/18 (100 %)** ; zooms 250 dpi : p.141 (Situation 2, « 20t » confirmé), p.144 (tableau de l'Ex. 12).
- **Écarts texte/image** : p.132 L1 perd « n ∈ ℤ » (Act. 1b, 2c) et ⁿ√e ; p.133 L1 : e^(√3), e^(−1/2), e^((1/2)ln7)
  illisibles ; p.135 L1 « e2 ln » pour e^(2lnπ) (π perdu), d) lim_{x→0⁻} e^(1/x) (signe 0⁻ perdu) ; p.136 L1 Act. 4 et
  encadré de propriétés mélangés ; p.137 L1 indices f_{1/2} illisibles ; p.139–140 L1 exposants (1/2)x éclatés sur
  plusieurs lignes, tableaux de variation et courbes absents ; p.143–147 L1 sur deux colonnes entrelacées (Ex. 6/7/8,
  13/14/15, 16–19, 20–22 mêlés), « % » pour φ (Ex. 19), exposants perdus (Ex. 2 h, 4 h, 20) ; figures des Ex. 13 B, 14,
  15 (courbes 1–3) uniquement sur image.
- **Coquilles [sic]** : « e^(n lnx) » pour e^(r lnx) (p.135) ; « e^(xLna) » (p.138) ; « (aˣ)ʸ = a^(xy) » avec y non
  introduit (p.138) ; « +∞ » parasite dans la ligne f du tableau de l'Exemple 1 (p.139) ; « 0 » parasite dans la ligne f′ du tableau de l'Exemple 2 (p.140) ; Ex. 6.6 même nom f pour la
  fonction et sa primitive ; Ex. 10 « α et α (β < 0 et β > 0) » ; Ex. 20 « f(x′) » et « f(x) » pour f′(x) ; bandeau
  « Cours » sur la page d'exercices p.146 ; Ex. 13 B « (C_g) sa courbe IR » (IR parasite).
- **Doutes [?]** : (1) Situation 2 p.141 : imprimé « P(t) = 20t/(1 + 19e^(−1,2t)) » ; le modèle logistique attendu est
  20/(1 + 19e^(−1,2t)) (avec « 20t », P(0) = 0 et la question « initialement atteintes » perd son sens) : relevé tel quel,
  à ne pas corriger silencieusement ; (2) Ex. 21 B 1b : D : y = 2x asymptote « au voisinage de +∞ » alors que
  f(x) − 2x = (x − 1)eˣ → 0 en **−∞** (pas en +∞) : coquille probable du manuel ; (3) Appl. III.1 a) « 81^(2/3) » lu tel
  quel (81^(3/4) serait entier ; l'image est nette : 2/3) ; (4) Ex. 12 : valeur −e²/2 au maximum local, signe « − » à
  peine visible.
## 2.8 Chapitre 8 — Calcul intégral (manuel 222472, p.149–163)

**Page de garde (p.149)** — « Chapitre 8 », titre « CALCUL INTEGRAL ». Plan imprimé : « I . Intégrale d'une fonction
sur un intervalle · II . Intégrales et inégalités · III . Calcul d'aires planes ». Portrait légendé « RIEMANN Bernhard
(1826 - 1866) ». Pas de citation.

**Plan du chapitre** : **Cours** p.150–156 — I. Intégrale d'une fonction sur un intervalle (p.150–152 : Activités 1–4,
« A retenir » Définition / Propriétés / Intégration par parties, « Applications » 1–5) · II. Intégrales et inégalités
(p.152–154 : Activités 1–4, « A retenir » Positivité / Valeur moyenne / Inégalité de la moyenne / Égalité de la
moyenne, « Applications » 1–3) · III. Calculs d'aires planes (titre courant « Calculs », p.154–156 : « Activités
préliminaires » 1–3, « A retenir » deux théorèmes avec figures, « Applications » 1–3) · **Apprendre à chercher**
(p.157 : Situations 1–2) · **Avec l'outil informatique** (p.158 : programme Pascal, méthode des rectangles) ·
**Exercices et problèmes** (p.159–162 : **18 exercices**) · **Maths et culture** (p.163 : Riemann, intégrale de
Riemann, approximation). Pas de QCM/Vrai-Faux séparé (Ex. 1 = QCM « Cocher la bonne réponse », Ex. 2 = vrai/faux),
pas d'exercice résolu dans le cours.

### Cours — Activités (une ligne chacune)

**I. Intégrale d'une fonction sur un intervalle**
- **Act. 1** (p.150) : f(x) = x² − 2x + 3 sur IR. a) une primitive F, calculer F(3) − F(1) ; b) vérifier que F(3) − F(1)
  ne dépend pas du choix de F. Suite imprimée : « • Le nombre F(3) – F(1) est appelé **intégrale** de f entre 1 et 3. On
  le note : ∫₁³ f(x)dx Lire : « intégrale de 1 à 3 de f(x) dx». • x est une variable muette et on peut écrire :
  ∫₁³ f(x)dx = ∫₁³ f(t)dt = ∫₁³ f(u)du = ... • Le réel F(3) – F(1) est aussi noté [F(x)]₁³ Lire :« F(x) pris entre 1 et
  3». • Les réels 1 et 3 sont les **bornes** de l'intégrale. Pour toute fonction définie et continue sur [ab] [sic], on
  peut définir ∫ₐᵇ f(x)dx car elle admet une primitive sur [ab]. »
- **Act. 2** (p.150) : f continue sur I, a, b, c ∈ I, F primitive : calculer ∫ₐᵃ f ; comparer ∫ₐᵇ f et ∫ᵦᵃ f ; montrer
  ∫ₐᶜ f = ∫ₐᵇ f + ∫ᵦᶜ f.
- **Act. 3** (p.150) : h = αf + βg ; a) H = αF + βG primitive de h ; b) ∫ₐᵇ h = α∫ₐᵇ f + β∫ₐᵇ g.
- **Act. 4** (p.150–151) : u, v dérivables sur I ; 1) en intégrant (uv)′ = u′v + uv′, montrer
  [u(x)v(x)]ₐᵇ = ∫ₐᵇ u′v dx + ∫ₐᵇ uv′ dx ; 2) en déduire ∫ₐᵇ u(x).v′(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u′(x).v(x)dx.
- **Applications I** (p.151–152) : 1. justifier l'existence et calculer I = ∫₁² (4x³ − 3x² + 2x − 1)dx ; J = ∫₃⁵ 1/(t − 1) dt ;
  K = ∫_{π/2}^{−π/2} sin u du ; L = ∫₁^{−2} e^(2x) dx. 2. a) peut-on intégrer f : x ↦ 1/(x − 1) sur [0,2] ? pourquoi ?
  b) condition sur a et b pour que ∫ₐᵇ dt/(1 − t) existe. 3. f(x) = |2x − 3| : a) existence de ∫₀² f(x)dx ; b) écrire f
  sans valeur absolue puis calculer ∫₀³ |2x − 3| dx [sic : borne 3 ici, 2 en a)]. 4. a) I = ∫₋₁¹ 1/(x + 2) dx ;
  b) K = ∫₋₁¹ x/(x + 2) dx : calculer 2I + K, en déduire K. 5. par parties : a) ∫₁ᵉ ln(x) dx ; b) ∫₀^{π/2} x cos x dx.

**II. Intégrales et inégalités**
- **Act. 1** (p.152) : f continue positive sur I, a ≤ b. a) F primitive : F croissante, en déduire ∫ₐᵇ f ≥ 0 ; b) g ≤ h
  sur I : comparer ∫ₐᵇ g et ∫ₐᵇ h.
- **Act. 2** (p.152) : tableau de bord d'une voiture, distance x(t), vitesse v(t), x′(t) = v(t). a) vitesse moyenne v̄
  entre t₁ et t₂ ; b) distance parcourue = ∫_{t₁}^{t₂} v(t)dt ; exprimer v̄ par cette intégrale. Puis : « Plus
  généralement f étant une fonction continue sur un intervalle I, a et b deux réels distincts de I, on appelle **valeur
  moyenne** de la fonction f sur l'intervalle [a,b] le réel : f̄ = (1/(b − a))∫ₐᵇ f(t)dt = (F(b) − F(a))/(b − a) ».
- **Act. 3** (p.152) : m ≤ f(x) ≤ M sur [a,b] : montrer m ≤ (1/(b − a))∫ₐᵇ f(t)dt ≤ M. « Cette inégalité s'appelle
  **inégalité de la moyenne**. »
- **Act. 4** (p.152) : en appliquant le théorème des accroissements finis à F sur [a,b], montrer qu'il existe c ∈ [a,b]
  tel que ∫ₐᵇ f(x)dx = (b − a)f(c).
- **Applications II** (p.153–154) : 1. a) justifier ∫₋₂¹ 1/(x² + 1) dx ≥ 0 et ∫₁⁹ (−x² + 4√x − 3)dx ≥ 0 [sic ? voir
  doutes] ; b) pour x ∈ [1,2], 0 ≤ 1/(x³ + 1) ≤ 1/2 ; en déduire 0 ≤ ∫₁² dt/(t³ + 1) ≤ 1/2. 2. valeur moyenne de f sur
  [a,b] : a) f(x) = 3, x ∈ [−1,2] ; b) f(x) = sin x, x ∈ [0,π] ; c) f(x) = −x + 5, x ∈ [0, 5/2]. 3. intensité
  i(t) = 2 sin(120πt + π/2) : a) T = 1/60 est une période ; b) valeur moyenne de i sur cette période.

**III. Calculs d'aires planes** (« Activités préliminaires »)
- **Act. 1** (p.154) : figure de f : x ↦ 2x − 1 (points A, B, C, D sur l'axe, E, F, G sur la droite) ; « L'unité d'aire
  est celle d'un carré de longueur 1. » a) aire du triangle ACF puis ∫_{1/2}² f(x)dx, que remarque-t-on ? b) aire du
  trapèze BDGE puis ∫₁³ f(x)dx. Puis : « Plus généralement on admet que si f est une fonction continue et positive sur
  un intervalle [a,b] (a < b) alors l'aire de la partie limitée par la courbe de f, la droite des abscisses et les
  droites d'équation x = a et x = b a pour mesure ∫ₐᵇ f(x)dx » (figure hachurée).
- **Act. 2** (p.154–155) : a) f continue négative sur [a,b] : l'aire A de la partie hachurée a pour mesure −∫ₐᵇ f(x)dx ;
  b) figure de f : x ↦ x² − 4x + 3 : tableau de signe sur [0,3], aire hachurée, vérifier qu'elle vaut ∫₀³ |f(x)| dx.
- **Act. 3** (p.155) : f : x ↦ x + 1 et g : x ↦ (x − 1)² (figure, domaines D₁ et D₂). a) aire(D₁) = ∫₋₁⁰ [g(x) − f(x)]dx,
  aire(D₂) = ∫₀² [f(x) − g(x)]dx ; les calculer ; b) D = D₁ ∪ D₂ : aire de D, vérifier = ∫₋₁² |g(x) − f(x)| dx.
- **Applications III** (p.156) : 1. f(x) = eˣ : aire limitée par (C_f), l'axe des abscisses [« la droite de abscisses »
  sic] et x = −2, x = 1. 2. aire limitée par la courbe de f : x ↦ cos x, l'axe et x = −π/2, x = π. 3. f(x) = x − 1/x sur
  [1, +∞[ : aire entre (C), Δ (droite y = x, figure) et x = 1, x = e.

### Cours — Encadrés « A retenir » (VERBATIM, vérifiés sur l'image)

> **Définition** (p.151) — « f étant une fonction continue sur un intervalle I. On appelle intégrale de f entre a et b, le
> réel noté ∫ₐᵇ f(x)dx défini par: ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a) où a et b sont des réels de l'intervalle I et F une
> primitive de f sur I. »
> **Propriétés** — « ∫ₐᵃ f(x)dx = 0 ; ∫ₐᵇ f(x)dx = − ∫ᵦᵃ f(x)dx ; ∫ₐᶜ f(x)dx = ∫ₐᵇ f(x)dx + ∫ᵦᶜ f(x)dx (Relation de
> Chasles) ; ∫ₐᶜ [αf(x) + βg(x)]dx = α∫ₐᵇ f(x)dx + β∫ᵦᶜ g(x)dx (Linéarité de l'intégrale) » [sic : bornes a→c / a→b /
> b→c mélangées dans la ligne de linéarité ; l'Act. 3 donne la forme correcte ∫ₐᵇ(αf + βg) = α∫ₐᵇ f + β∫ₐᵇ g]
> **Intégration par parties** — « u et v étant deux fonctions dérivables sur un intervalle I, et a, b deux éléments de I
> on a : ∫ₐᵇ u(x).v′(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u′(x).v(x)dx » (hypothèse de continuité de u′, v′ non mentionnée).

> **Positivité** (p.153) — « Si a ≤ b et si f(x) ≥ 0 pour tout x ∈ [a,b], alors ∫ₐᵇ f(x)dx ≥ 0. Si a ≤ b et si
> f(x) ≤ g(x) pour tout x ∈ [a,b], alors ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx »
> **Valeur moyenne** — « f étant une fonction définie et continue sur un intervalle I, a et b deux réels distincts de I,
> on appelle valeur moyenne de f sur [a,b] et on note f̄ le réel : f̄ = (1/(b − a))∫ₐᵇ f(t)dt = (F(b) − F(a))/(b − a) »
> **Inégalité de la moyenne** — « f étant une fonction définie et continue sur un intervalle I, a et b deux réels de I, si
> pour tout réel x ∈ [a,b] on a : m ≤ f(x) ≤ M, alors m ≤ (1/(b − a))∫ₐᵇ f(t)dt ≤ M »
> **Égalité de la moyenne** — « f étant une fonction définie et continue sur un intervalle I, a et b deux réels de I, il
> existe au moins un réel c ∈ [a,b] tel que : ∫ₐᵇ f(x)dx = (b − a)f(c). Si a ≠ b alors l'égalité de la moyenne s'écrit :
> f̄ = f(c). »

> **Théorème** (p.155) — « f étant une fonction continue sur un intervalle [a,b] (a< b), et le plan étant rapporté à un
> repère orthonormé, l'aire de la partie du plan limitée par les droites d'équations x = a et x =b l'axe des abscisses et
> la courbe représentative de f a pour mesure A = ∫ₐᵇ |f(x)| dx. **En particulier** •Si f est positive sur [a,b] (a < b),
> alors A = ∫ₐᵇ f(x)dx •Si f est négative sur [a,b] (a < b), alors A = −∫ₐᵇ f(x)dx » (trois figures : f changeant de signe
> en c ; (f > 0) ; (f < 0)).

> **Théorème** (p.156) — « f et g étant deux fonctions continues sur[a,b] (a < b), et le plan étant rapporté à un repère
> orthonormé alors l'aire de la partie du plan limitée par les droites d'équations x = a et x = b, l'axe des abscisses
> [sic] et les courbes représentatives de f et g a pour mesure A = ∫ₐᵇ |g(x) − f(x)| dx. En particulier l'aire du domaine
> D = {M(x, y) / a ≤ x ≤ b et f(x) ≤ y ≤ g(x)} a pour mesure A = ∫ₐᵇ [g(x) − f(x)]dx » (figures (Cf), (Cg)).

### Apprendre à chercher (p.157)

- **Situation 1** : Iₙ = (1/n!)∫₀¹ (1 − x)ⁿ eˣ dx sur IN* [« la suite la suite » sic]. 1) I₁, I₂ ; 2) a) Iₙ₊₁ = Iₙ + 1/(n + 1)! [sic ? une intégration par parties donne Iₙ₊₁ = Iₙ − 1/(n + 1)!, vérifié à l'image p.157 le 2026-11-06] ;
  b) pour x ∈ [0,1], 0 ≤ 1 − x ≤ 1 ; c) (Iₙ) positive et croissante [sic ? décroissante avec la relation corrigée ; ne pas reprendre tel quel] ; 3) a) 0 ≤ Iₙ ≤ (e − 1)/n! (« On pourra utiliser
  2)b) ») ; b) limite de (Iₙ).
- **Situation 2** : **A)** f(x) = 1/(1 + x²), D = {M(x, y) / 0 ≤ x ≤ 1 et 0 ≤ y ≤ f(x)} (figure à rectangles, ordonnées
  1, 4/5, 1/2). 1) subdivision [0, 1/2], [1/2, 1] : montrer 13/20 < aire(D) < 9/10 ; 2) a) quatre intervalles
  [0,1/4], [1/4,1/2], [1/2,3/4], [3/4,1] : encadrement ; b) comparer ; 3) dix intervalles de même longueur.
  **B)** g(x) = tan x sur [0, π/4]. 1) a) tableau de variations, g admet une réciproque g⁻¹ définie sur [0,1] ;
  b) g⁻¹(0), g⁻¹(1) ; 2) g⁻¹ dérivable sur [0,1] et (g⁻¹)′(x) = 1/(1 + x²) ; 3) ∫₀¹ dx/(1 + x²) = π/4 ; 4) déduire de A et
  B un encadrement de π.

### Avec l'outil informatique (p.158)

« Un programme qui donne une valeur approchée de l'intégrale d'une fonction par la méthode des rectangles. La fonction f
est définie par : f(x) = 1/(1 + x²) ». Programme Pascal `Integration_Rectangles` : `function f(x:real):real; begin
f:=1.0 /(1.0+x*x) end;` ; `function Rectangles(a,b:real;n:integer):real;` avec `h:=(b-a)/n; x:=a+h/2.0; for k:=0 to
n-1 do begin somme:=somme+f(x); x:=x+h; end; Rectangles:=somme*h` (rectangles au **point milieu**) ; programme
principal : lecture de a, de b (`repeat … until b>a`), de n (`until n>0`), `writeln ('Valeur de l'intégrale est =
',Rectangles(a,b,n):0:12)`. (Coquilles du listing : `{Lafonction à integrer}`, `write('Borne inférieure (a) " ')`.)

### Exercices et problèmes (p.159–162) — 18 exercices

- **Ex. 1** (p.159) : « Cocher la bonne réponse » : 1) ∫₀ᵃ dx = (a) 0 (b) a² (c) a ; 2) ∫₋₁¹ (1/x)dx = (a) 0 (b) 2
  (c) n'existe pas ; 3) ∫₀¹ eˣdx = (a) 0 (b) e − 1 (c) e ; 4) ∫₋₁¹ x²dx = (a) 2/3 (b) 2 (c) 0 ; 5) ∫₀^π sin x dx = (a) π
  (b) 2 (c) 0.
- **Ex. 2** (p.159) : vrai ou faux : 1) ∫₀² x²dx > 0 ; 2) ∫₀^{−2} √(eˣ + 1) dx ≥ 0 ; 3) ∫₂³ ln x dx > 0 ; 4) ∫₁² (x + 4)dx ≥ 0.
- **Ex. 3** (p.159) : calculer A = ∫₁⁴ (x² − 1)/x dx ; B = ∫₀¹ (t² − t + 2)dt ; C = ∫ₑ^{e²} 1/(x ln x) dx ;
  D = ∫₁ᵉ (1/t)e^(ln t) dt ; E = ∫₀¹ (e^(3x) + 1)/eˣ dx ; F = ∫₁² e^(1/t)/t² dt ; G = ∫₀^{π/2} cos t e^(sin t) dt ;
  H = ∫_{−√2}^{√2} x e^(x²) dx ; I = ∫₁^{−1} 1/(4 + 2t)² dt ; J = ∫₋₁⁰ 1/(1 − 2t) dt ; K = ∫₀ˣ t/(1 + t)³ dt [sic : borne
  « x », variable libre] ; L = ∫₁ᵉ eˣ/(eˣ − 1) dx ; M = ∫₀¹ 1/(1 + t) dt ; N = ∫₀^{π/2} sin u/(1 + cos u) du.
- **Ex. 4** (p.159) : I = ∫₀¹ e^(−x)/(e^(−x) + eˣ) dx et J = ∫₀¹ eˣ/(e^(−x) + eˣ) dx : 1) I + J et J − I ; 2) I et J.
- **Ex. 5** (p.159) : population f(x) = 50·(1,04)ˣ sur [0 ; 10], x rang depuis 2000, f(x) en milliers : a) population après
  10 ans ; b) valeur moyenne entre 2000 et 2010.
- **Ex. 6** (p.159) : par parties : A = ∫₀¹ t e^(−2t) dt ; B = ∫₁ᵉ t ln t dt ; C = ∫₀^{ln2} (t² + 1)eᵗ dt ;
  D = ∫₁ᵉ x² ln x dx ; E = ∫₀^π t cos t dt ; F = ∫₁ᵉ ln x dx ; G = ∫₀¹ x²eˣ dx.
- **Ex. 7** (p.159–160) : I₀ = ∫₀^{π/2} sin t dt, Iₙ = ∫₀^{π/2} tⁿ sin t dt (n ∈ IN*). 1) a) I₀ ; b) I₁ par parties ; 2) Iₙ = n∫₀^{π/2} t^(n−1) cos t dt ; 3) a) pour n ≥ 2, Iₙ = n(π/2)^(n−1) − n(n − 1)Iₙ₋₂ ; b) I₂, I₃, puis
  J = ∫₀^{π/2} (1 − 2t + t² − t³) sin t dt.
- **Ex. 8** (p.160) : f(x) = (x³ − 3x² + x)/(1 − x), x ≠ 1. 1) réels a, b, c, d tels que f(x) = ax² + bx + c + d/(1 − x) ; 2) ∫₀^{1/2} f(x)dx.
- **Ex. 9** (p.160) : 1) n ≥ 1, ∫₀ⁿ e^(−t) dt ; 2) Uₙ = ∫₀ⁿ t e^(−t) dt (par parties) ; 3) Vₙ = ∫₀ⁿ t² e^(−t) dt :
  Vₙ = 2Uₙ − n²e^(−n) ; 4) lim Uₙ, en déduire lim Vₙ.
- **Ex. 10** (p.160) : ventes V(t) = 600/(1 + 3e^(−0,5t)), t en mois. 1) volume au début ; 2) volume maximum ; 3) volume
  moyen au cours des 4 premiers mois.
- **Ex. 11** (p.160) : f(x) = (eˣ − 2)/(eˣ + 1). 1) a, b tels que f(x) = a + beˣ/(eˣ + 1) ; 2) ∫₀^{ln2} f(x)dx.
- **Ex. 12** (p.160) : I = ∫₀¹ xeˣ/(1 + eˣ)³ dx. 1) A = ∫₀¹ eˣ/(1 + eˣ) dx et B = ∫₀¹ eˣ/(1 + eˣ)² dx ; 2) a, b (et c
  [sic : trois réels annoncés, deux utilisés]) tels que eˣ/(1 + eˣ)² = a/(1 + eˣ) + b/(1 + eˣ)² ; 3) en déduire
  J = ∫₀¹ 1/(1 + eˣ)² dx ; 4) en intégrant J par parties, exprimer I en fonction de J, en déduire I.
- **Ex. 13** (p.161) : f(x) = eˣ − 2 et g(x) = eˣ − e^(−x). 1) étudier f, g, tracer C_f, C_g (unité 2 cm) ; 2) point commun ; 3) λ ∈ IR* : aire A(λ) entre C_f, C_g, x = 0 et x = λ ; 4) limite de A(λ) en +∞, interprétation.
- **Ex. 14** (p.161) : f(x) = (3x² − x − 2)/(x + 2) sur I = ]−2 ; +∞[. 1) a, b, c tels que f(x) = ax + b + c/(x + 2) ; 2) variations, limites aux bornes, conséquence pour la courbe ; 3) asymptote oblique (D), position ; 4) tracer (unité
  2 cm) ; 5) a ≥ 1, A(a) = {M(x ; y) : 1 ≤ x ≤ a et 0 ≤ y ≤ f(x)} [sic ? voir doutes] : a) représenter A(3) ; b) vérifier
  ∫₁³ [f(x) − 3x + 7]dx = 12 ln(2/3) [sic ? voir doutes] ; aire de A(3) en cm² ; c) I(a) = ∫₁ᵃ [f(x) − 3x + 7]dx ; aire de
  A(a) en cm², limite quand a → +∞.
- **Ex. 15** (p.161) : 1) f(x) = (ax + b) ln(x + 1) sur ]−1, +∞[, (C) passe par B(1,0) et admet en O la tangente T : y = x
  (figure) : déterminer a et b ; 2) F(x) = x²/4 − 3x/2 − (x²/2 − x − 3/2) ln(x + 1) : a) F primitive de f s'annulant en 0 ;
  b) ∫₀¹ f(x)dx, interprétation géométrique.
- **Ex. 16** (p.161–162) : f(x) = (x − 1)eˣ, figure (C_f) hachurée sur [0, 2]. 1) par parties, I = ∫₀¹ f(x)dx et
  J = ∫₁² f(x)dx ; 2) aire A limitée par C_f, x = 0, x = 2 et y = 0.
- **Ex. 17** (p.162) : 1) par parties I = ∫₀^α (x − x²)eˣ dx (α ∈ IR₋) ; 2) f(x) = (x − x²)eˣ, (C) (unité 2 cm, figure) :
  a) aire A(α) en cm² de la région limitée par (C), (O, i⃗) [imprimé « (O, i⃗, j⃗) »] et x = α, x = 1 [sic ? (C) change de
  signe en 0 et 1] ; b) lim_{α→−∞} A(α).
- **Ex. 18** (p.162) : 1) Iₙ = ∫₀¹ xⁿe^(2x) dx (n ≥ 1) : a) I₁ = (e² + 1)/4 ; b) par parties 2Iₙ₊₁ + (n + 1)Iₙ = e² ;
  c) I₂, I₃. 2) f(x) = x²e^(2x), g(x) = x³e^(2x) : a) position relative ; b) aire entre (C_f), (C_g), x = 0, x = 1. 3) a) Iₙ ≥ 0, (Iₙ) décroissante ; b) en déduire e/(n + 3) ≤ Iₙ ≤ e/(n + 2) [sic ? voir doutes] ; lim nIₙ.

### Maths et culture (p.163)

Biographie : « **Bernhard Riemann** est né le 17 septembre 1826 à Hanovre. De 1847 à 1849, c'est à Berlin qu'il poursuit
ses études, avant de revenir à Göttingen préparer sa _Dissertation inaugurale_ (selon la terminologie allemande) sous la
direction de Gauss. Il la soutient en 1851 : elle concerne principalement la théorie des fonctions d'une variable
complexe, dont il s'intéresse particulièrement aux propriétés géométriques. Il donne notamment la définition de ce qu'on
nomme désormais une surface de Riemann. Dans la foulée, Riemann prépare son habilitation pour devenir Privat Dozent. Il
étudie désormais la représentation des fonctions par des séries trigonométriques, et au passage pose les jalons de
**l'intégrale de Riemann** : contrairement à Cauchy, il ne se limite plus aux fonctions c ontinues [sic]. » Puis
« **L'intégrale de Riemann d'une fonction continue** » : subdivision a = x₀ < x₁ < … < xₙ = b, somme de Riemann
Sₙ = (x₁ − x₀)f(c₁) + … + (xₙ − xₙ₋₁)f(cₙ), « xᵢ < cᵢ < cᵢ₊₁ » [sic, pour xᵢ₊₁] ; lim sₙ = ∫ₐᵇ f(x)dx « (le signe ∫ est dû
à Leibniz) » ; « • Toute fonction numérique continue sur [a,b] est intégrable au sens de Riemann sur cet intervalle.
• Une fonction numérique bornée sur [a,b] est intégrable au sens de Riemann sur cet intervalle si et seulement si ses
sommes de Riemann sont convergentes. » **Approximation** : pas h = (b − a)/n, xᵢ = a + i.h, cᵢ = xᵢ + h/2,
Sn = h.f(cᵢ) [somme sous-entendue], « i variant de 0 à n − 1 » ; méthode des rectangles (« converge "lentement" ») et
méthode des trapèzes (« interpolation linéaire »). (Le texte renvoie à une figure « en rose ci-dessus » absente de la
page.)

### Écart avec la référence (math-bac-sciences-exp/07 « Intégrales », manuel 222433 p.99–122 ; voisin : math-bac-techniques/08)

Correspondance **confirmée** : sciences-exp/07 (et techniques/08, de découpage presque identique).

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer)** :
- **volume d'un solide de révolution** (V = π∫f²) ;
- **fonction définie par une intégrale** F(x) = ∫ₐˣ f(t)dt (primitive s'annulant en a, F′ = f) comme notion de cours (ici
  seulement l'Ex. 15.2 « primitive qui s'annule en 0 » et la borne « x » de l'Ex. 3 K) ;
- **parité et périodicité** des intégrales (∫₋ₐᵃ f pour f paire/impaire, ∫ sur une période) — seule l'Appl. II.3 calcule une
  valeur moyenne sur une période ;
- corollaire strict de positivité, **|∫f| ≤ ∫|f|** ; l'introduction de l'intégrale par l'**aire** (ici l'intégrale est
  définie par F(b) − F(a), l'aire vient après en partie III) ;
- méthode des rectangles **en cours** avec rectangles inférieurs/supérieurs rᵢ, Rᵢ (ici : Situation 2 et programme
  Pascal au point milieu, et la lecture p.163) ;
- intégrales trigonométriques avancées (1/cos²x, tan²x, cos³x, cos x sin³x).

**Ce que ce manuel a en plus (ou autrement)** :
- **égalité de la moyenne** démontrée par le **théorème des accroissements finis** (Act. 4) ; motivation cinématique de la
  valeur moyenne (vitesse moyenne, Act. 2) ; valeur moyenne d'une **intensité de courant** (Appl. II.3) ;
- **modèles exponentiels** (population 50·1,04ˣ, ventes logistiques 600/(1 + 3e^(−0,5t))) ;
- **encadrement de π** par rectangles et ∫₀¹ dx/(1 + x²) = π/4 via la réciproque de tan (Situation 2) ;
- programme **Pascal** de la méthode des rectangles (point milieu) ; lecture « somme de Riemann », méthode des trapèzes ;
- intégrales combinant ln et exp (le ch. 6 ln et le ch. 7 exp précèdent ce chapitre ; dans la référence, les intégrales
  viennent avant ln/exp) ; décomposition en éléments simples guidée (Ex. 8, 11, 12, 14) ;
- QCM et Vrai/Faux placés comme Ex. 1–2.
- Vocabulaire/notations : « F(x) pris entre 1 et 3 », « variable muette », « bornes », « Relation de Chasles »,
  « Linéarité de l'intégrale », « Égalité de la moyenne », f̄ (barre) ; « [ab] » sans virgule (coquille).

### Bornes de scope (chapitre 8, section Sciences de l'informatique)

- ✅ INCLUS : intégrale ∫ₐᵇ f = F(b) − F(a) pour f continue, notation [F(x)]ₐᵇ, variable muette, bornes ; ∫ₐᵃ = 0,
  inversion des bornes, Chasles, linéarité ; existence (continuité sur [a, b]) ; intégration par parties (y compris
  répétée et pour des suites Iₙ) ; positivité, comparaison ; valeur moyenne, inégalité et égalité de la moyenne ; aire
  sous une courbe (f ≥ 0, f ≤ 0, signe quelconque ∫|f|), aire entre deux courbes ∫|g − f|, domaine
  {a ≤ x ≤ b, f(x) ≤ y ≤ g(x)}, aires en cm², aires dépendant d'un paramètre et leurs limites ; suites définies par une
  intégrale (exercices et Situation 1) ; encadrement d'aire par rectangles, approximation de π ; réciproque de tan
  (Situation 2 B).
- ⛔ EXCLU (absent de ces pages) : volumes de révolution ; fonction x ↦ ∫ₐˣ f(t)dt comme objet de cours ; parité /
  périodicité ; |∫f| ≤ ∫|f| ; sommes de Riemann exigibles (lecture seulement) ; méthode des trapèzes (citée en lecture) ;
  changement de variable ; intégrales impropres.

### Lecture

- **Pages lues en L1** : p.149 à 163 (15 pages).
- **Pages lues sur l'image (110 dpi)** : p.149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163 =
  **15/15 (100 %)** ; zooms 220–250 dpi : p.151 (bornes de K et L), p.153 (Appl. II.1 a), p.159 (Ex. 3), p.161 (Ex. 14 5b),
  p.162 (Ex. 18 3b).
- **Écarts texte/image** : L1 rend le signe ∫ par « & » et éclate les bornes sur la ligne précédente (toutes les
  intégrales reconstruites sur image) ; p.151 L1 « K = & 2 sin u du » (bornes π/2 → −π/2 perdues) ; p.152 L1 : la formule
  de f̄ est collée sous « Activité 3 » ; p.153 L1 perd √x (Appl. II.1) et les signes ≤ ; p.154–156 : figures (triangle ACF,
  trapèze BDGE, domaines D₁/D₂, aires hachurées) seulement sur image ; p.157 L1 « (g⁻¹)′(x) = 1 +1x » ; p.159–162 L1 sur
  deux colonnes entrelacées (Ex. 1/4, 2/5, 3/6, 7…, 13/14/15, 16/17/18 mêlés).
- **Coquilles [sic]** : « [ab] » (p.150) ; ligne « Linéarité » aux bornes incohérentes (p.151) ; Appl. I.3 borne 2 puis 3 ;
  « la droite de abscisses » (p.156) ; théorème aire entre deux courbes mentionnant « l'axe des abscisses » ; « la suite la
  suite » (p.157) ; Ex. 3 K borne « x » ; Ex. 12 « a, b et c » pour deux coefficients ; p.163 « c ontinues »,
  « xᵢ < cᵢ < cᵢ₊₁ », figure « en rose ci-dessus » absente ; listing p.158 « Lafonction », « (a) " ».
- **Doutes [?]** : (1) Appl. II.1 a p.153 : imprimé « ∫₁⁹ (−x² + 4√x − 3)dx ≥ 0 » (vérifié à 250 dpi). Tel qu'imprimé, l'énoncé est
  faux : l'intégrande est ≤ 0 sur [1, 9] (nul en 1, −16 + 8 − 3 < 0 en 4). Deux lectures sont possibles et le manuel
  ne permet pas de choisir : (a) l'exposant « ² » est la coquille, l'intégrande voulu étant −x + 4√x − 3 =
  −(√x − 1)(√x − 3), nul en 1 et en 9 (les bornes) et ≥ 0 sur [1, 9] (cohérent avec « justifier … ≥ 0 ») ; (b) le signe
  est la coquille, « ≤ 0 » au lieu de « ≥ 0 ». À l'adaptation, ne pas reprendre l'énoncé tel quel ;
  (2) Ex. 14 5b : imprimé « 12 ln(2/3) » (vérifié à 250 dpi) ; or f(x) − 3x + 7 = 12/(x + 2) donne 12 ln(5/3) ; de plus
  A(a) est défini « 0 ≤ y ≤ f(x) » alors que l'intégrale porte sur f(x) − (3x − 7) (aire entre (C_f) et (D)) : énoncé
  incohérent ; (3) Ex. 18 3b : imprimé « e/(n + 3) ≤ Iₙ ≤ e/(n + 2) » (vérifié à 250 dpi) ; la relation 2Iₙ₊₁ + (n + 1)Iₙ = e²
  donne e²/(n + 3) ≤ Iₙ ≤ e²/(n + 2) ; (4) Ex. 17 2a : région limitée par (C) et l'axe entre α ≤ 0 et 1 ; (C) est sous
  l'axe sur ]α, 0[ et au-dessus sur ]0, 1[ : aire = ∫|f|, non signalé dans l'énoncé ; (5) Ex. 2.2 : ∫₀^{−2} √(eˣ + 1)dx
  (bornes inversées, piège voulu).

## 2.9 Chapitre 9 — Arithmétique (manuel 222472, p.164–188)

**Page de garde (p.164)** — « Chapitre 9 », titre « ARITHMETIQUE ». Plan imprimé : « I . Divisibilité dans ℤ · II . Division
euclidienne · III . Congruences · IV . PGCD et PPCM de deux entiers · V . Théorème de Bézout · VI . Lemme de Gauss ·
VII. Application : résolution dans ℤ x ℤ d'équations du type ax+by = c où a, b et c sont des entiers relatifs ».
Illustration légendée « Euclide dans l'école d'Athènes de Raphaél (Musée du Vatican) ». Pas de citation.

**Plan du chapitre** : **Cours** p.165–179 — I. Divisibilité dans ℤ (p.165–166 : Activités préliminaires 1–3, Activités de
découverte 1–3, « A retenir », Applications 1–5) · II. Division euclidienne (p.167–168 : préliminaires 1–2, découverte
1–2, « A retenir », Applications 1–4) · III. Congruences (p.168–172 : découverte 1–4, encart Gauss 1801, « A retenir »,
Applications 1–8) · IV. PGCD et PPCM de deux entiers (p.172–174 : préliminaires 1–2, découverte 1–4, « A retenir » dont
algorithme d'Euclide, Applications 1–4) · V. Théorème de Bézout (p.174–176 : découverte 1–3, portrait « E Bézout »,
« A retenir », note historique Bachet de Méziriac, Applications 1–5) · VI. Lemme de Gauss (p.176–177 : découverte 1–4,
portrait « C . F Gauss (1777 - 1855) », « A retenir », Applications 1–3) · VII. Application : équations ax + by = c
(p.178–179 : activité de découverte non numérotée en 6 questions, encadré « Méthode de résolution », **Exercice
résolu** 62x + 43y = 1, Application a–d) · **Apprendre à chercher** (p.180 : Situations 1–2) · **Avec l'outil
informatique** (p.181–182 : tableur restes de 3ⁿ mod 11, Pascal Euclide, algorithme d'Euclide étendu au tableur et en
Pascal ; titre courant « Arithmique » [sic]) · **Exercices et problèmes** (p.183–187 : **36 exercices** numérotés 1 à 36,
le n° **11 étant imprimé deux fois** et le n° **12 absent** p.184 [sic] ; Ex. 2 = « QCM » ; liste des nombres premiers < 1000 p.187) · **Maths
et culture** (p.188 : « Ibn al-Haytham et le théoréme de Wilson »).

### Cours — Activités (une ligne chacune)

**I. Divisibilité dans ℤ**
- *Préliminaire* **Act. 1** (p.165) : pour tout n ∈ IN, 3^(n+5) − 3ⁿ est un multiple de 11.
- *Préliminaire* **Act. 2** : 1) 111 multiple de 37 ; 2) tout nombre de trois chiffres identiques est multiple de 37.
- *Préliminaire* **Act. 3** : 7892 + 2987 (nombre « à l'envers ») : multiple de 11 ? recommencer, expliquer.
- *Découverte* **Act. 1** (p.165) : droite réelle graduée ; 1) en vert E = {4k, k ∈ ℤ} ; 2) en rouge F = {(−4)k} ; constat.
  « ➢ Tout entier relatif de la forme 4k où k ∈ ℤ, s'appelle **multiple** de 4 dans ℤ. ➢ L'ensemble de multiples de a est
  identique à l'ensemble de multiples de (- a). » 3) somme de deux multiples de 4, propriété générale ; 4) deux multiples
  consécutifs 4k et le suivant, nombres compris entre eux.
- *Découverte* **Act. 2** : 1) quatre diviseurs distincts de a ≠ 0 ; 2) si b divise a alors −|a| ≤ b ≤ |a|, nombre fini de
  diviseurs.
- *Découverte* **Act. 3** (p.165–166) : a, b, c non nuls et différents de 1 : 1) a|b et b|a ⇒ a = b ou a = −b ; 2) transitivité ; 3) a|b et a|c ⇒ a | nb + mc (« aalors » [sic]).
- **Applications I** (p.166) : 1. diviseurs positifs de 72 ; 75 ; 83 ; 120 ; 200, puis diviseurs de 50 ; −56 ; −8 ; 63 ; 2. somme de trois entiers consécutifs divisible par 3 ; 3. n tel que n | n + 8 ; 4. n(n² − 1) multiple de 2 et de 3 ; 5. n tels que (n + 2)/(n − 4) ; (2n + 8)/(n − 2) ; (7n − 1)/(n + 3) ; (−6n + 3)/(n + 5) soient entiers.

**II. Division euclidienne**
- *Préliminaire* **Act. 1** (p.167) : division euclidienne de a par b : (2007, 35) ; (5000, 17) ; (18, 50).
- *Préliminaire* **Act. 2** : A = 13B + 50 : division euclidienne de A par 13 et de 3A + 20 par 13.
- *Découverte* **Act. 1** : 1) encadrer −37 entre deux multiples consécutifs de 11 (figure −44, −37, −33, flèches +7, +11) ; 2) −37 = −44 + 7 = 11 × (−4) + 7 (« **la division euclidienne de** −37 par 11. **Le reste** … est l'entier positif 7 ») ; 3) de −356 = 17 × (−20) − 16, compléter −356 = 17 × (….) + 1 ; 4) reste de −37 par −4 ; « De façon générale … trouver
  le couple (q ; r) d'entiers relatifs tels que : a = bq+r et 0 ≤ r < |b| » ; 5) division euclidienne de ±118 par ±23.
- *Découverte* **Act. 2** : 1) restes possibles ; 2) tout entier s'écrit 2k ou 2k + 1 ; 3) A = n(n² + 5) divisible par 3.
- **Applications II** (p.168) : 1. q et r pour (117, 28) ; (−317, 21) ; (−671, −6) ; « Sachant que 287025 = 635 x 452 + 5 » 2. quotient et reste de −287 025 par 635 et par 452 ; 3. restes de m et n par 11 : 2 et 7 ; restes de m + n, m − n,
  m² − n² ; 4. entiers naturels a, b, c tels que 59/3² = a + b/3 + c/3².

**III. Congruences**
- **Act. 1** (p.168) : « Le 1er janvier 2010 est vendredi, quel jour de la semaine sera le 20 mars 2015 ? »
- **Act. 2** (p.168–169) : entiers rangés par rangées de 2, 3, 4, 5 (quatre tableaux colorés par colonne) : propriété
  commune des entiers d'une même colonne.
- **Act. 3** (p.169) : 1) figure : −10, −4, 2, 8, 14, 20 (« divisés par 6 donnent un reste égal à 2 ») : différence de
  deux d'entre eux ; 2) a = nq + r, a′ = nq′ + r′ : même reste ⇔ a − a′ multiple de n (sens direct et réciproque). « ➢ On
  dit que a et a′ sont **congrus** modulo n, et on note a ≡ a′[n] (on lit a congru à a′ modulo n) ». Vérifier :
  a ≡ a[n] ; a ≡ r[n] (r reste) ; 14 ≡ 2[6] ; −2 ≡ 5[7] ; 27 ≡ −3[10].
- **Act. 4** (p.170) : prouver symétrie, transitivité, compatibilité avec +, −, ×, puissances aᵖ ≡ bᵖ[n] (p ∈ IN). Encart :
  « C'est en 1801 que Carl Friedrich Gauss a introduit la notion de congruence et le symbole ≡ ».
- **Applications III** (p.171–172) : 1. interpréter par congruences une droite graduée −3…8 surmontée de 1 2 3 0 1 2 3 0… ; 2. 1) écrire « a multiple de m » par une congruence ; 2) compléter 17 ≡ …[5] ; −3 ≡ …[8] ; 21 ≡ …[3] ; 3) vrai ? 27 ≡ 37[3] ;
  145 ≡ 1315[5] ; −5 ≡ −4[2] ; 3. vérifier 10 ≡ 3[7], 100 ≡ 2[7], 1000 ≡ −1[7], 10000 ≡ −3[7], 100000 ≡ −2[7], 1000000 ≡ 1[7] ;
  en déduire les multiples de 7 parmi 4 123 ; 321 083 ; 39 398 ; 1 111 117 ; 3 333 337 ; 4. 9 ≡ −1[10], chiffre des unités de
  9²ⁿ et 9^(2n+1) ; 5. 1) 9 | 7^(3n) − 1 ; 2) 2 × 35²⁰⁰⁶ − 3 × 84²⁰⁰⁷ ≡ 5[17] ; 6. restes de 32⁴⁵ par 7, 57383¹¹⁴ par 19,
  91234²⁰⁰⁷ par 7, 2006²⁰⁰⁸ par 2007 ; 7. a, b de restes 17 et 15 modulo 19 : restes de a + b, ab, 2a − 5b, a²b³ ; 8. 1) contre-exemples : c | a et a′, « a ≡ a′[n] » n'implique pas « a/c ≡ a′/c[n] » ; 2) si c | a, a′, n alors
  a ≡ a′[n] ⇒ a/c ≡ a′/c[n/c].

**IV. PGCD et PPCM de deux entiers**
- *Préliminaire* **Act. 1** (p.172) : diviseurs de 9 et 12 ; 9 ∧ 12 ; en déduire 63 ∧ 84 et 63 ∧ 147.
- *Préliminaire* **Act. 2** : 6 premiers multiples de 6 et 8 ; 6 ∨ 8 ; en déduire 30 ∨ 240 et 210 ∨ 240.
- *Découverte* **Act. 1** : diviseurs de 12 et de −18, diviseurs communs, PGCD noté « PGCD (12 ;-18) ou 12 ∧ (-18) ».
- *Découverte* **Act. 2** : D(a, b) ensemble des diviseurs communs : 1) D(a, b) = D(a − b, b) = D(a − kb, b) ; 2) 0 < b ≤ a :
  D(a,b) = D(r,b) ; 3) D(a, b) admet un plus grand élément d = PGCD, strictement positif ; PGCD(a, b) = PGCD(b,a) =
  PGCD(|a|,|b|) ; 4) PGCD(240,36) par la propriété 2) ; 5) PGCD(a, b) = PGCD(b, r).
- *Découverte* **Act. 3** : |ab| multiple commun ; existence du PPCM (« PPCM (a , b) ou a ∨ b ») ; PPCM(a, b) = PPCM(b, a) =
  PPCM(|a|, |b|).
- *Découverte* **Act. 4** (p.173) : 1) par l'algorithme d'Euclide multiplié par k : PGCD(ka, kb) = |k| PGCD(a, b) ; 2) a) d = PGCD(a, b) ⇒ a = da′, b = db′ avec a′ ∧ b′ = 1 ; b) réciproque ; « **la propriété caractéristique** du PGCD ».
- **Applications IV** (p.174) : 1. PGCD puis PPCM de (35, 84) ; (39, 52) ; (−60, 45) ; (18, −12) ; 2. par Euclide a ∧ b pour
  (441, 777) ; (2007, 9185) ; (1600, 259) ; 3. premiers entre eux ? (4847, 5633) ; (5617, 813) ; 4. sachant
  a ∧ b = b ∧ (a − b), calculer 1575 ∧ 210.

**V. Théorème de Bézout**
- **Act. 1** (p.174) : algorithme d'Euclide pour PGCD(145,55), puis remontée : (u ; v) tel que 145u + 55v = PGCD(145,55).
- **Act. 2** : G = {am + bn > 0, m, n ∈ ℤ} : 1) |a| ∈ G, plus petit élément D = au + bv ; 2) d | D, d ≤ D ; 3) a = Dq + r
  « avec 0 < r < D » [sic, 0 ≤ r] : r de la forme am + bn ; 4) r = 0, D | a ; 5) D | b, D = d.
- **Act. 3** (p.174–175) : 1) tout diviseur commun divise le PGCD ; 2) a ∧ b = 1 ⇔ ∃ u, v : au + bv = 1 ; 3) ax + by = c
  (c ≠ 0) a des solutions entières ⇔ c multiple de PGCD(a,b).
- **Applications V** (p.175–176) : 1. méthode de remontée pour 212 ∧ 87 (« Etape 1 : 212 = 2 x 87 + 38 ; Etape 2 :
  87 = 2 x 38 + 11 ; Etape 3 : 38 = 3 x 11 + 5 ; Etape 4 : 11 = 2 x 5 + 1 ; Etape 5 : 5 = 5 x 1 ») : déduire u₂, v₂ … u₅, v₅
  tels que 38 = au₂ + bv₂, 11 = au₃ + bv₃, 5 = au₄ + bv₄, 1 = au₅ + bv₅ ; 2. a = 4, b = 9 : (−2 ; 1), (7 ; −3), (97 ; −43)
  vérifient au + bv = 1 ; 3. premiers entre eux : (n, 2n + 1) ; (2n + 3, 3n + 5) ; (n² + 1, n) ; 4. (n³ + 1)² = n²(n⁴ + 2n) + 1,
  donc n³ + 1 et n⁴ + 2n premiers entre eux ; 5. solution particulière par Euclide de 726x + 137y = 1 et 2017x + 1771y = 1.

**VI. Lemme de Gauss**
- **Act. 1** (p.176) : a | bc et a premier avec b : 1) bc = ka ; 2) c = a(cu + kv), a | c ; 3) énoncer le résultat de Gauss.
- **Act. 2** : 1) a | c, b | c, a ∧ b = 1 ⇒ ab | c ; 2) a premier avec b₁, …, b_k ⇒ premier avec leur produit.
- **Act. 3** (p.176–177) : d = PGCD, m = PPCM : a = da′, b = db′ ; da′b′ multiple commun ; M = ka = k′b ⇒ ka′ = k′b′,
  a′ | k′ ; tout multiple commun est multiple de da′b′, m = d|a′b′| ; exprimer PGCD × PPCM.
- **Act. 4** (p.177) : 1) par Bézout, diviseurs communs = diviseurs de d ; 2) multiples communs = multiples de m ; 3) (ka ∨ kb) = |k|(a ∨ b).
- **Applications VI** (p.177) : 1. d = a ∧ b par Euclide puis m = a ∨ b pour (576, −480) ; (225, 350) ; (−845, −234) ; 2. a ∧ b = 1 : a) aᵐ et bⁿ premiers entre eux ; b) diviseurs d | a, d′ | b premiers entre eux ; 3. x ∧ n = 1 :
  ax ≡ a′x[n] ⇒ a ≡ a′[n].

**VII. Application : résolution dans ℤ × ℤ de ax + by = c**
- **Activité de découverte** (p.178) : 1) pourquoi 37x + 27y = 1 a des solutions ; 2) solution particulière par Euclide ; 3) solution particulière (x₀ ; y₀) de (E) : 37x + 27y = 1000 ; 4) toute solution vérifie 37(x − x₀) = −27(y − y₀) ; 5) par Gauss, x = x₀ + 27k, y = y₀ − 37k ; 6) ensemble des solutions.
- **Exercice résolu** (p.178–179) : (E) 62x + 43y = 1. 1) Euclide : 62 = 43 × 1 + 19 (4) ; 43 = 19 × 2 + 5 (3) ;
  19 = 5 × 3 + 4 (2) ; 5 = 4 × 1 + 1 (1) ; PGCD(62,43) = 1, (E) a des solutions (Bézout). 2) Remontée : (1′) 5 = 4 × 1 + 1 ;
  19 × 1 = 5 × 4 − 1 (2′) ; 43 × 4 = 19 × 9 + 1 (3′) ; 62 × 9 = 43 × 13 − 1 (4′) ; « Conclusion : 62 x (−9) + 43 x 13 = 1,
  donc (−9 ; 13) = (x₀;y₀) est une solution particulière de (E). » 3) Solution générale : « soit encore :
  62( x - xo ) = 43 (y - yo) (E ') » [sic : signe − manquant] ; 62 | y − y₀ (lemme de Gauss), 43 | x − x₀ ;
  y − y₀ = 62k et x − x₀ = 43l ; l = k ; « conclusion : x = xo + 43 k = − 9 + 43 k et y = yo − 62 k = 13 − 62 k »
  [sic : incohérent avec y − y₀ = 62k posé juste avant ; la conclusion finale est juste] ; réciproque « il est clair ».
- **Application VII** (p.179) : tous les couples solutions de a) 10x + 13y = 1 ; b) 42x + 35y = 7 ; c) 120x + 26y = 2 ;
  d) 39x − 52y = 3.

### Cours — Encadrés « A retenir » (VERBATIM, vérifiés sur l'image)

> **Définitions** (p.166) — « Soient a et b deux entiers relatifs. On dit que a **est un multiple de** b s'il existe un
> entier relatif k tel que a = kb. Si b ≠ 0, dire que b divise a signifie qu'il existe un entier relatif k tel que a = k b,
> c'est à dire, que a est un multiple de b. »
> **Remarques** — « • Les multiples d'un entier a sont les nombres : 0, a, 2a, …., k a …et 0, -a -2a, …, -k a, …
> • Tout entier relatif a non nul et différent de 1 admet au moins quatre diviseurs entiers relatifs : 1, -1, a , -a.
> • Si a ≠ 0, tout diviseur b de a vérifie −|a| ≤ b ≤ |a|. • Tout entier relatif non nul a divise 0, mais 0 ne divise acun
> [sic] entier relatif. »
> **Propriétés** — « a,b et c désignent des entiers relatifs non nuls. • Si a divise b alors -a divise b. • Si a divise b et
> b divise a alors a =b ou a= -b . • Si a divise b et b divise c alors a divise c . • Si a divise b, alors pour tout entier
> relatif non nul k , ka divise kb. • Si a divise b et c, alors pour tous entiers relatifs n et m, a divise nb +mc . »

> **Théorème (admis)** (p.168) — « Soit a un entier relatif et b un entier relatif non nul. Il existe un unique couple (q,r)
> d'entiers relatifs vérifiant à la fois : a = bq + r et 0 ≤ r < |b|. »
> **Définitions** — « Soit a un entier relatif et b un entier relatif non nul. Effectuer **la division euclidienne de a par
> b**, c'est trouver le couple d'entiers relatifs (q,r) tels que : a = bq+r et 0 ≤ r < |b|. q est **le quotient**, r est
> **le reste**, a s'appelle le **dividende** et b le **diviseur**. »
> **Remarques** — « Si a = bq+r et 0 ≤ r < |b|. • b divise a si et seulement si le reste r est nul. • Le reste ne peut
> prendre que l'une des valeurs parmi 0 ; 1 ; 2 ;…. ; |b|-1. • b étant fixé, les entiers relatifs peuvent être classés selon
> leur reste dans la division euclidienne par b . »

> **Définition** (p.170) — « Soit n un entier naturel non nul, a et b deux entiers relatifs. On dit que a et b sont
> **congrus modulo n** lorsque a et b ont le même reste dans la division euclidienne par n. On note : a ≡ b (modulo n) ou
> a ≡ b[n] »
> **Théorème** — « Soit n un entier naturel non nul, a et b deux entiers relatifs. On a : a ≡ b[n] si, et seulement si,
> a - b **est multiple de n**. »
> **Remarque** — « • n étant un entier naturel non nul, si r est le reste dans la division euclidienne de a par n alors
> a ≡ r[n] mais une relation a ≡ r[n] ne permet de conclure que r est le reste dans la division euclidienne de a par n que
> dans le cas où 0 ≤ |n| » [sic : phrase tronquée, pour 0 ≤ r < n]
> **Propriétés** (p.170–171) — « Soient n un entier naturel non nul et a,b , c, d des entiers relatifs. 1) a ≡ a[n]
> 2) Si a ≡ b[n] alors b ≡ a[n]. 3) Si a ≡ b[n] et b ≡ c[n] alors a ≡ c[n]. 4) Si a ≡ b[n] et c ≡ d[n] alors
> a + c ≡ b + d[n] et a - c ≡ b - d[n]. 5) Si a ≡ b[n] et c ≡ d[n] alors a × c ≡ b × d[n]. 6) Si a ≡ b[n] alors
> aᵖ ≡ bᵖ[n] pour tout p ∈ IN »
> **Remarque** — « Pour l'addition, la soustraction et la multiplication les règles de calculs sur les égalités se
> transmettent aux congruences. »

> **Définitions** (p.173) — « Soient a et b deux entiers relatifs non nuls. 1) Le plus grand entier qui divise à la fois a
> et b s'appelle **le plus grand commun diviseur** ou **PGCD** de a et b . On le note a ∧ b . 2) Le plus petit entier
> strictement positif qui est à la fois multiple de a et b s'appelle **le plus petit commun multiple** ou **PPCM** de a et b .
> On le note a ∨ b 3) Deux entiers relatifs non nuls a et b sont **premiers entre eux** lorsque leur PGCD est égal à 1. »
> **Propriétés** — « 1) Soient a et b deux entiers relatifs non nuls. Pour tout k entier relatif non nul, PGCD( k a, k b) =
> |k| PGCD( a , b). 2) Soit a et b deux entiers relatifs non nuls et d un entier naturel non nul. d = PGCD (a, b) si, et
> seulement si, a = da′ et b = db′ avec a′ et b′ entiers premier entre eux. »
> **L'algorithme d'Euclide** — « Le résultat suivant permet de calculer d = PGCD (a, b) sous forme algorithmique. Soit a et
> b deux entiers naturels non nuls. Considérons la suite des divisions euclidiennes : • de a par b : a = bq₀ + r₀ • de b par
> r₀ (si r₀ ≠ 0) : b = r₀q₁ + r₁ • de r₀ par r₁ (si r₁ ≠ 0) : r₀ = r₁q₂ + r₂ • de rₙ₋₁ par rₙ (si rₙ ≠ 0) : rₙ₋₁ = rₙqₙ₊₁ + rₙ₊₁
> Lorsque b ne divise pas a, le PGCD de a et b est le **dernier reste non nul** obtenu par cet algorithme. Si b divise a
> alors PGCD(a,b) = b. »
> **Remarque** — « Pour b ≠ 0 PGCD( 1,b) = 1 et , PGCD(0,b) = |b| Si a et b sont deux entiers non nuls tels que b divise a
> alors PPCM( a , b) = |a| »

> **Théorème** (p.175) — « a et b désignent deux entiers relatifs non nuls et d leur PGCD. Il existe deux entiers relatifs u
> et v tels que au + bv = d . »
> **Théorème de Bézout** — « a et b désignent deux entiers relatifs non nuls. a et b sont premiers entre eux si, et
> seulement si, il existe deux entiers relatifs u et v tels que : au + bv =1. L'égalité au + bv =1 s'appelle **relation de
> Bézout** (ou identité de Bézout *) »
> **Remarque** — « Le théoréme de Bézout est un théorème d'existence mais pas d'unicité. »
> **Conséquences** — « Soit a et b deux entiers relatifs non nuls 1) tout diviseur commun à a et b divise leur PGCD.
> 2) l'équation ax + by = c (c entier fixé non nul) admet des solutions entières si, et seulement si c est multiple de
> PGCD (a, b) . »
> Note : « *Ce théorème fut en fait énoncé pour les entiers par Bachet de Méziriac (1581-1638), mais fut ensuite démontré
> et utilisé dans d'autres domaines par Etienne Bézout (1730-1783). »

> **Lemme de Gauss** (p.177) — « Soit a, b et c trois entiers relatifs non nuls. Si **a divise b.c** et si **a et b sont
> premiers entres eux**, alors **a divise c.** »
> **Propriétés** — « Soit a et b deux entiers relatifs non nuls, alors on a : 1) (a ∧ b) (a ∨ b) = |ab| . 2) (ka ∨ kb) =
> |k|(a ∨ b). 3) L'ensemble des diviseurs communs à a et b est l'ensemble des diviseurs de a ∧ b 4) L'ensemble des multiples
> communs à a et b est l'ensemble des multiples de a ∨ b »

> **Méthode de résolution** (p.178, encadré) — « Méthode de résolution, dans ℤ x ℤ, de l'équation ax + by = c où a, b et c
> sont des entiers relatifs. 1) On détermine d = PGCD(a,b). 2) Si c n'est pas un multiple de d, on en déduit que l'équation
> n'a pas de solutions entières. Sinon, on divise a, b et c par d. on obtient alors une équation de la forme Ax + By = C ,
> avec A et B premiers entre eux. 3) On détermine une solution particulière (u ,v) de l'équation. Pour cela, on peut
> déterminer une solution particulière de l'équation ax + by = d ( équivalente à Ax + By = 1 ) à l'aide de l'algorithme
> d'Euclide et multiplier les nombres obtenus par c/d = C . 4) On écrit { Ax + By = C ; Au + Bv = C } En soustrayant membre
> à membre, on obtient l'équation : A (x-u) = -B (y-v). A et B étant premiers entre eux, d'après le théorème de Gauss,
> y-v = kA d'où par substitution x- v = - k B [sic, x − u]. Finalement l'ensemble des solutions est l'ensemble des couples
> de la forme : (u-kB;v+kA)où k désigne un entier relatif arbitraire. »

### Apprendre à chercher (p.180)

- **Situation 1 : Résolution de l'équation ax ≡ b (modulo n)** : 1) s'il existe une solution, a ∧ n divise b ; 2) réciproque ; 3) (C) : 9x ≡ 15 (modulo 24) : a) existence ; b) 9x ≡ 15 (mod 24) ⇔ 3x ≡ 5 (mod 8) ; c) 3x ≡ 5 (mod 8) ⇔
  x ≡ 7 (mod 8) ; d) solutions de (C) ; 4) résoudre 6x ≡ 6 (modulo 21) ; −3x ≡ 15 (modulo 13).
- **Situation 2 : Critères usuels de divisibilité** (a = aₙ10ⁿ + … + a₁10 + a₀) : 1. par 9 (10ⁿ ≡ 1 (mod 9), a ≡ somme des
  chiffres [9]) ; 2. par 3 ; 3. par 4, par 25 (deux derniers chiffres) ; 4. trouver un critère par 8 et par 125 ; 5. par 11
  (10ⁿ ≡ 1 si n pair, ≡ −1 si n impair ; différence des sommes de chiffres de rang impair et pair) ; « Le nombre 4 792 178
  est-il divisible par 11 ? » ; 6. par 7 : n = 10a + b = 7(a + b) + 3(a − 2b), n divisible par 7 ⇔ a − 2b divisible par 7 ;
  parmi 25 718 ; 62 216 ; 46 663 ; 38 983.

### Avec l'outil informatique (p.181–182)

- **1.** Tableur « Restes de a^n par b » (zone de saisie a = 3, b = 11 ; n = 0…5 ; a^n = 1, 3, 9, 27, 81, 243 ; restes 1, 3, 9, 5,
   4, 1) : formules « =$C$3^B5 et =MOD(C5 ;$D$3) » recopiées vers le bas pour déceler une périodicité.
- **2.** Turbo Pascal `Program euclide ; var r,t,q,z :longint ; … repeat q:=r div t; z :=r ;r :=t ;t :=z-q*t until t=0 ;
   Writeln('Le PGCD est' ,r) ;` pour a = 16 170, b = 9450 puis a = 195 728, b = 178 211.
- **3.** « Algorithme de calcul de coefficients u et v dans la relation de Bézout » : a) pour 0 ≤ k ≤ n, ∃ u_k, v_k :
   au_k + bv_k = r_k, définis par récurrence ; b) programmation au tableur ; exemple a = 78, b = 35 (quotients 2, 4, 2, 1, 2 ;
   restes 8, 3, 2, 1, 0 ; u : 1, −4, 9, −13 ; v : −2, 9, −20, 29) ; formules (QUOTIENT, MOD, SI(D3=0 ; ' ' ; …)) ; 2) Turbo Pascal `program coef_ besout` (u, v, u1, v1, r, r1, q, z) [« besout » sic ; `v1` non déclaré, `d0` pour `do` sic].

### Exercices et problèmes (p.183–187) — 36 exercices (numéros 1 à 36 ; « 11 » imprimé deux fois, « 12 » absent)

- **Ex. 1** (p.183) : Vrai ou Faux, justifier : a) divisible par 4 et 15 ⇒ par 60 ; b) 1111m = 1515n ⇒ m multiple de 1515 ;
  c) PGCD de 2001²⁰⁰⁷ et 2007²⁰⁰¹ est 3¹⁹⁹⁵ ; d) reste de 2¹⁰⁰ par 11 est 1 ; e) u₀ = 3, uₙ₊₁ = 2uₙ − 1 ; v₀ = 1, vₙ₊₁ = 2vₙ + 3 :
  termes de même indice impair ont pour PGCD 5 ; f) ∃ k : 36³⁶ = 37k + 1 ; g) 27ᵃ = 3 × 3ᵇ ⇒ a et b premiers entre eux ;
  h) c | ab, a premier ⇒ c | b ; i) PPCM = produit ⇒ premiers entre eux.
- **Ex. 2 (QCM)** (p.183) : a) 2007x − 19y = 1, x, y naturels < 1000 : nombre de solutions 0 ; 1 ; 53 ; 152 ; b) terrain
  rectangulaire, côtés entiers de PGCD 6, aire 3024 m² : nombre de périmètres possibles 3 ; 4 ; 5 ; 6 ; c) a. ab′ − a′b = 1 ⇒
  a/b et a′/b′ irréductibles ; b. ab′ − a′b = 2 ⇒ irréductibles ; c. fractions non irréductibles ⇒ ab′ − a′b ≠ 1 ;
  d) PGCD 12, quotients successifs 8, 2, 8 : le plus grand nombre est A. 1524 ; B. 1728 ; C. 2007 ; e) « Sachant que
  123 ≡ 0 (modulo 3) » : a. 123²⁰⁰⁵ − 1 ; b. 124²⁰⁰⁶ − 1 ; c. 125²⁰⁰⁷ − 1 divisible par 3 ?
- **Ex. 3** : reste par 7 de 999888777666555444333222111 et de 999888777666555444333222111000.
- **Ex. 4** : pour n ≥ 1 : a) 3^(2n+1) + 2^(n+2) divisible par 7 ; b) 3^(2n) + 2^(6n−5) par 11 ; c) 3·5^(2n−1) + 2^(3n−2) par 17.
- **Ex. 5** : 1) n³ + 5n multiple de 6 ; 2) en déduire n³ + 17n − 12 et n³ + 2009n multiples de 6.
- **Ex. 6** : 1) d | n ⇒ aᵈ − 1 divise aⁿ − 1 (a ≥ 1) ; 2) 2²⁰⁰⁸ − 1 divisible par 3, 15 et 255.
- **Ex. 7** : d | 7a + 5b et d | 4a + 3b ⇒ d | a et d | b.
- **Ex. 8** (p.184) : x entier tel que a) x − 2 | x + 5 ; b) x + 7 | 2x + 15 ; c) x − 1 | x² ; d) x + 1 | x³ + 2.
- **Ex. 9** : dividende < 900, quotient 72, reste 12 : diviseur et dividende ? pourquoi pas de solution.
- **Ex. 10** : restes de a et b par 11 : 2 et 7 ; restes de a + b, a − b, a² − b².
- **Ex. 11 (1er)** : 1) 20072007 divisible par 137 et 73 ; 20082008 ? 2) nombre de 4 chiffres juxtaposé avec lui-même ;
  calculer 137 × 73, justifier.
- **Ex. 11 (2e, à la place du n° 12)** : 1) a) 2x² − 2x + 1 = 0 sans solution réelle ; b) −21, −13, 34, 112 solutions de (1) 2x² − 2x + 1 ≡ 0
  (modulo 5) ; 2) a) x solution ⇔ ∃ k : 2x² − 2x + 1 − 5k = 0 (2) ; b) discriminant, il faut p² + 1 ≡ 0 (modulo 10) ; p
  modulo 10 ; c) solutions de (1) ; 3) suites arithmétiques de premiers termes −1 et 2, raison 5.
- **Ex. 13** : vérifier 2¹³ ≡ 1[13] [sic ? voir doutes] et 3⁶ ≡ 1[13] ; en déduire 13 | 2⁷⁰ + 3⁷⁰.
- **Ex. 14** : a) 7² ≡ −1 (modulo 10) ; b) chiffre des unités de 1 + 7 + 7² + … + 7⁴⁰⁰.
- **Ex. 15** : a ≡ b[c] ⇒ PGCD(a, c) = PGCD(b, c) ; réciproque ?
- **Ex. 16** : vrai ou faux : x² + x ≡ 0 (modulo 6) ⇒ x ≡ 0 (modulo 3).
- **Ex. 17** : restes possibles par 8 du carré d'un entier ; n ∈ ℤ tels que (n + 3)² ≡ 1[8].
- **Ex. 18** : pourquoi visiblement faux : PGCD(1602; 1846) = 3 ; PGCD(1714; 3026) = 1 ; PGCD(15; 23) = 7 ;
  PGCD(132; 63) = 63 ; PGCD(2121; 111) = 140 ; PGCD(121; 128) = 8.
- **Ex. 19** : a, b naturels non nuls, PGCD 8, a + b = 144.
- **Ex. 20** (p.185) : a = 2n², b = n(2n + 1) : 2n et 2n + 1 premiers entre eux ; PGCD de a et b.
- **Ex. 21** : ab = 1734 et PGCD 17.
- **Ex. 22** : PGCD et PPCM de a = 5^(n+2) − 5ⁿ et b = 7^(n+2) − 7ⁿ.
- **Ex. 23** : systèmes dans IN : a) xy = 1512, PPCM(x; y) = 252 ; b) x + y = 276, PPCM = 1440 ; c) xy = 16128, PGCD = 24.
- **Ex. 24** : résoudre 2PGCD(a ; b) = 111 (a, b naturels) [« pas de solution » attendu : 111 impair].
- **Ex. 25** : couples (a ; b), 0 < a < b, 2PPCM(a ; b) + 3PGCD(a ; b) = 78, a ne divise pas b.
- **Ex. 26** : a) PGCD(a,b) = 1 ⇒ PGCD(aⁿ, b) = 1 ; b) ⇒ PGCD(aⁿ, bⁿ) = 1 ; c) réciproque ?
- **Ex. 27** : couples (x ; y) de a) 10x + 13y = 1 ; b) 5x + 3y = 1 ; c) 30x + 35y = 100 ; d) 9x − 15y = 1.
- **Ex. 28** : n ∈ ℤ (n ≠ 7 [sic ?]), aₙ = n + 7, bₙ = 3n − 4 : 1) 3aₙ − bₙ, PGCD(aₙ, bₙ) divise 25 ; 2) dₙ = PGCD(aₙ, 25) ; 3) a) dₙ = 5 ⇔ n ≡ 3[5] ; b) dₙ = 25 ⇔ n ≡ 18[25] ; 4) sinon aₙ et bₙ premiers entre eux.
- **Ex. 29** : 1) n ≡ 1[7] : a) p tel que n³ ≡ p[7] ; b) 7 | n³ + 1 [sic ? n ≡ 1 donne n³ − 1] ; 2) m ≡ 4 (mod 7) ⇒ 7 | m³ − 1 ; 3) A = 1999³ + 2007³ : a) 1999 ≡ 4 (mod 7) ; b) plus petit p tel que 2007 ≡ p (mod 7) ; c) 7 | A sans calcul.
- **Ex. 30** : n = 10a + b : 13 | n ⇔ 13 | a + 4b ; application à 569 556 ; 8 888 ; 6 666 ; 6 567.
- **Ex. 31** (p.186) : n = 10a + b : 17 | n ⇔ 17 | a − 5b ; application à 16 831 ; 152 592 ; 16 983 ; 83 521.
- **Ex. 32** : 2¹¹ − 1 premier ? S = 1 + 2ᵖ + 2²ᵖ + … + 2^(p(q−1)) ; 2^(pq) ≡ 1[2ᵖ − 1] ; 2^(pq) − 1 divisible par 2ᵖ − 1 et
  2^q − 1 ; si 2ⁿ − 1 premier alors n premier ; réciproque ? « nombres de MERSENNE ».
- **Ex. 33** : pièces de 13 et 4 unités : 1) payer toute somme entière (avec rendu) ; 2) « Si on ne rend pas la
  monnaie, quelle est la plus grande somme qu'il est possible de payer ? » [sic ? la question attendue est la plus grande
  somme **impossible** à payer].
- **Ex. 34** : 38 allumettes, prises de 1 à 4, celui qui prend la dernière perd : stratégie gagnante du premier joueur ;
  valable pour tout nombre initial ?
- **Ex. 35** (p.186–187) : code ISBN (10 chiffres, clé = reste de S = a₁ + 2a₂ + … + 9a₉ par 11, « X » pour 10) : 1) compléter ISBN 9973 - 719 - 55 - 7, 2 - 7427 - 0008, 0 - 691 - 05729 ; 2) code 2 - 70 - 031999 - 7 erroné : a) détection ;
  b) inversion → 2 - 07 - 031999 - 7 cohérent ? 3) 2 - 85368 - 313 - 2, erreur sur le chiffre de gauche ; 4) algorithme en
  langage naturel ; 5) vrai/faux (a)–(d) ; 6) réciproque de (d) ; 7) transposition a₂ ↔ a₃ : S − S′, valeurs possibles,
  congruence modulo 11, conclusion.
- **Ex. 36** (p.187) : « si PGCD(a ; b) = 1 alors PGCD(a² ; b²) = 1 » ; Sₙ = Σ_{p=1}^{n} p³ : 1) Sₙ = (n(n + 1)/2)² ; 2) n = 2k : a) PGCD(S₂ₖ ; S₂ₖ₊₁) = (2k + 1)² PGCD(k² ; (k + 1)²) ; b) PGCD(k ; k + 1) ; c) PGCD(S₂ₖ ; S₂ₖ₊₁) ; 3) n = 2k + 1 :
  a) 2k + 1 et 2k + 3 premiers entre eux ; b) PGCD(S₂ₖ₊₁ ; S₂ₖ₊₂) ; 4) unique n pour lequel Sₙ et Sₙ₊₁ premiers entre eux.
- **Liste** (p.187) : « La liste des nombres premiers inférieurs à 1000 (sa consultation ne peut que faciliter la résolution
  de certains exercices). 2-3-5-11-13-… -997 » (**7 omis** [sic]).

### Maths et culture (p.188)

« Ibn al-Haytham et le théoréme de Wilson » — texte historique (signé « Recherches sur l'histoire des mathématiques
arabes ( R. RAHED) » [sic, Rashed]) : citation latine de Waring (1770) « Sit n numerus primus, & (1.2.3.4...(n − 2)(n − 1) + 1)/3
[sic : /n] erit integer numerus, e.g. (1.2 + 1)/3 = 1, (1.2.3.4 + 1)/5 = 5, (1.2.3.4.5.6 + 1)/7 = 103 … » ; Wilson n'avait pas
de démonstration ; formulation antérieure chez Leibniz (G. Vacca) : « Si p est un nombre premier, alors (p-2)! ≡ 1(mod p) » ;
démonstration par Lagrange (1771), dont la réciproque : « Si n > 1, les deux conditions suivantes sont équivalentes:
a) n est premier b) (n-1)! ≡ −1(mod n) » ; Ibn al-Haytham (965-1040) l'énonce au Xᵉ siècle en résolvant le système
x ≡ 1 (mod mᵢ), x ≡ 0 (mod p), p premier, 1 < mᵢ ≤ p − 1 (« cas particulier du célèbre théorème chinois »). Vignette
« Diophanti Alexandrini Arithmeticorum ».

### Écart avec la référence (math-bac-math/16 « Divisibilité dans ℤ » + math-bac-math/17 « Identité de Bézout », manuel 222446)

Correspondance **confirmée** : ce chapitre unique fusionne les deux chapitres de la section Mathématiques (seule section
de référence ayant l'arithmétique).

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer)** :
- **petit théorème de Fermat** (cité et exploité dans bac-math/16 et 17) et nombres de Fermat ; application
  **RSA** / chiffrement ; (nombres de Carmichael, indicatrice d'Euler et suite de Fibonacci : exercices du manuel bac-math,
  absents du cours publié — l'indicatrice n'apparaît que dans 17/exercices/04-defi.json ; rien à retirer du cours) ;
- **inverses modulo b** comme notion de cours (ici seulement la Situation 1 « ax ≡ b (mod n) ») ;
- **systèmes de deux congruences** x ≡ a (mod m), x ≡ b (mod n) (restes chinois partiels) — évoqués seulement dans la
  lecture p.188 ;
- **tableaux de congruence** systématiques et résolution de x² ≡ c (mod n) par balayage (ici seulement Ex. 11 bis,
  16, 17) ; **partie entière** dans la division euclidienne ; recherche du PGCD à la calculatrice (ab/c) ; **associativité**
  du PGCD ; équations 25x² − 9y² = k par factorisation.

**Ce que ce manuel a en plus (ou autrement)** :
- un seul chapitre « Arithmétique » en 7 parties avec **lemme de Gauss** en partie propre et partie VII **méthode de
  résolution de ax + by = c** en encadré + exercice résolu par **remontée** de l'algorithme d'Euclide (méthode des
  équations (1′)…(4′)) ;
- démonstration de Bézout par le **plus petit élément de G = {am + bn > 0}** (Act. V.2) ;
- **outil informatique** fourni : tableur des restes de aⁿ, programmes Turbo Pascal (Euclide, Euclide étendu
  `coef_besout`), tableur QUOTIENT/MOD/SI pour u_k, v_k — à rapprocher de la section Informatique ;
- **critères de divisibilité** par 3, 9, 4, 25, 8, 125, 11, 7 (Situation 2), par 13 et 17 (Ex. 30–31) ;
- applications « concrètes » : calendrier (Act. III.1), **code ISBN** (Ex. 35), jeu des allumettes (Ex. 34), pièces 13/4
  (Ex. 33), **nombres de Mersenne** (Ex. 32) ; somme des cubes et PGCD(Sₙ, Sₙ₊₁) (Ex. 36) ;
- lecture « théorème de **Wilson** » (Waring, Leibniz, Lagrange, Ibn al-Haytham) ;
- notations : « a ∧ b » (PGCD), « a ∨ b » (PPCM), « a ≡ b[n] » et « a ≡ b (modulo n) » ; « premiers entre eux »,
  « relation de Bézout (ou identité de Bézout) » ; PGCD défini pour a, b **non nuls** (Remarque : PGCD(0,b) = |b|).

### Bornes de scope (chapitre 9, section Sciences de l'informatique)

- ✅ INCLUS : multiples et diviseurs dans ℤ, propriétés (±, transitivité, combinaisons linéaires) ; division euclidienne
  dans ℤ (théorème admis, 0 ≤ r < |b|) ; congruences modulo n (définition par même reste, caractérisation a − b multiple
  de n, réflexivité/symétrie/transitivité, compatibilité +, −, ×, puissances) ; restes de grandes puissances,
  chiffre des unités, jour de la semaine ; critères de divisibilité (3, 9, 4, 25, 8, 125, 11, 7, 13, 17) ; PGCD (a ∧ b),
  algorithme d'Euclide, PGCD(ka, kb) = |k|PGCD(a, b), caractérisation a = da′, b = db′ ; PPCM (a ∨ b), (a ∧ b)(a ∨ b) = |ab|,
  (ka ∨ kb) = |k|(a ∨ b) ; diviseurs/multiples communs ; entiers premiers entre eux ; théorème « au + bv = d », théorème de
  Bézout, conséquences (existence de solutions de ax + by = c ⇔ PGCD | c) ; algorithme d'Euclide étendu (remontée,
  récurrence u_k, v_k) ; lemme de Gauss et corollaires (ab | c ; premier avec un produit) ; résolution complète de
  ax + by = c ; congruence linéaire ax ≡ b (mod n) (Situation 1) ; nombres de Mersenne, ISBN (exercices) ; programmes
  Pascal/tableur.
- ⛔ EXCLU (absent de ces pages) : petit théorème de Fermat ; théorème de Wilson (lecture seulement) ; inverses modulaires
  comme notion ; théorème chinois / systèmes de congruences (lecture seulement) ; décomposition en facteurs premiers et
  théorème fondamental (les nombres premiers n'ont pas de section : seulement Ex. 1h, 32 et la liste p.187) ;
  ℤ/nℤ ; indicatrice d'Euler ; RSA.

### Lecture

- **Pages lues en L1** : p.164 à 188 (25 pages).
- **Pages lues sur l'image (110 dpi)** : p.164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
  180, 181, 182, 183, 184, 185, 186, 187, 188 = **25/25 (100 %)** ; zoom 250 dpi : p.184 (Ex. 13).
- **Écarts texte/image** : L1 rend « ≡ » par « ' » et les crochets [n] par « » ou rien (toutes les congruences
  reconstruites sur image) ; L1 perd ℤ (« k . », « dans x ») partout ; p.165 L1 « 3n + 5 3n » pour 3^(n+5) − 3ⁿ ; p.166
  « − a ≤ b ≤ a » sans valeurs absolues ; p.168 « 0 ≤ r < b » sans |b| (encadré) ; p.172 L1 « 6 * 8 » et « 12 , (-18) » pour
  ∨ et ∧ ; p.173 L1 perd |k| ; p.169 tableaux colorés (rangées de 2 à 5) et droite graduée lus sur image ; p.171 Appl. 5–6
  exposants (35²⁰⁰⁶, 32⁴⁵, 57383¹¹⁴…) détachés par L1 ; p.180 L1 « 3x ≡ 15 (modulo 13) » sans le signe − ; p.181–182
  tableurs (valeurs) uniquement sur image ; p.183–187 colonnes entrelacées (Ex. 1/2, 8/13, 11/14…, 20/27, 31/35, 35/36).
- **Coquilles [sic]** : « aalors » (p.166), « acun » (p.166), « premier entre eux » (p.173), « premiers entres eux »
  (p.177), « théoréme » (p.175, p.188), « Arithmique » (titre courant p.181–182), « reste da la division » (p.169) ;
  Remarque p.170 tronquée « dans le cas où 0 ≤ |n| » ; « x − v = −kB » (p.178) ; exercice résolu : « 62(x − x₀) = 43(y − y₀) »
  sans le signe −, et « y − y₀ = 62k » puis « y = y₀ − 62k » ; Act. V.2 « 0 < r < D » ; numéro **11 en double** (p.184) ;
  liste des premiers sans **7** ; formule de Waring « /3 » ; « R. RAHED » ; « coef_ besout », « d0 », `v1` non déclaré.
- **Doutes [?]** : (1) Ex. 13 : « 2¹³ ≡ 1[13] » imprimé (vérifié à 250 dpi) ; or 2¹³ ≡ 2 (mod 13) ; 2¹² ≡ 1 attendu (et
  2⁷⁰ + 3⁷⁰ ≡ 2¹⁰ + 3⁴ ≡ 10 + 3 ≡ 0 fonctionne avec 2¹²) ; (2) Ex. 29 1b : n ≡ 1[7] donne n³ ≡ 1, donc 7 | n³ − 1 et non
  n³ + 1 (coquille probable ; 2) avec m ≡ 4 donne bien m³ − 1) ; (3) Ex. 24 : 2PGCD = 111 n'a pas de solution (sans doute
  voulu) ; (4) Ex. 28 « n ≠ 7 » imprimé alors que aₙ = n + 7 s'annule en −7 ; (5) Ex. 33 2) libellé ambigu (« la plus grande
  somme qu'il est possible de payer ») : la question attendue est la plus grande somme **impossible** à payer ; (6) numérotation p.184 : colonne gauche 8, 9, 10, 11, **11** ; colonne
  droite 13 à 19 : le second « 11 » tient la place du 12 (aucune case « 12 » imprimée). Décompte : **36 exercices** ;
  à l'adaptation, renuméroter le second 11 en 12.

## 2.10 Chapitre 10 — Nombres complexes (manuel 222472, p.189–208)

**Page de garde (p.189)** — « Chapitre 10 », titre « NOMBRES COMPLEXES ». Plan imprimé : « I . Définition et propriétés ·
II . Représentation géométrique d'un nombre complexe · III . Conjugué d'un nombre complexe · IV . Module d'un nombre
complexe · V . Equations dans ℂ ». Portrait légendé « Cardan Girolamo (Jérôme) 1501-1576 ». Pas de citation.

**Plan du chapitre** : **Cours** p.190–201 — I. Définition et propriétés (p.190–192 : préliminaires 1–2, découverte 1–2,
« A retenir », Applications 1–4) · II. Représentation géométrique (p.192–194 : découverte 1–3, « A retenir » avec figure,
Applications 1–2) · III. Conjugué (p.194–196 : découverte 1–4, « A retenir » avec figure M(z), M′(−z), M″(z̄), M‴(−z̄),
Applications 1–3) · IV. Module (p.196–198 : découverte 1–3, « A retenir » avec figure du parallélogramme z + z′,
Applications 1–3) · V. Equations dans ℂ (p.198–201 : préliminaires 1–2 ; **1. Equations du second degré dans ℂ** :
découverte 1–5, « A retenir », Applications 1–3 ; **2. Equations de degré supérieur à deux dans ℂ** : découverte 1–2,
encadré « Point méthode », Applications 1–3) · **Apprendre à chercher** (p.202 : Situations 1–2 avec « Vers une
solution ») · **Avec l'outil informatique** (p.203 : deux programmes Turbo Pascal + applications) · **Exercices et
problèmes** (p.204–207 : **19 exercices** numérotés 1 à 19, **« 11 » imprimé deux fois et « 12 » absent** p.205 [sic] ;
Ex. 1 = « VRAI-FAUX », Ex. 2 = « QCM » ; p.206 porte le bandeau « Cours » [sic]) · **Maths et culture** (p.208 : dal
Ferro, Bombelli, √−1). **Ni argument, ni forme trigonométrique ou exponentielle** dans tout le chapitre.

### Cours — Activités (une ligne chacune)

**I. Définition et propriétés**
- *Préliminaire* **Act. 1** (p.190) : 1) (2 + √3)(2 − √3) ; 2) écrire 1/(2 + √3) et (1 + 2√3)/(2 + √3) sous la forme
  a + b√3 (a, b rationnels).
- *Préliminaire* **Act. 2** : résoudre dans IN, ℤ, ℚ, IR : x + 1 = 0, 2x + 1 = 0, x² − 2 = 0.
- *Découverte* **Act. 1** : 1) x² + 1 = 0 dans IR. Texte : « ➢ L'équation x² + 1 = 0 n'admet pas des solutions dans IR.
  • On suppose qu'il existe un ensemble noté ℂ contenant IR, appelé ensemble des nombres complexes, et dans lequel
  l'équation x² + 1 = 0 admet une solution. Cette solution notée i n'est pas un nombre réel; c'est **un imaginaire pur**.
  • Tout élément de ℂ s'écrit sous la forme a+ i b où a et b sont deux réels et i² = - 1 • On définit dans ℂ une addition et
  une multiplication ayant les mêmes propriétés que celles définies dans IR. » 2) résoudre dans ℂ x² + a = 0 (a > 0).
- *Découverte* **Act. 2** : 1) z = 2 − 3i, z′ = 1 + i : 3z, z + z′, z − z′, zz′ ; 2) cas général z + z′, z − z′, z.z′ ; 3) a) (1 + i)(1 − i) ; b) 1/(1 + i) et (2 − 3i)/(1 + i) ; 4) a) (a′ + ib′)(a′ − ib′) = (a′)² + (b′)² ; b) 1/z′ et z/z′.
- **Applications I** (p.191–192) : 1. z = 3 + 2i, z′ = 2 + i : z + z′, z − z′, 3z − 5z′, z.z′, 1/z′, z/z′ ; 2. 1) forme
  algébrique de (1 − 2i) − (3 + i) ; (1 + i)² ; (1 + i)³ ; (3 + i)(3 − i) ; (a + i)(a² − ia + i²), a ∈ IR ; 2) réel x tel que
  x² + 3x − 3 + i(x + 2) = 1 − 2i ; 3. résoudre z − 2i = iz + 5 ; 2z(z − i) = 0 ; (z − 2i)/(z + 3) = 2 − i ; 4. i³ … i⁸ ;
  i⁵⁰, i⁵⁷, i²⁰⁰⁰, i²⁰⁰⁷ ; (1 + i)², (1 − i)², (1 + i)⁵⁰, (1 − i)⁵⁰.

**II. Représentation géométrique d'un nombre complexe**
- **Act. 1** (p.192) : z₁ = 1 + 2i, z₂ = −2 + 3i, repère orthonormé (O, e⃗₁, e⃗₂) : 1) placer A(Re(z₁), Im(z₁)),
  B(Re(z₂), Im(z₂)) ; « ➢ Les points A et B … s'appellent les **images** … les nombres complexes z₁ et z₂ s'appellent les
  **affixes** … On note Aff(A) = z₁ ; on lit : affixe de A est égal à z₁ ou encore A(z₁) ; on lit : A d'affixe z₁ » ; 2) a) affixes de C(1, 3), D(0, −2), E(√2, 0), F(1/2, 0) ; b) points des axes ; 3) a) affixe du milieu I de [AB] ;
  b) (z₁ + z₂)/2, conclure.
- **Act. 2** : u⃗ = xe⃗₁ + ye⃗₂, OM⃗ = u⃗, z = x + iy « est aussi appelé affixe du vecteur u⃗. On le note : Aff(u⃗) ou z_u⃗ ». 1) a) M tel que OM⃗ = AB⃗ ; b) Aff(AB⃗) = z_B − z_A ; 2) Aff(I) = (z_A + z_B)/2.
- **Act. 3** (p.193) : coordonnées de ku⃗ et u⃗ + v⃗ ; Aff(ku⃗) = k Aff(u⃗), Aff(u⃗ + v⃗) = Aff(u⃗) + Aff(v⃗).
- **Applications II** (p.194) : 1. figure (A(2 + i), B(−1 + 2i), C(−i) lus sur la grille) : 1) affixes de A, B, C ; 2) milieu I de [BC] ; 3) D symétrique de A par rapport à I ; 4) ABDC parallélogramme ; 5) E tel que EB⃗ = OA⃗. 2. z = (a − 2) + i(2a − b) : ensemble des M(a, b) tels que z soit a) réel ; b) imaginaire pur ; c) nul.

**III. Conjugué d'un nombre complexe**
- **Act. 1** (p.194) : M(2 + 3i), M′ symétrique par rapport à l'axe réel ; « ➢ Le nombre complexe trouvé z′ = 2 - 3 i
  s'appelle **conjugué** de z et se note par z̄ ».
- **Act. 2** : 1) conjugués de 1 + i ; 3 ; 2 − 3i ; 2i ; 4i − 3 ; 3 − 2√3 ; i√5 ; 2) conjugué d'un réel, d'un imaginaire pur.
- **Act. 3** (p.194–195) : 1) z = 1 + 2i, z′ = −2 + i : a) calculs de z̄, z̄′, conjugués de z + z′, z − z′, zz′, 1/z′, z/z′ ;
  b) vérifier les égalités ; 2) cas général : conjugué d'une somme, différence, produit ; b) conj(1/z′) = 1/z̄′ (via
  z′.(1/z′) = 1) ; c) conj(z/z′) = z̄/z̄′.
- **Act. 4** (p.195) : u⃗(z = a + ib), v⃗(z′ = a′ + ib′) non nuls : 1) z̄z′ = (aa′ + bb′) + i(ab′ − a′b) = u⃗.v⃗ + i det(u⃗, v⃗) ; 2) u⃗, v⃗ colinéaires ⇔ z̄z′ réel ; orthogonaux ⇔ z̄z′ imaginaire pur.
- **Applications III** (p.196) : 1. 1) conjugués (forme algébrique) de √5 ; −3 ; 3i ; −7i ; 1 + 3i ; −5 − i ; (3 − 5i)/2 ;
  2i − 3 ; (1 + i)²⁰⁰⁸ ; (5 − 2i)/i ; 1/i ; (5 + i)/(3 − i) ; 2) écrire sous la forme (a + ib)ⁿ : conj((2 − 3i)¹⁷) ;
  conj((3 + i)/(4 + 3i)) ; conj((3 + i)²⁰/(4 + 3i)²⁰) ; 2. A(z = 1 + ia), B(z′ = 1 − ia), a ∈ ℂ : 1) z̄.z′ = 1 − aā − i(a + ā) ; 2) a) O, A, B alignés ⇔ Re(a) = 0 ; b) OA⃗ ⊥ OB⃗ ⇔ aā = 1 ; 3. Z = z + 1/z (z ≠ 0) : ensemble des M(z) tels que Z réel.

**IV. Module d'un nombre complexe**
- **Act. 1** (p.196) : z_A = −2i, z_B = 2 − 3i : 1) placer ; 2) OB et √(z_B z̄_B) ; 3) AB et √((z_B − z_A)·conj(z_B − z_A)) ; 4) OM et √(z z̄) ; « ➢ Le réel positif √(z z̄) s'appelle **module** du nombre complexe z et se note par |z| » ; 5) comparer AB et |z_N − z_M| [sic : M et N introduits, « AB » écrit].
- **Act. 2** : |z + z′| ≤ |z| + |z′| (interprétation géométrique, inégalité triangulaire).
- **Act. 3** (p.197) : |zz′| = |z||z′| ; |1/z′| = 1/|z′| ; |z/z′| = |z|/|z′|.
- **Applications IV** (p.197–198) : 1. z_A = √3 + i ; z_B = √2 + i√2 ; z_C = 1 + i√3 : modules, A, B, C sur un même cercle
  (centre, rayon) ; 2. z_A = i ; z_B = −4 − i ; z_C = −2 + 5i : placer, affixes Z₁, Z₂, Z₃ de AB⃗, BC⃗, CA⃗, modules, nature
  de ABC ; 3. 1) ensemble des M(z) : |z − 2i| = |z + 3| ; 2) a) |z − 3i| = 3 ; b) en déduire |z̄ + 3i| = 3 et |z̄ − 3i| = 3.

**V. Equations dans ℂ**
- *Préliminaire* **Act. 1** (p.198) : 1) factoriser dans IR si possible x² + 4 ; x² − 3 ; −x² + 9 ; 2x² − 3x − 5 ; 2) x³ − 8 = 0
  dans IR ; 3) 3x⁴ + 4x² − 7 = 0 dans IR.
- *Préliminaire* **Act. 2** : f(x) = 3x³ + x² + 2x − 6 : 1) 1 racine ; 2) f(x) = 0 dans IR.
- **1. Second degré** — **Act. 1** : 1) −4 = (2i)², z² = −4 ; 2) a) z² + 2z + 5 = (z + 1)² + 4 ; b) z² + 2z + 5 = 0.
- **Act. 2** : z² = 0 ; z² = m (m ∈ IR*₊) ; z² = m (m ∈ IR*₋).
- **Act. 3** (p.199) : z = x + iy : z² = 3 + 4i ⇔ {x² − y² = 3 ; xy = 2} ; solutions de z² = 3 + 4i.
- **Act. 4** : z, z′ non réels : z = z′ ⇔ {a = a′ ; |z| = |z′| ; bb′ > 0} ; application à z² = 3 + 4i.
- **Act. 5** : (E) az² + bz + c = 0 (a ≠ 0, coefficients complexes) ; forme canonique a[(z + b/(2a))² − (b² − 4ac)/(4a²)],
  Δ = b² − 4ac ; 1) cas Δ = 0 ; 2) Δ ≠ 0 : « Δ admet deux racines carrées δ et (−δ) » ; deux solutions.
- **Applications V.1** (p.200) : 1. 1) racines carrées de 3 ; −5 ; 7 + 24i ; 2) a) (1 + i)² et (1 − i)² ; b) racines carrées de
  i ; 3i ; −i ; −7i ; 2. résoudre z² + z + 1 = 0 ; z² − (2 + i)z + 2i = 0 ; 3. factoriser (2 − i)z² − (2 + i)z + 2i ;
  iz² + √2 z − i.
- **2. Degré supérieur à deux** — **Act. 1** (p.200) : 1) a) (3 + 4i)² ; b) 2z² + 3z + 2 − 3i = 0 ; 2) (E) 2z⁴ + 3z² + 2 − 3i = 0
  en posant Z = z².
- **Act. 2** (p.201) : (E) z³ + z² + z + 1 = 0 : 1) −1 solution ; 2) a, b, c tels que z³ + z² + z + 1 = (z + 1)(az² + bz + c) ; 3) résoudre.
- **Applications V.2** (p.201) : 1. z³ + 8 = 0 ; z³ + 3iz² − 3z − i = 0 ; z⁴ + (1 − 2i)z² − 2i = 0 ; 2. (E) z³ + (√3 − i)z² +
  (1 − i√3)z − i = 0 : 1) i solution [« Vésrifier » sic] ; 2) b, c réels avec (z − i)(z² + bz + c) ; 3) résoudre ; 3. P(z) = z³ 1 [sic, pour z³ − 1] : 1) j = −1/2 + i√3/2 : 1, j, j̄ racines ; 2) A(1), B(j), C(j̄) : a) ABC équilatéral ; b) centre de gravité.

### Cours — Encadrés « A retenir » (VERBATIM, vérifiés sur l'image)

> **Théorème et définition** (p.191) — « Il existe un ensemble, appelé ensemble des nombres complexes et noté ℂ, vérifiant
> les propriétés suivantes : •L'ensemble ℂ contient l'ensemble IR . • L'ensemble ℂ est muni d'une addition et d'une
> multiplication qui vérifient les mêmes propriétés que l'addition et la multiplication dans IR. • L'ensemble ℂ contient un
> nombre non réel noté i tel que i² = -1. • Tout élément z de [ℂ, symbole absent à l'impression] s'écrit de maniére unique :
> z = a + i b où a et b sont des réels. »
> **Vocabulaire et notation** — « L'écriture z = a + i b, où a et b sont des réels, s'appelle forme algébrique (ou
> cartésienne) du nombre complexe z . Le réel a est appelé **la partie réelle** de z et noté Re(z) . Le réel b est appelé
> **la partie imaginaire** de z et noté Im(z). Si a = 0, alors z est appelé imaginaire pur. »
> **Conséquences** — « Soit z et z′ deux nombres complexes. • z est réel si et seulement si Im(z) = 0 . • z est imaginaire
> pur si et seulement si Re(z) = 0. • z = 0 si et seulement si Re(z) = Im(z) = 0. • z = z′ si et seulement si
> Re(z) = Re(z′) et Im(z) = Im(z′). »
> **Propriétés: Opérations dans ℂ** — « Soient z = a + i b et z′ = a′ + i b′ avec a, b, a′ et b′ des réels. • z + z′ =
> (a + a′) + i (b + b′) • z - z′ = (a - a′) + i (b - b′) • z .z′ = (a a′ - b b′) + i (a b′ + b a′) Si en plus z′ ≠ 0 alors on
> a : • 1/z′ = a′/(a′² + b′²) + i (−b′)/(a′² + b′²) • z/z′ = (aa′ + bb′)/(a′² + b′²) + i (ba′ − ab′)/(a′² + b′²) »
> Encart : « Les calculs dans ℂ se font de la même manière que les calculs dans IR en remplaçant i² par ( - 1) chaque fois
> que le cas se présente. Dans la pratique, on ne retient pas les formules de l'inverse et du quotient, on fait intervenir
> l'égalité : (x + i y)(x - i y) = x² + y² »

> **Théorème** (p.193) — « Le plan est rapporté à un repère orthonormé (O, e⃗₁, e⃗₂). • A tout nombre complexe z = a + i b,
> où a et b sont des réels, on associe un unique point M(a, b) du plan. • A tout point M(a, b) du plan, on associe un unique
> nombre complexe z = a + ib. »
> **Vocabulaire et notation** — « • Le nombre complexe z = a + ib est appelé affixe du point M(a, b) et est noté Aff(M) ou
> z_M. • Le point M(a, b) est appelé l'image du nombre complexe z = a + i b et on note M(z). »
> **Remarques** — « • A tout vecteur u⃗(a, b) du plan on associe un unique nombre complexe z = a + ib. Le nombre complexe
> z = a + ib est appelé affixe du vecteur u⃗ ; on le note Aff(u⃗) ou z_u⃗ . • Lorsqu' on repère un point ou un vecteur dans un
> repère orthonormé par son affixe, on dit qu'on se place dans **le plan complexe**. »
> **Conséquences** — « Soient M et M′ deux points d'affixes respectives z et z′. • (M et M′ sont confondus) signifie
> (z = z′). • z est réel si et seulement si M appartient à la droite des abscisses, appelée **axe réel**. • z est imaginaire
> pur si et seulement si M appartient à la droite des ordonnées, appelée **axe imaginaire.** • Les points d'affixes z et
> (- z) sont symétriques par rapport à O. »
> **Propriétés** — « • Si A et B sont deux points du plan, on a : Aff(AB⃗) = Aff(B) − Aff(A) • Pour tous vecteurs u⃗ et v⃗ du
> plan et pour tout réel k, on a : Si I est le milieu de [AB] alors Aff(I) = (Aff(A) + Aff(B))/2 ; Aff(ku⃗) = k Aff(u⃗) ;
> Aff(u⃗ + v⃗) = Aff(u⃗) + Aff(v⃗) » (figure : axe réel, axe imaginaire, M(z), u⃗ — étiquettes « axe réel » / « axe imaginaire »
> placées de façon ambiguë sur la figure).

> **Définition** (p.195) — « Le conjugué du nombre complexe z = a + i b, où a et b sont des réels, est le nombre complexe
> z̄ = a - i b. »
> **Remarques** — « Les points d'affixes z et z̄ sont symétriques par rapport à l'axe des abscisses. • 1/z = z̄/(z.z̄) »
> **Propriétés** — « Pour tous nombres complexes z , z′ et tout entier naturel non nul n, on a : conj(z̄) = z ;
> conj(z + z′) = z̄ + z̄′ ; conj(zz′) = z̄ z̄′ ; conj(zⁿ) = (z̄)ⁿ. Pour tous nombres complexes z et z′ (z′ ≠ 0) et tout entier
> naturel n, on a : conj(1/z′) = 1/z̄′ ; conj(z/z′) = z̄/z̄′ ; conj(1/(z′)ⁿ) = 1/(z̄′)ⁿ • z + z̄ = 2 Re(z) ; z − z̄ = 2i Im(z)
> • z est réel ⇔ z = z̄ • z est imaginaire pur ⇔ z = - z̄ . »
> **Théorème** — « Le plan complexe est rapporté à un repère orthonormé (O, e⃗₁, e⃗₂). Soient u⃗ et v⃗ deux vecteurs non nuls
> d'affixes respectives z et z′ on a: • u⃗ et v⃗ sont colinéaires ⇔ z̄ z′ est réel • u⃗ et v⃗ sont orthogonaux ⇔ z̄ z′ est
> imaginaire pur »

> **Définition** (p.197) — « Le plan complexe est muni d'un repère orthonormé (O, e⃗₁, e⃗₂). Soit z un nombre complexe de
> forme algébrique a + i b et M le point d'affixe z. On appelle module du nombre complexe z et on note |z| le réel positif
> √(z z̄). On a : |z| = √(z z̄) = OM = √(a² + b²) »
> **Remarques** — « •Pour tout réel x, |x| pourra être lu indifféremment "valeur absolue de x" ou "module de x" • Pour tout
> nombre complexe z imaginaire pur, si z = i y, avec y un réel, alors |z| = |y| »
> **Conséquences** — « • |z| = 0 ⇔ z = 0 Pour tous nombres complexes z et z′ et tout réel k, on a : • |Re(z)| ≤ |z| ;
> |Im(z)| ≤ |z| ; |z + z′| ≤ |z| + |z′| • |z| = |z̄| = |−z| = |−z̄| • Si A et B sont deux points du plan complexe alors
> AB = |z_B − z_A| » (figure : O, A(z), B(z′), C(z + z′)).
> **Propriétés** — « • Pour tous nombres complexes z et z′ et tout entier naturel non nul n, on a : |z z′| = |z| |z′| ;
> |k z| = |k||z| ; |zⁿ| = |z|ⁿ • Pour tous nombres complexes z et z′ (z ≠ 0) et tout entier naturel n, on a : |1/z| = 1/|z| ;
> |z′/z| = |z′|/|z| ; |1/zⁿ| = 1/|z|ⁿ »

> **Théorème** (p.199) — « Soient z et z′ deux nombres complexes non réels de formes algébriques z = a + i b et
> z′ = a′ + i b′, on a : z = z′ ⇔ { a = a′ ; |z| = |z′| ; bb′ > 0 } »
> **Théorème 1 (admis)** — « Soit a un nombre complexe non nul. L'équation z² = a admet dans ℂ, deux solutions opposées .
> Les solutions de l'équation z² = a sont appelées les racines carrées de a. »
> **Théorème 2** (p.199–200) — « Soit T(z) = a z² + b z + c, où a, b et c sont des nombres complexes, tels que a ≠ 0. Soit
> Δ = b² - 4 a c le discriminant de T(z) • Si Δ = 0 alors l'équation T(z) = 0 admet une seule solution z = −b/(2a) • Si
> Δ ≠ 0 alors l'équation T(z) = 0 admet deux solutions dans ℂ : z′ = (−b + δ)/(2a) et z″ = (−b − δ)/(2a) où δ est une racine
> carrée de Δ. »
> **Remarque** — « Les solutions de l'équation T(z) = 0 sont aussi appelées les racines du polynôme T(z). »
> **Cas particulier : a, b et c sont des réels** — « • Si Δ > 0, alors z′ = (−b + √Δ)/(2a) et z″ = (−b − √Δ)/(2a) • Si Δ < 0,
> alors z′ = (−b + i√−Δ)/(2a) et z″ = (−b − i√−Δ)/(2a) »
> **Remarques** — « Soit T(z) = a z² + b z + c, où a, b et c sont des nombres complexes, tels que a ≠ 0. • Si z′ et z″ sont les
> solutions de l'équation T(z) = 0 alors on a: z′ + z″ = −b/a ; z′ . z″ = c/a ; T(z) = a z² + b z + c = a (z - z′) (z - z″)
> • Si a + b + c = 0, alors l'équation T(z) = 0 admet deux solutions : 1 et c/a. • Si a - b + c = 0, alors l'équation
> T(z) = 0 admet deux solutions : -1 et - c/a. »

> **Point méthode** (p.201, encadré) — « Résolution d'une équation de degré 3 : Pour résoudre dans ℂ l'équation P(z) = 0 où
> P(z) = a₁ z³ + a₂ z² + a₃ z + a₄ (a₁ ≠ 0), connaissant une solution z₀ : • On calcule les trois nombre complexes a, b et c
> tels que : P(z) = (z - z₀) (a z² + b z + c ) • On résout l'équation : a z² + b z + c = 0. Résolution d'une équation
> bicarrée : Pour résoudre dans ℂ l'équation P(z) = 0 où P(z) = a z⁴ + b z² + c (a ≠ 0) : • On pose Z = z² et on détermine Z′
> et Z″ solutions de l'équation a Z² + b Z + c = 0 • On cherche les racines carrées de Z′ et Z″ »

### Apprendre à chercher (p.202)

- **Situation 1** : Z = (z − 1)/(z − i). 1) ensemble E des M(z) tels que Z réel ; 2) ensemble F tels que Z imaginaire pur.
  « Vers une solution » : z ≠ i (M ≠ A(i)). *Première méthode* : Z = ((x − 1) + iy)/(x + i(y − 1)) puis
  Z = (x² − x + y² − y)/(x² + (y − 1)²) + i (x + y − 1)/(x² + (y − 1)²) ; E : Im(Z) = 0, F : Re(Z) = 0 « ... ». *Deuxième
  méthode* : Z̄ = (z̄ − 1)/(z̄ + i) ; Z = Z̄ ⇔ (z − 1)/(z − i) = (z̄ − 1)/(z̄ + i) ⇔ i(z + z̄) + (z − z̄) − 2i = 0 (z ≠ i) ;
  avec z = x + iy, (x, y) ≠ (0, 1), on retrouve E ; même démarche pour F avec Z = −Z̄.
- **Situation 2** : (E) z³ − 2(√3 + i)z² + 4(1 + i√3)z − 8i = 0. 1) solution imaginaire pure ; 2) résoudre. « Vers une
  solution » : z = iy : (2√3y² − 4√3y) + i(−y³ + 2y² + 4y − 8) = 0, système (S), on résout la plus simple et on vérifie ; 2) (z − 2i)(z² + bz + c) ; « On trouve : z₀ = 2 i ; z₁ = √3 + i et z₂ = √3 − i ».

### Avec l'outil informatique (p.203)

- « Produit de deux nombres complexes » : `program produit; … ReP:=a1*a2-b1*b2; ImP:=a1*b2+a2*b1; writeln('le produit de z1
  et z2 est: ',ReP,'+(',ImP,')i'); end.` — Applications : « Calculer z₁z₂ dans chacun des cas suivants » (z₁z₂ imprimé
  décalé sous la ligne [sic]) : a) z₁ = 3 + 4i et z₂ = 1 − i ; b) z₁ = 1 + i et z₂ = 1 + i ; c) z₁ = 2i et z₂ = 3 + i.
- « Racine carrée d'un nombre complexe » : `program racine; … modu:= sqrt(a*a+b*b); ar:=sqrt((a+modu)/2); br:=b/(2*ar);
  writeln('une racine carrée de z est',ar,'+i(',br,')'); end.` — Applications : une racine carrée de a) z₁ = −3 + 4i ;
  b) z = 1 + i ; c) z = 2i. (Le programme divise par ar, nul si z est un réel négatif : non signalé.)

### Exercices et problèmes (p.204–207) — 19 exercices (numéros 1 à 19 ; « 11 » imprimé deux fois, « 12 » absent)

- **Ex. 1 VRAI-FAUX** (p.204) : (z, z′ complexes) 1) |z| = |z′| ⇔ z = z′ ou z = −z′ ; 2) |z′| = |z̄| ⇔ |z| = |z′| ; 3) les
  points d'affixes z et z̄ appartiennent à un même cercle de centre O ; 4) les solutions a et b de z² − 2z + 10 = 0 sont
  conjuguées.
- **Ex. 2 QCM** (une seule réponse) : 1) {M : |z − 2i| = 4} : a) médiatrice de [AB], A(2i), B(4) ; b) cercle de centre A(2i) ;
  c) cercle de rayon 2 ; 2) Im(3 + i(2 + i)) : a) 2 + i ; b) 2i ; c) 2 ; 3) z = (1 − i)² : a) |z| = 1 ; b) réel > 0 ;
  c) imaginaire pur ; 4) solutions de z² − 4z + 13 = 0 : a) 2 − 5i et −2 + 5i ; b) −4 + i et 4 + i ; c) 2 − 3i et 2 + 3i ; 5) racines carrées de 2/i : a) √2/i et −√2/i ; b) 1 − i et −1 + i ; c) √2 i et −√2 i ; 6) z′ = (z + 4i)/(z − 2), z ≠ 2 :
  {M : |z′| = 1} est a) un cercle de rayon 1 ; b) une droite ; c) une droite privée d'un point ; d) un cercle privé d'un
  point.
- **Ex. 3** : z = 4 + 3i, z′ = 5 − 2i : forme algébrique de z + z′ ; z − z′ ; 3z − z′ ; zz′ ; (z + z′)² ; (z − z′)² ;
  z² − (z′)² ; z³ − (z′)³ ; z/z′.
- **Ex. 4** : placer z₁ = 2 + 3i, z₂ = 3 + i, z₃ = −1 + 2i, z₄ = 2 − i, z₅ = 2z₁ − 3z₂, z₆ = z₃(z₄ − z₂).
- **Ex. 5** : conjugués de 2 − √3 ; i√2 + 5i ; i⁴ ; (1 + 5i)/(537i) ; 2i − 7 ; (1 + i)/(1 − i) ; 3/(5 − i) + i/(5 + i).
- **Ex. 6** : z = 3 + 4i, z′ = 1 − i : modules de z, z′, zz′, 1/z, z/z′, z²⁰⁰⁷.
- **Ex. 7** (p.204–205) : A(−1), M(x + iy), Z = iz/(z + 1) : 1) Re(Z), Im(Z) ; 2) a) E : Z réel ; b) F : Z imaginaire pur.
- **Ex. 8** (p.205) : A(1), B(−3i), C(i) ; z′ = (z − 1)/(3 − iz) (z ≠ −3i) : 1) a) z′ = i(z − 1)/(z + 3i) ; b) |z′| = 1 ; 2) z′ réel ; 3) a) |z′ − i|·|z + 3i| = √10 ; b) M sur le cercle de centre B de rayon 1 ⇒ M′ sur un cercle (centre, rayon).
- **Ex. 9** : A(i), z′ = (iz − 2 + 4i)/(z − i) (z ≠ i) : 1) a) x′, y′ en fonction de x, y ; b) z′ réel ; c) z′ imaginaire
  pur ; 2) Z = z − i, Z′ = z′ − i : a) ZZ′ = −3 + 4i, module ; b) M sur (C) de centre A, rayon r ⇒ M′ sur (C′) de centre A
  [« d'écrit » sic] ; c) r pour (C) = (C′).
- **Ex. 10** : racines carrées de 1 + 2i√2 ; 6 − 30i [sic ? voir doutes] ; −45 − 28i ; 5 ; −7i ; 24 + 10i ; −7 ; −5 + 12i.
- **Ex. 11 (1er)** : résoudre 1) (2 + i)z − 3 + 2i = 0 ; 2) (z + 2)/(z − 1) = 3 + i ; 3) z + 3z̄ = 4 + 2i ; 4) z² − 2z̄ + 1 = 0 ; 5) (3 + i)z² + (1 + 4i)z − 4 − 5i = 0 ; 6) (2 + i)z² − (3 + 2i)z + 1 − i/2 = 0 ; 7) z² − (10i − 7)z − (11 + 41i) = 0 ; 8) z² − 4(6 + i)z + (63 + 16i) = 0 ; 9) z³ − 8 = 0 ; 10) z³ + 1 = 0.
- **Ex. 11 (2e, à la place du n° 12)** : P(z) = z³ − 6z² + 12z − 16 : 1) a) P(4) = 0 ; b) P(z) = 0 ; 2) résoudre
  ((z − i)/(z + i))³ − 6((z − i)/(z + i))² + 12((z − i)/(z + i)) − 16 = 0 (poser Z = (z − i)/(z + i)).
- **Ex. 13** (p.206) : 1) a) (2 − 3i)² = −5 − 12i ; b) z² − (4 − i)z + 5 + i = 0 ; 2) (E) z³ − (10 − i)z² + (29 − 5i)z − 30 − 6i = 0 :
  a) = (z − 6)(z² − (4 − i)z + 5 + i) ; b) résoudre ; 3) A(6), B(1 + i), C(3 − 2i) : a) placer ; b) AB, AC, BC ; c) nature
  de ABC ; d) D tel que ACBD soit un carré.
- **Ex. 14** : P(z) = z⁴ − 4z² + 16 : 1) a réel tel que P(z) = (z² + az + 4)(z² − az + 4) ; 2) a) résoudre, z₁ à parties réelle
  et imaginaire positives ; b) solutions z₁, −z₁, z̄₁, −z̄₁ ; 3) a) placer A, B, C, D ; b) sur le cercle de centre O de
  rayon 2.
- **Ex. 15** : 1) résoudre dans IR³ (S) {8x + 2y + t = 0 ; x + y + t = −5 ; −x − y + t = −3} ; 2) f(z) = az³ + bz + c (a, b, c
  réels) : a) a, b, c tels que f(2) = 0, f(1) = −5, f(−1) = −3 ; b) résoudre f(z) = 0.
- **Ex. 16** : 1) (S) {x + y − 2t = −6 ; y + t = −1 ; x + t = 3} ; 2) f(z) = az³ + biz² + (c − 6)z + ic : a) a, b, c tels que
  f(1) = −3 − i et f(i) = 0 ; b) résoudre f(z) = 0 ; 3) A(i), B(1 + i), C(−1 + i) : a) placer ; b) nature de OBC.
- **Ex. 17** (p.206–207) : f(z) = z³ − (16 − i)z² + (89 − 16i)z + 89i : 1) a) racine imaginaire pure z₀ ; b) b, c réels
  [« deux réel » sic] avec f(z) = (z − z₀)(z² + bz + c) ; c) résoudre ; 2) A(−i), B(8 + 5i), C(8 − 5i) : a) nature de ABC ;
  b) ensemble E des M tels que −MA² + MB² − MC² = 20.
- **Ex. 18** (p.207) : **I-** f(z) = z³ + az² + bz + c (a, b, c réels) : 1) a) f(2) = 0 et f(1 − i) = 0 ⇒ (S) {4a + 2b + c + 8 = 0 ;
  b + c − 2 = 0 ; 2a + b + 2 = 0} ; b) résoudre (S) dans IR³ ; 2) f(z) = z³ − 4z² + 6z − 4 : a) = (z − 2)(z² − 2z + 2) ;
  b) résoudre. **II-** A(2), B(1 − i) : 1) OAB rectangle en B ; 2) C symétrique de B par rapport à l'axe des abscisses :
  OABC carré. « (Bac Tunisien) »
- **Ex. 19** : 1) (S) {x + y + z = −1 ; x − y + z = −5 ; 4x + 2y + z = 4} ; 2) f(z) = z³ + az² + bz + c : a) f(1) = 0,
  f(−1) = −6, f(2) = 12 ; b) f(z) = (z − 1)(z² + 2z + 4) ; 3) résoudre ; 4) A(1), B(−1 + i√3), C(−1 − i√3) : a) placer ;
  b) D tel que ABCD soit un parallélogramme. « (Bac Tunisien) »

### Maths et culture (p.208)

dal Ferro (début du XVIᵉ s.) : formule pour x³ + px = q : x = ∛((q − √(q² + 4p³/27))/2) + ∛((q + √(q² + 4p³/27))/2) ;
Bombelli applique à x³ − 15x = 4 : x = ∛(2 − 11√−1) + ∛(2 + 11√−1) ; (2 + √−1)³ = 2 + 11√−1, (2 − √−1)³ = 2 − 11√−1, d'où
x = 2 + √−1 + 2 − √−1 = 4. « C'est ainsi qu'est née la théorie des nombres complexes. » « • Les solutions de l'équation
z² = -1 sont i et -i d'où √−1 = i . • On a : 1 = √((-1)(-1)) = √-1 √-1 = i . i = i² = -1 c'est absurde. •Pour cette raison le
symbole √−1 que nous avons utilisé en toute impunité est absolument interdit à partir de maintenant. • Dans la réalité, il
a fallu 150 ans pour l'abandonner et utiliser la notation i proposée par Euler. »

### Écart avec la référence (math-bac-sciences-exp/11 « Nombres complexes » + /12 « Équations à coefficients complexes », manuel 222434 ; voisins : math-bac-techniques/10 + 11)

Correspondance **confirmée, mais très partielle** : seules les sections « forme algébrique / conjugué », « affixe,
colinéarité, orthogonalité », « module, distances, lieux » de sciences-exp/11 et « racines carrées », « second degré »,
« somme et produit », « degré 3 », « changer d'inconnue » (bicarrée) de sciences-exp/12 sont couvertes.

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer)** :
- tout ce qui touche à l'**argument** : argument, **forme trigonométrique**, arg(zz′), arg(zⁿ), **formule de Moivre**,
  **notation e^(iθ) / forme exponentielle**, **formules d'Euler**, **linéarisation**, expression de cos nx / sin nx,
  factorisation par l'angle moitié ;
- **racines n-ièmes** de l'unité et d'un complexe (polygones réguliers) — seul **j** apparaît (Appl. V.2.3, racines de
  z³ − 1, sans j² = j̄ ni propriétés) ; équations paramétrées par θ ;
- racines carrées par la **méthode exponentielle** ; résolution du système {somme ; produit} ;
- lieux « cercle de diamètre [AB] » via arguments ; colinéarité/orthogonalité par le **quotient** z_w⃗/z_w₁⃗ (ici par
  le **produit z̄z′**).

**Ce que ce manuel a en plus (ou autrement)** :
- ℂ introduit **axiomatiquement** (« Théorème et définition », existence admise) après la résolution de x² + 1 = 0 ;
- colinéarité/orthogonalité par **z̄z′ = u⃗.v⃗ + i det(u⃗, v⃗)** (produit scalaire + déterminant) ;
- critère **z = z′ ⇔ {a = a′, |z| = |z′|, bb′ > 0}** pour extraire une racine carrée ; « Cas particulier » coefficients réels
  (Δ < 0 → i√−Δ) ; racines évidentes 1 et c/a, −1 et −c/a ;
- encadré « **Point méthode** » degré 3 et bicarrée ;
- **systèmes 3 × 3 dans IR³** pour identifier les coefficients (Ex. 15, 16, 18, 19) — lien avec le ch. 11 « Systèmes »
  du même manuel ;
- **programmes Turbo Pascal** (produit, racine carrée) ; lecture historique dal Ferro/Bombelli/√−1 interdit ;
- notations : Aff(M), Aff(u⃗), z_M, z_u⃗, M(z), « plan complexe », « axe réel / axe imaginaire », repère (O, e⃗₁, e⃗₂).

### Bornes de scope (chapitre 10, section Sciences de l'informatique)

- ✅ INCLUS : ℂ, i² = −1, forme algébrique unique, Re/Im, réel, imaginaire pur, égalité ; opérations, inverse et quotient
  (par le conjugué du dénominateur) ; puissances de i ; affixe d'un point, d'un vecteur, Aff(AB⃗) = z_B − z_A, milieu,
  linéarité ; axes réel et imaginaire, symétries (−z, z̄, −z̄) ; conjugué et propriétés (somme, produit, puissance,
  inverse, quotient, z + z̄, z − z̄, caractérisations réel / imaginaire pur) ; colinéarité / orthogonalité par z̄z′ ;
  module (√(zz̄), OM, AB = |z_B − z_A|, inégalité triangulaire, |zz′|, |kz|, |zⁿ|, |1/z|, |z′/z|) ; ensembles de points
  (cercle |z − a| = r, médiatrice |z − a| = |z − b|, Z réel / imaginaire pur, |z′| = 1 pour une homographie) ; nature de
  triangles et quadrilatères (rectangle, isocèle, équilatéral, carré, parallélogramme) ; racines carrées (algébrique :
  x² − y², 2xy, module) ; second degré à coefficients complexes (Δ, δ), cas réel ; somme et produit des racines,
  factorisation ; degré 3 avec racine connue / imaginaire pure / identification ; bicarrées ; changement d'inconnue
  Z = (z − i)/(z + i) ; j (racines de z³ − 1) ; systèmes 3 × 3 pour identifier des coefficients ; programmes Pascal.
- ⛔ EXCLU (absent de ces pages) : argument, forme trigonométrique, forme exponentielle e^(iθ), Moivre, Euler,
  linéarisation ; racines n-ièmes (sauf racines cubiques de 1 et z³ = ±8, ±1 par factorisation) ; transformations du
  plan (rotations, similitudes) par les complexes ; théorème fondamental de l'algèbre ; formules de Cardan (lecture
  seulement).

### Lecture

- **Pages lues en L1** : p.189 à 208 (20 pages).
- **Pages lues sur l'image (110 dpi)** : p.189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205,
  206, 207, 208 = **20/20 (100 %)** ; zooms 250 dpi : p.194 (figure Appl. II.1 : A(2 + i), B(−1 + 2i), C(−i)), p.204
  (VRAI-FAUX 1–2).
- **Écarts texte/image** : L1 perd systématiquement ℂ (« dans : »), les barres de conjugaison, les flèches de vecteurs,
  les modules |…| et les racines (√3, √2, √5) ; p.192–193 vecteurs et Aff(…) illisibles ; p.195 propriétés du conjugué
  réduites à « z = z » ; p.197 propriétés du module sans barres ; p.199–200 δ lu « / », Δ lu « », formules du discriminant
  écrasées ; p.204–207 colonnes entrelacées (Ex. 1/2/3…, 8/9/10/11, 13/14/15/16, 17/18/19) ; p.207 L1 « zB = 1+ i 3 » au
  lieu de −1 + i√3 (Ex. 19) ; p.206 L1 « 18 x + 2y + t », « 2- x » (numéros parasites) pour 8x + 2y + t, −x − y + t ;
  p.208 formules de dal Ferro/Bombelli illisibles en L1.
- **Coquilles [sic]** : « Tout élément z de [ℂ absent] » (p.191) ; « maniére » ; Act. IV.1 5) « Comparer AB et
  |z_N − z_M| » (pour MN) ; « Vésrifier » (p.201) ; « P(z) = z³ 1 » sans le signe − (Appl. V.2.3, p.201) ; « d'écrit » (Ex. 9) ; « deux réel » (Ex. 17) ; « des chacun » (Ex. 10) ;
  numéro **11 doublé** et **12 absent** (p.205) ; bandeau « Cours » sur la page d'exercices p.206 ; « z₁z₂ » décalé (p.203) ;
  « ci-desous » (p.208).
- **Doutes [?]** : (1) Ex. 10 « 6 − 30i » : |6 − 30i|² = 936 non carré parfait (racines non « jolies ») — lu tel quel ;
  (2) Ex. 2 QCM 6 : |z′| = 1 ⇔ |z + 4i| = |z − 2| : médiatrice des points d'affixes −4i et 2, qui ne contient pas le point
  exclu (2) ; la bonne réponse est donc b) « une droite » (aucun corrigé dans le manuel ; noté pour la génération) ;
  (3) l'encadré « Théorème » p.199 (z = z′ ⇔ a = a′, |z| = |z′|, bb′ > 0) est énoncé tel quel pour des complexes non
  réels ; il sert à résoudre z² = d en comparant Re, module et signe de Im ; (4) la figure p.193 place « axe réel » et
  « axe imaginaire » à des endroits trompeurs (étiquettes près de l'origine).

## 2.11 Chapitre 11 — Systèmes d'équations linéaires (manuel 222472, p.209–234)

**Page de garde (p.209)** — « Chapitre 11 », titre « SYSTÈMES D'ÉQUATIONS LINÉAIRES ». Plan imprimé :
« I . Matrices et opérations sur les matrices · II . Déterminant d'une matrice carrée d'ordre 2 ou 3 ·
III . Inverse d'une matrice carrée d'ordre 2 ou 3 · IV . Applications ». Portrait et légende : « Arthur
Cayley (1821 - 1895) mathématicien anglais, connu, surtout, pour avoir été l'inventeur de la théorie des
matrices ». Pas de citation liminaire.

**Plan du chapitre** : **Cours** (bandeau « Cours ») — **I. Matrices et opérations sur les matrices**
(p.210–214 : « Activités de découverte » Act. 1–5 ; « A retenir » p.212–214 ; « Applications » 1–5 p.214) ·
**II. Déterminant d'une matrice carrée d'ordre 2 ou 3** (p.215–218 : Act. 1–3 ; « A retenir » p.216–217 ;
« Applications » 1–4 p.217–218) · **III. Inverse d'une matrice carrée d'ordre 2 ou 3** (p.218–220 :
Act. 1–3 + texte de cours mineur/cofacteur/comatrice avec « Exemple » p.219 ; « A retenir » p.220 ;
« Applications » 1–5 p.220) · **IV. Applications** (p.221–226 : « Activités préliminaires » —
« 1. Résolution de systèmes linéaires » Act. 1–2 p.221 ; « Activités de découverte » Act. 1–2 p.221–223 ;
« A retenir » p.223 ; « Applications » 1–4 p.224 ; « 2. système de Cramer » [sic « systèmede »] activité
non numérotée p.224–225 ; « A retenir » p.226 ; « Applications » 1–3 p.226). Puis **Apprendre à chercher**
(p.227 : Situations 1–3), **Avec l'outil informatique** (p.228 : Excel), **Exercices et problèmes**
(p.229–233 : blocs numérotés 1 à 26, sans « 24 », « 25 » imprimé deux fois, + 1 bloc non numéroté),
**Maths et culture** (p.234 : « Les carrés magiques »). Pas de rubrique QCM/Vrai-Faux séparée : le QCM
(Ex. 1) et le Vrai-Faux (Ex. 2) ouvrent les exercices. Pas d'« exercices résolus » ni de « Tout ce qu'on
doit savoir ». Les en-têtes de p.227 et p.228 portent « Chapitre 12 : Systèmes d'équations linéaires »
[sic].

### Cours — Activités (une ligne chacune)

**I. Matrices et opérations sur les matrices — Activités de découverte**

- **Act. 1** (p.210) : tableau des quantités (en litres) de carburants vendues sur une semaine (lignes sans
  plomb / super / gazole ; colonnes lundi … dimanche : sans plomb 2000, 1500, 1000, 1800, 1500, 2500, 2400 ;
  super 1800, 1500, 1100, 1500, 1400, 1500, 2100 ; gazole 3000, 2500, 3200, 2700, 3500, 3300, 3500). 1) représenter les ventes de chaque jour par une colonne de 3 nombres ; 2) représenter les quantités de
     gazole de la semaine ; 3) traduire les quantités de la semaine par un tableau. ➢ « Le tableau obtenu est
     une matrice de dimension 3 x 7. » Suit la définition (voir encadrés).
- **Act. 2** (p.210) : entreprise de matériel audiovisuel, quatre magasins A, B, C, D ; stocks S = (2 3 1 4 ;
  1 2 1 3 ; 3 4 2 1) en téléviseurs (t), magnétoscopes (m), chaînes hi-fi (c) ; réapprovisionnement
  R = (3 1 5 1 ; 2 2 3 1 ; 1 1 4 5). Matrice M du nouvel état des stocks ? « La matrice M est la somme de S
  et R. » ➢ somme de deux matrices de même dimension n x p.
- **Act. 3** (p.210–211) : M = (1000 1500 800 ; 200 100 250 ; 130 110 130) (lignes t, e, p ; colonnes A, B, C)
  donne travail, énergie, matière première pour une unité de chaque produit semi-fini [sic « semis-finis »] ;
  N = (4 3 ; 10 5 ; 8 3) (lignes A, B, C ; colonnes X, Y). Quantités de travail, énergie, matière première
  pour une unité de X ? de Y ? ➢ produit d'un vecteur-ligne par un vecteur-colonne ; produit A x B ; exemple
  (2 3 ; 4 5)(−1 7 0 ; 1 −2 6) = (2×(−1)+3×1 … ) = (1 8 18 ; 1 18 30).
- **Act. 4** (p.211) : 1) calculer (1 2 3 ; 4 5 6) + (a b c ; d e f) ; 2) A, B de dimension 3 x 3 : vérifier
  A + B = B + A ; 3) A = (6 −4 ; −1 2 ; 3 −5) : calculer A + A, A + A + A ; ➢ produit par un réel k ; 4) A, B, C de dimension 3 x 3 : a) (A + B) + C = A + (B + C) = A + B + C ; b) k(A + B) = kA + kB.
- **Act. 5** (p.212) : 1) calculer (1 1 ; 1 1)(2 2 ; 3 3) puis (1 1 ; 1 1)(1 1 ; 4 4), que remarquer ? 2) (0 5 ; 1 2)(2 1 ; 1 0) puis (2 1 ; 1 0)(0 5 ; 1 2), que remarquer ? 3) (3 0)(2 ; 1) puis (2 ; 1)(3 0) ; 4) (4 −11 ; −2 8)(0,8 1,1 ; 0,2 0,4).

**II. Déterminant d'une matrice carrée d'ordre 2 ou 3 — Activités de découverte**

- **Act. 1** (p.215) : A = (a b ; c d), a, b, c, d réels non tous nuls ; chercher A′ = (x y ; z t) telle que
  (a b ; c d)(x y ; z t) = (1 0 ; 0 1). 1) le problème revient aux systèmes {ax + bz = 1 ; cx + dz = 0} et
  {ay + bt = 0 ; cy + dt = 1} ; 2) condition d'unique solution ; 3) vérifier x = d/(ad − bc) ;
  y = −b/(ad − bc) ; z = −c/(ad − bc) ; t = a/(ad − bc). ➢ « Le réel ad - bc est appelé **déterminant** de
  la matrice A, on le note : dét (A) = |a b ; c d|, et A' ainsi définie est la matrice inverse de A, notée
  A⁻¹. »
- **Act. 2** (p.215) : pour tout réel a, (S) {ax + y + z = 3 ; ax + a2 + az = -1 [sic : « a2 » pour a²y] ;
  x + y + az = 7}. 1) résoudre pour a = 0, a = 1, a = 2 ; 2) écrire (S) sous la forme A X = B ; 3) « Calculer que Δ défini par » [sic] a|a² a ; 1 a| − a|1 1 ; 1 a| + |1 1 ; a² a| ; 4) vérifier
  Δ = a(a + 2)(a − 1)² et conclure sur le lien entre les a tels que Δ = 0 et les ensembles de solutions.
  ➢ Δ déterminant du système ; pour M = (a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃),
  Δ = a₁|b₂ c₂ ; b₃ c₃| − a₂|b₁ c₁ ; b₃ c₃| + a₃|b₁ c₁ ; b₂ c₂|.
- **Act. 3** (p.216) : M = (a b c ; d e f ; g h i). 1) vérifier dét(M) = a|e f ; h i| − b|d f ; g i| +
  c|d e ; g h| ; ➢ développement suivant la 1ʳᵉ ligne, ou toute ligne/colonne avec le facteur (−1)^(i+j) ; 2) a) vérifier |7 5 1 ; 0 2 1 ; 7 −3 0| = 7|1 5 1 ; 0 2 1 ; 1 −3 0| ; b) montrer r|a b ; c d| =
  |ra rb ; c d| = |a rb ; c rd| ; c) en déduire : deux lignes ou colonnes proportionnelles ⇒ déterminant
  nul ; 3) A = (−3 5 6 ; −1 2 2 ; 1 −1 −1), B = (−3 5 1 ; −1 2 0 ; 1 −1 0) : a) transformation élémentaire
  de A à B ? b) vérifier dét(A) = dét(B). ➢ « La valeur d'un déterminant ne change pas si on ajoute à une
  ligne une combinaison linéaire des autres lignes ou à une colonne une combinaison linéaire des autres
  colonnes. »

**III. Inverse d'une matrice carrée d'ordre 2 ou 3 — Activités de découverte**

- **Act. 1** (p.218) : reprise quasi littérale de II Act. 1 (seules différences : « admettent une unique solution » au lieu de « admettent - ils une unique solution », et « la solution est : x = … ») (A = (a b ; c d), A′ telle que AA′ = I₂, deux
  systèmes, solution x = d/(ad − bc) …). ➢ « La A' ainsi définie est la matrice **inverse** de A, notée
  A⁻¹. »
- **Act. 2** (p.218) : A = (1 2 3 ; 4 5 6 ; 7 8 9). 1) écrire la matrice B obtenue en échangeant lignes et
  colonnes de même indice ; ➢ B **transposée** de A, notée Aᵗ ; 2) vérifier det(A) = det(Aᵗ).
- **Act. 3** (p.218–219) : A = (1 2 −1 ; 3 4 2 ; 1 0 5) et A′ = (−10 5 −4 ; 13/2 −3 5/2 ; 2 −1 1). a) dét(A)
  et dét(A′) ; b) A x A′ puis A′ x A, conclure. ➢ A′ inverse de A, A **inversible**. Puis (numérotée
  « 2) » [sic, après a) b)]) : a) B = (1 1 0 ; −1 0 0 ; 2 0 −1), calculer dét(B) ; b) vérifier B³ + I₃ = θ
  (B³ = B × B × B) ; en déduire que B est inversible et B⁻¹. ➢ inversibilité ⇔ déterminant non nul ;
  mineur, cofacteur, comatrice, A⁻¹ = (1/det(A))(ComA)ᵗ (voir encadrés). **Exemple** (p.219) :
  A = (−3 5 6 ; −1 2 2 ; 1 −1 −1), vérifier dét(A) = −1 ; matrice des cofacteurs écrite en déterminants
  2×2 signés, ComA = (0 1 −1 ; −1 −3 2 ; −2 0 −1) ; transposée (0 −1 −2 ; 1 −3 0 ; −1 2 −1) ;
  A⁻¹ = (0 1 2 ; −1 3 0 ; 1 −2 1).

**IV. Applications — 1. Résolution de systèmes linéaires**

- **Act. préliminaire 1** (p.221) : vérifier que (S) {x − 3y + 2z = 1 ; 2x − y + 3z = 9 ; 3x − 2y + 4z = 11} et
  (S′) {x − 3y + 2z = 1 ; 5y − z = 7 ; z = 3} sont équivalents.
- **Act. préliminaire 2** (p.221) : {2x₁ + x₂ − x₃ = 1 (L₁) ; x₁ − x₂ + x₃ = 2 (L₂) ; 4x₁ + 3x₂ + x₃ = 1 (L₃)}. 1) matrice du système et déterminant ; 2) matrice complète puis L₂ ← L₂ − ½L₁ et L₃ ← L₃ − 2L₁ ; 3) supprimer x₂ dans la 3ᵉ ligne et résoudre. « La méthode utilisée précédemment pour résoudre le système
     est appelée méthode du **pivot de Gauss** ».
- **Act. de découverte 1** (p.221–222) : A = (1 0 −1 ; 2 1 3 ; 0 −1 1). 1) déterminant, A inversible ; 2) (X, Y, Z) donné, chercher (x, y, z) avec {x − z = X ; 2x + y + 3z = Y ; −y + z = Z} ; a) forme
  A(x ; y ; z) = (X ; Y ; Z) (➢ « forme matricielle ») ; b) matrice augmentée (A | X Y Z) et, par le pivot de
  Gauss, vérifier les calculs successifs (… (0 1 5 | −2X + Y), (0 0 6 | −2X + Y + Z), (0 0 1 | −⅓X + ⅙Y + ⅙Z),
  jusqu'à I₃ | (⅔X + ⅙Y + ⅙Z ; −⅓X + ⅙Y − ⅚Z ; −⅓X + ⅙Y + ⅙Z)) ; c) vérifier A⁻¹ = (2/3 1/6 1/6 ;
  −1/3 1/6 −5/6 ; −1/3 1/6 1/6). ➢ si M inversible, une suite d'opérations élémentaires sur les lignes fait
  passer de M à I₃.
- **Act. de découverte 2** (p.222–223) : opération élémentaire de lignes = multiplication à gauche par I₃
  transformée ; recherche de l'inverse de (1 2 −1 ; 3 4 2 ; 1 0 5) en deux colonnes (matrice | I₃) :
  L₂ ← L₂ − 3L₁, L₃ ← L₃ − L₁ → (1 2 −1 ; 0 −2 5 ; 0 −2 6) | (1 0 0 ; −3 1 0 ; −1 0 1) ; L₁ ← L₁ + L₂ →
  (1 0 4 ; 0 −2 5 ; 0 −2 6) | (−2 1 0 ; −3 1 0 ; −1 0 1). 1) compléter le procédé en appliquant les transformations indiquées (p.223, trois étapes à cases « .. ») :
  L₃ ← L₃ − L₂ : matrice de gauche donnée (1 0 4 ; 0 −2 5 ; 0 0 1), celle de droite à compléter ;
  L₁ ← L₁ − 4L₃, L₂ ← L₂ − 5L₃ : matrice de gauche à compléter, celle de droite donnée (−10 5 −4 ; −13 6 −5 ;
  2 −1 1) ; L₂ ← L₂/(−2) : matrice de gauche donnée I₃, celle de droite à compléter ; 2) en déduire l'inverse ; 3) résoudre (1 2 −1 ; 3 4 2 ; 1 0 5)(x ; y ; z) = (2 ; 1 ; −4) : a) vérifier
  (−10 5 −4 ; 13/2 −3 5/2 ; 2 −1 1)(1 2 −1 ; 3 4 2 ; 1 0 5)(x ; y ; z) = (1 ; 0 ; −1) ; b) solution
  (x ; y ; z) = (1 ; 0 ; −1).

**IV. Applications — 2. Système de Cramer**

- **Activité (non numérotée)** (p.224–225) : (S) {x − 3y + 2z = 1 ; 2x − y + 3z = 9 ; 3x − 2y + 4z = 1}
  [3ᵉ second membre 1 ici, 11 en p.221]. 1) matrice M et dét(M), en déduire l'unique solution ; ➢ « On
  appelle **système de cramer** tout système carré dont la matrice est inversible. » 2) écrire
  (1 −3 2 ; 2 −1 3 ; 3 −2 4)(x ; y ; z) = (1 ; 9 ; 1) ; 3) « En revenant au paragraphe III. 1. » vérifier
  x, y, z comme quotients de déterminants (colonne remplacée par (1 ; 9 ; 1), imprimée en rouge). ➢ cas
  général a₁x₁ + b₁x₂ + c₁x₃ = k₁ … ; écriture A × X = K, Aᵢ = A dont la iᵉ colonne est remplacée par K ;
  x₁ = det(A₁)/det(A), x₂ = det(A₂)/det(A), x₃ = det(A₃)/det(A) (déterminants développés). Encart :
  « Gabriel Cramer (1704-1752) Mathématicien suisse ; nous lui sommes redevables de la résolution complète
  des systèmes carrés par les déterminants ». Dernière ligne : « ➢ Remarquer qu'il s'agit de la même
  méthode, déjà vue, pour les systèmes carrés d'ordre 2 : » — phrase sans suite (rien n'est imprimé après).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Texte de cours après Act. 1** (p.210) — « Une matrice A de dimension n x p est un tableau rectangulaire
> dont les éléments sont rangés en n **lignes** et p **colonnes** et on écrit : A=( aᵢⱼ ) 1 ≤ i ≤ n ;
> 1 ≤ j ≤ p. Les réels aᵢⱼ sont **les coefficients** de A. aᵢⱼ est le **coefficient** d'indice (i , j).
> Une matrice comportant une ligne et p colonnes s'appelle un vecteur-ligne de dimension p. Une matrice
> comportant une colonne et n lignes s'appelle un vecteur-colonne de dimension n. »

> **Texte de cours** (p.210) — « ➢ De façon générale la somme de deux matrices de même dimension n x p
> s'effectue en additionnant les coefficients de même indice et la matrice obtenue est aussi de dimension
> n x p. »

> **Texte de cours** (p.211) — « ➢ La quantité de travail est le produit d'un vecteur ligne par un vecteur
> -colonne. Plus généralement le produit de (a₁, a₂,..., aₙ) par (b₁ ; b₂ ; . ; bₙ) est le réel
> a₁b₁ + a₂b₂ + ..+ aₙbₙ. ➢ On appelle produit d'une matrice A de dimension n x p par une matrice B de
> dimension p x q la matrice notée A x B de dimension n x q obtenue de la façon suivante : le cœfficient de
> la ligne l et de la colonne c de A x B est le produit du vecteur-ligne l de A par le vecteur-colonne c de
> B. »

> **Texte de cours** (p.211) — « ➢ Plus généralement le produit d'une matrice M de dimension n x p par un
> réel k est la matrice de dimension n x p, notée k A, obtenue en multipliant par k chaque coefficient de
> A. » (M puis A dans la même phrase [sic].)

> **A retenir — Définitions** (p.212) — « n et p désignent des entiers naturels non nuls, **une matrice** de
> dimension n x p est un tableau de nombres réels à n lignes et p colonnes. **Notation :** Toute matrice M
> est notée ( aᵢⱼ ) et représentée comme ci-dessous. aᵢⱼ désigne le cœfficient de la i ᵉᵐᵉ ligne et de
> j ᵉᵐᵉ colonne, avec 1 ≤ i ≤ n et 1 ≤ j ≤ p » (schéma M = (a₁₁ … a₁ⱼ … a₁ₚ ; … ; aᵢ₁ … aᵢⱼ … aᵢₚ ; … ;
> aₙ₁ … aₙⱼ aₙₚ), flèches « Colonnes 1 j p » et « Lignes 1 . i . n »). « Une matrice comportant une ligne
> et p colonnes s'appelle **un vecteur-ligne** de dimension p. Une matrice comportant une colonne et n
> lignes s'appelle **un vecteur-colonne** de dimension n Lorsque n = m, on dit que la matrice est
> **carrée** d'ordre n. » [sic : « n = m » pour n = p]. Encart : « Carl Friedrich Gauss (1777-1855) a
> introduit la notation matricielle. »

> **A retenir (suite)** (p.213) — « Une matrice carrée dont tous les cœfficients sont nuls sauf les aᵢⱼ
> formant la diagonale s'appelle **matrice diagonale**. Une matrice diagonale dont tous les coefficients
> de la diagonale sont égaux à 1 est appelée **matrice unité**, notée Iₙ. Une matrice dont tous les
> cœfficients sont nuls est appelée **matrice nulle**, notée θ. Deux matrices A = ( aᵢⱼ) et B = ( bᵢⱼ)
> sont égales si et seulement si, elles sont de même dimension et si aᵢⱼ = bᵢⱼ pour tout i et j. »

> **Opérations sur les matrices — Définitions** (p.213) — « A et B sont deux matrices qui ont n lignes et
> p colonnes. • La somme de A et B est la matrice n x p , notée A+B , obtenue en additionnant deux à deux
> les termes qui ont la même position (ou ayant le même indce) [sic] • Le produit de la matrice A par un
> réel k est la matrice n x p , notée k A, obtenue en multipliant par k chaque coefficient de A. »

> **Propriétés** (p.213) — « Soient A, B et C trois matrices de dimensions n x p et k un réel alors : 1) A + B = B + A 2) ( A + B) + C = A + ( B + C) 3) k (A + B) = kA + kB »

> **Définition** (p.213) — « Soit A = (aᵢⱼ) une matrice à n lignes et p colonnes et B = (bⱼₖ) une matrice
> à p lignes et q colonnes. Le produit de la matrice A par la matrice B est la matrice, notée
> A × B = (cᵢₖ) à n lignes et q colonnes, définies par : cᵢₖ = aᵢ₁b₁ₖ + aᵢ₂b₂ₖ + ... + aᵢₚbₚₖ »

> **Remarques** (p.213–214) — « • La multiplication de deux matrices n'est possible que si le nombre de
> colonnes de la première est égal au nombre de lignes de la deuxiéme. • La disposition ci-dessous est très
> pratique : elle permet de calculer facilement le « produit d'une ligne de A par une colonne de B » »
> (schéma en croix : B = (0 1 ; −1 2 ; 4 −2) en haut, A = (2 1 5 ; 3 4 1) à gauche,
> (2×0 + 1×(−1) + 5×4 … ) = (19 −6 ; 0 9) = A × B). (p.214) « Le produit d'une matrice 2 x 3 par une
> matrice 3 x 2 est une matrice 2 x 2. »

> **Propriétés** (p.214) — « Soient A, B et C trois matrices, alors on a : • A x (B x C ) = (A x B ) x C
> • A x ( B + C ) = A x B + A x C »

> **A retenir — Déterminant d'une matrice carrée d'ordre 2 — Définition** (p.216) — « Soit M = (a b ; c d).
> Le déterminant de M est le réel, noté dét (M), définit par : dét (M) = |a b ; c d| = ad − bc »

> **Déterminant d'une matrice carrée d'ordre 3 — Définition** (p.216–217) — « Le déterminant d'une matrice
> carrée M d'ordre 3 est le réel défini par : dét (M) = |a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃| =
> a₁(b₂c₃ − b₃c₂) − a₂(b₁c₃ − b₃c₁) + a₃(b₁c₂ − b₂c₁) = a₁|b₂ c₂ ; b₃ c₃| − a₂|b₁ c₁ ; b₃ c₃| +
> a₃|b₁ c₁ ; b₂ c₂| = (−1)¹⁺¹a₁det(A₁₁) + (−1)²⁺¹a₂det(A₂₁) + (−1)³⁺¹a₃det(A₃₁) où Aᵢⱼ obtenue en
> supprimant la iᵉ ligne et la jᵉ colonne de A. »

> **Remarque** (p.217) — « On peut développer le déterminant suivant une autre ligne ou une autre colonne. »

> **Propriétés** (p.217) — « • La valeur d'un déterminant change de signe si on permute deux lignes ou deux
> colonnes entre elles. • Un déterminant qui posséde deux lignes ou deux colonnes identiques est nul.
> • Dans un déterminant, on peut mettre en évidence un facteur commun à tous les éléments d'une ligne ou
> d'une colonne. • La valeur d'un déterminant ne change pas si on lui applique la transformation
> élémentaire L₁ ← L₁ + a₂L₂ + a₃L₃. »

> **Texte de cours III** (p.219) — « ➢ Plus généralement, on montre qu'une matrice carrée M d'ordre 3, est
> inversible si et seulement si, son déterminant est non nul et dans ce cas il existe une matrice carrée
> d'ordre 3, notée M⁻¹, telle que M × M⁻¹ = M⁻¹ × M = I₃ ➢ Pour calculer l'inverse d'une matrice carrée
> A = (aᵢⱼ), 1 ≤ i, j ≤ 3, d'ordre 3, dont le déterminant est non nul, on considère la matrice (Aᵢⱼ) où
> chaque coefficient est otenu [sic] en supprimant la iᵉ ligne et la jᵉ colonne de A. On appelle **mineur**
> de aᵢⱼ dans A le déterminant de la matrice (Aᵢⱼ). Le réel αᵢⱼ = (−1)ⁱ⁺ʲ det(Aᵢⱼ) est appelé
> **cofacteur** du coefficient aᵢⱼ. On appelle aussi comatrice de A et on note Com A la matrice carrée
> d'ordre 3 de terme général (αᵢⱼ), 1 ≤ i, j ≤ 3. La matrice inverse de A est alors donnée par :
> A⁻¹ = (1/det(A)) (ComA)ᵗ »

> **A retenir — Inverse d'une matrice carrée d'ordre 2 — Définition** (p.220) — « Soit M = (aᵢⱼ) une
> matrice carrée d'ordre 2 ou 3. l'inverse de M, si elle existe, est la matrice, notée M⁻¹ telle que
> M × M⁻¹ = M⁻¹ × M = Iₙ où Iₙ est la matrice unité(n = 2 ou 3) » (titre « d'ordre 2 » alors que la
> définition vise l'ordre 2 ou 3 [sic]).

> **Remarques** (p.220) — « 1) Une matrice n'admet pas forcément d'inverse, dans ce cas on dit qu'elle n'est
> pas inversible. 2) Si une matrice est inversible, alors l'inverse est unique. »

> **Théorème** (p.220) — « Une matrice carrée M d'ordre 2 est inversible si et seulement si, dét (M) ≠ 0,
> dans ce cas si M = (a b ; c d) alors M⁻¹ = (1/(ad − bc)) (d −b ; −c a) »

> **Théorème** (p.220) — « Une matrice carrée M d'ordre 3 est inversible si et seulement si, dét (M) ≠ 0 »

> **Texte de cours IV** (p.221–222) — « La méthode utilisée précédemment pour résoudre le système est
> appelée méthode du **pivot de Gauss** » ; « ➢ On dit qu'on a exprimé le système d'équations sous forme
> matricielle. » ; « ➢ De façon générale, si une matrice M est inversible, il est possible, par une suite
> d'opérations élémentaires sur les lignes, de passer de M à I₃. » ; (p.222) « On peut constater, à partir
> de l'activité précédente, qu'appliquer une transformation élémentaire de lignes à une matrice M revient à
> multiplier à gauche cette matrice par la matrice identité I₃ dans laquelle on a effectué la même
> transformation. »

> **A retenir — Théorème** (p.223) — « Soit une matrice carrée A d'ordre 2 ou 3 telle que dét(A) ≠ 0. Un
> système, qui s'écrit matriciellement A × X = B , a une solution et une seule, définie par X = A⁻¹ × B ,
> où A⁻¹ est l'inverse de A. »

> **Remarque** (p.223) — « Lorsqu'un système A × X = B n'a pas de solution ou une infinité de solutions, la
> matrice A n'admet pas de matrice inverse. »

> **Texte de cours Cramer** (p.225) — « C'est important d'exprimer ce système d'équations sous forme
> matricielle, puisque les calculatrices qui résolvent ce genre de problème demandent souvent qu'on leur
> donne les coefficients sous forme matricielle. On va donner une méthode de résolution qui fait appel à
> cette notation : c'est la méthode de Cramer. Nous supposons que (S) est de Cramer, il s'écrit :
> A × X = K où A = (a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃), X = (x₁ ; x₂ ; x₃) la matrice des inconnues et
> K = (k₁ ; k₂ ; k₃) la matrice des constantes. Nous noterons Aᵢ (i =1, 2, 3) la matrice A des coefficients
> dans laquelle on a remplacé la iᵉ colonne par la matrice des constantes. La solution du système, par la
> méthode de Cramer, est donnée par : x₁ = det(A₁)/det(A) = |k₁ b₁ c₁ ; k₂ b₂ c₂ ; k₃ b₃ c₃| /
> |a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃| , x₂ = det(A₂)/det(A) = |a₁ k₁ c₁ ; a₂ k₂ c₂ ; a₃ k₃ c₃| / … et
> x₃ = det(A₃)/det(A) = |a₁ b₁ k₁ ; a₂ b₂ k₂ ; a₃ b₃ k₃| / … »

> **A retenir — Définition** (p.226) — « On appelle **système de Cramer** tout système linéaire de n
> équations à n inconnues ( n = 2 ou 3) : M x X = K tel que dét (M) ≠ 0. »

> **Théorème** (p.226) — « Tout système de Cramer d'ordre 3 a une unique solution (x₁, x₂, x₃) donnée par
> xᵢ = det(Mᵢ)/det(M) où Mᵢ est la matrice obtenue en remplaçant la iᵉᵐᵉ colonne de la matrice M par celle
> des constantes. »

### Applications (fin de chaque partie du cours) — 21

- **I. Appl. 1** (p.214) : A matrice 3 x 3 avec a₂₁ = 4, a₃₂ = 5, a₂₃ = 1, a₁₃ = −5, a₁₂ = 7, a₃₁ = 3 ;
  recopier et compléter A = (6 . . ; . 1 . ; . . 0).
- **I. Appl. 2** (p.214) : produits a. (2 0 ; 0 2)(2 ; 3) ; b. (2 −3 ; 0 −5)(−3 ; 3) ; c. (5 10 ; 2 4)(1 0 ;
  3 1) ; d. (2 4 −2 ; 0 1 1 ; 3 1 −1)(4 ; 8 ; 4) ; e. (2 4 3 ; 0 1 1 ; 2 2 −1)(1 0 1 ; 1 1 0 ; 1 2 1) ;
  f. (3 4 5 ; 6 7 4)(2 4 3 ; 0 1 1 ; 2 2 −1). (Identique à l'Ex. 8 p.230.)
- **I. Appl. 3** (p.214) : A = 2(3 ; −1) + 5(3 ; −3) ; B = 2(1 0 ; 2 −3) − 5(6 −2 ; 7 −1) ;
  C = −2(1 −2 0 ; 3 7 −1 ; 2 4 −2) + (2/3)(0 4 −3 ; −1 6 −3 ; 2 8 0).
- **I. Appl. 4** (p.214) : A² = A × A pour A = (1 −1 ; 1 −1).
- **I. Appl. 5** (p.214) : M = (3 2 ; 2 −1) ; chercher N = (a b ; c d) telle que M x N = I₂.
- **II. Appl. 1** (p.217) : déterminants |2 1 ; −5 3| ; |2 0 6 ; 1 1 −4 ; 1 0 5| ; |1 a a² ; 1 b b² ;
  1 c c²|.
- **II. Appl. 2** (p.217) : déterminants de (a b c ; 0 d e ; 0 0 f) ; (u 0 0 ; v x 0 ; w y z) ;
  (r 0 0 ; 0 s 0 ; 0 0 t) ; conclusions ?
- **II. Appl. 3** (p.217) : A carrée d'ordre 3, det(A) = δ, k réel ; déterminant de a) B = kA ; b) C obtenue
  en multipliant la 1ʳᵉ colonne par 3k, la 2ᵉ par −5k² et en divisant la 3ᵉ par 4.
- **II. Appl. 4** (p.218) : vérifier sur un exemple det(M × N) = det(M).det(N) (M, N carrées d'ordre 2 ou 3).
- **III. Appl. 1** (p.220) : A = (1 3 1 ; 3 1 3 ; −1 5 7) ; 1) vérifier ComA = (−8 −24 16 ; −16 8 −8 ;
  8 0 −8) ; 2) dét(A), en déduire A⁻¹.
- **III. Appl. 2** (p.220) : montrer l'inversibilité et inverser A = (1 1 ; 0 1), B = (−1 −1 −3 ; 1 2 0 ;
  0 0 1), C = (1 0 0 ; 0 2 0 ; 0 0 3).
- **III. Appl. 3** (p.220) : M = (1 0 0 ; 0 0 −1 ; 0 1 2) ; vérifier (I₃ − M)³ = θ ; en déduire M inversible
  et son inverse.
- **III. Appl. 4** (p.220) : A = (2 1 −4 ; 3 3 −5 ; 4 5 2), B = (1/12)(19 −18 7 ; −14 12 −2 ; 3 −6 3) ;
  dét(A), dét(B), A x B, dét(A x B).
- **III. Appl. 5** (p.220) : montrer que si M inversible, det(M⁻¹) = 1/det(M).
- **IV.1 Appl. 1** (p.224) : P = (−4 −4 2 ; 3 0 1 ; 2 1 0) ; 1) déterminant, P inversible ; 2) par le
  procédé des activités, vérifier P⁻¹ = ½(−1 2 −4 ; 2 −4 10 ; 3 −4 12) ; 3) résoudre P(x ; y ; z) =
  (−1 ; 2 ; 5).
- **IV.1 Appl. 2** (p.224) : inverse, si elle existe, de B = (2 1 −1 ; 3 −1 0 ; −1 1 2).
- **IV.1 Appl. 3** (p.224) : résoudre {−x + 3y + z = 1 ; 2x + 5y = 3 ; 3x + y − 2z = −2}.
- **IV.1 Appl. 4** (p.224) : A = (1 0 0 ; 0 −4 10 ; 0 −3 7) ; 1) A² ; 2) A² − 3A + 2I = θ ; 3) A inversible,
  A⁻¹.
- **IV.2 Appl. 1** (p.226) : {x + y − z = 10 ; x + 10z = 10 ; x + y + 9z = 20} ; 1) système de Cramer ; 2) vérifier la solution (0 ; 11 ; 1).
- **IV.2 Appl. 2** (p.226) : résoudre {3x − 2y + 4z = −7 ; 5x + 7y − 3z = 16 ; x + y − z = 6} par Cramer.
- **IV.2 Appl. 3** (p.226) : résoudre d'abord algébriquement (substitution ou réduction), puis par Cramer :
  {u + v + w = 1 ; 2u − v − w = 5 ; −u + 2v − 3w = −4} et {2x − y = 11 ; 3x − 4z = −1 ; 3x + 4y − z = 0}.

### Apprendre à chercher (p.227)

- **Situation 1 : Un problème d'Euler** — « Trois personnes jouent ensemble trois parties. A chaque partie,
  le perdant double l'avoir de chacun des deux autres joueurs. Ils se retirent du jeu avec 24 louis chacun.
  On demande combien chaque joueur avait d'argent au début de jeu, sachant que chacun d'eux a perdu une
  partie. » « Vers une solution : mise en équation » : tableau des avoirs (début x, y, z ; après la 1ʳᵉ
  partie x − y − z, 2y, 2z ; après la 2ᵉ 2(x − y − z), 3y − x − z, 4z ; après la 3ᵉ 4(x − y − z),
  2(3y − x − z), 7z − x − y) ; système {4(x − y − z) = 24 ; 2(3y − x − z) = 24 ; 7z − x − y = 24} ;
  « La solution est x = 39, y = 21, z = 12. »
- **Situation 2** — (S) {x − y = 0 (1) ; y − z = 1 (2) ; z − x = 0 (3)} ; on forme (S′) {x − z = 1 (1)+(2) ;
  z − y = 0 (1)+(3) ; x + y − 2z = 1 (2)−(3)}. « Il est clair que le système(S) est sans solution alors que
  (1, 0 , 0) est une solution de (S'). D'où vient l'erreur ? »
- **Situation 3** — {ax + y + z = 0 ; x + ay + z = 0 ; x + y + az = 0}, a réel ; matrice (a 1 1 ; 1 a 1 ;
  1 1 a), permutée en (1 1 a ; a 1 1 ; 1 a 1), transformée (« quelles sont les transformations ? ») en
  (1 1 a ; 0 1−a 1−a² ; 0 a−1 1−a) ; cas a = 1 ; si a ≠ 1, (1 1 a ; 0 1 1+a ; 0 −1 1) puis (1 1 a ; 0 1 1+a ;
  0 0 2+a), « comment ? » ; si a = −2, système équivalent à {x + y = 2z ; y = z}, solutions ? ; si a ≠ −2,
  montrer que l'unique solution est (0, 0, 0).

### Avec l'outil informatique (p.228) — « Avec EXCEL »

- Identification d'une matrice par une plage (ex. A1 : C3) ; nommer : « Insertion / Nom / Définir » ;
  opérations matricielles validées par « Ctrl Maj Entrée » ; formules : « = A+B », « = 3*A-B »,
  « = PRODUITMAT (A ; B) », « = A^n », « = INVERSEMAT(A) ».
- **Résolution d'un système avec un tableur** : 1) (S) {3x + 2y + 6z = 24 ; 2x + 4y + 3z = 23 ;
  5x + 3y + 4z = 33} ; a) forme AX = B ; b) A en A1 : C3, B en E1 : E3 (feuille imprimée) ; c) en A5
  « = INDEX(INVERSEMAT($A$1 :$C$3) ;1 ;1) » ; d) recopier à droite (indices (1 ; 2), (1 ; 3)) ; e) recopier
  vers le bas (A5 : C7) ; f) en E5 « = INDEX(PRODUITMAT($A$5 :$C$7 ;$E$1 ;$E$3) ;1 ;1) » [sic : « ;$E$1
  ;$E$3 » pour la plage $E$1:$E$3] ; g) recopier sur E5:E7 « les termes a₂₁, a₂₂ et a₂₃ de A⁻¹B » [sic] ;
  conclure. 2) résoudre avec Excel {3a − 2b + 6c = 0 ; 24a − 12b + 41c = 2 ; −17a + 9b − 5c = 5}.

### Exercices et problèmes (p.229–233) — 26 blocs numérotés (1–26 sans « 24 », « 25 » deux fois) + 1 bloc non numéroté

- **Ex. 1** (p.229, QCM « Indiquer la réponse exacte ») : 1) u = (−4 ; 2 ; −1) est de dimension ☐ 1 ☐ 2
  ☐ 3 ; 2) une matrice 3 x 2 a ☐ 3 lignes et 2 colonnes ☐ 2 lignes et 3 colonnes ☐ 6 lignes et 6 colonnes ; 3) u = (1 ; 2 ; 3), v = (−2 ; 3 ; 2) : 2u + v = ☐ (0 ; 7 ; 8) ☐ (−2 ; 10 ; 10) ☐ (−3 ; 8 ; 7) ; 4) A = (2 3 ; −1 0), X = (−1 ; 1) : ☐ A + X = (1 3 ; 0 0) ☐ A + X = (2 2 ; −1 1) ☐ on ne peut pas
  additionner ; 5) X = (2 −2 1 ; 1 0 3), Y = (0 ; 1 ; −1) : ☐ X × Y = (−3 ; −3) ☐ X × Y = (−3 −3) ☐ « On
  peut pas multiplier X et Y » ; 6) (1 1 ; −2 0)(x ; y) = (1 ; 2) est l'écriture matricielle de
  ☐ {x − 2y = 1 ; x = 2} ☐ {2x = 1 ; −2y = 2} ☐ {x + y = 1 ; −2x = 2}. (Réponses non fournies.)
- **Ex. 2** (p.229, Vrai-Faux « Dire si l'affirmation est vraie ou fausse. Justifier la réponse ») : 1) un vecteur-colonne de dimension 4 est une matrice 2 x 2 ; 2) A = (1 2 ; 3 4), B = (0 −1 ; 3 1) ⇒
     A + B = (−2 ; 11) ; 3) A = (1 2 3), B = (−1 ; 2 ; −1) ⇒ A × B = θ ; 4) {2x − y + z = −3 ; 3x + 2y + z = 7 ;
     x + y − z = 6} s'écrit (2 3 1 ; −1 2 1 ; 1 1 −1)(x ; y ; z) = (−3 ; 7 ; 6) ; 5) {7x + 3y − 3z = a ;
     −8x + 5y − 4z = b ; 5x − 7y + 5z = c} ⇔ (1/54)(3 −6 −3 ; −20 −50 −52 ; −31 −64 −59)(a ; b ; c) = (x ; y ; z).
- **Ex. 3** (p.229) : énoncé et solution d'élève à corriger : a) résoudre {5x + 2y = a ; 4x + y = b} ; b) en
  déduire l'inverse de A = (5 2 ; 4 1). Solution de l'élève : avec a = 1, b = 3, x = 5/3, y = −11/3 ;
  A⁻¹ = (−0,33 0,66 ; 1,33 −1,66). Corriger et rédiger.
- **Ex. 4** (p.229–230) : M = (2 0 ; 2 1) ; 1) M(0 ; 1), M²(0 ; 1), Mⁿ(0 ; 1) (Mⁿ = M × … × M, n ≥ 2) ; 2) même question avec (1 ; 2) au lieu de (0 ; 1).
- **Ex. 5** (p.230) : graphe des liaisons aériennes quotidiennes entre aéroports de trois pays A (A₁, A₂),
  B (B₁, B₂), C (C₁ … C₄) (ex. : 4 vols entre A₂ et B₂) ; a) matrices M (A vers B), N (B vers C), P (A vers
  C) ; b) vérifier P = M × N, interpréter.
- **Ex. 6** (p.230) : A = (0 0 1 ; 1 0 0 ; 0 1 0) ; a) A², A³, A⁴ ; b) expression de Aⁿ, n ∈ ℕ.
- **Ex. 7** (p.230) : A x B et B x A avec A = (1 ½ ; 2 1), B = (−½ −1 ; 1 2) ; le produit des matrices
  carrées est-il commutatif ?
- **Ex. 8** (p.230) : produits a)–f) (identiques à l'Application 2 de I, p.214).
- **Ex. 9** (p.230) : A = (1 2 3 ; 0 3 0), B = (0 −2 −3 ; 1 2 3) ; a) A + B ; 4A − 3B ; b) produit A x B
  possible ?
- **Ex. 10** (p.230) : a ∈ ℝ, A = (−a 0 0 ; 0 a 1 ; 0 −1 a), B = (−2 −1 0 ; −1 0 1 ; 0 1 2) ; 1) condition
  sur a pour A inversible ; 2) réels a tels que B − aI₃ non inversible.
- **Ex. 11** (p.230–231) : confection : jupe 0,75 m de tissu, 4 boutons, 1 fermeture ; robe 1,50 m, 6, 1 ;
  pantalon 1,25 m, 2, 1 ; x, y, z quantités, a, b, c tissu/boutons/fermetures ; M = (0,75 1,50 1,25 ;
  4 6 2 ; 1 1 1), A = (x ; y ; z), B = (a ; b ; c). 1) a) B = M x A ; b) a, b, c pour 200 jupes, 120 robes,
  320 pantalons ; 2) M′ = (−1,6 0,1 1,8 ; 0,8 0,2 −1,4 ; 0,8 −0,3 0,6) : a) M′ × M ; b) A en fonction de B
  et M′ ; c) x, y, z pour 735 m de tissu, 2400 boutons, 620 fermetures.
- **Ex. 12** (p.231) : stocks de calculatrices A et B dans trois points de vente M = (8 11 ; 17 5 ; 12 1),
  prix N = (45 ; 60) dinars ; 1) M x N ; 2) signification.
- **Ex. 13** (p.231) : déterminer A telle que (2 5 ; 1 3)A = (4 −6 ; 2 1) ; A(2 1 ; 2 1) = (1 0 ; 0 1) ;
  (1 2 −3 ; 0 1 2 ; 0 0 1)A = I₃.
- **Ex. 14** (p.231) : T = (0 1 0 ; 0 0 1 ; 0 0 0), A = (1 1 0 ; 0 1 1 ; 0 0 1) ; 1) A = T + I₃ et
  A × I₃ = I₃ × A = A ; 2) T², T³, en déduire Tⁿ puis Aⁿ, n ∈ ℕ.
- **Ex. 15** (p.231) : A = (1 1 0 ; −1 0 0 ; 2 0 −1) ; 1) A³, en déduire A⁻¹ ; 2) résoudre A(x ; y ; z) =
  (2 ; 3 ; 1).
- **Ex. 16** (p.231) : A = (2 −1 3 ; −3 1 −1 ; 1 1 1) ; 1) A², B = 4A − A², A x B, en déduire A⁻¹ ; 2) « Résoudre par un calcul matriciel, le système d'équations suivant : » — système non imprimé sous
  l'exercice (voir doute : vraisemblablement celui placé sous l'Ex. 17).
- **Ex. 17** (p.232) : « Résoudre, par la méthode des déterminants, les systèmes suivants » :
  {2x − y + 3z = −1 ; −3x + y − z = 5 ; x + y + z = −1} (imprimé sous le titre) ; puis, imprimés sous
  l'Ex. 18, {x + 2y + 3z = −2 ; 4x + 5y + 6z = 1 ; 7x + 8y + 9z = 3} et {7x + 3y − 3z = 2 ;
  −8x + 5y − 4z = −1 ; 5x − 7y + 5z = 6}.
- **Ex. 18** (p.232) : déterminer toutes les matrices carrées d'ordre 2 vérifiant A² = A.
- **Ex. 19** (p.232) : besoins trimestriels (crayons, stylos, surligneurs) : secrétariat 100, 200, 100 ;
  comptabilité 200, 300, 180 ; atelier 500, 300, 120. 1) matrice A ; signification de (1 1 1)A et
  A(1 ; 1 ; 1) ; 2) prix unitaires (dinars) des fournisseurs A, B, « B » [sic, pour C] : crayons 0,250 /
  0,280 / 0,300 ; stylos 0,120 / 0,110 / 0,110 ; surligneurs « 0500 » [sic] / 0,450 / 0,420 ; par un produit
  de matrices, dépenses de chaque service selon le fournisseur ; a) choix le plus économique pour le
  secrétariat ; b) intérêt d'une commande commune ?
- **Ex. 20** (p.232) : A = (1 1 1 ; 1 1 1 ; 1 1 1) ; A⁰ = I₃, A¹ = A, Aⁿ⁺¹ = Aⁿ × A ; montrer Aⁿ⁺¹ = 3ⁿ.A.
- **Ex. 21** (p.232) : île : chaque année 40 % des habitants de la capitale la quittent, 20 % du reste de
  l'île y viennent ; E₀ = (c₀, b₀). 1) population un, deux, trois ans après ; 2) Eₙ = (cₙ, bₙ) : a) vérifier
  (c₁ ; b₁) = (0,6 0,2 ; 0,4 0,8)(c₀ ; b₀), E₁ = A × E₀ ; b) Eₙ = Aⁿ × E₀ ; c) étudier l'évolution sur
  n années (n < 30) selon des états initiaux, chercher un état stable.
- **Ex. 22** (p.232) : (1) {x − 3y = −1 ; 2x − 6y = −3}, (2) {x − 2,999y = −1 ; 2x − 6y = −3},
  (3) {x − 2,9995y = −1 ; 2x − 6y = −3} ; 1) (1) admet-il des solutions ? 2) vérifier (1498,5 ; 500)
  (resp. (2998,5 ; 1000)) solution de (2) (resp. (3)) ; 3) remarque ?
- **Ex. 23** (p.233) : usine de cartes d'ordinateur, modèles I, B, M ; puces P1, P2, P3 : P1 5, 2, 7 ;
  P2 3, 8, 6 ; P3 3, 4, 5. a) matrice A ; b) avec un vecteur colonne X, puces pour 20 cartes I, 12 B,
  18 M ; c) un jour 588 P1, 630 P2, 470 P3 utilisées ; compléter A(x ; y ; z) = (… ; … ; …) et trouver x, y, z
  avec A⁻¹.
- **Ex. 25 (1ᵉʳ)** (p.233, colonne gauche) : M = (0 1 1 ; 1 0 1 ; 1 1 0) ; 1) M² ; 2) M² − M − 2I₃ = θ, M
  inversible, M⁻¹ ; 3) résoudre M(x ; y ; z) = (3 ; 2 ; 1).
- **Ex. 25 (2ᵉ)** (p.233, colonne droite) : A = (−15 10 8 ; −8 6 4 ; −24 15 13) ; 1) A² ; 2) A² − 3A + 2I₃ = θ,
  A inversible, expression de A⁻¹ ; 3) résoudre A(x ; y ; z) = (−1 ; 2 ; −3).
- **Bloc non numéroté** (p.233, suit le 2ᵉ « 25 ») : « Pour chacune des matrices suivantes calculer son
  déterminant, puis déterminer sa matrice inverse si elle existe » : a) (2 1 ; 3 1) ; b) (1 −1 2 ; −2 3 −4 ;
  −3 2 1) ; c) (2 3 3 ; 2 1 1 ; −5 7 0).
- **Ex. 26** (p.233) : A = (1 1 1 ; 1 1 1 ; 1 1 1), B = (−3 1 1 ; 1 −3 1 ; 1 1 −3) ; 1) A = B + 4I₃ ; 2) relation entre A et A² ; 3) relation entre B, B², I₃ ; 4) B inversible, B⁻¹ ; 5) résoudre B ×
  (x ; y ; z) = (−5 ; 2 ; −1).

### Maths et culture (p.234) — « LES CARRÉS MAGIQUES »

Définition (somme de chaque ligne, colonne, diagonale « vaut n » [sic : n désigne ici la constante, pas
l'ordre]) ; gravure « la Mélancolie d'Albrecht Dérer [sic, Dürer] (1514) » ; tout carré magique 3 x 3
s'écrit de manière unique m(1 1 1 ; 1 1 1 ; 1 1 1) + y(0 1 −1 ; −1 0 1 ; 1 −1 0) + p(−1 1 0 ; 1 0 −1 ;
0 −1 1) « où m, n, p sont des entiers » [sic : coefficient imprimé « y »] ; constantes magiques des carrés
normaux d'ordre 3, 4, 5, 6, 7, 8 : 15, 34, 65, 111, 175, 260 ; carrés d'ordre 3 (8 1 6 ; 3 5 7 ; 4 9 2),
4 (16 3 2 13 ; 5 10 11 8 ; 9 6 7 12 ; 4 15 14 1), 5 (17 24 1 8 15 ; 23 5 7 14 16 ; 4 6 13 20 22 ;
10 12 19 21 3 ; 11 18 25 2 9) ; « figue [sic] symétrique » en reliant les nombres dans l'ordre croissant.

### Écart avec la référence (aucune référence publiée)

**Référence : AUCUN chapitre publié n'enseigne ce contenu.** Recherche dans `content/` (`matrice`,
`Cramer`, `pivot`, `déterminant`, `systèmes`) : ni `math-bac-math`, ni `math-bac-sciences-exp`, ni
`math-bac-techniques` n'ont de chapitre « matrices / systèmes linéaires » ; la fiche bac-math
(l.3902) note même que les équations analytiques y sont traitées « sans formalisme matriciel ». Les
chapitres les plus proches, à n'utiliser que comme source partielle :

- `math-1ere-sec/15-systemes-deux-equations` : systèmes 2×2 par substitution / élimination, interprétation
  graphique (droites sécantes / parallèles / confondues) — couvre seulement le prérequis « méthode
  algébrique (substitution ou réduction) » invoqué en IV.2 Appl. 3 ;
- `math-bac-sciences-exp/13-produit-scalaire-vectoriel` (et `math-bac-techniques/13`) : déterminant de
  trois vecteurs développé suivant la 1ʳᵉ ligne (même formule a(b′c″ − c′b″) − …) — couvre le calcul d'un
  déterminant 3×3, mais dans un cadre vectoriel (coplanarité, volume) absent ici.

**À créer de zéro (tout le chapitre)** : matrices (dimension n x p, coefficient aᵢⱼ, vecteur-ligne /
vecteur-colonne, matrice carrée, diagonale, unité Iₙ, nulle θ, égalité) ; somme, produit par un réel,
propriétés ; produit matriciel (condition de dimension, disposition en croix, non-commutativité,
associativité, distributivité) ; puissances Aⁿ ; transposée Aᵗ ; déterminant d'ordre 2 et 3 (développement
suivant une ligne ou une colonne avec (−1)^(i+j), propriétés : permutation, lignes identiques ou
proportionnelles, facteur commun, combinaison linéaire) ; det(M × N) = det(M).det(N) et
det(M⁻¹) = 1/det(M) (en applications) ; matrice inverse (ordre 2 : formule explicite ; ordre 3 : critère
dét ≠ 0, mineur, cofacteur, comatrice, A⁻¹ = (1/det A)(ComA)ᵗ ; méthode de Gauss-Jordan par opérations sur
les lignes ; inverse via un polynôme annulateur A² − 3A + 2I = θ, B³ + I₃ = θ, (I₃ − M)³ = θ) ; écriture
matricielle AX = B et X = A⁻¹B ; pivot de Gauss ; système de Cramer (n = 2 ou 3) et formules de Cramer ;
systèmes à paramètre (Situation 3, Act. II.2) ; mal-conditionnement (Ex. 22) ; modélisations (stocks,
production, liaisons aériennes = produit matriciel, migrations Eₙ = AⁿE₀) ; Excel (PRODUITMAT,
INVERSEMAT, INDEX, Ctrl Maj Entrée).

**Vocabulaire / notations propres à ce manuel** : « dét (A) » et « det(A) » alternent ; produit noté
« A x B » ou « A × B » ; matrice nulle « θ » ; matrice unité « matrice unité » / « matrice identité » ;
cofacteur αᵢⱼ ; « Com A » ; transposée « Aᵗ » ; « matrice complète » (= augmentée) ; « transformation
élémentaire » notée Lᵢ ← … ; « système de cramer » (minuscule p.224).

### Bornes de scope (chapitre 11, section Sciences de l'informatique)

- ✅ INCLUS : matrices réelles n x p et vocabulaire ; somme, produit par un réel, produit matriciel et leurs
  propriétés ; non-commutativité ; puissances ; transposée ; déterminant d'ordre 2 et 3 (développement,
  propriétés) ; matrice inverse d'ordre 2 et 3 (formule ordre 2, comatrice, Gauss-Jordan, polynôme
  annulateur) ; forme matricielle AX = B, X = A⁻¹B ; pivot de Gauss ; systèmes de Cramer d'ordre 2 et 3 et
  formules de Cramer ; systèmes à paramètre réel ; problèmes concrets modélisés par matrices ; tableur Excel.
- ⛔ EXCLU (absent de ces pages) : matrices d'ordre ≥ 4 (sauf carrés magiques culturels) ; rang, noyau,
  espaces vectoriels, applications linéaires ; valeurs propres / diagonalisation (Ex. 21 c reste empirique,
  « n < 30 ») ; déterminant d'ordre n général ; matrices complexes ; méthode de Gauss pour systèmes non
  carrés (aucun exemple) ; interprétation géométrique des systèmes 3×3 (plans) ; lien avec le déterminant de
  trois vecteurs de l'espace.

### Lecture

- **Pages lues en L1 (pdftotext -layout)** : p.209 à p.234, toutes.
- **Pages lues sur l'image (110 dpi)** : p.209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221,
  222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234 = **26 pages sur 26** (100 % ; toutes
  portent matrices ou formules).
- **Écarts texte / image constatés** : toutes les matrices sont éclatées en L1 (parenthèses perdues, signes
  « − » perdus : p.214 a₁₃ = 5 au lieu de −5 ; p.219 ComA sans signes ; p.220 ComA « 8 24 16 » au lieu de
  −8 −24 16 ; p.233 A = (15 10 8 …) au lieu de (−15 10 8 …)) ; fractions et déterminants désalignés (p.215
  Δ illisible, p.222 matrices augmentées illisibles) ; « ≤ », « ≠ », « ← », « θ », « ℝ » perdus ou rendus
  par des blancs ; p.218 la matrice A d'Act. III.1 absente du texte ; p.217 Appl. 2 (trois matrices)
  totalement absente en L1 ; p.230 graphe de l'Ex. 5 non rendu ; p.234 coefficients de la décomposition des
  carrés magiques sans signes. **Toute formule vient de l'image.**
- **Coquilles [sic]** : « semis-finis » (p.211) ; « produit d'une matrice M … notée k A … coefficient de A »
  (p.211) ; « Lorsque n = m » (p.212) ; « indce » (p.213) ; « ax + a2 + az = -1 » (p.215, y manquant) ;
  « Calculer que Δ » (p.215) ; « otenu » (p.219) ; « En transposons » (p.219) ; numérotation « 2) a) »
  après « a) b) » dans Act. III.3 (p.218–219) ; titre « Inverse d'une matrice carrée d'ordre 2 » pour une
  définition d'ordre 2 ou 3 (p.220) ; « systèmede Cramer », « système de cramer » (p.224) ; en-têtes
  « Chapitre 12 » p.227–228 ; « $E$1 ;$E$3 » et « a₂₁, a₂₂ et a₂₃ de A⁻¹B » (p.228) ; « On peut pas »
  (p.229) ; fournisseurs « A, B, B » et « 0500 » (p.232, Ex. 19) ; numéro 24 absent et 25 répété (p.233) ;
  « Dérer », « figue », « + y(…) … où m, n, p » (p.234) ; « constante … vaut n » (p.234).
- **Doutes signalés** : (1) Ex. 16 2) annonce « le système d'équations suivant » sans le donner ; la matrice
  de l'Ex. 16 (2 −1 3 ; −3 1 −1 ; 1 1 1) est exactement celle du système {2x − y + 3z = −1 ; …} imprimé sous
  le titre de l'Ex. 17 : mise en page probablement décalée (ce système appartient sans doute à l'Ex. 16, et
  les deux systèmes placés sous l'Ex. 18 à l'Ex. 17) — à trancher ; (2) le système de l'activité Cramer
  (p.224, 3ᵉ équation « = 1 ») diffère de celui de IV Act. préliminaire 1 (p.221, « = 11 ») pour le même
  membre de gauche — les deux sont reproduits tels quels ; (3) phrase finale de p.225 (« … pour les systèmes
  carrés d'ordre 2 : ») sans suite imprimée ; (4) le bloc non numéroté p.233 est peut-être l'Ex. « 24 »
  manquant ; (5) Act. III.1 duplique quasi littéralement II Act. 1 (même énoncé, à deux formulations près) — la définition de l'inverse figure donc deux
  fois.

## 2.12 Chapitre 12 — Séries statistiques à deux caractères (manuel 222472, p.235–268)

**Page de garde (p.235)** — « Chapitre 12 », titre « SÉRIES STATISTIQUES A DEUX CARACTÈRES ». Plan imprimé :
« I . Activités de rappel · II . Nuage de points–Cœfficient de corrélation linéaire · III . Ajustements
affines · IV . Exemples d'ajustements non affines ». Portrait légendé « Giuseppe Piazzi » et texte : « Le 1er
janvier 1801, l'astronome G. Piazzi a décelé dans le ciel un objet inconnu. Après l'avoir étudié pendant
quelques temps, il fit part de sa découverte. Mais lorsque ses collègues voulurent observer cet objet, ils ne
le trouvèrent plus. Le mathématicien Carl Friedrich Gauss appliqua alors la méthode des moindres carrés qu'il
avait mise au point quelques années plus tôt et réussit à prédire, à partir des observations de Piazzi, où
serait précisément cet objet céleste le dernier jour de l'année. »

**Plan du chapitre** : **Cours** — **I. Activités de rappel** (p.236–238 : Act. 1–7, statistique à une
variable) · **II. Nuage de point– cœfficient de corrélation linéaire** [sic « point », titre de p.238]
(p.238–244 : « Activités de découverte » Act. 1–3 p.238–240 ; « A retenir » p.241–242 ; « Applications » 1–2
p.242–244) · **III. Ajustements affines** (p.244–249 : Act. 1 p.244–245 — imprimée AVANT le titre « III.
Ajustements affines / Activités de découverte » — ; Act. 2 p.245 ; « Activités 3 » [sic] p.246 ; « A
retenir » p.247 ; « Applications » 1–5 p.247–249) · **IV. Exemples d'ajustements non affines** (p.249–250 :
« Ajustement par une fonction puissance », « Ajustement exponentiel », « Ajustement parabolique » — trois
activités non numérotées, sans « A retenir »). Puis **Apprendre à chercher** (p.251–253 : Situations 1–3,
avec « Vers une solution » pour 1 et 2), **Avec l'outil informatique** (p.254–255 : « Meilleur ajustement et
tableur »), **Exercices et problèmes** (p.256–266 : 19 exercices ; Ex. 1 titré « VRAI-FAUX » mais au format
QCM, Ex. 7 titré « VRAI - FAUX »), **Maths et culture** (p.267–268 : « Une brève histoire des outils
statistiques »). Pas d'exercices résolus, pas de « Tout ce qu'on doit savoir ». En-têtes de p.241 et p.247 :
« Chapitre 13 : Séries statistiques à deux caractéres » [sic].

### Cours — Activités (une ligne chacune)

**I. Activités de rappel**

- **Act. 1** (p.236) : notes du dernier devoir de contrôle de mathématiques de la 4ᵉ sciences de
  l'informatique : 14 16 12 10 12 14 15 15 16 16 15 12 12 16 10 18 16 14 9 12 10 18 ; calculer X̄, V, σ.
  (Rappels des formules, voir encadrés.)
- **Act. 2** (p.236) : diagramme en boîte (repères a, b, c, d, e) ; identifier les paramètres. [« digramme »
  sic]
- **Act. 3** (p.236) : notes de fonctionnaires sur 40, X̄ = 16 ; 1) moyenne x̄ des notes ramenées sur 20 ; 2) on ajoute 1 point sur 20 à tous : moyenne m ? 3) m en fonction de x̄.
- **Act. 4** (p.236–237) : espérances de vie (1995) de 21 pays d'Afrique de plus de 10 millions d'habitants :
  55 69 47 47 55 47 46 58 49 52 39 / 53 69 40 41 52 42 51 53 49 40. 1) une valeur médiane et « les deux
  quartiles (Q₁ et Q₂) » [sic, pour Q₃] ; 2) diagramme en boîte ; 3) placer Haïti (49 ans, plus basse
  d'Amérique) et l'Inde (61 ans). ➢ rappels médiane, quartiles, intervalle et écart interquartile.
- **Act. 5** (p.237) : interventions chirurgicales quotidiennes 0, 1, 2, 3, 4, 5, 6 ; effectifs (en jours)
  84, 105, 72, 59, 28, 15, 2. 1) tableau des fréquences ; 2) moyenne et écart-type par les fréquences
  (arrondis au dixième) ; 3) pourcentage (au dixième) des valeurs dans [X̄ − σ ; X̄ + σ].
- **Act. 6** (p.237) : chiffre d'affaires (milliers de dinars) de 500 magasins, classes [100 ; 150[ … [450 ;
  500[ d'effectifs 40, 50, 60, 70, 100, 80, 60, 40. 1) a) effectifs cumulés croissants ; b) Q₁ ∈ [200 ;
  250[ ; c) classes de Me et Q₃ ; 2) hypothèse de répartition uniforme dans [200 ; 250[ : a) expliquer
  (Q₁ − 200)/(125 − 90) = (250 − 200)/(150 − 90) (tableau 200 / Q₁ / 250 ↔ 90 / 125 / 150) ; b) Q₁ arrondi au
  dixième ; c) Me et Q₃ de même.
- **Act. 7** (p.238) : 100 nombres au hasard (0 à 9) de la touche « Random » (tableau 4 × 25 imprimé) ; 1) a) moyenne attendue ; b) vérifier sur S₁ ; c) écart-type au dixième ; 2) groupes de 4 : a) 25 moyennes ;
     b) moyenne de S₂, prévisible ? c) écart-type de S₂ ; d) comparer avec S₁ ; 3) groupes de 10 → S₃ :
     a) moyenne et écart-type ; b) diagrammes en boîte de S₂ et S₃ ; c) conclusion.

**II. Nuage de points – coefficient de corrélation linéaire — Activités de découverte**

- **Act. 1** (p.238–239) : consommation de tabac (g/jour, plus de 15 ans) et indice du prix (base 100 en
  1970), années 1995–2004, rangs 1–10 : xᵢ = 5,1 [imprimé « 5 ,1 »] ; 5 ; 4,8 ; 4,7 ; 4,7 ; 4,6 ; 4,6 ;
  4,4 ; 3,9 ; 3,3 ; yᵢ = 121 ; 126 ; 136 ; 138 ; 143 ; 147 ; 152 ; 162 ; 180 ; 220. Population
  A = {a₁, …, a₁₀}. 1) a) les 10 couples (➢ série statistique à deux caractères) ; b) X̄ « (xᵢ) 1 ≤ i ≤ j »
  [sic] ; c) Ȳ ; 2) a) nuage Mᵢ(xᵢ ; yᵢ) (1 cm pour 1 g ; 1 cm pour 10 points d'indice, graduation à partir
  de 120), placer en rouge G « de coordonnées (Ȳ ; X̄) » [sic, inversé] ; ➢ nuage de points, point moyen
  G(X̄ ; Ȳ) ; b) tracer à l'œil une droite proche des points ; c) droite (GM₁₀), équation (coefficients au
  centième) ; 3) estimer la consommation pour un indice 250 (graphiquement puis par le calcul).
- **Act. 2** (p.239–240) : série (xᵢ ; yᵢ) = (10 ; 105), (11 ; 107), (13 ; 110), (15 ; 111), (17 ; 112),
  (18 ; 115). 1) X̄, Ȳ, σ(x), σ(y) ; 2) ➢ covariance (définition), la calculer ; 3) montrer
  cov(X ; Y) = (1/n)Σxᵢyᵢ − X̄Ȳ, cov(aX + b ; Y) = a cov(X ; Y), cov(X ; X) = V(X) ; ➢ « Ainsi un changement
  d'unité ou d'origine du repère affecte la covariance . » 4) admis cov²(X ; Y) ≤ V(X)V(Y), en déduire
  |cov(X ; Y)| ≤ σ(X)σ(Y) ; 5) quand V(X) et V(Y) sont-ils nuls ? ➢ coefficient de corrélation linéaire
  cov/(σ(X)σ(Y)), « Ce réel garde la même valeur quelque soit l'unité choisie » ; le calculer.
- **Act. 3** (p.240) : a) nuage et coefficient de corrélation de (zᵢ ; tᵢ) = (10 ; 105), (11 ; 107),
  (13 ; 110), (15 ; 111), (17 ; 112), (18 ; 115) et de (xᵢ ; yᵢ) = (30 ; 9), (60 ; 14), (114 ; 14), (122 ; 51) ;
  b) conjecture sur le lien forme du nuage / coefficient.

**III. Ajustements affines**

- **Act. 1** (p.244–245) : consommation tunisienne (tonnes) d'une matière première M, 1996–2003 : 7740, 7800,
  7880, 7900, 7920, 8000, 8020, 8060 ; xᵢ rang à partir de 1996. 1) nuage (2 cm pour 1 unité ; 1 cm pour
  20 unités, à partir de 7720) ; 2) sous-nuages M₁–M₄ et M₅–M₈ : a) points moyens G₁, G₂ ; b) équation de
  (G₁G₂), la tracer ; c) estimer la consommation en 2007 ; 3) a) deux autres sous-nuages de 4 points, G′₁,
  G′₂, droite (G′₁G′₂), estimation 2007 ; b) une estimation est-elle meilleure ? ➢ « La droite (G₁ G₂) est
  appelée **la droite de MAYER** (1814-1878) ». **Commentaire** (modéliser, ajustement de Y en X, modèle,
  variable explicative / expliquée ; trois croquis de nuages ajustés par une droite et par des courbes).
- **Act. 2** (p.245) : série (1 ; 3), (2 ; 4), (3 ; 6) ; D droite variable par G de coefficient directeur a. 1) a) G ; b) équation de D ; c) coefficient de corrélation ; d) nuage ; 2) P₁, P₂, P₃ points de D
     d'abscisses 1, 2, 3 : a) Σ(MᵢPᵢ)² en fonction de a ; b) a minimisant la somme ; ➢ **droite de régression**
     de Y en X ; 3) construire D.
- **Act. 3** (p.246, « Activités 3 ») : production xᵢ (milliers) 20, 50, 80, 90, 100, 120, 160, 180 ; charge
  yᵢ (milliers d'heures) 60, 85, 90, 105, 115, 125, 140, 160. 1) nuage ; 2) G(X̄ ; Ȳ), vérifier r = 0,98 ; 3) D : y = ax + b par G : montrer b = ȳ − ax̄ ; 4) f(a) = Σ(MᵢPᵢ)² minimale : a) « Montrer que
  8 f(a) = a²V(X) − 2aCov(X,Y) + V(Y) » [sic ? voir doutes] ; b) a = cov(X,Y)/V(X) ; 5) calculer a, tracer
  D ; ➢ moindres carrés ; 6) a) D : y = 0,6x + 50,4 ; b) charge pour une production de 300 unités.
  ➢ interpolation / extrapolation.

**IV. Exemples d'ajustements non affines** (p.249–250, activités non numérotées)

- **Ajustement par une fonction puissance** (p.249) : prix unitaire x (dinars) 1,5 ; 2,5 ; 3,5 ; 4,5 ; 5 ; 7 ;
  8,5 ; demande y (milliers) 8,4 ; 5,3 ; 5,3 ; 3,1 ; 2,8 ; 2,1 ; 1,7 ; offre z (milliers) 0,75 ; 1,23 ; 1,75 ;
  2,25 ; 2,5 ; 3,5 ; 4,25. 1) z proportionnelle à x, fonction g (z = g(x), x ∈ [0 ; 10]) ; 2) droite de
  régression de y en x, prix d'équilibre ; 3) a) Xᵢ = ln(xᵢ), Yᵢ = ln(yᵢ) à 10⁻³ ; b) coefficient de
  corrélation de (X, Y), interpréter ; c) ajustement affine de Y en X ; d) relation y = k x^α.
- **Ajustement exponentiel** (p.250) : population piscicole (milliers) 1995–2000, rangs 1–6 : 951,3 ; 106,7 ;
  96,5 ; 63,2 ; 21 ; 9,4. 1) nuage Mᵢ(xᵢ ; ln(yᵢ)), pourquoi un ajustement exponentiel ; 2) z = ln(y) :
  a) coefficient de corrélation de (x, z) ; b) z = ax + b (au centième) ; c) y = Ae^(Bx) ; 3) a) année où
  la population passe sous 1000 ; b) estimation en 2008.
- **Ajustement parabolique** (p.250) : 11 élèves tracent des disques : rayon xᵢ (cm) 2 ; 2,5 ; 3 ; 3,5 ; 4 ;
  4,5 ; 5 ; 5,5 ; 6 ; 6,5 ; 7 ; aire Aᵢ (cm²) 12 ; 20 ; 28 ; 38 ; 50 ; 50 ; 78 ; 95 ; 113 ; 113 ; 154. 1) séries proportionnelles ? 2) y = √A : a) tableau (xᵢ ; yᵢ) au dixième ; b) nuage (2 cm) ; c) droite
     d'ajustement de y en x (au centième) ; d) la tracer avec G ; 3) A = πX², Y = √A proportionnel à X :
     coefficient ? valeur approchée de π via 2.c).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Rappels (texte de cours, Act. 1)** (p.236) — « ➢ La moyenne arithmétique d'une série statistique
> ( xᵢ,nᵢ ) est donnée par : X̄ = Σᵢ₌₁ⁿ nᵢxᵢ / Σᵢ₌₁ⁿ nᵢ ➢ La variance d'une série statistique (xᵢ, nᵢ) est le
> réel V défini par : V = Σᵢ₌₁ⁿ nᵢ(xᵢ − X̄)² / Σᵢ₌₁ⁿ nᵢ = Σᵢ₌₁ⁿ nᵢxᵢ² / Σᵢ₌₁ⁿ nᵢ − (X̄)² ; ➢ L'écart type
> d'une série statistique (xᵢ, nᵢ) est le réel σ défini par : σ = √V »

> **Rappels (Act. 4)** (p.237) — « ➢ La médiane partage la série ordonnée (dans l'ordre croissant) en deux
> groupes de même effectif. ➢ Les quartiles partagent la série ordonnée en quatre groupes de même effectif.
> ➢ L'intervalle interquartile [Q₁;Q₃] contient 50% des observations ➢ L'écart interquartile I = Q₃- Q₁
> mesure la dispersion de la série par rapport à la médiane. »

> **Texte de cours (Act. II.1)** (p.239) — « L'ensemble des 10 couples (xᵢ, yᵢ) où 1 ≤ i ≤ 10 , est **une
> série statistique à deux caractères**. » ; « ➢ L'ensemble des 10 points Mᵢ(xᵢ;yᵢ) où 1 ≤ i ≤ 10 est **le
> nuage de points** de la série statistique à deux caractères et le point G (X̄;Ȳ) est **le point moyen** de
> ce nuage. »

> **A retenir — Nuage de points — Définitions** (p.241) — « X et Y désignent deux variables statistiques
> numériques observées sur n individus d'une même population. Pour 1 ≤ i ≤ n, xᵢ et yᵢ désignent les mesures
> relevées respectives de X et Y . • Les n couples (xᵢ ; yᵢ) forment **une série statistique à deux
> caractères.** • Dans un repère orthogonal, l'ensemble des n points Mᵢ(xᵢ ; yᵢ) constitue l**e nuage de
> points** associé à cette série statistique double. • Le **point moyen** G du nuage de points Mᵢ(xᵢ ; yᵢ) ,
> 1 ≤ i ≤ n , dans un repère, est le point G( X̄ ; Ȳ ) »

> **Covariance — Définition** (p.241) — « Soit une série statistique double (xᵢ ; yᵢ)₁≤ᵢ≤ₙ définie en
> données individuelles. On désigne par x₁, x₂,..., xₙ les valeurs du 1ᵉʳ caractère quantitatif X et par
> y₁, y₂,..., yₙ celles du 2ᵉᵐᵉ caractère quantitatif Y. On appelle covariance du couple (X ;Y) le réel noté
> cov(X ;Y) et défini par : cov(X;Y) = (1/n)Σᵢ₌₁ⁿ(xᵢ − X̄)(yᵢ − Ȳ) où X̄ = (1/n)Σᵢ₌₁ⁿ xᵢ et
> Ȳ = (1/n)Σᵢ₌₁ⁿ yᵢ »

> **Propriétés** (p.241) — « Avec les notations de la définition, on a : • cov(X ;Y) = (1/n)Σᵢ₌₁ⁿ xᵢyᵢ − X̄Ȳ
> • cov(X ;Y) = cov(Y ;X) • cov(a X + b ;Y) = a cov(X ;Y) pour tous réels a et b . • cov(X;X) = V(X).
> • cov²(X;Y) ≤ V(X)V(Y) »

> **Cœfficient de corrélation linéaire — Définition** (p.241) — « Soient X et Y deux variables
> quantitatives, non constantes et observées dans une même population. On appelle cœfficient de corrélation
> linéaire du couple (X ;Y) le réel r défini par r = cov(X;Y)/(σ(X)σ(Y)) , σ(X) et σ(Y) étant les
> écart-types respectifs de X et Y. »

> **Propriétés** (p.242) — « • −1 ≤ r ≤ 1 . • r est invariant par changement d'unité ou d'origine. • Si
> |r| ≥ 0,75 alors la corrélation linéaire entre X et Y est forte . • Si |r| < 0,75 alors la corrélation
> linéaire entre X et Y est faible. »

> **Texte de cours III — Mayer, Commentaire** (p.245) — « ➢ La droite (G₁ G₂) est appelée **la droite de
> MAYER** (1814-1878) **Commentaire** Lorsque deux caractères X et Y sont liés l'un à l'autre, l'étude de la
> forme du nuage de points permet de **modéliser** cette liaison. La forme d'un nuage de points associé à une
> série à deux variables X et Y invite à retenir, pour l'ajuster, des modèles de fonctions familières : soit
> le modèle affine y = ax + b, soit le modèle exponentiel y = a.bˣ ou autres. Effectuer un **ajustement de Y
> en X** d'un nuage de points consiste à trouver une fonction f telle que la courbe d'équation y = f(x) passe
> « le plus près possible » des points du nuage. Pour les statisticiens, une formule telle que y = f(x) est
> appelé un **modèle** ; x est la variable **explicative** et y la variable **expliquée**. »

> **Texte de cours III — moindres carrés** (p.245–246) — « ➢ La droite ainsi obtenue est appelée **droite de
> régression** de Y en X. » ; « ➢ Σᵢ₌₁⁸(MᵢPᵢ)² est minimale pour la valeur de a déterminée au b). La droite D
> tracée passe donc «le plus proche possible» des points du nuage. C'est-à-dire que la somme des carrés des
> écarts entre les points Mᵢ du nuage et les points Pᵢ de la droite D de même abscisse, est la plus petite
> possible . On dit qu'on a effectué un ajustement linéaire par la méthode **des moindres carrés**. » ;
> « ➢ Pour une valeur donnée xᵢ de la variable X, la fonction f (x) = ax + b permet de prévoir
> approximativement la valeur correspondante de Y ; pour cela on calcule f (xᵢ) . • Si xᵢ appartient à
> l'intervalle d'observation des valeurs de X, on dit qu'on fait une **interpolation.** • Si xᵢ n'appartient
> pas à cet intervalle, on parle d'**extrapolation**, mais dans ce cas il faut faire l'hypothèse que le modèle
> reste plausible à l'extérieur de cet intervalle. »

> **A retenir** (p.247) — « Soient X et Y deux variables statistiques quantitatives, non constantes et
> observées dans une population donnée.Lorsque le cœfficient de corrélation r vérifie |r| ≥ 0,75 ou lorsque
> le nuage de points a une forme allongée, alors il est possible d'effectuer un ajustement affine du nuage de
> points M (xᵢ,yᵢ) . »

> **Théorème et définition** (p.247) — « Lors d'un ajustement affine de Y en X par la méthode des moindres
> carrés, la droite obtenue passe par le point moyen du nuage et a pour équation : y = a ( x - X̄) + Ȳ où
> a = cov(X,Y)/V(X) . Cette droite s'appelle la **droite de régression de Y en X**. La droite de régression de
> X en Y obtenue par la méthode des moindres carrés, lors d'un ajustement affine, passe par le point moyen du
> nuage et a pour équation : x = a' ( y - Ȳ ) + X̄ où a' = cov(X,Y)/V(Y) . »

> **Remarques** (p.247) — « On suppose ici que les points du nuage ne sont pas tous alignés sur une même droite
> verticale, ni sur une même droite horizontale. On a donc σ(X) ≠ 0 et σ(Y) ≠ 0 • Les deux droites de
> régression : { D : y = ax + b ; D' : x = a'y + b' } passent par le point moyen G (X̄; Ȳ). • Les deux
> coefficients a et a' sont de même signe et le cœfficient corrélation r vérifie r² = aa' »

> **Méthode de Mayer** (p.247) — « Cette méthode d'ajustement consiste à partager les données en deux
> groupes de mêmes effectifs ( à un près) après un tri en fonction des valeurs de la première variable. On
> calcule ensuite les coordonnées des points moyens G₁ et G₂ de chaque groupe. On construit alors la droite
> (G₁G₂). »

### Applications (fin des parties II et III) — 7

- **II. Appl. 1** (p.242–243, « Vrai ou faux. Corriger les réponses fausses. ») : séries xᵢ = 1…8 ;
  yᵢ = 1, 1, 8, 5, 3, 8, 9, 8 ; zᵢ = 0, 3, 8, 15, 24, 35, 48, 63 ; tᵢ = 0, 10, …, 70 ; wᵢ = 6,71 ; 9,29 ;
  10,71 ; 0,23 ; 1,68 ; 11,96 ; 8,64 ; 0,23 ; quatre nuages (1)–(4) dessinés. a) Mᵢ(xᵢ;wᵢ) est le nuage (4) ;
  b) Nᵢ(xᵢ;zᵢ) est le nuage (2) ; c) le point moyen du nuage (1) est un de ses points ; d) les points du nuage
  (2) sont alignés ; e) le point moyen du nuage (2) est aligné avec ses points ; f) « Le point du nuage (3)
  sont ceux d'une parabole » [sic] ; g) point moyen de (xᵢ;yᵢ) : G₁(4,5 ; 4) ; h) point moyen de (xᵢ;tᵢ) :
  G₂(4,5 ; 35).
- **II. Appl. 2** (p.243–244) : part des salariés parmi les actifs : années 1975, 1980, 1985, 1990, 1995,
  2000, 2001 ; yᵢ (%) 82,3 ; 84 ; 85,3 ; 87 ; 89,5 ; 91,1 ; 91,3. 1) a) nuage (origine O(1975 ; 80)) ;
  b) G(1989,4 ; 87,2) ; c) covariance, r = 0,99 ; 2) zᵢ = xᵢ − 1975, tᵢ = yᵢ − 80 : a) tableau (2ᵉ ligne
  imprimée « Part en % yi : 2.3 » [sic, pour tᵢ]) ; b) point moyen ; c) covariance, r(Z, T) = 0,99 ; 3) uᵢ = yᵢ/100 : a) tableau (0 ; 0,823), (5 ; 0,84) … ; b) point moyen ; c) covariance, r(Z, U) = 0,99 ; 4) que déduire ?
- **III. Appl. 1** (p.247–248) : taille moyenne (cm) des nouveau-nés selon l'âge gestationnel 30 à 45
  semaines : 47,5 ; 48,5 ; 49 ; 49,7 ; 50 ; 50,5 ; 50,8 ; 51,2 ; 51,5 ; 51,8 ; 52,2 ; 52,5 ; 52,8 ; 53 ; 53,5 ;
  53,7. 1) nuage (1 cm / semaine dès 20 ; 2 cm / unité dès 45 cm) ; 2) méthode de Mayer : G₁, G₂, droite ; 3) équation de la droite.
- **III. Appl. 2** (p.248) : droite de régression de X en Y : x = −0,43y + 12,3 ; valeurs de X : 1 ; 2 ; 5 ;
  7 ; 11 ; 13. (La consigne « Calculer les coordonnées du point moyen. » est imprimée derrière la case « 3 » ;
  voir doutes.)
- **III. Appl. 3** (p.248) : « Calculer les coordonnées du point moyen. » puis espérance de vie des hommes à
  la naissance : 1980, 1985, 1990, 1995, 1998, 1999, 2000, 2001, 2002, 2003, 2004 → 70,02 ; 71,3 ; 72,8 ;
  73,9 ; 74,6 ; 74,9 ; 75,3 ; 75,5 ; 75,8 ; 75,9 ; 76,7. 1) nuage, ajustement affine justifié ? 2) données
  X̄ = 21957/11 ≈ 1996,09 ; Ȳ = 816,9/11 ≈ 74,26 ; Σ(xᵢ − X̄)² = 616,91 ; Σ(xᵢ − X̄)(yᵢ − Ȳ) = 159,84 :
  droite D de y en x (moindres carrés), la tracer ; 3) estimation pour 2007 ; 4) estimation en 2500 ? en 3000 ?
- **III. Appl. 4** (p.248–249) : série (1 ; 4), (2 ; 7), (3 ; 10), (5 ; 14), (6 ; 16). 1) **QCM** « Donner
  toutes les bonnes réponses » : a) D₁ : y = 2x + 4 passe par trois points du nuage, donc est un bon
  ajustement ; b) D₂ : y = 3x + 1 passe par trois points, donc meilleur ajustement ; c) la droite de régression
  Δ de y en x est y = 2,36x + 2,17 (coefficients à 10⁻²). 2) **VRAI OU FAUX** (corriger) : a) pour Δ, D₁, D₂
  on calcule S = Σ(yᵢ − (axᵢ + b))² ; b) pour D₁, les trois derniers termes de S sont nuls ; c) pour Δ tous les
  termes de S sont nuls ; d) S a même valeur pour D₁ et D₂ ; e) S minimale pour Δ ; f) S vaut 5 pour D₁.
- **III. Appl. 5** (p.249) : droite de régression de y en x : y = −0,43x + 12,3 ; X̄ = 5,7 ; r = 0,85 ;
  équation de la droite de régression de x en y.

### Apprendre à chercher (p.251–253)

- **Situation 1** (p.251) : prix de revient kilométrique (D) selon la puissance fiscale 4, 5, 6, 7, 8 CV :
  0,424 ; 0,471 ; 0,492 ; 0,513 ; 0,555. 1) nuage ; 2) G ; 3) droite admise y = 0,03x + 0,311 : a) G ∈ droite ;
  b) la tracer ; 4) prix de revient pour 10 CV (lecture) ; 5) PRK maximum 0,650 D : puissance maximale.
  **Vers une solution** : G(6 ; 0,491) ; 0,03x + 0,311 < 0,65 donc x < 11,3 ; « La puissance fiscale maximale
  autorisée par le comptable est de 11 CV » (graphique PRK / puissance fiscale).
- **Situation 2** (p.251–252) : consommation Y (L/100 km) selon la vitesse X (km/h) 80, 90, 100, 110, 120 :
  4 ; 4,8 ; 6,3 ; 8 ; 10. 1) proportionnalité ? 2) a) nuage (2 cm pour 10 km/h, 1 cm pour 1 L) ; b) G ;
  c) droite des moindres carrés ; d) consommation à 130 km/h ; 3) z = ln(y), droite admise
  z = 0,0234x − 0,508 : a) y = Ae^(Bx) (A, B à 10⁻⁴) ; b) tracer pour x ∈ [80 ; 120] ; c) consommation à
  130 km/h ; 4) quelle valeur est la plus proche du réel ? **Vers une solution** : 1) 4/80 ≠ 10/120 ; 2) c) y = 0,152x − 8,58, à 130 km/h y = 11,18 (≈ 11,2 L) ; 3) a) y = e^(0,0234x − 0,508) ;
  A = e^(−0,508) ≈ 0,6017 ; c) y = 0,6017e^(0,0234×130), ≈ 12,6 L ; 4) « La seconde valeur (12,6) est la plus
  vraisemblable » (accroissements de plus en plus grands, +2 L entre 110 et 120).
- **Situation 3** (p.253) : poids (kg) du fils de « Monsieur Math » aux âges 7 à 12 ans : 22, 24, 28, 34, 42, 51. 1) nuage (1 cm / an ; 1 cm / 4 kg) ; 2) zᵢ = √yᵢ à 10⁻² ; 3) a) nuage (xᵢ, zᵢ), coefficient de
  corrélation, G ; b) droite de régression de z en x ; 4) poids à 20 et 25 ans ; que penser de ces calculs ?

### Avec l'outil informatique (p.254–255) — « MEILLEUR AJUSTEMENT ET TABLEUR »

Taux de chômage (%) Japon / France 1985, 1990, 1995, 2000, 2001, 2002, 2003 (rangs 0, 5, 10, 15, 16, 17, 18) :
Japon yᵢ 2,6 ; 2,1 ; 3,1 ; 4,7 ; 5 ; 5,4 ; 5,3 ; France zᵢ 10,1 ; 8,6 ; 11,3 ; 9,3 ; 8,5 ; 8,8 ; 9,4.
**Travail sur papier** : 1) pourcentage d'évolution 1985–2003 ; 2) évolution annuelle moyenne admise 12,6 %
(Japon) et −1,19 % (France) : estimer les taux en 2004. **Tableur** : feuille A1 « Taux de chomage », plage
B2 : D9 ; « Nuages de points » ; clic-droit « Ajouter une courbe de tendance… » « Linéaire » ; « Format de la
courbe de tendance » / « Option » / « Afficher l'équation sur le graphique ». **Question** : équations des
droites de régression, ajustements affines appropriés ? **Pour aller plus loin** : a) courbe de tendance
polynomiale (ordre 2, 3, 4…) pour (xᵢ ; yᵢ) ; b) idem pour (xᵢ ; zᵢ) ; c) « Prévision Prospective /
Rétrospective » : estimation Japon 2004 puis 2007 ; d) prévision France 2004 ; e) comparer au taux réel de 9 %
en France.

### Exercices et problèmes (p.256–266) — 19 exercices

- **Ex. 1** (p.256–257, titré « VRAI-FAUX », format QCM) : nuage de 6 points (x de 1 à 6, y ≈ 9, 13, 15,
  18, 20, 21) ; G point moyen. 1) le nuage est celui de : a) {9; 13; 15; 18; 20; 21} ; b) {(1;9), (2;13),
  (3;15), (4;18), (5;20), (6;21)} ; c) {(1991;19), (1992;13), (1993;15), (1994;18), (1995;20), (1996;21)} ; 2) ordonnée de G : a) médiane des yᵢ b) moyenne des yᵢ c) demi-somme y₁ et y₆ ; 3) G : a) (3,5 ; 16)
  b) (3,5 ; 16,5) c) (3,5 ; 15) ; 4) ajustement par a) ax² + bx + c, a > 0 b) ax² + bx + c, a < 0 c) ax + b,
  a > 0 d) ax + b, a < 0 ; 5) meilleure droite : a) premier et dernier points b) droite de MAYER c) droite de
  régression de y en x ; 6) moindres carrés = minimiser a) S = Σ(yᵢ − (axᵢ + b)) b) S = Σ(yᵢ − (axᵢ + b))²
  c) S = Σ|yᵢ − (axᵢ + b)| ; 7) droite de régression : a) y = 2,4x + 7,6 b) y = 7,6x + 2,4 c) y = −2,4x + 7,6 ; 8) un ajustement affine est a) toujours possible b) toujours pertinent c) le meilleur ajustement. (Réponses
  non fournies.)
- **Ex. 2** (p.257) : (14 ; 8), (20 ; 10), (28 ; 17), (30 ; 23), (36 ; 29), (45 ; 32), (50 ; 40). 1) méthode de
  Mayer ; 2) tracer ; 3) G ; 4) G ∈ (G₁G₂).
- **Ex. 3** (p.257) : coefficient de corrélation et pertinence d'un ajustement affine : a) x 1–4, y 3, 5, 4, 5 ;
  b) x 1–4, y 6,5 ; 4 ; 2,5 ; 1 ; c) x 8,4 ; 8,5 ; 8,6 ; 8,7 ; 8,8, y 8,1 ; 8,3 ; 8,6 ; 8,9 ; 9,2 ; d) x 1–5,
  y 54, 48, 70, 60, 130.
- **Ex. 4** (p.257–258) : moyennes trimestrielles des 22 élèves de 4ᵉ sciences de l'informatique en Math /
  Info. / Philo (deux tableaux de 11 colonnes : Math 6 10 10 12 2 11 7 8 9 11 11 | 8 10 1 10 6 11 8 9 15 11 7 ;
  Info. 10 7 10 11 9 13 10 10 6 7 12 | 10 11 9 7 12 10 11 13 10 10 6 ; Philo 11 11 13 12 11 14 11 9 12 11 13 |
  12 15 15 13 13 10 11 11 11 13 11). a) r(Math, Info) ; b) r(Info, Philo), conclusion.
- **Ex. 5** (p.258) : consommation mondiale de sucre (Mt) : 1900 8,1 ; 1910 12,3 ; 1920 13 ; 1930 24,7 ;
  1940 26,7 ; 1950 29,4 ; 1960 49,3 ; 1970 70,5 ; 1980 88,6 ; 1995 116,6 ; 2000 129 ; 2001 130,7 ; 2002
  135,7 ; 2003 139,2 ; 2004 143,3. a) nuage (série chronologique) ; b) point moyen au dixième ; c) modèle
  affine ?
- **Ex. 6** (p.258) : note sur 20 selon le temps de travail hebdomadaire (min) : (5 ; 3), (60 ; 8), (180 ; 14),
  (300 ; 18) ; trouver une courbe d'ajustement compatible avec la réalité.
- **Ex. 7** (p.258–259, titré « VRAI - FAUX ») : D et D′ peuvent-elles être les deux droites de régression ?
  a) y = 12,5x + 7,2 et x = −10⁻²y + 3 ; b) y = 3x + 5 et x = (1/3)y − 5 ; c) y = 7x − 14 et x = (13/8)y ;
  d) y = 0,5x et y = 3x ; e) y = −7 et x = 5.
- **Ex. 8** (p.259) : éclosions d'œufs de grenouilles (échantillons de 200, 22ᵉ jour) selon la température
  tᵢ (°C) 6 ; 6,4 ; 6,8 ; 7,2 ; 7,6 ; 8 : xᵢ = 131, 144, 157, 170, 190, 189. 1) nuage, droite « à l'œil » ; 2) coefficient de corrélation, droite de régression de x en t, qualité ; 3) prédiction à 7,5 °C.
- **Ex. 9** (p.259) : n = 100, Σxᵢ = 800 ; Σyᵢ = 1200 ; Σxᵢ² = 7200 ; Σyᵢ² = 16000 ; Σxᵢyᵢ = 10200. 1) droite de régression de y en x ; 2) de x en y.
- **Ex. 10** (p.259–260) : allométrie d'insectes, x = log longueur de l'élytre, y = log largeur de la tête,
  50 insectes : Σxᵢ = 155 ; Σyᵢ = 125 ; Σxᵢyᵢ = 391,1 ; Σxᵢ² = 482,5 ; Σyᵢ² = 320,5 ; Σxᵢ²yᵢ² = 3468,7. 1) a) moyenne, écart-type de x ; b) de y ; c) covariance, r ; d) droite de y en x ; 2) loi d'allométrie.
- **Ex. 11** (p.260–261) : quatre nuages (a), (b), (c), (d) dessinés. 1) ajustement affine pertinent pour
  chacun ? 2) coefficient directeur d'une droite ajustant (b) ; 3) nuage ajustable par une fonction associée
  à la fonction inverse ? 4) nuage ajustable par une parabole, son équation.
- **Ex. 12** (p.261) : chiffre d'affaires (milliers de dinars) 1995–2004, rangs 0–9 : 110, 130, 154, 180, 190,
  210, 240, 245, 270, 295. 1) nuage (2 cm ; 1 cm pour 20) ; 2) pourcentage d'augmentation 1995–2004 ; 3) G ; 4) justifier l'ajustement affine, droite D des moindres carrés, G ∈ D ; 5) prévision 2010 ; 6) progression
  de 8 % par an à partir de 2004 : chiffre prévisible en 2010.
- **Ex. 13** (p.261) : 10 individus, xᵢ 18, 20, 19, 16, 19, 16, 19, 21, 15, 17 ; yᵢ 43, 110, 70, 17, 91, 29,
  80, 134, 15, 34 ; relation y = a ln x + b, z = ln x. 1) nuage (zᵢ ; yᵢ), droite de régression de y en z ; 2) prédiction pour x = 22.
- **Ex. 14** (p.262) : prix xᵢ (D/kg) 10 ; 11,5 ; 12 ; 13 ; 13,7 ; 15 ; 16,5 ; 18,8 ; 20 ; quantité yᵢ
  (centaines de tonnes) 4,7 ; 4,1 ; 4 ; 3,7 ; 3,5 ; 3,2 ; 2,9 ; 2,6 ; 2,4. 1) a) nuage, ajustement affine ?
  b) droite Δ de y en x (10⁻²), quantité pour 24,5 D ; 2) z = 100/y : a) zᵢ à 0,1 ; b) z = ax + b (a, b à
  l'unité) ; c) fonction f, vérifier f(24,5) = 2 ; 3) demande réelle 210 t à 24,5 D : ajustement le plus
  judicieux ?
- **Ex. 15** (p.262–263) : livres vendus par mois (milliers) : janvier 2002 (rang 1) 1,2 ; janvier 2003 (13)
  2,5 ; juillet 2003 (19) 3,5 ; janvier 2004 (25) 5,1 ; « Juillet 2004 » (28) 6. 1) nuage ; 2) zᵢ = ln(yᵢ) à
  10⁻³ (z = 1,253 imprimé pour le rang 19) ; 3) droite D de z en x ; 4) y = α e^(kx) ; 5) a) estimation pour
  « janvier 2205 » [sic] ; b) mois où les ventes dépassent 13 000 ; 6) nombre moyen m entre janvier 2002 et
  avril 2004 : m = (1/28)∫₀²⁸ 1,14e^(0,06) dx [sic, exposant sans x] ; valeur exacte et approchée.
- **Ex. 16** (p.263–264) : indices des prix 1990–1997 (rangs 0–7) : 100 ; 103,2 ; 105,7 ; 107,9 ; 109,7 ;
  111,6 ; 113,6 ; 115,2. 1) nuage, point moyen ; 2) droite D des moindres carrés ; 3) branche de parabole
  y = ax² + bx + c : on pose zᵢ = √(1198 − 10yᵢ), droite admise z = −x + 14 : a) vérifier
  y = −0,1x² + 2,8x + 100,2 ; b) tracer pour x ∈ [0 ; 7] ; c) prévision 1998 ; d) indice réel 116 en 1998 :
  pourcentage d'erreur.
- **Ex. 17** (p.264–265) : population (milliers) d'une ville nouvelle 1970–2000 (rangs 0, 5, …, 30) : 18, 21,
  25, 30, 36, 42, 50 (nuage imprimé). 1) a) droite des moindres carrés (au centième) ; b) estimation 2003 ; 2) a) f(x) = ae^(bx) sur [0 ; +∞[ avec f(0) = 18 « et » [condition suivante non imprimée, voir doutes] ; b au
  millième ; b) estimation 2003 ; c) tracer f ; d) population réelle 55 milliers en 2003 : ajustement le plus
  pertinent ? 3) f(x) = 18e^(0,034x) : a) valeur moyenne sur [0 ; 30] au dixième ; b) année correspondante
  (lecture graphique).
- **Ex. 18** (p.265–266) : médicament injecté, quantité qᵢ (mg) dans le sang à tᵢ (h) 0, 2, 4, 6, 8 : 9,9 ;
  7,5 ; 5,5 ; 3,9 ; 3 (nuage imprimé). 1) a) droite D de q en t (10⁻¹) ; b) estimation à 12 h, critique ; 2) a) yᵢ = ln qᵢ (au centième) ; b) droite de y en t ; c) q = ae^(−bt) ; d) variations de f(t) = 10e^(−0,15t)
  sur [0 ; 15], courbe C ; e) quantité à 12 h (10⁻¹).
- **Ex. 19** (p.266) : hypermarché de 20 caisses : caisses ouvertes X 3, 4, 5, 6, 8, 10, 12 ; attente moyenne
  Y (min) 16 ; 12 ; 9,6 ; 7,9 ; 6 ; 4,7 ; 4. 1) nuage ; 2) G ; 3) ajustement affine : a) r ; b) droite D de y
  en x ; c) caisses pour 5 min d'attente, attente avec 15 caisses, fiabilité ; 4) ajustement non affine
  f(x) = λ/x sur ]0 ; +∞[ : a) λ tel que f(3) = 16 ; b) courbe C ; c) mêmes estimations avec f.

### Maths et culture (p.267–268) — « Une brève histoire des outils statistiques »

Astronomie « mère [imprimé « mêre »] de toutes les sciences » ; Babyloniens ; Ptolémée, Aristarque de Samos,
Hipparque ; encart « La loi statistique ne s'impose pas à l'esprit humain avec le même caractère de nécessité
que les lois naturelles. Emile Borel » ; **Les valeurs typiques d'une série univariée** (mode, milieu de
l'étendue, moyenne arithmétique chez Tycho Brahé, Képler ; Roger Cotes 1722, moyenne pondérée ; médiane 1757 ;
moyennes géométrique et harmonique 1874 ; Galilée 1632 ; variance au XIXᵉ siècle, Gauss préfère l'écart-type) ;
**Ajustement, corrélation et régression** (Euler et « Johan Tobias Maver » [sic, Mayer], méthode des moyennes ;
Legendre 1805, moindres carrés, Gauss un an plus tard ; loi normale ; Galton 1888 « Partial co-relation » ;
Pearson 1896 ; Spearman 1904 ; chi-deux). Source : « Tangente J073-n° 77-Octobre -Novembre 2000. »

### Écart avec la référence (math-bac-techniques/16 « Statistiques », secondairement math-bac-sciences-exp/17)

**Référence retenue : `math-bac-techniques/16-statistiques`** (corrige la proposition du brief : sciences-exp/17
et bac-math/19 n'ont PAS le seuil |r| ≥ 0,75 — ils utilisent √3/2 — alors que bac-techniques/16 l'a, ainsi
que les deux droites D₁/D₂ avec a × a′ = r², la méthode de Mayer et les changements de variable Z = ln Y,
Z = √Y) ; `math-bac-sciences-exp/17` en appui pour les ajustements non affines réinvestissant exp/ln/intégrale.

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer)** :

- **tableau à double entrée, distributions marginales, effectifs nᵢⱼ, covariance d'un échantillon groupé**
  (techniques/16 § 1, sciences-exp/17 § 1 et § 3) : ce manuel ne traite que des séries « définies en données
  individuelles » (xᵢ ; yᵢ)₁≤ᵢ≤ₙ ;
- les éventuels exemples « calculatrice touche-à-touche » (sciences-exp/17) — ici remplacés par Excel.

**Ce que ce manuel a en plus (à ajouter)** :

- **I. Activités de rappel de statistique à une variable** (7 activités : moyenne, variance, écart-type par
  effectifs et fréquences, effet d'un changement affine sur la moyenne, médiane, quartiles, diagramme en boîte,
  intervalle et écart interquartile, % dans [X̄ − σ ; X̄ + σ], quartiles d'une série classée par interpolation
  linéaire dans une classe, moyennes d'échantillons « Random » et réduction de l'écart-type) ;
- démonstration demandée (Act. II.2) des formules cov = (1/n)Σxᵢyᵢ − X̄Ȳ, cov(aX + b ; Y) = a cov(X ; Y),
  cov(X ; X) = V(X), et de |cov| ≤ σ(X)σ(Y) à partir de cov² ≤ V(X)V(Y) (admis) ;
- construction de la droite des moindres carrés par **minimisation d'un trinôme en a** (Act. III.2 et III.3 :
  Σ(MᵢPᵢ)², b = ȳ − ax̄, a = cov/V(X)) ;
- vocabulaire **interpolation / extrapolation**, **modèle**, **variable explicative / expliquée** ;
- Mayer avec **deux partages différents** à comparer (Act. III.1) ; vérification que G ∈ (G₁G₂) (Ex. 2) ;
- ajustements non affines plus variés : **fonction puissance y = k x^α** par (ln x, ln y), **logarithmique
  y = a ln x + b** (Ex. 13), **y = λ/x** (Ex. 19), **z = 100/y** (Ex. 14), **parabolique** via √A ou
  √(1198 − 10y) (Ex. 16), prix d'équilibre offre/demande ;
- **Excel** : courbes de tendance linéaire et polynomiale, affichage de l'équation, prévision
  prospective/rétrospective (p.254–255) ;
- QCM/Vrai-Faux sur le critère des moindres carrés (S = Σ(yᵢ − (axᵢ + b))² vs Σ|…|) et sur la
  compatibilité de deux droites de régression (Ex. 7 : signes de a et a′, aa′ = r² ≤ 1) ;
- données contextualisées « sciences de l'informatique » (notes de la classe, Ex. 4 Math/Info/Philo).

**Vocabulaire / notations propres à ce manuel** : « série statistique à deux caractères » / « série double » ;
X̄, Ȳ ; σ(X), V(X) ; cov(X ; Y) (parfois « Cov ») ; r ; « droite de MAYER » ; « droite de régression de Y en
X » notée D ou Δ ; seuil **|r| ≥ 0,75** (corrélation « forte » / « faible ») ; a et a′.

### Bornes de scope (chapitre 12, section Sciences de l'informatique)

- ✅ INCLUS : rappels de statistique à une variable (X̄, V, σ, médiane, quartiles, diagramme en boîte, écart
  interquartile, quartiles par interpolation dans une classe) ; série double en données individuelles ; nuage,
  point moyen G ; covariance (définition, forme développée, symétrie, cov(aX + b ; Y), cov(X ; X) = V(X),
  cov² ≤ V(X)V(Y)) ; coefficient r, −1 ≤ r ≤ 1, invariance, seuil 0,75 ; méthode de Mayer ; moindres carrés
  (droites de régression de Y en X et de X en Y par G, a = cov/V(X), a′ = cov/V(Y), r² = aa′, même signe) ;
  interpolation/extrapolation et esprit critique des prévisions ; ajustements non affines par changement de
  variable (ln y, ln x et ln y, √y, 100/y, λ/x, a ln x + b, parabole) avec réinvestissement exp/ln et valeur
  moyenne/intégrale (Ex. 15, 17) ; tableur.
- ⛔ EXCLU (absent de ces pages) : tableau à double entrée et séries doubles groupées (nᵢⱼ), distributions
  marginales ; démonstration de cov² ≤ V(X)V(Y) (admise) ; seuil √3/2 ; inférence statistique, tests, intervalles
  de confiance ; régression multiple ; coefficient de détermination R² nommé ; corrélation de rang (seulement
  citée en « Maths et culture ») ; calculatrice touche-à-touche.

### Lecture

- **Pages lues en L1 (pdftotext -layout)** : p.235 à p.268, toutes.
- **Pages lues sur l'image (110 dpi)** : p.235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
  248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268
  = **34 pages sur 34** (100 %).
- **Écarts texte / image constatés** : sommes Σ, barres X̄/Ȳ, racines, exposants, « ≤ », « ≥ », « |r| »,
  « σ » dégradés partout en L1 (p.236 formules de V éclatées ; p.240–242 cov² ≤ V(X)V(Y) et |r| ≥ 0,75
  illisibles ; p.247 équations des droites de régression désalignées) ; signes « − » perdus (p.248
  « x = 0,43y » pour x = −0,43y ; p.249 « y = 0,43x » pour y = −0,43x ; p.259 « x = 10² y » pour
  x = −10⁻²y ; p.252 z = 0,0234x « 0,508 » ; p.264 z = « x + 14 » pour −x + 14 et y = « 0,1x² » pour
  −0,1x² ; p.265 q = ae^(bt) / 10e^(0,15t) pour les exposants négatifs) ; p.242 et p.260 les nuages dessinés
  absents du texte ; p.254–255 captures Excel (boutons « Nuages de points », « Ajouter une courbe de
  tendance… », « Linéaire », « Prévision ») absentes du texte ; p.263 l'intégrale de l'Ex. 15 illisible en L1.
- **Coquilles [sic]** : « digramme » (p.236) ; « Q₁ et Q₂ » pour Q₁ et Q₃ (p.236) ; « (xᵢ) 1 ≤ i ≤ j » et
  « G de coordonnées (Ȳ ; X̄) » (p.239) ; « Nuage de point– » (p.238) ; « quelque soit » (p.240) ; en-têtes
  « Chapitre 13 … caractéres » (p.241, 247) et « caractéres » (p.251–253) ; « cœfficient corrélation »
  (p.247) ; « Activités 3 » (p.246) ; « Le point du nuage (3) sont » (p.243) ; « Part en % yi : 2.3 » pour tᵢ
  (p.243) ; « méthodes des moindres carrés », « caractéres X » (p.248) ; « Le tableau suivant donne
  représente » (p.261) ; « janvier 2205 » et « 1,14e^(0,06) dx » (p.263) ; « répartie » (p.237) ;
  « mêre », « surlesdécouvertes », « intérét » (p.267) ; « Maver »,
  « mëthode », « réversion », « régres-sion » (p.268).
- **Doutes signalés** : (1) « droite de MAYER (1814-1878) » (p.245) : dates imprimées telles quelles (la
  méthode est attribuée en p.268 à « Johan Tobias Maver ») — ne pas reprendre les dates sans vérification ;
  (2) Act. III.3 4) a) « 8 f(a) = a²V(X) − 2aCov(X,Y) + V(Y) » : avec f(a) = Σ(MᵢPᵢ)² sur 8 points, l'identité
  attendue est f(a) = 8[a²V(X) − 2a cov + V(Y)] ; reproduit tel quel ; (3) p.248 : la consigne « Calculer
  les coordonnées du point moyen. » est placée derrière la case « 3 », alors qu'elle complète vraisemblablement
  l'Appl. 2 (droite de X en Y + valeurs de X) ; l'Appl. 3 serait alors l'espérance de vie — à trancher ;
  (4) Ex. 15 : « Juillet 2004 » au rang 28 alors que la question 6 parle d'avril 2004 (rang 28 = avril 2004) ;
  (5) Ex. 17 2) a) : la seconde condition après « f(0) = 18 et » n'est pas imprimée (saut de page) [?] ;
  (6) Ajustement exponentiel p.250 : 951,3 pour 1995 (valeur isolée très au-dessus des autres) — reproduit tel
  quel ; (7) Ex. 1 est titré « VRAI-FAUX » mais présente des choix a)/b)/c) ; (8) Ex. 10 : « Σxᵢ²yᵢ² = 3468,7 »
  imprimé (donnée non utilisée par les questions).

## 2.13 Chapitre 13 — Probabilités (manuel 222472, p.269–302)

**Page de garde (p.269)** — « Chapitre 13 », titre « PROBABILITÉS ». Plan imprimé : « I . Espaces probabilisés
finis - Probabilité. · II . Probabilités conditionnelles · III . Variables aléatoires · IV . Schéma de
Bernoulli · V . Exemples de variables aléatoires continues ». Portrait légendé « Bernoulli Jean ». Pas de
citation. ⚠️ Le plan imprimé ne correspond pas aux titres du cours : le cours a **six** parties (une partie
« IV. Paramètres d'une variable aléatoire » non annoncée ; Bernoulli devient V, les lois continues VI).

**Plan du chapitre (titres du cours)** : **I. Espaces probabilisés finis - Probabilités** (p.270–272 :
« Activités préliminaires » Act. 1–4 ; « A retenir » p.271–272 ; « Applications » 1–3 p.272) ·
**II. Probabilités conditionnelles** (p.273–278 : « Activités de découverte » Act. 1–5 ; « A retenir » p.276 ;
« Exemple » résolu (Bayes) p.277 ; « Applications » 1–3 p.277–278) · **III. Variables aléatoires**
(p.278–281 : Act. 1–3 ; « A retenir » p.280 ; « Applications » 1–2 p.281) · **IV. Paramètres d'une variable
aléatoire** (p.281–284 : « Activités préliminaires » Act. 1–4 ; « A retenir » p.283–284 ; « Applications »
1–2 p.284) · **V. Schéma de Bernoulli - Loi binomiale** (p.285–288 : « Activité » unique ; « A retenir »
p.286 ; « Exemple » résolu p.287 ; « Application » p.288) · **VI. Exemples de variables aléatoires continues**
(p.288–293 : « Activités préliminaires » (classement discret/continu) ; « Activités de découverte » Act. 1–4 ;
« A retenir » p.291–292 ; « Exemple 1 » et « Exemple 2 » résolus p.292–293 ; « Applications » 1–3 p.293).
Puis **Apprendre à chercher** (p.294 : Situations 1–2), **Avec l'outil informatique** (p.295–296 : programme
Pascal « LoiContinues »), **Exercices et problèmes** (p.297–301 : 27 exercices), **Maths et culture** (p.302).
Pas de QCM/Vrai-Faux, pas de « Tout ce qu'on doit savoir ». En-têtes de p.280 et p.291 : « Chapitre 14 :
Probabilité » [sic].

### Cours — Activités (une ligne chacune)

**I. Espaces probabilisés finis — Activités préliminaires**

- **Act. 1** (p.270) : étagère : 5 livres de mathématiques, 4 de physique, 6 romans ; deux de chaque sorte
  édités en Tunisie, les autres à l'étranger ; on tire un livre. a) nombre d'issues ; b) E « livre de
  mathématiques » : card et probabilité (• univers) ; c) p(F), F « édité en Tunisie » ; d) G « mathématiques
  édité en Tunisie » en fonction de E et F, p(G) ; e) H « roman », E ∩ H (• incompatibles) ; f) K « édité à
  l'étranger » en fonction de F, p(K) ; g) L « roman édité en Tunisie » en fonction de F et H, p(L).
- **Act. 2** (p.270) : bonbonnière 8 caramel, 12 menthe ; 1) équiprobabilité : p(menthe) ; 2) p(caramel) = 2 ×
  p(menthe) : p(menthe).
- **Act. 3** (p.270–271) : urne 5 blanches, 3 rouges ; 1) p(blanche) ; 2) deux tirages avec remise : a) arbre
  de choix ; b) E « deux blanches », F « 2ᵉ blanche », G « au plus une blanche » ; 3) sans remise : a) arbre ;
  b) p(E), p(F), p(G).
- **Act. 4** (p.271) : électroménager, usines U₁, U₂, U₃ (30 %, 25 %, 45 %), défectueux 10 %, 15 %, 4 % ;
  D « défectueux », F « fonctionne ». 1) compléter l'arbre (0.3 ; 0.1 / 0.9 imprimés) ; 2) p(U₁ ∩ D),
  p(U₂ ∩ D), p(U₃ ∩ D), p(D) ; 3) p(F) de deux manières.

**II. Probabilités conditionnelles — Activités de découverte**

- **Act. 1** (p.273) : tableau adhésion à un club (garçons 14 adhérents / 10 non, total 24 ; filles 8 / 4, total
  12 ; totaux 22 / 14 / 36). 1) a) garçons adhérents ; b) filles non adhérentes ; 2) G « garçon », A
  « adhérent » : p(A), p(Ā), p(G), p(Ḡ) ; 3) un garçon : p(adhérent), p(non adhérent) ; 4) un non-adhérent :
  a) p(garçon), p(fille) ; • **probabilité conditionnelle de A sachant G**, notée p(A/G) ou p_G(A) ; b) p(A/G) ; 5) a) p(Ā/G), p(G/Ā), p(Ḡ/A) ; b) p(Ā ∩ G), p(G ∩ A), p(Ḡ ∩ A), comparer p(Ā/G) et p(Ā ∩ G)/p(G), p(G/A) et
  p(G ∩ A)/p(A), p(Ḡ/A) et p(Ḡ ∩ A)/p(A).
- **Act. 2** (p.273–274) : arbres probabilistes (schéma 1 : Ω → G (2/3), Ḡ (1/3) ; G → A (7/12), Ā (5/12) ;
  p(G ∩ A) = 14/36, p(G ∩ Ā) = 10/36, p(Ḡ ∩ A) = 2/9, p(Ḡ ∩ Ā) = 1/9 ; schéma 2 : Ω → A, Ā → G, Ḡ) ;
  7/12 = p(A/G) ; a) compléter le schéma 1 ; b) remplir le schéma 2 ; c) sommes égales à 1, nœud = somme des
  branches issues.
- **Act. 3** (p.274) : machines A (40 %) et B (60 %), défectueuses 15 % et 8 % ; E « produite par A », D
  « défectueuse ». a) compléter l'arbre Ω → E, Ē → D, D̄ ; b) p(D), p(D̄) ; c) arbre inversé Ω → D, D̄ → E, Ē ;
  d) p(E/D), p(Ē/D̄), p(E/D̄).
- **Act. 4** (p.274–275) : 1) A ≠ ∅, Ā ≠ ∅ ; a) (diagramme) p(E) = p(E ∩ A) + p(E ∩ Ā) ; b) p(E) =
  p(E/A).p(A) + p(E/Ā).p(Ā) ; 2) A₁ … Aₙ partition de Ω (Aₖ ≠ ∅, Aᵢ ∩ Aⱼ = ∅ pour i ≠ j, A₁ ∪ … ∪ Aₙ = Ω) :
  a) p(E) = Σ p(E/Aᵢ).p(Aᵢ) — « formule **des probabilités totales** » ; b) p(E/Aₖ)p(Aₖ) = p(Aₖ/E)p(E), en
  déduire p(Aₖ/E) = p(E/Aₖ).p(Aₖ)/(p(E/A₁).p(A₁) + … + p(E/Aₙ).p(Aₙ)) — « **formule de Bayes** ».
- **Act. 5** (p.275) : A) autre tableau (garçons 15 / 5 / 20 ; filles 12 / 4 / 16 ; total 27 / 9 / 36) :
  a) comparer proportions d'adhérents chez garçons et filles ; b) comparer p(A), p(A/G), p(A/Ḡ) puis p(G),
  p(G/A), p(G/Ā) ; c) comparer p(A ∩ G) et p(A).p(G) ; ➢ G et A **indépendants** ; B) Act. 1 : A et G
  indépendants ?

**III. Variables aléatoires — Activités de découverte**

- **Act. 1** (p.278–279) : dé : gain 2 D pour 6, 1 D pour 2 ou 4, −1 D pour un impair ; a) tableau issue/gain
  (« -1 » imprimé pour 1) ; X : Ω → ℝ, • **variable aléatoire** ; b) p(E₁), p(E₂), p(E₃) ; • p(X = 2) ;
  tableau gain xᵢ (−1, 1, 2) / p(X = xᵢ) ; **loi de probabilité** P_X ; c) P_X(−1), P_X(1), P_X(2) et leur
  somme.
- **Act. 2** (p.279) : voitures par ménage 0, 1, 2, 3 : 40 %, 35 %, 20 %, 5 %. 1) a) X(Ω), loi ; b) p(au plus
  2), p(au moins 2) ; • notations p(X ≤ 2), p(X ≥ 2) ; c) p(X > 1), p(X ≤ 1), somme = 1, « Peut-on prévoir le résultat ? » ; d) sachant au moins
  une voiture, p(2 voitures).
- **Act. 3** (p.279–280) : reprise de l'Act. 1 ; a) p(X ≤ −1), p(X ≤ 1), p(X ≤ 2) ; b) p(X ≤ x) selon x ≤ −1 ;
  −1 < x ≤ 1 ; 1 < x ≤ 2 ; x > 2 ; F(x) = P(X ≤ x) : F = 0 sur ]−∞, −1[ ; 1/2 sur [−1, 1[ ; 5/6 sur [1, 2[ ;
  1 sur [2, +∞[ (graphe en escalier) ; F **fonction de répartition** ; c) p(1 < X ≤ 2) = F(2) − F(1) et
  p(−0,6 < X ≤ 1,3) = F(1,3) − F(−0,6) ; d) à partir de ]−∞, b] = ]−∞, a] ∪ ]a, b], p(a < X ≤ b) = F(b) − F(a).

**IV. Paramètres d'une variable aléatoire — Activités préliminaires**

- **Act. 1** (p.281) : même jeu (gains −1, 1, −1, 1, −1, 2) ; a) moyenne E des gains, jeu favorable ?
  b) E = (−1)p(X = −1) + 1 p(X = 1) + 2 p(X = 2) ; • **espérance mathématique** E(X) = Σ_{ω∈Ω} X(ω)p({ω}) =
  Σ xᵢ p(X = xᵢ) ; c) espérance pour les voitures par ménage, interpréter.
- **Act. 2** (p.281–282) : 1) Y = X − 1, Z = 3X : a) loi de Y, E(Y) = E(X) − 1 ; b) loi de Z, E(Z) = 3E(X) ; 2) Y donnée par ω 1–6 ↦ −3, 1, 2, 1, −2, 2 ; Z = X + Y : a) loi de Z ; b) E(Z) = E(X) + E(Y).
- **Act. 3** (p.282–283) : réclamations quotidiennes, supermarché A : 0–5 avec 0,10 ; 0,20 ; 0,30 ; 0,20 ;
  0,10 ; 0,10 ; supermarché B : 0,01 ; 0,25 ; 0,35 ; 0,25 ; 0,10 ; 0,04. a) E(X) = E(Y) = 2,3 ; • variance
  V(X) = Σ(xᵢ − E(X))²p(X = xᵢ), σ(X) = √V(X) ; • **variance**, **écart-type** ; b) V(X), V(Y), comparer, « Interpréter le résultat. » ; 2) [numérotation « 2) » après a) b)] a) lois de X² et Y² ; b) E(X²), E(Y²) ; c) V = E(X²) − (E(X))².
- **Act. 4** (p.283) : 1) Y = X + a : a) valeurs ; b) p(Y = xᵢ + a) = p(X = xᵢ) ; c) V(X + a) = V(X),
  σ(X + a) = σ(X) ; 2) a ≠ 0, Z = aX : a) valeurs ; b) p(Z = axᵢ) = p(X = xᵢ) ; c) V(aX) = a²V(X),
  σ(aX) = |a|σ(X).

**V. Schéma de Bernoulli - Loi binomiale — Activité de découverte (unique)**

- **Activité** (p.285–286) : plants de roses, probabilité de germer 4/5. 1) 2 plants : p(X = 0), p(X = 1),
  p(X = 2) (arbre, plants p₁, p₂) ; 2) 5 plants : épreuve élémentaire, succès S / échec E = S̄ ; • **épreuve de
  Bernoulli** ; issue S S E S S de probabilité (4/5)⁴ × (1/5) ; a) nombre d'issues à 4 succès ; b) issue
  E S S E E, sa probabilité, nombre d'issues à 2 succès = C₅² ; c) issue à 3 succès, C₅³ issues ; d) loi de X
  (nombre de plants ayant germé) ; e) E(X), V(X), vérifier E(X) = 5p(S) et V(X) = 5p(S)p(S̄) ; • « **loi
  binominale** [sic] **de paramètres** 5 et 4/5 ».

**VI. Exemples de variables aléatoires continues**

- **Activité préliminaire** (p.288) : variables discrètes / continues ; lesquelles sont continues : a) temps
  d'un coureur sur 800 m ; b) température d'une personne en bonne santé ; c) nombre d'absents ; d) poids d'un
  nouveau-né ; e) montant de la facture d'électricité ; f) nombre de repas servis.
- **Act. 1** (p.288) : loi discrète X : 0–5 avec 0,03 ; 0,07 ; 0,30 ; 0,40 ; 0,15 ; 0,05 ; a) p(X ≤ 2),
  p(X ≥ 3) ; b) p(1 < X ≤ 4), p(1 ≤ X ≤ 4). « Pour une variable aléatoire continue il n'est pas possible de
  représenter sa loi de probabilité par un tableau analogue à celui d'une loi discrète. »
- **Act. 2** (p.289) : courbe C_f (histogramme lissé des moyennes générales d'un lycée, classes d'amplitude
  0,1), X ∈ [4, 17] ; • f **densité de probabilité** ; aire hachurée = p(x₁ ≤ X ≤ x₂) ; loi P([x₁, x₂]) ;
  a) p(x₁ ≤ X ≤ x₂) = ∫_{x₁}^{x₂} f(t)dt ; b) ∫₄¹⁷ f(t)dt ; c) F(x) = ∫₄ˣ f(t)dt est la fonction de
  répartition ; d) p(x₁ ≤ X ≤ x₂) = F(x₂) − F(x₁).
- **Act. 3** (p.289–290) : train prévu à 0h10mn, arrivée entre 0h00mn et 0h40mn équiprobable ; **la loi P est
  uniforme** sur [0, 40], densité constante (rectangle de hauteur 1/40). 1) aire du rectangle, hauteur ; 2) p(arrivée entre 0h15mn et 0h20mn) ; b) avant l'heure ; c) après 0h20mn ; 3) F(x) pour x ≤ 0, 0 < x ≤ 40,
  x > 40.
- **Act. 4** (p.290) : intervalle entre deux arrivées de clients à un guichet, densité f(x) = λe^(−λx) (λ > 0) ;
  • **loi exponentielle de paramètre λ** ; courbe pour λ = 0,1. 1) p(durée < 2 min), p(> 2 min),
  p(entre 2 et 3 min) ; 2) F(x) = 1 − e^(−0,1x).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Texte de cours I** (p.270) — « • L'ensemble de toutes les issues possibles est appelé **univers**. » ;
> « • On dit que E et H sont **incompatibles.** »

> **A retenir — Définition** (p.271) — « Soit Ω l'ensemble des issues d'une expérience aléatoire et 𝒫(Ω)
> l'ensemble des parties de Ω. On appelle probabilité sur Ω toute application p de 𝒫(Ω) dans [0,1] telle
> que : • p( Ω ) = 1 • Pour tous A et B de 𝒫( Ω ) tels que A ∩ B = ∅ on a : p (A ∪ B) = p (A) + p (B). Le
> triplet (Ω , 𝒫(Ω), p) s'appelle espace probabilisé fini. »

> **Vocabulaire** (p.271–272) — « • L'ensemble Ω est appelé univers. • Toute partie de Ω est appelée
> événement. Un singleton est appelé évènement élémentaire. • La partie Ω est appelée évènement certain.
> • L'ensemble vide est appelé évènement impossible. • A et B étant deux évènements. - A ∩ B est appelé
> évènement A et B. A ∪ B est appelé évènement A ou B. - Si A ∩ B = ∅ , on dit que A et B sont incompatibles.
> A et B sont deux évènements contraires si: A ∪ B = Ω et A ∩ B = ∅ . On note : B = Ā ou A = B̄ . • Deux
> évènements A et B sont dits équiprobables si p(A) = p(B). »

> **Propriétés** (p.272) — « Soit (Ω , 𝒫 (Ω), p) un espace probabilisé fini : •Lorsque les évènements
> élémentaires sont tous équiprobables, la probabilité d'un évènement A est p(A) = card(A)/card(Ω) = nombre de
> cas favorables / nombre de cas possibles •A et B étant deux évènements -p(A ∪ B) = p(A) + p(B) - p(A ∩ B).
>
> - p(A ∪ B) = p(A) + p(B) si A et B sont incompatibles. - p(Ā) = 1 - p(A) »

> **Texte de cours II** (p.273) — « • La probabilité pour que parmi les garçons on obtienne un élève adhérent à
> un club s'appelle **probabilité conditionnelle** de l'événement **A sachant G.** Elle est notée **p(A/G)**
> ou bien **p_G(A)** » ; (p.275) « L'égalité précédente s'appelle formule **des probabilités totales.** » ;
> « La dernière formule est appelée **formule de Bayes**. Elle sert à calculer une probabilité conditionnelle
> connaissant des probabilités conditionnelles «inverses». » ; « ➢ On dit que les évènements G et A sont
> **indépendants.** »

> **A retenir — Définition** (p.276) — « Dans un espace probabilisé fini (Ω, 𝒫(Ω), p) , on donne deux
> évènements A et B tels que p(B) ≠ 0 . On appelle « probabilité conditionnelle de A sachant B» le réel noté
> p(A/B) ou bien p_B(A) et défini par : p (A/B) = p(A ∩ B)/p(B) »

> **Conséquence** (p.276) — « si p(A) ≠ 0 alors p (A ∩ B) = p (A).p (B/A) ; si p(B) ≠ 0 alors
> p (A ∩ B) = p (B). p (A/B) »

> **Formule des probabilités totales** (p.276) — « A₁ , A₂ …. Aₙ étant des évènements formant une partition de
> l'univers Ω et E étant un évènement de probabilité non nulle, on a : p(E) = p(E/A₁).p(A₁)+p(E/A₂).p(A₂)+…..
> +p(E/Aₙ).p(Aₙ) En particulier si A est un évènement tel que p(A) ≠ 0 et p(Ā) ≠ 0 alors
> p(E) = p(E/A).p (A) + p(E/Ā).p (Ā). »

> **Formule de Bayes** (p.276) — « A₁ , A₂ …. Aₙ étant des évènements formant une partition de l'univers et E
> étant un évènement de probabilité non nulle, pour tout k ∈ {1, 2, 3, ….., n} on a
> p(Aₖ/E) = p(E/Aₖ).p(Aₖ) / Σᵢ₌₁ⁿ p(E/Aᵢ).p(Aᵢ) »

> **Evènements indépendants** (p.276) — « Deux évènements A et B sont dits indépendants si la réalisation de
> l'évènement A ne dépend pas de la réalisation de l'évènement B c'est à dire: p(A/B) = p(A) , p(B/A) = p(B)
> ou encore p(A ∩ B) = p(A).p(B) »

> **A retenir — Définition - Vocabulaire - Notation.** (p.280) — « • (Ω , 𝒫 (Ω), p) , étant espace probabilisé
> fini , on appelle variable aléatoire définie sur Ω toute application de Ω dans ℝ . • X(Ω) = {x₁, x₂, …….,
> xₙ} étant l'ensemble des valeurs que prend la variable X, on note p(X = xᵢ) la probabilité pour que X prenne
> la valeur xᵢ. • L'application de X(Ω) = {x₁, x₂, ……., xₙ} vers [0,1] notée P_X ,qui à tout xᵢ associe
> p(X = xᵢ) est appelée loi de probabilité de X. P_X(xᵢ) = p(X = xᵢ) • La probabilité pour que X prenne une
> valeur strictement inférieure à un réel a est notée p(X < a) et la probabilité pour que X prenne une valeur
> supérieure ou égale à un réel a est notée p(X ≥ a). • On appelle fonction de répartition de la variable
> aléatoire X la fonction F définie sur ℝ par : F(x) = p(X ≤ x). »

> **Propriétés** (p.280) — « X étant une variable aléatoire et a étant un réel, • Si X(Ω) = {x₁, x₂, …….,
> xₙ} avec x₁< x₂< …….< xₙ alors Σᵢ₌₁ⁿ p(X = xᵢ) = 1 • p(X ≤ a) + p(X > a) = 1 • La fonction de répartition
> de X est constante sur chacun des intervalles ]-∞, x₁[, ….[xᵢ, xᵢ₊₁[,……, [xₙ, +∞ [ • Pour tous réels a et
> b tels que a ≤ b on a : p(a< X ≤ b) = F(b) - F(a) »

> **A retenir — Définition** (p.283) — « Soit (Ω ,𝒫 ( Ω ), p) un espace probabilisé fini et X une variable
> aléatoire définie sur Ω . L'espérance mathématique de X est le réel noté E(X) tel que
> E(X) = Σ_{ω∈Ω} X(ω) p({ω}) Si X(Ω) = {x₁, x₂, ……., xₙ} alors E(X) = Σᵢ₌₁ⁿ xᵢp(X= xᵢ) . »

> **Propriétés** (p.283) — « X et Y étant des variables aléatoires définies sur Ω et a un réel.
> E(X+a) =E(X) + a E (aX) = aE(X) E(X+Y) = E(X) + E(Y) »

> **Définition** (p.283–284) — « Soit (Ω,𝒫(Ω), p) un espace probabilisé fini et X une variable aléatoire
> définie sur Ω et telle que X(Ω) = {x₁, x₂, ……., xₙ}. • La variance de X notée V(X) est le réel
> V(X) = Σᵢ₌₁ⁿ (xᵢ - E(X))² p(X= xᵢ) • L'écart type de X noté σ(X) est le réel σ (X)=√V(X) »

> **Propriétés** (p.284) — « X étant une variable aléatoire définie sur Ω et a un réel V(X) = E(X²) - (E(X))²
> V(X + a) = V(X) σ(X+a)=σ(X) V (aX) = a²V(X) σ(aX)=|a|σ(X) »

> **A retenir — Définition et vocabulaire** (p.286) — « • On appelle schéma de Bernoulli, une suite
> d'expériences identiques telles que : - Chaque expérience ne donne lieu qu'à deux issues : l'une, notée S,
> appelée succès, l'autre E = S̄ appelée échec. - Les expériences sont indépendantes les unes des autres .
> • Les paramètres d'un schéma de Bernoulli sont le nombre d'expériences n et la probabilité p de succès d'une
> expérience élémentaire. • La loi de probabilité de X qui a chaque issue de n expériences associe le nombre de
> succès s'appelle loi binomiale de paramètres n et p. »

> **Théorème (admis)** (p.286) — « Etant donné une loi binominale X de paramètres n et p on a :
> • p(X=k) = Cₙᵏpᵏ(1 – p)ⁿ⁻ᵏ avec k ∈{0,1,2......n} • L'espérance et la variance de X sont E(X)=np et
> V(X)=np(1-p) »

> **Texte de cours VI** (p.288) — « • Les variables aléatoires qu'on a étudiées précédemment sont définies sur
> un ensemble fini et prennent un nombre fini de valeurs. Ce sont des variables aléatoires discrètes.
> •Cependant certaines variables aléatoires peuvent prendre n'importe quelle valeur dans un intervalle donné.
> On les appelle **variables aléatoires continues.** »

> **A retenir — Définition :** (p.291) — « • Une variable aléatoire continue est une variable aléatoire X qui
> peut prendre n'importe quelle valeur dans un intervalle donné. On s'intéresse alors à des évènements du
> type : « La valeur de X est comprise entre x₁ et x₂ où x₁ et x₂ sont deux réels donnés ». • X étant une
> variable aléatoire prenant des valeurs dans [a,b] , - On appelle densité de probabilité de X la fonction f
> positive et continue sur [a,b] telle que : ∫ₐᵇ f(t)dt = 1 et pour tous x₁ et x₂ de l'intervalle [a,b]
> p(x₁ ≤ X ≤ x₂) = ∫_{x₁}^{x₂} f(t)dt - La loi de probabilité P de X est l'application qui, à tout
> sous-intervalle [x₁, x₂] de [a,b] associe la quantité P([x₁, x₂]) = p(x₁ ≤ X ≤ x₂) » (figure : courbe
> en cloche C_f, aire hachurée entre x₁ et x₂).

> **Définition** (p.291) — « On appelle loi uniforme sur [a,b] la loi de probabilité dont la densité f est la
> fonction constante égale à 1/(b − a) sur [a,b]. »

> **Conséquences** (p.291) — « • x₁et x₂ étant deux réels de l'intervalle [a,b] et X une variable aléatoire
> qui suit une loi uniforme sur [a,b] on a : P([x₁, x₂]) = p(x₁ ≤ X ≤ x₂) = (x₂ − x₁)/(b − a) • La fonction
> de répartition de X est définie sur ℝ par F(x) = 0 si x<a ; (x − a)/(b − a) si a≤x<b ; 1 si x ≥ b »
> (figures : rectangle de hauteur 1/(b − a) avec P(x₁ ≤ X ≤ x₂) ; graphe de F, rampe de a à b).

> **Définition** (p.292) — « Soit λ un réel strictement positif. On appelle loi exponentielle de paramètre λ la
> loi de probabilité dont la densité f est la fonction définie sur [0;+∞[ par f(x)=λ e^(-λx) »

> **Conséquences** (p.292) — « • Si X est une variable aléatoire qui suit une loi exponentielle de paramètre
> λ alors, pour tous réels positifs a et b tels que a ≤ b : P([a,b]) = p(a ≤ X ≤ b) = e^(-λa)-e^(-λb) • On a
> p(X ≥ a) = e^(-λa) • La fonction de répartition de X est définie sur ℝ par : F(x) = 1- e^(-λx) si x ≥ 0 ;
> 0 si x < 0 » (la figure placée à côté reproduit le graphe de F de la loi UNIFORME, rampe de a à b [sic,
> figure non adaptée]).

### Exemples résolus (rubrique « Exemple » du cours) — 4

- **Exemple (Bayes)** (p.277) : terminales : 50 % scientifique, 30 % économique, 20 % lettres ; choisissent
  l'informatique : 3/4 des scientifiques, la moitié des économistes (« économiquee » [sic]), 1/4 des
  littéraires ; un élève a choisi l'informatique : p(scientifique) ? **Solution** : E, A₁, A₂, A₃ ;
  p(A₁) = 50/100, p(A₂) = 30/100, p(A₃) = 20/100 ; p(E/A₁) = 3/4, p(E/A₂) = 1/2, p(E/A₃) = 1/4 ; Bayes :
  p(A₁/E) = (3/4 · 50/100)/(3/4 · 50/100 + 1/2 · 30/100 + 1/4 · 20/100) ; « p(A₁/E) = 15/23 ≈ 0,65 ».
- **Exemple (binomiale)** (p.287) : tireur, p = 7/10, 4 tirs ; a) toucher 3 fois ; b) « toucher au plus 2
  fois » ; c) paie 1 D par tir, gagne 2 D par cible touchée : jeu favorable ? **Solution** : schéma de
  Bernoulli n = 4, p = 7/10 ; a) p₃ = C₄³(7/10)³.3/10 = 4·1029/10⁴ = 4116/10000 = 0,4116 ; b) [la solution
  traite « au moins 2 fois », voir doutes] E « au moins 2 fois », F « moins de 2 fois » contraires ;
  p(F₀) = C₄⁰(7/10)⁰(3/10)⁴ = 3⁴/10⁴ = 0,0081 ; p(F₁) = C₄¹(7/10)¹(3/10)³ = 4·7/10·3³/10³ = 0,0756 ;
  p(F) = 0,0837 ; p(E) = 1 − 0,0837 = 0,9163 ; c) X gain, X₁ nombre de touches, X(Ω) = {0, 2, 4, 6, 8},
  X₁(Ω) = {0, 1, 2, 3, 4}, X = 2X₁ ; loi de X : (3/10)⁴ ; 4·(7/10)·(3/10)³ ; 6·(7/10)²·(3/10)² ;
  4·(7/10)³·(3/10) ; (7/10)⁴ ; E(X) = E(2X₁) = 2E(X₁) = 2·4·7/10 = 5,6 ; « Puisqu'il a payé 4 dinars pour 4
  tirs, le jeu lui est favorable. »
- **Exemple 1 (uniforme)** (p.292–293) : épaisseur (cm) de pièces, loi uniforme sur [2 ; 2,8] ; 1) P(X ≤ 2,6),
  P(2,3 ≤ X ≤ 2,5) ; 2) acceptée si épaisseur > 2,4 ; 3) sachant épaisseur > 2,2, p(acceptée). **Solution** : 1) (2,6 − 2)/(2,8 − 2) = 0,6/0,8 = 0,75 ; (2,5 − 2,3)/(2,8 − 2) = 0,2/0,8 = 0,25 ; 2) P(X ≥ 2,4) =
     0,4/0,8 = 0,5 ; 3) A « acceptée », B « > 2,2 » ; P(A/B) = P(A ∩ B)/P(B) ; « On a A B = A » [∩ manquant] donc
     P(A/B) = P(A)/P(B) ; P(B) = (2,8 − 2,2)/(2,8 − 2) = 0,75 ; P(A/B) = 0,5/0,75 = 2/3.
- **Exemple 2 (exponentielle)** (p.293) : durée de consultation, loi exponentielle de paramètre 0,1 ;
  a) proportion > 15 min ; b) p(entre 5 et 10 min). **Solution** : a) P(X ≥ 15) = e^(−0,1.15) = e^(−1,5) ≈
  0,22, « 22% » ; b) P(5 ≤ X ≤ 10) = e^(−0,1.5) − e^(−0,1.10) = e^(−0,5) − e^(−1) ≈ 0,23.

### Applications (fin de chaque partie du cours) — 14

- **I. Appl. 1** (p.272) : boîte : 3 jetons blancs (1, 2, 3), 4 rouges (1–4), 5 verts (1–5) ; tirage simultané
  de 3 jetons ; p(E) « tous blancs », F « même couleur », G « un seul porte le 1 », H « un et un seul vert »,
  I « numéros impairs », J « somme égale à 5 », K « deux rouges et un seul jeton porte le 4 ».
- **I. Appl. 2** (p.272) : code de serrure à 3 chiffres parmi 0–9 ; 1) au hasard : a) obtenir le code ;
  b) même chiffre des unités ; 2) code formé des chiffres 1, 3, 6 : a) obtenir le code ; b) même chiffre des
  unités, des dizaines ou des centaines.
- **I. Appl. 3** (p.272) : urne 5 blancs, 3 rouges, deux tirages sans remise ; E « blanc au 1ᵉʳ », F « rouge au
  2ᵉ » ; 1) arbre ; 2) p(E), p(Ē), p(E ∩ F), p(Ē ∩ F), en déduire p(F).
- **II. Appl. 1** (p.277) : urne 5 blancs, 3 rouges ; si blanc on remet, si rouge on ne remet pas, puis 2ᵉ
  tirage ; A « blanc au 1ᵉʳ », B « un jeton blanc et un jeton noir » [sic, rouge], C « blanc au 2ᵉ » ; 1) p(B/A), p(B/C) ; 2) p(C/A), p(C/Ā), en déduire p(C) ; arbre de probabilité.
- **II. Appl. 2** (p.278) : défauts D₁ (8 %), D₂ (15 %), les deux (5 %) ; a) p(un seul défaut) ; b) p(D₂
  sachant D₁).
- **II. Appl. 3** (p.278) : tennis : 1ᵉʳ service réussi 2/3 ; si échec, 2ᵉ réussi 4/5 ; 1) p(double faute) ; 2) p(mise en jeu réussie).
- **III. Appl. 1** (p.281) : deux dés, X somme ; a) Ω, X(Ω) ; b) loi ; c) p(X < 4), p(X ≤ 4), p(X > 4),
  p(X ≤ 5), p(3 < X ≤ 7), p(2,5 < X ≤ 9,12).
- **III. Appl. 2** (p.281) : reprendre l'Act. 2 (voitures) : fonction de répartition et courbe.
- **IV. Appl. 1** (p.284) : loterie de 100 billets : 10 gagnent 10 D, 2 gagnent 100 D ; gain espéré.
- **IV. Appl. 2** (p.284) : accidents par an (0–4) : 0,60 ; 0,25 ; 0,12 ; 0,02 ; 0,01 ; cinq ans plus tard :
  0,65 ; 0,15 ; 0,12 ; 0,05 ; 0,03 ; a) E(X), E(Y) ; b) V(X), V(Y) ; c) σ(X), σ(Y), interpréter.
- **V. Application** (p.288) : a) 15 machines garanties un an, p(panne) = 0,1 ; gagnante si au plus 5 pannes :
  probabilité ; b) X nombre de pannes : p(X = 0), p(X = 10), E(X).
- **VI. Appl. 1** (p.293) : métro toutes les 6 min, attente X uniforme sur [0 ; 6] ; a) p(entre 3 et 5 min) ;
  b) F et sa représentation.
- **VI. Appl. 2** (p.293) : durée de vie d'une voiture, loi exponentielle de paramètre 0,05 ; a) p(> 10 ans),
  p(> 20 ans) ; b) âgée de 10 ans : p(dépasse 15 ans) ; c) comparer avec p(dépasse 5 ans) ; d) F et courbe.
- **VI. Appl. 3** (p.293) : recherche d'erreur dans un programme, densité f(x) = 0,02e^(−0,02x) ; a) courbe de
  f ; b) p(durée > 1 h) ; c) p(durée < un quart d'heure).

### Apprendre à chercher (p.294)

- **Situation 1** : urne de n boules numérotées 1 à n, tirages avec remise jusqu'à la première répétition d'un
  numéro ; 1) n = 3 : loi du nombre X de tirages ; 2) n quelconque : a) p(X > 2), p(X > 3) ; b) pour
  k ∈ {2, …, n}, p(X > k) = Aₙᵏ/nᵏ⁺¹ [sic ? voir doutes] ; loi de X.
- **Situation 2** : demi-cercle C de centre O, rayon 1 (figure A, O, B, M, angle θ = BOM) ; M choisi selon une
  loi uniforme sur C ; a) θ suit une loi uniforme ; b) aire A du triangle ABM ; c) A ≥ 0,5 ⇔ θ ∈ [π/6, 5π/6] ;
  probabilité de A ≥ 0,5.

### Avec l'outil informatique (p.295–296)

« Ce programme calcule la probabilité d'une loi uniforme ou d'une loi exponentielle entre a et b » —
programme Turbo Pascal `program LoiContinues; uses wincrt;` (variables `choix:integer; a,b,lambda:real`) ;
procédures `affiche(Proba:real)` (affiche « Loi exponentielle » + lambda ou « Loi uniforme », puis a, b et
`p[a,b]`), `LoiUniforme` (lit a < b, **`p:=1/(b-a);`**), `LoiExronontielle` [sic] (lit a < b et lambda,
`p:=exp(-lambda*a)-exp(-lambda*b);`), `Saisie` (choix 1 : loi uniforme, 2 : loi exponentielle) ; programme
principal `saisie;`.

### Exercices et problèmes (p.297–301) — 27 exercices

- **Ex. 1** (p.297) : urne de 10 boules : « cinq blanches numérotées 1,1,2,3 » [sic, 4 numéros pour 5 boules],
  trois noires 1, 1, 2, deux rouges 1, 3. 1) tirage simultané de 3 : A « somme égale à 5 », B « 2 blanches et
  1 noire » ; 2) successif sans remise : C « une seule rouge », D « dans l'ordre 1, 2, 3 » ; 3) avec remise :
  E « au moins une rouge », F « trois couleurs différentes ».
- **Ex. 2** (p.297) : dé truqué, p₁ = p₃ = p₅ = α, p₂ = p₄ = p₆ = 2α (α ∈ ℝ*₊) ; 1) α (rappel
  Σ_{ω∈Ω} p({ω}) = 1) ; 2) p(face paire).
- **Ex. 3** (p.297) : équipe de football : victoire 0,6, défaite 0,3, nul 0,1 ; trois matches ; 1) arbre ; 2) A « gagne au moins deux fois et ne perd pas », P(A) ; 3) B « gagne et fait un match nul », P(B).
- **Ex. 4** (p.297) : 1) 12 leçons étudiées sur 24, tirage simultané de 2 questions (fractions irréductibles) :
  a) aucune connue ; b) les deux ; c) une et une seule ; d) au moins une ; 2) n leçons étudiées (n ≤ 24) :
  a) Pₙ (au moins une) ; b) n tels que Pₙ ≥ 0,95.
- **Ex. 5** (p.297) : 60 personnes : le quart porte des lunettes, 40 % fument, 5 fument et portent des
  lunettes ; arbre avec L et F.
- **Ex. 6** (p.297) : dé régulier : p(pair et > 4) ; p(pair sachant > 4) ; p(> 4 sachant pair).
- **Ex. 7** (p.298) : urne : 4 jetons blancs (1, 1, 2, 2), 5 noirs (1, 1, 2, 2, 2) ; tirage simultané de 2 ;
  A « deux noirs », B « deux portant le 1 » ; p(A/B), p(Ā/B), p(A/B̄).
- **Ex. 8** (p.298) : microprocesseurs : 4 % défectueux ; la vérification détecte 95 % des défectueux et
  déclare défectueux 2 % des bons ; M « défectueux », R « rejeté » ; 1) p(M), p(R/M), p(R/M̄) ; 2) p(M et R),
  p(M̄ et R) ; 3) p(défectueux et déclaré bon) ; 4) p(bon sachant rejeté).
- **Ex. 9** (p.298) : 1250 athlètes, test antidopage (« n'est pas sur à 100% » [sic]) : sains 1188 négatifs /
  12 positifs ; dopés 1 / 49 ; 1) p(S) « sain », p(T) « test positif » ; 2) un sain : p(test positif) ; 3) arbre.
- **Ex. 10** (p.298) : dépistage : malade → test positif 96 % ; non malade → test négatif 94 % ; une personne
  sur 65 malade ; a) arbre ; b) test positif : p(malade).
- **Ex. 11** (p.298–299) : p(A) = 3/5, p(B) = 7/10, p(A ∪ B) = 9/10 ; 1) p(Ā) ; 2) p(A ∩ B), indépendance ? 3) p(A/B), p(Ā/B), p(B/Ā).
- **Ex. 12** (p.299) : population active : 45 % d'hommes ; chômage 5 % des femmes, 4 % des hommes ; F « femme »,
  C « chômage » ; 1) p(F), p(F̄), p(C/F), p(C/F̄) ; 2) p(C) ; 3) sachant au chômage : a) femme ; b) homme.
- **Ex. 13** (p.299) : urne 8 blanches, 4 noires ; 1) 3 simultanément : même couleur ; 2) 3 successivement
  avec remise, X nombre de noires : a) loi ; b) E(X), V(X), σ(X).
- **Ex. 14** (p.299) : deux dés, X somme ; 1) loi ; 2) mise 10 D, gain 50 D si X > 9, sinon perte : jeu
  équitable, favorable, défavorable ?
- **Ex. 15** (p.299) : QCM de 4 questions indépendantes, 3 réponses dont une correcte, au hasard ; 1) X nombre
  de bonnes réponses (loi, espérance, écart-type) ; 2) score Z (+2 par bonne, −1 par mauvaise).
- **Ex. 16** (p.299) : mauvaise réaction à un vaccin 0,01 ; 1) famille de 5 : a) chez 2 membres ; b) chez moins
  de 2 ; 2) famille de 7, X nombre de réactions : a) loi ; b) E(X), V(X).
- **Ex. 17** (p.299–300) : appareil : 6 blanches, 3 rouges, 3 boules tombent ; 3 rouges → 100 D ; 2 rouges →
  15 D ; 1 rouge → lot de 5 D ; jeton à 8 D ; 1) X somme gagnée : a) loi ; b) espérance ; c) gain moyen du
  forain ; 2) jeton à 9 D ou une boule blanche de plus : solution la plus rentable ?
- **Ex. 18** (p.300) : boîte : blanches 1, 1, 2 ; rouges 2, 2 ; 1) deux tirages sans remise, X produit des
  numéros : loi ; S = (X = 2), vérifier P(S) = 3/5 ; 2) épreuve répétée 4 fois avec remise, Y nombre de
  réalisations de S : a) loi ; b) E(Y), V(Y).
- **Ex. 19** (p.300) : durée de trajet uniforme sur [0 ; 1] (heure) ; p(entre 15 et 20 min).
- **Ex. 20** (p.300) : métro toutes les 6 min, T ∈ [0, 6] ; 1) p(attente entre 3 et 5 min) ; 2) p(plus de
  5 min). [Variante de VI. Appl. 1 : la loi uniforme n'y est pas nommée.]
- **Ex. 21** (p.300) : OAB rectangle isocèle de côté 1 (figure), M au hasard sur [AB] (loi uniforme sur
  [0, 1]), variable OM ; a) 1 ≤ OM ≤ √2 ; b) p(OM ≤ a), a ∈ [1, √2].
- **Ex. 22** (p.300) : temps de réponse d'un terminal, loi exponentielle de paramètre 0,3 ; 1) p(entre 3 et
  8 s) ; 2) p(> 8 s).
- **Ex. 23** (p.300–301) : M au hasard sur [AB], A d'abscisse 2, B d'abscisse 4 ; 1) p(x ∈ [2, 3]) ; 2) p(M milieu de [AB]).
- **Ex. 24** (p.301) : M au hasard sur [AB] (4 cm), triangles équilatéraux sur [AM] au-dessus et [MB]
  au-dessous (figure) ; 1) p(même aire) ; 2) p(somme des aires ≥ 4√3).
- **Ex. 25** (p.301) : durée d'une conversation téléphonique, loi exponentielle de paramètre 1/10 ;
  a) p(attendre plus de 10 min) ; b) p(entre 10 et 20 min).
- **Ex. 26** (p.301) : attente à un guichet, loi exponentielle de paramètre λ, moyenne 8 min ; 1) attente
  moyenne = limite en +∞ de ∫₀ᴬ λxe^(−λx)dx ; montrer ∫₀ᴬ λxe^(−λx)dx = (−λAe^(−λA) − e^(−λA) + 1)/λ ; en
  déduire λ = 0,125 ; 2) p(attente ≤ 5 min) ; 3) p(attente ∈ [10 ; 20[) ; 4) sachant 15 min d'attente déjà,
  p(moins de 45 min au total).
- **Ex. 27** (p.301) : durée de vie d'une lampe, loi exponentielle de paramètre 1/5 ; 1) P([0,4]), P([4,6]),
  P([3, +∞[) ; 2) fonction de survie S(x) = P(X > x) ; 3) vie moyenne 5 ans : p(survie au-delà) ; 4) âgée de
  10 ans : p(durer encore au moins 5 ans).

### Maths et culture (p.302)

Cardan (1501-1576) « le joueur savant » ; problème des partis ; Pascal, chevalier de Méré (1654), Fermat ;
Huygens, _Tractatus de ratiociniis in aleae ludo_ (1657) ; stabilisation des fréquences ; Jacques Bernoulli,
_Ars Conjectandi_ (« qui ne sera publié qu'après sa mort en 1713 par son neveu Daniel » — tel quel, voir
doutes) ; Laplace, _Théorie analytique des probabilités_ (1812) : « La probabilité est une fraction dont le
numérateur est le nombre de cas favorables, et dont le dénominateur est le nombre de tous les cas possibles. » ;
de Moivre, Gauss, Poisson, Tchebychev, Markov, Kolmogorov.

### Écart avec la référence (math-bac-techniques/14 + 15, secondairement math-bac-sciences-exp/15 + 16)

**Référence retenue : `math-bac-techniques/14-probabilite` + `math-bac-techniques/15-variables-aleatoires`**
(corrige la proposition du brief sciences-exp/15 + 16 : sciences-exp/15 n'enseigne pas la **formule de Bayes**
et sciences-exp/16 ne pose pas de **densité générale** — alors que ce manuel les a, comme techniques/14 (§
« Formule de Bayes ») et techniques/15 (§ « Variable continue, fonction de répartition et densité »)).
sciences-exp/15 + 16 restent utilisables pour la binomiale, l'uniforme et l'exponentielle.

**Ce que la référence enseigne et que ce manuel n'a PAS (à retirer)** :

- le **dénombrement comme notion de cours** (p-uplets, arrangements, combinaisons, « dénombrer les tirages
  avec remise / sans remise / simultané » : techniques/14 § 3, sciences-exp/15 § 1–2) : ce manuel n'a aucune
  partie de dénombrement ; Cₙᵏ et Aₙᵏ y sont **utilisés comme acquis** (Act. V, Situation 1, exercices de
  tirages) ;
- **E(X) = 1/λ, V(X) = 1/λ²** et l'**absence de mémoire** énoncées en cours (techniques/15) : absentes des
  encadrés ; la moyenne 1/λ n'apparaît que via l'Ex. 26 (limite d'intégrale, λ = 0,125 pour 8 min) et
  l'absence de mémoire seulement dans des questions (VI. Appl. 2 b–c, Ex. 26 4, Ex. 27 4) ;
- les **suites de probabilités / chaînes** (sciences-exp/15 § « Les suites de probabilités qui se
  répètent ») ;
- l'espérance/variance des lois uniforme et exponentielle continues.

**Ce que ce manuel a en plus (ou autrement)** :

- définition **axiomatique** de la probabilité (application de 𝒫(Ω) dans [0,1], additivité sur des
  incompatibles) et le mot « espace probabilisé fini » (Ω, 𝒫(Ω), p) ;
- partie « **Paramètres d'une variable aléatoire** » avec E(X + a), E(aX), **E(X + Y) = E(X) + E(Y)**,
  V(X + a) = V(X), V(aX) = a²V(X), σ(aX) = |a|σ(X), V = E(X²) − E(X)² (activités de démonstration) ;
- **densité de probabilité générale** sur [a,b] (∫ₐᵇ f = 1, p(x₁ ≤ X ≤ x₂) = ∫ f, F(x) = ∫ₐˣ f) et
  classement discret / continu ;
- problèmes géométriques de probabilité continue (Situation 2 : demi-cercle, aire ≥ 0,5 ; Ex. 21 : OM ;
  Ex. 23–24 : point sur un segment, triangles équilatéraux) ;
- **fonction de survie** S(x) = P(X > x) (Ex. 27) ; calcul de ∫₀ᴬ λxe^(−λx)dx par parties (Ex. 26) ;
- Situation 1 (temps de première répétition, p(X > k) = Aₙᵏ/nᵏ⁺¹) ;
- **programme Turbo Pascal** (loi uniforme / exponentielle entre a et b) — spécifique à la section
  Sciences de l'informatique ;
- contextes « informatique » (Bayes sur l'option informatique, microprocesseurs, terminal d'ordinateur,
  recherche d'erreur dans un programme).

**Vocabulaire / notations propres à ce manuel** : p(A/B) ou p_B(A) (barre oblique) ; « arbre de choix » /
« arbre probabiliste » ; P_X loi de X ; « aléa numérique » (Ex. 13, 18) ; « loi binominale » [sic] ; Cₙᵏ ;
Aₙᵏ ; P([a,b]) ; « espace probabilisé fini » ; « épreuve de Bernoulli », succès S, échec E = S̄.

### Bornes de scope (chapitre 13, section Sciences de l'informatique)

- ✅ INCLUS : univers, événements, opérations, incompatibles, contraires, équiprobabilité ; probabilité sur un
  ensemble fini (définition axiomatique), p(A ∪ B), p(Ā) ; arbres de choix / pondérés ; probabilité
  conditionnelle, p(A ∩ B) = p(A)p(B/A), probabilités totales, **Bayes** ; indépendance de deux événements ;
  variable aléatoire discrète, loi, fonction de répartition (escalier, p(a < X ≤ b) = F(b) − F(a)) ; espérance,
  variance, écart-type et leurs propriétés (y compris E(X + Y)) ; schéma de Bernoulli, loi binomiale (admise),
  E = np, V = np(1 − p) ; variables continues, densité, loi uniforme sur [a,b], loi exponentielle (densité,
  P([a,b]), p(X ≥ a), F) ; probabilités conditionnelles avec lois continues ; jeux équitables / favorables ;
  usage de Cₙᵏ et Aₙᵏ dans les exercices ; intégration (par parties, Ex. 26) au service des lois continues.
- ⛔ EXCLU (absent de ces pages) : cours de dénombrement ; indépendance de plus de deux événements ou de
  variables aléatoires (hors schéma de Bernoulli) ; covariance de variables aléatoires ; loi normale (citée
  seulement au ch.12), loi de Poisson, loi géométrique nommée ; E(X) et V(X) des lois continues comme résultats
  de cours ; absence de mémoire comme propriété énoncée ; loi des grands nombres (seulement culturelle p.302) ;
  chaînes de Markov.

### Lecture

- **Pages lues en L1 (pdftotext -layout)** : p.269 à p.302, toutes.
- **Pages lues sur l'image (110 dpi)** : p.269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281,
  282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302
  = **34 pages sur 34** (100 %).
- **Écarts texte / image constatés** : la couche texte de ce chapitre **remplace les symboles par des
  caractères ASCII** : « # » pour Ω, « " » pour ∩, « % » pour ∪, « $ » pour ∅, « & » pour ω, « ! » pour λ,
  « P ( # ) » pour 𝒫(Ω) ; barres de complémentaire (Ā, Ḡ, D̄, S̄) perdues partout (p.272–275, 277, 297–299) ;
  « ≠ », « ∈ », « ≤ » souvent perdus (p.274–276, 286, 288–289) ; arbres (p.271, 273, 274), graphe en escalier
  de F (p.280), courbes C_f / rectangle / exponentielle (p.289–291) et figures géométriques (p.294, 300, 301)
  absents du texte ; p.286 « C₅² », « Cₙᵏ » rendus « C52 », « Ckn » ; exposants négatifs des exponentielles
  perdus (p.290–293, 301). **Toute formule vient de l'image.**
- **Coquilles [sic]** : plan de la page de garde (I–V) ≠ titres du cours (I–VI) ; « Probabilités » / « Probabilité »
  (p.269 vs 270) ; en-têtes « Chapitre 14 : Probabilité » (p.280, 291) ; « y'a-t-il », « à l'aide F » (p.270) ;
  « B : … un jeton blanc et un jeton noir » dans une urne blanc/rouge (p.277) ; « économiquee » (p.277) ;
  numérotation « 2) » après a) b) dans IV Act. 3 (p.283) ; « loi binominale » (p.286, deux fois) ; « qui a
  chaque issue » (p.286) ; « fonction du répartition » (p.290) ; « On a A B = A » (p.293, ∩ manquant) ;
  figure de F uniforme placée à côté de la définition de la loi exponentielle (p.292) ; « LoiExronontielle »
  (p.295–296) ; « cinq blanches numérotées 1,1,2,3 » (p.297) ; « probabilié », « élèments », « matches »
  (p.297) ; « n'est pas sur à 100% », « hopitaux » (p.298) ; « Déterminez les entiers n tels Pn » (p.297) ;
  « qu'elle soient », « boule noires » (p.299) ; « fois ou S est réalisé » (p.300) ; « variablealéatoire »,
  « entre de 10 mn et 20 mn », « soient supérieure où égale », « paramètre 1/5) », « probabilié » (p.301).
- **Doutes signalés** : (1) Exemple binomial p.287 : la question b) demande « au plus 2 fois » mais la solution
  calcule « au moins 2 fois » (0,9163) — à ne pas reprendre tel quel ; (2) programme Pascal p.295 :
  `LoiUniforme` calcule `p:=1/(b-a)` (la densité, pas une probabilité entre a et b, et sans bornes de
  l'intervalle de la loi) — erreur de fond du manuel ; (3) Situation 1 p.294 : p(X > k) = Aₙᵏ/nᵏ⁺¹ imprimé
  (avec k tirages sans répétition on attendrait Aₙᵏ/nᵏ) — reproduit tel quel ; (4) Ex. 1 p.297 : 5 boules
  blanches pour 4 numéros (1, 1, 2, 3) [?] ; (5) p.302 « publié … par son neveu Daniel » : reproduit tel quel ;
  (6) Ex. 24 : la figure montre deux triangles non équilatéraux (croquis) ; (7) le plan imprimé p.269 omet la
  partie « Paramètres d'une variable aléatoire » ; à l'adaptation, suivre les titres du cours (I–VI).
