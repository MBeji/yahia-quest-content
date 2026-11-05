<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source unique : manuel élève officiel CNP 222433P00, mathématiques, 4ème année Sciences
     expérimentales, tome 1. Page PDF = page imprimée. Ce fichier est complété chapitre par chapitre :
     il ne contient ici que le §2.4 ; les autres chapitres s'y ajoutent dans leurs propres PR. -->

# Mathématiques — Bac Sciences expérimentales (`bac-sciences-exp`) · manuel officiel CNP

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
