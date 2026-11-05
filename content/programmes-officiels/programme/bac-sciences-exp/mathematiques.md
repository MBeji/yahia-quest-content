<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Sources : manuels élève officiels CNP 222433P00 (tome 1, 182 p.) et 222434P00 (tome 2, 119 p.),
     mathématiques, 4ème année Sciences expérimentales. Aucun guide enseignant au corpus pour ce
     couple ⇒ le manuel élève fait référence. Lu le 2026-11-05 depuis le Drive `cnp-officiel` : les
     PDF n'ont pas de couche texte ⇒ OCR (tesseract, fra, 150 dpi) page par page, puis vérification
     sur l'image de chaque page à formules, encadrés compris ; page PDF = page imprimée (offset 0).
     Fiche DIFFÉRENTIELLE : même collection CNP que la section Mathématiques (222445/222446, fiche
     `programme/bac-math/mathematiques.md`), en version allégée ; chaque section note l'écart avec
     le chapitre de référence (bac-math ou bac-techniques) dont le contenu généré est adapté
     (décision de Mohamed du 2026-11-05). -->

# Mathématiques — Bac Sciences expérimentales (`bac-sciences-exp`) · manuels officiels CNP

> **Sources (Drive `cnp-officiel`, `manuels/secondaire/c4/eleve/`)** :
>
> - **Manuel élève, tome 1** : code **222433P00** (182 p.) — analyse, chapitres 1 à 10.
> - **Manuel élève, tome 2** : code **222434P00** (119 p.) — complexes, géométrie dans l'espace,
>   probabilités et statistiques, chapitres 11 à 17.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
>   Le programme officiel ministériel n'est pas intégré au corpus (R-3) : le manuel prime.
> - **Langue d'enseignement** : **fr**. **subject id** : `math-bac-sciences-exp` · **gradeSlug** :
>   `bac-sciences-exp`.
> - **Notation** : chiffres occidentaux 0-9, équations LTR ; l'OCR dégrade les formules (racines,
>   exposants, ≤/≥, ℝ, ∈, vecteurs, barres) : elles sont rétablies sur l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Sciences expérimentales. Les deux tomes appartiennent à la même
collection CNP que ceux de la section Mathématiques (mêmes pages de garde, mêmes citations
liminaires, même découpage : activités, encadrés de cours, QCM – Vrai-Faux, exercices et problèmes),
dans une version allégée : moins de chapitres (pas d'arithmétique, d'isométries ni de similitudes,
pas de coniques), des chapitres plus courts, et un chapitre « Études de fonctions » à part entière (comme en
section Sciences techniques). Chaque section ci-dessous donne le plan du chapitre, ses
activités et exercices en une ligne, ses encadrés verbatim (vérifiés sur l'image), l'**écart avec la
référence** (ce que le manuel retire ⛔ et ce qu'il ajoute), les bornes de scope ✅/⛔ et la note de
lecture (sondage image).

## 2. Plan annuel (carte des chapitres = sommaires des deux tomes)

> Statut de transcription par chapitre — `generation` = transcrit à profondeur de génération
> (chaque activité et exercice décrit, encadrés verbatim). La couverture de pages réelle vit dans
> `suivi/bac-sciences-exp.json`. Colonne « référence » : chapitre déjà généré qui a été adapté.

| #   | Chapitre | manuel | pages (PDF = imprimées) | référence adaptée | profondeur |
| --- | -------- | ------ | ----------------------- | ----------------- | ---------- |
| 1 | Continuité et limites | 222433 | 5–22 | `math-bac-math/01` | `generation` |
| 2 | Suites réelles | 222433 | 23–38 | `math-bac-math/02` | `generation` |
| 3 | Dérivabilité | 222433 | 39–53 | `math-bac-math/03` | `generation` |
| 4 | Fonctions réciproques | 222433 | 54–66 | `math-bac-math/04` | `generation` |
| 5 | Études de fonctions | 222433 | 67–84 | `math-bac-techniques/04` | `generation` |
| 6 | Primitives | 222433 | 85–98 | `math-bac-math/05` | `generation` |
| 7 | Intégrales | 222433 | 99–122 | `math-bac-math/06` | `generation` |
| 8 | Fonction logarithme népérien | 222433 | 123–141 | `math-bac-math/07` | `generation` |
| 9 | Fonction exponentielle | 222433 | 142–164 | `math-bac-math/08` | `generation` |
| 10 | Équations différentielles | 222433 | 165–182 | `math-bac-math/09` | `generation` |
| 11 | Nombres complexes | 222434 | 5–21 | `math-bac-math/10` | `generation` |
| 12 | Équations à coefficients complexes | 222434 | 22–33 | `math-bac-techniques/11` | `generation` |
| 13 | Produit scalaire — produit vectoriel dans l'espace | 222434 | 34–47 | `math-bac-techniques/13` | `generation` |
| 14 | Équations de droites, de plans et de sphères | 222434 | 48–62 | `math-bac-techniques/12` | `generation` |
| 15 | Probabilités sur un ensemble fini | 222434 | 63–81 | `math-bac-math/18` | `generation` |
| 16 | Variables aléatoires | 222434 | 82–96 | `math-bac-techniques/15` | `generation` |
| 17 | Statistiques | 222434 | 97–119 | `math-bac-math/19` | `generation` |

## 2.1 Chapitre 1 — Continuité et limites (manuel 222433, p.5–22)

**Page de garde (p.5)** — Titre : « Continuité et limites », Chapitre 1. Citation liminaire :
« C'est l'élaboration d'une démonstration précise du théorème des valeurs intermédiaires, qui amena
Bolzano (1817) à définir la notion de continuité d'une fonction. Le théorème des valeurs
intermédiaires, qui semble géométriquement évident, a été utilisé sans scrupules par Euler et Gauss.
Bolzano, cependant estime qu'une démonstration précise est nécessaire pour atteindre une plus grande
rigueur en Analyse. » — « (E.Haier et al, L'analyse au fil de l'histoire, 2000). » (coquille source
pour Hairer, imprimée « E.Haier » comme dans la référence.)

**Plan du chapitre (p.6–17, bandeau « Cours »)** : **I. Rappels** (I.1 Continuité et limite en un
réel ; I.2 Continuité sur un intervalle ; I.3 Opérations sur les limites) · **II. Continuité et
limite d'une fonction composée** (II.1 Composée de deux fonctions ; II.2 Continuité d'une fonction
composée ; II.3 Limite d'une fonction composée) · **III. Limites et ordre** · **IV. Image d'un
intervalle par une fonction continue** (IV.1 Théorème des valeurs intermédiaires ; IV.2 Image d'un
intervalle fermé borné par une fonction continue) · **V. Image d'un intervalle par une fonction
strictement monotone**. Puis **QCM – VRAI-FAUX** (p.18) et **Exercices et problèmes** (p.19–22 :
26 exercices + 1 « Application »). Pas de rubrique « problème résolu » ni de sommaire de chapitre.
Numérotation des activités continue DANS chaque partie principale (I : 1–7 ; II : 1–6 ; III : 1–3 ;
IV : 1–8 ; V : 1), à la différence de la référence (qui renumérote par sous-partie).

### Cours — Activités (une ligne chacune)

**I. Rappels** (p.6) — « Dans ce paragraphe nous rappelons les principaux théorèmes vus en
troisième année. »

- **Act. 1** (p.6) : ensemble de définition de f et justification de la continuité en tout réel de
  cet ensemble, pour f : x ↦ 1 − x + x² ; x ↦ |−5x + 1|/(x² + 4) ; x ↦ x − 1/(x − 1) ;
  x ↦ 1/((x + 1)(x + 2)) ; x ↦ (x + 1)/(x² + 2x + 3). (Encadré rose latéral : voir plus bas.)
- **Act. 2** (p.6) : f : x ↦ (2x² − 4x + 2)/|x − 1| ; 1. vérifier que pour x ≠ 1, f(x) = 2|x − 1| ;
  2. en déduire lim_{x→1} f(x).
- **Act. 3** (p.7) : f définie sur ℝ* par f(x) = x + sin 2x/x ; montrer que f est prolongeable par
  continuité en 0 et déterminer son prolongement. (Encadré rose : lim_{x→0} sin x/x = 1.)
- **Act. 4** (p.7) : f(x) = 2x − 1 si x ≤ 1 ; x/2 + 1/(2x) si x > 1. 1. calculer lim_{x→1⁻} f(x) et
  lim_{x→1⁺} f(x) ; 2. f est-elle continue en 1 ? (Encadré rose latéral : caractérisation par limites
  à gauche/droite.)
- **Act. 5** (p.7) : f : x ↦ |x + 1|/(x + 1) ; f admet-elle une limite en −1 ?
- **Act. 6** (p.7, I.2) : f définie sur [0, π] par f(x) = sin 3x / x si x ∈ ]0, π] ; 3 si x = 0 ;
  montrer que f est continue sur [0, π]. (Encadré rose latéral : continuité sur un intervalle.)
- **Act. 7** (p.8, I.3) : déterminer 1. lim_{x→−∞} 2x + 1/(x² + 1) ; 2. lim_{x→−∞} √(−5x + 1) − 3x ;
  3. lim_{x→+∞} (−x² − x)² + √2·x ; 4. lim_{x→2} 1/|x − 2|³ − 1/|x − 2| ;
  5. lim_{x→3} 3/(x − 3)² − 2 ; 6. lim_{x→1} (x³ − 3x² + 2x)/(x² − 1) ; 7. lim_{x→+∞} √x − x.

**II. Continuité et limite d'une fonction composée**

- **Act. 1** (p.9, II.1) : figure : courbes C_f et C_g de f (sur ℝ) et g (sur ℝ₊). 1. lire les images
  par f de −1, 0, 1, 2, 3 et par g de 0, 1, 2, 3 ; 2. h : x ↦ g(f(x)) et k : x ↦ f(g(x)) ;
  a. images par h de −1, 0, 1, 2, 3 ; b. images par k de 0, 1, 2, 3.
- **Act. 2** (p.9) : déterminer deux fonctions u et v telles que f = v∘u, pour 1. f : x ↦ cos(πx + 1) ;
  2. f : x ↦ (1 + cos x)/(2 + cos x) ; 3. f : x ↦ sin((x + x⁴)/(x² + 1)).
- **Act. 3** (p.9, II.2) : étudier la continuité de f sur ℝ : 1. f : x ↦ sin(x² + π/4) ;
  2. f : x ↦ cos(sin x).
- **Act. 4** (p.10, II.3) : limite de f(x) quand x → a : 1. f : x ↦ tan(x²/4), a = √π ;
  2. f : x ↦ (cos x² − 1)/x², a = 0 ; 3. f : x ↦ sin(π/(x − 1)), a = 2.
- **Act. 5** (p.10) : figure : courbe d'une fonction f définie sur ℝ ; déterminer
  lim_{x→2} f(2/x), lim_{x→4} f((x − 4)/x), lim_{x→0} f(sin x − 1).
- **Exercice résolu 1** (p.10) : f : x ↦ cos(1/x²) − 1/x² ; lim_{x→+∞} f(x) ? Solution : v : x ↦ cos x − x,
  u : x ↦ 1/x², f = v∘u ; lim_{x→+∞} 1/x² = 0 et lim_{x→0} cos x − x = 1, donc lim_{x→+∞} f(x) = 1.
- **Act. 6** (p.10) : déterminer lim_{x→1⁺} tan(π/(2x)) et lim_{x→+∞} (x/(x − 1))·sin(πx/(2x − 1)).

**III. Limites et ordre**

- **Act. 1** (p.10–11) : f(x) = x² sin(1/x) + 1, g(x) = −x² + 1, h(x) = x² + 1. 1. montrer que pour
  tout x ≠ 0, g(x) ≤ f(x) ≤ h(x) ; 2. figure (trois courbes) : a. identifier la courbe de chaque
  fonction ; b. conjecturer la limite de f(x) quand x → 0.
- **Act. 2** (p.11) : figure : f(x) = √(−x) + cos x et g(x) = √(−x) − 1. 1. position relative de C_f
  et C_g ; 2. conjecturer la limite de f(x) quand x → −∞.
- **Exercice résolu 2** (p.11) : f : x ↦ (cos²x + 1)/x ; lim_{+∞} f et lim_{−∞} f. Méthode : 0 ≤ cos²x ≤ 1
  ⇒ 1 ≤ cos²x + 1 ≤ 2 ⇒ 1/x ≤ f(x) ≤ 2/x (x > 0) et 2/x ≤ f(x) ≤ 1/x (x < 0) ; lim 1/x = lim 2/x = 0 ;
  donc lim_{+∞} f = 0 ; « on montre de même » lim_{−∞} f = 0.
- **Act. 3** (p.12) : f : x ↦ 1/x² + sin²(1/x). 1. montrer f(x) ≥ 1/x², x ∈ ℝ* ; 2. étudier la limite de
  f en 0.

**IV. Image d'un intervalle par une fonction continue**

- **Act. 1** (p.12, IV.1) : trois courbes ; déterminer graphiquement f(I) pour I = ]−1, 3[ , I = [1, 4]
  (droite repère à y = 5/2 sur le graphique), I = ]0, 2].
- **Act. 2** (p.12) : courbe de g définie sur [−6, +∞[ ; déterminer g([−6, 4]) et g([−3, 5]).
- **Act. 3** (p.13) : montrer que les fonctions sont strictement monotones sur I : x ↦ x², I = ℝ₊ ;
  x ↦ (x + 2)/(x + 1), I = ]−1, +∞[ ; x ↦ (1 + x)²⁰, I = [0, 4]. (Encadré rose : définitions de stricte
  croissance/décroissance/monotonie.)
- **Act. 4** (p.13) : courbe de f : x ↦ 2x − cos x. 1. justifier la continuité de f sur ℝ ;
  2. a. montrer que f est strictement croissante sur [0, π/2] ; b. montrer que f(x) = π/6 admet une
  solution unique α dans [0, π/2] ; 3. a. lequel de ]0, π/4[ et ]π/4, π/2[ contient α ; b. encadrement
  de α d'amplitude π/8.
- **Act. 5** (p.13–14) : courbe de f : x ↦ x³ + x − 1. **I.** 1. ensemble de définition ; 2. continuité sur
  ℝ ; 3. f(x) = 0 admet une unique solution α dans [0, 1] ; 4. **méthode de dichotomie** (« division à
  chaque fois de l'intervalle contenant α en deux intervalles de même amplitude ») : a. calculer f(1/2),
  en déduire α ∈ [1/2, 1] ; b. calculer f(3/4), en déduire α ∈ [1/2, 3/4] ; c. poursuivre jusqu'à une
  amplitude 10⁻¹ ; d. amplitude 10⁻². **II. Avec l'ordinateur** (tableur Excel, feuille imprimée
  a, b, (a+b)/2, f(a), f(b), f((a+b)/2) ; A2 = 0, B2 = 1 ; C2 `=(A2+B2)/2` ; D2 `=PUISSANCE(A2;3)+A2-1`
  recopié en E2 et F2 ; A3 `=SI(F2*E2>0;A2;C2)` ; B3 `=SI(F2*E2>0;C2;B2)`) : encadrement de α d'amplitude 10⁻³
  (le tableau imprimé affiche jusqu'à ≈ 0,68212891 ≤ α ≤ 0,68237305).
- **Act. 6** (p.15) : 1. montrer que pour x ≠ 1, 1 + x + x² + x³ + x⁴ = (x⁵ − 1)/(x − 1) ; 2. en déduire
  que f : x ↦ 1 + x + x² + x³ + x⁴ garde un signe constant sur ℝ.
- **Act. 7** (p.15, IV.2) : courbe de f définie sur [−5, 4]. 1. déterminer f([−5, 4]) ; 2. a. minimum m et
  maximum M de f sur [−5, 4] ; b. résoudre graphiquement f(x) = m et f(x) = M.
- **Exercice résolu 3** (p.15) : f(x) = x³/3 + x sur ℝ ; f([0.6, 1]) et f([−1, −0.6]). Méthode : 0.6 ≤ x ≤ 1
  ⇒ 0.216 ≤ x³ ≤ 1 ⇒ 0.672 ≤ f(x) ≤ 4/3 ; f(0.6) = 0.672, f(1) = 4/3 ⇒ f([0.6, 1]) = [0.672, 4/3] ;
  f impaire ⇒ f([−1, −0.6]) = [−4/3, −0.672]. (Décimaux à point, comme imprimé.)
- **Act. 8** (p.16) : f(x) = sin²x sur ℝ ; 1. minimum et maximum de f sur [−π/6, π/6] ; 2. en déduire
  f([−π/6, π/6]).

**V. Image d'un intervalle par une fonction strictement monotone**

- **Act. 1** (p.16) : f définie et croissante sur ℝ₊ telle que f(n) = n + 1 pour tout entier naturel n.
  1. a ≥ 0 : montrer f(E(a)) ≥ a (E(a) partie entière) ; 2. étudier la limite de f en +∞.
- **Exercice résolu 4** (p.17) : image de I par f : 1. x ↦ x² − 2x, I = ]−∞, 0] → [0, +∞[ (strictement
  décroissante, lim_{−∞} f = +∞) ; 2. x ↦ 1/x², I = [1, +∞[ → ]0, 1] (décroissante, lim_{+∞} f = 0) ;
  3. x ↦ sin x, I = ]0, π/2[ → ]0, 1[ (croissante, lim_0 f = 0, lim_{π/2} f = 1).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Encadrés roses latéraux de la p.6** — « • Toute fonction polynôme est continue en tout réel.
> • Toute fonction rationnelle est continue en tout réel de son ensemble de définition. • Les
> fonctions x ↦ cos x et x ↦ sin x sont continues en tout réel. »

> **Théorème** (p.6) — « Soit f et g deux fonctions définies sur un intervalle ouvert I et a un réel
> de I. • Si f et g sont continues en a, alors les fonctions f + g et f × g sont continues en a.
> • Si f est continue en a, alors les fonctions αf (α ∈ ℝ), |f| et fⁿ (n ∈ ℕ*) sont continues en a.
> • Si f est continue en a et f(a) ≠ 0, alors les fonctions 1/f et 1/fⁿ (n ∈ ℕ*) sont continues en a.
> • Si f et g sont continues en a et g(a) ≠ 0, alors la fonction f/g est continue en a.
> • Si f est positive sur I et f est continue en a, alors la fonction √f est continue en a. »

> **Théorème** (p.6) — « Soit f une fonction définie sur un intervalle ouvert I, sauf peut-être en un
> réel a de I. S'il existe une fonction g définie sur I, continue en a et telle que g(x) = f(x) pour
> tout x ≠ a, alors lim_{x→a} f(x) = g(a). »

> **Encadré rose** (p.7) — « lim_{x→0} (sin x)/x = 1 »

> **Théorème** (p.7) — « Soit f une fonction définie sur un intervalle ouvert I, sauf en un réel a de
> I. Si la fonction f admet une limite finie ℓ lorsque x tend vers a, alors la fonction g définie sur
> I par g(x) = f(x) si x ≠ a ; g(x) = ℓ si x = a, est continue en a. »

> **Encadré rose** (p.7) — « Une fonction f définie sur un intervalle ouvert I est continue en un réel
> a de I, si et seulement si, lim_{x→a⁻} f(x) = lim_{x→a⁺} f(x) = f(a). »

> **Encadré rose** (p.7) — « • Une fonction est continue sur un intervalle ouvert I si elle est
> continue en tout réel de I. • Une fonction est continue sur un intervalle [a, b] si elle est
> continue sur ]a, b[, à droite en a et à gauche en b. De façon analogue, on définit la continuité de
> f sur les intervalles [a, b[, ]a, b], [a, +∞[ et ]−∞, a]. »

> **Tableaux d'opérations sur les limites** (p.8 ; « Soit L et L′ deux réels. Les résultats qui suivent
> concernent les opérations sur les limites en un réel ou à l'infini. ») —
> lim(f + g) : (L, L′) → L + L′ ; (L, +∞) → +∞ ; (−∞, L′) → −∞ ; (+∞, +∞) → +∞ ; (−∞, −∞) → −∞.
> lim(f × g) : (L, L′) → L × L′ ; (+∞, L′ > 0) → +∞ ; (+∞, L′ < 0) → −∞ ; (+∞, +∞) → +∞ ;
> (+∞, −∞) → −∞ ; (−∞, −∞) → +∞.
> lim(f/g) : (L, L′ ≠ 0) → L/L′ ; (+∞, L′ > 0) → +∞ ; (+∞, L′ < 0) → −∞ ; (L, +∞) → 0 ; (L, −∞) → 0 ;
> (L ≠ 0, 0) → ∞ (« On applique la règle des signes »).
> lim f → lim |f| → lim √f : L → |L| → √|L| ; +∞ → +∞ → +∞ ; −∞ → +∞ → +∞.
> (Le tableau de √f imprimé porte « √|L| » pour L ; noté tel quel — voir doutes.)

> **Formes indéterminées** (p.8) — « Les règles énoncées dans les tableaux précédents ne s'appliquent
> pas lorsqu'il s'agit d'étudier * la limite de la somme de deux fonctions dont l'une tend vers +∞ et
> l'autre tend vers −∞. * la limite du produit de deux fonctions dont l'une tend vers l'infini et
> l'autre tend vers 0. * la limite du quotient de deux fonctions qui tendent toutes les deux vers
> l'infini ou toutes les deux vers 0. Une transformation d'écriture adéquate pourra nous ramener à
> l'un des théorèmes résumés dans les tableaux ci-dessus. »

> **Théorème** (p.8) — « • La limite d'une fonction polynôme à l'infini est la même que celle de son
> terme de plus haut degré. • La limite d'une fonction rationnelle à l'infini est la même que celle du
> quotient des termes de plus haut degré. »

> **Définition** (p.9) — « Soit u une fonction définie sur un ensemble I et v une fonction définie sur
> un ensemble J tel que u(I) est inclus dans J. La fonction notée v∘u, définie sur I par
> v∘u(x) = v(u(x)), est appelée fonction composée de u et v. »

> **Théorème (admis)** (p.9) — « Soit u une fonction définie sur un intervalle ouvert I contenant un
> réel a et v une fonction définie sur un intervalle ouvert J contenant le réel u(a). Si u est
> continue en a et v est continue en u(a), alors la fonction v∘u est continue en a. »

> **Corollaire** (p.9) — « La composée de deux fonctions continues est continue. »

> **Théorème (admis)** (p.10) — « Soit u et v deux fonctions. Soit a, b et c finis ou infinis.
> Si lim_{x→a} u(x) = b et lim_{x→b} v(x) = c alors lim_{x→a} v∘u(x) = c. »

> **Théorème (admis)** (p.11) — « Soit f, u et v trois fonctions définies sur un intervalle I sauf
> peut-être en un réel a de I. Soit deux réels ℓ et ℓ′. • Si u(x) ≤ v(x) pour tout x ≠ a et si
> lim_a u = ℓ et lim_a v = ℓ′, alors ℓ ≤ ℓ′. • Si u(x) ≤ f(x) ≤ v(x) pour tout x ≠ a et si
> lim_a u = lim_a v = ℓ, alors lim_a f = ℓ. • Si v(x) ≥ u(x) pour tout x ≠ a et si lim_a u = +∞, alors
> lim_a v = +∞. • Si v(x) ≤ u(x) pour tout x ≠ a et si lim_a u = −∞, alors lim_a v = −∞. Les résultats
> énoncés ci-dessus restent valables lorsque l'on considère des limites à l'infini, à droite en a ou à
> gauche en a. » (Phrase d'introduction p.11 : « Les résultats énoncés ci-dessous permettent de
> déterminer la limite d'une fonction par comparaison avec les limites d'autres fonctions. »)

> **Théorème (Rappel)** (p.12) — « L'image d'un intervalle par une fonction continue est un
> intervalle. »

> **Théorème des valeurs intermédiaires (Rappel)** (p.12) — « Soit f une fonction continue sur un
> intervalle I. Soit a et b deux réels de I tels que a < b. Pour tout réel k compris entre f(a) et
> f(b) l'équation f(x) = k possède au moins une solution dans l'intervalle [a, b]. En particulier,
> si f(a).f(b) < 0 alors l'équation f(x) = 0 admet au moins une solution dans ]a, b[. » (Figure :
> courbe avec f(a), f(b), k, solutions x₀, x₁, x₂.)

> **Encadré rose** (p.13) — « Une fonction f est strictement croissante sur un intervalle I si pour
> tous réels a et b de I tels que a < b, f(a) < f(b). Une fonction f est strictement décroissante sur
> un intervalle I si pour tous réels a et b de I tels que a < b, f(a) > f(b). Une fonction est
> strictement monotone sur un intervalle I, si elle est strictement croissante sur I ou strictement
> décroissante sur I. »

> **Théorème** (p.13) — « Soit f une fonction continue et strictement monotone sur un intervalle I.
> Soit a et b deux réels de I tels que a < b. Alors pour tout réel k compris entre f(a) et f(b)
> l'équation f(x) = k admet une unique solution dans [a, b]. » **Démonstration** : « Elle découle du
> théorème des valeurs intermédiaires et de la stricte monotonie de f. »

> **Théorème** (p.14) — « Soit f une fonction continue sur un intervalle I. Si la fonction f ne
> s'annule en aucun point de I alors elle garde un signe constant sur I. » **Démonstration** (imprimée) :
> « Supposons que f change de signe sur I. Il existe alors deux réels α et β (α < β) de I tels que
> f(α).f(β) < 0. La fonction f étant continue sur [α, β], l'équation f(x) = 0 admet au moins une
> solution dans [α, β]. Ce qui contredit l'hypothèse « f ne s'annule en aucun point de I ». »

> **Théorème** (p.15) — « L'image d'un intervalle fermé borné [a, b] par une fonction continue est un
> intervalle fermé borné [m, M]. Le réel m est le minimum de f sur [a, b]. Le réel M est le maximum de
> f sur [a, b]. » (Figure : courbe avec m, M, f(a), f(b), α, β.)

> **Théorème (admis)** (p.16) — « Soit f une fonction définie sur un intervalle de type [a, b[ (b fini
> ou infini). • Si la fonction f est croissante et majorée alors f possède une limite finie en b.
> • Si la fonction f est croissante et non majorée alors f tend vers +∞ en b. • Si la fonction f est
> décroissante et minorée alors f possède une limite finie en b. • Si la fonction f est décroissante
> et non minorée alors f tend vers −∞ en b. »

> **Théorème (admis)** (p.16) — « L'image d'un intervalle I par une fonction continue et strictement
> monotone sur I est un intervalle de même nature. »

> **Exemples** (p.16, tableau) — Colonnes « Si f est strictement croissante sur I » / « Si f est
> strictement décroissante sur I » :
> I = [a, b] : f(I) = [f(a), f(b)] / [f(b), f(a)] ;
> I = [a, b[ (a ∈ ℝ, b ∈ ℝ) : f(I) = [f(a), lim_{b⁻} f[ / ]lim_{b⁻} f, f(a)] ;
> I = [a, +∞[ (a ∈ ℝ) : f(I) = [f(a), lim_{+∞} f[ / ]lim_{+∞} f, f(a)] ;
> I = ]a, b[ (a ∈ ℝ, b ∈ ℝ) : f(I) = ]lim_{a⁺} f, lim_{b⁻} f[ / ]lim_{b⁻} f, lim_{a⁺} f[.

### QCM – VRAI-FAUX (p.18)

- **QCM** « Cocher la réponse exacte. » 1. Si lim_{+∞} f = +∞ et g(x) = sin(1/x) − f(x), alors lim_{+∞} g
  est égale à ☐ +∞ ☐ n'existe pas ☐ −∞. 2. f continue décroissante sur [2, 5] et f([2, 5]) = [1, 3] :
  ☐ f(2) = 3 et f(5) = 1 ☐ f(2) = 1 et f(5) = 3 ☐ 1 < f(2) < 3. 3. f continue sur [−2, 5], f(−2) = 3 et
  f(5) = −2 : l'équation f(x) = −1 ☐ n'admet pas de solution ☐ admet au moins une solution ☐ admet
  exactement une solution dans [−2, 5].
- **VRAI-FAUX** « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)
  1. f paire et lim_{−∞} f = −∞ ⇒ lim_{+∞} f = −∞. 2. Toute fonction croissante sur ℝ tend vers +∞ en +∞.
  3. Fonction à limite finie en −∞ et en +∞ ⇒ bornée. 4. f non définie en a ⇒ nécessairement la droite
  Δ : x = a est asymptote verticale à C_f. 5. g ≤ f ≤ h sur ℝ, lim_{+∞} g = 3 et lim_{+∞} h = 5 ⇒ f
  admet une limite finie en +∞.

### Exercices et problèmes (p.19–22) — 26 exercices + « Application »

- **Ex. 1** (p.19) : ensemble de définition et continuité en tout réel de cet ensemble : x ↦ |x² − x − 3| ;
  x ↦ x + 1 + √(x² + 1) ; x ↦ √((x + 1)/(x − 1)) ; x ↦ (|x + 1| − 2)⁵ ; x ↦ (3x² − |x|)/(x² + 4) ;
  x ↦ 1/(cos²x + 1) ; x ↦ (cos x − 1)/(sin x − 1).
- **Ex. 2** (p.19) : f(x) = 2 + 1/(x + 1) si x < −1 ; 2x² + x si x ≥ −1. 1. tracer C_f (repère orthonormé) ;
  2. continuité sur ]−∞, −1[ et ]−1, +∞[ ; 3. f continue sur ℝ ? ; 4. nombre graphique de solutions de
  f(x) = −3 ; −1 ; 0.5 ; 1 ; 4.
- **Ex. 3** (p.19) : f(x) = √(x + 2) si x ≥ −2 ; (2x² − |x³|)/(x + 2) si x < −2. 1. continuité en −2 ;
  2. sur ]−∞, −2[ et sur [−2, +∞[ ; 3. f continue sur ℝ ?
- **Ex. 4** (p.19) : f(x) = √(x² − 1) si x ∈ ]−∞, −1] ∪ [1, +∞[ ; (1 − x³)/(1 − x²) si −1 < x < 1.
  1. continuité à gauche et à droite en −1 ; 2. continuité sur ]−∞, −1], ]−1, 1[ et [1, +∞[.
- **Ex. 5** (p.19) : f : x ↦ (x³ + 3x² − 6x − 8)/(x − 2). 1. ensemble de définition ; 2. lim_{−∞}, lim_{+∞},
  lim_{x→2} f(x) ; 3. f admet-elle un prolongement par continuité en 2 ?
- **Ex. 6** (p.19) : la fonction admet-elle un prolongement par continuité en a : 1. (x² + |x|)/(x² − |x|),
  a = 0 ; 2. (x³ + 1)/(x² − 1), a = −1 ; 3. (sin x + 3x)/x, a = 0.
- **Ex. 7** (p.19) : f(x) = x(x² − x − 2)/(|x|(x − 2)) si x ≠ 2 et x ≠ 0 ; 3 si x = 2 ; 2 si x = 0.
  1. continue en 0 ? 2. continue en 2 ?
- **Ex. 8** (p.19) : f(x) = |x||x − 2|/(x(x² − x − 2)) si x ≠ 2 ; 1/3 si x = 2. 1. ensemble de définition ;
  2. limites en −1, +∞, −∞ ; 3. prolongement par continuité en 0 ?
- **Ex. 9** (p.20) : limites : 1. −2/(x − 1) en 1⁺ et 1⁻ ; 2. −2x³/(x² − 1) en −1⁺ et −1⁻ ;
  3. −3/(x² − 3x + 2) en 1⁻ et 1⁺ ; 4. √(1 + x²)/x en +∞ et −∞.
- **Ex. 10** (p.20) : prolongement par continuité en x₀ : 1. (x³ + 3x² − 2x − 4)/(x + 1), x₀ = −1 ;
  2. (1 − √2 cos x)/(4x − π), x₀ = π/4 ; 3. (cos(4x) − 1)/x², x₀ = 0.
- **Ex. 11** (p.20) : limite de 1. cos((πx + 1)/x) en −∞ ; 2. sin(3/√x) en +∞ ; 3. sin(x²)/x en 0⁺.
- **Ex. 12** (p.20) : f(x) = (1 − cos x)/x sur ℝ*. 1. lim_{x→0} f(x) ; 2. lim_{x→0} f(sin x) et
  lim_{x→0} f(1 − cos x).
- **Ex. 13** (p.20) : par comparaison, limite en 0 de 1. x·sin(2/x) ; 2. 1 + x²·sin(2/x) ; 3. 1/x + sin(2/x).
- **Ex. 14** (p.20) : par comparaison, limites en +∞ et −∞ de 1. (1 + cos x)/x ; 2. (1 + cos x)/√|x| ;
  3. (x + x cos x)/(x⁴ + x² + 3).
- **Ex. 15** (p.20) : 1. montrer que pour tout x, 1/3 ≤ 1/(2 − sin x) ≤ 1 ; 2. en déduire le comportement en
  +∞ de x ↦ x/(2 − sin x) et x ↦ (x + sin x)/(2 − sin x).
- **Ex. 16** (p.20) : f : x ↦ x cos x/(x² + 1). 1. trouver M > 0 tel que |x·f(x)| ≤ M pour tout x ;
  2. en déduire le comportement de f en −∞ et +∞.
- **Ex. 17** (p.20) : f sur ℝ* : f(x) = (1/x)(2 − sin(1/x)). 1. a. x > 0 : f(x) ≥ 1/x ; b. en déduire
  lim_{0⁺} f ; 2. a. x < 0 : f(x) ≤ 1/x ; b. en déduire lim_{0⁻} f.
- **Ex. 18** (p.21) : image de I par f : 1. (x + 1)/(x − 2), I = ]2, +∞[ ; 2. √(x² − 2x), I = ]−∞, 0] ;
  3. 1/sin x, I = ]0, π/2] ; 4. tan(πx), I = ]−1/2, 0].
- **Ex. 19** (p.21) : lecture graphique de f(I) : quatre courbes, I = [−1, 3] ; [−2, 3] ; [−1, 3] ; [−2, 2[.
- **Ex. 20** (p.21) : tracer la courbe (repère orthonormé) et donner f(I) : 1. x ↦ −x + 3, I = [1, 4] ;
  2. x ↦ 1/x, I = ]−∞, 0[ ; 3. x ↦ x² + 1, I = ]−1, 2].
- **Ex. 21** (p.21) : f : x ↦ x³ + 10x − 1. 1. strictement croissante sur ℝ ; 2. a. f(x) = 0 admet une unique
  solution a dans [0, 1] ; b. valeur approchée de a à 10⁻¹ près.
- **Ex. 22** (p.21) : f : x ↦ x³ − 2x² + x + 1. 1. tableau de variation et tracé (repère orthogonal) ;
  2. f(x) = 0 admet une solution a dans [−1, 0] ; 3. valeur approchée de a à 10⁻¹ près.
- **Ex. 23** (p.21–22) : f : x ↦ x³ − 12x + 1. 1. tableau de variation et tracé ; 2. vérifier graphiquement
  que C_f coupe l'axe des abscisses en trois points M₁, M₂, M₃ d'abscisses x₁ < x₂ < x₃ ; 2. [sic, numérotation
  imprimée] x₁ ∈ ]−4, −3[ ; 3. pour x₂ et x₃, encadrement par deux entiers consécutifs ; 4. discuter selon k le
  nombre de solutions de f(x) = k ; 5. nombre de solutions de |f(x)| = 1.
- **Ex. 24** (p.22) : 1. h : x ↦ √x − 1/x − 1 ; a. strictement croissante sur ]0, +∞[ ; b. h(]0, +∞[) ;
  c. h(x) = 0 admet dans [2, 3] une unique solution α ; d. valeur approchée de α à 10⁻¹ près ;
  2. représenter dans un repère orthogonal f(x) = √x et g(x) = 1/x + 1 sur ]0, +∞[.
- **Ex. 25** (p.22) : f : x ↦ cos x − x. 1. strictement décroissante sur [0, π/2] ; 2. f(x) = 0 admet une
  solution unique a dans [0, π/2] ; 3. valeur approchée de a à 10⁻¹ près.
- **Ex. 26** (p.22) : f continue de [0, 1] sur [0, 1], g(x) = f(x) − x. 1. signe de g(0)g(1) ; 2. en déduire
  que f(x) = x admet au moins une solution dans [0, 1].
- **Application** (p.22) : montrer que cos(π/2·x) = x admet au moins une solution dans [0, 1].

### Écart avec la référence (chapitre math-bac-math/01, manuel 222445, p.5–27)

**Ce que la référence enseigne et que ce manuel n'a PAS (à exclure du chapitre bac-sciences-exp)** :
- toute la partie **II. Branches infinies** de la référence (asymptotes verticale/horizontale/oblique, tableau
  des branches infinies, étude de f(x)/x, branches paraboliques, directions asymptotiques, Act. 1–4 p.9–11) et
  la définition d'un **axe de symétrie** Δ : x = a ; les exercices de branches infinies (réf. Ex. 7, 10–14) ;
- le **Problème résolu** (réf. p.20–22 : f(x + 1/n) = f(x), somme télescopique) ;
- les activités de **limites composées plus nombreuses** de la référence (III.3 Act. 1–5) : ici 3 activités + 1
  exercice résolu + Act. 6 ;
- les **applications géométriques** de la référence (rectangle OPMQ inscrit, aire AHM, Ex. 28) et le **point
  fixe généralisé** (réf. Ex. 29, f([a, b]) ⊂ [a, b]) : ici seulement le point fixe sur [0, 1] (Ex. 26 +
  Application) ;
- les activités « image de [1, 4] et [−10, −1] par x + 4/x », « signe constant de 1 + x + … + x¹⁰ » et
  « 1 + sin x + … + sin¹⁰x » : ici 1 + x + x² + x³ + x⁴ (Act. 6) seulement ;
- la dichotomie est **présente** dans les deux manuels (x³ + x − 1 sur [0, 1], tableur) : pas d'écart, sinon
  l'amplitude finale demandée (10⁻³ ici).

**Ce que ce manuel a en plus (ou autrement)** :
- numérotation différente (parties I à V, ci-dessus) ; Rappels = Act. 1–7 (réf. : 1–5 + I.2 + I.3) ;
  Act. 6 sur la continuité de sin 3x/x sur [0, π] (réf. : (1 − cos x)/x sur [0, π]) ;
- **Exercices résolus 1–4** (p.10, 11, 15, 17) ; la référence n'a qu'un Problème résolu ;
- énoncé du théorème de comparaison avec **4 puces** dont u ≤ v ⇒ ℓ ≤ ℓ′ (la référence : encadrement et
  minoration seulement) ;
- **fonctions parité/imparité** utilisées dans Exercice résolu 3 (f impaire) ;
- **tableau de variation + tracé** exigés (Ex. 22, 23) ; discussion du nombre de solutions de f(x) = k et
  de |f(x)| = 1 (Ex. 23) ;
- énoncé de la **monotonie stricte** (encadré rose p.13, définitions) et théorème « signe constant » AVEC
  démonstration imprimée ;
- exercices de **continuité par morceaux** avec valeur absolue (Ex. 2–4, 7–8) et de prolongement (Ex. 5–6, 10) ;
- QCM (3) + Vrai-Faux (5) identiques à ceux de la référence (mêmes énoncés).

### Bornes de scope (chapitre 1, section Sciences expérimentales)

- ✅ INCLUS : rappels de 3ᵉ année (continuité et limite en un réel, prolongement par continuité, continuité
  sur un intervalle ouvert/fermé, limites à gauche/droite) ; opérations sur les limites, formes
  indéterminées, limites de polynômes/rationnelles à l'infini ; continuité d'une composée v∘u et limite d'une
  composée (théorèmes admis) ; limites par comparaison (u ≤ f ≤ v, minoration, majoration, ℓ ≤ ℓ′) ;
  image d'un intervalle par une fonction continue (intervalle) ; TVI ; théorème de la bijection version
  « unique solution » (continue + strictement monotone) ; signe constant ; image d'un intervalle fermé borné
  (minimum/maximum) ; théorème de la limite monotone (admis) ; image par fonction continue strictement
  monotone (tableau f(I)) ; dichotomie à la main et au tableur ; point fixe sur [0, 1] ; parité (f impaire, ER3) ; partie entière E(a)
  (V Act. 1) ; discussion selon k du nombre de solutions de f(x) = k sur des morceaux strictement monotones
  (Ex. 23).
- ⛔ EXCLU (non traité dans ces pages) : branches infinies (asymptotes, branches paraboliques, directions
  asymptotiques), axe de symétrie ; problème résolu à paramètre n ; dérivation et lien continuité ↔
  dérivabilité (les « tableaux de variation » des Ex. 22–23 y sont demandés sans dérivée enseignée : voir
  doutes) ; suites et limites de suites ; définition ε de la limite ; fonction réciproque.

### Lecture

- **Pages lues par l'OCR (texte)** : p.5 à p.22, toutes (fichiers pNNN.txt).
- **Pages lues sur l'image (110 dpi)** : p.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
  = **18 pages sur 18** (100 %, au-delà du plancher « ≥ 1 sur 10 » ; toute page à formule/encadré/tableau).
- **Écarts OCR / image constatés** : p.6 OCR mêlait l'encadré rose au corps (activité 1 illisible, « Act. 2 »
  à fraction coupée) ; p.7 OCR confond Act. 6 avec I.2 sans numéro, perd « sin 3x/x » et « 3 » (valeur en 0) ;
  p.8 OCR : tableaux de limites totalement dégradés (colonnes mélangées, « √|L| » ↔ « √L ») ; p.9 OCR perd
  les images de la figure et la forme de f en Act. 2 ; p.10 OCR : Act. 4 « tan x²/4 » OK mais Exercice résolu 1
  inversé (1/x² ↔ cos x − x), figure Act. 5 absente ; p.11 OCR : « ℓ ≤ ℓ′ » devenu « ℓ</′ », bornes
  d'encadrement 1 ≤ … ≤ 2 écrites 1 ≤ … 2 ; p.12 OCR : TVI sans bornes d'intervalle correctes (« ,b[ »
  pour ]a, b[), Act. 1 sans les trois intervalles ; p.13 OCR perd les définitions roses et l'intervalle
  [0, π/2] de l'Act. 4 ; p.14 OCR : le tableur est du bruit (chiffres lus faux), seules les formules
  `=PUISSANCE(A2;3)+A2−1` et `=SI(F2*E2>0;…)` ont été récupérées sur image ; p.15 OCR « 0.672 ≤ f ≤ 4/3 »
  mal formé ; p.16 OCR : tableau « Exemples » à moitié illisible (lim_{b⁻}, lim_{a⁺}) ; p.18 OCR
  QCM 2 : « f(L; 5) » pour f([2, 5]) ; p.19–22 OCR : exposants et valeurs absolues dégradés (Ex. 1, 3, 4, 7,
  8 reconstruits sur image) ; p.21 OCR : les 4 graphiques de l'Ex. 19 non rendus (intervalles
  I = [−1, 3], [−2, 3], [−1, 3], [−2, 2[ lus sur image). **Conclusion : l'OCR ne suffit pas pour ce
  chapitre ; toute formule vient de l'image.**
- **Doutes signalés** : (1) tableau de √f p.8 : imprimé « √|L| » pour la limite de √f quand lim f = L ;
  noté tel quel (la référence écrit √L) ; (2) Ex. 23 : « 2. » imprimé deux fois (coquille source) ;
  (3) Ex. 22–24 demandent un tableau de variation / stricte croissance alors que la dérivation n'est pas
  traitée dans ces pages : non contredit, mais à confronter au chapitre « Dérivabilité » du manuel
  (hors périmètre p.5–22) ; (4) Ex. 3 : la 2ᵉ ligne de f(x) est (2x² − |x³|)/(x + 2) (valeur absolue sur x³,
  lue sur image, OCR illisible) ; (5) Act. 6 p.7 est numérotée « Activité 6 » dans I.2, alors que la
  référence la numérote « Activité » seule.

## 2.2 Chapitre 2 — Suites réelles (manuel 222433, p.23–38)

**Page de garde (p.23)** — Titre « Suites réelles », Chapitre 2. Même citation liminaire d'As-Samaw'al
(1172, traité d'Arithmétique : approximation indéfinie d'une racine irrationnelle par des rationnels de
plus en plus proches ; « R. Rashed, Entre Arithmétique et Algèbre, 1984 » ; reproduction « Tableau
d'As-Samawal »). Aucune notion mathématique sur cette page.

**Plan (p.24–32, 7 parties, identique à la référence)** : I. Rappels et compléments sur les limites de
suites (p.24–25) · II. Suites géométriques et applications (p.25–27) · III. Suites du type vₙ = f(uₙ)
(p.28) · IV. Limites et ordre (p.28–30) · V. Convergence des suites monotones (p.30–31) · VI. Suites
récurrentes (p.31–32) · VII. Suites adjacentes (p.32). Puis Exercice résolu 2 (p.33), QCM – VRAI-FAUX
(p.34), « Exercices et problèmes » (p.35–38, 22 exercices numérotés 1 à 22). Pas de « Problème corrigé »
ni de rubrique d'exercice avec solution autre que les deux « Exercices résolus » (p.26–27 et p.33).

### Cours — Activités

**I. Rappels et compléments sur les limites de suites** (p.24–25)

- **Act. 1** (p.24) : limite de (uₙ) : uₙ = 1/n (n ≥ 1) ; uₙ = n² + 1 (n ≥ 0) ; uₙ = 10ⁿ (n ≥ 0).
- **Act. 2** (p.24) : uₙ = (1 − (−1)ⁿ)/(2n + (−1)ⁿ), n ≥ 1. 1. expressions de u₂ₙ et u₂ₙ₊₁ ; 2. que dire
  de la limite de uₙ ? (suivie du théorème U₂ₙ / U₂ₙ₊₁ admis).
- **Act. 3** (p.24) : étudier la convergence de uₙ = 1 + (−1)ⁿ/n, n ≥ 1.
- **Act. 4** (p.24) : uₙ = (−1)ⁿ. 1. montrer que (uₙ) est bornée ; 2. est-elle convergente ?
- **Act. 5** (p.24) : uₙ = n/(2n + 2). 1. montrer que (uₙ) est convergente ; 2. est-elle bornée ?
  (suivie du théorème « toute suite convergente est bornée », admis).
- **Act. 6** (p.25) : limite de uₙ = 1/(2 − 1/√n) − 3n³ (n ≥ 1) ; uₙ = (1/n² − 1/2)(n³ + 3n − 1)
  (n ≥ 1) ; uₙ = −1/n + √((5n + 3)/(2n + 9)) (n ≥ 1) ; uₙ = (1/√(4n + 1))·√(n + 1/2) (n ≥ 0) [lecture confirmée sur l'image p.25].

**II. Suites géométriques et applications** (p.25–27)

- **Act. 1** (p.25) : limite de uₙ = (1/5)ⁿ ; (−2/√5)ⁿ ; (√π)ⁿ (n ≥ 0).
- **Act. 2** (p.26) : limite de (uₙ) : 1. uₙ = (1 − (−1/3)ⁿ)/(1 − n³) (n ≥ 2) ; 2. uₙ = ((−2)ⁿ − 3)/
  (4(−2)ⁿ + 5) (n ≥ 0) ; 3. uₙ = 1 + 5/3 + … + (5/3)ⁿ (n ≥ 0) ; 4. uₙ = −3 − 9/π − … − 3(3/π)ⁿ (n ≥ 0).
- **Act. 3** (p.26) : u₀ = 2, uₙ₊₁ = 2uₙ − 1 (n ≥ 0). 1. solution α de x = 2x − 1 ; 2. vₙ = uₙ − α,
  montrer que (vₙ) est géométrique ; 3. en déduire uₙ en fonction de n et lim uₙ.
- **Exercice résolu 1** (p.26–27, solution imprimée en entier) : f : x ↦ 1 + 2/(x + 1). 1. réels x tels
  que f(x) = x (réponse : f(√3) = √3 et f(−√3) = −√3) ; 2. pour x, y ≠ −1, f(x) − f(y) = 2(y − x)/
  ((x+1)(y+1)) ; 3. u₀ = 1, uₙ₊₁ = f(uₙ) : a. uₙ positif (récurrence) ; b. représenter f et y = x
  (graphique imprimé) ; c. u₁ = 2, u₂ = 5/3, u₃ = 7/4, à représenter sur l'axe (O, i⃗) ; 4. vₙ =
  (uₙ − √3)/(uₙ + √3) : a. via Q2, (vₙ) géométrique de raison (1 − √3)/(1 + √3) et de premier terme
  (1 − √3)/(1 + √3) ; b. |(1 − √3)/(1 + √3)| < 1 donc vₙ → 0, uₙ = (√3 + √3·vₙ)/(1 − vₙ), donc (uₙ)
  converge vers √3. (Même exercice résolu que la référence.)

**III. Suites du type vₙ = f(uₙ)** (p.28)

- **Act. 1** (p.28) : limite de uₙ = sin((0,75)ⁿ) (n ≥ 1) ; uₙ = n·sin(π/(2n)) (n ≥ 1) ;
  uₙ = cos(πn/(2n + 1)) (n ≥ 0) ; uₙ = (cos(1/n) + 1)/n (n ≥ 1).

**IV. Limites et ordre** (p.28–30)

- **Act. 1** (p.28) : vₙ = (n + cos n)/(n² + 1), n ≥ 1. 1. montrer (n − 1)/(n² + 1) ≤ vₙ ≤ (n + 1)/(n² + 1) ;
  2. valeurs approchées à 10⁻⁵ de v₁₀₀₀ et v₁₀⁶ ; 3. conjecture sur lim vₙ.
- **Act. 2** (p.28) : 1. pour n ≥ 4, 2ⁿ ≥ n² ; 2. en déduire 2ⁿ/n ≥ n pour n ≥ 4 ; 3. conjecture sur
  lim 2ⁿ/n. (Suivie des résultats de comparaison admis.)
- **Act. 3** (p.29) : uₙ = 1/(√n + cos²n), n ≥ 0. 1. pour n ≥ 1, 0 ≤ uₙ ≤ 1/√n ; 2. en déduire lim uₙ.
- **Act. 4** (p.29) : uₙ = 10ⁿ/n!. 1. montrer 0 < uₙ₊₁/uₙ ≤ 10/11 pour n ≥ 10 ; 2. montrer
  0 < uₙ ≤ (10/11)^(n−10)·u₁₀ (n ≥ 10), en déduire que (uₙ) converge et sa limite ; 3. à la calculatrice,
  un entier n₀ tel que |uₙ| ≤ 10⁻⁶ pour n ≥ n₀.
- **Act. 5** (p.29) : limite de uₙ = (3n + 1)ⁿ (n ≥ 1) ; uₙ = n³/(2 + sin 3n) (n ≥ 1) ; uₙ = n³(sin n − 3)
  (n ≥ 1) ; uₙ = (n + sin²(2n))/n³ (n ≥ 1).
- **Act. 6** (p.30) : symbole Σ. 1. écrire avec Σ : A = 1 + 2 + 3 + … + n ; B = −1/2 + 1/4 − 1/8 + … − 1/512
  [signes lus sur l'image] ; 2. calculer C = Σ_{k=10}^{500} 1 ; D = Σ_{k=0}^{20} (3k − 1) ;
  E = Σ_{k=3}^{10} 10⁻ᵏ.
- **Act. 7** (p.30) : 1. vérifier 1/(k(k+1)) = 1/k − 1/(k+1) (k entier non nul) ; 2. limite de
  wₙ = Σ_{k=1}^{n} 1/(k(k+1)) (n ≥ 1).

**V. Convergence des suites monotones** (p.30–31)

- **Act. 1** (p.30) : wₙ = 1/n² + 2/n² + … + n/n² (n ≥ 1). 1. a. 1 + 2 + … + n = n(n+1)/2 ; b. (wₙ)
  décroissante et minorée ; c. (wₙ) convergente, sa limite. 2. vₙ = 1/n + 2/n + … + n/n (n ≥ 1) :
  a. (vₙ) croissante ; b. est-elle convergente ?
- **Act. 2** (p.31) : uₙ = 1 + 1/√2 + 1/√3 + … + 1/√n (n ≥ 1). 1. croissante ; 2. uₙ ≥ √n ; 3. lim uₙ ;
  4. (uₙ) non majorée.

**VI. Suites récurrentes** (p.31–32)

- **Act. 1** (p.31) : uₙ₊₁ = uₙ(uₙ − 1), n ≥ 1 ; au tableur, calculer les dix mille premiers termes et
  conjecturer la limite pour u₁ = 0 ; 2 ; 1 ; −1 ; 0,5 ; 4.
- **Act. 2** (p.32) : a₀ = 1, aₙ₊₁ = √(aₙ + 1), n ≥ 0. 1. croissante et majorée par 2 ; 2. sa limite.
- **Act. 3** (p.32) : u₀ = 0,25, uₙ₊₁ = uₙ(1 − uₙ), n ≥ 0. 1. décroissante ; 2. 0 ≤ uₙ ≤ 1 ; 3. limite.

**VII. Suites adjacentes** (p.32) : aucune activité de découverte ; définition-théorème suivi de sa
démonstration, puis Exercice résolu 2.

- **Exercice résolu 2** (p.33, solution imprimée en entier) : uₙ = 1 − 1/√2 + 1/√3 − … + (−1)ⁿ⁺¹/√n,
  n ≥ 1. 1. (u₂ₙ) croissante et (u₂ₙ₊₁) décroissante ; 2. comparer u₂ₙ et u₂ₙ₊₁, calculer
  lim (u₂ₙ − u₂ₙ₊₁) (= 0) ; 3. (uₙ) converge vers α (suites (u₂ₙ), (u₂ₙ₊₁) adjacentes, puis convergence de
  (uₙ) par la convergence des deux sous-suites vers α) ; 4. a. u₂ₙ ≤ α ≤ u₂ₙ₊₁ ; b. u₄, u₅ et valeur
  approchée de α à 10⁻³ près (α ≈ 0,817 [valeur imprimée fausse : 0,817 ≈ u₅ ; α ≈ 0,605 ; erreur du manuel, à ne pas reprendre]).

### Cours — Encadrés, définitions, théorèmes (VERBATIM, vérifiés sur l'image)

> **Théorème (admis)** (p.24) — « Soit (uₙ) une suite réelle et a fini ou infini. lim_{n→+∞} uₙ = a,
> si et seulement si, lim_{n→+∞} u₂ₙ = a et lim_{n→+∞} u₂ₙ₊₁ = a. »

> **Théorème (admis)** (p.25) — « Toute suite convergente est bornée. »

> **Opérations sur les limites de suites** (p.25) — « Soit a et b deux réels. Les résultats qui suivent
> concernent les opérations sur les limites de suites réelles. Soit deux suites (uₙ) et (vₙ) et deux
> réels a et b. » Trois tableaux (lim uₙ ; lim vₙ ; résultat) :
> Somme lim(uₙ + vₙ) : a, b → a + b ; +∞, b → +∞ ; −∞, b → −∞ ; +∞, +∞ → +∞ ; −∞, −∞ → −∞.
> Produit lim(uₙ·vₙ) : a, b → ab ; ∞, b ≠ 0 → ∞ (on applique la règle des signes) ; ∞, ∞ → ∞ (on applique
> la règle des signes).
> Quotient lim(uₙ/vₙ) : a, b ≠ 0 → a/b ; ∞, b → ∞ (on applique la règle des signes) [colonne « b » sans
> « ≠ 0 » telle qu'imprimée sur cette ligne ; la référence note b ≠ 0 : coquille probable du manuel,
> signalée] ; a, +∞ → 0 ; a, −∞ → 0 ; a ≠ 0, 0 → ∞ (on applique la règle des signes).

> **Théorème (Rappel)** (p.26) — « Soit (uₙ) une suite géométrique définie par uₙ = qⁿ, n ≥ 0, où q est
> un réel non nul. • Si q > 1, alors lim_{n→+∞} uₙ = +∞. • Si |q| < 1, alors lim_{n→+∞} uₙ = 0. • Si
> q ≤ −1, alors la suite (uₙ) n'a pas de limite. • Si q = 1, alors la suite (uₙ) est constante. »

> **Théorème (admis)** (p.28) — « Soit f une fonction définie sur un intervalle ouvert I et (uₙ) une
> suite d'éléments de I. Si lim_{n→+∞} uₙ = ℓ (fini ou infini) et si lim_{x→ℓ} f(x) = L (fini ou infini),
> alors lim_{n→+∞} (f(uₙ)) = L. »

> **Résultats de comparaison (admis)** (p.29) — « Nous admettons les résultats ci-dessous qui nous
> permettent de trouver la limite d'une suite par comparaison avec d'autres suites dont on connaît les
> limites. Soit (uₙ), (vₙ) et (wₙ) des suites réelles, a et b deux réels.
> Si uₙ ≤ vₙ, n ≥ N₀ et si lim uₙ = a et lim vₙ = b, alors a ≤ b.
> Si vₙ ≤ uₙ ≤ wₙ, n ≥ N₀ et si lim vₙ = lim wₙ = a, alors lim uₙ = a.
> Si 0 ≤ |uₙ| ≤ vₙ, n ≥ N₀ et si lim vₙ = 0, alors lim uₙ = 0.
> Si uₙ ≤ vₙ, n ≥ N₀ et lim uₙ = +∞, alors lim vₙ = +∞.
> Si uₙ ≤ vₙ, n ≥ N₀ et lim vₙ = −∞, alors lim uₙ = −∞. » (toutes limites en n → +∞)

> **Encadré de notation Σ** (p.30) — « On note Σ_{k=1}^{n} aₖ et on lit « sigma pour k variant de 1 à n
> des réels aₖ » le réel obtenu en faisant la somme des réels a₁, a₂, …, aₙ. On a donc
> Σ_{k=1}^{n} aₖ = a₁ + a₂ + … + aₙ. »

> **Théorème (admis)** (p.31) — « Soit (uₙ) une suite définie pour n ≥ 0. Si la suite (uₙ) est croissante
> et majorée, alors elle converge vers un réel a et pour tout n ≥ 0, uₙ ≤ a. Si la suite (uₙ) est
> croissante et non majorée alors elle tend vers +∞. Si la suite (uₙ) est décroissante et minorée, alors
> elle converge vers un réel b et pour tout n ≥ 0, uₙ ≥ b. Si la suite (uₙ) est décroissante et non
> minorée alors elle tend vers −∞. »

> **Théorème** (p.31, non marqué « admis » ; démonstration p.32) — « Soit une suite (uₙ) vérifiant la
> relation de récurrence uₙ₊₁ = f(uₙ), n ≥ 0 où f est une fonction. Si la suite (uₙ) est convergente vers
> un réel a et si la fonction f est continue en a alors a = f(a). »
> Démonstration (p.32, texte courant, non encadré) : si (uₙ) converge vers a, (uₙ₊₁) aussi ; f continue en
> a, donc (f(uₙ)) tend vers f(a) ; uₙ₊₁ = f(uₙ) et unicité de la limite donnent a = f(a).

> **Définition et théorème** (p.32) — « Deux suites (uₙ)_{n≥0} et (vₙ)_{n≥0} sont adjacentes lorsqu'elles
> vérifient les conditions • pour tout n ≥ 0, uₙ ≤ vₙ, • la suite (uₙ) est croissante et la suite (vₙ)
> est décroissante, • la suite (vₙ − uₙ) converge vers 0. Dans ce cas les suites (uₙ) et (vₙ) convergent
> vers la même limite. »
> Démonstration (p.32, non encadrée) : (vₙ) décroissante donne uₙ ≤ vₙ ≤ v₀, donc (uₙ) croissante et
> majorée converge vers a ; de même (vₙ) décroissante minorée par u₀ converge vers b ; vₙ = (vₙ − uₙ) + uₙ
> donne b = a.

### Quiz du manuel (p.34)

**QCM** (« Cocher la réponse exacte. ») : 1. uₙ = (n² + 2)/n sur ℕ* — (uₙ) est bornée / uₙ ≥ n pour tout n de
ℕ* / (uₙ) est majorée par 1. 2. uₙ = (n + cos n)/(n + 1) — lim = 0 / lim = −1 / lim = 1. 3. uₙ = n·sin(1/n)
sur ℕ* — lim = 0 / lim = +∞ / lim = 1. (Réponses non fournies.)

**VRAI-FAUX** (« Répondre par vrai ou faux en justifiant la réponse. », réponses non fournies) : 1. Si (uₙ)
prend un nombre fini de valeurs alors (uₙ) est convergente. 2. a. Si (uₙ) et (vₙ) sont convergentes alors
(uₙ + vₙ) est convergente ; b. Si (uₙ + vₙ) est convergente alors (uₙ) et (vₙ) sont convergentes. 3. Si
(uₙ²) converge vers L, alors on peut affirmer que (uₙ) converge vers √L ou vers −√L. 4. Si lim uₙ = lim vₙ
alors (uₙ) et (vₙ) sont adjacentes. 5. Si (u₂ₙ) et (u₂ₙ₊₁) sont convergentes alors (uₙ) est convergente.

### Exercices et problèmes (p.35–38) — 22 exercices

- **Ex. 1** (p.35) : limites de (3n−1)/(n+2) ; (n−1)/(3n+2) ; 1/(n²−n+2) ; n³−2n²+1 ; (3n−1)/|−n+2| ;
  √((n²+1)/|−n−1|) [radical sur toute la fraction, vu sur image agrandie] ; sin(1/n) ; cos(1/n).
- **Ex. 2** (p.35) : aₙ = n(1 + (−1)ⁿ)/(n² + 1), n ≥ 0. 1. a₂ₙ, a₂ₙ₊₁ ; 2. convergence et limite.
- **Ex. 3** (p.35) : aₙ = n(1 + (−1)ⁿ)/(n + 1), n ≥ 0. 1. a₂ₙ, a₂ₙ₊₁ ; 2. (aₙ) est-elle convergente ?
- **Ex. 4** (p.35) : limites de 2 + (1/3)ⁿ ; 1/(3 + 2ⁿ) ; 2ⁿ/(2ⁿ + 1).
- **Ex. 5** (p.35) : uₙ = 2ⁿ/(−5)ⁿ⁺¹, n ≥ 0 — montrer qu'elle converge, limite.
- **Ex. 6** (p.35) : limites de uₙ = sin n + n (n ≥ 0) ; uₙ = (1/n)(sin n + (1/2)ⁿ) (n ≥ 1) ;
  uₙ = −1 + (1/n²)(cos n + n) (n ≥ 1).
- **Ex. 7** (p.35) : 1. uₙ = (1 − 1/2)(1 − 1/3)…(1 − 1/n) (n ≥ 1) : montrer uₙ = 1/n, en déduire la
  limite ; 2. limite de vₙ = (1 + 1/2)(1 + 1/3)…(1 + 1/n) (n ≥ 1).
- **Ex. 8** (p.35) : uₙ = (2/n)ⁿ (n ≥ 1). 1. pour n ≥ 4, uₙ ≤ (1/2)ⁿ ; 2. lim uₙ.
- **Ex. 9** (p.35) : wₙ = n!/3ⁿ (n ≥ 0). 1. wₙ₊₁/wₙ ≥ 4/3 pour n ≥ 3 ; 2. wₙ ≥ (4/3)^(n−3)·w₃ (n ≥ 3) ;
  3. lim wₙ.
- **Ex. 10** (p.36) : uₙ = n/3ⁿ (n ≥ 0). 1. a. placer Aᵢ(i, uᵢ), i ∈ {0,…,7} ; b. uₙ₊₁/uₙ ≤ 2/3 (n ≥ 1) ;
  c. uₙ ≤ (2/3)ⁿ (n ≥ 0) ; d. lim uₙ. 2. Sₙ = Σ_{k=0}^{n} uₖ : a. Sₙ ≤ 2 ; b. (Sₙ) convergente.
- **Ex. 11** (p.36) : a > 0, bₙ = n/(1 + a)ⁿ (n non nul). 1. (binôme) (1 + a)ⁿ ≥ n(n−1)a²/2 ; 2. lim bₙ ;
  3. (xₙ)_{n≥0} géométrique de raison q, 0 < q < 1 : q = 1/(1 + a) pour un a > 0 ; lim n|xₙ| = 0 ; en
  déduire lim nxₙ ; 4. limites de n/2ⁿ⁻¹ ; n(1/3)ⁿ⁺² ; (n + 1)(1/√2)ⁿ (signes lus sur image agrandie).
- **Ex. 12** (p.36) : u₁ = 1, uₙ₊₁ = √(3uₙ), n ≥ 1. 1. 0 ≤ uₙ ≤ 3 ; 2. croissante ; 3. converge, limite.
- **Ex. 13** (p.36) : f(x) = 1 + 1/x sur ]0, +∞[. 1. variations et f(]0, +∞[) ; 2. représenter f et y = x ;
  3. φ = (1 + √5)/2, f(φ) = φ ; 4. x₀ = 2, xₙ₊₁ = f(xₙ) (suite de rationnels convergeant vers φ) :
  a. x₁…x₄ à calculer et représenter ; b. xₙ rationnel positif ; c. |xₙ₊₁ − φ| ≤ (4/9)|xₙ − φ| ; d. conclure.
- **Ex. 14** (p.36) : uₙ = Σ_{k=1}^{n} 1/k² (n ≥ 1). 1. a. u₁, u₂, u₃ ; b. croissante ; 2. a. 1/k² ≤ 1/(k−1) − 1/k
  (k ≥ 2) ; b. uₙ ≤ 2 − 1/n (n ≥ 2) ; c. converge vers ℓ et 49/36 ≤ ℓ ≤ 2.
- **Ex. 15** (p.37) : f(x) = (4x − 3)/x sur ]0, +∞[. 1. variations, courbe ; (uₙ) : u₀ ∈ ]0, +∞[,
  uₙ₊₁ = (4uₙ − 3)/uₙ. 2. u₀ = 3/4 : a. u₁, représenter u₀, u₁ ; b. (uₙ) est-elle définie ? 3. u₀ = 3 :
  a. représenter u₁, u₂, u₃ ; b. (uₙ) constante. 4. u₀ = 5 : a. représenter u₀…u₃ ; b. décroissante et
  uₙ ≥ 3 (n ≥ 1) ; c. converge vers α à déterminer ; d. calculatrice : n₀ tel que uₙ − α ≤ 10⁻⁵ (n ≥ n₀).
- **Ex. 16** (p.37) : u₁ = 5, uₙ₊₁ = 5 − 6/uₙ, n ≥ 1. 1. u₂, u₃ ; 2. pour n ≥ 0, uₙ₊₁ = (3ⁿ⁺² − 2ⁿ⁺²)/
  (3ⁿ⁺¹ − 2ⁿ⁺¹) ; 3. lim uₙ.
- **Ex. 17** (p.37) : a₀ = 1, aₙ₊₁ = aₙ² + aₙ ; b₀ = −0,5, bₙ₊₁ = bₙ² + bₙ (n ≥ 0). 1. aₙ ≥ n, lim aₙ ;
  2. a. (bₙ) bornée par −1 et 0 ; b. croissante ; c. converge, limite.
- **Ex. 18** (p.37) : u₀ = 0,1, uₙ₊₁ = 1,6uₙ(1 − uₙ). 1. variations de f : x ↦ 1,6x(1 − x) ; 2. 0,1 ≤ uₙ ≤ 3/8 ;
  3. (uₙ) converge ; 4. a. 3/8 − uₙ₊₁ = 1,6(5/8 − uₙ)(3/8 − uₙ) ; b. vₙ = 3/8 − uₙ ≥ 0 et vₙ₊₁/vₙ ≤ 0,84 ;
  c. par récurrence 0 ≤ vₙ ≤ 0,84ⁿ ; d. lim uₙ ; e. n₀ tel que 0 ≤ 3/8 − uₙ ≤ 10⁻⁵ (n ≥ n₀).
- **Ex. 19** (p.38) : « Soit a un réel strictement positif et f … f(x) = (1/2)(x + 5/x) » sur ℝ* [le « a »
  n'apparaît pas dans la formule imprimée, qui contient 5 : coquille du manuel, signalée]. 1. f′(x) =
  (x − √5)(x + √5)/(2x²), variations ; 2. u₀ = 3, uₙ₊₁ = f(uₙ) : a. √5 < uₙ₊₁ < uₙ ≤ 3, (uₙ) converge,
  limite.
- **Ex. 20** (p.38) : (uₙ) et (vₙ) adjacentes ? 1. uₙ = 2/n, vₙ = −3/n (n ≥ 2) ; 2. uₙ = (n+2)/(n−1),
  vₙ = (2n+3)/(2n+5) (n ≥ 4) ; 5. uₙ = √(n+1) − √n, vₙ = √n − √(n+1) (n ≥ 1) [numérotation imprimée
  1, 2, 5 : pas de 3 ni 4].
- **Ex. 21** (p.38) : u₀ = 12, v₀ = 1, uₙ₊₁ = (uₙ + 2vₙ)/3, vₙ₊₁ = (uₙ + 3vₙ)/4. 1. (uₙ − vₙ) géométrique,
  raison et premier terme ; 2. uₙ ≥ vₙ ; 3. adjacentes, même limite α ; 4. tₙ = 3uₙ + 8vₙ : a. constante ;
  b. valeur de α.
- **Ex. 22** (p.38) : 1. 0 < b < a : a. √(ab) ≤ (a + b)/2 ; b. (a − b)² ≤ a² − b². a₀ = a, b₀ = b, aₙ₊₁ =
  (aₙ + bₙ)/2, bₙ₊₁ = √(aₙbₙ). 2. a. bₙ ≤ aₙ ; b. (aₙ) décroissante, (bₙ) croissante ; 3. a. (aₙ₊₁ − bₙ₊₁)² ≤
  ((aₙ − bₙ)/2)² ; b. aₙ − bₙ ≤ (a − b)/2ⁿ ; 4. adjacentes, même limite α ; 5. a = 2, b = 1 : n donnant un
  encadrement de α d'amplitude 10⁻¹⁰. (Même énoncé que Ex. 32 de la référence.)

### Écart avec la référence (chapitre math-bac-math/02-suites-reelles, manuel 222445)

**À EXCLURE (dans la référence, absent de ce manuel)** :
- théorème du signe de la limite (uₙ ≥ 0 à partir d'un rang ⇒ a ≥ 0) et sa « Conséquence » m ≤ a ≤ M ;
- théorème « f continue sur I ouvert, uₙ → a ∈ I ⇒ f(uₙ) → f(a) » (ici seul le théorème limite∘suite
  admis, avec I intervalle ouvert, figure p.28) ;
- Activités sur (cos(πa))²ⁿ et (sin(n!πa))ⁿ, les suites décimales aₙ, bₙ (4,22…2), les polygones
  réguliers inscrits/circonscrits (encadrement de π), le produit 2(1+1/2)…(1+1/n), n¹⁰⁰/(1,01)ⁿ (binôme),
  les activités alternées Σ(−1)ⁿ⁺¹/n et Σ(−1)ⁿ⁺¹/n², la suite aₙ = √(2√2…), Σ1/n non majorée (U₂ₙ − Uₙ ≥ 1/2),
  les suites adjacentes uₙ₊₁ = (2uₙ + vₙ)/3 en activité de cours ;
- Problème corrigé (e : Uₙ = Σ1/k!, irrationalité de e) ;
- QCM de la référence : 3 questions dont une = Ex. 1 pour n·sin(1/n) conservée ; VF de la référence : 5
  énoncés, ici les mêmes avec 2 scindé en a. et b. ;
- les 32 exercices de la référence : ici 22 ; absents notamment : suites décimales (réf. Ex. 6), Ex. 1 avec
  calculatrice |uₙ − 2| ≤ 10⁻⁶, partie entière (réf. Ex. 16), sin(k/n²) et encadrement de sin x (réf. Ex. 17),
  Wallis (réf. Ex. 22), sommes Σk·xᵏ⁻¹ (réf. Ex. 27), (bⁿ−aⁿ)/… (réf. Ex. 28), aₙ² + aₙ discuté selon a₀
  (réf. Ex. 29), Héron avec E(√a) (réf. Ex. 31).

**EN PLUS dans ce manuel** : Act. 2 p.28 (2ⁿ ≥ n², conjecture sur 2ⁿ/n) ; Act. 1 p.31 (uₙ₊₁ = uₙ(uₙ − 1) au
tableur, dix mille termes, six valeurs de u₁) ; Act. 3 p.32 (uₙ₊₁ = uₙ(1 − uₙ)) ; Exercice résolu 2 (p.33,
alternée en 1/√n, α ≈ 0,817 [valeur imprimée fausse : 0,817 ≈ u₅ ; α ≈ 0,605 ; erreur du manuel, à ne pas reprendre]) ; Ex. 3 (n(1+(−1)ⁿ)/(n+1), non convergente) ; Ex. 15 (point fixe de
(4x−3)/x, trois cas u₀ = 3/4, 3, 5) ; Ex. 16 (uₙ₊₁ = 5 − 6/uₙ) ; Ex. 17 (aₙ² + aₙ, b₀ = −0,5) ;
démonstrations imprimées du théorème de récurrence et des suites adjacentes (p.32). Le théorème de
convergence monotone tient en un seul encadré (les cas « non majorée/non minorée » y figurent ; la
référence les sépare). Ex. 12, 13, 14, 18, 21, 22 ont leur équivalent dans la référence (Ex. 18, 20, 21,
30, 25, 32).

### Bornes de scope (section Sciences expérimentales)

- ✅ INCLUS : limite via sous-suites paire/impaire (admis) ; suite convergente ⇒ bornée (admis) ;
  opérations sur les limites (tableaux somme, produit, quotient) ; suites géométriques qⁿ (théorème de
  rappel), suites arithmético-géométriques uₙ₊₁ = 2uₙ − 1 et points fixes de f ; composition limite∘suite
  (I ouvert, admis) ; comparaison/encadrement : ≤ ⇒ limites ordonnées, gendarmes, |uₙ| ≤ vₙ → 0,
  minoration/majoration vers ±∞ (tous admis) ; factorielle (10ⁿ/n!, n!/3ⁿ) ; notation Σ et télescopage
  1/(k(k+1)) ; sommes géométriques (Act. 2.3-2.4, Ex. 10) ; convergence monotone (croissante majorée,
  décroissante minorée, non majorée → +∞, non minorée → −∞) ; suites récurrentes uₙ₊₁ = f(uₙ) : point
  fixe a = f(a) si f continue en a (démontré) ; suites adjacentes (définition et démonstration, sous-suites
  paire/impaire de l'alternée en 1/√n) ; approximation à la calculatrice/tableur (dix mille termes,
  n₀ pour 10⁻⁵ ou 10⁻⁶) ; formule du binôme pour (1+a)ⁿ ≥ n(n−1)a²/2 (Ex. 11).
- ⛔ EXCLU : signe de la limite et encadrement m ≤ a ≤ M ; théorème f continue ⇒ f(uₙ) → f(a) (à ne pas
  introduire comme encadré) ; Problème de e (Σ1/k!) et irrationalité ; polygones/approximation de π ;
  suites décimales (0,33…3) ; encadrement de sin x ; partie entière ; (sin(n!πa))ⁿ ; n¹⁰⁰/1,01ⁿ ;
  Héron (E(√a)) ; Wallis ; discussion de aₙ² + aₙ selon a₀ ; ε-définition de la limite (absente) ;
  dérivation uniquement comme outil d'étude de f (Ex. 18, 19), non enseignée ici.

### Lecture

- **Pages lues par l'OCR** : p.23 à p.38 (16 pages, `/root/.cache/yqa-manuels/222433/txt/p023.txt`…`p038.txt`).
- **Pages lues sur l'image** (110 dpi) : p.23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38
  = **16 pages sur 16** ; agrandissements 220 dpi : p.26 (Act. 2-3), p.35 (Ex. 1), p.36 (Ex. 11, 13).
- **Sondage / écarts OCR–image constatés** : toutes les formules de l'OCR sont dégradées (fractions,
  exposants, indices, Σ, racines). Écarts majeurs : p.24 Act. 2-3 (u₂ₙ/u₂ₙ₊₁, (−1)ⁿ/n illisibles) ; p.25
  tableaux de limites aux colonnes mélangées par l'OCR (b ≠ 0, règle des signes) ; p.26 Act. 2 sommes
  « 1 + 5/3 + … » et « −3 − 9/π … » (OCR « 1424 », « -3-?- ») ; p.27 corrigé (raison (1−√3)/(1+√3),
  u₃ = 7/4, figure) ; p.29 Act. 3 : l'OCR donne « √n + cos n », l'image donne 1/(√n + cos²n) ; Act. 4
  exposant n−10 et fraction 10/11 ; p.30 Act. 6 signes de B ; p.33 corrigé de l'Ex. résolu 2 (exposants
  2n+1, 2n+3, α ≈ 0,817 [valeur imprimée fausse : 0,817 ≈ u₅ ; α ≈ 0,605 ; erreur du manuel, à ne pas reprendre]) ; p.34 QCM 2 OCR « n'+cosn » (image : n + cos n) ; p.35–38 la plupart des
  énoncés (OCR « 2 » pour « ≤ », « Ex » et « [22] » pour les numéros d'exercices encadrés). Aucun
  écart de nature à changer le périmètre ; les énoncés du présent fichier sont repris de l'image.
- **Doutes signalés** : α ≈ 0,817 p.33 (Ex. résolu 2 : valeur imprimée fausse, 0,817 ≈ u₅ ; α ≈ 0,605) ; quotient « ∞, b » sans « ≠ 0 »
  p.25 ; Ex. 19 « a » inutilisé avec 5 ; Ex. 20 numérotée 1, 2, 5 ;
  corrigé de l'Ex. résolu 1 p.27 : OCR/image concordent sur « raison et premier terme (1−√3)/(1+√3) ».

## 2.3 Chapitre 3 — Dérivabilité (manuel 222433, p.39–53)

**Page de garde (p.39)** — « Chapitre 3 », titre « Dérivabilité ». Citation liminaire :
« […] Pour résoudre ces équations, il étudie le maximum des expressions algébriques. Il prend
"la dérivée première" de ces expressions qu'il annule et démontre que la racine de l'équation
obtenue, substituée dans l'expression algébrique donne le maximum. […] Et comme la seule
démonstration convaincante est de faire parler le texte même d'Al-Tusi, nous allons prendre trois
exemples dans l'œuvre de ce mathématicien :[…], le troisième, pour dégager comment transformation
affine, divisibilité et dérivée se conjuguent dans la solution de l'équation. »
(« R. Ras hed, Entre Arithmétique et Algèbre, 1984 » — coupure typographique de la source pour
Roshdi Rashed.) Légende : « Sharaf Al-Din Al-Tusi est un mathématicien arabe qui a écrit un traité
mathématique vers 1213. » Illustration : couverture d'un ouvrage.

**Plan (p.40–49)** : I. Rappels (p.40–42) · II. Dérivées successives (p.42) · III. Dérivabilité des
fonctions composées (p.42–43) · IV. Théorème des accroissements finis (p.43–45) · V. Inégalité des
accroissements finis (p.45–46) · VI. Variations d'une fonction (p.46–48) · VII. Extrema (p.48) ·
« VII. Point d'inflexion » (p.49 — numéroté VII une seconde fois dans la source, la numérotation
attendue serait VIII ; signalé tel quel). Puis « QCM - VRAI - FAUX » (p.50) et « Exercices et
problèmes » (p.51–53, 24 exercices). Pas de résumé, pas de partie « exemples d'étude de fonctions »,
pas de réponses.

### Cours — Activités

**I. Rappels** (p.40) — « Dans ce paragraphe nous rappelons les principaux résultats vus en
troisième année. »

- **Act. 1** (p.40) : figure d'une f dérivable sur ℝ (courbe type parabole) avec tangentes aux points
  d'abscisses −2 et 0. 1. nombres dérivés de f en −2 et 0 ; 2. lim_{h→0} (f(h)−1)/h et
  lim_{x→−2} f(x)/(x+2).
- **Act. 2** (p.40) : f(x) = x³+3x²+3x+1, C_f dans (O, i⃗, j⃗) orthonormé. 1. nombre dérivé en 0 et 1 ;
  2. tangentes aux points d'abscisses 0 et 1 ; 3. approximation affine de (1.0002)³ et (2.0001)³.
- **Act. 3** (p.40) : approximation affine de sin(0.0001) et cos(0.0001).
- **Act. 4** (p.40) : f(x) = |x²−1|, C_f. 1. dérivabilité à droite et à gauche en −1, interpréter ;
  2. idem en 1.
- **Act. 5** (p.41) : étudier la dérivabilité de f sur I : x ↦ sin x/(1+cos²x), I = ℝ ;
  x ↦ (1+x+x²)/(1−x²), I = [0, 1/2] ;
  x ↦ x(x+1)/(1−x²), I = [−3, −1[.
- **Act. 6** (p.42) : calculer la dérivée de f en précisant son ensemble de définition et celui de sa
  dérivée : (2−x³)⁴ ; cos x sin⁴x ; (1+x⁴)/(x²−1) ; 1/(x−2)³ + 2/x ; (1+tan²x)tan²x ; tan²x/cos²x.

**II. Dérivées successives** (p.42)

- **Act. 1** (p.42) : dérivées d'ordre 1, 2, 3 et 4 de f : x ↦ 2x³−4x²+x−1 ; x ↦ sin x ; x ↦ cos x.
- **Act. 2** (p.42) : f(x) = 1/(1−x) sur ]1, +∞[. Calculer f′(x), f″(x), f⁽³⁾(x), f⁽⁴⁾(x).

**III. Dérivabilité des fonctions composées** (p.42–43)

- **Act. 1** (p.42) : f(x) = sin x² sur ℝ. 1. lim_{x→0} sin x²/x² ; 2. vérifier que pour x non nul
  (f(x)−f(0))/x = x·sin x²/x², en déduire f dérivable en 0 et f′(0).
- **Act. 2** (p.43) : montrer que f est dérivable sur I et déterminer sa dérivée : f : x ↦ sin x²,
  I = ℝ ; g : x ↦ 1−cos x², I = ℝ ; h : x ↦ sin(1/x), I = ]−∞, 0[.

**IV. Théorème des accroissements finis** (p.43–45)

- **Act. 1** (p.43) : f définie sur [−3, 2], dérivable sur ]−3, 2[ ; courbe C_f avec tangentes aux
  points d'abscisses −2, 0 et 3/2. Lire les abscisses des points où la tangente est parallèle à l'axe
  des abscisses. (Précède Rolle.)
- **Act. 2** (p.44) : f(x) = x⁵−3x⁴−5x³+15x²+4x+2, 𝒞 dans (O, i⃗, j⃗). 1. calculer f(1) et f(−1) ;
  2. en déduire que 𝒞 admet au moins une tangente parallèle à l'axe des abscisses.
- **Act. 3** (p.44) : f(x) = (1/3)x³−x² sur ℝ, 𝒞, A et B points d'abscisses 3 et 1. Existe-t-il des
  points de 𝒞 où la tangente est parallèle à (AB) ? (Précède le TAF.)
- **Act. 4** (p.45) : f(x) = x²√(x−1) sur [1, +∞[, C_f. Montrer que C_f admet au moins une tangente
  parallèle à (AB), A(1, 0) et B(2, 4).

**V. Inégalité des accroissements finis** (p.45–46)

- **Act. 1** (p.45) : f : [0, π/2] → ℝ, x ↦ sin x. 1. 0 ≤ f′(x) ≤ 1 sur [0, π/2] ; 2. en déduire
  0 ≤ sin t ≤ t sur [0, π/2].
- **Exercice résolu** (p.46, avec solution rédigée) : f : x ↦ √(1+x). 1. f dérivable sur [0, 1/2] ;
  2. 1/√6 ≤ f′(x) ≤ 1/2 sur [0, 1/2] ; 3. 1 + t/√6 ≤ √(1+t) ≤ 1 + t/2 sur [0, 1/2] ; 4. en déduire un
  encadrement de √(1+10⁻¹⁰). (Solution : f dérivable là où 1+x > 0 ; f′(x) = 1/(2√(1+x)), 1 ≤ √(1+x)
  ≤ √1.5 ; théorème des inégalités des accroissements finis sur [0, t] ; encadrement 1 + 10⁻¹⁰/√6 ≤
  √(1+10⁻¹⁰) ≤ 1 + 10⁻¹⁰/2.)

**VI. Variations d'une fonction** (p.46–48)

- **Act. 1** (p.46) : graphique d'une f dérivable sur [−7, 7] (plusieurs paliers à tangente horizontale).
  1. intervalles où f est strictement monotone ; 2. signe de f′(x).
- **Act. 2** (p.47) : figure de f(x) = x − sin x sur ℝ. 1. sens de variation graphique ; 2. a. f′ ;
  b. résoudre f′(x) = 0 dans ℝ et interpréter graphiquement.
- **Act. 3** (p.48) : étudier les variations de x ↦ √(1 − sin x) sur [−π/2, π/2].

**VII. Extrema** (p.48)

- **Act. 1** (p.48) : figure d'une f définie sur ]−4, 7[. Déterminer graphiquement les extrema locaux.
- **Act. 2** (p.48) : restriction de f : x ↦ 1−x² à [0, 1], tangente en M d'abscisse a ∈ ]0, 1] (figure
  O, P, Q, M). Déterminer M pour que l'aire du triangle OPQ soit minimale.

**« VII. » (= VIII) Point d'inflexion** (p.49)

- **Act. 1** (p.49) : f(x) = x³−3x+1 sur ℝ, C_f. 1. équation de la tangente T au point d'abscisse 0 ;
  2. position relative de C_f et T ; 3. variations de f puis tracer T et C_f.
- **Act. 2** (p.49) : f(x) = x⁴−6x²+1 sur ℝ, C_f. Montrer que C_f admet deux points d'inflexion que
  l'on précisera.
- **Act. 3** (p.49) : f(x) = 2x − sin x sur ℝ, C_f. 1. variations de f sur [−π/2, 3π/2] ;
  2. points d'inflexion de C_f sur [−π/2, 3π/2].

### Cours — Encadrés / définitions / théorèmes (VERBATIM, vérifiés sur l'image)

> **Encadré — dérivable en un réel** (p.40) — « Une fonction f définie sur un intervalle ouvert I est
> dérivable en un réel a de I s'il existe un réel, noté f′(a) tel que lim_{x→a} (f(x) − f(a))/(x − a) =
> f′(a). »

> **Encadré — fonction polynôme** (p.40) — « Soit f : x ↦ aₙxⁿ + … + a₁x + a₀ une fonction polynôme.
> La fonction f est dérivable en tout réel x et f′(x) = naₙxⁿ⁻¹ + … + a₁. »

> **Encadré — approximation affine** (p.40) — « Si f est dérivable en a, alors le réel f(a) + f′(a)h
> est une approximation affine de f(a + h). »

> **Encadré — dérivabilité à gauche et à droite** (p.40) — « Une fonction f définie sur un intervalle
> ouvert I est dérivable en un réel a de I, si et seulement si, elle est dérivable à gauche et à droite
> en a et f′_g(a) = f′_d(a). »

> **Encadré — dérivable sur un intervalle** (p.41) — « • Une fonction est dérivable sur un intervalle
> ouvert I si elle est dérivable en tout réel de I. • Soit deux réels a et b tels que a < b. Une
> fonction est dérivable sur [a, b] si elle est dérivable sur ]a, b[, à droite en a et à gauche en b.
> • On définit de façon analogue la dérivabilité d'une fonction sur les intervalles [a, b[, ]a, b], a
> et b finis ou infinis. »

> **Tableau — Dérivées des fonctions usuelles** (p.41) — (Fonction f | Intervalle | f′) :
> x ↦ xⁿ, n ∈ ℕ\{0,1} | ℝ | x ↦ nxⁿ⁻¹ ;
> x ↦ 1/xⁿ, n ∈ ℕ* | Tout intervalle inclus dans ℝ* | x ↦ −nx⁻ⁿ⁻¹ ;
> x ↦ sin(ax+b) | ℝ | x ↦ a cos(ax+b) ;
> x ↦ cos(ax+b) | ℝ | x ↦ −a sin(ax+b) ;
> x ↦ tan(ax+b) | Tout intervalle inclus dans l'ensemble de définition de f. | x ↦ a(1 + tan²(ax+b)).
> (Phrase d'introduction : « Nous donnons dans les deux tableaux ci-dessous les dérivées de certaines
> fonctions usuelles, ainsi que les règles opératoires sur les dérivées. »)

> **Tableau — Opérations sur les fonctions dérivables** (p.41) — « Soit f et g deux fonctions
> dérivables sur un intervalle I. » (Fonction | Intervalle | Fonction dérivée) :
> f+g | I | f′+g′ ; af (a ∈ ℝ) | I | af′ ; f×g | I | f′×g+g′×f ;
> 1/f | Tout intervalle inclus dans {x ∈ I ; f(x) ≠ 0} | −f′/f² ;
> f/g | Tout intervalle inclus dans {x ∈ I tel que g(x) ≠ 0} | (f′g − g′f)/g² ;
> fⁿ, n ∈ ℕ\{0,1} | I | nf′fⁿ⁻¹ ;
> 1/fⁿ, n ∈ ℕ* | Tout intervalle inclus dans {x ∈ I ; f(x) ≠ 0} | −nf′f⁻ⁿ⁻¹.

> **Dérivées successives** (p.42) — « Soit f une fonction dérivable sur un intervalle I. La dérivée f′
> de f est appelée la dérivée première de f. Si la fonction f′ est dérivable sur I, sa fonction dérivée
> est appelée dérivée seconde de f et notée f⁽²⁾ ou f″. Par itération, si la fonction f⁽ⁿ⁻¹⁾ (n ≥ 2)
> est dérivable sur I, sa fonction dérivée est appelée dérivée nᵉᵐᵉ de f et est notée f⁽ⁿ⁾. La dérivée
> nᵉᵐᵉ de f est aussi appelée dérivée d'ordre n de f. »

> **Théorème (admis) — dérivabilité d'une composée** (p.43) — « Soit f une fonction définie sur un
> intervalle ouvert I contenant un réel a et g une fonction définie sur un intervalle ouvert J contenant
> f(a). Si f est dérivable en a et g est dérivable en f(a), alors g∘f est dérivable en a et
> (g∘f)′(a) = f′(a) × g′(f(a)). »

> **Corollaire** (p.43) — « Si f est dérivable sur un intervalle I et g est dérivable sur un intervalle
> J contenant f(I), alors g∘f est dérivable sur I et (g∘f)′(x) = f′(x) × g′[f(x)], pour tout x de I. »

> **Théorème de Rolle** (p.43) — « Soit a et b deux réels tels que a < b. Soit f une fonction continue
> sur [a, b] dérivable sur ]a, b[ et telle que f(a) = f(b). Alors il existe un réel c de ]a, b[ tel que
> f′(c) = 0. » — « Si C_f est la représentation graphique de f dans un repère (O, i⃗, j⃗), alors il
> existe au moins une tangente à C_f parallèle à l'axe des abscisses. »
> **Démonstration** (p.44) : « Si f est constante sur [a, b], le résultat est immédiat. Supposons f non
> constante sur [a, b]. La fonction f étant continue sur [a, b], elle est bornée et atteint ses bornes
> m et M. Soit x₀ et x₁ tels que m = f(x₀) et M = f(x₁). Alors l'un des réels x₀ ou x₁ appartient à
> ]a, b[, car f n'est pas constante sur [a, b]. On en déduit que f′(x₀) = 0 ou f′(x₁) = 0. Le théorème
> en découle. »

> **Théorème des accroissements finis** (p.44) — « Soit a et b deux réels tels que a < b et f une
> fonction définie sur [a, b]. Si f est continue sur [a, b] et dérivable sur ]a, b[, alors il existe un
> réel c de ]a, b[ tel que f(b) − f(a) = f′(c)(b − a). » — « Si C_f est la représentation graphique de
> f dans un repère (O, i⃗, j⃗) alors il existe au moins une tangente à C_f parallèle à la droite (AB) où
> A et B sont les points de C_f d'abscisses respectives a et b. »
> **Démonstration** (p.45) : « Considérons la fonction g définie sur [a, b] par
> g(x) = f(x) − ((f(b) − f(a))/(b − a))(x − a). D'après l'hypothèse faite sur f, la fonction g est
> continue sur [a, b], dérivable sur ]a, b[ et vérifie g(a) = g(b). On déduit du théorème de Rolle,
> l'existence d'un réel c de ]a, b[ tel que g′(c) = 0. Le théorème en découle. »

> **Théorème — inégalité des accroissements finis** (p.45) — « Soit f une fonction continue sur [a, b]
> (a < b) et dérivable sur ]a, b[. Soit deux réels m et M. Si m ≤ f′(x) ≤ M pour tout x de ]a, b[,
> alors m(b − a) ≤ f(b) − f(a) ≤ M(b − a). »
> **Démonstration** (p.45) : « Le théorème des accroissements finis justifie l'existence d'un réel c de
> ]a, b[ tel que f(b) − f(a) = f′(c)(b − a). L'hypothèse faite sur f′ permet de déduire que
> m ≤ f′(c) ≤ M. Ce qui implique que m(b − a) ≤ f′(c)(b − a) ≤ M(b − a), car b − a > 0. Le théorème
> en découle. »

> **Corollaire** (p.45) — « Soit f une fonction dérivable sur un intervalle I et M > 0. Si |f′(x)| ≤ M
> pour tout x de I, alors |f(b) − f(a)| ≤ M|b − a|, pour tous réels a et b de I. »

> **Théorème — signe de f′ strict** (p.47) — « Soit f une fonction dérivable sur un intervalle I. Si la
> dérivée de f est strictement positive sur I, alors la fonction f est strictement croissante sur I.
> Si la dérivée de f est strictement négative sur I, alors la fonction f est strictement décroissante
> sur I. »
> **Démonstration** (p.47) : « Supposons que f′(x) > 0 pour tout x de I et considérons deux réels a et
> b de I tels que a < b. La fonction f étant dérivable sur I, elle est dérivable sur [a, b]. D'après le
> théorème des accroissements finis, il existe un réel c de ]a, b[ tel que f(b) − f(a) = f′(c)(b − a).
> On en déduit que f(b) − f(a) > 0, car f′(c) et b − a sont strictement positifs. Ce qui prouve que f
> est strictement croissante sur I. La deuxième propriété découle de la première en considérant la
> fonction −f. »

> **Théorème — f′ de signe large** (p.47) — « Soit f une fonction dérivable sur un intervalle I. Si f′
> est positive et ne s'annule sur aucun intervalle ouvert contenu dans I, alors f est strictement
> croissante sur I. Si f′ est négative et ne s'annule sur aucun intervalle ouvert contenu dans I, alors
> f est strictement décroissante sur I. »
> **Démonstration** (p.47) : « De l'hypothèse f′(x) ≥ 0 pour tout réel x de I, il résulte que la
> fonction f est croissante sur I. Supposons qu'il existe deux réels a et b tels que a < b et
> f(a) = f(b). Il en résulte que f(a) ≤ f(x) ≤ f(b), pour tout réel x de ]a, b[. Par suite f est
> constante sur [a, b] et f′(x) = 0 pour tout x de ]a, b[. Ce qui contredit l'hypothèse faite sur f′.
> La deuxième propriété découle de la première en considérant la fonction −f. »

> **Théorème — prolongement aux bornes** (p.48) — « Soit f une fonction continue sur un intervalle
> [a, b] et dérivable sur ]a, b[. • Si f est croissante (respectivement strictement croissante) sur
> ]a, b[ alors f est croissante (respectivement strictement croissante) sur [a, b]. • Si f est
> décroissante (respectivement strictement décroissante) sur ]a, b[ alors f est décroissante
> (respectivement strictement décroissante) sur [a, b]. »
> **Démonstration** (p.48) : « Soit c < d deux réels de [a, b]. La fonction f étant continue sur [c, d]
> et dérivable sur ]c, d[, il existe un réel x₀ de ]c, d[ tel que f(d) − f(c) = (d − c)f′(x₀). Le
> théorème en découle. »

> **Encadré — extrema locaux (définitions)** (p.48, sans titre) — « Soit f une fonction définie sur un
> intervalle I et a un réel de I. On dit que f admet un maximum local en a, s'il existe un intervalle
> ouvert J contenant a et inclus dans I tel que pour tout x de J, f(x) ≤ f(a). On dit que f admet un
> minimum local en a, s'il existe un intervalle ouvert J contenant a et inclus dans I tel que pour tout
> x de J, f(x) ≥ f(a). Lorsque f admet un minimum local ou un maximum local en a on dit que f admet un
> extremum local en a. »

> **Encadré — extrema locaux et dérivée** (p.48, sans titre) — « Soit f une fonction dérivable sur un
> intervalle ouvert I et a un réel de I. Si f admet un extremum local en a alors f′(a) = 0. Si f′(x)
> s'annule en a en changeant de signe alors f admet un extremum local en a. »

> **Définition — point d'inflexion** (p.49) — « Soit f une fonction définie sur un intervalle ouvert I
> et dérivable en un réel a de I et C_f sa courbe dans un repère orthogonal (O, i⃗, j⃗). On dit que le
> point A(a, f(a)) est un point d'inflexion de C_f si C_f traverse sa tangente en ce point. »

> **Théorème (admis) — critère d'inflexion** (p.49) — « Soit f une fonction deux fois dérivable sur
> ]a − h, a + h[, (h > 0) et C_f sa représentation graphique dans un repère orthonormé. Si la fonction
> dérivée seconde f″ de f s'annule en a en changeant de signe, alors le point I(a, f(a)) est un point
> d'inflexion de la courbe C_f. »

### QCM – VRAI – FAUX (p.50) — réponses non fournies

**QCM** (« Cocher la réponse exacte. »)
1. x ↦ cos(πx²) dérivable sur ℝ, dérivée : [x ↦ 2π sin(πx²)] / [x ↦ 2πx sin(πx²)] /
   [x ↦ −2πx sin(πx²)] (première proposition imprimée sans le facteur x, tel quel).
2. f dérivable sur [−2, 2], tableau de variation de f′ : x = −2, −1, 0, 1, 2 ; f′ vaut 1 en −2, 0 en
   −1, −2 en 0, −1 en 1, −1/4 en 2 (valeurs lues sur la flèche du tableau, fraction −1/4 vérifiée en
   zoom). « Alors » f(−2) < f(−1) / f(−1) < f(0) / f(0) < f(1). Puis : « la courbe de f admet
   exactement deux tangentes parallèles à la droite d'équation » y = −1/2 / y = (1/2)x / y = −(1/2)x.
3. L'image de [1, +∞[ par x ↦ √(x²−1) − 1 est : [0, +∞[ / [−1, +∞[ / ]−∞, 0].
4. La courbe de x ↦ (1/20)x⁵ − 4x² admet un point d'inflexion d'abscisse : x = 0 / x = −2 / x = 2.
5. f(x) = (x−1)(x−2)(x−3) sur ℝ ; la courbe admet exactement : deux tangentes horizontales / une
   tangente horizontale / aucune tangente horizontale.

**VRAI – FAUX** (« Répondre par vrai ou faux en justifiant la réponse. »)
1. f dérivable sur [−1, 2], f(−1) = 2, f(2) = −1 : l'équation f′(x) = −1 admet au moins une solution
   dans [−1, 2].
2. Si le produit de deux fonctions est dérivable en un réel a alors chacune des deux fonctions est
   dérivable en a.
3. f : x ↦ (x²−x)(x−2) : la courbe (repère orthogonal) admet exactement deux tangentes horizontales.
4. f dérivable sur [2, 5], |f′(t)| ≤ 2 pour t ∈ [2, 5] : alors |f(5) − f(2)| ≤ 6.

### Exercices et problèmes (p.51–53) — 24 exercices (une ligne chacun)

- **Ex. 1** (p.51) : justifier la dérivabilité de f en a et donner l'équation de la tangente :
  (x+1)/(x−1), a = 2 ; 0.25x⁴+0.5x³−x, a = 0 ; √(x²−4), a = −3 ; √|2x+1|, a = −1.
- **Ex. 2** (p.51) : par la définition de la dérivabilité, calculer lim_{x→1} (√(x+1)−√2)/(x−1) ;
  lim_{x→3} (x−√(x−2)−2)/(x−3) ; lim_{x→0} ((x+1)¹⁹⁵−1)/x ; lim_{x→1} (x⁵+x⁴+x³+x²−4)/(x−1).
- **Ex. 3** (p.51) : f(x) = |x²−4|. 1. dérivabilité en 2 et −2 ; 2. construire les demi-tangentes aux
  points d'abscisses 2 et −2.
- **Ex. 4** (p.51) : 1. approximation affine de 1/(1+h)², h voisin de 0 ; 2. en déduire une estimation
  de 1/(1.0000000002)² et 1/(0.9999999998)².
- **Ex. 5** (p.51) : vérifier que f est dérivable sur I et déterminer f′ : 3x¹⁰−(5/4)x⁸+3x−10 (ℝ) ;
  (1−x−3x³)(x+2x)³ (ℝ, énoncé imprimé tel quel) ; x²/(1−x) (]1,+∞[) ; (x+1)³/x² ([1,+∞[) ;
  cos(3x)−sin(2x) (ℝ) ; sin x/(1−cos x) (]0,π]) ; (1+sin 2x)³ (ℝ) ; tan²((π/2)x) ([0,1[) ;
  √((x−1)/(x+1)) (]1,+∞[) ; (√x−2)/(√x+2) (]0,+∞[).
- **Ex. 6** (p.51) : f(x) = x³−3x, g(x) = x−4/x, courbes 𝒞 et 𝒞′. 1. 𝒞 et 𝒞′ ont deux points communs
  A et B ; 2. en chacun, même tangente aux deux courbes, en donner une équation.
- **Ex. 7** (p.51) : f(x) = √(−x−1) si x < −1 ; x²−1 si −1 ≤ x ≤ 1 ; 2 sin(x−1) si x > 1. 1. continuité
  en −1 et 1 ; 2. dérivabilité en −1 et 1 ; 3. f dérivable sur ]−∞,−1[, ]−1,1[ et ]1,+∞[.
- **Ex. 8** (p.51) : dérivées successives de x⁵−2x³+3x+4 ; cos x + sin x ; sin 2x ; 1/(x−1) + 1/(x+1),
  x > 1.
- **Ex. 9** (p.52) : vérifier la dérivabilité sur I et déterminer f′ : √(sin x), I = ]0, π/2] ;
  sin(π/x), I = [1, +∞[ ; tan(sin x), I = ℝ. (Numérotation imprimée 2, 3, 4 : l'item « 1. » est
  absent de la page, sans doute une omission d'impression.)
- **Ex. 10** (p.52) : f(x) = (x²−3x+6)/(x−1), 𝒞. 1. 𝒞 admet deux tangentes parallèles à y = −3x ;
  2. coordonnées des points de contact et équation de chaque tangente.
- **Ex. 11** (p.52) : f(x) = x³−3x+2 sur [1, 2], A et B d'abscisses 1 et 2. Points de 𝒞 où la tangente
  est parallèle à (AB).
- **Ex. 12** (p.52) : f(x) = (x−1)(x−2)(x−3)(x−4). Sans calculer f′(x), montrer que f′ admet trois
  zéros distincts.
- **Ex. 13** (p.52) : f : x ↦ tan x. 1. 1 ≤ f′(x) ≤ 2 sur [0, π/4] ; 2. en déduire x ≤ tan x ≤ 2x sur
  [0, π/4].
- **Ex. 14** (p.52) : 1. par l'inégalité des accroissements finis, 0 ≤ √(1+x) − 1 ≤ x/2, x ≥ 0 ;
  2. en déduire que pour x > 0, x ≤ √(1+x²) ≤ x + 1/(2x).
- **Ex. 15** (p.52) : montrer a. |sin x| ≤ |x|, x ∈ ℝ ; b. x ≤ tan x, x ∈ [0, π/2[ ;
  c. 1−x ≤ cos x ≤ 1+x, x ∈ [0, +∞[.
- **Ex. 16** (p.52) : f : x ↦ (x−1)√(1−x). 1. ensemble de définition ; 2. dérivabilité en 1,
  interpréter ; 3. tableau de variation.
- **Ex. 17** (p.52) : f(x) = 1/√(1+x) sur ℝ₊. 1. f dérivable sur ℝ₊ et |f′(x)| ≤ 1/2, x ≥ 0 ;
  2. pour x ≥ 0, 1 − x/2 ≤ 1/√(1+x) ≤ 1 + x/2 (borne droite lue sur l'image à 200 dpi) ;
  3. en déduire un encadrement de 1/√(1+10⁻¹¹).
- **Ex. 18** (p.52) : f(x) = x³−x. 1. variations de f ; 2. comparer A et B : a. A = 0.577350269³ −
  0.577350269, B = 0.577350268³ − 0.577350268 ; b. A = 0.577350271³ − 0.577350271,
  B = 0.577350272³ − 0.577350272.
- **Ex. 19** (p.53) : variations de f sur I : √(x+1) − √(x−1), [1, +∞[ ; cos x − sin x, [0, π] ;
  cos(sin x), [0, π].
- **Ex. 20** (p.53) : f(x) = 4√(x+1) si x ≥ 3 ; x²−5x+c si x < 3. 1. c pour f continue sur ℝ, puis f
  dérivable sur ℝ et f′ ; 2. tableau de variation ; 3. préciser l'extremum de f.
- **Ex. 21** (p.53) : f : x ↦ x√(1−x²), 𝒞. 1. ensemble de définition ; 2. lim_{x→1⁻} (f(x)−f(1))/(x−1),
  conséquence pour la courbe en x = 1 ; 3. a. f impaire, b. tableau de variation, c. extrema ;
  4. a. tangente en 0, b. l'origine est un point d'inflexion de 𝒞.
- **Ex. 22** (p.53) : f(x) = x√x − (3/16)x², x > 0. 1. a. f dérivable sur [0, +∞[ et
  f′(x) = (12√x − 3x)/8, b. variations, c. existe-t-il x ≥ 0 tel que x√x − (3/16)x² = 20 ;
  2. a. f deux fois dérivable sur ]0, +∞[, b. point d'inflexion de 𝒞.
- **Ex. 23** (p.53) : f : x ↦ √(x+√x). 1. ensemble de définition ; 2. dérivabilité à droite en 0,
  interpréter ; 3. a. f dérivable sur ]0, +∞[ et f′(x), b. tableau de variation.
- **Ex. 24** (p.53) : f : x ↦ (1/2)(4 + sin x). 1. |f′(x)| ≤ 0.5, x ∈ ℝ ; 2. a. g : x ↦ f(x) − x
  strictement décroissante sur ℝ, b. 3/2 − x ≤ g(x) ≤ 5/2 − x, c. lim_{+∞} g, lim_{−∞} g, g(ℝ),
  d. unique a tel que f(a) = a et 2π/3 < a < 5π/6 ; 3. suite u₀ donné, u_{n+1} = f(uₙ) : a. |u_{n+1}−a| ≤
  0.5|uₙ−a|, b. |uₙ−a| ≤ (0.5)ⁿ|u₀−a|, c. lim uₙ.

### Écart avec la référence (chapitre math-bac-math 03-derivabilite, manuel 222445)

**À EXCLURE — la référence l'enseigne, ce manuel non** :
- Activité « racine double d'un polynôme » (réf. Act. 6 p.56 : P(α) = P′(α) = 0, P″(α) ≠ 0,
  factorisation de x⁴−4x³+5x²−4x+4) : absente.
- Partie IX « Exemples d'étude de fonctions » et les 3 « problèmes résolus » (réf. p.64–69) : absente ;
  aucune étude complète guidée de fonction (limites, asymptotes, branches infinies, tracé), aucune
  rubrique « Résumé ».
- Centre de symétrie O′(a, b) (réf. Act. 2 p.63 et encadré 2a−x ∈ D, f(2a−x) = 2b−f(x)) : absent.
- Activité « point d'inflexion et dérivée seconde » en mode démonstration (réf. Act. 3 p.63–64,
  φ(x) = f(x) − [f′(a)(x−a)+f(a)]) : absente ; ici le critère f″ est seulement admis.
- Composée : activité de la réf. (√(1−x²), h(t) = f(sin t), dérivabilité à gauche en 1) et démonstration
  par fonction auxiliaire φ de l'admis : absentes ; le théorème est « admis » sans démonstration.
- Activités d'approximation par encadrement de sin/cos et φ(x) = (x−sin x)/x dérivable en 0 (réf. V Act. 3),
  tan x ≤ 2x type 1 ≤ f′ ≤ 2 seulement en Ex. 13.
- Exercices de la réf. sans équivalent ici : dérivée n-ième générale (f⁽ⁿ⁾ = (−1)ⁿ n!/(x−2)ⁿ⁺¹), décomposition
  en éléments simples (réf. Ex. 6), limites par f(√(2+x))/(x−2), polynôme de degré 3 à jets donnés,
  x²sin(1/x) dérivable non C¹, lecture graphique de limites (asymptotes), 14 études de fonctions
  (Ex. 22–36 réf.), tangentes passant par l'origine, f ayant n+1 zéros ⇒ f⁽ⁿ⁾ s'annule, suites
  récurrentes à équation x³−10x²−1 = 0, suite uₙ = Σ1/k³, suite aₙ de x²+x³ = n, tan(uₙ), x√|x²−x|
  et gₙ(x) = xⁿ√(x(1−x)), sin(sin x).
- Qualification « f dérivable ⇒ f continue » : non encadrée ici (la continuité y est seulement utilisée,
  Ex. 7 et 20) ; à ne pas inventer.
- Référence TECH (222451) : problèmes d'optimisation (coût, volume, aire) absents ; ici seule l'Act. 2
  p.48 (aire du triangle OPQ minimale) et l'Ex. 22 y ressemblent faiblement.

**EN PLUS dans ce manuel** (absent ou non repéré dans la référence) :
- Rolle présenté avec démonstration (cohérent avec la réf.) et TAF démontré ; IAF démontrée par le TAF ; corollaire
  |f(b)−f(a)| ≤ M|b−a| énoncé sans démonstration.
- Cours : « Exercice résolu » unique (p.46, √(1+x)) ; théorème « prolongement aux bornes »
  (p.48) avec démonstration ; démonstration de « f′ ≥ 0 ne s'annulant sur aucun intervalle ouvert ».
- Page de garde avec citation sur Al-Tusi (la citation de la réf. est la même ; illustration différente).
- Activité 6 de la partie I (six dérivées avec ensembles de définition de f et de f′).
- Exercices : f continue puis dérivable par paramètre c (Ex. 20), dérivée et tangente de |x²−4| / demi-tangentes
  (Ex. 3), dérivées de produits de sin/cos de x² (Ex. 9, 5), comparaison de nombres décimaux par
  variations de x³−x (Ex. 18), une seule suite à rayon contractant 0.5 (Ex. 24, via f(x) = ½(4+sin x)).
- Ex. 7 (f à trois branches) et Ex. 21 (impaire, tangente et inflexion à l'origine) sont des
  « mini-études » absentes de la référence sous cette forme.

### Bornes de scope

- ✅ INCLUS : rappels de 3ème année (nombre dérivé, approximation affine, dérivabilité à gauche/à droite
  et sur un intervalle, dérivées usuelles xⁿ, 1/xⁿ, sin/cos/tan(ax+b), opérations) ; dérivées successives
  et dérivée n-ième ; dérivabilité d'une composée (théorème admis + corollaire) ; théorème de Rolle ;
  théorème des accroissements finis ; inégalité des accroissements finis + corollaire |f(b)−f(a)| ≤ M|b−a| ;
  lien signe de f′ / variations (f′ > 0 ; f′ ≥ 0 ne s'annulant sur aucun intervalle ouvert ; prolongement
  à [a, b]) ; extrema locaux (définitions, f′(a) = 0, changement de signe) ; point d'inflexion (définition
  « C_f traverse sa tangente », critère f″ s'annule en changeant de signe, admis) ; dérivabilité d'une
  fonction définie par morceaux (paramètre c) ; encadrements numériques par l'IAF ; tangente et demi-tangente
  d'une courbe ; une application à une suite uₙ₊₁ = f(uₙ) (Ex. 24).
- ⛔ EXCLU : racine double d'un polynôme ; centre de symétrie ; démonstration du critère d'inflexion par
  φ ; études complètes de fonctions avec limites infinies, asymptotes obliques/branches paraboliques
  (aucun exemple résolu ni exercice dédié dans ces pages) ; formule générale f⁽ⁿ⁾ pour 1/(x−a) ;
  décomposition en éléments simples ; lecture graphique de limites ; problèmes d'optimisation (hors Act. 2
  p.48) ; fonctions réciproques, ln, exp, primitives, intégrales ; convexité formelle (vocabulaire convexe/
  concave non utilisé) ; formule de Taylor-Lagrange ; dérivabilité d'une fonction implicite ou paramétrique.
  Rien de hors-chapitre n'est à ajouter. Point de doute : la présence ou non d'une démonstration de
  « dérivable ⇒ continue » ne se constate pas dans ces pages.

### Lecture

- **Pages lues par l'OCR** (texte p039–p053, 15 pages) : toutes les 15 pages (39–53) ; l'OCR n'a servi
  qu'à la prose et au repérage.
- **Pages lues sur l'image** (110 dpi) : **15 pages sur 15** — p.39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
  49, 50, 51, 52, 53 (toute page contient formule, encadré, tableau ou figure). Zooms 200–220 dpi :
  p.50 (tableau de variation de f′ du QCM 2), p.52 (Ex. 9 en-tête et Ex. 17).
- **Sondage image ≥ 1/10 parmi les plus denses** : fait sur l'intégralité (15/15). Écarts OCR/image
  constatés : p.39 « ls maximum », « substitnée », « troïs », « Ras bed » (image : « le maximum »,
  « substituée », « trois », « Ras hed ») ; p.40 Act. 4 f(x) = |x²−1| illisible en OCR, Act. 1 limites
  dégradées ; p.41 tableaux entiers dégradés (colonnes, exposants, I = [3,−1[ vs [−3,−1[) ;
  p.42 Act. 6 : fonctions illisibles en OCR (« 2-x » de (2−x³)⁴, tan²x/cos²x), Act. 2 OCR « 1/x » vs
  image 1/(1−x) sur ]1,+∞[, Act. 1 de la partie II OCR « sinx » vs cos x ajouté ; p.43 Act. 2 h : OCR
  « sinl » vs sin(1/x), figure de l'Act. 1 en image seulement ; p.44 Act. 2–3 exposants perdus ;
  p.45 Act. 1 OCR « sinx » avec domaine [0, π/2] cassé ; p.46 solution et encadrements dégradés ;
  p.47–48 intervalles et conditions des théorèmes dégradés en OCR (« Ja, b[ ») ; p.50 QCM : valeurs du
  tableau de variation lues « 1 / 0 / −2 / −1 / −1/4 » (OCR : « −1 » et « 4 » séparés), 1re proposition
  du QCM 1 sans facteur x ; p.51 Ex. 5.2 « (x+2x)³ » imprimé tel quel ; p.52 Ex. 9 item « 1. » absent
  sur l'image ; Ex. 17 borne droite 1 + x/2 ; p.53 Ex. 20 4√(x+1) (radical sur x+1, zoom 300 dpi) et Ex. 24 à vérifier au calcul
  (2π/3 < a < 5π/6 lu sur l'image).

## 2.4 Chapitre 4 — Fonctions réciproques (manuel 222433, p.54–66)

**Page de garde (p.54)** — Titre « Fonctions réciproques », Chapitre 4. Citation liminaire
(« J.Dieudonné, Abrégé d'Histoire des Mathématiques, 1978 ») : le 29 novembre 1873 Cantor écrit à Dedekind
pour lui « soumettre une question […] à laquelle je ne puis répondre » (existence d'une bijection entre ℕ et ℝ) ;
sa lettre du 7 décembre 1873 contient la première démonstration de la non-existence d'une bijection entre ℕ et
]0, 1[ ; le 20 juin 1877 Cantor envoie à Dedekind sa première démonstration de la bijection entre [0, 1] et
[0, 1]×[0, 1] (« je le vois, mais je ne le crois pas »). Texte identique à la référence (222445).

**Plan** : I. Définition (p.55–57) · II. Fonction réciproque d'une fonction strictement monotone (p.57–59) ·
III. Fonction x ↦ ⁿ√x, n ≥ 2 (p.59–60) · QCM – VRAI-FAUX (p.61) · Exercices et problèmes (p.62–66, 24 exercices).
Pas de partie IV (ⁿ√(u(x))), pas d'« exercices résolus ».

### Cours — Activités

**I. Définition**
- **Activité 1** (p.55) : g(x) = x² + 3 sur ℝ. 1.a. déterminer g([0, +∞[) ; b. pour tout y de [3, +∞[,
  g(x) = y admet une unique solution dans [0, +∞[ (à déterminer). 2. h(x) = √(x − 3) sur [3, +∞[ : pour tout y de
  [0, +∞[, h(x) = y admet une unique solution dans [3, +∞[. 3. déterminer g∘h et h∘g.
- **Activité 2** (p.55–56) : parmi f_i, i ∈ {1,2,3,4}, représentées (4 figures), identifier celles qui réalisent une
  bijection de I sur f_i(I). Figures : ① I = [−5, 2], f₁(I) = [−2, 3] ; ② I = [−6, 4], f₂(I) = [−3, 4] ;
  ③ I = ]−4, 4[, f₃(I) = ]−4, 4[ ; ④ I = [−2, 3[, f₄(I) = ]−3, 1]. (Lecture des courbes sur l'image : ① non monotone,
  ② strictement décroissante, avec un point à tangente horizontale vers (−2, 1), sans palier ; ③ croissante avec un palier constant y = 2 ; ④ décroissante.)
- **Activité 3** (p.56) : figure d'une bijection de [−2, +∞[ sur [−1, +∞[ ; déterminer f⁻¹(−1), f⁻¹(1), f⁻¹(3).
- **Activité 4** (p.57) : 1. f : x ↦ 1/x — a. bijection de ℝ*₊ sur ℝ*₊ ; b. expliciter f⁻¹(x). 2. g : x ↦ √(1 + x²) —
  a. bijection de ℝ₊ sur [1, +∞[ ; b. déterminer g⁻¹.
- **Représentation graphique de f⁻¹** (p.57, texte + figure) : C₁, C₂ courbes de f et f⁻¹ en repère orthonormé ;
  M₁(x, y), M₂(y, x) symétrique par rapport à Δ : y = x ; M₁(x, y) ∈ C₁ ⟺ {y = f(x), x ∈ I} ⟺ {x = f⁻¹(y), y ∈ J} ⟺ M₂ ∈ C₂.
- **Activité 5** (p.57) : figure des courbes de deux bijections f (sur [0, 7]) et g (sur [−2, 5]) et de leurs
  réciproques ; identifier la courbe de chacune de f, f⁻¹, g, g⁻¹.

**II. Fonction réciproque d'une fonction strictement monotone**
- **Activité 1** (p.58) : f(x) = sin x sur [−π/2, π/2]. 1. f admet une réciproque f⁻¹ continue sur un intervalle J à
  préciser ; 2. valeurs de f⁻¹(1/2), f⁻¹(−√3/2), f⁻¹(√2/2), f⁻¹(1).
- **Activité 2** (p.58) : f(x) = x/(1 + x²) sur [1, +∞[. 1. bijection de [1, +∞[ sur un intervalle J à préciser ;
  2. expliciter f⁻¹(x), montrer que f⁻¹ est dérivable sur ]0, 1/2[ ; 3. avec f∘f⁻¹(y) = y, pour y ∈ ]0, 1/2[, montrer que
  (f⁻¹)′(y) = 1/f′(f⁻¹(y)).
- **Activité 3** (p.59) : figure d'une bijection f de [−6, 5] sur [−4, 4] avec tangentes aux points d'abscisses −4, −2,
  −1 ; étudier la dérivabilité de f⁻¹ aux points d'abscisses −2, 0 et 1.
- **Activité 4** (p.59) : f(x) = cos x sur [0, π], C_f en repère orthonormé. 1. tracer C_f ; 2. f bijection de [0, π] sur
  [−1, 1] ; 3. dérivabilité de f⁻¹ en 0, calculer (f⁻¹)′(0) ; 4. C_{f⁻¹} courbe de f⁻¹ : que dire des demi-tangentes à
  C_{f⁻¹}, à droite en −1 et à gauche en 1 ? 5. tracer la courbe de f⁻¹ dans le même repère.

**III. Fonction x ↦ ⁿ√x, n ≥ 2**
- **Activité 1** (p.60) : écrire plus simplement ⁶√64, ⁶√(2⁻¹²), √(∛729), ∛(2⁶·3³), ⁸√16/⁸√81, ∛(2√2).
- **Activité 2** (p.60) : 1. comparer ⁶√(2⁴) et ⁴√(2³) ; 2. pour x ≥ 0, comparer ⁶√(x⁴) et ⁴√(x³).
- **Activité 3** (p.60) : étudier la dérivabilité à droite en 0 de x ↦ ⁿ√x, n ≥ 2. Interpréter.
- **Activité 4** (p.60) : étudier et représenter les fonctions x ↦ ∛x ; x ↦ ⁴√x ; x ↦ ⁶√x.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur l'image)

> **Définition — bijection** (p.55) — « Soit I un intervalle de ℝ et f une fonction définie sur I. On dit que f réalise
> une bijection de I sur f(I) (ou que f est une bijection de I sur f(I)), si pour tout y de f(I), l'équation f(x) = y
> admet une unique solution dans I. »

> **Théorème — monotonie stricte ⇒ bijection** (p.55) — « Si f est une fonction strictement monotone sur un intervalle I,
> alors f réalise une bijection de I sur f(I). » (Démonstration : existence par définition de f(I), unicité par la
> stricte monotonie de f.)

> **Définition — fonction réciproque** (p.56) — « Soit f une bijection d'un intervalle I sur f(I). On appelle fonction
> réciproque de f et on note f⁻¹ la fonction définie sur f(I) qui à tout y de f(I) associe l'unique solution dans I de
> l'équation f(x) = y. »

> **Conséquence** (p.56) — « Soit f une bijection d'un intervalle I sur f(I) et f⁻¹ sa fonction réciproque.
> Pour tout x de I et tout y de f(I), f(x) = y, si et seulement si, f⁻¹(y) = x.
> f⁻¹∘f(x) = x, pour tout x de I et f∘f⁻¹(y) = y, pour tout y de f(I). »

> **Conséquence — symétrie des courbes** (p.57) — « Les courbes respectives d'une bijection f et de sa réciproque f⁻¹
> dans un repère orthonormé sont symétriques par rapport à la droite d'équation y = x. »

> **Théorème — réciproque d'une fonction strictement monotone** (p.57) — « Si f est une fonction continue et strictement
> monotone sur un intervalle I alors sa réciproque f⁻¹ est continue et strictement monotone sur l'intervalle f(I) et
> varie dans le même sens que f. » (Démonstration p.58 : la continuité de f⁻¹ est admise ; stricte croissance établie par
> l'absurde pour f strictement croissante.)

> **Théorème — dérivée de la réciproque en un point** (p.58) — « Soit f une bijection d'un intervalle ouvert I sur f(I),
> a un réel de I et b = f(a). Si f est dérivable en a et si f′(a) ≠ 0, alors f⁻¹ est dérivable en b et
> (f⁻¹)′(b) = 1/f′(a). » (Démonstration par le taux d'accroissement, p.58–59 ; f⁻¹ continue en b. Aucune remarque sur les
> dérivées à droite/à gauche.)

> **Corollaire — dérivée de la réciproque sur f(I)** (p.59) — « Soit f une bijection d'un intervalle I sur f(I).
> Si f est dérivable sur I et f′(x) ≠ 0 pour tout x de I, alors f⁻¹ est dérivable sur f(I) et
> (f⁻¹)′(y) = 1/f′[f⁻¹(y)], pour tout y de f(I). »

> **Théorème et définition — fonction racine nᵉᵐᵉ** (p.59) — « Soit n un entier supérieur ou égal à 2.
> La fonction x ↦ xⁿ réalise une bijection de ℝ₊ sur ℝ₊. Elle admet une fonction réciproque strictement croissante de
> ℝ₊ sur ℝ₊, appelée fonction racine nᵉᵐᵉ. » (Figure : y = x³, y = x², y = √x, y = ∛x.)

> **Notation** (p.60) — « L'image d'un réel positif x par la fonction racine nᵉᵐᵉ est noté ⁿ√x et se lit « racine nᵉᵐᵉ de x ».
> Lorsque n = 2 et pour x positif ²√x = √x. »

> **Conséquence** (p.60) — « Pour tous réels positifs x et y, y = xⁿ, si et seulement si, x = ⁿ√y. »

> **Conséquence — opérations sur les radicaux** (p.60) — « Soit deux entiers n et p tels que n ≥ 2 et p ≥ 2 et deux réels
> positifs a et b. Alors ⁿ√(aⁿ) = a ; (ⁿ√a)ⁿ = a ; ⁿ√(a·b) = ⁿ√a·ⁿ√b ; ⁿ√(a/b) = ⁿ√a/ⁿ√b, b ≠ 0 ; ⁿ√a = ⁿᵖ√(aᵖ) ;
> (ⁿ√a)ᵖ = ⁿ√(aᵖ) ; ⁿ√(ᵖ√a) = ⁿᵖ√a. » (Précédée de : « Les opérations sur les radicaux découlent immédiatement de la
> définition de la fonction racine nᵉᵐᵉ. »)

> **Théorème — dérivée de x ↦ ⁿ√x** (p.60) — « Pour tout entier n ≥ 2, la fonction f : x ↦ ⁿ√x est continue sur [0, +∞[ et
> dérivable sur ]0, +∞[. De plus, f′(x) = 1/(n·(ⁿ√(xⁿ⁻¹))), pour tout x > 0. » (Démonstration : g : x ↦ xⁿ dérivable sur ℝ₊, de
> dérivée ne s'annulant pas sur ℝ*₊, donc sa réciproque est dérivable sur ℝ*₊ ; (g⁻¹)′(x) = 1/g′(g⁻¹(x)) = 1/(n(ⁿ√x)ⁿ⁻¹) =
> 1/(n·ⁿ√(xⁿ⁻¹)), x > 0.)

### QCM – VRAI-FAUX (p.61) — réponses non fournies

QCM « Cocher la réponse exacte. » : 1. f = sin sur ℝ réalise une bijection de I sur [−1, 1] où ☐ I = [0, 2π] / ☐ I = [0, π] /
☐ I = [−π/2, π/2]. 2. f = cos sur [0, π] : (f⁻¹)′(1/2) est égal à ☐ 2/√3 / ☐ −2 / ☐ −2/√3. 3. f de représentation graphique
donnée (segment croissant de (1,1) à (2,2), segment décroissant de (2,4) à (4,2), f réalise une bijection de ☐ [1,4] sur [1,4] /
☐ [1,2] sur [1,2] / ☐ [1,3] sur [1,3]. 4. f : x ↦ ∛x est dérivable sur ☐ [0, +∞[ / ☐ ]0, +∞[ / ☐ ℝ*.
Vrai-faux « en justifiant » : 1. f continue sur [1, +∞[, f(1) = 2, lim_{+∞} f = 3 ⇒ f bijection de [1, +∞[ sur [2, 3[.
2. Toute fonction affine réalise une bijection de ℝ sur ℝ. 3. Pour tout x > 0, ⁴√x ≥ ∛x. 4. La réciproque de f(x) = ⁿ√x sur ℝ₊ est
dérivable à droite en 0. 5. Si f strictement monotone et dérivable sur I et garde un signe constant sur I, sa réciproque garde un
signe constant sur f(I).

### Exercices et problèmes (p.62–66) — 24 exercices

- **Ex. 1** (p.62) : 3 figures ; identifier celles qui réalisent une bijection de I sur f_i(I). (1) I = [−4, 3], f₁(I) = [−4, 3] ;
  (2) I = [−3, 1], f₂(I) = [−4, 4] ; (3) I = [−3, 4], f₃(I) = [−3, 4].
- **Ex. 2** (p.62) : f(x) = x² − 4x + 5 sur I = ]−∞, 2]. 1. bijection de I sur J à préciser ; 2. tracer C_f ; 3. a. tracer la courbe de
  f⁻¹ ; b. étudier graphiquement la dérivabilité de f⁻¹ à droite en 1 ; c. f⁻¹ dérivable sur ]1, +∞[ ; d. expliciter f⁻¹(x), x ∈ J.
- **Ex. 3** (p.62) : f(x) = x − 1 − 1/x sur I = ]−∞, 0[. 1. f admet une réciproque définie sur J à déterminer ; 2. expliciter f⁻¹(x),
  tout réel x ; 3. f⁻¹ dérivable sur J, expliciter (f⁻¹)′(x).
- **Ex. 4** (p.62) : f(x) = (x + 1)/(x − 1) sur I = ]1, +∞[. 1. variations, f bijection de I sur I ; 2.a. expliciter f∘f(x), x ∈ I ; b. qu'en déduit-on ?
- **Ex. 5** (p.62) : f(x) = √(x − 1) + 2 sur [1, +∞[. 1. dérivabilité de f à droite en 1, interpréter ; 2. tableau de variation ; 3. f admet
  une réciproque f⁻¹ (à déterminer) ; 4. étudier la dérivabilité de f⁻¹.
- **Ex. 6** (p.63) : f(x) = 1 + x/√(1 + x²) sur ℝ. 1. variations, f bijection de ℝ sur ]0, 2[ ; 2. expliciter f⁻¹(x), x ∈ ]0, 2[.
- **Ex. 7** (p.63) : f(x) = x/(x + √x) si x > 0, f(0) = 0 sur ℝ₊. 1. continuité puis dérivabilité à droite en 0 ; 2.a. tableau de variation ;
  b. f bijection de ℝ₊ sur [0, 1[ ; c. dérivabilité de f⁻¹ sur [0, 1[ ; 3. expliciter f⁻¹(x), x ∈ [0, 1[.
- **Ex. 8** (p.63) : courbe C_f d'une fonction f bijective de ℝ sur ℝ (décroissante ; branche tendant vers 2 en −∞ ; tangente verticale au point (−2, 1), tangente horizontale au point (0, −1)) ; g = f⁻¹. 1. dérivabilité de g en −1 et en 1 ; 2. tableau de variation de g ; 3. reproduire la courbe de f et représenter celle de g.
- **Ex. 9** (p.63) : courbe C d'une fonction f bijective de ]−1, 2] sur [−4, +∞[, asymptote verticale x = −1 ; g = f⁻¹. 1. dérivabilité de g
  en −1 et en −4 ; 2. tableau de variation de g ; 3. limite de g en +∞.
- **Ex. 10** (p.63) : f(x) = tan x sur ]−π/2, π/2[. 1. bijection de ]−π/2, π/2[ sur ℝ ; 2. f⁻¹ dérivable sur ℝ et (f⁻¹)′(x) = 1/(1 + x²), x ∈ ℝ.
- **Ex. 11** (p.63) : f(x) = 2cos x + 3 sur [0, π]. 1. tableau de variation ; 2. bijection de [0, π] sur I à déterminer ; 3. g = f⁻¹ — a. calculer
  g(5), g(3), g(1) ; b. g dérivable sur ]1, 5[, expliciter g′(x).
- **Ex. 12** (p.64) : f(x) = 1/sin x sur [π/2, π[. 1. bijection de [π/2, π[ sur [1, +∞[ ; 2. calculer f⁻¹(√2) et f⁻¹(2√3/3) ; 3. continuité et
  dérivabilité de f⁻¹ sur [1, +∞[ ; 4. calculer (f⁻¹)′(x), x ∈ ]1, +∞[.
- **Ex. 13** (p.64) : f(x) = 1 − tan x sur ]−π/2, π/2[. 1. tableau de variation ; 2. bijection sur ℝ ; 3. calculer f⁻¹(0) et f⁻¹(2) ; 4. f⁻¹
  dérivable sur ℝ et (f⁻¹)′(x) = 1/(−x² + 2x − 2) ; 5. nature des branches infinies de la courbe de f⁻¹.
- **Ex. 14** (p.64) : f(x) = √(cos x) sur [0, π/2]. 1. dérivabilité de f en π/2 à gauche, interpréter ; 2.a. f admet une réciproque f⁻¹ définie
  sur [0, 1] ; b. en utilisant 1., f⁻¹ dérivable en 0 à droite et préciser (f⁻¹)′_d(0) ; c. demi-tangente à la courbe de f en son point d'abscisse 0
  et en déduire que f⁻¹ n'est pas dérivable à gauche en 1 ; 3. f⁻¹ dérivable sur ]0, 1[ et (f⁻¹)′(x) = −2x/√(1 − x⁴).
- **Ex. 15** (p.64) : f(x) = cos((π/2)x) sur [0, 1]. 1. variations, tracer la courbe (demi-tangentes aux abscisses 0 et 1) ; 2. bijection de [0, 1]
  sur I à préciser ; 3. f⁻¹ dérivable sur [0, 1[ et (f⁻¹)′(x) = −2/(π√(1 − x²)).
- **Ex. 16** (p.64) : f(x) = 1/(1 − cos πx) sur ]0, 1]. 1. variations, tracer la courbe ; 2.a. f(x) = x admet une unique solution x₀ dans ]0, 1] ;
  b. calculer f(2/3), en déduire x₀ ; 3.a. bijection de ]0, 1] sur [1/2, +∞[ ; b. f⁻¹ dérivable en 1/2 à droite ? c. f⁻¹ dérivable sur ]1/2, +∞[ et
  (f⁻¹)′(x) = −1/(πx√(2x − 1)).
- **Ex. 17** (p.65) : f(x) = (x² + 1)/(x² + x + 1) sur [−1, 1]. 1. bijection de [−1, 1] sur I à préciser ; 2. g(x) = f(x) − x — a. g(x) = 0 admet une unique
  solution α dans ]−1, 1[ ; b. α ∈ ]2/3, 1[ ; c. Δ : y = x coupe la courbe de f en un unique point ; 3. f⁻¹ dérivable en 2/3 ? 4.a. calculer f(−1/2), f(0), f(1/2) ;
  b. en déduire les nombres dérivés de f⁻¹ en 5/3, en 1 et en 5/7.
- **Ex. 18** (p.65) : f(x) = x/√(x² + 1) − 1 sur ℝ. 1. bijection de ℝ sur I à préciser ; 2.a. f(x) = x admet une unique solution α dans ℝ et −2 < α < −1 ; b. signe
  de f(x) − x ; 3. expliciter f⁻¹(x), x ∈ I ; 4. (uₙ) : u₀ = −1, uₙ₊₁ = f(uₙ) — a. pour tout n, α ≤ uₙ ≤ −1 ; b. (uₙ) convergente, déterminer sa limite.
- **Ex. 19** (p.65) : A/ f(x) = √(x² − 1)/x + 1 sur [1, +∞[. 1.a. dérivabilité à droite en 1 ; b. tableau de variation ; c. bijection de [1, +∞[ sur I à préciser ;
  2.a. f⁻¹ dérivable à droite en 1 ? b. expliciter f⁻¹(x), x ∈ I. B/ g(x) = 1/f(1/cos x) si x ∈ [0, π/2[, g(π/2) = 1/2. 1.a. g continue à gauche en π/2 ; b. pour
  tout x ∈ [0, π/2], g(x) = 1/(1 + sin x) ; 2. g bijection de [0, π/2] sur J à préciser ; 3.a. g⁻¹ dérivable sur ]1/2, 1] et calculer (g⁻¹)′(x) ; b. g⁻¹ dérivable à droite en 1/2 ?
- **Ex. 20** (p.65) : 1. simplifier x = ∛3·∛27·∛8/∛81, y = ∛4/∛32, t = ∛(8²). 2.a. développer (2 + √5)³ ; b. simplifier ∛(38 + 17√5) − ∛(17√5 − 38).
- **Ex. 21** (p.65) : résoudre dans ℝ : 1. ∛x = ⁴√2 ; 2. ⁵√(x²) = ∛3 ; 3. ∛(x²) − 3∛x + 2 = 0 ; 4. (1 − ⁴√x)³ + 8 = 0.
- **Ex. 22** (p.66) : limites : lim_{x→+∞} ∛(x² − x + 1) ; lim_{x→+∞} (x − ∛x) ; lim_{x→2} (∛x − ∛2)/(x − 2) ; lim_{x→+∞} (∛x − √x)/⁴√x.
- **Ex. 23** (p.66) : f(x) = x + ∛x sur ℝ₊. 1. dérivabilité à droite en 0, interpréter ; 2. tableau de variation ; 3. branche infinie ; 4. f bijection de ℝ₊ sur ℝ₊ ;
  5. calculer f(1), f(8), (f⁻¹)′(2) et (f⁻¹)′(10).
- **Ex. 24** (p.66) : f(x) = x·⁴√x sur ℝ₊. 1. dérivabilité à droite en 0, interpréter ; 2. tableau de variation ; 3. lim_{x→+∞} f(x)/x, interpréter ; 4. f bijection de ℝ₊
  sur ℝ₊ ; 5. expliciter f⁻¹(x), x ∈ ℝ₊.

### Écart avec la référence (math-bac-math ch.04, manuel 222445 p.77–95)

**À EXCLURE (la référence l'enseigne, ce manuel non)** :
- Partie IV « x ↦ ⁿ√(u(x)) » : théorème de dérivation de ⁿ√(u(x)) et ses exercices résolus (absent ; ce manuel s'arrête à ⁿ√x). Les exercices résolus 1 et 2 de la référence (étude de ∛(x² + 1), de √x − 1/(2x)) n'existent pas ici.
- Remarque « valable pour dérivée à droite/à gauche » du théorème (f⁻¹)′(b) = 1/f′(a) : absente ; ici le théorème est énoncé pour « un intervalle ouvert I » (p.58), alors que la référence dit « un intervalle I » (ce sont les exercices 5, 7, 14, 16, 19 qui font pourtant étudier des dérivabilités à droite : voir doute ci-dessous).
- Conséquence « lim_{x→+∞} ⁿ√x = +∞ » : absente.
- Inégalité des accroissements finis / suites récurrentes avec IAF (ex. 16, 24, 27, 28 de la référence), suites (vₙ), sommes de Riemann, théorème des valeurs intermédiaires dans des problèmes longs, géométrie (ex. 25) : absents. Une seule suite ici (ex. 18 : convergence monotone, sans IAF).
- Aucun problème long type « étude complète + tangente + position relative + construction + réciproque » à plusieurs parties A/B/C (seul l'ex. 19 a deux parties A/ B/).
- Pas d'équations de réciproques trigonométriques composées (ex. 12 de la référence avec g⁻¹(x) + g⁻¹(1/x)), pas d'exercice sur le centre de symétrie de f⁻¹.

**EN PLUS dans ce manuel** :
- Activité 3 p.60 (dérivabilité à droite en 0 de ⁿ√x) et Activité 4 (étudier et représenter ∛x, ⁴√x, ⁶√x) suivent le théorème de dérivation de ⁿ√x, démontré par la dérivée de la réciproque de x ↦ xⁿ.
- Activité 4 p.59 : question sur les demi-tangentes à C_{f⁻¹} en −1 (droite) et en 1 (gauche) (la référence demande « dérivabilité à droite en −1 et à gauche en 1 »).
- Exercices de cours : ex. 4 (f∘f = id, « qu'en déduit-on ? » : involution), ex. 14 (demi-tangente et dérivabilité à gauche de f⁻¹ en 1), ex. 12/13 (réciproques de 1/sin x, 1 − tan x), calculs de nombres dérivés de réciproques sans expliciter f⁻¹ (ex. 11, 12, 17, 23).
- Ex. 20–21–22 : radicaux, résolution d'équations en ⁿ√, limites avec racines cubiques ; ex. 20.2.b (∛(38+17√5) − ∛(17√5−38)).
- Les exercices de référence 1, 2, 4, 5, 10, 21, 22 ont un équivalent proche (ex. 2, 3, 10, 5 ici) mais plus guidés et moins longs.

### Bornes de scope

- ✅ INCLUS : bijection d'un intervalle I sur f(I) (unicité de la solution de f(x) = y ; théorème monotone stricte ⇒ bijection) ; fonction réciproque f⁻¹, f⁻¹∘f = id_I, f∘f⁻¹ = id_{f(I)} ;
  courbe de f⁻¹ par symétrie d'axe Δ : y = x (repère orthonormé) ; réciproque d'une fonction continue strictement monotone (continuité admise, même sens de variation) ; dérivabilité de f⁻¹ en b = f(a)
  (f′(a) ≠ 0) et sur f(I) ; demi-tangentes verticale/horizontale de la courbe de f⁻¹ lorsque f′(a) = 0 (activités 3, 4, ex. 8, 9, 14) ; fonction racine nᵉᵐᵉ (n ≥ 2) comme réciproque de x ↦ xⁿ sur ℝ₊, notation ⁿ√x,
  équivalence y = xⁿ ⟺ x = ⁿ√y, opérations sur les radicaux, continuité sur [0, +∞[ et dérivabilité sur ]0, +∞[ (f′(x) = 1/(n·ⁿ√(xⁿ⁻¹))) ; réciproques de fonctions usuelles (sin, cos, tan sans notation Arc) ;
  explicitation de f⁻¹(x) ; calcul de nombres dérivés de f⁻¹ ; branches infinies ; équations f(x) = x ; une suite récurrente simple (ex. 18) ; équations et limites avec radicaux d'ordre 3, 4, 5.
- ⛔ EXCLU : dérivée de ⁿ√(u(x)) (partie IV de la référence) ; Arcsin/Arccos/Arctan comme fonctions nommées ; exposants rationnels x^(p/q) ; IAF et suites avec |f′| ≤ k ; ln, exp, primitives, intégrales ; problèmes géométriques longs (ex. 25 de la référence) ;
  exercices résolus de la référence.
- ⚠ DOUTE : le théorème p.58 est énoncé pour un intervalle OUVERT I, mais les exercices 5, 7, 14, 16, 19 demandent des dérivabilités de f⁻¹ « à droite » en 1, 0, 1/2 : ne pas reproduire la restriction dans une question ; écrire les énoncés des questions comme le manuel.

### Lecture

- **Pages lues par l'OCR** (texte brut /root/.cache/yqa-manuels/222433/txt/p054…p066.txt) : p.054 à p.066 (13 pages), toutes.
- **Pages lues sur l'image** (pdftoppm -r 110) : p.54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66 — 13 pages sur 13 (toutes contiennent formule, encadré, figure ou tableau).
- **Sondage image / OCR : écarts constatés** :
  - p.56 : OCR inutilisable (bruit pur sur les 4 figures) ; seules l'image donne I = [−5, 2] / f₁(I) = [−2, 3], I = [−6, 4] / f₂(I) = [−3, 4], I = ]−4, 4[ / f₃(I) = ]−4, 4[, I = [−2, 3[ / f₄(I) = ]−3, 1] et les encadrés Définition / Conséquence ; Activité 3 : « f⁻¹(−1), f⁻¹(1), f⁻¹(3) » (OCR : exposants perdus).
  - p.55 : OCR « g(x)= x2+3 », « [E +oo[ » = [3, +∞[, « h(x)=Vx-3 » = √(x − 3) ; « [3, +c[ » = [3, +∞[.
  - p.57 : OCR a perdu f : x ↦ 1/x et g : x ↦ √(1 + x²) (Activité 4), le système d'équivalences de la représentation graphique, et la figure de l'Activité 5.
  - p.58 : OCR « [5 3] » = [−π/2, π/2] ; valeurs « f⁻¹(√3/2…) » perdues ; fraction x/(1 + x²) dégradée ; « b 1 » = ]0, 1/2[.
  - p.59 : OCR coupe le bloc « Théorème et définition » (figure) ; « Activité 3 » figure perdue.
  - p.60 : OCR « ⁿ√ » rendu « 9x », « Vx », radicaux de la conséquence illisibles (« me (fe. vues. Ho. ») ; seule l'image donne l'ensemble des sept formules ; énoncé du théorème de dérivée n·ⁿ√(xⁿ⁻¹) dégradé.
  - p.61 : OCR : QCM 1 sans « I = [−π/2, π/2] », figure du QCM 3 perdue.
  - p.62 : OCR « 3-1 » pour f(x) = x − 1 − 1/x (dégradé), figures de l'ex. 1 perdues, ex. 4 « f(x) = (x+1)/(x−1) » illisible.
  - p.63 : OCR : ex. 6 f(x) = 1 + x/√(1+x²) illisible, ex. 7 piecewise dégradé (« 0 six=0 »), figures ex. 8 et 9 perdues ; ex. 9 : OCR « [−4, +x[ » = [−4, +∞[.
  - p.64–66 : OCR rend « f⁻¹ » en « f 7 », « f7! », « fl », les fractions et radicaux sont illisibles (ex. 12–19 en entier) ; tout le détail d'énoncé de ces pages provient de l'image.
  - Aucun désaccord de fond entre OCR et image sur la prose ; tous les désaccords concernent les formules, exposants, figures.

## 2.5 Chapitre 5 — Études de fonctions (manuel 222433, p.67–84)

**Page de garde (p.67)** — « Chapitre 5 — Etudes de fonctions ». Citation : « Euler (1707-1783) définit une fonction d'une quantité variable comme " une expression analytique composée d'une manière quelconque de cette quantité variable et de nombres ou de quantités constantes". En fait Euler donne une classification des fonctions en deux types: algébriques (fonctions rationnelles et irrationnelles), transcendantes ( fonctions trigonométriques, logarithmes, exponentielles, puissances). » Pas de « Plan du chapitre » imprimé (différence avec la référence). Plan réel, lu sur les pages : **I. Branches infinies** (p.68–70, Act. 1–4) · **II. Éléments de symétrie** (p.70–71, Act. 1–2) · **III. Exemples d'étude de fonctions** (p.71–78, Exemples 1–6 avec solution) · **QCM – VRAI-FAUX** (p.79) · **Exercices et problèmes** (p.80–84, 27 exercices). Ni résumé du cours, ni « Avec l'ordinateur », ni aperçu historique.

### Activités (p.68–71) — il n'y a PAS d'« activités préliminaires » distinctes

- **I. Act. 1** (p.68) : courbe donnée (figure) d'une fonction f définie sur ]−∞, −1[ ∪ ]1, +∞[ ; asymptotes x = −1, x = 1, y = 0 et y = −x − 3. Déterminer lim_{x→−∞} f(x), lim_{x→−∞} [f(x) + x + 3], lim_{x→(−1)⁻} f(x), lim_{x→1⁺} f(x), lim_{x→+∞} f(x). Suit un tableau « vu en 3ᵉ année » (encadré ci-dessous).
- **I. Act. 2** (p.68–69) : f(x) = √(x² + x + 1) sur ℝ, C_f repère orthonormé. 1) a) lim_{x→+∞} f(x) ; b) pour x > 0, f(x) = x√(1 + 1/x + 1/x²) ; c) en déduire lim_{x→+∞} f(x)/x. 2) a) pour x > 0, f(x) − x = (1 + 1/x) / (√(1 + 1/x + 1/x²) + 1) ; b) en déduire lim_{x→+∞} [f(x) − x], interpréter graphiquement. 3) calculer lim_{x→−∞} f(x), lim_{x→−∞} f(x)/x et lim_{x→−∞} [f(x) + x], interpréter graphiquement.
- **I. Act. 3** (p.70) : f(x) = 2x + √(x + 1) sur [−1, +∞[, repère orthonormé. Nature de la branche infinie de C_f au voisinage de +∞.
- **I. Act. 4** (p.70) : f(x) = (x² + x − 1)/(x + 1) sur ]−1, +∞[, repère orthonormé. Étudier les branches infinies de C_f.
- **II. Act. 1** (p.70) : repère orthonormé ; Δ : y = 1 − x ; à tout réel x on associe M de Δ d'abscisse x ; f(x) = OM (figure). 1) f(x) = √(x² + (1 − x)²) ; 2) Δ : x = 1/2 axe de symétrie de C_f ; 3) Δ' : y = √2 x − √2/2 asymptote à C_f au voisinage de +∞.
- **II. Act. 2** (p.71) : f(x) = 2 − √(2 − x) si x < 1 ; √x si x ≥ 1 ; sur ℝ, repère orthonormé. 1) I(1, 1) centre de symétrie de C_f ; 2) f dérivable en 1 ; 3) équation de la tangente T en I ; 4) I point d'inflexion de C_f ; 5) position relative de T et C_f.

### Exemples résolus (p.71–78) — avec solution rédigée (NOUVEAU par rapport à la référence)

- **Ex. 1** (p.71–72) : f : x ↦ x³/8 + x − 4, C₁ repère orthonormé. 1) branches infinies ; 2) a) f'(x), b) C₁ admet un point d'inflexion I, c) tangente T en I ; 3) tableau de variation ; 4) f réalise une bijection de ℝ sur ℝ ; 5) représenter C₁ et C₂ (courbe de f⁻¹) dans le même repère. Solution : deux branches paraboliques de direction (O, j⃗) ; f'(x) = 3x²/8 + 1 ; f''(x) = 3x/4 s'annule en 0 en changeant de signe, I(0, −4) ; T : y = x − 4 ; f continue strictement croissante donc bijection de ℝ sur f(ℝ) = ]lim_{−∞} f, lim_{+∞} f[ = ℝ.
- **Ex. 2** (p.72–73) : f : x ↦ (2x² + x − 4)/(x − 1). 1) vérifier f(x) = 2x + 3 − 1/(x − 1), x ≠ 1 ; 2) étudier f et tracer sa courbe (repère orthogonal) ; 3) montrer que pour tout réel k, f(x) = k admet exactement deux solutions. Solution : asymptote x = 1 ; lim [f(x) − 2x − 3] = 0 en ±∞ donc y = 2x + 3 asymptote ; f'(x) = 2 + 1/(x − 1)², strictement croissante sur ]−∞, 1[ et sur ]1, +∞[ ; f(]−∞, 1[) = ℝ et f(]1, +∞[) = ℝ, donc deux solutions x₁, x₂.
- **Ex. 3** (p.73–74) : f : x ↦ 1/((x + 3)(x − 2)). 1) vérifier f(x) = 1/(5(x − 2)) − 1/(5(x + 3)), x ≠ −3 et x ≠ 2 ; 2) étudier f et tracer sa courbe (repère orthogonal) ; 3) étudier graphiquement, suivant k, les solutions de f(x) = k. Solution : asymptotes x = −3, x = 2, y = 0 ; f'(x) = −1/(5(x−2)²) + 1/(5(x+3)²) = (−2x − 1)/((x−2)²(x+3)²) ; f'(x) ≥ 0 ssi x ≤ −0,5 et x ≠ −3 ; maximum local f(−0,5) = −0,16 ; si k < −0,16 ou k > 0 : deux points d'intersection ; k = −0,16 : un ; −0,16 < k ≤ 0 : aucun.
- **Ex. 4** (p.75–76) : f : x ↦ x + √(x² − 1), C repère orthonormé. 1) ensemble de définition D ; 2) a) f(x)f(−x) = −1 sur D ; b) en déduire f(x) ≠ 0 ; c) limites en +∞ et −∞ ; d) Δ : y = 2x asymptote à C ; 3) f'(x) = f(x)/√(x² − 1), x ∈ ]−∞, −1[ ∪ ]1, +∞[ ; 4) dérivabilité à droite en 1 et à gauche en −1 ; 5) tableau de variation et tracé. Solution : D = ]−∞, −1] ∪ [1, +∞[ ; lim_{−∞} f = lim −1/f(−x) = 0 ; f(x) − 2x = −1/(x + √(x² − 1)) → 0 ; taux d'accroissement en 1 : 1 + (x + 1)/√(x² − 1) → +∞ (idem −∞ en −1, demi-tangentes verticales) ; f' garde un signe constant sur chaque intervalle (f ne s'annule pas, signe de f(1) puis de f(−1)) : f'(x) > 0 ssi x > 1.
- **Ex. 5** (p.76–77) : f : x ↦ 4 sin x/(2 + cos x). 1) a) ensemble de définition ; b) parité et 2π période ; 2) variations sur [0, π] ; 3) tracer, repère orthonormé, la restriction de f à [−2π, 2π]. Solution : définie sur ℝ (2 + cos x ≠ 0), impaire, 2π période ; f'(x) = 4(2cos x + 1)/(2 + cos x)² ; f'(x) ≥ 0 ssi x ∈ [0, 2π/3] ; maximum f(2π/3) = 4/√3, f(0) = f(π) = 0.
- **Ex. 6** (p.77–78) : f(x) = sin x − (2/π)x sur [0, π/2]. 1) a) variations de f' et existence d'un unique réel α de [0, π/2] tel que f'(x) ≥ 0 ssi x ∈ [0, α] ; b) valeur approchée à 10⁻⁴ près de α avec la touche cos⁻¹ de la calculatrice ; 2) tableau de variation de f, signe de f ; 3) tracer la courbe de f. Solution : f'(x) = cos x − 2/π ; f''(x) = −sin x ≤ 0 ; f' bijection strictement décroissante de [0, π/2] sur [−2/π, 1 − 2/π] (valeurs de signes contraires) ; α unique solution de cos x = 2/π, α ≈ 0,88068923 donc 0,8807 à 10⁻⁴ près ; f(α) ≈ 0,21051366.

### QCM – VRAI-FAUX (p.79) — NOUVEAU par rapport à la référence

- **QCM 1–5** (p.79) : tableau de variation (figure) de f sur ]−∞, −1] [−1, −0,5[ ]−0,5, 0] [0, +∞[ : f' = − 0 + || + 0 − ; valeurs 2, +∞ | −∞, 3, −5 ; minimum 0 en −1. 1) minimum relatif (0 / −1 / −5) ; 2) f croissante sur [−1, 0] / sur [−1, −0,5[ et ]−0,5, 0] / décroissante sur ]−∞, −0,5] ; 3) asymptote verticale (x = 2 / x = −0,5 / x = −5) ; 4) asymptote horizontale (y = 2 / y = −0,5 / y = −1) ; 5) f et l'axe des abscisses : un / deux / trois points communs. [Levé en L3 (image p.79) : sur ]−∞ ; −1], f décroît de 2 à 0 ; sur [−1 ; −0,5[, elle croît de 0 à +∞ ; sur ]−0,5 ; 0], elle croît de −∞ à 3 ; sur [0 ; +∞[, elle décroît de 3 à −5.]
- **Vrai-Faux 1–4** (p.79) : « Répondre par vrai ou faux en justifiant la réponse. » f deux fois dérivable sur ]a − h, a + h[ (h > 0), dérivée seconde continue. 1) si f''(a) = 0 alors la courbe admet un point d'inflexion d'abscisse a ; 2) si f' est décroissante sur ]a − h, a[ et croissante sur [a, a + h[ alors point d'inflexion d'abscisse a ; 3) si f' est croissante sur ]a − h, a + h[ alors f est croissante sur ]a − h, a + h[ ; 4) si f'' est négative sur ]a − h, a + h[ alors f est décroissante sur ]a − h, a + h[. (Piège pédagogique du manuel : 1, 3 et 4 sont à justifier par contre-exemple ; aucun corrigé imprimé. Réponses NON reprises ici.)

### Exercices et problèmes (p.80–84) — 27 exercices

- **Ex. 1** (p.80) : courbe C d'une fonction f définie sur ℝ\{0, 2} (figure : asymptotes Δ oblique, x = 0, x = 2, y = 0) ; 1) limites de f en −∞, 0⁻, 0⁺, 2⁻, 2⁺, +∞, lim f(x)/x et lim [f(x) + x − 2] en +∞, lues graphiquement ; 2) tableau de variation ; 3) nombre de solutions de f(x) = m suivant m.
- **Ex. 2** (p.80) : f(x) = x² + 1, g(x) = √x, h(x) = x − 2/(x + 1) sur [0, +∞[ ; 3 courbes (C₁, C₂, C₃) représentées ; 1) identifier chaque courbe ; 2) nature de la branche infinie de chacune.
- **Ex. 3** (p.80) : repère orthogonal ; nature des branches infinies de : 1) f : x ↦ 2x − 3√(x − 1) ; 2) f : x ↦ 1/x − √(x + 2) ; 3) f : x ↦ x√((x − 1)/(x + 1)).
- **Ex. 4** (p.80) : f(x) = x + √(x² + 1) sur ℝ, C. 1) l'axe des abscisses est asymptote à C en −∞ ; 2) la droite y = 2x est asymptote à C en +∞.
- **Ex. 5** (p.80) : f(x) = x² − 2x + 4 si x ≤ 1 ; 1/x + x + 1 si x > 1. 1) f dérivable en 1, préciser f'(1) ; 2) f dérivable sur ℝ, déterminer f' ; 3) tableau de variation et courbe (repère orthonormé).
- **Ex. 6** (p.80) : 1) f : x ↦ x²/3 + 9/(4x) ; 2) ensemble de définition ; 3) tableau de variation ; 4) branches infinies ; 5) courbe (repère orthonormé) ; 6) en déduire la construction de la courbe d'équation y = |x²/3 + 9/(4x)|.
- **Ex. 7** (p.81) : f : x ↦ x³/(x − 1)². 1) lim_{x→1} f(x), lim_{x→+∞} [f(x) − x − 2], interpréter ; 2) variations de f et courbe (repère orthogonal).
- **Ex. 8** (p.81) : f : x ↦ (x³ + 3x² + 3x + 5)/(x + 1)², x ≠ −1. 1) a, b, c tels que f(x) = ax + b + c/(x + 1)² ; 2) tableau de variation ; 3) C courbe (repère orthonormé) : a) asymptote D au voisinage de l'infini ; b) position relative de C et D ; c) tracer D et C.
- **Ex. 9** (p.81) : f : x ↦ (x² − 2x + 3)/(x − 1), x ≠ 1. 1) a, b, c tels que f(x) = ax + b + c/(x − 1) ; 2) tableau de variation ; 3) C admet un centre de symétrie ; 4) a) asymptote oblique D, b) position relative, c) tracer D et C ; 5) la restriction g de f à [1 + √2, +∞[ réalise une bijection sur un intervalle à préciser : a) tableau de variation de g⁻¹ ; b) résoudre g(x) = x, en déduire les points d'intersection de C et C' (courbe de g⁻¹) ; c) tracer C'.
- **Ex. 10** (p.81) : f : x ↦ x/√3 − √3/x, C repère orthonormé. 1) variations et tracé de C ; 2) S symétrie orthogonale par rapport à D : x = 1, M(x, y) → M'(x', y') : a) coordonnées de M' ; b) équation de C' image de C par S ; c) points communs à C et C' ; d) tracer C'.
- **Ex. 11** (p.81) : f : x ↦ |x + 1| + x/(x² − 1), C repère orthonormé. 1) ensemble de définition ; 2) tableau de variation ; 3) asymptotes ; 4) position de C par rapport à ses asymptotes obliques ; 5) tangente au point d'abscisse 0 et position de C par rapport à elle sur ]−1, 1[ ; 6) tracer C.
- **Ex. 12** (p.81) : f : x ↦ (x⁴ − 6x² + 1)/(x³ − x), C repère orthonormé. 1) a) ensemble de définition ; b) a, b, c tels que f(x) = x + a/x + b/(x − 1) + c/(x + 1), x ∈ ℝ\{−1, 0, 1} ; 2) tableau de variation ; 3) asymptotes ; 4) résoudre f(x) = 0 et f(x) = x ; 5) C possède un centre de symétrie, tracer C ; 6) P_k(x) = x⁴ − kx³ − 6x² + kx + 1 : l'équation P_k(x) = 0 admet, quel que soit k, quatre racines réelles distinctes.
- **Ex. 13** (p.82) : f : x ↦ (3x² − x − 2)/(x² − x − 2), C repère orthonormé. 1) ensemble de définition ; 2) tableau de variation ; 3) asymptotes et tracé de C ; 4) discuter graphiquement, suivant m, le nombre et le signe des solutions de (3 − m)x² + (m − 1)x + 2(m − 1) = 0 ; 5) g restriction de f à ]2, +∞[ : a) g admet une réciproque g⁻¹ dont on précisera l'ensemble de définition ; b) tracer la courbe de g⁻¹.
- **Ex. 14** (p.82) : f : x ↦ (x + 1)³/(x − 1)², x ≠ 1. 1) f(x) = x + 5 + 12/(x − 1) + 8/(x − 1)² ; 2) tableau de variation ; 3) courbe 𝒞 (repère orthonormé) : a) asymptote oblique D ; b) points d'intersection A et B de 𝒞 avec x = 0 et y = x + 5 ; c) tangentes en A et en B ; d) tracer ces tangentes et 𝒞.
- **Ex. 15** (p.82) : f : x ↦ √(x² − x + 1), C_f (repère orthogonal). 1) a) ensemble de définition D ; b) f(x) = √((x − 1/2)² + 3/4) ; 2) a) Δ : y = x − 1/2 asymptote à la courbe en +∞ ; b) position de la courbe par rapport à Δ ; 3) nature de la branche infinie de C_f en −∞ ; 4) tracer C_f et Δ.
- **Ex. 16** (p.82) : f : x ↦ √(x² + 3x − 4), C repère orthonormé. 1) ensemble de définition ; 2) dérivabilité à gauche en −4 et à droite en 1, interpréter graphiquement ; 3) dérivabilité sur ]−∞, −4[ et ]1, +∞[, déterminer f' ; 4) tableau de variation ; 5) branches infinies ; 6) a) tracer C ; b) en déduire la représentation de la courbe d'équation x² − y² + 3x − 4 = 0.
- **Ex. 17** (p.82) : f : x ↦ x² − 32√x + 31, C repère orthogonal (1 cm sur l'axe des abscisses, 2 mm sur l'axe des ordonnées). 1) dérivabilité à droite en 0 ; 2) tableau de variation ; 3) tracer C ; 4) en déduire la courbe de g : x ↦ x² − 32√|x| + 31.
- **Ex. 18** (p.82) : g(x) = x√x + 10 sur ℝ₊ [levé en L3 (image p.82) : « x√x + 10 », le +10 est hors de la racine]. 1) g dérivable à droite en 0 ; 2) g'(x), x > 0 ; 3) tableau de variation ; 4) lim_{x→+∞} g(x)/x ; 5) représenter g (repère orthogonal).
- **Ex. 19** (p.83) : f : x ↦ (2 + √(4 − x²))/x, C repère orthonormé. 1) ensemble de définition ; 2) dérivabilité de f en 2 à gauche, interpréter ; 3) dérivabilité sur ]0, 2[, f' ; 4) tableau de variation ; 5) a) points d'intersection de C et de D : y = x ; b) tracer C ; 6) g restriction de f à ]0, 2] : a) g bijection de ]0, 2] sur un intervalle I à préciser ; b) expliciter g⁻¹(x), x ∈ I ; c) tracer C' de g⁻¹.
- **Ex. 20** (p.83) : f : x ↦ (2x + 1)/√(x² + x + 1), C repère orthonormé. 1) tableau de variation ; 2) le point d'intersection I de C avec l'axe des abscisses est centre de symétrie ; 3) points de C où la tangente est parallèle à y = 1,5x ? si oui, équations ; 4) tracer C ; 5) a) f admet une réciproque f⁻¹ ; b) tracer f⁻¹ ; c) calculer (f⁻¹)'(1).
- **Ex. 21** (p.83) : I. f : x ↦ −1/2 + x/(2√(x² + 1)), C. 1) tableau de variation ; 2) f bijection de ℝ sur un intervalle à préciser. II. g(x) = −x/2 + 1 + (1/2)√(x² + 1) sur ℝ. 1) tableau de variation de g ; 2) asymptotes à la courbe C' de g et position de C' par rapport à ses asymptotes ; a) tracer C' ; b) g bijection de ℝ sur un intervalle I à préciser ; c) vérifier g⁻¹(x) = 1/(4x − 4) + 1 − x, x ∈ I ; d) tracer la courbe de g⁻¹. [Levé en L3 (image p.83) : I.f = −1/2 + x/(2√(x²+1)) et g⁻¹(x) = 1/(4x − 4) + 1 − x, conformes à l'image.]
- **Ex. 22** (p.83) : f : x ↦ 1 + x/√(x² + 1), C repère orthonormé. 1) tableau de variation ; 2) a) point d'inflexion A (coordonnées), b) tangente T en A, c) A centre de symétrie, d) construire C ; 3) a) f bijection de ℝ sur un intervalle I ; b) expliciter f⁻¹(x) pour x ∈ I ; c) tracer f⁻¹ ; d) f⁻¹ dérivable, calculer (f⁻¹)'(x) ; 4) f(x) = x admet une unique solution dans [√3, 2] ; 5) suite (uₙ) : u₀ = 2, uₙ₊₁ = f(uₙ) : a) (uₙ) décroissante ; b) √3 ≤ uₙ ≤ 2 pour tout n ; c) en déduire que (uₙ) converge, déterminer sa limite.
- **Ex. 23** (p.84) : étudier et représenter f : x ↦ sin x + (1/2) sin 2x.
- **Ex. 24** (p.84) : étudier et représenter f : x ↦ cos x/(2cos x − 1).
- **Ex. 25** (p.84) : f(x) = sin²x + cos x sur ℝ, C_f. 1) a) 2π est une période ; b) l'axe des ordonnées est axe de symétrie de C_f ; 2) a) variations de f ; b) f(x) = 0 admet une unique solution α dans [0, π], encadrement d'amplitude 10⁻¹ ; c) tracer la restriction de f à [−π, 2π].
- **Ex. 26** (p.84) : I. étudier et représenter f : x ↦ x³/(x − 1)². II. h : x ↦ sin³x/(sin x − 1)², C_h repère orthonormé. 1) a) ensemble de définition ; b) 2π période ; c) x = π/2 axe de symétrie de C_h ; 2) a) lim_{x→π/2⁻} h(x) ; b) en écrivant h = f ∘ sin, sens de variation de h sur [−π/2, π/2[ ; c) résoudre h'(x) = 0 ; d) l'origine est point d'inflexion de C_h ; 3) tracer C_h.
- **Ex. 27** (p.84) : 1) étudier et représenter f : x ↦ x(x + 1)/(x − 2) ; 2) nombre de solutions de x² + (1 − m)x + 2m = 0 suivant m (graphiquement) ; 3) nombre de solutions de cos²x + (1 − m)cos x + 2m = 0 dans [0, 2π[ suivant m (graphiquement).

### Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur image)

> **Définition — branche infinie** (p.68, I.) — « Soit f une fonction et C_f sa courbe représentative dans un repère orthogonal. On dit que C_f admet une branche infinie dès que l'une des coordonnées d'un point de C_f tend vers l'infini. »

> **Tableau — asymptotes** (p.68, « Nous avons résumé dans le tableau ci-dessous la nature de certaines branches infinies vues en 3ème année. ») — (1) « lim_{x→a⁺} f(x) = +∞ ou lim_{x→a⁺} f(x) = −∞. lim_{x→a⁻} f(x) = +∞ ou lim_{x→a⁻} f(x) = −∞. » ⇒ « La droite D : x = a est asymptote à C_f. » (2) « lim_{x→+∞} f(x) = L ou lim_{x→−∞} f(x) = L. ( L réel) » ⇒ « La droite D : y = L est asymptote à C_f. » (3) « lim_{x→+∞} (f(x) − (ax + b)) = 0 ou lim_{x→−∞} (f(x) − (ax + b)) = 0. » ⇒ « La droite D : y = ax + b est asymptote à C_f. »

> **Branches infinies — procédé** (p.69) — « Soit f une fonction telle que f(x) tend vers l'infini, lorsque x tend vers l'infini. On désigne par C_f sa courbe dans un repère orthogonal (O, i⃗, j⃗). Alors la branche infinie de C_f dépend de la limite de f(x)/x, lorsque x tend vers l'infini. Nous donnons dans le tableau ci-dessous un procédé de détermination de la branche infinie de C_f dans le cas où lim_{x→+∞} f(x) est infinie. Les autres cas se déterminent de façon analogue. » Encadré : « * Si lim_{x→+∞} f(x)/x est infinie, alors C_f admet une branche parabolique de direction (O, j⃗) au voisinage de +∞. * Si lim_{x→+∞} f(x)/x = 0, alors C_f admet une branche parabolique de direction (O, i⃗) au voisinage de +∞. * Si lim_{x→+∞} f(x)/x = a (a ∈ ℝ*) alors deux cas peuvent se présenter selon lim_{x→+∞} (f(x) − ax). • Si lim_{x→+∞} (f(x) − ax) = b (b ∈ ℝ) alors la droite d'équation y = ax + b est une asymptote oblique à la courbe C_f au voisinage de +∞. • Si lim_{x→+∞} (f(x) − ax) est infinie alors la droite d'équation y = ax est une direction asymptotique à la courbe C_f au voisinage de +∞. »

> **Axe de symétrie** (p.70, encadré rose) — « Soit f une fonction définie sur D. On désigne par C_f sa courbe représentative dans un repère orthogonal. La droite Δ : x = a (a ∈ ℝ) est un axe de symétrie pour C_f si pour tout x de D, (2a − x) ∈ D et f(2a − x) = f(x). » (accolade imprimée sur les deux conditions)

> **Centre de symétrie** (p.71, encadré rose) — « Le plan est muni d'un repère orthogonal (O, i⃗, j⃗). Soit f une fonction définie sur un ensemble D, de courbe représentative C et O' le point de coordonnées (a, b). Le point O' est un centre de symétrie de C, si pour tout x appartenant à D, 2a − x appartient à D et f(2a − x) = 2b − f(x). »

Aucun autre encadré dans les p.67–84 : pas de définition imprimée de la périodicité, du point d'inflexion, de la bijection réciproque ni de la parité (ces notions sont mobilisées sans encadré : Ex. 5 « f est impaire et 2π est une période de f », Ex. 1 « f'' s'annule en 0 en changeant de signe, on en déduit que le point I est un point d'inflexion »). Pas de plan d'étude en étapes, pas de résumé.

### Écart avec la référence (chapitre math-bac-techniques 04, manuel 222451, p.78–98)

**À EXCLURE (la référence l'enseigne, ce manuel NON)** :
- plan d'étude d'une fonction en 7 étapes (réduction du domaine, limites, variations, asymptotes, points, construction) et page « Résumé du cours » ;
- 6 « activités préliminaires » (p.79–81 de la référence) ; aucune ici ;
- théorème « restriction à [a, a + T] et translations de vecteurs kT i⃗ » ; **définition de la périodicité** (f(x + T) = f(x)) ; réduction du domaine par parité/périodicité explicitée ; tg x (étude, restriction, réciproque) et fonction cosinus réciproque (arccos) en situation ;
- changement de repère « équation Y = F(X) dans (W, i⃗, j⃗) » comme méthode (le manuel n'a que les critères de centre/axe de symétrie, pas le changement de repère) ;
- transformations : encadré « translation de vecteur k j⃗ » et « symétrie d'axe (O, i⃗) » (courbes de f + k, −f) ; la construction de |f| apparaît seulement dans l'Ex. 6 (|x²/3 + 9/(4x)|), et x ↦ f(|x|) dans l'Ex. 17 (g(x) = x² − 32√|x| + 31), sans encadré ;
- problèmes d'optimisation (aire minimale, clôture) ; activités « Avec l'ordinateur » (logiciel) ; suite contractante |f'| ≤ 2/3 et inégalité des accroissements finis ;
- fonctions définies par morceaux avec raccordement C¹ à étude de dérivabilité complète : présent seulement Act. II.2 et Ex. 5 ; aucune fonction polynôme de degré 4 d'étude guidée (l'Ex. 12 est rationnelle) — la référence a x⁴ − 2x² + 2 ; ici pas de polynôme de degré 4 étudié (à signaler) ; pas de f_n(x) = xⁿ√(x − 1) ; pas de fonction à paramètre n ;
- fonctions ln, exp : exclues dans les deux manuels ; aperçu historique (Descartes) remplacé ici par la citation d'Euler en page de garde.

**EN PLUS dans ce manuel** :
- section « I. Branches infinies » avec la définition de branche infinie, le tableau des asymptotes verticale / horizontale / oblique (rappel de 3ᵉ année) et le procédé complet par f(x)/x : branche parabolique de direction (O, j⃗) ou (O, i⃗), asymptote oblique, **direction asymptotique y = ax** (b infini) ; la référence ne mentionne que « branche parabolique de direction y = ax » entre parenthèses ;
- 6 **exemples résolus** rédigés (solution complète, tableaux, courbes) — la référence n'a « aucun exercice résolu » ;
- **QCM (5 questions) et Vrai-Faux (4 énoncés)** p.79 — la référence : « Pas de QCM ni de Vrai-Faux » ;
- utilisation du **signe de f' par bijection de f'** (Ex. 6, α par cos x = 2/π, valeur approchée à la calculatrice avec cos⁻¹) ;
- **point d'inflexion** via f'' qui s'annule en changeant de signe (Ex. 1, Ex. 22, Ex. 26) ;
- **dérivabilité à droite/gauche en un point avec tangente verticale** (Ex. 4, 16, 17, 18, 19) ;
- **courbe d'équation x² − y² + 3x − 4 = 0** déduite de y = √(x² + 3x − 4) (Ex. 16), **composition h = f ∘ sin** (Ex. 26), **symétrie orthogonale d'axe x = 1** et équation de l'image (Ex. 10), **polynôme P_k à quatre racines réelles distinctes** (Ex. 12), discussion graphique d'équations paramétrées (Ex. 13, 27) y compris en cos x (Ex. 27 q.3) ;
- **suite uₙ₊₁ = f(uₙ) monotone et bornée, limite** (Ex. 22 q.5) — la référence n'a que le cas contractant ;
- exercices avec fonction réciproque et dérivée de la réciproque ((f⁻¹)'(1), (f⁻¹)'(x), expression explicite de g⁻¹) (Ex. 9, 13, 19–22).

### Bornes de scope

- ✅ INCLUS : branche infinie ; asymptotes verticale, horizontale, oblique ; **branche parabolique de direction (O, i⃗) ou (O, j⃗) et direction asymptotique y = ax** (procédé par f(x)/x puis f(x) − ax) ; axe de symétrie x = a (f(2a − x) = f(x)) et centre de symétrie (f(2a − x) = 2b − f(x)) ; point d'inflexion (f'' change de signe) ; tangente en un point ; position relative d'une courbe et d'une asymptote / d'une tangente ; fonctions polynômes (degré 3 : Ex. 1), rationnelles (Ex. 2, 3, 6–14, 26 I, 27), irrationnelles (√ de polynôme ou de fraction : Ex. 4, 15–22, Act. 2–3), trigonométriques (sin, cos, fractions et composées en sin/cos : Ex. 5, 6, 23–26) ; parité, 2π-périodicité (vérification) pour restreindre l'étude ; tableau de variation, tracé en repère orthogonal/orthonormé ; décomposition f(x) = ax + b + c/(x − α)ⁿ (identification) ; discussion graphique du nombre de solutions de f(x) = k / de familles d'équations paramétrées ; dérivabilité à droite/gauche en un point (taux d'accroissement), demi-tangente verticale ; bijection et fonction réciproque en situation (existence, ensemble de définition, courbe symétrique, expression explicite, dérivée) ; suite uₙ₊₁ = f(uₙ) (Ex. 22) ; construction de |f(x)| (Ex. 6), f(|x|) (Ex. 17), de la courbe d'équation x² − y² + 3x − 4 = 0 (Ex. 16) ; encadrement à 10⁻¹ ou 10⁻⁴ près d'une racine/point annulant f' (calculatrice).
- ⛔ EXCLU : plan d'étude en 7 étapes ; définition générale d'une période T et théorème de restriction à [a, a+T] / translations kT i⃗ énoncés comme cours (restent ✅ la vérification f(x + 2π) = f(x) et le tracé répété sur [−2π ; 2π], Ex. 5, p.77) ; tg x et fonction réciproque tg⁻¹/arccos étudiées pour elles-mêmes ; changement de repère Y = F(X) ; translations/symétries de courbe avec encadré (f + k, −f) ; optimisation d'aire/longueur ; logiciel de géométrie ; fonctions ln, exp, puissances réelles, fonctions à paramètre n ; convexité (hors point d'inflexion) ; intégrales, primitives, équations différentielles ; développements limités ; courbes paramétrées ou polaires ; suite contractante et inégalité des accroissements finis ; QCM/Vrai-Faux corrigés (aucun corrigé imprimé : ne rien reprendre comme réponse, les résoudre soi-même).

### Lecture

- **Pages lues par l'OCR (couche texte)** : 67 à 84 (les 18 pages, entièrement).
- **Pages lues sur l'image (110 dpi, L3)** : 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84 — **18 pages sur 18** (chaque page à formule, encadré, tableau ou figure relue sur l'image ; toutes les pages de ce chapitre en contiennent). Sondage ≥ 1/10 : dépassé (100 %).
- **Écarts OCR / image constatés** (les plus denses : p.69, 71, 72, 75, 79, 81, 82, 83, 84) : l'OCR perd ou déforme systématiquement les racines (« Vx²+x+1 », « vx »), les fractions (« f(x) = x L 4 . x x » pour x√(1 + 1/x + 1/x²) en p.69), les indices (C4/C+/C£ pour C_f), les symboles ∞, ∈, ℝ, ≤ ; les tableaux de variation (p.72–79) sont illisibles ou absents du texte ; p.69 les trois cas de l'encadré sont lus sur l'image ; p.71 « f(x) = 1/8 x³ + x − 4 » est « 1/8 x³ » seulement sur l'image (p.71 : x³/8, f'(x) = 3x²/8 + 1 ; l'OCR « Le +1 » est faux) ; p.75 « f(x) = x + x² − 1 » (√ perdu) ; p.77 Ex. 6 : tableau de f' lu sur l'image ; p.79 le tableau du QCM est entièrement absent de l'OCR (lu sur l'image, doute levé en L3) ; p.81 Ex. 12 : l'OCR donne « P_k(x) = x ln − 6x² + kx + 1 » pour x⁴ − kx³ − 6x² + kx + 1 ; p.82 Ex. 15 : l'OCR « f(x) = ( 13. » pour √((x − 1/2)² + 3/4) ; p.83 Ex. 19 et Ex. 21 presque illisibles à l'OCR ; p.84 Ex. 26 II : « (sinx − 1)² » recomposé depuis l'image ; **aucun écart image/image** (les numéros d'exercices 1–27 sont encadrés sur l'image, l'OCR les perd). Coquille du manuel : p.72 « T à pour équation » (accent). L'Ex. 1 p.80 demande des limites lues sur une figure dont l'allure précise n'est pas exploitable en texte (à décrire à partir de l'image si la mission est reprise).
- Doutes levés en L3 (image p.79/82/83) : tableau du QCM p.79 (f décroît de 2 à 0 sur ]−∞ ; −1], croît de 0 à +∞ sur [−1 ; −0,5[, croît de −∞ à 3 sur ]−0,5 ; 0], décroît de 3 à −5 sur [0 ; +∞[) ; Ex. 18 p.82 : g(x) = x√x + 10, +10 hors de la racine ; Ex. 21 p.83 : f = −1/2 + x/(2√(x²+1)) et g⁻¹(x) = 1/(4x − 4) + 1 − x, conformes.

## 2.6 Chapitre 6 — Primitives (manuel 222433, p.85–98)

**Page de garde (p.85)** — Titre : « Primitives », Chapitre 6. Citation liminaire de Lagrange (1797) :
« Nous appellerons la fonction fx, fonction primitive, par rapport aux fonctions f′x, f″x, &c.qui en
dérivent, et nous appellerons celles-ci, fonctions dérivées, par rapport à celle-là » (« Cité dans
E.Haier et al, _L'analyse au fil de l'histoire_, 2000 » — même coquille source que dans le manuel
Mathématiques). Les primes de la citation sont perdues à l'OCR (« fx, f?x ») : reconstituées d'après la
citation du chapitre de référence (p.85 relue sur image (audit), aucun encadré ni formule).

**Plan** (3 parties numérotées, pas de page de sommaire) : I. Définition (p.86–87) ; II. Primitives des
fonctions usuelles et opérations (p.88–89) ; III. Calcul de primitives (p.89–93, avec 2 exercices résolus) ;
puis « QCM – VRAI – FAUX » (p.94) et « Exercices et problèmes » (p.95–98, 22 exercices). Pas de partie
« intégrale » : le chapitre s'arrête aux primitives.

### Cours — Activités

**I. Définition** (p.86–87)

- **Activité 1** (p.86) : f, F définies sur ℝ par f(x) = 3x² + 4x − 1 et F(x) = x³ + 2x² − x + 2. Vérifier
  que F′ = f ; déterminer une fonction G dérivable sur ℝ, distincte de F, telle que G′ = f. (Suivie de la définition.)
- **Activité 2** (p.86) : vérifier que F est une primitive de f sur I : 1. F(x) = 1/x ; f(x) = −1/x² ;
  I = [1, +∞[. 2. F(x) = x² ; f(x) = 2x ; I = ℝ. 3. F(x) = tan x ; f(x) = 1/cos²x ; I = ]−π/2, π/2[.
  (Suivie du théorème admis d'existence.)
- **Activité 3** (p.86–87) : repère orthogonal (O, i⃗, j⃗), courbe C_F de F(x) = x³ − x² − 4x sur [0, 3] et
  deux courbes C₁, C₂ images de C_F par des translations de vecteurs colinéaires à j⃗ (figure : C_F, C₁
  au-dessus, C₂ en dessous ; C₁ = image de C_F par la translation de vecteur 2j⃗, elle passe par (0 ; 2), C₂ par −4j⃗, elle passe par (0 ; −4) ; d'où G₁ = F + 2, G₂ = F − 4), G₁, G₂ les fonctions de courbes C₁, C₂. 1. déterminer la dérivée f de F ; que
  représente F pour f ? 2. déterminer G₁, G₂ ; 3. H primitive de f sur [0, 3] : justifier que la courbe
  de H est l'image de celle de F par une translation. (Suivie du théorème « F − G constante » avec sa
  démonstration, puis du corollaire avec sa démonstration.)
- **Activité 4** (p.87) : f, g, h définies sur ]0, +∞[ par f(x) = 1/√x + 2/(x + 2)² ; g : x ↦ sin x + cos x ;
  h : x ↦ sin x − cos x. Identifier parmi F₁ : x ↦ 2√x − 2/(x + 2) − 4 ; F₂ : x ↦ π − sin x − cos x ;
  F₃ : x ↦ −sin x − cos x − 1 ; F₄ : x ↦ sin x − cos x + π ; F₅ : x ↦ sin x − cos x celles qui sont des
  primitives sur ]0, +∞[ de l'une des fonctions précédentes.
- **Activité 5** (p.87) : F(x) = (2/3)x√x − (1/2)x² et f(x) = √x − x sur ]0, +∞[. 1. montrer que F est une
  primitive de f ; 2. déterminer la primitive G de f sur ]0, +∞[ telle que G(1) = 2.

**II. Primitives des fonctions usuelles et opérations** (p.88–89)

- **Activité 1** (p.88–89) : déterminer une primitive de f sur I. 1. f : x ↦ −2x² + 3x, I = ℝ.
  2. f : x ↦ −3/x² + 2/√x, I = ]0, +∞[. 3. f : x ↦ −2 cos x + 5 sin x, I = ℝ. 4. f : x ↦ cos(−2x) + sin(5x),
  I = ℝ. 5. f : x ↦ 2 + 2tan²(x), I = ]−π/2, π/2[. 6. f : x ↦ 2/x³ − 3/x⁴, I = [−3, −1].
- **Activité 2** (p.89) : quantité de substance chimique produite pendant les dix premières secondes : 12 g ;
  taux de production instantané (en g/s) Q′(t) = 40/t² + 200/t³, t ≥ 10. 1. déterminer la fonction Q (quantité
  produite au bout de t secondes, t ≥ 10) ; 2. tracer la courbe de Q ; 3. peut-on avoir 20 g produits ? pourquoi ?

**III. Calcul de primitives** (p.89–93)

- **Exercice résolu 1** (p.90–91, solution intégrale imprimée) : vérifier que f possède des primitives sur I et
  déterminer la primitive F telle que F(x₀) = y₀. 1. f : x ↦ (2x − 1)(x² − x + 3), I = ℝ, x₀ = 1, y₀ = 2.
  2. f : x ↦ (6x − 1)/(3x² − x)², I = ]1, +∞[, x₀ = 2, y₀ = 0. 3. f : x ↦ tan²x/cos²x, I = ]−π/2, π/2[,
  x₀ = −π/4, y₀ = −1. Solution : justification de l'existence par la continuité (polynôme / fonction rationnelle /
  quotient de fonctions continues à dénominateur non nul) ; reconnaissance de la forme u′u (u = x² − x + 3),
  u′/u² (u = 3x² − x), u′u² (u = tan x) ; primitives F_c(x) = ½(x² − x + 3)² + c, −1/(3x² − x) + c,
  ⅓tan³x + c ; la condition F(x₀) = y₀ fixe c : F(x) = ½(x² − x + 3)² − 5/2 ; F(x) = −1/(3x² − x) + 1/10 ;
  F(x) = ⅓tan³x − 2/3 (la solution écrit « définie sur ℝ » pour le cas 3 : coquille source, I = ]−π/2, π/2[).
- **Activité 1** (p.91) : même consigne (existence + F(x₀) = y₀). 1. f : x ↦ tan³x/cos²x + sin x,
  I = ]−π/2, π/2[, x₀ = −π/4, y₀ = −1. 2. f : x ↦ 2√x + (x + 1)/(2√x), I = ]0, +∞[, x₀ = 1, y₀ = −1.
  3. f : x ↦ √(2 − x) + 1/(2 − x)², I = ]−∞, 2[, x₀ = 1, y₀ = 0.
- **Activité 2** (p.91) : particule, vitesse initiale 3 m/s, accélération (en cm/s²) a(t) = 1 − 1/(2(√(t + 1))³) (radical sur t + 1, vu sur l'image p.91).
  1. vitesse à l'instant t ; 2. distance parcourue à l'instant t. (Unités incohérentes dans la source — m/s
  pour la vitesse, cm/s² pour l'accélération ; l'OCR lit « m/s² », l'image « cm/s² » : à signaler à l'auteur, ne pas corriger.)
- **Activité 3** (p.91) : f définie sur ]2, +∞[ par f(x) = (2x³ − 11x² + 20x − 10)/(x − 2)². 1. déterminer les
  réels a, b, c tels que f(x) = ax + b + c/(x − 2)² ; 2. en déduire une primitive de f sur ]2, +∞[.
- **Activité 4** (p.92) : 1. f(x) = sin²x : utiliser sin²x = (1 − cos 2x)/2 pour une primitive de f sur ℝ.
  2. g(x) = sin³x : utiliser sin³x = sin x(1 − cos²x) pour une primitive de g sur ℝ. 3. déterminer une primitive
  sur ℝ de x ↦ cos²x, puis de x ↦ cos³x.
- **Exercice résolu 2** (p.92–93, solution intégrale) : f(x) = (1 + x²)/(1 + x + x²) sur [0, +∞[, C_f dans un repère
  orthonormé (O, i⃗, j⃗). 1.a. étudier f et tracer C_f ; b. en déduire que ⅔ ≤ f(t) ≤ 1 pour tout t ≥ 0.
  2. F primitive de f qui s'annule en 0 : a. montrer ⅔x ≤ F(x) ≤ x ; b. en déduire lim_{+∞} F ; c. tableau de
  variation de F. 3.a. montrer que pour tout entier m ≥ 0 il existe un unique réel x_m tel que F(x_m) = m ;
  b. étudier les variations de la suite (x_m) et en déduire sa limite. Solution : f′(x) = (x² − 1)/(1 + x + x²)²,
  f décroissante de 1 à ⅔ sur [0, 1] puis croissante de ⅔ à 1, courbe avec asymptote y = 1 ; F′ = f donc
  ⅔ ≤ F′ ≤ 1, inégalités des accroissements finis sur [0, x] ; lim F = +∞ ; F continue strictement croissante
  = bijection de [0, +∞[ sur [0, +∞[, x_m = F⁻¹(m), suite croissante de limite +∞ (tableau de variation de F : F′ > 0, F de 0 à +∞).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur l'image)

> **Définition — primitive** (p.86) — « Soit f et F deux fonctions définies sur un intervalle I. On dit que F est
> une primitive de f sur I lorsque F est dérivable sur I et F′(x) = f(x), pour tout x de I. »

> **Théorème (admis) — existence** (p.86) — « Toute fonction continue sur un intervalle I admet au moins une
> primitive sur I. »

> **Théorème — deux primitives diffèrent d'une constante** (p.87) — « Soit f une fonction continue sur un
> intervalle I. Si F et G sont deux primitives de f sur I, alors la fonction F − G est constante sur I. »
> Démonstration : « Les fonctions F et G étant des primitives de f sur I, il en résulte que F′(x) − G′(x) = 0,
> pour tout x de I. Ce qui implique que F − G est constante sur I. »

> **Corollaire — primitive vérifiant une condition initiale** (p.87) — « Soit f une fonction continue sur un
> intervalle I. Soit x₀ un réel de I et y₀ un réel. Alors il existe une unique primitive F de f sur I telle que
> F(x₀) = y₀. » Démonstration : « L'unicité découle du théorème précédent. D'autre part, soit G une primitive de
> f sur I. La fonction F définie sur I par F(x) = G(x) − G(x₀) + y₀ est la primitive de f qui prend la valeur
> y₀ en x₀. »

> **Table — primitives des fonctions usuelles** (p.88) — « Dans le tableau ci-dessous F désigne une primitive de
> la fonction f sur l'intervalle I et a, c, ω et φ des réels avec ω ≠ 0. » Lignes (f | I | F) : x ↦ a | ℝ |
> x ↦ ax + c ; x ↦ xⁿ, n ∈ ℕ* | ℝ | x ↦ x^(n+1)/(n+1) + c ; x ↦ 1/xⁿ, n ∈ ℕ\{0,1} | ]0, +∞[ (ou ]−∞, 0[) |
> x ↦ x^(−n+1)/(−n+1) + c ; x ↦ √x | [0, +∞[ | x ↦ (2/3)x√x + c ; x ↦ 1/√x | ]0, +∞[ | x ↦ 2√x + c ;
> x ↦ cos x | ℝ | x ↦ sin x + c ; x ↦ sin x | ℝ | x ↦ −cos x + c ; x ↦ cos(ωx + φ) | ℝ |
> x ↦ (1/ω) sin(ωx + φ) + c ; x ↦ sin(ωx + φ) | ℝ | x ↦ −(1/ω) cos(ωx + φ) + c ; x ↦ 1 + tan²x |
> ]−π/2, π/2[ | x ↦ tan x + c.

> **Théorème — linéarité** (p.88) (introduit par « Le théorème ci-dessous découle des opérations sur les
> fonctions dérivables. ») — « Soit F et G deux primitives respectives de deux fonctions f et g sur un
> intervalle I. • La fonction F + G est une primitive sur I de f + g. • Soit λ un réel. La fonction λF est une
> primitive sur I de λf. »

> **Table — calcul de primitives (opérations)** (p.89) — « Dans le tableau suivant F désigne une primitive de la
> fonction f sur un intervalle I et u et v désignent deux fonctions dérivables sur I. » Lignes (f | Condition | F) :
> u′uⁿ, n entier naturel non nul | (aucune) | u^(n+1)/(n+1) ; u′v + v′u | (aucune) | u.v ;
> u′/uⁿ, n ∈ ℕ\{0,1} | u ne s'annule pas sur I | u^(−n+1)/(−n+1) ; (u′v − v′u)/v² | v ne s'annule pas sur I | u/v ;
> u′/√u | u strictement positive sur I | 2√u ; u′√u | u positive sur I | (2/3)u√u ;
> u′(w′∘u) | w une fonction dérivable sur u(I) | w∘u. (Table à 7 lignes : PAS de ligne « racine n-ième ».)

### Questions de contrôle

**QCM (p.94)** — « Cocher la réponse exacte. » (réponses non fournies)
1. x ↦ tan x est la primitive sur ]−π/2, π/2[ qui s'annule en 0 de (☐ x ↦ 1 + tan²x / ☐ x ↦ 1/sin²x / ☐ x ↦ sin²x).
2. La primitive sur ℝ de x ↦ sin x qui s'annule en 0 est (☐ x ↦ 1 − cos x / ☐ x ↦ −cos x / ☐ x ↦ cos x − 1).
3. La primitive sur ℝ qui s'annule en 0 de x ↦ 1 + cos x est (☐ paire / ☐ impaire / ☐ ni paire ni impaire).
4. La primitive sur ]−1, +∞[ de x ↦ 1/(1 − x)³ qui s'annule en 0 est (☐ x ↦ 1/(2(1 − x)²) − 1/2 /
   ☐ x ↦ 1/(4(1 − x)⁴) − 1/4 / ☐ x ↦ −1/(2(1 − x)²) + 1/2).
5. La primitive sur ℝ de x ↦ x cos x qui prend la valeur 1 en 0 est (☐ x ↦ (x²/2) sin x + 1 / ☐ x ↦ x sin x + cos x /
   ☐ x ↦ cos x − x sin x).

**Vrai – Faux (p.94)** — « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)
1. La primitive sur ℝ d'une fonction continue est une fonction continue sur ℝ.
2. x ↦ { x² sin(1/x) si x ∈ ℝ*, 0 si x = 0 } est une primitive sur ℝ de x ↦ { −cos(1/x) + 2x sin(1/x) si x ∈ ℝ*,
   0 si x = 0 }.
3. Si F est une primitive de f sur ℝ et G une primitive de g sur ℝ, alors F.G est une primitive de f.g sur ℝ.
4. Si F est une primitive de f sur ℝ, alors x ↦ F(2x) est une primitive de x ↦ f(2x) sur ℝ.
5. Si deux primitives d'une fonction f sur un intervalle I coïncident en un réel x₀ de I, alors elles sont égales.

### Exercices et problèmes (p.95–98) — 22 exercices

- **Ex. 1** (p.95) : déterminer les primitives F sur I de : 1. −5x⁴ + 2x − 3, ℝ. 2. x + 2 − 3/x², ]−∞, 0[.
  3. 3x/(3x² + 2)², ℝ. 4. (−x + 3)⁶, ℝ. 5. (x − 1)(x² − 2x + 7)⁴, ℝ. 6. 1/√(−4x + 3), ]−∞, 3/4[.
  7. cos(√x)/√x, ]0, +∞[. 8. (x² + 1)/(x³ + 3x)⁵, ]−∞, −√3[. 9. sin(2x + 1)cos⁴(2x + 1), ℝ. 10. x² sin(x³ + 1), ℝ.
  11. sin x/(cos x + 1)³, ]−π, π[. 12. (3x² + 4x − 2)/x⁴, ]−∞, 0[. 13. (2x − 1)/√(x² − x), ]1, +∞[. 14. tan²x, ]−π/2, π/2[.
- **Ex. 2** (p.95) : courbes (figures) de trois fonctions g, f, h dérivables sur [−2, 2]. 1. f admet une primitive parmi g
  et h : laquelle ? justifier ; 2. h admet une primitive parmi f et g : laquelle ? justifier. (Lecture graphique : figures non transcrites.)
- **Ex. 3** (p.95) : une primitive sur I de : 1. √(x + 1), ℝ*₊. 2. x√(x² + 1), ℝ. 3. (x − 3)√(x² − 6x), [6, +∞[.
  4. (x + 1)/√(x − 1), ]1, +∞[ (« on pourra écrire f(x) sous la forme a√(x − 1) + b/√(x − 1) »). 5. (x² + x)⁷(x + ½), ℝ.
  6. (1/x²)√((3 + x)/(2x)), ℝ*₊. 7. x(x + 1)²⁰⁰⁸, ℝ (« on pourra vérifier que f(x) = (x + 1)²⁰⁰⁹ − (x + 1)²⁰⁰⁸ »).
- **Ex. 4** (p.95–96) : vérifier l'existence de primitives et déterminer F avec F(x₀) = y₀ : 1. tan x + tan³x, [0, π/2[,
  F(π/4) = 1. 2. cos x − cos³x, ℝ, F(π/2) = −1. 3. sin x − sin³x, ℝ, F(−π/4) = 2. 4. (1 + tan x)/cos²x, [0, π/2[, F(π/4) = 0.
- **Ex. 5** (p.96) : 1. f(x) = cos x·cos(3x), g(x) = sin x·sin(3x) : a. une primitive sur ℝ de f + g et de f − g ; b. en déduire
  les primitives de f et g. 2. primitive sur ℝ qui s'annule en π de h(x) = (1 + cos x) sin(4x).
- **Ex. 6** (p.96) : f(x) = x sin x. 1. f deux fois dérivable et f(x) = 2 cos x − f″(x) ; 2. en déduire la primitive de f qui s'annule en π.
- **Ex. 7** (p.96) : f(x) = (x² + 2)/(x + 1)⁴ sur ]−1, +∞[ ; chercher a, b, c, d avec f(x) = a/(x + 1) + b/(x + 1)² + c/(x + 1)³
  + d/(x + 1)⁴. 1.a. calculer lim_{x→(−1)⁺}(x + 1)⁴f(x) et lim_{x→+∞}(x + 1)f(x) ; b. en déduire d = 3 et a = 0. 2.a. vérifier que
  (x − 1 − c)/(x + 1)³ = b/(x + 1)² ; b. en déduire b et c. 3. primitive de f sur ]−1, +∞[ égale à 2 en 0.
- **Ex. 8** (p.96) : f(x) = (2x + 1)/(x − 2)³ sur ℝ\{2}. 1. a, b tels que f(x) = a/(x − 2)² + b/(x − 2)³ ; 2. une primitive de f sur ]−∞, 2[.
- **Ex. 9** (p.96) : f(x) = 1/√(1 − x²) sur ]−1, 1[, F primitive nulle en 0, g(x) = F(sin x) sur ]−π/2, π/2[. 1. g dérivable,
  sa dérivée ; 2. en déduire g(x) = x ; 3. calculer F(√2/2), F(1/2), F(−√3/2).
- **Ex. 10** (p.96) : f(x) = √(1 − x²) sur [0, 1], F primitive nulle en 0, g(x) = F(cos x) sur [0, π/2]. 1. g dérivable, sa dérivée ;
  2. en déduire g(x) = −½x + ¼ sin 2x + π/4 ; 3. calculer F(1) et F(1/√2).
- **Ex. 11** (p.96) : toutes les fonctions deux fois dérivables sur I telles que : 1. f″(x) = 0, I = ℝ. 2. f″(x) = sin x, I = ℝ.
- **Ex. 12** (p.97) : 1. f(x) = |x| : a. f admet au moins une primitive sur ℝ ; b. la primitive F de f qui prend la valeur 0 en 4.
  2. g(x) = |x| + |x − 1| : a. g admet au moins une primitive sur ℝ ; b. une primitive G de g sur ℝ.
- **Ex. 13** (p.97) : f(x) = sin³x + sin⁵x sur ℝ : une primitive.
- **Ex. 14** (p.97) : mobile sur un axe, accélération a(t) = 1 − 1/(t + 1)², t ∈ [0, 10], en t = 0 à l'origine avec vitesse nulle.
  1. vitesse instantanée v(t) ; 2. vitesse et position pour t = 10.
- **Ex. 15** (p.97) : f(x) = √(4 − x²) sur [−2, 2]. 1.a. f admet au moins une primitive ; b. F primitive nulle en 0 : parité de F.
  2. G(x) = F(2 cos x) sur [0, π], courbe C (repère orthonormé) : a. I(π/2, 0) centre de symétrie de C ; b. G′(x), puis
  G(x) = π − 2x + sin 2x ; c. calculer F(1), F(2) et F(√2).
- **Ex. 16** (p.97) : u(x) = x + √(x² + 1) sur ℝ. 1. exprimer √(x² + 1) à l'aide de u(x) et u′(x) ; 2. primitives de
  f : x ↦ 1/((x + √(x² + 1))√(x² + 1)) et g : x ↦ (x + √(x² + 1))²/√(x² + 1).
- **Ex. 17** (p.97) : f : x ↦ x cos x et g : x ↦ x sin x. 1. en calculant f′(x) + g(x), une primitive G de g sur ℝ ;
  2. de même, une primitive F de f sur ℝ.
- **Ex. 18** (p.97) : n entier ≥ 2 (« supérieur à 2 »), Pₙ(x) = 1 + 2x + 3x² + … + nxⁿ⁻¹ sur ℝ. 1. la primitive Fₙ de Pₙ égale à 1 en 0 ;
  2. en déduire une autre expression de Pₙ(x).
- **Ex. 19** (p.97–98) : 1. g(x) = x sin x + cos x − 1 sur [0, π] : a. variations ; b. g(x) = 0 admet une solution α dans
  ]2π/3, π[, signe de g(x). 2. f(x) = (1 − cos x)/x si x ∈ ]0, π], 0 si x = 0 : a. continuité et dérivabilité en 0 ; b. variations
  sur [0, π] ; c. f(α) = sin α. 3. avec α ≈ 2,34 et f(α) ≈ 0,72, construire la courbe de f (repère orthonormé). 4. la restriction
  de f à [α, π] est une bijection de [α, π] sur un intervalle I à préciser. 5. h(x) = g(x) − 2 cos x sur [0, π] : h admet des
  primitives ; la primitive H de h qui prend la valeur 1 en 0.
- **Ex. 20** (p.98) : φ(x) = 1/(1 + x²), G primitive de φ sur ℝ nulle en 0. 1. G impaire. 2.a. ψ(x) = G(x) + G(1/x) sur ℝ* :
  ψ constante sur ]−∞, 0[ et sur ]0, +∞[ ; en déduire lim_{+∞} ψ = 2G(1) ; b. u(t) = G(tan t), t ∈ ]−π/2, π/2[ : u′(t) puis u(t).
  3. G(1), puis lim_{+∞} ψ et lim_{+∞} G. 4. construire la courbe de G (repère orthonormé).
- **Ex. 21** (p.98) : f(x) = √(1 + cos x) sur [0, π]. 1.a. f bijection de [0, π] sur [0, √2] ; b. f⁻¹ dérivable sur ]0, √2[ et
  (f⁻¹)′(x). 2. g(x) = 2/√(2 − x²) sur ]−√2, √2[, G primitive nulle en 0 : a. dérivée de x ↦ G(x) + G(−x), en déduire G impaire ;
  b. pour x ∈ [0, √2[, G(x) = π − f⁻¹(x) ; en déduire G(1).
- **Ex. 22** (p.98) : f continue sur [0, 1], dérivable sur ]0, 1[, f(0) = 1, f(1) = 0, f′(x) = −2/(π√(1 − x²)). 1. f bijection de
  [0, 1] sur [0, 1]. 2.a. f(cos x) = (2/π)x sur [0, π/2] ; b. en déduire f⁻¹(x). 3. h(x) = f(cos x) + f(sin x) sur [0, π/2] :
  a. h dérivable sur ]0, π/2[, h′(x) ; b. h(x) = 1. 4. φₙ(x) = cos((π/2)x) − xⁿ sur [0, 1], n ∈ ℕ* : a. unique aₙ ∈ ]0, 1[ avec
  φₙ(aₙ) = 0 ; b. si n > p alors φₙ(x) > φₚ(x) sur ]0, 1[ ; c. la suite (aₙ) est strictement croissante et convergente.

### Écart avec la référence (ch.5 de 222445, math-bac-math/05-primitives) — à reporter à la génération

**Ce que la référence enseigne et que CE manuel n'a PAS (à exclure)**
- **Ligne « racine n-ième » de la table des opérations** : u′·ⁿ√(u^(1−n)) ↦ n·ⁿ√u (n ∈ ℕ*\{1}, u > 0) ABSENTE ; la table du manuel
  Sciences expérimentales a 7 lignes (u′uⁿ, u′v+v′u, u′/uⁿ, (u′v−v′u)/v², u′/√u, u′√u, u′(w′∘u)). Aucun exercice n'en dépend.
- **Question 3 de l'exercice résolu (G(x) = F(x²))** : dérivabilité à droite en 0, variations de G, branche parabolique — ABSENTE ; remplacée
  par l'étude de la suite (x_m) définie par F(x_m) = m (bijection réciproque F⁻¹).
- **Activité III.1 à 5 cas** (dont (2x − 1)(x² − x + 3) et √(2 − x) en conditions initiales isolées, (6x − 1)/(3x² − x)², 2x√x + (x² + 1)/(2√x)) :
  ici 3 cas dans l'Exercice résolu 1 + 3 cas d'Activité 1, de contenu différent pour 2 d'entre eux (voir ci-dessous) ; Activité III.1.4 de la
  référence (2x√x + (x² + 1)/(2√x)) n'est pas reprise.
- Activité II.1.5 : la référence donne f(x) = tan²x ; ici « 2 + 2tan²(x) » (variante, même technique : 1 + tan²x).
- Tout le reste des 22 exercices et du QCM/Vrai-Faux est, d'après la lecture, identique en énoncé à la référence (même numérotation,
  mêmes données) : comparaison faite sur la fiche de référence, ligne à ligne pour les exercices 1 à 22 et les 10 questions de contrôle,
  aucun écart de données relevé hors ceux listés ici.

**Ce que ce manuel a EN PLUS de la référence**
- **Exercice résolu 1** (p.90–91) : trois cas résolus en entier (méthode « continuité → reconnaître u′uⁿ, u′/uⁿ, u′uⁿ → F_c → fixer c ») ;
  la référence n'a qu'un exercice résolu (celui de f = (1 + x²)/(1 + x + x²)).
- **Activité III.1 (p.91)** : cas 2 « 2√x + (x + 1)/(2√x) » et cas 3 « √(2 − x) + 1/(2 − x)² » combinés (variantes de la référence) ;
  cas 1 « tan³x/cos²x + sin x » (référence : tan³x/cos²x seul).
- **Exercice résolu 2, question 3** : suite (x_m) et bijection réciproque de F (voir ci-dessus).
- Démonstrations du théorème « F − G constante » et du corollaire (p.87) imprimées au cours (la référence les donne aussi : même contenu).

### Bornes de scope observées (chapitre 6)

- ✅ INCLUS : définition d'une primitive (F dérivable sur I, F′ = f) ; existence (toute fonction continue sur un intervalle admet au moins une
  primitive — théorème admis) ; « F − G constante » et unique primitive vérifiant F(x₀) = y₀ (avec démonstrations) ; table des primitives usuelles
  (a, xⁿ, 1/xⁿ, √x, 1/√x, cos, sin, cos(ωx + φ), sin(ωx + φ), 1 + tan²x) ; linéarité ; table d'opérations à 7 lignes (u′uⁿ, u′v + v′u,
  u′/uⁿ, (u′v − v′u)/v², u′/√u, u′√u, u′(w′∘u)) ; techniques : forme u′uⁿ / u′/uⁿ / u′√u / composée, décomposition « ax + b + c/(x − 2)² » et en
  éléments simples (a/(x + 1) + … + d/(x + 1)⁴, par limites), linéarisation sin²/cos² (cos 2x), sin³/cos³ (sin x(1 − cos²x)), produits cos·cos / sin·sin
  par somme et différence, fonction valeur absolue (existence d'une primitive par continuité) ; primitive avec condition initiale ; applications physiques
  (taux de production → quantité, accélération → vitesse → position) ; ponts avec parité, bijection réciproque (f⁻¹)′, suites (x_m), (aₙ).
- ⛔ EXCLU (non traité dans ce chapitre) : racine n-ième (ligne de table absente) ; notion d'intégrale, aire, notation ∫ ; intégration par parties nommée
  (seule la ligne « u′v + v′u ↦ uv ») ; fonctions ln/exp et leurs primitives ; équations différentielles ; dérivabilité à droite de G = F(x²) ;
  tout recours à la primitive de 1/x. DOUTE à signaler : Ex. 9, 10, 15, 20, 21, 22 supposent la fonction réciproque et sa dérivée, ainsi que les inégalités
  des accroissements finis (Ex. résolu 2) : leur présence dans le programme officiel Sciences expérimentales est à confirmer sur la fiche des chapitres 1–5 de CE
  manuel avant toute génération.

### Lecture

- **Pages lues par l'OCR (texte)** : 85–98 (14 pages, texte complet ; p.85 = page de garde, relue sur image (audit) : la citation porte bien f′x et f″x, et « E.Haier »).
- **Pages lues sur l'image (110 dpi)** : 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98 (13 pages = toutes les pages à formule, encadré, tableau ou figure) ;
  chaque encadré ci-dessus (définition, théorèmes, corollaire, démonstrations, deux tables, linéarité) est transcrit depuis l'image de sa page.
- **Sondage image** : 13 pages sur 14 (≥ 1 sur 10 requis, toutes les plus denses). Écarts OCR/image constatés (l'image fait foi) : exposants et indices perdus
  partout (« x? +2x2 » = x³ + 2x² p.86 ; « F(x)=tanx ; = ; 1-1, SL » = f(x) = 1/cos²x, I = ]−π/2, π/2[) ; p.87 Activité 4 : F₁–F₅ illisibles à l'OCR ;
  p.88 table des usuelles : flèches « ↦ » et signes − perdus, lignes 1/xⁿ et 1/√x mélangées ; p.89 Activité 1.5-6 : « 2+2tan?(x) » et I = [−3, −1]
  incomplets, table des opérations : fractions et racines désordonnées ; p.91 Activité 2 : l'OCR lit « (en m/s²) » alors que l'image porte « (en cm/s²) » ;
  p.92 : « Zx » pour (2/3)x ; p.93 : « Ê< f(t)<1 » pour ⅔ ≤ f(t) ≤ 1 ; p.94 QCM 4 : « ⁻¹ » et signes mêlés ; p.96 Ex. 9-10 : bornes et valeurs F(√2/2), F(1/2),
  F(−√3/2), F(1/√2) en désordre ; p.97 Ex. 19 : ]2π/3, π[ illisible, 4 − x² (Ex. 15) lu « Va » ; p.98 Ex. 21 : OCR « G(x)=x−f⁻¹(x) » alors que l'image porte
  « G(x) = π − f⁻¹(x) » (π perdu) ; Ex. 22 : f′(x) = −2/(π√(1 − x²)) dégradé. Figures (p.86 activité 3, p.92 courbe de f, p.95 Ex. 2) vues sur l'image mais non transcrites.
- **Doutes signalés** : (1) coquille source « Haier » (Hairer) dans la citation ; (2) corrigé de l'Exercice résolu 1.3 : « définie sur ℝ » au lieu de ]−π/2, π/2[ ;
  (3) unités de l'Activité III.2 (cm/s² pour a, m/s pour la vitesse initiale) ; (4) Ex. 1.8 : intervalle ]−∞, −√3[ lu tel quel sur l'image (x³ + 3x ne s'annule qu'en 0 sur ℝ,
  l'intervalle est valable mais non maximal) ; (5) réponses du QCM / Vrai-Faux non fournies par le manuel ; (6) QCM 4 : intervalle ]−1, +∞[ incompatible avec 1/(1 − x)³ (non définie en 1) ; ]−1, 1[ ou ]−∞, 1[ attendu ; transcrit tel quel.

## 2.7 Chapitre 7 — Intégrales (manuel 222433, p.99–122)

**Page de garde (p.99)** — « Chapitre 7 — Intégrales ». Citation liminaire : « La parabole considérée
par Thabit Ibn Qurra est définie par une propriété que nous traduisons aujourd'hui par l'équation
y² = px et la quadrature de la parabole est équivalente à notre calcul de l'intégrale ∫₀ᵃ √(px).
Mais le calcul immédiat d'une telle intégrale, […], aurait exigé la sommation de […] √1 + √2 + … + √n.
Ibn Qurra étudie cette difficulté en recourant à un artifice astucieux. […]. » (AP. Youschkevitch,
_Les mathématiques arabes_, 1976) ; légende : « Thabit Ibn Qurra est un mathématicien arabe qui vécut
au Xe siècle ». (Même citation que la référence ; borne supérieure « a » lue sur l'image, absente de l'OCR.)

**Plan du chapitre** (pas de sommaire imprimé ; sections lues dans le corps) : I. Définition (I.1
intégrale d'une fonction continue et positive ; I.2 intégrale d'une fonction continue) · II. Propriétés
algébriques de l'intégrale · III. Intégrales et inégalités · IV. Calculs d'intégrales (IV.1 au moyen
d'une primitive ; IV.2 intégration par parties ; IV.3 calcul approché, méthode des rectangles ; IV.4
valeur moyenne et inégalité de la moyenne) · V. Calcul de volumes de solides de révolution · VI.
Fonctions définies par une intégrale · puis « QCM – VRAI – FAUX » (p.117) · « Exercices et problèmes »
(p.118–122, exercices 1 à 35). **Pas de section « suites définies par une intégrale »** (cf. Écart).

### Cours — Activités (préliminaires et de cours)

**I.1** (p.100) — encadré rose : unité d'aire (voir « Encadrés »).
- **Activité 1** (p.100) : f(x) = x + 2 ; 𝒫 limitée par l'axe, C_f, x = −2, x = 0. 1. tracer C_f ;
  3. calculer l'aire 𝒜 de 𝒫 ; 4. a. primitive F de f sur ℝ avec F(0) = 1 ; b. vérifier 𝒜 = F(0) − F(−2) ;
  c. si G autre primitive, 𝒜 = G(0) − G(−2). (Suivie de la Propriété F(b)−F(a)=G(b)−G(a) + démonstration
  puis de la Définition de l'intégrale positive.) [OCR : l'énoncé « 2. soit 𝒫… » contient la question 2 et
  la 3 est « Calculer l'aire » ; numérotation lue sur l'image.]

**I.2** (p.101)
- **Activité 2** (p.101) : f : x ↦ x³ − (3/2)x² ; 1. représenter 𝒫 limitée par l'axe, C_f, x = 2, x = 3 ;
  2. calculer l'aire de 𝒫. (Placée avant la Définition I.2.)
- **Activité 3** (p.101) : calculer ∫_{1/2}^{1} (x² − 1)dx ; ∫₀¹ sin(2x + 3)dx ; ∫_{−1}¹ 2x/(x² + 1)² dx.

**II** (p.102–103)
- **Activité 1** (p.102) : f(x) = −x² − 1 ; 1. représenter f ; 2. aire limitée par la courbe de −f, l'axe,
  x = −1, x = 2 ; 3. en déduire que l'aire limitée par C_f, l'axe, x = −1, x = 2 est ∫_{−1}² −f(x)dx.
- **Activité 2** (p.102) : C de f(x) = x³ tracée ; 1. tracer C′ de |f| ; 2. a. représenter P′ limitée par
  l'axe, C′, x = −2, x = 3 ; b. aire de P′ ; 3. en déduire l'aire de P (axe, C, x = −2, x = 3). (Suivie de la
  Définition de l'aire via ∫|f|.)
- **Activité 3** (p.103) : aire limitée par l'axe, C_f, x = a, x = b pour 1. f : x ↦ cos 3x, a = −π/3,
  b = π/4 ; 2. f : x ↦ x(x² + 1)², a = −2, b = 1. (Suivie du Théorème de linéarité + démonstration.)
- **Activité 4** (p.103) : calculer ∫₁² x²/(x + 1)² dx + ∫₁² (2x + 1)/(x + 1)² dx.
- **Activité 5** (p.103) : I = ∫₀^{π/2} sin²x dx, J = ∫₀^{π/2} (cos²x)/2 dx ; 1. calculer I + 2J et 2J − I ;
  2. en déduire I et J.

**III** (p.104–106)
- **Exercice résolu 1** (p.104) : 1. montrer 1/(1 + x) > 1 − x pour x ∈ ]0, 1] ; 2. montrer
  ∫₀¹ x/(1 + x²) dx > 1/4. Solution : (1 − x)(1 + x) = 1 − x² < 1 ; d'où 1/(1 + x²) > 1 − x² ;
  ∫₀¹ (x − x³)dx = 1/4.
- **Exercice résolu 2** (p.105) : 1. pour x ≥ 0 (énoncé : x > 0), −x ≤ sin x ≤ x ; 2. en déduire
  1 − x²/2 ≤ cos x. Solution : −1 ≤ cos t ≤ 1 intégré sur [0, x] ; puis ∫₀ˣ sin t dt ≤ ∫₀ˣ t dt, soit
  1 − cos x ≤ x²/2.
- **Activité 1** (p.105) : f dérivable sur [−1, 4], tangentes aux abscisses 0 et 3 tracées ; 1. vérifier
  graphiquement x/2 ≤ f(x) ≤ (x + 1)/2 sur [0, 3] ; 2. en déduire 9/4 ≤ ∫₀³ f(x)dx ≤ 15/4.
- **Activité 2** (p.106) : uₙ = ∫₀¹ x^{n+1}/(1 + x²) dx (n ∈ ℕ) ; 1. 0 ≤ x^{n+1}/(1 + x²) ≤ x^{n+1} sur [0, 1] ;
  2. en déduire 0 ≤ uₙ ≤ 1/(n + 2) ; 3. a. valeur approchée de u₁₀₀ et erreur ; b. de u₁₀₀₀₀ et erreur.
- **Activité 3** (p.106) : f(x) = x, g(x) = x³ sur [−1/2, 1] (figure) ; aire limitée par C_f, C_g, x = −1/2,
  x = 1. 1. a. aire sous C_f (x = 0 à 1) ; b. sous C_g (x = 0 à 1) ; c. en déduire l'aire entre C_f et C_g
  (x = 0 à 1) ; 2. aire entre C_f et C_g (x = −1/2 à 0) ; 3. conclure. (Suivie de la Définition de l'aire
  entre deux courbes via ∫|f − g|.)
- **Activité 4** (p.107) : f = sin, g = cos sur [0, π/2] ; 1. représenter ; 2. signe de f − g ; 3. aire entre
  C_f et C_g, x = 0, x = π/2.

**IV.1 Calcul au moyen d'une primitive**
- **Activité 1** (p.107) : calculer ∫₀³ (5x⁴ − x³ − 2)dx ; ∫_{−2}^{−1} 1/t² dt ; ∫₀^{π/4} 1/cos²x dx ;
  ∫_{−1}² (3x² + 1)(x³ + x − 2)dx ; ∫₀¹ −2u/(u² + 2)³ du ; ∫_{π/6}^{π/2} cos t/sin³t dt ;
  ∫₀^{π/2} cos x sin³x dx ; ∫₀¹ x³/√(x⁴ + 1) dx. (Pas de seconde activité IV.1.)

**IV.2 Intégration par parties** (p.107–108) — Théorème + démonstration (voir « Encadrés »).
- **Exercice résolu 3** (p.108) : I = ∫₀^{π/2} x sin x dx ; J = ∫₀^{π/2} x cos x dx ; K = ∫₀^{π/2} x² cos x dx.
  Solution par tableau « Posons u, u′, v′, v » : I = 1 ; J = π/2 − 1 ; K = π²/4 − 2I = π²/4 − 2.

**IV.3 Méthode des rectangles** (p.108–109)
- **Activité 2** (p.108–109) [numérotée « Activité 2 », il n'y a pas d'activité 1 en IV.3] : f(x) = 1/x sur
  ]0, +∞[ ; A l'aire limitée par l'axe, la courbe, x = 1, x = 2. 1. vérifier A = ∫₁² dx/x ; 2. rectangles r₁
  et R₁ (schéma) : vérifier 1/2 ≤ A ≤ 1 ; 3. [1, 2] en 2 intervalles de longueur 0.5, rectangles r₁, r₂,
  R₁, R₂ : vérifier 7/12 ≤ A ≤ 5/6 ; 4. [1, 2] en 5 intervalles de longueur 1/5, rectangles rᵢ, Rᵢ
  (1 ≤ i ≤ 5) : donner un nouvel encadrement de A. (Aucun encadré de méthode.)

**IV.4 Valeur moyenne** (p.109–110)
- **Activité 3** (p.109) : f(x) = 3x − 1 sur [0, 2] ; valeur moyenne de f sur [0, 2], puis la comparer à f(1).
- **Activité 4** (p.110) : valeur moyenne de f(x) = cos x sur [0, π/2].
- **Exercice résolu 4** (p.110–111) : montrer 0.5 ≤ ∫₀¹ 1/(1 + x²) dx ≤ 1 et
  1/2 ≤ ∫₀^{1/2} 1/√(1 − x²) dx ≤ √3/3. Solution : 0.5 ≤ 1/(1 + x²) ≤ 1 sur [0, 1] ; 3/4 ≤ 1 − x² ≤ 1 sur
  [0, 1/2], d'où 1 ≤ 1/√(1 − x²) ≤ 2/√3, puis intégration.

**V. Volumes de solides de révolution** (p.111–112) — texte de définition (arc AB, surface de révolution
(S), solide de révolution, section = disque de rayon HM, aire S(x) = πy² = πf²(x)) puis formule (voir
« Encadrés »).
- **Activité** (p.112) : solide S engendré par la rotation autour de (Ox) de l'arc AB de y = √x,
  A(0, 0), B(4, 2) (figure) ; déterminer le volume de S. (Seule activité de la section ; pas de sphère.)

**VI. Fonctions définies par une intégrale** (p.112–116)
- **Activité 1** (p.112) : justifier la dérivabilité de F sur I et calculer F′ : 1. F(x) = ∫₁ˣ √(1 − t²)dt,
  I = [−1, 1] ; 2. F(x) = ∫₀ˣ 1/(1 + t²) dt, I = ℝ ; 3. F(x) = ∫₁ˣ (sin t)/t dt, I = ]0, +∞[ ;
  4. F(x) = ∫₀ˣ dt/√(1 − t²), I = ]−1, 1[.
- **Activité 2** (p.113) : f continue sur I centré en 0 ; g(x) = ∫_{−x}ˣ f(t)dt. 1. g dérivable, dérivée ;
  2. f impaire : a. g(x) = 0 ; b. ∫_{−x}⁰ f = −∫₀ˣ f ; 3. f paire : a. g primitive de t ↦ 2f(t) s'annulant en 0 ;
  b. ∫_{−x}ˣ f = 2∫₀ˣ f et ∫_{−x}⁰ f = ∫₀ˣ f. (Suivie du Théorème de parité.)
- **Activité 3** (p.113) : calculer ∫_{−5π}^{5π} x⁵ sin⁶(x)dx ; ∫_{−1}¹ t⁵/(t⁶ + 1) dt ;
  ∫_{−5π}^{5π} x^{1001} cos^{100}(x)dx ; ∫_{−1}¹ |t³ + t|dt.
- **Activité 4** (p.113) : f continue sur ℝ, de période T ; g(x) = ∫ₓ^{x+T} f(t)dt ; montrer g(x) = ∫₀ᵀ f(t)dt.
  (Suivie du Théorème de périodicité.)
- **Activité 5** (p.114) : calculer ∫₀^{20π} |sin x|dx ; ∫_{−10π}^{10π} |cos x|dx.
- **Exercice résolu 5** (p.114–115) : F(x) = ∫₁ˣ (1 − cos t)/t² dt sur [1, +∞[. 1. a. F croissante ; b. F majorée
  par 2 ; c. F admet une limite finie L en +∞. 2. G(x) = ∫₁ˣ (sin t)/t dt ; par IPP (u(t) = 1/t,
  v(t) = 1 − cos t) montrer G(x) = F(x) + (1 − cos x)/x + cos 1 − 1 ; en déduire que G a une limite finie
  en +∞ : L + cos 1 − 1. (Identique à l'exercice résolu 1 de la référence.)
- **Exercice résolu 6** (p.115–116) : f(x) = ∫₀ˣ dt/√(1 − t²) sur [0, 1[. 1. f dérivable, f′(x) = 1/√(1 − x²) ;
  2. g(x) = ∫₀^{sin x} dt/√(1 − t²) sur [0, π/2[ : a. g dérivable (composée de f et u : x ↦ sin x, u([0, π/2[) = [0, 1[) [le manuel imprime « g est dérivable sur [0,1[ » (coquille ; lire [0, π/2[)],
  g′(x) = u′(x)×f′(u(x)) = 1 ; b. g(x) = x ; 3. ∫₀^{1/2} dt/√(1 − t²) = π/6 ; ∫₀^{√3/2} dt/√(1 − t²) = π/3 ;
  4. a. pour x ∈ [0, 1[ il existe un unique t ∈ [0, π/2[ avec sin t = x ; b. lim_{x→1⁻} f(x) = π/2 ;
  5. tableau de variation et représentation de f (demi-tangente à l'origine tracée).

### Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Unité d'aire** (p.100, encadré rose) — « Le plan étant muni d'un repère orthogonal (O, i⃗, j⃗), l'unité
> d'aire, notée par u.a est l'aire du rectangle de dimensions ‖i⃗‖ et ‖j⃗‖. »

> **Propriété** (p.100) — « Soit f une fonction continue sur un intervalle I. Si F et G sont deux primitives
> de f sur I alors pour tous a et b de I, F(b) − F(a) = G(b) − G(a). » Démonstration : « Les fonctions F et
> G étant des primitives de f sur I, la fonction F − G est constante sur I. On en déduit que pour tous
> réels a et b de I, F(b) − G(b) = F(a) − G(a). La propriété en découle. »

> **Définition (intégrale d'une fonction continue et positive)** (p.100) — « Le plan est muni d'un repère
> orthogonal. Soit f une fonction continue et positive sur un intervalle [a, b] et F une primitive de f sur
> [a, b]. L'aire (en u.a) de la partie du plan limitée par la courbe de f, l'axe des abscisses et les droites
> d'équations x = a et x = b est le réel F(b) − F(a). Le réel F(b) − F(a) est appelé intégrale de f de a à b
> et est noté ∫ₐᵇ f(x)dx. »

> **Définition (intégrale d'une fonction continue)** (p.101) — « Soit f une fonction continue sur un
> intervalle I, a et b deux réels de I et F une primitive de f sur I. On appelle intégrale de f entre a et
> b le réel, noté ∫ₐᵇ f(x)dx, défini par ∫ₐᵇ f(x)dx = F(b) − F(a). »

> **Vocabulaire et notations** (p.101) — « • Le réel ∫ₐᵇ f(x)dx est appelé intégrale de f sur [a, b]
> lorsque a ≤ b, ou encore de a à b, ou encore entre a et b. • Dans l'écriture ∫ₐᵇ f(x)dx, on peut
> remplacer la lettre x par n'importe quelle lettre et on peut écrire ∫ₐᵇ f(x)dx = ∫ₐᵇ f(u)du = ∫ₐᵇ f(t)dt.
> On dit que x est une variable muette. • Pour toute primitive F de f, on écrit
> ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a). L'expression [F(x)]ₐᵇ se lit « F(x) pris entre a et b ». »
> (Écart avec la référence : « lorsque a ≤ b » ici ; la référence ne note pas cette condition.)

> **Propriétés algébriques** (p.102) — « Soit f une fonction continue sur un intervalle I, a, b et c des
> réels de I. Alors ∫ₐᵃ f(x)dx = 0 ; ∫ₐᵇ f(x)dx = −∫ᵦᵃ f(x)dx. ∫ₐᶜ f(x)dx + ∫꜀ᵇ f(x)dx = ∫ₐᵇ f(x)dx
> (Relation de Chasles). » Démonstration : « Soit F une primitive de f sur I. ∫ₐᵃ f(x)dx = F(a) − F(a) = 0.
> ∫ₐᵇ f(x)dx = F(b) − F(a) = −(F(a) − F(b)) = −∫ᵦᵃ f(x)dx. ∫ₐᶜ f(x)dx + ∫꜀ᵇ f(x)dx =
> (F(c) − F(a)) + (F(b) − F(c)) = F(b) − F(a) = ∫ₐᵇ f(x)dx. »

> **Définition (aire, fonction de signe quelconque)** (p.103) — « Le plan est muni d'un repère orthogonal.
> Soit f une fonction continue sur [a, b]. L'aire (en u.a) de la partie du plan limitée par l'axe des
> abscisses, la courbe de f, les droites d'équations x = a et x = b est le réel ∫ₐᵇ |f(x)|dx. »

> **Théorème (linéarité)** (p.103) — « Soit f et g deux fonctions continues sur [a, b]. Pour tous réels α
> et β, ∫ₐᵇ (αf(x) + βg(x))dx = α∫ₐᵇ f(x)dx + β∫ₐᵇ g(x)dx. » Démonstration : F, G primitives de f, g ;
> αF + βG est une primitive de αf + βg ; (αF(b) + βG(b)) − (αF(a) + βG(a)) = α(F(b) − F(a)) +
> β(G(b) − G(a)).

> **Théorème (positivité)** (p.104) — « Soit f une fonction continue sur [a, b]. Si f est positive sur
> [a, b], alors ∫ₐᵇ f(x)dx ≥ 0. » Démonstration : « Toute primitive sur [a, b] d'une fonction positive est
> croissante sur [a, b]. Le théorème en découle. »

> **Corollaire** (p.104) — « Soit f une fonction continue sur [a, b] où a < b. Si f est positive et ne
> s'annule qu'en un nombre fini de réels de [a, b], alors ∫ₐᵇ f(x)dx > 0. » Démonstration : primitive
> strictement croissante.

> **Corollaire (comparaison)** (p.104) — « Soit f, g et h trois fonctions continues sur [a, b]. Si
> h ≤ f ≤ g, alors ∫ₐᵇ h(x)dx ≤ ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx. » Démonstration (p.105) : f − h positive, donc
> ∫(f − h) ≥ 0 ; « On montre de même que ∫ₐᵇ g(x)dx ≥ ∫ₐᵇ f(x)dx. »

> **Corollaire** (p.105) — « Si f est une fonction continue sur [a, b], alors |∫ₐᵇ f(x)dx| ≤ ∫ₐᵇ |f(x)|dx. »
> Démonstration : « La propriété découle du corollaire précédent et de la double inégalité
> −|f| ≤ f ≤ |f|. »

> **Définition (aire entre deux courbes)** (p.106) — « Le plan est muni d'un repère orthogonal. Soit f et g
> deux fonctions continues sur [a, b]. L'aire (en u.a) de la partie du plan limitée par la courbe de f, la
> courbe de g et les droites d'équations x = a et x = b est le réel ∫ₐᵇ |f(x) − g(x)|dx. »

> **Théorème d'intégration par parties** (p.107) — « Soit f et g deux fonctions dérivables sur [a, b] et
> telles que leurs dérivées f′ et g′ sont continues sur [a, b]. Alors
> ∫ₐᵇ f(t)g′(t)dt = [f(t)g(t)]ₐᵇ − ∫ₐᵇ f′(t)g(t)dt. » Démonstration : (fg)′ = f′g + g′f ; la continuité de f′
> et g′ permet d'écrire ∫ₐᵇ (fg)′(x)dx = ∫ₐᵇ (f′(x)g(x) + g′(x)f(x))dx = [f(x)g(x)]ₐᵇ.

> **Définition (valeur moyenne)** (p.109) — « Soit f une fonction continue sur [a, b] tel que a < b. On
> appelle valeur moyenne de f sur [a, b] le réel, noté f̄, défini par f̄ = 1/(b − a) · ∫ₐᵇ f(x)dx. »

> **Interprétation géométrique de la valeur moyenne** (p.109) — « Le plan est muni d'un repère orthogonal.
> Soit f une fonction continue et positive sur [a, b]. L'aire (en u.a) de la partie du plan limitée par la
> courbe de f, les droites d'équations, x = a, x = b et y = 0 est égale à celle du rectangle de côtés
> (b − a) et f̄. »

> **Théorème (Inégalité de la moyenne)** (p.110) — « Soit f une fonction continue sur [a, b] tel que a < b.
> Soit m et M deux réels. Si pour tout x de [a, b], m ≤ f(x) ≤ M, alors m ≤ f̄ ≤ M. » Démonstration :
> ∫ₐᵇ m dx ≤ ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ M dx, avec ∫ₐᵇ m dx = m(b − a) et ∫ₐᵇ M dx = M(b − a), b − a > 0.

> **Corollaire** (p.110) — « Soit f une fonction continue sur [a, b] tel que a < b. Il existe c ∈ [a, b],
> tel que f̄ = f(c). » Démonstration : f([a, b]) = [m, M] (f continue) et m ≤ f̄ ≤ M.

> **Formule du volume d'un solide de révolution** (p.111) — « L'espace est muni d'un repère orthonormé
> (O, i⃗, j⃗, k⃗). Soit f une fonction continue et positive sur [a, b]. Le volume V du solide de révolution
> engendré par la rotation de l'arc AB = {M(x, y) tels que y = f(x) et a ≤ x ≤ b} autour de l'axe (O, i⃗)
> est le réel V = π ∫ₐᵇ f²(x)dx. » (La formule est « donnée », non démontrée : « Nous donnons ci-dessous la
> formule… ».)

> **Théorème (fonction définie par une intégrale)** (p.112) — « Soit f une fonction continue sur un
> intervalle I et a un réel de I. Alors la fonction F définie sur I par F(x) = ∫ₐˣ f(t)dt est la primitive
> de f qui s'annule en a. » Démonstration : G primitive de f ; ∫ₐˣ f(t)dt = G(x) − G(a), donc F dérivable
> sur I et F′ = f ; F(a) = ∫ₐᵃ f(t)dt = 0.

> **Corollaire** (p.112) — « Soit f une fonction continue sur un intervalle I et a un réel de I. Alors la
> fonction F : x ↦ ∫ₐˣ f(t)dt est dérivable sur I et F′(x) = f(x), pour tout x de I. »

> **Théorème (parité)** (p.113) — « Soit f une fonction continue sur un intervalle I centré en 0 et soit a
> un réel de I. • Si f est impaire alors ∫_{−a}ᵃ f(x)dx = 0. • Si f est paire alors
> ∫_{−a}ᵃ f(x)dx = 2∫₀ᵃ f(x)dx. »

> **Théorème (périodicité)** (p.113) — « Soit f une fonction continue sur ℝ, périodique de période T.
> Pour tout réel a, ∫ₐ^{a+T} f(t)dt = ∫₀ᵀ f(t)dt. »

Aucun encadré « Méthode » ni « Remarque » dans le chapitre ; les seules méthodes rédigées sont les
solutions des exercices résolus 1 à 6.

### QCM – VRAI – FAUX (p.117)

**QCM** « Cocher la réponse exacte. » 1. D'après la représentation graphique (courbe croissante partant de l'axe en x = −2
et atteignant environ 3 en x = 3), l'aire limitée par la courbe de f, l'axe des abscisses, x = −2 et x = 3
est comprise entre (☐ 7 et 13 / ☐ 15 et 20 / ☐ 14 et 21). 2. I = ∫₀¹ t cos²(πt)dt et J = ∫₀¹ t sin²(πt)dt :
I + J est égal à (☐ 1 / ☐ 1/2 / ☐ 0). 3. I = |∫_{−1}¹ (−3x³ + 5x)dx| et J = ∫_{−1}¹ |−3x³ + 5x|dx :
(☐ I ≤ J / ☐ I = J / ☐ I ≥ J).
**VRAI – FAUX** « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)
1. ∫₀^{π/2} sin x dx = ∫_{4π}^{9π/2} sin x dx. 2. ∫_{−1}¹ |x|dx = 1. 3. Si f est dérivable sur [a, b] et si sa
dérivée est continue sur [a, b], alors ∫ₐᵇ f(x)dx = [xf(x)]ₐᵇ − ∫ₐᵇ x f′(x)dx. 4. f continue sur [0, 1] :
si f ≤ 1 alors ∫₀¹ f(x)dx ≤ 1. 5. D'après la représentation graphique (courbe de −2 à 2), ∫_{−2}² f(x)dx ≥ 0.
6. Si ∫ₐᵇ f(x)dx ≥ 0 alors f ≥ 0 sur [a, b]. 7. La fonction x ↦ ∫₀ˣ 1/(1 + t²) dt est définie sur ℝ.

### Exercices et problèmes (p.118–122) — 35 exercices

- **Ex. 1** (p.118) : calculer ∫_{−1}³ (x²/2 − x)dx ; ∫₁² t(t + 1)³dt ; ∫_{−1}¹ (2x + 1)(x² + x − 5)³dx ;
  ∫₁² √(2x + 1)dx ; ∫₁² dx/(1 + x)² ; ∫₁² 2/(3x − 1)² dx ; ∫₀⁴ dx/√(2x + 1) ; ∫₁² (x + 1)/√(x² + 2x) dx ;
  ∫_{−2}¹ |x(x + 1)|dx ; ∫_{−3}³ |x³ + x|dx ; ∫₀³ |2t − 1|dt ; ∫_{−3}⁰ |x² − x − 2|dx ; ∫₀^π cos³x dx ;
  ∫₀^{π/4} tan²x dx ; ∫₀^{π/6} sin 2x/cos³2x dx ; ∫₀^{π/6} sin x/cos²x dx ; ∫₀^{π/4} cos⁴t sin t dt ; ∫₀^{2π} |sin x|dx.
- **Ex. 2** (p.118) : 1. a, b tels que (6x² − 12x + 42)/(x − 1)² = a + b/(x − 1)², x ≠ 1 ; 2. calculer
  ∫_{−1}⁰ (6x² − 12x + 42)/(x − 1)² dx.
- **Ex. 3** (p.118) : f(x) = x/(x − 1)⁴, x ≠ 1. 1. a, b tels que f(x) = a/(x − 1)³ + b/(x − 1)⁴ ;
  2. calculer ∫₂³ (x + 1)/(x − 1)⁴ dx. **[Doute : l'intégrande de la question 2 est (x + 1)/(x − 1)⁴, différent de
  f(x) = x/(x − 1)⁴ de la question 1 — incohérence possible du manuel, lue ainsi sur l'image.]**
- **Ex. 4** (p.118) : A = ∫₀¹ x/(1 + x²)³ dx, B = ∫₀¹ x³/(1 + x²)³ dx. 1. calculer A ; 2. calculer A + B ;
  3. en déduire B.
- **Ex. 5** (p.118) : repère orthonormé, a > 0 ; parabole y = x² et droite y = a (figure, parties D₁ sous la
  droite, D₂ au-dessus jusqu'à y = 4) : pour quelle valeur de a les parties D₁ et D₂ ont-elles la même aire ?
- **Ex. 6** (p.118) : f : x ↦ (x² − 4x − 2)/(x − 2)². 1. vérifier f(x) = 1 − 6/(x − 2)², x ≠ 2 ; 2. étudier f
  et construire C ; 3. aire limitée par l'axe, C, x = 3, x = 5.
- **Ex. 7** (p.118) : f(x) = (2x − 1)/(x − 1)³ sur ℝ\{1}. 1. étudier f et tracer C ; 2. a, b tels que
  f(x) = a/(x − 1)² + b/(x − 1)³ ; 3. λ < 1/2, 𝒜(λ) l'aire limitée par C, l'axe, x = λ, x = 1/2 : a. déterminer
  𝒜(λ) ; b. calculer lim_{λ→−∞} 𝒜(λ).
- **Ex. 8** (p.119) : 1. h(x) = x² − 4x + 6 − 3√x sur ]0, +∞[ : a. h″(x) ; b. h′(x) = 0 admet une unique
  solution α ∈ ]2, 3[ ; c. signe de h′, tableau de variation ; d. h(1), h(4) ; en déduire que 1 et 4 sont les
  uniques solutions de h(x) = 0. 2. a. représenter f(x) = x² − 4x + 6 et g(x) = 3√x ; b. aire limitée par ces
  deux courbes.
- **Ex. 9** (p.119) : f(x) = cos x, g(x) = cos²x sur [0, π]. 1. étudier f et g ; 2. position de C_f, C_g ;
  3. représenter ; 4. aire limitée par ces deux courbes.
- **Ex. 10** (p.119) : f(x) = 5 − x², g(x) = 4/x² sur ]0, +∞[. 1. position relative de C et C′ ;
  2. représenter ; 3. aire limitée par les deux courbes, x = 0.5, x = 5.
- **Ex. 11** (p.119) : f(x) = x + 1 + 4/(x − 2)², g(x) = x + 1 sur ]2, +∞[. 1. représenter ; 2. λ > 2, 𝒜(λ)
  l'aire limitée par C_f, C_g, x = 3, x = λ : a. vérifier 𝒜(λ) = |∫₃^λ 4dx/(x − 2)²| ; b. calculer 𝒜(λ) ;
  c. étudier et représenter 𝒜 : λ ↦ 𝒜(λ) ; d. selon m, nombre de solutions de 𝒜(λ) = m.
- **Ex. 12** (p.119) : 1. par IPP, calculer ∫₀^π x cos x dx et ∫₀^π x sin x dx ; 2. en déduire
  ∫₀^π x² cos x dx et ∫₀^π x² sin x dx. [Bornes supérieures lues « π » sur l'image ; l'OCR les rend « a ».]
- **Ex. 13** (p.119) : f(x) = 1/√(1 + x⁴) sur ℝ₊, I = ∫_{100}^{1000} f(t)dt. 1. a. vérifier f(x) ≤ 1/x² (x > 0) ;
  b. par l'inégalité des accroissements finis, 1 − x/2 ≤ 1/√(1 + x) (x > 0) ; c. en déduire
  1/x² − 1/(2x⁶) ≤ f(x) (x > 0) ; 2. encadrement de I.
- **Ex. 14** (p.119) : 1. calculer ∫₀^{π/4} dx/cos²x ; 2. f(x) = sin x/cos³x sur [0, π/4] : montrer
  f′(x) = 3/cos⁴x − 2/cos²x ; 3. calculer ∫₀^{π/4} dx/cos⁴x.
- **Ex. 15** (p.120) : f(x) = 1/sin²x sur ]0, π/2[. 1. montrer f(x) = (1 + tan²x)/tan²x ; 2. f réalise une
  bijection de ]0, π/2[ sur un intervalle I à préciser ; 3. f⁻¹ dérivable sur I et
  (f⁻¹)′(x) = −1/(2√(x³ − x)) ; 4. calculer ∫_{4/3}² dt/(2√(t³ − t)). [Bornes et expressions lues sur
  l'image ; l'OCR les perd.]
- **Ex. 16** (p.120) : 1. représenter f(x) = x²/(1 + x²) sur ℝ ; 2. 𝒜 l'aire limitée par C_f, l'axe, x = 1,
  x = 2 : a. vérifier 1/2 ≤ 𝒜 ≤ 1 ; b. méthode des rectangles, [1, 2] en 5 intervalles d'amplitude 0.2 :
  nouvel encadrement.
- **Ex. 17** (p.120) : uₙ = ∫₀¹ xⁿ/(x² + 1)² dx (n ≥ 1). 1. montrer 0 ≤ x^{2n+1}/(x² + 1)² ≤ x^{2n+1} pour
  n ≥ 1 et 0 ≤ x ≤ 1 ; 2. (uₙ) converge, limite. [Incohérence du manuel : définition en xⁿ, question 1 en
  x^{2n+1}.]
- **Ex. 18** (p.120) : Jₙ = ∫₀¹ xⁿ√(1 + x) dx (n ≥ 1). 1. par un encadrement de √(1 + x), 1/(n + 1) ≤ Jₙ ≤
  √2/(n + 1) ; limite de Jₙ ; 2. a. pour x ∈ [0, 1], 0 ≤ √2 − √(1 + x) ≤ (1/2)(1 − x) ; b. en déduire
  √2/(n + 1) − 1/(2n²) ≤ Jₙ ≤ √2/(n + 1) ; c. limite de (nJₙ).
- **Ex. 19** (p.120) : uₙ = ∫₀^{π/4} xⁿ cos 2x dx (n ≥ 0). 1. (uₙ) décroissante ; 2. comparer uₙ et
  ∫₀^{π/4} xⁿ dx (n ≥ 1) ; 3. (uₙ) convergente, limite ; 4. a. calculer u₀, u₁ ; b. uₙ₊₂ en fonction de uₙ ;
  c. calculer u₂, u₃.
- **Ex. 20** (p.120) : uₙ = ∫₀¹ dx/(1 + xⁿ) (n ≥ 1). 1. 1 − uₙ = ∫₀¹ xⁿ/(1 + xⁿ) dx ; 2. 0 ≤ 1 − uₙ ≤ 1/(n + 1) ;
  3. (uₙ) converge, limite.
- **Ex. 21** (p.121) : Iₙ = ∫₀^π sinⁿx dx. 1. calculer I₀, I₁ ; 2. (n + 2)Iₙ₊₂ = (n + 1)Iₙ, en déduire I₂, I₃ ;
  3. uₙ = (n + 1)IₙIₙ₊₁ : a. calculer uₙ₊₁ − uₙ, (uₙ) constante ; b. valeur de uₙ ; 4. (Iₙ) décroissante ;
  5. a. déduire π/(2(n + 1)) ≤ Iₙ² ≤ π/(2n), n ≥ 1 ; b. encadrement de I₁₀₀₀.
- **Ex. 22** (p.121) : f(x) = tan³x + tan x sur [0, π/4]. 1. variations ; 2. f bijection de [0, π/4] sur
  [0, 2] ; 3. a. représenter f et f⁻¹, demi-tangentes aux extrémités ; b. calculer ∫₀^{π/4} f(x)dx, en
  déduire ∫₀² f⁻¹(x)dx.
- **Ex. 23** (p.121) : f sur [0, 3] : f(x) = x si x ∈ [0, 1], f(x) = 1/x² si x ∈ ]1, 3]. 1. f continue ;
  2. F(x) = ∫₀ˣ f(t)dt : a. expliciter F(x), x ∈ [0, 3] ; b. représenter F.
- **Ex. 24** (p.121) : Iₙ = ∫₀^{π/4} tan^{n+2}x dx. 1. a. calculer I₀ ; b. 0 ≤ Iₙ₊₁ ≤ Iₙ ; c. (Iₙ) convergente ;
  2. a. Iₙ + Iₙ₊₂ = 1/(n + 3) ; b. lim Iₙ ; c. calculer I₂ et I₄.
- **Ex. 25** (p.121) : valeur moyenne de f sur I : 1. f : x ↦ x⁴ − x³ + 1, I = [−1, 3] ; 2. f : x ↦ 1/x³ − 1,
  I = [2, 4] ; 3. f : x ↦ sin(2x), I = [0, π].
- **Ex. 26** (p.121) : par l'inégalité de la moyenne, encadrement de ∫₂⁴ dx/(x² − x + 1).
- **Ex. 27** (p.121) : par l'inégalité de la moyenne, encadrement de ∫_{π/6}^{π/3} dx/(3 + tan²x).
- **Ex. 28** (p.121) : C = {M(x, y) : y = x², 0 ≤ x ≤ 2}, S solide par rotation autour de (Ox) ; volume de S.
- **Ex. 29** (p.121) : C = {M(x, y) : y = 1/x, 1 ≤ x ≤ 3}, rotation autour de (Ox) ; volume de S.
- **Ex. 30** (p.122) : C = {y = tan x, 0 ≤ x ≤ π/4}, rotation autour de (Ox) ; volume de S.
- **Ex. 31** (p.122) : C = {y = sin x + cos x, 0 ≤ x ≤ π/2}, rotation autour de (Ox) ; volume de S.
- **Ex. 32** (p.122) : C = {y = sin x, 0 ≤ x ≤ π/2} et C′ = {y = x, 0 ≤ x ≤ π/2}, solides S et S′ de
  rotation autour de (Ox) (figure) ; volume de la partie de l'espace comprise entre S et S′.
  [Le texte imprimé avant l'ex. 28 dit « Dans les exercices 31, 32, 33, 34 et 35 l'espace est muni d'un repère
  orthonormé (O, i⃗, j⃗, k⃗) » : numéros erronés du manuel (les volumes sont les ex. 28 à 32).]
- **Ex. 33** (p.122) : **I.** F(x) = ∫₀^{tan x} dt/(1 + t²) sur [0, π/4]. 1. F dérivable, dérivée ;
  2. F(x) = x ; 3. calculer ∫₀¹ dt/(1 + t²). **II.** J₀ = ∫₀¹ dt/(1 + t²), Jₙ = ∫₀¹ t^{2n}/(1 + t²) dt (n ≥ 1).
  1. a. 0 ≤ Jₙ ≤ 1/(1 + 2n) ; b. lim Jₙ ; 2. a. Jₙ₊₁ + Jₙ = 1/(1 + 2n) ; b. calculer J_k, 1 ≤ k ≤ 6.
- **Ex. 34** (p.122) : F(x) = ∫₀^{sin x} √(1 − t²) dt sur [0, π/2]. 1. F dérivable, dérivée ; 2. F(x) = x/2 +
  (1/4)sin(2x) ; 3. calculer ∫₀¹ √(1 − t²) dt ; 4. variations de F ; 5. tracer la courbe de F.
- **Ex. 35** (p.122) : f(x) = x + √(4 − x²) sur [−2, 2]. 1. étudier f, représenter C ; 2. F(x) =
  ∫₀^{2cos x} √(4 − t²) dt sur [0, π] : a. F dérivable et F′(x) = −4 sin²x ; b. calculer F(π/2) ;
  c. F(x) = −2x + sin(2x) + π ; 3. 𝒜 l'aire limitée par C, l'axe des abscisses et les droites d'équations
  « y = x, x = −2 et x = 2 » (libellé du manuel) : a. montrer 𝒜 = F(0) − F(π) ; b. en déduire 𝒜.
  [Doute : « l'axe des abscisses et les droites y = x, x = −2, x = 2 » lu ainsi ; l'aire attendue est
  vraisemblablement celle entre C et la droite y = x. L'OCR rendait « + x » au lieu de « + π » en 2.c.]

### Écart avec la référence (chapitre 6 de bac-math, manuel 222445, lignes 1588-1965)

**Ce que la référence enseigne et que ce manuel n'a PAS (à exclure)** :
- **Théorème « dérivée de x ↦ ∫ₐ^{u(x)} f(t)dt »** (F′ = f(u)·u′) : absent comme énoncé. ⚠️ Mais l'exercice
  résolu 6 (g = f∘sin, justifiée par « composée »), les ex. 33, 34, 35 (bornes tan x, sin x, 2cos x) le
  **mobilisent**. DOUTE de scope à arbitrer : soit l'enseigner en conséquence (la dérivée d'une composée
  suffit), soit exclure ces trois exercices. Ne pas l'ériger en théorème nommé par fidélité au manuel.
- **Section VII « Exemples de suites définies par une intégrale »** (Activité I₁, J₁, Iₙ, Jₙ en xⁿ sin x,
  xⁿ cos x) : absente comme section de cours ; les suites n'apparaissent qu'en exercices (17–21, 24, 33.II).
- **Exercice résolu 2 (Iₙ = ∫₀²xⁿ/√(x²+4)dx)** et **Problème résolu : intégrales de Wallis**
  (∫₀^{π/2}cosⁿ, récurrence par IPP, uₙ = (n+1)IₙIₙ₊₁) : absents. (Seul l'ex. 21, ∫₀^π sinⁿ, en est proche.)
- **Activité 3 de I.1** de la référence (fonction aire 𝒜(t), 𝒜′ = f, dérivation à droite et à gauche) : absente ;
  ici la définition vient de la seule Propriété F(b) − F(a) = G(b) − G(a) (Activité 1, f = x + 2).
- **Activités de la référence absentes** : f par morceaux (aire par géométrie) ; demi-cercle √(1 − x²) ;
  aire entre trois courbes (4x², x/2, 4/x²) ; IV.1 Act. 2 (∫sin³x, ∫(1 + tan²x)/tan⁴x) ; volume de la sphère ;
  calcul de ∫ ... avec ∫x²cos x en activité (présent ici seulement en exercice résolu 3).
- **QCM 3 et exercices** : plusieurs exercices de la référence n'ont pas d'équivalent ici (dont celui sur
  x + sin x, 3x² + 2/x³, ∫sin x/(1 + x²), ∫dt/(1 + t²)ⁿ, ∫xⁿ/(1 + x + x²), séries ∑1/(n(n+1)) et ∑1/k³ par
  comparaison série-intégrale). Ici 35 exercices contre 39.

**Ce que ce manuel a en plus (exploitable)** :
- Encadré **unité d'aire** (p.100) ; **Exercices résolus 1 à 4** (inégalités, sin x ≤ x puis cos x ≥ 1 − x²/2,
  IPP I/J/K en tableau « Posons », encadrement de ∫1/(1+x²) et ∫1/√(1−x²)) ; **Exercice résolu 6** (arcsin
  par ∫dt/√(1−t²), limite en 1⁻ = π/2, tableau et courbe) — la référence le place en activité.
- Activités : u_n = ∫xⁿ⁺¹/(1+x²) avec approximation de u₁₀₀, u₁₀₀₀₀ (Act. III-2) ; Act. III-1 (tangentes,
  9/4 ≤ ∫ ≤ 15/4) ; Act. IV.1 (cos t/sin³t…).
- Exercices : décomposition a/(x−1)ᵏ (ex. 2, 3, 7 — dont ex. 2 : 6x² − 12x + 42) ; ex. 5 (aire de D₁ = D₂ pour
  y = a) ; ex. 6 ((x²−4x−2)/(x−2)²) ; ex. 10 (5 − x² et 4/x²) ; ex. 15 (bijection de 1/sin²x et réciproque)
  ; ex. 16 (méthode des rectangles sur x²/(1+x²)) ; ex. 18 (∫xⁿ√(1+x)) ; ex. 20 (∫dx/(1+xⁿ)) ; ex. 21
  (∫sinⁿ).
- Vocabulaire : « lorsque a ≤ b » dans « Vocabulaire et notations » ; définition de l'intégrale d'une fonction
  de signe quelconque après celle de l'intégrale positive, identique à la référence pour le reste
  (linéarité, Chasles, positivité, comparaison, IPP, valeur moyenne, volume, parité, périodicité, F(x) = ∫ₐˣ).
- Position dans le plan : **VI est ici la dernière section** (la référence a VI puis VII).

### Bornes de scope observées (chapitre 7)

- ✅ INCLUS : intégrale d'une fonction continue et positive comme aire (F(b) − F(a)), unité d'aire ;
  intégrale d'une fonction continue (∫ₐᵇ f = F(b) − F(a)), variable muette, [F(x)]ₐᵇ ; propriétés
  algébriques (∫ₐᵃ = 0, ∫ₐᵇ = −∫ᵦᵃ, **Chasles**), **linéarité** ; aire d'une fonction de signe quelconque
  (∫|f|) et **aire entre deux courbes** (∫|f − g|) ; **positivité**, corollaire strict, **comparaison**
  h ≤ f ≤ g, |∫f| ≤ ∫|f| ; calcul au moyen d'une primitive (polynômes, puissances de forme u′uⁿ,
  trigonométrie : 1/cos²x, cos x sin³x, cos t/sin³t, tan²x, cos³x, valeur absolue avec étude du signe,
  racines √(2x+1), (x+1)/√(x²+2x)) ; **intégration par parties** (xsin x, x cos x, x² cos x ; xⁿ cos 2x,
  récurrences) ; **méthode des rectangles** (encadrement de ∫₁²dx/x, de ∫₁² x²/(1+x²) ; rectangles rᵢ et Rᵢ,
  5 intervalles) ; **valeur moyenne**, interprétation géométrique, **inégalité de la moyenne**, corollaire
  (f̄ = f(c)) ; **volume d'un solide de révolution** V = π∫f² autour de (Ox) (formule donnée) ; **fonction
  définie par une intégrale** F(x) = ∫ₐˣ f (primitive s'annulant en a, F′ = f) ; **parité** et **périodicité**
  des intégrales ; suites définies par une intégrale en exercices seulement (encadrement, convergence,
  récurrence par IPP, Iₙ + Iₙ₊₂, Jₙ₊₁ + Jₙ) ; études de fonctions, tracés et bijections réciproques
  mobilisés dans les exercices (ex. 6, 7, 8, 11, 15, 22).
- ⛔ EXCLU (non traité ici) : primitives/intégrales de **ln et exp** (donc pas d'intégrale ∫dx/x calculée :
  ∫₁²dx/x n'apparaît qu'encadrée, jamais évaluée) ; **équations différentielles** ; **changement de variable**
  formalisé (seule l'IPP est un procédé nommé) ; **intégrales impropres** (les limites passent par encadrement
  et théorème de l'encadrement ou fonction croissante majorée) ; **théorème de dérivation de ∫ₐ^{u(x)}**
  (cf. doute) ; **section « suites définies par une intégrale »** et **intégrales de Wallis** de la référence ;
  **volumes autour d'un autre axe que (Ox)** (aucun exemple) ; **démonstration de la formule de volume** (donnée) ;
  **démonstration du théorème de l'inégalité de la moyenne par primitive** (ici par intégration de m ≤ f ≤ M) ;
  **séries / comparaison série-intégrale** de la référence ; **calcul d'une primitive par décomposition
  en éléments simples généralisée** hors a/(x−α)ᵏ (ex. 2, 3, 7 : ce sont les seuls cas).
- DOUTES à trancher contre le **programme officiel** (R-3) : (1) la **méthode des rectangles** (IV.3) et
  le **volume de révolution** (V) sont au manuel mais leur présence au programme de Sciences expérimentales
  n'est pas vérifiée ici ; (2) la **dérivation de ∫ₐ^{u(x)}** (ex. 33–35, ER 6) ; (3) l'ex. 3 et l'ex. 35 (énoncés
  possiblement fautifs) ; (4) la numérotation « exercices 31 à 35 » (erreur du manuel).

### Lecture

- **Pages lues par l'OCR** (texte, prose) : 99 à 122 (les 24 pages), via `/root/.cache/yqa-manuels/222433/txt/pNNN.txt`.
- **Pages lues sur l'image** (110 dpi, `pdftoppm`) : **24 sur 24** — 99, 100, 101, 102, 103, 104, 105, 106,
  107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122. Tous les encadrés,
  formules, tableaux et figures ont été relus sur l'image ; l'OCR n'a servi que de prose de contrôle.
- **Sondage image (≥ 1 page sur 10, parmi les plus denses)** : fait sur la totalité, dont les plus
  denses 103, 108, 118, 119, 120, 121, 122. **Écarts OCR / image constatés** :
  p.99 « per l'équation y“=px », « Youschkevitch » mal transcrit, borne « a » de ∫₀ᵃ√(px) perdue ;
  p.100 définition et unité d'aire cassées en colonnes (les ‖i⃗‖, ‖j⃗‖ perdus) ; p.101 f : x ↦ x³ − (3/2)x²
  réduite à « x° _ » et bornes de l'Activité 3 perdues ; p.102–103 intégrales sans bornes, f(x) = x(x²+1)²
  perdue (Act. 3-2), « cos² x / 2 » de J (Act. 5) ; p.105 tangentes et valeurs 9/4, 15/4 mal lues ;
  p.106 fractions de l'Act. 2 et −1/2 des bornes ; p.107 plusieurs intégrales de l'Act. 1 (bornes de
  ∫ cos t/sin³t : π/6 et π/2) ; p.111 formule V = π∫f² (π perdu, lu « n ») ; p.113–114 ∫|sin x| sans
  valeurs absolues, bornes −5π…5π ; p.118 la moitié des intégrales de l'ex. 1 (valeurs absolues,
  racines) mal reproduites ; p.119 ex. 12 (« 2x² » au lieu de x², bornes « a » au lieu de π) et ex. 13 ;
  p.120 ex. 15 (bornes 4/3 et 2 perdues, dérivée de f⁻¹ illisible), ex. 18 (−1/(2n²)) ; p.122 ex. 35
  (F(x) = −2x + sin 2x + **π**, rendu « + x » par l'OCR) ; p.117 les deux graphiques de QCM 1 et V/F 5.
  Aucun écart ne change un encadré du cours, mais plusieurs exercices (118–122) ne sont fiables que lus
  sur l'image.

## 2.8 Chapitre 8 — Fonction logarithme népérien (manuel 222433, p.123–141)

**Page de garde (p.123)** — « Chapitre 8 — Fonction logarithme népérien ». Citation : « M.Stifel (1544) met en
évidence les deux suites » — table à deux lignes : ligne du haut … −3, −2, −1, 0, 1, 2, 3, 4, … 8 ; ligne du
bas … 1/8, 1/4, 1/2, 0, 1, 4, 8, 16 [sic : la ligne du bas imprime 1/2, 0, 1, 4 sous −1, 0, 1, 2 — on attendrait 1/2, 1, 2, 4 ; le terme 2 manque
et « 0 » s'intercale], … 256. Texte : « Le passage de la ligne inférieure ("in inferiore ordine")
à la ligne supérieure ("in superioreordine") transforme les produits en sommes. Par exemple, au lieu de multiplier 8
par 32 "in inferiore ordine", on peut prendre les "logarithmes" correspondants 3 et 5 "in superioreordine", calculer
leur somme, qui est 8, retourner "in inferiore ordine", où l'on trouve le produit 8.32=256. Cette table plus
détaillée, serait d'une grande utilité, car additionner est plus facile que multiplier. Les premières tables
logarithmiques […] ont été calculées par John Napier (1614, 1619), Henry Briggs (1624) et Jost Burgi (1620). »
Source : « (E.Haier et al, L'analyse au fil de l'histoire, 2000) » [sic, Haier pour Hairer]. Page de garde sans plan.

**Plan (titres imprimés)** : I. Introduction (p.124) · II. Étude et représentation graphique de la fonction ln
(p.126) · III. Propriétés algébriques (p.127) · IV. Autres limites (p.129) · V. Fonctions x ↦ ln(u(x)) et
x ↦ ln(|u(x)|) (p.130) · rubrique « QCM – VRAI – FAUX » (p.133) · rubrique « Exercices et problèmes » (p.134–141,
31 exercices, numérotés 1 à 31 dans un carré). Pas de « Problème résolu » : deux « Exercice résolu » insérés
dans le cours (p.128 et p.129–130).

### Cours — Activités

**I. Introduction** (p.124–125)

- **Activité 1** (p.124–125) — **A/** courbe de f : ]0,+∞[ → ℝ, t ↦ 1/t ; S(a) = aire limitée par la courbe, l'axe
  des abscisses et x = 1, x = a (a > 0). 1. S(1) ? 2. a. [1,2] en trois intervalles égaux, rectangles r₁,r₂,r₃ et
  R₁,R₂,R₃ (figures) ; 𝒜 / 𝒜′ sommes des aires ; montrer 37/60 ≤ S(2) ≤ 47/60. b. [1,3] en huit intervalles, rectangles
  rᵢ (1 ≤ i ≤ 8, figure) : somme des aires, vérifier S(3) ≥ 1. c. montrer S(2.5) ≤ 1. 3. a. E = {M(x,y), 1/2 ≤ x ≤ 1,
  0 ≤ y ≤ 1/x}, F = {M(x,y), 1 ≤ x ≤ 2, 0 ≤ y ≤ 1/x} : même aire ; b. en déduire S(1/2) = S(2). **B/** F(x) = ∫₁ˣ (1/t) dt,
  x > 0. 1. a. F(x) > 0 ssi x > 1 ; b. exprimer F(x) à l'aide de S(x). 2. dérivabilité de F sur ]0,+∞[, F′(x),
  F strictement croissante. 3. il existe un unique réel e ∈ ]2,3[ tel que F(e) = 1 (le réel est noté **e** dès cette
  question).
- **Activité 2** (p.126) : 1. Résoudre dans ℝ : a. ln(x + 1) = 0 ; b. ln(1 − x) = ln(2 + x). 2. Résoudre dans ℝ :
  a. ln(x − 1) ≤ 0 ; b. ln(4 − 3x) > 0 ; c. ln(x² + 1) ≥ 0 ; d. ln(2x − 5) ≤ ln x.

**II. Étude et représentation graphique de la fonction ln** (p.126–127) — « On se propose d'étudier la fonction ln et
de construire sa courbe représentative C dans un repère orthonormé (O, i⃗, j⃗). »

- **Activité 1** (p.126) : 1. n ≥ 1 entier : a. 1/t ≥ 1/2ⁿ⁺¹ pour 2ⁿ ≤ t ≤ 2ⁿ⁺¹ ; b. en déduire ∫_{2ⁿ}^{2ⁿ⁺¹} (1/t) dt ≥ 1/2.
  2. Vérifier ∫₁^{2ⁿ} = ∫₁² + ∫₂^{2²} + … + ∫_{2ⁿ⁻¹}^{2ⁿ} (1/t) dt, n ≥ 1. 3. a. ∫₁^{2ⁿ} (1/t) dt ≥ n/2, n ≥ 1 ;
  b. ln non majorée, déterminer lim_{x→+∞} ln x. 4. a. x ↦ ln x et x ↦ −ln(1/x) ont même dérivée sur ]0,+∞[ ;
  b. ln x = −ln(1/x), x > 0 ; c. calculer lim_{x→0⁺} ln x. (Suit le **Théorème** des limites en +∞ et 0⁺.)
- **Activité 2** (p.126–127) : 1. calculer lim_{x→1} (ln x − ln 1)/(x − 1). 2. 1/t ≤ 1/√t pour t ≥ 1. 3. ∫₁ˣ (1/t) dt ≤
  ∫₁ˣ (1/√t) dt, x ≥ 1. 4. calculer ∫₁ˣ (1/√t) dt, en déduire ln x ≤ 2√x − 2 ; montrer lim_{x→+∞} (ln x)/x = 0.
  (Suit le **Théorème** à deux limites ; puis tableau de variation et courbe de ln, sans activité.)

**III. Propriétés algébriques** (p.127–128)

- **Activité 1** (p.127) : 1. f(x) = ln x, g(x) = ln(ax) sur ]0,+∞[, a > 0 : a. comparer f′(x) et g′(x) ; b. il existe c
  constante avec ln(ax) = ln x + c ; c. en déduire ln(ax) = ln a + ln x, x > 0. 2. ln(a/b) = ln a − ln b, a > 0, b > 0.
- **Activité 2** (p.128) : 1. exprimer avec ln 2 et ln 3 : ln(√3), ln(∛2), ln 108, ln(81/8), ln(⁵√(2³)), ln(√(1/27)).
  2. simplifier : ln(√e), ln(1/e), ln(e³), ln(e⁻²), ln(∛e/√e), ln(⁴√e·∛e).
- **Exercice résolu 1** (p.128) : 1. plus petit entier naturel n tel que (1/2)ⁿ ≤ 10⁻⁴ ; 2. plus petit entier naturel n tel
  que 2ⁿ ≥ 10⁵. Solution imprimée : par croissance de ln, −n ln 2 ≤ −4 ln 10, donc n ≥ 4 ln 10 / ln 2, « réalisé dès que
  n ≥ 14 » ; 2ⁿ ≥ 10⁵ ssi n ≥ 5 ln 10 / ln 2, « réalisé dès que n ≥ 17 ».
- **Activité 3** (p.128) : limites lim_{x→1} ln(∛x)/x ; lim_{x→+∞} ln(∛x)/x ; lim_{x→+∞} ln x/¹⁰√x ;
  lim_{x→+∞} ln(2x + 3)/(3x + 4) ; lim_{x→+∞} (x − ln x).

**IV. Autres limites** (p.129–130)

- **Activité 1** (p.129) : m ∈ ℕ*, n ≥ 2. 1. a. vérifier (ln x)ⁿ/xᵐ = ( (n/m) × ln(ⁿ√(xᵐ)) / ⁿ√(xᵐ) )ⁿ, x > 0 ;
  b. en déduire lim_{x→+∞} (ln x)ⁿ/xᵐ = 0. 2. calculer lim_{x→0⁺} |xᵐ (ln x)ⁿ|.
- **Activité 2** (p.129) : 1. lim_{x→+∞} (x² − ln³x) ; lim_{x→0⁺} (x² + ln³x). 2. lim_{x→0⁺} x⁴(1 − ln⁵x) ;
  lim_{x→+∞} x⁴(1 − ln⁵x).
- **Exercice résolu 2** (p.129–130) : f(x) = x² ln²x si x > 0, f(0) = 0. 1. dérivabilité sur son ensemble de
  définition ; 2. variations et courbe (repère orthonormé). Solution imprimée : f dérivable sur ]0,+∞[ (produit) ;
  taux (f(x) − f(0))/x = x ln²x → 0, f dérivable à droite en 0, f′_d(0) = 0, donc f dérivable sur [0,+∞[ ;
  f′(x) = 2x ln x (ln x + 1), f′(x) ≤ 0 ssi 1/e ≤ x ≤ 1 ; lim_{+∞} x² ln²x = +∞ et lim_{+∞} x² ln²x / x = +∞ :
  branche parabolique de direction (O, j⃗) en +∞ ; tableau : f croît de 0 à 1/e² (en x = 1/e), décroît jusqu'à 0
  (en x = 1), puis croît vers +∞ ; courbe tracée.

**V. Fonctions x ↦ ln(u(x)) et x ↦ ln(|u(x)|)** (p.130–132)

- **Activité 1** (p.130) : u : x ↦ x² + x + 2. 1. signe de u sur ℝ. 2. f : x ↦ ln(x² + x + 2) : a. ensemble de définition ;
  b. f dérivable en tout réel de son ensemble de définition, calculer f′(x). (« Le théorème de dérivation des fonctions
  composées fournit la démonstration des théorèmes ci-dessous. »)
- **Activité 2** (p.131) : f : x ↦ ln((x − 2)/(x + 1)) + x. 1. tableau de variation ; 2. nature des branches infinies ;
  3. tracer la courbe (repère orthonormé).
- **Activité 3** (p.131) : primitive de f sur I : 1. f(x) = x/(1 − x²), I = ]1,+∞[ ; 2. f(x) = (x + 1)/(x + 3),
  I = ]−∞, −4[ ; 3. f(x) = 1/(x ln x), I = ]0,1[ ; 4. f(x) = 2cos(2x)/sin(2x), I = ]0, π/2[.
- **Activité 4** (p.131) : dériver x ↦ x ln x ; en déduire une primitive de ln.
- **Activité 5** (p.132) : f : x ↦ 1 − x + ln x (repère orthonormé). 1. variations et courbe C_f. 2. α ∈ ]0,1[ :
  a. aire 𝒜(α) du domaine limité par C_f, l'axe des abscisses et x = α, x = 1 ; b. lim_{α→0⁺} 𝒜(α).
- **Activité 6** (p.132) : 1. a, b tels que, pour t ∈ ℝ*\{−1}, 1/(t(t + 1)) = a/t + b/(t + 1). 2. calculer ∫₁² dt/(t(t + 1)).
  3. à l'aide d'une intégration par parties, valeur de ∫₁² ln(1 + t)/t² dt.

### QCM (p.133) — « Cocher la réponse exacte. » (réponses non fournies)

1. Pour tout réel x > 0, ln(x + x²) est égal à (☐ ln x + ln(x + 1) / ☐ ln(x²) + ln x / ☐ 3 ln x).
2. ln(1/√e) est égal à (☐ −2 / ☐ 1/2 / ☐ −1/2).
3. f(x) = ln(−x), x < 0 : f′(x) est égal à (☐ −1/x / ☐ 1/x / ☐ −x).
4. f(x) = x ln(x²), x < 0 : f′(x) est égal à (☐ 2(1 + ln|x|) / ☐ 2(1 + ln x) / ☐ ln(x²) + 1/x).
5. La limite de x ↦ (ln x)/x en 0⁺ est égale à (☐ +∞ / ☐ −∞ / ☐ 0).
6. La limite de x ↦ ln x + 1/x en 0⁺ est égale à (☐ −∞ / ☐ 0 / ☐ +∞).

### Vrai – Faux (p.133) — « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)

1. La fonction x ↦ x ln x − x + 1 est la primitive de la fonction ln sur ℝ*₊, qui s'annule en 1.
2. La fonction ln est une bijection de ℝ*₊ sur ℝ*₊.
3. Pour tout réel x, ln x = ∫₂ˣ dt/t + ln 2. [sic : « pour tout réel x » imprimé, x > 0 sous-entendu]
4. lim_{x→0⁺} 1/(x ln x − x) = +∞.

### Exercices et problèmes (p.134–141) — 31 exercices

(Notation : « repère » = orthonormé sauf mention ; tous les énoncés lus sur l'image.)

- **1** (p.134) : calculer ln(e²) ; ln(1/e) ; ln 25 − 2 ln 5 ; « ln 100000 − ln 100000 − ln 1000 − ln ln 100 − ln 10 » [libellé lu sur
  l'image à 200 dpi : la répétition « ln 100000 − ln 100000 » et l'enchaînement « ln ln 100 » sont imprimés ainsi — coquille source probable, ne pas corriger en silence].
- **2** (p.134) : résoudre dans ℝ : 1. ln x + ln(x + 1) = 0 ; 2. ln(ln x) = 0 ; 3. ln(1/x) + ln(x³) = ln 3 ; 4. (ln x)² − 2 ln x − 3 = 0.
- **3** (p.134) : inéquations : 1. ln(2x + 3) < 5 ; 2. ln(3x + 1) ≤ 0 ; 3. ln(5x) > 1 − ln 5 ; 4. ln((1 + x)/(x + 2)) ≥ 0 ;
  5. (ln x)² − 2 ln x < 0.
- **4** (p.134) : limite en +∞ de f : 1. ln(x⁴)/x ; 2. (x² + 1)/(x ln x) ; 3. (2 − ln x)/(1 + ln x) ; 4. ln((1 + x)/(2 + x)) ;
  5. ln(x + 1)/(x + 2) ; 6. 1 + x − ln x ; 7. x − ln²x ; 8. x − ln(x + 1) + ln(x).
- **5** (p.134) : limites : 1. (ln x − ln 3)/(x − 3), x→3 ; 2. (ln x − 1)/(x − e), x→e ; 3. (ln x + ln 2)/(x − 1/2), x→1/2 ;
  4. ln(1 + 3x)/x, x→0 ; 5. ln(cos x)/x, x→0 ; 6. ln(1 + sin x)/x, x→0 ; 7. ln(x)/(x² − 3x + 2), x→1.
- **6** (p.134) : limites : 1. x² ln x (0⁺) ; 2. √x ln x (0⁺) ; 3. 1/x² + ln x (0⁺) ; 4. x³/ln x (+∞) ; 5. ln³x/x (+∞) ;
  6. x³ ln²(1/x) (0⁺).
- **7** (p.134) : pour chaque f : ensemble de définition, ensemble de dérivabilité, f′(x), puis représenter f après étude des
  branches infinies : 1. ln(1/x) ; 2. ln(x² − x + 1) ; 3. x ln x − x ; 4. x² ln x ; 5. ln(x + √(x² + 1)) ; 6. ln((x + 1)/(x − 1)).
- **8** (p.134) : primitive de f sur I : 1. (1 + x + x² + x³)/x⁴, ℝ*₊ ; 2. (2x − 3)/(x + 1), ]−1,+∞[ ; 3. (x + 1)/(x + 2), ]−2,+∞[ ;
  4. x/(x² + 1) − x(x² + 1), ℝ ; 5. 1/(x ln x), ]1,+∞[ ; 6. ln³x/x, ]0,+∞[ ; 7. tan x, ]0, π/2[ ; 8. 1/tan x, ]0, π/2[.
- **9** (p.135) : intégrales : 1. ∫₁ᵉ ln²x/x dx ; 2. ∫₁² 2/(x + 1) dx ; 3. ∫₀¹ (x + 1)/(x² + 2x + 3) dx ; 4. ∫_{π/6}^{π/4} tan x dx ; 5. ∫₁² ln x/x dx ;
  6. ∫₂⁴ dx/(x ln x).
- **10** (p.135) : par intégration par parties : 1. ∫₁ᵉ x ln x dx ; 2. ∫ₑ^{e²} x² ln x dx ; 3. ∫₁ᵉ ln x/√x dx ; 4. ∫₁ᵉ ln²x dx.
- **11** (p.135) : f : x ↦ 1/(x²(x − 2)). 1. déterminer a, b, c tels que f(x) = a/x + b/x² + c/(x − 2), x ≠ 0, x ≠ 2, par
  a. lim_{x→2} f(x)(x − 2) ⇒ c ; b. lim_{x→0} f(x)x² ⇒ b ; c. lim_{x→+∞} f(x)x ⇒ a. 2. calculer ∫₃⁴ f(x) dx.
  3. par intégration par parties, ∫₃⁴ ln(x − 2)/x³ dx.
- **12** (p.135) : étudier f et tracer sa courbe (repère orthogonal) : 1. (ln x)² ; 2. 1/ln x ; 3. ln(√x) ; 4. ln|x² − 1|.
- **13** (p.135) : f(x) = (ln x − 2)/(ln x − 1) sur ]0,e[. 1. variations et courbe C ; 2. f bijection de ]0,e[ sur ]1,+∞[ ;
  3. a. courbe de f⁻¹ ; b. calculer f⁻¹(2) et en déduire (f⁻¹)′(2).
- **14** (p.135) : f : x ↦ −x/2 + ln|(x − 1)/x|. 1. ensemble de définition ; 2. tableau de variation ; 3. la droite Δ : y = −x/2
  est asymptote à C, position relative ; 4. I(1/2, −1/4) centre de symétrie de C ; 5. construire C ; 6. f(x) = 0 admet une
  solution unique x₀ et 2/5 < x₀ < 9/20.
- **15** (p.135) : f : x ↦ (ln x)² − 3 ln x + 2. 1. tableau de variation (indication : ln(√(e³)) = 3/2) ; 2. courbe C, points
  d'intersection avec (O, i⃗) ; 3. F : x ↦ x(ln x)² − 5x ln x + 7x est une primitive de f sur ]0,+∞[ ; 4. aire limitée par C,
  x = e, x = e², y = 0.
- **16** (p.136) : f(x) = 2 − x + (ln x)/x sur ]0,+∞[. 1. lim_{+∞} f, lim_{0⁺} f ; 2. g(x) = 1 − x² − ln x : sens de variation,
  g(1), signe de g ; 3. f′(x) = g(x)/x² ; 4. a. Δ : y = −x + 2 asymptote à C ; b. position C/Δ ; c. tracer C et Δ.
- **17** (p.136) : **A/** g(x) = x² − 2 + 2 ln x. 1. tableau de variation ; 2. g(x) = 0 a une unique solution x₀ ∈ [1,2], valeur
  approchée à 10⁻¹ près, signe de g ; 3. (repère orthogonal) a. aire limitée par la courbe de g, l'axe des abscisses,
  x = 2, x = 3 ; b. même chose avec x = 1/3 et x = 0.5. **B/** f(x) = x − 2 − (2 ln x)/x : 1. f′(x) = g(x)/x² ; 2. tableau ;
  3. a. asymptote D en +∞ (équation), b. position C/D, c. tracer C et D.
- **18** (p.136) : 1. g(x) = 2x√x − 3 ln x + 6 : a. variations, b. signe. 2. f(x) = (3 ln x)/√x + x − 1 (repère orthogonal) :
  a. limites en 0 et +∞ ; b. variations ; 3. a. asymptote D en +∞ ; b. position C/D ; c. tracer C et D.
- **19** (p.136) : f(x) = (1 − ln x)/x. 1. tableau ; 2. tracer C_f ; 3. aire limitée par C_f, l'axe des abscisses, x = 1, x = e ;
  4. solide S de révolution autour de (Ox) de {y = f(x), 1 ≤ x ≤ e} : a. par intégration par parties ∫₁ᵉ ln x/x² dx puis
  ∫₁ᵉ ln²x/x² dx ; b. en déduire le volume de S.
- **20** (p.136–137) : f(x) = (1 − 1/x)(ln x − 2) sur ]0,+∞[. 1. limites à droite en 0 et en +∞ ; 2. f dérivable, dérivée ;
  3. u(x) = ln x + x − 3 : a. variations ; b. u(x) = 0 a une unique solution α ∈ [2.2, 2.21] ; c. signe de u ; 4. a. variations
  de f ; b. f(α) = −(α − 1)²/α, encadrement de f(α) d'amplitude 2×10⁻² ; 5. tracer la courbe.
- **21** (p.137) : **A/** g(x) = 1 − x − 2x ln x : 1. variations (indication : ln(1/√(e³)) = −3/2) ; 2. g(1), signe de g.
  **B/** f(x) = (1 + ln x)/(1 + x)² (repère orthogonal) : 1. a. f′(x) = g(x)/(x(1 + x)³), b. tableau, c. branches infinies ;
  3. tangente au point d'intersection avec l'axe des abscisses ; 4. tracer C. **C/** λ > 1 : 1. 1/(x(1 + x)) = 1/x − 1/(x + 1) ;
  2. ∫₁^λ dx/(x(1 + x)) ; 3. 𝒜(λ) aire limitée par C, l'axe, x = 1, x = λ : a. par parties, 𝒜(λ) ; b. lim_{λ→+∞} 𝒜(λ).
- **22** (p.137–138) : **I.** g(x) = x(x − 1) + ln x : 1. g strictement croissante ; 2. g(1), signe de g. **II.** f(x) = (x − 1)² + ln²x,
  C₁ : 1. a. limites en 0⁺ et +∞ ; b. f′(x) = 2g(x)/x ; c. tableau ; 2. h restriction de f à ]0,1] bijection sur [0,+∞[, h⁻¹ de
  courbe C₂ ; 3. u(x) = h(x) − x : a. tableau, b. h(a) = a a une seule solution a ∈ ]0,1], 0.5 < a < 1 ; 2. a. C₁ admet en +∞ une
  branche parabolique de direction (O, j⃗) ; b. tracer Δ : y = x, C₁, C₂. **III.** A aire limitée par C₁, l'axe, x = a, x = 1 ;
  I = ∫ₐ¹ x f′(x) dx : 1. par parties I = −a² − A ; 2. a. I = 2∫ₐ¹ g(x) dx ; b. I = −(2/3)a³ + a² + 2a − 7/3 − 2a ln a ;
  c. A en fonction de a.
- **23** (p.138) : [sic : « définie sur l'intervalle ]0,+∞[ » imprimé alors que f(0) = 0 est défini — [0,+∞[ attendu] f(0) = 0, f(x) = (1/2)x²(3 − 2 ln x) si x > 0. **A/** 1. a. lim_{0⁺} f, conséquence ; b. limite en +∞ ; 2. a. dérivabilité
  en 0 ; b. dérivabilité sur ]0,+∞[ et f′ ; 3. variations, tableau ; 4. f(x) = 0 unique solution α, valeur approchée à 10⁻² près.
  **B/** 1. tangente D au point d'abscisse 1 ; 2. g(x) = f(x) − 2x + 1/2 : a. g′ et g″, sens de variation de g′, signe de g′ ;
  b. variations de g, position de C par rapport à D ; 3. construire C et D. **C/** 1. Iₙ = ∫_{1/n}^1 x² ln x dx en fonction de n ;
  2. aire Aₙ limitée par C, D, x = 1/n, x = 1 ; 3. lim Aₙ.
- **24** (p.138) : tracer x ↦ ln x ; n ≥ 2, Sₙ = ln 1 + ln 2 + … + ln n, Tₙ = ln 1 + ln 2 + … + ln(n − 1). 1. Tₙ ≤ ∫₁ⁿ ln x dx ≤ Sₙ ;
  2. ln((n − 1)!) ≤ n ln n − n + 1 ≤ ln n!, puis e(n/e)ⁿ ≤ n! ≤ n e(n/e)ⁿ.
- **25** (p.138) : f(x) = ln(ln x). 1. ensemble de définition ; 2. dérivabilité, f′(x) ; 3. Sₙ = Σ_{k=2}^{n} 1/(k ln k), n ≥ 2 :
  ∫ₖ^{k+1} dt/(t ln t) ≤ 1/(k ln k), k ≥ 2 ; 4. calculer ∫₂^{n+1} dt/(t ln t), en déduire lim Sₙ.
- **26** (p.138–139) : 1. x − x²/2 ≤ ln(1 + x) ≤ x pour x ∈ ℝ₊ ; 2. a. Σ k = n(n + 1)/2 et Σ k² = n(n + 1)(2n + 1)/6 ; 3. Pₙ =
  (1 + 1/n²)(1 + 2/n²)…(1 + n/n²) : a. (1/n²)Σk − (1/(2n⁴))Σk² ≤ ln Pₙ ≤ (1/n²)Σk ; b. en déduire lim Pₙ.
- **27** (p.139) : **I.** g(x) = ln(x + 2) − ln x − 2/(x + 2) + 1/4 sur [0,+∞[ [lecture : l'énoncé commence sur [0,+∞[ alors que ln x
  exige x > 0 — coquille source possible, à signaler] : 1. a. variation de g, b. lim_{+∞} g, c. signe de g ; 2. g(x) < 1/2 sur [2,3].
  **II.** f(x) = x ln((x + 2)/x) + x/4 + 1/2 pour x > 0, f(0) = 1/2 : 1. lim_{0⁺} x ln((x + 2)/x), continuité en 0 à droite ;
  2. dérivabilité en 0 à droite, interprétation graphique ; 3. variations de f ; 4. a. lim_{+∞} x ln((x + 2)/x) = 2, b. lim_{+∞} f,
  c. Δ : y = x/4 + 5/2 asymptote en +∞ ; 5. tracer Δ, C, D : y = x. **III.** 1. h(x) = f(x) − x sur [2,3], h′(x) < 0 ; 2. variation de h,
  h(x) = 0 a une unique solution α dans [2,3] ; 3. 0 < f′(x) < 1/2 sur [2,3] ; 4. |f(x) − α| < (1/2)|x − α| ; suite u₀ = 2,
  uₙ₊₁ = f(uₙ) : a. uₙ ∈ [2,3] ; b. |uₙ₊₁ − α| ≤ (1/2)|uₙ − α| ; c. |uₙ − α| ≤ (1/2)ⁿ ; d. (uₙ) converge, limite.
- **28** (p.139–140) : **I.** f(x) = 4 − x − (ln x)/4 sur ]0,+∞[, C : 1. limites aux bornes, branches infinies ; 2. a. tableau, b. f(x) = 0
  solution unique a ∈ [3,4], c. tracer C ; 3. aire A limitée par C, l'axe, x = a, x = 4 en fonction de a. **II.** 1. g(x) = 4 − (1/4) ln x :
  a. a solution de g(x) = x ; b. g([3,4]) ⊂ [3,4] ; c. |g′(x)| ≤ 1/12 sur [3,4] ; 2. u₀ = 3, uₙ₊₁ = g(uₙ) : a. uₙ ∈ [3,4] ; b. |uₙ₊₁ − a| ≤
  (1/12)|uₙ − a| ; c. (uₙ) converge, limite.
- **29** (p.140) : **A/** 1. g(x) = (1 − x) ln x sur ℝ*₊, signe de g ; 2. h(x) = ln x − x : a. tableau, b. signe de h. **B/** f(x) = ln x (ln x − x) sur
  ℝ*₊ : 1. f′(x) = (g(x) + h(x))/x ; 2. tableau ; 3. branches infinies ; 4. a. intersection avec l'axe des abscisses, b. tangente T au
  point d'abscisse 1, c. A(e, −e + 1) ∈ C_f ∩ T ; 5. construire C_f et T ; 6. α ∈ ]0,1[, D limité par C_f, l'axe, x = α, x = 1 :
  a. par parties ∫ₐ¹ ln²x dx et ∫ₐ¹ x ln x dx, b. aire 𝒜(α), c. lim_{α→0⁺} 𝒜(α) ; 7. a. f bijection de ℝ*₊ sur un intervalle J, b. courbe de f⁻¹.
- **30** (p.140–141) : **A/** f(x) = 1/x + 1/ln x sur ]0,+∞[\{1} (zoom 200 dpi ; cohérent avec f′ imprimée) : 1. lim en 0⁺, 1⁻, 1⁺, +∞, interprétation ;
  2. a. f′(x) = −1/x² − 1/(x(ln x)²), b. tableau ; 3. h restriction de f à ]0,1[ : a. bijection sur un intervalle J, b. h(x) = 0 a une solution α et
  0.5 < α < 0.6, c. C_f coupe l'axe en un seul point ; 4. tracer C_f ; 5. courbe de h⁻¹ ; 6. a. h′(α) = −(α + 1)/α³, b. h⁻¹ dérivable en 0,
  (h⁻¹)′(0) en fonction de α. **B/** g(x) = 2f(x²) sur ]1,+∞[ : 1. f(x) − g(x) = 1/x − 2/x² ; 2. position C_f / C_g ;
  3. x ∈ [2,+∞[, M ∈ C_f, N ∈ C_g d'abscisse x : valeur de x qui rend NM maximale.
- **31** (p.141) : **I/** 1. h(x) = x − ln x sur ]0,+∞[ : a. tableau, b. h(x) ≥ 1 ; 2. f(x) = 1/(x − ln x) si x > 0, f(0) = 0 sur [0,+∞[ :
  a. f continue, b. f dérivable à droite en 0 ? **II/** F(x) = ∫ₓ^{2x} f(t) dt sur [0,+∞[ : 1. a. F dérivable, b. F′(x) = (ln 2 − ln x)/(h(2x)h(x))
  et F′_d(0) = 0 ; 2. ∫ₓ^{2x} dt/t = ln 2 ; 3. pour x ≥ 1, 0 ≤ F(x) − ln 2 ≤ ln(2x)/(x − ln x), en déduire lim_{+∞} F ; 4. a. F(1/2) ≤ ln 2,
  b. il existe α ∈ [1/2, 1] tel que F(α) = ln 2 ; 5. a. tableau de F, b. allure de la courbe (F(1) ≈ 0.9, F(2) ≈ 1.1 donnés). **III/** n ∈ ℕ* :
  1. vₙ = ∫_{1/n}^1 t/(t − ln t) dt : a. t/(t − ln t) ≤ t sur ]0,+∞[, b. (vₙ) croissante, c. convergente, 0 ≤ lim vₙ ≤ 1/2 ; 2. wₙ =
  ∫₁ⁿ t/(t − ln t) dt : a. 1 ≤ t/(t − ln t) sur [1,+∞[, b. lim wₙ.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur l'image)

> **Définition** (p.125) — « On appelle fonction logarithme népérien et on note ln, la fonction x ↦ ln x = ∫₁ˣ (1/t) dt, x > 0. »
> Suivent, hors encadré : « Les résultats suivants découlent immédiatement de la définition précédente. La fonction logarithme
> népérien est la primitive sur ]0,+∞[ de la fonction t ↦ 1/t, qui s'annule en 1. La fonction ln est définie, continue,
> dérivable sur l'intervalle ]0,+∞[ et ln′(x) = 1/x, x > 0. La fonction ln est strictement croissante sur ]0,+∞[ et ln 1 = 0. Il
> existe un unique réel x appartenant à ]2,3[ tel que ln(x) = 1. »

> **Encadré** (p.125, après « Il en résulte que ») — « Soit a et b deux réels strictement positifs. ln a > ln b, si et seulement si, a > b.
> ln a = ln b, si et seulement si, a = b. ln a = 0, si et seulement si, a = 1. ln a > 0, si et seulement si, a > 1. ln a < 0, si et
> seulement si, 0 < a < 1. »

> **Théorème** (p.126) — « lim_{x→+∞} ln x = +∞. lim_{x→0⁺} ln x = −∞. »

> **Théorème** (p.127) — « lim_{x→1} (ln x)/(x − 1) = 1. lim_{x→+∞} (ln x)/x = 0. »

> **Tableau de variation et représentation graphique** (p.127) — ln définie sur ]0,+∞[ ; (ln)′(x) > 0 ; ln croît de −∞ (en 0) à +∞.
> Hors encadré : « • La fonction ln réalise une bijection strictement croissante de ℝ*₊ sur ℝ. • L'unique solution de l'équation ln x = 1 est le
> réel noté e. Ainsi, ln e = 1. Les calculatrices donnent des valeurs approchées du réel e de sorte que e ≈ 2.71828... »

> **Théorème** (p.128) — « Soit a et b deux réels strictement positifs. • ln(a.b) = ln a + ln b. • ln(a/b) = ln a − ln b. • ln(1/b) = −ln b.
> • Pour tout entier p, ln(aᵖ) = p ln a • Pour tout entier p ≥ 2, ln(ᵖ√a) = (1/p) ln a. »

> **Théorème** (p.129) — « Pour tous entiers naturels non nuls n et m, lim_{x→+∞} lnⁿx / xᵐ = 0 et lim_{x→0⁺} xᵐ lnⁿx = 0. »

> **Théorème** (p.130) — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) > 0, pour tout réel x dans I. La fonction
> f : x ↦ ln(u(x)) est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x dans I. »

> **Corollaire** (p.131) — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0, pour tout réel x de I. La fonction
> f : x ↦ ln|u(x)| est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x de I. »

> **Corollaire** (p.131) — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0 pour tout réel x dans I. Les primitives
> sur I de la fonction x ↦ u′(x)/u(x) sont les fonctions x ↦ ln|u(x)| + k, où k est une constante réelle. »

> **Théorème** (p.131) — « La fonction x ↦ x ln x − x est une primitive de la fonction x ↦ ln x sur ℝ*₊. »

### Écart avec la référence (ch.7 de la section Mathématiques, manuel 222445, p.137–157 ; fiche bac-math l.1966-2316)

Même plan I–V, mêmes encadrés de fond (définition, équivalences ln a ⋛ ln b, limites, propriétés algébriques, croissances comparées,
ln(u) et ln|u|, primitive de u′/u, primitive de ln), même QCM (6) et même Vrai-Faux (4). Seules différences :
- **Corollaires** : ici ln|u| est un « Corollaire » (p.131) ; la référence le donne en « Théorème ». Même énoncé.
- **e** : ici défini dès l'Activité 1 B/3 (« unique réel e ∈ ]2,3[ tel que F(e) = 1 ») puis p.127 « ln e = 1 » ; la référence l'introduit au théorème p.141.

**Ce que la référence enseigne et que ce manuel n'a PAS (à exclure)** :
- le **« Problème résolu »** (p.146–147) : série harmonique Sₙ, divergence par Sₙ ≥ ln(n + 1), Tₙ = Sₙ − ln n, **théorème des accroissements finis**,
  **suites adjacentes**, constante d'Euler ≈ 0.5772 ;
- l'**Activité 2 de II** (tangente à C en A, y_H − y_K constant, construction de la tangente) et l'étude de la tangente en 1 dans l'Activité 1 de II ;
- l'**Activité 4 de IV** (comparer 2007²⁰⁰⁸ et 2008²⁰⁰⁷ par ln) ;
- l'**Activité 3 de V** (ln|tan(x/2)|, primitive de 1/sin x), l'**Activité 5 de V** (1/(x+1) ≤ ln(x+1) − ln x ≤ 1/x, suite vₙ = Σ 1/k,
  limite ln 2), l'**Activité 10** (uₙ = ∫₀¹ xⁿ ln(x + 2) dx) ;
- l'Activité 5 d'équations de la référence ((ln x)² + 2 ln x = 3, ln(x + 3) + ln(x + 2) = ln(x + 11), (1 − ln x)(2 − ln x) ≥ 0…) : ici les
  équations/inéquations sont dans l'Act. 2 de I (ln(x + 1) = 0, ln(1 − x) = ln(2 + x), ln(x − 1) ≤ 0, ln(4 − 3x) > 0, ln(x² + 1) ≥ 0,
  ln(2x − 5) ≤ ln x) et en exercices 2–3 ; données différentes de la référence, mêmes types.

**Ce que ce manuel a en plus** :
- **deux « Exercice résolu » avec solution rédigée** : 1 (p.128, plus petit n avec (1/2)ⁿ ≤ 10⁻⁴ et 2ⁿ ≥ 10⁵ ; la référence pose le même type en Activité 4
  sans solution) et 2 (p.129–130, f(x) = x² ln²x : dérivabilité en 0 par le taux, tableau, branche parabolique) ;
- l'**Activité 3 de V** (primitives de x/(1 − x²), (x + 1)/(x + 3), 1/(x ln x), 2cos(2x)/sin(2x)) et l'**Activité 6 de V** (décomposition
  1/(t(t + 1)) puis intégration par parties de ln(1 + t)/t²), regroupées différemment de la référence ;
- dans les **exercices** (31 contre 30), vérifié absent de la référence : **solide de révolution** (ex. 19), **décomposition 1/(x²(x − 2)) par limites**
  (ex. 11), **suites uₙ₊₁ = f(uₙ) avec point fixe et |f′| ≤ k < 1** (ex. 27, 28), **F(x) = ∫ₓ^{2x} f(t) dt** (ex. 31), **Pₙ produit et ln(1 + x) ≥ x − x²/2** (ex. 26) ;
  les exercices (ln x)², 1/ln x, −x/2 + ln|(x − 1)/x| (centre de symétrie), encadrement de n!, Σ 1/(k ln k) figurent aussi dans la référence.
  [Comparaison exercice par exercice non faite : la liste « en plus » n'est garantie que pour les thèmes testés ci-dessus.]

### Bornes de scope (chapitre 8 de la section Sciences expérimentales)

- ✅ **INCLUS** : définition de ln par l'**intégrale ∫₁ˣ dt/t** (construction par l'aire S(a)), ln′(x) = 1/x, stricte croissance, ln 1 = 0, existence
  du réel **e** (unique réel de ]2,3[ tel que ln = 1, e ≈ 2.71828), **bijection** ℝ*₊ → ℝ ; équivalences ln a ⋛ ln b ; **équations et
  inéquations** avec ln (domaine de définition, ln(ln x), (ln x)² − 2 ln x − 3) ; **propriétés algébriques** (somme, quotient, inverse,
  puissances entières p, racine p-ième 1/p) ; **limites** de référence (ln en +∞ et 0⁺, (ln x)/x, (ln x)/(x − 1) en 1) et **croissances comparées**
  lnⁿx/xᵐ, xᵐ lnⁿx ; limites du type ln(1 + ax)/x en 0, ln(cos x)/x (exercice 5) ; **tableau de variation**, **courbe** de ln ; **dérivation** de
  ln(u), ln|u| ; **primitive** de u′/u et de ln ; **branches infinies** (asymptote oblique, branche parabolique) et **étude complète** de fonctions
  à ln (domaine, dérivabilité, parité/symétrie centre, signe de f′ via une fonction auxiliaire g, TVI, tracé) ; **intégrales** (primitive directe,
  décomposition en éléments simples 1/(x²(x − 2)), **intégration par parties** avec ln) ; **aire** et **volume de révolution** ; **suites** uₙ₊₁ = f(uₙ)
  convergentes avec |f′| ≤ k < 1 ; fonction **réciproque** d'une fonction à ln ; **encadrements** et sommes (ln(1 + x), n!, Σ 1/(k ln k)).
- ⛔ **EXCLU** (non traité ici, ni dans les pages 123–141) : la **fonction exponentielle** et exp comme réciproque de ln (aucune occurrence dans p.123–141 ; chapitre 9 du manuel, confirmé par le manifeste), aᵇ à
  exposant réel et a^x, ln comme réciproque de exp ; le **logarithme décimal** log ; les **équations différentielles** ; le **théorème des
  accroissements finis** et l'**inégalité des accroissements finis** nommés (les exercices 27 et 28 les utilisent sans les citer : « montrer
  que |f(x) − α| < ½|x − α| » est donné par l'étude de f′, pas par un théorème énoncé) ; **suites adjacentes** ; **constante d'Euler** ; **Problème
  résolu** de la référence ; construction géométrique de la tangente à ln.
- ⚠️ **À ne pas élargir** : ln(aᵖ), ln(ᵖ√a) restent aux exposants entiers / 1/p ; valeurs numériques de ln données en fonction de ln 2, ln 3, ln 10
  (Act. 2 de III, Ex. résolu 1) ; e défini uniquement par ln e = 1.

### Lecture

- **Pages lues par l'OCR (texte)** : 123–141 (19 pages), toutes ; l'OCR rend la prose mais dégrade les formules.
- **Pages lues sur l'image (110 dpi)** : **les 19 pages, 123 à 141** (toutes sont à formule, encadré ou tableau) ; agrandissements à 200–220 dpi de p.134 (ex. 1), p.135 (ex. 9), p.136
  (ex. 17 : x = 1/3 et x = 0.5 confirmé) et p.140 (ex. 30).
- **Sondage image / OCR** : 19/19 pages (≫ 1 sur 10). Écarts constatés : p.123 le tableau de Stifel est illisible à l'OCR ; p.124–125 énoncé « 37/60 ≤ S(2) ≤ 47/60 »
  perdu à l'OCR (« 2 <S(2)< _ »), figures E/F absentes du texte ; p.126 Act. 2 b. OCR « ln(1−x)=1ln(2+x) » → image « ln(1 − x) = ln(2 + x) », OCR perd
  « ≥ 0 » de c. ; p.126 Act. 1 numérotation OCR brouillée (3 puis 4) ; p.127–128 tableau de variation et courbe : seule l'image donne −∞/+∞ ;
  p.128 Act. 2 entièrement perdue à l'OCR (racines et fractions) ; p.129 Act. 1 formule (ln(ⁿ√xᵐ)/ⁿ√xᵐ)ⁿ perdue ; p.130 signe de f′ et tableau
  de variation d'Exercice résolu 2 lisibles sur l'image seulement ; p.131 Act. 3 (quatre primitives) quasi illisible à l'OCR, lue sur l'image ;
  p.134–141 : exercices tous réécrits à partir de l'image (l'OCR a confondu ln/In, a perdu exposants, bornes et indices).
- **Doutes non levés** : (a) ex. 1 dernière expression : lue à 200 dpi, imprimée telle quelle (répétition probablement fautive) ; (b) levé (ex. 9 q.2 = ∫₁² 2/(x + 1) dx, zoom 200 dpi) ;
  (c) ex. 27 I : domaine [0,+∞[ imprimé pour g qui contient ln x (coquille source probable) ; (d) levé (ex. 30 A : f(x) = 1/x + 1/ln x, cohérent avec f′ et avec 30 B/1) ; (e) levé ; (f) VF 3 : « pour tout réel x » (x > 0 sous-entendu) ; (g) Stifel : « 0 » sous 0.
  Restent ouverts : (a), (c), (f), (g) — coquilles de la source à signaler, jamais à corriger en silence.

## 2.9 Chapitre 9 — Fonction exponentielle (manuel 222433, p.142–164)

**Page de garde (p.142)** — « Chapitre 9 », titre « Fonction exponentielle ». Citation liminaire (Euler 1748,
_Introductio_ §110) : « Des questions telles que "Si le nombre d'habitants d'une province s'accroît tous les ans
d'une trentieme, & qu'il y ait au commencement 100.000 habitants; on veut savoir combien il y en aura au bout de
100 ans ?" (Euler 1748, Introductio §110) ou "Un particulier doit 400.000 florins, dont il est convenu de payer
tous les ans l'intérêt à 5 pour cent..." En appliquant la formule du binôme, Euler dit sans la moindre hésitation,
"Si N est un nombre plus grand qu'aucune quantité assignable la fraction ((N−1)/N) égalera l'unité". [...] si N tend
vers l'infini, (1 + 1/N)^N tend vers le nombre d'Euler e. » — « (E.Haier et al, L'analyse au fil de l'histoire, 2000) »
(coquille source « Haier » [sic], comme les autres chapitres de la collection).

**Plan du chapitre** (numérotation source : **I, II, III, IV, V, VI, VIII — saute de VI à VIII, aucune partie « VII »** [sic]) :
I. Définition et propriétés (p.143–145) · II. Étude de la fonction exponentielle (p.145–146) · III. Limites usuelles
(p.146) · IV. La fonction x ↦ e^(u(x)) (p.147–150, avec 2 exercices résolus) · V. Exponentielle de base a
(p.150–152) · VI. Fonctions puissances (p.152–154) · VIII. Croissances comparées (p.154–155) · QCM – Vrai-Faux
(p.156) · Exercices et problèmes (p.157–164, **33 exercices**, numérotés 1–33 dans des cases).
_Ce manuel ne contient aucune équation différentielle ni aucun logarithme décimal._

### Cours — Activités (une ligne chacune)

**I. Définition et propriétés**
- **Act. 1** (p.143) : figure de ln. 1. valeur approchée graphique de l'antécédent de 1/2 et de −√2/2. 2. ln admet une
  réciproque notée exp, tracer sa courbe. 3. ensemble de définition de exp et limites aux bornes. 4. exp(0), exp(1), exp(2), exp(−1).
- **Act. 2** (p.143) : calculatrice, valeur approchée de e^(1/2), e^(2/3), e^√3, e^(−√2/2).
- **Act. 3** (p.143) : simplifier e^(ln 1), e^(ln 2), e^(−ln 3), ln(e^(−2)), ln(e^(−2 ln 3)).
- **Act. 4** (p.144) : simplifier ⁶√(e²)·e^(3/2) ; (√(e³)/√(e^−4))·⁴√(e²) ; (√(e^30)/√(e^−42))·¹⁰√(e^−20).
- **Act. 5** (p.145) : résoudre dans ℝ 1. e^x = 3 ; 2. ln x = 3 ; 3. e^(2x+3) = 4 ; 4. e^(2x+3) = e ; 5. (e^x − 1)(e^x − 2) = 0 ; 6. e^(2x) + e^x − 3 = 0.

**II. Étude de la fonction exponentielle**
- **Act. 1** (p.145) : C courbe de exp dans (O, i⃗, j⃗). 1. lim_{−∞} e^x, lim_{+∞} e^x. 2. X = e^x : a. e^x/x = X/ln X ; b. en déduire
  lim_{+∞} e^x/x, interpréter graphiquement. 3. a. dérivabilité de exp sur ℝ et dérivée ; b. lim_{x→0}(e^x − 1)/x ; c. tableau de variation.
  4. intersection de C avec les axes. 5. a. tangente T en 0 ; b. h(x) = e^x − x − 1, variations, position de C par rapport à T. 6. tracer C et T.
- **Act. 2** (p.146) : résoudre dans ℝ 1. e^(3x) ≤ e^(x²) ; 2. e^(3x) ≤ 4e^x ; 3. e^(x(x−1)) > 1.

**III. Limites usuelles**
- **Act. 1** (p.146) : f(x) = x e^x, C_f. 1. branche infinie en +∞. 2. a. lim_{t→+∞} t/e^t ; b. lim_{x→−∞} x e^x, interpréter. 3. tableau de variation. 4. point d'inflexion I. 5. tracer C_f et la tangente T en I.
- **Act. 2** (p.146) : 1. lim_{X→+∞} ln^m X / X^n et lim_{X→0⁺} X^n ln^m X (n, m ∈ ℕ*). 2. a. en déduire lim_{x→+∞} e^(nx)/x^m = +∞ ; b. lim_{x→−∞} |x^m e^(nx)|.
- **Act. 3** (p.146) : limites de x² − e^(2x) (+∞) ; x(e^(2x) − e^x) (+∞) ; x(e^(2x) − e^x) (−∞) ; (x + 1)/(e^x + 1) (−∞) ; e^x/(x³ + 1) (+∞) [bornes lues sur l'image].

**IV. La fonction x ↦ e^(u(x))**
- **Act. 1** (p.147) : étudier et représenter x ↦ e^(2x).
- **Act. 2** (p.147) : dériver x ↦ √x e^√x ; (2x + 1)e^(−3x) ; (e^(2x) + 1)/(2e^(2x) + 3) ; x³ e^(3x).
- **Act. 3** (p.147) : primitives sur ℝ de x ↦ e^(−3x) ; x e^(x²) ; (2x + 1)e^(x²+x) ; sin x · e^(cos x).
- **Act. 4** (p.147) : ∫₀¹ e^x dx ; ∫₀¹ e^(−x+1) dx ; ∫₀¹ e^x/(e^x + 1)² dx ; ∫₀¹ x e^(x²) dx.
- **Exercice résolu A** (énoncé p.147, solution p.148) : I = ∫₀¹ x e^x dx et J = ∫₀¹ x² e^x dx par intégration par parties (I = 1, J = e − 2).
- **Act. 5** (p.148) : I_n = ∫₀¹ x^n e^(−x) dx (n ≥ 1). 1. a. 0 ≤ I_n ≤ 1/(n + 1) ; b. lim I_n.
- **Exercice résolu B** (énoncé p.148, solution p.149–150) : f : x ↦ e^(−x²), C. 1. étudier et représenter f (f′(x) = −2x e^(−x²), f paire, asymptote y = 0, maximum 1 en 0). 2. F(X) = ∫₀^X f(x)dx (X ≥ 0), interprétation géométrique (aire). 3. a. x ≥ 1 : e^(−x²) ≤ e^(−x) ; b. pour tout X ≥ 1 : ∫₀¹ e^(−x²)dx ≤ F(X) ≤ ∫₀¹ e^(−x²)dx + ∫₁^X e^(−x)dx ; c. pour tout X ≥ 1 : e^(−1) ≤ F(X) ≤ 1 + e^(−1). 4. F croissante sur [1, +∞[ et majorée ⇒ limite finie L ; e^(−1) ≤ L ≤ 1 + e^(−1).

**V. Exponentielle de base a**
- **Act. 1** (p.150) : 1. calculer e^(3 ln 2), e^(4 ln(1/2)), e^(−ln(1/2)), e^(−2 ln √2). 2. a > 0, n entier : a^n = e^(n ln a).
- **Act. 2** (p.150) : p, q entiers, q ≥ 2, a > 0 : montrer a^(1/q) = q√a ; a^(p/q) = q√(a^p).
- **Act. 3** (p.150) : résoudre dans ℝ 2^x = 1/2 ; 10^(x+1) = 2^(−x+2) ; 2^x = 2^(−x+1).
- **Act. 4** (p.150) : f : x ↦ e^(x ln 2), g : x ↦ e^(−x ln 2). 1. étudier et représenter f. 2. le symétrique de A(a, f(a)) par rapport à l'axe des ordonnées est un point de C_g. 3. C_f et C_g symétriques par rapport à l'axe des ordonnées.
- **Act. 5** (p.152) : graphique de C₁ et C₂, courbes de f_{b₁} : x ↦ (b₁)^x et f_{b₂} : x ↦ (b₂)^x ; déterminer b₁, b₂ > 0 (figure, lue sur l'image).
- **Act. 6** (p.152) : lim_{+∞} 2^(x²−2x) ; lim_{−∞} 2^(x²−2x) ; lim_{−∞} (1/2)^(3−2x).

**VI. Fonctions puissances**
- **Act. 1** (p.152) : figure de x ↦ x⁴, x⁵, x^−4, x^−5 (x > 0) ; identifier chacune.
- **Act. 2** (p.152) : figure de x ↦ ³√x et x ↦ ³√(1/x) ; identifier chacune.
- **Act. 3** (p.153) : f sur ℝ*₊, f(x) = √(x³). 1. f(x) = e^((3/2) ln x). 2. étudier et représenter f. 3. bijection strictement croissante de ℝ*₊ sur ℝ*₊. 4. déterminer f⁻¹.
- **Act. 4** (p.153) : f(x) = ⁿ√x sur ℝ₊ (n ≥ 2) ; pour x > 0, f(x) = x^(1/n).
- **Act. 5** (p.153) : lim_{+∞} x^(2/3) ; lim_{0⁺} x^(2/3) ; lim_{+∞} x^(−4/3) ; lim_{0⁺} x^(−4/3).

**VIII. Croissances comparées**
- **Act. 1** (p.154) : deux figures à identifier : f : x ↦ (ln x)² et g : x ↦ √x (courbes C₁, C₂) ; h : x ↦ x² et t : x ↦ √(e^x) (courbes C₃, C₄). _Une seule activité 1 contenant deux consignes « Identifier chacune des courbes » (le libellé est répété sur l'image)._
- **Act. 2** (p.155) : 1. (1 + x)^(−3/4) ≤ x^(−3/4) pour x > 0. 2. comparer (1 + x)^(1/4) et 1 + x^(1/4) pour x > 0.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur l'image)

> **Définition — fonction exponentielle** (p.143, encadré) — « On appelle fonction exponentielle la fonction réciproque de la fonction logarithme népérien. L'image d'un réel x par la fonction exponentielle est noté e^x. » [sic « noté »]

> **Conséquences** (p.143, encadré) — « • Pour tout réel x et pour tout réel strictement positif y, y = e^x ⇔ x = ln y. • Pour tout réel x, ln(e^x) = x. • Pour tout réel x > 0, e^(ln x) = x. • ln e = 1. »

> **Propriétés** (p.144, encadré) — « Soit deux réels a et b. P₁. e^(a+b) = e^a × e^b, e^(−a) = 1/e^a, e^(a−b) = e^a/e^b. P₂. Pour tout entier n, e^(na) = (e^a)^n. P₃. Pour tout entier naturel q ≥ 2, e^(a/q) = q√(e^a). P₄. Pour tout entier naturel q ≥ 2 et tout entier p, e^((p/q)a) = q√(e^(pa)). » (démonstration : « p un entier naturel » [sic]) — **Démonstrations non encadrées** de P₁–P₄ juste dessous (p.144).

> **Théorème** (p.145, encadré) — « • lim_{x→−∞} e^x = 0, lim_{x→+∞} e^x = +∞, lim_{x→+∞} e^x/x = +∞, lim_{x→0} (e^x − 1)/x = 1. • La fonction exponentielle est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ e^x. La fonction exponentielle est strictement croissante sur ℝ. • La fonction exponentielle est bijective de ℝ sur ℝ*₊. » (courbe y = e^x à droite, repère de −3 à 2 ; **« e^x > 0 » n'est pas énoncé dans l'encadré**, contrairement à la référence).

> **Théorème** (p.146, encadré) — « Soit m et n deux entiers naturels non nuls, lim_{x→+∞} e^(nx)/x^m = +∞, lim_{x→−∞} x^m e^(nx) = 0. »

> **Théorème** (p.147, encadré) — « Soit u une fonction dérivable sur un intervalle I. La fonction h : x ↦ e^(u(x)) est dérivable sur I et h′(x) = u′(x)e^(u(x)), x ∈ I. » — Démonstration non encadrée : h = f ∘ u avec f : x ↦ e^x.

> **Corollaire** (p.147, encadré) — « Soit u une fonction dérivable sur un intervalle I. Les primitives sur I de la fonction x ↦ u′(x)e^(u(x)) sont les fonctions x ↦ e^(u(x)) + k, k ∈ ℝ. »

> **Encadré — puissance à exposant réel** (p.150) — « Soit un réel a > 0. Pour tout réel b, on pose a^b = e^(b ln a). »

> **Propriétés** (p.150, encadré) — « Pour tous nombres réels strictement positifs a et b et tous réels c et d, a^(c+d) = a^c × a^d ; (a^c)^d = a^(cd) ; a^(−d) = 1/a^d ; a^(c−d) = a^c/a^d ; a^c × b^c = (ab)^c ; a^c/b^c = (a/b)^c. » (introduit par « Les règles opératoires ci-dessous découlent des propriétés de la fonction logarithme népérien et de la fonction exponentielle. »)

> **Définition — exponentielle de base a** (p.151, encadré) — « Soit un réel a > 0. On appelle fonction exponentielle de base a la fonction x ↦ a^x. »

> **Conséquences** (p.151) — intro : « Les résultats ci-dessous découlent de la définition précédente et des propriétés de la fonction logarithme népérien et de la fonction exponentielle. » Encadré : « Soit un réel a > 0. La fonction x ↦ a^x est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ (ln a)a^x. » Hors encadré : « La fonction x ↦ a^x est strictement croissante sur ℝ si a > 1. La fonction x ↦ a^x est strictement décroissante sur ℝ si 0 < a < 1. La fonction x ↦ 1^x est une fonction constante. » Encadré : « Si a > 1 alors lim_{x→+∞} a^x = +∞ ; lim_{x→−∞} a^x = 0. Si 0 < a < 1 alors lim_{x→+∞} a^x = 0 ; lim_{x→−∞} a^x = +∞. » Suivent le tableau de variation de f : x ↦ a^x (a > 1 : f′ > 0, de 0 à +∞ ; 0 < a < 1 : f′ < 0, de +∞ à 0) et les courbes pour a = 0.5, 0.2, e, 2.

> **Notation** (p.153, hors encadré) — « Pour tout rationnel r et tout x > 0, on note e^(r·ln x) = x^r. »

> **Définition — fonction puissance** (p.153, encadré) — « Soit r un rationnel. On appelle fonction puissance r la fonction x ↦ e^(r·ln x), x > 0. »

> **Limites des fonctions puissances** (p.153, encadré ; intro : « Les résultats ci-dessous découlent des propriétés des limites des fonctions ln et exp. ») — « Si r > 0 alors lim_{x→+∞} x^r = +∞ ; lim_{x→0⁺} x^r = 0. Si r < 0 alors lim_{x→+∞} x^r = 0 ; lim_{x→0⁺} x^r = +∞. »

> **Théorème** (p.153, encadré) — « Soit r un rationnel. La fonction x ↦ x^r est dérivable sur ℝ*₊ et sa dérivée est la fonction x ↦ r x^(r−1). »

> **Corollaire** (p.154, encadré) — « Soit r un rationnel différent de −1. Les primitives sur ℝ*₊ de la fonction x ↦ x^r sont les fonctions x ↦ (1/(r + 1)) x^(r+1) + k, k ∈ ℝ. »

> **Théorème — limites usuelles** (p.154, encadré) — « Soit r un rationnel strictement positif. lim_{x→+∞} ln x / x^r = 0 ; lim_{x→0⁺} x^r ln x = 0 ; lim_{x→+∞} e^x / x^r = +∞. » — Démonstration non encadrée p.155 (ln x/x^r = (1/r)(ln x^r)/x^r ; e^x/x^r = e^(x − r ln x), x − r ln x = x(1 − r ln x/x) → +∞).

_Aucune « Méthode » encadrée dans ce chapitre._

### QCM (p.156) — « Cocher la réponse exacte. »

1. e^(−3 ln(1/2)) est égal à (☐ −1/8 / ☐ 8 / ☐ −6). 2. 2e^(x+y) est égal à (☐ e^(2x+2y) / ☐ e^(2x)e^(2y) / ☐ 2e^x e^y). 3. e^x = 1/e équivaut à (☐ x = −1 / ☐ x = ln e / ☐ x = e). 4. −2 < e^(x²−1) < 1 équivaut à (☐ e^(x²−1) > 0 / ☐ x² > 1 / ☐ −1 < x < 1). 5. f(x) = 2e^x/x⁴ − 1/x² sur ℝ* : (☐ lim_{+∞} f = 0 / ☐ = 2 / ☐ = +∞). 6. Sur ℝ*₊ la dérivée de f : x ↦ e^x/x est (☐ f′(x) = e^x / ☐ f′(x) = (x − 1)/(x²e^(−x)) / ☐ f′(x) = e^x(x + 1)/x²). 7. ∫₀¹ x e^(x²) dx est égale à (☐ e − 1 / ☐ ½e / ☐ ½(e − 1)).

### Vrai – Faux (p.156) — « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)

1. La fonction exponentielle est dérivable sur ℝ et égale à sa dérivée. 2. Pour tout x ∈ ℝ*₊, ln x < x < e^x. 3. Soit r un rationnel différent de −1 : la fonction x ↦ x^(r+1) est une primitive de x ↦ x^r sur ]0, +∞[ [_énoncé tel quel ; la bonne primitive porte le facteur 1/(r+1), d'où le Faux attendu_ — doute signalé]. 4. f(x) = (e^x − 1)/(e^x + 1) sur ℝ est paire. 5. (e^x + e^(−x))/2 = 1 équivaut à e^x = 1.

### Exercices et problèmes (p.157–164) — 33 exercices

- **Ex. 1** (p.157) : écrire sous la forme d'une puissance de e : e⁷/e², (e^−1)⁴/e, (e²)^−3, e²e^−3.
- **Ex. 2** (p.157) : 1. simplifier e^(5 ln 3), e^(−3 ln 2), ln(e^(−2/3)), e^(ln 3 − ln 2), e^(5 ln 2) − e^(3 ln 4), e^(2 ln 3)/e^(ln 81), e³/e^(4+ln 3).
- **Ex. 3** (p.157) : 1. écrire plus simplement e^x·e^−2x, e·e^x, (e^−x)², e^x/e^−x, e^(2x)/e^(1−x), (e^x)⁴/e^(2x). 2. vérifier a. e^(2x) + e^(−2x) + 2 = (e^x + e^−x)² ; b. (e^x − e^−x)/(e^x + e^−x) = (e^(2x) − 1)/(e^(2x) + 1).
- **Ex. 4** (p.157) : résoudre e^(2x−3) = 1 ; e^x = 2 ; e^(−2x) = −2 ; e^(3x+1) = e^(1−5x) ; (e^x)² − 3e^x + 2 = 0 ; e^(x²−16) = e^(x−4) ; e^(−x) + e^x = 2.
- **Ex. 5** (p.157) : résoudre e^(−x) ≤ 1 ; e^(−3x) ≥ 0 ; 2 − e^(1/x) > 0 ; e^x + 2/e^x − 3 ≤ 0.
- **Ex. 6** (p.157) : figure C₁…C₄ ; associer f : x ↦ −e^x, g : x ↦ e^−x, h : x ↦ 1/e^(2−x), k : x ↦ 1 + e^x à sa courbe.
- **Ex. 7** (p.157) : 21 limites : x² − e^x (+∞) ; e^(3x) − 2e^x (+∞) ; 2e^x − 1/x (+∞) ; 2e^x − 1/x (−∞) ; x e^(−(1−x)) (−∞) ; (x² − 2x + 3)e^x (−∞) ; (x² − x)e^x (−∞) ; x e^(1/x) (0⁺) ; x³ − e^(2x) (+∞) ; e^x/√(x+1) (+∞) ; (2x − e^x)/(x² + x) (+∞) ; e^(−1/x)/x (0⁺) ; (e^x − 1)/x (+∞) ; x²(e^(2x) − e^x) (+∞) ; (e^(2x) − 1)/x (0) ; x/(1 − e^−x) (0) ; (e^x − 1)/√(2x) (0⁺) ; x(e^(1/x) − 1) (+∞) ; x(e^(1/x²) − 1) (−∞) ; x(e^(1/x) − 1)/(e^(1/x) + 1) (+∞) ; x²(e^(1/x) − e^(1/(x+1))) en +∞ puis en −∞.
- **Ex. 8** (p.157–158) : dérivée f′ sur I de 2x − e^−x (ℝ) ; x² + e^(1/x) (ℝ*₊) ; x e^−x (ℝ) ; (x − 1)/e^x (ℝ) ; (e^(2x) − 1)/(x² + 1) (ℝ) ; 2x − 2 ln(1 + e^x) (ℝ) ; e^x ln x (ℝ*₊) ; e^−x(e^(2x) + e^x − 1) (ℝ) ; (e^x − e^−x)/(e^x + e^−x) (ℝ).
- **Ex. 9** (p.158) : pour f : x ↦ e^(x²), e^(−x²/2), e^(1/x), e^(−1/x), e^√x, x/(1 + e^−x) : ensemble de définition, ensemble de dérivabilité, f′(x), tableau de variation, représentation (étude des branches infinies).
- **Ex. 10** (p.158) : primitive de f sur I : e^(2x) (ℝ) ; x e^(x²+1) (ℝ) ; e^(tan x)/cos²x (]−π/2, π/2[) ; sin(2x)e^(cos²x) (ℝ) ; (1/(x−1)²)e^(1/(x−1)) (]1, +∞[) ; √(e^x) (ℝ) ; e^(2x)/(1 + e^(2x)) (ℝ) ; x e^(2x²) (ℝ).
- **Ex. 11** (p.158) : 1. ∫₀¹(1 + e^x)dx ; ∫₀¹ x e^(x²)dx ; ∫₀¹ e^x/(1 + e^x)dx ; ∫₁² dx/(1 + e^x) ; ∫₀¹ (1/x)e^(ln x)dx ; ∫₁² (1/x²)e^(1/x)dx. 2. par parties : ∫₁² 2x e^−x dx ; ∫₀¹ x³/e^(x²) dx ; ∫₀^(π/2) e^−x sin x dx ; ∫₀^(−ln 2) ln(1 + e^x)/e^x dx ; ∫₁⁰ x² e^x dx.
- **Ex. 12** (p.158) : f(x) = x − 1/(1 + e^x). 1. a. f′ > 0 ; b. tableau. 2. a. Δ₁ : y = x et Δ₂ : y = x − 1 asymptotes ; b. positions relatives. 3. tracer C.
- **Ex. 13** (p.158) : f(x) = (2 + e^x)/(1 + e^x). 1. f(x) = 2 − e^x/(1 + e^x). 2. calculer ∫₀¹ (2 + e^x)/(1 + e^x) dx.
- **Ex. 14** (p.158–159) : 1. ∫₀¹ e^x/(1 + e^x)dx et ∫₀¹ e^x/(1 + e^x)²dx. 2. a, b, c tels que 1/(1 + t)² = a + bt/(1 + t) + ct/(1 + t)² (t ≥ 0) ; en déduire I = ∫₀¹ 1/(1 + e^x)² dx. 3. J = ∫₀¹ x e^x/(1 + e^x)³ dx. 4. exprimer J en fonction de I, en déduire J.
- **Ex. 15** (p.159) : f(x) = e^x/(1 + e^x), C. 1. tableau de variation. 2. I(0, 1/2) : a. I ∈ C ; b. centre de symétrie ; c. tangente T : y = x/4 + 1/2. 3. f′(x) ≤ 1/4. 4. a. x > 0 : f(x) ≤ x/4 + 1/2 ; b. positions de C et T. 5. tracer C et T.
- **Ex. 16** (p.159) : f : x ↦ x − 2 + e^(−x/2), C. 1. variations. 2. a. D : y = x − 2 asymptote ; b. tracer D et C. 3. λ > 0, Δ : x = λ, A(λ) aire limitée par C, D, Δ et l'axe des ordonnées ; lim_{λ→+∞} A(λ).
- **Ex. 17** (p.159) : 10 limites : (√3)^x (+∞) ; (1/2)^(1−x) (+∞) ; 2^x/2^(x²+x) (+∞) ; (1/4)^x − (1/4)^(x+1) (−∞) ; (3^x + 3^(x+1))/(2^x + 2^(x−1)) (+∞) ; x^(1/3) − x^(2/3) (+∞) ; ln(x)/2^x (+∞) ; x^(1/3)e^−x (+∞) ; (x^(2/3) − x^(4/3)) ln x (0⁺) ; 2^x − e^x (+∞).
- **Ex. 18** (p.159) : f(x) = ln(2^x) − ln(x²) sur ]0, +∞[. 1. f(2), f(4). 2. variations, signe. 3. comparer x² et 2^x.
- **Ex. 19** (p.159) : f(x) = 4^x/(4^(2x) − 1) sur ℝ*. 1. f impaire. 2. variations sur ]0, +∞[. 3. a. résoudre f(x) = 4/15 ; b. en déduire f(x) = −4/15.
- **Ex. 20** (p.159) : intégrales : ∫₀¹ 3^x dx ; ∫₀^(−1) 3^x/(1 + 3^x)dx ; ∫₁² x^(4/3)dx ; ∫_{1/2}^1 4x^(−1/5)dx ; ∫₀¹ ⁴√x dx ; ∫₀^(1/ln 2) 2^x(1 + 2^x)²dx.
- **Ex. 21** (p.159–160) : g(t) = (1 − e^−t)/t si t > 0, g(0) = 1, sur [0, +∞[. 1. a. continue à droite en 0 ; b. lim en +∞. 2. a. g′(t) ; b. 1 − t ≤ e^−t (t ≥ 0), en intégrant sur [0, x] : e^−x ≤ 1 − x + x²/2 ; c. e^−u ≥ 1 − u + u²/2 − u³/6 (u ≥ 0) ; d. g dérivable en 0, g′(0). 4. tracer la courbe (_numérotation source : saute de 2 à 4_ [sic]).
- **Ex. 22** (p.160) : h(x) = (x − 2)e^x + 2 sur [0, +∞[ : 1. variations, h(0). 2. unique a ∈ [1, 2], h(a) = 0, signe de h. 3. f(x) = (e^x − 1)/x² sur ]0, +∞[ : a. limites aux bornes ; b. f′(x) = (xe^x − 2e^x + 2)/x³, tableau ; c. f(a) = −1/(a(a − 2)), signe de f(a). 4. tracer.
- **Ex. 23** (p.160) : f : x ↦ (e^x − e^−x)/(e^x + e^−x), C. 1. parité. 2. a. variations ; b. tracer C. 3. λ > 1, Δ : x = λ, A(λ) aire limitée par C, Δ, l'axe des abscisses et l'axe des ordonnées ; calculer A(λ).
- **Ex. 24** (p.160) : f(x) = x e^−x − x/2 sur [0, +∞[. 1. f′ et lim_{+∞} f. 2. a. g(x) = (1 − x)e^−x − 1/2 : sens de variation, g(x) = 0 a une unique solution a ∈ [0, 0.5] [la source nomme a] ; c. signe de g ; d. variations de f. 2. (_second « 2. »_ [sic]) h(x) = 1 − ½e^x sur [0, 0.5] : a. a unique solution de h(x) = x ; b. variations de h ; c. h([0, 0.5]) ⊂ [0, 0.5] ; c. (_second « c. »_ [sic]) −0,83 ≤ h′(x) ≤ 0 d'où |h(x) − a| ≤ 0,83|x − a|. 3. u₀ = 0, u_{n+1} = h(u_n) : a. u_n ∈ [0, 0.5] et |u_{n+1} − a| ≤ 0,83|u_n − a| ; b. convergence, limite.
- **Ex. 25** (p.160–161) : **I.** f(x) = (3 + x)e^(−x/2) sur ℝ. 1. limites en −∞, +∞. 2. tableau. 3. construire C. 4. a. f(x) = 3 a deux solutions ; α la non nulle : −2 < α < −3/2 ; b. nombre de solutions de f(x) = m selon m (graphique). **II.** φ(x) = 3e^(x/2) − 3. 1. f(x) = 3 ⇔ φ(x) = x. 2. a. φ′, φ″, φ′(α) = (α + 3)/2 ; b. variations de φ′ puis φ ; c. I = [−2, α]. 3. a. φ(I) ⊂ I ; b. 1/2 ≤ φ′(x) ≤ 3/4 sur I ; c. 0 ≤ ½(α − x) ≤ φ(α) − φ(x) ≤ ¾(α − x) (en intégrant sur [x, α]). 4. u₀ = −2, u_{n+1} = φ(u_n) : a. u_n ∈ I ; b. 0 ≤ α − u_{n+1} ≤ ¾(α − u_n) ; c. convergence, limite ; d. plus petit entier k avec (3/4)^k ≤ 10^−2, approximation de u_k à 10^−2 (calculatrice), valeur approchée de α à 2×10^−2 près.
- **Ex. 26** (p.161) : f(x) = x e^(−x+2) sur [0, +∞[. **I.** 1. tableau de variation. 2. branches infinies de C. 2. (_second « 2. »_ [sic]) a. tracer f et ln (C′), conjecturer le nombre de solutions de f(x) = ln x dans [1, +∞[ ; b. g(x) = ln x − f(x) strictement croissante sur [1, +∞[, unique solution α dans [1, +∞[ ; c. valeur approchée de α à 10^−2. **II.** double intégration par parties : I = ∫₀³ x² e^(−2x) dx ; 2. solide S de révolution autour de (Ox) de y = f(x), 0 ≤ x ≤ 3 : valeur approchée à 1 u.a près du volume V.
- **Ex. 27** (p.161–162) : **I.** g(x) = e^x(1 − x) + 1. 1. variations. 2. g(x) = 0 a une unique solution α dans [1.27, 1.28]. 3. signe de g. **II.** f(x) = x/(e^x + 1) + 2, C dans un repère orthogonal. 1. limite en +∞ et interprétation. 2. a. limite en −∞ ; b. D : y = x + 2 asymptote ; c. position de C/D. 3. a. f′ de même signe que g ; b. tableau. 4. tracer C, asymptotes, tangente en α. **III.** n ≥ 2, D_n = {M(x, y) : 2 ≤ x ≤ n, 2 ≤ y ≤ f(x)}, aire A_n. 1. faire apparaître D₅. 2. x ≥ 2 : (7/8)x e^−x ≤ x/(e^x + 1) ≤ x e^−x. 3. I_n = ∫₂^n x e^−x dx par parties. 4. encadrement de A_n par I_n. 5. (A_n) croissante et majorée ; lim I_n ; que dire de lim A_n.
- **Ex. 28** (p.162) : **I.** f(x) = ln(e^x + e^−x) sur [0, +∞[. 1. a. limite en +∞ ; b. f(x) = x + ln(1 + e^(−2x)), asymptote D : y = x ; c. position C/D. 2. variations, tableau. 3. tracer C et D. **II.** F(x) = ∫₀^x ln(1 + e^(−2t)) dt (sans calculer F(x)). 1. interprétation géométrique de F(a). 2. sens de variation de F. 3. a > 0 : 1/(1 + a) ≤ 1/(1 + t) ≤ 1 sur [0, a], d'où a/(1 + a) ≤ ln(1 + a) ≤ a. 4. ∫₀^x e^(−2t)/(1 + e^(−2t)) dt ≤ F(x) ≤ ∫₀^x e^(−2t) dt, puis ½ ln 2 − ½ ln(1 + e^(−2x)) ≤ F(x) ≤ ½ − ½e^(−2x). 5. limite L admise : ½ ln 2 ≤ L ≤ ½. 6. u_n = ∫_n^(n+1) ln(1 + e^(−2t)) dt : a. variations de h(t) = ln(1 + e^(−2t)) ; b. 0 ≤ u_n ≤ ln(1 + e^(−2n)) ; c. lim u_n. 7. S_n = Σ_{i=0}^{n−1} u_i en fonction de F et n ; convergence, limite.
- **Ex. 29** (p.162–163) : **I.** g(x) = (x + 1)² e^−x, C. 1. a. lim en −∞, +∞ ; b. g′, signe de (1 − x²) ; c. tableau. 2. tracer C (points d'abscisses −2, −1, 0, 1, 3). 3. a. nombre de solutions de g(x) = k (graphique) ; b. g(x) = 2 a une unique solution α ∈ [−2, −1] ; c. α = −1 − √2 e^(α/2). **II.** f(x) = −1 − √2 e^(x/2) sur I = [−2, −1]. 1. a. variations ; b. f(I) ⊂ I ; c. |f′(x)| ≤ 1/√(2e) ; d. |f(x) − α| ≤ ½|x − α|. 2. u₀ = −3/2, u_{n+1} = f(u_n) : a. |u_{n+1} − α| ≤ ½|u_n − α| ; b. convergence, limite ; c. entier n₀ tel que u_{n₀} approche α à 10^−3, calculer u_{n₀}.
- **Ex. 30** (p.163) : **I.** g(x) = e^x/(1 + 2e^x) − ln(1 + 2e^x). 1. g′ et son signe. 2. lim en −∞. 3. tableau, signe de g. **II.** f(x) = e^(−2x) ln(1 + 2e^x). 1. f′(x) = 2e^(−2x) g(x). 2. limites en +∞ et −∞. 3. tableau. 4. a. tangente T en 0 ; b. tracer C et T.
- **Ex. 31** (p.163–164) : **I.** 1. g(x) = e^x − x − 1 sur [0, +∞[ : variations, signe. 2. h(x) = (2 − x)e^x − 1 : a. variations ; b. h(x) = 0 a une unique solution α ∈ [1, 2] ; c. encadrement d'amplitude 10^−2 ; d. signe de h. **II.** f(x) = (e^x − 1)/(e^x − x) sur [0, +∞[, C. 1. a. f(x) = (1 − e^−x)/(1 − x e^−x), lim +∞, interpréter ; b. f′(x) = h(x)/(e^x − x)² ; c. tableau. 2. a. f(x) − x = (1 − x)g(x)/(e^x − x) ; b. position de C et Δ : y = x. 3. a. tangente en 0 ; b. tracer C. **III.** u_n = ∫₀^n (f(x) − 1) dx : 1. u_n en fonction de n ; 2. interpréter −u₁ ; 3. lim u_n (énoncé recopié tel qu'il s'imprime, doute sur « f(x) − 1 »).
- **Ex. 32** (p.164) : **I.** u(x) = x e^x − e^x + 1. 1. a. tableau, u(x) ≥ 0 ; b. u(x) = ∫₀^x t e^t dt. 2. a. 0 ≤ t ≤ x : t ≤ te^t ≤ te^x, d'où ½x² ≤ u(x) ≤ ½x²e^x (x ≥ 0) ; b. x ≤ t ≤ 0 : ½x²e^x ≤ u(x) ≤ ½x² (x ≤ 0). 3. a. lim_{x→0} u(x)/x² ; b. en déduire lim_{x→0} u(x)/(x(e^x − 1)) = 1/2. **II.** f(x) = x/(e^x − 1) si x ≠ 0, f(0) = 1. 1. a. continue en 0 ; b. dérivable en 0, f′(0). 2. a. f′(x) = −u(x)/(e^x − 1)² (x ≠ 0) ; b. tableau. 3. a. asymptote D en −∞ ; b. tracer C et D.
- **Ex. 33** (p.164) : **I.** g(x) = (1 + 1/x)e^(−1/x) sur ]0, +∞[ : 1. variations ; 2. 0 < g(x) < 1. **II.** f(x) = x ln(−x) si x < 0 ; x(2 − e^(−1/x)) si x > 0 ; 0 si x = 0. 1. a. continue en 0 ; b. dérivabilité à droite et à gauche en 0 ; c. f′(x) = 2 − g(x) (x > 0). 2. tableau. 3. a. asymptote D au voisinage de l'infini ; b. D tangente à C en un point d'abscisse négative ; c. position C/D pour x ≥ 0 ; d. tracer C et D ; e. C′ symétrique de C par rapport à l'axe des abscisses. **III.** α ∈ ]−1, 0[, A(α) aire entre C, C′, x = α et x = −1 : 1. ∫_{−1}^α f(x)dx ; 2. A(α) ; 3. lim_{α→0} A(α).

### Écart avec la référence (chapitre 08 de math-bac-math, manuel 222445, fiche l.2317–2694 ; et math-bac-techniques ch.07)

**La référence enseigne, ce manuel 222433 NE l'a PAS (à exclure du chapitre Sciences expérimentales) :**
- l'activité sur les valeurs **exp(n) = e^n**, **exp(a + b) = exp(a)exp(b)** et **exp(na) = (exp a)^n** (réf. Act. I.1 q.5–6) ; ici seuls exp(0), exp(1), exp(2), exp(−1) sont demandés (Act. I.1 q.4) ;
- l'**équation différentielle f′ = f** (Act. II.2 de la réf.) et ses conséquences (f = k e^x) ;
- l'activité **(1 + x/n)^n → e^x** (Act. I.6 de la réf.) et celle de la **tangente passant par l'origine / par (n, 0)** (Act. II.4) ;
- l'activité **x e^x** avec **f_n(x) = e^x − Σ x^k/k!** et la récurrence ; la limite **e = Σ 1/k!** par I_n = ∫₀¹ x^n e^−x dx (ici I_n sert seulement à 0 ≤ I_n ≤ 1/(n + 1) et lim I_n = 0) ;
- les activités fonctions puissances sur **f(x) = x^(2/3), x^(10/3)** (continuité, dérivabilité à droite en 0, aire, réciproques) ; les activités croissances comparées **(1 + x)^r vs 1 + rx**, **x^(1/x)** et **le signe de f′ − g′** ;
- les **deux exercices résolus de la référence** (f(x) = √|x − 1|e^(1/x) par dérivation logarithmique ; F(x) = ∫_x^(2x) e^−t/t dt) — remplacés ici par deux autres exercices résolus (IPP ∫x e^x, ∫x² e^x ; aire sous e^(−x²) et limite L) ;
- les exercices de la réf. à **dérivée n-ième** (f^(n)), **sommes/séries** (S_n = Σ 1/e^k ; Σ 1/k^α), **intégrale bêta** (I(n, m)), **I_n/J_n = ∫ e^(−nx) sin/cos**, **suites implicites à ln** (ex. 43 de la réf.), **équation 3^x + 4^x = 5^x** ; la réf. compte **43 exercices**, ce manuel **33** ;
- l'énoncé « e^x > 0 » dans l'encadré Théorème (ici seulement « bijective de ℝ sur ℝ*₊ »).

**Ce manuel a en plus (ou autrement) :**
- les **démonstrations** de P₁–P₄ (p.144), du théorème e^(u) (p.147) et du théorème ln x/x^r, e^x/x^r (p.155) ; la fiche de référence ne les liste pas ;
- la règle **a^(−d) = 1/a^d** dans l'encadré des propriétés de a^b (p.150) ;
- Act. V.5 (déterminer b₁ et b₂ sur graphique) et V.6 (limites de 2^(x²−2x)) ; l'encadré a^b = e^(b ln a) est identique à celui de la réf. ;
- **identifications de courbes** (x⁴, x⁵, x^−4, x^−5 ; ³√x, ³√(1/x) ; (ln x)², √x ; x², √(e^x)) ;
- les **primitives et intégrales de base** (Act. IV.3–4), 2 exercices résolus IPP/aire, exercices **14, 20, 28 II, 31 III** (intégrales de fractions en e^x, a^x, x^r) ;
- exercices **types bac** composés (25, 26, 27, 29, 31, 33) avec **suites récurrentes u_{n+1} = φ(u_n) et inégalité des accroissements finis intégrée** (|φ′| ≤ k) ; ex. 28 (F(x) = ∫ ln(1 + e^(−2t))dt, S_n) ;
- un exercice de **volume de solide de révolution** (ex. 26 II.2) — réinvestit la formule du ch. 7 (manuel p.111) ;
- numérotation source : parties I–VI puis **VIII** (pas de VII) ; la réf. saute de V à VII.
**Doutes à trancher en audit :** (2) VF 3 énoncé sans facteur 1/(r+1) ; (3) coquilles source de numérotation (Ex. 21 q.4 sans q.3 ; Ex. 24 deux « 2. » et deux « c. » ; Ex. 26 deux « 2. »).

### Bornes de scope observées (chapitre 9, section Sciences expérimentales)

- ✅ INCLUS : **exp = réciproque de ln**, e^x, équivalences y = e^x ⇔ x = ln y, ln(e^x) = x, e^(ln x) = x, ln e = 1 ; **propriétés algébriques** P₁–P₄ (e^(a+b), e^(−a), e^(a−b), e^(na), e^(a/q), e^((p/q)a)) ; **équations et inéquations** avec e^x (dont changement de variable X = e^x, factorisation) ; **étude de exp** (limites en ±∞, e^x/x → +∞, (e^x − 1)/x → 1, dérivée, croissance stricte, bijection ℝ → ℝ*₊, tangente en 0, position de C par rapport à x + 1) ; **limites usuelles** e^(nx)/x^m → +∞, x^m e^(nx) → 0 ; **dérivée de e^u**, **primitives de u′e^u** ; **intégrales** de la forme ∫ u′e^u, par parties (x e^x, x² e^x, e^−x sin x) ; **exponentielle de base a** (a^b = e^(b ln a), règles, dérivée (ln a)a^x, sens de variation, limites, courbes) ; **fonctions puissances rationnelles** x^r = e^(r ln x) (limites, dérivée r x^(r−1), primitive x^(r+1)/(r+1), ⁿ√x = x^(1/n)) ; **croissances comparées** ln x/x^r, x^r ln x, e^x/x^r ; **études complètes de fonctions** (variations, asymptotes, branches infinies, tracé, tangente, point d'inflexion, symétrie) ; **suites récurrentes u_{n+1} = φ(u_n)** par inégalité |φ′| ≤ k ; **suites définies par une intégrale** (I_n, u_n, S_n) ; aires et limites d'aires ; **volume d'un solide de révolution** autour de (Ox) (réinvestissement du ch. 7, ex. 26 II.2).
- ⛔ EXCLU (absent de ce manuel) : **équation différentielle f′ = f** et y′ = ay + b ; **logarithme décimal** ; **fonctions hyperboliques** ch, sh, th (seules apparaissent (e^x ± e^−x)/2 dans des exercices) ; **e = lim(1 + 1/n)^n** et **e = Σ 1/k!** (cités uniquement dans la citation de la page de garde) ; **dérivation logarithmique** ; **exposant irrationnel** pour x^α (la fonction puissance x^r reste énoncée pour r **rationnel**) ; dérivées successives f^(n) ; séries Σ 1/k^α ; intégrale bêta ; exp(a + b) comme question d'activité préliminaire.

### Lecture

- **Pages lues par l'OCR** : p.142 à p.164 (23 pages, texte `/root/.cache/yqa-manuels/222433/txt/p142…p164.txt`) ; l'OCR rend la prose mais dégrade presque toutes les formules (exposants, fractions, indices, bornes d'intégrales, racines n-ièmes, figures).
- **Pages lues sur l'image (110 dpi)** : **les 23 pages** p.142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164 (toutes les pages à formule, encadré ou tableau) ; agrandissements à 200–220 dpi : p.157 (ex. 7 : bornes des limites), p.158 (ex. 11 : bornes ∫₀^(π/2), ∫₁⁰), p.159 (ex. 17 : limites). Sondage image : **100 % des pages** (≥ 1 sur 10 requis).
- **Écarts OCR/image constatés** : p.143 Act. 1 « FE » pour −√2/2, Act. 2–3 illisibles (e^(ln 1), e^(−ln 3)…) ; p.144 encadré P₁–P₄ et démonstrations illisibles (« Ÿe », « e"* ») ; p.145 Act. 5 (« e^{2x+3}=e » et « 6. e^{2x}+e^x−3 = 0 » dégradés) et théorème (e^x/x, (e^x−1)/x) ; p.146 Act. 3 limites (« lim (2-7) ») et bornes ; p.147 Act. 2–4 (√x e^√x, intégrales sans bornes) ; p.148–149 exercice résolu B (exposants −x², bornes des ∫) ; p.150 Act. 1 (e^(4 ln(1/2)), e^(−ln(1/2)) lus « ln(12) ») et encadré des propriétés (a^(−d) = 1/a^d dégradé) ; p.151 tableaux de variation et courbes a = 0.5, 0.2, e, 2 ; p.152 figures C₁–C₄ illisibles ; p.153–154 exposants rationnels et encadrés ; p.155 démonstration (exposants r) ; p.156 QCM 1, 4, 5, 6, 7 et VF 3–5 ; p.157 à 164 : tous les exercices (indices u_n, bornes, fractions, ∫, énoncés complets). Aucun contenu inventé : toute formule de cette fiche a été relue sur l'image.

## 2.10 Chapitre 10 — Équations différentielles (manuel 222433, p.165–182)

**Page de garde (p.165)** — « Chapitre 10 », titre « Equations différentielles » [sic, sans accent sur le É dans tous les bandeaux du chapitre]. Citation liminaire : « Le pendule isochrone. Le problème consiste à modifier le pendule standard pour rendre la période indépendante de l'amplitude. Hygens [sic] (1673, Horologium Oscillatorium ) a l'idée de modifier le cercle du pendule standard pour que la force accélératrice devienne proportionnelle à la longueur d'arc s. Le mouvement du pendule serait alors décrit par s″+ Ks = 0, dont les oscillations sont indépendantes de l'amplitude. » Référence : « (E.Haier [sic] et al, _L'analyse au fil de l'histoire_, 2000). » (même citation que le chapitre de référence).

**Plan** : **I. Définition** (p.166) · **II. Équations différentielles du type y′ = ay + b, où a et b sont deux réels tels que a ≠ 0** (p.169) · **III. Équations différentielles du type y″ + ω²y = 0, ω réel** (p.170) · un **Problème résolu** (p.173–174, un seul) · **QCM – VRAI – FAUX** (p.175) · **Exercices et problèmes** (p.176–182). Pas de rubrique « Résumé » dans ces pages.

### Cours — Activités

**I. Définition** (p.166)

- **Activité 1** (p.166) : 1. f : x ↦ e^−x, relation entre f′ et f. 2. idem pour g : x ↦ −2e^−x et h : x ↦ 0,5e^−x. 3. représenter f, g, h dans un même repère orthonormé. 4. donner d'autres fonctions vérifiant la relation de la question 1.
- **Activité 2** (p.166) : population de bactéries, N₀ à t = 0, N(t), N′(t) vitesse instantanée. 1. N(t) = 9000 e^(−0,4t) : a. nombre aux instants t = 0, 10, 20 ; b. relation entre N′ et N ; c. vitesse instantanée à t = 10 et t = 20 ; d. représenter t ↦ N(t). 2. reprendre si N(t) = 3000 e^(−0,4t) [sur l'image l'exposant est « −0,4t » ; la référence transcrit « 0,4t » : écart, voir plus bas].
- **Activité 3** (p.167) : repère orthogonal, courbes de quatre fonctions f, g, h et t solutions de y′ = 0.3y (figure : C_g, C_t, C_f, C_h ; graduations ±5, ±10). Donner les expressions de f, g, h et t.
- **Activité 4** (p.167) : 1. a. résoudre (E) : 2y′ + 3y = 0 ; b. montrer qu'il existe une unique solution f de (E) vérifiant f(0) = −3 ; c. la représenter. 2. reprendre pour (E) : y′ = 0.
- **Activité 5** (p.168) : repère (O, i⃗, j⃗). Représenter la fonction f dont la courbe C_f passe par A(1, 2) et telle que la tangente en tout point M de C_f a un coefficient directeur égal au double de l'ordonnée de M.
- **Activité 6** (p.168) : substance radioactive, N(t) (t en années), N₀ ; N′(t) proportionnelle à N(t) de coefficient −λ (λ > 0 constante radioactive). 1. expression de N(t). 2. temps T₀.₅ (demi-vie) en fonction de λ. 3. carbone 14 : a. λ sachant T₀.₅ = 5730 ; b. âge d'un fragment d'os contenant 60 % de la quantité initiale.

**II. y′ = ay + b, a ≠ 0** (p.169–170)

- **Activité 1** (p.169) : figure de f : x ↦ e^(−2x) + 3. 1. montrer que f vérifie (E) : y′ = −2y + 6. 2. g solution de (E) ssi h : x ↦ g(x) − 3 solution de y′ = −2y. 3. donner toutes les solutions de (E).
- **Activité 2** (p.170) : donner la solution f et la représenter : a. √2 y′ − 2y = 1, f(0) = −1 ; b. √2 y′ − 2y = 1, f(0) = −1/2.
- **Activité 3** (p.170) : circuit (générateur G tension E, condensateur C, résistance R) ; i(t) intensité (t en seconde), q(t) charge. 1. relation entre i(t) et q′(t). 2. montrer que R q′(t) + (1/C) q(t) = E. 3. q(t), puis i(t). 4. représenter t ↦ i(t) si i(0) = 10 mA. (Figure du circuit.)

**III. y″ + ω²y = 0, ω réel** (p.170–173)

- **Activité 1** (p.170) : 1. f : x ↦ sin x + cos x : a. r > 0 et φ ∈ ]−π, π] tels que f(x) = r cos(x − φ) ; b. écrire f″ en fonction de f ; c. représenter f. 2. idem pour g : x ↦ √3 sin(2x) − cos(2x).
- **Activité 2** (p.170) : figure d'une courbe sinusoïdale de la forme f : x ↦ a sin(3x) + b cos(3x) (graduations −2…2, −π, π). 1. déterminer a et b. 2. f deux fois dérivable sur ℝ, relation entre f″ et f.
- **Activité 3** (p.171) : (E) : y″ + 9y = 0, y deux fois dérivable sur ℝ. 1. x ↦ sin(3x) solution. 2. x ↦ cos(3x) solution. 3. a. pour tous a, b réels, f : x ↦ a sin(3x) + b cos(3x) solution ; b. f(0) = √3/2 et f′(0) = 3/2, déterminer a et b ; c. r > 0 et φ ∈ ]−π, π] tels que f(x) = r cos(3x − φ) ; d. représenter f.
- **Activité 4** (p.171) : ω ≠ 0, x₀, y₀ réels, (E) : y″ + ω²y = 0. 1. f(x) = (y₀/ω) sin(ωx) + x₀ cos(ωx) solution de (E) ; vérifier f(0) = x₀ et f′(0) = y₀. 2. g autre solution avec g(0) = x₀, g′(0) = y₀ ; h(x) = ω²(f(x) − g(x))² + (f′(x) − g′(x))² : a. h dérivable sur ℝ et h′(x) = 2ω²(f′(x) − g′(x))(f(x) − g(x)) + 2(f″(x) − g″(x))(f′(x) − g′(x)) ; b. h constante sur ℝ ; c. calculer h(0) et conclure.
- **Activité 5** (p.172) : 1. a. solution f de y″ + 4y = 0 telle que f(π/2) = −1 et f′(π/2) = 2 ; b. représenter f ; c. résoudre dans ℝ f(x) = 1, f(x) = −1. 2. idem pour la solution g de y″ + π²y = 0 avec g(0) = 0 et g′(0) = 1.
- **Activité 6** (p.172) : ω ≠ 0, (E) : y″ + ω²y = 0. A/ 1. x ↦ cos(ωx) et x ↦ sin(ωx) solutions. 2. x ↦ A sin(ωx) + B cos(ωx) solution pour tous A, B. B/ f solution de (E) : 1. g(x) = f(x) − A sin(ωx) − B cos(ωx) solution de (E) ; 2. a. déterminer g′(x) ; b. en déduire qu'il existe un unique couple (A, B) tel que g(0) = g′(0) = 0 ; 3. montrer que les solutions de (E) sont les x ↦ A sin(ωx) + B cos(ωx), (A, B) ∈ ℝ².
- **Activité 7** (p.173) : 1. résoudre dans ℝ y″ + 9y = 0. 2. montrer qu'il existe une seule solution de (E) telle que f(π/12) = √2/2 et f(π/3) = −1/2. 3. existe-t-il une solution de (E) telle que f(0) = 1/2 et f(2π/3) = 1 ?

### Cours — encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Vocabulaire** (p.166, non encadré) — « Une équation de la forme y′ = ay, où l'inconnue y est une fonction et a est un réel, est appelée équation différentielle linéaire du premier ordre à coefficient constant. Résoudre dans ℝ une équation de la forme y′ = ay, c'est trouver toutes les fonctions dérivables sur ℝ qui vérifie [sic] y′ = ay. Ces fonctions sont appelées solutions sur ℝ de l'équation y′ = ay. »

> **Théorème** (p.166) — « Soit a un réel. L'ensemble des solutions de l'équation différentielle y′ = ay est l'ensemble des fonctions définies sur ℝ par f : x ↦ ke^(ax), où k est un réel quelconque. »

> **Démonstration** (p.167, non encadrée) — « Désignons par (E) l'équation différentielle y′ = ay. Pour tout réel k, la fonction f définie sur ℝ par f(x) = ke^(ax) est dérivable sur ℝ et vérifie f′(x) = kae^(ax) = af(x), pour tout x de ℝ. Réciproquement, montrons que toute solution g de (E) est telle que g(x) = ke^(ax), pour tout x de ℝ. Soit g une solution de (E) et h la fonction définie pour tout réel x par h(x) = g(x)e^(−ax). La fonction h est dérivable sur ℝ et h′(x) = g′(x)e^(−ax) − ag(x)e^(−ax), pour tout réel x. La fonction g étant solution de (E) par hypothèse, on en déduit que h′(x) = ag(x)e^(−ax) − ag(x)e^(−ax), ou encore que h′(x) = 0, pour tout réel x. Ce qui implique que la fonction h est constante sur ℝ, c'est à dire qu'il existe un réel k tel que h(x) = g(x)e^(−ax) = k, pour tout x de ℝ. Il en résulte que g(x) = ke^(ax), pour tout réel x. »

> **Théorème** (p.167) — « Soit a un réel non nul. Pour tous réels x₀ et y₀, l'équation y′ = ay admet une unique solution qui prend la valeur y₀ en x₀. C'est la fonction définie sur ℝ par f : x ↦ y₀e^(a(x−x₀)). »

> **Démonstration** (p.168) — « Soit f une solution de (E) qui prend la valeur y₀ en x₀. Alors f(x) = ke^(ax), pour tout x de ℝ et ke^(ax₀) = y₀. Il en résulte que k = y₀e^(−ax₀). Par suite f(x) = y₀e^(a(x−x₀)), x ∈ ℝ. »

> **Théorème** (p.169) — « Soit a et b deux réels tels que a ≠ 0. L'ensemble des solutions de l'équation différentielle y′ = ay + b est l'ensemble des fonctions f : x ↦ ke^(ax) − b/a, où k est un réel quelconque. De plus pour tous réels x₀, y₀, la fonction f : x ↦ (y₀ + b/a)e^(a(x−x₀)) − b/a est l'unique solution de y′ = ay + b, telle que f(x₀) = y₀. »

> **Démonstration** (p.169, non encadrée) — « Soit a non nul. L'équation différentielle (E) : y′ = ay + b, est équivalente à l'équation différentielle (E₁) : (y + b/a)′ = a(y + b/a). On en déduit qu'une fonction f est solution de (E), si et seulement si, f + b/a est solution de (E₁). Il en résulte que les solutions de (E) sont les fonctions f : x ↦ ke^(ax) − b/a, où k est un réel quelconque. Si f est une solution de (E) prenant la valeur y₀ en x₀, alors f(x₀) = ke^(ax₀) − b/a = y₀. On en déduit que k = (y₀ + b/a)e^(−ax₀), ou encore que f est la fonction définie sur ℝ par f(x) = (y₀ + b/a)e^(a(x−x₀)) − b/a. »

> **Vocabulaire** (p.171, non encadré) — « Une équation de la forme y″ + ω²y = 0, où l'inconnue y est une fonction et ω est un réel, est appelée équation différentielle linéaire du second ordre à coefficients constants. Résoudre une équation de la forme y″ + ω²y = 0, c'est trouver toutes les fonctions deux fois dérivable [sic] sur ℝ qui la vérifient. »

> **Théorème** (p.172) — « Soit ω un réel non nul et x₀, y₀ deux réels. L'équation y″ + ω²y = 0 admet une unique solution dans ℝ vérifiant f(0) = x₀ et f′(0) = y₀. C'est la fonction définie sur ℝ par f(x) = (y₀/ω) sin(ωx) + x₀ cos(ωx). »

> **Conséquence** (p.172, non encadrée) — « Soit ω un réel non nul. La fonction nulle est l'unique solution de l'équation différentielle y″ + ω²y = 0 qui vérifie y(0) = y′(0) = 0. »

> **Théorème** (p.173) — « Soit ω un réel non nul. L'ensemble des solutions de l'équation différentielle y″ + ω²y = 0 est l'ensemble des fonctions définies sur ℝ par f(x) = A sin(ωx) + B cos(ωx), (A, B) ∈ ℝ². »

(Le théorème de p.172 est établi via l'Activité 4, celui de p.173 via l'Activité 6, comme dans la référence ; ici, en plus, les trois premiers théorèmes sont suivis d'une démonstration rédigée, p.167, 168, 169.)

### Cours — Problème résolu (p.173–174) — un seul

**Problème résolu** (énoncé p.173, solution p.173–174) : mobile sur un axe horizontal (x′x), mouvement « uniformément varié » [sic]. x(t) position, x′(t) vitesse, x″(t) accélération (t en secondes, x en mètres) ; x″(t) proportionnelle à x(t) avec un coefficient égal à −π²/4. 1. équation horaire si x(1) = 2 et x(2) = 0 (solution : x″ + (π²/4)x = 0 ; x(t) = A sin((π/2)t) + B cos((π/2)t), t ∈ ℝ₊ ; A = 2, B = 0 ; x(t) = 2 sin((π/2)t), t ≥ 0). 2. position et vitesse à t = 0 (x(0) = 0 ; x′(t) = π cos((π/2)t), x′(0) = π m/s). 3. représenter t ↦ x(t) (période 4, étude sur [0, 4] ; tableau : x′(t) : + sur [0,1], 0 en 1, − sur [1,3], 0 en 3, + sur [3,4] ; x : 0 ↗ 2 ↘ −2 ↗ 0 ; courbe sinusoïdale).

### QCM – VRAI – FAUX (p.175)

**QCM** « Cocher la réponse exacte. » 1. x ↦ 2e^(2x) est solution de (☐ y′ = 4y / ☐ y′ = −4y / ☐ y′ = 2y). 2. f solution de y′ = 2y avec f(0) = 1 : la courbe de f admet une tangente (☐ horizontale / ☐ parallèle à y = 2x / ☐ parallèle à y = −x). 3. f solution de y′ = −y + 1 avec f(0) = 1 : f est (☐ négative / ☐ positive / ☐ n'a pas un signe constant). 4. x ↦ 2 cos x − 3 sin x est solution de (☐ y″ + 2y = 0 / ☐ y″ + y = 0 / ☐ y″ + 3y = 0).

**Vrai – Faux** « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies) 1. f : x ↦ 2^x est solution sur ℝ de y′ − y ln 2 = 0. 2. Si f est solution sur ℝ de y′ = −2y alors f est croissante sur ℝ. 3. Si f est la solution sur ℝ de y′ = 3y telle que f′(1) = 3 alors f(1) = 1. 4. Si f est la solution sur ℝ de y″ + 2y = 0 qui s'annule et change de signe en π/4 alors sa courbe dans un repère orthonormé admet un point d'inflexion.

### Exercices et problèmes (p.176–182) — 29 exercices (numérotation imprimée avec trous : 2, 10 et 19 absents)

- **Ex. 1** (p.176) : 1. résoudre dans ℝ a. y′ + 3y = 0 ; b. y′ + √2 y = 0 ; c. −5y′ + y = 0. 2. solution f sur ℝ : a. y′ − y/2 = 0, y(−1) = e ; b. −3y′ − y = 0, y(ln 8) = 1 ; c. y′ − 2y = 0, y(0) = 1.
- **Ex. 3** (p.176) : 1. résoudre sur ℝ a. y′ − 2y + 1 = 0 ; b. y′ − πy + 3 = 0 ; c. −2y′ + 5y − 1 = 0. 2. solution f : a. y′ − y − 1 = 0, y(2) = 0 ; b. 2y′ + y − 3 = 0, y(0) = 3 ; c. y′ + 3y + 3/4 = 0, y(−1) = 0.
- **Ex. 4** (p.176) : loi de refroidissement de Newton ; air à 25 °C ; corps de 100 °C à 75 °C en 15 min ; f(t) température à t minutes. 1. vérifier qu'il existe a tel que { f′(t) = a(f(t) − 25), f(0) = 100, f(15) = 75 }. 2. déterminer f. 3. au bout de combien de temps (à 1 min près) 25 °C ?
- **Ex. 5** (p.176) : substance se dissolvant à une vitesse proportionnelle à la quantité non dissoute ; 20 g, les dix premiers grammes en 5 min. 1. quantité dissoute f(t) (g, t en min). 2. quantité non dissoute (à 1 mg près) au bout de 10 min ? 30 min ? 1 heure ?
- **Ex. 6** (p.176) : concentration C(t) (mg/l) d'un médicament, t en heures, C(0) = 5, C′(t) = −0.25 C(t). 1. C(t). 2. représenter C. 3. encadrement à 0.1 près de l'instant t₀ à partir duquel C(t) < 1.
- **Ex. 7** (p.176) : charge/décharge d'un condensateur sur [0, 2 ln 3[ : f solution de y′ + y = 0 avec f(ln 3) = −2. 1. f(x). 2. étudier f et la représenter.
- **Ex. 8** (p.176) : 1. vérifier que u : x ↦ 2 vérifie y′ + 2y = y². 1. [sic, « 1 » répété] E = fonctions dérivables sur ℝ, ne s'annulant pas, telles que f′(x) + 2f(x) = (f(x))². a. E non vide ; b. f ∈ E : g = 1/f solution d'une équation y′ = ay + b ; c. déterminer E.
- **Ex. 9** (p.177) : microbes, y′(t) = ky(t), k > 0, N à t = 0 (t en heures). 1. unique solution de y′ = ky avec y(0) = N. 2. quadruplé en 2 h : nombre au bout de 3 h en fonction de N. 3. N sachant 6400 microbes au bout de 5 h.
- **Ex. 11** (p.177) : (E) : y′ + 2y = x². 1. solutions de (E₀) : y′ + 2y = 0. 2. un trinôme du second degré g vérifiant (E). 3. f solution de (E) ssi f − g solution de (E₀). 4. solutions de (E).
- **Ex. 12** (p.177) : (E) : y′ − y = 4 cos x. 1. solutions de (E₀) : y′ − y = 0. 2. a, b tels que g(x) = a cos x + b sin x vérifie (E). 3. f solution de (E) ssi f − g solution de (E₀). 4. solutions de (E).
- **Ex. 13** (p.177) : bobine, L y′ + r y = E ; E = 10 v, r = 100 Ω, L = 0.2 H ; intensité nulle à t = 0. 1. i(t). 2. limite de i en +∞, interpréter.
- **Ex. 14** (p.177) : solution f sur ℝ : 1. y″ + 2y = 0, y(0) = 1, y′(0) = √2. 2. y″ + 16y = 0, y(π) = −1, y′(π) = −2. 3. y″ + y/4 = 0, y(−π) = 1, y′(−π) = 0.
- **Ex. 15** (p.177) : (E) : y″ = 2y′. 1. en posant z = y′, résoudre sur ℝ. 2. solution f avec f′(0) = 1 et f(0) = 2.
- **Ex. 16** (p.177) : (E) : y″ = −3y′ + 1. 1. en posant z = y′, résoudre sur ℝ. 2. solution f avec f′(0) = 0 et f(0) = 0.
- **Ex. 17** (p.177) : 1. résoudre y″ + 16y = 0. 2. solution f avec f(0) = 1, f′(0) = 4. 3. a, b > 0 tels que f(t) = √2 cos(at − b). 4. valeur moyenne de f sur [0, π/8].
- **Ex. 18** (p.177) : 1. résoudre dans ℝ y″ + y′ = 0. 2. en déduire les solutions de y‴ + y″ = 0.
- **Ex. 20** (p.178) : 4y″ + π²y = 0. 1. résoudre. 2. repère orthonormé (O, i⃗, j⃗) ; g solution dont la courbe passe par N(1/2, √2/2) avec tangente en N parallèle à l'axe des abscisses. 3. vérifier g(x) = (√2/2) cos((π/2)x − π/4).
- **Ex. 21** (p.178) : circuit RC (C capacité, R résistance, U tension) ; R q′(t) + (1/C) q(t) = U, q(0) = 0. 1. équation différentielle vérifiée par q. 2. montrer q(t) = CU − CU e^(−t/RC). 3. i(t) = q′(t), déterminer i(t). (Figure.)
- **Ex. 22** (p.178) : f continues sur ℝ avec (E) : f(x) = ∫₀ˣ f(t)dt + x. 1. f vérifie (E) ⇒ f dérivable. 2. toute solution de (E) est solution de (E′) : y′ = y + 1 ; réciproquement, quelle condition ? 3. résoudre (E).
- **Ex. 23** (p.178) (**La piqûre intraveineuse**) : dose de 1.8 unité à t = 0 (h), Q′(t) = −αQ(t). 1. Q(t) = 1.8 e^(−αt) ; baisse de 30 % en une heure : équation en α ; via x ↦ e^−x, unique α tel que e^(−α) = 0.7 ; valeur approchée à 10⁻⁴. 2. variation de Q (t ≥ 0), limite en +∞, courbe C. 3. réinjections à t = 1, 2, 3… ; Rₙ quantité à t = n après injection : a. R₁ = 1.8 + 0.7 × 1.8 ; b. R₂ = 1.8 + 0.7 × R₁, calculer R₂ ; c. R_{n+1} en fonction de Rₙ ; d. Rₙ = 6(1 − (0.7)^(n+1)) ; e. limite de Rₙ.
- **Ex. 24** (p.179) : (I) y′ = 2y, (II) y′ = y. 1. résoudre. 2. graphique (courbe C de f et tangente T, repère orthonormé) ; f = f₁ − f₂ (f₁ solution de (I), f₂ de (II)) : a. f(0), f′(0) lus ; b. f₁, f₂, d'où f(x) = 2e^(2x) − e^x ; c. limites en −∞, +∞ ; d. abscisse du point d'intersection avec l'axe des abscisses. 3. t < −ln 2 : a. aire 𝒜(t) limitée par C, l'axe des abscisses, x = t, x = −ln 2 ; b. lim_{t→−∞} 𝒜(t) = ∫_{−ln 2}^0 f(t)dt, interpréter.
- **Ex. 25** (p.179) : 1. a. résoudre (E) : 4y′ + 3y = 0 ; b. solution f avec f′(0) = −6. 2. g(x) = 8e^(−0.75x) sur I = [0, 4] : a. variations et courbe (C) ; b. volume V du solide de révolution du domaine entre (C), l'axe des abscisses, x = 0, x = 4 autour de l'axe des abscisses ; valeur exacte en cm³ puis approchée arrondie au mm³.
- **Ex. 26** (p.179) : masse de sel m(t) (g, t en min), m(0) = 300, (E) : 5y′ + y = 0 sur [0, +∞[. 1. a. résoudre (E) ; b. m(t) = 300e^(−0.2t). 2. t₀ tel que m(t₀) = 150. 3. indétectable ssi m(t) ≤ 10⁻² : à partir de quel instant ?
- **Ex. 27** (p.179) : g(x) = cos x − sin x. 1. g′(x) = g(π − x). 2. f dérivables sur ℝ avec f′(x) = f(π − x) : a. f deux fois dérivable et solution de y″ + y = 0 ; b. déterminer les f.
- **Ex. 28** (p.180) : A/ (E) : y′ − 2y = −2/(1 + e^(−2x)). 1. solution de y′ − 2y = 0 valant 1 en 0. 2. f dérivable, f(0) = ln 2, f(x) = e^(2x) g(x) : a. g(0) ; b. f′(x) en fonction de g′, g ; c. f solution de (E) ssi g′(x) = −2e^(−2x)/(1 + e^(−2x)) ; d. g(x) puis f(x). B/ f(x) = e^(2x) ln(1 + e^(−2x)) : 1. h(x) = ln(1 + e^(−2x)) − 1/(e^(2x) + 1) : a. limite en +∞ ; b. variation ; c. signe. 2. f′(x) du signe de h(x). 3. limite en +∞ ; f(x) = e^(2x)[−2x + ln(1 + e^(2x))] ; limite en −∞. 4. tableau de variation. 5. courbe (5 cm), tangente en 0. C/ 1. primitive de x ↦ 1/(1 + e^(−2x)) (remarque 1/(1 + e^(−2x)) = e^(2x)/(1 + e^(2x))). 2. aire (cm²) entre l'axe, la courbe, x = −1, x = 0 par intégration par parties ; exacte et approchée à 10⁻³. D/ u₀ = 0, u_{n+1} = f(uₙ) : 1. f([0,1]) ⊂ [0,1], uₙ ∈ [0,1] ; 2. croissante (récurrence), converge vers α ; 3. f(α) = α et 0 < α < 1 ; 4. valeur approchée de α à 10⁻¹ près (graphique).
- **Ex. 29** (p.180) : loi de Newton θ′(t) = k[T − θ(t)], k = 0.1, θ₀ = 30 °C (t en min). 1. équation différentielle avec conditions initiales. 2. T = 100 °C : a. θ ; b. limite en +∞, interpréter. 3. courbes pour T = 100, 30 et −10 °C.
- **Ex. 30** (p.181) : fil conducteur, θ′(t) + 0.1θ(t) = 2, θ(0) = 0 (t en s). 1. θ(t), t ∈ ℝ₊. 2. a. température à 10 s, à 1 min ; b. limite en +∞, interpréter.
- **Ex. 31** (p.181) : A/ f(x) = 3e^(x/5)/(e^(x/5) + 2), repère orthogonal (1 cm, 5 cm) : 1. variations, asymptotes. 2. tangente T en 0. 3. tracer. 4. a. primitive de f s'annulant en 0 ; b. aire limitée par l'axe des abscisses, l'axe des ordonnées, (C) et x = 5. B/ 1. poissons g′ = g/5 (I) (milliers, t en années) : a. résoudre (I) ; b. g(0) = 1, expression de g. 2. avec prédateur g′ = g/5 − g²/15 (II) : a. h = g/(3 − g), g(t) ≠ 3 : g solution de (II) ssi h solution de (I) ; b. h puis g ; c. g solution de (II) avec g(0) = 1, coïncide avec f de A ; d. limite de la population.
- **Ex. 32** (p.181–182) : circuit fermé (C farads, L henrys, interrupteur), condensateur chargé à t = 0 ; q(t) deux fois dérivable sur [0, +∞[, (E) : y″ + (1/LC)y = 0 ; C = 1.25×10⁻³, L = 0,5×10⁻². 1. résoudre (E). 2. q(0) = 6×10⁻³, q′(0) = 0. 3. i(t) = −q′(t) : a. i(t) = 2.4 sin(400t) ; b. calculer (400/π)∫₀^(π/400) cos(800t)dt ; c. intensité efficace I_e > 0 : (I_e)² = (400/π)∫₀^(π/400) i²(t)dt ; calculer (I_e)², puis I_e à 10⁻³ près.

### Écart avec la référence (chapitre 9 de math-bac-math, manuel 222445)

**La référence enseigne et ce manuel n'a PAS (à exclure)** :
- le **Problème résolu 1 « sous tangente »** (courbe y = e^−x, sous tangente constante, y′ = −(1/a)y) : absent ; seul le problème résolu du mobile (ref. PR2) est présent, avec x″ + (π²/4)x = 0 ;
- **Ex. 2** de la référence (f′ = af, f(0) = 1, f(x + 10) = 2f(x)), **Ex. 10** (f(x) = e^−x sin x : variations, tangentes communes, f″ + 2f′ + 2f = 0, aire) et **Ex. 19** (linéariser cos⁴ x, y″ + y′ = cos⁴ x par a cos 4x + b cos 2x + c) : absents (numéros 2, 10, 19 sautés dans la numérotation imprimée ; 29 exercices au lieu de 32). Donc plus de linéarisation de cos⁴ et plus d'équation y″ + y′ = second membre trigonométrique.
- Le chapitre est numéroté 10 (pas 9) et tient en 18 pages (p.165–182) contre 19 (p.189–207).

**Ce manuel a en plus** : rien de nouveau en notions ; il imprime en revanche les **trois démonstrations rédigées** (théorèmes y′ = ay p.167, unicité p.168, y′ = ay + b p.169) que la référence ne fait que signaler. Les activités (6 + 3 + 7), les encadrés, le QCM et les exercices 1, 3–9, 11–18, 20–32 sont identiques à la référence dans leurs données.

**Divergences de texte relevées sur l'image (à trancher à la rédaction)** : Activité 2 p.166, question 2 : « N(t) = 3000e^(−0,4t) » sur l'image, « 3000 e^(0,4t) » dans la référence (cas croissant vs décroissant : à ne pas copier sans choisir ; l'énoncé du manuel fait foi) ; Vrai-Faux 1 p.175 : « y′ − y ln 2 = 0 » sur l'image (énoncé vrai), « y′ − ln 2 − y = 0 » dans la référence.

### Bornes de scope

- ✅ INCLUS : **y′ = ay** (vocabulaire « linéaire du premier ordre à coefficient constant », solutions x ↦ ke^(ax), problème de Cauchy f(x₀) = y₀ ⇒ f(x) = y₀e^(a(x−x₀)), avec démonstration) ; **y′ = ay + b**, a ≠ 0 (solutions ke^(ax) − b/a, condition initiale, changement f + b/a) ; **y″ + ω²y = 0** (vocabulaire « second ordre à coefficients constants », solutions A sin(ωx) + B cos(ωx), unicité sous f(0) = x₀, f′(0) = y₀, conséquence de la solution nulle, passage à r cos(ωx − φ), φ ∈ ]−π, π]). Méthodes : résolution avec second membre par solution particulière (trinôme, a cos x + b sin x : Ex. 11, 12) puis équivalence « f solution ssi f − g solution de (E₀) » ; réduction d'ordre z = y′ (Ex. 15, 16, 18) ; équation intégrale se ramenant à y′ = y + 1 (Ex. 22) ; changement de fonction f = e^(2x)g (Ex. 28), h = 1/f (Ex. 8), h = g/(3 − g) (Ex. 31). Modélisations : désintégration radioactive (demi-vie, carbone 14), refroidissement de Newton, dissolution, médicament, population (bactéries, microbes, poissons, modèle à prédateur), circuits RC, bobine L-r, oscillations L-C et intensité efficace, mobile à accélération −π²/4·x. Calculs associés : études de fonctions, limites, aires/volume par intégrale, valeur moyenne, suite (uₙ) convergente (Ex. 28 D).
- ⛔ EXCLU (non traité dans ce manuel) : y″ − ω²y = 0 (solutions exponentielles/hyperboliques) ; y″ + ay′ + by = 0 général et équation caractéristique ; seconds membres généraux de l'ordre 2 hors réduction d'ordre z = y′ (et, par rapport à la référence, y″ + y′ = cos⁴ x : Ex. 19 absent) ; variation de la constante formalisée ; systèmes différentiels ; sous tangente (PR1 absent).

### Lecture

- **Pages lues par l'OCR** (texte intégral) : 165 à 182, soit 18 pages.
- **Pages lues sur l'image (110 dpi)** : 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182 — **18 pages sur 18** (toute page du chapitre porte formule, encadré, tableau ou figure) ; tous les encadrés ci-dessus ont été vérifiés sur l'image de leur page.
- **Écarts OCR/image constatés** : p.166 « t = —10 » (OCR) pour t = 10, et « e^−t » d'exposant perdu pour 9000e^(−0,4t) ; p.167 « y₀e^(a(x−x₀)) » dégradé et figure de l'Activité 3 illisible à l'OCR (courbes C_g, C_t, C_f, C_h lues sur l'image) ; p.169 f(x) = e^(−2x) + 3 rendu « e ?* » et théorème/démonstration en fractions b/a illisibles à l'OCR ; p.170 Activité 2.b « f(0) = −1/2 » : fraction perdue, et Activité 3 « Ra′ + aq » pour R q′(t) + (1/C) q(t) ; p.171 f(0) = √3/2, f′(0) = 3/2 perdus ; p.172 f(π/2) = −1 et f′(π/2) = 2 perdus ; p.173 f(π/12), f(π/3), f(2π/3) perdus ; p.174 tableau de variation et courbe illisibles à l'OCR ; p.176 Ex. 3.b « xy » (OCR) pour « πy », Ex. 8 « 2 » pour y² ; p.177 Ex. 13 « r = 1000 » (OCR) pour « r = 100 Ω », Ex. 14.2 « y(x) » pour « y(π) », Ex. 18 « y″ + y″ = 0 » pour y‴ + y″ = 0, Ex. 17.4 intervalle [0, π/8] perdu ; p.178 Ex. 20 et Ex. 21 formules (e^(−t/RC)) dégradées ; p.179 Ex. 24 « e^(−0.75x) » illisible, figure (courbe C, tangente T) non chiffrable à l'OCR ; p.180 Ex. 28 (fractions, e^(−2x), ln) très dégradé ; p.181 Ex. 31 f(x) = 3e^(x/5)/(e^(x/5) + 2) et g′ = g/5 − g²/15 dégradés, Ex. 32 exposants 10⁻³ et 10⁻² perdus ; p.182 bornes des intégrales perdues.
- Aucun doute restant sur les encadrés. Seule incertitude : l'exposant de l'Activité 2.2 p.166 (« −0,4t » lu sur l'image, divergent de la référence) et les données chiffrées des figures (Activité 3 p.167, Ex. 24 p.179), non lisibles avec certitude à 110 dpi.

## 2.11 Chapitre 11 — Nombres complexes (manuel 222434, p.5–21)

**Page de garde (p.5)** — « Chapitre 1 — Nombres complexes » (numérotation interne du tome 2 ; c'est le
chapitre 11 dans la numérotation content). Encart historique : « À partir de la deuxième moitié du XVIIe,
les géomètres utilisent de façon de plus en plus courante le symbole -1 [sic, sans radical] dans les identités algébriques et
les recherches relatives aux résolutions d'équations. En 1740, Euler donne la formule cos x =
½(e^(x√−1) + e^(−x√−1)), et en 1748, la formule e^(x√−1) = cos x + √−1 sin x, x est réel. Dontzig [sic,
pour Dantzig] dit de cette dernière qu'elle contient "les symboles les plus importants, union mystérieuse
dans laquelle l'arithmétique est représentée par 0 et 1, l'algèbre par −1 [sic, imprimé « -1 » sans radical
dans la phrase], la géométrie par p [sic, pour π] et l'analyse par e". (Dalmedico et al, Une histoire des
mathématiques, 1986). Cauchy ne se ralliera explicitement à la représentation géométrique des nombres
complexes qu'en 1874, […] et s'est convaincu que la "notion de quantité géométrique […] comprendra comme
cas particulier la notion de quantité algébrique. » (guillemet final non fermé dans l'imprimé).

**Plan** : **I. Rappels et compléments** (I.1 Définition et opérations ; I.2 Affixe d'un point, affixe d'un
vecteur ; I.3 Module ; I.4 Argument d'un nombre complexe non nul ; I.5 Écriture trigonométrique ; I.6
Propriétés d'un argument) — **II. Écriture exponentielle d'un nombre complexe** — **III. Nombres complexes
et trigonométrie** — cinq **exercices résolus** — **QCM / VRAI-FAUX** (p.18) — **Exercices et problèmes**
(p.19–21, 27 exercices). Le chapitre s'arrête p.21 ; p.22 ouvre le « Chapitre 2 — Équations à coefficients
complexes » (hors de ce chapitre). Numérotation des activités : continue 1–14 en partie I (p.6–13), puis
repart à 1 en II (1–6, p.13–16) et en III (1–4, p.16–17).

### Cours — Activités

**I.1 Définition et opérations sur les nombres complexes** (p.6)

- **Activité 1** (p.6) : écriture cartésienne de (2 − 2i)(1 + i)² ; (−√2 − i√3)(√2 + i√3) ; (1 + i)⁴(1 − i)²⁰.
- **Activité 2** (p.6) : z = −1 + 2i et z′ = i. 1. écriture cartésienne de z² et z³, et de leurs conjugués.
  2. de zz′, (zz′)², (zz′)³, et de leurs conjugués. 3. de z/z′, (z/z′)², (z/z′)³, et de leurs conjugués.
  (Encart rose : « Soit z = a + ib, où a et b sont des réels. Le conjugué de z est le nombre complexe
  z̄ = a − ib. »)

**I.2 Affixe d'un point, affixe d'un vecteur** (p.7)

- **Activité 3** (p.7) : repère orthonormé direct (O, u⃗, v⃗). 1. placer A, B, C d'affixes i, 1 − 3i, 1 + 2i.
  2. affixes de leurs symétriques par rapport à l'axe des abscisses. 3. par rapport au point O. 4. par
  rapport à l'axe des ordonnées. 5. affixes des vecteurs OB⃗ − 2OC⃗ et −AB⃗ + (3/2)AC⃗. 6. affixe du centre de
  gravité du triangle ABC. (Encart rose : définitions affixe d'un point / d'un vecteur, linéarité.)
- **Exercice résolu 1** (énoncé p.7, solution p.8) : A, B d'affixes 2 − 2i et −1 + i. 1. montrer que O, A, B
  sont alignés. 2. déterminer l'ensemble des points M d'affixe z = k(2 − 2i), k ∈ ℝ. Solution : O, A, B
  alignés ssi OA⃗ et OB⃗ colinéaires, ssi ∃ k réel tel que Aff(OA⃗) = k Aff(OB⃗) ; ici Aff(OA⃗) = −2(−1 + i)
  = −2 Aff(OB⃗). 2. M ∈ D ssi Aff(OM⃗) = k Aff(OA⃗), ssi OM⃗ = kOA⃗ ; l'ensemble est la droite (OA).
- **Activité 4** (p.8) : A, B d'affixes 1 + 2i et i(1 + 2i). 1. placer A et B. 2. montrer que OA⃗ et OB⃗ sont
  orthogonaux. (Suivie, p.8–9, d'une Démonstration de la propriété d'orthogonalité, par aa′ + bb′ = 0.)
- **Exercice résolu 2** (énoncé + solution p.9) : déterminer l'ensemble E des points M d'affixe z tels que
  (z − i)/(z − 1) soit imaginaire. Solution : A d'affixe i, B d'affixe 1, z ≠ 1 ; (z − i)/(z − 1) imaginaire
  ssi AM⃗ ⊥ BM⃗ et M ≠ B ; E = cercle de diamètre [AB] privé du point B.

**I.3 Module d'un nombre complexe** (p.9)

- **Activité 5** (p.9) : A, B d'affixes z_A = 1 + i√3 et z_B = 1 − i√3. Calculer OA, OB et AB. (Encart rose :
  définition |z| = OM = √(a² + b²) ; |z_N − z_M| = MN.)
- **Activité 6** (p.9) : z = 2 − i et z′ = −3 + 4i. 1. écritures cartésiennes de z + z′ ; zz′ ; z/z′ ; z⁴ ;
  (z̄z′)². 2. calculer les modules de z + z′ ; zz′ ; z/z′ ; z⁴ ; (z̄z′)².
- **Activité 7** (p.10) : calculer les modules de (1 + i)⁵, (1 + i)¹¹/(1 − i)⁶ et (1 − i)⁵.
- **Exercice résolu 3** (énoncé + solution p.10) : déterminer l'ensemble des M d'affixe z tels que 1. |z − 1 + 2i| = 2 ;
  2. |z + 2 − i| = |z̄ − 2 + 2i|. Solution : 1. cercle de centre A(1 − 2i) et de rayon 2. 2. |z̄ − 2 + 2i| =
  |z − 2 − 2i| (un complexe et son conjugué ont même module) ; K(−2 + i), L(2 + 2i) ; KM = LM ; médiatrice de [KL].

**I.4 Argument d'un nombre complexe non nul** (p.10–11)

- **Activité 8** (p.10–11) : repère orthonormé. 1. placer A, B, C, D d'affixes z_A = −i ; z_B = 4 ; z_C = 2 + 2i ;
  z_D = −1 + i et déterminer, graphiquement, un argument de chacun. 2. A₁, B₁, C₁, D₁ symétriques par rapport
  à l'axe des abscisses : un argument de chacun de leurs affixes. 3. idem pour les symétriques par rapport
  à O. 4. idem par rapport à l'axe des ordonnées. (Encart rose : définition arg(z) = mesure de (u⃗, OM⃗).)
- **Activité 9** (p.11) : M ≠ O tel que (u⃗, OM⃗) ≡ θ [2π] ; M₁, M₂, M₃ symétriques de M par rapport à l'axe
  des abscisses, au point O, à l'axe des ordonnées. Déterminer (u⃗, OM₁⃗), (u⃗, OM₂⃗), (u⃗, OM₃⃗) en fonction de θ.

**I.5 Écriture trigonométrique** (p.12)

- **Activité 10** (p.12) : repère orthonormé direct. z = −2√3 + 2i. 1. écriture trigonométrique de z et placer
  le point d'affixe z. 2. en déduire l'écriture trigonométrique de z̄, −z, ½z et −(3/2)z, puis placer leurs
  points images. (Encart rose : écriture trigonométrique ; position de M sur le cercle de rayon |z|.)
- **Activité 11** (p.12) : z = 1 + 9i et z′ = 2 − 8i. Valeur approchée de leurs arguments à 10⁻² près.
  (Encart rose : cos θ = a/√(a²+b²) et sin θ = b/√(a²+b²).)
- **Activité 12** (p.12) : repère orthonormé direct. Écriture trigonométrique de z_A = 4, z_B = −1 + i√3,
  z_C = 1 − i√3.

**I.6 Propriétés d'un argument d'un nombre complexe non nul** (p.12–13)

- **Activité 13** (p.12) : z, z′ non nuls, z = |z|(cos θ + i sin θ), z′ = |z′|(cos θ′ + i sin θ′). 1. écritures
  trigonométriques de zz′, 1/z et z′/z. 2.a. montrer par récurrence, sur l'entier naturel n, que
  zⁿ = |z|ⁿ(cos(nθ) + i sin(nθ)) ; b. en déduire que pour tout entier naturel n,
  z⁻ⁿ = |z|⁻ⁿ(cos(−nθ) + i sin(−nθ)).
- **Activité 14** (p.13) : écriture trigonométrique de (1 + i)⁶ ; (1 − i)⁹·(√3 + i)⁵/(√3 − i)⁸ ;
  (2√3 − 2i)⁶(1 + i√3)³ (trois nombres ; le deuxième est un produit).

**II. Écriture exponentielle d'un nombre complexe** (p.13–16)

- **Activité 1** (p.13) : repère orthonormé direct. A, B, C d'affixes z_A = i, z_B = ½(√3 + i), z_C = (√2/2)(1 − i).
  1. écritures trigonométriques de z_A, z_B, z_C. 2. en déduire que A, B, C appartiennent au cercle
  trigonométrique. (Suivie de l'encadré « Notation » e^(iθ), p.13.)
- **Activité 2** (p.14) : z = e^(−iπ/3) et z′ = e^(i3π/2). 1. module et un argument de −z, z̄, zz′, 1/z, z/z′ et zⁿ
  (n ∈ ℤ). 2. écrire sous la forme e^(iθ) les nombres zz′, z̄, z/z′, zⁿ (n ∈ ℤ).
- **Exercice résolu 4** (énoncé p.14, solution p.15) : z = 1 + i + e^(iθ), θ ∈ [0, 2π[ ; E = ensemble des points M
  d'affixe z. 1. vérifier que B d'affixe z_B = 1 + 2i appartient à E. 2. déterminer E. Solution : i = e^(iπ/2),
  donc z_B = 1 + i + e^(iπ/2) ; A d'affixe z_A = 1 + i ; M ∈ E ssi z − z_A = e^(iθ), θ ∈ [0, 2π[, ssi AM = 1 ; E =
  cercle de centre A et de rayon 1 (figure).
- **Activité 3** (p.15) : repère orthonormé direct. 1. écriture trigonométrique de z₁ = 2i, z₂ = −3i, z₃ = −5/2,
  z₄ = √3(1 + i), z₅ = (−2√3 + 2i)/5. 2. écrire chacun sous la forme re^(iθ), r > 0.
- **Activité 4** (p.15) : z = √3 + i et z′ = −1 + i. Écriture exponentielle de z, z̄, z′, z̄′, zz′, 1/z, z⁵, z/z′ et z′².
- **Activité 5** (p.15) : 1. écrire sous forme exponentielle z = √3 − i et z′ = 1 + i. 2. en déduire l'écriture
  cartésienne de (1 + i)¹⁴/(√3 − i)⁸.
- **Activité 6** (p.16) : 1. vérifier que pour tout réel θ, 1 + e^(iθ) = (e^(−iθ/2) + e^(iθ/2)) e^(iθ/2). 2. écriture
  exponentielle de z = 1 + e^(i2π/5) et z = 1 + e^(i3π/5) [sic : même lettre z imprimée pour les deux nombres].

**III. Nombres complexes et trigonométrie** (p.16–17)

- **Activité 1** (p.16) : k entier. Montrer que pour tout réel x différent de (2k + 1)π/2, e^(2ix) = (1 + i tan x)/(1 − i tan x).
- **Activité 2** (p.16) : 1. avec la formule de Moivre et la formule du binôme de Newton, montrer que
  cos(3x) = cos³x − 3cos x sin²x et sin(3x) = 3cos²x sin x − sin³x. 2. exprimer cos(4x) et sin(4x) en fonction
  de puissances de cos x et de sin x.
- **Exercice résolu 5** (énoncé p.16, solution p.17) : linéariser sin⁵x, x ∈ ℝ. (Encart rose : définition de
  « linéariser ».) Solution : sin⁵x = (1/(2i)⁵)(e^(ix) − e^(−ix))⁵ ; binôme de Newton ; (e^(ix) − e^(−ix))⁵ =
  (e^(5ix) − e^(−5ix)) − 5(e^(3ix) − e^(−3ix)) + 10(e^(ix) − e^(−ix)) ; d'où sin⁵x = (1/16)(sin 5x − 5 sin 3x + 10 sin x).
- **Activité 3** (p.17) : linéariser cos³x, sin³x, où x est un réel.
- **Activité 4** (p.17) : linéariser sin²x · cos³x.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM, vérifiés sur l'image)

> **Théorème et définition (rappel)** (p.6) — « Il existe un ensemble appelé ensemble des nombres complexes,
> noté ℂ et vérifiant les propriétés ci-dessous. 1. L'ensemble ℂ contient l'ensemble ℝ des nombres réels.
> 2. Il existe un élément de ℂ, noté i, tel que i² = −1. 3. L'ensemble ℂ est muni d'une addition et d'une
> multiplication qui vérifient les mêmes propriétés que l'addition et la multiplication dans ℝ. 4. Tout
> élément z de ℂ s'écrit de façon unique sous la forme z = a + ib, où a et b sont des réels. »

> **Conséquences** (p.6) — « Soit z = a + ib et z′ = a′ + ib′, où a, a′, b et b′ sont des réels. • z = z′, si et
> seulement si, a = a′ et b = b′. • z = 0, si et seulement si, a = b = 0. • z est réel, si et seulement si, b = 0.
> • z est imaginaire, si et seulement si, a = 0. »

> **Encart (conjugué)** (p.6) — « Soit z = a + ib, où a et b sont des réels. Le conjugué de z est le nombre
> complexe z̄ = a − ib. »

> **Propriétés** (p.7) — « • Pour tous nombres complexes z et z′, (z + z′)‾ = z̄ + z̄′ ; (zz′)‾ = z̄ z̄′ ;
> (zⁿ)‾ = (z̄)ⁿ ; n ∈ ℕ*. • Pour tout nombre complexe z et tout nombre complexe non nul z′, (z/z′)‾ = z̄/z̄′ ;
> (1/z′ⁿ)‾ = 1/(z̄′)ⁿ, n ∈ ℤ. • z + z̄ = 2 Re(z) ; z − z̄ = 2i Im(z) ; zz̄ = (Re(z))² + (Im(z))².
> • z = z̄, si et seulement si, z est réel. • z = −z̄, si et seulement si, z est imaginaire. »

> **Encart (affixe)** (p.7) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). • L'affixe d'un
> point M(a, b) du plan est le nombre complexe z = a + ib noté Aff(M) ou z_M. On dit aussi que le point
> M(a, b) est l'image de z. • Soit w⃗ un vecteur et M et N deux points tels que w⃗ = MN⃗. Alors l'affixe du
> vecteur w⃗ est le nombre complexe noté Aff(w⃗) ou z_w⃗, vérifiant z_w⃗ = z_N − z_M. • Pour tous vecteurs w⃗ et
> w₁⃗ et tous réels α et β, Aff(αw⃗ + βw₁⃗) = αAff(w⃗) + βAff(w₁⃗). »

> **Propriété** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ ≠ 0⃗. Les vecteurs w⃗ et w₁⃗ sont colinéaires,
> si et seulement si, z_w⃗/z_w₁⃗ est réel. » (Suivie d'une Démonstration : w⃗ = kw₁⃗ ⇔ Aff(w⃗) = kAff(w₁⃗) ⇔
> Aff(w⃗)/Aff(w₁⃗) = k.)

> **Propriété** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ ≠ 0⃗. w⃗ et w₁⃗ sont orthogonaux, si et
> seulement si, z_w⃗/z_w₁⃗ est imaginaire. » (Suivie d'une Démonstration p.9.)

> **Encart (module)** (p.9) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). • Soit z = a + ib et
> M(a, b) le point d'affixe z. On appelle module de z le réel positif, noté |z|, défini par |z| = OM = √(a² + b²).
> • Pour tous points M et N d'affixes z_M et z_N, |z_N − z_M| = MN. »

> **Propriétés** (p.10) — « Soit deux nombres complexes z et z′. |z| = 0, si et seulement si, z = 0 ;
> |z + z′| ≤ |z| + |z′| ; |kz| = |k||z|, k ∈ ℝ. |zz′| = |z||z′| ; |z̄| = |z| ; |z|² = zz̄ ; |zⁿ| = |z|ⁿ, n ∈ ℕ*.
> |1/z| = 1/|z|, z ≠ 0 ; |z′/z| = |z′|/|z|, z ≠ 0 ; |1/zⁿ| = 1/|z|ⁿ, z ≠ 0 et n ∈ ℤ. »

> **Encart (argument)** (p.10) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Soit z un nombre
> complexe non nul et M son image. On appelle argument de z et on note arg(z) toute mesure de l'angle (u⃗, OM⃗). »

> **Propriétés** (p.11) — « Soit z un nombre complexe non nul et k un réel non nul. arg(z̄) ≡ −arg(z) [2π].
> arg(−z) ≡ π + arg(z) [2π]. Si k > 0 alors arg(kz) ≡ arg(z) [2π]. Si k < 0 alors arg(kz) ≡ π + arg(z) [2π]. »
> (trois figures : M(z), M′(z̄), M″(−z) ; k > 0 ; k < 0)

> **Encart (écriture trigonométrique)** (p.12) — « Soit z un nombre complexe non nul tel que arg(z) ≡ θ [2π].
> Alors z = |z|(cos θ + i sin θ). L'écriture précédente est appelée écriture trigonométrique de z. Si M est
> l'image de z dans le repère orthonormé direct (O, u⃗, v⃗) alors M appartient au cercle de centre O et de rayon
> |z| et à la demi droite [OB) telle que (u⃗, OB⃗) ≡ θ [2π]. »

> **Encart (cos, sin d'un argument)** (p.12) — « Soit un nombre complexe non nul z = a + ib, a et b des réels.
> arg(z) ≡ θ [2π], si et seulement si, cos θ = a/√(a² + b²) et sin θ = b/√(a² + b²). »

> **Propriétés** (p.13) — « Soit z et z′ deux nombres complexes non nuls. arg(zz′) ≡ arg(z) + arg(z′) [2π].
> arg(1/z) ≡ −arg(z) [2π] ; arg(z′/z) ≡ arg(z′) − arg(z) [2π]. arg(zⁿ) ≡ n arg(z) [2π], n ∈ ℕ ;
> arg(1/zⁿ) ≡ −n arg(z) [2π], n ∈ ℕ. »

> **Formule de Moivre (encadré)** (p.13) — « Soit un nombre complexe non nul z = |z|(cos θ + i sin θ). Pour tout
> entier n, zⁿ = |z|ⁿ(cos(nθ) + i sin(nθ)). La formule précédente est appelée formule de Moivre. »

> **Notation** (p.13) — « Pour tout réel θ, on note e^(iθ) le nombre complexe cos θ + i sin θ. » Puis (texte et
> figure, hors encadré bleu) : « Un point M appartient au cercle trigonométrique, si et seulement si, M a pour
> affixe z = e^(iθ), où θ ≡ (u⃗, OM⃗) [2π]. »

> **Conséquences** (p.14) — « • e^(i0) = 1, e^(iπ/2) = i, e^(−iπ/2) = −i, e^(iπ) = −1. • Pour tout réel θ et tout
> entier k, e^(iθ) = e^(i(θ+2kπ)). • Pour tout réel θ, |e^(iθ)| = 1 et (e^(iθ))‾ = e^(−iθ) et −e^(iθ) = e^(i(θ+π)). »

> **Propriétés** (p.14) — (phrase d'introduction : « Les propriétés ci-dessous découlent des propriétés de
> l'argument du produit, de l'inverse ou du quotient de deux nombres complexes non nuls. ») « Soit deux réels
> θ et θ′. e^(iθ)·e^(iθ′) = e^(i(θ+θ′)) ; 1/e^(iθ) = e^(−iθ) ; e^(iθ)/e^(iθ′) = e^(i(θ−θ′)) ; (e^(iθ))ⁿ = e^(inθ), n ∈ ℤ. »

> **Théorème et définition** (p.15) — « Tout nombre complexe non nul z, s'écrit sous la forme z = re^(iθ), où
> r = |z| et arg(z) ≡ θ [2π]. L'écriture z = re^(iθ) est appelée écriture exponentielle de z. »

> **Théorème** (p.16) — « Pour tout réel x et pour tout entier n, (cos x + i sin x)ⁿ = cos(nx) + i sin(nx).
> (Formule de Moivre). Pour tout réel x, cos x = (e^(ix) + e^(−ix))/2 et sin x = (e^(ix) − e^(−ix))/2i.
> (Formules d'Euler). » Suivi du texte : « Les formules de Moivre et d'Euler permettent d'établir un grand
> nombre de formules trigonométriques. Elles permettent aussi d'exprimer des puissances de cos x et sin x à
> l'aide de cos(nx) et sin(nx). »

> **Encart (linéariser)** (p.16) — « En transformant une expression contenant une puissance de cos x ou de
> sin x sous une forme qui ne contient aucun produit de fonctions circulaires, on dit qu'on a linéarisé
> l'expression donnée. »

Démonstrations imprimées : colinéarité (p.8) et orthogonalité (p.8–9) uniquement. Aucune « méthode »
encadrée dans ce chapitre (les méthodes sont dans les solutions des exercices résolus).

### QCM (p.18) — « Cocher la réponse exacte. »

Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Soit les points M(z) et M′(z′).

1. a. La distance MM′ est égale à (☐ |z − z′| / ☐ ||z| − |z′|| / ☐ |z + z′|). b. Si arg(z) ≡ arg(z′) [2π], alors
   (☐ O, M et M′ sont alignés / ☐ z = z′ / ☐ |z| = |z′|). c. Si arg(z) ≡ arg(iz′) [2π] et |z| = |z′| = 1, alors
   (☐ z = z′ / ☐ z = iz′ / ☐ z = −z′).
2. A, B, C d'affixes z_A, z_B, z_C tels que z_B − z_A = 4(z_C − z_A), alors (☐ ABC est isocèle / ☐ (AB) et (AC) sont
   perpendiculaires / ☐ A, B et C sont alignés).
3. z_B − z_A = 4i(z_C − z_A), alors (☐ ABC est isocèle / ☐ (AB) et (AC) sont perpendiculaires / ☐ (AB) et (AC)
   sont parallèles).

### Vrai ou faux (p.18) — « Répondre par vrai ou faux en justifiant la réponse. » (réponses non fournies)

1. Soit z₁ et z₂ deux nombres complexes non réels. Le conjugué de Z = z₁ + iz₂ est Z̄ = z₁ − iz₂.
2. Soit z un nombre complexe. Si z³ est réel alors nécessairement z est réel.
3. Soit z et z′ deux nombres complexes non nuls. Si |z| = |z′| alors nécessairement z = z′ ou z = −z′.

### Exercices et problèmes (p.19–21) — 27 exercices

(Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗) — en tête de p.19.)

**p.19**
- **1** : mettre sous forme algébrique 2i + 1/i − 1 ; (1 + i√3)/(√3 − i) ; ((1 + i)/(1 − i))² ; (1 − i)(2 + i)/(i − 2).
- **2** : conjugué de (3 − 2i)(5 + i)/(3i(7 + 2i)) ; ((i − 3)/(1 + i))² ;
  (2 − i)(3 + 2i)(2 + i)(3 − 2i).
- **3** : z₁ = [(11 + 13i)(11 − 13i) − (3 − 5i) − (3 + 5i)] / [(7 + 3i) + (7 − 3i)] ; z₂ = (3 − 7i)/(9 + 2i) ;
  z₃ = (3 + 7i)/(9 − 2i). Montrer, sans effectuer de calcul, que z₁ est réel, z₃ + z₂ est réel et z₃ − z₂ est
  imaginaire.
- **4** : déterminer et représenter l'ensemble des points M d'affixe z : 1. z = a + i(a + 1), a ∈ ℝ ;
  2. z = 2i sin(a/2), a ∈ [0, 2π[ ; 3. a(z − i) = i(z + 1), a ∈ ℝ\{0}.
- **5** : module de (1 + i)⁴ ; (2 − 3i)² ; (−2 + i)(1 − 3i)(1 − 4i) ; (1 − 5i)/(i + 2√3).
- **6** : 1. montrer que pour tout complexe z, |z| = 1 si et seulement si z̄ = 1/z. 2. en déduire que si
  |z₁| = |z₂| = 1 alors (z₁ + z₂)/(1 + z₁z₂) est réel.
- **7** : déterminer z pour que z, 1 − z et z² aient le même module.
- **8** : z = x + iy (x, y réels), z′ = z². 1. partie réelle et imaginaire de z′ en fonction de x, y.
  2. ensemble des M tels que z′ soit réel. 3. ensemble des M tels que z′ soit imaginaire (déterminer et
  représenter).
- **9** : A, B, C d'affixes 2 + i, −1 et 3 − 2i. 1. affixe du milieu I de [BC]. 2.a. calculer AB, AC, BC ; b. nature
  de ABC. 3.a. affixe du point D symétrique de A par rapport à I ; b. nature du quadrilatère ABDC.
- **10** : placer A, B, C, D d'affixes −2 + i, 4i, 7/2 + 2i, 3/2 − i ; nature du quadrilatère ABCD.
- **11** : 1. déterminer et représenter l'ensemble E des M tels que |z − 1 + 2i| = 3. 2. déterminer et
  représenter l'ensemble E des M tels que |iz + 1 − i|/|z + 2 + i| = 1.

**p.20**
- **12** : graphique (triangle OAB équilatéral, quadrillage) ; module et un argument des affixes z_A, z_B, z_C et z_D.
- **13** : graphique (cercle trigonométrique, 0,75, 1,5, points A…F) ; un argument des affixes z_A…z_F.
- **14** : forme trigonométrique de a. −8i ; (−1 + i)/√2 ; 3i + √3 ; −2,5 ; √2 − √6 i ; 5 + 5i. b. 3(1 + i√3)/(1 + i)² ;
  (1 + i)/(1 − i) ; ((1 + i√3)/(√3 + i))³ ; (1 − i)⁵(1 + i)³.
- **15** : z₁ = 1 + i, z₂ = √3 − i. 1. |z₁|, arg(z₁), |z₂|, arg(z₂). 2. forme algébrique et trigonométrique de z₁z₂.
  3. en déduire les valeurs exactes de cos π/12 et sin π/12.
- **16** : z₁ = −1 + i√3, z₂ = 1 + i. 1. |z₁|, arg(z₁), |z₂|, arg(z₂). 2. |z₁/z₂| et arg(z₁/z₂). 3. en déduire cos 5π/12 et
  sin 5π/12.
- **17** : forme algébrique de e^i ; e^(−iπ/4) ; e^(2iπ/3) ; e^(iπ)/4 ; 2ie^(iπ/6).
- **18** : forme exponentielle de 2√3 − 2i ; −5 − 5i ; −1 + i√3 ; (1 + i)/√2 ; cos π/5 − i sin π/5.
- **19** : 1. forme exponentielle de z = (1 + i√3)/(√3 + i). 2. en déduire la forme algébrique de z⁶.
- **20** : 1. forme exponentielle de −1 + i. 2. en déduire que (−1 + i)¹¹ = 32 + 32i.
- **21** : déterminer et construire l'ensemble des points M d'affixe z : 1. z = 2e^(iθ), θ ∈ [0, π] ; 2. z = −2e^(iθ),
  θ ∈ [0, π] ; 3. z = 2 + cos θ + i sin θ, θ ∈ [0, 2π[.

**p.21**
- **22** : θ ∈ ]0, π[. 1. montrer que 1 + e^(iθ) = 2cos(θ/2)e^(iθ/2) et 1 − e^(iθ) = −2i sin(θ/2)e^(iθ/2). 2. en
  déduire module et argument de 1 + e^(iθ) et 1 − e^(iθ).
- **23** : forme exponentielle de z : 1. cos θ − i sin θ, θ ∈ ℝ ; 2. sin θ + i cos θ, θ ∈ ℝ ; 3. −cos θ − i sin θ, θ ∈ ℝ ;
  4. 1 + i tan θ, θ ∈ [0, π/2[ ; 5. (e^(iθ) − e^(−iθ))/(e^(iθ) + e^(−iθ)), θ dans un intervalle symétrique privé de 0
  (intervalle : ]−π/2, π/2[\{0}, confirmé sur l'image).
- **24** : 𝒞 cercle trigonométrique de centre O ; M ∈ 𝒞 d'affixe t telle que (u⃗, OM⃗) ≡ α [2π], α ∈ [0, π/2] ;
  u = t³ et v = 2t. 1. écritures trigonométriques de u et v. w = 2t − t³ ; A, B, C d'affixes u, v, w. 2. placer A, B, C
  pour α = π/3. 3. réels α pour lesquels O, A, B sont alignés. 4. α ∈ ]0, π/2[ : a. nature de OABC ; b. α pour
  que OABC soit un rectangle.
- **25** : z = e^(i2θ) − i, θ ∈ [0, π/4[. 1. M et M′ images de z et z̄ ; affixe du point N pour que OMNM′ soit un
  losange. 2.a. montrer que z = 2cos(θ + π/4)e^(i(θ − π/4)) ; b. forme exponentielle de z/z̄ ; c. valeur de θ pour que
  OMNM′ soit un carré ; d. construire le carré OMNM′ pour la valeur trouvée.
- **26** : θ ∈ ]0, π/2[, 𝒞 cercle trigonométrique de centre O, M ∈ 𝒞 d'affixe z tel que arg(z) ≡ θ [2π]. 1. placer A et
  B d'affixes z_A = 1 + cos θ et z_B = −1 + i sin θ (lu sur l'image à 300 dpi). 2.a. montrer que le quadrilatère OAMB est un parallélogramme ; b. montrer qu'il existe une
  valeur de θ telle que OABM soit un losange [sic, ordre des lettres tel qu'imprimé, différent de la question a] ;
  c. valeur approchée de θ à 10⁻¹ près. 3. 𝒜(θ) aire du parallélogramme OAMB ; montrer que 𝒜(θ) est maximale
  lorsque θ = π/3.
- **27** : φ ∈ ]0, π[, z = ½(sin φ + i(1 − cos φ)). 1. module et argument de z en fonction de φ. 2. un module et un
  argument de z₁ = z − i et z₂ = z/(z − i). On considère les points M et N d'affixes z₁ et z₂ : 1. ensemble E
  décrit par M ; 2. ensemble F décrit par N ; 3. représenter E et F. [sic : la numérotation 1-2-3 repart à 1
  dans l'énoncé imprimé ; les questions « E, F, représenter » sont à lire comme 3, 4, 5.]

### Écart avec la référence (chapitre 10 de bac-math, manuel 222446, p.5–34)

**Ce que la référence enseigne et que ce manuel (222434) n'a PAS — à EXCLURE** :
- **I.7 Angles orientés et nombres complexes** : (u⃗, AB⃗) ≡ arg(z_B − z_A) et (AB⃗, CD⃗) ≡ arg((z_D − z_C)/(z_B − z_A))
  (théorème + conséquence) — absents ; donc aucun lieu « arg(z − a) ≡ θ » ni « arg((z − a)/(z − b)) ≡ θ »
  (demi-droite, arc de cercle) : ER 2 et ER 3 de la référence n'existent pas ici.
- **III. Équation zⁿ = a** : racines nièmes de l'unité, de j = e^(2iπ/3), racines nièmes d'un complexe, polygone
  régulier, racines carrées par méthode algébrique (système x² − y², 2xy) — absents (le Chapitre 2 du manuel,
  p.22, « Équations à coefficients complexes », les traite : hors de ce chapitre).
- **IV. Équation du second degré** az² + bz + c = 0 (discriminant, δ, somme/produit) et **V. équations de degré
  ≥ 3** (factorisation P(z) = (z − z₀)g(z)) — absents (renvoyés au Chapitre 2).
- Transformations z ↦ z′ (z′ = 1/z, z′ = z² − 4z, homographies) comme technique : absentes sauf z′ = z² (ex. 8) ;
  sommes Σcos kθ / Σsin kθ par exponentielle — absentes ; factorisation 1 − e^(iθ) = −2i sin(θ/2)e^(iθ/2) hors
  d'un exercice (ex. 22, à démontrer) ; pas d'encadré « formule de factorisation ».
- Exercices résolus : 5 au lieu de 7 (pas d'ER racines 5ᵉ de l'unité ni d'ER degré 3) ; exercices et problèmes :
  27 au lieu de 39 ; QCM de 3 questions (la question 3 de la référence sur z² − 2z + 2 = 0 est remplacée par une
  question sur z_B − z_A = 4i(z_C − z_A)) ; Vrai/Faux de 3 énoncés au lieu de 6.
- Propriétés d'argument : ici arg(zⁿ) ≡ n arg(z) avec **n ∈ ℕ** (et 1/zⁿ, n ∈ ℕ) ; la référence a n ∈ ℤ ; la formule
  de Moivre est ici dite « pour tout entier n » (inclut ℤ). Ne pas écrire n ∈ ℤ pour arg(zⁿ).
- Pas de justification d'e^(iθ) comme notation différente : même statut (notation pour cos θ + i sin θ), pas de
  fonction exponentielle complexe.

**Ce que ce manuel a en PLUS (ou de différent)** :
- Une **activité préliminaire sur le conjugué** (Activité 2 p.6 : z = −1 + 2i, z′ = i, puissances et quotient) ;
  l'encadré rose du conjugué avant les propriétés.
- Les **Activités d'orthogonalité** (Activité 4 p.8) et la **démonstration** de la propriété d'orthogonalité avec
  aa′ + bb′ = 0.
- **ER 4 : z = 1 + i + e^(iθ), θ ∈ [0, 2π[** (cercle entier de centre A(1 + i), rayon 1) au lieu de θ ∈ [0, π].
- **Activité 1 de III** : e^(2ix) = (1 + i tan x)/(1 − i tan x) (x ≠ (2k + 1)π/2) ; **Activité 2 de III** : cos 3x,
  sin 3x par Moivre + binôme, puis cos 4x, sin 4x (« exprimer en fonction de puissances de cos x et sin x »).
- Exercices à thème **géométrique de configuration** (ex. 9, 10, 12, 13), calcul de **cos π/12, sin π/12,
  cos 5π/12, sin 5π/12** (ex. 15, 16), **ensembles z = ae^(iθ) sur demi-cercle** (ex. 21), **formes exponentielles
  paramétriques** (ex. 22–23), problèmes OAMB / OMNM′ avec aire maximale (ex. 24–27).

### Bornes de scope (chapitre 11, Bac Sciences expérimentales)

- ✅ INCLUS : **définition de ℂ** (i² = −1, forme algébrique unique, égalité, réel/imaginaire pur, conjugué et
  ses propriétés, Re/Im) ; **affixe** d'un point et d'un vecteur, linéarité, **colinéarité** (z_w⃗/z_w₁⃗ réel) et
  **orthogonalité** (z_w⃗/z_w₁⃗ imaginaire) avec leurs démonstrations ; **module** et propriétés (inégalité
  triangulaire, |zz′|, |z/z′|, |zⁿ|, |z|² = zz̄) ; **|z_N − z_M| = MN** ; lieux : droite (OA), cercle de diamètre [AB]
  privé de B, cercle de centre A et rayon r, médiatrice de [KL] (équation |z − a| = r, |z − a| = |z − b|, rapport
  de modules égal à 1) ; **argument** : définition, arg(z̄), arg(−z), arg(kz), (k ≷ 0) ; **écriture trigonométrique**
  et détermination de θ par cos θ = a/√(a²+b²), sin θ = b/√(a²+b²) (valeur approchée à 10⁻² près ou valeurs
  exactes par angles remarquables) ; **arg(zz′), arg(1/z), arg(z′/z), arg(zⁿ) n ∈ ℕ, formule de Moivre** ;
  **notation e^(iθ)**, conséquences, règles de calcul, **écriture exponentielle** re^(iθ), passage
  algébrique ↔ trigonométrique ↔ exponentielle, calcul de puissances/quotients par l'exponentielle ;
  factorisation par l'angle moitié sur 1 + e^(iθ) (et 1 − e^(iθ) en ex. 22) ; **trigonométrie** : formules
  de Moivre et d'Euler, **expression de cos nx, sin nx** (n = 3, 4) par binôme, **linéarisation** (cos³x, sin³x,
  sin²x·cos³x, sin⁵x) ; exp. de e^(2ix) = (1 + i tan x)/(1 − i tan x) ; valeurs exactes de cos/sin de π/12, 5π/12
  par produit de complexes ; problèmes de configuration (nature d'un triangle ou quadrilatère par affixes et
  modules, parallélogramme/losange/carré/rectangle, alignement, aire maximale).
- ⛔ EXCLU : **angles orientés** (u⃗, AB⃗) ≡ arg(z_B − z_A), (AB⃗, CD⃗) ≡ arg((z_D − z_C)/(z_B − z_A)) ;
  ensembles « arg(z − a) ≡ θ », « arg((z − a)/(z − b)) ≡ θ » (demi-droite, arc de cercle) ; **racines nièmes**
  de l'unité et d'un complexe, racines carrées par système algébrique, **équation du second degré** à
  coefficients complexes (discriminant, δ, somme/produit), **équations de degré ≥ 3** et factorisation
  P(z) = (z − z₀)g(z), polygones réguliers inscrits ; transformations z ↦ z′ classifiées et **similitudes** ;
  homographies ; sommes Σcos kθ, Σsin kθ ; fonction racine carrée complexe ou exponentielle complexe comme
  fonction ; arg(zⁿ) pour n négatif énoncé comme propriété (seule la formule de Moivre « n entier » le couvre) ;
  généralités sur les polynômes.

### Lecture

- **Pages lues par l'OCR** (texte, p.5–21) : 17 pages, toutes ; l'OCR rend la prose mais dégrade formules,
  exposants, vecteurs, barres de conjugaison, fractions et figures.
- **Pages lues sur l'image** (110 dpi, 17 pages) : **p.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  21** — soit 17 pages sur 17 (toute page à formule, encadré ou tableau, donc toutes).
- **Sondage et écarts OCR/image constatés** : p.6 — l'OCR donne « (−2)(4i) ; (−V2−i05)(V2 V5) ; Gi) (1) » pour
  l'Activité 1, l'image « (2 − 2i)(1 + i)² ; (−√2 − i√3)(√2 + i√3) ; (1 + i)⁴(1 − i)²⁰ » ; l'OCR lit z′ = « i » avec
  un énoncé à double colonne mélangé (Activité 2 + encart conjugué), l'image donne la mise en page correcte.
  p.7 — barres de conjugaison perdues dans l'OCR (z + z′ = z̄ + z̄′ illisible). p.10 — OCR « ble: Fe: Hz: »
  pour les modules de quotients ; l'image donne |1/z| = 1/|z|, |z′/z| = |z′|/|z|, |1/zⁿ| = 1/|z|ⁿ. p.12 — OCR
  « z=−243+2i » pour z = −2√3 + 2i. p.13 — OCR « n∈N; … −nars » pour arg(zⁿ) ; l'image confirme n ∈ ℕ.
  p.16 — OCR « 1+e/° » pour 1 + e^(iθ). p.19–21 — OCR trop dégradé pour les exercices (ex. 2 : « 3i(7+2i) »
  et ex. 26 ne sont pas fiables sur l'OCR) ; tous les énoncés de cette fiche sont tirés de l'image.
- **Doutes signalés** : ex. 26 (lettres OAMB / OABM, telles qu'imprimées), ex. 27 (numérotation des sous-questions) ; ER 1 : l'encart
  « Exercice résolu 1 » est ici sans lien avec la référence (ER 1 de la référence = zⁿ pour z = 1 − i).

## 2.12 Chapitre 12 — Équations à coefficients complexes (manuel 222434, p.22–33)

**Page de garde (p.22)** — Titre : « Equations à coefficients complexes ». Numéro de chapitre imprimé « 2 » [sic : différent du rang 12 de la section]. Citation (Wikipedia) : « Les nombres complexes ont de riches propriétés algébriques et analytiques. Le théorème fondamental de l'algèbre établit que tout polynôme non nul possède autant de racines complexes (comptées avec leur multiplicité) que son degré. Les nombres complexes furent inventés au 16ème siècle par les mathématiciens Cardan, Bombelli et Tartaglia comme intermédiaires de calcul pour trouver des solutions aux équations polynomiales du troisième degré. Il semblerait que ce soit Héron d'Alexandrie qui ait inventé le nombre impossible. »
Plan (bandeaux, pas de sommaire imprimé) : I. Équation zⁿ = a, n ≥ 2, a ∈ ℂ* (p.23–26) ; II. Résolution dans ℂ de l'équation az² + bz + c = 0, a ≠ 0 (p.26–28) ; III. Exemples d'équations de degré supérieur ou égal à 3 (p.28–29) ; QCM — VRAI-FAUX (p.30) ; Exercices et problèmes (p.31–33, 24 exercices). Pas d'activités préliminaires, pas de résumé, pas de rubrique informatique ni d'aperçu historique. Convention des exercices (p.31) : plan muni d'un repère orthonormé direct (O, u⃗, v⃗).

### Activités et exercices résolus (une ligne chacun)

**I. Équation zⁿ = a**
- **Act. 1** (p.23) : 1) résoudre dans ℂ (E) : u² = −3/4 ; 2) en déduire les solutions de (E′) : (z + 1/2)² = −3/4 ; z₁ (partie imaginaire positive) et z₂ (négative) sous forme exponentielle ; 3) a) montrer z³ − 1 = (z − 1)[(z + 1/2)² + 3/4] ; b) en déduire les solutions de (E″) : z³ = 1.
- **Act. 2** (p.24) : j = (−1 + i√3)/2 ; a) j racine cubique de l'unité ; b) j³ = 1, j² = j̄ et 1 + j + j² = 0 ; c) pour tout n ∈ ℕ : j^{3n} = 1, j^{3n+1} = j, j^{3n+2} = j̄.
- **Exercice résolu 1** (p.24) : 1) résoudre (E) : z⁶ = 1 (z₀ = 1, z₁ = e^{i2π/6}, z₂ = e^{i4π/6}, z₃ = e^{i6π/6} = −1, z₄ = e^{i8π/6}, z₅ = e^{i10π/6}) ; 2) en déduire que la somme des solutions est nulle (z_k = z₁^k, z₁ ≠ 1, 1 + z₁ + … + z₁⁵ = (z₁⁶ − 1)/(z₁ − 1) = 0).
- **Act. 3** (p.24) : résoudre dans ℂ z⁸ = 1.
- **Act. 4** (p.24) : (E) : z³ = 8i ; 1) z solution ⇔ z/(2e^{iπ/6}) racine cubique de l'unité ; 2) (E) a exactement trois solutions ; vérifier z_k = 2e^{i(π/6 + 2kπ/3)}, k ∈ {0, 1, 2}.
- **Act. 5** (p.26) : racines carrées, puis racines quatrièmes de u = −4i.
- **Act. 6** (p.26) : z = √(2 − √2) + i√(2 + √2) ; 1) module et argument de z² ; 2) en déduire une écriture trigonométrique de z.

**II. az² + bz + c = 0**
- **Act. 1** (p.26, racines carrées par méthode algébrique) : d = 3 − 4i ; on pose z = x + iy ; 1) z² = d équivaut à { x² − y² = 3 ; 2xy = −4 ; x² + y² = 5 } ; 2) vérifier que les couples solutions sont (2, −1) et (−2, 1) ; 3) conclure.
- **Act. 2** (p.26) : racines carrées de −8 + 6i et de 1 − 2√2 i.
- **Act. 3** (p.26) : (E) : z² + 2iz − 7/4 − i = 0 ; 1) (E) ⇔ (z + i)² = (3 + 4i)/4 ; 2) vérifier ((2 + i)/2)² = (3 + 4i)/4 ; 3) en déduire les solutions de (E).
- **Act. 4** (p.27) : a, b, c ∈ ℂ, a ≠ 0, (E) : az² + bz + c = 0 ; 1) (E) ⇔ (z + b/(2a))² = (b² − 4ac)/(4a²) ; 2) Δ = b² − 4ac : a) si Δ = 0, (E) a une unique solution à déterminer ; b) si Δ ≠ 0, Δ a deux racines carrées opposées δ et −δ ; montrer (E) ⇔ (z + (b − δ)/(2a))(z + (b + δ)/(2a)) = 0 ; en déduire les solutions. (Conduit au théorème p.27.)
- **Act. 5** (p.27) : résoudre dans ℂ : a. z² − (1 − i)z + 2 − 2i = 0 ; b. 1 + z + z² = 0 ; c. 1 − z + z² = 0.
- **Act. 6** (p.28) : déterminer z₁ et z₂ vérifiant { z₁ + z₂ = 1 + 2i ; z₁z₂ = −1 + i }.

**III. Degré ≥ 3**
- **Act. 1** (p.28) : a₁,…,a_n ∈ ℂ, a_n ≠ 0, n ≥ 2, f(z) = a_n zⁿ + a_{n−1} z^{n−1} + … + a₁z + a₀, (E) : f(z) = 0 ; 1) si z₀ est solution de (E), alors f(z) = 0 ⇔ a_n zⁿ + … + a₁z = a_n z₀ⁿ + … + a₁z₀ ; 2) en déduire (E) ⇔ (z − z₀)g(z) = 0, g(z) = a_n z^{n−1} + b_{n−2} z^{n−2} + … + b₀.
- **Exercice résolu 2** (p.28–29) : (E) : z³ + (1 − 4i)z² − (7 + 3i)z + 6i − 2 = 0 ; 1) (E) admet une solution imaginaire : z₀ = iy, système { −y² + 3y − 2 = 0 (∗) ; −y³ + 4y² − 7y + 6 = 0 (∗∗) } ; (∗) a pour racines 1 et 2, seul 2 vérifie (∗∗), donc z₀ = 2i ; 2) factorisation (z − 2i)(z² + bz + c), identification : b = 1 − 2i, c = −3 − i ; (E₁) : z² + (1 − 2i)z − 3 − i = 0 de solutions z₁ = −2 + i et z₂ = 1 + i ; S = {2i, −2 + i, 1 + i}. [coquille imprimée p.29 : « (z² + (1 − 2i)z + −3 − i) »]
- **Act. 2** (p.29) : f(z) = z³ + (2 + 2i)z² + (2 + i)z + 3 + i, z ∈ ℂ ; 1) vérifier f(i) = 0 ; 2) en déduire les solutions de f(z) = 0.

### QCM — Vrai-Faux (p.30)
- **QCM (5 questions, 3 propositions, « Cocher la réponse exacte »)** : 1. z² + z + 1 = 0 a deux solutions opposées / conjuguées / confondues ; 2. z² − 2z + 2 = 0 a pour solutions z₁ = 1 − i et z₂ = 1 + i / z₁ = 2i et z₂ = −i / z₁ = 1 − i et z₂ = 2 + i ; 3. z³ − z² + z − 1 = 0 admet une seule / deux / trois solutions réelles ; 4. z⁴ = −1 admet une solution réelle / une solution imaginaire / quatre solutions distinctes ; 5. √2 + i√2 est une racine carrée de 4i / −4i / 2√2 i.
- **Vrai-Faux (6, « en justifiant »)** : 1. z² = −3 n'admet pas de solution dans ℂ ; 2. z⁴ = z² équivaut à z² = 1 ; 3. 0 est l'unique solution dans ℂ de z⁴ + z² = 0 ; 4. une équation du second degré dans ℂ admet toujours deux racines opposées ; 5. z, a non nuls : z⁴ = a⁴ ⇔ z = a ou z = −a ; 6. z³ = i ⇒ z imaginaire.
- (Corrigés non fournis.)

### Exercices et problèmes (p.31–33) — 24 exercices
- **Ex. 1** (p.31) : racines cubiques de 4√2(i + 1).
- **Ex. 2** (p.31) : racines quatrièmes de 8√2(−1 − i).
- **Ex. 3** (p.31) : racines cinquièmes de 32i.
- **Ex. 4** (p.31) : racines sixièmes de 32(i − √3).
- **Ex. 5** (p.31) : résoudre dans ℂ : z² = 2i ; z² + 4 = 0 ; z² = −5 + 12i ; z² = e^{iπ/3} ; z² + i = 0 ; (1 − iz)² = −1 ; (2z − 1)² − (i − z)² = 0 [dernier : « (i − z)² » lu sur l'image, l'OCR donnait « (1 − z)² »].
- **Ex. 6** (p.31) : résoudre : 1. z² + z + 2 = 0 ; 2. z² − 2iz − 1 = 0 ; 3. z² − (4 + 2i)z + 2 + 4i = 0 ; 4. (2 + i)z² + (1 − 7i)z − 5 = 0.
- **Ex. 7** (p.31) : α ∈ ℂ* ; 1) développer (α − i)² ; 2) résoudre (E) : z² − α(α + i)z + iα³ = 0 ; 3) r = |α|, θ = arg α : module et argument de chaque solution en fonction de r et θ.
- **Ex. 8** (p.31) : 1) a) résoudre (E) : z² − (3 + i)z + 2(1 + i) = 0 ; b) solutions sous forme algébrique et trigonométrique ; 2) résoudre (E′) : X⁴ − (3 + i)X² + 2(1 + i) = 0.
- **Ex. 9** (p.31) : (E) : z⁴ + az² + b + 12i = 0, a, b réels ; 1) déterminer a et b sachant que √2(1 + i) est solution ; 2) résoudre l'équation obtenue.
- **Ex. 10** (p.31) : 1) résoudre (E) : z² + (1 + i)z + i = 0 ; 2) en déduire les solutions de : a. iz² + (1 − i)z − 1 = 0 ; b. z⁴ + (1 + i)z² + i = 0.
- **Ex. 11** (p.31) : résoudre : 1. z⁴ + 6z² + 25 = 0 ; 2. z⁴ + 4z² − 77 = 0 ; 3. z⁵ = z̄.
- **Ex. 12** (p.31) : (E) : z³ − 8z² + 24z − 32 = 0 ; 1) vérifier z₀ = 4 ; 2) résoudre (E) ; 3) forme exponentielle des solutions.
- **Ex. 13** (p.31) : (E) : z³ − (3 + 4i)z² − 4(1 − 3i)z + 12 = 0 ; 1) (E) admet une racine réelle à déterminer ; 2) résoudre (E).
- **Ex. 14** (p.32) : (E) : z³ = 2 + 11i ; 1) vérifier z₀ = 2 + i ; 2) résoudre (E).
- **Ex. 15** (p.32) : 1) α = (1 − i√3)/2 et β = (3 + i√3)/2 sous forme exponentielle ; 2) θ ∈ ]0, π[ : a) résoudre z² − 2z + 1 − e^{2iθ} = 0, z₁ de partie imaginaire négative, z₂ l'autre ; b) z₁, z₂ sous forme trigonométrique ; c) θ tel que z₁ = α et z₂ = β.
- **Ex. 16** (p.32) : résoudre (E) : z² + (1 − 2i)z − 2i = 0 ; θ réel, E_θ : z² + (1 − 2e^{iθ})z − 2e^{iθ} = 0, z₁ solution indépendante de θ, z₂ l'autre ; A(z₁), M(z₂), I milieu de [AM], z_I son affixe ; 1) z_I + 0,5 = e^{iθ} ; 2) ensemble des I quand θ ∈ [0, 2π[ ; 3) valeurs de θ ∈ [0, 2π[ pour lesquelles O, A, I sont alignés.
- **Ex. 17** (p.32) : a ∈ ℂ*, équation z² − 2z + 1 + a² = 0 ; 1) la résoudre ; 2) A(1 + ia), B(1 − ia), a = a₁ + ia₂ : a) O, A, B alignés ⇔ a₁ = 0 ; b) OA⃗ ⊥ OB⃗ ⇔ |a| = 1 ; 3) a = e^{iα}, α ∈ ]−π/2, π/2[ : a) 1 + e^{ix} = 2cos(x/2) e^{ix/2} et 1 − e^{ix} = −2i sin(x/2) e^{ix/2} ; b) formes exponentielles de 1 + ia et 1 − ia ; c) α pour que OAB soit rectangle isocèle en O.
- **Ex. 18** (p.32) : w = z + 4/z (z ≠ 0), θ réel ; 1) résoudre z + 4/z = 4cos θ ; 2) solutions sous forme exponentielle ; 3) ensemble E des points M(z) tels que w soit réel, à déterminer et construire ; 4) A(2e^{iθ}), B(4cos θ), C(2e^{−iθ}), θ ∈ ]0, π/2[ : a) placer pour θ = π/6 ; b) A, B, C ∈ E ; c) OABC est un losange ; d) θ pour que OABC soit un carré.
- **Ex. 19** (p.33) : θ ∈ [0, 2π[ ; 1) a) (e^{iθ} − i)² = −1 + e^{2iθ} − 2ie^{iθ} ; b) résoudre z² − 2iz + 2ie^{iθ} − e^{2iθ} = 0 ; 2) M₁(e^{iθ}), M₂(2i − e^{iθ}) : a) ensemble 𝒞₁ décrit par M₁, à construire ; b) affixe du milieu I de [M₁M₂] ; c) ensemble 𝒞₂ décrit par M₂, à construire ; 3) a) (M₁M₂)² = 8(1 − sin θ) ; b) valeur de θ pour laquelle M₁M₂ est maximale.
- **Ex. 20** (p.33) : I. résoudre z² + i√3 z − i = 0. II. θ ∈ [0, π/2] (vérifié à 300 dpi), (E) : z² + (2i sin θ)z − 2i cos θ = 0 ; 1) a) (cos θ + i)² = −sin²θ + 2i cos θ ; b) résoudre (E) ; 2) A(a = i), B(b = cos θ + (1 − sin θ)i), C(c = −cos θ − (1 + sin θ)i) : a) θ pour que A, B, C soient alignés ; b) θ pour que B et C appartiennent à un cercle de centre O, et rayon de ce cercle.
- **Ex. 21** (p.33) : 1) résoudre (E) : z² − 2(1 + i)z + 1/2 + i = 0 ; 2) θ ∈ [0, π/2], E_θ : 2z² − (1 + 2cos θ + 2i)z + cos θ + i = 0 : a) E_θ admet une racine réelle à calculer, l'autre racine en fonction de θ ; A(1/2), M(cos θ + i) ; b) ensemble E des M quand θ ∈ [0, π/2], à déterminer et construire ; c) AM en fonction de θ, valeur de θ pour laquelle AM est minimale.
- **Ex. 22** (p.33) : résoudre dans ℂ : z⁴ = 1 et ((z − i)/(z + i))⁴ = 1.
- **Ex. 23** (p.33) : (E) : z³ = 4√2(−1 + i) ; 1) solutions sous forme trigonométrique ; 2) en utilisant les racines cubiques de l'unité, les écrire sous forme algébrique ; 3) en déduire cos(π/12) et sin(π/12).
- **Ex. 24** (p.33) : résoudre dans ℂ z⁶ = −1 ; mettre le polynôme x⁶ + 1 sous la forme d'un produit de trois polynômes du second degré à coefficients réels.

### Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Théorème et définition — racines nièmes de l'unité** (p.23) — « Pour tout entier naturel n ≥ 2, l'équation zⁿ = 1 admet dans ℂ n solutions distinctes définies par z_k = e^{i2kπ/n}, l'entier k appartenant à {0, 1, ..., (n − 1)}. Les solutions de l'équation zⁿ = 1 sont appelées racines nièmes de l'unité. »

> **Conséquence** (p.23) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Lorsque n ≥ 3, les points images des racines nièmes de l'unité sont les sommets d'un polygone régulier inscrit dans le cercle trigonométrique. » (Figure : racines sixièmes de l'unité, hexagone M₀(e^{i0}), M₁(e^{iπ/3}), M₂(e^{i2π/3}), M₃(e^{iπ}), M₄(e^{i4π/3}), M₅(e^{i5π/3}).)

> **Théorème et définition — racines nièmes d'un nombre complexe** (p.25) — « Soit a un nombre complexe non nul d'argument θ et un entier naturel n ≥ 2. L'équation zⁿ = a admet dans ℂ, n solutions distinctes définies par z_k = r e^{i(θ/n + 2kπ/n)}, k ∈ {0, 1, ..., n − 1}, où r est le réel strictement positif tel que rⁿ = |a|. Ces solutions sont appelées les racines nièmes du nombre complexe a. »
> Démonstration (p.25, hors encadré) : a = |a|e^{iθ} ; r > 0 avec rⁿ = |a| donne a = rⁿ(e^{iθ/n})ⁿ ; zⁿ = a ⇔ (z/(re^{iθ/n}))ⁿ = 1 ⇔ z/(re^{iθ/n}) racine nième de l'unité.

> **Conséquences** (p.25) — « • Tout nombre complexe non nul admet deux racines carrées opposées. • Le plan complexe est muni d'un repère orthonormé direct (O, u⃗, v⃗). Lorsque n ≥ 3, les points images des racines nièmes d'un nombre complexe non nul sont les sommets d'un polygone régulier inscrit dans le cercle de centre O et de rayon r tel que rⁿ = |a|. » (Figure : points images des solutions de z⁶ = |a|e^{iθ}, M_k(re^{i(θ + 2kπ)/6}), k = 0…5.)

> **Théorème — équation du second degré** (p.27) — « Soit a, b et c des nombres complexes tels que a ≠ 0. L'équation az² + bz + c = 0, admet dans ℂ, deux solutions (éventuellement confondues) définies par z₁ = (−b + δ)/(2a) et z₂ = (−b − δ)/(2a), où δ est une racine carrée du discriminant Δ = b² − 4ac. »

> **Conséquences** (p.27) — « Si z₁ et z₂ sont les solutions de az² + bz + c = 0, a ≠ 0, alors az² + bz + c = a(z − z₁)(z − z₂), z₁ + z₂ = −b/a et z₁z₂ = c/a. »

> **Théorème — factorisation par une racine** (p.28) — « Soit a₁, a₂,..., a_n des nombres complexes tels que a_n ≠ 0, n ≥ 2. Soit P(z) = a_n zⁿ + a_{n−1} z^{n−1} + ... + a₁z + a₀. Si z₀ est un zéro de P, alors P(z) = (z − z₀)g(z), où g(z) est de la forme a_n z^{n−1} + b_{n−2} z^{n−2} + ... + b₀, avec b₀, b₁,..., b_{n−2} complexes. »

Aucun autre encadré (pas de définition de « racine carrée », pas d'encadré sur la forme algébrique, pas de résumé).

### Écart avec la référence (ch. 11 bac-techniques, manuel 222451, et ch. 10 bac-math)
**Enseigné par la référence, ABSENT de ce manuel (à exclure)** :
- activités préliminaires (équations dans ℝ, z̄ dans ℂ, z² = −2i…) ; définition encadrée « racine carrée » ; encadré « racines carrées par la forme algébrique » avec le système à trois lignes comme énoncé général (ici seulement l'Act. 1 p.26 sur d = 3 − 4i, sans théorème général, et sans le rappel x² + y² = √(a² + b²) : la 3ᵉ ligne n'est donnée que numériquement, x² + y² = 5) ;
- racines carrées « par la forme exponentielle » en encadré dédié (ici seulement le cas n = 2 du théorème p.25 et l'Act. 5/6 p.26) ;
- définition encadrée de l'équation du second degré, cas Δ ≠ 0 / Δ = 0 distingués dans l'énoncé (ici : « deux solutions, éventuellement confondues », la racine double n'est pas nommée), discriminant réduit Δ′ (b = 2b′), théorème « coefficients réels » (Δ > 0, = 0, < 0, solutions conjuguées) et ses activités, encadré « somme et produit donnés → z² − Sz + P = 0 » (ici seulement demandé en Act. 6 p.28, sans encadré) ;
- définition « racine nième de Z » pour Z quelconque en notation ⁿ√r (ici r défini par rⁿ = |a|) ;
- exposition en forme exponentielle z = r e^{iθ} avec k ∈ ℤ et périodicité z_k = z_{k+n} ; exemple de la racine cubique de 8 ;
- rubrique « Avec l'ordinateur » (hexagone régulier, z⁶ = 64i), Résumé du cours, Aperçu historique (Cardan, Ferrari, Galois…) ;
- exercices d'annales « D'après Bac Tunisien 1999/2000 », équation z⁶ − 4z³ + 8 = 0, équations de degré 4 type 4z⁴ + 4cos θ(1 + cos θ)z² + … ; Act. 3 du ch. 11 (P(z) = Q₁(z)Q₂(z)) ; Act. 4 (somme/produit avec racine évidente sans calculer Δ) ; relation Δ = λ² dans l'Act. 1.

**Présent dans ce manuel en plus** : Exercice résolu 1 (racines sixièmes de l'unité, somme nulle) et Exercice résolu 2 (racine imaginaire pure par système { Re = 0 ; Im = 0 }, puis factorisation par identification) ; encadré « racines nièmes de l'unité » traité AVANT les racines nièmes de a (démonstration par ramener à l'unité) ; j = (−1 + i√3)/2 et j^{3n+k} ; Act. 3 z⁸ = 1 ; Act. 4 z³ = 8i par division par 2e^{iπ/6} ; théorème de factorisation d'un polynôme par un zéro (encadré, degré n quelconque) ; QCM (5) et Vrai-Faux (6) ; exercices : z⁵ = z̄ (Ex. 11-3), ((z − i)/(z + i))⁴ = 1 (Ex. 22), cos et sin de π/12 par les racines cubiques (Ex. 23), factorisation de x⁶ + 1 en trois trinômes réels (Ex. 24), équation en w = z + 4/z avec lieu E et losange/carré OABC (Ex. 18), équations paramétrées par θ et lieux (Ex. 15, 16, 19, 21), cas général z² − 2z + 1 + a² = 0 avec alignement/orthogonalité (Ex. 17). Écart de numérotation : 24 exercices (réf. 23) ; aucun corrigé dans les deux.

### Bornes de scope
- ✅ INCLUS : racines nièmes de l'unité (zₖ = e^{i2kπ/n}, polygone régulier inscrit dans le cercle trigonométrique) ; j et ses puissances ; racines nièmes d'un complexe non nul (rⁿ = |a|, zₖ = r e^{i(θ/n + 2kπ/n)}, polygone régulier de centre O et de rayon r) ; racines carrées (méthode algébrique avec x² − y², 2xy, x² + y² = |d| ; méthode exponentielle) ; équation az² + bz + c = 0 dans ℂ par le discriminant et une racine carrée δ ; factorisation a(z − z₁)(z − z₂) ; somme et produit des racines ; résolution du système { z₁ + z₂ ; z₁z₂ } ; équations de degré ≥ 3 par racine évidente ou imaginaire pure, factorisation (z − z₀)g(z) et identification des coefficients ; équations bicarrées en z² (Ex. 8-2, 10-2b, 11) ; équations paramétrées par θ avec forme exponentielle/trigonométrique des solutions ; lieux géométriques des points images (cercles, droites), alignement, losange, carré, rectangle isocèle ; z⁵ = z̄ ; z⁶ = −1 et factorisation de x⁶ + 1 en trinômes réels.
- ⛔ EXCLU : formules de Cardan / Ferrari ; théorème fondamental de l'algèbre (seulement cité en page de garde) ; discriminant réduit ; encadré « coefficients réels » (cas Δ < 0 du réel traité seulement par les activités/QCM 1–2) ; racine « double » nommée ; relations coefficients-racines pour le degré ≥ 3 ; équations de degré ≥ 5 hors racines nièmes ; usage de logiciel ; démonstration des racines nièmes autrement que par ramener à l'unité ; notation ⁿ√ ; QCM et Vrai-Faux sont des exercices à transcrire seulement en missions (corrigés non fournis, à résoudre).

### Lecture
- **Pages lues par l'OCR (texte)** : 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 (12/12).
- **Pages lues sur l'image (110 dpi)** : 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 — soit **12 pages sur 12** (sondage total, toutes les pages portent formules ou encadrés).
- **Écarts OCR / image constatés** : p.23 — « z'=a, n>2, a∈C" » pour « zⁿ = a, n ≥ 2, a ∈ ℂ* », exposants et fractions écrasés (« 2kπ ») ; p.24 — « j?=j » pour « j² = j̄ » (barre de conjugué perdue), « j³n+2 = j̄ » sans barre ; z_k en « e 6 » sans indice d'argument ; p.25 — exposants i(θ/n + 2kπ/n) illisibles (« e" 1/ »), « r° » pour rⁿ ; p.26 — « √ » perdue dans Act. 6 (z = √(2 − √2) + i√(2 + √2)) ; système à trois lignes (x² + y² = 5) conservé ; « (2+i)/2 ² = (3+4i)/4 » dégradé ; p.27 — δ lu « ô / ù / à / 5 » ; formules −b ± δ sur 2a écrasées ; p.28 — indices et « bₙ₋₂ » dégradés, (∗)/(∗∗) lus « (*), (++) » ; p.29 — « z_k » et ensemble S correctement lus mais coquille imprimée « + −3 − i » à noter ; p.30 — z³ − z² + z − 1 lu « 2-7?+7-1 », « √2 + i√2 » lu « 2v2i » ; p.31 — Ex. 5 dernier terme « (1 − z)² » (OCR) contre « (i − z)² » (image), Ex. 11-3 barre de z̄ perdue (« z⁵ = z »), Ex. 4 « 32(i − √3) » lu « 32(i 3) » ; p.32 — Ex. 14 « z³ = 2#11i » pour z³ = 2 + 11i, Ex. 15 α, β sans fractions, Ex. 17 3a exposants i·x/2 perdus ; p.33 — Ex. 19 « e^{iθ} » lu « ei® », Ex. 22 (z−i)/(z+i) sous exposant 4 perdu, Ex. 24 « x⁶ + 1 » lu « x6+1 ».
- **Doutes à signaler** : numéro de chapitre imprimé « 2 » (≠ 12) ; figure p.25 : sommet M₅ lisible, libellé M₅(re^((iθ+10π)/6)), coquille d'écriture imprimée (« iθ + 2kπ » sur 6, sans parenthèse autour de θ + 2kπ) ; Ex. 5 dernier terme (« (i − z)² » retenu).

## 2.13 Chapitre 13 — Produit scalaire — produit vectoriel dans l'espace (manuel 222434, p.34–47)

**Page de garde (p.34)** — Numérotation propre du manuel : « Chapitre **3** » (13ᵉ de la fiche). Titre imprimé : « Produit scalaire — Produit vectoriel dans l'espace » (p.35 : bandeau « Chapitre 3 »). La p.34 est une page d'ouverture historique, texte seul : « Le produit scalaire apparaît assez tard dans l'histoire des mathématiques. On en trouve trace chez Hamilton en 1843 lorsqu'il crée le corps des quaternions. Peano le définit ensuite associé à un calcul d'aire ou de déterminant. Roberto Marcolongo et Cesare Burali-Forti le définissent à l'aide du cosinus d'un angle et lui donne le nom de produit intérieur ou produit scalaire. […] Sa qualité de forme bilinéaire symétrique sera ensuite exploitée en algèbre et, de propriété, deviendra définition. La définition utilisée actuellement du produit vectoriel est apparu en 1881 dans un manuel d'analyse vectorielle écrit par Josiah Willard Gibbs pour ses étudiants en physique. Les travaux de Hermann Grassmann et William Hamilton sont à l'origine du produit vectoriel défini par Gibbs. » (M-J. Crowe, *A history of vector analysis*, 1994). Pas de sommaire imprimé, pas de page « Résumé » ni « Avec l'ordinateur » ni « Aperçu historique » séparés.

**Plan du chapitre (d'après les intertitres)** : I. Rappels (I.1 Déterminants ; I.2 Produit scalaire dans l'espace) → II. Produit vectoriel dans l'espace (II.1 Orientation de l'espace et d'un plan, avec les intertitres « Orientation de l'espace » et « Orientation d'un plan de l'espace » ; II.2 Produit vectoriel, dont l'intertitre p.40 « Expression analytique du produit vectoriel dans une base orthonormée directe » ; II.3 Aires et volumes) → QCM — Vrai-Faux (p.45) → Exercices et problèmes (p.46–47, 19 exercices). Aucune activité préliminaire séparée : le bloc « I. Rappels » (p.35–36) en tient lieu. Convention de l'énoncé des exercices (p.46) : « Dans tous les exercices, l'espace est muni d'un repère orthonormé direct (O, i⃗, j⃗, k⃗). »

### Activités de « Rappels » (p.35–36) — 5 activités (intitulées « Activité 1 » à « Activité 5 » dans le manuel ; numérotation reprise à 1 en II.1)

- **Rappels 1** (p.35) : cube ABCDEFGH d'arête 1, repère (A, AB⃗, AD⃗, AE⃗), base 𝓑 = (AB⃗, AD⃗, AE⃗). Coordonnées des sommets ; calculer det_𝓑(AB⃗, AC⃗, AH⃗), det_𝓑(AD⃗, AF⃗, AG⃗), det_𝓑(AB⃗, AD⃗, AC⃗).
- **Rappels 2** (p.35) : repère (O, u⃗, v⃗, w⃗) ; A(1,2,0), B(0,−1,1), C(−1,0,2), D(0,1,0), E(1,2,−2). 1) A, B, C, D coplanaires ? 2) B, C, D, E coplanaires ?
- **Rappels 3** (p.35) : cube ABCDEFGH d'arête a. 1) Exprimer en fonction de a : AF⃗.AB⃗, AF⃗.DC⃗, AF⃗.DG⃗, AF⃗.DH⃗, AF⃗.DE⃗. 2) Exprimer en fonction de a les distances AC, AF, DH, DF.
- **Rappels 4** (p.36) : tétraèdre ABCD, triangles ABC, ABD, ACD rectangles et isocèles en A, AB = AC = AD = 1. 1) Montrer que (A, AB⃗, AC⃗, AD⃗) est orthonormé. 2) Coordonnées du centre de gravité P du triangle ABC. 3) G centre de gravité du tétraèdre (GA⃗ + GB⃗ + GC⃗ + GD⃗ = 0⃗) : coordonnées. 4) Montrer que DG⃗ = (3/4) DP⃗ (fraction lue sur image).
- **Rappels 5** (p.36) : cube ABCDEFGH d'arête 1 ; I, J milieux de [FB] et [CD] ; K pied de la hauteur issue de A dans le triangle ABH ; utiliser un repère orthonormé adéquat. 1) Calculer BE⃗.IJ⃗. 2) a) Calculer KA⃗.KC⃗ ; b) en déduire la mesure en radian de l'angle AKC.

### Activités du cours (p.37–44) — 15 activités + 3 exercices résolus

- **Orientation** (p.37) : pas d'activité ; exposé (voir encadrés « Orientation »).
- **II.1 Activité 1** (p.38) : repère direct (O, i⃗, j⃗, k⃗). Parmi (i⃗,k⃗,j⃗), (j⃗,k⃗,i⃗), (i⃗,−j⃗,k⃗), (−i⃗,j⃗,−k⃗), (k⃗,i⃗,−j⃗), (−i⃗,−k⃗,−j⃗) : bases directes / indirectes ?
- **Exercice résolu 1** (p.38) : cube ABCDEFGH, repère orthonormé direct (A, AB⃗, AD⃗, AE⃗). Direct ou indirecte : (AE⃗,AD⃗,AB⃗) ; (EF⃗,HD⃗,FG⃗) ; (CG⃗,DC⃗,BC⃗). Solution : (AE⃗,AD⃗,AB⃗) indirecte (permutation de AB⃗ et AE⃗) ; (EF⃗,HD⃗,FG⃗) = (AB⃗, −AE⃗, AD⃗) directe ; (CG⃗,DC⃗,BC⃗) = (AE⃗, AB⃗, AD⃗) directe — attention : la solution imprimée écrit « (CG⃗, BC⃗, DC⃗) » à la dernière ligne alors que l'énoncé donne (CG⃗, DC⃗, BC⃗) : incohérence du manuel, à ne pas reproduire.
- **II.2 Exercice résolu 2** (p.39) : espace orienté direct, cube ABCDEFGH d'arête 1. Déterminer AB⃗∧AD⃗, AB⃗∧FG⃗, EF⃗∧EF⃗, EF⃗∧GH⃗. Réponses : AE⃗ ; AE⃗ ; 0⃗ ; 0⃗ (colinéaires).
- **II.2 Activité 2** (p.40) : A, B, C non alignés, espace orienté : ensemble des points M tels que AB⃗∧CM⃗ = 0⃗.
- **II.2 Activité 3** (p.40) : A, B, C, D quatre points : montrer AB⃗∧AC⃗ + AC⃗∧AD⃗ + AD⃗∧AB⃗ = BC⃗∧BD⃗.
- **II.2 Activité 4** (p.40) : A ≠ B, I milieu de [AB] : ensemble des points M tels que (MA⃗ − MB⃗) ∧ (MA⃗ + MB⃗) = 0⃗.
- **II.2 Activité 5** (p.40) : repère orthonormé direct ; A(−1,2,1), B(1,−6,−1), C(2,2,2), I(0,1,−1). Déterminer AB⃗∧AC⃗ ; AI⃗∧(AC⃗ + AI⃗) ; 2AI⃗∧(−3BC⃗).
- **II.2 Activité 6** (p.41) : repère orthonormé direct ; A(1,0,−1), B(1,−2,1), C(0,−1,2), D(3,1,0). 1) AB⃗∧AC⃗ ; 2) valeur approchée à 0,1 rad près de l'angle géométrique BAC ; 3) montrer (AD) ⊥ plan (ABC).
- **II.2 Activité 7 — distance d'un point à une droite** (p.41) : u⃗ ≠ 0⃗, A point, D la droite (A, u⃗), M ∉ D, H projeté orthogonal de M sur D. 1) Montrer MA⃗∧u⃗ = MH⃗∧u⃗ ; 2) en déduire MH = ‖MA⃗∧u⃗‖/‖u⃗‖.
- **II.2 Activité 8** (p.41) : tétraèdre ABCD, ABC, ABD, ACD rectangles, AB = AC = AD = 1 ; repère orthonormé direct (A, AB⃗, AC⃗, AD⃗) ; I ∈ (BD) avec BI⃗ = (1/3)BD⃗ ; K ∈ (AC) avec AK⃗ = (1/4)AC⃗ (fractions lues sur image). Distance de B à la droite (IK).
- **II.3 Activité 9** (p.42) : repère orthonormé direct ; montrer (u⃗∧v⃗).w⃗ = (v⃗∧w⃗).u⃗ = (w⃗∧u⃗).v⃗ = det(u⃗, v⃗, w⃗).
- **II.3 Activité 10** (p.42) : ABCD parallélogramme. 1) Aire = ‖AB⃗∧AD⃗‖ ; 2) aire du triangle ABD.
- **II.3 Activité 11** (p.42) : cube ABCDEFGH de centre O, repère R = (A, AB⃗, AD⃗, AE⃗) direct ; I, J, K, L centres des faces ABFE, BCGF, CDHG, ADHE. 1) AB⃗∧AD⃗ ; 2) IJKL parallélogramme de centre O ; 3) a) IJ⃗∧IL⃗ ; b) aire de IJKL ; 4) volume de la pyramide AIJKL.
- **II.3 Activité 12** (p.43) : repère orthonormé direct ; A(1,0,0), B(0,3,0), C(−1,3,0), D(2,2,2), E(3,2,2), F(2,5,2), G(1,5,2). 1) OABCDEFG est un parallélépipède ; 2) son volume.
- **II.3 Activité 13** (p.43) : espace orienté direct, tétraèdre ABCD, H projeté orthogonal de A sur (BCD). 1) (BC⃗∧BD⃗).BA⃗ = (BC⃗∧BD⃗).HA⃗ ; 2) |(BC⃗∧BD⃗).BA⃗| = ‖BC⃗∧BD⃗‖.‖HA⃗‖ ; 3) volume du tétraèdre = (1/6)|(BC⃗∧BD⃗).BA⃗|.
- **Exercice résolu 3** (p.43–44) : espace orienté direct, cube ABCDEFGH d'arête a, M milieu de [BF]. 1) Volume du tétraèdre MEBG ; 2) volume du solide S = cube privé du tétraèdre. Solution : repère orthonormé direct (A, (1/a)AB⃗, (1/a)AD⃗, (1/a)AE⃗) ; B(a,0,0), E(0,0,a), M(a,0,a/2), G(a,a,a) ; (1/6)|det(BE⃗, BG⃗, BM⃗)| = (1/12)a³ ; volume de S = (11/12)a³.
- **II.3 Activité 14** (p.44) : repère orthonormé direct (O, OI⃗, OJ⃗, OK⃗) ; R(1,1,0), M(1,1,1), N(0,1,1), L(1,0,1). 1) OIRJKLMN est un cube ; 2) A milieu de [IL], B défini par KB⃗ = (2/3)KN⃗ : a) coordonnées de A et B ; b) u⃗ = OA⃗∧OB⃗ ; c) aire du triangle OAB ; 3) volume du tétraèdre OABK. (I(1,0,0), J(0,1,0), K(0,0,1) par définition du repère ; OIRJ face inférieure, KLMN face supérieure : énoncé cohérent, vérifié sur l'image)
- **II.3 Activité 15** (p.44) : cube ABCDEFGH ; I, J, K, L, M, N, S milieux de [AB], [AD], [DH], [HG], [FG], [FB], [EH]. Volume de la pyramide SIJKLMN.

### QCM — Vrai-Faux (p.45)

- **QCM 1** : v⃗ = −2u⃗ et ‖v⃗‖ = 2 ; u⃗.v⃗ vaut ? (−2 ; 2 ; 4).
- **QCM 2** : A, B, C non alignés ; AB⃗∧AC⃗ est-il normal au plan ABC / directeur du plan ABC / directeur à la droite (BC) ?
- **QCM 3** : ABCD parallélogramme : (AB⃗∧AD⃗ = BA⃗∧BC⃗) ; (‖AB⃗∧AD⃗‖ = ‖BA⃗∧BC⃗‖) ; (‖AB⃗∧AD⃗‖ = (1/2)‖AB⃗∧AC⃗‖).
- **QCM 4** (cube ABCDEFGH d'arête 1) : a) AB⃗∧AC⃗ ∈ {AB⃗∧AD⃗ ; AC⃗∧DC⃗ ; √2 AE⃗} ; b) AC⃗∧EG⃗ ∈ {0⃗ ; BD⃗ ; BF⃗} ; c) AC⃗.FH⃗ ∈ {2 ; 0 ; √2} ; d) volume du tétraèdre FBEG ∈ {1/6 ; 1/3 ; 1/2}.
- **Vrai-Faux 1** : A, B, C, D non coplanaires ; si AB⃗.AD⃗ = AC⃗.AD⃗ = 0 alors (AD) ⊥ (ABC).
- **Vrai-Faux 2** : pour u⃗, v⃗ non colinéaires, la famille {u⃗, v⃗, u⃗∧v⃗} est liée.
- **Vrai-Faux 3** (u⃗, v⃗, w⃗ trois vecteurs) : a) si u⃗∧v⃗ = v⃗ alors v⃗ = 0⃗ ; b) si u⃗.v⃗ = u⃗.w⃗ alors v⃗ = w⃗ ; c) si u⃗∧v⃗ = u⃗∧w⃗ alors v⃗ = w⃗.

### Exercices et problèmes (p.46–47) — 19 exercices (repère orthonormé direct sauf mention)

- **1** (p.46) : cube ABCDEFGH d'arête 1, repère orthonormé adéquat : AG⃗.FH⃗ ; AG⃗.HC⃗ ; EG⃗.GB⃗ ; AB⃗.HB⃗.
- **2** (p.46) : tétraèdre régulier ABCD de côté 1. 1) AB⃗.AD⃗ et AB⃗.AC⃗ ; 2) AB⃗.CD⃗ ; 3) deux arêtes opposées sont orthogonales.
- **3** (p.46) : le repère proposé est-il orthogonal ? a) (O, j⃗+k⃗, k⃗−j⃗, i⃗) ; b) (O, i⃗−j⃗, j⃗−k⃗, k⃗−i⃗).
- **4** (p.46) : triangle ABC. 1) en écrivant BC⃗ = BA⃗ + AC⃗, montrer BC⃗∧BA⃗ = AB⃗∧AC⃗ ; 2) CA⃗∧CB⃗ = AB⃗∧AC⃗ ; 3) en déduire AB/sin Ĉ = AC/sin B̂ = BC/sin Â.
- **5** (p.46) : calculer u⃗∧v⃗ : a) u⃗ = j⃗ − 2k⃗, v⃗ = i⃗ + j⃗ − k⃗ ; b) u⃗ = i⃗ − 2j⃗, v⃗ = i⃗ + k⃗ ; c) u⃗ = i⃗ + (2/3)j⃗ + (1/2)k⃗ et v⃗ = (1/3)i⃗ − (4/9)j⃗ + (1/2)k⃗ (zoom 300 dpi).
- **6** (p.46) : calculer j⃗∧k⃗ ; k⃗∧i⃗ ; i⃗∧(−j⃗) ; 2j⃗∧(−3k⃗).
- **7** (p.46) : u⃗ = 2i⃗ + j⃗ + k⃗, w⃗ = 3i⃗ − 4j⃗ − 2k⃗. 1) u⃗ ⊥ w⃗ ; 2) trouver un vecteur v⃗ tel que u⃗∧v⃗ = w⃗ ; trouver tous les v⃗ ; 3) trouver v⃗ tel que u⃗∧v⃗ = w⃗ et u⃗.v⃗ = 1.
- **8** (p.46) : ‖u⃗‖ = 1, ‖v⃗‖ = 4, u⃗.v⃗ = 2 ; w⃗ = 2u⃗∧v⃗ − 3v⃗. Calculer u⃗.w⃗, v⃗.w⃗ et ‖w⃗‖.
- **9** (p.46) : u⃗, v⃗ unitaires orthogonaux ; w⃗ tel que u⃗ = w⃗ + w⃗∧v⃗. 1) w⃗ ⊥ v⃗ et ‖w⃗‖ = (1/2)√2 ; 2) w⃗ = (1/2)u⃗ − (1/2)u⃗∧v⃗.
- **10** (p.46) : vecteur non nul w⃗ orthogonal à u⃗ et v⃗ : a) u⃗(1,2,3), v⃗(−2,3,1) ; b) u⃗(2,1,−1), v⃗(0,−1,3) ; c) u⃗(1+√2, −√2, 1−√2), v⃗(−1, 2−√2, 3−2√2).
- **11** (p.46) : u⃗(1,−1,0), v⃗(0,1,−1), w⃗(−1,0,1) : composantes de (u⃗∧v⃗)∧w⃗ et u⃗∧(v⃗∧w⃗) ; que remarque-t-on ?
- **12** (p.47) : A(1,1,1), B(2,1,0), C(−1,2,2), D(3,0,0), E(−4,3,4). 1) AB⃗∧AC⃗ et AD⃗∧AE⃗ colinéaires ; 2) en déduire A, B, C, D, E coplanaires.
- **13** (p.47) : distance de A à la droite (BC) : A(1,1,1), B(−1,0,1), C(0,0,1) ; A(−1,2,0), B(−1,5,0), C(−3,7,−3) ; A(1,−1,2), B(1,0,1), C(0,1,2).
- **14** (p.47) : droite D : x = 1−2t, y = 3+2t, z = −1−t (t ∈ ℝ) ; A(0,3,−2). 1) a) distance de A à un point M de D ; b) valeur de t minimisant cette distance ; c) coordonnées du projeté orthogonal de A sur D.
- **15** (p.47) : A(0,0,3), B(1,1,0), C(3,0,0), D(0,3,0). 1) non coplanaires ; 2) volume du tétraèdre ABCD ; 3) ACD équilatéral ; H projeté orthogonal de B sur (ACD) : calculer BH.
- **16** (p.47) : cube ABCDEFGH de centre O, d'arête 1 ; I milieu de [AB], J et K centres des faces ABFE et ABCD. 1) O, I, J, K coplanaires ; 2) nature du quadrilatère OKIJ ; 3) volume de la pyramide BIJOK (l'OCR lit « BIOK » : l'image donne « BIJOK »).
- **17** (p.47) : cube d'arête 1 ; AI⃗ = (1/3)AD⃗, BJ⃗ = (1/3)BC⃗, HL⃗ = (1/3)HE⃗, GK⃗ = (1/3)GF⃗. 1) ABKLIJGH est un parallélépipède ; 2) repère (A, AB⃗, AD⃗, AE⃗) : a) composantes de AB⃗, AI⃗, AL⃗ ; b) volume de ABKLIJGH.
- **18** (p.47) : cube ABCDEFGH, repère (D, DC⃗, DH⃗, DA⃗) orthonormé direct ; K centre du carré ADHE, J milieu de [BG]. 1) un représentant de FE⃗∧FG⃗, DC⃗∧CB⃗, DB⃗∧DC⃗ ; 2) comparer DB⃗∧AH⃗ et CE⃗ ; 3) un représentant de AB⃗∧AJ⃗.
- **19** (p.47) : cube ABCDEFGH, repère (A, AB⃗, AD⃗, AE⃗) orthonormé direct ; I milieu de [EF], K centre du carré ADHE. 1) a) BK⃗ = IG⃗∧IA⃗ ; b) aire du triangle IGA ; 2) volume du tétraèdre ABIG.

### Encadrés — VERBATIM (vérifiés sur l'image de leur page)

> **Déterminant dans une base** (p.35) — « Soit 𝓑 une base de l'espace. Soit u⃗(a, b, c), v⃗(a', b', c') et w⃗(a'', b'', c'') trois vecteurs de l'espace. Le déterminant de (u⃗, v⃗, w⃗) dans la base 𝓑 est le réel a(b'c'' − c'b'') − b(a'c'' − c'a'') + c(a'b'' − b'a''). »

> **Coplanarité par déterminant** (p.35) — « Soit 𝓑 une base de l'espace. Les points A, B, C et D sont coplanaires, si et seulement si, le déterminant de (AB⃗, AC⃗, AD⃗) dans la base 𝓑 est nul. »

> **Produit scalaire — définition** (p.35) — « Soit A, B et C des points de l'espace. Le produit scalaire des vecteurs AB⃗ et AC⃗ est le réel défini par : AB⃗ . AC⃗ = 0, si AB⃗ = 0⃗ ou AC⃗ = 0⃗. AB⃗ . AC⃗ = AB.AC.cos BÂC, si AB⃗ et AC⃗ sont non nuls. AB⃗ . AB⃗ = ‖AB⃗‖² = AB². »

> **Propriétés (Rappel)** (p.36) — « Pour tous vecteurs u⃗, v⃗ et w⃗ de l'espace et tous réels α et β : u⃗.v⃗ = v⃗.u⃗ ; u⃗.(v⃗ + w⃗) = u⃗.v⃗ + u⃗.w⃗ ; (αu⃗).v⃗ = u⃗.(αv⃗) = α(u⃗.v⃗) ; (αu⃗).(βv⃗) = αβ(u⃗.v⃗). »

> **Repère orthonormé** (p.36) — « On dit que le repère (O, i⃗, j⃗, k⃗) est orthonormé si, ‖i⃗‖ = ‖j⃗‖ = ‖k⃗‖ = 1 et i⃗.j⃗ = i⃗.k⃗ = j⃗.k⃗ = 0. »

> **Expression analytique du produit scalaire** (p.36) — « Soit (O, i⃗, j⃗, k⃗) un repère orthonormé de l'espace. Pour tous vecteurs u⃗(x, y, z) et v⃗(x', y', z'), u⃗.v⃗ = xx' + yy' + zz' et ‖u⃗‖ = √(x² + y² + z²). Pour tous points M(x, y, z) et M'(x', y', z'), MM' = √((x − x')² + (y − y')² + (z − z')²). »

> **Orientation de l'espace** (p.37, texte courant, non encadré) — « Soit (O, i⃗, j⃗, k⃗) un repère de l'espace. Considérons les points de l'espace I, J et K tels que OI⃗ = i⃗, OJ⃗ = j⃗ et OK⃗ = k⃗. Un observateur d'Ampère pour ce repère est un personnage placé le long de (OK), les pieds en O et qui regarde dans la direction de (OI). Le plan (OIK) partage l'espace en deux demi-espaces, l'un à gauche de l'observateur et l'autre est à sa droite. • Si (OJ) est dans le demi-espace placé à gauche de l'observateur, on dit que le repère est direct. • Si (OJ) est dans le demi-espace placé à droite de l'observateur, on dit que le repère est indirect. Orienter l'espace c'est choisir l'un de ces repères. On dit que l'espace est orienté dans le sens direct s'il est muni d'un repère direct. On dit que l'espace est orienté dans le sens indirect s'il est muni d'un repère indirect. Nous admettrons qu'étant donné une base (i⃗, j⃗, k⃗), le repère (O, i⃗, j⃗, k⃗) a toujours la même orientation quelque soit le point O de l'espace. • On dit que la base (i⃗, j⃗, k⃗) est directe, dans le cas où le repère (O, i⃗, j⃗, k⃗) est direct. • On dit que la base (i⃗, j⃗, k⃗) est indirecte, dans le cas où le repère (O, i⃗, j⃗, k⃗) est indirect. • Chaque permutation de deux vecteurs d'une base change l'orientation de cette base. • Chaque permutation circulaire des trois vecteurs conserve l'orientation de la base. • En remplaçant un vecteur d'une base par son opposé, on change l'orientation de cette base. » (figures « repère direct » / « repère indirect »)

> **Orientation d'un plan de l'espace** (p.38, texte courant, non encadré) — « Soit P un plan de l'espace orienté et O un point de P. On considère la perpendiculaire Δ à P en O, un point C de Δ distinct de O, deux points A et B de P tels que O, A et B ne soient pas alignés. • Le repère cartésien (O, OA⃗, OB⃗) de P est dit direct si (O, OA⃗, OB⃗, OC⃗) est un repère cartésien direct de l'espace. • Le repère cartésien (O, OA⃗, OB⃗) de P est dit indirect si (O, OA⃗, OB⃗, OC⃗) est un repère cartésien indirect de l'espace. »

> **Théorème (existence de k⃗)** (p.39) — « Soit P un plan. Pour toute base (i⃗, j⃗) de P et tout réel d > 0, il existe un unique vecteur k⃗ vérifiant ‖k⃗‖ = d, k⃗.i⃗ = k⃗.j⃗ = 0 et la base (i⃗, j⃗, k⃗) est directe. »

> **Définition — produit vectoriel** (p.39) — « Soit u⃗ et v⃗ deux vecteurs. On appelle produit vectoriel de u⃗ par v⃗ et on note u⃗∧v⃗, le vecteur défini comme suit. • Si u⃗ et v⃗ sont colinéaires alors u⃗∧v⃗ = 0⃗. • Si u⃗ et v⃗ ne sont pas colinéaires alors : u⃗∧v⃗ orthogonal à u⃗ et à v⃗, (u⃗, v⃗, u⃗∧v⃗) est une base directe, ‖u⃗∧v⃗‖ = ‖u⃗‖.‖v⃗‖.sin α, où α est la mesure en radians de l'angle géométrique déterminé par deux représentants de même origine de u⃗ et v⃗. »

> **Théorème — propriétés du produit vectoriel** (p.40) — « Pour tous vecteurs u⃗, v⃗ et w⃗ : • u⃗∧u⃗ = 0⃗. • u⃗∧v⃗ = 0⃗, si et seulement si, u⃗ et v⃗ sont colinéaires. • u⃗∧v⃗ = −(v⃗∧u⃗). • au⃗∧bv⃗ = ab(u⃗∧v⃗), pour tous réels a et b. • (u⃗ + v⃗)∧w⃗ = u⃗∧w⃗ + v⃗∧w⃗. • u⃗∧(v⃗ + w⃗) = u⃗∧v⃗ + u⃗∧w⃗. »

> **Théorème — expression analytique du produit vectoriel** (p.40) — « L'espace est muni d'une base orthonormée directe (i⃗, j⃗, k⃗). Pour tous vecteurs u⃗(a, b, c) et v⃗(a', b', c'), u⃗∧v⃗ = (bc' − cb')i⃗ + (ca' − ac')j⃗ + (ab' − ba')k⃗. »

> **Définition — distance d'un point à une droite** (p.41) — « On appelle distance d'un point M à une droite D, la distance MH, où H est le projeté orthogonal de M sur D. Cette distance est notée d(M, D). »

> **Théorème — distance d'un point à une droite** (p.41) — « Soit D une droite de vecteur directeur u⃗ et A un point de D. La distance d'un point M de l'espace à la droite D est le réel d(M, D) = ‖MA⃗∧u⃗‖ / ‖u⃗‖. »

> **Propriété — produit mixte comme déterminant** (p.42) — « L'espace est muni d'un repère orthonormé direct (O, i⃗, j⃗, k⃗). Pour tous vecteurs u⃗, v⃗ et w⃗ de l'espace, (u⃗∧v⃗).w⃗ = (v⃗∧w⃗).u⃗ = (w⃗∧u⃗).v⃗ = det(u⃗, v⃗, w⃗). »

> **Théorème — aires** (p.42) — « • L'aire d'un parallélogramme ABCD est égale à ‖AB⃗∧AD⃗‖. • L'aire d'un triangle ABD est égale à (1/2)‖AB⃗∧AD⃗‖. »

> **Théorème — volume du parallélépipède** (p.42) — « L'espace est muni d'un repère orthonormé direct. Le volume d'un parallélépipède ABCDEFGH est égal à |(AB⃗∧AD⃗).AE⃗| = |det(AB⃗, AD⃗, AE⃗)|. »

> **Démonstration du volume du parallélépipède** (p.43, démonstration imprimée, texte courant, non encadré) — « Soit M le point de l'espace tel que AB⃗∧AD⃗ = AM⃗ et K le projeté orthogonal de E sur la droite (AM). On sait que le volume 𝒱 du parallélépipède ABCDEFGH est égal au produit de l'aire du parallélogramme ABCD et de la distance AK, d'où 𝒱 = ‖AM⃗‖.‖AK⃗‖. Les vecteurs AM⃗ et AK⃗ étant colinéaires, on en déduit que |AM⃗.AK⃗| = ‖AM⃗‖.‖AK⃗‖. Par suite, 𝒱 = |(AB⃗∧AD⃗).AK⃗| = |(AB⃗∧AD⃗).AE⃗|. Le théorème en découle. »

> **Théorème — volume du tétraèdre** (p.43) — « L'espace est muni d'un repère orthonormé direct. Le volume d'un tétraèdre ABCD est égal à (1/6)|(BC⃗∧BD⃗).BA⃗| = (1/6)|det(BC⃗, BD⃗, BA⃗)|. »

Absents du chapitre (vérifié sur les 14 pages) : définition du produit scalaire par projection orthogonale, équation cartésienne d'un plan, vecteur normal défini en encadré, distance d'un point à un plan, sphère, produit mixte comme notion nommée, « Résumé », « Avec l'ordinateur ».

### Écart avec la référence

**Référence** : chap. 13 de `math-bac-techniques` (manuel 222451, p.275–306, 32 p., 6 activités préliminaires, 26 exercices, QCM absent) et chap. 15 de `math-bac-math`.

**Ce que la référence enseigne et que ce manuel n'a PAS (à exclure)** :
- le **produit mixte** nommé et ses propriétés (coplanarité par (u⃗,v⃗,w⃗) = 0, base orthonormée directe ⇔ produit mixte = 1) : ce manuel n'a que le déterminant et l'égalité (u⃗∧v⃗).w⃗ = det ;
- **équation cartésienne d'un plan** (par point et vecteur normal, vecteur normal (a,b,c) de ax+by+cz+d=0), **plan médiateur**, **distance d'un point à un plan** ;
- **représentation paramétrique d'une droite** comme outil de cours, distance point-droite par projection orthogonale (méthode H : AH⃗.u⃗ = 0) — seule la formule ‖MA⃗∧u⃗‖/‖u⃗‖ est en encadré ; l'ex. 14 (minimiser MA via t) y fait seulement appel en exercice ;
- **positions relatives plan/plan, droite/plan, droite/droite par vecteurs normaux/directeurs** (tableau p.283 de la référence) ;
- **hauteur du tétraèdre** h = |(BC,BD,BA)|/‖BC∧BD‖ ; **distance entre deux droites non coplanaires**, perpendiculaire commune ;
- toute la **sphère** (définition, équation cartésienne, sphère de diamètre [AB], section plane, plan tangent, sphère circonscrite) ;
- le **sinus/cosinus de l'angle de deux vecteurs** (|sin θ| = ‖u∧v‖/(‖u‖‖v‖)) en encadré ; l'**aire du triangle** n'est en encadré que sous la forme AB, AD (triangle ABD) ;
- le **vecteur normal u⃗∧v⃗** d'un plan en encadré ; le **moment d'une force**, **Geospace**/« Avec l'ordinateur », le **Résumé du cours** et l'**Aperçu historique** paginés à part ;
- la définition du produit vectoriel par « normal au plan (ABC) » : ici la définition est par « orthogonal à u⃗ et à v⃗ ».

**Ce que ce manuel a EN PLUS** :
- section **« Rappels »** sur les **déterminants 3×3** (formule, coplanarité de quatre points par déterminant) et sur le produit scalaire (définition par cos, propriétés, expression analytique, norme, distance) ;
- **orientation de l'espace** et **d'un plan** (observateur d'Ampère, repère direct/indirect, permutations de bases, exercice résolu 1) — absente de la référence ;
- **théorème d'existence/unicité de k⃗** (‖k⃗‖ = d, orthogonal à i⃗, j⃗, base directe) ;
- **démonstration imprimée** du volume du parallélépipède ; volume du tétraèdre démontré en activité 13 ;
- **QCM et Vrai-Faux** (p.45) que la référence n'a pas ; exercice 4 (**loi des sinus** par produit vectoriel), exercices 7–11 (équation u⃗∧v⃗ = w⃗, identité de non-associativité, vecteur orthogonal à deux vecteurs), ex. 3 (repères orthogonaux).

### Bornes de scope

- ✅ INCLUS : déterminant 3×3 (formule et coplanarité de 4 points) ; produit scalaire (définition par cos, propriétés, expression analytique, norme, distance, repère orthonormé) ; orientation de l'espace (repère direct/indirect, permutations, opposé) et d'un plan ; produit vectoriel (définition géométrique en 3 conditions, propriétés, nullité ⇔ colinéaires, anticommutativité, bilinéarité, expression analytique en base orthonormée directe) ; produit mixte comme (u⃗∧v⃗).w⃗ = det ; distance d'un point à une droite par ‖MA⃗∧u⃗‖/‖u⃗‖ ; aire d'un parallélogramme/triangle ; volume du parallélépipède et du tétraèdre ; calculs : produit scalaire et norme en repère orthonormé, produit vectoriel en composantes ou sur une figure de cube, aire, volume, coplanarité par colinéarité de produits vectoriels, loi des sinus, minimisation d'une distance par paramètre (ex. 14).
- ⛔ EXCLU : produit mixte nommé avec ses propriétés (base orthonormée directe ⇔ 1) ; équation cartésienne d'un plan, vecteur normal en encadré, distance point-plan par la formule |ax+by+cz+d|/√(a²+b²+c²) (ch. 14) ; BH par le volume, comme dans l'ex. 15, reste inclus ; positions relatives par vecteurs normaux ; distance entre deux droites non coplanaires ; sphère sous toutes ses formes ; hauteur du tétraèdre en encadré ; sin/cos d'angle en encadré ; Geospace ; démonstration de l'expression analytique du produit vectoriel (admise, non démontrée) ; transformations de l'espace, quadriques, ℝⁿ.
- ⚠ Point à signaler : l'exercice 14 (distance A–droite D en paramétrique) et l'activité 6 (angle BAC, perpendicularité (AD) ⊥ (ABC)) exigent des savoir-faire non encadrés (paramétrisation, perpendiculaire à un plan par deux orthogonalités) ; la référence les traite par des encadrés absents ici.

### Lecture

- **Lues par l'OCR (texte)** : p.34 (page d'ouverture historique, texte seul sans formule) ; p.35 à p.47 en texte, mais **dégradées** : toutes les formules, vecteurs, exposants, fractions et le contenu des encadrés y sont inexploitables.
- **Lues sur l'image (110 dpi)** : p.35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47 = **13 pages sur 14** ; zooms 220 dpi sur p.46 (ex. 2, 4, 11) et p.47 (ex. 18). Seule la p.34 n'est pas confrontée à l'image (texte clair, aucune formule).
- **Sondage image** : 13 pages sur 14 (≥ 1 sur 10), soit toutes les pages à formule ou encadré. **Écarts OCR/image constatés** : (1) tous les symboles ∧, ⃗, fractions, racines, indices et exposants cassés ou absents dans l'OCR ; (2) p.35, le texte OCR mêle les encadrés roses aux énoncés (« Sur 2umsbses dl leurs ») : encadrés transcrits depuis l'image ; (3) p.47 ex. 16 OCR « BIOK » mais l'image donne « BIJOK » ; ex. 17 OCR « ABKLIJGH » confirmé ; (4) p.47 ex. 18, l'OCR et l'image donnent « orthonormé direct » (zoom) ; (5) p.46 ex. 11, u⃗(1,−1,0), v⃗(0,1,−1), w⃗(−1,0,1) lus sur zoom : l'OCR les rend illisibles ; (6) p.38 : l'exercice résolu 1 a une incohérence interne (énoncé (CG⃗,DC⃗,BC⃗), solution (CG⃗,BC⃗,DC⃗)), conservée comme anomalie du manuel ; (7) p.44 activité 14 : coordonnées lues sur l'image, « R(1,1,0) » confirmé (OIRJ face inférieure) .

## 2.14 Chapitre 14 — Équations de droites, de plans et de sphères (manuel 222434, p.48–62)

**Page de garde (p.48)** — Titre : « Equations de droites, de plans et de sphères » ; numéro imprimé « Chapitre 4 »
(numérotation interne du tome 2 ; rang 14 dans la numérotation content ; bandeau courant « Equations de droites,
de plans et de sphères »). Citation : « La géométrie analytique est une approche de la géométrie dans laquelle on
représente les objets par des équations ou inéquations. Le plan ou l'espace est nécessairement muni d'un repère.
La géométrie analytique permet à l'inverse de représenter des fonctions mathématiques sous la forme de courbes,
de graphiques. Elle est donc fondamentale pour la physique et l'infographie. » — (Wikipedia).
Mention liminaire (p.49) : « Dans tout le chapitre, l'espace est orienté dans le sens direct. »

**Plan du chapitre** (pas de page « plan » imprimée : déduit des intertitres) : I. Equations d'une droite et d'un
plan (p.49–50) ; II. Vecteur normal à un plan (p.50–51) ; III. Position relative de plans (p.52–53) ; IV. La Sphère
(p.53–54) ; V. Intersection d'une sphère et d'un plan (p.54–56) ; QCM – Vrai-Faux (p.57) ; Exercices et problèmes
(p.58–62, 32 exercices). Pas d'activités préliminaires, pas de résumé du cours, pas de rubrique « Avec l'ordinateur »,
pas d'aperçu historique, pas de corrigés. Trois « Exercice résolu » (ER 1, 2, 3) avec solution rédigée.

### Cours — Activités et exercices résolus

Repère général : (O, i⃗, j⃗, k⃗) ; repère orthonormé (direct quand dit) dès la partie II.

**I. Équations d'une droite et d'un plan** (p.49–50)

- **Act. 1** (p.49) : A(0, −1, 1), B(2, 1, 3) ; Δ : x = α, y = −2 + 2α, z = 1 + α (α ∈ ℝ). 1) un point et un vecteur
  directeur de Δ ; 2) représentation paramétrique de la droite Δ′ passant par A et parallèle à Δ ; 3) a) représentation
  paramétrique de (AB) ; b) (AB) et Δ sécantes en un point I à préciser.
- **Act. 2** (p.49) : A(−1, 2, 1), B(1, −6, −1), C(2, 2, 2). 1) a) A, B, C non alignés ; b) équation cartésienne du plan
  (ABC) ; 2) équation cartésienne du plan Q passant par O et parallèle à (ABC) ; 3) D(0, 0, 1) : intersection de (OD)
  avec (ABC) puis avec Q.
- **Act. 3** (p.50) : A(−1, 2, 1), B(−1, 0, 1). 1) équation cartésienne de chacun des plans (O, i⃗, k⃗) et (O, j⃗, k⃗) ;
  2) équation cartésienne de chacun des plans (A, i⃗, k⃗) et (B, j⃗, k⃗).

**II. Vecteur normal à un plan** (p.50–51)

- **Act. 1** (p.50) : A(−5, 10, 2), B(−2, 1, 2). 1) équation du plan P passant par A(−5, 10, 2) et de vecteur normal
  n⃗ (2, 1, −1) ; 2) ensemble des points M(x, y, z) tels que BM⃗.n⃗ = 0.
- **ER 1** (p.50–51) : repère orthonormé direct ; A(1, 1, 1), B(1, 2, 3), C(0, 0, 1). 1) A, B, C non alignés ;
  2) justifier que AB⃗ ∧ AC⃗ est normal à (ABC) ; 3) a) coordonnées de AB⃗ ∧ AC⃗, b) équation cartésienne de (ABC) ;
  4) représentation paramétrique de la droite passant par O et perpendiculaire à (ABC). Solution imprimée :
  AB⃗ (0, 1, 2), AC⃗ (−1, −1, 0) ; AB⃗ ∧ AC⃗ (2, −2, 1) ; (ABC) : 2x − 2y + z − 1 = 0 ; droite : x = 2α, y = −2α,
  z = α (α ∈ ℝ).
- **Act. 2** (p.51) : cube ABCDEFGH d'arête 1, repère orthonormé direct (A, AB⃗, AD⃗, AE⃗). 1) équation cartésienne
  du plan (AFH) ; 2) représentation paramétrique de la droite perpendiculaire à (AFH) passant par C ; 3) distance de
  C au plan (AFH) ; 4) volume du tétraèdre CAFH.

**III. Position relative de plans** (p.52–53)

- **Act. 1** (p.52) : repère orthonormé direct ; P : 4x − 2y + 2z + 3 = 0, Q : −2x + y − z + 6 = 0, R : x − 2z + 1 = 0.
  1) P et Q parallèles ; 2) a) P et R perpendiculaires, b) représentation paramétrique de leur droite d'intersection ;
  3) que dire de Q et R ?
- **ER 2** (p.52–53) : A(2, 0, −1), B(1, −1, 0), C(0, 1, 4). 1) a) A, B, C non alignés, b) équation de (ABC) ; 2) plan Q
  passant par O et parallèle à (ABC) ; 3) a) plan R passant par A et perpendiculaire à (AC), b) R ⊥ (ABC) ;
  4) intersection Δ de (ABC) et R. Solution imprimée : AB⃗ (−1, −1, 1), AC⃗ (−2, 1, 5), AB⃗ ∧ AC⃗ (−6, 3, −3) ;
  (ABC) : 2x − y + z − 3 = 0 ; Q : 2x − y + z = 0 ; R : 2x − y − 5z − 9 = 0 ; Δ : x = α, y = −4 + 2α, z = −1.

**IV. La Sphère** (p.53–54)

- **Act. 1** (p.53) : I(1, 0, 2) ; S = ensemble des M(x, y, z) tels que x² + y² + z² − 2x − 4z + 4 = 0. 1) M ∈ S ⇔ IM = 1 ;
  2) A(1, 1, 2) et B(1, −1, 4) sont-ils des points de S ?
- **Act. 2** (p.53) : A(x₀, y₀, z₀), B(x₁, y₁, z₁) : l'ensemble des M tels que MA⃗.MB⃗ = 0 est la sphère de centre le milieu I
  de [AB] et de diamètre [AB] (« Cette activité démontre le théorème suivant »).
- **Act. 3** (p.54) : A(−1, 1, 0), B(0, 1, 1) : ensemble des points M tels que MA = 2MB.
- **Act. 4** (p.54) : ensemble des M(x, y, z) tels que a) x² + y² + z² − 2x + 2y + 2z + 1 = 0 ; b) … + 4 = 0 ;
  c) … + 3 = 0 (mêmes termes −2x + 2y + 2z).

**V. Intersection d'une sphère et d'un plan** (p.54–56)

- **Act. 1** (p.54) : S sphère de centre O et de rayon 1. 1) P : x + y + z − 1 = 0 : distance de O à P, position
  relative de S et P ; 2) idem pour Q : x + y + z + 2 = 0 et R : x + y + z + √3 = 0. (Figure : sphère et plan.)
- **Act. 2** (p.55) : S = {M(x, y, z) ; x² + y² + z² − 2x = 1} ; position relative de S et de P : z = 0, Q : x + y = 0,
  R : x = 1.
- **ER 3** (p.55–56) : S = {M ; x² + y² + z² + 2x − 4y + 2z = 3}. 1) rayon R et centre I ; 2) a) A(−3, 1, 1) ∈ S,
  b) plan P tangent à S en A ; 3) Q = {M ; MA = MI} : a) Q est un plan (équation), b) Q ∩ S est un cercle (centre,
  rayon), c) équation de la sphère S′ tangente à P et Q respectivement en A et K ; 4) R : 2x + y − 2z − 6,5 = 0 :
  R ∩ S est un cercle (centre, rayon). Solution imprimée : S de centre I(−1, 2, −1), rayon 3 ; P : −2x − y + 2z − 7 = 0
  (IA⃗ (−2, −1, 2) normal) ; Q plan médiateur de [IA], K(−2 ; 1,5 ; 0), Q : −2x − y + 2z − 2,5 = 0 ; IK = 1,5 < 3, cercle de
  centre K et de rayon √(9 − 9/4) = 3√3/2 ; S′ de centre J(−2,5 ; 1,25 ; 0,5), rayon 0,75 ; h = |−2 + 2 + 2 − 6,5|/√9 = 1,5,
  H(0 ; 2,5 ; −2) obtenu par IH⃗ colinéaire à IA⃗, cercle de centre H et de rayon 3√3/2. [sic] la solution imprime
  l'équation de S′ avec « x » trois fois : (x + 2,5)² + (x − 1,25)² + (x − 0,5)² = 0,75² (coquille pour x, y, z).

### QCM – Vrai-Faux (p.57, réponses non fournies)

Repère orthonormé direct (O, i⃗, j⃗, k⃗). **QCM** « Cocher la réponse exacte. » : 1) S : x² + y² + z² − x − y − z − 1/2 = 0 ;
a) centre et rayon parmi (I(0,5 ; 0,5 ; 0,5), rayon 0,25) / (I(0,5 ; 0,5 ; 0,5), rayon √5/2) / (I(1, 1, 1), rayon 0,5) ;
b) intersection de S avec le plan x + y + z + 1/2 = 0 : cercle / point / vide. 2) cube ABCDEFGH d'arête 1, repère
(A, AB⃗, AD⃗, AE⃗) : a) équation du plan (BCH) parmi x + y − 1 = 0 / x + z − 1 = 0 / y + z − 1 = 0 ; b) le système
{x + z − 1 = 0 ; y = 1} est celui de (HG) / (HC) / (HD) ; c) intersection des plans x + y − 1 = 0 et x − y = 0 : (HC) /
(BD) / la droite passant par le centre du carré ABCD et parallèle à (AE). **VRAI-FAUX** « Répondre par vrai ou faux
en justifiant la réponse. » : 1) x − 2y + z − 1 = 0 et x + y + z − 1 = 0 sont perpendiculaires ; 2) P : x + 2y + 3z + 4 = 0 :
pour tous A, B, C de P, u⃗ = i⃗ + 2j⃗ + 3k⃗ est colinéaire à AB⃗ ∧ AC⃗ ; 3) le plan x = 0,5 coupe S : x² + y² + z² = 1
suivant un cercle de centre I(0,5 ; 0 ; 0) et de rayon 0,5 ; 4) la sphère (x − 1)² + (y − 1)² + (z − 1)² = 1 est
tangente à chacun des plans x = 0, y = 0, z = 0.

### Exercices et problèmes (p.58–62) — 32 exercices

Repère orthonormé direct (O, i⃗, j⃗, k⃗) sauf mention contraire (consigne p.58). Numéros imprimés en cases 1…32.

- **Ex. 1** (p.58) : représentation paramétrique de (AB) : a) A(1, −2, 3), B(−1, 0, 1) ; b) A(2 ; 3,5 ; 0), B(2, −2, 1) ;
  c) A(0, 0, 1), B(−1, −1, −1).
- **Ex. 2** (p.58) : D : x = 1 − α, y = 2 + α, z = −1 − α ; D′ : x = 1 + 2β, y = 2 − 2β, z = 1 + 2β ; montrer D′ // D.
- **Ex. 3** (p.58) : position relative de D et P : Δ : x = 2t + 4, y = −3t − 5, z = t + 8 avec P : x + y + z − 5 = 0 ;
  Δ : x = 5t + 4, y = 3, z = 2t avec P : 2x − 3y + 4z − 11 = 0.
- **Ex. 4** (p.58) : points d'intersection du plan P : 2x + 3y − 5z = 20 avec les droites (O, i⃗), (O, j⃗) et (O, j⃗ ∧ i⃗).
- **Ex. 5** (p.58) : parallélépipède rectangle ABCDEFGH, AB = 2, AD = 1, AE = 1 ; I milieu de [BD] ; repère
  R = (A, ½AB⃗, AD⃗, AE⃗). 1) représentation paramétrique de (HI) ; 2) équation de (DEG) ; 3) (HI) coupe (DEG) au milieu
  de [HI].
- **Ex. 6** (p.58) : A(−1, −2, −3). 1) équation cartésienne de P(A, i⃗ − j⃗, k⃗), Q(A, i⃗ + j⃗, i⃗ + k⃗), R(A, i⃗ ∧ j⃗, j⃗ ∧ k⃗) ;
  2) distances de O à P, Q, R.
- **Ex. 7** (p.58) : tétraèdre OIJK, repère (O, OI⃗, OJ⃗, OK⃗) orthonormé direct. 1) équation de chaque plan des faces ;
  2) M(1/3, 1/3, 1/3) : distance de M à chaque face ; 3) O, I, J, M non coplanaires, volume du tétraèdre OIJM.
- **Ex. 8** (p.58) : plan passant par A et de vecteur normal n⃗ : a) A(1, 0, 1), n⃗ (2, −1, 3) ; b) A(1, 2, 0), n⃗ (1, −1, 0) ;
  c) A(−1, 2, −3), n⃗ (2, −3, −4).
- **Ex. 9** (p.58) : droite passant par A et perpendiculaire à P (représentation paramétrique) : a) A(0, 0, 1),
  P : −3x + 2y − 7 = 0 ; b) A(1, −3, 2), P : y − 5 = 0 ; c) A(1, 5, 3), P : y − 5z + 4 = 0.
- **Ex. 10** (p.59) : P : −x + 5y − z = 7, A(1, 1, 5). 1) A ∉ P ; H(x₀, y₀, z₀) projeté orthogonal de A sur P : 2) a) justifier
  l'existence de k tel que AH⃗ (−k, 5k, −k), b) coordonnées de H.
- **Ex. 11** (p.59) : A(1, −2, 3), B(2, 0, 3), C(0, −1, 2). 1) non alignés ; 2) équation de (ABC) ; 3) plan Q passant par
  D(0, 1, 2) parallèle à (ABC) ; 4) intersection de (OD) et (ABC).
- **Ex. 12** (p.59) : P : 2x − y + 2z − 5 = 0, Q : 2x + 2y − z − 4 = 0. 1) P ⊥ Q ; 2) distances de A(1, 2, −1) à P et à Q ;
  3) en déduire la distance de A à la droite d'intersection Δ de P et Q ; 4) représentation paramétrique de Δ ;
  5) point M de Δ tel que AM soit minimale.
- **Ex. 13** (p.59) : plan P_m : (1 + m)x + y − 2mz − 4 − 3m = 0, A(0, 3, −2). 1) a) distance de A à P_m, b) valeurs de m
  pour lesquelles cette distance vaut √2/2 ; 2) D : x = 1 − 2t, y = 3 + 2t, z = −1 − t : pour tout m, D ⊂ P_m.
- **Ex. 14** (p.59) : P : x + 2y + 2z − 1 = 0, Q : 3x − 4z = 0. 1) P et Q sécants ; 2) l'ensemble des points équidistants de
  P et Q est constitué de deux plans perpendiculaires passant par la droite d'intersection de P et Q.
- **Ex. 15** (p.59) : A(1, 2, −1), B(2, 1, 1). 1) plan Q passant par A perpendiculaire à (AB) ; 2) P_m : x + y + m − 3 = 0
  (écrit ainsi) : a) (AB) // P_m, b) valeur de m pour (AB) ⊂ P_m, c) P_m ⊥ Q pour tout m ; 3) B′, A′ projetés orthogonaux
  de B, A sur P_m : valeurs de m pour que ABB′A′ soit un carré.
- **Ex. 16** (p.59–60) : tétraèdre trirectangle OABC (OA, OB, OC deux à deux orthogonales), H projeté orthogonal de O sur
  (ABC), OA = a, OB = b, OC = c (> 0), repère R = (O, (1/a)OA⃗, (1/b)OB⃗, (1/c)OC⃗). 1) a) équation de (ABC) avec a, b, c ;
  b) en déduire 1/OH² = 1/OA² + 1/OB² + 1/OC² ; 2) a) aire du triangle ABC par un calcul de volume ; b) le carré de
  l'aire de ABC est la somme des carrés des aires des trois autres faces (De Gua de Malves, 1738, « généralisation
  du théorème de Pythagore à l'espace »).
- **Ex. 17** (p.60) : ensemble des M(x, y, z) : 1) x² + y² + z² − 4x + 2y − 6z = 0 ; 2) … − 4x + 2y − 6z + 14 = 0 ;
  3) … − 4x + 2y − 6z + 16 = 0.
- **Ex. 18** (p.60) : équation de la sphère passant par O(0, 0, 0), A(1, 1, 1), B(2, 0, 0), C(1, −2, 2).
- **Ex. 19** (p.60) : sphère de centre A tangente au plan P : A(1, 7, −1), P : x + y + z = 0 ; A(0, 2, 3), P : x − y + z + 5 = 0 ;
  A(5, 3, 1), P : 3x − 2y − z + 7 = 0.
- **Ex. 20** (p.60) : plan P tangent en A(1, 4, −5) à la sphère de centre I(1, 3, −2).
- **Ex. 21** (p.60) : A(2, 0, 0), B(1, 1, 0), C(1, 1, 1). (OAB) ⊥ (ABC) ; équations des plans médiateurs de [OA], [OB],
  [OC] ; centre et rayon de la sphère circonscrite à OABC.
- **Ex. 22** (p.60) : centre et rayon du cercle S ∩ P : 1) S : x² + y² + z² − 2x − 2y − 2z − 13 = 0, P : x + y + z − 1 = 0 ;
  2) S : x² + y² + z² − 3x + 5y − z = 0, P : x + 2y + 3z + 5 = 0.
- **Ex. 23** (p.60) : intersection de S et P : 1) S de centre O, rayon 2, P : x + 2y − z + 1 = 0 ; 2) S : x² + y² + z² − 4x + 2y + 2z = 0,
  P : x + y + z − 1 = 0 ; 3) S : x² + y² + z² − 2x + 3y − z = 1/2, P : x + 2y + 2z − 1 = 0 ; 4) S : x² + y² + z² + 2x − 4y − 4z + 4 = 0,
  P : x = 1 + 2α − β, y = −1 + β, z = 1 − α (α, β ∈ ℝ).
- **Ex. 24** (p.60) : A(0, 1, 0), B(0, 0, 1), C(1, 1, −1), S sphère de centre A, rayon 1 ; intersection de S avec 1) (ABC) ;
  2) le plan passant par A perpendiculaire à (AC) ; 3) le plan passant par C perpendiculaire à (AC).
- **Ex. 25** (p.61) : A(1, −1, 2), B(−1, 1, −2). 1) représentation paramétrique de (AB) ; 2) P plan passant par A ⊥ (AB),
  Q : x − y + 2z + 6 = 0 : a) équation de P, b) Q contient B et // P ; 3) sphère S tangente en B à Q et dont l'intersection
  avec P est le cercle de centre A et de rayon 2√3, I(a, b, c) centre : a) I ∈ (AB), b) b = −a et c = 2a, c) IB² − IA² = 12
  et a − b + 2c = 3, d) coordonnées de I, équation de S.
- **Ex. 26** (p.61) : A(6, 0, 0), B(0, 6, 0), C(0, 0, 6), D(−2, −2, −2). 1) a) A, B, C non alignés ; b) équation du plan
  P = (ABC) ; c) (OD) ⊥ P ; d) représentation paramétrique de (OD) ; e) H projeté orthogonal de O sur P, H équidistant
  de A, B, C ; f) (OD) est l'axe du cercle circonscrit à ABC ; 2) Q plan médiateur de [CD] : a) équation de Q, b) (OD)
  coupe Q en I (coordonnées) ; 3) S sphère de centre I et de rayon 3√3 : a) équation, b) A, B, C, D ∈ S, c) S ∩ P.
- **Ex. 27** (p.61) : S : x² + y² + z² + 2x − 2y − 2 = 0. 1) centre et rayon ; 2) P_m : x + z + m = 0 : 1. a) P₀ ∩ S est un
  cercle 𝒞 (centre, rayon) ; b) (O, (1/√2)(i⃗ − k⃗), j⃗) est un repère orthonormé de P₀ ; c) M ∈ P₀ de coordonnées (X, Y)
  dans ce repère : X, Y en fonction de x, y, z, équation cartésienne de 𝒞 dans ce repère ; 2. position relative de P_m
  et S selon m.
- **Ex. 28** (p.61) : A(0, 4, −1), B(−2, 4, −5), C(1, 1, −5), D(1, 0, −4). 1) équations des plans médiateurs de [AB],
  [BC], [AD] ; 2) ces trois plans ont un point commun I ; équation de la sphère circonscrite à ABCD.
- **Ex. 29** (p.61–62) : A(0, 6, 0), B(0, 0, 8), C(4, 0, 8) (figure). 1) (BC) ⊥ (BA), (CO) ⊥ (OA), (BC) ⊥ plan (OAB) ;
  2) volume du tétraèdre OABC ; 3) O, A, B, C sur une sphère (centre, rayon) ; 4) α ∈ ]0, 8[, M(0, 0, α), plan contenant M
  et orthogonal à (OB) rencontrant (OC), (AC), (AB) en N, P, Q : a) nature de MNPQ, b) (PM) ⊥ (OB) ? valeur de α pour
  (PM) ⊥ (AC), c) MP² en fonction de α, valeur de α minimisant PM.
- **Ex. 30** (p.62) : S sphère de centre J(0, 1, 0), rayon 1 ; OM⃗ = αk⃗, AN⃗ = βi⃗, A(0, 2, 0). 1) équation de S ;
  2) représentation paramétrique de (MN) avec α, β ; 3) a) (MN) tangente à S ⇔ α²β² = 4, b) coordonnées du point de
  contact.
- **Ex. 31** (p.62) : tétraèdre ABCD, G centre de gravité de BCD, I et J milieux de [BC] et [CD], 5KA⃗ + KD⃗ = 0⃗,
  AL⃗ = (1/6)AB⃗, repère (A, AB⃗, AC⃗, AD⃗). 1) coordonnées de A, B, C, D, G, I, J, K, L ; 2) représentations paramétriques de
  (IK), (JL), (AG) ; 3) ces trois droites sont concourantes.
- **Ex. 32** (p.62) : repère orthonormé (O, OA⃗, OC⃗, OS⃗), B(1, 1, 0), plan P : x + y = a, a ∈ ]0, 1[ ; section de P avec la
  pyramide SOABC et maximum de son aire (figure). 1) représentations paramétriques de (SA), (SB), (SC), (OC), (OA) ;
  2) I, J, K, L, M intersections de P avec (SA), (SB), (SC), (OC), (OA) : a) coordonnées, b) IKLM est un rectangle,
  c) aire du pentagone IJKLM ; 3) f(x) = (x√2/4)(4 − 3x) sur ]0, 1[ : a) variations, b) position de P réalisant l'aire
  maximale, vérifier qu'il passe par le centre de gravité du triangle OAC.

### Cours — Encadrés à retenir (VERBATIM, vérifiés sur l'image)

> **Droite (p.49)** — « Soit A un point, u⃗ un vecteur non nul et D la droite passant par A et de vecteur directeur u⃗.
> Alors D(A, u⃗) = { M ; AM⃗ = αu⃗ où α est un réel }. • Deux droites de l'espace sont parallèles si elles ont des
> vecteurs directeurs colinéaires. »

> **Plan (p.49)** — « L'espace est muni d'un repère (O, i⃗, j⃗, k⃗). • Soit A un point, u⃗ et v⃗ deux vecteurs non
> colinéaires et P le plan passant par A et de vecteurs directeurs u⃗ et v⃗. Alors P(A, u⃗, v⃗) = { M ; det(AM⃗, u⃗, v⃗) = 0 }.
> • Soit A et B deux points et u⃗ et v⃗ deux vecteurs non colinéaires. Alors les plans P(A, u⃗, v⃗) et P(B, u⃗, v⃗) sont
> parallèles. »

> **Vecteur normal — équation (p.50)** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). Si P est un plan
> d'équation ax + by + cz + d = 0, alors le vecteur n⃗ (a, b, c) est normal à P. Soit n⃗ un vecteur non nul . l'ensemble
> des points M tels que AM⃗.n⃗ = 0 est un plan de vecteur normal n⃗ . »

> **Vecteur normal — caractérisation (p.50)** — « Un vecteur non nul n⃗ est normal à un plan de vecteurs directeurs u⃗ et
> v⃗, si et seulement si, u⃗.n⃗ = v⃗.n⃗ = 0. Si un vecteur non nul n⃗ est normal à un plan P, alors toute droite de vecteur
> directeur n⃗ est perpendiculaire à P. »

> **Distance point-plan (p.51)** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). La distance d'un point
> M(x₀, y₀, z₀) au plan P d'équation ax + by + cz + d = 0 est le réel |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²). »

> **Plans parallèles / perpendiculaires (p.52)** — « Deux plans sont parallèles, si et seulement si, leurs vecteurs
> normaux sont colinéaires. Deux plans sont perpendiculaires, si et seulement si, leurs vecteurs normaux sont
> orthogonaux. »

> **Définition (p.53)** — « Soit R un réel strictement positif et I un point de l'espace. On appelle sphère de centre I
> et de rayon R, l'ensemble des point M de l'espace tels que IM = R. » [sic : « point » au singulier]

> **Conséquence (p.53)** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). Soit le point I(x₀, y₀, z₀) et R un
> réel strictement positif. L'ensemble des points M(x, y, z) tels que (x − x₀)² + (y − y₀)² + (z − z₀)² = R² est la
> sphère de centre I et de rayon R. »

> **Théorème (p.54)** — « Soit A et B deux points distincts de l'espace. L'ensemble des points M tels que MA⃗.MB⃗ = 0 est
> la sphère de diamètre [AB]. »

> **Théorème (p.54)** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). L'ensemble des points M(x, y, z) tels
> que x² + y² + z² + ax + by + cz + d = 0 est soit une sphère, soit un point, soit le vide. »

> **Théorème — intersection sphère-plan (p.55)** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). Soit S une
> sphère de centre A et de rayon R. Soit P un plan, h la distance de A à P et H le projeté orthogonal de A sur P.
> L'intersection de S et P est • vide si h > R, • réduite au singleton {H} si h = R, • le cercle de rayon √(R² − h²)
> et de centre H si h < R. »

Aucun autre encadré dans le chapitre (pas de résumé). Non encadrés mais utilisés : plan tangent (vecteur normal IA⃗, ER 3 / Ex. 20),
plan médiateur (ER 3), produit vectoriel ∧ et produit scalaire « . » (employés sans rappel dans ce chapitre).

### Écart avec la référence

Référence principale : ch.12 bac-techniques (`math-bac-techniques/12-droites-plans-espace`, manuel 222451) ; comparaison
secondaire : ch.15 bac-math (manuel 222446).

- **Ce que la référence enseigne et que ce manuel n'a PAS (à exclure)** : activités préliminaires (coordonnées, milieux,
  colinéarité, coplanarité) ; colinéarité et coplanarité par déterminants 2×2 et 3×3 (théorème p.259 de la référence ;
  ici le déterminant n'apparaît que dans la définition det(AM⃗, u⃗, v⃗) = 0, sans calcul de déterminant 3×3 enseigné) ;
  représentation paramétrique d'un plan (système avec λ, μ, thème central de la référence) : ici absente comme encadré :
  seul l'Ex. 23.4 (p.60) donne un plan sous forme paramétrique ; Act. 1 p.52 demande celle d'une droite et Ex. 6 des équations cartésiennes ; représentation cartésienne d'une droite (système de deux équations) :
  seulement employée (ER 2 q.4), jamais définie ; positions relatives de deux droites (tableau de quatre cas, droites non
  coplanaires) : absent ; positions relatives de deux plans par rapport a/a′ = b/b′ = c/c′ : remplacée par les vecteurs
  normaux (p.52) ; position relative droite-plan (théorème p.266) : absente comme encadré (traitée en Ex. 3) ;
  section d'un tétraèdre par un plan (Act. 5 p.267) : absente ; « Résumé du cours », « Avec l'ordinateur » (Geospace),
  « Aperçu historique » : absents.
- **Ce que ce manuel a EN PLUS de la référence bac-techniques** : produit scalaire et produit vectoriel de l'espace
  utilisés (repère orthonormé, espace orienté direct) ; vecteur normal à un plan et équation ax + by + cz + d = 0 ;
  perpendicularité de plans et de droite-plan ; distance d'un point à un plan ; **sphère** (définition, équation,
  théorème du diamètre, équation générale x² + y² + z² + ax + by + cz + d = 0, intersection sphère-plan, plan tangent,
  plan médiateur, sphère circonscrite à un tétraèdre) ; volume d'un tétraèdre (formule non encadrée, utilisée Act. 2,
  Ex. 7, 16, 29) ; exercices à paramètre m (Ex. 13, 15, 27).
- **Rapport à bac-math ch.15** : ce manuel reprend les mêmes sphères (théorème sphère-plan, ER 3 proche de l'exercice
  du plan tangent / plan médiateur de la référence, Ex. 30 identique à l'exercice « α²β² = 4 » de bac-math). Il n'a PAS :
  définitions du produit scalaire et du produit vectoriel (supposés acquis, aucun encadré ici), produit mixte, aire et volume
  en encadré, distance point-droite par ‖MA⃗ ∧ u⃗‖/‖u⃗‖ (Ex. 12 la fait par deux distances plan-point), translation,
  homothétie, QCM/VF de la référence (autres). produit scalaire, produit vectoriel et déterminant de trois vecteurs : chapitre précédent du même tome
  (content ch.13, manuel 222434 p.34–47).

### Bornes de scope

- ✅ INCLUS : représentation paramétrique d'une droite (point + vecteur directeur), droites parallèles par vecteurs
  directeurs colinéaires ; plan P(A, u⃗, v⃗) = {M ; det(AM⃗, u⃗, v⃗) = 0} et équation cartésienne (calcul par déterminant
  ou par vecteur normal) ; plans parallèles par P(A, u⃗, v⃗) et P(B, u⃗, v⃗) ; plans de base (O, i⃗, k⃗), (A, i⃗, k⃗) ;
  vecteur normal (a, b, c) d'un plan en repère orthonormé, AM⃗.n⃗ = 0, n⃗ = AB⃗ ∧ AC⃗ ; droite perpendiculaire à un
  plan ; distance point-plan ; plans parallèles / perpendiculaires (vecteurs normaux colinéaires / orthogonaux) ;
  droite d'intersection de deux plans ; intersection droite-plan, position droite-plan (Ex. 3, 15) ; projeté orthogonal
  d'un point sur un plan (Ex. 10, ER 3 q.4, Ex. 15) ; sphère (définition, équation centre-rayon, théorème du diamètre
  MA⃗.MB⃗ = 0, ensemble x² + y² + z² + ax + by + cz + d = 0 : sphère / point / vide, lieu MA = kMB) ; intersection
  sphère-plan (vide / point / cercle de rayon √(R² − h²) centre H, centre du cercle par projeté) ; plan tangent à une
  sphère ; plan médiateur ; sphère passant par 4 points ; sphère circonscrite à un tétraèdre ; tangence d'une droite
  à une sphère (Ex. 30) ; sphère tangente à un plan ; repères non orthonormés pour paramétrisation (Ex. 5, 31) ;
  problèmes à paramètre m ; section de pyramide et optimisation (Ex. 32).
- ⛔ EXCLU : colinéarité / coplanarité par déterminants 3×3 comme méthode enseignée ; positions relatives de deux
  droites (4 cas, non coplanaires) comme théorème ; représentation cartésienne de droite comme notion définie ;
  critère a/a′ = b/b′ = c/c′ de parallélisme de plans ; produit mixte, formule générale d'aire/volume par produit
  vectoriel (hors usage direct) ; distance point-droite par formule ; translations, homothéties ; coniques/quadriques
  autres que la sphère ; démonstrations de cours (rien n'est démontré hors Act. 2 p.53) ; QCM/VF corrigés ;
  sphère en repère non orthonormé.

### Lecture

- **Pages lues par l'OCR** : 048 à 062 (les 15 pages) — texte exploitable en prose ; **formules, matrices-colonnes,
  encadrés roses et bleus, figures illisibles** : p.49, 50, 51, 52, 53, 54 (pages d'encadrés) fortement dégradées.
- **Pages lues sur l'image (110 dpi)** : 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062
  — **15 pages sur 15**, toutes les données, encadrés et exercices ci-dessus sont repris de l'image (sondage ≥ 1 page sur 10 largement dépassé).
- **Écarts OCR / image constatés** : p.49 colonnes de texte et encadrés entrelacés par l'OCR (« AM =aù » pour AM⃗ = αu⃗) ;
  Act. 2 p.49 : OCR « B(1, 6, −1) » = erreur, image **B(1, −6, −1)** ; p.50 : OCR du chapitre illisible (« Ë », « ES »,
  Act. 3 noyée) et encadrés reconstruits sur image ; p.51 : OCR « 2x−2y+z−1 » correct mais matrices colonnes
  perdues, formule de distance dégradée ; p.52 : coordonnées de AB⃗, AC⃗ et AB⃗ ∧ AC⃗ à relire sur image ; p.53 :
  « sphère de centre I et de rayon R » correct, « (x−x₀)² » lu « (x = x0) » ; p.54 : Act. 3 et théorèmes lisibles, mais « MA.ME » pour MA⃗.MB⃗, « (x²+ÿ+…) » pour x²+y²+z² ; p.56 :
  √ et fractions détruits, solution lue sur image (« x » triple dans S′ = coquille imprimée) ; p.57 : cases à cocher
  « El / [ » et fractions « 1/2 » perdues (QCM 1 : −1/2) ; p.58 : « Ex. 4 (O, j⃗ ∧ i⃗) » lu « (o;jni) » ; p.59 : **Ex. 13
  A(0, 3, −2)** image, OCR « A(0, 3, 2) » faux ; Ex. 15 « x + y + m − 3 = 0 » conforme à l'image (aucun « z ») ;
  p.60 : Ex. 16 et Ex. 23.3 (« = 1/2 ») fractions perdues par l'OCR ; p.61 : Ex. 25 à 28 repris sur image ; p.62 :
  Ex. 31 « 5KA⃗ + KD⃗ = 0⃗ » et AL⃗ = (1/6)AB⃗ lus sur image, f(x) = (x√2/4)(4 − 3x) reconstitué sur image.
- Doutes signalés : (1) manuel sans corrigés pour QCM/VF et exercices ; (2) Ex. 15 : « m » seul sans variable ;
  (3) numéro de chapitre imprimé « 4 » ≠ rang 14 (convention du tome).

## 2.15 Chapitre 15 — Probabilités sur un ensemble fini (manuel 222434, p.63–81)

**Page de garde (p.63)** — Titre : « Probabilités sur un ensemble fini », bandeau « Chapitre **5** » (numérotation propre du
tome 2 ; c'est le chapitre 15 de la fiche). Citation : « Un homme du monde a proposé deux problèmes à Pascal et Roberval,
le second fut à l'origine des calculs de probabilité. C'est le problème "des points" ou "des parties" ou "de division". Le
prix d'un tournoi est gagné par le premier des participants qui obtient un certain nombre de points. Comment partager ce
prix si le tournoi est interrompu ? Toutes les solutions qui en furent ensuite données étaient fausses. Le calcul des
probabilités fut présenté au monde en 1657 par Huyghens. Pour la première fois, les concepts fondamentaux, énoncés et
correctement utilisés, sont dans le domaine public. » — (Dieudonné, Abrégé d'histoire des mathématiques, 1978).

**Plan (titres de parties imprimés, p.64–76)** : I. Expériences aléatoires · II. Définition d'une probabilité sur un
ensemble fini · III. Equiprobabilité · IV. Probabilité conditionnelle (sous-rubriques non numérotées : « Evénements
indépendants » p.73, « Formule des probabilités totales » p.74) · QCM — VRAI-FAUX (p.77) · Exercices et problèmes
(p.78–81, 18 exercices). Pas de sommaire imprimé, pas de résumé de cours, pas d'« Avec l'ordinateur », pas d'aperçu
historique. 6 « exercices résolus » intégrés au cours. Notation : C_n^p (aussi noté « (n ; p) en colonne, n au-dessus de p (lu « p parmi n ») »), A_n^p, p_B(A) =
p(A/B), 𝒫(E), univers noté **E** (et non Ω).

### Cours — Activités et exercices résolus (une ligne chacun)

**I. Expériences aléatoires** (p.64–66)

- **Act. 1** (p.64) : E = entiers naturels pairs ≤ **100** ; A multiples de 10, B de 6, C de 15. 1. dénombrer E, A, B, C.
  2. déterminer et dénombrer Ā, B̄, C̄, A∩B, A∩C, B∩C, A∩B̄, complémentaire de A∪B, complémentaire de A∩C, (A∩B)∪C
  (barres exactes à confirmer sur l'image : lecture « Ā, B̄, C̄, A∩B, A∩C, B∩C, A∩B̄, \overline{A∪B}, \overline{A∩C}, (A∩B)∪C »).
- **Act. 2** (p.64) : nombre d'anagrammes de CHOIX ; POSSIBLE ; BACCALAUREAT.
- **Ex. résolu 1** (p.64–65) : urne de boules 1, 2, 3, **5 tirages** avec remise. A_j = tirages sans le numéro j : card
  A₁, A₂, A₃ (= 2⁵) ; A_{2,3} = sans 2 ni 3 (= 1⁵ = 1) ; B = tirages n'amenant pas en même temps 2 et 3, B = A₂ ∪ A₃,
  card B = 2×2⁵ − 1 (corrigé imprimé).
- **Act. 3** (p.65) : 12 titres de revues, 3 clients ; 1. commandes possibles ; 2. aucun titre choisi deux fois ; 3. même
  revue pour tous ; 4. exactement deux clients choisissent le même titre.
- **Act. 4** (p.65) : n ≥ 2, 2 ≤ p ≤ n, E de cardinal n, a et b deux éléments. 1. nombre de parties à p éléments a. contenant
  a et b ; b. contenant a ou bien b ; c. ne contenant ni a ni b. 2. en déduire C_n^p = C_{n−2}^{p−2} + 2C_{n−2}^{p−1} + C_{n−2}^p.
- **Ex. résolu 2** (p.66) : cube de 5 cm d'arête peint puis découpé en 125 cubes de 1 cm ; tirage simultané de 4 cubes.
  1. combien de cubes à 3, 2, 1, 0 face colorée (8, 36, 54, 27) ; 2. tirages possibles C₁₂₅⁴ = 9691375 ; 3. exactement deux
  cubes à trois faces colorées : C₈²×C₁₁₇² = 190008 [valeur imprimée] ; 4. au moins une face colorée : C₉₈⁴ = 3612280.

**II. Définition d'une probabilité sur un ensemble fini** (p.66–69)

- **Act. 1** (p.67) : pièce lancée 3 fois (P/F). 1. issues ; 2. card de A « pile une seule fois » et B « P pour la première fois
  au deuxième lancer » ; 3. card A∩B et A∪B.
- **Act. 2** (p.67) : dé 1–6 où p(6) = 3 × p(chacun des 1…5). 1. probabilité de chaque événement élémentaire ; 2. A « pair »,
  B « impair ≤ 3 », C « pair > 3 », D « multiple de 3 ou pair ».
- **Ex. résolu 3** (p.68–69) : lot de 1000 appareils, 60 avec D₁, 50 avec D₂, 20 avec les deux. A « les deux défauts » (0,02),
  B « au moins un » (0,09), C « aucun » (0,91), D₁′ « D₁ sans D₂ » (0,04), D₂′ « D₂ sans D₁ » (0,03), D « un seul défaut »
  (0,07) ; diagramme de Venn imprimé p.69.

**III. Equiprobabilité** (p.69–70)

- **Ex. résolu 4** (p.69) : deux dés équilibrés rouge et vert (faces 1–6). 1. univers E (36 couples) ; 2. même chiffre
  (6/36 = 1/6) ; 3. chiffres distincts (5/6).
- **Act.** (p.70, non numérotée) : code = deux lettres suivies de deux chiffres. 1. codes possibles ; 2. au hasard :
  a. commençant par A ; b. contenant les lettres A et Z ; c. contenant le chiffre 0 deux fois ; d. sans chiffre pair.

**IV. Probabilité conditionnelle** (p.70–76)

- **Act. 1** (p.70) : familles à deux enfants (sexe et âge), naissances équiprobables. 1. a. les 4 éléments de l'univers ;
  b. aîné fille ; c. deux filles ; d. deux garçons ; e. un garçon et une fille. 2. une fille ouvre la porte : probabilité que
  l'autre enfant soit a. une fille ; b. un garçon.
- **Act. 2** (p.71) : urne de 4 boules rouges numérotées (1, 1, 2, 2) et 2 vertes (1, 2) ; R « rouge », D « numéro 2 ». 1. p(rouge) ;
  2. rouge tirée : prob. numéro 2 ; numéro 1 ; 3. verte tirée : idem ; 4. a. rouge et numéro 2 ; b. verte et numéro 1. Suit
  l'arbre de probabilités générique (p.71–72, expérience (I) à issues B, B̄ puis expérience (II) à issues A, Ā ; branches
  p(B), p(B̄), p(A/B), p(Ā/B), p(A/B̄), p(Ā/B̄) ; feuilles B∩A, B∩Ā, B̄∩A, B̄∩Ā).
- **Ex. résolu 5** (p.72–73) : dépistage sur 1000 individus : 10 % de malades ; 98 positifs sur 100 malades ; 1 positif sur
  100 non-malades. M « malade », T « test positif ». 1–2. p(T/M)=0,98, p(T̄/M)=0,02, p(T/M̄)=0,01, p(T̄/M̄)=0,99 ; 3. arbre :
  0,098 ; 0,002 ; 0,009 ; 0,891 ; 4. a. p(T)=0,107 ; b. p(M/T̄) = p(T̄∩M)/(1−p(T)) = 0,002/0,893 ≈ 0,0022.
- **Act. 3** (p.73) : dé équilibré 1–6 ; A « pair », B « multiple de 3 », C « multiple de 6 » ; p(A), p(B), p(C), p(A∩B), p(A∩C).
- **Act. 4** (p.74) : urne U₁ (3 noires, 6 vertes), U₂ (2 noires, 3 vertes) ; une urne choisie au hasard, deux tirages successifs
  avec remise dans l'urne choisie ; A « verte au 1er », B « verte au 2e » : indépendants ?
- **Act. 5** (p.74) : 3 candidats A, B, C ; deux cadeaux attribués au hasard (un candidat peut recevoir les deux) ; A « A ne
  reçoit aucun cadeau », B « B ne reçoit aucun cadeau ». 1. p(A), p(B), p(A∩B) ; 2. indépendants ?
- **Act. 6** (p.74) : usine : 1/3 de la production de la machine A, 1/4 de B, le reste de C ; défectueuses sur 1000 : 2 (A), 10 (B),
  5 (C). Par un arbre : a. p(défectueuse) ; b. p(fonctionne) ; c. p(provient de A | défectueuse) ; d. p(ne provient pas de A | fonctionne).
- **Ex. résolu 6** (p.75–76) : U₁ (7 noires, 3 vertes), U₂ (2 noires, 8 vertes) ; tirages avec remise : si le (n−1)ᵉ tirage est noir, le
  nᵉ se fait dans U₁, s'il est vert dans U₂. 1. urne choisie au hasard, p₁ (= 9/20) ; 2. a. p₂ (= 17/40) ; b. pₙ = (1/2)pₙ₋₁ + 1/5,
  n ≥ 2 ; 3. a. qₙ = pₙ − 2/5 géométrique (raison 0,5, q₁ = 1/20) ; b. pₙ = 2/5 + (1/20)(0,5)ⁿ⁻¹, lim pₙ = 2/5.
- **Act. 7** (p.76) : feu tricolore, cycle 1 min : vert 25 s, orange 5 s, rouge 30 s. 1. p(vert), p(orange), p(rouge) ;
  2. l'automobiliste passe sans s'arrêter avec prob. 99 % (vert), 80 % (orange), 1 % (rouge) : p(passer sans s'arrêter).
- **Act. 8** (p.76) : sport un jour ⇒ sport le lendemain avec prob. 0,4 ; pas de sport ⇒ sport le lendemain avec prob. 0,8 ;
  sport le lundi : probabilité de faire du sport le jeudi.

**QCM — VRAI-FAUX** (p.77)

- **QCM 1** : urne de 20 jetons numérotés de 0 à 19 ; probabilité de deux numéros impairs : a. tirage simultané ; b. successif
  avec remise ; c. successif sans remise ; choix (identiques en a, b, c) : 0,5 ; 9/38 ; 0,25.
- **QCM 2** : arbre pondéré imprimé (A : 0,9 ; Ā : 0,1 ; de A : B∩A 0,1, B̄∩A 0,9 ; de Ā : Ā∩B 0,9, Ā∩B̄ 0,1) ; a. p(B sachant A)
  (0,9 / 0,1 / 0,09) ; b. p(Ā∩B̄) (0,01 / 0,1 / 0,2) ; c. p(A sachant B) (0,09 / 0,5 / 0,9). [Figure lue sur l'image.]
- **Vrai-Faux** (justifier) : 1. A, B indépendants ⇒ p(A∪B) = p(A) + p(B) ; 2. A, B incompatibles ⇒ p(A∩B) = p(A).p(B) ;
  3. A∪B événement certain ⇒ pour tout C, p(C) = p(A∩C) + p(B∩C).

### Exercices et problèmes (p.78–81) — 18 exercices

- **Ex. 1** (p.78) : 12 ampoules dont 4 défectueuses, tirage simultané de 3 : p(aucune défectueuse) ; p(exactement une) ; p(au moins une).
- **Ex. 2** (p.78) : urne : 1 boule n°1, 2 boules n°2, 3 boules n°3, 4 boules n°4, … et enfin 9 boules n°9 [les points de suspension
  « … » sont imprimés : la suite des effectifs 5…8 n'est PAS donnée, seuls 1, 2, 3, 4 et 9 le sont — à signaler]. 1. nombre de boules ;
  2. tirage simultané de 2 : a. deux numéros pairs ; b. somme ≥ 3 ; c. somme ≤ 15 ; 3. 4 tirages successifs sans remise : « 1983 » et
  « 1389 » ont-ils la même probabilité ? 4. idem avec remise.
- **Ex. 3** (p.78) : classe de 40 élèves ; « oui » : maths 31, philosophie 1, sport 9 ; supplément : 1 aime seulement la philosophie,
  3 seulement le sport, 25 seulement les maths. Probabilité de : 1. les trois matières ; 2. maths et pas sport ; 3. ni philosophie ni
  maths [texte imprimé : « N'aime pas la philosophie et les mathématiques ? »] ; 4. aucune matière ; 5. au moins une.
- **Ex. 4** (p.78) : épreuve de 100 questions, candidat en a étudié 80, 3 tirées au sort : probabilité qu'il ait étudié 1. les trois ;
  2. deux seulement ; 3. une seule ; 4. aucune ; 5. au moins une.
- **Ex. 5** (p.78) : réussite de la 1re épreuve (maths) 80 % ; si réussie, 75 % pour la 2e (sciences physiques) ; sinon 40 %. M, S :
  déterminer p(M), p(S/M), p(S/M̄) et p(S).
- **Ex. 6** (p.78) : deux générateurs, panne chacun avec prob. 0,005, indépendamment : 1. les deux en panne ; 2. au moins un en état de marche.
- **Ex. 7** (p.79) : A, B indépendants, p(A) = 0,2, p(B) = 0,4 : p(A∩B), p(A∪B), p(A∩B̄), p(Ā∪B) [barres lues sur l'image, doute léger sur
  la 3e et la 4e].
- **Ex. 8** (p.79) : entreprise : 10 % ingénieurs, 80 % techniciens ; 80 % de femmes, 60 % des ingénieurs sont des hommes, 90 % des
  techniciens sont des femmes. 1. a. femme ingénieur ; b. homme technicien ; c. femme du personnel administratif ; 2. c'est une femme :
  a. technicienne ; b. ingénieur ; 3. c'est un ingénieur : a. femme ; b. homme.
- **Ex. 9** (p.79) : 2000 clients, 1200 modèle A, 960 abonnement I ; S « modèle A », C « abonnement I ». 1. p(modèle A) ; 2. parmi les
  acheteurs de A, 32 % ont l'abonnement I : a. A et abonnement I ; b. B et abonnement II.
- **Ex. 10** (p.79) : urne de 8 jetons (3 noirs n°1, 3 noirs n°2, 1 vert n°1, 1 vert n°2) ; pièce truquée, p(pile) = 7/15 ; pile ⇒ tirage
  simultané de 2 jetons, face ⇒ tirage successif sans remise. A « même numéro ou même couleur », B « même numéro et même couleur »,
  C « même couleur », D « même numéro ». 1. p(C/P), p(D/P), p(B/P), p(A/P) ; 2. p(A/F), en déduire p(A).
- **Ex. 11** (p.80) : tireurs X (9 fois sur 10) et Y (4 fois sur 10) ; X ne tire qu'une fois sur trois ; la cible est atteinte : probabilité
  que ce soit Y.
- **Ex. 12** (p.80) : urne A (3 blanches, 5 rouges), urne B (7 blanches, 5 rouges) ; deux dés de couleurs différentes : total ≤ 7 ⇒ urne A,
  total > 7 ⇒ urne B ; 4 boules tirées successivement sans remise. 1. 2 blanches et 2 rouges ; 2. que des rouges ; 3. que des rouges :
  probabilité p que ce soit l'urne B.
- **Ex. 13** (p.80) : deux amis arrivent indépendamment un jour numéroté de 1 à 8 (au hasard), restent 3 jours (période 1 à 10).
  1. même jour ; 2. un jour d'écart ; 3. peuvent se rencontrer ; 4. sachant qu'ils se sont rencontrés, ont pu passer ensemble au moins
  deux jours.
- **Ex. 14** (p.80) : fumeur : C₁ s'il reste un jour sans fumer, p(fume le lendemain) = 0,2 ; C₂ s'il fume, p(fume le lendemain) = 0,7.
  Fₙ « fume le nᵉ jour », pₙ = p(Fₙ). 1. arbre de choix : p(Fₙ₊₁/Fₙ), p(Fₙ₊₁/F̄ₙ), p(F̄ₙ₊₁/Fₙ), p(F̄ₙ₊₁/F̄ₙ) [barres lues sur
  l'image] ; 2. pₙ₊₁ = 0,5 pₙ + 0,2 ; 3. aₙ = pₙ − 0,4 géométrique (raison, limite) ; lim pₙ et interprétation.
- **Ex. 15** (p.80–81) : transmission d'une information P₁, P₂, … fidèle avec prob. 0,9, inversée avec 0,1 ; P₁ possède l'information
  non déformée ; Aₙ, pₙ. 1. p₁, p₂ ; 2. p₃ par arbre ; 3. pₙ₊₁ = 0,8 pₙ + 0,1 ; 4. pₙ en fonction de n ; 5. p₂₀ ; 6. lim pₙ.
- **Ex. 16** (p.81) : génotypes AA, Aa, aa ; 1. parents AA et Aa : p(enfant AA), p(Aa) ; 2. parents Aa et Aa : p(AA), p(Aa), p(aa) ;
  3. pₙ, qₙ, rₙ pour la nᵉ génération ; par arbre, montrer pₙ₊₁ = (pₙ + qₙ/2)², rₙ₊₁ = (qₙ/2 + rₙ)²,
  qₙ₊₁ = 1 − (pₙ + qₙ/2)² − (qₙ/2 + rₙ)² ; 4. α = p₀ − r₀ : a. pₙ − rₙ = α ; b. 2rₙ + qₙ = 1 − α ; 5. en déduire (pₙ), (qₙ), (rₙ) constantes.
- **Ex. 17** (p.81) : sac de n rouges et 2n noires, 3 boules tirées simultanément. 1. pₙ (une seule rouge), limite p ; 2. qₙ (au moins une
  rouge), limite q ; 3. trois tirages successifs avec remise : a. une seule rouge = p ; b. au moins une rouge = q.
- **Ex. 18** (p.81) : pile ou face : gagne dès que (nb de pile) dépasse de deux (nb de face), perd dès que (nb de face) dépasse de deux
  (nb de pile) ; p(pile) = 5/12, p(face) = 7/12. 1. nombre pair de lancers pour gagner ; 2–5. p(gagner au plus au bout de 2, 4, n, 20 lancers).

### Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Définition et théorème — dénombrement** (p.65) — « Soit E = {a₁, a₂,…,aₙ} un ensemble à n éléments et p un entier naturel non nul.
> * Le nombre des p- uplets d'éléments de E est l'entier nᵖ.
> * Le nombre de n- uplets d'éléments de E deux à deux distincts est l'entier n !
> * Si 1 ≤ p ≤ n alors
> • le nombre des p- uplets d'éléments de E deux à deux distincts est l'entier A_n^p = n!/(n−p)!,
> • le nombre de parties à p éléments de E est l'entier C_n^p = n!/((n−p)!p!).
> (L'entier C_n^p est aussi noté (n ; p) en colonne, n au-dessus de p (lu « p parmi n ») et on convient que C_n^0 = 1). »

> **Définition — expérience aléatoire, univers** (p.66) — « Une expérience aléatoire est une expérience dont le résultat est soumis au hasard et est
> donc imprévisible. L'ensemble E des issues d'une expérience aléatoire est appelé univers. Les éléments de E sont appelés événements élémentaires.
> Une partie A de E est appelée événement. »

> **Définition — probabilité sur E** (p.67) — « Soit E l'univers fini d'une expérience aléatoire et 𝒫(E) l'ensemble des événements de E. On appelle probabilité sur E,
> toute application p, de 𝒫(E) dans [0,1] vérifiant les conditions ci-dessous.
> • L'image p(E) de E est égale à 1.
> • L'image p(∅) de l'ensemble vide est égale à 0.
> • L'image p(A) d'un événement A, est la somme des images des événements élémentaires de A, c'est-à-dire p(A) = Σ_{aᵢ∈A} p(aᵢ). »
> **Vocabulaire** (p.67, hors encadré) : « Le triplet (E, 𝒫(E), p) est appelé espace probabilisé fini. L'événement E est appelé événement certain. L'événement vide est
> appelé événement impossible. L'événement contraire d'un événement A est noté Ā. Deux événements sont dits incompatibles si leur intersection est vide. »

> **Propriétés** (p.68) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et A et B deux événements de E.
> • p(Ā) = 1 − p(A). • p(A∪B) = p(A) + p(B) − p(A∩B).
> • Si A∩B = ∅ alors p(A∪B) = p(A) + p(B).
> • Si A₁, A₂, …, A_k sont des événements deux à deux incompatibles, alors p(A₁∪A₂∪…∪A_k) = p(A₁) + p(A₂) + … + p(A_k). »

> **Définition et théorème — probabilité uniforme** (p.69) — « Soit E l'univers fini d'une expérience aléatoire dans une situation d'équiprobabilité et 𝒫(E)
> l'ensemble des parties de E. L'application p définie de 𝒫(E) dans [0,1] par p(a) = 1/card(E), pour tout événement élémentaire a de E est une probabilité sur E,
> appelée probabilité uniforme. »
> **Propriété** (p.69) — « Si (E, 𝒫(E), p) est un espace probabilisé fini tel que la probabilité p est uniforme, alors p(A) = card(A)/card(E), pour tout événement A de E. »

> **Théorème — probabilité conditionnelle** (p.70) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et B un événement tel que p(B) ≠ 0. L'application p_B de 𝒫(E)
> dans [0,1], définie par p_B(A) = p(A∩B)/p(B), pour tout événement A, est une probabilité sur E. » (suivie d'une **Démonstration** p.70–71 : p_B(E) = 1, p_B(∅) = 0,
> p_B({αⱼ}) = p(αⱼ)/p(B), additivité.)

> **Définition — probabilité B-conditionnelle** (p.71) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et B un événement tel que p(B) ≠ 0. L'application p_B ainsi
> définie s'appelle probabilité B-conditionnelle. Le réel p_B(A) est noté p(A/B) (on lit « probabilité de A, sachant B »). »

> **Définition — indépendance** (p.74) — « On dit que deux événements A et B sont indépendants lorsque p(A∩B) = p(A)×p(B). Dans le cas où p(B) ≠ 0, la réalisation de B
> n'influence pas celle de A, c'est à dire p(A/B) = p(A). »

> **Définition — partition** (p.75) — « Soit E un ensemble fini, les parties B₁, B₂,…, B_n forment une partition de E lorsqu'ils sont deux à deux disjoints et leur réunion est E. »

> **Théorème — formule des probabilités totales** (p.75) — « Soit (E, 𝒫(E), p) un espace probabilisé fini, B₁, B₂,…, B_n des événements formant une partition de E tels que
> pour tout i, p(Bᵢ) ≠ 0. Alors pour tout événement A, p(A) = Σ_{i=1}^{n} p(A∩Bᵢ) = Σ_{i=1}^{n} p(Bᵢ).p_{Bᵢ}(A). » (Figure : E partitionné en B₁…B_n, A en rose ; suivie
> d'une démonstration : A∩B₁,…,A∩B_n forment une partition de A, additivité, p(A∩Bᵢ) = p(Bᵢ).p_{Bᵢ}(A).)

Aucun autre encadré : pas de formule des probabilités composées nommée, pas de formule de Bayes nommée, pas de tableau de tirages, pas de résumé (la formule p(A∩B) = p(A).p_A(B) est
utilisée dans les solutions p.73 et p.76 sans encadré ; la fraction p(M/T̄) = p(T̄∩M)/(1 − p(T)) de la p.73 est l'application directe de la définition).

### Écart avec la référence

Référence = chap. 18 « Probabilités » de bac-math (222446, p.179–207) ; chapitre voisin = chap. 14 de bac-techniques (222451, p.307–330).

**Ce que la référence enseigne et que ce manuel n'a PAS (à exclure)** :
- variables aléatoires (loi, espérance, variance, fonction de répartition), loi binomiale ; lois continues (uniforme, exponentielle) — partie B de la référence ;
- Bayes comme formule nommée (le cas M/T̄ de l'ex. résolu 5 et les ex. 11 et 12.3 en relèvent sans énoncé) ;
- principe des probabilités composées nommé et encadré (p(A∩B∩C) à trois événements absent) ;
- tableau « tirages successifs avec/sans remise, simultanés » (card nᵖ, A_n^p, C_n^p) ;
- indépendance de plus de deux événements, schéma de Bernoulli ;
- encadré « langage des probabilités » détaillé, résumé du cours, « Avec l'ordinateur », aperçu historique, exercices de simulation ;
- rappels de dénombrement en encadré de rappel : ici, seul l'encadré p.65 (p-uplets, arrangements, combinaisons), sans applications ni partie à 2ⁿ, ni binôme ;
- en bac-techniques : les 6 « activités préliminaires » et le résumé ; ce manuel a 6 exercices résolus, pas la rubrique « Avec l'ordinateur ».

**Ce que ce manuel a en plus** :
- une introduction au dénombrement dans le cours (p-uplets, anagrammes avec répétition, cube peint, ex. résolu 2) : activités d'**expériences aléatoires** (partie I) absentes
  du schéma bac-techniques ;
- la définition de la probabilité par somme des événements élémentaires (p(E)=1, p(∅)=0, p(A)=Σp(aᵢ)), sans « application additive » ;
- le théorème « p_B est une probabilité » avec démonstration ; la partition (définition) et la formule des probabilités totales à n parties démontrée ;
- l'étude de suites récurrentes issues de chaînes de Markov à deux états (ex. résolu 6, ex. 14, 15, 16) ; ex. 18 : jeu de pile ou face (marche aléatoire) ; ex. 17 : limites de probabilités ;
- QCM et Vrai-Faux (p.77) ; ex. de génétique (Hardy-Weinberg, ex. 16).

### Bornes de scope

- ✅ INCLUS : dénombrement de base (p-uplets, arrangements, combinaisons, parties, anagrammes avec répétitions, principe additif/multiplicatif en contexte) ; univers fini, événements
  (contraire, incompatibles, certain, impossible, élémentaire) ; probabilité sur 𝒫(E) et ses propriétés (complémentaire, réunion, additivité) ; équiprobabilité p(A) = card A / card E (dés, urnes,
  codes, pièces, tirages simultanés/successifs) ; probabilité conditionnelle (définition, p_B est une probabilité), arbres pondérés ; événements indépendants (deux événements) ; formule des
  probabilités totales (partition à n événements) ; suites récurrentes tirées de situations de probabilité (pₙ₊₁ = a pₙ + b, suites géométriques, limites) ; calcul de p(M/T̄) de type Bayes en application directe.
- ⛔ EXCLU : variable aléatoire, espérance, variance, fonction de répartition, loi binomiale, lois continues ; formule de Bayes énoncée comme théorème ; indépendance mutuelle de plus de deux événements ;
  schéma de Bernoulli ; probabilités composées à 3 événements en tant qu'encadré ; simulation (tableur, programmation) ; démonstration du binôme / identités de combinaisons (hors act. 4 p.65) ;
  univers infini ; ex. 2 (effectifs 5 à 8 non donnés) à ne pas exploiter tel quel.

### Lecture

- **OCR (texte)** : pages 63 à 81 (19 pages), toutes parcourues.
- **Image (110 dpi, relue en pleine page)** : **19 pages sur 19** : 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81 (soit ≥ 1/10 et les pages les plus denses ; toutes pages à formule, encadré, tableau ou figure lues sur image).
- **Écarts OCR/image constatés** : p.64 l'OCR écrit « 100 » (correct) mais le chapitre de référence a « 500 » (donnée du manuel de bac-math, pas ici) ; barres de complémentaire perdues (Ā, B̄, C̄ en « A, B ,C » ; « ANnB »
  pour A∩B̄ ; « AUB » pour le complémentaire de A∪B) ; p.65 encadré dénombrement : « n?/n! » pour nᵖ et n!, « C? = ... » pour C_n^p, formule de C_n^p déformée, « Sil1<p<n » pour « Si 1 ≤ p ≤ n » ; p.66 « C?xC2 » = C₈²×C₁₁₇²
  (la valeur 190008 est imprimée telle quelle, non recalculée) ; p.67 « Σ p(aᵢ) » rendu « Y p(a;) » ; p.68 « Dᵢ′ » rendu « D! » ; p.69 « p(a) = m6 / car » = 1/card(E) ; p.73 fractions et barres (« TS Il en résulte » = fraction p(T̄∩M)/(1−p(T)),
  valeur 0,002/0,893) ; p.75 « p_{Bᵢ}(A) » rendu « .pa, (A) » ; p.76 fractions de l'ex. résolu 6 (7/10, 2/10, 9/20, 17/40) en désordre dans l'OCR ; p.77 arbre du QCM 2 et cases du QCM 1 illisibles à l'OCR (valeurs 0,5 ; 9/38 ; 0,25 lues sur image) ;
  pp.78–81 numérotation 1…18 des exercices **absente** de l'OCR (numéros encadrés lus sur l'image) ; p.79 « 7/15 » rendu « 7 t égale » ; p.81 formules de l'ex. 16 (exposants au carré, fractions q_n/2) lues sur l'image.
- Aucun nombre ou mot d'énoncé faux détecté dans la couche texte pour la prose ; tous les écarts relevés concernent symboles, barres, fractions, indices et exposants.
- **Doutes signalés** : barres exactes de l'Act. 1 p.64 et de l'Ex. 7 p.79 (3ᵉ et 4ᵉ expression) ; ex. 2 p.78 effectifs des numéros 5 à 8 non imprimés (points de suspension) ; Act. 3 p.65 (consigne « commandent la même revue ») reprise telle quelle ;
  coquilles imprimées conservées : « événements A et B sont-ils indépendant » (Vrai-Faux 1), « est elle la même », « l'une » pour « l'urne » (ex. 12, texte image), « personne ... technisienne » (ex. 8) ; ex. 9 : « Quelle est la probabilité que le client ait
  acheté le modèle B et choisi l'abonnement II ? ».

## 2.16 Chapitre 16 — Variables aléatoires (manuel 222434, p.82–96)

**Page de garde (p.82)** — Titre imprimé : « Variables aléatoires » ; numérotation propre du manuel : « Chapitre **6** » (ce chapitre est le 16ᵉ de la fiche). Citation de couverture : « Né en 1777 dans le duché de Brunswick (Allemagne), Carl Friedrich Gauss fut un véritable génie des mathématiques. Entre autres découvertes, on lui doit une constatation très simple. Dans une population donnée (les salariés d'une entreprise, des haricots dans un sac, etc.), si on classe les individus selon une caractéristique (leur taille, leur poids, leur QI, leur niveau de compétence), on s'aperçoit que, plus on s'approche de la moyenne sur le critère considéré, et plus il y a d'individus. Plus on s'en éloigne, et moins il y en a. Aux deux extrémités, il n'y a presque personne. La représentation graphique de cette réalité s'appelle une courbe de Gauss et prend la forme d'une cloche. » (Pas de « Plan du chapitre » imprimé sur cette page, contrairement à la référence ; pas d'activités préliminaires, pas de résumé, pas d'« Avec l'ordinateur », pas d'aperçu historique.)

**Plan (reconstitué sur les titres imprimés, pas de plan imprimé)** : **A. Variables aléatoires sur un espace probabilisé fini** — I. Définition et propriétés (p.83–84) · II. Espérance et variance d'une variable aléatoire (p.84–86) · III. Fonction de répartition d'une variable aléatoire (p.86–87) · IV. Loi binomiale (p.87–88) ; **B/ Exemples de lois continues** — I. La loi uniforme (p.88–90) · II. La loi exponentielle (p.90–92) ; **QCM – VRAI-FAUX** (p.93) ; **Exercices et problèmes** (p.94–96, 19 exercices numérotés dans un cadre).

### Cours — Activités (une ligne chacune)

**A. I. Définition et propriétés** (p.83–84)
- **Act. 1** (p.83) : urne de deux boules numérotées 4 et trois numérotées −2 ; tirage simultané de deux boules. 1) a) P(deux boules « 4 ») ; b) P(numéros différents) ; c) P(même numéro) ; 2) X = somme des numéros : valeurs prises par X.
- **Act. 2** (p.83) : pièce équilibrée lancée trois fois. 1) ensemble des issues ; 2) X = nombre de « face » : P(X=0), P(X=1), P(X=2), P(X=3).
- **Exercice résolu 1** (p.84) : concours, trois candidats dans l'ordre, le premier qui réussit le test (probabilité p) est engagé ; X = j si le jᵉ est engagé, X = 4 si aucun ; loi de X. Solution imprimée : p(X=1)=p ; p(X=2)=(1−p)p ; p(X=3)=(1−p)²p ; p(X=4)=(1−p)³ ; « Remarquons aussi que p+(1−p)p+(1−p)²p+(1−p)³=1 ».

**A. II. Espérance et variance** (p.84–86)
- **Act. 1** (p.85) : dé à six faces ; X = numéro, Y = 1 si pair, −1 si impair ; calculer E(X), E(−3X), E(Y), E(X+Y).
- **Act. 2** (p.85) : marchand de glaces, 5 parfums, trois personnes choisissent au hasard et indépendamment. 1) P(parfums deux à deux différents) ; P(même parfum) ; 2) X = nombre de parfums choisis : loi, espérance, écart-type.
- **Act. 3** (p.85–86) : enveloppe de 12 figures (4 rois, 4 dames, 4 valets). 1) tirage simultané de 5 cartes, X = nombre de rois : loi, espérance, écart-type ; 2) tirage successif avec remise de 5 cartes, Y = nombre de rois : loi, espérance, écart-type ; 3) comparer 1.b et 2.b et interpréter.

**A. III. Fonction de répartition** (p.86–87)
- **Act. 1** (p.86) : courbe en escalier de F : x ↦ p(X ≤ x) donnée (hauteurs lues 0,1 ; 0,3 ; 0,8 ; 0,9 ; 1, sauts en x = 0, 1, 2, 3, 4 vers 0,1 ; 0,3 ; 0,8 ; 0,9 ; 1, point plein à gauche de chaque palier). Lire : 1) valeurs prises par X ; 2) p(X ≤ −1), p(X ≤ 1.3), p(X ≤ 11/3), p(X ≤ 1), p(X < 2), p(X = 2), p(1 ≤ X ≤ 6) ; 3) loi de X.
- **Act. 2** (p.86) : pièce truquée, P(pile)=0.6, lancée 3 fois, X = nombre de piles. 1) loi de X ; 2) expression de F : x ↦ p(X ≤ x) et sa représentation.
- **Act. 3** (p.86–87) : trois urnes de jetons numérotés 1 à 6, un jeton tiré dans chacune, X = plus grand numéro tiré. 1) k entier ≤ 6 : a) probabilité dans chaque urne de tirer un numéro ≤ k ; b) en déduire p(X ≤ k) ; 2) fonction de répartition de X et sa courbe ; 3) loi de X.

**A. IV. Loi binomiale** (p.87–88)
- **Act. 1** (p.87) : fléchettes, P(atteindre la cible)=0.9. 1) deux tirs, X = nombre de succès : a) loi ; b) P(« au moins une fois sa cible ») ; 2) dix tirs, Y = nombre de succès : a) P(neuf succès), P(au moins un succès) ; b) loi de Y.
- **Act. 2** (p.87–88) : mobile sur un axe (O, i⃗), en O à t=0 ; chaque seconde abscisse +1 (probabilité 1/2) ou −1 (probabilité 1/2). 1) t=2 : a) P(abscisse 2) ; b) P(en O) ; 2) t=n : a) P(abscisse n) ; b) P(abscisse −n).
- **Act. 3** (p.88) : on lance n fois (n ≥ 1) un dé, A « obtenir au moins un 6 ». 1) p(A) pour n=3 ; 2) p(A) en fonction de n ; 3) nombre minimal de lancers pour p(A) ≥ 0.9.

**B/ I. La loi uniforme** (p.88–90)
- **Act. 1** (p.88) : 1) a) amplitude de I=[−1,1] ; b) f(x)=1/2 sur I : calculer ∫₋₁¹ f(x)dx ; c) pour tout [c,d] ⊂ [−1,1], 0 ≤ ∫꜀ᵈ f ≤ 1 ; 2) f constante sur [a,b] : a) valeur de f pour que ∫ₐᵇ f = 1 ; b) alors 0 ≤ ∫꜀ᵈ f ≤ 1 pour tout [c,d] ⊂ [a,b].
- **Act. 2** (p.89) : fléchette lancée au hasard sur cible circulaire de rayon 30 cm, d = distance centre–impact. 1) valeurs possibles de d ; 2) [0,30] partagé en 10 intervalles de même amplitude : a) amplitude ; b) d a-t-il plus de chances d'appartenir à un intervalle qu'à un autre ; c) probabilité (« selon vous ») que d ∈ [0,30], [4,5], [9,10]. Texte : « Dans l'activité précédente le réel d varie de façon aléatoire dans l'intervalle [0,30], mais de façon équirépartie. On dit alors que d est une variable aléatoire à valeurs dans [0,30]. »
- **Act. 3** (p.89) : mobile M sur un cercle de centre O, part de A, s'arrête au hasard ; α = angle entre [OA) et [OM) (figure) ; P probabilité uniforme sur [0,2π] ; calculer P(π/4 ≤ X ≤ π), P(π/4 ≤ X ≤ 3π/2), P(0 ≤ X ≤ π).
- **Act. 4** (p.90) : durée du trajet X ∈ [30,50] min, loi uniforme P. 1) P(30 ≤ X ≤ 40), P(30 ≤ X ≤ 43) ; 2) F(x) = 0 si x<30 ; P(30 ≤ X ≤ x) si x ∈ [30,50] ; 1 si x>50 : expression et représentation.

**B/ II. La loi exponentielle** (p.90–92)
- **Act. 1** (p.90) : λ > 0, f(t)=λe^{−λt} sur [0,+∞[. a) calculer ∫₀ˣ f(t)dt et lim_{x→+∞} ∫₀ˣ f(t)dt ; b) pour tout [c,d] ⊂ [0,+∞[, 0 ≤ ∫꜀ᵈ f ≤ 1.
- **Act. 2** (p.91) : durée de vie t (semaines) d'un appareil, loi exponentielle de paramètre 0.5 : probabilité que la durée de vie soit entre 100 et 200 semaines. Texte : « …On dit alors que t est une variable aléatoire qui suit la loi exponentielle de paramètre 0.5. »
- **Act. 3** (p.91) : X exponentielle de paramètre λ. 1) λ sachant P(X ≥ 10)=0.5 ; 2) P(0 ≤ X ≤ 10), P(100 ≤ X ≤ 300), P(X ≥ 300) ; 3) F(x)=0 si x<0, P(0 ≤ X ≤ x) si x ∈ [0,+∞[ : a) expression ; b) lim_{x→+∞} F(x) ; c) représentation.
- **Act. 4** (p.92) : X exponentielle de paramètre λ ; courbe de F donnée (figure : passe par ≈ (1 ; 0.85), graduations 1 et 2). 1) valeur approchée de λ à 10⁻¹ près ; 2) p(X ≥ 2).

### Cours — Encadrés (VERBATIM, relus sur l'image de leur page)

> **Définition — aléa numérique / variable aléatoire** (p.83) — « Soit (E, 𝒫(E), p) un espace probabilisé fini. On appelle aléa numérique ou variable aléatoire toute application X: E → ℝ. »
> **Notation** (p.83, texte hors encadré) — « L'événement {a∈E ; X(a)=xᵢ} est noté (X=xᵢ). L'ensemble X(E) désigne l'ensemble des valeurs prises par X. »

> **Définition — loi de probabilité** (p.83) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et X une variable aléatoire. On appelle loi de probabilité de X ou distribution de X, l'application P_X : X(E) → [0,1], xᵢ ↦ p(X=xᵢ). »

> **Conséquences** (p.84) — « Soit (E, 𝒫(E), p) un espace probabilisé fini. Si X est une variable aléatoire sur E telle que X(E)={x₁,x₂,…,xₙ}, alors Σᵢ₌₁ⁿ p(X=xᵢ)=1. » — **Démonstration** (hors encadré) : « Les parties (X=x₁), (X=x₂),… et (X=xₙ) forment une partition de E. On en déduit que Σᵢ₌₁ⁿ p(X=xᵢ)=p(E)=1. »

> **Définition — espérance** (p.84) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et X une variable aléatoire sur E telle que X(E)={x₁,x₂,…,xₙ}. On appelle espérance mathématique ou moyenne de X le nombre E(X)=Σᵢ₌₁ⁿ xᵢpᵢ. »

> **Théorème** (p.85) — « Soit (E, 𝒫(E), p) un espace probabilisé fini, X et Y deux variables aléatoires sur E. • Pour tout réel α, E(αX)=αE(X). • E(X+Y)=E(X)+E(Y). »

> **Définition — variance, écart-type** (p.85) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et X une variable aléatoire sur E. On appelle variance de X le nombre V(X)=E((X−E(X))²). On appelle écart-type de X le nombre σ(X)=√V(X). »

> **Propriété** (p.85) — « Soit (E, 𝒫(E), p) un espace probabilisé fini. Si X est une variable aléatoire sur E alors V(X)=E(X²)−(E(X))². »

> **Définition — fonction de répartition** (p.86) — « Soit (E, 𝒫(E), p) un espace probabilisé fini et X une variable aléatoire sur E. On appelle fonction de répartition de X, l'application définie de ℝ dans [0,1] par F: x ↦ p(X≤x). » (Image : « (X≤x) désigne l'ensemble {a∈E ; X(a)≤x} » est dit dans l'énoncé de l'Act. 1, hors encadré.)

> **Théorème et définition — loi binomiale** (p.87) — « Soit E une expérience aléatoire constituée de n épreuves identiques, indépendantes et n'ayant que deux issues : succès ou échec. Soit p la probabilité de l'événement succès. On considère la variable aléatoire X associant à cette expérience le nombre de succès réalisés au cours des n épreuves. Alors la loi de probabilité de X est donnée par : p(X=k)=C_nᵏ pᵏ (1−p)ⁿ⁻ᵏ, k∈{0, 1,…, n}. On dit que X suit une loi binômiale de paramètre (n,p). » — **Notation et vocabulaire** (p.87, hors encadré) : « La loi binomiale de paramètre (n,p) est notée B(n,p). Lorsque n=1, on dit que X suit une loi de Bernoulli. »

> **Espérance et variance** (p.88) — « Soit X une variable aléatoire suivant une loi binomiale B(n,p). Alors E(X)=np, V(X)=np(1−p) et σ(X)=√(np(1−p)). »

> **Définition — densité et probabilité uniformes** (p.88) — « Soit un intervalle [a,b] (a<b). La fonction f définie sur [a,b] par f(x)=1/(b−a) est appelée densité de la loi de probabilité uniforme sur [a,b]. On appelle probabilité uniforme sur [a,b] l'application qui à tout intervalle [c,d] inclus dans [a,b] associe le réel P([c,d])=∫꜀ᵈ f(x)dx. »

> **Conséquences** (p.89) — « Pour tout réel c de [a,b], P({c})=∫꜀꜀ f(x)dx=0. Si on désigne par [c,d]‾ le complémentaire de [c,d] dans [a,b], alors P([c,d]‾)=1−P([c,d]). » (figure : aire hachurée sous la droite y=1/(b−a) entre c et d, légende « l'aire de la partie hachurée est ∫꜀ᵈ 1/(b−a) dx »).

> **Définition — loi uniforme** (p.89) — « On dit qu'une variable aléatoire X à valeurs dans un intervalle [a,b] suit la loi de probabilité uniforme P si P(c≤X≤d)=(d−c)/(b−a). »

> **Définition — fonction de répartition (loi uniforme)** (p.90) — « Soit X une variable aléatoire qui suit la loi de probabilité uniforme P sur l'intervalle [a,b]. On appelle fonction de répartition de X, l'application F: ℝ→[0,1] définie par F(x)= 0 si x<a ; P(a≤X≤x) si x∈[a,b] ; 1 si x>b. » (figure : rampe de 0 à 1 entre a et b.)

> **Définition — densité et loi exponentielles** (p.90) — « Soit λ un réel strictement positif. La fonction f définie sur [0,+∞[ par f(t)=λe^{−λt} est appelée densité de loi exponentielle. On appelle loi de probabilité exponentielle de paramètre λ, l'application P qui • à tout intervalle [c, d] inclus dans [0,+∞[ associe le réel P([c, d])=∫꜀ᵈ λe^{−λx}dx, • à tout intervalle [c,+∞[ inclus dans [0,+∞[ associe le réel P([c,+∞[)=e^{−λc}. »

> **Conséquences** (p.91) — « 1. Pour tout réel c>0, P({c})=∫꜀꜀ f(x)dx=0. 2. Pour tout réel c>0, P([0,c])=∫₀ᶜ f(x)dx=1−e^{−λc}. 3. P([c,+∞[)=1−P([0,c]). »

> **Définition — loi exponentielle** (p.91) — « On dit qu'une variable aléatoire X suit la loi exponentielle de paramètre λ, si P(c≤X≤d)=∫꜀ᵈ λe^{−λx}dx=e^{−λc}−e^{−λd} et P(X≥c)=e^{−λc}. »

> **Définition — fonction de répartition (loi exponentielle)** (p.92) — « Soit X une variable aléatoire qui suit la loi de probabilité exponentielle P de paramètre λ. On appelle fonction de répartition de X, l'application F: ℝ→[0,1] définie par F(x)= 0 si x<0 ; P(0≤X≤x) si x∈[0,+∞[. » (figure : courbe croissante concave de 0 vers l'asymptote y=1.)

Pas d'autre encadré : aucune « Méthode », « Remarque » encadrée ni « Conseil » dans ces pages.

### QCM – VRAI-FAUX (p.93) — réponses non fournies

**QCM** (« Cocher la réponse exacte. », trois cases par question). **1.** X suit la loi binomiale de paramètre 3 et 1/3. a) La probabilité de l'événement X>2 est : (1/3)³ · (2/3)³ · C₃²(1/3)(2/3)² [exposants de la 3ᵉ case lus sur l'image : (1/3) et (2/3)² ; doute minime de lecture]. b) L'espérance de X est égale à : 1 · 2/3 · 1/3. c) Si F est la fonction de répartition de X alors F(1) est égal à : 7/27 · 20/27 · 6/27. **2.** X suit la loi exponentielle de paramètre 0.1 : l'arrondi au centième de p(X>10) est : 0.63 · 0.37 · 0.91.

**VRAI-FAUX** (« Répondre par vrai ou faux en justifiant la réponse. »). **1.** P(A)=0.2, expérience répétée huit fois, indépendamment : P(A réalisé au moins une fois)=1−(0.8)⁸. **2.** « Les situations de tirages sans remise obéissent à une loi binomiale. » **3.** « La probabilité de choisir au hasard un réel entre 0 et 0.0000001 est égale à 0. » **4.** X de loi exponentielle : p(0≤X≤2)=p(0<X≤2). **5.** Tableau de loi de X : xᵢ = −1, 0, 1 ; pᵢ = 0.25, 0.5, 0.25 : a) l'espérance de X est nulle ; b) la variance de X est nulle.

### Exercices et problèmes (p.94–96) — 19 exercices (numéros 1 à 19 encadrés sur l'image ; l'OCR les perd)

- **Ex. 1** (p.94) : 100 questions au programme, le candidat en a étudié 80, trois tirées au sort ; probabilité d'en avoir étudié : 1) les trois, 2) deux seulement, 3) une seule, 4) aucune, 5) au moins une.
- **Ex. 2** (p.94) : joueurs X (9/10) et Y (4/10) au tir à la cible ; X n'effectue qu'un tir sur trois ; un des joueurs tire et la cible est atteinte : probabilité que ce soit Y. [Probabilité conditionnelle : prérequis du ch.15.]
- **Ex. 3** (p.94) : dé cubique, trois faces « 1 », deux faces « 2 », une face « 3 », lancé deux fois ; X = somme. 1) loi ; 2) E(X), V(X) ; 3) F et sa courbe.
- **Ex. 4** (p.94) : sac de 10 jetons (4 rouges, 6 blancs), tirage sans remise un à un ; X = rang du premier rouge : loi, espérance, variance.
- **Ex. 5** (p.94) : deux dés identiques équilibrés ; X = plus grand, Y = plus petit. 1) lois de X et Y ; 2) E et V de X et de Y.
- **Ex. 6** (p.94) : standardiste répond à 90 % des appels, 10 appels : probabilité de répondre aux 10 ; à seulement 5 ; à au moins un.
- **Ex. 7** (p.94) : pièce jetée 20 fois. 1) nombre moyen de faces ; probabilité d'un nombre de faces 2) égal à 10, 3) entre 9 et 11, 4) entre 8 et 12, 5) entre 7 et 13.
- **Ex. 8** (p.94) : ampoule défectueuse avec probabilité 0.1, lot de 400 : moyenne et écart type de la distribution des pièces défectueuses.
- **Ex. 9** (p.94) : trois tétraèdres équilibrés (une face bleue, une jaune, deux rouges), lancés simultanément. 1) P(aucune face rouge visible) ; 2) P(aucune face bleue visible) ; 3) A « les six faces rouges sont visibles » : p(A) ; 4) expérience répétée n fois : p_n = P(A réalisé une et une seule fois).
- **Ex. 10** (p.95) : 1) deux dés non pipés, A₂ « total pair » : p(A₂) ; 2) trois dés, A₃ : p(A₃) ; 3) n dés, Aₙ : montrer par récurrence que la suite (p(Aₙ)) est constante.
- **Ex. 11** (p.95) : « Un billet sur deux est gagnant, achetez deux billets » (exactement un billet sur deux gagnant). 1) 100 billets, deux achetés : P(au moins un gagnant) ; 2) 2n billets, deux achetés, pₙ : a) montrer pₙ=(3n−1)/(4n−2) ; b) calculer p₁ et expliquer ; c) montrer 3/4 ≤ pₙ ≤ 1 ; 3) 3 jours, 2n billets/jour, deux achetés : a) qₙ = P(au moins un gagnant sur 3 jours) ; b) limite de (qₙ).
- **Ex. 12** (p.95) : loterie, chaque billet gagnant avec probabilité 1/100. 1) n billets, A « au moins un gagnant » : p(A) en fonction de n ; 2) n minimal pour p(A) > 0.5 (« supérieur »).
- **Ex. 13** (p.95) : lot de n pièces dont une défectueuse. 1) machine testant une à une ; n-ième test si seule la défectueuse reste ; X = nombre de tests : a) P(un seul test) ; b) P(exactement deux tests) ; c) loi de X ; d) E(X), V(X) (rappel : Σₖ₌₁ⁿ k² = n(n+1)(2n+1)/6) ; 2) un homme teste ; s'il ne reste que deux pièces il ne fait qu'un test de plus ; Y = nombre de tests : a) P(un seul test) ; b) P(exactement n−1 tests) ; c) loi de Y ; d) E(Y), V(Y).
- **Ex. 14** (p.95–96) : x choisi au hasard dans [0,1] : 1) P(x=0.1), P(x=0.0005), P(x=0.99999) ; 2) P(x ∈ [0.5,1]) ; 3) P(x ∈ [0.001,0.002]) ; 4) P(x plus petit que 0.99999) ; 5) P(x plus grand que 0.99999).
- **Ex. 15** (p.96) : bus toutes les 20 min, X = temps d'attente, loi uniforme sur [0,20] : P(2 à 5 min), P(10 à 13), P(exactement 3), P(moins de 3), P(plus de 3).
- **Ex. 16** (p.96) : durée de vie X (années) exponentielle de paramètre 0.2. 1) a) P(X=10), b) P(X≤10), c) P(X≥10) ; 2) réel c tel que P(X≤c)=P(X≥c).
- **Ex. 17** (p.96) : durée de vie (années) d'un robot jusqu'à la première panne, exponentielle de paramètre 0.0005 : P(durée entre 5 et 8 ans), P(dépasse 5 ans), P(dépasse 8 ans). [Doute : λ=0.0005 par an donne des probabilités ≈ 0.0015 et ≈ 0.9975 ; lu tel qu'imprimé.]
- **Ex. 18** (p.96) : cylindres ; écart X (dixièmes de mm) exponentielle de paramètre 1.5. 1) à 10⁻³ près P(X≤1), P(X≥2), P(1≤X≤2) ; règle : écart < 1 accepté ; entre 1 et 2 rectification, accepté dans 80 % des cas ; > 2 refusé ; 2) cylindre prélevé : a) P(accepté) ; b) sachant accepté, P(rectifié).
- **Ex. 19** (p.96) : durée de vie X (années) jusqu'à la première panne, exponentielle de paramètre λ. 1) λ à 10⁻¹ près pour P(X>6)=0.3 ; ensuite λ=0.2 : 2) instant t, à un mois près, où la probabilité de première panne est 0.5 ; 3) P(pas de panne dans les deux premières années) ; 4) lot de cinq machines indépendantes : P(au moins une sans panne durant les deux premières années).

### Écart avec la référence

**Référence principale** : le plus proche est en réalité **bac-math ch. 18 « Probabilités » (manuel 222446, p.191–201), parties V–VIII et B/I–II** : le texte du manuel 222434 en est une **reprise quasi mot pour mot** (mêmes activités, mêmes encadrés, mêmes figures, mêmes notations (E, 𝒫(E), p)). Le chapitre bac-techniques 15 (manuel 222451, p.331–365) est d'une autre rédaction, plus riche.

*À EXCLURE (la référence bac-techniques 15 l'enseigne, ce manuel NON)* : univers Ω fini avec « variable aléatoire réelle » rédigée Ω → ℝ ; vocabulaire « variable discrète », tableau de la loi, conseil Σ pᵢ = 1 comme règle de méthode ; **propriétés générales de F** (en escalier, continue à droite, croissante, F(x) par intervalles) ; remarque « jeu favorable / équitable / défavorable » (signe de E(X)) ; **épreuve de Bernoulli, schéma de Bernoulli**, variable de Bernoulli de paramètre p ; **variable aléatoire continue** (X(Ω)=I, p(X=a)=0), F continue, **densité = dérivée de F**, p(x ≤ X ≤ x+h) ≃ f(x)·h, propriétés de la densité ; **E(X) et V(X) des lois continues** (E=(a+b)/2, V=(b−a)²/12 ; E=1/a, V=1/a²) ; **absence de mémoire** p(X>s+t | X>s)=p(X>t) ; F(x)=1−e^{−ax} énoncée comme propriété ; résumé du cours ; usage de logiciels ; aperçu historique ; exercices type bac tunisien avec années (« D'après Bac Tunisien »).

*À EXCLURE (la référence bac-math 18 l'enseigne, ce manuel NON)* : toute la partie probabilités préalable (expériences aléatoires, probabilité sur un ensemble fini, équiprobabilité, probabilité conditionnelle, indépendance, probabilités totales, arbres pondérés : parties I–IV, p.180–191 — enseignées au ch.15 de cette section, réinvestissables comme prérequis, voir ✅) ; exercices résolus 1 à 4 de ce chapitre ; QCM/VF sur arbres et indépendance ; exercices 2, 4–7, 9–12, 20, 23, 25 de bac-math (sondages, arbres, chaînes à deux états, suites arithmético-géométriques, jeu de pile ou face à gain).

*Ce manuel a EN PLUS* : par rapport à bac-math 18 : « Conséquences Σ p(X=xᵢ)=1 » avec **démonstration** (partition) ; ce qui est « Activité 3 » (concours, 3 candidats) en bac-math devient ici **Exercice résolu 1** avec solution imprimée ; QCM 1 b) et c) (espérance, F(1) de B(3, 1/3)) ; Vrai-Faux 4 (loi exponentielle, P(0≤X≤2)=P(0<X≤2)) et 5 (tableau à trois valeurs −1, 0, 1 : E et V) ; **Ex. 6** (standardiste, loi binomiale) absent de bac-math ; énoncés d'exercices répartis sur 19 numéros dont 18 recoupent bac-math (correspondance : Ex.1→bm3, 2→bm8, 3→bm13, 4→bm14, 5→bm15, 7→bm16, 8→bm17, 9→bm18, 10→bm19, 11→bm21, 12→bm22, 13→bm24, 14→bm26, 15→bm27, 16→bm28, 17→bm29, 18→bm30, 19→bm31). Par rapport à bac-techniques 15 : rien de nouveau hors QCM/VF et Ex. 6.

*Points d'attention* : (1) l'Ex. 2 suppose une probabilité conditionnelle (formule de Bayes / probabilités des causes), enseignée au ch.15 (prérequis) ; Ex. 18 2b est du même type ; (2) l'espérance/variance des lois uniforme et exponentielle ne sont pas définies : aucune question ne doit les exiger ; (3) Ex. 17 : λ=0.0005 (unité par an), valeur imprimée telle quelle.

### Bornes de scope

- ✅ INCLUS : prérequis du ch.15 réinvestissables (probabilité conditionnelle, indépendance, probabilités totales) : Ex. 2 et Ex. 18 2b ; variable aléatoire X : E → ℝ sur un espace probabilisé fini (E, 𝒫(E), p), événement (X=xᵢ), loi de probabilité (tableau, vérification Σ=1) ; espérance E(X)=Σxᵢpᵢ, linéarité E(αX)=αE(X) et E(X+Y)=E(X)+E(Y) (énoncée sans preuve), variance V(X)=E((X−E(X))²), écart-type σ=√V, V=E(X²)−(E(X))² ; fonction de répartition F : x ↦ p(X≤x) (calcul par morceaux, tracé en escalier, lecture graphique de p(X≤a), p(X<a), p(X=a), p(a≤X≤b)) ; loi binomiale B(n,p) (théorème-définition, loi de Bernoulli pour n=1, E=np, V=np(1−p), σ=√(np(1−p)), calculs de p(X=k), « au moins un » 1−(1−p)ⁿ, plus petit n) ; loi uniforme sur [a,b] (densité 1/(b−a), P([c,d])=(d−c)/(b−a), P({c})=0, complémentaire, F en rampe) ; loi exponentielle de paramètre λ (densité λe^{−λt}, P(c≤X≤d)=e^{−λc}−e^{−λd}, P(X≥c)=e^{−λc}, P([0,c])=1−e^{−λc}, F, déterminer λ à partir d'une donnée ou d'un graphique de F, lim F=1) ; calcul d'intégrales ∫λe^{−λx}dx et ∫ de constante ; problèmes de modélisation (urnes, dés, pièces, durées de vie, tirs, loteries) ; suites et limites dans Ex. 11 et récurrence dans Ex. 10 (réinvestissement).
- ⛔ EXCLU : variable aléatoire continue générale (X(Ω)=I, p(X=a)=0 comme théorème), densité comme dérivée de F, p(x≤X≤x+h) ≃ f(x)·h ; **E(X) et V(X) des lois continues** (uniforme, exponentielle) ; absence de mémoire ; propriétés générales de F (croissante, continue à droite, F en escalier énoncée comme théorème) ; schéma de Bernoulli formalisé ; jeu équitable/favorable ; démonstration de E(X)=np, V(X)=np(1−p), de la linéarité de E et de V=E(X²)−(E(X))² ; loi normale (la page de garde la suggère par « courbe de Gauss » mais aucun contenu), Poisson, loi géométrique nommée, inégalité de Bienaymé–Tchebychev, loi des grands nombres, indépendance de variables aléatoires, covariance ; logiciels (Excel, Sine qua non) ; aperçu historique.

### Lecture

- **Pages lues par l'OCR** (couche texte, /root/.cache/yqa-manuels/222434/txt) : p.82 à p.96, soit 15 pages sur 15.
- **Pages lues sur l'image** (pdftoppm -r 110) : **15 pages — 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96** (toutes les pages du chapitre ; toute page à formule, encadré, tableau ou figure relue ; sondage de 100 % donc ≥ 1 page sur 10).
- **Écarts OCR/image constatés** : (1) p.83–85 : encadrés mathématiques très dégradés par l'OCR (E→ℝ rendu « E —R », 𝒫(E) absent, « Σp(x=x;} », V(X)=E((X−E(X))²) en « f(x −E(x))) », E(αX) en « E(aX)… ») ; relus et rétablis sur image. (2) p.84 : exposants de l'Exercice résolu 1 ((1−p)²p, (1−p)³) et de la remarque finale perdus ; relus sur image. (3) p.86 : l'OCR rend « p(X<x) » (« ≤ » perdu) dans la définition de F ; la figure en escalier de l'Act. 1 est absente du texte ; « p(1≤X≤6) » rendu « p(i<X<6) ». (4) p.87 : OCR « cp" (1-p)" * » pour C_nᵏpᵏ(1−p)ⁿ⁻ᵏ ; les probabilités 1/2 et 1/2 de l'Act. 2 manquantes dans l'OCR (vues sur l'image). (5) p.88 : f(x)=1/2, bornes d'intégrales et densité 1/(b−a) perdues par l'OCR. (6) p.89 : figure de l'aire hachurée et du cercle absentes ; « ≤ » rendus « < ». (7) p.90–91 : définition exponentielle OCR « A6 À » pour λe^{−λt} ; « P(X≥10)=0.5 » lu « P(X>10) » dans l'OCR ; ≥ perdus. (8) p.93 : options de QCM (fractions, puissances), tableau de loi, tous perdus ou dégradés dans l'OCR ; relus sur image. (9) p.94–96 : **numéros d'exercices 1 à 19 entièrement absents de l'OCR** (cadres) ; deux colonnes lues dans le bon ordre par l'OCR mais Ex. 14 coupé entre p.95 et p.96 ; formules de l'Ex. 11 (3n−1)/(4n−2) et 3/4 ≤ pₙ ≤ 1 et de l'Ex. 13 Σk² dégradées ; ordre rétabli sur image. (10) Aucun mot ni nombre faux dans les énoncés une fois relus sur image ; coquilles imprimées conservées : « binômiale » (p.87), « plus gand » (Ex. 14), « supérieur » (Ex. 12), « soit réalisé » (Ex. 9).

## 2.17 Chapitre 17 — Statistiques (manuel 222434, p.97–119)

**Page de garde (p.97)** — Bandeau « Chapitre 7 » (numérotation interne du manuel ; c'est le chapitre 17 de la fiche ; **dernier chapitre du manuel : p.119 = dernière page du PDF**), titre « Statistiques ». Encart historique (titre imprimé : « Huygens (1669) : Espérance de vie. ») : « "Par les observations faites à Londres avec beaucoup d'exactitude. De 100 personnes conçues, il en meurt [...]. Donc, de 100 personnes, ceux qui atteignent l'âge de 6 ans sont 64, de 16 ans sont 40, de 26 ans sont 25, de 36 ans sont 16, de 46 ans sont 10, de 56 ans sont 6, de 66 ans sont 3, de 76 ans est 1 et de 86 ans est 0. Qui gagerait qu'un enfant conçu virait jusqu'à 6 ans, peut mettre 64 contre 36 ou 16 contre 9. Et qui gagerait [...]. De 100 enfants conçus, il en meurt 36 avant l'age de 6 ans, lesquels on peut dire ont vécu l'un portant l'autre 3 ans. Des 64 restants, il en meurt 24 avant l'âge de 16 ans [...]." Une correspondance de Huygens sur la statistique démographique. Huygens aboutit au total 1822 en multipliant 36 par 3, 24 par 11, jusqu'à 1 par 81 et en ajoutant tous les produits ainsi obtenus puis calcul le quotient de 1822 par 100 et déclare :" Et le quotient qui est ici 18 ans et environ 2 mois et demi, ce n'est pas à dire qu'il soit apparent qu'il vivra si longtemps, car il est beaucoup plus apparent qu'il mourra avant ces termes." » — « (J Dhombres et al, Mathématiques au fil des âges, 1987). »

**Plan du chapitre** — le manuel n'imprime **aucun** encadré « Plan du chapitre » (ni Résumé, ni Aperçu historique, ni rubrique « Avec l'ordinateur », ni QCM / Vrai-Faux). Plan reconstitué des titres imprimés : **I. Distributions marginales** (p.98–100) · **II. Covariance d'une série statistique double** : II.1 Cas d'un échantillon simple (p.100–102), II.2 Cas d'un échantillon groupé (p.102–105) · **III. Ajustement d'une série statistique double** (p.105) : III.1 Méthode de Mayer (p.106–107), III.2 Méthode d'ajustement par les moindres carrés (p.107–110), III.3 Coefficient de corrélation linéaire (p.110–111), III.4 Exemple d'ajustement non affine (p.111–113) · **Exercices et problèmes** (p.114–119). Texte liminaire (p.98) : « Il arrive que l'on soit amené à effectuer deux séries de mesure X et Y sur un même échantillon composé de n individus et que l'on s'interroge sur les relations possibles entre ces mesures. On dit alors que l'on a une série statistique double (X,Y). » Notation : X̄, Ȳ ; σ_X, σ_Y ; V(X) ; cov(X,Y) ; ρ_XY. Les « Utilisation d'une calculatrice » (p.104, p.112) sont des rubriques du cours. Numérotation des activités **telle qu'imprimée** (elle repart de 1 à chaque sous-partie ; voir « Écart »).

### Cours — Activités (numérotation imprimée)

**I. Distributions marginales**
- **Act. 1** (p.98) : tableau double entrée, intensité de travail X (kJ/min : 9.6, 12.8, 18.4, 31.2, 36.8, 47.2, 49.6, 56.8) × fréquence cardiaque Y (70, 86, 90, 104), 100 personnes ; totaux X = 9, 13, 30, 21, 13, 6, 4, 4 ; totaux Y = 6, 21, 28, 45 ; le « 12 » encadré = case (X = 18.4, Y = 104). 1.a signification du 12 ; b nb d'individus Y > 100 ; c nb d'individus X > 49 ; d nb avec X > 49 ET Y > 100. 2. distribution marginale de X, puis X̄ et σ_X. 3. idem Y.
- **Act. 2** (p.99) : 20 voitures, distance X (mille km) avant la 1re grande panne et puissance Y (chevaux) : (42,4) (55,5) (57,6) (81,6) (64,4) (70,7) (75,6) (58,5) (61,4) (65,5) (48,4) (58,4) (65,4) (72,6) (75,4) (80,7) (65,7) (73,5) (43,6) (61,5). 1.a valeurs prises par Y ; b Ȳ et σ_Y. 2. compléter le tableau des effectifs par classes de distance (Moins de 50 ; [50,60[ ; [60,70[ ; 70 et plus). 3. pourcentage des voitures ayant parcouru < 60 000 km ET de puissance ≥ 6 chevaux.
- **Act. 3** (p.100) : poids X (kg ; [40,45[ [45,50[ [50,55[ [55,60[) × taille Y (cm ; [120,155[ [155,160[ [160,165[ [165,170[), effectifs 20 9 1 0 / 2 18 4 1 / 0 5 12 6 / 0 1 7 14 ; marges effectif/fréquence (taille 30, 25, 23, 22 ; 0.30, 0.25, 0.23, 0.22 ; poids 22, 33, 24, 21 ; 0.22, 0.23 [sic, 33/100 = 0.33], 0.24, 0.21 ; total 100). 1. distributions marginales de X et de Y. 2. X̄, σ_X. 3. Ȳ, σ_Y.

**II.1 Échantillon simple**
- **Act. 1** (p.100–101) : exportations X et importations Y mensuelles de la Tunisie en 2006 (12 mois, de Janvier (1081.1 ; 1312.1) à Décembre (1347.3 ; 1660.6)). 1. taille de l'échantillon. 2.a X̄, σ_X ; b Ȳ, σ_Y. 3. calculer (1/12)Σ_{i=1}^{12} xᵢyᵢ − X̄Ȳ.
- **Act. 2** (p.101) : logements, X (milliers) = 1313.1, 1512.3, 1870.1, 2204.3, 2501.0 ; Y logements modernes = 265.2, 343.3, 630.2, 848.7, 1128.0 (années 1984, 1989, 1994, 1999, 2004). 1. nuage de points. 2.a X̄, Ȳ ; b cov(X,Y), interpréter.
- **Act. 3** (p.102) : graphique de 5 points M(X,Y), X = nombre de logements (1313, 1512.3, 1870.1, 2204.3, 2501.0), Y = % de logements traditionnels (≈ 71, 72.4, 63.6, 60.3, 54.1) : signe de cov(X,Y) ?

**II.2 Échantillon groupé**
- **Exercice résolu** (p.102–104) : poids Y (kg) de 63 nouveaux-nés (]1.5,2.5], ]2.5,3.5], ]3.5,4.5]) × poids maternel X (]40,50], ]50,60], ]60,70], ]70,80]) ; effectifs 1 0 1 0 / 11 17 13 2 / 4 4 8 2 ; totaux colonnes 16, 21, 22, 4 ; lignes 2, 43, 18 ; 63. 1. X̄, σ_X, Ȳ, σ_Y. 2. cov(X,Y), interpréter. Solution : centres 45, 55, 65, 75 ; nᵢ = 16, 21, 22, 4 ; Σnᵢxᵢ = 3605 ; Σnᵢxᵢ² = 211375 ; X̄ ≃ 57.2222 ; V(X) = (1/63)Σnᵢxᵢ² − (X̄)² ≃ 80.776 ; σ_X ≃ 8.9875 ; yⱼ = 2, 3, 4 ; nⱼ = 2, 43, 18 ; Σnⱼyⱼ = 205 ; Σnⱼyⱼ² = 683 ; Ȳ ≃ 3.2539 ; V(Y) ≃ 0.2529 ; σ_Y ≃ 0.5029 ; 10 couples distincts (45,2) (45,3) (45,4) (55,3) (55,4) (65,2) (65,3) (65,4) (75,3) (75,4), effectifs 1, 11, 4, 17, 4, 1, 13, 8, 2, 2 ; produits nᵢⱼxᵢyⱼ = 90, 1485, 720, 2805, 880, 130, 2535, 2080, 450, 600 ; ΣΣnᵢⱼxᵢyⱼ = 11775 ; cov(X,Y) = (1/63)×11775 − X̄Ȳ ≃ 0.7 ; « La covariance est positive donc X et Y ont tendance à varier dans le même sens. »
- **Utilisation d'une calculatrice** (p.104) : MODE puis 1 ; sous-mode statistique à deux variables ; saisie xᵢ STO yⱼ STO nᵢⱼ M+ (ex. 55 STO 3 STO 17 M+) ; RCL n → 63 ; RCL Σx → 3605 ; RCL Σx² → 211375 ; RCL X̄ → 57.22222222 ; RCL σ_X → 8.987547725 ; RCL σ_X x² → 80.77601411 (V(X)) ; RCL Σxy → 11775 ; RCL Σxy ÷ 63 − (RCL X̄ × RCL Ȳ) → 0.705467372 (cov(X,Y)). Touches propres à un modèle (indicatif).
- **Act. 4** (p.105) : 100 ménages, nombre d'enfants X (0 à 5) × revenu du chef de famille Y en DT (Moins de 200 ; [200,400[ ; [400,600[ ; [600,800[) ; effectifs 6 4 1 0 0 0 (11) / 3 11 10 5 1 0 (30) / 1 3 16 13 4 1 (38) / 0 1 3 5 8 4 (21) ; totaux 10, 19, 30, 23, 13, 5. 1.a ménages à 4 enfants et revenu > 600 ; b sans enfant et revenu < 200 ; c moins de 4 enfants et revenu entre 400 et 600. 2.a X̄, σ_X ; b Ȳ, σ_Y. 3.a peut-on prévoir le signe de cov(X,Y) ? b calculer cov(X,Y).

**III. Ajustement** (texte p.105, voir encadrés) — **III.1 Mayer**
- **Act. 1** (p.106) : commerce extérieur de la Tunisie, importations X et exportations Y (M DT) de 1990 à 2004 (15 années : (4826.4 ; 3087.4) (4788.9 ; 3417.1) (5688.8 ; 3549.7) (6172.1 ; 3760) (6647.3 ; 4696.6) (7464.3 ; 5172.5) (7498.8 ; 5372) (8793.5 ; 6147.9) (9489.5 ; 6518.3) (10070.5 ; 6966.9) (11738 ; 8004.8) (13697.3 ; 9536.2) (13510.9 ; 9748.6) (14038.9 ; 10342.6) (15960.3 ; 12054.9)). 1.a X̄, σ_X ; b Ȳ, σ_Y. 2. nuage fourni : placer G(X̄,Ȳ). 3. scinder en (I) 1990–1997 et (II) 1998–2004, G₁ et G₂ : a coordonnées, vérifier G, G₁, G₂ alignés, tracer (G₁G₂) ; b répartition des points autour de (G₁G₂) ; c ajustement affine de (X,Y) ; d estimer les exportations pour une importation de 17000.
- **Act. 2** (p.107) : mur béton + polystyrène d'épaisseur X (cm), résistance thermique R (m².°C/W) : (2 ; 0.83) (4 ; 1.34) (6 ; 1.63) (8 ; 2.3) (10 ; 2.44) (12 ; 2.93) (14 ; 3.44) (16 ; 3.85) (18 ; 4.28). 1. nuage (X,R). 2. ajustement affine de R en X par Mayer. 3. résistance espérée pour 25 cm.

**III.2 Moindres carrés** — texte p.107 : nuage Mᵢ(xᵢ,yᵢ), droite D : y = ax + b, Hᵢ(xᵢ,zᵢ) point de D de même abscisse que Mᵢ (figure : M₁…M₄, H₁…H₄ projetés verticalement).
- **Act. 3** (p.108) : chiffre d'affaires annuel (mille DT), rang X = 1..8, Y = 13.6, 15, 15.8, 17, 18, 20, 19, 20. 1.a nuage ; b ajustement affine justifié ? 2. point moyen G. 3.a tracer D : y = 1.6x + 10.1 ; b S_D = Σ_{i=1}^{8}[yᵢ − (1.6xᵢ + 10.1)]². 4. droite Δ par Mayer : a équation y = ax + b (a, b à 10⁻¹ près) ; b S_Δ = Σ[yᵢ − (axᵢ + b)]². 5. comparer S_D et S_Δ. 6. estimer le chiffre d'affaires de la 10ᵉ année.
- **Act. 1** (p.109–110) : poids X (kg) et surface corporelle Y (m²) de 15 sujets : (15 ; 0.58) (20 ; 0.7) (25 ; 0.8) (29 ; 0.9) (34 ; 1) (39 ; 1.1) (44 ; 1.2) (50 ; 1.3) (55 ; 1.4) (60 ; 1.5) (65 ; 1.56) (70 ; 1.64) (74 ; 1.74) (80 ; 1.8) (85 ; 1.9). 1.a X̄, σ_X ; b Ȳ, σ_Y. 2. covariance de (X,Y). 3. nuage fourni : a placer G ; b répartition ; c ajustement affine par les moindres carrés. 4. surface corporelle d'un sujet de 62 kg.

**III.3 Coefficient de corrélation** (texte p.110, voir encadrés)
- **Act. 4** (p.111) : population scolaire de 3ᵉ année secondaire, octobre 1997 à 2002 : X = 1997…2002 ; Y = 67755, 74581, 79266, 76138, 80123, 90087. 1. coefficient de corrélation linéaire. 2. ajustement par moindres carrés, estimation pour octobre 2010.
- **Act. 5** (p.111) : voitures, puissance Y (20, 25, 30) × durée des pneumatiques X (2, 3, 4 milliers de km) ; effectifs 0 8 30 (38) / 5 20 7 (32) / 25 3 2 (30) ; totaux 30, 31, 39 ; 100. 1. coefficient de corrélation. 2. ajustement par moindres carrés justifié ?

**III.4 Ajustement non affine**
- **Exercice résolu** (p.111–112) : personnel paramédical tunisien du secteur public, 1990–2005 (23743, 24555, 25070, 25291, 25466, 25874, 26130, 26369, **26676** [année imprimée « 19989 » [sic] pour 1998], 27050, 27392, 30292, 28629, 29976, 29584, 29607). 1. années numérotées 0 à 15 : valeurs de (X, ln Y). 2. Z = ln Y : a coefficient de corrélation, justifier l'ajustement affine de (X,Z) ; b droite de régression de Z en X. 3. nombre de paramédicaux en 2010. Solution : tableau xᵢ, yᵢ, zᵢ = ln(yᵢ), xᵢ², zᵢ², xᵢzᵢ (z₀ = 10.075 … z₁₅ = 10.295) ; X̄ = 7.5, σ_X ≃ 4.6, Z̄ ≃ 10.199, σ_Z ≃ 0.074, Cov(X,Z) ≃ 0.326, ρ_XZ ≃ 0.960 ; « Le coefficient de corrélation est très proche de 1 / L'ajustement est donc justifié. » ; z = (0.326/(4.61)²)(x − 7.5) + 10.199, soit z = 0.015(x − 7.5) + 10.199 ; 3. « e^{0.015(20−7.5)+10.199} ≃ 32419 ».
- **Utilisation d'une calculatrice** (p.112) : « Dans cet exercice la série est à données simples. » saisie xᵢ STO yᵢ M+ ; RCL r (corrélation) ; RCL b (pente de la droite de régression de Y en X) ; RCL a (ordonnée à l'origine).
- **Act. 6** (p.113) : résistance à l'avancement R (kW) d'un poids lourd selon la vitesse V (km/h) : V = 10…90 (pas 10) ; R = 2.6, 5.8, 9.9, 15.4, 23.6, 34.5, 49, 67.2, 89.1. 1. tableau de (X,Y), X = V² et Y = R/V. 2. coefficient de corrélation de (X,Y) et droite de régression de Y en X. 3. relation entre R et V. 4. R pour V = 100 km/h.

### Exercices et problèmes (p.114–119) — numéros imprimés 1 à 12, puis 15 (**13 et 14 absents : le manuel passe de 12 à 15, la dernière page 119 est contiguë**)
- **Ex. 1** (p.114) : quatre nuages (1. en V ; 2. décroissant allongé ; 3. croissant incurvé ; 4. décroissant hyperbolique) : le nuage justifie-t-il un ajustement affine ?
- **Ex. 2** (p.114) : poids de 12 pères X et fils aînés Y : (65,63) (63,61) (67,66) (64,62) (68,67) (62,60) (70,69) (66,65) (68,67) (67,67) (69,66) (71,70). 1. nuage ; 2. Mayer ; 3. poids du fils aîné d'un père de 77 kg.
- **Ex. 3** (p.114–115) : nombre de médecins en Tunisie 1990–2003, X = 1..14, Y = 4425, 4500, 5099, 5257, 5344, 5965, 6177, 6464, 6819, 7149, 7444, 7767, 7964, 8189. 1. nuage ; 2. point moyen G ; 3. Mayer ; 4. estimation pour 2010.
- **Ex. 4** (p.115) : 100 ménages, X pièces habitées (1 à 4) × Y enfants (0 à 4) : 6 2 1 0 0 (9) / 5 12 8 1 1 (27) / 2 7 15 11 3 (38) / 0 1 8 14 3 (26) ; totaux 13, 22, 32, 26, 7. 1.a X̄, σ_X ; b Ȳ, σ_Y. 2.a coefficient de corrélation ; b ajustement affine justifié ?
- **Ex. 5** (p.115) : grue, longueur de flèche X (m) = 9, 10, 12, 14, 16, 18, 20, 22 ; charge max Y (t) = 1.4, 1.25, 1, 0.84, 0.7, 0.62, 0.55, 0.5. Réponses à 10⁻² près : a nuage ; b corrélation ; c droite de régression de Y en X, la construire ; d charge max pour une flèche de 23 m.
- **Ex. 6** (p.115–116) : 11 cliniques C₁…C₁₁, lits X / postes non médicaux Y : (122,185) (177,221) (77,114) (135,164) (109,125) (88,118) (185,193) (128,160) (120,151) (146,172) (100,150). 1. nuage ; 2. corrélation ; 3. droite de régression de Y en X (coefficients à 10⁻¹ près), la tracer ; 4. clinique de 35 lits : personnel non médical à embaucher (avec le résultat de 3).
- **Ex. 7** (p.116) : A/ club créé en 1999 (600 adhérents), rang X = 0..6, Y = 600, 690, 794, 913, 1045, 1207, 1380 ; Z = ln Y. 1.a vérifier l'ajustement affine par moindres carrés de (X,Z) ; b prévision 2006. 2. justifier Y ≃ 602 × (1.15)^X. B/ le club a compté 2400 adhérents en 2006 ; f(x) = 3600/(1 + 0.5e^{−x}) sur ℝ₊, adhérents en 2006 + n = f(n). 1. limite de f(n) en +∞, interpréter. 2.a tableau 2007…2011 (n = 1..5 ; f(1) = 3040) ; b moyenne M des adhérents prévus 2007–2011. 3. valeur moyenne f̄ de f sur [0.5, 5.5].
- **Ex. 8** (p.116) : 16 jeunes filles, taille X / poids Y : (160,46) (165,48) (167,48) (160,46) (168,49) (170,51) (160,45) (162,45) (165,48) (170,49) (170,51) (168,50) (172,50) (165,48) (165,47) (170,50). 1.a nuage ; b ajustement justifié ? 2.a corrélation ; b droite de régression de Y en X ; c masse pour 180 cm. 3. loi de Lorentz M = (T − 100) − (T − 130)/2 : estimer la masse pour 180 cm.
- **Ex. 9** (p.117) : onze élèves de 7ᵉ année de base, rayon X (cm) = 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7 ; aire Y (cm²) = 12, 20, 28, 38, 50, 64, 78, 95, 113, 133, 154. 1. proportionnelles ? 2. Z = √Y : a nuage (X,Z) (Z à 10⁻¹ près) ; b ρ_XZ, interpréter ; c droite de régression de Z en X (10⁻¹ près) ; d en déduire une valeur approchée de π.
- **Ex. 10** (p.117) : quantité X = 350, 400, 450, 500, 550, 600 ; prix Y (DT) = 140, 120, 100, 95, 85, 70. 1. ρ_XY ; 2. droite de régression de Y en X (10⁻¹ près) ; 3. recette r(x) : a montrer r(x) = (226.5 − 0.3x)x ; b variations de f(x) = −0.3x² + 226.5x sur ℝ₊ ; c prix de vente de recette maximale, recette maximale.
- **Ex. 11** (p.117–118) : population d'une ville, rang X = 0, 5, 10, 15, 20, 25, 30 (années 1975…2005), Y (milliers) = 18, 21, 25, 30, 36, 42, 50 ; nuage fourni. A/ 1. corrélation ; 2.a droite de régression de Y en X ; b la tracer ; c estimation en 2008 à un millier près. B/ 1. f(x) = ae^{bx} sur [0,+∞[, f(0) = 18, f(30) = 50 (b au millième) ; 2. estimation en 2008 ; 3. tracer la courbe ; 4. population réelle 2008 = 55 milliers : quel ajustement est le plus pertinent ? C/ f(x) = 18e^{0.034x} : 1. valeur moyenne f̄ sur [0,30] (au dixième) ; 2. lecture graphique de l'année où la population atteint f̄.
- **Ex. 12** (p.118) : population d'un pays 1965–2000, T = 0, 5, …, 35 ; P (millions) = 8, 8.9, 9.9, 11, 12, 13.5, 15, 16.6. A/ 1. nuage (2 cm pour 5 ans ; ordonnées : 8 à l'origine, 2 cm pour 1 million) ; 2. Y = ln P : a corrélation de (T,Y) à 10⁻³ près par défaut ; b droite de régression de Y en T (coefficients à 10⁻³) ; c expression de P en fonction de T. B/ f(t) = 8.e^{0.02t} sur [0,35] : 1. variations, tableau ; 2. courbe (C) ; 3. I = ∫₀³⁵ f(t)dt : a valeur approchée à 10⁻² ; b population moyenne m, la représenter ; 4. rapport (f(t+1) − f(t))/f(t), interprétation en pourcentage ; 5. année où la population aurait dépassé 19 millions.
- **Ex. 15** (p.119) : diamètre D (cm) d'une tige après T semaines : T = 0, 2, 6, 8, 10, 12 ; D = 0.4, 1.2, 5.4, 5.8, 6.4, 6.9. 1. nuage ; 2. U = ln(8/D − 1) : a corrélation de (T,U) ; b droite d'ajustement de U en T par moindres carrés ; c vérifier D(t) = 8/(1 + ce^{−at}) (a et c à préciser) ; 3.a tracer f : t ↦ D(t), t ≥ 0 ; b le diamètre dépassera-t-il 8 cm ?

### Cours — Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Définitions** (p.99) — « Soit (X,Y) une série statistique double sur un échantillon de taille n et soit (xᵢ,yᵢ)_{1≤i≤n} les valeurs numériques prises respectivement par les variables X et Y. La distribution marginale de la variable X est la distribution des valeurs (xᵢ)_{1≤i≤n} prises par la variable X. La distribution marginale de la variable Y est la distribution des valeurs (yᵢ)_{1≤i≤n} prises par la variable Y. »

> **Moyenne, variance, écart-type** (p.99, second encadré, sans titre) — « Soit X une série statistique sur un échantillon de taille n. Si X̄, V(X) et σ_X désignent respectivement la moyenne, la variance et l'écart-type de la série, alors X̄ = (1/n)Σ_{i=1}^{p} nᵢxᵢ, V(X) = (1/n)Σ_{i=1}^{p} nᵢ(xᵢ − X̄)², σ_X = √V(X), où les valeurs x₁, x₂,..., x_p désignent les valeurs distinctes prise par la variable X si elle est discrète, ou les centres des classes si la variable X est continue. L'entier nᵢ désigne l'effectif de la valeur xᵢ. »

> **Définition (covariance, échantillon simple)** (p.101) — « Soit (X,Y) une série statistique double sur un échantillon de taille n. On appelle covariance de (X,Y) le réel, noté cov(X,Y) défini par cov(X,Y) = (1/n)Σ_{i=1}^{n} xᵢyᵢ − X̄Ȳ, où (xᵢ,yᵢ) est la valeur observée pour l'individu i si X et Y sont discrètes, ou le centre de la classe si l'une des variables est continue. » Hors encadré : « Il découle de la définition que cov(X,Y) = cov(Y,X). »

> **Interprétation de la covariance** (p.101, texte sous titre, hors encadré) — « La covariance mesure la tendance qu'ont les variables X et Y à varier ensemble. La covariance est positive si X et Y ont tendance à varier dans le même sens. La covariance est négative si X et Y ont tendance à varier en sens contraire. »

> **Définition (covariance, échantillon groupé)** (p.102) — « Soit (X,Y) une série statistique double de taille n. Soit nᵢⱼ le nombre de fois qu'apparaît le couple (xᵢ,yⱼ). Alors cov(X,Y) = (1/n)Σ_{j=1}^{q}Σ_{i=1}^{p} nᵢⱼxᵢyⱼ − X̄Ȳ. »

> **Ajustement affine** (p.105, texte hors encadré) — « [...] le statisticien essaiera de trouver une fonction f qui modélise le phénomène étudié, grâce à la relation Y = f(X). Dans ce cas, on dit que X est la variable explicative et Y est la variable expliquée. La fonction f cherchée dépendra de l'allure du nuage de points. Si le nuage de point a l'allure d'une droite, le statisticien essaiera de trouver une fonction affine f qui sera la plus proche des points du nuage. On dit que le statisticien effectue un ajustement affine. Par conséquent faire un ajustement affine consiste à déterminer deux réels a et b tels que Y = aX + b soit un modèle acceptable du phénomène étudié. La droite d'équation y = ax + b sera appelée droite d'ajustement affine de Y en X. »

> **Définition (nuage de points, point moyen)** (p.107) — « Soit (X,Y) une série statistique double de valeurs (xᵢ,yᵢ)_{1≤i≤n}. L'ensemble des points Mᵢ de coordonnées (xᵢ,yᵢ) dans un repère orthogonal est appelé nuage de points représentant la série statistique. Le point moyen du nuage est le point dont les coordonnées sont les moyennes X̄ et Ȳ. »

> **Principe de la méthode de Mayer** (p.107) — « Soit un nuage de points représentant une série statistique double (X,Y) et G son point moyen. On scinde le nuage de points de (X,Y) en deux parties contenant à peu prés le même nombre de points. On considère alors les points moyens G₁ et G₂ des deux nuages obtenus. La droite (G₁G₂) définit un ajustement affine du nuage de points représentant la série statistique double (X,Y). La droite (G₁G₂) est appelée droite de Mayer et passe par le point moyen G du nuage global. »

> **Principe des moindres carrés** (p.108, texte hors encadré) — « Le principe de la méthode d'ajustement par la méthode des moindres carrés consiste à déterminer les réels a et b tels que la somme Σ_{i=1}^{n} MᵢHᵢ² soit minimale. Dans ce cas, le statisticien pourra faire des prévisions en remplaçant la valeur observée yᵢ par la valeur théorique zᵢ = axᵢ + b. »

> **Théorème (admis)** (p.108) — « Soit (X,Y) une série statistique double sur un échantillon de taille n et telle que σ_X ≠ 0. Soit (xᵢ,yᵢ)_{1≤i≤n} les valeurs observées de la série. Alors la somme Σ_{i=1}^{n}(axᵢ + b − yᵢ)² est minimale pour le couple (a₀,b₀) tel que a₀ = cov(X,Y)/σ_X² et b₀ = (Ȳ − (cov(X,Y)/σ_X²)·X̄). »

> **Définition (droites des moindres carrés)** (p.109) — « Soit (X,Y) une série statistique double sur un échantillon de taille n. La droite d'équation y = (cov(X,Y)/σ_X²)(x − X̄) + Ȳ est appelée droite des moindres carrés de Y en X, ou droite de régression de Y en X. La droite d'équation x = (cov(X,Y)/σ_Y²)(y − Ȳ) + X̄ est appelée droite des moindres carrés de X en Y, ou droite de régression de X en Y. »

> **Conséquence** (p.109) — « Les droites des moindres carrés de Y en X et de X en Y passent par le point moyen G du nuage associé à la série (X,Y). »

> **Définition (coefficient de corrélation linéaire)** (p.110) — « Soit (X,Y) une série statistique double. On appelle coefficient de corrélation linéaire le réel noté ρ_XY défini par ρ_XY = cov(X,Y)/(σ_Xσ_Y). »

> **Propriétés** (p.110) — « Soit (X,Y) une série statistique double. Alors −1 ≤ ρ_XY ≤ 1. Le coefficient de corrélation linéaire est invariant par changement d'unité ou d'origine. »

> **Interprétation du coefficient de corrélation linéaire** (p.110) — « Les statisticiens conviennent que lorsque |ρ_XY| > √3/2, l'ajustement affine est justifié et les prédictions faites au moyen de cet ajustement sont raisonnables. »

Pas de « méthode » encadrée au sens des chapitres de la section Mathématiques : les méthodes sont dans les solutions (exercice résolu p.103–104 : tableau centres/effectifs/Σnᵢxᵢ/Σnᵢxᵢ² ; p.112 : changement de variable Z = ln Y, ρ, droite, prévision par exponentielle).

### Écart avec la référence (chap. 19 math-bac-math, manuel 222446, p.208–230 ; contrôle croisé avec math-bac-techniques ch.16)

**Ce que la référence (bac-math) enseigne et que ce manuel n'a PAS : rien de substantiel.** Le chapitre est le même texte (mêmes encadrés, mêmes activités, mêmes 12+1 exercices, mêmes valeurs numériques) en 23 pages au lieu de 23 (p.97–119 contre p.208–230) : version « allégée » seulement par la mise en page (une colonne de moins, pas de reproduction des tableaux de solution en pleine page). Aucune notion du programme de référence n'est absente.

**Différences constatées** (toutes de forme ou de transcription, à signaler à l'auteur) :
- Numérotation interne : « Chapitre 7 » imprimé (référence : « Chapitre 10 ») ; dernier chapitre du manuel (p.119 = dernière page) comme dans la référence.
- Numérotation des activités : imprimée ici « Act. 4 » (p.105, ménages), « Act. 1/2 » Mayer, « Act. 3 » moindres carrés (p.108), « Act. 1 » (p.109, surface corporelle), « Act. 4/5 » (p.111), « Act. 6 » (p.113) ; la référence les a renumérotées (Act. 1 p.216, Act. 2 p.220…, « Activité » terminal p.224). Ici il y a **2 « Exercice résolu »** (p.102–104 nouveaux-nés ; p.111–112 paramédicaux) ; la référence en annonce 3 en comptant l'Act. 6 (qui n'est pas résolue).
- Exercice résolu p.103 : la solution calcule V(X) par la forme développée (1/63)Σnᵢxᵢ² − (X̄)², alors que l'encadré p.99 donne la forme centrée (1/n)Σnᵢ(xᵢ − X̄)². Les deux formes coexistent ; la forme développée n'est démontrée nulle part.
- Ex. 10 3.b : la référence écrit f(x) = −0.3x² + 226.5 (x manquant) ; l'image p.117 imprime **f(x) = −0.3x² + 226.5x**. La fiche ci-dessus suit l'image.
- Ex. 1 : référence décrit les quatre nuages comme ici (V, décroissant, croissant incurvé, hyperbolique) ; confirmé sur l'image p.114.
- Pas de rubrique « Résumé du cours », « Avec l'ordinateur », « Aperçu historique », QCM ni Vrai-Faux dans ce manuel (comme la référence). Le chapitre bac-techniques 16 en a (Résumé, Avec l'ordinateur, Aperçu historique, exercices résolus, ajustements non affines exemples) ; **ce manuel n'a pas** : la méthode de Mayer à partage par parallèle à l'axe des ordonnées, le seuil 0.75 ≤ |r|, la cov/var par table de série simple, les exercices « Bac Tunisien » datés, la calculatrice Sharp.

**Ce que ce manuel a en plus : rien par rapport à la référence bac-math.** Par rapport à bac-techniques : présence de la covariance groupée (II.2), des droites de régression de X en Y avec « Conséquence » (passage par G), du seuil √3/2 et des modèles exponentiels/logistiques réinvestissant exp, ln et intégrale (ex. 7, 11, 12, 15).

### Bornes de scope

- ✅ INCLUS : série statistique double (X,Y) ; distributions marginales (effectifs, moyennes X̄ Ȳ, écarts-types σ_X σ_Y, variance, centres de classes) sur tableau à double entrée et sur données simples ; covariance (échantillon simple, échantillon groupé nᵢⱼ), cov(X,Y) = cov(Y,X), interprétation du signe ; nuage de points, point moyen G ; ajustement affine, variable explicative / expliquée ; **méthode de Mayer** (partage en deux parties de même effectif environ, droite (G₁G₂) passant par G) ; **moindres carrés** (somme ΣMᵢHᵢ² minimale, théorème admis a₀ = cov/σ_X², b₀ = Ȳ − a₀X̄, droites de régression de Y en X et de X en Y, passage par G) ; comparaison S_D / S_Δ ; **coefficient de corrélation linéaire** ρ_XY = cov/(σ_Xσ_Y), −1 ≤ ρ ≤ 1, invariance par changement d'unité ou d'origine, seuil |ρ| > √3/2 ; prévision / estimation par la droite ; **ajustements non affines par changement de variable** (Z = ln Y, Z = √Y, U = ln(8/D − 1), X = V² et Y = R/V) puis retour aux modèles exponentiel, logistique et quadratique ; réinvestissement de ex, ln, étude de fonction, valeur moyenne et intégrale ∫f ; usage d'une calculatrice en mode statistique à deux variables (n, Σx, Σx², X̄, σ_X, Σxy, r, a, b).
- ⛔ EXCLU : démonstration du théorème des moindres carrés (admis) et de la forme développée de V(X) ; justification du seuil √3/2 (« les statisticiens conviennent ») ; inférence (estimation, intervalle de confiance, test) ; régression multiple, régression de X en Y utilisée en calcul (seulement définie ; son seul usage admis est le passage par G, intersection des deux droites, encadré « Conséquence » p.109) ; variables aléatoires couplées / lien covariance-probabilités ; médiane, quartiles, diagramme en boîte ; coefficient de détermination ; valeurs de |ρ| ≤ √3/2 commentées autrement que « non justifié » ; calculatrices de modèles précis (la touche-à-touche du manuel est indicative). Types de calcul attendus : moyennes et écarts-types sur tableaux, Σxy et cov, ρ et droite à 10⁻¹/10⁻²/10⁻³ près, prévisions par droite ou par exponentielle ; les classes ouvertes existent dans le manuel (Act.2 p.99, Act.4 p.105) ; leur centre y est implicite. Le contenu généré ne pose pas de classe ouverte sans en donner le centre.

### Lecture

- **Pages lues par l'OCR (texte)** : 97 à 119 (23 pages) ; OCR fiable pour la prose et les énoncés, dégradé sur formules, indices, tableaux et figures.
- **Pages lues sur l'image (110 dpi)** : **les 23 pages**, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119 (la totalité du chapitre, toutes les pages portant formule, encadré ou tableau). Sondage image donc 23/23 (≫ 1 page sur 10).
- **Écarts OCR/image constatés (les plus denses)** :
  - p.98 : OCR « 96 128 184 312 368 472 496 568 », décimales perdues ; image 9.6, 12.8, 18.4, 31.2, 36.8, 47.2, 49.6, 56.8 ; ligne Y = 70 garbée (« a) | 6 »), image 4, 2, total 6 ; case encadrée 12 en (18.4 ; 104).
  - p.99 : classe « [60,70] » à l'OCR, image « [60,70[ » ; formules des moyennes/variances illisibles à l'OCR (indices p, 1≤i≤n, exposants), lues sur l'image ; tableau de 20 voitures colonné en désordre à l'OCR.
  - p.108–110 : formules du théorème, des droites de régression et de ρ_XY absentes ou garbées à l'OCR ; seuil lu « Es » à l'OCR, image √3/2.
  - p.111 : tableau des paramédicaux amputé à l'OCR (1998 à 2000 perdus) ; image : année imprimée « 19989 » en face de 26676 [sic] ; tableau de l'Act. 5 garbé à l'OCR.
  - p.112 : (4.61)², ≃, exposants de l'exponentielle perdus à l'OCR.
  - p.114–119 : figures (4 nuages p.114 ; nuage p.117) absentes ; tableaux de l'ex. 4 (p.115), f(x) = 3600/(1+0.5e^{−x}) (p.116), f(x) = −0.3x² + 226.5x (p.117), f(x) = ae^{bx} et 18e^{0.034x} (p.118, OCR « 1800088 »), D(t) = 8/(1+ce^{−at}) (p.119) restitués sur l'image seulement ; numéros d'exercice rendus « [4] », « AJ », « [1] », « 12] », « 15] » par l'OCR, lus 4, 7, 11, 12, 15 sur l'image.
  - Aucune divergence de **donnée** non corrigée : toutes les valeurs ci-dessus sont celles de l'image.
- Doutes signalés : (1) « 19989 » p.111 est une coquille d'impression, 1998 supposé ; (2) la place de l'exercice 13 et 14 : absents du manuel (numérotation 12 → 15), pas une perte de lecture (p.119 est la dernière page du PDF) ; (3) les valeurs finales (cov ≃ 0.7, ρ_XZ ≃ 0.960, 32419) sont celles du manuel, non recalculées ici.

## 3. Audit R-7 (2026-11-05)

Relecture indépendante (auditeur en contexte vierge, opus) de chaque chapitre **contre le PDF lui-même** : 100 % des encadrés verbatim confrontés à l'image de la page, 100 % du chapitrage et des zones `[?]`, et le reste par sondage (≥ 15 % des pages). Aucun chapitre n'a atteint le seuil d'escalade (3 erreurs substantielles sur la fiche). Corrections appliquées par un correcteur, puis revérifiées par un second auditeur opus ; les corrections des ch. 10 (p.171), 11 (F1, F2) et 15 (A-1, A-2) ont été appliquées sans nouvelle lecture de l'image.

| Chapitre | Pages sondées en image | Corrections fiche |
|---|---|---|
| 01 | 15 | 2 |
| 02 | 17 | 3 |
| 03 | 14 | 3 |
| 04 | 12 | 5 |
| 05 | 12 | 2 |
| 06 | 14 | 4 |
| 07 | 24 | 2 |
| 08 | 15 | 4 |
| 09 | 15 | 4 |
| 10 | 15 | 1 |
| 11 | 17 | 4 |
| 12 | 11 | 3 |
| 13 | 14 | 5 |
| 14 | 15 | 4 |
| 15 | 19 | 2 |
| 16 | 15 | 3 |
| 17 | 17 | 2 |

Total : 53 corrections, 261 pages sondées en image par les auditeurs (sur 301), en plus des pages lues en image par les lecteurs (toutes les pages à formules : l'OCR les dégrade). Ch. 14 : 15 pages vues sur image, dont 6 pages denses confrontées ligne à ligne.
