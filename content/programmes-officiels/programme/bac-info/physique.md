<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source : manuel élève officiel CNP 223471P00 (399 p.), physique, 4ème année secondaire Sciences de
     l'informatique. Aucun guide enseignant au corpus pour ce couple ⇒ le manuel élève fait référence.
     Lu le 2026-11-07 depuis le Drive `cnp-officiel` : couche texte (L1, `pdftotext -layout` page par page)
     puis vérification sur l'image (110 dpi) des pages à formule, encadré, tableau, montage ou courbe exploitée ;
     page PDF = page imprimée (offset 0). Fiche DIFFÉRENTIELLE : le contenu généré adaptera les chapitres déjà
     publiés de `physique-bac-sciences-exp` (autre manuel, 223433P00) là où il existe une référence ; ch.4 et
     ch.6 à 9, 12 et 13 n'en ont aucune (à écrire de zéro). ⚠️ Chaque chapitre commence une page AVANT sa page
     d'ouverture numérotée (page « Objectifs / Prérequis ») : les plages ci-dessous sont celles constatées. -->

# Physique — Bac Sciences de l'informatique (`bac-info`) · manuel officiel CNP

> **Source (Drive `cnp-officiel`, `manuels/`)** :
>
> - **Manuel élève** : code **223471P00** (399 p.) — 13 chapitres en deux thèmes (évolution de systèmes :
>   ch.1–9 ; ondes : ch.10–13) ; réponses aux exercices p.392–397 ; p.398–399 : sites web.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
> - **Langue d'enseignement** : **fr**. **subject id** : `physique-bac-info` · **gradeSlug** : `bac-info`.
> - **Notation** : chiffres occidentaux 0-9, unités SI ; la couche texte dégrade formules, indices, exposants,
>   vecteurs, courbes et schémas de montage : tout cela est rétabli sur l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Sciences de l'informatique. Les trois premiers chapitres (condensateur,
bobine, oscillations libres) et le chapitre 10 reprennent presque mot pour mot les chapitres correspondants du
manuel 223433 (Sciences expérimentales) ; les chapitres 4 (oscillations entretenues), 6 à 9 (filtres,
signaux non sinusoïdaux, conversion) et 12–13 (transmission, modulation) sont propres à cette section et
n'ont aucune référence publiée. Chaque section ci-dessous donne le plan du chapitre, ses activités et exercices
en une ligne, ses encadrés verbatim, l'**écart avec la référence**, les bornes de scope ✅/⛔ et la note de
lecture (pages vues sur l'image, coquilles `[sic]`, doutes `[?]`).

## 2. Plan annuel (carte des chapitres)

> `generation` = transcrit à profondeur de génération. La couverture de pages vit dans `suivi/bac-info.json`.
> Colonne « référence » : chapitre(s) publié(s) de `physique-bac-sciences-exp` à adapter ; « — » = à écrire de zéro.

| # | Chapitre | pages | référence à adapter | profondeur |
| --- | -------- | ----- | ------------------- | ---------- |
| 1 | Le condensateur ; le dipôle RC | 10–41 | `physique-bac-sciences-exp/01` | `generation` |
| 2 | La bobine ; le dipôle RL | 42–77 | `physique-bac-sciences-exp/02` | `generation` |
| 3 | Oscillations électriques libres | 78–109 | `physique-bac-sciences-exp/03` | `generation` |
| 4 | Oscillations électriques entretenues | 110–129 | — | `generation` |
| 5 | Oscillations électriques forcées en régime sinusoïdal | 130–157 | `physique-bac-sciences-exp/04` (sans la partie « charge q ») | `generation` |
| 6 | Généralités sur les filtres | 158–173 | — | `generation` |
| 7 | Exemples de filtres | 174–219 | — | `generation` |
| 8 | Production de signaux non sinusoïdaux | 220–247 | — | `generation` |
| 9 | Conversion de signaux | 248–273 | — | `generation` |
| 10 | Ondes mécaniques progressives | 274–307 | `physique-bac-sciences-exp/07` (mot pour mot, sans les ondes sismiques) | `generation` |
| 11 | Interactions onde-matière | 308–337 | `physique-bac-sciences-exp/08` (partiel : diffraction, dispersion) | `generation` |
| 12 | Généralités sur la transmission des signaux | 338–363 | — | `generation` |
| 13 | Modulation et démodulation des signaux | 364–391 | — | `generation` |

<!-- Partie A de la fiche différentielle « Physique — Bac Sciences de l'informatique », manuel élève CNP
     223471P00. Chapitres 1 à 3. Lu le 2026-11-07 : couche texte page par page (pdftotext -layout) et
     image 110 dpi de CHAQUE page du chapitre (pages de garde, cours, exercices, fiches, réponses).
     Référence de comparaison : physique-bac-sciences-exp (manuel 223433P00), fiche
     programme/bac-sciences-exp/physique.md §2.1–2.3 et chapitres publiés 01, 02, 03. -->

> **Constat d'ensemble (chapitres 1–3)** : le texte, les figures, les activités, les exercices et la
> pagination de ces trois chapitres sont ceux du manuel 223433 (Sciences expérimentales) **à quelques
> lignes près** — même découpage, mêmes numéros de figures, mêmes données, mêmes exercices numérotés à
> l'identique. Les plages réelles sont **décalées d'une page par rapport au brief** : ch1 = **p.10–41**,
> ch2 = **p.42–77**, ch3 = **p.78–109** (exactement les plages du manuel 223433 ; p.110 ouvre le ch4
> « Oscillations électriques entretenues »). Les écarts constatés sont listés, page par page, dans
> chaque rubrique « Écart avec la référence ».

## 2.1 Chapitre 1 — Le condensateur ; le dipôle RC (manuel 223471, p.10–41)

Bandeau de page : « Evolution de systèmes ◆ Le condensateur ; le dipôle RC ». Le thème s'appelle au
sommaire du thème (p.9) « SYSTÈMES ELECTRIQUES » (sommaire p.4 : « ÉVOLUTION DE SYSTÈMES ÉLECTRIQUES »),
chapitres 1 à 9. Deux leçons titrées : « LE CONDENSATEUR » (p.12–20) et « LE DIPÔLE RC » (p.21–30), puis
« L'essentiel » (p.31), « Exercices » (exercice résolu p.32–33, exercices à résoudre p.34–37), « Fiche
technique » (p.38–39), « En savoir plus » (p.40–41). Notation : « Log » = logarithme népérien (p.30, p.33
« 2 log10 ») ; u_C / uc, Q_o / Q₀, I_o / I₀ indifféremment.

**Objectifs (p.10, VERBATIM, lu sur l'image)** — « Réaliser la charge et la décharge d'un condensateur. » ·
« Reconnaitre que l'intensité i du courant électrique est une grandeur algébrique. » · « Déterminer à
l'aide de la courbe de charge d'un condensateur, la valeur de la capacité C. » · « Déterminer
graphiquement la constante de temps τ = RC d'un dipôle RC. » · « Établir l'équation différentielle
régissant, au cours du phénomène de charge d'un condensateur : - la charge instantanée q(t) du
condensateur, - la tension u(t) à ses bornes, - l'intensité i(t) du courant transitoire parcourant le
circuit. » · « Calculer l'énergie emmagasinée par un condensateur. »

**Prérequis (p.10)** — SAVOIR : Définir : l'intensité du courant électrique, la tension (ou d.d.p)
électrique, la quantité d'électricité, un résistor ; « Ecrire la relation Q = I.Δt » ; « **Enoncer la
convention récepteur et la convention générateur.** » ; Enoncer : la loi des mailles, la loi des noeuds,
la loi d'Ohm relative à un résistor, la loi d'Ohm relative à un générateur. SAVOIR FAIRE : distinguer
tension continue / tension variable ; utiliser un oscilloscope bicourbe ; calculer Q = I.Δt ; reconnaître
une tension variable alternative ; reconnaître une tension en créneaux ; « **Utiliser les conventions
récepteur et générateur.** » ; appliquer la loi d'Ohm pour un résistor et pour un générateur ; appliquer
la loi des mailles.

**Page d'ouverture (p.11)** — « LE CONDENSATEUR / LE DIPÔLE RC », n° 1 ; photo d'un appareil (écran
« Launch when ready. ») ; légende : « L'éclair lumineux de très forte intensité d'une lampe flasch [sic]
d'un appareil photo se produit grâce à un condensateur. » Questionnement (VERBATIM) : « Le condensateur est
un composant électrique connu comme un réservoir d'énergie. De quelle forme d'énergie s'agit-il et
qu'est-ce qui confère au condensateur cette propriété ? » · « Quel est le principe de fonctionnement du
flash d'un appareil photo ? »

**Plan (titres numérotés)** — LE CONDENSATEUR (p.12) : 1 Définition et exemples (1.1 Définition et
symbole ; 1.2 Exemples de condensateurs usuels) · 2 Charge et décharge d'un condensateur (p.13–14) ·
3 Charge d'un condensateur et intensité du courant (p.14–15 ; 3.1 Caractère algébrique de l'intensité ;
3.2 Charge q d'un condensateur ; 3.3 Relation entre i et q) · 4 Relation entre la charge q et la tension u_C
(p.15–17) · 5 Capacité d'un condensateur plan (p.18) · 6 Tension de service et tension de claquage (p.19) ·
7 Énergie emmagasinée par un condensateur (p.19–20 ; 7.1 réservoir d'énergie ; 7.2 expression).
LE DIPÔLE RC (p.21) : 1 Réponse d'un dipôle RC à un échelon de tension (1.1 Étude expérimentale ;
1.2 Étude théorique, p.22–24) · 2 Décharge d'un condensateur dans un résistor (p.24–26) · 3 Influence des
grandeurs caractéristiques d'un dipôle RC sur la durée de charge ou de décharge (p.26–30 ; 3.1 Influence de
R ; 3.2 Influence de C ; 3.3 Constante de temps, avec « Récapitulation »).

### Cours — Activités

- **Intro historique (p.12, VERBATIM)** : « Le condensateur est un terme introduit en 1782 par Volta (
  physicien italien, 1745-1827) après avoir constaté que l'électricité “se condense” sur les surfaces en
  regard de deux conducteurs quand on les approche l'un de l'autre. »
- **§1.2 Exemples (p.12)** : Fig.2 photo ; condensateurs à air ; à diélectrique solide (feuilles métalliques
  minces roulées, forme cylindrique) ; électrochimiques (armatures en aluminium, diélectrique = mince
  couche d'alumine déposée par électrolyse). Diélectriques cités en 1.1 : air, papier imbibé d'huile de
  paraffine, céramique (oxyde de titane et titanates), mica, téflon, polyéthène, alumine.
- **§2 Manipulation charge/décharge (p.13–14)** : Fig.3 générateur E, galvanomètre balistique G, résistor R,
  commutateur K (1 : E–condensateur–G ; 2 : condensateur–R–G, R dans la seule branche 2 d'après le schéma) ;
  K en 2 d'abord → rien ; K en 1 → déviation α sens (1) puis retour à zéro ; rouvrir/refermer → rien
  (« chargé ») ; K en 2 → même α sens (2), retour lent (Fig.4a/4b, flèches e⁻ et i opposées) ; questions
  1°) « Peut-on décharger un condensateur non chargé ? […] » 2°) « Expliquer les phénomènes de charge et de
  décharge […] et en déduire si l'on peut recharger un condensateur déchargé. » ; interprétation par
  déplacement d'électrons (A → pôle +, pôle − → B ; +q sur A, −q sur B ; V_A − V_B = tension du générateur ;
  en 2, électrons de B vers A à travers le résistor). Conclusion : voir Encadrés.
- **§3.1 Manipulation caractère algébrique de i (p.14–15)** : Fig.5 générateur idéal E, R, condensateur, K,
  DEL D1 et D2 tête-bêche, voltmètre, entrée Y sur u_R ; enregistrement de u_R (oscilloscope à mémoire ou
  acquisition) K en 1 puis 2 (Fig.6 : u_R > 0 décroissant, puis u_R < 0 croissant vers 0) ; questions
  1°) D1 seule en position 1, D2 seule en 2 ; 2°) « Sachant que u_R=Ri, montrer graphiquement qu [sic] i est
  positive et décroissante pendant la charge, négative et croissante pendant la décharge. »
- **§4 Manipulation charge à courant constant (p.15–17)** : Fig.8 générateur de courant, K1, ampèremètre,
  condensateur (armatures A, B) en série ; voltmètre numérique et K2 aux bornes ; « q = I.t » ; fermer puis
  rouvrir K2 ; fermer K1 et chronométrer ; u_C mesurée « toutes les 5 secondes […] **en convention
  récepteur** » ; I = 0,144 mA ; tableau t (s) 0 / 5 / 10 / 15 / 20 / 25 / 30 — u_C (V) 0 / 1,5 / 3 / 4,6 /
  6,1 / 7,6 / 9,2 ; questions 1°) fermeture de K2 et indication du voltmètre ; 2°) tension non nulle avant
  K2 ; 3°) q augmente avec u_C ; 4°) Fig.9 (droite par l'origine, sans graduations chiffrées) « Montrer
  graphiquement que u_C = kt où k est une constante que l'on calculera » ; 5°) relation q–u_C.
  Interprétation : « u_C = kt avec k = 0,3 V.s⁻¹ » ; u_C = k q/I d'où q = (I/k) u_C ; I/k constante notée C.
  (Valeur numérique de C non calculée par le manuel.)
- **§6 Question d'entrée (p.19, VERBATIM)** : « En plus de la valeur de la capacité du condensateur, le
  constructeur indique généralement sur le boitier deux valeurs différentes de tensions électriques, que
  représentent-elles? » ; texte sur l'étincelle, le diélectrique troué, le crépitement, « le condensateur a
  claqué ».
- **§7.1 Expérience complémentaire (p.20)** : Fig.11 générateur de tension continue E réglable,
  condensateur de très grande capacité C, petit moteur M, commutateur K ; K en 1 puis 2 → le moteur tourne
  puis s'arrête ; questions 1°) ce qui montre le réservoir d'énergie ; 2°) l'opération qui l'a « rempli » ;
  3°) petite durée de rotation.
- **RC, intro (p.21, VERBATIM)** : « Le dipôle RC est constitué d'un résistor de résistance R associé en
  série avec un condensateur de capacité C. On se propose d'étudier la variation de la charge q du
  condensateur en fonction du temps dans un tel dipôle lorsque la tension à ses bornes passe brusquement de
  zéro à une valeur constante E ou inversement. L'évolution brusque de la tension constitue l'échelon de
  tension. »
- **RC §1.1 Manipulation échelon (p.21)** : Fig.12 C, R, générateur E en série, K (1/2) ; Fig.13 points D,
  A, B (masse en B), Y1 en D, Y2 en A, flèches u_DA, u_AB ; oscilloscope numérique à mémoire ; K en 1 →
  Fig.14 (une courbe croissante avec palier visible) ; questions 1°) identifier les voies Y1/Y2 ; 2°) charge
  instantanée ? ; interprétation u_DB = E, u_AB croît jusqu'à E, q = C u_AB.
- **RC §1.2 (p.22–24)** : Fig.15 circuit de charge ; mise en équation « En convention récepteur » ;
  Remarque p.23 : GBF en créneaux à la place du générateur continu en l'absence d'oscilloscope à mémoire ;
  visualisation simultanée u_C(t) et i(t) (Fig.19–20) : générateur à **masse flottante** (ou via
  transformateur d'isolement), masse en A, Y1 : u_DA = Ri, Y2 : u_AB « au lieu de u_BA et ce, en appuyant
  sur le bouton INV » ; Question p.24 : montrer que (1) = u_DA et (2) = u_AB.
- **RC §2.1 Manipulation décharge (p.24)** : montage Fig.13, condensateur chargé, K en 2 ; Y2 → Fig.21
  (u_C décroissant) ; questions 1°) allure de u_C(t) ; 2°) décharge instantanée ? ; interprétation :
  énergie progressivement dissipée dans le résistor.
- **RC §2.2 Remarque (p.26)** : visualisation simultanée en décharge (Fig.26–27), note marginale « Pour que
  l'opération soit possible, le générateur doit être à masse flottante. » ; (1) = u_DA devenue négative,
  (2) = u_AB (u_BA changée de signe) positive décroissante.
- **RC §3.1 Manipulation influence de R (p.26–27)** : Fig.28, B à la masse, A sur Y1 (u_C), D sur Y2 (u_DB) ;
  E = 6 V ; C = 1 μF ; R1 = 5 kΩ, R2 = 10 kΩ, R3 = 15 kΩ, R4 = 20 kΩ ; 5 ms/div, 1 V/div ; Fig.29a–d ;
  questions 1°) tableau R (kΩ) 5 / 10 / 15 / 20 — t (ms) pour u_C = 4 V (vide) ; 2°) influence qualitative ;
  t proportionnelle à R.
- **RC §3.2 Manipulation influence de C (p.28)** : R = 10 kΩ ; C1 = 0,5 μF, C2 = 2 μF, C3 = 5 μF,
  C4 = 10 μF ; 1 V/div ; 5 ms/div (Fig.30a, b) et 50 ms/div (Fig.30c, d) ; même tableau (C (μF) 0,5 / 2 /
  5 / 10) ; t proportionnelle à C ; Remarque : mêmes résultats en décharge.
- **RC §3.3 (p.28–30)** : notion de constante de temps (proportionnalité à RC, analyse dimensionnelle) ;
  Question p.28 : « Tant au cours de la charge qu'au cours de la décharge, u_C(t) est une fonction
  exponentielle du temps d'exposant (- t/τ). En déduire que τ =RC ne peut avoir effectivement que la
  dimension d'un temps. » ; Question p.30 : tangente à i(t) → t = τ (Fig.35a, 35b) ; Question p.30 :
  « Montrer que les mêmes durées 4,6 τ et 6,9 τ sont indispensables pour décharger complètement un
  condensateur respectivement à 1 % et à 1 ‰ près. »

**Total : 11 activités/manipulations à questions** (§2, §3.1, §4, §6, §7.1, RC §1.1, RC §1.2-visualisation,
RC §2.1, RC §3.1, RC §3.2, RC §3.3-questions).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Définition (1.1, p.12)** — « Un condensateur est un composant électrique constitué de deux plaques
> conductrices trés [sic] faiblement espacées et séparées par un isolant électrique. Les plaques sont
> désignées par les armatures du condensateur et le matériau isolant est appelé diélectrique. Le
> condensateur est symboliquement représenté par deux traits parallèles qui représentent les armatures
> (Fig.1). » […] « Étant un dipôle électrocinétique, le condensateur a deux bornes reliées directement à ses
> armatures. Dans le cas où les armatres [sic] sont planes et parallèles, le condensateur est dit plan. »

> **Conclusion (§2, p.14)** — « Le condensateur est un composant électrique capable de stocker des charges
> électriques. »

> **Conclusion (§3.1, p.15)** — « L'intensité du courant électrique est une grandeur algébrique. Elle est
> positive si le courant circule dans le sens arbitraire choisi et négative si le courant circule dans le
> sens contraire. »

> **Définition (§3.2, p.15)** — « On appelle charge q d'un condensateur, la charge de l'une de ses armatures
> choisie conventionnellement, celle vers laquelle est orienté le sens positif du courant. » Note marginale :
> « Ne pas confondre entre la charge q d'un condensateur et le phénomène de charge ».

> **Relation i–q (§3.3, p.15)** — « Entre les instants t et t+Δt le courant circulant dans le sens positif,
> transporte la quantité d'électricité Δq>0, ce qui fait augmenter la charge de l'armature A de Δq.
> L'intensité du courant étant la quantité d'électricité transportée (ou traversant une section droite) par
> unité de temps, on a : » **i(t) = lim_{Δt→0} Δq/Δt = dq/dt**

> **(§4, p.17, encadré)** — « On a ainsi : **q = C u_C** »

> **Capacité (p.17)** — « La charge q d'un condensateur est proportionnelle à la tension u_C à ses bornes :
> q = C u_C. Le facteur de proportionnalité C est une grandeur qui caractérise l'aptitude du condensateur à
> emmagasiner une charge électrique q lorsqu'il est soumis à une tension u_C, appelée capacité du
> condensateur. C ne dépend que des caractéristiques géométriques du condensateur et de la nature du
> diélectrique. »

> **Unité (p.17)** — « La capacité C d'un condensateur est une grandeur mesurable. Dans le système
> international d'unités, elle s'exprime en Farad (F). Le farad est la capacité d'un condensateur qui, soumis
> à une différence de potentiel de 1 V, prend une charge de 1 C. » « […] le farad est une grande unité de
> capacité. » « 1 mF = 10⁻³ F ; 1 μF = 10⁻⁶ F ; 1 nF = 10⁻⁹ F ; 1 pF = 10⁻¹² F ; 1 fF = 10⁻¹⁵ F ». Note :
> Michael Faraday (physicien et chimiste anglais, 1791-1867). Tableau « Type du condensateur / Ordre de
> grandeur de C » : électrochimique μF - F ; au mica, céramique pF - nF ; au papier μF ; au tantale
> 0,1 μF - 0,01 μF ; au polypropylène nF - μF.

> **Condensateur plan (§5, p.18)** — « La capacité d'un condensateur plan est proportionnelle à la surface S
> des armatures en regard et inversement proportionnelle à l'écartement e de ses armatures (Fig.10). On peut
> écrire : » **C = ε S/e** « Le facteur de proportinnalité [sic] ε est une constante qui ne dépend que de la
> nature du diélectrique, on l'appelle permittivité absolue du diélectrique. Dans le système international
> d'unités, ε s'exprime en farads par mètre. La permittivité ε_o du vide est : » **ε_o = 1/(36π.10⁹)
> (F.m⁻¹)** « La permittivité de l'air est pratiquement égale à celle du vide. Tous les autres diélectriques
> ont une permittivité absolue plus-grande que celle du vide. » « […] permittivité relative ε_r d'un
> diélectrique comme étant le rapport de sa permittivité absolue sur la permittivité du vide : »
> **ε_r = ε/ε₀ d'où C = ε_r ε_o S/e**. Tableau (ε_r ; ε en 10⁻¹¹ F.m⁻¹) : Vide, air 1 ; 0,885 · Papier
> paraffiné 2 - 2,5 ; 1,8 - 2,2 · Polystyrène 2 - 3 ; 1,8 -2,7 · Verre 4 - 7 ; 3,5 - 6,2 · Mica 5 - 8 ;
> 4,4 - 7,1 · Céramique 15 - 2500 ; 13,2 - 2200.

> **Définition (§6, p.19)** — « On appelle tension de claquage d'un condensateur la plus petite tension (en
> valeur absolue) faisant jaillir une étincelle entre les armatures du condensateur. » · « La deuxième
> valeur de tension indiquée sur le boitier d'un condensateur est appelée tension de service, elle est d'une
> valeur nettement inférieure à celle de claquage, c'est la tension nominale du composant. »

> **Conclusion (§7.1, p.20)** — « Le condensateur est un réservoir d'énergie potentielle électrique (ou
> électrostatique). Cette énergie se manifeste, lors de la décharge du condensateur, en se transformant en
> énergie thermique dans les différents conducteurs, en énergie cinétique dans un moteur, en énergie
> lumineuse dans une diode LED par exemple... »

> **Énergie (§7.2, p.20)** — « L'énergie électrostatique emmagasinée par un condensateur de capacité C,
> chargé sous une tension u, s'exprime par : » **E_C = ½ C u²** « Avec C en farad et u en volt, E_C
> s'exprime en joule. En utilisant la relation q = C.u, on obtient d'autres expressions de E_C soit : »
> **E_C = q²/(2C) = ½ q u** (donnée, non démontrée).

> **Conclusion (RC §1.1, p.21)** — « La réponse d'un dipôle RC à un échelon de tension est la charge du
> condensateur. N'étant pas instantanée, celle-ci constitue un phénomène transitoire. »

> **Mise en équation — charge (p.22)** — « En régime transitoire et pendant que le condensateur se charge,
> le circuit de la figure 12 est équivalent à celui de la figure 15. **En convention récepteur**, la loi des
> mailles s'écrit pour ce circuit : u_DA + u_AB − E = 0, soit : Ri + u_C − E = 0. Or, i = dq/dt =
> C du_C/dt, d'où : **u_C + RC du_C/dt = E (1)** ou bien : **du_C/dt + (1/τ) u_C = E/τ avec τ = RC**,
> équation différentielle en u_C avec second membre non nul. Avec u_C = q/C et i = dq/dt, la même équation
> différentielle s'écrit : **dq/dt + (1/τ) q = E/R (2)** ou **i + (1/τ) ∫ i dt = E/R (3).** »

> **u_C(t) — charge (p.22)** — « La solution de l'équation différentielle (1) est de la forme :
> u_C(t) = B + Ae^{−αt} où A, B et α sont des constantes à déterminer. A t = 0, u_C = A + B = 0, d'où
> B = − A. Il vient u_C(t) = A(e^{−αt} − 1). La dérivée de u_C(t) par rapport au temps s'écrit :
> du_C/dt = − αAe^{−αt}. En remplaçant du_C/dt par son expression dans l'équation (1), on trouve :
> A(e^{−αt} − 1) − ατAe^{−αt} = E ; ce qui donne : − A + (1 − ατ)Ae^{−αt} = E. En égalisant membre à membre
> cette équation qui doit être satisfaite pour toute valeur de t, on obtient : A = − E et 1 − ατ = 0 d'où
> α = 1/τ. Ainsi, avec A = − E et α = 1/τ, la tension aux bornes du condensateur s'écrit :
> **u_C(t) = E(1 − e^{−t/τ})**. » (Fig.16.)

> **q(t) et i(t) — charge (p.23)** — « **q(t) = Q₀(1 − e^{−t/τ}) avec Q_o = CE.** » « Lorsque t tend vers
> l'infini u_C(t) tend vers E et q vers q_o, le condensateur porte sa charge maximale. » · « On a i = dq/dt.
> En remplaçant q par son expression, on trouve i(t) = (Q_o/τ) e^{−t/τ} ou encore : **i(t) = I_o e^{−t/τ}
> avec I_o = E/R** » ; « L'intensité i du courant est alors positive au cours de la charge du condensateur,
> résultat attendu du fait que le sens positif du courant est orienté vers l'armature située dans le circuit
> du côté du pôle positif du générateur. » (Fig.17, Fig.18.)

> **Conclusion (RC §2.1, p.24)** — « Dans un dipôle RC, un condensateur chargé se décharge progressivement
> dans le résistor. »

> **Mise en équation — décharge (p.24–25)** — « Le condensateur étant initialement chargé, à l'instant
> t = 0, la tension à ses bornes est égale à E. Le circuit est équivalent à celui de la figure 22. Avec
> l'orientation choisie pour le circuit, on peut écrire : u_C + u_R = 0 et u_R = Ri d'où u_C + Ri = 0. Or,
> i = dq/dt et q = Cu_C, on aura : **u_C + RC du_C/dt = 0** ou bien **du_C/dt + (1/τ) u_C = 0 (4).** On
> obtient une équation différentielle en u_C sans second membre. On obtient aussi les équations
> différentielles (5) et (6) respectivement en q et en i : **dq/dt + (1/τ) q = 0 (5) ; i + (1/τ) ∫ i dt = 0
> (6).** »

> **u_C(t), q(t), i(t) — décharge (p.25–26)** — « La solution de l'équation différentielle (4) est de la
> forme : u_C(t) = A e^{−αt} où les constantes A et α sont déterminées par les conditions initiales : A
> t = 0, u_C = E, d'où A = E. […] on obtient : − α A e^{−αt} + (1/τ) A e^{−αt} = 0, ce qui entraine :
> (− α + 1/τ)A e^{−αt} = 0 ∀t. D'où − α + 1/τ = 0, ce qui donne : α = 1/τ. Il vient finalement :
> **u_C(t) = E e^{−t/τ}** » · « **q(t) = Q_o e^{−t/τ} avec Q_o = CE** » ; « Lorsque t tend vers l'infini, q
> tend vers zéro ; le condensateur est déchargé. » · « On a : i = dq/dt, donc : i(t) = − (E/R) e^{−t/τ} ou
> encore : **i(t) = − I_o e^{−t/τ} avec I_o = E/R** » ; « On note bien pour i(t) le signe contraire de celui
> de l'intensité du courant de charge, c'est à dire que le courant de décharge circule dans le sens contraire
> de celui de charge (Fig.25). »

> **Constante de temps (p.28, encadré)** — « **τ = RC : constante de temps** » · **Définition (p.29)** —
> « La constante de temps τ est une grandeur caractéristique du dipôle RC, elle renseigne sur la rapidité
> avec laquelle s'établit la tension u_C = E entre les armatures du condensateur. La charge et la décharge du
> condensateur sont d'autant plus rapides que la constatnte [sic] de temps τ est plus petite. »

> **Détermination de τ (p.29–30)** — « Par calcul direct […] τ = RC. » · « Détermination graphique (première
> méthode) : Pour déterminer τ, on trace la tangente à la courbe de charge ou de décharge u_C(t) au point
> d'abscisse t = 0. Cette tangente a pour équation u_C = a t, a étant son coefficient directeur dont la valeur
> est donnée par : a = (du_C/dt)_{t=0}. Or : du_C/dt = (E/τ) e^{−t/τ}, alors (du_C/dt)_{t=0} = E/τ.
> Finalement, l'équation de la tangente s'écrit : u_C = E t/τ. L'intersection de cette tangente avec la
> droite u_C = E donne t = τ (fig.31). » Remarque : décharge → intersection de la tangente à l'origine avec
> l'axe des abscisses (fig.32). · « Détermination graphique (deuxième méthode) : […] u_C = E(1-e⁻¹) =
> 0,63 E. […] τ correspond donc au temps nécessaire pour charger un condensateur à 63%. Dans le cas de la
> décharge, […] u_C = E e⁻¹ = 0,37E. » (Fig.33, 34.) Remarque : tangente à i(t) en t = 0 (Fig.35a : depuis
> I_o ; Fig.35b : depuis −I_o).

> **Intérêt pratique de τ (p.30)** — « On admet alors que le condensateur est complètement chargé ou
> déchargé quand la différence relative entre la valeur atteinte par u_C et la valeur asymptotique E (pour la
> charge) ou zéro (pour la décharge) ne dépasse pas 1%. Pour la charge par exemple : (E − u_C)/E ≤ 1% ce qui
> signifie que E − u_C ≤ 0,01 E d'où u_C ≥ 0,99 E. […] e^{−t/τ} = 0,01, d'où Log e^{−t/τ} = Log 0,01 ou
> bien t_c/τ = 2Log10 = 4,6, d'où **t_c ≃ 5 τ**. Quand l'étude se veut plus précise, on exige une erreur
> relative ne dépassant pas 1 ‰. Avec un calcul semblable au précédent, on aboutit à t_c = 6,9 τ ≃ 7 τ pour
> avoir u_C = 0,999 E. » **Récapitulation (tableau)** — Durée t : 0 | τ | 4,6 τ | 6,9 τ — Charge u_C : 0 |
> 0,63 E | 0,99 E | 0,999 E — Décharge u_C : E | 0,37 E | 0,01 E | 0,001 E.

**L'essentiel (p.31, VERBATIM, lu sur l'image)** — « ■ Un condensateur est un ensemble de deux plaques
conductrices séparées par un isolant. Il se charge lorsqu'on établit entre ses bornes une tension continue
et se décharge lorsqu'on le ferme sur un récepteur. ■ En désignant par q la charge portée par l'armature du
condensateur vers laquelle est orienté le sens positif du courant, on a : **i = dq/dt** ■ La capacité C est
une grandeur mesurable caractérisant la faculté d'un condensateur à stocker une charge q sous une tension
u : **q = C.u** ■ La capacité C d'un condensateur plan est proportionnelle à la surface S en regard des
armatures et inversement proportionnelle à la distance e qui les sépare : **C = e S/e** [sic : lire
C = ε S/e] où ε est la permittivité absolue du diélectrique. ■ Sous une tension u, un condensateur de
capacité C emmagasine une énergie potentielle électrique : **E_C = ½ C u²** ■ Toute décharge d'un
condensateur s'explique par une restitution d'énergie emmagasinée. ■ Un dipôle RC soumis à un échelon de
tension E répond par une évolution de la tension u_C aux bornes du condensateur régie par la loi :
**u_C(t) = E(1 − e^{−t/t})** [sic : exposant imprimé « t/t », lire −t/τ] où τ = RC est la constante de
temps du dipôle. ■ Quand un dipôle RC chargé est fermé sur lui même, la tension u_C aux bornes du
condensateur, initialement égale à E, évolue selon la loi : **u_C(t) = E e^{−t/t}** [sic : lire −t/τ] ■ La
constante de temps τ = RC renseigne sur la rapidité de la charge et de la décharge du condensateur. »

### Exercices résolus

- **Exercice résolu (p.32–33)** — Énoncé : Fig.1 générateur E, R1, commutateur K (1 : charge à travers R1 ;
  2 : décharge dans R2), condensateur C ; ordinateur + capteur + interface. 1°) K en 1 → Fig.2 (u_C de 0 à
  6 V, t de 0 à 0,8 s) : a) interpréter l'allure ; b) déterminer graphiquement le temps de charge (chargé
  quand u_C = E à 1 % près). 2°) K en 2, décharge complète dans R2 = 1 kΩ au bout de t = 250 ms, Fig.3 (u_C
  depuis 6 V, t de 0 à 200 ms) : a) interpréter ; b) τ2 graphiquement et C. 3°) R1. Démarche : loi des
  mailles u_C + u_R1 − E = 0 → τ1 du_C/dt + u_C = E, τ1 = R1C ; u_C = E(1 − e^{−t/τ1}) ; θ : u_C(θ) = 0,99 E
  → θ/τ1 = 2 log10, θ = 4,6 τ1 ≃ 5 τ1 ; tangente à l'origine, intersection P avec l'asymptote → **τ1 = 0,1 s,
  θ = 0,5 s** ; décharge : u_C + u_R2 = 0, τ2 du_C/dt + u_C = 0, **τ2 = R2C** (imprimé correctement ici),
  u_C = E.e^{−t/τ2} ; tangente → **τ2 = 50 ms**, C = τ2/R2 = **50 μF** ; R1 = τ1/C = **2 kΩ**.

### Tests rapides des acquis

- **Ex. 1 — « vrai ou faux » (p.34)** : 1. chargé sous U → q = CU ; 2. caractérisé par sa capacité ; 3. « ne
  restitue jamais la même quantité d'énergie emmagasinée » ; 4. i = dq/dt ; 5. pendant la charge d'un
  condensateur initialement déchargé, i maximale au début et nulle à la fin ; 6. intensité maximale du
  courant de charge = E/R ; 7. au début de la décharge, i nulle ; 8. τ : tangente à l'origine à la courbe de
  décharge u_C(t) en t = 0 et coordonnées de son intersection avec l'axe des abscisses ; 9. « Un
  condensateur de charge 2q emmagasine l'énergie : E_C = q²/2C ».
- **Ex. 2 — QCM (p.34)** : I. 5 s à I = 1,2 mA → Q = a- 8.10⁻³ C / b- 6.10⁻³ C / c- 5.10⁻³ C ; II. q
  quadruplée quand : a- tension 2 fois plus grande / b- tension 4 fois plus grande / c- capacité 4 fois plus
  petite ; III. C = 10 μF, τ = 2 ms → R = a- 20 Ω / b- 200 Ω / c- 2000 Ω ; IV. τ = durée au bout de laquelle le
  condensateur est a- complètement chargé / b- à moitié chargé / c- chargé à 63 % ; V. ralentir la décharge
  (R réglable) : a- diminuer R / b- augmenter la constante de temps tout en augmentant R / c- diminuer la
  constante de temps tout en diminuant R ; VI. énergie (charge q) doublée quand on double a- la charge q /
  b- sa capacité C / c- la tension u.

### Exercices et problèmes

Exercices d'application (p.35) :
- **Ex. 3** : condensateur plan, deux feuilles d'aluminium, S = 1 m², ε_r = 8, e = 0,1 mm. 1°) C ; 2°) énergie
  sous 50 V.
- **Ex. 4** : C = 20 μF initialement non chargé, générateur de courant I = 1,8 μA. 1°) q après 10 s ;
  2°) a) u_AB à t = 10 s ; b) énergie à t = 10 s.
- **Ex. 5** : C = 3 μF, R = 80 kΩ, E = 12 V. 1°) τ ; 2°) a) u_C après 2 s ; b) i après 2 s.
- **Ex. 6** : E = 6 V, C = 2 μF, R = 10 kΩ, K. 1°) i à la fermeture ; 2°) τ ; 3°) durée pour u_C = 0,99 E ;
  4°) allure de u_C(t).
- **Ex. 7** : acquisition [« L'aquisition » sic], R = 100 Ω, K, E = 5 V ; tableau t (μs) 0 ; 0,5 ; 1 ; 1,5 ;
  2 ; 3 ; 4 ; 5 — u_C (V) 0 ; 2,2 ; 3,3 ; 4 ; 4,3 ; 4,7 ; 4,8 ; 4,9. 1°) schéma ; 2°) graphe ; 3°) τ ;
  4°) C.
- **Ex. 8** : **0,12 dq/dt + q = 12.10⁻⁵** (exposant −5 lu sur l'image). 1°) τ ; 2°) E = 12 V → R ; 3°) C.
Exercices de synthèse (p.35–37) :
- **Ex. 9** : E, R, C = 10 μF en série. 1°) schéma et connexions d'un oscilloscope numérique pour u_C(t) et
  u_R(t) ; 2°) identifier « Courbe (a) » (croissante vers 12 V) et « Courbe (b) » (décroissante depuis 12 V)
  — u (V) 0–12, t (ms) 0–400 ; 3°) E et τ ; 4°) R.
- **Ex. 10** : C = 22 μF, alimentation stabilisée E = 6 V, R = 1 kΩ, condensateur déchargé, K fermé à t = 0
  (schéma : générateur N, P ; K ; D–C–B–R–A). 1°) q = charge de l'armature B : sens positif pour i = dq/dt ;
  2°) équation différentielle en q(t) ; 3°) q(t) = α.(1 − e^{−t/β}) : a) α et β littéraux et numériques ;
  b) i(t) ; 4°) a) t_{1/2} où q = ½.C.E, comparer à τ ; b) instant où q = CE/4.
- **Ex. 11** : C et R en série, K (1 : générateur E ; 2 : décharge), points A, B, G, interface + ordinateur ;
  K en 1 depuis longtemps ; courbe u (V) décroissant depuis 5 V, t (ms) 0–80. 1°) état du condensateur à
  t = 0 (K en 2) ; 2°) à quoi correspond la courbe ; 3°) manipulation ; 4°) signe de i en décharge ;
  5°) relations i–u_BG, q_A–u_AB, i–q_A, u_BG–u_AB ; 6°) montrer (1/α) du_AB/dt + U_AB = 0 [U majuscule, sic],
  α à exprimer.
- **Ex. 12** : C = 5 μF chargé sous u_AB = U_o > 0 ; 2,5 ms/div et 2 V/div ; 1°) équation différentielle en
  u_AB ; 2°) R1 = 500 Ω → courbe 1, R2 → courbe 2 (graphe gradué sans valeurs) : a) U_o ; b) résistance la
  plus grande, méthode et calcul de R2 ; 3°) a) énergie emmagasinée ; b) énergie E1 dissipée par effet Joule
  dans R1 ; c) E1 varie-t-elle si R1 → R2 ?
- **Ex. 13 — Étude de texte « Le défibrillateur cardiaque »** : « circuit à choc exponentiel tronqué »,
  C = 32.10⁻⁶ F, U ≈ 5 kV, libération en une dizaine de millisecondes, thorax ≈ 75 ohms (adulte). 1°) circuit
  RC ; 2°) τ ; 3°) ordre de grandeur de l'énergie ; 4°) expliquer l'expression.

**Total : 13 exercices** (2 tests rapides, 6 d'application, 5 de synthèse) + 1 exercice résolu.

### Réponses du manuel (p.392, colonne « Chapitre 1 », lue sur l'image)

Ex. 3 : 1°) 0.7 μF, 2°) 8.8 10⁻³ J [? recalcul ½·0,708·10⁻⁶·50² ≈ 8,8·10⁻⁴ J] · Ex. 4 : 1°) 18 μc [sic, μC],
2°) a) 0.9 V, b) 8.1 10⁻⁶ J · Ex. 5 : 1°) 0.24 s, 2°) a) 12 V, b) 3.6 10⁻⁸ A · Ex. 6 : 1°) 6 10⁻⁴ A,
2°) 20 ms, « 2°) » [sic, lire 3°)] 92 ms · Ex. 7 : « 2°) » [sic, lire 3°)] 1 μs, 4°) 10⁻⁸ F · Ex. 8 :
1°) 0.12 s, 2°) 12 kΩ, « 2°) » [sic, lire 3°)] 10 μF · Ex. 9 : 2°) [lire 3°)] 12 V, 150 ms, 4°) 15 kΩ.
Pas de réponse pour Ex. 1, 2, 10–13.

### En savoir plus / Documents

- **Fiche technique (p.38–39)** « Mesure d'une tension continue aux bornes d'un condensateur » : 1. voltmètre
  (R_v ; numérique ≈ 10 MΩ ; à aiguille ≈ 20 kΩ par volt, 200 kΩ sur le calibre 10 V ; C = 5600 µF,
  R_v = 10 MΩ → 56000 s ; suiveur TL081 ≈ 10¹² Ω, C = 10 nF → 10⁴ s ; suiveur 741 ≈ 1 MΩ) ; 2. oscilloscope
  à mémoire (impédance d'entrée 1 MΩ, 50 pF ; R = 20 kΩ, C = 125 nF ; u = R_osc/(R + R_osc)·E(1 − e^{−t/τ})
  avec τ = R·R_osc/(R + R_osc)·C ; erreur 2 % ; R_oscC = 125 ms ; montage de droite u_C = E − u_R), deux
  schémas (Y1 sur u_C ; Y1 sur u_R). « D'après web.ac-reims.fr/datice/sc_physiques/docs/lyc/T/RC.doc ».
- **En savoir plus (p.40–41)** « La foudre et les paratonnerres » : nuage–Terre « seconde plaque d'un
  énorme condensateur », ionisation vers 10 000 V par cm, précautions, paratonnerres, effets positifs
  (azote). « D'après Encarta 2006 ».

### Écart avec la référence (sciences-exp/01 — correspondance CONFIRMÉE)

Contenu identique à 223433 ch1 (mêmes pages 10–41, mêmes figures, mêmes 13 exercices et mêmes réponses).
- ⛔ À retirer : **rien** au titre des notions. Seule nuance d'objectif : la référence vise τ « à partir des
  courbes de réponse u_C(t) ou i(t) » ; ici « Déterminer graphiquement la constante de temps τ = RC d'un
  dipôle RC » (le cours enseigne pourtant la tangente à i(t), p.29–30 : rien à retirer).
- ✅ À ajouter / autrement : **conventions récepteur et générateur** explicitement en prérequis (p.10, savoir
  et savoir-faire) et invoquées dans le cours (« mesure […] u_C en convention récepteur », p.16 ; « En
  convention récepteur, la loi des mailles s'écrit », p.22) — une phrase de rappel suffit dans le cours
  adapté.
- Vocabulaire/notations : identiques (« Log » népérien, Q_o, I_o, « résistor »). Thème nommé « Évolution de
  systèmes électriques ».
- Coquille de la référence absente ici : l'exercice résolu porte bien « τ2 = R2C » (p.33) ; à l'inverse,
  l'Essentiel imprime l'exposant « −t/t » (p.31).

### Bornes de scope

- ✅ **INCLUS** : identiques aux bornes de sciences-exp/01 — condensateur (définition, symbole, plan, types
  usuels, ordres de grandeur) ; charge/décharge qualitatives (galvanomètre balistique) ; intensité
  algébrique, charge q d'un condensateur, **i = dq/dt** ; charge à courant constant, **q = C u_C**, farad et
  sous-multiples ; **C = εS/e**, ε₀ = 1/(36π·10⁹) F.m⁻¹, ε_r ; tensions de claquage et de service ;
  **E_C = ½Cu² = q²/2C = ½qu** (donnée) ; dipôle RC : échelon, équations différentielles en u_C, q, i (forme
  ∫ i dt), solution imposée B + Ae^{−αt} / Ae^{−αt} ; u_C(t), q(t), i(t) en charge et en décharge (signe de
  i) ; oscilloscope à mémoire, masse flottante, bouton INV, GBF créneaux (mention) ; influence de R et de C ;
  **τ = RC** (dimension, calcul, tangente à l'origine sur u_C et sur i, 0,63 E / 0,37 E, 4,6 τ ≃ 5 τ à 1 %,
  6,9 τ ≃ 7 τ à 1 ‰) ; conventions récepteur/générateur (rappel).
- ⛔ **EXCLU** : associations de condensateurs ; champ électrique, démonstration de C = εS/e et de E_C ;
  résolution par séparation des variables, notation « ln » ; réponse quantitative à un signal créneau ;
  régime sinusoïdal ; influence de E ; demi-vie comme résultat de cours (exercice 10 seulement) ; fiche
  technique (non exigible) ; foudre (lecture).

### Lecture

- **Pages lues en L1** : 9–41 (toutes) et 392 (réponses).
- **Pages lues sur l'image (110 dpi)** : 10, 11, 13, 15, 16, 17, 18, 20, 22, 23, 25, 26, 27, 28, 29, 30,
  31, 32, 33, 34, 35, 36, 37, 39 (24 pages) + 392 (160 dpi). **Non vues sur l'image** (rendu refusé par
  l'outil, limite de requêtes) : 12, 14, 19, 21, 24 (prose + schémas simples ; aucune formule encadrée
  exploitée hors couche texte, sauf le symbole Fig.1 et les Fig.5/6, 12–14, 21 décrites d'après la couche
  texte et, pour leur contenu, d'après la fiche 223433 au texte identique — à revérifier si une figure de
  ces pages est reprise), 38, 40, 41 (prose : fiche technique p.38, foudre), 9 (garde de thème).
- **Relecture R-7 (2026-11-07)** : les pages d'abord non vues sur l'image (ch.1 : p.12, 14, 19, 21, 24, 38, 40, 41) ont été vues sur l'image par l'auditeur indépendant et sont conformes au texte transcrit.
- **Écarts texte/image** : p.15 encadré i = lim Δq/Δt = dq/dt absent du texte ; p.18 ε, ε₀, ε_r, π perdus ;
  p.20 fractions et carrés de E_C éclatés ; p.22, p.25 α, τ, ∫, ∀ perdus ; p.29 (du_C/dt)_{t=0} illisible ;
  p.30 ≤, ≥ perdus, « ≃ » rendu « b », « 1 ‰ » rendu « 1o/oo » ; p.31 ε rendu « e » (fidèle : coquille réelle)
  et τ rendu « t » (fidèle) ; p.33 τ1, τ2, θ perdus ; p.35 « 12.10⁵ » au lieu de **12.10⁻⁵** ; p.36 CE/4
  éclaté ; p.37 α perdu (ex. 11 6°) ; p.392 colonnes ch1/ch2 entremêlées.
- **Coquilles [sic]** : « flasch » (p.11) ; « trés », « armatres » (p.12) ; « qu i » (p.14) ;
  « proportinnalité », « plus-grande » (p.18) ; « aqcuisition » (p.23) ; « constatnte » (p.29) ; « Interêt »
  (p.30) ; « C = e S/e » et exposant « −t/t » (p.31) ; « L'aquisition » (ex. 7) ; « interrrupteur » (ex. 11) ;
  « résistane », « difibrillateur », « d'élètères » (ex. 13) ; réponses p.392 : « μc », numéros « 2°) » au lieu
  de « 3°) » (ex. 6, 7, 8, 9).
- **Doutes [?]** : (1) réponse ex. 3 2°) « 8.8 10⁻³ J » vs recalcul 8,8·10⁻⁴ J (même doute que la
  référence) ; (2) Fig.25 (p.26) : l'ordonnée de départ de i(t) est étiquetée « I_o » sans signe moins alors
  que la courbe part sous l'axe (lire −I_o, cf. Fig.35b « −I_o ») ; (3) ex. 12 : graphe sans valeurs, U_o non
  lisible avec certitude ; (4) ex. 11 6°) « U_AB » majuscule ; (5) tableaux §3.1/§3.2 laissés vides, C de la
  manipulation §4 non calculée.

## 2.2 Chapitre 2 — La bobine ; le dipôle RL (manuel 223471, p.42–77)

Bandeau : « Evolution de systèmes ◆ La bobine ; le dipôle RL » (p.56 : « Evolution de systèmes
électriques »). Deux parties titrées : « L'INDUCTION ÉLECTROMAGNÉTIQUE » (p.44–56, §1–6) et « LE DIPÔLE
RL » (p.57–66, §1–3), puis L'essentiel (p.67), Exercice résolu (p.68–70), Exercices à résoudre
(p.71–76), En savoir plus (p.77). Pas de fiche technique.

**Objectifs (p.42, VERBATIM, lu sur l'image)** — « Mettre en évidence expérimentalement le phénomène
d'induction électromagnétique. » · « Appliquer la loi de Lenz. » · « Reconnaître les facteurs dont dépend
la f.e.m. d'auto-induction. » · « Calculer l'énergie emmagasinée dans un solénoïde. » · « Établir, pour un
dipôle RL soumis à un échelon de tension, l'équation différentielle qui régit les variations de
l'intensité i du courant parcourant la bobine en fonction du temps. » · « Déterminer graphiquement la
constante de temps τ = L/R **à partir de la courbe u_L(t)** d'un dipôle RL. »

**Prérequis (p.42)** — SAVOIR : définir un champ magnétique, une ligne de champ magnétique, le vecteur
champ magnétique, un champ magnétique uniforme ; « Enumérer les caractéristiques d'un hamp [sic] magnétique
créé par un courant continu circulaire (solénoïde). » SAVOIR FAIRE : identifier les pôles d'un aimant et
les faces d'une bobine ; mettre en évidence expérimentalement l'existence d'un champ magnétique ;
déterminer les caractéristiques d'un vecteur champ magnétique ; reconnaître un champ magnétique uniforme à
partir de la forme de son spectre.

**Page d'ouverture (p.43)** — « LA BOBINE / LE DIPÔLE RL », n° 2 ; photo d'un transformateur de poste,
légende « Même les gros transformateurs utilisent des bobines ». Questionnement : « Pourquoi, les
transformateurs ne peuvent pas être utilisés en courant continu ? » · « Comment fonctionnent les
ralentisseurs électromagnétiques des véhicules “poids lourds” ? »

**Introduction (p.44, VERBATIM)** — « Une bobine est un dipôle électrocinétique constitué d'un enroulement
dans le même sens, de fil conducteur recouvert d'un vernis isolant. De ce fait, elle a une résistance
électrique interne. Un tel dipôle placé dans un circuit électrique, se comporte-t-il alors comme un
résistor vis à vis du courant électrique ? La bobine est-elle, comme le condensateur, un réservoir
d'énergie ? »

**Plan** — *L'induction électromagnétique* : 1 Le phénomène d'induction électromagnétique (1.1 par
déplacement relatif aimant-bobine, p.44–45 ; 1.2 Autre mode de production, p.45–46) · 2 Loi de Lenz
(p.46–48) · 3 La force électromotrice d'induction (p.48) · 4 L'auto-induction (4.1 Mise en évidence,
p.48–49 ; 4.2 « La force éloctromotrice [sic] d'auto-induction », p.49–51 ; 4.3 Facteurs dont dépend
l'inductance, p.51–52 ; 4.4 Relation tension–intensité « qui y cirule [sic] », p.53) · 5 Énergie
magnétique emmagasinée dans une bobine (p.53–56) · 6 Applications (6.1 Alternateurs ; 6.2 Transformateurs,
p.56). *Le dipôle RL* : 1 Réponse à un échelon de tension (1.1 expérimentale, p.57–58 ; 1.2 théorique,
p.58–60) · 2 La rupture du courant (2.1, p.61 ; 2.2, p.62) · 3 Influence des grandeurs caractéristiques sur
le régime transitoire (3.1 R, p.63–64 ; 3.2 L, p.64–65 ; 3.3 Constante de temps, p.65–66).

### Cours — Activités

- **1.1 Expérience 1 (p.44)** : bobine fermée sur un milliampèremètre à zéro central « sensible aux courants
  très brefs » (Fig.1) ; approcher un pôle d'un barreau aimanté → déviation dans un sens (Fig.2a), retour à
  zéro à l'arrêt ; éloigner → sens contraire (Fig.2b) ; mêmes observations en déplaçant la bobine ; Remarque :
  mieux avec un galvanomètre balistique.
- **1.1 Expérience 2 (p.44–45)** : bobine (B1) fermée sur R (Fig.3, A, M, masse en M), Y1 d'un oscilloscope à
  mémoire → u_R(t) ; approche du pôle nord → Fig.4a (impulsion négative, lue sur l'image) ; éloignement →
  Fig.4b (impulsion positive) ; approche plus rapide → « pic plus prononcé » ; questions 1°) que se passe-t-il ?
  2°) justifier le recours à u_R(t) ; 3°) facteurs dont dépend le phénomène.
- **1.2 Autre mode (p.45–46)** : aimant remplacé par un solénoïde (B2) de plus grand diamètre alimenté par un
  GBF, (B1) introduite dedans (Fig.5) ; Y1 → u_R(t), Y2 → u(t) du générateur ; tension sinusoïdale → tension
  « de forme semblable » aux bornes de (B1) (Fig.6) ; Remarque : générateur continu → rien une fois le courant
  établi ; question : interpréter l'apparition du courant induit ; « Constatation » et « Interprétation » :
  voir Encadrés.
- **2 Loi de Lenz (p.46–48)** : expérience 2 avec le pôle **sud** : approche (Fig.7a) → Fig.7c impulsion
  positive ; éloignement (Fig.7b) → Fig.7d impulsion négative ; questions 1°) signe de u_R et sens du courant
  induit ; 2°) vecteur champ b⃗ créé par le courant induit et nom de la face ; 3°) correspondance avec 4a/4b ;
  4°) opposition au déplacement et au signe de variation de ‖B⃗‖ ; tableau p.47 (approche, pôle N / pôle S :
  « Sens de B⃗ : de l'aimant vers la bobine | de la bobine vers l'aimant » ; « Valeur de B⃗ : ‖B⃗‖ augmente » ;
  « Sens du courant induit : La bobine présente sa face nord au pôle nord de l'aimant | La bobine présente sa
  face sud au pôle sud de l'aimant » ; « Effets du sens du courant induit : La bobine présente à l'aimant la
  face de même nom que le pôle de l'aimant qui est de son côté : répulsion bobine-aimant » / « Ayant le sens
  contraire de celui de B⃗, le vecteur champ b⃗ créé par le courant induit s'oppose à l'augmentation de
  ‖B⃗‖. ») ; Question p.48 : traiter 7b et 2b (éloignement → attraction ; b⃗ « prend plutôt le même sens que
  B⃗ ») ; Remarque : « champ induit ».
- **3 f.e.m. d'induction (p.48)** : texte seul (f.e.m. délocalisée, naît et cesse avec la cause, tension aux
  bornes d'un circuit induit ouvert).
- **4.1 Auto-induction (p.48–49)** : Fig.8 générateur E, K, (R ajustable + lampe L1) ∥ (bobine à noyau de fer
  doux + lampe L2), lampes identiques, même résistance R ; L1 brille tout de suite, L2 « avec un retard de
  quelques millièmes de secondes » ; questions 1°) même intensité à la fermeture ? 2°) influence de la bobine ?
- **4.2 f.e.m. d'auto-induction (p.49–51)** : Fig.9–10 R₀, bobine longue (B1) de r négligeable devant R₀, GBF
  à masse flottante ; A → Y1, C → Y2, masse en B ; u_AB (Y1) et u_BC (Y2, bouton INV) ; Fig.11 : u_AB
  triangulaire, u_BC carrée ; questions 1°) expressions de u_AB et u_BC ; 2°) les exprimer entre t₁ = 0 et
  t₂ = T/2 ; en déduire e en fonction de i ; raisonnement « en convention récepteur » u_BC = − e + r i ≃ − e,
  e = ± U₀ (1), di/dt = ± a₁/R₀ (2), e/(di/dt) = − U₀R₀/a₁, d'où e = − L di/dt avec L = U₀R₀/a₁.
- **4.3 Facteurs de l'inductance (p.51–52)** : autre fréquence, mêmes sensibilités, bobines (B1) N = 500,
  ℓ = 20 cm, D = 10 cm ; (B2) 500, 30, 10 ; (B3) 500, 20, 15 ; (B4) 250, 20, 10 (N nombre total de spires,
  ℓ longueur, D diamètre moyen) ; Fig.12a–d (même triangle ; créneau d'amplitude la plus grande pour (B3),
  la plus petite pour (B4), (B2) < (B1)) ; questions 1°) a) L augmente avec N, diminue quand ℓ augmente ;
  b) influence de la section ; 2°) oscillogrammes à comparer à la Fig.11 pour la dépendance en fréquence.
- **4.4 (p.53)** : symbole (Fig.13a « (L,r) »), modèle équivalent (Fig.13b, 14b : générateur de f.é.m. e en
  série avec r) ; démonstration u_AB = u_AC + u_CB = − e + r i = L di/dt + r i ; Remarque : variation très
  brusque → u ≈ L di/dt.
- **5 Énergie magnétique (p.53–55)** : Fig.15 bobine (B) L = 10 mH (« bobine de 500 spires par exemple »),
  résistance r, générateur E = 6 V, diode D, condensateur C = 5 μF, voltmètre numérique, milliampèremètre ;
  K fermé : I = 240 mA, tension nulle aux bornes de C ; après ouverture : u_AM négative ; questions 1°) diode
  passante ? 2°) déterminer r ; 3°) interpréter u_AM < 0, justifier le voltmètre numérique ; 4°) la bobine
  emmagasine de l'énergie ; 5°) importance de la diode. Interprétation : u_NM = ri + L di/dt ; régime permanent
  u_NM = ri ; courant induit bref de même sens ; p = r.i² + Li di/dt ; encart p = ri² + d/dt(½Li²), p_L =
  dE_L/dt, E_L = ½L.i². (Le texte p.54 écrit « u_AB » là où la question écrit « u_AM ».)
- **Étincelle de rupture (p.55–56)** : durée de transfert « de l'ordre de 1ms » ; ionisation de l'air ;
  précautions (condensateurs) ; exemples : allumeur de cuisinières à gaz, soudage par arc, amorçage de tube
  néon.
- **6 Applications (p.56)** : alternateur (énergie mécanique → électrique ; induit mobile / induit fixe ;
  alternateur de voiture Fig.16 : stator induit, rotor = aimant cylindrique multipolaire ; fréquence liée à
  la fréquence de rotation) ; transformateur (Fig.17, « Comme on a vu en deuxième année secondaire »,
  quadripôle, alternatif seulement).
- **RL 1.1 Établissement (p.57–58)** : générateur idéal E = 6 V, bobine L = 0,1 H, r = 10 Ω, R₀ = 40 Ω, diode
  D, K ; « on relie les points A et B du circuit respectivement aux entrées Y1 et Y2 d'un oscilloscope à
  mémoire » (ou interface d'acquisition) ; Fig.19 : (1) palier = u_AM, (2) montée = u_BM ; questions 1°)
  identifier l'intensité visualisée ; 2°) quel chronogramme représente i(t) ; 3°) I₀ graphiquement, comparer
  à E/R ; 4°) raison du retard ; 5°) allure et valeur max de u_BM si r = 0 ; 6°) rôle de la diode.
  **Fig.18 (image) : la diode D n'est PAS dessinée, et Y2 est porté en A, Y1 en B (inverse
  du texte).** Interprétation : régime transitoire puis permanent (Fig.20), I₀ = U₀/R₀ = E/R, u_AB = rI,
  bobine ≡ résistor r en régime permanent ; si r = 0, u_R₀ = E.
- **RL 1.2 (p.58–60)** : Fig.21, loi des mailles, équation et solution (voir Encadrés) ; u_AB(t) (Fig.23) ;
  questions 1°) modifier le branchement de la Fig.18 pour visualiser u_AB ; 2°) vérifier la courbe Fig.23.
- **RL 2.1 Rupture (p.61)** : même montage, régime permanent, ouverture de K → Fig.24 (u_R₀ décroissante) ;
  questions 1°) allure ; 2°) rupture instantanée ? 3°) sans diode ? ; Remarque : étincelle ; « Exemple : Avec
  L = 1 H, I = 500 mA, e = − L di/dt ≃ − L Δi/Δt. Δt ≃ 1 ms, ce qui donne e ≃ 500 V ! » (renvoi au
  « paragraphe 5 […] page 54 »).
- **RL 2.2 (p.62)** : Fig.25 (bobine, R₀, diode D en série) ; équation, solution (Encadrés) ; questions
  1°) montrer par deux méthodes u_AB = (r/R − 1)Ee^{−t/τ} ; 2°) vérifier Fig.27 (u_AB = E avant t = 0 sur la
  figure, saut à −R₀E/R puis retour vers 0) ; 3°) comparer u_AB(0) à sa valeur juste avant, en déduire que si
  r = 0, u_AB passe de zéro à (−E).
- **RL 3.1 Influence de R (p.63–64)** : montage Fig.18, L = 0,2 H ; R1 = 210 Ω, R2 = 230 Ω, R3 = 270 Ω,
  R4 = 350 Ω ; 1 ms/div, 1 V/div (Fig.28a–d) ; tableau R (Ω) 210 / 230 / 270 / 350 — t (ms) pour u_R₀ = 4 V
  (vide) ; influence qualitative ; t inversement proportionnelle à R.
- **RL 3.2 Influence de L (p.64–65)** : bobine d'inductance réglable (« Bobine dépourvue de tout noyau de fer
  doux »), R = R₀ + r = 210 Ω constante ; L1 = 0,10 H, L2 = 0,13 H, L3 = 0,15 H, L4 = 0,20 H ; 0,5 ms/div,
  1 V/div (Fig.29a–d) ; tableau L (H) / t (ms) (vide) ; t proportionnelle à L.

**Total : 15 activités/manipulations à questions** (Exp. 1, Exp. 2, 1.2, 2 Lenz [+ question p.48], 4.1, 4.2,
4.3, 5, RL 1.1, RL 1.2-questions, RL 2.1, RL 2.2-questions, RL 3.1, RL 3.2 ; §3, §4.4, §6 sans manipulation).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Conclusion (1.1, p.45)** — « Avec un déplacement relatif bobine-aimant, on peut produire un courant
> électrique dans la bobine en circuit fermé. Un tel courant électrique est appelé courant induit, alors que
> l'aimant est appelé inducteur. L'intensité du courant induit est d'autant plus grande que le déplacement
> relatif bobine-aimant est plus rapide. »

> **Constatation (1.2, p.46)** — « La variation de l'intensité du courant électrique dans une bobine produit
> un courant induit dans une autre bobine en circuit fermé à proximité de la première. Le courant électrique
> variable, qui est à l'origine du courant induit, est appelé courant inducteur, tandis que le circuit dans
> lequel il circule est appelé circuit inducteur. »

> **Conclusion (p.46)** — « Toute variation de champ magnétique crée dans un circuit électrique fermé situé à
> proximité du champ, un courant électrique appelé courant induit : c'est le phénomène d'induction
> électromagnétique. Le courant induit est d'autant plus intense que la variation locale des
> caractéristiques du champ inducteur est plus rapide. Le sens du vecteur champ magnétique inducteur est un
> facteur dont dépend le sens du courant induit. »

> **Conclusion : la loi de Lenz (p.48)** — « Le courant induit a un sens tel qu'il s'oppose par ses effets à
> la cause qui lui donne naissance. »

> **f.e.m. d'induction (p.48)** — « […] il est dû à une f.e.m. délocalisée ; elle est là, partout dans le
> circuit induit. Elle prend naissance dans le circuit avec la cause et cesse avec la cause. Si le circuit
> induit est ouvert, la f.e.m. se manifeste par l'apparition d'une tension à ses bornes. Cette force
> électromotrice est appelée force électromotrice d'induction ou force électromotrice induite. »

> **Auto-induction (p.49)** — « Une telle induction électromagnétique due à une variation du vecteur champ
> magnétique propre de la bobine (le circuit induit est lui même le circuit inducteur) est appelée
> auto-induction. Dans ce cas particulier, la f.e.m. qui est à l'origine du courant induit est appelée f.e.m.
> d'auto-induction (ou f.e.m. auto-induite). » · **Conclusion** — « Une bobine ne se comporte pas comme un
> conducteur ohmique. Placée dans un circuit fermé, elle s'oppose aux variations de l'intensité du courant
> électrique qui y circule. »

> **Définition (p.51)** — « L'inductance est une grandeur caratérisant [sic] l'aptitude d'une bobine à modérer
> les variations de tout courant électrique qui y circule. Dans le système international d'unités,
> l'inductance s'exprime en henry (H). » Note : « Nom dédié au physicien américain Joseph Henry
> (1797-1878) ». · **Signe (p.51)** — « Dans l'expression (− L di/dt), le signe (−) traduit la loi de Lenz :
> - Quand i croît, L.di/dt > 0. Donc, e < 0 : la f.e.m. d'auto-induction s'oppose à l'augmentation de
> l'intensité du courant. - Quand i décroît, L.di/dt < 0. Donc, e > 0 : la f.e.m. d'auto-induction s'oppose à
> la diminution de l'intensité du courant. » · **Conclusion : Expression de la f.e.m. d'auto-induction** —
> « Toute bobine d'inductance L parcourue par un courant électrique d'intensité i variable est le siège d'une
> force électromotrice appelée force électromotrice auto-induite (ou d'auto-induction) **e = − L di/dt**. »

> **Conclusion (p.52)** — « L'inductance d'une bobine ne dépend que de ses caractéristiques géométriques, à
> savoir le nombre total de spires, la longueur et la section moyenne, d'où sa qualification d'inductance
> propre. » · **Remarques** — « Les bobines usuelles ont une inductance nettement inférieure à 1 H. Exemple :
> - un solénoïde de 150 spires, de 15 cm de longueur et de 3 cm de diamètre a une inductance L = 140 μH, -
> L'introduction d'un barreau de fer doux dans un solénoïde fait augmenter la valeur de son inductance L.
> Mais, dans ces conditions, l'expression e = − L di/dt n'est plus valable. - Du fait que la f.e.m.
> auto-induite est due à l'inductance L de la bobine, toute bobine d'inductance L non nulle est qualifiée de
> bobine inductive. Si en plus, sa résistance est nulle, elle est dite purement inductive. »

> **Tension aux bornes (p.53, encadré rouge)** — « En choisissant comme sens positif du courant parcourant la
> bobine le sens orienté de A vers B, la tension u_AB s'écrit : u_AB = u_AC + u_CB. Par application de la loi
> d'Ohm : u_AB = −e + r i. Or, e = −L di/dt. donc : **u_AB = L di/dt + r i** »

> **Énergie magnétique (p.54–55)** — « u_NM = ri + L di/dt » (encadré) ; « p = + u_NM.i, ce qui donne :
> p = r.i² + Li di/dt » ; encart : « p = ri² + Li di/dt = ri² + d/dt(½Li²) ; ri² : puissance dissipée par effet
> Joule ; d/dt(½Li²) : puissance magnétique p_L ; Or p_L = dE_L/dt. Donc, E_L = ½L.i² » ; « On montre que
> l'énergie magnétique emmagasinée dans une bobine d'inductance L s'écrit : **E_L = ½L.i²** » ; « Si |i|
> diminue, p_L = L.di/dt [sic, facteur i absent] diminue, ce qui signifie que l'énergie magnétique diminue :
> la bobine restitue à l'extérieur un peu de l'énergie qu'elle a emmagasinée avec l'augmentation de |i|, elle
> joue ainsi le rôle de générateur. » · **Conclusion** — « Tant qu'elle est parcourue par un courant
> électrique, la bobine inductive est un réservoir d'énergie dite magnétique. » · **Remarque** — « L'énergie
> magnétique ne peut rester stockée dans une bobine en l'absence de courant. Par contre, l'énergie potentielle
> électrique reste stockée dans le condensateur même hors circuit. Donc, le condensateur est un réservoir
> permanent d'énergie, tandis que la bobine en est un réservoir temporaire. »

> **Dipôle RL (p.57)** — « On appelle dipôle RL l'association en série d'une bobine d'inductance L, de
> résistance r et d'un résistor de résistance R_o, R étant la résistance totale R_o+r du dipôle. »

> **Conclusion (p.58)** — « La réponse d'un dipôle RL à un échelon de tension E est un courant continu
> d'intensité I_o = E/R. Celui-ci ne s'établit pas instantanément à cause de l'inductance L de la bobine.
> Autrement dit, la bobine s'oppose à l'établissement du courant électrique dans la portion de circuit où elle
> se trouve insérée. »

> **Établissement — équation et solution (p.58–59)** — « u_AB + u_BM − E = 0 » ; « u_AB + u_BM = E (1) » ;
> « u_AB = L di/dt + ri » ; « u_BM = R_o.i » ; « L di/dt + Ri = E (2), avec R = R_o + r » ; « di/dt + (R/L)i =
> E/L » ; encadré « **di/dt + (1/τ) i = E/L (3), avec τ = L/R** » ; « Cette équation différentielle régit
> l'évolution dans le temps de l'intensité i du courant circulant dans le dipôle RL soumis à un échelon de
> tension E. » ; analogie avec du_C/dt + (1/τ)u_C = E/τ « (équation (1) de la page 22) » ; i(t) = Ae^{−αt} + B ;
> i(0) = A + B = 0 ; i(t) = A(e^{−αt} − 1) ; di/dt = −αA.e^{−αt} ; « Ae^{−αt}[1/τ − α] − A/τ = E/L (4) » ;
> « −A/τ = E/L, d'où A = −E/R » ; « Ae^{−αt}(1/τ − α) = 0 quel que soit t » ⇒ α = 1/τ ; encadré
> « **i(t) = (E/R)(1 − e^{−t/τ}), avec τ = L/R** » (Fig.22).

> **Conclusions (p.60)** — « La réponse d'un dipôle RL en courant est constituée de deux régimes: un régime
> transitoire au cours duquel l'intensité augmente en exponentielle à partir de la valeur zéro en tendant vers
> la valeur I_O = E/R et un régime permanent caractérisé par un courant continu d'intensité I_o. » ·
> « Éxpression [sic] de la tension aux bornes de la bobine » : « u_AB = L (E/(Rτ)).e^{−t/τ} + r(E/R)(1 − e^{−t/τ})
> = E.e^{−t/τ} + r(E/R)(1 − e^{−t/τ}) » ; « u_AB(0) = E » ; « lim_{t→∞} u_AB = (r/R)E » ; Remarque « Si r = 0,
> u_AB = Ee^{−t/τ}. Dans ces conditions lim u_AB = 0 » · « Quand on soumet un dipôle RL à un échelon de
> tension E, il apparaît instantanément aux bornes de la bobine une tension égale à E mais qui décroît selon
> un régime transitoire pour s'annuler si la résistance de la bobine est nulle. »

> **Conclusion (p.61)** — « Lors de la rupture du courant dans un circuit comportant une bobine, celle-ci a
> pour effet d'assurer la continuité du courant électrique par une annulation progressive de son intensité. »

> **Rupture — équation et solution (p.62)** — « u_AB + u_BM = 0 (1) » ; « en convention récepteur : u_AB =
> L di/dt + r.i et u_BM = R_o.i » ; « L di/dt + R.i = 0 avec R = R_o + r » ; « **di/dt + (1/τ).i = 0 (2), avec
> τ = L/R** : équation différentielle en i à coefficients constants et à second membre nul » ; i(t) = A.e^{−αt} ;
> I₀ = E/R donc A = E/R ; « −αA e^{−αt} + (1/τ)Ae^{−αt} = 0, d'où Ae^{−αt}(−α + 1/τ) = 0 ∀t » ; encadrés
> « **i(t) = (E/R)e^{−t/τ}** » avec « **R = R_o + r et τ = L/R** » (Fig.26).

> **Constante de temps (p.65)** — « Donc, la durée d'établissement du courant dans le circuit est
> proportionnelle au quotient L/R. De ce fait, le quotient L/R est appelé constante de temps du dipôle RL ; on
> la note τ. » Remarque : « On sait que la résistance R a la dimension du quotient d'une tension par une
> intensité de courant et que L a celle de U.t/I. Donc le quotient L/R a la dimension d'un temps, ce qui
> justifie encore son appéllation [sic] de constante de temps. » Encadré : « **τ = L/R : constante de
> temps** ». **Définition** — « La constante de temps τ est une grandeur caractéristique du dipôle RL, elle
> renseigne sur le retard avec lequel s'établit le régime permanent ou la rupture du courant dans le dipôle.
> τ ayant la dimension d'un temps, elle s'exprime en secondes. »

> **Détermination de τ (p.65–66)** — « Les méthodes possibles pour déterminer la constante de temps sont les
> mêmes que celles utilisées dans le cas du dipôle RC. » ▸ Par calcul direct τ = L/R ▸ « Détermination
> graphique (1ère méthode) : Sur la courbe de i(t) représentant l'établissement du régime permanent, on trace
> la tangente au point d'abscisse t = 0s. L'abscisse du point d'intersection de la tangente avec l'asymptote
> I_o = E/R est τ. (Fig.30) » ; « Justification : […] i = k t, […] k = di/dt (t = 0) = I_o/τ […] i(t) =
> (I_o/τ) t […] i(t) = (I_o/τ)t = I_o, d'où t = τ. » ; Remarque : rupture, tangente à l'origine → axe des
> abscisses en τ (Fig.31) ▸ « Détermination graphique (2ème méthode) : […] i(τ) = (E/R)(1 − e⁻¹) = 0,63 E/R »
> (Fig.32) ; rupture « i(τ) = (E/R)e⁻¹ = 0,37 E/R » (Fig.33).

**L'essentiel (p.67, VERBATIM, lu sur l'image)** — « ■ Une bobine est un dipôle électrocinétique constitué
généralement par un enroulement cylindrique dans le même sens, de fil conducteur recouvert d'une gaine
isolante. ■ Toute variation de champ magnétique à proximité d'une bobine en circuit fermé produit un courant
électrique appelé courant induit. ■ Loi de Lenz : Le courant induit a un sens tel qu'il s'oppose par ses
effets à la cause qui lui donne naissance. ■ Tout courant induit est dû à une f.e.m. délocalisée appelée
f.e.m. d'induction. ■ Toute bobine parcourue par un courant variable d'intensité i est le siège d'une f.e.m.
d'auto-induction : **e = − L di/dt**, où L est l'inductance de la bobine. ■ L'auto-induction traduit
l'opposition d'une bobine à toute variation de courant. ■ Pour une bobine d'inductance L, de résistance
interne r, parcourue de sa borne A à sa borne B par un courant variable d'intensité i, la tension à ses bornes
s'écrit: **u_AB = L di/dt + ri** ■ L'énergie magnétique emmagasinée dans une bobine parcourue par un courant
d'intensité i s'exprime : **E_L = ½Li²** ■ L'inductance d'une bobine est une grandeur caractérisant sa faculté
d'emmagasiner de l'énergie magnétique. ■ Etant liée à l'intensité du courant, l'énergie magnétique stockée par
une bobine est transférée à l'extérieur du circuit avec la rupture du courant. ■ Un dipôle RL soumis à un
échelon de tension de valeur E est parcouru par un courant continu qui ne s'établit pas brusquement, mais à la
suite d'un régime transitoire, selon la loi : **i(t) = (E/R)(1 − e^{−t/t})** [sic : exposant « t/t », lire
−t/τ] où τ = L/R est la constante de temps du dipôle RL. ■ Lors de la rupture du courant dans un circuit
comportant une bobine, l'intensité i du courant ne s'annule pas brusquement, mais en diminuant de manière
continue selon la loi : **i(t) = (E/R)e^{−t/τ}** »

### Exercices résolus

- **Exercice résolu (p.68–70)** — Énoncé : série générateur E = 6 V, K, bobine (L, r), R₀ = 140 Ω ;
  oscilloscope à mémoire ; Fig.1 (montée exponentielle, 2 ms/div, 1 V/div). 1°) choisir entre schéma 1 (R₀
  entre K et la bobine) et schéma 2 (R₀ entre la bobine et M, masse en M), ajouter les connexions ;
  2°) allure ; 3°) a) montrer du/dt + (1/τ)u = (R₀/L)E, τ = L/R, R = R₀ + r ; b) u = Ae^{−αt} + B : A, B, α ;
  4°) τ, r et L graphiquement ; 5°) i(t). Démarche : schéma 2, B à une entrée (« Entrée Y », Fig.3) ;
  u_AB + u_BM + u_MA = 0 ⇒ u + ri + L di/dt = E ⇒ du/dt + (R/L)u = (R₀/L)E ; u = B(1 − e^{−αt}) ;
  « αBe^{−αt} + (B/α)(1 − e^{−αt}) = (R₀/L)E » [sic, lire B/τ] ; B = (R₀/R)E, α = 1/τ ;
  **u = (R₀/R)E(1 − e^{−t/τ})** ; U₀ = 5,6 V ⇒ r = (E/U₀ − 1)R₀ = **10 Ω** ; « u(τ) = U₀(1 − 1/e) = 0,632 U₀ =
  3,45 V » puis « En portant u=3.54V » (figure : 3,54) → **τ = 2 ms** ; **L = τR = 300 mH** ;
  **i = I₀(1 − e^{−t/τ}), I₀ = E/R = 0,04 A**.

### Tests rapides des acquis

- **Ex. 1 — vrai/faux (p.71)** : 1- bobine dans un champ magnétique variable siège d'une f.e.m. induite ;
  2- toute variation du courant dans un circuit → f.e.m. induite ; 3- noyau de fer doux fait diminuer L ;
  4- abaisser une tension continue avec un transformateur ; 5- τ caractérise la durée du régime transitoire ;
  6- augmenter la durée du transitoire en augmentant la résistance totale ; 7- à l'établissement, la tension
  aux bornes de la bobine diminue et tend vers une limite ; 8- à l'ouverture, i ne subit pas de discontinuité.
- **Ex. 2 — QCM « la (ou les) proposition(s) juste(s) » (p.71)** : I- bobine inductive : a- s'oppose aux
  variations de la tension / b- s'oppose aux variations de l'intensité / c- équivalente en continu à un
  résistor de résistance r ; II- u_AB pour un courant de B vers A : a- L.i + r.i / b- L.di/dt + r.i /
  c- − L.di/dt − r.i / d- − (dL/dt).i − r.i ; III- L dépend de : a- la tension / b- ses caractéristiques
  géométriques / c- l'intensité ; IV- bobine purement inductive, tension : a- augmente sans cesse / b- varie en
  tendant vers zéro / c- prend instantanément E / d- tend vers une constante < E ; V- courant : a- augmente de
  manière continue vers E/R / b- diminue vers zéro / c- prend directement E/R.

### Exercices et problèmes

Exercices d'application (p.72–73) :
- **Ex. 3** : 4 schémas (bobine fermée sur R, A, M) : Fig.1 N en avant s'approche ; Fig.2 N s'éloigne ;
  Fig.3 S s'éloigne ; Fig.4 S s'approche ; sens du courant induit et nom de la face en regard.
- **Ex. 4** : bobine fermée sur R ; 1°) approche par le pôle nord : a) champ induit ; b) sens du courant ;
  2°) pôle sud en regard, éloignement : a) champs inducteur et induit au centre ; b) sens.
- **Ex. 5** : L = 40 mH ; graphe e(t) : +240 mV sur [0, 5 ms], −400 mV sur [5, 8 ms], période 8 ms (13, 16…) ;
  1°) di/dt en fonction de e et L ; 2°) di/dt sur [0, 5 ms] et [5, 8 ms] ; 3°) tracer i(t) avec i(5 ms) = 0.
- **Ex. 6** : L = 470 mH, r = 10 Ω, i(t) = 0,006 t² de A vers B ; 1°) u_AB(L, r, t) ; 2°) u_AB à t = 10 s.
- **Ex. 7** : L = 0,1 H, r négligeable, générateur de courant variable (Fig.1) ; Fig.2 i(t) en dents de scie
  0 → 120 mA de 0 à 40 ms, retour à 0 à 50 ms ; 1°) u_AB(t) sur les deux phases (0–50 ms) ; 2°) tracer u_AB
  (10 ms/div, 0,5 V/div).
- **Ex. 8** : montage type Fig.18 (A → Y1, B → Y2, masse M ; pas de diode) ; 1°) phénomène à la fermeture
  (R = R₀ + r) ; 2°) I₀ ; 3°) équation en i ; 4°) vérifier i(t) = A(1 − e^{−αt}) ; 5°) A et α ; 6°) « Définir la
  constante de temps   pour le régime transitoire » [symbole τ absent] et l'exprimer en fonction de α.
- **Ex. 9** : L, r nulle, R, U = 12 V ; 1°) schéma ; 2°) branchement de l'oscilloscope ; 3°) allure de i(t) ;
  4°) a) I₀ ; b) τ avec L = 100 mH, R = 120 Ω.
Exercices de synthèse (p.74–76) :
- **Ex. 10** : E = 6 V (idéal), K, bobine (L, r = 10 Ω), R = 200 Ω ; acquisition de u_AB (bobine) et u_BC
  (résistor) ; courbe 1 croissante → ≈ 5,7 V, courbe 2 décroissante depuis 6 V (0–20 ms) ; 1°) u_AB(i, di/dt) ;
  2°) u_BC(i) ; 3°) associer les courbes ; 4°) I₀ par la loi des mailles ; 5°) I₀ graphiquement ; 6°) τ (méthode) ;
  7°) expression de τ et homogénéité ; 8°) L ; 9°) appareil de remplacement.
- **Ex. 11** : bobine (L, r) + r' = 50 Ω, E = 6 V ; oscilloscope à mémoire sur générateur et r' (le graphe
  imprimé ne montre qu'une courbe, u_r' → ≈ 5 V, 0–10 ms) ; 1°) schéma ; 2°) « lavaleur [sic] » de la tension
  bobine ; 3°) a) I₀ ; b) r ; 4°) τ ; 5°) L ; 6°) énergie en régime permanent.
- **Ex. 12** : rupture, i(t) décroissante depuis 50 mA (0–55 ms) ; 1°) i(0) ; 2°) τ de deux façons ; 3°) L avec
  R = r + R₀ = 50 Ω ; 4°) e à t = 0.
- **Ex. 13** : générateur E = 6 V, r = 2 Ω ; bobine AB L = 1,8 H, R = 8 Ω ; en dérivation : petit moteur en
  série avec une diode au silicium D (Fig.1) ; 1°) sens du courant, I = 0,6 A, pourquoi le moteur ne tourne
  pas ; 2°) à l'ouverture, le moteur tourne : sens du courant, origine de l'énergie, phénomène ; 3°) il soulève
  m = 20 g de h = 18,5 cm (poulie, Fig.2) ; travail, comparaison à l'énergie magnétique, rendement ;
  g = 9,8 N.kg⁻¹.
- **Ex. 14 — Étude de texte « La cuisson par induction »** (p.76) : plaques froides, la casserole chauffe,
  champ magnétique variable créé par le générateur sous la plaque, courant induit dans la paroi qui « joue le
  rôle de noyau », effet Joule ; 1°) circuit du courant induit ; 2°) inducteur et induit ; 3°) source
  d'énergie ; 4°) pourquoi la casserole fait augmenter l'intensité.

**Total : 14 exercices** (2 tests rapides, 7 d'application, 5 de synthèse) + 1 exercice résolu.

### Réponses du manuel (p.392, colonnes « Chapitre 2 », lues sur l'image)

Ex. 3 : a- Nord, b- Sud, c- Sud ; d- Nord · Ex. 4 : 1°) a) Bp et Ba sont opposés, b) La règle du bonhomme
d'Ampère ; 2°) a) Bp et Ba ont le même sens, b) La règle du bonhomme d'Ampère · Ex. 5 : 1°) di/dt = − e/L ;
2°) t ∈ [0, 5 ms], i = (−6.t + 30).10⁻³ A ; t ∈ [5, 8 ms] ⇒ i = (10.t − 50).10⁻³ A ; 3°) t ∈ [0, 5 ms],
i = f(t) décroissante ; t ∈ [5, 8 ms] ⇒ i = f(t) croissante (t en ms) · Ex. 6 : 1°) u_AB = (12.L.t +
6.r.t²).10⁻³ V ; 2°) u_AB ≃ 6,06 V · Ex. 7 : 1°) t ∈ [0, 40 ms] ⇒ u_AB = 3L ; t ∈ [40, 50 ms] ⇒ u_AB =
−12.L ; 2°) [0, 40 ms] u_AB = 0,3 V ; [40, 50 ms] u_AB = −1,2 V · Ex. 8 : 1°) i(t) tend vers une limite I₀ ;
2°) I₀ = E/(r + R₀) ; 3°) di/dt + (R/L).i = E/L ; 4°) on remplace i par son expression ; 5°) A = E/R ;
α = R/L ; 6°) τ = L/R ; pour t = 5.τ le régime permanent s'établit · Ex. 9 : a) I₀ = E/R = 0,1 A ;
b) τ = L/R = 0,83 ms · Ex. 10 : 1°) u_AB = L.di/dt + r.i ; 2°) u_BC = R.i ; 3°) courbe 1 : u_BC, courbe 2 : u_AB ;
4°) I₀ = E/(r + R) = 28,6 mA ; 5°) I₀ = u_BC/r' [sic, lire /R] = 28,5 mA ; 6°) méthode de tangente ;
7°) τ = 2,5.10⁻³ s ; 8°) τ = L/(r + R), donc « R » [sic, lire L] = τ.(r + R) = 0,53 H · Ex. 11 : 2°) u_AB =
L.di/dt + r.i ; 3°) a- I₀ = u_r'/r' = 0,1 A ; b- « r' = 10 ? » [lire r = 10 Ω] ; 4°) τ ≃ 10⁻³ s ; 5°) L =
(r + r').τ = 60 mH ; 6°) W = 0,3 mJ · Ex. 12 : 1°) I₀ = 50 mA ; 2°) a) la méthode de la tangente donne
τ = 22 ms ; b) i(t₁/₂) = I₀/2 → τ = 22 ms ; 3°) L = R.τ = 1,1 H ; **4°) e = 2,5 V**.
**Pas de réponse pour Ex. 1, 2, 13, 14** (le corrigé de l'ex. 13 présent dans 223433 p.316 n'existe pas ici).

### En savoir plus / Documents

- **En savoir plus (p.77)** « Les pouvoirs de l'induction électromagnétique » (« D'après “Revue pour la
  science” ») : plaque à induction, courant de Foucault (« courants tourbillonnaires »), intensité
  proportionnelle à la vitesse et à la valeur du champ, disque de cuivre dans l'entrefer d'un aimant,
  ralentisseurs électromagnétiques des poids lourds (disques entre électroaimants, efficaces à grande
  vitesse, nuls à l'arrêt, freins mécaniques en complément).

### Écart avec la référence (sciences-exp/02 — correspondance CONFIRMÉE)

Contenu identique à 223433 ch2 (pages 42–77, mêmes 14 exercices, même exercice résolu).
- ⛔ À retirer : **rien** au titre des notions. Nuance d'objectif : τ « à partir de la courbe u_L(t) »
  seulement (référence : « courbes de réponse u_L(t) ou i(t) ») — le cours détermine pourtant τ sur i(t)
  (p.65–66), rien à retirer.
- ✅ À ajouter / autrement : « en convention récepteur » explicite (p.50 u_BC = −e + ri ; p.62 u_AB =
  L di/dt + r.i) ; **réponse de l'ex. 12 4°) : e = 2,5 V** (= R·I₀ ; la référence imprime 3,3 V) — si le
  chapitre publié reprend 3,3 V, corriger ; pas de corrigé pour l'ex. 13 (ne pas citer de « réponse du
  manuel »).
- Vocabulaire/notations identiques (Bp/Ba au corrigé ex. 4, « résistor », R₀, I₀).
- Figures : Fig.18 sans diode et voies Y1/Y2 inversées par rapport au texte (p.57) ; ex. 11 : un seul
  oscillogramme imprimé (p.75).

### Bornes de scope

- ✅ **INCLUS** (identiques à sciences-exp/02) : induction qualitative (aimant-bobine, bobine-bobine,
  inducteur/induit, courant/champ/circuit inducteur, champ induit) ; loi de Lenz (sens du courant, nom des
  faces, répulsion/attraction, b⃗ vs B⃗, bonhomme d'Ampère au corrigé) ; f.e.m. d'induction délocalisée ;
  auto-induction, **e = − L di/dt**, signe, inductance (henry), dépendance qualitative en N, ℓ, section,
  fer doux, bobine inductive / purement inductive, ordres de grandeur ; symbole, modèle équivalent,
  **u_AB = L di/dt + r i** ; u(t) à partir d'un i(t) donné (polynôme, dents de scie), di/dt à partir de e(t) ;
  p = ri² + d/dt(½Li²), **E_L = ½Li²**, réservoir temporaire/permanent, diode, étincelle de rupture
  (e ≈ L Δi/Δt) ; alternateur et transformateur qualitatifs ; dipôle RL : échelon, régimes transitoire et
  permanent, I₀ = E/R, **di/dt + (1/τ)i = E/L**, solution imposée, **i(t) = (E/R)(1 − e^{−t/τ})**, u_bobine(t),
  rupture **i(t) = (E/R)e^{−t/τ}**, u_AB = (r/R − 1)Ee^{−t/τ} ; influence de R et de L ; **τ = L/R** (calcul,
  tangente, 0,63/0,37 E/R, 5τ au corrigé) ; exploitation d'oscillogrammes.
- ⛔ **EXCLU** : flux Φ, loi de Faraday, L = μ₀N²S/ℓ ; force de Laplace, induction de mouvement ; calcul sur
  transformateurs (rapport) ; courants de Foucault hors lecture ; associations d'inductances, mutuelle ;
  régime sinusoïdal ; méthodes générales de résolution d'équations différentielles ; énergie dissipée par
  intégration.

### Lecture

- **Pages lues en L1** : 42–77 (toutes, couche texte présente partout, y compris p.66 et p.73) et 392.
- **Pages lues sur l'image (110 dpi)** : 42 à 75 (les 34 pages) + 392 (160 dpi). Non vues sur l'image :
  76 (étude de texte, prose + photo) et 77 (prose seule).
- **Relecture R-7 (2026-11-07)** : les pages d'abord non vues sur l'image (ch.2 : p.76, 77) ont été vues sur l'image par l'auditeur indépendant et sont conformes au texte transcrit.
- **Écarts texte/image** : fractions, exposants, indices perdus (p.50–51, 54–55, 59–62, 65–66, 69–70) ;
  tableau de Lenz p.47 et tableau des bobines p.51 déstructurés ; signes des impulsions Fig.4a/4b/7c/7d,
  courbes Fig.12, 19, 23, 27 et graphes des ex. 5, 7, 10, 11, 12 uniquement sur l'image ; Fig.18 : diode absente
  et voies inversées (visible seulement sur l'image) ; p.392 colonnes mêlées (lues sur l'image).
- **Coquilles [sic]** : « hamp » (p.42) ; « ÉLOCTROMOTRICE » (p.49) ; « tesions » (Fig.11) ; « caratérisant »
  (p.51) ; « lorque » (p.52) ; « CIRULE », « milliampèremère » (p.53) ; « p_L = L.di/dt » (p.55) ; « Éxpression »
  (p.60) ; « atteingne » (p.64) ; « appéllation » (p.65) ; « graphiaue », « détermi-nanation » (Fig.31–32) ;
  exposant « t/t » (L'essentiel p.67) ; « (B/α) » et « 3,45 V » vs « 3.54 V » (p.69–70) ; « lavaleur » (ex. 11) ;
  corrigé : « u_BC/r' », « R = τ.(r + R) = 0,53 H », « r' = 10 ? ».
- **Doutes [?]** : (1) Fig.18 sans la diode D que le texte et les questions 6°) (p.57) et 3°) (p.61)
  supposent ; voies Y1/Y2 inversées ; (2) p.54 « u_AB » vs « u_AM » pour la tension du condensateur ;
  (3) ex. 11 : l'énoncé annonce deux oscillogrammes, un seul est imprimé ; (4) ex. 8 6°) symbole τ manquant ;
  (5) p.61 renvoie au « paragraphe 5 … page 54 » (le §5 commence p.53) ; (6) tableaux p.63–64 non remplis ;
  (7) Fig.27 : avant t = 0 la courbe est tracée à E (et non à rE/R) ; (8) Fig.33 (p.66), censée illustrer
  la lecture à 0,37 E/R, montre une tangente à l'origine (doublon de la Fig.31), sans repère 0,37 E/R.

## 2.3 Chapitre 3 — Oscillations électriques libres (manuel 223471, p.78–109)

Bandeau : « Evolution de systèmes ◆ Oscillations électriques libres ». Deux parties titrées :
« OSCILLATIONS ÉLECTRIQUES LIBRES AMORTIES » (p.80–87) et « LES OSCILLATIONS ÉLECTRIQUES LIBRES NON
AMORTIES » (p.88–94), puis L'essentiel (p.95), Exercice résolu (p.96–99), Exercices à résoudre
(p.100–106), Fiche technique (p.107–109). Pas d'« En savoir plus ».

**Objectifs (p.78, VERBATIM, lu sur l'image)** — « Réaliser un montage permettant de suivre les
oscillations libres d'un circuit RLC série. » · « Reconnaître le régime pseudopériodique et le régime
apèriodique [sic]. » · « Reconnaître le facteur responsable de l'amortissement. » · « Reconnaître les
grandeurs oscillantes d'un circuit RLC série. » · « Etablir l'équation différentielle des oscillations
libres d'un circuit RLC série. » · « Interpréter la diminution de l'amplitude des oscillations libres d'un
circuit RLC série par le transfert d'énergie de l'oscillateur vers le milieu extérieur. » · « Ecrire
l'expression d'une grandeur oscillante en régime libre non amorti. » · « Définir la pulsation propre ω₀ et la
période propre T₀ d'un oscillateur RLC non amorti. » · « Exprimer T₀ en fonction de L et de C. » ·
« Déterminer la période, l'amplitude et la phase initiale d'une grandeur oscillante sinusoïdale d'un circuit
RLC série non amorti. » · « Démontrer la conservation de l'énergie totale d'un oscillateur LC. » ·
« Interpréter le cas particuler [sic] des oscillations libres non amorties. »

**Prérequis (p.78)** — SAVOIR : définir un phénomène périodique ; définir la période T et la fréquence N ;
« Ecrire la relation N = 1/T » ; « Ecrire la relation i = dq/dt » ; « **Ecrire, en convention récepteur,
l'expression de la tension** u = q/c : - aux bornes d'un condensateur ; - aux bornes d'une bobine u = ri +
L di/dt » ; exprimer l'énergie potentielle électrique E_C d'un condensateur ; exprimer l'énergie magnétique
E_L d'une bobine. SAVOIR FAIRE : reconnaître un phénomène périodique ; distinguer période et fréquence ;
utiliser i = dq/dt ; expliquer la charge et la décharge d'un condensateur ; « Expliquer le phènomène
d'auto-indution [sic] » ; distinguer transfert et transformation d'énergie ; appliquer la loi des mailles.

**Page d'ouverture (p.79)** — « OSCILLATIONS ÉLECTRIQUES LIBRES », n° 3 ; photo d'une montre ; légende « Le
quartz impose sa fréquence propre aux oscillations ; une montre électronique y gagne en précision. »
Questionnement : « Que désigne-t-on par les expressions “oscillations électriques”, “oscillateur
électrique”, “circuit oscillant”...? » · « Est-ce que le courant alternatif est un phénomène oscillatoire ? »

**Plan** — *Amorties* (intro p.80 : « Que se passera-t-il si l'on décharge le condensateur dans une bobine
sachant que celle-ci emmagasine aussi de l'énergie? ») : 1 Production d'oscillations libres amorties
(p.80–83) · 2 Influence de l'amortissement (p.83–85) · 3 Équation différentielle (p.85) · 4 Énergie totale
d'un oscillateur RLC série (p.85–87). *Non amorties* (intro p.88 : étude « uniquement, par une étude
théorique […] l'oscillateur LC non amorti est un cas idéal parce qu'il est impossible de le réaliser dans la
pratique ») : 1 Nature des oscillations (1.1 Évolution de la charge, p.88–89, « Simulation des
oscillations » p.89 ; 1.2 Période et fréquence, p.90 ; 1.3 Amplitude et phase initiale, p.90–92) · 2 Énergie
totale d'un oscillateur LC (2.1 Conservation, p.92–93 ; 2.2 Évolution des énergies électrique et
magnétique, p.93–94).

### Cours — Activités

- **A1 Manipulation (p.80–83)** : générateur idéal E = 5 V, C = 0,5 μF, R₀ réglable fixé à 100 Ω, bobine
  L = 1 H, r = 12,5 Ω, commutateur K (Fig.1 : 1 = charge, 2 = décharge dans (L ; r) + R₀ ; Y1 sur le
  condensateur, Y2 en A, masse en M) ; « u_c = u_BM » sur Y1, « u_Ro = u_AM » sur Y2, oscilloscope à mémoire ;
  Fig.2 oscillogrammes ① et ② (sinusoïdes amorties décalées) ; questions 1°) chronogramme en position 1 ;
  2°) ① = u_C et traduit q(t) ; 3°) ② traduit i(t) « dans le circuit MKA » ; 4°) oscillations de q et i,
  pourquoi « amorties » ; 5°) intervalles T entre maximums ou minimums de u_C et u_R₀ ; 6°) amorties ;
  pourquoi « pseudopériodiques » ; 7°) interpréter. Interprétation : q = C u_C et « u_Ro = R_o i **en
  convention récepteur** » ; récit par étapes (Fig.3 sens positif ; Fig.4a–4d ; t₀ = 0, Q₀ = CE ; [0, T/4] ;
  T/4 ; T/2 charges +Q₁ < 0 ; T ; 3T/2 ; 2T) ; Fig.5 Q₀ > |Q₁| > Q₂ > |Q₃| ; amortissement dû à R = r + R₀.
- **A2 Influence de l'amortissement (p.83–84)** : R₀ = 100 Ω, 500 Ω, 1000 Ω (Fig.6a–c, oscillations de moins
  en moins nombreuses), 3 kΩ, 4 kΩ, 5 kΩ (Fig.6d–f, apériodique) ; questions 1°) influence de R sur
  l'amortissement et la pseudopériode ; 2°) conditions d'oscillation libre ; 3°) comparer 6d, 6e, 6f, durée
  du retour à l'équilibre. Analyse : T « augmente légèrement » ; apériodique : décharge « aussi longue que la
  résistance R₀ est plus grande ». Remarques : régime critique (nommé, « difficile de le mettre en
  évidence ») ; limite d'amortissement nul → périodique (Fig.7).
- **A3 (p.85)** : Fig.8 (q, u_C, u_b, u_R₀, i) ; mise en équation (Encadrés).
- **A4 Énergie (p.85–87)** : interface d'acquisition (« console VTT par exemple ») ; R₀ = 100 Ω (Fig.9 :
  u_C(V) −5…5, t 0–12 ms) puis 500 Ω (Fig.10) ; tableur-grapheur : E_C = ½C.u_C², E_L = ½(L/R₀²).u_R₀²,
  E = E_C + E_L ; Fig.11a/11b (« En(μJ) » 0–0,6 ; énergie totale, électrique, magnétique) ; questions
  1°) zéros et maxima à T/2 ; 2°) E = E_C + E_L ; 3°) transformations mutuelles ; 4°) « Préciser l'influence
  sur la vitesse de diminution de l'énergie totale » [complément absent]. Interprétation : non-conservation
  (dE/dt = −Ri²), transformations mutuelles non intégrales.
- **B1.1 Simulation (p.89)** : logiciel, d²q/dt² + (1/LC)q = 0, L = 10 mH, C = 100 μF, Q_m = 6.10⁻⁴ C
  (Fig.13 : champs « U = 6 V, C = 100 μF, L = 10 mH, Q₀ = 0,6 mC », échelles 1 V/div, 1 ms/div).
- **B1.2 Questions (p.90)** : 1°) T₀ et N₀ sur la Fig.13 ; 2°) vérifier T₀ = 2π√LC ; Remarque : T₀ = 6,28 ms.
- **B1.3 (p.90–92)** : 2ᵉ simulation Q′_m = 9.10⁻⁴ C (Fig.14 : « U = 9 V, C = 100 μF, L = 10 mH, Q′₀ = 0,9 mC ») ;
  amplitudes = charges initiales ; q(0) = Q₀ ⇒ sinφ = 1 ⇒ φ = π/2 rad ; questions p.92 : 1°) i(t) =
  ω₀Q_m cos(ω₀t + π/2) ; 2°) i(t) = I_m sin(ω₀t + φ) : I_m et φ.
- **B2.1 Questions (p.92)** : 1°) comparer E à l'énergie transférée initialement ; 2°) E = ½L.I_m² (I_m = ω₀Q_m,
  LCω₀² = 1) ; 3°) par dE/dt, cas particulier de dE/dt = −Ri².
- **B2.2 (p.93–94)** : Fig.15 (q courbe 1, i courbe 2, q = Q_m à t = 0) ; récit énergétique par quarts de
  période ; enregistrement C = 0,47 μF, L = 0,1 H, U₀ = 5 V (Fig.16 : palier E₀ à 5,875 μJ ; graduations
  0,34 ; 0,68 ; 1,02 ; 1,36 ms) ; questions 1°) interprétation énergétique ; 2°) a) E_C et E_L périodiques ;
  b) périodes vs T₀ ; c) E vs E₀ ; 3°) E_C = (Q_m²/4C)(1 + cos 2ω₀t), E_L = ¼LI_m²(1 − cos 2ω₀t) avec
  q = Q_m cos ω₀t.

**Total : 8 activités à questions** (A1, A2, A4, B1.1–1.2, B1.3, B2.1, B2.2 + A3 sans question).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Conclusion (p.83)** — « Un circuit constitué d'un dipôle RL série fermé sur un condensateur initialement
> chargé peut être le siège d'oscillations électriques amorties. De telles oscillations qui s'effectuent
> d'elles mêmes sans intervention de l'extérieur sont dites libres. Les oscillations libres amorties sont des
> oscillations pseudopériodiques de pseudopériode T. »

> **Conclusion (p.85)** — « Un circuit RLC série fermé, avec le condensateur initialement chargé, ne peut
> osciller librement que lorsque l'amortissement est faible. Plus la résistance du circuit est grande, plus la
> pseudopériode est grande et plus le retour de l'oscillateur à son état d'équilibre est rapide. Avec des
> valeurs élevées de R, le régime n'est plus oscillatoire, il est apériodique » [?] (contredit l'analyse
> p.84, comme dans la référence).

> **Équation différentielle (p.85)** — « u_C + u_b + u_Ro = 0, ce qui signifie q/C + (ri + L di/dt) + R_oi = 0.
> D'où : L di/dt + (r + R_o)i + q/C = 0. (1) Or, i = dq/dt. Donc, (1) s'écrit : **L d²q/dt² + (r + R_o) dq/dt +
> q/C = 0 ou bien d²q/dt² + ((r + R_o)/L) dq/dt + (1/LC) q = 0.** »

> **Énergies (p.86)** — « E_C = ½C.u_C² » ; « E_L = ½ (L/R_o²).u_Ro² » ; « E = E_C + E_L ». **Non-conservation** —
> « dE/dt = d/dt(q²/2C + (L/2)i²) = (q/C)(dq/dt) + Li di/dt = i(L di/dt + q/C) » ; « L di/dt + q/C + Ri = 0, ce
> qui donne L di/dt + q/C = − Ri, d'où **dE/dt = − Ri²** » ; encart : « La vitesse de variation de l'énergie
> totale d'un système dE/dt n'est autre que la puissance instantanée p du même système : p = dE/dt ». ·
> (p.87) « L'énergie totale emmagasinée dans le circuit RLC série diminue au cours du temps, elle est
> transformée progressivement en énergie thermique par effet Joule. Cette dissipation est d'autant plus
> rapide que la résistance est plus grande. En conséquence, on dit qu'un circuit RLC série en régime libre
> est un système non conservatif. »

> **Oscillateur LC (p.88–89)** — « u_C + u_L = 0, ce qui signifie q/C + L di/dt = 0. Or i = dq/dt, d'où
> **d²q/dt² + ω₀²q = 0 avec ω₀² = 1/LC** : constante positive » ; « On constate bien que l'équation
> différentielle établie est exactement celle des oscillations libres amorties, mais sans le terme
> (R/L) dq/dt. » ; « On admet que la solution générale d'une telle équation différentielle est de la forme :
> q(t) = Q_m sin(ω₀t + φ). ω₀ : pulsation des oscillations de la charge q, exprimée en radians par seconde
> (rad.s⁻¹). Q_m : amplitude des oscillations de la charge q, exprimée en coulombs (C). φ : phase initiale de
> la charge q, exprimée en radians (rad). φ(t) = ωt + φ : phase à l'instant t, exprimée en radians (rad) » ;
> vérification : « − ω₀²q + (1/LC)q = 0, d'où q(1/LC − ω₀²) = 0 quel que soit q. Donc, 1/LC − ω₀² = 0, ce qui
> donne : ω₀ = 1/√LC ». · **Conclusion (p.89)** — « La charge q du condensateur d'un circuit LC (circuit RLC
> série non amorti) oscille sinusoïdalement au cours du temps avec la pulsation ω₀ = 1/√LC. Ne dépendant que
> des grandeurs L et C caractéristiques du circuit, la pulsation des oscillations libres non amorties est
> qualifiée de pulsation propre de l'oscillateur. »

> **Période et fréquence propres (p.90)** — « La pulsation ω₀ étant propre à l'oscillateur, la période des
> oscillations T₀ = 2π/ω₀ est appelée période propre. » **T₀ = 2π√LC** · « De même, la fréquence des
> oscillations N₀ = 1/T₀ est appelée fréquence propre des oscillations. » **N₀ = 1/(2π√LC)**

> **Conclusion (p.91)** — « L'amplitude et la phase initiale des oscillations libres d'un circuit RLC série non
> amorti ne dépendent que des conditions initiales. Toutefois, la valeur de l'amplitude est tributaire de la
> valeur de la charge initiale du condensateur, tandis que la valeur de la phase initiale est fonction du choix
> arbitraire de l'origine des temps. »

> **Conservation (p.92)** — « E = E_C + E_L = (1/2C)q² + ½Li². Avec q = Q_m sin(ω₀t + π/2), i = dq/dt =
> Q_mω₀ cos(ω₀t + π/2). Donc, E = (1/2C)(Q_m cosω₀t)² + ½L(− Q_mω₀ sin ω₀t)². E = (Q_m²/2C)cos²(ω₀t) +
> ½Lω₀²Q_m² sin²(ω₀t). Or, ω₀² = 1/LC, il vient : E = (Q_m²/2C)[(cos²(ω₀t) + sin²(ω₀t)] On sait que (cos²ω₀t +
> sin²ω₀t = 1) quel que soit t. Donc, E = (1/2C)Q_m². Q_m et C étant des constantes, E reste constante au cours
> du temps : on dit que l'énergie totale de l'oscillateur LC se conserve. »

> **Conclusion (p.93)** — « L'oscillateur RLC série en régime libre non amorti est un système conservatif. Son
> énergie est proportionnelle au carré de l'amplitude de la grandeur oscillante q(t) ou i(t). »
> **E = Q_m²/2C = ½L.I_m² = ½CU_Cm²**

> **Conclusion (p.94)** — « Les oscillations libres d'un circuit RLC série non amorti sont dues aux
> transformations mutuelles et intégrales de ses énergies électrostatique et magnétique : l'énergie totale du
> système est transférée continuellement de manière intégrale du condensateur à la bobine et inversement. »

**L'essentiel (p.95, VERBATIM, lu sur l'image)** — « ■ L'évolution de la charge du condensateur d'un circuit
RLC série est régie en régime libre par l'équation différentielle : **d²q/dt² + (R/L) dq/dt + (1/LC) q = 0**
■ Un circuit RLC série auquel on a transféré initialement de l'énergie peut être le siège d'oscillations
électriques libres amorties, c'est le régime pseudo-périodique. ■ Les oscillations libres d'un circuit RLC
série sont d'autant plus amorties et leur pseudopériode est d'autant plus grande que la résistance R du
circuit est plus grande. Pour des valeurs suffisamment élevées de la résistance R, c'est le régime
apériodique. ■ Si la résistance d'un circuit RLC série est nulle, les oscillations libres ne sont plus
amorties, elles sont sinusoïdales, c'est le régime périodique. ■ La période propre d'un oscillateur RLC série
s'exprime : **T₀ = 2π√LC** ■ La pseudo-période des oscillations libres amorties d'un circuit RLC série est
légèrement supérieure à T₀. ■ Les oscillations libres d'un circuit RLC série sont dues aux transformations
mutuelles de ses énergies électrostatique et magnétique. ■ En régime libre, l'énergie totale d'un circuit RLC
série ne se conserve que si sa résistance électrique est nulle. »

### Exercices résolus

- **Exercice résolu (p.96–99)** — Énoncé : E = 5 V (idéal), C = 1 μF, bobine L = 10 mH et r, R = 90 Ω,
  oscilloscope à mémoire, interrupteur ; Fig.1 : E–R–K, puis C ∥ (L ; r) entre A et B, Y1 en A, masse en B.
  1°) r nulle : a) K fermé : tension bobine nulle, charge du condensateur, I₀ ; b) ouverture à t = 0 :
  description, équation en u, u = U_m sin(ω₀t + φ), ω₀ = 1/√LC à calculer, U_m, φ, q(t), i(t) ; c) origine et
  valeur de l'énergie. 2°) Fig.2 (échelles portées sur la figure : flèche « 5V » verticale, « 0,2ms »
  horizontale ; palier avant l'ouverture, puis oscillations amorties) : a) r ≠ 0 par deux méthodes ;
  b) r ; c) T et T₀ ; d) variation d'énergie entre t₁ et t₂.
  Démarche : « en convention récepteur » u₁ = ri + L di/dt ; régime permanent u₁ = 0, q = 0 (u_AB = −q/C) ;
  Pouillet **I₀ = E/R = 55,5 mA** ; u − L di/dt = 0, q = −C.u ⇒ **d²u/dt² + (1/LC)u = 0** ; ω₀ = 10⁴ rad.s⁻¹ ;
  sinφ = 0 et cosφ < 0 ⇒ **φ = π rad** ; U_m = I₀/(Cω₀) ≃ 5,55 V ; **u(t) = 5,55 sin(10⁴t + π)** ;
  **q = 5,55.10⁻⁶ sin(10⁴t)** ; I_m = I₀ = 55,5 mA, **i = 55,5 sin(10⁴t + π/2)** (mA) ; **E = ½L.I₀² =
  1,54.10⁻⁵ J** ; 2°a) amplitude décroissante ; u = 0,5 V pour t < 0 ; b) **r = u.R/(E − U) = 10 Ω** [sic :
  « E − U » au dénominateur pour E − u] ; c) « T = t₂ − t₁ qui correspond à peu près à 3.15 div […] une division
  représente 0,2 ms. Donc, **T = 0,63 ms** » ; T₀ = 2π/ω₀ = 0,628 ms ; T légèrement supérieure à T₀ ;
  d) E₁ = ½CU_m1², E₂ = ½CU_m2², « **U_m1 = 5,5 V et U_m2 = 5 V** », **E₂ − E₁ = ½C(U_m2² − U_m1²) =
  − 2,625.10⁻⁶ J**.

### Tests rapides des acquis

- **Ex. 1 — vrai/faux (p.100)** : 1- décharge dans une bobine identique à la décharge dans un résistor ;
  2- pseudo-période légèrement inférieure à la période propre ; 3- un RLC transfère son énergie à l'extérieur
  d'autant plus rapidement que sa résistance est plus grande ; 4- en pseudo-périodique, le nombre
  d'oscillations augmente quand la pseudo-période augmente ; 5- oscillations libres d'un RLC amorti dues à des
  transformations intégrales des énergies.
- **Ex. 2 — QCM « la (ou les) proposition(s) juste(s) » (p.100)** : I- amortissement dû à : a- capacité /
  b- inductance / c- résistance du résistor / d- résistance de la bobine / e- résistance totale ; II- décharge
  dans une bobine purement inductive : a- périodiques / b- sinusoïdales amorties / c- pseudo-périodiques non
  amorties / d- incessantes ; III- « La pèriode [sic] propre » T₀ : a- 2π√(L/C) / b- 2π√(1/LC) / c- 2π√LC ;
  IV- un RLC ne peut entrer en oscillations libres : a- sans lui transférer initialement de l'énergie / b- sans
  lui transférer sans cesse de l'énergie / c- sans qu'il transfère lui-même de l'énergie à l'extérieur /
  d- sans les transformations mutuelles.

### Exercices et problèmes

Exercices d'application (p.100–102) :
- **Ex. 3** : bobine (r, L), C = 15 μF, pile plate E = 4.5 V, R = 1 kΩ (Fig.1 commutateur 1/2, entrée Y sur
  u) ; Fig.2 (1 V/div, 20 ms/div) ; 1°) phénomène ; 2°) énergie à t = 0 et après deux oscillations,
  transformations sur une pseudopériode ; 3°) équation en u_C si r nulle ; 4°) ω₀, T₀ littéraux ; T ≈ T₀ ⇒ L.
- **Ex. 4** : L = 1 H, résistance R (de la bobine), C = 1 μF ; graphe u_C et E_C sans échelle d'ordonnées
  (« 1ms ») ; 1°) R non nulle ; 2°) T ; 3°) comparer à T₀ ; 4°) T_E ; 5°) comparer.
- **Ex. 5** : C = 0.47 μF chargé sous 5 V, L = 44 mH, résistance nulle, interrupteur ; 1°) a) équation en u_C,
  T₀ ; b) u_C(t) ; c) q(t) ; 2°) C′ = 4C, L′ = L/2 : T′₀ en fonction de T₀.
- **Ex. 6** : d²q/dt² + (1/LC)q = 0 (1), Q₀ = 4.10⁻⁴ C ; 1°) « l'expession [sic] » de l'énergie totale ;
  2°) retrouver (1) par conservation ; 3°) vérifier q = Q_m sin(ω₀t + φ) ; 4°) T₀ ; 5°) constantes de q (C = 30 μF,
  L = 0,1 H, fermeture à t = 0).
- **Ex. 7** : C = 1,16 μF, L = 0,35 H, r ; T = 4,4 ms ; graphe u(V) (−2…2), maxima numérotés 1 à 7 ;
  1°) T vs T₀ ; 2°) énergie électrique en t₁ et t₇ ; 3°) a) énergie magnétique et totale aux mêmes instants ;
  b) conclure.
Exercices de synthèse (p.102–106) :
- **Ex. 8** : E = 6 V, C = 20 μF, L = 0,8 H (r nulle), deux R = 20 Ω, K1, K2 (Fig.1). A- K1 fermé : 1°) phénomène
  (voie 1) ; 2°) schéma, sens du courant, signes des charges, u₁ ; 3°) Fig.2 (u₁ 0 → 6 V, t 0–4 ms) : τ, C avec
  R = 20 Ω ; 4°) τ du₁/dt + u₁ = E : a- retrouver ; b- u₁ = E[1 − exp(−t/τ)], u₁(5τ), conclure. B- K1 ouvert, K2
  fermé : Fig.3 (« 5 ms/dv [sic] ; 1 V/div pour u₁ ; 0,2 mV/div pour u₂ ») : 1°) attribuer les courbes ;
  2°) équation de u₂(t) ; 3°) T vs T₀ ; 4°) Fig.4/Fig.5 : L ou R augmentée.
- **Ex. 9** : C = 10 μF, U₀ = 3 V ; 1°) charge et énergie ; 2°) L = 0,1 H, résistance nulle, t = 0 : a) schéma,
  allure ; b) interprétation énergétique ; c) équation en u_C ; d) relation T₀, C, L pour u_C = U_m sin(ω₀t + φ) ;
  e) U_m, φ ; f) instants de |i| maximale ; 3°) r non nulle, oscillogramme 10 ms/div : a- T vs T₀ ; b- pourquoi
  un oscilloscope à mémoire ; c- énergie thermique dissipée entre t₀ = 0 et t₁ = T.
- **Ex. 10** : vérifier L = 0,2 H ; C = 0,5 μF chargé sous E = 6 V ; acquisition de u (6 V, t 0–50 ms) ;
  1°) pseudopériodique ; 2°) a) équation en u ; b) forme d²u/dt² + (1/τ) du/dt + ω₀²u = 0 : τ, dimension,
  signification ; τ approché ⇒ L (R = 20 Ω) ; c) écart relatif (L_exp − L)/L, indication correcte ?
- **Ex. 11** : générateur idéal, condensateur, deux résistors, bobine inductive (Fig.1 : E, R, K 1/2, C, L, R₀) ;
  1°) charge de C = 50 μF par E = 6 V à travers R = 30 kΩ (Fig.2 : courbes (1) croissante, (2) décroissante,
  u 0–6 V, t 0–4 s) : a) courbe de u_C ; b) charge finale ; c) τ (63 %) ; d) i à t = τ ; 2°) K en 2 : u_C sur Y1,
  u_R₀ (R₀ = 5 Ω) sur Y2 ; 5 ms/div ; 1 V/div (Y1), 250 mV/div (Y2) ; Fig.3 points P et Q : a) E_C, E_L en P et
  Q ; b) comparer les énergies totales.
- **Ex. 12 — Étude de texte « Capteur d'humidité »** (p.105–106) : hygrométrie (%HR), capteurs résistifs vs
  capacitifs (« humidistances », « Un hémidistance [sic] ») ; condensateur plan C ≈ 120 pF, diélectrique
  polymère (polyamide) (Fig.1) ; inséré dans un RLC série (Fig.2 : boîtier, bobine, résistance) ; −10 °C à
  +40 °C, 10 à 100 %HR, réponse ~30 s ; 1°) « hygroscopique » ; 2°) humidité ⇒ variation de N₀ ;
  3°) « Sachant que la valeur de C est à 40% HR » et N₀ = 31850 Hz, L = 200 mH : taux d'humidité.

**Total : 12 exercices** (2 tests rapides, 5 d'application, 5 de synthèse) + 1 exercice résolu.

### Réponses du manuel (p.392, colonne « Chapitre 3 », lue sur l'image 160 dpi)

Ex. 3 : 1°) Oscillations libres amorties ; 2°) E = 1,52.10⁻⁴ J ; 4°) L = 2,67 H · Ex. 4 : 1°) L'amplitude
décroit au cours du temps ; 2°) T = 6,5 ms ; « 2°) » [sic, lire 3°)] T₀ = 6,28 ms ; 4°) T_E = 3,3 ms ;
5°) T = 2T_E · Ex. 7 : 1°) T₀ = 4,0 ms et T = 4,4 ms, donc T > T₀ ; 2°) E₁ = 1,485 μJ et E₇ = 0,145 μJ ;
3°b) L'énergie totale diminue au cours du temps · **Ex. 8 : A. 3°) τ = 0,4 ms ; 4°b) u₁ = 0,993 E ≃ 5,96 V. Le
condensateur est complètment [sic] chargé. B. 1°) La courbe (2) représente U_r [sic]. 2°) (L/2R) du₂/dt + U₂
+ (1/2RC) ∫ U₂ dt = 0 ; 3°) T = 25 ms, T₀ = 24,8 ms. Donc : T ≃ T₀ ; 4°) Fig. 4 correspond à une augmentation de
L. Fig.5 correspond à une augmentation de R.** · Ex. 9 : 1°) Q₀ = 3.10⁻⁵ C ; 2°e) U_m = 3 V, φ = π/2 rad ;
2°f) t_k = 0,75 T₀ + kT₀ ; 3°a) T > T₀ ; 3°c) W_J = 32,2 μJ · Ex. 10 : 1°) L'amplitude des oscillations
diminue ; 2°b) L = 0,25 H ; 25 % · Ex. 11 : 1°a) A t = 0, u_C = E, donc (2) correspond à u_C ; 1°c) τ = 0,7 s ;
1°d) i ≃ 158 μA. **Pas de réponse pour Ex. 1, 2, 5, 6, 12.**

### En savoir plus / Documents

- **Fiche technique (p.107–109)** « Visualisation d'un régime transitoire avec un oscilloscope analogique » :
  persistance rétinienne θ_p = 0,1 s ; générateur de créneaux ±U₀ = ±5 V (Fig.1, abscisses légendées « T₀/2 »
  et « T₀ ») au lieu de E = 5 V (montage Fig.2, renvoi à « la figure 1 de la page 80 ») ; Fig.3 oscillogramme
  stable ; conditions « T₀ << T_e. D'où, LC << T_e² » et « T_e < θ_p. D'où, T_e² < θ_p² » ⇒ « LC << θ_p² =
  10⁻² s² » ; Remarque : pour RC/RL, demi-période dix fois plus grande que la constante de temps ; Fig.4 une
  seule décharge oscillante ; entrée d'oscilloscope R_osc = 1 MΩ ∥ C_osc 16 à 47 pF (Fig.5) ; équation
  LC d²u_C/dt² + [(R₀ + r)C + L/R_osc] du_C/dt + (1 + (R₀ + r)/R_osc) u_C = u ; conditions R/R_osc << 1 et
  L/((R₀ + r)C) << R_osc = 10⁶ Ω ; exemples L = 10 mH, C = 100 μF, (R₀ + r) = 20 Ω → 5 Ω « très bon choix » ;
  L = 1 H, C = 1 μF → « 5.1O4 [sic] Ω » « mauvais choix ».

### Écart avec la référence (sciences-exp/03 — correspondance CONFIRMÉE)

Contenu identique à 223433 ch3 (pages 78–109, mêmes activités, mêmes 12 exercices, même fiche technique).
- ⛔ À retirer : **rien** au titre des notions.
- ✅ À ajouter / autrement :
  - « convention récepteur » explicite (prérequis p.78 ; interprétation p.81 ; exercice résolu p.97).
  - **Exercice résolu, valeurs différentes** : T ≈ **3,15 div** → **T = 0,63 ms** (référence 3,25 div,
    0,65 ms) ; **U_m1 = 5,5 V, U_m2 = 5 V, E₂ − E₁ = −2,625.10⁻⁶ J** (référence 5 V / 4,5 V, −2,375.10⁻⁶ J).
    Si le chapitre adapté reprend cet exercice, utiliser les valeurs de 223471.
  - **Corrigé de l'ex. 8 présent** (τ = 0,4 ms ; u₁(5τ) ≃ 5,96 V ; équation (L/2R)du₂/dt + u₂ +
    (1/2RC)∫u₂dt = 0 ; T = 25 ms, T₀ = 24,8 ms ; Fig.4 ↔ L, Fig.5 ↔ R) — la référence n'en a pas.
  - Corrigé ex. 9 sans le renvoi « Voir cours page 2° » de la référence.
- Notations : « circuit MKA » (référence « MNKA »), u_c = u_BM (référence u_NM) ; le reste identique.

### Bornes de scope

- ✅ **INCLUS** (identiques à sciences-exp/03) : décharge d'un condensateur dans une bobine (L ; r) + R₀,
  visualisation u_C (image de q) et u_R₀ (image de i), oscilloscope à mémoire ou acquisition ; oscillations
  libres, amorties, pseudopériodiques, pseudopériode ; régimes pseudopériodique, apériodique, critique
  (nommé), périodique ; influence qualitative de R ; T légèrement > T₀ ; équation **d²q/dt² + (R/L)dq/dt +
  (1/LC)q = 0** (et en u, en u_R₀ intégro-différentielle au corrigé ex. 8) ; E_C, E_L, **dE/dt = −Ri²**,
  p = dE/dt, non conservatif, transformations mutuelles ; oscillateur LC : **d²q/dt² + ω₀²q = 0**, solution
  admise **q = Q_m sin(ω₀t + φ)**, **ω₀ = 1/√LC, T₀ = 2π√LC, N₀ = 1/(2π√LC)**, amplitude et phase par les
  conditions initiales, i(t), I_m = ω₀Q_m ; conservation **E = Q_m²/2C = ½LI_m² = ½CU_Cm²** ; E_C, E_L en
  (1 ± cos 2ω₀t), période T₀/2 ; lectures d'oscillogrammes ; rappels RC/RL (ex. 8, 11) ; convention
  récepteur.
- ⛔ **EXCLU** : résolution de l'équation amortie (pas d'exponentielle × sinus, pas de décrément, pas de
  facteur de qualité) ; résistance critique chiffrée ; oscillations forcées, résonance, impédance ;
  **entretien des oscillations** (traité ici au chapitre 4 « Oscillations électriques entretenues », p.110+) ;
  Fresnel ; analogie mécanique ; oscilloscope analogique et impédance d'entrée (fiche technique, non exigible).

### Lecture

- **Pages lues en L1** : 78–110 (p.110 = garde du ch4, vérifiée) et 392.
- **Pages lues sur l'image (110 dpi)** : 78, 80, 81, 83 à 109 (30 pages) + 392 (160 dpi). Non vues sur
  l'image : 79 (page d'ouverture, photo + 2 questions lues en L1) et 82 (prose du récit par étapes et
  Fig.4b–4d, Fig.5 — texte pris en L1).
- **Relecture R-7 (2026-11-07)** : les pages d'abord non vues sur l'image (ch.3 : p.79, 82) ont été vues sur l'image par l'auditeur indépendant et sont conformes au texte transcrit.
- **Écarts texte/image** : ω, φ, π, √ supprimés (p.88–92, 95, 98, 100 QCM III) ; équations éclatées (p.85, 86,
  108) ; E_L = ½(L/R₀²)u_R₀² illisible (p.86) ; « ≃ » rendu « b » (p.98, 108) ; φ = π (p.98) perdu ; 1/τ ex. 10
  perdu ; θ_p rendu « p » (p.107) ; valeurs des champs des Fig.13–14, échelles et courbes uniquement sur
  l'image ; p.392 colonnes mêlées.
- **Coquilles [sic]** : « apèriodique », « particuler » (p.78) ; « auto-indution », « phènomène » (p.78) ;
  « visualié » (p.80) ; « quit » (p.81) ; « exrêmums » (p.82) ; « de moins au moins » (p.84) ; « mégnétique »
  et deux « t₂ » (p.87) ; « φ(t) = ωt + φ » (p.88) ; « non amori » (p.92) ; « électrostique » (p.93) ; « pèriode »
  (QCM III) ; « acquisation » (ex. 3), « vériferait » (ex. 3) ; « l'expession » (ex. 6) ; « 5 ms/dv » (ex. 8) ;
  « emmagasiné » (ex. 9) ; « hémidistance », « sensibilté » (ex. 11–12) ; « r = u.R/(E − U) » (p.98) ;
  « 5.1O4 » (p.109) ; corrigé : « 2°) T₀ » (ex. 4), « complètment », « U_r » (ex. 8).
- **Doutes [?]** : (1) Conclusion p.85 « plus le retour … est rapide » contredit l'analyse p.84 (même
  défaut que la référence) ; (2) corrigé ex. 11 (« (2) correspond à u_C », τ = 0,7 s, i ≃ 158 μA)
  incompatible avec la Fig.2 (courbe (1) croissante = u_C ; RC = 1,5 s) — à re-résoudre ; (3) Fig.11a/11b :
  axe « En(μJ) » 0–0,6 alors que ½·0,5 μF·25 V² = 6,25 μJ ; (4) p.86 question 4°) sans complément ;
  (5) exercice résolu Fig.2 : flèche verticale étiquetée « 5V » (sensibilité non explicitée en V/div) — les
  valeurs U_m1 = 5,5 V, U_m2 = 5 V et u = 0,5 V ne se vérifient pas sans hypothèse ; (6) ex. 9 3°)
  oscillogramme sans sensibilité verticale (W_J = 32,2 μJ invérifiable) ; (7) ex. 12 3°) phrase incomplète,
  aucune loi C(%HR) : non résoluble tel qu'imprimé ; (8) Fig.1 fiche technique : abscisses « T₀/2 », « T₀ »
  pour le créneau de période T_e ; (9) Fig.1 p.80 : point B non étiqueté alors que le texte écrit u_c = u_BM ;
  (10) corrigé ex. 8 B.1°) « La courbe (2) représente U_r » (lire u₂, tension du résistor).

## 2.4 Chapitre 4 — Oscillations électriques entretenues (manuel 223471, p.110–129)

**Plage vérifiée** : la page d'objectifs/prérequis est la p.110 (et non la p.111 du brief) ; la page d'ouverture
numérotée « 4 » est la p.111 ; le cours va de la p.112 à la p.117 ; L'essentiel p.118 ; Exercices p.119–124 ; Fiche
technique p.125–127 ; En savoir plus p.128–129. La p.130 est déjà la page d'objectifs du chapitre 5.
Bandeau : « Evolution de systèmes électriques ◆ Oscillations électriques entretenues » ; de la p.122 à la p.129 le
bandeau ajoute « - 4ᵉ Sc Info ».

**Objectifs (p.110, VERBATIM)** — « Réaliser à l'aide d'un amplificateur opérationnel, un montage équivalent à un dipôle
à résistance négative. » · « Réaliser un montage permettant d'entretenir les oscillations d'un circuit RLC série. » ·
« Déterminer la valeur de la résistance négative indispensable à l'entretien des oscillations d'un circuit RLC série. » ·
« Montrer que la fréquence des oscillations entretenues est égale à la fréquence propre de l'oscillateur. » ·
« Interpréter énergétiquement l'amorçage des oscillations entretenues d'un circuit RLC série. »

**Prérequis (p.110)** — SAVOIR : Définir un oscillateur électrique. · Définir la pulsation propre, la période propre et la
fréquence propre d'un oscillateur RLC série. · Ecrire l'équation différentielle régissant les oscillations libres d'un
circuit RLC série. · Exprimer l'énergie totale d'un circuit RLC série. · **Enumérer les propriétés d'un amplificateur
opérationnel idéal.** SAVOIR FAIRE : Reconnaître les oscillations libres d'un circuit RLC série. · Visualiser à
l'oscilloscope les oscillations libres amorties d'un circuit RLC série. · Mesurer la pseudopériode des oscillations libres
amorties d'un circuit RLC série. · Etablir l'équation différentielle régissant les oscillations libres d'un circuit RLC
série. · Expliquer la diminution de l'énergie totale d'un oscillateur RLC série.

**Page d'ouverture (p.111)** — « OSCILLATIONS ÉLECTRIQUES ENTRETENUES », n° 4 ; photo : satellite au-dessus de la Terre,
avion, camion, navire ; légende (texte incliné, lu sur l'image) : « Egnos, satellite géostationnaire assurant la sécurité
des applications de la navigation aérienne et maritime grâce à son horloge atomique dont les oscillations sont entretenues
en permanence. » Questions d'accroche (VERBATIM) : « La résistance d'un oscillateur électrique étant inéluctable, n'y
a-t-il pas un moyen pratique à la compensation de l'amortissement conséquent ? » · « Quel rôle peut-elle avoir la pile
d'alimentation dans le fonctionnement de l'oscillateur à quartz d'une montre électronique ? »

**Plan (titres numérotés du manuel)** — introduction (p.112) · **1** Principe d'entretien des oscillations libres (p.112) ·
**2** Exemple de dipôle à résistance négative (2.1 Étude expérimentale, p.112–113 ; 2.2 Étude théorique en régime
linéaire, p.113–114 ; Conclusion ; Remarque) · **3** Entretien d'un oscillateur RLC série avec un dipôle à résistance
négative (3.1 Étude expérimentale, p.114–115 ; 3.2 Interprétation énergétique de l'entretien des oscillations,
p.116–117) · L'essentiel (p.118) · Exercices : Exercice résolu (p.119–120) ; Exercices à résoudre — Tests rapides des
acquis (1 V/F, 2 QCM, p.121), Exercices d'application (3–7, p.121–122), Exercices de synthèse (8–10, p.122–124),
11 Étude de texte (p.124) · Fiche technique « Réalisation pratique d'oscillations électriques entretenues » (p.125–127) ·
En savoir plus « Amorçage et stabilisation des oscillations entretenues » (p.128–129).

### Cours — Activités

- **Introduction (p.112)** — oscillations libres « plus ou moins amorties » ; pour qu'elles perdurent, restituer
  continuellement l'énergie dissipée sous forme thermique avec un « dispositif d'entretien » ; étude limitée au circuit
  RLC série.
- **§1 Principe (p.112, raisonnement, pas de manipulation)** — modèle RLC série (C, inductance pure L, résistance totale
  R ≈ r de la bobine) ; amortissement dû à la chute de tension u_R ; on insère en série un dipôle D faisant apparaître une
  tension u opposée à u_R (Fig.1 : R, L, C en série avec D ; flèches u_R, u_L, u_C, u ; courant i).
- **§2.1 Manipulation — dipôle à résistance négative (p.112–113)** — Fig.2a (schéma) et Fig.2b (photo) : amplificateur
  opérationnel (TL081 ou 741) ; entre l'entrée E⁻ et la sortie S un résistor (imprimé « R », lire R₁ [sic], courant i₁) ;
  entre S et D le résistor R₂ ; D relié à E⁺ ; entre D et la masse M le résistor réglable R' ; R₁ = R₂ = 1 kΩ,
  R' = 50 Ω ; alimentation ±15 V (non représentée) ; à gauche de A et M : GBF en série avec R = 200 Ω, interrupteur K ;
  Y₂ en A (tension u = u_AM), Y₁ entre GBF et R (u_BM). GBF : tension **triangulaire** ≈ 2 V crête à crête, N = 250 Hz,
  puis on augmente l'amplitude jusqu'à saturation de l'A.O. (sortie u_S visualisée). Mode **XY** avec voie Y₁ inversée :
  caractéristique u = f₁(u'), u' tension aux bornes de R en convention récepteur. Fig.3a (R₁ = R₂ = 1 kΩ, R' = 50 Ω),
  Fig.3b (R₁ = R₂ = 1 kΩ, R' = 80 Ω), Fig.3c (R₁ = R₂ = 2 kΩ, R' = 80 Ω) ; sensibilités 1 V/div sur Y₁ et 0,5 V/div sur
  Y₂ ; courbes en N (segment central décroissant, deux branches montantes). Questions (VERBATIM) : « 1°) Montrer que la
  caractéristique u = f₁(u') représente la cractéristique [sic] u = f(i), où i est l'intensité du courant débité par le
  générateur BF et justifier l'inversion du signal visualisé sur la voie Y₁. 2°) Comparer les linéarités des portions
  centrales des caractéristiques u = f₁(u') de la figure 3 et en déduire l'influence de la valeur de R' et de la valeur
  commune de R₁ et de R₂ sur la pente et la largeur de ces portions linéaires. 3°) Calculer la pente p de chacune des
  portions linéaires des caractéristiques u = f₁(u') de la figure 3. 4°) Montrer d'après la forme de l'oscillogramme
  u = f₁(u') de la figure 3 que u = ki, où k est une constante négative que l'on exprimera en fonction de la pente p et de
  la résistance R. 5°) - Calculer k dans les trois cas de figures 3a, 3b et 3c. - Comparer les valeurs de k et de R'. »
  (Aucune valeur de pente ni de k n'est imprimée.)
- **§2.2 Étude théorique en régime linéaire (p.113–114)** — lois des mailles et des nœuds sur le dipôle AM, A.O. idéal :
  voir Encadrés ; Fig.4 : GBF + R en série avec un dipôle (−R') entre A et M.
- **Remarque (p.114)** — A.O. à réaction sur l'entrée **non inverseuse** (Fig.5) : toujours un dipôle (−R'), mais
  « qui n'est stable qu'avec des valeurs très élevées de R' ».
- **§3.1 Manipulation — entretien d'un RLC série (p.114–115)** — Fig.6 : à gauche de A et M, C, bobine (L, r) et R₀ en
  série (Y₁ aux bornes de R₀, Y₂ en S) ; L = 1 H ; C = 47 μF ; R = R₀ + r ; R₀ = 2 kΩ ; r de l'ordre de 25 Ω ; R'
  réglable (n × 1 Ω, n × 10 Ω, n × 100 Ω, n × 1 kΩ). R' = 0 au départ ; A.O. alimenté ±15 V ; K fermé ; oscilloscope
  numérique sur u₀ aux bornes de R₀. En augmentant R', amorçage pour **R' = 2070 Ω environ** puis stabilisation
  quasi-sinusoïdale (Fig.7a : amorçage et stabilisation, amplitude croissante puis constante ; Fig.7b : régime
  permanent, 10 ms/div et 1 V/div ; Fig.8 plus ample ; Fig.9 écrêtée, quasi trapézoïdale) ; R' plus
  élevée → amplitude plus grande (Fig.8, mêmes sensibilités) ; R' trop élevée → sinusoïde « distordue et écrêtée »
  (Fig.9). Questions (VERBATIM) : « 1°) Qu'est-ce qui fait naître dans le circuit RLC série les oscillations illustrées par
  l'oscillogramme de la figure 7a, surtout que l'on sait que le condensateur n'a pas été chargé au préalable. 2°) Expliquer
  l'absence d'oscillations pour les valeurs de R' inférieures à R (R = R₀ + r). 3°) On s'attendait à ce que l'on obtienne
  des oscillations sinusoïdales pour R' = R, mais l'expérience montre que les oscillations ne sont générées que pour une
  valeur de R' un peu supérieure à R (R' = 2070 Ω). Expliquer cette différence. 4°) Mesurer directement sur
  l'oscillogramme de la figure 7b, la période des oscillations entretenues et la comparer à la valeur de la période propre
  T₀ = 2π√LC de l'oscillateur. 5°) Expliquer l'augmentation de l'amplitude des oscillations quand R' est trop supérieure à
  R, ainsi que leur écrétage [sic]. » (Lecture de Fig.7b : crêtes espacées de ≈ 2 div, soit ≈ 20 ms ; T₀ calculé =
  2π√(1 × 47·10⁻⁶) ≈ 43 ms — voir doutes [?].)
- **§3.2 Interprétation énergétique (p.116–117)** — question d'entrée : « Grâce à son alimentation en + 15 V et en -15 V,
  l'amplificateur opérationnel fournit au dipôle RLC série de l'énergie. Mais, avec les petites valeurs de R', cette
  énergie suffit-elle pour y générer d'abord des oscillations ? » Fig.10 : circuit équivalent (R₀, bobine L,r, C, −R').
  Discussion en quatre cas (R' < R ; R' = R ; R' > R ; R' >> R) : voir Encadrés. Notes marginales p.117 : « Pour plus de
  détails, se référer à la fiche technique présentée à la fin du chapitre (p. 127). » · « L'étude de l'influence de la
  fréquence des oscillations sur la valeur de la résistance de la bobine de l'oscillateur est hors programme. »

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Principe (§1, p.112)** — « Or, en convention récepteur, u_R = Ri, avec R = r. Donc u = - Ri, où le coefficient
> négatif (- R) signifie une résistance négative simulée par le dipôle D. »

> **Étude théorique (§2.2, p.113–114)** — « Pour la maille MAE⁻E⁺DM, on a : u = R'i' + (v⁻ - v⁺) (1) · Pour la maille
> DSE⁻E⁺D, on a : R₂i₂ + R₁i₁ + (v⁺ - v⁻) = 0 (2) · La loi des noeuds s'écrit au point E⁻ : i + i₁ + i⁻ = 0 (3) · Au point
> D : i₂ + i' + i⁺ = 0 (4) » ; « L'amplificateur opérationnel utilisé étant supposé idéal, on a : ε = (v⁺ - v⁻) = 0,
> i⁺ = 0 et i⁻ = 0. D'autre part, R₁ = R₂. Les équations (1), (2), (3) et (4) deviennent : u = R'i' (1)' ; i₂ = - i₁ (2)' ;
> I₁ = - i (3)' ; I' = - i₂ (4)' » [majuscules I₁, I' imprimées ainsi] « D'où la relation : **u = - R'.i** Par conséquent,
> le montage de l'amplificateur opérationnel de la figure 2 est équivalent à un dipôle AM caractérisé par une résistance
> négative (-R'). (Fig. 4) »

> **Conclusion (p.114, encadré)** — « Avec un amplificateur opérationnel monté en boucle fermée à réaction sur l'entrée
> inverseuse, on peut réaliser un dipôle à résistance négative. En convention récepteur, la tension u aux bornes d'un
> dipôle à résistance négative (-R), parcouru par un cournat [sic] d'intensité i s'écrit : **u = - R i** »

> **Conclusion (§3.1, p.115, encadré)** — « Il est possible d'entretenir les oscillations d'un circuit RLC série en le
> fermant sur un dipôle à résistance négative légèrement supérieure en valeur absolue à la résistance totale du circuit.
> Les oscillations entretenues d'un circuit RLC série sont quasi-sinusoïdales de fréquence égale à la fréquence propre de
> l'oscillateur. L'amplitude des oscillations entretenues augmente avec la valeur absolue de la résistance négative
> d'entretien. »

> **Mise en équation (§3.2, p.116)** — « En fait, en convention récepteur, la loi des mailles s'écrit pour le circuit
> électrique équivalent (Fig.10) du montage d'entretien des oscillations : **q/C + L di/dt + r i + R₀i + (- R') i = 0.**
> Il vient donc, **q/C + L di/dt + R_t i = 0, avec R_t = R₀ + r - R'.** On sait qu'en multipliant une telle équation par
> i = dq/dt, on aboutit à **dE/dt = - R_t.i²**, où E = E_C + E_L : énergie totale de l'oscillateur. »

> **Cas R' < R (p.116)** — « Si R' < R, on a R_t > 0. Par suite, dE/dt < 0, ce qui signifie que l'énergie apportée par le
> dipôle à résistance négative ne suffit pas pour compenser les pertes par effet Joule dues à R_t. Par conséquent, les
> oscillations initiées dans le circuit RLC série sont systématiquement amorties, ce qui explique l'impossibilité de les
> visualiser dans de telles conditions. »

> **Cas R' = R (p.116–117)** — « Dans le cas où R' est égale à R, la résistance totale R_t devient nulle. En d'autres
> termes, lorsque cette condition est satisfaite, on a dE/dt = 0, ce qui signifie que l'énergie totale E du système ne
> diminue plus, elle reste constante. Ce résultat recherché s'explique par le fait que les bouffées d'énergie apportées par
> l'amplificateur opérationnel au cours du temps compensent exactement les dissipations d'énergie en énergie thermique, ce
> qui favorise l'amplification des oscillations qui naissent dans le circuit RLC série (phase d'amorçage) pour se
> stabiliser très rapidement sous forme quasi-sinusoïdale à une fréquence égale à la fréquence propre
> **N₀ = 1/(2π√LC)** de l'oscillateur, c'est-è-dire [sic] exactement comme si l'oscillateur RLC série n'a aucune
> résistance. On dit que les oscillations sont ainsi auto-entretenues. Mais, dans la pratique, on n'a le régime entretenu
> qu'à R' légèrement supérieure à (R₀+r). Cela est dû essentiellement à des imperfections de l'amplificateur opérationnel
> (il n'est pas parfaitement idéal comme il est supposé), aux perturbations provoquées par l'oscilloscope utilisé comme
> appareil de mesure et au fait que la résistance r de la bobine ne reste pas constante, elle augmente avec la fréquence
> des oscillations. »

> **Cas R' > R (p.117)** — « La résistance totale R_t devient remarquablement négative. Dans ce cas, dE/dt > 0 : le
> montage de l'amplificateur opérationnel apporte plus d'énergie qu'il en faut pour l'entretien des oscillations, ce qui
> explique l'augmentation de leur amplitude. »

> **Cas R' >> R (p.117)** — « Lorsque la résistance R' devient trop élevée, on atteint la saturation pour une valeur de
> l'intensité du courant oscillant inférieure en valeur absolue à sa valeur maximale. Par suite, l'amplificateur
> opérationnel ne peut plus continuer à ne fonctionner qu'en régime linéaire. En conséquence, les oscillations entretenues
> deviennent distordues et écrêtées. »

> **Conclusion (§3.2, p.117, encadré)** — « Un dipôle à résistance négative joue le rôle de générateur mais non autonome.
> Les oscillations d'un circuit RLC série ne peuvent être entretenues par un dipôle à résistance négative que lorsque
> l'énergie apportée par ce dernier suffit pour compenser l'énergie dissipée dans l'oscillateur par effet Joule. »

> **L'essentiel (p.118, VERBATIM)** — « ■ L'entretien des oscillations nécessite un apport extérieur d'énergie en
> bouffées. ■ Les oscillations libres d'un circuit RLC série peuvent être entretenues avec un dipôle à résistance
> négative. ■ Avec un montage particulier d'un ensemble de résistors autour d'un amplificateur opérationnel, on peut
> réaliser un dispositif d'entretien simulant un dipôle à résistance négative. ■ L'amorçage des oscillations entretenues
> d'un circuit RLC série demande une résistance négative lègérement [sic] supérieure en valeur absolue à la résistance
> totale de l'oscillateur. ■ Dans certaines limites, les oscillations quasi-sinusoïdales d'un circuit RLC série entretenu
> sont d'autant plus amples que l'apport d'énergie assuré par le dipôle à résistance négative est plus grand. ■ Les
> oscillations entretenues d'un dipôle à résistance négative ne peuvent être stabilisées que lorsque l'amplificateur
> opérationnel du dispositif d'entretien fonctionne en régime linéaire. ■ Les oscillations entretenues d'un circuit RLC
> série sont quasi-sinusoïdales de période égale à sa période propre » — l'encadré **T₀ = 2π√LC** est imprimé à la fin de
> la 5ᵉ puce (« … est plus grand. [T₀ = 2π√LC] ») au lieu de clore la dernière : mise en page fautive.

### Exercices résolus

- **Exercice résolu (p.119–120)** — Énoncé : RLC série, C = 2 μF, L = 0,5 H, r = 24 Ω ; montage de la Fig.6 p.114 mais R'
  réglable par une boîte (n × 1 kΩ) seulement. 1°) parmi trois oscillogrammes (1 : sinusoïde de faible amplitude ;
  2 : sinusoïde écrêtée, quasi rectangulaire ; 3 : sinusoïde ample), celui obtenu avec R' = 2 kΩ, justifier ; 2°) a) valeur
  de R' permettant théoriquement l'entretien, justifier ; b) fréquence des oscillations entretenues ; 3°) a) montrer
  qu'avec cette boîte on ne peut entretenir les oscillations, proposer une solution pratique ; b) avec la seule boîte
  (n × 1 kΩ), proposer une autre méthode améliorant la qualité des oscillations. Solution : 1°) R' = 2 kΩ trop supérieure à
  r = 24 Ω → l'A.O. apporte « beaucoup plus d'énergie qu'il en faut » → oscillations distordues → **oscillogramme 2** ;
  2°a) compensation de toute dissipation par effet Joule « chose qui n'est réalisée que lorsque R' = r » ; 2°b) le
  dispositif aide le circuit à osciller « librement », à sa fréquence propre **N₀ = 1/(2π√LC)**, « A.N: N = 159Hz » ;
  3°a) R'min = 1 kΩ encore très supérieure à 24 Ω → oscillations distordues ; remplacer par une association en série de
  boîtes (n × 1 Ω, n × 10 Ω, n × 100 Ω) ; 3°b) une augmentation de la valeur commune de R₁ et R₂ réduit la largeur du
  domaine linéaire (« manipulation de la page 112 ») → choisir R₁ = R₂ plus petites, R' fixée à 1 kΩ.

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux (p.121)** : 1- « L'amplificateur opérationnel est un dipôle à résistance négative. » ;
  2- « On ne peut entretenir les oscillations d'un circuit RLC série que par l'insertion d'un dipôle à résistance
  négative. » ; 3- « Un circuit LC ne demande aucun entretien. » ; 4- « Le dispositif d'entretien des oscillations joue le
  rôle du générateur. » ; 5- « L'entretien des oscillations permet à un circuit RLC série d'osciller sans diminution
  d'amplitude et à son propre rythme. » ; 6- « Quelle que soit la valeur de la résistance négative du dispositif
  d'entretien, les oscillations sinusoïdales d'un circuit RLC série se produisent à la même fréquence. » (Pas de réponse
  imprimée.)
- **Ex. 2 — QCM, une ou plusieurs réponses justes (p.121)** : I- oscillateur entretenu lorsque : a- aucune perte
  d'énergie ; b- pertes dues à sa résistance compensées par un apport d'énergie de l'extérieur ; c- perpétuation assurée
  par un dispositif d'entretien appropriè [sic] ; d- oscillations sinusoïdales. II- oscillations entretenues d'un RLC
  série : a- amplitude dépendant des caractéristiques du dispositif d'entretien ; b- pour toute résistance négative
  supérieure ou égale en valeur absolue à R ; c- fréquence imposée par le dispositif d'entretien ; d- fréquence égale à
  sa fréquence propre. III- RLC série + dipôle à résistance négative R' : oscillations seulement lorsque : a- condensateur
  chargé au préalable ; b- R' réglable et de valeur maximale supérieure à R ; c- condensateur de très grande capacité.
  (Pas de réponse imprimée.)

### Exercices et problèmes

- **Ex. 3 (p.121)** — RLC série + dipôle D (−R'). 1°) schéma avec u = − R'i ; 2°) oscillations quasi-sinusoïdales de u pour
  R' = 250 Ω, T = 6 ms, U_m = 2 V : a) propriétés de i ; b) C = 15,5 μF → L ; c) valeur théorique de la résistance R de la
  bobine, justifier.
- **Ex. 4 (p.122)** — dipôle (−R) réglable, C réglable en série avec bobine (L, r) ; oscillations obtenues avec
  C = 0,5 μF, R = 470 Ω ; C = 10 μF, R = 380 Ω ; C = 150 μF, R = 250 Ω. 1°) fréquence en fonction de L et C ; 2°) montrer
  que r n'est pas constante et augmente avec la fréquence.
- **Ex. 5 (p.122)** — A.O. idéal, générateur idéal E = 6 V, résistors R = 120 Ω, R₀ (×2 : rétroaction et S–D) et R' ;
  schéma : GBF « E » [sic : générateur noté BF sur le schéma], R, ampèremètre A, dipôle u ; 1°) u = − R'i ; 2°) ampèremètre
  I = 200 mA → R' ; 3°) a) convient-il pour C = 0,5 μF, L = 0,5 H, r = 50 Ω (« résistancer » [sic]) ? b) période.
- **Ex. 6 (p.122)** — R₀, C₀, bobine (L₀, r) entretenus par (−R). 1°) schéma ; 2°) à l'amorçage, montage équivalent
  théoriquement à C₀ initialement chargé en série avec une bobine purement inductive L₀ ; 3°) en régime permanent,
  oscillations sinusoïdales de fréquence N₀ (expression) ; 4°) a) énergie totale en fonction de L₀ et I_m ; b) origine
  de cette énergie.
- **Ex. 7 (p.122)** — chronogramme de u aux bornes du condensateur d'un RLC entretenu, 5 ms/div (amplitude croissante sur
  ≈ 3,3 div, soit ≈ 15–17 ms, puis constante). 1°) début d'enregistrement ≈ fermeture : a) interpréter énergétiquement ; b) durée
  approximative d'amorçage ; 2°) période T ; 3°) comparer à la période propre ; C = 2,53 μF ; L = 0,25 H.
- **Ex. 8 (p.122–123, synthèse)** — circuit (L, r)–C–interrupteur K, condensateur initialement chargé. 1°) décrire
  qualitativement après fermeture ; 2°) si r = 0, oscillations sinusoïdales de période T₀ ; 3°) K remplacé par un
  générateur G de tension u = k i : a) k a la dimension d'une résistance ; b) équation différentielle en i ; c) signe de k
  pour compenser r ; d) valeur de k pour des oscillations entretenues.
- **Ex. 9 (p.123)** — Fig.1 : R₁ = R₂ = 5 kΩ ; R' boîtes (n × 1 Ω ; n × 10 Ω) ; L = 0,5 H ; r = 50 Ω ; C = 35 μF ou 85 μF
  (« le chiffre des dizaines peut être 8 ou 3 ») ; K₁ (charge par une pile), commutateur K₂ (A : circuit libre ; B :
  dispositif d'entretien). 1°) K₁ fermé puis ouvert, K₂ en A ; 10 ms/div, 2 V/div ; Fig.2 (oscillations amorties) :
  a) commenter ; b) pseudopériode T ; c) montrer que C ne peut être que 35 μF. 2°) R' = 25 Ω, K₂ en B, A.O. alimenté :
  aucun oscillogramme ; a) attendu ? pourquoi ? b) réglage argumenté ; c) parmi trois oscillogrammes (Fig.3,
  10 ms/div), celui réellement obtenu, justifier.
- **Ex. 10 (p.123–124)** — C, bobine (L, r), dispositif A.O. idéal + R, R₁, R₂ (Y aux bornes de C). 1°) équivalent à (−R)
  seulement si R₂ = R₁ ; 2°) R₁ = R₂, sinusoïde T = 2,5 ms, U_m = 4 V : a) comparer r et R ; b) i(t) avec C = 0,5 μF ;
  c) L ; d) énergie totale.
- **Ex. 11 — Étude de texte « Montre à quartz » (p.124)** — piézoélectricité du quartz ; lamelle de quartz, fréquence ne
  dépendant que de sa masse et de sa rigidité, « entre 32 et 33 kHz » ; précision (moins d'une minute par an, moins d'une
  seconde par jour) ; pile bouton, ≈ 5 μW. Questions : 1°) analogie grandeurs RLC série / oscillateur à quartz ;
  2°) facteurs de la fréquence → fréquence propre ; 3°) montrer que la lamelle effectue des oscillations entretenues.

### Réponses du manuel (p.393, colonne gauche « Chapitre 4 »)

« 3. 2°a) i(t) = I_m sin2πNt, avec I_m = 8 mA ; 2°b) L = 58,8 mH ; c) R ≤ 250 Ω, car les oscillations sont
autoentretenues pour R'min = R. » · « 4. 1°) N = 1/(2π√LC) 2°) Plus C est grande, plus N et R sont petites. Donc, r
augmente avec N. » · « 5. 2°) R' = R - E/I = 90 Ω ; 3°a) Oui, car R' > r ; 3°b) T= 3,14 ms. » · « 6. 2°) A l'amorçage, la
résistance négative est égale à (- R₀ - r). Donc, le circuit est équivalent à un dipôle LC. 2°) [sic, pour 3°)] Expression
de N₀ est celle de 1°) de l'exercice 4. 4°a) E = (1/2)U_m² [sic] ; 4°b) E provient du dispositif d'entretien (dipôle à
résistance négative). » · « 7. 2°b) [sic, pour 1°b)] 25 ms ; 2°) T = 5 ms ; 4°) [sic, pour 3°)] T_th = 4,994 ms. Donc, T
est pratiquement égale à T_th. » · « 8. 1°) Oscillations libres ; 2°) T₀ = (LC)^1/2 [sic] ; 3°a) k a la dimension du
quotient U/I qui est celle d'une résistance ; 3°b) d²i/dt² + (r + k).di/dt + (1/LC).i = 0 [sic : 1/L manquant devant
(r + k)] ; 3°c) k < 0 ; 3°d) k ≤ - r » · « 9. 1°a) Oscillations libres amorties ; 1°b) T = 30 ms ; 1°c) C < T²/4π²L =
45,6.10⁻⁶ F. Donc, C = 35 μF ; 2°a) Oui, car R' < r ; 2°b) Augmenter R' car elle est inférieure à r ; 3°c) [sic, pour
2°c)] Oscillogramme (2) dont T = T₀ » (sur l'image, la ligne « 1°c) … 2°a) … 2°b) » est partiellement masquée par un
bandeau bleu ; lue en couche texte) · « 10. 1°) u = - R.(R₁/R₂).i. Donc, il faut R₁ = R₂ pour avoir u = - Ri ; 2°a) R > r ;
2°b) Avec u_C = U_Cm.sin2π t/T, i = dq/dt = I_m sin(2π t/T + π/2), où I_m = (2π/T) CU_m = 5 mA. 2°c) L = T²/4π²C = 317 mH ;
2°d) E = (1/2)U_m² [sic] = 3,96.10⁻⁶ J. »
Aucune réponse pour les ex. 1, 2 et 11.

### En savoir plus / Documents

- **Fiche technique (p.125–127) « Réalisation pratique d'oscillations électriques entretenues »** —
  (a) *Caractéristique u = f(i) point par point* : générateur 15 V (celui qui alimente l'A.O.) + rhéostat (0–1 kΩ) à la
  place du GBF, milliampèremètre en série avec un résistor (imprimé « R₀ = 220 Ω » dans le texte, « R » sur la Fig.1),
  voltmètre entre A et M [la Fig.1 nomme B le point de masse] ; R'₁ = 20 Ω ; pente du segment central k = − R'₁, donc
  u = − R'₁i pour i de − I₀ à + I₀ (Fig.2, caractéristique en N, ±U₀₁, ±I₀₁) ; deuxième voltmètre : u_s = − 15 V pour
  i ≤ − I₀, + 15 V pour i ≥ + I₀ ; R'₂ = 40 Ω (Fig.3). Conclusion : « Pour - I₀ < i < + I₀ tel que u donne
  - U_sat < u_s < + U_sat, le montage de l'amplificateur opérationnel est équivalent à un dipôle à résistance négative
  (-R') inséré entre les points A et M : u = -R'i » ; « Plus R' est grande, plus le domaine de linéarité est étroit. » ;
  Remarque : R₁ = R₂ portées de 1 kΩ à 10 kΩ → même effet que l'augmentation de R'.
  (b) *Influence des caractéristiques d'entrée de l'oscilloscope (p.127)* : entrée ≡ R_osc = 1 MΩ en parallèle avec
  C_osc de 16 à 47 pF (Fig.4) ; au lieu de d²u_c/dt² + ((R₀ + r − R')/L) du_c/dt + ω₀²u_c = 0, en négligeant C_osc devant
  C : d²u_c/dt² + [1/(CR_osc) + (R₀ + r − R)/L] du_c/dt + ω₀²[1 + (R₀ + r − R')/R_osc] u_c = 0 [sic : « R » au lieu de R'
  dans le premier crochet, image] ; démarrage si 1/(CR_osc) + (R₀ + r − R')/L ≤ 0, soit **R' ≥ R₀ + r + L/(CR_osc)** ;
  choisir L petite et C grande (petit quotient L/C) ; contre-exemple : R₀ + r = 250 Ω, R_osc = 1 MΩ, L = 1 H, C = 1 mF →
  L/(R_osc C) = 4(R₀ + r) ! → amorçage pour R' = 1250 Ω [?] (avec C = 1 mF, L/(R_osc C) = 10⁻³ Ω ; la valeur
  annoncée suppose C = 1 nF : coquille probable mF/nF). Renvoie à la fiche technique du chapitre précédent (p.108–109).
- **En savoir plus (p.128–129) « Amorçage et stabilisation des oscillations entretenues »** — en convention générateur
  u = R'i ; puissance p = − u.i = − R'i² < 0 ; « u = k i, où k est une constante ayant la dimension d'une résistance :
  k = R. » ; amorçage (ou accrochage) sans charger le condensateur (renvoi « figure 6 (p. 118) » [sic : la Fig.6 est
  p.114]) ; dans le modèle linéaire l'amplitude augmenterait indéfiniment → la stabilisation exige des éléments non
  linéaires ; A.O. linéaire si ε = V_E+ − V_E- = 0, − 15 V < u_s < + 15 V, sinon saturation ± U_sat ; en régime linéaire
  u_s = − (R' + R₂)i ; avec R₂ = R₁ : **u = R'/(R' + R₁) · u_s**, − U_sat < u_s < + U_sat ; condition sur u :
  − R'/(R'+R₁)·U_sat < u < + R'/(R'+R₁)·U_sat ; condition sur i : **− I₀ < i < + I₀, I₀ = U_sat/(R' + R₁)** ; au-delà,
  oscillations « pratiquement rectangulaires » ; si R' (ou R₁) augmente, I₀ diminue. Illustration graphique (p.129) :
  régime linéaire u = − R'i (1) ; saturation ε > 0 : u = + U_sat + R₁i (2) ; ε < 0 : u = − U_sat + R₁i (3) ;
  caractéristique en N, et graphe de la pente (axe imprimé « du/dt » [sic : lire du/di]) valant R₁ en saturation et − R'
  entre − I₀ et I₀ : « puits de résistance négative » ; « la stabilité des oscillations est assurée par l'existence de ce
  puits ».

### Écart avec la référence (aucun chapitre équivalent ; voisins sciences-exp/03 et 04)

- **Correspondance** : confirmée « aucune ». Le chapitre 03 publié (oscillations libres) et sa fiche §2.3 déclarent
  explicitement l'entretien **EXCLU** (« entretien des oscillations (résistance négative, amplificateur) : absent ») ;
  le chapitre 04 (forcées) ne traite pas d'entretien électrique. Seuls les prérequis (RLC série libre, T₀, N₀,
  E = E_C + E_L, dE/dt = − Ri²) recouvrent sciences-exp/03 : chapitre **à créer** en s'appuyant sur 03 pour les rappels.
- ✅ **À ajouter (propre à ce manuel)** : principe d'entretien par un dipôle de tension u = − Ri ; **dipôle à résistance
  négative** réalisé par un A.O. idéal (ε = 0, i⁺ = i⁻ = 0), R₁ = R₂, démonstration u = − R'i par mailles et nœuds ;
  caractéristique **en N** (mode XY, voie inversée ; pente, domaine linéaire, influence de R' et de R₁ = R₂) ; montage
  d'entretien d'un RLC série ; amorçage pour R' légèrement > R₀ + r ; oscillations **quasi-sinusoïdales à N₀** ;
  amplitude croissante avec R' ; écrêtage/saturation ; équation **q/C + L di/dt + R_t i = 0, R_t = R₀ + r − R'** ;
  **dE/dt = − R_t i²** et discussion des quatre cas ; dipôle à résistance négative = « générateur non autonome » ;
  apport d'énergie « en bouffées » ; montre à quartz (piézoélectricité), horloge atomique ; en exercices : générateur
  u = k i (k ≤ − r), r qui augmente avec la fréquence, lecture d'un chronogramme d'amorçage, choix d'une boîte de
  résistances, I_m = (2π/T)CU_m, énergie totale ½LI_m² = ½CU_m².
- ⛔ **Rien à retirer** (pas de référence) ; mais ne pas reprendre de sciences-exp/03 la résolution, Q, etc. (déjà exclus
  là-bas).
- **Vocabulaire / notations propres** : « dispositif d'entretien », « résistance négative (−R') », « amorçage »
  (« accrochage »), « auto-entretenues », « bouffées d'énergie », « R_t » résistance totale, « E » (énergie totale, lettre
  ronde), « N₀ » fréquence propre, « R₀ » résistor additionnel, « ε » tension d'entrée différentielle de l'A.O., « U_sat »,
  « puits de résistance négative ».

### Bornes de scope

- ✅ **INCLUS** : principe d'entretien (compensation de u_R) ; dipôle à résistance négative à A.O. (réaction sur l'entrée
  inverseuse ; mention de la réaction sur l'entrée non inverseuse, instable) ; établissement de u = − R'i (A.O. idéal,
  R₁ = R₂) ; caractéristique en N, domaine linéaire et son rétrécissement quand R' ou R₁ = R₂ augmentent ; montage
  d'entretien d'un RLC série ; conditions R' < R (amorties, rien), R' = R (entretien théorique), R' > R (amplitude
  croissante), R' >> R (distorsion, écrêtage) ; amorçage réel pour R' un peu > R (imperfections de l'A.O., oscilloscope,
  r qui varie) ; période des oscillations entretenues = T₀ = 2π√LC, N₀ = 1/(2π√LC) ; équation différentielle avec R_t et
  bilan dE/dt = − R_t i² ; calculs d'exercices (L, C, T, N₀, R', I_m, énergie totale, condition k ≤ − r) ; lecture
  d'oscillogrammes (période, durée d'amorçage, oscillogramme écrêté) ; montre à quartz (texte).
- ⛔ **EXCLU** : influence de la fréquence sur la résistance de la bobine (« hors programme », note p.117 — en exercice 4
  seulement de façon qualitative) ; impédance d'entrée de l'oscilloscope et condition R' ≥ R₀ + r + L/(CR_osc) (fiche
  technique seulement) ; étude de la saturation, I₀ = U_sat/(R' + R₁), « puits de résistance négative » (En savoir plus,
  non exigible) ; résolution de l'équation différentielle ; autres dispositifs d'entretien (oscillateurs à réaction,
  quartz détaillé) ; entretien mécanique.

### Lecture

- **Pages lues en L1** : 109 (fin du chapitre 3, pour la borne), 110 à 129 (les 20 pages), 130 (borne), 393 (réponses).
- **Pages lues sur l'image** (110 dpi) : 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127,
  128, 129, 393 ; p.110 et p.121 vues sur l'image par la relecture R-7 (auditeur B), conformes : le chapitre est
  désormais entièrement vu sur l'image.
- **Écarts texte/image** : p.111 légende inclinée illisible en L1 ; p.115, p.116, p.118, p.120 « T₀ = 2π√LC » et
  « N₀ = 1/(2π√LC) » rendus « T = 2 LC », « No = 1 / 2 LC » (π et √ perdus) ; p.116 « E » rond de l'énergie rendu « EE » ;
  p.126 ≤/≥ perdus ; p.127 toutes les équations déstructurées (« (Ro + r  R ') », « R'  Ro + r + L/CRosc ») ; p.128
  fractions R'/(R'+R₁) éclatées ; p.129 schéma du puits absent du texte ; p.393 √ perdu, ligne masquée de l'ex. 9.
- **Coquilles [sic]** : p.113 « cractéristique » ; p.114 « cournat », Fig.2a résistor de rétroaction marqué « R » (lire
  R₁), (3)' « I₁ » et (4)' « I' » en majuscules ; p.115 « écrétage », « permanant » ; p.117 « c'est-è-dire » ; p.118
  « lègérement » et encadré T₀ mal placé ; p.120 « osillogrammes », « q'une » ; p.121 « appropriè », « trés » ; p.122
  « résistancer », « énegétiquement » ; p.125 « réhostat », R₀ (texte) / R (figure), A et M (texte) / A et B (figure) ;
  p.127 « (R₀ + r − R) » au lieu de R' ; p.128 « figure 6 (p. 118) » (Fig.6 est p.114), « élèments », « si i > I₀ » (lire
  |i| > I₀) ; p.129 axe « du/dt » (lire du/di) ; p.393 numérotations erronées des questions (ex. 6, 7, 9), « E = (1/2)U_m² »
  sans C (ex. 6, ex. 10 ; la valeur 3,96·10⁻⁶ J correspond à ½CU_m² ≈ 4·10⁻⁶ J), « T₀ = (LC)^1/2 » sans 2π (ex. 8), 1/L
  manquant dans l'équation de l'ex. 8.
- **Doutes [?]** :
  - [?] 1 — **§3.1, Fig.7b** : L = 1 H, C = 47 μF donnent T₀ = 2π√(47·10⁻⁶) ≈ 43 ms ; l'oscillogramme (10 ms/div) montre
    des crêtes espacées de ≈ 2 div (≈ 20 ms) — incohérence probable entre données et figure ; le manuel ne donne pas la
    valeur mesurée. Ne pas en tirer de valeur.
  - [?] 2 — **§3.1** : R₀ = 2 kΩ et amorçage à « 2070 Ω environ » (> R₀ + r ≈ 2025 Ω) cohérent ; mais R₀ = 2 kΩ est très
    grand pour un RLC (régime libre apériodique : 2√(L/C) ≈ 292 Ω) — sans conséquence sur le texte, à ne pas exploiter en
    exercice de régime libre.
  - [?] 3 — **Ex. résolu 2°a** : réponse « R' = r » alors que la Fig.6 comporte R₀ ; l'énoncé ne mentionne pas R₀
    (« montage de la figure 6 … mais avec R' réglable ») — on suppose R₀ absent.
  - [?] 4 — **Ex. 7** : 1 période = 1 div = 5 ms (T ≈ 5 ms, conforme) ; les crêtes croissent jusqu'à la 4ᵉ et le régime
    est stable à partir de ≈ 3,3 div, soit une durée d'amorçage ≈ 15–17 ms, alors que la réponse imprimée donne « 25 ms »
    — à trancher.
  - [?] 5 — **Fig.3 (p.113)** : aucune valeur de pente ni de k n'est donnée ; la réponse attendue (k = − R') n'est imprimée
    qu'implicitement (conclusion u = − R'i).
  - [?] 6 — **Fiche technique p.127** : contre-exemple chiffré faux tel qu'imprimé (C = 1 mF au lieu de 1 nF probable) ;
    par ailleurs la « Fig.4 » de la p.127, censée montrer l'entrée de l'oscilloscope (R_osc ∥ C_osc), reproduit le montage
    de mesure de u = f(i) (Fig.1 p.125). Fiche technique EXCLUE de l'exigible.
- **Doutes levés (relecture R-7)** :
  - **Ex. 9** : mesure au zoom de la Fig.3 (10 div) : (1) crêtes à ≈ 4 div → T ≈ 40 ms ; (2) ≈ 3 div → T ≈ 30 ms ;
    (3) ≈ 2 div → T ≈ 20 ms. (2) a la période de la Fig.2 (3 div = 30 ms) et est le plus proche de T₀ = 26,3 ms : la
    réponse imprimée « Oscillogramme (2) dont T = T₀ » est **juste** (mon comptage initial en périodes visibles était
    erroné).
  - **Ex. 5** : « R' = R − E/I = 90 Ω » se démontre avec le cours : loi des mailles E = RI + u = RI − R'I, d'où
    R' = R − E/I = 120 − 6/0,2 = 90 Ω. Réponse juste.

## 2.5 Chapitre 5 — Oscillations électriques forcées en régime sinusoïdal (manuel 223471, p.130–157)

**Plage vérifiée** : objectifs/prérequis p.130 ; ouverture n° 5 p.131 ; cours p.132–145 ; L'essentiel p.146 ; Exercices
p.147–155 ; Fiche technique p.156 ; En savoir plus p.157 (la p.158 est la page d'objectifs du chapitre 6). Bandeau :
« Evolution de systèmes ◆ Oscillations électriques forcées en régime sinusoïdal ».
**Constat général** : le texte du cours, ses figures, ses valeurs (C = 0,47 μF, L = 0,2 H, r = 12,5 Ω, N₀ = 520 Hz,
tableau U_Cm 40/21/6,5…), son exercice résolu et la plupart des exercices sont **les mêmes** que ceux du chapitre 4 du
manuel 223433 (fiche bac-sciences-exp §2.4), **amputés de tout ce qui concerne la charge q(t)** : déphasage i/q,
amplitude Q_m, résonance de charge, réponse linéaire, montage u_C du §1.1.

**Objectifs (p.130, VERBATIM)** — « Distinguer, en régime forcé, le résonateur de l'excitateur. » · « Visualiser
simultanément à l'oscilloscope la tension excitatrice u(t) et l'intensité du courant i(t). » · « Mesurer l'amplitude et la
fréquence d'une grandeur oscillante en régime forcé sinusoïdal. » · « Déterminer le déphasage entre la tension excitatrice
u(t) et l'intensité du courant i(t). » · « Mettre en évidence expérimentalement le phénomène de résonance d'intensité. » ·
« Établir l'expression de l'intensité maximale I_m du courant oscillant en fonction de la fréquence des excitations. » ·
« Interpréter théoriquement le phénomène de résonance. » · « Calculer la puissance moyenne absorbée par un oscillateur
électrique. » · « Expliquer l'importance du facteur de puissance dans les transformations de l'énergie électrique. »
(Par rapport à 223433 : disparaissent « et celui de la résonance de charge », « Etablir en i(t) ou en q(t), l'équation
différentielle… » et « … et en déduire celle de la charge maximale Q_m ».)

**Prérequis (p.130)** — SAVOIR : Définir un oscillateur. · Caractériser une grandeur oscillante sinusoïdale par sa période,
son amplitude et sa phase initiale. · Écrire les relations : T = 2π/ω et N = 1/T. · Définir les valeurs maximale I_m et
efficace I de l'intensité du courant alternatif. · Définir les valeurs maximale U_m et efficace U d'une tension alternative.
· Ecrire les relations : I_m = I√2 et U_m = U√2. · Ecrire les relations : E_c = q²/2C et E_L = ½ L.i². SAVOIR FAIRE :
Reconnaître un oscillateur. · Visualiser à l'oscilloscope : une tension électrique, une intensité de courant. · Déterminer
graphiquement la période et l'amplitude d'une grandeur électrique oscillante. · Calculer la période propre d'un oscillateur
RLC série. · Établir l'équation différentielle régissant les oscillations libres d'un circuit RLC série par application de
la loi des mailles. · Calculer l'énergie totale d'un oscillateur RLC série.

**Page d'ouverture (p.131)** — « OSCILLATIONS ÉLECTRIQUES FORCÉES EN RÉGIME SINUSOÏDAL », n° 5 ; photo de guitare
électrique ; légende (inclinée, confirmée sur l'image par la relecture R-7) : « La guitare électrique est munie d'une caisse creuse à laquelle sont
adjoints des microphones électromagnétiques. Grâce à la résonance électrique, le son amplifié prime sur la résonance
naturelle de la caisse. » Questions (VERBATIM) : « En quoi consiste la recherche manuelle ou automatique d'une chaîne radio
ou d'un canal de télévision? » · « Que veut-on dire par “résonance électrique” dont les applications sont trés [sic]
nombreuses ? »

**Plan** — titre p.132 « OSCILLATIONS ÉLECTIRQUES [sic] FORCÉES EN RÉGIME SINUSOÏDAL » ; introduction · **1** Réponse d'un
circuit RLC série à une tension sinusoïdale (1.1 Production d'oscillations forcées, p.132–134 ; 1.2 Déphasage, p.134–135 —
sans sous-paragraphe 1.2.2) · **2** Influence de la fréquence d'excitation sur la réponse d'un circuit RLC série
(p.135–139 : manipulation ; interprétation théorique — I_m et φ par Fresnel ; résonance d'intensité) · **3** Influence de la
résistance totale du circuit sur la résonance (p.139–140) · **4** Le phénomène de surtension (p.140–141) · **5** Applications
de la résonance (p.141–142) · **6** Puissance moyenne et facteur de puissance (6.1 Puissance électrique instantanée ;
6.2 Puissance électrique moyenne ; 6.3 Résonance de puissance ; 6.4 Transfert de puissance moyenne ; 6.5 Importance du
facteur de puissance cosφ ; p.142–145) · L'essentiel (p.146) · Exercices : résolu (p.147–149) ; Tests rapides (1 V/F,
2 QCM, p.150) ; Exercices d'application (3–11, p.151–153) ; Exercices de synthèse (12–15, p.153–155) ; 16 Étude de texte
(p.155) · Fiche technique « Construction de Fresnel » (p.156) · En savoir plus « Générateur de courant haute fréquence »
(p.157).

### Cours — Activités

- **Introduction (p.132, VERBATIM)** — « On a vu dans le chapitre précédent que si un circuit RLC série peut effectuer des
  oscillations libres, celles-ci cessent plus au moins rapidement à cause de l'amortissement dû à sa résistance. Quel sera
  l'effet de l'application d'une tension sinusoïdale aux bornes d'un tel oscillateur, une simple compensation de
  l'amortissement ou plus ! » [« chapitre précédent » : ici le chapitre 4 est l'entretien ; le texte est repris du manuel
  223433 où le chapitre précédent était les oscillations libres.]
- **§1.1 Manipulation (p.132–133)** — Fig.1 : GBF entre A et M, interrupteur K, C, bobine (L, r), R₀ réglable entre B et M ;
  u(t) = U_m.sinωt, U_m constante ; R₀ réglable, C = 0,47 μF, L = 0,2 H, r = 12,5 Ω ; M à la masse, A → Y₁, B → Y₂ ;
  N = 400 Hz, U_m = 2 V, R₀ = 50 Ω « par exemple » ; K ouvert : seul l'oscillogramme (1) ; K fermé : (1) et (2) stables
  (Fig.2, 1 ms/div) ; à 400 Hz, mesures de U_R0m en fonction de U_m → Fig.3 (droite par l'origine ; U_R0m (V) 0–0,8 en
  ordonnée, U_m (V) 0–4 en abscisse, point final ≈ (4 V ; 0,6 V) ; légende « Tracé de U_m = f (U_R0m) » alors que l'axe
  vertical porte U_R0m). Questions (VERBATIM) : « 1°) Comparer la forme de l'oscillogramme représentant i(t) à celle de
  u(t). 2°) Mesurer la fréquence N de i(t) et la comparer à celle de u(t). 3°) Comparer la fréquence N à la fréquence propre
  No de l'oscillateur. 4°) a) A l'aide de la courbe de la figure 3, montrer que : U_m = kU_R0m, où k est une constante que
  l'on calculera. b) Montrer que la tension maximale U_m peut s'écrire en fonction de l'intensité maximale I_m sous la
  forme : U_m = Z I_m où Z une constante dont on déterminera la dimension. » Commentaire et interprétation théorique : voir
  Encadrés. (Pas de montage u_C ni de question sur Q_m, contrairement à 223433.)
- **§1.2 Déphasage — exemples (p.134)** — Fig.4a (u₁, u₂ en concordance de phase), Fig.4b (opposition), Fig.5a (u₂ en
  quadrature retard sur u₁), Fig.5b (quadrature avance). Questions (VERBATIM) : « 1°) Justifier qualitativement
  l'appellation concordance de phase et opposition de phase. 2°) a) Montrer que la concordance de phase signifie Δφ = 2kπ
  rad, avec k entier relatif. b) Montrer que l'opposition de phase signifie Δφ = (π + 2kπ) rad, avec k entier relatif.
  3°) Dans les cas de la figure 5 où le décalage horaire Δt entre u₁ et u₂ est égale à T/4, on dit que u₂ et u₁ évoluent au
  cours du temps en quadrature de phase. Plus précisement, u₂ est en quadrature retard sur u₁ dans le cas de la figure 5a,
  tandis qu'elle est en quadrature avance sur u₁ dans le cas de la figure 5b. Expliquer cette différence par le calcul de Δφ
  dans les deux cas. 4°) Déduire des exemples traités précedemment que la valeur absolue du déphasage |Δφ| entre deux
  fonctions sinusoïdales isochrones est liée à leur décalage horaire Δt par la relation : |Δφ| = (2π/T)Δt »
- **§2 Manipulation — influence de N (p.135–136)** — montage Fig.1, u(t) = U_m sin2πNt, U_m = 2 V ; u_R0 reste sinusoïdale,
  U_R0m et Δt changent ; mesures de I_m et Δt en fonction de N → Fig.6a (I_m (mA) 0–32 en fonction de N (0–700 Hz), pic
  ≈ 31 mA vers 520 Hz) et Fig.6b (phase initiale φ (rad) de i : positive aux basses fréquences, nulle vers 520 Hz, négative
  au-delà ; axe sans graduation chiffrée) ; Remarque : suivre aussi I efficace à l'ampèremètre. Questions (VERBATIM) :
  « 1°) Montrer que, dans les conditions de l'expérience réalisée, la valeur de la phase initiale φ est égale à la valeur du
  déphasage entre i et u. 2°) Décrire la forme particulière de la courbe représentant I_m en fonction de N. 3°) a) Déterminer
  graphiquement la valeur de la fréquence N pour laquelle l'intensité maximale I_m du courant oscillant est à sa valeur la
  plus élevée I_m0 et la comparer à celle de la fréquence propre N₀ de l'oscillateur. b) Relever I_m0 et la valeur
  correspondante φ₀ de φ. c) Calculer l'impédance Z qu'a le circuit RLC dans ce cas particulier et la comparer à sa
  résistance totale (R₀+r). » (223433 étudiait en plus u_C et Q_m(N), Fig.9.)
- **§2 Interprétation théorique (p.136–138)** — Fresnel (renvoi à la fiche technique p.156) : voir Encadrés ; Fig.7a
  (Lω > 1/Cω, B sous l'axe, φ < 0), Fig.7b (Lω < 1/Cω, φ > 0), Fig.7c (Lω = 1/Cω, φ = 0).
- **§3 Manipulation — influence de R (p.139)** — L = 0,2 H, C = 0,47 μF, R₀₂ = 20 Ω et R₀₃ = 200 Ω [la valeur R₀₁ n'est pas
  citée ; R₀ = 50 Ω de la Fig.6a sert de référence] ; Fig.8a : I_m(N), courbe (1) pic ≈ 30 mA vers 520 Hz [?, cf. doutes],
  courbe (2) pic ≈ 8 mA ; Fig.8b : φ(N), courbes (a) et (b). Questions (VERBATIM) : « 1°) Comparer les allures des courbes
  de résonance (1) et (2) entre elles et avec celle de la courbe de la figure 6a ; en déduire l'influence de la résistance
  totale du circuit sur la résonance. 2°) Pour les valeurs R₀₂ et R₀₃ de R₀, déterminer graphiquement : a) la valeur de la
  fréquence de résonance, b) le déphasage φ correspondant entre l'intensité i et la tension d'alimentation u. »
  Interprétation : résonance aiguë (R très petite) / floue (R grande) — pas de « très floue » ni de résonance de charge.
- **§4 Manipulation — surtension (p.140)** — montage Fig.1 (p.132), L = 0,2 H, C = 0,47 μF, U_m = 2 V, N = N₀ = 520 Hz ;
  tableau R₀ (Ω) 20 / 50 / 200 → U_Cm (V) 40 / 21 / 6,5. Questions (VERBATIM) : « 1°) Reproduire, puis compléter le tableau
  suivant : [R₀ (Ω) 20, 50, 200 ; Q = U_Cm/U_m] 2°) Le quotient Q = U_cm/U_m est appelé facteur de surtension à la
  résonance. Justifier cette appellation. 3°) a) Montrer théoriquement que Q peut s'écrire uniquement en fonction des
  caractéristiques R, L et C de l'oscillateur. b) Calculer les valeurs théoriques de Q, correspondant respectivement aux
  valeurs 20 Ω, 50 Ω et 200 Ω de la résistance R₀. 4°) Quelle précaution faut-il prendre pour avoir un facteur de
  surtension modéré à la résonance ? » ; Remarque (p.141) : surtension aux bornes de la bobine (Fig.9, diagramme de
  Fresnel : R₀I, rI, Lω₀I, U_Bobine, I/(Cω₀) = U_C).
- **§5 Applications (p.141–142)** — oscillateurs à quartz ; haut-parleur et microphone électrodynamique ; réception
  d'émissions radiophoniques (poste radio : résonance aiguë, accord de la fréquence propre ; chaîne « haute fidélité » :
  courbes de résonance floue « les plus aplaties possibles »).
- **§6 Puissance (p.142–145)** — développement théorique sans manipulation (voir Encadrés) ; Fig.10 dipôle D entre A et B ;
  Fig.11 P (mW, 08–64) en fonction de N, pic ≈ 60 mW vers 520 Hz ; Fig.12 résonance aiguë (verte) et floue (orange) de P(N).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Commentaire (§1.1, p.133)** — « L'analyse des oscillogrammes de la figure 2 montre que, comme celle de u(t), la courbe
> représentant i(t) varie sinusoïdalement au cours du temps. De plus, il y a constamment le même décalage horaire entre les
> deux oscillogrammes. Par conséquent, l'intensité i(t) varie avec la même fréquence que la tension u(t) imposée par le GBF
> et non avec la fréquence propre du circuit RLC série : les oscillations imposées par le GBF ne sont plus libres, elles
> sont forcées. Ainsi, le GBF a joué le rôle d'excitateur. La forme linéaire de la courbe représentant U_R0m en fonction de
> U_m montre que le quotient U_m/I_m est une constante qui ne dépend que des caractéristiques de l'oscillateur. On l'appelle
> impédance du circuit et on la note Z. » (Pas de phrase sur l'unité ohm, présente dans 223433.)

> **Interprétation théorique (p.133)** — « Pour le circuit utilisé précédemment, la loi des mailles s'écrit :
> u_BM + u_DB + u_AD + (-u_AM) = 0, d'où u_AM = u_BM + u_DB + u_AD. Donc, u_AM = R₀.i + r.i + L di/dt + q/C, […] Or,
> q = ∫i.dt. Donc, **u_AM = R.i + L di/dt + (1/C)∫i.dt, où R = R₀ + r** et ω = 2πN. Une telle équation différentielle à
> second membre non nul admet comme solution particulière celle du régime permanent : **i(t) = I_m sin(ωt + φ).** »
> Remarque (p.134) : « La solution générale faisant apparaître de plus le régime transitoire qui ne dure qu'une très petite
> fraction de seconde est hors programme. » (Seule l'équation intégro-différentielle en i est écrite ; aucune équation en q.)

> **Conclusion (§1.1, p.134)** — « La réponse d'un circuit RLC série à une tension sinusoïdale est un courant alternatif
> sinusoïdal y oscillant : - à la fréquence N de la tension excitatrice, - avec une amplitude I_m = U_m /Z, où Z est une
> grandeur physique ayant la dimension d'une résistance appelée impédance du circuit RLC série. »

> **Définition (§1.2, p.134)** — « On appelle déphasage entre deux fonctions sinusoïdales de phases initiales φ₁ et φ₂ la
> différence de phase Δφ = (φ₂ - φ₁) ou (φ₁ - φ₂). » Exemples : « deux tensions u₁ et u₂ synchrones (de même période et
> simultanées) » ; Fig.4a « en phase ou en concordance de phase », Fig.4b « en opposition de phase ».

> **Conclusion (§1.2, p.135)** — « A tout décalage horaire Δt entre deux fonctions sinusoïdales y₁(t) et y₂(t) isochrones
> (de même péride [sic] T), représentées dans le même système d'axes, est associé un déphasage Δφ tel que :
> **|Δφ| = (2π/T)Δt**. - Si Δt = 0, Δφ = 0 : les deux fonctions sont en concordance de phase. - Si Δt = T/2, Δφ = ± π rad :
> les deux fonctions sont en opposition de phase. - Si Δt = T/4, Δφ = ± π/2 rad : les deux fonctions sont en quadrature de
> phase. Si le déphasage (φ₂ - φ₁) est positif, y₂(t) est en avance de phase par rapport à y₁(t) et inversement. »

> **Conclusion (§2, p.136)** — « En régime forcé sinusoïdal, l'intensité maximale I_m et la phase initiale φ du courant
> oscillant dans un circuit RLC série dépendent de la fréquence N de la tension excitatrice et des grandeurs R, L et C
> caractéristiques de l'oscillateur. La réponse d'un circuit RLC série à une tension sinusoïdale de fréquence N égale à la
> fréquence propre N₀ du circuit est un courant oscillant en phase avec la tension excitatrice et avec l'intensité maximale
> la plus élevée : c'est la résonance d'intensité. A la résonance d'intensité, le circuit RLC série se comporte comme un
> résistor de résistance R. »

> **I_m et φ par Fresnel (p.136–137)** — « On a : Ri + L di/dt + (1/C)∫i.dt = U_m sinωt, avec R = R₀ + r ; i(t) =
> I_m sin(ωt + φ). di/dt = ωI_m sin(ωt + φ + π/2) ; ∫i.dt = (I_m/ω) sin(ωt + φ − π/2) + cte. Il vient alors :
> RI_m sin(ωt+φ) + LωI_m sin(ωt+φ+π/2) + (I_m/Cω) sin(ωt+φ−π/2) + cte/C = U_m sin(ωt). Etant une fonction sinusoïdale,
> U_m sinωt ne peut être qu'une somme de fonctions sinusoïdales. Donc, cte = 0. • RI_m sin(ωt + φ) ↦ OA⃗₁ [RI_m, φ] •
> LωI_m sin(ωt + φ + π/2) ↦ OA⃗₂ [LωI_m, φ + π/2] • (I_m/Cω) sin(ωt+φ − π/2) ↦ OA⃗₃ [I_m/Cω, φ − π/2] • U_m sinωt ↦ OA⃗
> [U_m, 0] tel que : OA⃗ = OA⃗₁ + OA⃗₂ + OA⃗₃. Les vecteurs de Fresnel OA⃗₂ et OA⃗₃ étant de sens contraires, il en résulte
> trois constructions possibles : • ‖OA⃗₂‖ > ‖OA⃗₃‖, cas correspondant à Lω > 1/Cω c'est-à-dire N>N₀ : […] figure 7a.
> • ‖OA⃗₂‖ < ‖OA⃗₃‖, […] Lω < 1/Cω c'est-à-dire N<N₀ : […] figure 7b. • ‖OA⃗₂‖ = ‖OA⃗₃‖, […] Lω = 1/Cω c'est-à-dire N=N₀ :
> […] figure 7c. Dans le cas général, on a : U_m² = (RI_m)² + (LωI_m − I_m/Cω)², d'où U_m = √(R² + (Lω − 1/Cω)²) I_m.
> Donc, **I_m = U_m / √(R² + (Lω − 1/Cω)²)**, soit : **I_m = U_m/Z avec Z = √(R² + (Lω − 1/Cω)²)**. D'après le cas de la
> figure 7a, Lω > 1/Cω, on a φ < 0, ça signifie que l'intensité i(t) du courant est en retard de phase par rapport à la
> tension excitatrice u(t) : le circuit RLC série est dit inductif. D'après le cas de la figure 7b, Lω < 1/Cω, on a φ > 0,
> ça signifie que l'intensité i(t) du courant est en avance de phase par rapport à la tension excitatrice u(t) : le circuit
> RLC série est dit capacitif. D'après les constructions précédentes, on a : |tgφ| = |Lω − 1/Cω| / R. En tenant compte de la
> dépendance du signe de φ de celui de (Lω − 1/Cω), la phase initiale φ de i est telle que : **tgφ = (1/Cω − Lω)/R, avec
> − π/2 rad < φ < π/2 rad** » ; Remarque (p.138) : « Le déphasage φ entre i et u peut être aussi caractérisé par :
> **cosφ = R/Z** »

> **Résonance d'intensité (p.138)** — « L'impédance du circuit s'écrit Z = √(R² + (Lω − 1/Cω)²). Aux très basses pulsations
> ainsi qu'aux pulsations beaucoup plus élèvées [sic] que la pulsation propre ω₀ de l'oscillateur, l'écart entre Lω et 1/Cω
> augmente. Par suite, l'impédance Z devient de plus en plus grande. Donc, dans l'un ou dans l'autre cas, I_m(ω) = U_m/Z → 0,
> ce qui signifie que la réponse du circuit RLC série devient de plus en plus faible. Cette réponse s'améliore lorsque Z
> prend une valeur modérée, ce qui n'est possible qu'avec des valeurs comparables de Lω et de 1/Cω. Dans le cas particulier
> où Lω = 1/Cω obtenu avec ω = ω₀ = 1/√LC, l'impédance Z est minimale : Z = R. Par conséquent, l'intensité maximale prend sa
> valeur la plus élevée **I_m0 = U_m/R** : c'est la résonance d'intensité. tgφ = (1/Cω − Lω)/R = 0, ce qui signifie qu'à la
> résonance, la tension u et l'intensité i sont en phase. » Remarque : « L'appellation d'un oscillateur en régime forcé
> comme étant un résonateur revient au phénomène de résonance. » (Les puces sont imprimées « ∞ » : glyphe parasite.)

> **Conclusion (p.139, encadré)** — « La réponse d'un circuit RLC série à une tension sinusoïdale de fréquence N égale à la
> fréquence propre N₀ du circuit est un courant oscillant en phase avec la tension excitatrice et avec l'intensité maximale
> la plus élevée : c'est la résonance d'intensité. **N = N₀ = 1/(2π√LC) : Résonance d'intensité ⇔ { I_m est la plus élevée ;
> u et i sont en phase }** »

> **Interprétation §3 (p.139)** — « A la résonance d'intensité, on a I_mo = U_m/R. Cela signifie que l'importance de la
> résonance dépend de l'ordre de grandeur de R, donc de R₀ car R = R₀ + r : I_mo est d'autant plus grande que R est plus
> petite. - Si R est très petite, le maximum de I_m est très élevé, ce qui se traduit par un pic de résonance très pointu
> (courbe (1) de la figure 8a) : c'est la résonance aiguë. - Si R est grande, I_mo est faible, ce qui se traduit par un pic
> de résonance très peu prononcé (courbe (2) de la figure 8a) : c'est la résonance floue. »

> **Conclusion (§3, p.140)** — « La résonance d'intensité de courant d'un oscillateur RLC série est d'autant plus aiguë que
> l'amortissement est faible. Cependant, quel que soit l'amortissement, la fréquence de résonance reste toujours égale à la
> fréquence propre du résonateur. »

> **Expression de Q (§4, p.140–141)** — « Pour une pulsation ω égale à la pulsation propre ω₀, U_C = I₀/(Cω₀) et
> I₀ = U/(R₀ + r). D'où : **Q = 1/((R₀ + r) Cω₀)** (1). Or, 1/(Cω₀) = Lω₀. Donc, Q s'exprime autrement comme suit :
> **Q = Lω₀/(R₀ + r)** (2). En remplaçant ω₀ par 1/√LC dans (1) par exemple, il vient : Q = (1/((R₀ + r) C)) √LC. Donc :
> **Q = (1/(R₀ + r)) √(L/C)** » ; « Donc, le facteur de surtension Q augmente quand l'inductance L augmente et lorsque la
> capacité C et la résistance R du circuit diminuent. S'il est trop élevé, la surtension devient dangereuse tant pour
> l'utilisateur que pour les composants du circuit ou les appareils d'une manière générale : elle peut provoquer le
> claquage du condensateur et des étincelles entre les spires de la bobine, d'où le risque d'électrocution. » Remarque :
> « A la résonance d'intensité : U = (R₀ + r) I et U_Bobine = √(r² + (Lω₀)²) I. Si la valeur de l'inductance L est telle
> que, Lω₀ >> (R₀ + r), La valeur de la tension efficace aux bornes de la bobine sera plus grande que la valeur de la
> tension efficace d'alimentation. Donc, il y a aussi risque de surtension aux bornes de la bobine (Fig.9). »

> **Conclusion (§4, p.141)** — « - A la résonance d'intensité d'un circuit RLC série, il peut surgir aux bornes du
> condensateur, une surtension caractérisée par le facteur : **Q = (1/(R₀ + r)) √(L/C)** - Le facteur de surtension Q est
> d'autant plus grand que la résonance est plus aiguë. - Une surtension élevée peut entraîner des conséquences néfastes. »

> **Puissance instantanée (§6.1, p.142)** — « En appliquant à ses bornes A et B une tension sinusoïdale de basse fréquence
> u(t) = U√2 sin ωt, un dipôle D (Fig.10) sera parcouru par un courant d'intensité sinusoïdale i(t) = I√2 sin(ωt + φ) et
> recevra, à tout instant, une puissance électrique p s'écrivant en convention récepteur : p(t) = u(t).i(t). […]
> p = u.i = U√2 sin(ωt).I√2 sin(ωt + φ) = 2U.I.sin(ωt + φ) sin(ωt). En appliquant […] la relation trigonométrique
> sin a.sin b = ½[cos(a − b) − cos(a + b)], on aboutit à : **p = UIcosφ - UIcos(2ωt + φ).** On constate que la puissance
> instantanée est la somme algébrique du terme constant “UIcosφ” et du terme “-UIcos(2ωt+φ)” évoluant périodiquement au
> cours du temps avec une fréquence double de celle de u et de i, ce qui rend p(t) périodique de période **T_p = T/2**.
> Ainsi, pendant une demi oscillation de i, cos(2ωt+φ) varie entre +1 et -1. Par conséquent, p peut être positive et le
> dipôle RLC série est effectivement un récepteur. Puis, elle peut devenir négative et le même dipôle se comporte alors
> comme un générateur. Cependant, pour déterminer le bilan, ces constatations restent insuffisantes. »

> **Définition (§6.2, p.142–143)** — « La puissance moyenne d'un dipôle D est la valeur moyenne prise par sa puissance
> instantanée p(t) sur une très grande durée Δt (tendant vers l'infini). Lorsque p(t) est périodique, il est équivalent de
> prendre Δt égale à une période. On note la puissance électrique moyenne P et on l'appelle aussi en régime forcé
> sinusoïdal, puissance électrique active ou réelle. Comme toute puissance, la puissance moyenne s'exprime en watt (W) et
> se mesure avec un wattmètre. » Note marginale : « Le cas unique qui figure dans le programme est celui du régime
> sinusoïdal forcé. »

> **Expression de P (p.143–144)** — « **P = (1/T_p) ∫_{kT_p}^{(k+1)T_p} p(t)dt** où k est un entier naturel. […] Donc,
> P = (1/T_p)∫UIcosφdt − (1/T_p)∫UIcos(2ωt+φ)dt. Ce qui donne : P = (UIcosφ/T_p)[t] − (UI/(2ωT_p))[sin(2ωt+φ)]. La fonction
> sin(2ωt+φ) étant périodique de période T_p = 2/ω [sic, image : π absent, lire T_p = π/ω],
> on a : [sin(2ωt + φ)] = 0. Cependant, [t] = T_p. Il vient donc : **P = UIcosφ** » ; « Cette forme générale de
> l'expression de la puissance moyenne est indépendante de la nature du dipôle. Etant semblable à l'expression de la
> puissance consommée en courant continu, le produit UI intervenant dans l'expression de P est appelé puissance apparente
> du dipôle. La puissance apparente s'exprime en volt-ampère (V.A). Le facteur cosφ auquel la puissance moyenne est
> proportionnelle s'appelle facteur de puissance. Pour le circuit RLC série, cosφ =R/Z. Donc, ce facteur est toujours
> positif. Par suite, la puissance moyenne est positive, ce qui veut dire que le circuit RLC série se comporte dans
> l'ensemble comme un dipôle passif. D'autre part, on a U = Z.I, d'où : **P = R.I²** Ainsi, on montre que la puissance
> active d'un circuit RLC série est due à sa résistance totale R : c'est une puissance consommée par effet Joule. […] en
> moyenne, l'énergie transférée de l'excitateur à l'oscillateur sert, lorsque le régime oscillatoire est établi, à
> compenser les pertes par effet Joule. »

> **Résonance de puissance (§6.3, p.144)** — « La puissance moyenne (P = RI²) d'un circuit RLC série est proportionnelle au
> carré de l'intensité efficace du courant oscillant dans le circuit. il s'en suit une résonance de puissance à chaque fois
> qu'il y a résonance d'intensité (Fig.11). A la résonance d'intensité, P est maximale, ce qui est en accord avec la
> condition (cosφ = 1) établie précédemment. »

> **Transfert de puissance (§6.4, p.144)** — « **P = R U²/Z² = RU² / (R² + (Lω − 1/Cω)²)** » ; amortissement important :
> P quasi nulle pour ω → 0 ou ω très grand, « au voisinage de ω₀, P devient égale à U²/R » ; transfert faible → résonance
> floue ; amortissement faible : transfert important → résonance aiguë (Fig.12).

> **Facteur de puissance (§6.5, p.144–145)** — réseau STEG, puissance nominale ; **I = P/(U cosφ)** ; perte en ligne :
> « P₀ = R₀I², soit : **P₀ = R₀ P²/(U² cos²φ)** » ; « P et U étant imposées, pour minimiser P₀, il faut chercher à minimiser
> R₀ et augmenter cosφ » ; diminuer R₀ = câbles plus gros, plus lourds, plus chers ; « on exige qu'une installation
> électrique ait un facteur de puissance élevé (cosφ > 0,8). »

> **Conclusion (§6, p.145)** — « La puissance moyenne d'un circuit RLC série est dissipée par effet Joule. Cette
> dissipation se fait à n'importe quelle fréquence mais elle est d'autant plus importante que la résistance est plus
> grande. A la résonance d'intensité, correspond une résonance de puissance : la puissance moyenne de l'oscillateur RLC
> série est dans ces conditions la plus élevée. »

> **L'essentiel (p.146, VERBATIM)** — « ■ Comme en régime libre non amorti, les oscillations forcées d'un circuit RLC série
> sont sinusoïdales mais de fréquence imposée par l'excitateur. ■ La réponse d'un circuit RLC série à une tension
> excitatrice sinusoïdale de fréquence N est un courant électrique d'intensité sinusoïdale de valeur maximale I_m et de
> phase initiale φ dépendant de la fréquence des excitations et des grandeurs électriques R, L et C de l'oscillateur :
> **I_m = U_m/√(R² + (Lω − 1/Cω)²)** ; **tgφ = (1/Cω − Lω)/R** ■ Selon le signe de (Lω -1/Cω) ou du déphasage φ entre i et u,
> l'oscillateur électrique RLC série peut étre [sic] inductif ou capacitif. ■ En régime forcé sinusoïdal, la valeur
> maximale de l'intensité du courant est d'autant plus élevée que l'amortissement est plus faible. ■ La résonance
> d'intensité est obtenue pour une fréquence des excitations égale à la fréquence propre de l'oscillateur. ■ La résonance
> d'intensité d'un circuit RLC série peut être accompagnée d'une surtension aux bornes du condensateur, caractérisée par
> un quotient Q > 1 appelé dans ces conditions facteur de surtension : **Q = U_C/U** ■ En régime sinusoïdal forcé, la
> puissance moyenne P d'un circuit RLC série est la valeur moyenne prise par sa puissance instantanée p(t) durant une
> période : **P = UIcosφ = RI²** ■ Comme la résonance d'intensité, la résonance de puissance est obtenue pour une fréquence
> des excitations égale à la fréquence propre de l'oscillateur. ■ Les pertes par effet Joule sont d'autant plus faibles que
> le facteur de puissance est plus grand. »

### Exercices résolus

- **Exercice résolu (p.147–149)** — Énoncé : C, bobine B (L), R₀ = 81,5 Ω en série ; GBF U_m = 6 V, N réglable (Fig.1).
  1°) a) point (A ou B) relié à la masse pour visualiser u(t) et u_R0 ; b) schéma des branchements ; 2°) fréquence N₁,
  Fig.2 : 0,5 ms/div ; u(t) 2 V/div ; u_R0(t) 1 V/div : a) identifier u(t) ; b) N₁ et I_m ; c) Z ; d) déphasage i/u ; en
  déduire que la bobine a une résistance r non nulle, la calculer ; 3) [sic, sans °] fréquence N₂, u(t) et u_C(t) : a) point
  de masse ; b) schéma ; c) Fig.3, 1 ms/div, 2 V/div sur Y₁ et Y₂ : identifier u_C(t) ; d) fréquence de u_C et déphasage
  par rapport à u ; e) montrer que l'oscillateur est en résonance d'intensité ; f) facteur de surtension, danger ? ;
  g) C et L. Solution : 1°a) masse en B ; b) A → Y₁, D → Y₂ (Fig.4) ; 2°a) (1) = u(t) (« crêtes distantes de 6 div ») ;
  b) T₁ = 6 div × 0,5 ms = 3 ms, **N₁ ≈ 333 Hz** ; U_R0m = 2 V, **I_m = 24,5 mA** ; c) **Z = 244,9 Ω ≈ 245 Ω** ;
  d) |Δφ| ↔ Δt = T/6, **Δφ = −π/3 rad** ; R = Z.cosφ = 122,5 Ω, **r = 41 Ω** ; 3°a) masse en A (Fig.5) ; b) B → Y₁,
  E → Y₂ ; c) (2) = u_C ; d) **N₂ = 167 Hz**, **φ_uC − φ_u = −π/2 rad** ; e) i = dq/dt ⇒ φ_i = φ_q + π/2 ; u_C = q/C ⇒
  φ_uC = φ_q ⇒ **φ_u − φ_i = 0** : résonance d'intensité ; f) U_Cm = 7 V, **Q ≈ 1,17**, aucun danger ; g) Q = 1/(RCω₂) ⇒
  **C = 6,68 μF** (imprimé « 6,68 ∝F » [sic]) ; **L = 137 mH**. (Par rapport à 223433 : disparaissent « en déduire Q_m »
  en 2°b et « ou bien en résonance de charge » en 3°e ; la relation φ_i = φ_q + π/2 n'est utilisée qu'ici, sans être
  enseignée dans le cours de ce manuel.)

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux (p.150)** : 1- oscillations d'un RLC série soumis à une tension sinusoïdale « libres » ;
  2- fréquence des oscillations forcées peut être égale à la fréquence propre ; 3- résonance d'intensité quand la tension aux
  bornes du RLC est en phase avec l'intensité ; 4- résonance d'intensité quand l'impédance est maximale ; 5- Q augmente quand
  la résistance totale augmente ; 6- la puissance moyenne consommée par le condensateur est nulle ; 7- la résonance de
  puissance est elle même une résonance d'intensité ; 8- pour minimiser les pertes Joule en ligne, on diminue le facteur de
  puissance. (Pas de réponse imprimée.)
- **Ex. 2 — QCM (p.150)** : I- résonance d'intensité lorsque : a- impédance minimale ; b- fréquence imposée = fréquence
  propre ; c- impédance = résistance du résistor ; d- intensité et tension appliquée en phase. II- à la résonance
  d'intensité, i est : a- en quadrature avance sur la tension aux bornes du condensateur ; b- en quadrature retard par
  rapport à la tension aux bornes de la bobine ; c- en phase avec la tension aux bornes du résistor ; d- en phase avec la
  tension aux bornes du RLC. **III- (propre à ce manuel)** caractère capacitif lorsque : a- LCω² < 1 ; b- la tension aux
  bornes du condensateur est supérieure à celle aux bornes de la bobine en valeur maximale ; c- l'intensité est en avance de
  phase sur la tension appliquée. **[pas de IV : numérotation sautée, sic]** V- à la résonance d'intensité, une augmentation
  de la résistance entraîne : a- diminution de la fréquence caractéristique de la résonance ; b- diminution de la valeur
  maximale de l'amplitude de l'intensité ; c- l'augmentantion [sic] de la valeur maximale de la puissance moyenne.
  VI- Q s'écrit : a- 2πLN₀/R ; b- U_L/U quelle que soit N ; c- (1/R)√(C/L) ; d- U_C/U à la résonance d'intensité. (Pas de
  réponse imprimée.)

### Exercices et problèmes

- **Ex. 3 (p.151)** — circuit d'accord radio, N = 16233 Hz, L = 10⁻⁴ H : C ?
- **Ex. 4 (p.151)** — C et bobine (L, r) ; u(t) = 30√2 sinωt ; ω = 2000 rad.s⁻¹ : I = 600 mA, U₁ (bobine) = 30 V,
  U₂ (condensateur) = 30 V ; i = I_m sin(ωt + φ). 1°) Fresnel : φ, r, L, C ; 2°) comparer ω et ω₀ par leur quotient, sens
  de variation de ω pour la résonance.
- **Ex. 5 (p.151)** — C = 20 μF, R = 20 Ω, L = 0,55 H, r = 12,5 Ω ; u(t) = 100√2 sin2πNt, N = 48 Hz. 1°) Z (sans
  démonstration), la calculer ; 2°) I en fonction de Z ; 3°) circuit équivalent à (R + r) : a) N = N₀, la calculer ;
  b) Z₀ et I₀.
- **Ex. 6 (p.151)** — R, L, C ; U efficace, ω réglable, ampèremètre. 1°) Fresnel : Z et déphasage ; 2°) a) allure de
  I = f(ω), phénomène ; b) ω₀ dépend-elle de R, L, C ? expression ; c) Z et déphasage pour ω = ω₀.
- **Ex. 7 (p.151–152)** — bobine (L, r), C = 0,5 μF ; U = 2 V ; N₀ = 2325 Hz, I₀ = 130 mA. 1°) caractéristiques de la
  bobine ; 2°) facteur de surtension et puissance moyenne maximale.
- **Ex. 8 (p.152)** — portion MN : C et bobine (L, r) ; I = 0,20 A ; U_MN = 120 V, U_MP = 160 V, U_PN = 56 V. 1°) impédances
  bobine et condensateur, r ; 2°) déphasage de u_MN / i ; 3°) ω₀ = 250 rad.s⁻¹ : a) L et C ; b) ω et N ; c) puissance
  moyenne ; 4°) seconde pulsation ω' pour I = 0,20 A ; 5°) comparer les puissances à ω, ω₀, ω'.
- **Ex. 9 (p.152)** — R = 50 Ω, C = 1 μF, L réglable (résistance négligeable), u(t) = 10√2 sin(100πt). 1°) équation
  différentielle en i ; 2°) i(t) = I_m sin(100πt + φ) : a) L₀ pour la résonance d'intensité ; b) surtension aux bornes du
  condensateur si L = L₀ ; 2°) [sic, pour 3°)] tension de rupture U₀ = 100 V : L à ne pas dépasser.
- **Ex. 10 (p.152)** — résistor, C, bobine purement inductive L ; R totale ; u_AB = U_m sinωt ; wattmètre. 1°) à ω = ω₀,
  P₀ maximale (U, R) ; énergie E₀ reçue pendant une période (U, R, ω₀) ; 2°) à la résonance, E_t = E_L + E_C en fonction du
  temps, constante, en fonction de L, U, R ; que devient l'énergie reçue ? 3°) E_t/E₀ en fonction de Q (« surtention »
  [sic]).
- **Ex. 11 (p.153)** — G : N = 50 Hz, U = 6 V ; R = 300 Ω, C = 3 μF, bobine (L, r) ; u(t) sur Y₁ (4 V/div), u_R(t) sur Y₂
  (2 V/div), 1 ms/div ; « Pour une valeur N₀ » : deux sinusoïdes en phase ; la flèche « voie Y₂ » désigne la sinusoïde de plus grande
  amplitude (≈ 2,5 div × 2 V/div = 5 V), Y₁ ≈ 1,5 div × 4 V/div = 6 V ; période ≈ 4 div = 4 ms (N₀ ≈ 250 Hz) ; a) phénomène ;
  b) L et r.
- **Ex. 12 (p.153, synthèse)** — condensateur « EFD-CPM13B ; Capacité 1,2 MF ; Tolérence [sic] 10 % ; Tension maximale
  160 V » ; GBF U = 2 V, R = 10 Ω, bobine L = 58 mH (r) ; voltmètre, ampèremètre. 1°) schéma ; 2°) à N = 610 Hz, I maximale
  = 96,7 mA : a) fréquence propre ; b) C, indication à la place de « MF » ; c) dans la tolérance ?
- **Ex. 13 (p.153–154)** — R = 40 Ω, C, bobine (L, r) ; u(t) = 10√2 sin(2πNt). 1°) à N₀ : U_R = 9,6 V, u_c(t) =
  U_c√2 sin(318πt − π/2), U_c = 36 V : a) résonance d'intensité ; b) I₀ ; C, L, r ; Q ; c) u_c² = − Q²u² + 2U_c² ; d) énergie
  totale en fonction de u et u_c, conservation.
- **Ex. 14 (p.154)** — U = 10 V, R = 100 Ω, C = 0,5 μF, bobine r = 100 Ω, L = 50 mH. 1°) N₁ = 318 Hz : a) Z₁ ; b) I₁ ;
  c) P₁ ; d) φ₁ de u par rapport à i, grandeur en avance, caractère (résistif, capacitif ou inductif) ; 2°) diagramme de
  Fresnel à l'échelle ; 3°) N = N₀ : a) nouveau diagramme ; b) Z₀, I₀, P₀.
- **Ex. 15 (p.154–155)** — générateur 0–10 V, « de 5 à 5 kHz » [sic], ampèremètre, deux voltmètres, bobine (L, r), C,
  boîte 0–1,1 kΩ, oscilloscope bicourbe. 1°) schéma ; 2°) U = 5 V, tableau N (Hz) / I (mA) : 100/1,6 ; 200/3,4 ; 300/5,7 ;
  400/8,9 ; 500/15,1 ; 600/27,6 ; 700/47,0 ; 800/31,5 ; 900/20,5 ; 1000/14,6 ; 1100/11,7 ; 1200/9,8 ; 1300/8,5 ; 1400/7,6 ;
  a) tracer I = f(N) (1 cm ↔ 100 Hz ; 1 cm ↔ 2,5 mA) ; b) N₀ ; c) résistance totale ; 3°) a) branchements (u voie A,
  intensité voie B) ; b) à N₀ (voie A 2 V/div, voie B 1 V/div, 0,2 ms/div ; sinusoïdes (1) et (2) en phase, (2) plus ample) :
  courbe de la voie A, R puis r ; c) U_C maximale 21,5 V : C ; d) L.
- **Ex. 16 — Étude de texte « Le facteur de puissance » (p.155)** — STEG, pertes en ligne, puissance apparente = active +
  réactive (« La puissance active assure le fonctionnement des équipements produisant de la chaleur […] la puissance
  réactive résulte de la création de champs magnétiques utiles au fonctionnement de divers équipements (moteurs,
  compresseurs, etc.) »), condensateurs chez les industriels. Questions : 1°) mauvais facteur de puissance et pertes en
  ligne ; 2°) avantages d'un facteur élevé ; 3°) démontrer l'amélioration par l'insertion de condensateurs.

### Réponses du manuel (p.393, « Chapitre 5 » col. gauche puis col. droite)

« 3. C = 9,5.10⁻⁷ F » · « 5. 2°) I = U/Z; 3°a) N = 48 Hz; 3°b) Z₀ = 32,5 Ω ; I₀ = 3,077 A. » · « 6. 2°a) Résonance
d'intensité. 2°b) ω₀ ne dépend que de L et de C. 2°c) Z = R et Δφ = 0. » · « 7. 1°) r = 15,4 Ω ; 2°) Q = 10,445; P = 0,26 W. »
· « 9. 2°a) L₀ = 1H; 2°b) Q = 6,28 >1; 2°) L < 1,6 H. » · « 10. 1°) E₀ = 2πU²/ω₀R; 2°) E_t = LU²/R². 3°) E_t/E₀ = Q/2π. »
Aucune réponse pour les ex. 1, 2, 4, 8, 11–16. (223433 donnait aussi « 11. 2°) L = 0,135 H ; r = 60 Ω » ; ce manuel ne
la reprend pas.)

### En savoir plus / Documents

- **Fiche technique (p.156) « Construction de Fresnel »** — somme de fonctions sinusoïdales isochrones
  y_k = a_k sin(ωt + φ_k), période T = 2π/ω, y = A sin(ωt + φ) ; vecteur de Fresnel OA⃗ : module a, origine O (centre du
  cercle trigonométrique), tournant à la vitesse angulaire ω dans le sens trigonométrique, angle φ avec (O, i⃗) à t = 0 ;
  projection sur (O, j⃗) = y (Fig.1–3) ; y_k ↦ OA⃗_k [a_k, φ_k] ; y = Σy_k ↦ OA⃗ = ΣOA⃗_k ⇒ OA⃗ [A, φ] (Fig.4).
- **En savoir plus (p.157) « Générateur de courant haute fréquence »** — appareil vers 1895 (bobine de Ruhmkorff,
  décharge oscillante des condensateurs ; période croissant avec l'auto-induction et la capacité) ; tubes de Crookes et
  Geissler ; Nikola Tesla (« physicien autrichien né en Dalmatie en 1857 ») ; d'Arsonval (1893, Salpêtrière,
  « d'arsonvalisation ») ; résonateur du docteur Oudin ; source www.patrimoine.polytechnique.fr.

### Écart avec la référence (sciences-exp/04 — Oscillations électriques forcées)

- **Correspondance confirmée** : sciences-exp/04 (manuel 223433, ch.4, p.110–143). Même texte de base, mêmes figures et
  valeurs.
- ⛔ **À retirer à l'adaptation** (enseigné par la référence, absent de ce manuel) :
  - **Résonance de charge** tout entière : N_r = √(N₀² − R²/8π²L²) < N₀, condition R² < 2L/C, étude de g(ω), Q_m0,
    résonance impossible, courbes Q_m(N) (Fig.9, Fig.11b de 223433). (« Réponse linéaire » et résonance « très floue »
    figurent dans le manuel 223433 et sa fiche, mais pas dans le chapitre publié sciences-exp/04 : rien à retirer pour
    eux à l'adaptation.)
  - **Charge q(t)** : montage avec condensateur côté masse (u_C image de q), **Q_m = I_m/ω**, **φ_i = φ_q + π/2** et le
    §1.2.2 « Déphasage entre i(t) et q(t) », −π < φ_q < 0 ; **équation différentielle en q** (L d²q/dt² + R dq/dt + q/C = u) ;
    les objectifs correspondants.
  - Exercices de la référence portant sur la charge : QCM III (résonance de charge), ex. 12 et ex. 17 de 223433 ;
    question « en déduire Q_m » de l'exercice résolu.
  - Mention « l'impédance s'exprime en ohm (Ω) » du commentaire (absente ici, mais Z « a la dimension d'une résistance » :
    l'unité reste implicite — à garder avec prudence).
- ✅ **À ajouter / autrement** : QCM III sur le **caractère capacitif** (LCω² < 1 ; U_Cm > U_Lm ; i en avance) ;
  numérotation des exercices décalée (ref 13→12, 14→13, 15→14, 16→15, 18→16) ; Fig.8 à deux courbes seulement
  (R₀ = 20 Ω et 200 Ω) au lieu de trois (50/200/1000 Ω) ; l'exercice résolu utilise φ_i = φ_q + π/2 sans que le cours
  l'établisse (le garder seulement si l'on enseigne la relation i = dq/dt sur des sinusoïdes, déjà vue au ch.3 de ce
  manuel — à vérifier par le lecteur A) ; le chapitre suit ici l'**entretien** (ch.4) et précède les **filtres** (ch.6–7),
  qui réutilisent Z, Fresnel, la résonance d'intensité et Q (filtre passe-bande RLC, ch.7).
- **Vocabulaire / notations** : identiques à la référence (excitateur / résonateur, I_m0 ou I_mo, φ phase initiale de i,
  tgφ = (1/Cω − Lω)/R, cosφ = R/Z, Q facteur de surtension, P puissance moyenne « active ou réelle », UI puissance apparente
  en V.A, STEG, cosφ > 0,8).

### Bornes de scope

- ✅ **INCLUS** : excitateur (GBF) / résonateur (RLC série) ; visualisation de u et u_R0 (image de i) à l'oscilloscope
  bicourbe, choix du point de masse ; lecture d'oscillogrammes (période, amplitude, décalage) ; impédance Z = U_m/I_m ;
  équation intégro-différentielle en i, solution permanente admise i = I_m sin(ωt + φ) (régime transitoire hors programme) ;
  déphasage, |Δφ| = 2πΔt/T, concordance / opposition / quadrature avance-retard ; construction de Fresnel ;
  Z = √(R² + (Lω − 1/Cω)²), tgφ = (1/Cω − Lω)/R, −π/2 < φ < π/2, cosφ = R/Z ; circuit inductif / capacitif ; résonance
  d'intensité (N₀ = 1/2π√LC, Z = R, I_m0 = U_m/R, u et i en phase) ; influence de R (aiguë / floue, fréquence de résonance
  inchangée) ; surtension Q = U_C/U = 1/((R₀ + r)Cω₀) = Lω₀/(R₀ + r) = (1/(R₀ + r))√(L/C), dangers, surtension aux bornes de
  la bobine ; applications (quartz, haut-parleur, radio, hi-fi) ; puissance instantanée, T_p = T/2 ; puissance moyenne
  (définition, intégrale sur T_p, P = UIcosφ = RI²), puissance apparente (V.A), facteur de puissance, résonance de
  puissance, P = RU²/Z², pertes en ligne P₀ = R₀P²/(U²cos²φ), cosφ > 0,8 ; en exercices : énergie E_t à la résonance,
  E_t/E₀ = Q/2π, u_c² = −Q²u² + 2U_c², diagramme de Fresnel à l'échelle, tracé I = f(N), tolérance d'un composant.
- ⛔ **EXCLU** : résonance de charge, amplitude Q_m, équation en q, déphasage i/q comme résultat de cours ; régime
  transitoire (« hors programme ») ; régimes non sinusoïdaux (note p.143) ; bande passante, fréquences de coupure,
  Q = N₀/ΔN (ces notions arrivent au chapitre 7 pour le filtre RLC) ; nombres complexes ; puissance réactive chiffrée
  (seulement nommée dans le texte de l'ex. 16) ; compensation chiffrée par condensateurs ; résonance mécanique.

### Lecture

- **Pages lues en L1** : 130 à 157 (les 28 pages), 393 (réponses).
- **Pages lues sur l'image** (110 dpi) : 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147, 148, 149,
  150, 153, 155, 156, 393 ; p.130, 131, 134, 145, 151, 152, 154 et 157 vues sur l'image par la relecture R-7 (auditeur B),
  conformes : légende de la p.131 confirmée mot pour mot, Fig.4–5 de la p.134 conformes, √2 des énoncés des ex. 4, 5, 9,
  13 confirmés, formules de la p.145 conformes. Le chapitre est désormais entièrement vu sur l'image.
- **Écarts texte/image** : p.131 légende inclinée illisible en L1 ; p.133 ∫ et ω perdus (« i(t) = Imsin(tt + ) ») ; p.136–137
  toutes les phases (π/2, φ) et vecteurs OA⃗ perdus (« LLLI », « 8 OA1 ») ; p.138 √ et fractions éclatées, puces « ∞ »
  (présentes aussi sur l'image) ; p.139 accolade de l'encadré perdue ; p.140–141 ω₀ perdu (« Co », « L0 ») ; p.142 √2 perdus
  (« U 2 sin t ») ; p.143 bornes d'intégrales en désordre ; « T_p = 2/ω » identique sur l'image : π manquant [sic] ; p.145 fractions ; p.146 encadrés éclatés ; p.148–149
  ≈, φ, π perdus ; p.150 formules du QCM VI éclatées ; p.153 tableau EFD conforme ; p.154 tableau de l'ex. 15 conforme ;
  p.393 √ perdu.
- **Coquilles [sic]** : p.131 « trés » ; p.132 « ÉLECTIRQUES », « plus au moins » ; p.134 « est égale », « précisement »,
  « précedemment » ; p.135 « péride » ; p.138 « élèvées » ; p.139 « paragrahe », « déphase φ » (légende Fig.8b) ; p.140 bandeau « sinusoïdall » ; p.141
  « on cite » sans majuscule ; p.146 « étre » ; p.147 « branchechements », « pour le deux voies », « 3) » sans ° ; p.143 « T_p = 2/ω » (lire π/ω) ; p.149
  « 6,68 ∝F » ; p.150 QCM sans IV, « augmentantion », « quel que soit la fréquence » ; p.151 « fontion » ; p.152 numérotation
  « 2°) » répétée (ex. 9), « surtention » ; p.153 « Tolérence », « 1,2 MF » (sic voulu par l'exercice) ; p.154 « de 5 à
  5 kHz » ; p.155 « industrielle- par » ; p.393 « 2°) L < 1,6 H » (pour 3°).
- **Doutes [?]** :
  - [?] 1 — **Ex. 9, réponse « L₀ = 1 H »** : avec C = 1 μF et ω = 100π rad/s, L₀ = 1/(Cω²) ≈ 10,1 H ; Q = Lω/R = 6,28
    correspond à L = 1 H. Incohérence (C devrait valoir ≈ 10 μF pour L₀ = 1 H) ; la réponse « L < 1,6 H » (U_C ≤ 100 V)
    est cohérente avec Q = Lω/R. Ne pas reprendre les valeurs sans recalcul. (Même erreur dans 223433.)
  - [?] 2 — **Ex. 7, réponse « Q = 10,445 »** : r = U/I₀ = 15,4 Ω, L = 1/(4π²N₀²C) ≈ 9,37 mH, Q = Lω₀/r ≈ 8,9 ; 10,445
    est exactement le Q théorique du cours §4 pour R₀ = 50 Ω ((1/62,5)√(0,2/0,47·10⁻⁶) = 10,44) : réponse très
    probablement recopiée par erreur depuis le cours. P = 0,26 W cohérent.
  - [?] 3 — **Ex. 11** : U = 6 V est donnée comme valeur efficace, mais 6 V est l'amplitude lue sur la voie Y₁
    (1,5 div × 4 V/div) — seule incohérence résiduelle de l'énoncé (voir « doutes levés »).
  - [?] 4 — **Fig.11 (p.144)** : pic P ≈ 60 mW ; avec U_m = 2 V, R = 62,5 Ω, P_max = U²/R = (√2)²/62,5 = 32 mW ; 60–64 mW
    correspond à U_m²/R (confusion efficace/maximale probable). Fig.6a cohérente (I_m0 = 2/62,5 = 32 mA, pic ≈ 31 mA).
  - [?] 5 — **Fig.8a** : la courbe (1) (R₀₂ = 20 Ω, R = 32,5 Ω) devrait culminer à ≈ 61 mA ; elle culmine à ≈ 30 mA (même
    valeur que Fig.6a avec R₀ = 50 Ω) ; la courbe (2) (R₀₃ = 200 Ω) ≈ 8 mA cohérente (2/212,5 ≈ 9,4 mA).
  - [?] 6 — **Introduction p.132** : « chapitre précédent » = oscillations libres ; dans ce manuel le chapitre précédent
    est l'entretien (texte non adapté).
  - [?] 7 — **Exercice résolu, Fig.1 (p.147)** : l'énoncé demande de choisir « parmi les points A et B » le point de masse,
    mais la Fig.1 de l'énoncé ne porte aucune lettre (A, B, D, E n'apparaissent que sur les Fig.4–5 de la solution).
  - [?] 8 — **§3 / §4** : le §3 nomme R₀₂ = 20 Ω et R₀₃ = 200 Ω, le §4 nomme R₀₁ = 20 Ω, R₀₂ = 50 Ω, R₀₃ = 200 Ω
    (indices incohérents d'un paragraphe à l'autre).
- **Contrôles (cohérents)** :
  - Tableau §4 : Q théoriques 20,1 ; 10,44 ; 3,07 → U_Cm 40 ; 20,9 ; 6,1 V : cohérent avec 40 / 21 / 6,5 V.
  - Fig.3 (p.132) : à 400 Hz avec R = 62,5 Ω, Lω = 502,7 Ω, 1/Cω = 846,6 Ω, Z ≈ 350 Ω et k = Z/R₀ ≈ 7,0 ; la lecture
    graphique 4/0,6 ≈ 6,7 est compatible (valeur non imprimée).
- **Doutes levés (relecture R-7)** :
  - **Ex. 11** : période ≈ 4 div = 4 ms, soit N₀ ≈ 250 Hz (« N = 50 Hz » est la fréquence de départ du générateur ;
    l'énoncé passe ensuite à « une valeur N₀ ») ; L = 1/(4π²N₀²C) ≈ 0,135 H et U_R/U = 5/6 = R/(R + r) donne r = 60 Ω,
    exactement la réponse de 223433 (« L = 0,135 H ; r = 60 Ω »), non reprise dans ce manuel. Ma lecture initiale (Y₂ de
    plus faible amplitude, période ≈ 3,1 ms) était erronée.

## 2.6 Chapitre 6 — Généralités sur les filtres (manuel 223471, p.158–173)

**Plage vérifiée** : objectifs/prérequis p.158 ; ouverture n° 6 p.159 ; cours p.160–165 ; L'essentiel p.166 ; Exercices
p.167–170 ; En savoir plus p.171–173 (p.173 sans bandeau) ; pas de fiche technique. La p.174 est la page d'objectifs du
chapitre 7. Bandeau : « Evolution de systèmes électriques ◆ Généralités sur les filtres ».

**Objectifs (p.158, VERBATIM)** — « Reconnaître le schéma d'un filtre. » · « Distinguer entre l'entrée et la sortie d'un
filtre. » · « Représenter, en convention récepteur, les grandeurs électriques sur le schéma d'un filtre. » · « Calculer la
transmittance (ou fonction de transfert) d'un filtre. » · « Calculer le gain d'un filtre en décibels. » · « Reconnaître la
courbe de réponse d'un filtre (T = f(N) ou G = h(N)). » · « Tracer la courbe de réponse d'un filtre. » · « Déterminer la
(ou les) fréquence(s) de coupure d'un filtre. » · « Déterminer graphiquement la bande passante d'un filtre à - 3dB. »

**Prérequis (p.158)** — SAVOIR : Définir un quadripôle. · Caractériser une grandeur sinusoïdale par sa période, son
amplitude et sa phase initiale. · Écrire les relations entre la pulsation, la période et la fréquence d'une grandeur
sinusoïdale. · Écrire la relation entre la valeur maximale et la valeur efficace d'une tension sinusoïdale. · Définir
l'impédance d'un dipôle. SAVOIR FAIRE : Schématiser un quadripôle. · Utiliser la convention récepteur. · Visualiser
simultanément deux tensions électriques à l'oscilloscope. · Déterminer graphiquement la période et l'amplitude d'une
grandeur électrique oscillante. · Appliquer la relation entre la valeur maximale et la valeur efficace d'une tension
sinusoïdale.

**Page d'ouverture (p.159)** — « GÉNÉRALITÉS SUR LES FILTRES », n° 6 ; photo de deux enceintes et d'une « Courbe de réponse
amplitude ( dB ) / fréquences ( Hz ) » (60–110 dB, 50 Hz–10 kHz, plateau ≈ 95–97 dB) ; légende : « Les hauts parleurs
professionnels performants sont munis de filtres électriques réalisés avec des composants de grande fiabilité. » Texte
d'accroche (VERBATIM) : « En acoustique, dans le monde de la photo et de la vidéo, en télécommunications et dans beaucoup
d'autres domaines, les filtres électriques jouent un très grand rôle dans l'amélioration de la qualité des produits et de
la sensibilité, voire la stabilité de systèmes électroniques et dans la précision des tâches qu'ils assurent. Qu'est-ce
qu'un filtre électrique et qu'est-ce qui lui confère toutes ces propriétés de pointe ? »

**Plan** — titre p.160 « GENERALITÉS SUR LES FILTRES » ; introduction · **1** Filtrage (p.160–162 ; Manipulation,
Expérience 1, Expérience 2, Questions, Interprétation, Conclusion et définitions, Grandeurs caractéristiques d'un filtre
et shéma [sic]) · **2** Fonction de transfert et gain d'un filtre (2.1 Fonction de transfert, p.162–163 ; 2.2 Le gain d'un
filtre, p.164 ; 2.3 Courbe de réponse d'un filtre, p.164) · **3** Bande passante et fréquence(s) de coupure d'un filtre
(p.164–165) · **4** Applications des filtres (p.165) · L'essentiel (p.166) · Exercices : résolu (p.167–168) ; Tests rapides
(1 V/F, 2 QCM, p.169) ; Exercices d'application (3–6, p.170) · En savoir plus « Le filtrage en acoustique » (p.171–173).
(Pas d'exercices de synthèse ni d'étude de texte.)

### Cours — Activités

- **Introduction (p.160, VERBATIM)** — « On sait que les transformateurs servent à abaisser ou élever les tensions
  électriques. Par leur fonction analogique, les transistors bipolaires et les amplificateurs opérationnels peuvent être
  utilisés pour amplifier respectivement les courants et les tensions électriques. Autrement dit, les quadripôles servent à
  traiter les valeurs instantanées des signaux électriques. Il reste à savoir s'il n'y a pas des quadripôles qui peuvent
  traiter la fréquence (ou les fréquences) du signal et à saisir l'intêret [sic] pratique d'une telle opération. »
- **§1 Manipulation — filtrage (p.160–161)** — R₀ = 500 Ω, bobine L = 0,2 H, r = 12,5 Ω, C = 0,47 µF, interrupteur K :
  circuit RLC série utilisé comme quadripôle (Fig.1 : entrée E – K – résistor [noté « R » sur la figure] – bobine (L, r) –
  sortie S ; condensateur C entre S et M ; Y₁ en E, Y₂ en S : la sortie est la tension aux bornes du condensateur) ; GBF
  u_E(t) = U_Em sin(2πNt), U_Em = 6 V, N réglable ; masse du GBF en M (commune à l'entrée et à la sortie). Expérience 1 :
  N₁ = 50 Hz, K fermé → Fig.2a (u_E et u_S quasi confondues). Expérience 2 : N croissante, U_Em constante ; N₂ = 430 Hz
  (Fig.2b : u_S plus ample que u_E et décalée), N₃ = 1 kHz (Fig.2c : u_S plus faible), N₄ = 5 kHz (Fig.2d : u_S très
  atténuée). Remarque : « Tous les oscillogrammes de la figure 2 sont visualisés avec la même sensibilité verticale de
  l'oscilloscope, mais avec des réglages différents da [sic] la sensibilité horizontale. » Questions (VERBATIM) :
  « 1°) Identifier parmi les oscillogrammes (1) et (2) de la figure 2, ceux qui correspondent à la tension d'entrée u_E.
  2°) Comparer: a- les amplitudes U_Em et U_Sm respectivement de la tension d'entrée u_E et de la tension de sortie u_S,
  b- les fréquences de u_S et de u_E, c- les phases initiales de u_S et de u_E. 3°) Exprimer u_S en fonction du temps.
  4°) Préciser l'influence de la fréquence de la tension d'entrée sur l'amplitude de la tension de sortie. »
  Interprétation : voir Encadrés.
- **§2.1 Manipulation — fonction de transfert (p.162–163)** — montage de la Fig.1, N = 400 Hz « par exemple » ; tableau :

  | U_Em (V) | 2 | 4 | 6 | 8 | 10 |
  |---|---|---|---|---|---|
  | U_Sm (V) | 2,75 | 5,47 | 8,20 | 10,96 | 13,70 |

  Remarque : mesure possible des tensions efficaces U_E et U_S avec deux voltmètres (Fig.4). Questions (VERBATIM) :
  « 1°) En s'appyant [sic] sur le tableau dressé précédemment, préciser comment varie U_Sm en fonction de U_Em. 2°) Reproduire
  le même tableau, y ajouter une ligne pour le calcul du rapport U_Sm/U_Em et commenter le résultat obtenu. 3°) Préciser si
  le rapport U_Sm/U_Em garde la même valeur si l'on fixe la fréquence de la tension d'entrée à une valeur différente de
  400 Hz. En s'appuyant sur l'étude développée dans le paragraphe 1, justifier la réponse. » Commentaires : u_S sinusoïdale
  de même fréquence, U_Sm proportionnelle à U_Em (Fig.5 : droite par l'origine) → « quadripôle linéaire ».
- **§2.2–2.3 (p.164)** — exemples chiffrés T ↔ G ; courbes de réponse : Fig.6 (C_T, T = f(N), maximum T₀ ≈ 2, T = 1 en N₁),
  Fig.7 (C_G, G = h(N), G₀ = 6,02 dB, G = 0 en N₁), Fig.8 (G = h(N) en quadrillage semi-logarithmique, N de 1 à 10⁴ Hz).
- **§3 (p.164–165)** — question : « Montrer que T ≥ T₀/√2 équivaut : G ≥ G₀ - 3 dB » ; Fig.9a (N_b et N_h définies par
  T = T₀/√2), Fig.9b (définies par G = G₀ − 3 dB, repère « 3dB »).
- **§4 Applications (p.165)** — voir Encadrés.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Interprétation §1 (p.161–162)** — « L'apparition du chronogramme (2) sur l'écran de l'oscilloscope lorsque
> l'interrupteur K est fermé montre que le quadripôle transmet le signal d'entrée à la sortie ; en effet, le signal de
> sortie est une tension sinusoïdale de même fréquence N que celle d'entrée, mais son amplitude U_Sm et sa phase initiale φ
> dépendent de la valeur de N. **u_S(t) = U_Sm sin(2π Nt +φ)** On constate que U_Sm est comparable à U_Em pour les basses
> fréquences, mais elle lui est nettement inférieure pour les fréquences moins basses. De plus, elle devient très atténuée
> aux fréquences élevées. En fait, lors de l'étude des oscillations d'un circuit RLC série en régime forcé sinusoïdal
> (chapitre 5), on a montré que : U_Cm = I_m/(Cω) et que I_m = U_Em/Z avec Z = √(R² + (Lω − 1/Cω)²). I_m : valeur maximale
> de l'intensité du courant dans le circuit. Z : impédance du circuit. Or, U_Sm = U_Cm. Donc, U_Sm/U_Em = U_Cm/U_Em ;
> **U_Sm/U_Em = 1 / (Cω √(R² + (Lω − 1/Cω)²)) = 1 / √((RCω)² + (LCω² − 1)²)** soit N₀ = ω₀/2π où ω₀ = 1/√LC, il vient
> donc : **U_Sm/U_Em = 1 / √((RCω)² + (ω²/ω₀² − 1)²) = 1 / √(4π²R²C²N² + (N²/N₀² − 1)²)**. Cette expression de U_Sm/U_Em
> en fonction de N permet de vérifier que : * pour les basses fréquences c'est-à-dire lorsque N → 0, on a U_Sm ≈ U_Em ;
> * pour les hautes fréquences c'est-à-dire lorsque : N → ∞, on a U_Sm → 0. »

> **Conclusion et définitions (§1, p.162, encadré)** — « Selon la valeur de sa fréquence, un signal sinusoïdal appliqué à
> l'entrée d'un quadripôle donné peut être récupéré à sa sortie plus ou moins amplifié ou atténué. Une telle opération est
> appelée filtrage et le quadripôle utilisé a joué le rôle de filtre électrique. Le filtrage est une opération de tri des
> signaux électriques selon leurs fréquences. On appelle filtre électrique tout quadripôle ne transmettant que les signaux
> électriques de fréquence(s) comprise(s) dans un certain domaine. **Grandeurs caractéristiques d'un filtre et shéma** [sic]
> On schématise un filtre comme dans la figure 3. Un filtre est caractérisé par les grandeurs électriques : u_E(t) :
> tension d'entrée. u_S(t) : tension de sortie. i_E(t) : intensité du courant d'entrée en convention récepteur. i_S(t) :
> intensité du courant de sortie en convention récepteur. » (Fig.3 : quadripôle, i_E entrant à l'entrée, i_S entrant par la
> sortie, flèches u_E et u_S.)

> **Conclusion et définitions (§2.1, p.163, encadré)** — « Pour une fréquence donnée de la tension d'entrée d'un filtre, le
> rapport U_Sm/U_Em est constant. Par suite, il est considéré comme étant une caractéristique du filtre. Par définition, on
> l'appelle fonction de transfert ou transmittance du filtre, on la note T. **T = U_Sm / U_Em** Étant caractérisé par une
> transmittance constante pour une fréquence donnée, le filtre est qualifié de quadripôle linéaire. » Remarque : « ■ Si
> T < 1, il y a filtrage avec atténuation du signal traité. ■ Si T = 1, il y a uniquement filtrage. ■ Si T > 1, en plus du
> filtrage, il y a amplification du signal traité. »

> **Gain (§2.2, p.164)** — « La transmittance T d'un filtre peut varier dans un domaine très large [0,001 , 100 et même
> plus]. Pour rendre les différentes valeurs de T commodes à utiliser, il faut chercher à étirer les petites valeurs et à
> compresser les grandes valeurs. On introduit alors la grandeur “gain”. Le gain en tension d'un filtre, noté G, s'écrit
> par définition : **G = 20 logT** Le gain est exprimé en décibels de symbole dB. Il peut être mesuré directement à l'aide
> d'un décibelmétre [sic]. » Note marginale : « décibel : du nom du physcien [sic] américain Graham Bell (1847 - 1922) ».
> Tableau d'exemples : T 10⁻³ / 10⁻² / 10⁻¹ / 0,5 / 1 / 10 / 10² → G (dB) −60 / −40 / −20 / −6 / 0 / 20 / 40. « On remarque
> que : ■ si T > 1 , G > 0 ■ si T = 1 , G = 0 ■ si T < 1 , G < 0 Donc, le gain est une grandeur algébrique. »

> **Courbe de réponse (§2.3, p.164)** — « On appelle courbe de réponse d'un filtre la courbe (C_T) représentant T = f(N) ou
> la courbe (C_G) représentant G = h(N). De l'allure générale de (C_T) (Fig.6), on peut déduire celle de (C_G) (Fig.7). »
> Remarque : « Bien que l'on traite des signaux de basse fréquence, le domaine de variation de N, reste très large [0,1Hz -
> 300kHz ou plus]. Par suite, il est plus commode d'attribuer à l'axe des fréquences une échelle logarithmique, c'est-à-dire
> que l'on gradue l'axe des abscisses en logarithme décimal de N, ce qui explique la non linéarité de cette échelle
> (Fig.8). Dans ce cas, le quadrillage dans lequel est tracée la courbe est dit semilogarithmique. »

> **Bande passante (§3, p.164–165)** — « La forme générale de la courbe de réponse (Fig 6 , 7 ou 8) est caractérisée par un
> maximum T₀ ou G₀. Le filtre est passant lorsque sa transmittance T est telle que : **T ≥ T₀/√2** » ; « La valeur T₀/√2 de
> T [ou (G0 -3dB] de G) peut être atteinte généralement avec deux fréquence [sic] différentes (Fig. 9a et 9b) : - une
> fréquence inférieure appelée fréquence de coupure basse N_b, - une fréquence supérieure appelée fréquence de coupure
> haute N_h. » **Définition** : « On appelle bande passante d'un filtre, l'intervalle des fréquences [N_b , N_h] pour
> lesquelles : T ≥ T₀/√2, ce qui signifie : l'intervalle [N_b , N_h] tel que **G ≥ G₀ - 3 dB**. La différence (N_h - N_b)
> est la largeur de la bande passante. » Remarque : « L'étude des cas (objet du chapitre suivant :chap.7) montre qu'il y a
> des filtres caractérisés par une seule fréquence de coupure, la fréquence de coupure basse N_b ou bien la fréquence de
> coupure haute N_h. Par conséquent, leur bande passante sera définie par une seule limite (inférieure ou supérieure). »

> **Conclusion (§3, p.165, encadré)** — « Le filtre électrique est caractérisé par sa bande passante, domaine de fréquences
> pour lesquelles la chute de gain est inférieure à 3 dB. La sélectivité d'un filtre est définie par sa bande passante :
> plus la bande passante est étroite, plus le filtre est sélectif. »

> **Applications (§4, p.165)** — « Les filtres servent à - extraire ou supprimer la composante continue d'un signal
> (capteur de vitesse...), - éliminer des fréquences indésirables dans les circuits électroniques (bruit haute fréquence,
> perturbations dues au réseau du secteur 50 Hz...), - sélectionner une (ou des) bande(s) de fréquence : ✔ en acoustique
> (haut-parleurs des chaîne Hi-Fi), ✔ en télécommunication (sélection d'une station sur un poste radio, d'une chaîne de
> télévision, appel téléphonique avec un appareil à touches, ligne ADSL pour faire passer simultanément des conversations
> téléphoniques, des signaux de chaînes de télévision et des signaux de IP “Internet Protocol”...) »

> **L'essentiel (p.166, VERBATIM)** — « ■ Le filtre électrique est un quadripôle qui ne transmet que les signaux de
> fréquence(s) comprise(s) dans un certain domaine. ■ Le filtrage est une opération de trie [sic] des signaux électriques
> électriques [sic] selon leurs fréquences. ■ Un signal sinusoïdal appliqué à l'entrée d'un filtre peut être récupéré à sa
> sortie plus ou moins amplifié ou atténué. ■ La fonction de transfert (ou transmittance) d'un filtre est le rapport :
> **T = U_Sm/U_Em** ■ Le gain d'un filtre est : **G = 20 log T** ; c'est une grandeur sans dimension qui s'exprime en
> décibels; ■ - Tout filtre atténuant le signal traité a un gain négatif (G < 0). - Tout filtre amplifiant le signal traité
> a un gain positif (G > 0). - Tout filtre n'affectant pas l'amplitude du signal traité a un gain nul (G=0). ■ La bande
> passante à (-3dB) d'un filtre est l'intervalle des fréquences [N_b,N_h] pour lesquelles : **G ≥ G₀ - 3** [sic, sans
> « dB »] où : - G₀ est le gain maximal, - N_b est la fréquence de coupure basse, - N_h est la fréquence de coupure haute.
> ■ Un filtre est passant pour tout signal électrique dont la fréquence appartient à sa bande passante. ■ Un filtre est
> d'autant plus sélectif que sa bande passante est plus étroite. »

### Exercices résolus

- **Exercice résolu (p.167–168)** — Énoncé : filtre alimenté par un GBF, u_E = U_Em sin2πNt. 1°) schéma et branchements
  (u_E sur Y₁, u_S sur Y₂) ; 2°) Fig.1 (u_E à N₁ ; 2 ms/div, 1 V/div) : N₁ et U_Em ; 3°) Fig.2 (u_E et u_S, mêmes
  sensibilités) : a) identifier u_S, comparer fréquence et phase initiale ; b) T et G ; 4°) U_Sm maximale 2,82 V pour
  N₀ = 1,5 kHz : G₀ ; 5°) comparer G et G₀, en déduire que N₁ est une fréquence de coupure, basse ou haute ? Solution :
  1°) schéma GBF → entrée E, masse en M commune, E → Y₁, S → Y₂ ; « il est inutile de relier le point M à la masse de
  l'oscilloscope parce que celle-ci est automatiquement reliée à la masse du GBF via le fil de terre » ; 2°) T_E sur
  4 div → T_E = 8 ms, **N₁ = 125 Hz** ; 2U_Em sur 5 div → **U_Em = 2,5 V** ; 3°a) (1) d'amplitude 2,5 V = u_E ; (2)
  d'amplitude 2 V = u_S ; décalage τ = T_E/8 → |Δφ| = 2πτ/T_E ; u_S en retard → **φ_S = −π/4 rad** (φ_E = 0) ; b) **T₁ = 0,8 ;
  G₁ = −1,938 dB** ; 4°) **G₀ = + 1,046 dB** ; 5°) « G₀ - G₁ = -2,984 dB ≅ -3 dB » [sic : la différence vaut + 2,984 dB],
  N₁ < N₀ → **fréquence de coupure basse**.

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux (p.169)** : 1- le filtrage est le traitement de l'amplitude des signaux ; 2- tout filtre est un
  quadripôle ; 3- tout quadripôle est un filtre ; 4- la fonction de transfert est l'inverse de la transmittance ; 5- la
  transmittance dépend de la fréquence de la tension d'entrée ; 6- le filtre est un quadripôle linéaire parce que
  l'amplitude de sortie est proportionnelle à celle d'entrée ; 7- « Le gain d'un filtre est supérieur à l'unité (G>1 dB)
  lorsque sa transmittance T est positive. » ; 8- bande passante = intervalle où G > 3 dB ; 9- dans la bande passante à
  −3 dB tant que T > 1/3 ; 10- le filtre ne transmet pas les signaux de fréquence supérieure à sa fréquence de coupure
  basse ; 11- (G₀ − 3 dB) et (G₀ + 3 dB) correspondent respectivement à N_b et N_h. (Pas de réponse imprimée.)
- **Ex. 2 — QCM (p.169)** : I- le filtre sert à : a- modifier la fréquence d'un signal ; b- transmettre tout signal dont la
  fréquence appartient à un domaine déterminé ; c- amplifier les tensions. II- la courbe de réponse : a- peut représenter
  la fonction de transfert en fonction de la fréquence ; b- est une droite linéaire ; c- est une sinusoïde de même
  fréquence que l'entrée ; d- peut représenter le gain en fonction de la fréquence. III- la bande passante : a- renferme
  uniquement fréquence propre, N_b et N_h ; b- est limitée par N_b et N_h ; c- est l'intervalle où le gain est maximal.
  **[IV et V absents : numérotation sautée, sic]** VI- réponse d'un quadripôle linéaire à une tension sinusoïdale :
  courbes a (droite u_S(t) croissante), b (sinusoïde déformée), c (signal écrêté/trapézoïdal), d (sinusoïde). (Pas de
  réponse imprimée.)

### Exercices et problèmes

- **Ex. 3 (p.170)** — tableau N (Hz) 100 / 200 / 500 / 1000 / 2000 / 4000 ; T 25,14 / 25,14 / 17,79 / 12,60 / 6,31 / 3,17.
  1°) a) G(T) ; b) ligne G ; c) G = f(N) sur papier semi-logarithmique ; 2°) a) G₀ ; b) fréquence(s) de coupure à −3 dB.
- **Ex. 4 (p.170)** — filtre commandé par une tension sinusoïdale de N réglable de 20 Hz à 5 kHz, U_Em = 1,000 V ; voltmètre
  en sortie : 1 V pour 44 et 52 Hz ; maximum 1,414 V vers 48 Hz. 1°) expressions de T et G ; 2°) à quoi correspond
  l'indication maximale ; 3°) montrer que 44 et 52 Hz sont les fréquences de coupure.
- **Ex. 5 (p.170)** — courbe G (dB) en fonction de N (échelle logarithmique 6–40 Hz ; maximum ≈ 1 dB vers 14 Hz).
  1°) graphiquement : a) G₀ et T₀ ; b) fréquences de coupure à −3 dB ; c) bande passante et largeur ΔN ; 2°) U_Sm la plus
  élevée pour U_Em = 0,4 V.
- **Ex. 6 (p.170)** — trois droites U_Sm = f(U_Em) (graduations 0,4 V) : courbe 1 (pente ≈ 1), courbe 2 (pente < 1),
  courbe 3 (pente > 1). 1°) T₀ et G₀ pour U_Em = 0,8 V ; 2°) signal atténué, amplifié ou non affecté ?

### Réponses du manuel (p.393, colonne droite « Chapitre 6 »)

« 3. 1°) a) G = 20logT ; b) [tableau] N(Hz) 100 / 200 / 500 / 1000 / 2000 / 4000 ; T 25,14 / 25,14 / 17,79 / 12,60 / 6,31 /
3,17 ; G(dB) 28 / 28 / 25 / 22 / 16 / 10 ; 2°) a) G₀ = 28 dB ; b) Nh = 500Hz » · « 4. 1°) T = USm/UEm ; G = 20 logT
2°) Valeur efficace maximale de la tension de sortie. 2°) [sic, pour 3°)] US₀/US = 1,414 soit » [phrase inachevée,
sic] · « 5. 1°) a) G₀ = 1dB ; G₀ = 20 logT₀, ce qui équivaut T₀ = 10^(G₀/20) D'où, T₀ = 1,122 ; b) Les fréquences de
coupure: Nb = 12 Hz et Nh = 15 Hz. La bande passante [12Hz, 15Hz] La largeur de la bande passante : 3Hz 2°) G₀ = logT₀
[sic : 20 log] et T₀ = USmo/UEm USmo = T₀ .UEm soit 0,4488V » · « 6. 1°) Courbe 1 : USm = 0,8V ; T = 1 ; G = 0 dB ;
Courbe 2 : USm = 0,45 V ; T = 0,56 ; G = -5 dB ; Courbe 3 : USm = 1,4 V ; T = 1,75 ; G = 4,86 dB 2°) G = 0. L'amplitude
du signal traité n'est pas affectée. » Pas de réponse pour les ex. 1 et 2.

### En savoir plus / Documents

- **« Le filtrage en acoustique » (p.171–173, d'après www.freesoundeditor.com)** — sons = sommes de signaux sinusoïdaux ;
  note principale N₀ et harmoniques (fréquence double, triple, quadruple, de volume décroissant) ; égaliseur (équaliseur),
  boutons « basses », « aigüs », « medium » ; signal carré décomposé en somme de sinusoïdes (figure) ; signal riche /
  pauvre en aigus (figure : signal filtré) ; filtrage des « sifflantes » et des occlusives, filtres « Dresseurs » [sic,
  pour « de-esser »] ; spectrogramme (figure, fréquence 0–20 000 Hz, intensité −60 à 10 dB) ; définitions qualitatives :
  « Le filtre passe-haut bloque les harmoniques basses et moyennes et laisse passer les harmoniques aiguës. Le filtre
  passe-bas bloque les harmoniques hautes et moyennes et laisse passer les harmoniques basses. Le filtre passe-bande
  bloque les harmoniques hautes et basses et laisse passer les harmoniques moyennes. » ; « notch », « filtre en peigne » ;
  effet « wha-wha », « humanizer » ; chaîne hi-fi et carte son : fréquences de moins de 10 Hz et de plus de 25 000 Hz
  « oubliées ».

### Écart avec la référence (aucune)

- **Correspondance** : confirmée « aucune » dans physique-bac-sciences-exp (le manuel 223433 ne traite pas les filtres ;
  sa fiche §2.4 classe « bande passante, fréquences de coupure à −3 dB, largeur de bande » en ⛔ EXCLU). Aucun chapitre de
  `content/` ne traite des filtres (recherche « filtre », « passe-bas », « décibel », « bande passante » : seule occurrence
  hors fiches, le logarithme décimal et les décibels du niveau sonore dans `math-bac-info/06-logarithme-neperien`, utile en
  prérequis pour G = 20 log T). Chapitre **à créer** ; il réutilise le chapitre 5 (Z, U_Cm = I_m/Cω, N₀) comme exemple
  introductif.
- ✅ **À créer (tout le contenu)** : filtrage, filtre = quadripôle (entrée, sortie, masse commune, convention récepteur
  i_E, i_S, u_E, u_S) ; quadripôle linéaire ; transmittance (fonction de transfert) T = U_Sm/U_Em (ou U_S/U_E efficaces) ;
  gain G = 20 log T en dB, grandeur algébrique ; courbes de réponse T = f(N), G = h(N), échelle semi-logarithmique ;
  bande passante à −3 dB, T ≥ T₀/√2 ⇔ G ≥ G₀ − 3 dB, N_b, N_h, largeur, sélectivité ; filtres à une seule fréquence de
  coupure ; applications ; lecture d'oscillogrammes (T, φ_S − φ_E) ; exemple RLC série « sortie aux bornes de C » et son
  expression U_Sm/U_Em = 1/√((RCω)² + (LCω² − 1)²).
- **Vocabulaire / notations propres** : « quadripôle », « transmittance », « fonction de transfert », T, T₀, G, G₀, (C_T),
  (C_G), N_b « fréquence de coupure basse », N_h « fréquence de coupure haute », « bande passante à (−3 dB) »,
  « sélectivité », « décibelmètre », « log » = logarithme décimal.

### Bornes de scope

- ✅ **INCLUS** : définitions (filtrage, filtre, quadripôle linéaire), schéma normalisé d'un filtre, transmittance, gain
  en dB et sa signification (atténuation / amplification / sans effet), tableau T ↔ G, courbes de réponse (linéaires et
  semi-logarithmiques), bande passante et fréquences de coupure à −3 dB (définitions par T₀/√2 et par G₀ − 3 dB, démonstration
  de l'équivalence), largeur, sélectivité, applications ; en exercices : calculs T, G, G₀, T₀ = 10^(G₀/20), lecture de
  N_b et N_h sur un tableau ou une courbe, U_Sm maximale, mesure aux voltmètres (valeurs efficaces), lecture
  d'oscillogrammes (période, amplitude, déphasage).
- ⛔ **EXCLU** : étude détaillée des filtres particuliers (passe-bas, passe-haut, passe-bande, RC, RLC, actifs : chapitre 7) ;
  fonction de transfert complexe, diagrammes de Bode asymptotiques, pentes en dB/décade ; ordre d'un filtre ; décomposition
  de Fourier (seulement évoquée qualitativement dans « En savoir plus ») ; filtres numériques.

### Lecture

- **Pages lues en L1** : 158 à 173 (les 16 pages), 393 (réponses).
- **Pages lues sur l'image** (110 dpi) : 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 393 ; p.158 et
  171–173 vues sur l'image par la relecture R-7 (auditeur C), conformes. Le chapitre est désormais entièrement vu sur
  l'image.
- **Écarts texte/image** : p.159 légende et courbe d'ouverture absentes du texte ; p.161–162 fractions et racines
  déstructurées (« (RC) + (LC2 1)2 », « & pour les basses fréquences ») ; p.164 T₀/√2 rendu « T  o 2 » ; p.165 ≥ perdus,
  « T ≥ T₀/√2 » illisible ; p.168 Δφ, π perdus ; p.169 courbes du QCM VI absentes ; p.170 courbes des ex. 5 et 6
  absentes (seuls des « ) » parasites) ; p.393 tableau de l'ex. 3 conforme.
- **Coquilles [sic]** : p.160 « intêret », Fig.1 « R » pour R₀ ; p.161 « da la sensibilité » ; p.162 « shéma »,
  « mesurses » ; p.163 « osillloscope », « s'appyant », « proportionnellent » ; p.164 « physcien »,
  « décibelmétre », « Graham Bell » qualifié de « physicien américain » ; p.165 « deux fréquence », « [ou (G0 -3dB] de G) »,
  « des chaîne » ; Fig.9b étiquettes « N_h N_b » à gauche ; p.166 « trie », « électriques électriques », « G ≥ G₀ - 3 »
  (sans dB) ; p.167 « nécéssaires », « respectivemnet » ; p.168 « celle u_E », « G₀ - G₁ = -2,984 dB » (signe), étiquette « 0,25T_E » de la figure de la solution (le
  décalage mesuré vaut ≈ 0,5 div pour une période de 4 div, soit T_E/8) ; p.169 QCM
  sans IV ni V, item 7 « supérieur à l'unité (G>1 dB) » ; p.170 « tranmittance », « voltmétre » ; p.171 « ci-essous »,
  « aigüs », « a diminuer » ; p.172 « Dresseurs » ; p.173 « des système » ; p.393 ex. 4 « 2°) » répété et réponse
  tronquée, ex. 5 « G₀ = logT₀ ».
- **Doutes [?]** :
  - [?] 1 — **Ex. 5, réponse « N_b = 12 Hz et N_h = 15 Hz »** : sur la courbe (échelle logarithmique régulière), le
    maximum ≈ 1 dB est vers 14 Hz et G = G₀ − 3 = −2 dB est atteint vers ≈ 10 Hz et ≈ 20 Hz ; la réponse imprimée paraît
    fausse.
  - [?] 2 — **Ex. 4** : « le voltmètre indique 1 V » pour U_Em = 1,000 V : ambiguïté valeur efficace / maximale (un
    voltmètre indique une valeur efficace) ; la réponse 2°) parle de « valeur efficace maximale de la tension de sortie ».
- **Contrôles (cohérents)** :
  - Ex. 6 : courbe 2, U_Sm = 0,45 V, T = 0,56, « G = −5 dB » (20 log 0,56 = −5,04) ; courbe 3, T = 1,75, G = 4,86 dB.
  - Tableau §2.1 : T ≈ 1,37 constant (2,75/2 = 1,375 ; 13,70/10 = 1,37) ; recalcul théorique à 400 Hz avec R = 512,5 Ω :
    T ≈ 1,37.
- **Doutes levés (relecture R-7)** :
  - **Exercice résolu 3°a** : mesuré au zoom, le décalage entre les crêtes vaut ≈ 0,5 div pour une période de ≈ 4 div,
    soit T_E/8 ; le crochet marqué « 0,25T_E » couvre lui aussi ≈ 0,5 div. τ = T_E/8 et φ_S = −π/4 rad sont confirmés ;
    l'étiquette « 0,25T_E » est une coquille [sic] (relevée dans les coquilles).


## 2.7 Chapitre 7 — Exemples de filtres (manuel 223471, p.174–219)

**Plage vérifiée** : objectifs/prérequis p.174 ; ouverture n° 7 p.175 ; cours p.176–206 ; L'essentiel p.207–208 ;
Exercices p.209–216 ; En savoir plus p.217–219 (p.219 sans bandeau). La p.220 est la page d'objectifs du chapitre 8
(« Production de signaux périodiques non sinusoïdaux »). Pas de fiche technique. Bandeau : « Evolution de systèmes
électriques ◆ Exemples de filtres ».

**Objectifs (p.174, VERBATIM)** — « Réaliser un filtre ( passe bas, passe haut, passe bande). » · « Etablir l'expression
de la fonction de transfert T d'un filtre. » · « Calculer le gain d'un filtre. » · « Tracer la courbe de réponse
U_Sm = f(N) [ou G = f(N)] d'un filtre. » · « Déterminer la (ou les) fréquence(s) de coupure et la largeur de la bande
passante d'un filtre. » · « Distinguer le filtre actif du filtre passif. »

**Prérequis (p.174)** — SAVOIR : Définir un quadripôle. · Définir une tension sinusoïdale. · Exprimer la valeur maximale
de l'intensité du courant parcourant un circuit RLC série en régime sinusoïdal forcé. · Exprimer le facteur de surtention
[sic] à la résonance d'un circuit RLC série. · Définir la fonction de transfert d'un filtre. · Définir le gain d'un filtre
en décibels. · Exprimer le gain d'un filtre en décibels. · Définir les fréquences de coupure d'un filtre. · Définir la
bande passante d'un filtre. SAVOIR FAIRE : Utiliser la convention récepteur. · Distinguer entre l'entrée et la sortie d'un
filtre. · Visualiser simultanément deux tensions à l'oscilloscope. · Mesurer à l'oscilloscope : - la valeur maximale d'une
tension ; - le déphasage entre deux tensions sinusoïdales. · Mesurer la valeur efficace d'une tension sinusoïdale avec un
voltmètre. · Appliquer la loi des mailles. · Appliquer la loi des noeuds. · Utiliser les propriétés d'un amplificateur
opérationnel idéal. · Faire une construction de Fresnel.

**Page d'ouverture (p.175)** — « EXEMPLES DE FILTRES », n° 7 ; photo d'une table de mixage (« KOOL SOUND KOOL-03 ») ;
légende : « En HiFi , les équaliseurs utilisés sont des filtres dont la technologie fait généralement intervenir des
amplificateurs opérationnels. » Texte d'accroche (VERBATIM) : « Les filtres sont indissocibles [sic] de l'acoustique, de
la radiophonie et de plusieurs autres domaines. Sans eux, on aurait du mal à concevoir des chaînes HiFi, des émetteurs,
des récepteurs, etc. Comment fonctionnent-ils ? » · « Pourquoi appelle-t-on les filtres utilisés dans le domaine des
asservissements, des correcteurs ? »

**Plan** — titre p.176 « EXEMPLES DE FILTRES » ; introduction · **1** Filtres passe bas (1.1 Filtre passe bas passif :
1.1.1 Courbes de réponse G = f(N), p.176–178 ; 1.1.2 Facteurs dont dépend la fréquence de coupure d'un filtre passe bas,
p.178–180 ; 1.1.3 Étude théorique, p.180–183 ; 1.2 Filtre passe bas actif : 1.2.1 Courbe de réponse G = f(N), p.183–185 ;
1.2.2 Facteurs dont dépend la fréquence de coupure du filtre, p.185–188 ; 1.2.3 Étude théorique, p.189–191) · **2** Filtre
passe haut (2.1 Courbes de réponse U_Sm = f(N) et G = h(N), p.192–194 ; 2.2 Étude théorique, p.195–198) · **3** Filtre
passe bande (3.1 Réponse du quadripôle, p.198–201 ; 3.2 Étude théorique, p.201–206 : transmittance, gain, bande passante,
largeur, sélectivité et facteur de qualité, déphasage ; Conclusion ; Remarque générale sur l'ordre) · **4** Applications
des filtres (p.206) · L'essentiel (p.207–208) · Exercices : résolu (p.209–211) ; Tests rapides (1 V/F, 2 QCM, p.212) ;
Exercices d'application (3–6, p.213) ; Exercices de synthèse (7–10, p.214–216) ; 11 Étude de texte (p.216) · En savoir
plus « Technologies des filtres » (p.217–219).

### Cours — Activités

- **Introduction (p.176, VERBATIM)** — « Dans le traitement des signaux électriques en fréquence, on cherche à utiliser les
  filtres qui conviennent mieux par leur sélectivité et par le gain qu'ils offrent à leur sortie. Il est fort intéressant
  alors de déterminer ces spécifications particulières et d'identifier les facteurs dont elles dépendent. »
- **§1.1.1 Manipulation — filtre passe-bas passif RC (p.176–177)** — Fig.1 : E – K – R₁ – S, C₁ entre S et M (sortie aux
  bornes du condensateur) ; GBF u_E(t) = U_Em sin(2πNt), U_Em = 5 V, N réglable ; C₁ = 0,47 µF, R₁ = 318 Ω ; E → Y₁, S → Y₂ ;
  N₁ = 700 Hz → Fig.2 (2 V/div sur les deux voies ; u_S plus faible et en retard). Tableau :

  | N (Hz) | 10 | 50 | 10² | 2.10² | 5.10² | 10³ | 2.10³ | 5.10³ | 10⁴ | 10⁵ |
  |---|---|---|---|---|---|---|---|---|---|---|
  | U_Sm (V) | 5 | 5 | 5 | 4,9 | 4,44 | 3,60 | 2,30 | 1,01 | 0,52 | 0,05 |

  u_S en retard de phase sur u_E, Δφ = φ_S − φ_E « d'autant plus remarquable que la fréquence N est plus élevée » ;
  Remarque : voltmètres (valeurs efficaces) ; voltmètre électronique : transmittance directe pour N > 1 kHz. Questions
  (VERBATIM) : « 1°) A l'aide des oscillogrammes de la figure 2, comparer U_Sm à U_Em et vérifier que u_S est en retard de
  phase par rapport à u_E. 2°) Relever du tableau la valeur la plus élevée U_Smo de U_Sm, calculer U_Smo/√2, comparer les
  différentes valeurs de U_Sm à U_Smo/√2 et en déduire que le quadripôle RC est un filtre. 3°) Reproduire le tableau des
  mesures et y ajouter une ligne pour le calcul du gain G du filtre. 4°) Tracer les courbes représentant l'évolution de U_Sm
  et G en fonction de N en adoptant une échelle logarithmique en abscisse. 5°) Décrire chacune des deux courbes, déterminer
  graphiquement la (ou les) fréquence(s) de coupure du filtre et en déduire la largeur de sa bande passante. 6°) Sachant
  qu'a [sic] la fréquence de coupure trouvée, on obtient les oscillogrammes de la figure 3, calculer le déphasage
  Δφ = φ_S − φ_E caractérisant ce cas particulier. » Analyse : Fig.4 (G = f(N) semi-log, palier 0 dB, repère « 3dB »,
  asymptote haute fréquence) ; N_h = 1070 Hz, ΔN = 1070 Hz ; « filtre passif » ; pente −20 dB/décade ; note marginale
  « Décade : rapport de 10. Octave : rapport de 2. » (avec une échelle logarithmique illustrée). Question (VERBATIM) :
  « A l'aide de la même tangente, montrer que l'atténuation de 20 dB/ décade est équivalente à une atténuation de 6
  dB/octave. »
- **§1.1.2 Expérience 1 — influence de C (p.178–179)** — Fig.5 : C réglable, R₁ = 318 Ω ; C₂ = 0,30 µF, C₃ = 0,90 µF ; Fig.6
  (trois courbes G = f(N), C₃ à gauche, C₁, C₂ à droite). Questions (VERBATIM) : « 1°) Déterminer graphiquement et
  approximativement les fréquences de coupure hautes N_h2 et N_h3 obtenues respectivement avec C₂ et C₃. 2°) Calculer pour
  les trois cas étudiés, le produit N_h.C ; comparer les valeurs trouvées entre elles et en déduire que la fréquence de
  coupure N_h est inversement proportionnelle à C. »
- **§1.1.2 Expérience 2 — influence de R (p.179)** — Fig.7 : R réglable, C₁ = 0,47 µF ; R₂ = 500 Ω, R₃ = 1 kΩ ; Fig.8 (trois
  courbes, asymptotes tracées). Questions (VERBATIM) : « 1°) Déterminer graphiquement et approximativement les fréquences
  de coupure hautes N'_h2 et N'_h3 obtenues respectivement avec R₂ et R₃. 2°) Calculer pour les trois cas de R, le produit
  N_h.R ; comparer les valeurs trouvées entre elles et en déduire que N_h est inversement proportionnelle à R. »
  Récapitulation : voir Encadrés.
- **§1.1.3 Étude théorique (p.180–183)** — Fig.9 (circuit, u_R, u_C, i) ; Fig.10 (Fresnel, triangle rectangle en A₁ :
  U_Sm, R₁C₁ωU_Sm, U_Em) ; Fig.11 (déphasage) : voir Encadrés. Questions (VERBATIM, p.182) : « 1°) Vérifier de même pour
  les autres cas étudiés expérimentalement qu'il y a toujours accord entre la valeur théorique et la valeur expérimentale
  de N_h. 2°) Montrer que le gain s'écrit : G = - 10 log(1 + x²), où x = N/N_h. »
- **§1.2.1 Manipulation — filtre passe-bas actif (p.183–185)** — Fig.12 : A.O. (µA741 par exemple), R₀ = 159 Ω entre E et
  l'entrée inverseuse, R₁ = 318 Ω et C₁ = 0,47 µF en parallèle entre l'entrée inverseuse et la sortie S, entrée non
  inverseuse à la masse ; u_E(t) = 2sin(2πNt + φ_E) ; N₁ = 1 kHz → Fig.13 (1 V/div ; u_S plus ample, décalée) ; Fig.14
  (G = f(N) : palier ≈ 6 dB, ligne 3 dB, asymptote −20 dB/décade). Questions (VERBATIM) : « 1°) A l'aide des oscillogrammes
  de la figure 13 : a) montrer que le quadripôle est linéaire. b) montrer qu'à la fréquence N₁, u_S est en avance de phase
  par rapport à u_E et U_Sm > U_Em. c) calculer T et G à la fréquence N₁. 2°) A l'aide de la courbe G = f(N), déterminer :
  a) la valeur la plus élevée G₀ de G, calculer (G₀ - 3dB), comparer les différentes valeurs de G à (G₀ - 3dB) et en
  déduire que le quadripôle utilisé est un filtre. b) la (ou les) fréquence(s) de coupure du filtre et la largeur de sa
  bande passante. En déduire qu'il s'agit encore d'un filtre passe bas. 3°) a) Ce filtre est dit actif tandis que le filtre
  RC est considéré comme étant passif. Pourquoi ? b) En exploitant la valeur de G₀ des deux filtres étudiés dans les
  paragraphes 1.1 et 1.2, préciser ce qui différencie le filtre actif du filtre passif. » Analyse : N_h ≈ 1050 Hz, bande
  [0 , 1050 Hz], G > 0 sur un domaine (amplification possible) ; tangente HF coupe G = G₀ en N_h, pente −20 dB/décade ;
  Δφ diminue de 180° à 90° quand N croît ; à N_h, Δφ = 135° = 180° − 45°.
- **§1.2.2 Expérience 1 — influence de C (p.185–186)** — Fig.15 (C réglable, R₀ = 159 Ω, R₁ = 318 Ω) ; C₂ = 0,235 µF,
  C₃ = 0,94 µF ; Fig.16 (trois courbes, même palier ≈ 6 dB). Questions : « 1°) Déterminer graphiquement et
  approximativement : a) le gain maximal G₀ et préciser s'il dépend de C. b) les fréquences de coupure hautes N_h2 et N_h3
  obtenues respectivement avec C₂ et C₃. 2°) Calculer, pour les trois cas étudiés, le produit N_h.C ; comparer les valeurs
  trouvées entre elles et en déduire que N_h est inversement proportionnelle à C. »
- **§1.2.2 Expérience 2 — influence de R₀ (p.186–187)** — Fig.17 (R₀ réglable, R₁ = 318 Ω, C₁ = 0,47 µF) ; R'₀ = 318 Ω,
  R"₀ = 636 Ω ; Fig.18 (paliers ≈ 6, 0 et ≈ −6 dB [lecture], même N_h). Questions : « 1°) Déterminer graphiquement et
  approximativement : a) le gain maximal G₀ pour chacune des valeurs de R₀, R'₀ et R"₀ de la résistance réglable. b) les
  fréquences de coupure hautes N'_h et N"_h obtenues respectivement avec R'₀ et R"₀ ; les comparer à N_h et en déduire que
  la fréquence de coupure haute N_h du filtre est indépendante de R₀. 2°) a) Calculer pour les trois cas étudiés, le
  produit R₀ × 10^(G₀/20), comparer les valeurs trouvées entre elles et avec celle de R₁. b) En déduire que :
  G₀ = 20 log(R₁/R₀) »
- **§1.2.2 Expérience 3 — influence de R₁ (p.187–188)** — Fig.19 (R₁ réglable, R₀ = 159 Ω, C₁ = 0,47 µF) ; R'₁ = 159 Ω,
  R"₁ = 636 Ω (référence R₁ = 318 Ω) ; Fig.20 (paliers ≈ 12, 6 et 0 dB ; N"_h, N_h, N'_h). Questions : « 1°) Déterminer
  graphiquement et approximativement les fréquences de coupure hautes N_h2 et N_h3 obtenues respectivement avec R'₁ et R"₁ ;
  les comparer à N_h1. 2°) Calculer pour les trois cas étudiés, le produit N_h.R₁, comparer les valeurs trouvées entre elles
  et en déduire que la fréquence de coupure N_h est inversement proportionnelle à la résistance réglable R₁. 3°) a)
  Déterminer graphiquement le gain maximal G₀₂ et G₀₃ pour R'₁ et R"₁. b) Calculer pour les trois cas étudiés, le quotient
  R₁/10^(G₀/20), comparer les valeurs trouvées à la valeur de R₀ et en déduire que G₀ = 20 log(R₁/R₀) »
- **§1.2.3 Étude théorique (p.189–191)** — Fig.21 (schéma, i₀, i₁, i_C, ε, i⁺, i⁻) ; Fig.22 et 23 (Fresnel : (R₀/R₁)U_Sm,
  R₀C₁ωU_Sm, U_Em) : voir Encadrés.
- **§2.1 Manipulation — filtre passe-haut CR (p.192–194)** — Fig.24 : E – K – C₁ – S, R₁ entre S et M (sortie aux bornes du
  résistor) ; u_E(t) = 5sin(2πNt) ; N₁ = 100 Hz (Fig.25a : u_S très faible) et N₂ = 5 kHz (Fig.25b : u_S ≈ u_E) ; mesures
  U_Sm(N) → Fig.26 (U_Sm (V) croissante vers 5 V, repère 3,53 V ; G (dB) croissante vers 0, repère −3 ; semi-log 1 Hz–
  10 kHz). Questions (VERBATIM) : « 1°) a) Quel est, parmi les oscillogrammes (1) et (2) de chacune des figures 25a et 25b,
  celui qui correspond à la tension de sortie? En déduire que le quadripôle est linéaire. b) Dire en le justifiant, si
  u_S(t) est en avance ou bien en retard de phase par rapport à u_E(t). 2°) Préciser graphiquement la valeur la plus élevée
  U_Smo de U_Sm, calculer U_Smo/√2, comparer les différentes valeurs de U_Sm à U_Smo/√2 et en déduire que le quadripôle CR
  est un filtre. 3°) a) Déterminer graphiquement la (ou les) fréquence(s) de coupure du filtre et en déduire la largeur de
  sa bande passante. b) A l'encontre de la qualification “passe bas” attribuée au filtre RC, quelle qualification peut-on
  donner au filtre CR ? 4°) Retrouver la largeur de la bande passante du filtre en utilisant la courbe de réponse
  G = h(N). » Analyse : U_Smo = U_Em, G₀ = 0 dB ; N_b ≈ 1050 Hz ; bande [1050 Hz, ∞[ ; u_S en avance quel que soit N, Δφ
  croît avec N [sic : en réalité décroît, cf. théorie] ; « à la fréquence de coupure haute [sic], u_S(t) est en quadrature
  avance de phase par rapport à u_E(t) : Δφ = + π/2 rad (Fig.27) » [sic, contredit la conclusion Δφ = + 45° à N_b] ;
  Remarques : N_b (CR) = N_h (RC) avec les mêmes composants, intersection des courbes G_b(N) et G_h(N) (Fig.28, « N_h = N_b »
  à −3 dB) ; N_b ne dépend que de R et C ; pente +20 dB/décade aux basses fréquences (imprimé « chute de gain est de
  (- 20 dB) par décade »).
- **§2.2 Étude théorique (p.195–198)** — Fig.29 (schéma), Fig.30–31 (Fresnel : U_Sm, U_Sm/(R₁C₁ω), U_Em) : voir Encadrés.
  « Application » (p.197, VERBATIM) : « Pour le filtre réalisé avec C₁ = 0,47µF et R₁ = 318 Ω, calculer N_b et la comparer à
  sa valeur expérimentale. Y a-t-il accord entre la valeur théorique et la valeur expérimentale de N_b? »
- **§3.1 Manipulation — filtre passe-bande RLC (p.198–201)** — introduction (VERBATIM) : « Les filtres passifs étudiés
  précédemment sont réalisés par une association en série d'un résistor et d'un codensateur [sic]. Qu'en est-il pour un
  quadripôle réalisé avec un circuit RLC série ayant comme sortie les bornes du résistor ? » ; montage de la résonance
  d'intensité du chapitre 5 : R₀ = 50 Ω, C = 0,47 µF, L = 0,2 H, r = 12,5 Ω ; U_Em = 2 V, N réglable ; résistor à la masse,
  u_S = u_R0 (Fig.32 : E – K – C – (L, r) – S, R₀ entre S et M) ; N₁ = 400 Hz, N₂ = 500 Hz, N₃ = 600 Hz → Fig.33a, b, c
  (mêmes sensibilités verticales ; u_S faible et en avance à 400 Hz, presque en phase et ample à 500 Hz, faible et en
  retard à 600 Hz). Questions (VERBATIM) : « 1°) a) Quel est parmi les oscillogrammes (1) et (2) de chacune des figures
  33a, 33b et 33c celui qui correspond à la tension de sortie, en déduire que le quadripôle est linéaire. b) En quoi
  diffère le signe du déphasage entre u_S(t) et u_E(t) de ceux des filtres passifs précédemment étudiés ? 2°) Les résultats
  des mesures qui ont permis de tracer la courbe d'évolution de l'amplitude I_m de l'intensité i du courant en fonction de N
  au chapitre 5 (paragraphe 2), sont consignés dans le tableau suivant : [N (Hz) 440 / 460 / 480 / 500 / 520 / 540 / 560 /
  580 / 600 ; I_m (mA) 8,9 / 11,8 / 16,7 / 25,2 / 32 / 25,8 / 17,2 / 12,7 / 10,1] a) Reproduire le tableau, y insérer une
  ligne pour le calcul des tensions maximales U_Sm correspondant aux intensités maximales I_m relevées en fonction de N et
  une ligne pour le calcul du gain G. b) Tracer les courbes de réponse du quadripôle U_Sm =f(N) et G = h(N) dans le même
  système d'axes. 3°) Décrire la courbe U_Sm = f(N) et préciser la valeur la plus élevée U_Smo de U_Sm, calculer U_Smo/√2,
  comparer les différentes valeurs de U_Sm à U_Smo/√2 et en déduire que le quadripôle RLC est un filtre. 4°) a) Déterminer
  graphiquement la (ou les) fréquence(s) de coupure du filtre et en déduire la valeur de la largeur de sa bande passante.
  b) Quelle qualification peut-on attribuer a [sic] ce filtre ? 4°) [sic, pour 5°)] Retrouver la valeur de la largeur de
  la bande passante du fil -tre en utilisant la courbe de gain G = h(N). » Analyse : Fig.34 (quadrillage linéaire,
  410–580 Hz : U_Sm max 1,6 V, repère 1,13 V ; G max −1,94 dB, repère −4,94 dB) ; N₀ = 519 Hz ; bande [495 Hz, 545 Hz] ;
  N_b = 495 Hz, N_h = 545 Hz ; Remarque (N_h + N_b)/2 = N₀ « fréquence centrale » (symétrie de la courbe).
- **§3.2 Étude théorique (p.201–206)** — Fig.35 (schéma), Fig.36a/b/c (Fresnel pour Lω > 1/Cω, = , <) : voir Encadrés ;
  Questions (VERBATIM) : p.203 « Montrer que T₀ est la valeur maximale de la transmittance T et qu'elle est atteinte à la
  fréquence N = N₀. » ; p.205 « Montrer que pour un filtre passe bande sélectif (Q >> 1), les fréquences de coupure sont
  telles que : (N_b + N_h)/2 = N₀ On rappelle que : N_b = (N₀/2Q)[−1 + √(1 + 4Q²)] et N_h = (N₀/2Q)[+1 + √(1 + 4Q²)] » ;
  p.205 « Montrer que le déphasage Δφ entre u_S et u_E est égal à (- 45°) pour N = N_h et à (+ 45°) pour N = N_b. » ;
  Fig.37 (T = f(N) en quadrillage linéaire, 0–1000 Hz ; R₀ = 50 Ω : pic ≈ 0,8 étroit ; R₀₁ = 100 Ω : pic ≈ 0,88 ; R₀₂ =
  500 Ω : pic ≈ 0,97 large).
- **§4 Applications (p.206)** — voir Encadrés ; Fig.38 table de mixage (« réglage de tonalité (graves, médiums, aiguës
  -12 dB à +12 dB). Bande passante : [20 Hz, 20 kHz] ») ; note ADSL.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Filtre passe-bas passif — constat (p.178)** — « On a : G = (G₀ -3 dB), avec G₀ = 0 dB pour une fréquence unique égale
> à 1070 Hz. Pour N < 1070 Hz, la chute de gain est inférieure à 3 dB. Donc, il s'agit d'un filtre passe bas et 1070 Hz est
> la fréquence de coupure haute : N_h = 1070 Hz. Par suite, la bande passante [0 , 1070Hz] du filtre a comme largeur :
> ΔN = 1070 Hz. » Remarque : « Etant réalisé uniquement avec des composants passifs (condensateur, résistor), un tel filtre
> est dit passif. La tangente à la partie de la courbe correspondant aux hautes fréquences coupe l'axe des fréquences au
> point d'abscisse N_h et sa pente est égale à (- 20 dB) par décade. »

> **Récapitulation (p.179–180)** — « ■ Avec R constante, N_h est inversement proportionnelle à C. ■ Avec C constante, N_h
> est inversement proportionnelle à R. Donc, la fréquence de coupure N_h est inversement proportionnelle à la constante de
> temps τ = RC, ce qui signifie : N_h = (1/k) × (1/RC), où k est une constante dont le calcul par recours à l'une des
> valeurs de N_h trouvées donne : k = 2π. On a alors : **N_h = 1/(2πRC)** »

> **Équation différentielle RC (p.180)** — « On a : u_R(t) + u_S(t) = u_E(t) Or, u_S(t) = u_C(t) En convention récepteur :
> u_C(t) = q(t)/C₁, où q est la charge portée par l'armature du condensateur vers laquelle est orienté le sens du courant.
> u_R(t) = R₁i(t). D'où : u_S + R₁i = u_E Or, i = dq/dt et u_S = q/C₁, ce qui équivaut : q = C₁u_S. Donc,
> u_R = R₁C₁ du_S/dt. Ceci conduit à l'équation différentielle en u_S : **u_S + R₁C₁ du_S/dt = u_E** Avec
> u_E = U_Em sin(ωt+φ_E), cette équation admet comme solution particulière : u_S(t) = U_Sm sin(ωt+φ_S). C'est bien
> l'expression de u_S en régime permanant [sic] du filtre. »

> **Transmittance RC (p.180–181)** — « u_S(t) → OA⃗₁ [U_Sm , φ_S] ; R₁C₁ du_S(t)/dt → OA⃗₂ [R₁C₁ωU_Sm , φ_S + π/2] ;
> u_E(t) → OA⃗ [U_Em , φ_E]. […] OA⃗₁ + OA⃗₂ = OA⃗ […] Le triangle OA₁A étant rectangle en A₁, on a :
> U_Em² = U_Sm² + (R₁C₁ωU_Sm)² ce qui équivaut : (U_Sm/U_Em)² = 1/(1 + (R₁C₁ω)²). […] Donc, T = 1/√(1 + (R₁C₁ω)²), ce qui
> revient à écrire : **T = 1/√(1 + (2πR₁C₁N)²)** sachant que ω = 2πN. R₁C₁ω > 0, d'où √(1 + (R₁C₁ω)²) > 1. Donc, T < 1 ∀ N.
> Toutefois, aux très basses fréquences, R₁C₁ω devient négligeable devant 1. Par conséquent T ≈ 1 » ; Remarque :
> « U_Em = ZI_m avec Z = √(R₁² + (1/C₁ω)²) ; U_Sm = Z_C I_m avec Z_C = 1/(C₁ω). Donc, **T = Z_C/Z** »

> **Gain et bande passante RC (p.181–182)** — « G = 20 logT. […] Finalement : **G = - 10 log[1 + (2πR₁C₁N)²]** T étant
> inférieure à l'unité ∀ N, le gain G est < 0. A la limite, quand N → 0, G → 0 » ; « La bande passante à (- 3 dB) est
> telle que : G ≥ (G₀ - 3 dB) Ce qui signifie : - 10 log[1 + (2πR₁C₁N)²] ≥ - 3, car G₀ = 0 dB Par suite,
> log[1 + (2πR₁C₁N)²] ≤ 0,3. D'où, 2πR₁C₁N ≤ √(10^0,3 − 1) ; 2πR₁C₁N ≤ 0,998. Or, 0,998 ≈ 1 Donc, N ≤ 1/(2πR₁C₁).
> N ≤ N_h avec **N_h = 1/(2πR₁C₁)** : fréquence de coupure haute. Donc, il s'agit d'un filtre passe bas de bande passante :
> **[0, 1/(2πR₁C₁)]** » ; Application : « Pour le filtre RC réalisé avec R₁ = 318 Ω et C₁ = 0,47 µF, le calcul donne
> N_h = 1064 Hz, ce qui est très proche de la valeur expérimentale 1070 Hz. » ; Remarque : « La fréquence de coupure haute
> ne dépend que des grandeurs R et C caractéristiques du filtre, donc c'est une grandeur caractéristique du filtre. »

> **Déphasage RC (p.182)** — « Δφ = φ_S - φ_E (cas où φ_E = 0 rad) D'après la construction de la figure 11, Δφ < 0 ∀ N. De
> plus, - π/2 rad < Δφ < 0, ce qui signifie que la tension de sortie u_S(t) évolue toujours en retard de phase par rapport
> à la tension d'entrée u_E(t). De plus, tgΔφ = - ‖A₁A‖/‖OA₁‖, ce qui donne : tgΔφ = - R₁C₁ω. Il vient donc :
> **tgΔφ = - N/N_h** - Quand N → 0, tgΔφ → 0. Donc, φ_S → 0 : u_S en phase avec u_E - Quand N → ∞, tgΔφ → - ∞. Donc,
> φ_S → - π/2 rad. - Quand N → N_h, tgΔφ → -1 . Donc, φ_S → - π/4 rad. »

> **Conclusion (§1.1, p.183, encadré)** — « Le quadripôle RC (avec condensateur relié à la masse) est un filtre passe bas
> caractérisé par la fréquence de coupure haute : **N_h = 1/(2πRC)** La tension de sortie u_S d'un filtre passe bas RC est
> toujours en retard de phase par rapport à la tension d'entrée. Pour N = N_h, Δφ = φ_S - φ_E = - π/4 rad. Le filtre est
> passif (absence de composants actifs, G < 0 ...) »

> **Récapitulation filtre actif (p.188)** — « ◆ Le gain maximal est indépendant de C, il dépend uniquement de R₀ et de R₁.
> Le recours au calcul montre que : R₀.10^(G₀/20) = R₁ et R₁/10^(G₀/20) = R₀ d'où : **G₀ = 20 log(R₁/R₀)** ◆ La fréquence de
> coupure haute N_h est indépendante de R₀; elle est inversement proportionnelle au produit R₁C. Par le recours à l'une des
> valeurs trouvées, le calcul montre que : **N_h = 1/(2πR₁C)** »

> **Équation différentielle du passe-bas actif (p.189)** — « En supposant l'amplificateur opérationnel utilisé idéal, on a :
> i⁺ = i⁻ = 0 et ε = 0 u_S = - R₁ i₁ - ε . Or, ε = 0, d'où : i₁ = - u_S/R₁. D'après la loi des noeuds, on a au point A :
> i₀ = i₁ + i_C. i_C = dq/dt […] En convention récepteur : u_C = q/C₁. Or, u_C = - u_S. Donc, on a : q = - C₁u_S. Par
> suite, i_C = - C₁ du_S/dt u_E = R₀i₀ - ε. Or, ε = 0. On a donc : i₀ = u_E/R₀. Ainsi, on a : u_E/R₀ = - u_S/R₁ - C₁ du_S/dt,
> ce qui est équivalent à : **(R₀/R₁)u_S + R₀C₁ du_S/dt = - u_E** » ; solution u_S(t) = U_Sm sin(ωt + φ_S). (Le texte renvoie
> à « la figure 11 » pour le circuit : lire figure 12 [sic].)

> **Transmittance et gain du passe-bas actif (p.189–190)** — « (R₀/R₁)u_S(t) → OA⃗₁ [(R₀/R₁)U_Sm , φ_s] ;
> R₀C₁ du_S/dt → OA⃗₂ [R₀C₁ωU_Sm , φ_s + π/2] ; (– u_E(t)) = U_Em sin(ωt + φ_E + π) → OA⃗ [U_Em , φ_E + π] » ;
> « (U_Em)² = ((R₀/R₁)U_Sm)² + (R₀C₁ωU_Sm)² ce qui équivaut (U_Sm/U_Em)² = (R₁/R₀)² / (1 + (R₁C₁ω)²) » ;
> « **T = (R₁/R₀) × 1/√(1 + (2πR₁C₁N)²)** sachant que ω = 2πN » ; « aux très basses fréquences, R₁C₁ω devient négligeable
> devant 1. Par conséquent **T₀ = R₁/R₀** Donc, T = T₀/√(1 + (R₁C₁ω)²) ≤ R₁/R₀ ∀ N. » Remarque : « – Si R₁ > R₀, on a T₀ > 1 :
> le signal filtré est amplifié. – Si R₁ = R₀, on a T₀ = 1. – Si R₁ < R₀, on a T₀ < 1 : le signal filtré est atténué. » ;
> « G = 20 logT₀ - 10 log(1 + (R₁C₁ω)²) Or, √(1 + (R₁C₁ω)²) ≥ 1. Donc, G ≤ 20logT₀ ou encore, G ≤ G₀, avec G₀ = 20 logT₀ :
> valeur maximale du gain. Finalement, on a : **G = G₀ - 10 log(1 + (R₁C₁ω)²)** » ; Remarque (p.191) : R₁ > R₀ ⇒ G₀ > 0 ;
> R₁ = R₀ ⇒ G₀ = 0 ; R₁ < R₀ ⇒ G₀ < 0.

> **Bande passante et déphasage du passe-bas actif (p.191)** — « G ≥ (G₀ - 3dB). […] 10 log[1 + (R₁C₁ω)²] ≤ 3. Par suite,
> log[1 + (R₁C₁ω)²] ≤ 0,3. D'ou, R₁C₁ω ≤ √(10^0,3 − 1). Or, √(10^0,3 − 1) ≈ 1. On a : ω = 2πN. D'où, N ≤ 1/(2πR₁C₁). On a
> ainsi : N ≤ N_h avec **N_h = 1/(2πR₁C₁)** : fréquence de coupure haute. Donc, il s'agit d'un filtre passe bas de bande
> passante : [0, 1/(2πR₁C₁)] » ; « D'après la construction de Fresnel de la figure 23 : Δφ > 0. De plus : - lorsque N → 0,
> Δφ → 180° - lorsque N → ∞, Δφ → 90° On a alors : 90° ≤ Δφ ≤ 180° ∀ N. »

> **Conclusion (§1.2, p.191, encadré)** — « Avec les mêmes composants d'un filtre pase [sic] bas RC (filtre passif), on peut
> réaliser autour d'un amplificateur opérationnel, un autre filtre passe bas (filtre actif) de même fréquence de coupure
> haute : **N_h = 1/(2πRC)** Contrairement au filtrage réalisé avec un filtre passe bas passif, le filtrage obtenu avec un
> fitre [sic] passe bas actif peut être accompagné d'une amplification du signal. »

> **Équation différentielle CR (p.195)** — « la tension de sortie n'est autre que celle aux bornes du résistor qui s'écrit
> en convention récepteur u_S = R₁i. D'autre part : u_E(t) = u_C(t) + u_R(t) ; u_C = q/C₁ […] q(t) = ∫i(t)dt. Or,
> u_S = R₁i. Donc, q(t) = (1/R₁)∫u_S(t)dt. […] u_C(t) = (1/R₁C₁)∫u_S(t)dt On a ainsi : u_E(t) = u_S(t) +
> (1/R₁C₁)∫u_S(t)dt. En dérivant cette équation membre à membre par rapport au temps, on aboutit à l'équation
> différentielle : **R₁C₁ du_S(t)/dt + u_S(t) = R₁C₁ du_E(t)/dt** » ; solution u_S(t) = U_Sm sin(ωt + φ_S).

> **Transmittance, gain, bande passante CR (p.195–197)** — « u_S(t) → OA⃗₁ [U_Sm, φ_S] ; (1/R₁C₁)∫u_S(t)dt =
> (U_Sm/R₁C₁ω) sin(ωt + φ_S − π/2) → OA⃗₂ = [U_Sm/R₁C₁ω, φ_S − π/2] ; u_E(t) → OA⃗ = [U_Em, φ_E] » ; « (U_Em)² = (U_Sm)² +
> (U_Sm/R₁C₁ω)² » ; « **T = 1/√(1 + 1/(2πR₁C₁N)²)** » ; « T ≤ 1 ∀ N. Toutefois, aux très hautes fréquences, 1/(2πR₁C₁N)²
> devient négligeable devant 1. Par conséquent T = 1 » ; « **G = − 10 log[1 + (1/(2πR₁C₁N))²]** » ; « G ≤ 0 ; A la limite,
> quand N → ∞, G = 0 dB » ; bande passante : « -10 log(1 + (1/(2πR₁C₁N))²) ≥ − 3 […] log(…) ≤ 0,3 [imprimé « ≥ - 0,3 », sic]
> D'où, 1/(R₁C₁ω) ≤ √(10^0,3 − 1). Donc, N ≥ 1/(2πR₁C₁). N ≥ N_b avec **N_b = 1/(2πR₁C₁)** : fréquence de coupure basse.
> Donc, il s'agit d'un filtre passe haut de bande passante : **[1/(2πR₁C₁), ∞[** »

> **Déphasage CR (p.197–198)** — « D'après la construction de la figure 31, Δφ > 0 ∀ N. De plus, 0 < Δφ < π/2 rad, ce qui
> signifie que la tension de sortie u_S(t) évolue toujours en avance de phase par rapport à la tension d'entrée u_E(t). On
> a, tgΔφ = ‖A₁A₂‖/‖OA₁‖ [sic, lire A₁A], ce qui donne : tgΔφ = 1/(2πR₁C₁N). Il vient donc : **tgΔφ = N_b/N** car
> N_b = 1/(2πR₁C₁N) [sic : N en trop au dénominateur] - Quand N → 0, tgΔφ → ∞. Donc, φ_s → π/2 rad. - Quand N → ∞,
> tgΔφ → 0. Donc, φ_s → 0 rad. - Quand N → N_b, tgΔφ → 1. Donc, φ_s → π/4 rad. »

> **Conclusion (§2, p.198, encadré)** — « Le quadripôle CR (avec résistor relié à la masse) est un filtre passe haut
> caractérisé par une fréquence de coupure basse : **N_b = 1/(2πRC)** La tension de sortie u_S d'un filtre passe haut passif
> CR est toujours en avance de phase par rapport à la tension d'entrée u_E. Pour N = N_b, Δφ = + 45°. »

> **Passe-bande — constat (p.199–201)** — « L'expérience réalisée montre qu'en appliquant à l'entrée du quadripôle RLC (avec
> le résistor du côté de la masse), une tension sinusoïdale u_E de fréquence N, on récupère à la sortie du quadripôle (aux
> bornes du résistor) une tension u_S(t) synchrone avec u_E(t) : u_S(t) = U_Sm sin(2πNt+φ_S). Donc, il s'agit d'un
> quadripôle linéaire. […] Selon la fréquence de la tension délivrée entre les bornes du générateur, la tension de sortie
> u_S(t) est en avance, en retard ou en concordence [sic] de phase par rapport à u_E(t). En d'autres termes, contrairement
> aux filtres passe bas et passe haut, le déphasage Δφ = (φ_S - φ_E) entre la tension de sortie u_S(t) et la tension
> d'entrée u_E(t) du présent filtre change de signe en fonction de N. » ; « U_Sm est maximale pour une fréquence unique et
> particulière qui correspond à la fréquence propre N₀ = 519 Hz du circuit RLC série étudié et que de part et d'autre de
> N₀, U_Sm diminue jusqu'à atteindre des valeurs inférieures à U_Smo/√2. Donc, le quadripôle étudié est un filtre. Pour
> toute fréquence N de la bande [495 Hz, 545 Hz], U_Sm > U_Smo/√2 ( ou encore G > G₀ -3 dB), la chute de gain est inférieure
> à 3 dB. Donc, il s'agit d'un filtre passe bande. Les fréquences limites de cette bande sont respectivement la fréquence de
> coupure basse N_b = 495 Hz et la fréquence de coupure haute N_h = 545 Hz du filtre réalisé. Par suite, la bande passante
> du filtre est : [495 Hz, 545 Hz] » ; Remarque : « On peut vérifier qu'aux erreurs expérimentales près, on a :
> **(N_h + N_b)/2 = N₀** Etant donné la symétrie de la courbe de réponse tracée par rapport à la droite N = N₀, ce résultat
> est attendu, d'où la qualification de N₀ comme étant la fréquence centrale. »

> **Équation différentielle RLC (p.201–202)** — « u_S(t) = R₀.i(t) On a u_E = u_C + u_B + u_S En convention récepteur :
> u_B(t) = ri(t) + L di(t)/dt. Or, i(t) = u_S(t)/R₀ D'où, u_B(t) = (r/R₀).u_S(t) + (L/R₀).du_S(t)/dt. u_C(t) = q(t)/C […]
> q(t) = (1/R₀)∫u_S(t)dt. D'où, u_C(t) = (1/R₀C)∫u_S(t)dt Par suite : u_E(t) = (1/R₀C)∫u_S(t)dt + (1+ r/R₀)u_S(t) +
> (L/R₀) du_S(t)/dt En dérivant cette équation membre à membre par rapport au temps, on aboutit à l'équation
> différentielle : **(1/R₀C)u_S(t) + (1+ r/R₀) du_S(t)/dt + (L/R₀) d²u_S(t)/dt² = du_E(t)/dt** » ; solution
> u_S(t) = U_Sm sin(ωt + φ_S) « traduisant l'évolution de u_S(t) en régime permanent ».

> **Transmittance RLC (p.202–203)** — « (1+ r/R₀) × u_S(t) → OA⃗₁ [(1+ r/R₀)U_Sm, φ_S] ; (L/R₀) × du_S(t)/dt → OA⃗₂
> [LωU_Sm/R₀, φ_S + π/2] ; (1/R₀C)∫u_S(t)dt → OA⃗₃ [U_Sm/(R₀Cω), φ_S − π/2] ; u_E(t) → OA⃗ [U_Em, φ_E] » ; « Le triangle OA₁A
> étant rectangle en A₁, on a : (U_Sm/U_Em)² = 1 / ((R/R₀)² + (Lω/R₀ − 1/(R₀Cω))²), avec R = R₀ + r Par suite,
> **T = (R₀/R) × 1/√(1 + (Lω/R − 1/(RCω))²)** Soit **ω₀ = 1/√LC**, la pulsation propre de l'oscillateur,
> **Q = Lω₀/R = 1/(RCω₀)** : facteur de surtension à la résonance. En posant : ∞ x = ω/ω₀ = N/N₀ que l'on appelle pulsation
> ou fréquence réduite, ∞ T₀ = R₀/R, la transmittance s'écrit : **T = T₀ / √(1 + Q²(x − 1/x)²)** Or,
> √(1 + Q²(x − 1/x)²) ≥ 1 . Donc, T ≤ T₀ ; T₀ = R₀/R ≤ 1 car R₀ ≤ R. Finalement, on a : ∀N, T ≤ 1. Par conséquent, le filtre
> passif passe bande est un atténuateur de tension. » (puces « ∞ » : glyphe parasite imprimé.)

> **Gain RLC (p.203)** — « **G = 20 log [T₀ / √(1 + Q²(x − 1/x)²)]**. Comme la transmittance, le gain est maximum à N = N₀ :
> **G₀ = 20 logT₀**. T₀ ≤ 1. Donc, G₀ ≤ 0. Il s'en suit : G ≤ 0 ∀N. »

> **Bande passante RLC (p.203–204)** — « G ≥ (G₀ − 3 dB), ce qui signifie : 20 log [T₀/√(1 + Q²(x − 1/x)²)] ≥ 20 logT₀ - 3,
> d'où : log[1 + Q²(x − 1/x)²] ≤ 3/10, ce qui permet d'aboutir à : (x − 1/x)² ≤ 1/Q². Il s'en suit : - 1/Q ≤ x − 1/x ≤ 1/Q.
> La résolution de l'inéquation (- 1/Q ≤ x − 1/x) qui s'écrit : x² + x/Q - 1 ≥ 0 donne x ≥ (1/2Q)[-1 + √(1 + 4Q²)] La
> résolution de l'inéquation (x − 1/x ≤ 1/Q) qui s'écrit : x² - x/Q - 1 ≤ 0 donne x ≤ (1/2Q)[1 + √(1 + 4Q²)] On a ainsi :
> x_b ≤ x ≤ x_h […] N₀x_b ≤ N ≤ N₀x_h, ce qui revient à écrire N_b ≤ N ≤ N_h, avec : **N_b = (N₀/2Q)[-1 + √(1 + 4Q²)]** :
> fréquence de coupure basse, **N_h = (N₀/2Q)[+1 + √(1 + 4Q²)]** : fréquence de coupure haute. » ; « Largeur de la bande
> passante du filtre ΔN = N_h − N_b. En remplaçant N_b et N_h par leur expression, on obtient : **ΔN = N₀/Q** » (3/10 :
> approximation de log 2 non signalée.)

> **Sélectivité et facteur de qualité (p.204–205)** — « Un filtre passe bande est dit sélectif lorsque la largeur ΔN de sa
> bande passante est nettement petite devant sa fréquence propre N₀. On a : ΔN = N₀/Q. Il est clair alors que pour N₀
> donnée, la bande passante est d'autant plus étroite que la constante Q est plus grande. Donc, la sélectivité du filtre
> augmente avec Q, d'où le nom de facteur de qualité pour la constante Q caractéristique du filtre. **Q = Lω₀/R = 1/(RCω₀)**
> : facteur de qualité Un filtre n'est sélectif que si Q est nettement supérieur à 1. » Remarque : « Pour L et C données,
> le filtre RLC est d'autant plus sélectif que sa résistance totale R est plus petite (Fig.37). »

> **Déphasage RLC (p.205)** — « D'après les constructions de Fresnel de la figure 36, le déphasage Δφ = φ_S - φ_E entre u_S
> et u_E, est tel que : **- π/2 rad < Δφ < π/2 rad**, ce qui montre que u_S peut être en avance de phase, en phase ou en
> retard de phase par rapport à u_E. »

> **Conclusion (§3, p.206, encadré)** — « Le circuit RLC série monté en quadripôle de manière que la tension aux bornes du
> résistor soit la tension de sortie est un filtre passe bande caractérisé par une bande passante de largeur :
> **ΔN = N_h − N_b = N₀/Q** où **N₀ = 1/(2π√LC)** est la fréquence centrale et **Q = Lω₀/R** est le facteur de qualité du
> filtre. »

> **Remarque générale (p.206)** — « Du fait que les équations différentielles des filtres passe bas et passe haut étudiés
> font intervenir en plus de u_S(t) uniquement sa dérivée première par rapport au temps, ils sont qualifiés comme étant des
> filtres du premier ordre (ou d'ordre 1), tandis que le filtre passe bande RLC série dont l'équation différentielle fait
> intervenir de plus, la dérivée seconde de u_S(t) est qualifié de filtre du second ordre (ou d'ordre 2). »

> **Applications (§4, p.206)** — « Les applications des filtres électriques sont nombreuses et multiples dans plusieurs
> domines [sic] comme en télécommunications, en acoustique, en mécanique... On cite essentiellement l'émission et la
> réception radio ou de télévision, la correction audio ou vidéo, l'analyse de spectres, l'antiparasitage, la
> distortiométrie, les générateurs de fonctions, la modulation et démodulation de signaux que l'on va étudier aux chapitres
> 12 et 13... » ; ADSL (conversation téléphonique en basses fréquences audibles, télévision en hautes fréquences, IP à haut
> débit ; note : « ADSL : “Asymmetric Digital Subscriber Line” signifiant en français une liaison numérique à débit
> asymétrique. ») ; « Les filtres passe bas ainsi que ceux passe haut sont utilisés en acoustique comme atténuateurs de
> composantes respectivement aigües et graves d'un signal audio. Les filtres passe bande peuvent servir à éliminer le bruit
> du signal […] ; ils permettent la sélection de la fréquence radio écoutée, des canaux ou chaînes de télévision, des
> vibrations sonores à détecter par un microphone ou un sismographe ; en Hi Fi, ils sont à la base des équaliseurs et des
> tables de mixage (Fig.38)... »

> **L'essentiel (p.207–208, VERBATIM, lu sur l'image)** — « ■ Les filtres passifs sont caractérisés par : **T ≤ 1 et
> G ≤ 0 dB, ∀ N** d'où une atténuation du signal. ■ Le filtre passe bas actif peut avoir un gain positif, d'où une
> amplification possible du signal. ■ Le filtre passif passe bas RC est un filtre du premier ordre caractérisé par : - une
> fréquence de coupure haute : **N_h = 1/(2πRC)** - une transmittance : **T = 1/√(1+(2πRCN)²). ∀ N, T ≤ 1** -un gain :
> **G = -10 log(1+(2πRCN)²)** - une tension de sortie en retard de phase par rapport à la tension d'entrée :
> **– 90° ≤ φ_S - φ_E ≤ 0, ∀N** ■ Le filtre actif passe bas réalisé avec un amplificateur opérationnel, un condensateur et
> des résistors est un filtre du premier ordre, caractérisé par : - une fréquence de coupure haute : **N_h = 1/(2πR₁CN)**
> [sic : N en trop] - une transmittance : **T = T₀/√(1+ (2πR₁CN)²) ; T₀ = R₁/R₀** - un gain : **G = G₀ -10 log(1+(2πRCN)²) ;
> G₀ = 20 logT₀** [sic : R pour R₁] - une tension de sortie en avance de phase par rapport à la tension d'entrée :
> **90° ≤ φ_S - φ_E ≤ 180° ; ∀N** ■ Le filtre passif passe haut CR est un filtre du premier ordre caractérisé par : - une
> fréquence de coupure basse : **N_b = 1/(2πRCN)** [sic : N en trop] - une transmittance :
> **T = 1/√(1+ 1/(2πRCN)²) ; T ≤ 1 ∀N** - un gain : **G = - 10 log(1+ 1/(2πRCN)²)** - une tension de sortie en avance de
> phase par rapport à la tension d'entrée : **0 ≤ φ_S - φ_E ≤ π/2 rad, ∀N** ■ Le filtre passif passe bande RLC série est un
> filtre du second ordre caractérisé par : - une transmittance : **T = T₀/√(1 + Q²(x − 1/x)²)** où x = N/N₀ = ω/ω₀ et
> Q = Lω₀/R - un gain : **G = 20 log [T₀/√(1+ Q²(x − 1/x)²)] ; G₀ = 20 logT₀** - une bande passante de largeur :
> **ΔN = N_h - N_b = N₀/Q** - une tension de sortie pouvant être en avance, en retard ou en concordance de phase avec la
> tension d'entrée : **– π/2 rad < φ_S - φ_E < π/2 rad , ∀N** » (le symbole degré est imprimé « ϒ » : « – 90ϒ », « 90ϒ ».)

### Exercices résolus

- **Exercice résolu (p.209–211)** — Énoncé : **I-** filtre RC (Fig.1 : R entre E et S, C entre S et M), u_E(t) =
  U_Em sin(2πNt + π/2), R = 160 Ω, C = 1 µF. 1°) équation différentielle de u_S, filtre du premier ordre ; 2°) a) U_Sm ;
  b) T et G ; 3°) a) filtre passe bas ; b) N_h ; c) pour N = N_h, Δφ et φ_S. **II-** avec R' et le même condensateur, filtre
  passe haut, même u_E : 1°) schéma ; 2°) Fig.2 (deux courbes de gain (1) et (2), semi-log) : a) identifier le passe haut ;
  b) N_b et R'. **III-** passe bande : C = 0,5 nF, bobine purement inductive L = 9,8 mH, R = 370 Ω : 1°) a) Q ; b) ΔN ;
  c) sélectif ? 2°) a) montrer N_b = N₀ − ΔN/2, en déduire N_h = N₀ + ΔN/2 ; b) N_b et N_h. Solution : I-1°) u_S + RC du_S/dt
  = u_E, premier ordre ; 2°a) Fresnel (OA⃗₁ [U_Sm, φ_S + π/2] [sic : lire φ_S], OA⃗₂ [RCωU_Sm, φ_S + π] [sic : lire
  φ_S + π/2], OA⃗ [U_Em, π/2]) → **U_Sm = U_Em/√(1 + (2πRCN)²)** ; b) **T = 1/√(1 + (2πRCN)²)**, **G = −10 log[1 + (2πRCN)²]** ;
  3°a) N → 0 : T → 1 ; N → ∞ : T → 0 → passe bas ; b) 2πRCN = √(10^0,3 − 1) = 0,998 ≈ 1 → N_h = 1/(2πRC), « A.N. :
  N_b = 995 Hz » [sic : N_h] ; c) tg(φ_S − φ_E) = − N/N_h = −1 → **φ_S − φ_E = −π/4 rad**, φ_E = π/2 → **φ_S = π/4 rad** ;
  II-1°) Fig.3 (C entre E et S, R' entre S et M) ; 2°a) courbe (1) (gain élevé aux hautes fréquences) ; b) **N_b = 2 kHz**,
  R' = 1/(2πN_bC) → **R' = 80 Ω** ; III-1°a) ω₀ = 451,754.10³ rad.s⁻¹, **Q = 11,96 ≈ 12** ; b) N₀ = ω₀/2π = 71,935 kHz
  ≈ 72 kHz, **ΔN = 6,014 kHz ≈ 6 kHz** ; c) Q nettement supérieur à 1 → sélectif (2ᵉ méthode : ΔN très petit devant N₀) ;
  2°a) 4Q² >> 1 → N_b ≈ (N₀/2Q)(−1 + 2Q) = N₀ − N₀/2Q → N_b ≈ N₀ − ΔN/2 ; N_h = N_b + ΔN [imprimé « N_b = N_h − ΔN »] → N_h ≈
  N₀ + ΔN/2 ; b) **N_b = 68,9 kHz ; N_h = 74,9 kHz**.

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux (p.212)** : 1- un passe bas a pour fonction le filtrage des signaux de fréquences supérieures à
  N_h ; 2- on appelle fréquence de coupure toute fréquence arrêtée par le filtre ; 3- un filtre passif a pour fonctions le
  filtrage et l'amplification ; 4- le passe bas actif peut amplifier les signaux de fréquence inférieure à sa « fréquence de
  coupure basse » ; 5- la réponse d'un passe bas à un signal sinusoïdal est un signal sinusoïdal de fréquence plus basse ;
  6- à la sortie d'un passe haut RC, le signal est déphasé de 45° par rapport à l'entrée ; 7- la fréquence de coupure d'un
  filtre résistor + condensateur ne dépend que de R et C ; 8- la bande passante d'un passe bande est d'autant plus étroite
  que Q est plus petit. (Pas de réponse imprimée.)
- **Ex. 2 — QCM (p.212)** : I- courbe T(N) croissante vers un palier : a- passe haut ; b- passe bas ; c- passe bande.
  II- courbe G(N) (palier 0 dB, chute au-delà de ≈ 10³ Hz ; axe 1–10³ Hz) : a- type (a-1 passe bas, a-2 passe bande, a-3
  passe haut) ; b- fréquence de coupure (1000 / 1100 / 1200 Hz) ; c- bande passante ([0 ; 1000 Hz] ; [1100 Hz ; ∞] ;
  [1000 Hz ; ∞]). III- passe bas actif : a- U_Sm toujours < U_Em ; b- toujours > ; c- inférieure ou supérieure.
  IV- quadripôle (R en série, dipôle D en sortie) avec U_Sm = U_Em à très haute fréquence : D est a- un résistor ; b- un
  condensateur ; c- un A.O. V- courbe G(N) d'un passe bas actif : courbe (1) (palier ≈ 2 dB puis chute), (2) (palier 0 dB
  puis chute), (3) (creux, type réjecteur). (Pas de réponse imprimée.)

### Exercices et problèmes

- **Ex. 3 (p.213)** — filtre RC (R entre E et S, C entre S et M), C = 0,1 µF, R = 1,59 kΩ, u_E(t) = U_Em sin(ωt). 1°) a) u_S(t)
  (filtre linéaire) ; b) fonction de transfert ; c) G en dB ; 2°) a) tableau G pour N = 10 / 100 / 200 / 500 / 1000 / 10⁴ /
  10⁵ Hz ; b) G = f(N) en semi-log, type de filtre ; c) fréquence de coupure et largeur de bande ; 3°) a) Δφ pour N = 1 kHz ;
  b) u_S(t) avec « U_E = 2 V » [?] (notation d'une valeur efficace, mais la réponse p.393 « U_Sm ≈ 1,4 V » à N = N_h
  suppose U_Em = 2 V).
- **Ex. 4 (p.213)** — filtre CR (C entre E et S, R entre S et M), R = 1 kΩ, C = 10 nF. 1°) nature ; 2°) T, valeur pour
  N = 0 et N infinie ; 3°) N_c à 3 dB, bande passante ; 4°) allure de G = f(N) pour 0,1 N_c < N < 10 N_c.
- **Ex. 5 (p.213)** — A.O. idéal, R₁ (entrée), R₂ et C en parallèle (rétroaction) : passe bas actif inverseur. 1°) fonction
  de transfert ; 2°) nature ; 3°) fréquence de coupure à −3 dB avec R₂ = 5R₁ = 1 kΩ, C = 0,01 µF ; 4°) a) G ; b) G_Max,
  actif ou passif ? c) allure de G = f(N) et points remarquables.
- **Ex. 6 (p.213)** — R, C, bobine (L, r) en série, passe bande. 1°) schéma (entrée, sortie) ; 2°) connexions oscilloscope
  (Y₁ : entrée ; Y₂ : tension proportionnelle à i) ; 3°) aspect de l'écran pour N quelconque ; 4°) a) Q ; b) largeur de la
  bande ; R = 500 Ω ; r = 10 Ω ; C = 0,05 µF ; L = 0,1 H.
- **Ex. 7 (p.214, synthèse)** — R = 90 Ω, L = 0,1 H, r = 10 Ω, C = 0,5 µF en série, sortie aux bornes du résistor ;
  u_E sinusoïdale, ω réglable, U_Em fixe. 1°) a) schéma, sens positif ; b) loi des mailles ; 2°) a) Z par Fresnel ;
  b) résonance d'intensité, N₀, valeur ; c) Q₀ (« surtention » [sic]) ; 3°) T à N = 2N₀ ; 4°) a) N₁, N₂, ΔN en fonction de
  Q₀ et N₀ ; valeurs (« Calcuer » [sic]) ; b) Q, comparer à Q₀.
- **Ex. 8 (p.214)** — TP : A.O. idéal, R₀, R₁, R₂, C, GBF, oscilloscope ; montage : R₀ entre E et l'entrée non inverseuse,
  C entre cette entrée et la masse, sortie S, pont R₁ (S–A) / R₂ (A–M), A relié à l'entrée inverseuse (passe bas actif
  non inverseur). 1°) schéma avec voies Y₁ (u_E), Y₂ (u_S) ; 2°) un élève dit qu'il manque un générateur : a-t-il raison ?
  3°) Fig.1 (N = 100 Hz, 2 V/div ; u_S ≈ 2,5 div d'amplitude) et Fig.2 (N = 100 kHz, 0,5 V/div ; u_E) pour U_Em = 1 V :
  a) montrer que le filtre est passe bas ; b) valeur approchée du maximum de T ; c) gain maximal en dB ; 4°) a) T en
  fonction de R₀, R₁, R₂, C, ω ; b) limites de T ; 5°) N_h ; 6°) allure de T = f(N).
- **Ex. 9 (p.215)** — filtre CR, C = 10 pF, R = 1 kΩ ; u_E(t) = 4sin(2πNt) ; Fig.1 (N₁ = 10 kHz), Fig.2 (N₂ = 15923 Hz),
  Fig.3 (N₃ = 20 kHz) : chronogrammes u_E et u_S. 1°) u_E(t) ; 2°) u_S(t) pour N₂ ; 3°) a) tableau U_Sm, T, G pour N₁, N₂,
  N₃ ; b) sens de variation ; c) passe bas, haut ou bande ? d) pourquoi déduire les limites pour N → 0 et non N → ∞.
- **Ex. 10 (p.215–216)** — RLC série (C, L, ampèremètre, R en sortie), GBF de 5 à 85 MHz, u_E(t) = 100√2 sin(2πNt) ;
  R = 50 Ω, L = 1 µH, C = 10 pF. 1°) tableau N (MHz) 5 / 20 / 50.3 / 70 / 85 ; I (A) 0,032 / 0,149 / 2 / 0,458 / 0,285 :
  a) ligne U_S ; b) U_S = f(N) ; c) nature du filtre ; 2.1°) condensateur : a) Z_C(N, C), U_C ; b) tableau Z_C (Ω) 3183 / – /
  316 / – / 187 ; U_C (V) – / 118,6 / – / 104 / – ; c) variation de Z_C ; d) cas limites ; 2.2°) bobine (« Comprtement »
  [sic]) : a) Z_L, U_L ; b) tableau Z_L (Ω) – / 126 / – / 440 / – ; U_L (V) 0,98 / – / 632 / – / 53,3 [?] (à 85 MHz, U_L = Z_L·I ≈ 534 × 0,285 ≈ 152 V ; 53,3 V est la valeur de U_C
  = 187 × 0,285) ; c) variation ;
  d) cas limites ; e) comparer ; 2.3°) circuit : a) Z(R, L, C, N), U_S ; b) tableau Z (Ω) 3152 / 671 / – / 218 / 350 ;
  U_S (V) 1,858 [?] / 7,45 / – / 22,9 / 14,25 (à 5 MHz, U_S = R·I = 50 × 0,032 = 1,6 V, ou U/Z = 1,586 V :
  inversion de chiffres probable) ; c) variations de u_S et principe du passe bande ; 3°) maximum de a) la fonction
  de transfert ; b) du gain ; 4°) bande passante à « -3db » [sic].
- **Ex. 11 — Étude de texte « Filtres et musique Techno » (p.216)** — filtres en techno et trip-hop ; passe-bas (Low Pass),
  passe-bande (Band Pass), passe-haut (Hi Pass), réjecteur de bande « notch » (karaoké) ; « l'atténuation d'un filtre est
  toujours multiple de 6 dB par octave » ; filtres à 12 ou 24 dB ; « Cut Off » à 3 dB. Questions : 1°) réjecteur
  complémentaire du passe bande ; 2°) cut off et leur nombre pour un passe bande ; 3°) filtres les plus performants entre
  12 et 24 dB.

### Réponses du manuel (p.393 col. droite « Chapitre 7 », p.394 col. gauche et haut de col. droite)

« 3. 1°a) u_S(t) = U_Sm sin(ωt + φ) ; b) T = 1/√(1 + (RCω)²) c) G = -10 log (1 + (RCω)²) 2°c) N_b ≈ 1 kHz [sic : N_h] et
ΔN = 1 kHz 2°a) [sic, pour 3°a)] Pour N = 1 kHz, on a : φ = - 45° ; b) U_Sm ≈ 1,4 V ; u_S(t) = 1,4sin(2000 πt – π/4) » ·
« 4. 1°) Z_R indépendant de ω ; Z_c = 1/Cω : • Si ω → 0, Z_c → ∞ Le condensateur se comporte comme un circuit ouvert, le
signal d'entrée est atténué à la sortie. • Si ω →∞, Z_c →0 Le condensateur se comporte comme un circuit fermé, le signal
d'entrée est transmis à la sortie. Le filtre est passant pour les hautes fréquences : c'est un filtre passe haut.
2°) T = 1/√(1 + 1/(RCω)²) T(0) = 0 ; T(∞) = 1 2°) [sic, pour 3°)] N_c = N_b = 1/(2πRC) = 15,9 Hz La bande passante :
[15,9 Hz, ∞ [ » · « 5. 1°) T = (R₂/R₁)/√(1 + (2πR₂CN)²) 2°) • Si N → 0, T → R₂/R₁ U_Sm ≠ 0. Le filtre est passant. • Si
N → ∞, T → 0 U_Sm = 0. Le filtre n'est pas passant. Il s'agit d'un filtre passe bas. 2°) [sic, pour 3°)] N_h = 15,92 Hz
4°) a) G = 20 log[(R₂/R₁)/√(1 + (2πR₂CN)²)] b) G_Max = 13,97 Le filtre est actif. » · « 6. 4°) a) Q = 2,77 ; b) ΔN ≈
813 Hz » · « 7. 2°) a) z = √((r + R)² + (Lω − 1/Cω)²) b) Z=r+R N₀ = 1/(2π√LC) = 712,12Hz ; c- Q₀ = Lω₀/(R+r) = 4,472
2°) [sic, pour 3°)] T (2N₀) = 0,186 4°) a) N₁ = (N₀/2Q)(−1 + √(1 + 4Q²)) N₁ [sic, pour N₂] = (N₀/2Q)(+1 + √(1 + 4Q²))
N₂ − N₁ = N₀/Q N₁ = 1346,5 Hz ; N₂ = 1505,7 Hz ΔN = 159,2 Hz b) Q = N₀/ΔN, Q = 4,472 ; Q = Q₀ » · « 8. 2°) Oui, il manque le
générateur d'alimentation de l'amplificateur opérationnel. 2°) [sic, pour 3°)] a) Pour la fréquence faible 100 Hz,
U_Sm/U_Em ≈ 5, d'où T > 1 Pour la fréquence très élevée 100 kHz, U_Sm/U_Em ≈ 0,25, d'où T < 1 Il s'agit d'un filtre passe
bas b- T_Max ≈ 5 c- G_Max = 13,979 dB ≈ 14 dB. 4°) a) T = ((R₁ + R₂)/R₂) × 1/√(1 + (R₀Cω)²) b) T(0) = 1 + R₁/R₂ ;
T(∞) = 0 » · Pas de réponse pour les ex. 1, 2, 9, 10, 11 (la colonne passe ensuite au « Chapitre 8 »).

### En savoir plus / Documents

- **« Technologies des filtres » (p.217–219, d'après www.techno-science.net)** — quatre types courants : passe-bas,
  passe-haut, passe-bande, réjecteur de bande ; réalisations passive, active ou numérique. *Filtres passifs* : composants
  passifs seulement, « leur transmittance ne peut excéder l'unité » ; circuits RC, RL, LC, RLC ; sélectivité et nombre de
  composants ; pas de saturation (enceintes) ; toutes gammes de fréquences ; condensateur électrochimique inductif en HF ;
  bobine conductrice en BF, s'oppose aux HF ; condensateur inverse ; au-delà de 100 MHz, « stubs » ; facteur de qualité
  (« rapport entre leur fréquence centrale et leur bande passante », valable pour un passe bande) ; bruits (thermique,
  magnétique) ; filtres à quartz, SAW, céramiques, mécaniques. *Filtres actifs* : au moins un composant actif (transistor,
  A.O.…) ; pas de bobines ; gain positif possible ; signaux faibles ; alimentation nécessaire, saturation ; bruit.
  *Filtres numériques* : traitement numérique (CD audio), DSP, reproductibilité, filtre en peigne. *Autres* :
  piézoélectriques (quartz), SAW (onde acoustique de surface ; « Les sorties retardées sont recombinées pour produire une implémentation d'un
  filtre à réponse impulsionnelle finie »), atomiques (masers à césium, maser à rubis) ;
  note MASER (« Microwave Amplification by Stimulated Emission of Radiation »).

### Écart avec la référence (aucune)

- **Correspondance** : confirmée « aucune » dans physique-bac-sciences-exp ; aucun chapitre de `content/` sur les filtres
  (cf. §2.6). Chapitre **à créer**. Il s'appuie sur : sciences-exp/01 et /02 pour les dipôles RC (équation différentielle
  du premier ordre, mais ici en régime sinusoïdal permanent), sciences-exp/04 et le chapitre 5 de ce manuel pour Fresnel,
  Z, la résonance d'intensité et Q (le passe-bande RLC réutilise exactement le montage du chapitre 5), le chapitre 4 de ce
  manuel pour l'A.O. idéal (ε = 0, i⁺ = i⁻ = 0).
- ✅ **À créer (contenu propre)** : filtre passe-bas passif RC (sortie aux bornes de C) : mesures, courbes semi-log, N_h,
  influence de R et C, N_h = 1/(2πRC), équation u_S + RC du_S/dt = u_E, T par Fresnel, T = Z_C/Z, G = −10 log[1 + (2πRCN)²],
  bande [0, N_h], tgΔφ = −N/N_h, −π/2 < Δφ < 0, Δφ = −π/4 à N_h, asymptote −20 dB/décade (= −6 dB/octave), décade/octave ;
  filtre passe-bas actif inverseur (R₀ en entrée, R₁ ∥ C₁ en rétroaction) : T = (R₁/R₀)/√(1 + (2πR₁C₁N)²), T₀ = R₁/R₀,
  G₀ = 20 log(R₁/R₀), N_h = 1/(2πR₁C₁) indépendante de R₀, amplification possible, Δφ de 180° à 90° (135° à N_h) ;
  filtre passe-haut passif CR (sortie aux bornes de R) : R₁C₁ du_S/dt + u_S = R₁C₁ du_E/dt, T = 1/√(1 + 1/(2πR₁C₁N)²),
  N_b = 1/(2πRC), bande [N_b, ∞[, tgΔφ = N_b/N, Δφ = + π/4 à N_b, N_b(CR) = N_h(RC) mêmes composants ; filtre passe-bande
  RLC série (sortie aux bornes de R₀) : équation du second ordre, T = T₀/√(1 + Q²(x − 1/x)²), T₀ = R₀/R, x = N/N₀ « fréquence
  réduite », Q = Lω₀/R = 1/(RCω₀) « facteur de qualité » (même expression que le facteur de surtension), N_b et N_h
  (formules en √(1 + 4Q²)), ΔN = N₀/Q, sélectivité (Q >> 1), N₀ fréquence centrale ((N_b + N_h)/2 ≈ N₀ si Q >> 1),
  −π/2 < Δφ < π/2, ± 45° aux coupures ; ordre d'un filtre (1 ou 2) ; filtre passif ⇒ T ≤ 1, G ≤ 0 ; applications (ADSL,
  hi-fi, tables de mixage, radio, antiparasitage).
- **Vocabulaire / notations propres** : « quadripôle RC / CR / RLC », « filtre passif / actif », « fréquence réduite x »,
  « facteur de qualité Q », « fréquence centrale », « décade », « octave », « filtre du premier / second ordre », T₀, G₀, N_b,
  N_h, U_Smo, Δφ = φ_S − φ_E, angles tantôt en rad, tantôt en degrés.

### Bornes de scope

- ✅ **INCLUS** : les quatre filtres étudiés (passe-bas RC passif, passe-bas actif inverseur, passe-haut CR passif,
  passe-bande RLC série) : montages, lecture d'oscillogrammes, tableaux de mesures, tracés semi-log et linéaires,
  détermination graphique de N_b, N_h, ΔN, G₀ ; équations différentielles en régime sinusoïdal (premier ordre pour RC/CR et
  passe-bas actif, second ordre pour RLC), solution permanente admise ; transmittance par Fresnel ; expressions de T, G,
  N_h, N_b, ΔN, Q, T₀, G₀ ; déphasage (tgΔφ, intervalles, ± 45°, 135°) ; influence de R, C, R₀, R₁ ; pente ± 20 dB/décade
  (± 6 dB/octave) ; ordre ; passif/actif ; en exercices : calcul de R' à partir de N_b, approximation N_b ≈ N₀ − ΔN/2 pour
  Q >> 1, passe-bas actif non inverseur (T₀ = 1 + R₁/R₂, ex. 8), comportements limites de Z_C et Z_L, lecture de
  chronogrammes.
- ⛔ **EXCLU** : nombres complexes et fonction de transfert complexe ; diagrammes de Bode de phase ; filtres d'ordre
  supérieur à 2, réjecteur de bande (« notch », seulement cité en texte), filtres RL, LC ; filtres passe-haut ou
  passe-bande actifs (non étudiés en cours) ; filtres numériques, à quartz, SAW, atomiques (lecture) ; décomposition en
  harmoniques ; régime transitoire.

### Lecture

- **Pages lues en L1** : 174 à 219 (les 46 pages), 220 (borne), 393–394 (réponses).
- **Pages lues sur l'image** (110 dpi) : 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
  191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
  216, 217, 393, 394 (44 pages) ; p.174, 201, 218 et 219 vues sur l'image par la relecture R-7 (auditeur C), conformes
  (p.201 : formules reconstituées depuis L1 exactes). Le chapitre est désormais entièrement vu sur l'image.
- **Écarts texte/image** : figures et courbes (Fig.2–4, 6, 8, 13, 14, 16, 18, 20, 25–28, 33–34, 37) absentes du texte ;
  p.180–182, 189–191, 195–197, 201–205 : vecteurs de Fresnel rendus « LLLLI », ω, φ, π, √ perdus, fractions et crochets
  éclatés (« (           )² », « '!  #( ») ; p.191 « 10^0,3 − 1 ≈ 1 » rendu « 100,3  1 c 1 » ; p.203–204 inéquations
  illisibles (≤/≥ perdus) ; p.207–208 L'essentiel quasi illisible en L1 (encadrés éclatés, « 90ϒ ») ; p.210–211 solution
  de l'exercice résolu déstructurée ; p.212 courbes du QCM absentes ; p.215 chronogrammes de l'ex. 9 absents ; p.393–394
  formules en désordre.
- **Coquilles [sic]** : p.174 « surtention » ; p.175 « indissocibles » ; p.177 « qu'a la fréquence » ; p.180 « interrupteur
  k », « Shéma » (Fig.9), « permanant » ; p.181 « métthode » ; p.182 « passe bass » ; p.183 « Fig:12 », « sensibiltés » ;
  p.185 « correspodant », « jusqu'a », « règlable » ; p.189 « figure 11 » (lire figure 12) ; p.191 « pase bas », « fitre » ;
  p.192 « Shéma » (Fig.24), « sucsessivement » ; p.194 « à la fréquence de coupure haute » + « Δφ = + π/2 » (lire coupure
  basse, + π/4), « Δφ augmente » quand N augmente (il diminue), « chute de gain de (−20 dB) par décade » aux basses
  fréquences (pente + 20 dB/décade) ; p.197 « log(…) ≥ − 0,3 » (lire ≤ 0,3), « ‖A₁A₂‖ », « N_b = 1/(2πR₁C₁N) » ; p.198
  « codensateur », « résitor », « sucsessivement » ; p.199 « a ce filtre », deux questions « 4°) », « concordence » ;
  p.203 et p.207 puces « ∞ » et degrés « ϒ » parasites ; p.206 « domines » ; p.207 « N_h = 1/(2πR₁CN) », « N_b = 1/(2πRCN) »
  (N en trop), « G = G₀ − 10 log(1+(2πRCN)²) » (R pour R₁) ; p.209 « apllique », « lévolution » ; p.210 phases des
  vecteurs de Fresnel (φ_S + π/2 et φ_S + π au lieu de φ_S et φ_S + π/2) ; p.211 « A.N. : N_b = 995 Hz » (lire N_h),
  « N_b = N_h − ΔN » ; p.213 « opérationel », « naturee », « shéma », « shématisé » ; p.214 « compsants », « surtention »,
  « Calcuer » ; p.215 « lorque » ; p.216 « Comprtement », « tensin », « -3db », « fltre » ; p.219 « expresion » ; p.393–394
  numérotations des questions décalées (ex. 3, 4, 5, 7, 8), « N₁ » pour N₂ (ex. 7).
- **Doutes [?]** :
  - [?] 1 — **Ex. 4, réponse « N_c = 15,9 Hz »** : R = 1 kΩ, C = 10 nF donnent 1/(2πRC) ≈ 15,9 **kHz** ; idem **ex. 5
    « N_h = 15,92 Hz »** avec R₂ = 1 kΩ, C = 0,01 µF → 15,9 kHz. Unités fausses dans les réponses.
  - [?] 2 — **Ex. 7, réponses « N₁ = 1346,5 Hz ; N₂ = 1505,7 Hz »** : avec N₀ = 712 Hz et Q = 4,472, les formules donnent
    N₁ ≈ 637 Hz et N₂ ≈ 796 Hz (ΔN = 159,2 Hz cohérent) ; « T(2N₀) = 0,186 » : recalcul ≈ 0,133 — à ne pas reprendre sans
    recalcul. Réponse 7 p.394 : « z = √((r + R)² + (Lω − 1/C_o)²) » [sic, ω manquant] ; « c- = Q₀ ».
  - [?] 3 — **Ex. 9** : C = 10 pF et R = 1 kΩ donnent N_b ≈ 15,9 MHz, alors que les fréquences des figures (10 kHz,
    15 923 Hz, 20 kHz) supposent N_b = 15 923 Hz, soit C = 10 nF : valeur de C probablement fausse (pas de réponse
    imprimée).
  - [?] 4 — **Ex. 10** : U_S = 1,858 V à 5 MHz (attendu ≈ 1,6 V) et U_L = 53,3 V à 85 MHz (attendu ≈ 152 V ; 53,3 V = U_C)
    dans les tableaux de l'énoncé ; les autres cases se recalculent juste.
  - [?] 5 — **Ex. 3** : « U_E = 2 V » (efficace) contre U_Em = 2 V supposé par la réponse.
  - [?] 6 — **Fig.34 (p.200)** : sur le même graphe, la courbe G = h(N) paraît nettement plus étroite que la courbe
    U_Sm = f(N) (échelles verticales différentes, mêmes abscisses 410–580 Hz) : la lecture de la bande passante sur la
    courbe U_Sm (niveau 1,13 V) ne redonne pas visiblement [495 Hz, 545 Hz] — figure à ne pas réutiliser telle quelle.
  - [?] 7 — **Ex. 8, Fig.2** : légende « u_E » sur un oscillogramme censé montrer u_S (à 100 kHz, 0,5 V/div). Fig.1 : à
    100 Hz, u_S ≈ 2,5 div × 2 V/div ≈ 5 V pour U_Em = 1 V → T ≈ 5, conforme à la réponse.
  - [?] 8 — **Bande passante RLC (p.204)** : « log[…] ≤ 3/10 » utilise l'approximation log 2 ≈ 0,3, non signalée (comme
    « 0,998 ≈ 1 » pour RC).
- **Contrôles (cohérents)** :
  - §1.2.1 : G₀ ≈ 6 dB lu (R₁/R₀ = 2 → 6,02 dB) ; N_h « sensiblement égale à 1050 Hz » contre 1064 Hz théorique.
  - §2.1 : N_b ≈ 1050 Hz pour le CR contre 1070 Hz pour le RC avec les mêmes composants (égalité « aux erreurs
    expérimentales près », p.194).
  - §3.1 : bande [495 Hz, 545 Hz], ΔN = 50 Hz ; théorie avec R = 62,5 Ω : Q ≈ 10,4, ΔN ≈ 50 Hz ; Fig.34 : U_Sm max 1,6 V
    (= 50 × 32 mA) et G₀ = −1,94 dB (= 20 log 0,8).
  - Fig.37 : pics T ≈ 0,8 / 0,88 / 0,97, cohérents avec T₀ = R₀/(R₀ + r) (0,8 ; 0,89 ; 0,976).

## 2.8 Chapitre 8 — Production de signaux non sinusoïdaux (manuel 223471, p.220–247)

Partie du manuel : « Evolution de systèmes électriques » (bandeau de chaque page) ; bandeau de chapitre
« Production de signaux périodiques non sinusoïdaux » (titre de la page d'ouverture : « PRODUCTION DE SIGNAUX
NON SINUSOÏDAUX », n° 8). **Plage exacte : p.220 (objectifs/prérequis) – p.247** (la plage provisoire 221–248 est
décalée d'une page : p.248 est la page d'objectifs du chapitre 9). Le chapitre ne contient **pas de fiche
technique**. Notation : **« Log » = logarithme népérien** (p.228, p.232 : « T = RC log3 = 1,098. RC ») ;
indices écrits u_E/u_e, u_S/u_s, U_sat/Usat indifféremment ; seuils notés **U_BH** (basculement bas→haut, atteint
par u_E décroissante) et **U_HB** (haut→bas, atteint par u_E croissante) ; états haut/bas **E_H / E_B** ; tension
d'alimentation des portes CMOS **U_DD** (exercices : V_cc, V_T+, V_T− dans « En savoir plus »).

**Objectifs (p.220, VERBATIM)** — « Reconnaître un multivibrateur astable. » · « Réaliser un montage de
multivibrateur astable. » · « Visualiser les chronogrammes d'un multivibrateur astable. » · « Tracer les
chronogrammes d'un multivibrateur astable. » · « Interpréter les chronogrammes d'un multivibrateur astable. » ·
« Relever les deux niveaux de sortie d'un multivibrateur astable. » · « Calculer la période du signal généré par un
multivibrateur astable. » · « Calculer le rapport cyclique δ d'un multivibrateur astable. »

**Prérequis (p.220)** — SAVOIR : définir un oscillateur ; citer les propriétés caractéristiques d'un amplificateur
opérationnel idéal ; citer des exemples de portes logiques ; décrire le principe de fonctionnement d'une porte
logique NAND ; citer un montage comparateur à un seuil de basculement ; décrire la réponse d'un dipôle RC à un
échelon de tension ; écrire l'équation différentielle régissant la réponse d'un dipôle RC à un échelon de tension.
SAVOIR FAIRE : utiliser un oscilloscope bicourbe ; déterminer la période d'un signal périodique ; reconnaître un
signal sinusoïdal ; reconnaître la caractéristique de transfert d'un amplificateur opérationel [sic] ; établir
l'expression de la tension de sortie en fonction de la tension d'entrée de quelques montages à amplificateur
opérationnel ; expliquer le fonctionnement des portes logiques NO [sic, = NON] et NAND et tracer leurs
chronogrammes.

**Page d'ouverture (p.221)** — photos « Système d'alarme », « Chenillard modulateur », « Signaux en créneaux » ;
légende : « Les multivibrateurs astables qui produisent des signaux en créneaux sont à la base des systèmes
d'alarme, des chenillards modulateurs... ». Questions d'accroche (VERBATIM) : « Actuellement, les ordinateurs les
plus perfermants [sic] sont caractérisés par une vitesse d'horloge allant de 1 GHz à 2x3,2 GHz. Que signifie cette
caractéristique technique ? Qu'est-ce que ça peut être, l'horloge du processeur d'un ordinateur ? » · « Qu'est-ce
qu'un oscillateur de relaxation et qu'est-ce qui le distingue d'un oscillateur harmonique ? » · « Qu'est-ce qui
confère aux générateurs BF cette possibilité de délivrer à leurs bornes un signal carré ou triangulaire ? »

**Plan (titres numérotés du manuel)** — introduction (p.222 : signaux rectangulaires ou triangulaires « les plus
pratiques d'utilisation ») · **1 Générateurs de signaux périodiques non sinusoïdaux** (p.222 : multivibrateur ;
bistable, monostable, astable ; oscillateur de relaxation) · **2 Fonctionnement astable d'un multivibrateur**
(p.223) : 2.1 Montages de base : comparateurs à deux seuils (p.223–226) ; 2.2 Montage multivibrateur astable et
grandeurs caractéristiques (p.226) ; 2.3 Principe de fonctionnement d'un multivibrateur astable bouclé en RC
(p.226–228 : expression de u_C(t), expression de la période T) · **3 Exemples de multivibrateurs astables**
(p.229) : 3.1 à amplificateur opérationnel (p.229–230) ; 3.2 à porte CMOS inverseuse à hystérésis (p.231–232) ;
3.3 à portes CMOS inverseuses (p.232–235) · L'essentiel (p.236) · Exercices : exercice résolu (p.237–239) ; Tests
rapides des acquis (ex. 1–2, p.240) ; Exercices d'application (ex. 3–6, p.241–242) ; Exercices de synthèse
(ex. 7–11, p.242–244) · En savoir plus « Bascules de Schmitt » (p.245–247).

### Cours — Activités

- **§1 Texte (p.222)** — pas de manipulation : définitions du multivibrateur et des trois catégories (voir Encadrés).
- **§2.1 Manipulation, 1ʳᵉ expérience (p.223–225)** — montage (M1), Fig.1 : AO (LM301 ou μA 741), R1 = R2 = 10 kΩ,
  GBF triangulaire ≈ 20 V crête à crête, N = 1 kHz ; u_E sur l'entrée inverseuse (point A → Y1), R2 de la sortie
  S vers l'entrée +, R1 de l'entrée + à la masse ; S → Y2. On augmente l'amplitude « jusqu'à ce que
  l'amplificateur opérationnel puisse basculer ». Fig.2 : u_E(t) triangulaire et u_S(t) en créneaux, 0,2 ms/div,
  5 V/div ; Fig.3 : mode XY, caractéristique u_S = f(u_E) en cycle rectangulaire (hystérésis). Questions (VERBATIM,
  p.224) : « 1°) En exploitant les chronogrammes de la figure 2 : a) montrer que le montage (M1) est un comparateur
  à deux seuils de basculement dont on donnera les valeurs. b) donner les valeurs prises par la tension de sortie
  et les comparer aux tensions de saturation Usat et - Usat de l'amplificateur opérationnel. 2°) a) Par application
  de la loi des mailles aux schémas du montage (M1), établir l'équation : ε = R1/(R1+R2) u_S − u_E. b) En supposant
  que l'amplificateur opérationnel est idéal, montrer que lorsque ε change de signe uS passe de : (- Usat) à
  (+ Usat) à l'instant où uE franchit, en décroissant , un seuil de basculement U_BH que l'on calculera. (+ Usat) à
  (- Usat) à l'instant où u_E franchit, en croissant, un deuxième seuil de basculement U_HB que l'on calculera.
  3°) Comparer les valeurs trouvées théoriquement à celles obtenues expérimentalement. Expliquer les écarts relatifs
  constatés. 4°) Montrer que le montage (M2) est aussi un comparateur à deux seuils dont on précisera les
  caractéristiques. » Interprétation (Fig.6, mailles MAE⁻E⁺R1M et MSR2R1M) : u_E + ε − R1 i = 0 (1) ;
  u_S − R2 i − R1 i = 0 (2) ; ε = R1 i − u_E (3) ; i = u_S/(R1 + R2) (4) → formule encadrée (voir Encadrés).
  Valeurs mesurées : U_sat ≈ 14,5 V au lieu de 15 V et ≈ −14 V au lieu de −15 V (zone linéaire non verticale, largeur
  Δu « de l'ordre du mV », Fig.7) ; seuils ≈ 7 V au lieu de 7,5 V et ≈ −7,25 V au lieu de −7,5 V (« tension de
  décalage (ou offset) »).
- **§2.1 Manipulation, 2ᵉ expérience (p.223, p.225)** — montage (M2), Fig.4 : porte logique CMOS **4093** montée en
  inverseur (entrées réunies, R en série à l'entrée A, GBF, sortie S) ; tension triangulaire « préalablement
  calibrée » (note marginale : « Pour calibrer la tension triangulaire, il suffit de jouer sur le décalage de zéro
  en observant le signal à l'oscilloscope. ») ; Y1, Y2 en mode DC, mode XY → caractéristique (C1), Fig.5a (cycle
  d'hystérésis). Porte remplacée par une **CMOS 4011** → caractéristique (C2), Fig.5b (basculement unique, sans
  cycle). Résultats : voir Encadrés (seuils U_BH, U_HB des portes 4093 et 4011).
- **§2.2 Texte (p.226)** — Fig.8 : schéma de principe « COMP » dont l'entrée inverseuse (A) est rebouclée par R
  depuis la sortie S, C entre A et la masse ; Fig.9 : u_S(t) rectangulaire entre E_H et E_B, durées T1 et T2.
- **§2.3 Étude (p.226–228)** — régime permanent, condensateur initialement chargé sous U_i, u_S passant du niveau
  bas au haut ; Fig.10 : u_C(t) exponentielles entre U_BH et U_HB visant E_H puis E_B, u_S(t) créneaux ; Fig.11 :
  maille MSRACM ; Fig.12a/12b : détermination de T1 (charge, points U_iC → P) et de T2 (décharge, P → Q).
  Formules : voir Encadrés.
- **§3.1 Manipulation (p.229–230)** — Fig.13 : comparateur (M1) dont l'entrée inverseuse est rebouclée par R
  (S → A) et C (A → masse) ; **R = 10 kΩ, C = 100 nF** ; A → Y1 (u_C), S → Y2 (u_S) ; Fig.14 : chronogrammes
  u_C(t) (entre U_BH et U_HB) et u_S(t) (entre E_B et E_H) ; « la période change si on modifie la valeur de R ou de
  C ». Questions (VERBATIM) : « 1°) En exploitant les chronogrammes de la figure 14 : a) expliquer qualitativement le
  principe de fonctionnement du montage. En déduire qu'il s'agit bien d'un multivibrateur astable, b) déterminer
  graphiquement les valeurs de la période T et du rapport cyclique δ de la tension de sortie sachant que la
  sensibilité horizontale utilisée est de 0,2ms par division. 2°) Pour un tel multivibrateur astable : a) montrer
  que la période T est donnée par la relation : T = 2τLog(1 + 2 R1/R2) (5) ; b) dans le cas ou R1 = R2, montrer que
  T1 = T2 =1,1.τ. En déduire l'expression de T en fonction de τ. Retrouver la même expression à partir de la formule
  générale (5). c) calculer la période T ainsi que le rapport cyclique δ et comparer les valeurs trouvées à celles
  de la réponse à la question 1°b. » (Les valeurs graphiques de T et δ ne sont pas données par le manuel.) Étude
  théorique (p.229–230, Fig.15) : voir Encadrés.
- **§3.2 Manipulation (p.231–232)** — Fig.16 : porte CMOS 4093 (symbole à hystérésis) dont l'entrée commune est
  rebouclée par R (réglable, flèche) depuis S, C entre A et la masse ; **R = 10 kΩ, C = 100 nF** ; Fig.17 :
  chronogrammes u_C(t) (entre U_BH et U_HB, sous U_DD) et u_S(t). Questions (VERBATIM) : « 1°) Qu'est-ce qui
  différencie les chronogrammes de la figure 15 [sic : lire 17] de ceux d'un multivibrateur à amplificateur
  opérationnel ? 2°) En exploitant les chronogrammes et en s'appuyant sur une analogie avec les chronogrammes
  précédemment trouvés, expliquer qualitativement le principe de fonctionnement du montage. En déduire qu'il s'agit
  aussi d'un oscillateur fonctionnant en relaxation et déterminer la période T ainsi que le rapport cyclique δ qui le
  caractérise. 3°) Montrer théoriquement que l'expression de la période T de la tension délivrée par un tel
  générateur est donnée par la relation : T = RC.Log((U_DD − U_HB)/(U_DD − U_BH) . U_BH/U_HB) [sic : fractions
  inversées par rapport au résultat du cours, voir doutes], où U_DD = E_H. La calculer. » Étude : voir Encadrés.
- **§3.3 Manipulation (p.232–235)** — Fig.19 : deux portes **NAND 4011** montées en inverseurs (1) et (2), C entre
  S1 et A2 via R1, R entre le nœud (C, R1) et S2 relié à l'entrée A1 ; **C = 10 nF, U_DD = 12 V, R = 22 kΩ,
  R1 = 470 kΩ** (« valeur très grande pour éviter la modification de la tension u à l'entrée de la porte (2) ») ;
  Fig.20 : chronogrammes u_S1 (créneaux 0/U_D [sic, U_DD]), u_S2 (créneaux complémentaires 0/U_DD), u_E2 (pics à
  3U_DD/2 et −U_DD/2, basculement à U_DD/2) et u_C (entre −U_DD/2 et +U_DD/2). Questions (VERBATIM, p.233) :
  « 1°) Montrer que l'équation différentielle régissant l'évolution, au cours du temps, de la tension uC aux bornes
  du condensateur est analogue à celle qui a été obtenue pour le multivibrateur à amplificateur opérationnel. En
  déduire que ce montage est aussi un exemple de multivibrateur astable. 2°) Décrire le principe de fonction0nement
  [sic] de ce multivibrateur. En déduire que sa période T est donnée par la relation : T = RC.Log((U2 − 2U1)/(U2 − U1)
  . (U1 + U2)/U2) 3°) Sachant que U1= U_DD et u2 = ½ u_DD calculer T et δ. » Étude : voir Encadrés.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Multivibrateur (§1, p.222)** — « Les montages produisant des signaux périodiques non sinusoïdaux sont des
> multivibrateurs. Un multivibrateur est un circuit constitué essentiellement d'un comparateur, d'un réservoir
> d'énergie (dipôle RC par exemple) et d'une source autonome d'énergie (tension(s) continue(s) d'alimentation). Il y
> a trois catégories de multivibrateurs : ■ le multivibrateur bistable : circuit possédant deux états ou niveaux de
> sortie stables, un état initial qu'il atteint en le soumettant à un signal externe et un autre état qu'il peut
> maintenir tant qu'on ne lui applique pas un deuxième signal de déclenchement (ou de bascule), ■ le multivibrateur
> monostable : circuit possédant un seul état stable. En le soumettant à un signal externe dit de commande, il passe
> à un état quasi-stable qu'il maintient pendant une certaine durée puis revient à son état stable initial et ainsi
> de suite, ■ le multivibrateur astable : circuit oscillant entre deux états quasi-stables sans avoir besoin
> d'aucun signal externe de déclenchement. » Remarque : « En raison du retour périodique du multivibrateur à un état
> stable (niveau d'énergie minime), tout oscillateur dont il est la base est appelé oscillateur de relaxation. »

> **Comparateur à deux seuils à AO (§2.1, p.224, encadré)** — **ε = R1/(R1 + R2) · u_S − u_E** ; « Où u_S = + U_sat
> si ε > 0 et u_S = - U_sat si ε < 0. »

> **Seuils de basculement (p.225)** — « si ε passe d'une valeur négative à une valeur positive, u_S passe de
> - U_sat = - 15 V à U_sat = 15 V à l'instant où u_E franchit la tension de basculement
> **U_BH = − R1/(R1 + R2) · U_sat** en décroissant ; - si ε passe d'une valeur positive à une valeur négative, u_S
> passe de U_sat = 15 V à - Usat = -15 V à l'instant où u_E franchit la tension de basculement
> **U_HB = + R1/(R1 + R2) · U_sat** en croissant. On dit que le système bascule autour de ε = 0 et les tensions de
> basculement sont définies lorsque ε = 0 et u_s = ± U_sat. » […] « Ainsi, le montage formé par l'amplificateur et
> les deux résistances R1 et R2 permet de comparer la tension d'entrée u_E aux deux tensions de références U_BH et
> U_HB et à chaque fois que u_E franchit l'une de ces tensions seuils, la tension de sortie u_S bascule de la valeur
> (+ U_sat) à (- U_sat) ou inversement : c'est un montage comparateur à deux seuils. »

> **Portes CMOS (p.225)** — « le montage (M2), formé par la porte CMOS inverseuse (4093 ou 4011) est aussi un
> comparateur de tension à deux seuils : ◆ **U_BH = ½ U_DD et U_HB = U_DD** pour la porte CMOS inverseuse de type
> 4093 (ou à hystérésis). ◆ **U_BH = 0 et U_HB = ½ U_DD** pour la porte CMOS 4011. » [image vérifiée ; valeurs
> discutables, voir doutes]

> **Conclusion (§2.1, p.226)** — « Un comparateur de tensions est un circuit qui délivre un signal électrique défini
> en sortie selon le signe et les valeurs des seuils de basculement. Un comparateur utilisant un amplificateur
> opérationnel ou une porte CMOS monté en inverseur est un montage à deux seuils qui délivre une tension à deux
> niveaux de sortie : c'est une tension périodique non sinusoïdale. »

> **Multivibrateur astable, grandeurs caractéristiques (§2.2, p.226)** — « De tels multivibrateurs astables sont des
> comparateurs dont l'entrée inverseuse est rebouclée par un dipôle RC (Fig 8). La tension de sortie u_S est une
> tension périodique qui ne peut prendre que deux niveaux, l'un représente l'état haut E_H de l'oscillateur et
> l'autre représente l'état bas E_B du même oscillateur : ce sont les niveaux de sortie du multivibrateur (Fig.9). En
> plus des niveaux de sortie, un multivibrateur est caractérisé par une période T et un rapport cyclique δ.
> ◆ La période T est la durée d'un cycle ; c'est la durée T2 de l'état bas ajoutée à la durée T1 de l'état haut.
> **T = T1 + T2** ◆ Le rapport cyclique δ d'un multivibrateur est le rapport entre la durée T1 de son état haut et la
> durée totale T d'un cycle (ou période). **δ = T1/T** , il s'exprime en un pourcentage. » Remarque : « Aucun des deux
> états haut et bas n'est stable. Mais, du fait qu'ils sont plus au moins durables, ils sont dits quasistables. »

> **Principe (§2.3, p.226–227)** — « A part la polarisation, il n'y a pas de tension externe appliquée à l'entrée du
> montage : c'est un générateur autonome qui maintient à sa sortie une tension périodique non sinusoïdale. » […]
> « la tension u_C à ses bornes croît exponentiellement au cours du temps en visant la valeur de la tension du niveau
> haut E_H en même temps que le courant de charge i_C qui décroît en tendant à s'annuler. Mais, lorsque u_c atteint
> le seuil de basculement U_HB, le comparateur commute et u_S passe instantanément de son niveau haut à son niveau
> bas E_B et le courant change de sens. Donc, le condensateur commence à se décharger pour se charger de nouveau
> (avec inversion des signes des charges des armatures) toujours à travers le résistor. Par conséquent, u_C décroît
> exponentiellement au cours du temps vers E_B. Mais, une fois sa valeur atteint le seuil de basculement U_BH, le
> comparateur commute de nouveau, u_S bascule vers son niveau haut et le processus se répète continuellement tel quel
> (Fig.10). »

> **Expression de u_C(t) (p.227)** — « Pour la maille MSRACM (Fig.11) : u_S − R i − u_C = 0. Or, i = dq/dt =
> C du_C/dt. Donc , on obtient : **RC du_C/dt + u_C = u_S (1)** où u_S prend la valeur E_H (niveau haut) ou bien E_B
> (niveau bas). Ainsi, l'équation différentielle à laquelle obéït le dipôle RC environnant le comparateur est la même
> que celle d'un dipôle RC soumis à un échelon de tension. Or, on a vu au chapitre 1 que la solution générale de
> l'équation différentielle (1) peut s'écrire sous la forme u_C(t) = α.e^(−t/τ) + β, où les constantes α et β sont
> deux constantes déterminées à partir des conditions initiales et asymptotiques : Supposons qu'à t = 0, le
> condensateur est initialement chargé à la tension initiale U_i. Il en découle : α + β = U_i. Encore, lorsque t
> tend vers l'infini, la tension u_C(t) tend vers une tension de valeur finale U_f égale soit à E_H ou à E_B. Par
> conséquent : β = U_f. Finalement, […] : **u_C(t) = (U_i − U_f).e^(−t/τ) + U_f = (U_i − U_f).e^(−t/RC) + U_f (2)** »

> **Expression de la période T (p.228)** — « La durée Δt nécessaire à u_C(t) pour passer de sa valeur initiale U_i à
> une valeur donnée U_0 s'écrit : **Δt = τ Log((U_i − U_f)/(U_o − U_f)) (3)** » ; phase de charge (Fig.12a) :
> **T1 = t_P = τ Log((U_iC − E_H)/(U_HB − E_H))** ; phase de décharge PQ (Fig.12b), U_iD = U_P = U_HB :
> **T2 = t_Q − t_P = τ Log((U_iD − E_B)/(U_BH − E_B)) = τ Log((U_HB − E_B)/(U_BH − E_B))** ; « Donc, l'expression de la
> période T d'un multivibrateur astable est de la forme : **T = T1 + T2 = τ Log((U_iC − U_HB)/(U_HB − E_H) .
> (U_iD − E_B)/(U_BH − E_B)) (4)** » [sic, image zoomée 250 dpi : numérateur imprimé « U_iC − U_HB », lire
> U_iC − E_H d'après T1].

> **Conclusion (§2.3, p.228)** — « Le fonctionnement d'un multivibrateur astable est basé sur la commande de son
> entrée par sa sortie en l'absence de tout générateur d'alimentation (à part celui de la polarisation du
> comparateur) : c'est un auto-oscillateur qui évolue grâce à un réservoir d'énergie comme le dipôle RC dont
> l'évolution fixe la valeur de la période T. Bien qu'un tel oscillateur soit qualifié de multivibrateur astable,
> les deux états haut et bas entre lesquels il évolue sont quasi-stables. »

> **Astable à AO (§3.1, p.229–230)** — principe : condensateur initialement déchargé ; « En supposant que u_S passe
> de son niveau haut à son niveau bas [sic : u_C croît, donc u_S est au niveau haut], u_c croît exponentiellement au
> cours du temps vers la tension U_sat. Mais, lorsque u_C atteint le seuil de basculement U_HB = ½ U_sat, le
> comparateur commute et u_s passe de son niveau haut (+ U_sat) à son niveau bas (- U_sat) […] u_C décroît
> exponentiellement au cours du temps vers (- U_sat). Mais, une fois sa valeur atteint le seuil de basculement
> U_BH= -½ U_sat, le comparateur commute de nouveau […] » (les valeurs ± ½ U_sat supposent R1 = R2, non dit).
> Charge [AP] : U_iC = U_BH = − R1/(R1+R2) U_sat ; E_H = U_sat ; U_P = U_HB = + R1/(R1+R2) U_sat ;
> **T1 = τ Log((U_iC − E_H)/(U_HB − E_H)) = τ Log((−R1/(R1+R2) U_sat − U_sat)/(R1/(R1+R2) U_sat − U_sat)) =
> τ.Log(1 + 2R1/R2)**. Décharge [PQ] : U_iD = U_P = U_HB = + R1/(R1+R2) U_sat ; E_B = − U_sat ;
> U_Q = U_BH = − R1/(R1+R2) U_sat ; **T2 = t_Q − t_P = τ Log((U_iD − E_B)/(U_BH − E_B)) = τ Log(1 + 2R1/R2)**.
> « On obtient : » **T = T1 + T2 = 2T1 = 2RC Log(1 + 2R1/R2)** et **δ = T1/T = 0,5** (encadrés) ; « En particulier,
> pour R1 = R2, on a T = 2,2τ. » Conclusion : « Un multivibrateur sans générateur de commande, à amplificateur
> opérationnel et à dipôle RC, est un astable dont la tension de sortie est une tension en créneaux de période
> réglable par modification de R et de C. »

> **Astable à porte CMOS à hystérésis (§3.2, p.231–232)** — principe : « Le fonctionnement d'un tel montage est
> semblable à celui du multivibrateur à amplificateur opérationnel. En effet, le condensateur est initialement
> déchargé : u_C = 0 et u_s = E_H = U_DD. Le condensateur commence à se charger à travers la résistance R et par
> conséquent, u_C croît exponentiellement vers U_DD. Mais, une fois le seuil de basculement U_HB est atteint, le
> condensateur commence à se décharger et u_C décroît vers zéro. Mais, une fois la tension d'entrée de l'inverseur
> CMOS (tension u_C) atteint le deuxième seuil de basculement U_BH, le condensateur commence à se charger de nouveau
> et ainsi de suite. » Charge [OP] : U_iC = U_O = U_BH ; E_H = U_DD ; U_P = U_HB →
> **T1 = τ Log((U_iC − E_H)/(U_HB − E_H)) = τ Log((U_BH − U_DD)/(U_HB − U_DD))**. Décharge [PQ] : U_iD = U_P = U_HB ;
> E_B = 0 ; U_Q = U_BH → **T2 = t_Q − t_P = τ Log((U_HB − 0)/(U_BH − 0)) = RC Log(U_HB/U_BH)**. « On obtient : »
> **T = T1 + T2 = RC Log((U_BH − U_DD)/(U_HB − U_DD) . U_HB/U_BH)** ; « Pour U_BH = ½ U_DD et U_HB = ¾ U_DD , on
> trouve : T= RC log3 =1,098. RC et δ = 0,63. » [vérifié : T1 = RC Log2, T2 = RC Log(3/2), δ = Log2/Log3 ≈ 0,63 ;
> noter que ces seuils ½ et ¾ U_DD ne sont pas ceux de l'encadré p.225 (½ U_DD et U_DD)]. Conclusion : « Comme un
> multivibrateur à amplificateur opérationnel, le multivibrateur à porte CMOS inverseuse à hystérésis est un astable
> dont la tension de sortie est en créneaux et la période est une fonction de la constante de temps du dipôle RC. »

> **Astable à deux portes CMOS inverseuses (§3.3, p.234–235)** — principe : « Les tensions u_E1 et u_S2 étant égales
> (les points A1 et S2 sont portés au même potentiel), si u_S1 prend la valeur U_DD, u_S2 s'annule et inversement. En
> revanche, la tension d'entrée u_E2 à la porte (2) est évolutive grâce à la présence du condensateur. » […]
> « Lorsque la tension u_E2 atteint en décroissant la valeur ½ U_D [sic, U_DD], la porte (2) bascule et u_S2 passe de
> la valeur U_DD à zéro. Cette chute de la tension U_s2 se répercute à la tension u_E2 dont la valeur passe de ½ U_DD à
> (½ U_DD − U_DD). Par conséquent, le sens du courant s'inverse et le condensateur commence à se décharger jusqu'à ce
> qu'un autre basculement se produise : il s'agit bien d'un multivibrateur astable. » Mise en équation (Fig.21, maille
> MS2RCS1M) : « u_s2 + R i + u_C − u_s1 = 0 » ; i = dq/dt = C du_C/dt ; **RC du_C/dt + u_C = u_S1 − u_S2** ; « Si
> u_s1 = 0, donc u_s2 = U_DD. L'équation différentielle devient : RC du_C/dt + u_C = − u_DD » ; « Si u_s1 = U_DD,
> donc u_s2 = 0. […] RC du_C/dt + u_C = + u_DD » ; « Finalement […] **RC du_C/dt + u_C = ± u_DD** ». Grandeurs
> (Fig.22) : charge [MP] : U_iC = U_M = U2 − U1 ; E_H = U1 ; U_0 = U_P = U2 →
> **T1 = RC Log((U_iC − E_H)/(U_0 − E_H)) = RC Log((U2 − U1 − U1)/(U2 − U1)) = RC Log((U2 − 2U1)/(U2 − U1))** ;
> décharge [PQ] : U_iD = U_P = U2 + U1 ; E_B = 0 ; U_0 = U_Q = U2 → **T2 = RC Log((U1 + U2 − 0)/(U2 − 0)) =
> RC Log((U1 + U2)/U2)** ; **T = T1 + T2 = RC Log((U2 − 2U1)/(U2 − U1) . (U1 + U2)/U2)** ; « Pour U2 = ½ U_DD et
> U1 = U_DD , on trouve : T1= T2 = RC Log3 = 1,1RC = 1,03 ms et δ = 0,5. » [? avec R = 22 kΩ et C = 10 nF,
> 1,1 RC = 0,24 ms ; voir doutes]. Conclusion : « Le multivibrateur à portes logiques inverseuses fonctionne aussi en
> régime de commutation. Il comporte deux états dont la durée est déterminée essentiellement par les valeurs de R et
> de C : c'est un astable fonctionnant en relaxateur. »

**L'essentiel (p.236, VERBATIM)** — « ■ Un multivibrateur astable est un générateur autonome délivrant un signal
périodique non sinusoïdal. ■ Un montage de multivibrateur astable est constitué d'un comparateur dont la sortie est
rebouclé sur son entrée inverseuse par un dipôle RC. ■ Les états haut et bas d'un multivibrateur astable dépendent
essentiellement de la constante de temps de son dipôle RC. ■ Un multivibrateur astable à amplificateur
opérationnel ou à inverseur(s) logique(s), est caractérisé par deux niveaux de la tension de sortie, une période et
un rapport cyclique. ■ La période T d'un multivibrateur astable s'écrit sous la forme : **T = T1 + T2** oùT1 est la
durée de son état haut et T2 la durée de son état bas sur une période. ■ La période T d'un multivibrateur astable à
amplificateur opérationnel s'exprime par : **T = 2RC Log(1 + 2R1/R2)** ■ Le rapport cyclique d'un multivibrateur
astable est le rapport entre la durée T1 de son état haut et sa période T : **δ = T1/T** »

### Exercices résolus

**Exercice résolu (p.237–239)** — Énoncé : générateur de signaux (Fig.1) : deux portes NAND identiques (1) et (2)
montées en inverseurs (entrée E → (1) → P → (2) → S), R entre P et N, C entre N et S ; courants d'entrée nuls ;
caractéristique de transfert (Fig.2) : u_s = U_DD = 10 V pour u_e < U_DD/2 = 5 V, 0 au-delà. « 1°) A l'instant t = 0,
l'entrée E est à l'état logique " 1 " : on considère u_E = 10 V à cet instant. a) Que valent alors les potentiels u_P et
u_S des points P et S ? b) En déduire la tension entre les points S et P. c) Cet état est-il stable ? Justifier la
réponse. 2°) a) Que vaut la tension u_C lorsque l'entrée E prend l'état logique " 0 " à un instant t = t1 ? b) Que
deviennent les valeurs des potentiels des points P et S juste après le basculement des inverseurs logiques ? c) Cet
état est-il stable ? Justifier la réponse. 3°) Ce dispositif est un multivibrateur astable. Justifier cette
qualification. 4°) A un instant t = t2, l'entrée E reprend l'état logique " 1 ". a) Quelles sont les valeurs de u_P et
de u_S juste avant et juste après l'instant t2 ? b) Représenter les évolutions de u_C, de u_P et de u_S sur une
période. c) Calculer la période T du phénomène pour R = 470 Ω et C = 100 nF. »
Solution : 1°a) V_P = 0, V_S = 10 V ; b) u_SP = V_S − V_P = 10 V ; c) u_C = V_S − V_N, V_N = V_E → u_C = 0 V ; le
condensateur se charge à travers R : « état instable » (schéma Fig.1 : 0 V, 10 V, 0 V, 10 V). 2°a) l'inverseur 1
bascule quand V_E = V_N atteint 5 V → u_C = V_S − V_E = 5 V (Fig.2) ; b) après basculement u_C « n'évolue
pratiquement pas », u_P passe de 0 à 10 V, u_S de 10 V à 0 V (Fig.3 : 10 V, −15 V, −5 V, 5 V, 0 V) ; c) u_SP = − 10 V,
décharge à travers R, état instable. 3°) évolution entre deux états instables → astable. 4°a) bascule quand V_N
retrouve 5 V : juste avant V_P = 10 V, V_S = 0 V, u_N = 5 V ; juste après V_P = 0 V, V_S = 10 V, u_N = 15 V.
4°b) chronogrammes u_S, u_P (créneaux complémentaires 0/10 V), u_N (pics à 15 V et −5 V, basculements à 5 V).
4°c) « T = 2(t2 − t1). Entre les instants t1 et t2, l'équation de u_N(t) = u_S − u_C s'écrit :
u_N(t) = (U_DD/2 + U_DD)(1 − e^(−(t−t1)/2τ)) − U_DD/2 » [exposant imprimé « (t−t1)/2τ », image] ; à t = t2,
u_N = U_DD/2 → « 1 − e^(−T/2τ) = U_DD/(U_DD + U_DD/2) = 2/3 » ; « Donc : Log 3 = T/2τ, soit : **T = 2RCLog3** » ;
« A.N : **T = 10⁻⁴ s**. » (2 × 470 × 100·10⁻⁹ × Log3 ≈ 1,03·10⁻⁴ s.)

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux** (p.240) : 1- « Un multivibrateur astable est un oscillateur auto-entretenu. » ; 2- « Un
  oscillateur de relaxation est un générateur capable de délivrer une tension périodique sinusoïdale. » ; 3- « Un
  multivibrateur astable est un oscillateur dont la sortie ne peut présenter que deux niveaux stables. » ; 4- « Un
  multivibrateur astable fonctionne grâce à un comparateur, un dipôle RC et un signal externe de déclenchement. »
  (Réponses non fournies.)
- **Ex. 2 — QCM** (p.240, « la (ou les) proposition(s) juste(s) ») : I- un multivibrateur astable possède : a- un
  seul état stable / b- deux états quasi-stables / c- deux états stables ; II- oscillateurs de relaxation (mécaniques
  ou électroniques) font intervenir : a- un comparateur / b- un réservoir d'énergie dont l'évolution fixe la valeur
  de la fréquence / c- une source de tension variable pour leur démarrage ; III- un astable évoluant grâce à un
  dipôle RC délivre une tension : a- en créneaux de fréquence dépendant des valeurs de R et C / b- sinusoïdale /
  c- en créneaux de fréquence dépendant des seuils de basculement ; IV- un astable à porte logique inverseuse diffère
  de celui à AO par : a- le principe de fonctionnement / b- la valeur de la fréquence de la tension qu'il délivre /
  c- la très grande valeur du rapport cyclique du signal qu'il délivre à sa sortie ; V- une horloge est un oscillateur
  qui délivre une tension : a- ne prenant que deux états possibles / b- en créneaux / c- sinusoïdale. (Réponses non
  fournies.)

### Exercices et problèmes

**Exercices d'application**
- **Ex. 3** (p.241) : porte CMOS commutant de 0 à 1 dans un dipôle R = 1,5 kΩ, C initialement déchargé (schéma :
  C entre la masse et A, R entre A et U_DD) ; u_c = A e^(−t/RC) + B. 1°) A et B ; 2°) a) durée t1 pour u_c = U_DD/2 ;
  b) C pour t1 = 10 ms ; 3°) C chargé à t = 0 sous U1 < U_DD : a) montrer t0 = RC Log((U_DD − U1)/(U_DD − U0)) ;
  b) t0 pour U1 = − U0 et U_DD = 2 U0 ; c) courbe de u_A pour U1 < 0. Donnée : C = 9,6 μF.
- **Ex. 4** (p.241) : comparateur à AO polarisé ± 15 V + dipôle RC (Fig.1 : R de S vers A, C de A à la masse, R1 de
  S vers +, R2 de + à la masse) ; graphe u_c(t) : phases (MN) charge de M ≈ −7,5 V à N ≈ +7 V (t ≈ 3 ms) et (NP)
  décharge vers P, tangente en M tracée ; axes u_c (V) −10 … 10 par 5, t (ms) 1 … 5. 1°) graphiquement : a) τ ;
  b) tensions de basculement ; c) T1 et T2 ; 2°) δ ; 3°) montrer T = 2 RC Log(1 + 2R2/R1) ; 4°) R et R2.
  Données : R1 = 10 kΩ, C = 100 nF.
- **Ex. 5** (p.241–242) : comparateur à seuils de valeurs absolues différentes : AO idéal saturant à ± 15 V, u_e sur
  l'entrée −, R de + à la masse, deux branches de réaction R2–D2 et R1–D1 (diodes tête-bêche). 1°) seuil U2 à u_s
  décroissante en fonction de R2, R et u_D2 ; 2°) seuil U1 à u_s croissante en fonction de R1, R et u_D1 ;
  3°) U1, U2. Données : u_D1 = u_D2 = 1 V ; R = 10 kΩ ; R1 = 20 kΩ ; R2 = 50 kΩ.
- **Ex. 6** (p.242) : astable à rapport cyclique variable : potentiomètre (R_A, R_B, curseur P), branches R–D2 et
  R–D1, C sur l'entrée −, pont R1–R2 sur l'entrée + (u_o aux bornes de R1) ; AO et diodes idéaux ;
  R1 = R2 = 10 kΩ ; à t = 0, u_S = 12 V et u_C = 0. 1°) u_o en fonction de R1, R2, u_S ; 2°) saturations ± 12 V :
  valeurs U01 et U02 de u_0 provoquant le basculement ; 3°) fonctionnement, allures de u_s(t) et u_c(t) ;
  4°) a) T1 et T2 en fonction de R, R_A, R_B, R1, R2, C ; b) T pour R = 10 kΩ, R_v = 10 kΩ [sic : R_v non défini ;
  lire R_A + R_B ?] et C = 100 nF.

**Exercices de synthèse**
- **Ex. 7** (p.242) : « Trigger de schmitt » : AO à réaction positive (u_E sur l'entrée **−**, R1 de + à la masse,
  R2 de S vers + — schéma vérifié au zoom 300 dpi : c'est le comparateur (M1) du cours, trigger **inverseur**). 1°) comparateur ou multivibrateur ? 2°) seuils ± 6 V et période T_o = 1 ms ; entrée
  u_e(t) = 12 sin(2π/T t) : a) u_s(t) en fonction de R1, R2, u_E et ε ; b) AO polarisé ± 15 V : valeur minimale de R2
  (R1 = 10 kΩ) ; c) tracer u_E et u_S, en déduire T de u_E.
- **Ex. 8** (p.242–243) : astable à AO en commutation, u_s = ± U_sat = ± 12 V ; diodes D1, D2 idéales (u_D = 0
  passante, i_D = 0 bloquée) ; schéma : R3 et branches R–D2, R–D1 vers l'entrée −, C, pont R1–R2. 1°) tableau à
  compléter (état passant/bloqué de D1 et D2 pour u_s = U_sat et − U_sat ; constante de temps) ; données :
  R = 3,3 kΩ ; R1 = R2 = R3 = 10 kΩ ; C = 10 nF ; 2°) avec Δt = RC Log((U_i − U_f)/(U_0 − U_f)) : a) T1, T2 ;
  b) δ et N.
- **Ex. 9** (p.243–244) : deux portes inverseuses identiques, C, R (Fig.1 : E → (1) → A → (2) → S ; R de P
  (entrée, côté C) à A ; C entre P et S) ; caractéristique (Fig.2) : u_s = 5 V pour u_e < 2 V, 0 au-delà ; courants
  d'entrée nuls. 1°) a) U_sat (état haut) et U_r (basculement) ; b) potentiels de P et E égaux ; 2°) a) à t = 0,
  u_E = U_sat + U_r : u_A, u_S, u_C ; b) montrer u_C + RC du_C/dt = U_sat ; c) u_C = α e^(−λt) + β : α, β, λ en
  fonction de U_sat, U_r, R, C ; en déduire u_P(t) ; d) T1 (basculement) en fonction de R, C, U_sat, U_r ;
  e) allures de u_S, u_P sur [0, T1[ ; f) u_C constante pendant le basculement : u_P et u_S à T1 + dt ;
  3°) a) après T1 : u_C + RC du_C/dt = − U_sat ; b) u_C = α' e^(−λ't) + β' : α', b' [sic, β'], λ' ; u_P ; c) même loi
  jusqu'à T ; d) T en fonction de U_sat, U_r, R, C ; A.N. R = 800 Ω, C = 20 nF ; 4°) a) compléter le graphe sur
  [T1, T[ ; b) u_S, u_P à T + dt ; c) comparer à l'état à t = 0 ; d) u_S périodique de période T.
- **Ex. 10** (p.244) : montage voisin de l'ex. 9 avec diode D idéale (en parallèle sur R2, en série avec R1) et
  résistor R_o protégeant l'inverseur 1 ; U_sat = 5 V, U_r = 2 V. 1°) à t = 0, u_E = U_sat + U_r : montrer
  T1 = R1C Log((U_r + U_sat)/U_r) ; 2°) deuxième basculement après T2 = (R1 + R2)C Log((2U_sat − U_r)/(U_sat − U_r)) ;
  3°) N et δ. (Valeurs de R1, R2, C non données.)
- **Ex. 11 — Étude de texte « Oscillateurs de relaxation »** (p.244) : systèmes bouclés accumulant puis restituant
  de l'énergie ; fréquence et amplitude dépendant du débit et des caractéristiques du système d'accumulation ;
  horloges de circuits numériques, signaux de test, porteuses en télécommunication ; fréquence peu stable →
  oscillateurs à quartz préférés ; autres domaines (vase de tantale, système thermique régulé, détecteur de
  lumière). Questions : 1°) qu'est-ce qu'un oscillateur de relaxation d'après le texte ? 2°) relever : a) les
  propriétés ; b) ce qui montre leur importance en électronique ; c) leurs autres applications.

### Réponses du manuel (p.394, lues sur l'image)

- Ex. 3 : « 1°) A = - U_DD; B = U_DD. ; 2°.a) t1 = RC Log2 2°. b) C= 9,6 μF ; 3°.b) t0 = 15,82 ms. »
- Ex. 4 : « 1°) a) τ = 2,2 ms b) U_HB = 7,5 V ; U_BH = -7,5 V c) T1= T2 = 3 ms 2°) d [sic, δ]=0,5 4°) R = 22 kΩ ;
  R2 = 14,55 kΩ » [? voir doutes].
- Ex. 5 : « 1°) U2 = (R/R+R2)(Usat - U_D2) ; 2°) U1 = (R/R + R1)(U_D1 - Usat) 2°) [sic, 3°)] U2 = 2,33 V ;
  U1 = - 4,67 V. »
- Ex. 6 : « 1°) Uo = R1Us /(R1 + R2) ; 2°) Uo2 = - Uo1 = 6 V. 4°a) T1 = (R+R_A)CLog(1 + 2R1/R2) T2 = (R+R_B)CLog(1 +
  2R1/R2) 4°b) T = (R+Rv)CLog(1 + 2R1/R2) = 3,3 ms. » [formule incohérente avec la somme T1 + T2, voir doutes].
- Ex. 7 : « 1°) Comparateur ; 2°a) u_F [sic, u_S] = (R1 + R2 /R1)(u_E - ε); 2°b) R2 = 2,5 kΩ. » [2°a : avec ε = V⁺ − V⁻
  et u_E sur l'entrée −, on trouve u_S = (R1 + R2)/R1·(u_E + ε) : signe « − ε » à lire [sic, ?] (ou ε défini V⁻ − V⁺) ;
  2°b cohérent, voir doute 6].
- Ex. 1, 2, 8, 9, 10, 11 : pas de réponse.

### En savoir plus / Documents

**« Bascules de Schmitt » (p.245–247, « D'après Daniel Robert »)** — bascule (trigger) : circuit intégré logique
(AO ou CMOS) à une sortie (0 ou 1) et une ou plusieurs entrées ; à la différence des circuits combinatoires, « la
sortie maintient son état même après disparition du signal de commande » ; symboles (Fig.1 : trigger non inverseur /
inverseur, NAND à hystérésis) ; remise en forme de signaux parasités ou à fronts lents ; oscillateurs donnant la
cadence aux circuits numériques synchronisés ; entrée CLOCK, « SIGNAL D'HORLOGE ». Application typique : bascule
astable à AO (Fig.2, renvoi « p. 230 » : T = 2RC Log(1 + 2R1/R2) ; R1, R2 = réaction positive, RC = seconde
réaction retardant le basculement) ; à porte CMOS (Fig.3) : **T = 1/N_Oscillation = RC Log((V_cc − V_T−)/(V_cc − V_T+) .
V_T+/V_T−)** ; A.N. « Pour R = 100 kΩ , C = 0,1 µF, V_cc = 5 V, V_T+ = 3,05 volts, V_T- = 1,95 V, on trouve : T = 8,9 ms
et N_oscillation = 112 Hz. » ; seuils dépendant de V_cc (variation de 4 à 5 % de la fréquence pour V_cc de 5 à 15 V),
alimentation régulée. Transformation sinus → rectangulaire (Fig.4 : pont R1–R2, condensateur de découplage ;
Fig.5 : entrée sinusoïdale, sortie rectangulaire de même fréquence ; V1 = (V_T+) − (V_T−) / 2 [sic, parenthésage]) ;
génératrice tachymétrique. Autres applications : débarrasser un signal du bruit (écart S_H − S_B > amplitude
crête-à-crête du bruit), contrôle avec hystérésis (thermostats, interrupteurs crépusculaires, niveau d'une cuve),
générateurs de musique, sonneries, Game-Boy, « bip des premiers ordinateurs ».

### Écart avec la référence (aucune)

**Aucun chapitre de `physique-bac-sciences-exp` ne correspond** (correspondance du brief confirmée) : le manuel
223433 (Sciences expérimentales) ne traite ni l'AO en comparateur, ni les portes logiques, ni les multivibrateurs.
Recherche dans `content/` (« multivibrateur », « astable », « comparateur », « amplificateur opérationnel »,
« porte logique ») : **aucun chapitre proche** ; seul point d'appui réutilisable : **sciences-exp/01 Condensateur,
dipôle RC** (équation différentielle de charge, τ = RC, lecture de τ ; attention : le chapitre publié écrit la solution
u_C(t) = B + A·e^(−αt) (cours.md l.229), alors que ce chapitre 8 utilise α·e^(−t/τ) + β (p.227) — notation à adapter) dont ce chapitre est
une application directe. Le chapitre est donc **à écrire en entier** (✅ tout ce qui suit est à ajouter) :
- ✅ multivibrateurs bistable / monostable / astable ; oscillateur de relaxation (vs harmonique) ;
- ✅ comparateur à deux seuils (trigger) à AO : ε = R1/(R1+R2) u_S − u_E, U_BH, U_HB, saturation ± U_sat, cycle
  d'hystérésis en mode XY, écarts (offset, zone linéaire) ; comparateur à porte CMOS 4093 (hystérésis) / 4011 ;
- ✅ astable = comparateur rebouclé par RC ; niveaux E_H / E_B, T = T1 + T2, rapport cyclique δ = T1/T (en %) ;
  u_C(t) = (U_i − U_f)e^(−t/RC) + U_f ; **Δt = τ Log((U_i − U_f)/(U_0 − U_f))** ; T1, T2, T ;
- ✅ trois astables : à AO (T = 2RC Log(1 + 2R1/R2), δ = 0,5, T = 2,2τ si R1 = R2), à porte CMOS à hystérésis
  (T = RC Log((U_BH − U_DD)/(U_HB − U_DD) · U_HB/U_BH)), à deux portes NAND (T = RC Log((U2 − 2U1)/(U2 − U1) ·
  (U1 + U2)/U2), T = 2,2 RC si U2 = ½U_DD) ;
- ✅ en exercices : astable à rapport cyclique variable (diodes + potentiomètre), comparateur à seuils dissymétriques
  (diodes), trigger inverseur (comparateur à deux seuils (M1)) attaqué par un sinus.
Vocabulaire et notations propres : « Log » (népérien), U_BH / U_HB, E_H / E_B, U_DD, « quasi-stable »,
« relaxateur », « trigger de Schmitt », « horloge ».

### Bornes de scope

- ✅ **INCLUS** :
  - Définitions : multivibrateur (comparateur + réservoir d'énergie + source autonome) ; bistable, monostable,
    astable ; état stable / quasi-stable ; oscillateur de relaxation ; horloge (accroche, QCM V, En savoir plus).
  - Comparateur à deux seuils à AO (réaction positive R1–R2, entrée inverseuse attaquée) : établir
    ε = R1/(R1+R2) u_S − u_E par la loi des mailles, U_BH = − R1/(R1+R2) U_sat, U_HB = + R1/(R1+R2) U_sat, u_S = ± U_sat
    selon le signe de ε ; lecture des seuils et niveaux sur chronogrammes et en mode XY ; explication qualitative des
    écarts (zone linéaire, offset).
  - Comparateur à porte CMOS inverseuse (4093 à hystérésis, 4011) : caractéristique de transfert, seuils en fraction
    de U_DD ; caractéristique de transfert d'une porte (exercices : U_DD/2 = 5 V ; U_r = 2 V, U_sat = 5 V).
  - Astable bouclé en RC : principe (charge/décharge entre U_BH et U_HB en visant E_H / E_B), équation
    RC du_C/dt + u_C = u_S, solution u_C(t) = (U_i − U_f) e^(−t/RC) + U_f (forme imposée du chapitre 1), relation
    Δt = τ Log((U_i − U_f)/(U_0 − U_f)) et son emploi pour T1, T2, T, δ.
  - Les trois montages du cours et leurs formules ; calculs de T, δ, N, R, C, seuils ; tracé et interprétation des
    chronogrammes u_C, u_S (u_S1, u_S2, u_E2, u_P, u_N) ; état des diodes idéales selon le signe de u_S (exercices).
  - Trigger inverseur (comparateur à deux seuils (M1)) attaqué par un sinus (ex. 7) ; comparateur à seuils dissymétriques (ex. 5) ; astable à rapport cyclique
    variable (ex. 6, 8) ; étude de texte.
- ⛔ **EXCLU** (absent du chapitre) :
  - Monostable et bistable étudiés quantitativement (seulement définis) ; bascules RS, D, JK, compteurs (seulement
    évoqués dans « En savoir plus » : entrée CLOCK).
  - Générateur de signal triangulaire (intégrateur), générateur de rampe, NE555, oscillateur à quartz (cité, non
    étudié), astable à transistors.
  - Décomposition en série de Fourier d'un signal non sinusoïdal ; régime de l'AO en linéaire (rappelé en prérequis
    seulement).
  - Résolution de l'équation différentielle autrement que par la forme imposée ; notation « ln ».

### Lecture

- **Pages lues en couche texte** (`pdftotext -layout`, page par page) : 220 à 247 (les 28 pages) et 394 (réponses du
  chapitre 8).
- **Pages lues sur l'image** (110 dpi) : 220 à 247 (les 28 pages) et 394 (**29 pages**) ; recadrages 250 dpi : p.228
  (formule (4)), p.241 (graphe de l'ex. 4) ; 300 dpi : p.242 (schéma de l'ex. 7, après relecture R-7). Pages 220, 221,
  222 relues sur l'image après relecture R-7 (conformes au texte transcrit).
- **Écarts couche texte / image constatés** : les symboles **δ, ε, τ, ±, ≠, flèches et racines sont perdus** dans la
  couche texte (« - = 1 » pour δ = T1/T p.226, « = R1 i - uE » pour ε p.224, « t = Log » pour Δt = τ Log p.228,
  « T = 2Log(1 + 2 R1/R2) » pour T = 2τLog p.229) ; toutes les fractions sont éclatées sur trois lignes ; p.230 le
  signe « − » de U_BH est perdu ; p.233 Fig.20 (chronogrammes) absente du texte ; p.238–239 (solution) colonnes
  entremêlées avec les schémas Fig.1–3 ; p.241 graphe de l'ex. 4 absent ; p.243 tableau de l'ex. 8 déstructuré ;
  p.394 réponses entremêlées avec la colonne du chapitre 7.
- **Coquilles [sic]** : « perfermants » (p.221) ; « opérationel », « portes logiques NO » (p.220) ; deux figures
  numérotées **Fig.7** (p.225) ; « fonction0nement » (p.233) ; « sPour déterminer la période T » (p.228) ; « u_D » pour U_DD (Fig.20 u_S1, p.233 ; « ½ U_D »
  p.234) ; question §3.2 1°) renvoie à « la figure 15 » au lieu de 17 (p.231) ; **formule (4) p.228 : numérateur
  « U_iC − U_HB » au lieu de U_iC − E_H** ; p.229 « En supposant que u_S passe de son niveau haut à son niveau bas,
  u_c croît … vers U_sat » (contradiction : u_S doit être au niveau haut) ; « b' » pour β' (ex. 9) ; « d=0,5 » pour
  δ (réponse ex. 4) ; « u_F » pour u_S (réponse ex. 7) ; « T = (R+Rv)C… » (réponse ex. 6) ; légende Fig.20 « u_S(t) »
  pour u_S1(t).
- **Doutes [?]** :
  1. **Seuils de la porte 4093 (p.225)** : imprimé « U_BH = ½ U_DD et U_HB = U_DD » (image vérifiée) ; un seuil égal à
     U_DD est physiquement impossible et §3.2 calcule ensuite avec U_BH = ½ U_DD et **U_HB = ¾ U_DD** (p.232) ; seuils
     4011 « U_BH = 0 et U_HB = ½ U_DD » également douteux (Fig.5b = basculement unique). À ne pas reprendre tel quel. 2. **§3.3 p.235 « T1 = T2 = RC Log3 = 1,1RC = 1,03 ms »** : avec R = 22 kΩ et C = 10 nF, 1,1 RC ≈ 0,24 ms (T ≈ 0,48
     ms) ; 1,03 ms ne correspond à aucune donnée du montage (coïncide numériquement avec 2RC Log3 de l'exercice
     résolu ×10). Valeur à ne pas reprendre. 3. **Formule de la question §3.2 3°) (p.231)** : « T = RC.Log((U_DD − U_HB)/(U_DD − U_BH) . U_BH/U_HB) » est l'inverse
     (argument du Log inversé, donc T < 0) du résultat établi p.232 « T = RC Log((U_BH − U_DD)/(U_HB − U_DD) .
     U_HB/U_BH) ». Garder la forme p.232. 4. **Réponses ex. 4** : U_HB = 7,5 V avec AO ± 15 V impose R2/(R1+R2) = ½ soit R2 = R1 = 10 kΩ, incompatible avec
     « R2 = 14,55 kΩ » ; et τ = 2,2 ms avec C = 100 nF donne R = 22 kΩ, puis T = 6 ms = 2RC Log(1 + 2R2/R1) donne bien
     R2 ≈ 14,5 kΩ — les réponses mélangent deux lectures. Le graphe lui-même (M ≈ −7,5 V, N ≈ +7 V à 3 ms) est trop
     grossier pour trancher. Exercice à reprendre avec données cohérentes. 5. **Réponse ex. 6 4°b** : T1 + T2 = (2R + R_A + R_B)C Log(1 + 2R1/R2) ; la formule imprimée « (R + R_v) » est fausse,
     mais la valeur 3,3 ms correspond à (2R + R_v)C Log3 avec R_v = R_A + R_B = 10 kΩ (« R_v » n'est défini nulle part
     dans l'énoncé). 6. **Ex. 7 (corrigé après relecture R-7)** : le montage est un trigger inverseur (u_E sur l'entrée −), seuils
     ± R1/(R1+R2)·U_sat ; pour que le sinus d'amplitude 12 V fasse basculer l'AO polarisé ± 15 V, R1/(R1+R2)·15 < 12, soit
     R2 > 2,5 kΩ : la réponse « R2 = 2,5 kΩ » (p.394) est **cohérente**. Seule incohérence restante : l'énoncé annonce
     des seuils de ± 6 V, qui exigeraient R2 = 15 kΩ (non demandé ; ne pas mélanger les deux à l'adaptation). 7. Exercice résolu : exposant « −(t − t1)/2τ » (image p.239) incohérent avec une constante de temps τ = RC ; il
     sert à justifier T = 2RC Log3 ; la Fig.3 de la solution porte « −15V » alors que le texte donne u_N = 15 V après
     basculement. 8. Ex. 3 : la donnée « C = 9,6 μF » est fournie alors que 2°b demande de calculer C (= 9,6 μF, réponse). 9. Tableau de l'ex. 8, valeurs graphiques de §3.1 1°b) et §3.2 2°) : non fournies par le manuel.

## 2.9 Chapitre 9 — Conversion de signaux (manuel 223471, p.248–273)

Partie du manuel : « Evolution de systèmes électriques » ; bandeau de chapitre « Conversion de signaux » ; page
d'ouverture « CONVERSION DE SIGNAUX », n° 9. **Plage exacte : p.248 (objectifs/prérequis) – p.273** (la plage
provisoire 249–274 est décalée d'une page : p.274 = objectifs du chapitre 10). Le chapitre a une **fiche technique**
(DAC 0808, p.270) et un « En savoir plus » démonstratif (C.N.A. R-2R, p.271–273). Notations : mot binaire **[N]**,
équivalent décimal **N**, éléments binaires **a_j** (a₀ = bit de poids faible) ; tension de référence notée
**U_ref / U_réf** dans le cours, **E_ref** ou **E** dans les exercices ; résistance de contre-réaction **R'** ;
« P.E. » = pleine échelle ; « C.N.A. », « C.A.N. » avec points.

**Objectifs (p.248, VERBATIM)** — « Comparer un signal analogique avec un signal numérique. » · « Distinguer un
convertisseur analogique-numérique (C.A.N.) d'un convertisseur numérique-analogique (C.N.A.). » · « Etablir
l'expression de la tension de sortie us d'un C.N.A. à réseau de résistances pondérées en fonction du nombre N
d'entrées. » · « Convertir un signal numérique en signal analogique. » · « Tracer la caractéristique de transfert
us = f (N) d'un C.N.A. »

**Prérequis (p.248)** — SAVOIR : décrire le principe de fonctionnement d'une porte logique ; décrire le principe de
conversion d'un courant en une tension ; énoncer la loi d'Ohm aux bornes d'un récepteur passif ; énumérer les
caractéristiques d'un amplificateur opérationnel. SAVOIR FAIRE : dresser la table de vérité d'une fonction logique ;
appliquer la loi d'Ohm ; établir l'expression de la tension de sortie en fonction de tension d'entrée dans le cas
d'un amplificateur opérationnel en montage sommateur ; tracer la caractéristique de transfert d'une porte logique.

**Page d'ouverture (p.249)** — photo (appareil photo numérique, texte en arc) : « Dans un appareil photo numérique,
la lumière émise par une petite zone de la vue photographiée est convertie en tension, puis numérisée par un
convertisseur analogique-numérique et mise en mémoire. » (encart oblique, vérifié sur l'image). Questions d'accroche (VERBATIM) : « Quel est le rôle de l'interface dans la chaîne de mesure en EXAO ? »
· « Qu'est-ce qui permet de transformer les signaux numériques dans un ordinateur en signaux analogiques au niveau
des périphériques tels que l'écran de son moniteur et les hauts-parleurs ? »

**Plan (titres numérotés du manuel)** — introduction (p.250 : « Fini, le temps de l'analogique ») · **1 Signaux
analogiques, logiques et numériques** (p.250–252 : 1.1 signal analogique ; 1.2 signal logique ; 1.3 signal
numérique ; 1.4 comparaison des signaux analogiques et numériques ; 1.5 numérisation décimale et binaire (rappel)) ·
**2 Convertisseurs numériques-analogiques (C.N.A.) et convertisseurs analogiques-numériques (C.A.N.)** (p.252–255 :
2.1 C.N.A. — 2.1.1 définition et symbole, 2.1.2 intérêt ; 2.2 C.A.N. — 2.2.1 définition et symbole, 2.2.2 intérêt ;
2.3 exemples de chaînes de traitement de signaux — 2.3.1 chaîne du son, 2.3.2 appareil photo-numérique) · **3
Convertisseur numérique-analogique (C.N.A.)** « Cas d'un convertisseur numérique-analogique à réseau de résistances
pondérées » (p.255–261 : 3.1 schéma du montage ; 3.2 principe de fonctionnement ; 3.3 caractéristiques d'un C.N.A. —
pleine échelle, quantum, résolution, caractéristique de transfert ; avantages et inconvénients ; cas du réseau
« R-2R ») · **4 Convertisseurs analogiques-numériques (C.A.N.)** (p.262 : 4.1 phases de la conversion ; 4.2 principe)
· L'essentiel (p.263) · Exercices : exercice résolu (p.264–265) ; Tests rapides (ex. 1–2, p.266) ; Exercices
d'application (ex. 3–4, p.266–267) ; Exercices de synthèse (ex. 5–9, p.267–269) · Fiche technique « Le DAC 0808 »
(p.270) · En savoir plus « Le C.N.A. à réseau de résistances R-2R » (p.271–273).

### Cours — Activités

- **§1–2 (p.250–255)** — cours magistral sans manipulation : Fig.1 (signal analogique g(t)), Fig.2 (signal logique
  h(t), niveaux 1/0), Fig.3 (« Signal numérique à 4 bits » : lignes a₀…a₃ regroupées en N) ; tableau décimal/binaire
  0–4 ; Fig.4a/4b (schéma et symbole du C.N.A. : entrée N sur n fils, symbole # / ∩, sortie u_s) ; Fig.5 (photo de
  circuits Analog Devices AD6622, AD6624, AD6644) ; Fig.6a/6b (schéma et symbole du C.A.N.) ; Fig.7a (micro),
  Fig.7b (chaîne du son : capteur analogique → amplificateur analogique → C.A.N. → traitement ou transmission →
  C.N.A. → amplificateur analogique → transducteur analogique) ; Fig.8 (appareil photo) ; Fig.9 (signal → capteur →
  tension U → C.A.N. → valeur numérique N → mémoire ; légende « Chaîne de traitement du son » [sic]) ; Fig.10
  (mémoire → N → C.N.A. → tension U → actionneur → grandeur physique).
- **§3.1–3.2 Étude guidée du C.N.A. à résistances pondérées 4 bits (p.255–258)** — Fig.11 : interrupteurs K3…K0
  commandés par a3…a0, résistors R, 2R, 4R, 8R, U_réf, AO (entrée + à la masse), R' en contre-réaction, sortie u_s.
  Questions (VERBATIM, p.256) : « 1°) Ecrire le mot binaire d'entrée [N] de ce convertisseur. 2°) a) Etablir
  l'expression de l'intensité du courant I3 qui parcourt le circuit : ◆ pour a3 = 1 et a2 = a1 = a0 =0, ◆ pour
  a3 = a2 = a1 = a0 = 0, ◆ exprimer I3 en fonction de U_réf, R et a3. b) Etablir l'expression de la tension u_s en
  fonction de R,R',a3 et U_réf. 3°) Préciser le rôle de l'amplificateur opérationnel dans ce montage. » Réponses
  dans le cours (Fig.12 : circuit d'entrée avec a3 = 1 ; Fig.13 : schéma équivalent simplifié à générateurs
  a_jU_ref) : voir Encadrés.
- **§3.3 Questions (p.258–260)** — « Montrer que l'expression de la tension pleine échelle d'un convertisseur
  numérique-analogique à 4 bits et à réseau de résistances pondérées (R, 2R, 4R, 8R) est : U_s.max = 15.R'.U_ref/8.R. »
  · « Montrer que pour un C.N.A. à 4 bits et à réseau de résistances pondérées (R, 2R, 4R, 8R), le quantum q s'écrit :
  q = R'.U_ref/2³.R »
- **§3.3 Expérience — caractéristique de transfert (p.259–260)** — Fig.14 : C.N.A. à résistances pondérées **3 bits**
  (interrupteurs a2, a1, a0 ; R2, R1, R0 ; R') ; AO « supposé idéal (A 741) » polarisé ± 15 V ; tension de référence
  par alimentation stabilisée (**U_réf = 5 V** lu sur la figure zoomée, absent du texte) ; voltmètre en sortie ;
  pour chaque N (0 à 7) on note u_S. Fig.15 : courbe en escalier u_s(V) 0–7 en fonction de N, avec tableau
  N 0…7 / a₀ 0 1 0 1 0 1 0 1 / a₁ 0 0 1 1 0 0 1 1 / a₂ 0 0 0 0 1 1 1 1. Question (VERBATIM) : « Montrer graphiquement
  que u_S = f(N) s'écrit : u_S = k.N, où k est une constante que l'on calculera. » (Valeurs de R0, R1, R2, R' non
  données ; paliers lus sur l'image : ≈ 0,25 ; 1,2 ; 1,9 ; 2,8 ; 4,0 ; 4,65 ; 5,75 ; 6,35 V — irréguliers, voir
  doutes.) Remarque : même manipulation avec un circuit intégré (DAC 0800 ou DAC 0808), « comme il est décrit dans la
  fiche technique de la fin du chapitre ».
- **R-2R (p.261)** — Fig.16 : réseau R/2R 4 bits, interrupteurs K0…K3, U_ref, AO, R' ; « L'étude du principe de
  fonctionnement du C.N.A. à réseau de résistances «R-2R» n'est pas au programme. » ; résultat donné (Encadrés).
- **§4 (p.262)** — Fig.17 : schéma de principe d'un C.A.N. : comparateur (AO), horloge, porte ET, compteur, C.N.A.
  rebouclé sur l'entrée + du comparateur. Aucune étude quantitative.

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Introduction (p.250)** — « Cependant, les phénomènes physiques courants sont analogiques et nos sens d'ouïe et
> de vision sont adaptés à ce qui est analogique (son et image). C'est pour cette raison que les appareils numériques
> cités plus haut sont tous munis de montages à base de circuits intégrés jouant le rôle de convertisseurs :
> analogique-numérique (C.A.N.) ou numérique-analogique (C.N.A.). »

> **Signal analogique (1.1, p.250)** — « Un signal est analogique si sa valeur varie dans le temps de façon continue
> (Fig.1 par exemple). L'information transportée par le signal à un instant t donné est sa valeur à cet instant. La
> variation des grandeurs physiques telles que la température T, la pression p, la vitesse v, est continue dans le
> temps. Ainsi, toutes ces grandeurs physiques sont des exemples de grandeurs analogiques. »

> **Signal logique (1.2, p.250)** — « Un signal (une tension électrique par exemple) est logique si sa valeur varie de
> façon discrète au cours du temps (Fig.2 par exemple). Il est constitué par la succession de deux valeurs possibles
> **V_cc** et **0 V** appelées niveaux haut et bas : le niveau haut **V_cc** correspondant à l'état logique **1** et le
> niveau bas **0 V** correspondant à l'état logique **0**. L'information transportée par le signal à un instant t donné
> est **V_cc** ou **0 V**. »

> **Signal numérique (1.3, p.250)** — « Un signal est numérique lorsqu'il est défini comme une suite de valeurs
> numériques représentées par un nombre ou un mot binaire [N] de n bits. Le mot binaire [N] est constitué par un
> ensemble de signaux logiques formant les éléments binaires du mot. La figure 3 représente un signal logique [sic,
> légende : « Signal numérique »] à 4 bits avec a₀, a₁, a₂ et a₃ qui sont les éléments binaires du mot. »

> **Comparaison (1.4, p.251)** — « ◆ Les signaux analogiques traduisent la variation continue des différentes
> grandeurs physiques. Ainsi, tous les signaux issus des capteurs sont analogiques. Cependant, un signal analogique est
> très sensible à son environnement. Sa dégradation est facile et la correction de cette dégradation est difficile,
> voire impossible. D'autre part, un signal analogique est difficile à mémoriser ou à traiter mathématiquement.
> ◆ Les signaux numériques prennent uniquement deux états, un état haut et un état bas. Un signal numérique est
> insensible au bruit. Ainsi, on peut mémoriser, traiter mathématiquement et transformer un signal numérique sans
> qu'il soit altéré. On peut par exemple faire transiter un signal sonore de qualité HI-FI par une ligne téléphonique
> sans que la bande passante réduite ou le bruit de cette ligne ne soient gênants, ce qui aurait été impensable avec un
> signal analogique ! ◆ Si un signal numérique est plus facile à stocker et à manipuler, il faut tout de même pouvoir
> l'exploiter. Ainsi, après un transport et un stockage en numérique, tout signal vidéo ou audio, devra revenir à sa
> forme analogique de départ. En effet, nos oreilles ne savent pas entendre en numérique ! »

> **Binaire (1.5, p.251–252)** — « Le "numérique" repose sur le système binaire dans lequel il ne peut exister que les
> deux valeurs **0** et **1**. Ce choix du système binaire s'explique par la facilité à reproduire électriquement ces
> deux valeurs : - la valeur **0** qui signifie l'absence de tension (0V), - la valeur **1** signifiant la présence
> d'une tension (5 V par exemple). » Tableau décimal → binaire : 0 → 0 ; 1 → 1 ; 2 → 10 ; 3 → 11 ; 4 → 100. « Un mot
> binaire [N] de n bits s'écrit avec n éléments binaires a_j, j variant de 0 à (n-1). [N] = [a_{n-1}a_{n-2}a_{n-3}
> ............a₂a₁a₀] » ; encadré : « Son équivalent décimal en code binaire naturel s'écrit :
> **N = 2^{n-1}a_{n-1} + 2^{n-2}a_{n-2} + 2^{n-3}a_{n-3} + ...............+2⁰a₀** » ; encadré : « La valeur maximale d'un
> nombre binaire de n bits, exprimé en décimal est : **N_max = 2ⁿ − 1** » ; « Exemple : Ecrivons le nombre décimal 9
> dans la base binaire à quatre bits. 9 = 2³a₃+2²a₂+2¹a₁+2⁰a₀, avec a₃=1, a₂=0, a₁=0 et a₀=1. Le nombre 9 s'écrira
> ainsi en base binaire à quatre bits : **1001**. »

> **C.N.A. (2.1.1, p.252)** — « Un convertisseur numérique-analogique, ou C.N.A. est un montage électronique
> transformant une information numérique (un nombre binaire [N]) en un signal analogique (tension ou courant) (Fig.4a
> et Fig.4b) proportionnel à la valeur décimale du nombre binaire converti. - Si la grandeur de sortie est une tension,
> elle s'écrit : **u_S = k.N**, avec k en volt. - Si la grandeur de sortie est un courant, son intensité s'écrit :
> **i_S = k'.N** avec k' en ampère. »

> **Intérêt d'un C.N.A. (2.1.2, p.253)** — « Les convertisseurs numériques-analogiques (C.N.A.) permettent de convertir
> un signal numérique en signal analogique exploitable. […] A quoi servirait un son numérique si l'on ne pouvait pas
> l'entendre ? Ainsi, dans un ordinateur multimédia, on trouve des C.N.A. pour la plupart des sorties telles que :
> - sortie audio des cartes son, - synthétiseur musical, - imprimante, - le modem (à la réception). »

> **C.A.N. (2.2.1, p.253)** — « Un convertisseur analogique-numérique, ou C.A.N. (Fig.5) est un montage électronique
> transformant un signal analogique (une tension u_E) appliqué à son entrée en un nombre binaire [N] de sorties,
> proportionnel à cette grandeur u_E (fig.6a et 6b). **N = K.u_E** avec k en v⁻¹ [sic, V⁻¹] » ; intérêt (2.2.2) :
> « transformer en valeurs numériques un phénomène variant dans le temps pour assurer son stockage ou son
> traitement » ; périphériques à C.A.N. : « les cartes d'acquisition vidéo, - les scanners, - les cartes de capture
> sonore, - les lecteurs (optiques comme le lecteur de cédérom), - les modems (à l'émission). »

> **Chaînes de traitement (2.3, p.254–255)** — son : micro (capteur analogique), amplification, numérisation par
> C.A.N., traitement numérique (mixage), stockage « presque toujours numérique (compact disk CD) », lecteur de CD à
> C.N.A., amplification, enceintes. Appareil photo : « La lumière émise par une petite zone de la vue photographiée
> est convertie en tension par un photo-capteur, puis numérisée par un convertisseur analogique-numérique (C.A.N.) et
> mise en mémoire. L'appareil photo (Fig.8) contient un très grand nombre de capteurs formant un quadrillage […]. » ;
> restitution : « Chacune des données numériques de ce fichier est convertie par un convertisseur numérique-analogique
> (C.N.A.) en une tension commandant l'éclairage plus ou moins intense d'un point (pixel) de l'écran. »

> **Schéma du C.N.A. à résistances pondérées (3.1, p.255–256)** — « La réalisation du montage de principe d'un
> convertisseur numérique-analogique (C.N.A.) à réseau de résistances pondérées nécessite essentiellement : - une
> tension de référence U_ref, - un ensemble de n résistors de résistances pondérées à la puissance de 2 (R, 2R,
> 4R….2^{n-1} R), - des interrupteurs commandés par les variables logiques a_j du signal à transformer, - un
> amplificateur opérationnel fonctionnant en régime linéaire. » Remarque : « Pour obtenir une conversion de qualité,
> il faut s'assurer que la tension constante U_ref n'est pas affectée par une diminution de la température ou autre. »

> **Principe (3.2, p.256–258)** — « pour a_j = 1, l'interrupteur k_j est fermé. Le résistor correspondant de
> résistance **R_j = 2^{(n-j-1)}R** est parcouru par un courant I_j qui dépend de sa propre valeur (avec n = 4). En
> revanche, pour a_j = 0, l'interrupteur k_j est ouvert. Le même résistor n'est alors parcouru par aucun courant. »
> Encadré : **N = 2³a₃ + 2²a₂ + 2¹a₁ + 2⁰a₀**. « L'amplificateur opérationnel étant supposé idéal, ainsi u⁺=u⁻=0. Par
> suite, on écrit en convention récepteur : U_R = - U_ref, ce qui donne : **I₃ = − U_ref/R**. » ; a₃ = … = a₀ = 0 :
> **I₃ = 0** ; « **I₃ = − a₃U_ref/R**, avec a₃ = 0 ou bien 1. Ainsi, on a : U_R = -a₃U_ref. En généralisant ce résultat
> à toutes les dérivations d'entrée de résistance : R_j = 2^{(n-j-1)}R , on aura : **I_j = − a_jU_ref/R_j et
> U_Rj = −a_jU_ref**. » ; « us + R'i' = 0. Par suite, us = - R'i'. Or i' = i car i⁻ = 0. i est la somme des courants
> collectés par les commutateurs k_j fermés : i = I₃+ I₂+ I₁+ I₀. » ; encadré : **I₃ = − a₃U_ref/R , I₂ = − a₂U_ref/2R ,
> I₁ = − a₁U_ref/4R et I₀ = − a₀U_ref/8R** ; « Pour a₃ = a₂ = a₁ = a₀ =1, nous constatons que les courants générés par
> les résistances pondérées de R à 8R forment une suite géométrique de raison ½. » ; encadré :
> **i = − (a₃U_ref/R + a₂U_ref/2R + a₁U_ref/4R + a₀U_ref/8R) (3)** ; « Il vient donc : u_s = R'(a₃U_ref/R + a₂U_ref/2R +
> a₁U_ref/4R + a₀U_ref/8R) » ; u_s = (R'.U_ref/8.R)(8.a₃ + 4.a₂ + 2.a₁ + a₀) = (R'.U_ref/8.R)(2³.a₃ + 2².a₂ + 2¹.a₁ +
> 2⁰.a₀) ; encadré « Donc : **u_s = (R'.U_ref/8.R) N** » ; **u_S = k.N , avec k = R'.U_ref/8.R**. « Ce montage réalise
> bien une conversion numérique-analogique puisque la tension de sortie u_s est proportionnelle au nombre binaire N
> d'entrée. »

> **Conclusion (3.2, p.258)** — « Dans le cas d'un C.N.A. à réseau de résistances pondérées (R, 2R, 4R, 8R,
> …2^{n-1}R), le signal analogique (tension électrique u_s) issue de la conversion d'un signal numérique (mot binaire
> [N]) est proportionnel à l'équivalent décimal N de [N] : **u_s = KN. avec k = R'U_ref/2^{n-1}R** , n étant le nombre
> de bits du mot binaire converti N. »

> **Pleine échelle (3.3, p.258)** — « C'est la tension maximale U_Smax (tension que l'on ne peut jamais atteindre)
> prévue en sortie à laquelle correspond la valeur maximale N_max = 2ⁿ -1. » Encadré : **P.E. = U_Smax = k.N_max**
> « Avec P.E. en volt. » ; « Cas général : […] l'expression de la tension pleine échelle d'un C.N.A. à n bits et à
> réseau de résistances pondérées (R, 2R, 4R, 8R, ... 2^{n-1}R) est : **P.E. = (2ⁿ − 1).R'.U_ref/2^{n-1}.R** » ;
> Remarque (p.259) : « La tension de référence U_ref est calculée pour que le maximum de tension de sortie (U_s max) soit
> inférieure à la tension de saturation de l'amplificateur intégré. »

> **Quantum (p.259)** — « Le quantum, noté q, pour un convertisseur C.N.A. correspond à la quantité élémentaire de
> variation du signal de sortie u_s correspondant à une variation de ± 1 de N en entrée.
> **q = U_smax/(2ⁿ − 1) = P.E./(2ⁿ − 1) = P.E./N_max** pour un convertisseur de n bits. » Remarque : « **q = (U_Smax −
> U_Smin)/2ⁿ** si U_Smin ≠ 0. Le quantum s'exprime en volt. » [incohérence 2ⁿ / 2ⁿ − 1, voir doutes]

> **Résolution (p.259)** — « C'est le plus petit incrément possible en entrée. En valeur absolue, elle est égale au
> quantum q avec q = U_smax/(2ⁿ − 1). La résolution relative d'un C.N.A. est définie par rapport au nombre de bits n
> du mot binaire [N] à convertir. Elle correspond à la variation d'une unité du nombre binaire d'entrée. La résolution
> relative (**r**) d'un C.N.A. est égale à l'inverse du nombre de combinaisons binaires que le convertisseur est capable
> de convertir **r = 1/2ⁿ** où n représente le nombre de bits. Ainsi, un C.N.A. à 4 bits possède 2⁴ combinaisons à
> l'entrée (de 0000 à 1111). Par conséquent, sa résolution relative est 1/16. Celle d'un C.N.A. à 8 bits est 1/256. »

> **Caractéristique de transfert (p.260)** — « Cette courbe qui traduit l'évolution de la tension analogique de sortie
> u_S en fonction de N est appelée caractéristique de transfert du convertisseur numérique-analogique. Cette
> caractéristique u_S = f(N) est constituée par une suite de points s'appuyant sur une droite qui passe par l'origine
> (Fig.15). »

> **Avantages et inconvénients (p.261)** — « L'avantage du convertisseur numérique-analogique à résistances pondérées
> est sa simplicité. Cependant, dans la pratique, il est très délicat et même difficile de réaliser un réseau de
> résistances ayant un rapport de valeurs précis. En effet, réaliser des résistors identiques ne pose pas problème,
> mais trouver quatre résistors de résistances de valeurs parfaitement ajustées est très difficile en pratique. »

> **C.N.A. R-2R (p.261–262)** — « Ce type de convertisseur prend en compte les défauts du C.N.A. à résistances
> pondérées. Il est bâti autour d'un réseau de résistances, composé de deux valeurs seulement, R et 2R. […] L'étude du
> principe de fonctionnement du C.N.A. à réseau de résistances «R-2R» n'est pas au programme. Mais, ça n'empêche pas
> de le connaître et de le comprendre surtout que c'est l'un des principes adoptés dans les circuits intégrés utilisés
> dans la conversion des signaux. On montre que : **u_s = − (R'.U_ref/16.R).N** , pour un C.N.A. à 4bits et à réseau
> de résistances « R-2R ». »

> **C.A.N. (4.1–4.2, p.262)** — « D'une manière générale, convertir une grandeur analogique en une grandeur numérique
> nécessite deux opérations successives : - la quantification qui transforme la valeur analogique de la grandeur
> d'entrée en un nombre fini de niveaux, - le codage qui associe une valeur numérique à chacun de ces niveaux. » ;
> « Le principe d'un C.A.N. consiste à comparer deux grandeurs analogiques (tensions) réalisées à l'aide
> d'amplificateurs opérationnels. L'une de ces grandeurs est la tension à convertir, tandis que l'autre grandeur
> correspond à la sortie du C.N.A. étudié précédemment (Fig.17). »

**L'essentiel (p.263, VERBATIM)** — « ■ Un signal est dit analogique lorsque sa valeur varie de façon continue au
cours du temps. ■ Un signal est dit logique si sa valeur varie de façon discrète au cours du temps ; il prend
uniquement deux états, un état haut et un état bas. ■ Un C.N.A. est un montage électronique qui transforme une
information numérique (un mot binaire [N]) en un signal analogique proportionnel à la valeur décimale du nombre
binaire converti. ■ La tension pleine échelle (P.E.) d'un C.N.A. est la valeur maximale de la tension de sortie du
convertisseur : **P.E. = U_smax = K.N_max.** ■ Le quantum, noté q, pour un convertisseur C.N.A. correspond à la
quantité élémentaire de variation du signal de sortie u_s correspondant à une variation de ± 1 de N en entrée. ■ Le
quantum s'exprime : **q = U_smax/(2ⁿ − 1)**. ■ Un C.A.N. est un montage électronique qui transforme un signal analogique
(une tension u_E) appliquée à son entrée en un nombre binaire [N] de sortie (proportionnel à cette tension u_E). ■ Le
principe d'un C.A.N. consiste à comparer deux grandeurs analogiques (tensions) réalisées à l'aide d'amplificateurs
opérationnels. »

### Exercices résolus

**Exercice résolu (p.264–265)** — Énoncé : « On considère le convertisseur numérique C.N.A. à de [sic] 4 bits de la
figure 1, utilisant une échelle de résistances pondérées (R_o = 8 R ; R₁ = 4 R ; R₂ = 2 R ; R₃ = R). L'amplificateur
opérationnel fonctionne en régime linéaire. Il est supposé idéal. Il est polarisé ± V_cc, avec V_cc = 12 V ;
E_ref = 4 V et R = R'. » (registre a₃…a₀, interrupteurs k3…k0, E_ref). « 1°) Montrer que l'expression de l'intensité
du courant I₃ qui parcourt le résistor de résistance R est : I₃ = − a₃E_ref/R. 2°) Exprimer l'intensité du courant i
qui traverse le résistor R' en fonction de a_j, E_ref et R. 3°) Préciser l'importance de l'amplificateur
opérationnel dans un montage pareil. 4°) Exprimer u_s en fonction de a_j, E_ref, R et R' et montrer que u_s = k.N.
5°) En déduire le quantum q et la pleine échelle U_s max du C.N.A . »
Solution : 1°) seul k3 fermé, loi des mailles « E_ref + U_R − ε = 0 avec ε = 0 » → I₃ = − E_ref/R (1) ; tous ouverts
→ I₃ = 0 (2) ; maille équivalente à un générateur a₃E_ref en série avec R → **I₃ = − a₃E_ref/R**. 2°) loi des nœuds
i = I₃ + I₂ + I₁ + I₀ → i = − E_ref/R [a₃ + a₂/2 + a₁/4 + a₀/8] → **i = − (E_ref/8R)[8a₃ + 4a₂ + 2a₁ + a₀] (3)**.
3°) « L'amplificateur opérationnel a pour rôle de convertir le courant i en une tension u. » 4°) u_s + u_R' + ε = 0,
u_S = − R'.i', i' = i → u_s = R'.(E_ref/8R)[8a₃ + 4a₂ + 2a₁ + a₀] → **u_s = K.N , avec k = R'.E_ref/8R** et
N = [8a₃ + 4a₂ + 2a₁ + a₀]. 5°) quantum : a₀ = 1, a₃ = a₂ = a₁ = 0 → **q = R'.E_ref/8R** ; pleine échelle :
a₃ = a₂ = a₁ = a₀ = 1 → **P.E. = 15.R'.E_ref/8R**. (Les valeurs numériques E_ref = 4 V, R = R', V_cc = 12 V ne sont pas
exploitées ; elles donneraient q = 0,5 V et P.E. = 7,5 V < 12 V — calcul non fait par le manuel.)

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux** (p.266) : 1- « Un signal est dit logique si sa valeur varie de façon continue au cours du
  temps. » ; 2- « Un signal numérique est plus facile à stocker et à manipuler. » ; 3- « Un convertisseur
  numérique-analogique transforme une information numérique en courant. » ; 4- « L'amplificateur opérationnel dans un
  C.N.A. a pour rôle de convertir un courant I en tension analogique u_s. » ; 5- « Le quantum q pour un convertisseur
  C.N.A. représente la valeur de la tension maximale qu'il peut transmettre. » (Réponses non fournies.)
- **Ex. 2 — QCM** (p.266) : 1- la tension de référence dans un C.N.A. est : a- indépendante de la tension de sortie /
  b- indépendante du signal d'entrée / c- dépend de la tension de saturation de l'AO ; 2- nombre binaire de 36 :
  a- 110000 / b- 101000 / c- 100100 ; 3- nombre de combinaisons d'un C.N.A. 4 bits : a- 16 / b- 32 / c- 64 ; 4- la
  résolution d'un C.N.A. dépend : a- de E_ref / b- du nombre de bits à convertir / c- de la pleine échelle ; 5- P.E.
  d'un C.N.A. 8 bits à résistances pondérées : a- U_S max = 7.R'.E_ref/4.R / b- U_S max = 15.R'.E_ref/8.R /
  c- U_S max = 225.R'.E_ref/128.R [sic : la valeur juste 255.R'.E_ref/128.R ne figure pas parmi les propositions ;
  image vérifiée]. (Réponses non fournies.)

### Exercices et problèmes

**Exercices d'application**
- **Ex. 3** (p.266) : C.N.A. 3 bits (Fig.2) : générateurs a₂E, a₁E, a₀E en série avec R/4, R/2, R vers l'entrée −,
  R' en contre-réaction ; E = 10 V, R = 10 R'. 1°) I traversant R en fonction de R, a₀, E ; 2°) u_s en fonction de N ;
  3°) quantum q et pleine échelle.
- **Ex. 4** (p.267) : signal numérique → analogique de pleine échelle 10 V, C.N.A. à résistances pondérées 8 bits.
  1°) nombre de niveaux d'entrée ; 2°) quantum q ; 3°) u_s pour l'information 11001000.

**Exercices de synthèse**
- **Ex. 5** (p.267) : C.N.A. 8 bits (Fig.3) : registre (de haut en bas 1 1 0 0 1 0 1 0), interrupteurs k_j,
  résistances R, 2R, …, 128R (k₀ associé à 128 R), R₁ en contre-réaction, E_ref. 1°) a) I₀ dans 128 R ; b) u_S en
  fonction de a₀, R, R₁, E_ref ; 2°) montrer que pour 11001010 : u_s = [E_ref/R + E_ref/2R + E_ref/16R +
  E_ref/64R].R₁ ; 3°) u_s correspondant à cette information « sachant que la tension maximale de sortie de
  l'amplificateur opérationnel est 10 V » ; 4°) choix de E_ref pour un fonctionnement convenable. (Les questions 3°
  et 4° sont en tête de la colonne de droite de p.267, au-dessus de l'ex. 6 : elles appartiennent à l'ex. 5, comme
  le confirment les réponses p.395.)
- **Ex. 6** (p.267–268) : C.N.A. à résistances pondérées 3 bits (Fig.4) : entrées 2, 1, 0 par 5 kΩ, 10 kΩ, 20 kΩ,
  contre-réaction 4 kΩ, voltmètre ; AO ± 15 V ; convention « la valeur 1 sera représentée par le potentiel négatif
  - 5 V , la valeur 0 par le potentiel 0 V » ; entrée non connectée = 0 ; E_ref = - 5 V. 1°) expression de u_s ;
  2°) compléter le tableau (N de 0 à 7, écriture en base 2, u_s) et le graphe u_s = f(N) ; 3°) U_Smax ; 4°) N_max ;
  5°) résolution.
- **Ex. 7** (p.268) : AO idéal, linéaire, ± 15 V ; sommateur inverseur : V_A, V_B, V_C, V_D à travers R_A, R_B, R_C,
  R_D (courants I_A…I_D), contre-réaction R₀ (I₀). 1°) rôle de l'AO ; 2°) a) I_A ; b) I_B ; 3°) I₀ en fonction de
  u_S et R_o ; 4°) u_S en fonction de V_A…V_D et R_A…R_D, R₀ ; 5°) R_A = 2.R_B, R_A = 4.R_C = 8.R_D, R_A = 10 kΩ,
  R₀ = 1 kΩ : u_S en fonction de V_A, V_B, V_C, V_D.
- **Ex. 8** (p.268) : C.N.A. 3 bits à résistances pondérées R, R/2, R/4 (a₂E sur R/4, a₁E sur R/2, a₀E sur R),
  contre-réaction α.R ; AO idéal ± 10 V ; E = 4,5 V. 1°) a₀ = 1, a₁ = a₂ = 0 : u_s en fonction de E, a₀, α ;
  2°) u_s en fonction de E, N, α ; 3°) quantum q en fonction de α ; 4°) α pour q = − 1 V ; 5°) montage rendant u_s
  positive.
- **Ex. 9 — Étude de texte** (p.268–269, « Sophie Fleury, L'Internaute ») : phénomènes continus ; enregistrement
  analogique (cassette vidéo, cassette audio, disque vinyle) vs signal numérique (valeurs bien définies en nombre
  limité) ; « La représentation d'un signal analogique est donc une courbe, tandis que celle d'un signal numérique
  peut être visualisée par un histogramme » (figure : sinusoïde amortie échantillonnée en bâtons) ; copie d'une
  cassette = pertes. Questions : 1°) représentation d'un signal numérique en fonction du temps ; 2°) plus simple de
  reproduire un signal numérique ou analogique ? 3°) inconvénient d'un support analogique ; 4°) peut-on se limiter au
  numérique et abandonner l'analogique ?

### Réponses du manuel (p.395, lues sur l'image)

- Ex. 3 : « 1°) I = a_oE / R . 2°) u_S= -(R'E/R)N. 3°) q=-R'E/R, q = - 1 V, P.E.= -7 V. »
- Ex. 4 : « 1°) n = 28 [sic, 2⁸ : exposant perdu dans le manuel] = 256. 2°) q = (P.E.)/2ⁿ - 1 = 39 mV. 3°) v_S [sic] = 7,84V. »
- Ex. 5 : « 1°) a) I_o=-(a_oE_ref)/128R, b)u_S=(a_oR1/128R)E_ref. 2°) a1 = a3 = a6 = a7 =1 et a_o = a2 = a4 = a5 =0.
  3°) u_S=7,88V. 4°)U_S max< U_Sat de l'amplificateur. »
- Ex. 6 : « 1°) u_S = -(R'E_ref4R)N [sic, lire −(R'E_ref/4R)N]. 2°) q = 143 mV. 2°) U_Smax = 1 V. 4°) N_max = 7.
  5°) r = 1/2ⁿ = 1/8. » [? voir doutes]
- Ex. 7 : « 1°) Donner une tension à partir d'un courant. 2°) I_A = V_A/R_A, I_B = V_B/R_B. 3°) I_o = - u_S /R_o.
  5°) u_S = 0,1(8 V_D + 4 V_C + 2 V_B + V_A). » [? signe, voir doutes]
- Ex. 8 : « 1°) u_S= - a.a_o.E [a = α]. 2°) u_S = -a.E.N . 3°) q = -a.E. 4°) a = 0,22 ; 5°) insérer un amplificateur
  opérationnel. »
- Ex. 1, 2, 9 : pas de réponse.

### En savoir plus / Documents

- **Fiche technique « Le DAC 0808 » (p.270)** — « Le DAC 0808 est un convertisseur à 8 bits dont la conversion est de
  type "R-2R". pour la conversion, il est associé à un amplificateur opérationnel utilisé en convertisseur courant /
  tension. L'amplificateur opérationnel dont l'entrée inverseuse est reliée à la broche 4 permet d'obtenir la tension
  analogique de sortie. » Brochage (Fig.1) : 1 NC, 2 GND, 3 V⁻cc, 4 I out, 5–12 B1…B8 (5 B1, 6 B2, 7 B3, 8 B4, 9 B5,
  10 B6, 11 B7, 12 B8), 13 V⁺cc, 14 U ref (+), 15 U ref (−), 16 Comp ; légende « B1 à B7 [sic, B8] : entrées
  numériques, I Out : sortie courant, U_ref (+), U_ref (-) : entrées de la tension de référence, V⁺cc : alimentation
  +15 V, V⁻cc : alimentation -15 V, Comp : compensation. NC : non connectée ». Fig.2 : montage DAC 0808 + AO (R2 sur
  broche 15, R1 en contre-réaction de l'AO relié à la broche 4) ; étiquettes d'entrées « B1, B2, B2, B4, B6, B8, B7,
  B2 » [sic, numérotation erronée sur la figure].
- **En savoir plus « Le convertisseur numérique-analogique à réseau de résistances « R-2R » » (p.271–273)** — Fig.1
  (légende erronée « Schéma du montage d'un C.N.A avec un DAC 0808 » [sic]) : réseau R/2R 4 bits, K0…K3 (« Ks »
  [sic]), E_ref, AO inverseur, R'. « Pour a_j = 1 , l'interrupteur k_i est au potentiel E_ref. Par contre, pour
  a_i=0, k_j est à la masse. » → Fig.2 (schéma simplifié, générateurs a_jE_ref, nœuds A, B, C, D). Démonstration par
  **théorème de Thévenin** et **théorème de superposition** en 5 étapes : E_0T = a₀E_ref.2R/4R = a₀E_ref/2,
  R_0T = 2R//2R = R ; E_1T = a₁E_ref R/2R + E_0T R/2R = a₁E_ref/2 + a₀E_ref/4, R_1T = R ;
  E_2T = a₂E_ref/2 + a₁E_ref/4 + a₀E_ref/8, R_2T = R ; E_3T = a₃E_ref/2 + a₂E_ref/4 + a₁E_ref/8 + a₀E_ref/16 ;
  5ᵉ étape (Fig.7, sortie notée « u8 » [sic]) : E_3T − U_R + ε = 0, u_s + U_R' − ε = 0, I = I' + I⁻ →
  u_s = − (R'/R) E_3T = − (R'E_ref/16.R)[8a₃ + 4a₂ + 2a₁ + a₀] → **u_s = − (R'.E_ref/16R) N**. « On se propose
  d'exprimer la tension de sortie u_s en fonction de E_ref, R, R [sic, R'] et N. »

### Écart avec la référence (aucune)

**Aucun chapitre de `physique-bac-sciences-exp` ne correspond** (correspondance du brief confirmée) ; recherche dans
`content/` (« analogique », « numérique », « C.N.A. », « binaire ») : aucun chapitre de physique proche (seule
mention : `physique-1ere-sec/04-tension-electrique`, voltmètre numérique, sans rapport). Le chapitre est **à écrire
en entier** (✅ tout est à ajouter) ; il s'appuie sur des prérequis hors référence (AO idéal en régime linéaire,
montage sommateur inverseur, portes logiques) que la fiche du programme Sciences de l'informatique doit situer
(chapitres antérieurs du manuel ou classes précédentes — non vérifié ici) :
- ✅ signaux analogique / logique / numérique ; comparaison (bruit, mémorisation, traitement) ; numération binaire
  naturelle (N = Σ 2^j a_j, N_max = 2ⁿ − 1, conversions décimal ↔ binaire) ;
- ✅ C.N.A. et C.A.N. : définitions, symboles, u_S = k.N, N = K.u_E, intérêt, chaînes son / appareil photo ;
- ✅ C.N.A. à résistances pondérées (n bits) : I_j = − a_jU_ref/R_j, i = Σ I_j, u_s = − R'i, **k = R'U_ref/2^{n−1}R**,
  P.E., quantum q, résolution relative r = 1/2ⁿ, caractéristique de transfert en escalier ; avantages/inconvénients ;
- ✅ C.N.A. R-2R : résultat seul (u_s = − R'U_ref N/16R, 4 bits), démonstration Thévenin hors programme (lecture) ;
- ✅ C.A.N. : quantification + codage, principe par comparaison avec la sortie d'un C.N.A. (schéma seul).
Vocabulaire : « pleine échelle (P.E.) », « quantum », « résolution relative », « code binaire naturel », « mot
binaire [N] », « caractéristique de transfert », U_ref/E_ref.

### Bornes de scope

- ✅ **INCLUS** :
  - Définitions des signaux analogique, logique (V_cc / 0 V ↔ 1 / 0), numérique (mot de n bits) ; comparaison.
  - Binaire naturel : écrire N à partir de [N] et inversement (9 → 1001 ; QCM 36 ; 11001000 → 200 ; 11001010) ;
    N_max = 2ⁿ − 1 ; nombre de combinaisons 2ⁿ.
  - C.N.A. et C.A.N. : rôle, symbole, u_S = k.N (k en V), i_S = k'.N, N = K.u_E (K en V⁻¹) ; exemples de
    périphériques ; chaînes de traitement.
  - C.N.A. à résistances pondérées : établir I_j, i, u_s, k (3, 4 et 8 bits ; générateurs a_jE en entrée ;
    convention de signe E_ref < 0 de l'ex. 6) ; P.E. = k.N_max = (2ⁿ − 1)R'U_ref/2^{n−1}R ; q = U_smax/(2ⁿ − 1) ;
    r = 1/2ⁿ ; choix de U_ref (U_smax < U_sat) ; rôle de l'AO (convertisseur courant → tension) ; tracer et
    exploiter la caractéristique de transfert u_s = f(N) ; rendre u_s positive (AO inverseur supplémentaire).
  - Sommateur inverseur à AO (ex. 7) ; avantages/inconvénients du réseau pondéré.
  - C.N.A. R-2R : connaître le schéma et le résultat u_s = − R'U_ref N/16R (4 bits).
  - C.A.N. : quantification, codage, principe (comparateur + C.N.A.), qualitatif.
- ⛔ **EXCLU** :
  - **Démonstration du C.N.A. R-2R** (« n'est pas au programme », p.261) et théorèmes de Thévenin / superposition
    (seulement en « En savoir plus ») ; brochage du DAC 0808 (fiche technique, non exigible).
  - Étude quantitative d'un C.A.N. (C.A.N. à rampe, à approximations successives, flash, temps de conversion),
    échantillonnage, théorème de Shannon, fréquence d'échantillonnage (absents).
  - Codes autres que le binaire naturel (BCD, Gray, complément à 2), hexadécimal ; arithmétique binaire.
  - Erreurs de quantification, non-linéarité, temps d'établissement d'un C.N.A.

### Lecture

- **Pages lues en couche texte** : 248 à 273 (les 26 pages) et 395 (réponses du chapitre 9).
- **Pages lues sur l'image** (110 dpi) : 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264,
  265, 266, 267, 268, 269, 270, 271, 272, 273, 249, 248, 395 (**27 pages** : 248 à 273 et 395) ; recadrage 250 dpi :
  p.259 (Fig.14, U_réf = 5 V). Page 248 relue sur l'image après relecture R-7 (conforme).
- **Écarts couche texte / image** : exposants perdus (« 2n-1an-1 », « Nmax = 2n -1 », « Rj = 2(n-j-1)R ») ; toutes les
  fractions éclatées (I_j, k, P.E., q) ; symboles ≠ et ± perdus p.259 ; crochets de la solution p.265 rendus
  « ' ( ! # " » ; schémas (Fig.11, 13, 14, 16, 17, ex. 3–8) déstructurés ou absents ; Fig.15 (escalier et tableau)
  partiellement rendue ; U_réf = 5 V de Fig.14 absent du texte ; colonnes de l'ex. 5 / ex. 6 entremêlées p.267
  (attribution des questions 3°–4° à l'ex. 5 établie sur l'image et les réponses) ; p.395 réponses ch.9/ch.10
  entremêlées.
- **Coquilles [sic]** : « figure 3 représente un signal logique à 4 bits » (légende : signal numérique, p.250) ;
  « k en v⁻¹ » (p.253) ; « résistances pondérés » (légende Fig.11) ; Fig.9 légendée « Chaîne de traitement du son »
  pour la chaîne de l'appareil photo (p.255) ; « C.N.A. à de 4 bits » (p.264) ; QCM 5-c « 225 » (p.266) ; « R/2' »
  (Fig.2 ex. 3, p.266) ; DAC 0808 « B1 à B7 » et étiquettes B2 répétées (p.270) ; légende Fig.1 p.271 « avec un DAC
  0808 » ; « Ks » (p.271) ; « u8 » (Fig.7, p.273) ; « en fonction de E_ref, R, R et N » (p.271) ; réponse ex. 6
  « R'E_ref4R » ; réponse ex. 4 « v_S ».
- **Doutes [?]** :
  1. **Quantum** : définition principale q = U_smax/(2ⁿ − 1), mais la remarque p.259 écrit q = (U_Smax − U_Smin)/2ⁿ
     (dénominateur 2ⁿ) — incohérence interne ; et la pleine échelle est dite « tension que l'on ne peut jamais
     atteindre » tout en valant k.N_max (atteinte pour N = N_max). À trancher : retenir q = P.E./(2ⁿ − 1) = k
     (cohérent avec l'exercice résolu et les réponses ex. 4). 2. **Fig.15 (p.260)** : paliers irréguliers (≈ 0,25 ; 1,2 ; 1,9 ; 2,8 ; 4,0 ; 4,65 ; 5,75 ; 6,35 V), u_s(0) ≠ 0 ;
     aucune valeur de R0, R1, R2, R' : k « que l'on calculera » ne peut être déterminé qu'approximativement (≈ 0,9 V)
     ; le manuel ne donne pas la valeur. 3. **Réponse ex. 6** : avec les valeurs de Fig.4 (5, 10, 20 kΩ ; R' = 4 kΩ ; E_ref = −5 V), u_s = 4·5·N/20 = N (V),
     soit q = 1 V et U_Smax = 7 V ; les réponses « q = 143 mV ; U_Smax = 1 V » correspondent à un U_Smax de 1 V posé
     a priori (1/7 V). Incohérent avec le schéma. 4. **Réponse ex. 7 5°)** : le sommateur inverseur donne u_S = − R₀ Σ V/R = − 0,1(V_A + 2V_B + 4V_C + 8V_D) ; le
     signe « − » manque dans la réponse imprimée. 5. **QCM 2-5** : aucune proposition juste (P.E. 8 bits = 255 R'E_ref/128R) ; b- est la P.E. d'un 4 bits. 6. Exercice résolu : données numériques (E_ref = 4 V, V_cc = 12 V, R = R') non exploitées par la solution.

## 2.10 Chapitre 10 — Ondes mécaniques progressives (manuel 223471, p.274–307)

Partie du manuel : « Ondes » (bandeau « Ondes • Ondes mécaniques progressives ») ; page d'ouverture « ONDES
MECANIQUES PROGRESSIVES », n° 10. **Plage exacte : p.274 (objectifs/prérequis) – p.307** (plage provisoire 275–308
décalée d'une page : p.308 = objectifs du chapitre 11). **Pas de page d'ouverture de partie « Ondes »** dans ce manuel
(223433 en a une, p.188–189). **Constat central : le cours (p.276–294) est le MÊME TEXTE que celui du chapitre 7 du
manuel 223433** (mêmes titres, manipulations, tableaux, figures, encadrés, mêmes coquilles « unidimentionnel »,
« verticlament », « prorogation », « armortissement ») ; l'exercice résolu et les exercices 1 à 14 sont identiques
(énoncés et données) aux ex. 1–14 de 223433. Les écarts sont listés plus bas (§ Écart). Notation : élongation y,
source S ou O, a amplitude, φ_s phase initiale, θ retard, Δφ déphasage, T_e / N_e période/fréquence des éclairs.

**Objectifs (p.274, VERBATIM, vérifiés sur l'image)** — « Distinguer entre une onde transversale et une onde
longitudinale. » · « Reconnaître que la propagation d'une onde est due à une propagation d'énergie sans transport de
matière. » · « Réaliser une expérience illustrant la propagation d'une onde sinusoïdale dans un milieu homogène et
isotrope. » · « Identifier dans un milieu de propagation donné, les propriétés dont dépend la célérité d'une onde. » ·
« Etablir l'équation horaire du mouvement d'un point donné du milieu de propagation connaissant celle de la source
d'onde progressive et représenter graphiquement le diagramme du mouvement de ce point. » · « Représenter
graphiquement l'aspect à un instant donné, du milieu (ou d'une coupe du milieu) de propagation d'une onde
progressive. » · « Reconnaître la double périodicité d'une onde sinusoïdale. »

**Prérequis (p.274, image)** — SAVOIR : définir un phénomène périodique ; définir la période T et la fréquence N d'un
phénomène périodique ; écrire la relation N = 1/T ; définir une grandeur sinusoïdale ; définir la pulsation et
l'amplitude d'une grandeur sinusoïdale ; écrire la relation T = 2π/ω (ou N = ω/2π). SAVOIR FAIRE : utiliser
l'oscilloscope ; appliquer les relations N = 1/T et T = 2π/ω (ou ω = 2πN) ; représenter graphiquement une grandeur
sinusoïdale en fonction du temps ; mesurer les durées et les vitesses à l'aide de photocapteurs.

**Page d'ouverture (p.275, image)** — photo de vagues, encart : « Les vagues constituent un exemple de propagation
d'ondes dans un milieu élastique. » Questions : « D'où provient l'énergie des vagues ? » · « Le déferlement des vagues
correspond-il à un déplacement de matière ou d'énergie ? » · « Nos oreilles perçoivent des sons. Qu'est-ce qui fait
qu'ils nous parviennent et pourquoi les sons émis etceux [sic] qu'on perçoit sont les mêmes ? »

**Plan (titres numérotés du manuel)** — introduction (caillou dans une nappe d'eau, p.276) · **1 Propagation d'un
ébranlement** (1.1 milieu unidimentionnel [sic], p.276–277 ; 1.2 milieu bidimentionnel, p.277–278 ; 1.3 milieu
tridimentionnel, p.278 ; conclusion p.279 ; 1.4 célérité d'un ébranlement, p.279–282) · **2 Propagation d'une onde
sinusoïdale entretenue** (2.1 généralités, p.282 ; 2.2 onde progressive le long d'une corde élastique tendue — étude
expérimentale p.283–286, étude théorique p.286–289 ; 2.3 onde sinusoïdale le long d'un ressort, p.289–290 ; 2.4 onde
sinusoïdale à la surface de l'eau, p.291–292 ; 2.5 le son, p.292–293) · L'essentiel (p.294) · Exercices : exercice
résolu (p.295–297) ; Tests rapides (ex. 1–2, p.298) ; Exercices d'application (ex. 3–6, p.299–300) ; Exercices de
synthèse (ex. 7–14, p.300–304) · Fiche technique N°1 (p.305) · Fiche technique N°2 (p.306) · En savoir plus
« L'énergie et la houle » (p.307).

### Cours — Activités

- **Introduction (p.276)** — « En jetant un caillou dans une nappe d'eau calme, on provoque une déformation de courte
  durée à la surface d'impact. […] Comment peut-on expliquer l'élargissement progressif de ces rides circulaires qui
  prennent naissance à la surface de l'eau suite au lancement du caillou ? »
- **1.1 Expérience 1 (p.276)** — longue corde élastique tendue horizontalement sur le sol, va-et-vient rapide imprimé
  à l'extrémité O ; Fig.1 (corde à t₀ = 0, t₁ > 0, t₂ > t₁, t₃ > t₂ ; bosse qui avance ; légende « Chaque point de la
  corde se soulève verticlament » [sic]).
- **1.1 Expérience 2 (p.276–277)** — premières spires non jointives d'un ressort tendu horizontalement, comprimées
  puis lâchées ; Fig.2 (ressort aux dates 0, t₁, t₂ ; repères a, P, b ; « Chaque spire du ressort se déplace
  horizontalement ; il en est de même pour l'ébranlement »). Questions : 1°) comparer la direction du déplacement de
  l'ébranlement à celle des points de la corde ; 2°) même comparaison pour les spires. Interprétation : chaque point
  « reproduit le mouvement de l'extrémité O avec un certain retard » ; corde → **transversal** ; ressort (élongation
  y selon l'axe) → **longitudinal**.
- **1.2 Manipulation (p.277–278)** — goutte d'eau sur la surface d'une cuve à ondes → ride circulaire (Fig.3 : cercles
  centrés en S à t₁, t₂ > t₁, t₃ > t₂ ; légende « Propagation d'ne [sic] ride circulaire ») ; morceau de liège en M :
  « petit déplacement vertical sur place, sans s'éloigner de sa position initiale ». Questions : 1°) transversal ou
  longitudinal ? 2°) dans combien de directions ? 3°) déplacement d'une quantité d'eau à partir de S ?
  Interprétation : propagation dans toutes les directions ; point repéré par (x, y) → deux dimensions ; « la
  propagation de ce dernier se fait avec une transmission d'énergie, sans déplacement de matière. C'est pour cette
  raison qu'il est impropre de parler de déplacement d'un ébranlement. »
- **1.3 Exemples (p.278)** — acteur chantant une note entendue au balcon, à l'avant de la scène, dans les coulisses ;
  petit poste radio sous une cloche où l'on crée le vide → son inaudible. Questions : 1°) ébranlement sonore
  transversal ou longitudinal ? 2°) le son se propage-t-il dans le vide ? Interprétation : « Les vibrations
  longitudinales des molécules de gaz (l'air par exemple) permettent la transmission du son depuis la source sonore
  jusqu'au tympan de l'oreille de l'auditeur. Dans le vide, le son ne peut pas se propager. »
- **1.4 Manipulation — échelle de perroquet (p.279–280)** — Fig.4 (photo), Fig.5 (fil de torsion vertical, barreaux,
  deux capteurs distants de d reliés à un « mesureur de vitesse ») ; masselottes à 2 cm de l'axe ; barreau supérieur
  tourné d'un angle α puis abandonné. Tableau 1 : d (m) 0,23 / 0,30 / 0,40 / 0,54 → v (m.s⁻¹) 0,48 / 0,49 / 0,48 /
  0,49 ; angle α' > α : valeurs « pratiquement les mêmes » ; masselottes déplacées symétriquement (inertie modifiée) :
  tableau 2 : d 0,23 / 0,30 / 0,40 / 0,54 → v 0,28 / 0,29 / 0,28 / 0,28. Questions (p.280) : 1°) montrer que les
  ébranlements se propagent dans ces milieux homogènes avec une célérité constante (avec l'expérience 1.2) ; 2°) la
  célérité dépend-elle a) de l'amplitude ; b) des caractéristiques du milieu ? Interprétation : célérité constante,
  indépendante de l'amplitude, dépendante de l'inertie. **Autres constatations (p.281)** : la célérité augmente avec
  la tension du fil de torsion ; la vitesse du son dépend de la compressibilité, « plus grande dans les solides que
  dans les liquides et les gaz » ; tableau des célérités (m.s⁻¹) : ébranlement à la surface de l'eau 0,3 ; le long
  d'une échelle de perroquet 1 ; le long d'une corde 10 ; sonore dans l'air à 20 °C 342 ; sonore dans l'eau à 20 °C
  1500 ; sonore dans l'acier 5000 ; sismique 8000. **Remarque — tableau « Déplacement d'un mobile » / « Propagation
  d'un ébranlement » (p.281–282)** : trajectoire bien précise / toutes les directions possibles à partir d'une
  source ; transport de matière / « Il ne correspond pas à un transport de matière mais d'énergie » ; ralenti par les
  frottements / « Dans un milieu matériel, un ébranlement peut être amorti, mais cet amortissement porte davantage sur
  son amplitude que sur sa célérité » ; plus facile dans le vide que dans un gaz…, impossible dans les solides /
  « Un ébranlement mécanique ne se propage pas dans le vide. Il se propage plus vite dans les liquides que dans les
  gaz et fréquemment plus vite dans les solides que dans les liquides. » ; vitesse dépendant des conditions
  initiales / « célérité qui dépend des propriétés du milieu de propagation ».
- **2.1 (p.282)** — houles, vagues, son, tremblements de terre = émission régulière d'ébranlements identiques ;
  définitions (Encadrés) ; milieux finis limités « par une matière absorbante (coton, feutre, plaque métallique cintrée
  …) afin de pouvoir les assimiler à des milieux ouverts ».
- **2.2 Mise en évidence (p.283)** — Fig.6 : lame vibrante (lame d'acier excitée par un électro-aimant alimenté en
  tension alternative sinusoïdale) – O – corde élastique – A – pelote de coton ; « bandelette rectangulaire floue de
  largeur double de l'amplitude de vibration de l'extrémité O » ; picotement au doigt. Questions : 1°) bandelette
  floue ? 2°) rôle de la pelote de coton ? 3°) justifier « onde transversale ».
- **2.2 Mouvement d'un point — analyse optique (p.283–284)** — Fig.7 : électro-aimant, lame vibrante, diaphragme au
  niveau de M, lentille L, source lumineuse, miroir tournant, écran (sinusoïde), extrémité fixe A. Questions : 1°) que
  représente la sinusoïde d'ombre ? 2°) comparer le mouvement d'un point à celui de O. Interprétation : chaque point
  (sauf A) reproduit le mouvement de O « avec la même amplitude et un certain retard ».
- **2.2 Aspect instantané — stroboscope (p.284–286)** — T_e = p.T (p ∈ ℕ*) → sinusoïde immobile de période D (Fig.8) ;
  T_e légèrement > p.T → mouvement apparent lent dans le sens réel ; légèrement < p.T → sens contraire. Questions :
  expliquer a) l'immobilité apparente, b) le mouvement apparent. Interprétation : pendant T_e chaque point fait p
  oscillations complètes ; « Tous les points équidistants de k.D (k ∈ N*) ont le même état de mouvement » ; D =
  longueur d'onde λ ; Fig.9a/9b (déplacement apparent MM', « Sens réel de la prorogation » [sic] / « Sens apparent de
  la prorogation »).
- **2.2 Étude théorique (p.286–289)** — repère (O, i⃗, j⃗), O = extrémité attachée au vibreur, M d'abscisse x (Fig.10).
  Questions intégrées : « Déterminer les abscisses des points de la corde vibrant en opposition de phase avec la
  source. » (p.288) · « Montrer que les points de la corde vibrant en quadrature retard de phase par rapport à la
  source sont définis par leur position de repos d'abscisse : x = (4k+1) λ/4, avec k ∈ N . » (p.288). Fig.11 : photo
  de la corde devant une règle.
- **2.3 Ressort (p.289–290)** — ressort à spires non jointives tendu verticalement par un solide suspendu, S attachée
  à un vibreur (période T), partie inférieure plongée dans un récipient d'eau (Fig.12, point A) ; lumière ordinaire :
  flou ; T_e = T : immobile, zones alternativement comprimées et dilatées ; T_e légèrement > T : progression lente de S
  vers A. Questions : 1°) but de l'immersion ; 2°) aspect en lumière ordinaire ; 3°) a) T_e = kT ; b) T_e légèrement
  < ou > kT ; 4°) nature de l'onde ; 5°) spires équidistantes ? Interprétation : non-équidistance ; onde
  **longitudinale** ; « Si y_s(t) = a sin (ωt), on montre qu'en absence de tout amortissement : y_M(t) = a sin(ωt −
  2πx/λ). »
- **2.4 Surface de l'eau (p.291–292)** — vibreur à fourche à pointe unique, cuve à ondes, point S, fréquence N ;
  stroboscope N_e : N_e = N → crêtes et creux circulaires concentriques immobiles (cercles brillants/sombres sur le
  verre dépoli, Fig.13 photo) ; N_e légèrement diminuée → rides qui paraissent progresser en s'éloignant de S.
  Questions : 1°) célérité la même dans toutes les directions ? 2°) montrer qualitativement que, frottement nul,
  l'amplitude diminue avec la distance à S. Étude théorique (Fig.14) ; remarque dilution, réglette (Fig.15) : voir
  Encadrés.
- **2.5 Le son (p.292–293)** — HP alimenté par un GBF, microphone (M) très sensible, voies Y₁ et Y₂ d'un oscilloscope
  bicourbe (Fig.16a photo) ; (C₁) membrane du HP, (C₂) membrane du micro, même fréquence N (Fig.16b) ; en approchant/
  éloignant le micro : amplitude qui augmente ou diminue, décalage horaire passant « régulièrement plusieurs fois de 0
  à T/2 » ; à distance r constante : (C₂) identique et stable. Questions : 1°) constatation montrant que le son est une
  onde tridimensionnelle ? 2°) transversale ou longitudinale ? 3°) variations d'amplitude de C₂ ? 4°) longueur de
  déplacement du micro pour que le décalage horaire varie de T/2 ?

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Ébranlement, milieu élastique (p.276, corps du texte)** — « La déformation de courte durée, imposée par le caillou
> à une nappe d'eau calme est un ébranlement. Etant un milieu élastique, la nappe d'eau joue le rôle de milieu de
> propagation de l'ébranlement. On appelle milieu élastique, tout milieu qui reprend de lui-même sa forme initiale
> après avoir subi une déformation brève. »

> **Conclusion 1.1–1.3 (p.279, encadré)** — « Un ébranlement est une déformation de courte durée imposée localement à
> un milieu élastique. Le milieu de propagation d'un ébranlement peut être unidimensionnel (corde élastique, ressort),
> bidimensionnel (surface d'un liquide) ou tridimensionnel (l'air ou tout autre fluide). Selon sa direction de
> propagation et celle du déplacement des points matériels du milieu de propagation, un ébranlement peut être
> transversal ou longitudinal. La propagation d'un ébranlement est due à une transmission d'énergie d'un point du
> milieu de propagation vers d'autres. »

> **Célérité (1.4, p.279, corps)** — « La propagation d'un ébranlement se fait avec une vitesse v appelée vitesse de
> propagation ou célérité de l'ébranlement. Du fait que cette propagation ne correspond pas à un déplacement de
> matière mais plutôt à un transport d'énergie, la célérité v correspond à une vitesse de propagation de l'énergie. »

> **Conclusion 1.4 (p.281, encadré)** — « La célérité d'un ébranlement dépend de la nature du milieu matériel dans
> lequel il se propage et de ses propriétés. Ainsi, le long d'une corde élastique, la célérité d'un ébranlement est
> d'autant plus grande que la corde est plus tendue. Plus l'inertie d'un milieu de propagation est grande, plus la
> célérité de l'ébranlement est faible... »

> **Onde (2.1, p.282, encadré « Définition »)** — « On appelle onde (du latin unda) le phénomène résultant de la
> propagation d'une succession d'ébranlements dans un milieu donné. » **Célérité d'une onde mécanique** — « Comme dans
> le cas d'un seul ébranlement, l'onde est caractérisée par une célérité v (ou vitesse de propagation) qui dépend des
> propriétés du milieu élastique homogène. Plus précisément, la célérité d'une onde est celle des ébranlements qui la
> constituent. » **Onde transversale et onde longitudinale** — « Le caractère transversal ou longitudinal d'une onde
> est fonction de celui des ébranlements correspondants. Les ébranlements transversaux constituent des ondes
> transversales et les ébranlements longitudinaux constituent des ondes longitudinales. » **Ondes progressives** —
> « Lorsque le milieu de propagation est ouvert, c'est-à-dire illimité, les ondes progressent en s'éloignant
> indéfiniment de la source. De telles ondes sont dites progressives. »

> **Conclusion (corde, p.284, encadré)** — « Les vibrations imposées à l'extrémité d'une corde élastique tendue sont
> transmises aux différents points de celle-ci. Le phénomène qui en résulte constitue une onde transversale. Au cours
> de la propagation d'une onde transversale sinusoïdale le long d'une corde élastique, chacun des points de cette corde
> (à part l'extrémité fixe A) vibre sinusoïdalement avec la même amplitude que la source (en négligeant
> l'amortissement). »

> **Double périodicité (p.286, encadré)** — « La propagation d'une onde est caractérisée par deux périodicités à la
> fois : - une périodicité dans le temps appelée périodicité temporelle. La période T est celle de la source. - une
> périodicité dans l'espace, appelée périodicité spatiale. La période spatiale λ, contrairement à la période T, ne
> dépend pas seulement de la source mais dépend aussi du milieu de propagation. La période spatiale λ est la longueur
> d'onde, elle représente la distance parcourue par l'onde pendant une durée égale à la période temporelle T.
> **λ = v.T , soit λ = v/N** En effet, la période temporelle T de l'onde est la durée au bout de laquelle l'onde se
> propage d'une longueur λ telle que tous les points du milieu de propagation se retrouvent dans le même état
> vibratoire, d'où le nom de longueur d'onde. »

> **Équation horaire d'un point de la corde (p.287)** — « A tout instant t, l'onde qui se propage le long de la corde
> impose au point M une élongation y(t) égale à l'élongation qu'a eue l'extrémité source S à l'instant ( t - θ ) ;
> l'amortissement étant supposé nul. La durée θ désigne le temps mis par l'onde pour se propager de S à M.
> y_M(t) = y_s(t − θ) or y_s(t) = a sin(ωt + φ_s). Avec un choix convenable de l'origine des temps, on aura φ_s = 0.
> y_s(t) = a sin(ωt), d'où y_M(t) = a sin ω(t − θ). θ = x/v ; v = célérité de l'onde et ω = 2π/T ; T : période de
> l'onde. Ainsi : y_M(t) = a sin[2π(t/T − x/vT)]. Or : λ = v.T : Longueur d'onde, d'où :
> **y_M(t) = a sin[2π(t/T − x/λ)]**. »

> **Conclusion (p.287, encadré)** — « Au cours de la propagation d'une onde sinusoïdale entretenue le long d'une corde
> élastique, tout point M de la corde, d'abscisse x par rapport à la source, vibre sinusoïdalement avec une période T
> égale à celle de la source S, mais avec une phase initiale dont la valeur est fonction de sa position sur la
> corde. » (sans le « , au repos » final que porte 223433 p.203.)

> **Déphasage par rapport à la source (p.287)** — « Si la source commence à vibrer à t=0 en allant dans le sens positif
> des élongations : y_s(t) = a sin(ωt) ; y_M(t) = a sin(ωt − 2πx/λ) de la forme y_M(t) = a sin(ωt + φ_M) avec
> **φ_M = − 2πx/λ**. Le déphasage entre les élongations y_M(t) et y_s(t) noté Δφ est (φ_M − φ_s) ; **Δφ = − 2πx/λ**. »
> Remarque : « Ce résultat reste valable dans le cas général où l'armortissement [sic] n'est pas négligeable et où la
> phase initiale n'est pas nulle. y_s(t) = a_O sin(ωt + φ_s) ; y_M(t) = a sin(ωt + φ_s − 2πx/λ) ; avec a < a_O. Ainsi
> Δφ est une fonction de l'abscisse x du point M par rapport à la source. »

> **Points en concordance de phase (p.288)** — « Un point M de la corde vibre en phase avec la source lorsque son
> élongation y_M(t) est liée à celle de la source par la relation : y_s(t)/a_s = y_M(t)/a, soit : sin(ωt + φ_s) =
> sin(ωt − 2πx/λ + φ_s) ∀t, ce qui donne φ_s = φ_M + 2kπ ; avec φ_M = − 2πx/λ + φ_s (k : entier), soit Δφ = − 2 kπ, ce
> qui conduit à : **x = kλ**, où k est un entier positif. Soit ℓ la longueur de la corde au repos. On a : x < ℓ. Donc,
> k < ℓ/λ. Les points de la corde qui vibrent en phase avec la source sont situés au repos à des distances égales à un
> nombre entier de longueurs d'onde la source S. Leur nombre est limité par la longueur de la corde. »

> **Points en quadrature avance de phase (p.288)** — « Un point M de la corde vibre en quadrature avance de phase la
> source lorsqu' à tout instant t, son élongation est telle que : y_s( t ) = y_M(t-T/4), soit : a sin(ωt+φ_s) =
> a sin[ω(t-T/4)+φ_M], ce qui donne φ_s = φ_M - π/2 +2k π, avec k un entier positif. D'où : Δφ = - (4k-1) π/2, ce qui
> conduit à : **x = (4k-1)λ /4**, avec k un entier positif. Les points de la corde qui vibrent en quadrature avance de
> phase par rapport à la source sont situés au repos à λ/4 **avant** les points qui vibrent en phase avec la source. »
> (223433 p.204 imprime « ayant » : coquille absente ici.)

> **Aspect de la corde à un instant t (p.289)** — « Pour un point M donné, à tout instant t : y_M(t) = a sin(ωt −
> 2πx/λ) dans le cas où φ_s = 0, ce qui entraîne qu'à un instant t donné, on peut écrire : pour tout point M,
> **y_t(x) = a sin(2πx/λ − ωt + π)**. Ainsi, pour t donné, y_t(x) est fonction sinusoïdale de x, de période λ et de
> phase initiale (- ωt + π). La courbe représentant y_t(x) donne l'aspect de la corde à un instant t considéré
> (Fig.11). Elle est appelée par certains "sinusoïde des espaces". » Remarque (front d'onde) : « Si les vibrations de la
> source commencent à t = 0 et que l'instant t choisi est de l'ordre de quelques périodes seulement, il se peut qu'à
> cet instant l'onde n'a pas atteint encore l'autre extrémité de la corde. Il faut alors chercher la position x_f du
> front d'onde. Pour ce, il suffit de calculer la distance parcourue par l'onde entre l'instant t = 0 et l'instant t
> choisi. **x_f = v.t** , ce qui équivaut : **x_f = n.λ**, en posant n = t / T. »

> **Surface de l'eau — étude théorique (p.292)** — « Le mouvement vibratoire de la pointe de la fourche, imposé au
> point S de la surface libre de l'eau donne naissance à une onde circulaire qui se propage à partir de S dans toutes
> les directions de la surface de l'eau, sous forme de rides superficielles, circulaires et transversales. Ainsi, tous
> les points de la surface d'eau situés à la même distance r du point S et qui constituent un cercle de centre S et de
> rayon r, ont à tout instant le même état de mouvement. Ils vibrent toujours en phase et avec la même amplitude.
> Suivant une direction passant par le centre S, les cercles concentriques, lieux des points vibrant en phase, sont
> équidistants de la longueur d'onde λ (Fig.14). » Remarques : « L'amplitude des ondes qui progressent à la surface de
> l'eau décroît en s'éloignant de la source même si l'amortissement est supposé nul. Cette décroissance est due au fait
> que l'énergie mécanique cédée à l'onde par la source de vibrations se répartit de proche en proche sur une quantité de
> liquide de plus en plus grande quand elle progresse à la surface de l'eau. C'est le phénomène de dilution
> d'énergie. » · « Si au lieu de la pointe, on utilise une réglette verticale […], il se formera des rides rectilignes
> parallèles à la réglette. Ces rides se propagent perpendiculairement à la réglette. La distance séparant deux rides
> consécutives est égale à la longueur d'onde λ (Fig.15). »

> **Conclusion (son, p.293, encadré)** — « Le son est de nature vibratoire. C'est une onde mécanique, appelée onde
> sonore et plus particulièrement acoustique lorsqu'elle est susceptible d'être perçue par l'oreille de l'homme. L'onde
> sonore émise par une source ponctuelle (approximation du haut-parleur) est une onde progressive sphérique mais qui
> s'atténue en s'éloignant de la source à cause de la dilution de l'énergie. »

**L'essentiel (p.294, VERBATIM)** — « ■ On appelle onde, le phénomène résultant de la propagation d'une succession
d'ébranlements dans un milieu donné. ■ Une onde est dite transversale si la direction des déformations auxquelles
elle est due est perpendiculaire à la direction de sa propagation. ■ Une onde est dite longitudinale si la direction
des déformations auxquelles elle est due est parallèle à la direction de sa propagation. ■ La propagation d'une onde
correspond à un transport d'énergie sans déplacement de matière. ■ La célérité (ou vitesse de propagation) d'une onde
dépend de la nature du milieu de propagation et de ses propriétés. ■ Toute onde se propageant dans un milieu ouvert
est progressive. Elle est caractérisée par une double périodicité spatiale et temporelle. ■ La période temporelle T de
l'onde est liée à la période spatiale λ par la relation : **λ = v.T** , avec v la célérité de l'onde. »

### Exercices résolus

**Exercice résolu (p.295–297)** — Énoncé : extrémité libre O d'une lame vibrant à N = 100 Hz ; corde élastique
l = 0,6 m ; onde progressive sinusoïdale transversale non amortie, a = 5 mm, phase initiale nulle, v = 12 m.s⁻¹.
« 1°) Etablir l'équation horaire de mouvement du point M de la corde situé au repos à x = 21 cm de la source et
comparer ses vibrations par rapport à celle de la source. 2°) Représenter dans le même système d'axes, les diagrammes
des mouvements de la source et du point M . 3°) Déterminer le lieu et le nombre des points de la corde vibrant en
quadrature avance de phase par rapport à la source. 4°) Représenter l'aspect de la corde à l'instant t₁ = 3,25.10⁻² s
et en déduire celui pris à l'instant t₂ = 3,75.10⁻² s. »
Solution : 1°) y_M(t) = y_O(t − θ), θ = x/v ; y_M(t) = a sin(ωt − 2πx/λ), φ = − 2πx/λ ; λ = v/N, A.N. λ = 12 cm,
φ = − 7π/2 = (− 4π + π/2) rad ; **y_M(t) = 5.10⁻³ sin(200πt + π/2)** : même amplitude, quadrature avance. 2°) M ne
vibre qu'à partir de t₁ = θ ; x = 7λ/4 → θ = 7T/4 = 1,75 T ; pour t < 7T/4, y_M = 0 ; pour t > 7T/4, y_M(t) =
a sin(ωt + π/2) ; diagramme de M = translation de θ (graphe source et M de 0 à 4T). 3°) Δφ = − 2πx/λ = − (4k − 1)π/2
→ **x = (4k − 1)λ/4** ; x ≤ l → k ≤ l/λ + 1/4 ; l/λ = 5 → k ≤ 5,25, k ∈ ℕ* → k ∈ {1, 2, 3, 4, 5} ; tableau x (cm)
9 / 21 / 33 / 45 / 57 (« le point M situé à x = 21 cm est bien l'un de ces cinq points »). 4°) x₁ = v t₁ = λ t₁/T,
t₁/T = 3,25 → x₁ = 3,25 λ < l = 5λ : front x_f1 ; pour x > x_f1, y_t1(x) = 0 (brin F₁A au repos) ; pour x < x_f1,
y_t1(x) = a sin(ωt₁ − 2πx/λ), ωt₁ = 6,5π rad → **y_t1(x) = a cos(2πx/λ)** ; graphe (p.297) de 0 à x_f1 = 3,25 λ, A à
l = 5λ [l'axe porte « 4λ » puis A/l]. Remarques : M (x = 1,75 λ) a y = 0 à t₁ = 3,25 T ; méthode rapide : extrapoler la
sinusoïde de période λ depuis le front jusqu'à la source. t₂ : (t₂ − t₁)/T = 1/2 → progression λ/2 ;
**x_f2 = x_f1 + λ/2** = 3,75 λ ; aspect à t₂ en trait plein, celui de t₁ en pointillés.

### Tests rapides des acquis

- **Ex. 1 — Vrai ou faux** (p.298, 10 items) : 1- une onde mécanique se propage dans le vide ; 2- un ébranlement
  mécanique transporte de l'énergie ; 3- la célérité d'un ébranlement mécanique ne dépend pas du milieu ; 4- une onde
  sonore peut se propager dans le vide ; 5- λ est la distance parcourue pendant T ; 6- la propagation d'une onde
  correspond à un déplacement de matière ; 7- en milieu homogène la célérité est constante ; 8- l'onde à la surface
  d'un liquide est transversale ; 9- l'onde sonore est longitudinale ; 10- « Le déplacement d'un mobile correspond à
  un déplacement de matière alors que le la [sic] propagation d'une onde correspond à un déplacement d'énergie. »
  (Pas de réponse.)
- **Ex. 2 — QCM** (p.298) : I- à tout phénomène ondulatoire est associé : a- un déplacement de matière / b- d'énergie /
  c- de matière et d'énergie ; II- vitesse de l'ébranlement (caillou dans l'eau) dépend de : a- l'énergie initiale du
  caillou / b- la taille du caillou / c- la profondeur de l'étendue d'eau ; III- corde OA, lame N = 100 Hz, dispositif
  anti-réflexion en A, stroboscope N_e = 49 Hz : sinusoïde a- fixe / b- lente de O vers A / c- lente de A vers O ;
  IV- N = 50 Hz, v = 0,25 m.s⁻¹ : distance entre deux points en phase : a- 5 mm / b- 10 mm / c- 15 mm. (Pas de
  réponse.)

### Exercices et problèmes

**Exercices d'application**
- **Ex. 3** (p.299) : y = a sin(100πt), v = 10 m.s⁻¹, amortissement nul. 1°) N et λ ; 2°) a) aspect à t₁ = 0,02 s et
  t₂ = 0,05 s (S part dans le sens positif à t = 0) ; b) état vibratoire de M₁ (d₁ = 10 cm) et M₂ (d₂ = 40 cm) ;
  3°) aspect sous stroboscope N_e = 25, 49, 51 Hz.
- **Ex. 4** (p.299) : N = 50 Hz, a = 0,5 cm, lame à l'équilibre partant vers le haut ; 1°) équation de S (verticale
  orientée vers le haut) ; 2°) v = 1 m.s⁻¹, pas de réflexion : a) équation de M à d ; b) d = 3 cm, comparer à S ;
  3°) courbes y_S(t), y_M(t) ; 4°) aspect à t₁ = 0,03 s et t₂ = 0,035 s.
- **Ex. 5** (p.299) : électroaimant, lame N = 100 Hz, a = 5 mm, corde très longue ; lame partant de l'équilibre dans
  le sens positif ; à t = 6,5.10⁻² s, M (x = 32,5 cm) entre en vibration. 1°) a) v ; b) λ ; 2°) (pas de réflexion)
  a) équation horaire de M ; b) graphe de 0 à 0,1 s ; c) instants d'élongation maximale, premier instant t₀.
- **Ex. 6** (p.300) : N = 50 Hz, source S, t₀ = 0, surface de l'eau ; coupe verticale passant par S à t₁ (sinusoïde de
  A à B, S au milieu, y_S(t₁) = 0) ; AB = 3,0 cm, amplitude 4 mm. 1°) λ ; 2°) v ; 3°) t₁ ; 4°) y_s(t) ; 5°) nombre de
  points en opposition de phase avec S à t₁, schéma avec sens du mouvement ; 6°) coupe à t₂ = 6,25.10⁻² s.

**Exercices de synthèse**
- **Ex. 7** (p.300) : cuve à ondes, source ponctuelle en O (a, N), bords absorbants « les ondes progressives provenant
  de S » [sic, O], pas d'amortissement ; Fig.1 (photo des rides, axe x'x, points B, A, O, distance d) ; 1°) a) rides
  apparemment immobiles ? b) d = AB = 24 mm (A, B sur deux crêtes) : λ ; 2°) Fig.2 : y_M(t) d'un point M à d' de O
  (échelles 2.10⁻³ m et 5.10⁻³ s) : a) y_M(t) ; b) v ; c) y_O(t) ; 3°) coupe selon x'x à t₀ = 0,045 s ; 4°) points en
  phase avec « la source S » à t₀.
- **Ex. 8** (p.301) : lame en S, corde sur la gorge d'une poulie + solide suspendu, dispositif absorbant ; repère
  (O, X, Y), O = S au repos (Fig.1) ; y_s(t) = a.sin(ω.t + φ), a = 3 mm, démarrage t₀ = 0. 1°) a) éclairage continu ;
  b) stroboscope N_e légèrement < N ; 2°) Fig.2 : aspect à t₁ = 0,025 s, front en A, x = OA = 0,75 m : a) λ, v, N ;
  b) équation de S ; c) y_A(t) ; d) allure de y_A(t).
- **Ex. 9** (p.301–302) : I- corde infinie, vibrations transversales à partir de t = 0, sans amortissement ; courbes
  (I) (diagramme d'un point A, 1 division → t = 2,5.10⁻³ s) et (II) (aspect à t₁, 1 division → x = 5 cm), amplitude
  4 mm lue. 1°) identifier, T, λ, a ; 2°) v, x_A, t₁ ; 3°) équations de S et A ; 4°) a) aspect à t₂ = 2,5.10⁻² s ;
  b) points d'élongation (− a/2) se déplaçant dans le sens négatif ; c) nombre et abscisses des points en quadrature
  retard. II- pointe S, point O de l'eau, y_O(t) = 10⁻³ sin(628 t) : 1°) y_M(t) (OM = x) ; 2°) v sachant que la plus
  petite distance entre 2 points en quadrature est d = 1 mm ; 3°) coupes à t₂ = 0,035 s et t₃ = 0,040 s ;
  4°) fréquence des éclairs pour l'immobilité, plus grande possible ; un éclair de moins par seconde → sens apparent.
- **Ex. 10** (p.302) : corde L = 2 m, tension et coton à l'extrémité ; lame partant de l'équilibre à t = 0 ; Fig.1 :
  y_M1(t) (Y_M en cm, ± 0,5 ; t en 10⁻² s ; démarrage vers 5,5) ; Fig.2 : aspect à t₀ (x en 10⁻¹ m ; front vers 5,5).
  1°) a) N et λ ; b) v ; c) x₁ et t₀ ; 2°) mouvements de S et M₁ ; 3°) instants où M₁ passe par 2,5.10⁻³ m dans le
  sens positif entre 0 et 0,14 s, plus petite valeur ; 4°) abscisses des points à 2,5.10⁻³ m allant dans le sens
  négatif à t₀.
- **Ex. 11** (p.302–303) : deux microphones M₁, M₂ sur l'axe d'un HP, d = 34 cm, N = 2000 Hz, v = 340 m.s⁻¹, écran
  10 × 8 divisions. 1°) a) base de temps pour 2 périodes ; b) amplitude voie 2 < voie 1 ? c) oscillogramme ;
  2°) a) N = 1 kHz, d = 17 cm : nouvel oscillogramme ; b) M₂ éloigné, oscillogramme analogue à 1° : d et base de
  temps.
- **Ex. 12 — Mesure de la célérité d'une onde sonore** (p.303) : M₁, M₂ sur Y_A, Y_B (Fig.1 : GBF, HP, règle,
  oscilloscope) ; 2 périodes sur 10 divisions, 0,4 ms/div ; abscisses successives en phase x₂ (cm) = 68,0 / 136,0 /
  204,0 / 272,0 / 340,0. 1°) fréquence ; 2°) λ ; 3°) v.
- **Ex. 13** (p.303) : HP et micro M (Fig.1) ; 1°) tensions visualisées ; 2°) fréquence (2 périodes, 10 divisions,
  0,2 ms/div) ; 3°) positions en phase x₁ = 4,5 cm et x₂ = 38,5 cm : λ ; 4°) v.
- **Ex. 14** (p.304) : GBF N = 1,47 kHz sur voie A, micro à d du HP sur voie B (Fig.1 schéma ; Fig.2 oscillogramme de
  deux sinusoïdes décalées, sans indication de réglages lisible). 1°) a) durée de balayage ; b) décalage θ, temps de
  propagation en fonction de θ et N ; 2°) k = 100 mV/div : amplitudes, pourquoi différentes ; 3°) d₂ − d₁ = 23,0 cm
  (deux positions successives en phase) : λ et v ; 4°) d entre 40 et 60 cm : valeur ; 5°) la célérité change-t-elle
  avec la fréquence ?

### Réponses du manuel (p.395, lues sur l'image)

- Ex. 3 : « 1°) N = 50Hz , λ = 0,2 m. 2°) b - M1 et S vibrent en opposition de phase, M2 et S vibrent en phase.
  3°) N_e = 25 Hz : immobilité ; N_e = 49 Hz: mouvement ralenti dans le sens réel ; N_e = 51 Hz mouvement ralenti dans
  le sens inverse. »
- Ex. 4 : « 1°) y_S(t) =5.10⁻³.sin100 πt . 2°) a) y_M(t) = 5.10⁻³.sin(100 πt -2 πd/λ), b) y_M(t) = 5.10⁻³.sin(100 πt
  -π). »
- Ex. 5 : « 1°) a) v = 5 m.s⁻¹. b) λ = 5.10⁻² m. 2°) a) y_M(t) = 2.10⁻³.sin(200 πt - π). c) t = 6,75.T +k.T. »
  [amplitude 2.10⁻³ m incohérente avec a = 5 mm de l'énoncé — même doute que dans 223433].
- Ex. 6 : « 1°) λ = 5.10⁻³ m, 2°) v=0,25 m.s⁻¹. 3°) t1 = 6.10⁻²s. 4°) y_S(t) = 4.10⁻³.sin(100 πt + π), 5°) Points sur
  les cercles de rayons : x1 = λ/2 ; x2 = 3λ/2 ; x3 = 5λ/2 . »
- Ex. 7 : « 1°) b- λ= 8.10⁻³ m. 2°)a) y_M(t) = 2.10⁻³.sin(100πt) b) v = 0,4 m.s⁻¹. c- y_o(t) = 2.10⁻³.sin(100πt + π).
  3°) Deux cercles de rayons x1 = λ et x2 = 2λ. 4°) a) λ = 0,3 m ; v = 30 m.s⁻¹ ; N = 100 Hz. b) y_S(t) =
  3.10⁻³.sin(200 πt). c) y_A(t) = 3.10⁻³.sin(200 πt -π) . » [le libellé « 8. » manque : la partie « 4°) a) … c) »
  répond en réalité à l'**ex. 8, 2°) a)–c)** (λ, v, N, y_S, y_A) ; l'ex. 7 n'a pas de 4°) chiffré].
- Ex. 9 : « I.1°)T = 0,01 s ; λ = 0,2 m. 2°) v =20 m.s⁻¹ ; x_A = 0,40 m ; t1 =0,02 s . 3°) y_S(t) =4.10⁻³.sin(200 πt) ;
  y_A(t) = 4.10⁻³.sin(200πt - π/2 ) [recadrage 250 dpi ; ? voir doutes] 4°)c) 3 points situés à x = 5λ/12 +kλ
  (k =0, 1, ou 2). II-1) y_M(t) = 10⁻³sin(628t - 2π.x /λ), 2°) v =0,4 m.s⁻¹. 4°) immobilité : N_e= N /k, pour k=1:
  N_e = N =100 Hz. »
- Ex. 10 : « 1°) a) N = 50 Hz ; λ = 0,2m. b) v = 10 m.s⁻¹. c) x1 = 0,55 m ; t_o = 0,055 s. 2°) S et M1 en quadrature
  de phase. 3°) t =(6,75.10⁻² +0,02k) s ; t1 =6,75.10⁻² s. 4°) 3 points situés à x = λ/8 + kλ,avec k =0, 1, ou2. »
- Ex. 11 : « 1°)a)10⁻⁴ s/div, b) dilution de l'énergie. 2°) b) d = 34 cm ; base te [sic] temps : 2.10⁻⁴s / div. »
- Ex. 12 : « 1°) N = 500 Hz. 2°) λ = 0,68 m, 3°) v = 340 m.s⁻¹. »
- Ex. 13 : « b) N = 1000 Hz, c) λ = 0,34 m. d) v =340 m.s⁻¹ » (étiquettes b, c, d pour 2°, 3°, 4°).
- Ex. 14 : « 1°) a) T≃ 68 ms, s ≃ 0,1ms/div. b) θ ≃ 0,15 ms ; Δt = n.T +θ = n / f +θ . 2°) U_R = 300 mV ;
  U_B = 250 mV. 3°) λ = d2 – d1 = 23 cm. v = λ.f = 338 m.s⁻¹. 4°) d = v. Δt = v (n / f + θ) = λ.n + λ.f.θ,
  d = 23.n + 5,1 (cm) ; d = 51,1 cm. 5°) Célérité constante, l'air est un milieu non dispersif. »
- Ex. 1, 2, 8 (sauf la partie mal libellée), et plusieurs sous-questions : pas de réponse.

### En savoir plus / Documents

- **Fiche technique N°1 « Méthode d'analyse optique d'un phénomène périodique » (p.305)** — corde « souple sans
  raideur » entre vibreur et support fixe ; diaphragme unifente F au niveau de M, faisceau parallèle ; ombre de M
  réfléchie par un miroir tournant à vitesse constante → sinusoïde sur l'écran (E) (Fig.1 = Fig.7 du cours).
- **Fiche technique N°2 « La stroboscopie » (p.306)** — stroboscope électronique (Fig.1 photo), éclairs de période T_e
  / fréquence N_e ; persistance rétinienne 0,1 s (intérêt au-delà de 10 Hz) ; disque blanc à pastille noire à
  20 tr.s⁻¹ éclairé à N_e = 20 Hz → immobile (Fig.2 : t = 0, T, 2T, 3T) ; « D'une façon générale : • Il y a
  immobilité apparente chaque fois que : T_e = k T (avec k un entier naturel) • Il y a un mouvement ralenti apparent :
  - dans le sens réel du mouvement si T_e est très légèrement supérieure à T (ou kT) - dans le sens contraire du
  mouvement réel si T_e est très légèrement inférieure à T (ou kT) ».
- **En savoir plus « L'énergie et la houle » (p.307, Encyclopédie « Science et Vie »)** — houle = succession de
  vagues régulières créées par le vent ; caractérisée par la hauteur H (m), la période T (s), la longueur d'onde λ ;
  « Une houle courte de période 3 secondes et de hauteur 0,6 mètres a une puissance de 1 kW. La puissance d'une houle
  longue avec H = 7,5 m et T = 11 s est à peu près 600 fois plus élevée » ; figure (trajectoires circulaires des
  particules, L et H) ; « Houlomotrices » ; énergie dégradée de l'énergie éolienne, se propage loin sans trop de
  perte ; potentiel en France 30 kW/m (sites exposés), 10 à 20 kW/m ailleurs ; projet en Espagne ; pas encore de
  « winning technology ». Lecture culturelle (lien avec la question d'accroche sur l'énergie des vagues).

### Écart avec la référence (sciences-exp/07 Ondes mécaniques progressives — correspondance CONFIRMÉE)

Le cours (titres, manipulations, encadrés, L'essentiel), l'exercice résolu et les **ex. 1 à 14** sont identiques
mot pour mot à ceux du manuel 223433 (ch.7, p.192–221) ; le chapitre publié peut être repris presque tel quel.
- ⛔ **À retirer** (présent dans 223433 / dans le chapitre publié, absent ici) :
  - **Ex. 15** de 223433 (source ponctuelle, coupe de la surface à t₁ = 0,2 s, y_s = Y_m sin(2πNt + π)) et **ex. 16
    « Quand la Terre tremble… »** (ondes sismiques P et S, compression/cisaillement, sujet de bac 2009) : **absents**
    de 223471 (les exercices s'arrêtent à l'ex. 14, p.304). Le chapitre publié `07-ondes-mecaniques-progressives`
    mentionne les ondes P/S à trois endroits, à retirer ou à reformuler sans ondes P/S : `quiz.json` (item « secousse de
    cisaillement sismique (onde S) »), `cours.md` l.87 (ligne de tableau « Séisme, onde S | cisaillement … |
    transversale ») et `resume.md` l.4 (« … surface de l'eau, onde S) … ressort comprimé, son, onde P) »). (La ligne « Ebranlement sismique
    8000 m.s⁻¹ » du tableau de célérités reste, elle, présente p.281.)
  - « En savoir plus » de 223433 (propriétés des ondes, vitesses de phase et de groupe, vecteur d'onde, Fourier) :
    remplacé ici par la houle ; s'il a nourri le chapitre publié, retirer.
  - Page d'ouverture de partie « Ondes » (houle, tsunami, Grand Nuage de Magellan…) : absente.
- ✅ **À ajouter / autrement** :
  - « En savoir plus » **« L'énergie et la houle »** (H, T, λ, puissances 1 kW / ×600, houlomotrices, 10–30 kW/m) —
    lecture culturelle facultative.
  - p.288 : « à λ/4 **avant** les points qui vibrent en phase » (texte correct ici, « ayant » dans 223433).
  - Conclusion p.287 sans « au repos » (nuance mineure).
- Vocabulaire et notations : identiques **à 223433** (θ, φ_s, Δφ, T_e/N_e, x_f, « sinusoïde des espaces », « dilution
  d'énergie ») ; coquilles identiques. Mais **pas identiques au chapitre publié** : celui-ci écrit la quadrature avance
  x = (4k + 3)λ/4 (cours.md l.304) et l'aspect y_t(x) = a sin(ωt − 2πx/λ) (cours.md l.328), alors que le manuel écrit
  x = (4k − 1)λ/4 avec k ≥ 1 (p.288) et y_t(x) = a sin(2πx/λ − ωt + π) (p.289) ; formes équivalentes, mais l'adaptation
  doit reprendre celles du manuel 223471 (exercice résolu, tableau k = 1…5). Numérotation du chapitre : **10** (au lieu de 7) ; pages 274–307.

### Bornes de scope

- ✅ **INCLUS** (identique à la fiche sciences-exp §2.7, moins les ondes sismiques P/S) : ébranlement, milieu élastique,
  milieux uni-/bi-/tridimensionnels ; transversal / longitudinal (corde, ressort, eau, son) ; transport d'énergie sans
  transport de matière ; pas de propagation mécanique dans le vide ; célérité constante en milieu homogène,
  indépendante de l'amplitude, dépendante du milieu (tension, inertie, compressibilité ; ordres de grandeur du tableau
  p.281) ; mobile vs ébranlement ; onde, onde entretenue, onde progressive, matière absorbante ; double périodicité,
  **λ = v.T = v/N** ; **y_M(t) = y_s(t − θ), θ = x/v, y_M(t) = a sin(ωt + φ_s − 2πx/λ), Δφ = − 2πx/λ** ; points en
  phase (x = kλ), en opposition (question), en quadrature avance (x = (4k − 1)λ/4) et retard (x = (4k + 1)λ/4) et leur
  dénombrement ; diagramme du mouvement d'un point (translation de θ) ; aspect y_t(x) = a sin(2πx/λ − ωt + π), front
  d'onde x_f = v.t = n.λ, aspect à t₂ déduit de t₁ ; coupe de la surface de l'eau (rides circulaires / rectilignes) ;
  dilution d'énergie ; son = onde progressive sphérique ; stroboscopie (T_e = kT, N_e = N/k ; ralenti sens réel /
  inverse) ; analyse optique ; mesure de λ et v du son par positions successives en phase ; lecture d'oscillogrammes
  (base de temps, décalage θ, Δt = nT + θ) ; air non dispersif (réponse ex. 14).
- ⛔ **EXCLU** : ondes sismiques P et S (étude de texte de 223433 absente ici) ; réflexion, ondes stationnaires,
  interférences, diffraction, dispersion (chapitre 11) ; formule quantitative de la célérité (v = √(F/μ)…) ; vitesse de
  phase/groupe, vecteur d'onde, Fourier ; énergie transportée calculée, intensité sonore, décibels, effet Doppler ;
  puissance de la houle (lecture seulement).

### Lecture

- **Pages lues en couche texte** : 274 à 307 (les 34 pages) et 395 (réponses du chapitre 10).
- **Pages lues sur l'image** (110 dpi) : 274, 275, 276, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
  290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 395 (**34 pages**) ;
  recadrage 250 dpi : p.395 (réponse ex. 9 I-3°). Page 278 relue sur l'image après relecture R-7 (conforme) : les
  34 pages 274–307 sont toutes vues sur l'image.
- **Comparaison avec la fiche sciences-exp §2.7** : chaque encadré et chaque énoncé d'exercice ci-dessus a été relu sur
  l'image de 223471 et confronté à la transcription de 223433 : texte identique, sauf les deux nuances signalées
  (p.287 « au repos » absent ; p.288 « avant » au lieu de « ayant »).
- **Écarts couche texte / image** : formules de p.274 (prérequis), 287–289, 295–296 inutilisables en texte (ω, θ, φ, π,
  λ, fractions perdus : « yM (t ) = a sin(t  ) », « Δ = - (4k - 1) ») ; à la différence de 223433 p.213, la couche
  texte de p.297 contient les étiquettes des graphes ; p.300 colonnes de l'ex. 6 et de l'ex. 7 entremêlées (« B A O »
  de la Fig.1 de l'ex. 7 placé près de l'ex. 6) ; figures des ex. 9, 10, 14 (sinusoïdes, échelles) seulement
  partiellement en texte ; p.395 « T≃ », « θ ≃ » rendus « b ».
- **Coquilles [sic]** : « etceux » (p.275) ; « unidimentionnel », « bidimentionnel », « tridimentionnel » (p.276–278) ;
  « verticlament » (Fig.1) ; « d'ne ride » (Fig.3) ; « dispostion », « echelle » (Fig.5) ; « prorogation » (Fig.9a/9b) ;
  « instante t » (p.285) ; « armortissement » (p.287) ; « Dispositf » (Fig.12) ; « rectlilignes » (Fig.15) ;
  « le la propagation » (ex. 1-10) ; « tl » pour t₁ (ex. 4) ; « provenant de S » (ex. 7, source en O) ; « sembleraient »
  correct ici ; « base te temps » (réponse ex. 11) ; libellé « 8. » manquant dans les réponses (p.395).
- **Doutes [?]** :
  1. **Réponse ex. 5** : amplitude 2.10⁻³ m au lieu de 5.10⁻³ m (a = 5 mm dans l'énoncé). 2. **Réponse ex. 14 1°a** : « T ≃ 68 ms » pour N = 1,47 kHz (T ≈ 0,68 ms) ; la question porte sur la durée de
     balayage — valeur fautive ou mal libellée. 3. **Réponses ex. 7 / ex. 8** fusionnées sous « 7. » (voir ci-dessus) ; à réattribuer. 4. **Réponse ex. 9 I-3°** : imprimé « y_A(t) = 4.10⁻³.sin(200πt − π/2) » (recadrage 250 dpi, lecture sûre) ; or
     x_A = 0,40 m = 2λ donne Δφ = −4π, donc A en phase avec S (la fiche sciences-exp transcrit pour 223433
     « y_S = y_A = 4.10⁻³ sin(200πt) ») : la réponse de 223471 est fautive — ne pas la reprendre. 5. QCM III : réponse non fournie (règle T_e légèrement > 2T → ralenti dans le sens réel, O → A). 6. Ex. 14 : l'oscillogramme Fig.2 ne porte aucune indication de base de temps ; les réponses 1°) supposent
     s ≃ 0,1 ms/div non donnée dans l'énoncé.

## 2.11 Chapitre 11 — Interactions onde-matière (manuel 223471, p.308–337)

Partie du manuel : « Ondes » (bandeau « Ondes • Interactions onde - matière » sur chaque page). Plage exacte
vérifiée : **p.308** (Objectifs / Prérequis, page précédant l'ouverture ; bandeau « Ondes • Interactions onde -
matière ») → p.309 (page d'ouverture n° 11) → p.337 (« En savoir plus »). La p.307 est la fin du chapitre 10.
**La p.338 n'appartient PAS au chapitre 11** : c'est la page « Objectifs / Prérequis » du chapitre 12 (bandeau
« Généralités sur la transmission des signaux »), placée avant la page d'ouverture n° 12 (p.339).
Notations du manuel : la fréquence d'une radiation est notée **ν** (lettre nu en italique, rendue « V »/« Vx »
en couche texte), celle d'une onde mécanique **N** ; « tg » pour tangente ; angle d'incidence i / i₁, de
réflexion i' ou r, de réfraction i₂.

**Objectifs (p.308, VERBATIM)** — « Justifier le caractère ondulatoire de la lumière à partir d'expériences de
diffraction d'ondes mécaniques et d'ondes lumineuses. » · « Préciser l'influence, sur le phénomène de diffraction,
du quotient λ/a (λ étant la longueur d'onde et a la largeur de la fente). » · « Réaliser des expériences de
réflexion, de réfraction et de dispersion d'ondes mécaniques. » · « Montrer que la lumière blanche est constituée
d'une infinité de radiations monochromatiques. » · « Distinguer un milieu dispersif d'un milieu non dispersif. »

**Prérequis (p.308)** — SAVOIR : définir une onde mécanique rectiligne ; définir la réflexion et la réfraction de
la lumière ; énoncer les lois de Descartes relatives à la réflexion et à la réfraction de la lumière ; définir le
phénomène de dispersion de la lumière blanche. SAVOIR FAIRE : reconnaître une onde mécanique rectiligne ;
utiliser un stroboscope ; mesurer la longueur d'onde λ d'une onde plane progressive ; utiliser une source Laser ;
« Appliquer le [sic] lois de Descartes relatives à la réflexion et à la réfraction de la lumière » ; reconnaître
le phénomène de dispersion de la lumière blanche.

**Page d'ouverture (p.309)** — titre « INTERACTIONS ONDE-MATIERE », n° 11 ; photo de soleil à travers un arbre,
légende (VERBATIM) : « Les rayons solaires donnent, à travers les branches d'arbres, une lumière diffusée dans
toutes les directions. » Questions d'accroche (VERBATIM) : « Qu'est-ce qui fait que le son puisse contourner
les corps de dimensions habituelles ? » · « Comment une chauve-souris peut-elle détecter un papillon nocturne
dans l'obscurité totale ? » · « Comment un papillon nocturne peut-il neutraliser le système de détection d'une
chauve-souris ? »

**Introduction (p.310, VERBATIM)** — « On a vu que lorsque le milieu de propagation est ouvert, toute onde
mécanique qui s'y propage est progressive. Dans ce chapitre, on se propose d'étudier le comportement d'une
telle onde à la rencontre d'un obstacle ou au niveau d'une fente très petite. On traitera aussi le cas d'un
faisceau lumineux qui passe à travers une fente fine. »

**Plan (titres numérotés du manuel)** —
1 LA DIFFRACTION (p.310) : 1.1 Diffraction d'une onde mécanique (p.310–311) · 1.2 Diffraction de la lumière
(p.311–313, avec « Caractéristiques d'une onde lumineuse ») · 1.3 Influence du quotient (λ/a) sur le phénomène
de diffraction (p.313–316 : cas de l'onde mécanique ; cas de l'onde lumineuse, 1ʳᵉ et 2ᵉ étapes).
2 LA REFLEXION (p.316) : 2.1 Réflexion d'un ébranlement (p.316–317) · 2.2 Réflexion d'une onde (p.318–320 :
cas d'une onde plane ; cas d'une onde sphérique [sic : l'expérience utilise une onde sonore « sensiblement
unidirectionnelle »]).
3 LA REFRACTION D'UNE ONDE MECANIQUE (p.320) : 3.1 L'onde transmise (p.320–321) · 3.2 L'onde réfractée
(p.321–323).
4 LA DISPERSION (p.324) : 4.1 Dispersion de la lumière (p.324–325) · 4.2 Dispersion des ondes mécaniques
(p.325–326) · 4.3 Milieu dispersif et milieu non dispersif (p.327–328).
Puis « L'essentiel » (p.329), « Exercices » : exercice résolu (p.330–331), « Exercices à résoudre » (p.332–336),
« En savoir plus » (p.337). Pas de fiche technique.

### Cours — Activités (manipulations, dans l'ordre du manuel)

- **§1.1 Diffraction d'une onde mécanique (p.310–311)** — cuve à ondes, lame vibrante L (onde plane), deux
  plaques de plexiglas à distance d de L formant une ouverture F de largeur a (Fig.1). Observations : a = 4 cm →
  rides rectilignes légèrement déformées aux bords (Fig.2a « Absence de diffraction … pour a > λ ») ; a = 1,5 cm
  → rides circulaires dans une zone triangulaire de sommet I milieu de la fente (Fig.2b « Diffraction pour
  a ≃ λ ») ; a = 0,5 cm → rides quasi circulaires de centre I (Fig.2c « Diffraction pour a < λ »). Questions
  (VERBATIM) : « 1°) Quelle est la nature de l'onde incidente sur l'ouverture F ? 2°) Quelle est l'observation
  qui montre qu'il émerge de l'ouverture F une onde différente de l'onde incidente ? Préciser cette différence.
  3°) Par comparaison des distances entre deux rides consécutives rectilignes et deux rides consécutives
  circulaires, comparer les longueurs d'onde, λ de l'onde incidente et λ' de l'onde émergente. 4°) Comparer
  dans chacun des cas, la longueur d'onde λ à la largeur a de l'ouverture F. » Remarque : un obstacle de même
  largeur donne le même phénomène (Fig.3, photo).
- **§1.2 Diffraction de la lumière (p.311–313)** — laser rouge λ = 633 nm, écran E à distance d (Fig.4a :
  schéma laser → écran, tache ponctuelle ; puis laser → « Obstacle » → faisceau élargi → figure de taches,
  largeur L de la tache centrale). Diaphragme à fente rectangulaire F de largeur réglable : a = 0,6 mm → figure
  étalée horizontalement, taches brillantes séparées de zones sombres, tache centrale de largeur L la plus
  brillante ; a = 0,3 mm → tache centrale L' = 2 L (Fig.4b, photo). Remarques : obstacle de même largeur → même
  phénomène ; fente circulaire → « anneaux de diffraction » (Fig.4c, photo, légendée « Figure de diffraction par un
  trou »). Questions (VERBATIM) : « 1°)
  Comparer la largeur a de la fente (F) donnant sur (E) la figure étalée avec la valeur de λ. 2°) Les taches
  lumineuses formées sur l'écran E ont-elles la même largeur ? 3°) Comment se présentent les taches latérales
  par rapport à la tache centrale ? 4°) La forme de la fente a-t-elle un effet sur la nature des taches
  lumineuses qui se forment sur l'écran ? 5°) Le principe de propagation rectiligne de la lumière permet-il
  d'expliquer le phénomène observé ? » Interprétation : figure de diffraction, tache centrale de largeur L,
  taches latérales, zones sombres, « franges de diffraction » ; L augmente quand a diminue ; la figure a les
  symétries de la fente (rectangulaire ou circulaire).
- **§1.3 Influence de λ/a — onde mécanique (p.313–314)** — montage Fig.1, N constante, a = 1,5 cm ; épaisseur
  d'eau e₁ → rides circulaires dans une zone triangulaire (Fig.5a « a ≃ λ ») ; e₂ = 3.e₁ → rides quasi
  circulaires de centre I (Fig.5b « a < λ »). Questions (VERBATIM) : « 1°) Préciser la variation de la longueur
  d'onde λ de l'onde progressive incidente en fonction de la profondeur e du milieu de propagation. 2°)
  Comparer, pour chaque valeur de e, la valeur de la longueur d'onde λ à celle de la largeur a de la fente.
  3°) Préciser les facteurs qui peuvent influer sur le phénomène de diffraction. » Interprétation : λ augmente
  avec la profondeur ; diffraction d'autant plus marquée que λ est grande (a fixe).
- **§1.3 Influence de λ/a — onde lumineuse (p.314–316)** — montage Fig.4a, écran à **D = 2 m**, papier
  millimétré (Fig.6a photo ; Fig.6b « Définition de la demi-largeur angulaire θ de la raie centrale » : fente en
  I, angle θ entre l'axe et le bord de la tache, L sur l'écran). L = distance entre les milieux des bandes
  sombres qui entourent la tache centrale. **Tableau 1 (laser rouge λR)** :

  | a (10⁻³ m) | 0,10 | 0,14 | 0,20 | 0,25 |
  |---|---|---|---|---|
  | 1/a (10³ m) [sic, lire 10³ m⁻¹] | 10,0 | 7,1 | 5,0 | 4,0 |
  | L (10⁻³ m) | 25 | 18 | 12 | 10 |

  **Tableau 2 (laser vert λV, « source laser argon-ion »)** : mêmes a et 1/a ; L (10⁻³ m) = 21 ; 15 ; 10 ; 8.
  Fig.7 : deux droites passant par l'origine, L (10⁻³ m, 0–24) en fonction de 1/a (10³ m, 0–10), rouge
  au-dessus du vert. Questions (VERBATIM) : « 1°) La largeur a de la fente a-t-elle une influence sur la
  largeur L de la tache centrale de diffraction ? 2°) Par exploitation des courbes de la figure 7, donner une
  relation simple entre L et a. 3°) A partir de la figure 6b, montrer que l'angle θ correspondant à la
  demi-largeur angulaire de la raie centrale est donné par la relation : θ = L/2.D. 4°) Préciser la variation de
  L et par suite celle de θ en fonction de la longueur d'onde λ. » Interprétation et relations : voir Encadrés.
- **§2.1 Réflexion d'un ébranlement (p.316–317)** — ondoscope d'extrémités A et B ; ébranlement d'amplitude a
  (une torsion) en A. B libre (Fig.8a : bosse vers le haut A→B, puis bosse vers le haut B→A) ; B fixe (Fig.8b :
  bosse vers le haut A→B, puis bosse vers le bas B→A). Questions (VERBATIM) : « 1°) Expliquer l'apparition des
  ébranlements qui se propagent de B vers A. 2°) Dans les deux expériences précédentes, comparer l'ébranlement
  se propageant de A vers B et celui se propageant de B vers A : a) en amplitude, b) en direction et sens du
  déplacement, c) en signe de l'élongation. » Interprétation : ébranlement incident (1), ébranlement réfléchi
  (2) ; amplitude comparable ; même sens de déformation à une extrémité libre, sens contraire à une extrémité
  fixe.
- **§2.2 Réflexion d'une onde plane (p.318–319)** — cuve à ondes, lame L, plaque de plastique triangulaire P
  partiellement immergée (Fig.9a) ; rides rectilignes parallèles à L auxquelles se superposent des rides
  rectilignes de direction située de l'autre côté de la normale à P (Fig.9b : S, I, N, R ; Fig.9c : λ incident,
  λ' réfléchi, normale IN, rayon IR). Questions (VERBATIM) : « 1°) La plaque P absorbe-t-elle les ondes émises
  par L ? 2°) Préciser sur le schéma de la figure 9b, l'onde incidente et l'onde réfléchie. 3°) La réflexion
  d'une onde plane sur un obstacle plan se fait-elle avec la modification de sa longueur d'onde λ ? 4°) Mesurer
  l'angle d'incidence i = (SI, IN) que fait la direction de l'onde incidente avec la normale à P et le comparer
  à l'angle de réflexion i'= (RI, IN) que fait la direction de l'onde réfléchie avec la normale à P. »
- **§2.2 Réflexion d'une onde sonore (« Cas d'une onde sphérique », p.319–320)** — émetteur E (haut-parleur)
  relié à un GBF délivrant « un signal de haute fréquence » (onde sonore sensiblement unidirectionnelle),
  récepteur R (microphone) relié à un oscilloscope, plaque de polystyrène = écran absorbant, obstacle plan
  (côté lisse) (Fig.10). i = (EI, IN) fixé à 30° ; on fait varier i' = (RI, IN) et on relève l'amplitude U :

  | i' (degrés) | 0 | 5 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 55 | 60 | 70 | 80 | 90 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Amplitude (mV) | 0.48 | 0.60 | 0.78 | 0.84 | 0.90 | 0.92 | 0.89 | 0.85 | 0.78 | 0.59 | 0.49 | 0.38 | 0.16 | 0.10 |

  (pas de colonne 10°, 50°, 65°, 75°, 85° : tableau tel quel.) Remarque (VERBATIM) : « Pour limiter le
  phénomène de diffraction, il faut travailler avec des fréquences de l'ordre du mégahertz. » Questions
  (VERBATIM) : « 1°) La présence de l'obstacle modifie-t-elle la direction de propagation de l'onde sonore
  incidente ? 2°) Quelle est la forme de l'onde sonore reçue par R ? Justifier la réponse. 3°) Pour quelle
  valeur de i', l'amplitude de l'onde captée est-elle maximale ? ce résultat est-il prévisible ? 4°) Comment
  peut-on éviter le phénomène de diffraction dans cette expérience ? » Interprétation : amplitude maximale
  pour i' = i (30°).
- **§3.1 L'onde transmise (p.320–321)** — cuve à ondes, lame L, plaque rectangulaire de plexiglas P posée au
  fond du côté opposé à L (Fig.11) : deux milieux d'épaisseurs e₁ > e₂ ; surface de séparation notée σ ;
  éclairage stroboscopique Ne = N : deux séries de rides immobiles rectilignes équidistantes, plus serrées dans
  le milieu 2 (Fig.12, photo). Questions (VERBATIM) : « 1°) L'onde progressive incidente, émise par L, subit-elle
  un changement lors de son passage du milieu 1 vers le milieu 2 ? Si oui, lequel ? 2°) La profondeur du milieu
  de propagation a-t-elle un effet sur la célérité v de l'onde ? 3°) Comparer les longueurs d'onde, des ondes se
  propageant dans les deux milieux ? » Interprétation : λ₂ < λ₁ ; célérité la plus grande dans la zone la plus
  profonde.
- **§3.2 L'onde réfractée (p.321–323)** — même dispositif avec une plaque trapézoïdale : surface de séparation
  plane faisant un angle non nul avec L ; milieu 1 : rides parallèles à L ; milieu 2 : rides plus serrées et de
  direction différente ; cassure des rides à la surface de séparation (Fig.13a, flèches 1 et 2). Questions
  (VERBATIM) : « 1°) La direction de la surface de séparation des deux milieux a-t-elle un effet sur la
  direction de propagation de l'onde incidente qui est transmise du milieu 1 au milieu 2 ? 2°) L'onde transmise
  du milieu 1 au milieu 2 subit-elle une modification de longueur d'onde ? 3°) Mesurer l'angle que fait la
  direction de propagation de l'onde incidente (milieu 1) avec la normale à la surface de séparation des deux
  milieux, le comparer à celui que fait la direction de propagation de l'onde transmise (milieu 2) avec la même
  normale à la surface de séparation des deux milieux. » Démonstration géométrique (Fig.13b : I, I', H, H',
  normale N'N, λ₁, λ₂, i₁, i₂) : voir Encadrés.
- **§4.1 Dispersion de la lumière (p.324–325)** — laser He-Ne, prisme en verre d'indice n, écran E à distance d :
  déviation D du faisceau et déplacement de la tache (Fig.14). Questions (VERBATIM) : « 1°) Comment peut-on
  interpréter la déviation D du faisceau lumineux qui traverse le prisme ? 2°) Le principe de propagation
  rectiligne de la lumière est-il vérifié ? 3°) Rappeler les lois de Descartes pour la réfraction. » Puis
  source de lumière blanche, fente F, lentille convergente, prisme, écran (dans cet ordre) : spectre coloré
  bordé de rouge et de violet (Fig.15, photo « Spectre visible de la lumière blanche »). Questions (VERBATIM) :
  « 1°) Un faisceau de lumière blanche subit-il une déviation à la traversée du prisme ? 2°) Quelle est la
  source de ces différentes couleurs qui se forment sur l'écran E ? 3°) Peut-on caractériser la lumière blanche
  par une longueur d'onde λ ? » Interprétation : « double réfraction air/verre/air » ; spectre continu.
- **§4.2 Dispersion des ondes mécaniques (p.325–326)** — cuve à ondes, lame L, stroboscope Ne = N : rides
  immobiles ; on fait varier N commune au stroboscope et à la lame :

  | N (Hz) | 10 | 20 | 30 |
  |---|---|---|---|
  | λ (10⁻³ m) | 21 | 11 | 8 |
  | V (m.s⁻¹) | 0,21 | 0,22 | 0,24 |

  (cohérent : v = λN.) Questions (VERBATIM) : « 1°) Observe-t-on un changement de la nature de l'onde qui
  progresse à la surface de l'eau quand on change la fréquence N de la source ? 2°) La nature du milieu de
  propagation des ondes est-elle modifiée par la variation de la fréquence N de la source d'ondes ? 3°) La
  célérité d'une onde à la surface de l'eau est-elle indépendante de sa fréquence ? » Exemple du bateau
  (VERBATIM) : « Un bateau provoque une perturbation comprenant plusieurs ondes sinusoïdales de fréquences
  différentes sur une eau calme. Un observateur sur le rivage verra d'abord arriver des vagues très espacées
  (grandes longueurs d'onde) puis ensuite des vagues moins espacées. Ainsi, les différentes ondes sinusoïdales
  se propagent dans le même milieu avec des célérités différentes, les plus rapides se détachent à l'avant de
  la perturbation. »
- **§4.3 Milieu dispersif et non dispersif (p.327–328)** — dispositif du §4.1 avec filtres (rouge, jaune, vert …
  bleu), même incidence i : angle de déviation D par filtre (Fig.16 : prisme, rayons rouge, vert, bleu ; le
  bleu le plus dévié). Questions (VERBATIM) : « 1°) La déviation d'une radiation lumineuse par un prisme
  dépend-t-elle de son indice de réfraction n ? 2°) Sous le même angle d'incidence i, les différentes
  radiations de la lumière blanche sont-t-elles déviées du même angle ? 3°) Préciser la radiation la plus
  déviée par le prisme. » Tableau (p.327) :

  | Couleur de la lumière | ν (10¹⁴ Hz) | λ (10⁻⁶ m) | Indice n |
  |---|---|---|---|
  | Bleu sombre | 6,92 | 0,433 | 1,528 |
  | Bleu vert | 6,18 | 0,485 | 1,520 |
  | Jaune | 5,10 | 0,588 | 1,517 |
  | Rouge | 4,57 | 0,656 | 1,514 |
  | Rouge sombre | 3,91 | 0,767 | 1,511 |

  Remarque (p.328, VERBATIM) : « D'après ce tableau, on peut dire que l'indice de réfraction du verre est
  d'environ 1,5 dans tout le domaine visible, car sa dispersion produit une augmentation de (0,006) pour chaque
  diminution de dix picomètres (10 pm) de la longueur d'onde. » [? voir Lecture, doute 4]

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Interprétation (§1.1, p.311)** — « A son passage à travers la fente F, l'onde rectiligne de longueur
> d'onde λ se transforme en une onde circulaire de même longueur d'onde. Cette transformation qui se produit
> lorsque la largeur a de la fente F est inférieure à la longueur d'onde λ de l'onde incidente, est le
> phénomène de diffraction. L'onde qui en résulte est appelée onde diffractée. »

> **Conclusion (§1.1, p.311)** — « Au niveau d'une fente ou d'un obstacle de largeur a de même ordre de
> grandeur que sa longueur d'onde λ, l'onde mécanique subit le phénomène de diffraction. La diffraction est la
> modification du trajet d'une onde et par suite de sa forme, au voisinage d'une fente ou d'un obstacle. En
> subissant la diffraction, une onde initialement plane se propage après franchissement de la fente ou de
> l'obstacle, suivant plusieurs directions situées de part et d'autre de la direction d'incidence. »

> **Conclusion (§1.2, p.313)** — « Au niveau d'une fente fine ou d'un obstacle de largeur a très petite, un
> faisceau de lumière (lumière rouge par exemple, émise par une source laser) subit le phénomène de
> diffraction. La forme étalée de la figure de diffraction ne peut être expliquée par le principe de
> propagation rectiligne de la lumière. Par rapprochement avec la diffraction d'une onde mécanique, la
> propagation de la lumière dans un milieu transparent ou dans le vide peut être considérée comme étant la
> propagation d'une onde appelée onde lumineuse. »

> **Caractéristiques d'une onde lumineuse (p.313)** — « - Comme l'onde mécanique, l'onde lumineuse, est
> caractérisée par une période temporelle T et une période spatiale λ. - Dans le vide, toutes les ondes
> lumineuses se propagent à la célérité **c = 3.10⁸ m.s⁻¹**. La relation entre λ et T s'écrit :
> **λ_vide = c.T.** » Remarque : « La célérité des ondes lumineuses dans l'air est assimilée avec une bonne
> approximation à leur célérité dans le vide. »

> **Conclusion (§1.3 onde mécanique, p.314)** — « Une onde plane rectiligne, de longueur d'onde λ, qui se
> propage à la surface d'un liquide et qui traverse une fente F de largeur a ne subit pas une déformation
> appréciable tant que la valeur de a est très grande devant λ. Par conséquent, le phénomène de la diffraction
> est imperceptible. Cependant, pour des valeurs de a comparables ou très faibles par rapport à λ, le
> phénomène de diffraction est appréciable. Ainsi le phénomène de diffraction dépend du quotient **λ/a**. »

> **Interprétation (§1.3 onde lumineuse, p.315–316)** — « - La largeur L de la tache centrale ainsi que la
> demi-largeur angulaire θ de la raie centrale dépendent de la largeur a de la fente F. Par la suite, L et a
> sont inversement proportionnelles : **L = k.(1/a) (1)**, avec K [sic, k] une constante positive.
> L'exploitation de la figure 6b, nous permet d'écrire : **tg(θ) = L/2.D, d'où θ ≈ L/2.D (2)**, car D est
> grande devant la largeur L de la tache centrale. Exploitation des courbes de la figure 7 : - Pour une valeur
> fixe de a, la largeur L de la tache centrale dépend de la longueur d'onde λ de la source d'éclairement. En
> effet, sachant que λR et [sic, est] plus grande que λV d'après l'étude expérimentale d'une part et que LR est
> plus grande que LV d'autre part. Par conséquent, L = f(λ). - Des relations (1) et (2), on peut déduire
> [sic] : **θ = k/2.D.a (3)**. L'exploitation des courbes de la figure 7 nous permet de justifier que :
> **θr.a/λrouge = θv.a/λvert ≈ 1, et par la suite θ = λ/a (4)**. - A l'aide des relations (2) et (4), on peut
> exprimer L sous la forme : **L = 2.D.λ/a (5)** »

> **Conclusion (§1.3, p.316)** — « Une onde mécanique ou lumineuse subit une diffraction à la rencontre d'une
> fente fine de largeur a ou au niveau d'un obstacle dont les dimensions sont convenables. Cependant, la
> perception du phénomène de diffraction de l'onde dépend du quotient (λ/a). »

> **Interprétation (§2.1, p.317)** — « L'apparition d'un ébranlement (2) se propageant de l'extrémité B de
> l'ondoscope vers son extrémité A dès que l'ébranlement (1) créé en A atteint B s'explique par la réflexion de
> cet ébranlement (1) au niveau de B, d'où la qualification d'ébranlement réfléchi pour l'ébranlement (2) et
> d'ébranlement incident pour l'ébranlement (1). Un ébranlement réfléchi est caractérisé par : - une amplitude
> comparable à celle de l'ébranlement incident. - le même sens de déformation que celui de l'ébranlement
> incident lorsqu'il apparaît au niveau d'une extrémité libre et un sens de déformation contraire à celui de
> l'ébranlement incident quand il se manifeste au niveau d'une extrémité fixe. »

> **Conclusion (§2.1, p.317)** — « Un ébranlement incident, d'amplitude a, subit une réflexion au niveau d'une
> extrémité du milieu de propagation et donne lieu à un ébranlement réfléchi. La réflexion d'un ébranlement sur
> une extrémité libre se fait avec la même amplitude a et sans changement de signe. Par contre, sur une
> extrémité fixe, la réflexion d'un ébranlement se fait avec un changement de signe. »

> **Conclusion (§2.2 onde plane, p.319)** — « Une onde incidente progressive plane, d'angle d'incidence i, de
> longueur d'onde λ qui se propage dans un milieu de propagation, subit une réflexion au niveau d'un obstacle
> plan (plaque de plastique...) et donne naissance à une onde progressive plane réfléchie de longueur d'onde λ'
> et d'angle de réflexion i' tels que : **λ = λ' et i = i'**. Ce résultat nous rappelle la deuxième loi de
> Descartes, relative à la réflexion d'un rayon lumineux qui tombe sur un miroir plan sous une incidence i. »

> **Conclusion (§2.2 onde sonore, p.320)** — « Une onde sonore subit une réflexion à la rencontre d'un obstacle
> réfléchissant de grande dimension et donne naissance à une onde réfléchie. En chaque point d'incidence, on
> peut vérifier les lois de Descartes pour la réflexion. Ainsi, l'angle d'incidence i de l'onde sonore est égal
> à son angle de réflexion i'. Les dimensions de l'obstacle doivent être très supérieures à la longueur d'onde
> dans l'air de l'onde sonore incidente. Dans le cas contraire, l'onde incidente contourne l'obstacle et c'est
> le phénomène de diffraction qui aura lieu. »

> **Conclusion (§3.1, p.321)** — « Le passage d'une onde progressive d'un milieu vers un autre se produit avec
> changement de célérité mais sans changement de direction lorsque cette onde arrive à la surface de séparation
> des deux milieux de propagation suivant une direction perpendiculaire à cette surface. On dit qu'il s'agit
> d'une simple transmission. L'onde est dite alors onde transmise. »

> **Démonstration (§3.2, p.323)** — « NIN' est la normale à la surface de séparation des deux milieux. i₁ et i₂
> sont respectivement l'angle d'incidence et l'angle de réfraction. Dans le triangle HII' : II'.sin(HII') = λ₁.
> Autrement : **II'sin(i₁) = λ₁ (1)**. Dans le triangle H'II' : II'.sin(H'II') = λ₂. Autrement :
> **II'sin(i₂) = λ₂ (2)**. le rapport des relations (1) et (2) membre à membre donne : **λ₁/λ₂ =
> sin(i₁)/sin(i₂) (3)**. La relatrion [sic] (3) peut s'écrire : **λ₁.sin(i₂) = λ₂.sin(i₁) (4)**. En remplaçant λ₁
> par v₁.T et λ₂ par v₂.T, on obtient **sin(i₁)/v₁ = sin(i₂)/v₂**. Ainsi, on retouve [sic] la seconde loi de
> Descartes relative à la réfraction. »

> **Conclusion (§3.2, p.323)** — « Au niveau de la surface de séparation de deux milieux de propagation, l'onde
> mécanique subit un changement de direction de propagation : c'est le phénomène de réfraction. La réfraction
> d'une onde mécanique se fait avec un changement de sa longueur d'onde λ. La réfraction d'une onde mécanique
> est régie par la relation de Descartes : **λ₁ sin(i₂) = λ₂.sin(i₁)**. Où : λ₁ et λ₂ sont respectivement les
> longueurs d'onde de l'onde incidente et de l'onde réfléchie [sic, lire réfractée] ; i₁ et i₂ sont
> respectivement l'angle d'incidence et l'angle de réflexion [sic, lire réfraction]. »

> **Conclusion (§4.1, p.325)** — « La lumière blanche résulte de la superposition d'une infinité de lumières de
> couleurs différentes allant du rouge au violet. Ainsi, la lumière blanche est appelée lumière polychromatique
> car elle est constituée de plusieurs, voire une infinité de lumières colorées ou radiations. Chaque radiation
> est caractérisée par une fréquence ν et une longueur d'onde dans le vide λ₀. Une lumière constituée d'une
> seule radiation est appelée lumière monochromatique. Les différentes radiations constituant la lumière
> blanche ne sont pas déviées du même angle D par un prisme d'indice n, c'est le phénomène de dispersion de la
> lumière. Ainsi, la déviation d'une radiation lumineuse monochromatique par un prisme d'indice n, dépend de sa
> fréquence ν. »

> **Conclusion (§4.2, p.326)** — « Quand la célérité v d'une onde mécanique dans un milieu de propagation donné
> ne dépend pas uniquement de la nature de ce milieu, mais dépend aussi de sa fréquence N, on dit qu'il s'agit
> du phénomène de dispersion d'onde mécanique. »

> **Interprétation (§4.3, p.327)** — « […] Ainsi, le bleu est plus dévié que le rouge et le vert. La lumière
> est ainsi dispersée par le prisme. La dispersion de la lumière blanche est due au fait que l'indice n de
> réfraction du prisme n'est pas constant, et qu'il augmente en passant de la lumière rouge à la lumière
> bleue. Le prisme dans ce cas est un milieu dispersif. »

> **Conclusion (§4.3, p.328)** — « Chaque radiation lumineuse monochromatique de fréquence ν est caractérisée
> par une longueur d'onde dans le vide **λ₀ = c/ν**. En pénétrant dans un milieu transparent d'indice n, où la
> célérité de la lumière est **v = c/n**, sa longueur d'onde devient **λ = v/ν = c/n.ν = λ₀/n**. Le phénomène de
> dispersion de la lumière est la variation de sa célérité v dans un milieu transparent d'indice n, en fonction
> de sa fréquence ν. Ainsi, la déviation d'une radiation lumineuse monochromatique par un prisme en verre
> d'indice n dépend de sa fréquence ν. Tout milieu transparent d'indice de réfraction n, où la célérité d'une
> radiation lumineuse dépend de sa fréquence est appelé milieu dispersif. Le verre est un exemple de milieu
> dispersif. »

> **Définition générale (p.328, hors encadré)** — « En général, tant pour les ondes mécaniques que pour les
> ondes lumineuses, on appellera milieu dispersif pour une onde de fréquence N (ou ν) tout milieu où la
> célérité v de cette onde ne dépend pas uniquement des propriétés du milieu de propagation, mais dépend aussi
> de la fréquence N (ou ν) de l'onde. Dans le cas contraire où la célérité v de l'onde est indépendante de la
> fréquence N (ou ν), le milieu est dit non dispersif. » Remarque : « L'air est un exemple de milieu non
> dispersif pour les ondes sonores. En effet, des ondes sonores de fréquences différentes se propagent dans
> l'air avec la même célérité. Par conséquent, deux notes de musique de hauteurs différentes émises
> simultanément par deux instruments sont perçues par l'auditeur au même instant. »

**L'essentiel (p.329, VERBATIM)** — « ■ La diffraction d'une onde est la modification de son trajet et par
suite sa forme au voisinage d'une ouverture ou d'un obstacle de dimensions comparables à sa longueur d'onde.
■ La diffraction d'une onde se fait sans changement de sa longueur d'onde. ■ Un faisceau de lumière est décrit
comme étant une onde appelée onde lumineuse. ■ Le phénomène de diffraction dépend du quotient λ/a, λ étant la
longueur d'onde et a l'ouverture de la fente. ■ Une lumière monochromatique est une onde progressive
sinusoïdale caractérisée par sa fréquence ν et sa longueur d'onde λ₀ dans le vide. ■ Une lumière
polychromatique est constituée de plusieurs radiations. ■ La lumière blanche est une lumière polychromatique.
■ Une onde mécanique, comme une onde lumineuse, peut subir le phénomène de réflexion à la rencontre d'un
obstacle plan. ■ La réfraction d'une onde mécanique est le changement de sa longueur d'onde et de sa direction
de propagation, au niveau de la surface de séparation de deux milieux de propagation. ■ Le phénomène de
dispersion de la lumière est la variation de sa célérité v dans un milieu transparent d'indice n, en fonction
de sa fréquence ν. ■ On appelle milieu dispersif tout milieu dans lequel la célérité v d'une onde périodique
dépend de sa fréquence. » (L'essentiel ne reprend ni θ = λ/a ni L = 2Dλ/a, ni la relation de Descartes
λ₁ sin i₂ = λ₂ sin i₁.)

### Exercices résolus

**Exercice résolu (p.330–331)** — Énoncé : lumière monochromatique λ, fente rectangulaire de largeur a
réglable, écran à **D = 3 m** ; tableau a (mm) 0,10 ; 0,14 ; 0,20 ; 0,25 — L (mm) 31,5 ; 22,5 ; 16,0 ; 12,5.
« 1°) Décrire brièvement la figure de diffraction formée sur l'écran E. 2°) Tracer la courbe représentant L en
fonction de 1/a et calculer sa pente. 3°) Donner la relation entre la largeur L de la tache centrale et la
longueur d'onde λ. 4°) Déterminer la valeur de la longueur d'onde λ de la lumière utilisée. 5°) En remplaçant
la fente par un cheveu de diamètre d, la largeur de la tache centrale qui se forme sur l'écran devient
L' = 1,5 cm. Calculer de deux manières le diamètre d du cheveu. »
Solution : 1°) figure étalée horizontalement, tache centrale brillante de largeur L, taches latérales séparées
par des zones sombres (Fig.1, photo). 2°) droite passant par l'origine (graphe L (10⁻³ m) 0–35 vs 1/a
(10³ m⁻¹) 0–10) : **L = k/a = 3,15.10⁻⁶/a (1)** (unité de k non écrite ; m²). 3°) **L = 2.λD/a (2)**. 4°) par
identification 2.λ.D = k → **λ = k/2D** ; A.N. **λ = 525.10⁻⁹ m**. 5°) première méthode : L' = 2.λD/d →
**d = 2.λ.D/L'** ; A.N. **d = 0,21.10⁻³ m, soit d = 0,21 mm** ; deuxième méthode : lire sur la courbe
L = f(1/a) l'abscisse (1/d) correspondant à L' = 1,5 cm (lecture non faite dans le manuel).

### Tests rapides des acquis (p.332)

- **Ex. 1 — Vrai ou faux** : 1- La diffraction n'a pas d'influence sur la longueur d'onde λ de l'onde incidente ;
  2- passage d'un milieu à un autre → changement de fréquence ; 3- « On ne peut pas obtenir d'ondes réfléchies à
  partir d'ondes circulaires » ; 4- la direction d'une onde plane est modifiée chaque fois qu'elle rencontre un
  obstacle ; 5- la diffraction de la lumière met en évidence l'impossibilité d'isoler un rayon lumineux ; 6- la
  célérité de la lumière est indépendante de la nature du milieu ; 7- la réflexion d'un ébranlement à
  l'extrémité libre d'une corde élastique se fait avec changement du signe ; 8- l'eau est un milieu dispersif
  pour les ondes lumineuses. (Réponses non fournies.)
- **Ex. 2 — QCM** : I. diffraction observée pour : a- λ/a > 1 / b- **λ/a² = 1** [sic, imprimé a² — coquille
  probable pour λ/a ≈ 1] / c- λ/a < 1 ; II. L liée au « demi-diamètre apparent » : a- θ = L/D / b- θ = L/2D /
  c- θ = D/2L (D distance fente-écran) ; III. relation entre L (tache centrale) et L' (tache latérale) :
  a- L = 2.L' / b- L = L' / c- L = L'/2 ; IV. dans un milieu dispersif, la célérité est fonction uniquement de :
  a- la fréquence / b- la nature du milieu / c- la fréquence et la nature du milieu ; V. indice : a- n = c/v /
  b- n = v/c / c- n = c.v ; VI. radiation λ₀ entrant dans un milieu d'indice n : changement de a- sa fréquence /
  b- sa longueur d'onde / c- sa couleur. (Réponses non fournies.)

### Exercices et problèmes (p.333–336) — 14 exercices au total (2 tests + 6 application + 6 synthèse)

**Exercices d'application**
- **Ex. 3** (p.333) : onde rectiligne en cuve, obstacle à α = 30° de la direction de propagation, distance entre
  deux crêtes d = 4,0 cm, N = 12,5 Hz. 1°) angle d'incidence i ; 2°) célérité ; 3°) schéma de l'onde réfléchie,
  i et r.
- **Ex. 4** (p.333) : digue de largeur l = 30 m [ouverture dans la digue sur la Fig.2] séparant une baie de la
  mer ; vagues parallèles à la digue, λ = 80 m. 1°) propagation au-delà ; 2°) schéma ; 3°) phénomène ; 4°) vagues
  de λ = 5 m.
- **Ex. 5** (p.333) : plaque de verre délimitant deux zones (z₁), (z₂) (Fig.3, séparation oblique), vibreur S₁S₂,
  N = 40 Hz, v₁ = 36 cm.s⁻¹. 1°) changement à la séparation, phénomène ; 2°) v₂ = 29 cm.s⁻¹ → λ₂ ; 3°) représenter
  l'onde transmise.
- **Ex. 6** (p.333–334) : cuve partagée par une plaque de plexiglas, e₁ = 2,5 cm, e₂ = 1,5 cm (Fig.4), séparation
  parallèle à L. 1°) a) changement ? b) phénomène ; 2°) **v = √(‖g‖.e)** [imprimé ainsi, norme de g], N = 25 Hz,
  ‖g‖ = 10 m.s⁻² : a) λ₁ et λ₂ ; b) comparer ; 3°) allure en lumière stroboscopique Ne = N ; 4°) l'eau est-elle
  un milieu dispersif pour les ondes mécaniques ?
- **Ex. 7** (p.334) : v₁ = 0,30 m.s⁻¹, v₂ = 0,25 m.s⁻¹, vibreur 20 Hz, i₁ = 30°. 1°) λ₁ ; 2°) λ₂ ; 3°) i₂ par la
  seconde loi de Descartes ; 4°) schéma sans réflexion. [? réponses incohérentes avec ces données, voir
  Lecture]
- **Ex. 8** (p.334) : faisceau monochromatique λ, prisme d'indice n, incidence i (Fig.5 : rayon incident sur un
  prisme triangulaire, écran E oblique). 1°) définir l'indice ; 2°) lois pour la marche du faisceau émergent ;
  3°) tracer ; 4°) observation sur E, phénomène ; 5°) lumière blanche.

**Exercices de synthèse**
- **Ex. 9** (p.334) : fente a réglable, λ = 0.63 μm, D = 1 m, **L = 2.D.λ/a** donné. 1°) lumière
  monochromatique ; 2°) a = 0.1 mm : a) décrire, b) justifier en comparant L à a ; 3°) L' pour λb = 0.46 μm ;
  4°) pourquoi plus facile avec le rouge ; 5°) a = 2 mm : observable ?
- **Ex. 10** (p.335) : laser λ, fente a, écran perpendiculaire. 1°) relation λ/a pour observer ; 2°) schéma de
  la figure ; 3°) définir θ ; 4°) relation θ, L, D ; 5°) L en fonction de D, a, λ ; 6°) λ pour a = 60 μm,
  L = 4,2 cm, D = 2,0 m.
- **Ex. 11** (p.335) : fente **circulaire** de diamètre a, D = 4.5 m, rayon r de la tache centrale ; tableau
  a (10⁻⁴ m) 4,9 ; 6,2 ; 8,2 ; 12,0 — r (10⁻³ m) 7,5 ; 6,0 ; 4,5 ; 3,0. 1°) r = f(1/a) ; 2°) équation ;
  3°) relation D, r, θ ; 4°) donné **θ = 1,22.λ/a**, montrer **r = 1,22 λ.D/a** ; 5°) λ.
- **Ex. 12** (p.335) : figure de diffraction (Fig.5) à D = 2 m, fente a = 100 μm ; cotes x₁ = 2,7 cm (tache
  centrale), x₂ = 5,5 cm, x₃ = 8 cm. 1°) schéma du dispositif ; 2°) relation X₁ – demi-diamètre angulaire θ ;
  3°) relation θ, λ, a ; 4°) λ ; 5°) comparer tache centrale et tache latérale ; 6°) largeur pour λ = 450 nm.
- **Ex. 13** (p.335–336) : faisceau monochromatique, i = 30°, face plane d'un hémicylindre en plexiglas (Fig.6 :
  S, I, N). 1°) lois de Descartes ; 2°) r_j pour n_j = 1,485 (jaune) ; 3°) montrer D = i_j − r_j ; 4°) r_B pour
  n_B = 1,520 (bleu) ; 5°) lumière jaune + bleue : marche, angle entre les rayons, phénomène.
- **Ex. 14 — Étude de texte « Les ondes sonores dans une pièce vide »** (p.336) : diffraction prépondérante si
  λ du son ~ dimensions des objets, masque la réflexion ; pièce vide qui « résonne » ; meubles de l'ordre du
  mètre ; tissus, tapis, tentures. Questions : 1°) cas où la diffraction serait appréciable dans une pièce
  meublée ; 2°) atténuer la « résonance » ; 3°) effet du tissu ; 4°) éviter la réflexion dans un amphithéâtre.

### Réponses du manuel (p.396, colonne « Chapitre 11 », vérifiées sur l'image)

Ex. 3 : 1°) 60°, 2°) 0,50 m.s⁻¹, 3°) r = 60°. · Ex. 4 : 1°) λ>>l, 2°) rides circulaires, 3°) diffraction,
4°) l<< λ [sic : pour λ = 5 m on a l >> λ], pas de diffraction. · Ex. 5 : 1°) oui, 2°) λ₂ = v₂/N₂ = v₁/N₂ [sic]
= 7,25.10⁻³ m. · Ex. 6 : 1°) a) Oui, b) transmission avec changement de célérité, 2°) a) λ₁ = v₂/N [sic, v₁]
= 2.10⁻² m, λ₂ = v₂/N = 1,5.10⁻² m, b) λ₂ < λ₁, 4°) non, car v₂ ≠ v₁, pour N = Cte [sic : raisonnement
contestable, voir doutes]. · Ex. 7 : 1°) λ₁ = v₁/N = 2.10⁻² m, 2°) λ₂ = v₂/N = 1,33.10⁻² m, 3°) sin(i₂) =
v₂ sin(i₁)/v₁ ce qui donne i₂ = 19,47°. · Ex. 8 : 1°) n = c/v, 2°) sin(i₁) = n.sin(i₂), 4°) une tache, 5°) oui,
on obtient le spectre de la lumière blanche. · Ex. 9 : 1°) Une seule radiation, 2°) a) Tache centrale de
largeur L, b) λ/a = 6,3.10⁻⁶ < 0,174 [sic/?], 2°) [3°] L' = 9,2.10⁻³ m, 4°) L' < L, 5°) L = 0,63.10⁻³ m, on
mesure difficilement L. · Ex. 10 : 1°) θ = λ/a, 4°) θ = L/2D, 5°) L = 2λ.D/a, 6°) λ = L.a/2D, λ = 0,63 μm. ·
Ex. 11 : 1°) Une droite, 2°) r = k/a = 36,7.10⁻⁷/a, 4°) θ = 1,22.λ/a, θ = r/a [sic, r/D], r = 1,22.λD/a,
5°) λ = 0,67 μm. · Ex. 12 : 2°) θ₁ = X₁/2D, 3°) θ₁ = λ/a, 4°) λ = a.X₁/2D = 0,675 μm, 5°) L₁ = 2,7.10⁻² m,
L₂ = 1,4.10⁻² m, L₁ = 2L₂, 6°) X₁ = 2λ.D/a = 1,8.10⁻² m. · Ex. 13 : 1°) n₁sin(i₁) = n₂sin(i₂), 2°) sin(r_j) =
sin(i)/n_j, r_j = 19,67°, 2°) [3°] i_j > r_j par la suite D = i_j – r_j = 10,3°. 4°) r_b = 19,2° et D' = 10,8°,
ainsi la radiation bleue est la plus déviée, la dispersion de la lumière. · Pas de réponse : Ex. 1, 2, 14.

### En savoir plus / Documents

- **« L'interprétation du phénomène de diffraction avec la théorie des ondelettes » (p.337)** — surface d'onde
  Σt ; chaque point de Σt source secondaire émettant une ondelette circulaire de célérité v ; sources
  secondaires synchrones ; à t+T superposition → Σt+T (Fig.1) ; diffraction : ondelettes issues de F de rayon
  v.T (Fig.2) ; a << λ → Σt+T pratiquement circulaire, F assimilée à une source secondaire unique (Fig.3).
  Encadré biographique : Christian Huygens (1629-1695), « Traité de la lumière » (1678).
- Pas de fiche technique. Les questions d'accroche (chauve-souris, papillon) ne reçoivent aucune réponse dans
  le chapitre (l'écholocation n'est pas traitée).

### Écart avec la référence (physique-bac-sciences-exp/08-nature-ondulatoire-lumiere, + 07 pour la réflexion)

Correspondance **confirmée mais partielle** : sciences-exp/08 (« Nature ondulatoire de la lumière », manuel
223433 p.226–243) couvre les §1 (diffraction) et §4.1/4.3 (dispersion de la lumière, milieu dispersif) de ce
chapitre. Les §2 (réflexion), §3 (réfraction d'une onde mécanique) et §4.2 (dispersion des ondes mécaniques)
n'ont **aucun équivalent** publié (sciences-exp/07 exclut explicitement la réflexion : fiche sciences-exp
l.3276 ; à vérifier dans `07-ondes-mecaniques-progressives/cours.md`, qui n'a aucune section réflexion).
Interférences : **absentes des deux manuels** (le brief les citait avec « ? » : à écarter).

- ⛔ (dans la référence, absent ici) : aucun écart notionnel majeur sur la partie commune. Points à vérifier à
  l'adaptation : exemples chiffrés de la référence (N = 20 Hz, v = 0,24 m/s, fente 3,6/1,2/0,6 cm ; hémicylindre
  de verre à i = 60° avec n_rouge = 1,514, n_bleu = 1,528) — à remplacer par les données de CE manuel (a = 4 / 1,5 / 0,5 cm ; λ = 633 nm,
  a = 0,6/0,3 mm ; tableaux 1 et 2 à D = 2 m ; tableau ν/λ/n identique). L'étalement « perpendiculaire à la
  fente » est formulé ici « figure étalée horizontalement » ; le fil/cheveu n'apparaît ici qu'en exercice
  résolu (cheveu) et en remarque « obstacle de même largeur ».
- ✅ (en plus ici, à ajouter) :
  - **Établissement expérimental des relations de diffraction AU COURS** (p.315–316). La référence publiée
    (sciences-exp/08, section « 📏 La largeur L, l'angle θ et la distance D ») contient DÉJÀ θ = L/(2D) comme
    définition et L = 2λD/a « admise ici comme outil de calcul » (exemple chiffré, piège θ = L/D). Reste à
    ajouter : L = k/a tiré des droites L = f(1/a) pour deux couleurs (tableaux 1 et 2) ; tg θ = L/2D, θ ≈ L/2D ;
    θ = k/2Da ; puis **θ = λ/a** (absent tel quel de la référence) ; L = 2Dλ/a présentée comme conséquence et
    non plus admise. Calculs de λ, de d (cheveu), de L' pour une autre λ : déjà couverts par la référence. En
    exercice : fente circulaire **θ = 1,22 λ/a**, r = 1,22 λD/a (ex. 11, formule donnée).
  - **Réflexion** (§2) : ébranlement sur ondoscope, extrémité libre (sans changement de signe) / fixe (avec
    changement de signe), ébranlement incident/réfléchi ; onde plane en cuve sur obstacle plan : λ' = λ, i = i'
    (deuxième loi de Descartes) ; onde sonore sur obstacle plan (tableau i'/amplitude, maximum pour i' = i) ;
    condition « obstacle >> λ » sinon diffraction.
  - **Réfraction d'une onde mécanique** (§3) : transmission simple (incidence normale, changement de célérité
    et de λ, célérité plus grande en eau profonde) ; onde réfractée (incidence oblique) ; démonstration
    géométrique **λ₁ sin i₂ = λ₂ sin i₁** ⇔ **sin i₁/v₁ = sin i₂/v₂** ; exercices : v = √(g.e) (ex. 6), calcul de
    i₂ (ex. 7).
  - **Dispersion des ondes mécaniques** (§4.2) : tableau N/λ/v en cuve, l'eau dispersive pour les ondes de
    surface, exemple du bateau ; définition générale du milieu dispersif (N ou ν) ; l'air non dispersif pour le
    son (deux notes perçues en même temps).
  - Huygens (ondelettes) en « En savoir plus » (même statut de lecture que dans la référence).
- Vocabulaire / notations propres : « ondoscope », « ébranlement réfléchi/incident », « simple transmission »,
  « onde transmise », « onde réfractée », surface de séparation « σ », « demi-largeur angulaire θ de la raie
  centrale » (et « demi-diamètre apparent/angulaire » en exercices), « franges de diffraction », « anneaux de
  diffraction », « tg », ν pour les radiations et N pour les ondes mécaniques, r ou i' pour l'angle de
  réflexion.

### Bornes de scope

- ✅ **INCLUS** :
  - Diffraction d'une onde mécanique (fente, obstacle ; onde diffractée de même λ ; cas a > λ, a ≃ λ, a < λ) ;
    influence de λ via la profondeur d'eau ; dépendance au quotient λ/a.
  - Diffraction de la lumière (laser, fente rectangulaire, obstacle, trou → anneaux) ; description de la
    figure ; mise en défaut de la propagation rectiligne ; onde lumineuse : T, λ, c = 3.10⁸ m.s⁻¹,
    λ_vide = c.T ; air ≈ vide.
  - Tache centrale : L (entre milieux des bandes sombres), θ ; L = k/a ; θ ≈ L/2D ; θ = λ/a ; L = 2Dλ/a ;
    exploitation de tableaux/graphes L = f(1/a) ; calcul de λ, a, d (cheveu), L pour une autre couleur ;
    tache latérale de largeur moitié (ex. 12, QCM III) ; fente circulaire θ = 1,22 λ/a (en exercice, formule
    fournie).
  - Réflexion d'un ébranlement (extrémité libre / fixe, signe) ; réflexion d'une onde plane (λ' = λ, i = i') et
    d'une onde sonore ; condition de taille de l'obstacle ; application acoustique (pièce, amphithéâtre).
  - Réfraction d'une onde mécanique : transmission (incidence normale) ; réfraction (incidence oblique) ;
    λ₁ sin i₂ = λ₂ sin i₁, sin i₁/v₁ = sin i₂/v₂ ; calcul de λ = v/N dans chaque milieu et de i₂ ; v = √(g.e)
    donnée en exercice.
  - Dispersion de la lumière : prisme, double réfraction, déviation D, spectre continu, lumière mono/
    polychromatique, ν et λ₀, n croît du rouge au bleu (tableau), bleu le plus dévié ; λ₀ = c/ν, v = c/n,
    λ = λ₀/n ; lois de Descartes n₁ sin i₁ = n₂ sin i₂, déviation D = i − r sur hémicylindre (exercices) ;
    n = c/v.
  - Dispersion des ondes mécaniques (cuve), milieu dispersif / non dispersif (eau pour les ondes de surface,
    verre pour la lumière ; air non dispersif pour le son).
- ⛔ **EXCLU** (absent du chapitre) :
  - Interférences (Young, interfrange), ondes stationnaires, réseaux, polarisation.
  - Formules du prisme (A = r + r', minimum de déviation), loi de Cauchy ; calcul des minima d'ordre k,
    intensité de la figure de diffraction.
  - Effet Doppler, écholocation (accroche seulement), réflexion totale, coefficient de réflexion/transmission.
  - Théorie de Huygens : lecture seulement (« En savoir plus »).
  - Aspect corpusculaire de la lumière, spectres de raies (pas de chapitre de physique atomique dans ce
    manuel de Sciences de l'informatique — à confirmer par la fiche d'ensemble ; le bandeau de la p.396 « Physique
    atomique et nucléaire ◆ Réactions nucléaires » est un reliquat de mise en page, sans contenu correspondant).

### Lecture

- **Pages lues en couche texte** (pdftotext -layout, page par page) : 308 à 337 (30 pages), 338 (rattachée au
  ch.12), 396 (réponses, colonne gauche), 398–399 (sites web).
- **Pages lues sur l'image** (110 dpi) : 308 (ajoutée après la relecture R-7), 309, 310, 311, 312, 313, 314, 315,
  316, 318, 319, 322, 323, 326, 327, 328, 329, 331, 332, 333, 334, 335, 336, 396 (24 pages). Pages 317, 320, 321,
  324, 325, 330 et 337, d'abord non vues, vérifiées sur l'image par la relecture R-7 (lecteur E), conformes : toutes
  les pages du chapitre sont désormais vues sur l'image.
- **Écarts couche texte / image** : λ rendu « / » dans toutes les fractions (p.314, 316, 323, 328, 329, 332) ;
  θ perdu (« = L/2.D », « tg() ») p.315–316 ; ≈ rendu « $ » p.315–316 ; ν (nu) rendu « V »/« Vx » p.325–329 ;
  λ₀ = c/ν rendu « /0 = c/2 » p.328 ; √(‖g‖.e) illisible p.333 ; θ = 1,22.λ/a éclaté p.335 ; k = 3,15.10⁻⁶ rendu
  « 3,15.106 » (exposant négatif perdu) p.331 ; QCM I « λ/a² » p.332 ; colonnes de la p.333 et de la p.396
  entremêlées (ch.11/ch.12). Tableaux p.314, 319, 326, 327 conformes dans le texte.
- **Coquilles [sic]** : p.310 Fig.1 « onde mécnique » ; p.314 Fig.6a « Figue de diffraction » ; p.314 unités
  « 1/a (10³ m) » (lire m⁻¹) ; p.315 « avec K une constante » (k) ; p.316 « λR et plus grande », « on peut
  déduire » ; p.319 « d'une d'une plaque » ; p.322–323 « mlieux », « relatrion », « retouve » ; p.323
  conclusion : « onde réfléchie » / « angle de réflexion » au lieu de réfractée / réfraction ; p.332 QCM I
  « λ/a² = 1 » ; p.334 ex. 8 « indice de réfaction » ; p.336 ex. 13 « angle de réfaction » ; p.396 ex. 5
  « v₂/N₂ = v₁/N₂ », ex. 6 « λ₁ = v₂/N », ex. 11 « θ = r/a ».
- **Doutes [?]** :
  - **Doute 1** — **Ex. 7 : réponses incompatibles avec l'énoncé** — avec v₁ = 0,30 m.s⁻¹, v₂ = 0,25 m.s⁻¹, N = 20
    Hz on trouve λ₁ = 1,5.10⁻² m, λ₂ = 1,25.10⁻² m et sin i₂ = (0,25/0,30)·0,5 → i₂ ≈ 24,6° ; le manuel donne 2.10⁻²
    m, 1,33.10⁻² m et 19,47° (ce qui correspond à v₁ = 0,40, v₂ ≈ 0,27 m.s⁻¹). Ne pas reprendre.
  - **Doute 2** — **Ex. 9 2°b)** : réponse « λ/a = 6,3.10⁻⁶ < 0,174 » ; le calcul donne λ/a = 0,63.10⁻⁶/10⁻⁴ =
    6,3.10⁻³ ; la valeur 0,174 n'a pas d'origine identifiable. L = 2Dλ/a = 1,26.10⁻² m (non donné). Ne pas
    reprendre.
  - **Doute 3** — **Ex. 6 4°)** : réponse « non, car v₂ ≠ v₁, pour N = Cte » — la variation de v avec l'épaisseur
    à N constant ne prouve pas l'absence de dispersion ; raisonnement à ne pas reprendre. λ₂ calculé ≈ 1,55.10⁻² m
    (arrondi à 1,5.10⁻² m dans le manuel).
  - **Doute 4** — **Remarque p.328** : « augmentation de (0,006) pour chaque diminution de dix picomètres » —
    d'après le tableau, n varie de 0,017 sur 334 nm, soit ≈ 5.10⁻⁷ par 10 pm : chiffre incohérent. Ne pas reprendre.
  - **Doute 5** — **p.312 Remarque 1** : « fente F de largeur a inférieure à la longueur d'onde λ » alors que a =
    0,6 mm et λ = 633 nm (a >> λ) ; de même §1.1 « lorsque la largeur a … est inférieure à λ » vs Fig.2b « a ≃ λ ».
    Formulation à corriger à l'adaptation (diffraction observable dès que a n'est pas très grand devant λ).
  - **Doute 6** — **Ex. 4 4°)** : réponse « l << λ, pas de diffraction » — pour λ = 5 m et l = 30 m, c'est l >> λ.
  - **Doute 7** — Ex. 12 : x₂ = 5,5 cm et x₃ = 8 cm cotent la figure (Fig.5) ; la réponse déduit L₂ = (5,5 −
    2,7)/2 = 1,4 cm. Cohérent.
  - **Doute 8** — Vérifiés cohérents : exercice résolu (λ = 525 nm, d = 0,21 mm), ex. 3, 10, 11 (λ ≈ 0,67 μm), 12,
    13.

## 2.12 Chapitre 12 — Généralités sur la transmission des signaux (manuel 223471, p.338–363)

Partie du manuel : « Ondes » (bandeau « Ondes ◆ Généralités sur la transmission des signaux »). Plage exacte :
**p.338** (Objectifs / Prérequis, page précédant l'ouverture) → p.339 (page d'ouverture n° 12) → **p.363** (fin de
« En savoir plus »). La p.364 est déjà la page Objectifs/Prérequis du chapitre 13. (Plage provisoire du brief
339–364 décalée d'une page.)
Notations : fréquence de la porteuse N_p (aussi « Npm » [sic] p.348), du signal modulant N ; amplitudes Um,
Upm ; phases φ, φ_p ; λ = v/N.

**Objectifs (p.338, VERBATIM)** — « Distinguer entre signal, support et canal d'information. » · « Justifier le
recours à l'onde électromagnétique comme support de transmission de l'information. » · « Décrire le principe de
transmission d'un signal via une onde électromagnétique. » · « Reconnaître la lumière comme étant une onde
électromagnétique particulière. » · « Distinguer les ondes lumineuses et les ondes hertziennes par leurs
fréquences. » · « Expliquer les fonctions de modulation et de démodulatio [sic] d'un signal. »

**Prérequis (p.338)** — SAVOIR : caractériser une grandeur physique sinusoïdale par sa période, sa fréquence, son
amplitude et sa phase initiale ; caractériser une onde par sa double périodicité temporelle et spatiale ; citer la
réflexion, la réfraction, la diffraction et la dispersion d'une onde comme des exemples d'interaction
onde-matière. SAVOIR FAIRE : reconnaître une grandeur physique sinusoïdale ; mesurer pour une onde ses périodes
temporelle et spatiale, sa vitesse de propagation ; visualiser à l'oscilloscope bicourbe une tension électrique,
simultanément deux tensions électriques.

**Page d'ouverture (p.339)** — titre « GÉNÉRALITÉS SUR LA TRANSMISSION DES SIGNAUX », n° 12 ; photo d'antennes
paraboliques, légende (VERBATIM) : « Le Paraboloïde, communément appelé parabole, a révolutionné les
communications à distance en très hautes fréquences. » Questions d'accroche (VERBATIM) : « Avec quels types de
transmission fonctionnent, les postes radio, les téléviseurs et les téléphones portables ? » · « Qu'est-ce qui
fait que les communications téléphoniques ainsi que les émissions de télévision en direct sont reçues
instantanément ? » · « Comment le modem d'un ordinateur assure-t-il la connexion à Internet ? Quelle est
l'origine du nom “modem” ? »

**Introduction (p.340, VERBATIM)** — « La transmission des informations à distance a été toujours un problème qui
a intrigué toute l'humanité. Grâce à la télécommunication qui a connu une évolution chronologique rapide
(télégraphe, téléphone fixe, téléphone mobile, télévision...), les informations sont transmises d'une façon
instantanée et à longues distances. De plus, elles passent à nos jours, de l'analogique au numérique pour
améliorer la qualité du son et de l'image. »

**Plan (titres numérotés du manuel)** —
1 SIGNAL ET INFORMATION (p.340–343 : exemple 1 code Morse, manipulation DEL, expériences 1 et 2 ; exemple 2
langue ; exemple 3 thermographie infrarouge) ·
2 TÉLÉCOMMUNICATION D'UN SIGNAL (p.343) : 2.1 Support de transmission en télécommunication (p.344) · 2.2
Modulation et canal de transmission (p.345–347 ; exemples télécommande, lasers, alarmes) · 2.3 Modulation d'une
porteuse sinusoïdale (p.348) · 2.4 Réception d'un signal (p.348–349) ·
3 LES ONDES ÉLECTROMAGNÉTIQUES (p.349) : 3.1 Définition · 3.2 Caractéristiques essentielles [titre imprimé
« CARATÉRISTIQUES » sic] (3.2.1 Célérité ; 3.2.2 Période temporelle et fréquence ; 3.2.3 Période spatiale, p.350)
· 3.3 Ondes lumineuses (p.350–351) · 3.4 Ondes hertziennes (p.351–353 ; 3.4.1 Gammes de fréquence ; 3.4.2
Propagation dans les milieux matériels) · 3.5 Émission et réception d'ondes hertziennes (p.353–355 ; 3.5.1
Antenne de Hertz ; 3.5.2 Antenne parabolique).
Puis « L'essentiel » (p.356), exercice résolu (p.357–358), « Exercices à résoudre » (p.359–361), « En savoir
plus » (p.362–363).

### Cours — Activités

- **§1 Exemple 1 — code Morse (p.340–341)** — télégraphe électrique de Morse (1837, Fig.1), télégraphe de Breguet
  (1844, Fig.2), code par flash lumineux (Fig.3), tableau du code Morse international (Fig.4, d'après « radio
  receiving for Beginners », 1922 : lettres A–Z et chiffres 0–9 en points et tirets). Questions (p.340) : « 1°)
  Peut-on numériser le code Morse ? 2°) Dans l'affirmative, citer un exemple de numérisation. » Réponse du
  manuel : état haut ↔ 1 (tiret), état bas ↔ 0 (point) ; « pour la lettre A, le nombre binaire associé est 01.
  Pour B et C, on associe respectivement 1000 et 1010. » Questions (p.341) : « 1°) Ecrire en consultant le
  tableau de la figure 4, les nombres binaires associés aux lettres (H,I,S et E). Que peut-on conclure ? 2°)
  Quel est le plus grand nombre binaire utilisé par le code Morse et quelle est la lettre correspondante ? »
  (sans réponse).
- **§1 Manipulation — Morse lumineux par DEL (p.341–342)** — pile 9 V, DEL ; Fig.5 : pile, résistor R, DEL rouge
  et DEL bleue en série (lettre A = point + tiret). Code adopté : DEL bleue = tiret, DEL rouge = point, DEL jaune
  = espacement entre deux lettres [le « Matériel » cite des DEL « vertes, rouges et bleues » : sic, la jaune
  manque et la verte ne sert pas]. **Expérience 1** : mot BIEN → « BRRRJRRJRJBR, mot à 12 bits nécessitant deux
  Leds bleues, sept rouges et trois jaunes » (vérifié). **Expérience 2** : suite de 12 carrés colorés
  (B R R R J R B J B R B R, image) → « BAC ». Question : une personne ignorant le code reçoit-elle le signal ?
  décrypte-t-elle le message ? Nouveau code (Fig.6 : bleu = espacement, rouge = un point, jaune = un tiret) :
  état des DEL pour « Bac » (J R R R B R J B J R J R, image) ; avec l'ancien code, « Le décodeur ne décryptera
  aucun mot (la première lettre ne figure pas dans le code Morse). »
- **§1 Exemple 2 (p.342)** — un Tunisien parlant arabe à un étranger (un Allemand) : signal sonore reçu, aucune
  information ; la langue est le code.
- **§1 Exemple 3 — thermographie infrarouge (p.342–343)** — Fig.7 : chien photographié par caméra infrarouge,
  échelle couleur–température ; note marginale (définition de la thermographie : « Procédé d'imagerie
  permettant de recueillir les variations de température à la surface d'un corps. »). Questions : « 1°)
  Identifier la région la plus chaude et celle qui est la plus froide. 2°) Peut-on utiliser ce principe dans
  d'autres domaines ? » Analyse : bouche, yeux, oreilles les plus chauds ; bout du nez froid ; le signal
  infrarouge est le support ; application en astronomie (température à la surface des planètes).
- **§2.1 (p.344)** — voix : basses fréquences « variant de 15 Hz à 20 kHz environ », s'atténue rapidement ;
  microphone → signal électrique BF « Celui-ci a la propriété de générer un type d'onde connue sous le nom
  d'onde électromagnétique, de plus grande portée que l'onde sonore » ; onde porteuse ; Fig.8 : A. G. Bell et le
  premier téléphone électrique (1876), « première télécommunication filaire » (membrane, bobine, aimant
  permanent, courant induit) ; Fig.9 haut-parleur, Fig.10 microphone ; Remarque : transducteur.
- **§2.2 (p.345–347)** — question : suffit-il de fixer des fréquences porteuses N_p différentes ? « La réponse
  est NON » ; canal [N_p − 20 kHz, N_p + 20 kHz] ; écart minimal entre porteuses voisines ≈ 2 × 20 kHz.
  Questions (VERBATIM) : « 1°) Dans les lignes téléphoniques, comment plusieurs communications ont lieu
  simultanément sans qu'il y ait brouillage du signal ? 2°) Pourquoi les chaînes de radiodiffusion sur la bande
  des ondes hectométriques (ou petites ondes PO), émettent-elles leurs programmes à des fréquences espacées
  généralement de 9 kHz ? » Interprétation : deux canaux distincts par ligne téléphonique (N_p1, N_p2) ; en
  radio, canal réduit sous 20 kHz car les sons les plus aigus utiles sont « nettement inférieures à 10 kHz » →
  espacement de 9 kHz en PO. **Exemple 1 — télécommande** (Fig.11–13) : questions « 1°) Comment chaque bouton
  de la télécommande donne-t-il une information spécifique au récepteur ? 2°) Quel est le support de
  transmission des informations ? 3°) Est-ce que le signal et le support suffisent pour une transmission
  adéquate ? » ; diode infrarouge alimentée par un multivibrateur (tension en créneaux), rapport cyclique
  propre à chaque bouton, information codée → décodeur. **Exemple 2 — trois lasers** : vert = beau, rouge =
  chaud, bleu = froid ; question (VERBATIM) : « Dans l'exemple 2, quel est le support de l'information ? » ; support = rayonnement laser (électromagnétique) ; information = couleur ; deux émetteurs
  identiques → besoin d'un canal (4ᵉ diode laser jaune pour l'un, orangée pour l'autre). **Exemple 3 —
  alarmes** : support = onde sonore ; information = fréquence (aigu/grave) ; « le timbre du son émis est le canal
  de transmission ».
- **§2.3 (p.348)** — chronogrammes Fig.14a (signal modulant, période T), 14b (porteuse), 14c (signal modulé en
  amplitude), 14d (signal modulé en fréquence). Expressions : voir Encadrés.
- **§2.4 (p.348–349)** — questions (VERBATIM) : « 1°) Tout récepteur de signal transmis par télécommunication
  (poste radio, téléviseur, téléphone fixe ou mobile...) doit être muni d'un oscillateur résonateur et d'un
  filtre passe bande entre autres. Expliquer le rôle de chacun de ces dispositifs. 2°) Le signal transmis étant
  modulé, que faut-il lui faire subir à la réception afin de l'identifier ? » Réponse : accorder le circuit
  oscillateur sur N_p (résonance) ; filtre dont la bande passante englobe le canal ; démodulation par un
  « démoduleur (voir étude détaillée au chapitre 13) ».
- **§3.2.3 Exemple (p.350)** — station à 102,5 MHz, c = 3.10⁸ m.s⁻¹ → « λ = 2,926 m » [arrondi : 2,927 m].
- **§3.3 (p.350–351)** — bandeau du spectre : ultraviolet (invisible) | violet, bleu, vert, jaune, orange, rouge
  (spectre visible) | infrarouge (invisible). Fig.15 « Spectre radiofréquence des ondes électromagnétiques » :
  Gamma (0,01 nm), X (1 nm), U.V (100 nm), visible (400–700 nm), ondes hertziennes (1 mm, 1 cm, 1 m, 1 km).
- **§3.4.2 (p.352–353)** — Fig.16 « Interaction des ondes hertziennes avec l'ionosphère » (ondes A, B, C, D) ;
  question (VERBATIM) : « Pour quelle(s) gamme(s) de fréquences, les satellites géostationnaires jouent-ils le
  rôle de relais en télécommunications ? » → SHF (3–30 GHz), ligne droite, traversent l'ionosphère ; paraboloïde
  directionnel ; GSM, télécommunication intercontinentale, télévision par satellite.
- **§3.5.1 Antenne de Hertz (p.353)** — Fig.17 : GBF alimentant une tige T₁ de longueur L (deux demi-brins) ;
  tige T₂ identique « liée à un micro-ampèremètre ou un fréquencemètre » (Fig.17, appareil noté A) ; le texte
  précède d'un « Le premier pionnier des antennes est le physicien Hertz. » Question (VERBATIM) : « Sachant que les communications par
  GSM utilisent la gamme de fréquences (3 GHz - 30 GHz), montrer que l'antenne dont il faut munir les appareils
  de téléphone mobile peut être d'une longueur comprise entre 2,5 cm et 2,5 mm (Fig.18). » [? ces valeurs sont
  celles d'une antenne quart d'onde ; voir doutes]
- **§3.5.1 Manipulation — expérience de Hertz au laboratoire (p.354)** — GBF, deux fréquencemètres (multimètres
  numériques), deux antennes sur support (Fig.19) ; fréquencemètre (1) sur T₂, (2) aux bornes du GBF.
  **Expérience 1** : fréquences (1) et (2) pratiquement égales. **Expérience 2** : en éloignant T₂, (1) affiche
  zéro à partir d'une distance D « d'autant plus grande que la fréquence affichée par (2) est plus élevée ».
  Questions (VERBATIM) : « 1°) Qu'est-ce qui montre dans les expériences réalisées qu'il y a eu production d'une
  onde électromagnétique au niveau de la tige T2 ? 2°) Comparer les fréquences des signaux émis et reçu. 3°)
  Préciser l'influence de la fréquence de l'onde électromagnétique sur sa portée. » Commentaire : propagation
  sans changement de fréquence ; portée croissante avec la fréquence. Remarque : en BF, l'absence d'indication
  « n'infirme pas la production d'une onde électromagnétique ».
- **§3.5.2 (p.355)** — paraboloïde (Fig.20) ; antenne de Yagi (Fig.21, transmission terrestre) ; antennes à
  bobine (Fig.22, militaires).

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Conclusion (§1, p.343)** — « La transmission d'une information nécessite l'utilisation d'un signal codé. La
> réception d'un signal dont on ignore le code ne porte aucune information. » Remarque : « L'auditeur, qui est à
> l'écoute des émissions radio, reçoit les informations par un support électromagnétique entre la station
> émettrice et le poste radio et un support sonore (signal mécanique) entre le haut-parleur et son oreille. »

> **Définition (§2, p.344)** — « On appelle télécommunication toute transmission électronique d'informations
> (sons, images, écrits...) à distance (par fil électrique, fibre optique...). » (Introduction p.343 : « Cette
> technologie moderne a débuté depuis 1792 en France avec le télégrahe [sic] aérien. »)

> **Remarque (§2.1, p.344)** — « En télécommunication, on a besoin de transformer l'énergie sonore en énergie
> électrique et vice-versa, d'où le besoin d'un transducteur, appareil capable de transformer un signal
> quelconque en un signal électrique. Le haut parleur et le microphone sont les transducteurs les plus utilisés
> en télécommunications »

> **Conclusion (§2.1, p.344)** — « Etant de faible portée, les ondes sonores ne peuvent être télécommuniquées
> telles quelles sur des grandes distances. En télécommunication, le support de transmission des signaux est
> l'onde électromagnétique, d'où sa qualification de porteuse (ou onde porteuse). »

> **Modulation, signal modulant, canal (§2.2, p.345)** — « Au cours de la télécommunication d'un signal, la
> porteuse (onde électromagnétique) se trouve modifiée par ce dernier : on dit qu'elle est modulée par le signal
> qu'elle porte. Par suite, la télécommunication d'un signal est qualifiée comme étant une transmission par
> modulation, alors que le signal de basse fréquence qui a provoqué la modulation est appelé signal modulant. »
> […] « chacun des signaux émis va être transmis sous forme d'un signal modulé caractérisé par la bande de
> fréquence **[Np - 20 kHz, Np + 20 kHz]** environ et que l'on appelle canal de transmission du signal. » […]
> « il ne faut pas que la différence entre deux fréquences porteuses voisines Np1 et Np2 soit inférieure à deux
> fois 20 kHz. »

> **Conclusion (§2.2, p.347)** — « En télécommunication, la transmission des signaux se fait par modulation. La
> transmission par modulation met en jeu : - un signal à transmettre : le signal modulant de basse fréquence,
> - une porteuse (onde électromagnétique) : le signal de haute fréquence à moduler. La télécommunication d'un
> signal nécessite un canal de transmission, fréquence de la porteuse à laquelle est associée une bande de
> fréquence d'une largeur de l'ordre de grandeur du domaine des fréquences du signal transmis. »

> **Modulation d'une porteuse sinusoïdale (§2.3, p.348)** — « **u(t) = Umcos(2πNt + φ)**, où Um est son
> amplitude et φ est sa phase initiale. » ; porteuse « **up(t) = Upmcos(2πNpt + φp)** » ; « La modulation de la
> porteuse consiste à faire varier son amplitude Upm, sa fréquence Np ou sa phase initiale par le signal à
> transmettre u(t). - Si Upm varie en fonction de u(t), on a une modulation d'amplitude (Fig.14c). - Si Npm
> [sic, Np] varie en fonction de u(t), on a une modulation de fréquence (Fig.14d). Dans ce cas, le signal
> modulé a une amplitude égale à celle de la porteuse, mais une fréquence qui varie au cours du temps. - Si φp
> varie en fonction de u(t), on a une modulation de phase dont l'étude est hors programme. »
> **Conclusion** : « En télécommunication avec une porteuse sinusoïdale, la transmission d'un signal se fait par
> modulation, soit de son amplitude, soit de sa fréquence, voire de sa phase. »

> **Conclusion (§2.4, p.349)** — « A la réception d'un signal transmis par modulation, sa perception nécessite,
> en plus du filtrage, une démodulation. La démodulation est un procédé de traitement de signal modulé qui
> aboutit à la séparation du signal transmis de la porteuse. »

> **Définition (§3.1, p.349)** — « L'onde électromagnétique est une onde résultant de l'association d'un champ
> électrique et d'un champ magnétique, tous les deux de vecteurs champs sinusoïdaux, de même période,
> perpendiculaires l'un à l'autre en tout point et se propagent, dans toutes les directions sans nécessiter un
> support matériel. »

> **Caractéristiques (§3.2, p.349–350)** — « Les ondes électromagnétiques se propagent dans le vide et dans les
> milieux matériels. Du fait qu'elles sont transversales, les vecteurs champs **E⃗** et **B⃗** qui leur sont
> associés varient en tout point perpendiculairement à la direction de propagation. » · Célérité : « Dans le
> vide, elle a sa valeur la plus élevée : **c = 3.10⁸ m.s⁻¹**. Dans les milieux matériels, elle a comme
> expression : **v = c/n**, le nombre n étant l'indice de réfraction absolu du milieu. » Remarque : air ≈ 1 ;
> « Autre exemple : l'indice de réfraction du verre est n = 1,5. D'où, v = 2.10⁸ m.s⁻¹. » · Période : « Etant
> très petite, la période T peut avoir une valeur de l'ordre de 10⁻²⁸ s (rayons γ). La fréquence **N = 1/T** peut
> atteindre un milliard de milliards de gigahertz. » · Longueur d'onde : « la plus petite distance séparant
> deux points dans le même état vibratoire. C'est aussi la longueur λ parcourue par l'onde pendant une vibration
> complète, c'est-à-dire pendant la période temporelle T. » **λ = v/N = v.T, avec v = c/n**.

> **Ondes lumineuses (§3.3, p.350–351)** — « C'est un domaine d'ondes électromagnétiques caractérisé par des
> longueurs d'onde comprises, dans l'air, entre **0,38 µm et 0,78 µm**. » « Les radiations ultraviolettes et
> infrarouges constituent les parties invisibles du spectre. »

> **Ondes hertziennes (§3.4, p.351)** — « Les ondes hertziennes ou ondes radio sont des ondes électromagnétiques
> dont le domaine des fréquences s'étend de **300 kHz à 300 GHz**. Dans l'air ou dans le vide, elles ont des
> longueurs d'onde comprises entre **1 mm et 30 km**. Elles se propagent de deux façons : - dans l'espace libre
> (l'air, le vide, etc), - dans les lignes (câbles coaxiaux, fibres optiques, etc). Elles sont utilisées comme
> porteuses pour différents types de transmission. » [? 300 kHz ↔ 1 km, et non 30 km ; le tableau descend à
> 10 kHz : incohérence interne, voir doutes]

> **Tableau des gammes (§3.4.1, p.352)** —
>
> | Désignation métrique | Longueur d'onde | Fréquence | Désignation courante | Domaine d'utilisation |
> |---|---|---|---|---|
> | Ondes millimétriques | 1 mm - 10 mm | 30 - 300 GHz | EHF : extra-hautes fréquences | Radio-astronomie |
> | Centimétriques hyperfréquence | 1 cm - 10 cm | 3 GHz - 30 GHz | SHF : superhautes fréquences | - Satellite - Téléphone GSM |
> | Décimétriques | 1 dm - 10 dm | 300 MHz - 3 GHz | UHF : ultrahautes fréquences | Télévision et radars |
> | Métriques | 1 m - 10 m | 30 - 300 MHz | THF ou VHF : très hautes fréquences | Télévision et radio en FM |
> | Décamétriques ondes courtes | 10 m - 100 m | 3 MHz - 30 MHz | HF : hautes fréquences | Radio à grande portée |
> | Hectométriques petites ondes | 100 m -1000 m | 300 kHz - 3 MHz | MF : moyennes fréquences | Radio en modulation AM |
> | Kilométriques grandes ondes | 1 km -10 km | 30 kHz - 300 kHz | BF : basses fréquences | Avions, navires, radiotélégraphie |
> | Myriamétriques | 10 km - 30 km | 10 kHz - 30 kHz | VLF : très basses fréquences | Détresse en mer, radiotélégraphie |

> **Propagation (§3.4.2, p.352)** — « De ces interactions onde-matière, il peut résulter les phénomènes
> d'absorption, de réflexion, de diffusion, de réfraction ou de dispersion. […] Les ondes métriques se propagent
> en ligne droite et peuvent contourner les obstacles de quelques mètres de dimension. Elles sont réfléchies sur
> les murs, les rochers... Les ondes hertziennes de fréquences typiquement inférieures à 30 MHz (onde B de la
> figure 16) sont réfléchies par l'ionosphère (région de l'atmosphère comprise entre les altitudes 60 km et
> 800 km). Les ondes de fréquences plus grandes traversent l'ionosphère (onde notée a). » Conséquences : ondes
> courtes, PO et grandes ondes « piégées entre l'ionosphère et la Terre » ; fréquences supérieures → relais de
> télévision.

> **Antenne de Hertz (§3.5.1, p.353)** — « Une onde électromagnétique est produite par un courant électrique
> variable dans le temps. Donc, tout circuit électrique siège de courant variable peut produire une onde
> électromagnétique. Pour la détecter, il faut une antenne. » « On montre que la puissance rayonnée par la tige
> est optimale si sa longueur L vérifie la relation : **L = k λ/2 avec k ∈ N*** Pour k = 1 : la puissance
> rayonnée est maximale. De même, le courant produit par l'onde électromagnétique dans la tige réceptrice est
> maximal si : **L = λ/2**. On dit que l'on a une antenne demi-onde. Remarque : il y a des antennes quart d'onde
> **L' = λ/4** »

> **Conclusion (§3.5.1, p.355)** — « Pour qu'il y ait production d'une onde électromagnétique, il faut que
> l'antenne émettrice soit d'une longueur égale à la moitié ou au quart de la longueur d'onde. Il en est de même
> pour l'antenne réceptrice. La portée des ondes électromagnétiques augmente avec leurs fréquences. »

> **Antenne parabolique (§3.5.2, p.355)** — « Les antennes paraboloïdes (Fig.20) appelées communément antennes
> paraboliques sont réservées pour les émissions (SHF) dont la porteuse a une fréquence comprise entre 3 GHz et
> 30 GHz et dont la source est à l'infini (grande distance de 36000 km de la Terre) de telle façon que les
> surfaces équiphases sont des plans et non des sphères. La tête réceptrice se trouvant au foyer capte une
> puissance électromagnétique maximale. »

**L'essentiel (p.356, VERBATIM)** — « ■ L'onde électromagnétique est une onde transversale qui se propage dans les
milieux matériels à la célérité : v = c/n, où n est l'indice de réfraction du milieu et c est sa célérité dans le
vide. Dans l'air, comme dans le vide : c = 3.10⁸ m.s⁻¹. ■ L'onde électromagnétique est le support de transmission
des informations en télécommunication. ■ Le canal de transmission d'un signal est défini par la fréquence de sa
porteuse et par une bande de fréquences englobant les siennes ■ La télécommunication d'un signal est réalisée par
modulation d'un signal de haute fréquence nommé porteuse. ■ En modulation, le signal de basses fréquences à
transmettre est le signal modulant et le signal transporté par la porteuse est le signal modulé. ■ Les ondes
lumineuses et les ondes hertziennes sont des exemples d'ondes électromagnétiques. ■ Les ondes hertziennes sont
les ondes électromagnétiques utilisées en télécommunication. ■ L'onde hertzienne est générée au niveau d'un
circuit électrique parcouru par un courant de fréquence élevée. Sa réception, comme son émission, nécessite une
antenne. ■ La portée d'une onde électromagnétique, et en particulier l'onde hertzienne, augmente avec sa
fréquence. »

### Exercices résolus

**Exercice résolu (p.357–358) — éclair et tonnerre** — Énoncé : cumulonimbus = condensateur géant ; étincelle →
éclair ; dilatation brutale de l'air → tonnerre. « 1°) Quel est le type d'onde qui véhicule l'éclair et celui qui
véhicule le tonnerre ? 2°) Sachant que la vitesse de propagation de la lumière est c = 3.10⁸ m.s⁻¹ et celle du son
est v = 340 m.s⁻¹, expliquer pourquoi on voit l'éclair, puis on entend le tonnerre to secondes après. 3°) L'éclair
peut produire des surtensions dans les lignes électriques de la STEG. Expliquer ces phénomènes. Les ondes
électromagnétiques produites par les nuages sont-elles lumineuses, hertziennes ou les deux ? 4°) Peut-on
localiser la position de la décharge ? 5°) Montrer à l'aide d'une recherche documentaire que la couleur de
l'éclair constitue une source d'informations pour les météorologues. »
Solution : 1°) éclair = signal lumineux (onde électromagnétique, c dans l'air) ; tonnerre = onde sonore (onde
mécanique) [« tonerre » sic]. 2°) célérité du son « trop petite devant celle de la lumière » → décalage t₀.
3°) l'onde électromagnétique se propage dans les lignes et se superpose au champ de la ligne → surtension ou chute
de tension ; « La lumière ne se propage pas dans les lignes. Il s'agit alors d'une onde hertzienne » ; la
décharge produit une onde lumineuse et une onde hertzienne. 4°) d = c.t₁, d = v.t₂, t₂ − t₁ = t₀ →
**d = t₀ . c.v/(c − v)** (encadré). 5°) blanche : air sec ; jaune : grande quantité de poussière ; rouge : air
humide, « quantité d'eau abandante [sic] », jour pluvieux ; bleue : grande quantité de grêle (Fig.3 « Nuages
blancs », Fig.4 « Nuages poussiéreux », photos).

### Tests rapides des acquis (p.359)

- **Ex. 1 — Vrai ou faux (14 items)** : 1- transmission seulement avec les ondes électromagnétiques ; 2- ondes
  métriques 30 à 300 MHz ; 3- la couleur de la lumière peut constituer un canal ; 4- les ondes EM de basses
  fréquences se propagent mieux que celles de hautes fréquences dans un milieu matériel ; 5- la modulation est un
  canal de transmission ; 6- la fréquence de la porteuse est un canal de transmission ; 7- la lumière est une onde
  hertzienne ; 8- chaque station radio est caractérisée par la fréquence du signal modulant ; 9- toute onde EM est
  une onde hertzienne ; 10- célérité d'une onde EM maximale dans le vide ; 11- la télécommande d'un téléviseur
  émet des ondes EM infrarouges ; 12- les signaux de la télécommande sont modulés en fréquence ; 13- le modem est
  un modulateur et démodulateur de signaux ; 14- la fréquence du signal modulant est supérieure à celle de la
  porteuse. (Réponses non fournies.)
- **Ex. 2 — QCM (7 questions)** : I. ondes hertziennes : a- colorées / b- ne se propagent pas dans le vide / c- ondes
  électromagnétiques ; II. Radio-Tunis 92 MHz : a- λ = 3,26 m / b- période 10,8 ns / c- ondes centimétriques ;
  III. la modulation peut modifier : a- l'amplitude de la porteuse / b- la fréquence du signal modulant / c- la
  phase du signal modulé ; IV. signal émis par une antenne : a- lumineux / b- hertzien / c- sonore /
  d- électromagnétique ; V. ondes hertziennes se propagent : a- dans les métaux / b- dans les fibres optiques /
  c- à travers l'ionosphère ; VI. ondes hertziennes : a- fréquence plus élevée que la lumière / b- λ supérieure à
  celle de l'infrarouge / c- fréquence inférieure à celle des UV / d- constituent un canal de transmission ;
  VII. les antennes émettent : a- des ondes EM de même fréquence que le courant qui les produit / b- des signaux
  sonores / c- des ondes hertziennes sinusoïdales. (Réponses non fournies.)

### Exercices et problèmes (p.360–361) — 10 exercices au total (2 tests + 5 application + 3 synthèse)

**Exercices d'application**
- **Ex. 3** (p.360) : émetteurs E₁, E₂, nombre binaire à trois bits par trois LED bleues (allumée = 1,
  éteinte = 0) ; LED jaune = E₁, LED rouge = E₂ (figure à deux colonnes). 1°) nombres binaires ; 2°) support ; 3°) canaux.
- **Ex. 4** (p.360) : 1°) différence AM / FM ; 2°) identifier les signaux Fig-a (amplitude constante, fréquence
  variable) et Fig-b (amplitude variable) en justifiant.
- **Ex. 5** (p.360) : ondes courtes en radiodiffusion. 1°) nature ; 2°) pourquoi « courtes » ; 3°) longueurs d'onde
  dans l'air ; 4°) domaine de fréquences (c = 3.10⁸ m.s⁻¹).
- **Ex. 6** (p.360) : spectre des ondes EM (bande de Fig.15). 1°) comparer λ rouge et λ bleu ; 2°) comparer
  fréquences hertziennes et UV.
- **Ex. 7** (p.360) : autoradio, antenne L réglable, stations 87 MHz à 108 MHz. 1°) gamme ; 2°) porteuses ou ondes
  à transmettre ? 3°) λ aux limites ; 4°) antenne « quart d'onde » pour 94,3 MHz (Radio Tunis « chaîne
  nationale »), c = 3.10⁸ m.s⁻¹.

**Exercices de synthèse**
- **Ex. 8** (p.360) : antenne parabolique (photo). 1°) caractéristiques ; 2°) pourquoi l'émetteur est dans le plan
  équatorial à 36000 km ; 3°) but marqué à t = 89 min, instant de visualisation (c = 3.10⁸ m.s⁻¹) ; 4°) pourquoi un
  retard satellite vs voie terrestre.
- **Ex. 9 — Mesure de la hauteur d'un gratte-ciel par le laser** (p.361) : télémétrie ; laser rouge, goniomètre
  (i₁, i₂), mètre-ruban ; Fig-1 : deux positions du laser distantes de d, distances d₁, d₂ au pied, angles i₁, i₂,
  hauteur h. 1°) étapes ; 2°) montrer **h = d / (1/tg i₂ − 1/tg i₁)** ; 3°) calculer d₁ ? 4°) intérêt pratique ;
  5°) astronomie ?
- **Ex. 10 — Étude de texte « L'oscillateur de Hertz »** (p.361) : 1887, « Excitateur » (conducteur rectiligne
  fermé sur une bobine inductive B₁, éclateur de deux boules P et Q espacées d'un demi-centimètre, bobinage B₂ sur
  barreau de fer, pile, interrupteur à ressort), résonateur = boucle métallique non fermée à une dizaine de mètres
  ; onde prévue par Maxwell. Questions : 1°) preuve de l'onde EM ; 2°) émetteur et récepteur ; 3°) étincelles =
  oscillations amorties d'un RLC série : identifier bobine et condensateur ; 4°) λ = 9 m, célérité
  2,99.10⁸ m.s⁻¹ → fréquence. [« metta » sic, deux fois]

### Réponses du manuel (p.396 colonne droite → p.397 haut gauche, vérifiées sur l'image)

Ex. 3 : 1°) Pour E₁, c'est 101 et pour E₂ c'est 110 ; 2°) L'onde est électromagnétique ; 3°) Le canal de
transmission pour E₁ est la Led jaune et pour E₂, c'est la LED rouge. · Ex. 4 : 1°) - L'amplitude de la porteuse
varie au cours du temps : modulation d'amplitude. - La fréquence de porteuse varie au cours du temps : modulation
de fréquence. 2°) Fig.a : AM et Fig.b : FM [sic : sur l'image, Fig-a a une amplitude constante et Fig-b une
amplitude variable ⇒ Fig.a FM, Fig.b AM]. · Ex. 5 : 1°) Ondes électromagnetiques ; 2°) De hautes fréquences se
propageant directement ; 3°) de 1mm à 10 mm. 4°) de 30 à 300 GHz [? valeurs des ondes millimétriques, pas des
ondes courtes]. · Ex. 6 : 1°) λbleu < λrouge ; 2°) Les fréquences des ondes hertziennes sont inférieures aux
fréquences ultraviolettes. · Ex. 7 : 1°) Ondes kilométriques ou grandes ondes [? 87–108 MHz = ondes métriques
VHF/FM] ; 2°) Ondes porteuses ; 3°) 2,77 m < λ < 3,44 m ; 4°) l = 79,5 cm. · Ex. 8 : 1°) Détecteur d'ondes
électromagnétiques de hautes fréquences situé à l'infini ; 2°) Satellite géostationnaire ; 3°) Δt = 24.10⁻² s
plus tard ; 4°) Le signal émis par satellite parcourt une distance plus grande. · Ex. 9 : 1°) On mesure i₁ puis on
translate le laser de d et on mesure i₂ ; 2°) d₂ − d₁ = d = h(1/tgi₂ − 1/tgi₁) ; 3°) oui d₁ = h/tgi₁ ; 4°) Mesurer
les dimensions à distance. 5°) oui via les satellite équipés de laser. · Ex. 10 : 1°) L'étincelle entre les
extrémités de la boucle. 2°) Emetteur : conducteur fermé sur (B₁) avec éclateur ; Récepteur : boucle métallique
non fermée. 2°) [3°] (B₁) est la bobine, l'éclateur est le condensateur. 4°) N = 33,3 MHz. · Pas de réponse :
Ex. 1, 2.

### En savoir plus / Documents

- **« Télécommunication infra-rouge » (p.362–363)** — matériel : télécommande, DEL, circuit intégré 4011 (4 portes
  NAND), circuit intégré **TSOP1736** (détecteur IR et démodulateur pour porteuse de 36 kHz), polarisé sous +5 V
  (Fig.1 bornes −, +, S ; Fig.2 montage avec R = 5 kΩ et voltmètre). Exp. 1 : sans IR, sortie +4,84 V (Fig.3a) ;
  avec IR, +3,64 V (Fig.3b) ; tableau état diode 1 → 3,64 V → état logique 0 ; 0 → 4,84 V → 1 : « porte logique
  NON » ; « canal de transmission défini par la valeur de la tension ». Exp. 2 : oscilloscope à mémoire,
  succession d'états hauts et bas, « principe du code Morse » (Fig.4) ; codage propre à chaque bouton. Exp. 3 :
  porte NAND (broches 1-2 entrées, 3 sortie) + diode ; tension de basculement ≈ 4,5 V ; diode allumée sans IR,
  éteinte avec IR ; question : modifier le montage pour inverser. Exp. 4 : signal aux bornes de la diode IR
  modulé (Fig.6), porteuse 36 kHz. (Raisonnement de l'Exp. 3 confus dans le texte : « la sortie de la porte à
  l'état bas. Mais, puisqu'il s'agit d'une porte NON, la sortie est à l'état haut » [sic].)

### Écart avec la référence (aucune)

**Aucun chapitre de référence** : rien d'équivalent dans `physique-bac-sciences-exp` (11 chapitres, aucun sur les
télécommunications), ni ailleurs dans `content/` (recherche « modulation », « onde porteuse », « hertzien »,
« antenne », « Morse », « démodul » : aucun cours.md de physique ; seules occurrences hors sujet :
technologie-bac-techniques « transmission » mécanique, math-bac-info nombres complexes). Chapitre à **créer**
intégralement. Liens possibles : sciences-exp/08 pour v = c/n, spectre visible ; le ch.11 de ce manuel pour
réflexion/réfraction/diffraction (prérequis) ; le ch.13 pour modulation/démodulation détaillées ; les chapitres
filtres (ch.6–7 de ce manuel) pour le « filtre passe bande » de la réception.
- ✅ notions propres : signal / information / code / support / canal ; numérisation binaire du Morse ;
  télécommunication, transducteur, porteuse, signal modulant / modulé, canal [N_p ± 20 kHz], espacement 9 kHz en
  PO ; AM, FM, (modulation de phase hors programme) ; réception : résonance de l'oscillateur, filtre passe-bande,
  démodulation ; onde EM (E⃗ ⊥ B⃗, transversale, sans support), c, v = c/n, λ = v/N ; domaines lumineux
  (0,38–0,78 µm) et hertziens (tableau des gammes) ; ionosphère (< 30 MHz réfléchies) ; satellite géostationnaire
  (SHF) ; antenne demi-onde L = kλ/2, quart d'onde λ/4 ; portée croissante avec la fréquence (affirmation du
  manuel) ; télémétrie laser ; d = t₀·cv/(c − v).

### Bornes de scope

- ✅ **INCLUS** : distinction signal / support / canal / code (Morse, DEL, langue, thermographie, télécommande,
  lasers, alarmes) ; numérisation binaire (point 0 / tiret 1) ; définition de la télécommunication ;
  transducteurs (micro, haut-parleur) ; porteuse = onde électromagnétique ; modulation, signal modulant, signal
  modulé ; canal de transmission et écart entre porteuses ; expressions u(t) = Um cos(2πNt + φ) et
  up(t) = Upm cos(2πNpt + φp) ; reconnaissance AM / FM sur chronogramme ; rôle de l'oscillateur accordé, du filtre
  passe-bande, de la démodulation ; définition et caractéristiques de l'onde EM ; c = 3.10⁸ m.s⁻¹, v = c/n,
  N = 1/T, λ = v/N = v.T (calculs de λ pour une station, de T) ; domaine visible, UV/IR invisibles ; tableau des
  gammes hertziennes (désignations métriques et courantes, usages) ; réflexion ionosphérique, satellites relais
  ; antenne de Hertz demi-onde / quart d'onde (calcul de longueur) ; expérience de Hertz (fréquence conservée,
  portée) ; paraboloïde ; retard de transmission satellite (2 × 36000 km) ; distance d'un orage ; télémétrie par
  triangulation (ex. 9).
- ⛔ **EXCLU** : modulation de phase (« hors programme », VERBATIM p.348) ; étude quantitative de la modulation
  (taux, spectre, multiplieur) et de la démodulation → chapitre 13 ; équations de Maxwell, expression des champs
  E et B, énergie/intensité de l'onde EM, polarisation ; numérisation au sens CAN (chapitre 9) ; propagation
  guidée (fibre optique) au-delà de la mention ; électronique de l'« En savoir plus » (TSOP, portes NAND) :
  lecture, non exigible.

### Lecture

- **Pages lues en couche texte** : 338 à 363 (26 pages), 364 (rattachée au ch.13), 396–397 (réponses).
- **Pages lues sur l'image** (110 dpi) : 338, 341, 342, 348, 350, 351, 352, 353, 358, 359, 360, 361, 362, 396, 397
  (15 pages). Pages 340, 343–347, 349, 354–357 et 363, d'abord non vues, vérifiées sur l'image par la relecture
  R-7 (lecteur E), conformes ; E⃗ et B⃗ confirmés comme vecteurs p.349 (rendus « I I E et B » en couche texte).
  Seule la p.339 (ouverture, légende et questions lisibles en texte) n'a pas été vue sur l'image.
- **Écarts texte/image** : λ rendu « / » (p.350, 353) ; « k ∈ N* » rendu « k N * » (p.353) ; fraction de h
  (ex. 9) éclatée ; d = t₀·cv/(c − v) éclaté (p.358) ; tableau p.352 et tableau p.362 conformes ; colonnes
  ch.11/ch.12 entremêlées p.396.
- **Coquilles [sic]** : p.338 « démodulatio » ; p.343 « télégrahe » ; p.348 « Npm », « sigaux » ; p.349
  « CARATÉRISTIQUES » ; p.341 matériel « vertes, rouges et bleues » (DEL jaune utilisée) ; p.342
  « thermographieinfrarouge » ; p.357–358 « tonerre », « chronomètrant », « abandante » ; p.360 « correpondant »,
  « fréquence des ondes » ; p.361 « metta » (×2), « instrumnt », « La premier dispositif », « interrupeur » ;
  p.362–363 « abscence », « abscene » ; p.397 « Ondes électromagnetiques ».
- **Doutes [?]** :
  - **Doute 1** — **Ondes hertziennes p.351** : « 300 kHz à 300 GHz » et « 1 mm et 30 km » sont incompatibles (300
    kHz ↔ 1 km ; 30 km ↔ 10 kHz) ; le tableau p.352 descend jusqu'à 10 kHz (VLF). À trancher à l'adaptation
    (proposition : s'aligner sur le tableau, en le signalant).
  - **Doute 2** — **Antenne GSM p.353** : « entre 2,5 cm et 2,5 mm » pour 3–30 GHz = λ/4 (λ = 10 cm → 1 cm), alors
    que le paragraphe impose la demi-onde (5 cm → 5 mm). Préciser « quart d'onde » si repris.
  - **Doute 3** — **Réponses ex. 4 2°)** inversées (image : Fig-a FM, Fig-b AM) ; **ex. 5 3°–4°)** (1–10 mm,
    30–300 GHz) = ondes millimétriques, alors que les ondes courtes sont décamétriques 10–100 m, 3–30 MHz (tableau
    p.352) ; **ex. 7 1°)** « grandes ondes » faux (87–108 MHz = ondes métriques, radio FM). Ne pas reprendre. Ex. 7
    3°–4°), ex. 8 3°) (0,24 s), ex. 10 4°) (2,99.10⁸/9 = 33,2 MHz, imprimé 33,3 MHz) cohérents ; QCM II : λ = 3,26 m
    et T = 10,87 ns cohérents.
  - **Doute 4** — **p.350** : « T de l'ordre de 10⁻²⁸ s (rayons γ) » et « un milliard de milliards de gigahertz »
    (10²⁷ Hz) : ordres de grandeur extrêmes, à ne pas reprendre comme valeurs de référence.
  - **Doute 5** — **p.354–355 et L'essentiel** : « La portée … augmente avec sa fréquence » — conclusion du manuel
    tirée d'une expérience de labo ; formulation générale physiquement contestable (absorption, ionosphère) :
    reprendre comme résultat de l'expérience décrite, sans généraliser.
  - **Doute 6** — Exercice résolu 3°) : « La lumière ne se propage pas dans les lignes » — raisonnement du manuel,
    approximatif.
  - **Doute 7** — Sigles p.351 / tableau p.352 : la liste de la p.351 donne « VLF, LF, MF, HF, VHF, UHF, SHF et
    EHF », mais le tableau de la p.352 écrit « BF : basses fréquences » pour la ligne kilométrique (30–300 kHz).
    Incohérence interne ; à l'adaptation, retenir LF en signalant le « BF » du manuel.

## 2.13 Chapitre 13 — Modulation et démodulation des signaux (manuel 223471, p.364–391)

Partie du manuel : « Ondes » (bandeau « Ondes ◆ Modulation et démodulation des signaux »). Plage exacte :
**p.364** (objectifs / prérequis) → p.365 (page d'ouverture n° 13) → **p.391** (fin de « En savoir plus »). Les
réponses sont p.397. Dernier chapitre du manuel.
Notations : u(t) signal modulant, Uo tension de décalage (offset), up(t) porteuse, us(t) tension de sortie,
k = 0,1 V⁻¹ (multiplieur AD633JN), USm max / USm min, m taux de modulation, N / Np (No en FM : porteuse non
modulée), β indice de modulation ; Tp, T périodes de la porteuse et du modulant.

**Objectifs (p.364, VERBATIM — l'encadré n'a pas de titre « Objectifs » imprimé)** — « Réaliser la modulation
d'une tension sinusoïdale en amplitude. » · « Mettre en évidence expérimentalement l'influence de la composante
continue ajoutée à la tension modulante sur la qualité de la modulation. » · « Calculer le taux de modulation d'un
signal sinusoïdal. » · « Réaliser la démodulation d'un signal électrique sinusoïdal modulé en amplitude. » ·
« Mettre en évidence expérimentalement l'influence de la fréquence de l'onde électromagnétique porteuse du signal
sur la démodulation de ce dernier. » · « Réaliser la modulation d'une tension sinusoïdale en fréquence. »

**Prérequis (p.364)** — SAVOIR : caractériser une grandeur physique sinusoïdale par sa période, sa fréquence, son
amplitude et sa phase initiale ; donner le symbole d'une diode, d'un condensateur... ; définir la charge et la
décharge d'un condensateur ; définir un filtre électrique. SAVOIR FAIRE : reconnaître une grandeur physique
sinusoïdale ; visualiser à l'oscilloscope bicourbe une tension, simultanément deux tensions ; mesurer à
l'oscilloscope les caractéristiques d'un signal périodique (période, amplitude...) ; monter une diode ; réaliser
un filtre CR passe haut, un filtre passe bas RC.

**Page d'ouverture (p.365)** — titre « MODULATION ET DÉMODULTION [sic] DES SIGNAUX », n° 13 ; légende (VERBATIM) :
« La télécommunication a connu une grande révolution par l'avènement de la modulation et ne cesse de se développer
grâce au même phénomène qui trouve d'ailleurs ses applications dans d'autres domaines comme la synthèse
polyphonique. » Questions d'accroche (VERBATIM) : « Les émissions télévisées sont-elles modulées en amplitude (AM)
ou en fréquence (FM) et pourquoi ? » · « La fréquence de l'onde porteuse des émissions d'une station radio en AM
est égale à 150 kHz au minimum, tandis qu'en FM, elle tourne autour de 100 MHz, pourquoi ? »

**Introductions (p.366, VERBATIM)** — « Si les télécommunications deviennent de plus en plus présentes même dans la
vie de tous les jours, c'est grâce à l'utilisation des ondes électromagnétiques et plus précisément les ondes
hertziennes comme supports de transmission des informations. A ce propos, on a vu au chapitre précédent que, là
où on a à télécommuniquer la voix humaine, la musique, l'image, etc, on recourt à des porteuses de fréquences
élevées pour que leur portée soit suffisamment grande et pour que les antennes d'émission ou de réception soient
de dimensions non encombrantes. Entre l'émetteur et le récepteur, l'onde porteuse se propage sous forme modulée.
La modulation effectuée par le signal à transmettre peut se faire de trois manières différentes. Toutefois, on
n'en traitera dans ce qui suit que deux, la modulation d'amplitude et la modulation de fréquence. » ·
« MODULATION D'AMPLITUDE — La modulation d'amplitude a été la première technique utilisée en radiodiffusion.
L'information à transmettre est convertie en une tension électrique qui va moduler l'amplitude d'une autre
tension de fréquence beaucoup plus élevée que celle de la tension modulante. Pour extraire l'information du signal
modulé transmis, il faut lui faire subir une démodulation (ou le démoduler) à sa réception. »

**Plan (titres numérotés du manuel)** — **MODULATION D'AMPLITUDE** : 1 MODULATION (p.366) — 1.1 Étude
expérimentale (1.1.1 Modulation d'une tension sinusoïdale, p.366–369 ; 1.1.2 Influence de la composante continue
de la tension modulante, p.369–371) · 1.2 Étude théorique (1.2.1 Expression de la tension de sortie, p.371 ; 1.2.2
Expression du taux de modulation, p.372 ; 1.2.3 Spectre de fréquences du signal modulé, p.372–373) · 2
DÉMODULATION (p.373) — 2.1 Détection d'enveloppe (2.1.1 Étude expérimentale ; 2.1.2 Interprétation, p.374) · 2.2
Lissage du signal (p.374–375) · 2.3 Élimination de la composante continue (p.375) · 3 AVANTAGES ET INCONVÉNIENTS
(p.376). **MODULATION DE FRÉQUENCE** (p.376) : 1 MODULATION — 1.1 Étude théorique (p.376–377) · 1.2 Étude
expérimentale (p.377) · 2 AVANTAGES ET INCONVÉNIENTS (p.377–378) · 3 FM AU QUOTIDIEN (p.378). Puis « L'essentiel »
(p.379), exercice résolu (p.380–381), « Exercices à résoudre » (p.382–385), « Fiche technique — Opérateur AD633JN »
(p.386–387), « En savoir plus — Transmission par modulation » (p.388–391).

### Cours — Activités

- **AM §1.1.1 Modulation d'une tension sinusoïdale (p.366–369)** — matériel : deux GBF dont l'un à tension de
  décalage (offset) réglable ; multiplieur AD633JN (Fig.1 brochage : 1 E₁, 2 masse, 3 E₂, 4 masse, 5 −15 V,
  6 masse, 7 sortie, 8 +15 V) ; alimentation symétrique ±15 V (Fig.2) ; oscilloscope bicourbe (numérique de
  préférence) ou système d'acquisition « VTT » (note : « acronyme d'une interface sous forme de console
  graphique », Fig.3). Réglages : **u(t) = Uo + Um cos 2πNt** avec **Uo = 4 V, Um = 2,5 V, N = 5 kHz** ;
  **up(t) = Upm cos 2πNpt** avec **Upm = 6 V, Np = 180 kHz** ; Fig.4 chronogrammes de u et up sur la console.
  Questions (VERBATIM) : « Si l'on veut simuler une modulation d'amplitude avec les tensions u(t) et up(t) : 1°)
  préciser celle qui va jouer le rôle de signal porteur tout en justifiant la réponse, 2°) donner le rôle de
  l'autre tension. » Montage Fig.5 : u(t) [+Uo] sur E₁ (broche 1), up(t) sur E₂ (broche 3) ; N.B. : alimenter le
  circuit ; broches 2, 4 et 6 à la masse ; **us(t) = k.u₁.u₂ avec k = 0,1 V⁻¹**, u₁ = u(t) + Uo [sic : u(t) inclut
  déjà Uo dans l'énoncé p.366], u₂ = up(t). Remarque : sans offset, GBF en série avec une alimentation
  stabilisée, l'un des deux à masse flottante (Fig.6 : c'est le GBF). Oscillogrammes Fig.7 : (1) u₁(t) en voie
  Y1, (2) us(t) en Y2. Questions (VERBATIM) : « 1°) A l'aide de la figure 7 : a) montrer qualitativement et de deux
  manières différentes que l'oscillogramme (1) est celui de la tension u(t). b) justifier la qualification de la
  tension de sortie comme tension modulée. c) expliquer pourquoi on dit que le chronogramme du signal modulant u(t)
  constitue l'enveloppe de celui du signal modulé us(t). 2°) Analyser le spectre de la figure 9, spectre
  caractérisant uS (obtenu avec un oscilloscope numérique) et vérifier qu'il représente le canal de transmission
  du signal u(t). » Analyse : Fig.8a porteuse, 8b signal modulant, 8c signal modulé ; **spectre Fig.9 : raies à
  N₁ = 175 kHz, N₀ = 180 kHz, N₂ = 185 kHz, hauteurs 0,75 V, 2,4 V, 0,75 V** (cohérent : A = kUpmUo = 2,4 V,
  m = 2,5/4, mA/2 = 0,75 V) ; « de fréquences respectives N₁ = Np − N, No = N [sic, lire Np] et N₂ = Np + N » ;
  « spectre de fréquence ».
- **AM §1.1.2 Influence de Uo (p.369–371)** — montage Fig.6, **Um = 4 V, Upm = 6 V, N = 5 kHz**, Uo variable ;
  oscillogrammes et spectres (oscilloscope numérique ou analyseur de fréquence, Fig.11) : **Fig.10a Uo = 13,8 V ;
  Fig.10b Uo = 4,8 V ; Fig.10c Uo = 2 V** (raies latérales de même hauteur que la centrale). Mesure graphique de m
  (Fig.12 « m = 1,98 » ; Fig.13 « Cas d'un taux de modulation m = 1 ») ; méthode du trapèze en mode XY (Fig.14 :
  petite base AD = l, grande base BC = L). Questions (VERBATIM) : « 1°) vérifier graphiquement que le taux de
  modulation m pour les figures 10a, b et c sont égaux respectivement à 0,29 ; 0,82 et 1,98. 2°) Comparer m au
  rapport Um/Uo. 3°) Quels sont les cas pour lesquels le taux de modulation est : - inférieur à 1. - égal à 1.
  - supérieur à 1. 4°) Dans le cas où Uo = 2 V, on dit que l'on a obtenu une surmodulation. Justifier cette
  affirmation en s'appuyant sur la figure 10c. » Analyse : Uo influe sur m et sur les amplitudes des raies
  latérales, pas sur les fréquences ; USm min positive → m < 1 (bonne qualité) ; nulle → m = 1 ; négative → m > 1
  surmodulation ; « Le signal modulant perd son intégrité s'il y a une surmodulation. »
- **AM §2.1.1 Détection d'enveloppe (p.373)** — condensateur, diode, résistor, oscilloscope bicourbe ; Fig.18
  « Montage redresseur et détecteur d'enveloppe » (diode D, puis C et R en parallèle entre P et M ; Y1 sur us,
  Y2 en P) ; Fig.19 : signal modulé (Y1) et signal démodulé (Y2) « de forme semblable à celle du signal modulant,
  mais avec des ondulations » ; en augmentant Np, l'enveloppe devient moins ondulée. Questions (VERBATIM) :
  « 1°) Quels sont les rôles de la diode, du condensateur et du conducteur ohmique ? 2°) Les valeurs de C et de R
  influent-elles sur l'intégrité de l'enveloppe ? »
- **AM §2.2 Lissage (p.374–375)** — dipôle R'C' entre P et M (Fig.20 : R' en série P→Q, C' entre Q et M) ;
  Fig.21 « L'enveloppe avec la composante continue ». Questions (VERBATIM) : « 1°) Expliquer le rôle du
  quadripôle R'C' de la figure 20. 2°) Montrer qu'il s'en suit la double condition : Tp ≪ R'C' ≪ T, où Tp est la
  période de la porteuse et T, la période du signal modulant. »
- **AM §2.3 Élimination de la composante continue (p.375)** — troisième étage R''C'' (Fig.22 : C'' en série Q→S,
  R'' entre S et M ; oscillogrammes avant/après). Questions (VERBATIM) : « 1°) Expliquer le rôle du quatripôle
  [sic] R"C" de la figure 22. 2°) Montrer qu'il s'en suit la condition : R"C" ≫ T »
- **FM §1.2 Étude expérimentale (p.377)** — diode varicap (Fig.24, symbole) : C = k.uᵃ avec a ≃ 1/2 ; résonateur
  (L,C) de fréquence propre N₀ = 1/(2π√LC) ; oscillateur à quartz pour la stabilité de Np ; émetteur : micro →
  « Mod » → oscillateur (LC) → ampli → antenne (Fig.25). (Aucune manipulation chiffrée : description de principe.)

### Cours — Encadrés (VERBATIM, vérifiés sur l'image)

> **Conclusion (AM §1.1.1, p.369)** — « La modulation d'amplitude peut être simulée avec la multiplication d'une
> tension de haute fréquence (la porteuse) par une tension de basse fréquence (signal modulant). Le signal de
> sortie ou signal modulé est caractérisé par une fréquence constante égale à celle de la porteuse et une
> amplitude qui varie périodiquement au cours du temps avec la période du signal modulant. Le signal modulé en
> amplitude par un signal siusoïdal [sic] de fréquence N est composé de trois signaux dont la bande de fréquence
> associée est d'une largeur double de la valeur de la fréquence N du signal modulant. »

> **Taux de modulation (p.370)** — « La modulation d'amplitude est satisfaisante lorsqu'on retrouve sur le
> chronogramme du signal modulé, toute l'information portée par le signal modulant. Pour plus de précision, on
> caractérise le phénomène par ce que l'on appelle taux de modulation. Il est noté m est [sic] s'exprime comme
> suit : **m = (USm max − USm min)/(USm max + USm min)** » ; « On peut mesurer les valeurs maximale et minimale à
> la règle puisqu'on on a un rapport de tensions. » Remarque (trapèze, mode XY) : **m = (L − l)/(L + l) = BC/AD**
> [sic : avec L = BC et l = AD, le rapport BC/AD ne donne pas m ; lire (BC − AD)/(BC + AD)].

> **Conclusion (AM §1.1.2, p.371)** — « La tension de décalage Uo influe sur le taux de modulation du signal
> modulé. La modulation est de bonne qualité lorsque la composante continue Uo du signal modulant est supérieure à
> son amplitude Um. »

> **Étude théorique (§1.2.1, p.371)** — « Soit : u(t) = Um cos 2πNt, un signal de basse fréquence N. Uo : tension
> constante de décalage ou d'offset. up(t) = Upmcos 2πNpt, un signal de haute fréquence Np. » (Fig.15 montage
> multiplieur) « La tension de sortie est de la forme : **us(t) = k.(u+Uo)up = k.(Um cos 2πNt + Uo)Upmcos 2πNpt**.
> On peut la mettre sous la forme : **us(t) = kUpmUo(1 + (Um/Uo) cos 2πNt) cos 2πNpt**. La tension de sortie a une
> fréquence Np et une amplitude qui varie au cours du temps entre Usm max et Usm min dont les expressions sont :
> **USm max = kUPmUo (1 + Um/Uo)** et **USm max [sic, lire USm min] = kUPmUo (1 − Um/Uo)** » (Fig.16 oscillogramme).

> **Expression du taux (§1.2.2, p.372)** — « En remplaçant Usm max et Usm min par leurs expressions, on obtient :
> **m = Um/Uo** » — Conclusion : « Le taux de modulation dépend de la valeur de l'amplitude du signal modulant Um
> et de celle de la tension de décalage Uo. Son expression est : m = Um/Uo » — Application : « Pour le cas de la
> figure 10a, Uo = 13,8 V et Um = 4 V, d'où m = 0,29. Pour la figure 10b, Uo = 4,8 V et Um = 4 V d'où m = 0,83.
> Pour la figure 10c, Uo = 2 V et Um = 4 V, d'où m = 2 : le signal de sortie est surmodulé. Pour le cas de la
> figure 16, en mesurant USm max et USm min, on trouve m = 0,3, d'où Uo = 13,33 V. » (valeur 0,83 vs 0,82 de la
> question p.370, et 2 vs 1,98 : écarts de mesure graphique.)

> **Spectre (§1.2.3, p.372–373)** — note : « On rappelle que : cos a.cos b = 1/2 [cos(a + b) + cos(a − b)]. »
> Démonstration : « A partir de us(t) = kUpmUo.(1+ m cos 2πNt)cos 2πNpt […] us(t) = kUpmUocos 2πNpt +
> mkUpmUocos 2πNt.cos 2πNpt. […] us(t) = kUpmUocos 2πNpt + 1/2 mkUp[sic]Uocos 2π (Np+ N)t + 1/2 mkUpmUocos 2π
> (Np − N)t. En posant A = kUpmUo, on écrit : **us(t) = A.cos2πNpt + 1/2 m A.cos2π(Np+ N)t + 1/2 m A.cos
> 2π(Np−N)t** » ; « La bande de fréquences du signal modulé est : **ΔN = (Np + N) − (Np − N) = 2N**. » (Fig.17 :
> raies A en Np, ½mA en Np − N et Np + N.) Application : « Les fréquences du spectre de la figure 10c ont la même
> amplitude. D'où A = 1/2 m A, ce qui nous donne m = 2. Attention : L'unité de A est le volt tandis que m (taux de
> modulation) est sans unité. »
> **Conclusion** : « La tension de sortie d'un signal modulé en amplitude : - est la somme de trois fonctions
> sinusoïdales d'amplitudes respectives 1/2 m A, A et 1/2 m A. (A = kUpmUo, où k est le facteur multiplieur de
> circuit intégré) - a un spectre de fréquences de bande 2N, composé de : Np − N, Np et Np + N. »

> **Démodulation — définition (§2.1, p.373)** — « A sa réception, le signal modulé doit être décortiqué pour en
> extraire l'information intacte : c'est la démodulation. Pour ce faire, il faut séparer le signal de haute
> fréquence (la porteuse) du signal de basse fréquence (l'enveloppe ou signal modulant). »

> **Interprétation (§2.1.2, p.374)** — « […] lorsque la diode est conductrice pour une alternance positive et la
> tension modulée augmente au cours du temps, le condensateur se charge à travers la résistance [sic : la charge
> se fait à travers la diode]. Pendant la même alternance, la tension modulée décroît au cours du temps, le
> condensateur se décharge à travers la résistance. Pendant l'alternance négative, la diode est bloquée, le
> condensateur continue sa décharge à travers la résistance. Ainsi, la diode impose au condensateur de suivre
> l'évolution au cours du temps de l'enveloppe supérieure. Pour suivre l'évolution de l'enveloppe, la constante
> de temps τ = R.C doit vérifier une inégalité : **Tp < τ = R.C ≪ T** T : période du signal modulant ; Tp :
> période de la porteuse. […] une bonne détection d'enveloppe (avec le minimum d'ondulations) n'est possible que
> lorsque la fréquence Np de la porteuse est très supérieure à celle du signal modulant : **Np ≫ N**. »

> **Lissage (§2.2, p.374–375)** — « Pour supprimer intégralement la porteuse de fréquence Np très supérieure à la
> fréquence N du signal modulant, il faut un filtre passe bas comme celui de la figure 20. Or, on sait qu'un tel
> filtre passif est caractérisé par la fréquence de coupure haute **Nh = 1/(2π R'C')**. Donc, Nh doit être très
> inférieure à Np tout en restant nettement supérieure à N, d'où l'inéquation, **Tp ≪ R'C' ≪ T**. »

> **Élimination de la composante continue (§2.3, p.375)** — « La tension de décalage est une tension continue,
> c'est-à-dire une tension de fréquence nulle. Pour l'éliminer, il faut alors un filtre passe haut comme celui de
> la figure 22, de fréquence de coupure basse **Nb = 1/(2π R"C")**. Pour que le signal modulant ne soit pas
> affecté, il faut que Nb soit trés inférieure à sa fréquence N, d'où la condition **R"C" ≫ T**. »

> **Conclusion (démodulation, p.375)** — « La démodulation d'un signal modulé en amplitude s'effectue en trois
> phases : - la détection d'enveloppe avec un condensateur C et un résistor R montés en parallèle tels que :
> **Tp < τ = R.C << T**, où Tp est la période de la proteuse [sic] et T, la période du signal portant
> l'information ; - le lissage du signal avec un filtre passe-bas R'C' satisfaisant la condition : **Tp ≪ R'C' ≪
> T** - l'élimination de la composante continue avec un filtre passe-haut R"C" satisfaisant la conditon [sic]
> **R"C" ≫ T**. Pour une démodulation de qualité, il faut une porteuse de fréquence très supérieure à celle du
> signal modulant : **Np ≫ N**. » Remarques : démodulation possible avec détecteur d'enveloppe + passe-haut
> seulement, de qualité inférieure ; poste AM : antenne, circuit d'accord bobine ∥ condensateur (résonateur accordé
> sur la porteuse), démodulateur ; condensateur à capacité variable pour « raccorder » la fréquence du résonateur à
> Np.

> **Avantages et inconvénients de l'AM (§3, p.376)** — avantages : « simple à mettre en oeuvre (un multiplieur) » ;
> « la largeur de bande limitée à 2N [N étant la fréquence maximale du signal à transmettre (ou signal
> modulant)] » ; démodulation « qui ne demande qu'une diode, des condensateurs et des résistors ». Inconvénients :
> « sensibilité aux parasites (les émetteurs d'ondes électromagnétiques à proximité du récepteur : au démarrage
> d'une voiture, au passage d'une motocyclette...) » ; « une grande partie de la puissance de l'émetteur sert à
> émettre la porteuse qui ne véhicule aucune information. Celle-ci, c'est-à-dire l'information, est entièrement
> véhiculée par les bandes latérales du spectre de fréquences. »

> **Modulation de fréquence — étude théorique (p.376–377)** — introduction : « Par opposition à la modulation
> d'amplitude la modulation de fréquence consiste en la modification de la fréquence et non de la porteuse [sic,
> lire : et non de l'amplitude de la porteuse] en fonction de la tension modulante. » « u(t) = Um cos 2.π.N.t est
> l'expression du signal modulant. up(t) = Upm cos 2.π.Np.t est l'expression de la porteuse. Le principe de la
> modulation de fréquence et [sic] de varier la fréquence de la porteuse en fonction de u(t) (Fig.23). Soit No la
> fréquence de la porteuse en absence de modulation. La fréquence du signal modulé en fréquence s'écrit sous la
> forme générale : **Np(t) = No + k u(t) = No + k Um cos 2π.N.t**. […] **ΔNp = Np − No = k.u(t)** : est
> l'excursion en fréquence. Sa valeur maximale est appelée excursion crête de fréquence. On appelle indice de
> modulation : **β = (Npmax − No)/N = k Um/N**. On démontre que le signal modulé en fréquence prend la forme
> générale : **us(t) = Upm cos [ 2.π.Np t + (k.Um/2.π.N) cos2.π.N t ]** » [? voir doutes : la phase correcte est
> (kUm/N)·sin 2πNt, avec No au lieu de Np]. **Conclusion** : « Un signal modulé en fréquence a : - une amplitude
> constante, c'est celle de la porteuse, - une fréquence qui varie au cours du temps. » Remarque (p.377,
> VERBATIM) : « L'étude de la démodulation de fréquence est hors programme. »

> **Avantages / inconvénients FM (p.377–378)** — avantages : très faible sensibilité aux parasites
> électromagnétiques (hautes tensions, éclairs) ; haute fidélité ; porteuse sélectionnée facilement ; « Un
> excellent rendement énergétique : la majeure partie de l'énergie est portée par le signal modulant et non par la
> porteuse. » Inconvénients : « Le signal modulé en fréquence se propage directement d'où la nécessité des relais
> d'amplification du signal » ; montage plus compliqué ; démodulation plus délicate.

> **FM au quotidien (p.378)** — modems (« mot issu de deux termes : modulation et démodulation ») en FM bas débit ;
> téléphones analogiques : code DTMF (« Dual Tone Multiple Frequency » [sic, Multi-Frequency]), FSK (« Frequency
> Shift Keying »), MFSK ; radios de la bande FM en VHF (Fig.26).

**L'essentiel (p.379, VERBATIM)** — « ■ La modulation d'amplitude consiste à modifier l'amplitude d'une onde
porteuse de fréquence très élevée par le signal à transmettre, auquel on ajoute une tension continue (appelée
tension de décalage ou d'offset). ■ Avec : u(t) = Uo + Um cos 2π N t et up(t) = Upm cos 2π Np t, la forme générale
du signal modulé en amplitude est : **uS(t) = USm cos 2πNpt, où USm = kUpmUo(1 + (Um/Uo) cos 2πN t)** ;
**USm max = kUpmUo(1 + Um/Uo)** ; **USm min = kUpmUo(1 − Um/Uo)** ■ Chaque signal modulé en amplitude est
caractérisé par son taux de modulation : **m = (USm max − USm min)/(USm max + USm min) = Um/Uo** ■ La démodulation
d'un signal transmis par modulation d'amplitude consiste en sa récupération par trois opérations successives : la
détection d'enveloppe, le lissage et l'élimination de la composante continue. ■ En modulation de fréquence,
l'amplitude de la porteuse reste constante, mais sa fréquence varie autour de la valeur No en fonction de la
fréquence N du signal modulant (Signal à transmettre). - Sa fréquence est : **Np(t) = No + K.u(t)** ; Np(t) :
fréquence de la porteuse en excursion. - L'excursion en fréquence s'écrit : **Np − No = K.u(t)**. - L'indice de
modulation s'exprime : **β = (Nmax − No)/N** »

### Exercices résolus

**Exercice résolu (p.380–381)** — Énoncé : montage multiplieur (Fig.1), u₁(t) = Uo + Um cos 2πNt, u₂ = up =
Upm cos 2πNpt, us = k.u₁.u₂ (broches 2, 4, 6 à la masse) ; seule Uo varie. Première expérience : **Uo = 4 V**,
oscillogramme Fig.2. « 1°) Préciser, sans calcul, si le signal est modulé ou surmodulé. 2°) Calculer le taux de
modulation m et en déduire la valeur de Um. 3°) A l'aide d'un analyseur de fréquence, on obtient le spectre de
fréquences du signal précédent (Fig.3). a) Etablir les expressions des amplitudes des trois fréquences du spectre.
b) Retrouver la valeur de m. c) Sachant que le pic central du spectre a une fréquence N' = 100 kHz, en déduire les
valeurs de Np et de N. » Deuxième expérience : Uo inconnue, Fig.4 (« Une division représente deux unités »). « 4°)
a) préciser, sans calcul, si on a augmenté ou on a diminué Uo. b) Calculer la nouvelle valeur de m et en déduire
Uo. »
Solution : 1°) USm min positive → m < 1, correctement modulé. 2°) **m = (16 − 8)/(16 + 8) = 0,33** ; Um = m.Uo →
**Um ≃ 1,32 V**. 3°a) us = A cos 2πNpt + ½mA cos 2π(Np + N)t + ½mA cos 2π(Np − N)t, A = kUpmUo ; pics latéraux
½mA, pic central A. 3°b) rapport central/latéral = 2/m ; longueurs 24 mm et 4 mm : 2/m = 24/4 [imprimé
« 2/m = 4/24 » sic] → « n = 0,33 » [sic, m]. 3°c) Np = N' = 100 kHz ; γ = Np/(Np − N) = 11/9 (lu sur le
spectre) → « N = (1 − 1/8) Np » [sic, lire (1 − 1/γ)·Np] ; « A.N. : Np = 18,2 kHz » [sic, lire **N = 18,2 kHz**].
4°a) surmodulation → m augmente → Uo a diminué. 4°b) **m = (21 − (−4))/(21 + (−4)) = 1,47** [imprimé « 21 (− 4) » au numérateur, sans signe moins : sic, lire
21 − (−4)] ; « m = Um/Uo, d'où
m = Uo = Um/m » [sic, Uo = Um/m] → **Uo ≃ 0,90 V**.

### Tests rapides des acquis (p.382)

- **Ex. 1 — Vrai ou faux (14 items)** : 1- signal AM de fréquence constante ; 2- la modulation translate le signal
  en hautes fréquences ; 3- la porteuse constitue l'enveloppe ; 4- fréquence du modulant supérieure à celle de la
  porteuse possible ; 5- la fréquence d'une station radio est celle de la porteuse ; 6- le spectre de la figure 1
  (petit écran : raie centrale et deux raies latérales plus petites) montre une surmodulation ; 7- le taux dépend de
  la fréquence de la porteuse ; 8- signal FM d'amplitude constante ; 9- émissions FM sensibles aux parasites ;
  10- spectre AM composé de deux pics ; 11- en FM, Np(t) = No + K.u(t) ; 12- Np − No est l'excursion en fréquence ;
  13- le modem est un modulateur et démodulateur ; 14- forme générale AM uS = USm(1 + m cosωt)cosωpt. (Réponses
  non fournies.)
- **Ex. 2 — QCM (7 questions)** : I. signal AM : a- produit de deux tensions sinusoïdales / b- somme de trois
  tensions sinusoïdales / c- amplitude constante ; II. Radio-Tunis « chaîne internationale » en FM à 92 MHz :
  a- amplitude variable / b- 92 MHz fréquence de la porteuse / c- démodulation par détecteur de crête ; III. la
  modulation peut modifier : a- l'amplitude de la porteuse / b- la fréquence du signal modulant / c- la phase du
  signal modulé ; IV. signal de la figure 2 (écran : courbes a et b, enveloppe) : a- FM / b- AM / c- surmodulation ;
  V. pour la figure 2 : a- courbe a = porteuse / b- courbe b = enveloppe / c- fréquence variable ; VI.
  us(t) = 12.cos[6.10⁸t + 5cos1250t] : a- AM / b- Np = 6.10⁸ Hz / c- modulant de pulsation ω = 1250 rad.s⁻¹ /
  d- démodulable par détecteur d'enveloppe ; VII. montage de la figure 3 (diode, C ∥ R, u₁ → u₂) : a- démodulateur
  FM / b- détecteur de crête / c- u₂(t) représente le signal modulant. (Réponses non fournies.)

### Exercices et problèmes (p.383–385) — 12 exercices au total (2 tests + 6 application + 4 synthèse)

**Exercices d'application**
- **Ex. 3** (p.383) : **u₁(t) = 20.cos[10⁵t + 10cos 6280t]** et **u₂(t) = 30[3 + 2cos 1000t].cos 20.10⁴t**. 1°) mode
  de modulation ; 2°) fréquences du modulant et de la porteuse ; 3°) taux du signal AM ; 4°) excursion de fréquence
  du signal FM ; 5°) le plus sensible aux parasites.
- **Ex. 4** (p.383) : Y1 modulant, Y2 modulé ; trapèze (écran : A, B, C, D, l, L). 1°) comment visualiser le
  trapèze ; 2°) AM ou FM ; 3°) taux.
- **Ex. 5** (p.383) : spectre AM : u (V), raie centrale à 90 kHz, ligne pointillée à 5 V, deux raies latérales
  (fréquences non graduées). 1°) fréquences du modulant et de la porteuse ; 2°) amplitudes des pics ; 3°) m.
- **Ex. 6** (p.383) : oscillogramme d'un signal modulé (enveloppe, Uo repérés). 1°) AM ou FM ; 2°) N = 10 kHz →
  fréquence de la porteuse ; 3°) m ; 4°) montage de démodulation.
- **Ex. 7** (p.383) : démoduler u₁ = U₁m(1 + m cosω₀t)cosω₁t (m < 1) avec trois montages (C''–R'' passe-haut ;
  diode + C ∥ R, u₁ → u₂ ; R'–C' passe-bas). 1°) AM ou FM ; 2°) rôle de chaque montage ; 3°) u₂ basse ou haute
  fréquence ; 4°) montage de bonne qualité.
- **Ex. 8** (p.383) : multiplieur, **Uo = 4 V, u(t) = 2cos20t, up(t) = 3cos 2000t** (Y1 sur u + Uo, Y2 sur us).
  1°) amplitude et fréquence de l'oscillogramme Y1 ; 2°) idem Y2.

**Exercices de synthèse**
- **Ex. 9** (p.384) : station AM, **λ = 1827 m**, c = 3.10⁸ m.s⁻¹. 1°) fréquence émise, signification ; 2°)
  modulant sonore 1 kHz : a) périodes ; b) détecteur d'enveloppe (diode, C ∥ R), condition **T (modulant) >
  τ = R.C >> Tp (porteuse)** [imprimé ainsi], **R = 15 kΩ** → encadrement de C ; c) choisir C dans la liste 1 pF ;
  10 pF ; 100 pF ; 1 nF ; 10 nF ; 100 nF ; 1 µF ; 10 µF ; 100 µF.
- **Ex. 10** (p.384) : AD633JN, u₁ = Uo + Um cos ωt, u₂ = Upm cos ωpt ; Y1 modulant, Y2 modulé (Fig.4 : enveloppe
  et porteuse superposées). 1°) AM ou FM ; 2°) identifier les voies ; 3°) m ; 4°) Np = 120 kHz → N.
  [« visualisseur » sic]
- **Ex. 11** (p.384) : multiplieur, u(t) + Uo et **up(t) = 2 cos10³t** ; écran VTT (trait plein et trait fin).
  1°) tensions en trait plein / fin ; 2°) branchements ; 3°) Uo, N, Np ; 4°) a) branchements pour up et us ; b)
  montrer us(t) = a(1 + cos bt)cos ct, calculer a, b, c ; 5°) m.
- **Ex. 12 — Étude de texte** (p.384–385), titré « L'oscillateur de Hertz » [sic : titre repris du ch.12 ; le texte
  porte sur AM/FM/modulation de phase, d'après Microsoft Encarta 2006] : FM mise au point dans les années 1930,
  bandes 88 à 108 MHz, son TV en FM / image en AM, UHF, numérique, multiplexage. Questions : 1°) types de modulation
  en radiodiffusion, lequel est préféré et pourquoi ; 2°) pourquoi la FM est impossible avec des porteuses
  inférieures au mégahertz ; 3°) ce qui montre que les images exigent une large bande de fréquences plus élevées ;
  4°) gamme de la télévision numérique ; 5°) le multiplexage.

### Réponses du manuel (p.397, vérifiées sur l'image)

Ex. 3 : 1°) u₁(t) : FM et u₂(t) : AM ; 2°) Np1 = 15,9 kHz ; N₁ = 999 Hz ; Np2 = 31,8 kHz ; N₂ = 159 Hz. 3°) m =
66,66 % ; 4°) Np − No = k.u(t). 5°) C'est le signal modulé en amplitude. · Ex. 4 : 1°) En utilisant le mode XY ;
2°) Modulation en amplitude ; 3°) m = 0,63 = 63 %. · Ex. 5 : 1°) Np = 90 kHz et N = ΔN/2 = 38,25 kHz ; 2°)
L'amplitude des pics latéraux est de 2,94 V ; 3°) m = 117,6 % : sur modultion [sic] d'amplitude. · Ex. 6 : 1°)
C'est une modulation en amplitude ; 2°) Np = 10.N = 100 kHz ; 3°) m = 0,294 = 29,4 % ; 4°) Voir la figure 18 du
cours. · Ex. 7 : 1°) Le premier est un filtre passe-haut ; le second est un détecteur d'enveloppe et le troisième
est un filtre passe-bas ; 2°) u₁(t) est modulée en amplitude ; 3°) de basse fréquence : signal modulant ; 4°)
Détecteur d'enveloppe, filtre passe haut, filtre passe bas [sic : l'ordre du cours est détecteur → passe-bas →
passe-haut]. · Ex. 8 : 1°) L'amplitude est 2 V et la fréquence est N = 3,18 Hz. 3°) [2°] L'amplitude est 0,6 V et
la fréquence est N = 318,3 Hz. · Ex. 9 : 1°) Np = 164,2.10⁶ Hz [sic : 3.10⁸/1827 = 164,2.10³ Hz] : fréquence de
la porteuse ; 2°a) Tp = 0,609.10⁻⁵ s ; T = 10⁻³ s ; 2°b) 0,406 nF < C << 66,66 nF ; 2°c) C = 10 nF. · Ex. 10 :
1°) Modulation en amplitude ; 2°) a correspond à Y1 et b à Y2 ; 3°) m = 60 % ; 4°) N = Np/15 = 8 kHz. · Ex. 11 :
1°) u + Uo : trait plein ; up(t) : trait fin ; 2°) u + Uo : entre broche 1 et masse. up : entre broche 3 et masse ;
3°) Uo = 1 V ; Np = 159 Hz ; N = 32,8 Hz ; 4°a) up : entre broche 3 et masse, us(t) : entre broche 7 et masse.
4°b) us(t) = k.(u+Uo)up = kUoUpm(1 + Um/Uo cosωt)cosωpt ; Um = 1 V ; Uo = 1 V ; Upm = 2 V ; a = kUoUpm = 0,2 V ;
b = 206 rad.s⁻¹ et c = 103 rad.s⁻¹ [sic : ωp = 10³ rad.s⁻¹, exposant perdu à l'impression] ; 5°) m = 1 = 100 %. ·
Ex. 12 : 1°) Modulation AM et FM ; On préfère la FM qui est moins sensible aux parasites ; 2°) La large bande
passante ; 3°) Pour la télévision, le son... tandis que l'image ...par modulation d'amplitude ; 4°) En UHF
(ultra-haute fréquence) ; 5°) Une seule fréquence porteuse transmettant plusieurs signaux. · Pas de réponse :
Ex. 1, 2.

### En savoir plus / Documents

- **Fiche technique « Opérateur AD633JN » (p.386–387)** — circuit à huit broches, trois amplificateurs
  opérationnels (Fig.1 structure interne : X1, X2, Y1, Y2, Z, W, +VS, −VS) ; broches 5 et 8 à −15 V et +15 V.
  Multiplieur : broches 2, 4, 6 à la masse, u₁ entre 1 et masse, u₂ entre 3 et masse, **uS(t) = k.u₁.u₂ avec
  k = 0,1 V⁻¹** (Fig.2) ; en AM avec offset : « us(t) = k.Upm cos 2π Npm [sic] t [Uo + Um cos 2π N t] ».
  Multiplieur-sommateur : broches 2 et 4 à la masse, u₃ sur 6 : **us(t) = k.u₁.u₂ + u₃** (Fig.3) ; AM en reliant
  la broche 3 à la broche 6 : u₂ = u₃ = Upm cos 2πNpt, u₁ = Um cos 2πNt, « us(t) = Upmcos 2π Np t.[1 +
  k.Upmcos 2π Npt] » [sic : lire 1 + k.Um cos 2πNt ; vérifié sur l'image].
- **En savoir plus « Transmission par modulation » (p.388–391, « Extraits d'un document d'Etienne Guillier »)** —
  s(t) = S(t)cos[Ωt + φ(t)] ; AM (ondes moyennes 500–2000 kHz ; exemple source 3 kHz, porteuse 600 kHz, bande
  597–603 kHz ; BLU) ; AM à porteuse supprimée s = ½kUmVm[cos(Ω − ω)t + cos(Ω + ω)t] et sa démodulation par
  multiplication ; AM avec porteuse s = A(1 + m cos ωt)cos Ωt, A(1 − m) < S(t) < A(1 + m), puissance
  P = ((Vm.Um)²/2R)(1 + m²/2) ; détecteur de crêtes (m < 1) ; détection synchrone ; importance du spectre et des
  canaux ; FM (80–110 MHz) : φ(t) = 2πk∫sm dt, s(t) = Ao cos[Ωo t + (2πkAm/ω) sin ωt], taux mf = (fmax −
  fmin)/2f ; démodulation FM (FM → AM puis détecteur) ; « V - MODULATION DE PHASE (PSK) » [numérotation sautant de
  II à V : sic], bauds vs bits/s ; conclusion. Lecture, non exigible.

### Écart avec la référence (aucune)

**Aucun chapitre de référence** dans `physique-bac-sciences-exp` ni ailleurs dans `content/` (recherche
« modulation », « démodul », « porteuse », « multiplieur » : aucun cours.md). Chapitre à **créer** intégralement.
Appuis internes possibles : sciences-exp/01 (charge/décharge du condensateur, τ = RC) pour la détection
d'enveloppe ; les chapitres filtres RC/CR de ce manuel (ch.6–7 : fréquences de coupure Nh = 1/2πRC, Nb) pour le
lissage et l'élimination de la composante continue ; ch.12 pour porteuse / canal / AM-FM qualitatifs ;
sciences-exp/03 ou ch.3 de ce manuel pour N₀ = 1/(2π√LC) (circuit d'accord, varicap).
- ✅ notions propres : multiplieur AD633JN (us = k.u₁.u₂, k = 0,1 V⁻¹) ; tension de décalage ; AM : expression
  us(t), USm max/min, taux m (définition, = Um/Uo, mesure graphique, trapèze XY), sous-/sur-modulation, spectre à
  trois raies (Np, Np ± N ; A, ½mA), bande 2N ; démodulation en trois étages (détecteur d'enveloppe
  Tp < RC ≪ T ; passe-bas Tp ≪ R'C' ≪ T ; passe-haut R''C'' ≫ T ; Np ≫ N) ; avantages/inconvénients AM et FM ;
  FM : Np(t) = No + k.u(t), excursion, indice β = kUm/N, varicap, oscillateur à quartz ; modems, DTMF/FSK.

### Bornes de scope

- ✅ **INCLUS** : AM par multiplieur (montage, rôle de l'offset, k) ; lecture d'oscillogrammes (modulant,
  porteuse, modulé, enveloppe) ; us(t) = kUpmUo(1 + m cos 2πNt)cos 2πNpt ; USm max/min ; m par mesure (formule ou
  trapèze) et par Um/Uo ; m < 1, = 1, > 1 (surmodulation) ; spectre de fréquences (trois raies, amplitudes A et
  ½mA, rapport 2/m, bande 2N), lecture de Np et N sur un spectre ; développement par cos a·cos b ; démodulation AM :
  diode + RC, conditions sur τ, lissage R'C', élimination de Uo par R''C'' (Nh, Nb), choix de C dans une liste ;
  Np ≫ N ; poste AM (antenne, circuit d'accord LC, condensateur variable) ; avantages/inconvénients AM/FM ; FM :
  Np(t) = No + k.u(t), excursion (crête), β ; identification AM/FM depuis une expression (u₁, u₂ de l'ex. 3 ;
  QCM VI) ; varicap, quartz, chaîne d'émission (schéma-bloc) ; applications (modem, DTMF, radio FM).
- ⛔ **EXCLU** : démodulation de fréquence (« hors programme », VERBATIM p.377) ; modulation de phase (« hors
  programme », ch.12 p.348 ; présente seulement en « En savoir plus ») ; expression exacte du signal FM (formule
  « on démontre » non démontrée, et fautive) ; spectre FM, règle de Carson ; puissance émise, BLU, porteuse
  supprimée, détection synchrone, PSK/bauds (« En savoir plus », lecture) ; structure interne de l'AD633JN (fiche
  technique, non exigible) ; numérique/multiplexage (texte de l'ex. 12 seulement).

### Lecture

- **Pages lues en couche texte** : 364 à 391 (28 pages) et 397 (réponses).
- **Pages lues sur l'image** (110 dpi) : 364, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 377, 379, 380, 381,
  382, 383, 384, 387, 397 (20 pages). Pages 376, 378, 385, 386 et 388–390, d'abord non vues, vérifiées sur l'image
  par la relecture R-7 (lecteur E), conformes : Fig.1 de la fiche technique (structure interne X1, X2, Y1, Y2, Z,
  W, ±VS) ; formules de l'« En savoir plus » exactes — φ(t) = 2πk∫₀ᵗ sm(t)dt, s(t) = Ao cos[Ωo t + (2πkAm/ω)
  sin ωt], mf = (fmax − fmin)/2f, P = ((Vm.Um)²/2R)(1 + m²/2) ; spectres p.389 : bandes F − f et F + f, avec la raie
  A en F pour l'AM avec porteuse. Non vues sur l'image : 365 (ouverture) et 391 (prose PSK), lisibles en texte.
- **Écarts texte/image** : ≪/≫ rendus « % » / « & » (p.374–375) ; ≃ rendu « b » (p.377, 381) ; fractions
  Um/Uo éclatées (p.371, 379) ; exposants perdus : « 10 t » pour 10⁵t et « 20.10 t » pour 20.10⁴t (ex. 3 p.383),
  « 6.108t » (QCM VI) ; « β = (Npmax − No)/N » éclaté p.377 ; symboles − perdus p.379 (« 1  Um/Uo ») ; γ perdu
  p.381 (« 4 = 11/9 ») ; colonnes entremêlées p.383–385. Tableaux : aucun.
- **Coquilles [sic]** : p.365 « DÉMODULTION » ; p.367 « alimantation » ; p.368 « No = N » (lire Np) ; p.369
  « siusoïdal » ; p.370 « m est s'exprime », « puisqu'on on a », « BC/AD » ; p.371 deuxième « USm max » (lire
  min) ; p.372 « mkUpUo » ; p.373 « multitplieur » ; p.375 « quatripôle », « proteuse », « conditon » ; p.376
  « et non de la porteuse », « même notations », « de varier » (lire est de varier) ; p.378 « Dual Tone Multiple
  Frequency », « freqency » ; p.381 « 2/m = 4/24 », « n = 0,33 », « (1 − 1/8) », « Np = 18,2 kHz », « m = Uo =
  Um/m », « lafigure » ; p.383 « shématisés » ; p.384 « visualisseur », titre de l'ex. 12 « L'oscillateur de
  Hertz » ; p.386 « Npm » ; p.387 « 1 + k.Upm cos 2πNpt » ; p.391 numérotation II → V ; p.397 « sur modultion »,
  « Np = 164,2.10⁶ Hz », « c = 103 rad.s⁻¹ », ex. 8 « 3°) ».
- **Doutes [?]** :
  - **Doute 1** — **Expression du signal FM (p.377, encadrée)** : us(t) = Upm cos[2πNpt + (kUm/2πN) cos 2πNt] ;
    avec Np(t) = No + kUm cos 2πNt, la phase vaut 2πNo t + (kUm/N) sin 2πNt (cohérent avec β = kUm/N et avec la
    formule de l'« En savoir plus » p.390). Formule du cours fautive (cos au lieu de sin, facteur 2π, Np au lieu de
    No) : ne pas la reprendre telle quelle (et elle est « démontrée » sans démonstration).
  - **Doute 2** — **Ex. 5** : la réponse N = ΔN/2 = 38,25 kHz et « pics latéraux 2,94 V » ne sont pas lisibles sur
    la figure (seules 90 kHz et 5 V sont gradués) ; m = 117,6 % = 2 × 2,94/5 cohérent entre eux. Ex. non exploitable
    sans redessiner la figure.
  - **Doute 3** — **Ex. 8 2°)** : réponse « amplitude 0,6 V » ; avec k = 0,1 V⁻¹, Upm = 3 V, Uo = 4 V, Um = 2 V,
    on attend A = kUpmUo = 1,2 V (USm max = 1,8 V, USm min = 0,6 V). 0,6 V = kUpmUm ou USm min : ambigu, à
    recalculer. 1°) Y1 = u + Uo : la réponse « amplitude 2 V » omet la composante continue 4 V.
  - **Doute 4** — **Ex. 9 1°)** : « 164,2.10⁶ Hz » → 164,2 kHz (grandes ondes, cohérent avec Tp = 6,09 μs donné en
    2°a).
  - **Doute 5** — **Exercice résolu 3°c)** : N = 18,2 kHz (imprimé « Np = 18,2 kHz ») ; le rapport 11/9 est « lu »
    sur un spectre sans graduation de fréquence.
  - **Doute 6** — **Trapèze p.370** : « m = (L − l)/(L + l) = BC/AD » — le second membre est faux.
  - **Doute 7** — **Interprétation p.374** : charge « à travers la résistance » — en réalité à travers la diode (R
    en parallèle).
  - **Doute 8** — **Avantage FM p.378** : « la majeure partie de l'énergie est portée par le signal modulant et
    non par la porteuse » ; inconvénient « se propage directement » — formulations du manuel, approximatives.
  - **Doute 9** — **Ex. 7 4°)** : ordre « détecteur, passe-haut, passe-bas » dans la réponse ≠ ordre du cours
    (détecteur → passe-bas R'C' → passe-haut R''C'').
  - **Doute 10** — Vérifiés cohérents : spectre Fig.9 (A = 2,4 V, ½mA = 0,75 V), applications m = 0,29 / 0,83 / 2,
    Uo = 13,33 V (Fig.16, avec Um = 4 V), ex. résolu (m = 0,33, Um = 1,32 V, m = 1,47, Uo = 0,90 V), ex. 3, 9
    (encadrement C), 10, 11.

---

### Pages 398–399 (sites web)

« Sites Web intéressants » : liste d'URL par rubrique — « Pour l'ensemble du programme », « Evolution de systèmes
électriques » (p.398), « Ondes » (p.399 : diffraction, spectre de la lumière, ondes progressives, modulation AM/FM,
transmissions radio). Aucune donnée pédagogique ; liens anciens (wanadoo/orange, lycos, edunet.tn), non repris.
