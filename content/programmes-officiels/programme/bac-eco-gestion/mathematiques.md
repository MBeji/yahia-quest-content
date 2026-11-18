# Mathématiques — Baccalauréat, section Économie et gestion · programme officiel CNP

> **Source** (une seule, aucun guide enseignant au corpus ⇒ le manuel élève fait référence) :
> manuel élève `222463P00.pdf` — « Mathématiques, 4ème année de l'enseignement secondaire,
> Économie et gestion », **302 pages** (page PDF = page imprimée), auteurs H. Sbika, A. Chenini,
> M. N. Dalhoumi, N. Ben Ali ; évaluateurs N. Affi, O. Ferjani. **Langue** : `fr`. **gradeSlug** :
> `bac-eco-gestion`. **subject id** : `math-bac-eco-gestion`. **Statut** : `validee-r7` (avec réserve) / `generation`
> — transcription complète (texte + image de chaque page), R-7 passée (§9) ; réserve : figures des exercices de graphes (ch. X) non transcrites arête par arête. **Transcrit le** : 2026-11-18 (A1).
>
> Couche texte propre (Times, Arial) mais les formules, tableaux de variations et graphiques s'y
> dégradent : chaque page est lue au texte ET à l'image.

## 0. Préface (p. 3)

Chaque chapitre comporte les rubriques **Pour commencer** (activités de diagnostic ou
d'introduction), **Le cours** (partie « Revoir », puis cours progressif avec activités de découverte,
définitions, résultats utiles, activités d'application), **Avec l'ordinateur**, **Exercices et
problèmes** (exercices simples d'auto-évaluation, puis exercices et problèmes en situations variées)
et **Math culture**.

## 4. Chapitrage retenu (→ `manifest/bac-eco-gestion.json`)

| # | slug | chapitre du manuel | pages |
| --- | --- | --- | --- |
| 1 | `01-limites-continuite` | I — Limites et continuité | 5-32 |
| 2 | `02-derivation-primitives` | II — Dérivation, primitives | 33-62 |
| 3 | `03-etude-de-fonctions` | III — Étude de fonctions | 63-84 |
| 4 | `04-logarithme-exponentielles` | IV — Logarithme népérien, fonctions exponentielles | 85-114 |
| 5 | `05-integrale` | V — Intégrale d'une fonction continue | 115-136 |
| 6 | `06-suites-reelles` | VI — Suites réelles | 137-164 |
| 7 | `07-matrices-systemes` | VII — Matrices et systèmes | 165-200 |
| 8 | `08-statistiques` | VIII — Statistiques | 201-236 |
| 9 | `09-probabilites` | IX — Probabilités | 237-272 |
| 10 | `10-graphes` | X — Les graphes | 273-301 |

## 6. Incertitudes / à trancher

- Les chapitres IV, VII et IX sont longs (30 à 36 pages) : un chapitre ne dépassera pas 8 notions.

## 8. Transcription par chapitre (texte + image, corrigée par la R-7)
> Pages = pages PDF = pages imprimées. Les marques `[R7 : …]` signalent les passages corrigés par l'audit. Le manuel ne donne aucun corrigé : tout recalcul est étiqueté comme tel. Les coquilles imprimées sont reproduites et signalées, jamais corrigées en silence.

---

### Chapitre `m01-p5-32`

### m01 — Manuel Mathématiques 4ᵉ éco-gestion (222463P00.pdf), Chapitre I « LIMITES ET CONTINUITE », pages PDF 5 à 32

Notation : les limites sont écrites en LaTeX simple. `x→a^+` = limite à droite, `x→a^-` = limite à gauche. Le manuel note l'ensemble des réels tantôt ℝ, tantôt IR, tantôt \ (artefact de la couche texte) : tel qu'imprimé à l'image, ℝ / IR.

#### p.5 — Page de titre du chapitre

Chapitre 1 — LIMITES ET CONTINUITE. Plan imprimé :
- Pour commencer : Limites (Revoir ; Limites et ordre ; Limite d'une fonction composée) ; Continuité (Revoir ; Continuité d'une fonction composée ; Théorème des valeurs intermédiaire [sic, imprimé ainsi] ; Théorème de la bijection)
- Avec l'ordinateur
- Exercices et problèmes
- Math culture

---

### POUR COMMENCER (pp. 6-7)

#### Activité 1 (p.6) — QCM de limites de référence
Consigne verbatim : « Pour chacune des limites ci-dessous, une seule des réponses proposées est exacte. On demande de cocher cette réponse. »
Tableau QUESTIONS / REPONSES (cases à cocher) :

| N° | Limite | Réponses proposées |
|---|---|---|
| 1 | $\lim_{x\to-\infty} x^2 =$ | $+\infty$ ; $-\infty$ |
| 2 | $\lim_{x\to-\infty} \frac{1}{x^2} =$ | $+\infty$ ; $-\infty$ ; $0$ |
| 3 | $\lim_{x\to-\infty} x^3 =$ | $+\infty$ ; $-\infty$ |
| 4 | $\lim_{x\to+\infty} \frac{1}{x} =$ | $+\infty$ ; $0$ ; $1$ |
| 5 | $\lim_{x\to0} \frac{1}{x^2} =$ | $+\infty$ ; $0$ |
| 6 | $\lim_{x\to0^-} \frac{1}{x^3} =$ | $+\infty$ ; $-\infty$ ; $0$ |
| 7 | $\lim_{x\to+\infty} \frac{x^3}{x^2} =$ | $+\infty$ ; $-\infty$ ; $\frac{3}{2}$ |
| 8 | $\lim_{x\to-\infty} \frac{x^5}{x^3} =$ | $+\infty$ ; $-\infty$ ; $\frac{5}{3}$ |
| 9 | $\lim_{x\to-\infty} \sqrt{-x} =$ | $+\infty$ ; $-\infty$ |
| 10 | $\lim_{x\to0^+} \frac{1}{\sqrt{x}} =$ | $0$ ; $+\infty$ |

Pas de corrigé dans le manuel.

#### Activité 2 (p.6)
On considère la fonction f définie par : $f(x) = \frac{x^2 - x - 2}{x^3 - 2x^2}$.
a) Vérifier que : $x^2 - x - 2 = (x-2)(x+1)$.
b) Déduire $\lim_{x\to2^+} f(x)$ et $\lim_{x\to+\infty} f(x)$.

#### Activité 3 (p.7)
Soient g, h et k les fonctions définies par : $g(x) = 2x - \frac{1}{x}$ ; $h(x) = 2x - |x|$ et $k(x) = \frac{2x - x^3}{\sqrt{2} - x}$.
Calculer :
a) $\lim_{x\to0^+} g(x)$ ; $\lim_{x\to1} g(x)$ ; $\lim_{x\to+\infty} g(x)$ ; $\lim_{x\to-\infty} g(x)$
b) $\lim_{x\to0} h(x)$ ; $\lim_{x\to1} h(x)$ ; $\lim_{x\to+\infty} h(x)$ ; $\lim_{x\to-\infty} h(x)$
c) $\lim_{x\to0} k(x)$ ; $\lim_{x\to1} k(x)$ ; $\lim_{x\to-\infty} k(x)$ ; $\lim_{x\to+\infty} k(x)$ ; $\lim_{x\to\sqrt{2}} k(x)$

#### Activité 4 (p.7) — Coût moyen
Situation : fabrication d'objets, coût moyen. Verbatim : « Le coût moyen $C_M$ de fabrication en dinars de $x$ centaines d'objets est modélisé par la fonction : $C_M(x) = 5x + 31 + \frac{1500x + 100}{x^2}$ pour $x > 0$. On appelle C sa courbe représentative dans le plan muni d'un repère orthogonal $(O, \vec{i}, \vec{j})$ »
1- Déterminer la limite de $C_M$ à droite en 0 et donner une interprétation économique de cette limite.
2- a- Déterminer la limite de $C_M$ en $+\infty$. Interpréter économiquement le résultat.
   b- Montrer que pour des valeurs de x assez grandes (x tend vers $+\infty$), la différence $C_M(x) - (5x+31)$ prend des valeurs très proche de zéro (tend vers 0).
   c- Donner une estimation du coût moyen de fabrication de 100000 objets.
Unités : x en centaines d'objets, coût en dinars. (100000 objets = 1000 centaines, donc x = 1000 : déduction mienne, le manuel ne la donne pas.)

#### Activité 5 (p.7) — Coût total par lots
Situation : « Une petite entreprise qui fabrique des jouets pour enfants estime que le coût total en milliers de dinars, de production de x milliers d'objets s'exprime en fonction de x, par :
$C(x) = -x^2 + 4x$ si $x \le 2000$ et $C(x) = x^2 + x - 1.8$ si $x > 2000$
La courbe de la fonction coût total C est donnée par le graphique ci-dessous (l'unité des abscisses étant 1000 jouets). »
1- Calculer les limites de C(x) à droite et à gauche en 2000. Interpréter le résultat
2- L'entreprise veut fabriquer 3000 jouets, est-il plus rentable de les fabriquer en un lot de 3000 ou bien en deux lots de 1500.
Graphique (p.7) : repère à graduations 1 et 4 en ordonnée, 1 et 2 en abscisse ; arc rose concave de (0,0) à (2, 4) (sommet-palier à 4), puis courbe bleue convexe qui repart de (2, un peu au-dessus de 4) en montant vers la droite : saut visible en x = 2. Décimale imprimée avec point : « 1.8 ».
Remarque d'incohérence imprimée (voir Notes) : x est dit « en milliers » mais les seuils sont écrits 2000 ; le graphique place le seuil à 2.

---

### COURS — LIMITES

#### I- Revoir (pp. 8-9)

##### Activité 1 (p.8)
« On considère la fonction f dont la représentation est donnée par la figure ci-contre.
1) Déterminer les limites suivantes :
$\lim_{x\to0} f(x)$ ; $\lim_{x\to1^-} f(x)$ ; $\lim_{x\to1^+} f(x)$
$\lim_{x\to-1^-} f(x)$ ; $\lim_{x\to-1^+} f(x)$ ; $\lim_{x\to3^-} f(x)$
2) La fonction f admet-elle une limite au point 1 ?
3) f admet-elle une limite au point -1 ? »
Figure (agrandie à 200 dpi) : repère gradué -2, -1, 0, 1, 2 en abscisse, 1 et 2 en ordonnée. Courbe : branche décroissante venant de x = -2 (haut du cadre) jusqu'au point anguleux (-1, 1) ; arc concave (-1, 1) → (0, 2) sommet → (1, 1) avec point ouvert en (1, 1) ; puis demi-droite décroissante qui part de (1, 2) [point plein] et descend jusqu'à (3, 0) au bord du cadre. (Lectures graphiques, non corrigées par le manuel.)

##### Théorème (admis) — encadré vert (p.8), verbatim
Soit I un intervalle ouvert contenant $x_0$ et f une fonction définie sur I, sauf peut être en $x_0$.
On a $\left(\lim_{x\to x_0} f(x) = \ell\right)$ si et seulement si $\left(\lim_{x\to x_0^+} f(x) = \ell \text{ et } \lim_{x\to x_0^-} f(x) = \ell\right)$
($\ell$ est fini ou infini)

##### Activité 2 (p.8)
Soit f la fonction définie par : $f(x) = x + 1$ si $x \in\ ]-\infty, 1[$ ; $f(x) = -x + 3$ si $x \in [1, +\infty[$.
Calculer les limites suivantes : $\lim_{x\to1} f(x)$ ; $\lim_{x\to0} f(x)$ ; $\lim_{x\to-\infty} f(x)$ ; $\lim_{x\to+\infty} f(x)$.

##### Opérations sur les limites (pp. 8-9)
« Les tableaux suivants donnent les règles de calcul de la limite d'une somme, d'un produit et du quotient de deux fonctions. » Tableaux verbatim (L, L' réels ; « ∞ » = infini, signe à déterminer) :

**a) Somme**
| Limite de f | Limite de g | Limite de f+g |
|---|---|---|
| L | L' | L+L' |
| L | +∞ | +∞ |
| L | −∞ | −∞ |
| +∞ | +∞ | +∞ |
| −∞ | −∞ | −∞ |
| +∞ | −∞ | Pas de conclusion |

**b) Produit**
| Limite de f | Limite de g | Limite de f×g |
|---|---|---|
| L | L' | L×L' |
| L ≠ 0 | ∞ | (règle des signes) ∞ |
| ∞ | ∞ | (règle des signes) ∞ |
| 0 | ∞ | Pas de conclusion |

**c) Quotient**
| Limite de f | Limite de g | Limite de f/g |
|---|---|---|
| L | L' | L/L' |
| L | ∞ | 0 |
| ∞ | L' | (règle des signes) ∞ |
| ∞ | ∞ | Pas de conclusion |
| L ≠ 0 | 0 | (règle des signes) ∞ |
| ∞ | 0 | (règle des signes) ∞ |
| 0 | 0 | Pas de conclusion |
(Note : la ligne « L / L' » du quotient n'impose pas L' ≠ 0 dans le tableau imprimé ; reproduit tel quel. La ligne « ∞ / L' » est imprimée sans condition L' ≠ 0 ni précision ; la ligne « ∞ / 0 » est imprimée sans précision « 0 par valeurs positives/négatives ».)

##### Activité 3 (p.9)
1- Soit la fonction $f : x \mapsto (x-2) - \frac{1}{x}$. Calculer $\lim_{x\to0^+} f(x)$ ; $\lim_{x\to0^-} f(x)$ ; $\lim_{x\to+\infty} f(x)$.
2- Calculer $\lim_{x\to0^+}\left(\frac{\sqrt{x} - x}{x}\right)$ ; $\lim_{x\to+\infty}\left(2x\left(1 - \frac{1}{x^2}\right)\right)$.

##### Activité 4 (p.9)
Calculer les limites suivantes :
$\lim_{x\to1^+}\left(x(|x| - 1) + \frac{1}{\sqrt{x-1}}\right)$ ; $\lim_{x\to-\infty}\left(2x + 7 + \frac{x^4 + 7x^3 - 31}{(2x - 11)^3}\right)$
$\lim_{x\to1}\left((x-1)^3 - \frac{2x}{x^3 - 5x + 7}\right)$ ; $\lim_{x\to+\infty}\left((x-1)^3 - \frac{2x}{x^3 - 5x + 7}\right)$

##### Activité 5 (p.9)
Calculer les limites suivantes :
a) $\lim_{x\to-\infty}(-2x^3 + 5x^2 - 1)$ ; b) $\lim_{x\to-\infty}(x^3 - x^2 + 1)^3$
c) $\lim_{x\to+\infty}\frac{-x^2 + x - 1}{4x^4 - 3x + 6}$ ; d) $\lim_{x\to-\infty}\frac{x^3 - 27}{x^2 - 5x + 6}$ ;
e) $\lim_{x\to+\infty}\left[3x - \frac{2x^2 + 1}{x - 1}\right]$ ; f) $\lim_{x\to+\infty}\left(\frac{x - 1 + \frac{1}{x}}{x^2 + x - 2}\right)$.

Encadré vert (p.9), verbatim :
« -La limite en l'infini d'une fonction polynôme est égale à celle de son terme de plus haut degré.
-La limite en l'infini d'une fonction rationnelle est égale à celle du quotient des termes de plus haut degré. »

#### II- Limites et ordre (pp. 10-12)

##### Activité 1 (p.10)
1) Peut-on calculer la limite en $+\infty$ de la fonction $h : x \mapsto \frac{\sin x}{x}$ ?
2) Soient f et g les fonctions définies par : $f : x \mapsto \frac{1}{x}$ et $g : x \mapsto -\frac{1}{x}$.
Les courbes ci-contre sont celles des fonctions f, g et h.
a- Associer chacune des fonctions à sa représentation graphique.
b- Calculer $\lim_{x\to+\infty}\frac{1}{x}$ et $\lim_{x\to+\infty}\left(-\frac{1}{x}\right)$
c- Que peut-on conjecturer pour la limite de $\frac{\sin x}{x}$ lorsque x tend vers $+\infty$
Figure : trois courbes dans un repère (graduations -10 et 10 en abscisse, 1 et -1 en ordonnée) : deux hyperboles (l'une noire, branches en haut à droite et en bas à gauche ; l'autre rose, branches en haut à gauche et en bas à droite) et une courbe rose oscillante amortie (sin x / x) coincée entre elles [R7 : le lecteur décrivait les deux hyperboles en noir ; l'attribution f/g reste à faire par l'élève].

##### Théorèmes (admis) — encadré vert (p.10), verbatim
Soit $x_0$ un réel et I un intervalle ouvert contenant $x_0$.
f, g et h trois fonctions définies sur l'intervalle I sauf peut être en $x_0$.
1) Si pour tout $x \in I$ et $x \ne x_0$ on a $f(x) \le g(x)$ et si $\lim_{x\to x_0} f(x) = \ell$ et $\lim_{x\to x_0} g(x) = \ell'$
Alors $\ell \le \ell'$.
2) Si pour tout $x \in I$ et $x \ne x_0$ on a : $h(x) \le f(x) \le g(x)$ et si $\lim_{x\to x_0} h(x) = \lim_{x\to x_0} g(x) = \ell$
Alors f admet une limite en $x_0$ et $\lim_{x\to x_0} f(x) = \ell$.
Figure d'accompagnement : courbes $C_f$ (rose, oscillante) coincée entre $C_g$ (au-dessus) et $C_h$ (au-dessous), toutes tendant vers la droite horizontale pointillée d'ordonnée $\ell$.

##### Activité 2 (p.10)
Soit f la fonction définie sur $\mathbb{R}^*$ par : $f(x) = 2 - \frac{\cos x}{|x|}$.
1) Montrer que pour tout réel $x \ne 0$ on a : $2 - \frac{1}{|x|} \le f(x) \le 2 + \frac{1}{|x|}$.
2) Calculer : $\lim_{x\to+\infty}\left(2 - \frac{1}{|x|}\right)$ et $\lim_{x\to+\infty}\left(2 + \frac{1}{|x|}\right)$.
3) Déduire $\lim_{x\to+\infty} f(x)$.
4) Calculer $\lim_{x\to-\infty} f(x)$.

##### Activité 3 (p.11)
Soit f la fonction définie sur ℝ par $f : x \mapsto -x + \sin x$.
1) Montrer que pour tout $x \in \mathbb{R}$ on a : $f(x) \le -x + 1$.
2) Calculer $\lim_{x\to+\infty}(-x + 1)$.
3) En supposant que f admet une limite en $+\infty$, prévoir la valeur de cette limite ?

##### Théorème (admis) — encadré vert (p.11), verbatim
Soit $x_0$ un réel et I un intervalle ouvert contenant $x_0$.
f et h deux fonctions définies sur l'intervalle I sauf peut être en $x_0$.
Si pour tout $x \in I$ on a $f(x) \le h(x)$ et si $\lim_{x\to x_0} h(x) = -\infty$ Alors $\lim_{x\to x_0} f(x) = -\infty$
(Figure : $C_f$ sous $C_h$, $C_h$ descendant.)

##### Activité 4 (p.11)
« Démontrer le théorème suivant : »
Théorème : Soit $x_0$ un réel et I un intervalle ouvert contenant $x_0$. f et h deux fonctions définies sur l'intervalle I sauf peut être en $x_0$.
Si pour tout $x \in I$ on a $f(x) \ge h(x)$ et si $\lim_{x\to x_0} h(x) = +\infty$ Alors $\lim_{x\to x_0} f(x) = +\infty$
(Figure : $C_f$ au-dessus de $C_h$ le long de l'asymptote verticale d'abscisse $x_0$.)

##### Remarque (p.11), verbatim
« Les théorèmes précédents restent valables lorsque $x_0$, $\ell$ et $\ell'$ sont finis ou infinis. » [imprimé « lorsqu $x_0$ » : coquille, « lorsque » attendu ; voir Notes]

##### Activité 5 (p.11)
« Dire si chacune des affirmations suivantes est vraie ou fausse en donnant une brève justification.
1) Si une fonction f vérifie : pour tout x strictement positif, $3 \le f(x) \le 3 + \frac{5}{x+2}$ alors : $\lim_{x\to+\infty} f(x) = 3$
2) Si une fonction f vérifie : pour tout x de $[5\ ;\ +\infty[$, $f(x) \le \frac{9}{x}$ alors : $\lim_{x\to+\infty} f(x) = 0$.
3) Si une fonction g vérifie : pour tout x non nul, $-\frac{3}{x^2} \le g(x) - 7 \le \frac{3}{x^2}$ alors : $\lim_{x\to+\infty} g(x) = \lim_{x\to-\infty} g(x) = 7$. »

##### Activité 6 (p.12)
Soit f la fonction définie sur $\mathbb{R}^*_+$ par $f : x \mapsto 1 + \frac{\sin x}{\sqrt{x}}$.
1) Montrer que pour tout réel $x > 0$, $-\frac{1}{\sqrt{x}} \le f(x) - 1 \le \frac{1}{\sqrt{x}}$.
[2) numéro absent à l'impression] En déduire $\lim_{x\to+\infty}[f(x) - 1]$.
3) Calculer : $\lim_{x\to+\infty}\left(1 + \frac{\sin x}{\sqrt{x}}\right)$

#### III- Limite d'une fonction composée (p.12)

##### Activité 1 (p.12)
« On considère les fonctions f et g définies respectivement sur IR \ {1} et IR \ {−1} par $f(x) = \frac{x+1}{x-1}$ et $g(x) = \frac{x-1}{x+1}$.
1- Vérifier que pour tout $x \in IR^* \setminus \{1\}$ $(g \circ f)(x) = \frac{1}{x}$.
2- a- Calculer $\lim_{x\to+\infty} f(x)$, $\lim_{x\to1} g(x)$ et $\lim_{x\to+\infty}(g \circ f)(x)$.
   b- Comparer $\lim_{x\to1} g(x)$ et $\lim_{x\to+\infty}(g \circ f)(x)$.
3-a- Calculer $\lim_{x\to1^+} f(x)$, $\lim_{x\to+\infty} g(x)$ et $\lim_{x\to1^+}(g \circ f)(x)$.
   b- Comparer $\lim_{x\to+\infty} g(x)$ et $\lim_{x\to1^+}(g \circ f)(x)$. »

Encadré bleu (définition de la composée, p.12), verbatim :
« Soient f une fonction définie sur un intervalle I et g une fonction définie sur un intervalle J tel que $f(I) \subset J$. La fonction notée $g \circ f$ définie sur I par : $g \circ f(x) = g[f(x)]$ est une fonction composée des deux fonctions g et f.
Remarquer qu'en général on a : $g \circ f \ne f \circ g$ »

##### Théorème (admis) — encadré vert (p.12), verbatim
Soient f et g deux fonctions.
Si $\left(\lim_{x\to a} f(x) = b\right)$ et $\left(\lim_{x\to b} g(x) = L\right)$ alors $\left(\lim_{x\to a}(g \circ f)(x) = L\right)$
(a, b et L sont finis ou non)

##### Activité 2 (p.12)
« En appliquant le théorème précédent, calculer les limites suivantes :
a- $\lim_{x\to+\infty}(2x - 1)^3$ ; b- $\lim_{x\to+\infty}\left(\frac{x^3 + 3}{9 - x^2}\right)^2$ ; c- $\lim_{x\to2^+}\left(\frac{2x - 5}{x - 2}\right)^3$. »

##### Conséquence — encadré gris (p.12), verbatim
Soient f une fonction définie sur intervalle ouvert I contenant $x_0$ et L un réel.
• Si f est positive sur I et $\lim_{x\to x_0} f(x) = L$ alors $\lim_{x\to x_0}\sqrt{f(x)} = \sqrt{L}$.
• Si $\lim_{x\to x_0} f(x) = +\infty$ alors $\lim_{x\to x_0}\sqrt{f(x)} = +\infty$.

##### Activité 3 (p.13)
Calculer les limites suivantes :
a) $\lim_{x\to+\infty}\sqrt{\frac{2x-1}{x}}$ ; b) $\lim_{x\to-3^+}\sqrt{\frac{x-3}{x^2-9}}$ ; c) $\lim_{x\to+\infty}\sqrt{\frac{x^2-5}{x-2}}$

##### Activité 4 (p.13)
« Soient f et g les fonctions définies respectivement sur IR et IR* par $f(x) = ax$ et $g(x) = \frac{\sin(x)}{x}$ où a est un réel non nul.
1- Donner l'expression de $g \circ f$ et prouver que : $\lim_{x\to0}\frac{\sin(ax)}{x} = a$
2- En adoptant une démarche analogue, montrer que : $\lim_{x\to+\infty} x\sin\left(\frac{1}{x}\right) = 1$. »
Encadré vert « Rappelons qu'on a : » $\lim_{x\to0}\frac{\sin x}{x} = 1$, $\lim_{x\to0}\frac{1-\cos x}{x} = 0$ et $\lim_{x\to0}\frac{1-\cos x}{x^2} = \frac{1}{2}$.

##### Activité 5 (p.13)
« Soient f, g, u, v et h les fonctions définies par :
$f : x \mapsto \frac{1-\cos x}{x}$, $g : x \mapsto \frac{1-\cos x}{x^2}$, $u : x \mapsto 2x$, $v : x \mapsto \sqrt{x}$ et $h : x \mapsto x^2$
a) Vérifier que $\frac{1-\cos(x^2)}{x} = x.(f \circ h)(x)$ et en déduire $\lim_{x\to0}\frac{1-\cos x^2}{x}$
b) Donner l'expression de $(g \circ u)(x)$ et en déduire $\lim_{x\to0}\frac{1-\cos(2x)}{x^2}$
c) Montrer que $\lim_{x\to0^+}\frac{1-\cos(\sqrt{x})}{x} = \frac{1}{2}$. »
(La fonction v n'est pas citée dans les questions a à c, la question c l'utilise implicitement par $\sqrt{x}$.)

---

### COURS — CONTINUITE (pp. 14-)

#### I- Revoir (pp. 14-15)

##### Activité 1 (p.14)
« On considère les trois fonctions f, g, h et k [sic : quatre fonctions] dont les représentations graphiques sont données par les figures ci-dessous et qui sont définies par leurs expressions suivantes :
$f : x \mapsto |x^3 + x|$ ; $g : x \mapsto |x|$ si $x \ne 0$, $f(0) = 1$ [sic : « f(0)=1 » est imprimé pour g(0) ; coquille] ; $h : x \mapsto \sqrt{x} + 1$ si $x \ge 0$, $\sqrt{-x}$ si $x < 0$ et $k : x \mapsto \frac{x-1}{x}$
1- Associer à chaque fonction sa courbe.
2- Etudier la continuité éventuelle de chacune de ces fonctions au point 0. »
Quatre figures (à l'image, agrandi 200 dpi pour la première) : (1) en V, vertex à l'origine, avec un point isolé marqué en (0, 1) ; (2) hyperbole à asymptote verticale x = 0 et asymptote horizontale y = 1 (courbe de $(x-1)/x$) ; (3) courbe à deux branches : à gauche, de $\sqrt{-x}$ qui descend jusqu'à (0, 0), à droite, de $\sqrt{x}+1$ qui part de (0, 1) : saut en 0 ; (4) courbe en U resserrée, minimum 0 en l'origine (type $|x^3+x|$) ; attribution aux fonctions : à faire par l'élève, non indiquée.

##### Théorèmes — encadré vert (p.14), verbatim
• f est continue en $x_0$ si et seulement si : $\lim_{x\to x_0} f(x) = f(x_0)$.
• f est continue à droite en $x_0$ si et seulement si : $\lim_{x\to x_0^+} f(x) = f(x_0)$.
• f est continue à gauche en $x_0$ si et seulement si : $\lim_{x\to x_0^-} f(x) = f(x_0)$.
• f est continue en $x_0$ **si et seulement si** f est continue à droite et à gauche $x_0$. [« en » absent à l'impression]
Encadré bleu : « f est continue sur l'intervalle I si elle est continue en tout point de I. (pour les bornes de I appartenant à I on considère la continuité à droite ou bien à gauche en ces bornes) »

##### Activité 2 (p.15)
« Dans chacun des cas suivants, justifier la continuité de la fonction f en $x_0$ : »
a) $f(x) = 2x - \frac{1}{x}$ en $x_0 = 1$ ; b) $f(x) = |x| + 1$ en $x_0 = -1$
c) $f(x) = \frac{x^2 - 1}{|x| + 1}$ en $x_0 = -1$ ; d) $f(x) = (x-1)(1 - \cos x)$ en $x_0 = \frac{\pi}{2}$

##### Opérations sur les fonctions continues — Théorèmes, encadré vert (p.15), verbatim
Soient f et g deux fonctions continues en $x_0$ et $\lambda \in IR$.
Les fonctions $\lambda f$, $|f|$, $f + g$ et $fg$ sont continues en $x_0$.
Si de plus $g(x_0) \ne 0$, alors les fonctions $\frac{1}{g}$ et $\frac{f}{g}$ sont continues en $x_0$.

##### Remarques (p.15), verbatim
« 1 - L'application des opérations précédentes nous permet de justifier la continuité d'une grande gamme de fonctions en utilisant la continuité de fonctions simples.
2 - Du fait que la fonction $x \mapsto x^n$, $n \in \mathbb{N}^*$ est continue sur IR on déduit que : »
Encadré vert : « Toute fonction polynôme est continue sur IR. Toute fonction rationnelle est continue sur chaque intervalle contenu dans son domaine de définition. »

##### Activité 3 (p.15)
1) Soit f la fonction définie sur IR par $f(x) = 2x^2 - 3$ si $x \in\ ]-\infty, 1[$ ; $f(x) = 1 - 2\sqrt{x}$ si $x \in [1, +\infty[$
a- Montrer que f est continue en 1.
b- En déduire que f est continue sur tout ℝ.
2) Soit g la fonction définie sur IR par $g(x) = x^2 - 1$ si $x \in\ ]-\infty, 2]$ ; $g(x) = x + \alpha$ si $x \in\ ]2, +\infty[$ $(\alpha \in IR)$
a) Justifier que g est continue sur $]-\infty, 2]$ et $]2, +\infty[$ ?
b) Comment choisir $\alpha$ pour que g soit continue sur tout IR ?

##### Activité 4 (p.15)
« Reprendre les fonctions définies dans l'activité 2 ci-dessus.
1) Déterminer leurs ensembles de définitions.
2) En utilisant le théorème précédent, étudier la continuité de chacune d'elles sur chaque intervalle contenu dans son ensemble de définition. »

#### II- Continuité d'une fonction composée (p.16)

##### Activité 1 (p.16)
« Soient u et f les fonctions définies sur IR par : $u(x) = x^2 - \frac{\pi}{4}$ et $f(x) = \cos(u(x))$
a- Prouver que u est continue en 0 et que f est continue en u(0).
b- Déterminer la limite de f en 0 et en déduire que f est continue en 0. »

##### Théorème (admis) — encadré vert (p.16), verbatim
Si f est continue en $x_0$ et g est continue en $f(x_0)$, alors la fonction $g \circ f$ est continue en $x_0$. [imprimé « gof » dans l'encadré]

##### Conséquence 1 — encadré gris (p.16), verbatim
Si f est continue en $x_0$ et positive sur un intervalle contenant $x_0$ alors $\sqrt{f}$ est une fonction continue en $x_0$.

##### Activité 2 (p.16)
« En appliquant le théorème précédent étudier la continuité de f au point $x_0$ dans chacun des cas suivants :
1) $f : x \mapsto \sqrt{x^2 - 4}$, $x_0 = \sqrt{5}$
2) $f : x \mapsto \sin\left(1 - \frac{1}{x}\right)$, $x_0 = 1$
3) $f : x \mapsto \frac{1}{\sqrt{2x-1}}$, $x_0 = 5$ »

##### Conséquence 2 — encadré gris (p.16), verbatim
Soient f et g deux fonctions : Si ( $\lim_{x\to x_0} f(x) = a$ et g est continue en a ) alors ( la fonction $(g \circ f)$ admet une limite finie en $x_0$ et cette limite est égale à g(a) )
$x_0$ étant fini ou infini et a est un réel.

##### Activité 3 (p.16)
« Déterminer les limites suivantes : »
a) $\lim_{x\to1}\sqrt{2 - x^2}$ ; b) $\lim_{x\to+\infty}\sqrt{x^2 - x + 1}$ ; c) $\lim_{x\to-\infty}\sqrt{\frac{2x^3+1}{x^3-1}}$ ; d) $\lim_{x\to+\infty}\sin\left(\frac{\pi x + 2}{6x}\right)$

#### III- Théorème des valeurs intermédiaires (pp. 17-20)

##### Activité 1 (p.17)
« Déterminer à partir de chacun des graphiques suivants, l'image de l'intervalle I : » avec trois graphiques et I = $[0, 4]$ ; I = $]-1, 6[$ ; I = $[-4, 1[$.
Figures (agrandies 200 dpi) : 
- Graphique 1 (I = [0, 4]) : arche passant par (−2, 1) environ, sommet (0, 5) [graduation 5 en ordonnée], descend jusqu'au point anguleux (2, 1), puis segment croissant jusqu'à (6, 5), puis continue de monter après 6.
- Graphique 2 (I = ]−1, 6[) : parabole de minimum (0, −1), coupant l'axe des abscisses en −1 et 1, passant par (−2, 3), montant jusqu'au sommet anguleux (2, 3) ; puis segment décroissant jusqu'à (5, 0), puis horizontal sur l'axe jusqu'à 6.
- Graphique 3 (I = [−4, 1[) : courbe oscillante amortie de part et d'autre de l'axe des abscisses (valeurs entre −1 et 1 environ), touchant l'axe en 0 [graduations imprimées irrégulières : « -2, 1, 2 » ; le point d'abscisse 0 est noté « 2 » sur la graduation de l'image ; voir Notes].

##### Activité 2 (p.17)
Soit la fonction $f : x \mapsto x^2 - 1$
a- Tracer la courbe représentative de f dans un repère orthonormé $(O, \vec{i}, \vec{j})$ du plan.
b- Déterminer graphiquement l'image de l'intervalle $[-1, 1]$ par f

##### Théorèmes (admis) — encadré vert (p.17), verbatim
* L'image d'un intervalle par une fonction continue est un intervalle.
* L'image d'un intervalle fermé [a,b] par une fonction continue est un intervalle fermé [m,M].
Encadré blanc : $f([a, b]) = [m, M]$ ; m est la plus petite valeur de f sur $[a, b]$ ; M est la plus grande valeur de f sur $[a, b]$.
Figure : courbe sur [a, b] avec m (minimum), M (maximum), f(a), f(b) repérés sur l'axe des ordonnées, segment [a, b] en vert sur l'axe des abscisses.

##### Activité 3 (p.17) — [numérotée « Activité 3 » ; la page 18 comporte une seconde « Activité 3 », voir Notes]
Soit f la fonction définie par $f(x) = 3x^2 - 2$.
1- Construire la courbe représentative de f dans un repère orthonormé du plan.
2- Déterminer les images par f de chacun des intervalles suivants : $[0, 2]$ , $[-1, 3]$ , $]-\infty, 1]$ , $[3, 5[$ , $]0, +\infty[$ , ℝ.

##### Cas d'une fonction continue et strictement monotone (p.18)

###### Activité 3 (p.18) [seconde Activité 3 du paragraphe III]
« Soit f la fonction représentée graphiquement par la courbe ci-contre.
1- Déterminer $\lim_{x\to-\infty} f(x)$ ; $f(-1)$ ; $f(1)$ ; et $\lim_{x\to+\infty} f(x)$
2- Déterminer le sens de variation de f sur chacun des intervalles $]-\infty, -1]$, $[-1, 1]$ et $[1, +\infty[$
3- Préciser les images des intervalles $]-\infty, -1]$, $[-1, 1]$ et $[1, +\infty[$ par f et les comparer respectivement aux intervalles : $\left[f(-1), \lim_{x\to-\infty} f(x)\right[$ , $[f(-1), f(1)]$ et $\left]\lim_{x\to+\infty} f(x), f(1)\right]$ »
Figure (agrandie) : courbe passant par l'origine, asymptote horizontale y = 0 en −∞ et +∞ ; minimum local au point d'abscisse −1 (pointillés bleus vers l'axe des abscisses et vers l'axe des ordonnées), maximum local au point d'abscisse 1 (pointillés bleus) ; ordonnée « 1 » graduée sur l'axe ; les ordonnées des extrema ne sont pas étiquetées (lecture image : environ −2 et +2, non imprimé → [?] ; le manuel ne donne pas de valeurs).

« Ainsi si f est une fonction continue et strictement monotone sur un intervalle I on a : » — tableau verbatim :
| Intervalle I | L'image de I par f, f strictement croissante sur I | L'image de I par f, f strictement décroissante sur I |
|---|---|---|
| $[a, b]$ | $[f(a), f(b)]$ | $[f(b), f(a)]$ |
| $[a, b[$ | $\left[f(a), \lim_{x\to b^-} f(x)\right[$ | $\left]\lim_{x\to b^-} f(x), f(a)\right]$ |
| $]a, b]$ | $\left]\lim_{x\to a^+} f(x), f(b)\right]$ | $\left[f(b), \lim_{x\to a^+} f(x)\right[$ |
| $]a, b[$ | $\left]\lim_{x\to a^+} f(x), \lim_{x\to b^-} f(x)\right[$ | $\left]\lim_{x\to b^-} f(x), \lim_{x\to a^+} f(x)\right[$ |
« (a et b sont finis ou infinis). »

###### Activité 4 (p.18)
« Soit f la fonction définie sur $[-2, 5]$ par $f(x) = |1 - 2x| - |x + 2|$.
1- Vérifier que $f(x) = -3x - 1$ si $-2 \le x \le \frac{1}{2}$ ; $f(x) = x - 3$ si $\frac{1}{2} < x \le 5$
2- Tracer la courbe représentative de f dans un repère $(O, \vec{i}, \vec{j})$ du plan.
3- Dresser le tableau de variations de f.
4- Déterminer le nombre de solutions de l'équation $f(x) = 1$ dans l'intervalle $[-2, 5]$.
5- Déterminer de même le nombre de solutions de l'équation $f(x) = 3$ dans l'intervalle $[-2, 5]$. »

###### Activité 5 (p.19) — Coût et bénéfice, produits cosmétiques
Situation : « Une entreprise de fabrication de produits cosmétiques estime que le coût total de fabrication en milliers de dinars, de p lots de 1000 pièces est donné par la fonction $C(p) = p^2 + 3p + 4$. Le lot de 1000 pièces est vendu à un prix de 15000 dinars. »
1- La courbe ci-dessous représente le bénéfice en milliers de dinars en fonction du nombre p de lots vendus. Déterminer graphiquement le nombre de pièces à fabriquer pour avoir un bénéfice maximal.
2- Déterminer une approximation du nombre minimal et du nombre maximal de pièces que l'entreprise doit fabriquer pour être rentable (avoir un bénéfice positif).
3- Déterminer graphiquement le nombre de lots que l'entreprise doit fabriquer pour avoir un bénéfice égal à 23000 dinars.
Données : C en milliers de dinars ; p = nombre de lots de 1000 pièces ; prix d'un lot = 15000 dinars (= 15 milliers de dinars). Graphique : courbe en arche (parabole) ; graduations ordonnée +10, +20, +30 ; abscisse +1, +10 ; sommet vers p = 6, ordonnée un peu au-dessus de 30 ; coupe l'axe des abscisses vers p ≈ 0,3 et p ≈ 11,7 ; ordonnée à l'origine négative (≈ −4). (Lecture image ; cohérente avec le bénéfice $15p - C(p)$, expression non imprimée par le manuel.)

##### Théorème (admis) — encadré vert (p.19), verbatim — Théorème des valeurs intermédiaires
« Si une fonction f est continue sur un intervalle fermé [a ; b] et si k est un réel quelconque compris entre f(a) et f(b) (ces deux valeurs comprises), alors il existe au moins un réel $x_0$ dans [a ; b] tel que $f(x_0) = k$ »
(Mots soulignés/en gras à l'impression : « Si », « continue », « intervalle », « si », « alors », « existe au moins ».)
Texte d'accompagnement (italique) : « Notons que f prend toutes les valeurs intermédiaires entre f(a) et f(b), c'est pour cela que ce théorème est connu sous le nom " Théorème des valeurs intermédiaires ". »
Figure : courbe sur [a, b], droite horizontale y = k coupant la courbe en trois points d'abscisses $x_0$, $x_1$, $x_2$.

##### Activité 6 (p.20)
« On considère l'équation : $x\sqrt{x} - x - 1 = 0$ (E).
a) Montrer que la fonction $f : x \mapsto x\sqrt{x} - x - 1$ est continue sur $IR_+$.
b) Montrer que (E) admet au moins une solution dans $[1, 4]$. »

##### Remarque (p.20), verbatim
« Si de plus f est **strictement monotone** sur l'intervalle [a , b], alors l'équation f(x) = k admet une solution unique dans [a , b]. »
Figures : f croissante (f(a) < k < f(b)) et f décroissante (f(b) < k < f(a)) avec le point $x_0$ unique tel que f($x_0$) = k.

##### Activité 7 (p.20)
« Soit la fonction $f : x \mapsto \sqrt{x^2 - 1} - 1$.
1- Déterminer le domaine de définition de f.
2- Prouver que f est continue sur l'intervalle $[1, +\infty[$.
3- Montrer que f est strictement croissante sur $[1, +\infty[$.
4- Calculer f(2) et f(3) puis montrer que l'équation f(x) = 1 admet dans $[1, +\infty[$ une solution unique c.
5- Calculer f(1).f(2) et montrer que l'équation f(x) = 0 admet dans $]1, 2[$ une solution unique c'. Calculer la valeur de c'. »

##### Corollaire — encadré vert (p.20), verbatim
« **Si** f est une fonction **continue** sur un **intervalle** fermé [a ; b] et Si f(a).f(b) < 0 **alors** l'équation f(x) = 0 admet au moins une solution dans l'intervalle ]a, b[ . »
Illustration (deux figures) : « Cas d'une solution unique » (f décroissante de f(a) > 0 à f(b) < 0, un seul zéro $x_0$) ; « Cas de solutions multiples » (trois zéros $x_0$, $x_1$, $x_2$).

##### Activité 8 (p.21)
« Soit la fonction $f : x \mapsto x^3 + x - 1$.
1- Justifier la continuité de f sur [0, 1].
2- Montrer que l'équation : f(x) = 0 admet une solution unique $\alpha$ comprise entre 0 et 1.
3- Calculer $f(\frac{1}{2})$ et vérifier que : $\alpha \in \left[\frac{1}{2}, 1\right]$.
4- Calculer $f(\frac{3}{4})$ et vérifier que : $\alpha \in \left[\frac{1}{2}, \frac{3}{4}\right]$.
5- Calculer $f(\frac{5}{8})$ et vérifier que : $\alpha \in \left[\frac{5}{8}, \frac{3}{4}\right]$.
6- Calculer $f(\frac{11}{16})$ et en déduire un encadrement de $\alpha$.
7- Calculer f(0,682) et f(0,683) et donner un encadrement de $\alpha$ à $10^{-3}$ près. »

##### Résolution d'équations par dichotomie (p.21), verbatim
« f étant une fonction continue et strictement monotone sur un intervalle [a, b], on sait que si f(a).f(b)<0 alors l'équation f(x)= 0 possède une unique solution $x_0$ dans [a, b].
Pour encadrer la valeur de $x_0$ on peut utiliser le *principe de la dichotomie* qui consiste à partager l'intervalle [a, b] en deux intervalles de même amplitude : $\left[a, \frac{a+b}{2}\right]$ et $\left[\frac{a+b}{2}, b\right]$ et à reconnaître celui qui contient $x_0$, puis on recommence le même travail avec cet intervalle jusqu'à ce qu'on obtienne un encadrement satisfaisant de $x_0$. »
**Algorithme** (verbatim) :
« Soit $x_0$ la solution de l'équation f(x) = 0.
On veut trouver un encadrement de $x_0$ à $10^{-n}$ près ($n \in \mathbb{N}^*$).
• Si f(a) = 0 ou f(b) = 0, le problème est résolu.
• Si f(a).f(b) < 0, on détermine le réel $c = \frac{a+b}{2}$ milieu de [a, b] et on calcule f(c)
  o Si f(c) = 0 alors $x_0 = c$ et le problème est résolu.
  o Si f(c) ≠ 0, la solution $x_0$ est soit dans [a, c] soit dans [c, b].
On reprend les mêmes étapes sur l'intervalle qui contient $x_0$ jusqu'à avoir un encadrement d'amplitude $10^{-n}$ de la solution. »

##### Activité 9 (p.21)
« On considère la fonction f définie sur l'intervalle [0, 4] par $f(x) = x + \sqrt{x} - 3$
1. Montrer que f est continue et strictement croissante.
2. Expliquer pourquoi il existe un unique réel a de [0,4] tel que f(a) = 0.
3. A l'aide de votre calculatrice, donner une valeur approchée de a à $10^{-2}$ près.
4. Donner le signe de f(x) sur [0,4]. »

##### Activité 10 (p.22)
« On considère l'équation (E) : ($x^3 - 3x^2 + 4x - 1 = 0$) et on donne les courbes représentatives ci-dessous des fonctions f et g définies sur ℝ par : $f(x) = x^3 - 3x^2$ et $g(x) = -4x + 1$.
1- Vérifier que l'équation (E) est équivalente à l'équation : $f(x) - g(x) = 0$
2- En déduire graphiquement que (E) admet une unique solution $\alpha$ dont on donnera une valeur approchée à $10^{-1}$ près. »
Figure : repère gradué de −5 à +5 environ ; courbe rose de $x^3 - 3x^2$ (minimum local en x = 2, ordonnée −4 ; passe par l'origine) et droite bleue $y = -4x + 1$ ; un cadre « Agrandissement » zoome sur la zone d'intersection (abscisses 0,2 ; 0,3 ; 0,4 graduées dans l'agrandissement) où la droite et la courbe se coupent.

#### IV- Théorème de la bijection (pp. 22-23)

##### Activité 1 (p.22)
« Soit f la fonction définie sur l'intervalle $[0, +\infty[$ par $f(x) = 4x^2 - 1$
Montrer que f est strictement croissante sur $[0, +\infty[$.
1- Vérifier que $f([0, +\infty[) \subset [-1, +\infty[$.
2- Montrer que tout élément y de $[-1, +\infty[$ admet un unique antécédent x par f dans $[0, +\infty[$ et que $x = \frac{1}{2}\sqrt{y+1}$. »
Commentaire (verbatim) : « Notons alors que tout élément de $[0, +\infty[$ a une image par f dans $[-1, +\infty[$ et que tout élément de $[-1, +\infty[$ a un seul antécédent par f dans $[0, +\infty[$.
On dit que f réalise une bijection de $[0, +\infty[$ dans $[-1, +\infty[$ et il existe une fonction notée $f^{-1}$ appelée **fonction réciproque** ou **bijection réciproque** de f.
$f^{-1}$ est définie sur $[-1, +\infty[$ par $f^{-1}(x) = \frac{1}{2}\sqrt{x+1}$. »

##### Théorème (admis) — encadré vert (p.22), verbatim
« Si une fonction f est **strictement monotone** sur un intervalle I alors :
• f est une bijection de l'intervalle I sur f(I)
• La fonction réciproque $f^{-1}$ de f a le même sens de variation que f.
Si de plus, la fonction f est **continue** sur I, alors
La fonction réciproque $f^{-1}$ de f, est une bijection continue de l'**intervalle** J = f(I) sur I »

##### Remarque (p.23), verbatim
« Pour tout $x \in I$ et $y \in J$, $y = f(x) \Leftrightarrow x = f^{-1}(y)$. »

##### Activité 2 (p.23)
« Soit f la fonction définie sur $IR_+$ par $f(x) = x^2$
1) Montrer que f est une bijection de $IR_+$ sur $IR_+$.
2) Définir la fonction réciproque $f^{-1}$ de f.
3) Construire dans un repère orthonormé $(O, \vec{i}, \vec{j})$ du plan la droite $\Delta$ d'équation : y = x et les courbes représentatives de f et $f^{-1}$. Que remarquez-vous pour ces deux courbes ? »
« On admet que : » (encadré vert, verbatim) « Les courbes représentatives de f et de $f^{-1}$ dans un repère orthonormé du plan, sont symétriques par rapport à la droite $\Delta : y = x$. »
« Pour tout $x \in I$ et $y \in J$ : $M(x, y) \in C_f \Leftrightarrow M'(y, x) \in C_{f^{-1}}$ »
Figure : repère orthonormé gradué (−1, +1, +2, +3), droite $\Delta : y = x$, deux courbes $C_f$ (rose, type racine, partant de (−1, 0) environ) et $C_{f^{-1}}$ (bleue, type parabole partant de (0, −1)) symétriques par rapport à $\Delta$, points M(x, y) et M'(y, x) avec pointillés (figure générique, ne correspond pas à $x^2$ de l'activité : voir Notes).

##### Activité 3 (p.23)
« Soit la fonction $f : x \mapsto \sqrt{1 - x}$.
a- Montrer que f est strictement décroissante sur $]-\infty, 1]$.
b- En déduire que f est une bijection de $]-\infty, 1]$ sur $[0, +\infty[$.
c- Représenter graphiquement f et $f^{-1}$ dans un même repère orthonormé $(O, \vec{i}, \vec{j})$ du plan. »

##### Activité 4 (p.23)
« Soit la fonction $f : x \mapsto \frac{4}{x^2}$
1- Montrer que f est strictement décroissante sur $]0, +\infty[$.
2- Déterminer les images des intervalles $]0, 1]$, $[1, 2]$ et $[1, +\infty[$ par f. »

##### Activité 5 (p.23)
« Soit la fonction $f : x \mapsto \frac{2x}{x^2 + 1}$.
1- Etudier le sens de variation de f.
2- Déterminer les images des intervalles $]-1, 1[$ et $[1, +\infty[$ par f. »

---

### AVEC L'ORDINATEUR (pp. 24-)

#### Recherche d'une valeur approchée de π (p.24 et suivantes)
Texte verbatim (p.24) : « On peut considérer l'aire du cercle unitaire comme étant la limite de l'aire d'un polygone régulier à n côtés (polygone à n cotés isométriques) inscrit dans le cercle ou circonscrit au cercle, lorsque n tend vers l'infini.
D'autre part, l'aire du cercle de rayon 1, est égale à π et on remarque que : lorsque le nombre n de côtés augmente l'aire du polygone devient de plus en plus proche de la valeur de π. »
Figures : un pentagone régulier inscrit et circonscrit au cercle unitaire, légendé « n = 12 » [sic, inversé] ; un dodécagone régulier inscrit et circonscrit, légendé « n = 5 » [sic, inversé] (voir Notes).
« A l'aide d'un tableur (exemple : Excel), remplir le tableau contenant les mesures des aires en fonction du nombre n de cotés pour des valeurs de n de plus en plus grandes.
Pour calculer l'aire du polygone inscrit dans le cercle unitaire, on utilisera la formule suivante : $A_i = \frac{n}{2}\sin\frac{2\pi}{n}$
Pour calculer l'aire du polygone circonscrit au cercle unitaire, on utilisera la formule suivante : $A_c = n\,\mathrm{tg}\frac{\pi}{n}$ »
**Etape 1** : « Remplir la colonne « nombre d'arêtes » — Les cellules A3 jusqu'à A15 contiennent le nombre d'arêtes du polygone inscrit »
Capture d'écran du tableur (p.24) : colonne A « Nombre d'arêtes » : A3 = 4, puis 10, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150 (13 valeurs, A3 à A15) ; colonne B « Aire du polygone inscrit » ; colonne C « Aire du polygone circonscrit » (en-tête coupé) ; barre de formule affichée : B3 = `=(A3/2*SIN(2*PI()/A3))` ; B3 affiche « 2 ».

**Etape 2** (p.25) : « Dans la cellule B3, écrire la formule : =(A3/2*SIN(PI()/A3)) permettant de calculer l'aire d'un polygone inscrit en fonction du nombre d'arêtes » [formule imprimée telle quelle ; incohérente avec $A_i = \frac{n}{2}\sin\frac{2\pi}{n}$ et avec la capture p.24 « =(A3/2*SIN(2*PI()/A3)) » : voir Notes]
**Etape 3** : « Recopier la formule B3 dans les cellules B4 jusqu'à B15 »
**Etape 4** : « Dans la cellule C3, écrire la formule =(A3*SIN(PI()/A3)/COS(PI()/A3)) permettant de calculer l'aire d'un polygone circonscrit en fonction du nombre d'arêtes »
**Etape 5** : « Recopier la formule C3 dans les cellules C4 jusqu'à C15, on obtient le tableau suivant : »
Tableau (p.25, lu à 200 dpi ; décimales avec virgule ; recomptés avec n/2·sin(2π/n) et n·tan(π/n) : tous conformes) :

| Nombre d'arêtes | Aire du polygone inscrit | Aire du polygone circonscrit |
|---|---|---|
| 4 | 2 | 4 |
| 10 | 2,938926261 | 3,249196962 |
| 50 | 3,133330839 | 3,145733363 |
| 60 | 3,135853898 | 3,144466757 |
| 70 | 3,137375812 | 3,143703625 |
| 80 | 3,138363829 | 3,143208561 |
| 90 | 3,139041318 | 3,142869254 |
| 100 | 3,139525976 | 3,142626604 |
| 110 | 3,139884597 | 3,1424471 |
| 120 | 3,140157375 | 3,142310588 |
| 130 | 3,140369669 | 3,14220436 |
| 140 | 3,140538125 | 3,142120077 |
| 150 | 3,14067403 | 3,142052086 |

(Capture intermédiaire de l'étape 4 : C3 = 4 seulement, C4 à C15 vides ; barre de formule « C3 : =(A3*SIN(PI()/A3)/COS(PI()/A3)) ».)
**Etape 6** : « Sélectionner les trois colonnes A, B et C »
**Etape 7** : « Cliquer sur le bouton « Assistant graphique ». » (capture : « Assistant Graphique - Étape 1 sur 4 - Type de Graphique »)
**Etape 8** : « Sélectionner la commande « Nuage de points ». Poursuivre la démarche en cliquant à chaque fois sur le bouton « Suivant ». »

##### Résultat graphique (p.26)
« On obtient le graphique suivant : » nuage de points, abscisse 0 à 150, ordonnée 0 à 5 ; deux courbes (légende : « aire du polygone inscrit », « aire du polygone circonscrit ») : la courbe démarrant à 4 (n = 4, rose) décroît et celle démarrant à 2 (bleue) croît ; elles se confondent près de 3,14 dès n ≈ 30-50. (Les deux traits de la légende sont noirs à l'impression ; l'attribution des couleurs est déduite des valeurs de départ 2 et 4.)
« Observation des valeurs proches de π pour un grand nombre d'arêtes » — tableau (p.26, lu à 200 dpi, recompté : conforme) :

| Nombre d'arêtes | Aire du polygone inscrit | Aire du polygone circonscrit |
|---|---|---|
| 4 | 2 | 4 |
| 10 | 2,938926261 | 3,249196962 |
| 50 | 3,133330839 | 3,145733363 |
| 200 | 3,141075908 | 3,141851065 |
| 500 | 3,141509971 | 3,141633996 |
| 1000 | 3,141571983 | 3,141602989 |
| 5000 | 3,141591827 | 3,141593067 |
| 10000 | 3,141592447 | 3,141592757 |
| 100000 | 3,141592652 | 3,141592655 |

Pas de questions posées dans cette rubrique « Avec l'ordinateur » : c'est une procédure guidée (étapes 1 à 8) suivie d'un constat (« valeurs proches de π »).

---

### EXERCICES ET PROBLEMES (pp. 27-)

#### Exercice 1 (p.27) — QCM limites
« Pour chacune des questions ci-dessous, une seule des réponses proposées est exacte. » Tableau QUESTIONS / REPONSES (cases à cocher) :

| N° | Limite | Réponses |
|---|---|---|
| 1 | $\lim_{x\to-\infty}(-5x^2 - 3x + 4) =$ | $+\infty$ ; $-\infty$ ; $4$ |
| 2 | $\lim_{x\to+\infty}\left(\frac{1}{x^3} + x^2 - 1\right) =$ | $0$ ; $+\infty$ ; $-1$ |
| 3 | $\lim_{x\to+\infty}\left(\frac{1}{x^3} - x^2 - 1\right)^3 =$ | $+\infty$ ; $-\infty$ |
| 4 | $\lim_{x\to+\infty}\left(\frac{2x-1}{x+8}\right) =$ | $+\infty$ ; $-\frac{1}{8}$ ; $2$ |
| 5 | $\lim_{x\to+\infty}\left(\frac{4x^3 - 6x}{x^2+1}\right) =$ | $+\infty$ ; $4$ ; $6$ |
| 6 | $\lim_{x\to-\infty}\left(\frac{x+5}{x^2+3x+2}\right) =$ | $-\infty$ ; $\frac{5}{2}$ ; $0$ |
| 7 | $\lim_{x\to0}\left\|\frac{x^3-6}{x^2+1}\right\| =$ | $+\infty$ ; $6$ ; $0$ |
| 8 | $\lim_{x\to-\infty}\left\|\frac{x+1}{x^2+3x-2}\right\| =$ | $+\infty$ ; $-\frac{1}{2}$ ; $0$ |
| 9 | $\lim_{x\to2^+}\left(\frac{2-x}{4-4x+x^2}\right) =$ | $+\infty$ ; $-\infty$ |
| 10 | $\lim_{x\to1}(3x^2 - x - 2) =$ | $1$ ; $0$ ; $-2$ |
| 11 | $\lim_{x\to0}\frac{\sin x}{x} =$ | $1$ ; $0$ |
| 12 | $\lim_{x\to-1}\sqrt{2x^2+1} =$ | $+\infty$ ; $1$ ; $\sqrt{3}$ |

#### Exercice 2 (p.27) — Continuité (cocher la ou les réponses correctes)
« Pour chacune des questions ci-dessous cocher la ou les réponse(s) correcte(s) » Tableau :
- « La fonction $f : x \mapsto |x - 1|$ si $x > 1$ ; $2x - 1$ si $x \le 1$ » — réponses : « f est continue en 1 » ; « f n'est pas continue en 1 » ; « f est continue en 2 ».
- « La fonction $f : x \mapsto x^2 + 1$ si $x > 0$ ; $\frac{1}{x^2+1}$ si $x \le 0$ » — réponses : « f est continue en 0 » ; « f n'est pas continue en 0 » ; « f est continue sur ℝ ».
- « La fonction $f : x \mapsto \sqrt{2 - x}$ si $x < 2$ ; $\frac{x}{x-1}$ si $x \ge 2$ » — réponses : « f n'est pas continue en 2 » ; « f est continue en 2 » ; « f est continue sur $]-\infty, 2]$ ».

#### Exercice 3 (pp. 27-28) — « Calculer les limites suivantes si elles existent »
1) a- $\lim_{x\to+\infty}(3x^2 - x + 3)$ ; b- $\lim_{x\to-\infty}(-5x^2 + x + 3)$
2) a- $\lim_{x\to+\infty}(2x^3 + 5x - 2)$ ; b- $\lim_{x\to-\infty}(5x^3 + 2x - 2)$
3) a- $\lim_{x\to+\infty}(-3x^4 + x - 1)$ ; b- $\lim_{x\to-\infty}(-5x^4 + 2x - 1)$

#### Exercice 4 (p.28) — « Calculer les limites suivantes si elles existent »
1) a- $\lim_{x\to+\infty}\left(2 + \frac{1}{x} + \frac{2}{x^2}\right)$ ; b- $\lim_{x\to-\infty}\left(1 + \frac{1}{2x} + \frac{1}{x^2}\right)$
2) a- $\lim_{x\to+\infty}\left(\frac{2x+1}{x-2}\right)$ ; b- $\lim_{x\to-\infty}\left(\frac{x+1}{3x-2}\right)$
3) a- $\lim_{x\to+\infty}\left(x - \frac{5x+1}{x}\right)$ ; b- $\lim_{x\to-\infty}\left(2x - \frac{3x^2+1}{4x}\right)$
4) a- $\lim_{x\to+\infty}\left(\frac{x^2+2x-1}{3x^2-x+2}\right)$ ; b- $\lim_{x\to+\infty}\left(\frac{2x^3-5x^2-3}{3x^2-x-1}\right)$
5) a- $\lim_{x\to1}\left(\frac{3x^2-x-2}{x-1}\right)$ ; b- $\lim_{x\to2}\left(\frac{x^3-8}{x-2}\right)$ ; c- $\lim_{x\to2^+}\left(\frac{x^2-5x+6}{(x-2)^2}\right)$
6) a- $\lim_{x\to1^+}\left(\frac{1}{1-x} - \frac{1}{1-x^2}\right)$ ; b- $\lim_{x\to1^-}\left(\frac{1}{1-x} - \frac{1}{1-x^2}\right)$
7) a- $\lim_{x\to2^-}\left(\frac{x^2-5x+6}{(x-2)^2}\right)$ ; b- $\lim_{x\to2^+}\left(\frac{x^2-5x+6}{(x-2)^2}\right)$
(Remarque : 4-5-c et 4-7-b sont identiques à l'impression, voir Notes.)

#### Exercice 5 (p.28) — « Calculer les limites suivantes si elles existent »
1) a- $\lim_{x\to+\infty}\sqrt{x^2-x-2}$ ; b- $\lim_{x\to+\infty}\left(\sqrt{x^2-1}+2x\right)$ ; c- $\lim_{x\to-\infty}\left(\sqrt{x^2-1}-2x\right)$
2) a- $\lim_{x\to+\infty}\left(2x - \sqrt{4x^2-x}\right)$ ; b- $\lim_{x\to-\infty}\left(\sqrt{x^2-1}+2x\right)$
3) a- $\lim_{x\to-\infty}\sqrt{\frac{2-x}{x^2+1}}$ ; b- $\lim_{x\to+\infty} x\sqrt{\frac{2+x}{x^2-1}}$ ; c- $\lim_{x\to1^+}\frac{2x}{\sqrt{x^2-1}}$ ; d- $\lim_{x\to0^+}\left(\frac{\sqrt{x}-x}{x}\right)$

#### Exercice 6 (p.28)
a- « Calculer les limites suivantes : » $\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}$ , $\lim_{x\to0}\frac{\sqrt{x+4}-2}{x}$ et $\lim_{x\to0}\frac{\sqrt{x+9}-3}{x}$
b- « En déduire : » $\lim_{x\to0}\frac{\sqrt{x+1}+\sqrt{x+4}+\sqrt{x+9}-6}{x}$

#### Exercice 7 (p.28)
« Dans chacun des cas suivants, déterminer le domaine de définition de la fonction f et calculer les limites de f(x) aux bornes de ce domaine : »
a- $f : x \mapsto \frac{x-2}{-x^2+x+2}$ ; b- $f : x \mapsto \frac{2x-4}{x^2-x+1}$
c- $f : x \mapsto \frac{x^2+2x-1}{x+2}$ ; d- $f : x \mapsto \frac{x+3}{x^2-5x+6}$

#### Exercice 8 (p.28)
« Soit f la fonction définie sur l'intervalle I = ]0 ; 3[ par : $f(x) = \frac{3x-1}{x^2-3x}$
1- Etudier le signe de f sur l'intervalle I.
2- Déterminer les limites de f aux bornes de l'intervalle I. »

#### Exercice 9 (p.29)
« Soit f la fonction définie par : $f(x) = \frac{2x-5}{x^2-6x+9}$
1- Déterminer le domaine de définition $\mathcal{D}$ de f puis étudier son signe.
2- Déterminer les limites de f aux bornes de $\mathcal{D}$. »

#### Exercice 10 (p.29)
« Justifier la continuité de chacune des fonctions suivantes sur l'intervalle I : »
1) $f(x) = (x^2 - 5)^4$ ; I = IR
2) $f(x) = \left(\frac{3x-4}{x-1}\right)^2$ ; I = $]1, +\infty[$
3) $f(x) = \frac{1}{\sqrt{1+x^2}}$ ; I = $]-\infty, 0]$
4) $f(x) = \sqrt{3 + \cos^2 x}$ ; I = IR
5) $f(x) = \sin\left(\frac{\pi}{x}\right)$ ; I = $[0, +\infty[$
6) $f(x) = \sin(\sqrt{x})$ ; I = $[0, +\infty[$

#### Exercice 11 (p.29)
a) « f est une fonction vérifiant : pour tout réel $x > 1$, $1 - \frac{1}{x^2} \le f(x) \le \frac{x+1}{x}$. Peut-on calculer la limite de f en $+\infty$ ? Si oui déterminer cette limite. »
b) « g est une fonction vérifiant : pour tout réel $x > 10$, $-1 - \frac{1}{\sqrt{x}} < f(x) < -\frac{2}{\sqrt{x}}$ [sic : « g » annoncé, « f(x) » imprimé]. Peut-on calculer la limite de f en $+\infty$ ? »
c) « Calculer : $\lim_{x\to0}\frac{1-\cos(2x)}{x^2}$ »

#### Exercice 12 (p.29)
« Soit f la fonction définie sur $\mathbb{R}^*$ par : $f(x) = \frac{1}{x^2} + \sin\left(\frac{1}{x}\right)$. Calculer les limites de f en 0, $+\infty$ et $-\infty$. »

#### Exercice 13 (p.29)
« Soit u une fonction définie sur $[1, +\infty]$ [sic] et telle que : Pour tout $x \in [1\ ;\ +\infty[$, $0 \le u(x) \le x$ et soit f la fonction définie sur $[1, +\infty]$ [sic] par $f(x) = 1 + \frac{u(x)}{x^2}$.
1) Montrer que si $x \ge 1$ on a : $-\frac{1}{x} + 1 \le f(x) \le \frac{1}{x} + 1$.
2) En déduire la limite de f en $+\infty$. »

#### Exercice 14 (p.29)
« Soit dans IR l'équation : $x^3 - 3x^2 + 1 = 0$ (E).
1- Montrer que l'équation (E) admet une solution dans l'intervalle $]-1, 0[$.
2- On pose $f(x) = x^3 - 3x^2 + 1$ pour $x \in IR$
   a- Calculer f(0) et f(3).
   b- Peut-on appliquer le corollaire de la page 30 sur l'intervalle $[0, 3]$ ? [renvoi de page imprimé « page 30 » ; le corollaire est p.20 : voir Notes]
   c- Calculer f(2) et en déduire que l'équation (E) admet deux autres solutions.
3- Donner un encadrement d'amplitude 0,5 de chacune des trois solutions de (E). »

#### Exercice 15 (pp. 29-30)
« Soit f la fonction définie sur IR par $f(x) = |3x^2 + x - 4| - 2$
1- Calculer les limites de f en $-\infty$ et en $+\infty$.
2- montrer que f est continue sur IR.
3- Tracer la courbe représentative de f dans un repère orthonormé du plan.
4- A l'aide du graphique, déterminer le nombre de solutions de l'équation f(x) = 0.
5- Donner un encadrement de chacune des solutions à $10^{-2}$ près.
6- Déterminer les valeurs exactes des solutions. »

#### Exercice 16 (p.30)
« Soit f la fonction définie sur IR par $f(x) = \frac{1}{3}x^3 + \frac{1}{2}x^2 - 6x$
1- Calculer les limites de f en $-\infty$ et en $+\infty$.
2- Etudier les variations de f.
3- a- calculer f(−3) et f(2).
   b- Montrer que l'équation f(x) = 5 admet exactement trois solutions.
   c- Donner un encadrement à $10^{-1}$ près de la solution qui appartient à l'intervalle $[-3, 2]$. »

#### Exercice 17 (p.30)
« Soit f la fonction définie sur $IR_+$ par : $f(x) = \sqrt{x} + x^2 - 4$.
1) Montrer que f est continue et strictement croissante sur $IR_+$.
2) En déduire que f réalise une bijection de $IR_+$ sur lui même.
3) Montrer que l'équation f(x) = 0 admet une unique solution $\alpha$ dans $[0, +\infty[$ et que $1{,}6 < \alpha < 1{,}7$. »

#### Exercice 18 (p.30)
« On considère l'équation : $x^4 - 4x^3 + 2 = 0$ (E)
a) En utilisant le sens de variation de la fonction $f : x \mapsto x^4 - 4x^3 + 2$, montrer que (E) admet une solution unique $\alpha$ sur l'intervalle $[0, 1]$.
b) Trouver un encadrement de $\alpha$ d'amplitude $10^{-1}$.
c) Montrer que (E) admet une solution unique $\beta$ sur l'intervalle $[3, 4]$ puis trouver un encadrement d'amplitude $10^{-1}$ de $\beta$. »

#### Exercice 19 (p.30) — Coefficient directeur et coût unitaire moyen
« Soit f la fonction définie sur ℝ par $f(x) = x^2 + 4$.
1) Tracer la courbe C de f dans un repère orthonormé du plan.
2) Pour chaque point M de C d'abscisse x non nulle on considère la droite (OM) et on désigne par d(x) le coefficient directeur de (OM). Vérifier que $d(x) = x + \frac{x}{4}$. [sic : à l'image, numérateur x, dénominateur 4 ; voir Notes : le coefficient directeur de (OM) vaut $\frac{x^2+4}{x}$]
3) Etudier la limite de d en 0, en $+\infty$ et en $-\infty$.
4) Pour quelle position de M a-t-on : a) d(x) = 5 ? b) d(x) = 4 ? c) d(x) = 2 ?
5) Pour t non nul, soit $M(t, t^2 + 4)$ et $D_t$ la droite (OM). Déterminer selon les valeurs de t, le nombre de points d'intersection de C et $D_t$.
6) Expliquer les résultats trouvés dans 4).
7) En économie, si f(x) représente le coût de production de x objets (pour x > 0), expliquer pourquoi d(x) représente le coût unitaire moyen pour une production de x objets. »

#### Exercice 20 (p.31) — Coût total, prix de vente, bénéfice
Situation (verbatim) : « Le coût total de fabrication d'une quantité x d'un produit, exprimée en centaines d'unités, est représenté graphiquement par la courbe ci-contre.
1- Déterminer la quantité d'objets, à la centaine près, à fabriquer pour avoir un coût minimum.
2- On suppose que le prix de vente d'une centaine d'objets est égal à 13 000 dinars. Déterminer graphiquement le nombre minimum et le nombre maximum d'objets que l'entreprise doit fabriquer pour réaliser un bénéfice. »
Graphique (lu à 200 dpi) : trois courbes avec légende « Cq » (gris, coût, convexe), « prix de vente » (bleu, droite), « Bénéfice » (rose, arche coupant l'axe des abscisses) ; ordonnées graduées +1000, +2000, … +10000 ; abscisse : graduation « 1000 » à droite de l'axe. La courbe de bénéfice a un maximum voisin de 1000 (au-dessus de la graduation « +1000 » à l'image). Aucune expression algébrique du coût n'est donnée. Incohérence apparente (voir Notes) : x en centaines d'unités mais la graduation d'abscisse porte « 1000 ».

#### Exercice 21 (p.31) — Épidémie
« A la suite d'une épidémie dans une région, on a constaté que le nombre de malades, n jours après l'apparition des premiers cas, est : $-n^3 + 75n^2$, pour n entier tel que $0 < n < 60$.
Soit f la fonction définie sur [0 ; 60] par : $f(x) = -x^3 + 75x^2$
On donne sur le graphique ci-contre, la courbe représentative de f.
1-a- Déterminer graphiquement le jour où le nombre de malades est maximal durant cette période de 60 jours.
   b- Préciser le nombre de malades ce jour là
2- a- Déterminer graphiquement le jour où le nombre de malades est égal à 22000
   b- Déterminer graphiquement la période durant laquelle le nombre de malades est supérieur à 56000. »
Graphique : abscisse graduée 0, 20, 40, 60, 80 ; ordonnée 0 à 70000 par pas de 10000 ; arche de maximum voisin de 62000-63000 vers l'abscisse 50, courbe tracée de 0 à 60.

#### Exercice 22 (p.31) — Problème : coût moyen
« **Partie A** Soit g la fonction définie sur $[0\ ;\ +\infty[$ par : $g(x) = x^3 - 1200x - 100$.
1- Déterminer la limite de g en $+\infty$. Etudier le sens de variation de g et dresser son tableau de variation.
2- Montrer que l'équation g(x) = 0 admet une solution unique $\alpha$ dans l'intervalle [20 ; 40]. Donner une valeur approchée de $\alpha$ à l'unité près.
3- En déduire le signe de g(x) suivant les valeurs de x.
**Partie B** Soit f la fonction définie sur $]0\ ;\ +\infty[$ par : $f(x) = x + 50 + \frac{1200x + 50}{x^2}$.
On appelle C sa courbe représentative dans le plan muni d'un repère orthogonal $(O, \vec{i}, \vec{j})$
1- Déterminer la limite de f à droite en 0 et en $+\infty$.
2- Etudier les variations de f.
3- Montrer que la droite D d'équation y = x + 50 est asymptote à la courbe C.
4- Construire C et D sur le même graphique.
5- Résoudre graphiquement l'équation f(x) = 130. On donnera les valeurs approchées des solutions à l'unité près. »
(L'énoncé ne précise ni la situation économique ni les unités.)

---

### MATH CULTURE (p.32)

Titre de rubrique : « Math culture ». Contenu verbatim :
« Au XIXe siècle le mathématicien français Augustin Louis Cauchy définit la continuité d'une fonction sur un intervalle $[a, b]$ de la manière suivante :
« Si en partant d'une valeur x, comprise entre a et b, on attribue à la variable x un accroissement infiniment petit $\alpha$, la fonction elle-même recevra pour accroissement la différence $f(x+\alpha) - f(x)$... La fonction f est continue en x si la différence $f(x+\alpha) - f(x)$ décroît indéfiniment avec celle de $\alpha$ ». Ce ci est à comparer avec la définition moderne " f est continue en x si $\lim_{\alpha\to0} f(x+\alpha) = f(x)$ ". Mais pour arriver à cette définition, il a fallu d'abord définir d'une manière précise et opérationnelle une limite. »
Frise (colonne de droite) :
❖ « Vers 1760 Publication de l'article " limites" par Jean Laurent d'Alembert (1717 – 1783) » — portrait légendé « D'ALEMBERT (1717-1783) ».
❖ « Vers 1821 Publication du premier volume du cours d'analyse de l'école royale polytechnique où Cauchy fonde l'Analyse sur la notion de limite et de fonction continue »
Portrait légendé « Augustin Louis Cauchy 1789 - 1857 ». Texte : « Cauchy est devenu professeur à l'école polytechnique en 1814, après avoir débuté une carrière d'ingénieur des ponts et chaussées qui ne lui convenait pas. Il rédigea un cours d'analyse, dans lequel il prit comme notions fondamentaux [sic] la limite et la continuité. L'analyse moderne était née. »
Source citée : aucune (le manuel ne cite aucune référence ; seulement les noms et dates ci-dessus).

---

### VOCABULAIRE OFFICIEL DE LA SECTION (termes exacts du manuel)

- limite (à droite, à gauche, en un point, en l'infini, finie / infinie) ; « pas de conclusion » (forme indéterminée, le mot « indéterminée » n'est pas employé) ; « règle des signes »
- fonction polynôme ; fonction rationnelle ; terme de plus haut degré
- théorème des gendarmes : le terme n'apparaît pas ; le manuel dit « Limites et ordre » (encadrement par deux fonctions de même limite)
- fonction composée ($g \circ f$) ; « fonction réciproque » ou « bijection réciproque » ; « bijection de I sur f(I) »
- continue en $x_0$ ; continue à droite / à gauche ; continue sur un intervalle ; « sur chaque intervalle contenu dans son domaine de définition »
- « Théorème des valeurs intermédiaires » (titre du § III ; imprimé « Théorème des valeurs intermédiaire » dans le plan p.5) ; « Théorème de la bijection » ; « Corollaire » ; « principe de la dichotomie » ; « encadrement d'amplitude / à $10^{-n}$ près »
- image d'un intervalle par une fonction continue ; « strictement monotone » ; « coût moyen $C_M$ » ; « coût total » ; « bénéfice » ; « coût unitaire moyen » ; « prix de vente »
- notations : $\lim_{x\to x_0^+}$, $\lim_{x\to x_0^-}$, $g \circ f$ (imprimé « gof » dans un encadré), $f^{-1}$, $f(I)$, $IR$ / ℝ / $IR_+$ / $IR^*_+$, $\mathbb{N}^*$, $\Delta : y = x$, « tg » pour tangente (p.24, $A_c = n\,\mathrm{tg}\frac{\pi}{n}$)

### BORNES DE LA SECTION

INCLUS (présents dans le chapitre I) :
- limites en un point, à droite/à gauche, en $\pm\infty$ ; opérations (somme, produit, quotient) avec cas « pas de conclusion » ; limite d'un polynôme et d'une fonction rationnelle en l'infini ; limites et ordre (comparaison, encadrement, majoration ⇒ $-\infty$, minoration ⇒ $+\infty$) ; limite d'une fonction composée ; limite de $\sqrt{f}$ ; limites de référence $\frac{\sin x}{x}$, $\frac{1-\cos x}{x}$, $\frac{1-\cos x}{x^2}$
- continuité en un point, à droite, à gauche, sur un intervalle ; opérations sur les fonctions continues ; polynômes et rationnelles ; composée ; prolongement par une valeur (activité $g(x)$ avec paramètre α)
- théorème des valeurs intermédiaires, corollaire ($f(a) f(b) < 0$), image d'un intervalle par une fonction continue (strictement monotone), dichotomie, théorème de la bijection et fonction réciproque (sens de variation, courbes symétriques par rapport à $y = x$)
- applications économiques : limites d'un coût moyen, coût total par lots, bénéfice maximal / rentabilité, coût unitaire moyen

EXCLU / non traité dans les pages 5-32 :
- aucune définition $\varepsilon$-$\delta$ de la limite ; pas de forme indéterminée nommée, pas de théorème de la limite monotone ; pas de dérivation ni de dérivée de la réciproque (Chap. II) ; pas de branches infinies ni asymptotes obliques en cours (une asymptote oblique n'apparaît qu'à l'exercice 22 B3, et la « différence qui tend vers 0 » à l'activité 4 de Pour commencer) ; pas de limites par taux d'accroissement ; pas de $\ln$ / $\exp$ ; pas de corrigés.

### NOTIONS-CLÉS (≤ 8)
1. Limite en un point (à droite / à gauche) et en $\pm\infty$ ; existence ⇔ limites à droite et à gauche égales.
2. Opérations sur les limites et cas « pas de conclusion » ; polynôme/rationnelle en l'infini (terme de plus haut degré).
3. Limites et ordre : comparaison, encadrement, majoration par une fonction de limite $-\infty$ / minoration par $+\infty$.
4. Limite d'une fonction composée (et de $\sqrt{f}$ ; $\lim \frac{\sin x}{x} = 1$).
5. Continuité en un point / sur un intervalle ; opérations ; polynômes et rationnelles ; composée.
6. Théorème des valeurs intermédiaires et corollaire ($f(a)f(b) < 0$) ; image d'un intervalle ; dichotomie.
7. Théorème de la bijection, fonction réciproque, symétrie des courbes par rapport à $y = x$.
8. Interprétation économique des limites (coût moyen, coût total, bénéfice, coût unitaire moyen).

---

### § NOTES

#### Pages lues
Pages 5 à 32 : 28 pages sur 28, toutes lues à l'image (rendu 110 dpi sous `/root/.cache/yqa-manuels/render-m01/`), plus la couche texte (`pdftotext -layout`). La page 5 n'a pas de couche texte (page de titre en image) : lue à l'image seule.
Pages sondées à 170-220 dpi (zoom) : p.8 (figure f), p.14 (figures des quatre fonctions, point (0,1)), p.17 (trois graphiques), p.18 (figure activité 3), p.25 et p.26 (tableaux tableur : les 21 lignes de chiffres relues et recomptées par calcul de $\frac{n}{2}\sin\frac{2\pi}{n}$ et $n\tan\frac{\pi}{n}$ : aucun écart), p.30 (ligne $d(x)$), p.31 (graphique ex. 20).

#### Écarts couche texte / image (l'image fait foi)
- p.10 Act. 2 : la couche texte perd les valeurs absolues ($|x|$) ; à l'image : $f(x) = 2 - \frac{\cos x}{|x|}$ et encadrement $2 - \frac{1}{|x|} \le f(x) \le 2 + \frac{1}{|x|}$.
- p.12 Act. 6 : la couche texte perd $\sqrt{x}$ ; à l'image : $\frac{\sin x}{\sqrt{x}}$ et $\frac{1}{\sqrt{x}}$.
- p.13 Act. 3 : racines carrées perdues par le texte ; à l'image les trois limites portent sur $\sqrt{\cdot}$.
- p.16 Act. 2-1 : texte « x0 = 5 » ; à l'image $x_0 = \sqrt{5}$.
- p.20-21 : $f(x) = \sqrt{x^2-1} - 1$ (Act. 7), $x\sqrt{x} - x - 1$ (Act. 6), $x + \sqrt{x} - 3$ (Act. 9) : racines perdues par le texte, rétablies à l'image.
- p.29-31 : mêmes pertes de $\sqrt{\ }$ et de $|\ |$ (Ex. 10 : $\sqrt{1+x^2}$, $\sqrt{3+\cos^2 x}$, $\sin(\sqrt{x})$ ; Ex. 11-b : $\frac{1}{\sqrt{x}}$ ; Ex. 15 : $|3x^2+x-4| - 2$), rétablies à l'image.

#### Coquilles imprimées (reproduites telles quelles, signalées)
- p.5 : « Théorème des valeurs intermédiaire » (singulier) dans le plan ; le titre p.17 est « Théorème des valeurs intermédiaires ».
- p.11 Remarque : « lorsqu $x_0$ » (« lorsque » attendu).
- p.12 Act. 6 : numérotation 1), [2) absent], 3) : « En déduire … » tient lieu de 2).
- p.12 Act. 1 : « Vérifier que pour tout $x \in IR^* \setminus \{1\}$ » alors que f est définie sur $IR \setminus \{1\}$ et g sur $IR \setminus \{-1\}$ (point 0 : $g \circ f$ n'est définie qu'en $x \ne 0, 1$ ; la formule $1/x$ n'a de sens que pour $x \ne 0$ : cohérent avec $IR^*$).
- p.14 Act. 1 : « les trois fonctions f, g, h et k » (quatre listées) ; g(0) noté « f(0)=1 » (devrait être g(0)=1).
- p.17-18 : deux « Activité 3 » dans le paragraphe III (p.17 : $f(x)=3x^2-2$ ; p.18 : f de la courbe) ; la seconde ouvre le sous-titre « Cas d'une fonction continue et strictement monotone » et enchaîne avec les Activités 4 et 5 : numérotation non repartie.
- p.18 Act. 4 : « Vérifier que f(x) = … si −2 ≤ x ≤ 1/2 ; … si 1/2 < x ≤ 5 » : la vérification est correcte (recomptée : $1-2x - (x+2) = -3x - 1$ ; $2x-1-(x+2) = x - 3$).
- p.20 : Activité 6 et Activité 7 présentes avant le Corollaire ; le Corollaire (p.20) est cité « page 30 » à l'Ex. 14-2b (p.29) : renvoi erroné.
- p.22 Act. 1 : deux consignes d'ouverture (« Montrer que f est strictement croissante » sans numéro, puis 1- et 2-).
- p.23 Act. 2 figure : la figure illustre des courbes de type $\sqrt{x+1}$ / $x^2 - 1$ (point (−1, 0) et (0, −1) visibles), non $f(x) = x^2$ de l'énoncé ; figure générique de symétrie.
- p.24 : légendes inversées : « n = 12 » sous le pentagone, « n = 5 » sous le dodécagone ; « cotés » (au lieu de côtés) ; « arêtes » pour côtés ; « tg » pour tan.
- p.25 Étape 2 : formule imprimée `=(A3/2*SIN(PI()/A3))` contredit $A_i = \frac{n}{2}\sin\frac{2\pi}{n}$ et la capture p.24 `=(A3/2*SIN(2*PI()/A3))` ; la valeur affichée en B3 (= 2 pour n = 4) correspond à la version avec $2\pi$ (avec `PI()/A3`, on aurait 1,414…). À signaler aux auteurs : utiliser $2\pi/n$.
- p.25-26 : étape 5 : « on obtient le tableau suivant » ; en p.26 le second tableau ré-affiche n = 4, 10, 50 avec les mêmes valeurs ; sauts d'étapes : les lignes A3→A15 de l'étape 1 (13 lignes) correspondent bien à 13 valeurs de n (4, 10, 50, 60, …, 150).
- p.26 : légende du graphique, les deux traits de légende sont de même teinte (noire) à l'impression.
- p.28 Ex. 4 : les questions 5-c et 7-b sont identiques ($\lim_{x\to2^+}\frac{x^2-5x+6}{(x-2)^2}$).
- p.28 Ex. 3 : « Calculer les limites suivantes si elles existent » commence à la page 27 (3-1 et 3-2) et continue p.28 (3-3).
- p.29 Ex. 11-b : « g est une fonction vérifiant » puis l'encadrement et la question portent sur « f ».
- p.29 Ex. 13 : « $[1, +\infty]$ » (crochet fermant mal orienté) à deux reprises ; la majoration demandée $-\frac{1}{x} + 1 \le f(x) \le \frac{1}{x} + 1$ est conforme à l'hypothèse $0 \le u(x) \le x$ mais la borne inférieure est faible (cohérent avec la consigne).
- p.30 Ex. 19-2 : « Vérifier que $d(x) = x + \frac{x}{4}$ » : le coefficient directeur de (OM), avec $M(x, x^2+4)$, est $\frac{x^2+4}{x} = x + \frac{4}{x}$ ; l'image montre bien « x » au numérateur et « 4 » au dénominateur, donc coquille d'impression (numérateur et dénominateur inversés). L'énoncé 3) (limites en 0, $\pm\infty$) et 7) (coût unitaire moyen) sont cohérents avec $x + \frac{4}{x}$.
- p.31 Ex. 20 : x en centaines d'unités mais la graduation d'abscisse du graphique porte « 1000 » ; prix de vente d'une centaine = 13 000 dinars alors que l'axe des ordonnées va jusqu'à 10 000+ : lecture des valeurs seulement possible sur l'image.
- p.31 Ex. 22 : « On appelle Csa courbe » (espace manquant, « C sa courbe »).
- p.32 : « Ce ci » ; « notions fondamentaux » ; « Jean Laurent d'Alembert » (l'usage est « Jean Le Rond d'Alembert » : à vérifier avant reprise) ; date « 1814 » pour la chaire de Cauchy reproduite telle qu'imprimée (à ne pas reprendre sans vérification).

#### Incohérences de chiffres entre énoncé et synthèse
- p.7 Act. 5 : « C(x) = −x² + 4x si x ≤ 2000 » et x « en milliers » ; le graphique place le seuil à x = 2 (unité des abscisses = 1000 jouets), ce qui impliquerait x ≤ 2 (en milliers). Le seuil 2000 est cohérent seulement si x est le nombre d'objets, ce qui contredit « x milliers d'objets ». Les auteurs de chapitre doivent fixer l'unité (valeurs à x = 2 : −4 + 8 = 4 à gauche ; 4 + 2 − 1,8 = 4,2 à droite : saut de 0,2 milliers de dinars, calcul recompté par moi à partir des formules imprimées, non fourni par le manuel).
- p.19 Act. 5 : le bénéfice n'est pas donné par une formule ; il vaut $15p - C(p) = -p^2 + 12p - 4$ (calcul mien, cohérent avec la courbe : sommet vers p = 6, ordonnée ≈ 32 ; racines ≈ 0,35 et 11,65).

#### `[?]` justifiés
- p.18 Act. 3 figure : ordonnées des extrema de f non étiquetées ; l'image suggère environ −2 et +2, non imprimé : laissé `[?]`.
- p.17 Act. 1 graphique 3 : graduations imprimées irrégulières (le zéro étiqueté « 2 ») ; lecture exacte des extrema impossible sans hypothèse : laissé `[?]`.
- p.20 illustration « solutions multiples » : positions de $x_0$, $x_1$ non données par des valeurs.
Aucun `[?]` ne touche une formule, un tableau chiffré ou un énoncé.

#### Remarque de structure
Le chapitre ne contient pas de rubrique « Revoir » unique : le cours commence directement par « LIMITES » (I- Revoir ; II- Limites et ordre ; III- Limite d'une fonction composée) puis « CONTINUITE » (I- Revoir ; II- Continuité d'une fonction composée ; III- Théorème des valeurs intermédiaires ; IV- Théorème de la bijection). Aucun exemple résolu complet dans les pages 5-32 : le manuel ne fournit pas de corrigé et pas d'« exemple résolu ». La rubrique « Avec l'ordinateur » occupe les pp. 24-26 ; « Exercices et problèmes » pp. 27-31 (exercices 1 à 22) ; « Math culture » p. 32.

---

### Chapitre `m02-p33-62`

### m02 — Chapitre II « Dérivation - Primitives » (manuel CNP 222463P00, pp. 33-62)

Source : manuel officiel « Mathématiques », 4ᵉ année secondaire, section économie et gestion (CNP). Page PDF = page imprimée. Lecture : texte + image de chaque page.

#### p.33 — Page de titre
Chapitre 2 — DERIVATION - PRIMITIVES. Plan imprimé :
- Pour commencer
- Dérivation : Revoir ; Dérivée seconde et point d'inflexion ; Dérivée d'une fonction composée ; Dérivée de la fonction réciproque ; Théorème des accroissements finis
- Primitives : Notion de primitive ; Ensemble des primitives d'une même fonction ; Calculs sur les primitives
- Avec l'ordinateur ; Exercices et problèmes ; Math culture

#### POUR COMMENCER (pp. 34-35, bandeau « Cours » imprimé en tête de page)

##### Activité 1 (p.34) — QCM de prérequis
Consigne : « Pour chacune des questions ci-dessous, une seule des réponses proposées est exacte. On demande de cocher cette réponse. » Tableau QUESTIONS / REPONSES (10 questions, une seule réponse exacte, cases à cocher) :
1. (O, i⃗, j⃗) repère du plan, A(1,−1) et B(0,2) deux points. La droite (AB) a pour équation : ☐ y = 2 ; ☐ 3x + y − 2 = 0 ; ☐ x − y = 2
2. (o, i⃗, j⃗) repère du plan, D : y = −3x + 2. Le coefficient directeur D est égal à : ☐ −3/2 ; ☐ 2 ; ☐ −3
3. (o, i⃗, j⃗) repère du plan, D : y = −3x + 2 ; D' : 3x + y = 2. D et D' sont : ☐ parallèles ; ☐ sécantes
4. (o, i⃗, j⃗) repère orthonormé du plan, A(1,−1) et B(3,−1). La pente de la droite (AB) est égale à : ☐ 3 ; ☐ 0 ; ☐ −1
5. f : x ↦ x ; le nombre derivé de f en un point x₀ de IR est égal à : ☐ x₀ ; ☐ 1 ; ☐ 0
6. f : x ↦ a ; le nombre derivé de f en un point x₀ de IR est égal à : ☐ 0 ; ☐ a ; ☐ 1
7. f : x ↦ x³ ; le nombre derivé de f en un point x₀ de IR est égal à : ☐ x₀² ; ☐ 3 ; ☐ 3x₀²
8. f : x ↦ 1/x ; le nombre derivé de f en un point x₀ de IR* est égal à : ☐ −1/x₀² ; ☐ 1/x₀ ; ☐ 1
9. f : x ↦ √x ; le nombre derivé de f en un point x₀ de IR*₊ est égal à : ☐ √x₀ ; ☐ √1 ; ☐ 1/(2√x₀)
10. f : x ↦ (1/2)x² ; le nombre derivé de f en un point x₀ de IR est égal à : ☐ x₀ ; ☐ 1/2 ; ☐ 2x₀
(Aucun corrigé dans le manuel. [R7 : les numéros 1 à 10 sont ajoutés par le lecteur ; le manuel n'imprime aucun numéro de question dans ce tableau.] Le tableau est imprimé sur deux colonnes de questions : colonne gauche = questions 1-5 dans l'ordre 1,2,3,4,5 (droites puis f:x↦x), colonne droite = 6-10 (f:x↦a, x³, 1/x, √x, ½x²).)

##### Activité 2 (p.34) — Coût marginal
Situation : « Une usine fabrique des objets dont le nombre varie de 0 à 40. Le coût total de fabrication exprimé en dinars, de x quantités est modélisé par la fonction C définie par : C(x) = (1/3)x³ − 15x² + 200x »
Encadré : « Le coût marginal Cm est la dépense occasionnée par la production d'un objet supplémentaire et on suppose que Cm(x) = C'(x) »
Questions verbatim :
1- Calculer le coût marginal en fonction de x
2- A combien s'élève-t-il pour 10 unités ? et pour 30 unités ?
3- Pour quelle valeur de x ce coût marginal est-il minimal ?
(Pas de corrigé imprimé.)

##### Activité 3 (p.35) — Lecture graphique du coût marginal
Énoncé : « La courbe C ci-dessous représente le coût total de production d'un produit en fonction de la quantité x produite (x est exprimé en kg et le coût total en dinars). »
Figure : courbe C rose partant de l'origine (repère : unités 10 sur l'axe des x, 100 sur l'axe des y), croissante, avec une portion quasi horizontale (tangente horizontale/aplatie vers le milieu, flèches de tangente bleues), un point d'inflexion visible (tangente bleue qui traverse la courbe vers la droite du graphique), puis une branche à pente très forte tendant vers la verticale à droite ; une droite pointillée noire part de l'origine vers le point de la courbe. 
Travail demandé verbatim : « Parmi les représentations ci-dessous, une correspond au coût marginal associé à la production du produit. Laquelle ? Justifier la réponse. »
Quatre représentations proposées (repères avec graduations 2 sur y, 40 et 90 sur x) : (a) droite croissante d'ordonnée à l'origine 2 ; (b) courbe décroissante de 2 jusqu'à un minimum (≈0 vers x=40) puis croissante (en U asymétrique, croissant ensuite linéairement vers la droite) ; (c) arche concave croissante puis décroissante partant de 2 ; (d) droite horizontale à y = 2.
(Pas de réponse imprimée ; l'image seule ne permet pas de lire les graduations de la courbe C avec précision — [?] sur les valeurs exactes.)

#### LE COURS — DERIVATION (pp. 36-…)

##### I- Revoir
###### 1) Dérivabilité en un point (p.36)
**Activité 1** — Soit f la fonction définie, sur ]0,+∞[, par : f(x) = x + 1/x
1) Calculer f(1).
2) Vérifier que pour tout x ∈ ]0,+∞[ \ {1} on a : (f(x) − f(1))/(x − 1) = 1 − 1/x . En déduire que f est dérivable en 1 et que f'(1)=0.
3) Soit x₀ un élément de ]0,+∞[ et x ∈ ]0,+∞[ \ {x₀}, vérifier que : (f(x) − f(x₀))/(x − x₀) = 1 − 1/(x x₀).
4) En déduire que f est dérivable en x₀ et que f'(x₀) = 1 − 1/x₀².

**Encadré (définition)** : « On dit que f est dérivable en x₀ si et seulement si il existe un réel ℓ tel que : lim_{x→x₀} (f(x) − f(x₀))/(x − x₀) = ℓ . ℓ est appelé le **nombre dérivé** de f en x₀ et on note f '(x₀) = ℓ »

**Encadré (dérivabilité à droite / à gauche)** :
« 1) On dit que f est dérivable à droite en x₀ si et seulement si il existe un réel ℓ tel que lim_{x→x₀⁺} (f(x) − f(x₀))/(x − x₀) = ℓ . ℓ est appelé **nombre dérivé à droite** de f en x₀ et on note f'_d(x₀) = ℓ
2) On dit que f est dérivable à gauche en x₀ si et seulement si il existe un réel ℓ tel que lim_{x→x₀⁻} (f(x) − f(x₀))/(x − x₀) = ℓ . ℓ est appelé **nombre dérivé à gauche** de f en x₀ et on note f'_g(x₀) = ℓ »

**Encadré (propriétés)** : « 1) f est dérivable en x₀ si et seulement si f est dérivable à **droite** et à **gauche** en x₀ et f'_d(x₀) = f'_g(x₀) . 2) Si f est dérivable en x₀ alors f est continue en x₀ . »

**Activité 2** — Soit f la fonction définie, sur ℝ par f(x) = |x| − 1.
1- Etudier la continuité de f en 0 et en -1.
2- Montrer que f est dérivable en -1 et calculer f '(-1).
3- Etudier la dérivabilité de f en 0.

**Activité 3** — Soit la fonction f : x ↦ { 2x² − 1 si x ≤ −1 ; x + 2 si x > −1 }
1- Etudier la continuité de f en -1.
2- Vérifier que f est dérivable à droite et à gauche en -1. f est-elle dérivable en -1 ?

**Activité 4** — Soit f la fonction définie, sur ℝ par { f(x) = |x − 1| − x si x > 0 ; f(x) = −2x + 2 si x ≤ 0 }
1) Etudier la dérivabilité de f en 0 et en 1.
2) La fonction f est-elle continue en 0 ? et en 1 ?
(Le manuel imprime « .. » après l'accolade ; sans effet.)

**Remarque** : « La fonction f peut être continue en un point sans être dérivable en ce point. »

###### 2) Interprétation graphique du nombre dérivé (p.37)
**Activité 1** — « Soit f la fonction représentée graphiquement ci-contre : »
1- Préciser le domaine de définition de f.
2- Déterminer : a − f(−2) et f '(−2). b − f(−1) et f '(−1).
3- Déterminer f '(5/2) et donner une équation cartésienne de la tangente à la courbe de f au point d'abscisse 5/2.
Figure : courbe rose sur repère à quadrillage (unité 1) avec trois tangentes bleues : horizontale au creux près de x=−2 (marquée « −2 »), horizontale au sommet local près de x=−1, et une tangente fortement inclinée vers le bas à droite (après le maximum, au voisinage de x = 5/2). La courbe n'est lisible qu'à l'estimation : [?] pour les valeurs exactes (le domaine, f(−2), f(−1)).

**Encadré (tangente)** : « Si f est une fonction dérivable en x₀ alors sa courbe représentative admet au point d'abscisse x₀ une tangente d'équation: y = f '(x₀)(x − x₀) + f(x₀) . »

**Remarques** (verbatim) :
1) Si f est dérivable en x₀ et f'(x₀)=0 alors la tangente à la courbe représentative de f au point d'abscisse x₀ est parallèle à l'axe des abscisses.
2) - Si f est dérivable à droite en x₀ alors sa courbe représentative admet au point d'abscisse x₀ une demi tangente d'équation : { y = f'_d(x₀)(x − x₀) + f(x₀) ; x ≥ x₀ }
 - Si f est dérivable à gauche en x₀ alors sa courbe représentative admet au point d'abscisse x₀ une demi tangente d'équation : { y = f'_g(x₀)(x − x₀) + f(x₀) ; x ≤ x₀ } (le manuel termine par « : »)
3) Si la limite de (f(x) − f(x₀))/(x − x₀) est infinie lorsque x tend vers x₀⁺ ou x tend vers x₀⁻ alors la courbe représentative de f admet au point d'abscisse x₀ une demi tangente parallèle à l'axe des ordonnées.
4) Si la courbe représentative de f admet en un point M deux demi tangentes de directions différentes, alors M est dit : **un point anguleux.**

**Activité 2** — « Soit g la fonction dont la courbe représentative dans un repère orthonormé est donnée dans le graphique ci contre. Donner les équations des tangentes ou des demi tangentes à Cg aux points d'abscisses 5/2, 2 et -3. »
Figure : courbe rose (repère orthonormé, unité 1) ; tangente bleue inclinée ascendante à gauche (x≈−3), tangente horizontale en haut vers x≈1-2, demi-tangentes (bleu) vers x≈2 puis tangente horizontale au creux vers x≈5/2 ; point anguleux visible vers x=2. Valeurs lues à l'estimation uniquement : [?].

###### 3) Dérivabilité sur un intervalle – fonction dérivée (p.38)
**Activité 1** — Soit f la fonction définie sur ]0,+∞[, par : f(x) = x + √x
1- Soit x₀ un élément de ]0,+∞[ et x ∈ ]0,+∞[ \ {x₀} vérifier que : (f(x) − f(x₀))/(x − x₀) = 1 + 1/(√x + √x₀).
2- En déduire que f est dérivable en tout point x₀ de ]0,+∞[ et que f '(x₀) = 1 + 1/(2√x₀).

**Encadré (dérivabilité sur un intervalle)** : « Soit f une fonction a variable réelle.
1- On dit que f est dérivable sur un intervalle ]a,b[ lorsque f est dérivable en tout réel de ]a,b[.
2- On dit que f est dérivable sur [a,b[ lorsque f est dérivable sur ]a,b[ et f est dérivable à droite en a
3- On dit que f est dérivable sur ]a,b] lorsque f est dérivable sur ]a,b[ et f est dérivable à gauche en b
4- On dit que f est dérivable sur [a,b] lorsque f est dérivable sur ]a,b[, dérivable à droite en a et à gauche en b
(a et b peuvent être finis ou infinis) »

**Commentaire** : « - La fonction f est dérivable en tout point de ]0,+∞[, on dira que f est dérivable sur l'intervalle ]0,+∞[. - La fonction f ' est définie sur ]0,+∞[ par : f '(x) = 1 + 1/(2√x) »

**Encadré (fonction dérivée)** : « Si f est dérivable sur un intervalle I, la fonction qui à chaque réel x de I associe f '(x) est appelée la fonction dérivée de f. »

###### 4) Opérations sur les fonctions dérivables (p.38)
**Activité 3** — « Dans chacun des cas suivants étudier la dérivabilité de la fonction f sur l'intervalle I et définir sa fonction dérivée : »
a − f : x ↦ x + √x ; I = ]0,+∞[
b − f : x ↦ x²√x − 1 ; I = ]0,+∞[  (radical sur x seul, « −1 » hors radical, vérifié à 200 dpi)
c − f : x ↦ 2(x³ − x)√x ; I = ]0,+∞[
d − f : x ↦ x² − 1 ; I = IR  (pas de radical, vérifié à 200 dpi)
e − f : x ↦ 1/(x³ − 8) ; I = ]2,+∞[
f − f : x ↦ x − 2 + 1/(x − 1) ; I = ]1,+∞[
g − f : x ↦ (x + 1)/(x² + 3) ; I = IR

**Encadré (opérations)** : « f et g sont deux fonctions dérivables sur un intervalle I et α un réel fixé. On a :
La fonction f+g est dérivable sur I et (f+g)'=f '+g'
La fonction α f est dérivable sur I et (α f)' = α f '
La fonction f.g est dérivable sur I et (f.g)' = f '.g + f.g'
Si de plus f ne s'annule pas sur I Alors :
* La fonction 1/f est dérivable sur I et (1/f)' = − f'/f²
* La fonction g/f est dérivable sur I et (g/f)' = (g'f − gf')/f² »
**Encadré** : « Toute fonction polynôme est dérivable sur IR. Toute fonction rationnelle est dérivable sur chaque intervalle contenu dans son domaine de définition. »

###### 5) Sens de variation et signe de la dérivée (p.39)
**Activité 1** — 1) « On donne sur les graphiques suivants, les courbes représentatives des fonctions f et sa dérivée f '. Préciser le signe de f' et le sens de variation de la fonction f sur chacun des intervalles I = ]−2,0[, J = ]0,1[ et K = ]1,3[. »
Figures : à gauche la courbe Cf' (repère gradué −2…+3 en x ; −4…+7 en y) : décroissante convexe de (−2, ≈6-7) jusqu'à (0, ≈1) [ordonnée 1 en 0], puis segment sur l'axe (f'=0) de 0 à 1, puis segment droit croissant de (1, −4) à (3, ≈0) [pente 2 ; extrémité gauche ouverte]. À droite la courbe Cf (x de −2 à 3) : croissante de (−2, −5) à (0, 1), palier à 1 entre 0 et 1, puis décroissante jusqu'à (3, −3).
2) « Dans le cas suivant, donner le tableau de signe de f'(x) puis déterminer le sens de variation de f. »
Figure : courbe Cf' (repère unité 1) en forme d'ondulations, touchant l'axe des abscisses en x₁ (à gauche de 0), en 0 et en x₂ (à droite), avec deux bosses positives entre ces zéros. Valeurs de x₁, x₂ : [?] (non graduées, lecture graphique seulement).

**Activité 2** — « Soit f une fonction définie sur [−6,6] et ayant pour représentation graphique la courbe ci-dessous. Déterminer le signe de f'(x) pour tout x de ]−6,6[. »
Figure : courbe de f avec tangentes horizontales (bleues) au maximum local vers x≈−4, au minimum local vers x≈−1/0, au maximum local vers x≈3 ; tangente verticale (flèche vers le haut) à l'extrémité droite x=6.

**Encadré (sens de variation)** : « Soit f une fonction dérivable sur un intervalle I de ℝ.
- f est croissante sur I si et seulement si f '(x) ≥ 0 pour tout x de I .
- f est décroissante sur I si et seulement si f '(x) ≤ 0 pour tout x de I .
- f est constante sur I si et seulement si f '(x) = 0 pour tout x de I »

###### 5) (suite, p.40)
**Activité 4** — « On donne le tableau de variation suivant : Parmi les représentations graphiques ci-dessous, quelle est la courbe susceptible de représenter la fonction f ? »
Tableau de variation (transcrit à l'image) : x : −5 | 1 | 3 | 7 ; f'(x) : + sur ]−5,1[, 0 en x=1, − sur ]1,3[, double barre en x=3 (f' non définie), + sur ]3,7[ ; f(x) : −2 ↗ 4 (en x=1) ↘ −2 (en x=3) ↗ 4 (en x=7).
Trois courbes proposées (repère unité 1) : (1) courbe avec minimum horizontal à gauche, maximum horizontal en x≈0, minimum horizontal en x≈2 ; (2) courbe croissante, maximum horizontal vers x=1, descente, minimum horizontal (arrondi) vers x=2-3, remontée ; (3) même début, maximum horizontal vers x=1, descente verticale en pointe (point anguleux, demi-tangentes) vers x≈3 puis remontée.
(La 3ᵉ est la seule à présenter un point anguleux, compatible avec la double barre de f' en 3 ; le manuel ne donne pas la réponse — ne pas l'affirmer comme corrigé.)

**Activité 5** — « Dresser le tableau de variation de chacune des fonctions suivantes : »
a) f : x ↦ x − 1/x ; b) f : x ↦ 3x⁴ − 2x² + 1 ; c) h : x ↦ 4/(x² − 2x) ; d) g : x ↦ (x² + 4x + 1)/(x + 1)

**Activité 6** — « On donne dans la figure ci-contre la représentation graphique d'une fonction f. Déterminer les extremums de f sur [−5, 6] »
Figure : courbe avec tangentes horizontales (bleues) au minimum local vers x≈−4, maximum local vers x≈−2, minimum local vers x≈3 ; branche croissante raide vers la droite jusqu'à x=6 ; repère unité 1. Valeurs exactes : [?] (non graduées par le manuel, à lire sur quadrillage).

###### p.41 — Activité 7 (fin du « Revoir ») — Coût moyen et bénéfice
Situation : « Un artisan fabrique des objets en verre. Pour chaque semaine, il estime que le coût de production en dinars de x objets est modélisé par : C(x) = x² + 60x + 121 pour x ∈ [1;30]. Le coût moyen de production est défini par Cm(x) = C(x)/x . »
1- Calculer la dérivée C'm de Cm.
2- Etudier le signe de C'm et dresser le tableau de variation de Cm.
3- En déduire le nombre d'objets à fabriquer pour obtenir un coût moyen minimal.
4- Chaque objet est vendu à 110 d.
 a- Montrer que le bénéfice réalisé par la vente de x objets est donné par B(x) = −x² + 50x − 121.
 b- Etudier le signe de B'(x) et dresser le tableau de variation de B.
 c- En déduire le nombre d'objets à vendre pour obtenir un bénéfice maximal.
(Vérification arithmétique sans prétendre corrigé : B(x) = 110x − C(x) = −x² + 50x − 121, cohérent avec l'énoncé.)
**Encadré (extremum relatif)** : « Soit f une fonction dérivable sur un intervalle ouvert I contenant x₀. 1- Si f admet un extremum relatif en x₀ alors f '(x₀) = 0 . 2- Si f ' s'annule en x₀ en changeant de signe alors f(x₀) est un extremum relatif de f. »

##### II- Dérivée seconde et point d'inflexion (pp. 41-42)
**Activité 1** — f est la fonction définie sur ℝ par f(x) = x³ − 3x² + 1
1- Montrer que f est dérivable sur ℝ et déterminer sa fonction dérivée f '
2- Montrer que f ' est dérivable sur ℝ et déterminer sa fonction dérivée qu'on notera f''.

**Définition (encadré)** : « Soit f une fonction dérivable sur un intervalle I. Si sa fonction dérivée f ' est dérivable sur I, on dira que f est deux fois dérivable sur I et la fonction dérivée de f ' notée f '' est appelée fonction dérivée seconde de f sur I. »

**Activité 2** — « Soit f la fonction définie sur IR par f(x) = 2x³ + x − 1. On désigne par Cf sa courbe représentative dans un repère (O, i⃗, j⃗). »
1- Montrer que f est deux fois dérivable sur IR et déterminer les expressions de f ' et de f ''
2- Déterminer une équation cartésienne de la tangente T à Cf au point d'abscisse nulle.
3- Etudier les positions de Cf par rapport à T.
4- Dresser le tableau de signe de la fonction f ''.
Figure : Cf (rose) et la droite T qui la traverse en (0,−1) ; graduations −1, +1, +2 en x et −1, −2, −3 en y.

**Interprétation** : « Dans le cas de l'activité précédente, la tangente T traverse la courbe Cf au point d'abscisse nulle, on dira que A(0, -1) est un point d'inflexion de Cf. »

**Théorème (admis)** : « Soit f une fonction deux fois dérivable sur un intervalle ouvert I contenant x₀. Si f '' s'annule et change de signe en x₀, alors M(x₀, f(x₀)) est un point d'inflexion de la courbe représentative de f. » (imprimé avec « f " »)

**Activité 3 (p.42)** — « Soit f la fonction définie sur ℝ par : f(x) = (1/20)x⁵ − (1/6)x³ + 2. On désigne par Cf sa courbe représentative dans un repère (O, i⃗, j⃗). Montrer que la courbe représentative de f admet trois points d'inflexion que l'on déterminera. »

**Activité 4** — « On considère la fonction f définie sur IR* par f(x) = 1 − 1/x + 1/x² et on désigne par Cf sa courbe représentative dans un repère (O, i⃗, j⃗). Montrer que f est deux fois dérivable sur IR* et que sa courbe représentative Cf admet un point d'inflexion I dont-on donnera les coordonnées. »

**Activité 5** — « f est la fonction définie sur IR par f(x) = { √x si x ≥ 0 ; −√(−x) si x < 0 } et C sa courbe représentative dans un repère orthonormé (O, i⃗, j⃗). »
1- Etudier la dérivabilité de f en 0. Interpréter graphiquement le résultat.
2- Prouver que la tangente en O traverse la courbe C.
3- En déduire que O est un point d'inflexion de C

##### III- Dérivée d'une fonction composée (pp. 42-43)
**Activité 1 (p.42)** — « On considère les fonctions f, g et h définies sur IR₊ par : f(x) = 1/(1 + √x) ; g(x) = 1/(1 + x) et h(x) = √x »
1- Vérifier que : f = g ∘ h
1- Déterminer les fonctions dérivées de f, g et h   (numérotation imprimée « 1- » deux fois ; voir § Notes)
2- Comparer f '(x) et g '[h(x)].h '(x) pour x ∈ IR*₊.

**Théorème (admis, p.43)** : « Si f est une fonction dérivable sur un intervalle I et g est une fonction dérivable sur un intervalle J contenant f(I). Alors la fonction (g o f) est dérivable sur I, et pour tout x de I : (g o f)'(x) = g'(f(x)) × f '(x) »

**Activité 2** — « Soit f la fonction définie sur ]1,+∞[ par f(x) = (2x − 3)/(x − 1). »
1- Calculer f '(x) pour x ∈ ]1,+∞[.
2- Déduire la dérivée de la fonction g : x ↦ (2x² − 3)/(x² − 1).
3- Soit h la fonction définie sur ]1,+∞[ par h(x) = f(√x). Calculer h '(x) pour x ∈ ]1,+∞[.

**Conséquences (verbatim)** :
1) Soient f une fonction dérivable sur un intervalle I et n un entier relatif. fⁿ est dérivable :
 - En tout point de I lorsque n ≥ 2.
 - En tout point de I où f ne s'annule pas lorsque n ≤ −1.
 Et dans les deux cas on a : (fⁿ)' = n . fⁿ⁻¹ . f '
2) Si f est dérivable sur un intervalle ouvert I et f(x) > 0 pour tout x de I, alors la fonction √f est dérivable sur I et (√f)' = f '/(2√f).

**Activité 2 (deuxième du même nom, p.43)** — « Dans chacun des cas suivants étudier la dérivabilité de la fonction f sur l'intervalle I et donner l'expression de sa fonction dérivée : »
a) f(x) = ((2x − 1)/(x² + 2))³ ; I = ℝ
b) f(x) = 1/(x − 1)⁵ ; I = ]1,+∞[
c) f(x) = √(5x − 3) ; I = ]5/3,+∞[
d) f(x) = √((2x − 1)/(x² + 2)) ; I = ]1/2,+∞[

##### IV- Dérivée de la fonction réciproque (pp. 43-44)
**Activité 1 (p.43)** — « Soit f la fonction représentée par le graphique ci-contre. »
1- Vérifier que f réalise une bijection de [1,10] sur un intervalle J que l'on précisera.
2- Représenter la courbe de la fonction f⁻¹
3- Déterminer graphiquement l'intervalle sur lequel f⁻¹ est dérivable.
Figure : courbe croissante (repère unité 1), tangente horizontale au point de départ (x=1), un palier à tangente horizontale vers x≈5, puis une montée à tangente verticale à l'extrémité droite (x=10) ; ordonnées exactes [?] (non graduées finement).

**Activité 2 (p.44)** — « Soit la fonction f définie sur [0,+∞[ par : f(x) = x² − 1. »
1- Montrer que f est une bijection de [0,+∞[ sur un intervalle J que l'on déterminera.
2- Vérifier que pour tout x de J, f⁻¹(x) = √(x + 1).
3- Montrer que f⁻¹ est dérivable sur ]−1,+∞[ et calculer (f⁻¹)'(x).
4- Vérifier que pour tout x de ]−1,+∞[, (f⁻¹)'(x) = 1 / f '(f⁻¹(x)).

**Théorème (admis)** : « Soit f une fonction continue et strictement monotone sur un intervalle ouvert I contenant x₀. **Si** f est dérivable en x₀ et f '(x₀) ≠ 0 **alors** la fonction réciproque f⁻¹ est dérivable en y₀ = f(x₀) et on a : (f⁻¹)'(y₀) = 1/f '(x₀). »

**Remarque** : « Dans les conditions du théorème, si la fonction f⁻¹ est dérivable sur un intervalle J (J ⊂ f(I)) alors pour tout x de J on a (f⁻¹)'(x) = 1 / f '(f⁻¹(x)). »

**Activité 3 (p.44, première)** — « Soit la fonction f définie sur [−2,+∞[ par f(x) = x² + 4x + 5. »
1- Montrer que f réalise une bijection de [−2,+∞[ sur [1,+∞[.
3- Déterminer l'intervalle sur lequel f⁻¹ est dérivable et calculer (f⁻¹)'(x).
2- Expliciter f⁻¹(x) pour x dans [1,+∞[ et retrouver (f⁻¹)'(x).
(Ordre des questions imprimé 1, 3, 2.)

**Activité 3 (p.44, seconde du même numéro)** — « On donne dans le graphique ci-contre la courbe représentative d'une fonction f définie sur IR et telle que lim_{x→+∞} f(x) = 3 et lim_{x→−∞} f(x) = −∞ »
1- Prouver que f réalise une bijection de IR sur un intervalle J que l'on déterminera.
2- Construire dans le même repère la courbe de la fonction f⁻¹.
3- A l'aide du graphique, justifier que f⁻¹ est dérivable en tout point de J \ {1}.
Figure : courbe croissante (repère unité 1) avec tangente horizontale vers x≈−1/0 (point de la courbe d'ordonnée voisine de 1), puis tangente verticale vers x≈2 (montée raide), puis plateau vers 3. Coordonnées exactes : [?].

**Activité 4 (p.45)** — « Soit f : [0, π] → [−1,1], x ↦ cos x »
1- Montrer que f est une bijection.
2- Calculer les antécédents de 0, 1, −1, 1/2, et √3/2 par f⁻¹.
3- Tracer les courbes représentatives de f et de f⁻¹ dans un même repère orthonormé (O, i⃗, j⃗).
4- Préciser l'ensemble sur lequel f⁻¹ est dérivable et expliciter (f⁻¹)'(x).
**Encadré (rappel)** : « Les fonctions **sinus** et **cosinus** sont dérivables sur ℝ et pour tout réel x on a : sin '(x) = cos(x) et cos '(x) = − sin(x) »

##### V- Théorème des accroissements finis (pp. 45-47)
###### 1) Théorème des accroissements finis (p.45)
**Activité 1** — « Soit f la fonction définie sur [−1,2] par f(x) = −x² + 2x. On donne dans le graphique suivant la représentation de f. Soient A et B les points de Cf d'abscisses respectives -1 et 2 »
1- Calculer le coefficient directeur de la droite (AB).
2- Déterminer les points de C en lesquels la tangente est parallèle à la droite (AB).
Figure : parabole Cf (sommet en (1,1)), points A (−1, ≈−3) et B (2, 0), droite (AB) bleue ; graduations −1, +1, +2.
**Théorème (admis)** : « Soit f une fonction définie sur un intervalle [a ; b]. **Si** (f est continue sur [a,b] **et** f est dérivable sur ]a,b[) **Alors** (Il existe au moins un élément c de ]a ; b[ tel que f '(c) = (f(b) − f(a))/(b − a)). »

**Activité 2** — « Soit f la fonction définie sur [0,4] par f(x) = x²√x − x² »
1- Montrer que f est continue sur [0,4] et qu'elle est dérivable sur ]0,4[.
2- Montrer qu'il existe un réel c de ]0,4[ tel que f '(c) = 4.

**Remarques** (verbatim) :
1- Lorsque les conditions sont remplies, le théorème affirme l'existence d'au moins une tangente à Cf parallèle à la droite (AB) où A et B sont les points de Cf d'abscisses respectives a et b.
2- Le théorème affirme l'existence de c et non pas son unicité (voir la figure ci-contre).
Figure : courbe à deux bosses sur [a,b], points a et b, droite (AB) bleue, trois points c₀, c₁, c₃ où la tangente est parallèle à (AB) (tangentes bleues parallèles).

###### p.46 — suite
**Activité 3** —
1) Soit f la fonction définie sur IR par f(x) = x⁴ − 2x² − 4x + 2.
 a- Montrer que f est dérivable sur IR et déterminer sa fonction dérivée.
 b- Calculer f(0) et f(2).
 c- En appliquant le théorème des accroissements finis, déduire que l'équation x³ − x − 1 = 0 admet au moins une solution x₀ dans l'intervalle ]0,2[.
2) Soit f une fonction définie et continue sur un intervalle [a ; b] et dérivable sur ]a,b[. Montrer que si f(a) = f(b) alors il existe au moins une tangente à la courbe représentative de f qui soit parallèle à l'axe des abscisses.

###### 2) Inégalités des accroissements finis (p.46)
**Activité 1** — « Soit la fonction f définie sur [1,3] par : f(x) = √x »
1- Montrer que f est continue sur [1,3] et qu'elle est dérivable sur ]1,3[.
2- Montrer que pour tout x dans ]1,3[ on a : √3/6 ≤ f '(x) ≤ 1/2.
3- Vérifier que : √3/6 ≤ (f(3) − f(1))/(3 − 1) ≤ 1/2.
**Théorème (admis)** : « Soit f une fonction définie et continue sur un intervalle [a ; b] et dérivable sur ]a,b[. S'il existe deux réels m et M tels que: pour tout x de ]a ; b[, m ≤ f '(x) ≤ M, alors on a m ≤ (f(b) − f(a))/(b − a) ≤ M »

**Activité 2** — « Soit la fonction : f : x ↦ (x + 2)³ définie sur [0, 1/2]. »
1- Démontrer que : pour tout x dans ]0, 1/2[ on a : 12 ≤ f '(x) ≤ 75/4.
2- Montrer que pour tout x dans [0, 1/2] ; 12x ≤ f(x) − 8 ≤ (75/4)x.
3- En déduire un encadrement de (2,01)³ à 10⁻¹ près.

**Corollaire (encadré)** : « Soit f une fonction dérivable sur un intervalle I. S'il existe un nombre réel positif k tel que : pour tout élément x de I on a : |f '(x)| ≤ k Alors, quels que soient les réels a et b de I, |f(b) − f(a)| ≤ k|b − a| »

###### p.47
**Activité 3** — « Soit la fonction g définie sur ]0,+∞[ par : g(x) = 1 + 1/√x. »
1- Montrer que l'équation g(x) = x admet une unique solution α dans l'intervalle ]0,+∞[. Vérifier que α ∈ [1,2].
2- Montrer que pour tout x de ]1,+∞[ on a |g '(x)| ≤ 1/2.
3- En déduire que pour tout réel x de ]1,+∞[, on a |g(x) − α| ≤ (1/2)|x − α|.

#### PRIMITIVES (pp. 47-…)
##### I- Notion de primitive (p.47)
**Activité 1** — Situation : « Une entreprise fabrique un certain produit en quantité x (x ∈ [0 ; 500]). Les coûts fixes s'élèvent à 6000 DT. On suppose que le coût marginal (en DT) est donnée par: g(x) = 2x + 45. »
1- Quelle est l'expression du coût total en fonction de x ?
2- Pour 200 unités produites, trouver une relation entre le coût marginal, le coût de la dernière unité produite et le coût d'une unité supplémentaire.
(Pas de corrigé imprimé.)

**Activité 2** — « Soient f et F les fonctions définies sur ]0,+∞[ par f(x) = 1/(2√x) + 3x² et F(x) = √x + x³ − 1. Vérifier que F est dérivable sur ]0,+∞[ et que F'(x) = f(x). »

**Définition (encadré)** : « Soient f et F deux fonctions définies sur un même intervalle I. On dit que F est une primitive de f sur I, si F est **dérivable** sur I et pour tout x ∈ I, **F'(x) = f(x)**. »

**Activité 3** — « Dans chacun des cas suivants vérifier que F est une primitive de f sur l'intervalle I. »
a) f : x ↦ x³ − 2 ; F : x ↦ (1/4)x⁴ − 2x − 1 ; I = IR
b) f : x ↦ 3/x² + 2x + 1 ; F : x ↦ −3/x + x² + x ; I = ]−∞,0[
c) f : x ↦ 1/(2√x) + x² ; F : x ↦ √x − (1/3)x³ + √2 ; I = ]0,+∞[
(Coquille : en c), la dérivée de F est 1/(2√x) − x², non 1/(2√x) + x² ; voir § Notes.)

###### p.48
**Théorème (admis)** : « Toute fonction continue sur un intervalle I admet une primitive sur I. »
**Activité 4** — 1- Justifier que la fonction f : x ↦ 1/x admet une primitive F sur ]0,+∞[. 2- donner le sens de variation de F sur l'intervalle ]0,+∞[.
**Remarques** : « Le théorème précédent affirme l'existence d'une primitive d'une fonction continue sur un intervalle sans pour autant la déterminer. »

##### II- Ensemble des primitives d'une même fonction (p.48)
**Activité 1** — « Soit f la fonction définie sur IR par f(x) = 2x/(x² + 1)². »
1- Montrer que f admet une primitive sur IR.
2- Vérifier que les fonctions F et G définies sur IR par : F(x) = −1/(x² + 1) et G(x) = (2x² + 1)/(x² + 1) sont deux primitives de f sur IR.
3- Calculer F(x) – G(x) pour x ∈ IR.
(Vérification : G(x) = 2 − 1/(x²+1), donc G − F = 2 ; F(x) − G(x) = −2 ; cohérent.)

**Activité 2** — « Soient f une fonction continue sur un intervalle I et F une primitive de f sur I. »
1- Montrer que pour tout réel k la fonction G : x ↦ F(x) + k est aussi une primitive de f sur I.
2- Montrer que si H est une primitive de f sur I alors la fonction (H-F) est constante sur I.

**Théorème (admis)** : « Soit f une fonction qui admet une primitive F sur un intervalle I. 1- Toute fonction G définie sur I par G(x) = F(x) + k où k est un réel, est une primitive de f sur I. 2- Toute primitive de f sur I est de la forme : x ↦ F(x) + k où k est un réel. »
**Remarque** : « Deux primitives d'une fonction sur un même intervalle diffèrent d'une constante. »

###### p.49
**Activité 3** — « Soit f la fonction définie sur ]0,+∞[ par f(x) = 2/x² + 1/√x. »
1- Montrer que f admet une primitive sur ]0,+∞[.
2- Vérifier que pour tout réel k, la fonction définie sur ]0,+∞[ par Fk(x) = −2/x + 2√x + k est une primitive de f sur ]0,+∞[.
3- Déterminer k pour que Fk(1) = 2.
**Théorème (admis)** : « Soient f une fonction continue sur un intervalle I, x₀ un réel donné de I et y₀ un réel donné. Il existe une unique primitive F de f sur I telle que F(x₀) = y₀. »
**Activité 4** — 1- Trouver toutes les primitives sur ]0,+∞[ de la fonction f : x ↦ x²/3 − 3/x². 2- Déterminer celle qui s'annule en 1 puis celle qui prend la valeur -1 en 3.
**Activité 5** — « Soit f une fonction qui admet une primitive F sur un intervalle I et soit a un élément de I. Montrer que la primitive G de f sur I qui s'annule en a est définie sur I par : G(x) = F(x) – F(a). »

##### III- Calculs sur les primitives (p.49-)
**Activité 1** — « Soient f et g sont deux fonctions dérivables sur un intervalle ouvert I. »
1- Monter que les fonctions f et g admettent des primitives sur I.
2- Soient F et G deux primitives respectives de f et g sur I.
 a- Montrer que la fonction (F+G) est une primitive de (f+g) sur I.
 b- Soit α ∈ ℝ. Montrer que la fonction αF est une primitive de αf sur I.
**Théorème (encadré)** : « Si F et G sont deux primitives respectives de f et g sur I, alors (F+G) est une primitive de (f+g) sur I et αF est une primitive de αf sur I. »

###### p.50 — Primitives usuelles
« Les tableaux suivants donnent les primitives de quelques fonctions usuelles et de fonctions ayant la forme d'une dérivée connue. • k désigne un réel quelconque. »
Tableau 1 (f(x)=… | Primitive F(x)=… | Intervalle I=…) :
- c (constante) | cx + k | IR
- x | (1/2)x² + k | IR
- 1/x² | −1/x + k | ]−∞,0[ ou ]0,+∞[
- xⁿ, n entier, n ≤ −2 ou n ≥ 1 | (1/(n+1))xⁿ⁺¹ + k | IR si n ≥ 1 ; ]−∞,0[ ou ]0,+∞[ si n ≤ −2
- 1/√x | 2√x + k | ]0,+∞[
« • u désigne une fonction dérivable sur un intervalle I et k un réel quelconque. »
Tableau 2 (Forme de la fonction | Primitive | Conditions de validité) :
- u' | u + k | (aucune)
- u'/u² | −1/u + k | u(x) ≠ 0 pour tout x de I
- uⁿu', n ∈ ℤ \ {−1, 0} | (1/(n+1))uⁿ⁺¹ + k | Lorsque n ≤ −2 : u(x) ≠ 0 pour tout x de I
- u'/√u | 2√u + k | u(x) > 0 pour tout x de I

**Activité 2** — « Pour chacune des fonctions suivantes, déterminer une primitive en précisant l'intervalle sur lequel elle est définie : »
f : x ↦ 3x⁴ − 2x³ − 1 ; f : x ↦ 1/(2√x) + 1 ; f : x ↦ 2/x³
f : x ↦ −2(1 − 2x)⁴ ; f : x ↦ −3/(2 − 3x)³ ; f : x ↦ −4x/(1 − 2x²)²
f : x ↦ x²(2 + x³)² ; f : x ↦ 2(x + 1)/√(x² + 2x + 2) ; f : x ↦ 1/(2√x) + 1/√(4 − x)

###### p.51
**Activité 3** — 1- « Donner une primitive de chacune des fonctions x ↦ 1/(x − 1)³ et x ↦ 1/(x − 1)⁴ définies sur I = ]1,+∞[. »
2- « f est la fonction définie sur I par : f(x) = x/(x − 1)⁴. Trouver des réels α et β tels que pour tout x de I : f(x) = α/(x − 1)³ + β/(x − 1)⁴. En déduire une primitive de f sur I. »
(La page 51 ne contient que cette activité ; le reste est blanc.)

#### AVEC L'ORDINATEUR (p.52-…, bandeau « Avec l'ordinateur »)
**Activité tableur — « tableau dynamique » des coefficients directeurs (nombre dérivé)**
Énoncé (p.52) : « On considère la fonction f définie sur IR par f(x) = 4/(x² + 1). On se propose de dresser un tableau ‘dynamique’ contenant les coefficients directeurs des droites (AM) où A et M sont deux points de la courbe de f d'abscisses respectives : x₀ et x (x₀ fixé et x varie dans un intervalle [a , b] suivant un pas h >0. Les valeurs calculées dans ce tableau, changeront en fonction de a, b, h et de x. Le but est de mettre en évidence la convergence des valeurs vers f '(x₀) pour différentes valeurs de x₀ de l'intervalle [a , b] »
**Etape 1 : Préliminaire** — Dans la cellule A1 taper : « f(x) = 4/ (x²+1) » ; A3 : « a = » ; A4 : « b = » ; A5 : « h = » ; D3 : « x0 = » ; D4 : « f(x0) = » ; B7 : « x » ; C7 : « y » ; D7 : « c(x) ».
Capture d'écran (p.52) : A1 « f(x) = 4/(1+x²) » ; B3 = −2 ; B4 = 2 ; B5 = 0,01 ; D3 « x0 » ; D4 « f(x0) » ; colonnes B, C, D à partir de la ligne 7 (x, y, c(x)).
**Etape 2 : Définir les variables a, b et le pas h** — * Sélectionner la cellule B3 ; menu ‘Insertion’, commande ‘nom’ puis ‘définir’ ; taper la lettre : a ; valider. * B4 → b. * B5 → h. * Sélectionner E3 → taper : x0 ; valider. * Sélectionner E4 → taper : fx0 ; valider. « Ainsi les variables a, b et h, et x0 contiendront respectivement les valeurs introduites dans les cellules B3, B4, B5 et E3. »
(Boîte « Définir un nom » en capture : noms a, b, f_x0, h, x0 ; « Fait référence à : =Feuil1!$E$4 ».)

###### p.53 — Avec l'ordinateur (suite)
**Etape 3 : Calcul des coefficients directeurs de la droite (AM)**
* Choix des valeurs de a, b, h et x₀. « A titre d'exemple : dans la cellule B3 taper -5 ; dans la cellule B4 taper 5 ; dans la cellule B5 taper 0.1 ; dans la cellule E3 taper 1 »
* Dans la cellule E4 taper : « =(4/(x0^2+1) » (parenthèses non appariées telles qu'imprimées)
* Dans la cellule B8 taper : « =a »
* Dans la cellule B9 taper la formule : « = SI(ET(B8<>"";B8+h<=b);B8+h;"") » — « ( i.e. : si la cellule précédente n'est pas vide et x <b alors ajouter h à son contenu et l'écrire dans la cellule courante ; si non ne rien écrire dans la cellule courante ) » — Copier la cellule B9 et la coller dans les cellules : de B10 à B150 (on obtient alors les différentes valeurs de x)
* Dans la cellule C8 taper : « SI(B8<>"";4/(B8^2+1);"") » (c'est-à-dire : si la cellule x n'est pas vide afficher f(x), si non ne rien afficher). Copier la cellule C9 et la coller dans les cellules : de C10 à C150 (on obtient alors les différentes valeurs de y = f(x))
* Dans la cellule D8 taper : « =SI(ET(B8<>"";B8<>x0);(C8-fx0)/(B8-x0);"") » (c'est à dire : si la cellule x n'est pas vide et contient un réel différent de x0 alors afficher c(x), si non ne rien afficher). Copier la cellule C9 et la coller dans les cellules : de D10 à D150 (on obtient alors les différentes valeurs du coefficient directeur c(x)
Capture d'écran (a=-5, b=5, h=0,1, x0=1, f(x0)=2) — lignes 8 à 18 (x ; y ; c(x)) : −5 ; 0,153846 ; 0,307692 | −4,9 ; 0,159936 ; 0,311875 | −4,8 ; 0,166389 ; 0,31614 | −4,7 ; 0,173235 ; 0,320485 | −4,6 ; 0,180505 ; 0,32491 | −4,5 ; 0,188235 ; 0,329412 | −4,4 ; 0,196464 ; 0,333988 | −4,3 ; 0,205233 ; 0,338635 | −4,2 ; 0,214592 ; 0,343348 | −4,1 ; 0,224593 ; 0,348119 | −4 ; 0,235294 ; 0,352941 (recalculées : conformes à f(x)=4/(1+x²) et c(x)=(f(x)−2)/(x−1)).
**Etape 4 : Modification des données** — « Modifier l'une des valeurs a, b, h ou x₀ entraîne le changement de toutes les valeurs calculées dans le tableau, donc on pourra choisir des valeurs de a et b proches de x₀ et un pas h réduit pour voir de proche en proche la convergence des valeurs vers f'(x₀) »

#### EXERCICES ET PROBLÈMES (pp. 54-…)
(aucun corrigé dans le manuel)

**1-** « Pour chacune des questions ci-dessous, une au moins des réponses proposées a, b et c est correcte. » (p.54)
| Question | a | b | c |
1) Pour tout x ∈ ]0,+∞[ f(x) = (x + 2)/x ; f '(x) = ... | 2/x² | −2/x² | 1 + 2/x
2) Pour tout x ∈ ℝ f(x) = x⁵/5 − x⁴/4 ; f '(x) = ... | x⁴/5 − x³/4 | x⁶/6 − x⁵/5 | x⁴ − x³
3) Pour tout x ∈ ]0,+∞[ f(x) = 2/x² − 3x + 5. Une équation de la tangente à la courbe de f au point d'abscisse 1 est : … | y = −7x + 3 | y = −7x + 11 | y = x + 3
4) « On donne le tableau de variations d'une fonction f » : x : −∞ | 1 | 3 | +∞ ; f '(x) : + 0 − 0 + ; f(x) : −∞ ↗ 3 ↘ 1 ↗ +∞. « Et soit F une primitive de f sur IR » | F est croissante sur IR | F' est positive sur IR | F est croissante sur [1,3]

**2-** « Pour chacune des questions ci-dessous, une au moins des réponses proposées a, b et c est correcte. »
| Question | a | b | c |
1) Une primitive de la fonction f : x ↦ 2x + 5 − 2/x² sur ]0,+∞[ est la fonction F : x ↦ | x² − 1/x | x² + 5x − 1/x | x² + 5x + 2/x
 Une primitive de la fonction f : x ↦ 3√x sur IR₊ est la fonction F : x ↦ | 3/(2√x) | x(2√x + 1) | 2x√x
2) La fonction F : x ↦ (1/12)(x³ − 1)⁴ est une primitive sur IR de la fonction f : x ↦ | (1/3)(x³ − 1)³ | x²(x³ − 1)³ | (1/12)x²(x³ − 1)³
3) La fonction F : x ↦ √(x² − 2x + 5) est une primitive sur IR de la fonction f : x ↦ | (x − 1)/(2√(x² − 2x + 5)) | (x − 1)/√(x² − 2x + 5) | (2x − 2)/√(x² − 2x + 5)

**3 -** (p.55) « Dans chacun des cas suivants, prouver que f est dérivable sur l'intervalle I et déterminer sa fonction dérivée : »
a) f : x ↦ x² − 5x − 1, I = IR ; b) f : x ↦ x³ − 2x² + x + 1, I = IR ; c) f : x ↦ −2x⁴ + 3x³ − x + 1, I = IR ; d) f : x ↦ 1/(x − 2), I = ]2,+∞[ ; e) f : x ↦ (x + 1)/(x + 3), I = ]−3,+∞[ ; f) f : x ↦ 1/(x² + 4), I = IR ; g) f : x ↦ (2x² + 1)/(2x² + x + 2), I = IR ; h) f : x ↦ (2x − 1)/√x, I = ]0,+∞[ ; i) f : x ↦ 2x²√x − x, I = ]0,+∞[

**4 -** « Dans chacun des cas suivants, déterminer graphiquement les intervalles sur lesquels f est définie, continue et dérivable, puis dresser le tableau de variations de f »
Deux figures (repère à quadrillage, unité 1) :
- Figure de gauche [R7 : description refaite à l'image 220 dpi — le lecteur inversait le sens des branches extérieures et sous-estimait le maximum ; quadrillage : 1 carreau = 1 unité en abscisse comme en ordonnée] : courbe en trois morceaux et quatre traits verticaux roses (asymptotes) vers x ≈ −1, x ≈ −0,8, x ≈ 1,8 et x ≈ 2 ; branche gauche venant d'une ordonnée ≈ −3 (x ≈ −5) et CROISSANTE vers +∞ le long de l'asymptote x ≈ −1 ; morceau central partant de −∞ (asymptote x ≈ −0,8), maximum à tangente horizontale (flèche bleue) d'ordonnée ≈ 3 en x ≈ 1/2 (trait pointillé vertical), puis redescente vers −∞ (asymptote x ≈ 1,8) ; branche droite venant de +∞ (asymptote x ≈ 2) et DÉCROISSANTE jusqu'à une ordonnée ≈ −3 (x ≈ 6). Valeurs à l'estimation, aucune cote imprimée : [?].
- Figure de droite [R7 : abscisses relevées à l'image 220 dpi — le lecteur donnait −3, −2/−1 et 4,5-5] : courbe partant de x ≈ −6 (ordonnée ≈ −2) avec tangente verticale (flèche bleue vers le haut) ; maximum à tangente horizontale d'ordonnée ≈ 4 en x ≈ −4 ; décroissance jusqu'au point (1, −2) où la demi-tangente à gauche est horizontale (flèche vers la gauche) et la demi-tangente à droite oblique (flèche bleue) : point anguleux ; croissance, passage par l'axe vers x ≈ 2, jusqu'à l'extrémité (6, 3) à tangente horizontale (flèche vers la gauche). Valeurs à l'estimation : [?].

**5 -** « Etudier les variations de chacune des fonctions suivantes sur son domaine de définition : »
a) f : x ↦ x² − x − 1 ; b) f : x ↦ x³ − x² + (1/3)x + 1 ; c) f : x ↦ −x³ + 3x + 1 ; d) f : x ↦ 3x⁴ − 2x² + 1 ; e) f : x ↦ −7/(x + 2) ; f) f : x ↦ (x − 1)/(x + 3) ; g) f : x ↦ 4/(x² − 2x) ; h) f : x ↦ (3x + 1)/(x² − x + 1) ; i) f : x ↦ (x² − 4)/(x² + x + 1)

**6 -** « Dans chacun des cas suivants, vérifier que f est dérivable sur I et déterminer sa fonction dérivée : »
a) x ↦ √(−2x + 5) ; I = ]−∞, 5/2[ ; b) x ↦ x − √(x² − 16) ; I = ]4,+∞[ ; c) x ↦ cos 3x ; I = IR ; d) x ↦ sin 2x ; I = IR

**7 -** « Dans chacun des cas suivants, déterminer un intervalle sur lequel f est dérivable ainsi que sa fonction dérivée : »
a) x ↦ (1 − sin x) sin x ; b) x ↦ (1 + cos x) sin x ; c) f : x ↦ sin x/(1 − cos x) ; d) f : x ↦ sin x/cos 2x

**8 -** (p.56) « f et g étant les fonctions définies sur IR par f(x) = x(2 + x) et g(x) = (1/3)x³ + 2x² + 2x »
a) Calculer f'(x) et g'(x) puis dresser les tableaux de variation de f et de g.
b) On désigne par C et C' les courbes représentatives respectives de f de g dans un repère cartésien (O, i⃗, j⃗). Montrer C et C' admettent en O la même tangente T.
c) Donner une équation cartésienne de T.

**9 -** « Dans le plan muni d'un repère (O, i⃗, j⃗), on considère la parabole Γ d'équation : y = ax² + bx + c. »
1- Soient A et B les points de Γ d'abscisses respectives 0 et 2. Montrer que la tangente à la parabole au point C d'abscisse 1 est parallèle à la droite (AB).
2- Soient M et N les points de Γ d'abscisses respectives α et β. Montrer que la tangente à la parabole au pt P d'abscisse (α+β)/2 est parallèle à la droite (MN).

**10 -** « Soient v une fonction dérivable sur un intervalle ouvert I et u une fonction dérivable sur v(I). En appliquant le théorème ‘dérivée d'une fonction composée’, démontrer les deux résultats suivants : * Si u et v ont le même sens de variation, alors f = u o v est croissante. * Si u et v ont des sens de variation différents, alors f = u o v est décroissante. »

**11 -** « On donne sur le graphique suivant la courbe représentative C d'une fonction f. »
Figure : courbe partant de (0, ≈ −0,5) [R7 : le lecteur écrivait (0, −1) ; à l'image le vecteur unité couvre 2 carreaux et le départ est 1 carreau sous l'axe] avec tangente horizontale au départ (flèche bleue), croissante convexe, traversant l'axe des abscisses en un point d'abscisse voisine de 3 (graduation « 3 ») où une tangente oblique (flèche bleue, pente environ 1/2 à l'estimation) est tracée, puis montée jusqu'à une tangente verticale en x = 5 (flèche bleue vers le bas) ; graduations 1 (en x), 1 (en y). Valeurs exactes de f(0), du point d'abscisse 3 et de la pente : [?] (non cotées).
a- Justifier que f réalise une bijection de [0,5] sur un intervalle J que l'on précisera.
b- Etudier graphiquement la dérivabilité de sa fonction réciproque f⁻¹ sur J.
c- Déterminer (f⁻¹)'(0)

**12 -** « Soit f la fonction définie sur IR \ {1} par f(x) = (2x + 1)/(x − 1) »
a) Montrer que f est croissante sur chacun des intervalles de son domaine de définition.
b) En déduire le sens de variation de la fonction g définie pour x > 1 par g(x) = (2√x + 1)/(√x − 1)
c) On pose h(x) = (x + 2)/(−x + 1) pour x > 1 ; Montrer que h(x) = f(1/x). En déduire le sens de variation de h sur ]1,+∞[
(Remarque de fidélité : f(x) = (2x+1)/(x−1) est décroissante sur chaque intervalle (f' = −3/(x−1)² < 0), non croissante ; l'énoncé a) « croissante » est une coquille imprimée reproduite telle quelle ; voir § Notes. Aussi h(x) = (x+2)/(1−x) = f(1/x)·? : f(1/x) = (2/x+1)/(1/x−1) = (2+x)/(1−x), cohérent.)

###### p.57
**13-** « Soit f la fonction définie sur ℝ \ {1} par f(x) = ax + b + 2/(x − 1), où a et b sont deux réels. C désigne la courbe représentative de f. »
1- Déterminer a et b pour que C passe par le point A(2,3) et admette en ce point une tangente d'équation : y = −x + 5.
2- Pour les valeurs trouvées de a et b, étudier les variations de f.

**14-** « Soit f la fonction définie sur IR \ {−1} et dont le tableau de variations, incomplet, est le suivant : »
Tableau (image) : x : −∞ | −3 | −1 (double barre) | 1 | +∞ ; f '(x) : + 0 − (avant −1) ; − 0 + (après −1) ; f(x) : −∞ ↗ −6 (en x=−3) ↘ « … » (valeur manquante vers −1⁻) ; à droite de −1 : +∞ ↘ 2 (en x=1) ↗ « … » (valeur manquante vers +∞).
« On admet que f est définie par f(x) = ax + b + c/(x + 1). »
1- Calculer f '(x) en fonction de a, b et c.
2- En vous aidant du tableau de variations de f, montrer que l'on a : a = 1, b = -1 et c = 4.
3- Compléter alors le tableau de variations de la fonction f.
(Vérification : f '(x) = a − c/(x+1)² ; avec a=1, b=−1, c=4 : f(1)=2, f(−3)=−6, f '(1)=f '(−3)=0, cohérent avec le tableau.)

**15-** « On considère la fonction f définie sur ]−∞, 4] par f(x) = x√(4 − x). On désigne par C la courbe représentative de f dans un repère orthonormé (O, i⃗, j⃗). »
1- Donner une équation de la tangente T à la courbe C au point d'abscisse nulle.
2- Déterminer le point de C en lequel la tangente est perpendiculaire à T.

**16 -** « Une entreprise fabrique des objets. Le profit unitaire (le profit réalisé par objet fabriqué) est exprimé en dinars en fonction de la durée x nécessaire à la fabrication d'un objet par p = 4√x − x. »
1- Etudier les variations de la fonction f : x ↦ 4√x − x.
2- Pour quelles valeurs de x le profit unitaire est-il positif ?
3- Pour quelles valeurs de x le profit unitaire est-il maximal ? Quel est alors ce profit ?

**17-** « La courbe ci-dessous est la représentation graphique de la fonction f ' dérivée d'une fonction f définie sur [-4 , 6] ; Soit C la courbe représentative de f. »
Figure (repère à quadrillage, 1 carreau = 1 unité, graduations 1 et 1) [R7 : relu à 220 dpi — le lecteur lisait le minimum à −1,5 et le maximum à 3] : courbe de f ' qui part de (−4, 3), décroît en coupant l'axe des abscisses en x = −2, atteint un minimum local à tangente horizontale (flèche bleue) en (1, −3), remonte en coupant l'axe en x = 3, atteint un maximum local à tangente horizontale (flèche bleue) en (5, 4), puis redescend jusqu'à l'axe en x = 6 (segment final presque vertical). Lecture sur quadrillage (points sur des nœuds), aucune cote imprimée : à confirmer sur la figure redessinée [?].
1- Dresser le tableau de variation de f sur [-4 , 6].
2- Préciser les coefficients directeurs des tangentes à C aux points d'abscisses : -4, -2, 1, 3, 5 et 6.
3- Donner une allure possible de C sachant que : f(−4) = −1, f(−2) = 4, f(1) = 2, f(3) = −1, f(5) = 2 et f(6) = 4.

###### p.58
**18 -** « Un artisan fabrique des objets dont le nombre x varie de 1 à 20 par semaine. Le prix de vente unitaire P d'un objet, en dizaines de dinars, vérifie la relation P(x) = −x + 20. »
1- L'artisan fabrique et vend 8 objets. Calculer le prix unitaire de ces objets puis leur montant de vente (exprimé en dinars).
2- Vérifier que la recette R, en dizaines de dinars obtenue par la vente de x objets est R(x) = −x² + 20x.
3- Etudier les variations de R sur l'intervalle [1 , 20].
4- En déduire le nombre d'objets à vendre pour obtenir la recette maximale. Calculer cette recette en dinars.

**19 -** « Une usine fabrique et vend un produit dont la quantité journalière exprimée en tonnes, peut varier de 0 à 5. Toute la production étant vendue, le bénéfice exprimé en milliers de dinars est donné en fonction de la quantité x produite, par la fonction : B(x) = x³ − 12x² + 45x − 34. »
1- Calculer le bénéfice, en dinars pour 5 tonnes de produit puis pour une tonne de produit
2- Calculer B'(x) et étudier son signe
3- Etudier la fonction B sur l'intervalle [0,5]
4- Pour quelle quantité de produit le bénéfice est-il maximal ?
6- A partir de quelle quantité la fabrication est-elle rentable ?
(La numérotation imprimée saute le 5 : 1, 2, 3, 4, 6.)

**20 - (Notion d'élasticité)** « Une étude effectuée sur un certain article a conduit à établir la relation : f(p) = (10⁵ × 6p)/(36p² − 100) pour p ∈ [2,+∞[ où p représente le prix du produit en DT et f(p) la demande liée à ce produit pour le prix p. »
1- Calculer la demande pour p = 0, p = 2,5 et p = 15
2- Montrer que f est décroissante sur [2,+∞[.
3- On suppose que le prix p initialement égal à 2.5d, subit une augmentation de 1%.
 a- Calculer le nouveau prix p₁ et la demande correspondant à ce prix.
 b- Déduire le pourcentage de variation de la demande, consécutive à l'augmentation de ce prix.
4- « On appelle **élasticité** de la demande par rapport au prix, le nombre E(p) = p × f '(p)/f(p) pour p ∈ [2,+∞[. On admettra que ce réel donne une bonne approximation du pourcentage de variation de variation de la demande, pour une augmentation de 1% d'un prix donné. »
 a- Déterminer en le justifiant, le signe de E(p) ; interpréter le résultat.
 b- Montrer que E(p) = 1 − 72p²/(36p² − 100).
 c- Dresser le tableau de variation de E.
 d- Calculer la valeur p₀ pour laquelle l'élasticité est de -1,25.
 e- Comment évolue la demande quand le prix passe de 5 à 5,5DT ?
(Coquille : p = 0 n'appartient pas à [2,+∞[ ; « variation de variation » imprimé.)

###### p.59
**21 -** « Soit la fonction : f : x ↦ x³ − 3x² + 1. On désigne par Cf sa courbe représentative dans un repère (O, i⃗, j⃗). »
1- Vérifier que les fonctions f et f ' sont dérivables sur IR.
2- Déterminer une équation cartésienne de la tangente T à Cf au point d'abscisse nulle
3- Etudier les positions de Cf par rapport à T.
4- Dresser le tableau de signe de la fonction f ''. En déduire que Cf admet n point d'inflexion dont-on donnera les coordonnées. (« n point » imprimé)

**22 -** « f est la fonction définie sur IR par f(x) = x³ – 30x² + 112. »
1- Dresser le tableau des variations de f.
3- Démontrer que l'équation f(x) = 0 admet trois solutions. Avec la calculatrice, donner l'arrondi au dixième ou la valeur exacte de chaque solution.
4- En déduire le signe de f.
5- Calculer la dérivée g' de la fonction définie sur IR par g(x) = (1/4)x⁴ − 10x³ + 112x − 148. Que peut-on en déduire pour g ?
6- Dresser le tableau des variations de g sur IR.
(Numérotation imprimée sans question 2 : 1, 3, 4, 5, 6.)

**23 -** « Une entreprise estime que le coût total, en milliers de dinars, de production de x tonnes d'objets s'exprime, en fonction de x, par : C(x) = x³ – 12x² + 60x. »
1- Etudier les variations de la fonction x ↦ C(x) sur [0 ; +∞[.
« Le coût moyen de fabrication est donné par CM(x) = C(x)/x (pour x > 0). »
2- Quel est le coût moyen de fabrication de 500 kg ?
3- Exprimer CM(x) en fonction de x, puis étudier les variations de la fonction x ↦ CM(x) sur [0 ; +∞[. On note Cm(x) le coût marginal de x, et on admet que Cm(x) = C'(x).
4- Etudier les variations de la fonction x ↦ Cm(x) sur [0 ; +∞[.
5- L'entreprise vend sa production 60 000 dinars la tonne. On note B(x) le bénéfice réalisé pour la vente de x tonnes.
 a- Vérifier que B(x) = -x³ + 12x².
 b- Etudier les variations de la fonction B.
 c- Pour quelle valeur de x le bénéfice est-il maximal ? Vérifier alors que, pour cette valeur de x, le coût marginal est égal au prix de vente unitaire.
6- « On donne sur le graphique ci- dessous, les courbes représentatives des fonctions C, CM, Cm et B »
 a- Identifier chacune de courbes.
 b- Déterminer l'abscisse α du point d'intersection des courbes de CM et Cm.
 c- Que représente CM(α) pour la fonction CM ?
(Vérification interne : B(x) = 60x − C(x) = −x³ + 12x² + 0x ✓ car 60x − 60x = 0 ; prix de vente 60 (milliers de dinars par tonne).)

###### p.60 — suite de l'exercice 23 (graphique en haut de page) puis 24-27
Figure de l'exercice 23 6-) : quatre courbes sur un même repère (axe y gradué +10, +100, +200, +300 et −10 ; axe x gradué +10 et +2 [?] — libellé « +2 » à l'extrémité droite, probablement « +20 », lecture [?]) : une courbe bleue en cloche (maximum ≈ 250-260 vers x≈8), une courbe violette croissante avec palier d'inflexion (≈100 vers x≈4-5) montant à > 300, une courbe rose en U (minimum ≈ 12 vers x ≈ 4) et une courbe noire en U plus aplatie (minimum ≈ 24 vers x ≈ 6, remontant lentement) [R7 : relu à l'image (échelle : 100 unités = 110 px, 10 unités en x = 247 px) — le lecteur lisait le minimum noir à 50-60 et le rose à 15-20 ; la graduation d'abscisse de droite est « +2 » tronqué, placée à x = 20 d'après l'espacement]. Ni légende ni valeurs exactes : [?].
**24 -** « Dans chacun des cas suivants, donner une primitive de f sur l'intervalle I : »
f(x) = 2x² − 3x + 1, I = IR ; f(x) = −x³ + x − 1/√x, I = ]0,+∞[ ; f(x) = 5/√(2x − 1), I = ]1/2,+∞[ ; f(x) = (2 − x)/(x² − 4x + 1)², I = ]−∞,0] ; f(x) = (x − 1)(2x² − 4x + 1), I = IR
**25 -** « f est la fonction définie sur [0,+∞[ par f(x) = x/(2x + 1)³ »
a- Vérifier que pour tout réel positif x, f(x) = 1/(2(2x + 1)²) − 1/(2(2x + 1)³).
b- En déduire une primitive de f sur [0,+∞[.
**26 -** « Soit f la fonction définie sur ]−∞,−2[ par f(x) = (x² + 4x + 6)/(x + 2)². »
a- Justifier que f admet une primitive sur ]−∞,−2[.
b- Déterminer les réels a et b tels que pour tout réel x de ]−∞,−2[, f(x) = a + b/(x + 2)².
c- En déduire la primitive F de f sur ]−∞,−2[, qui prend pour valeur 1 en -3.
**27 -** « Soit f la fonction définie sur ]1,+∞[ par f(x) = (2x³ − 5x² + 4x + 2)/(x − 1)². »
a- Déterminer les réels a, b et c tels que pour tout réel x de ]1,+∞[, f(x) = ax + b + c/(x − 1)².
b- En déduire la primitive F de f qui s'annule en 2.

###### p.61
**28 -** « Soit f la fonction définie et dérivable sur l'intervalle [0 ; 4] dont la représentation graphique, dans un repère orthonormé (o, i⃗, j⃗), est la courbe C ci-dessous. »
« Les points M, N, P, Q et R appartiennent à C et leurs coordonnées sont respectivement : (0, 3/2), (1, 7/2), (2, 5/2), (3, 3/2) et (4, 7/2). La courbe C admet en chacun des points N et Q une tangente parallèle à l'axe des abscisses. La droite Δ est tangente à la courbe C au point P ; elle passe par le point S de coordonnées (3 ; 1). »
Figure : repère à quadrillage ; arche en M (début, x=0), maximum en N (tangente horizontale, flèche bleue), descente en P où la droite Δ (noire) est tangente, minimum en Q (tangente horizontale, flèche bleue), remontée jusqu'à R ; le repère (O, i⃗, j⃗) est dessiné séparément en bas à gauche (0, 1, 1), et le trait horizontal de la grille passant par M et Q n'est pas l'axe des abscisses de l'énoncé (ordonnées lues dans le texte, pas sur la figure).
1- a) Donner f '(1), f '(2) et f '(3).
 b) Déterminer une équation de la droite Δ.
2- Déterminer graphiquement le nombre de solutions de l'équation f(x) = 3 sur l'intervalle [0 ; 4].
3- f est la dérivée d'une fonction F définie sur l'intervalle [0 ; 4]. En justifiant la réponse, donner le sens de variation de F.
4- a) Pour tout x ∈ [0 ; 4], f '(x) = α (x – 1)(x – 3), α étant une constante réelle. Déterminer α à l'aide des résultats de la question 1- a).
 b) Vérifier que pour tout x ∈ [0 ; 4], f '(x) = (3/2)x² − 6x + 9/2 puis déterminer l'expression de f(x) pour x ∈ [0 ; 4].
(Cohérence vérifiée : pente de Δ entre P(2, 5/2) et S(3,1) = −3/2 = f '(2) ; α(2−1)(2−3) = −α = −3/2 donne α = 3/2 ; (3/2)(x² − 4x + 3) = (3/2)x² − 6x + 9/2 ; en revanche aucun corrigé n'est imprimé.)

#### MATH CULTURE (p.62)
**Titre imprimé : « Interprétation graphique du signe de la dérivée seconde »**
« Soit f une fonction admettant une dérivée seconde sur l'intervalle [a,b] et soit Cf la représentation graphique ci-contre. Les pentes des tangentes successives à Cf en un point M d'abscisse x décroissent. lorsque x varie de a à c, puis croissent lorsque x varie de c à b. Or la pente des tangentes est donnée, point par point, par le nombre dérivé f '(x) ; donc si la pente décroît, la dérivée de la fonction f ', c'est-à-dire f '', est négative pour tout x de [a,c] et si la pente croit, f '' est positive, pour tout x de [c,b].
Sur l'intervalle [a,c] on dira que la courbe Cf admet une concavité dirigée vers le bas ou aussi que Cf est concave.
Sur l'intervalle [c,b] on dira que la courbe Cf admet une concavité dirigée vers le haut ou aussi que Cf est convexe.
Ainsi la courbe Cf change de concavité au point de C(c ,f(c)), dans ce cas C est un point d'inflexion de Cf. »
Figures : (1) courbe en « S » sur [a,b] avec maximum local puis minimum local, abscisses a, c, b en pointillés verts et tangentes successives en gris ; (2) arche concave (cloche) avec faisceau de tangentes sur [a,c] ; (3) arche convexe (cuvette) avec faisceau de tangentes sur [c,b].
**Encadré biographique** : « LAGRANGE Joseph Louis, Comte de, français, 1736-1813 » (portrait). « Né à Turin (Italie), il y enseigna les mathématiques dès l'âge de 19 ans. Ses principaux traités mathématiques résident dans la Théorie des fonctions analytiques (1797). Lagrange simplifia les notations fonctionnelles en introduisant le symbole f ' pour la dérivée d'une fonction ainsi que f '', f '''. Il appelle fonction primitive la fonction f dont dérivent f ', f '', etc., appelées respectivement première fonction dérivée, seconde fonction dérivée, etc. On entendait par primitif à l'époque - indépendamment de tout sens mathématique - ce qui n'est dérivé d'aucun autre et par dérivé (du latin rivus = ruisseau) celui qui provient d'un autre appelé primitif. On tourne un peu en rond, mais c'est clair... notons que le substantif primitive ne prendra sa place définitive qu'au début du 20è siècle. »
Source citée : aucune source bibliographique imprimée au-delà du nom de Lagrange.

---

#### VOCABULAIRE OFFICIEL (termes exacts imprimés)
nombre dérivé ; dérivable en x₀ ; dérivable à droite / à gauche ; nombre dérivé à droite (f'_d) / à gauche (f'_g) ; tangente ; demi tangente ; point anguleux ; dérivable sur un intervalle ; fonction dérivée ; dérivée seconde / fonction dérivée seconde (f '') ; deux fois dérivable ; point d'inflexion ; fonction composée (g ∘ f) ; fonction réciproque (f⁻¹), bijection ; accroissements finis (théorème, inégalités) ; extremum relatif ; extremums ; primitive (de f sur I) ; coût marginal (Cm = C') ; coût moyen (CM = C(x)/x) ; élasticité de la demande par rapport au prix E(p) = p × f '(p)/f(p) ; concave / convexe / concavité dirigée vers le bas / vers le haut (Math culture seulement) ; « tableau de variation(s) » ; « fonction rationnelle », « fonction polynôme ».

#### BORNES DE LA SECTION
**INCLUS** (au programme tel qu'imprimé dans le chapitre) : dérivabilité en un point, à droite et à gauche ; condition dérivable ⇒ continue ; tangente y = f '(x₀)(x − x₀) + f(x₀), demi-tangentes, tangente parallèle à (Oy) (limite infinie du taux d'accroissement), point anguleux ; dérivabilité sur un intervalle, fonction dérivée ; opérations (somme, produit par un réel, produit, inverse, quotient) ; polynômes et fonctions rationnelles ; lien signe de f ' / sens de variation ; extremum relatif et f '(x₀) = 0 ; dérivée seconde, point d'inflexion (théorème admis) ; dérivée de g∘f, de fⁿ (n ∈ ℤ), de √f ; dérivée de la fonction réciproque (théorème admis) ; sin' = cos, cos' = −sin (rappel) ; théorème des accroissements finis (admis), inégalités des accroissements finis, corollaire |f(b) − f(a)| ≤ k|b − a| ; primitive : définition, existence pour une fonction continue (admis), ensemble des primitives (F + k), unicité avec condition F(x₀) = y₀ (admis), somme et produit par un réel, tableaux des primitives usuelles (c, x, 1/x², xⁿ n ≤ −2 ou n ≥ 1, 1/√x ; u', u'/u², uⁿu', u'/√u) ; applications économiques : coût marginal, coût moyen, coût total à partir du coût marginal, recette, bénéfice, élasticité ; tableur (taux d'accroissement convergeant vers f '(x₀)).
**EXCLU / non traité dans ces pages** : primitive de 1/x et de u'/u (le manuel ne donne aucune formule, l'Activité 4 p.48 demande seulement de justifier l'existence et le sens de variation de F, sans citer de logarithme) ; fonctions logarithme/exponentielle (chapitre IV) ; intégrale et lien intégrale/primitive (chapitre V) ; tableau de primitives de sin et cos (aucun imprimé) ; démonstration des théorèmes admis (composée, réciproque, TAF, existence de primitive, point d'inflexion) ; théorème de Rolle sous ce nom (l'exercice p.46 Act.3 2) en énonce le cas f(a)=f(b) sans le nommer) ; définition formelle de concave/convexe (seulement en Math culture, p.62, de façon intuitive) ; dérivées d'ordre supérieur à 2 (f ''' cité seulement dans la biographie) ; équations différentielles ; développements limités.

#### NOTIONS-CLÉS (≤ 8)
1. Nombre dérivé (limite du taux d'accroissement), dérivabilité à droite/à gauche, tangente et point anguleux.
2. Opérations sur les dérivées et signe de f ' ⇒ variations (extremum relatif si f ' s'annule en changeant de signe).
3. Dérivée seconde et point d'inflexion (f '' s'annule en changeant de signe).
4. Dérivée d'une composée : (g∘f)' = g'(f) × f ', (fⁿ)' = n fⁿ⁻¹ f ', (√f)' = f '/(2√f).
5. Dérivée de la réciproque : (f⁻¹)'(y₀) = 1/f '(x₀) si f '(x₀) ≠ 0.
6. Accroissements finis : égalité (existence de c), inégalités m ≤ ... ≤ M, majoration |f(b) − f(a)| ≤ k|b − a|.
7. Primitives : F' = f ; F + k ; unicité avec condition initiale ; tableaux de primitives usuelles (xⁿ, 1/x², 1/√x, u'uⁿ, u'/u², u'/√u).
8. Applications économiques : coût marginal Cm = C', coût moyen CM = C/x, recette R = x·P, bénéfice B, élasticité E(p) = p f '(p)/f(p).

---

#### § NOTES
**Pages lues** : 30/30 (pp. 33 à 62), chacune en texte (pdftotext -layout) ET à l'image (110 dpi). **Sondes agrandies** : p.38 (items b, d de l'Act.3 à 200 dpi : « x²√x − 1 » et « x² − 1 », sans radical sur d), p.53 (capture d'écran à 110 dpi, valeurs recalculées), p.55 (exercices 5, 6, 7 à 200 dpi ; graphiques de l'ex.4 à 170 dpi), p.56 (graphique de l'ex.11 à 170 dpi). Aucun écart de chiffre entre la couche texte et l'image sur ces pages, hormis les formules, dégradées dans la couche texte (lues à l'image seule).

**Structure du chapitre telle qu'imprimée** : p.33 plan ; pp.34-35 « Pour commencer » (Activités 1-3, bandeau « Cours » en tête de page) ; pp.36-51 « Cours » (Dérivation : Revoir I-1 à I-5 pp.36-41, II p.41-42, III pp.42-43, IV pp.43-44, V pp.45-47 ; Primitives : I pp.47-48, II pp.48-49, III pp.49-51) ; pp.52-53 « Avec l'ordinateur » ; pp.54-61 « Exercices et problèmes » (28 exercices) ; p.62 « Math culture ». Le manuel ne comporte pas de rubrique « Pour commencer » explicitement titrée sur les pages 34-35 : leur rattachement est déduit de la position (avant le titre « DERIVATION » p.36) et de la structure type annoncée dans le sommaire du manuel.

**Coquilles / incohérences imprimées** (reproduites telles quelles) :
- p.36-… numérotation : les activités ont leur numérotation redémarrant à 1 dans chaque sous-section, donc plusieurs « Activité 1/2/3 » ; la même numérotation répétée dans le chapitre (voir sous-sections).
- p.34 Act.1 : « derivé » sans accent (« nombre derivé »), « Lecoefficient directeur D est égalà » ; sans conséquence.
- p.42 Activité 1 (III) : deux questions numérotées « 1- » (« Vérifier que f = g∘h » puis « Déterminer les fonctions dérivées de f, g et h ») ; la 3ᵉ est numérotée « 2- ».
- p.43 : deux « Activité 2 » dans la sous-section III (une sur f = (2x−3)/(x−1), une avec quatre fonctions a-d).
- p.44 : Act.3 (première) numérotée 1, 3, 2 pour ses questions ; puis une seconde « Activité 3 » dans la même sous-section IV.
- p.45 Act.4 de IV, question 2 : « Calculer les antécédents de 0, 1, −1, 1/2 et √3/2 par f⁻¹ » (tel qu'imprimé ; f⁻¹ d'un nombre est une image, non un antécédent — formulation du manuel).
- p.47 Activité 3 (a, b, c) : en c), f(x) = 1/(2√x) + x² mais F(x) = √x − (1/3)x³ + √2 dont la dérivée est 1/(2√x) − x² (signe du terme en x²/x³ incohérent) : coquille imprimée.
- p.52 : texte « Dans la cellule D3 taper x0 = » et « D4 : f(x0) = » mais l'étape 2 définit les noms sur E3 (x0) et E4 (fx0) ; la capture montre A1 « f(x) = 4/(1+x²) » alors que le texte dit « f(x) = 4/ (x²+1) » ; la boîte « Définir un nom » liste « f_x0 » alors que le texte dit « fx0 ».
- p.53 : « =(4/(x0^2+1) » parenthèses non appariées ; « SI(B8<>"";4/(B8^2+1);"") » sans « = » en C8 ; « Copier la cellule C9 et la coller dans les cellules de D10 à D150 » (devrait être D9) ; « x <b » dans l'explication alors que la formule teste B8+h<=b.
- p.54 Ex.1 : la question 4 donne le tableau de variations de f (avec « F est une primitive de f ») : tableau transcrit −∞ ↗ 3 ↘ 1 ↗ +∞.
- p.54 Ex.2 : question 1 comporte deux sous-lignes (la 2ᵉ « Une primitive de 3√x » non numérotée) ; les questions suivantes sont numérotées 2) et 3).
- p.56 Ex.12 a) : « Montrer que f est croissante sur chacun des intervalles de son domaine de définition » alors que f(x)=(2x+1)/(x−1) a pour dérivée −3/(x−1)² < 0 (décroissante) : coquille d'énoncé à signaler ; b) et c) en dépendent.
- p.58 Ex.19 : numérotation 1, 2, 3, 4, 6 (le 5 manque). p.59 Ex.22 : 1, 3, 4, 5, 6 (le 2 manque). Ex.20 1) : p = 0 hors du domaine [2,+∞[ ; « variation de variation » ; Ex.21 4) : « admet n point d'inflexion ».
- p.60 Ex.24 : plusieurs fonctions sans « f » devant ; tout sans conséquence.
- p.61 Ex.28 : l'axe horizontal de la figure ne coïncide pas avec y = 0 (le repère de référence est dessiné à part, en bas à gauche) ; les ordonnées valent celles du texte.
- p.40/p.39 : l'Act.4 p.40 présente f ' non définie en x=3 (double barre) ; la troisième courbe est la seule avec point anguleux.
- Vérifications arithmétiques recomptées (sans corrigé) : p.41 Act.7 B(x) = 110x − (x²+60x+121) = −x²+50x−121 ; p.48 II Act.1 G(x) = 2 − 1/(x²+1) donc F − G = −2 ; Ex.14 (a=1, b=−1, c=4 reproduit le tableau) ; Ex.23 B = 60x − C ; Ex.25, 26 décompositions exactes.

**`[?]` justifiés** : valeurs exactes lues sur les courbes des figures non cotées (p.35 courbe C et 4 représentations ; p.37 Act.1 et Act.2 ; p.39 Act.1-2 ; p.40 Act.4-6 ; p.43 Act.1 de IV ; p.44 Act.3 seconde ; p.55 Ex.4 ; p.56 Ex.11 ; p.57 Ex.17 ; p.60 graphique de l'Ex.23 et son axe x) — le manuel n'imprime pas de valeurs ; les auteurs de chapitre ne doivent pas les inventer et doivent soit reconstruire la figure à partir d'une fonction explicite, soit renvoyer à une figure à redessiner.
**Aucun corrigé** n'est imprimé dans ces 30 pages ; aucun n'a été inventé.

---

### Chapitre `m03-p63-84`

### m03 — Chapitre III « Étude de fonctions » (manuel 222463P00, p.63-84)

Source : manuel officiel CNP « Mathématiques », 4e année secondaire, section économie et gestion. Notation : $\mathbb{R}$ = IR imprimé. Plan du chapitre (p.63) : Pour commencer ; Cours (Revoir ; Exemples d'étude de fonction polynôme ; rationnelle ; contenant des racines carrées ; trigonométrique) ; Avec l'ordinateur ; Exercices et problèmes ; Math culture. Les figures (courbes) sont décrites, non reproductibles en chiffres : le manuel ne donne pas de corrigé.

#### 1. POUR COMMENCER (p.64-65)

##### Activité 1 (p.64)
Énoncé : « Parmi les courbes suivantes, identifier celle qui représente une fonction paire et celle qui représente une fonction impaire : » 4 figures sur repère quadrillé (unité 1) : (a) courbe en forme de W/M à plusieurs arches, symétrique par rapport à l'axe des ordonnées ; (b) courbe décroissante à gauche puis croissante à droite, de type racine, non symétrique, passant près de l'origine ; (c) courbe oscillante (une bosse à gauche, creux, puis bosse à droite) de type sinus, symétrique par rapport à l'origine ; (d) courbe oscillante avec un saut/discontinuité en 0, non symétrique. Aucune réponse donnée.

##### Activité 2 (p.64)
Énoncé : « Déterminer dans chacun des cas suivants, les asymptotes à la courbe représentée et donner une équation cartésienne de chacune de ces asymptotes. » 4 figures : (a) courbe avec plateau horizontal à gauche et à droite (au-dessus de l'axe) et branche plongeant vers le bas autour de x = 0 (asymptote verticale + asymptote horizontale) ; (b) courbe avec une droite oblique tracée à gauche (asymptote oblique en −∞) et palier horizontal à droite ; (c) courbe à deux branches, droite horizontale tracée à gauche, asymptote verticale à droite de l'axe des ordonnées et droite oblique tracée à droite ; (d) courbe avec deux droites obliques tracées (une en −∞, une en +∞). Aucune équation numérique lisible sans le quadrillage : ne pas inventer.

##### Activité 3 (p.65)
« La fonction f définie sur $\mathbb{R}\setminus\{1\}$ par $f(x)=\frac{x^2-3}{x-1}$ a pour représentation graphique une courbe C dans un repère cartésien. Confirmer ou nier chacune des propositions suivantes en donnant une brève justification :
- La droite d'équation y = x+1 est asymptote à C en $+\infty$.
- La droite d'équation y = 1 est asymptote à C.
- La droite d'équation x = 1 est asymptote à C. »

##### Activité 4 (p.65)
« On donne ci-contre la représentation graphique d'une fonction f » (courbe décroissante de type arctan : palier horizontal en haut à gauche, palier horizontal en bas à droite, passant près de l'origine). « Identifier parmi les représentations graphiques suivantes, celle de la fonction $x \mapsto |f(x)|$. » 3 figures proposées : (1) courbe en pointe (cusp) en haut près de l'ordonnée 1, avec palier bas des deux côtés ; (2) courbe décroissante puis remontant avec pointe vers x≈1 et palier haut à droite ; (3) courbe symétrique avec pointe en bas près de l'ordonnée 1 et paliers hauts des deux côtés.

#### 2. COURS (p.66-73)

##### I- Revoir

###### 1) Asymptotes parallèles aux axes (p.66)
Encadré (verbatim) :
- « La droite d'équation y = a est asymptote horizontale à la courbe C si : $\lim_{x\to+\infty} f(x)=a$ ou $\lim_{x\to-\infty} f(x)=a$ »
- « La droite d'équation x = a est asymptote verticale à la courbe C si : $\lim_{x\to a^+} f(x)=\pm\infty$ ou $\lim_{x\to a^-} f(x)=\pm\infty$ »

Activité 1 : « Soit f la fonction dont la courbe représentative C est donnée ci-dessous » (figure : courbe qui descend de +∞ le long d'une droite verticale x = a située à gauche de l'axe des ordonnées, passe par un creux, puis remonte et se stabilise sur un palier horizontal à droite). « 1- Déterminer $\lim_{x\to+\infty} f(x)$ et $\lim_{x\to a^+} f(x)$. 2- Préciser les asymptotes à C. »

Activité 2 : « Soit f la fonction définie sur IR \ {2 ; −2} par $f(x)=\frac{2x^2-3x+1}{x^2-4}$. Calculer la limite de f : - à droite et à gauche en 2. - à droite et à gauche en -2. - en −∞ et +∞. Interpréter graphiquement les résultats. »

###### 2) Asymptote oblique (p.66)
Encadré (verbatim) : « La droite d'équation y = ax + b (a ≠ 0) est asymptote oblique à la courbe C au voisinage de +∞ (respectivement au voisinage de −∞) si : $\lim_{x\to+\infty}[f(x)-(ax+b)]=0$ (respectivement $\lim_{x\to-\infty}[f(x)-(ax+b)]=0$) »

Activité 1 : « Soit f la fonction définie sur $\mathbb{R}\setminus\{2\}$ par $f(x)=\frac{2x^2-5x+3}{x-2}$. C étant sa courbe représentative dans un repère $(O,\vec i,\vec j)$. 1- Montrer que pour tout x de $\mathbb{R}\setminus\{2\}$, $f(x)=2x-1+\frac{1}{x-2}$. 2- Montrer que la droite $\Delta : y=2x-1$ est asymptote à la courbe C au voisinage de +∞ et de −∞. »

###### 3) Branches paraboliques (p.67)
Encadré 1 (verbatim) : « Soient f une fonction admettant en l'infini une limite infinie et C sa courbe représentative.
* Si $\lim_{x\to+\infty}\frac{f(x)}{x}=0$ ou $\lim_{x\to-\infty}\frac{f(x)}{x}=0$, alors C admet une branche parabolique de direction celle de l'axe des abscisses.
* Si $\lim_{x\to+\infty}\frac{f(x)}{x}=\pm\infty$ ou $\lim_{x\to-\infty}\frac{f(x)}{x}=\pm\infty$, alors C admet une branche parabolique de direction celle de l'axe des ordonnées. »

Encadré 2 (verbatim) : « Soient f une fonction admettant en l'infini une limite infinie et C sa courbe représentative. Si $\lim_{x\to+\infty}\frac{f(x)}{x}=a\neq 0$ et $\lim_{x\to+\infty} f(x)-ax=\pm\infty$ ou si $\lim_{x\to-\infty}\frac{f(x)}{x}=a$ (a ≠ 0) et $\lim_{x\to-\infty} f(x)-ax=\pm\infty$, alors C admet une branche parabolique de direction celle de la droite d'équation y = ax. » (imprimé tel quel : les DEUX demi-lignes de limite portent « x→+∞ » ; la seconde devrait être −∞, voir § Notes.)

Activité 1 : « 1- Soit f la fonction définie sur $[-1,+\infty[$ par $f(x)=\sqrt{x+1}$. Montrer que la courbe représentative de f admet une branche parabolique de direction l'axe des abscisses au voisinage de +∞. 2- Soit g la fonction définie sur $\mathbb{R}$ par $g(x)=x^3-2x^2-1$. Montrer que la courbe représentative de g admet deux branches paraboliques de direction l'axe des ordonnées l'une au voisinage de +∞ et l'autre au voisinage de −∞. »

Activité 2 : « Soit f la fonction définie sur $[1,+\infty[$ par $f(x)=x-\sqrt{x-1}$. On donne sa représentation dans le graphique ci-contre (courbe C_f sous la droite y = x, minimum près de x = 1,25 environ ; droite y=x tracée, repère unité 1). Calculer $\lim_{x\to+\infty} f(x)$, $\lim_{x\to+\infty}\frac{f(x)}{x}$ puis $\lim_{x\to+\infty}(f(x)-x)$. »

(Numérotation imprimée : Activités 1, 2, puis 4 ; pas d'Activité 3 — voir § Notes.)

Activité 4 : « Étudier les branches infinies de la courbe de chacune des fonctions suivantes : $f:x\mapsto x^4-2x^2+5$ ; $g:x\mapsto x\sqrt{x}$ ; $h:x\mapsto x+2\sqrt{x}$ ; $k:x\mapsto \frac{x^3+1}{x+1}$ »

##### II- Exemples d'étude de fonction polynôme (p.68-69)
Encadrés (verbatim) :
- « Soient f une fonction définie sur un domaine D et C sa courbe représentative dans un repère orthonormé. * Le point I(a,b) est un centre de symétrie de C si et seulement si pour tout x de D on a : $(2a-x)\in D$ et $f(2a-x)=2b-f(x)$ »
- « Dans un repère, si C est la représentation graphique d'une fonction f alors la courbe représentative de f+k (avec k un réel) est l'image de C par la translation de vecteur $k\vec j$. »

**Activité 1** : « Soit la fonction $f:x\mapsto x^3-3x-1$. C désigne la courbe représentative de f dans un repère orthonormé $(O,\vec i,\vec j)$. 1- Étudier les variations de f. 2- Montrer que la courbe C admet un point d'inflexion I dont on donnera les coordonnées. 3- Vérifier que I est un centre de symétrie de C. 4- Étudier les branches infinies de C. 5- Tracer la courbe C dans un repère orthonormé $(O,\vec i,\vec j)$. 6- Soit g la fonction définie sur IR par $g(x)=x^3-3x+1$. a) Vérifier que la courbe de g se déduit de celle de f par une translation que l'on précisera. b) Tracer dans le même repère la courbe C' de la fonction g. »

**Activité 2** : « Soit la fonction $f:x\mapsto 2x^4-4x^2+1$. C désigne la courbe représentative de f dans un repère orthonormé $(O,\vec i,\vec j)$. 1- Montrer que la fonction f est paire. 2- Calculer $\lim_{x\to+\infty}f(x)$ et $\lim_{x\to+\infty}\frac{f(x)}{x}$ puis interpréter graphiquement les résultats. 3- a- Montrer que f est dérivable sur $\mathbb{R}$ et que $f'(x)=8x(x^2-1)$. b- Dresser le tableau de variation de f. 4- Tracer la courbe C dans un repère orthonormé. 5- a- Déterminer graphiquement, suivant les valeurs du réel k, le nombre de solutions de l'équation : f(x) = k. b- Résoudre dans IR l'équation f(x) = 1 et en déduire les solutions de l'inéquation f(x) > 1. »

**Activité 3** (situation entreprise, p.68-69) : « Une entreprise décide de fabriquer et de commercialiser un produit. Le coût de production exprimé en milliers de dinars, en fonction du nombre x de tonnes produites est modélisé par : $C(x)=x^3-30x^2+300x$, avec $x\in[0,20]$.
1- Après une étude de marché, l'entreprise espère vendre son produit à 84 milles dinars la tonne.
 a- Déterminer, en fonction du nombre x de tonnes produites, la recette R(x) en milliers de dinars espérée par cette entreprise.
 b- En étudiant la position relative des courbes Γ et Δ représentant respectivement les fonctions C et R, déterminer l'intervalle de production dans lequel l'entreprise assure un bénéfice.
 c- Tracer dans le même repère les courbes Γ et Δ. (sur l'axe des abscisses l'unité désigne une tonne et sur l'axe des ordonnées, l'unité désigne 100 milles dinars).
 d- Déterminer graphiquement, à une tonne près, le nombre de tonnes à produire pour assurer un bénéfice maximal. Confirmer le résultat précédent par le calcul.
2- Pour affaiblir la concurrence, l'entreprise décide de vendre son produit le moins cher possible tout en assurant un bénéfice. Soit $C_m(x)=\frac{C(x)}{x}$ le coût moyen de fabrication.
 a- Exprimer $C_m(x)$ en fonction de x. Étudier les variations de $C_m$ sur l'intervalle [0, 20].
 b- En déduire la valeur $x_0$ qui assure un coût moyen minimal. Quel est alors le prix de vente d'une tonne adopté ? »
(Prix 84 « milles dinars » = 84 milliers de dinars par tonne, tel qu'imprimé.)

##### III- Exemples d'étude de fonction rationnelle (p.69-71)
Encadré (verbatim) : « Dans un repère, si C est la représentation graphique d'une fonction f alors la courbe représentative de la fonction $x\mapsto f(x-k)$ (avec k un réel) est l'image de C par la translation de vecteur $k\vec i$. »

**Activité 1** : « On considère la fonction $f:x\mapsto\frac{(x-1)^2}{x^2-2x}$ et on désigne par C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. 1- Déterminer l'ensemble de définition de f. 2- Montrer que la droite D : x = 1 est un axe de symétrie pour la courbe C. 3- Calculer : $\lim_{x\to+\infty}f(x)$ [R7 : « +∞ » rétabli dans la formule], $\lim_{x\to2^-}f(x)$ et $\lim_{x\to2^+}f(x)$ et interpréter graphiquement les résultats [limites imprimées avec symboles : +∞ ; 2⁻ ; 2⁺]. 4- a- Montrer que f est dérivable en tout point de IR \ {0, 2} et que $f'(x)=\frac{2(1-x)}{(x^2-2x)^2}$. b- Dresser le tableau de variation de f. 5- Tracer la droite D et la courbe C.
4- Soit la fonction g définie sur IR \ {−1,1} par $g(x)=\frac{x^2}{x^2-1}$. a- Vérifier que la fonction g est paire. b- Montrer que pour tout x de IR \ {−1,1}, g(x) = f(x+1). c- En déduire la construction de la courbe C' de g. »

**Activité 2** : « Soit la fonction $f:x\mapsto\frac{x^3}{x^2+3x+3}$. 1- a- Montrer que f est dérivable sur IR et que $f'(x)=\frac{x^2(x+3)^2}{(x^2+3x+3)^2}$. b- Déduire que f est strictement croissante sur IR. c- Calculer : f(0), f(−3), $\lim_{x\to+\infty}f(x)$ et $\lim_{x\to-\infty}f(x)$. d- Dresser le tableau de variations de f. 2- a- Montrer que la droite D d'équation y = x − 3 est asymptote à la courbe C de f au voisinage de +∞. b- Montrer que la droite D coupe la courbe C en un seul point I dont on donnera les coordonnées. c- Démontrer que I est un centre de symétrie pour C. 3- Tracer D et C dans un même repère. 4- a- Tracer dans le même repère la courbe C' de la fonction |f|. b- Justifier graphiquement que la fonction |f| est dérivable en 0. »

**Activité 3** (coût marginal, coût moyen) : « Une entreprise fabrique x milliers d'objets avec 0 ≤ x ≤ 15. Le coût marginal en dinars de cette production est modélisé sur [0,15] par $C_m(x)=3x^2-36x+750$.
1- Sachant que les coûts fixes s'élèvent à 200 dinars, déterminer l'expression du coût total C(x).
2- La fonction coût moyen $C_M$ est définie sur ]0,15] par $C_M(x)=\frac{C(x)}{x}$.
 a- Déterminer l'expression de $C_M(x)$.
 b- Calculer $C'_M(x)$ et vérifier que pour tout x de ]0,15] on a : $C'_M(x)=\frac{2(x-10)(x^2+x+10)}{x^2}$.
 c- Étudier le signe de $C'_M(x)$ et dresser le tableau de variation de $C_M$ sur ]0,15].
 d- Combien d'objets faut-il fabriquer pour que le coût moyen soit minimal ?
 e- Calculer alors ce coût moyen et le coût marginal correspondant.
3- a- Tracer les courbes représentatives de $C_m$ et $C_M$ dans un même repère orthogonal (unités : 1cm pour un millier d'objets en abscisses et 1cm pour 100 dinars en ordonnées).
 b- Comparer graphiquement le coût marginal et le coût moyen. »
(Le texte imprime « $[0,15]$ » pour l'intervalle de définition de $C_M$ en 2-c, mais ]0,15] en 2 ; voir § Notes.)

**Activité 4** (p.70-71) : « Soient la fonction $f:x\mapsto\frac{1-x}{x^2-2x}$ et C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$ du plan. 1- Montrer que f est croissante sur chacun des intervalles de son ensemble de définition. 2- Dresser le tableau de variation de f. 3- Montrer que le point I(1 , 0) est un centre de symétrie pour la courbe C. 4- Déterminer les asymptotes à C. 5- Tracer la courbe C. 6- On se propose de construire la courbe C' de la fonction $g:x\mapsto\frac{2x^2-x-2}{x^2-1}$. a) Vérifier que g(x−1) = 2 + f(x) et en déduire une relation entre C et C'. b) Construire C' dans le même repère $(O,\vec i,\vec j)$. »

##### IV- Exemples d'étude de fonction contenant des racines carrées (p.71-72)

**Activité 1** : « Soient la fonction $f:x\mapsto\sqrt{x^2+2x+3}$ et C sa courbe représentative dans un repère orthonormé du plan. 1- a- Montrer que f est définie sur $\mathbb{R}$. b- Vérifier que la droite Δ : x = −1 est un axe de symétrie de la courbe C. 2- a- Montrer que f est continue et dérivable sur $\mathbb{R}$ et que : $f'(x)=\frac{x+1}{\sqrt{x^2+2x+3}}$. b- Préciser le sens de variation de f sur $[-1,+\infty[$. c- Prouver que $\lim_{x\to+\infty}f(x)=+\infty$. d- Dresser le tableau de variation de f sur IR. 3- a- Vérifier que $f(x)-(x+1)=\frac{2}{\sqrt{x^2+2x+3}+x+1}$. b- En déduire que la droite D : y = x+1 est asymptote à la courbe C au voisinage de +∞. c- Montrer que la droite D' : y = −x−1 est asymptote à la courbe C au voisinage de −∞. 4- Tracer la courbe C et les droites D et D'. »

**Activité 2** : « Soient la fonction $f:x\mapsto x+\sqrt{x^2+1}$ et C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$ du plan. 1- a- Montrer que f est continue et dérivable sur $\mathbb{R}$ et que : $f'(x)=1+\frac{x}{\sqrt{x^2+1}}$. b- Montrer que pour tout x de ]−∞, 0[, $f'(x)=\frac{1}{\sqrt{x^2+1}\,(\sqrt{x^2+1}-x)}$. c- En déduire le sens de variation de f. d- Prouver que $\lim_{x\to+\infty}f(x)=+\infty$ et $\lim_{x\to-\infty}f(x)=0$. e- Dresser le tableau de variation de f. 2- Vérifier que $f(x)-2x=\frac{1}{\sqrt{x^2+1}+x}$ et en déduire que la droite D : y = 2x est asymptote à la courbe C au voisinage de +∞. 3- Tracer la droite D et la courbe C dans le repère $(O,\vec i,\vec j)$. »

**Activité 3** : « Soient la fonction $f:x\mapsto\sqrt{|2x-x^2|}$ et C sa courbe représentative dans un repère orthonormé du plan. 1- Montrer que la droite D : x = 1 est un axe de symétrie pour C. 2-a- Vérifier que : pour tout x ≠ 2 on a $\frac{f(x)-f(2)}{x-2}=\frac{-x}{\sqrt{2x-x^2}}$. [R7 : renvoi « voir § Notes » sans note correspondante supprimé ; formule conforme à l'image, valable pour 0 < x < 2] b- Étudier alors la dérivabilité de f en 2 et interpréter graphiquement le résultat. c- Montrer que f est dérivable sur chacun des intervalles [1,2[ et ]2,+∞] [R7 : crochet fermant « ] » imprimé tel quel à 300 dpi (coquille du manuel pour ]2,+∞[), le lecteur l'avait corrigé en silence] et vérifier que : $f'(x)=\frac{1-x}{\sqrt{2x-x^2}}$ si 1 ≤ x < 2 ; $f'(x)=\frac{x-1}{\sqrt{x^2-2x}}$ si x > 2. 3- a- Déterminer le sens de variation de f sur chacun des intervalles [1,2] et [2,+∞[. b- Dresser le tableau de variation de f sur [1,+∞[. 4- a- Vérifier que pour x > 2 : $f(x)-(x-1)=\frac{-1}{\sqrt{x^2-2x}+(x-1)}$. b- Déduire que la droite Δ : y = x−1 est une asymptote oblique à C au voisinage de +∞. 5- Tracer la droite Δ et la courbe C. »

##### V- Exemples d'étude de fonction trigonométrique (p.72-73)
Encadré (verbatim) : « Soient f une fonction définie sur un domaine D. f est une fonction périodique si et seulement si il existe un réel non nul t tel que pour tout x de D on a : $x+t\in D$ et $f(x+t)=f(x)$ »
Encadré (verbatim, p.73) : « On appelle fonction tangente et on note **tg** la fonction définie sur $\mathbb{R}\setminus\{\frac{\pi}{2}+k\pi,\ (k\in\mathbb{Z})\}$ par $tg(x)=\frac{\sin(x)}{\cos(x)}$ »

**Activité 1** : « Soit la fonction $f:x\mapsto\sin(\pi x)$. 1- Montrer que la fonction f est impaire. 2- Vérifier que 2 est une période de f. 3- En déduire que l'on peut étudier f sur l'intervalle [0,1]. 4-a) Calculer f'(x) pour x ∈ [0,1]. b) Vérifier que pour tout x de [0,1] 0 ≤ πx ≤ π et en déduire le signe de f'(x) sur [0,1]. c) Dresser le tableau de variation de f sur [0,1]. 5- Tracer la courbe C₁ représentative de f sur [0,1] dans un repère orthonormé. 6- Expliquer comment tracer la courbe C de f sur IR. »

**Activité 2** : « Soit la fonction $f:x\mapsto tg(x)$. 1-a) Vérifier que la fonction f est impaire. b) Vérifier que π est une période de f. 2-a) Montrer que la fonction f est dérivable sur $[0,\frac{\pi}{2}[$ et que $f'(x)=\frac{1}{\cos^2(x)}=1+tg^2(x)$. b) Calculer $\lim_{x\to(\frac{\pi}{2})^-}f(x)$ puis dresser le tableau de variation de f sur $[0,\frac{\pi}{2}[$. 3- Donner une équation de la demi tangente à C au point d'abscisse nulle. 4- Tracer la courbe C₁ représentative de f sur $[0,\frac{\pi}{2}[$ dans un repère orthonormé $(O,\vec i,\vec j)$. 5- Expliquer comment tracer la courbe C de f sur $\mathbb{R}\setminus\{\frac{\pi}{2}+k\pi,\ (k\in\mathbb{Z})\}$. »

**Activité 3** : « Soit g la fonction définie sur $[-\pi,\pi]\setminus\{0\}$ par $g(x)=\frac{2}{1-\cos x}$. On désigne par C sa courbe représentative dans un repère orthonormé. 1- Montrer que la fonction g est paire. 2- Calculer $\lim_{x\to0^+}f(x)$ et interpréter graphiquement le résultat. 3- a- Montrer que pour tout x de ]0,π], $f'(x)=\frac{-2\sin x}{(1-\cos x)^2}$. b- Dresser le tableau de variations de f. 4- Tracer la courbe C. 5- Soit f la fonction définie sur $[-\pi,\pi]\setminus\{0\}$ par $f(x)=\frac{1+\cos x}{1-\cos x}$. a- Vérifier que pour tout x de $[-\pi,\pi]\setminus\{0\}$, f(x) = g(x) − 1. b- En déduire la représentation graphique de f. »
(Confusion f/g dans les questions 2 et 3 : coquille imprimée, voir § Notes.)

#### 3. AVEC L'ORDINATEUR (p.74-75) — macro Excel (Visual Basic)
« On se propose de créer une macro qui permet de remplir un tableau de valeurs d'une fonction qu'on programmera (sous Visual Basic pour Excel) et de représenter sa courbe. »

**Étape 1 : Définition des variables** : Dans la cellule A3 taper : « a = » ; A4 : « b = » ; A5 : « h = » ; B7 : « x » ; C7 : « y ». Définir les variables a, b et le pas h : sélectionner B3 ; menu ‘Insertion’, commande ‘nom’ puis ‘définir’ ; taper la lettre : a ; valider. Idem B4 → b ; B5 → h.

**Étape 2 : Programmation de la fonction et de la procédure de remplissage du tableau de valeurs.** « Afficher l'éditeur de code de Visual Basic et taper les lignes suivantes : »
```
Function f(x)
   f = x / (x * x + 1)     ' On peut considérer toute autre fonction
End Function

Sub calculs()
    a = Cells(3, 2)
    b = Cells(4, 2)
    h = Cells(5, 2)
    i = 8
    x = a
    Do While i <= 100      ' Effacer le contenu des 100 premières cellules
        Cells(i, 2) = ""   ' si elles ne sont pas vides
        Cells(i, 3) = ""
        i = i + 1
    Loop
    i = 8
    Do While x <= b
        Cells(i, 2) = x
        Cells(i, 3) = f(x)
        x = x + h
        i = i + 1
    Loop
End Sub
```
* « Ajouter un bouton pour lancer l'exécution de la procédure de représentation. » Choisir dans la barre des boutons le bouton « Bouton » ; s'il n'apparaît pas : Affichage/Barre d'outils… et choisir la barre d'outils Formulaire. Placer le bouton en faisant glisser la souris dans la feuille de calcul ; la fenêtre « Affecter une macro » s'ouvre : on lui affecte la procédure Calculs (capture : « Feuil1.calculs »).

**Étape 3 : Remplissage du tableau de valeurs.** « Cliquer sur le bouton ajouté et le tableau se remplit en fonction des valeurs et de la fonction choisies. » Capture : B3 = −5 (a), B4 = 5 (b), B5 = 0,1 (h) ; bouton « Button » en D4 ; tableau (x ; y) lignes 8 à 17, imprimé : −1 ; 0,5 / −0,9 ; 0,497238 / −0,8 ; 0,487805 / −0,7 ; 0,469799 / −0,6 ; 0,441176 / −0,5 ; 0,4 / −0,4 ; 0,344828 / −0,3 ; 0,275229 / −0,2 ; 0,192308 / −0,1 ; 0,09901 (valeurs de y imprimées SANS signe moins, alors que f(x)=x/(x²+1) est négative pour x<0 : voir § Notes).

**Étape 4 : Traçage de la courbe.** « Pour obtenir directement la courbe représentative de la fonction programmée : Sélectionner les cellules contenant les données x et y, à partir de la ligne 8, cliquer sur le bouton ‘Assistant graphique’ : choisir le modèle Nuages de points ; cliquer sur continuer puis sur terminer. L'avantage de ce procédé est que, si on change les bornes a, b, le pas h ou la fonction f elle-même, puis on clique sur le bouton ajouté à la feuille, le graphique est modifié directement. »

#### 4. EXERCICES ET PROBLÈMES (p.76-82) — énoncés verbatim, aucun corrigé dans le manuel

**1-** « Soit f une fonction définie sur l'intervalle ]−5,+∞[ dont le tableau de variations est donné ci-contre. Indiquer la réponse exacte parmi les réponses suivantes : Sur ]−5,+∞[, la courbe représentative de f : • Admet une seule asymptote, la droite d'équation x = −5. • Admet exactement deux asymptotes, les droites d'équations x = −5 et y = −2. • Admet exactement deux asymptotes, les droites d'équations y = −5 et x = −5. »
Tableau (imprimé, lu à 220 dpi) : x : −5 ; −3 ; « O » ; 1 ; +∞. f'(x) : + sur ]−5,−3[ ; 0 en −3 ; − ; 0 en la colonne « O » ; + ; 0 en 1 ; − sur ]1,+∞[. f(x) : −∞ (en −5) ↗ 6 (en −3) ↘ −5 (en « O ») ↗ 2 (en 1) ↘ −2 (en +∞). Le symbole « O » de la 3e colonne est un cercle, probablement le chiffre 0 : [?] (voir § Notes).

**2-** « On désigne par C la courbe représentative dans un repère orthonormé du plan de la fonction f définie sur $\mathbb{R}\setminus\{4\}$ par : $f(x)=\frac{x^2-3x+1}{x-4}$. Nier ou confirmer chacune des phrases suivantes en donnant une brève justification. a- la droite d'équation y = x+1 est asymptote oblique à C. b- la droite d'équation x = −4 est asymptote verticale à C. c- la droite d'équation x = 4 est asymptote horizontale à C. »

**3-** « Soit f une fonction définie sur un domaine D et C sa courbe représentative dans un repère orthonormé. 1- Montrer que si C est symétrique par rapport à l'axe des ordonnées alors la fonction f est paire. 2- Montrer que si C est symétrique par rapport à l'origine du repère alors la fonction f est impaire. »

**4-** « a- Tracer une courbe C représentant une fonction f définie sur IR et admettant pour asymptotes horizontales les droites d'équations y = −1 en +∞ et y = 3 en −∞. b- Tracer une courbe C représentant une fonction f définie sur IR \ {−1} et admettant une asymptote horizontale d'équation $y=-\frac12$ au voisinage de +∞ et de −∞. »

**5-** « Étudier la parité de chacune des fonctions suivantes : $x\mapsto\sqrt{x^2+1}$ ; $x\mapsto x^3-x$ ; $x\mapsto\frac{x^4+2x^2+1}{|x|}$ ; $x\mapsto\frac{\sin^2x}{x|x|}$. »

**6-** « Dans chacun des cas suivants, montrer que la droite D est un axe de symétrie pour la courbe représentative de la fonction f dans un repère orthonormé du plan. a) $f:x\mapsto x^2-2x+2$, D : x = 1 ; b) $f:x\mapsto|x^3+3x^2+x-1|$, D : x = −1 ; c) $f:x\mapsto\frac{1}{|x+2|}$, D : x = −2 ; d) $f:x\mapsto\sqrt{x(4-x)}$, D : x = 2 ; e) $f:x\mapsto\sqrt{x^2-6x}$, D : x = 3. »

**7-** « Dans chacun des cas suivants, montrer que le pt I est un centre de symétrie pour la courbe représentative de la fonction f dans un repère orthonormé du plan. a) $f:x\mapsto\frac{2x-1}{x-3}$, I(3, 2) ; b) $f:x\mapsto\frac{x^2+x-1}{x-1}$, I(1, 3) ; c) $f:x\mapsto\sqrt{1-x^2}-\sqrt{2x-x^2}$, $I(\frac12, 0)$. »

**8-** « Pour chacune des fonctions suivantes : a- Déterminer l'ensemble de définition. b- Calculer les limites de f aux bornes de cet ensemble. c- Déduire l'existence d'asymptotes à la courbe de f, qui soient parallèles aux axes des coordonnées et donner leurs équations. $f(x)=\frac{x-5}{2x+3}$ ; $f(x)=\frac{2x}{x^2-x-12}$ ; $f(x)=\frac{4x^2-2x-2}{x-1}$ ; $f(x)=\frac{x^2-x-1}{-2x^2+5x-3}$ »

**9-** « Soit la fonction f définie sur IR par $f(x)=\frac{x^3-2}{x^2+1}$. a- Montrer que la droite D : y = x est asymptote à la courbe C de f au voisinage de −∞ et de +∞. b- Étudier la position relative de C et D. »

**10-** « Soit la fonction f définie sur ]−2,+∞[ par $f(x)=\frac{x^2-4x-10}{2x+4}$. On désigne par C sa courbe représentative dans le plan muni d'un repère $(O,\vec i,\vec j)$. a- Déterminer les réels a, b et c tels que $f(x)=ax+b+\frac{c}{2x+4}$ pour tout x de ]−2,+∞[. b- Calculer $\lim_{x\to+\infty}[f(x)-(ax+b)]$, interpréter graphiquement le résultat. c- Étudier la position relative de C par rapport à la droite D : y = ax+b. »

**11-** « Soit f la fonction définie sur ]1,+∞[ par $f(x)=\frac{-2x^3+x^2+2x+1}{x^2-1}$. On note C_f sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$ du plan. 1- Étudiez les limites de la fonction f aux bornes de son intervalle de définition. 2- Déterminez les réels a, b et c tels que $f(x)=ax+b+\frac{c}{x^2-1}$. 3- a- Soit D la droite d'équation y = −2x+1. Montrez que D est asymptote à la courbe C_f au voisinage de +∞. b- Préciser la position relative de C_f par rapport à la droite D. 4- La courbe C_f admet une deuxième asymptote. Quelle est son équation ? 5- On donne le tableau de variation de la fonction f [x : 1 ; +∞ ; f'(x) : « − » ; f(x) : flèche décroissante, valeurs aux bornes non imprimées] a- Compléter le tableau avec les limites trouvées. b- Montrez que l'équation f(x) = 0 admet une solution unique α et que α ∈ [1,4 ; 1,5]. 6- Construire la courbe C_f. »

**12-** « Soit f la fonction définie sur IR par $f(x)=\frac13x^3+x^2-3x-4$. On note C_f sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$ du plan. 1- Vérifier que C_f admet un centre de symétrie dont-on donnera les coordonnées. 2- Étudier les branches infinies de C_f. 3- Dresser le tableau de variations de f. 4- Tracer la courbe C. 5- Montrer que l'équation f(x) = 6 admet une solution unique α et que α ∈ ]3,4[. 6- a- Tracer dans le même repère la courbe représentative de la fonction g : x ↦ |f(x)|. b- Justifier que l'équation (E) : g(x) = 6 admet exactement deux solutions dont l'une est α. c- Donner une valeur approchée de l'autre solution de (E) au dixième près. »

**13-** « Soit f la fonction définie sur IR \ {−1,1} par $f(x)=\frac{x^2+1}{(x^2-1)^2}$. On donne le tableau de variations de f » [tableau imprimé : x : −∞ ; −1 ; « O » ; 1 ; +∞ ; f'(x) : + ; + ; (0 en « O ») ; − ; − ; f(x) : « O » ↗ +∞ | +∞ ↘ −1 ↗ +∞ | +∞ ↘ « O »]. « 1- a- Calculer f'(x) et justifier le signe de f'(x) donné dans le tableau. b- Justifier la limite de f en +∞. Lire sur le tableau de variation le signe de f(x) selon les valeurs de x. c- Tracer la courbe représentative de f ainsi que ses asymptotes dans un repère orthonormé $(O,\vec i,\vec j)$ du plan. 2- F, G et H sont des primitives de f respectivement sur ]−∞,−1[, ]−1,1[ et ]1,+∞[. a- Déterminer le sens de variation de F, de G et de H sur chacun de leurs intervalles de définition. b- Vérifier que pour tout x ∈ IR \ {−1,1} on a $f(x)=\frac{1}{2(x-1)^2}+\frac{1}{2(x+1)^2}$. c- En déduire l'expression de chacune des fonctions F, G et H sur chacun de leurs intervalles de définition. d- Dresser le tableau de variation de F, G et de H. e- Tracer les courbes représentatives de F, G et de H dans le même repère orthonormé. »
(Le tableau imprimé est incohérent avec f : voir § Notes.)

**14-** « Soit f la fonction définie sur IR par $f(x)=|x^2-3x-4|-x$. On désigne par C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. 1- Étudier la dérivabilité de f en −1 et en 4 ; interpréter graphiquement le résultat. 2- Dresser le tableau de variations de f. 3- Tracer la courbe C ainsi que les demi tangentes aux points d'abscisses −1 et 4. »

**15-** « Soit f la fonction définie sur ]−1,+∞[ par $f(x)=\left|\frac{x-1}{x+1}\right|$. On désigne par C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. 1- Étudier la dérivabilité de f en 1 et préciser les demi tangentes à C au point d'abscisse 1. 2- Déterminer les asymptotes à C. 3- Tracer la courbe C et ses deux asymptotes. »

**16-** « Étudier les variations de chacune des fonctions suivantes sur son domaine de définition puis tracer sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$ : a) $f:x\mapsto x^2-2x+1$ ; b) $f:x\mapsto\frac13x^3+\frac12x^2+x-2$ ; c) $f:x\mapsto 2x^3+x-1$ ; d) $f:x\mapsto x^4-2x^2+1$ ; e) $f:x\mapsto\frac{x-1}{x+2}$ ; f) $f:x\mapsto\frac{x^2-1}{x+2}$ ; g) $f:x\mapsto\frac{1}{x^2+2x}$ ; h) $f:x\mapsto\frac{x}{x^2-2x+1}$ ; i) $f:x\mapsto\frac{x^2+1}{x^2+2x+1}$. »

**17- (fonction de satisfaction, envie, rejet)** « En économie, on appelle fonction de satisfaction toute fonction S définie sur un intervalle I et à valeurs dans l'intervalle [0,100] et appelle fonction envie la dérivée E de fonction S. On dit qu'il y a envie lorsque E est positive et qu'il y a rejet lorsque E est négative.
Situation 1 : La fonction de satisfaction S est représentée par le graphique ci-contre [parabole inversée : S(0)=0, sommet S=100 en x=5, S(10)=0 ; graduations 10, 75, 100 en ordonnée, 1, 5, 10 en abscisse]. 1- Justifier que S est dérivable sur [0,10]. 2- Pour quelle valeur de x la satisfaction est-elle maximale ? 3- Sur quel(s) intervalle(s) y'a-t-il envie ? y a-t-il rejet ? 4- Exprimer E(x) en fonction de x sachant que E est une fonction affine définie sur [0,10] et que E(0) = 50.
Situation 2 : La fonction envie E pour un salaire dans une petite entreprise est modélisée par $E(x)=\frac{100}{(x+1)^2}$ où x ≥ 0 et désigne le salaire annuel d'un employé en milliers de dinars. 1- Déterminer la fonction de satisfaction S sachant que S(0) = 0. 2- Représenter graphiquement la fonction S dans un repère orthogonal $(O,\vec i,\vec j)$ (On prendra pour unités : 3cm pour 10 unités sur l'axe des abscisses et 1cm pour 10 unités sur l'axe des ordonnées). 3- Cette entreprise estime qu'un employé est satisfait, si S prend une valeur supérieure ou égale à 75. Que devrait alors être la valeur minimale du salaire d'un employé satisfait ? »

**18-** « Soit f la fonction définie sur [1,+∞[ par $f(x)=\sqrt{x^2+x-2}$. On désigne par C sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. 1- a- Calculer les limites suivantes : $\lim_{x\to+\infty}f(x)$ ; $\lim_{x\to+\infty}\frac{f(x)}{x}=a$ ; $\lim_{x\to+\infty}[f(x)-ax]=b$ ; $\lim_{x\to+\infty}[f(x)-(ax+b)]$. b- En déduire l'existence d'une droite D asymptote à C au voisinage de +∞. c- Étudier la position relative de C et D. 2- Étudier la dérivabilité de f à droite en 1 ; interpréter graphiquement le résultat. 3- Dresser le tableau de variation de f. 4- Tracer la courbe C. »

**19-** « Étudier les variations de chacune des fonctions suivantes sur l'ensemble I puis tracer sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. a) $x\mapsto\sqrt{-x+1}$, I = ]−∞,1] ; b) $x\mapsto x-\sqrt{x-4}$, I = [4,+∞[ ; c) $x\mapsto\sqrt{x^2-x}$, I = ]−∞,0]∪[1,+∞[ ; d) $x\mapsto x-\sqrt{x^2-4}$, I = ]−∞,−2]∪[2,+∞[. »

**20-** « Étudier les variations de chacune des fonctions suivantes sur l'intervalle I puis tracer sa courbe représentative dans un repère orthonormé $(O,\vec i,\vec j)$. a) $x\mapsto\sin(2x-\frac{\pi}{4})$, I = [−π,π] ; b) $x\mapsto\cos(2\pi x+1)$, I = [0,3] ; c) $x\mapsto tg(2x)$, $I=]-\frac{\pi}{4},\frac{\pi}{4}[$ ; d) $x\mapsto\sin^2(x)$, I = IR. »

**21- (placement : versements annuels et livret à intérêts composés)** « Un investisseur a versé chaque 1er janvier pendant 5 années consécutives une somme S = 1000 DT, investie en construction de bâtiments. Il constate qu'au terme des 5 années, son avoir est de A = 6000 DT. Afin de comparer cette performance avec celle d'un livret classique à intérêts composés annuels, il déterminer le taux de rémunération du livret pour obtenir le même résultat. Désignons par t le taux (en %) cherché.
A- 1- Quel est le bénéfice total réalisé ? 2- Quel est alors le bénéfice moyen annuel réalisé ? 3- Que serait alors la valeur de t ? 4- Ce résultat est-il réaliste ?
B- 1- Augmenter une somme de t%, revient à la multiplier par T. Déterminer T en fonction de t. 2- En supposant que les investissements se soient faits sur un livret à t% annuel, montrer que l'avoir à la fin de la 1ère année serait 1000T et que l'avoir à la fin de la 2ième année serait 1000T + 1000T². 3- Déterminer l'avoir à la fin de la 5ième année. 4- Vérifier alors que le taux est déterminé par résolution de l'équation $x+x^2+x^3+x^4+x^5=6$.
C- Soit f la fonction définie sur [0,+∞[ par $f(x)=x+x^2+x^3+x^4+x^5$. 1- a- Vérifier que f'(x) > 0 pour tout x de [0,+∞[. b- Dresser le tableau de variations de f. c- Tracer la courbe représentative de la fonction f dans un repère orthonormé du plan. 2- Déterminer le nombre de solutions sur [0,+∞[ de l'équation (E) : $x+x^2+x^3+x^4+x^5=6$. 3- Encadrer strictement T entre deux entiers consécutifs, en le justifiant. 4- Donner un encadrement de T à $10^{-4}$ près. 5- En déduire la valeur de t au dixième de points près. »

**22-** « Soit f la fonction définie sur IR par $f(x)=1+\frac{2x-1}{(x^2-x+1)^2}$. 1- Vérifier que $f'(x)=\frac{-6x(x-1)}{(x^2-x+1)^3}$ pour tout x de IR. 2- En déduire le sens de variation de f suivant les valeurs de x. (On déterminera le signe de l'expression x²−x+1). 3- Vérifier que la courbe C de f admet une asymptote horizontale dont-on donnera une équation. 4- Dresser le tableau de variations de f. 5- Tracer la courbe représentative de f dans un repère orthonormé $(O,\vec i,\vec j)$. 6- Soit la fonction $F:x\mapsto x+1-\frac{1}{x^2-x+1}$. a- Montrer que F est la primitive de f sur IR, qui s'annule en 0. b- Dresser le tableau de signe de f ; en déduire les variations de F. c- Montrer que la droite D d'équation y = x + 1 est une asymptote oblique la courbe C' de F aux voisinages de −∞ et +∞. d- Étudier la position relative de C' et D. e- Tracer la droite D et la courbe C' dans un repère orthonormé du plan. »

**23- (Prix d'équilibre d'offre et de demande)**
Partie A : « Soit g la fonction définie sur ]−5 ;+∞[ par : $g(x)=\frac{9}{x+5}-0,05x+4$. On désigne par C sa courbe représentative dans un repère orthogonal $(O,\vec i,\vec j)$. 1- Calculer la limite de g en −5. En donner une interprétation graphique. 2- a- Calculer la limite de g en +∞. Montrer que la droite D d'équation y = −0,05x + 4 est asymptote oblique à la courbe C au voisinage de +∞. b- Étudier la position relative de C par rapport à la droite D. 3- Calculer g'(x) et étudier son signe. 4- Dresser le tableau de variations de g sur ]−5 ;+∞[. 5- Tracer les asymptotes ainsi que la courbe C. (Prendre pour unités graphiques : 0,5 cm sur l'axe des abscisses et 2 cm sur l'axe des ordonnées). »
Partie B : « Soit f la fonction définie sur IR par : $f(x)=4,5-\frac{6x^3+24x^2+36x+18}{(x^2+2x+2)^2}$. On désigne par C_f sa courbe représentative dans le même repère orthogonal $(O,\vec i,\vec j)$. 1- Calculer les limites de f en −∞ et +∞. En donner une interprétation graphique. 2- a- Vérifier que $f'(x)=\frac{6x(x+2)^3}{(x^2+2x+2)^3}$. b- Étudier les variations de f sur IR. (on précisera les extremums). 3- Représenter la courbe C_f dans le repère précédent.
x désignant le prix d'une unité de produit, exprimé en dinars. On admet que la quantité offerte sur le marché et la quantité demandée exprimées en milliers d'articles sont modélisées sur l'intervalle [0 ; 20] : – pour la fonction d'offre par : $f(x)=4,5-\frac{6x^3+24x^2+36x+18}{(x^2+2x+2)^2}$ ; – pour la fonction de demande par : $g(x)=\frac{9}{x+5}-0,05x+4$. (Les courbes représentatives des fonctions d'offre et de demande sont données ci-dessous) [graphique p.82 : axes « milliers d'articles » (0 à +6) et « prix unitaire en dinars » (0 à +20) ; offre croissante de 0 à ≈4,05 ; demande décroissante de +6 vers ≈3,4 en x=20 ; intersection vers x≈12-13, ordonnée ≈3,9]. 1- Soit la fonction p définie sur [0 ; 20] par p(x) = f(x) − g(x). À l'aide des résultats établis dans les parties A et B. a) Étudier le sens de variation de p. b) Prouver que l'équation p(x) = 0 admet une unique solution x₀. 2- Déduire de ce qui précède l'arrondi au 10⁻² de dinars près du prix d'équilibre, ainsi que le nombre d'objets proposés sur le marché à ce prix. »

#### 5. MATH CULTURE (p.83) — « Offre et demande » (aucune source citée dans le manuel ; p.84 blanche)
- L'offre est la quantité d'un bien économique que les producteurs souhaitent vendre à un prix donné. Principaux déterminants : le prix du marché et les coûts de production. Courbes représentatives généralement croissantes et concaves.
- La demande est la quantité voulue d'un bien, à un prix donné, par les consommateurs ayant les moyens de l'acheter. La courbe décrit cette quantité (en abscisses) en fonction du prix (en ordonnées). Déterminants : le prix du bien, le revenu, les goûts, mais aussi l'offre et la demande des biens de substitutions. Courbe généralement décroissante, concave ou convexe selon les cas.
- [R7 : phrase omise, verbatim] « En construisant les deux courbes, ou dans un cas plus simple les deux droites, on obtient la situation du marché. La rencontre de l'offre et de la demande permet de définir le point d'équilibre. Ce point définit le prix pour lequel l'offre égalise la demande, c'est-à-dire le point où se réalise l'échange. »
- Point d'équilibre : intersection des deux courbes ; coordonnées = « prix d'équilibre » et « quantité d'équilibre ». Tant que ce point n'est pas atteint, l'excédent d'offre provoque la baisse du prix ou la trop forte demande provoque sa montée.
- Encadré rouge : « Dans la théorie microéconomique, l'offre et la demande sont fonctions du prix (noté en ordonnées par convention) mais n'interagissent pas l'une sur l'autre. »
- L'évolution de la demande se représente par une translation de la courbe de demande vers la droite : D0 remplacée par D1 ; hausse du prix d'équilibre de P0 à P1 et de la quantité d'équilibre de Q0 à Q1. Inversement si la demande diminue : quantité échangée et prix décroissent.
- Deux figures : (1) offre croissante (trait plein) / demande décroissante (pointillés), axes Prix (ordonnée) et Quantité (abscisse), point d'équilibre (P, Q) ; (2) deux demandes D0 et D1 (D1 à droite), équilibres (Q0,P0) et (Q1,P1).

#### 6. VOCABULAIRE OFFICIEL
asymptote horizontale / verticale / oblique ; branche parabolique (de direction l'axe des abscisses / des ordonnées / la droite y = ax) ; branches infinies ; axe de symétrie ; centre de symétrie ; point d'inflexion ; fonction paire / impaire / périodique ; période ; fonction tangente tg ; demi-tangente ; tableau de variation ; position relative ; coût de production, recette, bénéfice, coût moyen $C_m$ / $C_M$, coût marginal, coûts fixes ; fonction de satisfaction, fonction envie (E = S'), envie / rejet ; fonction d'offre, fonction de demande, prix d'équilibre, quantité d'équilibre ; taux de rémunération, intérêts composés.

**Bornes INCLUS** (présents dans les activités du chapitre) : asymptotes horizontale/verticale/oblique, branches paraboliques, parité, symétrie (axe x = a, centre I(a,b)), translations $k\vec j$ et $k\vec i$, études complètes de polynômes (degré 3, 4), de fractions rationnelles, de fonctions avec racines carrées (y compris |2x−x²| sous racine et valeur absolue), de sin(πx), tg(x), 2/(1−cos x), |f|, primitives de fractions simples (ex.13, 22), applications économiques (coût, recette, bénéfice max, coût moyen min, coût marginal, satisfaction/envie, offre/demande), équation f(x)=k à solution unique et encadrement, dérivabilité à droite et demi-tangentes, macro Excel/VBA.
**Bornes EXCLU** (absentes de la tranche) : étude de fonctions avec ln ou exp (chapitre IV), intégrale (chapitre V) ; asymptote oblique pour fonctions trigonométriques ; théorème des valeurs intermédiaires non énoncé en encadré dans ce chapitre (utilisé seulement dans les exercices 11, 12, 21, 23 sans énoncé) ; aucun corrigé ; convexité formelle (hors Math culture : « concave/convexe » seulement cité dans la rubrique).

**Notions-clés (≤ 8)** : (1) asymptotes (verticale, horizontale, oblique : définitions par limites) ; (2) branches paraboliques (direction Ox, Oy, droite y=ax) ; (3) centre de symétrie I(a,b) : f(2a−x)=2b−f(x) ; (4) axe de symétrie ; (5) plan d'étude complet (domaine, parité/période, limites, dérivée, tableau, asymptotes, tracé) ; (6) translations de courbes (f+k, f(x−k)) et courbe de |f| ; (7) coût moyen minimal / bénéfice maximal / coût marginal ; (8) offre-demande, prix d'équilibre, fonction de satisfaction et envie.

#### 7. § NOTES

**Pages lues** : 22/22 (63 à 84), toutes à l'image (110 dpi) et au texte (pdftotext). p.63 : page de titre, texte vide (image lue). p.84 : blanche (texte vide, image lue : blanche).
**Pages sondées à l'agrandissement (170-220 dpi)** : p.67 (encadré branche parabolique), p.75 (tableau Excel), p.76 (tableau de variations de l'ex.1), p.77 (tableau de l'ex.11), p.78 (tableau de l'ex.13).
**Coquilles / incohérences imprimées (reproduites telles quelles)** :
1. p.67 : numérotation des activités « 1, 2, 4 » (pas d'Activité 3 ; l'encadré 2 est à sa place). Encadré 2 : les deux demi-lignes portent « x→+∞ » (la 2e devrait être −∞).
2. p.69 Activité 1 (rationnelle) : après 5-, le sujet repart sur « 4- Soit la fonction g… » (numérotation répétée : devrait être 6-).
3. p.70-71 Activité 3 : $C_M$ définie sur ]0,15] mais tableau demandé « sur [0,15] ». Activité 2 : « f(−3) » à calculer ; texte brut dégrade en f(3), l'image fait foi : f(−3).
4. p.73 Activité 3 : la fonction est g (g(x)=2/(1−cos x)), mais les questions 2 et 3 écrivent « f » (lim f, f'(x)) ; la question 5 redéfinit f. Aussi « ]0,π] » pour x en 3-a, et lim en 0⁺.
5. p.68 Activité 1 encadré : « translation de vecteur $k\vec j$ » ; p.69 : « translation de vecteur $k\vec i$ » pour x ↦ f(x−k) (tel qu'imprimé).
6. p.76 Ex.2 b : « x = −4 asymptote verticale » alors que f est définie sur ℝ∖{4} (piège voulu ou coquille : non tranché) ; c : « x = 4 asymptote horizontale ».
7. p.76 Ex.1 et p.78 Ex.13 : symbole « O » (cercle) dans la ligne x et aux bornes de f : lu comme 0, noté [?]. Ex.13 : le tableau imprimé donne f' : + , + , 0, − , − et f : ↗ +∞ | +∞ ↘ −1 ↗ +∞ | +∞ ↘ 0 ; or [R7 : recalcul du lecteur, non imprimé ; vérifié par l'auditeur] pour f(x)=(x²+1)/(x²−1)² on a f(0)=1 (et non −1) et f'(x) = −2x(x²+3)/(x²−1)³ de signes +, −, +, − : le tableau est incohérent avec la fonction (signes de f' et valeur du minimum). L'exercice demande pourtant « justifier le signe de f'(x) donné dans le tableau » : conflit énoncé / calcul.
8. p.77 Ex.7 a : I(3,2) et p.77 Ex.8 : fonctions transcrites telles quelles. Ex.7 c : I(1/2, 0).
9. p.75 tableau Excel : y imprimé positif pour x négatif (ex. −0,9 → 0,497238), alors que f(x)=x/(x²+1) donne −0,497238 ; le manuel imprime y sans signe ; −0,1 → 0,09901 imprimé. Le texte de code VBA : « a, b, h, i, x » non déclarés (imprimé tel quel) ; commentaire « 100 premières cellules » ; fonction par défaut f(x)=x/(x*x+1).
10. p.80 Ex.21 : « il déterminer » (faute imprimée), « B-2- … 1000T + 1000T² » ; p.81 : « les voisinages de −∞ et +∞ », « dont-on » (formes imprimées).
11. p.69 Activité 3 (p.68-69) : « 84 milles dinars la tonne » et « 100 milles dinars » (« milles » imprimé pour « milliers »).
12. p.82 Partie B de l'Ex.23 : la définition de f est donnée deux fois (au début de la partie B et dans l'énoncé du marché) ; texte « Étude des variations de f sur IR (on précisera les extremums) ».
**`[?]` restants** : x = « O » des tableaux Ex.1 et Ex.13 (cercle lu 0) ; valeurs numériques de la lecture graphique des figures (non transcrites) ; aucune formule illisible par ailleurs.
**Figures** : les courbes des Activités 1-4 de « Pour commencer », de l'activité 1/2 de « Revoir », et de l'Ex.17/23 sont décrites qualitativement ; leurs coordonnées exactes se lisent sur le quadrillage et n'ont pas été inventées.

---

### Chapitre `m04-p85-114`

### m04 — Chapitre IV « Fonction logarithme népérien — Fonctions exponentielles » (pp. 85-114)

Source : manuel officiel CNP « Mathématiques », 4e année secondaire, section économie et gestion (222463P00.pdf). Page PDF = page imprimée. Tranche lue : pp. 85-114.

Plan annoncé p.85 : Pour commencer · Fonction Logarithme Népérien (Définition, Propriétés, Étude et représentation graphique) · Fonction exponentielle de base e (Définition, Propriétés, Étude et représentation graphique, Fonction x ↦ a^x avec a > 0) · Avec l'ordinateur · Exercices et problèmes · Math culture.

Notation : intervalle ouvert « ]0,+∞[ » (imprimé avec crochets inversés dans le manuel) ; ℝ = IR ; tg = tangente.

---------------------------------------------------------------------
#### POUR COMMENCER (p.86)
---------------------------------------------------------------------

##### Pour commencer — Activité 1 (p.86)
Soit f la fonction définie sur ]−1,+∞[ par f(x) = (x² + 2x)/(x+1)².
1- Vérifier que la fonction F, définie sur ]−1,+∞[ par F(x) = x²/(x+1) [imprimé « f (x) » au lieu de F(x), coquille], est une primitive de f.
2- Donner la primitive G de f qui prend la valeur 2 en 1.
(Aucun corrigé donné.)

##### Pour commencer — Activité 2 (p.86)
On donne dans le graphique suivant les courbes représentatives de deux fonctions f et g définies sur ]0,+∞[.
Graphique : C_f (bleue) croissante, passe par (1 ; 0), négative sur ]0,1[, tend vers −∞ en 0+, atteint environ 2 vers x≈6 (axe : graduations 1, 2, 3 en abscisse, −1, 1, 2 en ordonnée). C_g (rose) décroissante, tend vers +∞ en 0+, positive, tend vers 0 en +∞ ; les deux courbes se coupent vers x≈1,7 (ordonnée ≈ 0,5).
1) Déterminer graphiquement selon les valeurs de x le signe de f(x) et de g(x).
2) Sachant que l'une des deux fonctions est une primitive de l'autre, Reconnaître parmi les deux affirmations suivantes, celle qui est vraie
 • f est une primitive de g.
 • g est une primitive de f.
(Aucun corrigé donné.)

##### Pour commencer — Activité 3 (p.86)
Soient n un entier naturel non nul et f la fonction définie sur ]0,+∞[ par f(x) = 1/xⁿ.
1- Montrer que f possède une primitive sur ]0,+∞[.
2- Pour n supérieur ou égal à deux, déterminer la primitive de f qui s'annule en 1.
3- Peut-on faire de même pour n = 1 ?
(Aucun corrigé donné.)

---------------------------------------------------------------------
#### COURS — A- FONCTION LOGARITHME NÉPÉRIEN
---------------------------------------------------------------------
##### 1) Définition (p.87)

**Activité 1** — On considère la fonction f définie sur ]0,+∞[ par f(x) = 1/x.
Parmi les trois courbes ci-dessous, une seule représente une primitive F de f sur ]0,+∞[.
(Figure : trois graphiques. [R7 : description refaite à l'image 260 dpi] 1er graphique : courbe croissante concave passant par (1 ; 0), asymptote verticale en 0, tangente en (1 ; 0) en pointillé de coefficient directeur 1 (passe par (0 ; −1) et (2 ; 1)). 2e graphique : courbe décroissante convexe passant par (1 ; 0), tangente en ce point de coefficient directeur −1 (passe par (0 ; 1)). 3e graphique : courbe croissante concave passant par (1 ; 0), asymptote verticale en 0, tangente (bleue) en (1 ; 0) de coefficient directeur ≈ 1/2 (passe par (0 ; −0,5) et (3 ; 1)). Le manuel ne donne pas de corrigé.)
1- Calculer f(1) et reconnaître la courbe de F.
2- Préciser F(1).
3- Préciser le sens de variation de F.
4- Montrer graphiquement qu'il existe un unique réel x0 tel que F(x0) = 1.

Texte : « f est continue sur l'intervalle ]0,+∞[ donc elle admet une primitive sur cet intervalle. La primitive de f qui s'annule en 1 est une nouvelle fonction appelée *Fonction logarithme népérien*. »

**Définition (encadré)** : La fonction *logarithme népérien*, notée ln( ou Log), est la primitive sur ]0,+∞[ de la fonction x ↦ 1/x qui s'annule en 1.

**Remarque (encadré)** : On adoptera la notation courante ln.
 ln : ]0,+∞[ → ℝ ; x ↦ ln x

**Conséquences immédiates (encadré)** :
 1) ln(1) = 0
 2) La fonction ln est continue et dérivable sur ]0,+∞[ et pour tout x > 0 (ln)'(x) = 1/x
 3) La fonction ln est strictement croissante sur ]0,+∞[ et on a : x1 > x2 > 0 équivaut à ln(x1) > ln(x2)

##### 1) Définition — suite (p.88-89)

**Activité 2** (p.88)
1- Montrer que :
 ln(x) < 0 équivaut à 0 < x < 1
 ln(x) > 0 équivaut à x > 1
2- Soient x et y deux réels strictement positifs, prouver que : ln(x) = ln(y) équivaut à x = y

**Activité 3** (p.88) Déterminer l'ensemble de définition de chacune des fonctions suivantes :
 f : x ↦ (ln x)/(x+2) [R7 : parenthésage levé à l'image] ; g : x ↦ ln((x+2)/(x−2)) ; h : x ↦ 1/ln(x²+1) ; k : x ↦ ln(x+2) − ln(x−2)

**Activité 4** (p.88)
1) Soient u et f les fonctions définies sur IR par u(x) = x² − x + 3 et f(x) = ln|u(x)|
 a- Vérifier que pour tout x de IR, u(x) > 0
 b- Montrer que f est dérivable sur IR et que f'(x) = u'(x)/u(x).
2) Soient v et g les fonctions définies sur ]1,+∞[ par v(x) = 1/x − 1 et g(x) = ln|v(x)|
 a- Prouver que pour tout x de ]1,+∞[ on a v(x) < 0.
 b- Montrer que g est dérivable sur ]1,+∞[ et que g'(x) = v'(x)/v(x).

**Théorème (admis) (encadré)** : Si une fonction u est dérivable sur un intervalle ouvert I et si pour tout x de I, u(x) ≠ 0 alors la fonction f : x ↦ ln|u(x)| est dérivable sur I et sa fonction dérivée est définie par : f'(x) = u'(x)/u(x).

**Remarque (encadré)** : Lorsque u est une fonction dérivable sur un intervalle I et qui ne s'annule pas sur I, une primitive sur I de la fonction x ↦ u'(x)/u(x) est la fonction x ↦ ln|u(x)|.

**Activité 5** (pp.88-89)
1- Pour chacun des cas suivants, justifier que la fonction f est dérivable sur l'intervalle I puis définir sa fonction dérivée f'.
 a) f(x) = ln(x²/2) ; I = ]0,+∞[
 b) f(x) = ln((1−x)/(x+2)) ; I = ]−2,1[
 c) f(x) = ln|2/x + x| ; I = ]0,+∞[
 d) f(x) = ln|ln x| ; I = ]0,1[
2- Déterminer une primitive de f sur l'intervalle I
 a) f(x) = 2x/(x²+1) ; I = ℝ
 b) f(x) = (4x³+2x)/(x⁴+x²) ; I = ]0,+∞[
 c) f(x) = (2+3√x)/(x+x√x) ; I = ]0,+∞[
 d) f(x) = −tg(x) ; I = ]−π/2 , π/2[

##### 2) Propriété fondamentale (p.89-90)

**Activité 1** (p.89) — Soit a un réel strictement positif, on considère les fonctions f et g définies sur ]0,+∞[ par f(x) = ln(ax) et g(x) = ln(x) + ln(a).
a- Montrer que f et g sont deux primitives sur ]0,+∞[ de la fonction x ↦ 1/x.
b- Calculer f(1) et g(1).
c- Déduire que : pour tout x ∈ ]0,+∞[ f(x) = g(x)

**Propriété (encadré)** : Pour tous réels strictement positifs a et b on a : ln(a b) = ln(a) + ln(b)

**Activité 2** (p.89)
1) Soit a,b et c trois réels strictement positifs, montrer que : ln(abc) = ln(a) + ln(b) + ln(c).
2) Soit a un nombre réel strictement positif, montrer par récurrence que pour tout entier naturel n on a : ln(aⁿ) = n ln(a).

**Activité 3** (p.89) Parmi les réponses a, b et c retrouver celles qui sont correctes :
| Expression | a | b | c |
|---|---|---|---|
| ln(2)+ln(9) = | ln(11) | ln(18) | ln(6)+ln(3) |
| ln(27) = | 3ln(3) | 9ln(3) | ln(9)+ln(3) |
| ln(108)+ln(2) | ln(110) | ln(216) | 3ln(6) |
| ln(24) + 2 ln(5) = | ln(600) | 2 ln(12) + ln(25) | ln(6)+2ln(10) |
| Pour x > 0, ln x + ln(1/x) = | ln((x+1)/x) | 0 | 1 |
| Pour x > 0, ln(x² + 6x + 9) = | ln(x²) + 6 ln(x) + ln(9) | ln(x+3)² | 2 ln(x+3) |
| Pour x > 0, ln(x) + ln(x+1) = | ln(x) . ln(x+1) | ln(x² + x) | ln(x²) + ln(x) |
(Plusieurs réponses peuvent être correctes par ligne ; aucun corrigé donné.)

**Activité 4** (p.90)
1) Résoudre dans ℝ les équations :
 a) ln x + ln(x+1) = ln(6) ; b) ln(x−1) + ln(2+x) = ln(x²)
2) Résoudre dans ℝ les inéquations :
 a) ln(2x+2) > ln(x+5) ; b) ln(x−2) ≤ ln(3x+6).

**Activité 5** (p.90) Soient a et b deux réels strictement positifs.
 1. Calculer ln(a) + ln(1/a) et en déduire que ln(1/a) = −ln a.
 2. Calculer ln(a/b) + ln b et en déduire que ln(a/b) = ln a − ln b.
 3. Sachant que (√a)² = a prouver que ln √a = (1/2) ln a.

**Propriétés (encadré)** :
 1- Pour tout réel on a : ln(1/a) = −ln(a).  [imprimé « Pour tout réel », sans « a > 0 » : imprécision du manuel]
 2- Pour tous réels a > 0 et b > 0 on a : ln(a/b) = ln(a) − ln(b).
 3- Pour tout réel a > 0 on a : ln(√a) = (1/2) ln(a).

**Activité 6** (p.90) On sait que pour tout entier naturel n et pour tout réel a strictement positif on a : l'égalité (E) : ln(aⁿ) = n ln(a). On suppose que n est un entier relatif inférieur ou égal à −1, en écrivant aⁿ = 1/a^(−n) vérifier que l'égalité (E) reste vraie. (on remarquera que (−n) ∈ ℕ).
« Ainsi : » **(encadré)** Pour tout a > 0 et tout n ∈ ℤ : ln(aⁿ) = n ln(a)

**Activité 7** (pp.90-91)
1) On donne ln 2 ≃ 0,7 et ln 3 ≃ 0,1 [valeur imprimée ; incohérente avec la réalité (ln 3 ≈ 1,1) : coquille du manuel, voir § Notes]
 Donner une valeur approchée de chacun des réels A et B :
 A = 4 ln(1/2) + 3 ln(2) + ln(8) ; B = ln(4/5) − 3 ln(3) + ln(10)
2) Sans utiliser une calculatrice, comparer les réels x et y dans chacun des cas suivants :
 a) x = 3 ln(2) et y = 2 ln(3) ; b) x = ln(5) − ln(2) et y = ln(12) − ln(5)
3) a, b et c sont trois réels strictement positifs tels que : ln a = ln(b/2) = 3 et ln c = −2
 Calculer le réel D = ln(16a³c²/b⁴).

##### 3) Étude de la fonction ln (pp.91-92)

**Activité 1** (p.91)
1) Montre que si la fonction ln est majorée alors elle admet une limite finie ℓ lorsque x tend vers +∞.
2) Prouver que lim_{x→+∞} [ln(2x)] = ℓ
3) En écrivant ln(2x) = ln x + ln 2 déduire que l'hypothèse faite en 1) entraîne ln2 = 0. Déduire que lim_{x→+∞} ln x = +∞
4) En écrivant ln(1/x) = −ln x, montrer que lim_{x→0+} ln x = −∞

**Théorème (encadré)** : lim_{x→+∞} ln x = +∞ et lim_{x→0+} ln x = −∞

**Activité 2** (p.91) On considère la fonction g définie sur ]0,+∞[ par g(x) = √x − ln x.
1- Vérifier que g est dérivable sur ]0,+∞[ et que g'(x) = (√x − 2)/(2x).
2- Déterminer le sens de variation de g sur ]0,+∞[.
3- Montrer que pour tout x > 0 √x > ln x et en déduire que : pour tout x > 1 on a : 0 ≤ ln x / x ≤ 1/√x
4- En déduire que lim_{x→+∞} (ln x)/x = 0 et lim_{x→+∞} (ln x)/xⁿ = 0 (n entier supérieur ou égal à 2).
5- a- Montrer que pour tout réel strictement positif x on a : x ln(x) = − ln(1/x)/(1/x)
 b- En déduire que lim_{x→0+} x ln x = 0 et lim_{x→0+} xⁿ ln x = 0 (n entier supérieur ou égal à 2)

**Théorème (encadré)** :
 • lim_{x→+∞} (ln x)/x = 0 ; lim_{x→0+} x ln x = 0
 • Pour tout n ∈ ℕ* lim_{x→+∞} (ln x)/xⁿ = 0 et lim_{x→0+} xⁿ ln x = 0

##### 3) Étude de la fonction ln — suite (p.92)

**Activité 3 (Autres limites)** (p.92)
a) En considérant le nombre dérivé de la fonction ln en 1, montrer que lim_{x→1} (ln x)/(x−1) = 1
b) En déduire que lim_{x→0} ln(1+x)/x = 1

**Théorème (encadré)** : lim_{x→1} (ln x)/(x−1) = 1 et lim_{x→0} ln(1+x)/x = 1

**Activité 4** (p.92) On désigne par Γ la courbe représentative de la fonction ln dans un repère orthonormé (O, i, j) du plan.
1- a) Etudier le sens de variation de la fonction ln. b) Dresser le tableau de variation de la fonction ln.
2- Montrer que la fonction ln réalise une bijection de ]0,+∞[ sur IR
3- Montrer que l'équation ln x = 1 admet dans ]0,+∞[ une solution unique qu'on notera e. Vérifier que e ∈ ]2,7 ; 2,8[.
4- Donner une équation de la tangente T à Γ au point d'abscisse 1.
5- Vérifier que Γ admet une asymptote verticale dont-on donnera une équation et qu'elle présente une branche parabolique de direction l'axe des abscisses au voisinage de +∞
6- Tracer la droite T et la courbe Γ.

**Représentation graphique** (p.92) : courbe Γ de ln dans un repère (graduations 1, e, 3, 5 en abscisse ; 1, 2 en ordonnée), passant par (1 ; 0), tangente T en pointillé au point d'abscisse 1, point d'abscisse e marqué à l'ordonnée 1, asymptote verticale (axe des ordonnées). Mention : e ≃ 2,71828...

**Activité 5** (p.92-93) Soit f la fonction définie sur ]0,+∞[ par f(x) = x − 2 − ln x. On désigne par C la courbe représentative de f dans un repère orthonormé (O, i, j) du plan.
1) Calculer : lim_{x→0+} f(x) et lim_{x→+∞} f(x)
 2) Montrer que f est dérivable sur ]0,+∞[ et que f'(x) = (x−1)/x
 3) Dresser le tableau de variations de f.
 4) Calculer lim_{x→+∞} f(x)/x et interpréter graphiquement le résultat.
 5) Montrer que l'équation f(x) = 0 admet exactement deux solutions α et β telles que α ∈ ]0,1 ; 0,2[ et β ∈ ]3,1 ; 3,2[  [intervalles à virgule décimale ; vérifié : f(0,1)>0>f(0,2) et f(3,1)<0<f(3,2) ; voir § Notes]
 6) Tracer la courbe C.

**Activité 6** (p.93)
1) Soit g la fonction définie sur IR par g(x) = x² − 8x + 17
 a) Dresser le tableau de variation de g. b) En déduire le signe de g(x).
2) Soit f la fonction définie sur IR par f(x) = ln(x² − 8x + 17).
 a) Montrer que f est dérivable sur IR et que f'(x) = 2(x−4)/g(x).
 b) Calculer les limites de f en −∞ et en +∞.
 c) Dresser le tableau de variation de f.
On désigne par C_g et C_f les courbes représentatives respectives de f et g [sic, ordre inversé dans le manuel] dans un repère orthonormé (O, i, j) du plan.
3) Montrer que la droite D d'équation x = 4 est un axe de symétrie pour la courbe C. [« C » non défini : coquille, il s'agit de C_f]
4) Tracer les courbes C_g et C_f.
5) Résoudre dans IR, graphiquement puis par le calcul : f(x) = ln 5 et f(x) ≥ ln 5.

**Activité 7** (p.93) Soient f la fonction définie sur ]−1,1[ par f(x) = ln((1−x)/(1+x)) et C sa courbe représentative dans un repère orthonormé (O, i, j) du plan.
1- Montrer que la fonction f est impaire.
2- a) Calculer lim_{x→1−} f(x) et en déduire lim_{x→−1+} f(x)
 b) Interpréter graphiquement les résultats.
3- a) Montrer que f est dérivable sur ]−1,1[ et que f'(x) = 2/(x²−1)
 b) Déterminer le sens de variation de f puis dresser son tableau de variation.
 c) Montrer que le point O est un point d'inflexion pour la courbe C. Donner une équation de la tangente D à la courbe C en ce point.
4- Tracer D et C.

**Activité 8** (pp.93-94) — situation : modèle offre/demande d'un produit.
« Une étude a permis de modéliser les quantités d'un produit ( en milliers d'unités ) mis sur le marché par la fonction d'offre g définie sur [1,22] par : g(x) = 0,3x + 1 où x désigne le prix unitaire en dinars.
La fonction de demande des consommateurs est modélisée pour x ∈ [1,22] par q(x) = −0,4x + 5 + ln(2x + 6) ( q(x) représente les quantités du produit (en milliers) que les consommateurs sont prêts à acheter pour un prix unitaire x). »
1) Montrer que la fonction g − q est strictement croissante sur [1,22].
2) En déduire qu'il existe sur [1,22] un unique prix d'équilibre x0 ( l'équilibre est établi lorsque l'offre est égale à la demande )
 Quelle est alors la quantité d'équilibre q0 ?
3) Tracer dans un même repère orthogonal les courbes représentatives de f et de g (On prendra : 0,5cm pour 1dinar en abscisses et 1cm pour un millier d'unités en ordonnées ).
4) Retrouver graphiquement p0 et q0 .
[Notes : « f » dans la question 3 désigne en fait q (coquille) ; « p0 » en question 4 = x0 (prix d'équilibre) ; « g(x) = 0,3x + 1 » pour la fonction d'offre. Aucun corrigé.]

---------------------------------------------------------------------
#### COURS — B- FONCTION EXPONENTIELLE DE BASE e
---------------------------------------------------------------------
##### 1) Définition (pp.94-95)

**Activité 1** (p.94)
1°) Vérifier que pour tout entier relatif n on a : ln(eⁿ) = n.
2°) Résoudre dans IR les équations suivantes :
 a) ln x = 2 ; b) ln(x+2) = −1 ; c) ln(x²+1) = 4 ; d) ln x = n où n ∈ ℤ

**Activité 2** (p.94) Soit f la fonction définie sur ]0,+∞[ par f(x) = ln x.
1- a) Vérifier que f admet une fonction réciproque définie sur IR, que l'on note exp
 b) Montrer que : { x > 0 ; ln(x) = y } si et seulement si { y ∈ ℝ ; exp(y) = x }
 c) Calculer exp(0), exp(1) et exp(n) pour n entier relatif.
 d) Montrer que pour tout réel x on a : exp(x) > 0
 e) Montrer que pour tout réel x on a : ln(exp(x)) = x et que pour tout réel x strictement positif on a : exp(ln x) = x.
2- a) Montrer que g est continue et strictement croissante sur IR. [« g » non défini : coquille, il s'agit de exp]
 b) En déduire que pour tous réels x et y on a :
 • exp(x) = exp(y) si et seulement si x = y.
 • exp(x) > exp(y) si et seulement si x > y.

**Définition (encadré)** : On appelle fonction exponentielle de base e et on note **exp** la fonction réciproque de la fonction logarithme népérien.

**Notation** : « Du fait que pour tout entier relatif n on a : ln(x) = n équivaut à x = eⁿ on en déduit que : pour tout entier relatif n on a : exp(n) = eⁿ. On convient d'étendre cette écriture à tout réel x et on écrit exp(x) = eˣ. »
 Ainsi exp : ℝ → ]0;+∞[ ; x ↦ eˣ

**Conséquences (p.95)** :
 1) e⁰ = 1 et pour tout réel x, eˣ > 0.
 2) Les fonctions ln et exp étant des fonctions réciproques, on a : { x > 0 ; ln(x) = y } si et seulement si { y ∈ ℝ ; eʸ = x }
 3) Pour tout réel x, ln(eˣ) = x.
 4) Pour tout réel x strictement positif, e^{ln(x)} = x.
 5) La fonction exp est comme la fonction ln, continue et strictement croissante sur ℝ.
 6) Pour tous réels x et y on a : ∗ eˣ = eʸ si et seulement si x = y ; ∗ eˣ > eʸ si et seulement si x > y

**Activité 3** (p.95)
1- Calculer : a) e^{ln 1} − e^{ln 2} ; b) ln e^{−2} + 2 ln e ; c) e^{ln 2}/e^{−ln 3} ; d) e^{2 ln 3}/e^{ln 8} ; e) e^{3 ln 3} − 3 ln(e⁷)
2- Résoudre dans IR chacune des équations suivantes :
 a) e^{2x+1} = e² ; b) e^{−4x+1} = 3 ; c) ln(x−2) = −1/2 ; d) e^{2x} = e^{−x}

##### 2) Propriétés (pp.95-96)

**Activité 1** (p.95) Soient a et b deux nombres réels.
1- Vérifier que ln(eᵃ × eᵇ) = a + b.
2- En déduire que : e^{a+b} = eᵃ × eᵇ , e^{−a} = 1/eᵃ et e^{a−b} = eᵃ/eᵇ ,
3- Montrer que pour tout entier relatif n on a : e^{na} = (eᵃ)ⁿ

**Propriétés (encadré)** — Pour tous réels a et b :
 • e^{a+b} = eᵃ × eᵇ • e^{−a} = 1/eᵃ • e^{a−b} = eᵃ/eᵇ • e^{na} = (eᵃ)ⁿ (n ∈ ℤ)

**Activité** (sans numéro, p.95)
1- a) Calculer : A = e^{1+ln 2} ; B = e^{1−2 ln 3}.
 b) Simplifier les expressions suivantes :
 A = (eˣ + e^{−x})² ; B = (e^{−x} − eˣ)(e^{−x} + eˣ) ; C = e^{2x}/(e^{3x−2} × e^{1−x}) ; D = ln( e^{2x}/e^{x−1} × e^{−x} )
2- Résoudre dans IR : a) 2e^{2x} − 3eˣ + 1 = 0 ; b) 2e^{2x} ≤ 3eˣ − 1
3- Résoudre dans IR : a) e^{(x−4)(2x−1)} = e ; b) eˣ + e^{−x} = 2 ; c) 2eˣ(eˣ − 6e^{−x}) = 5eˣ
4- (p.96) Démontrer les égalités suivantes :
 a) eˣ(1 + eˣ) = 1 + e^{2x} [imprimé tel quel à l'image (zoom 200 dpi) ; égalité fausse en général, eˣ(1+eˣ) = eˣ + e^{2x} : coquille du manuel, voir § Notes] ; b) eˣ/(1+eˣ) = 1/(1+e^{−x}) ; c) 1/(1+e^{−x}) = eˣ − eˣ/(1+e^{−x})

##### 3) Étude de la fonction exp (p.96-97)

**Activité 1** (p.96) Soit f la fonction définie sur IR par f(x) = eˣ. On désigne par C sa courbe représentative dans un repère orthonormé (O, i, j) du plan.
1- A partir du tableau de variation de la fonction ln vérifier que : lim_{x→+∞} eˣ = +∞ et que lim_{x→−∞} eˣ = 0.
2- Dresser le tableau de variation de la fonction f.
3- a) Montrer que f est dérivable en 0 et que f '(0) = 1. En déduire que lim_{x→0} (eˣ − 1)/x = 1.
 b) Déterminer une équation cartésienne de la tangente à la courbe C au point d'abscisse nulle.
4- a) A partir de la courbe de la fonction ln, que peut-on conjecturer pour la branche infinie de C au voisinage de +∞ ?
 b) Soit u la fonction définie sur ]0,+∞[ par u(x) = x/ln x. Calculer lim_{x→+∞} u(x) puis lim_{x→+∞} u(eˣ)
 c) En déduire que lim_{x→+∞} eˣ/x = +∞. Interpréter graphiquement le résultat.

**Théorème (encadré)** :
 • lim_{x→+∞} eˣ = +∞ • lim_{x→−∞} eˣ = 0 • lim_{x→+∞} eˣ/x = +∞ • lim_{x→0} (eˣ − 1)/x = 1

**Représentation graphique** (p.96) : figure avec C_exp (passe par (0 ; 1), tangente en ce point), C_ln (passe par (1 ; 0), tangente en ce point) et la droite Δ : y = x (axe de symétrie des deux courbes) ; graduations 1, 3, 5 en abscisse, 1, 3 en ordonnée.

**Activité 2** (p.97)
1- Soit u la fonction définie sur ]0,+∞[ par u(x) = x ln x
 a) Calculer lim_{x→−∞} u(eˣ)
 b) En déduire que lim_{x→−∞} x eˣ = 0.
2- Soit n un entier naturel non nul.
 a) Montrer que pour tout réel strictement positif x on a : ln(eˣ/xⁿ) = x − n ln x.
 b) Calculer lim_{x→+∞} (1 − n (ln x)/x) puis lim_{x→+∞} (x − n ln x).
 c) En déduire que lim_{x→+∞} eˣ/xⁿ = +∞.
 d) Vérifier que (−x)ⁿ e^{−x} = (−1)ⁿ xⁿ/eˣ. En déduire que lim_{x→−∞} xⁿ eˣ = 0.

**Théorème (encadré)** :
 • lim_{x→−∞} x eˣ = 0
 • Pour tout entier naturel n non nul on a : lim_{x→+∞} eˣ/xⁿ = +∞ et lim_{x→−∞} xⁿ eˣ = 0

**Activité 3** (p.97)
1- Calculer les limites suivantes :
 a) lim_{x→+∞} (e^{2x} + eˣ − 1) ; b) lim_{x→−∞} x e^{2x} ; c) lim_{x→+∞} ln(1 + e^{−x}) ; d) lim_{x→−∞} x³ eˣ
2- Calculer :
 a) lim_{x→+∞} 1/(x eˣ) ; b) lim_{x→−∞} (1/x + e^{−x}) ; c) lim_{x→+∞} x e^{−x} ; d) lim_{x→−∞} (eˣ + 1)/(eˣ − 1)
 e) lim_{x→+∞} x² e^{−3x} ; f) lim_{x→0} x/(eˣ − 1) ; g) lim_{x→+∞} (eˣ + 3)/eˣ ; h) lim_{x→0+} x e^{1/x}

**Activité 4** (p.97)
1- Soit h la fonction définie sur IR par h(x) = (ln∘exp)(x). Calculer de deux manières différentes h'(x) et en déduire que Pour tout x de IR, (exp)'(x) = exp(x)
2- Soit g la fonction définie sur IR par g : x ↦ e^{−x²+3x+1}. Montrer que la fonction g est dérivable sur IR et que g'(x) = (−2x + 3) e^{−x²+3x+1}.
3- Soit u une fonction dérivable sur un intervalle I de IR. Montrer que la fonction (exp∘u) est dérivable sur I et que (exp∘u)'(x) = u'(x).e^{u(x)}

**Théorème (encadré, p.98)** :
 • La fonction exponentielle est dérivable sur IR et est égale à sa fonction dérivée. (exp)' = exp
 • Soit u une fonction dérivable sur un intervalle I de IR. La fonction (exp∘u) est dérivable sur I et pour tout x de I on a : (exp∘u)'(x) = u'(x).e^{u(x)}

**Remarque (encadré)** : Lorsque u est une fonction dérivable sur un intervalle I, une primitive sur I de la fonction : x ↦ u'(x)e^{u(x)} est la fonction x ↦ e^{u(x)}.

**Activité 5** (p.98)
1- Pour chacun des cas suivants, justifier que la fonction f est dérivable sur l'intervalle I puis définir sa fonction dérivée f '.
 a) f(x) = e^{x²/2} ; I = IR b) f(x) = e^{1/(x+2)} ; I = ]−∞,−2[
 c) f(x) = e^{√x} ; I = ]0,+∞[ d) f(x) = e^{√(x³)} ; I = ]0,+∞[
2- Déterminer une primitive de f sur l'intervalle I
 a) f(x) = 2x e^{x²−1} ; I = ℝ b) f(x) = (4x³ + 2x) e^{x⁴+x²} ; I = IR
 c) f(x) = e^{√(x−1)}/√(x−1) ; I = ]1,+∞[ d) f(x) = e^{1/(x+1)}/(x+1)² ; I = ]−1,+∞[

**Activité 6** (p.98) On considère la fonction g définie sur IR par g(x) = x² − 2x
1- a) Dresser le tableau de variation de g. b) Tracer la parabole (P) représentant la fonction g.
2- Soit f la fonction définie sur IR par f(x) = e^{x²−2x}
 a) Montrer que f est continue et dérivable sur IR. b) Calculer les limites de f en −∞ et en +∞. c) Dresser le tableau de variation de f.
3- a) Montrer que pour x ∈ IR \ {0,2} on a f(x)/x = (x − 2) e^{x²−2x}/(x²−2x)
 b) Calculer lim_{x→+∞} f(x)/x et lim_{x→−∞} f(x)/x interpréter graphiquement les résultats.
 c) Tracer la courbe (C) de f dans le même repère (P).

**Activité 7** (pp.98-99) Soit f la fonction définie sur IR par f(x) = x² eˣ. On désigne par C sa courbe représentative dans un repère orthonormé du plan.
1- Calculer la limite de f en −∞. Interpréter graphiquement le résultat.
2- Calculer lim_{x→+∞} f(x) et lim_{x→+∞} f(x)/x. Interpréter graphiquement le résultat.
3- Etudier les variations de f.
4- Tracer la courbe C.

**Activité 8** (p.99) Soit f la fonction définie sur IR par f(x) = e^{(x−1)/x} si x ≠ 0 ; f(0) = 0.
On désigne par C sa courbe représentative dans un repère orthonormé du plan.
1- Etudier la continuité de f à droite et à gauche en 0.
2- a) Montrer que pour tout réel x strictement positif, on a : e^{(x−1)/x}/x = (1 − 1/x) e^{1−1/x} / (x − 1)  [image : e^{(x−1)/x}/x = (1−1/x)e^{1−1/x}/(x−1)]
 b) Calculer lim_{x→0+} (1 − 1/x). En déduire que f est dérivable à droite en 0 et que f'_d(0) = 0.
3- Calculer les limites de f en −∞ et en +∞. Interpréter graphiquement les résultats.
4- Déterminer une équation de la tangente T à C au point d'abscisse 1.
5- a) Montrer que f est dérivable et strictement croissante sur chacun des intervalles ]−∞,0[ et [0,+∞[.
 b) Dresser le tableau de variation de f.
6- Tracer la tangente T et la courbe C.

**Activité 9** (p.99) On considère la fonction f définie sur IR par f(x) = eˣ/(eˣ − 1). On note (C) sa courbe représentative dans le plan rapporté au repère orthogonal (o, i, j), l'unité graphique est 2 cm sur l'axe des abscisses et 5 cm sur l'axe des ordonnées.
[Remarque de lecture : f(x) = eˣ/(eˣ − 1) n'est pas définie en 0 ; le manuel dit « définie sur IR » — coquille, voir § Notes.]
Partie A. Soit g la fonction définie sur IR par g(x) = eˣ − x − 1.
 1. Étudier les variations de la fonction g sur R. En déduire le signe de g.
 2. Justifier que pour tout x, (eˣ − x) est strictement positif.
Partie B.
 1. a. Calculer les limites de la fonction f en +∞ et en −∞. b. Interpréter graphiquement tes résultats précédents.
 2. a. Calculer f '(x). b. Étudier le sens de variations de f puis dresser son tableau de variations.
 3. a. Déterminer une équation de la tangente (T) la courbe (C) au point d'abscisse 0. b. À l'aide de la partie A, étudier la position de la courbe (C) par rapport à la droite (T).
 4. Tracer la droite (T) les asymptotes et la courbe (C ).
[Notes : [R7 : image 300 dpi — imprimé exactement f(x) = eˣ/(eˣ − 1), « définie sur IR ». Hypothèse d'auditeur, NON imprimée : la Partie A (eˣ − x > 0) suggère que la fonction voulue est eˣ/(eˣ − x) ; l'ancienne hypothèse « x/(eˣ − 1) » est retirée.] L'énoncé est reproduit tel quel — voir § Notes.]

##### 4) Fonction x ↦ aˣ (avec a > 0) (p.100-101)

**Activité 1** (p.100) — situation : placement de capital.
Un capital de 8000 DT placé durant n années, a une valeur acquise modélisée par la fonction C définie par C(n) = 8000.(1,055)ⁿ.
a- Déterminer la valeur acquise après 5 ans.
b- Montrer que pour tout entier naturel n on a C(n) = 8000.e^{n ln(1,055)}
(Taux annuel implicite 5,5 %, intérêts composés [R7 : déduction du lecteur, non imprimée] ; aucun corrigé donné.)

**Définition (encadré)** : Soit a un réel strictement positif. On appelle fonction exponentielle de base a, la fonction x ↦ e^{x ln a} définie sur IR et qu'on note x ↦ aˣ

**Remarques (encadré)** :
 • Si a = 1, alors pour tout x de IR 1ˣ = 1
 • Lorsque a = e, on retrouve la fonction exp.
 • Pour tout réel strictement positif a et pour tout réel x, le réel aˣ est strictement positif.
 • Pour tout réel strictement positif a et pour tout réel x, ln(aˣ) = x ln a

**Activité 2** (p.100) Résoudre dans IR :
 a) 2ˣ = e^{x−1} ; b) e^{−x} = 5^{2x} ; c) 3^{x²+4x} = 1/27 ; d) 3ˣ = 2^{x−1}
 e) 5^{x+2} = 4^{1−x} ; f) |2^{x²} − 8| = 8 ; g) 3ˣ − e^{x+1} > 0

**Activité 3** (p.100) Soit a ∈ IR*₊ et x et y deux nombres réels quelconques.
1- Montrer que aˣ × aʸ = a^{x+y}
2- En déduire que : a^{−y} = 1/aʸ et a^{x−y} = aˣ/aʸ
3- Vérifier que pour tout entier relatif n on a a^{nx} = (aˣ)ⁿ.

**Propriétés (encadré)** : Soit a > 0, pour tous réels x et y on a :
 a^{x+y} = aˣ × aʸ ; a^{−y} = 1/aʸ ; a^{x−y} = aˣ/aʸ ; a^{nx} = (aˣ)ⁿ (n ∈ ℤ)

**Activité 4** (p.101)
1- a) Résoudre dans IR l'équation 2x² − 5x + 3 = 0
 b) En déduire les solutions de l'équation 2e^{2x} − 5eˣ + 3 = 0.
2- Résoudre dans IR les équations : a) 5^{2x} + 5ˣ − 4 = 0 ; b) 4ˣ − 2ˣ + 6 = 0
3- Simplifier les écritures suivantes :
 a) (3^{n+2} × 3^{2n})/3^{n+3} [R7 : le « a) » n'est pas imprimé] ; b) (2×3)ⁿ/(2^{n−1})² ; c) (4ⁿ × 2^{n+1})/(3ⁿ × 2^{3n+1})

##### Étude des fonctions du type x ↦ aˣ (pp.101-102)

**Activité 1** (p.101) Soient a un nombre réel strictement positif différent de 1 et f la fonction définie sur IR par f(x) = aˣ. On désigne par C la courbe représentative de f dans un repère orthonormé (O, i, j).
1- Montrer que la fonction f est continue et dérivable sur IR et que f '(x) = ln a .(aˣ)
2- On suppose que a ∈ ]0,1[
 a- Vérifier que f est strictement décroissante sur IR.
 b- Calculer lim_{x→−∞} aˣ et lim_{x→+∞} aˣ puis dresser le tableau de variations de f.
 c- Donner une équation de la tangente à C au point d'abscisse nulle.
 d- Tracer une allure de la courbe C
3- On suppose que a ∈ ]1,+∞[
 a- Vérifier que f est strictement croissante sur IR.
 b- Calculer lim_{x→−∞} aˣ et lim_{x→+∞} aˣ puis dresser le tableau de variations de f.
 c- Donner une équation de la tangente à C au point d'abscisse nulle.
 d- Tracer une allure de la courbe C.
4- Le plan étant muni d'un repère orthonormé (O, i, j), vérifier que les courbes représentatives des fonctions x ↦ aˣ et x ↦ (1/a)ˣ sont symétriques par rapport à l'axe des ordonnées.

**Théorèmes (encadré)** :
 • Soit a un nombre réel strictement positif et différent de 1. La fonction f définie sur IR par f(x) = aˣ est dérivable sur IR et f '(x) = ln a .(aˣ)
 • Si a ∈ ]0,1[ alors : lim_{x→−∞} aˣ = +∞ et lim_{x→+∞} aˣ = 0
   Si a ∈ ]1,+∞[ alors : lim_{x→−∞} aˣ = 0 et lim_{x→+∞} aˣ = +∞

**Activité 2** (p.102) Soit f la fonction définie sur IR par f(x) = 2ˣ. On désigne par C sa courbe représentative dans un repère orthonormé (O, i, j) du plan.
1- a) Etudier le sens de variation de f puis dresser son tableau de variation.
 b) Vérifier que la courbe C admet au voisinage de −∞ une asymptote dont-on donnera une équation cartésienne.
 c) Montrer que la courbe C admet au voisinage de +∞ une branche parabolique de direction l'axe des ordonnées.
2- Vérifier que f '(0) = ln 2. Donner une équation de la tangente T à C au point d'abscisse nulle. [numérotation imprimée : « 2- » puis « 4- » ; il manque un « 3- » (coquille de numérotation)]
4- Tracer la droite T et la courbe C.

**Activité 3** (p.102) Soit g la fonction définie sur IR par g(x) = (1/3)ˣ. On désigne par C sa courbe représentative dans un repère orthonormé (O, i, j) du plan.
1- a) Etudier le sens de variation de g puis dresser son tableau de variation.
 b) Montrer que lim_{x→−∞} g(x)/x = −∞, interpréter graphiquement le résultat
2- a) Montrer que g réalise une bijection de IR sur ]0,+∞[ ; soit g⁻¹ sa fonction réciproque.
 b) Montrer que pour tout x de ]0,+∞[, g⁻¹(x) = − ln x / ln 3,
 c) Montrer que g⁻¹ est dérivable sur ]0,+∞[ et calculer (g⁻¹)'(x)
3- Tracer les courbes représentatives de g et g⁻¹ dans un même repère orthonormé (O, i, j).

**Activité 4** (p.102) — situation : évolution de deux populations animales.
De 2000 à 2007 on a suivi l'évolution de deux populations A et B de deux espèces animales. Ces populations sont données respectivement par : f(t) = 10 × 1,2ᵗ et g(t) = 40 × 0,9ᵗ
f(t) et g(t) sont exprimées en milliers d'individus et t = 0 à la fin de l'an 2000.
1- Etudier le sens de variation de chacune des fonctions f et g sur [0,7].
2- Dresser les tableaux de variation de f et de g.
3- Représenter graphiquement dans le même repère orthonormé les courbes des fonctions f et g.
4- a- Vérifier graphiquement que la population A dépasse la population B vers la fin de l'an 2004.
 b- Montrer que f(t) = g(t) pour t = ln 4 / (ln 4 − ln 3). En déduire que la population A dépasse la population B en septembre 2004.
([R7 : le manuel imprime seulement t = ln4/(ln4 − ln3), sans valeur ; « ≈ 4,82 » est un recalcul d'auditeur, non imprimé.])

---------------------------------------------------------------------
#### AVEC L'ORDINATEUR (p.103)
---------------------------------------------------------------------
**I-** On se propose d'élaborer sous un tableur (tel que Excel), une feuille de calcul qui nous permet ce calculer la valeur acquise d'un capital placé Cp durant n années sur un taux de t% ; cette valeur acquise est obtenue par : Cp(1 + t/100)ⁿ.
**Etape 1** : Donner un nom à chaque cellule de données. Définir les variables *i* et *aire* [sic, phrase sans rapport avec la feuille ; coquille du manuel]
 * Sélectionner la cellule B1 — Dans le menu : 'Insertion' sélectionner la commande 'nom' puis 'définir'. Taper la lettre : Cp ; puis valider
 * Sélectionner la cellule B2 — Dans le menu : 'Insertion' sélectionner la commande 'nom' puis 'définir'. Taper : t ; puis valider
 * Sélectionner la cellule B3 — Dans le menu : 'Insertion' sélectionner la commande 'nom' puis 'définir'. Taper : n ; puis valider
**Etape 2** : Recopier le tableau suivant (capture de tableur) :
| Capital placé (Dt) | 100 |
|---|---|
| Taux (%) | 4 |
| Nombre d'années | 2 |
| Valeur acquise (Dt) | =(Cp*(1+t/100)^n) |
(Les valeurs dans la capture : B1 = 100 ; B2 = 4 ; B3 = 2 ; B4 = formule ci-dessus.)
**Etape 3** : Saisir de différentes valeurs du capital, du taux ou du nombre d'années.
**II-** En revenant à la rubrique *avec l'ordinateur du chapitre étude de fonctions*, représenter des exemples de fonctions du type x ↦ aˣ où a est un réel strictement positif différent de 1. On obtient les courbes suivantes pour a = 0,5 et pour a = 2
 (Deux graphiques : f = Exp(x * Log(0,5)) décroissante, ordonnées 0 à 35, abscisses −10 à 10, courbe tracée de x=−5 à x≈4 ; f = Exp(x * Log(2)) croissante, ordonnées 0 à 140, courbe tracée jusqu'à x≈7 environ 128.)
Reprendre le même travail avec d'autres valeurs de a.

---------------------------------------------------------------------
#### EXERCICES ET PROBLÈMES (pp.104-111) — « Logarithme népérien » (p.104)
---------------------------------------------------------------------
**1-** Indiquer les bonnes réponses parmi les réponses a, b, c et d.
| | a | b | c | d |
|---|---|---|---|---|
| ln 2 + ln 3 = | ln 5 | ln 6 | ln 12 − ln 2 | ln12/ln2 |
| 3.ln 2 = | ln 6 | 2.ln 3 | ln 8 | 2 ln 4 |
| ln 4 + 3.ln2 − ln 16 = | ln 2 | 6.ln 2 − ln 32 | ln 32 − ln 16 | ln32/ln16 |

**2-** Ecrire en somme de logarithmes :
 a) ln(3 × 7²/24) ; b) ln(10 000/81) ; c) ln(2a³ × b²/25) où a et b dans ]0,+∞[
 d) ln(3(x−2)²) où x ∈ ]2,+∞[ ; e) ln(x²(x−3)) où x ∈ ]3,+∞[

**3-** Ecrire à l'aide d'un seul logarithme :
 a) ln(2/3) + ln(3/2) + ln 2 ; b) 2 ln 2 + ln 3 − ln 5 ; c) 3 ln 10 − ln 0,02 + 5 ln 2

**4-** Préciser l'ensemble de définition de chacune des fonctions suivantes puis l'exprimer à l'aide d'un seul logarithme :
 a) f : x ↦ ln x + ln(x−1) ; b) g : x ↦ ln(3−x) + ln(3+x)
 c) h : x ↦ 2 ln(x²−1) − 3 ln(x+1) ; d) k : x ↦ 2 ln(5−x) + ln 7 − ln x

**5-** Calculer les limites suivantes :
 a) lim_{x→+∞} (x² + ln x) ; b) lim_{x→+∞} ((1−x) ln x) ; a) [sic, étiquette répétée : c)] lim_{x→+∞} (1 − (ln x)²) ; d) lim_{x→+∞} ((1 − ln x)/x)
 e) lim_{x→0+} (x − 2 + ln x) ; f) lim_{x→0+} (1/x − ln x) ; g) lim_{x→0+} ((2 ln x + 1)/x) ; h) lim_{x→0+} (1/x + ln x)

**6-** Calculer les limites de chacune des fonctions suivantes aux bornes de son ensemble de définition D :
 a) f : x ↦ 2x² − ln x D = ]0,+∞[ ; b) f : x ↦ −(ln x)² + 2 ln x − 2 D = ]0,+∞[
 c) f : x ↦ 2x ln x − x D = ]0,+∞[ ; d) f : x ↦ (2x − ln x)/x D = ]0,+∞[
 e) f : x ↦ (2x+1)/ln x D = ]1,+∞[ ; g) f : x ↦ (3x ln x + 2)/x² D = ]0,+∞[  [étiquettes imprimées a-b-c-d-e-g : pas de f)]

**7-** Résoudre dans IR
 a) 2 ln x = ln 3 ; b) ln(2x²) = 0 ; c) ln(x+2) = 2 ln x ; d) ln x = −4
 e) ln(x−4) = ln(2x−1) ; f) 2 ln x − ln(x+1) = 2 ln 2 ; g) (ln x)(1 + ln x) = 0

**8-** (p.105) a) le plan P étant rapporté à un repère orthonormé (O, i, j), tracer la courbe représentative de la fonction f : x ↦ ln x.
 b) En déduire la représentation graphique de la fonction g : x ↦ −ln x + 2 puis celle de la fonction h : x ↦ ln(x−2) + 1.

**9-** (p.105) On considère la fonction f définie sur ]0,+∞[ par f(x) = −x + 1 + ln x. C désigne la courbe représentative de f dans un repère orthonormé du plan.
1- a) Calculer la limite de f à droite en 0 ; donner alors l'équation de l'asymptote verticale de la courbe C.
 b) Calculer lim_{x→+∞} f(x) et lim_{x→+∞} f(x) + x et interpréter graphiquement le résultat.
2- Dresser le tableau de variation de f
3- Tracer la courbe C.

**10-** (p.105) Soit f la fonction définie sur ]0,+∞[ par : f(x) = x²(2 ln x − 1) si x ≠ 0 ; f(0) = 0  [domaine imprimé « ]0,+∞[ » alors que f(0) est défini : coquille, probable [0,+∞[]
Soit C sa courbe représentative dans un repère orthonormé du plan.
1- a) Etudier la continuité de f à droite en 0.
 b) Vérifier que f est dérivable à droite en 0 et que f '_d(0) = 0.
 c) Calculer la limite de f en +∞ puis lim_{x→+∞} f(x)/x, interpréter graphiquement le résultat.
 d) Dresser le tableau de variation de f.
2- Déterminer l'intersection de la courbe c avec l'axe des abscisses.
3- Tracer la courbe C.

**11-** (p.105) On considère la fonction f : x ↦ x/(ln x + 1) ; On désigne par C sa courbe représentative dans un repère orthonormé du plan.
a) Justifier que f est définie sur ]0,+∞[ \ {e⁻¹}
b) Calculer les limites de f à droite et à gauche en 1/e. Interpréter graphiquement le résultat.
c) Vérifier que la courbe C admet au voisinage de +∞ une branche parabolique dont-on déterminera la direction.
d) Dresser le tableau de variation de f.
e) Tracer la courbe C.

**12-** (p.105) Soit f la fonction définie sur ]0,+∞[ par f(x) = 1 + (2 ln x)/x [R7 : parenthésage levé à l'image]. On désigne par C sa courbe représentative dans un repère orthonormé du plan.
1- Déterminer les limites de f à droite en 0 et en +∞. Interpréter graphiquement les résultats.
2- Dresser le tableau de variation de f.
3- Montrer que la courbe C et la droite D d'équation y = 1 ont un point commun A dont on donnera les coordonnées.
4- Déterminer une équation de la tangente T à la courbe C au point A.
5- Tracer D et T et la courbe C.

**13-** (p.106) — situation : fonction bénéfice d'une production.
Soit f la fonction définie sur ]0,15] par f(x) = 3 + 2 ln x − (ln x)². On désigne par c sa courbe représentative dans un repère orthonormé (O, i, j).
1- a) Calculer lim_{x→0+} f(x) puis interpréter graphiquement le résultat.
 b) Démontrer que f est dérivable sur ]0,15] et vérifier que f' a le même signe que 1 − ln x.
 c) Dresser le tableau de variation de f.
2- Déterminer les points d'intersection de la courbe C avec l'axe des abscisses.
3- Tracer la courbe C.
4- La fonction f est la fonction bénéfice d'une production de x milliers d'objets. (f(x) est exprimé en milliers de dinars).
5- a) Déterminer la plage de production qui permet de réaliser un profit.( On donnera les bornes de l'intervalle en valeur approchée à 0,01 près ).
 c) Donner une valeur arrondie entière de la quantité x₀ pour laquelle le bénéfice est maximal. [numérotation imprimée : 5- a) puis c) ; pas de b) — coquille]

##### Fonctions exponentielles (p.106-111)

**14-** (p.106) Indiquer les bonnes réponses parmi les réponses a, b, c et d.
| | a | b | c | d |
|---|---|---|---|---|
| ((e²)³)/e⁻¹ = | e⁶ | e⁷ | e⁸ | e⁹ |
| (e⁴ × e⁻²)/e = | e⁵ | e | 1/e⁻¹ | e⁻¹ |
| ((2e)³ × e³)/5 = | 2³e⁹/5 | 2³e⁶/5³ | 2³e⁶/5 | 1/(5(2e²)⁻³) |

**15-** (p.106) Résoudre dans IR
 a) eˣ(eˣ − 1) = 0 ; b) (eˣ − 2)(2eˣ + 4) = 0 ; c) e^{−2x+3} = 1
 d) (2eˣ + 1)/(eˣ − 1) = 3 ; e) e^{−x} = e^{x/2} ; f) 2e^{−0,5+7} = 1 [imprimé tel quel, exposant sans x ; voir § Notes] ; g) e^{0,1x−2} = 0

**16-** (p.106)
1- a) Résoudre dans IR l'équation x² − 4x − 5 = 0
 b) En déduire la résolution dans IR des équations : • (ln x)² − 4 ln x − 5 = 0 ; • eˣ − 4 = 5e^{−x}
2- a) Résoudre dans IR l'équation x² − 10x + 9 = 0 puis (ln x)⁴ − 10(ln x)² + 9 = 0
 b) En déduire les solutions de l'équation : (ln x)⁴ − 10(ln x)² + 9 = 0 [sic : 2-a) et 2-b) répètent la même équation ; coquille probable de 2-a) : « puis »]

**17-** (p.106) Résoudre dans IR
 a) e^{2x} − 4eˣ = 0 ; b) e^{2x} − 2eˣ + 1 = 0 ; c) 2e^{2x} + eˣ = ln 0,1
 d) 1 − eˣ > 0 ; e) 3 − 2e^{−x} ≥ 0 ; f) e^{−x+4} ≤ 10^{−2}.

**18-** (p.107) Calculer les limites suivantes :
 a) lim_{x→−∞} x³eˣ ; b) lim_{x→+∞} eˣ/x³ ; c) lim_{x→0+} x⁴ ln x ; d) lim_{x→+∞} ln x/x⁴
 e) lim_{x→+∞} ln x/eˣ ; f) lim_{x→0+} ln x/eˣ ; g) lim_{x→+∞} eˣ/2ˣ ; h) lim_{x→+∞} eˣ/(0,1)ˣ

**19-** (p.107) Déterminer dans chacun des cas suivants les limites de f aux bornes de son ensemble de définition puis dresser son tableau de variations et tracer sa courbe représentative dans un repère orthonormé du plan.
 a) f : x ↦ eˣ/x D = IR* ; b) f : x ↦ x eˣ D = IR
 c) f : x ↦ eˣ/(eˣ + x) D = [0,+∞[ ; d) f : x ↦ eˣ/(1 + x) D = ]−∞,−1[ ∪ ]−1,+∞[

**20-** (p.107) Soit la fonction définie sur IR dont une représentation graphique est la suivante : [graphique : courbe C_f ; repère avec graduations 1 et 4 en ordonnée, −4 et 1 en abscisse ; la courbe coupe l'axe des abscisses en x = −4, croît jusqu'à un maximum d'ordonnée 4 (vers x ≈ −2 [R7 : relu à l'image, était « ≈ −2,5 »]), décroît ensuite, coupe l'axe des ordonnées vers y ≈ 2, puis décroît lentement en restant positive vers y ≈ 0,5 à droite (asymptote horizontale apparente en +∞) ; à gauche elle tend vers −∞]
1- a) Déterminer graphiquement les limites de f en −∞ et en +∞.
 b) En déduire les limites en −∞ et en +∞ de la fonction g : x ↦ exp(f(x))
2- a) Résoudre graphiquement f(x) = 0 ; puis f(x) ≥ 0.
 b) En déduire les solutions de exp(f(x)) = 1, puis exp(f(x)) ≥ 1
3- Dresser le tableau de variation de f puis celui de g.

**21-** (p.107) Soit la fonction f définie sur IR par f(x) = e^{2x}/(eˣ + 1). On désigne par C sa courbe représentative dans un repère orthonormé du plan.
1- Calculer lim_{x→−∞} f(x), lim_{x→+∞} f(x) et lim_{x→+∞} f(x)/x ; interpréter graphiquement les résultats.
2- Justifier que f est dérivable sur IR et calculer f '(x).
3- Dresser le tableau de variation de f.
4- Déterminer une équation de la tangente T à la courbe C au point d'abscisse nulle.
5- Tracer la droite T et la courbe C.
6- Montrer que f réalise une bijection de IR sur un intervalle J que l'on déterminera. On notera g sa fonction réciproque.
7- Tracer dans le même repère, la courbe représentative de la fonction g.
8- Expliciter g(x) pour x appartenant à J.

**22-** (pp.107-108) f est la fonction définie sur IR par : f(x) = 2eˣ − 2 − xeˣ. On désigne par c sa courbe représentative dans un repère orthonormé (O, i, j) du plan.
a- Calculer les limites de f aux bornes de son ensemble de définition.
b- Etudier le sens de variation de f puis dresser son tableau de variation.
c- Donner une équation de la droite D asymptote à la courbe C en −∞
d- Etudier la position relative de C et D.
e- Montrer que l'équation f(x) = 0 admet dans IR deux solutions dont l'une appartient à l'intervalle [1,5 ; 1,6].
f- Tracer C et D.

**23-** (p.108) Résoudre dans ]0,+∞[ chacune des équations suivantes :
 a) (1 + t/10)³ = 125 ; b) 12 = 17(1 − x)⁶ ; c) 48(1 + x)¹² = 187

**24-** (p.108) Déterminer le plus petit entier n vérifiant :
 a) 0,6ⁿ ≤ 10⁻³ ; b) 2,02ⁿ ≥ 500 ; c) (1/2)ⁿ ≤ 0.01

**25-** (p.108) — situation : taux équivalents et placements.
a) x étant un taux annuel, vérifier que son taux mensuel équivalent x' est tel que (1 + x')¹² = 1 + x c'est à dire 1 + x' = (1 + x)^{1/12}
b) Calculer la valeur acquise par un capital de 2000 DT placé à 7% annuel durant • six ans • six ans et demi • six ans et huit mois
c) Déterminer le temps de placement, au mois près pour un capital de 2500 DT, placé au taux annuel de 4,5%, ayant acquis la valeur de 3161,5 DT
d) Calculer le taux mensuel équivalent à un taux annuel de 8,5%
e) calculer le taux journalier équivalent à un taux annuel de 21% (une année étant de 365 jours ).

**26-** (p.108) — situation : bureau d'étude d'une société de grande distribution.
Le bureau d'étude d'une société de grande distribution a établi une relation donnant la superficie y (en m²) de ses magasins en fonction du nombre x de clients (en milliers par jour) : ln y = 0,09x + 7,1
1- a- Déterminer y en fonction de x sous la forme y = k.aˣ, où k est un réel dont-on donnera une valeur arrondie à la centaine.
 b- calculer la superficie d'un magasin pour une clientèle de 7 milliers.
2- Déterminer à partir de quel nombre de clients la superficie est supérieure à 2000m².( on donnera une valeur approchée par défaut à 0,1 millier près ).

**27-** (p.108) — situation : croissance de population.
a- La population d'un ville est passée en 5 ans de 20000 habitants à 29000 habitants . calculer le taux annuel de croissance de la population
b- Déterminer à 0,1 millier près la population de cette ville après 10 ans en supposant qu'elle garde le même taux de croissance.

**28-** (p.108) a- Un arbre, planté alors que sa taille mesurait 20cm, atteint 2m de hauteur au bout de 5 ans. Calculer le pourcentage moyen annuel d'augmentation de la hauteur de l'arbre.
 [l'énoncé 28 ne comporte qu'une question « a- » ; pas de b- imprimé]

##### Problèmes (pp.109-113)

**29-** (p.109) La fonction f est définie sur ]−1,+∞[ par : f(x) = −2x + 5 + 3 ln(x+1)
1- a- Calculer la limite de f en −1. Interpréter graphiquement le résultat.
 b- Montrer que lim_{x→+∞} ln((x+1)/x) = 0 ; calculer lim_{x→+∞} f(x).
2- a- Calculer f'(x) et étudier le sens de variation de f.
 b- Dresser le tableau de variation de f. Préciser la valeur exacte du maximum de f.
3- Nommer sur la figure précédente les points O, I et J du repère et ajouter les asymptotes éventuelles à la courbe. [« la figure précédente » : aucune figure n'est imprimée dans le manuel (coquille)]
4- a- Montrer qu'il existe deux réels α et β tels que α < 0 < β et f(α) = f(β) = 0.
 b- Donner une valeur approchée à 10⁻² près par défaut de α et de β.
 c- En déduire le signe de f(x) sur ]−1,+∞[
5- Soit g la fonction définie sur ]−1,+∞[ par : g(x) = (x+1) ln(x+1) − x
 a- Calculer g'(x)
 b- En déduire l'expression de la primitive de f s'annulant pour x=0.

**30-** (p.109) — situation : coût de fabrication d'un produit.
Une entreprise fabrique un produit en quantité x exprimée en milliers de tonnes. Le coût total de fabrication est donné par C_t(x) = x²/4 + (9/2) ln(x+1) pour x ∈ [0,5]. Les coûts sont exprimés en millions de dinars.
A- On considère la fonction f définie sur [0,5] par f(x) = x²/2 + 9x/(x+1) − 9 ln(x+1).
1- Vérifier que : f '(x) = x(x−2)(x+4)/(x+1)² pour tout x de [0,5].
2- Dresser le tableau de variation de f sur [0,5].
3- Montrer que l'équation f(x) = 0 admet dans ]0,5] une seule solution c.
4- Déterminer un encadrement à 10⁻³ près de c.
5- Dresser le tableau de signe de la fonction f sur [0,5].
B- La fonction coût moyen C_m est définie sur ]0,5] par C_m(x) = C_t(x)/x = x/4 + (9/2).ln(x+1)/x.
1- Calculer C'_m(x) et vérifier que l'on peut écrire C'_m(x) = f(x)/(2x²).
2- Etudier alors le sens de variation de C_m puis dresser son tableau de variation sur ]0,5].
3- Pour quelle production l'entreprise a-t-elle un coût moyen minimal, exprimé en dinars par tonnes ? Déterminer ce coût.
(Vérification de cohérence : f'(x) et C'_m(x) = f(x)/(2x²) recalculés, exacts.)

**31-** (pp.109-110) Partie A. Soit g la fonction définie sur l'intervalle ]0,+∞[ par g(x) = x − 5 + 5 ln x.
1- Etudier le sens de variation de g (ne pas étudier les limites).
2- a) Montrer que l'équation g(x) = 0 a une solution unique dans l'intervalle [1 ; 7]. On note α cette solution.
 b) Déterminer la valeur décimale arrondie au centième de α.
3- Etudier le signe de g(x), pour x appartenant à ]0,+∞[.
Partie B. Soit f la fonction définie sur ]0,+∞[ par f(x) = (x − 5) ln x / x.
1- Vérifier que l'on peut écrire : f(x) = (1/x)(x − 5) ln x = ln x − 5 ln x / x
 a- Déterminer la limite de f en 0. Interprétez graphiquement ce résultat.
 b- Déterminer la limite de f en +∞.
2- a- Soit f' la fonction dérivée de f. Calculer f'(x).
 b- Montrer que f'(x) et g(x) ont le même signe.
 c- Dresser le tableau de variation de la fonction f.
3- On désigne par (C) la courbe représentative de f dans le plan rapporté à un repère orthonormé (O, i, j).
 a- Soit A le point de la courbe (C) d'abscisse 1. Donner une équation de la droite D, tangente en A à la courbe (C). Déterminer les coordonnées du point d'intersection de D et de l'axe des ordonnées.
 b- Tracer D et (C) (Unités graphiques : 2cm).

**32-** (pp.110-111) Le but du problème est d'étudier le coût marginal et le coût total de production d'un produit dans une entreprise.
Partie A. La courbe (C), ci-contre, est la représentation graphique d'une fonction h définie sur [0 ; +∞[. Le point A a pour coordonnées (0 ; 2). La droite (T) est tangente à la courbe (C) au point A.
[Figure : repère d'unité 1 ; A = (0 ; 2) ; T est une droite décroissante partant de A et coupant l'axe des abscisses vers x = 2 (lecture : pente −1) ; C part de A, décroît jusqu'à un minimum d'ordonnée voisine de 0,7-0,8 vers x ≈ 2,5 [R7 : relu à l'image, était « 0,6-0,7 vers x ≈ 3 »] puis remonte jusqu'à environ y ≈ 3,4 vers x ≈ 5,1. Lecture graphique approximative, non chiffrée dans le manuel.]
1. Préciser h(0). Déterminer à l'aide d'une lecture graphique le nombre dérivé h'(0). Justifier la réponse.
2. La fonction h, définie sur [0 ; +∞[ est de la forme : h(x) = ax² + bx + c + 2 ln(x + 1) où a, b et c sont des nombres réels. On note h' la dérivée de la fonction h, exprimer h'(x) en fonction de a et b.
3. On donne h'(3) = 1/2. En utilisant ce résultat et les résultats de la question 1., déterminer chacune des valeurs a, b et c.
Partie B. Soit f la fonction définie sur I = [0 ; 5] par : f(x) = x²/2 − 3x + 2 + 2 ln(x + 1).
1. a) Calculer la dérivée f ' de la fonction f.
 b) Montrer que pour tout x de l'intervalle I : f '(x) = (x² − 2x − 1)/(x + 1)
 c) Etudier le signe de la fonction f ' sur l'intervalle I.
 d) En déduire les variations de f sur [0 ; 5].
2. Soit g la fonction définie sur I par : g(x) = (x + 1) ln(x + 1) − x.
 a) Calculer la dérivée de la fonction g.
 b) En déduire une primitive F de la fonction f sur I.
 c) Calculer la valeur exacte, puis la valeur approchée à 10⁻³ près, de la différence F(5) − F(0).
Partie C. Sur l'intervalle [0 ; 5], la fonction f de la partie précédente représente le coût marginal de production d'un liquide conditionné en flacons d'un litre, en fonction de la quantité produite. On rappelle que le coût marginal de production est assimilé à la dérivée du coût total. x représente le volume en milliers de litres, x variant sur l'intervalle [0 ; 5]. f(x) représente le coût marginal en milliers de dinars.
1. Quel est le coût marginal, en dinars, du 3000ᵉ litre produit ?
2. Pour quelle quantité produite le coût marginal est-il minimum ? (Donner la valeur au litre près.)
3. Les coûts fixes sont de 1000 dinars.
 a) Montrer, en utilisant le résultat de la partie B, question 2. b), que le coût total est donné sur [0 ; 5] par l'expression définie sur [0 ; 5] par : C(x) = (1/6)x³ − (3/2)x² + 2(x+1) ln(x+1) + 1.
 b) Calculer C(5) − C(0) à un dinar près et interpréter en termes de coût cette différence. Comparer ce résultat à celui trouvé à la partie B, 2. c) et expliquer cette réponse.
(Cohérence recalculée : f' = (x²−2x−1)/(x+1) exact ; C(x) cohérent avec F + 1.)

**33-** (p.111) Partie I : Soit la fonction f définie sur ]0,+∞[ par f(x) = x² − 3,2 − 8 ln x
1- Déterminer la limite de la fonction f en 0. On peut écrire f(x) = x²(1 − 3,2/x² − 8 ln x/x²). Déterminer la limite de f en +∞
2- a) Étudier les variations de la fonction f sur ]0,+∞[
 b) Montrer que l'équation f(x) =0 possède une solution unique α dans [3, 4], puis déterminer une valeur approchée par excès de α à 10⁻¹ près. Dans la suite du problème, on utilisera cette valeur dans les calculs.
 c) En déduire le signe de f(x) sur [1, 6].
Partie II : Une application économique — situation : fabrication d'un solvant pour peinture.
Une entreprise fabrique un solvant pour peinture. x désigne le nombre de m³ de solvant produit chaque jour ; x ∈ [1, 6]. Le coût total de production de ces x mètres cubes, en milliers de dinars est : C_t(x) = x²/4 + 2,8 + 2 ln x.
On cherche à déterminer le prix de vente pour que l'entreprise fasse des bénéfices.
A. Étude de la fonction coût total C_t :
 1- Étudier les variations de C_t sur [1, 6].
 2- a) Reproduire et compléter le tableau suivant :
 | x | 1 | 1,5 | 2 | 2,5 | 3 | 3,5 | 4 | 4,5 | 5 | 5,5 | 6 |
 |---|---|---|---|---|---|---|---|---|---|---|---|
 | C_t(x) à 10⁻¹ près | | | | | | | | | | | |
 b) Tracer dans un repère (O; i, j) la représentation graphique (C) de la fonction C_t (unités graphiques : 2cm pour 1 m³ et 1cm pour 1 millier de dinars)
B. Étude de la fonction coût moyen C_m : Pour une production journalière de x mètres cubes, le coût moyen de production en milliers de dinars de 1 m³ est : C_m(x) = C_t(x)/x
 1- Montrer que C_m(x) = (x² + 11,2 + 8 ln x)/(4x).
 2- Démontrer que, pour tout réel x de [1, 6], C'_m(x) = f(x)/(4x²). (f étant la fonction définie dans la partie I).
 3- a. Étudier les variations de la fonction C_m sur [1, 6].
 b. Quel est le coût minimum de production de 1m³ de solvant ? Pour quelle production ?
 c. Comment faut-il choisir le prix de vente de 1m³ de solvant pour que l'entreprise puisse faire des bénéfices ?
(Cohérence recalculée : C_m = (x²+11,2+8 ln x)/(4x) et C'_m = f/(4x²) exacts.)

**34-** (p.112) — situation : machine à emboutir.
Une entreprise fabrique des objets à l'aide d'une machine à emboutir. On désigne par x, en centaines, le nombre d'objets fabriqués et l'on sait que le coût, exprimé en milliers de dinars, d'utilisation de cette machine en fonction de x est exprimé par : f(x) = (3/4)x + e^{−(3/4)x+1/2}
1- Etudier le sens de variation de f sur [0,+∞[ puis dresser son tableau de variation.
2- Donner une valeur arrondie entière du nombre d'objets qu'il faut produire pour que le coût soit minimal.
3- Un objet fabriqué par cette machine est vendu 8 Dt. Prouver que le bénéfice, en milliers de dinars, en fonction de x est donné par : g(x) = (1/20)x − e^{−(3/4)x+1/2}
4- Dresser le tableau de variation de g sur [0,+∞[.
5- a) Montrer que l'équation g(x) = 0 admet une solution unique α et que 3,13 < α < 3,14
 b) En déduire le nombre minimal d'objets à fabriquer afin que l'entreprise réalise un bénéfice.
(Cohérence recalculée : 8 Dt × 100x objets = 0,8x millier de dinars ; 0,8x − (3/4)x = x/20, g exact.)

**35-** (pp.112-113) A- On considère la fonction f définie sur [0,+∞[ par f(x) = x + 3 + e^{−x+2}
On désigne par C sa courbe représentative dans un repère orthonormé (O, i, j) (on prendra pour unité graphique 1cm).
1- Calculer la limite de f en +∞
2- Montrer que la droite D : y = x + 3 est asymptote à C.
3- Dresser le tableau de variation de f sur [0,+∞[.
4- a) Tracer la courbe C et la droite D. b) Déterminer graphiquement le nombre de solutions de l'équation (E) : f(x) = 8.
 c) Justifier que dans l'intervalle [2,6], l'équation (E) admet une solution unique α dont on donnera un encadrement d'amplitude 10⁻².
B- Une entreprise industrielle produit chaque jour x centaines d'objets (1 ≤ x ≤ 20). Le coût de fabrication de x centaines d'objets est modélisé par f(x) exprimé en milliers de dinars.
1- Calculer le coût de fabrication de 600 objets, 1000 objets, 1200 objets arrondi au dinar.
2- Quelle quantité d'objets doit-on fabriquer pour que le coût de fabrication soit le plus proche possible de 8000DT ?
3- Montrer que le coût de fabrication est minimal lorsque l'entreprise fabrique une quantité q₀ d'objets. Donner une valeur de q₀.
Quel est alors le coût, en dinars, de fabrication d'un objet ?
[Remarque : en B, f est celle de A (f(x) = x + 3 + e^{−x+2}) ; calcul du rédacteur de la fiche, NON donné par le manuel : f'(x) = 1 − e^{−x+2} s'annule en x = 2 (minimum), soit q₀ = 200 objets, f(2) = 6 milliers de dinars = 30 dinars/objet ; à ne pas reprendre comme corrigé officiel.]

**36-** (p.113) On considère la fonction f définie sur [0,+∞[ par f(x) = x + 2 (eˣ − 1)/(eˣ + 1) et on note c sa courbe représentative dans le plan rapporté à un repère orthonormé (O, i, j) (unité graphique 2cm).
1- Justifier que f(x) = x + 2 − 4/(eˣ + 1) puis calculer la limite de f en +∞.
2- Montrer que la droite d : y = x + 2 est asymptote à C en +∞. Etudier la position de C par rapport à D.
3- On désigne par M le point de C d'abscisse x et n le point de D de même abscisse x. La distance entre les points M et N est alors le nombre MN = 4/(eˣ + 1). Résoudre l'inéquation MN < 10⁻¹.
4- Calculer f '(x) puis dresser le tableau de variation de f sur [0,+∞[.
5- Démontrer que l'équation f(x) = 1 admet dans l'intervalle [0,1] une solution unique x₀ dont on donnera un encadrement à 10⁻¹ près.
6- Donner une équation cartésienne de la tangente T à C au point d'abscisse nulle.
7- Tracer D, T et la partie de la courbe C correspondant aux points dont l'abscisse appartient à l'intervalle [0,4].
8- Soit g la fonction définie sur [0,+∞[ par g(x) = eˣ/(eˣ + 1).
 a) déterminer une primitive de g sur [0,+∞[.
 b) Vérifier que pour tout x de [0,+∞[ on a 1/(eˣ + 1) = 1 − g(x).
 c) en déduire une primitive de f sur [0,+∞[

---------------------------------------------------------------------
#### MATH CULTURE (p.114) — « John Napier (1550 ; 1617) » (portrait gravé)
---------------------------------------------------------------------
Texte (verbatim) : « A la fin du XVIe et au début du XVIIe siècle, l'astronomie se développe considérablement. L'étude du mouvement des planètes conduit à de longs et pénibles calculs. Les banquiers sont aussi confrontés à des calculs fastidieux car ils calculent les intérêts dans une économie occidentale dopée par l'exploitation des terres découvertes. Il n'est pas étonnant que les mathématiciens cherchent alors les méthodes simplificatrices de calcul, L'idée est simple : remplacer des multiplications par des additions, mais la réalisation est difficile. C'est l'écossais John Napier qui inventa un algorithme par lequel une addition remplaçait une multiplication. Un fait est remarquable, du temps de Napier, On ne connaît ni les limites ni les dérivées, et Neper n'a donc pas inventé la fonction logarithme.
Le premier à s'intéresser de façon sérieuse au nombre e est le mathématicien suisse Leonhard Euler (1707 ; 1783). C'est à lui que nous devons le nom de ce nombre. En 1748, Euler explique que : e = 1 + 1/1! + 1/2! + 1/3! + ... Par cette formule, il obtient une estimation de e avec 18 décimales exactes.
Les premières décimales du nombre e sont : e=2,71828182845904523536028747 1352662497757247093699959574966967 6277240766303535475945713821785251 664274…
Les applications du nombre e sont variées. Nous retrouvons la fonction exponentielle en économie (calculs des intérêts versés de façon continue), en biologie (mesure de la multiplication des cellules vivant dans un organisme), en sciences physiques …
Voici un extrait du "Théorème du perroquet" de Denis Guedj qui donne une représentation concrète du nombre e : « Suppose qu'il y a un an tu aies amassé une épargne qui nous permettra de payer notre voyage pour Manaus. Soit E, cette épargne. Tu l'as placé en attendant. Ton banquier t'a proposé un taux d'intérêt surprenant : 100 % ! Ne rigole pas, ça s'est vu. Rêve ! Calcule ! Au bout d'un an, tu aurais eu E + E = 2E. Tu aurais doublé ton épargne. Si au lieu de toucher les intérêts à la fin de l'année, tu les avais touchés tous les six mois et que tu les aies replacés, au bout d'un an ça t'aurait fait E(1 + 1/2)². Calcule Tu aurais plus que doublé ton épargne tu aurais 2,25E. Si au lieu de toucher les intérêts tous les six mois, tu les avais touchés tous les trimestres et que tu les aies replacés, au bout de l'année, ça t'aurait fait E(1 + 1/4)⁴. Calcule ! Tu aurais gagné encore plus : 2,441E. Si tu les avais touchés tous les mois et que tu les aies replacés, ça t'aurait fait E(1 + 1/12)¹². Calcule ! 2, 596E. Encore plus ! Puis, tous les jours : E(1 + 1/365)³⁶⁵. Encore plus toutes les secondes, encore plus. Et puis, tous les riens du tout, « en continu ». Tu n'en peux plus, tu t'envoles, tu planes, tu te dis que c'est Byzance, que ton épargne va doubler, qu'il va quadrupler, décupler, centupler, millionupler, milliardupler, [ ... ] Tes intérêts composés, ils ont beau se décomposer, eh bien, à l'arrivée, tu n'a même pas le triple de ton épargne, ni même 2,9 fois plus, ni même 2,8 fois plus, ni même 2,75 fois plus, ni même 2,72 fois plus... Tu as seulement 2, 71 828 1828 !! ... fois plus. Mon pauvre, après toute cette richesse, te voilà seulement e fois moins pauvre qu'au départ ! ». »
Sources citées : Denis Guedj, « Le Théorème du perroquet » ; John Napier (portrait) ; Leonhard Euler.

---------------------------------------------------------------------
#### VOCABULAIRE OFFICIEL de la section
---------------------------------------------------------------------
fonction logarithme népérien (ln ou Log) ; primitive qui s'annule en 1 ; propriété fondamentale (ln(ab) = ln a + ln b) ; ensemble de définition ; fonction réciproque ; bijection de ]0,+∞[ sur IR ; le nombre e (e ≃ 2,71828…, unique solution de ln x = 1) ; fonction exponentielle de base e (exp, eˣ) ; fonction exponentielle de base a (x ↦ aˣ = e^{x ln a}) ; limites usuelles (croissances comparées) ; asymptote verticale ; branche parabolique de direction l'axe des abscisses / des ordonnées ; tangente ; point d'inflexion ; tableau de variation ; taux mensuel équivalent ; valeur acquise ; coût total, coût moyen, coût marginal ; fonction d'offre, fonction de demande, prix d'équilibre, quantité d'équilibre ; bénéfice.

**Bornes INCLUS** : définition de ln comme primitive de 1/x s'annulant en 1 ; ln(ab), ln(a/b), ln(1/a), ln √a, ln(aⁿ) (n ∈ ℤ) ; limites en +∞ et 0⁺ (ln x, ln x/xⁿ, xⁿ ln x), ln x/(x−1) en 1, ln(1+x)/x en 0 ; dérivée de ln|u| et primitive de u'/u ; étude et courbe de ln ; exp réciproque de ln, propriétés, limites (eˣ en ±∞, eˣ/xⁿ, xⁿeˣ, (eˣ−1)/x), dérivée de e^u et primitive de u'e^u ; fonction x ↦ aˣ (étude, courbes, bijection réciproque log_a présente dans Activité 3 p.102 sous la forme g⁻¹(x) = −ln x/ln 3) ; équations/inéquations avec ln et exp ; applications économiques (placements, taux équivalents, coût, bénéfice, offre/demande).
**EXCLU** (non traité dans cette tranche) : logarithme décimal log₁₀ (absent), logarithme de base a comme chapitre (non défini), équations différentielles (y' = ay), intégrale (Chapitre V, p.115 et suivantes), formules de dérivation de a^x en dehors de ln a·aˣ, étude des suites géométriques (Chap. VI).

**Notions-clés (≤ 8)** : (1) définition de ln comme primitive de 1/x s'annulant en 1 ; (2) ln(ab) = ln a + ln b et conséquences ; (3) limites usuelles du ln (croissances comparées) ; (4) tableau de variation et courbe de ln, nombre e ; (5) exp réciproque de ln, eˣ et propriétés ; (6) dérivée de ln|u| et de e^u, primitives associées ; (7) x ↦ aˣ = e^{x ln a} et équations/inéquations exponentielles ; (8) modèles économiques (intérêts composés, taux équivalent, coût moyen minimal, bénéfice).

---------------------------------------------------------------------
#### § NOTES
---------------------------------------------------------------------
**Pages lues** : 30/30 (85 à 114). Chaque page lue à l'image (110 dpi) ; la couche texte (pdftotext) a servi à la prose (p.86-88 et p.114 intégralement) et à recouper. La p.85 est la page de titre du chapitre (sommaire/plan) sans contenu mathématique : lue à l'image seulement (couche texte vide).

**Pages sondées à agrandissement (170-220 dpi)** : p.96 (exercice 4 a/b/c, texte vs image), p.99 (Activité 9, fonction f et Partie A/B), p.106 (exercices 14-15, exposants de 15 f), p.112 (exercice 34, exposants de f et g). Résultat : voir coquilles ci-dessous. Graphiques non quantifiés : p.86 (Act. 2), p.87, p.92, p.96, p.103, p.107 (ex. 20), p.110 (ex. 32) — décrits qualitativement, lecture approximative signalée.

**Coquilles imprimées (reproduites telles quelles et signalées)** :
- p.86 Pour commencer Act. 1, q.1 : « Vérifier que la fonction F, définie … par f(x) = x²/(x+1) » — la fonction est notée f au lieu de F (coquille de casse).
- p.88-89 : la propriété 1 (p.90) « Pour tout réel on a : ln(1/a) = −ln(a) » omet la condition a > 0.
- p.90 Act. 7, q.1 : « On donne ln 2 ≃ 0,7 et ln 3 ≃ 0,1 » — valeur imprimée ln 3 ≃ 0,1 incohérente avec la réalité (ln 3 ≈ 1,1) et avec le cours (ln 3 > ln 2). Probablement 1,1. Les résultats attendus A, B dépendent de cette valeur : ne pas l'utiliser telle quelle dans un exercice sans correction [?].
- p.93 Act. 5 : « 5) α ∈ ]0,1 ; 0,2[ et β ∈ ]3,1 ; 3,2[ » — sans coquille, intervalles à virgule décimale, vérifiés (f(0,1)>0>f(0,2) ; f(3,1)<0<f(3,2)) ; à lire avec soin car le point-virgule sert de séparateur.
- p.93 Act. 6 : « courbes représentatives respectives de f et g » (ordre inversé : C_g et C_f) ; q.3 « la courbe C » (non définie).
- p.93-94 Act. 8 : q.3 « courbes représentatives de f et de g » — f n'est pas définie dans l'énoncé (c'est q) ; q.4 « p0 et q0 » alors que le prix d'équilibre a été noté x0.
- p.94 Act. 2 (exp), q.2-a) : « Montrer que g est continue … » ; g non définie (exp).
- p.96 q.4-a) : « eˣ(1+eˣ) = 1 + e^{2x} » faux en général (vrai pour eˣ+e^{2x}) — vérifié à l'image (200 dpi). Coquille du manuel.
- p.99 Act. 9 : f(x) = eˣ/(eˣ − 1) « définie sur IR » alors que eˣ − 1 = 0 pour x = 0 : f n'est pas définie en 0 (domaine IR*) ; la Partie A (g(x)= eˣ − x − 1 ; « eˣ − x strictement positif ») suggère que la fonction visée est f(x) = eˣ/(eˣ − x) [?]. À l'image (220 dpi) : dénominateur imprimé « eˣ − 1 ». À ne pas corriger sans arbitrage.
- p.102 Act. 2 : numérotation 1-, 2-, 4- (pas de 3-).
- p.103 : étape 1 « Définir les variables i et aire » (phrase sans rapport avec la feuille de calcul).
- p.104 ex. 5 : étiquettes a), b), a), d) (le 3e item devrait être c) ; les items vont donc a-b-« a »-d-e-f-g-h) ; ex. 6 : étiquettes a-b-c-d-e-g (pas de f).
- p.105 ex. 10 : f définie « sur ]0,+∞[ » avec f(0) = 0 (domaine [0,+∞[ visé).
- p.106 ex. 13 : sous-questions de 5 numérotées « a) » puis « c) ».
- p.106 ex. 15 f) : « 2e^{−0,5+7} = 1 » imprimé tel quel (exposant constant, 2e^{6,5} ≠ 1 : équation sans solution) ; probablement −0,5x + 7 visé [?]. g) « e^{0,1x−2} = 0 » : sans solution (présent peut-être à dessein).
- p.106 ex. 16 : 2-a) et 2-b) répètent la même équation (ln x)⁴ − 10(ln x)² + 9 = 0.
- p.109 ex. 29 q.3 : « la figure précédente » — aucune figure.
- p.113 ex. 35 B : 1 ≤ x ≤ 20 : f est celle de A (non rappelée) ; coût de fabrication de 600, 1000, 1200 objets = f(6), f(10), f(12) (centaines).
- p.114 Math culture : « 2, 596E » (valeur impr. 2,596E) ; « 2,441E » imprimé (valeur exacte (1+1/4)⁴ = 2,4414) ; « Tu as seulement 2, 71 828 1828 !! » (imprimé tel quel) ; portrait légendé « John Napier (1550 ; 1617) » (légende du portrait).

**Incohérences de chiffres** : aucune entre énoncé et synthèse dans cette tranche, hors p.90 (ln 3 ≃ 0,1). Totaux de tableaux : tableau p.89 act. 3 : 7 lignes × 3 réponses ; tableau p.112 33-II-A : 11 colonnes (1 ; 1,5 ; 2 ; 2,5 ; 3 ; 3,5 ; 4 ; 4,5 ; 5 ; 5,5 ; 6) comptées.

**Recouvrements de cohérence recalculés** (calculs de la fiche, non du manuel) : ex. 30 f'(x) et C'_m = f/(2x²) ; ex. 32 f'(x) = (x²−2x−1)/(x+1) ; ex. 33 C_m' = f/(4x²) ; ex. 34 g(x) = x/20 − e^{…}.

**`[?]` restants** : (1) ln 3 ≃ 0,1 (p.90) valeur douteuse ; (2) f de l'activité 9 p.99 (eˣ − 1 vs eˣ − x au dénominateur) ; (3) exposant de 15 f) ; (4) lectures graphiques approchées (ex. 20 p.107, ex. 32 p.110). Pas d'autre doute substantiel.

---

### Chapitre `m05-p115-136`

### m05 — Chapitre V « Intégrale d'une fonction continue » (pp. 115-136) — Bac Économie et gestion, Mathématiques

Source : manuel CNP `222463P00.pdf` (Mathématiques, 4e année secondaire, économie et gestion). Page PDF = page imprimée. Sommaire du chapitre (p.115) : Pour commencer · Cours (Définition et propriétés ; Intégration par parties ; Valeur moyenne ; Calcul d'aires planes) · Avec l'ordinateur · Exercices et problèmes · Math culture.

Convention : $\int_a^b f(t)\,dt$ ; IR = ℝ comme imprimé.

---
#### POUR COMMENCER (p.116)

##### Activité 1 (p.116)
Énoncé : « Dans chacun des cas suivants, montrer que la fonction f admet une primitive sur l'intervalle I et déterminer celle qui s'annule en1 : »
- a) f : x ↦ x² − x − 1, I = IR
- c) [sic, étiquette « c) » imprimée deux fois] f : x ↦ −1/x³, I = ]0,+∞[
- c) [sic] f : x ↦ (2x+1)/(x²+x+1)², I = IR
- d) f : x ↦ x/√(x²+2), I = IR
Corrigé : non donné.

##### Activité 2 (p.116)
Situation : coût marginal d'un produit, en centaines de dinars par tonne.
Données : f(x) = 4x³ − 6x² + 50, quantité de production x comprise entre 0 et 5 tonnes ; coûts fixes 1000 dinars.
Travail : « Déterminer le coût total de production de x tonnes sachant que les coûts fixes s'élèvent à 1000 dinars. »
Corrigé : non donné. (Piège d'unités à noter : f en centaines de dinars/tonne, coûts fixes en dinars.)

##### Activité 3 (p.116)
« On donne la représentation graphique d'une fonction f sur l'intervalle [−4, 2] » : graphique à image (courbe C = segment de droite, région hachurée sous C au-dessus de l'axe des abscisses entre x=−4 et x=2 ; repère quadrillé, unité 1 sur chaque axe). Lecture à l'image (non chiffrée dans le texte) : la droite passe par (−4 ; 1), (0 ; 3) et (2 ; 4), soit f(x) = x/2 + 3 ; la région est un trapèze.
Travail :
1- Justifier que f admet une primitive F sur [−4, 2].
2- Expliciter f(x) pour x dans [−4, 2].
3- Donner une primitive F de f sur [−4, 2], puis calculer F(2) – F(–4)
4- Déterminer l'aire A de la région hachurée (en unités d'aire ).
5- Comparer A et (F(2) – F(–4) .  [parenthèse non refermée imprimée]
Corrigé : non donné. (Lecture de l'image : aire trapèze = (1+4)/2 × 6 = 15, à vérifier par l'auteur du chapitre — c'est une lecture graphique, pas un chiffre du manuel.)

---
#### COURS — I- Définition et propriétés

##### 1) Définition (pp.117-118)

**Activité 1 (p.117)** Soit f la fonction définie sur IR par f(x) = x² − x + 1.
1- Montrer que f admet au moins une primitive sur IR.
2- Déterminer la primitive F de f sur IR qui prend pour valeur 1 en -2.
3- Donner une autre primitive G de f sur IR.
4- Comparer F(b) − F(a) et G(b) − G(a).

**Activité 2 (p.117)** Soient f une fonction continue sur un intervalle I, F et G deux primitives de f sur I.
1- Montrer que pour tous réels a et b de I, G(b) − G(a) = F(b) − F(a).
2- En déduire que le réel J = F(b) − F(a) ne dépend pas du choix de la primitive de f sur l'intervalle I.

**Définition (encadré, p.117)** « Soit f une fonction continue sur un intervalle I contenant deux réels a et b. On appelle intégrale de f entre a et b et on note $\int_a^b f(t)\,dt$, le réel défini par $\int_a^b f(t)\,dt = F(b) − F(a)$ où F est une primitive de f sur I. »

**Remarques (encadré, p.117)**
1) L'écriture $\int_a^b f(t)\,dt$ se lit « Intégrale (ou somme ) de a à b de f(t) dt »
2) Dans l'écriture $\int_a^b f(t)\,dt$, on peut remplacer la lettre t par toute autre lettre autre que a et b, par exemple : $\int_a^b f(t)dt = \int_a^b f(x)dx = \int_a^b f(y)dy = ....$
3) On écrit $\int_a^b f(t)dt = [F(t)]_a^b$ (On lit F(t) pris entre a et b ) $= F(b) − F(a)$
4) Lorsque a < b, le réel $\int_a^b f(t)dt$ est appelé intégrale de f sur [a, b].

**Activité 3 (p.118)** Calculer les intégrales suivantes :
$\int_{-1}^{3} a\,dt$ (a ∈ IR) ; $\int_0^2 2t\,dt$ ; $\int_0^1 x^3 dx$ ; $\int_{-1}^{1} 2e^{2x+1}dx$ ; $\int_1^2 \frac{x+1}{x^2+x}dx$ ; $\int_1^2 \frac{2x+1}{(x^2+x)^2}dx$.

**Activité 4 (p.118)**
1- Soit f la fonction définie sur ]0,+∞[ par f(x) = ln x / x.
 a- Vérifier que la fonction F définie par F(x) = (1/2)(ln x)² est une primitive de f sur ]0,+∞[.
 b- En déduire $\int_1^e \frac{\ln(t)}{t}dt$.
2- Soit f la fonction définie sur IR par f(x) = x/√(x²+1).
 a- Justifier que f admet au moins une primitive sur IR.
 b- Calculer $\int_0^1 f(t)dt$.

##### 2) Propriétés (pp.118-121)

**Relation de Chasles — Activité 1 (p.118)** Soient f continue sur un intervalle I et F une primitive de f sur I.
1- Vérifier que pour tous réels a, b et c de I on a : $\int_a^c f(t)dt + \int_c^b f(t)dt = \int_a^b f(t)dt$.
2- En déduire que $\int_a^a f(t)dt = 0$ et que $\int_a^b f(t)dt = −\int_b^a f(t)dt$.

**Propriétés (encadré, p.118)** Soit f une fonction continue sur un intervalle I
- Pour tous réels a, b et c de I on a $\int_a^b f(t)dt = \int_a^c f(t)dt + \int_c^b f(t)dt$ (Relation de Chasles)
- Pour tout réel a de I on a $\int_a^a f(t)dt = 0$
- Pour tous réels a et b de I on a $\int_a^b f(t)dt = −\int_b^a f(t)dt$. (inversion des bornes)

**Activité 2 (p.119)**
1- On considère la fonction f définie sur IR f(x) = |x − 1|
 a) Calculer les intégrales : $\int_0^1 f(t)dt$ et $\int_1^3 f(t)dt$.
 b) En déduire la valeur de l'intégrale $\int_0^3 |t − 1|dt$
2- Calculer de même les intégrales suivantes : $\int_1^3 (|x − 2| + x^2)dx$ ; $\int_1^e |1 − 2/t|dt$.

**Linéarité de l'intégrale — Activité 1 (p.119)** Soient f et g continues sur un intervalle I contenant a et b. F et G deux primitives respectives de f et de g sur I.
1- Montrer que $\int_a^b (f(t)+g(t))dt = \int_a^b f(t)dt + \int_a^b g(t)dt$.
2- Soit k ∈ IR, montrer que $\int_a^b k.f(t)dt = k\int_a^b f(t)dt$.
3- En déduire que pour tous réels α et β, $\int_a^b (αf(t)+βg(t))dt = α\int_a^b f(t)dt + β\int_a^b g(t)dt$.

**Propriétés (encadré, p.119)** Soient f et g deux fonctions continues sur un intervalle I contenant a et b.
* $\int_a^b (f(t)+g(t))dt = \int_a^b f(t)dt + \int_a^b g(t)dt$.
* Pour tout réel k on a $\int_a^b k.f(t)dt = k\int_a^b f(t)dt$

**Activité 2 (p.119)** Soit f une fonction continue sur l'intervalle [-1, 2]. Sachant que : $\int_{-1}^2 f(t)dt = 1/2$, calculer les intégrales suivantes :
a) $\int_{-1}^2 4f(t)dt$ ; b) $\int_{-1}^2 (f(t) − e^t)dt$ ; c) $\int_{-1}^2 (3e^t − 2f(t))dt$

**Activité 3 (p.120)** Soit f la fonction définie sur ]0,+∞[ par f(t) = t ln t − t.
a- Montrer que f est dérivable sur ]0,+∞[ et que f'(t) = ln t.
b- Calculer I = $\int_1^e \ln t\,dt$.
c- En déduire J = $\int_1^e \ln 3t\,dt$ et K = $\int_1^e \ln(t^2)dt$.

**Intégrales et ordre — Activité 1 (p.120)** Soient f continue sur un intervalle I et F une primitive de f sur I. On suppose que pour tout x de I on a f(x) ≥ 0.
1- a) Justifier que la fonction F est croissante sur I.
 b) En déduire que si a et b sont deux éléments de I tels que a ≤ b alors $\int_a^b f(x)dx ≥ 0$.
2- Soient u et v deux fonctions continues sur un intervalle [a,b]. Montrer que : si pour tout x de [a,b] u(x) ≤ v(x) alors $\int_a^b u(x)dx ≤ \int_a^b v(x)dx$.

**Propriétés (Positivité et comparaison d'intégrales) (encadré, p.120)**
1) Soit f une fonction continue sur un intervalle [a,b]. Si pour tout réel x de [a,b] on a f(x) ≥ 0 alors $\int_a^b f(x)dx ≥ 0$.
2) Soient f et g deux fonctions continues sur un intervalle [a,b]. Si pour tout réel x de [a,b] on a f(x) ≤ g(x) alors $\int_a^b f(t)dt ≤ \int_a^b g(t)dt$

**Activité 2 (p.120)** Soit f la fonction définie sur ]0,+∞[ par f(x) = e^{1/x}.
a- Montrer que f est strictement décroissante sur ]0,+∞[.
b- En déduire que pour tout x de [2,3] on a 1,39 ≤ f(x) ≤ 1,64.
c- Donner alors un encadrement de I = $\int_2^3 e^{1/x}dx$.

**Activité 3 (p.121)** Soit f la fonction définie sur ]0,+∞[ par f(x) = x − 1 − ln x
1- a- Déterminer le sens de variation de f sur ]0,+∞[.
 b- Calculer f(1) et en déduire que pour tout x de ]0,+∞[, on a f(x) ≥ 0.
2- Prouver que $0 ≤ \int_1^2 \ln x\,dx ≤ 1/2$.

**Activité 4 (p.121)** Soit f la fonction définie sur IR par f(x) = x² − 1.
a- Calculer $\int_0^2 f(t)dt$.
b- Déterminer le signe de f sur [0, 2].
c- Est il vrai que si (a ≤ b et $\int_a^b f(t)dt ≥ 0$) alors f est positive sur [a, b].

---
#### COURS — II- Intégration par parties (pp.121-122)

**Activité 1 (p.121)** Soient u et v deux fonctions dérivables sur un intervalle I de IR
1- a) Déterminer une primitive sur I de la fonction : u'v + uv'.
 b) En déduire une primitive sur ]0,+∞[ de la fonction x ↦ x ln x + (x²/2)·(1/x).
 c) Calculer $\int_1^e (x\ln x + \frac{x^2}{2}\cdot\frac{1}{x})dx$ puis $\int_1^e x\ln x\,dx$.
2- En s'inspirant de la question 1-, calculer les intégrales $\int_0^1 xe^x dx$ puis $\int_0^1 x^2 e^x dx$.

**Théorème (encadré, p.121)** « Soient u et v deux fonctions dérivables sur un intervalle [a,b] dont les dérivées u' et v' sont continues sur [a,b]. On a $\int_a^b u'(x)v(x)dx = [u(x)v(x)]_a^b − \int_a^b u(x)v'(x)dx$ »

**Remarque (encadré, p.121)** « On utilise la méthode d'intégration par parties, chaque fois que l'on veut calculer une intégrale de la forme $\int_a^b u'(x)v(x)dx$, dont le calcul direct n'est pas simple alors que celui de l'intégrale $\int_a^b u(x)v'(x)dx$ l'est. »

**Activité 2 (p.122)**
1- Calculer chacune des intégrales suivantes à l'aide d'une intégration par parties :
 a) I = $\int_2^0 (2t − 1)e^t dt$ [bornes imprimées 2 en bas, 0 en haut] b) J = $\int_1^e (x + 1)\ln x\,dx$ c) $\int_0^π t\cos t\,dt$
2- A l'aide de deux intégrations par parties successives, calculer les intégrales I = $\int_0^π t^2\sin t\,dt$ et J = $\int_2^0 (x^2 − x)e^x dx$. [bornes 2 en bas, 0 en haut, comme imprimé]

---
#### COURS — III- Valeur moyenne (pp.122-124)

**Activité 1 (p.122)** Situation : une entreprise fabrique un produit en quantité x, avec x ∈ [0, 700]. Coût total de fabrication exprimé en dinars : C(x) = 0.02x² + 2500x (point décimal imprimé).
1- Déterminer le coût marginal C'(x) pour x ∈ [0, 700].
2- Calculer le coût moyen m pour 700 objets fabriqués.
3- Calculer I = $\frac{1}{700}\int_0^{700} C'(x)dx$
Texte : « On obtient m = I, nous dirons que dans ce cas que le coût moyen de fabrication de 700 objets est égal à la moyenne du coût marginal entre 0 et 700 objets fabriqués. »

**Définition (encadré, p.122)** « Soit f une fonction continue sur un intervalle [a , b]. On appelle valeur moyenne de f sur [a , b] et on note $\bar f$ le réel $\bar f = \frac{1}{b−a}\int_a^b f(t)dt$. »

**Activité 2 (p.122)** f définie sur [−2,3] par f(x) = 3x² − 2x. Calculer la valeur moyenne $\bar f$ de f sur [−2,3].

**Activité 3 (p.122)** f définie sur IR par f(x) = e^{1−x}.
1- Calculer la valeur moyenne m₁ de f sur l'intervalle [1,4], puis la valeur moyenne m₂ de f sur l'intervalle [4,8].
2- Soit m la valeur moyenne de f sur l'intervalle [1,8]. Vérifier que m = (3m₁ + 4m₂)/7.

**Activité 4 (p.123)** Situation : marché d'un produit, quantité q en tonnes, prix unitaire p en dinars par kilogramme.
Données : « La courbe d'offre d'un produit est définie par la relation liant quantité offerte q (en tonnes) et prix unitaire p (en dinars par kilogramme) : $p_O = 10×(1,01)^q$. La courbe de demande est définie par la relation liant quantité demandée et prix unitaire : $p_d = 50×(0,98)^q$. » Graphique : deux courbes (repère : graduations 10 et 50 en ordonnée ; 10, 50 et 60 en abscisse) ; la courbe décroissante part de 50, la courbe croissante part de 10 ; légende imprimée : bleu (croissante) « Prix unitaire en fonction de la quantité demandée », rose (décroissante) « Prix unitaire en fonction de la quantité offerte ».
1- Déterminer une valeur arrondie entière q_e de la quantité d'équilibre. (« la quantité d'équilibre correspond à l'égalité du prix d'offre et du prix de la demande »)
2- Déterminer alors la valeur arrondie entière du prix d'équilibre p_e.
3- On admet que la valeur moyenne du prix d'offre des producteurs pour une quantité de a tonnes à b tonnes est égale à $\frac{1}{b−a}\int_a^b p_O(q)dq$.
 a) Calculer la valeur moyenne du prix d'offre des producteurs pour une quantité de 50t à 60t.
 b) Comparer cette valeur moyenne avec le prix d'équilibre p₀ [sic : « p_0 » imprimé, p_e attendu].
Corrigé : non donné. Anomalie de légende : la courbe croissante (10 → …, prix d'offre) est légendée « demandée » et la décroissante (50 → …, demande) « offerte » : légende inversée par rapport aux formules.

---
#### COURS — IV- Calcul d'aires planes (pp.123-126)

**Activité 1 (p.123)** f définie sur IR par f(x) = |x/2 + 1| (écrit |(1/2)x + 1|).
1- Représenter graphiquement la fonction f dans un repère orthonormé (O, i, j) (l'unité étant 1cm)
2- Calculer en cm², l'aire A de la région du plan limitée par la courbe C de f, l'axe des abscisses et les droites d'équations x = -4 et x = 2.
3- Calculer l'intégrale I = $\int_{-4}^2 |\frac12 x + 1|dx$.
4- Vérifier que A = I.

**Activité 2 (p.124)** « On donne le graphique suivant : » (repère quadrillé, courbe C = droite descendante, région hachurée en triangle de x=1 à x=4 au-dessus de l'axe puis petit triangle sous l'axe de x=4 à x=5 ; graduations 1, 4, 5 en abscisse, 1 et 3 en ordonnée).
1- Vérifier que C est la représentation graphique de la fonction f définie sur [1 , 5] par f(x) = –x + 4
2- Calculer l'aire A de la région hachurée sur le graphique.
3- Calculer $\int_1^5 |f(x)|dx$.
4- Vérifier que $\int_1^5 |f(x)|dx = A$.

**Théorème (encadré, p.124)** « Soient a et b deux réels tels que a ≤ b, f une fonction continue sur l'intervalle [a ; b], et C sa courbe représentative dans un repère orthogonal (O, OI, OJ). (l'unité d'aire notée u.a. , est l'aire du rectangle OIJK) $\int_a^b |f(x)|dx$ est l'aire, en u.a. , du domaine plan compris entre la courbe C, l'axe des abscisses et les droites d'équations x = a et x = b. » (figure : courbe C, rectangle OIJK d'unité d'aire, domaine grisé entre x=a et x=b au-dessus de l'axe.)

**Activité 3 (p.124)** f définie sur [−2,1] par f(x) = x³ − 3x + 3. C = courbe représentative de f dans un repère orthonormé du plan. Figure : courbe C_f (maximum visible vers x=−1, valeur lue 5 ; graduations +1…+5 en ordonnée, −2, −1, +1, +2 en abscisse), rectangle ABCD bleu, hauteur h.
1- Calculer l'aire A en unités d'aire, de la partie du plan délimitée par la courbe C, l'axe des abscisses et les droites d'équations x = -2 et x = 1.
2- Calculer la valeur moyenne $\bar f$ de f sur l'intervalle [-2,1].
3- On considère le rectangle ABCD de la figure (tel que A(-2,0) et B(1,0)).
 a) Déterminer la largeur h du rectangle ABCD pour que son aire soit égale à A. [sic : « largeur h » alors que h est la hauteur sur la figure]
 b) Vérifier que h = $\bar f$.
(Vérifié à l'image : f(−2)=1, f(1)=1, f(−1)=5 concordent avec la courbe.)

**Activité 4 (p.125)** f définie sur IR par f(x) = e^{−x}.
1- Dresser le tableau de variation de f.
2- Tracer la courbe représentative de f dans un repère orthonormé du plan. (l'unité graphique étant 1 cm).
3- Calculer l'aire en cm² de la région du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations x = 1 et x = 2.
4- a- Soit λ > 1, calculer en fonction de λ, l'aire A(λ) de la région du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations x = 1 et x = λ.
 b- Calculer $\lim_{λ→+∞} A(λ)$.

**Activité 5 (p.125)** « Dans le graphique ci-contre, C_f et C_g représentent respectivement les fonctions f et g définies par f(x) = 1/x et g(x) = x². On se propose de calculer l'aire A de la partie du plan limitée par les courbes C_f, C_g et les droites d'équations respectives x = 1/2 et x = 1. » (figure : C_f décroissante, C_g convexe croissante, se coupant en x=1 ; région bleue entre elles de x=1/2 à x=1 ; graduations 1/2, 1 en abscisse, 1 en ordonnée.)
1- Colorier la région du plan limitée par la courbe C_f, l'axe des abscisses et les droites d'équations respectives x = 1/2 et x = 1.
2- Colorier (par une autre couleur) la région du plan limitée par la courbe C_g, l'axe des abscisses et les droites d'équations respectives x = 1/2 et x = 1.
3- En déduire la valeur de A et la comparer à $\int_{1/2}^{1} |f(t) − g(t)|dt$.

**Théorème (encadré, p.125)** « Soient f et g deux fonctions continues sur un intervalle [a,b]. L'intégrale $\int_a^b |f(t) − g(t)|dt$ est l'aire, en unités d'aire, de la région du plan limitée par les courbes représentatives de f et de g et des droites d'équations x = a et x = b. »

**Activité 6 (p.126)** « Dans chacun des cas suivants, on donne deux fonctions f et g ainsi que leurs courbes représentatives dans un repère orthonormé du plan. Calculer dans chacun des cas suivants l'aire (en unité d'aire) du domaine colorié. »
a) f(x) = x² − 6x + 10 et g(x) = −x² + 8x − 10 ; (figure : C_f parabole de minimum (3 ; 1), C_g parabole de maximum (4 ; 6), croisement lus en x=2 et x=5 ; domaine coloré entre les deux)
b) f(x) = 1/x et g(x) = ln(x) + 1 (figure : croisement en x=1, domaine coloré de x=1 à x=e entre C_g au-dessus et C_f ; graduations 1, 2, e, 3 en abscisse)
(Vérifié par calcul : f=g ⇔ x²−7x+10=0, x=2 ou 5, cohérent avec la figure.)

**Activité 7 (p.126)** f et g définies sur ]0,+∞[ par f(x) = 2x − 1/x² − 15/4 et g(x) = x − 2. C et C' = courbes représentatives de f et de g dans un repère orthonormé (O, i, j) (L'unité graphique étant 2cm).
1- a- Montrer que pour tout x > 0 on a f(x) − g(x) = (x − 2)(4x² + x + 2) / (4x²).
 b- En déduire les positions relatives de C et C'.
2- Calculer l'aire (en cm²) du domaine compris entre C, C' et les droites d'équations x = 1 et x = 3.
(Identité vérifiée : f−g = x − 1/x² − 7/4 = (4x³−7x²−4)/(4x²) = (x−2)(4x²+x+2)/(4x²).)

---
#### AVEC L'ORDINATEUR (pp.127-128)

**Texte (p.127)** « On se propose de compléter les travaux pratiques du chapitre étude de fonctions en calculant l'intégrale de f entre a et b d'une part, et l'aire de la région du plan limitée par la courbe de f, l'axe des abscisses et les droites d'équations respectives x = a et x = b d'autre part. »
**Étape 1 : Définition des variables** — Les cellules A3, A4, A5, B3, B4, B5, B7 et C7 sont définies dans le chapitre étude de fonctions. Dans la cellule D3 taper : « Intégrale de f » ; dans la cellule D4 taper : « Aire A ». Définir les variables i et aire : sélectionner la cellule B3, menu ‘Insertion’ → commande ‘nom’ → ‘définir’, taper la lettre : i ; valider. Sélectionner la cellule B4, même menu, taper : aire ; valider.
**Étape 2 : Programmation de la fonction et de la procédure de remplissage du tableau de valeurs** — afficher l'éditeur de code de Visual Basic et taper (code reproduit, p.127-128) :
```
Function f(x)
   On Error GoTo Erreur
    f = x / (x ^2 + 1)              ' On peut considérer toute autre fonction
   Exit Function
Erreur:
   f = ""
   Resume Next
End Function
Function Intégrale(a, b)
    i=0                      'calcul de l'intégrale de f(x)dx de a jusqu'à b
   aire =                    'le calcul reste correct même si b<a      [R7 : vérifié à 250 dpi — « aire = » est imprimé SANS valeur (absente, non illisible) ; coquille du manuel]
   x=a
  dx = (b - a) / 100 'dx est négatif lorsque a>b ' pour plus de précision on peut diviser par 1000 au lieu de 100
  Do
      i = i + f(x) * dx                 ' valeur cumulée de l'intégrale
      aire = aire + Abs(f(x)) * dx      ' valeur cumulée de l'aire
      x = x + dx
   Loop While (dx > 0 And x < b) Or (dx < 0 And x > b)   ' cette condition tient compte des 2 cas possibles a<b et b<a
    Cells(4, 5) = aire
  Intégrale = i
End Function            ' Reprise de la procédure considérée dans le chapitre
Sub calculs()           ' étude de fonctions
  a = Cells(3, 2)
  b = Cells(4, 2)
  h = Cells(5, 2)
  i=8
  x=a
  Do While i <= 100
    Cells(i, 2) = ""
    Cells(i, 3) = ""
    i=i+1
  Loop
  i=8
  Do While x <= b
    Cells(i, 2) = x
    Cells(i, 3) = f(x)
    x=x+h
    i=i+1
  Loop
  Cells(3, 5) = Intégrale(a, b)       ' appel de la fonction intégrale
End Sub
```
**Étape 3 : Remplissage du tableau de valeurs et traçage de la courbe** (étapes décrites dans le chapitre étude de fonctions). « Cliquer sur le bouton ajouté (ici libellé Graphisme) et le tableau se remplit en fonction des valeurs et de la fonction choisies. » Capture d'écran (p.128, lue à 220 dpi) : A1 = « f(x) = 4/(1+x²) » ; a = −2, b = 2, h = 0,1 ; « Intégrale de f » = −0,016 ; « Aire A » = 1,609139203 ; tableau x/y : −2 → −0,4 ; −1,9 → −0,41215 ; −1,8 → −0,42453 ; −1,7 → −0,43702 ; −1,6 → −0,44944 ; −1,5 → −0,46154 ; −1,4 → −0,47297 ; −1,3 → −0,48327 ; −1,2 → −0,4918 ; −1,1 → −0,49774 ; −1 → −0,5 ; −0,9 → −0,49724 ; −0,8 → −0,4878 ; −0,7 → −0,4698 ; −0,6 → −0,44118 ; −0,5 → −0,4 ; −0,4 → −0,34483 ; −0,3 → −0,27523 ; −0,2 → −0,19231 ; −0,1 → −0,09901 ; courbe en S de −0,5 à +0,5.
Clôture : « On peut traiter une autre fonction, pour cela il faut activer l'éditeur visual basic (menu outils, macro, éditeur visual basic) ou simplement à l'aide du raccourci clavier Alt+F11, puis modifier la fonction ou éventuellement ajouter de nouvelles procédures. »
Anomalies : (i) l'étiquette A1 « 4/(1+x²) » ne correspond pas au code `f = x/(x^2+1)` ni aux valeurs du tableau (x/(1+x²) : f(−2) = −0,4, f(−1) = −0,5) ; (ii) « Intégrale de f » = −0,016 est une somme de Riemann (le code fait aussi un pas de plus que b) pour une fonction impaire sur [−2 ; 2] (valeur exacte 0) ; Aire = 1,609139203 proche de ln 5 = 1,6094 ; (iii) `aire =` sans valeur initiale ; (iv) code Visual Basic à usage de tableur, hors compétence d'examen (voir bornes).

---
#### EXERCICES ET PROBLÈMES (pp.129-135) — énoncés verbatim, corrigés : aucun dans le manuel

**1- Cocher la ou les bonne(s) réponse(s) :** (p.129, tableau QUESTIONS / REPONSES)
- a) $\int_3^6 x^2 dx$ = ☐189 ☐27 ☐63
- b) $\int_{-1}^1 e^{-x}dx$ = ☐ e − 1/e ☐ 1/e − e ☐ 0
- c) $\int_1^e \ln x\,dx$ est un nombre ☐ Positif ☐ Négatif ☐ Nul
- d) $\int_0^{-1} x^2 dx$ [R7 : bornes relues à 300 dpi — 0 en BAS, −1 en HAUT ; la fiche portait $\int_{-1}^0$, ce qui inverse le signe attendu] est un nombre ☐ Positif ☐ Négatif ☐ Nul
- e) Si $\int_{-1}^2 f(t)dt = −3$ et si $\int_4^2 f(t)dt = 5$ [bornes imprimées : 4 en bas, 2 en haut, vérifié à l'image] alors $\int_{-1}^4 f(t)dt$ vaut : ☐ 2 ☐ − 8 ☐ 8
- f) Si $\int_0^2 f(t)dt = −1$ et si $\int_0^2 g(t)dt = 3$ alors $\int_0^2 (2f(t) − 3g(t))dt$ vaut : ☐ − 11 ☐ 7 ☐ − 7
- g) Soit f la fonction définie sur [1, 2] par f(x) = 1/x. La valeur moyenne de f sur [1, 2] est ☐ −1/2 ☐ − ln(1/2) ☐ ln 2
- h) Si pour tout t ∈ [−1, 2] on a 0,1 ≤ f(t) ≤ 1 et I = $\int_{-1}^2 f(t)dt$ Alors : ☐ 0,1 ≤ I ≤ 1 ☐ − 0,1 ≤ I ≤ 2 ☐ 0,3 ≤ I ≤ 3

**2-** f définie sur IR par f(x) = −(x + 1)e^{−x}. a- Calculer f '(x). b- En déduire la valeur de l'intégrale I = $\int_0^1 xe^{−x}dx$.
**3-** f définie sur ]0,+∞[ par f(x) = (1 + ln x)². a- Calculer f '(x). b- En déduire la valeur de l'intégrale I = $\int_1^e \frac{1 + \ln x}{x}dx$.
**4-** f définie sur IR par f(x) = e^x/(1 + e^x). a- Montrer que la fonction F : x ↦ ln(1 + e^x) est une primitive de f sur IR. b- En déduire la valeur de l'intégrale I = $\int_0^e f(x)dx$ [borne supérieure imprimée « e »].

**5- Calculer les intégrales suivantes :** (p.130, lu à 200 dpi)
a) $\int_0^2 (t+1)dt$ ; b) $\int_{-1}^1 (3x^2 − x)dx$ ; c) $\int_{-1}^1 (4x(x^2 − 1))dx$ ;
d) $\int_{-1}^1 e^x dx$ ; e) $\int_1^2 (t + 1/t)dt$ ; f) $\int_e^1 \frac{t+1}{t}dt$ [bornes imprimées : e en bas, 1 en haut] ;
g) $\int_{-1}^1 (\frac{x^2}{2} − \frac{2}{x^2})dx$ ; h) $\int_0^1 \frac{2}{\sqrt{4t+1}}dt$ ; i) $\int_0^1 2xe^{x^2}dx$ ;
j) $\int_e^1 \frac{\ln t}{t}dt$ [e en bas, 1 en haut] ; k) $\int_1^e \frac{3}{x}(\ln x)^2dx$ ; l) $\int_2^1 \frac{1}{x^2}e^{1/x}dx$ [2 en bas, 1 en haut].

**6-** a- Calculer $\int_{-1}^4 \frac{1}{x+2}dx$. b- Montrer que pour tout x de ]−2,+∞[ on a x/(x+2) = 1 − 2/(x+2). c- En déduire la valeur de I = $\int_{-1}^2 \frac{x}{x+2}dx$.
**7-** a- Montrer que pour tout x de ]−2,2[ on a 4/(4−x²) = 1/(2−x) + 1/(2+x). b- En déduire la valeur de I = $\int_{-1}^1 \frac{4}{4−x^2}dx$.
**8-** f définie sur ]0,+∞[ par f(x) = (x²+3x+1)/(x²+x). a- Montrer que pour tout x de ]0,+∞[ on a f(x) = 1 + 1/x + 1/(x+1). b- En déduire la valeur de I = $\int_1^2 f(x)dx$.
**9-** f définie sur IR \ {2} par f(x) = (x²−2x+5)/(x−2). a- Déterminer les réels a, b et c tels que pour tout x de IR \ {2} on a : f(x) = ax + b + c/(x−2). b- En déduire l'intégrale $\int_0^1 f(x)dx$.
**10-** a- Montrer que pour tout réel x on a e^{2x}/(1+e^x) = e^x − e^x/(1+e^x). b- En déduire la valeur de I = $\int_0^{\ln 2}\frac{e^{2x}}{1+e^x}dx$ et de J = $\int_0^{\ln 2}\frac{e^x}{e^{−x}+1}dx$.
**11-** f définie sur IR par f(x) = (x²+2x−3)e^x. a- Déterminer les réels a, b et c tels que la fonction F définie sur IR par F(x) = (ax²+bx+c)e^x soit une primitive de f sur IR. b- En déduire la valeur de l'intégrale I = $\int_0^1 f(x)dx$.
**12-** a- A l'aide d'un[e] intégration par parties, calculer les intégrales suivantes : I = $\int_0^1 (2x−1)e^{3x}dx$ ; J = $\int_1^e (1−x)\ln x\,dx$. b- En déduire les valeurs des intégrales K = $\int_0^1 (x^2−x)e^{3x}dx$ ; L = $\int_1^e (2x−x^2)\ln x\,dx$. c- Soit n un entier naturel non nul, on pose I_n = $\int_0^1 x^n e^x dt$ [sic : « dt » imprimé, dx attendu]. Montrer que pour tout entier naturel non nul n on a I_{n+1} = e − (n+1)I_n.
**13-** Situation : « Le débit en m³ × h⁻¹ d'une pompe à arrosage qui fonctionne en été de 6 heures à 20 heures, est modélisé par f(x) = 5e^{0,002x} où x est l'heure considérée (6 ≤ x ≤ 20). » a- Vérifier que la fonction F définie sur IR par F(x) = 2500e^{0,002x} est une primitive de la fonction f sur IR. b- Le volume V d'eau débité par cette pompe entre 6 et 20 heures est égal à : $\int_6^{20} f(x)dx$. Vérifier que V est environ 71,85 m³. c- Montrer que le débit moyen de cette pompe entre 6 et 20 heures est environ 5,13m³.h⁻¹ [« 5,13m3 » p.131 puis « m³.h⁻¹ »]. (Vérifié par calcul : V = 2500(e^{0,04} − e^{0,012}) ≈ 71,85 ; 71,85/14 ≈ 5,13.)
**14- (Valeur moyenne du coût marginal)** Situation : une entreprise fabrique des objets dont le nombre x ∈ [0 ; 3,5] est exprimé en milliers. Le coût de fabrication C(x) est exprimé en milliers de dinars et le coût marginal C_m(x) = C'(x) est modélisé par C_m(x) = 1 + ((x − 3)/8)e^x ; x ∈ [0 ; 3,5].
 1- a- Dresser le tableau de variation de la fonction C_m. b- En déduire que C_m(x) ≥ 0 pour tout x de [0 ; 3,5].
 2- Soit u la fonction définie sur [0 ; 3,5] par u(x) = ((x − 4)/8)e^x. a- Calculer u'(x) pour x de [0 ; 3,5]. b- En déduire la primitive de C_m qui s'annule en 0.
 3- Calculer la valeur moyenne $\bar{C_m}$ de C_m sur [0 ; 3,5].

**15-** « Soient f une fonction définie sur [a,b] et C sa courbe représentative dans un repère orthonormé (O, i, j). Dans chacun des cas suivants, calculer l'aire de la région du plan limitée par la courbe C, l'axe des abscisses et les droites d'équations x = a et x = b : » (p.132)
a) f(x) = x² + x + 1, a = 0 et b = 1 ; b) f(x) = 2/x, a = 2 et b = 3 ; c) f(x) = e^{1−x}, a = −2 et b = 2 ; d) f(x) = (2/(x+1))·ln(x+1), a = 0 et b = 1.
**16-** f définie sur ]0,+∞[ par f(x) = x + 1/x, C sa courbe dans un repère orthonormé (O, i, j) du plan (l'unité graphique : 3cm). a- Démontrer que la droite D : y = x est asymptote à C en +∞. b- Vérifier que pour tout x de ]0,+∞[, on a f '(x) = (x²−1)/x² et dresser le tableau de variation de la fonction f. c- Tracer la courbe représentative de f et la droite D. d- Calculer l'aire (en cm²) du domaine compris entre la courbe C, la droite D et les droites d'équations x = 1 et x = 3.
**17-** f définie sur IR par : f(x) = (1/2)x²e^{−x}. C sa courbe dans un repère orthonormé (O, i, j) (l'unité étant 2cm). 1- Déterminer les limites de f en −∞ et +∞. 2- Dresser le tableau de variations de f. 3- Construire la courbe C. a- Soit α ∈ ]0,+∞[, montrer que l'aire A(α) de la région du plan limitée par la courbe de f, l'axe des abscisses et les droites d'équations x = 0 et x = α est égale à 4(1 − e^{−α}(1 + α + α²/2)) cm². (On utilisera deux intégrations par parties successives). b- Calculer $\lim_{α→+∞}A(α)$.
 [Note : 3 est suivi de a-, b- sans numéro ; imprimé tel quel. Vérifié : avec unité 2 cm, 1 u.a. = 4 cm² ; $\int_0^α \frac12 x^2e^{-x}dx = 1 − e^{−α}(1+α+α²/2)$, cohérent avec le facteur 4.]
**18-** f définie sur [0,6] par f(x) = (1/36)(6x − x²). 1- a- Dresser le tableau de variations de f. b- Tracer la courbe représentative de f dans un repère orthonormé (O, i, j) du plan. c- Calculer $\int_0^6 f(x)dx$. Interpréter graphiquement cette intégrale. d- Soient a et b deux réels de [0,6] tels que a ≤ b. Montrer que $0 ≤ \int_a^b f(x)dx ≤ 1$ (p.133). 2- Situation : « Une entreprise fabrique un produit et vend chaque semaine x milliers d'unités tel que 0 ≤ x ≤ 6. Soient a et b deux réels de [0,6] tels que a ≤ b. On estime que la probabilité de vendre entre a et b milliers d'unités pour une semaine choisie au hasard est $\int_a^b f(x)dx$. Déterminer la probabilité de vendre : a- Moins de 2000 unités ; b- Entre 2000 et 4000 unités ; c- Plus de 4000 unités. » (Vérifié : $\int_0^6 f = 1$.)
**19-** (pp.133-134) f et g définies sur [1,+∞[ par f(x) = 1,1x + ln x − ln(x+1) et g(x) = 1,1x + 1/x. C_f et C_g leurs courbes dans un repère orthonormé (O, i, j) (l'unité graphique est 2cm).
 A- 1- a- Calculer $\lim_{x→+∞}\ln(\frac{x}{x+1})$. En déduire $\lim_{x→+∞}f(x)$. b- Dresser le tableau de variation de f. 2- a- Montrer que la droite D d'équation y = 1,1x est une asymptote à C_f. b- Etudier la position relative de C_f par rapport à D. 3- Tracer C_f et D.
 B- 1- Dresser le tableau de variation de g. 2- Vérifier que la droite D est asymptote à C_g et préciser la position relative de C_g par rapport à la droite D. 3- Tracer C_g dans le même repère (O, i, j). 4- On pose pour tout x de [1,+∞[, H(x) = (x+1)ln(x+1) − x ln x. a- Calculer H'(x) pour x ∈ [1,+∞[. b- En déduire une primitive sur [1,+∞[ de la fonction h : x ↦ g(x) − f(x). c- Calculer l'intégrale $\int_1^5 (g(x) − f(x))dx$. En donner une interprétation graphique.
 C- « Les fonctions f et g modélisent respectivement la quantité d'objets produits par une entreprise et la quantité d'objets commandés à cette entreprise. Plus précisément, si t est la date exprimée en semaines, f(t) est la quantité en milliers d'objets produits à la date t et g(t) est la quantité d'objets commandés à cette même date en milliers. » 1- Lorsque f(t) ≥ g(t), on dit que « la demande est satisfaite à la date t ». Démontrer que la demande n'est jamais satisfaite. 2- On admet que le nombre total d'objets en milliers dont la demande n'est pas satisfaite entre les dates n et n', avec n' > n est donné par : $\int_n^{n'}(g(t) − f(t))dt$. Donner à un objet près, le nombre total d'objets dont la demande n'est pas satisfaite entre les dates 1 et 5. 3- On considère que « le niveau de fabrication est suffisant » lorsque moins de 20 demandes ne sont pas satisfaites c'est-à-dire lorsque l'on a : g(t) − f(t) ≤ 0,02. En admettant que (g − f) est une fonction strictement décroissante sur [1,+∞[, à partir de quelle date le niveau de fabrication est-il suffisant ?
**20-** (p.134) 1) g définie sur ]0,+∞[ par : g(x) = −x² − 4 + ln x. Dresser le tableau de variations de g et en déduire le signe de g(x) pour tout x > 0. 2) f définie sur ]0 ; +∞[ par : f(x) = −x + 2 − (4 ln x)/x. Le plan est rapporté à un repère orthogonal (O, i, j) (unités graphiques : 2 cm sur l'axe des abscisses et 1 cm sur l'axe des ordonnées). Soit C la courbe représentative de f. a) Etudier le sens de variation de f. b) Etudier la limite de f en 0 et interpréter graphiquement le résultat obtenu. c) Calculer la limite de f en +∞. d) Démontrer que la droite D d'équation y = -x + 2 est asymptote à C en +∞. e) Etudier la position relative de D et C. f) Dresser le tableau de variation de f. g) Déterminer les points de C en lesquels la tangente est parallèle à D. h) Représenter C et D. 3) h définie sur ]0,+∞[ par : h(x) = –x + 2 – 4/x. On appelle H sa courbe représentative dans le repère (O, i, j). a) Etudier les variations de h. b) Démontrer que la droite D est asymptote à H. Déterminer l'autre asymptote à H. c) Etudier les intersections de C et H, et étudier la position relative des deux courbes. 4) Calculer $\int_a^b (f(x) − h(x))dx$. Interpréter graphiquement le résultat. [a et b non définis dans l'énoncé imprimé]
**21-** (pp.134-135) A- Le plan est rapporté à un repère orthonormé (O, i, j) (unité graphique : 5 cm). Les points C et A ont respectivement pour coordonnées (1 ; 1) et (1 ; 0), et D est la droite d'équation y = x. 1- Soit g la fonction définie sur [0 ; 1] par : g(x) = (e^x − 1)/(e − 1). a) Etudier les variations de g et vérifier que sa courbe représentative C passe par les points O et C. b) Déterminer des équations des tangentes à C en O et C. c) Etudier la position relative de C et D. d) Calculer l'aire de la portion du plan délimitée par la courbe C, la droite D et les droites d'équations x = 0 et x = 1. 2- « Dans cette question, on se propose de généraliser les résultats obtenus à la première question et d'en donner une interprétation économique. On considère une fonction F définie et continue sur [0 ; 1] satisfaisant aux conditions (C) suivantes : F est croissante, F(0) = 0 et F(1) = 1. »
 B- « Une fonction F satisfaisant aux conditions (C) décrit la distribution de la masse salariale d'une entreprise entre ses salariés, que l'on classe par salaires croissants : F(x) représente le pourcentage des salaires perçus par le pourcentage x de salariés (par exemple, si 50% des salariés perçoivent 30% de la masse salariale, alors F(0,5) = 0,3). La courbe C correspondante est appelée **courbe de Lorentz** [le point manque dans le texte imprimé : « Lorentz Le coefficient »] Le coefficient γ égal au rapport de l'aire coloriée sur le dessin à l'aire du triangle OAC, appelé **indicateur de Gini**, est alors un indicateur d'inégalité de répartition salariale. » Figure : carré OACB (O origine, A=(1;0) à droite, C=(1;1), B=(0;1)), courbe convexe de O à C, région bleue entre la diagonale OC et la courbe.
 a) Vérifier que la fonction g étudiée à la première question satisfait aussi aux conditions (C) et donner la valeur γ_i [sic « γi »] de γ correspondante. b) Mêmes questions pour les fonctions h et k définies sur [0 ; 1] par : h(x) = x² et k(x) = (x³ + x)/2. Les fonctions g, h et k représentent trois entreprises G, K et L [sic : h n'est pas nommée ; K et L pour h et k ?]. Classer ces trois entreprises de la plus égalitaire au moins égalitaire.

---
#### MATH CULTURE (p.136) — « PID ou proportionnel, intégral, dérivée »
Texte intégral : « Pâte à papier, pâtisserie ou pétrole, en usine le problème est le même : éviter à tout prix que la cuve ne déborde et garde le tout à la bonne température lors de la fabrication. Il faut donc jouer du thermostat et de la vanne pour réguler l'ensemble. L'une des méthodes les plus courantes de régulation des processus de fabrication industriels est le contrôle PID. Le principe est simple : Si le niveau d'une cuve est N₀ et que le niveau mesuré à l'instant t est n(t), la commande à envoyer à la vanne pour qu'elle fasse elle-même les régulations nécessaires est représentée par la somme de trois termes. Le premier est proportionnel à l'écart N(t)–N₀, le deuxième à la dérivée de ce même écart et le troisième est sa primitive. Ces deux derniers termes jouent un rôle primordial. La dérivée permet de contrebalancer les variations brutales liées au premier écart, l'intégrale entre deux instants aide à supprimer les éventuelles oscillations de niveau autour de la valeur fixée N₀. D'où le nom de régulation par « contrôle PID », qui signifie tout simplement Proportionnel, Intégral, Dérivée. »
Source citée : aucune. Coquille : « n(t) » puis « N(t) » pour le même niveau mesuré.

---
#### VOCABULAIRE OFFICIEL de la section
intégrale de f entre a et b ; primitive ; bornes ; « [F(t)] pris entre a et b » ; intégrale de f sur [a, b] ; relation de Chasles ; inversion des bornes ; linéarité de l'intégrale ; positivité et comparaison d'intégrales ; intégration par parties ; valeur moyenne de f sur [a , b] (notation $\bar f$) ; coût marginal / coût moyen ; unité d'aire (u.a.) ; aire du domaine compris entre la courbe, l'axe des abscisses et les droites x = a, x = b ; position relative de deux courbes ; courbe de Lorentz ; indicateur de Gini ; quantité / prix d'équilibre ; courbes d'offre et de demande ; contrôle PID.

#### BORNES — INCLUS / EXCLU (déduit du contenu imprimé ; le manuel ne donne pas de liste de bornes)
INCLUS : définition de l'intégrale par une primitive (f continue) ; notation [F]_a^b ; Chasles, ∫_a^a = 0, inversion des bornes ; linéarité ; positivité et comparaison ; encadrement par majoration/minoration de f ; IPP (u', v' continues), y compris deux IPP successives ; valeur moyenne ; aire sous la courbe (∫|f|), aire entre deux courbes (∫|f−g|), unité d'aire ; intégrales avec ln, e^x, puissances, (u'/u), u'·e^u, u'/√u ; applications économiques (coût marginal → coût total, prix moyen d'offre, débit/volume, probabilité par intégrale d'une densité sur [0 ; 6], Lorentz/Gini) ; aire cm² avec unité graphique donnée ; limite de A(λ) quand λ→+∞ (aire d'un domaine non borné).
EXCLU (non traité dans le chapitre) : somme de Riemann / définition par limite de sommes ; intégrales généralisées en tant que théorie ; équations différentielles ; changement de variable (hors u'·f(u) reconnu directement) ; volumes de révolution. Le code Visual Basic de « Avec l'ordinateur » est un TP, pas un contenu d'examen (non évalué dans les exercices).

#### NOTIONS-CLÉS (≤ 8)
1. Intégrale = F(b) − F(a), indépendante de la primitive. 2. Chasles, inversion, ∫_a^a = 0. 3. Linéarité. 4. Positivité/comparaison → encadrements. 5. Intégration par parties ∫u'v = [uv] − ∫uv'. 6. Valeur moyenne $\frac{1}{b-a}\int_a^b f$. 7. Aire = ∫|f| (u.a.) ; aire entre courbes = ∫|f−g|. 8. Modélisation économique (coût marginal, prix moyen, débit, probabilité, Lorentz-Gini).

---
#### § NOTES
**Pages lues** : 22/22 (115 à 136), texte `pdftotext` + image 110 dpi pour chacune. **Sondées plus fort (170-220 dpi)** : p.128 (capture tableur, 220 dpi), p.130 (exercice 5, 200 dpi). Texte pdf peu fiable pour les bornes d'intégrales : tout est tranché à l'image (ex. ex.1 d : ∫_0^{-1} [R7 : corrigé, la fiche indiquait ∫_{-1}^0 ; à 300 dpi la borne inférieure est 0 et la supérieure −1] ; ex.1 e : ∫_4^2).
**Coquilles imprimées (reproduites/signalées)** : p.116 Act.1 étiquettes a), c), c), d) (b manquant) et « s'annule en1 » ; p.123 Act.4 « p_0 » pour p_e et légende des courbes inversée (« demandée » sur la courbe croissante p_O) ; p.124 Act.3 « largeur h » (h = hauteur) ; p.128 A1 de la capture « 4/(1+x²) » ≠ code `x/(x²+1)` et valeurs ; `aire =` sans valeur dans le code ; p.128 « Intégrale de f » = −0,016 (somme de Riemann, valeur exacte 0) ; p.129 ex.4 b borne supérieure « e » ; p.130 ex.5 f, j, l bornes inversées (e en bas/1 en haut ; 2 en bas/1 en haut), ex.5 g : 2/x² non définie en 0 sur [−1 ; 1] (intégrale impropre, énoncé incorrect tel qu'imprimé) ; p.122 Act.2 : intégrales avec bornes 2 en bas et 0 en haut (a et J) ; p.131 ex.12 c « dt » au lieu de « dx » ; ex.12 a « d'un intégration » ; p.134 ex.20 4) a et b non définis ; p.135 « courbe de Lorentz » sans point, « γi », entreprises « G, K et L » pour g, h, k ; p.136 n(t) / N(t).
**Incohérences chiffrées vérifiées par recalcul** : p.126 Act.7 identité f−g OK ; ex.13 V ≈ 71,85 et débit moyen ≈ 5,13 OK ; ex.17 facteur 4 OK ; p.124 Act.3 et p.126 Act.6 a) cohérents avec les figures ; p.116 Act.3 : droite lue à l'image f(x) = x/2 + 3 (non écrite dans le texte). Aucun total de tableau à recompter dans cette tranche (seul tableau chiffré : capture p.128).
**Corrigés** : aucun dans le manuel (ni activités ni exercices) ; rien n'a été inventé. Seules vérifications de cohérence mentionnées ci-dessus, balisées comme calculs de lecteur.
**`[?]`** : aucun. [R7 : l'ancien [?] (valeur initiale de `aire`, p.127) est levé à 250 dpi : la valeur est absente de l'impression, pas illisible — coquille du manuel.]
**Structure** : « Avec l'ordinateur » = pp.127-128 ; « Exercices et problèmes » = pp.129-135 (exercices 1 à 21) ; « Math culture » = p.136. Le cours : I (pp.117-121), II (pp.121-122), III (pp.122-123), IV (pp.123-126). Pas d'exemple résolu dans le chapitre.

---

### Chapitre `m06-p137-164`

### m06 — Manuel Mathématiques 4e année secondaire, éco-gestion — Chapitre VI « Suites réelles » (pages PDF 137-164)

Source : `222463P00.pdf`, CNP. Notation : IN = ℕ, IR = ℝ ; $u_n$ = terme général. Les graphiques de points sont lus à l'image (valeurs de lecture, signalées « lu »).

Sommaire du chapitre (p.137, titre « Chapitre 6 — SUITES REELLES ») : Pour commencer · Cours : Revoir ; Suites minorées, suites majorées ; Variation d'une suite ; Opérations sur les suites ; Suites convergentes - suites divergentes ; Opérations sur les limites des suites ; Limites et ordre ; Exemples de suites récurrentes · Avec l'ordinateur · Exercices et problèmes · Math culture.

---
#### POUR COMMENCER (p.138-139)

##### Activité 1 (p.138) — QCM « Cocher la ou les réponse(s) correcte(s). » (aucune situation d'entreprise ; pas de corrigé donné)
1) Soit u la suite définie sur IN par : $u_n = 3 - 2n$. $u_2$ est égal à : [-1] [1]
2) Soit u la suite définie par $u_n = \frac{2n+5}{n^2-2n}$ : [$u_0$ n'existe pas] [$u_1 = 7$] [$u_1 = -7$]
3) u étant une suite arithmétique de raison r et de premier terme $u_0$. Le terme général de la suite u est : [$u_n = u_{n-1} + r$] [$u_n = u_0 + nr$] [$u_n = nu_0 + r$]
4) Soit u la suite définie sur IN par : $u_0 = 1$ et $u_{n+1} = u_n + 2$. $u_{20}$ est égal à : [7,5] [21] [41]
5) La suite définie sur IN par : $u_n = \frac{n+30}{4}$ est une suite arithmétique de raison : [7,5] [$\frac{1}{4}$] [$\frac{n}{4}$]
6) u étant une suite géométrique de raison q et de premier terme $u_0$, le terme général de la suite u est : [$u_n = q^n u_0$] [$u_n = q^{n+1} u_0$] [$u_n = q\,u_{n-1}$]
7) La suite définie sur IN par : $u_n = 2\times\left(\frac{1}{3}\right)^n$ est une suite géométrique de raison : [n] [$\frac{1}{3}$] [2]

##### Activité 2 (p.138-139) — lecture graphique
Énoncé : « Dans chacun des cas suivants, on représente graphiquement les premiers termes d'une suite $(u_n)_{n\in\mathbb N}$ arithmétique ou géométrique. 1- Indiquer la nature de la suite et sa raison. 2- Donner une expression de $u_n$ en fonction de n. 3- Déterminer éventuellement la limite de la suite $(u_n)_{n\in\mathbb N}$. »
Quatre nuages de points (repères cartésiens quadrillés, abscisses n = 0..4), points lus à l'image :
- Graphique 1 (p.138 gauche) : (0 ; 2), (1 ; 1), (2 ; 0,5), (3 ; 0,25), (4 ; ≈0,125) (lu) — ordonnée axes graduées 1 et 2.
- Graphique 2 (p.138 droite) : (0 ; 5), (1 ; 3,5), (2 ; 2), (3 ; 0,5), (4 ; -1) (lu) — graduations 1..5.
- Graphique 3 (p.139 gauche) : (0 ; 5), (1 ; -4), (2 ; ≈3,2), (3 ; ≈-2,5), (4 ; 2) (lu) — graduations -4..5.
- Graphique 4 (p.139 droite) : (0 ; -3), (1 ; -1), (2 ; 1), (3 ; 3), (4 ; 5) (lu).
Aucun corrigé dans le manuel (lecture : 1 géom. q=1/2, 2 arith. r=-1,5, 4 arith. r=2 ; le 3 est compatible avec géom. q=-0,8 d'après les points lus — NON affirmé par le manuel).

##### Activité 3 (p.139)
1) $(u_n)_{n\in\mathbb N}$ est une suite arithmétique de raison 3 et de premier terme $u_0 = 4$. a) Calculer $u_1$, $u_2$ et $u_3$. b) Exprimer $u_n$ en fonction de n pour tout entier naturel n. c) Soit $n\in IN^*$, exprimer la somme $S_n = u_0 + u_1 + ... + u_{n-1}$ en fonction de n.
2) $(v_n)_{n\in\mathbb N}$ est une suite géométrique de raison 2 et de premier terme $v_0 = -3$. a) Calculer $v_1$, $v_2$ et $v_3$. b) Exprimer $v_n$ en fonction de n pour tout entier naturel n. c) Soit $n\in IN^*$, exprimer la somme $S_n = u_0 + u_1 + ... + u_{n-1}$ en fonction de n. [coquille imprimée : en 2c la somme est écrite avec u au lieu de v]

##### Activité 4 (p.139)
1- Démontrer par récurrence chacune des propriétés suivantes : a) Pour tout entier naturel n, $1+2+3+...+n = \frac{n(n+1)}{2}$. b) Pour tout entier naturel n, $1^2+2^2+3^2+...+n^2 = \frac{n(n+1)(2n+1)}{6}$.
2- On considère la suite $(u_n)_{n\in\mathbb N}$ définie par $u_0 = 0$ et pour tout entier naturel n, $u_{n+1} = \frac{3}{u_n - 1}$. Montrer que pour tout entier naturel n, $u_n \le 0$.

---
#### COURS

##### 1) Revoir (p.140-141)

**Activité 1 (p.140)** Soit u la suite définie sur IN par $u_0 = -1$ et $u_{n+1} = 2 + u_n$. 1) Vérifier que la suite u est arithmétique et déterminer sa raison. 2) Exprimer $u_n$ en fonction de n. 3) Déterminer $\lim_{n\to+\infty} u_n$. 4) Soit $n\in IN^*$, exprimer la somme $S_n = u_0+u_1+...+u_{n-1}$ en fonction de n.

Encadré (vert, résultat, p.140) — verbatim : « Soit u une suite arithmétique de premier terme $u_0$ et de raison r non nul – Si $r>0$ alors $\lim_{n\to+\infty}u_n = +\infty$ – Si $r<0$ alors $\lim_{n\to+\infty}u_n = -\infty$ ».

**Activité 2 (p.140)** Situation : un marteau frappe une pièce métallique. « Un marteau frappe toutes les 5 secondes une pièce métallique dont l'épaisseur initiale est 1cm. A chaque coup, l'épaisseur du métal diminue de 1%. Soit $u_n$ l'épaisseur en cm de la pièce après n coups. » 1- Calculer $u_1$, $u_2$ et $u_3$. 2- Montrer par récurrence que pour tout entier naturel n on a $u_n = (0,99)^n$. 3- En déduire que $(u_n)$ est une suite géométrique dont on précisera la raison q. 4- Déterminer le nombre de coups minimal pour que l'épaisseur de la pièce soit inférieur à 5mm. 5- Calculer $\lim_{n\to+\infty}u_n$.

**Activité 3 (p.140)** Calculer la limite, lorsqu'elle existe, de chacune des suites $(u_n)_{n\in IN}$, $(v_n)_{n\in IN}$ et $(w_n)_{n\in IN}$ : a) $u_n = (1-\sqrt3)^n$. b) $v_n = (-2)^{n+1}$. c) $w_0 = 1$ et pour tout entier naturel n, $3w_{n+1} - 4w_n = 0$.

Encadré (vert, résultat, p.140) — verbatim : « Soit $(u_n)$ une suite géométrique de premier terme $u_0 \ne 0$ et de raison $q \ne 1$ – Si $q \le -1$ alors la suite $(u_n)$ n'admet pas de limite. – Si $-1<q<1$ alors $\lim_{n\to+\infty}u_n = 0$. – Si $q>1$ alors la limite de la suite $(u_n)$ est $+\infty$ ou $-\infty$, selon que $u_0$ est strictement positif ou strictement négatif. »

**Activité 4 (p.140)** Soit u la suite définie sur IN par $u_0 = -2$ et $u_n = \frac{3}{2}u_{n+1}$. 1) Calculer $u_1$, $u_2$ et $u_3$. 2) Dans le plan muni d'un repère cartésien $(O,\vec i,\vec j)$, représenter les points $A_n(n,u_n)$ pour $n\in\{0,1,2,3\}$. 3) Exprimer $u_n$ en fonction de n, puis déterminer $\lim_{n\to+\infty}u_n$. 4) Soit $n\in IN^*$, exprimer la somme $S_n = u_0+u_1+...+u_{n-1}$ en fonction de n.

**Activité 5 (p.141)** Dans chacun des cas suivants, préciser la nature puis déterminer la limite de la suite $(u_n)$ : a) $u_n = \frac{2-n}{3}$ ; b) $u_n = \frac{n(1-3n)}{3} + n^2$ ; c) $u_n = \frac{1}{2}\left(\frac{1}{5}\right)^n$ ; d) $u_n = \frac{2^{n+1}}{3^n}$.

##### 2) Suites minorées, suites majorées (p.141-142)

**Activité 1 (p.141)** 1- On considère la suite $(u_n)_{n\in IN}$ définie par $u_0 = -1$ et pour tout $n\in IN$, $u_{n+1} = \frac{1}{3}u_n + 2$. Montrer par récurrence que pour tout entier naturel n, $u_n \le 3$. 2- Soit $(v_n)_{n\in IN}$ la suite définie par $v_n = e^n + 2n + 3$. Montrer que pour tout entier naturel n, $v_n \ge 4$.

**Activité 2 (p.141)** Soit la suite définie par : $u_n = \left(-\frac{1}{2}\right)^n + \frac{1}{n^2+1}$. a) Montrer que pour tout entier naturel n on a : $-\frac12 \le \left(-\frac12\right)^n \le \frac12$ et que $0 \le \frac{1}{n^2+1} \le 1$. b) En déduire que pour tout entier naturel n $-\frac12 \le u_n \le \frac32$.

**Définitions (encadré bleu, p.141) — verbatim** : « Soient $n_0$ un entier naturel et $(u_n)_{n\ge n_0}$ une suite réelle • $(u_n)_{n\ge n_0}$ est dite majorée s'il existe un réel M tel que pour tout entier naturel $n\ge n_0$, $u_n \le M$. • $(u_n)_{n\ge n_0}$ est dite minorée s'il existe un réel m tel que pour tout entier naturel $n\ge n_0$, $m\le u_n$. • $(u_n)_{n\ge n_0}$ est dite bornée si elle est à la fois minorée et majorée. »

**Vocabulaire (p.141) — verbatim** : « M et m désignent deux réels donnés. La suite $(u_n)_{n\ge n_0}$ est dite majorée par M (respectivement minorée par m), si pour tout entier naturel $n\ge n_0$, $u_n \le M$ (respectivement $u_n \ge m$). »

**Activité 3 (p.142)** On considère la suite $(s_n)_{n\in\mathbb N}$ définie par $s_n = \left(1+\frac12+\frac14+\frac18+...\frac{1}{2^n}\right) - n$. a) Montrer que pour tout entier naturel n, $s_n = 2 - n - \left(\frac12\right)^n$. b) Calculer $s_0$, $s_1$ et $s_2$ puis prouver que la suite $(s_n)_{n\in\mathbb N}$ est majorée par 2.

**Activité 4 (p.142)** Soit u la suite définie sur IN par $u_n = \sqrt{3+e^n}$. Montrer que la suite u est minorée par 2.

**Activité 5 (p.142)** On considère les suites u, v et w définies sur IN par leurs termes généraux suivants : $u_n = 1+3e^{-n}$, $v_n = \frac{n+1}{n!}$ et $w_n = \frac{\cos(n)}{n^2+1}+1$. Prouver que les suites u, v et w sont bornées.

##### 3) Variation d'une suite (p.142-143)

**Activité 1 (p.142)** 1- Soit $(u_n)_{n\in\mathbb N}$ la suite définie par $u_0 = 4$ et pour tout $n\in IN$ $u_n = 2(u_{n+1}-1)$. a) Calculer $u_1$ et $u_2$. b) Montrer que pour tout entier naturel n, $u_n \ge 2$. c) En déduire que pour tout entier naturel n, $u_{n+1} \le u_n$. 2- Soit $(v_n)_{n\in\mathbb N}$ la suite définie par $v_n = 1+e^n$. Prouver que pour tout entier naturel n, $v_{n+1} \ge v_n$.

**Définitions (encadré bleu, p.142) — verbatim** : « Soient $n_0$ un entier naturel et $(u_n)_{n\ge n_0}$ une suite réelle. • $(u_n)$ est dite croissante (respectivement strictement croissante) si pour tout entier naturel $n\ge n_0$, $u_{n+1}\ge u_n$ (respectivement $u_{n+1}>u_n$). • $(u_n)$ est dite décroissante (respectivement strictement décroissante) si pour tout entier naturel $n\ge n_0$, $u_{n+1}\le u_n$ (respectivement $u_{n+1}<u_n$). • $(u_n)$ est dite constante si pour tout entier naturel $n\ge n_0$, $u_{n+1}=u_n$. • $(u_n)$ est dite monotone si elle est soit croissante, soit décroissante. »

**Activité 2 (p.143)** Soit $(u_n)_{n\in\mathbb N}$ la suite définie par : $u_0 = \alpha$ ; $\alpha\in IR$ et $3u_{n+1} = 2u_n - 6$ pour tout $n\in IN$. 1- Exprimer $u_{n+1}$ en fonction de $u_n$. 2- Montrer que si $\alpha=-6$ alors la suite $(u_n)$ est constante. 3- On suppose que $\alpha=1$. a) Montrer par récurrence que pour tout entier naturel n, $u_n \ge -6$. b) Montrer que la suite $(u_n)$ est décroissante. 4- On suppose que $\alpha=-8$. a) Montrer que pour tout entier naturel n, $u_n\le -6$. b) Montrer que la suite $(u_n)$ est croissante.

**Activité 3 (p.143)** 1- Soit $(u_n)_{n\in\mathbb N}$ la suite définie par $u_n = (\frac14)^n - 2$. a) Montrer que la suite $(u_n)$ est minorée par 2. b) Montrer que la suite $(u_n)$ est décroissante. 2- Soit $(v_n)_{n\in\mathbb N}$ la suite définie par $v_0 = 2$ et pour tout $n\in IN$, $v_{n+1} = 2v_n - 1$. a) Montrer que la suite $(v_n)$ est minorée par 1. b) Montrer que la suite $(u_n)$ est croissante. [coquilles imprimées : 1a « minorée par 2 » est faux pour $u_n=(1/4)^n-2$ (u_0=-1 ; minorant correct -2) ; 2b écrit $(u_n)$ au lieu de $(v_n)$]

**Activité 4 (p.143)** Soit f la fonction définie sur $]1,+\infty[$ par $f(x) = x - \ln(x-1)$. a) Montrer que f est dérivable sur $]1,+\infty[$ et que $f'(x) = \frac{x-2}{x-1}$. b) En déduire que f est croissante sur $[2,+\infty[$. c) Montrer que la suite $(u_n)_{n\ge2}$ définie par $u_n = f(n)$ est croissante.

**Théorème (admis) (encadré vert, p.143) — verbatim** : « Soient $n_0$ un entier naturel, f une fonction définie sur $[n_0,+\infty[$ et $(u_n)_{n\ge n_0}$ la suite définie par $u_n = f(n)$. • Si f est croissante sur $[n_0,+\infty[$ alors la suite $(u_n)_{n\ge n_0}$ est croissante. • Si f est décroissante sur $[n_0,+\infty[$ alors la suite $(u_n)_{n\ge n_0}$ est décroissante. »

**Activité 5 (p.143)** Etudier la monotonie de chacune des suites suivantes : a) $u_n = n^2+n-1$ ; b) $u_n = \frac{n}{n+2}$ ; c) $u_n = \frac{n+3}{2n+1}$ ; d) $u_n = \ln(n+2) - \ln n$ ; e) $u_n = e^{-2n} - n$.

##### 4) Opérations sur les suites (p.144)

**Définition (encadré bleu, p.144) — verbatim** : « Soit p un entier naturel, u et v deux suites réelles définies pour $n\ge p$. • La somme des deux suites u et v est une suite, notée u+v, de terme général $u_n+v_n$. • Le produit des deux suites u et v est une suite, notée uv, de terme général $u_n\times v_n$. • Le produit de la suite u par un réel λ est une suite, notée λ.u, de terme général : λ.$u_n$. • La valeur absolue de la suite u est une suite, notée |u|, de terme général : $|u_n|$. • Si de plus pour tout entier $n\ge p$, $v_n\ne0$, l'inverse de v et le quotient de u par v sont des suites, notées respectivement $\frac1v$ et $\frac uv$, de termes généraux respectifs $\frac1{v_n}$ et $\frac{u_n}{v_n}$. »

**Activité 1 (p.144)** On considère les suites u et v définies sur $IN^*$ par $u_n = 1+\frac13+\left(\frac13\right)^2+...+\left(\frac13\right)^{n-1}$ et $v_n = \left(\frac13\right)^n+\left(\frac13\right)^{n+1}+...+\left(\frac13\right)^{2n-1}$. Prouver que les termes généraux des suites $h=\frac23u$, $k=u+v$ et $w=\frac ku$ sont respectivement : $h_n = 1-\left(\frac13\right)^n$, $k_n = \frac32\left(1-\left(\frac13\right)^{2n}\right)$ et $w_n = 1+\left(\frac13\right)^n$. (Vérifié par recalcul : cohérent.)

**Activité 2 (p.144)** Soit u une suite géométrique de raison $q\in IR\setminus\{0,1\}$ et de premier terme $u_0\in IR^*$. Montrer que la suite $\frac1u$ est aussi une suite géométrique dont on précisera la raison et le premier terme.

##### 5) Suites convergentes – suites divergentes (p.144-)

**Activité 1 (p.144)** Soient f et g les fonctions définies sur IR par : $f(x)=2x-1$ et $g(x)=-3e^{-x}$. 1) Calculer $\lim_{x\to+\infty}f(x)$ et $\lim_{x\to+\infty}g(x)$. 2) On considère les suites $(u_n)$ et $(v_n)$ définies sur IN par $u_n=f(n)$ et $v_n=g(n)$. a) Montrer que $(u_n)$ est une suite arithmétique puis déterminer sa limite ℓ. b) Montrer que $(v_n)$ est une suite géométrique puis déterminer sa limite ℓ'. 3) Comparer ℓ et ℓ' respectivement à $\lim_{x\to+\infty}f(x)$ et $\lim_{x\to+\infty}g(x)$.

(suite de la rubrique 5, p.145-146)

**Théorème (admis) (encadré vert, p.145) — verbatim** : « Soient $n_0$ un entier naturel, f une fonction définie sur $[n_0,+\infty[$ et $(u_n)_{n\ge n_0}$ la suite définie par $u_n=f(n)$. Si $\lim_{x\to+\infty}f(x)=\ell$ alors $\lim_{n\to+\infty}u_n=\ell$. (ℓ étant fini ou infini). »

**Remarques (p.145)** : • « On admet que : si une suite admet une limite, alors cette limite est **unique**. » • « Si $\lim_{n\to+\infty}u_n=\ell$ (ℓ étant fini ou infini), alors $\lim_{n\to+\infty}u_{n+1}=\lim_{n\to+\infty}u_{2n}=\lim_{n\to+\infty}u_{2n+1}=\ell$. »

**Activité 2 (p.145)** Soit f la fonction définie sur $[0,+\infty[$ par $f(x)=1+\frac{1}{x+1}$. 1- Calculer la limite de f en $+\infty$. 2- On considère la suite u définie sur IN par $u_n=\frac{n+2}{n+1}$. a) Vérifier que pour tout entier naturel n, $u_n=f(n)$. b) Calculer $\lim_{n\to+\infty}u_n$.

**Activité 3 (p.145)** Calculer la limite de $(u_n)$ dans chacun des cas suivants : a) $u_n=\frac1n$ ; b) $u_n=\sqrt n$ ; c) $u_n=\frac{2n-1}{n+3}$ ; d) $u_n=\frac{n^2+2}{n^3-n+1}$ ; e) $u_n=\frac{\ln n}{n^2}$ ; f) $u_n=\ln\left(\frac{n-1}{n+1}\right)$.

**Définition (encadré bleu, p.145) — verbatim** : « Soient $n_0$ un entier naturel et $(u_n)_{n\ge n_0}$ une suite réelle. • $(u_n)_{n\ge n_0}$ est dite **convergente** lorsqu'elle admet une limite finie. • $(u_n)_{n\ge n_0}$ est dite **divergente** lorsque sa limite est infinie ou elle n'admet pas de limite. »

**Activité 4 (p.145)** Dire dans chacun des cas suivants si la suite u est convergente ou divergente. a) $u_n=\left(-\frac23\right)^{2n}$ ; b) $u_n=2-\frac n5$ ; c) $u_n=(-1)^n$ ; d) $u_n=1-2^{-n}$ ; e) $u_n=n\ln(1+\frac1n)$ ; f) $u_n=\left(1+\frac1n\right)^n$.

**Activité 5 (p.145-146)** Soit $u=(u_n)_{n\in\mathbb N}$ la suite définie par $u_0=0$ et $u_{n+1}=\frac14u_n+3$. 1) Montrer que la suite u est croissante. 2) Montrer que la suite u est majorée par 4. 3) Construire dans un repère orthonormé $(O,\vec i,\vec j)$, les droites $D:y=x$ et $D':y=\frac14x+3$. 4) Placer sur l'axe des abscisses les cinq premiers termes de la suite u ; la suite semble-t-elle converger ? Si oui, vers quelle limite ? 5) a) Montrer que la suite v définie sur IN par $v_n=u_n-4$ est une suite géométrique dont on donnera la raison et le premier terme. b) Exprimer $v_n$ en fonction de n. c) en déduire que pour tout entier naturel n, $u_n=4(1-e^{-n\ln4})$. 6) Calculer alors $\lim_{n\to+\infty}u_n$. (Recalcul : $v_0=-4$, $q=\frac14$, $u_n=4-4(\frac14)^n=4(1-e^{-n\ln4})$ : cohérent avec l'énoncé.)

**Théorème (admis) (encadré vert, p.146) — verbatim** : « Toute suite croissante et majorée est convergente. Toute suite décroissante et minorée est convergente. »

**Activité 6 (p.146)** Soient u et v les suites définies sur $IN^*$ par : $u_n=1+\frac1{2!}+\frac1{3!}+...+\frac1{n!}$ et $v_n=u_n+\frac1{n!}$. 1) Montrer que u est croissante et que v est décroissante. 2) Montrer que u est majorée par $v_1$ et que v est minorée par $u_1$. 3) En déduire que les suites u et v sont convergentes.

**Activité 7 (p.146)** On considère la suite $(u_n)$ définie sur $IN^*$ par $u_n=\frac1{n+1}+\frac1{n+2}+...+\frac1{2n}$. 1- Montrer que la suite $(u_n)$ est croissante. 2- a) Soit $n\in IN^*$, vérifier que pour tout $k\in IN^*$, $\frac1{n+k}\le\frac1n$. b) En déduire que pour tout $n\in IN^*$, $u_n\le1$. 3- En déduire que la suite $(u_n)$ est convergente.

##### 6) Opérations sur les limites des suites (p.146-147)

Texte (p.146) : « Comme dans le cas des fonctions, les règles de calcul de la limite de la somme, du produit, de l'inverse et du quotient de deux fonctions s'étendent pour les suites. »

**Théorème (admis) (encadré vert, p.146) — verbatim** : « Soient $(u_n)$ et $(v_n)$ deux suites convergentes de limites respectives ℓ et ℓ' et soit λ un réel. • Les suites $(u+v)$, $(uv)$, $(\lambda+u)$ et $(\lambda u)$ sont convergentes et on a : $\lim_{n\to+\infty}(u_n+v_n)=\ell+\ell'$ et $\lim_{n\to+\infty}(u_nv_n)=\ell.\ell'$. $\lim_{n\to+\infty}(\lambda+u_n)=\lambda+\ell$ et $\lim_{n\to+\infty}(\lambda u_n)=\lambda.\ell$. • Si de plus les termes $v_n$ sont non nuls et si $\ell'\ne0$ alors les suites $\left(\frac1v\right)$ et $\left(\frac uv\right)$ convergent et on a : $\lim_{n\to+\infty}\frac1{v_n}=\frac1{\ell'}$ et $\lim_{n\to+\infty}\frac{u_n}{v_n}=\frac{\ell}{\ell'}$. »

**Activité 1 (p.147)** Déterminer la limite de la suite $(u_n)_{n\in\mathbb N^*}$ dans chacun des cas suivants : a) $u_n=\frac{3n-1}{n^2}+\left(\frac12\right)^n$ ; b) $u_n=\left(-\frac{2n+1}{3n+2}\right)\left(\frac{n+1}{e^n}+3\right)$ ; c) $u_n=\frac{e^{\frac1n}-1}{\ln(1+\frac1n)}$ ; d) $u_n=\frac{1}{2+n\sin(\frac1n)}$.

**Activité 2 (p.147)** Soit $(u_n)$ la suite définie sur $IN^*$ par : $u_n=\frac{5^n+4^n}{3^n-5^n}$. a) Vérifier que pour tout $n\in IN^*$, on a : $u_n=\frac{1+\left(\frac45\right)^n}{\left(\frac35\right)^n-1}$. b) En déduire $\lim_{n\to+\infty}u_n$.

Texte (italique, p.147) : « Les théorèmes suivants donnent les règles de calcul de la limite de la somme, du produit et du quotient de deux suites dont la limite de l'une, au moins, est infinie. »

**Théorèmes (admis) (p.147) — verbatim** : « ℓ étant un réel non nul et u et v sont deux suites réelles. » Tableau (limite de u | limite de v | limite de u+v | limite de uv | limite de u/v), 7 lignes :
1. ℓ≠0 | ±∞ | ±∞ | ±∞ | 0
2. ±∞ | ℓ≠0 | ±∞ | ±∞ | ±∞
3. +∞ | +∞ | +∞ | +∞ | Pas de conclusion
4. −∞ | −∞ | −∞ | +∞ | Pas de conclusion
5. +∞ | −∞ | Pas de conclusion | −∞ | Pas de conclusion
6. 0 | ±∞ | ±∞ | Pas de conclusion | 0
7. ±∞ | 0 | ±∞ | Pas de conclusion | ±∞
(Les « Pas de conclusion » sont imprimés en rouge. Remarque de lecture : les lignes 1 et 2 sont imprimées avec « ±∞ » sans règle des signes explicite ; ligne 7, u/v « ±∞ ».)

**Activité 3 (p.147)** Déterminer la limite de la suite $(u_n)$ dans chacun des cas suivants : a) $u_n=2^n+(1-\frac1n)$ ; b) $u_n=1+2+...2^n$ ; c) $u_n=\frac{n^2+1}{2n-1}+\frac{e^{2n}}{n^2}$ ; d) $u_n=\left[2-\left(\frac12\right)^n\right]\left[1-\ln(n)\right]$.

##### 7) Limites et ordre (p.148-149)

**Activité 1 (p.148)** On considère les suites u, v et w définies sur $IN^*$ par : $u_n=\frac{3n+(-1)^n}{n}$ ; $v_n=\frac{3n-1}{n}$ et $w_n=\frac{3n+1}{n}$. 1) Montrer que par tout $n\in IN$, $v_n\le u_n\le w_n$. [coquille : « par tout » pour « pour tout » ; IN au lieu de IN*] 2) Déterminer $\lim v_n$ et $\lim w_n$ ($n\to+\infty$). 3) Que peut-on conjecturer à propos du comportement de $u_n$ quand n tend vers $+\infty$ ?

**Activité 2 (p.148)** On considère les suites $(u_n)$ et $(v_n)$ et définie sur IN par : $u_n=3n+\sin(n)$ et $v_n=-n^2+(-1)^n$. [coquille : « et définie »] 1) a - Montrer que pour tout $n\in IN$, $v_n\ge3n-1$. b- Calculer $\lim_{n\to+\infty}(3n-1)$. c- Que peut-on conjecturer à propos du comportement de $u_n$ quand n tend vers $+\infty$ ? 2) a – Montrer que pour tout $n\in IN$, $v_n\le-n^2+1$. b- Calculer $\lim_{n\to+\infty}(-n^2+1)$. c- Que peut-on conjecturer à propos du comportement de $u_n$ quand n tend vers $+\infty$ ? [coquilles : 1a doit porter sur $u_n$ ($u_n\ge3n-1$) ; 2a dit $v_n\le-n^2+1$ ce qui est correct pour $v_n$ mais la conjecture 2c porte sur $u_n$ alors que la question 1c concerne bien $u_n$ ; l'énoncé mélange u et v]

**Théorème (admis) (encadré vert, p.148) — verbatim** : « Soient $(u_n)_{n\ge p}$, $(v_n)_{n\ge p}$ et $(w_n)_{n\ge p}$ trois suites • S'il existe un entier $n_0\ge p$ tel que pour tout $n\ge n_0$, $u_n\ge0$ et si $\lim_{n\to+\infty}u_n=\ell$ alors $\ell\ge0$ • S'il existe un entier $n_0\ge p$ tel que pour tout $n\ge n_0$, $v_n\le u_n\le w_n$ et si $\lim_{n\to+\infty}v_n=\lim_{n\to+\infty}w_n=\ell$ alors : la suite $(u_n)$ converge et $\lim_{n\to+\infty}u_n=\ell$ • S'il existe un entier $n_0\ge p$ tel que pour tout $n\ge n_0$, $u_n\ge v_n$ et si $\lim_{n\to+\infty}v_n=+\infty$ alors $\lim_{n\to+\infty}u_n=+\infty$ • S'il existe un entier $n_0\ge p$ tel que pour tout $n\ge n_0$, $u_n\le v_n$ et si $\lim_{n\to+\infty}v_n=-\infty$ alors $\lim_{n\to+\infty}u_n=-\infty$ »

**Conséquence (encadré vert, p.148) — verbatim** : « Soient $(u_n)_{n\ge p}$ et $(v_n)_{n\ge p}$ deux suites. S'il existe un entier $n_0\ge p$ tel que pour tout $n\ge n_0$, $|u_n|\le v_n$ et si $\lim_{n\to+\infty}v_n=0$ alors $\lim_{n\to+\infty}u_n=0$ » (la valeur absolue de $u_n$ est lue à l'image ; la couche texte l'a perdue).

(suite de la rubrique 7, p.149)

**Activité 3 (p.149)** Déterminer les limites de chacune des suites : $(u_n)$, $(v_n)$, $(w_n)$, $(t_n)$ et $(h_n)$ définies sur IN par : a) $u_n=\left(\frac34\right)^n\cos(n)$ ; b) $v_n=\frac{\sin(n)}{n^2+1}$ ; c) $w_n=\frac{(-1)^n}{2n^2+n+3}$ ; d) $t_n=-5+(\sqrt2)^n$ ; e) $h_n=1+2+2^2+...+2^n$.

**Activité 4 (p.149)** Soit u et v les suites définies sur IN par $u_0=1$ et pour tout $n\in IN$, $u_{n+1}=2u_n+3$ et $v_n=-2u_n+(\frac12)^n$. 1- Vérifier que pour tout $n\in IN$, $u_{n+1}\ge2u_n$. 2- a) Montrer par récurrence que pour tout $n\in IN$, $u_n\ge2^n$ b) En déduire $\lim_{n\to+\infty}u_n$. 3- a) Vérifier pour tout $n\in\mathbb N^*$ on a $n\in IN$, $v_n\le-2^{n+1}+(\frac12)^n$ [formulation imprimée telle quelle, coquille : « pour tout n ∈ ℕ* on a n ∈ IN »] b) En déduire $\lim_{n\to+\infty}v_n$.

##### 8) Exemples de suites récurrentes (p.149-153)

###### Suites de la forme $u_{n+1}=au_n+b$ (p.149-150)

**Activité 1 (p.149)** On considère la fonction f définie sur IR par : $f(x)=0{,}75x+2$. Soit D sa représentation graphique dans le plan muni d'un repère orthonormé. Soit D' la droite d'équation : $y=x$. 1- Représenter les droites D et D'. Déterminez leur point d'intersection I. 2- On définit la suite $(v_n)$ par : $v_0=0$ et pour tout entier naturel n, $v_{n+1}=f(v_n)$. a) Placer, sur l'axe des abscisses, les points $A_n$ d'abscisses $v_n$ où $n\in\{0,1,2,..,8\}$. b) Que peut on conjecturer pour la limite de la suite $(v_n)$ 3-a) Montrer que la suite $(w_n)$ définie sur IN par $w_n=v_n-8$, est une suite géométrique et déterminer sa raison. b) Exprimer $v_n$ en fonction de $w_n$. c) Calculer la limite de la suite $(w_n)$ et en déduire la limite de la suite $(v_n)$.

**Activité 2 (p.149-150)** Soit $(u_n)$ la suite définie par $u_0=5$ et, pour tout entier naturel n, $u_{n+1}=\frac{2u_n+6}{3}$. 1- a) Calculer $u_1$, $u_2$ et $u_3$. b) Déduire que la suite $(u_n)$ n'est ni arithmétique ni géométrique. 2- On considère la suite $(v_n)$ définie pour tout entier naturel n, par $v_n=u_n-\alpha$. a) Exprimer $v_{n+1}$ en fonction de $v_n$. b) En déduire que $(v_n)$ est une suite géométrique dont on précisera la raison et le premier terme. c) Exprimer $v_n$ en fonction de n et en déduire $u_n$ en fonction de n. d) Déterminer le sens de variation de la suite $(u_n)$. e) Déterminer la limite de la suite $(u_n)$. [Note : α n'est pas défini dans l'énoncé ; il faut le déterminer (point fixe de $x\mapsto\frac{2x+6}{3}$) — le manuel ne le dit pas.]

###### Suites homographiques (p.150-152)

**Activité 1 (p.150)** Situation : migrations de population (pays, zones rurale/ville). « On suppose que dans une période, la population d'un pays est constante et égale à 60 millions d'habitants, dont 40 millions vivent en zone rurale et 20 millions en ville. On constate que les mouvements de population sont décrits par la règle suivante : « chaque année 20% des ruraux émigrent à la ville et 10% des citadins émigrent en zone rurale ». On note respectivement $v_n$ et $r_n$ les effectifs (en millions) des citadins et des ruraux au bout de n années. » 1- a) On considère la suite $(p_n)$ définie par $p_n=\frac{v_n}{r_n}$. Montrer qu'elle vérifie : $p_0=0{,}5$ et pour tout n de IN, $p_{n+1}=\frac{9p_n+2}{p_n+8}$. b) On pose pour tout entier naturel n, $q_n=\frac{p_n-2}{p_n+1}$. 2- a) Montrer que la suite $(q_n)$ est géométrique et exprimer $q_n$ et $p_n$ en fonction de n. b) Calculer la limite de la suite $(p_n)$. (Recalcul : $v_0=20$, $r_0=40$, $p_0=0{,}5$ ✓ ; $v_{n+1}=0{,}8v_n$-type bilan : $v_{n+1}=0{,}9v_n+0{,}2r_n$, $r_{n+1}=0{,}1v_n+0{,}8r_n$, d'où $p_{n+1}=\frac{9p_n+2}{p_n+8}$ ✓ — recalcul de ma part, le manuel ne donne pas ce corrigé.)

**Commentaire (encadré bleu, p.150) — verbatim** : « La suite $(p_n)$ est du type : $u_{n+1}=\frac{au_n+b}{cu_n+d}$, elle est dite ***suite homographique*** » (gras italique à l'impression).

**Activité 2 (p.150-151)** On considère la suite $(u_n)$ définie sur IN par $u_0=6$ et $u_{n+1}=\frac{4u_n+2}{u_n+3}$. Dans le graphique ci-contre, on donne la courbe représentative $C_f$ de la fonction $f:x\mapsto\frac{4x+2}{x+3}$ pour $x\in]-1,+\infty[$ et la droite D d'équation $y=x$. [Figure p.150 : repère gradué de -2 à 4 en abscisse, -1 à 2 en ordonnée ; $C_f$ et D se coupent aux points (-1 ; -1) et (2 ; 2), lu] 1-a) Déterminer graphiquement les abscisses α et β ; (α < β) des points d'intersection de la courbe $C_f$ et la droite D. b) Placer sur l'axe des abscisses, les points $A_n(u_n,0)$ pour $n\in\{0,1,2,3,4,5\}$. c) Quelles conjectures peut-on faire sur les variations et la limite de la suite $(u_n)$ ?. 2- Montrer que pour tout entier naturel n, $u_n\ge2$. a) Montrer que la suite $(u_n)$ est décroissante. b) En déduire que la suite $(u_n)$ est convergente et que sa limite ℓ vérifie : ℓ = f(ℓ). c) Prouver que ℓ ≥ 2 puis donner sa valeur. 3- Soit $(v_n)$ la suite définie sur IN par $v_n=\frac{u_n-2}{u_n+1}$. a) Montrer que $(v_n)$ est une suite géométrique de raison $\frac25$. b) Exprimer $u_n$ en fonction de $v_n$. c) Calculer la limite de la suite $(v_n)$, puis retrouver la limite de la suite $(u_n)$. [Note : le « 2- » est imprimé « Montrer que ... u_n ≥ 2 » puis a), b), c) à la suite : numérotation imprimée telle quelle. Dans l'énoncé 2c la lettre ℓ est parfois imprimée « A » par la couche texte — sur l'image c'est ℓ.]

**Activité 3 (p.151)** On considère la suite $(u_n)$ définie sur IN par : $u_0=-1$ et $u_{n+1}=\frac{u_n-1}{4u_n-3}$. 1- Soit f la fonction définie sur $]-\infty,\frac34[$ par $f(x)=\frac{x-1}{4x-3}$. a) Construire la courbe représentative C de la fonction f dans un repère orthonormé du plan. b) Montrer que la droite D : y = x est tangente à la courbe C et déterminer l'abscisse α de leur point de contact. c) Placer, sur l'axe des abscisses, les trois premiers termes de la suite $(u_n)$. d) Que peut on conjecturer pour la limite de la suite $(u_n)$ ? 2- Soit $(v_n)$ la suite définie sur IN par $v_n=\frac{1}{u_n-\alpha}$. a) Montrer que $(v_n)$ est une suite est arithmétique de raison -4 et de premier terme $v_0=-\frac23$. [coquille : « est une suite est »] b) Exprimer $v_n$ puis $u_n$ en fonction de n. c) Calculer la limite de la suite $(v_n)$, puis retrouver la limite de la suite $(u_n)$. (Recalcul : $f(x)=x\iff(2x-1)^2=0$, α = 1/2, $v_0=\frac1{-1-1/2}=-\frac23$ ✓ ; cohérent.)

**Encadré de résultat (vert, p.151) — verbatim** : « Si une suite $(u_n)$ de la forme $u_{n+1}=\frac{au_n+b}{cu_n+d}$ converge alors sa limite ℓ vérifie : $\ell=\frac{a\ell+b}{c\ell+d}$. »

**Activité 4 (p.151-152)** On considère la suite $(u_n)$ définie sur IN par : $u_0=2$ et $u_{n+1}=\frac{u_n+6}{u_n-4}$. 1- Soit f la fonction définie sur $]-\infty,4[$ par $f(x)=\frac{x+6}{x-4}$. a) Construire la courbe représentative C de la fonction f dans un repère orthonormé du plan. b) Déterminer les coordonnées du point d'intersection de C et la droite D : y = x. c) Placer, sur l'axe des abscisses, les quatre premiers termes de la suite $(u_n)$. d) Justifier que la suite $(u_n)$ n'est pas monotone. e) Que peut on conjecturer pour la limite de la suite $(u_n)$ ? 2- Soit $(v_n)$ la suite définie sur IN par $v_n=\frac{u_n+1}{u_n-6}$. a) Montrer que $(v_n)$ est une suite géométrique et déterminer sa raison. b) Calculer la limite de la suite $(v_n)$ et en déduire celle de la suite $(u_n)$.

**Activité 5 (p.152)** Soit $(u_n)$ la suite définie sur IN par : $u_0>2$ et $u_{n+1}=4\left(\frac{u_n-1}{u_n}\right)$. 1- a) Vérifier que pour tout entier naturel n on a : $u_{n+1}=4\left(1-\frac1{u_n}\right)$. b) Montrer que pour tout entier naturel n : $u_n>2$. c) Vérifier que pour tout entier naturel n on a : $u_{n+1}-u_n=-\frac{(u_n-2)^2}{u_n}$. d) Déduire que la suite $(u_n)$ est convergente et calculer sa limite ℓ. 2- Soit $(v_n)$ la suite définie sur IN par $v_n=\frac1{u_n-2}$. a) Montrer que $(v_n)$ est une suite arithmétique de raison $\frac12$. b) Exprimer $v_n$ puis $u_n$ en fonction de n. c) Calculer la limite de la suite $(v_n)$, puis retrouver la limite de la suite $(u_n)$. (Recalcul 1c : ✓.)

**Activité 6 (p.152)** On considère la suite $(u_n)$ définie sur IN par $u_0=-5$ et $u_{n+1}=\frac{-8u_n+9}{2u_n-11}$. 1- a) Vérifier que pour tout entier naturel n, $u_{n+1}+\frac32=\frac{-5}{2u_n-11}\left(u_n+\frac32\right)$. b) Montrer que pour tout entier naturel n, $u_n\le-\frac32$. c) Prouver que pour tout entier naturel n, $u_{n+1}-u_n=\frac{(u_n-3)(-2u_n-3)}{2u_n-11}$ et déduire que la suite $(u_n)$ est croissante. d) Montrer que la suite $(u_n)$ est convergente et calculer sa limite ℓ. 3- On considère la suite $(v_n)$ définie sur IN par $v_n=\frac{u_n+\frac32}{u_n-3}$. a) Montrer que $(v_n)$ est une suite géométrique dont on déterminera la raison et le premier terme. b) Calculer $\lim v_n$ et en déduire $\lim u_n$. [numérotation imprimée : 1- puis 3- (pas de 2-)]. (Recalcul 1a ✓.)

(suite de la rubrique 8, p.153 ; le titre courant de la page 153 est « Avec l'ordinateur » alors que les activités 7 et 8 prolongent la rubrique Cours)

**Activité 7 (p.153)** On considère la suite $(u_n)$ définie sur IN par : $u_0=\frac52$ et $u_{n+1}=\frac{u_n+2}{u_n}$. 1- Soit f la fonction définie sur l'intervalle $I=[\frac32,3]$ par $f(x)=\frac{x+2}{x}$. a) Montrer que f est dérivable sur I et que $f(I)\subset I$. b) Montrer que l'équation f(x) = x admet dans I une solution unique ℓ que l'on précisera. c) Montrer que pour tout x de I, $|f'(x)|\le\frac89$. d) Prouver que pour tout $x\in]\frac32,3[$ on a : $|f(x)-\ell|\le\frac89|x-\ell|$. 2- a) Montrer que pour tout entier naturel non nul n on a : $|u_{n+1}-\ell|\le\frac89|u_n-\ell|$. b) Montrer que pour tout entier naturel n on a : $|u_n-\ell|\le\frac12\left(\frac89\right)^n$. c) Déduire que la suite $(u_n)$ est convergente et calculer sa limite. [coquilles : 1d intervalle ouvert $]\frac32,3[$ alors que I est fermé ; 2a « entier naturel non nul » puis 2b « entier naturel n » — incohérence de domaine] [R7 : vérifié à l'image p.153 — ces deux formulations sont bien imprimées ; ce sont des particularités d'énoncé, pas des fautes typographiques (même schéma aux ex. 22 et 23 p.159-160, non relevé) : à lire « particularité » plutôt que « coquille »]. (Recalcul : $f'(x)=-\frac2{x^2}$, $|f'|\le\frac{2}{9/4}=\frac89$ sur I ✓ ; ℓ=2, $|u_0-\ell|=\frac12$ ✓.)

**Activité 8 (p.153)** On considère la suite $(u_n)$ définie sur IN par : $u_0=3$ et $u_{n+1}=\frac{u_n-1}{u_n+2}$. Soit la fonction $f:x\mapsto\frac{x-1}{x+2}$. a) Construire la courbe représentative C de la fonction f dans un repère orthonormé du plan. b) Vérifier que la courbe C et la droite D : y = x n'ont pas de point commun. c) Placer, sur l'axe des abscisses, les sept premiers termes de la suite $(u_n)$. d) Montrer par l'absurde que la suite $(u_n)$ est divergente.

---
#### AVEC L'ORDINATEUR (p.154)

Texte : « On se propose d'utiliser un tableur pour calculer les termes d'une suite définie par récurrence » [imprimé « de d'utiliser » : coquille].

**1ère situation** : « On considère la suite U définie sur IN par : $U_0=2$ et $U_{n+1}=\frac{n+1}{n^2+1}U_n$. Dans la colonne A on placera les valeurs de n et dans la colonne B les valeurs correspondantes de $U_n$. Ainsi on place 0 dans la cellule A2, 1 dans A3, 10 dans B2 et dans la cellule B3 la formule calculant son contenu en fonction du contenu de A2 et celui de B2. La formule étant : =(A2+1)*B2/(A2*A2+1) Remplir les cellules de la colonne A par des valeurs croissantes de n. Copier la formule et la coller dans les cellules correspondantes de la colonne B. Quelle conjecture peut on faire sur la limite de la suite U ? »
Capture d'écran du tableur (cellule B3 sélectionnée, formule affichée =(A2+1)*B2/(A2*A2+1)), colonnes A (n) et B (Un), lignes 2 à 14 :
n=0 : 10 ; 1 : 10 ; 2 : 10 ; 3 : 6 ; 4 : 2,4 ; 5 : 0,705882 ; 6 : 0,162896 ; 7 : 0,030818 ; 8 : 0,004931 ; 9 : 0,000683 ; 10 : 8,33E-05 ; 11 : 9,07E-06 ; 12 : 8,92E-07.
[INCOHÉRENCE imprimée : l'énoncé dit $U_0=2$ mais on « place 10 dans B2 » et la capture part de 10. Recalcul avec $U_0=10$ : U1=10, U2=10, U3=6, U4=2,4, U5=0,70588… ✓ la capture est cohérente avec $U_0=10$ ; l'énoncé « U_0 = 2 » est donc une coquille. Dans la capture, ligne 3 (n=1) = 10 et ligne 4 (n=2) = 10.]

**2ème situation** : « On considère la suite U définie sur IN par : $U_0=2$, $U_1=10$ et $U_{n+2}=1{,}5U_{n+1}-0{,}5U_n$. On procèdera de la même manière que précédemment, sauf que On deux lignes de données initiales $U_0$ et $U_1$. On introduit la formule dans la cellule B4 : =(1,5*B3-0,5*B2) » [coquille : « On deux lignes »].
Capture (B4 sélectionnée, formule =(1,5*B3-0,5*B2)) : n=0 : 2 ; 1 : 10 ; 2 : 14 ; 3 : 16 ; 4 : 17 ; 5 : 17,5 ; 6 : 17,75 ; 7 : 17,875 ; 8 : 17,9375 ; 9 : 17,96875 ; 10 : 17,98438 ; 11 : 17,99219 ; 12 : 17,99609. (Recalcul ✓ : 14=15-1, 16=21-5, 17=24-7, 17,5, 17,75, 17,875, 17,9375.) Aucune question n'est posée sur cette 2ème situation (la conjecture n'est demandée explicitement que pour la 1ère).

---
#### EXERCICES ET PROBLÈMES (p.155-)  (aucun corrigé dans le manuel)

**1-** Soit u la suite géométrique de raison 0,1 et de premier terme $u_0=5$. a) Exprimer $u_n$ en fonction de n. b) Montrer que pour tout entier naturel n, $u_n>0$. c) Montrer que la suite définie sur IN par $v_n=\ln(u_n)$, est arithmétique ; donner sa raison.

**2-** Soit u la suite arithmétique de raison ln2 et de premier terme $u_0=\ln3$. a) Exprimer $u_n$ en fonction de n. b) Montrer que la suite définie sur IN par $v_n=e^{u_n}$, est géométrique ; donner sa raison.

**3-** (finance, intérêts simples) « On place le 1er de chaque mois (du 1er janvier 2006 au 1er Décembre 2006 inclus) un montant de 300DT sur un compte rémunéré à intérêts simples à 0,4% par mois. On retire le capital acquis le 1 janvier 2007. a) Calculer le montant de l'intérêt rapporté par chacun des quatre premiers mois. b) $u_n$ est l'intérêt rapporté par le montant placé le n-ième mois. Montrer que la suite $(u_n)$ est arithmétique et donner sa raison. c) En déduire le montant total des intérêts acquis, puis le capital acquis. »
Encadré (italique) verbatim : « Un capital est dit placé à intérêts simples lorsque les intérêts ne s'ajoutent pas au capital pour porter eux-mêmes intérêts. Les intérêts versés à la fin du placement sont calculés proportionnellement à la durée du placement. $K_{n+1}=K_n+i\times K_n$ ; (i est le taux du placement) » [formule imprimée telle quelle ; elle exprime une croissance géométrique, donc ne correspond pas aux intérêts simples — coquille/incohérence signalée]

**4-** (intérêts composés) « On place un capital initial $C_0$ de 10 000DT à intérêts composés au taux annuel de 8%. Soit $C_n$ le capital dont on dispose au bout de n années. 1- Montrer que C est une suite géométrique dont on donnera la raison. Calculer $C_5$. 2- Au bout de combien d'années de placement, le capital acquis dépassera-t-il le double du capital initial ? Le résultat dépend-t-il du capital $C_0$ ? »
Encadré verbatim : « Un capital est dit placé à intérêts composés lorsque à l'issue de chaque période de placement, les intérêts s'ajoutent au capital et portent eux-mêmes intérêts au taux i de placement. $C_{n+1}=C_n+i\times C_0$ » [formule imprimée telle quelle ; correcte serait $C_n+i\times C_n$ — coquille signalée ; les deux formules des encadrés 3 et 4 semblent inversées l'une pour l'autre]

**5-** (annuités, intérêts composés) « On place le 2 janvier de chaque année, de 2007 à 2012 inclus, un montant de 1 000DT à intérêts composés au taux annuel de 5,5% a) De quel capital acquis C disposera-t-on le 2 janvier 2010 juste après le dernier versement ? b) Exprimer en fonction de n, le capital acquis $C_n$ après n versements annuels de 1 000DT (au 2 janvier de chaque année à partir de 2007). » [incohérence imprimée : versements « de 2007 à 2012 inclus » mais la question a) demande le capital au 2 janvier 2010 « juste après le dernier versement » ; le dernier versement serait en 2012 — datation non cohérente, à ne pas résoudre sans arbitrage ; on peut lire « après le dernier versement » = le versement de 2010 si l'on s'arrête en 2010]

**6-** « On considère les suite u et v définies pour tout entier naturel n, par $u_n=e^{an+b}$ et $v_n=\ln(u_n)$ où $a\in IR^*$ et $b\in IR$. 1- Montrer que u est une suite géométrique dont on précisera la raison et le premier terme. 2- Montrer que v est une suite arithmétique dont on précisera la raison et le premier terme. » [coquille : « les suite »]

**7-** « On considère les suites u et v définies sur IN par : $u_0=1$, $u_{n+1}=3U_n$ et $v_n=\ln(u_n)$. [coquille : « U_n » majuscule pour $u_n$] 1- Vérifier que u est une suite géométrique. Exprimer son terme général en fonction de n. 2- a) Montrer que v est une suite arithmétique dont on précisera la raison et le premier terme $v_0$. b) Exprimer $v_n$ en fonction de n. 3- a) Soit n un entier naturel non nul, calculer $S_n=v_0+v_1+v_2+...+v_{n-1}$ en fonction de n. b) En déduire en fonction de n, le produit : $P_n=u_0\times u_1\times u_2\times...\times u_{n-1}$. »

**8-** Soit u la suite définie sur IN par : $u_n=\frac{2+(-1)^n}{2^n}-1$. a) Prouver que, pour tout entier naturel n, $\frac{2+(-1)^n}{2^n}\ge0$. b) En déduire que, pour tout entier naturel n, $u_n\ge-1$. c) Vérifier que, pour tout entier naturel n, $2+(-1)^n\le3$ et $0<\frac1{2^n}\le1$. d) En déduire que pour tout entier naturel n, $u_n\le2$. (Recalcul : $\frac{2+(-1)^n}{2^n}\le 3$ d'où $u_n\le 3-1=2$ ✓.)

**9-** Dans chacun des cas suivants, étudier le sens de variation de la suite $(u_n)$ définie par son terme général $u_n$ : a) $u_n=\frac{n-1}{2n+1}$ ; b) $u_n=n^2+2n+5$ ; c) $u_n=\frac{2}{n^2+2n+5}$ ; d) $u_n=2^n-1$ ; e) $u_n=(-2)^n$ ; f) $u_n=3-1{,}1^n$ ; g) $u_n=\ln(1+\frac2n)$ ; h) $u_n=e^{3-n}$ ; i) $u_n=\sqrt{1+n+n^2}$ ; j) $u_n=\frac1{1+\sqrt n}$ ; k) $u_n=\frac12e^{0{,}1n+2}-3$ (exposant lu « 0,1n+2 » ; le glyphe 1 imprimé ressemble à un l, levé par la couche texte).

**10-** On considère la suite u définie pour $n\ge1$ par $u_n=\frac{4-n^2}{n}$. 1- a) Etudier le signe de $u_{n+1}-u_n$. b) En déduire le sens de variation de la suite u. 2- a) Déterminer la fonction f telle que $u_n=f(n)$. b) Retrouver le sens de variation de la suite U à l'aide de la fonction f. [coquille : « la suite U » majuscule]

**11-** On considère la suite u de terme général $u_n=\frac{1-n}{5-2n}$ pour tout entier $n\ge3$ et la fonction $f:x\mapsto\frac{x-1}{2x-5}$ définie sur $[3,+\infty[$. a) Etudier les variations de f et en déduire que $f(x)\le2$ pour tout réel x de $[3,+\infty[$. (suite de l'énoncé p.157)

(suite de l'exercice 11, p.157)
11 (suite) b) Déterminer la limite ℓ de f en $+\infty$. Exprimer f(x) – ℓ en fonction de x et en déduire que pour tout réel x de $[3,+\infty[$, $f(x)\ge\ell$. c) Construire la courbe C représentative de f dans un repère orthonormé du plan. d) Représenter la suite U dans le même repère. e) Déduire de l'étude de la fonction f un encadrement du terme général $u_n$ pour $n\ge3$. f) A partir de quel entier p peut-on affirmer que $u_n-\frac12\le10^{-3}$ ? [R7 : AUCUNE valeur absolue n'est imprimée (vérifié à 250 dpi) — la fiche disait à tort « la valeur absolue est imprimée » ; l'imprimé est $u_n-\frac12\le10^{-3}$ ; $u_n=f(n)$ avec ℓ=1/2]

**12-** Soit la suite u définie sur $IN^*$ par : $u_n=1+\frac1{\sqrt2}+\frac1{\sqrt3}+...+\frac1{\sqrt n}$. a) Vérifier que pour tout $k\in IN^*$, $\frac1{\sqrt k}\ge\frac1{\sqrt n}$. b) En déduire que pour tout $n\in IN^*$, $u_n\ge\sqrt n$. c) Déterminer alors $\lim_{n\to+\infty}u_n$. [la condition de a) est implicitement $k\le n$ ; non précisée dans l'énoncé]

**13-** On considère la suite $(u_n)$ définie sur $IN^*$ par $u_n=\int_0^1t^ne^t\,dt$. a) Vérifier que pour tout $t\in[0,1]$ on a $t^n\le t^ne^t\le et^n$. b) En déduire que pour tout $n\in IN^*$, $\frac1{2n+1}\le u_n\le\frac e{2n+1}$. c) Calculer $\lim_{n\to+\infty}u_n$. [ERREUR IMPRIMÉE vérifiée à 200 dpi : $\int_0^1t^n\,dt=\frac1{n+1}$, pas $\frac1{2n+1}$ ; l'encadrement imprimé est faux à droite (ex. n=1 : $u_1=\int_0^1te^t\,dt=1>\frac e3\approx0{,}906$). La bonne forme est probablement $\frac1{n+1}\le u_n\le\frac e{n+1}$ ; la limite 0 reste vraie.]

**14-** On considère la suite u définie par $u_0=1$ et $u_{n+1}=3u_n-1$ pour tout entier naturel n. 1- Calculer les trois premiers termes de la suite u. 2- On pose pour tout entier naturel n, $v_n=u_n-\frac12$. a) Montrer que la suite v est géométrique et donner sa raison et son premier terme. b) En déduire $v_n$ puis $u_n$ en fonction de n. c) En déduire la limite de la suite u.

**15-** On considère la suite u définie sur IN par : $u_0=e$ et $u_{n+1}=\sqrt{u_n}$. On pose $v_n=\ln(u_n)$ pour tout entier naturel n. 1- Montrer que v est une suite géométrique de raison $\frac12$. En déduire son terme général en fonction de n, puis $u_n$ en fonction de n. 2- pour tout entier naturel n, on pose : $S_n=v_0+v_1+v_2+...+v_n$ et $P_n=u_0\times u_1\times u_2\times...\times u_n$. a) Exprimer $S_n$ en fonction de n. En déduire $P_n$ en fonction de n. b) Calculer $\lim S_n$ puis $\lim P_n$ ($n\to+\infty$).

**16-** On considère la suite U définie par : $u_0=2$ et $u_{n+1}=0{,}8u_n+2$ pour tout $n\in IN$. 1- Calculez $u_1$, $u_2$ et $u_3$. 2- Déterminez un réel a tel que la suite $(v_n)$ définie pour tout entier naturel n par : $v_n=u_n+a$ soit une suite géométrique. On suppose dans la suite que pour tout entier naturel n, $v_n=u_n-10$. 3- a) Calculer $v_0$ puis donnez l'expression de $v_n$ en fonction de n. b) Quelle est l'expression de $u_n$ en fonction de n ? Déterminer $\lim u_n$. 4- Pour n entier naturel, on pose : $S_n=u_0+u_1+...+u_n$ et $T_n=v_0+v_1+...+v_n$. a) Quelle est l'expression de $T_n$ en fonction de n ? Calculer $\lim T_n$. b) Quelle est l'expression de $S_n$ en fonction de n ? Calculer $\lim S_n$. [coquille : « u_n..» ponctuation double]

**17-** On considère la suite u définie par $u_0=5$ et $u_{n+1}=\frac15u_n+8$ pour tout entier naturel n. 1- a) Le plan étant muni d'un repère orthonormé $(O,\vec i,\vec j)$, placer sur l'axe des abscisses les quatre premiers termes de la suite u. b) Que peut on conjecturer pour la convergence de la suite u ? 2- On considère la suite v définie par $v_n=u_{n+1}-u_n$ pour tout entier naturel n. a) Calculer les trois premiers termes de la suite v. b) Montrer que v est une suite géométrique, préciser sa raison. c) Exprimer $v_n$ en fonction de n. 3- Montrer que pour tout entier naturel $n\ge1$, on a $u_n=u_0+(v_0+v_1+v_2+....+v_{n-1})$. 4- En déduire que pour tout entier naturel $n\ge1$, $u_n=5+5(1-0{,}2^n)$. 5- Montrer que la suite u converge et préciser sa limite. [recalcul : point fixe 10, $u_n=10-5(0{,}2)^n=5+5(1-0{,}2^n)$ ✓ cohérent ; $u_1=9$, $v_0=4$]

**18-** Soit u la suite définie sur IN par : $u_0=2$ et pour tout $n\in IN$, $u_{n+1}=\frac{2u_n+1}{u_n+2}$. a) Montrer par récurrence que pour tout $n\in IN$, $|u_{n+1}-1|\le\frac13|u_n-1|$. b) Montrer par récurrence que pour tout $n\in\mathbb N$ $n\in IN$, $|u_{n+1}-1|\le(\frac13)^n$. c) Montrer alors que la suite $(u_n)$ est convergente et calculer sa limite. [coquille imprimée en b : « pour tout n ∈ ℕ n ∈ IN » doublé ; et le membre de gauche $|u_{n+1}-1|$ est imprimé ainsi alors que l'encadrement naturel serait $|u_n-1|\le(\frac13)^n$ ($|u_0-1|=1$ ✓ ; $|u_1-1|=\frac13$) ; en b l'indice imprimé est n+1 : vérifié à l'image]

**19-** On considère la suite $(u_n)_{n\in\mathbb N}$ définie par : $u_0=4$ et pour tout entier naturel n, $u_{n+1}=\frac{u_n}{1+3u_n}$. 1- Montrer par récurrence que pour tout entier naturel n, $u_n>0$. 2- On considère la suite $(v_n)_{n\in\mathbb N}$ définie par $v_n=\frac1{u_n}$. a) Prouver que $(v_n)$ est une suite arithmétique dont on donnera la raison et le premier terme $v_0$. b) En déduire $v_n$ puis $u_n$ en fonction de n. c) En déduire le sens de variation et la limite de la suite $(u_n)_{n\in\mathbb N}$.

**20-** On considère la suite u définie par $u_0=0$ et $u_{n+1}=\frac{u_n+6}{3u_n-2}$ pour tout entier naturel n. 1- Prouver que la fonction f définie par $f(x)=\frac{x+6}{3x-2}$ est décroissante sur $]-\infty,\frac23[$. 2- En déduire par récurrence, que pour tout entier naturel n, on a $-3\le u_n\le0$. Soit v la suite définie par $v_n=\frac{u_n+1}{u_n-2}$ pour tout entier naturel n. a) Exprimer $u_n$ en fonction de $v_n$. b) Montrer que v est une suite géométrique de raison $-\frac45$. c) En déduire la limite de $v_n$ lorsque n tend vers $+\infty$, puis la limite de $u_n$ lorsque n tend vers $+\infty$. [numérotation imprimée telle quelle]

**21-** Soit $(u_n)$ la suite définie par $u_0=1$ et pour tout entier naturel n, $u_{n+1}=\frac{2u_n+12}{u_n+1}$. 1- Etudier les variations de la fonction f définie sur $]0,+\infty[$ par $f(x)=\frac{2x+12}{x+1}$. 2- tracer dans un même repère orthonormé, la représentation graphique C de la fonction f et la droite D d'équation y = x. 3- En utilisant C et D, placer les points de coordonnées $(u_0,0)$, $(u_1,0)$, $(u_2,0)$ et $(u_3,0)$. 4- Que peut-on conjecturer pour la limite de la suite $(u_n)$. 5- Soit $(v_n)$ et $(w_n)$ les suites définies sur IN par $v_n=u_{2n}$ et $w_n=u_{2n+1}$. a) Montrer que pour tout entier naturel n, $1\le u_n\le7$. b) Montrer que $(v_n)$ est une suite croissante et que $(w_n)$ est une suite décroissante. c) En déduire que les suites $(v_n)$ et $(w_n)$ sont convergentes. 6- On considère $(t_n)$ la suite définie sur IN par $t_n=\frac{u_n-4}{u_n+3}$. a) Montrer que $(t_n)$ est une suite géométrique et déterminer sa raison et son premier terme. b) Calculer la limite de la suite $(t_n)$ et en déduire celle de la suite $(u_n)$. [recalcul : $u_1=14/2=7$ ; point fixe 4 ✓]

**22-** On considère la suite $(u_n)$ définie sur IN par : $u_0=4$ et $u_{n+1}=\frac{4u_n+3}{u_n+2}$. 1- Soit f la fonction définie sur l'intervalle $I=[3,+\infty[$ par $f(x)=\frac{4x+3}{x+2}$. a) Montrer que f est dérivable sur I et que $f(I)\subset I$. b) Montrer que l'équation f(x) = x admet dans I une solution unique ℓ que l'on précisera. c) Montrer que pour tout x de I, $|f'(x)|\le\frac15$. d) Prouver que pour tout $x\in]3,+\infty[$ on a : $|f(x)-\ell|\le\frac15|x-\ell|$. 2- a) Montrer que pour tout entier naturel non nul n on a : $|u_{n+1}-\ell|\le\frac15|u_n-\ell|$. b) Montrer que pour tout entier naturel n on a : $|u_n-\ell|\le(\frac15)^n$. c) Déduire que la suite $(u_n)$ est convergente et calculer sa limite. (Recalcul : $f'(x)=\frac5{(x+2)^2}\le\frac15$ sur I ; ℓ=3 ; $|u_0-3|=1$ ✓ ; cohérent.)

**23-** On considère la suite $(u_n)$ définie sur IN par : $u_0=-1$ et $u_{n+1}=\frac{u_n}{3-u_n}$. 1- Soit f la fonction définie sur l'intervalle $I=]-\infty,0]$ par : $f(x)=\frac x{3-x}$. a) Montrer que f est dérivable sur I et que $f(I)\subset I$. b) Résoudre dans I l'équation f(x) = x. c) Montrer que pour tout x de I, $|f'(x)|\le\frac13$. d) Prouver que pour tout $x\in]-\infty,0[$ on a : $|f(x)|\le\frac13|x|$. 2- a) Montrer que pour tout entier naturel non nul n on a : $|u_{n+1}|\le\frac13|u_n|$. b) Montrer que pour tout entier naturel n on a : $|u_n|\le(\frac13)^n$. c) Déduire que la suite $(u_n)$ est convergente et calculer sa limite. (Recalcul : $f'(x)=\frac3{(3-x)^2}\le\frac13$ sur I ; point fixe 0 ✓.)

**24-** Soient a, b et c trois réels tels que $ac-b\ne0$. On considère la suite $u=(u_n)_{n\in\mathbb N}$ définie par : $u_{n+1}=\frac{au_n+b}{u_n+c}$ et $u_0\ne-c$. 1- Montrer que la suite u est constante si et seulement si $u_0$ est solution de l'équation (E) : $x^2+(c-a)x-b=0$. 2- Dans cette question on prend a = 4, b = 3, c = 6 et $u_0=2$. a) Montrer que (E) admet deux racines distinctes α et β (β < α), que l'on précisera. b) On considère la suite v définie sur IN par $v_n=\frac{u_n-\alpha}{u_n-\beta}$. Montrer que la suite v est géométrique de raison $q=\frac37$. c) Exprimer $v_n$ puis $u_n$ en fonction de n. d) Calculer $\lim v_n$ puis $\lim u_n$ ($n\to+\infty$). (Recalcul : (E) : $x^2+2x-3=0$, α=1, β=-3 ; $\frac{u_{n+1}-1}{u_{n+1}+3}=\frac37\cdot\frac{u_n-1}{u_n+3}$ ✓.)

**25-** (association sportive — début d'énoncé, suite p.161) « Le président d'une association sportive constate que chaque année, l'association garde les trois quarts de ses anciens adhérents et qu'il y a 800 nouveaux adhérents. On suppose que l'évolution du nombre des adhérents reste le même au fil des ans et on se propose d'étudier cette évolution. On suppose que l'association a commencé ses activités » (suite à la page 161)

(suite de l'exercice 25, p.161)
25 (suite) « ... avec un nombre d'adhérents égal à 1600 et on désigne par $u_n$ le nombre d'adhérents au bout de n années. 1- Calculer $u_1$, $u_2$ et $u_3$. 2- Exprimer $u_{n+1}$ et fonction de $u_n$. [coquille : « et » pour « en »] 3- On pose $v_n=3200-u_n$. a) Montrer que la suite v est géométrique ; déterminer sa raison et son premier terme. b) Exprimer $v_n$ en fonction de n et en déduire que pour tout entier naturel n on a $u_n=3200-1600\times(0{,}75)^n$. c) Calculer la limite de la suite u. Interpréter le résultat. » (Recalcul : $u_{n+1}=0{,}75u_n+800$, $u_0=1600$, point fixe 3200, $v_0=1600$, $q=0{,}75$ ✓ ; $u_1=2000$, $u_2=2300$, $u_3=2525$ — recalcul de ma part.)

**26-** (économie — offre/demande, équilibre de marché) « Une usine produit des machines et les vend à un prix de $P_n$ l'année n. Les quantités offertes $O_n$ sont fonction du prix $P_{n-1}$ de l'année précédente. Les quantités demandées $D_n$ sur le marché sont fonction du prix $P_n$ de l'année n. Les fabricants recherchent l'équilibre du marché, c'est-à-dire qu'à chaque année n, on ait $O_n=D_n$. On a vérifié que : $O_n=2P_{n-1}-10$ pour $n>1$ ; $D_n=-3P_n+140$ pour $n>0$. » 1- a) Représenter sur le même graphique, les droites d'équations respectives $y=2x-10$ et $y=-3x+140$ puis déterminer leur point d'intersection. b) On suppose que $P_0=15$, calculer $O_1$ puis représenter sur le graphique $O_1$ et $P_1$. c) Calculer et représenter de même $P_2$ et $P_3$. d) Que peut on conjecturer pour la limite de la suite $(P_n)$ ? 2- A l'équilibre du marché, on a $O_n=D_n$. a) Démontrer que pour tout entier naturel $n>1$, $P_n=-\frac23P_{n-1}+50$. b) On pose pour tout entier naturel n, $U_n=P_n-30$ ; montrer que la suite $(U_n)$ est géométrique. Exprimer alors $U_n$ puis $P_n$ en fonction de n. c) Déterminer la limite p de la suite $(P_n)$. d) Quelles sont alors les quantités offertes et demandées à ce prix p ? [incohérence imprimée : $O_n$ est défini « pour n>1 » alors que 1b demande $O_1$ ; $D_n$ défini pour n>0 ; la loi $P_n=-\frac23P_{n-1}+50$ est annoncée « pour n>1 » alors que $P_1$ est utilisé. Recalcul : intersection : $2x-10=-3x+140\Rightarrow x=30$, $y=50$ ; $2P_{n-1}-10=-3P_n+140\Rightarrow P_n=\frac{150-2P_{n-1}}{3}=-\frac23P_{n-1}+50$ ✓ ; point fixe 30 ; à p=30, $O=D=50$ — recalcul de ma part.]

**27-** (finance — abonnements) « Un club de sport propose deux types d'abonnements non permutables. **Formule A** : Une cotisation annuelle de 50DT à laquelle s'ajoute la première année seulement un droit d'entrée de 100DT. **Formule B** : Une cotisation annuelle initiale de 10DT qui augmente de 10% par an. Dès la seconde année, pour fidéliser la clientèle, on effectue une réduction de 0,5DT sur la cotisation annuelle. Si $C_n$ est le montant, exprimé en DT, de la cotisation annuelle de la nième année, on a $C_1=10$ et pour tout entier n supérieur ou égal à 1, $C_{n+1}=1{,}1C_n-0{,}5$. 1- Déterminez la somme $T_n$ versée au club de sport par membre pendant n années avec la formule A. 2- Soit $(D_n)$ la suite définie pour tout entier n supérieur ou égal à 1 par $D_n=C_n+a$ où a est un réel. a) Déterminer le réel a pour que la suite $(D_n)$ soit une suite géométrique de raison 1,1 et préciser son premier terme. b) Exprimer $D_n$ puis $C_n$ en fonction de n. c) Déterminer la somme $S_n$ versée au club par un membre pendant n années avec la formule B. d) Quel nombre minimum d'années un membre doit-il cotiser pour que la formule A soit plus avantageuse que la formule B ? » (Recalcul : a = -5, $D_1=5$ ; $C_n=5\cdot1{,}1^{n-1}+5$ — recalcul de ma part, non imprimé.)

**28-** « Soit a un réel strictement positif, on considère la suite arithmétique V de raison a et de premier terme 0. 1- On définit sur IN les suites A et I par $A_n=\int_{a^n}^{a^{n+1}}\frac1x\,dx$ et $I_n=\int_{V_n}^{V_{n+1}}3^x\,dx$. a) Montrer que la suite A est constante dont précisera la valeur en fonction de a. [coquille : « dont précisera »] Interpréter graphiquement chacun des termes de cette suite. b) Montrer que la suite I est géométrique dont on précisera la raison en fonction de a. Calculer la somme $I_0+I_1+I_2+...+I_{10}$ par deux méthodes. 2- On considère l'intégrale $B_n=\int_n^{n+1}3e^{0{,}1t}\,dt$ où n est un entier naturel. a) Exprimer cette intégrale en fonction de n. b) Démontrer que $B_n$ est le terme général d'une suite géométrique dont on donnera la raison et le premier terme (on donnera les valeurs exactes). c) Calculer par deux méthodes la somme $S_n=B_0+B_1+....+B_{11}$. »

**29-** « a est un nombre réel tel que $0<a<\frac\pi4$. $(u_n)$ est la suite réelle définie pour n entier naturel non nul par les relations : $u_1=1+\frac1{2(\sin a)^2}$ et pour tout entier naturel n non nul, $u_{n+1}=\cos(2a)u_n+1$. 1- Démontrer que : $u_n>1$ pour tout naturel n non nul. 2- On pose pour n entier naturel non nul : $v_n=u_n-\frac1{2(\sin a)^2}$. a) Montrer que la suite $(v_n)$ est géométrique. b) Exprimer $v_n$ en fonction de n et de a, puis $u_n$ en fonction de n et de a. c) Les suites $(v_n)$ et $(u_n)$ sont-elles convergentes ? Justifiez la réponse. 3- Pour tout entier naturel non nul n, on pose $S_n=u_1+u_2+...+u_n$. a) Quelle est l'expression de $S_n$ en fonction de n ? b) Déterminer la limite de $S_n$ lorsque n tend vers $+\infty$. » (Recalcul : $\frac1{1-\cos2a}=\frac1{2\sin^2a}$ : point fixe cohérent.)

**30-** 1- Démontrer que pour tout entier naturel n, on a $e^{n+1}>2e^n$. 2- Soit $(u_n)$ la suite définie par : $u_n=\int_n^{n+1}(e^x+1)\,dx$, pour tout entier naturel n. a) Préciser le sens de variation de la suite $(u_n)$. b) En déduire que $u_n>e$, pour tout entier naturel n non nul. c) Calculer la limite de $u_n$ lorsque n tend vers $+\infty$. 3- On considère la suite $(S_n)$ définie pour tout entier naturel n par : $S_n=u_0+u_1+...+u_n-n$. a) Démontrer que la suite $(S_n)$ est une suite géométrique, dont on précisera la raison. b) Déterminer les entiers naturels tels que : $S_n>23$. [coquille : « les entiers naturels » sans « n » ; un point isolé « . » avant le b) ; recalcul : $u_n=e^n(e-1)+1$ ;]

**31-** (aire et suites) « Les courbes $H_1$ et $H_2$ représentées dans le repère orthonormé ci-contre ont respectivement pour équation $y=\frac1x$ et $y=\frac2x$. On note $D_2$ le domaine délimité par les courbes $H_1$ et $H_2$ et les droites d'équation x = 2 et x = 3. On note $D'_2$ le domaine délimité par l'axe des abscisses, la courbe $H_1$ et les droites d'équation x = 2 et x = 3. 1- Colorier les domaines $D_2$ et $D'_2$ d'une couleur différente et montrer qu'ils ont la même aire. Soit n un entier naturel strictement positif. On note $u_n$ l'aire du domaine $D_n$ délimité par les courbes $H_1$ et $H_2$ et les droites d'équation x = n et x = n +1. 2- Exprimer $u_n$ en fonction de n. 3- Montrer que la suite $(u_n)$ est décroissante. On pourra comparer les nombres n(n +2) et (n +1)². 4- Étudier la convergence de la suite $(u_n)$. 5- Déterminer la plus grande valeur de n telle que l'aire du domaine $D_n$ reste supérieure à 1/10 d'unité d'aire. Soit N cette valeur. 6- Calculer l'aire du domaine délimité par les courbes $H_1$ et $H_2$ et les droites d'équation x =1 et x = N. » Figure (p.163) : repère orthonormé gradué en 0 et 1 (une graduation 1 en abscisse et en ordonnée), $H_1$ (courbe inférieure, magenta) et $H_2$ (courbe supérieure, bleue), décroissantes vers l'axe des abscisses, aucune valeur numérique supplémentaire. (Recalcul : $u_n=\int_n^{n+1}\frac1x\,dx=\ln\frac{n+1}n$, $D_2$ et $D'_2$ même aire car $H_2-H_1=H_1$ ✓ ; $u_n>0{,}1$ ⇔ $\frac{n+1}{n}>e^{0,1}$ — recalcul de ma part.)

---
#### MATH CULTURE (p.164) — « La flèche toujours sans cible !! »
Texte (résumé fidèle, chiffres verbatim) : un maître archer tire une flèche vers une cible située à vingt mètres ; vitesse constante de dix mètres par seconde. Zénon d'Elée, mathématicien grec du cinquième siècle avant Jésus-Christ, avait proposé un paradoxe « qui ne fut complètement résolu qu'au dix-huitième siècle, soit vingt-deux siècles plus tard ». Partant du principe qu'on ne peut pas effectuer réellement une infinité d'étapes, il concluait à l'impossibilité de tous les mouvements. La flèche tirée d'un point A vers un point B passe d'abord par le milieu $M_0$ de [AB], puis par le milieu $M_1$ de $[M_0B]$, etc. : une infinité de milieux (figure : segment AB avec $M_0$, $M_1$, $M_2$, ..., B, flèches).
**Résolution du paradoxe** (verbatim) : « La distance parcourue est la limite lorsque n tend vers l'infini, de la distance $d_n$ égale à : $20\times\frac12+20\times\left(\frac12\right)^2+20\times\left(\frac12\right)^3+...+20\times\left(\frac12\right)^n$ c'est-à-dire de $d_n=20\left(1-\left(\frac12\right)^n\right)$, en un temps total en secondes égal à la limite lorsque n tend vers l'infini de $t_n=2\left(1-\left(\frac12\right)^n\right)$. On vérifie que les suite $(d_n)$ et $(t_n)$ sont convergentes et que $\lim d_n=20$ et $\lim t_n=2$. On peut donc imaginer que la flèche parcourt une infinité de milieux, mais l'ensemble se produit bien en un temps fini et notre flèche atteint bien sa cible en un temps fini égal à 2 secondes !! » [coquille : « les suite »]. Source : aucune source n'est citée dans le manuel pour cet encadré (vérifié p.164). Recalcul : $d_n=20(1-(1/2)^n)$ ✓ ; $t_n=d_n/10$ ✓.

---
#### VOCABULAIRE OFFICIEL (chapitre VI)
suite réelle ; terme général ; suite définie par récurrence / suite récurrente ; suite arithmétique (raison, premier terme) ; suite géométrique (raison, premier terme) ; suite minorée (par m) / majorée (par M) / bornée ; suite croissante, strictement croissante, décroissante, strictement décroissante, constante, monotone ; somme, produit, valeur absolue, inverse, quotient de suites ; limite d'une suite ; suite convergente / divergente ; « Pas de conclusion » ; encadrement (théorème des gendarmes non nommé : le manuel ne l'appelle pas ainsi, voir Théorème p.148) ; suite homographique ; point fixe non nommé (le manuel écrit « sa limite ℓ vérifie ℓ = f(ℓ) » ) ; intérêts simples / intérêts composés (exercices 3-4) ; raisonnement par récurrence, par l'absurde ; le manuel emploie IN, IN*, ℕ, IR indifféremment.

#### BORNES (déduites du seul contenu des pages)
INCLUS : suites arithmétiques et géométriques (rappels, termes généraux, sommes, limites selon raison) ; suites minorées/majorées/bornées ; variation d'une suite (signe de $u_{n+1}-u_n$, récurrence, suite $u_n=f(n)$ et sens de variation de f) ; opérations sur les suites ; suites convergentes/divergentes, théorème $\lim f(x)=\ell\Rightarrow\lim f(n)=\ell$ ; théorème « croissante majorée converge, décroissante minorée converge » (admis) ; opérations sur les limites (somme, produit, quotient, tableau des formes déterminées) ; limites et ordre (comparaison, encadrement, $|u_n|\le v_n\to0$) ; suites récurrentes $u_{n+1}=au_n+b$, $u_{n+1}=\frac{au_n+b}{cu_n+d}$ (méthode : suite auxiliaire géométrique/arithmétique), $u_{n+1}=f(u_n)$ avec $|f'|\le k<1$ ; problèmes d'intérêts simples/composés, d'offre-demande, d'abonnements ; tableur (récurrence à un et deux pas) ; suites d'intégrales (ex. 13, 28, 30, 31).
EXCLU (non présent dans ces pages) : définition formelle de la limite par ε (aucune définition epsilon dans le chapitre) ; théorème d'unicité démontré (admis) ; théorème des suites adjacentes (non cité ; les activités 6 et 7 de p.146 emploient seulement croissante-majorée) ; équations de récurrence linéaires d'ordre 2 (la 2ème situation du tableur n'est pas résolue) ; formule générale de $u_n$ pour $u_{n+1}=au_n+b$ non encadrée (elle se retrouve par activité 1-2 p.149) ; le mot « théorème des gendarmes » n'apparaît pas ; aucune « somme de série » au sens de convergence de série.

#### NOTIONS-CLÉS (≤ 8)
1. Suite arithmétique / géométrique : terme général, somme, limite selon r ou q (encadrés p.140). 2. Minorée / majorée / bornée (définitions p.141). 3. Monotonie : signe de $u_{n+1}-u_n$, récurrence, lien avec f(n) (théorème admis p.143). 4. Opérations sur les limites et tableau des formes (p.146-147). 5. Limites et ordre : comparaison, gendarmes, $|u_n|\le v_n$ (p.148). 6. Convergence monotone (théorème p.146) et unicité de la limite. 7. Suite récurrente $u_{n+1}=au_n+b$ : poser $v_n=u_n-\ell$ (ℓ point fixe) → géométrique. 8. Suite homographique : $v_n=\frac{u_n-\alpha}{u_n-\beta}$ (géométrique) ou $\frac1{u_n-\alpha}$ (arithmétique), limite vérifiant ℓ = (aℓ+b)/(cℓ+d) (encadré p.151) ; contraction $|u_{n+1}-\ell|\le k|u_n-\ell|$.

---
#### § NOTES
**Pages lues** : 28/28 (PDF 137 à 164). Page 137 = page de titre du chapitre (sommaire seul). Toutes les pages lues à l'image à 110 dpi.
**Pages sondées en agrandi (170-220 dpi)** : 138 et 139 (graphiques de la Pour commencer, Activité 2) ; 143 (Act. 3 de « Variation d'une suite » : $u_n=(\frac14)^n-2$, l'imprimé est bien « - 2 ») ; 156 (ex. 9, lignes g à k) ; 157 (ex. 13, borne $\frac1{2n+1}$ confirmée imprimée).
**Écarts texte / image** : la couche texte perd les racines (activité 4 p.142 $\sqrt{3+e^n}$ ; ex. 12 ; ex. 15 ; ex. 9i), la valeur absolue de la Conséquence p.148 ($|u_n|\le v_n$), les exposants $n^2$ (Avec l'ordinateur p.154 : $\frac{n+1}{n^2+1}$), les lettres ℓ (lues « A »/« l ») ; tout est repris de l'image. Les formules de l'image font foi dans ce fichier.
**Coquilles / incohérences imprimées (reproduites et signalées dans le corps)** :
- p.139 Act. 3-2c : somme écrite avec u au lieu de v.
- p.143 Act. 3-1a : « minorée par 2 » faux pour $u_n=(\frac14)^n-2$ (minorant correct -2) ; 3-2b : $(u_n)$ pour $(v_n)$.
- p.148 Act. 1 « par tout n ∈ IN » (suites sur IN*) ; Act. 2 : question 1a/2a énoncées sur $v_n$ alors que la conjecture porte sur $u_n$ ; « et définie ».
- p.149 Act. 4-3a formulation doublée « n ∈ ℕ* on a n ∈ IN ».
- p.149-150 Act. 2 : α non défini dans l'énoncé.
- p.153 Act. 7 : 1d intervalle ouvert alors que I fermé ; 2a « non nul » vs 2b « n ».
- p.154 Avec l'ordinateur : $U_0=2$ imprimé alors que la capture démarre à 10 (B2 = 10) ; « de d'utiliser » ; « On deux lignes ».
- p.155 ex. 3 et 4 : encadrés de formules $K_{n+1}=K_n+i\times K_n$ (« intérêts simples ») et $C_{n+1}=C_n+i\times C_0$ (« intérêts composés ») apparemment permutés/erronés ; ex. 5 : dates 2007-2012 et question « 2 janvier 2010 juste après le dernier versement » incohérentes ; ex. 6 « les suite ».
- p.156 ex. 7 « U_n » majuscule ; ex. 10 « suite U ».
- [R7 : p.157 ex. 11f — l'imprimé est $u_n-\frac12\le10^{-3}$ SANS valeur absolue (la fiche affirmait le contraire ; corrigé dans le corps).]
- p.157 ex. 13b : bornes $\frac1{2n+1}$, $\frac e{2n+1}$ fausses (devrait être n+1) ; ex. 12a : condition k ≤ n absente.
- p.158 ex. 18b : « n ∈ ℕ n ∈ IN » doublé et indice n+1 imprimé au membre de gauche.
- p.160 ex. 25 / p.161 : « et fonction » ; ex. 26 : bornes d'indices (n>1 vs O_1).
- p.162 ex. 28 « dont précisera » ; p.163 ex. 30-3b « les entiers naturels » sans n.
- p.164 « les suite ».
- numérotation : p.152 Act. 6 passe de 1- à 3- (pas de 2-) ; p.151 Act. 2 : « 2- Montrer... » suivi de a), b), c) ; titre courant de la p.153 = « Avec l'ordinateur » bien que les activités 7-8 appartiennent à la section 8 du Cours.
**Lectures graphiques (non écrites par le manuel)** : points des 4 graphiques de la Pour commencer Act. 2 (valeurs lues, non vérifiables autrement) ; points d'intersection α=-1, β=2 de $C_f$ et D p.150.
**`[?]` restants** : aucun bloc illisible ; seule réserve : exposant de l'ex. 9k lu « 0,1n+2 » (glyphe 1/l ambigu à l'image, tranché par la couche texte) et les valeurs exactes des points des graphiques de la Pour commencer Act. 2 (notées « lu »).
**Aucune solution n'est donnée dans le manuel** pour aucune activité, exercice ou problème de ces 28 pages : les « recalculs » indiqués entre parenthèses sont des vérifications de cohérence de la fiche, pas des corrigés du manuel.

---

### Chapitre `m07-p165-200`

### m07 — Manuel Maths 4e secondaire Économie et gestion (222463P00.pdf), pages 165-200 : Chapitre VII « Matrices et systèmes »

Source : manuel officiel CNP « Mathématiques », 4ᵉ année secondaire, section économie et gestion. Page PDF = page imprimée. Notation : matrices écrites en lignes séparées par « ; » entre crochets, ex. [a b ; c d] = matrice 2×2 de lignes (a b) et (c d). Notation linéaire, rien simplifié.

#### p.165 — Page de titre du chapitre
« Chapitre 7 — MATRICES ET SYSTEMES ». Plan imprimé : Pour commencer ; Cours : Matrices · Déterminant d'une matrice carrée d'ordre 2 ou 3 · Inverse d'une matrice carrée d'ordre 2 ou 3 · Résolution des systèmes linéaires de premier degré à deux ou trois inconnues ; Avec l'ordinateur ; Exercices et problèmes ; Math culture.

#### POUR COMMENCER (p.166)

##### Activité 1
« Donner le nombre de solutions dans IR² de chacun des systèmes suivants (les solutions ne sont pas demandées). »
- S1 : 3x − y = 2 ; x + 5y = 1
- S2 : 2x + 3y = 1 ; 6x + 9y = 1
- S3 : 5x + 2y = 2 ; 10x + 4y = 4
(Corrigé non donné par le manuel.)

##### Activité 2
1- « Résoudre dans IR² les systèmes suivants : » (a) 2x − 3y = −1 ; x + 2y = 10 — (b) 5x − y = 8 ; −3x + 7y = 8
2- « Résoudre dans IR³ les systèmes suivants : »
- (a) x + y + z = 3 ; x + y − z = 1 ; x − 2y + 2z = 1
- (b) 2x − y + 3z = 5 ; x + 2y − z = −1 ; x + 7y − 6z = −2
- (c) 2x + y − z = 0 ; 2x + y + z = 1 ; 2x + y − 3z = 2

##### Activité 3
Situation : coût total de production d'une quantité x d'un produit, modélisé par C(x) = a x² + b x + c, a, b, c trois réels. Le coût est exprimé en milliers de dinars et la quantité x en kilogrammes. Données (verbatim) : « les coûts fixes sont de cinq milles dinar ; le coût total de 1 kg est de 6000 DT et le coût total de 2 kg est de 9000 DT. » Travail : « Déterminer l'expression de C(x). » (Raisonnement attendu : non donné ; se ramène à un système 3×3 en a, b, c : c = 5 (milliers), a+b+c = 6, 4a+2b+c = 9 — déduit par le lecteur, le manuel ne le détaille pas.)

##### Activité 4
Situation : employés d'une entreprise partagés en 3 groupes de travail : 1er groupe : un cadre, 2 agents techniques et 3 ouvriers ; second groupe : 2 cadres, 3 agents techniques et 5 ouvriers ; 3ème groupe : 3 cadres, 2 agents techniques et 7 ouvriers. Masses salariales en DT du premier, du second et du troisième groupe respectivement : 3100, 5300 et 6300. Travail : « Déterminer les salaires moyens respectifs d'un cadre, d'un agent technique et d'un ouvrier. » (Système : x+2y+3z=3100 ; 2x+3y+5z=5300 ; 3x+2y+7z=6300 — mise en équation par le lecteur, non écrite par le manuel.)

#### COURS

##### I- Matrices — 1) Notion de matrice (p.167-169)

###### Activité 1 (p.167)
Situation : état du stock concernant deux produits de beauté B1 et B2 sur trois points de vente P1, P2 et P3. Tableau :
| | B1 | B2 |
|---|---|---|
| P1 | 70 | 35 |
| P2 | 30 | 27 |
| P3 | 27 | 24 |
Questions : 1- « Donner la colonne représentant l'état du stock du produit B1 sur les trois points de ventes. » 2- « Donner la ligne représentant l'état du stock en B1 et B2 sur le point de vente P3. » 3- « Que représente le nombre 24 situé à l'intersection de la troisième ligne et la deuxième colonne du tableau ? »
Synthèse imprimée : « Les informations précédentes peuvent être résumées dans le tableau à trois lignes et deux colonnes suivant : [70 35 ; 30 27 ; 27 24] appelé matrice d'ordre 3×2 ».

**Définition (encadré)** : « n et p étant deux entiers naturels non nuls, une **matrice** d'ordre n × p est un tableau de nombres réels formé de n lignes et de p colonnes. Ces nombres sont appelés coefficients ou termes de la matrice. »

**Notation (encadré)** : « ● Soit M une matrice d'ordre n × p. Le coefficient situé à l'intersection de la i^ème ligne et la j^ème colonne est noté a_ij. ● Toute matrice M de coefficients a_ij avec i et j des entiers vérifiant : 1 ≤ i ≤ n et 1 ≤ j ≤ p. est notée ( a_ij ) et représentée comme ci-dessous. » Schéma : M = tableau dont la première ligne est (a_11 … a_1j … a_1p), une ligne intermédiaire (a_i1 … a_ij … a_ip), la dernière (a_n1 … a_nj  a_np) ; colonnes numérotées 1, j, p ; lignes numérotées 1, i, n.

###### Activité 2 (p.168)
1) « Soit A une matrice d'ordre 3×3 dont voici certains termes : a21 = 4, a32 = 5, a23 = 1, a13 = −5, a12 = 7, a31 = 3. Recopier et compléter A = [6 . . ; . 1 . ; . . 0] » (points = termes à compléter ; diagonale donnée 6, 1, 0).
2) « Soit la matrice B = [−3 1 . ; . . √3] dont les termes manquants sont : b21 = 4, b22 = −1 et b13 = 5. » a) Recopier et compléter B. b) Quel est l'ordre de B ? c) Déterminer b23. Peut-on parler de b32 ? Pourquoi ?

###### Activité 3 (p.168)
Situation : notes de trois élèves e1, e2, e3 ; « pour i ∈ {1,2,3}, la colonne i indique les notes de l'élève e_i respectivement en mathématiques, en économie et en gestion. » M = [10 12 9 ; 10 15 13 ; 15 12 11].
Questions : 1- Donner l'ordre de M. Que représente la troisième colonne de M ? Que représente la première ligne de M ? 2- Quelle est la note obtenue en économie pour l'élève e3 ? 3- On pose M=(a_ij). Donner les valeurs de a11, a23, a33 et a32.

**Vocabulaire (verbatim, p.168-169)** :
- « Une matrice formée d'une seule ligne et de p colonnes s'appelle une **matrice ligne** d'ordre p. » Exemple : A = (1  2  −2/5) est une matrice ligne d'ordre 3.
- « Une matrice formée d'une seule colonne et de n lignes s'appelle une **matrice colonne** d'ordre n. » Exemple : B = (2 ; 1) (colonne) est une matrice colonne d'ordre 2.
- « Une matrice ayant le même nombre n de lignes et de colonnes est une **matrice carrée** d'ordre n. »
- « La **diagonale** d'une matrice carrée A=(a_ij) d'ordre n est la rangée formée des coefficients a_ii. » (schéma p.169 : diagonale de a_11 à a_nn.)
- « La **matrice unité d'ordre n**, notée I_n, est une matrice carrée d'ordre n dont tous les coefficients sont nuls sauf ceux de la diagonale valent 1. » I2 = [1 0 ; 0 1] ; I3 = [1 0 0 ; 0 1 0 ; 0 0 1].
- « Une matrice d'ordre n×p dont tous les coefficients sont nuls est dite **matrice nulle** d'ordre n×p cette matrice est notée **O**. » O = [0 0 0 ; 0 0 0 ; 0 0 0] est la matrice nulle d'ordre 3.

###### Activité 4 (p.169)
Soit A = [6 −4 ; −1 2 ; 3 −5]. « Répondre par vrai ou faux en justifiant la réponse. » a) A est une matrice d'ordre 2x3. b) a22 = -1. c) a32 = -5.

**Propriété (encadré)** : « Deux matrices sont égales si et seulement si, elles sont de même ordre et leurs coefficients de mêmes indices sont égaux deux à deux. »

###### Activité 5 (p.169)
1) « Compléter les matrices A = [−1 ... 0 ; 1 −2 ...] et B = [−1 7 ... ; ... −2 6] pour qu'elles soient égales. » 2) « Déterminer le réel a pour que la matrice B = [a² a²−1 ; 2a+2 a²] soit égale à la matrice unité d'ordre 2. »

##### I- 2) Opérations sur les matrices (p.170-172) — Addition

###### Activité 1 (p.170)
Situation : un gestionnaire de stock d'une chaîne de magasins suit, sur trois points de vente, l'état du stock de trois articles de confection : séries de chemises (c), de pantalons (p), de vestes (v). Matrices (lignes étiquetées c, p, v) :
- I (état initial) = [3 1 1 ; 0 2 1 ; 5 10 0]
- E (entrées) = [20 10 20 ; 10 15 25 ; 25 30 30]
- S (sorties) = [18 9 5 ; 20 4 3 ; 25 10 10]
Questions : 1- Donner la matrice S1 représentant le stock total avant les sorties. 2- Donner la matrice S2 représentant le nouvel état des stocks après les sorties.

**Définition (encadré)** : « Soit A = (a_ij) et B = (b_ij) deux matrices de même ordre n × p. ♦ La somme des deux matrices A et B, notée A + B, est la matrice C = (a_ij + b_ij) de même ordre n × p. ♦ La différence des deux matrices A et B, notée A – B, est la matrice D = (a_ij − b_ij) de même ordre n × p. »

###### Activité 2 (p.170)
1- « Vérifier que [1 0 ; 1 −1 ; 2 0] + [3 √5 ; 1 −1 ; 2 0] = [4 √5 ; 2 −2 ; 4 0] et que [3 0 2 ; −2 5 −1] − [1 5 −2 ; −3 0 −1] = [2 −5 4 ; 1 5 0] »
2- Calculer : (1 −1 2) + (0 2 2/3) ; (1;1;0) + (0;−2;−5) (colonnes) ; [20 1 0 ; 10 −5 25 ; −2 30 0] + [0 10 20 ; 10 15 5 ; 5 30 3] ; (3;−1) − (5;−2) ; [2 1 −1/6 ; √5 5 −√5 ; 11 2 5/2] − [1 −3 5/6 ; 0 5 −√5 ; 9 −2 3/2].
3- « Soient A = [x 5 ; 0 2x] et B = [y 7 ; −1 3y] où x et y sont deux réels, déterminer x et y pour que : A+B = [4 12 ; −1 17]. »

###### Propriétés (p.171, encadré)
« A, B, C trois matrices d'ordre n × p (n et p deux entiers naturels non nuls) et O la matrice nulle d'ordre n × p. ♦ A + O = O + A = A ♦ A + B = B + A. ♦ (A+B) + C = A + (B + C). »

###### Activité 3 (p.171)
Calculer : A = [1 −2 0 ; 3 7 −1 ; 2 4 −2] + [0 4 −3 ; −1 6 −3 ; 2 8 0] + [2 −2 0 ; 0 3 −3 ; 2 4 −2] ; B = (1 −5 1/3) − (0 −1/5 1/3) + (1/15 4 7).

##### Multiplication d'une matrice par un réel (p.171-172)

###### Activité 1 (p.171)
Soit A = [6 −4 ; −1 2 ; 3 −5], « calculer A+A qu'on note 2A puis calculer 2.A + A qu'on note 3A ».

**Définition (encadré)** : « Le produit d'une matrice A par un réel k est la matrice notée kA obtenue en multipliant chaque coefficient de A par le réel k. »
**Remarque (encadré)** : « ♦ k.A et A sont deux matrices de même ordre. ♦ (−1).A = −A (la matrice opposée de A). »

###### Activité 2 (p.171)
1- « Dans chacun des cas suivants calculer 3A ; 4B ; 3A − 4B. » i) A = [2 −5 ; 1 0] et B = [−2 −6 ; 7 5/3] ; ii) A = [4 −3 ; 5 1 ; 0 −8] et B = [0 −3 ; 5√2 −1 ; 0 −18] ; iii) A = (1 2 −1) et B = (1 −2 6).
2- « Dans chacun des cas suivants calculer A − 5B. » i) A = (2) et B = (10). ii) A = [2 −2 0 ; 0 3 −3 ; 2 4 −2] et B = [10 −1 0 ; 0 3 −5 ; 2 0 −2].

###### Activité 3 (p.172)
1- « Dans chacun des cas suivants comparer (2/3)A + (2/3)B et (2/3)(A+B) : » i) A = [2 −15 ; 11 10] et B = [−1 −4 ; 0 5/3] ; ii) A = [4 −3 ; 0 1 ; 0 6] et B = [0 −3 ; 5√2 −1 ; 0 −18] ; iii) A = (4;1;2) et B = (1;2;0) (colonnes).
2- « Soient A = (a_ij) et B = (b_ij) deux matrices d'ordre n x p et k un réel quelconque. Comparer k.(A + B) et k.A + k.B. »

**Propriété (encadré)** : « A et B, deux matrices d'ordre n × p (n et p deux entiers naturels non nuls). Pour tout réel k on a : k.(A+B) = kA+kB. »

###### Activité 4 (p.172)
1) « Soit x un réel différent de 1 et −1 et soient A = [6 −2 ; 7 −1] et B = (2(x²−1)/(x+1)) A + (3(x²−1)/(x−1)) A. a) Vérifier que B = (5x+1)A. b) Existe-t-il une valeur de x pour laquelle B = [36 −12 ; 42 −6] ? »
2) « Calculer : C = −2 [1 −2 0 ; 3 7 −1 ; 2 4 −2] + (2/3) [0 4 −3 ; −1 6 −3 ; 2 8 0] − 3 [2 −2 0 ; 0 3 −3 ; 2 4 −2] »
3) « Déterminer le réel x tel que : x [4 1 ; 2 5] + [1 5 ; −2 1] + [1 3 ; 5 0] = [1 31/4 ; 5/2 −1/4] » (second membre lu à l'image ; cohérent avec x = −1/4 sur les quatre coefficients).

###### Activité 5 (p.172)
Situation : « Pour les trois premiers mois de l'année 2008, on donne l'évolution du prix hors taxes (HT) en DT de deux portables A et B par la matrice P » ; colonnes A, B : P = [120 100 ; 100 90 ; 80 70] (lignes = mois : janvier, février, mars, rangés dans l'ordre).
1- Quel est le prix HT du portable B au mois de Mars 2008 ? 2- « La TVA sur ces produits est 19,6%. Que représente la matrice T = 0,196 P. » 3- a) « Vérifier que la matrice représentant les prix TTC est P' = 1,196P. Donner cette matrice. » b) Quel est le prix TTC du portable B au mois de Mars 2008 ?

##### I- 3) Produit de deux matrices (p.173-…)

###### Activité 1 (p.173)
Situation : un fleuriste vend des bouquets de fleurs. « Chaque bouquet se compose de 4 roses, 5 tulipes et 3 branches de marguerite. Une rose coûte 2 DT, une tulipe coûte 1,5 DT et une branche de marguerite coûte 1 DT. » 1) Donner la matrice ligne A = (a1 a2 a3) représentant la composition d'un bouquet et la matrice colonne B = (b1;b2;b3) représentant les prix unitaires respectifs de chaque type de fleurs. 2) Vérifier que le prix p d'un bouquet est : p = a1b1 + a2b2 + a3b3.
Schéma imprimé : A × B = (4 5 3)(2 ; 1,5 ; 1) = 4×2 + 5×1,5 + 3×1 = 18,5. « On dit qu'on a effectué le produit de la matrice ligne A = (4 5 3) par la matrice colonne B = (2 ; 1,5 ; 1). »

**Définition (encadré)** : « A = (a1 a2 … ap) étant une matrice ligne d'ordre p et B = (b1 ; b2 ; … ; bp) une matrice colonne de même ordre p. Le produit des deux matrices A et B, noté A.B, est le réel a1b1+a2b2+.....+apbp. On pose ce produit comme suit : (a1 a2 … ap)(b1;b2;…;bp) = a1b1 + a2b2 … + apbp. »

###### Activité 2 (p.173-174)
1) « Vérifier que (3 5)(2/5 ; −2) = −44/5 et que (1 1 0)(1 ; 2 ; −3) = 3. » (colonne à 2 termes : 2/5 et −2 ; lu à l'image 200 dpi, la couche texte donnait « 2 ; 5 ; −2 » à tort.)
2) Calculer : (2 1 0)(2;2;3) ; (2 11 0)(−2;12;−3) ; (1/3 −4/7)(2;1) ; (0 5)(10;−1).
3) « Déterminer les réels x tels que : (2 x −1)(2 ; x−1 ; 4) = 0. »

###### Activité 3 (p.174)
Situation : concours ; « Dans la matrice A = [07 10 11 ; 10 12 13 ; 11 09 12] sont organisées les notes obtenues, lors d'un concours, par trois élèves e1, e2 et e3 en français, en mathématiques et en économie. (La ligne Ni précise les notes de l'élève ei respectivement en français, en mathématiques et en économie). La matrice C = (2 ; 2.5 ; 4) donne les coefficients respectifs de français, des mathématiques et d'économie. »
1) Donner les matrices lignes N1, N2 et N3 représentant successivement les notes obtenues par les élèves e1, e2 et e3 dans ce concours. 2) a) Pour i ∈ {1,2,3} calculer le réel ti = NiC. b) Que représente la matrice colonne T = (t1;t2;t3) ?
Schéma imprimé : A × C = [7 10 11 ; 10 12 13 ; 11 9 12](2;2.5;4) = (7×2+10×2.5+11×4 ; 10×2+12×2.5+13×4 ; 11×2+9×2.5+12×4) = (83 ; 102 ; 92.5). « On dit qu'on a effectué le produit de la matrice A par la matrice colonne C. »

**Définition (encadré, p.174)** : « A est une matrice d'ordre n×p et B une matrice colonne d'ordre p. Le produit AB de ces deux matrices est la matrice colonne d'ordre n obtenue en appliquant le principe suivant : Le premier coefficient de AB est le produit de la première ligne de A par la matrice colonne B : le deuxième coefficient de AB est le produit de la deuxième ligne de A par la matrice colonne B et ainsi de suite jusqu'au n^ième coefficient du produit A.B. »

###### Activité 4 (p.175)
1) « Vérifier que [2 0 −2 ; 0 −1 1 ; −2 1 −1](1/2 ; 8 ; 4) = (−7 ; −4 ; 3). » (colonne à 3 termes 1/2, 8, 4 ; recalcul : 1−8=−7 ; −8+4=−4 ; −1+8−4=3, cohérent.)
2) « Calculer les produits de matrices suivants : » a. [2 0 ; 0 2](2 ; 3) — b. [2 −3 ; 0 −5](−3 ; 3) — c. [2 4 −2 ; 0 1 1 ; 3 1 −1](4 ; 8 ; 4).
3) « Trouver les réels x et y tels que : [1 −3 ; 4 2](x ; y) = (1 ; 2). »

###### Activité 5 (p.175)
Situation : entreprise qui commercialise 3 produits P1, P2 et P3. « A la fin d'une période de 3 semaines, les quantités vendues par semaines sont données par la matrice Q suivante » (colonnes P1 P2 P3, une ligne par semaine) : Q = [45 120 10 ; 50 90 15 ; 40 98 9]. Prix unitaire hors taxe : P1 = 2 DT, P2 = 1 DT, P3 = 3 DT. Questions : 1- « Ecrire la matrice colonne P des prix unitaires puis déterminer la matrice V des prix de vente hors taxe pour ces trois semaines. » 2- « calculer le montant TTC que l'entreprise a encaissé pour la vente du produit P2 durant la période étudiée avec un taux de TVA de 19,6% sur ces produits. »

###### Activité 6 (p.175)
Situation : inventaire des calculatrices de type A et de type B, en stock dans trois points de ventes d'une grande surface : M = [8 11 ; 17 5 ; 12 1], « les lignes indiquent les stocks de calculatrices disponibles dans chacun des trois points de ventes ». Prix de vente en DT des calculatrices de type A et de type B : matrice à une colonne N = (45 ; 60). Questions : 1) Calculer M × N. 2) Que représentent les nombres obtenus dans la matrice M × N ?

###### Activité 7 (p.176)
Situation : « Dans une entreprise, les services : secrétariat, comptabilité et ateliers ont estimé leurs besoins pour un trimestre en crayons, stylos et surligneurs » :
| | Crayons à papier | Stylos à billes | Surligneurs |
|---|---|---|---|
| secrétariat | 100 | 200 | 500 |
| comptabilité | 200 | 300 | 300 |
| atelier secrétariat [sic] | 100 | 180 | 120 |
« Les prix HT par unité, en DT, proposés par deux fournisseurs F1 et F2 sont les suivantes » :
| | F1 | F2 |
|---|---|---|
| Crayon à papier | 0.25 | 0.28 |
| Stylos à billes | 0.12 | 0.11 |
| Surligneurs | 0.5 | 0.45 |
Questions : 1) « Dans cette question on suppose que chaque service est responsable de sa commande. a) A l'aide du produit de deux matrices convenablement choisies, présenter les dépenses estimées de chacun des services suivant le fournisseur qu'il aura choisi. b) Quel sera le choix le plus économique pour le secrétariat ? pour les ateliers ? » 2) « Dans cette question on suppose que les trois services choisissent le même fournisseur. a) A l'aide d'un produit de deux matrices, présenter sous forme de deux matrices colonnes C1 et C2 les dépenses estimées pour chaque service par l'entreprise suivant le fournisseur choisi. b) Les trois services ont-ils intérêt à faire une commande commune ? Chez quel fournisseur ? »
Schéma imprimé (matrice R) : [100 200 500 ; 200 300 300 ; 100 180 120] × [0,25 0,28 ; 0,12 0,11 ; 0,5 0,45] = [100×0,25+200×0,12+500×0,5 , 100×0,28+200×0,11+500×0,45 ; 200×0,25+300×0,12+300×0,5 , 200×0,28+300×0,11+300×0,45 ; 100×0,25+180×0,12+120×0,5 , 100×0,28+180×0,11+120×0,45] = [299 275 ; 236 224 ; 106,6 101,8]. (Recomptés : 25+24+250=299 ; 28+22+225=275 ; 50+36+150=236 ; 56+33+135=224 ; 25+21,6+60=106,6 ; 28+19,8+54=101,8 — tous exacts.) « On dit qu'on a effectué le produit de la matrice [100 200 500 ; 200 300 300 ; 100 180 120] par la matrice [0,25 0,28 ; 0,12 0,11 ; 0,5 0,45]. »
(Remarque : c'est la phrase d'introduction du schéma (« La matrice R peut être schématisée par ») qui nomme « la matrice R », non la question 1 ; l'énoncé ne l'a pas nommée — incohérence de nommage, voir Notes. [R7 : précision de forme, vérifié à l'image p.176])

**Définition (encadré, p.176)** : « Soit A = (a_ik) une matrice à n lignes et p colonnes et B = (b_kj) une matrice à p lignes et q colonnes. Le produit de la matrice A par la matrice B est la matrice, notée A × B = (c_ij) à n lignes et q colonnes, définies par c_ij = a_i1 b_1j + a_i2 b_2j + … a_ik b_kj + …. a_ip b_pj. »

**Remarques (encadré, p.177)** : « • La multiplication de deux matrices n'est possible que si le nombre de colonnes de la première est égal au nombre de lignes de la deuxième. ● Le produit d'une matrice d'ordre n×p par une matrice p×m est une matrice d'ordre n×m. »

###### Activité 8 (p.177)
1) « Vérifier que [3 2 ; −1 4][−1 5 ; 3 1] = [3 17 ; 13 −1] et que [4√3 8 −1 ; 1 √3 0][1 −2 ; √3 0 ; 0 0] = [12√3 −8√3 ; 4 −2] » (recomptés : 3, 17, 13, −1 exacts ; 4√3+8√3=12√3, −8√3, 1+3=4, −2 exacts.)
2) « Calculer les produits de matrices suivants : » a. [3 2 ; 2/3 4][1 0 ; 3 1] — b. [3 6 2 ; 0 3 1 ; 2 2 −1][1 0 3 ; 1 1 0 ; 1 −1 1] — c. [3 4 5 ; 6 7 4][2 4 3 ; 0 1 1 ; 2 2 −1].
3) « Calculer A² puis A³ pour : A = [1 −1 ; 1 −1] puis pour A = [1 4 0 ; 0 0 1 ; 2 0 −1]. »

###### Activité 9 (p.177)
1- « Calculer A×B, B×A, A×(B×C) et (A×B)×C dans chacun des deux cas suivants : » a) A = [3 2 ; 2/3 4] ; B = [1 0 ; 3 1] et C = [−2 3 ; 5 −1] — b) A = [3 6 2 ; 0 3 1 ; 2 2 −1] ; B = [1 0 3 ; 1 1 0 ; 1 −1 1] et C = [−1 2 3 ; 0 1 4 ; 1 2 −2] — c) « A-t-on A×B = B×A ? »
2- « Soient M et N les matrices suivantes : M = [−√2 1/4 ; 2/7 2√3] ; N = [2/5 −2√3 0 ; 0 1 √11 ; √5 −7 2]. Calculer I2×M, M×I2, I3×N et N×I3. »

**Propriétés (encadré, p.178)** : « ♦ Soient A, B et C trois matrices, tels que les produits ci-dessous sont possibles on a : A×(B×C) = (A×B)×C. ♦ Pour toute matrice carrée M d'ordre 2 on a : I2×M = M×I2 = M. ♦ Pour toute matrice carrée N d'ordre 3 on a : I3×N = N×I3 = N. »

###### Activité 10 (p.178)
Situation : « Dans une chaîne de restauration rapide, on sert chaque jour : 800 hamburgers, 600 cheeseburgers et 1000 cafés. Les prix unitaires PU de revient et des bénéfices unitaires BU sont donnés, en DT, par le tableau » :
| | hamburger | cheeseburger | café |
|---|---|---|---|
| PU de revient | 0,8 | 0,6 | 0,4 |
| BU | 1 | 1 | 0,7 |
Questions : 1) « Ecrire les quantités des produits vendus dans une matrice ligne Q, les PU de revient dans une matrice colonne R, les bénéfices unitaires BU dans une matrice colonne B. » 2) a- Calculer le coût total à l'aide d'un produit d'une matrice ligne par une matrice colonne. b- Même question pour les bénéfices totaux. c- En déduire le prix de vente total. 3) a- Ecrire les prix de vente unitaires dans une matrice colonne notée V. b- Retrouver le résultat de la question 2)-c. 4) a- Exprimer V en fonction de B et R. b- Comparer alors Q×R + Q×B et Q×(R+B). (Les lettres Q et R sont imprimées en petit symbole dans l'énoncé, lues à l'image.)

**Propriété (encadré, p.178)** : « Soient A, B et C trois matrices, tels que les produits et les sommes ci-dessous sont possibles on a : A×(B+C) = A×B + A×C ».

###### Activité 11 (p.178)
Soient A = [1 0 3 ; 1 1 0 ; 1 −1 1] et B = [1 0 3 ; 0 5 0 ; 1 2 1]. 1) Calculer A×B puis B×A. 2) a) Calculer A×B + B ; c) En déduire A²×B + A×B. (La sous-question « b) » n'existe pas : numérotation a) puis c) telle qu'imprimée.)

##### II- Déterminant d'une matrice carrée d'ordre 2 ou 3 (p.179-181)

###### Activité 1 (p.179)
1) « M = [4 −1 ; 3 5/2] est une matrice carrée d'ordre 2. Le réel 4 × 5/2 − 3 × (−1) s'appelle le **déterminant de la matrice M**. On le note |4 −1 ; 3 5/2| et on écrit **dét (M)** = |4 −1 ; 3 5/2| = 4 × 5/2 − 3 × (−1). » « On donne les matrices A = [2 1 ; −1 3] ; B = [0 −2 ; −1 3] et C = [0 −2 ; 2 1]. Calculer dét (A) ; dét (B) et dét (C). »
2) « N = [1 0 −2 ; 3 2 1 ; −4 −1 3] est une la matrice carrée d'ordre 3. On désigne par Δ_ij le déterminant de la matrice carrée d'ordre 2 obtenue à partir de la matrice N en supprimant la i-ème ligne et la j-ème colonne. Exemple : Δ_21 = |0 −2 ; −1 3|. a) Donner Δ_11 et Δ_31 sans les calculer. Le réel +1.Δ_11 − 3.Δ_21 + (−4).Δ_31 (1, 3 et (−4) sont les coefficient qui forment la première colonne de la matrice N) est **le déterminant de la matrice N**. On le note |1 0 −2 ; 3 2 1 ; −4 −1 3| et on écrit dét (N) = |1 0 −2 ; 3 2 1 ; −4 −1 3| = +1.|2 1 ; −1 3| − 3.|0 −2 ; −1 3| + (−4).|0 −2 ; 2 1|. »
b) « On donne la matrice D = [−4 1 0 ; 0 3 −1 ; 1 7 −2]. Vérifier que dét (D) = −5. »
(Note : 4×5/2 − 3×(−1) = 13 ; l'exemple d'ordre 3 développe par la PREMIÈRE COLONNE avec les signes + − +.)

**Définition (encadré, p.180)** : « Soit M = [a b ; c d] une matrice carrée d'ordre 2. Le déterminant de M est le réel, noté dét (M), défini par : dét (M) = |a b ; c d| = ad − bc. Soit N = [a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3] une matrice carrée d'ordre 3. Le déterminant de N est le réel défini par : dét (N) = |a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3| = a1 |b2 b3 ; c2 c3| − b1 |a2 a3 ; c2 c3| + c1 |a2 a3 ; b2 b3| » (développement par rapport à la première colonne.)
**Conséquence (encadré)** : « dét(I2) = 1 et dét(I3) = 1 ».

###### Activité 2 (p.180)
« Calculer les déterminants des matrices suivantes : A = [2 2 ; 5 1] ; B = [1 0 ; 5 1] ; C = [1 0 ; 2 2] ; D = [−4 1 0 ; −1 2 2 ; 3 5 1] ; E = [1 −1 2 ; −2 3 −4 ; −3 2 1] et F = [2 −3 −4 ; 0 −1 5 ; 0 0 3] »

###### Activité 3 (p.180)
Soit N = [a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3] d'ordre 3. « Vérifier que dét(N) = a1 |b2 b3 ; c2 c3| − a2 |b1 b3 ; c1 c3| + a3 |b1 b2 ; c1 c2|. »
**Encadré (propriété, p.180)** : « Soit N = [a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3] une matrice carrée d'ordre 3. Le déterminant de N peut être calculé en développant par rapport à la première ligne et on obtient : dét(N) = a1 |b2 b3 ; c2 c3| − a2 |b1 b3 ; c1 c3| + a3 |b1 b2 ; c1 c2|. »

###### Activité 4 (p.181)
« Calculer les déterminants des matrices suivantes : » A = [0 2 0 ; −1 2 2 ; 3 2 1] ; B = [0 −1 2 ; −2 3 −4 ; 0 2 1] ; C = [2 0 −4 ; 2 −1 5 ; 1 0 3] ; D = [2 2 −4 ; 2 2 5 ; 1 1 3].

##### III- Inverse d'une matrice carrée d'ordre 2 ou 3 (p.181-…)

###### Activité 1 (p.181)
« On donne A = [2 1 ; 4 3] et B = [1 2 3 ; 1 0 2 ; 2 −1 1]. »
1) a) « Déterminer x et y pour que A' = [3/2 y ; x 1] vérifie A×A' = I2. » b) « Pour les valeurs de x et y trouvées, vérifier que A'×A = I2. »
2) a) « Déterminer les réels a, b et c pour que B' = (1/5)[a −5 4 ; 3 b 1 ; −1 5 c] vérifie B×B' = I3. » b) « Pour les valeurs de a, b et c trouvées, vérifier que B'×B = I3. »
« On dit que A est **inversible** et que A' est **la matrice inverse** de A ou que A' est **l'inverse** de A. De même pour la matrice B elle est inversible et son inverse est B'. »
(Vérification du lecteur : x = −2, y = −1/2 ; non écrit par le manuel.)

**Définition (encadré)** : « Soit M = (a_ij) une matrice carrée d'ordre n. On dit que M est inversible si et seulement s'il existe une matrice M' de même ordre n vérifiant : M × M' = M' × M = I_n, où I_n est la matrice unité. M' est appelée dans ce cas l'inverse de M, noté M^{−1}. »
**Remarques (encadré)** : « On admet que : ◆ Si une matrice carrée est inversible alors sa matrice inverse est unique. ◆ Si M est une matrice carrée d'ordre n et s'il existe une matrice carrée M' d'ordre n vérifiant M×M' = I_n **ou** M'×M = I_n alors M est inversible et son inverse est la matrice M'. »

###### Activité 2 (p.182)
1) « Soit A = [2 2 ; 3 5]. Vérifier que A^{−1} = [5/4 −2/4 ; −3/4 2/4]. » (dét A = 4 ; recomptage coefficient par coefficient : exact.)
2) « Soit B = [−4 −4 2 ; 3 0 1 ; 2 1 0]. Vérifier que B^{−1} = [−1/2 1 −2 ; 1 −2 5 ; 3/2 −2 6]. » (vérification partielle ligne 1 × colonnes 1 et 2 : exacte.)

###### Activité 3 (p.182)
1- « Soit la matrice A = [−1/2 √3/2 ; √3/2 1/2]. a) Vérifier que A² = I2. b) A est-elle inversible ? si oui déterminer son inverse. »
2- « Soit la matrice B = [−1 −1 ; 2 3]. a) Montre que B² − 2B − I2 = **O**. b) En déduire que B est inversible et déterminer son inverse. »

**Théorème (admis) (encadré)** : « Soit M une matrice carrée d'ordre 2 ou 3. M est inversible si et seulement si, dét (M) ≠ 0. »

###### Activité 4 (p.182)
1- « Soit la matrice A = [1 1 ; 3 5]. a) Calculer dét (A) et en déduire que A est inversible. b) Vérifier que la matrice A' = (1/dét(A)) [5 −1 ; −3 1] est la matrice inverse de A. »
2- « On donne la matrice B = [3 2 ; −2 1]. En utilisant le même procédé qu'en 1), montrer que B est inversible et déterminer son inverse. »
3- « Soit M = [a c ; b d] une matrice carrée d'ordre 2. On suppose que dét (M) ≠ 0, montrer que la matrice M' = (1/dét(M)) [d −c ; −b a] est la matrice inverse de M. »

**Encadré (p.183, formule de l'inverse d'ordre 2)** : « Soit M = [a c ; b d] une matrice carrée d'ordre 2 telle que dét(M) ≠ 0. L'inverse de M est la matrice M^{−1} = (1/dét(M)) [d −c ; −b a] »

###### Activité 5 (p.183)
« Soient a ∈ IR, A = [−a 0 0 ; 0 a 1 ; 0 −1 a] et B = [−2 −1 0 ; −1 0 1 ; 0 1 2]. 1) Donner la condition sur a pour que A soit inversible. 2) Trouver les réels a pour lesquels la matrice B − a I3 n'est pas inversible. »

###### Activité 6 (p.183)
« Soit A = [1 3 −3 ; 0 3 0 ; 1 4 −2]. 1- Vérifier que A est inversible. 2- Pour i et j des entiers variant de 1 à 3, on désigne par A_ij la matrice obtenue à partir de A en supprimant la i^ième ligne et la j^ième colonne et par Δ_ij = (−1)^{i+j} dét(A_ij). Par exemple : A_11 = [3 0 ; 4 −2] et Δ_11 = (−1)² |3 0 ; 4 −2| = −6 ; A_22 [sic, voir Notes] = [0 0 ; 1 −2] et Δ_12 = (−1)³ |0 0 ; 1 −2| = 0. 3- Soit B = (Δ_ij), i=1,2,3 j=1,2,3. compléter : B = [−6 0 .. ; .. .. .. ; 9 .. 3]. 4- a- Donner la matrice C obtenue en échangeant les lignes et les colonnes de B. b- Donner la matrice D = (1/det A) × C. Vérifier que A^{−1} = D. »
**Encadré (p.183)** : « Les étapes de l'activité précédente constituent un algorithme permettant de calculer l'inverse d'une matrice carrée d'ordre 3 à déterminant non nul. »

###### Activité 7 (p.184)
« Déterminer les inverses des matrices A = [−1 1 0 ; 4 1 2 ; −1 0 3] et B = [1 1 1 ; 3 5 2 ; 3 2 5] »

##### IV- Résolution des systèmes linéaires de premier degré à deux ou trois inconnues (p.184-188)

###### 1) Revoir (p.184)
**Activité 1** : « En utilisant la méthode du pivot de Gauss, résoudre dans IR³ les systèmes suivants » (S1) x + y + 3z = 10 ; 2x − y + z = −3 ; 3x + 2y − 5z = 33 — (S2) x + y = 5 ; y + z = 1 ; 2x + 3y + z = 4 — (S3) : x − y = y − z = z − x = 1.
**Activité 2** : « Résoudre dans IR³ les systèmes suivants » a) x − y + z = 1 ; x + 2y + 3 = 3y − z + 4 — b) 3x + 2y − z = −2 ; x + 2y + 3z = 4 — c) x − 2y = 0 ; x − y + 5t = 9 — d) x − 2y + z = 3x + z = 2y − z + 2. (Tel qu'imprimé : le c) contient une inconnue t dans un « IR³ » ; voir Notes.)
**Activité 3** — Situation : un magasin vend deux produits concurrents : un mélange de céréales courant et le même mélange en produit bio. « Le produit bio est 40% plus cher, mais le magasin fait une réduction de 0,1DT pour l'achat d'un paquet. (des deux types de produits) Le produit courant est proposé en paquet de 200g, alors que le produit bio est en paquet de 150g. On achète trois paquets de produit courant et deux paquets de produits bio pour un total de 2,7DT. » 1) Calculer le prix de chaque paquet. 2) Calculer le prix au kilogramme en tenant compte de la réduction. (Aucun corrigé dans le manuel.)
**Activité 4** : « Résoudre dans IR² les systèmes suivants » (S1) x + y = 10 ; 2x − y = −1 ; 3x + 2y = 23 — (S2) x + 3y = 15 ; 2x − y = −3 ; 3x + 2y = 33 — (S3) x − 3y = 1 ; 2x − 6y = 2 ; 3x − 9y = 3.

###### 2) Résolution d'un système en utilisant l'inverse d'une matrice (p.185-…)
**Activité 1 (p.185)** : « Le système (S) −5x + 3y = 2 ; −x + y = 5 peut être représenté sous la forme A×X = B avec A = [−5 3 ; −1 1] ; X = (x ; y) et B = (2 ; 5). » Vocabulaire imprimé : « ◆ A est dite **la matrice du système**. ◆ l'égalité A×X=B est dite **l'écriture matricielle** du système. ◆ La matrice colonne B est dite **la matrice des constantes**. » Question : « 1- Donner l'écriture matricielle de chacun des deux systèmes suivants : a) 2,23x − 5,5y = 12 ; 0,2x + y = 7 — b) 3x − y + 2z = 7 ; 5x + y − z = 8 ; −x + 3y + 7z = −22 ». « Lorsque A est une matrice carrée le système est dit **système carré**. »

**Activité 2 (p.185)** — Situation : « Une petite entreprise artisanale s'est spécialisée dans la fabrication de deux jeux en bois : des toupies et des bilboquets. La fabrication, à l'aide d'un tour à bois, demande 2 minutes pour une toupie et 7 minutes pour un bilboquet. La vente d'une toupie rapporte un bénéfice de 0,5 DT et celle d'un bilboquet 2DT. Cette entreprise désire obtenir un bénéfice de 80 DT en utilisant le tour à bois durant 5h. On désigne par x : le nombre des toupies et y bilboquets à fabriquer. »
1- « Montrer que le couple (x, y) vérifie le système (S) 2x + 7y = 300 ; (1/2)x + 2y = 80 » 2- Résoudre le système (S) et écrire la solution sous la forme d'une matrice colonne qu'on note C. 3- a) Déterminer la matrice A du système (S) et la matrice B des constantes. b) En déduire l'écriture matricielle de ce système. 4- Déterminer A^{−1} puis A^{−1}×B. 5- Comparer A^{−1}×B et C.
(Raisonnement implicite : 5 h = 300 min.)

**Activité 3 (p.185-186)** — Situation : « En Janvier 2007, Ahmed achète des actions de trois sociétés : X (5 DT l'action), Y (4 DT l'action) et Z (10 DT l'action). Au total il achète 10 actions pour un montant de 63 DT. En juillet 2007, par rapport à janvier 2007, l'action X a doublé, l'action Y a augmenté de 25% et l'action Z a chuté de 40%. Le portefeuille d'année [sic] vaut alors en juillet 78 DT. On désigne par x, y et z les nombres d'actions d'Ahmed respectivement des sociétés X, Y et Z. »
1- « Montrer que le triplet (x, y, z) vérifie le système : (S) x + y + z = 10 ; 5x + 4y + 10z = 63 ; 10x + 5y + 6z = 78 » 2- Résoudre le système (S) et écrire la solution sous la forme d'une matrice colonne qu'on note C. 3- a) Déterminer la matrice A du système (S) et la matrice B des constantes. b) En déduire l'écriture matricielle de ce système. 4- « Vérifier que A^{−1} = (1/29) × [−26 −1 6 ; 70 −4 −5 ; −15 5 −1] puis calculer A^{−1}×B. » 5- Comparer A^{−1}×B et C.
(Vérifs du lecteur : dét A = 29 ; 5×2=10, 4×1,25=5, 10×0,6=6 donc 10x+5y+6z=78, cohérent avec le système imprimé.)

**Théorème (encadré, p.186)** : « Soit A une matrice carrée d'ordre 2 ou 3 telle que dét(A) ≠ 0. tout système, d'écriture matricielle : A×X = B, a une solution et une seule et l'on a X = A^{−1}×B, où A^{−1} est l'inverse de A. »
**Remarque (encadré, p.186)** : « Si A est une matrice carrée non inversible alors le système A×X = B n'a pas de solution ou a une infinité de solutions »

**Activité 4 (p.186)** : « Pour chacun des deux systèmes suivants a) Donner l'écriture matricielle du système. b) Déterminer l'inverse de la matrice du système. c) En déduire la solution de chacun des systèmes » : 3x − 10y = 4 ; −2x + 8y = 7 — et — 2√3 x − 2y = −1 ; 4x − √3 y = 4.
**Activité 5 (p.186-187)** : « Soit la matrice M = [1 −1 0 ; 2 1 1 ; −1 0 1]. 1) Vérifier que M^{−1} = (1/4) [1 1 −1 ; −3 1 −1 ; 1 1 3]. 2) Résoudre alors les deux systèmes (S) et (S') suivants : (S) x − y = 10 ; 2x + y + z = 2 ; −x + z = 3 et (S') x − y = 0 ; 2x + y + z = −1 ; −x + z = 3. » (dét M = 4, cohérent avec le facteur 1/4.)
**Activité 6 (p.187)** : « Considérons le système (S) x + y + z = 3 ; 2x + y − z = 10 ; 3x + 2y − z = 3. 1) Montrer que le système (S) est équivalent au système (S') z = 3 − x − y ; 3x + 2y = 13 ; 4x + 3y = 11. 2) Soit la matrice A = [3 2 ; 4 3]. a) Donner la matrice inverse A^{−1}, puis résoudre le système (S'') 3x + 2y = 13 ; 4x + 3y = 11. b) En déduire la solution du système (S). »
**Activité 7 (p.187)** : « Soit la matrice A = [3 −10 −1 ; −2 8 2 ; 2 −4 −2]. 1) donner la matrice inverse A^{−1} (mettre les coefficients sous forme fractionnaire) 2) En déduire la solution du système (S) 3x − 10y − z = 4 ; −2x + 8y + 2z = 7 ; 2x − 4y − 2z = 5 »
**Activité 8 (p.187-188)** — Situation : « Une entreprise de confection de vêtements fabrique des jupes, des robes et pantalons. Pour fabriquer une jupe, il faut 0,75 m de tissu, 4 boutons et une fermeture ; la confection d'une robe nécessite 1,50 m de tissu, 6 boutons et une fermeture ; pour confectionner un pantalon, on utilise 1,25 m de tissu, 2 boutons et une fermeture. On appelle x, y et z les quantités respectives de jupes, de robes et de pantalons confectionnés et a, b et c les quantités de tissus (en mètres), de boutons et de fermetures utilisés pour leur fabrication. On appelle M = [0,75 1,50 1,25 ; 4 6 2 ; 1 1 1], A = (x ; y ; z) et B = (a ; b ; c). »
1) a) Vérifier que B = M × A. b) Déterminer a, b et c pour la fabrication de 200 jupes, 120 robes et 320 pantalons. 2) « On considère la matrice M' = [−1,6 0,1 1,8 ; 0,8 0,2 −1,4 ; 0,8 −0,3 0,6]. a) Calculer M'×M. b) Ecrire la matrice A en fonction de B et de M'. c) En déduire x, y et z quand on a utilisé 735 mètres de tissu, 2400 boutons et 620 fermetures. » (Recomptage lecteur : ligne 1 de M' × colonnes de M donne 1, 0, 0 ; M' est bien l'inverse de M.)

#### AVEC L'ORDINATEUR (p.189-190)
(Bandeau « Avec l'ordinateur » en p.189 ; la p.190 porte le bandeau « Exercices et problèmes » alors que son contenu — Activités 3 et 4 — prolonge « Avec l'ordinateur » : voir Notes.)

##### Activité 1 (p.189)
« On donne les matrices A = [2 3 0 ; 5 1 −1 ; −1 −3 7] et B = [2 9 ; −7 4 ; 1 0]. On se propose de calculer le produit A×B à l'aide d'Excel : »
1) Dans les cellules de A1 à C3, entrer les coefficients de la matrice A [« À » imprimé] et dans les cellules de E1 à F3, entrer les coefficients de B.
2) « AB étant une matrice d'ordre 3×2, sélectionner donc sa place, à titre d'exemple les cellules de B6 à C8. »
3) « Dans la barre des formules écrire la formule ci-contre : **{=PRODUITMAT(A1:C3;E1:F3)}**. Valider en appuyant en même temps sur les touches de clavier ci-dessous : Ctrl ⇧ (Maj) Entrée. Des accolades apparaissent alors autour de la formule. » « La matrice obtenue est A×B. »
Capture imprimée : A1:C3 = [2 3 0 ; 5 1 −1 ; −1 −3 7] ; E1:F3 = [2 9 ; −7 4 ; 1 0] ; résultat B6:C8 = [−17 30 ; 2 49 ; 26 −21]. (Recomptés : −17, 30, 2, 49, 26, −21 — exacts.)

##### Activité 2 (p.189)
« On donne les matrices A' = [1 −2 8 ; 1/2 2 2 ; 1 2 −1] et B' = [6 7 2 ; 2 0 −5 ; −1 3 4]. Vérifier que A'×B' = [−6 31 44 ; 5 19/2 −1 ; 11 4 −12]. » (Recomptés : tous les coefficients exacts.)

##### Activité 3 (p.190)
« On donne la matrice C = [1 2 3 ; 1 0 2 ; 2 −1 1]. Il est facile de vérifier que C est inversible on se propose de déterminer A^{−1} [sic : C^{−1}] à l'aide d'Excel. » 1) Dans les cellules de A1 à C3, entrer les coefficients de la matrice C. 2) Sélectionner la place de C^{−1}, à titre d'exemple les cellules de E1 à G3. 3) Formule : **{=INVERSEMAT(A1:C3)}**, valider par Ctrl ⇧ Entrée. 4) « Aller dans la barre de menu et choisir Format puis aller à l'onglet : » (capture « Format de cellule »). 5) « Choisir le mot fraction (de deux ou de trois chiffres selon la valeur de dét (A)). » « La matrice obtenue est A^{−1}. » [sic]
Capture imprimée : E1:G3 = [2/5 −1 4/5 ; 3/5 −1 1/5 ; −1/5 1 −2/5]. (dét C = 5, cohérent.)

##### Activité 4 (p.190)
« On donne la matrice D = [2 −5 6 ; 0 4 7 ; −3 1 0]. Vérifier que la matrice D est inversible et que D^{−1} = [1/14 −26/73 7/24 ; −2/63 19/71 −5/36 ; 5/91 −23/97 4/29]. » ⚠ Voir Notes : dét D = 163 (calcul du lecteur) et la matrice proposée est incohérente.

#### EXERCICES ET PROBLÈMES (p.191-…)

##### 1- (p.191) QCM — « Une seule des réponses proposées est exacte » (colonnes a, b, C)
- **Q1.** A = [−1 5 0 ; 1 −2 1/2]. L'ordre de A est : a) 2×3 — b) 3×2 — C) 3×3.
- **Q2.** Pour la matrice A ci-dessus, a21 est égale à : a) 5 — b) −2 — C) 1.
- **Q3.** A = (5 ; 0 ; −1) et B = (−1/2 ; 0 ; −2) (colonnes). A+B est égale à : a) [5 −1/2 ; 0 0 ; −1 −2] — b) (9/2 ; 0 ; −3) colonne — C) (9/2  0  −3) ligne.
- **Q4.** A = [2√2 9 ; −7 4 ; 1 0] ; B = [√2 3 ; 0 −4 ; −1 5] et C = [0 3 ; −7 12 ; 3 −10]. Donc C est égale à : a) 2A+B — b) A+2B — C) A−2B.
- **Q5.** A = [−1 3 −2 ; 3 2 1/2] ; B = [2√2 9 ; −7 4 ; 1 0] et C = A×B. Donc c11 est égale à : a) −2√2 — b) −2√2+27 — C) −2√2−23.
- **Q7.** A = [a −1 ; 1 a] ; a ∈ ℝ. a) Pour tout réel a, A est inversible — b) A est inversible si et seulement si a ∈ ℝ \ {−1,1} — C) Pour tout réel a on a : A est non inversible. (La numérotation saute de Q5 à Q7 : pas de Q6 imprimée.)
- **Q8.** A = [1 3 0 ; 0 −1 1 ; −1 3 7]. a) A est non inversible — b) A^{−1} = [1 1/3 0 ; 0 −1 1 ; −1 1/3 1/7] — C) A^{−1} = [−5/29 8/29 1/29 ; 13/29 −16/87 −2/87 ; −12/29 17/87 13/87]. (Voir Notes : dét A = −13 au calcul du lecteur.)
(Les bonnes réponses ne sont pas dans le manuel.)

##### 2- (p.191)
« Soit A = [1/3 √3 ; −2 −1 ; −1 12]. 1) Donner l'ordre de A. 2) Préciser les valeurs des coefficients a31, a22 et a32 de la matrice A. »

##### 3- (p.192)
« Dans une menuiserie on utilise des matières première M1, M2 et M3 pour fabriquer trois types de chaises C1, C2 et C3. Le coefficient a_ij de la matrice A ci-dessous représente le coût HT en DT, de matière première M_i nécessaire pour une chaise C_j. A = [23 20 18 ; 20 17 15 ; 19 18 14]. 1) Donner le coût en matière première M3 d'une chaise de type C2 ? en matière première M2 d'une chaise de type C3 ? 2) Que représente le coefficient inscrit à l'intersection de la troisième ligne et de la première colonne de A ? » (symboles M_i et C_j lus à l'image : imprimés comme petits pictogrammes.)

##### 4- (p.192)
« Calculer, si c'est possible, les sommes suivantes. Lorsque c'est impossible, expliquer pourquoi ? » a) (1 ; 0,1) + (−2 ; 0,3) — b) [0,8 −1 ; −0,1 0] + (3 ; 0,2) — c) (1 3) + (3 −2) — d) (0,2 0,7) + [3 0,4 ; 2 0,6] — e) [0,3 10 ; −0,1 2] + [1 2 0,4 ; 2 3 −5] — f) [0,3 10 1 ; −0,1 2 −1] + [1 2 0,4 ; 2 3 −5].

##### 5- (p.192)
« Soit I3 la matrice unité d'ordre 3. Calculer : A − I3 ; A − 2I3 et A − (2/3) I3 dans chacun des cas suivants : » a) A = [2 1 1 ; 5 0 −1 ; 8 1 7] ; b) A = [2 0 0 ; 0 1 0 ; 0 0 −7] ; c) A = [2 0 0 ; 15 10 0 ; 1 11 3].

##### 6- (p.192)
« Calculer A−B ; (A−B)−C ; A−(B−C). » a) A = [2 −4 ; 7 −2 ; 1 2] ; B = [−2 9 ; 0 4 ; 1 0] et C = [1 1 ; 1 1 ; 1 1]. b) A = (1 2 3) ; B = (0 1 0) et C = (0 0 0).

##### 7- (p.192-193)
« Dans chacun des cas suivant calculer 3A, (2/3)B et 3A − (2/3)B. » a) A = [3 5 ; −2 2] et B = [0 9/4 ; −1 6] (matrices 2×2). b) A = [1 √3 1 ; −2 2 −1] et B = [0 2√3/2 15 ; 1/3 3 0].

##### 8- (p.193)
« On donne A = [1 0 −2x ; x 1 0 ; 0 0 1] et B = A + xA + x²A + x³A avec x un réel différent de 1. a) Vérifier que B = ((x⁴−1)/(x−1)) A. b) Calculer B pour x = 2. c) Trouver la valeur de x pour la quelle B = I3. »

##### 9- (p.193)
« Un gestionnaire de distributeurs automatiques de boissons a noté l'état des stocks en début de journée dans 3 distributeurs d1, d2 et d3 pour les boissons de type b1, les boissons de type b2 et les boissons de type b3. Le coefficient a_ij de la matrice A ci-dessous représente le nombre des boissons de type b_j dans le distributeur d_i : A = [20 15 10 ; 15 10 8 ; 18 11 7]. Les entrées des stocks de la journée et l'état des stocks en fin de journée sont données respectivement par les matrices B et C ci-dessous : B = [12 12 10 ; 12 12 10 ; 12 12 10] et C = [23 19 15 ; 20 12 12 ; 22 8 6]. 1) Donner la matrice des ventes de la journée 2) Quelle est la vente la plus importante ? »

##### 10- (p.193)
« Une usine fabrique trois types de bicyclettes dans deux ateliers. le tableau ci-dessous donne le nombre de chaque type produit dans chacun des ateliers A et B au mois d'Avril. »
| | type 1 | type 2 | type 3 |
|---|---|---|---|
| Atelier A | 150 | 120 | 100 |
| Atelier B | 180 | 90 | 130 |
1- Ecrire une matrice A d'ordre 2×3 représentant les informations fournies par le tableau ci-dessus. 2- « Le constructeur a augmenté la production de l'usine 20% au mois de Mai par rapport à celle d'Avril. Donner une matrice M représentant la production de l'usine au mois de Mai. » 3- Que représente la matrice A+M ? 4- « Reprendre la deuxième et la troisième question en supposant que la production de l'usine diminue 10% au moi [sic] de Mai par rapport à celle d'Avril. »

##### 11- (p.194)
« Calculer A×B dans chacun des cas suivant : » a) A = (−1 3) et B = (3 ; 2) — b) A = (5/3 1 5) et B = (2 ; −3 ; −2/3) — c) A = [−3 0 ; 5 4] et B = (5 ; 1) — d) A = [1 −4 ; √2 0 ; 1 2] et B = [1 −2 ; −2 9] — e) A = [−2 1/3 −5 ; 0 0 −1 ; 2 1 0] et B = [−2 1 1 ; 3 2 −2 ; −1 1 3].

##### 12- (p.194)
« Youssef étudie les prix des pains au chocolat et des croissants dans trois boulangeries. Il constate que les prix des pains au chocolat sont supérieurs ou égaux à ceux des croissants. Les prix en DT, sont donnés par la matrice : A = [0,85 0,78 0,85 ; 0,8 0,78 0,83]. Il achète x pains au chocolat et y croissants de l'une des trois boulangeries. On note X = (x ; y) la matrice des quantités achetées. 1) A l'aide d'un calcul matriciel, déterminer en fonction de x et y la dépense de Youssef dans chacune des boulangeries. 2) Youssef doit acheter 2 pains et 1 croissant de l'une des trois boulangeries. Comparer les prix payés par Youssef suivant la boulangerie qu'il choisit. » (Lignes de A : pains au chocolat puis croissants — lu d'après l'énoncé ; le manuel ne l'étiquette pas.)

##### 13- (p.194)
« Les résultats à un examen de trois élèves 1, 2 et 3 sont donnés par la matrice A, où la i^ème ligne donne les notes sur 20 de l'élève i en Economie, maths, et gestion. La matrice B donne trois simulations possibles des trois coefficients de ces matières. A = [11 10 9 ; 10 11 7 ; 8 16 5] et B = [7 5 4 ; 4 4 7 ; 4 5 4]. 1) Effectuer le produit A×B. 2) Pour chacun des trois élèves quel choix de coefficients qui lui conviendra le mieux ? »

##### 14- (p.194-…)
« Un catalogue de vente par correspondance propose des lots de linge de maison. La parure « enfants » contient une taie, un drap housse et une housse de couette. La parure « toucher soyeux » contient deux taies, un drap housse et une housse de couette. La parure « prix minis » contient deux taies, deux draps housse et une housse de couette. 1) Présenter toutes ces données dans une matrice. 2) a- On note x, y et z le nombre de parures de chaque sorte, vendues par jour. Exprimer les nombres de taies, de draps et de housses de couette vendus à l'aide de x, y et z. b- Le prix d'une parure « enfants » est 70DT celui d'une parure « toucher soyeux » est 99 DT et celui d'une parure « prix minis » est 42 DT. » (suite p.195)

(suite 14, p.195) « …Traduire ces informations par une matrice colonne. c- La recette totale de la journée pour ces trois lots est 4869DT Traduire ce résultat par une relation entre x, y et z. »

##### 15- (p.195)
« Le nombre d'entrées, la même semaine, dans trois cinémas C1, C2 et C3 qui présentent les mêmes films : F1, F2 et F3 est donné par la matrice A ci-dessous. Le coefficient a_ij de la matrice A représente le nombre des entrées au film Fj dans le cinéma Ci. A = [120 250 110 ; 280 300 100 ; 350 240 160]. 1) a- Quel est l'ordre de cette matrice A ? b- Donner les valeurs des coefficients a13 et a32 de la matrice A. c- Quel est le nombre d'entrées pour le film F1 dans le cinéma C2 ? 2) La semaine suivante, tous les cinémas ont vu une augmentation de 20% du nombre d'entrées pour chacun des films. Donner la matrice B des entées [sic] en deuxième semaine. 3) La troisième semaine, le nombre d'entées [sic] pour le film F3 a chuté de 60% par rapport à la première semaine, et celui pour film F2 a augmenté de 40%. Pour F1, le nombre d'entrées est resté celui de la deuxième semaine. a) Donner la matrice C des entrées en troisième semaine. b) Calculer la matrice du total des entrées sur les trois semaines. c) Donner le nombre total d'entrées pour le film F3 dans le cinéma C2. »

##### 16- (p.195)
« Calculer A² et A³ dans chacun des cas suivants : » a) A = [√2 1 ; −1 √2] — b) A = [11 10 9 ; 10 11 7 ; 8 16 5] — c) A = [2 1 1 ; 1 2 1 ; 1 1 2].

##### 17- (p.195)
« Soient T = [0 1 0 ; 0 0 1 ; 0 0 0] et A = [1 1 0 ; 0 1 1 ; 0 0 1]. 1) Vérifier que A = T + I. 2) Calculer T² puis T³ en déduire T⁵ puis A⁵. »

##### 18- (p.195)
« Les matrices suivantes sont-elles inversibles ? » A = [√2 1 ; −1 2] ; B = [1 a ; −a 1] (a ∈ ℝ) ; C = [2 0 1 ; 1 2 0 ; 1 −2 2] ; D = [2 1 2 ; 1 2 1 ; 1 1 1]. (Énoncé imprimé : « son-elles » [sic].)

##### 19- (p.196)
« Donner la matrice inverse, si elle existe, de chacune des matrices suivantes. » A = [1 5 ; −3 1] ; B = [0 0 ; 4 1] ; C = [√3 √2 ; −√2 2√3].

##### 20- (p.196)
« Soit A = [1 1 0 ; −1 0 0 ; 2 0 −1]. Calculer A³ puis en déduire A^{−1}. »

##### 21- (p.196)
« Donner l'écriture matricielle de chacun des systèmes suivants. (la résolution n'est pas demandée). » a) 3x − y + 2z = 7 ; 5x + y − z = 8 ; −x + 3y + 7z = −22 — b) 3x − z = 15 ; x + 7z = 12 ; x + y = 25 — c) x + y + z = −5 ; −y + z = 2 — d) 3x + 6y = x + z + 31 ; 7y + 2z = x − y + 27.

##### 22- (p.196)
« Un hôtel compte 160 chambres, certaines chambres à un lit et les autres à deux lits. Le prix d'une chambre à un lit est de 45 DT et celui d'une chambre à deux lits est de 60DT. En raison d'un tournoi de Golf, toutes les chambres sont occupées. Le total des ventes pour la nuit est de 8700DT. On désigne par x et y respectivement les nombres de chambres à un lit et à deux lits de l'hôtel. 1) Traduire les informations ci-dessus en un système de deux équations à deux inconnues x, et y. 2) Combien de chambres à un lit et combien de chambres à deux lits l'hôtel compte-t-il ? »

##### 23- (p.196)
« Soit la matrice A = [2 3 ; −3 1]. 1) Vérifier que A est inversible et donner sa matrice inverse A^{−1}. 2) En déduire la résolution des systèmes suivants : 2x + 3y = −1 ; −3x + y = 2. 3) Résoudre à l'aide d'un calcul matriciel le système suivant : 3x − y = 0 ; 2x + 4y = 5. » (Énoncé imprimé tel quel : le système du 3) a pour matrice [3 −1 ; 2 4], différente de A ; voir Notes.)

##### 24- (p.196)
« On considère la matrice : A = [2 −1 3 ; −3 1 −1 ; 1 1 1]. 1) Calculer A² puis B = 4A − A² et le produit A×B. En déduire A^{−1}. 2) Résoudre par un calcul matriciel, le système d'équations suivant : 2x − y + 3z = −1 ; −3x + y − z = 5 ; x + y + z = −1 »

##### 25- (p.197)
« On donne A = [3 10 1 ; 2 8 2 ; 2 −4 −2]. 1) Donner la matrice inverse A^{−1} (coefficients sous forme fractionnaire). 2) En déduire la résolution du système suivant : 3x + 10y + z = 10 ; 2x + 8y + 2z = 7 ; 2x − 4y − 2z = 8 » (Comparer avec « Avec le cours » p.187 Act. 7 : matrice [3 −10 −1 ; −2 8 2 ; 2 −4 −2] — signes différents ; voir Notes.)

##### 26- (p.197)
« Déterminer les réels a, b et c tels que la courbe d'équation y = ax³+bx²+cx+2, passe par les points A(5,62) ; B(−1,−4) et C(3,8). »

##### 27- (p.197)
« Yassine, Khalil et Nabil veulent s'équiper en matériels informatiques soit dans le magasin M1, soit dans le magasin M2. Leurs besoins et les prix unitaires HT en DT, sont donnés ci-dessous. »
| | Yassine | Khalil | Nabil |
|---|---|---|---|
| Disquette | 10 | 20 | 15 |
| CD | 15 | 5 | 10 |
| DVD | 3 | 5 | 10 |
| | Prix de M1 | Prix de M2 |
|---|---|---|
| Disquette | 0,50 | 0,55 |
| CD | 0,75 | 0,72 |
| DVD | 15,24 | 13,72 |
« Pour chaque question, on nommera par une lettre chaque matrice intervenant, en précisant ce qu'elle représente. 1) a- Donner la matrice représentant les dépenses HT respectives de Yassine, Khalil et Nabil, suivant qu'ils achètent à M1 ou à M2. b- Sur les vitrines de chaque magasin, on affiche 30% de remise sur tous les produits. La TVA sur ces produits étant de 19,6 % déterminer la matrice des dépenses TTC respectives de Yassine, Khalil et Nabil suivant qu'ils achètent à M1 ou à M2. 2) Finalement Yassine, Khalil et Nabil, se sont équipés dans un autre magasin nommé M3 et ont dépensé respectivement 52,5DT ; 75DT et 138,75DT. a- Etablir le système à résoudre pour trouver le prix unitaire TTC de chaque type d'articles. b- Résoudre le système en utilisant les matrices et conclure. c- En déduire la matrice colonne donnant les prix unitaires HT de chaque article chez M3 et conclure. »

##### 28- (p.197-198)
I) « On donne A = [17 14 16 ; 1 1 1 ; 2 1 4]. 1) Vérifier que A est inversible. 2) Déterminer la matrice inverse de A. »
II) « Le service informatique de gestion d'une entreprise occupe un grand bureau au troisième étage. Sa masse salariale est de 13 800DT par mois et ce service utilise 9 ordinateurs pour la gestion totale. On restructure ce service en trois bureaux b1, b2 et b3 de x, y et z personnes respectivement. Chaque personne du bureau b1 reçoit en moyenne 1700DT par mois, travaille avec un ordinateur et s'occupe de 10% de la gestion totale. Chaque personne du bureau b2 reçoit en moyenne 1400DT, travaille avec un ordinateur et s'occupe de 5% de la gestion totale. Chaque personne du bureau b3 reçoit, en moyenne 1600 DT, travaille avec un ordinateur et s'occupe de 20% de la gestion totale. 1) Traduire les informations ci-dessus en un système de trois équations à trois inconnues x, y et z. 2) Déterminer le nombre de personnes dans chaque bureau. »

##### 29- (p.198)
« Une firme internationale utilise trois sous-traitants A, B et C pour la fabrication de calculettes qui lui fournissent par jour : - A fournit : 100 boîtiers ; 40 claviers et 20 afficheurs. - B fournit : 100 boîtiers et 400 afficheurs. - C fournit : 30 boîtiers ; 80 claviers et 10 afficheurs. Cette firme veut réaliser en toute urgence 1 000 calculettes. Elle a donc besoin de 1 000 boîtiers, 1000 claviers et 1000 afficheurs. On note x, y et z le nombre de jours nécessaires à la fabrication pour chaque sous-traitant. 1) Traduire les informations ci-dessus en un système (S) de trois équations à trois inconnues x, y et z. 2) a) Donner l'écriture matricielle du système (S). b) Résoudre alors le système (S) et en déduire le nombre de jours de fabrication de chaque sous-traitant. » (Données telles qu'imprimées : B ne fournit pas de claviers — pas de ligne « claviers » pour B.)
(Les corrigés des exercices 1 à 29 ne sont pas dans le manuel.)

#### MATH CULTURE (p.199) — « Système de Cramer »
Texte imprimé : « Considérons le système d'équations (S) a1x1 + a2x2 + a3x3 = k1 ; b1x1 + b2x2 + b3x3 = k2 ; c1x1 + c2x2 + c3x3 = k3. (S) s'écrit donc AX = K avec A = [a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3], X = (x1 ; x2 ; x3) est la matrice des inconnues et K = (k1 ; k2 ; k3) est la matrice des constantes. (S) est dit **système de Cramer** lorsque A est inversible. Nous noterons A_i (i = 1, 2, 3) la matrice A dans laquelle on a remplacé la i-ème colonne par la matrice des constantes. Monsieur Cramer a prouver [sic] que lorsque A est inversible c'est à dire (S) est de Cramer alors ce dernier (le système (S)) admet une unique solution (x1, x2, x3) tels que : »
- x1 = dét(A1)/dét(A) = |k1 a2 a3 ; k2 b2 b3 ; k3 c2 c3| / |a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3|
- x2 = dét(A2)/dét(A) = |a1 k1 a3 ; b1 k2 b3 ; c1 k3 c3| / |a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3|
- x3 = dét(A3)/dét(A) = |a1 a2 k1 ; b1 b2 k2 ; c1 c2 k3| / |a1 a2 a3 ; b1 b2 b3 ; c1 c2 c3|
« Cette méthode de résolution est dite **méthode de Cramer**. »
Encart biographique (avec portrait) : « Gabriel Cramer (1704-1752). Mathématicien suisse ; nous lui sommes redevables de la résolution complète des systèmes carrés par les déterminants ». Source citée : aucune autre que ce texte (pas de référence bibliographique imprimée).

#### p.200 — page blanche (aucun contenu, vérifiée à l'image).

---
#### VOCABULAIRE OFFICIEL de la section (termes exacts imprimés)
matrice d'ordre n×p · coefficients ou termes · notation (a_ij), i^ème ligne / j^ème colonne · matrice ligne d'ordre p · matrice colonne d'ordre n · matrice carrée d'ordre n · diagonale · matrice unité d'ordre n, notée I_n · matrice nulle, notée O · matrices égales · somme A + B · différence A − B · matrice opposée (−1).A = −A · produit d'une matrice par un réel kA · produit de deux matrices A × B (produit ligne × colonne) · état initial / entrées / sorties du stock · déterminant, notation dét(M) ou |…| · Δ_ij (déterminant de la matrice d'ordre 2 obtenue en supprimant la i-ème ligne et la j-ème colonne) · développement par rapport à la première ligne (colonne) · matrice inversible · matrice inverse, notée M^{−1} · matrice du système · écriture matricielle A × X = B · matrice des constantes · système carré · méthode du pivot de Gauss · système de Cramer · méthode de Cramer · PRODUITMAT, INVERSEMAT (Excel).

#### BORNES de la section (d'après le manuel)
**INCLUS** : matrices d'ordre quelconque n×p (notation a_ij, matrices ligne/colonne/carrée/unité/nulle, égalité) ; somme, différence, produit par un réel (propriétés A+O, commutativité, associativité, k(A+B)=kA+kB) ; produit ligne×colonne, matrice×colonne, matrice×matrice (condition d'ordre, associativité, I_n neutre, A×(B+C)=A×B+A×C) ; déterminants d'ordre 2 (ad−bc) et 3 (développement selon la 1ʳᵉ colonne, équivalent selon la 1ʳᵉ ligne) ; dét(I2)=dét(I3)=1 ; inverse d'ordre 2 par la formule, d'ordre 3 par l'algorithme des cofacteurs Δ_ij (Activité III.6) ; théorème « inversible ⇔ dét ≠ 0 » (admis) ; unicité de l'inverse et « M×M'=I_n ou M'×M=I_n suffit » (admis) ; résolution de systèmes 2×2 et 3×3 par pivot de Gauss (« Revoir ») et par X = A^{−1}×B (théorème, cas dét(A)≠0) ; mise en système de problèmes économiques ; usage d'Excel (PRODUITMAT, INVERSEMAT).
**EXCLU / non traité dans les pages 165-200** : propriétés du déterminant (multiplicativité dét(AB), dét de la transposée, effet d'un échange de lignes…), transposée comme notion nommée (« échanger lignes et colonnes » n'est qu'une étape de l'algorithme, Activité III.6), développement selon une autre ligne/colonne, rang, valeurs propres, diagonalisation, matrices d'ordre > 3, systèmes non carrés traités matriciellement ; la méthode de Cramer n'apparaît qu'en « Math culture » (hors programme exigible a priori — le manuel la range en culture).

#### NOTIONS-CLÉS (≤ 8)
1. Matrice d'ordre n×p, coefficients a_ij, matrices particulières (ligne, colonne, carrée, unité, nulle) et égalité.
2. Somme, différence, produit par un réel : mêmes ordres requis, calcul coefficient par coefficient.
3. Produit de deux matrices (ligne×colonne ; condition colonnes(A)=lignes(B) ; non commutatif ; associatif ; distributif ; I_n neutre).
4. Déterminant d'ordre 2 (ad−bc) et d'ordre 3 (développement), dét(I_n)=1.
5. Matrice inversible et inverse M^{−1} ; critère dét(M)≠0 ; formule d'ordre 2 ; algorithme d'ordre 3 (cofacteurs, échange lignes/colonnes, 1/dét).
6. Écriture matricielle A×X=B d'un système ; système carré.
7. Résolution X=A^{−1}×B si dét(A)≠0 (solution unique) ; sinon 0 ou une infinité de solutions ; pivot de Gauss pour les cas non inversibles.
8. Modélisation de problèmes économiques (stocks, prix TTC avec TVA 19,6 %, masses salariales, mélanges) par matrices et systèmes.

---
#### § NOTES
**Pages lues** : 36/36 (165 à 200), toutes lues à la couche texte ET à l'image (110 dpi). La p.165 (titre) n'a pas de couche texte : lue à l'image. La p.200 est vierge (texte et image vides).
**Pages agrandies à 200 dpi** : p.173 (colonne de l'Act. 2.1), p.174 (Act. 2.2-2.3), p.175 (Act. 4), p.191 (Q4, Q5, ex. 2 ; Q8 relu), p.194 (ex. 11). Résultat : p.173 la couche texte donnait la colonne « 2 ; 5 ; −2 » alors que l'image montre (2/5 ; −2) — l'image fait foi (3×(2/5)+5×(−2)=−44/5 confirme).
**Coquilles imprimées (reproduites telles quelles)** :
- p.166 Act. 3 : « cinq milles dinar » ; p.174 Act. 3 : « Dans a matrice » pour « Dans la matrice ».
- p.176 Act. 7 : la ligne « atelier secrétariat » du tableau (probablement « atelier » seul) ; la matrice « R » est citée dans le schéma (« La matrice R peut être schématisée par ») sans avoir été nommée dans l'énoncé ; la question 1-b demande « pour les ateliers » alors que le tableau parle d'« atelier secrétariat ».
- p.178 Act. 11 : sous-questions numérotées « a) » puis « c) » (pas de b).
- p.183 Act. 6 : « A_22 = [0 0 ; 1 −2] » imprimé, alors que cette matrice est A_12 (suppression de la 1ʳᵉ ligne et de la 2ᵉ colonne de A) ; le Δ_12 qui suit correspond bien à [0 0 ; 1 −2] ; l'image p.183 montre des traits rouges de repérage de la ligne/colonne supprimées.
- p.190 Act. 3 : « déterminer A^{−1} » et « La matrice obtenue est A^{−1} » alors que la matrice donnée s'appelle C (il s'agit de C^{−1}) ; le bandeau de la p.190 porte « Exercices et problèmes » alors que ses Activités 3 et 4 appartiennent à « Avec l'ordinateur » ; l'activité 3 de « Avec l'ordinateur » (p.190) ne porte pas de titre de rubrique propre.
- p.191 : le QCM saute de Q5 à Q7 (pas de Q6) ; la colonne de réponses est titrée « C » (majuscule) après « a » et « b ».
- p.195 Ex. 18 : « son-elles » ; Ex. 15 : « entées » (deux fois) ; Ex. 13 : « trois coefficients de ces matières » (lu à l'image).
- p.198 Ex. 29 : le sous-traitant B ne fournit pas de claviers (aucune ligne « claviers » pour B), tel qu'imprimé.
**Incohérences de chiffres / énoncés à signaler (calculs du lecteur, à ne pas reprendre tels quels)** :
- p.190 Act. 4 (Avec l'ordinateur) : D = [2 −5 6 ; 0 4 7 ; −3 1 0] a pour dét = 163 (calcul du lecteur : 2(0−7) − (−5)(0+21) + 6(0+12) = −14+105+72 = 163) ; l'inverse correct serait (1/163)·[−7 6 −59 ; −21 18 −14 ; 12 13 8]. La matrice « D^{−1} » imprimée (dénominateurs 14, 73, 24, 63, 71, 36, 91, 97, 29) est donc incohérente avec D : l'énoncé « Vérifier que D est inversible et que D^{−1} = … » est faux tel qu'imprimé. Activité à ne pas reprendre (ou à corriger).
- p.191 Q8 : A = [1 3 0 ; 0 −1 1 ; −1 3 7] a dét = 1(−7−3) − 3(0+1) + 0 = −13 ≠ 0 (calcul du lecteur) ; la proposition « A est non inversible » est donc fausse, et les inverses proposés en b) et c) ne semblent pas être l'inverse de cette A (ex. b) : la 1ʳᵉ ligne de A × 2ᵉ colonne de la matrice b) = 1×1/3 + 3×(−1) + 0 = −8/3 ≠ 0). Aucune des trois propositions n'est exacte à l'image ; la question n'est pas fiable pour un QCM « une seule réponse exacte ».
- p.196 Ex. 23 3) : le système 3x − y = 0 ; 2x + 4y = 5 n'a pas la matrice A = [2 3 ; −3 1] de la question ; il faut recalculer l'inverse de [3 −1 ; 2 4] (dét = 14).
- p.197 Ex. 25 vs p.187 Act. 7 : A = [3 10 1 ; 2 8 2 ; 2 −4 −2] (ex. 25) contre [3 −10 −1 ; −2 8 2 ; 2 −4 −2] (Act. 7), seconds membres 10, 7, 8 contre 4, 7, 5 : deux matrices différentes (signes), probablement une variante voulue — ne pas les confondre.
- p.186 Act. 3 (actions d'Ahmed) : le système imprimé 10x+5y+6z=78 est cohérent avec « X ×2, Y +25 %, Z −40 % » (5×2=10 ; 4×1,25=5 ; 10×0,6=6) ; l'énoncé écrit « Le portefeuille d'année vaut » (coquille pour « Le portefeuille d'Ahmed »).
- p.182 Act. 2 : A^{−1} = [5/4 −2/4 ; −3/4 2/4] imprimé avec des coefficients non simplifiés (−2/4, 2/4).
- p.172 Act. 5 : « P' = 1,196P » (TTC) : TVA 19,6 % ; le prix du portable B en mars (2e coefficient de la 3e ligne) = 70 HT (lu dans P=[120 100 ; 100 90 ; 80 70]).
- p.174 Act. 3 : A×C : 7×2+10×2.5+11×4 = 14+25+44 = 83 ; 10×2+12×2.5+13×4 = 20+30+52 = 102 ; 11×2+9×2.5+12×4 = 22+22.5+48 = 92.5 — les totaux imprimés sont exacts.
- Notation : la matrice A de la p.174 Act. 3 est écrite avec des zéros initiaux (07, 09) ; le schéma qui suit les écrit 7 et 9.
- Notations de produit imprimées : « A×B » (croix) et « A.B » (point) pour les produits ligne×colonne (p.173) ; « k.A » pour le produit par un réel.
- TVA : taux imprimé 19,6 % partout (p.172 Act. 5, p.175 Act. 5, p.197 ex. 27) ; les prix sont en DT.
**`[?]` restants** : aucun (aucun passage illisible à l'image).
**Notes de forme** : chaque activité est numérotée par rubrique (le manuel recommence « Activité 1 » à chaque sous-section : 1) Notion de matrice, 2) Opérations — Addition / Multiplication par un réel, 3) Produit, II- Déterminant, III- Inverse, IV-1) Revoir, IV-2) Résolution par l'inverse) ; les numéros ci-dessus suivent cette numérotation imprimée. Il n'y a PAS d'exemple résolu complet dans cette tranche : le manuel ne donne aucun corrigé ni exemple résolu (hormis les schémas de calcul de A×B p.173, 174, 176 et les captures Excel p.189-190).

---

### Chapitre `m08-p201-236`

### m08 — Chapitre VIII « Statistiques » (pages PDF 201-236)

Source : manuel CNP « Mathématiques », 4ᵉ année secondaire, section économie et gestion (`222463P00.pdf`). Page PDF = page imprimée. Rubriques : Pour commencer (p.202-204), Cours (p.205-221), Avec l'ordinateur (p.222-223), Exercices et problèmes (p.224-235), Math culture (p.236). Notation : $\bar x$ = moyenne de x ; $\sigma_X$ ou $\sigma_x$ = écart type ; V(x) = variance ; cov(x, y) = covariance ; r(x, y) = coefficient de corrélation linéaire.

**Page 201 (couverture du chapitre)** : « Chapitre 8 — STATISTIQUES ». Plan imprimé : Pour commencer · Cours (Covariance ; Ajustement : Ajustement affine, Exemples d'ajustements non affines) · Avec l'ordinateur · Exercices et problèmes · Math culture.

---
#### POUR COMMENCER (p.202-204)

##### Pour commencer — Activité 1 (p.202) — distribution des employés par âge et par salaire
Situation : entreprise ; tableau « donne la distribution des employés par âge (x) et par salaire (y) dans une entreprise ». Salaire (y) en DT ; Age (x) en classes.

| Salaire y (DT) \ Age x | [18,25[ | [25,35[ | [35,45[ | [45,55[ | [55,65[ |
|---|---|---|---|---|---|
| [300,400[ | 25 | 2 | 18 | 15 | 10 |
| [400,500[ | 30 | 35 | 40 | 20 | 15 |
| [500,600[ | 26 | 34 | 40 | 25 | 20 |
| [600,900[ | 12 | 15 | 20 | 26 | 20 |
| [900,1500[ | 10 | 12 | 15 | 18 | 21 |

(Totaux recomptés, non imprimés : colonnes 103 · 98 · 133 · 104 · 86 ; lignes 70 · 140 · 145 · 93 · 76 ; total général 524.)

Questions verbatim :
1- a) Déterminer la distribution des effectifs marginaux de x.
 b) Peut on dire que les trois quarts des employés ont moins de 45 ans ?
 c) Calculer $\bar x$ et $\sigma_X$.
2- a) Déterminer la distribution des effectifs marginaux de y.
 b) Calculer $\bar y$ et $\sigma_Y$.
 c) Peut on dire que les trois quarts des employés sont bien payés (salaire dépassant 600DT) ?
(Pas de corrigé imprimé.)

##### Pour commencer — Activité 2 (p.202) — exportation du phosphate
Situation : « Le tableau suivant donne l'évolution x_i ; i = 1, 2,...,12 des revenues de l'exportation du phosphate (en millions de DT) et sa part en pourcentage y_i ; i = 1, 2,...,12 des revenues totales des exportations tunisiennes de l'année 1998 à l'année 2004. (source : INS 2004) »

| x_i | 355.5 | 461.5 | 525.2 | 615 | 670 | 702 | 712.5 | 717 | 765 | 725 | 686 | 865 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| y_i | 9.5 | 9.2 | 10.1 | 11.4 | 10.9 | 10.7 | 10.2 | 8.9 | 8.0 | 7.4 | 6.6 | 7.1 |

(Décimales avec point, telles qu'imprimées.) Questions verbatim :
1- Placer dans un repère orthogonal $(O,\vec i,\vec j)$ les points M_i(x_i, y_i) ; i = 1, 2,...,12.
2- a) Calculer $\bar x$ : la moyenne arithmétique de la série statistique à variable x_i et $\bar y$ la moyenne arithmétique de la série statistique à variable y_i.
 b) Placer le point G($\bar x$, $\bar y$) dans le repère $(O,\vec i,\vec j)$.
3- Existe-t-il un lien entre les variations de x et les variations de y ?

##### Pour commencer — Activité 3 (p.202-203) — salaires proposés et nombre de candidats
Énoncé : « Le nuage ci-dessous représente la série statistique double donnant les salaires en DT x_i, i = 1, 2,...,5 proposés par quelques entreprises pour des emplois analogues et les nombres y_i ; i = 1, 2,...,5 des candidats qui se présentent pour ses emplois. » Le nuage (p.203, repère : abscisses graduées 0 à 600 de 25 en 25, ordonnées 0 à 24 de 2 en 2) montre 5 points, lus à l'image (agrandie 200 dpi) : (225 ; 10), (350 ; 13), (375 ; 17), (400 ; 19) et le dernier vers (≈550-555 ; ≈21) [?] (le dernier point n'est pas exactement sur une graduation ; lecture approchée).
Questions verbatim : 1) Reconstruire le tableau statistique relatif à ce nuage. 2) Donner le salaire moyen offert par ces entreprises. 3) Préciser le point moyen du nuage.

##### Pour commencer — Activité 4 (p.203) — série double par classes (x entier, y en classes)
« On considère la série statistique à double caractères x et y donnée par le tableau ci-dessous. On désigne par y_i le centre de la classe C_i. »

| x \ y | [0,12[ | [12,18[ | [18,24[ | [24,48[ |
|---|---|---|---|---|
| -5 | 0 | 2 | 4 | 6 |
| -4 | 0 | 2 | 1 | 3 |
| 0 | 4 | 0 | 0 | 1 |
| 1 | 6 | 3 | 5 | 0 |
| 2 | 3 | 0 | 0 | 0 |

(Effectif total recompté : 12+6+5+14+3 = 40.) Questions : 1) Représenter le nuage des points M_i(x_i, y_i) dans un repère orthogonal $(O,\vec i,\vec j)$. 2) Déterminer le point moyen G.

##### Pour commencer — Activité 5 (p.203-204) — espérance de vie femmes/hommes
« Le tableau ci-dessous indique l'espérance de vie des femmes et des hommes en 1998 dans les 12 pays ayants le plus grand I.D.H (indicateur de développement humain). »

| x_i (femmes) | 81,9 | 81,3 | 80,2 | 81,2 | 81,4 | 81 | 80,7 | 80,8 | 83 | 80 | 80,8 | 82,1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| y_i (hommes) | 76,2 | 75,4 | 73,5 | 75,6 | 76,9 | 76,4 | 74 | 75,1 | 76,9 | 74,7 | 73,2 | 74,4 |

(Décimales avec virgule, comme imprimé.) Questions verbatim :
1- Placer le nuage des points de cette série dans un repère orthogonal (on pourra effectuer un changement d'origine).
2- Calculer les coordonnées du point moyen G de cette série. Combien de pays ont une espérance de vie pour les hommes et pour les femmes inférieure aux valeurs moyennes ?
3- N1 désigne le nuage des points M1(x1, y1), M2(x2, y2),..., M6(x6, y6). N2 désigne le nuage des points restants.
 a) Calculer les coordonnées de G1 (respectivement G2) le point moyen du nuage N1 (respectivement du nuage N2).
 b) Donner une équation cartésienne de la droite (G1G2).
 c) Pourquoi la droite (G1G2) passe par G ?

---
#### COURS — I- COVARIANCE (p.205-209)

Introduction (verbatim) : « En deuxième et en troisième année on a vu que la variance permet une mesure de l'écart à la moyenne des valeurs de la variable d'une série statistique simple. On peut se demander : Existe-t-il un paramètre qui permet de mesurer la dispersion des points du nuage par rapport au point moyen dans le cas d'une série double ? »

##### Cours I — Activité 1 (p.205) — taux d'activité de la population en Tunisie
Séries A et B : « La série A présente le taux global x (en %) de la population active en Tunisie et le taux y en (%) de la population masculine active. La série B présente le taux global x' (en %) de la population active en Tunisie et le taux y' en (%) de la population féminine active. »

SERIE A
| | 1966 | 1975 | 1984 | 1994 | 2004 |
|---|---|---|---|---|---|
| taux global x | 46 | 50 | 51 | 48 | 46 |
| Taux masculin y | 86 | 81 | 80 | 74 | 68 |

SERIE B
| | 1966 | 1975 | 1984 | 1994 | 2004 |
|---|---|---|---|---|---|
| taux global x' | 46 | 50 | 51 | 48 | 46 |
| Taux féminin y' | 6 | 19 | 22 | 33 | 24 |

Questions verbatim :
1- Construire, dans deux repères différents, les nuages des points des deux séries A et B.
2- Placer les points moyens G_A de la série A et G_B de la série B.
3- Calculer le réel : $C_A=\frac{1}{5}\sum_{i=1}^{5}(x_i-\bar x)(y_i-\bar y)$ où $\bar x$ et $\bar y$ sont respectivement les moyennes arithmétiques des variables x et y. C_A s'appelle **la covariance** de x et y et on la note cov(x, y).
4- Calculer cov(x', y').
5- Quelle est la série dont les points sont plus dispersés par rapport à son point moyen ?

**Définition (encadré, p.205, verbatim)** : Soit (x_i, y_i) avec i = 1,..., n une série statistique double. On appelle covariance de x et y le nombre noté cov(x, y) et défini par :
$\mathrm{cov}(x,y)=\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y)$.

##### Cours I — Activité 2 (p.206)
On reprend l'activité1 ci-dessus. a) Comparer cov(x, y) et le réel $\frac{1}{5}(\sum_{i=1}^{5}x_iy_i)-\bar x\,\bar y$. b) Comparer cov(x', y') et le réel $\frac{1}{5}(\sum_{i=1}^{5}x'_iy'_i)-\bar x'\,\bar y'$. c) Quelle conjecture peut on faire ?

##### Cours I — Activité 3 (p.206) — démonstration de la formule (I)
« Soit (x_i, y_i) avec i = 1,..., n une série statistique double. On se propose de montrer que : $\mathrm{cov}(x,y)=\frac{1}{n}(\sum_{i=1}^{n}x_iy_i)-\bar x.\bar y$ (I). »
1) Montrer que $\sum_{i=1}^{n}x_i=n\bar x$ et $\sum_{i=1}^{n}y_i=n\bar y$.
2) Vérifier que $\sum_{i=1}^{n}\bar x y_i=\bar x\sum_{i=1}^{n}y_i$ et que $\sum_{i=1}^{n}\bar x.\bar y=n\bar x.\bar y$.
3) Développer le produit $(x_i-\bar x)(y_i-\bar y)$ et déduire à l'aide des questions précédentes le résultat (I).

**Théorème (encadré, p.206, verbatim)** : Soit (x_i, y_i) avec i = 1,..., n une série statistique double :
• $\mathrm{cov}(x,y)=\frac{1}{n}(\sum_{i=1}^{n}x_iy_i)-\bar x.\bar y$.
• cov(x, y) = cov(y, x).
« Cette seconde expression de la covariance est plus commode pour les calculs "à la main". » (en gras italique)
**Exemple :** Soit (x_i, y_i) avec i = 1,..., n une série statistique double. Vérifier que : a) cov(x, y) = cov(y, x). b) cov(x, x) = V(x). (Pas de résolution imprimée.)

##### Cours I — Activité 4 (p.206-207) — prix du poisson
« Le tableau suivant indique l'évolution de 2000 à 2006 du prix moyen au kilogramme, en DT d'une sorte de poisson. »
| Année | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 |
|---|---|---|---|---|---|---|---|
| Rang de l'année x | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Prix y | 1,2 | 1,7 | 1,8 | 2,6 | 2,7 | 3,2 | 3,3 |
1) Représenter le nuage des points M_i(x_i, y_i) dans un repère orthogonal. Placer le point moyen G($\bar x$, $\bar y$). 2) Calculer cov(x, y). (Le manuel donne plus loin, Activité 7, « cov(x, y) ≈ 1.48 ».)

##### Cours I — Activité 5 (p.207)
« On considère les deux séries statistiques doubles suivantes (x_i, y_i) et (x_i', y_i') i = 1, 2,3, 4,5. »
| x | 1 | 3 | 7 | 8 | 9 |
|---|---|---|---|---|---|
| y | 2 | -2 | 4 | 7 | 10 |

| x' | 1 | 3 | 7 | 8 | 9 |
|---|---|---|---|---|---|
| y' | 3 | 10 | 18 | 25 | 30 |
1) Représenter, dans un même repère, les nuages des points des deux séries (x_i, y_i) et (x_i', y_i'). 2) Placer les points moyens G($\bar x$,$\bar y$) et G'($\bar x'$,$\bar y'$). 3) Dire les quels des deux nuages est le moins dispersé autour de son point moyen ? 4) Calculer puis comparer : cov(x, y) et cov(x', y'). 5) Faire une conjecture.

**Remarques (encadré, p.207, verbatim)** : 1) La variance permet une mesure de l'écart à la moyenne des valeurs de la variable d'une série statistique simple. 2) La covariance permet une mesure de la dispersion des points du nuage par rapport au point moyen.

**Propriétés (admises, encadré p.207, verbatim)** : « On admet les propriétés suivantes : » Soit (x_i, y_i) avec i = 1,..., n une série statistique double. Pour tous réels α, β.
P1 : cov(x + α, y + β) = cov(x, y).
P2 : cov(αx, βy) = αβ cov(x, y).

##### Cours I — Activité 6 (p.207-208) — amortissement d'une machine-outil
« Une entreprise achète une machine –outil 10000DT. Le tableau d'amortissement ci-dessous donne la valeur y (en DT) de cette machine après x années d'utilisation. »
| x | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| y | 8500 | 7000 | 6000 | 5500 | 4500 |
1) On pose $x'=x$ et $y'=\frac{y-4000}{1000}$. Calculer cov(x', y'). 2) En déduire la valeur de cov(x, y). (Par P1 et P2 ; aucun corrigé imprimé.)

##### Cours I — Activité 7 (p.208) — « Avec une calculatrice » (touches de calculatrice)
Texte : « La quasi-totalité des calculatrices scientifiques contiennent des touches qui permettent de calculer aisément les différents paramètres statistiques que ce soit dans le cas des séries simples ou des séries doubles. Ainsi on épargne un calcul parfois pénible et une perte de temps inutile. Ce que nous vous proposons par la suite n'est pas un algorithme valable pour tous les modèles des calculatrices mais une stimulation pour chercher à utiliser la calculatrice. On se propose de répondre à la deuxième question de l'activité 4 en utilisant deux modèles de calculatrices. » (données : celles de l'Activité 4 ci-dessus, y = 1,2 ; 1,7 ; 1,8 ; 2,6 ; 2,7 ; 3,2 ; 3,3 pour x = 1…7).
- Premier modèle (touches : 2ndF MODE 2, DATA et RCL). Étape préliminaire : 2ndF MODE 2 → l'écran affiche 0 ; puis, pour chaque donnée : `(x, y) 1,2 DATA` → écran 1 ; `(x, y) 1,7 DATA` → 2 ; 1,8 → 3 ; 2.6 → 4 ; 2.7 → 5 ; 3.2 → 6 ; 3.3 → 7. Obtention des résultats : RCL $\bar x$ (pour obtenir $\bar x$) ; RCL $\bar y$ (pour obtenir $\bar y$) ; RCL $\Sigma xy$ (pour obtenir $\sum_{i=1}^{7}x_iy_i$). « Vérifier que : cov(x, y) ≈ 1.48 ».
- Deuxième modèle (touches : MODE ÷, SHIFT , Scl et EXE). Étape préliminaire : MODE ÷ (et LR s'affiche) SHIFT Scl EXE (pour entrer en mode série statistique double) ; puis `1 SHIFT , 1,2 DT` ; `2 SHIFT , 1,7 DT` ; `3 SHIFT , 1,8 DT` ; `4 SHIFT , 2,6 DT` ; `5 SHIFT , 2,7 DT` ; `6 SHIFT , 3,2 DT` ; `7 SHIFT , 3,3 DT`. Obtention : SHIFT $\bar x$ EXE (pour obtenir $\bar x$) ; SHIFT $\bar y$ EXE (pour obtenir $\bar y$) ; SHIFT $\Sigma xy$ EXE (pour obtenir $\sum_{i=1}^{7}x_iy_i$). « Vérifier que : cov(x, y) ≈ 1.48 ».

##### Cours I — Activité 8 (p.209) — exports/imports en Tunisie
« Le tableau ci-dessous représente les taux de croissance en pourcentage des exports et des imports en Tunisie de l'année 1995 à l'année 2004. »
| Export (x_i) | 10.1 | 3.9 | 14.4 | 6.0 | 6.9 | 14.9 | 19.1 | 12.6 | 16.1 | 16.6 |
|---|---|---|---|---|---|---|---|---|---|---|
| Import (y_i) | 12.3 | 13.5 | 17.3 | 7.9 | 6.0 | 16.6 | 16.7 | 14.4 | 13.9 | 13.7 |
1) Calculer la moyenne arithmétique $\bar x$ de la série (x_i) i=1,...,10 et la moyenne arithmétique $\bar y$ de la série (y_i) i=1,...,10. 2) Calculer cov(x, y) de la série statistique double (x_i, y_i). Interpréter le résultat trouvé.

##### Cours I — Activité 9 (p.209) — salaire et ancienneté des cadres
« Dans le tableau ci-dessous, on a consigné par classes les observations relatives aux salaires perçus (en DT) par les cadres d'une entreprise et l'ancienneté (en années) de ces mêmes cadres. »
| Salaire y (DT) \ Ancienneté x | [0,2[ | [2,4[ | [4,6[ | [6,10[ | [10,15[ |
|---|---|---|---|---|---|
| [300,400[ | 5 | 2 | 2 | 1 | 0 |
| [400,500[ | 3 | 5 | 3 | 4 | 2 |
| [500,600[ | 2 | 4 | 1 | 5 | 6 |
| [600,900[ | 0 | 0 | 1 | 1 | 2 |
| [900,1500[ | 0 | 0 | 0 | 0 | 2 |
(Total recompté : colonnes 10 · 11 · 7 · 11 · 12 ; lignes 10 · 17 · 18 · 4 · 2 ; effectif total 51.)
1- Dans un repère orthogonal représenter le nuage des points associé à la série double (x_i, y_i) où x_i désigne le centre de la i-ème classe d'ancienneté et y_i désigne le centre de la i-ème classe de salaires. 2- a) Déterminer la distribution des effectifs marginaux de x. b) Calculer $\bar x$ et σ_X. 3- a) Déterminer la distribution des effectifs marginaux de y. b) Calculer $\bar y$ et σ_Y. 4- Calculer cov(x, y).

---
#### COURS — II- AJUSTEMENT (p.210-224)

##### 1) Introduction (p.210, verbatim)
« L'analyse d'un nuage de points M_i(x_i, y_i) représentant une série statistique double (x_i, y_i) peut conduire à la recherche d'une liaison entre les deux variables x et y. Cette liaison aide, entre autre, à faire des prévisions et à répondre à des questions parfois décisives. Une question s'impose alors : peut-on trouver une formule mathématique qui exprime le lien entre les deux variables ? La réponse à cette question conduit à étudier le type de relation entre les deux variables (affine, parabolique, …) on parle d'**ajustement**. »

##### Cours II.1 — Activité 1 (p.210) — équipement des ménages tunisiens
« Les courbes ci-dessous donnent les taux (en %) d'équipement des ménages tunisiens en quelques biens (Voitures – Téléviseurs - Téléphones) de l'année 1989 à l'année 2005. » Graphique : 3 courbes, axe vertical 0 à 100 (graduations de 10 en 10), axe horizontal gradué « 1994 1989 1999 2000 2001 2002 2003 2004 » [coquille d'ordre, voir Notes]. Lecture à l'image (indicative) : téléviseurs ≈ 58 au départ, ≈ 80 vers « 1999 », ≈ 85-90 ensuite, ≈ 88 à la fin ; téléphones ≈ 6 au départ puis ≈ 27, ≈ 37 à la fin ; voitures ≈ 9 au départ puis ≈ 16-19.
Questions verbatim : 1) Pour chaque bien, en quelle année le taux d'équipement était-il ou serait-il de l'ordre de 60 % ? 3) Quel bien ne semble pas atteindre ce taux ? [numérotation imprimée « 1) » puis « 3) » ; pas de « 2) »]

##### Cours II.1 — Activité 2 (p.210-211) — UNESCO, enfants non scolarisés
« A partir des chiffres connus de l'année 1970 à l'année 2000 le graphique ci-dessous permet à l'UNESCO de faire des prévisions pour les dix ans à venir. » Graphique p.211 : « Nombre d'enfants d'âge scolaire non scolarisés dans le monde (en millions). » Séries (légende) : Afrique subsaharienne, Asie de l'Est – Océanie, Amérique latine – Caraïbes, Asie du sud, États arabes ; axe vertical 0 à 50 (pas de 5), axe horizontal 1970-2010 ; la zone « prévision » est en pointillés après 2000 (lecture indicative : Afrique subsaharienne prévue ≈ 43-44 millions en 2010 ; États arabes ≈ 29-30 en 2010 [?], valeurs lues à l'œil, non imprimées).
Questions verbatim : 1) Donner les prévisions du nombre d'enfants non scolarisés dans les états arabes et dans l'Afrique subsaharienne en 2010. 2) Quelle est la région du monde où l'effort de scolarisation a été le plus important ? 3) En quelles régions du monde l'UNESCO doit faire plus d'efforts ?

##### 2) Ajustement affine (p.211-224)
**Cours II.2 — Activité 1 (p.211-212) — trois nuages**
« On considère les trois nuages de points : » Nuage 1 (Nombre en milliers de médecins en Tunisie de 1990 à 2004) [Source INS 2004] : points croissants de ≈ 4,3 (1990) à ≈ 10 (2004), allure allongée ; Nuage 2 (Nombre en milliers de parcs logements en Tunisie) [Source INS 2004] : 8 points de 1966 à 2004 [R7 : 8 points comptés à l'image, non « ≈ 9 »], croissants, allure allongée (graduations verticales partiellement illisibles à l'impression : 500, 1000, … 3000 [?]) ; Nuage 3 (Prix moyen en dollars du baril de pétrole de 1973 à 2005) [Source OMC 2004] : points dispersés, (1973 ; ≈ 70), (1984 ; ≈ 17), (1985 ; ≈ 23), (1987 ; ≈ 30), (1989 ; ≈ 32), (1995 ; ≈ 28), (1999 ; ≈ 30), (2004 ; ≈ 41), (2005 ; ≈ 65) (lecture à l'image, valeurs non imprimées).
Question verbatim : « Quel est le nuage qui semble avoir une forme allongée ? Dans ce cas, tracer une droite qui passe aussi près que possible des points de ce nuage ? (On dit alors que **l'on ajuste** ce nuage par une droite). »

###### Méthode des moindres carrés (p.212-214)
**Activité 1 (p.212-213) — notes d'économie au baccalauréat et au concours**
« Voici les notes obtenues en économie par cinq élèves d'une même classe au baccalauréat et lors d'un concours d'accès à un institut supérieur. »
| Note x_i au baccalauréat | 7 | 10 | 11 | 13 | 16 |
|---|---|---|---|---|---|
| Note y_i au concours | 8 | 9 | 12 | 12 | 13 |
1- Dans un repère orthogonal représenter le nuage des points associé à cette série double. 2- Ces points sont-ils alignés ? 3- a) Sur le graphique précédent, tracer la droite qui passe par les points A1(7;8) et A4(13;12). b) Vérifier que la droite (A1A4) admet pour équation : $y=\frac{2}{3}x+\frac{10}{3}$.
4- a) Calculer la moyenne $\bar x$ des notes obtenues par ces élèves au baccalauréat, puis la moyenne $\bar y$ des notes obtenues au concours. b) Placer le point moyen G. c) Vérifier que (A1G) admet pour équation : $y=\frac{7}{11}x+\frac{39}{11}$.
5- Comparer $S_1=\sum_{i=1}^{5}(y_i-\frac{2}{3}x_i-\frac{10}{3})^2$ et $S_2=\sum_{i=1}^{5}(y_i-\frac{7}{11}x_i-\frac{39}{11})^2$.
6- Soit d la droite d'équation $y=\frac{66}{113}x+\frac{468}{113}$. a) Calculer $S_3=\sum_{i=1}^{5}(y_i-\frac{66}{113}x_i-\frac{468}{113})^2$. Comparer S1 ; S2 et S3. b) Vérifier que la droite d passe par G et que le coefficient directeur de d est égal à $\frac{\mathrm{cov}(x,y)}{V(x)}$.
(Vérification faite par moi, hors manuel : $\bar x=11,4$ ; $\bar y=10,8$ ; V(x)=9,04 ; cov=5,28 ; $\frac{66}{113}$ et $\frac{468}{113}$ cohérents. Le manuel n'imprime aucun de ces résultats.)

**Principe de la méthode des moindres carrés (p.213, verbatim)** :
« Etant donnée une série statistique double (x_i, y_i), i = 1, 2,...., n ou' (x_i) est une série non constante et telle que le nuage des points M_i(x_i, y_i) soit relativement allongé. On cherche une droite D d'équation réduite $y=ax+b$ qui passe le plus près possible des points du nuage. Pour cela :
- On calcule, pour tout, i = 1, 2,...., n la distance M_iP_i entre le point M_i du nuage et le point P_i de la droite D ayant la même abscisse que M_i.
- On cherche les réels a et b pour lesquels la somme $S=M_1P_1^2+M_2P_2^2+...+M_nP_n^2$ des carrés de ces distances est minimale.
La somme $S=M_1P_1^2+M_2P_2^2+...+M_nP_n^2$ est appelée **somme des carrées des résidus**. »
(Figure : nuage, droite D, points M_i(x_i,y_i) et P_i(x_i, ax_i+b), ordonnées marquées y_1, ax_1+b, y_2, ax_2+b, y_i, ax_i+b.)
**Encadré (p.213, verbatim)** : « On admet qu'une telle droite existe et qu'elle est unique. On l'appelle droite de régression de y en x » — suivi (italique gras) : « Pourquoi droite de régression ? (Voir maths culture). »

**Théorème : (admis) (encadré p.214, verbatim)** : « La droite de régression de y en x dans un repère orthogonal associée à la série statistique double (x_i, y_i) est la droite qui passe par le point moyen G($\bar x$, $\bar y$) et de coefficient directeur le réel $a=\frac{\mathrm{cov}(x,y)}{V(x)}$. » (figure : nuage, droite D, point G, $\bar x$, $\bar y$.)
**Remarques (encadré p.214, verbatim)** :
1) L'équation réduite de la droite de régression de y en x est : $y=a(x-\bar x)+\bar y$ avec $a=\frac{\mathrm{cov}(x,y)}{V(x)}$.
2) L'équation réduite de la droite de régression de x en y est : $x-\bar x=a'(y-\bar y)$ avec $a'=\frac{\mathrm{cov}(x,y)}{V(y)}$.

**Activité 2 (p.214) — population active en Tunisie**
« Le tableau ci-dessous représente l'évolution de la population active (en millier) en Tunisie depuis 1966. »
| Année x_i | 1966 | 1975 | 1984 | 1989 | 1994 | 1997 | 1999 | 2000 | 2001 | 2002 | 2003 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Population y_i | 1093.5 | 1621.8 | 2137.3 | 2360.6 | 2772.4 | 2978.3 | 3143.9 | 3215.7 | 3292.7 | 3375.7 | 3460.5 |
1- Déterminer le point moyen G de la série (x_i, y_i). 2- Représenter, dans un repère orthogonal, le nuage des points associé à cette série double. L'ajustement affine est-il plausible ? 3- a) Donner une équation de la droite de régression y en x. b) Trouver le nombre de la population active vers l'an 2010. 4- a) Donner une équation de la droite de régression de x en y. b) Vers quelle année la population active dépasse t-elle le nombre 5000000 ?

###### Coefficient de corrélation linéaire (p.215-216)
**Activité 1 (p.215)** : 1) Pour les activités 1 et 2 précédentes, calculer le réel $r(x,y)=\frac{\mathrm{cov}(x,y)}{\sigma_x\sigma_y}$. 2) Dans chacun des cas comparer |r(x, y)| à 0.95.
**Définition (encadré p.215, verbatim)** : « On appelle coefficient de corrélation linéaire des variables x et y le réel $r(x,y)=\frac{\mathrm{cov}(x,y)}{\sigma_x\sigma_y}$. »
**Remarques (encadré p.215, verbatim)** :
✓ La décision d'ajuster un nuage par une droite se prend jusqu'à présent à la seule vue du nuage de points, selon que sa forme est allongée ou non.
✓ On s'accorde à dire, pour des raisons qui dépassent le cadre du programme, que :
- Si |r(x, y)| ∈ [0 ; 0,70] alors la corrélation entre x et y est faible.
- Si |r(x, y)| ∈ ]0,70 ; 0,95] alors la corrélation entre x et y est forte.
- Si |r(x, y)| ∈ ]0,95 ; 1] alors la corrélation entre x et y est très forte.
✓ On démontre et nous admettons les propriétés suivantes :
• −1 ≤ r(x, y) ≤ 1.
• Si |r(x, y)| = 1 alors il y'a une dépendance totale entre x et y, l'une est une fonction affine de l'autre.
**Activité 2 (p.215)** : « En reprenant les données de l'activité 4 de la **partie I**. » (prix du poisson) 1- Calculer le coefficient de corrélation entre x et y. L'ajustement affine est-il plausible ? 2- a) Par la méthode des moindres carrés donner une équation de la droite de régression de y en x. b) Estimer le prix au kg de cette sorte de poisson en 2010.
**Activité 3 (avec une calculatrice) (p.215-216)** : « On reprend les données de **l'activité 4 de la partie I** et on se propose de calculer le coefficient de corrélation linéaire entre x et y et de déterminer l'équation de la droite d de régression de y en x avec les mêmes modèles de calculatrices utilisées dans **la partie I.** » Touches (p.216) : Premier modèle : 2ndF MODE 2 → écran 0. ; `(x,y) 1,2 DATA` → 1. ; … `(x,y) 3.3 DATA` → 7. (mêmes données qu'en partie I). Obtention : RCL r (coefficient de corrélation entre x et y) ; RCL b (coefficient directeur de d) ; RCL a (l'équation de d est y = bx + a). Deuxième modèle : mêmes saisies `n SHIFT , valeur DT` ; SHIFT r EXE (coefficient de corrélation entre x et y) ; SHIFT B EXE (coefficient directeur de d) ; SHIFT A EXE (l'équation de d est y = Bx + A).
**Activité 4 (p.216-217) — intensité du travail et fréquence cardiaque**
« Les relevés de l'intensité du travail fourni (x_i) exprimée en kilojoules par minute et la fréquence cardiaque (y_i) (nombre de battements par minute) de huit personnes sont consignés dans le tableau suivant : »
| x_i | 9.6 | 12.8 | 18.4 | 31.2 | 36.8 | 47.2 | 49.6 | 56.8 |
|---|---|---|---|---|---|---|---|---|
| y_i | 70 | 86 | 90 | 104 | 120 | 128 | 144 | 154 |
1- Représenter le nuage des points M_i(x_i, y_i). 2- Calculer la moyenne, la variance et l'écart type de chacune des séries à une variable x et y. 3- Calculer le coefficient de corrélation linéaire entre les variables x et y. Interpréter le résultat trouvé. 4- Par la méthode des moindres carrés donner une équation de la droite d de régression de y en x puis une équation de la droite d' de x en y. Tracer ces deux droites dans un même repère. 5- a) Prévoir le nombre par minute correspondant à un travail de 40 kilojoules. b) Prévoir l'intensité du travail correspondant à 100 battements par minute.

###### Méthode de Mayer (p.217-218)
**Activité 1 (p.217) — valeurs d'une action en bourse**
« Le tableau ci-dessous donne le relevé des valeurs d'une action en DT sur 15 jours consécutifs d'une bourse. »
| jour x_i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeur y_i | 18.8 | 18.9 | 18.9 | 19.5 | 19.2 | 19 | 19.2 | 19.6 | 19.5 | 19.7 | 19.2 | 19.7 | 19.8 | 20 | 20.5 |
« On note N1 le nuage de points associé la série (x_i, y_i) ; i = 1, 2,...,8 et N2 le nuage des points restants. a) Déterminer le point moyen G1 de la première série. b) Déterminer le point moyen G2 de la deuxième série. c) Déterminer l'équation de la droite (G1G2). d) La droite (G1G2) passe t – elle par le point moyen de la série totale ? »
**Encadré (p.217, verbatim)** : « Le principe de l'ajustement par la méthode de Mayer consiste à partager le nuage associé à une série (x_i, y_i) en deux nuages dont le nombre de points diffère d'au plus un. On désigne par G1 et G2 les points moyens respectifs du premier et du deuxième nuage. La droite (G1G2) est appelée **droite de Mayer**. »
**Activité 2 (p.217-218) — population urbaine en Tunisie (%)** [Source INS 2004]
| Année x_i | 1990 | 1991 | 1992 | 1993 | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Population Urbaine (%) y_i | 59.6 | 59.8 | 60.5 | 60.8 | 61.0 | 61.3 | 61.6 | 61.9 | 62.2 | 62.4 | 62.6 | 63.2 | 63.4 | 63.6 | 64.9 |
1- a) Représenter le nuage des points M_i(x_i, y_i). b) Calculer le coefficient de corrélation linéaire entre x et y. Interpréter le résultat. 2- a) Donner une équation cartésienne de la droite de régression d de y en x par la méthode des moindres carrés. b) Donner une équation d'une droite d' d'ajustement de cette série par la méthode de Mayer. 3- On note S la somme des carrés des résidus de la série (x_i, y_i) par rapport à la droite d et S' la somme des carrés des résidus de la série (x_i, y_i) par rapport à la droite d'. a) Expliquer pourquoi S' ≥ S. b) Vérifier le résultat précédent par le calcul. 4- Estimer le pourcentage de la population urbaine à l'an de 2010. a) à l'aide de la droite d. b) à l'aide de la droite d'.
**Activité 3 (p.218) — taux d'équipement automobile et âge au premier mariage des femmes**
« Une étude faite dans un pays riche sur le taux d'équipement des ménages en automobiles et l'âge des femmes lors de leur premier mariage. Les résultats sont donnés dan le tableau ci-dessous : »
| Années | 1979 | 1981 | 1984 | 1986 | 1988 | 1990 | 1991 | 1992 | 1993 | 1994 |
|---|---|---|---|---|---|---|---|---|---|---|
| Taux en (%) x_i | 68.6 | 70 | 72.9 | 73.4 | 74.6 | 76.5 | 76.8 | 77 | 78 | 79.5 |
| Age y_i | 22.9 | 23.1 | 23.9 | 24.5 | 25 | 25.6 | 25.8 | 26.1 | 26.4 | 26.7 |
1- Construire le nuage des points relatif à la série (x_i, y_i). 2- a) Calculer le coefficient de corrélation linéaire r(x, y) de cette série et interpréter le résultat. b) Donner l'équation de la droite de régression de y en , on note a son coefficient directeur [mots manquants imprimés : « de y en [x] »]. c) Suivant cet ajustement, quel serait l'âge au premier mariage pour un taux de 90 % ? Ce calcul a-t-il un sens ? 3- On note t_i le nombre d'années écoulées depuis 1979, ainsi t = 0 en 1979. a) Dresser les deux tableaux (t_i, x_i) et (t_i, y_i) et représenter ces deux séries double dans deux repères orthogonaux. Quel type d'ajustement peut-on faire ? b) Déterminer le coefficient directeur m de la droite de régression de y en t puis m' celui de la droite de régression de x en t. c) Déterminer le lien entre a, m et m'.
Conclusion imprimée (verbatim) : « Ici le taux d'équipement et l'âge étant deux fonctions affine du temps. On retrouve une relation affine entre le taux et l'âge, pourtant il n'y a aucune relation de causalité entre l'âge des femmes lors de leurs premiers mariages et l'équipement des ménages en automobiles. »

##### 3) Exemples d'ajustements non affines (p.218-220)
**Exemple 1 : (ajustement polynomial) (p.218-219)** — « Le tableau ci-dessous donne l'évolution de salaires nets en indice, base 100 en 1992 dans un pays industrialisé : »
| Année | 1992 | 1993 | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 |
|---|---|---|---|---|---|---|---|---|
| Rang x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Indice y | 100 | 97,6 | 96,8 | 98,4 | 98,3 | 99,8 | 103,3 | 106,7 |
1- a) Représenter la série double (x_i, y_i) dans un repère orthogonal. b) Un ajustement affine est – il justifié ? 2- On propose un ajustement par une fonction polynôme du deuxième degré (ajustement quadratique) représentée par une parabole P d'équation $y=ax^2+bx+c$. a) Déterminer les réels a, b et c afin que P passe par les points A(0,100), B(5,100) et C(7,107). b) Construire la parabole P dans le repère précédent. c) À l'aide de cet ajustement calculer la prévision de l'indice des salaires n et en 2002.
**Exemple 2 : (Ajustement homographique) (p.219)** — « Etude du taux d'équipement des ménages en automobile de 1969 à 2000 en France : »
| Année | 1969 | 1973 | 1977 | 1979 | 1980 | 1984 | 1986 | 1988 |
|---|---|---|---|---|---|---|---|---|
| Taux | 55,4 | 61,6 | 66,1 | 68,6 | 70 | 72,9 | 73,4 | 74.6 [R7 : point décimal imprimé] |

| Année | 1990 | 1991 | 1992 | 1993 | 1996 | 1998 | 2000 |
|---|---|---|---|---|---|---|---|
| Taux | 76,5 | 76,8 | 77 | 78 | 78,9 | 79,4 | 80 |
1- a) Déterminer l'ajustement affine par la méthode des moindres carrés de ce nuage, en prenant x_i = année − 1900 et on donnera le coefficient a à 10⁻³ près et b à 0,1 près. b) En déduire la valeur du taux d'équipement en 2000 à l'aide de cet ajustement. Comparer le résultat trouvé à la valeur réelle. 2- On se propose de faire un ajustement par une fonction homographique f telle que : $f(x)=\frac{kx+m}{x-50}$ pour $x\in[60,+\infty[$. a) Déterminer les réels k et m pour avoir f(80) = 70 et f(100) = 80. b) Etudier la fonction f. c) Calculer le taux en 2000 à l'aide de cet ajustement. Comparer le résultat avec la valeur réelle. d) Faire une prévision pour 2007.
**Exemple 3 : (ajustement logarithmique) (p.219)** — « De 1987 à 1997, L'OPEP a augmenté sa production de pétrole, mais de manière ralentie. Le tableau ci-dessous donne cette production. On note x le rang de l'année et y la production en millions de tonnes. On pose X = ln(x) on a obtenu les valeurs arrondies de X à 10⁻² près. »
| Année | 1987 | 1988 | 1989 | 1990 | 1991 | 1992 | 1993 | 1994 | 1995 | 1996 | 1997 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| production y_i | 944 | 1065 | 1137 | 1232 | 1231 | 1297 | 1332 | 1333 | 1368 | 1408 | 1423 |
| Rang x_i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| X = ln(x_i) | 0.00 | 0.69 | 1.10 | 1.39 | 1.61 | 1.79 | 1.95 | 2.08 | 2.20 | 2.30 | 2.40 |
1- a) Déterminer une équation de la droite de régression de y en X relative à la série double (X_i, y_i) sous la forme : y = aX + b, avec a et b arrondis à l'unité. b) En déduire une relation entre le rang x et la production y : y = f(x).

**Exemple 3 (suite, p.220)** — 2- a) Dans un même repère orthogonal, placer le nuage de points M_i(x_i, y_i) et représenter la fonction f définie sur [1;+∞[. b) À l'aide de cet ajustement ; donner une estimation de la production de pétrole en 2002, si cette politique se poursuit.

**Exemple 4 : (ajustement exponentiel) (p.220-221)** — « Le but de l'exemple est de déterminer le prix d'équilibre d'un produit. (On rappelle que le prix d'équilibre d'un produit est obtenu lorsque l'offre et la demande sont égales.) Une étude faite sur un produit a donné les résultats suivants (le prix au kilogramme est exprimé en DT et les quantités offre et demande sont exprimées en milliers de kilogrammes). »
| Prix proposé x_i | 0,30 | 0,35 | 0,45 | 0,65 | 0,80 | 1 |
|---|---|---|---|---|---|---|
| Demande y_i | 6,25 | 4,90 | 3,75 | 2,75 | 2,40 | 2,25 |
| Offre z_i | 1,25 | 1,30 | 1,30 | 1,50 | 1,55 | 1,60 |
« Tous les résultats numériques seront donnés en valeur décimale arrondie à 10⁻² près. »
1- Le plan P est rapporté au repère orthogonal (O, i, j) d'unités graphiques 10 cm pour 1DT en abscisse et 2 cm pour 1 milliers de kilogrammes en ordonnée. Représenter sur le même graphique les nuages de points associés respectivement aux séries statistiques doubles (x_i, y_i) et (x_i, z_i).
2- **Etude de la demande** : La forme du nuage de points associé à la série (x_i, y_i) permet d'envisager un ajustement exponentiel de y en x. On pose donc Y_i = ln(y_i). a) Donner une équation de la droite des moindres carrés du nuage de points associé à la série statistique double (x_i, Y_i). b) En déduire, en utilisant l'égalité Y = ln(y), une estimation de la demande y en fonction du prix x au kilogramme.
3- **Etude de l'offre** : La forme du nuage de points associé à la série (x_i, z_i) permet d'envisager un ajustement affine. Donner une équation de la droite des moindres carrés du nuage de points associé à cette série statistique double (x_i, z_i).
4- **Etude graphique du prix d'équilibre** : On considère, dans la suite du problème, que la demande et l'offre sont respectivement formalisées par les fonctions f et g définies sur l'intervalle [0 ; 2] par : $f(x)=e^{-1,41x+2,08}$ et $g(x)=0,53x+1,10$. a) Déterminer le sens de variation de la fonction f sur l'intervalle [0 ; 2] et dresser son tableau de variation. b) Sur le graphique du 1, tracer les courbes représentatives des fonctions f et g. c) Déterminer graphiquement le prix d'équilibre du produit.
5- **Etude numérique du prix d'équilibre** : On considère la fonction h définie sur l'intervalle [0 ; 2] par : h(x) = f(x) – g(x). a) Déterminer le sens de variation de la fonction h sur l'intervalle [0 ; 2] et dresser son tableau de variation. b) Montrer que l'équation h(x) = 0 admet dans l'intervalle [0 ; 2] une solution unique x₀. Donner une valeur approchée à 10⁻¹ près de x₀. c) Quel est le prix d'équilibre du produit considéré ?

---
#### AVEC L'ORDINATEUR (p.222-223)

##### Avec l'ordinateur — Activité 1 (Avec Excel 2003) (p.222) — population urbaine en Tunisie
Texte verbatim : « On se propose d'étudier l'évolution de la population urbaine en Tunisie. Les données sont entrées en tableau : les années en colonne **A**, la population tunisienne totale en colonne B et la population urbaine tunisienne en colonne C. Pour calculer la part de la population urbaine tunisienne par rapport à la population tunisienne totale, taper dans la cellule D3 la formule suivante : D3 =C3/B3*100. Pour obtenir le graphique : sélectionner les années (Colonne **A**) et les parts (colonne **D**) en appuyant simultanément sur la touche Ctrl et le bouton droit de la souri. Cliquer, en suite, sur l'onglet [icône assistant graphique] et choisir du type graphique : nuage de points. Cliquer droit sur les points du nuage pour entrer dans le format de la série de données et cliquer « Ajouter une courbe de tendance… », Cliquer sur l'onglet « Type | Options », choisir « Type | Linéaire », puis « Options » ☑ « Afficher l'équation sur le graphique » on obtient le graphique ci-dessous représentant la série double (x_i, y_i). x_i désigne les années et y_i désigne les parts. »
Feuille Excel imprimée (titre « Part de la population urbaine en Tunisie », colonnes A Année · B Pop Totale · C Pop Urbaine · D Part (en %), lignes 3 à 17), lue à l'image (agrandie 220 dpi) :
| Année | Pop Totale | Pop Urbaine | Part (en %) |
|---|---|---|---|
| 1990 | 8154,4 | 4860,0 | 59,6 |
| 1991 | 8318,2 | 4974,3 | 59,8 |
| 1992 | 8489,9 | 5136,4 | 60,5 |
| 1993 | 8657,4 | 5263,7 | 60,8 |
| 1994 | 8815,4 | 5377,4 | 61 |
| 1995 | 8957,5 | 5490,9 | 61,3 |
| 1996 | 9089,3 | 5599,0 | 61,6 |
| 1997 | 9214,2 | 5712,8 | 62 |
| 1998 | 9333,3 | 5805,3 | 62,2 |
| 1999 | 9455,9 | 5900,5 | 62,4 |
| 2000 | 9563,5 | 5986,8 | 62,6 |
| 2001 | 9673,6 | 6113,7 | 63,2 |
| 2002 | 9781,9 | 6201,7 | 63,4 |
| 2003 | 9839,8 | 6258,1 | 63,6 |
| 2004 | 9932,4 | 6456,1 | 65 |
Graphique : nuage de points 1990-2004 (ordonnées 59 à 66) avec droite de tendance linéaire, équation affichée « y = 0,3296x - 596,36 » (lue à l'image ; signe du terme constant lu « - »).
Questions verbatim : 1) L'ajustement affine parait-il judicieux ? Quelle prévision peut-on faire pour 2010 ? 2) Déterminer les coordonnées du point moyen G. 3) Cliquer sur le graphique pour faire apparaître les données sélectionnées et à l'aide du curseur ne sélectionner que les données depuis 1995, recopier l'équation de la droite de régression obtenue et calculer la prévision pour 2010 ? 4) Refaites le même travail de la 3ème question pour les données depuis 1999. Quel semble être le meilleur ajustement ?

##### Avec l'ordinateur — Activité 2 (p.223) — indice du coût de la construction (tableur)
Texte : « On s'intéresse à l'indice du coût à la construction dans un pays industrialisé de 1960 à 2000, base 100 en 1953. L'évolution est donnée par le graphique ci-contre. On se propose de chercher une droite qui approche au mieux ce nuage de points. On se fixe pour critère que la somme des carrés des écarts de la valeur réelle à la valeur obtenue par le modèle soit la plus petite possible. »
Nuage (étiquettes imprimées) : (1960 ; 142), (1965 ; 187), (1970 ; 222), (1975 ; 355), (1980 ; 592), (1985 ; 837), (1990 ; 950), (1995 ; 1017), (2000 ; 1098) (ordonnées graduées 0-1200 de 200 en 200).
Questions verbatim : 1- a) Reproduire ce nuage de points dans un repère orthogonal. b) Calculer les coordonnées du point moyen G. 2- On a essayé trois droites (AB), D et Δ, à l'aide d'un tableur. a) D'après ce tableaux quels sont les points A et B ? Tracer la droite (AB) sur le graphique et déterminer son équation réduite. b) La droite Δ passe par le point moyen et à pour coefficient directeur 25. Déterminer son équation réduite et tracer cette droite. c) Déterminer l'équation de la droite D passant par le point moyen et de coefficient directeur 27.5. Tracer D. d) En appliquant les formules données, compléter les valeurs manquantes en cases bleues. e) Calculer et comparer les sommes des écarts suivant le critère fixé. Quel est le meilleur ajustement ?
Feuille de calcul imprimée (A1 « Indice du coût à la construction base 100 en 1953 » ; A2 « écart : différence entre l'indice et l'ordonnée sur la droite »), lue à l'image (agrandie 220 dpi). Colonnes : année · indice · droite(AB) · (écart)² · droite D · (écart)² · delta · (écart)².
| année | indice | droite(AB) | (écart)² | droite D | (écart)² | delta | (écart)² |
|---|---|---|---|---|---|---|---|
| 1960 | 142 | 142 | 0 | 50 | 8489 | 100 | 1764 |
| 1965 | 187 | 261,5 | 5550 | 187 | 0 | 225 | 1444 |
| 1970 | 222 | 381 | 2581 | 325 | 10595 | 350 | 16384 |
| 1975 | 355 | 500,5 | 21170 | 462 | 11549 | 475 | 14400 |
| 1980 | 592 | 620 | 784 | 600 | 64 | 600 | 64 |
| 1985 | 837 | 739,5 | 9506 | 738 | 9894 | 725 | 12544 |
| 1990 | 950 | (case bleue vide) | (vide) | (vide) | (vide) | (vide) | (vide) |
| 1995 | 1017 | 978,5 | 1482 | 1013 | 19 | 975 | 1764 |
| 2000 | 1098 | 1098 | 0 | 1150 | 2718 | 1100 | 4 |
Ligne 13 : B13 = 5400 ; cases « somme » en bleu vides (colonnes D, F, H). Moyennes (A16:B17) : 1980 et 600. Tableau des coefficients : droite (AB) coef 23,9 ; D coef 27,5 ; delta 25. Formules imprimées : C5 = $F$16*(A5-$A$4)+$B4 ; E5 = $F$17*(A5-$A$17)+$B$17 ; G5 = $F$18*(A5-$A$17)+$B$17 ; F16 = (B12-B4)/(A12-A4) ; F17 = DROITEREG(B4:B12; A4:A12) ; F18 = 25 (valeur choisie).

---
#### EXERCICES ET PROBLÈMES (p.224-235) — énoncés verbatim, aucun corrigé dans le manuel

**1- (QCM) (p.224)** « Les questions se rapportent à la série statique à deux variables ci-contre. » 
| x_i | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| y_i | 1.9 | 3.2 | 4.1 | 4.9 |
« Une seule des réponses proposées est exacte » — colonnes a, b, c :
- Q1. Le point moyen du nuage associé à cette série a pour coordonnées… (valeurs arrondies à 10⁻¹ près) : a (3.5 ; 2.5) · b (10 ; 14) · c (2.5 ; 3.5).
- Q2. La covariance de cette série est égale à : a 1,2 · b 31,05 · c V(x).V(y).
- Q3. Avec une calculatrice, on trouve pour équation de la droite de régression de y en x : (avec les coefficients arrondis au centième) : a y =1.1 x +0.96 · b y =0.96 x +1.1 · c x =0.96 y +1.1.
- Q4. Avec une calculatrice, on trouve pour équation de la droite de régression de x en y : (avec les coefficients arrondis au centième) : a x = 1.04 y-1.15 · b y = 1.02 x -1.07 · c x = 1.02 y-1.07.
- Q5. Avec une calculatrice, on trouve pour coefficient de corrélation linéaire entre x et y : a r =0.99 · b r ≈ 0.99 · c r ≈ -0.99.
- Q6. pour cette série, l'ajustement affine par la méthode des moindres carrés… : a n'est pas justifié · b est justifié · c est parfois justifié, mais parfois ne l'est pas.

**2- (p.224)** « Calculer la covariance de chacune des deux séries suivantes : »
| x_i | 20 | 25 | 30 | 35 | 40 |
|---|---|---|---|---|---|
| y_i | 1.1 | 2.4 | 6.5 | 11 | 8 |

| x_i | -4 | -2 | -1 | 0 | 5 |
|---|---|---|---|---|---|
| y_i | -3.5 | -2.5 | -1.5 | 4.5 | 10 |

**3- (p.225)** « Le tableau suivant indique le montant des frais de publicité et celui du chiffre d'affaires, en DT, communiqués par une entreprise et pour chacun des six premiers mois de l'année 2006. »
| Frais x_i | 10 000 | 12 000 | 15 000 | 15 000 | 16 000 | 20 000 |
|---|---|---|---|---|---|---|
| Chiffre d'affaires y_i | 203 000 | 220 000 | 210 000 | 250 000 | 280 000 | 300 000 |
« On pose $x'_i=\frac{x_i-10\,000}{1\,000}$ et $y'_i=\frac{y_i-200\,000}{10\,000}$. » 1) Calculer σ_x', σ_y' et cov(x', y'). 2) En déduire σ_x, σ_y et cov(x, y).

**4- (p.225)** « Considérons la série statique à deux variables (x_i , y_i) pour i =1, 2,3,…, 5, suivant : »
| x_i | 5050 | 5080 | 5130 | 5150 | 5220 |
|---|---|---|---|---|---|
| y_i | 309 | 315 | 326 | 334 | 346 |
1- Placer, dans un repère orthogonal, le nuage de points A_i(x_i ; y_i). 2- a) Calculer le coefficient de corrélation de cette série. b) Un ajustement affine est-il justifié ? 3- a) Tracer la droite d de régression de y en x. b) Calculer la somme S des carrés des résidus par rapport à d.

**5- (p.225)** a) Dans chacun des cas ci-dessous placer les points A_i(x_i ; y_i). b) Expliquer pour quoi un ajustement affine est justifié. c) Tracer la droite de régression de y en x. d) Tracer la droite de régression de x en y.
❶ | x_i | 0.75 | 0.3 | 0.16 | 0.8 | 0.57 | 0.43 | / | y_i | 0.8 | 0.95 | 0.9 | 0.7 | 0.8 | 0.85 |
❷ | x_i | 8 | 10 | 12 | 14 | 16 | 18 | / | y_i | 9 | 11 | 13 | 13 | 14 | 16 |
« Pour ❸ et ❹, calculer à la main les coefficients a et b de la droite de régression de y en x, ainsi que le coefficient de corrélation linéaire r, puis contrôler les résultats obtenus avec une calculatrice. »
❸ | x_i | 0 | 2 | 4 | 6 | 8 | / | y_i | 1 | 3 | 4 | 5 | 9 |
❹ | x_i | -3 | -2 | -1 | 0 | 1 | 2 | / | y_i | 3 | 2 | 1 | 1 | -0.5 | -1.5 |

**6- (p.226)** « On donne la série statistique double suivante où α remplace y_5. »
| x_i | 1.2 | 1.4 | 1.6 | 1.8 | 2 |
|---|---|---|---|---|---|
| y_i | 13 | 12 | 14 | 16 | α |
« Par la méthode des moindres carrés on a obtenu une équation de la droite d de régression de y en x, à savoir y = 9x + 0.6. En déduire la valeur de α. »

**7- (Indicateur de développement) (p.226)** « Le tableau suivant indique, pour 1992, le rang occupé dans le monde par un pays donné, en fonction de son Indicateur de Développement Humain (IDH) d'une part et de son Produit Naturel Brut (PNB) par habitant. Ainsi, L'Egypte occupe le 110ième rang dans le monde pour l'IDH et le 122ième rang pour le PNB »
| Pays | Rang IDH | Rang PNB par hab. |
|---|---|---|
| Allemagne | 11 | 12 |
| Corée du sud | 32 | 36 |
| Égypte | 110 | 122 |
| Émirats A. Unis | 62 | 10 |
| États-Unis | 8 | 9 |
| Ethiopie | 161 | 171 |
| France | 6 | 13 |
| Japon | 6 | 13 |
| Pakistan | 132 | 140 |
| Royaume-Uni | 10 | 19 |
| Salvador | 112 | 97 |
| Sénégal | 143 | 114 |
« On note x_i le i-ème terme de la colonne « rang IDH » et y_i le i-ème terme de la colonne « rang PNB par hab. ». » 1) Représenter le nuage de point A_i(x_i ; y_i). 2) Calculer le coefficient de corrélation linéaire entre x et y. 3) Donner une équation de la droite régression de y en x. 4) Donner une équation de la droite régression de x en y. 5) Estimer le rang IDH d'un pays classé 50° pour son PNB par habitant.

**8- (Un enfant qui promet) (p.226-227)** « Monsieur Youssef est un papa heureux. Son fils bénéficie d'une excellente santé. Il a noté son poids (en kg) à chacun de ces anniversaires. »
| Âge x_i (en année) | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|
| Poids y_i | 22 | 24 | 28 | 34 | 42 | 51 |
« Soucieux de l'avenir, Youssef souhaiterait avoir une idée de l'évolution du poids de son héritier. Aidons-le. » 1-Représenter cette série par un nuage de point (un centimètre pour un an en abscisse, 1 cm pour 4 kg en ordonnées). 2-Les points ne semble pas alignées, mais donnent plutôt l'impression d'appartenir à un parabole. Poser $z_i=\sqrt{y_i}$ et compléter le tableau suivant en arrondissant à 10⁻² près : [tableau x_i = 7, 8, 9, 10, 11, 12 ; z_i vide] a) Sur un autre graphique, représenter les points de coordonnées (x_i ; z_i). Calculer le coefficient de corrélation linéaire entre x et z. b) Donner, par la méthode des moindres carrés, une équation de la droite de régression de z en x. 3-En utilisant cette droite, calculer quel pourrait être le poids de l'héritier à 20 ans. Youssef doit-il réellement se faire du souci ?

**9- (De l'hyperbole à la droite) (p.227)** « Le tableau ci-dessous donnes la charge maximale y_i, en tonne, qu'une grue peut lever pour une longueur x_i, en mètres, de la flèche. »
| x_i | 18.5 | 18 | 19.8 | 22 | 25 | 27 | 29 | 32 | 35 | 39 | 41.7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| y_i | 10 | 9 | 8 | 7 | 6 | 5.5 | 5 | 4.5 | 4 | 3.5 | 3.2 |
1- Les valeurs numériques dans cette question seront données à 10⁻² près. a) Représenter le nuage de points M_i(x_i ; y_i) dans un repère orthogonal (O ; i ; j) d'unité 1 cm pour 2 mètres en abscisse et 1 cm pour une tonne en ordonnée. b) Calculer le coefficient de corrélation linéaire entre x et y. c) Déterminez une équation de la droite de régression de y en x par la méthode des moindres carrés. Construire cette droite sur le graphique précédent. d) Utiliser cette équation pour déterminer la charge maximale que peut lever la grue avec une flèche de 26 mètres. 2-on pose $z_i=\frac{1}{y_i}$. a) Recopier et compléter le tableau suivant (les z_i seront arrondis à 10⁻³ près) : [x_i = 18.5, 18, 19.8, 22, 25, 27, 29, 32, 35, 39, 41.7 ; z_i = 0.100, puis cases vides]. b) Déterminer le coefficient de corrélation linéaire entre x et z, puis une équation de la droite de régression de z en x par la méthode des moindres carrés (les résultats numériques seront arrondis à 10⁻⁴ près). c) En se fondant sur les résultats obtenus à la question 2.b. calculer la valeur de z correspondant à x =26 ; en déduire la charge maximale que peut lever la grue avec une flèche de 26 mètres. d) Ce résultat paraît-il plus satisfaisant que celui de 1.d ? Pourquoi ?

**10- (p.228)** « Considérons la série statistique suivante : »
| x_i | 1/2 | 2/3 | 1 | 3/2 | 2 | 3 |
|---|---|---|---|---|---|---|
| y_i | 2 | 3/2 | 1 | 2/3 | 1/2 | 1/3 |
1- a) Représenter, dans un repère orthogonal, le nuage des points A_i de coordonnées (x_i ; y_i). b) La forme de ce nuage incite-t-elle à un ajustement affine ? 2-Trouver le coefficient de corrélation linéaire entre x et y. Ce coefficient confirme-t-il la réponse précédente ? 3-En fait, vérifier que tous les points A_i sont sur l'hyperbole d'équation y = 1/x. 4-On complète la suite initiale par les données (1/10 ; 10) et (10 ; 1/10). Calculer le coefficient de corrélation linéaire de cette nouvelle série statique. Interpréter votre résultat.

**11- (p.228)** « Soit une série (x_i ; y_i) à deux variables, la méthode des moindres carrés a permis de déterminer des équations des droites d de régression de y en x et d' de régression de x en y. » 1- d : y = 1,3x − 3.4 ; d' : x = 0,36y + 1. a) Tracer ces deux droites. b) Calculer le coefficient de corrélation linéaire entre x et y. 2- Est-il possible d'avoir ? d : y = 0,8x + 7,1 et d' : x = 3y − 1.

**12- (Sans connaître la série) (p.228)** « Pour une série (x_i ; y_i) (avec i =1, 2,3,…,5) à deux variables. La méthode des moindres carrés a permis de trouver : L'équation de la droite d de régression de y en x : y = −0,7x + 5,6. L'équation de la droite d' de régression de x en y : y =−0,8x+2 [sic]. » 1- a) Calculer les coordonnées du point moyen associé à cette série. b) Déduisez –en les valeurs de $\sum_{i=1}^{5}x_i$ et $\sum_{i=1}^{5}y_i$. 2-On sait de plus que $\sum_{i=1}^{5}x_i^2=8130$. En déduire cov(x, y) puis $\sum_{i=1}^{5}x_iy_i$ et $\sum_{i=1}^{5}y_i^2$.

**13- (p.228-229)** « En prévision du lancement d'un nouveau produit une société a effectué une enquête auprès de clients éventuels pour fixer le prix de vente de ce produit. Les résultats sont donnés dans le tableau ci-dessous : »
| Prix x_i de vente en (DT) | 9 | 10 | 11 | 12 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|
| Nombre y_i d'acheteurs éventuels | 180 | 160 | 150 | 130 | 100 | 90 | 80 | 70 |
1- Représenter graphiquement le nuage de points M_i(x_i, y_i) unité 1cm sur l'axe des abscisses et 1cm pour 10 unités sur l'axe des ordonnées. 2- a) Calculer les coordonnées du point moyen G_1 des quatre premiers Points, puis les coordonnées du point moyen G_2 des quatre derniers points. Placer ces points sur le graphique et tracer la droite (G_1G_2). b) On admet que la droite (G_1G_2) est une droite d'ajustement du nuage de points. Estimer graphiquement le prix maximum pour qu'il y ait au moins 50 acheteurs potentiels. 3- a) Justifier qu'une équation de la droite (G_1G_2) est (y = −14x + 302). b) En déduire : ❖ Le nombre d'acheteurs que l'on peut prévoir si le prix de vente est fixé à 13 DT. ❖ Le prix de vente pour que le nombre d'acheteurs potentiels soit supérieur ou égal à 250.

**14- (p.229)** « On considère la série statistique double donnant le chiffre d'affaire d'une entreprise en millions de dinars : »
| Année | 1980 | 1985 | 1990 | 1995 | 1998 | 2000 | 2003 | 2006 |
|---|---|---|---|---|---|---|---|---|
| Rang de l'année x_i | 0 | 5 | 10 | 15 | 18 | 20 | 23 | 26 |
| Chiffre d'affaires y_i | 1.3 | 1.6 | 1.7 | 2.1 | 2.2 | 2.4 | 2.5 | 2.7 |
1- Déterminer par la méthode des moindres carrés une équation de la droite d'ajustement de y en x. 2- a) Donner le chiffre d'affaires estimé en 1992. b) Déterminer l'année où le chiffre d'affaires prévu dépassera 3 millions dinar.

**15- (p.229-230)** « Une entreprise a réalisé un emprunt de 280 000 DT pour l'achat d'une nouvelle machine. A la fin de chaque mois on note dans le tableau suivant le montant des bénéfices cumulés (En milliers de dinars) réalisés depuis l'acquisition de la nouvelle machine. »
| Rang du mois x_i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Montant des bénéfices cumulés y_i | 28 | 40 | 51 | 65 | 78 | 84 | 89 | 98 |
1- a) Représenter dans un repère orthogonal le nuage de points associé à la série double (x_i, y_i) (On prendra 2cm pour 1 mois sur l'axe des abscisses et 2cm pour 10 000 DT sur l'axe des ordonnées). b) Ce nuage permet-il d'envisager un ajustement affine ? c) Donner l'équation y = ax + b de la droite D des moindres carrés (arrondir les coefficients au centième). Construire la droite D dans le repère précédent. d) A partir de quel mois l'emprunt sera –il amorti par lés bénéfices cumulés réalisés depuis l'acquisition de la nouvelle machine ? 2- L'expérience d'une évolution linéaire des bénéfices semble trop optimiste. On effectue alors le changement de variable $x'=\sqrt{x}$. a) Calculer les valeurs x'_i (arrondies au centième). b) La droite D' des moindres carrés de cette nouvelle série (x'_i, y'_i) à pour équation y = 39.45x' − 13.80. En déduire une expression de y en fonction de x. c) A partir d'un tableau de valeurs, tracer dans le repère précédent la courbe C obtenue avec cette expression. Selon ce nouvel ajustement, à partir de quel mois l'emprunt sera –il amorti par lés bénéfices cumulés réalisés depuis l'acquisition de la nouvelle machine ? 2-Quel est le meilleur ajustement ? Justifier. [numérotation imprimée : « 2- » deux fois]

**16- (p.230)** « Dans un magasin le nombre annuel de ventes d'un appareil électroménager, relevé pendant 6 années, est donné par le tableau suivant : »
| Année | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 |
|---|---|---|---|---|---|---|
| Rang de l'année x_i | 1 | 2 | 3 | 4 | 5 | 6 |
| Nombre d'appareils y_i | 623 | 712 | 785 | 860 | 964 | 1073 |
1- a) Représenter dans un repère orthogonal le nuage de points M_i(x_i, y_i) en prenant comme unités graphiques: 2cm pour 1 rang en abscisses et 1cm pour 50 appareils en ordonnées et en commençant la graduation à 600 sur l'axe des ordonnées. b) Calculer, en donnant les résultats arrondis à 10⁻², les coordonnées du point moyen G du nuage et placer ce point sur le graphique. 2- a) Calculer en donnant les résultats arrondis à 10⁻², les coordonnées du point moyen G_1 du nuage formé par les points M_1, M_2 et M_3, puis les coordonnées du point moyen G_2, du nuage formé par les points M_4, M_5, et M_6. b) Placer les points G_1 et G_2 sur le graphique et déterminer, avec des coefficients arrondis à 10⁻², une équation de la droite (G_1 G_2). c) En utilisant cette droite comme droite d'ajustement, déterminer le nombre d'appareils que prévoie de vendre en 2010. 3-On sait maintenant que le nombre d'appareils vendus en 2002 est de 1125. a) Ajouter le point M_7(7,1125) sur le graphique précédent. b) On considère alors le nouveau nuage formé des points M_i, 2 ≤ i ≤ 7 (le nombre annuel de ventes de l'année 1996 n'est pas pris en compte). Donner une équation de la droite d'ajustement affine de y en x par la méthode des moindres carrés (les coefficients sont arrondis à 10⁻²). c) En utilisant cet ajustement quel nombre d'appareils peut-on prévoir vendre en 20010 ? [sic : « 20010 »]

**17- (p.230-231)** « Lors d'une période de sécheresse, un agriculteur relève la quantité totale d'eau (en m³) utilisée par son exploitation depuis le premier jour et donne le résultat suivant : »
| Nombre de jours écoulées (x_i) | 1 | 3 | 5 | 8 | 10 |
|---|---|---|---|---|---|
| Volume utilisé (en m³) y_i | 2.25 | 4.3 | 8 | 17.5 | 27 |
« Le plan est muni d'un repère orthogonal. On prendra pour unité sur l'axe des abscisses 1cm pour 1 jour et sur l'axe des ordonnées 0.5 cm pour un mètre cube. » 1- Représenter le nuage de points associé à la série statistique (x_i, y_i). 2- Donner l'équation de la droite D de régression de y en x obtenue par la méthode des moindres carrés sous la forme y = αx + β où α et β sont les arrondis à 10⁻² près. Représenter la droite D sur le graphique. 3- Le nuage de points permet d'envisager un ajustement par la parabole P qui passe par les points A(1; 2.25) ; B(10; 27) et qui à pour équation y = ax² + b où a et b sont des réels. a) Déterminer a et b, et donner l'équation de la parabole P. b) Représenter la parabole P. 4- Dans cette question on compare les deux ajustements à l'aide du tableau suivant : 
| x_i | 1 | 3 | 5 | 8 | 10 | |
|---|---|---|---|---|---|---|
| y_i | 2.25 | 4.3 | 8 | 17.5 | 27 | |
| [y_i − (αx_i + β)]² | | | | | | Total T1 |
| [y_i − (ax_i² + b)]² | | | | | | Total T2 |
« Compléter le tableau et donner les arrondis à 10⁻¹ près des deux totaux T1 et T2. Ces deux totaux évaluent pour chaque ajustement la somme des résidus. En déduire l'ajustement qui parait le mieux adapté. »

**Problème 1 (p.231-232)** « Le tableau suivant donne la population d'une ville nouvelle entre les années 1970 et 2000. »
| Année | 1970 | 1975 | 1980 | 1985 | 1990 | 1995 | 2000 |
|---|---|---|---|---|---|---|---|
| Rang de l'année x_i | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
| Population en milliers d'habitants y_i | 18 | 22 | 25 | 29 | 36 | 42 | 52 |
1- Représenter le nuage de points associé à la série statistique (x_i ; y_i) dans un repère orthogonal. (0.5 cm représente une année en abscisse et 1 cm représente 5 milliers d'habitants en ordonnée). Calculer les coordonnées du point moyen et placer ce point. 2- **Un ajustement affine :** a) Déterminer l'équation y = ax + b de la droite d'ajustement affine de y en x par la méthode des moindres carrés (les coefficients a et b seront arrondis au centième). b) Tracer cette droite sur le graphique. c) Déduire de cet ajustement une estimation de la population en 2005, arrondis au millier le plus proche. d) Calculer à la calculatrice la somme des carrés des résidus $S_1=\sum[y_i-(ax_i+b)]^2$. (On donnera le résultat arrondi à l'unité près.) 3- **Un deuxième ajustement :** On considère l'ajustement obtenu par la branche de parabole de la parabole d'équation $y=0.02x^2+0.5x+18$. a) Dans le repère précédent, sans étudier la fonction correspondante, tracer cette branche de parabole pour x appartenant à l'intervalle [0;30]. On pourra utiliser le tableau de valeurs ci-dessous que l'on recopiera et que l'on complètera : [x = 0, 5, 10, 15, 20, 25, 30 ; y = 0.02x²+0.5x+18 : cases vides]. b) Déduire de ce nouvel ajustement une estimation de la population en 2005, arrondis au millier le plus proche. c) Calculer la somme des carrés des résidus $S_2=\sum[y_i-(0.02x_i^2+0.5x_i+18)]^2$ pour ce nouvel ajustement. 4- **Comparaison des deux ajustements :** a) Des deux ajustements quel est le plus pertinent ? (La réponse sera justifiée) b) On sait maintenant que la population en 2005 était de 63 000 habitants. Calculer le pourcentage des erreurs commises en utilisant les prévisions trouvées avec chacun des deux ajustements précédents.

**Problème 2 (p.232-233)** « Au cours d'une séance d'essais, un pilote automobile doit, quand il reçoit un signal sonore dans son casque, arrêter le plus rapidement possible son véhicule. Au moment du top sonore, on mesure la vitesse v_i (en km/h) de l'automobile, puis la distance y_i (en m) nécessaire pour arrêter le véhicule. Pour sept expériences on a obtenu les résultats suivants : »
| Vitesse v_i | 20 | 43 | 62 | 80 | 98 | 115 | 130 |
|---|---|---|---|---|---|---|---|
| Distance d'arrêt y_i | 3.5 | 20.5 | 35.9 | 67.8 | 101.2 | 135.8 | 168.5 |
1- a) Dans un repère orthogonal, représenter le nuage de points de coordonnées (v_i, y_i) avec pour unités 1cm pour 10km/h sur l'axe des abscisses et 1cm pour 10m sur l'axe dés ordonnées. b) Tracer une parabole autour de laquelle ces points semblent se répartir. 2-Posons $x_i=v_i^2$. Reproduisez et complétez le tableau suivant : [x_i : 7 cases vides ; y_i : 101.2, 3.5, 20.5, 35.9, 67.8, 135.8, 168.5 — l'ordre imprimé de la ligne y_i diffère de celui du tableau initial, voir Notes]. a) Dans un repère orthogonal construisez le nuage des points de cordonnées [sic, R7 : « cordonnées » imprimé] (x_i, v_i) associé à cette nouvelle série double. b) Calculer le coefficient de corrélation linéaire entre x et y. Un ajustement affine est-il plausible ? Donnez l'équation de la droite de régression de y en x par la méthode des moindres carrés. Déduisez une formule qui donne une estimation de y en fonction de v. c) A l'aide de la formule précédente, estimez la vitesse v de ce véhicule lorsque sa distance d'arrêt est 180m. d) Estimez la distance d'arrêt de ce véhicule s'il roule à 150 km/h. e) Le manuel du code de la route donne pour calculer la distance d'arrêt (en m) la méthode suivante (prendre le carré de la vitesse exprimée en dizaines de km/h). Comparer le résultat obtenu au d) à celui que l'on obtiendrait avec cette méthode.

**Problème 3 (p.233)** « Le prix de vente des terrains à bâtir dans la même cité d'une ville est donné par le tableau suivant : »
| Année | 1980 | 1985 | 1987 | 1990 | 1995 | 1997 | 2000 |
|---|---|---|---|---|---|---|---|
| Rang de l'année x_i | 0 | 5 | 7 | 10 | 15 | 17 | 20 |
| Prix du m² en DT y_i | 58,8 | 60,9 | 62,1 | 67,5 | 71,7 | 73 | 73,8 |
1) Quelle est, en pourcentage, l'augmentation du prix du m² entre 1980 et 2000 ? 2) Représenter le nuage de points M_i (x_i ; y_i) dans un repère orthogonal où 5 cm représentent 10 ans en abscisse, 5 cm représentent 10 francs en ordonnées. 3) Déterminer le point moyen G du nuage et le placer sur le graphique. 4) On considère que la position des points sur le graphique justifie un ajustement affine par la méthode des moindres carrés. Ecrire une équation de la droite d'ajustement affine de y en x, notée (D) [les coefficients sont arrondis à 0,01]. Tracer (D). 5) Estimer à 1000 DT près le prix d'un terrain de 1500m² en 2003.

**Problème 4 (p.233-234)** « La production d'une entreprise a été relevée depuis 1991. Les années ont été numérotées x_i avec x_1 = 1 en 1991. La production est exprimée en tonnes et notée y_i. »
| Année | 1991 | 1992 | 1993 | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| x_i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| y_i | 600 | 700 | 640 | 900 | 800 | 940 | 100 | 500 | 700 | 900 | 1100 | 1000 | 1200 | 1400 | 1360 |
1- a) Représenter le nuage de points M_i(x_i, y_i) associé à la série statistique double (S) ci-dessus. b) Au cours de l'année x, les installations de l'entreprise ont été détruites par un incendie, puis reconstruites. Indiquer quelle est l'année x et expliquer brièvement votre réponse. 2- Dans la suite du problème, on considère les trois séries statistiques : - La série initiale (S). - La série (S') obtenue en retirant les années 1997 ; 1998 ; et 1999. - La série (S'') comprenant les seules valeurs postérieures à l'année 1999 (cette dernière incluse dans (S'')). a) Les coefficients de corrélation des séries (S) et (S') arrondis à 10⁻² près sont respectivement 0.66 et 0.93. Quelle série doit-on privilégier ? Justifier. b) Par la méthode des moindres carrés, donner une équation de la droite de régression D de y en x pour la série (S') (les coefficients seront arrondis à 10⁻² près). c) Tracer cette droite sur la figure précédente quelle prévision de la production de l'entreprise peut on en déduire pour 2006 et 2007 ? 3- a) Calculer le coefficient de corrélation de la série (S''). b) Par la méthode des moindres carrés donner une équation de la droite de régression D' de y en x pour cette série (les coefficients seront arrondis à 10⁻² près). c) Tracer cette droite D' sur la figure précédente. Quelle prévision de la production de l'entreprise peut-on faire pour 2006 et 2007 ?

**Problème 5 (Coût et recette dans un marché non monopoliste) (p.234)** « A. Etude du coût : Le coût total du production d'un bien produit par une entreprise en concurrence est donné en milliers de DT par : $C(q)=0.1q^2+2q+60$, q étant le nombre de centaines d'unités produites, avec $q\in[5;40]$. » 1) Étudier le sens de variation de cette fonction sur [5;40]. Construire la courbe (𝒞) représentative de la fonction de coût total dans un repère orthogonal. 2) Résoudre algébriquement C(q) >150. Donner une interprétation du résultat.
« B. Etude de la recette et de bénéfice : Une étude statistique a permis d'estimer la recette en fonction de la quantité fabriquée q. Le tableau ci-dessous rend compte de cette étude. »
| Quantité q_i | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 |
|---|---|---|---|---|---|---|---|---|
| Recette y_i (en milliers de DT) | 15 | 90 | 135 | 170 | 190 | 200 | 230 | 240 |
1-Représenter les points M_i(q_i; y_i) dans le repère de la question A. 2-Au vu de ce nuage, on décide d'ajuster la recette par une fonction logarithme. Pour cela, on considère la série (t_i; y_i), où t_i = ln(q_i). a) Déterminer une équation de la droite de régression de y en t par la méthode des moindres carrés (les coefficients seront donnés à l'unité près). b) En déduire une relation entre y et q de la forme Y = a ln(q) + b. c) On pose R(q) = a ln(q) + b ; la fonction R, ainsi définie sur [5;40], modélise la fonction de la recette de l'entreprise pour ce bien. Estimer graphiquement pour quelles quantités produites l'entreprise réalise un profit. 3-On considère la fonction B définie sur [5;40] par B(q) = R(q) − C(q). a) Calculer B'(q). En déduire l'étude des variations de la fonction B sur [5;40]. b) Montrer que l'équation B(q) = 0 admet deux solutions q_0 et q_1, dont on donnera un encadrement à 0.1 près. c) En déduire le plus grand intervalle tel que, pour tout quantité produite de cet intervalle, l'entreprise réalise un profit.

**Problème 6 (Offre et demande) (p.235)** « D'après une étude de marché, l'offre d'un produit est donnée par f(x) = 0.9x, où x est le prix en centaines de DT, avec x ∈ [1;6] et f(x) est la quantité offerte, en millier d'objets. L'étude des intentions d'achat conduit à une estimation de la demande donnée par le tableau suivant : »
| Prix x_i | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Quantité y_i | 3 | 2 | 1.5 | 1 | 0.6 | 0.5 |
1-Dans le même repère orthogonal, tracer la représentation (𝒟) de la fonction d'offre et les points M_i(x_i; y_i) de l'estimation de la demande. Un ajustement affine de la demande est-il justifié ? 2-On pose z_i = ln(y_i). a) Déterminer une équation de la droite de régression de z en x. Donner les coefficients à 0.01 près. b) En déduire une relation entre x et y de la forme y = Ke^{ax}. 3-On modélise la fonction de demande par la fonction g définie sur [1;6] par g(x) = Ke^{ax}. a) Etudier le sens de variation de la fonction g. Tracer la courbe représentative de g dans le même repère que la fonction d'offre. b) Soit h la fonction définie sur [1;6] par h(x) = g(x) − f(x). Etudier le sens de variation de h. Montrer que l'équation h(x) = 0 possède une unique solution x_0 dans [1;6]. Donner une valeur arrondie de x_0 à 0.01près. c) En déduire le prix d'équilibre, à un DT près, ainsi que le nombre d'objets que les producteurs doivent alors proposer sur le marché. Vérifier graphiquement.

---
#### MATH CULTURE (p.236)
Source citée : aucune source bibliographique imprimée ; seul auteur nommé : Francis Galton (1822-1911).
**1) Pour quoi droite de régression ? (verbatim)** « Francis Galton (1822-1911) a étudié d'éventuels liens entre la taille y_i d'un individu et celle x_i de son père. La droite qu'il est conduit à tracer pour ajuster le nuage des points de coordonnées (x_i, y_i) a un coefficient directeur positif et inferieur à 1. Cela signifie que les pères de grande taille ont (en général) des enfants de grande taille mais (en général) inferieur à celle de leur père : il y a régression du caractère (taille élevée) dans l'espèce ; d'où l'expression droite de régression. »
**2) Pour quoi (..... de y en x) ? (verbatim)** « x et y ne jouent pas le même rôle dans la définition de la droite de régression. Ceci explique la terminologie de y en x : elle précise que dans l'étude faite les x_i sont portés en abscisses et les y_i en ordonnées. »
**3) Mise en garde ! (verbatim)** « En fait, comme c'est toujours le cas pour une étude statistique d'un phénomène quel qu'il soit, c'est le spécialiste de la discipline concernée qui doit interpréter les résultats. D'une corrélation observée entre les variables on ne peut pas conclure à une liaison physique objective et encore bien moins à une dépendance causale. Un exemple classique est celui d'une enquête, réalisée en Angleterre de 1924 à 1937, révélant que le coefficient de corrélation entre le nombre de permis délivrés chaque année pour l'installation d'un poste de radio et le nombre des malades mentaux enregistrés pour 10 000 habitants valait 0.998, suggérant une relation quasi fonctionnelle. Une étude complémentaire de chacun des phénomènes s'imposait. Un autre exemple classique : le poids du nouveau-né croit avec l'âge de la mère. Une analyse plus fine montre que, si l'on prend uniquement des nouveaux nés de même rang de naissance on ne trouve pas de corrélation entre leur poids et l'age de leur mère. Mais le poids à la naissance croit avec le rang de la naissance .... lequel est évidement corrélé avec l'age de la mère, d'où la corrélation, qui n'est qu'apparente. Quant à savoir pourquoi le poids du nouveau né croit avec le rang de naissance .... ; C'est un problème complexe qui concerne les biologistes et les physiologistes. » (fin de page 236 = fin de la tranche)

---
#### VOCABULAIRE OFFICIEL (termes exacts du manuel)
série statistique double ; nuage de points ; point moyen G($\bar x$, $\bar y$) ; effectifs marginaux ; covariance (cov(x, y)) ; variance V(x) ; écart type σ_X, σ_Y ; ajustement (affine, parabolique, polynomial / quadratique, homographique, logarithmique, exponentiel) ; « on ajuste ce nuage par une droite » ; méthode des moindres carrés ; somme des carrées [sic] des résidus ; droite de régression de y en x / de x en y ; équation réduite ; méthode de Mayer, droite de Mayer ; coefficient de corrélation linéaire r(x, y) ; corrélation faible / forte / très forte ; dépendance totale ; changement de variable ; prix d'équilibre ; offre, demande.

#### BORNES (déduites du texte, p.201-236)
INCLUS : covariance (définition, formule de König cov = (1/n)Σx_iy_i − x̄ȳ, symétrie, cov(x,x)=V(x), P1 translation, P2 homothétie) ; ajustement affine par moindres carrés (droite de régression de y en x et de x en y, passe par G, a = cov/V(x), a' = cov/V(y), équation y = a(x − x̄) + ȳ) ; coefficient de corrélation r = cov/(σxσy), seuils 0,70 et 0,95, −1 ≤ r ≤ 1, |r|=1 ; méthode de Mayer ; ajustements non affines ramenés à un ajustement affine par changement de variable (X = ln x, Y = ln y, z = √y, z = 1/y, x = v², t = ln q) ; ajustement par parabole ou fonction homographique dont les coefficients se déterminent par passage par des points ; utilisation d'une calculatrice / d'un tableur (Excel 2003 : courbe de tendance, DROITEREG) ; prévisions (interpolation/extrapolation) ; étude de fonction pour le prix d'équilibre (f exponentielle, g affine, h = f − g, solution unique de h(x) = 0).
EXCLU / ADMIS : l'existence et l'unicité de la droite de régression est ADMISE (théorème « admis »), de même P1 et P2 ; les seuils 0,70/0,95 « dépassent le cadre du programme » ; −1 ≤ r ≤ 1 et le cas |r|=1 « démontrés et admis » ; aucune loi/inférence, aucune démonstration de la minimisation de S ; pas de rapport de corrélation ni de régression non linéaire directe (tout est ramené à du linéaire par changement de variable).
#### NOTIONS-CLÉS (≤ 8)
1. covariance et formule de calcul ; 2. effet d'un changement de variable affine sur cov (P1, P2) ; 3. droite de régression de y en x (passe par G, pente cov/V(x)) ; 4. droite de x en y (pente de x par rapport à y cov/V(y)) ; 5. coefficient de corrélation r et seuils ; 6. droite de Mayer ; 7. ajustement non affine par changement de variable (ln, √, 1/y, v²) ; 8. prévision et prix d'équilibre (offre/demande).

---
#### § NOTES

**Pages lues** : 36/36 (201 à 236), texte (`pdftotext`, pages 202-214 et 233, 235, 236 vérifiées en texte) + image 110 dpi de chacune. **Pages agrandies (170-220 dpi)** : p.203 (nuage Activité 3, 200 dpi), p.222 (feuille Excel, 220 dpi), p.223 (feuille de calcul, 220 dpi), p.228 (exercices 11-12, 190 dpi). p.201 : couverture, sans texte extractible.

**Coquilles imprimées (reproduites telles quelles)** :
- p.202 Act.2 : « de l'année 1998 à l'année 2004 » pour 12 valeurs (revenues) ; « revenues » pour revenus.
- p.203 Act.4 : « double caractères ». [R7 : supprimé « notation « y_i le centre de la classe C_i » alors que x est discret » : ce n'est pas une coquille, y est bien donné par classes et y_i en est le centre (image p.203).]
- p.206 : « Exemple » de l'encadré théorème ne contient aucune résolution.
- p.210 Act.1 : axe horizontal imprimé « 1994 1989 1999 2000 … » (ordre 1994/1989 inversé) ; questions numérotées « 1) » puis « 3) ». p.211 : fragment « ; » parasite au-dessus du graphique.
- p.213 : « ou' » pour « où », « somme des carrées des résidus ».
- p.214 : sur la figure du théorème, l'axe horizontal est étiqueté « y » à droite (devrait être x).
- p.218 Act.3 2-b : « de y en , on note a » (le mot « x » manque). [R7 : retiré « p.215 Act.3 » : le texte de p.215 est complet à l'image.]
- p.218 Act.3 : « dan le tableau », « deux fonctions affine » ; p.223 : « D'après ce tableaux ». [R7 : « une fonction affine » corrigé en « deux fonctions affine » (imprimé) ; retiré « p.220 Ex.4 : « sera » » : p.220 imprime « seront donnés », aucune coquille.]
- p.223 feuille de calcul : (écart)² de la droite (AB) pour 1970 imprimé **2581** ; (222−381)² = 25281 (coquille probable, 5 chiffres attendus). Les (écart)² des colonnes F et H : H cohérent ((142−100)² = 1764…) ; colonne F légèrement différente du recalcul (ex. (142−50)² = 8464 imprimé 8489 ; (1017−1013)² = 16 imprimé 19) : la droite D a vraisemblablement été calculée avec un coefficient non arrondi 27,5…, valeurs reproduites telles qu'imprimées.
- p.225 Ex.5 : « Expliquer pour quoi » [R7 : retiré « Ex.3 : « dans »/« 𝜎 » », aucune coquille imprimée à p.225 Ex.3] ; p.226 Ex.7 : titre « (Indicateur de développement) » avec parenthèse mal fermée, « Produit Naturel Brut » (PNB) ; Ex.8 « un parabole », « points ne semble pas alignées ».
- p.228 Ex.12 : la droite d' de régression de x en y est annoncée « y = −0,8x + 2 » (devrait être « x = −0,8y + 2 ») ; Ex.11 mélange virgule/point décimaux (« 1,3 x − 3.4 »).
- p.229 Ex.15 : numérotation « 2- » deux fois ; Ex.16 3-c : « 20010 » pour 2010.
- p.231 Pb.1 : « arrondis au millier » ; p.232 Pb.2 : le tableau « xi / yi » à compléter donne la ligne y_i dans l'ordre 101.2, 3.5, 20.5, 35.9, 67.8, 135.8, 168.5 (différent du tableau de l'énoncé : 3.5, 20.5, 35.9, 67.8, 101.2, 135.8, 168.5) ; question 2-a demande le nuage des points (x_i, v_i) alors que b) calcule r entre x et y (le nuage attendu semble (x_i, y_i)).
- p.233 Pb.3 : « 5 cm représentent 10 francs » (unité monétaire DT ailleurs). Pb.4 : y_i(1997) imprimé **100** (production 600…940 avant, 500, 700 après : valeur manifestement faible ; peut être volontaire, la question 1-b évoquant un incendie en 1997-1999).
- p.235 Pb.6 : « millier » pour milliers. p.236 : « Pour quoi », « inferieur », « evidement », « l'age ».

**Incohérences de chiffres entre rubriques** : (1) Les données « Population urbaine (%) » de Mayer Act.2 (p.217 : 1997 = 61.9, 2004 = 64.9) diffèrent de la colonne « Part (en %) » de la feuille Excel (p.222 : 1997 = 62, 2004 = 65) ; autres années identiques. (2) Exemple 1 (polynomial) : C(7,107) alors que le tableau donne 106,7 en x = 7 (approximation voulue, non commentée).
**Recomptes de totaux (hors manuel)** : Pour commencer Act.1 effectif total 524 ; Cours I Act.9 effectif total 51 ; Act.4 effectif total 40 ; B13 (p.223) = 5400 = somme des 9 indices (142+187+222+355+592+837+950+1017+1098), moyenne 600 = 5400/9, moyenne des années 1980 : cohérent. Exercice 1 : les 4 points ont pour moyennes 2,5 et 3,525 (les options Q1 imprimées : c « (2.5 ; 3.5) »). Moindres carrés de Cours II.2 Act.1 : $\bar x=11,4$, $\bar y=10,8$, V(x)=9,04, cov=5,28 donne a = 66/113, b = 468/113 : cohérent avec l'énoncé 6-a.
**`[?]` justifiés** : (a) p.203 Act.3, dernier point du nuage lu (≈ 555 ; ≈ 21), ni graduation ni valeur imprimée ; (b) p.211 Act.2, valeurs de prévision 2010 lues à l'œil sur un graphique sans étiquettes ; (c) p.212 Nuage 2, graduations verticales tronquées à l'impression ; (d) p.222, signe du terme constant de l'équation Excel « y = 0,3296x − 596,36 » lu « − » à 220 dpi (la valeur 0,3296×1990 − 596,36 ≈ 59,6 est cohérente avec le nuage, donc signe « − » confirmé).
**Pas de corrigé dans le manuel** : aucune des activités, aucun des exercices ni problèmes de ce chapitre n'est corrigé ; seuls résultats imprimés : « cov(x, y) ≈ 1.48 » (Act.7 p.208, pour la série du prix du poisson), r = 0.66 et 0.93 (Pb.4 2-a), 0.998 (Math culture), y = −14x + 302 (Ex.13), y = 39.45x' − 13.80 (Ex.15), y = 9x + 0.6 (Ex.6), droites des Ex.11-12, équations de f et g (Ex.4 de l'Exemple 4 : f(x)=e^{-1,41x+2,08}, g(x)=0,53x+1,10).

---

### Chapitre `m09-p237-272`

### m09 — Chapitre IX « Probabilités » (manuel Maths 4e éco-gestion, pp. 237-272)

Source : `222463P00.pdf`, pages PDF 237-272 (= pages imprimées). Page 237 = page de titre du chapitre : « Chapitre 9 — PROBABILITES. Pour commencer · Cours (Probabilité conditionnelle ; Variables aléatoires) · Avec l'ordinateur · Exercices et problèmes · Math culture ». Notation : $p(\bar A)$ = événement contraire de A ; « ∩ » intersection, « ∪ » réunion. `DT` = dinar tunisien.

---

#### 1. POUR COMMENCER (pp. 238-239)

##### Activité 1 (p.238) — répartition hommes/femmes par catégorie salariale
Situation : « Dans une entreprise, on s'intéresse à la répartition des hommes et des femmes selon les trois catégories salariales : ouvrier, agent et cadre. »

| | homme | femme | total |
|---|---|---|---|
| ouvrier | 34.1 % | 15.9 % | 50 % |
| Agent | 17.4 % | 12.6 % | 30 % |
| Cadre | 6.5 % | 13.5 % | 20 % |
| Total | 58 % | 42 % | 100 % |

(Totaux recomptés : lignes 50 / 30 / 20 ; colonnes 58 / 42 : exacts.)
« On choisit au hasard une fiche d'un employé et on considère les événements suivants : F : « la fiche choisie est celle d'une femme ». H : « … d'un homme ». O : « … d'un ouvrier ». A : « … d'un agent ». C : « … d'un cadre »..
Calculer les probabilités des évènements F, H, O, A, C, C ∩ F, O ∩ F, A ∩ H et F ∩ O. »
Corrigé : non donné.

##### Activité 2 (p.238) — offre d'emploi, gestionnaire de production
« Une société lance une offre d'emploi pour recruter un gestionnaire de production. 35 % des personnes répondant à cette offre ont une expérience professionnelle, 25 % ont un diplôme de gestionnaire et 15 % ont à la fois un diplôme de gestionnaire et une expérience professionnelle. On choisit au hasard le fichier d'un candidat. Quelle est la probabilité d'obtenir :
1) Un candidat ayant une expérience professionnelle ou un diplôme de gestionnaire ?
2) Un candidat sans diplôme de gestionnaire et sans expérience professionnelle ?
3) Un candidat ayant une expérience professionnelle et sans diplôme de gestionnaire ?
4) Un candidat ayant seulement une expérience professionnelle ou ayant seulement un diplôme de gestionnaire ? »

##### Activité 3 (p.238) — urne rouges/vertes numérotées
« Une urne contient cinq boules rouges numérotées 0, 0, 1, 2 et 3 et quatre boules vertes numérotées 0, 0, 2 et 3. Toutes les boules sont indiscernables au toucher.
1) Une épreuve consiste à tirer simultanément et au hasard trois boules de l'urne. Calculer la probabilité de chacun des évènements suivants :
 A « Obtenir une seule boule rouge » ; B « Obtenir une seule boule portant le numéro 0 » ; C « Obtenir une seule boule rouge portant le numéro 0 »
2) On tire au hasard, successivement sans remise deux boules de l'urne. Calculer la probabilité de chacun des évènements suivants :
 A' « Obtenir une seule boule portant un numéro pair » ; B' « La première boule tirée est rouge ». »

##### Activité 4 (p.239) — dé lancé trois fois
« On lance trois fois de suite un dé équilibré dont les faces sont marquées de 1 à 6. Calculer la probabilité de chacun des événements suivants : A « la face marquée 6 apparaît une seule fois » ; B « la face marquée 6 apparaît au moins une fois » ; C « la face marquée 6 n'apparaît pour la première fois qu'au troisième lancer » »

##### Activité 5 (p.239) — urne 3 blanches / 5 noires
« Une urne contient trois boules blanches et cinq boules noires.
1) On tire au hasard, successivement et sans remise deux boules de l'urne. Calculer la probabilité d'obtenir : a) Une boule blanche puis une boule noire. b) Une boule noire puis une boule blanche. c) Deux boules de couleurs différentes.
2) L'épreuve consiste maintenant à tirer successivement et au hasard deux boules de l'urne de la manière suivante : * Si la boule tirée est blanche, on la remet dans l'urne, puis on tire une seconde boule. * Si la boule tirée est noire, on la garde, puis on tire une seconde boule de l'urne.
Calculer la probabilité d'obtenir : a) Une boule blanche puis une boule noire. b) Une boule noire puis une boule blanche. c) Deux boules de couleurs différentes. »

##### Activité 6 (p.239) — fonctionnaire et quatre feux tricolores
« Pour aller au lieu de travail, un fonctionnaire traverse avec sa voiture une grande avenue où sont installés quatre feux de circulation tricolores et deux à deux indépendants : orange, rouge et vert. Le fonctionnaire doit s'arrêter chaque fois que le feu n'est pas vert. On suppose l'équiprobabilité d'apparition de chaque couleur dans chaque feu.
1) Calculer la probabilité de chacun des événements suivants : A : « Le fonctionnaire s'arrête aux quatre feux ». B : « Le fonctionnaire ne s'arrête pas. ». C : « Le fonctionnaire s'arrête au premier et au troisième feu ». D : « Le fonctionnaire ne s'arrête qu'au premier et au troisième feu ».
2) Chaque fois que le fonctionnaire s'arrête au moins deux fois, il arrive au lieu de travail en retard. Calculer la probabilité pour qu'il ne soit pas en retard, sachant qu'il sort de sa maison tous les jours à la même heure. »

---

#### 2. COURS — I. Probabilité conditionnelle (pp. 240-248)

##### 1) Probabilité conditionnelle et formule des probabilités composées

**Activité 1 (p.240) — RTT, 500 salariés** : « Les 500 salariés d'une entreprise sont classés en deux catégories : cadre et employé. Au cours de négociations sur la Réduction du Temps du Travail (RTT), on propose aux salariés deux formules suivantes : Formule F1 : une RTT de 30 minutes par jour de travail. Formule F2 : une RTT de 12 jours de travail par an. Une enquête a été réalisée auprès de tous les salariés de l'entreprise, chacun remplit une fiche mentionnant son statut (cadre ou employé) et son choix de RTT. Les résultats sont indiqués dans le tableau ci-dessous : »

| | Cadre | employé | Total |
|---|---|---|---|
| Salarié | 10 | 300 | (vide) |
| Salarié | 40 | 150 | (vide) |
| Total | (vide) | (vide) | 500 |

(Les deux lignes sont toutes deux libellées « Salarié » à l'impression : le libellé F1 / F2 manque, voir § Notes. 10+300+40+150 = 500.)
« 1- Recopier le tableau ci-dessus et remplir les cases vides.
2- On extrait, au hasard, une fiche d'un salarié. On considère les évènements suivants : C : « Le salarié choisi est un cadre » ; E : « … un employé » ; F1 : « Le salarié choisi préfère la formule F1 » ; F2 : « … la formule F2 » ; A : « Le salarié choisi préfère la formule F1 sachant que c'est un cadre » ; B : « Le salarié choisi préfère la formule F2 sachant que c'est un employé ».
a) Calculer les probabilités des événements C, E, F1, F2, A et F1 ∩ C.
b) Comparer p(A) et p(F1 ∩ C)/p(C), p(B) et p(F2 ∩ E)/p(E). »

**Définition (probabilité conditionnelle)** (encadré) : « Soit E l'ensemble des issues d'une expérience aléatoire et p une probabilité sur E. Soit A un événement de probabilité non nulle et B un événement quelconque. On appelle probabilité conditionnelle de B sachant A, le réel noté p(B/A) ou p_A(B) et défini par : p(B/A) = p(A ∩ B) / p(A) »

**Remarque** : « Dans le cas où p(B) = 0, on convient de poser p(A/B) = 0. » (tel qu'imprimé, voir § Notes)

**Activité 2 (pp.240-241) — urne blanches/noires numérotées** : « Une urne contient quatre boules blanches numérotées 1, 1, 2, 2 et cinq boules noires numérotées 1, 1, 1, 1, 2. Toutes les boules sont indiscernables au toucher. On tire au hasard et simultanément trois boules. Calculer la probabilité de chacun des événements : A : « Obtenir exactement deux boules blanches » ; B : « Obtenir trois boules portant le numéro 1 » ; C : « Obtenir exactement deux boules blanches sachant qu'on a obtenu trois boules portant le numéro 1 » ; D : « Obtenir trois boules de même couleur sachant qu'on a obtenu trois boule portant le numéro 1 » ; E : « Obtenir une boule portant le numéro 2 sachant qu'on a obtenu exactement deux boules blanches ». »

**Activité 3 (p.241) — dé, face paire** : « On lance, une seule fois, un dé équilibré dont les faces sont numérotés de 1 à 6. On constate que la face apparue porte un numéro pair. 1- Quelle est la probabilité pour que le nombre marqué sur la face obtenue soit égal à 2 ? 2- Quelle est la probabilité pour que le nombre marqué sur la face obtenue soit supérieur à 3 ? »

**Remarque (encadré, p.241)** : « Pour calculer p(B/A) on peut choisir l'une des deux possibilités suivantes : - Calculer p(A ∩ B) et p(A) puis utiliser la définition. - Considérer une nouvelle expérience aléatoire : celle dont les issues possibles sont les issues qui réalisent l'événement A, parmi celles-ci, les issues favorables sont les issues qui réalisent également B. »

**Activité 4 (p.241) — supermarché, chocolats** : « Lors d'une promotion, un supermarché vend par paquets d'un kilogramme, des chocolats au lait et des chocolats à la noisette fabriqués en Tunisie, en France ou en Suisse. Le nombre de kilos mis en vente est donné par le tableau suivant : »

| Produit \ Origine de fabrication | Tunisie | France | Suisse |
|---|---|---|---|
| Chocolat au lait | 200 | 200 | 100 |
| Chocolat à la noisette | 600 | 500 | 400 |

(Total : 2000 kg ; au lait 500, noisette 1500 ; Tunisie 800, France 700, Suisse 500 — recomptés par moi, non imprimés.)
« 1- Un client pressé prend au hasard un paquet de chocolat. Quelle est la probabilité de chacun des événements suivants ? a) L : « le client prend un paquet de chocolat au lait » b) T : le client prend un paquet de chocolat tunisien »
2- a) Sachant que le client ne veut que des produits tunisiens, quelle est la probabilité qu'il prenne un paquet de chocolat au lait ? b) Quelle est la probabilité que le client prenne un paquet de chocolat européen sachant qu'il est à la noisette ? »

**Formule des probabilités composées (p.242)**

*Activité 1 — recrutement de stagiaires* : « Pour recruter des stagiaires, une entreprise organise des tests de sélection. Parmi les candidats qui se présentent aux épreuves il y a 60 % de garçons. Les résultats aux tests on permis de recruter 70 % des garçons candidats et 80 % des filles candidates. On choisit au hasard un candidat. On considère les événements : G « le candidat choisi est un garçon » et R « le candidat choisi est recruté » 1) a- Préciser p(G) et p(G/R). b- En déduire la probabilité que le candidat soit un garçon et qu'il soit recruté comme stagiaire ? 2) Quelle est la probabilité que le candidat soit une fille et qu'il soit recruté comme stagiaire ? »

**Propriété** (encadré) : « Soit E l'ensemble des issues d'une expérience aléatoire et p une probabilité sur E. Soient A et B deux événements quelconques. p(A ∩ B) = p(A/B) × p(B) »

*Activité 2 — sac de jetons* : « On considère un sac contenant sept jetons rouges et six jetons noires. On tire au hasard, successivement et sans remise, huit jetons du sac. On considère les événements suivants : A : « Le premier jeton tiré est rouge » ; B : « Le deuxième jeton tiré est rouge » ; C : « Le troisième jeton tiré est noir » ; E : « Le premier jeton noir apparaît au troisième tirage ». 1- Calculer : p(A), p((B/A) [sic, parenthèse doublée imprimée ; R7] et p(C/A ∩ B). 2- Montrer que p(A ∩ B ∩ C) = p(A) × p(B/A) × p(C/A ∩ B) et en déduire p(E). »

**Propriété** (encadré) : « Soit n un entier supérieur ou égal à 2. p(A1 ∩ A2 … ∩ An) = p(A1) x p(A2/A1) x p(A3/A1∩A2) x … x p(An/A1∩A2…∩An-1) »

##### 2) Indépendance de deux évènements (pp.242-243)

**Activité 1 (p.242) — pièce de monnaie** : « On lance une pièce de monnaie équilibrée deux fois de suite et on note, dans leur ordre d'apparition, les côtés obtenus (P pour pile et F pour face). On considère les évènements : A : « Obtenir deux côtés différents ». B : « Obtenir au plus une fois F ». 1) a- Calculer p(A), p(B) et p(A ∩ B). b- Comparer p(A)x p(B) et p(A ∩ B). 2) Reprendre la première question lorsqu'on lance la pièce de monnaie trois fois de suites. »

**Définition** (encadré, p.243) : « Deux évènements A et B sont indépendants si et seulement si p(A ∩ B) = p(A) × p(B) »

**Activité 2 (p.243) — 105 salariés** : « Une entreprise comporte 105 salariés. 70 salariés sont mariés, 30 salariés sont des cadres et 20 salariés sont des cadres mariés. 1- Recopier et compléter le tableau suivant »

| | Cadres | Non cadres | Total |
|---|---|---|---|
| Mariés | 20 | | |
| Non mariés | | | |
| Total | 30 | | 105 |

« 2 - On prend un fichier quelconque d'un salarié. On considère les événements suivants : C : « le salarié choisi est un cadre » et M : « le salarié choisi est marié ». Les événements C et M sont-ils indépendants ? »

**Activité 3 (p.243) — bac, redoublants** : « Dans une classe terminale, 25 % sont des redoublants. On suppose que la probabilité de réussir au bac dans cette classe est 85 %, la probabilité de réussir chez les non redoublants est de 80 %. Après les résultats du bac, on rencontre au hasard un élève de cette classe et on note : B : « L'élève a le bac » et R : « L'élève est redoublant ». 1) Calculer p(B ∩ R). 2) Les événements R et B sont ils indépendants ? »

**Activité 4 (p.243)** : « Soient A et B deux événements tels que p(A) ≠ 0 et p(B) ≠ 0. Montrer que : 1- A et B sont indépendants si et seulement si p(A/B) = p(A) et p(B/A) = p(B) 2- Si A et B sont incompatibles alors A et B ne sont pas indépendants ? »

**Remarques (encadré, p.243)** : « • Deux événements sont indépendants, lorsque la réalisation de l'un n'a aucune influence sur la réalisation de l'autre. • Il ne faut pas confondre évènements indépendants et évènements incompatibles. Deux événements incompatibles ne sont pas généralement indépendants. »

**Activité 5 (arbre pondéré) (pp.243-244) — ballons en cuir, trois fournisseurs** : « Une entreprise est spécialisée dans la vente de ballons en cuir. Elle a trois fournisseurs A1, A2 et A3 qui alimentent le stock dans les proportions 25 %, 40 % et 35 %. Une étude statique [sic] faite par le service qualité de cette entreprise a prouvé que : La probabilité pour qu'un ballon ait un défaut sachant qu'il est fourni par A1 vaut 0,04. … par A2 vaut 0,03. … par A3 vaut 0,02. On note E : l'ensemble des ballons du stock. On prend un ballon au hasard de E et on note : Ai : « Le ballon provient du fournisseur Ai » i = 1, 2, 3. B : « Le ballon a un défaut ». »
Arbre fourni (p.244), racine E : branches rouges E–A1 (0.25), E–A2 (0.4), E–A3 (non pondérée) ; branches bleues A1–B / A1–B̄ (non pondérées), A2–B (0.03), A2–B̄ (non pondérée), A3–B (0.02), A3–B̄ (non pondérée). Texte : « Un ballon du stock ne peut être fourni que par les fournisseurs A1, A2 ou A3 seulement, cette condition est schématisée par les trois branches rouges … Chaque branche bleue correspond à une probabilité conditionnelle. Par exemple la branche A1-B correspond à l'événement : « le ballon a un défaut sachant qu'il est fourni par A1 »
« 1- a- Reproduire et compléter l'arbre ci-dessus en pondérant chaque branche par la probabilité qui lui correspond. b- Vérifier que la somme des probabilités affectées aux branches issues d'un même point (dit nœud) est égale à 1. 2- a) Calculer p(B∩A1). b) Vérifier que la probabilité de l'événement B∩A1 est égale au produit des probabilités inscrites sur les branches E-A1 et A1-B du chemin E-A1-B. c) Utiliser l'arbre pondéré ci-dessus pour calculer p(B∩A2) et p(B∩A3). »

**Remarque (encadré, p.244)** : « Lorsqu'une situation est représentée par un arbre pondéré : • La somme des probabilités affectées aux branches d'un même nœud est égale à 1. • La probabilité d'un événement correspondant à un chemin est égale au produit des probabilités inscrites sur chaque branche de ce chemin. »

##### 3) Formule des probabilités totales (pp.244-246)

**Activité 1 (p.244)** : « En reprenant l'activité (l'arbre pondéré) et en remarquant que A1, A2 et A3 forment une partition de E. a- Vérifier B ∩ A1, B ∩ A2 et B ∩ A3 forment une partition de B. b- Montrer que : p(B) = p(B/A1) × p(A1) + p(B/A2) × p(A2) + p(B/A3) × p(A3). c- En déduire la valeur de p(B). »

**Propriété** (encadré, p.245) : « Soit E l'ensemble des issues d'une expérience aléatoire, p une probabilité sur E et n un entier supérieur ou égal à 2. Soit A1, A2, A3 … An des événements formant une partition de E. La probabilité d'un événement quelconque B est donnée par la formule : p(B) = p(B/A1) × p(A1) + p(B/A2) × p(A2) + … … + p(B/An) × p(An) » (figure : ellipse E découpée en secteurs A1, A2, A3, …, An, avec B en ellipse centrale).

**Activité 2 (p.245) — pâtisserie** : « A la cafétéria, dans la vitrine pâtisserie : - 60 % des gâteaux sont à base de crème. - Parmi ceux qui sont à base de crème, 30 % ont aussi des fruits. - Parmi ceux qui ne sont pas à base de crème, 80 % ont des fruits. On considère les événements : C « avoir un gâteau à base de crème ». F « avoir un gâteau avec des fruits ». On modélise cette situation par l'arbre pondéré ci-contre : [racine→C 0,60 ; C→F 0,30 ; C̄→F 0,80 ; autres branches vides]. Reproduire et compléter l'arbre pondéré ci-contre. On prend un gâteau au hasard. Montrer que la probabilité de l'avoir avec des fruits est égale à 0.5 »

**Activité 3 (p.245) — machines M1 puis M2** : « Dans une usine, la fabrication d'une pièce nécessite son passage sur une machine M1 puis sur une machine M2. On note : M1 : événement : « La machine M1 est en marche ». M̄1 : L'événement : « La machine M1 est en panne ». Une étude a permis d'estimer que : (I) p(M̄1) = 0,004. (II) Lorsque M1 est en panne la probabilité que M2 tombe en panne est égale à 0.5. (III) Lorsque M1 est en marche la probabilité que M2 tombe en panne est égale à 0.002. 1) Construire un arbre pondéré représentant cette situation et écrire sur chaque branche la probabilité associée. 2) Calculer p(M2). »

**Activité 4 (p.246) — vélos tout terrain, 4 fournisseurs** : « Une chaîne de magasins commercialise des vélos tout terrain. Elle s'adresse exclusivement à quatre fournisseurs F1, F2, F3 et F4 qui produisent respectivement 10 %, 20 %, 30 % et 40 % du stock. L'essentiel de ces vélos est vendu dans deux magasins et la production de chaque fournisseur est répartie selon le tableau ci-dessous : »

| Fournisseur | F1 | F2 | F3 | F4 |
|---|---|---|---|---|
| Magasin A | 0 | 0,8 | 0,5 | 0,4 |
| Magasin B | 0,6 | 0 | 0,5 | 0,3 |
| Autres magasins C | 0,4 | 0,2 | 0 | 0,3 |

(Colonnes recomptées : chacune somme à 1.)
« On modélise la situation par l'arbre pondéré ci-dessous : » arbre : racine→F1 0,1 ; racine→F4 0,4 ; F1→A 0 ; F1→C 0,4 ; F2→A 0,8 ; F4→C 0,3 ; autres branches non pondérées (feuilles A, B, C sous chaque Fi).
« 1) Reproduire et compléter l'arbre pondéré ci-dessus. 2) On prend au hasard un vélo du stock de ces magasins. Calculer la probabilité des événements suivants : E : « Le vélo est vendu dans le magasin A et provient du fournisseur F1. » F : « Le vélo est vendu dans le magasin A et provient du fournisseur F2 » G : « Le vélo est vendu dans le magasin A ». 3) Quelle est la probabilité que le vélo soit vendu dans le magasin B ? »

**Activité 5 (pp.246-247) — salariés H/F, catégories A, B, C** : « Dans une entreprise, 75 % des salariés sont des femmes. Le tableau suivant donne la répartition de ces salariés, suivant le sexe, dans chacune des trois catégories d'emploi A, B ou C. »

| Catégorie | A | B | C |
|---|---|---|---|
| Homme | 20% | 50% | 30% |
| Femme | 20% | 35% | 45% |

(Lignes recomptées : 100 % chacune.)
« On tire au hasard la fiche d'un salarié de cette entreprise et on note : H : « le salarié choisi est un homme » F : « … une femme » A : « le salarié est de la catégorie A ». De même pour les catégories B et C. 1- a- Déterminer p(A/H), p(A/F) et en déduire p(A). b- Calculer p(B) et p(C). 2- Reprendre l'arbre ci-contre : et pondérer chaque branche par la probabilité correspondante. » (arbre p.247 : racine → A, B, C ; chacun → H, F ; aucune pondération imprimée.)

##### 4) Formule de Bayes (pp.247-248)

**Activité 1 (p.247) — deux urnes** : « Deux urnes U1 et U2 sont telles que : U1 contient 5 boules blanches et trois boules noires et U2 contient 4 boules blanches et 7 boules noires. On choisit au hasard une des deux urnes et on en extrait au hasard une boule de cette urne. On considère les événements suivants : A : « L'urne choisie est U1 » N : « La boule tirée est noire ». 1- Préciser p(A) ; p(Ā) ; p(N/A) et p(N/Ā) 2- On a constaté que la boule tirée est noire. Quelle est la probabilité pour que l'urne choisie soit U1 ? »

**Propriété** (encadré, p.247) : « Soient A et B deux événements de probabilités non nulles. p(A/B) = p(A) × p(B/A) / [ p(A) × p(B/A) + p(Ā) × p(B/Ā) ] . »

**Activité 2 (p.247) — touriste, falaise** : « La scène se passe en haut d'une falaise au bord de la mer. Pour trouver une plage et aller se baigner, les touristes ne peuvent choisir qu'entre deux plages, l'une à l'Est et l'autre à l'Ouest. Un touriste se retrouve deux jours consécutifs en haut de la falaise. Le premier jour, il choisit au hasard l'une des deux directions. Le second jour, on admet que la probabilité qu'il choisisse une direction opposée à celle prise la veille vaut 0,8. Pour i = 1 ou i = 2, on note Ei l'évènement : « Le touriste se dirige vers l'Est le i^ème jour » et Oi l'évènement : « Le touriste se dirige vers l'Ouest le i^ème jour ». Sachant que le touriste est à l'Ouest le deuxième jour quelle est la probabilité qu'il était à l'Est la veille. »

**Activité 3 (pp.247-248) — tulipes, deux lots** : « Un jardinier dispose de deux lots 1 et 2 contenant chacun de très nombreux bulbes donnant des tulipes de couleurs variées. La probabilité pour qu'un bulbe du lot 1 donne une tulipe jaune est égale à 1/4. La probabilité pour qu'un bulbe du lot 2 donne une tulipe jaune est égale à 1/2. Ce jardinier choisit au hasard un lot et plante un très grand nombre de bulbes de tulipes. Après la récolte on choisit au hasard une tulipe et on définit les évènements suivants : A : « Le jardinier a choisi le lot 1 » B : « Le jardinier a choisi le lot 2 » J : « La tulipe choisie est jaune » 1- On modélise la situation par l'arbre suivant : [racine→A, B ; A→J, J̄ ; B→J, J̄, sans pondération] Reproduire l'arbre ci-dessus et pondérer chaque branche par la probabilité convenable. 2- Sachant que la tulipe choisie est jaune quelle est la probabilité qu'elle soit planté dans le lot 1 ? »

**Activité 4 (p.248) — dé 1-2-3 et urne de lettres** : « On dispose d'un dé cubique équilibré dont une face porte le numéro 1, deux faces portent le numéro 2 et trois faces portent le numéro 3. On dispose également d'une urne contenant dix boules indiscernables au toucher, portant les lettres L, O, G, A, R, I, T, H, M, E (soit quatre voyelles et six consonnes). Un joueur fait une partie en deux étapes : Première étape : il jette le dé et note le numéro obtenu. Deuxième étape : • Si le dé indique 1, il tire au hasard une boule de l'urne. Il gagne la partie si cette boule porte une voyelle et il perd dans le cas contraire. • Si le dé indique 2, il tire au hasard et simultanément deux boules de l'urne. Il gagne la partie si chacune de ces deux boules porte une voyelle et il perd dans le cas contraire. • Si le dé indique 3, il tire au hasard et simultanément trois boules de l'urne. Il gagne la partie si chacune de ces trois boules porte une voyelle et il perd dans le cas contraire. À la fin de chaque partie, il remet dans l'urne la ou les boules tirée(s). On définit les évènements suivants : D1 : « le dé indique 1 » D2 : « le dé indique 2 » D3 : « le dé indique 3 » G : « la partie est gagnée ». 1- a) Déterminer les probabilités p(G/D1) et p(G/D2). b) Montrer que p(G) = 23/180. 2- Un joueur a gagné la partie. Calculer la probabilité qu'il ait obtenu le numéro 1 avec le dé. »
(Le manuel donne ici la valeur cible p(G) = 23/180 : seul résultat chiffré imprimé de la section.)

---

#### 3. COURS — II. Variables aléatoires (pp. 248-258)

##### Variable aléatoire (pp.248-249)
**Activité 1** : « On lance une pièce de monnaie équilibrée deux fois de suite et on note, dans leur ordre d'apparition, les côtés obtenus (P pour pile et F pour face). On désigne par E l'ensemble des 4 évènements élémentaires PP, PF, FP et FF. Soit X : l'application qui à chaque événement élémentaire associe le nombre de fois où face est apparu. 1) Déterminer l'image de chacun des évènements élémentaires de E par X et en déduire toutes les valeurs possibles prises par X. 2) On désigne par A l'ensemble des événements élémentaires ayant pour image le réel 1 par X. Déterminer p(A). »

**Définition** (encadré, p.249) : « Soit E l'ensemble des issues d'une expérience aléatoire. On appelle variable aléatoire sur E toute application X de E vers IR »

**Remarque** (encadré) : « Lorsque x1, ,……,xn (avec i = 1, ….,n).sont les valeurs prises par une variable aléatoire X. on note (X = xi) l'ensemble des événements élémentaires de E ayant xi pour image par X. » (ponctuation « x1, ,……,xn » telle qu'imprimée)

**Activité 2 — sac de 20 jetons** : « Un sac contient 20 jetons colorés et de même forme : 9 rouges, 8 verts et 3 noires. Un joueur prend au hasard un jeton du sac. Si le jeton est noir il gagne 5DT, s'il est vert, il gagne 3DT et s'il est rouge il perd 4DT. Soit X la variable aléatoire prenant pour valeurs le gain algébrique du joueur, (exprimé en DT). 1) Déterminer les valeurs x1, x2 et x3 prises par X. 2) a- Calculer : p1 = p(X = x1), p2 = p(X = x2) et p3 = p(X = x3). b- Vérifier que p1 + p2 + p3 = 1 »

**Loi de probabilité** (encadré) : « Lorsqu'à chaque valeur xi (avec i = 1, …,n) prise par une variable aléatoire X, on associe la probabilité pi = p(X = xi), on dit que l'on définit **la loi de probabilité de X** »

**Remarques** (encadré) : « • On peut donner la loi de probabilité d'une variable aléatoire X à l'aide du tableau ci-dessous » :

| Valeur de xi | x1 | x2 | …. | xn |
|---|---|---|---|---|
| p(X = xi) | p1 | p2 | | pn |

« • Les événements (X = xi) (avec i = 1, …,n) forment une partition de E, donc p1 + p2 + ...... + pn = 1 »

**Activité 3 (p.249)** : « Une boite contient trois carrés numérotés de 1 à 3 ; une deuxième boite contient quatre disques numérotés de 1 à 4. On tire indépendamment un objet de chacune des deux boites. Les objets d'une même boite sont supposés avoir la même probabilité d'être tirés. On considère la variable aléatoire X qui, à chaque tirage, associe la somme des deux nombres indiqués sur les objets tirés. Donnez la loi de probabilité de X »

**Activité 4 (p.250) — machine, sachets** : « Une machine remplit automatiquement des sachets en mélangeant deux produits A et B. Dans chaque sachet, la masse du produit A introduite par la machine est 50g avec une probabilité de 0,8 ou 51g avec une probabilité de 0,2 et indépendamment la masse du produit B introduite est 50g avec une probabilité égale à 0,6 ou 51g de probabilité égale à 0,4. On désigne par X la variable aléatoire prenant pour valeurs la masse d'un sachet. 1- Déterminer les valeurs prises par X. 2- Donner la loi de probabilité de X. »

##### Espérance mathématique (pp.250-252)
**Activité 1 (p.250) — ventes de voitures** : « Au cours d'une étude prospective sur la vente d'un nouveau model [sic] d'une voiture, le département marketing d'une société a pris par hypothèse la loi de probabilité de la variable aléatoire X prenant pour valeurs : le nombre de voiture susceptibles d'être vendues par jour dans tous les points de vente de cette société (chaque point de vente contient au départ de l'étude exactement 5 voitures de ce nouveau modèle). La loi de probabilité de X est donnée par le tableau suivant : »

| xi | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| pi | 0,09 | 0,34 | 0,23 | 0,20 | 0,10 | 0,04 |

(Somme recomptée = 1,00 ; E(X) recalculé = 2,00, cohérent avec la prévision de l'énoncé.)
« 1- Calculer le réel E(X) = x1p1 + x2p2 + ... + x6p6. 2- Le directeur de la société prévoit vendre en moyenne deux voitures par jour. Justifier sa prévision ? »

**Définition** (encadré, p.250) : « Soit X une variable aléatoire dont la loi de probabilité est donnée par le tableau ci-dessous : [Valeur de X : x1 x2 .... xn ; p(X = xi) : p1 p2 .... pn] L'espérance mathématique de X est le réel, noté E(X) et défini par : E(X) = x1p1 + x2p2 + ... + xnpn = Σ_{i=1}^{n} xi pi »
**Remarque** : « L'espérance mathématique est la moyenne des valeurs xi pondérées par les coefficients pi. »

**Activité 2 (p.251) — 12 articles** : « On tire au hasard un échantillon de trois articles dans une boite contenant 12 articles dont trois sont défectueux. Soit X la variable aléatoire prenant pour valeur le nombre des articles défectueux obtenus. 1- Déterminer la loi de probabilité de X. 2- Calculer E(X). Interpréter votre résultat. »

**Activité 3 (p.251) — jetons et cases** : « On considère 4 cases numérotées de 1 à 4 et quatre jetons numérotées de 1 à 4. Un joueur place un jeton (et un seul) au hasard dans chacune des quatre cases. Combien y a-t-il de répartitions possibles des 4 jetons dans les 4 cases ? On suppose par la suite chacune de ces répartitions équiprobables. On dit qu'un jeton est « en place » quand il a été placé dans la case portant le même numéro que lui. On associe à chaque répartition des quatre jetons dans les quatre cases le nombre de jetons « en place ». On définit ainsi une variable aléatoire X. Donnez sa loi de probabilité. Calculez E(X). »

**Activité 4 (p.251) — jeu de foire, deux dés** : « Dans une foire, on propose le jeu suivant : Le joueur mise 1 DT sur l'un des numéros 1 ; 2, 3, 4, 5 ou 6, puis on lance deux dés discernables et réguliers à six faces numérotées de 1 à 6. Si le numéro choisi sort deux fois, le joueur remporte deux fois sa mise. Si le numéro choisi sort une seule fois, le joueur récupère sa mise. Si le numéro choisi ne sort pas le joueur perd sa mise. Soit X : la variable aléatoire prenant pour valeur le gain algébrique : (c à d la somme d'argent gagnée ou perdue à la fin de l'épreuve par le joueur). 1- Déterminer la loi de probabilité de X. 2- a) Calculer E(X). b) Ce jeu est-il avantageux pour le joueur ? »
**Encadré (à droite, p.251) — jeu équitable/favorable/défavorable** : « Dans le cas où la variable aléatoire X indique le gain algébrique réalisé dans un jeu, on dit que le jeu est : - Équitable, si E(X) = 0. - Favorable ou gagnant, si E(X) > 0. - Défavorable ou perdant, si E(X) < 0. »

**Activité 5 (pp.251-252) — placement en bourse** : « Un chef d'entreprise envisage de placer une somme d'un million de DT dans une bourse. Deux opérations lui sont proposées : • La première opération a une probabilité de réussite de 0,6 et permettra de doubler la somme placée. Si cette opération est manquée, le chef d'entreprise ne récupérera que la moitié de la somme placée. • La seconde a une probabilité de réussite de 0,9 et permettra de gagner la moitié de la somme placée. Si cette opération est manquée, le chef d'entreprise ne récupérera que 40% de la somme placée. Soit X la variable aléatoire qui, à tout placement d'un million de DT selon la première opération financière, associe le gain algébrique ainsi obtenu. Soit Y la variable aléatoire qui à tout placement d'un million DT selon la seconde opération financière, associe le gain algébrique ainsi obtenu. 1- Donner la loi de probabilité de la variable aléatoire X et calculer son espérance E(X). 2- Donner la loi de probabilité de la variable aléatoire Y. et calculer son espérance E(Y). 3- Quelle est l'opération de placement la plus avantageuse ? »

##### Variance - Écart-type (pp.252-254)
**Activité 1 (p.252)** : « On considère les deux variables aléatoires X et Y dont les lois de probabilités sont données par les deux tableaux suivants : »

| xi | -6 | -1 | 4 |
|---|---|---|---|
| pi | 1/7 | 4/7 | 2/7 |

| yi | -1 | 0 | 1 |
|---|---|---|---|
| pi | 1/7 | 3/7 | 1/7 |

(Tableau de Y lu à 200 dpi : 1/7, 3/7, 1/7 — somme 5/7 ≠ 1, voir § Notes.)
« 1- a) Vérifier que E(X) = E(Y). b) Quelle est la variable aléatoire qui a les valeurs les plus dispersées par rapport à son espérance. 2- Comparer les réels V(X) = Σ_{i=1}^{3} (xi − E(X))² pi et V(Y) = Σ_{i=1}^{3} (yi − E(Y))² pi. Quelle conclusion peut-on faire ? »

**Définition** (encadré, p.252) : « Soit X une variable aléatoire, d'espérance mathématique E(X), dont la loi est donnée par le tableau ci-dessous. [xi : x1 x2 ......... xn ; pi : p1 p2 ......... pn]
• La variance de X est le réel, noté V(X), défini par : V(X) = (x1 − E(X))² p1 + (x2 − E(X))² p2 + ... ... + (xn − E(X))² pn = Σ_{i=1}^{n} (xi − E(X))² pi .
• L'écart type de X, noté σ(X) est la racine carrée de la variance σ(X) = √V(X). »
Texte en italique : « En probabilité, comme en statistique, on introduit la notion de variance pour estimer l'étendu [sic] de la dispersion des différentes valeurs de X par rapport à leur moyenne pondérée E(X). »

**« Pourquoi l'écart type ? » (p.253, italique)** : « On suppose que les valeurs xi d'une variable aléatoire X sont exprimées en DT, l'espérance qui représente un gain moyen est à son tour exprimée en DT. Par contre la variance est exprimée en « DT au carré ». En revanche σ(X) = √V(X) est exprimé en DT comme les valeurs de xi. »

**Activité 2 (p.253) — pièces d'horlogerie** : « Une usine rectifie des pièces d'horlogerie. A l'issue du processus de fabrication, une pièce peut présenter 0, 1, 2 ou 3 défauts d'aspects. Soit X la variable aléatoire ayant pour valeur le nombre de défauts d'une pièce triée au hasard dans un lot. La loi de X est définie par le tableau suivant : »

| xi | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| pi | 0,920 | 0,060 | 0,016 | 0,004 |

(Somme recomptée = 1,000.)
« 1- a) Calculer l'espérance mathématique de X. b) Calculer la variance, puis l'écart type de X. 2- Le prix de vente d'une pièce dépend du nombre de défauts qu'elle présente. »

| Nombre de défauts | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Prix de vente en DT | 30 | 20 | 15 | 5 |

« Soit Y : La variable aléatoire ayant pour valeur le prix de vente d'une pièce tirée au hasard dans un lot Déterminer la loi de probabilité de Y et calculer E(Y), V(Y) et σ(Y) »

**Propriété** (encadré, p.253) : « V(X) = E(X²) – [E(X)]² » ; italique : « Cette expression est souvent plus pratique pour le calcul de la variance. »

**Activité 3 (p.253)** : « On tire simultanément trois jetons d'une urne contenant 5 jetons indiscernables au toucher numérotés 0, 1, 2, 3 et 4. Soit X la variable aléatoire qui à chaque tirage associe le nombre de chiffres pairs portés par les trois jetons tirés. 1- Déterminer la loi de probabilité de X. 2- Calculer E(X) ; V(X) et σ(X). »

**Activité 4 (p.253) — somme de deux dés, gain** : « On lance deux dés et on lit la somme S des chiffres des faces supérieures. Si S ≤ 5 alors on perd 1 DT ; si 6 ≤ S ≤ 9 alors on gagne 0,4 DT ; si 10 ≤ S ≤ 12 alors on gagne 1,5 DT. X étant la variable aléatoire qui à une issue associe le gain algébrique correspondant. 1- Donner la loi de probabilité de X. 2- Calculer E(X). Ce jeu est il favorable pour le joueur ? 3- Calculer l'écart type de X. »
(Les symboles ≤ de l'énoncé, perdus dans la couche texte, sont confirmés à l'image.)

**Activité 5 (p.254) — deux boîtes A et B** : « Un sac contenant deux boites A et B indiscernables au toucher. A contient trois boules blanches et quatre boules noires et B contient quatre boules blanches et trois boules noires. Une épreuve consiste à choisir au hasard l'une des boites A ou B puis tirer simultanément trois boules. On note A l'événement « La boite choisie est A » ; B l'événement « La boite choisie est B » ; C l'événement « Obtenir une seule boule blanche » 1- a) Compléter l'arbre pondéré ci-contre. [racine→A 0,5 ; A→C, C̄ ; B→C, C̄] b) Calculer p(C). 2- Soit X la variable aléatoire prenant pour valeur le nombre de boules blanches obtenues. a) Déterminer la loi de probabilité de X. b) Calculer E(X) ; V(X) et σ(X). »

**Activité 6 (p.254) — étude de marketing, deux marchés** : « Une étude de marketing, portant sur la vente d'un article, est réalisée sur deux marchés potentiels M1 et M2. »

| Profit xi (en milliers de DT) | 20 | 25 | 30 | 35 | 40 | 50 |
|---|---|---|---|---|---|---|
| Marché M1, Pi | 20% | 30% | 20% | 15% | 10% | 5% |
| Marché M2, P'i | 10% | 45% | 27% | 10% | 6% | 2% |

(Sommes recomptées : M1 = 100 %, M2 = 100 %.)
« 1- a) Calculer les espérances mathématiques de profit E1 et E2 pour ce produit suivant les marchés M1 et M2 b) Calculer leurs écarts types σ1 et σ2. 2- Le directeur du marketing est une personne enthousiaste qui pense que son produit sera très demandé. Expliquer pour quoi il choisira de lancer son produit sur le marché M1 ? 3- Le directeur du marketing est un homme prudent compte tenu de la conjoncture, ci-dessus, il préférera le marché M2. Justifier son choix. »

##### Schéma de Bernoulli (pp.254-255)
**Activité 1 (p.254)** : « On jette, une seule fois, un dé truqué dont les faces sont numérotées de 1 à 6, de façon que la probabilité d'obtenir un nombre pair soit le double de celle d'obtenir un nombre impair. Soient les événement S : « obtenir un nombre impair » et E : « obtenir un nombre pair ». Calculer p(S) et p(E). »

**Définition** (encadré, p.255) : « Une expérience aléatoire à deux issues contraires S (succès) et E (échec), de probabilités respectives p et q, avec p+q = 1, est dite épreuve de Bernoulli. [arbre : p → S ; q → E] Une expérience constituée par la répétition de n épreuves de Bernoulli n≥2, identiques et indépendantes les unes des autres est un schéma de Bernoulli. »

**Activité 2 (p.255)** : « Proposer trois exemples correspondant à une épreuve de Bernoulli et préciser pour chacun p(S) et p(E) »

**Activité 3 (p.255) — dé truqué** : « Un dé truqué est tel que la probabilité d'obtenir le chiffre 1 à chaque lancer soit égale à 0,8. Les cinq autres éventualités 2, 3, 4, 5 et 6 ont la même probabilité. 1- On jette une fois ce dé. Quelle est la probabilité d'obtenir un nombre impair ? 2- On lance ce dé quatre fois de suite. a- Quelle est la probabilité d'obtenir exactement trois fois un nombre impair ? b- Quelle est la probabilité d'obtenir au moins une fois un nombre impair ? »

##### Loi binomiale (pp.255-258)
**Activité 1 (pp.255-256)** : « On considère l'épreuve de Bernoulli de l'activité 1 du paragraphe précédent. S désigne le succès et E désigne l'échec. On suppose que l'on répète cette épreuve trois fois. On s'intéresse à l'événement A : « obtenir exactement deux succès ». Cette expérience peut être représentée par l'arbre si dessous [sic] : » Arbre à trois lancers (1er, 2ème, 3ème Lancer), premier niveau pondéré 1/3 (S) et 2/3 (E), issues listées dans l'ordre SSS, SSE, SES, SEE, ESS, ESE, EES, EEE [R7 : l'arbre est tracé en entier (3 niveaux, nœuds S/E étiquetés à chaque niveau) ; seules les pondérations manquent hors du 1er niveau (1/3, 2/3) — et non « seules les branches du premier lancer étiquetées »].
« 1- Recopier et compléter l'arbre. 2- a- Donner toutes les issues qui réalisent A et vérifier qu'elles sont toutes équiprobables. b- Déterminer p(A). c- Pourquoi y a-t-il C(3,2) issues qui réalisent l'événement A ? 3- Justifier que p(A) = C(3,2) × (1/3)² × 2/3. 4- Calculer la probabilité de chacun des événements : B : « il y a exactement trois sucées [sic] » ; C : « il n'y a pas de sucées » ; D : « il y a exactement un sucées » ; E : « il y au moins un sucées » »
(L'activité 1 de Bernoulli donne p(S) = 1/3 pour le dé truqué, cohérent avec l'arbre ; cf. p(S)+2p(S)=1.)

**Activité 2 (p.256) — sondage téléphonique** : « Une entreprise confie à une société de sondage par téléphone, une enquête sur la qualité de ses produits. On admet que lors d'un appel téléphonique, la probabilité que le correspondant ne décroche pas est 1/3. Un enquêteur a une liste de 10 personnes à contacter. Les sondages auprès des personnes d'une même liste sont indépendants. On considère la variable aléatoire X prenant pour valeurs le nombre des personnes de cette liste qui ont décrochés. 1) Déterminer l'ensemble des valeurs prises par X. 2) Pour chaque valeur k de X vérifier que : p(X = k) = C(10,k) × (2/3)^k × (1/3)^(10−k). 3) Vérifier que : E(X) = 10 × 2/3 et V(X) = 10 × 2/3 × 1/3. »

[R7 : le manuel note la combinaison $C_n^k$ (n en indice, k en exposant : $C_{10}^k$, $C_3^2$) ; la fiche l'écrit C(n,k) = $C_n^k$.]
**Définition de la loi binomiale** (encadré, p.256) : « On considère un schéma de Bernoulli constitué par la succession de n épreuves de Bernoulli, identiques et indépendantes et on note p la probabilité du succès S et q la probabilité de l'échec E (q = 1 − p). La variable aléatoire X qui, à chaque issue de cette expérience aléatoire, associe le nombre de succès obtenus, suit une loi dite loi binomiale de paramètres (n,p). • X prend pour valeurs tous les entiers k compris entre 0 et n. • Pour tout entier k compris entre 0 et n : p(X = k) = C(n,k) p^k × q^(n−k) »

**Remarque** (encadré) : « On admet que l'espérance mathématique d'une variable aléatoire X qui suit une loi binomiale de paramètres (n,p) est **E(X) = n.p** et que sa variance est **V(X) = n.p.q** avec q = 1 − p. »

**Activité 3 (p.256) — tir sur cible** : « On tire six fois de suite sur une cible. A chaque tir la probabilité d'atteindre cette cible est 2/3. Soit X la variable aléatoire prenant pour valeurs le nombre de fois ou [sic] la cible est atteinte. 1- Déterminer la loi de probabilité de X. 2- Chaque fois où la cible est ratée on perd 1 DT et si elle est atteinte on gagne 0,5 DT. Ce jeu est il gagnant ? »

**Activité 4 (p.257) — dé tétraédrique** : « On lance un dé tétraédrique dont les quatre faces portent les nombres 1, 2, 3 et 4. On lit le nombre sur la face cachée. Pour k ∈ {1 ; 2 ; 3 ; 4), on note pi la probabilité d'obtenir le nombre k sur la face cachée. Le dé est déséquilibré de telle sorte que les nombres p1, p2, p3 et p4 dans cet ordre, forment une progression arithmétique. 1- Sachant que p4 = 0,4 démontrer que p1 = 0,1, p2 = 0,2 et p3 = 0,3. 2- On lance le dé trois fois de suite. a- Quelle est la probabilité d'obtenir dans l'ordre les nombres 1, 2, 4 ? b- Quelle est la probabilité d'obtenir trois nombres distincts rangés dans l'ordre croissant 3- On lance 10 fois de suite le dé. On suppose les lancers deux à deux indépendants. On note X la variable aléatoire qui décompte le nombre de fois où le chiffre 4 est obtenu. a- Pour 0 ≤ i ≤ 10, exprimer en fonction de i la probabilité de l'évènement (X = i). b- Calculer l'espérance mathématique de X. Interpréter le résultat obtenu. c- Calculer la probabilité de l'évènement (X ≥ 1). On donnera une valeur arrondie au millième. »

**Activité 5 (p.257) — 50 pièces, chaîne d'assemblage** : « On prélève au hasard 50 pièces fabriquées par une chaîne d'assemblage, on admet que, lorsque la chaîne fonctionne normalement, la probabilité qu'une pièce, choisie au hasard en sortie de chaîne, soit non conforme est égale à 0.025. Soit X la variable aléatoire qui prend pour valeurs le nombre de pièces non conformes sur les 50 prélevées. 1- a) Vérifier que X suit une loi binomiale dont on précisera les paramètres. b) Calculer p(X = 5) et p(X ≤ 2). 2- Calculer E(X), V(X) et σ(X). 3- On effectue un test de fonctionnement normal de la chaîne fondé sur le principe suivant : on prélève au hasard 50 pièces en sortie de chaîne et, si le nombre de pièces non conformes est situé dans l'intervalle [E(X) − 2σ(X) , E(X) + 2σ(X)] alors on considère que la chaîne fonctionne normalement. a- Sur un prélèvement donné on trouve 4 pièces non conformes. La chaîne fonctionne-t-elle normalement ? b) Montrer que la probabilité pour que la variable aléatoire X soit située dans l'intervalle [E(X) − 2σ(X) , E(X) + 2σ(X)] est supérieure à 95% (On arrondira les résultats a 3 chiffres significatifs). »

**Activité 6 (pp.257-258) — Ahmed, formation** : « Ahmed fait partie d'un groupe de 8 personnes suivant une formation professionnelle a raison de 6 séances hebdomadaires. A chaque séance, le formateur interroge au hasard l'un des participants, indépendamment de l'interrogation des séances précédentes. 1- Pour une séance donnée, quelle est la probabilité qu'Ahmed soit interrogé ? 2- Soit X la variable aléatoire égale au nombre de fois où Ahmed est interrogé durant la semaine a) Donner la loi de X. b) Calculer la probabilité pour qu'Ahmed soit interrogé au moins une fois dans la semaine. c) Calculer la probabilité pour qu'Ahmed soit interrogé au plus une fois dans la semaine. d) Calculer l'espérance de X. en déduire le nombre moyen d'interrogation concernant Ahmed sur une période de 4 semaines. »

**Activité 7 (p.258) — QCM télévisé** : « Un candidat à un jeu télévisé doit répondre à quatre questions de type QCM. Pour chaque question, trois réponses sont proposées dont une seule est exacte. Le candidat répond en choisissant au hasard une réponse pour chaque question. Soit X la variable aléatoire prenant pour valeurs le nombre de réponses exactes fournies par le candidat. a) Donner la loi de probabilité de X. b) On attribue trois points par réponse juste et on retire un point par réponse fausse. Combien de points le candidat peut-il espérer obtenir ? »
(Le reste de la page 258 est blanc.)

---

#### 4. AVEC L'ORDINATEUR (pp. 259-260) — Simulation (lancer de deux dés à l'aide d'Excel)

Texte verbatim (p.259) : « On lance deux dés N fois (N=25 ou N=150) et on calcule la somme S des points obtenus sur les faces supérieures des dés. On se propose de comparer les fréquences d'apparitions de chaque valeur de S avec les probabilités théoriques d'apparitions de ces valeurs. Les résultats sont résumés dans un histogramme, les distributions des fréquences observées sont représentées en parallèle avec les valeurs des probabilités théoriques.
- Créer sur Excel une feuille vierge
- Dans les 25 cellules A2:A26 taper des valeurs aléatoires qui peuvent êtres prises par le dé 1 en écrivant la formule suivante dans la cellule Ai i=2...26 : `Ai = ENT(6*ALEA()+1)` (On écrira la formule pour A2 (A2 = ENT(6*ALEA()+1)) puis utiliser copier/coller))
- Faire le même travail pour le dé 2 en écrivant dans la cellule Bi i=2....26
- La formule `Bi = ENT(6*ALEA()+1)` [capture : feuille avec colonnes A « Dé1 », B « Dé2 », C « Somme », lignes 2 à 6 vides]
Pour calculer la somme
- Taper dans la cellule Ci la formule `Ci = Ai + Bi` (i =2....26) (On écrira la formule pour C2 (C2 = A2 + B2) puis utiliser copier/coller))
Les Valeurs possibles de la somme sont (2,3,4,5,6,7,8,9,10,11,12)
- Dans les cellules de la colonne D, taper les valeurs possibles de la somme.
- Dans les cellules de la colonne E on calcule les effectifs correspondant à chaque valeur de la somme pour cela, taper dans les cellules Ei (i =2....26) la formule : `Ei = NB.SI(C2:C26;Di)`
- En suite on calcule les fréquences d'apparition de chaque valeur de S au cours des 25 lancers pour cela taper dans la cellule Fi (i =2.....12) la formule : `Fi = Ei/25`
- Dans les cellules de la colonne G taper les valeurs théoriques des probabilités d'apparition de chaque valeur de la somme S.
- Tracer l'histogramme des Fréquences et les probabilité correspondantes
Pour afficher les histogramme sélectionner les colonnes des Fréquences et celles des probabilités en appuyant sur le l'onglet assistant Graphique [icône] en suite choisir le type de graphique : Histogramme. »

Page 260 : « - Refaire le même travail pour N=150 et comparer les fréquences et les probabilités dans les deux cas. » Deux captures d'écran Excel (lues à 200 dpi) :
- Capture 1 (N=25) : colonnes Dé1, Dé2, Somme, Valeurs (2 à 12), Effectifs, Fréquence 25, Probabilité. Effectifs imprimés pour les valeurs 2..12 : 2, 1, 3, 1, 3, 3, 2, 2, 5, 1, 0 ; Fréquence 25 : 0,08 ; 0,04 ; 0,12 ; 0,04 ; 0,12 ; 0,12 ; 0,08 ; 0,08 ; 0,2 ; 0,04 ; 0. Colonne Probabilité (valeurs théoriques, arrondies) pour S = 2..12 : 0,028 ; 0,056 ; 0,083 ; 0,111 ; 0,139 ; 0,167 ; 0,139 ; 0,111 ; 0,083 ; 0,056 ; 0,028. Histogramme « Fréquence 25 » / « Probabilité » (axe des x gradué 1 à 11).
- Capture 2 (N=25 et N=150) : colonnes Valeurs (2..12), Effectifs 25 : 1, 2, 2, 2, 1, 2, 1, 7, 2, 1, 0 ; Effectifs 150 : 5, 9, 20, 20, 20, 20, 18, 15, 12, 8, 3 ; Fréquence 25 : 0,04 ; 0,08 ; 0,08 ; 0,08 ; 0,04 ; 0,08 ; 0,04 ; 0,28 ; 0,08 ; 0,04 ; 0 ; Fréquence 150 : 0,033333333 ; 0,06 ; 0,133333333 ; 0,133333333 ; 0,133333333 ; 0,133333333 ; 0,12 ; 0,1 ; 0,08 ; 0,053333333 ; 0,02 ; Probabilité : mêmes 11 valeurs que ci-dessus. Deux histogrammes (« Fréquence 25 »/« Probabilité » et « Fréquence 150 »/« Probabilité », axe « Axe des abscisses »).
- Recomptes : effectifs 150 = 150 (exact) ; effectifs 25 de la capture 1 = 23, de la capture 2 = 21 (≠ 25), voir § Notes.

---

#### 5. EXERCICES ET PROBLÈMES (pp. 261-271)

##### 1 - Une seule des réponses proposées est exacte (pp.261-262) — tableau de QCM, colonnes a / b / c
- **Q1.** « Le tableau ci-dessous donne les résultats d'un sondage effectué dans une population de 50 individus : »

| | Fumeur | Non fumeur |
|---|---|---|
| Homme | 5 | 15 |
| Femme | 10 | 20 |

 « Si l'on interroge au hasard l'un d'entre eux, la probabilité que l'interrogé soit non fumeur sachant que c'est un homme, est : » a : 0,75 ; b : 0,2 ; c : 0,08. (5+15+10+20 = 50.)
- **Q2.** « Au cours d'un concert, un amateur vidéo a enregistré 30 morceaux, 18 morceaux avec guitaristes, 24 avec pianistes, et 12 avec guitaristes et pianistes. Il visionne au hasard un des morceaux enregistrés : on note : A : « Le morceau choisi est avec guitaristes sachant qu'il est avec pianistes » On a : p(A) est égale : » a : 2/5 ; b : 1/2 ; c : 2/3.
- **Q3.** « Dans l'expérience décrite à la question Q2. on note B : Le morceau choisi est avec pianistes ; C : Le morceau choisi est avec guitaristes. On a : » a : B et C sont indépendants ; b : B et C ne sont pas indépendants ; c : B et C sont incompatibles.
- **Q4.** « Une expérience aléatoire est représentée par l'arbre ci-dessous : » arbre : racine→A 0,5 ; A→B 0,9 ; (A→B̄ non pondérée) ; racine→Ā (non pondérée) ; Ā→B 0,3 ; (Ā→B̄ non pondérée). « On a donc » a : P(B/A) = 0,8 ; b : p(Ā ∩ B) = 0,15 ; c : p(A ∩ B) = 0,5.
- **Q5.** « Dans l'expérience décrite à la question Q4. … » a : A et B sont indépendantes ; b : P(B) = 0,60 ; c : P(B) = 0,15. (Libellé « Q4. … » imprimé tel quel.)
- **Q6.** « On lance une pièce de monnaie trois fois de suite. X est la variable aléatoire prenant pour valeurs le nombre de fois où pile est apparu. p(X=2) = … » a : 1/2 ; b : 3/8 ; c : 1/8.
- **Q7.** « La loi de probabilité d'une variable aléatoire X est donnée ci dessous. [a1 : 1, 2, 3, 4 ; p(X=a1) : 0,2 ; 0,4 ; 0,1 ; 0,3] On a » a : E(X)=11 ; b : V(X)=5/2 ; c : σ(X)=√5/2. (Somme des probabilités = 1,0.)

##### 2 - (p.262) : « On lance un dé régulier à six faces. Calculer la probabilité que le nombre obtenu soit : a. pair et strictement supérieur à 4. b. pair sachant qu'il est strictement supérieur à 4. c. strictement supérieur à 4 sachant qu'il est pair. »

##### 3 - (p.262) : « Une urne contient cinq jetons blancs numérotés 1, 2, 3, 4, 5 et deux jetons noirs numérotés 1, 2. On tire un jeton au hasard. Calculer la probabilité : a. qu'il soit noir et pair. b. qu'il soit noir sachant qu'il est pair. c. qu'il est [sic] pair sachant qu'il est noir. »

##### 4 - (p.262) : « Dans un groupe de 50 personnes, composé de 30 femmes et 20 hommes, 25 personnes ont moins de 30 ans, dont 15 sont des femmes. On interroge au hasard une personne du groupe et on note : F : « être une femme » ; et J : « avoir au moins de 30 ans ». 1) Recopier et compléter le tableau ci-dessous. »

| | F | F̄ | (colonne total, sans titre) |
|---|---|---|---|
| J | | | |
| J̄ | | | |
| (ligne total, sans titre) | 0,6 | | |

« 2) Calculer la probabilité de chacun des évènements suivants A « La personne interrogée est une jeune femme ». B « La personne interrogée est une femme sachant qu'elle a moins de 30 ans » C « La personne interrogée a moins de 30 ans sachant que c'est une femme » »

##### 5 - (p.263) : « Dans un lycée, 60% sont des filles, 40% sont des élèves externes, dont 50% sont des filles. On prend au hasard la fiche d'un élève de ce lycée. On note : F : « l'élève est une fille » et E : « l'élève est externe » 1. Traduire ces informations dans un tableau à double entrée. 2. Calculer la probabilité de chacun des évènements suivants F, E et G « Obtenir la fiche d'une élève externe ». »

##### 6 - (p.263) — tickets de caisse : « Dans un magasin on a relevé le mode de paiement et le montant M (en DT) mentionnés sur 250 tickets de caisse. On a constaté que : • Tous les achats strictement inférieurs à 10DT sont payés en espèces ; • La moitié des achats dont le montant M est tel que 10 ≤ M < 20 est payé en espèces ; • 16 % des achats sont payés par carte de crédit ; • 36 % des achats ne sont pas payés en espèces. 1. Recopier et remplir le tableau ci-dessous à l'aide des informations données »

| Mode de paiement \ Montant | M<10 | 10 ≤ M < 20 | M ≥ 20 | Total |
|---|---|---|---|---|
| Espèces | | 38 | | |
| Chèque | | | | |
| Carte de Crédit | | 15 | | |
| Total | 106 | | | 250 |

« 2. On choisit au hasard un ticket de caisse et on considère les événements : A : « Le ticket indique un montant supérieur à 20 DT » B : « Le ticket correspond à un paiement par chèque ». C « Le ticket correspond à un paiement par chèque et indique un montant supérieur à 20 DT » Calculer les probabilités des événements : A, B et C. 3. On choisit un ticket de caisse correspondant à un paiement par chèque. Quelle est la probabilité qu'il indique un montant supérieur à 20 DT ? »

##### 7 - (p.263) : « Deux évènements A et B vérifient : P(A) = 0,4 ; P(B) = 0,5 ; P(A ∪ B) = 0,7. Sont-ils indépendants ? Sont-ils incompatibles ? »

##### 8 - (pp.263-264) — restructuration : « Dans le cadre d'une prévision de restructuration, la direction d'une entreprise a fait une enquête auprès de ses employés. Le siège social devra être placé dans une autre ville, il s'agit de prévoir combien d'employés sont susceptibles de changer de lieu de travail. Les résultats sont consignés dans le tableau suivant : »

| | célibataire | marié | Total |
|---|---|---|---|
| Refuse de changer de lieu de travail | 13% | | 65% |
| Accepte de changer de lieu de travail | | | |
| total | | | 100% |

« On choisit au hasard un employé de l'entreprise. On s'intéresse aux événements suivants : A : « l'employé accepte de changer de lieu de travail » ; B : « l'employé est célibataire » ; 1. Recopier et compléter le tableau ci-dessus sachant que les évènements A et B sont indépendants. 2. Quelle est la probabilité pour qu'l'employé choisi accepte de changer de lieu de travail sachant qu'il est marié ? »

##### 9 - (p.264) : « Compléter l'arbre pondéré suivant : [racine→A (non pondérée), racine→B 0,3 ; A→C 0,4 ; A→D (non pondérée) ; B→C (non pondérée) ; B→D 0,7] Calculer p(A∩C) ; p(A∩D) ; p(B∩C) et p(C). »

##### 10 - (p.264) : « Avec les données figurant sur l'arbre ci-dessous, calculer p(B) [arbre : racine→A 0,2 ; A→B 0,6 ; A→B̄ (non pondérée) ; racine→Ā (non pondérée) ; Ā→B (non pondérée) ; Ā→B̄ 0,5] 1. En déduire la probabilité de “A sachant B”. 2. Utiliser les résultats obtenus pour compléter le tableau ci-dessous : »

| | B | B̄ | (total) |
|---|---|---|---|
| A | 0,12 | | 0,2 |
| Ā | | | |
| (total) | | | |

##### 11 - (p.264) : « Une expérience aléatoire où interviennent deux événements A et B est modélisée par l'arbre suivant : [racine→A 1/5 ; A→B 1/6 ; autres branches non pondérées (A→B̄, racine→Ā, Ā→B, Ā→B̄)] Avec les seuls renseignements donnés, pouvez vous écrire, sur les branches toutes les probabilités manquantes. On suppose que les deux événements A et B sont indépendants. Montrer Ā et B sont indépendants. Recopier et compléter l'arbre précédent. »

##### 12 - (p.264) — dés bleu et blanc : « Des enfants jouent avec deux dés, l'un bleu tétraédrique à 4 faces numérotées de 1 à 4 et l'autre blanc à 6 faces numérotées de 1 à 6. **Règle du jeu :** On lance les deux dés. La partie est gagnée si le dé bleu tétraédrique indique 4 ou si le dé blanc indique 1 ou 6. Toutes les autres configurations sont perdantes. Un enfant joue une partie. On note : G : « la partie est gagnante » ; A : « le dé tétraédrique indique une face autre que 4 ». 1. a. Donner les probabilités P(A) et P_A(G). b. Calculer la probabilité P(G). 2. Déterminer la probabilité que l'on ait obtenu 4 au dé à quatre faces, sachant que la partie est gagnée. »

##### 13 - (p.265) — école de commerce : « Une école de commerce a effectué une enquête, en janvier 2000, auprès de ses jeunes diplômés des trois dernières promotions, afin de connaître leur insertion professionnelle. A la première question, trois réponses et trois seulement sont proposées : - A : « La personne a une activité professionnelle » ; - B : « La personne poursuit ses études » ; - C : « La personne recherche un emploi ». On a constaté que 60% des réponses ont été envoyées par des filles. Dans l'ensemble des réponses reçues, on a relevé les résultats suivants : *65 % des filles et 55 % des garçons ont une activité professionnelle ; * 20 % des filles et 15 % des garçons poursuivent leurs études. 1. On prend au hasard la réponse d'un jeune diplômé. a. Recopier et compléter l'arbre ci-dessous : » arbre : racine→F 0,60 ; F→A 0,65 ; F→B, F→C non pondérées ; racine→G (non pondérée) ; G→B 0,15 ; G→A, G→C non pondérées (le « 0,15 » est inscrit sur la branche G→B). « Montrer que la probabilité qu'il poursuive ses études est égale à 0,18. b. Calculer la probabilité qu'il exerce une activité professionnelle. 2. On prend au hasard la réponse d'une personne qui poursuit ses études ; quelle est la probabilité que ce soit la réponse d'une fille (on donnera le résultat sous forme fractionnaire) ? 3. On prend au hasard la réponse d'une personne à une activité professionnelle ; quelle est la probabilité que ce soit la réponse d'un garçon ? »

##### 14 - (pp.265-266) — calculatrices : « Une entreprise vend des calculatrices d'une certaine marque. Le service après-vente s'est aperçu qu'elles pouvaient présenter deux types de défauts, l'un lié au clavier et l'autre lié à l'affichage. Des études statistiques ont permis à l'entreprise d'utiliser la modélisation suivante : la probabilité pour une calculatrice tirée au hasard de présenter un défaut de clavier est égale à 0,04. En présence du défaut de clavier, la probabilité que la calculatrice soit en panne d'affichage est de 0,03. Alors qu'en l'absence de défaut de clavier, la probabilité de ne pas présenter de défaut d'affichage est 0,94. On note : - C l'événement : « La calculatrice présente un défaut de clavier » ; - A l'événement : « La calculatrice présente un défaut d'affichage ». Dans cet exercice, les probabilités seront écrites sous forme de nombres décimaux arrondis au millième.
1. a. Préciser à l'aide de l'énoncer [sic] les probabilités suivantes : p_C̄(Ā), p_C(A) et p(C) b. Construire un arbre pondéré décrivant cette situation.
2. On choisit une calculatrice de cette marque au hasard. a. Calculer la probabilité que la calculatrice présente les deux défauts. b. Calculer la probabilité pour que la calculatrice présente le défaut d'affichage mais pas le défaut de clavier. c. En déduire p(A). d. Montrer que la probabilité de l'événement « la calculatrice ne présente aucun défaut » arrondie au millième est égale à 0,902.
3. Un client choisit successivement au hasard trois calculatrices de cette marque. On admet que le nombre des calculatrices est suffisamment important pour que le choix des 3 calculatrices soit assimilé à 3 tirages indépendants. a. Calculer la probabilité pour que les trois calculatrices ne présentent aucun défaut. b. Calculer la probabilité pour qu'au moins une calculatrice ait un défaut. »

##### 15 - (p.266) : « Une variable aléatoire Y prend les valeurs 3, 4, 5, et 6. Quelle est la loi de probabilité de Y sachant que : p(Y > 5) = 1/2 ; p(Y < 5) = 1/3 et p(Y = 3) = p(Y = 4) ? Calculer l'espérance mathématique E(Y) et l'écart type √V(Y). » (la couche texte donne « V(Y) », l'image « √V(Y) » : à l'image, c'est bien la racine)

##### 16 - (p.266) : « Une variable aléatoire X prend les valeurs 1, 2, 3 ou 4. Déterminer sa loi de probabilité et son espérance mathématique E(X) dans chacun des cas suivants : 1. La probabilité p(X = xi) est proportionnelle à la valeur xi de la variable aléatoire. 2. La probabilité p(X = xi) est proportionnelle au carré de la valeur xi. 3. La probabilité p(X = xi) est inversement proportionnelle à la valeur de xi. »

##### 17 - (p.266) — vendeur de livres : « Pendant 100 jours un vendeur de livres a relevé le nombre de contrats qu'il a fait signer par jour : »

| Contrat signé xi | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Nombre de jour | 25 | 37 | 22 | 10 | 6 |

(25+37+22+10+6 = 100 : exact.)
« L'employeur de ce vendeur estime que la probabilité pour que son vendeur obtienne X contrats, un jour donné, est égale à la fréquence de ce nombre de contrats xi pour les cents jours étudiés. Calculer l'espérance de vente de ce vendeur. Calculer l'écart type de X. Si ce vendeur touche 40 DT par contrat signé, quelle est son espérance de gain » (sans point d'interrogation final imprimé)

##### 18 - (pp.266-267) — société PAPEX : « Lors d'une étude de marché, la société PAPEX (société de fabrication de papiers) a étudié la répartition de ses clients selon deux critères, leur besoin en papier et leur possibilité de financement : 35 % de ses clients utilisent moins de 12 tonnes de papier par ans [sic] et, parmi ceux-ci, 80 % sont solvables. 40 % de ses clients utilisent de 12 à 20 tonnes de papier par an et, parmi ceux-ci, 85 % sont solvables. Pour le reste de ses clients, seul 10 % ne sont pas solvables. 1. La société choisit au hasard l'un de ses clients. Quelle est la probabilité : a. Pour qu'il utilise plus de 20 tonnes de papier ? b. Pour qu'il ne soit pas solvable ? 2. La société désire relancer ses clients solvables. Elle choisit au hasard l'un de ses clients solvables. Quelle est la probabilité pour qu'il utilise au plus 20 tonnes de papier ? 3. La société établit un échantillon de 20 de ses clients choisis au hasard. On désigne par X la variable aléatoire égale au nombre de clients solvables parmi ces 20 clients. a. Déterminer la loi de X et son espérance. Interpréter concrètement la réponse. b. Calculer la probabilité de l'événement (X = 4). »

##### 19 - (p.267) — location de portables : « Une société de location de matériel informatique propose exclusivement deux types de portable A ou B, avec ou sans lecteur DVD. Une étude statistique, sur l'ensemble des clients louant un portable dans les magasins de cette société, a permis d'établir que 60% de ces clients louent un ordinateur portable de type A, et, parmi ceux-ci, 20% désirent un lecteur DVD. En revanche, 70% des clients louant un portable B demandent un lecteur DVD. On choisit au hasard un client louant un portable et on considère les événements : A : « le client loue un portable A » ; C : « le client loue un portable A avec lecteur DVD ». D : « le client loue un portable avec lecteur DVD ». 1. a. Déterminer les probabilités de ces événements. b. Déterminer la probabilité que le portable soit de type A sachant qu'il a un lecteur DVD. 2. On suppose que le nombre de client est suffisamment important pour que la probabilité de louer un portable avec lecteur DVD soit identique pour chacun des clients indépendant les uns des autres. On choisit trois clients au hasard. Soit X la variable aléatoire prenant pour valeurs le nombre des clients qui ont loué un portable avec un lecteur DVD. a. Quelle est la probabilité que les trois clients louent un portable avec lecteur DVD ? b. Déterminer la loi de probabilité de X. Calculer son espérance. »

##### 20 - (p.267) — tireur à l'arc : « Un tireur à l'arc envoie 10 flèches sur une cible. On admet que chaque tir est indépendant des précédents et que la probabilité d'atteindre la cible est pour chaque tir égale à 0,75. 1. Justifier que l'expérience décrite ci-dessous [sic] est un schéma de Bernoulli. En préciser les paramètres. 2. Calculer la probabilité : a. d'attendre [sic, pour « atteindre »] exactement 7 fois la cible. b. d'attendre exactement une fois la cible. c. d'attendre au moins 5 fois la cible. (Les résultats seront arrondis à trois décimales.) 3. On appelle X la variable aléatoire égale au nombre de fois où la cible est atteinte. a. Calculer l'espérance de X. b. Calculer la probabilité des événements : (X ≤ 1) et (3 < X ≤ 5) »

##### 21 - (p.268) — deux dés, 5 lancers : « On lance deux dés parfaitement équilibrés 5 fois de suite, et à chaque lancer, on calcule la somme des deux numéros sortis. 1. Calculer la probabilité pour que le lancer des deux dés donne une somme égale à 7. (On pourra constituer un tableau à double entré [sic] répertoriant tous les cas possibles.) 2. Soit X la variable aléatoire égale au nombre de lancers (parmi les cinq) dont la somme des numéros sortis est égale à 7. Justifier que la loi de X est une loi binomiale dont on précisera les paramètres. 3. Calculer la probabilité des événements : a. (X = 0) b. (X ≥ 1) c. (1 ≤ X < 5) 4. Calculer l'espérance de X. (Les résultats seront arrondis à deux décimales.) 5. Calculer V(X) et σ(X). »

##### 22 - (p.268) — urne 4 rouges / 3 noires : « Une urne contient 4 boules rouges et 3 boules noires. On extrait simultanément et au hasard 2 boules de l'urne. 1. Calculer la probabilité d'extraire deux boules noires. 2. On extrait n fois de suite 2 boules simultanément, en les remettant dans l'urne après chaque tirage. Soit X la variable aléatoire égale au nombre de tirages parmi les n, dont le résultat est 2 boules noires. Justifier que la variable aléatoire X suit une loi binomiale dont on précisera les paramètres. 3. a. Calculer en fonction de n la probabilité pn d'extraire au moins une fois 2 boules noires. b. déterminer le plus petit entier n vérifiant pn ≥ 0,99. 4. a. calculer en fonction de n l'espérance de X b. Déterminer le plus petit n1 tel que l'espérance de X soit supérieure ou égale à 2. »

##### 23 - (pp.268-269) — donateur, suite : « A partir de 2001, une association d'aide à la recherche médicale envoie chaque année à Monsieur X un courrier pour l'inviter à l'aider financièrement par un don. Monsieur X a répondu favorablement en 2001 en envoyant un don. On admet que, chaque année à partir de 2002, la probabilité pour que Monsieur X fasse un don est égale à 0,9 s'il a fait un don l'année précédente et à 0,4 s'il n'a rien donné l'année précédente. On note pour tout entier naturel n : • En l'événement : « Monsieur X est donateur en 2002+n » ; • Pn la probabilité de En ;
1- Traduire les données en formes de probabilités conditionnelles concernant les événements En+1, En, Ēn.
2- a. Précisez la valeur de P0. b. Calculez P(E1 ∩ E0) et P(E1 ∩ Ē0). Déduisez-en la valeur de P1.
3- a. Montrez que P(En+1 ∩ En) = 0.9 Pn et que P(En+1 ∩ Ēn) = 0.4(1 − Pn) pour tout entier n. b. Déduisez-en que Pn+1 = 0.5Pn + 0.4 pour tout entier n. c. Quelle est la probabilité pour que Monsieur X soit donateur en 2005 ?
4- On déduit une suite (Un) en posant pour tout entier naturel n : Un = Pn – 0,8. a. Démontrez que la suite (Un) est géométrique. Précisez sa raison et son premier terme. b. Exprimez (Un) en fonction de n. c. Déduire que Pn = 0,1 x 0,5^n + 0,8 pour tout entier naturel n. d. Calculez (0,5)^5, (0,5)^10, (0,5)^20 et ensuite P0, P10, P20. »

##### Problème 1 - (p.269) — sondage téléphonique : « Une entreprise confie à une société de sondage par téléphone une enquête sur la qualité de ses produits. On admet que lors du premier appel téléphonique, la probabilité que le correspondant ne décroche pas est 0,4 et que s'il décroche, la probabilité pour qu'il réponde au questionnaire est 0,3. On pourra construire un arbre pondéré.
1. On note : • D1 l'évènement : « la personne décroche au premier appel » ; • R1 l'évènement « la personne répond au questionnaire lors du premier appel ». Calculer la probabilité de l'évènement R1.
2. Lorsqu'une personne ne décroche pas au premier appel, on la contacte une seconde fois. La probabilité pour que le correspondant ne décroche pas la seconde fois est 0,3 et la probabilité pour qu'il réponde au questionnaire sachant qu'il décroche est 0,2. Si une personne ne décroche pas lors du second appel, on ne tente plus de la contacter. On note : • D2 l'évènement : « la personne décroche au second appel ». • R2 l'évènement : « la personne répond au questionnaire lors du second appel ». • R l'évènement : « la personne répond au questionnaire ». Montrer que la probabilité de l'évènement R est 0,236.
3. Sachant qu'une personne a répondu au questionnaire, calculer la probabilité pour que la réponse ait été donnée lors du premier appel. (On donnera la réponse arrondie au millième)
4. Un enquêteur a une liste de 25 personnes à contacter. Les sondages auprès des personnes d'une même liste sont indépendants. Quelle est la probabilité pour que 20% des personnes répondent au questionnaire ? (On donnera la réponse arrondie au millième) »

##### Problème 2 - (pp.269-270) — billes : « Pour les questions 1 et 2, on donnera les résultats sous forme de fraction et sous forme décimale approchée par défaut à 10^−3 près. Un enfant joue avec 20 billes : 13 rouges et 7 vertes. Il met 10 rouges et 3 vertes dans une boîte cubique et 3 rouges et 4 vertes dans une boîte cylindrique.
1. Dans un premier jeu, il choisit simultanément trois billes au hasard dans la boîte cubique et il regarde combien de billes rouges il a choisies. On appelle X la variable aléatoire correspondant au nombre de billes rouges choisies. a. Déterminer la loi de probabilité de X. b. Calculer l'espérance mathématique de X.
2. Un deuxième jeu est organisé de telle sorte que l'enfant choisisse d'abord au hasard une des deux boîtes, puis qu'il prenne alors une bille, toujours au hasard, dans la boîte choisie. On considère les évènements suivants : C1 : « L'enfant choisit la boîte cubique », C2 : « L'enfant choisit la boîte cylindrique », R : « L'enfant prend une bille rouge », V : « L'enfant prend une bille verte ». a. Représenter par un arbre pondéré la situation correspondant à ce deuxième jeu. b. Calculer la probabilité de l'évènement R. c. Sachant que l'enfant a choisi une bille rouge, quelle est la probabilité qu'elle provienne de la boîte cubique ?
3. L'enfant reproduit n fois de suite son deuxième jeu, en remettant à chaque fois la bille tirée à sa place. a. Exprimer, en fonction de n, la probabilité pn que l'enfant ait pris au moins une bille rouge au cours de ses n choix. b. Calculer la plus petite valeur de n pour laquelle pn ≥ 0,99. »
(10+3+3+4 = 20 ; 10+3 = 13 rouges, 3+4 = 7 vertes : bille comptes cohérents.)

##### Problème 3 - (p.270) — écrans plasma : « Un fabricant d'écrans plasma teste une première fois ses appareils à la sortie de la chaîne de fabrication. Si le test est positif (c'est-à-dire si l'écran fonctionne correctement), l'écran est acheminé chez le client. Sinon l'écran retourne en usine où il est réparé puis testé une seconde fois. Si ce deuxième test est positif, l'écran est acheminé chez le client, sinon il est détruit. Une étude statistique a permis de montrer que le test est positif pour 70% des écrans neufs sortis directement des chaînes de fabrication, mais que parmi les écrans réparés, seulement 65% d'entre eux passent le second test avec succès. On note T1 l'évènement : « le premier test est positif ». On note C l'évènement : « l'écran est acheminé chez le client ».
1. On choisit un écran au hasard à la sortie de la chaîne de fabrication. Déterminer les probabilités des évènements T1, et C.
2. La fabrication d'un écran revient à 300 DT au fabricant si l'écran n'est testé qu'une fois. Cela lui coûte 50 DT de plus si l'écran doit être testé une seconde fois. Un écran est facturé a euros (a étant un réel positif) au client. On introduit la variable aléatoire X qui, à chaque écran fabriqué, associe le « gain » (éventuellement négatif) réalisé par le fabricant. a. Déterminer la loi de probabilité de X en fonction de a. b. Exprimer l'espérance de X en fonction de a. c. À partir de quelle valeur de a, l'entreprise peut-elle espérer réaliser des bénéfices ? »
(Unités : coûts en DT, prix de facturation « a euros » : incohérence d'unité imprimée, voir § Notes.)

##### Problème 4 - (p.270) — personnel d'un hôpital : « Le personnel d'un très grand hôpital est réparti en trois catégories : les médecins, les soignants (non médecins) et le personnel AT (administratif ou technique). 12% des personnels sont des médecins et 71% sont des soignants. 67% des médecins sont des hommes et 92% des soignants sont des femmes. On donnera une valeur approchée de tous les résultats à 10^−4 près.
1. On interroge au hasard un membre du personnel de cet hôpital. a. Quelle est la probabilité d'interroger une femme soignante ? b. Quelle est la probabilité d'interroger une femme médecin ? c. On sait que 80% du personnel est féminin. Calculer la probabilité d'interroger une femme AT. En déduire la probabilité d'interroger une femme sachant que la personne interrogée fait partie du personnel AT.
2. Une entreprise souhaite envoyer un courrier publicitaire à 40 personnes qui travaillent dans cet hôpital. Elle a la liste du personnel mais ne connaît pas la fonction de chacun. Elle choisit au hasard 40 noms de la liste (en raison de la taille de la population, on considère qu'il s'agit de 40 tirages successifs indépendants avec remise). Quelle est la probabilité que, sur les 40 courriers envoyés, 10 exactement soient reçus par des médecins ? »

##### Problème 5 - (p.271) — cible et fonction x·e^x
« **Première partie** Calculer l'intégrale ∫_0^1 x e^x dx.
**Deuxième partie** La figure ci-contre représente une cible rectangulaire OIMN telle que, dans le repère orthonormé (O ; OI→ ; OJ→), la courbe C reliant le point O au point M est une partie de la courbe représentative de la fonction f définie sur R par f(x) = x e^X [sic, « X » majuscule imprimé en exposant]. Cette courbe partage la cible OIMN en deux parties A et B comme l'indique la figure ci-dessous. Un jeu consiste à lancer une fléchette qui atteint soit l'extérieur de la cible, soit l'une des parties A ou B. On admet que la fléchette ne peut atteindre aucune des frontières de la cible, ni la courbe C. Une étude statistique a montré que la fléchette tombe à l'extérieur de la cible avec une probabilité de 1/2 et que les probabilités d'atteindre les parties A et B sont proportionnelles à leurs aires respectives.
1. Démontrer que la probabilité d'atteindre la partie A est égale à 1/(2e). Quelle est la probabilité d'atteindre la partie B ?
2. On lance de manière indépendante trois fléchettes. a. Soit X la variable aléatoire qui est égale au nombre de fléchettes ayant atteint la partie A. Définir la loi de probabilité de X. En déduire la valeur exacte de son espérance mathématique. b. Soit E l'évènement : « Exactement deux fléchettes atteignent la partie A ». Calculer une valeur approchée au millième de la probabilité de E. c. Soit F l'évènement : « les trois fléchettes atteignent la partie B ». Calculer la probabilité de F (on donnera la valeur exacte). Sachant qu'aucune fléchette n'a atteint l'extérieur de la cible, quelle est la probabilité que toutes les trois se trouvent dans la partie B ?
3. On lance cette fois de manière indépendante n fléchettes. a. Déterminer en fonction de n la probabilité pn pour qu'au moins une des fléchettes atteigne la partie A. b. Déterminer le plus petit naturel n tel que pn ≥ 0.99. »
Figure (lue à l'image) : rectangle OIMN (N en haut à gauche, M en haut à droite, O en bas à gauche, I en bas à droite, J sur l'axe vertical près de O) ; la courbe C va de O à M ; « Partie B » au-dessus de la courbe (zone gauche/haut), « Partie A » entre la courbe et le côté OI (zone basse-droite). Un trait vertical épais marque le segment OJ.
Remarque de cohérence (ne pas inventer de corrigé) : ∫_0^1 x e^x dx = 1 est le résultat classique de la 1re partie ; aire de la cible = f(1)×1 = e, d'où l'énoncé 1/(2e) ; le manuel ne le détaille pas.

---

#### 6. MATH CULTURE (p.272) — « De la statistique aux probabilités »
Texte verbatim (colonne gauche) : « Au XVIème siècle, à la cour des rois de France, les questions sur les jeux de hasard conduisent Pascal et Fermat à élaborer une approche quantitative du hasard. Ainsi, en 1654, Pascal adresse à l'Académie Parisienne des Sciences sa "nouvelle géométrie du hasard [...] joignant la rigueur des démonstrations de la science à l'incertitude du sort, et conciliant ces deux choses d'apparence contradictoire". Mais c'est en 1714 que paraît une oeuvre capitale qui fera le lien entre statistique et probabilité : Ars Conjectandi du suisse Jacques Bernoulli. Celui-ci y énonce un théorème important : la probabilité de l'apparition d'un résultat dans une épreuve est "pratiquement égale" à la fréquence d'apparition de ce résultat quand on a répété un grand nombre de fois cette même épreuve. Ainsi fut fait le lien entre probabilité et statistique. »
Colonne droite, « Une autre approche ... » : « On vient de lancer un dé un millier de fois et on a trouvé que la fréquence d'apparition de la face 6 est 0,1335. On veut lancer le dé une fois de plus ce dé, et on ce pose la question : "Quelle sont les chances d'obtenir la face 6 ?" Si les statistiques descriptives sont statiques, les probabilités sont dynamiques : il y a toujours une action liée à la situation, et suivant celle-ci, on s'intéresse à ce qui peut arriver. »
Illustration : portrait, légende « Jacques Bernoulli (1654-1705) — Mathématicien suisse, il compléta le calcul infinitésimal de Leibniz et posa les fondements du calcul des probabilités ».
Source citée : aucune source bibliographique imprimée (texte non attribué ; seule la légende du portrait).
Coquille d'époque : « Au XVIème siècle » alors que 1654 et 1714 relèvent du XVIIe/XVIIIe siècle (imprimé tel quel).

---

#### 7. VOCABULAIRE OFFICIEL, BORNES, NOTIONS-CLÉS

**Vocabulaire exact** : probabilité conditionnelle (p(B/A), p_A(B)) · formule des probabilités composées · événements indépendants / incompatibles · arbre pondéré, nœud, branche, chemin · partition de E · formule des probabilités totales · formule de Bayes · variable aléatoire (application X de E vers IR), (X = xi) · loi de probabilité · espérance mathématique E(X) · variance V(X) · écart type σ(X) · jeu équitable / favorable ou gagnant / défavorable ou perdant · gain algébrique · épreuve de Bernoulli, succès S, échec E · schéma de Bernoulli · loi binomiale de paramètres (n,p) · événements élémentaires, issues, équiprobabilité · tirage simultané / successif sans remise / avec remise.

**Bornes INCLUS** (ce que le manuel traite) : p(B/A) définition ; composées (2 événements, puis n ≥ 2) ; indépendance (définition, caractérisation par p(A/B)=p(A), incompatible ≠ indépendant) ; arbres pondérés (somme des branches d'un nœud = 1 ; produit le long d'un chemin) ; probabilités totales (partition A1…An) ; Bayes (forme à deux événements A, Ā) ; variable aléatoire discrète finie, loi, E(X), V(X) = Σ(xi − E(X))² pi, V(X) = E(X²) − [E(X)]², σ(X) ; jeux équitable/favorable/défavorable ; épreuve et schéma de Bernoulli ; loi binomiale p(X=k) = C(n,k) p^k q^(n−k), E(X) = np, V(X) = npq (ADMIS) ; intervalle [E(X) − 2σ(X), E(X) + 2σ(X)] (act. 5 p.257) ; simulation Excel de deux dés (ENT(6*ALEA()+1), NB.SI).
**Bornes EXCLU** (rien au manuel dans ces pages) : formule de Bayes à n hypothèses (seule la version à A et Ā est encadrée) ; démonstration de E(X)=np et V(X)=npq (admis) ; variables aléatoires continues / loi normale ; probabilité conditionnelle étendue p(·/A) comme probabilité (aucun énoncé) ; table de la loi binomiale ; inégalité de Bienaymé-Tchebychev ; fonction de répartition ; E(aX+b), V(aX+b) (aucun encadré).

**Notions-clés (≤ 8)** : (1) p(B/A)=p(A∩B)/p(A) ; (2) composées p(A∩B)=p(A/B)p(B) et généralisation ; (3) indépendance p(A∩B)=p(A)p(B) ; (4) arbre pondéré (règles de nœud/chemin) ; (5) totales + Bayes ; (6) loi de probabilité, E(X), V(X)=E(X²)−[E(X)]², σ(X) ; (7) épreuve/schéma de Bernoulli ; (8) loi binomiale (n,p), E(X)=np, V(X)=npq.

---

#### 8. § NOTES (fidélité, coquilles, pages lues)

**Pages lues** : 36/36 (237 à 272), toutes lues à la fois en couche texte (`pdftotext -layout`) et à l'image (110 dpi). La page 237 n'a pas de couche texte (page de titre graphique) : lue à l'image uniquement.

**Pages sondées à l'agrandissement (200 dpi)** : 252 (tableaux X et Y de l'activité 1 de Variance) ; 260 (les deux captures d'écran Excel). Les formules, fractions, intégrales, ≤, ∩, ∪ des autres pages ont été vérifiées à l'image 110 dpi, sans doute résiduel.

**Coquilles et incohérences imprimées (reproduites telles quelles) :**
1. **p.252, Variance, Activité 1** : tableau de Y imprimé yi = −1, 0, 1 ; pi = 1/7, 3/7, 1/7 (somme 5/7 ≠ 1, confirmé à 200 dpi). Les probabilités de X (1/7, 4/7, 2/7) somment bien à 1 mais donnent E(X) = −2/7 (calcul de contrôle de ma part), alors que le texte demande « Vérifier que E(X) = E(Y) » et que Y tel qu'imprimé a E(Y)=0 : le tableau de Y est donc faux tel quel (cause probable : 3/7 ; 3/7 ; 1/7, qui donnerait E(Y)=−2/7 — hypothèse, non imprimée, `[?]`). À signaler aux auteurs de chapitre : ne pas reprendre ce tableau tel quel.
2. **p.240, tableau RTT** : les deux lignes sont libellées toutes deux « Salarié » (les libellés F1 et F2 sont perdus à l'impression) ; 10, 300, 40, 150, total 500 corrects.
3. **p.240, Remarque** : « Dans le cas où p(B) = 0, on convient de poser p(A/B) = 0 » (devrait être p(A) = 0 ⇒ p(B/A) = 0 pour cadrer avec la définition p(B/A) ; imprimé ainsi).
4. **p.242, Composées, Activité 1** : « Préciser p(G) et p(G/R) » — vraisemblablement p(R/G) (l'énoncé donne les taux de recrutement par sexe) ; imprimé tel quel.
5. **p.238, Act.1 de « Pour commencer »** : « C : … d'un cadre ».. » (double point imprimé) ; « F ∩ O » listé en dernier.
6. **p.245** : l'événement contraire est écrit « C » barré / « M̄1 » ; l'énoncé de l'activité 3 donne (I) p(M̄1) = 0,004 (la panne), (II)/(III) 0.5 et 0.002 : notation décimale en point, comme imprimé (mélange virgule/point dans le manuel : 0,60 / 0.5 / 0.25).
7. **p.246, Act.4** : arbre partiellement pondéré (0,1 ; 0,4 ; 0 ; 0,4 ; 0,8 ; 0,3) ; les feuilles F3 non pondérées ; le texte dit « deux magasins » mais le tableau a trois lignes (A, B, Autres magasins C).
8. **p.248, Variables aléatoires** : « 23/180 » pour p(G) (Activité 4) : valeur cible imprimée, non recalculée ici.
9. **p.249, Remarque** : « x1, ,……,xn (avec i = 1, ….,n) » (ponctuation brisée imprimée).
10. **p.253** : « V(X) = E(X²) – [E(X)]² » encadré ; la phrase « Pourquoi l'écart type ? » est en italique et non encadrée.
11. **p.255-256, Loi binomiale** : « sucées » pour « succès » (4 occurrences dans l'activité 1) ; arbre imprimé avec premier niveau 1/3 (S) et 2/3 (E) seulement.
12. **p.256, Activité 2** : « qui ont décrochés » (accord) ; k de 0 à 10.
13. **p.257, Activité 4** : « Pour k ∈ {1 ; 2 ; 3 ; 4) » (accolade fermante remplacée par une parenthèse) ; le texte écrit « p1 = 0, 1, p2 = 0,2 et p3 = 0, 3 » (espaces parasites dans « 0, 1 » et « 0, 3 », normalisés ici en 0,1 et 0,3).
14. **p.262, Q4/Q5** : Q5 renvoie à « l'expérience décrite à la question Q4. … » (libellé tronqué imprimé). **Q7** : tableau a1 = 1, 2, 3, 4 ; probabilités 0,2 ; 0,4 ; 0,1 ; 0,3 (somme 1). Les trois réponses proposées : E(X)=11 ; V(X)=5/2 ; σ(X)=√5/2. Contrôle (non imprimé, de ma part) : E(X)=2,5 ; E(X²)=7,5 ; V(X)=1,25=5/4 ; σ(X)=√5/2 : les options a et b imprimées (11 ; 5/2) semblent fausses/tronquées, la c est cohérente — `[?]` sur la clé du manuel, aucune clé imprimée.
15. **p.264, ex. 8** : « qu'l'employé » (coquille). **Ex. 11** : seules les branches racine→A (1/5) et A→B (1/6) sont pondérées.
16. **p.265, ex. 13** : l'arbre ne porte que 0,60 ; 0,65 (F→A) et 0,15 (inscrit sur G→B) ; l'énoncé donne 55 % des garçons en activité (G→A).
17. **p.266, ex. 15** : la couche texte perd la racine carrée de « √V(Y) » ; à l'image la racine est imprimée (aucune coquille).
18. **p.270, Problème 3** : coûts en DT (300 DT, 50 DT) mais prix de vente « a euros » : incohérence d'unité imprimée.
19. **p.271, Problème 5** : f(x) = x e^X (X majuscule en exposant) ; incipit « Calculer l'intégrale ∫_0^1 x e^x dx » (x minuscule).
20. **p.272, Math culture** : « Au XVIème siècle » associé à des dates de 1654 et 1714 (XVIIe/XVIIIe) ; « on ce pose la question » ; « Quelle sont les chances » (fautes imprimées).
21. **p.260, captures Excel** : effectifs de la capture 1 somment à 23 (non 25), ceux de N=25 de la capture 2 à 21 ; effectifs N=150 somment à 150. Les captures sont des illustrations de simulation aléatoire non cohérentes entre elles (les valeurs du tirage diffèrent d'une capture à l'autre). Axes des histogrammes gradués 1 à 11 alors que S varie de 2 à 12.
22. **Typographie générale** : probabilités tantôt avec virgule (0,60), tantôt avec point (0.5 ; 0.25 ; 0.4 ; 0.025 ; 0.9 ; 0.4(1−Pn)) ; « événement » / « évènement » mêlés ; notation « sachant que » = p(B/A) (barre oblique), jamais p_A(B) dans les exercices.

**Corrigés** : aucun corrigé n'est imprimé dans ces pages (rien d'inventé). Seules valeurs-cibles imprimées dans les énoncés : p(G)=23/180 (act.4 Bayes p.248) ; « égale à 0.5 » (pâtisserie p.245) ; p=0,18 (ex.13) ; 0,902 (ex.14.2.d) ; 0,236 (Pb 1.2) ; 1/(2e) (Pb 5.1) ; p1=0,1, p2=0,2, p3=0,3 (act.4 p.257).

**`[?]` restants** : un seul, justifié (note 1, p.252, tableau de Y ; et note 14, clé du Q7 p.262). Aucun `[?]` pour illisibilité : toutes les formules et tous les nombres sont lisibles.

**Remarque d'organisation** : aucune section « Revoir » ni « Math culture » à numéros d'exercices ; la section « Avec l'ordinateur » ne contient qu'une seule activité (simulation Excel, pp.259-260). Les rubriques du cours ne portent pas de numéro d'activité continu : chaque sous-section (1 à 4, puis Variable aléatoire, Espérance, Variance, Bernoulli, Binomiale) recommence à « Activité 1 ».

---

### Chapitre `m10-p273-301`

### m10 — Chapitre X « Les graphes » (manuel 222463P00, pp. 273-301)

Rubriques : Pour commencer (pp. 274), Cours (pp. 275-289 : I Revoir, II Graphes orientés – Matrice associée à un graphe, III Graphes probabilistes), Avec l'ordinateur (pp. 290-291), Exercices et problèmes (pp. 292-299/300, 27 exercices), Math culture (p. 301). p. 273 = page de titre : « Chapitre 10 — LES GRAPHES » ; sommaire du chapitre : Pour commencer ; Cours (Revoir, Graphes orientés, Matrice associée à un graphe, Graphes probabilistes) ; Avec l'ordinateur ; Exercices et problèmes ; Math culture. (En-tête courant des pages : « Chapitre X ».)

Convention : les FIGURES (graphes) sont décrites d'après l'image ; `[?]` = lecture incertaine d'un arc/arête/orientation. Les sommets/nombres écrits dans le texte sont verbatim.

---------------------------------------------------------------------
#### POUR COMMENCER (p. 274)

##### Activité 1 — QCM
« Soit le graphe G ci-dessous. Une seule des réponses proposées est exacte. »
Figure G (lue à l'image) : sommets A, B, C, D, E ; arêtes : E-D, E-A, A-B, B-D (côtés du rectangle E-D-B-A), diagonales E-B et A-D, puis D-C et B-C (triangle D-B-C à droite). Soit 8 arêtes ; degrés A3, B4, C2, D4, E3 (somme 16).

| | a | b | c |
|---|---|---|---|
| Q1. L'ordre de G est… | 6 | 5 | 8 |
| Q2. Le sommet C est… | isolé | de degré 2 | Adjacent au sommet A |
| Q3. La somme des degrés des sommets de G est égale à… | 10 | 12 | 16 |
| Q4. Le graphe G est … | Complet. | Connexe. | Non connexe. |
| Q5. A-B-C-D-B | n'est pas une chaîne de G. | est une chaîne de G. | Est un cycle de G. |
| Q6. E-D-C-D-E est … | une chaîne de longueur 5. | N'est pas une chaîne | une chaîne fermée. |

##### Activité 2
« Dire, en justifiant, si les assertions suivantes sont vraies ou fausses : »
A1 : Un sous graphe d'un graphe complet est complet.
A2 : Un graphe non complet admet un sous graphe complet.
A3 : Un sous graphe d'un graphe connexe est connexe.
A4 : Le nombre de sommets d'un graphe est égal au nombre de ses arêtes.
A5 : La somme des degrés des sommets d'un graphe est paire.
A6 : Un graphe peut avoir un seul sommet de degré impair.
(Aucun corrigé dans le manuel.)

---------------------------------------------------------------------
#### COURS — I- REVOIR (pp. 275-278)

##### 1) Chaîne eulérienne – Cycle eulérien (p. 275)

**Activité 1** — « Dire, en justifiant, si chacun des graphes suivants admet une chaîne eulérienne ou un cycle eulérien et donner, dans l'affirmative, un exemple de telle chaîne ou de tel cycle. » Six petits graphes, SANS lettres de sommets (figure) : (1) 4 sommets : quadrilatère croisé en « papillon/ruban » (2 arêtes qui se croisent) ; (2) 6 sommets avec un sommet interne, un pendant à droite ; (3) pentagone-triangle accolé (5 sommets, 6 arêtes env.) ; (4) triangle + un sommet pendant (4 sommets, 4 arêtes) ; (5) triangle (3 sommets) ; (6) 5 sommets : triangle + 2 sommets liés, un pendant. Arêtes non transcrites au détail [?] (figures non étiquetées).

Encadré — **Théorème d'Euler (admis).**
❖ Un graphe connexe G admet une chaîne eulérienne si et seulement si tous ses sommets sont de degré pair ou deux uniquement de ses sommets sont de degré impair (ce sont les extrémités de la chaîne).
❖ Un graphe connexe G admet un cycle eulérien si et seulement si tous ses sommets sont de degré pair.

Encadré — « Un graphe ayant plus de deux sommets de degré impair ne possède pas de chaîne eulérienne. »

**Activité 2** — « Peut – on dessiner les graphes ci-contre, sans lever le crayon et en ne passant qu'une seule fois sur chaque arête ? » Trois figures : (a) étoile à 5 branches (pentagramme, 5 sommets, 5 arêtes) ; (b) rectangle 4 sommets avec 2 sommets internes reliés entre eux (rectangle + barre centrale, chaque sommet interne relié à deux coins) ; (c) « maison » : carré + toit triangulaire + petit motif intérieur (rectangle avec croix).

**Activité 3** — « Une grande surface est conçue de telle façon que six secteurs (alimentation, hi-fi, etc…) notés A, B, C, D, E, F sont reliés par des allées selon le graphe ci-dessous. »
Figure : E, A, B, F alignés (arêtes E-A, A-B, B-F) ; D au-dessus de A, C au-dessus de B ; arêtes D-A, C-B, D-C ; puis E-D, E-C, A-C, D-F (10 arêtes ; degrés A4 B3 C4 D4 E3 F2).
1. a) Le graphe est-il connexe ? b) Compléter le tableau suivant : (Sommet A B C D E F ; Degré : vide).
2. Un visiteur désire parcourir l'ensemble des allées en ne passant par chacune d'elle qu'une seule fois. a). Montrer que son souhait est réalisable. b). Donner un exemple d'un tel parcours.

##### 2) Coloriage d'un graphe (p. 276-277)

**Activité 1** — « Colorier les graphes suivants en utilisant le minimum de couleurs. » G1 : 4 sommets, 3 arêtes (chaîne). G2 : pentagone avec toutes ses diagonales (5 sommets, graphe complet K5).
Encadré — « Colorier un graphe consiste à affecter une couleur à chacun de ses sommets de sorte que deux sommets adjacents ne portent pas la même couleur. »

**Activité 2** — « On donne le graphe G ci-dessous. » Figure (agrandie à l'image) : 6 sommets : 4 forment un K4 (deux sommets du haut, le sommet de gauche, le sommet central bas relié aussi à deux sommets pendants) ; le sommet central est relié à 5 autres (degré 5), 2 pendants.
1- Quel est le plus grand degré des sommets de G ? 2- Déterminer un sous graphe complet de G d'ordre 4. 3- Déterminer le nombre chromatique de G, noté γ(G).
Encadré — « Le nombre chromatique d'un graphe G, noté γ(G), est le nombre minimal de couleurs nécessaires pour sa coloration »
Encadré — ❖ « Le nombre chromatique d'un graphe est supérieur ou égal à l'ordre de tous ses sous graphes complets. » ❖ « Le nombre chromatique d'un graphe est inférieur ou égal à (Δ + 1) où Δ est le plus grand degré de ses sommets. »

**Activité 3** — « Dans le service administratif d'une entreprise, on observe des incompatibilités d'humeur entre certains employés recensés dans le tableau suivant. La présence d'une croix à l'intersection de la ligne i et la colonne j signifie que les employés ne peuvent pas travailler dans le même bureau. »
Croix (lues à l'image, symétriques) : E1 : E2, E5, E6 ; E2 : E1, E3, E4, E5, E6 ; E3 : E2, E4, E5, E6 ; E4 : E2, E3, E5 ; E5 : E1, E2, E3, E4, E6 ; E6 : E1, E2, E3, E5. (24 croix, soit 12 paires incompatibles, recompté.)
1- Représenter cette situation par un graphe. 2- Montrer que le nombre minimum de bureaux nécessaires à la répartition des employés qui peuvent travailler ensemble est égal à 4.

**Activité 4** — « Six compagnies de voyage proposent des visites de monuments et lieux touristiques : A, B,C et D .Un même lieu ne peut être visité par plusieurs groupes de compagnies différentes le même jour .La première compagnie fait visiter uniquement le lieu A ; la seconde les lieux A et C;la troisième le lieu D ; la quatrième les lieux C et D; la cinquième les lieux A et B; la sixième le lieu B. Comment organiser les visites d'une journée pour que chaque compagnie visite au moins un site ? »

##### 3) Recherche d'une plus courte chaîne (p. 277-278)

**Activité 1** — « Le graphe pondéré ci-contre représente un réseau routier. Sur chacune de ses arêtes on a marqué la distance séparant les deux villes reliées par cette arête. »
Figure : sommets A, B, C, D, E, F, G ; arêtes pondérées : A-B 35, A-F 33, B-C 45, C-G 8, G-F 40, F-E 75, E-C 80, E-D 130, D-C 75.
1-Déterminer le poids de la chaîne : F-G-C-D. 2- En appliquant l'algorithme de Dijkstra, vérifier que les plus courtes chaînes reliant le sommet A à n'importe quel autre sommet du graphe sont données par le tableau suivant :

Tableau de Dijkstra imprimé (colonnes A B C D E F G | « Sommet sélectionné ») ; une case vide = hachurée/vide à l'image :
| A | B | C | D | E | F | G | Sommet sélectionné |
|---|---|---|---|---|---|---|---|
| 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | A |
| | 0+35 / 35(A) | ∞ | ∞ | ∞ | 0+33 / 33(A) | ∞ | F |
| | 35(A) | ∞ | ∞ | 33+75 / 108(F) | | 33+40 / 73(F) | B |
| | | 35+45 / 80(B) | ∞ | 108(F) | | 73(F) | G |
| | | 73+8 / 80(B) | ∞ | 108(F) | | | C |
| | | | 80+75 / 155(C) | 80+80 / 108(F) | | | E |
| | | | 108+130 / 155(C) | | | | D |
3- Donner les plus courtes chaînes et les poids de chacune de ces chaînes, reliant : a) A à C b) A à D c) A à G.

**Activité 2** — « Un fournisseur se prépare à livrer un produit à ses clients d'une ville A à une ville F . Le tableau ci- contre indique les livraisons de ville à ville ainsi que la longueur du trajet, en kilomètres, entre deux villes. »
Tableau (lignes/colonnes A..H), valeurs lues à l'image (symétrique) : A : B20, D60, E80 ; B : A20, C10 ; C : B10, D20, G90, H80 ; D : A60, C20, E20, H40 ; E : A80, D20, F70, H30 ; F : E70, G20 ; G : C90, F20, H20 ; H : C80, D40, E30, G20.
1- Représenter les liaisons possibles par un graphe pondéré . 2- Déterminer la chaîne donnant la durée minimale du trajet de A à F.

---------------------------------------------------------------------
#### COURS — II- GRAPHES ORIENTÉS – MATRICE ASSOCIÉE À UN GRAPHE (pp. 278-285)

##### 1) Graphe orienté (p. 278-279)

**Activité 1** — « Le tableau suivant indique les rues à sens unique d'une partie d'une ville. »
Croix (ligne → colonne) : A→B ; B→C ; B→F ; C→D ; C→F ; D→F ; E→D ; F→A ; F→E.
Figure partielle déjà dessinée (sommets A…F, D isolé dans la figure) : A→B, B→F, C→F, F→E (arcs de départ).
1- Recopier le graphe G ci-dessus et le compléter en utilisant le tableau. Le graphe obtenu est appelé *graphe orienté*. 2- Déterminer un parcours, en voiture, de A à D en 4 étapes. 3- a) Peut–on déterminer un parcours de A à E, en voiture, en 2 étapes? b) Peut–on déterminer un parcours de A à E, à pieds, en 2 étapes?

Définition — « On appelle **graphe orienté** un graphe où chaque arête est orientée, c'est-à-dire qu'elle ne peut être parcourue que dans un seul sens. »
Vocabulaire — Dans un graphe orienté,
▪ Une arête orientée A→B est appelée **arc** d'origine A et d'extrémité B.
▪ Une **boucle** est un arc dont l'extrémité et l'origine sont les mêmes.
▪ **Une chaîne orientée** ou **un chemin** est une suite d'arcs tel que l'extrémité de chacun soit l'origine du suivant.
▪ **Un cycle orienté** ou **un circuit** est une chaîne orientée fermée composée d'arcs tous distincts.

**Activité 2** (p. 279) — « Soit le graphe G ci – contre. » Figure (lue) : arcs A→C (long), C→D, D→E, E→B, B→A, D→B [orientation de B-A et D-B : B→A et D→B lues, ?].
1) Donner une chaîne orientée reliant D à C. 2) Donner une chaîne orientée reliant B à E. 3) Peut-on déterminer un cycle orienté d'origine et d'extrémité A ? 4) Combien a-t-on d'arêtes orientées sortant de D? 5) Combien a-t-on d'arêtes orientées arrivant à B?

##### 2) Chaîne orientée eulérienne – Cycle orienté eulérien (p. 279-280)
Définitions —
▪ « Une chaîne orientée est dite **eulérienne** si elle passe une fois et une seule par chaque arête. »
▪ « **Un cycle orienté eulérien** est une chaîne orientée eulérienne fermée. »
▪ « Un graphe orienté est dit **eulérien** s'il admet un cycle orienté eulérien. »

**Activité 3** — « On donne les graphes G1, G2 et G3 suivants : » (figures : G1 5 sommets A,B,C,D,E (+F sur la figure : A,B,C,D,F ; lettres lues A,B,C,D,F, [?] car le tableau 1 est A,B,C,D,E) ; G2 : I,J,K,L,M ; G3 : P,Q,R,S,T ; arcs non transcrits [?]).
« Le tableau 1 (Respectivement 2 et 3) indique le nombre d'arêtes orientées rentrant, noté d-, et le nombre d'arêtes orientées sortant, noté d+, de chaque sommet du graphe G1 (respectivement G2 et G3). » Tableaux 1 (A B C D E), 2 (I J K L M), 3 (P Q R S T), lignes d+, d-, d+ - d- ; tableau 1 préremplit « d+ : B = 1 » et « d- : D = 2 ». (Tableau 2 et 3 : lignes d-, d+, d+ - d-, ordre différent de celui du tableau 1, tel qu'imprimé.)
1- Recopier et compléter les tableaux 1,2 et 3. 2- Vérifier que G1 est un graphe orienté eulérien et que G2 admet une chaîne orientée eulérienne. 3- G3 admet-il un cycle orienté eulérien ? une chaîne orientée eulérienne ? 4- Conjecturer.

Encadré (p. 280) — **Théorème (admis) :**
« Soit G un graphe connexe orienté. Pour tout sommet X de G, On note d+(X) (respectivement d-(X)) le nombre d'arêtes orientés **sortant** de x(respectivement **rentrant** à X).
❖ G admet un cycle orienté eulérien si et seulement si pour tout sommet X du G on a : d+(X) = d-(X)
❖ G admet une chaîne orientée eulérienne qui n'est pas un cycle orienté si et seulement si pour tout sommet X de G d+(X) = d-(X) sauf pour deux sommets exactement (A et B), on a : d+(A) = d-(A) + 1 et d+(B) = d-(B) - 1. »

**Activité 4** — « Dire, en justifiant, si chacun des graphes suivants admet un cycle orienté eulérien ou une chaîne orientée eulérienne. » Trois figures de graphes orientés SANS lettres (6 sommets avec centre ; 6 sommets en deux rangées ; 8 sommets) ; arcs non transcrits [?].

**Activité 5** — « Le graphe ci-dessous donne le plan d'un quartier avec le sens de circulation sur chaque arc, ainsi que le temps de parcours en voiture, en minutes, entre les différents lieux. » Sommets B, L, P, C, M, D. Arcs pondérés [R7 : relus à l'image 400 dpi, orientations sûres ; « P→B 10 » corrigé en B→P 10] : B→P 10, P→M 4, M→B 5, M→C 9, C→B 3, B→L 9, L→C 5, C→D 4, D→L 11, D→M 10 (10 arcs).
1- Ines affirme qu'elle peut parcourir, en voiture, toutes les rues du quartier une fois et une seule. A-t- elle raison? Justifier la réponse. 2- Elle désire se rendre de son domicile D à la piscine P, toujours en voiture, en un temps minimal .Quel chemin doit – elle suivre?

##### 3) Matrice associée à un graphe (pp. 280-283)

**Activité 1** — « Un livreur d'une société de vente à domicile doit, dans son après – midi, charger son camion à l'entrepôt noté A1, livrer cinq clients qu'on note A2, A3 A4, A5, et A6, puis retourner à l'entrepôt. Le réseau routier, tenant compte des sens de circulation, est représenté par le graphe G ci-après : »
Figure G (lue à l'image, 13 arcs, cohérente avec la chaîne eulérienne demandée) : A1→A5, A1→A6, A2→A1, A4→A1, A5→A4, A4→A3, A3→A4, A3→A6, A6→A3, A6→A2, A2→A6, A6→A4, A3→A2 [orientations lues à l'image, quelques-unes ?].
1- Recopier et compléter le tableau suivant en indiquant, dans la case correspondante, le nombre d'arêtes orientées reliant deux sommets. Tableau 6×6 (A1…A6) préremplie : ligne A1 : A1→A1 = 0, A1→A6 = 1 ; ligne A3 : colonne A4 = 1 ; ligne A4 : colonne A3 = 1 ; ligne A6 : colonne A1 = 0.
« La matrice carrée A d'ordre 6 ainsi obtenue est appelée **matrice associée** au graphe G. »
2- Que signifie le terme qui se trouve à l'intersection de la 3-ième ligne et la 2-ième colonne de la matrice A? à l'intersection de la i-ième ligne et la j-ième colonne (1 ≤ i,j ≤ 6) ? 3- a) Comparer d+(A2) et la somme des termes de la deuxième ligne de la matrice A. b) Comparer d-(A6) et la somme des termes de la sixième colonne de la matrice A. 4- Comment obtient – on d+(Ai) et d-(Ai)? 5- Montrer, à partir de A, que le graphe G admet une chaîne orientée eulérienne.

**1-Définition** (encadré) : « Soit G un graphe dont les sommets sont S1, S2, ..., Sn. On appelle **matrice associée** au graphe G, la matrice carrée A = (aij)1≤i,j≤n d'ordre n où le terme aij est le nombre d'arêtes d'origine Si et d'extrémité Sj. »
**2-Conséquences** (encadré) : ❖ « d+(Si) est égal à la somme des termes de la i-ième ligne de la matrice associée à ce graphe. » ❖ « d-(Si) est égal à la somme des termes de la i-ième colonne de la matrice associée à ce graphe. » [R7 : « (sic : « i-ième » pour d-) » retiré : « i-ième colonne » est correct, aucune coquille]

**Activité 2** — « Reconnaître, parmi les matrices M1, M2 et M3 suivantes, celle qui est associée au graphe G » (G : sommets A1…A5 ; figure : A1→A2, A1→A5 [?], A2→A4, A3→A1, A3→A5 [?]…).
M1 = [[0,1,0,0,1],[0,0,0,1,0],[1,0,0,0,1],[0,1,0,0,0],[1,0,1,0,0]] ;
M2 = [[0,1,1,0,1],[0,0,0,0,0],[1,0,0,0,1],[0,1,0,0,0],[0,0,0,0,0]] ;
M3 = [[0,1,0,0,1],[0,0,0,1,0],[1,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]].

**Activité 3** (p. 282) — « 1- Vérifier que la matrice A suivante est la matrice associée au graphe G ci – contre » A = [[0,0,1,0,1],[0,0,1,1,0],[1,1,0,0,1],[0,1,0,0,1],[1,0,1,1,0]] ; figure : sommets 1…5, arêtes 1-3, 1-5, 2-3, 2-4, 3-5, 4-5. 2- Justifier la symétrie de la matrice A par rapport à sa diagonale. 3- Comparer la somme de tous les termes de la matrice avec la somme des degrés des sommets de G. Justifier le résultat obtenu.

**3-Remarque** (encadré) : ❖ « La somme de tous les termes de la matrice associée à un graphe non orienté est égale à la somme des degrés des sommets de ce graphe. » ❖ « La matrice associée à un graphe non orienté est symétrique par rapport à sa diagonale. »

**Activité 4** — 1- « Donner la matrice associée à chacun des graphes suivants : » (i) graphe non orienté A-B, A-C, D isolé ; (ii) graphe orienté a, b, c : boucle sur a, a→b, b→c, boucle sur c ; (iii) A, B, C, D avec arêtes A-B, B-C, D-C, diagonale A-C (pas d'arête A-D ni B-D) [R7 : relu à 400 dpi ; « c→b » corrigé en b→c (la flèche pointe vers c) ; [?] levés]. 2- « Représenter un graphe dont la matrice associée est : » a) [[0,1,1],[1,0,0],[1,0,0]] b) [[0,1,0,1],[1,0,1,1],[0,1,0,1],[1,1,1,0]] c) [[0,0,0,0,1],[1,0,1,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,0,1,0,0]] (c : 5×5, ligne 4 = 0 1 0 1 0 telle qu'à l'image).

##### 4) Distance de deux sommets – Diamètre d'un graphe (pp. 282-285)

**Activité 5** — « Le graphe G ci-dessous représente les liaisons ferroviaires existant entre différentes villes nommées A1, A2, A3, A4 et A5. » Figure : arêtes A1-A3, A1-A5, A2-A4, A4-A5 (vérifiable avec A²).
Encadré : « La longueur d'une chaîne est le nombre d'arêtes qui la composent »
1) Ecrire toutes les chaînes : a) de longueur 2 reliant A1 à A4 ; b) de longueur 3 reliant A1 à A5 ; c) de longueur 3 reliant A1 à A2. 2) Donner la matrice A associée au graphe G. [libellé : « a) On a calculé les matrices A² et A³ suivantes : » — la numérotation du manuel saute de a) à c), coquille]
A² = [[2,0,0,1,0],[0,1,0,0,1],[0,0,1,0,1],[1,0,0,2,0],[0,1,1,0,2]] ; A³ = [[0,1,2,0,3],[1,0,0,2,0],[2,0,0,1,0],[0,2,1,0,3],[3,0,0,3,0]].
« Vérifier que les termes a14 ; a15 et a34 de la matrice A² correspondent bien aux nombres de chaînes de longueur 2 reliant : A1 à A4 ; A1 à A5 et A3 à A4. c) Déterminer le nombre de chaînes de longueur 3 reliant A1 à A5. »

Encadré — **Théorème (admis) :** « Soit G un graphe de matrice associée A. Le nombre de chaînes de longueur n joignant le sommet i au sommet j est égal au terme aij de la matrice An. » « Une justification de ce théorème se trouve dans la partie « maths culture » de ce chapitre. »

**Activité 6** — « La matrice A = [[0,1,1],[1,0,1],[0,1,1]] est la matrice associée à un graphe G. 1- Dénombrer les chaînes de G de longueur 2. 2- Dénombrer les chaînes de G de longueur 4. » (A non symétrique : graphe orienté, telle qu'imprimée.)

**Activité 7** — « Un parcours de santé est aménagé pour les sportifs dans le parc de la ville. Le graphe G ci- contre représente ce parcours. » Figure : sommets S1, S2, S3, S4 ; 7 arcs de 500 m chacun (7 étiquettes « 500m ») [R7 : relu à l'image 300 dpi et vérifié par le calcul de A², A³, A⁴, A⁵ imprimées (A est l'unique matrice 0/1 dont le carré vaut A²) ; remplace « 6 arcs : S1→S2, S4→S1, S2→S4, S4→S2 ou S2→S3, S3→S2, S3→S4 [?] »] : S1→S2, S1→S4, S2→S4, S3→S2, S3→S4, S4→S2, S4→S3.
1) Donner la matrice A associée au graphe G. 2) Après calcul, on obtient les matrices A², A³, A⁴ et A⁵ suivantes :
A² = [[0,1,1,1],[0,1,1,0],[0,1,1,1],[0,1,0,2]] ; A³ = [[0,2,1,2],[0,1,0,2],[0,2,1,2],[0,2,2,1]] ; A⁴ = [[0,3,2,3],[0,2,2,1],[0,3,2,3],[0,3,1,4]] ; A⁵ = [[0,5,3,5],[0,3,1,4],[0,5,3,5],[0,5,4,4]].
« Combien y a-t-il de trajets différents : De 1 km reliant S1 à S4 ? De 1,5 km reliant S3 à S2 ? De 2 km reliant S2 à S3 ? De 2 km reliant S4 à S4 ? De 2,5 km reliant S3 à S4 ? »

**Activité 8** (p. 284) — « Le graphe ci-contre représente les liaisons routières entre cinq villes, V1 ; V2 ; V3 ; V4 et V5 » Figure : arêtes lues V1-V5 (courbe), V1-V4, V5-V2, V5-V3 (courbe), V2-V3, V3-V4 [?].
1- a) Donner tous les itinéraires possibles à suivre pour aller de V1 à V2. b) Quel est celui qui a le minimum d'étapes ? 2- Vérifier que la longueur d'une plus courte chaîne reliant V1 à V2 est égale à 2. « Le nombre 2 ainsi trouvé s'appelle **distance** des deux sommets V1 et V4. » (coquille : V4 au lieu de V2)

Encadré — **Définitions :** ❖ « **La distance de deux sommets** distincts est la longueur de la plus courte chaîne joignant ces deux sommets. La distance est infinie, s'il n'existe pas de chaîne joignant ces deux sommets. La distance d'un sommet à lui-même est, par convention, nulle. » ❖ « Le **diamètre d'un graphe** est la plus grande des distances entre deux sommets du graphe. »

**Activité 9** — « Un port est constitué de plusieurs bassins reliés les uns aux autres par des passerelles. Dans le graphe G ci-contre, les sommets représentent les bassins et les arêtes les passerelles qui les relient. » Figure : sommets A, B, C, D, E, F ; arêtes lues : A-F, A-B, F-B, F-E, D-F, D-E, E-B, E-C [?].
1- Quel est le nombre minimal de passerelles à franchir pour relier les deux bassins A et C ? 2- Recopier le tableau ci-contre et compléter chaque case par la distance entre les sommets correspondants. (Tableau « Distance » A..F ; préremplie : A-A = 0 ; D-C = 2.) 3- En déduire le diamètre du graphe G. 4- Modifier le graphe G de façon à en faire un graphe de diamètre 2.
Texte (italique) : « Quand l'ordre d'un graphe est assez grand, la recherche « à la main » de la distance entre deux de ses sommets et, par conséquent, la détermination du diamètre de ce graphe deviennent très difficiles. Le théorème suivant donne une méthode permettant de trouver ces deux quantités facilement, à l'aide des matrices. »

Encadré — **Théorème (admis) :** « Soit G un graphe de matrice associée A.
❖ La distance entre deux sommets distincts i et j est le plus petit entier naturel n (n ≥ 1) tel que le terme d'indice i,j de An est non nul.
❖ Le diamètre du graphe G est le plus petit entier naturel n tel que la matrice (A + Id)^n ait tous ses termes strictement positifs. »

**Activité 10** (p. 285) — « On donne le graphe G ci-dessous, sa matrice associée M, et les matrices M⁴ et M⁵. Dire pourquoi la distance entre les sommets A et S est égale à 5. » Graphe : 11 sommets, A à gauche, S à droite (figure).
M (11×11, telle qu'imprimée) :
L1 0 1 1 0 0 0 0 0 0 0 0
L2 1 0 1 1 0 0 0 0 0 0 0
L3 1 1 0 1 1 0 0 0 0 0 0
L4 0 1 0 0 0 0 1 0 0 0 0
L5 0 0 0 0 0 1 0 0 0 0 0
L6 0 0 1 0 0 0 1 0 0 1 0
L7 0 0 0 1 0 1 0 1 1 0 0
L8 0 0 0 0 0 0 1 0 1 0 1
L9 0 0 0 0 0 0 1 1 0 1 1
L10 0 0 0 0 0 1 0 0 1 0 1
L11 0 0 0 0 0 0 0 1 1 1 0
M⁴ :
11 10 10 13 7 3 3 2 2 1 0
10 17 17 11 8 3 10 2 2 3 2
10 17 24 12 5 8 10 3 4 2 3
13 11 12 19 8 10 5 9 11 4 4
7 8 5 8 9 1 9 4 3 7 3
3 3 8 10 1 17 6 12 19 5 11
3 10 10 5 9 6 29 15 16 20 19
2 2 3 9 4 12 15 21 22 17 15
2 2 4 11 3 19 16 22 31 15 21
1 3 2 4 7 5 20 17 15 20 14
0 2 3 4 3 11 19 15 21 14 20
M⁵ :
20 34 41 23 13 11 20 5 6 5 5
34 38 46 44 20 21 18 14 17 7 7
41 46 44 51 32 17 27 17 18 15 9
23 44 51 28 22 17 49 20 22 25 24
13 20 32 22 6 25 16 15 23 7 14
11 21 17 17 25 12 58 36 34 47 36
20 18 27 49 16 58 42 64 83 41 51
5 14 17 20 15 36 64 52 68 49 60
6 17 18 22 23 34 83 68 74 71 68
5 7 15 25 7 47 41 49 71 34 52
5 7 9 24 14 36 51 60 68 52 50
(Lecture attendue : terme (1,11) = 0 dans M⁴ et 5 dans M⁵ ; dans l'énoncé « A » = sommet 1, « S » = sommet 11.)

---------------------------------------------------------------------
#### COURS — III- GRAPHES PROBABILISTES (pp. 286-289)

**Activité 1** (p. 286) — « Un compte bancaire peut être créditeur ou débiteur. L'évolution mensuelle du compte bancaire d'un certain client est telle que - Lorsque son compte est créditeur à la fin d'un mois, la probabilité qu'il le soit encore à la fin du mois suivant est 0,4. - Lorsque son compte est débiteur à la fin d'un mois, la probabilité qu'il le soit encore à la fin du mois suivant est 0,35. »
1) « La situation peut être représentée par le graphe orienté G ci-dessous » Figure : C avec boucle 0,4 ; C→D 0,6 ; D avec boucle 0,35 ; D→C 0,65. « où : - les sommets sont les deux états : C « le compte est créditeur » et D « le compte est débiteur ». - les arêtes sont orientées et pondérées par les probabilités conditionnelles de passer d'un état à un autre, d'un mois au suivant. Calculer la somme des poids des arêtes orientés issues de C puis la somme des poids des arêtes orientés issues de D » « On dit qu'il s'agit d'un **graphe probabiliste**. »
2) « Recopier le tableau ci-contre et compléter chaque case par le poids de l'arête orientée correspondant. La matrice carrée M d'ordre 2 ainsi obtenue est appelée **la matrice de transition** du graphe G qui est à 2 sommets. » (tableau C,D × C,D ; préremplie : case (C,D) = 0,6.)
Encadré — **Définitions :** ❖ « On appelle **graphe probabiliste** un graphe orienté et pondéré dont la somme des poids des arêtes orientées sortant de chaque sommet vaut 1. » ❖ « On appelle **matrice de transition** d'un graphe probabiliste à n sommets, la matrice carrée d'ordre n dont le terme figurant à la i-ième ligne et la j-ième colonne est égal au poids de l'arête allant du sommet i au sommet j, si elle existe, et à 0 sinon. »
Texte (italique) : « Les graphes probabilistes sont utilisés pour modéliser une évolution d'un état vers un autre. Les sommets du graphe sont les états possibles et le poids d'une arête orientée issue du sommet i et d'extrémité j est la probabilité de transition de l'état i à l'état j. »

**Activité 2** (p. 287) — « Parmi les graphes suivants indiquer ceux qui sont des graphes probabilistes et donner leur matrice de transition. » Cinq figures (lues à l'image) :
(G-a) sommets 1, 2 : boucle 1 : 2/3 ; 1→2 : 1/3 ; boucle 2 : 0.6 ; 2→1 : 0.4.
(G-b) sommets 1, 2, 3 : boucle 1 : 0.2 ; 1→2 : 0.8 ; boucle 2 : 0.5 ; 2→3 : 0.9 ; boucle 3 : 1/5 ; 3→1 : 0.8.
(G-c) trois sommets non nommés (P gauche, Q haut-droit, R bas) : boucle P : 0.1 ; P→Q : 0.2 ; Q→P : 0.4 ; boucle Q : 0.6 ; P→R : 0.5 ; R→P : 0.4 ; R→Q : 0.6 [orientations lues à l'image].
(G-d) sommets a, b, c : boucle a : 0.6 ; a→c : 0.4 ; c→a : 0.3 ; boucle c : 0.2 ; c→b : 0.5 ; b→c : 0.4 ; b→a : 0.6.
(G-e) sommets 1, 2, 3 : boucle 1 : 0.2 ; 1→2 : 0.8 ; boucle 2 : 1/4 ; 2→3 : 3/4 ; boucle 3 : 1/5 ; 3→1 : 0.8.
(Sommes sortantes lues : G-a 1 et 1 ; G-b sommet 2 : 0,5+0,9 = 1,4 ; G-c sommet P : 0,1+0,2+0,5 = 0,8 ; G-d, G-e : 1 partout. Le manuel ne donne pas le corrigé. Notations décimales imprimées en « 0.6 » (point) et en « 0,6 » (virgule) : mélange tel quel.)

**Activité 3** — « Représenter un graphe probabiliste dont la matrice de transition est : » a) M1 = [[0,25 ; 0,75],[0,75 ; 0,25]] b) M2 = [[0,15 ; 0,2 ; 0,65],[0,7 ; 0 ; 0,3],[0,25 ; 0,5 ; 0,25]] c) M3 = [[0,1 ; 0 ; 0,9],[0,8 ; 0,2 ; 0],[0 ; 0,5 ; 0,5]]

**Activité 4** — « Reprenons l'activité 1. A l'état initial, on note C0 l'événement : « le compte est créditeur » et D0 l'événement : « le compte est débiteur ». On pose c0 la probabilité de C0, d0 la probabilité de D0, cn la probabilité de l'événement Cn : « le compte est créditeur à la fin du n-ième mois » et dn la probabilité de l'événement Dn : « le compte est débiteur à la fin du n-ième mois » .
1) a) A l'aide d'un arbre de probabilité, exprimer en fonction de c0 et d0 : i) c1 et d1 ; ii) c2 et d2.
b) Recopier et compléter l'arbre de probabilité ci-contre (racine → Cn, Dn ; chacun → Cn+1, Dn+1), et vérifier que pour tout entier n ≥ 1 : c(n+1) = 0,4.cn + 0,65.dn ; d(n+1) = 0,6.cn + 0,35.dn.
2) Notons, pour tout entier n ≥ 1, pn = (cn dn) la matrice ligne décrivant l'état probabiliste au n-ième mois et p0 = (c0 d0) la matrice ligne décrivant l'état probabiliste à l'état initial.
a) Vérifier, en utilisant les résultats de la première question, que : p1 = p0 × M ; p2 = p1 × M et p(n+1) = pn × M où M est la matrice de transition du graphe G (voir activité 1). b) En déduire alors que, pour tout n ∈ IN, pn = p0 × M^n »

Encadré — **Théorème (admis) :** « Soit M la matrice de transition d'un graphe probabiliste d'ordre supérieur ou égal à 2. Si pn est la matrice ligne décrivant l'état probabiliste à l'étape n et p0 est la matrice ligne décrivant l'état probabiliste à l'état initial, alors pn = p0 × M^n »
Encadré — **Remarque :** « Si l'état initial est p1 alors pn = p1 × M^(n−1) »

**Activité 5** (p. 288) — « Une personne joue à la machine à sou. Elle estime à 0,15 ses chances de gagner au départ . Puis à chaque jeu, elle pense avoir : - Une chance sur deux de gagner au jeu suivant si elle vient de gagner. - Deux chances sur cinq de gagner au jeu suivant si elle vient de perdre. L'état probabiliste initial est donc p0 = (0.15 0.85). On désigne par an la probabilité de gagner le n-ième jeu et par bn celle de le perdre.
1) Représenter cette situation à l'aide d'un graphe probabiliste. 2) donner sa matrice de transition.
3) Montrer par récurrence que M^n = [[4/9 + (5/9)(1/10)^n , 5/9 − (5/9)(1/10)^n],[4/9 − (4/9)(1/10)^n , 5/9 + (4/9)(1/10)^n]]
4) En déduire an et bn en fonction de n. 5) Vérifier alors que lim(n→+∞) an = 4/9 et lim(n→+∞) bn = 5/9. 6) Vérifier que (4/9 5/9) est l'unique solution de l'équation (x y) × M = (x y) »
Encadré — **Théorème (admis) :** « Pour tout graphe probabiliste d'ordre 2 dont la matrice de transition ne comporte pas de zéro, l'état pn à l'étape n converge vers un état p, dit **stable**, indépendante de l'état initial p0. De plus p est l'unique solution de l'équation X×M = X où X = (x y) avec x + y = 1 »

**Activité 6** (pp. 288-289) — « On considère une grande population d'acheteurs de yaourts. On suppose que l'effectif de cette population est stable. Une entreprise commercialise des yaourts sous la marque Y. 30 % des acheteurs de yaourts achètent la marque Y. L'entreprise décide de faire une campagne publicitaire pour améliorer ses ventes. Au bout d'une semaine, une enquête indique que : · 20 % des acheteurs de yaourts qui achetaient la semaine précédente des yaourts des autres marques achètent maintenant des yaourts Y. · 10 % des acheteurs de yaourts qui achetaient la semaine précédente des yaourts Y achètent maintenant des yaourts des autres marques. L'entreprise continue sa campagne publicitaire. On fait l'hypothèse que l'évolution des résultats obtenus à l'issue de la première semaine de campagne publicitaire est la même les semaines suivantes.
1) Dessiner le graphe probabiliste correspondant à cette situation. 2) Soit X0 = (0,3 0,7) la matrice ligne décrivant l'état initial de la population. a) Donner la matrice de transition (notée A) associée au graphe précédent. b) Déterminer la probabilité qu'un acheteur de yaourts choisi au hasard après deux semaines de campagne publicitaire, achète des yaourts de la marque Y.
3) On admet que, pour tout entier naturel n, on a : A^n = [[2/3 + (1/3)·0,7^n , 1/3 − (1/3)·0,7^n],[2/3 − (2/3)·0,7^n , 1/3 + (2/3)·0,7^n]]. Avec l'hypothèse ci-dessus, l'entreprise peut-elle espérer atteindre une part de marché de 70 % ? Justifier. »

**Activité 7** (p. 289) — « Un guide touristique classe chaque année les hôtels d'une certaine région en deux catégories selon la qualité de leurs prestations. Les plus confortables sont classés dans la catégorie A, les autres dans la catégorie B. On constate que, chaque année, 5% des hôtels de la catégorie A sont relégués dans la catégorie B, alors que 20% des hôtels de la catégorie B sont promus dans la catégorie A. 1) Réaliser un graphe décrivant cette situation. 2) Ecrire la matrice de transition de ce graphe en respectant l'ordre alphabétique. 3) En 2006, le classement était tel que le quart des hôtels étaient dans la catégorie A. Calculer l'état de l'année 2007, puis celui de l'année 2008. 4) L'état (0,5 0,5) est-il stable ? Justifier la réponse. 5) Trouver vers quel état converge ce système. »

---------------------------------------------------------------------
#### AVEC L'ORDINATEUR (pp. 290-291) — Derive 6

« Utilisation d'un logiciel de calcul formel (Derive) pour calculer une puissance entière d'une matrice. »
**Activité 1** — « 1°) Exécuter le logiciel Derive. On obtient : » (capture : fenêtre « Derive 6 - [Algèbre1] »). « 4°) On veut calculer [[1, 0, 1/2, −1/2],[3, 4, 0, 0],[3, 2, −1, −3],[1/2, −1, 0, 0]]^3 , Pour cela on introduit dans la barre de calcul de Derive [1, 0, 1/2, −1/2; 3, 4, 0, 0; 3, 2, −1, −3; 1/2, −1, 0, 0] ^3 et en valide par la touche Entrer au clavier, on obtient : » (capture : la matrice entrée #1, non évaluée.) (la numérotation passe de 1° à 4° : étapes 2°-3° absentes, tel qu'imprimé).
p. 291 : « Pour obtenir le résultat : aller dans [Simplifier/ = Basique] Ou bien le raccourci [ = ] On obtient : » Résultat #2 (capture, lu à l'image agrandie) : [[23/4, 8, 9/8, −9/8],[267/4, 137/2, 6, −12],[159/4, 79/2, −1/4, −39/4],[−111/8, −61/4, −3/2, 1/2]].
**Activité 2** — « En utilisant le procédé de l'activité 1, calculer : »
(1) [[1,1,0,1,0],[1,1,3,−1,4],[0,3,1,2,1],[1,−1,2,1,1/2],[0,4,1,1/2,1]]^10 ;
(2) [[2,1,3,2/5],[−2,1/2,3,0],[2,1,−3,1/2],[−2,1/2,−3,−4]]^22.
(Aucun résultat donné ; le manuel ne le fournit pas.)

---------------------------------------------------------------------
#### EXERCICES ET PROBLÈMES (pp. 292-300) — 27 exercices

**1-** « Répondre par vrai ou Faux à chacune des affirmations suivantes en justifiant les réponses. a) Le graphe G ci-contre admet un cycle eulérien. b) Le graphe G admet une chaîne eulérienne. c) La chaîne D-A-B-C-F-E-F-A-E est une chaîne eulérienne de G. » Figure G : sommets F, B, C, A, E, D ; arêtes : F-B, F-C, F-A, F-D, F-E, E-A, D-A, B-A, B-C (9 arêtes) [R7 : relu à 400 dpi ; « E-D » corrigé en E-A (il n'y a pas d'arête E-D) ; [?] levé].

**2-** « Soit le graphe G ci-contre. a) G admet -il une chaîne eulérienne ? Pourquoi ? b) G admet -il un cycle eulérien ? Si oui, lequel ? Si non, proposer une modification du graphe pour qu'il en admette un. » Figure : sommets A, B, E, C, D, F, G, H ; (rectangle A-B-H-F avec points internes ; arêtes lues non toutes sûres [?]) : A-B, B-H, A-F, A-E, E-F, A-D, A-C, D-F, D-G, C-G, C-B, G-B [?].

**3-** « Le ramassage des ordures ménagères dans la ville dont un plan est représenté ci-contre, à l'aide d'un graphe, doit être effectué en minimisant le trajet à effectuer. Les sommets sont les différents carrefours et les arêtes les voies de circulation. a) Est-il possible de partir d'un carrefour et d'y revenir en empruntant chaque voie une fois et seule ? b) Le graphe ci-dessus admet-il une chaîne eulérienne ? Si oui, en déterminer une. » Figure : sommets A, B, C, D, E, F, G, H ; arêtes lues : A-B, B-C, A-F, C-H, F-G, G-H, A-D, D-F, D-E, D-C, B-E, C-E, E-G, E-H, F-E, D-G [?].

**4-** « Pour chaque question, cocher une case sur chaque ligne, la case « Vrai » ou la case « Faux ». 1. Dans le graphe ci-contre, il est possible de définir une chaîne eulérienne… a) Partant de Q et finissent en T. b) Partant de S et finissent en S. c) Partant de P et finissent en R. » Figure : sommets P, Q, S, R, T ; arêtes lues : P-Q, P-S, P-R, Q-S, S-R, R-T, T-S.
« 2. Dans le graphe pondéré ci-contre, la plus courte chaîne pour aller de P à V… A pour poids 16. / A pour poids 14. (Vrai / Faux) » Figure : sommets P, Q, U, S, R, T, V ; arêtes pondérées : P-Q 8, P-R 6, Q-U 2, U-S 2, Q-S 5, Q-R 1, Q-T 4, S-T 1, S-V 3, R-T 5, T-V 5.

**5-** « a) Citer deux chaînes de longueur 3 reliant les sommets A et D du graphe G ci-contre. b) Pour chacune des chaînes ci-dessous Donner sa longueur, dire si elle est fermée et préciser s'il s'agit d'un cycle eulérien. A-B-D-C-F-A ; A-E-C-F-E-A et B-D-C-F-E-A » Figure G : sommets A, B, C, D, E, F ; arêtes déduites des chaînes imprimées : A-B, B-D, D-C, C-F, F-A, A-E, E-C, F-E ; autres arêtes sur la figure (B-C, B-E, A-E, D-E) [?].

**6-** « Recopier le graphe ci-dessous et utiliser l'algorithme de Welch-Powell pour le colorier. » Figure : sommets A, C, D, E, B, G, F, H ; arêtes lues : A-C, A-B, C-D, B-E, G-D, G-E, G-F, F-D ?, G-H [?]. (l'algorithme de Welch-Powell n'est pas énoncé dans ce chapitre du manuel.)

**7-** « Encadrer le nombre chromatique de chacun des graphes ci-dessous par deux nombres entiers (il n'est pas demandé de chercher ce nombre chromatique). » Deux figures : (1) 6 sommets A, B, C, D, E, F, F central relié à plusieurs [?] ; (2) 6 sommets : pentagone A-B-C-D-E avec F central [?].

**8-** « Le plan ci-dessous représente différents échantillons de papier posés les uns sur les autres délimitant ainsi sept zones à colorier de telle façon que si deux d'entre elles ont une frontière commune alors elles seront de couleurs différentes. a) Représenter la situation par un graphe G. b) Colorier le graphe G avec l'algorithme de Welch-powell. c) Reproduire le plan et colorier comme souhaité » Plan : rectangles superposés, zones nommées a, b, c, d, e, f, g (g = fond/extérieur).

**9-** « T est le graphe ci-contre. 1. On note γ(T) le nombre chromatique de T. a) Dire pourquoi le sous graphe constitué des sommet C ; D ; E et F est complet. b) Démontrer que 4 ≤ γ(T) ≤ 6. c) Déterminer la valeur de γ(T). 2. On considère un groupe d'élèves notés A, B, C, D, E, F et G. Pour un exposé, les élèves se mettent en équipes, mais il faut respecter les incompatibilités entre les élèves. Dans le tableau ci-après, chaque croix indique une incompatibilité entre les élèves correspondants. » Figure T : sommets A, F, B, E, D, G, C (arêtes non transcrites [?]).
Tableau (p. 294, croix lues) : A : B, E, F ; B : A, C ; C : B, D, E, F ; D : C, E, F, G ; E : A, C, D, F, G ; F : A, C, D, E ; G : D, E.
« a) Si l'on décide de modéliser ce tableau d'incompatibilité par le graphe T, quel sens faut-il donner à l'existence d'un arrête entre deux sommets ? b) Combien d'équipes faudra-t-il créer en minimum ? Proposer une répartition des élèves en équipes (une équipe peut comporter un seul élève). »

**10-** « Un laboratoire de produits pharmaceutiques de première urgence doit livrer un médicament le plus rapidement possible à un certain nombre de pharmacie de la région. Il ne dispose à ce moment que d'un seul véhicule. Le départ est de A et les différentes pharmacies sont nommées B, C, D, E, F et G. Mettre au point un parcours qui soit le plus rapide possible, sachant que le temps de parcours sont indiqués dans le tableau ci-dessus. » Tableau des temps (ligne = départ ; la phrase dit « ci-dessus », le tableau est imprimé en dessous) :
| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| A | | 8 | 5 | 6 | 3 | 5 | 2 |
| B | 8 | | 7 | 9 | 6 | 2 | 9 |
| C | 9 | 7 | | 3 | 6 | 5 | 5 |
| D | 6 | 9 | 3 | | 9 | 8 | 4 |
| E | 3 | 6 | 6 | 9 | | 4 | 6 |
| F | 5 | 2 | 5 | 8 | 4 | | 7 |
| G | 2 | 9 | 5 | 4 | 6 | 7 | |
Incohérence : tableau non symétrique : A→C = 5 mais C→A = 9 (le reste est symétrique : A-B 8/8, A-D 6/6, A-E 3/3, A-F 5/5, A-G 2/2, B-C 7/7, B-D 9/9, …).

**11-** « Un concert de solidarité est organisé dans une grande salle de spectacle. A ce concert sont conviés sept artistes de renommée internationale : A ; B ; C ; D ; E ; F et G. Les différents musiciens invités refusant de jouer avec certains autres, l'organisateur du concert doit prévoir plusieurs parties de spectacle. Les arêtes du graphe T ci-contre indiquent quels sont les musiciens qui refusent de jouer entre eux. 1. Colorier le graphe T. 2. Combien de parties l'organisateur du concert doit-il prévoir ? 3. Proposer une répartition des musiciens pour chacune de ces parties. » Figure T : 7 sommets, graphe dense (C, B, A, G, D, E, F), arêtes non transcrites [?].

**12-** « Ce schéma représente un carrefour. Le tableau ci-dessous précise les « franchissements » possibles de ce carrefour. (la circulation de A vers E est considérée comme un « franchissement » même si on ne traverse pas le carrefour). » Schéma : routes A, B, C, D, E autour du carrefour.
| En arrivant par … | A | B | C | D | E |
|---|---|---|---|---|---|
| Il est possible d'aller en … | C, E | A, E, D | A, D | C, A | C, D |
« Les franchissements AC et BE ne peuvent naturellement pas être autorisés simultanément sous peine de collision. On se propose de déterminer le nombre minimal de phases des feux de signalisation nécessaire au bon fonctionnement de ce carrefour. a) Modéliser cette situation à l'aide d'un graphe dont : • Les sommets représentent les franchissements possibles (AC, CA, AE, BA, BE,…) • Les arêtes reliant les sommets représentant des franchissements ne peuvent pas être simultanés sous peine de collision. b) Montrer que (EC ; AC ; DB ; CD ; DA) est un sous graphe complet d'ordre 5. c) Que peut-on dire de sommet DA ? en déduire un encadrement du nombre chromatique du graphe. d) Proposer une coloration de graphe. En déduire son nombre chromatique. e) Que peut –on dire d'un ensemble de sommets ayant même couleur ? a quoi peut correspondre le nombre chromatique de ce graphe ? »
Incohérences : la liste des franchissements ne contient pas « DB » ni « EC » comme écrit ... tableau : B → A, E, D (donc « BD » et non « DB »), E → C, D (« EC » ok), D → C, A (« DA » ok, « DB » absent du tableau) ; coquille probable.

**13-** « Le graphe suivant représente les différents itinéraires pour aller de D à S. Le poids des arêtes est le coût, en DT, du trajet effectué entre deux villes nommées par des sommets. a) Quel est le poids de la chaîne D-A-C-S ? b) Quelle est la chaîne de poids minimal ? c) Quelle est la longueur de la chaîne D-A-C-S ? » Figure : sommets D, A, C, S, B ; arêtes pondérées : D-A 4, D-C 9, D-B 3, A-C 3, A-S 6, C-S 2, C-B 5, B-S 7.

**14-** « Des touristes sont logés dans un hôtel noté A. Un guide fait visiter six cites touristiques noté B,C,D,E,F et G. Les tronçons de route qu'il peut emprunter sont représentés sur le graphe ci-contre : (le long de chaque arête figure la distance en kilomètres de différents tronçons). 1.a) A partir de l'hôtel, le guide peut-il emprunter tous les tronçons de route en passant une fois et une seule sur chacun d'eux ? Justifier la réponse. b) Même question s'il doit obligatoirement terminer son circuit à l'hôtel. 2. Déterminer le plus court chemin menant de l'hôtel A au site E. Justifier la réponse. » Figure : arêtes lues (km) : A-D (sans étiquette lue) [?], A-C 20, A-B 12, B-G 13, D-C 8, D-F 21, C-F 11, C-G 7, F-G 5, F-E 3, G-E 9.

**15-** « 1. Caractériser les graphes de diamètre 1. 2. Trouver le diamètre des graphes ci-dessous ? » (a) pentagramme (5 sommets, étoile) ; (b) hexagone ; (c) octogone [?]. « 3 Quel est le diamètre de chacun des deux graphes ci- dessous ? » : deux arbres (racine, branches binaires).

**16-** « Soit G le graphe ci-contre. 1) Donner la matrice M associée à G en écrivant les sommets dans l'ordre alphabétique. 2) On a calculé les matrice M² et M⁵ suivantes : »
Figure : sommets A, B, C, D, E, F ; arêtes lues : A-B, A-F, F-B, B-D, D-C, C-E, E-F.
M² = [[2,1,0,1,1,1],[1,3,1,0,1,1],[0,1,2,0,0,1],[1,0,0,2,1,1],[1,1,0,1,2,0],[1,1,1,1,0,3]] ;
M⁵ = [[14,21,12,9,9,21],[21,18,9,19,14,26],[12,9,2,12,12,9],[9,19,12,4,7,14],[9,14,12,7,4,19],[21,26,9,14,19,18]].
« a) En déduire le nombre de chaînes de longueur 2 reliant A et D. Les écrire. b) Entre quels sommets de ce graphe y a –t-il le plus de chaînes de longueur 2 ? Les écrire. c) Entre quels sommets y a-t- il 4 chaînes de longueur 2 ? d) Déterminer le nombre de chaînes de longueur 5 reliant B et F. »

**17-** « Représenter un graphe non orienté dont la matrice associée est la suivante : » M = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]].

**18-** « M est la matrice d'un graphe non orienté G. » M = [[0,1,0,1,1,0],[1,0,1,1,0,1],[0,1,0,0,1,1],[1,1,0,0,0,1],[1,0,1,0,0,1],[0,1,1,1,1,0]]. « a) Quel est l'ordre de G ? b) Calculer la somme des degrés des sommets de G. c) Quel est le nombre d'arêtes de G ? »

**19-** « On considère le graphe orienté ci-contre. a) Ecrire la matrice A associée à ce graphe. b) On a calculé les matrices A⁵ et A⁶ suivantes : » Figure : sommets 1…6 (2 et 4 au-dessus, 1 et 3 puis 6 en bas, 5 à droite) ; arcs [R7 : relus à l'image et vérifiés par le calcul (A⁵ et A⁶ imprimées retrouvées exactement) ; « 5→3 » corrigé en 3→5] : 1→2, 1→3, 2→4, boucle en 4, 4→3, 4→6, 5→4, 3→5, 3→6, 6→5.
A⁵ = [[0,0,3,5,5,5],[0,0,3,6,3,4],[0,0,2,4,5,4],[0,0,6,9,7,9],[0,0,3,6,3,4],[0,0,1,3,3,2]] ;
A⁶ = [[0,0,5,10,8,8],[0,0,6,9,7,9],[0,0,4,9,6,6],[0,0,9,16,15,15],[0,0,6,9,7,9],[0,0,3,6,3,4]].
« c) Donner le nombre de chaînes orientées de longueur 5 du sommet 1 au sommet 5. Les écrire. d) Le graphe contient – il des chaînes orientées fermées ? Si oui combien ? »
Note : les colonnes 1 et 2 de A⁵ et A⁶ sont nulles ; les lignes 2 et 5 de A⁵ sont identiques ([0,0,3,6,3,4]) [R7 : « différentes » corrigé], tel qu'imprimé.

**20-** « Dans un groupe de six personnes chacune d'elles doit choisir celles en qui elle a confiance pour partager ces activités de loisir. A, B, C, D, E et F ces personnes. On constate que : • A n'a confiance qu'en lui-même, mais possède la confiance de B. • E a confiance en B, C et D mais n'a la confiance que de B et C. • B et D ont confiance en C. • F est très méfiant et n'a même pas la confiance en soi. a) Représenter cette situation à l'aide d'un graphe orienté dans lequel les sommets représentent ces six personnes et les arêtes orientées signifient « a confiance en ». b) Quelle est la personne qui a la confiance du plus grand nombre d'entre elles ? »

**21-** « Cinq personnes notées A, B, C ; D et E et peuvent communiquer entre elles soit par téléphone, soit par courrier électronique. A et B ; A et C ; B et C peuvent se téléphoner. C peut envoyer et recevoir du courrier électronique avec D et E. a) Recopier et compléter le tableau suivant : (A..E × A..E, diagonale préremplie 0) Dans ce tableau, on inscrit 1 au croisement de la ligne X et la colonne Y si la personne de la ligne X peut communiquer avec la personne de colonne Y et 0 sinon. b) Ecrire la matrice M associée à cette situation. c) Construire le graphe associé à cette matrice M. d) Quelle est la personne qui peut communiquer avec le plus grand nombre directement ? e) On admet que deux personnes peuvent communiquer par l'intermédiaire d'un troisième. Si X peut communiquer directement avec Y et Y directement avec Z. On admet que la matrice M² est » M² = [[2,1,1,1,1],[1,2,1,1,1],[1,1,4,0,0],[1,1,0,1,1],[1,1,0,1,1]]. « Calculer la matrice S = M + M². f) Déduire le résultat que chacune des cinq personnes peut communiquer avec tout autre personne directement ou indirectement. »

**22-** « Dans un club de football ; lors de longues séances de tirs au but, le gardien se comporte de la manière suivante : • S'il arrête un tir, il arrête le suivant avec la probabilité de 0,5. • S'il a encaissé un but, il arrête le tir suivant avec la probabilité de 0,2. 1.a) Représenter la situation à l'aide d'un graphe probabiliste. b) Donner la matrice de la transition de ce graphe. 2. Le gardien n'a pas arrêté le premier tir. Quelle est la probabilité qu'il arrête le troisième tir ? »

**23-** « Un théâtre propose deux types d'abonnement pour une année : un abonnement A donnant droit à six spectacles ou un abonnement B donnant droit à trois spectacles. On considère un groupe de 2500 personnes qui s'abonnent tous les ans. n étant un entier naturel, on note : an la probabilité qu'une personne ait choisit l'abonnement A l'année n ; bn la probabilité qu'une personne choisit l'abonnement B l'année n ; Pn la matrice (an bn) traduisant l'état probabiliste l'année n. Tous les ans, 85% des personnes qui ont choisi l'abonnement A et 55% des personnes qui ont choisi l'abonnement B conservent le même type d'abonnement l'année suivante. Les autres changent d'abonnement. 1. On suppose que, l'année zéro, 1500 personnes ont choisi l'abonnement A et 1000 personnes ont choisi l'abonnement B. Déterminer l'état initiale P0 = (a0 b0). 2. a) Tracer un graphe probabiliste traduisant les données de l'énoncé. b) Déterminer la matrice de transition M de ce graphe c) En déduire le nombre d'abonnés l'année un. »

**24-** « On a divisé une population en deux catégories : « fumeurs » et « non-fumeurs ». Une étude statistique a permis de constater que, d'une génération à l'autre, - 60% des descendants de fumeurs sont des fumeurs, - 10% des descendants de non-fumeurs sont des fumeurs. On suppose que le taux de fécondité des fumeurs est le même que celui des non fumeurs. On désigne par : - fn le pourcentage de fumeurs à la génération de rang n, - gn = 1 – fn le pourcentage de non-fumeurs à la génération de rang n, où n est un entier naturel. On considère qu'à la génération 0, il y a autant de fumeurs que de non-fumeurs. On a donc f0 = g0 = 0,5. 1) Traduire les données de l'énoncé par un graphe probabiliste. 2) Justifier l'égalité matricielle : (f(n+1) g(n+1)) = (fn gn).A où A désigne la matrice : [[0,6 ; 0,4],[0,1 ; 0,9]]. 3) Déterminer le pourcentage de fumeurs à la génération de rang 2. 4) Déterminer l'état probabiliste stable et l'interpréter. 5) Montrer que : pour tout entier naturel n, f(n+1) = 0,5.fn + 0,1. 6) On pose, pour tout entier naturel n, un = fn – 0,2. a) Montrer que la suite (un) est une suite géométrique dont on précisera le premier terme et la raison. b) Donner l'expression de un en fonction de n. c) En déduire que, pour tout entier naturel n, fn = 0,3.0,5^n + 0,2. d) Déterminer la limite de la suite (fn) lorsque n tend vers +∞ et l'interpréter. »

**25-** « Au cours de la première semaine de l'année scolaire, un professeur propose aux élèves de sa classe le choix entre deux sorties pédagogiques une sortie A et une sortie B. 20% des élèves de la classe sont favorables à la sortie A et tous les autres élèves sont favorables à la sortie B. Les arguments des uns et des autres font évoluer cette répartition en cours d'année. Ainsi 30 % des élèves favorables à la sortie A et 20 % des élèves favorables à la sortie B changent d'avis la semaine suivante. On note : an la probabilité qu'un élève soit favorable à la sortie A la semaine n ; bn la probabilité qu'un élève soit favorable à la sortie B la semaine n ; Pn la matrice (an bn) traduisant l'état probabiliste la semaine n. 1) Déterminer l'état initial P1. 2) Représenter la situation par un graphe probabiliste. 3) En déduire que P(n+1) = Pn × M où M est la matrice [[0,7 ; 0,3],[0,2 ; 0,8]]. 4) Déterminer l'état probabiliste P3 et en déduire la probabilité qu'un élève soit favorable à la sortie A la troisième semaine. 5) Déterminer le réel x tel que (x ; 1- x).M = (x ; 1- x). On admet que la suite (an) est croissante. La sortie A finira-t-elle par être préférée à la sortie B ? »

**26-** « On s'intéresse aux performances réalisées par des étudiants courant le 200 mètres dans les compétitions universitaires. Lors d'une compétition, le score d'un(e) étudiant(e) est son meilleur temps en secondes obtenu aux 200 m. Une enquête a permis d'établir le comportement général suivant, qu'on supposera valable pour les filles et les garçons dans toute la suite : · Lors de la première compétition, le score d'un(e) étudiant(e) est toujours supérieur ou égal à 25 secondes. · Si, lors de la n-ième compétition, l'étudiant(e) a réalisé un score strictement inférieur à 25 secondes, la probabilité qu'il (elle) réalise encore un score strictement inférieur à 25 secondes lors de la n+1-ième compétition est de 2/5. · Si, lors de la n-ième compétition, l'étudiant(e) a réalisé un score supérieur ou égal à 25 secondes, la probabilité qu'il (elle) réalise encore un score strictement inférieur à 25 secondes est 1/5. On représente les données précédentes par un graphe probabiliste G à deux états. On note A tout score strictement inférieur à 25 secondes et B tout score supérieur ou égal à 25 secondes. On note an la probabilité d'obtenir un score A lors de la compétition n et bn la probabilité d'obtenir un score B lors de la compétition n. L'état probabiliste lors de la compétition n est donc représenté par la matrice ligne (an bn). 1) Représenter G et donner sa matrice de transition. 2) Mouna, jeune étudiante, se présente à sa première compétition universitaire. a) Calculer la probabilité qu'elle réalise un score strictement inférieur à 25 secondes aux 200 mètres lors de cette compétition. b) Calculer la probabilité qu'elle réalise un score strictement inférieur à 25 secondes aux 200 mètres lors de sa troisième compétition. 3) Déterminer l'état stable du graphe G. 4) Riadh a déjà de nombreuses compétitions universitaires. Montrer que, pour sa prochaine compétition, il a environ une chance sur quatre de réaliser un score strictement inférieur à 25 secondes aux 200 mètres. »

**27-** « Étude de l'évolution météorologique d'un jour à l'autre dans une localité. Tous les résultats seront donnés sous forme de fractions rationnelles.
Partie A · S'il fait sec aujourd'hui, alors il fera encore sec demain avec la probabilité 5/6, donc il fera humide demain avec la probabilité 1/6. · S'il fait humide aujourd'hui, alors il fera encore humide demain avec la probabilité 2/3. Nous sommes dimanche et il fait sec. On s'intéresse à l'évolution météorologique des jours suivants. 1) Construire un arbre de probabilité représentant la situation de dimanche à mercredi. 2) En déduire la probabilité des évènements suivants : J : « il fera sec lundi, mardi et mercredi » ; K : « il fera sec mardi » ; L : « il fera humide mercredi ».
Partie B 1) Soit n un entier naturel, on note : sn la probabilité pour que le jour n, il fasse sec ; hn la probabilité pour que le jour n, il fasse humide ; Pn la matrice (sn hn) traduisant l'état probabiliste du temps le jour n. Déterminer une relation entre sn et hn. 2) a) Si le premier dimanche est le jour correspondant à n = 0, donner la matrice associée à l'état initial du temps. b) Décrire l'évolution de cet état à l'aide d'un graphe probabiliste. 3) La matrice M de ce graphe est [[5/6, 1/6],[1/3, 2/3]]. a) Déterminer M². b) Expliquer comment retrouver à l'aide de la matrice M, la situation du mardi étudiée dans la partie A. 4) a) Déterminer l'état stable associé à l'évolution météorologique. b) En déduire, qu'à long terme, la probabilité qu'il pleuve un certain jour est 1/3. »
(Aucun corrigé dans le manuel pour 1 à 27.)

---------------------------------------------------------------------
#### MATH CULTURE (p. 301)

**I - Une justification du théorème suivant :** (encadré) « Soit G un graphe de matrice associée A. Le nombre de chaînes de longueur n joignant le sommet i au sommet j est égal au terme aij de la matrice An. »
« Soient i et j deux sommets distincts de G. La solution, comme souvent, vient en cherchant un problème plus facile : chercher le nombre de chemins de longueur 1, puis 2, puis 3 reliant i à j. Les chaînes de longueur 1 qui joignent i à j sont les arêtes qui joignent i à j. On notera aij le nombre de ces chaînes de longueur 1 : il vaut 0 si i n'est pas relié à j par une arête, 1 s'il y a une arête qui joint i à j. Comment compter les chaînes de longueur 2 joignant i à j? Une telle chaîne est forcément formée d'une chaîne de longueur 1 allant de i à un certain sommet k, puis d'une chaîne de longueur 1 du même sommet k à j; il faut bien sûr envisager toutes les possibilités pour k. Si bij désigne le nombre de chaînes de longueur 2, on a donc : bij = Σ_k aik . akj la somme étant prise sur tous les sommets du graphe. On reconnaît la formule usuelle du produit de matrices ! Les sommets sont numérotés de 1 à n, on peut donc regrouper les nombres aij définis ci-dessus en une matrice A = (aij). Si l'on note B = (bij) la matrice des chaînes de longueur 2, on vient de voir que B = A², le produit étant le produit matriciel usuel. De même, si l'on note cij le nombre de chaînes de longueur 3 de i à j, on voit que, puisqu'une telle chaîne se décompose en une chaîne de longueur 1 de i à k, suivie d'une chaîne de longueur 2 de k à i, on a : cij = Σ_k aik . bki d'où l'on déduit que la matrice C = (cij) vérifie C = A × B = A³. Il est alors immédiat de généraliser : le nombre de chaînes de longueur n qui joignent le sommet i au sommet j est le terme d'indice i,j de la matrice An. »
(Coquilles imprimées : « de k à i » et « bki » devraient être « de k à j » et « bkj » ; reproduites telles quelles.)

**II - Introduction aux chaînes de Markov** (pictogramme graphe) : « Généralement, un processus stochastique est une suite d'expériences dont le résultat dépend du hasard. Ici, nous admettrons qu'en certains temps 0, 1, 2, ..., t, nous observons un système. Celui-ci peut se trouver dans l'un des états d'une collection finie d'états possibles. L'observation du système est ainsi considérée comme une expérience dont le résultat (aléatoire) est l'état dans lequel se trouve le système. Nous supposons que nous connaissons pour chaque paire d'états i et j, et pour chaque instant t, la probabilité pij(t) que le processus soit dans l'état j à l'instant t+1 étant donné qu'il se trouve dans l'état i à l'instant t. De plus, la probabilité pij(t) sera supposée ne pas dépendre de t. Un tel processus est appelé chaîne de Markov (à temps discret et avec un ensemble fini d'états), du nom de son inventeur Andrei Andreyevich Markov (1856-1922), dont vous voyez le visage ci-contre. Avec ces hypothèses, nous pouvons décrire le système en donnant l'ensemble {u1, ..., um} des états ui possibles et une matrice P de dimensions m × m dont le terme pij est la probabilité que le processus soit dans l'état j à l'instant t+1 étant donné qu'il se trouve dans l'état i à l'instant t, pour tout t. P est appelée matrice de transition du système. On représente généralement P par un graphe orienté G dont les sommets correspondent aux m états et les arcs aux couples ordonnés d'états (i,j) tels que pij>0. »
Source citée : AUCUNE source imprimée (photo de Markov sans légende, pas de référence bibliographique) ; le texte est un emprunt non référencé [?].

---------------------------------------------------------------------
#### VOCABULAIRE OFFICIEL (termes exacts du chapitre)
graphe, sommet, arête, ordre, degré, sommet isolé, sommets adjacents, graphe complet, graphe connexe, sous graphe, chaîne, chaîne fermée, cycle, longueur d'une chaîne, chaîne eulérienne, cycle eulérien, théorème d'Euler, coloriage / colorier un graphe, nombre chromatique γ(G), Δ, graphe pondéré, poids d'une chaîne, algorithme de Dijkstra, plus courte chaîne, algorithme de Welch-Powell (cité en exercices seulement), graphe orienté, arc (origine, extrémité), boucle, chaîne orientée / chemin, cycle orienté / circuit, chaîne orientée eulérienne, cycle orienté eulérien, graphe orienté eulérien, d+(X) / d-(X), matrice associée à un graphe, distance de deux sommets, diamètre d'un graphe, graphe probabiliste, matrice de transition, état probabiliste, état stable, chaîne de Markov (Math culture).

#### BORNES
INCLUS (traité en cours/activités) : théorème d'Euler (admis) ; coloriage, nombre chromatique, encadrement γ ≥ ordre des sous-graphes complets et γ ≤ Δ+1 ; Dijkstra (vérifier un tableau donné) ; graphes orientés, d+/d-, théorème d'Euler orienté (admis) ; matrice associée, symétrie, somme des termes = somme des degrés ; nombre de chaînes de longueur n = terme de A^n (admis, justifié en Math culture) ; distance / diamètre par matrices ((A+Id)^n, admis) ; graphes probabilistes, matrice de transition, pn = p0×M^n (admis), état stable d'un graphe d'ordre 2 sans zéro (X×M = X, x+y = 1, admis), calcul de puissance de matrice avec Derive.
EXCLU / non traité : démonstration des théorèmes d'Euler, du théorème sur A^n (hors Math culture), du théorème de convergence ; description de l'algorithme de Welch-Powell (aucune règle énoncée dans le chapitre, pourtant utilisé aux ex. 6, 8) ; graphes probabilistes d'ordre ≥ 3 : état stable non traité en cours (matrices d'ordre 3 vues en construction, Act. 3) ; chaînes de Markov au-delà de l'introduction.

#### NOTIONS-CLÉS (≤ 8)
1. Théorème d'Euler (chaîne/cycle eulérien : degrés impairs 0 ou 2) et version orientée (d+ = d-).
2. Nombre chromatique : ordre des sous-graphes complets ≤ γ(G) ≤ Δ+1 ; coloriage d'incompatibilités.
3. Plus courte chaîne pondérée (Dijkstra, tableau).
4. Matrice associée, d+ = somme des lignes, d- = somme des colonnes.
5. a_ij(A^n) = nombre de chaînes de longueur n de i à j.
6. Distance et diamètre via A^n et (A+Id)^n.
7. Graphe probabiliste / matrice de transition (lignes de somme 1).
8. pn = p0×M^n ; état stable X×M = X (ordre 2, matrice sans zéro).

---------------------------------------------------------------------
#### § NOTES
- Pages lues : 273 à 301 (29/29), texte (pdftotext) ET image (110 dpi) pour chaque page. Pages agrandies à 170-300 dpi : 275 (graphes act. 1-3), 276 (G1, G2, G act. 2 — K4 vérifié, degré max 5), 279 (act. 2 et tableaux), 280 (act. 4-5), 281 (act. 1 digraphe), 285 (M, M⁴, M⁵), 287 (cinq graphes act. 2), 291 (résultat Derive), 292 (ex. 1-5 figures), plus lectures 110 dpi des autres.
- Figures : les graphes des act. 1 (p.275), act. 4 (p.280), ex. 1, 2, 3, 6, 7, 8, 9, 11, 12, 15, 19 et les orientations de plusieurs digraphes n'ont pas pu être transcrits arête par arête avec certitude : marqués [?]. Sûrs (vérifiés par les matrices ou les tableaux imprimés) : p.275 act. 3 (10 arêtes), p.276 K5 et G act. 2, p.277 Dijkstra (réseau), p.278 tableau act. 2, p.281 act. 1 (13 arcs : d+−d- = +1 en A3, −1 en A4, 0 ailleurs → chaîne eulérienne de A3 à A4, cohérent avec la question 5), p.282 act. 5, ex. 4, 13, 14, 16.
- Coquilles/anomalies imprimées : (1) p.284 Act. 8 : « distance des deux sommets V1 et V4 » alors que la question porte sur V1 et V2. (2) p.282-283 Act. 5 : la numérotation saute de « 2) a) » à « c) ». (3) p.285 : M (Act. 10) n'est pas symétrique : M(3,5)=1 mais M(5,3)=0 ; M(6,3)=1 mais M(3,6)=0 ; M(5,6)=1 mais M(6,5)=0, alors que M⁴ et M⁵ imprimées sont symétriques → [R7 : M relue à 200 dpi : la transcription est conforme à l'imprimé ; la non-symétrie est donc dans le manuel (incohérence imprimée M / M⁴), plus de [?]]. (4) p.281 Conséquences : d-(Si) rapporté à « la i-ième colonne » (correct), rien à signaler. (5) p.287 Act. 2 : notation décimale mixte « 0.6 » / « 0,6 » ; G-b : somme sortante de 2 = 1,4 ; G-c : somme sortante de P = 0,8 (donc non probabilistes). (6) p.289 : « Activité7 » sans espace. (7) Ex. 10 : tableau annoncé « ci-dessus », imprimé dessous ; matrice des temps non symétrique : ligne A, colonne C = 5, ligne C, colonne A = 9. (8) Ex. 12 : « DB » n'est pas un franchissement du tableau (B → D l'est). (9) Ex. 14 : l'arête A-D n'a pas d'étiquette lisible ; 10 étiquettes lues pour 11 arêtes. (10) Math culture : « de k à i » et « bki » au lieu de « k à j » et « bkj ». (11) Ex. 6 et 8 demandent l'algorithme de Welch-Powell sans l'avoir énoncé dans ce chapitre. (12) p.290 Activité 1 : numérotation 1° puis 4° (2°, 3° absents). (13) Ex. 19 : [R7 : orientations levées, cf. ex. 19]. (14) p.279 Act. 3 : figure G1 étiquetée A, B, C, D, F tandis que le tableau 1 porte A, B, C, D, E [?].
- Totaux recomptés : Act. 3 (p.275) degrés 4+3+4+4+3+2 = 20 = 2×10 arêtes ; Act. 3 (p.276) : E1:3, E2:5, E3:4, E4:3, E5:5, E6:4 = 24 croix = 12 paires (symétrique) ; Ex. 16 : trace de M² = 2+3+2+2+2+3 = 14 = 2×7 arêtes ; Act. 5 p.282 : trace A² = 2+1+1+2+2 = 8 = 2×4 arêtes, cohérent.
- `[?]` restants : arêtes/orientations des figures listées ci-dessus ; (M de l'Act. 10 levé par R7 : conforme à l'imprimé.)

## 9. R-7 — rapports des auditeurs (opus, 2026-11-18)

---

### Rapport `R7-R1`

### R7-R1 — Audit R-7 de la fiche Mathématiques Bac Économie et gestion (222463P00), pages 5 à 84

Auditeur R-7, en contexte vierge. Fichiers audités : `m01-p5-32.md`, `m02-p33-62.md`, `m03-p63-84.md`. Corrections appliquées dans ces fichiers par des Edit ancrés et marqués « [R7 : …] ». Pas de git.

#### 1. Contrôle à 100 % des pages présentes
- **Pages contrôlées : 80/80** (p.5 à p.84). Chaque page figure dans un fichier : p.5, 33 et 63 sont des pages de titre sans couche texte, lues à l'image ; p.84 est blanche.
- Méthode : `pdftotext -layout` page par page, puis comparaison automatique par trigrammes de mots normalisés avec le fichier de fiche (script de l'auditeur). Couverture ≥ 0,75 sur toutes les pages sauf p.13 (0,71, lignes de formules) et p.83 (0,54, Math culture paraphrasée). J'ai relu une par une les 88 lignes sous le seuil : ce sont des lignes de formules dégradées par la couche texte (présentes dans la fiche en LaTeX), des pas à pas Excel condensés (p.52, 74, 75, contenu conservé) et, en p.83, la Math culture paraphrasée. Une seule omission réelle : une phrase de la p.83, rétablie (voir F6).

#### 2. Sondage image : 55 pages sur 80 (69 %)
Rendu à 130 dpi dans `render-r7m-R1/` ; zoom à 220-300 dpi pour p.9, 44, 55, 57 et 72.
- **m01 (20)** : 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 22, 25, 27, 28, 29, 30, 31
- **m02 (21)** : 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 50, 53, 54, 55, 56, 57, 58, 60, 61
- **m03 (14)** : 64, 66, 67, 68, 69, 70, 72, 73, 75, 76, 77, 78, 81, 82

Pages prioritaires couvertes : tous les encadrés (définitions, théorèmes, propriétés, corollaires), les tableaux de variations (p.40, 54, 57, 76, 77, 78), les tableaux de primitives (p.50), les tableurs (p.25, 53, 75) et les pages signalées « coquille ».

Coquilles signalées par les lecteurs et confirmées à l'image : p.12 Act. 6 (numéro 2 absent) ; p.14 (« trois fonctions », « f(0)=1 » pour g) ; p.17-18 (deux Activité 3) ; p.25 (formule SIN(PI()/A3)) ; p.29 Ex. 11-b (g puis f), Ex. 13 « [1,+∞] », Ex. 14 « page 30 » ; p.30 Ex. 19 « x + x/4 » ; p.47 Act. 3 c ; p.56 Ex. 12 « croissante » ; p.67 (encadré à deux « x→+∞ », pas d'Activité 3) ; p.69 (« 4- » répété) ; p.73 (confusion f/g) ; p.75 (y imprimés positifs) ; p.78 Ex. 13 (tableau incohérent avec f). **Aucune coquille imputée à tort au manuel.** Un faux positif possible a été écarté : à 130 dpi, la p.44 semblait montrer « ]−1,+≠[ », mais à 300 dpi c'est bien « +∞ ». La fiche est correcte sur ce point.

Formules, bornes, exposants, signes et valeurs des énoncés et des encadrés : aucun écart sur les 55 pages sondées.

#### 3. Constats

##### SUBSTANTIEL : 4, tous corrigés (tous dans m02, section Exercices p.54-61, et tous des lectures de figures)
| # | Page | Avant | Après | État |
|---|---|---|---|---|
| S1 | p.55 Ex. 4, figure gauche | branche gauche « croissante vers −∞ », branche droite « décroissante vers −∞ puis remontée », maximum central ≈ 2, deux asymptotes | branche gauche croissante vers **+∞** (asymptote x ≈ −1) ; morceau central de −∞ à un maximum ≈ **3** en x ≈ 1/2, puis retour vers −∞ (asymptotes x ≈ −0,8 et x ≈ 1,8) ; branche droite **décroissante depuis +∞** (x ≈ 2) jusqu'à ≈ −3. Le sens de variation était inversé, donc le tableau demandé aurait été faux | corrigé |
| S2 | p.55 Ex. 4, figure droite | départ x ≈ −3, maximum vers x ≈ −2/−1, maximum final vers x ≈ 4,5-5 d'ordonnée 2-3 | départ **x ≈ −6** (tangente verticale) ; maximum **(−4, 4)** ; point anguleux (1, −2) ; extrémité **(6, 3)** à tangente horizontale | corrigé |
| S3 | p.57 Ex. 17 (courbe de f ') | minimum ≈ −1,5 en x = 1 ; maximum ≈ 3 en x = 5 | minimum **(1, −3)** ; maximum **(5, 4)** (1 carreau = 1 unité, points sur des nœuds). Les coefficients directeurs demandés en 2) en dépendent | corrigé |
| S4 | p.60, graphique de l'Ex. 23 | courbe noire : minimum ≈ 50-60 ; courbe rose : minimum ≈ 15-20 | noire : minimum **≈ 24** vers x ≈ 6 ; rose : minimum **≈ 12** vers x ≈ 4 ; la graduation tronquée « +2 » correspond à x = 20 | corrigé |

Les lecteurs avaient signalé ces quatre lectures comme estimations [?]. Elles sont fausses de façon mesurable sur le quadrillage, d'où le classement en SUBSTANTIEL. Comme il y a 3 écarts ou plus dans la section, j'ai relu à l'image toutes les figures des p.54-61. Dans les énoncés et formules de cette section, je ne relève aucun écart.

##### FORME : 8, tous corrigés
| # | Page | Avant → après | État |
|---|---|---|---|
| F1 | p.10 (m01), figure Act. 1 | « deux hyperboles noires » → une hyperbole noire et une rose | corrigé |
| F2 | p.56 (m02), Ex. 11 | départ « (0, −1) » → (0, ≈ −0,5) : le vecteur unité couvre 2 carreaux | corrigé |
| F3 | p.34 (m02), Act. 1 | numéros 1-10 présentés comme imprimés → ajout signalé comme venant du lecteur | corrigé |
| F4 | p.69 (m03), Act. 1 | $\lim_{x\to\infty}$ → $\lim_{x\to+\infty}$ | corrigé |
| F5 | p.72 (m03), Act. 3 2-c | « ]2,+∞[ » corrigé en silence → « ]2,+∞] » tel qu'imprimé (vérifié à 300 dpi), signalé comme coquille | corrigé |
| F5b | p.72 (m03), Act. 3 2-a | renvoi « [voir § Notes] » sans note correspondante → supprimé, avec le motif | corrigé |
| F6 | p.83 (m03), Math culture | phrase « En construisant les deux courbes… se réalise l'échange » omise → rétablie verbatim | corrigé |
| F7 | p.78 (m03), Notes, Ex. 13 | recalcul f(0)=1 et f' non étiqueté → étiqueté « recalcul du lecteur, non imprimé » | corrigé |

#### 4. Rien d'inventé
Aucun corrigé n'est attribué au manuel. Les recalculs des lecteurs (m01 p.7, 19 ; m02 p.41, 48, 57, 59, 61 ; m03 p.78) sont étiquetés comme tels. F7 répare le seul qui ne l'était pas.

#### 5. `[?]` restants
- Valeurs lues sur des figures non cotées : m01 p.17 (graphique 3) et p.18 (extrema d'environ ±2,3) ; m02 p.35, 37, 39, 40, 43, 44, 55, 56, 57, 60 ; m03 Ex. 1 et 13 (symbole « O » lu comme 0) et figures qualitatives.
- Aucun `[?]` ne porte sur une formule, un énoncé ou un tableau chiffré.

#### 6. Taux par 10 pages
| Section | Pages | Substantiels | Taux / 10 p. |
|---|---|---|---|
| m01, ch. I (p.5-32) | 28 | 0 | 0,0 |
| m02, Pour commencer + Cours + Avec l'ordinateur (p.33-53) | 21 | 0 | 0,0 |
| m02, Exercices (p.54-61) + Math culture (p.62) | 9 | 4 | **4,4** |
| m03, ch. III (p.63-84) | 22 | 0 | 0,0 |
| **Ensemble** | 80 | 4 | 0,5 |

#### Verdict
Textes, encadrés, formules, tableaux et énoncés sont fidèles sur les trois fichiers. **La section Exercices de m02 (p.54-62) passe sous la barre** avant correction : 4 substantiels pour 9 pages, soit 4,4 pour 10 pages. Tous concernent des lectures de figures (Ex. 4, 17, 23) et tous sont corrigés. Les autres sections sont au-dessus de la barre. Après correction, la fiche p.5-84 est utilisable. Conseil aux auteurs : redessiner les figures des Ex. 4, 11, 17 et 23 à partir des points relevés sur le quadrillage plutôt qu'à partir des descriptions.

---

### Rapport `R7-R2`

### R7-R2 — Audit (contexte vierge) des tranches m04 (pp.85-114) et m05 (pp.115-136)

Manuel : CNP 222463P00 (Mathématiques, Bac Économie et gestion). Rendus : `/root/.cache/yqa-manuels/render-r7m-R2/` (130 dpi ; zooms 250-300 dpi).

#### Couverture
- **Pages contrôlées : 52/52** (85 à 136). Toutes les pages figurent dans les fichiers ; aucune n'est absente.
- **Pages sondées à l'image : 52/52 (100 %)** : 85-136, comparées à la fiche mot à mot et symbole par symbole (encadrés, exemples, tableaux, figures, bornes d'intégrales, exposants).
- **Zooms 250-300 dpi** : p.87 (les trois courbes de l'Act. 1), p.99 (Act. 9, dénominateur), p.127 (code VB, `aire =`), p.129 (ex. 1 d et e, bornes).
- Comparaison avec la couche texte : pdftotext sur les points douteux (p.99, p.108, p.109-113) ; le reste de la prose a été comparé directement à l'image.

#### Constats SUBSTANTIELS (2, tous corrigés)
| # | Page | Fichier | Avant | Après | État |
|---|---|---|---|---|---|
| S1 | p.87 | m04 | Figure de l'Act. 1 : 2e courbe « passant par un point d'ordonnée ≈ 1 en x≈1 » ; 1re et 3e « de même allure », sans rien qui les distingue (on ne pouvait pas répondre à la q.1). | 2e courbe décroissante passant par (1 ; 0), tangente de pente −1 ; 1re courbe : tangente en (1 ; 0) de pente 1 ; 3e : tangente de pente ≈ 1/2. | corrigé |
| S2 | p.129 | m05 | Ex. 1 d) $\int_{-1}^0 x^2dx$ (et § Notes « tranché à l'image : ∫_{-1}^0 »). | $\int_0^{-1} x^2dx$ (0 en bas, −1 en haut, à 300 dpi) : le signe attendu s'inverse. Note corrigée elle aussi. | corrigé |

#### Constats FORME (9, tous corrigés)
| # | Page | Fichier | Avant → Après |
|---|---|---|---|
| F1 | p.88 | m04 | Act. 3 « ln x/(x+2) » (ambigu) → « (ln x)/(x+2) » |
| F2 | p.99 | m04 | Act. 9, hypothèse non imprimée « probablement x/(eˣ−1) ou eˣ/(eˣ−1) » → imprimé confirmé eˣ/(eˣ−1) ; hypothèse eˣ/(eˣ−x) marquée « auditeur, non imprimée » |
| F3 | p.100 | m04 | « Taux annuel implicite 5,5 % » présenté comme un fait → marqué « déduction du lecteur, non imprimée » |
| F4 | p.101 | m04 | Act. 4 q.3 : un « a) » qui n'est pas imprimé → signalé |
| F5 | p.102 | m04 | « le manuel indique t … ≈ 4,8 » (contradictoire) → le manuel ne donne que ln4/(ln4−ln3) ; ≈ 4,82 est un recalcul de l'auditeur |
| F6 | p.105 | m04 | Ex. 12 « 1 + 2 ln x / x » → « 1 + (2 ln x)/x » |
| F7 | p.107 | m04 | Ex. 20, maximum de la figure « vers x ≈ −2,5 » → « ≈ −2 » |
| F8 | p.110 | m04 | Ex. 32, minimum de la figure « 0,6-0,7 vers x≈3 ; ≈3,5 vers x≈5,3 » → « 0,7-0,8 vers x≈2,5 ; ≈3,4 vers x≈5,1 » (lecture approximative) |
| F9 | p.127 | m05 | `aire =` « ILLISIBLE/absente » [?] → à 250 dpi, la valeur est absente de l'impression (coquille du manuel) ; [?] levé |

#### Coquilles imputées au manuel, vérifiées à l'image (toutes bien imprimées)
- **m04** :
  - p.86 : F écrite f.
  - p.90 : « ln 3 ≃ 0,1 », et « Pour tout réel » sans a > 0.
  - p.93 : C_g/C_f inversées et « courbe C ».
  - p.94 : « f et g », « p0 », et « g » pour exp.
  - p.96 : « eˣ(1+eˣ) = 1+e^{2x} ».
  - p.99 : eˣ/(eˣ−1) « sur IR ».
  - p.102 : numérotation 2-, puis 4-.
  - p.103 : « i et aire ».
  - p.104 : ex. 5 étiqueté a-b-a-d ; ex. 6 sans f.
  - p.105 : ex. 10 « ]0,+∞[ » avec f(0).
  - p.106 : ex. 13 a) puis c) ; ex. 15 f) « 2e^{−0,5+7} » ; ex. 16, équation répétée.
  - p.109 : « figure précédente ».
- **m05** :
  - p.116 : étiquettes a-c-c-d et parenthèse non refermée.
  - p.122 : bornes ∫_2^0.
  - p.123 : légende inversée et « p₀ ».
  - p.124 : « largeur h ».
  - p.128 : A1 « 4/(1+x²) ».
  - p.129 : ex. 4 borne « e ».
  - p.130 : bornes de f, j, l.
  - p.131 : « dt » et « d'un intégration ».
  - p.134 : ex. 20 « a, b » non définis.
  - p.135 : « Lorentz » sans point, « γi », « G, K et L ».
  - p.136 : n(t)/N(t).
- **Aucune correction silencieuse n'a été trouvée.**

#### Recalculs de la fiche contrôlés (tous étiquetés, tous justes)
- m04 :
  - Act. 5 p.93 : bornes de α et β.
  - Ex. 30 : f′ et C′_m.
  - Ex. 32 : f′, et C = F + 1.
  - Ex. 33 : C_m.
  - Ex. 34 : g.
  - Ex. 35 : q₀ = 200 et 30 DT par objet.
- m05 :
  - Act. 3 p.116 : la droite x/2 + 3, vérifiée sur le quadrillage.
  - Act. 3 p.124 : f(−2) = f(1) = 1 et f(−1) = 5.
  - Act. 7 p.126.
  - Ex. 8.
  - Ex. 13 : 71,85 et 5,13.
  - Ex. 17 : facteur 4.
  - Valeurs du tableur p.128.

#### [?] restants
- m04 :
  - ln 3 ≃ 0,1 (imprimé ; valeur voulue douteuse).
  - Fonction de l'Act. 9 p.99 (imprimé eˣ/(eˣ−1) ; eˣ/(eˣ−x) plausible).
  - Exposant de l'ex. 15 f).
  - Lectures graphiques approchées : ex. 20 et ex. 32.
- m05 : aucun.

#### Taux
- m04 (30 p.) : 1 substantiel, soit **0,33 / 10 pages** ; 8 de forme (2,7 / 10).
- m05 (22 p.) : 1 substantiel, soit **0,45 / 10 pages** ; 1 de forme (0,45 / 10).
- Aucune section n'atteint 3 substantiels pour 10 pages : **au-dessus de la barre** pour les deux tranches.

---

### Rapport `R7-R3`

### R7-R3 — Audit R-7 (contexte vierge) : manuel Mathématiques Bac Économie et gestion (CNP 222463P00), pages 137-200

Fichiers audités : `m06-p137-164.md` (ch. VI Suites réelles, p.137-164) ; `m07-p165-200.md` (ch. VII Matrices et systèmes, p.165-200).
Méthode : contrôle 100 % couche texte (`pdftotext -layout`, page par page) ; sondage image `pdftoppm -r 130` (zoom 250-300 dpi au doute), rendus dans `render-r7m-R3/`.

#### Contrôle de présence
- Pages contrôlées : **64 / 64** (137-200). Toutes présentes dans les fiches ; p.165 (titre, sans couche texte) et p.200 (blanche) signalées comme telles. Aucune phrase, consigne ou donnée omise relevée à la comparaison texte (la Math culture p.164 est en résumé fidèle annoncé, chiffres verbatim).

#### Sondage image
- Pages sondées : **47 / 64 = 73 %**.
  - m06 (22/28) : 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 162.
  - m07 (25/36) : 166, 168, 170, 172, 174, 175, 176, 177, 178, 179, 180, 182, 183, 184, 186, 187, 189, 190, 191, 193, 194, 195, 196, 197, 199.
- Priorités couvertes : tous les encadrés définitions/théorèmes/propriétés des deux chapitres (p.140-148, 150-151, 167-186), le tableau des limites p.147, les captures tableur/Excel (p.154, 189, 190), les 4 nuages de points p.138-139 (valeurs « lu » confirmées), la figure p.150, toutes les pages à « coquille » signalée (139, 143, 148, 149→texte, 153, 154, 155, 156, 157, 158, 160-163 texte, 176, 178, 183, 190, 191, 195).
- Coquilles imputées au manuel : toutes vérifiées imprimées (p.139 u/v ; p.143 « minorée par 2 » et (u_n) pour (v_n) ; p.148 « par tout », v_n ≥ 3n−1 ; p.154 U_0 = 2 vs B2 = 10, « de d'utiliser », « On deux lignes » ; p.155 formules K_{n+1}=K_n+i×K_n et C_{n+1}=C_n+i×C_0 ; p.157 bornes 1/(2n+1) ; p.158 « n ∈ ℕ n ∈ IN » ; p.176 « atelier secrétariat », « la matrice R » ; p.178 a) puis c) ; p.183 « A22 » ; p.190 A^{-1} pour C^{-1} et D^{-1} incohérente (dét D = 163 recalculé par l'auditeur, confirmé) ; p.191 Q6 absente, Q8 (dét = −13) ; p.195 « son-elles », « entées »). Aucune correction silencieuse détectée.
- Contrôle de glyphe p.176 (définition du produit) : à 300 dpi, les indices finaux de c_ij = a_i1 b_1j + … semblent « i » parce que la jambe du j est rognée par le bord de l'encadré ; la couche texte donne « j » — la fiche (j) est juste.

#### Constats

##### SUBSTANTIEL (1)
| # | Fichier / page | Avant | Après | Statut |
|---|---|---|---|---|
| S1 | m06, p.157, exercice 11 f) | « $|u_n-\frac12|\le10^{-3}$ ? [note : la valeur absolue est imprimée] » | « $u_n-\frac12\le10^{-3}$ ? » + note R7 : AUCUNE valeur absolue imprimée (vérifié 250 dpi) | corrigé (corps + § Notes) |

Effet : section « Exercices et problèmes » du ch. VI (p.155-163, 9 pages) → 1 substantiel ; le sondage de toute la section a été fait (p.155-160, 162 à l'image, 161/163 au texte) : aucun autre écart.

##### FORME (2)
| # | Fichier / page | Avant | Après | Statut |
|---|---|---|---|---|
| F1 | m06, p.153, Act. 7 | intervalle ouvert en 1d et « non nul » en 2a qualifiés de « coquilles » | note R7 : bien imprimés, mais particularités d'énoncé (même schéma ex. 22-23), pas des fautes typographiques | corrigé (annotation) |
| F2 | m07, p.176, Act. 7 | « la question 1 y nomme « la matrice R » » | c'est la phrase d'introduction du schéma qui nomme R | corrigé |

#### `[?]` restants
Aucun `[?]` dans les deux fiches. Réserves de lecture déjà étiquetées par les lecteurs et confirmées à l'image : points « lu » des graphiques p.138-139 (cohérents : q = 1/2 ; r = −1,5 ; q ≈ −0,8 ; r = 2) ; exposant ex. 9k « 0,1n+2 » (confirmé à l'image p.156).

#### Rien d'inventé
Les fiches n'attribuent aucun corrigé au manuel ; tous les recalculs sont étiquetés « recalcul / calcul du lecteur ». Recalculs de l'auditeur concordants : dét D (p.190) = 163 ; A^{-1} p.186 (1/29) exact ; dét D p.179 = −5 ; x = −1/4 (p.172) ; dét C p.190 = 5 ; Q5 p.191 : c11 = −2√2 − 23.

#### Taux
- Global : 1 substantiel / 64 pages = **0,16 pour 10 pages** ; forme : 0,31 pour 10 pages.
- Par section : ch. VI Exercices (p.155-163) 1,1 / 10 pages ; toutes les autres sections : 0.
- Verdict : **au-dessus de la barre** (aucune section ≥ 3 substantiels pour 10 pages).

---

### Rapport `R7-R4`

### R7-R4 — Audit (contexte vierge) des tranches m08 (pp.201-236), m09 (pp.237-272) et m10 (pp.273-301)

Manuel : CNP 222463P00 (Mathématiques, Bac Économie et gestion). Rendus : `/root/.cache/yqa-manuels/render-r7m-R4/` (130 dpi pour les 101 pages ; zooms à 200-400 dpi : p.252, 280, 281, 282, 283, 284, 285, 292).

#### Couverture
- **Pages contrôlées : 101/101** (201 à 301). Toutes les pages figurent dans les fichiers ; aucune page absente.
- **Contrôle texte, automatisé sur 100 % des pages** : chaque nombre et chaque mot de 5 lettres ou plus de `pdftotext -layout`, page par page, a été cherché dans la fiche. Aucun énoncé, aucune consigne ni aucune donnée ne manque. Les seuls écarts sont des faux positifs (décimales, « Etape », « entrée » des touches de calculatrice) et un mot imprimé corrigé sans le dire (« cordonnées », p.232).
- **Pages sondées à l'image : 50/101 (49,5 %)** :
  - m08 (22) : 202, 203, 205, 206, 207, 209, 210, 212, 213, 214, 215, 217, 218, 219, 220, 221, 223, 224, 226, 228, 232, 234 ;
  - m09 (15) : 240, 242, 244, 245, 246, 247, 252, 255, 256, 257, 260, 262, 263, 264, 271 ;
  - m10 (13) : 274, 277, 278, 279, 280, 281, 282, 283, 284, 285, 287, 292, 296.
  - Ce sondage couvre tous les encadrés (définitions, théorèmes, propriétés) des pages sondées, les tableaux de données, les arbres et les graphes.
- **Recalculs de contrôle (auditeur, non imprimés)** : nous avons recompté les totaux de p.202, 203 et 209. Nous avons recalculé les statistiques de p.212-213 (x̄ = 11,4 ; V = 9,04 ; cov = 5,28) et E/V/σ du Q7 de p.262. Les puissances de matrices imprimées sont retrouvées à partir des arêtes : A² et A³ (p.283 Act.5), M² et M⁵ (ex.16), M² (ex.21), A²…A⁵ (p.283 Act.7), A⁵ et A⁶ (ex.19). La matrice M de p.285, relue à 200 dpi, est conforme à l'imprimé.
- **Section relue entièrement à l'image** (règle des « trois écarts ») : m10 Cours II, pp.278-285.

#### Constats SUBSTANTIELS (10, tous corrigés)
| # | Page | Fichier | Avant | Après | État |
|---|---|---|---|---|---|
| S1 | p.280 | m10 | Act.5 (plan du quartier) : arc « P→B 10 » | B→P 10 (orientation relue à 400 dpi) : la question « de D à P » en dépend | corrigé |
| S2 | p.283 | m10 | Act.7 : « 6 arcs : S1→S2, S4→S1, S2→S4, S4→S2 ou S2→S3, S3→S2, S3→S4 [?] » | 7 arcs : S1→S2, S1→S4, S2→S4, S3→S2, S3→S4, S4→S2, S4→S3 (image à 300 dpi, plus le calcul : seule matrice 0/1 qui redonne A²…A⁵ imprimées) | corrigé |
| S3 | p.282 | m10 | Act.4 (ii) : arc « c→b » | b→c (la flèche pointe vers c, 400 dpi) ; graphe (iii) précisé (A-B, B-C, D-C, A-C) | corrigé |
| S4 | p.296 | m10 | Ex.19 : arc « 5→3 » | 3→5 (vérifié : A⁵ et A⁶ imprimées sont retrouvées exactement) | corrigé |
| S5 | p.292 | m10 | Ex.1 : arête « E-D » | E-A (pas d'arête E-D ; 400 dpi) | corrigé |
| S6 | p.281 | m10 | « (sic : « i-ième » pour d-) » : coquille imputée au manuel | retiré : « i-ième colonne » est correct | corrigé |
| S7 | p.203 | m08 | Note : « y_i le centre de la classe C_i alors que x est discret » présenté comme coquille | retiré : ce n'est pas une coquille (y est donné par classes) | corrigé |
| S8 | p.215 | m08 | Coquille « de y en , on note a » imputée aussi à p.215 Act.3 | rattachée à p.218 seulement ; p.215 est complète | corrigé |
| S9 | p.220 | m08 | Coquille « sera » imputée à p.220 | retirée : p.220 imprime « seront donnés » | corrigé |
| S10 | p.225 | m08 | Coquille « dans »/« 𝜎 » imputée à Ex.3 | retirée : rien de fautif n'est imprimé | corrigé |

#### Constats FORME (9, tous corrigés)
| # | Page | Fichier | Avant → Après |
|---|---|---|---|
| F1 | p.212 | m08 | Nuage 2 « ≈ 9 points » → 8 points (comptés à l'image) |
| F2 | p.232 | m08 | « coordonnées » (corrigé sans le dire) → « cordonnées [sic] », tel qu'imprimé |
| F3 | p.219 | m08 | Taux de 1988 « 74,6 » → « 74.6 » (point décimal imprimé) |
| F4 | p.218 | m08 | Coquille citée « une fonction affine » → « deux fonctions affine » (texte imprimé) |
| F5 | p.255 | m09 | Arbre « seules les branches du 1er lancer étiquetées » → arbre complet sur 3 niveaux avec nœuds S/E étiquetés ; seules les pondérations manquent au-delà du 1er niveau |
| F6 | p.242 | m09 | « p(B/A) » (corrigé sans le dire) → « p((B/A) [sic] », tel qu'imprimé |
| F7 | p.256 | m09 | Notation C(n,k) sans renvoi → mention de la notation du manuel $C_n^k$ |
| F8 | p.296 | m10 | Note ex.19 « lignes 2 et 5 de A⁵ différentes » → identiques |
| F9 | p.285 | m10 | M de l'Act.10 « lignes 5-6 à vérifier [?] » → conforme à l'imprimé (200 dpi) ; la non-symétrie de M face à M⁴ et M⁵ est une incohérence du manuel |

Coquilles du manuel vérifiées comme réellement imprimées (non imputées à tort) :
- **m08** : 2581 (p.223), « 20010 » (p.230), la droite d' de l'ex.12, « Produit Naturel Brut », « V1 et V4 » (p.284), y(1997) = 100 (Pb.4) ;
- **m09** : tableau Y 1/7, 3/7, 1/7 (p.252), « Salarié/Salarié » (p.240), remarque p(B)=0 ⇒ p(A/B)=0, p(G/R) (p.242), « sucées », « a euros » ;
- **m10** : G1 étiqueté F contre E dans le tableau (p.279), numérotation a) → c) (p.283).

#### `[?]` restants
- **m08 : 4.** Lectures approchées de graphiques, sans valeur imprimée : p.203, p.211, p.212, p.222.
- **m09 : 3.** Le tableau Y de p.252 (incohérence du manuel), la clé du Q7 de p.262 (aucune clé imprimée), et un renvoi.
- **m10 : 23.** Ce sont surtout des figures qui ne sont pas transcrites arête par arête : p.275 Act.1, p.279 G1/G2/G3, p.280 Act.4, ex.2, 3, 5, 6, 7, 8, 9, 11, 15 et l'étiquette A-D de l'ex.14. Ce trou est signalé honnêtement. À reprendre à l'image avant de générer à partir de ces exercices de graphes.

#### Taux par section (substantiels pour 10 pages)
| Section | Pages | Substantiels | Taux / 10 p. |
|---|---|---|---|
| m08 Pour commencer (201-204) | 4 | 1 | 2,5 |
| m08 Cours (205-221) | 17 | 2 | 1,2 |
| m08 Ordinateur + Exercices + Math culture (222-236) | 15 | 1 | 0,7 |
| m09 (toutes sections, 237-272) | 36 | 0 | 0 |
| m10 Pour commencer + Cours I (273-277) | 5 | 0 | 0 |
| **m10 Cours II (278-285)** | **8** | **4** | **5,0 → sous la barre** |
| m10 Cours III + Ordinateur (286-291) | 6 | 0 | 0 |
| m10 Exercices + Math culture (292-301) | 10 | 2 | 2,0 |
| **Global** | **101** | **10** | **1,0** |

#### Verdict
- **m08** : au-dessus de la barre. Ses 4 constats substantiels sont des coquilles imputées à tort dans les § Notes ; aucune donnée ni formule n'est fausse.
- **m09** : au-dessus de la barre, sans aucun constat substantiel.
- **m10** : **sous la barre pour la section Cours II (pp.278-285)**, avec 4 constats substantiels pour 8 pages : 3 orientations d'arcs fausses et 1 coquille imputée à tort. Cette section a été relue en entier à l'image et les 4 écarts sont corrigés. Les figures des exercices de graphes restent [?].
