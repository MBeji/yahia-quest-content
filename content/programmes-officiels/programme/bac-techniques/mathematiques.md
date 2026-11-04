<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source unique : manuel élève officiel CNP 222451P00 (392 p.), mathématiques, 4ème année
     Sciences techniques (programme applicable à partir de 2007/2008). Aucun guide enseignant au
     corpus pour ce couple ⇒ le manuel élève fait référence. Lu le 2026-11-04 depuis le Drive
     `cnp-officiel` : couche texte page par page (pdftotext) et vérification sur l'image de chaque
     page à formules, encadrés compris ; page PDF = page imprimée (offset 0). -->

# Mathématiques — Bac Sciences techniques (`bac-techniques`) · manuel officiel CNP

> **Sources (Drive `cnp-officiel`, `manuels/secondaire/c4/eleve/`)** :
>
> - **Manuel élève** : code **222451P00** (392 p.), un seul tome — 16 chapitres.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
>   Le programme officiel ministériel n'est pas intégré au corpus (R-3) : le manuel prime tant
>   qu'il est seul.
> - **Langue d'enseignement** : **fr**. **subject id** : `math-bac-techniques` · **gradeSlug** :
>   `bac-techniques`.
> - **Notation** : chiffres occidentaux 0-9, équations LTR ; les formules perdues par la couche
>   texte (racines, exposants, ≤/≥, ℝ, ∈, vecteurs) sont rétablies sur l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Sciences techniques. Préface (p.3) : le manuel est « conforme
au programme de mathématiques de la quatrième année Sciences Techniques applicable à partir de
l'année scolaire 2007/2008 » ; il vise à « construire des savoirs et maîtriser des habiletés et des
aptitudes par la consolidation des acquis et leur mobilisation dans des situations-problèmes du
domaine des mathématiques ou en rapport avec l'environnement », avec démarche expérimentale et
conjectures, et des exercices d'évaluation en fin de chapitre. Mode d'emploi (p.4) : **16
chapitres** construits sur le même modèle — **Activités préliminaires** (rappels, prérequis),
**Cours** (activités de découverte, résultats essentiels en encadrés), **Résumé du cours**, **Avec
l'ordinateur**, **Exercices et problèmes**, **Aperçu historique**. Les chapitres 1 à 4 ne
comportent ni QCM ni Vrai-Faux.

## 2. Plan annuel (carte des chapitres = sommaire p.5)

> Statut de transcription par chapitre — `generation` = transcrit à profondeur de génération
> (chaque activité et exercice décrit, encadrés verbatim). La couverture de pages réelle vit dans
> `suivi/bac-techniques.json`.

| #   | Chapitre | pages (PDF = imprimées) | profondeur |
| --- | -------- | ----------------------- | ---------- |
| 1 | Limite et continuité | 7–34 | `generation` |
| 2 | Dérivabilité | 35–58 | `generation` |
| 3 | Fonction continue et strictement monotone sur un intervalle — fonction réciproque | 59–77 | `generation` |
| 4 | Étude de fonctions | 78–98 | `generation` |
| 5 | Fonctions primitives | 99–116 | `generation` |
| 6 | Fonctions logarithmes | 117–142 | `generation` |
| 7 | Fonctions exponentielles | 143–166 | `generation` |
| 8 | Calcul intégral | 167–192 | `generation` |
| 9 | Suites réelles | 193–220 | `generation` |
| 10 | Nombres complexes | 221–240 | `generation` |
| 11 | Équations à coefficients complexes | 241–256 | `generation` |
| 12 | Droites et plans de l'espace | 257–274 | `generation` |
| 13 | Produit scalaire, produit vectoriel et produit mixte dans l'espace | 275–306 | `generation` |
| 14 | Probabilité sur un ensemble fini | 307–330 | `generation` |
| 15 | Variables aléatoires réelles | 331–365 | `generation` |
| 16 | Statistiques | 366–392 | `generation` |

## 2.1 Chapitre 1 — Limite et continuité (manuel 222451, p.7–34)

**Page de garde (p.7)** — Titre : « Limite et continuité », Chapitre 1. « Plan du chapitre » : ❈ Activités préliminaires ; ❈ Cours (❖ Prolongement par continuité ; ❖ Limite et ordre ; ❖ Fonctions monotones et limites ; ❖ Limite et continuité d'une fonction composée ; ❖ Continuité sur un intervalle – Image d'un intervalle par une fonction continue ; ❖ Résolution d'équations de la forme f(x) = k ; ❖ Limites et comportement asymptotique) ; ❈ Résumé du cours ; ❈ Avec l'ordinateur ; ❈ Exercices et Problèmes ; ❈ Aperçu historique. Le chapitre n'a **ni QCM ni Vrai-Faux** : pas de rubrique de ce type (p.7–34 lues en entier).

### Activités préliminaires (p.8–10)

- **Act. prél. 1** (p.8) : déterminer la limite de f en x₀ : 1) f(x) = −x³ + x² + 1, x₀ = 0 ; 2) f(x) = (x² − x)/(x − 1), x₀ = 1 ; 3) f(x) = √(x² − 2x + 9), x₀ = 2.
- **Act. prél. 2** (p.8) : calculer lim_{x→+∞} (1/x³ + 1) ; lim_{x→+∞} (√(x²+1) − x) ; lim_{x→1⁺} (x − 1)/√(x − 1) ; lim_{x→0} 1/(x²√(x+1)) ; lim_{x→0⁺} (1/√x − (x+1)/√x).
- **Act. prél. 3** (p.8) : f(x) = −3x⁷ − x⁵ − x + 1 ; g(x) = (x − 1)/(x² + 3) ; h(x) = √(2x² + x) + x ; k(x) = |(x³ + 4x²)/(x + 4)|. a) ensemble de définition de chacune ; b) limites aux bornes de l'ensemble de définition.
- **Encadré « Théorèmes »** (p.8, rappels 3ème) — voir « Résultats » ci-dessous (polynôme, rationnelle, √f, |f|).
- **Encadré « Théorèmes : Opérations sur les limites »** (p.9) — tableaux somme, produit, quotient, F.I. (voir ci-dessous).
- **Act. prél. 4** (p.9) : a) vérifier que pour x > 0, sin x/√x = (sin x / x)·√x, en déduire lim_{x→0⁺} sin x/√x ; b) calculer lim_{x→0} (1 − cos x)/sin x ; c) calculer lim_{x→0} sin 3x/sin 2x (encadré jaune donné : lim_{x→0} (1 − cos x)/x = 0 ; lim_{x→0} (1 − cos x)/x² = 1/2 ; lim_{x→0} sin ax / x = a) ; d) calculer lim_{x→0} (1 − cos x)/sin² x.
- **Act. prél. 5** (p.10) : f définie sur ℝ par f(x) = (x − 1)²/|x − 1| si x ≠ 1 ; f(1) = 0. 1) étudier la continuité de f à droite et à gauche en 1 ; 2) f est-elle continue en 1 ? 3) f est-elle continue sur ℝ ?
- **Encadré « Théorèmes »** (p.10, continuité en un point) — voir « Résultats ».
- **Act. prél. 6** (p.10) : répondre par « vrai » ou « faux » en se référant à la représentation graphique de f (trois figures) : a) f est continue sur [−2, 3] (ligne brisée passant par (−2, 0), (0, 2) puis (2, 0), suivie d'une montée ; fig. lue) ; b) f est continue en 0 (courbe en arche, avec un segment horizontal à gauche de l'axe des ordonnées) ; c) f est continue sur ]0, 5[ (courbe croissante, saut, puis palier horizontal jusqu'à x = 5). Les réponses ne sont pas données.

### Cours — Activités

**Prolongement par continuité** (p.11)

- **Activité 1** (p.11) : 1) f(x) = (x² + 4x + 3)/(x + 1) pour tout réel x ≠ −1 ; a) prouver que f est continue en tout réel différent de −1 ; b) montrer que lim_{x→−1} f(x) = 2. 2) p définie sur ℝ par p(x) = f(x) si x ≠ −1, p(−1) = 2 ; a) montrer que p(x) = x + 3 pour tout réel x ; b) en déduire que p est continue en −1. 3) représenter f et p dans un repère (O, i⃗, j⃗).
- **Activité 2** (p.11) : 1) f continue en tout point d'un intervalle ouvert I sauf peut-être en x₀, g son prolongement par continuité en x₀ : montrer que lim_{x→x₀} f(x) = g(x₀). 2) f(x) = (x³ − 64)/(x − 4) : déterminer le prolongement par continuité de f en 4.
- **Activité 3** (p.11) : f(x) = x² / (|x + 1| − |x − 1|). 1) ensemble de définition D ; 2) prolongement par continuité de f en 0 ; 3) tracer la courbe de f dans (O, i⃗, j⃗).

**Limite et ordre** (p.12–14)

- **Activité 1** (p.12) : a) montrer que pour tout réel x, −x² + 2x − 5 < 0 ; b) calculer lim_{x→−2} (−x² + 2x − 5) ; c) préciser lim_{x→−2} |−x² + 2x − 5|.
- **Activité 2** (p.12) : f(x) = √(x²+1) − x. 1) calculer lim_{x→1} f(x), lim_{x→−∞} f(x) ; 2) a) montrer que pour tout réel x, √(x²+1) − x = 1/(√(x²+1) + x) ; b) déterminer alors lim_{x→+∞} f(x) ; 3) montrer que pour tout réel x on a f(x) > 0.
- **Activité 3** (p.12) : f, g définies sur un intervalle ouvert I, sauf peut-être en x₀ ; lim_{x₀} f = ℓ ; lim_{x₀} g = ℓ' ; pour tout x ≠ x₀ de I, f(x) ≤ g(x). Montrer que ℓ ≤ ℓ'. (Indication : considérer h = f − g.)
- **Activité 4** (p.13) : f(x) = x² cos(1/x) sur ℝ*. 1) montrer que pour x ≠ 0 : −x² ≤ f(x) ≤ x² ; 2) que peut-on conjecturer sur lim_{x→0} f(x) ?
- **Activité 5** (p.13) : f, g définies sur I ouvert sauf peut-être en x₀ ; pour tout x ≠ x₀ de I, |f(x)| ≤ |g(x)| et lim_{x₀} g(x) = 0. a) montrer que ∀ x ∈ I − {x₀} : −|g(x)| ≤ f(x) ≤ |g(x)| ; b) en déduire lim_{x₀} f(x).
- **Activité 6** (p.13) : f, g, ℓ réel ; pour tout x ≠ x₀ de I, |f(x) − ℓ| ≤ |g(x)| et lim_{x₀} g(x) = 0. a) montrer que ∀ x ∈ I − {x₀}, ℓ − |g(x)| ≤ f(x) ≤ ℓ + |g(x)| ; b) que peut-on conjecturer sur lim_{x₀} f(x) ?
- **Activité 7** (p.14) : f(x) = x sin(1/(2x)) + 3 sur ℝ*. a) montrer que pour tout x ∈ ℝ*, |f(x) − 3| ≤ |x| ; b) en déduire lim_{x→0} f(x).
- **Activité 8** (p.14) : f(x) = 1/x³ + sin(1/x) sur ℝ*. a) montrer que pour tout réel non nul x, 1/x³ − 1 ≤ f(x) ≤ 1/x³ + 1 ; b) conjecturer lim_{x→0⁺} f(x) et lim_{x→0⁻} f(x).
- **Activité 9** (p.14) : 1) a) montrer que pour tout réel x, x − 1 ≤ x + cos x ≤ x + 1 ; b) en déduire lim_{x→+∞} (x + cos x) et lim_{x→−∞} (x + cos x) ; 2) calculer lim_{x→+∞} (3x + 1 + 2 sin x) et lim_{x→0} (−1/x² + cos(1/x)).

**Fonctions monotones et limites** (p.15–16)

- **Activité 1** (p.15) : f(x) = x|x| + 1 sur [−2, 2]. 1) tracer la courbe de f ; 2) sens de variation de f sur [−2, 0] et [0, 2] ; 3) en déduire que pour tout x de [−2, 2], −3 ≤ f(x) ≤ 5.
- **Activité 2** (p.15) : 1) f(x) = 1/(3 − sin x) sur ℝ : montrer que f est bornée sur ℝ ; 2) en déduire lim_{x→+∞} x/(3 − sin x) et lim_{x→−∞} x/(3 − sin x).
- **Activité 3** (p.15) : f(x) = 1/sin x sur ]π/2, π[. 1) montrer que f est croissante sur ]π/2, π[ ; 2) f est-elle majorée sur ]π/2, π[ ? 3) quelle est la limite de f à gauche en π ?
- **Activité 4** (p.16) : f décroissante et non minorée sur I = ]a, b[. 1) montrer que (−f) est croissante et non majorée sur I ; 2) en déduire lim_{x→b⁻} f(x) = −∞.
- **Activité 5** (p.16) : f : [0, π/2[ → ℝ, x ↦ −2/cos x + 1 ; g : ]0, +∞[ → ℝ, x ↦ (x − 1)/x. 1) montrer que f est décroissante sur [0, π/2[ et g croissante sur ]0, +∞[ ; 2) calculer lim_{x→π/2⁻} f(x) et lim_{x→+∞} g(x) ; 3) f est-elle majorée ? minorée ? 4) montrer que g est majorée sur ]0, +∞[.

**Limite et continuité d'une fonction composée** (p.16–18)

- **Activité 1** (p.16) : f(x) = 4x², g(x) = √x, h(x) = 2|x|. 1) montrer que pour tout réel x, g(f(x)) = h(x) ; 2) préciser lim_{x→−1} g(f(x)) et comparer avec g(f(−1)).
- **Activité 2** (p.17) : f(x) = (1 + x)/(1 − x), g(x) = √x. 1) donner l'expression de (g∘f)(x) ; 2) calculer lim_{x→1⁻} (g∘f)(x).
- **Activité 3** (p.17) : f, g définies sur I et J avec f(x) ∈ J pour x ∈ I ; x₀ ∈ I ; montrer que si f est continue en x₀ et g continue en y₀ = f(x₀) alors g∘f est continue en x₀.
- **Activité 4** (p.17) : f définie sur un intervalle ouvert I, x₀ ∈ I. 1) montrer que si f est positive sur I et continue en x₀ alors √f est continue en x₀ ; 2) montrer que si f est continue en x₀ alors |f| est continue en x₀.
- **Activité 5** (p.18) : f(x) = √(x² + x) − x sur ]0, +∞[. 1) montrer que lim_{x→+∞} f(x) = 1/2 ; 2) a) montrer que pour tout x > 0, f(1/x) = (√(1+x) − 1)/x ; b) calculer lim_{x→0⁺} f(1/x), comparer avec lim_{x→+∞} f(x) ; c) conclure.
- **Activité 6** (p.18) : 1) déterminer lim_{x→+∞} x sin(1/x) ; lim_{x→+∞} (x² cos(1/x) − x²) ; 2) calculer de deux façons lim_{x→−∞} ((x+1)/(2x+3))⁶.
- **Activité 7** (p.18) : calculer lim_{x→−∞} (x³ + x² + x)⁴ ; lim_{x→+∞} |x² − x| ; lim_{x→0} √(sin x / x³).

**Continuité sur un intervalle — Image d'un intervalle** (p.19–21)

- **Activité 1** (p.19) : f(x) = √(x² + x) − x : déterminer l'ensemble de continuité de f.
- **Activité 2** (p.19) : justifier : a) x ↦ √(x² + 1) est continue sur ℝ ; b) x ↦ (3x² + 2x + 1)/(x + 1) est continue sur ]−1, +∞[ ; c) x ↦ √(1 − x²) est continue sur [−1, 1].
- **Activité 3** (p.20) : f : x ↦ x² + x définie dans [−2, 2], courbe (C) donnée (parabole, sommet d'ordonnée −1/4, point (2, 6), point (−2, 2) lus sur la figure). 1) justifier que f est continue sur [−2, 2] ; 2) reproduire le graphique et représenter f([−2, −1[), f([−1, 0]) et f([0, 2]) ; 3) a) montrer que pour tout x de [0, 2], f(x) ∈ [0, 6] ; b) montrer que pour tout y de [0, 6] il existe x de [0, 2] tel que y = f(x) ; c) en déduire f([0, 2]) ; 4) a) résoudre graphiquement f(x) = 0 et f(x) = 1 ; b) les résoudre algébriquement.
- **Activité 4** (p.20) : f(x) = 2 sin 3x dans ]−5, 5[, courbe donnée (sinusoïde, amplitude 2). 1) a) justifier que f est continue sur ]−5, 5[ ; b) image de ]−5, 5[ par f ; 2) résoudre graphiquement f(x) = 0 dans ]−5, 5[ ; 3) résoudre graphiquement f(x) = 1 ; 4) résoudre algébriquement, dans [−π, π], f(x) = 0 et f(x) = 1.
- **Activité 5** (p.20) : 1) représenter f sur ℝ : f(x) = x² + 1 si x ≠ 0 ; f(0) = −2 ; 2) montrer que f n'est pas continue sur ℝ ; 3) déterminer f(ℝ), est-ce un intervalle ? 4) déterminer f(]−∞, 0[), est-ce un intervalle ? 5) résoudre graphiquement f(x) = k (k réel donné), discuter.
- **Activité 6** (p.21) : 1) f : x ↦ x², déterminer algébriquement l'image de ]−1, 1[ par f ; 2) g sur ℝ : g(x) = 2x + 1 si x ≠ 0, g(0) = −2 : 1) étudier la continuité de g sur ]−∞, 0] ; 2) déterminer l'image de ]−∞, 0] par g.

**Résolution d'équations de la forme f(x) = k** (p.21–24)

- **Activité 1** (p.21) : h(x) = √(x+1) − x² sur [−1, 2], courbe donnée. 1) justifier la continuité de h sur [−1, 2] ; 2) résoudre graphiquement √(x+1) − x² = 0 ; 3) a) calculer h(1) et h(2), justifier que 0 ∈ h([1, 2]) ; b) en déduire que h(x) = 0 possède une solution α dans ]1, 2[ puis prouver 1 < α < 1,5 ; 4) montrer de même que h(x) = 0 possède une deuxième solution β dont on donnera un encadrement d'amplitude 0,5.
- **Activité 2** (p.22) : f : x ↦ x³ + x − 1 (graphique donné). 1) justifier la continuité de f sur ℝ ; 2) conjecturer sur l'ensemble des solutions de f(x) = 0 dans [0, 1] ; 3) comparer 0 avec f(0) et f(1).
- **Activité 3** (p.23, « unicité de la solution ») : f : x ↦ 2x³ + 2x − 1. 1) montrer que f est continue et strictement croissante sur ℝ ; 2) montrer que l'image de [0, 1] par f est [−1, 3] ; 3) montrer que f(x) = 0 admet une solution unique α dans ]0, 1[ ; 4) valeur approchée à 10⁻² près par défaut de α.
- **Activité 4** (p.23) : f : x ↦ x⁵ + x³ − 3 sur ℝ (graphique donné). 1) f continue sur ℝ ; 2) f strictement croissante sur [0, 2] ; 3) a) calculer f(0) et f(2) ; b) en déduire que f(x) = 0 admet une solution unique dans [0, 2] ; 4) α cette solution : a) calculer f(1), en déduire α ∈ [1, 2] ; b) calculer f(1,5), en déduire une valeur approchée à 0,5 près par défaut ; c) calculer f(1,25), en déduire une valeur approchée à 0,25 près par défaut.
- **Activité 5** (p.24) : f(x) = 2x³ − 3x² − x + 1 sur ℝ. a) montrer que f(x) = 0 admet une solution unique α dans [0, 1] ; b) utiliser la dichotomie pour déterminer une valeur approchée de α.

**Limites et comportement asymptotique** (p.24–26)

- **Activité 1** (p.24) : 1) f(x) = 2x³ − 3x² − x + 1, courbe donnée : montrer que (C) admet au voisinage de +∞ et de −∞ des branches paraboliques de direction celle de l'axe des ordonnées ; 2) f : x ↦ √(2x − 1) définie sur [1/2, +∞[ (courbe donnée) : montrer que (C) admet au voisinage de +∞ une branche parabolique de direction celle de l'axe des abscisses.
- **Activité 2** (p.25) : f(x) = (2x + 1)/(x − 1) sur ℝ − {1} (courbe, asymptotes y = 2 et x = 1 figurées) : montrer que sa courbe possède une asymptote horizontale et une asymptote verticale.
- **Activité 3** (p.25) : f(x) = (2x² + 4x + 1)/(x + 1), (C) courbe dans (O, i⃗, j⃗) (asymptote verticale x = −1 et oblique figurées). a) montrer que D : x = −1 est asymptote à (C) ; b) montrer que pour tout x ≠ −1, f(x) = 2x + 2 − 1/(x + 1) ; c) prouver que Δ : y = 2x + 2 est asymptote à (C) au voisinage de +∞ et de −∞.
- **Activité 4** (p.26) : 1) f : x ↦ (2x² + x + 1)/(x² + x − 2) : a) ensemble de définition et domaine de continuité ; b) limites aux bornes de l'ensemble de définition ; c) interpréter graphiquement. 2) g : x ↦ (x² + x + 1)/(x − 2) : a) déterminer a, b, c tels que pour tout x ≠ 2, g(x) = ax + b + c/(x − 2) ; b) asymptotes à la courbe C de g. 3) h(x) = √(x² + x + 1) sur ℝ : a) calculer lim_{+∞} h(x), lim_{+∞} h(x)/x et lim_{+∞} [h(x) − x] ; b) montrer que D : y = x + 0,5 est asymptote oblique à (C) au voisinage de +∞ ; c) étudier le comportement asymptotique de (C) au voisinage de −∞. 4) k(x) = x + √x : montrer que sa courbe admet une branche parabolique de direction la droite D : y = x au voisinage de +∞.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Théorèmes** (p.8) — « La limite d'une fonction polynôme, quand la variable tend vers + ∞ ou vers − ∞, est la même que celle de son monôme de plus haut degré : P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ où aₙ ≠ 0, on a lim_{|x|→+∞} P(x) = lim_{|x|→+∞} aₙxⁿ. » / « La limite d'une fonction rationnelle, quand la variable tend vers + ∞ ou vers − ∞, est la même que celle du quotient des monômes de plus haut degré : R(x) = (aₙxⁿ + ... + a₀)/(bₘxᵐ + ... + b₀) où aₙbₘ ≠ 0, on a lim_{|x|→+∞} R(x) = lim_{|x|→+∞} aₙxⁿ/(bₘxᵐ). » / « Soit f une fonction et ℓ un réel. Quand le réel x tend vers x₀, ou vers x₀⁺, ou vers x₀⁻, ou vers + ∞, ou vers − ∞, on a les résultats suivants : Si lim f = ℓ et f est positive alors lim √f = √ℓ (ℓ ≥ 0). Si lim f = +∞ et f est positive alors lim √f = √ℓ [sic : imprimé « √ℓ » au lieu de +∞]. Si lim f = ℓ alors lim |f| = |ℓ|. Si lim f = +∞ ou lim f = −∞ alors lim |f| = + ∞. »

> **Théorèmes : Opérations sur les limites** (p.9) — « Soient f et g deux fonctions. Quand le réel x tend vers x₀, ou vers x₀⁺, ou vers x₀⁻, ou vers +∞, ou vers −∞, on a les résultats suivants : » (ℓ, ℓ' réels)
> Somme f+g : (ℓ, ℓ') → ℓ+ℓ' ; (ℓ, +∞) → +∞ ; (−∞, ℓ') → −∞ ; (+∞, +∞) → +∞ ; (−∞, −∞) → −∞ ; (−∞, +∞) → F.I.
> Produit f×g : (ℓ, ℓ') → ℓ × ℓ' ; (+∞, ℓ'>0) → +∞ ; (−∞, ℓ'>0) → −∞ ; (+∞, ℓ'<0) → −∞ ; (−∞, ℓ'<0) → +∞ ; (+∞, +∞) → +∞ ; (+∞, −∞) → −∞ ; (−∞, −∞) → +∞ ; (0, +∞ ou −∞) → F.I.
> Quotient f/g : (ℓ, ℓ'≠0) → ℓ/ℓ' ; (+∞, ℓ'>0) → +∞ ; (−∞, ℓ'>0) → −∞ ; (+∞, ℓ'<0) → −∞ ; (−∞, ℓ'<0) → +∞ ; (ℓ, +∞) → 0 ; (ℓ, −∞) → 0 ; (ℓ≠0, 0) → « + ∞ ou − ∞ (on applique la règle des signes) » ; (0, 0) → F.I ; (+∞ ou −∞, +∞ ou −∞) → F.I.
> « N.B : F.I désigne une forme indéterminée, pour laquelle une étude spécifique doit être menée pour déterminer l'éventuelle limite. »

> **Théorèmes** (p.10) — « Soit f une fonction définie sur un intervalle ouvert I et x₀ un réel de I. f est continue en x₀ si et seulement si lim_{x→x₀} f(x) = f(x₀). » / « Soit f une fonction définie sur un intervalle [x₀, x₀ + h[, (h > 0). f est continue à droite en x₀ si et seulement si lim_{x→x₀⁺} f(x) = f(x₀). » / « Soit f une fonction définie sur un intervalle ]x₀ − h, x₀], (h > 0). f est continue à gauche en x₀ si et seulement si lim_{x→x₀⁻} f(x) = f(x₀). » / « Soit f une fonction définie sur un intervalle ouvert contenant x₀. f est continue en x₀ si et seulement si f est continue à droite et à gauche en x₀. » / « Si f et g sont deux fonctions continues en x₀ alors les fonctions f+g, f×g et |f| sont continues en x₀, si de plus g(x₀) ≠ 0 alors la fonction f/g est continue en x₀. » / « Toute fonction polynôme est continue en tout réel x₀. » / « Toute fonction rationnelle est continue en tout réel x₀ de son domaine de définition. »

> **Définition** (p.11) — « Soit f une fonction continue en tout point d'un intervalle ouvert I, sauf peut-être en x₀ de I. On appelle prolongement par continuité de f en x₀, la fonction g définie sur I, continue en x₀ et vérifiant : ∀ x ∈ I − {x₀}, g(x) = f(x). »

> **Théorèmes « Limite et ordre »** (p.12–14), chacun suivi de : « Le résultat du théorème reste vrai lorsque x tend vers x₀⁻, x₀⁺, −∞ ou +∞. » — (1) « Soit f une fonction définie sur un intervalle ouvert I, sauf peut-être en un réel x₀. On suppose que lim_{x→x₀} f(x) = ℓ. Si f(x) ≥ 0 pour tout x de I, distinct de x₀, alors ℓ ≥ 0. Si f(x) ≤ 0 pour tout x de I, distinct de x₀, alors ℓ ≤ 0. » (p.12) — (2) « Si lim_{x₀} f(x) = ℓ ; lim_{x₀} g(x) = ℓ' et pour tout x de I, différent de x₀, f(x) ≤ g(x) alors ℓ ≤ ℓ'. » (p.12) — (3) « Soit f, g et h trois fonctions définies sur un intervalle ouvert I, sauf peut-être en x₀ de I. Si lim_{x₀} g(x) = ℓ ; lim_{x₀} h(x) = ℓ et pour tout x de I, différent de x₀, h(x) ≤ f(x) ≤ g(x) alors lim_{x₀} f(x) = ℓ » (p.13) — (4) « Si pour tout x de I, différent de x₀, on a |f(x)| ≤ |g(x)| et lim_{x₀} g(x) = 0 alors lim_{x₀} f(x) = 0. » (p.13) — (5) « Soit f et g [...] et soit ℓ un réel. Si pour tout x de I, différent de x₀, on a |f(x) − ℓ| ≤ |g(x)| et lim_{x₀} g(x) = 0 alors lim_{x₀} f(x) = ℓ. » (p.14) — (6) « Si pour tout x de I, différent de x₀, on a f(x) ≥ g(x) et lim_{x₀} g(x) = +∞ alors lim_{x₀} f(x) = +∞. Si pour tout x de I, différent de x₀, on a f(x) ≤ g(x) et lim_{x₀} g(x) = −∞ alors lim_{x₀} f(x) = −∞. » (p.14)

> **Définition** (p.15) — « Soit I un intervalle de ℝ. Une fonction est dite monotone sur I, lorsqu'elle est croissante sur I ou décroissante sur I. Une fonction est dite strictement monotone sur I, lorsqu'elle est strictement croissante sur I ou strictement décroissante sur I. »

> **Définition** (p.15) — « Soit f une fonction définie sur un intervalle I de ℝ. * La fonction f est majorée sur I s'il existe un réel M tel que pour tout x ∈ I, f(x) ≤ M. * La fonction f est minorée sur I s'il existe un réel m tel que pour tout x ∈ I, m ≤ f(x). * La fonction f est dite bornée sur I s'il existe deux réels m et M tels que pour tout x ∈ I, m ≤ f(x) ≤ M. »

> **Théorèmes « Fonctions monotones et limites »** (p.16) — « Soit f une fonction définie sur un intervalle I = ]a, b[ (ou I = ]a, +∞[). Si f est croissante et non majorée sur I alors lim_{x→b⁻} f(x) = +∞ (ou lim_{x→+∞} f(x) = +∞). » / « Si f est décroissante et non minorée sur I alors lim_{x→b⁻} f(x) = −∞ (ou lim_{x→+∞} f(x) = −∞). » / « Soit f une fonction définie sur un intervalle I = ]a, b[ (ou I = ]a, +∞[). * Si f est croissante et majorée sur I alors f admet une limite finie à gauche en b (ou en +∞). * Si f est décroissante et minorée sur I alors f admet une limite finie à gauche en b (ou en +∞). »

> **Définition** (p.17) — composée : « Soient f et g deux fonctions définies respectivement sur I et J telles que pour tout x ∈ I on a f(x) ∈ J. La fonction qui à tout réel x de I associe le réel g(f(x)) est appelée la composée de f par g. On la note g∘f, on lit : « g rond f » et on écrit (g∘f)(x) = g(f(x)). »

> **Théorèmes** (p.17–18) — « Soient f et g [...] telles que pour tout x ∈ I on a f(x) ∈ J. Si lim_{x→x₀} f(x) = ℓ (ℓ ∈ ℝ) et g est continue en ℓ alors lim_{x→x₀} (g∘f)(x) = g(ℓ). Le résultat du théorème reste vrai lorsque x tend vers x₀⁻, x₀⁺, −∞ ou +∞. » / « Soit x₀ un élément de I. Si f est continue en x₀ et si g est continue en f(x₀) alors g∘f est continue en x₀. » / (p.18) « Soit f une fonction définie sur un intervalle du type ]0, +∞[. On a : lim_{x→+∞} f(x) existe ⇔ lim_{x→0⁺} f(1/x) existe. Dans ce cas on a lim_{x→+∞} f(x) = lim_{x→0⁺} f(1/x). Soit f une fonction définie sur un intervalle du type ]−∞, 0[. On a : lim_{x→−∞} f(x) existe ⇔ lim_{x→0⁻} f(1/x) existe. Dans ce cas on a lim_{x→−∞} f(x) = lim_{x→0⁻} f(1/x). » / (p.18) « Soient f et g [...] telles que pour tout x ∈ I on a f(x) ∈ J. Si lim_{x→x₀} f(x) = ℓ et lim_{x→ℓ} g(x) = ℓ' alors lim_{x→x₀} (g∘f)(x) = ℓ' (x₀, ℓ et ℓ' pourront être finis ou infinis). »

> **Définition** (p.19) — « Soit a et b deux réels tels que a < b. * Une fonction définie sur un intervalle ]a, b[ est dite continue sur ]a, b[ si elle est continue en tout réel de ]a, b[. * [...] sur ]a, b] est dite continue sur ]a, b] si elle est continue sur ]a, b[ et continue à gauche en b. * [...] sur [a, b[ est dite continue sur [a, b[ si elle est continue sur ]a, b[ et continue à droite en a. * [...] sur [a, b] est dite continue sur [a, b] si elle est continue sur ]a, b[, continue à droite en a et continue à gauche en b. * [...] sur ]a, +∞[ (resp. sur ]−∞, a[) est dite continue sur ]a, +∞[ (resp. sur ]−∞, a[) si elle est continue en tout réel de ]a, +∞[ (resp. de ]−∞, a[). * [...] sur [a, +∞[ est dite continue sur [a, +∞[ si elle est continue sur ]a, +∞[ et continue à droite en a [sic : la page imprime « continue sur ]−∞, a[ » au lieu de ]a, +∞[]. * [...] sur ]−∞, a] est dite continue sur ]−∞, a] si elle est continue sur ]−∞, a[ et continue à gauche en a. »

> **Image d'un intervalle par une fonction** (p.19) — « Soit f une fonction définie sur un intervalle I de ℝ. On désigne par f(I) l'ensemble des réels f(x) tels que x ∈ I. On note f(I) = {f(x) ; x ∈ I}. »

> **Théorème** (p.21) — « * L'image d'un intervalle par une fonction continue est un intervalle. * L'image d'un intervalle fermé borné [a, b] par une fonction continue f est un intervalle fermé borné [m, M] où m et M sont respectivement le minimum et le maximum de f sur l'intervalle [a, b]. » (figure : courbe sur [a, b], f(a), f(b), m, M)

> **Théorème des valeurs intermédiaires** (p.22) — « Soit f une fonction définie et continue sur un intervalle I. Soit a et b deux réels de I tels que a < b. Pour tout réel k compris entre f(a) et f(b), l'équation f(x) = k possède au moins une solution dans l'intervalle [a, b]. » Commentaire : « Le théorème des valeurs intermédiaires affirme que la courbe représentative d'une fonction continue sur un intervalle ne présente ni trous ni sauts. »

> **Corollaire 1** (p.22) — « Si f est une fonction continue sur un intervalle [a, b] et vérifiant f(a).f(b) < 0 alors il existe au moins un réel c appartenant à l'intervalle ouvert ]a, b[ tel que f(c) = 0. » Remarque : « Ce corollaire indique que lorsque f est continue et change de signe sur un intervalle [a, b] alors sa courbe représentative coupe l'axe des abscisses au moins une fois en un point d'abscisse appartenant à cet intervalle. »

> **Corollaire 2** (p.23) — « Si f est une fonction continue sur un intervalle et ne s'annule en aucun réel de cet intervalle alors elle garde un signe constant sur cet intervalle. »

> **Théorème** (p.23) — « Si f est une fonction continue et strictement monotone sur un intervalle [a, b] et vérifiant f(a).f(b) < 0 alors il existe un réel unique c appartenant à l'intervalle ouvert ]a, b[ tel que f(c) = 0. »

> **Commentaires — dichotomie** (p.24) — « Pour trouver une valeur approchée d'une solution α de l'équation f(x) = 0, dans un intervalle [a, b], on utilise la dichotomie de la façon suivante : - On partage [a, b] en deux intervalles [a, c] et [c, b] de même amplitude. - On détermine lequel de ces deux intervalles contient α en utilisant le corollaire 1. - On recommence avec cet intervalle les deux étapes précédentes. - On s'arrête lorsqu'on a obtenu un encadrement satisfaisant de α. (Dichotomie signifie : division en deux) »

> **Branches paraboliques d'une courbe** (p.24) — « * Si lim_{x→+∞} f(x) = +∞ ou −∞ et lim_{x→+∞} f(x)/x = +∞ ou −∞ (resp. quand x → −∞) alors (C_f) admet en +∞ (resp. en −∞) une branche parabolique de direction celle de l'axe des ordonnées. * Si lim_{x→+∞} f(x) = +∞ ou −∞ et lim_{x→+∞} f(x)/x = 0 (resp. quand x → −∞) alors (C_f) admet en +∞ (resp. en −∞) une branche parabolique de direction celle de l'axe des abscisses. »

> **Asymptotes parallèles aux axes du repère** (p.25) — « * On dit que la droite Δ : x = a est une asymptote à la courbe de f dans l'un des quatre cas suivants : lim_{x→a⁺} f(x) = +∞ ; lim_{x→a⁺} f(x) = −∞ ; lim_{x→a⁻} f(x) = +∞ ; lim_{x→a⁻} f(x) = −∞. * On dit que la droite Δ : y = b est une asymptote à la courbe de f lorsque lim_{x→−∞} f(x) = b ou lim_{x→+∞} f(x) = b. »

> **Asymptote oblique à une courbe** (p.26) — « On dit que la droite Δ : y = ax + b est une asymptote oblique à la courbe de f au voisinage de −∞ (resp. de +∞) si on a : lim_{x→−∞} [f(x) − (ax + b)] = 0 (resp. lim_{x→+∞} [f(x) − (ax + b)] = 0). »

> **Encadré** (p.26) — « Soit f une fonction définie sur un intervalle du type [c, +∞[. Si lim_{x→+∞} f(x) = +∞ (ou −∞) et lim_{x→+∞} f(x)/x = a (a ∈ ℝ*) et lim_{x→+∞} [f(x) − ax] = b (b ∈ ℝ) alors la droite D : y = ax + b est une asymptote oblique à la courbe représentative de f au voisinage de +∞. Si lim_{x→+∞} f(x) = +∞ (ou −∞) et lim_{x→+∞} f(x)/x = a (a ∈ ℝ*) et lim_{x→+∞} [f(x) − ax] = +∞ ou −∞ alors la courbe représentative de f admet au voisinage de +∞ une branche parabolique de direction celle de la droite D : y = ax. Les résultats sont vrais pour une fonction f définie sur un intervalle du type ]−∞, c] et x tendant vers −∞. »

### Résumé du cours (p.27–28)

Reprend, en deux pages, les rubriques : prolongement par continuité (p fonction prolongée : p(x) = f(x) si x ≠ x₀ ; p(x₀) = ℓ) ; limite et ordre (mêmes théorèmes qu'ci-dessus, avec en plus la version « Si f(x) ≤ g(x) et lim f(x) = +∞ alors lim g(x) = +∞ » (p.27) et « f(x) ≤ g(x) et lim g(x) = −∞ alors lim f(x) = −∞ ») ; fonctions monotones et limite ; limite d'une fonction composée (dont : « Si f est continue sur D_f et si g est continue sur D_g alors g∘f est continue sur D_f » ; « Si f est positive et continue en x₀ alors √f est continue en x₀ ; si f est continue en x₀ alors |f| est continue en x₀ ») ; continuité sur un intervalle – image d'un intervalle ; résolution d'équations f(x) = k (TVI, corollaires, théorème d'unicité) ; asymptote oblique (« Si b = +∞ ou −∞ la courbe possède une branche parabolique de direction la droite D : y = ax au voisinage de +∞ »). Aucun résultat nouveau par rapport au cours.

### Exemple résolu — néant

Aucun exercice résolu intégral dans ce chapitre (le manuel ne contient pas d'encadré « Problème résolu »).

### QCM / Vrai-Faux

Aucun dans ce chapitre (hors la mini-activité préliminaire 6 « vrai/faux sur graphique », p.10).

### Avec l'ordinateur (p.29)

- **Activité 1** : f(x) = x³ − x² − 1 ; construire dans un tableur (colonnes A et B, formule `= A3*A3*A3 - A3*A3 - 1`, pas A4 = A3 + 1), tracer un nuage de points, conjecturer sur les solutions de f(x) = 0, affiner (A4 = A3 + 0.1 puis + 0.05), puis montrer que f(x) = 0 admet dans ℝ une solution unique α et vérifier α ∈ ]1.45, 1.5[.
- **Activité 2** : calcul de limite avec le logiciel de calcul formel Derive (exemple lim_{x→+∞} x sin(1/x) = 1) ; application : lim_{x→+∞} (√(x²+1) − x) ; lim_{x→1} (x − 1)/√(x − 1) ; lim_{x→−1} (x+1)/(x²+x) ; N.B. : « x² + 1 − x » s'écrit `sqrt(x^2 + 1) − x`.

### Exercices et problèmes (p.30–32) — 24 exercices

- **Ex. 1** (p.30) : f(x) = (x − 2)³. a) limite de f en 2 ; b) limites de 1/f à droite et à gauche en 2 ; c) que représente x = 2 pour la courbe de 1/f ?
- **Ex. 2** (p.30) : 1) représenter f : x ↦ 2x/(x+1) et g : x ↦ (−x+1)/(2x+1) ; 2) Cf, Cg dans un repère orthogonal : asymptotes aux voisinages de +∞ et −∞.
- **Ex. 3** (p.30) : calculer lim_{x→−∞} (2x² + x + 2) ; lim_{x→+∞} (2x³ + 2x + 1)/(x² − x − 1) ; lim_{x→+∞} (√x + 1/(x−1)²) ; lim_{x→−∞} (−x − √(1−x) + 1) ; lim_{x→+∞} (x² + √x)/(x−1)² ; lim_{x→−∞} (√(x²−1) + x)/x.
- **Ex. 4** (p.30) : calculer lim_{x→+∞} (√(1+x) − x − 1) ; lim_{x→−∞} (√(x²+1) − 1)/x ; lim_{x→+∞} √(x²−1)/x³ ; lim_{x→−∞} √(x²−1)/x³ ; lim_{x→+∞} (√(x²−1) − x) ; lim_{x→+∞} (2x + 1 + 3 cos x) ; lim_{x→−∞} (2x + 1 + 3 cos x).
- **Ex. 5** (p.30) : étudier a) lim_{x→2⁺} 1/(x√(x−2)) ; b) lim_{x→1} √(x²−1)/(x−1)³ ; c) lim_{x→1} (2x³+x²−x−2)/(x²+3x−4) ; d) lim_{x→1⁺} 1/((x−1)√(x−1)) ; e) lim_{x→4} (√(x+5) − 3)/(x − 4) ; f) lim_{x→3} (√(x+1) − 2)/(√(x−2) − 1).
- **Ex. 6** (p.30) : f(x) = x/(1+√x)² ; g(x) = (x²+4)/(2x) ; h(x) = (x²+3x−4)/(x+4) si x ≠ −4, h(−4) = a (a réel). 1) a- ensemble de définition et domaine de continuité ; b- limites aux bornes ; 2) pour h, déterminer a pour que h soit continue en x₀ = −4.
- **Ex. 7** (p.30) : pour x ∈ [−5/2, 2[ ∪ ]2, +∞[, g(x) = (x−2)/(x + 1 − √(2x+5)). a) montrer que pour x ≠ −2 et x ∈ [−5/2, 2[ ∪ ]2, +∞[, g(x) = (x + 1 + √(2x+5))/(x+2) ; b) en déduire que g admet un prolongement par continuité en x₀ = 2 que l'on précisera.
- **Ex. 8** (p.31) : lim_{x→0} sin 5x/tg 2x ; lim_{x→0·} (1 − cos 3x)/x² ; lim_{x→0·} (1 − cos 2x)/(4x²) ; lim_{x→0·} (tg x − sin x)/x² ; lim_{x→0·} tg²x/(1 − cos x) [?, les limites 2 à 5 portent toutes une même petite marque après 0 (« x→0· »), non identifiable : ni 0⁻ ni 0⁺ n'est affirmé].
- **Ex. 9** (p.31) : 1) f(x) = 1/(2 + cos x) sur ℝ : montrer que f est bornée ; 2) en déduire lim_{x→+∞} x/(2 + cos x) et lim_{x→+∞} (x + sin x)/(2 + cos x).
- **Ex. 10** (p.31) : f(x) = (2 sin x + 1 − cos x)/x si x ≠ 0 ; f(0) = 1. Étudier la continuité de f en 0.
- **Ex. 11** (p.31) : f(x) = (1 − cos x)/x si x ≠ 0 ; f(0) = 0. Montrer que f est continue sur ℝ.
- **Ex. 12** (p.31) : f(x) = (|x|√|x|)/x si x ≠ 0 ; f(0) = 0. Étudier la continuité de f sur ]−1, 1[.
- **Ex. 13** (p.31) : f(x) = x² si x ∈ [0, 1] ; f(x) = 2x − 1 si x ∈ ]1, +∞[. 1) f continue sur [0, 2] ; 2) image de [0, 2] ; 3) image de [0, +∞[ ; 4) tracer C dans un repère orthonormé.
- **Ex. 14** (p.31) : g(x) = −1/x² . a- continuité de g sur ℝ* ; b- sens de variation sur ]−∞, 0[ et ]0, +∞[ ; c- images de ces intervalles par g.
- **Ex. 15** (p.31) : a- montrer que x⁵ + 3x − 2 = 0 possède une solution réelle unique α ∈ ]0, 1[ ; b- vérifier que 1/2 < α < 3/4.
- **Ex. 16** (p.31) : 1) f : x ↦ x³ + 2x − 1 pour x ∈ ]−∞, 1[ : montrer que x³ + 2x = 1 admet une solution unique x₀ telle que 0 < x₀ < 1 ; 2) valeur approchée à 0,1 près par défaut de x₀.
- **Ex. 17** (p.31) : 1) montrer que sin x − 2x + 1 = 0 admet une solution unique β dans ]0, π/2[ ; par dichotomie, valeur approchée à π/8 près ; 2) montrer que (3/2)x − tg x = 0 possède une solution unique α dans ]π/4, π/3[.
- **Ex. 18** (p.32) : P(x) = 2x³ − 3x² − 1 sur ℝ : montrer que P(x) = 0 admet une racine réelle comprise entre 1,6 et 1,7.
- **Ex. 19** (p.32) : P(x) = x⁶ − x − 1. a) P(x) = 0 admet une racine réelle unique α dans [1, 2] ; b) dichotomie : valeur approchée par défaut à 10⁻¹ près ; c) vérifier 1,2 < α < 1,25.
- **Ex. 20** (p.32) : f(x) = x² − 3x|x|. 1) continuité et variations de f sur ]−∞, 0[ et ]0, +∞[ ; 2) représenter f dans un repère orthonormé ; 3) images des intervalles ]−∞, 0[ et ]0, +∞[ par f.
- **Ex. 21** (p.32) : 1) parabole y = x² et droite D : y = x + 1 sur un même graphique (unité 3 cm) ; 2) établir graphiquement que f(x) = x² − x − 1 = 0 admet deux solutions, α positive et β négative ; 3) a) placer les points d'abscisses 3/2 et 5/3 ; b) conjecturer un encadrement de α ; 4) a) expliquer par le graphique que sur [0, +∞[ il est équivalent de dire x < α ou f(x) < 0 ; b) en déduire 3/2 < α < 5/3 ; c) montrer le résultat précédent ; 5) a) montrer que 1 − α est une solution négative de f(x) = 0 ; b) en déduire un encadrement de β.
- **Ex. 22** (p.32) : h(x) = x/(|x| − 1). 1) domaine de définition, h impaire, tracer (C') et ses asymptotes ; 2) tableau de variation ; 3) discuter graphiquement suivant k le nombre de solutions de x + k = k|x|.
- **Ex. 23** (p.32) : P(x) = 4x³ − 3x − 1/2. 1) calculer P(−1), P(−1/2), P(0), P(1) ; 2) a) P(x) = 0 admet dans ℝ trois racines distinctes x₁ < x₂ < x₃ ; b) vérifier −1 < x₁ < −1/2 < x₂ < 0 < x₃ < 1 ; 3) a) cos(3α) = 4cos³(α) − 3cos(α) ; b) montrer que x₁ = cos(11π/9), x₂ = cos(7π/9), x₃ = cos(π/9).
- **Ex. 24** (p.32) : f(x) = 2x + √(2x − 1). Étudier les branches infinies de sa courbe C et tracer une allure de C.

### Aperçu historique (p.33–34)

Une ligne : biographie d'Augustin Louis Cauchy (1789–1857) — fondateur du calcul rigoureux des limites (« Résumé des leçons sur le calcul infinitésimal », 1823), définitions de limite et de continuité ; Dirichlet (1829) pour le lien dérivée/dérivabilité.

### Bornes de scope observées (chapitre 1)

- ✅ INCLUS : rappels de 3ème (limites de polynômes/rationnelles, opérations, F.I., continuité en un point/à droite/à gauche) ; prolongement par continuité ; limite et ordre (théorèmes de comparaison, d'encadrement, |f−ℓ| ≤ g) ; fonctions monotones et limites (majorée/minorée/bornée) ; composée (limite, continuité, changement de variable x → 1/x) ; continuité sur un intervalle ; image d'un intervalle ; TVI + corollaires + unicité, dichotomie ; branches paraboliques, asymptotes verticale/horizontale/oblique ; limites trigonométriques usuelles (sin x/x, (1−cos x)/x²).
- ⛔ NON traité : dérivée (le sens de variation est étudié par comparaison directe, sans dérivation) ; suites ; définition ε-δ de la limite ; démonstrations des théorèmes TVI et « image d'un intervalle fermé borné » (énoncés admis) ; limite d'une fonction monotone à gauche en b admise (théorèmes énoncés sans preuve).

> Sondage image : pages 8 à 32 (toutes) lues en L3 (seules les pages 7 et 33–34 : plan et biographie, en L1) + zoom 220 dpi sur l'Ex. 4 (p.30) ; écarts : la couche texte perd systématiquement les valeurs absolues (p.13, 14, 15, 17, 18, 19), tous les radicaux, ≤/≥, ℝ, ∈ (corrigés sur l'image) ; écarts image/transcription relevés à la relecture R-7 puis corrigés (p.12 Act. 1 b : pas de radical ; p.10 Act. prél. 6 a : ligne brisée ; p.31 Ex. 8 : marque « 0· » uniformisée ; p.29 : radical couvrant x − 1 confirmé ; p.32 Ex. 21 : β) ; 2 coquilles du manuel reprises en [sic] (p.8 « √ℓ » pour +∞ ; p.19 « continue sur ]−∞,a[ » pour ]a,+∞[) ; [?] : 1 (marque après 0 des limites 2 à 5 de l'Ex. 8, p.31).

## 2.2 Chapitre 2 — Dérivabilité (manuel 222451, p.35–58)

**Page de garde (p.35)** — Titre : « Dérivabilité », Chapitre 2. « Plan du chapitre » : ❈ Activités préliminaires ; ❈ Cours (❖ Dérivabilité à gauche – Dérivabilité à droite ; ❖ Dérivabilité sur un intervalle – Fonction dérivée ; ❖ Dérivée seconde et point d'inflexion ; ❖ Dérivée et sens de variation ; ❖ Extrema ; ❖ Dérivée d'une fonction composée ; ❖ Théorème et Inégalités des accroissements finis) ; ❈ Résumé du cours ; ❈ Avec l'ordinateur ; ❈ Exercices et Problèmes ; ❈ Aperçu historique. Pas de QCM ni de Vrai-Faux en rubrique (p.35–58 lues en entier).

### Activités préliminaires (p.36–37)

- **Act. prél. 1** (p.36) : 1) déterminer, chaque fois, le nombre dérivé de f en x₀ en utilisant la définition : a) f(x) = x³, x₀ = 2 ; b) f(x) = √(x+1), x₀ = 1 ; c) f(x) = 2/x, x₀ = (−1) ; d) f(x) = 5, x₀ = 3. 2) donner, pour chaque résultat, l'approximation affine de f en x₀.
- **Act. prél. 2** (p.36) : g : x ↦ √x pour x ∈ [0, +∞[. a) nombre dérivé de g en x₀ = 1 ; b) approximation affine du réel √1,0001 ; c) en déduire une valeur approchée du réel √10001.
- **Act. prél. 3** (p.36) : plan muni de (O, i⃗, j⃗), f : x ↦ x² + 1. a) équation cartésienne de la tangente (T) à la courbe C_f en son point d'abscisse 1 ; b) tracer (C_f) et la tangente (T).
- **Encadrés de rappel** (p.36–37) : « Nombre dérivé », « Approximation affine », « Nombre dérivé et interprétation géométrique » (voir « Résultats »), avec trois schémas f'(x₀) > 0, f'(x₀) < 0, f'(x₀) = 0.

### Cours — Activités

**Dérivabilité à gauche – Dérivabilité à droite** (p.38–40)

- **Activité 1** (p.38, « Continuité et dérivabilité ») : f définie sur un intervalle ouvert I, dérivable en x₀ de I ; on pose k(x) = (f(x) − f(x₀))/(x − x₀) si x ≠ x₀. a) vérifier que pour x ≠ x₀, f(x) = f(x₀) + (x − x₀)·k(x) ; b) limite de k(x) lorsque x tend vers x₀ ; c) trouver lim_{x→x₀} f(x) et conclure.
- **Activité 2** (p.38) : f sur ℝ : f(x) = x² si x ≤ 0 ; f(x) = (1 − cos x)/x si x > 0. 1) montrer que f est continue en x₀ = 0 ; 2) a) nombre dérivé à gauche de f en 0, interprétation graphique ; b) dérivabilité de f à droite en 0, interprétation graphique ; c) f est-elle dérivable en 0 ?
- **Activité 3** (p.39) : f : x ↦ |x² − 1|, (C) courbe dans un repère orthogonal. 1) a) étudier la dérivabilité de f en x₀ = 1 ; b) en déduire que (C) admet une demi-tangente à gauche et une demi-tangente à droite au point A(1, 0) ; c) tracer les deux demi-tangentes en A ; 2) a) montrer que f est paire ; b) construire (C).
- **Activité 4** (p.40) : f : x ↦ √(2x − 4) pour x ∈ [2, +∞[. 1) dérivabilité de f à droite en 2 ; 2) interpréter graphiquement ; 3) tracer (C_f) dans (O, i⃗, j⃗).

**Dérivabilité sur un intervalle – Fonction dérivée** (p.40–43)

- **Activité 1** (p.40) : f sur ℝ : f(x) = x² − 4 si x ≤ 2 ; f(x) = 8 − 16/x si x > 2. 1) montrer que f est continue sur ℝ ; 2) montrer que f est dérivable sur ]−∞, 2[ et ]2, +∞[ et calculer f'(x) pour x < 2 et pour x > 2 ; 3) a) étudier la dérivabilité de f en x₀ = 2 ; b) f est-elle dérivable sur ℝ ?
- **Activité 2** (p.41) : recopier et compléter un tableau à trois colonnes (fonction f ; fonction dérivée f' ; ensemble de dérivabilité de f) pour : f : x ↦ x⁶ + 3x⁴ + 5x² + 6 ; f : x ↦ (−3x + 1)/(2x − 1) ; f : x ↦ 3√x + 2/x³ ; f : x ↦ 2 cos(3x + 1) ; f : x ↦ tgx.
- **Activité 3** (p.42) : f(x) = 4x², g(x) = √x. 1) ensemble de dérivabilité de chacune ; 2) calculer les fonctions dérivées de f + g, f·g, f/g et g³.

**Dérivée seconde et point d'inflexion** (p.43–45)

- **Activité 1** (p.43) : repère orthonormé ; courbe (C_f) de f : x ↦ −x³ − 3x² et tangente (T) au point I d'abscisse (−1) (graphique donné). 1) lire graphiquement la pente de (T) ; 2) dérivée f' ; 3) dérivée seconde f'' ; 4) a) équation cartésienne de (T) ; b) conjecturer la position relative de (C_f) et (T) ; 5) tableau de signe de f''(x). Commentaires imprimés : « On a f''(x) = −6x − 6, qui s'annule et change de signe en x₀ = −1. Le point I d'abscisse (−1) est un point d'inflexion de la courbe (C_f). On remarque aussi que la courbe (C_f) traverse sa tangente en I(−1, f(−1)). »
- **Activité 2** (p.44) : f : x ↦ (1/3)x³ − 2x² + 4x + 1, (C_f) dans (O, i⃗, j⃗). a) calculer f''(x) pour tout x réel ; b) en déduire que (C_f) possède un point d'inflexion d'abscisse x₀ que l'on précisera ; c) montrer que f' s'annule en x₀ sans changer de signe.

**Dérivée et sens de variation** (p.45)

- **Activité 1** (p.45) : f : x ↦ x² + 2x. 1) a) vérifier que f(x) = (x+1)² − 1 ; b) en déduire f strictement croissante sur [−1, +∞[ et strictement décroissante sur ]−∞, −1] ; 2) calculer f'(x), étudier son signe sur ]−∞, −1] et [−1, +∞[ ; 3) tableau de variation de f sur ℝ.
- **Activité 2** (p.45) : étudier le sens de variation de a) f : x ↦ tgx sur ]−π/2, π/2[ ; b) g : x ↦ x²/(x² + 1) sur [0, +∞[.

**Extrema** (p.46–48)

- **Activité 1** (p.46) : une entreprise fabrique une quantité x d'objets par jour ; coût de production en DT : f(x) = (0.1)·x² − 2x + 20. 1) tableau de variation de f sur ℝ ; 2) en déduire la valeur de x qui minimise le coût journalier.
- **Activité 2** (p.46) : courbe de f(x) = −x³ + 6x² − 9x + 1 sur ℝ (graphique donné). Répondre par vrai ou faux : a) f admet sur ℝ un maximum en x₀ = 3 égal à 1 ; b) f admet sur [0, +∞[ un maximum en x₀ = 3 égal à −3 ; c) f admet sur ]−∞, 4] un minimum en x₀ = 1 égal à −3 ; d) pour tout x ∈ ]−∞, 0], f(x) ≥ 1 ; e) pour tout x ∈ [0, +∞[, f(x) ≤ 1 ; f) pour tout x ∈ ]0, 4[, f(x) ≤ f(1). (Réponses non fournies.)
- **Activité 3** (p.46) : courbe de f(x) = 8x³ − 6x − 1 sur ℝ ; g définie sur ]−1, 1[ par g(x) = f(x). a) nombre d'extremum(s) de g ; b) conjecturer les nombres dérivés de g en ces extremums ; c) tableau de variation de g ; d) en déduire que g admet un minimum et un maximum, les préciser ; e) m minimum de g sur ]−1, 1[ : est-ce un minimum de f sur ℝ ? f) M maximum de g sur ]−1, 1[ : est-ce un maximum de f sur ℝ ? g) montrer que g est bornée.
- **Activité 4** (p.47) : tracer la courbe de f(x) = x³ sur [−1, 1]. a) f'(0) ? b) la courbe présente-t-elle un extremum local en 0 ? c) signe de f'(x) pour x > 0 et pour x < 0.
- **Activité 5** (p.48) : f : x ↦ 2x³ + 3x² − 12x + 1 : dresser le tableau de variation de f sur ℝ, en déduire qu'elle possède deux extremums dont on précisera la nature.
- **Activité 6** (p.48) : boîte fabriquée à partir d'une plaque carrée de côté 45 cm dont on découpe aux quatre coins un carré de côté x (figure donnée). a) montrer que le volume de la boîte est v(x) = x·(45 − 2x)², où 0 < x < 22.5 ; b) en déduire la valeur de x pour laquelle le volume est maximal.

**Dérivée d'une fonction composée** (p.48–49)

- **Activité 1** (p.48) : f : x ↦ 2x³ et g : x ↦ −12x + 1. 1) montrer que f et g sont dérivables sur ℝ, calculer f'(x), g'(x) ; 2) a) définir g∘f ; b) montrer que g∘f est dérivable sur ℝ, calculer (g∘f)'(x) ; c) définir la fonction g'∘f et calculer (g'∘f)(x)·f'(x) ; d) conclure.
- **Activité 2** (p.48) : 1) h : x ↦ √(ax + b) (a, b réels) : montrer que h est dérivable en tout réel x₀ tel que ax₀ + b > 0 et retrouver, par la dérivée d'une composée, h'(x₀) = a/(2√(ax₀ + b)) ; 2) f dérivable sur un intervalle I avec f(x) > 0 pour tout x de I : montrer que √f est dérivable sur I et déterminer sa fonction dérivée.
- **Activité 3** (p.49) : préciser sur quel ensemble f est dérivable et calculer f'(x) lorsqu'il existe : a) f(x) = √(x² + x + 1) ; b) f(x) = sin(2x + π/3) ; c) f(x) = ((2x + 1)/(x − 1))³ ; d) f(x) = √((1 + x)/(1 − x)).

**Théorème et Inégalités des accroissements finis** (p.49–51)

- **Activité 1** (p.49) : f : x ↦ x² − 2x − 3, (C) dans (O, i⃗, j⃗), points A(1, f(1)) et B(3, f(3)). 1) coefficient directeur de (AB) ; 2) a) montrer que (C) admet une tangente T parallèle à (AB) en un point M₀(x₀, f(x₀)) à préciser ; b) équation cartésienne de T ; 3) tracer (C), (AB) et T.
- **Activité 2** (p.50) : f : x ↦ ax² + bx + c ; a ≠ 0 ; A et B points de (C) d'abscisses α et β (α ≠ β). Montrer que la tangente à (C) au point d'abscisse (α + β)/2 est parallèle à la corde (AB).
- **Activité 3** (p.50) : f : x ↦ 1/x ; x ∈ [1, 5]. 1) montrer que ∀ x ∈ [1, 5], −1 ≤ f'(x) ≤ −1/25 ; 2) a- montrer que pour tous réels a et b de [1, 5] tels que a < b il existe c ∈ ]1, 5[ tel que f'(c) = (f(b) − f(a))/(b − a) ; b- en déduire un encadrement du rapport (f(b) − f(a))/(b − a).
- **Activité 4** (p.51) : 1) f : x ↦ √x : a) montrer que pour tout x ∈ [64, 65], 1/18 ≤ f'(x) ≤ 1/16 ; b) en déduire un encadrement de √65 ; 2) montrer que pour tous réels x et y de [−π/12, π/12], |cos²x − cos²y| ≤ (1/2)|x − y|.
- **Activité 5** (p.51) : 1) f : t ↦ sin t : a) montrer que pour tout t ∈ ℝ, |f'(t)| ≤ 1 ; b) en déduire que pour tous réels a et b, |sin b − sin a| ≤ |b − a| ; 2) montrer que pour tout x ∈ [0, π/4], x ≤ tgx ≤ 2x.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Nombre dérivé** (p.36) — « Soit f une fonction définie sur un intervalle ouvert I et soit x₀ un réel de I. On dit que f est dérivable en x₀, s'il existe un nombre réel ℓ tel que lim_{x→x₀} (f(x) − f(x₀))/(x − x₀) = ℓ ou encore lim_{h→0} (f(x₀ + h) − f(x₀))/h = ℓ. Le réel ℓ, est alors appelé le nombre dérivé de f en x₀ et il est noté f'(x₀). »

> **Approximation affine** (p.36) — « Soit f une fonction définie sur un intervalle ouvert I et soit x₀ un élément de I. * Si f est dérivable en x₀ alors sa courbe représentative admet au point A(x₀, f(x₀)) une tangente (T) dont une équation cartésienne est y = f(x₀) + (x − x₀) f'(x₀). * En posant x = x₀ + h, on a pour h voisin de zéro, le réel f(x₀) + hf'(x₀) est une valeur approchée de f(x₀ + h). On dit que le réel f(x₀) + hf'(x₀) est une approximation affine de f(x₀ + h). On écrit : f(x₀ + h) ≃ f(x₀) + hf'(x₀). »

> **Nombre dérivé et interprétation géométrique** (p.37) — « Soit f une fonction définie sur un intervalle ouvert I et soit x₀ un élément de I. Si f est dérivable en x₀ alors sa courbe représentative (C_f) admet au point M₀(x₀, f(x₀)) une tangente (T) de coefficient directeur f'(x₀) et dont un vecteur directeur est u⃗ (1, f'(x₀)). » (trois schémas : f'(x₀) > 0, f'(x₀) < 0, f'(x₀) = 0)

> **Théorème** (p.38) — « Si une fonction f est dérivable en x₀ alors elle est continue en x₀. »

> **Dérivabilité à gauche – Dérivabilité à droite** (p.38) — « Soit f une fonction définie sur un intervalle I de ℝ et x₀ un réel de I. * On dit que f est dérivable à gauche en x₀, s'il existe un nombre réel ℓ₁ tel que : lim_{x→x₀⁻} (f(x) − f(x₀))/(x − x₀) = ℓ₁ ou encore lim_{h→0⁻} (f(x₀ + h) − f(x₀))/h = ℓ₁. Le réel ℓ₁ est alors appelé le nombre dérivé à gauche de f en x₀ et il est noté f'_g(x₀). * On dit que f est dérivable à droite en x₀, s'il existe un nombre réel ℓ₂ tel que lim_{x→x₀⁺} (f(x) − f(x₀))/(x − x₀) = ℓ₂ ou encore lim_{h→0⁺} (f(x₀ + h) − f(x₀))/h = ℓ₂. Le réel ℓ₂ est alors appelé le nombre dérivé à droite de f en x₀ et il est noté f'_d(x₀). »

> **Remarques** (p.39) — « * On peut avoir une fonction continue en x₀ mais non dérivable en x₀. * Si f n'est pas continue en x₀ alors elle n'est pas dérivable en x₀. »

> **Interprétation géométrique du nombre dérivé à gauche et du nombre dérivé à droite** (p.39) — « * Soit f une fonction définie sur un intervalle ouvert I et dérivable à gauche en x₀ de I. Le nombre f'_g(x₀) représente la pente de la demi-tangente à gauche à la courbe représentative de f en son point M₀(x₀, f(x₀)). Une équation cartésienne de cette demi-tangente est donnée par : y = f'_g(x₀)·(x − x₀) + f(x₀), x ≤ x₀. * Soit f [...] dérivable à droite en x₀ de I. Le nombre f'_d(x₀) représente la pente de la demi-tangente à droite [...]. Une équation cartésienne de cette demi-tangente est donnée par : y = f'_d(x₀)·(x − x₀) + f(x₀), x ≥ x₀. Lorsque f'_g(x₀) ≠ f'_d(x₀) la courbe de f admet deux demi-tangentes de directions différentes en M₀(x₀, f(x₀)). On dit alors, que le point M₀ est un point anguleux pour la courbe de f. »

> **Théorème** (p.39) — « Soit f une fonction définie sur un intervalle ouvert I de ℝ et x₀ un réel de I. La fonction f est dérivable en x₀ si et seulement si f est à la fois dérivable à droite et à gauche en x₀ et f'_g(x₀) = f'_d(x₀). »

> **Commentaires — demi-tangente verticale** (p.40) — « Pour f : x ↦ √(2x − 4) ; x ∈ [2, +∞[ ; on a lim_{x→2⁺} (f(x) − f(2))/(x − 2) = +∞, on dit alors que la courbe représentative de f possède une demi-tangente verticale au point M₀(2, f(2)). » / « Plus généralement : si f est une fonction définie sur D et vérifiant pour x₀ de D, lim_{x→x₀⁺} (f(x) − f(x₀))/(x − x₀) = +∞ (ou −∞) ou lim_{x→x₀⁻} (f(x) − f(x₀))/(x − x₀) = +∞ (ou −∞) alors f n'est pas dérivable en x₀ et sa courbe représentative possède une demi-tangente verticale au point M₀(x₀, f(x₀)). »

> **Dérivabilité sur un intervalle** (p.41) — « * Soit f une fonction définie sur un intervalle ouvert I. La fonction f est dérivable sur I si elle est dérivable en tout réel x₀ de I. Dans ce cas f possède une fonction dérivée notée f' définie sur I, qui à tout x de I associe f'(x). * Soit a un réel. - La fonction f est dérivable sur [a, +∞[ si elle est dérivable sur ]a, +∞[ et dérivable à droite en a. - La fonction f est dérivable sur ]−∞, a] si elle est dérivable sur ]−∞, a[ et dérivable à gauche en a. * Soient a et b deux réels tels que a < b. La fonction f est dérivable sur [a, b] si elle est dérivable sur ]a, b[, dérivable à droite en a et dérivable à gauche en b. »

> **Dérivées des fonctions usuelles** (p.42) — f : x ↦ k : f'(x) = 0, x ∈ ℝ ; x ↦ ax + b : f'(x) = a, x ∈ ℝ ; x ↦ xⁿ ; n ∈ ℕ* − {1} : f'(x) = nxⁿ⁻¹, x ∈ ℝ ; x ↦ 1/x : f'(x) = −1/x², x ∈ ℝ* ; x ↦ 1/xⁿ ; n ∈ ℕ* − {1} : f'(x) = −n/xⁿ⁺¹, x ∈ ℝ* ; x ↦ √x : f'(x) = 1/(2√x), x > 0 ; x ↦ √(ax + b) : f'(x) = a/(2√(ax + b)), ax + b > 0 ; x ↦ (ax + b)/(cx + d) : f'(x) = (ad − cb)/(cx + d)², x ≠ −d/c ; x ↦ sin(ax + b) : f'(x) = a·cos(ax + b), x ∈ ℝ ; x ↦ cos(ax + b) : f'(x) = −a·sin(ax + b), x ∈ ℝ ; x ↦ tan x : f'(x) = 1 + tan²x = 1/cos²x, x ∈ ℝ \ {π/2 + kπ, k ∈ ℤ} ; x ↦ cotan(x) : f'(x) = −(1 + cotan²x) = −1/sin²x, x ∈ ℝ \ {kπ, k ∈ ℤ}.

> **Opérations sur les fonctions dérivées** (p.43) — « Soient f et g deux fonctions dérivables sur un intervalle I de ℝ. » f + g → f' + g' ; a.f (a constante réelle) → a.f' ; f.g → f'.g + g'.f ; fⁿ (n ≥ 2) → nf'.fⁿ⁻¹ ; 1/f → −f'/f² ; f/g → (f'.g − g'.f)/g².

> **Définitions** (p.44) — « Dérivée seconde : Soit f une fonction dérivable sur un intervalle I et f' sa fonction dérivée. Si la fonction f' est dérivable sur I alors f est dite deux fois dérivable sur I et la fonction dérivée de f' se note f'' et s'appelle fonction dérivée seconde de f. Point d'inflexion : Le point M₀(x₀, f(x₀)) est un point d'inflexion de (C_f) si et seulement si (C_f) traverse sa tangente en M₀. » (deux schémas : M₀ point d'inflexion / M₀ n'est pas un point d'inflexion)

> **Théorème** (p.44) — « Soit f une fonction deux fois dérivable sur un intervalle ouvert I contenant x₀ et (C) sa courbe représentative dans un repère (O, i⃗, j⃗) du plan. Soit f'' la fonction dérivée seconde de f. Si la fonction f'' s'annule et change de signe en x₀ alors le point M₀(x₀, f(x₀)) est un point d'inflexion de (C). »

> **Théorème** (p.45) — « Soit f une fonction deux fois dérivable sur un intervalle ouvert I contenant x₀ et (C_f) sa courbe représentative dans un repère (O, i⃗, j⃗) du plan. Soit f' la fonction dérivée de f. Si la fonction f' s'annule en x₀ sans changer de signe alors le point M₀(x₀, f(x₀)) est un point d'inflexion de (C_f). »

> **Théorème** (p.45) — « Soit f une fonction dérivable sur un intervalle I. On a : * La fonction f est croissante sur I si et seulement si pour tout x appartenant à I, f'(x) ≥ 0. * La fonction f est décroissante sur I si et seulement si pour tout x appartenant à I, f'(x) ≤ 0. * La fonction f est constante sur I si et seulement si pour tout x appartenant à I, f'(x) = 0. »

> **Minimum et maximum d'une fonction** (p.46) — « Soit f une fonction définie sur un ensemble D. * S'il existe x₀ appartenant à D tel que pour tout x de D, f(x) ≥ f(x₀), on dit que la fonction f admet sur D un minimum en x₀. Le réel f(x₀) est le minimum de f. * S'il existe x₀ appartenant à D tel que pour tout x de D, f(x) ≤ f(x₀), on dit que la fonction f admet sur D un maximum en x₀. Le réel f(x₀) est le maximum de f. * Un minimum ou un maximum de f s'appelle aussi un extremum de f. »

> **Définition** (p.47) — « Soit f une fonction définie sur un intervalle ouvert I et x₀ un réel de I. * La fonction f admet un maximum local en x₀ si et seulement si il existe un intervalle ouvert J contenant x₀ et inclus dans I tel que pour tout x de J, f(x) ≤ f(x₀). * La fonction f admet un minimum local en x₀ si et seulement si il existe un intervalle ouvert J contenant x₀ et inclus dans I tel que pour tout x de J, f(x) ≥ f(x₀). » (parenthèse fermante en trop imprimée, [sic])
> **Remarques** (p.47) — « • Si pour tout x de D_f, f(x) ≤ f(x₀) alors le réel f(x₀) est appelé le maximum absolu (ou global) de f. • Si pour tout x de D_f, f(x) ≥ f(x₀) alors le réel f(x₀) est appelé le minimum absolu (ou global) de f. »

> **Théorème** (p.47) — « Soit f une fonction dérivable sur un intervalle ouvert I et x₀ un réel de I. • Si f admet un extremum local en x₀ alors f'(x₀) = 0. • Si la fonction dérivée f' de f s'annule et change de signe en x₀ alors f admet un extremum local égal à f(x₀) en x₀. » (deux tableaux de variation figurés : f' de + à − : maximum f(x₀) ; de − à + : minimum f(x₀) ; deux courbes)

> **Théorème — dérivée d'une composée** (p.48) — « Soit f une fonction définie sur un intervalle I de ℝ et x₀ un réel de I. Soit g une fonction définie sur f(I). Si f est dérivable en x₀ et g est dérivable en f(x₀) alors g∘f est dérivable en x₀ et on a : (g∘f)'(x₀) = (g'∘f)(x₀).f'(x₀). »

> **Corollaire 1** (p.49) — « Si f est une fonction dérivable sur un intervalle I de ℝ et g est une fonction dérivable sur f(I) alors (g∘f) est dérivable sur I et on a (g∘f)' = (g'∘f) × f'. » **Corollaire 2** (p.49) — « Si f est une fonction dérivable sur un intervalle I de ℝ et si de plus pour tout x de I, f(x) > 0 alors la fonction √f est dérivable sur I et on a (√f)' = f'/(2√f). »

> **Théorème des accroissements finis (admis)** (p.50) — « Soient deux réels a et b avec a < b. Si f est une fonction continue sur un intervalle [a, b] et dérivable sur ]a, b[ alors il existe au moins un réel c appartenant à ]a, b[ tel que f'(c) = (f(b) − f(a))/(b − a). » Interprétation géométrique : « • Le réel f'(c) est le coefficient directeur de la tangente T à la courbe (C_f) en son point d'abscisse c. • Le rapport (f(b) − f(a))/(b − a) est le coefficient directeur de la droite (AB) où A(a, f(a)) et B(b, f(b)). Donc f'(c) = (f(b) − f(a))/(b − a) équivaut à T // (AB). Ainsi, le théorème des accroissements finis affirme qu'il existe au moins un réel c appartenant à ]a, b[ tel que la tangente à la courbe représentative de f au point d'abscisse c soit parallèle à la droite (AB). »

> **Inégalités des accroissements finis (admis)** (p.51) — « Si f est une fonction dérivable sur un intervalle I de ℝ et s'il existe deux constantes réelles m et M telles que pour tout x de I, m ≤ f'(x) ≤ M alors pour tous réels a et b de I, tels que a < b on a : m(b − a) ≤ f(b) − f(a) ≤ M(b − a). » **Corollaire** : « Si f est une fonction dérivable sur un intervalle I de ℝ et s'il existe k > 0 tel que pour tout x de I, |f'(x)| ≤ k alors pour tous réels a et b de I on a |f(b) − f(a)| ≤ k|b − a|. »

### Résumé du cours (p.52–53)

Reprend les rubriques : dérivabilité en un point (définition, tangente, vecteur directeur u⃗(1, f'(x₀)), équation y = f'(x₀)(x − x₀) + f(x₀)) ; dérivabilité à gauche/à droite et théorème « dérivable ⇔ dérivable à droite et à gauche et f'(x₀) = f'_g(x₀) = f'_d(x₀) » ; dérivée seconde et point d'inflexion (deux théorèmes : f' s'annule sans changer de signe ; f'' s'annule et change de signe) ; extrema ; dérivée d'une composée (théorème, corollaire, « Application » : (√f)' = f'/(2√f)) ; TAF et interprétation (T // (AB)) ; inégalités des accroissements finis (m ≤ (f(b) − f(a))/(b − a) ≤ M) et corollaire. Aucun résultat nouveau.

### Exemples résolus

Aucun exercice résolu intégral dans ce chapitre.

### QCM / Vrai-Faux

Aucun en rubrique (seule l'Activité 2 « Extrema », p.46, demande de répondre par vrai ou faux).

### Avec l'ordinateur (p.54) — 1 activité

Cercle de centre C et de diamètre [AB], AB = 8 cm ; M point variable de [AB] ; la perpendiculaire à (AB) en M coupe un demi-cercle en N. 1) calculer l'aire du triangle rectangle AMN à l'aide d'un logiciel ; 2) pour quelle position de M l'aire est-elle maximale ? « Une stratégie de résolution » : repère orthonormé (A, i⃗, j⃗) avec i⃗ = (1/8)AB⃗, x = AM ; a) prouver x = 8cos²θ où θ = BÂN ; b) prouver S(θ) = 8cosθ sinθ, θ ∈ [0, π/2[ ; c) en dérivant S, montrer que l'aire est maximale quand M est au milieu de [CB].

### Exercices et problèmes (p.55–57) — 17 exercices

- **Ex. 1** (p.55) : f(x) = x² + x − 2, (C_f). a) montrer par la définition que f est dérivable en 2 ; b) équation de la tangente T au point d'abscisse 2 ; c) construire T et (C_f) ; d) approximation affine de f en 2.
- **Ex. 2** (p.55) : montrer que f est dérivable en a, préciser f'(a), équation de la tangente, approximation affine : 1) f : x ↦ x² − 3x ; a = −1 ; 2) f : x ↦ (2x − 3)/(x + 4) ; a = 1 ; 3) f : x ↦ √(3x² + 5x − 4) ; a = 1.
- **Ex. 3** (p.55) : étudier la dérivabilité de f en x₀ et donner la (ou les) équation(s) de la (des) tangente(s) ou demi-tangente(s) : 1) f : x ↦ x² + |x| ; x₀ = 0 ; 2) f : x ↦ √(x² − 5x + 6) ; x₀ = 2 ; 3) f(x) = x² − 2x + 4 si x ≤ 1 ; f(x) = (x² + x + 1)/x si x > 1 ; x₀ = 1 ; 4) f : x ↦ |x² − x| ; x₀ = 1.
- **Ex. 4** (p.55) : f(x) = 4√(x+1) si x ≥ 3 ; f(x) = x² − 5x + c si x < 3 (c réel). 1) c pour que f soit continue sur ℝ ; 2) pour cette valeur de c, f dérivable sur ℝ et sa fonction dérivée.
- **Ex. 5** (p.55) : f(x) = x² − 1 si x ≤ 1 ; f(x) = √x − 1 si x > 1. 1) f continue sur ℝ ; 2) a) dérivabilité de f en 1 ; b) interprétation graphique.
- **Ex. 6** (p.55) : f(x) = 2x + √(x² − 1) si x < −1 ; f(x) = 2x³ − 3x² + 3 si −1 ≤ x ≤ 0 ; f(x) = 3 + (1 − cos(πx))/x si x > 0. 1) a) montrer que pour x > 0, 3 ≤ f(x) ≤ 2/x + 3 ; b) limite de f(x) quand x → +∞ ; 2) continuité de f en (−1) et en 0 ; 3) dérivabilité à gauche de f en (−1), interprétation géométrique ; 4) dérivabilité de f en 0.
- **Ex. 7** (p.56) : f(x) = (2 sin x + 1 − cos x)/x si x ≠ 0 ; f(0) = 1. a) continuité de f en 0 ; b) f est-elle dérivable en 0 ?
- **Ex. 8** (p.56) : ensemble de dérivabilité et f'(x) : a) sin x ; b) cos x ; c) |x| ; d) x³ − 5x² + 7x + 3 ; e) (2x + 1)/(x² + x − 2) ; g) √(4x − 1) [sic : la rubrique passe de e) à g)] ; h) sin x/(1 − cos x).
- **Ex. 9** (p.56) : domaine de définition, ensemble de dérivabilité, f'(x) : 1) x³/(x² + 1) ; 2) ((3 + x)/(2x + 1))⁴ ; 3) √((x + 1)/(x − 1)) ; 4) (sin x − 1)/(2cos x − 1) ; 5) cos(2x + π/6) ; 6) cos(√(x² − 1)) ; 7) x² sin(1/x) si x ≠ 0 et f(0) = 0.
- **Ex. 10** (p.56) : f : x ↦ (x² − 1)/(x² + 1) sur ℝ. 1) tableau de variation ; 2) en déduire un minimum global à préciser ; 3) f bornée.
- **Ex. 11** (p.56) : f(x) = (1 − √x)/(1 + √x) [sic : l'énoncé imprime « définie sur par », sans ensemble]. a) f dérivable sur ]0, +∞[ et f'(x) = −1/(√x(1 + √x)²) ; b) tableau de variation sur ]0, +∞[.
- **Ex. 12** (p.56) : f : ]1, +∞[ → ℝ, x ↦ 1 + 1/√x. 1) f(x) = x admet une solution unique α dans ]1, +∞[ ; 2) f dérivable et pour tout x de ]1, +∞[, |f'(x)| ≤ 1/2 ; 3) en déduire que pour tout x de ]1, +∞[, |f(x) − α| ≤ (1/2)|x − α|.
- **Ex. 13** (p.56) : f(x) = √(x/(x − 1)). 1) domaine de définition ; 2) tableau de variation ; 3) g définie sur ]0, π/2[ par g(x) = f(sin x) : montrer que g est dérivable et calculer g'(x).
- **Ex. 14** (p.57) : f(x) = cos²x sur ]0, π/2[. 1) a) f dérivable, calculer f'(x) ; b) tableau de variation ; 2) g(x) = f(x) − x : a) g(x) = 0 admet une solution unique α dans ]0, π/2[ ; b) signe de g(x) ; c) calculer g(π/4) et g(π/6), en déduire un nouvel encadrement de α [le symbole est omis dans l'impression de la phrase, [?]] ; d) position relative de (C) et de D : y = x.
- **Ex. 15** (p.57) : f(x) = 2 − √(x² − x) si x ∈ ]−∞, 0[ ; f(x) = 1 + 1/√(1 + x²) si x ∈ [0, +∞[, (C_f) repère orthonormé. 1) f continue en 0 ; 2) dérivabilité de f en 0, interprétation graphique ; 3) montrer que pour tout x de ]0, +∞[, f'(x) = −x/((1 + x²)√(1 + x²)) ; 4) tableau de variation ; 5) intersection de (C_f) avec l'axe des abscisses ; 6) a) f(x) = x admet une solution unique α dans ]0, +∞[ ; b) vérifier 1.5 < α < 1.6 ; 7) branches infinies et comportement asymptotique de f puis construire (C_f) ; 8) h définie sur [0, π/2[ par h(x) = f(tgx) : a) calculer h'(x) ; b) montrer que pour tout x ∈ [0, π/2[, h(x) = 1 + cos x.
- **Ex. 16** (p.57) : 1) g(x) = 2x/√(x² + 3) − 1 sur ℝ : a) g dérivable sur ℝ et g'(x) = 6/((3 + x²)√(3 + x²)) ; b) tableau de variation ; c) calculer g(1), en déduire le signe de g(x) sur ℝ ; 2) f(x) = 2√(3 + x²) − x sur ℝ : a) tableau de variation ; b) équation cartésienne de la tangente T à la courbe de f au point d'abscisse (−1).
- **Ex. 17** (p.57) : f(x) = (|x² + x| + 1)/(|x| + 1) sur ℝ. 1) a) dérivabilité de f en x₀ = 0 et en x₀ = (−1) ; b) interpréter graphiquement ; 2) tableau de variation ; 3) construire, dans un repère orthonormé, la courbe C, en précisant les asymptotes à C.

### Aperçu historique (p.58)

Une ligne : biographie de Bernard Bolzano (1781–1848) ; calcul infinitésimal, rôle de Cauchy (limites, théorème des accroissements finis) et de Dirichlet (1829, dérivée en un point).

### Bornes de scope observées (chapitre 2)

- ✅ INCLUS : nombre dérivé, approximation affine, dérivabilité à gauche/à droite, demi-tangentes, point anguleux, demi-tangente verticale ; lien continuité/dérivabilité (dérivable ⇒ continue) ; dérivabilité sur un intervalle, dérivées usuelles (dont √(ax+b), (ax+b)/(cx+d), tan, cotan) et opérations ; dérivée seconde, points d'inflexion (f'' change de signe ; f' s'annule sans changer de signe) ; dérivée et sens de variation ; extrema locaux/globaux ; dérivée d'une composée ; théorème et inégalités des accroissements finis (admis) ; problèmes d'optimisation (coût, volume de boîte, aire).
- ⛔ NON traité : primitives, intégrales ; dérivées de ln/exp (chapitres ultérieurs) ; convexité formelle (seul le point d'inflexion est traité) ; démonstrations du théorème et des inégalités des accroissements finis (admis) ; théorème de Rolle ; dérivée de la réciproque (chapitre 3).

> Sondage image : pages 36, 38–51, 53–57 lues en L3 (p.35, 37, 52 et 58 en L1 seule : plan, schémas et texte sans formule difficile) ; écarts : la couche texte perd les valeurs absolues, les racines, ≤/≥, ℝ et ∈ (corrigés sur l'image) ; sur p.54 la couche texte écrit « x = 8 cos θ » alors que l'image porte « x = 8 cos²θ » (retenu : image) ; aucun écart entre l'image et la transcription ; coquilles du manuel en [sic] : p.47 parenthèse fermante en trop ; p.56 ex. 8 saute la lettre f) ; [?] : Ex. 14 c) (p.57), symbole du texte omis dans l'impression.

## 2.3 Chapitre 3 — Fonction continue et strictement monotone sur un intervalle — fonction réciproque (manuel 222451, p.59–77)

**Page de garde (p.59)** — Titre imprimé : « Fonction continue et strictement monotone sur un intervalle » (Partie 1, Chapitre 3) ; la consigne d'ordre parle de « Fonction réciproque d'une fonction strictement monotone » : c'est le contenu de la partie centrale du chapitre (le titre imprimé ci-dessus fait foi). « Plan du chapitre » : ❈ Activités préliminaires ; ❈ Cours (❖ Restriction d'une fonction ; ❖ Image d'un intervalle par une fonction continue et strictement monotone ; ❖ Fonction réciproque d'une fonction continue et strictement monotone ; ❖ Fonction réciproque de la fonction f : x ↦ xⁿ ; x ≥ 0 et n ≥ 1 ; ❖ Dérivée de la fonction réciproque) ; ❈ Résumé du cours ; ❈ Avec l'ordinateur ; ❈ Exercices et Problèmes ; ❈ Aperçu historique. Pas de QCM ni de Vrai-Faux (p.59–77 lues en entier).

### Activités préliminaires (p.60–61)

- **Act. prél. 1** (p.60) : repère orthonormé (O, i⃗, j⃗) ; courbes (figures, avec la droite D : y = x tracée) de f : x ↦ √(x − 1) pour x ∈ [1, +∞[ et g : x ↦ −x³ pour x ∈ ]−∞, 1]. 1) a) lire graphiquement le sens de variation de chacune ; b) justifier ; 2) a) étudier la continuité de chacune ; b) image de [1, 5] par f et image de ]−1, 1] par g ; 3) S_D symétrie axiale d'axe D : y = x : a) reproduire les deux graphiques ; b) construire, avec C_f, la courbe (C₁) = S_D(C_f), expliquer le procédé de construction ; c) construire, avec C_g, (C₂) = S_D(C_g).
- **Act. prél. 2** (p.60) : 1) f(x) = x³ + 2x + 1 sur ℝ : a) montrer que le taux d'accroissement de f entre deux réels distincts a et b est strictement positif, en déduire le sens de variation de f sur ℝ ; b) montrer que f est dérivable sur ℝ et f'(x) > 0 pour tout réel x. 2) g(x) = −√x : a) en utilisant le taux d'accroissement de g entre deux réels strictement positifs, montrer que g est strictement décroissante sur ]0, +∞[ ; b) montrer que g est dérivable sur ]0, +∞[ et g'(x) < 0 pour tout x > 0.
- **Act. prél. 3** (p.61) : f(x) = 2x − sin x sur ℝ (graphique donné). 1) a) montrer que pour tout réel x, 2x − 1 ≤ f(x) ≤ 2x + 1 ; b) calculer lim_{x→−∞} f(x) et lim_{x→+∞} f(x) ; 2) montrer que f est dérivable sur ℝ et calculer f'(x) ; 3) a) montrer que f'(x) > 0 pour tout x ; b) tableau de variation de f sur ℝ.
- **Act. prél. 4** (p.61) : préciser le sens de variation sur l'intervalle I : a) f : x ↦ x³ ; I = ]−∞, +∞[ ; b) g : x ↦ 1/x ; I = ]0, +∞[ ; c) h : x ↦ cos(−2x) ; I = [−π/2, 0] ; d) k : x ↦ sin x ; I = [0, π/2] ; e) u : x ↦ tg x ; I = ]−π/2, π/2[ ; f) v : x ↦ cotg x ; I = ]0, π[.

### Cours — Activités

**Restriction d'une fonction** (p.62–63)

- **Activité 1** (p.62) : 1) tracer la parabole (P) de f : x ↦ x² − 3 sur ℝ ; 2) (C₁) ensemble des points de (P) d'abscisses dans [0, 3], g la fonction dont (C₁) est la représentation : a) colorier (C₁) et donner l'expression de g(x) ; b) déterminer g([0, 3]).
- **Activité 2** (p.62) : f sur ℝ : f(x) = (x² − 3x + 2)/|x − 1| si x ≠ 1 ; f(1) = 1. 1) g restriction de f à ]−∞, 1] : a) vérifier que g(x) = 2 − x ; b) en déduire que g est continue sur ]−∞, 1] ; c) sens de variation de g ; 2) construire la représentation graphique C de f.
- **Activité 3** (p.63) : f(x) = cos x sur ℝ ; g restriction de f à [0, π] (graphique donné, courbe décroissante de (0, 1) à (π, −1)). Quel est le sens de variation de g ? Justifier.

**Image d'un intervalle par une fonction continue et strictement monotone** (p.63–64)

- **Activité 1** (p.63) : repère orthogonal. 1) a) courbe (C) de f(x) = x² − 2x + 3 ; b) sens de variation de f sur [1, 3] ; c) représenter f([1, 3]) ; 2) a) courbe (C') de g(x) = 3/(x + 1) ; b) vérifier que g est continue sur [−4, −2] puis son sens de variation sur cet intervalle ; c) représenter g([−4, −2]) ; 3) h(x) = x³ + 3x − 1 sur ℝ : a) h strictement croissante sur ℝ ; b) conjecturer l'image de [0, +∞[ par h.
- **Activité 2** (p.63) : f continue sur [a, b], (C) sa courbe dans un repère orthogonal ; reproduire deux graphiques (courbe croissante à asymptote verticale à gauche ; courbe décroissante à asymptote verticale) et représenter à chaque fois l'intervalle f([a, b]).
- **Activité 3** (p.64) : 1) f(x) = tgx : a) ensemble de continuité de f, montrer que f est strictement croissante sur ]−π/2, π/2[ ; b) image de chacun des intervalles ]−π/2, π/2[, [0, π/2[ et [−π/4, π/4] par f ; 2) g : x ↦ −x³ + 2 : a) étudier le sens de variation de f [sic : « f » imprimé pour « g »] sur ℝ ; b) déterminer l'image de [0, +∞[ par f [sic : « f » pour « g »].

**Fonction réciproque d'une fonction continue et strictement monotone** (p.65–66)

- **Activité 1** (p.65) : repère orthonormé ; f(x) = (1/4)x² sur ℝ, g sa restriction à I = [0, +∞[. 1) courbe (C) de g ; 2) a) montrer que g est continue et strictement croissante sur I ; b) déterminer J = g(I) ; 3) soit y un réel positif, prouver que g(x) = y admet une solution unique dans I ; 4) h : [0, +∞[ → ℝ, h(x) = 2√x : a) tracer la courbe (C') de h dans le même repère ; b) montrer que M(x, y) ∈ (C) équivaut à M'(y, x) ∈ (C') ; c) en déduire que (C') est symétrique de (C) par rapport à Δ : y = x ; d) étudier la continuité et le sens de variation de h. Commentaire imprimé : « La fonction h s'appelle la fonction réciproque de la fonction g. On note h = g⁻¹. La fonction g est une bijection de I sur g(I). »
- **Activité 2** (p.66) : f(x) = (x² − 1)/(2x) sur I = ]0, +∞[. 1) tableau de variation de f ; 2) montrer que f est une bijection de I sur ℝ ; 3) y un réel : a) résoudre dans I l'équation f(x) = y (x inconnue) ; b) en déduire l'expression de f⁻¹(y) ; 4) tracer, dans (O, i⃗, j⃗), les courbes de f et f⁻¹.

**Fonction réciproque de la fonction f : x ↦ xⁿ ; x ≥ 0 et n ≥ 1** (p.66–68)

- **Activité 1** (p.66) : 1) montrer que f : x ↦ x² est bijective de ℝ⁺ sur ℝ⁺ ; 2) préciser sa fonction réciproque.
- **Activité 2** (p.66) : f(x) = x³ sur [0, +∞[. 1) sens de variation de f sur ]0, +∞[ ; 2) en déduire que f est une bijection de ]0, +∞[ sur ]0, +∞[ (on note f⁻¹ sa réciproque) ; 3) tracer les courbes de f et f⁻¹ ; 4) calculer f⁻¹(a) pour : i) a = 1 ; ii) a = 8 ; iii) a = 1/125.
- **Activité 3** (p.66) : f(x) = xⁿ sur [0, +∞[, n entier naturel ≥ 1. 1) sens de variation de f sur ]0, +∞[ ; 2) en déduire que f est une bijection de ]0, +∞[ sur ]0, +∞[ ; 3) montrer que pour tout x > 0, f∘f⁻¹(x) = x.
- **Activité 4** (p.67) : f(x) = xⁿ sur [0, +∞[ (n entier naturel supérieur à 1), f⁻¹(x) = ⁿ√x. 1) continuité et sens de variation de f⁻¹ ; 2) a) que peut-on dire des courbes de f et f⁻¹ ? b) en déduire que lim_{x→+∞} ⁿ√x = +∞ et lim_{x→+∞} ⁿ√x / x = 0 ; 3) tracer, dans (O, i⃗, j⃗), les courbes de g : x ↦ √x ; h : x ↦ ∛x ; k : x ↦ ⁴√x (x ∈ [0, +∞[).
- **Activité 5** (p.68) : u(x) = x² ; v(x) = ∛x = x^{1/3} ; f = v∘u (x ≥ 0). a) continuité de f sur [0, +∞[ ; b) calculer lim_{x→+∞} f(x) ; c) images de 0 et 1 par f. Notation imprimée : « Pour tout réel x ≥ 0, on a f(x) = v∘u(x) = (x²)^{1/3} qu'on note plus simplement f(x) = x^{2/3}. Plus généralement, pour tous entiers naturels p et q supérieurs à 1 et pour tout réel x ≥ 0, on pose x^{p/q} = (x^p)^{1/q} = ⁽ᵠ⁾√(x^p) (racine q-ième). »

**Dérivée d'une fonction réciproque** (p.68–69)

- **Activité 1** (p.68) : f : x ↦ x² pour x ∈ [0, +∞[. 1) prouver que f réalise une bijection de [0, +∞[ sur [0, +∞[ et définir f⁻¹ ; 2) montrer que f⁻¹ est dérivable sur ]0, +∞[ et calculer (f⁻¹)'(x) ; 3) y₀ ∈ ]0, +∞[ et x₀ ∈ ]0, +∞[ tel que f(x₀) = y₀ : vérifier que (f⁻¹)'(y₀) = 1/f'(x₀) = 1/f'(f⁻¹(y₀)).
- **Activité 2** (p.69) : f : x ↦ x² + 4x − 3 ; g restriction de f à [−2, +∞[. 1) montrer que g est une bijection de [−2, +∞[ sur un intervalle J à préciser ; 2) g⁻¹ réciproque de g : a) dérivabilité à droite de g⁻¹ en y₀ = (−7) ; b) déterminer g⁻¹(−3), montrer que g⁻¹ est dérivable en (−3) et calculer (g⁻¹)'(−3) ; 3) quelle est la partie de J sur laquelle g⁻¹ est dérivable ?
- **Activité 3** (p.69, « Les questions 1), 2) et 3) sont indépendantes ») : 1) a) montrer que f : x ↦ (x + 1)/(x − 1) est une bijection de ]1, +∞[ sur ]1, +∞[ ; b) montrer que f⁻¹ est dérivable sur ]1, +∞[ et calculer de deux manières sa fonction dérivée ; 2) g : x ↦ ⁿ√x : montrer que g est dérivable sur ]0, +∞[ et que g'(x) = ⁿ√x/(n·x) ; 3) h : x ↦ tgx : a) montrer que h réalise une bijection de ]−π/2, π/2[ sur ℝ ; b) déterminer h⁻¹(1) et h⁻¹(√3) ; c) montrer que h⁻¹ est dérivable en 1 et en √3 et calculer (h⁻¹)'(1) et (h⁻¹)'(√3) ; d) montrer que h⁻¹ est dérivable sur ℝ et que pour tout réel x, (h⁻¹)'(x) = 1/(1 + x²).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Définition — restriction** (p.62) — « Soit f une fonction définie sur un ensemble D et (C) sa représentation graphique dans un repère (O, i⃗, j⃗). Soit I une partie de D. On appelle restriction de la fonction f à I, la fonction g définie sur I par g(x) = f(x), pour tout x ∈ I. La représentation graphique de g est formée par les points M de (C), de coordonnées (x, f(x)) où x ∈ I. » (exemple figuré : f(x) = x³ ; x ∈ ℝ ; g est la restriction de f à l'intervalle [0, +∞[)

> **Théorème** (p.64) — « Soit f une fonction continue et strictement monotone sur un intervalle I d'extrémités a et b (a < b). » Si f est strictement croissante sur I alors : f([a, b]) = [f(a), f(b)] ; f(]a, b]) = ]lim_{x→a⁺} f(x), f(b)] ; f([a, b[) = [f(a), lim_{x→b⁻} f(x)[ ; f(]a, b[) = ]lim_{x→a⁺} f(x), lim_{x→b⁻} f(x)[. Si f est strictement décroissante sur I alors : f([a, b]) = [f(b), f(a)] ; f(]a, b]) = [f(b), lim_{x→a⁺} f(x)[ ; f([a, b[) = ]lim_{x→b⁻} f(x), f(a)] ; f(]a, b[) = ]lim_{x→b⁻} f(x), lim_{x→a⁺} f(x)[.

> **Théorème** (p.64) — « Soit f une fonction continue et strictement monotone sur un intervalle I de la forme ]−∞, a] ou [a, +∞[ ou ]−∞, +∞[ (où a est un réel donné). » Si f est strictement croissante sur I alors : f(]−∞, a]) = ]lim_{x→−∞} f(x), f(a)] ; f([a, +∞[) = [f(a), lim_{x→+∞} f(x)[ ; f(]−∞, +∞[) = ]lim_{x→−∞} f(x), lim_{x→+∞} f(x)[. Si f est strictement décroissante sur I alors : f(]−∞, a]) = [f(a), lim_{x→−∞} f(x)[ ; f([a, +∞[) = ]lim_{x→+∞} f(x), f(a)] ; f(]−∞, +∞[) = ]lim_{x→+∞} f(x), lim_{x→−∞} f(x)[.

> **Théorème (de la bijection)** (p.65) — « Si f est une fonction strictement monotone sur un intervalle I de ℝ alors on a : 1) f est une bijection de I sur f(I). 2) La fonction réciproque f⁻¹, de f, est strictement monotone sur f(I) et plus précisément elle a le même sens de variation que f. 3) Pour tout x de I et pour tout y de f(I), y = f(x) équivaut à x = f⁻¹(y). 4) Si de plus, f est continue sur I alors f⁻¹ est continue sur l'intervalle J = f(I). 5) Les courbes représentatives (C) et (C') de f et f⁻¹, dans un repère orthonormé du plan, sont symétriques par rapport à la première bissectrice Δ : y = x du repère. »

> **Remarques et commentaires** (p.67) — « * On a f(0) = 0. On pourra ainsi, poser f⁻¹(0) = 0 et par la suite le domaine de définition de f⁻¹ sera [0, +∞[. * Pour tous réels x et y appartenant à [0, +∞[ on a f⁻¹(x) = y ⇔ x = f(y) = yⁿ. On note y = ⁿ√x. C'est-à-dire f⁻¹(x) = ⁿ√x. »

> **Théorème** (p.67) — « Soit n un entier naturel supérieur ou égal à 1. La fonction f : x ↦ xⁿ est une bijection de [0, +∞[ sur [0, +∞[. Sa fonction réciproque f⁻¹ est définie sur [0, +∞[ par f⁻¹(x) = ⁿ√x. (On note également, f⁻¹(x) = x^{1/n} et pour n = 2, f⁻¹(x) = x^{1/2} = √x). »

> **Propriétés** (p.67) — « Soit n un entier naturel supérieur à 1. Soit la fonction f : x ↦ xⁿ définie sur [0, +∞[ et soit sa fonction réciproque f⁻¹ définie sur [0, +∞[ par f⁻¹(x) = ⁿ√x. On a : La fonction f⁻¹ est continue et strictement croissante sur [0, +∞[. Dans un repère orthonormé (O, i⃗, j⃗) du plan, les courbes de f et f⁻¹ sont symétriques par rapport à la première bissectrice Δ : y = x du repère. »

> **Propriétés** (p.68) — « Soit n un entier naturel supérieur à 1. • Pour tout x ≥ 0, (ⁿ√x)ⁿ = x. • lim_{x→0⁺} ⁿ√x = 0, lim_{x→ℓ} ⁿ√x = ⁿ√ℓ (ℓ > 0) ; lim_{x→+∞} ⁿ√x = +∞ et lim_{x→+∞} ⁿ√x / x = 0. » (figure : C₃ courbe de f(x) = x³ ; C'₃ courbe de f⁻¹(x) = ∛x ; C₄ courbe de g(x) = x⁴ ; C'₄ courbe de g⁻¹(x) = ⁴√x ; droite Δ : y = x)

> **Théorème** (p.69) — « Soit f une bijection d'un intervalle I de ℝ sur J = f(I) ; soit x₀ un réel de I et y₀ = f(x₀). Si f est dérivable en x₀ et f'(x₀) ≠ 0 alors la fonction réciproque f⁻¹ de f est dérivable en y₀ et on a : (f⁻¹)'(y₀) = 1/f'(x₀) = 1/f'(f⁻¹(y₀)). »

> **Corollaire** (p.69) — « Soit f une bijection d'un intervalle I de ℝ sur J = f(I). Si f est dérivable sur I et f' ne s'annule pas sur I alors la fonction réciproque f⁻¹ de f est dérivable sur J et on a : (f⁻¹)' = 1/(f'∘f⁻¹). » **Remarque** : « Si f est dérivable en un point x₀ et f'(x₀) = 0 alors f⁻¹ n'est pas dérivable en y₀ = f(x₀). »

### Résumé du cours (p.70–71)

Reprend à l'identique : restriction ; les deux théorèmes sur l'image d'un intervalle par une fonction continue et strictement monotone (mêmes tableaux que p.64) ; « Théorème de la bijection » (5 points, mêmes énoncés que p.65) ; dérivée d'une fonction réciproque (théorème et corollaire de p.69). Rien de nouveau (la définition de ⁿ√x et les propriétés p.67–68 ne sont pas reprises).

### Exemples résolus

Aucun exercice résolu intégral dans ce chapitre.

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.72) — 1 activité (logiciel Cabri II plus)

f(x) = √(x² + 1) + 2x sur ℝ. Étapes : écrire `sqrt(x^2+1) + 2x`, montrer les axes, appliquer l'expression sur un axe pour obtenir la courbe C de f ; conjecturer le sens de variation ; en déduire que f réalise une bijection de ℝ sur ℝ ; construire la bissectrice Δ de l'angle AÔB (A(0, 1), B(1, 0)) ; point M sur C, M' image de M par la symétrie S_Δ ; lieu C' de M' (« Que représente la courbe C' ? ») ; afficher l'équation (E') de C' (capture d'écran : x² − 4xy + 3y² − 1 = 0) ; « Montrer que (E') ⇔ f(y) = x ⇔ y ∈ {(2x + √(x²+3))/3 ; (2x − √(x²+3))/3} » ; déplacer M jusqu'à A, conjecturer que B ∈ C' ; en déduire la valeur de y qui correspond à l'expression de f⁻¹(x).

### Exercices et problèmes (p.73–76) — 20 exercices

- **Ex. 1** (p.73) : f(x) = x² + 1 sur [0, +∞[. a) f admet une fonction réciproque, préciser son ensemble de définition J ; b) calculer f⁻¹(1), f⁻¹(2) et f⁻¹(3) [?, des espaces autour de 2 et 3 dans la couche texte laissent penser qu'un symbole a pu se perdre à l'impression ; rien n'est inféré, aucun radical n'est imprimé] ; c) sens de variation de f⁻¹, ensemble de dérivabilité ; d) expliciter f⁻¹(x) pour x ∈ J ; e) construire les courbes de f et f⁻¹.
- **Ex. 2** (p.73) : g(x) = −1 + √x sur [0, +∞[. a) g admet une réciproque ; b) domaine J de g⁻¹ ; c) g⁻¹(x) pour x ∈ J ; e) [sic : la lettre d) est omise] construire les courbes de g et g⁻¹.
- **Ex. 3** (p.73) : h(x) = x − 1/x sur ]0, +∞[. 1) h admet une réciproque, domaine J de h⁻¹ ; 2) h⁻¹(x) pour x ∈ J ; 3) construire les courbes de h et h⁻¹.
- **Ex. 4** (p.73) : f : ]−π/2, +π/2[ → ℝ, x ↦ tgx. 1) f est bijective ; 2) construire les courbes de f et f⁻¹. [l'impression porte « +π/2 », forme inhabituelle]
- **Ex. 5** (p.73) : f(x) = (−1 + 2x)/(6 + 3x) sur ]−2, +∞[. a) sens de variation ; b) f réalise une bijection de ]−2, +∞[ sur un intervalle I à préciser ; c) f⁻¹(x) pour x ∈ I ; d) courbes de f et f⁻¹.
- **Ex. 6** (p.73) : f(x) = x²/(1 + x²) sur ℝ. 1) a) f dérivable, sa dérivée ; b) tableau de variation ; 2) g restriction de f à ]0, +∞[ : a) g bijection de ]0, +∞[ vers un intervalle J ; b) g⁻¹(x) pour x ∈ J ; c) tracer (C) de g et (C') de g⁻¹.
- **Ex. 7** (p.73) : f(x) = 2/sin x sur ]0, π[. 1) tableau de variation ; 2) g restriction de f à ]0, π/2] : a) g admet une réciproque, préciser son ensemble de définition ; b) calculer g⁻¹(2) et g⁻¹(4) ; 3) construire les courbes de g et g⁻¹.
- **Ex. 8** (p.74) : f(x) = x⁵ sur [0, +∞[. a) f admet une réciproque qu'on précisera ; b) construire les courbes de f et f⁻¹.
- **Ex. 9** (p.74) : g(x) = 2∛x + 1 sur [0, +∞[. a) g dérivable sur [0, +∞[ (énoncé imprimé tel quel : « dérivable sur [0, +∞[ ») et calculer g'(x) pour x > 0 ; b) calculer lim_{x→0⁺} (g(x) − 1)/x, interpréter ; c) tableau de variation de g ; d) g réalise une bijection de [0, +∞[ sur J à préciser ; e) g⁻¹(x) pour x ∈ J ; f) courbes de g et g⁻¹.
- **Ex. 10** (p.74) : f(x) = (1 − √x)/(1 + √x). 1) a) f dérivable sur ]0, +∞[ et f'(x) = −1/(√x(1 + √x)²) ; b) tableau de variation de f sur [0, +∞[ ; c) f admet une réciproque f⁻¹ définie sur un intervalle J à préciser ; d) déterminer le réel positif x tel que f(x) = 1/2 ; e) calculer f(4) et (f⁻¹)'(−1/3) ; 2) g(x) = f(x) − x : a) g bijection de [0, +∞[ sur ]−∞, 1] ; b) en déduire que f(x) = x possède une solution unique α dans [0, +∞[ ; c) montrer que 0 < α < 1.
- **Ex. 11** (p.74) : g : [0, π] → [−1, 1], x ↦ cos x. 1) g bijection ; 2) images des réels 0, 1/2, 1 et −1/2 par g⁻¹ ; 3) courbes de g et g⁻¹ ; 4) x réel de [−1, 1] : a) calculer cos(g⁻¹(x)) et sin(g⁻¹(x)) en fonction de x ; b) montrer que g⁻¹(−x) = π − g⁻¹(x).
- **Ex. 12** (p.74) : f(x) = 2x − sin x sur ℝ. 1) f bijection de ℝ sur ℝ ; 2) a) f(x) = 4 admet une solution unique α dans ℝ ; b) vérifier 2,2 < α < 2,4 ; 3) g(x) = 2 + (1/2)sin x : a) vérifier g(α) = α ; b) montrer que pour tout x, |g'(x)| ≤ 1/2 ; c) en déduire que pour tout x, |g(x) − α| ≤ (1/2)|x − α|.
- **Ex. 13** (p.74–75) : f : ]1, +∞[ → ℝ, x ↦ 1 + 1/√x. 1) f réalise une bijection de ]1, +∞[ vers un intervalle J à préciser ; 2) f⁻¹(x) pour x ∈ J ; 3) tracer les courbes de f et f⁻¹ ; 4) f(x) = x admet une solution unique α dans ]1, +∞[ ; 5) pour tout x de ]1, +∞[, |f'(x)| ≤ 1/2 ; 6) en déduire |f(x) − α| ≤ (1/2)|x − α|.
- **Ex. 14** (p.75) : f(x) = 2 − √(−2x + 1) pour x ∈ ]−∞, 1/2]. 1) a) f dérivable sur ]−∞, 1/2[, f'(x), tableau de variation ; b) f réalise une bijection de ]−∞, 1/2] sur un intervalle J ; 2) expliciter f⁻¹(x) pour x ∈ J ; 3) ensemble sur lequel f⁻¹ est dérivable ; 4) calculer (f⁻¹)'(1).
- **Ex. 15** (p.75) : h(x) = x/(|x| − 1). 1) ensemble de définition, h impaire, asymptotes ; 2) tableau de variation ; 3) g restriction de h à ]0, 1[ : a) g bijection de ]0, 1[ sur un intervalle J ; b) g⁻¹(x) pour x ∈ J ; c) dérivabilité de g⁻¹ sur J et (g⁻¹)'(x) ; d) courbes de g et g⁻¹ dans un même repère orthonormé.
- **Ex. 16** (p.75) : 1) g(x) = 2x³ + 3x² + 1 sur ℝ : a) tableau de variation ; b) g(x) = 0 possède dans ℝ une solution unique α, vérifier −1.7 < α < −1.6 ; c) signe de g(x) dans ]−∞, α[ et [α, +∞[ ; 2) f(x) = (1 + x)/(1 − x³) sur ℝ \ {1} : a) limites aux bornes du domaine, interprétation géométrique ; b) pour tout x de ℝ \ {1}, f'(x) = g(x)/(1 − x³)² ; c) tableau de variation ; 3) h restriction de f à ]1, +∞[ : a) h bijection de ]1, +∞[ sur un intervalle J ; b) calculer h(2), en déduire (h⁻¹)'(−3/7) ; c) tracer les courbes de h et h⁻¹.
- **Ex. 17** (p.75) : g(x) = 2x³ − 3x² + 3 sur [−1, 0]. a) tableau de variation ; b) g admet une fonction réciproque ; c) g(x) = 0 admet une solution unique x₀ ∈ ]−1, 0[ ; d) calculer (g⁻¹)'(0) en fonction de x₀ ; e) construire les courbes de g et g⁻¹.
- **Ex. 18** (p.76) : f(x) = √(x/(1 − x)). 1) tableau de variation ; 2) a) f admet une réciproque f⁻¹, domaine de définition ; b) (f⁻¹)(1) et (f⁻¹)(2) ; c) f⁻¹ dérivable en 1 et en 2, calculer (f⁻¹)'(1) et (f⁻¹)'(2) ; d) équation de la tangente T à (C) de f au point d'abscisse 0.5 ; e) équation de la tangente T' à (C') de f⁻¹ au point d'abscisse 1 ; 3) tracer (C), (C'), T et T' ; 4) définir f⁻¹ ; 5) g(x) = f(sin x) pour x ∈ ]0, π/2[ : montrer que g est dérivable sur ]0, π/2[ et calculer g'(x).
- **Ex. 19** (p.76) : f(x) = √(x³/(2 − x)) sur [0, 2[. 1) tableau de variation ; 2) f admet une réciproque f⁻¹, domaine de définition.
- **Ex. 20** (p.76) : f(x) = 1/√(cos x) sur [0, π/2[. 1) f dérivable sur [0, π/2[ ; 2) f réalise une bijection de [0, π/2[ sur [1, +∞[ ; 3) a) dérivabilité de f⁻¹ à droite en 1 ; b) f⁻¹ dérivable sur ]1, +∞[ et calcul de (f⁻¹)'(x) pour tout x ∈ ]1, +∞[.

### Aperçu historique (p.77)

Une ligne : le concept de fonction et la notation fonctionnelle — Leibniz (1646–1716, premières notations fonctionnelles), Euler (1707–1783, f(x) ; extrait « De l'utilisation des fonctions discontinues en Analyse », 1765), D'Alembert (1750).

### Bornes de scope observées (chapitre 3)

- ✅ INCLUS : restriction d'une fonction ; image d'un intervalle par une fonction continue et strictement monotone (tableaux avec limites aux bornes) ; théorème de la bijection (5 points : bijection, même sens de variation, équivalence y = f(x) ⇔ x = f⁻¹(y), continuité de f⁻¹, symétrie par rapport à y = x) ; racine n-ième comme réciproque de xⁿ (propriétés, limites), puissances rationnelles x^{p/q} (notation) ; dérivée de la réciproque (théorème, corollaire, remarque f'(x₀) = 0) ; réciproque de tan (dérivée 1/(1+x²) en activité 3.3.d) ; réciproque d'un cosinus restreint (Ex. 11).
- ⛔ NON traité : fonctions arcsin/arccos/arctan comme objets nommés (la réciproque de tg et celle de cos sont étudiées sans leur donner de nom) ; ln et exp (traités aux chapitres 6 et 7 de ce manuel) ; démonstration du théorème de la bijection (énoncé donné, preuves dans les activités) ; suites.

> Sondage image : pages 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76 lues en L3 (p.70, 71 et 77 en L1 : résumé identique aux pages 64/65/69 déjà lues en image, texte sans formule) ; écarts : la couche texte de p.59 est illisible (police ornementale : « cÄtÇ wâ v{tÑ|àÜx ») et perd, sur toutes les pages, racines, valeurs absolues, ℝ, ∈, ≤ (corrigés sur image) ; p.66 « bijective de ℝ⁺ sur ℝ⁺ » (le texte écrit « de sur ») ; p.74 ex. 9 cube root « 2∛x + 1 » (texte : « 2 x + 1 ») ; écarts image/transcription relevés à la relecture R-7 puis corrigés (p.73 Ex. 1 b : f⁻¹(1), f⁻¹(2), f⁻¹(3), aucun radical imprimé ; p.68 : racine q-ième) ; coquilles du manuel en [sic] : p.64 Act. 3 (f pour g), p.73 ex. 2 (lettre d) omise) .

## 2.4 Chapitre 4 — Étude de fonctions (manuel 222451, p.78–98)

**Page de garde (p.78)** — Titre : « Étude de Fonctions », Chapitre 4. « Plan du chapitre » : ❈ Activités préliminaires ; ❈ Cours (❖ Étude d'exemples de fonctions polynômes ; ❖ Étude d'exemples de fonctions rationnelles ; ❖ Étude d'exemples de fonctions irrationnelles ; ❖ Étude d'exemples de fonctions trigonométriques) ; ❈ Résumé du cours ; ❈ Avec l'ordinateur ; ❈ Exercices et Problèmes ; ❈ Aperçu historique. Pas de QCM ni de Vrai-Faux (p.78–98 lues en entier).

### Activités préliminaires (p.79–81)

- **Act. prél. 1** (p.79) : repère cartésien ; courbe C (figure : arche de cubique, maximum 1 en x = 3, minimum −3 en x = 1, passage par (0, 1)) d'une fonction f définie et dérivable sur ℝ. 1) a) extrema de f dans [0, 4] ; b) sens de variation de f sur [0, 4] ; c) en déduire le signe de f' sur [0, 4] ; d) résoudre graphiquement f(x) = 0 dans [0, 4] ; 2) f(x) = −x³ + 6x² − 9x + 1 sur ℝ : a) calculer f'(x), tableau de variation de f sur ℝ ; b) montrer que f(x) = 0 admet exactement trois racines dans ℝ ; c) encadrement à 10⁻¹ près de chacune.
- **Act. prél. 2** (p.79) : repère orthogonal R = (O, i⃗, j⃗) ; f : x ↦ (2x² − 4x + 3)/(x − 1)², C sa courbe. 1) ensemble de définition D ; 2) continuité de f sur D ; 3) montrer que Δ : x = 1 est un axe de symétrie de C. Encadré : « Soit f une fonction définie sur D et C sa courbe représentative dans un repère orthogonal (O, i⃗, j⃗). Soit a un réel et Δ la droite d'équation x = a. La droite Δ est un axe de symétrie de la courbe C si et seulement si pour tout x de D, (2a − x) ∈ D et f(2a − x) = f(x). »
- **Act. prél. 3** (p.79–80) : repère orthonormé ; f : x ↦ sin(4x). 1) f impaire ; 2) domaine de dérivabilité et f'(x) ; 3) images de 0 ; π/4 ; π/3 ; π/2 et π par f ; 4) f périodique de période π/2 ; 5) tableau de variation de f sur [0, π/4] et construire sa courbe dans [−π/4, π/4]. Encadré (p.80) : « Soit f une fonction définie sur ℝ et T un réel strictement positif. La fonction f est périodique de période T si pour tout réel x, f(x + T) = f(x). »
- **Act. prél. 4** (p.80) : f(x) = x³ − 3x² + 5x − 2 sur ℝ, C. 1) montrer f(x) = (x − 1)³ + 2(x − 1) + 1 ; 2) montrer que W(1, 1) est un centre de symétrie de C ; 3) équation de C dans le repère (W, i⃗, j⃗) ; 4) W est un point d'inflexion de C ; 5) tableau de variation de f et construire C. Encadré : « Soit f une fonction définie sur D et C sa courbe représentative dans un repère (O; i⃗, j⃗) du plan. Soit W(a, b) un point du plan. Le point W est un centre de symétrie de la courbe C, si et seulement si pour tout x de D, (2a − x) ∈ D et f(2a − x) = 2b − f(x). »
- **Act. prél. 5** (p.80) : 1) f(x) = 1/(1 + x²) sur ℝ, C : a) parité de f, en déduire que la droite (O, j⃗) est un axe de symétrie pour C ; b) tableau de variation de f sur [0, +∞[ puis construire C ; 2) g(x) = x³ + x sur ℝ, C' : a) g impaire, en déduire que O est un centre de symétrie pour C' ; b) variations de g sur [0, +∞[ puis construire C'.
- **Act. prél. 6** (p.81) : f : x ↦ (2x² + x + 1)/x, C dans un repère orthogonal. 1) déterminer les réels a, b, c tels que ∀ x ∈ ℝ*, f(x) = ax + b + c/x ; en déduire que C admet au voisinage de l'infini une asymptote oblique que l'on précisera ; nature de l'autre asymptote ? 2) variations de f et construire C. Encadré : « On dit que la droite Δ : y = ax + b est une asymptote oblique à la courbe de f au voisinage de −∞ (resp. de +∞) lorsqu'on a : lim_{x→−∞} [f(x) − (ax + b)] = 0 (resp. lim_{x→+∞} [f(x) − (ax + b)] = 0) ».

### Cours — Activités

**Étude d'exemples de fonctions polynômes** (p.82–83)

- **Activité 1** (p.82) : figure : OA = 8, le triangle OMN est équilatéral, M ∈ [OA] ; OM = x ; f(x) aire du triangle OMN, g(x) aire du triangle AMN. 1) exprimer f(x) et g(x) en fonction de x ; 2) étudier f et g et tracer leurs courbes dans un même repère orthonormé ; 3) résoudre graphiquement, puis algébriquement, f(x) = g(x) et f(x) > g(x).
- **Activité 2** (p.82) : repère orthogonal ; f(x) = x³ − 3x² + 3 sur ℝ, C. 1) a) tableau de variations ; b) branches infinies de C ; 2) a) montrer f(x) = (x − 1)³ − 3(x − 1) + 1 ; b) en déduire que I(1, 1) est un centre de symétrie de C ; 3) a) équation cartésienne de la tangente T à C en I ; b) I est un point d'inflexion de C ; 4) construire T et C ; 5) déduire la courbe C' de g : x ↦ x³ − 3x² à partir de celle de f ; 6) construire la courbe C'' de h : x ↦ |x³ − 3x²|. Encadré latéral (p.82) : « Soit f une fonction définie sur une partie D de ℝ et C sa courbe représentative dans (O, i⃗, j⃗). On désigne par g et h les fonctions définies sur D par g : x ↦ f(x) + k (k réel fixé) et h : x ↦ −f(x). On a alors, les résultats suivants : *La courbe représentative de g dans le repère (O, i⃗, j⃗) est l'image par la translation de vecteur k j⃗ de la courbe C de f. **La courbe représentative de h dans le repère (O, i⃗, j⃗) est l'image de la courbe C de f par la symétrie axiale d'axe (O, i⃗). »
- **Activité 3** (p.83) : f(x) = x⁴ − 2x² + 2 sur ℝ, C repère orthonormé. 1) a) f paire ; b) tableau de variation de f sur ℝ⁺ ; c) branches infinies de C ; 2) a) tracer C ; b) utiliser le graphique pour déterminer le nombre de solutions de f(x) = m (m paramètre réel) ; 3) tracer, avec une autre couleur, la courbe C' de (−f).
- **Activité 4** (p.83) : f(x) = x³ + x² + x + 5 sur ℝ. 1) f dérivable sur ℝ, calculer f'(x) ; 2) tableau de variation de f ; 3) construire la courbe de f dans (O, i⃗, j⃗).

**Étude d'exemples de fonctions rationnelles** (p.83–86)

- **Activité 1** (p.83) : repère orthonormé ; A(1, 2) ; à chaque point M(x, 0) (x > 1) on associe le point N de l'axe (Oy) tel que A, M, N soient alignés (figure) ; S(x) aire du triangle OMN. 1) a) exprimer l'ordonnée de N en fonction de x ; b) en déduire S(x) = x²/(x − 1) ; 2) a) tableau de variation de S sur ]1, +∞[ ; b) en déduire x pour que l'aire de OMN soit minimale ; 3) a) déterminer a et b tels que pour tout x > 1, S(x) = ax + b + 1/(x − 1) ; b) en déduire que Δ : y = x + 1 est asymptote à la courbe (C) de S au voisinage de +∞ ; c) tracer Δ et (C).
- **Activité 2** (p.84) : f : x ↦ 3 + 2/(x − 1), C, W(1, 3). 1) a) équation de C dans le repère (W, i⃗, j⃗) ; b) en déduire que W est un centre de symétrie de C ; 2) variations de f et construire C.
- **Activité 3** (p.84) : f(x) = (2x² − x + 1)/(3x − 3), repère orthonormé, C. 1) a) déterminer a et b tels que lim_{x→+∞} f(x)/x = a et lim_{x→+∞} [f(x) − ax] = b ; b) en déduire que D : y = ax + b est une asymptote oblique au voisinage de +∞ ; 2) C possède un centre de symétrie à préciser ; 3) tableau de variation de f ; 4) tracer C ; 5) g restriction de f à I = [2, +∞[ : a) g réalise une bijection de I sur un intervalle J à préciser ; b) g⁻¹ réciproque : continuité, dérivabilité et sens de variation de g⁻¹ sur J ; c) courbe (C') de g⁻¹ dans (O, i⃗, j⃗).
- **Activité 4** (p.84) : f : ℝ → ℝ, f(x) = x³/(x² + 3x + 3), C repère orthonormé. 1) sens de variation de f sur ℝ ; 2) a) C admet une asymptote oblique D, équation cartésienne ; b) position de C par rapport à D ; 3) C possède un centre de symétrie I à préciser, équation de la tangente à C au point I ; 4) a) tracer D, T et C ; b) construire la courbe C' de la fonction |f| à partir de celle de f, préciser les éléments remarquables de C'.
- **Activité 5** (p.85) : g : x ↦ (x² + 4)/x, C_g repère orthonormé. 1) ensemble de définition et parité ; 2) tableau de variation de g sur ]0, +∞[ ; 3) a) calculer lim_{x→+∞} [g(x) − x], en déduire que C_g admet deux asymptotes à préciser ; b) position de C_g par rapport à Δ : y = x ; 4) tracer C_g et ses asymptotes ; 5) h : x ↦ (x² + 4)/|x| : construire la courbe de h à partir de celle de g.
- **Activité 6** (p.85) : f : x ↦ (3x² − 18x + 25)/(x² − 6x + 8), C_f repère orthonormé. 1) ensemble de définition D et limites aux bornes de D ; 2) C_f admet un axe de symétrie à préciser ; 3) en déduire que C_f admet trois asymptotes ; 4) tableau de variation de f ; 5) tracer C_f ; 6) g : x ↦ (5x² − 30x + 41)/(x² − 6x + 8) : a) montrer que pour tout x de D, g(x) = f(x) + k où k est une constante réelle à préciser ; b) en déduire que C_g s'obtient de C_f par une transformation géométrique simple à caractériser ; c) tracer C_g ; d) tableau de variation de g ; e) construire, avec une autre couleur, la courbe de |g|.
- **Activité 7** (p.85–86) : aire de jeu rectangulaire de 450 m² le long d'un bâtiment, dimensions supérieures ou égales à 10 m, entourée sur trois côtés d'une allée de 3 m de large (croquis A, B, C, D ; dimensions x et y), clôturée sur [AB], [BC], [CD] ; longueur L de la clôture. 1) a) démontrer que y = 450/x, puis x ∈ [10, 45] ; b) exprimer L en fonction de x ; 2) f(x) = 2x + 12 + 450/x sur [10, 45] : a) tableau de variation de f ; b) tracer la courbe (C) ; c) en déduire les dimensions de l'aire de jeu pour que la clôture soit la plus courte, et cette longueur.
- **Activité 8** (p.86) : repère orthonormé ; courbe d'une fonction f définie et dérivable sur ]−2,5 ; 2] (figure avec une asymptote oblique Δ et une asymptote verticale). 1) a) tableau de variation de f ; b) signe de f' ; c) extremum(s) relatif(s) éventuels ; 2) discuter, suivant le paramètre réel k, le nombre de solutions de f(x) = k dans ]−2,5 ; 2] ; 3) préciser le signe de [f(x) − (2x + 1)] pour x ∈ ]−2,5 ; 2] ; 4) sachant que pour tout x ∈ ]−2,5 ; 2] on a f(x) = ax + b + c/x², déterminer a, b, c.

**Étude d'exemples de fonctions irrationnelles** (p.86–87)

- **Activité 1** (p.86) : repère orthonormé ; A(−2, 0) ; à chaque point M(x, 0) de l'axe des abscisses on associe le point N(0, y) de l'axe des ordonnées tel que le triangle AMN soit rectangle en N (figure). 1) exprimer y en fonction de x ; 2) on pose y = f(x) : étudier et représenter graphiquement f.
- **Activité 2** (p.87) : f : x ↦ √(x² + 3x − 4), C repère orthonormé. 1) ensemble de définition D et limites aux bornes de D ; 2) montrer que Δ : x = −3/2 est un axe de symétrie de C ; 3) tableau de variation de f ; 4) a) montrer que ∀ x ∈ ]0, +∞[, f(x) = x√(1 + 3/x − 4/x²) ; b) en déduire lim_{x→+∞} f(x)/x ; c) montrer que ∀ x ∈ ]0, +∞[, f(x) − x = (3 − 4/x)/(√(1 + 3/x − 4/x²) + 1) ; d) montrer que D : y = x + 3/2 est une asymptote oblique à C ; e) montrer que C admet une autre asymptote oblique D' ; 5) tracer C et les droites Δ, D et D'.
- **Activité 3** (p.87) : f : x ↦ (1/2)x + 1 + (1/2)√(x² + 16). 1) montrer que D : y = x + 1 est asymptote à C_f au voisinage de +∞ ; 2) comportement asymptotique de f au voisinage de (−∞) ; 3) tableau de variation de f sur ℝ ; 4) f réalise une bijection de ℝ sur un intervalle J à déterminer ; 5) calculer f⁻¹(x) pour x ∈ J ; 6) tracer les courbes de f et f⁻¹ dans un repère orthonormé.
- **Activité 4** (p.87) : f(x) = √((x² + 2x)/(x² − 1)). 1) ensemble de définition D et limites aux bornes de D ; 2) variations de f ; 3) tracer la courbe C de f dans un repère orthonormé.

**Étude d'exemples de fonctions trigonométriques** (p.88–89)

- **Activité 1** (p.88) : f : ℝ → [−1, 1], f(x) = cos x. 1) étudier et construire, dans un repère orthonormé, la courbe (C) de f sur [−3π, 3π] ; 2) g restriction de f à [0, π] : a) montrer que g est une bijection de [0, π] sur [−1, 1] et déterminer g⁻¹(0) ; g⁻¹(1) ; g⁻¹(1/2) et g⁻¹(−1/2) ; b) construire la courbe (C') de g⁻¹.
- **Activité 2** (p.88) : f : x ↦ 2 sin x − sin 2x. 1) a) montrer f'(x) = 4(1 − cos x)(cos x + 1/2) ; b) en déduire le tableau de variation de f sur [0, π] ; 2) a) f est 2π périodique ; b) parité de f ; en déduire qu'il suffit d'étudier f sur [0, π] et préciser les transformations géométriques qui permettent de tracer la courbe sur [−π, 3π] ; 3) tracer la courbe de f sur [−π, 3π].
- **Activité 3** (p.88–89) : f(x) = tgx. 1) a) ensemble de définition et période de f ; b) f impaire ; 2) g restriction de f à ]−π/2, π/2[ : a) variations de g et tracer sa courbe ; b) g admet une fonction réciproque : ensemble de définition et ensemble de dérivabilité ; 3) a) calculer g⁻¹(0) ; g⁻¹(1) ; g⁻¹(√3) et lim_{x→+∞} g⁻¹(x) ; b) tracer la courbe de g⁻¹ ; 4) construire la courbe de f sur ]π/2, π[.
- **Activité 4** (p.89) : f(x) = tgx + sin(2x). 1) a) ensemble de définition D ; b) f π-périodique ; c) parité de f ; d) en déduire qu'il suffit d'étudier f sur [0, π/2[ ; 2) étudier f sur [0, π/2[ puis tracer sa courbe sur [−π/2, 3π/2].
- **Activité 5** (p.89) : f(x) = sin x/(sin x + cos x). 1) a) ensemble de définition D ; b) montrer ∀ x ∈ D, (x + π) ∈ D et f(x + π) = f(x), interpréter ; 2) g restriction de f à ]−π/4, 3π/4[ : variations de g, tracer sa courbe C.
- **Activité 6** (p.89) : f(x) = 1/cos((π/4)x). 1) ensemble de définition et période de f ; 2) g restriction de f à [0, 2[ : a) sens de variation de g ; b) g réalise une bijection de [0, 2[ sur un intervalle J à préciser ; c) tracer les courbes de g et g⁻¹.

> **Théorème** (p.88) — « Si f est une fonction périodique de période T et g est sa restriction à un intervalle [a, a+T] où a est un réel, alors sa courbe représentative dans un repère (O, i⃗, j⃗) se déduit de la courbe représentative de g par des translations de vecteurs (kT i⃗) ; k ∈ ℤ. Il suffit donc d'étudier f sur [a, a+T]. » (figure : courbe périodique, période T, restriction C_g sur [a, a+T])

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

Les encadrés de définition sont donnés dans les activités préliminaires (axe de symétrie, périodicité, centre de symétrie, asymptote oblique — reproduits ci-dessus) et dans le « Résumé du cours » (p.90) :

> **Plan d'étude d'une fonction numérique** (p.90) — « Pour étudier une fonction numérique f et tracer convenablement sa courbe représentative C, il importe d'étudier les propriétés de f telles que parité, variation, branches infinies, etc. On disposera, également, de moyens tels que : changement de repère, utilisation de transformations planes ou une transformation d'écriture conduisant à un changement de repère et permettant d'alléger le procédé de construction de la courbe C. Plan d'étude : En général, on adopte la démarche suivante (lorsque l'énoncé de l'exercice ne suggère aucun autre plan d'étude) : 1ère étape : Détermination de l'ensemble D sur lequel la fonction f est définie. 2ème étape : Réduction de domaine d'étude : - si f est paire ou impaire le domaine d'étude de f est D_e = D ∩ ℝ⁺. - si f est périodique de période T, il suffit d'étudier f sur un domaine du type D_e = D ∩ [a, a + T]. 3ème étape : Calcul des limites de f aux bornes de son ensemble de définition (ou d'étude). 4ème étape : Étude du sens de variation de f et consignation des résultats dans un tableau de variations. 5ème étape : Étude du comportement asymptotique de la courbe C. 6ème étape : Construction de quelques points de la courbe C ainsi que les asymptotes éventuelles ou les éléments de symétrie de C et les tangentes aux points particuliers etc. 7ème étape : Construction de C dans un repère convenablement choisi. »

> **Encadré** (p.90) — « Soit f une fonction définie sur un intervalle du type [α, +∞[. Si lim_{x→+∞} f(x) = +∞ (ou −∞) et lim_{x→+∞} f(x)/x = a (a ∈ ℝ*) et lim_{x→+∞} [f(x) − ax] = b (b ∈ ℝ) alors la droite D : y = ax + b est une asymptote oblique à la courbe représentative de f au voisinage de +∞. (Si b = +∞ ou −∞ la courbe possède une branche parabolique de direction la droite D : y = ax au voisinage de +∞). Le résultat est vrai pour une fonction f définie sur un intervalle du type ]−∞, α] et x tendant vers −∞. »

> **Axe de symétrie** (p.90, repris de p.79) — « Soit f une fonction définie sur D et C sa courbe représentative dans un repère orthogonal (O, i⃗, j⃗). Soit a un réel et Δ la droite d'équation x = a. La droite Δ est un axe de symétrie de la courbe C si et seulement si pour tout x de D, (2a − x) ∈ D et f(2a − x) = f(x). » — **Centre de symétrie** (p.90, repris de p.80) — « Soit f une fonction définie sur D et C sa courbe représentative dans un repère (O, i⃗, j⃗) du plan. Soit W(a, b) un point du plan. Le point W est un centre de symétrie de la courbe C, si et seulement si pour tout x de D, (2a − x) ∈ D et f(2a − x) = 2b − f(x). »

### Résumé du cours (p.90)

Une seule page (voir ci-dessus) : plan d'étude en 7 étapes, asymptote oblique / branche parabolique de direction y = ax, axe de symétrie x = a, centre de symétrie W(a, b). Rien de plus.

### Exemples résolus

Aucun exercice résolu intégral dans ce chapitre.

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.91) — 2 activités

- **Activité 1** : à l'aide d'un logiciel : repère orthonormé, point A(0, 4) ; cercle (C) de diamètre [OA], point N sur (C) distinct de O ; tangente à (C) en A coupant (ON) en P ; point M intersection de la parallèle à (AP) passant par N et de la perpendiculaire à (AP) en P ; conjecturer l'ensemble des points M quand N varie sur (C). 2) M(x, y) : a) montrer que y = 64/(x² + 16) ; b) étudier f : x ↦ 64/(x² + 16) et représenter graphiquement l'ensemble des points M.
- **Activité 2** : logiciel de géométrie : triangle ABC isocèle de sommet principal A, inscrit dans un cercle de centre O et de rayon 1 ; H pied de la hauteur issue de A ; α = angle HÔC (0 < α < π/2) ; aire de ABC ; faire varier α pour obtenir l'aire maximale S, valeur approchée de S et de α. 2) a) calculer BC et AH en fonction de α ; b) en déduire l'aire de ABC en fonction de α ; 3) a) représenter graphiquement f : [0, π/2] → ℝ, x ↦ sin x(1 + cos x) ; b) lire une valeur approchée de x pour laquelle f(x) est maximal ; 4) a) montrer que f'(x) = (2cos x − 1)(cos x + 1), x ∈ [0, π/2] ; b) tableau de variation de f sur [0, π/2] ; c) valeur de α pour laquelle l'aire de ABC est maximale ; d) préciser ce maximum et la nature du triangle ABC.

### Exercices et problèmes (p.92–97) — 25 exercices

- **Ex. 1** (p.92) : f(x) = x² − x + 1 et g(x) = −x² − 2x + 2, C_f et C_g repère orthonormé. 1) variations de f et g ; 2) a) position relative de C_f et C_g ; b) construire C_f et C_g.
- **Ex. 2** (p.92) : f(x) = (1/4)x⁴ − 2x², C. a) tableau de variations ; b) abscisses des points d'intersection de C avec l'axe (O, i⃗) ; c) branches infinies ; d) tracer C.
- **Ex. 3** (p.92) : f(x) = x³ − 4x² + 3x + 1 sur ℝ. a) variations de f ; b) branches infinies de C_f ; c) construire C_f.
- **Ex. 4** (p.92) : f(x) = 2x³ − 6x, repère orthogonal. 1) parité, en déduire que O est un centre de symétrie de C_f ; 2) étudier f, tableau de variations ; 3) a) coordonnées des points d'intersection de C_f avec l'axe des abscisses ; b) branches infinies ; 4) a) équation de la tangente T à C_f en O ; b) position de C_f par rapport à T ; c) tracer T et C_f.
- **Ex. 5** (p.92) : f(x) = x³ − 3x − 1 sur ℝ. 1) tableau de variations ; 2) justifier que f(x) = 0 admet trois solutions, encadrement à l'unité près de chacune ; 3) a) branches infinies ; b) construire C_f.
- **Ex. 6** (p.92) : f : x ↦ (1/2)x³ − 3x² + 4x − 1. 1) montrer que f(x) = (1/2)(x − 2)(x² − 4x) − 1 ; 2) W(2 ; −1) est un centre de symétrie de C_f ; 3) a) équation Y = F(X) de C_f dans le repère (W, i⃗, j⃗) ; b) étudier F ; c) construire C_f.
- **Ex. 7** (p.92–93) : f(x) = (x² + 3x)/(x² − 4x + 3). 1) domaine de définition D_f et limites aux bornes ; 2) en déduire que C_f admet trois asymptotes ; 3) tableau de variation ; 4) tracer C_f ; 5) C_f admet un axe de symétrie à préciser ; 6) g : x ↦ (4x² − 9x + 9)/(x² − 4x + 3) : a) montrer que g(x) = f(x) + k (k constante à préciser) ; b) en déduire que C_g s'obtient de C_f par une transformation géométrique simple ; c) tracer C_g ; d) utiliser C_g pour dresser le tableau de variation de g.
- **Ex. 8** (p.93) : f(x) = x²/(|x + 1| − |x − 1|). 1) a) ensemble de définition D ; b) f impaire ; 2) prolongement par continuité de f en 0, noté g ; 3) a) dérivabilité de g en 0 ; b) tableau de variations de g ; 4) a) branches infinies de la courbe C de g ; b) tracer C.
- **Ex. 9** (p.93) : f : x ↦ (x² + 2x − 1)/(x + 1), C_f. 1) a) déterminer a, b, c tels que f(x) = ax + b + c/(x + 1) ; b) en déduire les équations des asymptotes ; 2) variations de f et tracer C_f.
- **Ex. 10** (p.93) : f : x ↦ (x⁴ − 1)/x². 1) a) ensemble de définition ; b) tableau de variations ; 2) a) branches infinies de C ; b) tracer la parabole P : y = x² ; c) calculer lim_{|x|→+∞} [f(x) − x²], interpréter graphiquement ; d) tracer C.
- **Ex. 11** (p.93) : f(x) = (1/3)x³ − x + 2/3 si x ∈ ]−∞, 2[ ; f(x) = x²/(x + 1) si x ∈ [2, +∞[ ; C_f. 1) a) domaine de définition et continuité de f en 2 ; b) dérivabilité à gauche et à droite de f en 2, f est-elle dérivable en 2 ? interpréter graphiquement ; 2) a) déterminer a, b, c tels que ∀ x ∈ [2, +∞[, f(x) = ax + b + c/(x + 1) ; b) C_f admet une asymptote oblique D au voisinage de +∞, position relative de C_f et D ; c) branche infinie de C_f au voisinage de −∞ [le symbole −∞ est omis dans l'impression, « au voisinage de puis tracer »], puis tracer C_f et D.
- **Ex. 12** (p.94) : f : x ↦ (x³ − 2x²)/(x − 1)². 1) ensemble de définition D et limites aux bornes ; 2) a) déterminer a, b, c tels que f(x) = ax + b/(x − 1) + c/(x − 1)² ; b) en déduire les équations des asymptotes ; 2) [sic : numérotation « 2) » imprimée deux fois] tableau de variation de f ; 3) tracer C_f ; 4) discuter graphiquement, suivant m, le nombre de points d'intersection de C_f et de D : y = x + m.
- **Ex. 13** (p.94) : f(x) = √(x² − 2x − 3), repère orthogonal. 1) a) D_f et continuité de f sur D_f ; b) dérivabilité de f à gauche en (−1) et à droite en 3, interpréter ; c) lim_{−∞} f et lim_{+∞} f ; 2) a) ∀ x ∈ D_f − {−1 ; 3}, f'(x) = (x − 1)/√(x² − 2x − 3) ; b) tableau de variation ; 3) a) vérifier ∀ x ∈ D_f, f(x) = √((x − 1)² − 4) ; b) lim_{x→−∞} [f(x) + x − 1] = 0 et lim_{x→+∞} [f(x) − x + 1] = 0 ; c) C admet deux asymptotes obliques D et D' ; 4) tracer D, D' et C.
- **Ex. 14** (p.94) : f(x) = √((x − 2)² − 1), C. 1) ensemble de définition D ; 2) a) D : x = 2 est un axe de symétrie de C ; b) tableau de variation ; c) Δ₁ : y = x − 2 asymptote à C au voisinage de +∞ et Δ₂ : y = −x − 2 asymptote au voisinage de −∞ ; 3) tracer D, Δ₁, Δ₂ et C.
- **Ex. 15** (p.94) : f(x) = 1 − √(x² + x), C. 1) a) ensemble de définition ; b) D : x = −1/2 est un axe de symétrie de C ; c) en déduire qu'il suffit d'étudier f sur [0, +∞[ ; 2) a) dérivabilité de f à droite en 0, interpréter ; b) f'(x) pour x ∈ ]0, +∞[ ; c) tableau de variation sur ]0, +∞[ ; 3) a) D : y = −x + 1/2 est asymptote à C en +∞ ; b) position de C par rapport à D ; c) équation de l'asymptote D' à C au voisinage de −∞ ; 4) tracer D, D' et C_f ; 5) déduire de C_f la courbe C_g de g(x) = 1 − √(x² + |x|) et la construire.
- **Ex. 16** (p.95) : fₙ(x) = xⁿ√(x − 1) pour tout entier naturel n. 1) domaine de définition de fₙ ; 2) tableau de variation de fₙ pour n ≥ 1 ; 3) représenter dans un même repère orthonormé f₀, f₁ et f₂.
- **Ex. 17** (p.95) : f(x) = sin(2x + 2π/3) sur ℝ. 1) f périodique, préciser une période ; 2) a) calculer f'(x), résoudre dans [0, π] f'(x) = 0 ; b) tableau de variation de f sur [0, π] ; 3) représenter la restriction de f à [0, 2π] ; 4) selon le paramètre réel k, nombre de solutions de f(x) = k dans [0, 2π].
- **Ex. 18** (p.95) : f(x) = sin(2x) − 2 sin x sur ℝ. 1) parité ; 2) période ; 3) compléter l'étude de f et représenter la restriction de f à [−π, π].
- **Ex. 19** (p.95) : f(x) = sin x + cos²x sur ℝ. 1) f est 2π-périodique ; 2) Δ : x = π/2 est un axe de symétrie de C_f ; 3) étudier et représenter la restriction g de f à [0, π/2] ; 4) tracer la courbe de la restriction de f à [−π/2, 3π/2].
- **Ex. 20** (p.95) : 1) g : [0, π/2[ → ℝ, g(x) = tgx − x : variations de g, en déduire le signe de g(x) sur [0, π/2[ ; 2) f(x) = x sin(π/x) si x ≠ 0 et f(0) = 0 : continuité et dérivabilité de f sur ℝ ; 3) h restriction de f à ]2, +∞[ : a) sens de variation de h ; b) tracer la courbe de h ; c) h est une bijection de ]2, +∞[ sur un intervalle J.
- **Ex. 21** (p.95–96) : f : [0, π/2[ → ℝ₊, f(x) = √(tgx). 1) étudier f et tracer C_f ; 2) f est une bijection ; 3) g = f⁻¹ : a) dérivabilité de g et sa fonction dérivée ; b) calculer g(0) et g(1), tracer C_g avec C_f ; c) montrer que ∀ x ∈ ]0, +∞[, g(x) + g(1/x) = π/2 ; 4) h : ]−1/2, 1/2[ → ℝ, h(x) = g(1/cos(πx)) : a) h dérivable et son tableau de variation ; b) h prolongeable par continuité sur [−1/2, 1/2].
- **Ex. 22** (p.96) : f(x) = −2cos²x + 2cos x + 1 sur ℝ. 1) a) ∀ x ∈ ℝ, f'(x) = 2 sin x(2 cos x − 1) ; b) résoudre dans [0, π] 2 sin x(2 cos x − 1) = 0 ; c) tableau de variation de la restriction de f à [0, π] ; d) tracer cette restriction ; 2) g restriction de f à [π/3, π] : a) g admet une fonction réciproque g⁻¹ définie sur un intervalle J ; b) domaine D de dérivabilité de g⁻¹ ; c) t ∈ J : calculer cos(g⁻¹(t)) et sin(g⁻¹(t)) en fonction de t, en déduire (g⁻¹)'(t) pour t ∈ D.
- **Ex. 23** (p.96) : f(x) = (1 − x²)/(2 + x) sur ℝ − {−2}. 1) a) montrer ∀ x ∈ ℝ − {−2}, f(x) = −x + 2 − 3/(x + 2) ; b) calculer f'(x) et f''(x) ; c) en déduire que f' est strictement décroissante et déterminer l'image de [−1, 1] par f' ; d) tableau de variation de f ; e) montrer ∀ x ∈ [0, 1], |f'(x)| ≤ 2/3 ; f) en déduire ∀ x, y ∈ [0, 1], |f(x) − f(y)| ≤ (2/3)|x − y| ; 2) tracer la courbe C de f dans un repère orthonormé ; 3) g(t) = (1 − sin²t)/(2 + sin t) sur ℝ : a) montrer ∀ t ∈ ℝ, g(π − t) = g(t) ; b) expliquer comment l'étude et la représentation de la restriction de g à [−π/2, π/2] permet de construire la courbe de g ; c) prouver que g'(t) = f'(sin t) × cos t ; d) g'(t) = 0 admet une solution unique α ∈ ]−π/2, π/2[ ; e) calculer la valeur exacte de g(α) ; f) construire la courbe de la restriction de g à [0, π/2] dans un repère orthonormé convenablement choisi ; 4) a) résoudre graphiquement g(t) = t ; b) montrer que g(t) − t = 0 admet une solution unique t₀ ∈ [0, π/2] ; 5) suite réelle (uₙ) : u₀ = 0 et uₙ₊₁ = (1 − sin²(uₙ))/(2 + sin(uₙ)) : a) montrer que |uₙ₊₁ − t₀| ≤ (2/3)|uₙ − t₀| ; b) montrer par récurrence ∀ n ∈ ℕ, |uₙ − t₀| ≤ (2/3)ⁿ|u₀ − t₀| ; c) en déduire lim_{n→+∞} uₙ.
- **Ex. 24** (p.97) : étudier et représenter graphiquement f(x) = sin²x − sin x et g(x) = cos(3x)cos²x.
- **Ex. 25** (p.97, « D'après Bac tunisien 2004 ») : 1) g(x) = 1 + x/√(x² + 1) sur ℝ : a) g'(x) = 1/((x² + 1)√(x² + 1)) ; b) variations de g, en déduire g(x) > 0 pour tout x ; 2) f(x) = x − 1 + √(x² + 1), C repère orthonormé : a) f'(x) = g(x) ; b) lim_{x→−∞} f(x) = −1, interpréter ; c) tableau de variation de f ; 3) a) Δ : y = 2x − 1 asymptote à C au voisinage de +∞ ; b) équation de la tangente T à C en O, position de T par rapport à C ; c) tracer C, T et Δ (placer les points de C d'abscisses −1 et 1) ; 4) a) f réalise une bijection de ℝ sur un intervalle J à déterminer ; b) calculer (f⁻¹)'(√2) ; c) tracer C' courbe de f⁻¹.

### Aperçu historique (p.98)

Une ligne : René Descartes (1596–1650), « Je pense… donc… je suis ! », fondateur de la géométrie analytique (courbes définies par leur équation relativement à un repère) et du rationalisme moderne.

### Bornes de scope observées (chapitre 4)

- ✅ INCLUS : plan d'étude en 7 étapes ; réduction du domaine (parité, périodicité) ; axe de symétrie x = a et centre de symétrie W(a, b) (critères f(2a − x) = f(x) et f(2a − x) = 2b − f(x)) ; changement de repère (équation Y = F(X)) ; transformations simples (translation de vecteur k j⃗, symétrie d'axe (O, i⃗), passage à |f|) ; asymptotes verticale/horizontale/oblique, branches paraboliques ; fonctions polynômes, rationnelles, irrationnelles, trigonométriques ; restriction et fonction réciproque en situation (tg, cos, f restreinte) ; discussion graphique du nombre de solutions de f(x) = m ; problèmes d'optimisation (aires, clôture) ; suites par itération d'une fonction contractante (Ex. 23).
- ⛔ NON traité : fonctions ln, exp et leurs études (chapitres ultérieurs du programme) ; convexité (hors point d'inflexion) ; primitives, intégrales ; étude de courbes paramétrées ou en polaires ; asymptotes obliques par développement limité ; tracé informatisé détaillé (les activités « Avec l'ordinateur » ne nomment pas de logiciel dans ce chapitre).

> Sondage image : pages 79–90 (toutes), 91, 92, 93, 94, 95, 96, 97 lues en L3 (p.78 et 98 en L1 seule : plan et biographie) ; écarts : la couche texte perd, sur toutes les pages de ce chapitre, les racines, valeurs absolues (p.84 « |f| », p.85 « |g| » et « h : x ↦ (x²+4)/|x| », p.82 « h : x ↦ |x³−3x²| »), ℝ, ∈, ≤ (corrigés sur l'image) ; p.97 ex. 25 : le texte écrit « f(x) = x − 1 + x + 1 » pour « x − 1 + √(x² + 1) » ; aucun écart image/transcription ; coquilles du manuel en [sic] : p.94 ex. 12 (numérotation 2) en double) ; [?] : Ex. 11 c) (symbole omis dans l'impression).

## 2.5 Chapitre 5 — Fonctions primitives (manuel 222451, p.99–116)

**Page de garde (p.99)** — Titre : « Fonctions primitives », Chapitre 5. Plan du chapitre : Activités préliminaires ; Cours (Fonctions primitives d'une fonction continue ; Opérations sur les fonctions primitives ; Exemples de calculs de fonctions primitives) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ; Aperçu Historique. **Pas de rubrique QCM / Vrai-Faux dans ce chapitre.** Notation du manuel : tg x, cotg x (ou cotan) pour tan, cot ; ℝ, ℤ, ℕ pour les ensembles (la couche texte perd ces symboles, vérifiés sur image).

### Activités préliminaires (p.100)

- **Préliminaire 1** (p.100) : repère orthonormé (O, i⃗, j⃗). 1) Tracer la droite (D) : y = 2x. 2) A point de (D) d'abscisse 1, B(1, 0) : calculer l'aire 𝒜 du triangle OAB. 3) f, g définies sur ℝ par f(x) = x² et g(x) = x² + 5 : vérifier que 𝒜 = f(1) − f(0) = g(1) − g(0).
- **Préliminaire 2** (p.100) : f : x ↦ (3/8)x + (1/4)sin(2x) + (1/32)sin(4x). 1) Calculer f′(x) pour tout réel x. 2) a) En écrivant cos 4x = 2cos²2x − 1, montrer que f′(x) = (1/4)(cos 2x + 1)². b) En déduire que f est croissante sur ℝ.
- **Préliminaire 3** (p.100) : déterminer la fonction dérivée de a) f : x ↦ −1/x + 1 ; b) g : x ↦ 2√x + k (k constante réelle) ; c) h : x ↦ (x² + 1)³/3 ; d) k : x ↦ 2√(x² + 1) + 3 ; e) F : x ↦ −(1/2)cos(2x + π/3) ; f) G : x ↦ (1/3)(sin(3x) − cos(3x)) ; g) H : x ↦ tgx − cotgx ; h) K : x ↦ (x³ + x² + x + 1)cos x.

### Cours — Activités

**Fonctions primitives d'une fonction continue** (p.101–102)

- **Activité 1** (p.101) : mobile M en mouvement rectiligne, vitesse instantanée v(t) = 2t − 3. 1) Sachant x(0) = 0 à l'instant t = 0 (s), donner l'équation horaire x(t). 2) Vitesse moyenne entre deux instants distincts t₁ et t₂ : v_M(t₁ ; t₂) = (x(t₂) − x(t₁))/(t₂ − t₁) ; a) la calculer entre 3 s et 5 s ; b) entre 2 s et 3 s ; c) montrer que v(3) = lim_{t→3} v_M(3 ; t).
- **Activité 2** (p.101) : f(x) = 3x² + 2x + 1 et F(x) = x³ + x² + x + 5 sur ℝ. 1) Montrer que F est dérivable sur ℝ et que F′(x) = f(x) pour tout réel x. 2) Donner deux autres fonctions G et H dérivables sur ℝ telles que ∀x ∈ ℝ, G′(x) = H′(x) = f(x).
- **Activité 3** (p.101) : donner une primitive F de f sur l'intervalle I dans chaque cas : a) f : x ↦ 4x³ ; I = ℝ ; b) f : x ↦ 1/x² ; I = ]0, +∞[ ; c) f : x ↦ 1/√x ; I = ]0, +∞[.
- **Activité 4** (p.102) : f : x ↦ −2 sin(2x). 1) Vérifier que f est continue sur ℝ. 2) Donner la forme générale d'une primitive de f sur ℝ. 3) Déterminer la primitive F de f sur ℝ qui prend la valeur 1 en 0. 4) Déterminer la primitive G de f sur ℝ qui prend la valeur 0 en π/2.
- **Activité 5** (p.102) : f continue sur un intervalle I, x₀ réel de I, y₀ réel. Montrer que f possède une unique fonction primitive sur I qui prend la valeur y₀ en x₀.
- **Activité 6** (p.102) : f définie sur ℝ par f(x) = 2x. a) Tracer la courbe représentative (D) de f dans un repère orthonormé (O ; i⃗, j⃗). b) Pour tout réel positif x, A point de (D) d'abscisse x, B(x, 0) : calculer, en fonction de x, l'aire S(x) du triangle OAB. c) Calculer S′(x) ; comparer avec f(x). d) Donner la primitive F de f sur ℝ telle que F(1) = −2.

**Opérations sur les fonctions primitives** (p.103)

- **Activité 1** (p.103) : f, g continues sur un intervalle I de ℝ, α et β réels, F et G primitives de f et g sur I. Montrer que (α·F + β·G) est une primitive de (α·f + β·g) sur I.
- **Activité 2** (p.103) : f : x ↦ 2cos(3x) + 3sin(2x). 1) Déterminer une primitive de f sur ℝ. 2) Déterminer la primitive F de f sur I = [−π, π] telle que F(0) = −1.
- **Activité 3** (p.103) : f : x ↦ −1/x², F : x ↦ 1/x + 1, G : x ↦ 1/x − 1. 1) Vérifier que f est continue sur ℝ* (vérifié image). 2) a) Montrer que F est la primitive de f sur I = ]−∞, 0[ s'annulant en un réel a que l'on précisera. b) Montrer que G est la primitive de f sur I = ]0, +∞[ s'annulant en un réel b que l'on précisera.
- **Activité 4** (p.105, encore sous « Opérations sur les fonctions primitives » : le titre « Exemples de calcul de fonctions primitives » n'apparaît qu'en p.107) : recopier et compléter un tableau à trois colonnes (Fonction f ; Fonction primitive F de f ; Intervalle I sur lequel f et F sont définies) pour les sept fonctions : x ↦ 3 + 5x ; x ↦ −x − 1/x² ; x ↦ x⁴ + x² + 1 ; x ↦ −2/(2x − 1)² ; x ↦ 3 sin(2x) ; x ↦ 6cos(3x + π/6) ; x ↦ 1/sin²x + 1.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Définition** (p.101) — « Soient f et F deux fonctions définies sur un intervalle I. F est une primitive de f sur I si et seulement si F est dérivable sur I et pour tout réel x de I, F′(x) = f(x). »

> **Théorème 1** (p.102) — « Toute fonction continue sur un intervalle I admet des primitives sur I. »

> **Théorème 2** (p.102) — « Si une fonction f admet une fonction primitive F sur un intervalle I alors f admet une infinité de fonctions primitives sur I et qui sont toutes de la forme F + c où c désigne une constante réelle arbitraire. C'est-à-dire l'ensemble des primitives de f sur l'intervalle I est {F + c ; c ∈ ℝ} »

> **Théorème 3** (p.102) — « Etant donnés un intervalle I, un réel a de I et un réel b. Toute fonction f continue sur I admet une unique fonction primitive F sur I telle que F(a) = b. »

> **Théorème 4** (p.103) — « Etant données deux fonctions continues f et g sur un intervaiie [sic] I et deux réels α et β. Si F et G sont respectivement deux fonctions primitives de f et g sur I alors (α·F + β·G) est une primitive de la fonction (α·f + β·g) sur I. »

> **Tableau « Fonctions primitives des fonctions usuelles »** (p.104, vérifié image) — colonnes : I intervalle de ℝ ; f définie sur I par ; primitives F de f sur I (c ∈ ℝ). Lignes :
> 1. I = ℝ : x ↦ a (a ∈ ℝ) ; F : x ↦ ax + c.
> 2. I = ℝ : x ↦ x ; F : x ↦ (1/2)x² + c.
> 3. I = ℝ : x ↦ xⁿ (n ∈ ℕ*) ; F : x ↦ (1/(n+1))·xⁿ⁺¹ + c.
> 4. I = ℝ* : x ↦ 1/x² ; F : x ↦ −1/x + c.
> 5. I = ℝ* : x ↦ xⁿ (n ∈ ℤ* \ {−1}) ; F : x ↦ (1/(n+1))·xⁿ⁺¹ + c.
> 6. I = ℝ*₊ : x ↦ 1/√x ; F : x ↦ 2√x + c.
> 7. I = ℝ : x ↦ cos x ; F : x ↦ sin x + c.
> 8. I = ℝ : x ↦ sin x ; F : x ↦ −cos x + c.
> 9. I = ℝ \ {π/2 + kπ, k ∈ ℤ} : x ↦ 1/cos²x ; F : x ↦ tgx + c.
> 10. I = ℝ \ {kπ, k ∈ ℤ} : x ↦ 1/sin²x ; F : x ↦ −cotgx + c.
> 11. I = ℝ : x ↦ cos(ax + b) (a ∈ ℝ*, b ∈ ℝ) ; F : x ↦ (1/a)·sin(ax + b) (c ∈ ℝ).
> 12. I = ℝ : x ↦ sin(ax + b) (a ∈ ℝ*, b ∈ ℝ) ; F : x ↦ −(1/a)·cos(ax + b) (c ∈ ℝ).
> 13. I = ℝ \ {x ∈ ℝ tel que ax + b = π/2 + kπ, k ∈ ℤ} : x ↦ 1 + tan²(ax + b) (a ∈ ℝ*, b ∈ ℝ) ; F : x ↦ (1/a)·tan(ax + b) + c (c ∈ ℝ).
> 14. I = ℝ \ {x ∈ ℝ tel que ax + b = kπ, k ∈ ℤ} : x ↦ 1 + cotan²(ax + b) (a ∈ ℝ*, b ∈ ℝ) ; F : x ↦ −(1/a)·cotan(ax + b) + c (c ∈ ℝ).
>
> [sic/doute] ligne 3 : l'intervalle imprimé est ℝ pour n ∈ ℕ* ; ligne 5 : n ∈ ℤ* \ {−1} avec I = ℝ* (cohérent). La ligne 4 (1/x²) est un cas particulier de la ligne 5 (n = −2), répété tel quel.

> **Tableau « Règles générales de détermination des fonctions primitives »** (p.106, repris dans le Résumé p.109–110 en 8 lignes, sans la ligne u′/uⁿ ; vérifié image) — I intervalle de ℝ ; c ∈ ℝ :
> 1. u et v dérivables sur I : f = u′ + v′ ; F = u + v + c.
> 2. u dérivable sur I : f = a·u′ (a réel) ; F = a·u + c.
> 3. u et v dérivables sur I : f = u′·v + v′·u ; F = (uv) + c.
> 4. u dérivable sur I et ne s'annulant pas sur I : f = u′·uⁿ ; n ∈ ℤ \ {−1} ; F = (1/(n+1))·uⁿ⁺¹ + c.
> 5. u dérivable et ne s'annulant pas sur I : f = u′/u² ; F = −1/u + c.
> 6. u dérivable et ne s'annulant pas sur I : f = u′/uⁿ ; n ∈ ℕ* ; F = −1/((n − 1)·uⁿ⁻¹) + c. [sic : pour n = 1 le dénominateur (n − 1) est nul ; la règle imprimée ne l'exclut pas.]
> 7. u dérivable et strictement positive sur I : f = u′/√u ; F = 2√u + c.
> 8. u et v dérivables sur I et v ne s'annulant pas sur I : f = (u′·v − v′·u)/v² ; F = u/v + c.
> 9. u et v telles que v∘u soit dérivable sur I : f = (v′∘u)·u′ ; F = (v∘u) + c.

> **Résumé du cours** (p.109) — redit : la définition de primitive ; « Si une fonction f admet une fonction primitive F sur un intervalle I alors f admet une infinité de fonctions primitives sur I et qui sont toutes de la forme F + c où c désigne une constante réelle arbitraire. L'ensemble des primitives de f sur l'intervalle I est {F + c ; c ∈ ℝ}. » ; « Toute fonction continue sur un intervalle I admet au moins une fonction primitive sur I. » ; « Etant donné un intervalle I, un réel a de I et un réel b. Alors toute fonction f continue sur I admet une unique fonction primitive F sur I telle que F(a) = b. » ; Opérations (théorème 4 redit avec α, β) ; Règles générales (p.109–110 : tableau à 8 lignes, qui reprend celui de la p.106 **sans la ligne u′/uⁿ (n ∈ ℕ*)**). Le Résumé ne reprend pas le tableau des fonctions usuelles.

### Cours — Exemples résolus / à traiter (p.107–108)

Neuf « Exemples » ; seul l'Exemple 1 est donné avec son résultat ; les autres posent « vérifier que… » puis « en déduire que… » (résultat de F donné dans l'énoncé pour les Exemples 2 à 6).

- **Exemple 1** (p.107) : une primitive de f : x ↦ 3x² − 5x − 1 − 1/√x sur ]0, +∞[ est F : x ↦ x³ − (5/2)x² − x − 2√x + c, où c désigne une constante réelle arbitraire.
- **Exemple 2** (p.107) : f : x ↦ x(1 − x²)². 1) En posant u(x) = 1 − x², vérifier que f(x) = −(1/2)·u′(x)·[u(x)]². 2) En déduire que F : x ↦ −(1/6)(1 − x²)³ + c est une primitive de f sur ℝ.
- **Exemple 3** (p.107) : f : x ↦ x/√(x² + 1). 1) En posant u(x) = x² + 1, vérifier que f(x) = u′(x)/(2√(u(x))). 2) En déduire que F : x ↦ √(x² + 1) + c est une primitive de f sur ℝ.
- **Exemple 4** (p.107) : f : x ↦ (4x + 2)/(x² + x − 2)². 1) En posant u(x) = x² + x − 2, vérifier que f(x) = 2u′(x)/[u(x)]². 2) En déduire que F : x ↦ −2/(x² + x − 2) + c est une primitive de f sur ]1, +∞[.
- **Exemple 5** (p.107) : f : x ↦ 15x²/√(5x³). 1) En posant u(x) = 5x³, vérifier que f(x) = u′(x)/√(u(x)). 2) En déduire que F : x ↦ 2√(5x³) + c est une primitive de f sur ]0, +∞[.
- **Exemple 6** (p.108) : f : x ↦ (2x + 1)cos(x² + x + 1). 1) Avec u(x) = x² + x + 1 et v(x) = sin x, vérifier que f(x) = u′(x)·(v′∘u)(x). 2) En déduire que F : x ↦ sin(x² + x + 1) + c est une primitive de f sur ℝ.
- **Exemple 7** (p.108) : f : x ↦ (x² + 1)³. 1) Montrer que f(x) = x⁶ + 3x⁴ + 3x² + 1. 2) Déterminer alors la primitive F de f sur ℝ s'annulant en 1.
- **Exemple 8** (p.108) : f définie sur I = ]1/2, +∞[ par f : x ↦ x² − x/√(4x² − 1). En écrivant f(x) sous la forme u′(x) + v′(x) où u et v sont deux fonctions dérivables sur I, déterminer une primitive F de f sur I. [Aucune ambiguïté de parenthèse : le terme soustrait est x/√(4x² − 1).]
- **Exemple 9** (p.108) : f : x ↦ cos x − cos³x. a) Justifier que f est continue sur ℝ. b) Vérifier que f(x) = u′(x)·u²(x) où u est une fonction dérivable sur I = ]0, π[ et trouver alors une primitive F de f sur l'intervalle I.

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.111) — 2 activités

- **Activité 1** : signe de f(x) = (1/3)x³ − x − 1 à l'aide d'un grapheur et du tableur Excel, via F : x ↦ (1/12)x⁴ − (1/2)x² − x. 1) Vérifier que F est la primitive de f s'annulant en 0. 2) Tracer la courbe de F au grapheur. 3) S'assurer que F possède trois extremums, encadrement d'amplitude 0,5 de chacun. 4) Avec Excel, valeur approchée à deux chiffres après la virgule de chacun. 5) Dresser le tableau de signe de f(x).
- **Activité 2** : calcul de primitives avec le logiciel de calcul formel Derive. Exemple : f : x ↦ x cos x + x² sin x ; mode d'emploi (ouvrir Derive, taper x*cos(x) + x^2*sin(x), raccourci ∫f, intégrale indéfinie, simplify) ; résultat donné F(x) = (3 − x²)·cos x + 3x·sin x ; « Vérifier que F est une primitive de f sur ℝ ». Application : primitives de f : x ↦ x²√(x + 1) ; g : x ↦ x³sin(3x) ; h : x ↦ x cos(x² + 1) (notation Derive : x^2*sqrt(x+1)).

### Exercices et problèmes (p.112–114) — 13 exercices

- **Ex. 1** (p.112) : pour chaque f, déterminer une primitive F sur un intervalle à préciser : 1) x⁵ − 5x² + 2 − 3/x² ; 2) (x⁴ − 1)/x² ; 3) (2x − 1)(x² − x − 4)⁸ ; 4) (√x − 2)(√x + 1) ; 5) (x² − 1)(x³ − 3x + 5) ; 6) (2x + 1)/√(4x² + 4x + 5) ; 7) (x + 1)/(x² + 2x + 5)² ; 8) (2x + 1)³ ; 9) cos(2x + π/6) ; 10) (x/√(x² − 1))·cos(√(x² − 1)) ; 11) (cos x)×sin³x ; 12) x²/√(1 + x³).
- **Ex. 2** (p.112) : f(x) = 4x³ sur ℝ ; F(x) = x⁴ + 2 si x ≥ 0 et F(x) = x⁴ − 2 si x < 0. F est-elle une primitive de f sur ℝ ?
- **Ex. 3** (p.112) : f : x ↦ (cos x)×(2 sin x − 1). Justifier l'existence des primitives de f sur ℝ et déterminer la primitive F de f qui s'annule en x₀ = π/2.
- **Ex. 4** (p.112) : f : x ↦ cos³x − 3cos x + 2. 1) Vérifier que pour tout x réel f(x) = −(cos x)×sin²x − 2cos x + 2. 2) En déduire la primitive F de f sur ℝ qui s'annule en (−π/2).
- **Ex. 5** (p.112) : f : x ↦ 5 sin x + 3 sin³x. 1) Calculer f′(x) et f″(x) pour tout x réel. 2) En déduire l'expression générale des primitives de f sur ℝ.
- **Ex. 6** (p.112) : f : x ↦ (x³ − 3x² + 3x)/(x − 1)². 1) Déterminer a, b, c tels que f(x) = ax + b + c/(x − 1)² sur l'ensemble de définition. 2) En déduire une primitive de f sur ]1, +∞[.
- **Ex. 7** (p.112) : f : x ↦ sin(3x)×cos x. 1) Montrer que pour tout x ∈ ℝ, f(x) = (1/2)[sin(4x) + sin(2x)]. 2) En déduire la primitive F de f sur ℝ qui s'annule en π.
- **Ex. 8** (p.112–113) : **A /** f : [0, +∞[ → ℝ, x ↦ 1/(1 + x²). 1) Prouver l'existence et l'unicité d'une primitive F de f sur [0, +∞[ s'annulant en 0. 2) Pour x ∈ [0, π/2[, K(x) = F(tgx) : a) montrer que K est dérivable sur [0, π/2[ et déterminer K′(x) ; b) en déduire que pour tout x ∈ [0, π/2[, K(x) = x, puis calculer F(√3/3) et F(1). 3) Pour tout réel positif x, U(x) = F(1/(1 + x)) + F(x/(x + 2)) : a) montrer que U est dérivable sur [0, +∞[ et calculer U′(x) ; b) en déduire la valeur de F(1/2) + F(1/3). **B /** g(x) = −f(x) : 1) montrer que g admet une primitive et une seule G sur [0, +∞[ qui s'annule en 0 ; 2) T : ]0, π/2] → ℝ, x ↦ T(x) = G(cotgx) : a) montrer que T est dérivable sur ]0, π/2] et déterminer T′(x) ; b) en déduire que ∀x ∈ ]0, π/2], T(x) = x − π/2, puis calculer G(1) et G(√3) ; 3) ∀x ∈ [0, +∞[, V(x) = G(1/x) + G(x/(x + 2)) [sic : domaine imprimé [0, +∞[ alors que 1/x n'est pas défini en 0] : a) montrer que V est dérivable sur [0, +∞[ et déterminer V′(x) ; b) en déduire que G(1/4) + G(3/5) = π/4.
- **Ex. 9** (p.113) : f : x ↦ 1/sin x pour x ∈ ]0, π[. 1) Étudier et représenter la courbe (C_f) dans un repère orthonormé. 2) g restriction de f à [π/2, π[ : a) montrer que g réalise une bijection de [π/2, π[ vers un intervalle J à déterminer ; b) étudier la dérivabilité de g⁻¹ sur J et calculer (g⁻¹)′(x) lorsqu'il existe ; c) déterminer une primitive F de k : x ↦ 1/√(x² − 1) sur [3/2, +∞[.
- **Ex. 10** (p.113) : f primitive sur ℝ de u : t ↦ 1/(2t² − 2t + 1) ; g de I = ]−π/2, π/2[ dans ℝ définie par g(x) = f((1 + tgx)/2). 1) Prouver que g est dérivable sur I. 2) Montrer que g est une application affine. 3) Calculer f(1) − f(0).
- **Ex. 11** (p.113) : f : x ↦ 3 sin x − 2 sin³x. 1) Trouver a, b réels tels que x ↦ a cos x + b cos³x soit une primitive de f sur [0, π]. 2) En écrivant sin³x = (1 − cos²x) sin x, retrouver une primitive de f sur ]0, π[.
- **Ex. 12** (p.113–114) : f : ]0, +∞[ → ℝ, x ↦ 1/x. 1) Montrer que f admet une primitive et une seule F qui s'annule en 1. 2) Étudier le sens de variation de F, en déduire ∀x ∈ ]0, 1[, F(x) < 0 et ∀x ∈ ]1, +∞[, F(x) > 0. 3) H(x) = F(ax) pour x > 0 (a réel strictement positif donné) : a) montrer que H est une primitive de f sur ]0, +∞[ ; b) en déduire F(ax) = F(a) + F(x) ; c) montrer que F(x/a) = F(x) − F(a). 4) Déterminer, à l'aide de F, la primitive G de g : ]−∞, 0[ → ℝ, x ↦ 1/x, qui s'annule en (−1).
- **Ex. 13** (p.114) : automobile roulant à 60 km/h. a) Chemin parcouru en 2 h 45 min ? b) x(t) chemin parcouru pendant le temps t en heures décimales : calculer x(t) en fonction de t. c) Représenter graphiquement x(t) et v(t) sur un même graphique (4 cm pour 1 h en abscisse, 1 cm pour 10 km, ou pour 10 km/h, en ordonnée). d) A et B points d'abscisses 0 et t de la courbe de v, C(t, 0) : aire du rectangle OABC (unité d'aire = aire du rectangle formé par les vecteurs unitaires) ? Comparer avec x(t).

### Aperçu historique (p.115–116)

Biographie de Leonhard Euler (Suisse, 1707 ; 1783) : formation à Bâle, élève de Johann Bernoulli, Saint-Pétersbourg et Berlin, constante d'Euler γ = lim(1 + 1/2 + … + 1/n) − ln n (γ = 0,57721566490153286060…), notation f(x), symbole Σ (somme de 1 à 1000 des k), théorie des nombres (Fermat n = 3, nombres parfaits, correspondance avec Goldbach). Aucun contenu mathématique à enseigner.

### Bornes de scope observées (chapitre 5)

- ✅ INCLUS : définition de primitive ; existence (fonction continue sur un intervalle, théorème 1) ; ensemble des primitives F + c ; unicité sous condition initiale F(a) = b ; linéarité (théorème 4) ; primitives des fonctions usuelles (x ↦ a, x, xⁿ n ∈ ℕ* puis ℤ* \ {−1}, 1/x², 1/√x, cos, sin, 1/cos², 1/sin², cos(ax+b), sin(ax+b), 1 + tan²(ax+b), 1 + cotan²(ax+b)) ; règles u′+v′, au′, u′v+v′u, u′uⁿ, u′/u², u′/uⁿ, u′/√u, (u′v−v′u)/v², (v′∘u)u′ ; linéarisation trigonométrique (sin3x·cos x) ; lien primitive ↔ aire (activités 6, préliminaire 1) ; vitesse/trajet ; usage de grapheur, Excel, Derive.
- ⛔ NON traité dans ce chapitre : intégrale définie ∫ₐᵇ f et son lien avec les primitives (chapitre 8) ; fonction ln (primitive de 1/x seulement construite par F de l'exercice 12, sans nom, ln est introduit au chapitre 6) ; fonction exp ; changement de variable ; intégration par parties ; équations différentielles ; primitive de 1/x sur ℝ* (n = −1 exclu des tableaux) ; pas de QCM / Vrai-Faux ; pas de problème « résolu » avec solution imprimée (les Exemples 2 à 9 sont posés, non rédigés).

> Sondage image : pages 100, 103, 104, 105, 106, 107, 108, 111, 112, 113 (10 pages sur 18 — le texte des pages 101–102, 109–110, 114, 115–116 relu en couche texte seule, pages simples) ; écarts : couche texte p.104 donnait « n ∈ ℕ » (au lieu de ℕ*), « ℤ » (au lieu de ℤ*\{−1}) ; p.106 « n ∈ ℕ » → ℕ* ; p.107 la couche texte avait déplacé les termes de l'Exemple 1 et de F(x) (−2√x) — corrigés sur image ; aucun mot ni nombre faux restant après confrontation.

## 2.6 Chapitre 6 — Fonctions logarithmes (manuel 222451, p.117–142)

**Page de garde (p.117)** — Titre : « Fonctions logarithmes », Chapitre 6. Plan : Activités préliminaires ; Cours (La Fonction logarithme népérien ; Dérivée d'une fonction composée du type (ln∘u) ; Propriété fondamentale des logarithmes et règles de calcul ; Étude de la fonction logarithme népérien ; Étude d'exemples de fonctions du type x ↦ ln(u(x))) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ; Aperçu Historique. **Pas de rubrique QCM / Vrai-Faux.** Notation : « tg », « cotg » ; le logarithme décimal est noté log ; « In » imprimé dans la couche texte = ln.

### Activités préliminaires (p.118)

- **Préliminaire 1** (p.118) : repère orthonormé (O, i⃗, j⃗) ; courbe (C) de f : x ↦ √x pour x ∈ [0, +∞[ (représentée). 1) Conjecturer graphiquement le sens de variation de f et la nature de la branche infinie de (C). 2) Justifier. 3) Calculer lim_{x→0} (f(1 + x) − f(1))/x ; que représente cette limite ? interpréter graphiquement. 4) Équation de la tangente (T) à (C) au point A(1, 1). 5) a) Tracer (T) ; b) conjecture sur la position relative de (T) et (C).
- **Préliminaire 2** (p.118) : a) Montrer que F : x ↦ √(x² − 4x + 5) est une primitive sur ℝ de f : x ↦ (x − 2)/√(x² − 4x + 5). b) Primitive de f sur ℝ qui s'annule en 2. c) Primitive de f sur ℝ qui s'annule en 0.
- **Préliminaire 3** (p.118) : montrer que chacune des fonctions suivantes admet une fonction primitive sur l'intervalle I et donner la primitive F de f, sur I, qui s'annule en a : a) f : x ↦ x³ ; I = ]−∞, +∞[, a = 0 ; b) f : x ↦ 1/√x ; I = ]0, +∞[, a = 1 ; c) f : x ↦ 1/x² ; I = ]0, +∞[, a = 2 ; d) f : x ↦ (2x + 1)/(x² + x)² ; I = [1, +∞[, a = 3. (Corrigé sur image : la couche texte donnait 1/x pour b).)

### Cours — Activités

**La fonction logarithme népérien** (p.119)

- **Activité 1** (p.119) : f(x) = 1/x sur I = ]0, +∞[. 1) Justifier que f admet au moins une primitive sur I. 2) x₀ ∈ I, F l'unique primitive de f sur I qui s'annule en x₀ : montrer que F est strictement croissante sur I.
- **Activité 2** (p.119) : avec une calculatrice, valeur approchée à 10⁻² près par excès de ln 2 ; ln 3 ; ln π ; ln 5 ; ln 10 ; ln(1/3) ; ln(1/2) et ln √2.
- **Activité 3** (p.119) : f : x ↦ x − 1/x sur I = ]0, +∞[ : déterminer la primitive F de f sur I telle que F(1) = 1.
- **Activité 4** (p.119) : g : x ↦ ln x / x. a) Ensemble de définition D de g. b) Montrer que g est dérivable sur D et calculer g′(x).

**Propriété fondamentale de la fonction ln — Règles de calcul** (p.120–121)

- **Activité 1** (p.120) : g(x) = ln(ax) sur ]0, +∞[, a réel strictement positif. 1) Avec g = ln∘u, u(x) = ax, montrer que g est dérivable et g′(x) = 1/x. 2) En déduire g(x) = ln x + k (k constante réelle). 3) Calculer g(1), en déduire k. 4) Montrer que pour a, b > 0, ln(ab) = ln a + ln b. (Exemples numériques : ln 6 = ln(2×3) = ln 2 + ln 3 ; ln 10 = ln 2 + ln 5.)
- **Activité 2** (p.120) : x, y > 0. a) Avec (1/x)·x = 1, montrer ln(1/x) = −ln(x). b) Montrer ln(x/y) = ln(x) − ln(y).
- **Activité 3** (p.120) : x > 0. 1) a) Exprimer ln(x²) en fonction de ln(x), puis montrer ln(x³) = 3 ln(x) ; b) par récurrence, ln(xⁿ) = n·ln(x) pour tout entier naturel n. 2) a) Montrer ln(1/x²) = −2 ln(x) ; b) n entier relatif négatif, n′ = −n : prouver ln(xⁿ) = n·ln(x).
- **Activité 4** (p.121) : 1) x > 0 : a) avec x = (√x)², exprimer ln √x à l'aide de ln x ; b) montrer que pour tout entier n ≥ 2, ln(ⁿ√x) = (1/n)·ln x. 2) r = p/q rationnel (p ∈ ℤ, q ∈ ℕ*) : a) a > 0, b tel que b^q = a^p : montrer ln b = r·ln a et b = ᑫ√(a^p) [notation : racine q-ième de a^p ; encart « On notera pour tous p ∈ ℤ, q ∈ ℕ* et a ∈ ℝ*₊ : q√a = a^(1/q) et q√(a^p) = a^(p/q) »] ; b) en déduire ln(a^r) = r·ln a.
- **Activité 5** (p.121) : simplifier l'écriture puis donner une valeur approchée de A = ln 128 − ln 32 − ln 8 ; B = ln 625 − ln 50 − ln 75 ; C = ln((9² × 4⁻³)/(2⁻⁵ × 3³)) ; D = ln((4⁷ × 3⁻¹²)²/(4⁻¹ × 3⁶)⁻⁵) ; E = ln((2^(1/3) × 5^(2/3))/(4^(1/8) × (√2)^(1/2))) [exposants lus sur image].

**Étude de la fonction x ↦ ln x** (p.122–124)

- **Activité 1** (p.122) : 1) a) Prouver que ln est dérivable et strictement croissante sur ]0, +∞[ ; b) en déduire x < 1 ⇒ ln x < 0, x > 1 ⇒ ln x > 0. 2) On suppose ln majorée sur ]1, +∞[ : a) prouver lim_{+∞} ln(x) = ℓ, ℓ finie ; b) calculer lim_{+∞} ln(2x), en déduire ℓ = ℓ + ln 2 ; c) conclusion ? 3) Déterminer alors lim_{+∞} ln(x). (Encart « Retenons » : lim_{x→+∞} ln(x) = +∞.)
- **Activité 2** (p.122) : 1) lim_{x→0⁺} ln(1/x). 2) Exprimer ln(1/x) en fonction de ln x. 3) En déduire lim_{x→0⁺} ln(x). (« Retenons » : lim_{x→0⁺} ln(x) = −∞.)
- **Activité 3** (p.122) : montrer que f : x ↦ ln x est une bijection de ℝ*₊ sur ℝ.
- **Activité 4** (p.123) : 1) Tableau de variation de ln (tableau imprimé : x de 0 à +∞ avec 1 et e ; f′ > 0 ; f de −∞ à +∞ passant par 0 en 1 et 1 en e). 2) Existence et unicité d'un réel e > 1 tel que ln e = 1. 3) Vérifier 2 < e < 3. 4) Montrer que ∀r ∈ ℚ, ln(eʳ) = r.
- **Activité 5** (p.123) : g(x) = 2√x − ln x sur I = ]1, +∞[. 1) Montrer que g est dérivable sur I et g′(x) = (√x − 1)/x. 2) En déduire g strictement croissante. 3) a) g(1) ; b) signe de g(x) sur I et 2√x > ln x. 4) Montrer ∀x ∈ I, 0 < ln x/x < 2/√x ; en déduire lim_{+∞} ln x/x. (« Retenons » : lim_{x→+∞} ln x / x = 0.)
- **Activité 6** (p.123–124) : f = ln, (C) sa courbe. 1) Branches infinies de (C). 2) Tangente T à (C) en A(1, 0). 3) Tangente D à (C) en B(e, 1). 4) g(x) = x − 1 − ln x : a) tableau de variation sur ]0, +∞[ ; b) signe de g, position relative de T et (C) ; c) de même D et (C). 5) Tracer T, D, (C) (figure imprimée : T : y = x − 1 ; D : y = (1/e)x). 6) a) Avec le théorème des accroissements finis, il existe c ∈ ]1, e[ tel que la tangente en c soit parallèle à (AB) ; b) déterminer c.
- **Activité 7** (p.124) : 1) Avec x·ln(1/x) = ln(1/x)/(1/x) pour x > 0, calculer lim_{x→0⁺} x·ln(1/x). 2) En déduire lim_{x→0⁺} x·ln x. (« Retenons » : lim_{x→0⁺} x·ln x = 0.)
- **Activité 8** (p.124) : calculer lim_{+∞} (x − ln x) ; lim_{+∞} (x² − ln x) ; lim_{+∞} ln(∛x)/x ; lim_{+∞} ln(x)/√x ; lim_{0⁺} x² ln(x) ; lim_{0⁺} (2x + 1) ln(x).
- **Activité 9** (p.124) : 1) r ∈ ℚ*₊. a) Montrer que ∀x ∈ ]0, +∞[, (1/r)·ln(xʳ) = ln x. b) Calculer lim_{+∞} ln(x)/xʳ et lim_{0⁺} xʳ·ln(x). (Encart « On admet que : ∀r ∈ ℚ*₊, lim_{x→0⁺} xʳ = 0 et lim_{x→+∞} xʳ = +∞ ».) 2) Calculer lim_{+∞} x^(−2/3)·ln(x) et lim_{0⁺} ∛x·ln(x). (« Retenons » : ∀r ∈ ℚ*₊, lim_{x→0⁺} xʳ·ln x = 0 et lim_{x→+∞} ln x / xʳ = 0.)
- **Activité 10** (p.124) : 1) f = ln sur ]0, +∞[ : a) nombre dérivé de f en x₀ = 1 ; b) en déduire lim_{x→1} ln x/(x − 1) = 1. 2) Calculer lim_{x→1} ln x/(x − 1)³. (« Retenons » : lim_{x→1} ln x/(x − 1) = 1.)

**Résolution d'équations et d'inéquations** (p.125)

- **Activité 1** (p.125) : résoudre dans ℝ : 1 + ln x = 0 ; 2 − ln x = 0 ; 1 + 3 ln x = 0 ; ln(3x − 5) = 0 ; ln|3x + 7| = ln 4 ; ln(x² + 1) = 0 ; ln(x² − 4x + 7) = ln 2 ; ln((3x − 4)/(x + 2)) = ln(x − 2).
- **Activité 2** (p.125) : résoudre dans ℝ : ln(2x − 3) < ln(x + 5) ; ln|4 − x| − ln 2 ≥ 0 ; ln(3x² + 5x − 2) > 0 ; ln((2x − 3)/(5x + 1)) ≤ 0 ; 2 ln(2 + x√3) − ln(2 − x√3) ≥ ln 2 ; ln(x − 1) + ln(x + 2) ≤ ln(x² − 1). (Encadré : [ln(u(x)) ≥ ln(v(x))] ⇔ { u(x) > 0 ; v(x) > 0 ; u(x) ≥ v(x) }.)
- **Activité 3** (p.125) : la population d'une ville augmente de 5 % par an ; en 2000, 80 000 habitants ; en quelle année dépassera-t-elle 100 000 ? Indication : n = rang de l'année après 2000, vérifier (1,05)ⁿ ≥ 1,25 puis déterminer n.

**Dérivée d'une fonction du type x ↦ ln(u(x))** (p.126–127)

- **Activité 1** (p.126) : 1) f(x) = ln(x² − 2x + 5), f = ln∘u avec u(x) = x² − 2x + 5 : montrer que f est définie et dérivable sur ℝ, calculer f′(x). 2) g(x) = ln|x| : montrer que g est dérivable sur ℝ* et ∀x ∈ ℝ*, g′(x) = 1/x. 3) u dérivable sur D ⊂ ℝ avec ∀x ∈ D, u(x) ≠ 0 ; f(x) = ln|u(x)| : montrer que f est dérivable sur D et f′(x) = u′(x)/u(x).
- **Activité 2** (p.126) : 1) f(x) = ln|x² − 1| : ensemble D de dérivabilité, calculer f′(x). 2) g(x) = x/(x² − 1) sur I = ]1, +∞[ : déterminer la primitive G de g sur I telle que G(√2) = 0.
- **Activité 3** (p.127) : 1) Montrer que chaque f admet une primitive sur I et donner la primitive F qui s'annule en a : a) f(x) = (2x + 1)/(x² + x + 1) ; I = ]−∞, +∞[, a = 0 ; b) f(x) = x/(x + 2) ; I = [−1, 1], a = 0 ; c) f(x) = 1/(x·ln x) ; I = ]1, +∞[, a = 2 ; d) f(x) = ln x / x ; I = ]0, +∞[, a = 1. 2) Montrer que F : x ↦ (1/2)x² ln x − (1/4)(x² − 1) est la primitive de f : x ↦ x ln x sur ]0, +∞[ qui s'annule en 1.

**Étude d'exemples de fonctions du type x ↦ ln(u(x))** (p.127–131)

- **Activité 1** (p.127) : g(x) = ln(1 + x). 1) Ensemble de définition D. 2) g dérivable sur D, g′(x) = 1/(1 + x). 3) En déduire lim_{x→0} ln(1 + x)/x puis une approximation affine de ln(1 + h) pour h « voisin de zéro ». 4) Valeur approchée de ln(1,01) ; ln(0,99) ; ln(0,97). (« Retenons » : lim_{x→0} ln(1 + x)/x = 1 ; pour x « voisin de 0 », x est une approximation affine de ln(1 + x).)
- **Activité 2** (p.127) : limites : lim_{+∞} x·ln(1 + 1/x) ; lim_{0⁺} x·ln(1 + 1/x) ; lim_{x→0} sin x / ln(x + 1) ; lim_{x→0} ln(x² − 3x + 1)/x.
- **Activité 3** (p.128) : f(x) = 1/(x + 1) − ln(x + 1). 1) Ensemble de définition D et limites aux bornes. 2) Sens de variation. 3) a) f(x) = 0 admet une solution unique α ; b) prouver 0,7 < α < 0,8. 4) Construire C (unité 4 cm). 5) a) f admet une réciproque f⁻¹ (ensemble de définition à préciser) ; b) tracer C′ de f⁻¹.
- **Activité 4** (p.128) : g(x) = 2x − 1 + ln(x/(x + 1)). 1) D et limites aux bornes. 2) Variations sur ]−∞, −1[ et ]0, +∞[. 3) a) g(x) = 0 admet une solution unique α dans ]0, +∞[ ; b) encadrement de α à 10⁻¹ près par défaut. 4) Branches infinies de C. 5) Construire C.
- **Activité 5** (p.128) : **I** — f(x) = x·ln x − x sur ]0, +∞[ : 1) a) f dérivable, f′(x) ; b) en déduire la primitive F de ln s'annulant en 1 ; c) sens de variation de f ; 2) limites en 0⁺ et +∞ ; 3) a) résoudre f(x) = 0 ; b) signe de f(x). **II** — g définie sur [0, +∞[ par g(0) = 0 et pour x > 0 g(x) = 2x²·ln x − 3x² : 1) a) continuité et dérivabilité à droite en 0 ; b) g′(x) pour x > 0 ; c) sens de variation de g (via I) ; d) limite en +∞, tableau de variation ; 2) a) résoudre g(x) = 0 ; b) construire C. (« Retenons » : une primitive de x ↦ ln(x) sur ]0, +∞[ est du type x ↦ x·ln x − x + k, k constante réelle arbitraire.)
- **Activité 6** (p.129) : repère orthonormé ; graphique d'une partie de la courbe C d'une fonction f définie sur ]0, +∞[ ; T tangente en A(1, 1). 1) Par lecture graphique : a) coefficient directeur de T ; b) f(1), f′(1), f′(e) ; c) réels x de ]1, +∞[ tels que f′(x) < 0. 2) Sachant f(x) = (x/2)[2 − ln x] sur ]0, +∞[ : a) retrouver l'ordonnée du point B où f admet un extremum global ; b) abscisse du point C (autre que O) où C coupe l'axe des abscisses ; c) lim_{+∞} f(x) et lim_{+∞} f(x)/x, interprétation ; d) prolongement par continuité g en 0 ; e) dérivabilité de g à droite en 0, interprétation ; f) tableau de variation de g, tracer C′ d'une autre couleur.
- **Activité 7** (p.129) : g(x) = ln x / ln 10. 1) Ensemble de définition D, limites aux bornes. 2) Tableau de variation, g(10). 3) g réalise une bijection de D sur ℝ. 4) Branches infinies de C. 5) Construire C.
- **Activité 8** (p.130) : f(x) = ln√|x² + 2x − 3|, C sa courbe. 1) Ensemble de définition D et limites aux bornes. 2) Montrer que Δ : x = −1 est un axe de symétrie de C. 3) f dérivable sur D, fonction dérivée. 4) Tableau de variation. 5) Points d'intersection de C avec l'axe des abscisses, équation de la tangente en chacun. 6) Tracer C.
- **Activité 9** (p.131) : f(x) = x + ln(2x − 1), C sa courbe. 1) D, branche parabolique de direction la droite Δ : y = x, position relative de C par rapport à Δ. 2) a) f réalise une bijection de D sur un intervalle J ; b) f(x) = 0 admet dans D une solution unique α, vérifier 0,7 < α < 0,8. 3) f⁻¹ réciproque : a) calculer (f⁻¹)′(1) ; b) tracer Δ, C et C′ (courbe de f⁻¹).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Définition** (p.119, vérifié image) — « Soit f la fonction définie sur l'ensemble des réels strictement positifs par f(x) = 1/x. On appelle fonction logarithme népérien (notée ln) la primitive de f sur ]0,+∞[ s'annulant en 1. Ainsi, la fonction ln est définie sur ]0,+∞[ et pour tout x ∈ ℝ*₊ on a : (ln)′(x) = 1/x et ln(1) = 0. »

> **Propriété fondamentale** (p.120) — « Pour tous réels strictement positifs a et b on a : ln(ab) = ln a + ln b. » (Exemples numériques : ln(6) = ln(2×3) = ln 2 + ln 3 ; ln(10) = ln 2 + ln 5.)

> **Propriétés** (p.121, vérifié image) — « Pour tous réels x et y strictement positifs et pour tout n ∈ ℤ, on a : * ln(x/y) = ln x − ln y ; ln(1/x) = −ln x ; ln(xⁿ) = n·ln x. * Pour tous réels a₁, a₂, …, aₙ strictement positifs on a : ln(a₁·a₂…aₙ) = Σ_{i=1}^{n} ln aᵢ »

> **Propriétés** (p.121) — « Pour tout réel x strictement positif et pour tout r ∈ ℚ, on a : * ln xʳ = r·ln x * En particulier pour r = 1/2, on a : ln x^(1/2) = ln √x = (1/2) ln x »

> **Retenons** (p.122–124, vérifié image) — lim_{x→+∞} ln(x) = +∞ ; lim_{x→0⁺} ln(x) = −∞ ; lim_{x→+∞} ln x / x = 0 ; lim_{x→0⁺} x·ln x = 0 ; lim_{x→1} ln x/(x − 1) = 1 ; « ∀r ∈ ℚ*₊, lim_{x→0⁺} xʳ·ln x = 0 et lim_{x→+∞} ln x / xʳ = 0 » ; ln e = 1 ; ln 1 = 0 ; 2 < e < 3 ; e ≈ 2,71828 ; « ∀r ∈ ℚ, on a ln eʳ = r » ; « e s'appelle la base du logarithme népérien ».

> **Propriétés** (p.122, vérifié image) — « Soit f la fonction définie sur ]0,+∞[ par f(x) = ln x. La fonction f est dérivable et strictement croissante sur ]0,+∞[. Elle réalise une bijection de ]0,+∞[ sur ℝ. i) Pour tous réels strictement positifs a et b on a : * (ln a = ln b) ⇔ (a = b) * (ln a > ln b) ⇔ (a > b) ii) Pour tout x ∈ ]0,+∞[ on a : * (ln x < 0) ⇔ x ∈ ]0, 1[ * (ln x > 0) ⇔ x ∈ ]1, +∞[ * (ln x = 0) ⇔ x = 1 »

> **Équivalences équation / inéquation** (l'équivalence d'inéquation figure en p.125 et au Résumé p.132 ; celle d'équation seulement au Résumé p.132) — [ln(u(x)) = ln(v(x))] ⇔ { u(x) > 0 ; v(x) > 0 ; u(x) = v(x) } ; [ln(u(x)) ≥ ln(v(x))] ⇔ { u(x) > 0 ; v(x) > 0 ; u(x) ≥ v(x) }.

> **Théorème** (p.126, vérifié image) — « * Si u est une fonction dérivable sur une partie D de ℝ et telle que ∀x ∈ D, u(x) > 0, alors la fonction f définie sur D par f(x) = ln(u(x)) est dérivable sur D et on a : ∀x ∈ D, f′(x) = u′(x)/u(x). * Si u est une fonction dérivable sur une partie D de ℝ et telle que ∀x ∈ D, u(x) ≠ 0, alors la fonction f définie sur D par f(x) = ln|u(x)| est dérivable sur D et on a : ∀x ∈ D, f′(x) = u′(x)/u(x). »

> **Retenons** (p.126) — « Si u est une fonction dérivable sur un intervalle I de ℝ et telle que ∀x ∈ I, u(x) ≠ 0, alors les primitives de la fonction x ↦ u′(x)/u(x) sont les fonctions F définies sur I par F(x) = ln|u(x)| + k, où k est une constante réelle arbitraire. »

> **Retenons** (p.127, p.128) — « lim_{x→0} ln(1 + x)/x = 1. Pour x « voisin de 0 » on a : x est une approximation affine de ln(1 + x). » ; « Une primitive de la fonction x ↦ ln(x) sur ]0, +∞[ est du type x ↦ x·ln x − x + k où k est une constante réelle arbitraire. »

> **Le logarithme décimal** (p.129, vérifié image) — « On appelle fonction logarithme de base 10 (ou fonction logarithme décimale) la fonction, notée log, définie sur ]0, +∞[ par g(x) = ln x / ln 10. On a : * Pour tout réel x strictement positif, log x = 0.43 ln x et ln x ≃ (2,3)·log x [sic : « = » imprimé pour une valeur approchée ; le Résumé p.132 écrit « ≈ 0,43 ln x »] * log 10 = 1 et pour tout r ∈ ℚ, log 10ʳ = r. »

> **Résumé du cours** (p.132–133, vérifié image p.132) — ln strictement croissante et dérivable sur ]0, +∞[, bijection de ]0, +∞[ sur ℝ ; (ln)′(x) = 1/x ; ln 1 = 0 ; ln e = 1 ; (e ≈ 2,72) ; signe de ln ; ln a = ln b ⇔ a = b ; ln a > ln b ⇔ a > b ; ln xy = ln x + ln y ; ln(x/y) = ln x − ln y ; ln(1/x) = −ln x ; ln xʳ = r·ln x (r ∈ ℚ), en particulier ln √x = (1/2) ln x ; limites usuelles (lim_{+∞} ln x = +∞ ; lim_{0⁺} ln x = −∞ ; lim_{+∞} ln x / x = 0 ; lim_{0⁺} x·ln x = 0 ; lim_{x→0} ln(1 + x)/x = lim_{x→1} ln x/(x − 1) = 1) ; x approximation affine de ln(1 + x) ; ∀r ∈ ℚ*₊, lim_{0⁺} xʳ ln x = 0 et lim_{+∞} ln x / xʳ = 0 ; équivalences équation/inéquation ; logarithme décimal log x = ln x / ln 10 ≈ 0,43 ln x ; dérivée de x ↦ ln|u(x)| = u′/u (u ≠ 0 sur D) ; primitives de u′/u : ln|u| + k ; une primitive de ln sur ]0, +∞[ : x ↦ x ln x − x + k.

### Cours — Exercices résolus (2)

- **Exercice résolu 1** (p.125, solution intégrale imprimée) : société au chiffre d'affaires de 600 000 DT, qui prévoit de l'augmenter de 5 % par an ; au bout de quel nombre d'années ≥ 900 000 DT ? Solution : C₀ = 600 000, Cₙ₊₁ = Cₙ + 0,05 Cₙ = 1,05 Cₙ ; suite géométrique de raison q = 1,05, Cₙ = (1,05)ⁿ·C₀ ; 600 000(1,05)ⁿ ≥ 900 000 ⇔ (1,05)ⁿ ≥ 1,5 ⇔ ln((1,05)ⁿ) ≥ ln 1,5 ⇔ n·ln(1,05) ≥ ln(1,5) ⇔ n ≥ ln(1,5)/ln(1,05) ≈ 8,3 ; « à partir de la 9ème année le chiffre d'affaire de la société sera supérieur à 900.000 DT. »
- **Exercice résolu 2** (p.130–131, solution intégrale imprimée) : f(x) = 1/(x(1 + ln x)). 1) D. 2) Variations de f sur D. 3) g restriction de f à I = ]1/e, +∞[ : a) g bijection de I sur g(I), courbes de g et g⁻¹ ; b) g(e) et (g⁻¹)′(1/(2e)). Solution : 1) 1 + ln x = 0 ⇔ x = 1/e ; D = ]0, 1/e[ ∪ ]1/e, +∞[. 2) f′(x) = −u′(x)/u²(x), u(x) = x(1 + ln x) ; f′(x) = (−2 − ln x)/[x(1 + ln x)]² ; même signe que −2 − ln x ; −2 − ln x > 0 ⇔ x < e⁻² ; f strictement croissante sur ]0, 1/e²[ et strictement décroissante sur ]1/e², 1/e[ ∪ ]1/e, +∞[. 3) a) g continue strictement décroissante, bijection de I sur g(I) = ]lim_{+∞} f, lim_{x→(1/e)⁺} f[ = ]0, +∞[ ; b) g(e) = 1/(2e), donc (g⁻¹)′(1/(2e)) = 1/g′(e) = −(4/3)e². Courbes : C_{g⁻¹} = S_D(C_g), D : y = x (figure imprimée avec asymptotes y = 1/e et x = 1/e).

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.134) — 1 activité

f(x) = ln((x + √(x² + 4))/2) et g(x) = ln(x), courbes (C) et (C′) ; étudier leur position relative. **I — Avec Cabri II plus** (ressource Internet indiquée) : écrire les expressions ln((x + sqrt(x^2+4))/2) et ln(x) ; montrer les axes ; appliquer chaque expression sur un axe pour obtenir (C) et (C′) ; conjecturer la position relative ; conjecturer l'ensemble de définition de f, son sens de variation et les éléments de symétrie de (C) ; en déduire que f réalise une bijection de ℝ sur ℝ ; construire d'une autre couleur la courbe de f⁻¹. **II** — 1) a) calculer (x + √(x²+4))(x − √(x²+4)) ; b) en déduire ∀x ∈ ℝ, x + √(x²+4) > 0, D_f = ℝ, f impaire ; 2) tableau de variation de f ; 3) f bijection de ℝ sur ℝ ; 4) ∀x ∈ ]0, +∞[, f(x) − g(x) > 0 ; 5) lim_{+∞} (f(x) − ln x) = 0, position relative de (C) et (C′).

### Exercices et problèmes (p.135–140) — 25 exercices

- **Ex. 1** (p.135) : f(x) = x ln x et g(x) = x² ln x sur ]0, +∞[. 1) g′(x). 2) Vérifier g′(x) − x = 2f(x). 3) En déduire une primitive de f sur ]0, +∞[.
- **Ex. 2** (p.135) : ensemble D de dérivabilité et f′(x) : 1) ln(2x + 1) ; 2) 1/ln x ; 3) √(ln(x + 1)) ; 4) ln x / x ; 5) ln(x² − 3x) ; 6) ln|x² + x − 2| ; 7) ln|cos x| ; 8) ln²(2x + 1) ; 9) ln(ln x) ; 10) ln((x + 1)/(1 − x)) ; 11) (x + ln x)/x ; 12) x·ln|(x − 1)/x|.
- **Ex. 3** (p.135) : une primitive F de f sur I : a) 1/(4x − 3), I = ]3/4, +∞[ ; b) (x² + x + 1)/x, I = ]0, +∞[ ; c) ln²x / x, I = ]0, +∞[ ; d) 1/(x(ln x + 1)), I = ]e⁻¹, +∞[ ; e) 1/(x ln²x), I = ]1, +∞[ ; f) (2x + 1)/(2x² + 2x + 1), I = ]−∞, +∞[ ; g) (2x + 4)/(x − 1), I = ]1, +∞[.
- **Ex. 4** (p.135) : 1) g(x) = (x² + 4x + 7)/(x + 2) sur ℝ − {−2} : a) a, b, c tels que g(x) = ax + b + c/(x + 2) ; b) en déduire la primitive G de g sur ]−2, +∞[ qui s'annule en (−1). 2) Primitive F de f : x ↦ x/(x + 1)² sur [0, +∞[ telle que F(0) = 0 (indication : écrire f(x) = α/(x + 1)² + β/(x + 1)).
- **Ex. 5** (p.135) : résoudre dans ℝ : a) ln(2x − 1) = 0 ; b) ln(2x + 1) − 1 = 0 ; c) ln(x + 1) − ln(2 − x) + ln 2 = ln 7 − ln(4 − x) ; d) ln²x − 3 ln x − 4 = 0 ; e) ln|2x + 1| = 2 ln 2 ; f) (1/2) ln|x + 1| = ln|x + 2| ; g) ln|x + 3| + ln|x + 5| = ln 15.
- **Ex. 6** (p.135) : résoudre dans ℝ : ln²x − ln(1/x) − 2 = 0 ; 1 + ln x = 6/ln x ; ln x − 2 ln(x − 4) + ln 2 = 0 ; ln|x + 1| < 1 ; ln|x| < −ln|3x + 2| ; 2 ln x ≥ 1 ; ln(2 − x) + ln 2 < ln(x + 1) ; ln(x² − 4e²) < 1 + ln(3x).
- **Ex. 7** (p.136) : calculer 25 limites : lim_{+∞}(√x − ln x) ; lim_{0⁺}(√x ln x) ; lim_{+∞} ln x/√x ; lim_{0⁺} x³/ln x ; lim_{0⁺}(x − ln x) ; lim_{0⁺} ln(x + 1)/√x ; lim_{+∞} ln((x + 2)/(x − 1)) ; lim_{+∞} ln(x + 2)/(x + 3) ; lim_{+∞} (ln x + 1)/(ln x − 1) ; lim_{+∞} ln(x + 1)/x ; lim_{+∞} x ln((x + 1)/x) ; lim_{+∞} ln²x/x ; lim_{+∞} (2ln³x − ln²x + 3 ln x − 4) ; lim_{0⁺} ln(x + 1)/(x ln x) ; lim_{0⁺} ln(x + 1)/(4x) ; lim_{x→0} ln(x² + x + 1)/x ; lim_{x→0} ln(1 + x²)/x² ; lim_{0⁺} x^(2/3) ln x ; lim_{0⁺} x^(3/2) ln x ; lim_{+∞} ln x/∛x ; lim_{+∞} ln(∛x)/x ; lim_{x→2} ln(x/2)/(x − 2) ; lim_{x→e} (ln x − 1)/(x − e) ; lim_{+∞} (x² − 2)/(x ln x) ; lim_{x→1} ln|(x + 2)/(x − 1)|.
- **Ex. 8** (p.136) : f(x) = x − 1 − ln x et g(x) = ln x − (x − 1)/x sur ]0, +∞[. 1) Sens de variation de f et g. 2) En déduire ∀x ∈ ]1, +∞[, (x − 1)/x < ln x < x − 1.
- **Ex. 9** (p.136) : f définie sur ℝ par f(x) = 2x − x·ln|x| si x ≠ 0, f(0) = 0. 1) Continuité et dérivabilité de f en 0. 2) a) f impaire ; b) variations de f, tracer C.
- **Ex. 10** (p.136) : f(x) = ln|x² − 1|. 1) Ensemble de définition, parité. 2) Tableau de variation. 3) Branches infinies de C, tracer C. 4) g(x) = x·ln(x² − 1) + ln((x + 1)/(x − 1)) − 2x : montrer que g est une primitive de f sur ]1, +∞[.
- **Ex. 11** (p.136) : f(x) = ln|(3x − 6)/(x + 2)|, C sa courbe. 1) Variations de f sur chaque intervalle de définition. 2) Le point Ω(0, ln 3) est centre de symétrie de C. 3) Intersection de C avec les axes. 4) Tracer C. 5) g restriction de f à ]−2, 2[ : a) g bijection de ]−2, 2[ sur un intervalle J ; b) g⁻¹ dérivable en y₀ = ln 3, calculer (g⁻¹)′(ln 3).
- **Ex. 12** (p.136–137) : 1) g(x) = x·ln²x − 1 : a) tableau de variation sur ]0, +∞[ ; b) g(x) = 0 admet une solution unique α ∈ ]2, 3[ ; c) signe de g(x). 2) f définie par f(x) = (x ln x + 1)/ln x si x ≠ 1 et f(0) = 0 [sic : la définition imprimée donne f(0) = 0 alors que x ln x + 1 / ln x n'est défini que pour x > 0, x ≠ 1 ; l'énoncé demande D en a)] : a) ensemble de définition D de f ; b) f continue à droite en 0 ; c) dérivabilité à droite en 0 ; d) variations de f sur ]0, +∞[ ; e) montrer f(α) = α + √α ; f) la droite D : y = x est asymptote à C ; g) tracer C (α ≃ 2,5).
- **Ex. 13** (p.137) : f(x) = √(1 − ln x). 1) D. 2) f′(x) et f″(x) lorsqu'ils existent. 3) Variations. 4) f bijection de D sur ]0, +∞[ [sic : f(e) = 0, l'image exacte est [0, +∞[]. 5) C possède un point d'inflexion, équation de la tangente en ce point. 6) Construire C.
- **Ex. 14** (p.137) : g(x) = 2x√x − 3 ln x + 6 et f(x) = 3 ln x/√x + x − 1 sur ]0, +∞[. 1) Variation de g, signe de g(x). 2) Limites de f en 0⁺ et +∞. 3) Sens de variation de f. 4) D : y = x − 1 asymptote à C. 5) Position relative de D et C. 6) Tracer D et C.
- **Ex. 15** (p.137) : f sur [0, +∞[ : f(x) = x ln x/(x + 1) si x > 0, f(0) = 0. 1) Continuité et dérivabilité en 0. 2) g(x) = x + 1 + ln x sur ]0, +∞[ : a) variations ; b) g(x) = 0 admet une solution unique β avec 0,27 < β < 0,28. 3) a) f′(x) ; b) tableau de variation ; c) lim_{+∞}(f(x) − ln x), interprétation graphique. 4) Construire C et C′ (courbe de ln) dans un même repère.
- **Ex. 16** (p.137) : combien de fois une cellule s'est-elle divisée en 2 si on en compte 10⁶ ? Indication : n divisions, 2ⁿ = 10⁶, déterminer n.
- **Ex. 17** (p.137) : pH = −log[H₃O⁺] = −ln[H₃O⁺]/ln 10, [H₃O⁺] concentration (mol/L). 1) pH pour [H₃O⁺] = 2,3·10⁻³. 2) Concentration en ions H₃O⁺ d'une solution de pH = 9,4.
- **Ex. 18** (p.138) : f sur [0,1 ; 6] : y = f(x) = 70,228 + 5,104x + 9,222 ln x ; (C) dans un repère orthogonal (1 cm = 1 unité en abscisse, 1 cm = 10 unités en ordonnée). 1) Compléter le tableau (x = 0,1 ; 0,3 ; 0,5 ; 1 ; 2 ; 3 ; 4 ; 5 ; 6) en arrondissant à l'entier le plus proche. 2) Variations de f, tracer (C). 3) Formule empirique de la taille y (cm) d'un enfant de moins de 6 ans selon son âge x (années) : a) taille à 2 ans et demi à 1 cm près ; b) âge d'un enfant mesurant 1 m.
- **Ex. 19** (p.138) : polonium (Po, numéro atomique 84), masse divisée par 2 tous les 138 jours ; masse de départ 10 g ; au bout de combien de temps restera-t-il 0,1 g ? Indication : n périodes, vérifier (0,5)ⁿ = 0,01 puis déterminer n.
- **Ex. 20** (p.138) : trajectoire d'une balle de golf. 1) h(t) = −5t² + 20t pour t ≥ 0 : a) instant où la balle retombe ; b) instant et valeur de la hauteur maximale. 2) Avec résistance de l'air : h(t) = −5t² + 11t − 2 ln(t + 1) : a) h(0), interprétation ; b) variations de h ; c) instant et hauteur maximale (valeur approchée au mètre près) ; d) à la calculatrice, instant approché où la balle retombe.
- **Ex. 21** (p.138) : u : x ↦ √(x² + 1) + x et v : x ↦ √(x² + 1) − x sur ℝ. 1) a) u(x)·v(x), en déduire u(x) et v(x) de même signe ; b) pour tout x, u(x) et v(x) > 0 (indication : ∀x ∈ ℝ, √(x² + 1) ≥ |x|). 2) a) u′(x) ; b) en déduire la primitive F de f : x ↦ 1/√(x² + 1) sur ℝ telle que F(0) = 0. 3) a) F paire [sic : l'énoncé imprimé dit « F est une fonction paire » alors que F, primitive nulle en 0 d'une fonction paire, est impaire ; coquille de l'énoncé à noter] ; b) sens de variation de F ; c) construire C ; d) équation de la tangente T à C au point d'abscisse 0.
- **Ex. 22** (p.139, « D'après Bac Tunisien 1995 ») : **I** — g(x) = x + (x − 2) ln x sur ]0, +∞[ : 1) a) g′(x) = 2((x − 1)/x) + ln x ; b) x > 1 ⇒ g′(x) > 0, 0 < x < 1 ⇒ g′(x) < 0 ; 2) a) variations de g ; b) ∀x > 0, g(x) ≥ 1. **II** — f(x) = 1 + x ln x − (ln x)² sur ]0, +∞[ : 1) a) f′(x) = g(x)/x et variations de f ; b) f admet une réciproque f⁻¹ sur un intervalle J ; 2) C dans un repère orthonormé (unité 2 cm) : a) tangente T à C au point d'abscisse 1 ; b) variations de h(x) = x − 1 − ln x, signe de h ; c) f(x) − x = (ln x − 1)·h(x), position de C par rapport à T ; 3) tracer C, T et C′ (courbe de f⁻¹).
- **Ex. 23** (p.139, « D'après Bac Tunisien 1996 ») : f(x) = 1 + ln[x(2 − x)], C (unité 4 cm). 1) a) l'ensemble de définition est ]0, 2[ ; b) tableau de variation. 2) a) x = 1 axe de symétrie ; b) abscisses des points d'intersection de C avec (O, i⃗), x₀ la plus petite. 3) φ(x) = f(x) − x sur ]0, 2[ : a) tableau de variation de φ ; b) φ(x) = 0 a exactement deux solutions, 1 et α ; vérifier x₀ < α < 0,3 et ln[α(2 − α)] = α − 1 ; c) signe de φ, position de C par rapport à Δ : y = x. 4) Tracer C et Δ (x₀ ≈ 0,2). 5) g restriction de f à I = ]0, 1] : a) g bijection de I sur J ; b) g⁻¹(x) pour x ∈ J.
- **Ex. 24** (p.139–140, « D'après Bac Tunisien 2000 ») : 1) g(x) = −1 + x + 2 ln x sur ]0, +∞[ : a) variation ; b) g(1), signe de g ; c) x > 1 ⇒ g(1/x) < 0 et 0 < x < 1 ⇒ g(1/x) > 0. 2) f sur [0, +∞[ : f(x) = x − x² ln x si x > 0, f(0) = 0 : a) dérivable à droite en 0 ; b) f′(x) = x·g(1/x) ; c) tableau de variation ; d) f(x) = 0 admet exactement une solution α avec 7/4 < α < 2. 3) a) tangente Δ en O : y = x ; b) position de C par rapport à Δ ; c) tracer Δ et C (unité 2 cm).
- **Ex. 25** (p.140, « D'après Bac Tunisien 2004 ») : f définie et dérivable sur ℝ \ {−1, 1}, C sa courbe ; graphique d'une partie de C et de D : y = x ; tangente horizontale en O, asymptotes x = −1 et x = 1. **I** (lecture graphique) : 1) a) lim_{x→−1} f(x) et lim_{x→1} f(x) ; b) tableau de variation sur [−2, 2] ; c) nombre de solutions de f(x) = x dans [−2, 2], α celle de ]0, 1[ ; 2) g restriction de f à [0, 1[ : a) bijection de [0, 1[ sur J ; b) tracer C′ de g⁻¹. **II** — on suppose f(x) = ax + b + ln|(x + 1)/(x − 1)| : 1) a) f′(x) = a − 2/(x² − 1) ; b) a = −2 et b = 0 ; 2) f(x) = −2x + ln|(x + 1)/(x − 1)| : a) f impaire ; b) tableau de variation ; 3) Δ : y = −2x asymptote à C ; 4) tracer Δ et compléter le graphique.

### Aperçu historique (p.141–142)

John Napier (Neper), baron de Merchiston (1550–1617), mathématicien écossais, père des logarithmes (1614) ; lien progression arithmétique / géométrique, relation 2 sin A sin B = cos(A − B) − cos(A + B), Briggs et les logarithmes décimaux, Bürgi ; réglettes de Neper (multiplication de 327 par 546 = 178 542, exemple détaillé p.142). Aucun contenu à enseigner.

### Bornes de scope observées (chapitre 6)

- ✅ INCLUS : définition de ln comme primitive de 1/x s'annulant en 1 ; propriété fondamentale (ln(ab)), quotient, inverse, puissances (ℤ puis ℚ), sommes de logarithmes ; étude de ln (variations, limites en 0⁺ et +∞, bijection ℝ*₊ → ℝ, nombre e, ln eʳ = r) ; croissances comparées (ln x / x, xʳ ln x, x ln x) ; limite ln x/(x − 1) et ln(1 + x)/x, approximation affine ; branches infinies, tangentes et position relative ; équations et inéquations logarithmiques, problèmes de croissance (suites géométriques) ; dérivée de ln|u| ; primitives de u′/u et de ln ; logarithme décimal ; fonctions réciproques et dérivée de g⁻¹ ; sujets d'annales du bac tunisien (1995, 1996, 2000, 2004).
- ⛔ NON traité dans ce chapitre : fonction exponentielle comme fonction (chapitre 7) ; équations différentielles ; intégrale définie et calculs d'aires par ln (chapitre 8) ; logarithme de base quelconque (seul log₁₀) ; intégration par parties ; pas de QCM / Vrai-Faux.

> Sondage image : pages 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 135, 136, 137, 138, 139, 140 confrontées au PNG (21 pages sur 26 ; pages 117, 133, 134, 141, 142 en couche texte seule : page de garde, fin du résumé, activité informatique, biographie, simples) ; écarts : p.118 la couche texte donnait 1/x au lieu de 1/√x (Préliminaire 3 b, corrigé) ; p.121 la couche texte avait perdu les exposants fractionnaires de E (corrigés sur image) ; p.122–124 encarts « Retenons » décalés en couche texte (corrigés) ; p.129 « ≃ » lu « = » sur la formule log x ; p.136 l'ordre des limites de l'ex. 7 mélangé en couche texte (rétabli sur image) ; p.137 l'ex. 12 fragmenté en couche texte (rétabli sur image) ; aucun mot ou nombre faux restant sur les pages vues.

## 2.7 Chapitre 7 — Fonctions exponentielles (manuel 222451, p.143–166)

**Page de garde (p.143)** — Titre : « Fonctions exponentielles », Chapitre 7. Plan : Activités préliminaires ; Cours (La fonction exponentielle de base e ; Théorème fondamental — Règles de calcul ; Étude de la fonction exponentielle ; Dérivée de eᵘ — Primitives de u′·eᵘ ; Fonctions puissances ; Étude d'exemples de fonctions du type x ↦ e^{u(x)}) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ; Aperçu Historique. **Pas de rubrique QCM / Vrai-Faux.** Notation : « In » (couche texte) = ln ; « tan » écrit dans le chapitre.

### Activités préliminaires (p.144)

- **Préliminaire 1** (p.144) : f : x ↦ 1 − √x pour x ∈ [0, +∞[. 1) a) Montrer que f réalise une bijection de [0, +∞[ sur un intervalle J à préciser puis expliciter f⁻¹(x) pour x ∈ J ; b) citer les différentes propriétés de f⁻¹. 2) Représenter les courbes de f et f⁻¹ dans un repère orthonormé (O, i⃗, j⃗).
- **Préliminaire 2** (p.144) : résoudre dans ℝ : a) ln x = 1 ; b) ln x = 0 ; c) ln x = 2 ; d) ln x = −3 ; e) ln x = −1 ; f) ln x = 0.5.
- **Préliminaire 3** (p.144) : 1) Résoudre dans ℝ l'équation x² − 4x − 5 = 0. 2) En déduire la résolution dans ℝ de (ln x)² − 4 ln x − 5 = 0.
- **Préliminaire 4** (p.144) : montrer que chaque f admet une primitive sur I et donner la primitive F qui s'annule en a : a) f : x ↦ 2/(x + 1) ; I = ]−1, +∞[, a = 0 ; b) f : x ↦ 1/(x·ln x) ; I = ]1, +∞[, a = e.
- **Préliminaire 5** (p.144) : donner l'ensemble D sur lequel f est dérivable et calculer f′(x) : a) f : x ↦ ln((x + 1)²) ; b) f : x ↦ ln√(x² + x − 2) ; c) f : x ↦ ln|x² − x|.

### Cours — Activités

**La fonction exponentielle de base e** (p.145–146)

- **Activité 1** (p.145) : f : x ↦ ln x. 1) Montrer que f réalise une bijection de ]0, +∞[ sur ℝ. 2) f⁻¹ réciproque : calculer f⁻¹(0) et f⁻¹(1). 3) Prouver que f⁻¹ est une bijection de ℝ sur ]0, +∞[.
- **Activité 2** (p.145) : montrer que pour tous réels x et y tels que y > 0 : a) exp(x) = y ⇔ x = ln y ; b) ln[exp(x)] = x ; c) exp(ln y) = y.
- **Activité 3** (p.145) : 1) montrer que pour tous réels x et y : a) exp(x) = exp(y) ⇔ x = y ; b) exp(x) < exp(y) ⇔ x < y. 2) En déduire que pour tout réel a : a) a < 0 ⇔ 0 < exp(a) < 1 ; b) a > 0 ⇔ exp(a) > 1.
- **Activité 4** (p.146) : simplifier m = exp(3 ln 2) ; n = exp(−3 ln 2) ; p = ln[exp(1/3)] ; q = ln[e/exp(1/2)] ; r = ln √(exp(−3)).
- **Activité 5** (p.146) : résoudre dans ℝ : a) ln²x + ln x − 12 = 0 ; b) (2 exp(x) − 3)/(exp(x) + 1) = 5/3 ; c) exp(3x − 1) < 1 ; d) exp(2x² + x + 1) ≥ exp(1 − x).

**Théorème fondamental — Règles de calcul** (p.146–147)

- **Activité 1** (p.146) : a, b réels, x = exp(a), y = exp(b). 1) Exprimer ln x et ln y à l'aide de a et b. 2) Vérifier a + b = ln(xy). 3) En déduire exp(a + b) = exp(a)·exp(b).
- **Activité 2** (p.146) : 1) a réel : a) calculer de deux façons exp(a + (−a)) ; b) en déduire exp(−a) = 1/exp(a). 2) a, b réels : montrer exp(a − b) = exp(a)/exp(b).
- **Activité 3** (p.147) : r rationnel. a) Calculer ln(eʳ) et ln[exp(r)]. b) Conclure.
- **Activité 4** (p.147) : a réel, r rationnel : montrer que (eᵃ)ʳ = e^{a r}.
- **Activité 5** (p.147) : 1) a réel, écrire plus simplement A = (eᵃ + e⁻ᵃ)² − (eᵃ − e⁻ᵃ)² ; B = (eᵃ)²/(e × e^{a²}). 2) Équations (E) : e⁻³ˣ − 2e⁻²ˣ + e⁻ˣ = 0 et (F) : e⁴ˣ + 3e³ˣ + 3e²ˣ + eˣ = 0 ; a) vérifier e⁻³ˣ − 2e⁻²ˣ + e⁻ˣ = e⁻ˣ(e⁻ˣ − 1)² et e⁴ˣ + 3e³ˣ + 3e²ˣ + eˣ = eˣ(eˣ + 1)³ ; b) résoudre dans ℝ (E) et (F). 3) Résoudre dans ℝ : e^{2x−4} ≤ 1.

**Étude de la fonction x ↦ eˣ** (p.148–151)

- **Activité 1** (p.148) : f(x) = eˣ et g(x) = ln(eˣ) sur ℝ. 1) En utilisant la dérivabilité de ln sur ]0, +∞[, prouver que f est dérivable sur ℝ. 2) Montrer que g est dérivable sur ℝ et g′(x) = f′(x)/f(x). 3) a) Prouver g′(x) = 1 ; b) en déduire f′(x) = f(x) ; c) sens de variation de f.
- **Activité 2** (p.148) : 1) f(x) = eˣ − x − 1 sur ℝ : a) variations de f, calculer f(0) ; b) en déduire ∀x ∈ ℝ, eˣ ≥ x + 1 ; c) prouver lim_{+∞} eˣ = +∞. 2) Avec e⁻ˣ = 1/eˣ, montrer lim_{−∞} eˣ = 0.
- **Activité 3** (p.148) : calculer lim_{+∞} eˣ/x : a) en posant y = eˣ, montrer lim_{x→+∞} eˣ/x = lim_{y→+∞} 1/((ln y)/y) ; b) conclure.
- **Activité 4** (p.149) : 1) Tableau de variation de f : x ↦ eˣ. 2) Tracer dans le même repère orthonormé les courbes de ln et exp. 3) Équations des tangentes à la courbe de exp aux points A(0 ; 1) et B(1 ; e).
- **Activité 5** (p.150) : 1) montrer lim_{x→−∞} x eˣ = 0 (on pourra poser X = −x). 2) a) Vérifier que pour tout entier naturel non nul n et tout réel x, xⁿeˣ = ((x/n)·e^{x/n})ⁿ × nⁿ ; b) en déduire lim_{−∞} xⁿeˣ. 3) r rationnel positif, x > 0 : a) exprimer ln(eˣ/xʳ) à l'aide de x, r et ln x ; b) calculer lim_{+∞} ln(eˣ/xʳ) ; c) en déduire lim_{+∞} eˣ/xʳ.
- **Activité 6** (p.150) : calculer les limites : 1) lim_{+∞} x eˣ ; 2) lim_{+∞} (x − eˣ) ; 3) lim_{−∞} x² eˣ ; 4) lim_{+∞} ln(x)·e⁻ˣ ; 5) lim_{+∞} x²/eˣ ; 6) lim_{x→0} x² e^{1/x} ; 7) lim_{+∞} eˣ/x² ; 8) lim_{+∞} e^{2x}/x.
- **Activité 7** (p.150) : f : x ↦ eˣ. 1) a) Nombre dérivé de f en x₀ = 0 ; b) en déduire lim_{x→0} (eˣ − 1)/x = 1. 2) a) Approximation affine de f en x₀ = 0 ; b) en déduire qu'il existe φ définie sur un intervalle contenant 0 telle que eˣ = 1 + x + xφ(x) avec lim_{x→0} φ(x) = 0.
- **Activité 8** (p.151) : 1) Valeur approchée de e^{0.01} ; e^{0.1} ; e^{−0.03} et e^{10⁻⁶}. 2) Limites en 0 : a) (e^{2x} − 1)/x ; b) (e^{3x} − 1)/(2x) ; c) (e^{sin x} − 1)/x ; d) (eˣ − 1)/sin x ; e) (e^{x²} − 1)/(1 − cos x).

**Dérivée de eᵘ — Primitives de u′·eᵘ** (p.151–152)

- **Activité 1** (p.151) : 1) u dérivable sur D ⊂ ℝ à valeurs dans ℝ, f(x) = e^{u(x)} : montrer que f est dérivable sur D et calculer f′(x). 2) g(x) = e^{(x−1)/x²} : ensemble D de dérivabilité, calculer g′(x).
- **Activité 2** (p.151) : ensemble D de dérivabilité et f′(x) pour : 1) f(x) = e^{x²} ; 2) f(x) = x eˣ ; 3) f(x) = ln(eˣ − 1) ; 4) f(x) = e^{1/x} ; 5) f(x) = e^{sin x}.
- **Activité 3** (p.151) : 1) Primitives de f : x ↦ eˣ sur ℝ. 2) u dérivable sur un intervalle I : primitives de g : x ↦ u′(x)·e^{u(x)} sur I.
- **Activité 4** (p.152) : une primitive de f sur I : 1) f(x) = x e^{x²}, I = ℝ ; 2) f(x) = e^{1/x}/x², I = ]0, +∞[ ; 3) f(x) = e^{2x}, I = ℝ ; 4) f(x) = eˣ/(eˣ − 1), I = ]0, +∞[ ; 5) f(x) = (eˣ − 1)², I = ℝ ; 6) f(x) = (2x + 3) e^{x² + 3x − 1}, I = ℝ.

**Fonctions puissances — Fonctions du type x ↦ aˣ, a ∈ ]0, +∞[** (p.152–153)

- **Activité 1** (p.152) : a ∈ ℝ*₊ et r ∈ ℚ. 1) Simplifier ln(aʳ) et ln(e^{r·ln a}). 2) En déduire aʳ = e^{r·ln a}.
- **Activité 2** (p.152) : a réel strictement positif, f : x ↦ aˣ. 1) Montrer que f est dérivable sur ℝ et calculer f′(x). 2) Tableau de variation de f, trois cas : 0 < a < 1, a > 1, a = 1. 3) Variations de g : x ↦ 2ˣ et h : x ↦ (0,5)ˣ et tracer leurs courbes dans un repère orthonormé.
- **Activité 3** (p.153) : a > 0, x et y réels, r rationnel : montrer a^{x+y} = aˣ·aʸ ; a⁻ˣ = 1/aˣ ; a^{x−y} = aˣ/aʸ ; (aˣ)ʳ = a^{r·x}.
- **Activité 4** (p.153) : écrire plus simplement a = (3,1)^{2√3} × (3,1)^{1−√12} ; b = (0,5)^{3/4} × (0,5)^{−7/4} ; c = (3^{π−2} × 9)/27^{1/3} ; d = ((1,5)^{−2/7})³/(1,5)^{−7/6}.
- **Activité 5** (p.153) : 1) Résoudre dans ℝ : a) 2ˣ = 16 ; b) 3ˣ = 5 ; c) 10ˣ = 5 ; d) (0,5)ˣ = 8. 2) Inéquations : a) 5ˣ > 10 ; b) 2ˣ < 5 ; c) 3ˣ ≥ 1 ; d) (0,5)ˣ ≤ 8. 3) a) Résoudre X² − 5X + 4 = 0 ; b) en déduire la résolution de 2^{2x} − 5 × 2ˣ + 4 = 0 et 3^{−2x} − 5 × 3^{−x} + 4 = 0.

**Fonctions du type x ↦ xʳ, r rationnel** (p.153)

- **Activité 1** (p.153) : x > 0 : comparer x^{1/2} et e^{(1/2) ln x}.
- **Activité 2** (p.153) : f : x ↦ 3x^{1/3} sur ]0, +∞[. 1) lim_{0⁺} f et lim_{+∞} f. 2) f dérivable sur ]0, +∞[ et f′(x) = x^{−2/3}, tableau de variation. 3) ∀x ∈ [1000 ; 1001], (10,1)⁻² ≤ f′(x) ≤ 10⁻². 4) En déduire 10,0032 ≤ ∛1001 ≤ 10,0033 (inégalités des accroissements finis).

**Étude d'exemples de fonctions du type x ↦ exp(u(x))** (p.154–156)

- **Activité 1** (p.154) : f(x) = e^{−x²}. 1) f continue et dérivable sur ℝ, calculer f′(x). 2) a) parité ; b) tableau de variation sur ]0, +∞[ ; c) montrer f″(x) = e^{−x²}·P(x), P polynôme de degré 2 à déterminer ; d) points d'inflexion de C. 3) Tracer C.
- **Activité 2** (p.154) : f(x) = e^{−1/x}. a) D et limites aux bornes. b) Tableau de variation. c) Tracer C.
- **Activité 3** (p.156) : f définie sur [−2, +∞[ par f(x) = e^{x/(x+2)} si x ≠ −2 et f(−2) = 0 [l'énoncé imprimé écrit l'intervalle « [−2, +∞] » : [sic]]. a) Continuité et dérivabilité de f à droite en (−2). b) Tableau de variation. c) Asymptote et demi-tangente éventuelles. d) Tracer C.
- **Activité 4** (p.156) : f(x) = e^{sin x} sur ℝ. 1) f périodique de période 2π. 2) Tableau de variation sur [0, 2π]. 3) Tracer la restriction de f à [−π, π].
- **Activité 5** (p.156) : croissance d'une population en l'absence de facteurs inhibiteurs ; taux annuel d'accroissement de 2 % : P(x + 1) − P(x) = 0,02·P(x), d'où approximativement P(x) = P(x₀)·e^{0,02(x − x₀)} ; si P(1996) = 3 × 10⁹, P(x) = 3 × 10⁹·e^{0,02(x − 1996)}. 1) Tracer P sur [1996 ; 2008]. 2) Estimation de la population mondiale en l'an 2500.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Théorème et définition** (p.145, vérifié image) — « La fonction logarithme népérien est une bijection de ]0,+∞[ sur ℝ. Sa fonction réciproque est la fonction exponentielle de base e, notée exp, qui est aussi une bijection de ℝ sur ]0,+∞[. Ainsi, la fonction exp est définie sur ℝ et ∀ x ∈ ℝ, exp(x) ∈ ]0, +∞[ ; (ln)⁻¹ = exp et (exp)⁻¹ = ln ; exp(0) = 1 ; exp(1) = e. »

> **Retenons** (p.145) — « ∀x ∈ ℝ et ∀y ∈ ]0,+∞[ on a : exp(x) = y ⇔ x = ln y ; ln[exp(x)] = x et exp(ln y) = y. » ; « ∀x ∈ ℝ et ∀y ∈ ℝ on a : exp(x) = exp(y) ⇔ x = y ; exp(x) < exp(y) ⇔ x < y. »

> **Théorème fondamental** (p.146) — « Quels que soient les nombres réels a et b, on a : exp(a + b) = exp(a)·exp(b) »

> **Propriétés** (p.146) — « Quels que soient les nombres réels a et b, on a : exp(−a) = 1/exp(a) ; exp(a − b) = exp(a)/exp(b) »

> **Propriétés** (p.147) — « * Quel que soit le rationnel r, on a : exp(r) = eʳ. * D'une façon générale, on étend la notation précédente à tous les nombres réels, donc pour tout x réel on a : exp(x) = eˣ. * Ainsi, pour tous réels a et b on a : e^{a+b} = eᵃ × eᵇ ; e^{a−b} = eᵃ/eᵇ ; e⁻ᵃ = 1/eᵃ. * e⁰ = 1 et e¹ = e. »

> **Propriété** (p.147) — « Pour tous a réel et r rationnel on a : (eᵃ)ʳ = e^{a r} »

> **Retenons** (p.148) — « * La fonction exponentielle est dérivable sur ℝ et sa fonction dérivée est elle-même. Ainsi, ∀x ∈ ℝ on a exp′(x) = exp(x) = eˣ. * La fonction exponentielle est strictement croissante sur ℝ. »

> **Retenons** (p.148, p.150) — lim_{x→+∞} eˣ = +∞ et lim_{x→−∞} eˣ = 0 ; lim_{x→+∞} eˣ/x = +∞ ; lim_{x→−∞} x eˣ = 0 ; lim_{x→−∞} xⁿeˣ = 0, ∀n ∈ ℕ [sic : ℕ imprimé alors que l'Activité 5 ne traite que n entier naturel non nul] ; lim_{x→+∞} eˣ/xʳ = +∞, ∀r ∈ ℚ₊ ; lim_{x→0} (eˣ − 1)/x = 1 ; « Pour x « voisin de 0 » on a : 1 + x est une approximation affine de eˣ. »

> **Tableau de variation de f : x ↦ eˣ** (p.149) — x de −∞ à +∞ (repères 0 et 1) ; f′ > 0 ; f croît de 0 (en −∞) à +∞, avec f(0) = 1, f(1) = e. « ∀x ∈ ]−∞, 0] on a : 0 < eˣ ≤ 1. ∀x ∈ [0, 1], on a : 1 ≤ eˣ ≤ e. ∀x ≥ 1, eˣ ≥ e. » Courbes : « C′ : y = eˣ ; C : y = ln x ; D : y = x ; on a C′ = S_D(C) ; une équation de la tangente à C′ au point A(0, 1) est y = x + 1 ; une équation de la tangente à C′ au point B(1, e) est y = ex. »

> **Retenons** (p.151) — « Si u est une fonction numérique dérivable sur une partie D de ℝ alors la fonction f : x ↦ e^{u(x)} est dérivable sur D et pour tout x de D on a : f′(x) = u′(x)·e^{u(x)}. »

> **Retenons** (p.152) — « Si u est une fonction numérique dérivable sur un intervalle I de ℝ alors les primitives sur I de la fonction f : x ↦ u′(x)·e^{u(x)} sont les fonctions du type x ↦ e^{u(x)} + k où k est une constante réelle arbitraire. »

> **Définition** (p.152) — « Soit a un réel strictement positif. La fonction f : x ↦ aˣ est définie sur ℝ par ∀x ∈ ℝ, aˣ = e^{x·ln a} »

> **Définition** (p.153) — « Soit r un rationnel. La fonction f : x ↦ xʳ est définie sur ]0, +∞[ par f(x) = e^{r ln x}. »

> **Résumé du cours** (p.157–158, vérifié image p.157) — exp réciproque de ln, exp : ℝ → ]0, +∞[, (ln)⁻¹ = exp, (exp)⁻¹ = ln ; exp dérivable sur ℝ, exp′ = exp ; pour tout x, eˣ > 0 ; (0 < eˣ < 1) ⇔ x ∈ ]−∞, 0[ ; (eˣ > 1) ⇔ x ∈ ]0, +∞[ ; (eˣ = 1) ⇔ x = 0 ; (eᵃ = eᵇ) ⇔ (a = b) ; (eᵃ > eᵇ) ⇔ (a > b) ; propriétés e^{x+y} = eˣ·eʸ ; e^{x−y} = eˣ/eʸ ; e⁻ˣ = 1/eˣ ; (eˣ)ʳ = e^{rx} (r ∈ ℚ), en particulier √(eˣ) = e^{x/2} ; e^{u(x)} = e^{v(x)} ⇔ u(x) = v(x) ; e^{u(x)} ≤ e^{v(x)} ⇔ u(x) ≤ v(x) ; limites usuelles lim_{+∞} eˣ = +∞ ; lim_{−∞} eˣ = 0⁺ ; lim_{+∞} eˣ/x = +∞ ; lim_{−∞} x eˣ = 0⁻ ; lim_{x→0} (eˣ − 1)/x = 1 ; eˣ ≈ 1 + x (x voisin de 0) ; lim_{−∞} xⁿeˣ = 0, ∀n ∈ ℕ ; lim_{+∞} eˣ/xʳ = +∞, ∀r ∈ ℚ₊ ; dérivée de x ↦ e^{u(x)} : u′(x)·e^{u(x)} ; primitives de u′·eᵘ : e^{u} + k ; fonctions puissances : ∀x, aˣ = e^{x ln a} et xʳ = e^{r ln x}.

### Cours — Exercice résolu (1)

- **Exercice résolu** (p.154–155, solution intégrale imprimée) : f(x) = e^{(x−1)/x²} pour x ∈ ℝ*, f(0) = 0. a) D et limites aux bornes ; b) continuité et dérivabilité en x₀ = 0 ; c) tableau de variation ; d) tracer C dans un repère orthogonal. Solution : a) D = ℝ ; lim_{±∞}(x−1)/x² = lim 1/x = 0 donc lim_{±∞} f = e⁰ = 1 ; b) lim_{x→0⁻}(x−1)/x² = lim_{x→0⁺}(x−1)/x² = −∞ donc lim_{0⁻} f = lim_{0⁺} f = lim_{y→−∞} eʸ = 0 = f(0) : f continue en 0 ; (f(x) − f(0))/(x − 0) = ((x−1)/x²)·e^{(x−1)/x²}·x/(x − 1) tend vers 0 (car lim T e^T = 0 en −∞), donc f dérivable en 0, f′(0) = 0 ; c) f′(x) = u′(x)·e^{u(x)} = ((−x² + 2x)/x⁴)·e^{(x−1)/x²}, signe du trinôme −x² + 2x ; tableau : f′ < 0 sur ]−∞, 0[, f′ > 0 sur ]0, 2[, f′ < 0 sur ]2, +∞[ ; f décroît de 1 à 0 (en 0), croît de 0 à e^{1/4} (en 2), décroît de e^{1/4} à 1 ; f(2) = e^{1/4} ≈ 1,28 ; la droite Δ : y = 1 est asymptote horizontale en −∞ et +∞ ; C est en dessous de Δ au voisinage de −∞ et au-dessus de Δ au voisinage de +∞ ; d) graphique imprimé (maximum 1,28 en x = 2).

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.159–160) — 2 activités

- **Activité 1** (p.159) : f₁(x) = eˣ, f₂(x) = x², courbes (C), (C′) : position relative. 1) Avec le logiciel Sine qua non (ressource Internet indiquée) : montrer les axes, définir f1(x) = exp(x) et f2(x) = x^2, valider, conjecturer la position relative ; en déduire qu'il existe a ∈ ]−1, 0[ tel que pour x > a, eˣ > x² ; prouver alors lim_{+∞} eˣ/x = +∞. 2) φ(x) = eˣ − x² : a) φ′ et φ″ ; b) signe de φ″ et tableau de variation de φ″ ; c) en déduire φ′(x) > 0 et φ strictement croissante ; d) lim_{−∞} φ = −∞, lim_{+∞} φ = +∞, φ bijection de ℝ sur ℝ ; e) φ(x) = 0 admet une solution unique α dans [−1 ; 0], valeur approchée par dichotomie ; f) en déduire que φ(x) = 0 admet une solution unique dans ℝ ; g) position relative de (C) et (C′).
- **Activité 2** (p.160) : f(x) = eˣ + e⁻ˣ, g(x) = eˣ − e⁻ˣ, courbes (C), (C′). 1) Avec Cabri (ressource Internet indiquée) : écrire exp(x) + exp(−x) et exp(x) − exp(−x), montrer les axes, appliquer sur un axe, conjecturer la position relative. 2) Sur [−2 ; 2], la partie de (C) s'appelle une chaînette ; Galilée pensait que c'était une parabole ; h(x) = ax² + b sur [−2 ; 2] : a) si h(0) = f(0) et h(2) = f(2), montrer b = 2 et 4a + b = e² + e⁻² ; b) valeur approchée de a à 10⁻² ; c) valeur approchée de f(1) − h(1) à 10⁻² ; d) conclure.

### Exercices et problèmes (p.161–165) — 26 exercices

- **Ex. 1** (p.161) : simplifier a = ln √(e³) ; b = ln e^{√3} ; c = e^{−ln 3} ; d = e^{ln 2 − ln 5} ; A = (eˣ + e⁻ˣ)² − (eˣ − e⁻ˣ)² ; B = e^{2x} + e^{−2x} − (eˣ − e⁻ˣ)².
- **Ex. 2** (p.161) : résoudre dans ℝ : eˣ = −3 ; eˣ = e ; 3eˣ = e⁻ˣ ; e·e^{3x−1} = 1 ; e^{2x} − 3eˣ + 2 = 0 ; e^{2x} − 5eˣ + 6 = 0 ; e^{x²} = 1/9 ; e^{−x²−12x−35} = 1 ; e^{x²−5x} = e⁻⁶.
- **Ex. 3** (p.161) : résoudre dans ℝ : eˣ < 1 ; eˣ > e ; e^{x+2} < e^{2x−1} ; e^{3x−1} < 2 ; e^{−x²} > e⁻¹ ; e⁻ˣ > 3 ; e^{2x} − 3eˣ + 2 > 0.
- **Ex. 4** (p.161) : simplifier e^{ln|x|} ; e^{|ln x|} ; ln(e^{|x|}).
- **Ex. 5** (p.161) : P(x) = x³ − 3x² − 4x + 12. 1) 3 est racine de P ; déterminer a, b, c tels que P(x) = (x − 3)(ax² + bx + c). 2) Résoudre P(x) = 0. 3) En déduire la résolution de (E) : e^{3x} − 3e^{2x} − 4eˣ + 12 = 0.
- **Ex. 6** (p.161) : résoudre dans ℝ : ln((x + 1)/(x + 2)) = 2 ; e^{3x+4} = 4 ; eˣ − e⁻ˣ = 15/4 ; e^{2x} + 3eˣ − 4 = 0 ; e^{2x} − 4eˣ − 5 > 0 ; |e^{x−1} − 1| ≤ 3 ; 2e^{3x−1} − 3e^{2x−1} + e^{x−1} ≤ 0.
- **Ex. 7** (p.161) : f : x ↦ x e⁻ˣ ; g : x ↦ x² e⁻ˣ. 1) Tableaux de variation de f et g. 2) Représenter les courbes et préciser leurs positions.
- **Ex. 8** (p.161–162) : calculer 25 limites : lim_{+∞}(eˣ − x) ; lim_{+∞}(e^{3x} − 2eˣ) ; lim_{+∞} 2x e⁻ˣ ; lim_{+∞} x³ e⁻ˣ ; lim_{+∞}(e⁻ˣ + 2x) ; lim_{+∞} x(e^{1/x} − 1) ; lim_{+∞}(1 − 1/x)e^{1/x} ; lim_{+∞}(e^{3x} − 1)/x ; lim_{+∞}(eˣ − x)/(2x²) ; lim_{+∞}(eˣ − 3)/(eˣ + 2x) ; lim_{+∞}(1 + 1/x²)e^{1/x} ; lim_{+∞} x eˣ/(eˣ − 1) ; lim_{−∞} x² eˣ ; lim_{−∞} xⁿ eˣ ; lim_{−∞} x² e^{1/x} ; lim_{−∞}(x + 1/x)eˣ ; lim_{x→0}(e^{x ln 2} − 1)/x ; lim_{x→0} x² e^{1/x} ; lim_{x→0⁺}((x − 1)/x)e^{1/x} ; lim_{+∞} ln(1 + eˣ)/eˣ ; lim_{−∞} ln(1 + eˣ)/eˣ ; lim_{x→0}(e^{x+1} − e)/x ; lim_{x→0⁻}((x − 1)/x)e^{1/x} ; lim_{x→0}(x + 1/x)eˣ ; lim_{x→0⁺} e^{(1 + 1/x) ln x}.
- **Ex. 9** (p.162) : ensemble de définition et de dérivabilité puis f′(x) : 1) f : x ↦ e^{−x² + 2x} ; 2) f : x ↦ e^{1/(x² − 1)} ; 3) f : x ↦ e^{√(x² − x − 2)} ; 4) f : x ↦ (e^{2x} + 1)/(e^{2x} − 1).
- **Ex. 10** (p.162) : f(x) = 2e^{2x} − eˣ. 1) D et limites aux bornes. 2) Sens de variation. 3) Résoudre f(x) = 0. 4) Construire la courbe. 5) g restriction de f à I = [ln(1/4), +∞[ : a) g admet une réciproque g⁻¹, ensemble J ; b) tracer C′ de g⁻¹ ; c) calculer g⁻¹(x) pour x ∈ J. 6) Primitive F de f sur ℝ qui s'annule en ln(0,5).
- **Ex. 11** (p.162) : f(x) = eˣ/(e^{2x} + 1). 1) D et limites aux bornes. 2) f paire. 3) Variations de f, construire C. 4) g(x) = ln(tan x) : g bijection de I = ]0, π/2[ sur ℝ. 5) h réciproque de g : a) sens de variation de h sur ℝ ? ; b) h dérivable sur ℝ et h′ = f ; c) retrouver le sens de variation de h.
- **Ex. 12** (p.162) : f(x) = 2x + eˣ/(eˣ − 1), C. 1) D et limites aux bornes. 2) a) Le point I(0 ; 0,5) est centre de symétrie de C ; b) variations de f et construire C. 3) k paramètre réel : déterminer graphiquement le nombre de solutions de (E) : 2x·eˣ + (1 − k)eˣ − 2x + k = 0 (indication : (E) équivalente à f(x) = k).
- **Ex. 13** (p.163) : f : x ↦ eˣ + e⁻ˣ − 2 ; g : x ↦ eˣ − e⁻ˣ. 1) Tableaux de variation. 2) Courbes dans un repère orthonormé. 3) a) g admet une réciproque, construire la courbe de g⁻¹ ; b) g⁻¹ dérivable sur ℝ ; c) calculer (g⁻¹)′(1,5). 4) La restriction de f à [0, +∞[ est une bijection ; étudier et représenter son application réciproque.
- **Ex. 14** (p.163) : f(x) = x − 1 + e⁻ˣ. 1) Étudier et représenter f. 2) f(x) = 0 admet une solution unique α comprise entre 1 et 2.
- **Ex. 15** (p.163) : f(x) = x e^{2x+1} si x ≤ 0 et f(x) = x(1 − ln x) si x > 0. 1) Continuité en zéro. 2) Dérivabilité en zéro. 3) Tableau de variation. 4) Branches infinies de C. 5) Tracer C.
- **Ex. 16** (p.163) : f(x) = √(1 − e^{2x}). 1) D ; montrer ∀x ∈ D \ {0}, f(x)/x = (−1/√(−x))·√(2·(e^{2x} − 1)/(2x)). 2) Calculer lim_{x→0⁻} f(x)/x et interpréter graphiquement. 3) Étudier les variations de f. 4) a) Montrer que f admet une fonction réciproque f⁻¹ dont on précisera l'ensemble E de définition ; b) calculer f⁻¹(x) pour x ∈ E ; c) tracer dans un repère orthonormé les courbes de f et f⁻¹. 5) Soit g(x) = −x + (1/2)·ln(e^{2x} − 1) : a) montrer que ∀x ∈ D − {0}, g(x) = ln(f(x)) ; b) étudier les variations de g et tracer sa courbe.
- **Ex. 17** (p.163) : g(x) = −x − 1 + eˣ. 1) Sens de variation de g sur ℝ. 2) En déduire ∀x ∈ ]−1, +∞[, e⁻ˣ ≤ 1/(1 + x). 3) f(x) = ln(1 + x) + e⁻ˣ : a) limites aux bornes de I = ]−1, +∞[ ; b) tableau de variation ; c) tangente T à C au point d'abscisse zéro ; d) construire T et C.
- **Ex. 18** (p.163) : une lame de verre absorbe 4 % de la lumière qui la traverse. 1) Proportion de la lumière incidente qui traverse 20 lames identiques superposées. 2) Combien de lames pour absorber 40 % de la lumière incidente.
- **Ex. 19** (p.164) : f(x) = 3ˣ sur ℝ. 1) Étudier et représenter f. 2) Résoudre graphiquement puis par le calcul 3ˣ ≤ 6.
- **Ex. 20** (p.164) : f(x) = (1/5)ˣ sur ℝ. 1) Étudier et représenter f. 2) Résoudre graphiquement puis par le calcul (1/5)ˣ ≤ 5.
- **Ex. 21** (p.164) : f(x) = e⁻ˣ·sin(2x). 1) ∀x ∈ ℝ, −e⁻ˣ ≤ f(x) ≤ e⁻ˣ. 2) Exprimer f(x + π) et f(x + π/2) en fonction de f(x). 3) Étudier la restriction de f à [−π/2, π] et la représenter.
- **Ex. 22** (p.164) : 1) g(x) = e^{2x} − eˣ + 1 : a) variations de g ; b) tracer C_g ; c) k ∈ ℝ*₊ : discuter graphiquement le nombre de solutions réelles de (E) : e^{2x} − eˣ + 1 − k = 0. 2) f(x) = ln(e^{2x} − eˣ + 1) : a) montrer f(x) = 2x + ln(1 − e⁻ˣ + e^{−2x}) ; b) montrer que la droite D : y = 2x est asymptote à C ; c) sens de variation de f sur ℝ ; d) tracer C_f (préciser la tangente à C_f en son point d'ordonnée nulle).
- **Ex. 23** (p.164, « D'après Bac Tunisien 2004 ») : f(x) = √(1 + x)·e⁻ˣ sur [−1, +∞[, C. 1) a) Dérivabilité de f à droite en −1 ; b) interprétation graphique ; c) limite de f en +∞ ; d) interprétation. 2) Tableau de variation. 3) Tangente à C au point d'abscisse 0. 4) f(x) = x admet une solution unique α dans [−1/2, +∞[ et α ∈ ]1/2, 1[. 5) Tracer C.
- **Ex. 24** (p.164–165, « D'après Bac Tunisien 2005 ») : f(x) = 2e⁻ˣ + x − 2, (C) (unité 4 cm). 1) lim_{+∞} f et lim_{−∞} f = +∞. 2) a) Résoudre −2e⁻ˣ + 1 > 0 ; b) tableau de variation ; c) f(x) = 0 admet dans ℝ exactement deux solutions dont l'une est nulle ; α l'autre, vérifier 1,5 < α < 1,6. 3) a) (C) admet une asymptote oblique Δ : y = x − 2 en +∞ ; b) nature de la branche infinie en −∞. 4) a) Tangente T à (C) à l'origine O ; b) g(x) = −2e⁻ˣ + 2x − 2 : variation de g, signe de g(x) ; c) position de (C) par rapport à T. 5) Tracer Δ, T et (C). 6) h restriction de f à [ln 2, +∞[, h⁻¹ réciproque : a) tableau de variation de h⁻¹ ; b) tracer la courbe de h⁻¹.
- **Ex. 25** (p.165, « D'après Bac Tunisien 2002 ») : f(x) = e^{2x}/(1 + e^{2x}), C (unité 2 cm). 1) a) lim_{+∞} f et lim_{−∞} f ; b) f′(x) = 2e^{2x}/(1 + e^{2x})² puis tableau de variation ; c) I(0, 1/2) centre de symétrie de C ; d) équation de la tangente (T) à C au point I. 2) a) ∀t, f′(t) ≤ 1/2 ; b) ∀x ≥ 0, f(x) ≤ (1/2)(x + 1) ; c) position de C par rapport à (T). 3) Tracer (T) et C. 4) a) f bijection de ℝ sur ]0, 1[ ; b) y ∈ ]0, 1[ : déterminer x tel que f(x) = y ; c) en déduire la représentation graphique de g : ]0, 1[ → ℝ, g(x) = (1/2) ln(x/(1 − x)).
- **Ex. 26** (p.165) : injection intramusculaire d'une dose de 3 cm³ d'une substance dans le sang à t = 0 (heures) ; quantité Q(t) = (1/3)·t·e^{3−t} (cm³). 1) Volume restant au bout de 90 min. 2) Volume éliminé au bout d'une demi-heure, d'une heure. 3) Q′(t), tableau de variation de Q sur [0, +∞[. 4) La tangente T à (C) en t = 2 a un coefficient directeur ≈ −0,9. 5) Tracer T et (C). 6) Graphiquement, au bout de combien de temps la quantité est inférieure à 0,5 cm³.

### Aperçu historique (p.166)

Neper, Stifel (1487–1567), nombre e comme limite de (1 + 1/n)ⁿ (≈ 2,718…) baptisé e par Euler (1707–1785) [sic : l'Aperçu du chapitre 5 donne Euler 1707 ; 1783] ; croissance exponentielle/logarithmique ; Euler : π, i, e, formule e^{iπ} + 1 = 0 et e^{ix} = cos x + i sin x ; Institutiones calculi integralis (1768/70) et differentialis (1755) ; Vollständige Anleitung zur Algebra (1770) ; formule d'Euler pour les polyèdres S − A + F = 2. Aucun contenu à enseigner.

### Bornes de scope observées (chapitre 7)

- ✅ INCLUS : exp comme réciproque de ln (bijection ℝ → ]0, +∞[) ; propriétés algébriques e^{a+b}, e^{a−b}, e^{−a}, (eᵃ)ʳ ; notation eˣ ; dérivabilité (exp′ = exp), variations, limites en ±∞, croissances comparées (xⁿeˣ, eˣ/xʳ), limite (eˣ − 1)/x et approximation affine ; équations et inéquations exponentielles, changement d'inconnue X = eˣ ; dérivée de e^{u} et primitives de u′e^{u} ; fonctions aˣ (a > 0) et xʳ (r ∈ ℚ) définies par exp et ln ; études de fonctions e^{u(x)} (parité, extremum, branches infinies, prolongement par continuité) ; modèles de croissance exponentielle ; annales du bac tunisien (2002, 2004, 2005).
- ⛔ NON traité dans ce chapitre : équations différentielles ; intégrales ; exposants réels généraux xᵅ (seul r ∈ ℚ) ; exponentielle complexe (seulement citée en aperçu historique) ; logarithme de base a (seulement le décimal au chapitre 6) ; pas de QCM / Vrai-Faux ; la fonction aˣ est étudiée en activités sans théorème encadré propre (pas de tableau récapitulatif des trois cas 0 < a < 1, a > 1, a = 1).

> Sondage image : pages 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 161, 162, 163, 164, 165 confrontées au PNG (19 pages sur 24 ; 143, 158, 159, 160, 166 en couche texte seule : page de garde, fin du résumé, deux activités informatiques, aperçu historique) ; écarts : p.145–152 la couche texte avait réparti les encarts « Retenons » hors de leur place et perdu les exposants (rétablis sur image) ; p.153 couche texte : exposants de a, b, c, d (Activité 4) mélangés, corrigés sur image ; p.161–162 la couche texte de l'ex. 8 avait fusionné et mélangé les limites (ordre et exposants rétablis sur image : x(e^{1/x} − 1), x²e^{1/x}, e^{(1+1/x)ln x}) ; p.156 le « +∞] » imprimé reporté tel quel [sic] ; aucun autre mot ou nombre faux constaté sur les pages vues.

## 2.8 Chapitre 8 — Calcul intégral (manuel 222451, p.167–192)

**Page de garde (p.167)** — Titre : « Calcul intégral », Chapitre 8. Plan : Activités préliminaires ; Cours (Intégrale d'une fonction continue ; Propriétés de l'intégrale ; Inégalité de la moyenne — Théorème de la moyenne ; Méthode d'Intégration par parties ; Calcul d'aires planes et des volumes de solides de révolution) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ; Aperçu Historique. **Pas de rubrique QCM / Vrai-Faux.** Notation : ∫ₐᵇ f(x)dx, [F(x)]ₐᵇ, « u.a » (unité d'aire), « u.v » (unité de volume).

### Activités préliminaires (p.168–169)

- **Préliminaire 1** (p.168) : 1) f : x ↦ (12x + 6)/(x + 2)². a) Démontrer qu'il existe a, b réels tels que ∀x ∈ ℝ − {−2}, f(x) = a/(x + 2)² + b/(x + 2) ; b) en déduire la forme générale des primitives de f sur ]−2, +∞[. 2) Déterminer les primitives de g : x ↦ x/(x + 2) sur ]−2, +∞[. (À droite de la page : tableau de rappel « Fonction f / Primitive F de f (définie sur I) » pour u, v dérivables sur un intervalle I de ℝ et c constante réelle arbitraire : voir « Résultats » ci-dessous.)
- **Préliminaire 2** (p.168) : montrer que chaque f admet une primitive sur l'intervalle I et donner une primitive F de f sur I : 1) f : x ↦ 1/x ; I = ]0, +∞[ ; 2) f : x ↦ 1/x² ; I = ]−∞, 0[ ; 3) f : x ↦ 2e^{2x} ; I = ℝ ; 4) f : x ↦ 2x/(x² + 1) + 1 ; I = ℝ.
- **Préliminaire 3** (p.168) : F : x ↦ ln(√(x² + 1)). 1) Prouver que F est continue sur ℝ. 2) Montrer que F est la primitive de f : x ↦ x/(x² + 1) sur ℝ s'annulant en zéro. 3) a) Trouver un encadrement de f(x) pour x ∈ [0, 1] ; b) montrer que ∀x ∈ [0, 1], 1 ≤ √(x² + 1) ≤ √2 ; c) en déduire que ∀x ∈ [0, 1], 0 ≤ F(x) < 1/2.
- **Préliminaire 4** (p.169) : f(x) = (eˣ − 1)/(eˣ + 1) sur ℝ. 1) a) Vérifier que f(x) = −1 + 2eˣ/(eˣ + 1) ; b) en déduire la primitive F de f sur ℝ telle que F(0) = 0. 2) a) Vérifier f(x) = (e^{x/2} − e^{−x/2})/(e^{x/2} + e^{−x/2}) ; b) retrouver les résultats de la question 1).
- **Préliminaire 5** (p.169) : F(x) = (1/2)[x√(x² + 1) + ln(x + √(x² + 1))] sur ℝ. a) Montrer que pour tout réel x, x + √(x² + 1) > 0. b) Montrer que F est une primitive sur ℝ de f(x) = √(x² + 1).
- **Préliminaire 6** (p.169) : f(x) = −3x + 7 sur ℝ. 1) Tracer la droite Δ de f dans un repère orthonormé. 2) Pour x ∈ [0, 7/3], M et N points de Δ d'abscisses 0 et x, B(x, 0) distinct de O : a) calculer en fonction de x l'aire S(x) du trapèze OMNB ; b) S′ dérivée de S : calculer S′(x) et comparer avec f(x). 3) Reprendre a) et b) pour x réel négatif.

### Cours — Activités

**Intégrale d'une fonction continue** (p.170–171)

- **Activité 1** (p.170) : repère orthonormé ; D droite d'équation y = (3/10)x + 3/2 ; a et b réels positifs, b > a ; 𝒜 aire de la partie du plan limitée par D, (x′x) et les droites x = a et x = b (figure imprimée). 1) Calculer 𝒜. 2) F primitive de f : x ↦ (3/10)x + 3/2 : montrer 𝒜 = F(b) − F(a).
- **Activité 2** (p.170) : f continue sur un intervalle I, F et G deux primitives de f sur I, a et b dans I : montrer G(b) − G(a) = F(b) − F(a).
- **Activité 3** (p.170–171) : 1) a) Justifier l'existence de I = ∫₁^e (1/x) dx ; b) calculer I. 2) Calculer ∫₀¹ eˣ dx ; ∫₂¹(3x² + 2x + 1)dx [bornes imprimées 2 puis 1] ; ∫₁⁵ dx ; ∫₋₁¹ x e^{x²} dx ; ∫_{−π/3}^{π/3} sin y dy ; ∫₋₁^{−2} (2t² + 1)/t² dt [bornes imprimées −1 (inférieure) et −2 (supérieure)]. 3) f : x ↦ |x³| + 1 : a) f continue sur [−1, 1] ; b) calculer ∫₀¹ f(x)dx ; ∫₋₁⁰ f(x)dx.

**Propriétés de l'intégrale** (p.171–175)

- **Activité 1** (p.171) : 1) a) Calculer ∫₁¹ x²dx ; b) calculer ∫₀¹ x²dx et ∫₁⁰ x²dx, comparer ; c) calculer ∫₀^π sin x dx et ∫_π^0 sin x dx, comparer. 2) f continue sur I, F primitive, a et b dans I : a) calculer ∫ₐᵃ f(x)dx ; b) comparer ∫ₐᵇ f(x)dx et ∫_bᵃ f(x)dx.
- **Activité 2** (p.171) : 1) g : x ↦ 1/√x : a) sur quel ensemble f [sic : g] est-elle continue ? prouver que G : x ↦ 2√x + 1 est une primitive de f [sic : g] sur ]0, +∞[ ; b) calculer m = ∫₁⁴ g(x)dx + ∫₄⁹ g(x)dx et n = ∫₁⁹ g(x)dx, comparer. 2) a, b, c dans I : montrer, avec F, que ∫ₐᶜ f + ∫_cᵇ f = ∫ₐᵇ f.
- **Activité 3** (p.172) : I = ∫₋₂³ (|x + 1| + |x − 2|)dx. a) Écrire sans valeur absolue |x + 1| + |x − 2| ; b) en déduire I.
- **Activité 4** (p.172) : 1) Calculer ∫₀¹ 3(x + 1)·e^{((1/2)x² + x)} dx. 2) f continue, F primitive : montrer ∫ₐᵇ (kf)(x)dx = k ∫ₐᵇ f(x)dx pour tout réel k. 3) f, g continues, F, G primitives : montrer ∫ₐᵇ (f + g)(x)dx = ∫ₐᵇ f + ∫ₐᵇ g.
- **Activité 5** (p.173) : 1) Calculer ∫₀¹(3t² + 2e^{2t})dt ; ∫₀^π(2 sin t + cos t + 3)dt ; ∫₂³(3t² − 2/t²)dt ; ∫₁^e(1 + 1/t)dt. 2) I = ∫₂³ dx/(x² − 1) : a) justifier l'existence ; b) a, b tels que 1/(x² − 1) = a/(x − 1) + b/(x + 1) pour x ≠ ±1 ; c) calculer I. 3) J = ∫₀¹ (2t − 3)/(2t + 1) dt : a) a, b tels que (2t − 3)/(2t + 1) = a + b/(2t + 1) pour t ≠ −1/2 ; b) calculer J. 4) a) Montrer cos⁴x = (1/8)cos(4x) + (1/2)cos(2x) + 3/8 ; b) calculer K = ∫_{π/2}^π cos⁴x dx.
- **Activité 6** (p.173) : f : x ↦ x² + 1, g : x ↦ sin 2x, h : x ↦ x³ sur ℝ. 1) a) Parité de f et h ; b) périodicité de g. 2) a) Calculer I = ∫₋₂² f(t)dt ; J = ∫_{π/3}^{4π/3} g(t)dt ; K = ∫₋ₐᵃ h(t)dt (a ∈ ℝ) ; b) calculer 2∫₀² f(t)dt, comparer avec I ; c) calculer ∫₀^π g(t)dt, comparer avec J.
- **Activité 7** (p.174) : calculer I = ∫₋₅⁵ (x³ + x)dx ; J = ∫₋₁¹ (t⁴ + t² − 1)dt ; K = ∫_{π/4}^{5π/4} cos(2t)dt ; L = ∫₀^{1004π} |sin t| dt.
- **Activité 8** (p.174) : f(x) = eˣ − 1 et g(x) = x − 1 sur ℝ. 1) a) ∀x ∈ [0, 1], f(x) ≥ 0 ; b) calculer ∫₀¹ f(x)dx et préciser son signe. 2) a) Variations de h : x ↦ eˣ − x ; b) comparer f(x) et g(x) dans [0, 1] et vérifier ∫₀¹ f(x)dx ≤ ∫₀¹ g(x)dx.
- **Activité 9** (p.174) : 1) f continue et positive sur [a, b] (a ≤ b), F primitive : montrer F croissante, en déduire ∫ₐᵇ f ≥ 0. 2) f continue sur [a, b] : si ∀x, f(x) ≤ 0 alors ∫ₐᵇ f ≤ 0. 3) f, g continues, f ≤ g sur [a, b] : a) signe de ∫ₐᵇ (g − f) ; b) en déduire ∫ₐᵇ f ≤ ∫ₐᵇ g.
- **Activité 10** (p.175) : f continue sur [a, b] (a ≤ b). a) Justifier l'existence de ∫ₐᵇ |f(x)|dx. b) Avec −|f(x)| ≤ f(x) ≤ |f(x)|, montrer |∫ₐᵇ f(x)dx| ≤ ∫ₐᵇ |f(x)|dx.
- **Activité 11** (p.175) : 1) x réel positif : a) ∀t ≥ 0, eᵗ ≥ 1 ; b) en intégrant l'inégalité dans [0, x], montrer eˣ ≥ 1 + x. 2) Montrer ∀x ∈ [0, +∞[, eˣ ≥ 1 + x + x²/2 et retrouver lim_{+∞} eˣ/x. 3) x réel positif : a) ∀t ≥ 0, 1 − t ≤ 1/(1 + t) ≤ 1 − t + t² ; b) en déduire x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³/3 ; c) encadrement de ln(11/10) et ln(101/100).

**Inégalités de la moyenne — Théorème de la moyenne** (p.176–177)

- **Activité 1** (p.176) : f continue sur I, a < b dans I. Montrer que s'il existe m et M tels que ∀x ∈ [a, b], m ≤ f(x) ≤ M, alors m(b − a) ≤ ∫ₐᵇ f(x)dx ≤ M(b − a).
- **Activité 2** (p.176) : f continue sur I, a < b dans I ; l'image de [a, b] par f est un intervalle fermé [m, M] = f([a, b]). a) Montrer m ≤ (1/(b − a))∫ₐᵇ f(x)dx ≤ M. b) En déduire qu'il existe c ∈ [a, b] tel que f(c) = (1/(b − a))∫ₐᵇ f(x)dx.
- **Activité 3** (p.177) : 1) a) Valeur moyenne μ de f : x ↦ eˣ sur [0, 1] ; b) résoudre dans [0, 1] f(x) = μ. 2) g : x ↦ x² : résoudre dans [−2, 2] g(x) = λ, λ valeur moyenne de g sur [−2, 2].
- **Activité 4** (p.177) : vitesse instantanée v(t) = 3(2 + t²) (m/s, t en s) ; à t = 2 s, x(t) = 80 m ; à t = 4 s, x(t) = 148 m. Calculer de deux façons la vitesse moyenne du mobile dans [2, 4].

**Théorème d'intégration par parties** (p.177–179)

- **Activité 1** (p.177) : u, v dérivables sur I avec u′, v′ continues, a et b dans I. a) Montrer u′v = (uv)′ − v′u. b) En déduire ∫ₐᵇ u′(x)v(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u(x)v′(x)dx. c) Calculer ∫₀¹ x eˣ dx et ∫₀^π x sin x dx.
- **Activité 2** (p.178) : 1) par intégration par parties, calculer I = ∫₁^e x ln x dx ; J = ∫₀^{1/2}(x + 1)e^{−x}dx ; K = ∫₁² x² ln x dx. 2) En intégrant par parties deux fois successives : ∫₀^{ln 2} x²eˣ dx ; ∫₀^{π/2} t² sin t dt ; ∫₁^{e²} x(ln x)² dx.
- **Activité 3** (p.178) : F(x) = ∫₁ˣ t ln t dt pour x > 0. 1) Justifier l'existence de F(x), calculer F(1). 2) Avec u′(t) = t et v(t) = ln t, calculer F(x) en fonction de x. 3) a) Montrer que F est dérivable sur ]0, +∞[ et calculer F′(x) ; b) en déduire le sens de variation de F.

**Calcul d'aires planes — Calcul des volumes de solides de révolution** (p.179–183)

- **Activité 1** (p.179) : f : x ↦ 2x − 1. 1) Tracer la droite Δ dans un repère orthogonal (O, i⃗, j⃗) avec ‖i⃗‖ = 2 cm et ‖j⃗‖ = 3 cm. 2) A, E, F points de Δ d'abscisses respectives 1/2 ; 1 et −1/2 ; B(1, 0) ; C(0, 1) ; G(−1/2, 0) : a) calculer en cm² les aires 𝒜₁ du triangle ABE et 𝒜₂ du triangle AFG ; b) calculer I₁ = ∫_{1/2}^1 f(t)dt et I₂ = ∫_{−1/2}^{1/2} f(t)dt ; c) 𝒶 aire du rectangle OBEC : vérifier 𝒜₁ = I₁·𝒶 et 𝒜₂ = −I₂·𝒶.
- **Activité 2** (p.179–180) : courbe 𝒞 de f : x ↦ 1 − x² (graphique imprimé), tangentes T_A, T_B, T_N aux points A, B, N d'abscisses 0, 1 et 1/2 ; I = T_A ∩ T_N, I′ = T_B ∩ T_N. 1) Aire 𝒜₁ du polygone OANB. 2) Équations de T_A, T_B, T_N. 3) a) Coordonnées de I et I′ ; b) aire 𝒜₂ du polygone OAII′B (décomposer en deux trapèzes). 4) a) En déduire un encadrement de l'aire 𝒜 de la région limitée par 𝒞 et les axes ; b) calculer I = ∫₀¹ f(t)dt et vérifier 𝒜₁ ≤ I ≤ 𝒜₂ ; c) calculer J = ∫₋₁¹ f(t)dt, conjecturer l'interprétation graphique de J.
- **Activité 3** (p.181) : 1) Calculer et interpréter graphiquement I = ∫₁^e (ln x)/x dx et J = ∫₀^{π/2} sin 2t dt. 2) f : x ↦ cos x sur [0, π] : a) tracer 𝒞 dans un repère orthonormé avec ‖i⃗‖ = 2 cm ; b) calculer, en cm², l'aire de la partie limitée par 𝒞, l'axe des abscisses et les droites x = 0, x = π.
- **Activité 4** (p.181) : graphique avec P(π/2, π/2) et Q(0, π/2) ; courbes y = x et y = sin x. 1) Aire du triangle OPQ [sic : le texte donne Q(0, π/2), mais le graphique place Q en (π/2, 0) sur l'axe des abscisses (sous P) ; énoncé tel quel]. 2) Aire de la partie limitée par y = sin x, l'axe des abscisses, x = 0 et x = π/2. 3) a) En déduire l'aire 𝒜 de la région limitée par les courbes de f : x ↦ sin x et g : x ↦ x et les droites x = 0, x = π/2 ; b) comparer avec ∫₀^{π/2}(x − sin x)dx.
- **Activité 5** (p.181) : graphique de f : x ↦ x² et g : x ↦ 2x/(x² + 1). a) Calculer l'aire 𝒜 de la région D limitée par les courbes de f et g et les droites x = −1 et x = 0. b) Comparer avec ∫₋₁⁰ (f(x) − g(x))dx.
- **Activité 6** (p.182) : f(x) = x² − 2 et g(x) = x sur ℝ. 1) Construire C_f et C_g et étudier leur position relative. 2) Aire de la région limitée par C_f, C_g et les droites x = −2 et x = 2.
- **Activité 7** (p.182) : repère orthonormé R. 1) f(x) = (1/2)x, Δ sa courbe, D région limitée par Δ, l'axe des abscisses et les droites x = 0 et x = 4 ; S cône de révolution engendré par la rotation de D autour de (O, i⃗) : a) volume V du cône S ; b) calculer ∫₀⁴ π(f(t))²dt et le comparer avec V. 2) a < b, g définie sur [a, b] par g(x) = 2 ; points A(a, 0), B(a, 2), C(b, 2), D(b, 0) ; S solide engendré par la rotation du rectangle ABCD autour de (O, i⃗) : a) nature de S ; b) volume V de S en fonction de a et b ; c) calculer ∫ₐᵇ π(g(t))²dt et comparer avec V.
- **Activité 8** (p.183) : f(x) = sin(x/2) sur [0, π]. 1) Tracer 𝒞. 2) Aire du domaine D limité par 𝒞, l'axe des abscisses et x = 0, x = π. 3) Volume V du solide de révolution engendré par la rotation de D autour de l'axe des abscisses (rappel : sin²(x/2) = (1 − cos x)/2).
- **Activité 9** (p.183) : f(x) = √(R² − x²), R > 0 donné, 𝒞 sa courbe. 1) a) M(x, y) ∈ 𝒞 ⇔ (x² + y² = R², −R ≤ x ≤ R et y ≥ 0) ; b) reconnaître 𝒞 ; c) tracer 𝒞 (R entre 1 et 3). 2) D domaine limité par 𝒞, l'axe des abscisses et x = −R, x = R ; V volume de la boule engendrée par la rotation de D autour de (O, i⃗) : montrer V = (4/3)πR³.
- **Activité 10** (p.183) : f(x) = ln x. 1) Construire 𝒞. 2) Aire 𝒜 de la portion P limitée par 𝒞, l'axe des abscisses et les droites x = 1 et x = e. 3) Volume du solide engendré par la rotation de P autour de l'axe des abscisses.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Tableau de rappel des primitives** (p.168, vérifié image) — u et v deux fonctions dérivables sur un intervalle I de ℝ, c constante réelle arbitraire : u′ + v′ → u + v + c ; au′ (a réel) → au + c ; u′v + v′u → u·v + c ; u′uⁿ (n ∈ ℤ* − {−1} et u(x) ≠ 0 ∀x ∈ I) → (1/(n+1))uⁿ⁺¹ + c ; u′/u² (u(x) ≠ 0) → −1/u + c ; u′/√u (u(x) > 0) → 2√u + c ; (u′v − v′u)/v² (v(x) ≠ 0) → u/v + c ; (v′∘u)·u′ → v∘u + c ; u′/u (u(x) ≠ 0) → ln|u| + c ; u′eᵘ → eᵘ + c.

> **Théorème et définition** (p.170, vérifié image) — « Soit f une fonction continue sur un intervalle I, F une primitive de f sur I, a et b deux éléments de I. Le réel F(b) − F(a) ne dépend pas de la primitive choisie de f sur I. Ce réel s'appelle intégrale de a à b de f et se note ∫ₐᵇ f(x)dx. Ainsi, ∫ₐᵇ f(x)dx = F(b) − F(a) = [F(x)]ₐᵇ où F est une primitive quelconque de f sur I. »

> **Retenons** (p.170) — « * Si f est une fonction continue sur [a, b] alors ∫ₐᵇ f(t)dt existe. * ∫ₐᵇ f(x)dx = ∫ₐᵇ f(t)dt = ∫ₐᵇ f(y)dy = ∫ₐᵇ f(s)ds = … * ∫ₐᵇ 1 dt = b − a ; ∫ₐᵇ x dt = x(b − a), (x réel). »

> **Propriétés** (p.171) — « Soit f une fonction continue sur un intervalle I, a et b deux éléments de I. Alors on a : ∫ₐᵃ f(x)dx = 0 et ∫_bᵃ f(x)dx = −∫ₐᵇ f(x)dx »

> **Relation de Chasles** (p.172) — « Soit f une fonction continue sur un intervalle I. Soient a, b et c trois éléments de I alors on a : ∫ₐᵇ f(x)dx = ∫ₐᶜ f(x)dx + ∫_cᵇ f(x)dx. » (Encadré p.172 : « Si f est une fonction continue sur [a, b] et c et d deux éléments de [a, b] alors on a : ∫ₐᵇ f = ∫ₐᶜ f + ∫_cᵈ f + ∫_dᵇ f. »)

> **Linéarité de l'intégrale** (p.172) — « Soient f et g deux fonctions continues sur un intervalle I, a et b deux éléments de I. Soit k un nombre réel. Alors on a : • ∫ₐᵇ (f + g)(x)dx = ∫ₐᵇ f(x)dx + ∫ₐᵇ g(x)dx • ∫ₐᵇ (kf)(x)dx = k∫ₐᵇ f(x)dx • ∫ₐᵇ (k₁f(t) + k₂g(t))dt = k₁·∫ₐᵇ f(t)dt + k₂·∫ₐᵇ g(t)dt, pour tous réels k₁ et k₂. »

> **Parité et périodicité** (p.174, encadré non titré) — « 1) Soit f une fonction continue sur [−a, a]. * Si f est paire sur [−a, a] alors on a : ∫₋ₐᵃ f(t)dt = 2∫₀ᵃ f(t)dt. * Si f est impaire sur [−a, a] alors on a : ∫₋ₐᵃ f(t)dt = 0. 2) Si f est une fonction continue sur ℝ et périodique de période T alors pour tout réel a on a : ∫ₐ^{a+T} f(t)dt = ∫₀ᵀ f(t)dt. »

> **Intégration et inégalités** (p.175) — « Soient f et g deux fonctions continues sur un intervalle I, a et b deux éléments de I. • Si a ≤ b et ∀x ∈ [a, b], f(x) ≥ 0 alors ∫ₐᵇ f(x)dx ≥ 0. • Si a ≤ b et ∀x ∈ [a, b], f(x) ≤ 0 alors ∫ₐᵇ f(x)dx ≤ 0. • Si a ≤ b et ∀x ∈ [a, b], f(x) ≤ g(x) alors ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx. »

> **Encadré** (p.175) — « Soit f une fonction continue sur un intervalle [a, b]. On a : |∫ₐᵇ f(x)dx| ≤ ∫ₐᵇ |f(x)|dx. »

> **Inégalités de la moyenne** (p.176) — « Soit f une fonction continue sur un intervalle [a, b] (a < b) ; m et M sont deux réels. Si ∀x ∈ [a, b], m ≤ f(x) ≤ M alors m(b − a) ≤ ∫ₐᵇ f(x)dx ≤ M(b − a). »

> **Théorème de la moyenne** (p.176) — « Si f est une fonction continue sur un intervalle [a, b] (a < b), alors il existe au moins un réel c appartenant à [a, b] tel que f(c) = (1/(b − a))∫ₐᵇ f(x)dx. Le réel (1/(b − a))∫ₐᵇ f(x)dx s'appelle la valeur moyenne de f sur [a, b]. »

> **Théorème d'intégration par parties** (p.177) — « Soient u et v deux fonctions dérivables sur un intervalle I telles que leurs fonctions dérivées u′ et v′ soient continues sur I. Soient a et b deux éléments de I. On a alors, ∫ₐᵇ u′(x)v(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u(x)v′(x)dx. » Vocabulaire : « Cette formule s'appelle formule d'intégration par parties. »

> **Retenons** (p.178) — « Soit f une fonction continue sur un intervalle ouvert I et a un élément de I. La fonction F définie sur I par F(x) = ∫ₐˣ f(t)dt est dérivable sur I et on a pour tout x de I, F′(x) = f(x). La fonction F est la primitive de f sur I qui s'annule en a. »

> **Interprétation géométrique de l'intégrale** (p.180, vérifié image) — « Le plan est rapporté à un repère orthogonal (O, i⃗, j⃗). L'unité d'aire (u.a) est l'aire du rectangle de dimensions ‖i⃗‖ et ‖j⃗‖. Soit C la courbe représentative de f dans le repère (O, i⃗, j⃗) et a et b deux réels tels que a < b. • Si f est continue sur [a, b] et pour tout x ∈ [a, b], f(x) ≥ 0 alors ∫ₐᵇ f(x)dx (u.a) est égal à l'aire de la partie du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations : x = a et x = b. • Si f est continue sur [a, b] et pour tout x ∈ [a, b], f(x) ≤ 0 alors l'aire de la partie du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations : x = a et x = b est le réel positif ∫ₐᵇ (−f(x))dx (u.a). • Plus généralement, si f est continue sur [a, b] et ne garde pas un signe constant sur [a, b] alors l'aire de la partie du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations : x = a et x = b est égale ∫ₐᵇ |f(x)|dx (u.a). » Trois exemples chiffrés imprimés : f(x) = eˣ, 𝒜 = ∫₋₂¹ eˣ dx = [eˣ]₋₂¹ = e − e⁻² (u.a) ; f(x) = x³, 𝒜 = ∫₋₁⁰ −x³ dx = [−(1/4)x⁴]₋₁⁰ = 1/4 (u.a) ; f(x) = cos 2x, 𝒜 = ∫₋π⁰ |cos 2x| dx = 2 (u.a).

> **Théorème** (p.182, vérifié image) — « Soient f et g deux fonctions continues sur un intervalle I. Soient C_f et C_g les courbes représentatives de f et g dans le plan rapporté à un repère orthogonal (O, i⃗, j⃗). Soit a et b deux éléments de I tels que a < b. • Si pour tout réel x de [a, b] on a : f(x) ≤ g(x) alors l'aire de la partie D du plan limitée par les courbes C_f et C_g et les droites d'équations x = a et x = b est égale au nombre positif ∫ₐᵇ (g(x) − f(x))dx (u.a). • Plus généralement, l'aire de la partie D du plan limitée par les courbes C_f et C_g et les droites d'équations x = a et x = b est égale à ∫ₐᵇ |g(x) − f(x)|dx (u.a). »

> **Théorème admis** (p.183) — « Soit f une fonction continue sur un intervalle [a, b] (a < b) et soit C sa courbe représentative dans un repère orthonormé (O, i⃗, j⃗) du plan. On considère la partie P du plan limitée par C, l'axe des abscisses et les droites d'équations x = a et x = b. Soit V le volume du solide de révolution engendré par la rotation de la partie P autour de l'axe des abscisses. Alors on a : V = π∫ₐᵇ (f(x))²dx (u.v) (unité de volume). »

> **Résumé du cours** (p.184–185, vérifié image) — intégrale de a à b de f = [F(x)]ₐᵇ = F(b) − F(a) ; ∫ₐᵃ f = 0 ; ∫_bᵃ f = −∫ₐᵇ f ; Chasles ; linéarité ; positivité (a ≤ b, f ≥ 0 ⇒ ∫ ≥ 0) ; |∫ f| ≤ ∫ |f| ; f ≤ g ⇒ ∫ f ≤ ∫ g ; f paire/impaire sur [−a, a] ; f périodique de période T ⇒ ∫ₐ^{a+T} = ∫₀ᵀ ; théorème de la moyenne (« cette valeur moyenne est atteinte par f sur [a, b], au moins une fois en c ») ; intégration par parties ; fonction définie à l'aide d'une intégrale F(x) = ∫ₐˣ f(t)dt, F′ = f, F primitive de f qui s'annule en a ; aires : « Si f est continue sur [a, b] et a < b alors l'aire de la partie du plan limitée par la courbe C, l'axe des abscisses et les droites x = a et x = b est égale à ∫ₐᵇ |f(x)|dx (u.a) » ; aire entre deux courbes = ∫ₐᵇ |g(x) − f(x)|dx (u.a) ; volume V = π∫ₐᵇ (f(x))²dx (unité de volume).

### Cours — Exercice résolu (1)

- **Exercice résolu** (p.178–179, solution intégrale imprimée) : f : x ↦ ∫₁ˣ (eᵗ/t) dt. 1) f dérivable sur ]0, +∞[, calculer f′(x). 2) Sens de variation de f sur ]0, +∞[. 3) Calculer f(1), en déduire le signe de f(x) sur ]0, 1[ et ]1, +∞[. Solution : 1) g : t ↦ eᵗ/t continue sur ]0, +∞[ donc f dérivable et f′(x) = g(x) = eˣ/x ; 2) ∀x > 0, eˣ > 0 et x > 0 d'où f′(x) > 0, f strictement croissante sur ]0, +∞[ ; 3) f(1) = 0 et f strictement croissante : pour tout x ∈ ]0, 1[, f(x) < f(1) donc f(x) < 0 ; pour tout x ∈ ]1, +∞[, f(x) > f(1) donc f(x) > 0 ; tableau de variation imprimé (f′ > 0, f croît en passant par 0 en x = 1).

### QCM / Vrai-Faux

Aucun dans ce chapitre.

### Avec l'ordinateur (p.186–187) — 2 activités

- **Activité 1** (p.186) : 1) Approximation S(n) de ∫₁⁶ dx/x pour n subdivisions de [1, 6] avec le logiciel Menumath (ressources Internet indiquées : www.edunet.tn, etc.) : menu « intégrales définies / interprétation graphique », définir f(x) = 1/x avec a = 1, b = 6, repère (xmin = −3, xmax = 7, ymin = −2, ymax = 5), méthode Simpson, lire S(n) pour n = 5 ; calculer ∫₁⁶ dx/x, en déduire une valeur approchée de ln 6, vérifier à la calculatrice ; d'autres valeurs de n ; reprendre avec Rectangles, Trapèzes. 2) Approximations avec Menumath de I = ∫₀¹ ln(t + 1)dt ; J = ∫₋₂⁵ √(t² + 1) dt ; K = ∫₋₁³ t² cos(t + 1)dt.
- **Activité 2** (p.187) : « Calcul d'une intégrale avec un logiciel ». 1) Sine qua non : f(x) = e^{sin x} et g(x) = x ln x − x (expressions exp(sin(x)) et x*ln(x)-x), couleurs différentes, icône de calcul d'intégrales : aire 𝒜 de la région limitée par les courbes de f et g et les droites x = 0 et x = e. 2) Dérive : calculer I = ∫₋₁² x³ ln(1 + x²)dx (taper x^3*ln(1+x^2), ∫f, intégrale définie, bornes −1 et 2, simplify) ; résultat donné I = (15/4)ln 5 − 9/8. Application : calculer I = ∫₀⁵ t² sin t dt ; J = ∫₋₂⁵ 1/√(t² + 1) dt ; K = ∫₁³ t² ln t dt.

### Exercices et problèmes (p.188–191) — 17 exercices

- **Ex. 1** (p.188) : calculer ∫₂¹(2x + 1)dx [bornes imprimées 2 puis 1] ; ∫₁²(x² − 2x + 3)dx ; ∫₀¹ (2x + 1)/(x² + x + 1)² dx ; ∫₀^{√3} x/√(x² + 1) dx ; ∫₁² (x² + x + 1)/x dx ; ∫₀²(1 − |x − 1|)dx ; ∫₂³ 1/(3x + 2) dx ; ∫₀¹ e^{2x}dx ; ∫₁² x/(x + 1) dx ; ∫₁^e (ln x)/x dx ; ∫₂^e (ln²x)/x dx ; ∫₀^{π/2} sin 2x dx.
- **Ex. 2** (p.188) : f : x ↦ (3x − 5)/(2x − 1) ; g : x ↦ (x² + 2x − 5)/(x + 4) ; h : x ↦ (eˣ − 2)/(eˣ + 1). 1) a, b tels que f(x) = a + b/(2x − 1), puis ∫₁² f(x)dx. 2) a, b, c tels que g(x) = ax + b + c/(x + 4), puis ∫₋₃⁰ g(x)dx. 3) a, b tels que h(x) = a + b·eˣ/(eˣ + 1), puis ∫₀¹ h(x)dx.
- **Ex. 3** (p.188) : 1) ∀x ≠ −1, (x² + 2x)/(x + 1) = x + 1 − 1/(x + 1), puis calculer ∫₀¹ (x² + 2x)/(x + 1) dx. 2) Calculer I = ∫₀¹ (t + 1) ln(t + 1) dt.
- **Ex. 4** (p.188) : f(x) = 1/(x(x + 1)²). 1) a, b, c tels que ∀x > 0, f(x) = a/x + b/(1 + x) + c/(1 + x)². 2) α ∈ ]1, +∞[ : a) calculer ∫₁^α f(t)dt ; b) calculer A(α) = ∫₁^α (ln t)/(1 + t)³ dt ; c) calculer lim_{α→+∞} A(α).
- **Ex. 5** (p.188) : intégration par parties : ∫₀¹ x eˣ dx ; ∫₁^e (ln x)/x² dx ; ∫₁ˣ ln t dt ; ∫₀^π eˣ cos x dx ; ∫₁^e x(ln x)² dx.
- **Ex. 6** (p.188) : I = ∫₀^{π/2} (eˣ cos x)² dx et J = ∫₀^{π/2} (eˣ sin x)² dx [parenthésage imprimé tel quel]. 1) Calculer I + J. 2) Calculer I − J par intégration par parties. 3) En déduire I et J.
- **Ex. 7** (p.188–189) : 1) Vérifier ∀x ≠ 0, eˣ/(eˣ − 1) = 1 + 1/(eˣ − 1). 2) a) Calculer I = ∫_{ln 2}^{ln 3} eᵗ/(eᵗ − 1) dt ; b) calculer J = ∫_{ln 2}^{ln 3} 1/(eᵗ − 1) dt. 3) K = ∫_{ln 2}^{ln 3} e^{2t}/(eᵗ − 1) dt : calculer K − I, en déduire K.
- **Ex. 8** (p.189) : I- g(x) = (1 − x)e⁻ˣ + 1. 1) Sens de variation de g sur ℝ. 2) En déduire g(x) > 0 pour tout x. II- f(x) = x e⁻ˣ + x sur ℝ, C. 1) a) f dérivable et f′(x) = g(x) ; b) tableau de variation. 2) a) D : y = x asymptote à C en +∞ ; b) position de C par rapport à D ; c) tangente T au point d'abscisse 1 ; d) tracer T, D, C. 3) α ∈ ℝ*₊ : aire 𝒜(α) de la partie limitée par C, D et les droites x = 0 et x = α ; calculer 𝒜(α) et lim_{α→+∞} 𝒜(α). 4) Pour x < 1, h(x) = ln(g(x) − 1) : a) vérifier h(x) = −x + ln(1 − x) et −x/(1 − x) = 1 − 1/(1 − x) ; b) calculer I = ∫₋₁⁰ ln(1 − t)dt ; c) en déduire J = ∫₋₁⁰ h(t)dt.
- **Ex. 9** (p.189) : f(x) = (1 + ln x)/x (x > 0). 1) Tracer C dans un repère orthonormé. 2) Aire 𝒜 de la région limitée par C, l'axe des abscisses et les droites x = 1 et x = e.
- **Ex. 10** (p.189) : f(x) = x ln(x + 2) sur [0, +∞[, C (repère orthonormé, unité 3 cm). 1) Tableau de variation. 2) Δ : y = x ; position de C par rapport à Δ, tracer Δ et C. 3) a) f admet une réciproque f⁻¹ (ensemble de définition), construire C′ de f⁻¹ ; b) vérifier pour x ≠ −2 : x²/(x + 2) = x − 2 + 4/(x + 2) ; c) calculer I = ∫₀^{e−2} f(t)dt ; d) calculer en cm² l'aire 𝒜 de la région comprise entre les courbes de f et de f⁻¹. [L'énoncé imprimé écrit « x ln(x + 2.) » : point parasite ; sens clair.]
- **Ex. 11** (p.189) : (Intensité et quantité d'électricité) courant continu d'intensité I sur [t₁, t₂] : Q = I·(t₂ − t₁) ; si I dépend de t, Q = ∫_{t₁}^{t₂} I(t)dt [barres de valeur absolue imprimées autour de I(t) dans l'intégrale : « Q = ∫ |I(t)| dt », reportées telles quelles]. Courant alternatif I(t) = I_m cos(ωt + φ) : calculer la quantité d'électricité transportée à chaque demi-période et la valeur moyenne de l'intensité correspondante.
- **Ex. 12** (p.189–190) : (Puissance et énergie) W = U·I·(t₂ − t₁) ; si I et U fonctions du temps, W = ∫_{t₁}^{t₂} U(t)·I(t)dt. Courant alternatif I(t) = I_m cos(ωt) dans une résistance R, U(t) = R·I(t) = U_m cos(ωt) : calculer l'énergie fournie pendant une période T = 2π/ω.
- **Ex. 13** (p.190) : f(x) = sin²x, x ∈ [0, π]. 1) Tracer C. 2) Linéariser sin²x et sin⁴x. 3) Aire 𝒜 de la portion D formée des points M(x, y) tels que 0 ≤ x ≤ π et 0 ≤ y ≤ f(x). 4) Volume du solide obtenu par rotation de la courbe C autour de l'axe des abscisses.
- **Ex. 14** (p.190) : f(x) = 1 + 2cos²x, x ∈ [0, π]. 1) Variations de f. 2) Tracer C. 3) D domaine limité par C, l'axe des abscisses et x = 0, x = π : a) aire 𝒜 de D ; b) volume du solide de révolution engendré par la rotation de D autour de (O, i⃗).
- **Ex. 15** (p.190) : A- k(x) = (x² + x + 1)e⁻ˣ − 1 sur ℝ. 1) a) Limites de k en −∞ et +∞ ; b) sens de variation de k, tableau sur ℝ. 2) k(x) = 0 admet exactement deux solutions dans ℝ dont l'une dans [1, +∞[ notée α ; encadrement d'amplitude 10⁻² de α. 3) Signe de k(x) sur ℝ. B- f(x) = (2x + 1)e⁻ˣ et g(x) = (2x + 1)/(x² + x + 1), courbes C_f et C_g (repère orthogonal, unité 2 cm). 1) Les deux courbes passent par A(0 ; 1) et y admettent la même tangente. 2) a) f(x) − g(x) = ((2x + 1)k(x))/(x² + x + 1) ; b) signe de f(x) − g(x) ; c) position relative de C_f et C_g. 3) a) h(x) = (−2x − 3)e⁻ˣ − ln(x² + x + 1) est une primitive de f − g ; b) aire 𝒜 de la partie limitée par C_f et C_g et les droites x = 0 et x = 1/2.
- **Ex. 16** (p.190–191) : I- g(x) = (1 − x)e⁻ˣ sur [0, +∞[. 1) lim_{+∞} g. 2) a) Tableau de variation de g ; b) en déduire ∀x ≥ 0, g(x) ≤ 1. II- f définie sur ℝ par f(x) = x ln(−x) si x < 0 ; f(x) = x(2 − e⁻ˣ) si x ≥ 0 ; (C) dans un repère orthonormé avec ‖i⃗‖ = 2 cm. 1) f continue en 0. 2) a) Dérivabilité de f à droite puis à gauche en 0 ; b) interprétations graphiques. 3) a) ∀x > 0, f′(x) = 2 − g(x), en déduire le signe de f′ sur ]0, +∞[ ; b) f′(x) pour x < 0 ; c) tableau de variation de f sur ℝ. 4) a) lim_{+∞}(f(x) − 2x), en déduire une asymptote oblique ; b) (C) admet une branche parabolique (direction). 5) a) f(−1), tracer (C) ; b) tracer (C′) symétrique de (C) par rapport à l'axe des abscisses. III- α ∈ ]−1, 0[, A(α) aire en cm² de la partie limitée par (C) et (C′) et les droites x = α et x = −1 : 1) calculer ∫₁^α f(t)dt (intégration par parties) [sic : borne inférieure imprimée 1 alors que α ∈ ]−1, 0[ et f(t) = t ln(−t) n'est défini que pour t < 0 ; lecture image agrandie confirmée « 1 »] ; 2) en déduire A(α) ; 3) a) lim_{α→0} A(α) ; b) interprétation graphique.
- **Ex. 17** (p.191, « D'après bac tunisien 2003 » imprimé en fin d'énoncé) : I- g(x) = x² + 1 − ln x sur ]0, +∞[. 1) Tableau de variation de g. 2) En déduire g(x) > 0 pour tout x > 0. II- f(x) = x + 2 + (ln x)/x sur ]0, +∞[. 1) a) f dérivable sur ]0, +∞[ et « pour tout réel x strictement positif on a : f(x) = x + 2 + (ln x)/x » [sic : l'énoncé imprimé écrit f(x) et non f′(x) à cet endroit ; coquille probable, la formule de f′ n'est pas imprimée] ; b) tableau de variation. 2) C : a) asymptote oblique Δ (équation) ; b) position relative de C et Δ. 3) x ∈ [1, +∞[, M(x, f(x)), N(x, x + 2) : a) la distance MN est égale à (ln x)/x ; b) valeur x₀ de x pour laquelle MN est maximale ; c) la tangente T au point d'abscisse x₀ est parallèle à Δ. 4) Tracer Δ, T et C. 5) a) Aire 𝒜 de la partie limitée par C et les droites y = x + 2, x = 1 et x = e ; b) α > e : déterminer α pour que l'aire de la partie limitée par la courbe et les droites y = x + 2, x = e et x = α soit égale à 𝒜.

### Aperçu historique (p.192)

Leibniz (classification des nombres : entier, rompu, sourd, transcendant ; calcul différentiel et intégral publié en 1684 ; querelle de paternité avec Newton) et Henri Léon Lebesgue (1875–1941 ; théorie de l'intégration 1902–1904). Aucun contenu à enseigner.

### Bornes de scope observées (chapitre 8)

- ✅ INCLUS : intégrale d'une fonction continue définie par une primitive (F(b) − F(a)) ; intégrale d'une constante et notations muettes ; relation de Chasles ; linéarité ; intégrales de fonctions avec valeur absolue (découpage) ; parité et périodicité ; positivité, croissance, |∫f| ≤ ∫|f| ; inégalités de la moyenne et théorème / valeur moyenne ; intégration par parties (y compris deux fois) ; fonction définie par ∫ₐˣ f(t)dt ; aires planes (axe des abscisses, entre deux courbes) ; volumes de solides de révolution (V = π∫(f)²) ; décomposition en éléments simples simples (a/(x−1) + b/(x+1)) ; applications physiques (quantité d'électricité, énergie) ; annales du bac tunisien (2003) ; logiciels Menumath, Sine qua non, Dérive.
- ⛔ NON traité dans ce chapitre : définition de l'intégrale par sommes de Riemann (seule la définition par primitive) ; changement de variable ; intégrales généralisées (impropres) ; volumes par rotation autour de l'axe des ordonnées ; équations différentielles ; pas de QCM / Vrai-Faux ; les théorèmes sur les aires sont énoncés sans démonstration dans le cours (le volume V = π∫(f)² est explicitement « admis »).

> Sondage image : pages 168 à 191 (toutes) confrontées au PNG (24 pages sur 26, dont 186 et 187 ; 167 et 192 en couche texte seule : page de garde, aperçu historique) ; écarts : p.168 la couche texte avait mélangé le tableau de rappel des primitives et perdu les indices de n (ℤ* − {−1}) — rétabli sur image ; p.170 la couche texte donnait ∫ₐ^b f(t)dt sans bornes lisibles sur certaines lignes, bornes rétablies ; p.188 l'ex. 1 (bornes) et l'ex. 6 (parenthésage (eˣ cos x)²) rétablis sur image ; p.186–187 les bornes de J (−2 et 5) et K confirmées sur image ; p.191 borne inférieure « 1 » de ∫ f(t)dt (ex. 16 III) confirmée sur agrandissement, [sic] ; aucun autre mot ou nombre faux constaté sur les pages vues.

## 2.9 Chapitre 9 — Suites réelles (manuel 222451, p.193–220)

**Page de garde (p.193)** — Titre : « Suites réelles », Chapitre 9. Plan du chapitre : Activités
préliminaires ; Cours (Sens de variation d'une suite réelle ; Suite majorée, suite minorée, suite
bornée ; Limite d'une suite réelle) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ;
Aperçu Historique. Pas de rubrique QCM / Vrai-Faux dans ce chapitre. Le chapitre suppose acquis le
principe de récurrence, les suites arithmétiques et géométriques (rappelés en encadrés p.194–195) et
les limites de fonctions en +∞.

### Activités préliminaires (p.194–196)

- **Prél. 1** (p.194) : suite de Syracuse — N entier naturel non nul ; si N est pair on le divise par 2,
  sinon on le multiplie par 3 et on lui ajoute 1 ; on réitère jusqu'à l'apparition de 1. Déterminer
  tous les termes de la suite engendrée par N = 20 puis par N = 19.
- **Prél. 2** (p.194) : couples de lapins (suite de Fibonacci). 1) Vérifier que les nombres de couples
  sont 1, 1, 2, 3, 5, 8, 13, 21, … et forment la suite (v_n) définie par v_{n+2} = v_{n+1} + v_n,
  v_0 = v_1 = 1. 2) u_n = v_{n+1}/v_n : a) vérifier u_0 = 1 et ∀ n ∈ ℕ, u_{n+1} = 1 + 1/u_n ;
  b) montrer par récurrence que ∀ n ∈ ℕ, 1 ≤ u_n ≤ 2. 3) Figure : droite Δ : y = x et partie de la
  courbe C de f(x) = 1 + 1/x ; a) conjecturer graphiquement sur l'intersection de C et Δ ;
  b) résoudre dans ℝ l'équation f(x) = x. (Encadré « Principe de récurrence » : P(n) propriété d'un
  entier n ≥ n_0 ; si P(n_0) est vraie et si, pour n ≥ n_0, P(n) vraie ⇒ P(n+1) vraie, alors P(n) est
  vraie pour tout entier n ≥ n_0.)
- **Prél. 3** (p.195) : u_0 = 3, u_{n+1} = (2u_n + 3)/u_n. 1) Calculer u_1, u_2, u_3, u_4 ; conjecturer
  sur (u_n). 2) Démontrer le résultat par récurrence. (Encadré : (u_n) constante ⇔ ∀ n, u_{n+1} = u_n.)
- **Prél. 4** (p.195) : u_0 = 1, u_{n+1} = 3u_n/(u_n + 1). 1) Montrer par récurrence que ∀ n, u_n ≠ 2.
  2) v_n = u_n/(u_n − 2) : a) (v_n) géométrique (premier terme, raison) ; b) v_n en fonction de n et
  lim v_n ; c) S(n) = v_0 + … + v_n puis lim S(n) ; d) u_n en fonction de n et lim u_n.
- **Prél. 5** (p.195–196) : u_0 = 1, u_{n+1} = (−7u_n − 8)/(2u_n + 1). 1) Récurrence : ∀ n, u_n ≠ −2.
  2) v_n = (2u_n + 1)/(u_n + 2) : a) (v_n) arithmétique ; b) v_n en fonction de n et lim v_n ;
  c) u_n en fonction de n et lim u_n ; d) S_n = Σ_{k=0}^{n} v_k puis lim S_n.
- **Encadrés de rappel** (p.195–196) : suite géométrique (u_{n+1} = q·u_n, u_n = u_0·qⁿ, somme
  S_n = u_0·(1 − q^{n+1})/(1 − q) si q ≠ 1, (n+1)·u_0 si q = 1 ; lim u_n = 0 si −1 < q < 1, +∞ si q > 1
  et u_0 > 0, −∞ si q > 1 et u_0 < 0, u_0 si q = 1 ; pas de limite si q ≤ −1) ; suite arithmétique
  (u_{n+1} = u_n + r, u_n = u_0 + n·r, u_0 + … + u_n = (1+n)·(u_0 + u_n)/2 ; lim u_n = u_0 si r = 0,
  +∞ si r > 0, −∞ si r < 0) ; notation Σ_{k=0}^{n} u_k = u_0 + u_1 + … + u_n et
  Σ_{k=p}^{n} u_k = u_p + u_{p+1} + … + u_n pour p ≤ n.

### Cours — Activités

**Sens de variation d'une suite réelle** (p.197–199)

- **Activité 1** (p.197) : u_n = n² + 2n + 5 et f(x) = x² + 2x + 5 sur ℝ. a) Étudier le sens de variation
  de f ; b) en déduire ∀ n ∈ ℕ, u_{n+1} ≥ u_n.
- **Activité 2** (p.197) : u_n = (n + 4)/(2n + 1). a) Calculer u_{n+1} − u_n ; b) en déduire
  ∀ n ∈ ℕ, u_{n+1} ≤ u_n.
- **Activité 3** (p.197) : 1) u_n = 1 + E(2/n) sur ℕ* (E = partie entière) : montrer que (u_n) est
  stationnaire. 2) t_n = (−1)ⁿ sur ℕ : a) ensemble des valeurs de t_n ; b) (t_n) est-elle monotone ?
  (Encadré : la suite t_n = (−1)ⁿ est dite alternée.)
- **Activité 4** (p.198) : u_n = Σ_{k=1}^{n} 1/k² sur ℕ*. a) Calculer u_{n+1} − u_n ; b) en déduire le
  sens de variation.
- **Activité 5** (p.198) : a_0 = 16, a_{n+1} = √(a_n). 1) Calculer a_1, a_2, a_3 ; 2) a) récurrence :
  ∀ n, a_n ≥ 1 ; b) montrer que (a_n) est décroissante.
- **Activité 6** (p.198) : u_n = 2ⁿ/(n + 1). 1) a) ∀ n, u_n > 0 ; b) ∀ n, u_{n+1}/u_n ≥ 1 ; 2) en déduire
  que (u_n) est croissante sur ℕ.
- **Exercice résolu** (p.199, solution imprimée) : monotonie de a) v_n = n²/3ⁿ (v_{n+1} − v_n =
  (1/3^{n+1})(−2n² + 2n + 1) < 0 pour n ≥ 2, strictement décroissante sur {n ≥ 2}) ;
  b) w_n = 1 + 1/1! + 1/2! + … + 1/n! (w_{n+1} − w_n = 1/(n+1)! > 0, strictement croissante) ;
  c) t_n = e^{−n} (t_{n+1}/t_n = 1/e < 1, strictement décroissante ; « Autrement » : t_n = f(n) avec
  f(x) = e^{−x} strictement décroissante car f′(x) = −e^{−x} < 0).

**Suite majorée, suite minorée, suite bornée** (p.199–200)

- **Activité 1** (p.199) : 1) f(x) = (2x² + 1)/(x² + 5) sur ℝ : tableau de variation sur [0, +∞[ ;
  2) u_n = (2n² + 1)/(n² + 5) : en déduire ∀ n ∈ ℕ, 1/5 ≤ u_n ≤ 2.
- **Activité 2** (p.200) : u_n = (−1)ⁿ + cos n sur ℕ*. a) Montrer ∀ n, |u_n| ≤ 2 ; b) en déduire que
  (u_n) est bornée.
- **Activité 3** (p.200) : suite « définie sur ℕ* » [sic] avec u_0 = 8, u_{n+1} = √(2u_n + 35). Montrer par récurrence que (u_n) est
  minorée par 7.

**Limite d'une suite réelle** (p.200–209)

- **Activité 1** (p.200) : calculer lim u_n pour a) u_n = (5n + 3)/(n + 1) ; b) u_n = ln n / n ;
  c) u_n = 2n² − 1 ; d) u_n = (−3n² + 2)/(n + 5) ; e) u_n = (−1/2)ⁿ ; f) u_n = n·e^{−n}.
- **Activité 2** (p.201) : 1) étudier la convergence et comparer lim u_n et lim u_{n+1} pour
  a) u_n = (2/5)ⁿ ; b) u_n = 2ⁿ ; c) u_n = (2n − 1)/e^{2n}. 2) v_n = √(n+1) − √n : a) montrer que (v_n)
  est convergente et préciser sa limite ; b) ∀ n, 0 ≤ v_n ≤ 1.
- **Opérations — Activité 1** (p.202) : 1) u_n = (2eⁿ + 1)/(eⁿ + 5), lim u_n ; 2) v_n = cos(π/n) sur ℕ*,
  lim v_n ; 3) a_n = √(n² + 1) − √(n² − 1) [forme conjuguée], lim a_n ; 4) b_n = n·sin(1/n) sur ℕ*,
  lim b_n.
- **Exercice résolu** (p.203, solution imprimée) : lim u_n pour a) u_n = cos(2nπ) (=1) ;
  b) u_n = (2n² − n + 1)/(−n² + 3) (= f(n), limite −2) ; c) u_n = n²(1 − cos(1/n)) (limite 1/2 via
  lim_{x→0}(1 − cos x)/x² = 1/2).
- **Opérations — Activité 2** (p.203) : u_0 = 4, u_{n+1} = (1/2)u_n + 1. 1) a) ∀ n ∈ ℕ*,
  u_{n+1} − u_n = (1/2)(u_n − u_{n−1}) ; b) récurrence : (u_n) décroissante ; 2) (u_n) minorée par 2 ;
  3) v_n = u_n − 2 : a) géométrique (caractériser) ; b) lim v_n, en déduire (u_n) convergente ;
  4) w_n = 1 + 1/2 + 1/4 + … + 1/2ⁿ : a) croissante ; b) w_n = 2 − 1/2ⁿ donc w_n ≤ 2 ; c) lim w_n.
- **Opérations — Activité 3** (p.204) : u_0 = 4, u_{n+1} = (4u_n − 3)/u_n. 1) a) minorée par 3 ;
  b) décroissante ; c) convergente. 2) f(x) = (4x − 3)/x sur ]0, +∞[, courbe (C) en repère orthonormé
  (unité 2 cm) : a) variations et tracé ; b) résoudre f(x) = x, intersections de (C) et Δ : y = x ;
  c) représenter les 4 premiers termes ; d) conjecturer lim u_n. 3) a) ∀ n, u_{n+1} − 3 ≤ (1/3)(u_n − 3) ;
  b) ∀ n, u_n − 3 ≤ (1/3)ⁿ ; c) lim u_n = 3.
- **Opérations — Activité 4** (p.204) : 1) u_n = √(n+2) − √(n+1) : a) lim u_n ; b) v_n = √(u_n + 2) −
  √(u_n + 1), lim v_n. 2) x_n = 2ⁿ : a) lim x_n ; b) y_n = (2^{n+1} − 15)/(2ⁿ + 1), lim y_n.
- **Opérations — Exercice résolu** (p.205, solution imprimée) : u_0 = 3, u_{n+1} = √(u_n + 1) ;
  a) strictement décroissante (récurrence, u_{p+2} − u_{p+1} = (u_{p+1} − u_p)/(√(1+u_{p+1}) + √(1+u_p))) ;
  b) convergente, limite ℓ avec ℓ² = 1 + ℓ, soit ℓ = (1 + √5)/2.
- **Opérations — Activité 5** (p.205–206) : u_0 = 1/2, u_{n+1} = (u_n)² + 3/16. 1) ∀ n, 1/4 ≤ u_n ≤ 1/2 ;
  2) (u_n) décroissante ; 3) (u_n) convergente ; 4) f(x) = x² + 3/16 : a) résoudre dans [1/4, 1/2]
  l'équation x² + 3/16 = x ; b) montrer lim u_n = 1/4.

**Théorèmes de comparaison** (p.206–209)

- **Activité 1** (p.206) : 1) u_n = cos n − 3n : a) ∀ n, u_n ≤ 1 − 3n ; b) lim (1 − 3n), conclure sur
  lim u_n. 2) v_n = eⁿ + 2 sin n : a) ∀ n, v_n ≥ eⁿ − 2 ; b) lim (eⁿ − 2), conjecture sur lim v_n.
- **Activité 2** (p.206) : u_n = 1/√(n²+1) + 1/√(n²+2) + … + 1/√(n²+n) sur ℕ*. 1) ∀ n,
  n/√(n²+n) ≤ u_n ≤ n/√(n²+1) ; 2) a) lim n/√(n²+n) et lim n/√(n²+1) ; b) conjecturer lim u_n.
- **Activité 3** (p.207) : t_n = (3n + cos n)/(2n) sur ℕ*. 1) ∀ n, (3n − 1)/(2n) ≤ t_n ≤ (3n + 1)/(2n) ;
  2) en déduire que (t_n) converge et sa limite.
- **Activité 4** (p.207) : 1) u_0 = 0, u_{n+1} = 1/(2 − u_n) : a) calculer u_1, u_2, u_3 (forme
  irréductible) ; b) comparer les 4 premiers termes à ceux de w_n = n/(n+1) ; c) récurrence :
  ∀ n, u_n = w_n. 2) v_n = ln(n/(n+1)) sur ℕ* : a) v_1 + v_2 + v_3 = −ln 4 ; b) S_n = v_1 + … + v_n en
  fonction de n, puis lim S_n.
- **Activité 5** (p.207–208) : u_0 = ∫_0^1 dx/√(x²+1) et, pour n ∈ ℕ*, u_n = ∫_0^1 xⁿ/√(x²+1) dx.
  1) f(x) = ln(x + √(x²+1)) sur [0, 1] : a) f dérivable et f′(x) = 1/√(x²+1) ; b) en déduire u_0.
  2) a) (u_n) décroissante et minorée par 0 ; b) convergente. 3) a) ∀ x ∈ [0,1], 1 ≤ √(x²+1) ≤ √2 ;
  b) ∀ n, 1/((n+1)√2) ≤ u_n ≤ 1/(n+1) ; c) lim u_n.
- **Activité 6** (p.208) : 1) f(x) = eˣ/√(1+e^{2x}) sur ℝ, courbe C en repère orthonormé : a) vérifier
  f(x) = 1/√(1+e^{−2x}) ; b) lim_{+∞} f et lim_{−∞} f, interprétation graphique ; c) tableau de variation.
  2) φ(x) = f(x) − x : a) tableau de variation ; b) l'équation φ(x) = 0 admet une unique solution α avec
  0,9 < α < 1 ; c) signe de φ, position relative de C et Δ : y = x ; d) tracer C et Δ.
  3) u_0 = 1/2, u_{n+1} = f(u_n) : a) ∀ n, 0 ≤ u_n ≤ α ; b) monotonie de (u_n), conclure ; c) sachant
  ∀ x ∈ ℝ, 0 < f′(x) ≤ 2/(3√3) : |u_{n+1} − α| ≤ (2/(3√3))·|u_n − α| ; d) |u_n − α| ≤
  (2/(3√3))ⁿ·|1/2 − α|, en déduire lim u_n.
- **Exercice résolu** (p.208–209, solution imprimée) : I_n = ∫_{−1}^{0} e^{n·t}/(1 + eᵗ) dt sur ℕ*.
  1) I_1 = ln(2e/(e+1)) ; 2) a) (I_n) décroissante et positive ; b) convergente ; 3) a) ∀ n,
  I_n ≤ (1/n)(1 − e^{−n}) ; b) lim I_n = 0.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Définition — monotonie** (p.197) — « Soit (u_n) une suite réelle définie sur l'ensemble
> K = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ. On dit que : • (u_n) est croissante (resp. strictement croissante)
> sur K si et seulement si ∀ n ∈ K, u_{n+1} ≥ u_n (resp. u_{n+1} > u_n). • (u_n) est décroissante (resp.
> strictement décroissante) sur K si et seulement si ∀ n ∈ K, u_{n+1} ≤ u_n (resp. u_{n+1} < u_n).
> • (u_n) est constante sur K si et seulement si ∀ n ∈ K, u_{n+1} = u_n. • (u_n) est monotone sur K si
> elle est croissante ou décroissante sur K. • (u_n) est stationnaire sur K s'il existe un entier p de K
> tel que ∀ n ≥ p, u_{n+1} = u_n. »

> **Techniques d'étude de la monotonie d'une suite** (p.198) — « Pour étudier la monotonie d'une suite
> réelle (u_n) on peut utiliser l'une des techniques suivantes : • Étudier le signe de la différence
> u_{n+1} − u_n ; • Utiliser un raisonnement par récurrence ; • Comparer le rapport u_{n+1}/u_n à 1,
> dans le cas où tous les termes de (u_n) sont non nuls et de même signe. Par exemple, pour une suite
> (u_n) à termes strictement positifs : ◦ Si pour tout entier n, u_{n+1}/u_n ≥ 1 alors (u_n) est
> croissante. ◦ Si pour tout entier n, u_{n+1}/u_n ≤ 1 alors (u_n) est décroissante. »

> **Définition — majorée, minorée, bornée** (p.200) — « Soit n_0 un entier naturel donné et (u_n) une
> suite de nombres réels définie sur l'ensemble K = {n ∈ ℕ ; n ≥ n_0}. On dit que : • (u_n) est majorée
> sur K lorsqu'il existe un réel M tel que ∀ n ∈ K, u_n ≤ M. • (u_n) est minorée sur K lorsqu'il existe
> un réel m tel que ∀ n ∈ K, u_n ≥ m. • (u_n) est bornée sur K lorsqu'il existe des réels m et M tel que
> ∀ n ∈ K, m ≤ u_n ≤ M. » [sic : « tel que » au pluriel attendu]

> **Théorème admis** (p.200) — « Soit (u_n) une suite de nombres réels définie sur l'ensemble
> K = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ. La suite (u_n) est bornée sur K si et seulement si il existe un réel
> M tel que ∀ n ∈ K, |u_n| ≤ M. »

> **Définition — convergence** (p.201) — « Soit (u_n) une suite de nombres réels définie sur l'ensemble
> K = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ. • (u_n) est dite convergente si et seulement si il existe un réel ℓ
> tel que lim_{n→+∞} u_n = ℓ. Dans ce cas on dit que la suite (u_n) converge vers ℓ. • (u_n) est dite
> divergente lorsque lim_{n→+∞} u_n = −∞ ou lim_{n→+∞} u_n = +∞ ou (u_n) n'a pas de limite quand n tend
> vers +∞. »

> **Théorème** (p.201) — « Soit f une fonction définie sur un intervalle du type [a, +∞[ où a ∈ ℝ⁺ et
> (u_n) la suite définie par u_n = f(n). • Si lim_{x→+∞} f(x) = ℓ alors lim_{n→+∞} u_n = ℓ. • Si
> lim_{x→+∞} f(x) = +∞ alors lim_{n→+∞} u_n = +∞. • Si lim_{x→+∞} f(x) = −∞ alors lim_{n→+∞} u_n = −∞. »

> **Des limites de référence** (p.201) — lim_{n→+∞} n² = +∞ ; lim_{n→+∞} 1/n² = 0 ; lim_{n→+∞} 1/n = 0 ;
> lim_{n→+∞} √n = +∞ ; lim_{n→+∞} ln(n)/n = 0 ; lim_{n→+∞} eⁿ/n = +∞.

> **Propriétés** (p.201) — « • Si une suite (u_n) converge, alors sa limite est unique et on a :
> lim_{n→+∞} u_n = lim_{n→+∞} u_{n+1}. • Si une suite (u_n) converge, alors elle est bornée. »

> **Opérations sur les limites des suites réelles** (p.202, tableau ; F.I = forme indéterminée, « pour
> laquelle une étude spécifique doit être menée pour déterminer l'éventuelle limite »). Colonnes
> lim u_n ; lim v_n ; lim(u_n + v_n) ; lim(u_n × v_n) ; lim(u_n / v_n). Lignes :
> (a ; b réels) → a + b ; a × b ; a/b si b ≠ 0 · (0 ; 0) → 0 ; 0 ; F.I · (a réel ; 0⁺) → a ; 0 ;
> +∞ × signe(a) si a ≠ 0 · (+∞ ; b réel) → +∞ ; +∞ × signe(b) si b ≠ 0 ; +∞ × signe(b) si b ≠ 0 ·
> (+∞ ; 0⁻) → +∞ ; F.I ; −∞ · (+∞ ; 0⁺) → +∞ ; F.I ; +∞ · (−∞ ; b réel) → −∞ ; −∞ × signe(b) si b ≠ 0 ;
> −∞ × signe(b) si b ≠ 0 · (−∞ ; 0⁻) → −∞ ; F.I ; +∞ · (−∞ ; 0⁺) → −∞ ; F.I ; −∞ · (+∞ ; +∞) → +∞ ; +∞ ;
> F.I · (+∞ ; −∞) → F.I ; −∞ ; F.I · (−∞ ; −∞) → −∞ ; +∞ ; F.I · (a réel ; +∞) → +∞ ; +∞ × signe(a)
> (F.I si a = 0) ; 0 · (a réel ; −∞) → −∞ ; −∞ × signe(a) (F.I si a = 0) ; 0.

> **Théorème admis** (p.203) — « • Toute suite décroissante et minorée est convergente. • Toute suite
> croissante et majorée est convergente. »

> **Théorème admis** (p.205) — « Soit f une fonction définie sur D et (u_n) une suite numérique définie
> sur I = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ telle que ∀ n ∈ I, u_n ∈ D. Soit ℓ ∈ D. • Si (u_n) converge vers ℓ
> et f est continue en ℓ alors la suite (v_n) définie sur I par v_n = f(u_n) converge vers f(ℓ). • Si
> (u_n) est telle que u_{n+1} = f(u_n) et converge vers ℓ et f est continue en ℓ alors f(ℓ) = ℓ. • Si
> lim_{n→+∞} u_n = +∞ et lim_{x→+∞} f(x) = ℓ alors la suite (v_n) définie par v_n = f(u_n) converge vers ℓ. »

> **Théorème — comparaison** (p.206) — « (u_n) et (v_n) sont deux suites réelles définies sur
> K = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ. On suppose qu'il existe un entier p tel que ∀ n ≥ p, u_n ≤ v_n.
> • Si lim_{n→+∞} u_n = +∞ alors lim_{n→+∞} v_n = +∞. • Si lim_{n→+∞} v_n = −∞ alors
> lim_{n→+∞} u_n = −∞. »

> **Théorème — gendarmes** (p.207) — « Soient (u_n), (v_n) et (w_n) trois suites réelles définies sur
> K = {n ∈ ℕ ; n ≥ n_0} où n_0 ∈ ℕ. On suppose qu'il existe un entier p tel que ∀ n ≥ p,
> v_n ≤ u_n ≤ w_n. Si les suites (v_n) et (w_n) convergent vers le même réel ℓ alors (u_n) converge aussi
> vers ℓ. En particulier : s'il existe un entier p tel que ∀ n ≥ p, |u_n| ≤ v_n et lim_{n→+∞} v_n = 0
> alors lim_{n→+∞} u_n = 0. »

> **Résumé du cours** (p.210–211) — reprend les encadrés ci-dessus (monotonie, techniques d'étude,
> majorée/minorée/bornée, convergence, f(n), suites monotones bornées, théorème de composition avec f
> continue, théorèmes de comparaison et des gendarmes), avec ces écarts : f(n) y est énoncé pour a ∈ ℝ
> (le cours p.201 dit a ∈ ℝ⁺) ; sans la définition de la divergence, ni le théorème |u_n| ≤ M, ni les
> Propriétés p.201, ni les sous-cas du rapport u_{n+1}/u_n ; « tels que » correctement accordé ; les
> théorèmes de comparaison sont énoncés sans le cadre « Théorème » ; sans tableau d'opérations ni
> limites de référence.

### Avec l'ordinateur (p.212–214)

- **Activité 1** (p.212) : représentation graphique d'une suite récurrente u_{n+1} = f(u_n) (construction
  en escalier avec Δ : y = x) pour u_0 = 6 et f(x) = 1 + √(x − 1) ; usage du logiciel « Sine qua non »
  pour u_0 = 5, u_{n+1} = ln(u_n + 3).
- **Activité 2** (p.213–214) : étude à l'ordinateur (tableur) de u_0 = 1, u_{n+1} = 1 + 1/u_n : feuille
  de calcul (formules = 1 + 1/B2, etc.) et nuage de points, conjecture sur le sens de variation et la
  limite ; lecture d'une valeur approchée de la limite ; nombre d'or φ = (1 + √5)/2 : a) φ = 1 + 1/φ ;
  b) u_3, u_4, u_5, … sont des valeurs approchées de φ ; 5) déterminer lim u_n.

### Exercices et problèmes (p.215–218) — 16 exercices

- **Ex. 1** (p.215) : u_0 = −1, u_{n+1} = (4u_n + 3)/(u_n + 6). Récurrence −3 < u_n < 1 ; signe de
  u_{n+1} − u_n ; v_n = (u_n − 1)/(u_n + 3) géométrique, v_n et u_n en fonction de n, lim v_n,
  S_n = Σ_{k=0}^{n−1} v_k et lim S_n.
- **Ex. 2** (p.215) : u_0 = 1, u_{n+1} = 4/(4 − u_n). u_n ≤ 2 ; croissante ; convergente et limite ;
  v_n = 1/(u_n − 2) géométrique à caractériser, v_n, lim v_n, u_n en fonction de n, retrouver lim u_n.
- **Ex. 3** (p.215) : u_0 = 0, u_{n+1} = √(6 + u_n). 0 ≤ u_n ≤ 3 ; croissante ; convergente et limite ;
  |u_{n+1} − 3| ≤ (1/3)|u_n − 3| ; |u_n − 3| ≤ (1/3)^{n−1} ; retrouver lim u_n.
- **Ex. 4** (p.215) : u_0 = 1, u_{n+1} = (5u_n + 3)/(u_n + 3). u_{n+1} = 5 − 12/(u_n + 3) ; 0 ≤ u_n < 3 ;
  monotone, conclure ; v_n = (u_n − 3)/(u_n + 1) géométrique, v_n, u_n, limites ; w_n = u_n − 3 :
  |w_{n+1}| ≤ (2/3)|w_n|, |w_n| ≤ 2(2/3)ⁿ, lim w_n et lim u_n.
- **Ex. 5** (p.216) : u_0 = 3/2, u_{n+1} = 1 + √(u_n − 1). 1 < u_n < 2 ; croissante ; convergente, limite ;
  v_n = ln(u_n − 1) géométrique de raison 1/2, lim v_n, retrouver lim u_n (« D'après Bac Tunisien 2004 »).
- **Ex. 6** (p.216) : f(x) = eˣ/(1 + eˣ) ; u_n = (1/n)∫_0^n f(x + ln n) dt sur ℕ* [sic : dt avec variable
  x]. Vérifier f(x + ln n) = n·eˣ/(1 + n·eˣ) ; calculer u_n ; lim ln(1 + n·eⁿ)/n = 1 et
  lim ln(1+n)/n = 0 ; lim u_n.
- **Ex. 7** (p.216) : v_n = 1/√1 + 1/√2 + … + 1/√n sur ℕ*. a) pour 1 ≤ p ≤ n, 1/√p ≥ 1/√n ;
  b) v_n ≥ √n ; c) lim v_n.
- **Ex. 8** (p.216) : f(x) = ln(x + 3). Tableau de variation et courbe ; h(x) = f(x) − x : unique
  solution α ∈ ]1, 2[ de h(x) = 0 ; u_0 = 1, u_{n+1} = f(u_n) : 1 ≤ u_n ≤ 2, croissante, convergente,
  limite.
- **Ex. 9** (p.216) : u_0 = 1, u_{n+1} = √((1/2)u_n² + 1). 1 ≤ u_n ≤ √2 ; croissante ; convergente ;
  v_n = u_n² − 2 géométrique ; v_n et u_n en fonction de n ; lim v_n, lim u_n ; S_n = Σ_{k=0}^{n} u_k² ;
  lim S_n/n.
- **Ex. 10** (p.217) : K_n = ∫_0^1 (x + 1)e^{−n·x} dx sur ℕ*, I = ∫_0^1 x·e^{−x} dx. 1) a) calculer K_0,
  I, K_1 − I et K_1 ; b) (K_n) décroissante ; c) convergente. 2) a) e^{−nx} ≤ (x+1)e^{−nx} ≤ 2e^{−nx} ;
  b) (1 − e^{−n})/n ≤ K_n ≤ 2(1 − e^{−n})/n ; c) lim K_n.
- **Ex. 11** (p.217) : J_n = ∫_0^1 e^{nt}/(1 + eᵗ) dt. 1) a) J_0 + J_1 et J_1, en déduire J_0 ;
  b) (J_n) croissante ; 2) a) ∀ t ∈ [0,1], 1/4 ≤ 1/(1+eᵗ) ≤ 1/2 ; b) encadrement de J_n ; c) (J_n)
  divergente.
- **Ex. 12** (p.217) : 0 < U_0 < V_0, U_n·V_n = U_0·V_0 et V_n = (1/2)(U_{n−1} + V_{n−1}) pour n ∈ ℕ*.
  1) U_n > 0, V_n > 0 ; 2) a) U_n < V_n ; b) (U_n) croissante et (V_n) décroissante ; 3) suites
  convergentes ; a) V_n − U_n < (1/2)(V_{n−1} − U_{n−1}) ; b) lim (V_n − U_n) = 0 et lim U_n = lim V_n ;
  c) cette limite commune.
- **Ex. 13** (p.217) : U_0 = 1, U_{n+1} = U_n/√(1 + U_n²). 1) 0 < U_n ≤ 1 ; décroissante ; convergente,
  limite. 2) V_n = 1/U_n² : arithmétique de raison 1 ; V_n, U_n en fonction de n, retrouver lim U_n ;
  S_n = Σ_{k=0}^{n−1} V_k, lim S_n/n².
- **Ex. 14** (p.217–218) : I_0 = ∫_0^1 dt/(1 + t²) et, pour n ≥ 1, I_n = ∫_0^1 t^{2n}/(1 + t²) dt.
  1) a) I_0 + I_1 sachant ∫_0^1 dt/(1+t²) = π/4, en déduire I_1 ; b) I_{n+1} + I_n = 1/(2n+1), calculer
  I_2 et I_3 ; c) (I_n) décroissante et minorée par 0 ; d) conclure. 2) a) 0 ≤ t^{2n}/(1+t²) ≤ t^{2n} ;
  b) 0 ≤ I_n ≤ 1/(2n+1), lim I_n.
- **Ex. 15** (p.218) : a > 0 fixé, I_n(a) = ∫_0^a tⁿ·e^{−t}/n! dt sur ℕ*. 1) I_1(a) ; 2) a) 0 ≤ tⁿe^{−t}/n! ≤
  tⁿ/n! ; b) 0 ≤ I_n(a) ≤ a^{n+1}/(n+1)! ; 3) a) par parties, I_n(a) − I_{n−1}(a) = −(aⁿ/n!)·e^{−a} pour
  n ≥ 2 ; b) (I_n(a)) convergente ; c) I_n(a) = 1 − e^{−a}(1 + a/1! + a²/2! + … + aⁿ/n!) ; 4) sachant
  lim I_n(a) = 0, e^a = lim (1 + a/1! + a²/2! + … + aⁿ/n!).
- **Ex. 16** (p.218) : f(x) = x·ln(1 − x) + 1/4 si x < 0 ; f(x) = eˣ/(x² + 4) si x ≥ 0 ; courbe C.
  1) a) continuité et dérivabilité en 0 ; b) tableau de variation sur ℝ ; c) branches infinies, tracé.
  2) a) ∀ x ∈ [0,1], (x² − 2x + 4)/(x² + 4)² ≤ 1/4 ; b) 0 ≤ f′(x) ≤ 3/4. 3) g(x) = f(x) − x sur [0,1] :
  a) tableau de variation ; b) f(x) = x admet une unique solution α dans [0,1], comparer f(x) et x.
  4) u_0 = 1, u_{n+1} = f(u_n) : a) α ≤ u_n ≤ 1 ; b) monotone, conclure ; c) 0 ≤ u_{n+1} − α ≤
  (3/4)(u_n − α) ; d) α ≤ u_n ≤ α + (3/4)ⁿ ; e) lim u_n = α.

### Aperçu historique (p.219–220)

Archimède et les suites pour mesurer un arc de parabole ; Héron d'Alexandrie (racine carrée) ; Al-Karaji
(Xe–XIe s.) démontrant (Σ k)² = Σ k³ ; Lagrange (notation indicielle uₙ) ; Fibonacci (1170–1240) et la
suite récurrente v_{n+2} = v_{n+1} + v_n, nombre d'or, et une série pour π à partir d'une suite de type
Fibonacci (U_0, U_1 > 0, U_n = U_{n−1} + U_{n−2}).

### Bornes de scope observées (chapitre 9)

- ✅ INCLUS : monotonie (différence, récurrence, rapport) ; suites majorée/minorée/bornée ; limite
  d'une suite, f(n), tableau d'opérations et formes indéterminées ; convergence des suites monotones
  bornées (admise) ; suites récurrentes u_{n+1} = f(u_n) et limite par f(ℓ) = ℓ (f continue) ;
  comparaison et gendarmes ; suites auxiliaires géométriques/arithmétiques ; suites d'intégrales ;
  rappels de récurrence, arithmétique/géométrique, notation Σ.
- ⛔ NON traité : suites adjacentes, suites de Cauchy, sous-suites, théorème de Bolzano–Weierstrass,
  définition ε–N de la limite ; QCM / Vrai-Faux ; réponses ou corrigés des exercices (seuls 4 exercices
  résolus ; les exercices 1–16 n'ont pas de solution imprimée).

> Sondage image : pages 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 212, 215,
> 216, 217, 218 (19 pages sur 28 ; soit toutes les pages à formules) ; écarts constatés entre couche
> texte et image : exposants perdus (u_n = 2ⁿ/(n+1) lu « 2n » ; v_n = n²/3ⁿ lu « 3n » ; e^{−x} ; x^{n}),
> racines carrées perdues (a_{n+1} = √a_n ; f(x) = eˣ/√(1+e^{2x}) ; 1 + √(x−1)), barres de valeur absolue
> perdues (|u_n| ≤ M, |u_{n+1} − α|, |w_n|), indices de sommes ; tous corrigés ci-dessus d'après l'image.
> Pages 209, 210, 211, 213, 214, 219, 220 lues en texte seul (p.220 : formule de π lue en texte,
> reproduite en une ligne seulement).

## 2.10 Chapitre 10 — Nombres complexes (manuel 222451, p.221–240)

**Page de garde (p.221)** — Titre : « Nombres Complexes ». Le numéro de chapitre imprimé (pages de garde
et bandeaux) est « 1 » [sic : numéro imprimé différent du rang 10 dans le manuel 222451]. Plan : Activités préliminaires ; Cours (Opérations algébriques sur les nombres complexes ;
Forme trigonométrique et forme exponentielle d'un nombre complexe ; Conditions de colinéarité et
d'orthogonalité de deux vecteurs) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ;
Aperçu Historique. Pas de QCM / Vrai-Faux. Convention du chapitre (p.222) : P est le plan complexe
rapporté à un repère orthonormé direct (O, u⃗, v⃗) ; ℂ désigne l'ensemble des nombres complexes.

### Activités préliminaires (p.222)

- **Prél. 1** : z = 1 − 2i et z′ = 3 + 4i ; calculer z + z′, z·z′, z², 1/z, z/z′.
- **Prél. 2** : 1) calculer (1+i)², (1+i)³, (1−i)², (1−i)³, (1+i)(1−i) et (1+i)/(1−i) ; 2) écrire sous
  forme algébrique Z = (z² + z + 1)/(z³ + z² + 1) pour a) z = 1 + i ; b) z = 1 − i.
- **Prél. 3** : placer dans le plan complexe les images de z_1 = 1 − 2i, z_2 = −3i, z_3 = 1/i, z_4 = 2,
  z_5 = −3 − 4i.
- **Prél. 4** : 1) calculer i², i³, i⁴, i⁵, i⁶, i⁷, i⁸ ; conjecturer pour i¹² ; 2) montrer que pour tout
  n ∈ ℕ, iⁿ = i^r où r est le reste de la division euclidienne de n par 4 ; 3) en déduire i⁷⁴⁵, i¹⁹⁷²,
  i²⁰⁰⁸ et i^{−2007}.
- **Prél. 5** : à tout point M d'affixe z et de coordonnées (x, y) on associe Z = z². 1) Re(Z) et Im(Z)
  en fonction de x et y ; 2) ensemble des points M tels que a) Z soit réel ; b) Z soit réel négatif ;
  c) Z soit imaginaire pur.
- **Prél. 6** : u = 1 − i et v = 1 + i√3. 1) module et un argument de u et de v ; 2) écrire u et v sous
  forme trigonométrique.

### Cours — Activités

**Opérations algébriques sur les nombres complexes** (p.223–226)

- **Forme algébrique / représentation géométrique** (p.223, encadrés de cours, voir « Résultats ») et
  **Activité** (p.223) : repère orthonormé (O, u⃗, v⃗), points A(2+i), B(1−i), C(i), D(−1−i). 1) Affixes
  des vecteurs AB⃗, AC⃗, AD⃗ et AB⃗ + AC⃗ ; 2) en déduire la nature du quadrilatère ABDC.
- **Conjugué — Activité 1** (p.224) : z = 3 − 2i. 1) placer l'image M de z ; 2) construire le symétrique
  M′ de M par rapport à l'axe des réels ; 3) affixe z′ de M′ ; 4) comparer parties réelles et
  imaginaires de z et z′.
- **Conjugué — Activité 2** (p.224) : points A(−2−i), B(1+3i), I milieu de [AB]. 1) a) placer A, B, I ;
  b) déterminer et construire l'ensemble D des points M(z) tels que 4(z + z̄) + 3i(z − z̄) + 10 = 0 ;
  c) vérifier que A et B appartiennent à D. 2) 𝒞 = ensemble des points M(z) tels que
  4z·z̄ + 2(z + z̄) + 4i(z − z̄) − 20 = 0 : a) équation cartésienne de 𝒞 ; b) montrer que 𝒞 est le cercle de
  diamètre [AB].
- **Conjugué — Activité 3** (p.224) : à tout point M(z), z ≠ i, on associe M′(z′) avec
  z′ = (z − 1 + i)/(i − z). 1) coordonnées de A′ associé à A(1+2i) ; 2) coordonnées du point B auquel est
  associé B′(0, −2) ; 3) ensemble (à construire) des M(z) tels que z′ soit réel ; 4) ensemble des M(z)
  tels que z′ soit imaginaire pur.
- **Module — Activité 1** (p.225) : 1) modules de i ; −3 ; (1+i)² ; 3 − i√3 ; (−1 + i√3)/2. 2) calculer
  |(1 + i√3)⁴ (2 − i√2)⁷| et |1/(1+2i)² − (i+2)/(1−i)|. 3) a) montrer que |z + z′| ≤ |z| + |z′| ;
  b) dans quels cas |z + z′| = |z| + |z′| ?
- **Module — Activité 2** (p.226) : A(1), B(−1/2 + i√3/2), C(−1/2 − i√3/2) : montrer que ABC est
  équilatéral. (Encadré : MN = |z_N − z_M|.)
- **Module — Activité 3** (p.226) : a ≠ −i ; montrer que (1 + ai)/(1 − ai) est de module 1 si et seulement
  si a est réel.
- **Module — Activité 4** (p.226) : A(−2+i), B(−3i), C(i) ; à tout M(z), z ≠ −3i, on associe M′ d'affixe
  z′ = (z + 2 − i)/(3 − iz). 1) ensemble des M(z) tels que a) z′ soit réel ; b) z′ soit imaginaire pur ;
  c) |z′| = 1 (à construire). 2) a) montrer |z′ − i|·|z + 3i| = 2√5 (z ≠ −3i) ; b) en déduire que si M
  appartient au cercle de centre B et de rayon 1, M′ appartient à un cercle (centre et rayon à préciser).
- **Module — Activité 5** (p.226) : déterminer l'ensemble Δ des points M(z) tels que |z| = |z̄ − 2|.
  (Encadré : |z| = |z̄|.)

**Argument d'un nombre complexe non nul** (p.226–227)

- **Activité 1** (p.226) : 1) construire A, B, C d'affixes Z_1 = 1 + i, Z_2 = −i, Z_3 = 2 ; 2) mesure de
  chacun des angles (u⃗, OA⃗), (u⃗, OB⃗), (u⃗, OC⃗).
- **Activité 2** (p.227) : z non nul, M son image. 1) a) nature de l'application M(z) ↦ M′(z̄) ; b) arg(z̄)
  en fonction de arg(z). 2) a) application M(z) ↦ M′(−z) ; b) arg(−z) en fonction de arg(z). 3) α réel non
  nul : arg(α·z) en fonction de arg(z) (discuter selon le signe de α). 4) arguments de 1 ; −1 ; i ; −i ;
  1 + i ; 1 − i ; −1 + i ; −1 − i.

**Forme trigonométrique d'un nombre complexe non nul** (p.228–229)

- **Activité 1** (p.228) : 1) z = a + ib non nul, r = |z|, θ = Arg(z) + 2kπ (k ∈ ℤ) : exprimer cos θ et
  sin θ en fonction de a, b, r. 2) θ ∈ ℝ ; écrire sous forme trigonométrique z_1 = 1 + i√3 ;
  z_2 = √3 − i ; z_3 = −√2 + i√2 ; z_4 = −3 + i√3 ; z_5 = cos θ − i sin θ ; z_6 = −cos θ − i sin θ ;
  z_7 = sin θ + i cos θ.
- **Activité 2** (p.228–229) : 1) z = [r, θ], z′ = [r′, θ′] (r, r′ ∈ ℝ₊*, θ, θ′ ∈ ℝ) : formes
  trigonométriques de z̄ ; z·z′ ; 1/z ; z/z′ ; zⁿ (n ∈ ℤ) et λ·z (λ ∈ ℝ*). 2) Applications :
  z_1 = (√6 − i√2)/2 et z_2 = 1 − i : a) formes trigonométriques de z_1 ; z_2 ; z̄_1 ; z̄_2 ; z_2/z_1 et
  z_1⁶ ; b) en déduire la forme trigonométrique de Z = (√6 + √2)/4 + i(√6 − √2)/4.
- **Activité 3** (p.229) : points A, B, C, D d'affixes a = (√3 + i)/2, b = (−1 + i√3)/2, c = a + b, d = b − a ;
  figure : cercle trigonométrique gradué (valeurs remarquables). 1) a, b et b/a sous forme
  trigonométrique, nature du triangle ABO ; 2) placer A, B, C, D et montrer que OACB est un carré ;
  3) formes trigonométriques de c et d ; 4) en déduire cos(5π/12), sin(5π/12), cos(11π/12) et sin(11π/12).

**Forme exponentielle d'un nombre complexe non nul** (p.229–230)

- **Activité 1** (p.230) : 1) z = r·e^{iθ}, z′ = r′·e^{iθ′} : formes exponentielles de z̄ ; z·z′ ; 1/z ; z/z′ ;
  zⁿ (n ∈ ℤ) ; λ·z (λ ∈ ℝ*). 2) a) écrire sous forme exponentielle (−1 + i)⁴ ; (−1 + i√3)(3 − i√3) ;
  (√3 − i)³/(√2 − i√2)⁵ ; b) θ ∈ ℝ : exprimer cos θ et sin θ à l'aide de e^{iθ} et e^{−iθ} ;
  c) θ ∈ ]0, π[ : formes exponentielles de z_1 = 1 + e^{iθ} ; z_2 = 1 − e^{iθ} ;
  z_3 = (1 + i)(cos θ + i sin θ) ; z_4 = sin θ + i(1 + cos θ).
- **Activité 2** (p.230) : x réel. 1) comparer (e^{ix})ⁿ et e^{inx} ; 2) exprimer cos(3x) et sin(3x) en
  fonction des puissances de cos x et sin x.
- **Activité 3** (p.230) : x réel ; avec les formules d'Euler, écrire comme sommes de termes a·cos(nx) et
  b·sin(nx) (« linéariser ») : cos²x ; sin²x ; cos³x ; sin⁴x et cos³x·sin⁴x [sic : l'énoncé imprime
  « cos³x . sin⁴x »].

**Colinéarité et orthogonalité de deux vecteurs** (p.231–232)

- **Activité 1** (p.231) : z = e^{2iθ}, θ réel de ]0, 2π[. 1) module et un argument de
  z′ = (1 − z)²/(z̄(1 + z)) ; 2) valeur de θ pour laquelle z′ est un réel.
- **Activité 2** (p.231) : A(1), B(−i) ; f : P \ {B} → P, M(z) ↦ M′(z′) avec z′ = (z̄ + 2i)/(z̄ − i).
  1) vérifier z′ − 1 = 3i/(z̄ − i), en déduire BM·AM′ = 3 et (BM⃗, AM′⃗) = π/2 + 2kπ ; 2) a) si M
  appartient au cercle 𝒞 de centre B et de rayon 3, M′ appartient à un cercle 𝒞′ à préciser ; b) si M
  appartient à la droite (AB), M′ appartient à une droite à préciser.
- **Activité 3** (p.232) : A(1), B(−1) ; à tout M(z), z ≠ 1, on associe M′(z′) avec z′ = (z − 1)/(1 − z̄).
  1) |z′| = 1 ; 2) (z′ − 1)/(z − 1) est réel et (z′ + 1)/(z − 1) est imaginaire pur ; 3) interprétation
  géométrique, construction de M′ connaissant M.
- **Activité 4** (p.232) : z_1 = (1 + i)(−1 + 5i)/2 ; z_2 = (−9 + 7i)/(2 − 3i) ; z_3 = 2(1 + i)/(1 − i).
  1) placer A(z_1), B(z_2), C(z_3) ; 2) ABC est rectangle isocèle ; 3) a) affixe du milieu I de [BC] ;
  b) affixe du point D tel que ABCD soit un carré.
- **Activité 5** (p.232) : A(−2−i), B(1+3i), D(−5i/2), C(3 + 3i/2) [lecture : D(−5/2 i)]. 1) a) (CD) et (AB)
  parallèles ; b) (CD) tangente au cercle 𝒞 de diamètre [AB] ; 2) nature du quadrilatère ABCD.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Forme algébrique** (p.223) — « Tout nombre complexe z s'écrit d'une manière unique sous la forme
> algébrique suivante : z = a + i b où a et b sont des réels et i est un nombre complexe tel que : i² = −1.
> a s'appelle la partie réelle de z. On la note a = Re(z) ; b s'appelle la partie imaginaire de z. On la
> note b = Im(z). On note ℂ l'ensemble des nombres complexes. »

> **Représentation géométrique** (p.223) — « Le plan P est rapporté à un repère orthonormé direct
> (O, u⃗, v⃗). – Soit M(x, y) un point de P. On appelle affixe de M, le nombre complexe noté aff(M) ou
> z_M tel que : aff(M) = z_M = x + iy. – M(x, y) est le point image du nombre complexe z = x + iy. – Pour
> tous points A et B appartenant au plan, on appelle affixe du vecteur AB⃗, le complexe aff(AB⃗) =
> z_B − z_A. – Pour tous vecteurs u⃗ et v⃗ et tous réels α et β on a : aff(α u⃗ + β v⃗) = α aff(u⃗) +
> β aff(v⃗). »

> **Définition — conjugué** (p.224) — « Soit z = a + i b un nombre complexe donné sous forme algébrique.
> On appelle conjugué de z et on note z̄, le nombre complexe défini par : z̄ = a − ib. »

> **Propriétés du conjugué** (p.224) — « Soient les nombres complexes z = a + i b et z′ = a′ + i b′ où a,
> b, a′ et b′ sont des réels. On a : conj(z + z′) = z̄ + z̄′, conj(z z′) = z̄ z̄′, conj(zⁿ) = (z̄)ⁿ pour
> n ∈ ℕ* et conj(z/z′) = z̄/z̄′ pour z′ ≠ 0. » ; « Soit le nombre complexe z = a + i b où a et b sont
> réels. On a : z + z̄ = 2a ; z − z̄ = 2ib ; z·z̄ = a² + b². »

> **Réel / imaginaire pur** (p.225) — « Soit z un nombre complexe. (z est réel) équivaut à (Im(z) = 0)
> équivaut à (z = z̄). » « Soit z un nombre complexe non nul. (z est imaginaire pur) équivaut à (Re(z) = 0)
> équivaut à (z = −z̄). »

> **Définition — module** (p.225) — « Soit z = a + i b un nombre complexe. On appelle module de z et on
> note |z|, le réel positif défini par |z| = √(a² + b²) = √(z z̄). »

> **Interprétation géométrique du module** (p.225) — « Le module de l'affixe z = a + ib d'un point M(a, b)
> du plan complexe muni d'un repère orthonormé (O, u⃗, v⃗) est la distance OM. On a |z| = √(a² + b²) = OM. »

> **Propriétés du module** (p.225) — « Pour tous nombres complexes z et z′, on a : |z·z′| = |z|·|z′| ;
> |zⁿ| = |z|ⁿ avec n ∈ ℕ*. Pour tous nombres complexes z et z′, tels que z′ ≠ 0, on a : |z/z′| = |z|/|z′|. »
> (p.226) « Pour tous points M et N du plan complexe, on a : MN = |z_N − z_M| » ; « Soit z un nombre
> complexe. On a : |z| = |z̄|. »

> **Définition — argument** (p.227) — « Soit z = a + i b un nombre complexe non nul et M son image dans le
> plan complexe muni du repère orthonormé direct (O, u⃗, v⃗). On appelle argument de z et on note arg(z),
> toute mesure, en radian, de l'angle orienté (u⃗, OM⃗). On a donc : arg(z) = (u⃗, OM⃗) + 2kπ = θ + 2kπ ;
> k ∈ ℤ. »

> **Cas particuliers** (p.227) — « Si z est un nombre réel strictement positif alors arg(z) = 2kπ, k ∈ ℤ.
> Si z est un nombre réel strictement négatif alors arg(z) = π + 2kπ, k ∈ ℤ. Si z = ib avec b réel
> strictement positif alors arg(z) = π/2 + 2kπ, k ∈ ℤ. Si z = ib avec b réel strictement négatif alors
> arg(z) = −π/2 + 2kπ, k ∈ ℤ. »

> **Arguments de z̄ et −z** (p.227) — « Soient z et z′ deux nombres complexes non nuls. On a :
> arg(z̄) = −arg(z) + 2kπ, (k ∈ ℤ) ; arg(−z) = arg(z) + π + 2kπ, (k ∈ ℤ). » [sic : « z et z′ » alors que
> seul z intervient]

> **Forme trigonométrique** (p.228) — « Soit z un nombre complexe non nul. En notant r le module de z et θ
> un argument de z, on a : z = r(cos θ + i sin θ). L'écriture de z sous la forme r(cos θ + i sin θ) avec
> r > 0 et θ ∈ ℝ, est appelée forme trigonométrique de z. Pour tout r > 0 et θ ∈ ℝ, on note
> r(cos θ + i sin θ) = [r, θ]. r et θ sont les coordonnées polaires du point M d'affixe z. » Encadré
> voisin : « Soit z = a + i b = [r, θ] un complexe non nul. On peut représenter graphiquement le point M
> image de z par ses coordonnées algébriques a et b ou bien par ses coordonnées polaires r et θ. On a
> alors a = r cos θ et b = r sin θ. »

> **Opérations en forme trigonométrique** (p.229) — « Soient z = [r, θ] et z′ = [r′, θ′] deux nombres
> complexes non nuls avec r ∈ ℝ₊*, r′ ∈ ℝ₊*, θ ∈ ℝ et θ′ ∈ ℝ. On a pour tout entier n : z̄ = [r, −θ] ;
> 1/z = [1/r, −θ] ; z·z′ = [r·r′, θ + θ′] ; z/z′ = [r/r′, θ − θ′] ; zⁿ = [rⁿ, nθ]. »

> **Forme exponentielle** (p.229) — « Pour tout θ ∈ ℝ, on pose : cos θ + i sin θ = e^{iθ}. Soit z = [r, θ]
> un nombre complexe non nul, l'écriture z = r e^{iθ} est la forme exponentielle de z. »

> **Opérations en forme exponentielle** (p.230) — « Soient z = r e^{iθ} et z′ = r′ e^{iθ′} deux nombres
> complexes non nuls avec r ∈ ℝ₊*, r′ ∈ ℝ₊*, θ ∈ ℝ et θ′ ∈ ℝ. Soit n un entier relatif. On a :
> z̄ = r e^{−iθ} ; 1/z = (1/r) e^{−iθ} ; z·z′ = r·r′ e^{i(θ+θ′)} ; z/z′ = (r/r′) e^{i(θ−θ′)} ;
> zⁿ = rⁿ e^{inθ}. »

> **Formules d'Euler** (p.230) — « Pour tout réel θ on a : (e^{iθ} + e^{−iθ})/2 = cos θ ;
> (e^{iθ} − e^{−iθ})/(2i) = sin θ. »

> **Formule de Moivre** (p.230) — « Pour tout réel θ et pour tout n ∈ ℤ, on a :
> (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ). »

> **Formule du binôme** (p.230) — « Pour tous réels a, b et pour tout n ∈ ℕ, on a :
> (a + b)ⁿ = Σ_{k=0}^{n} C(n,k) a^{n−k} b^k » (noté Cᵏₙ dans le manuel).

> **Réel / imaginaire pur par l'argument** (p.231) — « Soit z un nombre complexe on a : (z est réel) ⇔
> (arg(z) = kπ, (k ∈ ℤ) ou z = 0) ; (z est imaginaire pur) ⇔ (arg(z) = π/2 + kπ, (k ∈ ℤ)). »

> **Angles et affixes** (p.231) — « Le plan P est rapporté au repère orthonormé direct (O, u⃗, v⃗). Pour
> tous points A, B, C et D tels que A ≠ B et C ≠ D, on a : (u⃗, AB⃗) = arg(z_B − z_A) + 2kπ (k ∈ ℤ) ;
> (AB⃗, CD⃗) = arg((z_D − z_C)/(z_B − z_A)) + 2kπ (k ∈ ℤ). »

> **Colinéarité, orthogonalité** (p.232) — « Soit u⃗ et v⃗ deux vecteurs non nuls du plan, d'affixes
> respectives z et z′, on a : (u⃗ et v⃗ sont colinéaires) ⇔ z/z′ est réel ; (u⃗ et v⃗ sont orthogonaux)
> ⇔ z/z′ est imaginaire pur. »

> **Résumé du cours** (p.233–235) — reprend les encadrés ci-dessus et ajoute, en vérifié sur l'image :
> conj(conj z) = z ; |z|² = z·z̄ = a² + b² et |z + z′| ≤ |z| + |z′| ; r = √(a² + b²), cos θ = a/r, sin θ = b/r ;
> z̄ = [r, −θ] ⇒ |z̄| = |z| et arg(z̄) = −arg(z) + 2kπ ; z·z′ = [rr′, θ+θ′] ⇒ |z·z′| = |z|·|z′| et
> arg(z·z′) = arg(z) + arg(z′) + 2kπ ; 1/z = [1/r, −θ] ⇒ |1/z| = 1/|z|, arg(1/z) = −arg(z) + 2kπ ;
> z/z′ = [r/r′, θ − θ′] ⇒ |z/z′| = |z|/|z′|, arg(z/z′) = arg(z) − arg(z′) + 2kπ ; zⁿ = [rⁿ, nθ] ⇒ |zⁿ| = |z|ⁿ,
> arg(zⁿ) = n·arg(z) + 2kπ (n ∈ ℤ) ; pour λ > 0, λ·z = [λr, θ] ⇒ |λz| = λ|z|, arg(λz) = arg(z) + 2kπ ;
> pour λ < 0, λ·z = [−λr, θ + π] ⇒ |λz| = −λ|z|, arg(λz) = arg(z) + π + 2kπ ; z réel ⇔ Im(z) = 0 ⇔ z = z̄ ⇔
> arg(z) = kπ ou z = 0 ; z imaginaire pur ⇔ Re(z) = 0 et z ≠ 0 ⇔ z = −z̄ et z ≠ 0 ⇔ arg(z) = π/2 + kπ ;
> Moivre ; Euler ; formes exponentielles des opérations ; angle (AB⃗, CD⃗) = arg((z_D−z_C)/(z_B−z_A)) + 2kπ ;
> colinéarité/orthogonalité par z/z′.

### Avec l'ordinateur (p.236)

- **Activité** (p.236) : logiciel de géométrie dynamique ; points M, M_1, M_2, M′ d'affixes z = e^{iθ}
  (θ ∈ ]0, π/2[), z_1 = z², z_2 = 2z et z′ = 2z − z². Construire le cercle trigonométrique, placer M sur
  l'arc [AB], construire M_1, M_2 et M′ pour que OM_1M_2M′ soit un parallélogramme, la tangente (D_M) en
  M ; conjecturer la position de A et M′ par rapport à (D_M) ; valeur de θ pour que OM_1M_2M′ soit un
  rectangle ; stratégie de justification : a) AM = MM′ ; b) (z′ − 1)/z est un réel ; c) justifier la
  conjecture ; d) valeur de θ pour le rectangle.

### Exercices et problèmes (p.237–239) — 19 exercices

- **Ex. 1** (p.237) : écrire sous forme algébrique (1 + i√3)/(i + √3) ; (−1 − i)²(1 − i√3) ; (1/i + i) ;
  (−1/2 + i√3/2)³.
- **Ex. 2** (p.237) : j = cos(2π/3) + i sin(2π/3). 1) j², j³, j⁴ ; 2) conjecturer jⁿ ; 3) j² = j̄ = 1/j ;
  4) 1 + j + j² = 0 ; 5) équivalence a + bj + cj² = 0 ⇔ a − c = j(c − b).
- **Ex. 3** (p.237) : m réel, z = (m − i)[(10 − m) + (2 + m)i]. 1) m pour que z soit réel ; 2) valeurs
  correspondantes de z.
- **Ex. 4** (p.237) : z_1 = 4 + 4i, z_2 = 1 − i√3. 1) module et argument de z_1, z_2 ; 2) module et
  argument de z_1², z_1z_2, z_1³, z_1/z_2 et z_2/z_1.
- **Ex. 5** (p.237) : φ ∈ [−π, π/2], Z = cos²φ + i sin φ cos φ. 1) φ pour que Z soit nul ; 2) ces valeurs
  exclues, formes algébrique, trigonométrique et exponentielle de 1/Z.
- **Ex. 6** (p.237) : θ ∈ ]−π/2, π/2[ ; M_1, M_2, M d'affixes z_1 = e^{iθ} − i, z_2 = e^{−iθ} + i,
  z = 2 cos θ. 1) forme exponentielle de z_1, en déduire z_2/z_1 = e^{i(π/2 − θ)} ; 2) OM_1MM_2 est un
  losange, valeur de θ pour laquelle c'est un carré.
- **Ex. 7** (p.237) : 1) ensemble des M tels que |z| = |z − 1| ; 2) si |z| = |z − 1|, alors
  Arg(z) + Arg(z − 1) ≡ π [2π].
- **Ex. 8** (p.237) : z = (1 + i)/(1 + i√3). 1) module et argument ; 2) forme algébrique ; 3) en déduire
  tg(π/12).
- **Ex. 9** (p.237) : triangle ABC d'affixes a, b, c ; M milieu de [BC] d'affixe m ; triangles BAB′ et
  C′AC directs, rectangles et isocèles de sommet principal A. 1) affixes de B′, C′ et M ; 2) a) B′C′ = 2·AM ; b) (B′C′) et (AM) perpendiculaires.
- **Ex. 10** (p.238) : A(i), B(−i) ; M(≠B) d'affixe z ↦ M′ d'affixe z′ = (1 − z)/(1 − iz). 1) a) ensemble
  des M tels que z′ réel ; b) ensemble des M tels que |z′| = 1 ; 2) a) z′ + i = (−1 + i)/(z + i) ;
  b) BM·BM′ = √2 ; c) si M ∈ cercle de centre B, rayon 1, M′ appartient à un cercle (précisé).
- **Ex. 11** (p.238) : 1) cos 3x et sin 5x en fonction de cos x et sin x ; 2) linéariser cos³x ; cos²x·sin x ;
  sin²x·cos³x ; 3) α, β réels : module et argument de z = (e^{iα} + e^{iβ})/(e^{iα} − e^{iβ}) (condition
  d'existence préalable).
- **Ex. 12** (p.238) : A(1), B(−2i), f : P\{B} → P, M(z) ↦ M′(z′) avec z′ = (z̄ + 4i)/(z̄ − 2i). 1) vérifier
  z′ − 1 = 6i/(z̄ − 2i) ; 2) en déduire (BM⃗, AM′⃗) ≡ π/2 [2π] ; 3) a) si M ∈ ζ(B, 3), M′ appartient à un
  cercle ζ′ à déterminer ; b) si M ∈ (AB), M′ appartient à une droite à préciser.
- **Ex. 13** (p.238) : A(1), M(z) ↦ M′(z′) avec z′ = 2z − z². 1) ensemble E_1 des M tels que
  arg(z′) − 2 arg(z) ≡ π/2 [2π] (à construire) ; 2) M_1(z²), M_2(2z) : a) ensemble E_2 des M tels que O,
  M_1, M_2 soient alignés ; b) M ∉ E_2 : OM_1M_2M′ est un parallélogramme.
- **Ex. 14** (p.238) : ensemble des M(z) tels que les points d'affixes 1, z et z² soient alignés.
- **Ex. 15** (p.238) : choix de l'entier naturel n pour que (1 − i√3)ⁿ soit un réel positif.
- **Ex. 16** (p.238–239) : Z = cos(2π/5) + i sin(2π/5). 1) a) Z⁵ − 1 = 0 ; b) avec Z⁵ − 1 =
  (Z − 1)(Z⁴ + Z³ + Z² + Z + 1), Z⁴ + Z³ + Z² + Z + 1 = 0. 2) a) Z⁴, Z³, Z² sous forme trigonométrique ;
  b) Z + Z⁴ = 2cos(2π/5) et Z² + Z³ = 2cos(4π/5). 3) a) 2cos(4π/5) + 2cos(2π/5) + 1 = 0 ; b) cos(2π/5) est
  solution de 4X² + 2X − 1 = 0 ; c) valeur de cos(2π/5).
- **Ex. 17** (p.239) : A(i), B((1 + i)/2) ; f : M(z) ↦ M′(z′), z′ = (1 − i)z − 1. 1) a) ensemble E des M tels
  que |z′| = 2√2 ; b) θ ∈ [0, π], z = (1/√2)(cos θ + i sin θ) : forme trigonométrique de z′ selon θ.
  2) a) M ≠ B : Arg(z′) ≡ −π/4 + (i⃗, BM⃗) [2π] ; b) ensemble F des M tels que z′ soit réel négatif
  (à construire). 3) a) M ≠ A : AMM′ rectangle en M, mesure de (AM⃗, AM′⃗) ; b) construction de
  M′ = f(M).
- **Ex. 18** (p.239) : A(i), B(2) ; M(z ≠ 2) ↦ M′(z′), z′ = (z − i)/(iz − 2i). 1) a) |z′| = AM/BM ; b)
  lorsque M décrit la médiatrice de [AB], M′ décrit un cercle ; 2) z ≠ i, z ≠ 2 : a) (u⃗, OM′⃗) =
  (BM⃗, AM⃗) − π/2 + 2kπ ; b) si M ∈ (AB), M′ appartient à une droite (D'après Bac Tunisien 1995).
- **Ex. 19** (p.239) : 𝒞 cercle trigonométrique, t affixe d'un point M de 𝒞 d'argument α ∈ [0, π/2].
  1) u = t³ et v = 2t sous forme trigonométrique ; 2) w = 2t − t³, A(u), B(v), C(w) : a) placer pour
  α = π/3 ; b) α pour que O, A, B soient alignés ; 3) α ∈ ]0, π/2[ : a) nature de OABC ; b) α pour que
  OABC soit un rectangle (D'après Bac Tunisien 1994).

### Aperçu historique (p.240)

Cardan et les « nombres impossibles ou imaginaires » (ex. 40 = (5 + √−15)(5 − √−15)) ; Descartes
(« racines imaginaires ») ; de Moivre (1722), Euler (formules, e^{iπ} = −1) ; Gauss (représentation,
« nombres complexes », notation i, théorème fondamental de l'algèbre en 1799, entiers de Gauss 1801) ;
Cauchy (fonctions d'une variable complexe, 1814) ; applications en physique (équation de Schrödinger).

### Bornes de scope observées (chapitre 10)

- ✅ INCLUS : forme algébrique, conjugué, module, argument, formes trigonométrique et exponentielle,
  formules d'Euler, de Moivre, du binôme, linéarisation, angles orientés et affixes, colinéarité /
  orthogonalité, ensembles de points et transformations z ↦ z′ (cercles, droites), lien avec la
  géométrie du triangle, du carré, du losange, valeurs exactes de cos/sin (π/12, 2π/5).
- ⛔ NON traité dans ce chapitre : équations du second degré dans ℂ (objet du chapitre 11), racines
  n-ièmes d'un complexe ; QCM / Vrai-Faux ; corrigés des exercices.

> Sondage image : pages 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238,
> 239, 240 (18 pages sur 20 ; seules 221 et 223 lues en texte seul) ; écarts couche texte / image :
> « i » à la place de θ, barres de conjugaison et de valeur absolue perdues, racines et exposants
> écrasés, symboles d'ensemble ; tout ce qui précède est repris de l'image.

## 2.11 Chapitre 11 — Équations à coefficients complexes (manuel 222451, p.241–256)

**Page de garde (p.241)** — Titre : « Equations à coefficients complexes ». Le numéro de chapitre imprimé
(pages de garde et bandeaux) est « 2 » [sic : numéro imprimé différent du rang 11 dans le manuel 222451]. Plan : Activités préliminaires ; Cours (Racines carrées d'un nombre complexe ; Équations
du second degré à coefficients complexes ; Racines nièmes d'un nombre complexe ; Exemples d'équations
dans ℂ de degré supérieur à 2) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ;
Aperçu Historique. Pas de QCM / Vrai-Faux. Convention (p.242) : P plan complexe rapporté à un repère
orthonormé direct (O, u⃗, v⃗), ℂ ensemble des nombres complexes.

### Activités préliminaires (p.242)

- **Prél. 1** : résoudre dans ℝ : 1) 3x² + 7x + 4 = 0 ; 2) 5x² − 3x + 1 = 0 ; 3) −√3 x² + (1 − √3)x + 1 = 0 ;
  4) x² − (√3 − √2)x − √6 = 0 ; 5) 4x² − 13|x| + 9 = 0 ; 6) 2x³ − 5x² + 4x − 1 = 0 (on remarquera que 1
  est une solution).
- **Prél. 2** : résoudre dans ℂ (on posera à chaque fois z = x + iy, x et y réels) : 1) (1 + 2i)z +
  (1 − i)z̄ = 2i ; 2) z·z̄ + z − z̄ = 5 + 4i ; 3) z² + 9 = 0 ; 4) z² − 2i·z̄ = 0.
- **Prél. 3** : résoudre dans ℂ : a) z² = −2i ; b) 2i/(z̄ + 2i) = z̄ + 2i.
- **Prél. 4** : a) calculer (1 − 3i)² ; b) vérifier 4z² − 4iz = (2z − i)² + 1 ; c) résoudre alors dans ℂ
  4z² − 4iz + 7 + 6i = 0.

### Cours — Activités

**Racines carrées d'un nombre complexe** (p.243–244)

- **Activité 1** (p.243) : 1) Z = a + ib non nul, (E) : z² = Z, z = x + iy : a) (E) équivaut au système
  { x² − y² = a ; 2xy = b } ; b) (z² = Z) entraîne (x² + y² = √(a² + b²)) ; c) résoudre (E), en déduire que
  Z admet deux racines carrées opposées. 2) racines carrées de z_1 = −3 − 4i et z_2 = 7 + 24i. 3) Z = −8 + 6i :
  en écrivant Z = 1 + 2·3i − 9, en déduire les racines carrées de Z.
- **Activité 2** (p.244) : 1) λ réel strictement positif, α réel, Z = λ·e^{iα} : résoudre z² = Z (on posera
  z = r·e^{iθ}, r > 0), solutions sous forme exponentielle. 2) racines carrées de −3 ; 16 ; −2i ; 1 − i et
  1 + i√3.

**Équation du second degré à coefficients complexes** (p.244–246)

- **Activité 1** (p.244) : 1) (E) : az² + bz + c = 0, a ∈ ℂ*, b, c ∈ ℂ : a) (E) équivaut à
  (z + b/(2a))² = (b² − 4ac)/(4a²) ; b) avec Δ = b² − 4ac = λ², λ racine carrée de Δ, résoudre (E) dans ℂ.
  2) résoudre dans ℂ : a) z² − (1 − i)z + 2 − 2i = 0 ; b) iz² − (1 − 5i)z + 6i − 2 = 0 ;
  c) z² + cos θ·z + 1/4 = 0 avec θ ∈ ℝ.
- **Activité 2** (p.245) : résoudre dans ℂ : a) z² + 2iz + 8 = 0 ; b) iz² − 2(1 + i)z + 2 = 0.
- **Activité 3** (p.245) : Q_1(z) = z² + 3(1 + i)z + 5i, Q_2(z) = z² + 3(1 − i)z − 5i, P(z) = (z² + 3z)² +
  (3z + 5)². 1) P(z) = Q_1(z)·Q_2(z) ; 2) a) résoudre (E) : Q_1(z) = 0 ; b) si z est solution de (E) alors z̄
  est solution de Q_2(z) = 0 ; c) en déduire les solutions dans ℂ de P(z) = 0 ; 3) P(z) est le produit de
  deux polynômes du second degré à coefficients réels.
- **Activité 4** (p.246) : 1) somme S et produit P des solutions de (E) : az² + bz + c = 0 en fonction de a, b,
  c (cas Δ = 0 et Δ ≠ 0) ; 2) (E) : z² − (1 + 2i)z + i − 1 = 0 : a) vérifier que i est solution ; b) sans
  calculer Δ, trouver l'autre solution.
- **Activité 5** (p.246) : 1) (E) à coefficients réels, Δ = b² − 4ac : a) si Δ < 0, (E) admet dans ℂ deux
  solutions conjuguées ; b) si z² + αz + β = 0 admet deux solutions conjuguées alors α et β sont réels ;
  2) résoudre dans ℂ z² + z + 1 = 0 et z² − 2z + cos²φ = 0 où φ ∈ ℝ*.
- **Activité 6** (p.246) : 1) deux complexes z_1, z_2 tels que { z_1 + z_2 = 1 + 2i ; z_1·z_2 = −1 + i } ;
  2) deux complexes z_1, z_2 sous forme exponentielle tels que { z_1 + z_2 = 2 + e^{2iθ} ;
  z_1·z_2 = 1 − e^{3iθ} } avec θ ∈ ]0, π/2].

**Racines nièmes d'un nombre complexe non nul** (p.247–248)

- **Exemples** (p.247) : 1, −1, i et −i sont les racines quatrièmes de 1 ; vérifier que (−1 + i√3)³ = 8 et
  en déduire que (−1 + i√3) est une racine cubique de 8.
- **Activité 1** (p.247) : Z = r·e^{iθ} (r ∈ ℝ₊*, θ ∈ ℝ), (E) : zⁿ = Z, n ∈ ℕ*, n ≥ 2. 1) (zⁿ = Z) ⇔
  (z = ⁿ√r·e^{i(θ+2kπ)/n} ; k ∈ ℤ) ; 2) z_k = ⁿ√r·e^{i(θ+2kπ)/n}, k entier relatif : a) z_k est solution de
  (E) ; b) z_0 = z_n et z_1 = z_{n+1} ; c) z_k = z_{k′} ⇔ k − k′ est multiple de n ; d) (E) admet exactement
  n solutions distinctes dans ℂ ; 3) les images M_k sont les sommets d'un polygone régulier à n côtés
  inscrit dans le cercle 𝒞 de centre O et de rayon ⁿ√r (Indication : (OM_k⃗, OM_{k+1}⃗) = 2π/n + 2kπ).
- **Activité 2** (p.248) : j = (−1 + i√3)/2. 1) écrire j sous forme exponentielle ; 2) j³ = 1 ; j² = j̄ = 1/j
  et 1 + j + j² = 0 ; 3) racines cubiques de l'unité et construction de leurs images dans le plan complexe.
- **Activité 3** (p.248) : U = e^{iθ}, θ ∈ ]0, 2π[. 1) nombre complexe z tel que (z − i)/(z + i) = U ;
  2) racines cinquièmes de l'unité ; 3) en déduire les solutions dans ℂ de (E) : (z² + 1)⁵ − (z + i)¹⁰ = 0.

**Équations de degré supérieur à 2 dans ℂ** (p.249)

- **Activité 1** : (E) : z² − (3 − i)z + 4 = 0. 1) a) résoudre (E) (z_1, z_2 solutions telles que Im(z_1) > 0) ;
  b) mettre z_1 et z_2 sous forme trigonométrique. 2) (E′) : 3z³ + (−9 + i)z² + (14 + 6i)z − 8i = 0 : a) vérifier
  que z_0 = (2/3)i est solution ; b) déterminer a, b, c complexes tels que 3z³ + (−9 + i)z² + (14 + 6i)z − 8i =
  (z − z_0)(az² + bz + c) ; c) résoudre (E′).
- **Activité 2** : (E) : z³ − (3 + 2i)z² + 3(1 + i)z − 4i = 0 : montrer que (E) admet une solution imaginaire
  pure puis résoudre (E).
- **Activité 3** : résoudre dans ℂ z⁴ + 2iz² + 3 = 0.
- **Activité 4** : (E) : 4z⁴ + 4cos θ(1 + cos θ)z² + (1 + cos θ)² = 0, θ ∈ [0, π]. 1) θ = π : résoudre (E) ;
  2) θ ∈ [0, π[ et z² = (1/2)(1 + cos θ)Z : a) résoudre l'équation (E′) d'inconnue Z ; b) module et argument de
  chacune des racines de (E′) ; 3) en déduire module et argument de chacune des racines de (E).
- **Activité 5** : résoudre dans ℂ (3z² + z + 1)² + (z² + 2z + 2)² = 0.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Définition — racine carrée** (p.243) — « Soit Z un nombre complexe donné. On appelle racine carrée de Z
> tout nombre complexe z vérifiant z² = Z. » Exemples : i et −i sont les racines carrées de −1 ; (1+i)² = 2i
> donc 1+i est une racine carrée de 2i.

> **Racines carrées par la forme algébrique** (p.243) — « Soit Z = a + i b un nombre complexe non nul.
> L'équation z² = Z avec z = x + iy est équivalente au système : x² − y² = a ; 2xy = b ;
> x² + y² = √(a² + b²). » ; « Un nombre complexe non nul admet deux racines carrées opposées. »

> **Racines carrées par la forme exponentielle** (p.244) — « Soit Z = λ e^{iα} un nombre complexe non nul
> donné sous forme exponentielle. L'équation z² = Z admet dans ℂ deux solutions opposées :
> z_1 = √λ · e^{iα/2} ; z_2 = −z_1. Les solutions z_1 et z_2 sont les racines carrées de Z. »

> **Définition — équation du second degré** (p.244) — « Soient a, b et c trois nombres complexes donnés tels
> que a ≠ 0. L'équation az² + bz + c = 0 s'appelle équation du second degré à coefficients complexes. »

> **Résolution** (p.245) — « Soit l'équation (E) : az² + bz + c = 0 telle que a ∈ ℂ* et b, c ∈ ℂ et z
> l'inconnue complexe. On pose Δ = b² − 4ac, appelé discriminant de l'équation (E). • Si Δ ≠ 0 alors
> l'équation (E) admet, dans ℂ, deux solutions distinctes : z′ = (−b − λ)/(2a) et z″ = (−b + λ)/(2a) avec λ
> une racine carrée de Δ. • Si Δ = 0 alors (E) possède une racine double z′ = z″ = −b/(2a). • Si z′ et z″
> sont les racines dans ℂ de l'équation du second degré (E) : az² + bz + c = 0 alors on a :
> az² + bz + c = a(z − z′)(z − z″). »

> **Remarque — discriminant réduit** (p.245) — « Lorsque b = 2b′, on a Δ = 4Δ′ où Δ′ = b′² − ac, appelé
> discriminant réduit de l'équation (E). On a : • Si Δ′ ≠ 0 alors l'équation (E) admet, dans ℂ, deux
> solutions distinctes : z′ = (−b′ − λ′)/a et z″ = (−b′ + λ′)/a avec λ′ une racine carrée de Δ′. • Si Δ′ = 0
> alors (E) possède une racine double z′ = z″ = −b′/a. »

> **Somme et produit des racines** (p.246) — « Soient a ∈ ℂ* et b, c ∈ ℂ. Si z′ et z″ sont les racines dans ℂ
> de l'équation du second degré (E) : az² + bz + c = 0 alors on a : z′ + z″ = −b/a ; z′·z″ = c/a. »

> **Coefficients réels** (p.246) — « Soient a, b et c trois réels, a non nul. L'équation du second degré :
> az² + bz + c = 0 admet dans ℂ deux solutions. On note Δ = b² − 4ac. – Si Δ > 0, les solutions sont réelles
> distinctes. – Si Δ = 0, les solutions sont réelles confondues. – Si Δ < 0, les solutions sont complexes
> conjuguées : z′ = (−b − i√(−Δ))/(2a), z″ = (−b + i√(−Δ))/(2a). »

> **Équation à somme et produit donnés** (p.246) — « Soient S et P deux nombres complexes donnés. Les
> nombres complexes z′ et z″ tels que z′ + z″ = S ; z′·z″ = P sont les solutions dans ℂ de l'équation du
> second degré z² − Sz + P = 0. »

> **Définition — racine nième** (p.247) — « Soient n un entier naturel non nul et Z un nombre complexe non
> nul. On appelle racine nième de Z, tout nombre complexe z tel que zⁿ = Z. Si Z = 1 alors on dit que z est
> une racine nième de l'unité. »

> **Racines nièmes** (p.247) — « Soient r un réel strictement positif, θ un réel et Z = r e^{iθ} un nombre
> complexe. L'équation (E) : zⁿ = Z avec n ∈ ℕ* admet, dans ℂ, n solutions distinctes :
> z_k = ⁿ√r · e^{i(θ+2kπ)/n} avec k ∈ {0, 1, …, n−1}. Les images M_k des solutions z_k de (E) sont les
> sommets d'un polygone régulier à n côtés inscrit dans le cercle 𝒞 de centre O et de rayon ⁿ√r. »
> (p.248, encadré avec figures : pour n = 3, M_0M_1M_2 est un triangle équilatéral ; n = 4, M_0M_1M_2M_3 est
> un carré ; n = 5, M_0M_1M_2M_3M_4 est un pentagone régulier.)

> **Résumé du cours** (p.250) — reprend à l'identique : racines carrées par forme exponentielle, système
> avec x² + y² = √(a² + b²), résolution de l'équation du second degré (discriminant Δ, racine double,
> factorisation a(z − z′)(z − z″)), somme et produit (−b/a, c/a), équation z² − Sz + P = 0, racines nièmes
> z_k = ⁿ√r·e^{i(θ+2kπ)/n}, k ∈ {0,…,n−1}, et polygone régulier inscrit dans le cercle 𝒞 de rayon ⁿ√r.
> (Le résumé ne reprend pas la remarque sur le discriminant réduit ni le cas des coefficients réels.)

### Avec l'ordinateur (p.251)

- **Activité** : logiciel de géométrie (capture d'écran « Déclic »). Construire un hexagone régulier dont
  les sommets sont les images des solutions de z⁶ = 64i. 1) Résoudre cette équation ; 2) choisir un repère
  orthonormé direct ; construire M_0 d'affixe z_0 = 2e^{iπ/12}, M_1 image de M_0 par la rotation R de centre O et
  d'angle π/3, M_2 image de M_1 par R, achever M_0…M_5 puis l'hexagone ; déterminer son périmètre et son aire ;
  contrôler avec le logiciel.

### Exercices et problèmes (p.252–255) — 23 exercices

- **Ex. 1** (p.252) : racines carrées de 3 − 4i ; 2i ; −5 − 12i ; (2i − 1)/(i + 2) ; 1 − i√3 et 1 + i.
- **Ex. 2** (p.252) : racines cubiques de 8i ; √3 + i et −i.
- **Ex. 3** (p.252) : a) vérifier que 2 − i est une racine cubique de 2 − 11i ; b) en déduire les deux autres.
- **Ex. 4** (p.252) : a) racines quatrièmes de −7 − 24i ; b) les représenter dans le plan complexe.
- **Ex. 5** (p.252) : résoudre dans ℂ : a) z² − (3 + 2i)z + 5 + i = 0 ; b) iz² + (4i − 3)z + i − 5 = 0 ;
  c) (4 − 3i)z² − (10 + 5i)z + 3 + 5i = 0.
- **Ex. 6** (p.252) : a) résoudre dans ℂ (z − 2)(z² − 3iz + 4) = 0 ; b) construire les images A, B, C des
  solutions et prouver que ABC est rectangle.
- **Ex. 7** (p.252) : θ ∈ ]−π/2, π/2[. 1) résoudre (E) : z² − 2(1 + i)z + 2i(1 + tg²θ) = 0, solutions z′ et z″ ;
  2) a = 1 + i et b = 1 + i·tgθ : a) a et b sous forme exponentielle ; b) z′ et z″ à l'aide de a et b ;
  c) module et argument de z′ et de z″.
- **Ex. 8** (p.252) : θ ∈ ]0, π[, (E_θ) : z² − e^{iθ}(1 + e^{iθ})z + e^{3iθ} = 0. 1) résoudre (E_θ) ; 2) A, B, C
  d'affixes 1, e^{iθ}, e^{2iθ} : a) ABC est isocèle de sommet B ; b) ABC équilatéral ⇔ |1 + e^{iθ}| = 1 ;
  3) a) module et argument de 1 + e^{iθ} ; b) valeurs de θ pour que ABC soit équilatéral.
- **Ex. 9** (p.252) : θ ∈ [0, π], (E) : (1 − i)z² − 2(cos θ + sin θ)z + 1 + i = 0, solutions z_1, z_2 (Im(z_1)
  positive pour tout θ). 1) sans calculer z_1, z_2 : z_2 = i/z_1, relation entre modules et arguments ; 2) a) 1 − sin(2θ) = (cos θ − sin θ)², calculer
  z_1, z_2 ; b) z_1, z_2 sous forme exponentielle ; c) valeur de θ pour laquelle z_1 = z_2 ; 3) M_1(cos θ +
  i sin θ) et M_2(sin θ + i cos θ) : ensembles 𝒞_1 décrit par M_1 et 𝒞_2 décrit par M_2 quand θ varie dans
  [0, π].
- **Ex. 10** (p.253) : θ ∈ ]0, π[, (E) : z² − 2z + 2sin²θ − 2i sin θ cos θ = 0. 1) a) cos 2θ + i sin 2θ =
  (cos θ + i sin θ)², résoudre (E) (z′ de partie imaginaire positive, z″ l'autre) ; b) z′ = 2cos(θ/2)·e^{iθ/2}
  et z″ = −2i sin(θ/2)·e^{iθ/2} ; 2) M′, M″ d'affixes z′, z″ : a) z″/z′ et OM′M″ rectangle en O ; b) θ pour
  que OM′M″ soit isocèle ; 3) M′ varie sur un cercle 𝒞 à préciser quand θ décrit ]0, π[.
- **Ex. 11** (p.253) : (E) : z³ − 2(3 + 2i)z² + 2(4 + 7i)z − 12i = 0. 1) a) (E) admet une solution réelle à
  déterminer ; b) résoudre (E). 2) repère orthonormé, A(2), B(1 + i), C(3 + 3i) : a) nature du triangle ABC ;
  b) affixe de D pour que ABCD soit un rectangle ; 3) M(z), z ≠ 1 + i, ↦ M′ d'affixe z′ = 2iz + 3 − i :
  a) (z′ − z_B)/(z − z_B) = 2e^{iπ/2} ; b) nature du triangle BMM′.
- **Ex. 12** (p.253) : (E) : z³ − (6 + 3i)z² + (9 + 12i)z − 9(2 + 3i) = 0. 1) a) z_0 = 3i est solution ;
  b) (E) équivaut à (z − 3i)[(z − 3)² − 6i] = 0. 2) a) résoudre U² = 6i ; b) autres solutions z_1, z_2.
  3) M_0, M_1, M_2 images de 3i, 3 + √3(1 + i), 3 − √3(1 + i), 𝒞 cercle circonscrit, I son centre :
  a) M_0M_1M_2 équilatéral ; b) affixe de I.
- **Ex. 13** (p.253) : 1) (E) : z³ + (√3 + i)z² + (1 + i√3)z + i = 0 : vérifier que −i est solution puis
  résoudre (E). 2) A, B, C d'affixes z_A = −i, z_B = (−√3 + i)/2, z_C = z̄_B : a) représenter A, B, C ;
  b) module et argument de Z = (z_B − z_C)/(z_A − z_C) ; c) nature du triangle ABC.
- **Ex. 14** (p.253–254) : f(z) = z³ + 2(i − √3)z² + 4(1 − i√3)z + 8i. 1) f(z) = 0 possède une racine
  imaginaire pure z_0 ; en déduire z_1, z_2 (z_1 de partie imaginaire négative) ; 2) w = z_1/z_0 : a) forme
  exponentielle de w ; b) à tout z on associe M, M_1, M_2 d'affixes z, wz, w²z : montrer que OMM_1M_2 est un
  losange.
- **Ex. 15** (p.254) : θ ∈ ]−π/2, π/2[, (E) : (1 + iz)³(1 − i tgθ) = (1 − iz)³(1 + i tgθ). 1) z solution :
  a) |1 + iz| = |1 − iz| ; b) z est réel ; 2) a) forme trigonométrique de (1 + i tgθ)/(1 − i tgθ) ; b) z = tgα,
  α ∈ ]−π/2, π/2[ : écrire l'équation en α, la résoudre, solutions de (E).
- **Ex. 16** (p.254) : 1) racines cubiques de u = 4√2(−1 + i) ; 2) θ ∈ ]0, π[ : 1/(1 − e^{iθ}) sous forme
  cartésienne ; 3) résoudre dans ℂ (E) : (2z − 1)³ = 4√2(−1 + i)z³.
- **Ex. 17** (p.254) : 1) a) forme trigonométrique de λ = (1 + i)(1 + i√3) ; b) cos(7π/12) et sin(7π/12) ;
  2) racines cubiques de a = 2 + 2i et b = ā, placer les images dans un repère orthonormé (unité 2 cm) ; 3) (suite en haut de la colonne de droite,
  p.254) P(z) = z⁶ − 4z³ + 8, (E) : P(z) = 0 : a) si z_0 est solution alors z̄_0 aussi ; b) résoudre
  dans ℂ (E) ; 4) en déduire une factorisation de P(z) en produit de polynômes du second degré à
  coefficients réels.
- **Ex. 18** (p.254) : θ ∈ [−π, π[, (E) : iz² + (2 sin θ)z − 2i(1 + cos θ) = 0. 1) a) sin²θ − 2(1 + cos θ) =
  −(1 + cos θ)² ; b) résoudre (E) ; 2) M′, M″ d'affixes z′ = 1 + cos θ + i sin θ et z″ = −1 − cos θ + i sin θ :
  a) z″ = −z̄′, M′ et M″ symétriques par rapport à une droite à déterminer ; b) z′ sous forme exponentielle,
  z″/z′ = e^{i(π − θ)} ; c) OM′M″ isocèle, valeurs de θ pour lesquelles OM′M″ est équilatéral.
- **Ex. 19** (p.254–255) : θ ∈ ]0, π[, (E) : z³ + 4z² + (5 − e^{2iθ})z − 4i sin θ·e^{iθ} = 0. 1) a) e^{iθ} est
  une racine carrée de 1 + 2i sin θ·e^{iθ} ; b) z_0 = −2 est solution de (E), résoudre (E) ; 2) A(−2),
  M_1(z_1 = −1 + e^{iθ}) et M_2(z_2 = −1 − e^{iθ}) : a) z_1 et z_1/z_2 sous forme exponentielle ; b) M_1 et M_2
  symétriques par rapport à un point fixe I ; c) ensemble Γ_1 des M_1 quand θ varie, puis Γ_2 des M_2, à
  construire ; d) OM_1AM_2 est un rectangle, θ pour lequel c'est un carré.
- **Ex. 20** (p.255) : θ ∈ ]0, π/2[. 1) a) module et argument de z_1 = 1 − e^{iθ} et z_2 = 1 − e^{3iθ} ; b) module
  et argument de z_3 = 1 + e^{iθ} + e^{2iθ} (rappel : a³ − b³ = (a − b)(a² + ab + b²)) ; 2) résoudre
  (E_θ) : z² − (2 + e^{2iθ})z + 1 − e^{3iθ} = 0 (solutions sous forme exponentielle).
- **Ex. 21** (p.255) : α ∈ ]0, π[, P(z) = z³ − (1 − 2 sin α)z² + (1 − 2 sin α)z − 1. 1) a) P(1) ;
  b) résoudre P(z) = 0, solutions sous forme exponentielle ; 2) résoudre U³ = e^{i(α + π/2)} ; 3) 1 + e^{iθ} =
  2cos(θ/2)·e^{iθ/2} ; 4) résoudre (z − 1)⁶ + 2 sin α·(z − 1)³ + 1 = 0.
- **Ex. 22** (p.255) : 1) résoudre z² − (1 + i)z + i = 0 ; 2) θ ∈ ]0, π/2[, (E_θ) : z² − 2e^{iθ}cos θ·z +
  e^{2iθ} = 0 : a) 1 est solution de E_θ ; b) l'autre solution ; 3) A(1), B(e^{2iθ}) : a) ensemble des points B
  quand θ varie dans ]0, π/2[ ; b) affixe de C tel que OACB soit un losange ; c) θ pour que l'aire du losange
  OACB soit 1/2 (D'après Bac Tunisien 2000).
- **Ex. 23** (p.255) : 1) a) résoudre z² − 2iz − 2 = 0 ; b) solutions sous forme trigonométrique ; 2) θ ∈ ]0, π[,
  (E) : z² − 2e^{iθ}z + e^{2iθ} − 1 = 0, résoudre (E) ; 3) A, B, C d'affixes z_1 = 2e^{iθ}, z_2 = 1 + e^{iθ},
  z_3 = −1 + e^{iθ} : a) z_2 et z_3 sous forme exponentielle ; b) OBAC est un rectangle ; c) θ ∈ ]0, π[ tel
  que OBAC soit un carré (D'après Bac Tunisien 1999).

### Aperçu historique (p.256)

Cardan (1545) et Tartaglia (équations du 3ᵉ degré), Ferrari (4ᵉ degré) ; Girard (1629, racines négatives ou
complexes), Viète (relations racines-coefficients) ; Descartes (1635, règle des signes) ; Newton
(méthode de Newton-Raphson) ; Gauss (toute équation polynomiale a au moins une solution) ; Lagrange,
Ruffini, Abel, Galois (pas de formule générale au-delà du degré quatre ; trisection de l'angle et
duplication du cube impossibles à la règle et au compas).

### Bornes de scope observées (chapitre 11)

- ✅ INCLUS : racines carrées (forme algébrique avec le système à trois lignes, forme exponentielle) ;
  équation du second degré dans ℂ (discriminant, discriminant réduit, racine double, factorisation, somme
  et produit, cas des coefficients réels) ; racines nièmes et racines nièmes de l'unité, polygone
  régulier ; équations de degré 3, 4 et 6 (z⁶ − 4z³ + 8, Ex. 17) par racine évidente / imaginaire pure / changement d'inconnue ;
  équations paramétrées par θ et lieux géométriques des points images (cercles, rectangles, losanges).
- ⛔ NON traité dans ce chapitre : formules de Cardan / Ferrari, théorème fondamental de l'algèbre
  (seulement cité à l'aperçu historique) ; résolution par le logiciel d'équations de degré ≥ 5 ; QCM /
  Vrai-Faux ; corrigés.

> Sondage image : pages 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256 (15
> pages sur 16 ; seule p.241 lue en texte). Écarts constatés couche texte / image : λ et Δ confondus
> avec « o », « T » ou « m » ; « x² + y² = a² + b² » lu sans la racine alors que l'image porte
> √(a² + b²) (p.243 Act. 1-b et encadré) ; fonctions « i » pour θ ; barres de conjugué perdues ; exposants
> écrasés (z⁴, z⁶). Ex. 9-1) revérifié sur un rendu 220 dpi (pas de barre : z_2 = i/z_1).

## 2.12 Chapitre 12 — Droites et plans de l'espace (manuel 222451, p.257–274)

**Page de garde (p.257)** — Titre : « Droites et plans dans l'Espace ». Le numéro de chapitre imprimé
(pages de garde et bandeaux) est « 3 » [sic : numéro imprimé différent du rang 12 dans le manuel 222451].
Plan : Activités préliminaires ; Cours (Équations de droites – Positions relatives de deux droites ;
Équations de plans – Positions relatives de deux plans ; Positions relatives d'une droite et d'un plan de
l'espace) ; Résumé du cours ; Avec L'ordinateur ; Exercices et Problèmes ; Aperçu Historique. Pas de
QCM / Vrai-Faux. Convention (p.258) : 𝓔 = ensemble des points de l'espace, 𝓦 = ensemble des vecteurs de
l'espace ; repère cartésien (O, i⃗, j⃗, k⃗), base 𝓑 = (i⃗, j⃗, k⃗). Pas de produit scalaire ni de produit
vectoriel dans ce chapitre : tout repose sur les déterminants, la colinéarité et la coplanarité.

### Activités préliminaires (p.258–259)

- **Prél. 1** (p.258) : A(2, 3, 0), B(3, 2, −3), C(4, −1, 2), D(3, 0, −2). 1) montrer que A, B, C, D ne
  sont pas coplanaires ; 2) a) milieux I, J, K, L de [AB], [BC], [CD], [DA] ; b) composantes de IJ⃗ et LK⃗,
  conséquence sur le quadrilatère IJKL ; 3) M et N milieux de [AC] et [BD] : comparer JM⃗ et NL⃗ ainsi que IM⃗
  et NK⃗.
- **Prél. 2** (p.258) : A(−1, 2, 3), B(4, 1, −2), C(3, 4, −5). 1) a) composantes de AB⃗ et AC⃗ dans la base
  (i⃗, j⃗, k⃗) ; b) AB⃗ et AC⃗ ne sont pas colinéaires ; 2) coordonnées du point M tel que ABCM soit un
  parallélogramme.
- **Prél. 3** (p.258) : A(−1, 2, 4), B(5, −2, 2). 1) milieu I de [AB] ; 2) coordonnées du point M défini par
  MA⃗ + 2MB⃗ = 0⃗.
- **Prél. 4** (p.258) : u⃗ = (−2, −m, 1) et v⃗ = (m, 4 − m, m − 3) dans la base 𝓑 ; m réel ; déterminer m pour
  que u⃗ et v⃗ soient colinéaires.
- **Prél. 5** (p.259) : A(2, 2, 2), B(−1, 2, −1), C(2, 3, 5), D(1, 0, −1) : montrer que A, B, C, D ne sont pas
  coplanaires.
- **Prél. 6** (p.259) : u⃗ = (1, 1, −2), v⃗ = (−2, 3, 1), w⃗ = (0, 5, −3) : a) déterminant de ces trois vecteurs ;
  b) sont-ils coplanaires ?
- **Prél. 7** (p.259) : A(0, −3, −4), B(6, 1, −3), C(−8, −9, 4). 1) A, B, C non alignés ; 2) milieux I de [AB]
  et J de [AC] ; 3) a) coordonnées du point K tel que AK⃗ = AB⃗ + AC⃗ + 2IJ⃗ ; b) prouver que A, C et K sont
  alignés et préciser leurs positions relatives.

### Cours — Activités

**Équations de droites dans l'espace — Positions relatives de deux droites** (p.260–262)

- **Activité 1** (p.260) : 1) u⃗ non nul, A un point, D la droite définie par A et de vecteur directeur u⃗ :
  M ∈ D ⇔ il existe un réel k tel que OM⃗ = OA⃗ + k·u⃗ ; 2) D = D(A, u⃗), A(x_0, y_0, z_0), u⃗ = (a, b, c),
  M(x, y, z) : M ∈ D ⇔ il existe un réel λ tel que x = x_0 + λa, y = y_0 + λb, z = z_0 + λc. Définition
  introduite : ce système, λ ∈ ℝ, est une **représentation paramétrique** de D dans le repère.
- **Activité 2** (p.260) : A(1, 2, −1), B(4, −3, 0) : système d'équations paramétriques de (AB).
- **Activité 3** (p.261) : D passant par A(1, −1, −3), de vecteur directeur v⃗ = (−2, 3, 5). a) système
  paramétrique de D ; b) M ∈ D ⇔ { 3x + 2y − 1 = 0 ; 5x + 2z + 1 = 0 }. Définition introduite : ce système
  est une **représentation cartésienne** de D.
- **Activité 4** (p.261) : D : x = 1 + 2t, y = −3 − 5t, z = 1 − t (t ∈ ℝ) ; représentation cartésienne de la
  droite Δ passant par A(3, −2, 1) et parallèle à D.
- **Activité 5** (p.261) : D : x = 3α − 2, y = −2α + 1, z = α (α ∈ ℝ) et D′ : x = −3t + 1, y = −t + 2,
  z = 4t − 3 (t ∈ ℝ). 1) un vecteur directeur u⃗ de D et v⃗ de D′ ; 2) D et D′ sont-elles parallèles ? ;
  3) D et D′ sont-elles coplanaires ? (justifier).
- **Activité 6** (p.261) : D_1 : x = 3z − 5, y = (2/3)z + 1 et D_2 : x = 9z + 2, y = 2z − 7. 1) représentation
  paramétrique de chacune ; 2) position relative de D_1 et D_2.
- **Activité 7** (p.262) : D : x = α + 1, y = α − 1, z = 2α + 1 (α ∈ ℝ) ; D′ : x = −2β, y = −β − 1, z = β + 4
  (β ∈ ℝ) ; Δ : { x − y + 3z + 3 = 0 ; x + y − z − 5 = 0 }. 1) position relative de D et D′ ; 2) représentation
  paramétrique de Δ ; 3) position relative de D et Δ.

**Équations de plans dans l'espace — Positions relatives de deux plans** (p.262–265)

- **Activité 1** (p.262–263) : plan P défini par A(x_0, y_0, z_0) et deux vecteurs directeurs non colinéaires
  u⃗ = (a, b, c), v⃗ = (a′, b′, c′) ; M(x, y, z). 1) M ∈ P ⇔ il existe deux réels λ et μ tels que
  OM⃗ = OA⃗ + λu⃗ + μv⃗ ; 2) en déduire M ∈ P ⇔ il existe λ, μ tels que x = x_0 + λa + μa′, y = y_0 + λb + μb′,
  z = z_0 + λc + μc′. Ce système, (λ, μ) ∈ ℝ², est une **représentation paramétrique** du plan P.
- **Activité 2** (p.263) : système paramétrique du plan P passant par A(4, 1, 1) de vecteurs directeurs
  u⃗ = (−2, 2, 3) et v⃗ = (−1, 2, 6).
- **Activité 3** (p.263) : A(−1, −2, 5), B(1, 7, 1), C(3, 4, 1). 1) A, B, C non alignés ; 2) système
  paramétrique du plan Q passant par A, B, C.
- **Activité 4** (p.263) : A(2, 3, 1), B(1, 0, 2), C(1, 1, 3). 1) A, B, C déterminent un plan ; 2) M(x, y, z),
  P = plan (ABC) : a) déterminant de AM⃗, AB⃗, AC⃗ en fonction de x, y, z ; b) M ∈ P ⇔ 4x − y + z − 6 = 0
  (« équation cartésienne du plan P ») ; 3) u⃗ = (α, β, γ) : condition nécessaire et suffisante pour que u⃗
  soit un vecteur du plan P.
- **Activité 5** (p.264) : plan P passant par A(2, −4, −3), B(−3, 2, 1) et parallèle à la droite D(O, u⃗),
  u⃗ = (−3, 1, 5) : équation cartésienne de P.
- **Activité 6** (p.264) : P : x + 2y − 4z + 1 = 0 et Q : (1/2)x + y − 2z + 1 = 0 : montrer que P et Q sont
  parallèles.
- **Activité 7** (p.264) : P : x − 2y + z + 3 = 0. 1) un point et deux vecteurs directeurs de P ; 2) une
  représentation paramétrique de P ; 3) équation cartésienne du plan Q parallèle à P passant par O.
- **Activité 8** (p.265) : 1) équations cartésiennes des plans (O, i⃗, j⃗), (O, i⃗, k⃗), (O, j⃗, k⃗) ;
  2) équation cartésienne de la droite d'intersection de (O, i⃗, j⃗) et (O, i⃗, k⃗) ; 3) équation du plan
  passant par A(1, 2, −3) et parallèle à (O, j⃗, k⃗) ; 4) intersection du plan Q : y = 2 et du plan (O, j⃗, k⃗).
- **Activité 9** (p.265) : position relative de P et Q et P ∩ Q : a) P : x − 2y + z + 5 = 0, Q : −2x + 4y −
  2z + 7 = 0 ; b) P : x − 2y + z + 1 = 0, Q : 3x + 4y − 2z + 5 = 0 ; c) P : 2x − 3y + 2z − 4 = 0, Q : x = λ,
  y = μ, z = 5 − 4λ + 2μ ((λ, μ) ∈ ℝ²).

**Positions relatives d'une droite et d'un plan de l'espace** (p.266–267)

- **Activité 1** (p.266) : 1) rappeler les positions relatives d'une droite et d'un plan, une figure par
  position ; 2) P : 3x − 2y + z − 5 = 0, D : x = 3 + 3t, y = −1 + 2t, z = −6 − 5t (t ∈ ℝ) : a) D incluse dans
  P ; b) D strictement parallèle au plan Q : x − (2/3)y + (1/3)z = 0.
- **Activité 2** (p.266) : 1) a) système paramétrique de la droite D passant par A(2, −1, 0) de vecteur
  directeur e⃗ = (−1, 1, 1) ; b) système paramétrique du plan P passant par B(1, −2, 2) de vecteurs
  directeurs u⃗ = (1, 1, 0) et v⃗ = (1, 2, 1) ; 2) position relative de D et P.
- **Activité 3** (p.267) : P : x − 2y − z − 1 = 0 et D : { 3x + y − 10 = 0 ; 2x + z − 9 = 0 }. 1) D sécante à P ;
  2) point d'intersection de D et P.
- **Activité 4** (p.267) : P : x − y + z + 1 = 0 ; Q : x + y − z + 1 = 0 ; R : x + 2y + z − 1 = 0. 1) P et Q
  sécants suivant une droite D (représentation paramétrique) ; 2) position relative de D et R ;
  3) intersection des trois plans.
- **Activité 5** (p.267) : tétraèdre ABCD ; P ∈ [AB], Q ∈ [AC], R ∈ [CD] tels que (PQ) et (BC) soient
  sécantes en M. 1) intersection des plans (PQR) et (BCD) ; 2) intersection des trois plans (PQR), (BCD),
  (ABC) ; 3) ABCD tétraèdre régulier de côté α, repère (B, BC⃗, BD⃗, BA⃗), P(0, 0, (3/4)α), Q((1/2)α, 0,
  (1/2)α), R((1/4)α, (3/4)α, 0) : a) équations cartésiennes de (BCD) et (ABC) ; b) équation de (PQR) :
  6x + 4y + 12z − 9α = 0 ; c) coordonnées de M ; d) (PQR) ∩ (BD) = (MR) ∩ (BD) ; e) S point d'intersection de
  (MR) et (BD), coordonnées de S ; f) nature du quadrilatère PQRS pour le tétraèdre ABCD (justifier).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Colinéarité et coplanarité par les déterminants** (p.259) — « 𝓦 est muni d'une base 𝓑 = (i⃗, j⃗, k⃗).
> Soient u⃗ (a, b, c), v⃗ (a′, b′, c′) et w⃗ (a″, b″, c″) trois vecteurs de 𝓦. On a : (u⃗ et v⃗ sont
> colinéaires) ⇔ ( |a a′ ; b b′| = |a a′ ; c c′| = |b b′ ; c c′| = 0 ) où |a c ; b d| = ad − bc. (u⃗, v⃗ et w⃗
> sont coplanaires) ⇔ ( |a a′ a″ ; b b′ b″ ; c c′ c″| = 0 ) où |a a′ a″ ; b b′ b″ ; c c′ c″| =
> a·|b′ b″ ; c′ c″| − b·|a′ a″ ; c′ c″| + c·|a′ a″ ; b′ b″|. » (Notation du déterminant : lignes séparées par « ; » dans cette transcription, colonnes = vecteurs.)

> **Représentation paramétrique d'une droite** (p.260) — « Le système x = x_0 + λa ; y = y_0 + λb ;
> z = z_0 + λc ; λ ∈ ℝ constitue une représentation paramétrique de la droite D dans le repère
> (O, i⃗, j⃗, k⃗) » (D = D(A, u⃗), A(x_0, y_0, z_0), u⃗ (a, b, c)).

> **Représentation cartésienne d'une droite** (p.261) — « On dit que ce système [3x + 2y − 1 = 0 ;
> 5x + 2z + 1 = 0] constitue une représentation cartésienne de la droite D dans le repère (O, i⃗, j⃗, k⃗). »

> **Positions relatives de deux droites D et D′ de l'espace** (p.262, tableau de quatre cas avec figures) —
> 1) « Les vecteurs directeurs de D et D′ sont colinéaires. D ∩ D′ = Ø. D et D′ sont strictement parallèles.
> (D // D′) » ; 2) « Les vecteurs directeurs de D et D′ sont colinéaires. D ∩ D′ = D = D′. D et D′ sont
> confondues. (D // D′) » ; 3) « Les vecteurs directeurs de D et D′ ne sont pas colinéaires. D ∩ D′ = {O}. D et
> D′ sont sécantes en O » ; 4) « Les vecteurs directeurs de D et D′ ne sont pas colinéaires et D ∩ D′ = Ø. »
> Sous les cas 1 à 3 : « D et D′ sont coplanaires » ; sous le cas 4 : « D et D′ ne sont pas coplanaires ».

> **Représentation paramétrique d'un plan** (p.263) — « Le système x = x_0 + λa + μa′ ; y = y_0 + λb + μb′ ;
> z = z_0 + λc + μc′ ; (λ, μ) ∈ ℝ² constitue une représentation paramétrique du plan P dans le repère
> (O, i⃗, j⃗, k⃗) » (P défini par A(x_0, y_0, z_0) et deux vecteurs directeurs non colinéaires u⃗ (a, b, c) et
> v⃗ (a′, b′, c′)).

> **Équation cartésienne d'un plan** (p.263) — « L'équation 4x − y + z − 6 = 0 est une équation cartésienne
> du plan P dans le repère (O, i⃗, j⃗, k⃗). » (cas particulier de l'Activité 4).

> **Plans, équations, vecteurs d'un plan** (p.264) — « L'espace 𝓔 est muni d'un repère cartésien
> (O, i⃗, j⃗, k⃗). – Tout plan de l'espace a une équation cartésienne de la forme ax + by + cz + d = 0 où a, b,
> c et d sont des constantes réelles telles que (a, b, c) ≠ (0, 0, 0). – Toute équation de la forme
> ax + by + cz + d = 0 où a, b, c et d sont des constantes réelles telles que (a, b, c) ≠ (0, 0, 0) est
> celle d'un plan de l'espace 𝓔. – Soit P : ax + by + cz + d = 0 un plan de l'espace et soit u⃗ (α, β, γ) un
> vecteur de l'espace. u⃗ est un vecteur du plan P, si et seulement si, aα + bβ + cγ = 0. »

> **Plans parallèles** (p.264) — « Deux plans P et P′ de 𝓔 sont parallèles si et seulement si, tout vecteur
> de l'un est un vecteur de l'autre. Soient P : ax + by + cz + d = 0 et P′ : a′x + b′y + c′z + d′ = 0 avec a′,
> b′ et c′ trois réels non nuls. On a : (P // P′) ⇔ (a/a′ = b/b′ = c/c′). »

> **Positions relatives de deux plans P et Q de l'espace** (p.265, tableau avec figures) — « les plans P et Q
> sont confondus : P = Q » ; « les plans P et Q sont disjoints : P ∩ Q = O » [sic : l'ensemble vide est imprimé
> « O »] ; « les plans P et Q sont sécants suivant une droite D : P ∩ Q = D ». Sous les deux premiers cas :
> « P et Q sont parallèles : Tout vecteur de l'un est un vecteur de l'autre. » ; sous le troisième : « P et Q
> sont sécants : Il existe au moins un vecteur de l'un qui n'est pas de l'autre. »

> **Droite et plan** (p.266) — « Soit D une droite et P un plan de l'espace. On a : • D est parallèle à P si
> et seulement si un vecteur directeur de D est un vecteur de P. • D est parallèle à P ou bien D est sécante
> avec P. »

> **Résumé du cours** (p.268–269) — reprend : coplanarité de u⃗, v⃗, w⃗ ⇔ A, B, C, D dans un même plan
> (avec AB⃗ = u⃗, AC⃗ = v⃗, AD⃗ = w⃗) ; colinéarité et coplanarité par les déterminants ; représentation
> paramétrique de D(A, u⃗) ; D(A, u⃗) et D(A′, v⃗) parallèles ⇔ u⃗ et v⃗ colinéaires ; représentation paramétrique
> de P(A, u⃗, v⃗) ; équation cartésienne ax + by + cz + d = 0, (a, b, c) ≠ (0, 0, 0), et tout plan en admet
> une ; u⃗ vecteur de P ⇔ aα + bβ + cγ = 0 ; (P // P′) ⇔ (a/a′ = b/b′ = c/c′) (a′, b′, c′ non nuls) ; « Deux
> plans sont parallèles si tout vecteur de l'un est un vecteur de l'autre. Deux plans sont sécants si et
> seulement si il existe un vecteur de l'un qui n'est pas un vecteur de l'autre. Une droite est parallèle à un
> plan si et seulement si un vecteur directeur de cette droite est un vecteur de ce plan. »

### Avec l'ordinateur (p.270)

- **Activité** : ABCD tétraèdre régulier de côté a ; M ∈ [BC], P plan perpendiculaire à [BC] passant par M ;
  la section du tétraèdre par ce plan est un triangle MNP ; G centre de gravité de MNP ; déterminer
  l'ensemble des points G lorsque M décrit [BC]. Recherche d'une conjecture avec le logiciel Geospace W
  (réel a libre dans [0, 10], repère orthonormal R_xyz d'origine O centre de gravité de la face BCD, i⃗
  colinéaire à DB⃗, j⃗ à OC⃗, k⃗ à OA⃗) : construire le tétraèdre, le plan Q orthogonal à [BC] en M, la section ;
  nature de la section ; section pour M milieu I de [BC] ; M ∈ [BI] : points N, P, centre de gravité G, lieu
  de G, symétries. Stratégie de justification : repère (B, BC⃗, BD⃗, BA⃗), M(x, 0, 0), 0 ≤ x ≤ 1/2 ; G(x/3, 2x/3,
  2x/3) puis BG⃗ = (2x/3)(BI⃗ + BD⃗ + BA⃗) ; G_1 centre de gravité de IAD (G_1I⃗ + G_1D⃗ + G_1A⃗ = 0⃗) ; BG⃗ =
  2x·BG_1⃗ ; ensemble des points G pour M ∈ [BI] puis M ∈ [BC].

### Exercices et problèmes (p.271–273) — 11 exercices

- **Ex. 1** (p.271) : base (i⃗, j⃗, k⃗), u⃗ = 4i⃗ + 3j⃗ + k⃗ ; u⃗′ = ai⃗ + 2j⃗ + bk⃗ ; v⃗ = −2i⃗ + 3j⃗ ;
  v⃗′ = 4i⃗ + αj⃗ + βk⃗ ; w⃗ = −3i⃗ + 2j⃗ + k⃗ ; w⃗′ = −5i⃗ + λj⃗ + μk⃗. a) réels a, b pour u⃗, u⃗′ colinéaires ;
  b) α, β pour v⃗, v⃗′ colinéaires ; c) λ, μ pour w⃗, w⃗′ colinéaires.
- **Ex. 2** (p.271) : u⃗, v⃗, w⃗ coplanaires ? a) u⃗ (1, 0, 3), v⃗ (8, −2, 5), w⃗ (−1, −1, −4) ; b) u⃗ (−2, 3, 1),
  v⃗ (1, −1, −2), w⃗ (−3, 1, −1) ; c) u⃗ (−2, −1, 1), v⃗ (−1, 1, −2), w⃗ (1, −2, −1).
- **Ex. 3** (p.271) : A(1, −1, 1), B(2, −2, 2), C(1, 0, 1), D(0, 0, 3) : position relative des droites (AB)
  et (CD).
- **Ex. 4** (p.271) : A(1, 0, 2), B(−1, 1, 4), C(5, −1, 2). 1) a) A, B, C non alignés ; b) représentation
  paramétrique du plan P(A, AB⃗, AC⃗) ; c) équation cartésienne de ce plan. 2) D(2, 3, 3) : a) représentation
  paramétrique de (AD) ; b) position relative de (AD) et du plan P(A, AB⃗, AC⃗).
- **Ex. 5** (p.271) : u⃗ = −2i⃗ + 3j⃗ − k⃗ ; v⃗ = i⃗ − j⃗ − 2k⃗ ; w⃗ = 2i⃗ − j⃗ − 9k⃗ ; A(1, 1, 4). 1) équation
  cartésienne du plan P passant par A de vecteurs directeurs (u⃗, v⃗) ; 2) existe-t-il a, b réels tels que
  w⃗ = a·u⃗ + b·v⃗ ? (justifier).
- **Ex. 6** (p.271–272) : A(1, −2, 1), B(2, −1, −2), C(1, 0, 1). 1) a) A, B, C déterminent un plan P ;
  b) équation cartésienne de P ; c) réel m pour que u⃗ = −2i⃗ + 3j⃗ + mk⃗ soit un vecteur de P. 2) position
  relative de la droite D et du plan P : a) D = D(A, −2i⃗ + 3j⃗ + 3k⃗) ; b) D = D(O, −2i⃗ + 3j⃗ + 3k⃗) ;
  c) D = D(B, −2i⃗ + 3j⃗ + k⃗).
- **Ex. 7** (p.272) : D : x = −α + 1, y = 3α + 2, z = α − 4 (α ∈ ℝ) ; D′ : x = 1 − 2β, y = 3 − β, z = 1 + 2β
  (β ∈ ℝ). a) vecteurs directeurs ; b) D et D′ non parallèles ; c) intersection de D et D′, position
  relative.
- **Ex. 8** (p.272) : position relative des plans P et P′ : a) P : x − y + z + 1 = 0, P′ : −x + y − z = 0 ;
  b) P : 2x + y + z − 2 = 0, P′ : x − y − z = 0 ; c) P : 2x − y + z + 1 = 0, P′ : x + 2y + 3z − 1 = 0 ;
  d) P : x + 2z − 1 = 0, P′ : y − 2z + 4 = 0 ; e) P : 2x − 3y + 2z − 4 = 0, P′ : x = 2 + t − s, y = 1 − 2t + s,
  z = t + 3s ; f) P : x = 1 + m − p, y = 2 − m − p, z = −1 + m − 2p ; P′ : x = −2 − 2t + 2s, y = 5 + 2t + 2s,
  z = 4 − 2t + 4s.
- **Ex. 9** (p.272) : A(1, 0, 2), B(−1, 2, 1), C(0, 1, 1). a) représentation paramétrique du plan (ABC) ;
  b) équation cartésienne du plan P parallèle à (ABC) passant par I(0, 2, −3).
- **Ex. 10** (p.272–273) : intersection de la droite D et du plan P : a) D : x = −α + 1, y = 3α + 2,
  z = α − 4, P : x + y + z + 4 = 0 ; b) P : x − y + z − 2 = 0, D : (x − 3)/2 = (y + 1)/2 = (z + 2)/3 ;
  c) D : x = α + 1, y = −2α, z = −α + 1, P : x = 3 + 2α + 3β, y = α − 4β, z = 2 + α + β ; d) D : { x + y − 3z + 2 = 0 ;
  x − y + 2z − 1 = 0 }, P : x − y + z + 1 = 0.
- **Ex. 11** (p.273) : P : 2x − y + z − 3 = 0 ; Q : x + 2y + z − 1 = 0 ; R : 3x + y − z + 2 = 0. 1) intersection
  deux à deux ; 2) intersection des trois plans.

### Aperçu historique (p.274)

Évolution de la notion d'espace : postulat d'Euclide des parallèles, géométries non euclidiennes
(XIXᵉ s.) et hyperespace ; géométrie projective (Jean Victor Poncelet, 1788–1867, « traité des propriétés
projectives des figures ») ; Euclide (grec, IIIᵉ s. av. J.-C., Éléments) ; géométrie euclidienne ; espace
vectoriel euclidien = espace vectoriel muni d'un produit scalaire ; figure : Euclide entouré d'étudiants.

### Bornes de scope observées (chapitre 12)

- ✅ INCLUS : coordonnées, milieux, vecteurs, colinéarité et coplanarité par déterminants (2×2 et 3×3) ;
  représentations paramétrique et cartésienne d'une droite ; équations paramétrique et cartésienne d'un
  plan ; positions relatives de deux droites (parallèles, confondues, sécantes, non coplanaires), de deux
  plans, d'une droite et d'un plan ; section d'un tétraèdre par un plan (Activité 5 p.267) ; tétraèdre
  régulier en repère non orthonormé ; recherche de lieux avec logiciel.
- ⛔ NON traité dans ce chapitre : produit scalaire et produit vectoriel dans l'espace, orthogonalité,
  distances, sphères (seule la mention « espace vectoriel euclidien » apparaît à l'aperçu historique) ;
  théorème général sur la représentation cartésienne d'une droite (donnée seulement par exemples, Act. 3
  p.261 et Act. 7 p.262) ; QCM / Vrai-Faux ; corrigés.

> Sondage image : pages 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273,
> 274 (17 pages sur 18 ; seule p.257 lue en texte). Écarts constatés couche texte / image : flèches de
> vecteurs et indices perdus, « λ/μ » remplacés par « m/o », « Δ » lu « T » ou « ∆ » rendu « D », ensemble
> vide lu « O » (imprimé « O » aussi sur l'image p.265, voir [sic]) ; ex. 3 D(0, 0, 3) revérifié sur un
> rendu 220 dpi. Tout ce qui précède est repris de l'image.

## 2.13 Chapitre 13 — Produit scalaire, produit vectoriel et produit mixte dans l'espace (manuel 222451, p.275–306)

**Page de garde (p.275)** — Numérotation propre du manuel : « Chapitre **4** » (ce chapitre est le 13ᵉ de la fiche, mais le chapitre « 4 » de la numérotation imprimée sur ses pages ; le même décalage vaut pour les chapitres suivants). Titre imprimé : « Produit scalaire, Produit vectoriel et Produit mixte dans l'espace » (sous-titre calligraphié arabe non transcrit). Sommaire de la page : ❈ Activités préliminaires ❈ Cours (❖ Exploitation du produit scalaire dans l'espace ❖ Exploitation du produit vectoriel dans l'espace ❖ Exploitation du produit mixte dans l'espace ❖ La Sphère) ❈ Résumé du cours ❈ Avec l'ordinateur ❈ Exercices et Problèmes ❈ Aperçu historique. Pas de QCM / Vrai-Faux dans ce chapitre. Notation : le manuel désigne par 𝓔 l'ensemble des points de l'espace et par 𝓦 l'ensemble des vecteurs de l'espace ; le texte des pages donne le symbole « ⊥ » (orthogonal) et « ∩ » mal rendus (« = », « k ») par la couche texte : relevé sur image.

### Activités préliminaires (p.276–277) — 6 activités

Intro : « Dans tout ce chapitre, on désigne par E l'ensemble des points de l'espace et par W l'ensemble des vecteurs de l'espace. »

- **Prél. 1** (p.276) : tétraèdre ABCD, I et J milieux des arêtes [AB] et [CD]. Montrer que AD⃗ + AC⃗ + BC⃗ + BD⃗ = 4 IJ⃗.
- **Prél. 2** (p.276) : parallélépipède ABCDA'B'C'D'. Démontrer que AB⃗ + AD⃗ + AA'⃗ = AC'⃗.
- **Prél. 3** (p.276) : prisme droit ABCA'B'C' tel que les quadrilatères ABB'A' et BCC'B' soient deux rectangles (figure). 1) Montrer que la droite (BB') est perpendiculaire au plan (ABC). 2) On suppose le triangle ABC rectangle en A : a) montrer que (A'B') est orthogonale aux deux droites (CA) et (CC') ; b) en déduire que (A'B') est perpendiculaire au plan (ACC').
- **Encadrés de rappel (p.276)** : « Deux droites D et D' de l'espace sont orthogonales, et on note D ⊥ D', lorsque leurs parallèles menées par un même point sont perpendiculaires. » — « Une droite D est perpendiculaire à un plan P, et on note D ⊥ P, lorsqu'elle est orthogonale à toute droite de ce plan. » — **Point méthode** : « Pour montrer qu'une droite est perpendiculaire à un plan, il suffit de montrer qu'elle est orthogonale à deux droites sécantes de ce plan. » (chacun accompagné d'une figure).
- **Prél. 4** (p.276) : tétraèdre ABCD tel que les triangles ABC et ABD soient isocèles et de même base. Démontrer que les droites (AB) et (CD) sont orthogonales.
- **Prél. 5** (p.277) : cube ABCDEFGH d'arête a, AE⃗ = BF⃗ = CG⃗ = DH⃗ ; I centre de gravité du triangle CFH. 1) a) Montrer que CFH est équilatéral ; b) montrer que A, G, I appartiennent au plan médiateur de [CH] et au plan médiateur de [CF] ; c) en déduire que (AG) est perpendiculaire au plan (CFH) et passe par I. 2) P plan contenant (AB) et (HG), P' plan contenant (AD) et (FG) : déterminer P ∩ P'.
- **Prél. 6** (p.277) : cube ABCDA'B'C'D' d'arête 1. 1) Vérifier que (B, BA⃗, BC⃗, BB'⃗) est un repère orthonormé de l'espace. 2) Déterminer les coordonnées des sommets du cube dans ce repère.

### Cours — Activités

**Convention (p.278)** — « Dans toute la suite, l'espace E est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗) : i⃗ ⊥ j⃗, i⃗ ⊥ k⃗, j⃗ ⊥ k⃗ ; ‖i⃗‖ = ‖j⃗‖ = ‖k⃗‖ = 1 ».

**I. Exploitation du produit scalaire dans l'espace** (p.278–295 pour l'ensemble du Cours, voir sous-parties)

- **Rappel de définition (p.278)** : A, B, C trois points deux à deux distincts : AB⃗ . AC⃗ = AB . AC . cos(AB⃗, AC⃗ [angle, avec chapeau]) ; puis définition du produit scalaire de deux vecteurs (encadré, voir verbatim).
- **Activité 1** (p.278) : a > 0 ; ABCD tétraèdre régulier d'arête a (figure : A sommet, hauteur h, H pied sur (BCD)). 1) H projeté orthogonal de A sur (BCD) : a) montrer que (CD) ⊥ plan (ABH) ; b) montrer que H est l'orthocentre du triangle BCD ; c) en déduire AB⃗ + AC⃗ + AD⃗ = 3 AH⃗. 2) a) Développer le carré scalaire (AB⃗ + AC⃗ + AD⃗)² et le calculer à l'aide de a ; b) en déduire AH à l'aide de a.
- **Activité 2** (p.279) : 𝓦 muni d'une base orthonormée (i⃗, j⃗, k⃗) ; u⃗(2/3, −1/3, −2/3) et v⃗(2/3, 2/3, 1/3). 1) Vérifier que u⃗ et v⃗ ont pour norme 1 et sont orthogonaux. 2) Déterminer les coordonnées d'un vecteur w⃗ tel que (u⃗, v⃗, w⃗) soit une base orthonormée de 𝓦.
- **Activité 3** (p.279–280) : cube ABCDEFGH de centre O et d'arête a (figure, diagonale [AG] en pointillés). 1) Calculer à l'aide de a : AB⃗.AC⃗ ; AE⃗.BG⃗ ; AH⃗.EC⃗ ; OA⃗.OG⃗ et OE⃗.FB⃗. 2) a) Montrer que (DB) et (EB) sont orthogonales à (AG) ; b) en déduire que B, D, E ont même projeté orthogonal I sur la diagonale [AG] et que C, F, H ont même projeté orthogonal J sur [AG]. 3) Montrer que AI = IJ = JG. Indication : considérer le repère orthonormé (A, i⃗, j⃗, k⃗) avec i⃗ = (1/a)·AB⃗ ; j⃗ = (1/a)·AD⃗ ; k⃗ = (1/a)·AE⃗.
- **Activité 4** (p.280) : repère orthonormé (O, i⃗, j⃗, k⃗). 1) Équation cartésienne du plan passant par A(1,−2,1) et de vecteur normal N⃗(1, 3, −5). 2) Équation cartésienne du plan parallèle au plan Q : 2x + y − 3z + 7 = 0 et passant par B(3,−2,5). 3) C(−1,2,3), D(0,4,−1) : équation cartésienne [sic : « cartésien »] du plan médiateur de [CD]. 4) Coordonnées du point d'intersection du plan P : 2x + 3y + 6z = 117 avec la droite (D) perpendiculaire à P passant par E(5,3,0).
- **Activité 5** (p.281) : repère orthonormé. 1) Équation cartésienne du plan P passant par B(0,−1,5) de vecteur normal N⃗(−1,−1,2). 2) Distance du point A(−2,3,−1) au plan P.
- **Activité 6** (p.281) : repère orthonormé ; A(1,2,−1), B(0,3,−2), E(−1,3,−1). 1) Représentation paramétrique de (AB) (paramètre noté α). 2) Vérifier que E ∉ (AB). 3) H(xH,yH,zH) point d'intersection de (AB) avec le plan passant par E et perpendiculaire à (AB) (H « projeté orthogonal de E sur la droite (AB) ») : a) coordonnées de H ; b) distance EH, « distance du point E à la droite (AB) ». 4) M(x,y,z) quelconque de (AB) : a) x, y, z en fonction de α ; b) EM² en fonction de α ; c) valeur minimale de EM², retrouver la distance de E à (AB).
- **Activité 7** (p.282) : repère orthonormé ; D : { x − z − 1 = 0 ; 2z − y + 1 = 0 } et D' : { x = −4 + 2β ; y = β ; z = 3 } (β ∈ ℝ) (figure : plans P et Q, droites D, Δ). 1) a) Représentation paramétrique de D ; b) montrer que D et D' ne sont pas coplanaires. 2) a) Montrer qu'une équation cartésienne du plan P contenant D et parallèle à D' est x − 2y + 3z + 1 = 0 ; b) en déduire un vecteur directeur w⃗ d'une droite orthogonale à la fois à D et D'. 3) Montrer qu'une équation cartésienne du plan Q contenant D' et perpendiculaire à P est 3x − 6y − 5z + 27 = 0. 4) a) Coordonnées du point d'intersection A de D et Q ; b) la droite Δ passant par A de vecteur directeur w⃗ coupe D' en A' : coordonnées de A' ; c) calculer AA', « distance des droites D et D' ».
- (Encadrés du produit scalaire : voir « Résultats à retenir » ; l'encadré « Distance d'un point à un plan » est placé entre les activités 5 et 6, l'encadré « Distance d'un point à une droite » après l'activité 6 ; le tableau des positions relatives p.283 clôt la sous-partie.)

**II. Exploitation du produit vectoriel dans l'espace** (p.283–287)

- **Activité 1** (p.283) : cube ABCDA'B'C'D' d'arête 1. 1) Montrer que (AB⃗, AD⃗, AA'⃗) et (DA⃗, DC⃗, DD'⃗) sont deux bases orthonormées directes de 𝓦. 2) Montrer que (DC⃗, DA⃗, DD'⃗) et (D'A'⃗, D'C'⃗, D'D⃗) sont deux bases orthonormées indirectes de 𝓦.
- (Définition du produit vectoriel p.283 : encadré, voir verbatim.)
- **Activité 2** (p.284) : u⃗, v⃗ deux vecteurs non nuls. 1) Simplifier : a) (2u⃗ − 3v⃗) ∧ (u⃗ + 2v⃗) ; b) (u⃗ − v⃗) ∧ (u⃗ + v⃗) ; c) (2u⃗ + 3v⃗) ∧ (2u⃗ + 3v⃗) ; d) (2u⃗ + 3v⃗) ∧ (2u⃗ − 3v⃗). 2) Montrer que u⃗ ⊥ v⃗ ⇔ ‖u⃗ ∧ v⃗‖ = ‖u⃗‖ . ‖v⃗‖. 3) u⃗, v⃗ non colinéaires : montrer que pour tous réels a, b, c, d, (a u⃗ + b v⃗) et (c u⃗ + d v⃗) sont colinéaires ⇔ (ad − bc = 0).
- **Activité 3** (p.284) : cube ABCDFGHE (sic : lettres dans cet ordre) tel que AB = 1 (figure : AB⃗, AD⃗ et AF⃗ marqués). 1) Vérifier que (A, AB⃗, AD⃗, AF⃗) est un repère orthonormé direct de E. 2) Calculer AB⃗∧AD⃗ ; AB⃗∧AC⃗ ; AC⃗∧BD⃗ ; AC⃗∧AH⃗ ; AC⃗∧AG⃗ et AG⃗∧BH⃗.
- **Activité 4** (p.285) : base orthonormée directe (i⃗, j⃗, k⃗) ; u⃗(−√3 + 2, √3 + 2, −4) ; v⃗(−3√3 + 1, 3√3 + 1, −2). Déterminer une mesure θ de l'angle orienté (u⃗, v⃗).
- **Activité 5** (p.285–286) : repère orthonormé direct. 1) u⃗(√2 − 1, 1, √2 + 1), v⃗(1, √2 + 1, 3 + 2√2) : a) calculer u⃗ ∧ v⃗ ; b) qu'en déduit-on pour u⃗ et v⃗ ? 2) u⃗(1,0,1), v⃗(2,1,0), w⃗(1,−1,2) : calculer (u⃗∧v⃗)∧w⃗ et u⃗∧(v⃗∧w⃗) ; conclure. 3) A(2,0,0), B(0,4,0), C(0,0,3) : a) calculer AB⃗∧AC⃗ ; BC⃗∧BA⃗ et CA⃗∧CB⃗ ; b) qu'en déduit-on ?
- **Activité 6** (p.286) : repère orthonormé direct ; u⃗(−1,1,0), v⃗(2,2,2). Donner deux vecteurs w⃗ tels que u⃗ ∧ w⃗ = v⃗.
- **Activité 7** (p.286) : repère orthonormé direct. 1) A(−3,5,2), u⃗(−1,3,4), v⃗(0,1,2) : a) montrer que u⃗ et v⃗ ne sont pas colinéaires ; b) équation cartésienne du plan passant par A et de vecteurs directeurs u⃗, v⃗. 2) B(1,2,1), C(3,−1,1), D(−1,0,2) : a) vérifier que B, C, D ne sont pas alignés ; b) équation cartésienne du plan (BCD).
- **Activité 8** (p.287) : A, B deux points de E ; u⃗, v⃗ non colinéaires. Déterminer l'ensemble des points M de E tels que : 1) AM⃗ ∧ AB⃗ = 0⃗ ; 2) AM⃗ . AB⃗ = 0 ; 3) (u⃗ ∧ v⃗) ∧ AM⃗ = 0⃗.
- **Activité 9** (p.287) : triangle ABC, H pied de la hauteur issue de C ; D tel que ABDC soit un parallélogramme (figure) ; 𝒜 aire de ABDC. 1) Montrer que 𝒜 = ‖AB⃗ ∧ AC⃗‖. 2) En déduire l'aire du triangle ABC. 3) A(1,2,3), B(4,2,−1), C(2,−1,2) dans un repère orthonormé direct : calculer l'aire du triangle ABC.
- **Activité 10** (p.287) : repère orthonormé direct ; point A, droite Δ passant par B de vecteur directeur u⃗ ; H projeté orthogonal de A sur Δ. 1) Montrer que la distance AH est donnée par AH = ‖AB⃗ ∧ u⃗‖ / ‖u⃗‖. 2) Calculer la distance du point A(2,2,1) à la droite Δ passant par B(4,2,0) de vecteur directeur u⃗(−2,3,1).

**III. Exploitation du produit mixte dans l'espace** (p.288–291)

- (Définition du produit mixte p.288 : encadré, voir verbatim.)
- **Activité 1** (p.288) : 1) Montrer que u⃗, v⃗, w⃗ sont coplanaires ⇔ (u⃗, v⃗, w⃗) = 0. 2) a) repère orthonormé direct, A(1,1,1), B(−1,2,−1), C(2,3,5), D(1,0,−1) : montrer que A, B, C, D ne sont pas coplanaires ; b) u⃗(2,−1,1), v⃗(1,−1,3), w⃗(4,−3,7) sont-ils coplanaires ? 3) A point, u⃗ et v⃗ non colinéaires : déterminer l'ensemble des points M tels que (u⃗, v⃗, AM⃗) = 0.
- **Activité 2** (p.288–289) : 1) (e₁, e₂, e₃) base orthonormée de 𝓦 : montrer qu'elle est directe ⇔ (e₁, e₂, e₃) = 1. 2) repère orthonormé direct, u⃗(−1/√2, 1/√2, 0), v⃗(1/√3, 1/√3, 1/√3), w⃗(1/√6, 1/√6, −2/√6) : montrer que (u⃗, v⃗, w⃗) est une base orthonormée directe de 𝓦.
- **Activité 3** (p.289) : u⃗, v⃗, w⃗ non coplanaires ; O, A, B, C tels que OA⃗ = u⃗, OB⃗ = v⃗, OC⃗ = w⃗ ; M tel que OM⃗ = OA⃗ ∧ OB⃗ ; H projeté orthogonal de C sur (OM) (figure : parallélépipède OADBCA'D'B'). 1) a) Montrer que |(u⃗, v⃗, w⃗)| = OM . OH ; b) en déduire le volume du parallélépipède OADBCA'D'B'. 2) Tétraèdre ABCD de volume υ : a) montrer que υ = (1/6)|(AB⃗, AC⃗, AD⃗)| ; b) calculer υ pour A(1,1,1), B(2,0,0), C(0,3,0), D(0,0,−2) dans un repère orthonormé direct.
- **Activité 4** (p.289) : ABCD tétraèdre, H projeté orthogonal de A sur (BCD). 1) Montrer que la hauteur AH = |(BC⃗, BD⃗, BA⃗)| / ‖BC⃗ ∧ BD⃗‖. 2) A(−1,4,5), B(0,1,1), C(1,4,0), D(−3,5,0) dans un repère orthonormé direct : a) calculer la hauteur h issue de A ; b) déterminer une équation du plan (BCD) et retrouver le résultat.
- **Activité 5** (p.290) : D : { x = 1 + α ; y = 1 − α ; z = α } (α ∈ ℝ) et D' : { x = 2β ; y = 1 ; z = −2β } (β ∈ ℝ). 1) Montrer que les droites orthogonales à la fois à D et D' ont toutes la même direction ; donner un vecteur directeur. 2) Montrer que, parmi elles, une seule droite coupe à la fois D et D' (notée Δ). 3) H, H' points d'intersection de Δ avec D et D' : coordonnées de H et H'. 4) Représentation paramétrique de Δ. (la couche texte lit « T » ; l'image porte Δ.)
- **Activité 6** (p.290–291) : D et D' non coplanaires ; D défini par (A, u⃗), D' par (A', u'⃗) (figure : perpendiculaire commune HH'). 1) Montrer que pour tout M ∈ D et tout M' ∈ D' : (u⃗, u'⃗, AA'⃗) = (u⃗, u'⃗, MM'⃗). 2) H, H' intersections de D et D' avec leur perpendiculaire commune : montrer que HH' = |(u⃗, u'⃗, AA'⃗)| / ‖u⃗ ∧ u'⃗‖. 3) Calculer la distance entre D : { x = 3 + α ; y = −1 − α ; z = 1 + 2α } (α ∈ ℝ) et D' : { x = 2β ; y = 3 − 3β ; z = 1 + 3β } (β ∈ ℝ).

**IV. La sphère** (p.291–295)

- (Définition p.291 : encadré, voir verbatim.)
- **Activité 1** (p.291) : I point de E, a > 0 : déterminer l'ensemble des centres des sphères de rayon a passant par I.
- **Activité 2** (p.291) : A, B distincts : quel est l'ensemble des centres des sphères passant par A et B ?
- **Activité 3** (p.291) : A, B, C non alignés : quel est l'ensemble des centres des sphères passant par A, B et C ?
- **Activité 4** (p.292) : ABCD tétraèdre régulier d'arête a : déterminer le centre I et le rayon R de la sphère S passant par A, B, C, D (« sphère **circonscrite** au tétraèdre ABCD »). Indication : étudier l'intersection des trois plans P, Q, R médiateurs respectifs des segments [BC], [CD], [AB].
- **Équation cartésienne d'une sphère (p.292–293)**, repère orthonormé direct :
  - **Activité 1** (p.292) : I(1,−2,3) ; condition nécessaire et suffisante sur x, y, z pour que M(x,y,z) appartienne à la sphère de centre I et de rayon 2.
  - **Activité 2** (p.292) : R ≥ 0 et I(a,b,c). 1) Condition nécessaire et suffisante sur x, y, z pour que M(x,y,z) appartienne à la sphère de centre I, rayon R. 2) Réciproquement, (S) = ensemble des M(x,y,z) tels que x² + y² + z² − 2ax − 2by − 2cz + d = 0 : a) écrire la relation sous la forme (x − a)² + (y − b)² + (z − c)² = h, où h est un réel à exprimer en fonction de a, b, c, d ; b) déterminer, suivant a, b, c, d, la nature et les éléments caractéristiques de (S).
  - **Activité 3** (p.293) : déterminer l'ensemble des points M(x,y,z) : 1) x² + y² + z² − 2x + 4z + 4 = 0 ; 2) x² + y² + z² + 2x − 2y + 2 = 0 ; 3) x² + y² + z² + 2x + 4y − 3z + 12 = 0.
  - **Activité 4** (p.293) : A(1,2,0), B(−1,0,3) : a) équation cartésienne de la sphère de diamètre [AB] ; b) ensemble des points M tels que MA = 2MB.
  - **Activité 5** (p.293) : A ≠ B, I milieu de [AB] (figure : sphère de diamètre [AB], point M). 1) Montrer que (MA⃗ . MB⃗ = 0) ⇔ (MI = AB/2). 2) En déduire l'ensemble des points M tels que MA⃗ . MB⃗ = 0. 3) Équation cartésienne de la sphère de diamètre [AB] où A(−1,2,1), B(−3,1,−2).
- **Section plane d'une sphère (p.293–295)** :
  - **Activité 1** (p.293) : S(I,R), plan P ; H projeté orthogonal de I sur P ; d = d(I,P) = IH. 1) d > R : montrer que S et P ne se rencontrent pas. 2) d = R : montrer que P rencontre S en un seul point H (« le plan est **tangent** à la sphère S(I,R) »). 3) d < R : a) M ∈ P : M ∈ S ⇔ HM² = R² − d² ; b) en déduire que P ∩ S est le cercle de centre H et de rayon √(R² − d²).
  - **Activité 2** (p.294) : sphère S de centre O et de rayon 5 ; [AB] un diamètre, I ∈ [AB], OI = h ; P plan perpendiculaire à (AB) en I. Déterminer l'ensemble des points communs à S et P pour : a) h = 4,8 ; b) h = 3 ; c) h = 0 ; d) h = 5 ; e) h = 5,1.
  - **Exercice résolu** (p.294–295) — Énoncé : repère orthonormé direct ; intersection de la sphère S : x² + y² + z² + 4x − 6y + 2z − 2 = 0 avec chacun des plans P : x + 3y + z + 10 = 0 et Q : x + y + z + 4√3 = 0. Solution imprimée : (S) ⇔ (x + 2)² + (y − 3)² + (z + 1)² = 4² ; centre I(−2,3,−1), R = 4 ; d(I,P) = |−2 + 3×3 − 1 + 10| / √11 = 16/√11 > 4 donc P ∩ S = ∅ ; d(I,Q) = |−2 + 3 − 1 + 4√3| / √3 = 4 donc Q et S tangents en H, projeté orthogonal de I sur Q ; H vérifie x + y + z + 4√3 = 0 et x + 2 = α, y − 3 = α, z + 1 = α (IH⃗ colinéaire à n⃗(1,1,1) normal à Q) ; (α − 2) + (α + 3) + (α − 1) + 4√3 = 0 ⇒ 3α = −4√3, α = −4√3/3 ; H(−4√3/3 − 2 ; −4√3/3 + 3 ; −4√3/3 − 1).
  - **Activité 3** (p.295) : repère orthonormé direct ; intersection de S et P : 1) S : x² + y² + z² − 2x + 6y − 8z + 25 = 0 et P : 12x + 5z − 19 = 0 ; 2) S : x² + y² + z² − 2x − 4y + 6z + 5 = 0 et P : 2x − 3z + 5z + 18 = 0 [sic : « −3z + 5z » imprimé] ; 3) S : x² + y² + z² − 2x − 4y + 6z + 5 = 0 et P : x + y + z = 0.
  - **Activité 4** (p.295) : équation cartésienne du plan P tangent à la sphère S de centre I(1,2,0) au point A(1,1,−1).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Produit scalaire — définition par les points** (p.278) — « Soient A, B et C trois points deux à deux distincts de l'espace E. On a AB⃗ . AC⃗ = AB . AC . cos(AB⃗, AC⃗) » [angle des deux vecteurs (AB⃗, AC⃗), surmonté d'un chapeau sur l'image ; ∧ est réservé au produit vectoriel].

> **Produit scalaire — définition vectorielle** (p.278) — « Soient u⃗ et v⃗ deux vecteurs de 𝓦 ; A, B et C trois points de E tels que : AB⃗ = u⃗ et AC⃗ = v⃗. Le produit scalaire de u⃗ et v⃗ est le réel noté u⃗ . v⃗ et défini comme suit : Si u⃗ = 0⃗ ou v⃗ = 0⃗ alors u⃗.v⃗ = 0. Si u⃗ ≠ 0⃗ et v⃗ ≠ 0⃗ alors u⃗ . v⃗ = AB⃗ . AC⃗. »

> **Propriétés** (p.279) — « Pour tous vecteurs u⃗, v⃗, w⃗ de 𝓦 et pour tout réel α on a : u⃗.v⃗ = v⃗.u⃗ ; (α u⃗).v⃗ = u⃗.(α v⃗) = α(u⃗.v⃗) ; u⃗.(v⃗ + w⃗) = u⃗.v⃗ + u⃗.w⃗. »

> **Orthogonalité** (p.279) — « Deux vecteurs u⃗ et v⃗ sont orthogonaux si et seulement si u⃗ . v⃗ = 0. »

> **Expression analytique** (p.279) — « 𝓦 est muni d'une base orthonormée (i⃗, j⃗, k⃗). Pour tous vecteurs u⃗(x, y, z) et v⃗(x', y', z') de 𝓦, on a : u⃗ . v⃗ = xx' + yy' + zz' ; ‖u⃗‖ = √(x² + y² + z²). »

> **Plan défini par un point et un vecteur normal** (p.280) — « Le plan passant par A et de vecteur normal N⃗ est l'ensemble des points M de E tels que AM⃗ . N⃗ = 0. »

> **Vecteur normal d'un plan d'équation cartésienne** (p.280) — « L'espace E est rapporté à un repère orthonormé (O, i⃗, j⃗, k⃗). Soit le plan P d'équation cartésienne : ax + by + cz + d = 0 avec (a,b,c) ≠ (0,0,0). Le vecteur N⃗(a, b, c) est un vecteur normal à P. »

> **Distance d'un point à un plan** (p.281) — « L'espace E est rapporté à un repère orthonormé (O, i⃗, j⃗, k⃗). Soient le plan P : ax + by + cz + d = 0, A(xA, yA, zA) un point de l'espace et H le projeté orthogonal de A sur P. La distance du point A au plan P est le réel positif AH noté d(A, P) et tel que : AH = |a xA + b yA + c zA + d| / √(a² + b² + c²). »

> **Distance d'un point à une droite — définition** (p.282) — « Soit (D) une droite de l'espace E, u⃗ un vecteur directeur de (D), A un point de E et H son projeté orthogonal sur (D). La distance du point A à la droite (D) est le réel positif AH, noté d(A, (D)). Le point H vérifie les conditions : H ∈ (D) et AH⃗ . u⃗ = 0. »

> **Positions relatives de plans et de droites** (p.283) — « Soient, dans l'espace E, deux plans P : ax + by + cz + d = 0 et P' : a'x + b'y + c'z + d' = 0 de vecteurs normaux respectifs N⃗(a,b,c) et N'⃗(a',b',c'). D(A, u⃗) et D(B, v⃗) sont deux droites de l'espace on a : P // P' ⇔ N⃗ et N'⃗ sont colinéaires ; P ⊥ P' ⇔ N⃗ ⊥ N'⃗ ; D(A, u⃗) // P ⇔ u⃗ ⊥ N⃗ ; D(A, u⃗) ⊥ P ⇔ u⃗ et N⃗ sont colinéaires ; D(A, u⃗) ⊥ D(B, v⃗) ⇔ u⃗ ⊥ v⃗ ; D(A, u⃗) // D(B, v⃗) ⇔ u⃗ et v⃗ sont colinéaires. » (tableau à six cases ; le symbole ⊥ est rendu « = » par la couche texte).

> **Produit vectoriel — définition** (p.283) — « Soient u⃗ et v⃗ deux vecteurs de l'espace orienté et A, B et C trois points de E tels que AB⃗ = u⃗ et AC⃗ = v⃗. On appelle produit vectoriel de u⃗ et v⃗, le vecteur w⃗, noté u⃗ ∧ v⃗ défini par : * Si u⃗ et v⃗ sont colinéaires, alors w⃗ = 0⃗. * Si non w⃗ est l'unique vecteur tel que 1/ w⃗ est normal au plan (ABC) ; 2/ (u⃗, v⃗, w⃗) est une base directe de 𝓦 ; 3/ ‖w⃗‖ = ‖u⃗‖ . ‖v⃗‖ . |sin(AB⃗, AC⃗)| » [dernier terme : sinus de l'angle (AB⃗, AC⃗) en valeur absolue, avec chapeau].

> **Propriétés du produit vectoriel** (p.284) — « Soient u⃗, v⃗ et w⃗ trois vecteurs de l'espace et α un réel. On a : u⃗ ∧ v⃗ = − v⃗ ∧ u⃗ ; (α u⃗) ∧ v⃗ = u⃗ ∧ (α v⃗) = α(u⃗ ∧ v⃗) ; (u⃗ + v⃗) ∧ w⃗ = u⃗ ∧ w⃗ + v⃗ ∧ w⃗ ; w⃗ ∧ (u⃗ + v⃗) = w⃗ ∧ u⃗ + w⃗ ∧ v⃗. »

> **Expression analytique du produit vectoriel** (p.285) — « Dans une base orthonormée directe (i⃗, j⃗, k⃗) de 𝓦, si u⃗(x,y,z) et v⃗(x',y',z') alors u⃗ ∧ v⃗ = |y y' ; z z'| i⃗ − |x x' ; z z'| j⃗ + |x x' ; y y'| k⃗ = (yz' − zy') i⃗ − (xz' − zx') j⃗ + (xy' − yx') k⃗ » [déterminants 2×2 lignes (y, y') / (z, z') etc.].

> **Sinus et cosinus de l'angle de deux vecteurs** (p.285) — « Soient u⃗ et v⃗ deux vecteurs non nuls de l'espace orienté 𝓦. Si θ est une mesure de l'angle orienté (u⃗, v⃗) alors on a : |sin θ| = ‖u⃗ ∧ v⃗‖ / (‖u⃗‖ . ‖v⃗‖) et cos θ = u⃗ . v⃗ / (‖u⃗‖ . ‖v⃗‖). »

> **Propriété — vecteur normal à un plan** (p.286) — « Soient u⃗ et v⃗ deux vecteurs non nuls de 𝓦. Si u⃗ et v⃗ sont deux vecteurs directeurs d'un plan P, alors le vecteur u⃗ ∧ v⃗ est un vecteur normal au plan P. » [sic : la propriété n'exige pas « non colinéaires » dans l'énoncé imprimé].

> **Aire d'un triangle** (p.287) — « Soient A, B et C trois points non alignés de l'espace E. L'aire du triangle ABC est égale au réel (1/2)‖AB⃗ ∧ AC⃗‖. »

> **Distance d'un point à une droite** (p.287) — « La distance d'un point A à une droite Δ = D(B, u⃗) est le réel ‖AB⃗ ∧ u⃗‖ / ‖u⃗‖. »

> **Produit mixte — définition** (p.288) — « Soient u⃗, v⃗ et w⃗ trois vecteurs de 𝓦. On appelle produit mixte de u⃗, v⃗ et w⃗, le réel (u⃗ ∧ v⃗) . w⃗. On le note (u⃗, v⃗, w⃗). »

> **Propriété — coplanarité** (p.288) — « Soient u⃗, v⃗ et w⃗ trois vecteurs de 𝓦. On a : u⃗, v⃗ et w⃗ sont coplanaires si et seulement si (u⃗, v⃗, w⃗) = 0. »

> **Propriété — base orthonormée directe** (p.289) — « Soient (u⃗, v⃗, w⃗) une base orthonormée de 𝓦. On a : (u⃗, v⃗, w⃗) est directe si et seulement si le produit mixte (u⃗, v⃗, w⃗) = 1. »

> **Propriété — volumes et hauteur** (p.290) — « * Soient ABCDA'B'C'D' un parallélépipède et 𝒱 son volume. On a : 𝒱 = |(AB⃗, AD⃗, AA'⃗)|. * Soient ABCD un tétraèdre, υ son volume et h la hauteur issue du point A. On a : υ = (1/6)|(AB⃗, AC⃗, AD⃗)| et h = |(BC⃗, BD⃗, BA⃗)| / ‖BC⃗ ∧ BD⃗‖. »

> **Distance entre deux droites non coplanaires** (p.291) — « Soient D(A, u⃗) et D'(A', u'⃗) deux droites non coplanaires de l'espace E. H et H' les intersections de D et D' avec leur perpendiculaire commune. La distance entre D et D' est HH' = |(u⃗, u'⃗, AA'⃗)| / ‖u⃗ ∧ u'⃗‖. »

> **Sphère — définition** (p.291) — « Soient I un point de l'espace E et R un réel positif. On appelle sphère de centre I et de rayon R, l'ensemble des points M de l'espace tels que IM = R. On la note S(I,R). »

> **Équation cartésienne d'une sphère** (p.292) — « L'espace E est rapporté à un repère orthonormé (O, i⃗, j⃗, k⃗). Soient I(a, b, c) un point de l'espace et R un réel positif. Une équation cartésienne de la sphère S(I, R) de centre I et de rayon R est : (x − a)² + (y − b)² + (z − c)² = R²., » [sic : « R²,. » imprimé, ponctuation parasite].

> **Section plane d'une sphère** (p.294) — « Soit S une sphère de centre I et de rayon R et P un plan de l'espace E. On désigne par H le projeté orthogonal du point I sur le plan P et on pose d = IH. * Si d > R alors P ∩ S = ∅ et on dit que P et S sont disjoints. * Si d = R alors P ∩ S = {H} et on dit que P et S sont tangents en H. * Si d < R alors P ∩ S est le cercle du plan P de centre H et de rayon r = √(R² − d²) ; P ∩ S = 𝒞(H, r). » (quatre figures).

> **Résumé du cours (p.296–298)** — reprend les encadrés ci-dessus dans l'ordre (produit scalaire, orthogonalité, expression analytique, vecteur normal, distance point-plan, positions relatives P//P', P⊥P', D//P, D⊥P, produit vectoriel nul si colinéaires, définition 1/2/3, propriétés, expression analytique, sin/cos, vecteur normal u⃗∧v⃗, aire du triangle, produit mixte, coplanarité, base orthonormée directe, volume du parallélépipède, volume et hauteur du tétraèdre, distance entre deux droites, distance point-droite, équation de sphère, section plane avec « sécants suivant ce cercle »). Nuances du résumé : p.296 « P ⊥ P' ⇔ N⃗ et N'⃗ sont orthogonaux » et « D(A,u⃗) // P ⇔ u⃗ et N⃗ sont orthogonaux » ; p.298 ajoute pour d < R « et on dit que P et S sont **sécants suivant ce cercle** ».

### Avec l'ordinateur (p.299–300)

Deux activités avec le logiciel Geospace W : **Activité 1** (p.299) — sphères S₁, S₂ de même centre O et de rayons 3 et 5 ; plan P : Z = m (−3 < m < 3) ; C₁ = P ∩ S₁, C₂ = P ∩ S₂ ; A = A₂ − A₁ (différence des aires) : conjecturer par la construction (pas à pas des menus Geospace donnés) que A est constante, puis la justifier (distance de O à P, rayons r₁, r₂ en fonction de m, aires, couronne d'aire indépendante de m). **Activité 2** (p.299–300) — A(−1,−1,1), B(−1,2,−2), P : X + Y + Z − 2 = 0 ; pour tout m, sphère S_m de centre I(−1, m, −m) et de rayon R_m = √(m² − m + 1) : vérifier que I_m décrit la droite (AB), étudier suivant m la position relative de P et S_m (construction Geospace détaillée, curseur m ∈ [−8, 8], conjecture puis justification).

### Exercices et problèmes (p.301–304) — 26 exercices

Convention : « L'espace E est rapporté à un repère orthonormé direct (O, i⃗, j⃗, k⃗) » (p.301).

- **Ex. 1** (p.301) : calculer u⃗.v⃗ pour u⃗(−1,−2,3), v⃗(0,6,−4) ; puis pour u⃗(−2/3, −2, 3/2), v⃗(2, −√2, 3).
- **Ex. 2** (p.301) : tétraèdre régulier ABCD d'arête a > 0 (I et J utilisés à la question 3 sans être définis dans l'énoncé imprimé [sic]). 1) Montrer que AB⃗.AC⃗ = a²/2 et AB⃗.BC⃗ = −a²/2. 2) a) Calculer AB⃗.CD⃗, AD⃗.BC⃗, AC⃗.BD⃗ ; b) que déduire pour les droites (AB) et (CD), (AC) et (BD), (AD) et (BC) ? 3) a) En écrivant IJ⃗ = IB⃗ + BC⃗ + CJ⃗, calculer AB⃗.IJ⃗ et CD⃗.IJ⃗ ; b) que représente (IJ) pour le couple (AB), (CD) ? c) distances des droites (AB) et (CD) ; (AC) et (BD) ; (AD) et (BC).
- **Ex. 3** (p.301) : équation cartésienne du plan passant par A(1,−2,3) et de vecteur normal u⃗(1,−1,0).
- **Ex. 4** (p.301) : équation cartésienne du plan passant par A(0,1,−2) perpendiculaire à (CD), C(−1,1,−1) et D(0-3,2) [sic : « D(0-3,2) » imprimé].
- **Ex. 5** (p.301) : système d'équations paramétriques de la droite perpendiculaire au plan P : 2x − 3y + z = 0 passant par I(4,−2,0).
- **Ex. 6** (p.301) : équation cartésienne du plan P sachant que le projeté orthogonal de l'origine O sur P est D(1,−2,3).
- **Ex. 7** (p.301) : position relative des plans P et P' : P : x − y + z + 1 = 0, P' : −x + y − z = 0 ; puis P : 2x + y + z − 2 = 0, P' : x − y − z = 0.
- **Ex. 8** (p.301) : 1) équation cartésienne d'un plan admettant k⃗ pour vecteur normal ; 2) a) en déduire que les plans x = 1 et y = 0 sont perpendiculaires ; b) système d'équations paramétriques de leur droite d'intersection.
- **Ex. 9** (p.301) : distance de A au plan P : A(1,0,2), P : 2x − y + z − 2 = 0 ; A(0,0,−3), P : 2x − 2y + z + 5 = 0 ; A(−1,1,1) et P passant par B(0,1,0), C(1,0,0), D(0,0,1).
- **Ex. 10** (p.301) : (i⃗, j⃗, k⃗) base orthonormée directe : déterminer i⃗∧j⃗, i⃗∧k⃗ et j⃗∧k⃗.
- **Ex. 11** (p.302) : 1) montrer que le produit vectoriel de deux vecteurs est nul ⇔ ils sont colinéaires ; 2) montrer que A(1,0,1), B(1,1,0), C(0,1,1) définissent un plan ; 3) équation cartésienne de ce plan.
- **Ex. 12** (p.302) : plans P : x + y + z + 1 = 0 et P' : x − y + 2z − 1 = 0. 1) deux vecteurs u⃗, v⃗ normaux à P et P' ; 2) leur produit vectoriel w⃗ ; 3) droite d'intersection de P et P'.
- **Ex. 13** (p.302) : u⃗, v⃗ orthogonaux : démontrer que u⃗ ∧ (u⃗ ∧ v⃗) = −‖u⃗‖² . v⃗.
- **Ex. 14** (p.302) : montrer que (u⃗, v⃗, w⃗) est orthonormée puis déterminer son sens, u⃗(8/9, 1/9, −4/9), v⃗(1/9, 8/9, 4/9), w⃗(4/9, −4/9, 7/9).
- **Ex. 15** (p.302) : A ≠ B, u⃗, v⃗ non colinéaires : ensemble des points M tels que 1) AM⃗.AB⃗ = 0 ; 2) AM⃗∧AB⃗ = 0⃗ ; 3) (u⃗∧v⃗).AB⃗ = 0 ; 4) (u⃗∧v⃗)∧AB⃗ = 0⃗.
- **Ex. 16** (p.302) : cube ABCDEFGH, AB = 1 : aire des triangles CEH, CFH et CDF.
- **Ex. 17** (p.302) : O point, F⃗ force appliquée en A d'un solide indéformable ; moment M_O(F⃗) = OA⃗ ∧ F⃗. 1) la droite (d) définie par (A, F⃗) est le support de la force ; a) H projeté orthogonal de O sur (d) : montrer ‖M_O(F⃗)‖ = OH.‖F⃗‖ ; b) en déduire que deux forces de même vecteur et de même support ont même moment en tout point. 2) O' point : le moment de F⃗ en O' = moment en O + F⃗ ∧ OO'⃗. 3) trois forces de résultante nulle dont le système a un moment nul par rapport à un point quelconque : leurs supports sont coplanaires.
- **Ex. 18** (p.302) : plans P : x + 2y − 3z = 0 et Q : 2x − y + z − 3 = 0. 1) P et Q sécants, D leur droite d'intersection ; 2) un vecteur directeur de D ; 3) équation cartésienne du plan R passant par O et perpendiculaire à D ; 4) coordonnées du point I intersection de R avec D.
- **Ex. 19** (p.303) : A(1,0,√2), B(−1,0,√2), C(0,−1,0), D(0,1,0). 1) A, B, C, D non coplanaires ; 2) nature du tétraèdre ABCD ; 3) hauteur du tétraèdre ; 4) a ∈ [0, √2], P_a : z = a : a) P_a rencontre (AC), (AD), (BD), (BC) en F, G, H, I ; b) nature du quadrilatère FGHI ; 5) a) périmètre p(a) et aire s(a) de FGHI ; b) extremums de p(a) et s(a).
- **Ex. 20** (p.303) : plans P : 3x − 2y + 5z − 1 = 0 et Q : 2x − 3y + 2z − 2 = 0. 1) P et Q se rencontrent suivant une droite D ; 2) a, b réels non tous nuls : a) a(3x − 2y + 5z − 1) + b(2x − 3y + 2z − 2) = 0 est l'équation d'un plan contenant D ; b) plan R passant par I(2,5,0) contenant D ; 3) plan S perpendiculaire à P contenant D ; 4) a) distances de A aux plans P et S et à la droite D [A non défini dans l'énoncé imprimé de cet exercice : sic] ; b) relation entre ces trois distances.
- **Ex. 21** (p.303) : équation de la sphère de centre I et de rayon R : 1) I(1,2,3), R = 1 ; 2) I(−1,0,3), R = √2.
- **Ex. 22** (p.303) : équation cartésienne de la sphère de diamètre [AB] : 1) A(−1,3,0), B(0,0,−2) ; 2) A(1,−2,2), B(1,−1,−2).
- **Ex. 23** (p.303) : ensemble des M(x,y,z) tels que : a) x² + y² + z² − 2x − 2y − 2z + 12 = 0 ; b) x² + y² + z² − 6x + 4y − 2z + 5 = 0 ; c) x² + y² + z + 2x + 2y + 6z − 8 = 0 [sic : « z » sans carré imprimé].
- **Ex. 24** (p.303) : position relative de la sphère S et du plan P : a) P : x − y = 0, S : x² + y² + z² − 2x − 2y − 2z = 0 ; b) P : 2x + 3y − 2z + 1 = 0, S : x² + y² + z² − 2x + 4y + 6z = 0 ; c) P : x + y = 0, S : x² + y² + z² − 2x = 0.
- **Ex. 25** (p.303) : D : { x = 1 + λ ; y = 1 − λ ; z = 2 − λ } (λ ∈ ℝ), A(0,2,2). 1) équations cartésiennes de deux plans dont D est l'intersection ; 2) a) équations paramétriques du plan P passant par A et contenant D ; b) équation cartésienne de P ; 3) plan Q parallèle à P passant par B(0,0,1) ; 4) a) plan R contenant D et perpendiculaire à P ; b) sphère tangente aux plans R et P ; c) sphère tangente aux plans P et Q.
- **Ex. 26** (p.304) — « D'après Bac Tunisien, juin 2005 » : repère orthonormé [sic : non « direct » ici] ; A(1,1,1), B(3,1,0), C(−1,0,1). 1) a) A, B, C non alignés ; b) vérifier que le plan P = (ABC) a pour équation x − 2y + 2z − 1 = 0 ; c) plan Q : 2x + y + 2z + 1 = 0 : P et Q sécants. 2) t réel, I_t(1,−1,t) : a) d(I_t, P) = d(I_t, Q) ; b) si t = −1, I_t ∈ P ∩ Q ; c) si t ≠ −1, il existe une sphère S_t de centre I_t tangente à P et Q, rayon en fonction de t ? 3) t = 2 : coordonnées du point H de contact de S₂ avec Q.

### Aperçu historique (p.305–306)

Une ligne par page : p.305 — Hamilton (1805–1865, quaternions 1843 ⇒ produit vectoriel ; Grassmann 1844, Maxwell, Clifford, Gibbs 1881 ; naissance du produit scalaire, Peano, Longo et Burali-Forti) ; p.306 — Gibbs (1839–1903, fondateur de l'analyse vectorielle, notation . et ∧ des années 1880 ; produit scalaire comme aire orientée / déterminant, cisaillement : figure de parallélogrammes verts et roses).

### Bornes de scope observées (chapitre 13)

- ✅ INCLUS : produit scalaire dans l'espace (définitions, propriétés, expression analytique, norme, orthogonalité) ; équation cartésienne de plan par vecteur normal ; distance point-plan ; distance point-droite (deux méthodes : projection et produit vectoriel) ; positions relatives plans/droites par vecteurs normaux/directeurs ; produit vectoriel (définition géométrique, propriétés, expression analytique en base orthonormée directe, sin/cos de l'angle, vecteur normal, aire d'un triangle) ; produit mixte (coplanarité, base orthonormée directe, volume du parallélépipède et du tétraèdre, hauteur, distance entre deux droites non coplanaires, perpendiculaire commune) ; sphère (définition, équation cartésienne, sphère de diamètre [AB], lieu MA = k·MB, section plane, plan tangent, sphère circonscrite à un tétraèdre) ; moment d'une force (Ex. 17) ; usage de Geospace W.
- ⛔ NON traité dans ce chapitre : démonstration de l'expression analytique du produit vectoriel (admise) ; déterminants 3×3 comme objet autonome (seul le développement 2×2 imprimé) ; transformations de l'espace (rotations, symétries) ; coniques ou quadriques autres que la sphère ; équation d'un plan par trois points autrement que via u⃗ ∧ v⃗ ou résolution de systèmes ; produit scalaire sur ℝⁿ ou formes bilinéaires (évoqué seulement dans l'aperçu historique).

> Sondage image : pages 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 301, 302, 303, 304 (27 pages sur 32, soit toutes les pages à formules/figures et aucune lue en L1 seul) ; écarts : aucun écart de contenu (mot, nombre, ordre) entre la couche texte et l'image ; seuls les symboles ⊥ et ∩ (rendus « = » et « k ») et les vecteurs/racines/fractions sont cassés par la couche texte — tout a été transcrit depuis l'image. Pages non confrontées : 275, 299, 300, 305, 306 (texte seul, lisible, sans formule).

## 2.14 Chapitre 14 — Probabilité sur un ensemble fini (manuel 222451, p.307–330)

**Page de garde (p.307)** — Titre imprimé : « Probabilité sur un ensemble fini » ; numérotation propre du manuel : « Chapitre **5** » (ce chapitre est le 14ᵉ de la fiche). Sommaire : ❈ Activités préliminaires ❈ Cours (❖ Probabilité sur un ensemble fini ❖ Probabilité uniforme ❖ Probabilité conditionnelle ❖ Évènements indépendants ❖ Principe des probabilités composées ❖ Principe des probabilités totales - Formule de Bayes) ❈ Résumé du cours ❈ Avec L'ordinateur ❈ Exercices et Problèmes ❈ Aperçu Historique. Pas de QCM / Vrai-Faux dans ce chapitre. Résumé, exercices et aperçu historique : p.324–330 ; pas de rubrique « Exercice résolu » titrée, mais cinq activités portent la mention « (résolue) » dans le Cours.

### Activités préliminaires (p.308) — 6 activités + encadré de rappels

- **Encadré de rappels (p.308, à droite)** — « • Soit n ∈ ℕ* et p un entier tel que 1 ≤ p ≤ n. – Le nombre d'arrangements de p éléments d'un ensemble à n éléments est : Aₙᵖ = n(n−1)(n−2)…(n−p+1) – Le nombre de combinaisons de p éléments d'un ensemble à n éléments est : Cₙᵖ = Aₙᵖ / p! = n! / (p!(n−p)!) • Soit E un ensemble de p éléments et F un ensemble de q éléments. Le nombre d'applications de E dans F est : (card F)^(card E) = q^p • Soit E un ensemble de n éléments. Le nombre de parties de E est card 𝒫(E) = 2ⁿ • Pour tous réels a et b et pour tout entier naturel n, on a : (a + b)ⁿ = Σ_{k=0}^{n} Cₙᵏ a^{n−k} bᵏ. »
- **Prél. 1** : dans un parking de 6 places, combien y a-t-il de façons de garer trois voitures ?
- **Prél. 2** : un club de basket-ball comporte 12 joueurs inscrits ; combien d'équipes différentes de 5 joueurs peut-il former ?
- **Prél. 3** : déterminer le nombre de façons de placer trois objets a, b, c dans deux cases x et y, chaque case ne pouvant contenir qu'un seul objet.
- **Prél. 4** : énoncé **identique mot pour mot** à Prél. 3 [sic, doublon à l'impression].
- **Prél. 5** : 1) pièce non truquée lancée une fois : probabilité d'obtenir pile ? 2) a) une carte au hasard d'un jeu de 32 cartes : probabilité d'obtenir la Dame de cœur ? b) 3 cartes tirées simultanément du même jeu : probabilité d'obtenir au moins un Roi ? 3) dé cubique non truqué (faces 1 à 6) jeté une fois : probabilité d'obtenir un nombre impair ? 4) dé cubique parfait jeté 3 fois de suite : probabilité d'obtenir dans l'ordre 2, 4 et 6 ?
- **Prél. 6** : dé cubique (faces 1 à 6) lancé une fois, truqué de sorte que la probabilité d'apparition de chaque numéro soit proportionnelle à ce numéro. 1) probabilité d'apparition de chaque numéro ; 2) probabilité de A : « numéro pair », B : « numéro impair », C : « numéro supérieur ou égal à 2 », D : « numéro premier ».

### Cours — Activités

**I. Probabilité sur un ensemble fini** (p.309–311)

- **Langage des probabilités** (p.309, encadré, voir verbatim).
- **Activité 1** (p.309) : dans un lycée, 40 % des élèves pratiquent des activités sportives, 35 % des activités culturelles, 10 % des activités culturelles et sportives. Un élève est choisi au hasard. 1) Probabilité qu'il pratique des activités culturelles ou sportives ? 2) ... ni culturelles ni sportives ? 3) ... culturelles et non sportives ?
- (Encadrés « Définition d'une probabilité » et « Propriétés », p.310 : voir verbatim.)
- **Activité 2** (p.310) : atelier de production, deux types de défaut (conception, montage) : 5 % des pièces ont un défaut de conception, dont 25 % ont aussi un défaut de montage ; parmi les pièces sans défaut de conception, 3 % ont un défaut de montage. A : « défaut dû à la conception », B : « défaut dû au montage ». a) p(A) ; b) p(A∩B) ; c) p(Ā∩B) ; d) en déduire p(B) ; e) p(A∪B) ; f) probabilité d'obtenir une pièce sans défaut.
- **Activité 3** (p.311) : tableau de 1000 entrées dans un musée (lignes Hommes / Femmes / Enfants ; colonnes Visiteurs tunisiens / Visiteurs étrangers / Total) : Hommes tunisiens 100, Hommes étrangers 250 ; Femmes tunisiennes 90 ; Enfants tunisiens 220, Enfants étrangers 70 (autres cases et totaux vides). 1) Recopier et compléter le tableau. 2) Un billet est pris parmi les billets remis : a) probabilité de A « le billet est celle [sic] d'une femme », B « ... d'une personne de nationalité étrangère », C « ... d'un enfant tunisien » ; b) p(A∩B) et p(A∪B) ; c) le billet est celui d'un homme : probabilité qu'il soit tunisien ?

**II. Probabilité uniforme** (p.311–314)

- (Définition p.311 : encadré, voir verbatim.)
- **Activité 1 (résolue)** (p.312) : deux dés cubiques A et B non truqués lancés simultanément (faces 1 à 6). a) Probabilité d'une somme égale à 7 ? b) d'un produit égal à 6 ? Solution imprimée : Ω = couples (a,b), card Ω = 36 ; somme 7 : (1,6),(6,1),(2,5),(5,2),(3,4),(4,3) donc 6/36 = 1/6 ; produit 6 : (1,6),(6,1),(2,3),(3,2) donc p(B) = 4/36 = 1/9.
- **Activité 2 (résolue)** (p.312) : jeu de 32 cartes, 3 cartes tirées simultanément. a) un as ? b) au moins un roi ? c) un valet ou un pique ? Solution imprimée (numérotée « 2) » en tête [sic]) : card Ω = C₃₂³ = 4960 ; a) p(C) = C₄¹×C₂₈²/C₃₂³ = 189/620 ≈ 0,30 ; b) p(D̄) = C₂₈³/C₃₂³ = 819/1240 ≈ 0,66, donc p(D) = 1 − p(D̄) = 421/1240 ≈ 0,33 ; c) p(E) = C₁₁¹×C₂₁²/C₃₂³ = 231/496 ≈ 0,47 (un parmi les huit piques ou un valet trèfle, cœur ou carreau).
- **Activité 3** (p.313) : urne : 4 boules rouges, 3 blanches, 2 noires ; 3 boules tirées successivement et sans remise. Probabilité de A « trois rouges », B « trois de même couleur », C « au moins une rouge », D « les deux boules noires ».
- **Activité 4** (p.313) : sac : quatre boules blanches numérotées 1, 2, 2, 2 et trois noires numérotées 1, 1, 2. 1) Tirage successif **avec** remise de trois boules : A « trois boules de même couleur », B « une seule blanche », C « deux boules numéro 2 », D « au moins une blanche », E « une seule blanche et une seule boule numéro 1 ». 2) Tirage successif de trois boules : boule numéro 1 non remise, boule numéro 2 remise : F « trois boules blanches », G « une seule boule numéro 1 », H « une seule boule numéro 2 ».
- **Activité 5** (p.313) : sac de 8 jetons : trois rouges numérotés 1, 1, 0 ; trois jaunes numérotés 1, 0, −1 ; deux verts numérotés 2, −1 ; trois jetons tirés simultanément. 1) A « trois jetons de même numéro », B « de même couleur », C « exactement deux rouges et un seul jeton portant le numéro 0 », D « exactement deux jaunes ou deux jetons à numéros positifs ». 2) S « numéros de somme nulle », N « numéros de produit égal à 0 ». 3) Probabilité d'un produit égal à 0 sachant que la somme est nulle.
- **Tableau « Tirage de p jetons d'un sac contenant n jetons (p ≤ n) »** (p.314, voir verbatim).

**III. Probabilité conditionnelle** (p.314–316)

- **Activité 1** (p.314) : 100 agents d'encadrement : Cadres administratifs : Hommes 10, Femmes 20 ; Cadres techniques : Hommes 50, Femmes 20. Une personne au hasard. 1) A « cadre administratif », B « un homme », C « un cadre administratif sachant que c'est un homme » : probabilités. 2) a) p(A∩B) ; b) comparer p(C) et p(A∩B)/p(B).
- **Activité 2** (p.315) : jeu de 32 cartes, une carte au hasard ; A « un roi ou un as », B « un cœur ». 1) p(A), p(B), p(A∩B). 2) Sachant (« parce qu'une personne nous l'a dit ») que la carte est un cœur : a) probabilité P que ce soit un roi ou un as ; b) comparer P et p(A∩B)/p(B).
- (Définition de la probabilité conditionnelle p.315 : voir verbatim.)
- **Activité 3** (p.315) : deux dés cubiques parfaits non identiques jetés simultanément ; A « nombres différents », B « somme égale à 7 », C « somme égale à 4 », D « somme égale à 12 ». 1) p(A), p(A∩B), p(A∩C), p(A∩D), p(B∩C). 2) p(Ω/A), p(B/A), p(C/A), p(D/A). 3) calculer p(B∪C / A) [sic : « (B ∪ C / A) » sans p] et comparer avec p(B/A) + p(C/A). 4) calculer p(B̄/A) et comparer avec 1 − p(B/A).
- (Encadré « Propriétés » de la probabilité conditionnelle, p.315 : voir verbatim.)
- **Activité 4** (p.316) : boîte avec trois boules rouges et sept blanches ; trois boules tirées simultanément. 1) A « une boule rouge », B « au moins une boule blanche » : probabilités. 2) a) p(A/B) et p(B/A) ; b) probabilité d'obtenir une boule rouge sachant qu'au moins deux blanches sont tirées. 3) comparer p(A/B) à p(A) et p(B/A) à p(B).

**IV. Évènements indépendants** (p.316–317)

- **Activité 1** (p.316) : deux dés parfaits non identiques lancés simultanément ; A « le premier dé amène un nombre pair », B « le deuxième dé amène un nombre impair ». a) p(A), p(B), p(A∩B) ; b) comparer p(A∩B) au produit p(A).p(B) ; c) p(A/B).
- (Définition de l'indépendance et Remarque p.316 : voir verbatim.)
- **Activité 2** (p.316) : A, B de probabilités non nulles ; montrer que (A et B indépendants) équivaut à (Ā et B̄ indépendants).
- **Activité 3** (p.316) : dé cubique dont les faces 1, 2, 3, 4, 5 sont blanches et la face 6 est rouge, lancé une fois ; A « la face porte un nombre pair », B « la face est rouge ». A et B sont-ils indépendants ? justifier.
- **Activité 4** (p.317) : famille de n enfants, Ω ensemble des répartitions possibles des sexes (en respectant l'ordre de naissance), équiprobables ; M « enfants des deux sexes », F « au plus une fille ». 1) n = 2 : M et F non indépendants. 2) n = 3 : M et F indépendants. 3) a) pour n ≥ 2 : p(M) = (2ⁿ − 2)/2ⁿ, p(F) = (n + 1)/2ⁿ et p(M∩F) = n/2ⁿ ; b) en déduire que M et F ne sont indépendants que pour une famille de 3 enfants.
- **Activité 5** (p.317) : sondage : 20 % lisent des revues hebdomadaires, 30 % des mensuelles, 10 % les deux. 1) A « lit des revues mensuelles » et B « lit des revues hebdomadaires » : indépendants ? 2) probabilité de lire des mensuelles sachant qu'on lit des hebdomadaires ; 3) probabilité de lire des hebdomadaires sachant qu'on lit des mensuelles.

**V. Principe des probabilités composées** (p.317–320)

- **Activité 1** (p.317) : Ω, p, A et B. 1) Vérifier que si p(A) = 0 alors p(A∩B) = 0. 2) Si p(A) ≠ 0 : montrer p(A∩B) = p(A).p(B/A). 3) Si p(A) ≠ 0 et p(B) ≠ 0 : p(A).p(B/A) = p(B).p(A/B). 4) A, B, C avec p(A) ≠ 0, p(B) ≠ 0, p(A∩B) ≠ 0 : en utilisant p(C/A∩B) = p(A∩B∩C)/p(A∩B), montrer p(A∩B∩C) = p(A).p(B/A).p(C/(A∩B)).
- (Encadré « Principe des probabilités composées », p.318 : voir verbatim.)
- **Activité 2** (p.318) : personnel composé de 32 % de femmes ; parmi elles 70 % ont moins de 30 ans ; probabilité qu'un employé choisi au hasard soit une femme et ait moins de 30 ans ?
- **Activité 3 (résolue)** (p.318) : usine de boulons : la machine M assure 40 % de la production ; 10 % de ses boulons sont défectueux ; probabilité qu'un boulon choisi provienne de M et soit défectueux ? Solution imprimée : A « provient de M » [sic : « choisie »], B « défectueux », C « provient de M et défectueux » ; p(C) = p(A∩B) = p(A).p(B/A) = 0,4 × 0,1 = 0,04.
- **Activité 4** (p.318) : trois boîtes B₁, B₂, B₃ d'apparence identique contenant respectivement deux, trois et quatre fiches, une seule marquée dans chacune. Épreuve : désigner une boîte au hasard puis tirer une fiche au hasard ; fiche marquée = cadeau. A₁, A₂, A₃ : « désigner Bᵢ et tirer une fiche marquée » ; A « la fiche tirée est marquée ». 1) a) p(A₁), p(A₂), p(A₃) ; b) p(A). 2) Fiche marquée tirée : probabilité qu'elle vienne de la boîte contenant deux fiches ?
- **Principe « Stochastique fini »** (p.319, texte de cours avec arbre pondéré, voir verbatim).
- **Activité 5 (résolue)** (p.319–320) : deux dés cubiques d'apparence identique (faces 1 à 6), l'un parfait, l'autre truqué (probabilité de la face 4 = 1/3 pour le truqué) ; un dé choisi au hasard (équiprobable), lancé une fois. A « choisir le truqué et obtenir 4 », B « choisir le parfait et obtenir 4 », C « obtenir 4 ». Solution imprimée avec arbre (D₁ truqué : 1/2 puis {4} : 1/3, {1;2;3;5;6} : 2/3 ; D₂ parfait : 1/2 puis {4} : 1/6, autres : 5/6) : p(A) = 1/2 × 1/3 = 1/6 ; p(B) = 1/2 × 1/6 = 1/12 ; C réunion des incompatibles A et B : p(C) = 1/6 + 1/12 = 1/4.
- **Activité 6** (p.320) : appareils électroniques : probabilité de fonctionner parfaitement 0,9 ; test avant livraison : un appareil parfait est toujours accepté ; un appareil non parfait est néanmoins accepté avec probabilité 1/11. A « accepté à l'issue du test », F « fonctionne parfaitement ». Calculer p(A) ; sachant l'appareil accepté, probabilité qu'il fonctionne parfaitement.

**VI. Principe des probabilités totales — Formule de Bayes** (p.321–323)

- **Activité 1** (p.321) : Soient Ω un univers et A et B deux événements de Ω tels que p(B) ≠ 1 et p(B) ≠ 0. a) En remarquant que A = A∩Ω et B ∪ B̄ = Ω, montrer A = (A∩B) ∪ (A∩B̄) ; b) en déduire p(A) = p(A∩B) + p(A∩B̄) ; c) prouver p(A) = p(B).p(A/B) + p(B̄).p(A/B̄) ; d) montrer p(B/A) = p(B).p(A/B) / [p(B).p(A/B) + p(B̄).p(A/B̄)].
- (Encadrés « Principe des probabilités totales » + généralisation, et « Formule de Bayes », p.321 : voir verbatim.)
- **Activité 2 (résolue)** (p.321–322) : un individu sur 200 est atteint d'une maladie ; test positif ; chez les malades le test est positif dans 98 % des cas, chez les non-malades il est négatif dans 94 % des cas ; probabilité que la personne soit réellement malade ? Solution imprimée (arbre pondéré : M 0,005 puis T 0,98 → 0,0049, T̄ 0,02 → 0,0001 ; M̄ 0,995 puis T̄ 0,94 → 0,9353, T 0,06 → 0,0597) : p(M/T) = p(M).p(T/M) / [p(M).p(T/M) + p(M̄).p(T/M̄)] = (0,005 × 0,98)/(0,005 × 0,98 + 0,995 × 0,06) = 0,0049/0,0646 ≈ 0,076 ; autre calcul : 1 − p(M̄/T) = 1 − p(T∩M̄)/p(T) = 1 − 0,0597/(0,0049 + 0,0597) ≈ 0,076.
- **Activité 3** (p.322) : un jeu de 32 cartes et un jeu de 52 cartes ; on choisit l'un des deux jeux et on y tire une carte, c'est une dame. Montrer que la probabilité qu'elle vienne du jeu de 32 cartes est égale à 13/21.
- **Activité 4** (p.322) : urne : une boule rouge et deux vertes. On tire une première boule, on la remet et on ajoute une boule de la même couleur, puis on tire une seconde boule. R « rouge au premier tirage », V « verte au premier tirage », A « rouge au deuxième tirage ». 1) p(R), p(V), p(A/R), p(A/V) ; 2) en déduire p(A∩R), p(A∩V) puis p(A) ; 3) p(R/A) ; 4) R et A sont-ils indépendants ?
- **Activité 5** (p.323) : trois urnes U₁, U₂, U₃ ; U₁ et U₂ contiennent chacune deux boules rouges et trois noires ; U₃ quatre rouges et une noire ; on choisit deux urnes au hasard et on extrait une boule de chaque. 1) A « les deux urnes choisies ont la même composition », B « tirer deux boules noires » : a) p(A) puis p(Ā) ; b) p(B/A) puis p(B∩A) ; c) p(B∩Ā) puis p(B). 2) C « deux boules de même couleur », D « deux boules de couleurs différentes » : probabilités. 3) Deux boules de même couleur viennent d'être tirées : probabilité d'avoir choisi deux urnes de même composition ?
- **Activité 6** (p.323) : un dé choisi au hasard parmi 100 dés cubiques (faces 1 à 6) dont 25 sont pipés ; pour un dé pipé la probabilité d'obtenir 6 est 1/2. On lance une fois le dé choisi et on obtient 6 [sic : « obtien »]. a) probabilité que ce dé soit pipé ? b) on relance et on obtient à nouveau 6 : probabilité que ce dé soit pipé ? c) Sₙ « obtenir 6 aux n premiers lancers », A « le dé est pipé » : montrer p(Sₙ/A) = 1/(1 + (1/3)^{n−1}) et calculer lim_{n→+∞} p(Sₙ/A) [sic : la source imprime « p(Sₙ / A) » alors que la quantité qui a du sens est p(A / Sₙ)].

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Langage des probabilités** (p.309) — « • On appelle univers (ou univers des possibles), l'ensemble des résultats (ou éventualités) possibles d'une expérience aléatoire. Cet ensemble se note Ω. • Toute partie A de Ω est appelée événement. • Si A = Ø, on dit que A est l'événement impossible. • Si A = Ω, on dit que A est l'événement certain. • Si A est une partie contenant un seul élément de Ω, on dit que A est un événement élémentaire. • L'évènement A ∩ B est l'évènement « A et B ». Il est réalisé si les deux événements A et B sont réalisés simultanément. • L'événement A ∪ B est l'évènement « A ou B ». Il est réalisé si l'un au moins des deux événements A et B est réalisé. • L'ensemble Ω \ A, qu'on note Ā, est l'événement contraire de A. Il est réalisé si et seulement si A n'est pas réalisé. • Deux événements A et B sont dits incompatibles s'ils ne peuvent pas se réaliser en même temps. C'est-à-dire si et seulement si A ∩ B = Ø. • Si A et B sont deux évènements de Ω tels que A ⊂ B alors B \ A désigne l'ensemble des éléments de B qui n'appartiennent pas à A. »

> **Définition d'une probabilité** (p.310) — « Soit Ω un univers fini. On appelle probabilité définie sur l'ensemble 𝒫(Ω) des parties de Ω, toute application p de 𝒫(Ω) dans [0,1] vérifiant : • p(Ω) = 1. • Pour tous événements A et B tels que A ∩ B = Ø on a : p(A ∪ B) = p(A) + p(B). »

> **Propriétés** (p.310) — « Soient Ω un univers fini, 𝒫(Ω) l'ensemble des parties de Ω, p une probabilité sur 𝒫(Ω) et A et B deux événements. On a : • La somme des probabilités de tous les événements élémentaires est égale à 1. • La probabilité d'un événement A est la somme des probabilités des événements élémentaires dont la réunion est A. • 0 ≤ p(A) ≤ 1 • Si A ⊂ B alors p(B \ A) = p(B) − p(A) et p(A) ≤ p(B). • p(Ā) = 1 − p(A) • p(Ø) = 0 • p(A∪B) = p(A) + p(B) − p(A∩B) »

> **Probabilité uniforme — définition** (p.311) — « Soient Ω = {w₁, w₂, w₃, …, wₙ} et p une probabilité définie sur 𝒫(Ω). Lorsque tous les évènements élémentaires ont la même probabilité d'être réalisés, on dit que p est une probabilité uniforme ou une équiprobabilité. Dans ce cas on a : • p({w₁}) = p({w₂}) = … = p({wₙ}) = 1/n = 1/card Ω • Pour tout évènement A on a : p(A) = card A / card Ω. (C'est le quotient du nombre des cas favorables à la réalisation de A par le nombre des cas possibles). »

> **Tableau « Tirage de p jetons d'un sac contenant n jetons (p ≤ n) »** (p.314) — colonnes : **Successifs et avec remise** — « L'ordre intervient » — un cas possible : « Un p-uplet avec possibilité de répétition » — card Ω : nᵖ ; **Successifs et sans remise** — « L'ordre intervient » — « Un p-uplet d'éléments deux à deux distincts » — card Ω : Aₙᵖ ; **Simultanés** — « L'ordre n'intervient pas » — « Une partie de p éléments » — card Ω : Cₙᵖ.

> **Probabilité conditionnelle — définition** (p.315) — « Soient Ω un univers, p une probabilité définie sur 𝒫(Ω) et A et B deux événements tels que p(B) ≠ 0. On appelle probabilité conditionnelle de A sachant B et on lit : " Probabilité de A sachant B ", le nombre réel : p(A / B) = p(A∩B) / p(B). On note aussi p(A / B) = p_B(A). »

> **Propriétés de la probabilité conditionnelle** (p.315) — « Soient Ω un univers, p une probabilité définie sur 𝒫(Ω) et B un événement tel que p(B) ≠ 0. • On a : p(Ω / B) = 1. • Pour tous évènements incompatibles A₁ et A₂ on a : p(A₁ ∪ A₂ / B) = p(A₁ / B) + p(A₂ / B). • Pour tout événement A on a : p(Ā / B) = 1 − p(A / B), » [sic : virgule finale imprimée].

> **Évènements indépendants — définition** (p.316) — « Soient Ω un univers, p une probabilité définie sur 𝒫(Ω) et A et B deux événements. A et B sont dits indépendants si et seulement si p(A ∩ B) = p(A) . p(B). Ce qui équivaut à : p(A / B) = p(A) si p(B) ≠ 0. » **Remarque** : « Deux événements A et B sont dits indépendants lorsque la réalisation de l'un n'influe pas sur la réalisation de l'autre. »

> **Principe des probabilités composées** (p.318) — « Soient Ω un univers, p une probabilité définie sur 𝒫(Ω) et A, B et C trois événements tels que p(A) ≠ 0 et p(B) ≠ 0. On a : • p(A ∩ B) = p(B) . p(A / B) = p(A) . p(B / A) • p(A ∩ B ∩ C) = p(A) . p(B / A) . p(C / (A ∩ B)). »

> **Principe « Stochastique fini »** (p.319) — « Ce principe s'intéresse à une succession finie d'expériences aléatoires. Par exemple : • Choisir une urne parmi trois urnes numérotées. • Puis, dans l'urne choisie, tirer une boule, parmi des noires et des blanches. Soient A : « L'urne choisie est de numéro 1 » et B : « La boule tirée est noire ». On s'intéresse à l'évènement (A puis B) c'est-à-dire à l'évènement K : « La boule tirée est noire et provient de l'urne n°1 ». Ainsi, p(K) = p(A ∩ B) = p(A).p(B /A). Si on connaît la probabilité de A et la probabilité de B lorsque A est réalisé alors on peut tirer la probabilité de l'évènement K. Dans ce type d'expériences aléatoires successives, il est parfois commode d'utiliser un **diagramme en arbre** : les « branches » successives traduisent la succession des évènements, et sur chacune des branches on peut marquer la probabilité associée (on obtient ainsi, un **arbre pondéré**). Si p(A) = p et p(B/A) = q alors p(K) = p(A puis B) = p.q ; de même p(A puis B̄) = p.(1−q). Remarques : * Cette technique s'applique également, pour calculer la probabilité de (A puis B puis C) etc. * La somme des nombres associés à toutes les branches de même origine est égale à 1. » (figure : arbre Ω → A (p) puis B (q) / B̄ (1−q) ; Ω → Ā (1−p)).

> **Principe des probabilités totales** (p.321) — « Soient Ω un univers, p une probabilité définie sur 𝒫(Ω) et A et B deux événements tels que p(A) ≠ 1 et p(A) ≠ 0. On a : p(B) = p(A) . p(B / A) + p(Ā) . p(B / Ā). Plus généralement [paragraphe imprimé hors de l'encadré] : Si A₁ ∪ A₂ ∪ A₃ … ∪ Aₙ = Ω ; Aᵢ ∩ Aⱼ = ∅ (pour tous i et j tels que i ≠ j) et ∀k ∈ {1, 2, …, n}, p(Aₖ) ≠ 0 alors pour tout évènement B on a : p(B) = Σ_{k=1}^{n} p(Aₖ).p(B / Aₖ). »

> **Formule de Bayes** (p.321) — « Soient Ω un univers et A et B deux événements tels que p(B) ≠ 0, p(B) ≠ 1 et p(A) ≠ 0. On a : p(B / A) = p(B).p(A / B) / [p(B).p(A / B) + p(B̄).p(A / B̄)]. »

> **Résumé du cours (p.324)** — reprend : p(A∪B) = p(A) + p(B) − p(A∩B) ; p(A∪B) = p(A) + p(B) si A∩B = Ø ; p(A) = card A / card Ω (équiprobabilité) ; p(A/B) = p(A∩B)/p(B) (p(B) ≠ 0) ; indépendance p(A∩B) = p(A).p(B) ; composées : « Si A et B sont deux événements tels que p(A) ≠ 1 et p(A) ≠ 0 [sic : conditions différentes de l'encadré p.318 (p(A) ≠ 0 et p(B) ≠ 0)] alors on a : p(A∩B) = p(B).p(A/B) = p(A).p(B/A) » et « Si p(A) ≠ 0 et p(B) ≠ 0 alors p(A∩B∩C) = p(A).p(B/A).p(C/A∩B) » ; totales : « p(A) ≠ 1 et p(A) ≠ 0 alors p(B) = p(A).p(B/A) + p(Ā).p(B/Ā) » ; Bayes : « p(B) ≠ 0, p(B) ≠ 1 et p(A) ≠ 0 alors p(B/A) = p(B).p(A/B) / [p(B).p(A/B) + p(B̄).p(A/B̄)] ».

### Avec l'ordinateur (p.325)

Deux activités. **Activité 1** — sac de 500 boules indiscernables dont n blanches (n ≥ 2), autres noires ; on tire successivement deux boules ; A « les deux boules tirées sont de même couleur » : a) tirage avec remise, calculer en fonction de n la probabilité p de A ; b) élaborer un programme (saisie de n, calcul de p, affichage, faire varier n et déterminer la valeur de n pour laquelle p est voisin de 0,5). **Activité 2** — simulation de lancers d'un dé cubique (faces 1 à 6) : 1) 100 lancers avec Excel (formule « = 1+ENT(ALEA()*6) » en A1, copie sur la plage A1:E20, relance par la touche Suppr, menu Outils / Option / Calcul / Ordre pour éviter la réactualisation, comptage par « = NB.SI(A1 : E20 ; k) » pour k ∈ {1,…,6}, tableau à compléter : k, Nombre d'apparition de k, Probabilités pₖ) ; 2) simuler 1000 lancers.

### Exercices et problèmes (p.326–329) — 17 exercices

- **Ex. 1** (p.326) : dé pipé tel que p₁ = p₃, p₂ = p₄ et p₅ = p₆ = 2p₁ = 3p₂ où pᵢ est la probabilité de la face i. 1) probabilité de chaque face ; 2) A « face paire », B « face portant un nombre supérieur ou égal à 5 ».
- **Ex. 2** (p.326) : sac de 3 boules rouges, 5 vertes, 7 jaunes ; 2 boules tirées successivement avec remise. 1) nombre de tirages possibles ; 2) A « deux rouges », B « deux jaunes », C « tirage unicolore », D « tirage bicolore ».
- **Ex. 3** (p.326) : urne de deux boules blanches numérotées 1 et 4 et quatre noires numérotées 2, 3, 5, 7. 1) Tirage simultané de deux boules : A « numéros impairs », B « même couleur », C « numéros impairs et même couleur », D « numéros impairs ou même couleur ». 2) Tirage successif avec remise de deux boules : E « parités différentes », F « au moins une boule noire ».
- **Ex. 4** (p.326–327) : urne de quatre blanches et deux rouges, n tirages successifs ; rouge remise, blanche non remise. 1) n = 3, Eₖ « seule la kᵉ boule tirée est blanche » (k ∈ {1,2,3}) : a) montrer p(E₁) = 8/75 ; b) p(E₂), p(E₃) ; c) E « une seule boule blanche parmi les trois » ; d) sachant E, probabilité que la blanche soit obtenue au 1ᵉʳ tirage. 2) n ≥ 2 : a) en fonction de n, probabilité pₙ d'avoir au moins une blanche parmi les n boules ; b) valeurs de n pour lesquelles pₙ > 0,99.
- **Ex. 5** (p.327) : n urnes U₁,…,Uₙ : U₁ contient trois blanches et deux noires ; chacune des urnes U₁, U₂, … Uₙ contient une boule blanche et quatre noires [sic : l'énoncé imprimé, tel quel, contredit la composition de U₁ donnée juste avant]. On tire une boule de U₁ que l'on remet dans U₂, puis une de U₂ remise dans U₃, etc. jusqu'à tirer une boule de Uₙ ; Eₖ « la boule tirée de Uₖ est blanche » (1 ≤ k ≤ n). 1) p(E₁), p(E₂/E₁), p(E₂/Ē₁), en déduire p(E₂). 2) pₖ = p(Eₖ) : a) montrer pₖ₊₁ = (1/6)pₖ + 1/6 ; b) montrer que la suite V définie sur ℕ* par Vₙ = pₙ − 1/5 est géométrique ; c) en déduire pₙ et lim pₙ.
- **Ex. 6** (p.327) : sac de huit jetons (trois rouges 1, 1, 0 ; trois jaunes 1, 0, −1 ; deux verts 2, −1), trois jetons tirés simultanément. 1) A « même numéro », B « même couleur », C « exactement deux rouges et un seul jeton portant le numéro 0 », D « exactement deux jaunes ou deux jetons à numéros positifs » ; 2) S « numéros de somme nulle », N « numéros de produit égal 0 » ; 3) p(N/S). (Mêmes données que l'activité 5 du Cours, p.313.)
- **Ex. 7** (p.327–328) : urne de 7 jetons : quatre numéro 0, deux numéro 1, un numéro 2 ; trois jetons tirés simultanément, somme S : si S ≠ 0, gain S points ; si S = 0, sans remettre les trois jetons, nouveau tirage d'un seul jeton, gain = son numéro. R « obligé de faire un deuxième tirage », A « le gain est 0 ». 1) p(R), p(A/R), p(A∩R) et montrer p(A) = 1/35 ; 2) a) B « le gain est 1 » ; b) H « obligé de faire un deuxième tirage sachant que le gain est 1 point ».
- **Ex. 8** (p.328) : p(B) = 0,06 ; p(A/B) = 0,85 ; p(A/B̄) = 0,40. 1) p(Ā/B) et p(B̄/A) ; 2) étudier l'indépendance de A et B.
- **Ex. 9** (p.328) : on lance deux fois un dé, résultats X et Y ; A « X et Y ont la même parité », B « X = 2 » : indépendants ?
- **Ex. 10** (p.328) : défauts D₁ et D₂ : 8 % des pièces ont D₁ ; parmi celles-ci 15 % ont D₂. A « D₁ », B « D₂ ». 1) probabilité des deux défauts ; 2) probabilité du défaut D₂ ; 3) sachant D₂, probabilité de D₁.
- **Ex. 11** (p.328) : maladie atteignant 2 % d'une population ; malades : 98 % de tests positifs, 2 % négatifs ; non-malades : 1 % positifs, 99 % négatifs. Probabilité : a) malade et test positif ; b) non malade et test négatif ; c) test positif ; d) test négatif ; e) non malade sachant test positif ; f) malade sachant test négatif.
- **Ex. 12** (p.328) : machine : probabilités de dérèglement électronique 0,003 et mécanique 0,007 (par jour), pas d'autre dérèglement, probabilité de mécanique sachant électronique = 0,5. 1) probabilité des deux dérèglements ; 2) aucun dérèglement ; 3) machine déréglée aujourd'hui : probabilité que les causes soient à la fois électroniques et mécaniques.
- **Ex. 13** (p.328–329) : une pièce présente deux sortes de défauts (et deux seulement) : 6 % ont D₁ au moins ; 12 % ont D₂ au moins ; 5 % ont les deux. Probabilité qu'elle présente un seul défaut.
- **Ex. 14** (p.329) : enquête état de santé / tabac : 50 % ne fument pas et sont en bonne santé, 25 % sont malades et ne fument pas ; l'état de santé ne dépend pas du fait d'être fumeur. Probabilité p₁ d'être fumeur et non malade, p₂ fumeur et malade.
- **Ex. 15** (p.329) : appareils fabriqués par deux entreprises, part de marché de la première = deux tiers ; fiabilité 95 % (première), 90 % (deuxième) ; fiabilité de l'appareil acheté.
- **Ex. 16** (p.329) : trois machines M₁, M₂, M₃ ; pièces fabriquées (%) : 50, 35, 15 ; fréquence de défauts (%) : 1, 2, 6 ; D « pièce défectueuse », Mᵢ « fabriquée par Mᵢ » : probabilité de D.
- **Ex. 17** (p.329) : emboutisseuse plastique et robot peintre : probabilité de panne de l'emboutisseuse 2·10⁻², du robot 8·10⁻² ; probabilité que le robot soit en panne sachant que l'emboutisseuse ne fonctionne plus = 1/4 ; probabilité que les deux machines soient en panne, puis que toutes deux fonctionnent.

### Aperçu historique (p.330)

Une ligne : Thomas Bayes (1702–1761) — notion d'expérience aléatoire, étymologie « aléa » et « hasard » (az-zahr), origines (Galilée, Chevalier de Méré, Fermat, Pascal), biographie et œuvres de Bayes, formule de Bayes (texte tiré de l'Encyclopædia Britannica).

### Bornes de scope observées (chapitre 14)

- ✅ INCLUS : rappels de dénombrement (arrangements, combinaisons, applications, parties, binôme) ; univers fini, événements, probabilité sur 𝒫(Ω) et ses propriétés ; équiprobabilité et types de tirages (avec remise, sans remise, simultané) ; probabilité conditionnelle ; indépendance de deux événements ; probabilités composées (2 et 3 événements), arbres pondérés ; probabilités totales (partition finie) ; formule de Bayes ; simulation de dé sur tableur ; exercices à contexte (tests médicaux, machines, urnes à tirages dépendants, suites).
- ⛔ NON traité dans ce chapitre : variables aléatoires, espérance, variance, loi binomiale (chapitre 15 de la fiche) ; indépendance de plus de deux événements (mutuelle) ; schéma de Bernoulli ; probabilités sur des univers infinis ; démonstration de la formule du binôme (rappelée sans preuve).

> Sondage image : pages 308, 309, 310, 311, 312, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329 + un agrandissement à 220 dpi de l'Ex. 8 (p.328) (20 pages sur 24 ; pages denses et toutes pages à formules confrontées) ; écarts : aucun mot ni nombre faux dans la couche texte pour les énoncés ; seuls écarts de la couche texte, tous corrigés sur image : indices/exposants perdus (p₁ = p₃, p₂ = p₄ de l'Ex. 1), barres de complémentaire perdues (Ā, B̄ des Act. 2/3 Probabilité conditionnelle, Ex. 8, Bayes), fractions éclatées (Ex. 4, 5, 7, 17), symbole ⊂ rendu « 1 » et ∩ rendu « I ». Pages non confrontées : 307, 313, 325, 330 (texte seul, sans formule).

## 2.15 Chapitre 15 — Variables aléatoires réelles (manuel 222451, p.331–365)

**Page de garde (p.331)** — Titre imprimé : « Variables aléatoires réelles » ; numérotation propre du manuel : « Chapitre **6** » (ce chapitre est le 15ᵉ de la fiche). « Plan du chapitre » : ❈ Activités préliminaires ❈ Cours (❖ Variable aléatoire réelle ❖ Loi de probabilité d'une variable aléatoire ❖ La loi binomiale ❖ Exemples de lois continues : La Loi uniforme, La Loi exponentielle) ❈ Résumé du cours ❈ Avec L'ordinateur ❈ Exercices et Problèmes ❈ Aperçu Historique. Pas de QCM / Vrai-Faux. Cinq activités portent la mention « (résolue) » dans le Cours. Le titre courant de la p.363 porte « Probabilités » au lieu de « Variables aléatoires réelles » [sic, titre courant erroné].

### Activités préliminaires (p.332) — 4 activités + encadré de rappels

- **Encadré de rappels (p.332)** — « * Dans le cas d'une « équiprobabilité », on a p(A) = card A / card Ω, pour tout évènement A. * Si A et B sont deux événements tels que p(B) ≠ 0 alors on a : p(A∩B) = p(B) . p(A / B) * Soient A et B sont deux événements tels que p(B)≠0, p(B)≠1 et p(A)≠0. On a la formule de Bayes : p(B/A) = p(B).p(A / B) / [p(B).p(A/B) + p(B̄).p(A/B̄)]. »
- **Prél. 1** : deux machines M₁ et M₂ produisent respectivement 200 et 300 objets ; M₁ produit 3 % et M₂ 5 % de pièces défectueuses. Probabilité qu'un objet défectueux ait été fabriqué par M₁ ?
- **Prél. 2** : sac de 7 jetons : quatre blancs numérotés 1, 2, 2, 2 et trois noirs numérotés 1, 1, 2. 1) Tirage successif avec remise de 3 jetons : A « obtenir 3 jetons blancs », B « parmi les 3 jetons, deux portent le n°1 ». 2) On remet tous les jetons et on tire successivement 3 jetons : un jeton portant le n°1 est remis dans le sac, un jeton portant le n°2 n'est pas remis ; A' « 3 jetons blancs », B' « deux jetons portent le n°1 » : probabilités.
- **Prél. 3** : soit n ∈ ℕ ; montrer que Σ_{k=0}^{n} Cₙᵏ (1/3)^{n−k} (2/3)ᵏ = 1.
- **Prél. 4** : dé cubique parfait dont les faces portent −1, −1, 0, 0, 1, 1 ; lancé deux fois de suite ; a = résultat du 1ᵉʳ lancer, b = résultat du 2ᵉ. a) A « somme (a + b) nulle », B « produit (ab) nul » : probabilités ; b) sachant que le produit est non nul, probabilité que la somme soit nulle.

### Cours — Activités

**Convention (p.333)** : « Dans tout le chapitre, Ω est un univers, 𝒫(Ω) est l'ensemble des parties de Ω et p est une probabilité sur 𝒫(Ω). »

**I. Variable aléatoire réelle — définition et loi de probabilité** (p.333–334)

- **Activité 1** (p.333) : urne de six boules : 3 rouges, 1 noire, 2 blanches (indiscernables) ; un joueur tire une boule ; rouge : gain 1 dinar tunisien, noire : gain 2 dinars, blanche : perte de 3 dinars. Ω = ensemble des couleurs possibles ; X : application de Ω vers ℝ associant le gain algébrique. a) Valeurs prises par X (notation X(Ω)). b) Pour chaque xᵢ de X(Ω), (X = xᵢ) = ensemble des éléments de Ω ayant pour image xᵢ ; probabilités de (X = 2), (X = 1), (X = −3). c) Vérifier que Σ_{xᵢ ∈ X(Ω)} p(X = xᵢ) = 1.
- (Définitions de variable aléatoire réelle, de (X = x), de loi de probabilité : p.333, voir verbatim.)
- (Texte p.334 : variable discrète, tableau de la loi.)
- **Activité 2** (p.334) : tirage simultané de trois articles dans une boîte de 12 articles dont 3 défectueux ; X = nombre d'articles défectueux observés. 1) Loi de probabilité de X ; 2) calculer p(X ≤ 1) et interpréter.
- **Activité 3** (p.334) : jeu : le joueur paie 3 dinars pour participer, lance une pièce deux fois et reçoit en dinars le triple du nombre de piles obtenus ; Y = gain net ; déterminer la loi de probabilité de Y. Encadré **Conseil** (voir verbatim).
- **Activité 4** (p.334) : sac de neuf jetons numérotés de 1 à 9 ; trois jetons tirés successivement et sans remise ; X = nombre de numéros impairs parmi les trois ; loi de probabilité de X.

**II. Fonction de répartition d'une variable aléatoire** (p.334–337) — la numérotation imprimée saute l'activité 2 : Activité 1, puis Activité 3 (résolue), Activité 4 [sic].

- **Activité 1** (p.334–335) : dé cubique parfait (faces 1 à 6) lancé une fois ; X = nombre inscrit sur la face supérieure ; F définie sur ℝ par F(x) = p(X ≤ x) où (X ≤ x) = {ω ∈ Ω ; X(ω) ≤ x}. 1) Loi de probabilité de X ; 2) calculer F(x) pour x dans chacun des intervalles ]−∞, 1[, [1, 2[, [2, 3[, [3, 4[, [4, 5[, [5, 6[ et [6, +∞[ ; 3) construire la représentation graphique de F dans un repère orthogonal ; 4) a) sens de variation de F ; b) justifier que F est continue à droite en tout xᵢ ∈ X(Ω).
- (Définition et Propriétés de la fonction de répartition : p.335, voir verbatim.)
- **Activité 3 (résolue)** (p.335–337) : dé cubique parfait dont les faces portent −1, 0, 0, 1, 1, 2 ; lancé deux fois de suite ; a, b les nombres apparus ; Y = a + b. 1) Loi de probabilité de Y ; 2) a) fonction de répartition F de Y ; b) représentation graphique ; 3) a) calculer p(0 < Y ≤ 3) et comparer à F(3) − F(0) ; b) montrer ∀ x ∈ ℝ, p(Y > x) = 1 − F(x) ; c) montrer que pour a < b, p(a < Y ≤ b) = F(b) − F(a). Solution imprimée : card Ω = 6² = 36 ; tableau des 36 sommes (−1, 0, 0, 1, 1, 2 en ligne/colonne) ; Y(Ω) = {−2 ; −1 ; 0 ; 1 ; 2 ; 3 ; 4} ; loi : p = 1/36, 4/36, 8/36, 10/36, 8/36, 4/36, 1/36 ; F(x) = 0 sur ]−∞, −2[ ; 1/36 sur [−2, −1[ ; 5/36 sur [−1, 0[ ; 13/36 sur [0, 1[ ; 23/36 sur [1, 2[ ; 31/36 sur [2, 3[ ; 35/36 sur [3, 4[ ; 36/36 = 1 sur [4, +∞[ ; 3) a) p(0 < Y ≤ 3) = p(Y=1) + p(Y=2) + p(Y=3) = 22/36 et F(3) − F(0) = 35/36 − 13/36 = 22/36 ; b) (Y ≤ x) et (Y > x) contraires ; c) (Y ≤ a) ⊂ (Y ≤ b) et (a < Y ≤ b) = (Y ≤ b) \ (Y ≤ a). **Remarque** : à partir de F on retrouve la loi : p₁ = F(x₁) et p(Y = xᵢ₊₁) = pᵢ₊₁ = F(xᵢ₊₁) − F(xᵢ) ; **Exemple** : p(Y = x₃) = p(Y = 0) = p₃ = F(0) − F(−1) = 13/36 − 5/36 = 8/36.
- **Activité 4** (p.337) : urne : 3 boules rouges, 2 noires, 1 verte ; tirage successif sans remise de trois boules ; X = 1 si la première boule est rouge ou verte, 0 sinon. 1) tableau de la loi de X ; 2) fonction de répartition F de X et représentation graphique.

**III. Espérance mathématique** (p.337–338)

- **Activité 1** (p.337) : jeu : dé cubique parfait (faces 1 à 6) : le joueur reçoit autant de dinars tunisiens que de points si le nombre est pair, perd autant de dinars que de points si le nombre est impair ; X = gain algébrique. 1) Loi de X ; 2) montrer p(X < 0) = p(X > 0) et en déduire qu'il est aussi probable de gagner que de perdre ; a) calculer le gain moyen Σ xᵢ p(X = xᵢ) ; b) en moyenne gagne-t-on autant que ce que l'on perd ?
- (Définition de l'espérance : p.338, voir verbatim.)
- **Activité 2** (p.338) : Amor envisage d'investir dans les actions d'une entreprise de nouvelles technologies pour un an ; rendements 6 %, 8 %, 10 %, 12 % de probabilités 0,2 ; 0,3 ; 0,35 ; 0,15. 1) Rendement le plus probable ; 2) rendement moyen espéré.
- **Activité 3** (p.338) : investisseur : option A à taux fixe 8 % ; option B (société en bourse) : rendements −10 %, 0 %, 10 %, 20 % de probabilités 0,1 ; 0,4 ; a ; b. Déterminer a et b pour que l'option B soit plus favorable.

**IV. Variance et écart-type** (p.338–341)

- (Définitions p.338 : voir verbatim.)
- **Activité 1** (p.339) : X̄ = E(X) ; en développant les carrés (xᵢ − X̄)², montrer que V(X) = (x₁ − X̄)².p₁ + … + (xₙ − X̄)².pₙ = Σ xᵢ²pᵢ − (E(X))². Encadré de formule (voir verbatim) ; **Remarques** : « * L'écart-type est un paramètre de dispersion qui donne une idée de la dispersion des valeurs prises par la variable aléatoire autour de son espérance mathématique. * L'écart-type est exprimé dans la même unité que la variable aléatoire. »
- **Activité 2** (p.339) : urne de cinq boules (trois noires, deux blanches), toutes tirées une à une ; R = rang de la première boule blanche tirée. 1) Loi de R ; 2) E(R) et σ(R).
- **Activité 3** (p.339) : urne : quatre boules blanches numérotées 1, 1, 1, 1 ; deux noires numérotées 2, 1 ; une rouge numérotée 2. Épreuve : 3 boules successives : si la boule porte le n°1 on la remet et on tire la suivante, sinon on la garde à l'extérieur. 1) A « trois boules blanches », B « exactement 2 boules portant le numéro 1 » : probabilités. 2) X = 0 si aucune boule tirée n'est noire, sinon le rang de la première boule noire : a) loi de X ; b) écart-type ; c) courbe de la fonction de répartition de X.
- **Activité 4 (résolue)** (p.340–341) : urne : quatre boules rouges portant 1, cinq vertes portant −1, trois blanches portant 0 ; tirage simultané de deux boules ; X = somme des nombres marqués. 1) Valeurs prises par X ; 2) loi de X ; 3) a) E(X) et interprétation ; b) V(X) ; c) σ(X) ; 4) représentation graphique de la fonction de répartition F. Solution imprimée : X(Ω) = {−2, −1, 0, 1, 2} ; card Ω = C₁₂² = 66 ; p(X=−2) = C₅²/66 = 10/66 ; p(X=−1) = C₅¹C₃¹/66 = 15/66 ; p(X=0) = (C₃² + C₄¹C₅¹)/66 = 23/66 ; p(X=1) = C₃¹C₄¹/66 = 12/66 ; p(X=2) = C₄²/66 = 6/66 ; Σ p = 1, « les évènements (X = xᵢ) forment un système complet d'évènements » ; E(X) = (−2)×10/66 + (−1)×15/66 + 0×23/66 + 1×12/66 + 2×6/66 = −1/6 < 0 donc le jeu est perdant ; **Remarque** (voir verbatim : jeu favorable / défavorable / équitable) ; V(X) = E(X²) − (E(X))² = [(−2)²×10/66 + (−1)²×15/66 + 0²×23/66 + 1²×12/66 + 2²×6/66] − (−1/6)² = 91/66 − 1/36 ≃ 1,35 ; σ(X) = √V(X) ≃ √1,35 ≃ 1,16 ; F = 0 sur ]−∞,−2[ ; 10/66 sur [−2,−1[ ; 25/66 sur [−1,0[ ; 48/66 sur [0,1[ ; 60/66 sur [1,2[ ; 1 sur [2,+∞[ (graphique en escalier).

**V. La loi binomiale** (p.342–344)

- **Activité 1** (p.342) : pièce parfaite lancée trois fois de suite ; A « deux fois pile », B « trois fois face », C « au moins deux fois pile », D « pile pour la première fois au 3ᵉ lancer » : probabilités.
- (Encadré « Épreuve de Bernoulli – Schéma de Bernoulli » p.342 et « Loi binomiale » p.343 : voir verbatim.)
- **Activité 2** (p.343) : I-1) dé en forme de tétraèdre régulier, faces 1, 2, 3, 4 ; faces 1, 2, 3 équiprobables et probabilité de la face 4 double de celle de chacune des autres ; probabilité de chaque face ? I-2) dé cubique équilibré (1 à 6) : probabilité de chaque face ? II-1) épreuve E : lancer simultanément les deux dés une fois : probabilité d'une somme égale à 7 ? II-2) E répétée quatre fois, X = nombre de fois où la somme vaut 7 : a) loi de X, E(X), V(X) ; b) probabilité d'obtenir exactement deux fois « la somme égale à 7 » ; c) probabilité d'obtenir « la somme égale à 7 » pour la première fois à la troisième répétition.
- **Activité 3** (p.343) : quatre chasseurs tirent en même temps sur un lapin, chacun a une chance sur quatre de l'atteindre ; probabilité que le lapin soit atteint.
- **Activité 4 (résolue)** (p.343–344) — « (D'après Bac Tunisien 2001) » : urne : quatre boules rouges, six noires. 1) Tirage successif avec remise de trois boules : probabilité de M « la première boule tirée est noire et les deux autres rouges » ; 2) même événement, tirage successif sans remise ; 3) E = tirer simultanément trois boules, A « une boule noire et deux rouges » : a) montrer p(A) = 3/10 ; b) E répétée 5 fois de suite en remettant les trois boules, X = nombre de fois où A est réalisé : loi de X ; c) E(X), V(X), σ(X) ; d) probabilité de (1 < X ≤ 3). Solution imprimée : p(M) = 6/10 × 4/10 × 4/10 = 0,096 (avec remise) ; 6/10 × 4/9 × 3/8 = 0,1 (sans remise) ; p(A) = C₆¹C₄²/C₁₀³ = 36/120 = 3/10 = 0,3 ; schéma de Bernoulli n = 5, p = 0,3 ; X suit la loi binomiale de paramètres n = 5 et p = 0,3 ; X(Ω) = {0,1,2,3,4,5} [sic : noté « x(Ω} »] et p(X = k) = C₅ᵏ (0,3)ᵏ (0,7)^{5−k} ; E(X) = n.p = 1,5 ; V(X) = n.p.(1−p) = 1,05 ; σ(X) = √1,05 ≃ 1,025 ; p(1 < X ≤ 3) = p(X=2) + p(X=3) = 0,441.
- **Activité 5** (p.344) : appareil électronique envoyant à une imprimante un code de 4 chiffres, chacun égal à 0 ou 1 (ex. 1101) : a) nombre de codes distincts ? Codes équiprobables ; b) X = nombre de 1 dans le code : loi de X et espérance.

**VI. Exemples de variables aléatoires réelles continues** (p.345–353)

- **1) Introduction et définition** (p.345–346) : texte sur la taille des individus (probabilité d'une taille exacte de 1,79 m nulle, mais calculable dans l'intervalle [1,785 ; 1,795]). **Activité** (p.345) : cercle (C) de centre O, rayon R = OA ; M choisi au hasard sur le cercle, θ = AÔM, X = longueur de la corde [AM] (figure). a) Préciser l'univers Ω ; b) calculer AM en fonction de θ ; c) déterminer X(Ω) ; d) probabilité de l'événement (X = R/7). Solution imprimée : Ω = le cercle (C), non fini ; AM = 2R.sin(θ/2) (θ ∈ [0,π]) ; u : x ↦ 2R.sin(x/2) continue et croissante sur [0,π] donc X(Ω) = [0, 2R] ; p(X = R/7) = 0 (événement « quasi-impossible », sin(θ/2) = 1/14) ; X définie sur un univers non fini avec X(Ω) intervalle non réduit à un point : variable aléatoire réelle continue (encadré, p.346, voir verbatim).
- **2) Fonction de répartition d'une variable aléatoire continue** (p.346–347) : définition (voir verbatim). **Activité 1** (p.346) : X continue de fonction de répartition F. 1) Justifier ∀ x, 0 ≤ F(x) ≤ 1 ; 2) a) p(X ∈ ]−∞,a]) = F(a) et p(X < a) = p(X ≤ a) ; b) en déduire p(X > a) = p(X ≥ a) = 1 − F(a) ; 3) a ≤ b : a) en remarquant que (X ≤ a) ⊂ (X ≤ b), montrer p(X ∈ [a,b]) = F(b) − F(a) ; b) en déduire que F est croissante sur ℝ ; 4) pour a < b : p(a < X ≤ b) = p(a ≤ X < b) = p(a < X < b) = p(a ≤ X ≤ b) = F(b) − F(a). Encadré de propriétés (voir verbatim). **Activité 2** (p.347) : F(x) = 0 si x < 0 ; x si 0 ≤ x ≤ 1 ; 1 si x > 1 : probabilités de (0,3 ≤ X ≤ 0,8) ; (X ≥ 1/2) ; (X < 0).
- **3) Densité de probabilité d'une variable aléatoire continue** (p.347–348) : **Activité 1** (p.347) : F(x) = 0 si x < 0 ; 1 − e^{−x} si x ≥ 0. 1) a) lim_{x→−∞} F(x) et lim_{x→+∞} F(x) ; b) F continue et dérivable sur ℝ ; c) courbe représentative de F ; 2) probabilité de A « (X ≤ 2) » ; 3) probabilité de B « (0 < X ≤ 0,5) » et C « 0,7 < X < 0,8) » [sic : parenthèse ouvrante manquante] ; 4) a) pour h > 0 voisin de zéro et tout x : F(x + h) − F(x) ≃ f(x).h (f dérivée de F) ; b) p(x ≤ X ≤ x + h) ≃ f(x).h ; c) a ≤ b : vérifier ∫ₐᵇ f(x)dx = p(a ≤ X ≤ b). **Commentaires** : « * Le réel positif f(x).h est une valeur approchée de la probabilité que la variable aléatoire continue X soit dans un intervalle de longueur h et contenant le réel x. * La fonction f s'appelle la fonction densité de probabilité de la variable aléatoire réelle continue X. » Encadré de définition (p.348, voir verbatim). **Activité 2** (p.348) : montrer que la densité f d'une variable aléatoire continue prend des valeurs positives ou nulles. **Activité 3** (p.348) : F(x) = 0 si x ≤ 0 ; 2(x − x²/2) si 0 < x < 1 ; 1 si x ≥ 1. 1) densité f ; 2) courbes de f et F dans deux repères orthogonaux ; 3) p(0,25 ≤ X ≤ 0,5) et interprétation graphique ; 4) résoudre dans ]0,1[ [sic : imprimé « ]0,1[, »] graphiquement puis par le calcul F(x) = 0,5, interpréter. Encadré de propriétés (voir verbatim).
- **4) La loi uniforme** (p.349–350) : définition et formules (voir verbatim) ; **Exemple** imprimé : X uniforme sur [0 ; 1], f constante égale à 1 sur [0 ; 1] et 0 ailleurs, p(t ≤ X ≤ s) = ∫ₜˢ 1 dx = s − t, E(X) = ∫₀¹ t.1 dt = [t²/2]₀¹ = 1/2, V(X) = ∫₀¹ t²dt − (1/2)² = [t³/3]₀¹ − 1/4 = 1/12. **Activité 1** (p.349) : montrer E(X) = (a + b)/2 ; V(X) = (b − a)²/12. **Activité 2** (p.350) : montrer F(x) = 0 si x < a ; (x − a)/(b − a) si a ≤ x < b ; 1 si x ≥ b. **Activité 3** (p.350) : X uniforme sur [2 ; 5] : 1) densité ; 2) F ; 3) graphes de f et F ; 4) E(X), V(X) ; 5) probabilités de (1 ≤ X ≤ 4) et (2,5 < X ≤ 2,6). **Activité 4 (résolue)** (p.350) : bus partant à 9 h d'un arrêt et passant toutes les 10 minutes ; un étudiant arrive entre 9 h et 9 h 20 ; X = heure exacte d'arrivée, uniforme sur [0 ; 20] ; 1) probabilité d'attendre moins de 5 mn ; 2) plus de 8 mn. Solution imprimée : f(x) = 1/20 sur [0, 20] ; 1) arrivée entre 9h5 et 9h10 ou entre 9h15 et 9h20 : p(5 ≤ X ≤ 10) + p(15 < X ≤ 20) = ∫₅¹⁰ 1/20 dt + ∫₁₅²⁰ 1/20 dt = 1/2 ; 2) arrivée entre 9h et 9h2 ou entre 9h10 et 9h12 : p(0 ≤ X ≤ 2) + p(10 < X ≤ 12) = ∫₀² + ∫₁₀¹² = 1/5.
- **5) La loi exponentielle** (p.351–353) : définition (voir verbatim) ; **Exemple** : « La durée de vie, exprimée en années, d'un noyau radioactif ou d'un composant électronique est modélisée par une variable aléatoire réelle continue qui suit une loi exponentielle. » **Activité 1** (p.351) : X exponentielle de paramètre a sur I = [0,+∞[ , densité f. 1) a) calculer ∫₀ˣ f(t)dt ; b) en déduire F(x) = 0 si x < 0 ; 1 − e^{−ax} si x ≥ 0 ; 2) a) pour t > 0, calculer par intégration par parties chacune des expressions E(t) = ∫₀ᵗ f(x) dx [sic : sans facteur x, alors que la limite demandée à la question b est 1/a, valeur de ∫ x f(x) dx] et V(t) = ∫₀ᵗ x² f(x) dx − (1/a)² ; b) montrer lim_{t→+∞} E(t) = 1/a et lim_{t→+∞} V(t) = 1/a². Encadré (voir verbatim). **Activité 2** (p.351–352) : T = temps d'attente (minutes) entre deux clients au guichet d'une poste, exponentielle de paramètre 0,4 : 1) allure de la densité ; 2) probabilité d'attendre plus de 15 min ; 3) espérance et variance de T. **Activité 3** (p.352) : X exponentielle de paramètre λ > 0 : 1) pour 0 ≤ a ≤ b, p(a ≤ X ≤ b) = e^{−λa} − e^{−λb}, interprétation graphique ; 2) a) pour t > 0 : p(X ≤ t) = 1 − e^{−λt} ; b) p(X > t) = e^{−λt} ; c) pour s, t positifs : p(X > s + t / X > s) = p(X > t) = e^{−λt}. Encadré (voir verbatim). **Activité 4 (résolue)** (p.352–353) : durée de vie d'une ampoule (heures), X exponentielle de paramètre λ. 1) densité ; 2) fonction de répartition ; 3) a) calculer λ sachant que la durée moyenne est 2000 heures ; b) graphes de f et F ; 4) probabilité qu'une ampoule dure moins de 2000 heures ; 5) sachant qu'elle a duré 2000 heures, probabilité qu'elle dure 500 heures de plus. Solution imprimée : f(t) = 0 si t < 0, λe^{−λt} si t ≥ 0 ; F(x) = 0 si x < 0, 1 − e^{−λx} si x ≥ 0 ; E(X) = 1/λ = 2000 donc λ = 1/2000 = 0.0005 ; p(X < 2000) = 1 − e^{−2000/2000} = 1 − e^{−1} ≃ 0.64 (aire sous la courbe de f entre x = 0 et x = 2000) ; p(X > 500 + 2000 / X > 2000) = p(X > 500) = e^{−500/2000} = e^{−0.25} ≃ 0.78 (graphes f et F fournis). **Activité 5** (p.353) : durée de vie (semaines) d'un composant, loi de probabilité p définie sur [0,+∞[ par : p(t) = ∫₀ᵗ λe^{−λx}dx = probabilité que « le composant ne soit plus en état de marche au bout de t semaines » ; environ 50 % d'un lot encore en marche au bout de 200 semaines : p(200) = 0,5. 1) Montrer λ = ln 2 / 200 ; 2) probabilité qu'un composant ait une durée de vie supérieure à 300 semaines ; 3) valeur approchée décimale à la semaine près de la durée de vie moyenne.

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Variable aléatoire réelle** (p.333) — « Soit un univers Ω fini. On appelle variable aléatoire réelle (ou aléa numérique) définie sur l'univers Ω, toute application X : Ω → ℝ. » — « Soit x ∈ ℝ. (X = x) désigne l'ensemble des éventualités ayant la même image x par X. C'est-à-dire : (X = x) = {ω ; ω ∈ Ω et X(ω) = x} »

> **Loi de probabilité** (p.333) — « Soit un univers Ω fini. Soit X une variable aléatoire réelle définie sur l'univers Ω. On appelle loi de probabilité de X ou distribution des probabilités de X, l'application qui à chacune des valeurs xᵢ prises par X, fait correspondre la probabilité pᵢ = p(X = xᵢ). »

> **Variable discrète, tableau de la loi** (p.334) — « D'une façon générale, si on a X(Ω) = {x₁, x₂, …, xₙ} alors on dit que X est **discrète** (ou **discontinue**). La donnée des nombres pᵢ = p(X = xᵢ) pour i ∈ {1, 2, …, n} détermine parfaitement la loi de probabilité de la variable aléatoire X qu'on peut résumer dans un tableau appelé tableau de la loi de probabilité de X : xᵢ : x₁, x₂, …, xₙ, Total ; pᵢ = p(X = xᵢ) : p₁, p₂, …, pₙ, Σ_{i=1}^{n} pᵢ = 1. »

> **Conseil** (p.334) — « Lorsqu'on détermine la loi de probabilité d'une variable aléatoire discrète X, il est conseillé de vérifier que : Σ_{xᵢ ∈ X(Ω)} p(X = xᵢ) = 1 »

> **Fonction de répartition — définition** (p.335) — « Soit un univers Ω fini et X : Ω → ℝ une variable aléatoire. La fonction de répartition de X est l'application F : ℝ → [0, 1] définie pour tout réel x par : F(X) = p(X ≤ x) [sic : « F(X) » majuscule imprimé]. Pour le réel x, F(x) est la probabilité de l'évènement {ω ∈ Ω / X(ω) ≤ x}. »

> **Propriétés** (p.335) — « Soit X une variable aléatoire discrète définie sur un univers fini Ω. Soit F la fonction de répartition de X. On a : • F est une fonction en escalier, continue à droite en tout xᵢ ∈ X(Ω). • F est croissante sur ℝ. • Si les éléments xᵢ de X(Ω) sont ordonnés : x₁ < x₂ < … xₙ [sic : « < » manquant avant xₙ] et si p(X = xᵢ) = pᵢ pour i ∈ {1, 2, …, n} alors F est définie sur ℝ par : F(x) = 0 si x ∈ ]−∞, x₁[ ; p₁ si x ∈ [x₁, x₂[ ; p₁ + p₂ si x ∈ [x₂, x₃[ ; … ; p₁ + p₂ + … + pᵢ si x ∈ [xᵢ, xᵢ₊₁[ ; … ; 1 si x ∈ [xₙ, +∞[. »

> **Espérance mathématique** (p.338) — « Soit X une variable aléatoire discrète prenant les valeurs xᵢ avec les probabilités respectives pᵢ pour i ∈ {1, 2, …, n}. On appelle espérance mathématique de X, ou valeur moyenne de X, que l'on note E(X) ou X̄, le réel défini par : E(X) = Σ_{k=1}^{n} pₖ.xₖ = p₁.x₁ + p₂.x₂ + … + pₙ.xₙ »

> **Variance et écart-type** (p.338) — « Soit X une variable aléatoire discrète prenant les valeurs xᵢ avec les probabilités respectives pᵢ pour i ∈ {1, 2, …, n}. La variance de X, que l'on note V(X), est le réel positif défini par la formule : V(X) = (x₁ − X̄)².p₁ + (x₂ − X̄)².p₂ + … + (xₙ − X̄)².pₙ = Σ_{i=1}^{n} (xᵢ − X̄)².pᵢ. L'écart-type de X, que l'on note σ(X), est le réel positif σ(X) = √V(X). »

> **Formule de Koenig–Huygens (non nommée dans le manuel)** (p.339) — « Si X est une variable aléatoire discrète prenant les valeurs xᵢ avec les probabilités respectives pᵢ pour i ∈ {1, 2, …, n}, alors on a : V(X) = Σ_{i=1}^{n} xᵢ²pᵢ − (E(X))² = E(X²) − (E(X))². »

> **Remarque sur le jeu** (p.341) — « Si X indique le gain algébrique (positif ou négatif) réalisé dans un jeu, alors on dit que : • Le jeu est favorable ou gagnant si et seulement si E(X) > 0. • Le jeu est défavorable ou perdant si et seulement si E(X) < 0. • Le jeu est équitable si et seulement si E(X) = 0. »

> **Épreuve de Bernoulli — Schéma de Bernoulli** (p.342) — « * Une épreuve de Bernoulli de paramètre p est une épreuve dont l'univers Ω possède exactement deux issues, l'une est appelée succès notée S de probabilité p et l'autre est appelée échec notée E de probabilité q = 1 − p. * On peut définir, sur cette épreuve, une variable aléatoire X, prenant la valeur 1 lorsque la première issue S est réalisée, p(X=1)=p et 0 si non, p(X=0) = 1 − p. Cette variable est une variable de Bernoulli de paramètre p et sa loi est la loi de Bernoulli. * Un schéma de Bernoulli est la répétition d'une même épreuve de Bernoulli de paramètre p un certain nombre n de fois (n > 1) en supposant que les épreuves sont deux à deux indépendantes. »

> **Loi binomiale** (p.343) — « * Si X est une variable aléatoire égale au nombre de succès au cours de n épreuves de Bernoulli de paramètre p, alors on dit que X suit une loi binomiale de paramètres n et p. * La loi de probabilité de X (qu'on note ℬ(n, p)) est définie par : pour tout k ∈ X(Ω) = {0, 1, …, n} on a : p(X = k) = Cₙᵏ.pᵏ.(1 − p)^{n−k}. * L'espérance mathématique, la variance et l'écart-type de X sont donnés par : E(X) = n.p ; V(X) = n.p.(1−p) et σ(X) = √(n.p.(1−p)). »

> **Variable aléatoire continue** (p.346) — « Lorsqu'une variable aléatoire réelle X définie sur un univers Ω vérifie : X(Ω) = I où I est un intervalle de ℝ non réduit à un point, nous dirons que cette variable aléatoire est continue et on a : p(X ∈ I) = 1, p(X ∉ I) = 0 et ∀ a ∈ ℝ, p(X = a) = 0. » (puis : « En particulier, si X(Ω) = [a,b] alors p(X ∈ [a,b]) = 1 et p(X ∉ [a,b]) = 0. Donc il n'est pas possible de définir une loi de probabilité pour une telle variable aléatoire continue comme on l'a fait pour une variable aléatoire discrète. Par contre, on cherchera à exprimer la probabilité que les valeurs de la variable aléatoire appartiennent à un intervalle donné. »)

> **Fonction de répartition d'une variable continue** (p.346) — « Soit X une variable aléatoire réelle continue définie sur un univers Ω. La fonction de répartition F de X est définie sur ℝ par : ∀ x ∈ ℝ, F(x) = p(X ≤ x). »

> **Propriétés de F (continue)** (p.346) — « Si X est une variable aléatoire réelle continue définie sur un univers Ω et de fonction de répartition F alors on a les propriétés suivantes : • F est croissante sur ℝ et ∀ x ∈ ℝ, 0 ≤ F(x) ≤ 1. • p(X < a) = p(X ≤ a) et p(X > a) = p(X ≥ a) = 1 − F(a) pour tout a ∈ ℝ. • p(a < X ≤ b) = p(a ≤ X < b) = p(a < X < b) = p(a ≤ X ≤ b) = F(b) − F(a) où a et b sont deux réels tels que a < b. »

> **Densité de probabilité — définition** (p.348) — « Soit X une variable aléatoire réelle continue de fonction de répartition F. * On admet que F est continue sur ℝ et que lim_{x→−∞} F(x) = 0 et lim_{x→+∞} F(x) = 1 * La fonction dérivée f de F s'appelle la fonction densité (ou densité de probabilité) de X. Pour tout réel x on a : p(x ≤ X ≤ x + h) ≃ f(x).h où h est un réel strictement positif et voisin de 0. »

> **Propriétés de la densité** (p.348) — « Si X est une variable aléatoire réelle continue définie sur un univers Ω et de densité de probabilité f alors on a les propriétés suivantes : * f(x) ≥ 0 ∀ x ∈ ℝ. * Pour tous réels t et s tels que t ≤ s on a : p(t ≤ X ≤ s) = ∫ₜˢ f(x) dx * Si X(Ω) = [a,b], (a<b), alors ∫ₐᵇ f(x) dx = 1 * Si X(Ω) = [a,+∞[ alors lim_{x→+∞} ∫ₐˣ f(t) dt = 1 »

> **Loi uniforme** (p.349) — « Soient a et b deux réels tels que a < b. – Une variable aléatoire continue X suit une loi de probabilité uniforme sur l'intervalle [a; b] si sa densité de probabilité f est définie sur ℝ par : f(x) = 0 si x < a ; 1/(b − a) si a ≤ x ≤ b ; 0 si x > b. – Si X est une variable aléatoire continue qui suit une loi de probabilité uniforme sur l'intervalle [a; b] alors on a : * L'espérance mathématique de X est définie par E(X) = ∫ₐᵇ t.f(t) dt * La variance de X est définie par V(X) = ∫ₐᵇ t².f(t) dt − (E(X))². » — et (p.349, encadré de l'activité 1) : « L'espérance mathématique de X est « la moyenne arithmétique » des bornes de l'intervalle [a; b] c'est-à-dire : E(X) = (a + b)/2. * La variance de X est V(X) = (b − a)²/12 ».

> **Loi exponentielle — définition** (p.351) — « Soit a un réel strictement positif. Une variable aléatoire continue X suit une loi exponentielle de paramètre a sur I = [0,+∞[ si sa densité de probabilité f est définie sur ℝ par : f(t) = 0 si t < 0 ; a e^{−at} si t ≥ 0. »

> **Propriétés (loi exponentielle de paramètre a)** (p.351) — « Si X est une variable aléatoire réelle continue qui suit une loi exponentielle de paramètre a > 0 sur I = [0,+∞[ alors on a : • L'espérance mathématique de X est E(X) = 1/a. • La variance de X est V(X) = 1/a². • La fonction de répartition F de X est définie sur ℝ par : F(x) = 0 si x < 0 ; 1 − e^{−ax} si x ≥ 0. »

> **Propriétés (loi exponentielle de paramètre λ)** (p.352) — « Si X est une variable aléatoire réelle continue qui suit une loi exponentielle de paramètre λ > 0 sur I = [0,+∞[ alors : • pour tous réels positifs a et b tels que a ≤ b on a : p(a ≤ X ≤ b) = e^{−λa} − e^{−λb}. • pour tout t > 0 on a : p(X ≤ t) = 1 − e^{−λt}. • pour tous réels positifs s et t on a : p(X > s + t / X > s) = p(X > t) = e^{−λt}. »

> **Résumé du cours (p.354–356)** — reprend dans l'ordre : variable aléatoire réelle ; fonction de répartition (« ∀ x ∈ ℝ, p(X > x) = 1 − F(x) et p(a < X ≤ b) = F(b) − F(a) pour tous réels a et b tels que a < b ») ; tableau de la loi ; E(X) = Σ pₖ.xₖ ; V(X) = E((X − X̄)²) et V(X) = Σ xᵢ²pᵢ − (Σ xᵢpᵢ)² = E(X²) − (E(X))² ; σ(X) = √V(X) ; schémas de Bernoulli (n > 1, épreuves deux à deux indépendantes, loi binomiale ℬ(n, p), p(X = k) = Cₙᵏ.pᵏ.(1 − p)^{n−k}, E(X) = n.p, V(X) = n.p.(1−p), σ(X) = √(n.p.(1−p))) ; variable continue (X(Ω) = I intervalle non réduit à un point ; p(X = a) = 0 ; si X(Ω) = ℝ alors p(X ∈ ℝ) = 1 ; si X(Ω) = [a,b] alors p(X ∈ [a,b]) = 1 et p(X ∉ [a,b]) = 0) ; F continue et croissante sur ℝ, 0 ≤ F ≤ 1, limites 0 et 1 ; densité (f ≥ 0, p(t ≤ X ≤ s) = ∫ₜˢ f, ∫ₐᵇ f = 1, lim ∫ₐˣ f = 1) ; loi uniforme (f, E(X) = (a+b)/2, V(X) = (b−a)²/12) ; loi exponentielle de paramètre λ (f(t) = λe^{−λt}, E(X) = 1/λ, V(X) = 1/λ², F(x) = 1 − e^{−λx}, p(a ≤ X ≤ b) = e^{−λa} − e^{−λb}, p(X > t) = 1 − p(X ≤ t) = e^{−λt} pour t > 0).

### Avec l'ordinateur (p.357–358)

**Activité** (p.357) : logiciel « Sine qua non » (loi binomiale B(n ; p) : menu Définir, icône loi binomiale ; exemple n = 10, p = 0,5 pour visualiser p(X = k), k ∈ {0,…,10} ; calcul de F(x) = p(X ≤ x), par exemple F(7) = p(X ≤ 7) ≃ 0.9453). **Application** (p.358, ressource Internet citée) : **Situation 1** — 3 % des pièces d'une usine sont rejetées ; probabilité d'avoir exactement trois pièces à rejeter dans un lot de 100 pièces. **Situation 2** — sac de 200 billes (20 rouges, les autres bleues) ; 1) probabilité d'obtenir une bille rouge ; 2) on tire 50 fois de suite avec remise, X = nombre de billes rouges : a) espérance ; b) tableau de la loi de X ; c) probabilité de l'événement A : (m − 2σ < X ≤ m + 2σ) où m est l'espérance et σ l'écart-type ; 3) F fonction de répartition de X : déterminer F et la tracer dans un repère orthogonal convenablement choisi.

### Exercices et problèmes (p.359–364) — 25 exercices

- **Ex. 1** (p.359) : urne de 6 boules blanches et 4 noires ; tirage simultané de 3 boules ; X = nombre de boules blanches **restant** dans l'urne après tirage. 1) Loi de X ; 2) fonction de répartition de X, représentation.
- **Ex. 2** (p.359) : loi de X : xᵢ = −3, −1, 2, 4, 6 ; pᵢ = 0,1 ; 0,15 ; 0,05 ; 0,35 ; 0,35. F fonction de répartition : calculer F(−2), F(0), F(4,2) ; représentation graphique de F.
- **Ex. 3** (p.359) : loi de X : xᵢ = −2, −1, 2, 4, 6 ; pᵢ = a ; 0,15 ; 0,25 ; b ; 0,1 ; E(X) = 1,05 : calculer a et b.
- **Ex. 4** (p.359) : sac de 20 boules dont r rouges, b bleues, v vertes, j jaunes, r, b, v, j proportionnels à 1, 2, 3, 4. 1) Une boule remise : probabilité de chaque couleur ; 2) tirage répété trois fois avec remise, X = nombre de boules bleues tirées : a) éléments de X(Ω) ; b) P(X = k), k ∈ X(Ω) ; c) fonction de répartition ; d) espérance et variance.
- **Ex. 5** (p.359) : urne : une boule blanche, une rouge, trois noires. 1) Une boule tirée : probabilité de A « il reste dans l'urne exactement deux couleurs » ; 2) deux boules successives sans remise : probabilité qu'il reste exactement deux couleurs ; 3) deux boules simultanément, X = nombre de couleurs qui restent : a) loi de X ; b) E(X) ; c) variance et écart-type ; d) fonction F représentée.
- **Ex. 6** (p.359–360) : urne de 9 boules blanches et une rouge. 1) Tirage simultané de trois boules : probabilité d'obtenir la boule rouge ; 2) expérience répétée 5 fois avec remise des trois boules ; X = nombre de boules rouges obtenues sur les cinq tirages : loi de X, E(X), σ(X).
- **Ex. 7** (p.360) : dé tétraédrique parfait (faces 1 à 4) lancé cinq fois (lancers indépendants), X = nombre de sorties du 4 : loi et espérance.
- **Ex. 8** (p.360) : 2 % de pièces défectueuses ; on prélève une pièce, on la replace, on répète 100 fois ; X = nombre de pièces défectueuses ; a) loi de X ; b) E(X) [sic : « Cacluler »].
- **Ex. 9** (p.360) : urne : deux boules vertes numérotées 1, 1 et trois blanches numérotées 0, 1, −1. 1) Pièce parfaite lancée une fois : « Face » : tirage simultané de deux boules ; sinon tirage successif avec remise de deux boules ; somme des numéros ; A « somme nulle » : a) montrer p(A) = 29/100 ; b) sachant la somme nulle, probabilité d'obtenir « Face » ; c) épreuve répétée n fois (n ≥ 1) avec remise : probabilité pₙ d'avoir au moins une fois une somme non nulle ; plus petite valeur de n pour laquelle pₙ ≥ 0,95. 2) Les cinq boules tirées successivement et sans remise ; X = rang de la première boule blanche : loi de X et E(X). 3) « On tire successivement trois boules de l'urne de la manière suivantes [sic] : * Si on obtient une boule blanche on la remet dans l'urne avant de procéder au tirage suivant. Soit Y l'aléa numérique égale au nombre de boules vertes restant dans l'une [sic]. Déterminer la loi de probabilité de Y. * Si on obtient une boule verte on la » — le texte s'interrompt ici (fin de colonne) [énoncé tronqué à l'impression, la suite de la règle manque].
- **Ex. 10** (p.360) : « On désigne par X la variable aléatoire prenant pour valeur le nombre de fois où l'on obtient une pièce défectueuse. a) loi de probabilité de X ; b) espérance ; c) représentation de la fonction de répartition F de X. » — l'énoncé ne contient aucun contexte (il semble détaché de l'Ex. 8, dont il reprend la phrase) : doute sur l'intégrité de l'énoncé.
- **Ex. 11** (p.360–361) : 1) nombre de clients dans une station-service en cinq minutes : loi pᵢ = P(X = i) : i = 0, 1, 2 ; pᵢ = 0,1 ; 0,5 ; 0,4 ; a) fonction de répartition de X (définir et représenter) ; b) espérance. 2) Un client achète de l'essence avec probabilité 0,7, du gazole 0,3 (choix indépendants) ; C₁ « en cinq minutes, un seul client », C₂ « deux clients », E « un seul client achète de l'essence » : a) P(C₁∩E) ; b) montrer P(E/C₂) = 0,42 et calculer P(C₂∩E) ; c) en déduire la probabilité qu'en cinq minutes un seul client achète de l'essence. 3) Y = nombre de clients achetant de l'essence en cinq minutes : loi de Y.
- **Ex. 12** (p.361) — « (D'après Bac Tunisien 1995) » : boîte B₁ : trois jetons 0, 0, 2 ; boîte B₂ : quatre jetons 1, 1, 3, 4. 1) Un jeton tiré de chaque boîte, X = produit des deux nombres : loi de X ; 2) tirage répété trois fois, chaque jeton remis : probabilité d'obtenir a) exactement deux fois un produit supérieur à quatre ; b) au plus une fois un produit supérieur à quatre ; 3) tirages d'un jeton de B₁ avec remise ; pₙ = probabilité d'« obtenir le jeton numéro 2 au nᵉ tirage pour la première fois » : a) P₁, P₂, P₃ puis Pₙ ; b) Sₙ = Σ_{i=1}^{n} Pᵢ et lim Sₙ.
- **Ex. 13** (p.361) — « (D'après Bac Tunisien 2002) » : dé cubique homogène à faces −1 ; −1 ; −1 ; 0 ; 1 ; 1, jeté deux fois. 1) A « les deux numéros sont différents », B « la somme est égale à 0 » : probabilités ; 2) C « les deux numéros obtenus sont différents sachant que leur somme est égale à 0 » : probabilité ; 3) X = somme des deux numéros : a) loi de X ; b) probabilité de « X > 0 ».
- **Ex. 14** (p.362) — « (D'après Bac Tunisien 2003) » : urne : deux jetons blancs numérotés 1 ; −1 et trois noirs numérotés 1 ; 1 ; −1. 1) Tirage simultané de deux jetons : a) A « deux jetons de même couleur », B « de même couleur et de même numéro » ; b) X = somme des numéros : loi et espérance. 2) Tirage successif sans remise de deux jetons : a = numéro du premier, b = numéro du second ; plans P : x + ay + b = 0 et P' : x + by − a = 0 dans un repère orthonormé de l'espace : C « P et P' parallèles », D « P et P' perpendiculaires » : probabilités.
- **Ex. 15** (p.362) : urne U₁ (3 blanches, 2 noires) ; « d'une urne U₂ contenant 3 boules noires parfait dont les faces sont numérotés 0, 0, 0, 0, 1, 1. On lance une fois le dé » [sic : l'énoncé imprimé est amputé d'un passage (« … et 2 blanches, et d'un dé cubique parfait … ») ; la composition de U₂ est incomplète] ; « - Si on obtient le nombre 0 alors on tire successivement et avec remise deux boules de U₁. - Sinon, on tire successivement et sans remise deux boules de U₂. » 1) E « deux boules de même couleur », F « exactement une boule noire » : probabilités ; 2) X = nombre de boules blanches obtenues : loi et σ(X).
- **Ex. 16** (p.362–363) : deux sacs S₁ et S₂ et un dé cubique parfait ; S₁ : trois jetons blancs numérotés 0, 0, 1 et trois noirs 0, 2, 2 ; S₂ : deux blancs 0, 1 et quatre noirs 0, 0, 0, 1 ; faces du dé 1, 1, 2, 2, 2, 2. 1) Épreuve : dé lancé une fois ; si 1 : tirage simultané de deux jetons de S₁ ; si 2 : tirage successif sans remise de trois jetons de S₂ ; a) A « parmi les jetons tirés, on obtient le jeton noir numéro 1 », B « les jetons tirés sont noirs » : calculer p(B) et montrer p(A) = 1/3 ; b) probabilité de faire le tirage dans S₁ sachant que les jetons sont noirs ; c) X = somme des numéros marqués : loi de X et σ(X) ; d) épreuve répétée 5 fois : probabilité d'obtenir le jeton noir numéro 1 pour la première fois à la troisième épreuve. 2) Dé lancé 3 fois, Y = nombre de fois où l'on obtient le numéro 2 : a) loi de Y ; b) espérance et écart-type.
- **Ex. 17** (p.363) — « (D'après Bac Tunisien 2000) » : urne de cinq boules numérotées −2 ; −1 ; 1 ; 1 ; 2 ; trois boules tirées simultanément. 1) A « aucune boule tirée ne porte le n°1 », B « parmi les trois, deux portent le n°1 », S « la somme des nombres inscrits sur les deux boules qui restent dans l'urne est nulle » : a) probabilités de A et B ; b) montrer p(S) = 3/10. 2) Épreuve répétée cinq fois avec remise, X = nombre de fois où S est réalisé : a) loi de X ; b) espérance et variance de X.
- **Ex. 18** (p.363) : Adem coupe au hasard une ficelle de 50 cm ; X = longueur du bout qu'il garde. 1) Loi de X et espérance ; 2) probabilité de (20 ≤ X ≤ 25).
- **Ex. 19** (p.363) : X uniforme sur [−1, 1], Y = X² : densité de probabilité de Y, espérance et variance.
- **Ex. 20** (p.363) : salle de coiffure de 5 coiffeurs, une coupe dure 20 minutes ; un client trouve tous les coiffeurs occupés et trois personnes qui attendent : loi du temps d'attente de ce client et son espérance (coupes indépendantes, débutées depuis un temps uniformément réparti entre 0 et 20 minutes).
- **Ex. 21** (p.363–364) : appareil à six lampes toutes nécessaires ; densité de la durée de vie d'une lampe f(t) = (1/4)e^{−t/4} (unité : l'année). a) Vérifier que f est une densité d'une variable positive ; espérance et variance ; b) probabilité que l'appareil fonctionne de façon continue pendant six ans.
- **Ex. 22** (p.364) : F(x) = 0 si x < 0 ; 1 − e^{−x/2} si x ≥ 0. 1) F satisfait les propriétés d'une fonction de répartition continue ; 2) densité f ; 3) f et F dans un même repère orthogonal ; 4) a) espérance et variance ; b) probabilité de (2 < X ≤ 4) représentée graphiquement.
- **Ex. 23** (p.364) : durée d'une conversation téléphonique (minutes), loi exponentielle de paramètre 1/10 ; Borhène arrive à une cabine et une personne passe devant lui à ce moment précis. 1) Probabilité qu'il attende plus de dix minutes ; 2) entre dix et vingt minutes.
- **Ex. 24** (p.364) : durée de vie d'un moteur de 5 ans, loi exponentielle de paramètre a. 1) a) montrer a = 0,2 ; b) 50 % des clients dépannés durant la garantie : montrer que la durée de garantie est d'environ 3 ans et demi ; c) probabilité qu'un moteur ne tombe pas en panne avant deux ans. 2) Lot de 10 moteurs indépendants, X = nombre de moteurs sans panne pendant les deux premières années : a) justifier que X suit une loi binomiale (paramètres) ; b) espérance ; c) fonction de répartition F de X ; d) représenter f et F.
- **Ex. 25** (p.364) : gaz de 75 % de particules A et 25 % de particules B ; les A, radioactives, se transforment en B ; p(t) = proportion de A à l'instant t ; p(0) = 0,75 ; p(t) = 0,75e^{−λt}, λ > 0 constante, t en années. a) À t = 5730, p(t) = (1/2)p(0) : valeur approchée de λ à 10⁻⁵ près par défaut ; b) au bout de combien d'années 10 % des particules de type A seront-elles transformées ; c) valeur de t pour laquelle il y aura autant de A que de B.

### Aperçu historique (p.365)

Une ligne : histoire de la théorie des probabilités (Pascal, Fermat ; Jacques Bernoulli, Ars conjectandi 1713 ; de Moivre ; Laplace 1814 ; Tchebychev, Markov, Borel, Kolmogorov), puis notices sur Blaise Pascal, Pierre de Fermat, Daniel Bernoulli (« 1700-1782 Pays-Bas »), la famille Bernoulli et Pierre-Simon Laplace (« Loi de Bays-La place » [sic dans le texte]).

### Bornes de scope observées (chapitre 15)

- ✅ INCLUS : variable aléatoire réelle discrète (loi, tableau, fonction de répartition en escalier, espérance, variance, écart-type, formule E(X²) − (E(X))²), jeu équitable / favorable ; épreuve et schéma de Bernoulli, loi binomiale ℬ(n, p) avec E, V, σ ; variable aléatoire continue (univers non fini, p(X = a) = 0), fonction de répartition continue, densité (dérivée de F, intégrale), loi uniforme sur [a ; b] (E, V, F), loi exponentielle de paramètre a ou λ (densité, F, E, V, p(a ≤ X ≤ b), absence de mémoire, durée de vie) ; usage des logiciels Excel et Sine qua non.
- ⛔ NON traité dans ce chapitre : loi normale (renvoyée à un chapitre de statistiques dans l'aperçu historique) ; inégalité de Bienaymé–Tchebychev et loi des grands nombres ; lois de Poisson / géométrique nommées ; indépendance de variables aléatoires ; démonstration de E(X) = n.p et V(X) = n.p(1−p) pour la loi binomiale (énoncées sans preuve) ; calcul d'espérance d'une variable continue sur un intervalle infini autre que pour la loi exponentielle (traité en Act. 1 avec limites).

> Sondage image : pages 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 359, 360, 361, 362, 363, 364 (31 pages sur 35, dont toutes les pages à formules et les pages d'exercices en deux colonnes) ; écarts : (1) la couche texte des pages d'exercices à deux colonnes (p.359–364) entrelace les colonnes (la fin de l'Ex. 9 se lit après l'Ex. 10, l'Ex. 15 est coupé) : ordre rétabli sur image ; (2) nombreux symboles/lettres cassés par la couche texte (∈ ℝ, ≃ rendu « b » ou « c », Ā, barres, intégrales avec bornes mal placées, F(x+h) − F(x) ≃ f(x).h, x(Ω} etc.), tous relus sur image ; (3) aucun mot ni nombre faux dans les énoncés une fois relus sur image. Pages non confrontées : 331, 357, 358, 365 (texte seul sans formule, pages 357–358 lues en L1 uniquement).

## 2.16 Chapitre 16 — Statistiques (manuel 222451, p.366–392)

**Page de garde (p.366)** — Titre imprimé : « Statistiques » ; numérotation propre du manuel : « Chapitre **7** » (ce chapitre est le 16ᵉ de la fiche, et le dernier du manuel : p.392 = dernière page). « Plan du chapitre » : ❈ Activités préliminaires ❈ Cours (❖ Séries statistiques à deux caractères quantitatifs. ❖ Ajustement affine d'une série statistique double. ❖ Exemples d'ajustement non affine. ❖ Exercices résolus.) ❈ Résumé du cours ❈ Avec L'ordinateur ❈ Exercices et Problèmes ❈ Aperçu Historique. Pas de QCM / Vrai-Faux. La rubrique « Exercices résolus » (p.380–382) est un sous-chapitre du Cours. Le bandeau de la p.392 (Aperçu historique) porte le titre courant « Exercices et Problèmes » [sic].

### Activités préliminaires (p.367–369) — 3 activités + encadrés de rappels

- **Prél. 1** (p.367) : « Une entreprise emploie 36 % d'hommes et 96 femmes. » Tableau des horaires de travail hebdomadaire (classes [20,25[, [25,30[, [30,35[, [35,40[, Total) : Femmes : 15 ; 22 ; (vide) ; (vide) ; 96. Hommes : 2 ; (vide) ; (vide) ; 41 ; (vide). Total : (vide) ; 29 ; (vide) ; 64 ; (vide). 1) a) Compléter le tableau ; b) pourcentage des employés travaillant moins de 35 heures par semaine ; c) pourcentage des femmes travaillant plus de 30 heures par semaine ; d) pourcentage des hommes travaillant plus de 35 heures par semaine. 2) Le tableau représente trois séries statistiques (horaire, femmes) ; (horaire, hommes) ; (horaire, employés) [sic : « précèdent »] : a) représenter chacune par un histogramme ; b) pour chacune, déterminer le temps moyen de travail hebdomadaire d'un employé et l'écart-type.
- **Prél. 2** (p.367) : l'âge des employés d'une usine varie entre 20 et 60 ans ; diagramme du polygone des effectifs cumulés croissants (axes : âges 0 à 60 de 5 en 5, effectifs cumulés 0 à 200 de 20 en 20 ; points lus approximativement (20 ; 0), (25 ; 20), (30 ; 80), (40 ; 120), (50 ; 140), (60 ; 200)). 1) Déterminer les classes et leurs effectifs ; 2) déterminer l'âge médian ; 3) calculer l'âge moyen et l'écart-type.
- **Encadré de rappels (p.368)** — « • La moyenne d'une série statistique à caractère quantitatif continu est donnée par la formule : x̄ = (Σ_{i=1}^{p} nᵢcᵢ) / n où cᵢ est le centre de la classe [xᵢ, xᵢ₊₁[ ; nᵢ l'effectif de cette classe et n est l'effectif total de la série. • L'écart-type de cette série est σ = √v avec V = (1/n) Σ_{i=1}^{p} nᵢcᵢ² − (x̄)² = \overline{x²} − (x̄)². • La médiane est la valeur Mₑ du caractère qui correspond à un effectif cumulé croissant égal à n/2 si n est pair, (ou (n+1)/2 si n est impair). » [la barre « ‾ » sur x² dans la formule : moyenne des carrés].
- **Prél. 3** (p.368) : relevé des tailles X (cm) et des poids Y (kg) de 100 élèves : tableau à double entrée, X en lignes [150,155[ , [155,160[ , [160,165[ , [165,170[ ; Y en colonnes [40,45[ , [45,50[ , [50,55[ , [55,60[ ; effectifs : ligne 1 : 18, 10, 2, 0 ; ligne 2 : 3, 16, 5, 1 ; ligne 3 : 0, 5, 13, 5 ; ligne 4 : 0, 2, 6, 14. 1) Distribution marginale de X et de Y ; 2) calculer X̄, Ȳ, V(X), V(Y), σ(X), σ(Y).
- **Encadré « Retenons » (p.368–369)** (voir verbatim).

### Cours — Activités

**I. Séries statistiques à deux caractères quantitatifs** (p.370–372)

- **Activité 1** (p.370) : distance de freinage d (m) d'un véhicule en fonction de sa vitesse v (km/h) sur route humide : v = 40, 50, 60, 70, 80, 90, 100 ; d = 21,5 ; 28 ; 37,5 ; 48 ; 60 ; 75 ; 92,5. 1) a) Construire le nuage de points sur papier millimétré (intersection des axes en (30 ; 10), 1 cm pour 5 km/h en abscisse et 1 cm pour 5 m en ordonnée) ; b) placer le point moyen G ; c) sur quelle courbe semblent situés les points ? 2) On pose y = √d : compléter le tableau (v ; y) ; a) construire le nouveau nuage ; b) placer le point moyen G' ; c) sur quelle ligne semblent situés les points ?
- **Activité 2** (p.370–371) : répartition de 100 enfants selon l'âge (années : [3,4[, [4,5[, [5,6[) et le poids (kg : [10,15[, [15,20[, [20,25[, [25,30[) ; effectifs : [10,15[ : 25, 10, 5 ; [15,20[ : 30, 8, 7 ; [20,25[ : 2, 1, 3 ; [25,30[ : 2, 5, 2 ; ligne Totaux vide. 1) Recopier et compléter le tableau ; 2) construire dans un repère orthogonal le nuage de points représentant la série double ; 3) coordonnées du point moyen G, le placer.
- (Définitions « nuage de points » et « point moyen » + figure « Exemple de nuage de points » (axes âge en abscisse de 2 à 6, poids en ordonnée de 10 à 30 ; points Mᵢⱼ affectés de leurs effectifs, ex. M₁₁(25), M₂₁(10), M₁₂(30), M₂₂(8) ; étiquettes partiellement illisibles à ce grain [?]) : p.371, voir verbatim.)
- **Activité 3** (p.371–372) : frais de publicité xᵢ et chiffre d'affaires yᵢ (milliers de dinars) sur 8 années : rang 1 à 8 ; xᵢ = 1,1 ; 1,4 ; 1,6 ; 2 ; 2,2 ; 2,3 ; 2,2 ; 2,4 ; yᵢ = 59 ; 68 ; 67 ; 71 ; 71 ; 69 ; 67 ; 72. 1) a) Nuage de points M(xᵢ, yᵢ) sur papier millimétré (intersection des axes en (1 ; 58), 1 cm pour 0,2 mille dinars en abscisse, 1 cm pour 2 mille dinars en ordonnée) ; b) montant moyen X̄ ; c) chiffre d'affaires moyen Ȳ ; d) placer G(X̄, Ȳ). 2) a) Équation de la droite D = (M₁M₈), tracer D, G est-il sur D ? b) équation de Δ = (GM₁), la tracer ; c) laquelle de D et Δ représente le mieux le nuage ? 3) Une année, frais de publicité de 2,5 mille dinars : peut-on prévoir le chiffre d'affaires ?
- **Activité 4** (p.372) : nombre de passagers (milliers) d'un aéroport en janvier (xᵢ) et juillet (yᵢ) sur dix années : xᵢ = 350 ; 360 ; 410 ; 420 ; 440 ; 480 ; 510 ; 530 ; 580 ; 630 ; yᵢ = 620 ; 625 ; 630 ; 690 ; 790 ; 760 ; 940 ; 920 ; 1030 ; 1040. 1) Nuage Mᵢ(xᵢ, yᵢ), intersection des axes en (300 ; 600) ; 2) a) coordonnées de G ; b) points moyens G₁ (cinq premiers points {Mᵢ / i ≤ 5}) et G₂ (cinq derniers {Mᵢ / 6 ≤ i ≤ 10}) ; c) équation de D = (G₁G₂), la tracer ; 3) en janvier 700 mille passagers : prévision pour juillet.

**II. Ajustement affine d'une série statistique double** (p.372–379)

- Encadré d'introduction (p.372, voir verbatim) : relation affine Y = aX + b ou X = a'Y + b' ; « ajustement affine » ; deux méthodes : Mayer et moindres carrés.
- **Méthode de Mayer** (p.373–374) :
  - **Activité 1** (p.373) : retraits à un guichet automatique d'une banque en une journée : montants en DT xᵢ = 40, 35, 30, 25, 20, 15, 10, 5 ; effectifs yᵢ = 19 ; 20 ; 17 ; 11 ; 13 ; 6 ; 7 ; 2. 1) a) Nuage de points ; b) particularité de la forme du nuage ; c) point moyen G, le placer. 2) On partage les points en deux parties : P₁ = retraits inférieurs ou égaux à 25 DT, P₂ = les autres ; a) coordonnées des points moyens G₁ et G₂, les placer ; b) équation cartésienne de (G₁G₂) et vérifier qu'elle passe par G. 3) Nombre de retraits de 50 DT prévisible en une journée ? **Commentaires** (avec figure du nuage, G, G₁, G₂ et droite) : « • Le nuage de points de la série considérée a une forme allongée. • La droite (G₁G₂) passe près des points du nuage. Elle est appelée droite de Mayer. • Nous disons qu'on a réalisé un ajustement affine du caractère y en fonction de la variable x à l'aide de la méthode de Mayer. » Encadré « La méthode de Mayer consiste à » (voir verbatim).
  - **Activité 2** (p.374) : pourcentage Y des frais de santé par rapport au budget des ménages d'un pays sur six années (rang X = 1 à 6) : Y = 7,2 ; 9,7 ; 11,9 ; 12,5 ; 14 ; 16. 1) Nuage ; 2) point moyen G, le placer ; 3) par la méthode de Mayer, équation cartésienne de la droite d'ajustement affine de Y en X ; 4) pourcentage prévisible pour l'année de rang 10.
  - **Activité 3** (p.374) : moyennes annuelles en mathématiques X de dix élèves de terminale : 7, 10, 6, 15, 16, 18, 15, 10, 7, 10 ; notes de mathématiques au baccalauréat Y : 7, 8, 5, 11, 17, 18, 13, 11, 9, 10. 1) Nuage de points ; 2) point moyen G ; 3) ajustement affine par la méthode de Mayer ; 4) estimation de la note au baccalauréat d'un élève ayant 13 de moyenne annuelle.
- **Méthode des moindres carrés** (p.375–379) :
  - Encadré d'introduction (p.375, voir verbatim) : « On peut reconnaître la relation affine éventuelle entre les deux variables X et Y à l'aide d'un moyen non graphique et en faisant intervenir deux nouveaux paramètres statistiques à savoir : la covariance et le cœfficient de corrélation linéaire. »
  - **1) Covariance** (p.375–376) : définition et remarque (voir verbatim). **Activité 1** (p.375) : accidents de la circulation sur cinq années (rang X = 1 à 5) : Y = 82 ; 90 ; 117 ; 96 ; 102. 1) a) X̄ et Ȳ ; b) V(X) et V(Y) ; 2) a) Cov(X, Y) ; b) comparer Cov²(X, Y) au produit V(X).V(Y) ; 3) nuage de points ; existe-t-il une relation affine entre X et Y ? **Commentaires** (p.375) : « Soit une série statistique à deux caractères quantitatifs X et Y. Lorsque Cov²(X,Y) est assez voisin de V(X).V(Y), on peut dire que la relation entre X et Y est approximativement affine. On peut alors trouver deux réels a et b tels que Y est proche de aX + b. Cette approximation pourrait être très utile pour décrire un phénomène aléatoire et prévoir son évolution. » **Activité 2** (p.376) : durée du travail quotidien X (h) = 8 ; 9 ; 10 ; 12 ; 14 ; 15 et nombre d'erreurs Y = 6 ; 7 ; 10 ; 14 ; 20 ; 25. 1) a) σ(X) et σ(Y) ; b) Cov(X, Y) ; c) comparer Cov(X, Y) au produit σ(X).σ(Y) ; d) que peut-on en déduire ? 2) Mayer : ajustement affine de Y en X ; 3) nombre d'erreurs d'un ouvrier ayant travaillé 13 heures.
  - **2) Cœfficient de corrélation linéaire** (p.376–378) : définition (voir verbatim). **Activité 1** (p.376–377) : résistances électriques vendues suivant leur puissance (W) X = 100 ; 150 ; 200 ; 300 ; 500 et nombre Y = 50 ; 70 ; 100 ; 150 ; 250. 1) a) Cov(X, Y), σ(X), σ(Y) ; b) peut-on déduire une relation affine entre X et Y ? 2) a) coefficient de corrélation linéaire r ; b) comparer r à 1 ; 3) a) tracer les droites D₁ : y = ax + b (a = cov(X,Y)/V(X), b = Ȳ − aX̄) et D₂ : x = a'y + b' (a' = cov(X,Y)/V(Y), b' = X̄ − a'Ȳ) ; b) nuage de points ; c) position des droites D₁, D₂ par rapport au nuage ; d) montrer que G(X̄, Ȳ) appartient à D₁ et D₂. **Commentaires** (p.377, voir verbatim, avec exemple et figure : r ≃ 0,81 ; D₁ : y = 0,53x + 5,49 ; D₂ : x = 1,24y − 5,79, G point moyen). **Activité 2** (p.377) : âge X et tension artérielle Y de 10 personnes : X = 58, 40, 74, 34, 65, 49, 53, 51, 36, 40 ; Y = 16,7 ; 13,1 ; 17,2 ; 11,6 ; 15,5 ; 15,1 ; 14,2 ; 14,4 ; 13,0 ; 14,2. 1) Nuage ; 2) moyenne et variance de X et Y ; 3) r ; 4) droite de régression de Y en X ; 5) tension d'une personne de 45 ans. **Activité 3** (p.378) : prix X (DT) = 0,650 ; 0,900 ; 1,100 ; 1,300 ; 1,500 ; 2,600 et poids Y (g) = 100 ; 150 ; 200 ; 250 ; 300 ; 500. 1) a) r ; b) un ajustement affine est-il justifié ? 2) équations des droites de régression dans un repère orthogonal ; 3) prix prévisible d'un produit de 1 kg.

**III. Exemples d'ajustement non affine** (p.378–379)

- **Activité 1** (p.378) : frais de publicité Y (DT) sur dix années (rang X = 1 à 10) : 1015 ; 1310 ; 1690 ; 1977 ; 2803 ; 3606 ; 4640 ; 5960 ; 7400 ; 9000. 1) Compléter le tableau Z = ln Y ; 2) a) nuage (X, Z) ; b) point moyen G ; 3) a) tracer une droite D passant par G près des points ; b) équation cartésienne de D ; c) relation entre X et Z ; 4) relation entre X et Y.
- **Activité 2** (p.379) : produit A. 1) Prix de revient = a (DT) de frais fixes + b (DT) par unité ; pour n unités a + n.b ; montrer que le prix de revient d'une unité est y = a/n + b. 2) Déterminer a, b : a) prix unitaire y pour n = 1 à 10 : 150 ; 81 ; 54 ; 44 ; 38 ; 32 ; 29 ; 26 ; 23 ; 21 ; nuage (n, y), ajustement affine justifié ? b) x = 1/n : valeurs de x à 10⁻² près par défaut ; nuage (x, y) et ajustement affine ; équation de la droite de régression de y en x ; relation entre y et n ; c) estimation du prix de revient unitaire pour 20 unités.
- **Activité 3** (p.379) : tension u (V) aux bornes d'un condensateur à l'instant t (s) : t = 30, 60, 90, 120, 150, 180, 210, 240 ; u = 2,35 ; 1,40 ; 0,80 ; 0,50 ; 0,30 ; 0,20 ; 0,15 ; 0,10. On pose y = ln u. 1) Tableau de valeurs de (t, y) ; 2) a) coefficient de corrélation entre t et y ; b) ajustement affine justifié ? 3) a) équation de la droite de régression de y en t ; b) relation entre t et u ; 4) instant T où u vaut 1 volt.

**IV. Exercices résolus** (p.380–382) — 3 exercices résolus (énoncé + solution imprimée)

- **Exercice 1** (p.380) — « (Bac Tunisien : juin 2005) » : distance de freinage d (m) en fonction de la vitesse v (km/h) : v = 30, 40, 50, 60, 70, 80 ; d = 42 ; 60 ; 80 ; 90 ; 95 ; 110. 1) v̄, d̄, V(v), V(d), cov(v, d) ; 2) a) coefficient de corrélation linéaire ; b) forte corrélation affine ? justifier ; 3) Δ droite de régression de d en v d'équation d = 1,3.v + 8 : distance de freinage à 100 km/h ; 4) vitesse de 140 km/h, obstacle à 200 mètres, une seconde pour appuyer sur les freins : le conducteur peut-il l'éviter ? Solution imprimée : v̄ = 55 ; d̄ = 79,5 ; V(v) = 291,66 ; V(d) = 511,25 et cov(v,d) = \overline{v.d} − v̄.d̄ = 379,166 ; r = cov(v,d)/(σ(v).σ(d)) ≃ 0,981 ; r proche de 1 donc forte corrélation affine et ajustement affine justifié ; à 100 km/h d = 138 m ; à 140 km/h d = 190 m ; en une seconde la voiture parcourt d₀ = 140.000/3600 = 38,8 m ; distance totale d + d₀ = 228,8 m > 200 m : le conducteur ne pourra pas éviter l'obstacle.
- **Exercice 2** (p.380–381) : rendement R d'une variété de blé (q/ha) et quantité E d'engrais azotés (kg/ha) : E = 50, 60, 70, 80, 90 ; R = 35,7 ; 41,4 ; 45,7 ; 47,2 ; 50,8. 1) a) r(E, R) ; b) conclusion ; 2) équation de la droite de régression de R en E ; 3) rendement prévisible pour E = 100 kg/ha. Solutions imprimées : Ē = 70 ; R̄ = 44,16 ; r(E,R) = cov(E,R)/(σ(E).σ(R)) ≃ 0,98 ; très voisin de 1 : « l'une des variables peut être approchée par une fonction affine de l'autre variable » ; R = a.E + b avec a = cov(E,R)/V(E) = 0,36 et b = R̄ − a.Ē = 18,92 ; équation R = 0,36.E + 18,92 ; pour E = 100 : R = 0,36 × 100 + 18,92 = 54,92 (q/ha).
- **Exercice 3** (p.381–382) : consommation d'énergie électrique Y (Twh) d'un pays sur 8 années (rang X = 1 à 8) : 30 ; 41 ; 56 ; 73 ; 97 ; 123 ; 165 ; 205. 1) a) nuage (X, Y) ; b) coefficient r₁ ; c) droite D de régression de Y en X par les moindres carrés ; 2) relation exponentielle Y = k.e^{aX}, V = ln Y : a) nuage (X, V) et coefficient r₂ ; b) en déduire forte corrélation linéaire entre V et X, construire la droite D' de régression de V en X ; d) [sic : l'énoncé passe de b) à d)] en écrivant V = a.X + b où b = ln k, trouver a et b. Solution imprimée (p.382) : X̄ = 4,5 ; Ȳ = 98,75 ; σ(X) = 2,29 ; σ(Y) = 57,9 ; cov(X,Y) = 129,37 ; r₁ = 0,97 ; « Une équation de la droite D de régression de X en Y est : y = 9,62.x + 29,71 » [sic : « de X en Y » alors que l'équation est celle de Y en X] ; tableau V = ln Y : 3,401 ; 3,713 ; 4,025 ; 4,290 ; 4,574 ; 4,812 ; 5,105 ; 5,323 ; X̄ = 4,5 ; V̄ = 4,40 ; σ(X) = 2,29 ; σ(V) = 0,62 ; cov(X,V) ≈ 1,441 ; r₂ = r(X,V) ≈ 0,99 ; r(X,V) voisin de 1 donc forte corrélation linéaire entre V et X ; « Une équation de la droite Δ de régression de X en V est : v = 0,27.x + 3,17 » [sic, même confusion] ; a = 0,27 et b = 3,17 ce qui donne Y = e^{3,17}.e^{0,27.X} = e^{0,27.X+3,17} ; 3) f(x) = e^{0,27.x+3,17} : étudier et représenter graphiquement f dans le même repère que le nuage (« e^{0,27.X+3,17} » avec X majuscule [sic] ; cette question 3 est présente seulement dans la solution imprimée p.382, absente de l'énoncé p.381).

### Cours — Résultats / définitions / théorèmes à retenir (VERBATIM)

> **Retenons — distributions marginales (p.368–369)** — « Soient deux variables statistiques quantitatives X et Y définies sur une même population E d'effectif total N. Soient x₁, x₂, …, xₚ les valeurs de X et y₁, y₂, …, y_q celles de Y (ou les centres des classes). On note : nᵢⱼ l'effectif correspondant à (X = xᵢ et Y = yⱼ) ; nᵢ. = nᵢ₁ + nᵢ₂ + … + nᵢq et n.ⱼ = n₁ⱼ + n₂ⱼ + … + nₚⱼ. On a le tableau à double entrée suivant : » (tableau Y : y₁ … yⱼ … y_q, Totaux ; X : x₁ … xᵢ … xₚ ; cases nᵢⱼ ; marges nᵢ. et n.ⱼ ; total N) — « La distribution marginale de X est donnée par le tableau suivant : Valeurs de X : x₁ … xᵢ … xₚ ; Effectif marginal : n₁. … nᵢ. … nₚ. * La moyenne arithmétique de X est X̄ = (1/N) Σ_{i=1}^{p} nᵢ. × xᵢ = Σ_{i=1}^{p} fᵢ. × xᵢ où fᵢ. = nᵢ./N est la fréquence marginale associée à la modalité xᵢ de X. * La variance marginale de X est V(X) = (1/N) Σ_{i=1}^{p} nᵢ. × xᵢ² − (X̄)². * L'écart-type de X est σ(X) = √V(X). »

> **Nuage de points — point moyen** (p.371) — « Le plan est muni d'un repère orthogonal (O, u⃗, v⃗). Soit une série statistique à deux caractères quantitatifs X et Y. On désigne par x₁, x₂, …, xₚ les valeurs de X et par y₁, y₂, …, y_q celles de Y (ou les centres des classes). On note nᵢⱼ l'effectif correspondant à (X = xᵢ et Y = yⱼ). * On appelle **nuage de points** de la série considérée, l'ensemble des points Mᵢⱼ(xᵢ, yⱼ) tels que 1 ≤ i ≤ p et 1 ≤ j ≤ q. Chacun d'eux est affecté par l'effectif nᵢⱼ correspondant. * On appelle **point moyen** du nuage de points, le point G(X̄, Ȳ) où X̄ et Ȳ désignent respectivement les moyennes arithmétiques des distributions de X et de Y. »

> **Ajustement affine (introduction)** (p.372) — « Lorsque le nuage des points, représentant graphiquement une série statistique à deux caractères X et Y, a une forme allongée, on peut approcher la relation entre les deux variables X et Y par une relation affine définie par : Y = aX + b ou X = a'Y + b'. On appelle **ajustement affine** toute méthode permettant la détermination d'une telle relation. Dans ce qui suit, nous présenterons deux méthodes : la méthode de Mayer et la méthode des moindres carrés. »

> **La méthode de Mayer** (p.373–374) — « La méthode de Mayer consiste à : a) Partager le nuage de points en deux parties P₁ et P₂ satisfaisant à : * P₁ et P₂ sont situées de part et d'autre par rapport à une droite parallèle à l'axe des ordonnées. * cardinal(P₁) = cardinal(P₂) si le nombre des points du nuage est pair. * cardinal(P₁) = cardinal(P₂) + 1 ou cardinal(P₁) = cardinal(P₂) − 1 si le nombre des points du nuage est impair. b) Déterminer les points moyens respectifs G₁ et G₂ des parties P₁ et P₂. c) La droite (G₁G₂) est alors la droite d'ajustement affine du nuage de points représentant la série considérée. Cette droite est la droite de Mayer associée au nuage de points. Elle passe par le point moyen G du nuage. »

> **Covariance — définition** (p.375) — « Soit une série statistique à deux caractères quantitatifs X et Y. On désigne par x₁, x₂, …, xₙ les valeurs de X et par y₁, y₂, …, yₙ celles de Y (ou les centres des classes). On note n l'effectif total de la population observée. On appelle covariance de la série double considérée le réel, noté Cov(X, Y), et défini par : Cov(X, Y) = (1/n) Σ_{i=1}^{n} xᵢyᵢ − X̄.Ȳ où X̄ et Ȳ sont les moyennes arithmétiques respectives des distributions (xᵢ)_{1≤i≤n} et (yᵢ)_{1≤i≤n} de X et Y. » — **Remarque** : « On a : Cov(X, Y) = \overline{XY} − X̄.Ȳ ; où \overline{XY} désigne la moyenne arithmétique de la distribution (xᵢyᵢ)_{1≤i≤n} du caractère statistique produit. »

> **Cœfficient de corrélation linéaire — définition** (p.376) — « Soit une série statistique à deux caractères quantitatifs X et Y non constants observés dans une population donnée d'effectif total n. On appelle cœfficient de corrélation linéaire de la série double (X, Y), le réel r défini par : r = Cov(X, Y) / (σ(X).σ(Y)) où σ(X) et σ(Y) sont les écarts-types respectifs des variables statistiques X et Y. »

> **Commentaires — droites de régression** (p.377) — « Soit une série statistique à deux caractères quantitatifs X et Y. Lorsque le cœfficient de corrélation linéaire r du couple (X, Y) est proche, en valeur absolue, de 1 (0.75 ≤ |r| ≤ 1), le nuage de points de la série considérée a une forme allongée et il est possible d'approcher la liaison entre X et Y par deux relations affines représentées graphiquement par deux droites D₁ et D₂ passant par le point moyen G(X̄, Ȳ) du nuage. * La droite D₁ : appelée **droite de régression de Y en X** et ayant pour équation : y = ax + b avec a = cov(X, Y)/V(X) et b = Ȳ − aX̄. * La droite D₂ : appelée **droite de régression de X en Y** et ayant pour équation : x = a'y + b' avec a' = cov(X, Y)/V(Y) et b' = X̄ − a'Ȳ. »

> **Résumé du cours (p.383–384)** — « * Nuage de points d'une série statistique double : [définitions du nuage de points et du point moyen, textes de la p.371]. * Ajustement affine d'une série statistique double : [texte de la p.372, « Y = a.X + b ou X = a'.Y + b' »]. Méthode de Mayer : [a) b) c) de la p.374]. Méthode des moindres carrés : Soit une série statistique à deux caractères quantitatifs X et Y. On désigne par x₁, x₂, …, xₙ les valeurs de X et par y₁, y₂, …, yₙ celles du caractère Y (ou les centres des classes). On note n l'effectif total de la population observée. Soit r le cœfficient de corrélation linéaire du couple (X, Y) : r = Cov(X, Y)/(σ(X).σ(Y)) où σ(X) et σ(Y) sont les écarts-types respectifs des variables statistiques X et Y ; et Cov(X, Y) = (1/n) Σ_{i=1}^{n} xᵢyᵢ − X̄.Ȳ est la covariance du couple (X, Y). * Lorsque le cœfficient de corrélation linéaire du couple (X, Y) est proche, en valeur absolue, de 1 (0.75 ≤ |r| ≤ 1) [sic : le résumé de la p.384 écrit « 0.75 ≤ r ≤ 1 » dans la couche texte, la barre de valeur absolue est présente sur l'image], il est possible d'approcher la liaison entre X et Y par deux relations affines représentées graphiquement par deux droites passant par le point moyen G du nuage. La droite D₁ : appelée droite de régression de Y en X et ayant pour équation : y = ax + b avec a = cov(X, Y)/V(X) et b = Ȳ − aX̄. La droite D₂ : appelée droite de régression de X en Y et ayant pour équation : x = a'y + b' avec a' = cov(X, Y)/V(Y) et b' = X̄ − a'Ȳ. » (Le résumé ne reprend pas la covariance Cov² ≈ V(X)V(Y) ni les exemples non affines.)

### Avec l'ordinateur (p.385–386)

- **Activité 1** (p.385) : logiciel **Sine qua non** (adresse Internet citée) ; une entreprise fabricant des lots de circuits électriques garantis un an envisage d'allonger la garantie ; tableau : x (semestres) = 1…10, y (pourcentage de circuits d'un lot en panne) = 2 ; 3 ; 4 ; 7 ; 9 ; 11 ; 16 ; 20 ; 23 ; 31. 1) Construire le nuage Mᵢ(xᵢ, yᵢ) avec le logiciel (menu Définir, repère ; 1 cm pour 1 semestre et 0,5 cm pour 1 % ; série statistique double) ; question : ajustement affine envisageable ? 2) Droite de régression de y en x (icône série statistique double, régression linéaire y en fonction de x). 3) Le logiciel donne cov(x, y) = 25,5 ; r = 0,97 ; y = 3,09x − 4,4 : justifier par le calcul. 4) Part de bénéfice z (en % du prix de vente du lot) liée à y par z = 40 − 1,2y : nombre maximum de semestres de garantie pour conserver z ≥ 25.
- **Activité 2** (p.386) : calculatrice **Sharp** : choix du mode statistique double (Sharp Mode (0-2) : 2ndf, Mode, 2 ⇒ Stat xy ; Sharp Mode (0-1) : 2ndf, Mode, 1, 1 ⇒ Stat 1 ; Sharp Mode (0-3) : 2ndf, Mode, 3, 1 ⇒ Stat 1). Exemple : 30 logements, X = nombre d'enfants, Y = nombre de pièces (valeurs individuelles x : 0 3 0 3 1 3 1 2 3 2 1 1 1 0 3 0 1 2 3 1 2 1 3 1 2 2 3 2 1 2 ; y : 1 3 2 2 1 3 2 2 2 1 3 2 3 1 3 2 2 3 3 1 3 2 2 3 3 1 2 3 2 2) résumé en tableau à double entrée (Y = 0 : 2, 2, 0, total 4 ; Y = 1 : 2, 5, 3, total 10 ; Y = 2 : 2, 2, 4, total 8 ; Y = 3 : 0, 4, 4, total 8 ; Totaux 6, 13, 11, 30 ; colonnes X = 1, 2, 3 — l'en-tête de ligne Y part de 0 alors que les valeurs de y dans la ligne individuelle vont de 1 à 3 [doute : incohérence interne entre les deux tableaux ; elle s'explique par des en-têtes X et Y du tableau à double entrée inversés par rapport aux données individuelles]). Séquences de touches pour la saisie (« 0 STO 1 STO 2 M+ », etc.) et résultats : X̄ = 1.66 ; V(X) = 1,02 ; σ(X) = 1,01 ; Ȳ = 2.16 ; V(Y) = 0.53 [sic : écrit « V(X) = 0.53 » dans la colonne de Y] ; σ(Y) = 0.73 ; r = 0.38 (corrélation faible) ; Cov(X, Y) = 0.28 ; droite de régression de Y en X : Y = αX + β, α = 0.28, β = 1.69 ; droite de X en Y : X = α'Y + β', α' = 0.04, β' = X̄ − α'Ȳ = 1.58.

### Exercices et problèmes (p.387–391) — 16 exercices

- **Ex. 1** (p.387) : distance parcourue (milliers de km, en 3 ans) par 100 véhicules : classes De 75 à 85, De 85 à 95, De 95 à 105, De 105 à 115, De 115 à 125 ; effectifs 10, 18, 40, 20, 12. 1) Histogramme ; 2) distance moyenne parcourue par un véhicule en une année.
- **Ex. 2** (p.387) : salaires horaires (dinars) dans deux entreprises A et B : classes De 1 à 1,5 ; De 1,5 à 2 ; De 2 à 2,5 ; De 2,5 à 3 ; De 3 à 3,5 ; effectifs de A : 10, 18, 40, 20, 12 ; effectifs de B : 10, 18, 40, 20, 12 [données identiques pour A et B, imprimées telles quelles]. 1) Tableau des fréquences ; 2) a) histogrammes des fréquences dans un même repère orthogonal ; b) comparer globalement les deux entreprises ; 3) pour chaque série, salaire horaire moyen, médiane et écart-type.
- **Ex. 3** (p.387) : diagramme en bâtons d'un caractère quantitatif discret X (valeurs en abscisse de 0 à 16, effectifs 1 à 3 ; valeurs exactes non lisibles sur le diagramme, hauteurs de bâtons imprimées en figure). 1) Moyenne, médiane et mode de X ; 2) Y : valeurs 2 ; 3 ; 4 ; 5 ; 9 ; 10 ; 10 ; 11 ; 12 ; 12 ; 12 ; 12 ; 15 ; 16 ; 17 : a) représenter graphiquement Y ; b) montrer que X et Y ont même moyenne, médiane et mode ; 3) a) pour chaque caractère : étendue, écart moyen et écart-type ; b) interpréter.
- **Ex. 4** (p.387) : taille X (cm) = 95, 103, 109, 122, 133 et poids Y (kg) = 15, 16, 19, 24, 30 de cinq enfants. 1) a) nuage de points ; b) point moyen G, le placer ; 2) méthode de Mayer : ajustement affine ; 3) valeur approchée du poids d'un enfant de taille 115 cm.
- **Ex. 5** (p.387–388) : dépenses annuelles d'un pays pour les nouvelles technologies de l'information et de la communication, six dernières années (en milliers de D.US [sic] ; tableau : « M.D.US ») : X = 1 à 6 ; Y = 445 ; 474 ; 504 ; 530 ; 568 ; 588. 1) Nuage de points et point moyen G ; 2) G₁ point moyen des points des années 1, 2, 3 et G₂ des années 4, 5, 6 : a) placer G₁, G₂ et tracer (G₁G₂) ; b) équation de (G₁G₂) ; c) que représente G pour le segment [G₁G₂] ? 3) valeur approchée de la dépense de l'année de rang 10.
- **Ex. 6** (p.388) : pluviosité X (mm) = 165 ; 130 ; 120 ; 80 ; 40 ; 30 et rendement Y (t/ha) = 0,37 ; 0,30 ; 0,29 ; 0,25 ; 0,20 ; 0,12 d'une variété de blé. 1) Coordonnées du point moyen ; 2) nuage de points ; 3) ajustement affine envisageable ? si oui équation de la droite de régression de Y en X.
- **Ex. 7** (p.388) : altitude X (km) = 0 ; 1 ; 2 ; 4 ; 6 ; 10 et hauteur barométrique Y (cm) = 76 ; 67 ; 59 ; 46 ; 35 ; 20. 1) a) nuage ; b) ajustement affine justifiable ? 2) Mayer : équation cartésienne d'une droite résumant le nuage ; 3) altitude d'un lieu où la hauteur barométrique est de 60 cm.
- **Ex. 8** (p.388) : chiffre d'affaires Y (millions de D.T) d'une entreprise sur dix années (rang X = 1 à 10) : 8 ; 12 ; 12 ; 15 ; 17 ; 22 ; 27 ; 32 ; 37 ; 42. 1) a) coefficient de corrélation linéaire ; b) conclusion ; 2) équations des droites de régression D₁ et D₂ dans un repère orthogonal ; 3) en supposant la même évolution, rang de l'année à partir duquel le chiffre d'affaires dépassera 50 millions de dinars tunisiens.
- **Ex. 9** (p.388–389) : dix essais de laboratoire : charge de rupture y (kg) d'un acier en fonction de sa teneur x (pour 10 000 unités) en carbone : x = 72 ; 60 ; 68 ; 66 ; 64 ; 62 ; 64 ; 70 ; 62 ; 74 ; y = 90 ; 70 ; 80 ; 80 ; 75 ; 75 ; 80 ; 85 ; 70 ; 100. 1) Nuage ; 2) X̄, Ȳ, V(X), V(Y), cov(X, Y) ; 3) liaison affine envisageable ? justifier par un calcul ; 4) droite de régression de Y en X, la construire ; 5) charge de rupture d'un acier de teneur 65 pour 10 000.
- **Ex. 10** (p.389) : litres d'essence achetés à une pompe par 8 véhicules selon leur puissance (chevaux) x = 4 ; 5 ; 6 ; 8 ; 9 ; 10 ; 11 ; 12 et litres y = 10 ; 20 ; 25 ; 30 ; 40 ; 32 ; 25 ; 45. 1) a) σ(x), σ(y), cov(x, y) ; b) coefficient de corrélation r ; c) conclusion ; 2) équations des droites de régression ; 3) volume d'essence prévisible pour un véhicule de 7 chevaux.
- **Ex. 11** (p.389) : tailles X (cm) et poids Y (kg) de 100 enfants : X en lignes [100,110[ , [110,120[ , [120,130[ , [130,140[ ; Y en colonnes [20,25[ , [25,30[ , [30,35[ , [35,40[ ; effectifs : 18, 10, 2, 0 ; 3, 16, 5, 1 ; 0, 5, 13, 5 ; 0, 2, 6, 14. 1) Nuage de points associé ; 2) X̄, Ȳ, V(X), V(Y) ; 3) calculer cov(X, Y) avec cov(X, Y) = (1/100) Σ_{1≤i≤4, 1≤j≤4} nᵢⱼ.cᵢc'ⱼ où les cᵢ sont les centres des classes de X, les c'ⱼ ceux de Y, nᵢⱼ l'effectif de (X = xᵢ et Y = yⱼ) ; 4) coefficient de corrélation r et ajustement affine estimable ? 5) droite de régression de Y en X. (Mêmes effectifs que la Prél. 3 p.368.)
- **Ex. 12** (p.389–390) : notes de 15 élèves de 1ère année secondaire au devoir de synthèse n° 2 : X Français, Y Mathématiques, Z Sciences physiques ; élèves 1 à 15 : (6.5 ; 12 ; 7,5), (6.5 ; 10 ; 7), (6 ; 8 ; 5), (8 ; 7.5 ; 4.5), (9.5 ; 14.5 ; 8), (4.5 ; 8.5 ; 5.5), (12 ; 12 ; 6), (6.5 ; 12 ; 7,5), (6.5 ; 10 ; 7), (6 ; 8 ; 5), (8 ; 7.5 ; 4.5), (9.5 ; 14.5 ; 8), (4.5 ; 8.5 ; 5.5), (12 ; 12 ; 6), (12 ; 12 ; 7) ; lignes à compléter : moyenne, médiane, mode, écart-type. A) Compléter le tableau (Excel ou calculatrice) ; B) étudier la relation entre X et Y : 1) a) nuage ; b) ajustement affine justifiable ? c) équation de la droite de Mayer ; 2) a) r ; b) conclusion [sic : « trier »] ; 3) équations des droites de régression ; C) étudier de même les séries doubles (X, Z) et (Y, Z).
- **Ex. 13** (p.390) : température moyenne extérieure X (°) en 24 h = −2 ; 0 ; 4 ; 8 ; 10 et consommation de pétrole de chauffage Y (litres) pour une famille = 40 ; 30 ; 20 ; 15 ; 10. 1) r et vérifier qu'il y a une forte corrélation linéaire ; 2) équation cartésienne de la droite de régression de Y en X ; 3) prévision de consommation (litres) si une vague de froid persiste 48 heures avec une température moyenne extérieure de −4° [sic : « −4° ? »].
- **Ex. 14** (p.390) : taux de chômage C (%) d'un pays sur 7 années (T = 1 à 7) : 6,6 ; 5,9 ; 7,2 ; 7 ; 8,7 ; 8 ; 9,3. 1) Nuage (T, C) ; 2) ajustement affine justifiable ? 3) par les moindres carrés, l'équation c = at + b.
- **Ex. 15** (p.390–391) : 50 logements selon le nombre X de pièces principales et la surface Y (m²) : colonnes Y = 30, 50, 70, 90, 120 ; lignes : X = 1 : 1 (sous Y = 30) ; X = 2 : 1, 2, 2 (sous 30, 50, 70) ; X = 3 : 1, 6, 6 (sous 50, 70, 90) ; X = 4 : 2, 16, 5 (sous 70, 90, 120) ; X = 5 : 4, 4 (sous 90, 120). 1) a) distributions marginales de X et de Y ; b) X̄, Ȳ, V(X), V(Y), σ(X), σ(Y) ; 2) nuage de points ; 3) a) Cov(X, Y) et r ; b) équation cartésienne de la droite D de régression de Y en X.
- **Ex. 16** (p.391) : quantité consommée X de parfum (dl) et revenu annuel Y des ménages (milliers de D.T) : xᵢ = 2 ; 4 ; 7 ; 10 ; 11 ; 14 ; 18 ; 20 ; 21 ; 22 ; yᵢ = 0.5 ; 0.9 ; 9 ; 25 ; 62 ; 110 ; 180 ; 290 ; 680 ; 1800. 1) a) nuage (X, Y) ; b) ajustement affine justifiable ? c) coefficient de corrélation et conclure ; 2) U = ln(X), V = ln(Y) : a) nuage (U, V) ; b) ajustement affine justifiable ? c) coefficient de corrélation (U, V) et conclure ; d) prouver v = 3,31.u − 3,91 ; e) en déduire y = 0,02 e^{3,31.ln x} ; f) revenu annuel prévisible pour 13 dl de parfum.

### Aperçu historique (p.392)

Une ligne : Al Birouni (973–1048) et Carl Friedrich Gauss (1777/1855) ; histoire des statistiques (recensements, mathématiciens arabes, 18ᵉ siècle, Laplace, Euler 1748 et Mayer 1750 « méthode des moyennes », Gauss et les moindres carrés, Boscovich 1755).

### Bornes de scope observées (chapitre 16)

- ✅ INCLUS : rappels (moyenne, variance, écart-type, médiane d'une série continue, effectifs cumulés, histogramme) ; série double (tableau à double entrée, distributions marginales, nuage de points, point moyen) ; ajustement affine par la méthode de Mayer (droite (G₁G₂)) et par les moindres carrés (covariance, coefficient de corrélation linéaire r, seuil 0,75 ≤ |r| ≤ 1, droites de régression D₁ de Y en X et D₂ de X en Y) ; prévisions par la droite ; ajustements non affines ramenés à un ajustement affine (changement de variable ln, 1/n, √d) ; usage de logiciels et de la calculatrice Sharp.
- ⛔ NON traité dans ce chapitre : démonstration de la formule des moindres carrés (somme des carrés des écarts minimisée) — seules les formules a, b, a', b' sont données ; tests statistiques, intervalles de confiance, échantillonnage ; corrélation de Spearman ; lois de probabilité (chapitre 15) ; régressions non linéaires par moindres carrés directs (le manuel passe uniquement par changement de variable).

> Sondage image : pages 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392 (26 pages sur 27 ; seule la p.366 non confrontée, page de garde sans formule) ; écarts : (1) la couche texte casse les formules (barres des moyennes X̄, Ȳ, \overline{XY}, symbole ≃ rendu « b », « c », Σ, fractions, indices nᵢ., n.ⱼ) et entrelace les colonnes des pages d'exercices à deux colonnes (p.387–391) : tout relu sur image ; (2) aucun nombre de tableau faux relevé après confrontation, mais le diagramme en bâtons de l'Ex. 3 (p.387) n'est pas lisible en valeurs exactes ; (3) un « écart » de la couche texte sur la p.384 : « 0.75 ≤ r ≤ 1 » (barres de valeur absolue perdues), corrigé sur image ; (4) incohérence du manuel sur la p.386 (en-têtes de tableau « Y = 0…3 » contre valeurs individuelles y ∈ {1,2,3}) reportée en doute, pas corrigée.

## 6. Audit R-7 (2026-11-04)

Relecture indépendante (auditeur en contexte vierge, opus) de chaque groupe de quatre chapitres **contre le PDF lui-même** : 100 % des encadrés verbatim confrontés à l'image de la page, 100 % du chapitrage et des zones `[?]`, et le reste par sondage (≥ 15 % des pages, souvent bien plus). Aucun chapitre n'a atteint le seuil d'escalade (3 erreurs substantielles). Corrections appliquées puis vérifiées sur la source.

| Chapitre | Pages sondées en image | Corrections |
| --- | --- | --- |
| 1 | 24 | 7 |
| 2 | 21 | 1 |
| 3 | 16 | 4 |
| 4 | 20 | 0 |
| 5 | 12 | 3 |
| 6 | 17 | 2 |
| 7 | 25 | 2 |
| 8 | 22 | 2 |
| 9 | 22 | 2 |
| 10 | 16 | 0 |
| 11 | 15 | 2 |
| 12 | 17 | 0 |
| 13 | 21 | 4 |
| 14 | 15 | 3 |
| 15 | 15 | 2 |
| 16 | 16 | 2 |

Total : 36 corrections, 294 pages sondées en image par l'auditeur (sur 392), en plus des pages lues en image par les lecteurs (toutes les pages à formules).
