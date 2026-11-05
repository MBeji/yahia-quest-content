<!-- Fiche de transcription — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source unique : manuel élève officiel CNP 223433P00 (318 p.), physique, 4ème année Sciences
     expérimentales (« conforme au programme officiel de 4e année Sciences Expérimentales, publié en
     septembre 2009 », édition mise à jour et adaptée). Aucun guide enseignant au corpus pour ce
     couple ⇒ le manuel élève fait référence. Lu le 2026-11-05 depuis le Drive `cnp-officiel` :
     couche texte page par page (pdftotext -layout) et vérification sur l'image de chaque page à
     formule, encadré, tableau, oscillogramme ou schéma exploité ; page PDF = page imprimée. -->

# Physique — Bac Sciences expérimentales (`bac-sciences-exp`) · manuel officiel CNP

> **Sources (Drive `cnp-officiel`, `manuels/secondaire/c4/eleve/`)** :
>
> - **Manuel élève** : code **223433P00** (318 p.), un seul tome — 11 chapitres en trois thèmes ;
>   réponses aux exercices p.316–318.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
>   Le programme officiel ministériel n'est pas intégré au corpus (R-3) : le manuel prime.
> - **Chimie** : manuel distinct (224433P00), fiche distincte (`chimie.md`).
> - **Langue d'enseignement** : **fr**. **subject id** : `physique-bac-sciences-exp` · **gradeSlug** :
>   `bac-sciences-exp`.
> - **Notation** : chiffres occidentaux 0-9, unités SI, puissances de 10 ; « Log » désigne le
>   logarithme népérien comme dans le manuel ; les formules perdues par la couche texte (indices,
>   exposants, fractions, vecteurs) sont rétablies sur l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Sciences expérimentales. Avant-propos (p.3) : « Cet ouvrage de
physique est conforme au programme officiel de 4e année Sciences Expérimentales, publié en septembre
2009 », découpé « en onze chapitres développant les trois thèmes du programme (Evolution de systèmes
- Ondes - Physique atomique et nucléaire) ». Chaque chapitre suit le même modèle : objectifs et
prérequis, questionnements tirés du vécu quotidien, activités le plus souvent sous forme de
manipulations suivies de questions, analyses et interprétations théoriques, rubrique « L'essentiel »,
questions de contrôle rapide des acquis, **exercice résolu**, exercices d'application et de synthèse
(réponses en fin d'ouvrage), puis une fiche technique ou un « En savoir plus ».

## 2. Plan annuel (carte des chapitres = sommaire p.4–5)

> Statut de transcription par chapitre — `generation` = transcrit à profondeur de génération
> (chaque activité et exercice décrit, encadrés verbatim). La couverture de pages réelle vit dans
> `suivi/bac-sciences-exp.json`.

| #   | Thème | Chapitre | pages (PDF = imprimées) | profondeur |
| --- | ----- | -------- | ----------------------- | ---------- |
| 1 | Évolution de systèmes | Le condensateur ; le dipôle RC | 10–41 | `generation` |
| 2 | Évolution de systèmes | La bobine ; le dipôle RL | 42–77 | `generation` |
| 3 | Évolution de systèmes | Oscillations électriques libres | 78–109 | `generation` |
| 4 | Évolution de systèmes | Oscillations électriques forcées en régime sinusoïdal | 110–143 | `generation` |
| 5 | Évolution de systèmes | Oscillations libres d'un pendule élastique | 144–167 | `generation` |
| 6 | Évolution de systèmes | Oscillations mécaniques forcées en régime sinusoïdal | 168–187 | `generation` |
| 7 | Ondes | Ondes mécaniques progressives | 188–225 | `generation` |
| 8 | Ondes | Nature ondulatoire de la lumière | 226–243 | `generation` |
| 9 | Physique atomique et nucléaire | Spectre atomique | 244–269 | `generation` |
| 10 | Physique atomique et nucléaire | Le noyau atomique | 270–283 | `generation` |
| 11 | Physique atomique et nucléaire | Réactions nucléaires | 284–315 | `generation` |

## 2.1 Chapitre 1 — Le condensateur ; le dipôle RC (manuel 223433, p.10–41)

Partie du manuel : « Evolution de systèmes » (bandeau de chaque page). Le chapitre comporte deux leçons
titrées : « LE CONDENSATEUR » (p.12–20) et « LE DIPÔLE RC » (p.21–30), puis « L'essentiel » (p.31),
« Exercices » (p.32–37), « Fiche technique » (p.38–39), « En savoir plus » (p.40–41).
Notation du manuel : **« Log » désigne le logarithme népérien** (p.30, p.33 : « 2Log10 = 4,6 ») ; le
manuel écrit u_C / uc indifféremment, Q_o / Q₀, I_o / I₀.

**Objectifs (p.10, VERBATIM)** — « Réaliser la charge et la décharge d'un condensateur. » · « Reconnaitre
que l'intensité i du courant électrique est une grandeur algébrique. » · « Déterminer à l'aide de la courbe
de charge d'un condensateur, la valeur de la capacité C. » · « Déterminer graphiquement la constante de
temps τ = RC d'un dipôle RC, à partir des courbes de réponse u_C(t) ou i(t). » · « Établir l'équation
différentielle régissant, au cours du phénomène de charge d'un condensateur : - la charge instantanée q(t)
du condensateur, - la tension u(t) à ses bornes, - l'intensité i(t) du courant transitoire parcourant le
circuit. » · « Calculer l'énergie emmagasinée par un condensateur. »

**Prérequis (p.10)** — SAVOIR : définir l'intensité du courant électrique, la tension (ou d.d.p) électrique,
la quantité d'électricité, un résistor ; écrire la relation Q = I.Δt ; énoncer la loi des mailles, la loi
des noeuds, la loi d'Ohm relative à un résistor, la loi d'Ohm relative à un générateur. SAVOIR FAIRE :
distinguer entre une tension continue et une tension variable ; utiliser un oscilloscope bicourbe ; calculer
la quantité d'électricité transportée par un courant continu d'intensité I pendant une durée Δt : Q = I.Δt ;
reconnaître une tension variable alternative ; reconnaître une tension en créneaux ; appliquer la loi d'Ohm
pour un résistor ; appliquer la loi d'Ohm pour un générateur ; appliquer la loi des mailles.

**Page d'ouverture (p.11)** — titre « LE CONDENSATEUR / LE DIPÔLE RC », n° 1 ; photo d'un appareil à flash,
légende : « L'éclair lumineux de très forte intensité d'une lampe flasch d'un appareil photo se produit grâce
à un condensateur. » Questions d'accroche (VERBATIM) : « Le condensateur est un composant électrique connu
comme un réservoir d'énergie. De quelle forme d'énergie s'agit-il et qu'est-ce qui confère au condensateur
cette propriété ? » · « Quel est le principe de fonctionnement du flash d'un appareil photo ? »

**Plan (titres numérotés du manuel)** —
LE CONDENSATEUR (p.12) : 1 Définition et exemples (1.1 Définition et symbole ; 1.2 Exemples de condensateurs
usuels) · 2 Charge et décharge d'un condensateur (p.13) · 3 Charge d'un condensateur et intensité du courant
(p.14 ; 3.1 Caractère algébrique de l'intensité du courant ; 3.2 Charge q d'un condensateur ; 3.3 Relation
entre intensité i du courant et charge q d'un condensateur) · 4 Relation entre la charge q et la tension u_C
(p.15–17) · 5 Capacité d'un condensateur plan (p.18) · 6 Tension de service et tension de claquage (p.19) ·
7 Énergie emmagasinée par un condensateur (p.19–20 ; 7.1 Le condensateur est un réservoir d'énergie ;
7.2 Expression de l'énergie emmagasinée).
LE DIPÔLE RC (p.21) : 1 Réponse d'un dipôle RC à un échelon de tension (1.1 Étude expérimentale ; 1.2 Étude
théorique, p.22–24) · 2 Décharge d'un condensateur dans un résistor (p.24 ; 2.1 Étude expérimentale ;
2.2 Étude théorique) · 3 Influence des grandeurs caractéristiques d'un dipôle RC sur la durée de charge ou de
décharge d'un condensateur (p.26 ; 3.1 Influence de la résistance R ; 3.2 Influence de la capacité C ;
3.3 Constante de temps d'un dipôle RC, p.28–30, avec « Récapitulation »).

### Cours — Manipulations, expériences et questions (dans l'ordre du manuel)

**Introduction historique (p.12, VERBATIM)** — « Le condensateur est un terme introduit en 1782 par Volta
( physicien italien, 1745-1827) après avoir constaté que l'électricité “se condense” sur les surfaces en
regard de deux conducteurs quand on les approche l'un de l'autre. »

**1.2 Exemples (p.12)** — Fig.2 (photo de condensateurs) ; trois types cités : condensateurs à air (diélectrique
= air) ; à diélectrique solide (feuilles métalliques minces roulées, généralement cylindriques) ;
électrochimiques (armatures en aluminium, diélectrique = mince couche d'alumine déposée par électrolyse).
Diélectriques cités en 1.1 : air, papier imbibé d'huile de paraffine, céramique (oxyde de titane et
titanates), mica, téflon, polyéthène, alumine.

**§2 Manipulation — charge et décharge (p.13–14)** — Fig.3 : générateur de f.é.m. E, galvanomètre balistique G,
résistor R, commutateur K (positions 1 et 2), condensateur d'armatures A et B ; sur la figure, la position 1
relie E au condensateur et à G, la position 2 ferme le condensateur sur R et G [lecture du schéma : R n'est
que dans la branche 2 ?]. Observations : K en 2 d'abord → rien ; K en 1 → l'aiguille dévie d'un angle α dans
le sens 1 (Fig.4a) puis revient à zéro ; ouvrir/refermer → plus de déviation (« condensateur chargé ») ; K en
2 → déviation du même angle α dans le sens 2 puis retour lent à zéro (Fig.4b) ; ouvrir/refermer → plus de
déviation (« déchargé »). Fig.4a/4b : flèches e⁻ et i de sens opposés.
Questions : « 1°) Peut-on décharger un condensateur non chargé ? préciser, parmi les observations faites,
celle qui justifie la réponse. 2°) Expliquer les phénomènes de charge et de décharge d'un condensateur et en
déduire si l'on peut recharger un condensateur déchargé. »
Interprétation : en position 1, A et B initialement neutres reliés aux pôles (+) et (−) ; électrons de A vers
le pôle (+) et du pôle (−) vers B ; charge +q sur A, −q sur B ; (V_A − V_B) égale à la tension du générateur.
En position 2, l'attraction entre +q et −q provoque un mouvement d'électrons de B vers A à travers le résistor
(courant de sens contraire), qui cesse quand A et B redeviennent neutres.
**Conclusion (VERBATIM)** : « Le condensateur est un composant électrique capable de stocker des charges
électriques. »

**§3.1 Manipulation — caractère algébrique de i (p.14–15)** — Fig.5 : générateur idéal de f.é.m. E, résistor R,
condensateur, commutateur K, deux DEL D1 et D2 montées tête-bêche, voltmètre aux bornes du condensateur,
entrée Y d'oscilloscope sur u_R. Enregistrement (oscilloscope à mémoire ou système d'acquisition) de u_R,
K en 1 puis en 2 (Fig.6 : u_R > 0 décroissant vers 0, puis u_R < 0 croissant vers 0).
Questions : « 1°) Montrer que lorsque le commutateur K est dans la position 1, la diode D1 seulement
s'allume, tandis que lorsqu'il est dans la position 2, c'est seulement D2 qui s'allume. 2°) L'enregistrement
de la figure 6 montre que la tension u_R est positive lorsque K est en 1, négative quand il est en 2. Sachant
que u_R=Ri, montrer graphiquement qu i est positive et décroissante pendant la charge, négative et croissante
pendant la décharge. »
Interprétation : sens positif de la Fig.5 ; i > 0 pendant la charge (D1 passante), i < 0 pendant la décharge
(D2). **Conclusion** : voir Encadrés.

**§4 Manipulation — charge à courant constant (p.15–17)** — Fig.8 : générateur de courant, interrupteur K1,
ampèremètre et condensateur en série ; voltmètre numérique et interrupteur K2 aux bornes du condensateur.
« La charge q étant proportionnelle à la durée t, on a q = I.t. » Protocole : fermer puis rouvrir K2 avant
toute mesure ; fermer K1 et déclencher le chronomètre ; mesurer u_C = u_AB toutes les 5 s.
Données (I = 0,144 mA) :

| t (s) | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|---|
| u_C (V) | 0 | 1,5 | 3 | 4,6 | 6,1 | 7,6 | 9,2 |

Questions : « 1°) Que se passe-t-il quand on ferme K2 ? Quelle est l'indication du voltmètre ? 2°) Avant de
fermer K2, le voltmètre peut indiquer une tension non nulle. Expliquer cette possibilité. 3°) A l'aide du
tableau des mesures dressé, montrer que la charge q augmente avec u_C. 4°) […] on obtient le tracé de la
figure 9 ci contre. Montrer graphiquement que u_C = kt où k est une constante que l'on calculera.
5°) Déterminer la relation entre la charge q du condensateur et la tension u_C à ses bornes. »
Interprétation : Fig.9 droite passant par l'origine ; « u_C = kt avec k = 0,3 V.s⁻¹ » ; « u_C = k q/I, d'où :
q = (I/k) u_C. Comme I est constant, le quotient I/k est une constante notée C. » → **q = C u_C**.
Remarque : un autre condensateur donne la même proportionnalité avec une autre valeur de C. (Le manuel ne
calcule pas la valeur numérique de C pour cette manipulation.)

**§6 Question d'entrée (p.19, VERBATIM)** — « En plus de la valeur de la capacité du condensateur, le
constructeur indique généralement sur le boitier deux valeurs différentes de tensions électriques, que
représentent-elles? » Texte : q = C.u ne peut augmenter indéfiniment ; tension très élevée → étincelles à
travers le diélectrique, troué s'il est autre que l'air ou le vide ; crépitement ; « le condensateur a
claqué » ; « tension de claquage ou de rupture ». Définition et tension de service : voir Encadrés.

**§7.1 (p.19–20)** — le courant de décharge circule sans générateur → le condensateur chargé a joué le rôle de
générateur → réservoir d'énergie. **Expérience complémentaire** : Fig.11 : générateur de tension continue E
réglable, condensateur de très grande capacité C, petit moteur M, commutateur K ; K en 1 puis en 2 → le moteur
tourne puis s'arrête spontanément. Questions : « 1°) Qu'est ce qui montre dans cette expérience que le
condensateur est un réservoir d'énergie? 2°) Quelle est l'opération avec laquelle le condensateur est devenu
ce réservoir d'énergie?. 3°) Expliquer la petite durée de rotation du moteur. » Conclusion : voir Encadrés.

**Dipôle RC — introduction (p.21, VERBATIM)** — « Le dipôle RC est constitué d'un résistor de résistance R
associé en série avec un condensateur de capacité C. On se propose d'étudier la variation de la charge q du
condensateur en fonction du temps dans un tel dipôle lorsque la tension à ses bornes passe brusquement de
zéro à une valeur constante E ou inversement. L'évolution brusque de la tension constitue l'échelon de
tension. »

**RC §1.1 Manipulation — réponse à un échelon (p.21)** — Fig.12 : C, R et générateur de tension continue E en
série, commutateur K (1/2). Fig.13 : points D (côté R), A (entre R et C), B (masse) ; Y1 relié en D (donc u_DB),
Y2 relié en A (u_AB) ; flèches u_DA et u_AB dessinées ; oscilloscope numérique à mémoire. K en 1 → Fig.14
(oscillogramme : u_C croissant puis palier).
Questions : « 1°) Identifier la courbe obtenue sur la voie Y1 de l'oscilloscope et celle obtenue sur la voie
Y2. 2°) La charge du condensateur est-elle instantanée ? » Interprétation : avant fermeture u_C = 0 ; K en 1 →
u_DB = E ; u_AB croît progressivement jusqu'à E ; q = C u_AB évolue de même. Conclusion : voir Encadrés.
[Fig.14 ne montre nettement qu'une courbe croissante avec palier ; la trace de u_DB = E n'est pas
distinguable sur l'image.]

**RC §1.2 Étude théorique — charge (p.22–23)** — Fig.15 : circuit de charge (D–R–A–C–B, générateur E, flèches
u_DA, u_AB, i). Mise en équation, solution, expressions : voir Encadrés.
Remarque (p.23) : sans oscilloscope à mémoire ni système d'acquisition, on peut utiliser dans le montage de
la Fig.12 un **générateur basse fréquence délivrant une tension en créneaux** à la place du générateur de
tension continue.
Visualisation simultanée de u_C(t) et i(t) (Fig.19–20) : générateur de tension de **masse flottante** (ou
branché au secteur via un transformateur d'isolement), f.é.m. E, interrupteur K, dipôle RC en série ; masse en
A ; Y1 : u_DA = Ri ; Y2 : u_AB « au lieu de u_BA et ce, en appuyant sur le bouton INV » ; Fig.20 :
oscillogrammes (1) décroissant et (2) croissant.
Question (p.24) : « Dans la figure 20, montrer que l'oscillogramme (1) représente la tension u_DA aux bornes du
résistor et que l'oscillogramme (2) représente la tension u_AB aux bornes du condensateur. »

**RC §2.1 Manipulation — décharge (p.24)** — même montage (Fig.13), condensateur préalablement chargé, K en 2 :
condensateur fermé sur R ; Y2 → Fig.21 (u_C décroissant vers 0). Questions : « 1°) Expliquer l'allure de
u_C(t). 2°) La décharge du condensateur est-elle instantanée? » Interprétation : u_C = E avant ; décroît car
l'énergie emmagasinée est progressivement dissipée dans le résistor ; q = C u_C s'annule. Conclusion : voir
Encadrés.

**RC §2.2 Étude théorique — décharge (p.24–26)** — Fig.22 (C fermé sur R, flèches u_C, u_R, i). Équations et
solutions : voir Encadrés. Remarque (p.26) : visualisation simultanée lors de la décharge (Fig.26) : générateur
E [note marginale : « Pour que l'opération soit possible, le générateur doit être à masse flottante. »],
dipôle RC, commutateur K ; masse en A ; Y1 : oscillogramme (1) de la Fig.27 = u_DA, « positive lors de la
charge, est devenue négative » ; Y2 : oscillogramme (2) = u_AB (u_BA changée de signe), positive, diminue
jusqu'à s'annuler.

**RC §3.1 Manipulation — influence de R (p.26–27)** — montage Fig.13 avec B à la masse, A sur Y1 (u_C), D sur
Y2 (u_DB) (Fig.28). E = 6 V ; C = 1 μF ; R1 = 5 kΩ, R2 = 10 kΩ, R3 = 15 kΩ, R4 = 20 kΩ ; sensibilités 5 ms/div
et 1 V/div ; Fig.29a–d (quatre oscillogrammes de charge).
Questions : « 1°) Dresser un tableau consignant les durées t au bout des quelles la tension u_C(t) a atteint
la valeur 4V par exemple. » (tableau vide R (kΩ) 5 / 10 / 15 / 20 ; t (ms) à remplir) « 2°) À l'aide des
résultats trouvés : préciser qualitativement l'influence de la valeur de la résistance sur la durée t de la
charge du condensateur. montrer que la durée t est proportionnelle à R. » (Valeurs non fournies par le manuel.)

**RC §3.2 Manipulation — influence de C (p.28)** — même expérience, R = 10 kΩ ; C1 = 0,5 μF, C2 = 2 μF,
C3 = 5 μF, C4 = 10 μF ; sensibilité verticale 1 V/div ; horizontale 5 ms/div (Fig.30a, 30b) et 50 ms/div
(Fig.30c, 30d). Questions : même tableau (C (μF) 0,5 / 2 / 5 / 10 ; t (ms)) pour u_C = 4 V ; influence
qualitative de C ; « montrer que la durée t est proportionnelle à la capacité C ». Remarque : « Les mêmes
expériences, faites avec la décharge d'un condensateur, conduisent aux mêmes résultats. »

**RC §3.3 Constante de temps (p.28–30)** — Notion : toute valeur de q atteinte au bout d'une durée
proportionnelle à R (C constant) et à C (R constant) → proportionnelle au produit RC, « constante de temps,
notée τ » ; analyse dimensionnelle : R = tension/intensité, C = charge/tension → RC = charge/intensité = un
temps. Question (p.28) : « Tant au cours de la charge qu'au cours de la décharge, u_C(t) est une fonction
exponentielle du temps d'exposant (- t/τ). En déduire que τ = RC ne peut avoir effectivement que la dimension
d'un temps. » Question (p.30) : « Montrer que l'intersection de la tangente à la courbe i(t) avec l'axe des
abscisses donne t = τ (Fig.35a et Fig.35b) ». Question (p.30) : « Montrer que les mêmes durées 4,6 τ et 6,9 τ
sont indispensables pour décharger complètement un condensateur respectivement à 1 % et à 1 ‰ près. »
Détermination de τ, intérêt pratique, récapitulation : voir Encadrés.

### Encadrés, définitions, lois et relations (VERBATIM, vérifiés sur l'image de leur page)

> **Définition (1.1, p.12)** — « Un condensateur est un composant électrique constitué de deux plaques
> conductrices trés faiblement espacées et séparées par un isolant électrique. Les plaques sont désignées par
> les armatures du condensateur et le matériau isolant est appelé diélectrique. Le condensateur est
> symboliquement représenté par deux traits parallèles qui représentent les armatures (Fig.1). » […] « Étant
> un dipôle électrocinétique, le condensateur a deux bornes reliées directement à ses armatures. Dans le cas
> où les armatres sont planes et parallèles, le condensateur est dit plan. » (Fig.1 : symbole, légendes
> « Armatures », « Diélectrique ».)

> **Conclusion (§3.1, p.15)** — « L'intensité du courant électrique est une grandeur algébrique. Elle est
> positive si le courant circule dans le sens arbitraire choisi et négative si le courant circule dans le
> sens contraire. »

> **Définition (§3.2, p.15)** — « On appelle charge q d'un condensateur, la charge de l'une de ses armatures
> choisie conventionnellement, celle vers laquelle est orienté le sens positif du courant. » Note marginale :
> « Ne pas confondre entre la charge q d'un condensateur et le phénomène de charge ». (Fig.7 : i entrant vers
> l'armature A portant +q, B portant −q.)

> **Relation i–q (§3.3, p.15, encadré)** — « Entre les instants t et t+Δt, le courant circulant dans le sens
> positif, transporte la quantité d'électricité Δq>0, ce qui fait augmenter la charge de l'armature A de Δq.
> L'intensité du courant étant la quantité d'électricité transportée (ou traversant une section droite) par
> unité de temps, on a : » **i(t) = lim_{Δt→0} Δq/Δt = dq/dt**

> **Relation charge–tension (§4, p.17, encadré)** — « On a ainsi : **q = C u_C** »

> **Capacité (p.17)** — « La charge q d'un condensateur est proportionnelle à la tension u_C à ses bornes :
> q = C u_C. Le facteur de proportionnalité C est une grandeur qui caractérise l'aptitude du condensateur à
> emmagasiner une charge électrique q lorsqu'il est soumis à une tension u_C, appelée capacité du
> condensateur. C ne dépend que des caractéristiques géométriques du condensateur et de la nature du
> diélectrique. »

> **Unité et ordres de grandeur (p.17)** — « La capacité C d'un condensateur est une grandeur mesurable. Dans
> le système international d'unités, elle s'exprime en Farad (F). Le farad est la capacité d'un condensateur
> qui, soumis à une différence de potentiel de 1 V, prend une charge de 1 C. » […] « le farad est une grande
> unité de capacité. » Sous-multiples : « 1 mF = 10⁻³ F ; 1 μF = 10⁻⁶ F ; 1 nF = 10⁻⁹ F ; 1 pF = 10⁻¹² F ;
> 1 fF = 10⁻¹⁵ F ». Note marginale : unité dédiée à Michael Faraday (physicien et chimiste anglais,
> 1791-1867). Tableau : électrochimique μF - F ; mica, céramique pF - nF ; papier μF ; tantale
> 0,1 μF - 0,01 μF ; polypropylène nF - μF.

> **Condensateur plan (§5, p.18)** — « La capacité d'un condensateur plan est proportionnelle à la surface S
> des armatures en regard et inversement proportionnelle à l'écartement e de ses armatures (Fig.10). On peut
> écrire : » **C = ε S/e** — « Le facteur de proportinnalité ε est une constante qui ne dépend que de la
> nature du diélectrique, on l'appelle permittivité absolue du diélectrique. Dans le système international
> d'unités, ε s'exprime en farads par mètre. La permittivité ε_o du vide est : » **ε_o = 1/(36π.10⁹)
> (F.m⁻¹)** — « La permittivité de l'air est pratiquement égale à celle du vide. Tous les autres diélectriques
> ont une permittivité absolue plus grande que celle du vide. » « permittivité relative ε_r […] rapport de sa
> permittivité absolue sur la permittivité du vide : » **ε_r = ε/ε₀ d'où C = ε_r ε_o S/e**.
> Tableau (ε_r ; ε en 10⁻¹¹ F.m⁻¹) : Vide, air 1 ; 0,885 · Papier paraffiné 2 - 2,5 ; 1,8 - 2,2 ·
> Polystyrène 2-3 ; 1,8 -2,7 · Verre 4-7 ; 3,5 - 6,2 · Mica 5-8 ; 4,4 - 7,1 · Céramique 15 - 2500 ; 13,2 - 2200.

> **Définition (§6, p.19)** — « On appelle tension de claquage d'un condensateur la plus petite tension (en
> valeur absolue) faisant jaillir une étincelle entre les armatures du condensateur. » Suite : « La deuxième
> valeur de tension indiquée sur le boitier d'un condensateur est appelée tension de service, elle est d'une
> valeur nettement inférieure à celle de claquage, c'est la tension nominale du composant. »

> **Conclusion (§7.1, p.20)** — « Le condensateur est un réservoir d'énergie potentielle électrique (ou
> électrostatique). Cette énergie se manifeste, lors de la décharge du condensateur, en se transformant en
> énergie thermique dans les différents conducteurs, en énergie cinétique dans un moteur, en énergie
> lumineuse dans une diode LED par exemple... »

> **Énergie (§7.2, p.20)** — « L'énergie électrostatique emmagasinée par un condensateur de capacité C,
> chargé sous une tension u, s'exprime par : » **E_C = ½ C u²** — « Avec C en farad et u en volt, E_C
> s'exprime en joule. En utilisant la relation q = C.u, on obtient d'autres expressions de E_C soit : »
> **E_C = q²/(2C) = ½ q u**. (Formule donnée, non démontrée.)

> **Conclusion (RC §1.1, p.21)** — « La réponse d'un dipôle RC à un échelon de tension est la charge du
> condensateur. N'étant pas instantanée, celle-ci constitue un phénomène transitoire. »

> **Mise en équation — charge (p.22)** — « En régime transitoire et pendant que le condensateur se charge, le
> circuit de la figure 12 est équivalent à celui de la figure 15. Appliquons la loi des mailles à ce
> circuit : u_DA + u_AB − E = 0, soit : Ri + u_C − E = 0. Or, i = dq/dt = C du_C/dt, d'où :
> **u_C + RC du_C/dt = E (1)** ou bien : **du_C/dt + (1/τ) u_C = E/τ avec τ = RC**, équation différentielle en
> u_C avec second membre non nul. Avec u_C = q/C et i = dq/dt, la même équation différentielle s'écrit :
> **dq/dt + (1/τ) q = E/R (2)** ou **i + (1/τ) ∫ i dt = E/R (3).** »

> **Expression de u_C(t) — charge (p.22)** — « La solution de l'équation différentielle (1) est de la forme :
> u_C(t) = B + Ae^{−αt} où A, B et α sont des constantes à déterminer. A t = 0, u_C = A + B = 0, d'où B = − A.
> Il vient u_C(t) = A(e^{−αt} − 1). La dérivée de u_C(t) par rapport au temps s'écrit : du_C/dt = − αAe^{−αt}.
> En remplaçant du_C/dt par son expression dans l'équation (1), on trouve : A(e^{−αt} − 1) − ατAe^{−αt} = E ;
> ce qui donne : − A + (1 − ατ)Ae^{−αt} = E. En égalisant membre à membre cette équation qui doit être
> satisfaite pour toute valeur de t, on obtient : A = − E et 1 − ατ = 0 d'où α = 1/τ. Ainsi, avec A = − E et
> α = 1/τ, la tension aux bornes du condensateur s'écrit : **u_C(t) = E(1 − e^{−t/τ})**. » (Fig.16 : courbe
> croissante, asymptote E.)

> **Expression de q(t) — charge (p.23)** — « L'expression de la charge q du condensateur est
> q(t)= C.u_C(t), d'où : **q(t) = Q₀(1 − e^{−t/τ}) avec Q₀ = CE.** » « Lorsque t tend vers l'infini u_C(t) tend
> vers E et q vers q_o, le condensateur porte sa charge maximale. » (Fig.17.)

> **Expression de i(t) — charge (p.23)** — « On a i = dq/dt. En remplaçant q par son expression, on trouve
> i(t) = (Q_o/τ) e^{−t/τ} ou encore : **i(t) = I_o e^{−t/τ} avec I_o = E/R** » ; « L'intensité i du courant est
> alors positive au cours de la charge du condensateur, résultat attendu du fait que le sens positif du
> courant est orienté vers l'armature située dans le circuit du côté du pôle positif du générateur. »
> (Fig.18 : décroissance de I_o vers 0.)

> **Conclusion (RC §2.1, p.24)** — « Dans un dipôle RC, un condensateur chargé se décharge progressivement
> dans le résistor. »

> **Mise en équation — décharge (p.24–25)** — « Le condensateur étant initialement chargé, à l'instant t = 0,
> la tension à ses bornes est égale à E. […] Avec l'orientation choisie pour le circuit, on peut écrire :
> u_C + u_R = 0 et u_R = Ri d'où u_C + Ri = 0. Or, i = dq/dt et q = Cu_C, on aura :
> **u_C + RC du_C/dt = 0** ou bien **du_C/dt + (1/τ) u_C = 0 (4).** On obtient une équation différentielle en
> u_C sans second membre. On obtient aussi les équations différentielles (5) et (6) respectivement en q et en
> i : **dq/dt + (1/τ) q = 0 (5) ; i + (1/τ) ∫ i dt = 0 (6).** »

> **Expression de u_C(t) — décharge (p.25)** — « La solution de l'équation différentielle (4) est de la
> forme : u_C(t) = A e^{−αt} où les constantes A et α sont déterminées par les conditions initiales : A t = 0,
> u_C = E, d'où A = E. En remplaçant u_C et du_C/dt par leurs expressions dans (4), on obtient :
> − α A e^{−αt} + (1/τ) A e^{−αt} = 0, ce qui entraine : (− α + 1/τ)A e^{−αt} = 0 ∀t. D'où − α + 1/τ = 0, ce
> qui donne : α = 1/τ. Il vient finalement : **u_C(t) = E e^{−t/τ}** » (Fig.23).

> **Expression de q(t) — décharge (p.25)** — « **q(t) = Q_o e^{−t/τ} avec Q_o = CE** » ; « Lorsque t tend vers
> l'infini, q tend vers zéro ; le condensateur est déchargé. » (Fig.24.)

> **Expression de i(t) — décharge (p.26)** — « On a : i = dq/dt, donc : i(t) = − (E/R) e^{−t/τ} ou encore :
> **i(t) = − I_o e^{−t/τ} avec I_o = E/R** » ; « On note bien pour i(t) le signe contraire de celui de
> l'intensité du courant de charge, c'est à dire que le courant de décharge circule dans le sens contraire de
> celui de charge (Fig.25). » (Fig.25 : i part de −I_o et croît vers 0.)

> **Constante de temps (p.28, encadré)** — « **τ = RC : constante de temps** »

> **Définition (p.29)** — « La constante de temps τ est une grandeur caractéristique du dipôle RC, elle
> renseigne sur la rapidité avec laquelle s'établit la tension u_C = E entre les armatures du condensateur.
> La charge et la décharge du condensateur sont d'autant plus rapides que la constatnte de temps τ est plus
> petite. »

> **Détermination de τ (p.29–30)** — « Par calcul direct : Connaissant les valeurs de C et de R, on peut
> calculer directement la valeur de la constante de temps τ = RC. » · « Détermination graphique (première
> méthode) : Pour déterminer τ, on trace la tangente à la courbe de charge ou de décharge u_C(t) au point
> d'abscisse t = 0. Cette tangente a pour équation u_C = a t, a étant son coefficient directeur dont la valeur
> est donnée par : a = (du_C/dt)_{t=0}. Or : du_C/dt = (E/τ) e^{−t/τ}, alors (du_C/dt)_{t=0} = E/τ. Finalement,
> l'équation de la tangente s'écrit : u_C = E t/τ. L'intersection de cette tangente avec la droite u_C = E
> donne t = τ (fig.31). » Remarque : « La même méthode […] s'applique à la courbe de décharge. L'intersection
> de la tangente à la courbe u_C(t) à l'origine avec l'axe des abscisses donne t = τ (fig.32). » ·
> « Détermination graphique (deuxième méthode) : Dans le cas de la charge du condensateur, en remplaçant t
> par τ dans l'expression de u_C(t), on obtient : u_C = E(1−e⁻¹) = 0,63 E. Donc, par lecture graphique de
> l'abscisse du point de la courbe u_C(t) d'ordonnée 0,63E, on obtient la valeur de τ (Fig.33). τ correspond
> donc au temps nécessaire pour charger un condensateur à 63%. Dans le cas de la décharge, […] on obtient
> u_C = E e⁻¹ = 0,37E. τ est alors l'abscisse du point de la courbe u_C(t) d'ordonnée 0,37E (Fig.34). »
> Remarque : « On peut déterminer τ en traçant la tangente à la courbe i(t) au point d'abscisse t = 0. »
> (Fig.35a charge : tangente depuis I_o ; Fig.35b décharge : tangente depuis −I_o.)

> **Intérêt pratique de τ (p.30)** — u_C atteint E (charge) ou 0 (décharge) au bout de durées infinies, « ce
> qui n'est pas physiquement pratique. On admet alors que le condensateur est complètement chargé ou déchargé
> quand la différence relative entre la valeur atteinte par u_C et la valeur asymptotique E (pour la charge)
> ou zéro (pour la décharge) ne dépasse pas 1%. Pour la charge par exemple : (E − u_C)/E ≤ 1% ce qui signifie
> que E − u_C ≤ 0,01 E d'où u_C ≥ 0,99 E. Or, u_C = E(1 − e^{−t/τ}). Donc, pour t_c = t_charge, on a :
> 0,99E = E(1 − e^{−t/τ}) d'où 0,99 = (1 − e^{−t/τ}), ce qui entraine e^{−t/τ} = 0,01, d'où Log e^{−t/τ} =
> Log 0,01 ou bien t_c/τ = 2Log10 = 4,6, d'où **t_c ≃ 5 τ**. Quand l'étude se veut plus précise, on exige une
> erreur relative ne dépassant pas 1‰. Avec un calcul semblable au précédent, on aboutit à t_c = 6,9 τ ≃ 7 τ
> pour avoir u_C = 0,999 E. »

> **Récapitulation (p.30, tableau)** — Durée t : 0 | τ | 4,6 τ | 6,9 τ — Charge u_C : 0 | 0,63 E | 0,99 E |
> 0,999 E — Décharge u_C : E | 0,37 E | 0,01 E | 0,001 E.

### L'essentiel (p.31, VERBATIM)

« ■ Un condensateur est un ensemble de deux plaques conductrices séparées par un isolant. Il se charge
lorsqu'on établit entre ses bornes une tension continue et se décharge lorsqu'on le ferme sur un récepteur.
■ En désignant par q la charge portée par l'armature du condensateur vers laquelle est orienté le sens
positif du courant, on a : **i = dq/dt** ■ La capacité C est une grandeur mesurable caractérisant la faculté
d'un condensateur à stocker une charge q sous une tension u : **q = C.u** ■ La capacité C d'un condensateur
plan est proportionnelle à la surface S en regard des armatures et inversement proportionnelle à la distance
e qui les sépare : **C = e S/e** [sic : imprimé « e » au lieu de ε, lire C = ε S/e] où ε est la permittivité
absolue du diélectrique. ■ Sous une tension u, un condensateur de capacité C emmagasine une énergie
potentielle électrique : **E_C = ½ C u²** ■ Toute décharge d'un condensateur s'explique par une restitution
d'énergie emmagasinée. ■ Un dipôle RC soumis à un échelon de tension E répond par une évolution de la tension
u_C aux bornes du condensateur régie par la loi : **u_C(t) = E(1 − e^{−t/τ})** où τ = RC est la constante de
temps du dipôle. ■ Quand un dipôle RC chargé est fermé sur lui même, la tension u_C aux bornes du
condensateur, initialement égale à E, évolue selon la loi : **u_C(t) = E e^{−t/τ}** ■ La constante de temps
τ = RC renseigne sur la rapidité de la charge et de la décharge du condensateur. »

### Exercice résolu (p.32–33)

**Énoncé** — Fig.1 : générateur E, R1, commutateur K (1 : charge à travers R1 ; 2 : décharge dans R2),
condensateur C ; acquisition par ordinateur, capteur, interface. « 1°) En plaçant le commutateur dans la
position 1, on obtient la courbe u_C(t) de la figure 2. a) Interpréter l'allure de la courbe u_C(t) de la
figure 2. b) Déterminer graphiquement le temps mis par le condensateur pour se charger. Pour cela on suppose
que le condensateur est complètement chargé quand u_C = E à 1% près. 2°) On bascule le commutateur dans la
position 2, le condensateur se décharge complètement dans le résistor de résistance R2 = 1 kΩ au bout d'une
durée t = 250 ms. La courbe de décharge u_C(t) est représentée sur la figure 3. a) Interpréter l'allure […].
b) Déterminer graphiquement la constante de temps τ2 et en déduire la valeur de la capacité C du
condensateur. 3°) Déterminer la valeur de la résistance R1. » Fig.2 : u_C (V) 0 → 6 (graduations 2, 4, 6),
t (s) 0,2 … 0,8 ; Fig.3 : u_C part de 6 V, t (ms) 50 … 200. (E = 6 V se lit sur les figures ; l'énoncé ne le
donne pas en clair.)
**Solution** — 1°a) loi des mailles u_C + u_R1 − E = 0 ; u_R1 = R1 i, u_C = q/C, i = dq/dt →
τ1 du_C/dt + u_C = E, τ1 = R1C ; solution u_C(t) = E(1 − e^{−t/τ1}) ; à t = 0, u_C = 0 ; u_C augmente
exponentiellement vers E. 1°b) θ durée de charge complète : u_C(θ) = 0,99 E → θ/τ1 = 2 log10, θ = 4,6 τ1 ≃ 5 τ1 ;
tangente à l'origine, intersection P avec l'asymptote u = E projetée sur l'axe des temps → **τ1 = 0,1 s, donc
θ = 0,5 s**. 2°a) loi des mailles u_C + u_R2 = 0 ; q/C + R2 i = 0 → τ2 du_C/dt + u_C = 0 [imprimé « où
τ1 = R2C » : coquille, lire τ2 = R2C] ; u_C(t) = E.e^{−t/τ2} ; à t = 0, u_C = E ; décroissance exponentielle vers
zéro. 2°b) tangente à la courbe de décharge → **τ2 = 50 ms** ; τ2 = R2C, C = τ2/R2 → **C = 50 μF**.
3°) τ1 = R1C, R1 = τ1/C → **R1 = 2 kΩ**.

### Exercices à résoudre (p.34–37) — 13 exercices

**Tests rapides des acquis**
- **Ex. 1 — Items « vrai ou faux »** (p.34) : 1. chargé sous U → q = CU ; 2. caractérisé par sa capacité ;
  3. « ne restitue jamais la même quantité d'énergie emmagasinée » ; 4. i = dq/dt ; 5. pendant la charge, i
  maximale au début et nulle à la fin ; 6. intensité maximale du courant de charge = E/R ; 7. au début de la
  décharge, i nulle ; 8. τ par la tangente à l'origine à la courbe de décharge u_C(t) et son intersection avec
  l'axe des abscisses ; 9. « Un condensateur de charge 2q emmagasine l'énergie : E_C = q²/2C ». (Réponses non
  fournies.)
- **Ex. 2 — QCM** (p.34) : I. chargé 5 s par I = 1,2 mA → Q = a- 8.10⁻³ C / b- 6.10⁻³ C / c- 5.10⁻³ C ;
  II. q quadruplée quand : a- tension 2 fois plus grande / b- tension 4 fois plus grande / c- capacité 4 fois
  plus petite ; III. C = 10 μF, τ = 2 ms → R = a- 20 Ω / b- 200 Ω / c- 2000 Ω ; IV. τ = durée au bout de laquelle
  le condensateur est a- complètement chargé / b- à moitié chargé / c- chargé à 63 % ; V. ralentir la décharge
  avec R réglable : a- diminuer R / b- augmenter la constante de temps tout en augmentant R / c- diminuer la
  constante de temps tout en diminuant R ; VI. énergie doublée quand on double a- la charge q / b- sa capacité
  C / c- la tension u. (Réponses non fournies.)

**Exercices d'application**
- **Ex. 3** (p.35) : condensateur plan, S = 1 m², ε_r = 8, e = 0,1 mm. 1°) C ; 2°) énergie sous 50 V.
  Réponse p.316 : **1°) 0.7 μF, 2°) 8.8 10⁻³ J** [? voir doutes : le recalcul donne ≈ 8,8·10⁻⁴ J].
- **Ex. 4** (p.35) : C = 20 μF initialement non chargé, générateur de courant I = 1,8 μA. 1°) q après 10 s ;
  2°) a) u_AB à t = 10 s ; b) énergie à t = 10 s. Réponse : **1°) 18 μC [imprimé « μc »], 2°) a) 0.9 V,
  b) 8.1 10⁻⁶ J**.
- **Ex. 5** (p.35) : C = 3 μF, R = 80 kΩ, E = 12 V. 1°) τ ; 2°) a) u_C après 2 s ; b) i après 2 s. Réponse :
  **1°) 0.24 s, 2°) a) 12 V, b) 3.6 10⁻⁸ A**.
- **Ex. 6** (p.35) : E = 6 V, C = 2 μF, R = 10 kΩ, interrupteur K. 1°) i à la fermeture ; 2°) τ ; 3°) durée pour
  u_C = 0,99 E ; 4°) allure de u_C(t). Réponse : **1°) 6 10⁻⁴ A, 2°) 20 ms, 3°) 92 ms**.
- **Ex. 7** (p.35) : charge avec R = 100 Ω, E = 5 V ; tableau t (μs) 0 ; 0,5 ; 1 ; 1,5 ; 2 ; 3 ; 4 ; 5 —
  u_C (V) 0 ; 2,2 ; 3,3 ; 4 ; 4,3 ; 4,7 ; 4,8 ; 4,9. 1°) schéma ; 2°) graphe ; 3°) τ graphiquement ; 4°) C.
  Réponse : **3°) 1 μs, 4°) 10⁻⁸ F**.
- **Ex. 8** (p.35) : équation **0,12 dq/dt + q = 12.10⁻⁵** (générateur E + dipôle RC). 1°) τ ; 2°) E = 12 V →
  R ; 3°) C. Réponse : **1°) 0.12 s, 2°) 12 kΩ, 3°) 10 μF**.

**Exercices de synthèse**
- **Ex. 9** (p.35–36) : E, R, C = 10 μF en série. 1°) schéma et connexions oscilloscope pour u_C(t) et u_R(t) ;
  2°) identifier les oscillogrammes (figure : « Courbe (a) » croissante vers 12 V, « Courbe (b) » décroissante
  depuis 12 V ; u (V) 0–12 par 2, t (ms) 100–400) ; 3°) E et τ ; 4°) R. Réponse : **3°) 12 V, 150 ms,
  4°) 15 kΩ**.
- **Ex. 10** (p.36) : C = 22 μF, E = 6 V (alimentation stabilisée), R = 1 kΩ ; condensateur déchargé à t = 0,
  on ferme K (schéma : générateur bornes N, P ; K ; D–C–B–R–A). 1°) q charge de l'armature B : sens positif
  pour i = dq/dt ; 2°) équation différentielle en q(t) ; 3°) solution q(t) = α.(1 − e^{−t/β}) : a) expressions
  et valeurs de α et β ; b) i(t) ; 4°) a) instant t_{1/2} où q = ½.C.E, le comparer à τ ; b) instant où
  q = CE/4. (Pas de réponse p.316.)
- **Ex. 11** (p.36–37) : C et R en série, commutateur K (1 : générateur E ; 2 : décharge), points A, B, G,
  interface + ordinateur ; K en 1 depuis longtemps ; courbe u (V) décroissante depuis 5 V, t (ms) 0–80.
  1°) état du condensateur à t = 0 (K en 2) ; 2°) à quoi correspond la courbe ; 3°) manipulation à effectuer ;
  4°) signe de i pendant la décharge ; 5°) relations i–u_BG, q_A–u_AB, i–q_A, u_BG–u_AB ; 6°) montrer
  (1/α) du_AB/dt + U_AB = 0 [imprimé « U_AB »], α à exprimer. (Pas de réponse.)
- **Ex. 12** (p.37) : C = 5 μF chargé sous u_AB = U_o > 0 ; réglages 2,5 ms/div et 2 V/div ; fermeture à t = 0.
  1°) équation différentielle en u_AB ; 2°) R1 = 500 Ω → courbe 1, R2 → courbe 2 (graphe sans valeurs
  numériques, seules les graduations) : a) U_o ; b) résistance la plus grande, méthode et calcul de R2 ;
  3°) a) énergie emmagasinée ; b) énergie E1 dissipée par effet Joule dans R1 en fin de décharge ; c) E1
  varie-t-elle si R1 → R2 ? (Pas de réponse.)
- **Ex. 13 — Étude de texte « Le défibrillateur cardiaque »** (p.37) : circuit « à choc exponentiel tronqué »,
  C = 32.10⁻⁶ F, U ≈ 5 kV, libération en une dizaine de millisecondes, résistance du thorax ≈ 75 Ω (adulte).
  1°) assimiler à un circuit RC ; 2°) τ ; 3°) ordre de grandeur de l'énergie ; 4°) expliquer « circuit à choc
  exponentiel tronqué ». (Pas de réponse.)

**Fiche technique (p.38–39)** — « Mesure d'une tension continue aux bornes d'un condensateur » : voltmètre de
résistance R_v décharge le condensateur avec la constante R_vC (numérique ≈ 10 MΩ ; aiguille ≈ 20 kΩ/V, soit
200 kΩ sur 10 V ; ex. C = 5600 μF → 56000 s ; suiveur de tension TL081 ≈ 10¹² Ω, ex. C = 10 nF → 10⁴ s) ;
oscilloscope (1 MΩ, 50 pF), R = 20 kΩ, C = 125 nF : u = R_osc/(R + R_osc)·E(1 − e^{−t/τ}) avec
τ = R·R_osc/(R + R_osc)·C, erreur 2 % ; R_oscC = 125 ms → décharge non enregistrable sans suiveur ; montage de
droite via u_C = E − u_R (d'après web.ac-reims.fr).
**En savoir plus (p.40–41)** — « La foudre et les paratonnerres » : nuage–Terre comme un énorme condensateur,
ionisation de l'air vers 10 000 V par cm, paratonnerres, précautions (d'après Encarta 2006).

### Bornes de scope (chapitre 1)

- ✅ **INCLUS** :
  - Condensateur : définition (armatures, diélectrique), symbole, condensateur plan ; types usuels (air,
    diélectrique solide roulé, électrochimique) ; ordres de grandeur de C par type.
  - Charge et décharge qualitatives (galvanomètre balistique, sens de déviation, déplacement d'électrons,
    charges +q / −q) ; le condensateur stocke des charges.
  - Intensité algébrique (sens positif arbitraire ; DEL tête-bêche ; signe de u_R = Ri) ; charge q d'un
    condensateur = charge de l'armature vers laquelle est orienté le sens positif ; **i = dq/dt** (limite de
    Δq/Δt).
  - Charge à **courant constant** : q = I.t, u_C = kt (lecture de pente), **q = C u_C**, C = I/k ;
    capacité, **farad** et sous-multiples mF, μF, nF, pF, fF.
  - **C = εS/e**, ε₀ = 1/(36π·10⁹) F.m⁻¹, **ε_r = ε/ε₀**, C = ε_r ε₀ S/e ; tableau de permittivités.
  - Tension de claquage (définition), tension de service (nominale).
  - Énergie : réservoir d'énergie potentielle électrique (moteur, DEL, thermique) ; **E_C = ½Cu² = q²/2C = ½qu**
    (formule donnée) ; énergie dissipée par effet Joule = énergie emmagasinée (ex. 12, en exercice) ;
    proportionnalités (doubler q, C ou u : QCM VI).
  - Dipôle RC : échelon de tension, phénomène transitoire ; **équations différentielles** par la loi des
    mailles, en u_C, en q et en i (forme avec ∫ i dt), charge (second membre E/τ ou E/R) et décharge (sans
    second membre) ; résolution par **solution imposée** B + Ae^{−αt} / Ae^{−αt} et identification des
    constantes (conditions initiales, « pour toute valeur de t ») ; identification α, β ou τ, R, C à partir
    d'une équation numérique (ex. 8, ex. 10).
  - Expressions **u_C(t), q(t), i(t)** en charge (Q₀ = CE, I₀ = E/R, i > 0) et en décharge (i = −I₀e^{−t/τ},
    i < 0) ; allures des chronogrammes ; calcul de u_C, i à un instant donné (exponentielles numériques) ;
    instant où q atteint une fraction de CE (ex. 10 : ½CE, CE/4 — passage au Log).
  - Visualisation à l'oscilloscope (numérique / à mémoire, voies Y1/Y2, masse, bouton INV, générateur à masse
    flottante, u_DA = Ri image de i) ; GBF en créneaux (mention) ; acquisition par ordinateur.
  - Influence de R et de C (lecture d'oscillogrammes, proportionnalité de la durée à R et à C) ; **τ = RC**,
    dimension d'un temps ; τ par calcul, par **tangente à l'origine** (u_C charge → droite u_C = E ; décharge
    → axe des abscisses ; i(t) charge et décharge), par lecture **0,63 E / 0,37 E** ; durée de charge ou
    décharge complète **4,6 τ ≃ 5 τ (1 %)**, **6,9 τ ≃ 7 τ (1 ‰)** ; tableau récapitulatif.
  - Calculs types des exercices : C d'un condensateur plan, q = It, u = q/C, E_C ; τ, R ou C déduits de τ ;
    I₀ = E/R ; lecture graphique de E et τ sur oscillogramme ou tableau de mesures ; application au flash et au
    défibrillateur.
- ⛔ **EXCLU** (absent du chapitre) :
  - Associations de condensateurs (série / parallèle) et capacité équivalente.
  - Champ électrique entre les armatures, force électrostatique, potentiel au sens électrostatique au-delà de
    V_A − V_B, densité d'énergie ; démonstration de C = εS/e ; **démonstration de E_C = ½Cu²** (par
    intégration de la puissance) — la formule est seulement donnée.
  - Résolution de l'équation différentielle par séparation des variables / intégration (seule la méthode de la
    solution de forme imposée est utilisée) ; notation « ln » (le manuel écrit « Log »).
  - Réponse à un signal créneau étudiée quantitativement (mentionnée en remarque seulement) ; régime
    sinusoïdal ; dipôles RL et RLC (chapitres suivants).
  - Influence de E sur la durée de charge (non étudiée : seuls R et C varient) ; demi-vie t_{1/2} = τ·Log2 comme
    résultat de cours (n'apparaît qu'en exercice 10).
  - Suiveur de tension, impédance d'entrée de l'oscilloscope, résistance interne du voltmètre : **fiche
    technique seulement**, non exigibles ; foudre et paratonnerres : lecture.

### Lecture

- **Pages lues en couche texte** (`/root/.cache/yqa-manuels/223433/txt/pNNN.txt`) : 10 à 41 (les 32 pages) et
  316 à 318 (réponses : seul p.316 concerne le chapitre 1 — ex. 3 à 9 ; p.317–318 = chapitres 5–11 et sites
  web, rien pour le chapitre 1).
- **Pages lues sur l'image** (110 dpi) : **32 pages** — 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
  24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 316 ; plus 4 recadrages à 200–250 dpi
  (p.33 « τ1 = R2C », p.35 exposant de l'ex. 8, p.37 graphe de l'ex. 12, p.316 réponses du chapitre 1).
  Page non vue sur l'image : 41 (prose seule, pas de formule ni de figure). Toutes les formules, encadrés,
  tableaux et figures cités ci-dessus ont été relus sur l'image.
- **Sondage image (≥ 1 page sur 10, parmi les plus denses)** : fait sur la totalité ; pages les plus denses
  : 15, 18, 22, 25, 29, 30, 31, 33, 35, 36. **Écarts couche texte / image constatés** :
  p.15 l'encadré **i(t) = lim Δq/Δt = dq/dt est totalement absent** du texte (seul un « C » parasite) ;
  p.16 q = (I/k)u_C fragmentée ; p.18 ε perdu dans C = εS/e (rendu « C= S/e »), ε₀ = 1/(36π.10⁹) rendu
  « o = 1/36 .109 », ε_r = ε/ε₀ perdu ; p.20 exposants de E_C ; p.22 α et τ perdus partout (« uC(t) = B + Ae t »,
  « 1 − = 0 »), signe ∫ perdu dans (3) ; p.23 et p.25 exposants −t/τ et ∀t perdus ; p.29 (du_C/dt)_{t=0} et
  E/τ illisibles ; p.30 ≤, ≥ perdus, « ≃ » rendu « b », « 1 ‰ » rendu « 1o/oo » ; p.33 τ1, τ2, θ perdus ;
  p.35 ex. 8 « 12.10⁵ » au lieu de **12.10⁻⁵** ; p.36 q = CE/4 éclaté ; p.37 ex. 11 6°) α perdu ; p.316
  fractions et unités ok mais colonnes entremêlées avec le chapitre 2. Les tableaux (p.16, p.17, p.18, p.30,
  p.35 ex. 7) sont conformes dans le texte.
- **Doutes signalés [?]** :
  1. **Réponse ex. 3 2°)** : imprimé « 8.8 10⁻³ J » (vérifié sur l'image) ; recalcul avec C ≈ 0,707 μF et
     u = 50 V : ½·0,707·10⁻⁶·2500 ≈ 8,8·10⁻⁴ J → facteur 10 probable dans le manuel. À ne pas reprendre tel quel.
  2. **Exercice résolu 2°a)** : « où τ1 = R2C » — coquille, lire τ2 = R2C (image p.33).
  3. **L'essentiel** : « C = e S/e » — coquille, lire C = ε S/e (image p.31).
  4. Ex. 11 6°) : « (1/α) du_AB/dt + U_AB = 0 » avec U majuscule (coquille probable pour u_AB).
  5. Ex. 12 : graphe sans valeurs numériques (graduations seules, 2 V/div et 2,5 ms/div annoncés) ; U_o
     n'est pas lisible avec certitude (le sommet est à la 3ᵉ graduation, soit 6 V si une graduation = 1 div) ;
     aucune réponse fournie.
  6. Réponses fournies seulement pour les ex. 3 à 9 ; Ex. 1 (V/F), Ex. 2 (QCM), Ex. 10–13 sans réponse ; tableaux
     des §3.1 et §3.2 (durées pour u_C = 4 V) laissés vides, et C de la manipulation §4 non calculé.
  7. Fig.3 (p.13) : d'après le schéma, R semble placé seulement dans la branche de décharge (position 2),
     alors que le texte cite R parmi les éléments du montage sans préciser sa place.
  8. Fig.13–14 (p.21) : Y1 en D (u_DB = E, tension du générateur), Y2 en A (u_AB) ; la figure porte aussi des
     flèches u_DA et u_AB, et Fig.14 ne laisse distinguer qu'une courbe — identification des voies à confirmer.
  9. Présence de E_C = q²/2C, de C = εS/e et de la fiche technique au **programme officiel** de la section
     Sciences expérimentales non vérifiée ici (R-3) : bornes établies sur le manuel seul.

## 2.2 Chapitre 2 — La bobine ; le dipôle RL (manuel 223433, p.42–77)

Bandeau courant : « Evolution de systèmes ◆ La bobine ; le dipôle RL » (p.56 : « Evolution de systèmes
électriques »). Le chapitre a deux parties titrées en bandeau : « L'INDUCTION ÉLECTROMAGNÉTIQUE »
(p.44–56, §1 à 6) et « LE DIPÔLE RL » (p.57–66, §1 à 3), puis L'essentiel (p.67), Exercices (p.68–76),
En savoir plus (p.77).

**Page d'ouverture (p.43)** — « LA BOBINE / LE DIPÔLE RL » ; numéro « 2 ». Photo d'un transformateur de
poste électrique, légende : « Même les gros transformateurs utilisent des bobines ». Questions d'accroche :
« ◆ Pourquoi, les transformateurs ne peuvent pas être utilisés en courant continu ? ◆ Comment fonctionnent
les ralentisseurs électromagnétiques des véhicules “poids lourds” ? » (réponses : §6.2 p.56 et « En savoir
plus » p.77).

**Objectifs (p.42, lus sur l'image)** — « ◆ Mettre en évidence expérimentalement le phénomène d'induction
électromagnétique. ◆ Appliquer la loi de Lenz. ◆ Reconnaître les facteurs dont dépend la f.e.m.
d'auto-induction. ◆ Calculer l'énergie emmagasinée dans un solénoïde. ◆ Établir, pour un dipôle RL soumis
à un échelon de tension, l'équation différentielle qui régit les variations de l'intensité i du courant
parcourant la bobine en fonction du temps. ◆ Déterminer graphiquement la constante de temps τ = L/R à
partir des courbes de réponse u_L(t) ou i(t) d'un dipôle RL. »

**Prérequis (p.42)** — SAVOIR : « Définir un champ magnétique. Définir une ligne de champ magnétique.
Définir le vecteur champ magnétique. Définir un champ magnétique uniforme. Enumérer les caractéristiques
d'un [c]hamp magnétique créé par un courant continu circulaire (solénoïde). » — SAVOIR FAIRE : « Identifier
les pôles d'un aimant et les faces d'une bobine. Mettre en évidence expérimentalement l'existence d'un
champ magnétique. Déterminer les caractéristiques d'un vecteur champ magnétique. Reconnaître un champ
magnétique uniforme à partir de la forme de son spectre. » (imprimé « hamp », coquille.)

**Plan du chapitre** (pas de sommaire imprimé ; titres lus dans le corps) :
- *L'induction électromagnétique* — 1 Le phénomène d'induction électromagnétique (1.1 Production d'un
  courant induit par déplacement relatif d'un aimant et d'une bobine ; 1.2 Autre mode de production du
  courant induit) · 2 Loi de Lenz · 3 La force électromotrice d'induction · 4 L'auto-induction (4.1 Mise en
  évidence du phénomène d'auto-induction ; 4.2 La force électromotrice d'auto-induction [imprimé
  « ÉLOCTROMOTRICE »] ; 4.3 Facteurs dont dépend l'inductance d'une bobine ; 4.4 Relation entre la tension
  aux bornes d'une bobine et l'intensité du courant qui y circule) · 5 Énergie magnétique emmagasinée dans
  une bobine · 6 Applications de l'induction électromagnétique (6.1 Les alternateurs ; 6.2 Les
  transformateurs).
- *Le dipôle RL* — 1 Réponse d'un dipôle RL à un échelon de tension (1.1 Étude expérimentale ; 1.2 Étude
  théorique) · 2 La rupture du courant dans un dipôle RL (2.1 Étude expérimentale ; 2.2 Étude théorique) ·
  3 Influence des grandeurs caractéristiques d'un dipôle RL sur le régime transitoire (3.1 Influence de la
  résistance totale R ; 3.2 Influence de l'inductance L ; 3.3 Constante de temps d'un dipôle RL).
- L'essentiel (p.67) · Exercice résolu (p.68–70) · Exercices à résoudre : Tests rapides des acquis (ex. 1–2,
  p.71), Exercices d'application (ex. 3–9, p.72–73), Exercices de synthèse (ex. 10–14, p.74–76) · En savoir
  plus (p.77).

Texte d'introduction (p.44) : « Une bobine est un dipôle électrocinétique constitué d'un enroulement dans le
même sens, de fil conducteur recouvert d'un vernis isolant. De ce fait, elle a une résistance électrique
interne. Un tel dipôle placé dans un circuit électrique, se comporte-t-il alors comme un résistor vis à vis
du courant électrique ? La bobine est-elle, comme le condensateur, un réservoir d'énergie ? »

### Partie A — L'induction électromagnétique : manipulations

**1.1 Expérience 1** (p.44) — bobine fermée sur un milliampèremètre à zéro central « sensible aux courants
très brefs » (Fig.1). Approcher un pôle d'un barreau aimanté d'une face : l'aiguille dévie dans un sens
(Fig.2a), revient à zéro dès que cesse le déplacement ; éloigner : déviation en sens contraire (Fig.2b).
Mêmes observations en déplaçant la bobine (aimant fixe) suivant son axe. Remarque : mieux avec un
« galvanomètre balistique ».
**1.1 Expérience 2** (p.44–45) — bobine (B1) fermée sur un résistor R (Fig.3, points A, M, masse en M) ;
entrée Y1 d'un oscilloscope à mémoire → u_R(t). Approche du pôle nord : chronogramme 1 (Fig.4a, impulsion
**négative**, lue sur l'image) ; éloignement : oscillogramme 2 (Fig.4b, impulsion **positive**) ; approche
plus rapide : même forme, « pic plus prononcé ».
Questions (p.45) : 1°) que se passe-t-il dans une bobine en circuit fermé lors d'un déplacement relatif
aimant-bobine ? 2°) justifier le recours à u_R(t) pour suivre i ; 3°) énumérer les facteurs dont dépendent
les propriétés du phénomène.
Conclusion (p.45) : « Avec un déplacement relatif bobine-aimant, on peut produire un courant électrique dans
la bobine en circuit fermé. Un tel courant électrique est appelé courant induit, alors que l'aimant est
appelé inducteur. L'intensité du courant induit est d'autant plus grande que le déplacement relatif
bobine-aimant est plus rapide. »

**1.2 Autre mode de production** (p.45–46) — montage Fig.3 conservé ; l'aimant remplacé par un solénoïde
(B2) de plus grand diamètre, alimenté par un GBF, (B1) introduite dedans (Fig.5) ; Y1 → u_R(t), Y2 → u(t)
du générateur. Tension sinusoïdale aux bornes de (B2) → tension « de forme semblable » aux bornes de (B1)
(Fig.6, deux sinusoïdes). Remarque : avec un générateur de tension continue, « il ne se passe plus rien dans
la bobine (B1), une fois le courant y est établi ». Question : interpréter l'apparition du courant induit.
Constatation : « La variation de l'intensité du courant électrique dans une bobine produit un courant induit
dans une autre bobine en circuit fermé à proximité de la première. Le courant électrique variable, qui est à
l'origine du courant induit, est appelé courant inducteur, tandis que le circuit dans lequel il circule est
appelé circuit inducteur. » Interprétation : dans les deux cas, variation des caractéristiques du champ où
baigne la bobine → « champ magnétique inducteur ».

**2 Loi de Lenz** (p.46–48) — expérience 2 refaite avec le **pôle sud** vers la même face : approche (Fig.7a)
→ Fig.7c impulsion **positive** ; éloignement (Fig.7b) → Fig.7d impulsion **négative** (lu sur l'image).
Questions (p.47) : 1°) signe de u_R dans 7a et 7b, en déduire le sens du courant induit ; 2°) représenter le
vecteur champ b⃗ créé par le courant induit à l'intérieur de la bobine et en déduire le nom de la face
présentée à l'aimant ; 3°) identifier parmi 4a et 4b celui où le courant induit a le même sens que 7c, 7d ;
4°) montrer que le courant induit s'oppose au sens de déplacement de l'aimant et au signe de variation de
‖B⃗‖. Tableau (p.47, lu sur l'image) pour l'approche : colonne pôle N approché / colonne pôle S approché ;
« Sens de B⃗ : de l'aimant vers la bobine | de la bobine vers l'aimant » ; « Valeur de B⃗ : ‖B⃗‖ augmente » ;
« Sens du courant induit : La bobine présente sa face nord au pôle nord de l'aimant | La bobine présente sa
face sud au pôle sud de l'aimant » ; « Effets du sens du courant induit : La bobine présente à l'aimant la
face de même nom que le pôle de l'aimant qui est de son côté : répulsion bobine-aimant ⇕ Ayant le sens
contraire de celui de B⃗, le vecteur champ b⃗ créé par le courant induit s'oppose à l'augmentation de ‖B⃗‖. »
Question (p.48) : traiter de même 7b et 2b (éloignement). Texte : éloigner → attraction aimant-bobine ; b⃗
prend « plutôt le même sens que B⃗ afin de compenser la diminution de la valeur de ce dernier ».
Remarque : « Le champ magnétique créé par le courant induit est appelé champ induit. »
[Interprétation p.47 : le manuel écrit « le vecteur champ inducteur b⃗ » (minuscule) là où le tableau note
B⃗ l'inducteur et b⃗ l'induit — coquille de notation, à ne pas reproduire.]

**3 La f.e.m. d'induction** (p.48) — texte seul : le courant induit est produit sans générateur, il est dû à
« une f.e.m. délocalisée ; elle est là, partout dans le circuit induit. Elle prend naissance dans le circuit
avec la cause et cesse avec la cause. Si le circuit induit est ouvert, la f.e.m. se manifeste par
l'apparition d'une tension à ses bornes. Cette force électromotrice est appelée force électromotrice
d'induction ou force électromotrice induite. »

**4.1 Mise en évidence de l'auto-induction** (p.48–49) — Fig.8 : générateur E, interrupteur K, deux
dérivations : (résistance ajustable R + lampe L1) ∥ (bobine à noyau de fer doux + lampe L2) ; lampes
identiques, conducteur ohmique et bobine de même résistance R. À la fermeture : L1 brille tout de suite ; L2
n'atteint son éclat maximal (identique à L1) « qu'avec un retard de quelques millièmes de secondes ».
Questions : 1°) les deux lampes parcourues par des courants de même intensité à la fermeture ? 2°) influence
de la bobine sur l'intensité dans L2 ? Interprétation : variation de i de zéro à I → variation du champ
propre → courant induit qui s'oppose (Lenz) ; « (le circuit induit est lui même le circuit inducteur) est
appelée auto-induction » ; « f.e.m. d'auto-induction (ou f.e.m. auto-induite) ».

**4.2 La f.e.m. d'auto-induction** (p.49–51) — Fig.9 : en série R₀, bobine longue (B1) de résistance r
négligeable devant R₀, GBF à masse flottante ; A → Y1, C → Y2 ; masse en B (Fig.10, lu sur l'image) ;
visualiser u_AB (Y1) et u_BC (Y2, bouton INV au lieu de u_CB) (Fig.11 : u_AB triangulaire, u_BC carrée).
Questions : 1°) expressions de u_AB et u_BC ; 2°) exprimer u_AB et u_BC entre t₁ = 0 et t₂ = T/2 en
fonction du temps ; en déduire l'expression de e en fonction de i.
Raisonnement (lu sur l'image) : u_AB = R₀ i ⇒ i = u_AB/R₀ triangulaire ; u_BC = − e + r i ≃ − e ;
« • Pour t ∈ [nT, nT + T/2] avec n entier, u_BC = + U₀ ; Donc e = − U₀ • Pour t ∈ [nT + T/2, (n+1)T],
u_BC = − U₀ ; Donc e = + U₀ » ; « e = ± U₀ (1) » ; u_AB = a₁t + b₁ ⇒ i = (a₁/R₀)t + b₁/R₀ ; u_AB = a₂t + b₂ ;
« Or a₂ = − a₁ … Donc, di/dt = ± a₁/R₀ (2) » ; « Les équations (1), (2) et la loi de Lenz donnent :
e/(di/dt) = − U₀ R₀/a₁ » ; « Ce qui signifie : e = − L di/dt, où L = U₀ R₀/a₁ est une constante positive
appelée inductance. » Puis discussion du signe (voir Encadrés).

**4.3 Facteurs dont dépend l'inductance** (p.51–52) — expérience 4.2 refaite à une autre fréquence, mêmes
sensibilités, avec quatre bobines (tableau lu sur l'image) :

| Bobine | (B1) | (B2) | (B3) | (B4) |
|---|---|---|---|---|
| N | 500 | 500 | 500 | 250 |
| ℓ (cm) | 20 | 30 | 20 | 20 |
| D (cm) | 10 | 10 | 15 | 10 |

(N nombre total de spires, ℓ longueur, D diamètre moyen.) Oscillogrammes Fig.12a–d (triangle identique ;
créneau u_BC d'amplitude : (B3) la plus grande, (B4) la plus petite, (B2) < (B1) — lecture qualitative de
l'image). Questions : 1°) a) montrer que L augmente avec N et diminue quand ℓ augmente ; b) influence de la
section ; 2°) quels oscillogrammes comparer à la Fig.11 pour savoir si L dépend de la fréquence du GBF.
Conclusion et remarques : voir Encadrés.

**4.4 Relation tension-intensité** (p.53) — symbole (Fig.13a, « L,r ») et modèle équivalent (Fig.13b :
inductance L en série avec r) ; Fig.14a/14b : générateur de f.e.m. e (A→C) en série avec résistor r (C→B).
« uAB = uAC + uCB. Par application de la loi d'Ohm : uAB = −e + r i. Or, e = −L di/dt. donc : uAB = L di/dt + r i »
(résultat encadré en rouge). Remarque : variation très brusque (coupure) ⇒ le terme L di/dt l'emporte,
tension « pratiquement égale à L di/dt ».

**5 Énergie magnétique** (p.53–56) — Fig.15 : bobine (B) L = 10 mH (« bobine de 500 spires par exemple »),
résistance r ; générateur E = 6 V ; diode D ; condensateur C = 5 μF ; voltmètre numérique ; milliampèremètre.
Diode en série avec le condensateur (branche A–B, voltmètre aux bornes de C) en dérivation sur la bobine
(N–M), montée en inverse. K fermé : I = 240 mA, tension nulle aux bornes du condensateur ; après ouverture :
tension u_AM négative. Questions (p.54) : 1°) diode passante circuit fermé ? 2°) déterminer r ; 3°)
interpréter u_AM négative après ouverture et justifier le voltmètre numérique ; 4°) montrer que la bobine
emmagasine de l'énergie quand K est fermé ; 5°) importance de la diode dans un circuit renfermant une bobine.
Interprétation : u_NM = r i + L di/dt (encadré) ; en régime permanent di/dt = 0, u_NM = r i, « l'énergie mise
en jeu par la bobine est une énergie consommée par effet Joule » ; charge du condensateur par un courant
induit bref « dans le même sens que le courant permanent » ; « p = + u_NM.i, ce qui donne : p = r.i² + Li di/dt ».
Encart (p.55) : « p = ri² + Li di/dt = ri² + d/dt(½Li²) ; ri² : puissance dissipée par effet Joule ;
d/dt(½Li²) : puissance magnétique p_L ; Or p_L = dE_L/dt. Donc, E_L = ½L.i² ». Puis E_L, décroissance de
|i| → la bobine « joue ainsi le rôle de générateur » ; à l'ouverture, elle restitue toute son énergie au
condensateur (la diode l'empêche de se décharger dans la bobine). Conclusion et Remarque : voir Encadrés.
[Le texte p.54 nomme la tension « u_AB » puis la question « u_AM » ; Fig.15 place le condensateur entre A et
B — incohérence de notation du manuel [?]. Le manuel ne donne pas la valeur numérique de r (I = 240 mA,
E = 6 V seuls fournis).]
**Étincelle de rupture** (p.55–56) : durée de transfert « de l'ordre de 1ms » ; tension très élevée ;
ionisation de l'air ; précautions (« insérer dans le montage, des condensateurs par exemple ») ; exploitée
dans : « Allumeur électrique de cuisinières à gaz, dispositif de soudage par arc électrique, dispositif
d'amorçage de tube néon... ».

**6 Applications** (p.56) — 6.1 alternateur : « transforme de l'énergie mécanique en énergie électrique » ;
alternateur à induit mobile / à induit fixe ; alternateur de voiture (Fig.16) : induit fixe (stator),
inducteur = aimant cylindrique multipolaire (rotor) ; fréquence liée à la fréquence de rotation de
l'inducteur. 6.2 transformateur (Fig.17) : « quadripôle qui permet d'abaisser ou d'augmenter une tension
alternative » ; ne fonctionne qu'en alternatif car « en courant continu, le primaire créerait un champ
magnétique constant au cours du temps. Par conséquent, il ne pourrait rien induire dans le secondaire. »

### Partie B — Le dipôle RL : manipulations

Définition (p.57) : « On appelle dipôle RL l'association en série d'une bobine d'inductance L, de résistance
r et d'un résistor de résistance R₀, R étant la résistance totale R₀+r du dipôle. »

**1.1 Établissement — étude expérimentale** (p.57–58) — Fig.18 : générateur idéal E = 6 V, K, bobine
L = 0,1 H, r = 10 Ω (entre A et B), résistor R₀ = 40 Ω (entre B et M, masse en M), diode D entre A et M, en
parallèle sur l'ensemble bobine + R₀ (montée en inverse) ; A → Y1, B → Y2 d'un oscilloscope à mémoire (ou interface d'acquisition).
Fig.19 : chronogrammes (1) = u_AM (palier) et (2) = u_BM (montée exponentielle). Questions : 1°) identifier
l'intensité représentée ; 2°) lequel représente i(t) ; 3°) déterminer graphiquement I₀ et la comparer à
E/R ; 4°) raison du retard ; 5°) allure et valeur maximale de u_BM si r = 0 ; 6°) rôle de la diode.
Interprétation : u_AM = E instantanément ; u_R₀ croît jusqu'à U₀ < E : « régime transitoire » ; puis
constante : « régime permanent » (Fig.20) ; i = u_R₀/R₀ ; I₀ = U₀/R₀ ; « on peut constater que I₀ = E/R » ;
u_AM = E = rI + R₀I ⇒ u_AB = rI : en régime permanent la bobine « se comporte alors comme un résistor de
résistance égale à sa résistance interne r. Si r = 0, uAB = 0. Or uAB + uBM = E, d'où uR₀ = uBM = E. »
Conclusion : voir Encadrés.

**1.2 Étude théorique** (p.58–60) — Fig.21. Loi des mailles u_AB + u_BM − E = 0 ⇒ u_AB + u_BM = E (1) ;
u_AB = L di/dt + ri ; u_BM = R₀.i ; « L di/dt + Ri = E (2), avec R = R₀ + r » ; « di/dt + (R/L)i = E/L » ;
encadré « di/dt + (1/τ)i = E/L (3), avec τ = L/R ». Analogie avec « du_C/dt + (1/τ)u_C = E/τ (équation (1)
de la page 22) » du dipôle RC. Solution proposée i(t) = Ae^(−αt) + B ; i(0) = A + B = 0 ⇒
i(t) = A(e^(−αt) − 1) ; di/dt = −αA.e^(−αt) ; « Ae^(−αt)[1/τ − α] − A/τ = E/L (4) » ; t → ∞ : « −A/τ = E/L,
d'où A = −E/R » ; « Ae^(−αt)(1/τ − α) = 0 quel que soit t » ⇒ α = 1/τ ; encadré « i(t) = (E/R)(1 − e^(−t/τ)),
avec τ = L/R » (Fig.22, asymptote E/R).
Tension aux bornes de la bobine (p.60) : « uAB = L (E/(Rτ)).e^(−t/τ) + r(E/R)(1 − e^(−t/τ)) =
E.e^(−t/τ) + r(E/R)(1 − e^(−t/τ)) » ; « uAB(0) = E » ; « lim_{t→∞} uAB = (r/R)E » (Fig.23) ; Remarque : « Si
r = 0, uAB = Ee^(−t/τ). Dans ces conditions lim uAB = 0 ». Questions : 1°) modifier le branchement de la
Fig.18 pour visualiser u_AB ; 2°) vérifier que la courbe enregistrée est celle de la Fig.23.

**2.1 Rupture — étude expérimentale** (p.61) — même montage Fig.18, régime permanent établi, on ouvre K :
Fig.24 (u_R₀ décroissante exponentielle). Questions : 1°) expliquer l'allure de u_R₀ ; 2°) rupture
instantanée ? pourquoi ? 3°) que se passerait-il au niveau de K sans diode ? Interprétation : avant
ouverture u_AM = E = RI, u_BM = R₀I, diode non passante ; après, courant transitoire dans le circuit bobine
+ résistor + diode, « dans le même sens que celui établi avant la rupture ». Remarque : sans diode, étincelle
de rupture ; « Exemple : Avec L = 1 H, I = 500 mA, e = −L di/dt ≃ −L Δi/Δt. Δt ≃ 1 ms, ce qui donne
e ≃ 500 V ! » (renvoie au « paragraphe 5 de la première partie … page 54 »).

**2.2 Rupture — étude théorique** (p.62) — Fig.25 (bobine A–B, R₀ B–M, diode D fermant le circuit).
« uAB + uBM = 0 (1) » ; « uAB = L di/dt + r.i et uBM = R₀.i » ; « L di/dt + R.i = 0 avec R = R₀ + r » ;
« di/dt + (1/τ).i = 0 (2), avec τ = L/R : équation différentielle en i à coefficients constants et à second
membre nul » ; solution i(t) = A.e^(−αt) ; i(0) = A = I₀ = E/R ; « −αAe^(−αt) + (1/τ)Ae^(−αt) = 0 … ∀t » ;
α = 1/τ ; encadré « i(t) = (E/R)e^(−t/τ) avec R = R₀ + r et τ = L/R » (Fig.26). Questions : 1°) montrer par
deux méthodes différentes que « uAB = (r/R − 1) Ee^(−t/τ) » ; 2°) vérifier à l'ordinateur la Fig.27 (u_AB
part de −R₀E/R et tend vers 0) ; 3°) comparer u_AB(0) à sa valeur juste avant l'ouverture et en déduire que
si r = 0, u_AB passe de zéro à (−E).

**3.1 Influence de R** (p.63–64) — montage Fig.18, L = 0,2 H, R₁ = 210 Ω ; R₂ = 230 Ω ; R₃ = 270 Ω ;
R₄ = 350 Ω ; 1 ms/div, 1 V/div (Fig.28a–d). Questions : 1°) tableau des durées t pour que u_R₀ atteigne
4 V (R (Ω) : 210, 230, 270, 350 ; t (ms) : vide) ; 2°) influence qualitative de R ; montrer que t est
inversement proportionnelle à R. (Le manuel ne remplit pas le tableau.)
**3.2 Influence de L** (p.64–65) — bobine d'inductance réglable (« Bobine dépourvue de tout noyau de fer
doux »), R₀ ajusté pour garder R = R₀ + r constante = 210 Ω ; L₁ = 0,10 H ; L₂ = 0,13 H ; L₃ = 0,15 H ;
L₄ = 0,20 H ; 0,5 ms/div, 1 V/div (Fig.29a–d). Questions : 1°) a) tableau t pour u_R₀ = 4 V ; b) influence
qualitative de L ; montrer que t est proportionnelle à L. (Tableau non rempli.)
**3.3 Constante de temps** (p.65–66) — notion, remarque dimensionnelle, définition, méthodes : voir Encadrés.

### Encadrés (VERBATIM, vérifiés sur l'image de leur page)

> **Conclusion : la loi de Lenz** (p.48) — « Le courant induit a un sens tel qu'il s'oppose par ses effets à
> la cause qui lui donne naissance. »

> **Conclusion** (p.46) — « Toute variation de champ magnétique crée dans un circuit électrique fermé situé à
> proximité du champ, un courant électrique appelé courant induit : c'est le phénomène d'induction
> électromagnétique. Le courant induit est d'autant plus intense que la variation locale des
> caractéristiques du champ inducteur est plus rapide. Le sens du vecteur champ magnétique inducteur est un
> facteur dont dépend le sens du courant induit. »

> **Conclusion** (p.49) — « Une bobine ne se comporte pas comme un conducteur ohmique. Placée dans un circuit
> fermé, elle s'oppose aux variations de l'intensité du courant électrique qui y circule. »

> **Définition** (p.51) — « L'inductance est une grandeur caratérisant l'aptitude d'une bobine à modérer les
> variations de tout courant électrique qui y circule. Dans le système international d'unités, l'inductance
> s'exprime en henry (H). » Note : « Nom dédié au physicien américain Joseph Henry (1797-1878) ». (imprimé
> « caratérisant ».)

> **Signe de −L di/dt** (p.51, hors encadré) — « Dans l'expression (− L di/dt), le signe (−) traduit la loi de
> Lenz : − Quand i croît, L.di/dt > 0. Donc, e < 0 : la f.e.m. d'auto-induction s'oppose à l'augmentation de
> l'intensité du courant. − Quand i décroît, L.di/dt < 0. Donc, e > 0 : la f.e.m. d'auto-induction s'oppose à
> la diminution de l'intensité du courant. »

> **Conclusion : Expression de la f.e.m. d'auto-induction** (p.51) — « Toute bobine d'inductance L parcourue
> par un courant électrique d'intensité i variable est le siège d'une force électromotrice appelée force
> électromotrice auto-induite (ou d'auto-induction) e = − L di/dt. »

> **Conclusion** (p.52) — « L'inductance d'une bobine ne dépend que de ses caractéristiques géométriques, à
> savoir le nombre total de spires, la longueur et la section moyenne, d'où sa qualification d'inductance
> propre. »
> **Remarques** (p.52) — « Les bobines usuelles ont une inductance nettement inférieure à 1 H. Exemple : un
> solénoïde de 150 spires, de 15 cm de longueur et de 3 cm de diamètre a une inductance L = 140 μH, —
> L'introduction d'un barreau de fer doux dans un solénoïde fait augmenter la valeur de son inductance L.
> Mais, dans ces conditions, l'expression e = − L di/dt n'est plus valable. — Du fait que la f.e.m.
> auto-induite est due à l'inductance L de la bobine, toute bobine d'inductance L non nulle est qualifiée de
> bobine inductive. Si en plus, sa résistance est nulle, elle est dite purement inductive. »

> **Tension aux bornes d'une bobine** (p.53, encadré rouge) — « uAB = L di/dt + r i » (sens positif de A vers
> B).

> **Énergie magnétique** (p.55, encadré) — « On montre que l'énergie magnétique emmagasinée dans une bobine
> d'inductance L s'écrit : E_L = ½L.i² ». Suite : « Si |i| diminue, p_L = L.di/dt diminue, ce qui signifie que
> l'énergie magnétique diminue : la bobine restitue à l'extérieur un peu de l'énergie qu'elle a emmagasinée
> avec l'augmentation de |i|, elle joue ainsi le rôle de générateur. » [imprimé « p_L = L.di/dt » sans le
> facteur i, alors que p_L = Li di/dt — coquille [?].]
> **Conclusion** (p.55) — « Tant qu'elle est parcourue par un courant électrique, la bobine inductive est un
> réservoir d'énergie dite magnétique. »
> **Remarque** (p.55) — « L'énergie magnétique ne peut rester stockée dans une bobine en l'absence de
> courant. Par contre, l'énergie potentielle électrique reste stockée dans le condensateur même hors circuit.
> Donc, le condensateur est un réservoir permanent d'énergie, tandis que la bobine en est un réservoir
> temporaire. »

> **Conclusion** (p.58) — « La réponse d'un dipôle RL à un échelon de tension E est un courant continu
> d'intensité I₀ = E/R. Celui-ci ne s'établit pas instantanément à cause de l'inductance L de la bobine.
> Autrement dit, la bobine s'oppose à l'établissement du courant électrique dans la portion de circuit où
> elle se trouve insérée. »

> **Équation différentielle (établissement)** (p.59, encadré rouge) — « di/dt + (1/τ) i = E/L (3), avec
> τ = L/R » ; « Cette équation différentielle régit l'évolution dans le temps de l'intensité i du courant
> circulant dans le dipôle RL soumis à un échelon de tension E. »
> **Solution** (p.59, encadré) — « i(t) = (E/R)(1 − e^(−t/τ)), avec τ = L/R ».

> **Conclusion** (p.60) — « La réponse d'un dipôle RL en courant est constituée de deux régimes: un régime
> transitoire au cours duquel l'intensité augmente en exponentielle à partir de la valeur zéro en tendant
> vers la valeur I₀ = E/R et un régime permanent caractérisé par un courant continu d'intensité I₀. »
> **Conclusion** (p.60) — « Quand on soumet un dipôle RL à un échelon de tension E, il apparaît
> instantanément aux bornes de la bobine une tension égale à E mais qui décroît selon un régime transitoire
> pour s'annuler si la résistance de la bobine est nulle. »

> **Conclusion** (p.61) — « Lors de la rupture du courant dans un circuit comportant une bobine, celle-ci a
> pour effet d'assurer la continuité du courant électrique par une annulation progressive de son intensité. »

> **Rupture** (p.62, encadrés) — « di/dt + (1/τ).i = 0 (2), avec τ = L/R » ; « i(t) = (E/R)e^(−t/τ) » avec
> « R = R₀ + r et τ = L/R ».

> **Constante de temps** (p.65) — « Donc, la durée d'établissement du courant dans le circuit est
> proportionnelle au quotient L/R. De ce fait, le quotient L/R est appelé constante de temps du dipôle RL ;
> on la note τ. » Remarque : « On sait que la résistance R a la dimension du quotient d'une tension par une
> intensité de courant et que L a celle de U.t/I. Donc le quotient L/R a la dimension d'un temps, ce qui
> justifie encore son appéllation de constante de temps. » Encadré : « τ = L/R : constante de temps ».
> **Définition** (p.65) — « La constante de temps τ est une grandeur caractéristique du dipôle RL, elle
> renseigne sur le retard avec lequel s'établit le régime permanent ou la rupture du courant dans le dipôle.
> τ ayant la dimension d'un temps, elle s'exprime en secondes. »

> **Détermination de τ** (p.65–66) — « Les méthodes possibles pour déterminer la constante de temps sont les
> mêmes que celles utilisées dans le cas du dipôle RC. » ▸ *Par calcul direct* : τ = L/R. ▸ *Détermination
> graphique (1ère méthode)* : « Sur la courbe de i(t) représentant l'établissement du régime permanent, on
> trace la tangente au point d'abscisse t = 0 s. L'abscisse du point d'intersection de la tangente avec
> l'asymptote I₀ = E/R est τ. (Fig.30) » Justification : « k = di/dt (t = 0) = I₀/τ » ; tangente
> « i(t) = (I₀/τ) t » ; « i(t) = (I₀/τ)t = I₀, d'où t = τ ». Remarque : même méthode pour la rupture : « la
> tangente à l'origine des temps coupe l'axe des abscisses au point d'abscisse τ (Fig.31) ». ▸
> *Détermination graphique (2ème méthode)* : « i(τ) = (E/R)(1 − e^(−1)) = 0,63 E/R » ; abscisse du point
> d'ordonnée 0,63 E/R (Fig.32) ; rupture : « i(τ) = (E/R)e^(−1) = 0,37 E/R » (Fig.33).

### L'essentiel (p.67, verbatim, lu sur l'image)

« ■ Une bobine est un dipôle électrocinétique constitué généralement par un enroulement cylindrique dans le
même sens, de fil conducteur recouvert d'une gaine isolante. ■ Toute variation de champ magnétique à
proximité d'une bobine en circuit fermé produit un courant électrique appelé courant induit. ■ Loi de Lenz :
Le courant induit a un sens tel qu'il s'oppose par ses effets à la cause qui lui donne naissance. ■ Tout
courant induit est dû à une f.e.m. délocalisée appelée f.e.m. d'induction. ■ Toute bobine parcourue par un
courant variable d'intensité i est le siège d'une f.e.m. d'auto-induction : e = − L di/dt, où L est
l'inductance de la bobine. ■ L'auto-induction traduit l'opposition d'une bobine à toute variation de
courant. ■ Pour une bobine d'inductance L, de résistance interne r, parcourue de sa borne A à sa borne B par
un courant variable d'intensité i, la tension à ses bornes s'écrit: uAB = L di/dt + ri ■ L'énergie
magnétique emmagasinée dans une bobine parcourue par un courant d'intensité i s'exprime : E_L = ½Li² ■
L'inductance d'une bobine est une grandeur caractérisant sa faculté d'emmagasiner de l'énergie magnétique.
■ Etant liée à l'intensité du courant, l'énergie magnétique stockée par une bobine est transférée à
l'extérieur du circuit avec la rupture du courant. ■ Un dipôle RL soumis à un échelon de tension de valeur E
est parcouru par un courant continu qui ne s'établit pas brusquement, mais à la suite d'un régime
transitoire, selon la loi : i(t) = (E/R)(1 − e^(−t/τ)) où τ = L/R est la constante de temps du dipôle RL.
■ Lors de la rupture du courant dans un circuit comportant une bobine, l'intensité i du courant ne s'annule
pas brusquement, mais en diminuant de manière continue selon la loi : i(t) = (E/R)e^(−t/τ) »

### Exercice résolu (p.68–70)

**Énoncé** — circuit série : générateur E = 6 V, K, bobine (L, r), résistor R₀ = 140 Ω ; oscilloscope à
mémoire ; Fig.1 : montée exponentielle, 2 ms/div, 1 V/div. 1°) choisir parmi les schémas 1 (R₀ entre K et la
bobine, masse en M côté générateur) et 2 (R₀ entre la bobine et M, masse en M) celui de l'enregistrement ;
ajouter les connexions ; 2°) expliquer l'allure ; 3°) a) montrer « du/dt + (1/τ)u = (R₀/L)E, où τ = L/R avec
R = R₀ + r » ; b) solution u = Ae^(−αt) + B : déterminer A, B, α ; 4°) déterminer graphiquement τ, r et L ;
5°) en déduire i(t).
**Solution** — 1°) l'oscilloscope ne visualise que des tensions ; il faut u = R₀.i, résistor avec une borne
à la masse ⇒ schéma 2, B relié à une entrée (Fig.3, « Entrée Y »). 2°) i ne peut augmenter que
progressivement (la bobine s'oppose à sa variation). 3°a) « uAB + uBM + uMA = 0 » ⇒ « u + ri + L di/dt = E où
u = uBM » ; i = u/R₀ ⇒ « u + (r/R₀)u + (L/R₀)du/dt = E » ; « 1 + r/R₀ = R/R₀ » ⇒ « du/dt + (R/L)u = (R₀/L)E » ;
encadré « du/dt + (1/τ)u = (R₀/L)E avec τ = L/R ». b) u(0) = A + B = 0 ⇒ B = −A ; u = B(1 − e^(−αt)) ;
du/dt = αBe^(−αt) ; « B(α − 1/τ)e^(−αt) + B/τ = (R₀/L)E » ; t → ∞ : « B/τ = (R₀/L)E, d'où B = (R₀/R)E » ;
α = 1/τ ; encadré « u = (R₀/R)E(1 − e^(−t/τ)) ». 4°) « U₀ = (R₀/R)E … (R₀ + r)/R₀ = E/U₀, d'où
r = (E/U₀ − 1)R₀ » ; U₀ lu sur l'asymptote : « U₀ = 5,6 V » ; « r = 10 Ω » ; « u(τ) = U₀(1 − 1/e) = 0,632 U₀ »
→ 3,54 V ; projection : « τ = 2 ms » ; L = τR : « L = 300 mH ». 5°) i = u/R₀ ⇒ encadré
« i = I₀(1 − e^(−t/τ)) avec I₀ = E/R = 0,04 A ».
[Coquilles du manuel lues sur l'image : p.69 « αBe^(−αt) + (B/α)(1 − e^(−αt)) = (R₀/L)E » (B/α au lieu de
B/τ) ; p.70 « 0,632 U₀ = 3,45 V » puis « En portant u = 3.54 V » (0,632 × 5,6 = 3,54 : la bonne valeur est
3,54 V, celle de l'oscillogramme).]

### Tests rapides des acquis (p.71)

**Ex.1 Vrai ou faux** (aucune réponse au corrigé p.316) : 1- bobine dans un champ magnétique variable siège
d'une f.e.m. induite ; 2- toute variation du courant dans un circuit donne naissance à une f.e.m. induite ;
3- noyau de fer doux fait diminuer L ; 4- abaisser une tension continue avec un transformateur ; 5- τ
caractérise la durée du régime transitoire ; 6- augmenter la durée du transitoire en augmentant la
résistance totale ; 7- à l'établissement, la tension aux bornes de la bobine diminue et tend vers une
limite ; 8- à l'ouverture, i ne subit pas une discontinuité.
**Ex.2 QCM** (aucune réponse au corrigé) : I- bobine inductive : a- s'oppose aux variations de la tension ;
b- s'oppose aux variations de l'intensité ; c- équivalente en continu à un résistor de résistance r. II- u_AB
pour un courant **de B vers A** : a- L.i + r.i ; b- L.di/dt + r.i ; c- − L.di/dt − r.i ; d- − (dL/dt).i − r.i.
III- L dépend de : a- la tension ; b- ses caractéristiques géométriques ; c- l'intensité. IV- bobine
purement inductive, tension à ses bornes : a- augmente sans cesse ; b- varie en tendant vers zéro ; c- prend
instantanément la valeur E ; d- tend vers une constante inférieure à E. V- courant i : a- augmente de manière
continue vers E/R ; b- diminue vers zéro ; c- prend directement E/R.

### Exercices d'application (p.72–73)

- **Ex.3** — 4 schémas (bobine fermée sur R, points A, M) : Fig.1 N en avant s'approche ; Fig.2 N en avant
  s'éloigne ; Fig.3 S en avant s'éloigne ; Fig.4 S en avant s'approche ; sens du courant induit et nom de la
  face en regard. Corrigé : « a- Nord, b- Sud, c- Sud ; d- Nord. »
- **Ex.4** — bobine fermée sur R ; 1°) approche par le pôle nord : a) représenter le champ induit ; b) sens
  du courant ; 2°) pôle sud en regard, on l'éloigne : a) champ inducteur et champ induit au centre ; b) sens.
  Corrigé : « 1°) a) Bp et Ba sont opposés, b) La règle du bonhomme d'Ampère. 2°) a) Bp et Ba ont le même
  sens, b) La règle du bonhomme d'Ampère. »
- **Ex.5** — L = 40 mH ; graphe e(t) créneau : e = 240 mV sur [0, 5 ms], − 400 mV sur [5, 8 ms], périodique
  (13, 16 ms…). 1°) di/dt en fonction de e et L ; 2°) di/dt sur [0, 5 ms] et [5 ms, 8 ms] ; 3°) tracer i(t)
  avec i(5 ms) = 0. Corrigé : di/dt = −e/L ; −6 A.s⁻¹ ; 10 A.s⁻¹ ; i décroissante sur [0, 5 ms], croissante
  sur [5, 8 ms].
- **Ex.6** — L = 470 mH, r = 10 Ω, i(t) = 0,006 t² de A vers B. 1°) u_AB(L, r, t) ; 2°) u_AB à t = 10 s.
  Corrigé : « u_AB = (12.L.t + 6.r.t²).10⁻³ V » ; « u_AB ≃ 6,06 V ».
- **Ex.7** — L = 0,1 H, r négligeable, générateur de courant variable (GBF) ; Fig.2 : i(t) en dents de scie,
  0 → 120 mA de 0 à 40 ms puis retour à 0 à 50 ms, période 50 ms. 1°) u_AB(t) sur les deux phases (0–50 ms) ;
  2°) tracer u_AB (10 ms/div, 0,5 V/div). Corrigé : [0, 40 ms] u_AB = 3L → 0,3 V ; [40, 50 ms] u_AB = −12.L →
  −1,2 V.
- **Ex.8** — montage type Fig.18 (A → Y1, B → Y2, masse M). 1°) phénomène à la fermeture (R = R₀ + r) ;
  2°) I₀ ; 3°) équation différentielle en i ; 4°) vérifier i(t) = A(1 − e^(−αt)) ; 5°) identifier A et α ;
  6°) définir la constante de temps et l'exprimer en fonction de α [symbole τ absent à l'impression].
  Corrigé : i tend vers I₀ ; I₀ = E/(r + R₀) ; di/dt + (R/L)i = E/L ; A = E/R ; α = R/L ; τ = L/R ; « pour
  t = 5.τ le régime permanent s'établit ».
- **Ex.9** — bobine L, r nulle, résistor R, générateur U = 12 V. 1°) schéma ; 2°) branchement de
  l'oscilloscope pour suivre l'établissement ; 3°) allure de i(t) ; 4°) a) I₀ ; b) τ avec L = 100 mH,
  R = 120 Ω. Corrigé : « I₀ = E/R = 0,1 A » ; « τ = L/R = 0,83 ms ».

### Exercices de synthèse (p.74–76)

- **Ex.10** — E = 6 V, K, bobine (L, r = 10 Ω), R = 200 Ω ; acquisition informatisée de u_AB (bobine) et u_BC
  (résistor) ; courbe 1 croissante → ≈ 5,7 V, courbe 2 décroissante depuis 6 V (0–20 ms). Questions 1°–9° :
  u_AB(i, di/dt) ; u_BC(i) ; associer les courbes ; I₀ par la loi des mailles ; retrouver I₀ graphiquement ;
  τ graphiquement (méthode explicitée) ; τ homogène à un temps ; L ; appareil de remplacement. Corrigé :
  courbe 1 : u_BC, courbe 2 : u_AB ; I₀ = E/(r + R) = 28,6 mA ; I₀ = u_BC/R ≃ 28,5 mA ; méthode de la
  tangente ; τ = 2,5.10⁻³ s ; L = τ(r + R) = 0,53 H. (9° sans réponse au corrigé.)
- **Ex.11** — bobine (L, r) + r' = 50 Ω, E = 6 V ; oscillogrammes : générateur 6 V, u_r' → ≈ 5 V (0–10 ms).
  1°) schéma et branchement ; 2°) u bobine ; 3°) a) I₀ ; b) r ; 4°) τ ; 5°) L ; 6°) énergie en régime
  permanent. Corrigé : I₀ = u_r'/r' = 0,1 A ; « r' = 10 ? » [lire r = 10 Ω, coquille du corrigé] ; τ ≃ 10⁻³ s ;
  L = (r + r')τ = 60 mH ; W = 0,3 mJ.
- **Ex.12** — rupture : courbe i(t) décroissante de 50 mA (0–55 ms). 1°) i(0) ; 2°) τ de deux façons ;
  3°) L avec R = r + R₀ = 50 Ω ; 4°) e à t = 0. Corrigé : I₀ = 50 mA ; méthode de la tangente : τ = 22 ms ;
  « b) i(t₁/₂) = I₀/2 → τ = 22 ms » ; L = R.τ = 1,1 H ; « e ≃ 3,3 V » [?].
- **Ex.13** — générateur E = 6 V, r = 2 Ω ; bobine AB L = 1,8 H, R = 8 Ω ; en dérivation : petit moteur en
  série avec une diode au silicium D (Fig.1). 1°) sens du courant, I = 0,6 A, pourquoi le moteur ne tourne
  pas ; 2°) à l'ouverture, le moteur tourne quelques secondes : sens du courant, origine de l'énergie,
  phénomène ; 3°) il soulève m = 20 g de h = 18,5 cm (poulie, Fig.2), g = 9,8 N.kg⁻¹ : travail, comparaison
  avec l'énergie magnétique, rendement. Corrigé : i de A vers B dans la bobine, I = E/(R + r) = 0,6 A ;
  2°) « Le courant i circule de A vers B à travers la bobine, la diode est passante » ; W = m.g.h =
  36,3.10⁻³ J ; W_m = ½L.I² = 324.10⁻³ J ; rendement 11,2 %.
- **Ex.14 Étude de texte** (p.76) — « La cuisson par induction » : plaques froides, c'est la casserole qui
  chauffe ; champ magnétique variable créé par le générateur sous la plaque → courant induit dans la paroi de
  la casserole, qui « joue le rôle de noyau pour la bobine source de champ magnétique variable », effet
  Joule. Questions : 1°) circuit où circule le courant induit ; 2°) inducteur et induit ; 3°) source
  d'énergie ; 4°) comment la casserole fait augmenter l'intensité du courant. (Pas de réponse au corrigé.)

**En savoir plus (p.77)** — « Les pouvoirs de l'induction électromagnétique » (d'après « Revue pour la
science ») : plaque à induction, courants de Foucault (« courants tourbillonnaires »), intensité
proportionnelle à la vitesse et à la valeur du champ, ralentisseurs électromagnétiques des poids lourds
(disques solidaires de l'arbre entre électroaimants ; efficaces à grande vitesse, nuls à l'arrêt, complétés
par des freins mécaniques).
Pas de « fiche technique » dans ce chapitre. Sites web (p.318, rubrique « Evolution de systèmes ») : liste
d'URL, dont « ac-grenoble.fr/phychim/term/tp/dipolerl.htm » — sans contenu exploitable.

### Bornes de scope

✅ **Inclus**
- Induction électromagnétique **qualitative** : courant induit par déplacement relatif aimant-bobine ou par
  courant variable dans une bobine voisine ; inducteur / induit, courant inducteur, champ inducteur, champ
  induit ; influence de la rapidité de la variation et du sens du champ inducteur.
- **Loi de Lenz** et son application : sens du courant induit, nom de la face (nord/sud) présentée à
  l'aimant, répulsion à l'approche / attraction à l'éloignement, b⃗ opposé ou de même sens que B⃗ ; règle du
  bonhomme d'Ampère (citée au corrigé ex.4) ; lecture du signe de u_R sur un oscillogramme.
- f.e.m. d'induction (délocalisée) ; **auto-induction** ; e = − L di/dt ; signe de e selon que i croît ou
  décroît ; inductance L (henry), dépend de N, ℓ, section (géométrie seule) ; fer doux augmente L ; bobine
  inductive / purement inductive ; ordres de grandeur (≪ 1 H, 140 μH).
- Symbole et modèle équivalent d'une bobine ; **u_AB = L di/dt + r i** (convention A→B) ; calcul de u_AB
  à partir d'un i(t) donné (polynôme, triangulaire/dents de scie) ; calcul de di/dt à partir de e(t) en
  créneaux ; tracé de i(t) ou u(t) par morceaux.
- Bilan de puissance p = ri² + d/dt(½Li²) ; **E_L = ½ L i²** ; réservoir temporaire vs condensateur
  réservoir permanent ; rôle de la diode ; étincelle de rupture et ordre de grandeur e ≈ L Δi/Δt.
- Alternateur (induit fixe/mobile, rotor/stator) et transformateur (alternatif seulement), qualitatif.
- Dipôle RL (R = R₀ + r) soumis à un **échelon de tension** : régimes transitoire / permanent ; I₀ = E/R ;
  bobine ≡ résistor r en régime permanent ; équation différentielle **di/dt + (1/τ)i = E/L** ; résolution par
  la forme proposée Ae^(−αt) + B et identification ; **i(t) = (E/R)(1 − e^(−t/τ))** ; u_bobine(t) =
  Ee^(−t/τ) + r(E/R)(1 − e^(−t/τ)), u(0) = E, limite rE/R ; équation en u_R₀ (exercice résolu).
- **Rupture** : di/dt + (1/τ)i = 0 ; **i(t) = (E/R)e^(−t/τ)** ; u_AB = (r/R − 1)Ee^(−t/τ) ; saut de u_AB
  (− E si r = 0) ; continuité de i.
- **τ = L/R** : influence de R (t ∝ 1/R) et de L (t ∝ L) à partir d'oscillogrammes ; homogénéité ;
  détermination par calcul direct, par la **tangente à l'origine** (établissement et rupture), par **0,63 E/R**
  et **0,37 E/R** ; régime permanent « pour t = 5τ » (corrigé ex.8).
- Exploitation d'oscillogrammes/courbes d'acquisition : identifier u_AM, u_BM, u_bobine, lire U₀, I₀, τ, en
  déduire r, L, énergie ; branchement de l'oscilloscope (masse, voie, bouton INV, masse flottante du GBF).

⛔ **Exclu** (absent du chapitre)
- Flux magnétique Φ, loi de Faraday e = − dΦ/dt, calcul de L = μ₀N²S/ℓ : **aucune formule** de l'inductance
  en fonction de N, ℓ, S (seulement le sens de variation qualitatif) ; pas de μ₀.
- Force de Laplace, rails de Laplace, induction par conducteur mobile, f.e.m. de mouvement.
- Calcul quantitatif sur alternateurs et transformateurs (rapport de transformation, nombre de spires) ;
  courants de Foucault seulement en lecture (« En savoir plus »).
- Inductances en série/parallèle, mutuelle inductance, bobine à noyau (e = −L di/dt « n'est plus valable »).
- Régime sinusoïdal forcé, impédance, oscillations RLC (chapitres 3–4) ; dipôle RC hors rappels (chap.1).
- Résolution d'équations différentielles par méthode générale (variation de la constante, etc.) : seule la
  forme proposée Ae^(−αt) + B est utilisée ; pas de demi-vie t½ = τ ln 2 dans le cours.
- Calcul de l'énergie dissipée par effet Joule pendant le transitoire (intégrale) : non traité.

### Lecture

- **Couche texte** lue en entier : p.42–77 (p.66 et p.73 : couche texte vide) et p.316–318.
- **Pages vues sur l'image** (36) : p.42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
  59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76 et 316. Non vues sur l'image : p.77
  (prose seule, « En savoir plus ») et p.317–318 (corrigés des chapitres 5–11, liste d'URL : aucun contenu
  du chapitre 2 hors URL).
- **Sondage / écarts texte → image constatés** : la couche texte perd toutes les fractions, exposants et
  indices (p.50–51, 59–62, 65–66, 69–70 : formules reconstituées entièrement sur l'image) ; p.66 et p.73 sans
  texte (méthodes graphiques de τ, ex.6–9 lus uniquement sur l'image) ; le tableau de Lenz p.47 et le tableau
  des bobines p.51 sont déstructurés dans le texte ; les signes des impulsions des Fig.4a/4b/7c/7d, les
  courbes Fig.12, 19, 23, 27 et les graphes des ex.5, 7, 10, 11, 12 n'existent que sur l'image ; p.316 :
  OCR mélange les colonnes (réponses ch.2 lues sur l'image).
- **Doutes [?]** :
  1. p.54–55 : tension du condensateur notée tantôt u_AM (manip., question 3°), tantôt u_AB (interprétation) ;
     Fig.15 place C entre A et B.
  2. p.55 : « p_L = L.di/dt » imprimé sans le facteur i.
  3. p.47 : « vecteur champ inducteur b⃗ » (minuscule) — notation incohérente avec le tableau (B⃗ inducteur).
  4. p.69–70 (exercice résolu) : « (B/α) » au lieu de B/τ ; « 3,45 V » vs « 3,54 V ».
  5. Corrigé ex.12 4°) « e ≃ 3,3 V » : avec I₀ = 50 mA et R = 50 Ω on attendrait R·I₀ = 2,5 V ; et 2°b)
     « i(t₁/₂) = I₀/2 → τ = 22 ms » ne passe pas par ln 2 — valeurs reportées telles qu'imprimées, non
     vérifiables sans hypothèse.
  6. Corrigé ex.11 « r' = 10 ? » : lire r = 10 Ω (r' = 50 Ω est donné).
  7. Ex.8 6°) : le symbole de la constante de temps manque à l'impression (« Définir la constante de temps
     pour le régime transitoire »).
  8. p.61 renvoie au « paragraphe 5 … page 54 » alors que le §5 commence p.53.
  9. Tableaux des durées t (p.63–64) : non remplis par le manuel ; aucune valeur à reprendre.
  10. Ex.1 (vrai/faux), ex.2 (QCM), ex.10 9°), ex.14 : aucune réponse au corrigé p.316.

## 2.3 Chapitre 3 — Oscillations électriques libres (manuel 223433, p.78–109)

**Partie** : « Evolution de systèmes » (bandeau de chaque page). Le chapitre a **deux grandes parties**
titrées : « OSCILLATIONS ÉLECTRIQUES LIBRES AMORTIES » (p.80–87) et « LES OSCILLATIONS ÉLECTRIQUES LIBRES
NON AMORTIES » (p.88–94), puis « L'essentiel » (p.95), « Exercices » (exercice résolu p.96–99, exercices à
résoudre p.100–106), « Fiche technique » (p.107–109).

**Page d'ouverture (p.79)** — « OSCILLATIONS ÉLECTRIQUES LIBRES », n° 3 ; photo d'une montre à quartz,
légende : « Le quartz impose sa fréquence propre aux oscillations ; une montre électronique y gagne en
précision. » Questions d'accroche : « Que désigne-t-on par les expressions “oscillations électriques”,
“oscillateur électrique”, “circuit oscillant”...? » ; « Est-ce que le courant alternatif est un phénomène
oscillatoire ? »

**Objectifs (p.78)** (verbatim) : Réaliser un montage permettant de suivre les oscillations libres d'un
circuit RLC série. · Reconnaître le régime pseudopériodique et le régime apèriodique. · Reconnaître le
facteur responsable de l'amortissement. · Reconnaître les grandeurs oscillantes d'un circuit RLC série. ·
Etablir l'équation différentielle des oscillations libres d'un circuit RLC série. · Interpréter la diminution
de l'amplitude des oscillations libres d'un circuit RLC série par le transfert d'énergie de l'oscillateur
vers le milieu extérieur. · Ecrire l'expression d'une grandeur oscillante en régime libre non amorti. ·
Définir la pulsation propre ω₀ et la période propre T₀ d'un oscillateur RLC non amorti. · Exprimer T₀ en
fonction de L et de C. · Déterminer la période, l'amplitude et la phase initiale d'une grandeur oscillante
sinusoïdale d'un circuit RLC série non amorti. · Démontrer la conservation de l'énergie totale d'un
oscillateur LC. · Interpréter le cas particuler des oscillations libres non amorties.

**Prérequis (p.78)** — SAVOIR : Définir un phénomène périodique. · Définir la période T et la fréquence N
d'un phénomène périodique. · Ecrire la relation N = 1/T. · Ecrire la relation i = dq/dt. · Ecrire
l'expression de la tension : aux bornes d'un condensateur u = q/c ; aux bornes d'une bobine u = ri + L di/dt.
· Exprimer l'énergie potentielle électrique E_C emmagasinée par un condensateur. · Exprimer l'énergie
magnétique E_L emmagasinée par une bobine. — SAVOIR FAIRE : Reconnaître un phénomène périodique. ·
Distinguer entre période et fréquence d'un phénomène périodique. · Utiliser la relation i = dq/dt. ·
Expliquer la charge et la décharge d'un condensateur. · Expliquer le phènomène d'auto-indution. · Distinguer
entre transfert et transformation d'énergie. · Appliquer la loi des mailles.

**Plan (titres numérotés du manuel)** :
- *Oscillations électriques libres amorties* (p.80) — intro : « Que se passera-t-il si l'on décharge le
  condensateur dans une bobine sachant que celle-ci emmagasine aussi de l'énergie? »
  1. Production d'oscillations libres amorties (p.80) · 2. Influence de l'amortissement (p.83) ·
  3. Équation différentielle régissant l'évolution d'un circuit RLC série en régime libre (p.85) ·
  4. Énergie totale d'un oscillateur RLC série (p.85).
- *Les oscillations électriques libres non amorties* (p.88) — intro : « … l'oscillateur LC non amorti est
  un cas idéal parce qu'il est impossible de le réaliser dans la pratique » ; étude « uniquement, par une
  étude théorique ».
  1. Nature des oscillations libres non amorties (p.88) : 1.1- Évolution de la charge du condensateur ;
  (Simulation des oscillations, p.89) ; 1.2- Période et fréquence des oscillations (p.90) ; 1.3- Amplitude
  et phase initiale des oscillations (p.90) · 2. Énergie totale d'un oscillateur LC (p.92) : 2.1-
  Conservation de l'énergie totale ; 2.2- Évolution des énergies électrique et magnétique (p.93).

### Cours — Manipulations, questions, interprétations

**Partie A. 1 — Production d'oscillations libres amorties (p.80–83)**
- **Manipulation** (p.80) : générateur de tension idéal E = 5 V ; condensateur C = 0,5 μF ; résistor R₀
  réglable, **R₀ = 100 Ω** ; bobine L = 1 H, r = 12,5 Ω ; commutateur K. Fig.1 (schéma) : position 1 = E
  charge C ; position 2 = C se décharge dans la bobine (L ; r) en série avec R₀ ; voie Y₁ : u_C = u_NM ;
  voie Y₂ : u_R₀ = u_AM ; masse en M ; oscilloscope à mémoire. Fig.2 : oscillogrammes ① et ② (deux
  sinusoïdes amorties décalées).
- **Questions** (p.80–81) : 1°) forme du chronogramme K en position 1 ; 2°) montrer que ① correspond à
  u_C et traduit q(t) ; 3°) ② traduit i(t) dans le circuit MNKA ; 4°) « Tels quels, les chronogrammes ① et ②
  traduisent des oscillations de q et de i » — signification ; pourquoi « amorties » ? 5°) comparer les
  intervalles T entre maximums ou minimums successifs de u_C et de u_R₀ ; 6°) en comparant les maximums,
  montrer que les oscillations sont amorties ; pourquoi « pseudopériodiques » ? 7°) interpréter les
  oscillations de q(t) et de i(t).
- **Interprétation** (p.81–83) : en position 1, u_C devient égale à E ⇒ ① = u_C(t). Par « q = C u_C et
  u_R₀ = R₀ i », ① et ② traduisent q(t) et i(t). Symétrie par rapport à l'axe des temps : q et i changent de
  signe à intervalles successifs égaux à T/2 ⇒ « q et i oscillent ». « On dit qu'un tel courant alternatif
  est un phénomène oscillatoire. » Récit par étapes (Fig.3 sens positif du courant, Fig.4a–4d) :
  t₀ = 0 : u_C0 = E, Q₀ = CE sur A et −Q₀ sur B ; électrons de B vers A, courant dans le sens négatif ;
  |i| ne passe pas instantanément de 0 à I_m « à cause de la f.e.m. auto-induite » ; [0, T/4] augmentation
  progressive de |i| ; à T/4 condensateur déchargé mais i ne s'annule pas (« fem auto-induite e = − L di/dt »)
  ⇒ charge de signe opposé ; à T/2 charges +Q₁ < 0 et −Q₁ > 0 maximales en valeur absolue, courant
  régénéré dans le sens positif ; à T charges +Q₂ (positive) ; à 3T/2 Q₃ < 0, à 2T Q₄ > 0. Fig.5 :
  Q₀ > |Q₁| > Q₂ > |Q₃| — diminution de l'amplitude due à la résistance totale R = R₀ + r. « De telles
  oscillations sont dites amorties. De plus, ces oscillations sont dites libres du fait qu'elles se
  produisent dans le circuit RLC série bien que celui-ci ne soit fermé sur aucun générateur. » Extrêmums
  atteints à intervalles égaux mais amplitude décroissante ⇒ « pseudopériodiques ».

**Partie A. 2 — Influence de l'amortissement (p.83–85)**
- **Manipulation** (p.83) : montage de la Fig.1, R₀ variable ; Fig.6a–6f : R₀ = 100 Ω, 500 Ω, 1000 Ω
  (oscillations de moins en moins nombreuses), 3 kΩ, 4 kΩ, 5 kΩ (plus d'oscillation : retour sans
  dépassement oscillant, de plus en plus lent).
- **Questions** : 1°) influence de la résistance sur l'amortissement et sur la pseudopériode ; 2°) conditions
  pour que le RLC oscille librement ; 3°) comparer 6.d, 6.e, 6.f ; influence de R₀ sur la durée du retour à
  l'état d'équilibre stable.
- **Analyse et interprétation** (p.84) : R₀ augmente ⇒ oscillations plus amorties (« le nombre total des
  oscillations diminue ») et pseudopériode T « augmente légèrement » (6a–6c). Pour R₀ élevée : plus
  d'oscillation, « simple décharge du condensateur ; celle-ci demande une durée aussi longue que la
  résistance R₀ est plus grande : un tel régime non oscillatoire est dit apériodique » (6d–6f).
- **Remarques** (p.84) : 1- « Le régime apériodique obtenu avec la valeur élevée la plus petite de la
  résistance totale R du circuit RLC série est connu sous le nom du régime critique mais expérimentalement,
  il est difficile de le mettre en évidence. » 2- à la limite d'un amortissement nul (pas de résistor, bobine
  de très petite r), « le régime pseudopériodique devient périodique (Fig.7) ».

**Partie A. 3 — Équation différentielle (p.85)** — Fig.8 : schéma RLC série (q, u_C, u_b, u_R₀, i).
Démonstration par la loi des mailles (voir Encadrés).

**Partie A. 4 — Énergie totale d'un oscillateur RLC série (p.85–87)**
- **Manipulation** : montage de la Fig.1, oscilloscope remplacé par une interface d'acquisition (« console
  VTT par exemple ») ; R₀ = 100 Ω (Fig.9 : u_C(V) de −5 à 5, t de 0 à 12 ms, u_C part de 5 V) puis
  R₀ = 500 Ω (Fig.10, oscillations fortement amorties en ~8 ms). Tableur-grapheur : E_C = ½ C·u_C² ;
  E_L = ½ (L/R₀²)·u_R₀² ; E = E_C + E_L. Fig.11a (R₀ = 100 Ω) et 11b (R₀ = 500 Ω) : énergie totale (enveloppe
  décroissante), énergie électrique, énergie magnétique, axe « En(μJ) » 0 à 0,6, t de 0 à 10 ms.
- **Questions** (p.86) : 1°) zéros et maxima de E_C ou E_L à intervalles égaux à T/2 ; 2°) E = E_C + E_L ;
  3°) transformations mutuelles de E_C et E_L ; 4°) influence [de la résistance] sur la vitesse de diminution
  de l'énergie totale (le mot « de la résistance » manque dans l'énoncé imprimé).
- **Interprétation** : « Non conservation de l'énergie totale d'un circuit RLC série » (dE/dt = −Ri², voir
  Encadrés). « L'énergie totale emmagasinée dans le circuit RLC série diminue au cours du temps, elle est
  transformée progressivement en énergie thermique par effet Joule. Cette dissipation est d'autant plus
  rapide que la résistance est plus grande. En conséquence, on dit qu'un circuit RLC série en régime libre
  est un système non conservatif. » « Transformations mutuelles des énergies électrique et magnétique » :
  entre nT et nT + T/4, E_C diminue (|q| diminue), E_L augmente (|i| augmente) ⇒ transformation E_C → E_L ;
  entre nT + T/4 et nT + T/2, l'inverse ; transformations « pas intégrales » : à chaque transfert une partie
  est transférée par chaleur au milieu extérieur, d'où l'amortissement et la cessation.

**Partie B. 1.1 — Évolution de la charge (p.88–89)** — Fig.12 : C initialement chargé fermé sur une bobine
« supposée purement inductive » (u_C, u_L, i). Équation, solution admise, vérification (voir Encadrés).
- **Simulation des oscillations** (p.89) : logiciel résolvant d²q/dt² + (1/LC)q = 0 avec L = 10 mH,
  C = 100 μF, Q_m = 6.10⁻⁴ C (Fig.13 : champs « U = 6 V, C = 100 μF, L = 10 mH, Q₀ = 0,6 mC », échelles
  1 V/div et 1 ms/div ; sinusoïde q(t) démarrant à son maximum).

**Partie B. 1.2 — Période et fréquence (p.90)**
- **Questions** : 1°) avec la Fig.13, calculer T₀ et en déduire N₀ ; 2°) vérifier avec L et C que
  T₀ = 2π√(LC).
- **Remarque** : « … la valeur obtenue pour T₀ (réponse à la question n°1 ci-dessus : T₀ = 6,28 ms) montre
  que l'oscillateur RLC série non amorti a une période propre très inférieure à la seconde. »

**Partie B. 1.3 — Amplitude et phase initiale (p.90–92)**
- Deuxième simulation, mêmes L et C, Q′_m = 9.10⁻⁴ C (Fig.14 : second jeu « U = 9 V, C = 100 μF, L = 10 mH,
  Q′₀ = 0,9 mC » ; deux sinusoïdes de même période, amplitudes différentes). Amplitudes relevées = charges
  initiales Q_m et Q′_m. Phase : origine des temps à la fermeture, q(0) = Q₀ ⇒ Q_m sinφ = Q₀ ⇒ sinφ = 1 ⇒
  φ = π/2 rad ; autre origine ⇒ autre φ.
- **Questions** (p.92) : 1°) sachant q(t) = Q_m sin(ω₀t + π/2), montrer i(t) = ω₀Q_m cos(ω₀t + π/2) ;
  2°) en déduire i(t) = I_m sin(ω₀t + φ) en précisant I_m et φ.

**Partie B. 2.1 — Conservation de l'énergie (p.92–93)** — démonstration (voir Encadrés).
- **Questions** : 1°) comparer E à l'énergie transférée initialement ; prévisible ? 2°) montrer
  E = ½ L·I_m² sachant I_m = ω₀Q_m et LCω₀² = 1 ; 3°) montrer autrement, par dE/dt, que E est constante,
  cas particulier de dE/dt = − Ri².

**Partie B. 2.2 — Évolution des énergies électrique et magnétique (p.93–94)** — Fig.15 : q (courbe 1) et
i (courbe 2) pour q = Q_m à t = 0, graduations T₀/4, T₀/2, 3T₀/4, T₀. À t = 0 : « E = E_Cmax = Q_m²/2C »,
énergie purement électrostatique ; ]0, T₀/4[ : q diminue, i négative augmente en valeur absolue, E_C → E_L ;
à T₀/4 : « E = E_Lmax = ½ L I_m² », purement magnétique ; ]T₀/4, T₀/2[ : « la bobine joue le rôle de
générateur en chargeant progressivement le condensateur », E_L → E_C ; à T₀/2 : purement électrostatique ;
deuxième demi-période identique (q de −Q_m à +Q_m, courant dans le sens positif) ; « transformation
mutuelle … mais sans aucune perte ». Enregistrement : C = 0,47 μF, L = 0,1 H, U₀ = 5 V (Fig.16 : E₀ en
palier à 5,875 μJ ; E_C et E_L sinusoïdales en opposition ; graduations 0,34 ; 0,68 ; 1,02 ; 1,36 ms).
- **Questions** (p.94) : 1°) interpréter énergétiquement les oscillations non amorties (R nulle) ;
  2°) avec Fig.16 : a) E_C et E_L périodiques ; b) périodes de E_C et E_L, comparées entre elles et à T₀ ;
  c) relever E et la comparer à E₀ ; 3°) montrer théoriquement E_C = (Q_m²/4C)(1 + cos 2ω₀t) et
  E_L = ¼ L I_m² (1 − cos 2ω₀t) sachant q = Q_m cos ω₀t ; vérifier E constante et égale à l'énergie
  transférée initialement.

### Encadrés, lois, relations (VERBATIM, vérifiés sur l'image de leur page)

> **Conclusion** (p.83) — « Un circuit constitué d'un dipôle RL série fermé sur un condensateur initialement
> chargé peut être le siège d'oscillations électriques amorties. De telles oscillations qui s'effectuent
> d'elles mêmes sans intervention de l'extérieur sont dites libres. Les oscillations libres amorties sont des
> oscillations pseudopériodiques de pseudopériode T. »

> **Conclusion** (p.85) — « Un circuit RLC série fermé, avec le condensateur initialement chargé, ne peut
> osciller librement que lorsque l'amortissement est faible. Plus la résistance du circuit est grande, plus
> la pseudopériode est grande et plus le retour de l'oscillateur à son état d'équilibre est rapide. Avec des
> valeurs élevées de R, le régime n'est plus oscillatoire, il est apériodique » [?] (voir Doutes : contredit
> l'analyse p.84).

> **Équation différentielle RLC série** (p.85) — « u_C + u_b + u_R₀ = 0, ce qui signifie q/C + (ri + L di/dt)
> + R₀i = 0. D'où : L di/dt + (r + R₀)i + q/C = 0. (1) Or, i = dq/dt. Donc, (1) s'écrit :
> L d²q/dt² + (r + R₀) dq/dt + q/C = 0 ou bien d²q/dt² + ((r + R₀)/L) dq/dt + (1/LC) q = 0 »

> **Énergies** (p.86) — « E_C = ½ C.u_C² » ; « E_L = ½ (L/R₀²).u_R₀² » ; « E = E_C + E_L ».

> **Non-conservation** (p.86) — « dE/dt = d/dt(q²/2C + (L/2)i²) = (q/C)(dq/dt) + Li di/dt = i(L di/dt + q/C).
> Or l'équation différentielle peut s'écrire : L di/dt + q/C + Ri = 0, ce qui donne L di/dt + q/C = − Ri,
> d'où **dE/dt = − Ri²** » (encadré). Encadré latéral : « La vitesse de variation de l'énergie totale d'un
> système dE/dt n'est autre que la puissance instantanée p du même système : p = dE/dt ».

> **Oscillateur LC** (p.88) — « u_C + u_L = 0, ce qui signifie q/C + L di/dt = 0. Or i = dq/dt, d'où
> d²q/dt² + ω₀²q = 0 avec ω₀² = 1/LC : constante positive ». « On admet que la solution générale d'une
> telle équation différentielle est de la forme : q(t)=Q_m sin(ω₀t + φ). ω₀ : pulsation des oscillations de la
> charge q, exprimée en radians par seconde (rad.s⁻¹). Q_m : amplitude des oscillations de la charge q,
> exprimée en coulombs (C). φ : phase initiale de la charge q, exprimée en radians (rad). φ(t) = ωt + φ : phase
> à l'instant t, exprimée en radians (rad) » (indice o absent de « ωt » dans l'imprimé).
> Vérification (p.88–89) : d²q/dt² = − ω₀²q ⇒ « − ω₀²q + (1/LC)q = 0 », « q(1/LC − ω₀²) = 0 quel que soit q »,
> « ω₀ = 1/√LC ».

> **Conclusion** (p.89) — « La charge q du condensateur d'un circuit LC (circuit RLC série non amorti) oscille
> sinusoïdalement au cours du temps avec la pulsation ω₀ = 1/√LC. Ne dépendant que des grandeurs L et C
> caractéristiques du circuit, la pulsation des oscillations libres non amorties est qualifiée de pulsation
> propre de l'oscillateur. »

> **Période et fréquence propres** (p.90) — « La pulsation ω₀ étant propre à l'oscillateur, la période des
> oscillations T₀ = 2π/ω₀ est appelée période propre. » Encadré : **T₀ = 2π√LC**. « De même, la fréquence des
> oscillations N₀ = 1/T₀ est appelée fréquence propre des oscillations. » Encadré : **N₀ = 1/(2π√LC)**.

> **Conclusion** (p.91) — « L'amplitude et la phase initiale des oscillations libres d'un circuit RLC série
> non amorti ne dépendent que des conditions initiales. Toutefois, la valeur de l'amplitude est tributaire de
> la valeur de la charge initiale du condensateur, tandis que la valeur de la phase initiale est fonction du
> choix arbitraire de l'origine des temps. »

> **Conservation** (p.92) — « E = E_C + E_L = (1/2C)q² + ½Li². Avec q = Q_m sin(ω₀t + π/2), i = dq/dt =
> Q_mω₀ cos(ω₀t + π/2). Donc, E = (1/2C)(Q_m cosω₀t)² + ½L(− Q_mω₀ sin ω₀t)². E = (Q_m²/2C)cos²(ω₀t) +
> ½Lω₀²Q_m² sin²(ω₀t). Or, ω₀² = 1/LC, il vient : E = (Q_m²/2C)[(cos²(ω₀t) + sin²(ω₀t)] … Donc,
> E = (1/2C)Q_m². Q_m et C étant des constantes, E reste constante au cours du temps : on dit que l'énergie
> totale de l'oscillateur LC se conserve. »

> **Conclusion** (p.93) — « L'oscillateur RLC série en régime libre non amorti est un système conservatif. Son
> énergie est proportionnelle au carré de l'amplitude de la grandeur oscillante q(t) ou i(t). »
> Encadré : **E = Q_m²/2C = ½ L.I_m² = ½ C U_Cm²**.

> **Conclusion** (p.94) — « Les oscillations libres d'un circuit RLC série non amorti sont dues aux
> transformations mutuelles et intégrales de ses énergies électrostatique et magnétique : l'énergie totale du
> système est transférée continuellement de manière intégrale du condensateur à la bobine et inversement. »

### L'essentiel (p.95, verbatim)

- « L'évolution de la charge du condensateur d'un circuit RLC série est régie en régime libre par l'équation
  différentielle : **d²q/dt² + (R/L) dq/dt + (1/LC) q = 0** »
- « Un circuit RLC série auquel on a transféré initialement de l'énergie peut être le siège d'oscillations
  électriques libres amorties, c'est le régime pseudo-périodique. »
- « Les oscillations libres d'un circuit RLC série sont d'autant plus amorties et leur pseudopériode est
  d'autant plus grande que la résistance R du circuit est plus grande. Pour des valeurs suffisamment élevées
  de la résistance R, c'est le régime apériodique. »
- « Si la résistance d'un circuit RLC série est nulle, les oscillations libres ne sont plus amorties, elles
  sont sinusoïdales, c'est le régime périodique. »
- « La période propre d'un oscillateur RLC série s'exprime : **T₀ = 2π√LC** »
- « La pseudo-période des oscillations libres amorties d'un circuit RLC série est légèrement supérieure à T₀. »
- « Les oscillations libres d'un circuit RLC série sont dues aux transformations mutuelles de ses énergies
  électrostatique et magnétique. »
- « En régime libre, l'énergie totale d'un circuit RLC série ne se conserve que si sa résistance électrique
  est nulle. »

### Exercice résolu (p.96–99)

**Énoncé** : E = 5 V (idéal), C = 1 μF, bobine L = 10 mH et r, R = 90 Ω, oscilloscope à mémoire,
interrupteur. Fig.1 : E en série avec R et K, puis C en parallèle avec la bobine (L ; r) entre A et B ;
Y₁ en A, masse en B. 1°) r supposée nulle : a) K fermé : tension aux bornes de la bobine nulle, charge du
condensateur ; I₀ ; b) ouverture de K à t = 0 : description qualitative ; équation différentielle en u ;
avec u = U_m sin(ω₀t + φ), ω₀ = 1/√LC à calculer, U_m et φ ; q(t) et i(t) ; c) origine et valeur de
l'énergie de l'oscillateur. 2°) oscillogramme Fig.2 (u_AB ; 1 V/div ; 0,2 ms/div ; palier avant 0, puis
oscillations amorties, instants t₁ et t₂ à deux maxima successifs) : a) montrer par deux méthodes que r ≠ 0 ;
b) calculer r ; c) pseudo-période T comparée à T₀ ; d) variation algébrique de l'énergie totale entre t₁ et t₂.

**Solution** :
- 1°a) u₁ = ri + L di/dt ; régime permanent di/dt = 0 ⇒ u₁ = r.i = 0 V ; sens positif de B vers A à travers
  le condensateur, u_AB = − q/C = 0 ⇒ « la charge q est nulle » ; condensateur = interrupteur ouvert ;
  loi de Pouillet **I₀ = E/R**, A.N. I₀ = 55,5 mA.
- 1°b) auto-induction, loi de Lenz : le courant continue dans le même sens, le condensateur se charge puis se
  décharge… « le circuit RLC série est le siège d'oscillations libres non amorties ». u_C + u_L = 0 ;
  u − L di/dt = 0 ; i = dq/dt et q = − C.u ⇒ i = − C du/dt ⇒ u + LC d²u/dt² = 0 ⇒
  **d²u/dt² + (1/LC)u = 0**. ω₀ = 1/√LC = 10⁴ rad.s⁻¹. À t = 0, u = U_m sinφ = 0 ⇒ φ = 0 ou π ;
  i = − CU_mω₀cos(ω₀t + φ), à t = 0 i = − CU_mω₀cosφ = I₀ > 0 ⇒ cosφ < 0 ⇒ **φ = π rad** ;
  U_m = I₀/(Cω₀) ≃ 5,55 V. **u(t) = 5,55 sin(10⁴t + π)** ; **q = 5,55.10⁻⁶ sin(10⁴t)** ;
  i = CU_mω₀ sin(ω₀t + φ − π/2), I_m = I₀ = 55,5 mA, **i = 55,5 sin(10⁴t + π/2)** en mA.
- 1°c) énergie conservée = énergie magnétique initiale **E = ½ L.I₀²**, A.N. E = 1,54.10⁻⁵ J.
- 2°a) méthode 1 : diminution de l'amplitude due à r ; méthode 2 : pour t < 0, u = 0,5 V = u_AB ≠ 0 ⇒
  r = u_AB/I′₀ non nulle. 2°b) r = u/I′₀, I′₀ = E/(r + R) ⇒ **r = u.R/(E − u)**, A.N. r = 10 Ω.
- 2°c) T = t₂ − t₁ ≈ 3,25 div × 0,2 ms ⇒ **T = 0,65 ms** ; T₀ = 2π/ω₀ = 0,628 ms ⇒ « T est légèrement
  supérieure à T₀ ».
- 2°d) en t₁ et t₂, |u| maximale ⇒ énergie purement électrostatique ; E₁ = ½CU_m1², E₂ = ½CU_m2² ;
  U_m1 = 5 V, U_m2 = 4,5 V ; **E₂ − E₁ = ½C(U_m2² − U_m1²)** = − 2,375.10⁻⁶ J.

### Exercices à résoudre (p.100–106) — réponses p.316 (colonne « Chapitre 3 »)

**Tests rapides des acquis**
- **1 Vrai ou faux** (p.100) : 1- décharge dans une bobine identique à la décharge dans un résistor ;
  2- pseudo-période légèrement inférieure à la période propre ; 3- le RLC transfère son énergie à l'extérieur
  d'autant plus rapidement que sa résistance est plus grande ; 4- en pseudo-périodique, le nombre
  d'oscillations augmente quand la pseudo-période augmente ; 5- oscillations libres d'un RLC amorti dues à
  des transformations intégrales des énergies. (Pas de corrigé.)
- **2 QCM** (p.100) : I- amortissement dû à : a capacité, b inductance, c résistance du résistor,
  d résistance de la bobine, e sa résistance totale ; II- décharge dans une bobine purement inductive :
  a périodiques, b sinusoïdales amorties, c pseudo-périodiques non amorties, d incessantes ; III- T₀ :
  a 2π√(L/C), b 2π√(1/LC), c 2π√LC ; IV- un RLC ne peut entrer en oscillations libres : a sans lui
  transférer initialement de l'énergie, b sans lui transférer sans cesse de l'énergie, c sans qu'il transfère
  lui-même de l'énergie à l'extérieur, d sans les transformations mutuelles. (Pas de corrigé.)

**Exercices d'application**
- **Ex. 3** (p.100–101) : bobine (r, L), C = 15 μF, pile plate E = 4,5 V, R = 1 kΩ (charge, Fig.1
  commutateur 1/2), acquisition de u_C ; Fig.2 (1 V/div, 20 ms/div, oscillations amorties depuis ~4,5 V).
  1°) phénomène ; 2°) énergie du condensateur à t = 0 et après deux oscillations, transformations sur une
  pseudopériode ; 3°) équation en u_C si r nulle ; 4°) ω₀, T₀ littéraux, T ≈ T₀ ⇒ L. — Rép. : 1°)
  oscillations libres amorties ; 2°) E = 1,52.10⁻⁴ J ; 4°) L = 2,67 H.
- **Ex. 4** (p.101) : L = 1 H, résistance R, C = 1 μF ; graphe u_C (oscillante) et E_C (toujours ≥ 0),
  échelle « 1ms », ordonnées non graduées. 1°) R non nulle ; 2°) T ; 3°) comparer à T₀ ; 4°) T_E ;
  5°) comparer. — Rép. : 1°) l'amplitude décroît ; 2°) T = 6,5 ms ; 3°) T₀ = 6,28 ms ; 4°) T_E = 3,3 ms ;
  5°) T = 2T_E.
- **Ex. 5** (p.101) : C = 0,47 μF chargé sous 5 V, L = 44 mH, résistance nulle. 1°a) équation en u_C, T₀ ;
  b) u_C(t) ; c) q(t) ; 2°) C′ = 4C, L′ = L/2 : T′₀ en fonction de T₀. (Pas de corrigé.)
- **Ex. 6** (p.102) : d²q/dt² + (1/LC)q = 0 (1), Q₀ = 4.10⁻⁴ C. 1°) énergie totale ; 2°) retrouver (1) par la
  conservation de l'énergie ; 3°) vérifier q = Q_m sin(ω₀t + φ) ; 4°) T₀ littéral et numérique ;
  5°) constantes de q(t), circuit fermé à t = 0 ; C = 30 μF, L = 0,1 H. (Pas de corrigé.)
- **Ex. 7** (p.102) : C = 1,16 μF, L = 0,35 H, r ; T = 4,4 ms ; graphe u(V) (−2 à 2), maxima numérotés 1 à 7.
  1°) T vs T₀ ; 2°) énergie électrique en t₁ et t₇ ; 3°a) énergie magnétique et totale aux mêmes instants ;
  b) conclure. — Rép. : 1°) T₀ = 4,0 ms, T = 4,4 ms, T > T₀ ; 2°) E₁ = 1,485 μJ, E₇ = 0,145 μJ ;
  3°b) l'énergie totale diminue.

**Exercices de synthèse**
- **Ex. 8** (p.102–103) : E = 6 V, C = 20 μF, L = 0,8 H (r nulle), deux R = 20 Ω, K₁, K₂ (Fig.1).
  A- K₁ fermé : 1°) phénomène (voie 1) ; 2°) schéma, sens du courant, signes des charges, flèche u₁ ;
  3°) Fig.2 (u₁ de 0 à 6 V en ~1,5 ms, t en ms) : τ graphique, C avec R = 20 Ω ; 4°) τ du₁/dt + u₁ = E :
  a- retrouver ; b- u₁ = E[1 − exp(−t/τ)], u₁(5τ), conclure. B- K₁ ouvert, K₂ fermé : Fig.3 (5 ms/div ;
  1 V/div u₁ ; 0,2 mV/div u₂) : 1°) attribuer les courbes ; 2°) équation de u₂(t) ; 3°) T vs T₀ ; 4°) Fig.4
  et 5 : L augmentée ou R augmentée, attribuer. (Pas de corrigé.) [Mobilise le dipôle RC du chapitre 1.]
- **Ex. 9** (p.103–104) : C = 10 μF chargé sous U₀ = 3 V. 1°) charge et énergie ; 2°) relié à t = 0 à L = 0,1 H,
  résistance nulle : a) schéma, allure à l'oscilloscope ; b) interprétation énergétique ; c) équation en
  u_C ; d) relation T₀, C, L pour u_C = U_m sin(ω₀t + φ) ; e) U_m, φ ; f) instants de |i| maximale en
  fonction de T₀ ; 3°) r non nulle, oscillogramme 10 ms/div : a- T vs T₀ ; b- pourquoi un oscilloscope à
  mémoire ; c- énergie thermique dissipée entre t₀ = 0 et t₁ = T. — Rép. : 1°) Q₀ = 3.10⁻⁵ C ;
  2°b) « Voir cours page 2° » [libellé du corrigé] ; d) U_m = 3 V, φ = π/2 rad ; 2°f) t_k = 0,75 T₀ + kT₀ ;
  3°a) T > T₀ ; 3°c) W_J = 32,2 μJ.
- **Ex. 10** (p.104) : vérifier L = 0,2 H ; C = 0,5 μF chargé sous E = 6 V, décharge dans la bobine ; graphe
  u(V) de 6 V, t de 0 à 50 ms (oscillations amorties). 1°) pourquoi pseudopériodique ; 2°a) équation en u ;
  b) forme d²u/dt² + (1/τ) du/dt + ω₀²u = 0 : expliciter τ, dimension, signification ; τ approché ⇒ L,
  R = 20 Ω ; c) écart relatif (L_exp − L)/L, indication correcte ? — Rép. : 1°) l'amplitude diminue ;
  2°b) L = 0,255 H ; 25 %.
- **Ex. 11** (p.104–105) : E = 6 V, C = 50 μF, R = 30 kΩ (charge), R₀ = 5 Ω, bobine L (Fig.1). 1°) charge
  (Fig.2 : courbes (1) croissante et (2) décroissante, u de 0 à ~6 V, t de 0 à 4 s) : a) courbe de u_C ;
  b) charge finale ; c) τ (63 %) ; d) i à t = τ. 2°) K en position 2 : Fig.3 (u_C sur Y₁, u_R₀ sur Y₂ ;
  5 ms/div ; 1 V/div Y₁, 250 mV/div Y₂ ; points P et Q) : a) E_C, E_L et leurs valeurs en P et Q ;
  b) comparer les énergies totales. — Rép. (p.316) : 1°a) « A t=0, u_C = E, donc (2) correspond à u_C » [?] ;
  1°c) τ = 0,7 s [?] ; 1°d) i ≃ 158 μA [?]. (Voir Doutes.)
- **Ex. 12 Étude de texte — Capteur d'humidité** (p.105–106) : hygrométrie (%HR) ; capteurs résistifs vs
  capacitifs (« humidistances ») ; condensateur plan C ≈ 120 pF, diélectrique polymère (polyamide) dont la
  permittivité varie avec l'humidité (Fig.1) ; inséré dans un RLC série (Fig.2) ; −10 °C à +40 °C, 10 à
  100 %HR, réponse ~30 s. 1°) pourquoi « hygroscopique » ; 2°) humidité ⇒ variation de N₀ ; 3°) C à 40 %HR
  [valeur non donnée], N₀ = 31850 Hz, L = 200 mH : taux d'humidité. (Pas de corrigé.)

### Fiche technique (p.107–109), en une ligne
« Visualisation d'un régime transitoire avec un oscilloscope analogique » : générateur de créneaux ±U₀ = ±5 V
(au lieu de E = 5 V), demi-période T_e/2 inférieure à la persistance rétinienne θ_p = 0,1 s et très
supérieure à T ⇒ « LC << θ_p² = 10⁻² s² » ; l'entrée d'oscilloscope ≡ R_osc = 1 MΩ ∥ C_osc (16 à 47 pF)
⇒ conditions R/R_osc << 1 et L/((R₀ + r)C) << R_osc = 10⁶ Ω ; exemples L = 10 mH, C = 100 μF (« très bon
choix ») vs L = 1 H, C = 1 μF (« mauvais choix »). Pas de rubrique « En savoir plus » dans ce chapitre.

### Bornes de scope (chapitre 3)

- ✅ INCLUS :
  - Décharge d'un condensateur chargé dans une bobine (L ; r) + résistor R₀ : circuit RLC série libre ;
    visualisation u_C (image de q par q = Cu_C) et u_R₀ (image de i par u_R₀ = R₀i) à l'oscilloscope à mémoire
    ou par acquisition informatisée.
  - Vocabulaire : oscillations libres, amorties, pseudopériodiques, pseudopériode T ; régimes
    pseudopériodique, apériodique, (critique, cité seulement) ; périodique (R nulle) ; amortissement dû à la
    résistance totale R = R₀ + r.
  - Influence qualitative de R : plus R grande ⇒ plus amorti, T augmente légèrement ; R élevée ⇒ apériodique.
    T légèrement supérieure à T₀ ; estimer T ≈ T₀ pour un faible amortissement.
  - Équation différentielle par la loi des mailles en q : d²q/dt² + (R/L)dq/dt + (1/LC)q = 0 ; aussi en u
    (exercices, avec q = ± Cu selon l'orientation) ; forme d²u/dt² + (1/τ)du/dt + ω₀²u = 0 (ex. 10).
  - Énergies E_C = ½Cu_C² = q²/2C, E_L = ½Li², E = E_C + E_L ; dE/dt = − Ri² ; p = dE/dt ; dissipation par
    effet Joule, système non conservatif ; transformations mutuelles E_C ↔ E_L non intégrales ; variation
    d'énergie entre deux maxima de |u| (½C(U_m2² − U_m1²)) ; énergie thermique dissipée sur une oscillation.
  - Oscillateur LC : d²q/dt² + ω₀²q = 0, ω₀² = 1/LC ; solution ADMISE q = Q_m sin(ω₀t + φ) et sa
    vérification ; ω₀ = 1/√LC, T₀ = 2π√LC, N₀ = 1/(2π√LC) ; amplitude et phase fixées par les conditions
    initiales (sinφ, signe de cosφ via i(0)) ; i = dq/dt = I_m sin(ω₀t + φ + π/2), I_m = ω₀Q_m ; u, q, i
    écrits numériquement ; instants où |i| est maximale.
  - Conservation E = Q_m²/2C = ½LI_m² = ½CU_Cm² ; E_C = (Q_m²/4C)(1 + cos 2ω₀t), E_L = ¼LI_m²(1 − cos 2ω₀t) ;
    période des énergies = T₀/2 (T = 2T_E).
  - Lecture d'oscillogrammes/chronogrammes : pseudopériode (nombre de divisions × sensibilité), amplitudes
    successives, période propre ; calculs T₀, L, C à partir de T ; T′₀ après changement de L et C ;
    capteur capacitif (N₀ ⇒ C).
  - Rappels mobilisés des chapitres 1–2 : I₀ = E/R en régime permanent, bobine idéale tension nulle en
    régime permanent, loi de Lenz, dipôle RC (τ, 63 %, u = E(1 − e^(−t/τ))) dans les ex. 8 et 11.
- ⛔ EXCLU (absent du chapitre) :
  - **Résolution** de l'équation différentielle amortie (aucune expression de q(t) en régime amorti,
    pas d'exponentielle × sinus, pas de décrément logarithmique, pas de facteur de qualité Q — Q relève du
    chapitre 4) ; **résistance critique** chiffrée (régime critique seulement nommé, « difficile de le mettre
    en évidence ») ; aucune condition R² vs 4L/C.
  - **Oscillations forcées / résonance**, impédance, générateur sinusoïdal (chapitre 4) ; **entretien des
    oscillations** (résistance négative, amplificateur) : absent.
  - Démonstration de la solution générale (elle est **admise**) ; écriture en sinus = forme du cours ; le cosinus
    apparaît dans la démonstration p.92 et la question p.94 ; pas de représentation de Fresnel.
  - Analogie mécanique (pendule élastique : chapitre 5) : absente ici.
  - Appareillage : oscilloscope analogique seulement dans la Fiche technique (hors cours) ; impédance
    d'entrée de l'oscilloscope = fiche technique uniquement.

### Lecture

- **Couche texte** (pdftotext) : p.78 à 109 (les 32 pages) + p.316–318.
- **Pages lues sur l'image** (110 dpi) : **33** — 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
  93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 316 ; zooms à 200 dpi : p.316
  (colonne Chapitre 3), p.105 (Fig.2 et Fig.3 de l'ex. 11), p.102 (bas de l'ex. 7). p.317–318 : texte
  seulement (chapitres 5–11 et sites web, rien pour le chapitre 3).
- **Sondage image** : totalité des pages ; plus denses : 85, 86, 88, 92, 94, 97, 98, 104, 108, 316.
  **Écarts texte / image constatés** : symboles grecs ω, φ, π, √ supprimés (« o = 1/LC », « To = 2 LC »,
  « No = 1/2 LC » p.88–90, 95, 100 QCM III) ; équations RLC éclatées sur plusieurs lignes (p.85, 86, 108) ;
  E_L = ½(L/R₀²)u_R₀² illisible (p.86) ; signe « − » de (1 − cos 2ω₀t) perdu (p.94) ; « ≃ » rendu « b »
  (p.98, 108–109) ; φ = π (p.98) et sinφ (p.91) perdus ; 1/τ de l'ex. 10 (p.104) perdu ; θ_p rendu « p »
  (p.107) ; Fig.13/14 (valeurs des champs du logiciel) et toutes les échelles d'oscillogrammes seulement sur
  l'image ; le corrigé p.316 est en colonne droite mêlé au chapitre 2 dans le texte. Aucun encadré n'est
  fiable en couche texte seule ; tous ont été recopiés depuis l'image.

### Doutes signalés
- [?] **Contradiction du manuel** : l'analyse p.84 dit que la décharge apériodique « demande une durée aussi
  longue que la résistance R₀ est plus grande », la Conclusion p.85 dit « plus le retour de l'oscillateur à son
  état d'équilibre est rapide » ; ne pas enseigner la phrase de la conclusion telle quelle.
- [?] **Ex. 11, corrigé p.316** : « A t=0, u_C = E, donc (2) correspond à u_C » contredit la Fig.2 (courbe (1)
  part de 0 et croît : c'est u_C pour une charge) ; τ = 0,7 s incompatible avec RC = 30 kΩ × 50 μF = 1,5 s
  et avec la lecture de la Fig.2 (63 % de 6 V ≈ 3,8 V vers t ≈ 1,4 s) ; i ≃ 158 μA en découle. Corrigé à ne pas
  reprendre sans re-résolution.
- [?] **Fig.11a/11b** (p.86) : axe « En(μJ) » de 0 à 0,6 alors que ½·0,5 μF·(5 V)² = 6,25 μJ — échelle (ou
  unité) douteuse ; ne pas tirer de valeur numérique des Fig.11.
- [?] p.86 question 4°) : « préciser l'influence sur la vitesse de diminution… » — complément (de R₀) absent.
- [?] p.87 coquille « Entre t₂ = nT + T/4 et t₂ = nT + T/2 » (deux t₂).
- [?] p.88 « φ(t) = ωt + φ » (indice o absent).
- [?] p.107 Fig.1 : abscisses légendées « T₀/2 » et « T₀ » pour le créneau de période T_e (coquille probable).
- [?] Ex. 9 corrigé « 2°b) Voir cours page 2° » (renvoi tronqué) ; ex. 9 3°) oscillogramme sans sensibilité
  verticale ⇒ W_J = 32,2 μJ non vérifiable sur la figure.
- [?] Ex. 12 3°) : « Sachant que la valeur de C est à 40% HR » — phrase incomplète, aucune loi C(%HR) donnée ;
  l'exercice n'est pas résoluble tel qu'imprimé (C calculée ≈ 125 pF à partir de N₀ et L, mais pas de
  correspondance vers %HR).
- [?] Ex. 4 : la résistance de la bobine est notée R (et non r) ; ex. 8 : 0,2 mV/div pour u₂ (sensibilité
  inhabituelle, recopiée telle quelle).
- [?] Bornes au programme officiel non vérifiées ici (R-3) : place du « régime critique » (seulement nommé) et
  de la Fiche technique (hors cours).

## 2.4 Chapitre 4 — Oscillations électriques forcées en régime sinusoïdal (manuel 223433, p.110–143)

**Rubrique** (bandeau de chaque page) : « Evolution de systèmes ◆ Oscillations électriques forcées en régime sinusoïdal ».

**Page d'ouverture (p.111)** — « 4 — OSCILLATIONS ÉLECTRIQUES FORCÉES EN RÉGIME SINUSOÏDAL ». Photo : guitare électrique ;
légende : « La guitare électrique est munie d'une caisse creuse à laquelle sont adjoints des microphones électromagnétiques.
Grâce à la résonance électrique, le son amplifié prime sur la résonance naturelle de la caisse. » Questions d'accroche :
« ◆ En quoi consiste la recherche manuelle ou automatique d'une chaîne radio ou d'un canal de télévision ? ◆ Que veut-on
dire par “résonance électrique” dont les applications sont trés nombreuses ? »
(La couche texte rend la légende en mots tronqués, texte incliné : lue sur l'image.)

**Objectifs (p.110)** (verbatim) :
- Distinguer, en régime forcé, le résonateur de l'excitateur.
- Visualiser simultanément à l'oscilloscope la tension excitatrice u(t) et l'intensité du courant i(t).
- Mesurer l'amplitude et la fréquence d'une grandeur oscillante en régime forcé sinusoïdal.
- Déterminer le déphasage entre la tension excitatrice u(t) et l'intensité du courant i(t).
- Mettre en évidence expérimentalement le phénomène de résonance d'intensité et celui de la résonance de charge.
- Etablir en i(t) ou en q(t), l'équation différentielle des oscillations forcées en régime sinusoïdal.
- Établir l'expression de l'intensité maximale Iₘ du courant oscillant en fonction de la fréquence des excitations et en
  déduire celle de la charge maximale Qₘ.
- Interpréter théoriquement le phénomène de résonance.
- Calculer la puissance moyenne absorbée par un oscillateur électrique.
- Expliquer l'importance du facteur de puissance dans les transformations de l'énergie électrique.

**Prérequis (p.110)** —
SAVOIR : Définir un oscillateur. · Caractériser une grandeur oscillante sinusoïdale par sa période, son amplitude et sa
phase initiale. · Écrire les relations : T = 2π/ω et N = 1/T. · Définir les valeurs maximale Iₘ et efficace I de l'intensité
du courant alternatif. · Définir les valeurs maximale Uₘ et efficace U d'une tension alternative. · Ecrire les relations :
Iₘ = I√2 et Uₘ = U√2. · Ecrire les relations : E_c = q²/2C et E_L = ½ L.i².
SAVOIR FAIRE : Reconnaître un oscillateur. · Visualiser à l'oscilloscope : une tension électrique, une intensité de courant.
· Déterminer graphiquement la période et l'amplitude d'une grandeur électrique oscillante. · Calculer la période propre
d'un oscillateur RLC série. · Établir l'équation différentielle régissant les oscillations libres d'un circuit RLC série par
application de la loi des mailles. · Calculer l'énergie totale d'un oscillateur RLC série.
(Image : « T = 2π/ω » ; la couche texte rend « T = 2 1 … T » et perd √2 → « Im = I 2 ». « E_c » est imprimé ainsi pour
l'énergie du condensateur.)

**Plan du chapitre** (pas de sommaire imprimé ; titres lus dans le corps) :
introduction (p.112) · **1** Réponse d'un circuit RLC série à une tension sinusoïdale (1.1 Production d'oscillations
forcées ; 1.2 Déphasage : 1.2.1 Étude générale, 1.2.2 Déphasage entre i(t) et q(t) en régime sinusoïdal forcé) ·
**2** Influence de la fréquence d'excitation sur la réponse d'un circuit RLC série (p.116–122 : interprétation théorique —
Iₘ et φᵢ par Fresnel ; Qₘ et φ_q ; résonance d'intensité ; résonance de charge) · **3** Influence de la résistance totale du
circuit sur la résonance (p.122–124) · **4** Le phénomène de surtension (p.125–126) · **5** Applications de la résonance
(p.127) · **6** Puissance moyenne et facteur de puissance (6.1 Puissance électrique instantanée ; 6.2 Puissance électrique
moyenne ; 6.3 Résonance de puissance ; 6.4 Transfert de puissance moyenne ; 6.5 Importance du facteur de puissance cosφ)
(p.127–130) · L'essentiel (p.131) · Exercices : exercice résolu (p.132–134) ; Exercices à résoudre — Tests rapides des
acquis (1 V/F, 2 QCM, p.135), Exercices d'application (3–12, p.136–138), Exercices de synthèse (13–17, p.138–141),
18 Étude de texte (p.141) · Fiche technique « Construction de Fresnel » (p.142) · En savoir plus (p.143).
(Titre de la p.112 imprimé « OSCILLATIONS ÉLECTIRQUES FORCÉES » — coquille du manuel.)

### Cours — Manipulations, questions, conclusions

**Introduction (p.112)** — « On a vu dans le chapitre précédent que si un circuit RLC série peut effectuer des oscillations
libres, celles-ci cessent plus au moins rapidement à cause de l'amortissement dû à sa résistance. Quel sera l'effet de
l'application d'une tension sinusoïdale aux bornes d'un tel oscillateur, une simple compensation de l'amortissement ou plus ? »

**1.1 Production d'oscillations forcées — Manipulation (p.112–113)**
- Dispositif : GBF délivrant u(t) = Uₘ.sinωt, fréquence N réglable, Uₘ maintenue constante ; circuit RLC série : résistor
  Ro réglable, condensateur C = 0,47 μF, bobine L = 0,2 H, r = 12,5 Ω (Fig.1 : GBF entre A et M, interrupteur K, C, (L, r),
  Ro entre B et M ; M à la masse, A → voie Y1, B → voie Y2 ; résistor côté masse du GBF).
- Réglages : N = 400 Hz, Uₘ = 2 V, Ro = 50 Ω « par exemple ». K ouvert : seul l'oscillogramme (1) ; K fermé : oscillogrammes
  stables (1) [u] et (2) [u_Ro], sensibilités 1 ms/div et 1 V/div (Fig.2 : (1) grande amplitude ≈ 2 div ; (2) petite
  amplitude, décalée de (1)).
- À 400 Hz, série de mesures de U_Rom en fonction de Uₘ → Fig.3 : droite passant par l'origine, U_Rom (V) en ordonnée
  (0 à 0,8), Uₘ (V) en abscisse (0 à 4), point final lu ≈ (4 V ; 0,6 V). (Légende imprimée « Tracé de Uₘ en fonction de
  f (U_Rom) » alors que l'axe vertical porte U_Rom [?].)
- Second montage (Fig.4) : condensateur côté masse ; M à la masse, A → Y1, D → Y2 ; 400 Hz, Uₘ = 2 V, Ro = 50 Ω ;
  sensibilités 1 ms/div et 2 V/div ; on observe (1) et l'oscillogramme stable (3) = u_C (Fig.5).
- **Questions** : 1°) Montrer qu'il y a deux moyens pour transformer le montage de la figure 1 en le montage de la figure 4.
  2°) Justifier le fait de prendre u_R0(t) et u_C(t) comme étant des tensions représentant respectivement i(t) et q(t).
  3°) Comparer la forme des oscillogrammes représentant i(t) et q(t) à la forme de celui de u(t). 4°) Mesurer les fréquences
  N₁ de i(t) et N₂ de q(t) et les comparer à la fréquence N de u(t) ainsi qu'à la fréquence propre No de l'oscillateur.
  5°) a) A l'aide de la courbe de la figure 3, montrer que : Uₘ = kU_Rom, où k est une constante que l'on calculera.
  b) Montrer que la tension maximale Uₘ peut s'écrire en fonction de l'intensité maximale Iₘ sous la forme : Uₘ = Z Iₘ où Z
  est une constante dont on déterminera la dimension. 6°) A l'aide des oscillogrammes (2) de la figure 2 et (3) de la
  figure 5, calculer respectivement Iₘ et la charge maximale Qₘ. (Aucune valeur numérique de réponse donnée.)
- **Commentaire** (p.113–114) : i(t) et q(t) varient sinusoïdalement, avec un décalage horaire constant par rapport à u(t),
  donc « avec la même fréquence N que la tension u(t) imposée par le GBF et non avec la fréquence propre du circuit RLC
  série : les oscillations de i(t) et de q(t) ne sont plus libres, elles sont imposées par le GBF, d'où leur qualification
  d'oscillations forcées. Ainsi, le GBF a joué le rôle d'excitateur. » La linéarité de U_Rom(Uₘ) montre que « le quotient
  Uₘ/Iₘ est une constante qui ne dépend que des caractéristiques de l'oscillateur. On l'appelle impédance du circuit et on
  la note Z. Ayant la dimension d'une résistance électrique, l'impédance s'exprime en ohm (Ω). »

**1.2.1 Déphasage — Étude générale (p.115–116)** — exemples Fig.6a (u₁, u₂ en concordance de phase), Fig.6b (opposition de
phase), Fig.7a (u₂ en quadrature retard sur u₁), Fig.7b (u₂ en quadrature avance sur u₁) — chronogrammes (1) rouge, (2) vert.
- **Questions** : 1°) Justifier qualitativement l'appellation concordance de phase et opposition de phase. 2°) a) Montrer que
  la concordance de phase signifie Δφ = 2kπ rad, avec k entier relatif. b) Montrer que l'opposition de phase signifie
  Δφ = (π + 2kπ) rad, avec k entier relatif. 3°) Dans les cas de la figure 7 où le décalage horaire Δt entre u₁ et u₂ est
  égale à T/4, on dit que u₂ et u₁ évoluent au cours du temps en quadrature de phase. Plus précisement, u₂ est en quadrature
  retard sur u₁ dans le cas de la figure 7a, tandis qu'elle est en quadrature avance sur u₁ dans le cas de la figure 7b.
  Expliquer cette différence par le calcul de Δφ dans les deux cas. 4°) Déduire des exemples traités précedemment que la
  valeur absolue du déphasage |Δφ| entre deux fonctions sinusoïdales isochrones est liée à leur décalage horaire Δt par la
  relation : |Δφ| = (2π/T)Δt.

**1.2.2 Déphasage entre i(t) et q(t) (p.116)** — démonstration (voir Encadrés) puis **Question** : « Vérifier que
(φᵢ − φ_q = π/2 rad) en montrant, à l'aide des oscillogrammes des figures 2 et 5 que les maxima de i(t) sont atteints à T/4
avant ceux de q(t), T étant la période des oscillations. »

**2 Influence de la fréquence d'excitation — Manipulation (p.116–117)**
- Montage de la figure 1, u(t) = Uₘsin2πNt, Uₘ = 2 V. En faisant varier N : u_Ro(t) reste sinusoïdale, U_Rom et le décalage
  horaire Δt < T/2 par rapport à u(t) changent ; « lorsque Δt s'annule, U_Rom est à sa valeur la plus élevée ».
- « On reprend le montage de la figure 3 » [sic — le montage u_C est celui de la figure 4, la fig. 3 est un graphe [?]] :
  mêmes faits pour u_C(t), « à la seule différence que la tension u_c(t) s'annule toujours à Δt < T/2, après la tension
  excitatrice u(t) ».
- Mesures de I (ampèremètre) et de U_C (voltmètre aux bornes du condensateur) pour différentes N (Fig.8 : GBF, ampèremètre A,
  K, C avec voltmètre V en parallèle, (L, r), Ro). Fig.9 : courbes (1) Iₘ (mA, axe gauche 0–40) et (2) Qₘ (μC, axe droit)
  en fonction de N (0–800 Hz) ; pics vers 500 Hz, celui de Qₘ légèrement à gauche de celui de Iₘ ; pic de Iₘ ≈ 30 mA.
  (Le texte dit « au cours du temps » pour des courbes en fonction de N ; graduations de l'axe Qₘ imprimées « 30, 20, 10,
  10 » [?].)
- **Questions** : 1°) D'après les constatations faites sur le décalage horaire Δt entre U_Ro(t) et u(t), puis entre u_c(t) et
  u(t), montrer que, selon la valeur de la fréquence N de u(t), l'intensité i(t) peut être en avance de phase ou bien en
  retard de phase par rapport à u(t), tandis que q(t) évolue toujours en retard de phase par rapport à u(t). 2°) Décrire la
  forme particulière de chacune des courbes Iₘ et Qₘ en foncion de N. 3°) a) Déterminer graphiquement les valeurs N₁ et N₂
  de la fréquence N correspondant respectivement aux valeurs maximales des amplitudes Iₘ et Qₘ ; les comparer à la fréquence
  propre No de l'oscillateur. b) Pour N = N₁, calculer l'indépendance [sic : impédance] Z du circuit et la comparer à sa
  résistance totale R = Ro + r.
- **Conclusion** (p.117–118) : verbatim dans « Encadrés ».

**3 Influence de la résistance totale — Manipulation (p.122)** — même étude, L = 0,2 H, C = 0,47 μF, Ro₁ = 50 Ω,
Ro₂ = 200 Ω, Ro₃ = 1000 Ω. Fig.11a : courbes de résonance d'intensité (1), (2), (3) (Iₘ en mA, 0–30 ; pic (1) ≈ 30 mA vers
500 Hz, (2) ≈ 8 mA, (3) quasi plate). Fig.11b : Qₘ (μC, 0–30) : (1) pic très pointu ≈ 30 μC, (2) peu marqué, (3) décroissante.
- **Questions** : 1°) Comparer les allures des courbes de résonance (1), (2) et (3) de la figure 11a entre elles ; en déduire
  l'influence de la résistance du circuit sur la résonance d'intensité. 2°) Comparer les allures des courbes (1), (2) et (3)
  de la figure 11b, entre elles ; en déduire l'influence de la résistance totale du circuit sur la résonance de charge.
  3°) Dans les deux cas de figure (11a et 11b) déterminer les valeurs de toutes les fréquences de résonances et conclure.
- **Interprétation** (p.123–124) : résonance aiguë / floue / très floue (intensité, fréquence inchangée = No) ; pour la
  charge : R petite → Nr très légèrement < No, Qmo très élevée, « résonance aiguë » ; R grande → Nr < No, Qmo très peu élevée,
  « résonance floue » ; R très grande → (R² − 2L/C) > 0, « Qₘ ne peut que décroitre lorsque la fréquence N des excitations
  augmente (coube (3) de la figure 11b) : résonance impossible. » Puis : « Une telle réponse du circuit RLC série,
  caractérisée par une évolution pratiquement linéaire de la charge maximale Qₘ en fonction de la fréquence N des excitations
  est appelée réponse linéaire ; on dit aussi qu'un tel régime forcé est linéaire. »

**4 Le phénomène de surtension — Manipulation (p.125)** — montage fig.1, L = 0,2 H, C = 0,47 μF, Uₘ = 2 V, N = No = 520 Hz.
Tableau : Ro (Ω) 20 / 50 / 200 → U_Cm (V) 40 / 21 / 6,5.
- **Questions** : 1°) Reproduire, puis compléter le tableau (ligne Q = U_Cm/Uₘ pour Ro = 20, 50, 200 Ω). 2°) Le quotient
  Q = U_Cm/Uₘ est appelé facteur de surtension à la résonance. Justifier cette appellation. 3°) a) Montrer théoriquement que
  Q peut s'écrire uniquement en fonction des caractéristiques R, L et C de l'oscillateur. b) Calculer les valeurs théoriques
  de Q, correspondant respectivement aux valeurs 20 Ω, 50 Ω et 200 Ω de la résistance Ro. 4°) Quelle précaution faut-il
  prendre pour avoir un facteur de surtension modéré à la résonance ? (Pas de réponses chiffrées imprimées.)
- Remarque (p.126) : « A la résonance d'intensité : U = (Ro + r) I et U_Bobine = √(r² + (Lω₀)²) I. Si la valeur de
  l'inductance L est telle que, Lω₀ >> (Ro + r), la valeur de la tension efficace aux bornes de la bobine sera plus grande
  que la valeur de la tension efficace d'alimentation. Donc, il y a aussi risque de surtenion aux bormes de la bobine
  (Fig.12). » (Fig.12 : diagramme de Fresnel — U horizontal, RoI, rI, LωoI, U_Bobine, I/(Cωo) = U_C.)

**5 Applications de la résonance (p.127)** — « les oscillateurs à quartz, le haut parleur et le microphone électrodynamique,
la réception d'émissions radiophoniques. » Poste radio : résonance aiguë recherchée (accorder la fréquence propre du RLC du
récepteur avec la fréquence de la station) ; chaîne « haute fidélité » : courbes de résonance floue (« les plus aplaties
possibles ») dans le domaine des sons audibles, pour restituer les timbres.

**6 Puissance (p.127–130)** — pas de manipulation ; développement théorique (voir Encadrés). Fig.13 : dipôle D entre A et B,
u = u_AB, courant i. Fig.14 : P (mW, 08 à 64) en fonction de N (0–700 Hz), pic ≈ 60 mW vers 520 Hz. Fig.15 : courbes de
résonance aiguë (verte) et floue (orange) de P(N).

### Encadrés, définitions, lois et relations (VERBATIM, vérifiés sur l'image de leur page)

> **Équations différentielles (p.114)** — « Pour le circuit de la figure 1, la loi des mailles s'écrit :
> u_BM + u_DB + u_AD + (− u_AM) = 0, d'où : u_AM = u_BM + u_DB + u_AD. Donc, u_AM = Roi + ri + L di/dt + q/C. En tenant compte
> de la relation i(t) = dq(t)/dt, on a : L di/dt + (Ro + r) i + (1/C)∫i.dt = u_AM, équation différencielle des oscillations
> de i(t). La même équation peut s'écrire : L d²q/dt² + (Ro + r) dq/dt + q/C = u_AM. Sous cette forme, c'est l'équation
> différentielle des oscillations de q(t). Ces équations différentielles à second membre non nul admettent respectivement
> comme solutions particulières celles du régime permanent : i(t) = Iₘsin(2πNt + φᵢ) et q(t) = Qₘsin(2πNt + φ_q), où :
> ◆ φᵢ et φ_q sont respectivement les phases initiales de i(t) et de q(t), ◆ Iₘ = Uₘ/Z. Sachant que i(t) = dq/dt, on a :
> i(t) = 2πNQₘcos(2πNt + φ_q). D'où : Iₘ = 2πNQₘ, ce qui équivaut à : Qₘ = Iₘ/2πN = Uₘ/2πNZ. »
> Remarque : « Par recours à la relation Qₘ = Iₘ/2πN, on peut retrouver l'une des valeurs maximales Iₘ et Qₘ, calculées
> précédemment (réponse à la question 6) à partir de l'autre. »

> **Conclusion 1.1 (p.115)** — « La réponse d'un circuit RLC série à une tension sinusoïdale est un courant alternatif
> sinusoïdal engendré par des oscillations sinusoïdales de la charge q du condensateur, à la même fréquence N que la tension
> excitatrice. Pour une fréquence donnée N de la tention excitatrice : – l'intensité maximale Iₘ est proportionnelle à la
> valeur maximale Uₘ de la tention excitatrice. Iₘ = Uₘ/Z, où Z est une grandeur physique ayant le dimentsion d'une
> résistance, appelée impédance du circuit RLC série. – la charge maximale Qₘ du condensateur est liée à Iₘ par la relation :
> Qₘ = Iₘ/2πN »

> **Définition (déphasage, p.115)** — « On appelle déphasage entre deux fonctions sinusoïdales de phases initiales φ₁ et φ₂ et
> de même période, la différence de phase Δφ = (φ₂ − φ₁) ou (φ₁ − φ₂). »

> **Conclusion 1.2.1 (p.116)** — « A tout décalage horaire Δt entre deux fonctions sinusoïdales y₁(t) et y₂(t) isochrones (de
> même péride T), représentées dans le même système d'axes, est associé un déphasage Δφ tel que : |Δφ| = (2π/T)Δt.
> – Si Δt = 0, Δφ = 0 : les deux fonctions sont en concordance de phase. – Si Δt = T/2, Δφ = ± π rad : les deux fonctions
> sont en opposition de phase. – Si Δt = T/4, Δφ = ± π/2 rad : les deux fonctions sont en quadrature de phase. Si le déphasage
> (φ₂ − φ₁) est positif, y₂(t) est en avance de phase par rapport à y₁(t) et inversement. »

> **1.2.2 (p.116)** — « q(t) = Qₘsin(2πNt + φ_q). Or i(t) = dq/dt. Donc, i(t) = 2πNQₘcos(2πNt + φ_q), ce qui revient à
> écrire : i(t) = 2πNQₘcos(2πNt + φ_q + π/2) [sic : sin attendu [?]]. Ainsi on montre que : φᵢ = φ_q + π/2 rad. »
> **Conclusion** : « Dans un circuit RLC série, en régime sinusoïdale forcé, l'intensité i(t) du courant électrique oscille en
> quadrature avance de phase par rapport à la charge q(t). »

> **Conclusion §2, expérimentale (p.117–118)** — « En plus de leur évoluton sinusoïdale, au cours du temps, à la fréquence N
> de la tension excitatrice u(t), la charge q(t) du condensateur d'un circuit RLC série et l'intensité i(t) du courant qui y
> circule sont caractérisées chacune par une valeur maximale (respectivement Qₘ et Iₘ) et une phase initiale (respectivement
> φ_q et φᵢ) qui dépendant de la fréquence N. La réponse d'un circuit RLC série à une tension sinusoïdale de fréquence N égale
> à la fréquence propre No du circuit est un courant oscillant en phase avec la tension excitatrice et avec la valeur la plus
> élevée de l'intensité maximale : **c'est la résonance d'intensité.** A la résonance d'intensité, le circuit RLC série se
> comporte comme un résistor de résistance R. Comme il peut se produire, dans un circuit RLC série, une résonance d'intesité,
> il peut s'y produire une résonance de charge, mais à une fréquence légèrment inférieure à la fréquence propre No du circuit. »

> **Fresnel appliqué au RLC (p.118)** — « On a : Ri + L di/dt + (1/C)∫i.dt = Uₘ sinωt, avec R = Ro + r ; i(t) = Iₘ sin(ωt + φᵢ).
> di/dt = ωIₘsin(ωt + φᵢ + π/2) ; ∫idt = (Iₘ/ω) sin(ωt + φᵢ − π/2) + cte. Il vient alors : RIₘsin(ωt + φᵢ) +
> LωIₘsin(ωt + φᵢ + π/2) + (Iₘ/Cω) sin(ωt + φᵢ − π/2) + cte/C = Uₘ sin(ωt). Étant une fonction sinusoïdale, Uₘ sinωt ne peut
> être qu'une somme de fonctions sinusoïdales. Donc, cte = 0. ◆ RIₘ sin(ωt + φᵢ) → OA⃗₁ [RIₘ, φᵢ] ◆ LωIₘ sin(ωt + φᵢ + π/2)
> → OA⃗₂ [LωIₘ, φᵢ + π/2] ◆ (Iₘ/Cω) sin(ωt + φᵢ − π/2) → OA⃗₃ [Iₘ/Cω, φᵢ − π/2] ◆ Uₘsinωt → OA⃗ [Uₘ, 0] tel que
> OA⃗₁ + OA⃗₂ + OA⃗₃ [sic, « OA⃗ = » omis]. Les vecteurs de Fresnel OA⃗₂ + OA⃗₃ étant de sens contraires, il en résulte trois
> constructions possibles : ◆ ‖OA⃗₂‖ > ‖OA⃗₃‖, cas correspondant à Lω > 1/Cω c'est-à-dire N > No : il donne la construction
> de la figure 10a. ◆ ‖OA⃗₂‖ < ‖OA⃗₃‖, cas correspondant à Lω < 1/Cω c'est-à-dire N < No : … figure 10b. ◆ ‖OA⃗₂‖ = ‖OA⃗₃‖,
> cas correspondant à Lω = 1/Cω c'est-à-dire N = No : … figure 10c. » (Renvoi imprimé « fiche technique de fin de chapitre
> (p.141) » : la fiche est en p.142 [?].)

> **Iₘ, Z, φᵢ (p.119, encadrés)** — « Le triangle OAB étant rectangle en B (Fig.10a et 10b), on a dans le cas général :
> Uₘ² = (RIₘ)² + (LωIₘ − Iₘ/Cω)², d'où Uₘ = √(R² + (Lω − 1/Cω)²) Iₘ. Donc, **Iₘ = Uₘ / √(R² + (Lω − 1/Cω)²)**, soit :
> Iₘ = Uₘ/Z avec **Z = √(R² + (Lω − 1/Cω)²)**. D'après le cas de la figure 10a, Lω > 1/Cω, on a φᵢ < 0, ça signifie que
> l'intensité i(t) du courant est en retard de phase par rapport à la tension excitatrice u(t) : le circuit RLC série est dit
> **inductif**. D'après le cas de la figure 10b, Lω < 1/Cω, on a φᵢ > 0, ça signifie que l'intensité i(t) du courant est en
> avance de phase par rapport à la tension excitatrice u(t) : le circuit RLC série est dit **capacitif**. D'après les
> constructions précédentes, on a : **|tgφᵢ| = |Lω − 1/Cω| / R**. En tenant compte de la dépendance du signe de φ de celui de
> (Lω − 1/Cω), la phase initiale φᵢ de i est telle que : **tgφᵢ = (1/Cω − Lω)/R, avec −π/2 rad < φᵢ < π/2 rad**. »
> Remarque : « Le déphasage φᵢ entre i et u peut être aussi caractérisé par : **cos φᵢ = R/Z** »
> (Fig.10a/b/c : vecteurs Uₘ horizontal (φ = 0), R.Iₘ, LωIₘ, Iₘ/Cω, angle φ ; 10c : R.Iₘ confondu avec Uₘ, « u ; i ».)

> **Qₘ et φ_q (p.120)** — « q(t) = Qₘsin(ωt + φ_q) et q(t) = ∫ i dt. D'où : **Qₘ = Iₘ/ω = Uₘ / √(R²ω² + (1/C − Lω²)²)** ;
> φ_q = φᵢ − π/2 rad. Or, −π/2 rad < φᵢ < π/2 rad, ce qui donne −π/2 rad < φ_q + π/2 < π/2 rad. D'où : **−π rad < φ_q < 0**,
> ce qui signifie que la charge q évolue toujours en retard de phase par rapport à u(t). »

> **Résonance d'intensité (p.120)** — « L'impédance du circuit s'écrit Z = √(R² + (Lω − 1/Cω)²). ◆ Aux très basses pulsations
> ainsi qu'aux pulsations beaucoup plus élèvées que la pulsation propre ωo de l'oscillateur, l'écart entre Lω et 1/Cω augmente.
> Par suite, l'impédance Z devient de plus en plus grande. Donc, dans l'un ou l'autre cas, Iₘ(ω) = Uₘ/Z → 0, ce qui signifie
> que la réponse du circuit RLC série devient de plus en plus faible. Cette réponse s'améliore lorsque Z prend une valeur
> modérée, ce qui n'est possible qu'avec des valeurs comparables de Lω et de 1/Cω. ◆ Dans le cas particulier où Lω = 1/Cω
> obtenu avec ω = ωo = 1/√LC, c'est-à-dire avec N = No = 1/(2π√LC) : – l'impédance Z est minimale : Z = R. Par conséquent,
> l'intensité maximale prend sa valeur la plus élevée **Im0 = Uₘ/R : c'est la résonance d'intensité**. – La phase initiale φᵢ
> de i(t) par rapport à u(t) est telle que tgφᵢ = (1/Cω − Lω)/R = 0, ce qui signifie qu'à la résonance, la tension u(t) et
> l'intensité i(t) sont en phase. »
> Remarque (p.121) : « L'appellation d'un oscillateur en régime forcé comme étant un résonateur revient au phénomène de
> résonance. »

> **Résonance de charge (p.121–122)** — « Qₘ = Iₘ/ω. Or, Iₘ = Uₘ/Z, d'où : Qₘ = Uₘ/√(R²ω² + (1/C − Lω²)²) = Uₘ/√g(ω), avec
> g(ω) = R²ω² + (1/C − Lω²)². Donc, l'étude de Qₘ en fonction de ω revient à celle de g(ω). Il suffit alors de déterminer le
> signe de dg/dω. dg/dω = 2R²ω − 4Lω(1/C − Lω²) = 2ω(R² − 2L/C + 2L²ω²). Comme on a ω ≠ 0, dg/dω s'annule seulement pour
> ω = ω₁ telle que : **ω₁² = 1/LC − R²/2L²**, et ce, en supposant qu'avec la valeur de Ro choisie, on a : **(R² − 2L/C) < 0**.
> Dans ces conditions, pour ω < ω₁, on a dg/dω < 0 et pour ω > ω₁, on a : dg/dω > 0, ce qui signifie que g(ω) est minimale
> lorsque ω = ω₁. Or, Qₘ = Uₘ/√g(ω). Donc, Qₘ est maximale […] ce qui explique la résonance de charge. Par suite, la pulsation
> ω₁ à laquelle on a une résonance de charge est appelée pulsation de résonance et on la note ωr. Or, ω = 2πN et
> 1/LC = (2πN₀)². Donc, la fréquence de résonance s'écrit : **Nr = √(N₀² − R²/8π²L²)**. Ainsi, on montre bien que la
> résonance de charge est obtenue à une fréquence Nr < No. »

> **Conclusion §2, théorique (p.122)** — « Un circuit RLC série soumis une tension sinusoïdale de fréquence N entre en résonance
> de charge à la fréquence N = √(No² − R²/8π²L²) et en résonance d'intensité à la fréquence N = No.
> • Résonance de charge ⇔ { Qₘ est la plus élevée ; q reste en retard de phase par rapport à u(t)
> • Résonance d'intensité ⇔ { Iₘ est la plus élevée ; i(t) est en phase avec u(t) »

> **Influence de l'amortissement (p.123)** — « A la résonance d'intensité, on a Imo = Uₘ/R. […] Imo est d'autant plus grande
> que R est plus petite. […] Cependant, la fréquence de résonance est inchangée : elle reste toujours égale à la fréquence
> propre de l'oscillateur (circuit RLC série). » — « A la résonance de charge, on a : Qmo = Uₘ / √(R²(2πNr)²[1/C − L(2πNr)²]²)
> [sic, « + » manquant entre les deux termes [?]], avec Nr = √(No² − R²/8π²L²) (1) ce qui donne **Qmo = Uₘ / (R√(1/LC − R²/4L²))** »

> **Conclusion §3 (p.124)** — « Pour un circuit RLC serie, la résonance de charge ou d'intensité est d'autant plus aiguë que
> l'amortissement est faible. Contrairement à la fréquence de la résonance d'intensité qui ne dépend pas de l'amortissement, la
> fréquence de la résonance de charge est d'autant plus proche de la fréquence propre No de l'oscillateur que l'amortissement
> est faible. »

> **Expression de Q (p.126)** — « Pour une pulsation ω égale à la pulsation propre ωo, U_C = Io/Cωo et Io = U/(Ro + r).
> D'où : Q = 1/((r + Ro) Cωo). (1) Or, 1/Cωo = Lωo. Donc, Q s'exprime autrement comme suit : **Q = Lωo/(Ro + r) (2)**. En
> remplaçant ωo par 1/√LC dans (1) par exemple, il vient : Q = (1/((Ro + r) C)) √LC. Donc : **Q = (1/(Ro + r)) √(L/C)**.
> Donc, le facteur de surtension Q augmente quand l'inductance L augmente et lorsque la capacité C et la résistance R du
> circuit diminuent. S'il est trop élevé, la surtension devient dangereuse tant pour l'utilisateur que pour les composants du
> circuit ou les appareils d'une manière générale : elle peut provoquer le claquage du condensateur et des étincelles entre
> les spires de la bobine, d'où le risque d'électrocution. »
> **Conclusion** : « – A la résonance d'intensité d'un circuit RLC série, il peut surgir aux bornes du condensateur, une
> surtension caractérisée par le facteur : Q = (1/(Ro + r))√(L/C) – Le facteur de surtension Q est d'autant plus grand que la
> résonance est plus aiguë. – Une surtension élevée peut entraîner des conséquences néfastes. »

> **6.1 Puissance instantanée (p.127–128)** — « En appliquant à ses bornes A et B une tension sinusoïdale de basse fréquence
> u(t) = U√2 sinωt, un dipôle D (Fig.13) sera parcouru par un courant d'intensité sinusoïdale i(t) = I√2 sin(ωt + φ) et
> recevra, à tout instant, une puissance électrique : p(t) = u(t).i(t). […] p(t) = ui = U√2sin(ωt).I√2sin(ωt + φ) =
> 2UI sinωt.sin(ωt + φ). En appliquant […] la relation trigonométrique Sina.sinb = ½[cos(a − b) − cos(a + b)], on aboutit à :
> **p(t) = UIcosφ − UIcos(2ωt + φ).** » — « […] avec une fréquence double de celle de u(t) et de i(t), ce qui rend p(t)
> périodique de période Tp = ½ T. […] p(t) peut être positive et le dipôle RLC série est effectivement un récepteur. Puis,
> elle peut devenir négative et le même dipôle se comporte alors comme un générateur. Cependant, pour déterminer le bilan,
> ces constatations restent insuffisantes. »

> **Définition (puissance moyenne, p.128)** — « La puissance moyenne d'un dipôle D est la valeur moyenne prise par sa puissance
> instantanée p(t) sur une très grande durée Δt (tendant vers l'infini). Lorsque p(t) est périodique(⊙), il est équivalent de
> prendre Δt égale à une période. On note la puissance électrique moyenne P et on l'appelle aussi en régime forcé sinusoïdal,
> puissance électrique active ou réelle. Comme toute puissance, la puissance moyenne s'exprime en watt (W) et se mesure avec un
> wattmètre. » Note marginale ⊙ : « Le cas unique qui figure dans le programme est celui du régime sinusoïdal forcé. »

> **Expression de P (p.128–129)** — « **P = (1/Tp) ∫_{kTp}^{(k+1)Tp} p(t)dt** où k est un entier naturel. […] Donc,
> P = (1/Tp)∫UIcosφdt − (1/Tp)∫UIcos(2ωt + φ)dt. Ce qui donne : P = (UIcosφ/Tp)[t] − (UI/2ωTp)[sin(2ωt + φ)]. La fonction
> sin(2ωt+φ) étant périodique de période Tp = π/ω, on a : [sin(2ωt + φ)]_{kTp}^{(k+1)Tp} = 0. Cependant, [t] = Tp. Il vient
> donc : **P = UIcosφ** » — « Cette forme générale de l'expression de la puissance moyenne est indépendante de la nature du
> dipôle. Étant semblable à l'expression de la puissance consommée en courant continu, le produit UI intervenant dans
> l'expression de P est appelé **puissance apparente** du dipôle. La puissance apparente s'exprime en volt-ampère (V.A). Le
> facteur **cosφ** auquel la puissance moyenne est proportionnelle s'appelle **facteur de puissance**. Pour le circuit RLC
> série, cosφ = R/Z. Donc, ce facteur est toujours positif. Par suite, la puissance moyenne est positive, ce qui veut dire que
> le circuit RLC série se comporte dans l'ensemble comme un dipôle passif. D'autre part, on a U = Z.I, d'où : **P = R.I²**.
> Ainsi, on montre que la puissance active d'un circuit RLC série est due à sa résistance totale R : c'est une puissance
> consommée par effet Joule. En d'autres termes, la puissance moyenne dissipée dans le circuit sert à compenser
> l'amortissement : en moyenne, l'énergie transférée de l'excitateur à l'oscillateur sert, lorsque le régime oscillatoire est
> établi, à compenser les pertes par effet Joule. »

> **6.3 Résonance de puissance (p.129)** — « La puissance moyenne (P = RI²) d'un circuit RLC série est proportionnelle au carré
> de l'intensité efficace du courant oscillant dans le circuit. il s'en suit une résonance de puissance à chaque fois qu'il y a
> résonance d'intensité (Fig.14). A la résonance d'intensité, P est maximale, ce qui est en accord avec la condition
> (cos φ = 1) établie précédemment. »

> **6.4 Transfert de puissance moyenne (p.129–130)** — « **P = R U²/Z² = RU² / (R² + (Lω − 1/Cω)²)** » — « – Si l'amortissement
> est important, lorsque ω tend vers zéro ou ω est très grand, la puissance transférée est quasiment nulle. Mais, au voisinage
> de ωo, P devient égale à U²/R. Le transfert de puissance s'effectue alors quelle que soit la fréquence mais il reste faible.
> Par conséquent, l'amplitude des oscillations est faible. C'est ce qui justifie la résonance floue (Fig.15). – Si
> l'amortissement est faible, le transfert de puissance est important. Par conséquent, l'amplitude des oscillations est
> élevée. C'est ce qui justifie la résonance aiguë (Fig.15). »

> **6.5 Importance du facteur de puissance (p.130)** — tension imposée par le réseau de la STEG ; appareil de puissance nominale
> P parcouru par **I = P/(U cosφ)** ; échauffement des câbles : « perte en ligne ». « Si l'on désigne par Po la puissance
> moyenne perdue par effet Joule dans la ligne d'alimentation de résistance Ro, on a : Po = RoI², soit : **Po = Ro P²/(U²cos²φ)**
> P et U étant imposées, pour minimiser Po, il faut chercher à minimiser Ro et augmenter cosφ. » Diminuer Ro (câbles plus gros,
> plus lourds, plus chers) est limité ; « la seule solution pratique pour rendre minimales les pertes par effet Joule est
> d'augmenter le facteur de puissance cosφ. Pour ce, on exige qu'une installation électrique ait un facteur de puissance élevé
> (cosφ > 0,8). »
> **Conclusion** : « La puissance moyenne d'un circuit RLC série est dissipée par effet Joule. Cette dissipation se fait à
> n'importe quelle fréquence mais elle est d'autant plus importante que la résistance est plus grande. A la résonance
> d'intensité, correspond une résonance de puissance : la puissance moyenne de l'oscillateur RLC série est dans ces conditions
> la plus élevée. »

### L'essentiel (p.131, verbatim)

- Comme en régime libre non amorti, les oscillations forcées d'un circuit RLC série sont sinusoïdales mais de fréquence imposée
  par l'excitateur.
- La réponse d'un circuit RLC série à une tension excitatrice sinusoïdale de fréquence N est : – pour l'ensemble, un courant
  électrique alternatif sinusoïdal de valeur maximale : Iₘ = Uₘ/√(R² + (Lω − 1/Cω)²) – pour le condensateur, une charge
  électrique sinusoïdale de valuer maximale : Qₘ = Uₘ/√(R² + ω²(1/Cω − Lω − 1/Cω)²) **[coquille du manuel, lue sur l'image à
  220 dpi : formule dimensionnellement fausse ; l'expression du cours (p.120–121) est Qₘ = Uₘ/√(R²ω² + (1/C − Lω²)²) —
  l'auteur doit enseigner celle du cours]**.
- Contrairement au déphasage (φ_q − φ_u) de la charge par rapport à la tension excitatrice qui es toujours négatif, le
  déphasage (φᵢ − φ_u) de l'intensité du courant par rapport à la tension excitatrice peut être positif ou nul. [Le cours
  (p.119) admet aussi φᵢ < 0 (circuit inductif) : formulation incomplète [?].]
- En régime forcé sinusoïdal, les valeurs maximales Qₘ de la charge du condensateur et Iₘ de l'intensité du courant sont
  d'autant plus élevées que l'amortissement est plus faible.
- La résonance d'intensité est obtenue pour une fréquence d'excitations égale à la fréquence propre No de l'oscillateur, alors
  que celle de la charge est obtenue pour une fréquence d'excitations légèrement inférieure à No.
- La résonance d'intensité d'un circuit RLC série peut être accompagnée d'une surtension aux bornes du condensateur,
  caractérisée par un quotient Q > 1 appelé dans ces conditions facteur de surtension : Q = U_C/U
- En régime sinusoïdal forcé, la puissance moyenne P d'un circuit RLC série est la valeur moyenne prise par sa puissance
  instantanée p(t) durant une période : P = UIcosφ = RI²
- Comme la résonance d'intensité, la résonance de puissance est obtenue pour une fréquence des excitations égale à la fréquence
  propre de l'oscillateur.
- Les pertes par effet Joule sont d'autant plus faibles que le facteur de puissance est plus grand.

### Exercice résolu (p.132–134)

**Énoncé** — Condensateur C, bobine B (L), résistor Ro = 81,5 Ω en série ; GBF : u(t) sinusoïdale, Uₘ = 6 V, N réglable
(Fig.1 : GBF entre A et B ; K, Ro, D, (L, r), E, C).
1°) a) point (A ou B) à relier à la masse du GBF pour visualiser u(t) et u_Ro sur un oscilloscope bicourbe ; b) schéma des
branchements. 2°) Fréquence N₁ ; Fig.2 : base de temps 0,5 ms/div ; voie u(t) : 2 V/div ; voie u_Ro(t) : 1 V/div. a) identifier
u(t) ; b) déterminer graphiquement N₁ et Iₘ ; en déduire Qₘ ; c) calculer Z ; d) déphasage entre i(t) et u(t) ; en déduire que
la bobine a une résistance interne non nulle, la calculer. 3) Autre fréquence N₂, on visualise u(t) et u_C(t) : a) point à
relier à la masse ; b) schéma ; c) Fig.3, 1 ms/div, 2 V/div pour Y1 et Y2 : identifier u_C(t) ; d) fréquence de u_C(t) et son
déphasage par rapport à u(t) ; e) montrer que l'oscillateur est en résonance d'intensité ou bien en résonance de charge ;
f) facteur de surtension, danger ? ; g) calculer C et L.
**Solution** — 1°a) masse au point B (côté résistor). b) A → Y1 (ou Y2) pour u(t), D → Y2 (ou Y1) pour u_Ro(t) (Fig.4).
2°a) Uₘ = 6 V à 2 V/div : l'oscillogramme (1) « dont les crêtes sont distantes de 6 div » est u(t). b) u_Ro = Ro.i ⇒ même
fréquence ; T₁ sur 6 divisions à 0,5 ms/div ⇒ T₁ = 3 ms, **N₁ ≈ 333 Hz** ; U_Rom : 2 div à 1 V/div = 2 V ⇒ **Iₘ = U_Rom/Ro =
24,5 mA** ; q(t) = (Iₘ/2πN₁) sin(2πN₁t + φᵢ − π/2) ⇒ **Qₘ = Iₘ/2πN₁ = 11,7.10⁻⁶ C**. c) **Z = Uₘ/Iₘ = 244,9 Ω ≈ 245 Ω**.
d) Δφ = φᵢ − φ_u ; |Δφ| ↔ Δt = T/6 et π rad ↔ T/2 ⇒ |Δφ| = π/3 ; maxima de u_Ro après ceux de u ⇒ **Δφ = −π/3 rad** ;
cosφ = R/Z ⇒ R = Z.cosφ = 122,5 Ω > Ro = 81,5 Ω ⇒ **r = R − Ro = 41 Ω**. 3°a) masse au point A (Fig.5). b) B → Y1 (ou Y2) pour
u(t), E → Y2 (ou Y1) pour u_C(t). c) (1) seul d'amplitude 6 V = u(t) ; (2) = u_C(t). d) **N₂ = 167 Hz** ; maxima de u atteints
T/4 avant ceux de u_C ⇒ **φ_uC − φ_u = −π/2 rad**. e) φᵢ = φ_q + π/2 et u_C = q/C ⇒ φ_uC = φ_q ; φ_u − (φᵢ − π/2) = π/2 ⇒
**φ_u − φᵢ = 0** : résonance d'intensité. f) Q = U_Cm/Uₘ ; U_Cm = 7 V ⇒ **Q ≈ 1,17** ; « Q étant très peu supérieur à l'unité
[…] on ne court aucun danger. » g) Q = 1/(RCω₂) ⇒ C = 1/(RQω₂), ω₂ = 2πN₂ ⇒ **C = 6,68 μF** (imprimé « 6,68 ∝F ») ;
N₂ = 1/(2π√LC) ⇒ L = 1/(4π²N₂²C) ⇒ **L = 137 mH**.
(Dans la question 3 de l'énoncé, « 3) » sans « ° » ; la solution 2°c renvoie à tort à « question 2.c » pour U_Rom (déterminée
en 2.b) [?].)

### Exercices à résoudre (p.135–141) — réponses p.316 (colonne droite, « Chapitre 4 »)

**Tests rapides des acquis**
- **1 Items « vrai ou faux »** (p.135) : 1- oscillations d'un RLC série soumis à une tension sinusoïdale libres ; 2- fréquence
  des oscillations forcées peut être égale à la fréquence propre ; 3- résonance d'intensité quand la tension aux bornes du RLC
  est en phase avec l'intensité ; 4- résonance d'intensité quand l'impédance est maximale ; 5- Q augmente quand la résistance
  totale augmente ; 6- la puissance moyenne consommée par le condensateur est nulle ; 7- la résonance de puissance est elle
  même une résonance d'intensité ; 8- pour minimiser les pertes Joule en ligne, on diminue le facteur de puissance.
  (Pas de réponses imprimées.)
- **2 QCM** (« la (ou les) proposition(s) juste(s) ») : I- résonance d'intensité lorsque : a- impédance minimale ; b- fréquence
  imposée = fréquence propre ; c- impédance = résistance du résistor ; d- intensité et tension appliquée en phase. II- à la
  résonance d'intensité, i est : a- en quadrature avance sur la tension aux bornes du condensateur ; b- en quadrature retard
  par rapport à la tension aux bornes de la bobine ; c- en phase avec la tension aux bornes du résistor ; d- en phase avec la
  tension aux bornes du RLC. III- résonance de charge possible seulement si : a- N₀ > R/(2πL√2) ; b- C < R²/2L² ;
  c- LCN₀² = 1. IV- à la résonance d'intensité, une augmentation de la résistance entraîne : a- diminution de la fréquence
  de résonance ; b- diminution de l'amplitude maximale de l'intensité ; c- augmentation de la puissance moyenne maximale.
  V- Q s'écrit : a- 2πLN₀/R ; b- U_L/U quelle que soit N ; c- (1/R)√(C/L) ; d- U_C/U à la résonance d'intensité.
  (Pas de réponses imprimées. III-a et III-b : formules lues sur l'image.)

**Exercices d'application**
- **3** (p.136) : circuit d'accord radio, N = 16233 Hz, L = 10⁻⁴ H ; trouver C. Réponse : **C = 9,5.10⁻⁷ F**.
- **4** : C et bobine (L, r) en série, u(t) = 30√2 sinωt, ω = 2000 rad.s⁻¹ : I = 600 mA, U₁ (bobine) = 30 V, U₂ (condensateur)
  = 30 V ; i = Iₘsin(ωt + φ). 1°) Fresnel : φ, r, L, C ; 2°) comparer ω et ωo par leur quotient ; sens de variation de ω pour
  la résonance d'intensité. (Pas de réponse imprimée.)
- **5** : C = 20 μF, R = 20 Ω, L = 0,55 H, r = 12,5 Ω ; u(t) = 100√2 sin2πNt, N = 48 Hz. 1°) Z (sans démonstration), la
  calculer ; 2°) I en fonction de Z ; 3°) circuit équivalent à (R + r) : a) N = No, la calculer ; b) Zo et Io. Réponses :
  **2°) I = U/Z ; 3°a) N = 48 Hz ; 3°b) Z₀ = 32,5 Ω ; I₀ = 3,077 A**.
- **6** : R, L, C série ; U efficace, ω réglable ; ampèremètre. 1°) Fresnel : Z et déphasage en fonction de ω, R, L, C ;
  2°) a) allure de I = f(ω), phénomène ; b) ωo dépend-elle de R, L, C ? expression ; c) Z et déphasage pour ω = ωo.
  Réponses : **2°a) Résonance d'intensité ; 2°b) ω₀ ne dépend que de L et de C ; 2°c) Z = R et Δφ = 0**.
- **7** : bobine (L, r), C = 0,5 μF ; U = 2 V ; No = 2325 Hz, Io = 130 mA. 1°) caractéristiques de la bobine ; 2°) facteur de
  surtension et puissance moyenne maximale. Réponses : **1°) r = 15,4 Ω ; 2°) Q = 10,445 ; P = 0,26 W** (L non donnée en
  réponse).
- **8** (p.137) : portion MN : C et bobine (L, r) ; I = 0,20 A ; U_MN = 120 V, U_MP = 160 V, U_PN = 56 V (P : jonction bobine-
  condensateur). 1°) impédances bobine et condensateur, r ; 2°) déphasage de u_MN par rapport à i ; 3°) ωo = 250 rad.s⁻¹ en
  phase : a) L et C ; b) ω et N ; c) puissance moyenne ; 4°) I = 0,20 A pour une deuxième pulsation ω' ; 5°) comparer les
  puissances à ω, ωo, ω'. (Pas de réponse imprimée.)
- **9** : R = 50 Ω, C = 1 μF, L réglable (résistance négligeable), u(t) = 10√2 sin(100πt). 1°) équation différentielle en i ;
  2°) i(t) = Iₘsin(100πt + φ) : a) Lo pour la résonance d'intensité ; b) surtension aux bornes du condensateur ; 3°) [numéroté
  « 2°) » au manuel, p.137 col. droite [?]] tension de rupture Uo = 100 V : L à ne pas dépasser. Réponses : **2°a) L₀ = 1 H ;
  2°b) Q = 6,28 > 1 ; 3°) L < 1,6 H**.
- **10** : résistor, C, bobine purement inductive L ; R résistance totale ; u_AB = Uₘsinωt, U constante, ω réglable ;
  wattmètre. 1°) à ω = ωo, Po en fonction de U et R ; énergie Eo reçue pendant une période (U, R, ωo) ; 2°) à la résonance,
  E_t = E_L + E_C en fonction du temps, constante, en fonction de L, U, R ; que devient l'énergie reçue ? 3°) E_t/Eo en
  fonction de Q. Réponses : **1°) E₀ = 2πU²/ωoR ; 2°) E_t = LU²/R² ; 3°) E_t/E₀ = Q/2π**.
- **11** (p.138) : R = 300 Ω, C = 3 μF, bobine (L, r) ; u(t) sur Y1 (4 V/div), u_R(t) sur Y2 (2 V/div), 1 ms/div ; à N = No,
  oscillogramme : deux sinusoïdes en phase, celle de Y2 de plus faible amplitude. 1°) phénomène observé ; 2°) L et r.
  Réponse : **2°) L = 0,135 H ; r = 60 Ω**. (Amplitudes en divisions non relevées ici [?].)
- **12** : R, C, bobine purement inductive L = 0,1 H ; u = Uₘsin2πNt. 1°) équation différentielle en q ; 2°) a) Iₘ(Uₘ, R, L,
  C, N) ; b) Qₘ ; 3°) résonance de charge à Nr(R, L, No) ; disparaît si R dépasse une valeur limite (L, C) ; 4°) courbes (1) et
  (2) (Qₘ et Iₘ en fonction de N ; repères 205 et 210 Hz) : a) identifier Qₘ(N) ; b) N₀, Nr, C, R. Réponses : **4°a) Courbe
  (2) ; b) No = 210 Hz ; Nr = 205 Hz ; C = 5,75 μF ; R = 40,5 Ω**.

**Exercices de synthèse**
- **13** (p.138–139) : condensateur « EFD-CPM13B, Capacité 1,2 MF, Tolérence 10 %, Tension maximale 160 V » ; circuit : GBF
  U = 2 V, R = 10 Ω, bobine L = 58 mH (r), condensateur, voltmètre, ampèremètre. 1°) schéma ; 2°) à N = 610 Hz, I maximale
  = 96,7 mA : a) fréquence propre ; b) C ; quelle indication à la place de « MF » ; c) dans la tolérance ? (Pas de réponse.)
- **14** (p.139) : R = 40 Ω, C, bobine (L, r) ; u(t) = 10√2 sin(2πNt). 1°) à No : U_R = 9,6 V et u_C(t) = U_c√2 sin(318πt − π/2)
  avec U_c = 36 V : a) résonance d'intensité ; b) Io ; C, L, r ; Q ; c) montrer u_c² = −Q²u² + 2U_c² ; d) énergie totale en
  fonction de u et u_c, conservation. (Pas de réponse.)
- **15** : U = 10 V, R = 100 Ω, C = 0,5 μF, bobine r = 100 Ω, L = 50 mH. 1°) N₁ = 318 Hz : a) Z₁ ; b) I₁ ; c) P₁ ; d) φ₁ de u
  par rapport à i, grandeur en avance, caractère (résistif, capacitif ou inductif) ; 2°) diagramme de Fresnel à l'échelle ;
  3°) N = No : a) nouveau diagramme ; b) Zo, Io, Po. (Pas de réponse.)
- **16** (p.140) : générateur 0–10 V, 5 Hz à 5 kHz [imprimé « de 5 à 5 kHz »], ampèremètre, deux voltmètres, bobine (L, r),
  condensateur C, boîte de résistances 0–1,1 kΩ, oscilloscope bicourbe. 1°) schéma ; 2°) U = 5 V, tableau N (Hz) / I (mA) :
  100/1,6 ; 200/3,4 ; 300/5,7 ; 400/8,9 ; 500/15,1 ; 600/27,6 ; 700/47,0 ; 800/31,5 ; 900/20,5 ; 1000/14,6 ; 1100/11,7 ;
  1200/9,8 ; 1300/8,5 ; 1400/7,6 ; a) tracer I = f(N) (1 cm ↔ 100 Hz ; 1 cm ↔ 2,5 mA) ; b) No ; c) résistance totale ;
  3°) a) branchements (u sur voie A, intensité sur voie B) ; b) à N = No, oscillogramme (voie A 2 V/div, voie B 1 V/div,
  0,2 ms/div ; deux sinusoïdes en phase, (2) de plus grande amplitude) : courbe de la voie A, R réglable puis r ; c) U_C
  maximale = 21,5 V : C ; d) L. (Pas de réponse.)
- **17** (p.140–141) : R, C, bobine purement inductive L = 1 H ; u(t) = U√2 sinωt. 1°) I(U, R, L, C, ω) puis U_c ; 2°) résonance
  de charge pour ωr < ωo ; 3°) ω = 100π rad.s⁻¹ : chronogrammes (1) et (2) de u et u_c : a) lequel est u_c ; b) déphasage de u_c
  par rapport à u ; c) résonance d'intensité ; 4°) sensibilité verticale 10 V/div : expression de q(t). (Pas de réponse.)
- **18 Étude de texte** (p.141) : « Le facteur de puissance » (STEG, pertes en ligne, puissance apparente = active + réactive,
  condensateurs installés par les industriels pour améliorer le facteur de puissance). Questions : 1°) mauvais facteur de
  puissance et pertes en ligne ; 2°) avantages d'un facteur de puissance élevé ; 3°) démontrer l'amélioration du facteur de
  puissance par l'insertion de condensateurs. (Pas de réponse.)

**Fiche technique (p.142)** — « Construction de Fresnel » : somme de fonctions sinusoïdales isochrones yₖ = aₖsin(ωt + φₖ) ;
vecteur de Fresnel OA⃗ (module a, origine O, tournant à ω dans le sens trigonométrique, angle φ avec (O, i⃗) à t = 0 ;
projection sur (O, j⃗) = y) ; yₖ ↦ OA⃗ₖ[aₖ, φₖ], y = Σyₖ ↦ OA⃗ = ΣOA⃗ₖ ⇒ OA⃗[a, φ] (Fig.1–4).
**En savoir plus (p.143)** — « Générateur de courant haute fréquence » : appareil vers 1895 (bobine de Ruhmkorff, décharge
oscillante des condensateurs), Tesla, d'Arsonval (d'arsonvalisation, 1893), résonateur du docteur Oudin (source :
www.patrimoine.polytechnique.fr). Culture, hors évaluation.

### Bornes de scope (chapitre 4)

- ✅ **INCLUS** : distinction **excitateur (GBF) / résonateur (RLC série)** ; montages de visualisation à l'oscilloscope
  bicourbe (u et u_Ro ; u et u_C ; choix du point de masse, résistor ou condensateur côté masse) ; u_Ro image de i, u_C image
  de q ; lecture d'oscillogrammes : période, fréquence, amplitude (sensibilités en ms/div, V/div), décalage horaire ;
  **déphasage** Δφ, |Δφ| = 2πΔt/T, concordance, opposition, quadrature avance/retard ; **équations différentielles** en i
  (forme intégro-différentielle avec ∫i.dt) et en q (L d²q/dt² + R dq/dt + q/C = u) — établies, non résolues ; solutions de
  régime permanent i = Iₘsin(ωt + φᵢ), q = Qₘsin(ωt + φ_q) admises ; **impédance** Z = Uₘ/Iₘ = U/I, Z = √(R² + (Lω − 1/Cω)²)
  (Ω) ; Qₘ = Iₘ/ω = Iₘ/2πN ; φᵢ = φ_q + π/2 ; **construction de Fresnel** (trois cas Lω ≷ 1/Cω, circuit inductif /
  capacitif / résonance), tgφᵢ = (1/Cω − Lω)/R avec −π/2 < φᵢ < π/2, cosφᵢ = R/Z ; −π < φ_q < 0 ; **résonance d'intensité**
  (N = No = 1/2π√LC, Z = R, Imo = Uₘ/R, i en phase avec u) ; **résonance de charge** (Nr = √(No² − R²/8π²L²) < No, condition
  R² < 2L/C, étude de g(ω) par dérivée, résonance impossible si R² − 2L/C > 0, Qmo = Uₘ/(R√(1/LC − R²/4L²))) ; **influence de
  R** : résonance aiguë / floue / très floue, fréquence de résonance d'intensité indépendante de R ; « réponse linéaire » ;
  **surtension** : Q = U_C/U à la résonance d'intensité, Q = 1/((Ro + r)Cωo) = Lωo/(Ro + r) = (1/(Ro + r))√(L/C), dangers
  (claquage, étincelles), surtension aux bornes de la bobine (U_Bobine = √(r² + (Lω₀)²) I) ; **applications** (quartz,
  haut-parleur/microphone, radio ; hi-fi = résonance floue) ; **puissance instantanée** p(t) = UIcosφ − UIcos(2ωt + φ),
  période Tp = T/2 ; **puissance moyenne** (définition, P = (1/Tp)∫p dt, P = UIcosφ = RI², W, wattmètre) ; **puissance
  apparente** UI (V.A) ; **facteur de puissance** cosφ = R/Z ; **résonance de puissance** ; P = RU²/Z² ; pertes en ligne
  Po = RoP²/(U²cos²φ), exigence cosφ > 0,8 (STEG) ; en exercices : calculs d'énergie E_L + E_C à la résonance, conservation,
  E_t/E₀ = Q/2π (ex. 10, 14 d) ; relation u_c² = −Q²u² + 2U_c² (ex. 14) ; tracé point par point de I = f(N) (ex. 16) ;
  diagramme de Fresnel à l'échelle (ex. 15) ; tolérance d'un composant (ex. 13).
- ⛔ **EXCLU** (absent du chapitre) : **nombres complexes / impédance complexe** et notation j ; **résolution** de l'équation
  différentielle (régime transitoire non étudié : seule la solution permanente est admise) ; **bande passante**, fréquences de
  coupure à −3 dB, largeur de bande et relation Q = No/ΔN ; **puissance réactive** (citée seulement dans le texte de l'ex. 18,
  sans formule ni unité var) ; **compensation par condensateur** chiffrée (seulement « démontrer » qualitativement, ex. 18) ;
  RLC **parallèle**, filtres ; régimes **non sinusoïdaux** (note marginale : « Le cas unique qui figure dans le programme est
  celui du régime sinusoïdal forcé ») ; résonance **mécanique** (chapitre suivant du manuel, non traitée ici) ; **triphasé**,
  transformateur ; valeurs de réponses non imprimées (ne pas inventer de corrigé « officiel » pour les ex. 1, 2, 4, 8, 13–18).
  Appareillage : GBF, oscilloscope bicourbe, ampèremètre, voltmètre, wattmètre, boîte de résistances — pas d'ExAO/carte
  d'acquisition dans ce chapitre.

### Lecture

- **Couche texte** : p.110 à 143 (34 pages) et p.316–318 (réponses ; le chapitre 4 n'occupe que la colonne droite de la p.316)
  via `/root/.cache/yqa-manuels/223433/txt/pNNN.txt`.
- **Pages lues sur l'image** (110 dpi) : **35** — 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124,
  125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 316 ; zooms 200–220 dpi :
  p.112 (Fig.2, Fig.3), p.113 (Fig.5), p.117 (Fig.9), p.131 (formule de Qₘ de l'Essentiel), p.140 (oscillogrammes ex. 16, 17),
  p.316 (réponses chap. 4). p.317–318 vues en couche texte seulement (aucune réponse du chapitre 4).
- **Sondage image** : totalité des pages, dont les plus denses 114, 118, 119, 121, 123, 126, 128, 131, 134, 135. **Écarts
  texte/image** : p.110 « T = 2π/ω » et √2 perdus ; p.111 légende inclinée en fragments de mots ; p.114 ∫, fractions et
  « 2πN » rendus « 2 N » ; p.118 tous les vecteurs de Fresnel, ω, φ, π perdus (« sin t ») ; p.119 racines et encadrés
  illisibles ; p.120–121 g(ω), ω₁² = 1/LC − R²/2L², Nr (π et racine perdus) ; p.123 Qmo sans racine ; p.126 √(L/C) perdue ;
  p.127–128 √2, intégrales et bornes kTp/(k+1)Tp ; p.131 Qₘ de l'Essentiel illisible ; p.133–134 φ, π/3, π/2 perdus,
  « C = 6,68 ∝F » ; p.135 QCM III-a/b et V (fractions, racines) ; p.136–139 « 30√2 », « 10√2 », « 318πt − π/2 » ; p.316
  colonnes entremêlées (chap. 1–3 et 4). Aucun écart non résolu après lecture image.
- **Doutes signalés [?]** : (1) **Essentiel p.131 : formule de Qₘ fautive** (ω² devant une parenthèse contenant 1/Cω − Lω −
  1/Cω) — suivre p.120–121 ; (2) p.123 : Qmo écrit sans « + » entre R²(2πNr)² et [1/C − L(2πNr)²]² ; (3) p.124 : « devient
  inférieure à la valeur de No² » pour R très grande (le sens attendu est « supérieure » ; texte contradictoire) ; (4) p.116 :
  i(t) = 2πNQₘ**cos**(2πNt + φ_q + π/2) (sin attendu) ; (5) Essentiel : φᵢ − φ_u « peut être positif ou nul » (omet négatif,
  contredit p.119) ; (6) p.117 : « On reprend le montage de la figure 3 » (figure 4 attendue) et courbes de Fig.9 « au cours
  du temps » ; graduations Qₘ de Fig.9 « 30, 20, 10, 10 » ; légende Fig.3 inversée ; (7) renvoi « fiche technique (p.141) »
  alors qu'elle est p.142 ; (8) ex. 9 : deux « 2°) » (le second = 3°) d'après la réponse p.316 « 3°) L < 1,6 H ») ; ex. 16
  « fréquence réglable de 5 à 5 kHz » ; ex. 13 « 1,2 MF » (piège voulu par l'énoncé, question 2°b) ; (9) solution 2°a de l'ER :
  « crêtes distantes de 6 div » (amplitude crête-à-crête) ; solution f renvoie à « question 2.c » au lieu de 2.b ; (10) les
  valeurs numériques lues sur les figures du cours (Fig.3 ≈ (4 V ; 0,6 V), pic Fig.9 ≈ 30 mA, Fig.14 ≈ 60 mW) sont des
  lectures graphiques, non des données imprimées ; (11) programme officiel non consulté ici : la **résonance de charge**
  (dérivation de g(ω)), la **surtension aux bornes de la bobine** et le **transfert de puissance P(ω)** sont au manuel ; leur
  exigibilité au Bac Sciences expérimentales est à confirmer (R-3).

## 2.5 Chapitre 5 — Oscillations libres d'un pendule élastique (manuel 223433, p.144–167)

Partie « Evolution de systèmes » (bandeau courant de chaque page). Notation du manuel : ω₀ est imprimé
tantôt « ωo », tantôt « ω0 » ; T₀ tantôt « To », tantôt « T0 » (même grandeur). Vecteurs fléchés
(P⃗, R⃗, T⃗, f⃗, i⃗, v⃗, a⃗) lus sur l'image.

**Objectifs (p.144, encadré)** — verbatim :
- « A l'aide d'un enregistrement graphique, reconnaitre le régime d'oscillations libres (amorties ou non
  amorties) d'un pendule élastique. »
- « Distinguer les régimes pseudopériodique, apériodique et critique des oscillations amorties. »
- « Etablir l'équation différentielle des oscillations libres d'un pendule élastique. »
- « Mesurer la période des oscillations d'un pendule élastique. »
- « Calculer l'énergie mécanique d'un pendule élastique en régime libre. »
- « Expliquer la conservation de l'énergie mécanique d'un oscillateur non amorti. »
- « Expliquer la diminution d'amplitude des oscillations libres amorties d'un pendule élastique par la
  non conservation de son énergie mécanique. »

**Prérequis (p.144)** — SAVOIR : écrire l'expression de l'énergie cinétique ; énumérer les facteurs dont
dépend l'énergie potentielle élastique ; écrire l'équation horaire d'un mouvement rectiligne sinusoïdal ;
énoncer la loi de Hooke. SAVOIR FAIRE : délimiter un système matériel ; distinguer les forces intérieures
des forces extérieures à un système ; reconnaitre la période et la fréquence d'un mouvement périodique ;
calculer la pulsation d'un mouvement rectiligne sinusoïdal ; appliquer la relation fondamentale de la
dynamique à un solide en mouvement de translation ; « Ecrire la solution générale de toute équation
différentielle de la forme d²x/dt² + kx = 0, où k est une constante positive » ; appliquer la loi de Hooke.

**Page d'ouverture (p.145)** — « 5 — OSCILLATIONS LIBRES D'UN PENDULE ÉLASTIQUE ». Deux photos légendées :
VTT tout suspendu (« Avec son amortissur à ressort, le VTT (Vélo Tout Terrain) TS (Tout Suspendu) donne au
cycliste un confort d'utilisation supérieur dans une compétition de descente d'une montagne. ») ; gymnaste
aux anneaux (« En évitant le balancement des anneaux, le gymnaste démontre tant sa force que son
équilibre. »). Questions d'accroche :
- « Les geysers, le cœur humain et le balancier d'une horloge sont, entre beaucoup d'autres exemples, des
  systèmes oscillants. Pourquoi ? »
- « Quelle est l'origine du ronflement continu que l'on entend souvent à proximité de fils électriques ou
  téléphoniques aériens ? »
- « A quoi est due la catastrophe naturelle connue sous le nom de tsunami ? »

**Définition liminaire (p.146)** — « On désigne par pendule élastique tout système constitué d'un solide (S)
de masse m attaché à un ressort à spires non jointives, de masse négligeable et de raideur k. » [coquilles
« sonstitué », « mase » corrigées].

**Plan du chapitre** (pas de sommaire imprimé ; titres lus dans le corps) :
- **OSCILLATIONS LIBRES NON AMORTIES** (p.146–151) : 1 Mise en évidence · 2 Facteurs dont dépend la période
  des oscillations (2.1 Influence de l'amplitude ; 2.2 Influence de la masse du solide (S) ; 2.3 Influence
  de la raideur du ressort ; 2.4 Conclusion générale : expression de la période T₀) · 3 Etude théorique ·
  4 Energie d'un pendule élastique (4.1 Energie cinétique ; 4.2 Energie potentielle élastique ; 4.3 L'énergie
  mécanique et sa conservation ; 4.4 Transformations mutuelles de l'énergie cinétique et de l'énergie
  potentielle).
- **OSCILLATIONS LIBRES AMORTIES** (p.152–154) : 1 Etude expérimentale · 2 Etude théorique (2.1 Equation
  différentielle des oscillations ; 2.2 L'énergie mécanique et sa non conservation).
- **Analogie entre un oscillateur mécanique et un oscillateur électrique** (p.155, tableau).
- **L'essentiel** (p.156) · **Exercices** : exercice résolu (p.157–159) ; « Exercices à résoudre » :
  Tests rapides des acquis (1 Items vrai ou faux, 2 QCM, p.160–161), Exercices d'application (3–5, p.161),
  Exercices de synthèse (6–12, p.161–164), 13 Etude de texte « Le tsunami » (p.165–166) · **En savoir plus**
  (p.167).

### Cours — Manipulations, questions, conclusions

**I.1 Mise en évidence (p.146–147)**
- **Manipulation** : pendule élastique horizontal sur banc à coussin d'air (Fig.1, photo « Oscillateur
  mécanique sur banc à coussin ») ; m = 0,1 kg ; k = 20 N.m⁻¹ ; (S) écarté de d = 2 cm de sa position
  d'équilibre dans la direction de l'axe du ressort, abandonné sans vitesse initiale. « Le solide (S)
  effectue des oscillations de part et d'autre de sa position d'équilibre (position de repos) : on dit que
  les oscillations sont libres. Le système {solide, ressort} constitue un oscillateur libre. »
  Remarque : l'enregistrement peut être réalisé par un dispositif d'acquisition informatique.
- **Enregistrement (Fig.2)** : sinusoïde x(mm) entre +20 et −20, départ à x = +20 à t = 0 ; un repère
  « 1,1 » (s) en pointillé tombe sur le 3ᵉ minimum (lu sur l'image : 2,5 oscillations en 1,1 s).
  [? légende imprimée erronée : « Fig.3 : Tracé de Um en fonction de f (URom) » — reprise d'un autre
  chapitre ; la figure est l'enregistrement x(t).]
- **Questions** : 1°) a) mesurer les valeurs maximales et minimales de l'élongation x de G, les comparer
  entre elles et à d ; b) mesurer les intervalles de temps séparant les maximums (ou minimums) successifs
  et les comparer ; 2°) en déduire si les oscillations sont amorties ou non amorties et qu'elles sont
  périodiques de période T₀ que l'on précisera ; 3°) conclure quant à la nature du mouvement de G.
- **Conclusion (encadré, p.147)** : « Les oscillations libres non amorties d'un pendule élastique sont
  rectilignes sinusoïdales. L'élongation s'écrit : x = Xm sin(2π t/T₀ + φ) » [forme imprimée
  x = Xₘ sin((2π/T₀)t + φ)]. Remarque : « Les valeurs de l'amplitude Xm et de la phase initiale φ dépendent
  des conditions initiales. »

**I.2 Facteurs dont dépend la période (p.147–149)**
- **2.1 Influence de l'amplitude** — Manipulation : même expérience pour différentes valeurs de d (Xm) ;
  chronomètre, durée Δt de dix oscillations. Tableau : Xm (cm) = 1 | 2 | 3 | 4 | 5 ; Δt (s) = 4,4 | 4,5 |
  4,4 | 4,4 | 4,5. Remarque : réalisable avec un pendule élastique vertical (Fig.3, schéma ressort vertical +
  masse). Questions : 1°) calculer T₀ pour chaque Xm ; 2°) comparer, en déduire si les oscillations
  d'amplitudes différentes sont isochrones. **Conclusion** : « La période T₀ des oscillations libres non
  amorties d'un pendule élastique est indépendante de leur amplitude. »
- **2.2 Influence de la masse** — Manipulation : solides de masses différentes ; T₀ déterminée
  indirectement. Tableau : m (kg) = 0,050 | 0,100 | 0,150 | 0,200 | 0,50 [? sic, vraisemblablement 0,250] |
  0,300 ; Δt = 10T₀ (s) = 3,2 | 4,4 | 5,4 | 6,3 | 7,0 | 7,7. Questions : 1°) montrer qualitativement que T₀
  n'est pas proportionnelle à m ; 2°) Fig.4 (droite T₀² (s²) = f(m) (kg), passant par l'origine, ≈ 0,6 s²
  pour 0,3 kg, lu sur l'image) : montrer que T₀² est proportionnelle à m, déterminer la constante ;
  3°) en déduire la relation entre T₀ et m. **Conclusion** : « La période des oscillations libres non
  amorties d'un pendule élastique est proportionnelle à la racine carrée de la masse du solide (S). »
- **2.3 Influence de la raideur** — Manipulation : même solide de masse 100 g, ressorts de raideurs
  différentes. Tableau : k (N.m⁻¹) = 10 | 20 | 30 | 40 | 50 ; Δt = 10T₀ (s) = 6,28 | 4,44 | 3,62 | 3,14 |
  2,80. Questions : 1°) montrer qualitativement que T₀ n'est pas inversement proportionnelle à k ;
  2°) Fig.5 (droite T₀² (10⁻² s²) = f(1/k) (10⁻² N⁻¹.m), par l'origine, ≈ 40 pour 10, lu sur l'image) :
  montrer que T₀² est proportionnelle à 1/k, déterminer la constante ; 3°) relation entre T₀ et k.
  **Conclusion** : « La période des oscillations libres non amorties d'un pendule élastique est
  inversement proportionnelle à la racine carrée de la raideur k du ressort. »
- **2.4 Conclusion générale : expression de la période T₀ (p.148–149)** — « La période d'un pendule
  élastique est indépendante de l'amplitude des oscillations, elle ne dépend que des grandeurs m et k
  caractéristiques du pendule, d'où sa qualification de période propre. Etant à la fois proportionnelle à
  √m et inversement proportionnelle à √k, la période propre d'un pendule élastique est alors
  proportionnelle à √(m/k), ce qui signifie T₀ = C√(m/k) où C est une constante dont la valeur 2π peut être
  déduite des résultats obtenus précédemment. D'où : **T₀ = 2π√(m/k)** ».

**I.3 Etude théorique (p.149)**
- Forces extérieures sur (S) dans un repère lié au laboratoire : poids P⃗, réaction R⃗ du coussin d'air,
  tension T⃗ du ressort (Fig.6 : ressort horizontal, solide (C)/G, axe x′x d'origine O, vecteur i⃗).
- **Questions** : 1°) a) montrer que T⃗ = −kx·i⃗ (k raideur, x élongation de G à l'instant t) ; b) justifier
  la qualification de T⃗ comme force de rappel ; 2°) par la relation fondamentale de la dynamique, montrer
  que l'équation différentielle du mouvement de G s'écrit d²x/dt² + ω₀²x = 0 avec ω₀² = k/m ; 3°) vérifier
  que cette équation admet comme solution générale x = Xm sin(ω₀t + φ) ; 4°) montrer que l'expression
  théorique de T₀ s'identifie à celle trouvée expérimentalement.
- **Conclusion (encadré)** : « Etant sinusoïdales, les oscillations libres non amorties d'un pendule
  élastique sont régies par l'équation différentielle : **d²x/dt² + ω₀²x = 0 avec ω₀² = k/m**. »

**I.4 Energie d'un pendule élastique (p.150–151)**
- « L'énergie mécanique E du système {solide (S) + ressort} est la somme de l'énergie cinétique Ec due au
  mouvement du solide (S) et de l'énergie potentielle élastique Ep due à la déformation du ressort :
  E = Ec + Ep. »
- **4.1 Energie cinétique** (cours rédigé, vérifié sur l'image) : Ec = ½mv² ; « or, v = dx/dt =
  Xmω₀ cos(ω₀t + φ) d'où : Ec = ½ m Xm² ω₀² cos²(ω₀t + φ) » ; « Compte tenu de ω₀²m = k, il vient :
  **Ec = ½kXm² cos²(ω₀t + φ) = ¼kXm²[1 + cos 2(ω₀t + φ)]** » ; « les variations de l'énergie cinétique en
  fonction du temps sont périodiques de période T₀/2 » (Fig.7 : Ec(t) pour φ = 0, maximum ½kXm² à t = 0,
  T₀/2, T₀).
- **4.2 Energie potentielle élastique** : « On a vu en deuxième année que l'énergie potentielle élastique
  d'un système matériel déformable dépend de ses caractéristiques. Pour un pendule élastique, étant une
  fonction de la raideur k du ressort et de sa déformation Δl, elle s'écrit sous la forme : » encadré
  **Ep = ½kΔl²**. Questions : 1°) montrer que Ep = ¼kXm²[1 − cos 2(ω₀t + φ)] ; 2°) représenter Ep = f(t) et
  montrer que sa période est T₀/2.
- **4.3 L'énergie mécanique et sa conservation** : E = Ec + Ep ; « E = ½kXm²[cos²(ω₀t + φ) + sin²(ω₀t + φ)].
  Or, cos²(ω₀t + φ) + sin²(ω₀t + φ) = 1. Il vient donc : **E = ½kXm² = ½mVm²**. Ainsi,
  **E = ½mv²(t) + ½kx²(t) = cte, ∀ t**. » **Conclusion (p.151)** : « En régime libre non amorti, l'énergie
  mécanique d'un pendule élastique horizontal est constante. Par suite, un tel système est dit
  conservatif. »
- **4.4 Transformations mutuelles Ec ↔ Ep** : passage par x = 0 avec v = ± Vm ; rebroussement quand v = 0 et
  x = ± Xm. Question : « Interpréter énergétiquement ces propriétés oscillatoires. » Interprétation
  (résumée) : en x = Xm énergie purement potentielle ; en se rapprochant de la position de repos Ep diminue
  aux dépens de Ec… ; en x = −Xm, Ec nulle, Ep maximale, (S) rebrousse chemin. Fig.8 : en fonction de x
  (−Xm à Xm), E horizontale, Ep parabole de sommet en 0, Ec parabole renversée ; « l'énergie cinétique et
  l'énergie potentielle dont la somme est constante varient toujours en sens inverses ». **Conclusion** :
  « Les oscillations libres non amorties d'un pendule élastique sont auto-entretenues par les
  transformations mutuelles de ses énergies cinétique et potentielle. »

**II. Oscillations libres amorties (p.152–154)**
- Introduction : l'amplitude diminue « à cause des facteurs dissipatifs inévitables (essentiellement les
  frottements) » ; même sur coussin d'air les oscillations prennent fin ; « De telles oscillations sont
  dites amorties. »
- **II.1 Etude expérimentale — Manipulation** : dispositif de la Fig.1 + palette fixée sur le solide
  perpendiculairement au déplacement, se déplaçant dans l'air puis dans un liquide (eau). Chronogrammes
  Fig.9 (air ; repère « 1,8 s ») et Fig.10 (eau ; repère « 2 s »). [Lu sur l'image : chacun des repères
  couvre 4 pseudopériodes, soit T₁ ≈ 0,45 s, T₂ ≈ 0,5 s — valeurs non imprimées, déduites de la figure.]
  **Questions** : 1°) a) évolution de l'amplitude ; en déduire que les oscillations sont plus amorties dans
  l'eau que dans l'air ; b) montrer que les maximums (ou minimums) sont atteints à intervalles égaux T₁
  (air), T₂ (eau), à calculer ; 2°) comparer T₁, T₂ entre eux et avec T₀ ; 3°) en déduire que, « comme celles
  d'un circuit RLC série », les oscillations libres amorties sont pseudopériodiques.
  **Interprétation** : l'amplitude décroît plus vite dans l'eau ; « Le passage du solide par la position
  d'équilibre est toujours périodique, mais le mouvement oscillatoire n'est plus périodique à cause de la
  diminution de l'amplitude. Le mouvement est dit pseudopériodique. »
- **Définitions (p.153)** : « On appelle pseudopériode la durée T qui sépare deux passages successifs du
  solide par la même position et dans le même sens. » ; « La valeur de la pseudopériode T (T₁ ou T₂) est
  voisine de celle de la période propre T₀ des oscillations : T est légèrement supérieure à T₀. » ; palette
  totalement immergée ou liquide plus visqueux (huile) : « le mouvement cesse d'être oscillatoire à partir
  d'une certaine valeur de l'amortissement : on dit qu'il est apériodique (Fig.11) » (Fig.11 : x(t) décroît
  sans osciller vers 0) ; « Pour un amortissement particulier, l'oscillateur retourne à sa position
  d'équilibre, sans osciller, en un minimum de temps : un tel régime est dit apériodique critique. »
  **Conclusion** : « Selon l'importance de l'amortissement, les oscillations d'un pendule élastique sont :
  – faiblement amorties, le régime est pseudopériodique. – fortement amorties, le régime est apériodique. »
- **II.2.1 Equation différentielle (p.153)** : forces (Fig.12) : poids P⃗, réaction R⃗, tension
  T⃗ = −kx i⃗ (force de rappel), frottements « supposés de type visqueux, elles sont équivalentes à une
  force f⃗ de sens contraire au vecteur vitesse et de la forme : **f⃗ = −hv⃗**, où h est une constante
  positive, ne dépendant que de la nature du liquide visqueux, appelée coefficient de frottement. »
  Deuxième loi de Newton : P⃗ + R⃗ + T⃗ + f⃗ = ma⃗ ; projection sur x′x : −kx − h dx/dt = m d²x/dt² ;
  « il vient finalement : **m d²x/dt² + h dx/dt + kx = 0** ou encore : **d²x/dt² + (h/m) dx/dt + (k/m) x = 0
  (1)** ». « Cette équation différentielle admet des solutions qui dépendent de la valeur de h et qui
  donnent les régimes mis en évidence expérimentalement. » (aucune solution explicite donnée).
- **II.2.2 L'énergie mécanique et sa non conservation (p.154)** : E = ½mv² + ½kx² ; dE/dt = mv dv/dt +
  kx dx/dt ; dE/dt = (dx/dt)[m d²x/dt² + kx] ; d'après (1), m d²x/dt² + kx = −h dx/dt, d'où
  **dE/dt = −h(dx/dt)² = −hv²** ; dE/dt < 0 : l'énergie diminue, dissipée « sous forme d'énergie
  thermique », ce qui « ne permet pas des transformations mutuelles intégrales d'énergie cinétique et
  d'énergie potentielle », d'où la diminution de l'amplitude. **Conclusion (encadré)** : « Le pendule
  élastique soumis à des forces de frottement n'est pas conservatif. Dans le cas de frottements visqueux,
  la diminution d'énergie mécanique d'un pendule élastique est telle que : dE/dt = −hv², où h est le
  coefficient de frottement. La diminution d'énergie due aux frottements est elle-même la cause
  d'amortissement des oscillations libres. »

### Tableau — Analogie oscillateur mécanique / oscillateur électrique (p.155, lu sur l'image)

| | pendule élastique | circuit RLC série |
|---|---|---|
| Coefficient d'inertie | masse m | inductance L (imprimé « indulance ») |
| Coefficient de rappel | raideur k | inverse de la capacité 1/C |
| Facteur dissipatif | coefficient de frottement h | résistance R |
| Grandeurs oscillantes | élongation x ; vitesse v = dx/dt | charge q ; intensité i = dq/dt |
| Éq. diff. amorties | d²x/dt² + (h/m)dx/dt + (k/m)x = 0 | d²q/dt² + (R/L)dq/dt + (1/LC)q = 0 |
| Éq. diff. non amorties | d²x/dt² + ω₀²x = 0 avec ω₀² = k/m | d²q/dt² + ω₀²q = 0 avec ω₀² = 1/LC |
| Période propre | T₀ = 2π√(m/k) | T₀ = 2π√(LC) |
| Équation horaire (non amorties) | x = Xm sin(ω₀t + φx) ou v = Vm sin(ω₀t + φv) | q = Qm sin(ω₀t + φq) ou i = Im sin(ω₀t + φi) |
| Énergies | potentielle élastique ½kx² ; cinétique ½mv² ; mécanique E = ½kx² + ½mv² | électrostatique ½q²/C ; magnétique ½Li² ; totale E = ½q²/C + ½Li² |
| Non amorti : se conserve | E = ½kXm² = ½mVm² = cte | E = ½Qm²/C = ½LIm² = cte |
| Amorti : diminue | dE/dt = −hv² < 0 | dE/dt = −Ri² < 0 |

### Encadrés, définitions, lois et relations (verbatim, vérifiés sur l'image)

- Pendule élastique : solide (S) de masse m + ressort à spires non jointives, de masse négligeable, de
  raideur k (p.146).
- x = Xm sin(2πt/T₀ + φ) ; Xm et φ dépendent des conditions initiales (p.147).
- T₀ indépendante de l'amplitude ; proportionnelle à √m ; inversement proportionnelle à √k ; « période
  propre » ; **T₀ = 2π√(m/k)** (p.147–149).
- T⃗ = −kx·i⃗ (force de rappel) (p.149) ; **d²x/dt² + ω₀²x = 0 avec ω₀² = k/m** ; solution générale
  x = Xm sin(ω₀t + φ) (p.149).
- Ec = ½mv² = ½kXm² cos²(ω₀t + φ) = ¼kXm²[1 + cos 2(ω₀t + φ)], période T₀/2 ; Ep = ½kΔl² (encadré) ;
  Ep = ¼kXm²[1 − cos 2(ω₀t + φ)], période T₀/2 ; E = ½kXm² = ½mVm² ; E = ½mv²(t) + ½kx²(t) = cte ∀t ;
  système conservatif (p.150–151).
- Oscillations auto-entretenues par les transformations mutuelles Ec ↔ Ep (p.151).
- Pseudopériode (définition) ; T légèrement supérieure à T₀ ; régimes pseudopériodique / apériodique /
  apériodique critique (p.152–153).
- f⃗ = −hv⃗ ; m d²x/dt² + h dx/dt + kx = 0 ⇔ d²x/dt² + (h/m)dx/dt + (k/m)x = 0 (p.153).
- dE/dt = −hv² < 0 ; non conservatif (p.154).

### L'essentiel (p.156) — verbatim

- « En l'absence de tout frottement, les oscillations libres d'un pendule élastique sont non amorties.
  Autrement, elles sont d'autant plus amorties que les frottements sont plus importants. »
- « Les oscillations libres non amorties d'un pendule élastique sont régies par l'équation
  différentielle : d²x/dt² + ω₀²x = 0, où x est l'élongation du centre d'inertie du solide S et
  ω₀² = k/m. »
- « Les oscillations libres non amorties d'un pendule élastique sont périodiques de période propre :
  T₀ = 2π√(m/k). »
- « En l'absence de tout frottement, le pendule élastique oscillant est un système conservatif. »
- « Les oscillations libres non amorties d'un pendule élastique résultent des transformations mutuelles
  d'énergie cinétique et d'énergie potentielle. »
- « Les oscillations libres amorties d'un pendule élastique soumis à des frottements visqueux sont régies
  par l'équation différentielle : d²x/dt² + (h/m) dx/dt + ω₀²x = 0 où h est le coefficient de frottement.
  Selon l'importance de l'amortissement, le régime peut être : – pseudopériodique (amortissement faible),
  – apériodique (amortissement important). »
- « Les oscillations libres amorties d'un pendule élastique sont pseudopériodiques ; leur pseudopériode T
  est légèrement supérieure à la période propre de l'oscillateur : l'écart (T – T₀) est d'autant plus
  remarquable que l'amortissement est plus important. »
- « La diminution d'énergie due aux frottements rend les oscillations libres du pendule élastique
  amorties. »

### Exercice résolu (p.157–159)

**Énoncé** : ressort à spires non jointives, masse négligeable, k = 10 N.m⁻¹, enfilé sur une tige
horizontale ; cylindre creux (C), m = 100 g, coulisse sans frottement ; abscisse x de G repérée par
rapport à O (position d'équilibre) (Fig.1 : (R), (C), (T), axe x′x, i⃗). Écarté de x₀ = 2 cm, abandonné à
t₀ = 0. 1°) sans vitesse initiale : a) par le théorème du centre d'inertie, montrer que les oscillations
sont sinusoïdales de pulsation propre ω₀ à calculer ; b) montrer par dE/dt que le système est
conservatif ; c) exprimer E en fonction de k et x₀, en déduire Xm1 = x₀ ; d) équation horaire. 2°) avec
v₀ = 0,2 m.s⁻¹ : a) qu'est-ce qui change ? (qualitatif) ; b) avec x(t) = Xm2 sin(ω₀t + φ₂), déterminer Xm2,
φ₂, Vm2 ; c) calculer E₀₂ à t₀ = 0 ; d) retrouver énergétiquement Xm2 et Vm2. 3°) comparer les énergies
mécaniques des deux expériences.
**Solution** :
- 1°) a) forces P⃗, R⃗ (tige), T⃗ ; P⃗ + T⃗ + R⃗ = ma⃗ ; −kx = ma = m d²x/dt² ⇒ d²x/dt² + ω₀²x = 0 (1),
  ω₀² = k/m ; ω₀ = √(k/m) ; A.N. ω₀ = 10 rad.s⁻¹.
- b) E = ½mv² + ½kx² ; dE/dt = kx dx/dt + mv dv/dt = v[kx + m d²x/dt²] = 0 d'après (1) ⇒ conservatif.
- c) E₁ = E₀₁ = ½kx₀² ; en x = ±Xm1, v = 0 ⇒ E₁ = ½kXm1² ⇒ Xm1 = x₀.
- d) x₀ = Xm1 sin φ₁, Xm1 = x₀ = 0,02 m ⇒ sin φ₁ = 1, φ₁ = π/2 rad ; **x(t) = 0,02 sin(10t + π/2)**.
- 2°) a) E₀₂ > E₀₁ ⇒ Xm2 > Xm1 = x₀. b) v(t) = Xm2ω₀ cos(ω₀t + φ₂) ; x₀ = Xm2 sin φ₂ (1),
  v₀ = Xm2ω₀ cos φ₂ (2) ; (1)/(2) : tg φ₂ = x₀ω₀/v₀ = 1 ⇒ φ₂ = π/4 ou 3π/4 ; cos φ₂ > 0 ⇒ **φ₂ = π/4 rad** ;
  Xm2 = x₀/sin φ₂ ≈ 2,83.10⁻² m ; Vm2 = Xm2ω₀ = 0,283 m.s⁻¹. c) E₀₂ = ½mv₀² + ½kx₀² = 4.10⁻³ J.
  d) E₂ = ½kXm2² = E₀₂ ⇒ Xm2 = √(2E₀₂/k) ≈ 2,83.10⁻² m ; E₀₂ = ½mVm2² ⇒ Vm2 = √(2E₀₂/m) = 2√2.10⁻¹ m.s⁻¹.
- 3°) E proportionnelle à Xm² : E₂/E₁ = Xm2²/Xm1² > 1 ⇒ E₂ > E₁. Remarque : E₂/E₁ = E₀₂/E₀₁ =
  1 + (1/ω₀²)(v₀/x₀)² > 1.

### Exercices à résoudre (p.160–166) — réponses du manuel p.317 quand elles existent

**Tests rapides des acquis**
- **1 Items vrai ou faux** (7 items, sans réponse imprimée) : 1. au passage par l'équilibre v = Xmω₀ ;
  2. éq. diff. d²x/dt² − ω₀²x = 0 [signe moins lu sur l'image] ; 3. oscillations non amorties dans l'air ;
  4. Ec max = ½kXm² ; 5. v(t) toujours en quadrature avance sur x(t) ; 6. les frottements influent sur
  l'amplitude ; 7. la pseudopériode augmente avec l'amortissement.
- **2 QCM** (9 questions, sans réponse imprimée) : 1. T₀ : dépend de Xm / proportionnelle à m / ne dépend
  pas des conditions initiales / temps entre deux passages successifs par l'équilibre ; 2. amplitude des
  oscillations non amorties : dépend de la vitesse initiale / ne dépend que de l'écart initial / augmente ;
  3. diminution d'amplitude due : aux transformations mutuelles / aux frottements / uniquement à la
  dissipation de Ec ; 4. vitesse au passage par l'équilibre : toujours maximale / toujours nulle /
  maximale ou minimale ; 5. k = 40 N.m⁻¹, m = 100 g : T₀ = 0,62 s / 3,10 s / 0,31 s ; 6. éq. diff. sans
  frottement : d²x/dt² + (m/k)x = 0 / d²x/dt² + (k/m)x = 0 / d²x/dt² + √(k/m) x = 0 ; 7. oscillations
  amorties : pseudopériode croissante / égale à T₀ / amplitude qui diminue en raison des frottements ;
  8. régime pseudopériodique lorsque : amortissement faible / abandon avec vitesse initiale / amplitude
  constante ; 9. amplitudes 4 cm puis 3,8 cm : amplitude constante / oscillations amorties / périodiques.

**Exercices d'application**
- **3** — pendule horizontal, m = 300 g, k = 10 N.m⁻¹, lancé depuis l'équilibre à t = 0 avec v₀ = 0,2 m.s⁻¹
  sens positif ; x(t) = Xm sin(ω₀t + φ) : déterminer Xm, ω₀, φ. Réponse : 3.46 cm, 5.77 rad.s⁻¹, 0 rad.
- **4** — m = 0,1 kg, k = 10 N.m⁻¹, banc à coussin d'air ; allongement 2 cm, abandon sans vitesse à t₀ = 0.
  1) éq. diff. ; 2) période ; 3) x(t). Réponse : 2°) 0.628 s.
- **5** — k = 25 N.m⁻¹, m = 0,5 kg, écart 2 cm, oscillations non amorties. 1) période propre ; 2) vitesse
  au passage par l'équilibre ; 3) évolution de l'amplitude si amorti. Réponse : 1°) 0.89 s, 2°) 0.14 m.s⁻¹,
  3°) Xm diminue.

**Exercices de synthèse**
- **6** (« D'après Bac. Juin 2005 (section sport) ») — corps (C) M = 0,2 kg, ressort k = 20 N.m⁻¹, tige
  horizontale (Fig.1) ; x = 0,1 sin(ω₀t + φ), ω₀ = √(k/M). 1°) a) T₀ ; b) N₀. 2°) frottements visqueux,
  Fig.2 (x(m) : départ 0,10, 1ᵉʳ maximum 0,06 ; graduations t « 0,8 ; 0,16 ; 0,24 ; 0,32 ») : a) pseudopériode
  T, comparer à T₀ ; b) E₀ et E₁ à t₀ = 0 et t₁ = T ; c) comparer. Réponse : 1°) a) 0.628 s, b) 1.59 Hz ;
  2°) a) 0.8 s, T > T₀ ; b) E₀ = 0.1 J, E₁ = 0.036 J. [? graduations incohérentes : « 0,8 » suivi de 0,16,
  0,24, 0,32 laisse lire 0,08 s, alors que la réponse donne T = 0,8 s > T₀.]
- **7** — d = 2 cm, abandon sans vitesse. 1°) sans frottement : nature des oscillations ; 2°) m = 360 g,
  T₀ = 0,60 s : raideur ; 3°) vitesse maximale au passage par la position de repos. (Pas de réponse
  imprimée.)
- **8** — enregistrements x(t) pour trois amortissements (lu sur l'image : courbe 1 et courbe 2 sans
  oscillation, partant de 0,04 m ; courbe 3 oscillante, maxima 0,03 / 0,02 / ≈0,013 / 0,01 m vers t = 1, 2,
  3, 4 s). 1°) lesquelles sont pseudopériodiques / apériodiques ; 2°) comment obtenir un régime apériodique
  à partir d'un régime pseudopériodique ; 3°) régime critique = « retour le moins lent à l'état de repos » :
  identifier la courbe. (Pas de réponse imprimée.)
- **9** — ressort l₀ = 10 cm, allongement/raccourcissement maximal 8,5 cm. 1°) vertical, m = 0,1 kg,
  l = 15 cm : raideur k ; 2°) sur banc à coussin d'air : pulsation, période, fréquence ; 3°) x₀ = 5,5 cm,
  expression de x(t) si a) abandon sans vitesse à t = 0 ; b) lâché sans vitesse et premier passage par
  l'équilibre à t = 0 ; c) lancé à t = 0 vers les élongations croissantes avec une vitesse telle qu'il subit
  ensuite son raccourcissement maximal. (Pas de réponse ; g non donné [?].)
- **10** — m = 292 g, k = 8 N.m⁻¹, tige horizontale sans frottement. 1°) éq. diff. ; 2°) expression
  littérale de T₀ ; Fig.1 x(mm)(t) : a) Xm, T₀ graphiquement, puis φ ; b) accord de T₀ avec m et k ; 3°) Fig.2
  a = f(x) (droite décroissante par l'origine, a en m.s⁻² de −0,8 à 0,8, x en mm de −20 à 20) : a) accord
  avec l'éq. diff. ; b) expression littérale du coefficient directeur, accord avec l'expérience. (Pas de
  réponse.) [? Fig.1 : graduations « 20, 10, 0, −20, −40 » asymétriques ; la courbe part du maximum et ses
  minima tombent sur la ligne « −40 » ; maxima à t = 0 ; ≈1,25 ; ≈2,5 s.]
- **11** (« D'après Bac. juin 2004 ») — ressort vertical k = 12 N.m⁻¹, solide M = 0,304 kg baignant dans un
  liquide visqueux, f⃗ = −hv⃗ ; stylet en A, cylindre enregistreur tournant (moteur) (Fig.1). 1°)
  enregistrement n°1, hₐ = 0,2 N.s.m⁻¹, G écarté de 4 cm vers le bas, libéré sans vitesse ; T ≈ T₀ :
  a) calculer T ; b) durée d'un tour du cylindre (l'enregistrement n°1, gradué T, 2T, 3T, = un tour).
  2°) h_b = 1, h_c = 4, h_d = 6 N.s.m⁻¹ → enregistrements n°2 (oscillant), n°3 et n°4 (non oscillants)
  (Fig.2) : remplir le tableau h / nature (pseudopériodique ou apériodique). (Pas de réponse.)
  [? formule imprimée « T ≈ T₀ = 2 √(M/k) » : π absent à l'impression.]
- **12** — graphe E (10⁻⁴ J) en fonction de x (cm) : Em horizontale à 2, Ep parabole de sommet 0 coupant Em en
  x = ±2 cm. 1°) variation de E, sa valeur, amorti ou non ; 2°) domaine d'élongation ; 3°) justifier la
  forme de Ep. (Pas de réponse.)
- **13 Etude de texte « Le tsunami »** (p.165–166) — séisme de Sumatra du 26 décembre 2004 ; oscillations de
  la Terre de fréquence pouvant atteindre 3 mHz, les plus graves entre 0,3 et 3 mHz ; en plein océan,
  oscillations horizontales de périodes de 10 min (1 km d'eau) à plus de 60 min (6 km) ; près des côtes la
  période diminue et l'amplitude augmente ; vague classique de période d'au plus une minute ; élévation du
  niveau pendant 5 à 30 minutes. Questions : 1°) relever les trois types d'oscillations libres ; 2°) a) ce
  qui montre que les oscillations de la Terre sont libres ; b) périodes minimale et maximale ; c) quelle
  qualification pour ces périodes ; 3°) ce qui montre que le tsunami est oscillatoire ; 4°) justifier la
  durée de 5 à 30 min. (Pas de réponse.)

**En savoir plus (p.167)** — « Les oscillations libres de la Terre » (d'après M. Van Camp) : modes normaux
(fondamental, harmoniques) excités par les grands séismes ; périodes de quelques secondes à 54 min ; 20,5 min
↔ 0,001 Hz ; comparaison au « Do 256 Hertz » (18 octaves) et à une corde de guitare de 300 km ; forces de
rappel dues à l'élasticité. Pas de fiche technique dans ce chapitre.

### Bornes de scope

✅ **Inclus**
- Pendule élastique horizontal (banc / table à coussin d'air, cylindre sur tige) ; vertical seulement comme
  variante de mesure (Fig.3) et dans les exercices 9 et 11.
- Lecture d'un enregistrement x(t) : amplitude, période / pseudopériode, nature amortie ou non,
  identification des régimes pseudopériodique, apériodique, critique (qualitatif).
- Mesure de T₀ au chronomètre (durée de 10 oscillations) ou par enregistrement / acquisition informatique.
- Étude expérimentale des facteurs de T₀ (amplitude, m, k) par tableaux et graphes linéarisés T₀² = f(m),
  T₀² = f(1/k) ; T₀ = 2π√(m/k), N₀, ω₀ = √(k/m).
- Bilan des forces, T⃗ = −kx i⃗ (force de rappel), RFD / théorème du centre d'inertie, projection sur x′x ;
  équation d²x/dt² + ω₀²x = 0 ; vérification de la solution x = Xm sin(ω₀t + φ) ; détermination de Xm et φ
  par les conditions initiales (x₀, v₀ ; tg φ = x₀ω₀/v₀, signe de cos φ) ; v(t), Vm = Xmω₀.
- Énergies : Ec, Ep = ½kΔl² (= ½kx²), E = ½kXm² = ½mVm² ; expressions en cos 2(ω₀t + φ) et période T₀/2 ;
  dE/dt = 0 (conservatif) ; graphes E, Ec, Ep en fonction de t et de x ; méthode énergétique pour Xm et Vm.
- Frottement visqueux f⃗ = −hv⃗ ; équation m d²x/dt² + h dx/dt + kx = 0 ; dE/dt = −hv² < 0 ; T légèrement
  > T₀, écart croissant avec l'amortissement ; énergie aux instants 0 et T lue sur un enregistrement.
- Graphe a = f(x) (droite de pente −ω₀² — demandée en ex.10, non énoncée dans le cours).
- Analogie mécanique ↔ électrique (tableau p.155, RLC série du chapitre 3).

⛔ **Exclu** (absent du chapitre)
- Résolution de l'équation amortie (aucune solution explicite, ni forme exponentielle, ni décrément
  logarithmique, ni facteur de qualité, ni valeur critique de h, ni relation T–T₀ chiffrée).
- Frottements solides (non visqueux) ; pendule pesant / pendule simple ; pendule de torsion.
- Équilibre et équation du pendule élastique vertical (position d'équilibre décalée, poids) — non traités
  en cours (l'ex.9 1°) utilise seulement l'allongement statique).
- Oscillations forcées, résonance (chapitre suivant) ; entretien des oscillations.
- Représentation de Fresnel (le manuel écrit l'élongation sous la seule forme x = Xm sin(ω₀t + φ)).
- Énergie potentielle de pesanteur dans E.

### Lecture

- **Couche texte** : p.144–167 (24 pages) et réponses p.316–318 (Chapitre 5 sur p.317 ; p.316 = chap.1–4,
  p.318 = sites web, rien pour le chap.5).
- **Pages vues sur l'image** (r110) : 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157,
  158, 159, 160, 161, 162, 163, 164, 165, 166, 167 (24/24) ; zooms r250 : p.146 (Fig.2), p.152 (Fig.9–10),
  p.162 (Fig.2 ex.6, figure ex.8), p.163 (Fig.1 ex.10), p.164 (formule ex.11) ; p.317 (bloc Chapitre 5,
  r200). Total 25 pages distinctes vues sur l'image.
- **Écarts texte/image constatés** : ω₀ rendu « to » / « t0 », π rendu « / », φ perdu (« sin(2/To t+) »),
  signe « − » rendu « < » (p.153–154 : « < kx < h », « = < hv² »), fractions éclatées sur plusieurs lignes,
  vecteurs perdus (T⃗ = −kx i⃗ rendu « T = - kx. i »), formules des p.153 et 158 absentes du texte (P⃗ + R⃗ +
  T⃗ + f⃗ = ma⃗, T⃗ = −kxi⃗, f⃗ = −hv⃗), Ep = ½kΔl² rendu « ½k6l2 », signe « − » de Ep = ¼kXm²[1 − cos…]
  rendu « < » ; graphiques et leurs graduations absents (Fig.2, 4, 5, 7–12 ; figures des ex.6, 8, 10, 11,
  12) ; ordre des colonnes mélangé p.161–164 (questions 1)–3) de l'ex.4 lues sur l'image dans la colonne
  de droite).
- **Doutes [?]** :
  1. p.146 : légende de la Fig.2 imprimée « Fig.3 : Tracé de Um en fonction de f (URom) » (erreur de
     maquette) ; T₀ ≈ 0,44 s seulement déductible de la figure (1,1 s = 2,5 oscillations), non imprimé.
  2. p.147 : masse « 0,50 » kg dans la série 0,050…0,300 (vraisemblablement 0,250).
  3. p.152 : T₁ ≈ 0,45 s et T₂ ≈ 0,5 s déduits des repères 1,8 s et 2 s (4 pseudopériodes chacun), non
     imprimés.
  4. p.162 ex.6 Fig.2 : graduation « 0,8 » puis 0,16, 0,24, 0,32 ; la réponse p.317 donne T = 0,8 s (> T₀ =
     0,628 s) — incohérence d'échelle.
  5. p.163 ex.10 Fig.1 : graduations verticales 20, 10, 0, −20, −40 incohérentes (amplitude réelle
     ambiguë).
  6. p.164 ex.11 : « T ≈ T₀ = 2 √(M/k) », π manquant à l'impression.
  7. ex.9 : g non donné dans l'énoncé.
  8. Aucune réponse imprimée pour les tests 1–2 ni pour les exercices 7 à 13.

## 2.6 Chapitre 6 — Oscillations mécaniques forcées en régime sinusoïdal (manuel 223433, p.168–187)

**Partie** : « Evolution de systèmes » (bandeau de page). Titre de la page d'ouverture (p.169) :
« OSCILLATIONS FORCÉES D'UN PENDULE ÉLASTIQUE EN RÉGIME SINUSOÏDAL » (numéro 6). [Bandeau de la p.170
imprimé « Oscillations électriques forcées en régime sinusoïdal » : coquille, toutes les autres pages
portent « Oscillations mécaniques forcées en régime sinusoïdal ».]

**Page d'ouverture (p.169)** — trois photos légendées : « Les marées sont des oscillations périodiques.
À quoi sont-elles dues et en quoi diffèrent-elles des tsunamis? » ; « Le violoniste fait vibrer les cordes
de son instrument en les frottant avec l'archet pour produire un son avec des notes plus ou moins
hautes. » ; « Clarinettes "graves" offrant une musique très impressionnante ». Questions d'accroche :
« - Pourquoi ces formes particulières des instruments de musique comme le violon, le violoncelle, le
contre basse, la clarinette … ? - Dans certaines voitures, on entend parfois des bruits inconfortables de
la carrosserie. A quoi sont-ils dus et pourquoi à des vitesses bien déterminées et non pas à d'autres ?
- Pourquoi a-t-on interdit à un régiment de soldats de traverser un pont (même non suspendu) au pas
cadencé ? »

**Objectifs (p.168)** — « Distinguer, en régime mécanique forcé, entre l'excitateur et le résonateur. ·
Distinguer en mécanique, entre les oscillations libres et les oscillations forcées. · Mettre en évidence,
qualitativement, la résonance d'élongation d'un pendule élastique. · Etudier qualitativement l'influence
de l'amortissement sur la résonance d'élongation d'un pendule élastique. · Établir l'expression du
déphasage entre la force excitatrice F et l'élongation x du solide. · Distinguer une résonance aiguë d'une
résonance floue. · Utiliser l'analogie formelle électrique - mécanique pour : - écrire, en x ou en v,
l'équation différentitelle [sic] des oscillations mécaniques forcées en régime sinusoïdal, - écrire
l'expression de l'amplitude Xm des oscillations et celle de la vitesse maximale Vm d'un pendule élastique
en fonction de la fréquence N de l'excitateur, - caractériser la résonance d'élongation, - caractériser la
résonance de vitesse d'un pendule élastique, - exprimer la puissance mécanique moyenne d'un pendule
élastique. »

**Prérequis (p.168)** — SAVOIR : exprimer la période propre des oscillations libres d'un pendule élastique
en fonction de ses grandeurs caractéristiques ; écrire l'équation différentielle caractéristique des
oscillations forcées d'un oscillateur RLC série ; exprimer l'intensité maximale Im du courant oscillant
dans un circuit RLC série en fonction de la fréquence des excitations sinusoïdales ; exprimer la puissance
électrique moyenne absorbée par un oscillateur électrique. SAVOIR FAIRE : distinguer entre un excitateur
et un résonateur ; établir en i(t) ou en q(t) l'équation différentielle des oscillations forcées d'un
circuit RLC série en régime sinusoïdal ; déduire de l'expression de Im en régime sinusoïdal forcé celle de
la charge maximale Qm du condensateur du circuit RLC série ; faire l'analogie formelle entre un oscillateur
mécanique amorti et un circuit RLC série.

**Introduction (p.170)** — « Comme dans la nature, nombreux sont les domaines où les oscillations
mécaniques sont importantes. Lorsqu'elles sont recherchées, il faut penser à les entretenir. En fait, pour
éviter la diminution de leur amplitude due aux frottements inéluctables, on doit leur apporter de
l'énergie. Comme dans le cas des oscillations électriques, lorsque l'apport de l'énergie se produit
périodiquement avec un dispositif approprié appelé excitateur, les oscillations mécaniques entretenues
sont dites forcées. »

**Plan du chapitre** (titres numérotés du manuel) : 1. Production d'oscillations forcées (p.170–171) ·
2. Influence de la fréquence de l'excitateur sur l'amplitude des oscillations (p.172) · 3. Influence de
l'amortissement sur l'amplitude des oscillations (p.172–174) · 4. Étude théorique (p.174–176) : 4.1 Nature
et vitesse des oscillations ; 4.2 Amplitude des oscillations ; 4.3 Résonance d'élongation et résonance de
vitesse · 5. Puissance mécanique moyenne (p.177) · 6. Importance des oscillations mécaniques forcées et de
la résonance (p.177–179) : 1- Dans la nature : phénomène des marées ; 2- En acoustique ; 3- En industrie :
oscillations forcées dues aux trépidations du rotor d'une machine tournante (+ « Exemple d'illustration »,
gyroscope à lames) ; 4- Dans les ouvrages · L'essentiel (p.180) · Exercices : exercices résolus 1 et 2
(p.181–182) ; Exercices à résoudre (p.183–186) : Tests rapides des acquis (1 vrai/faux, 2 QCM), Exercices
d'application (3–5), Exercices de synthèse (6–9), Etude de texte (10) · En savoir plus (p.187).
**Pas de fiche technique** dans ce chapitre.

### Cours — Manipulations (activités)

**1. Production d'oscillations forcées** (p.170–171)
- **Manipulation** (p.170) — dispositif Fig.1 « Dispositif d'étude des oscillations forcées d'un pendule
  élastique horizontal » : pendule élastique horizontal (système solide-ressort), moteur (M), dispositif
  d'entraînement. Palet (S) de masse **m = 100 g** sur banc à coussin d'air, attaché en A à un ressort de
  raideur **k = 6.5 N.m⁻¹** ; l'autre extrémité B du ressort reliée, par un dispositif de guidage, à un
  excentrique solidaire du moteur de fréquence de rotation N réglable. Schéma (légendes) : excentrique,
  moteur (M), articulation, guide, tige, fil inextensible, B, ressort, A, solide (S), règle graduée, banc à
  coussin d'air, cylindre enregistreur. Stylet fixé sur (S) enregistrant l'élongation de G sur un papier
  enroulé sur un cylindre tournant à vitesse constante. Moteur à **N = 1.5 tr.s⁻¹** ; en régime permanent,
  enregistrement Fig.2 : sinusoïde x(cm) de crête ±3 cm, partant de 0 en croissant à t = 0, axe t(s) gradué
  0,5 et 1 (zéros vers 1/3 s, 2/3 s, 1 s, lus sur l'image ; pas de quadrillage).
- **Remarque** (p.171) : acquisition informatique possible via un montage potentiométrique (Fig.3 :
  solide (S) dont la tige plonge en M dans une cuve de « Solution aqueuse de sulfate de cuivre », point O
  = position de repos, pile, sortie « Vers un ordinateur ou un oscilloscope à mémoire ») ; « La tension U_OM
  est proportionnelle à l'abscisse x du point M ».
- **Questions** (p.171) : « 1°) Déterminer graphiquement la fréquence des oscillations du pendule
  élastique, la comparer à sa fréquence propre et à la fréquence de rotation du moteur. En déduire qu'il
  s'agit d'oscillations forcées. 2°) Déterminer l'expression de l'élongation x en fonction du temps. »
- **Interprétation** : le moteur entraîne B dans un mouvement rectiligne sinusoïdal de fréquence N ;
  « Ainsi, l'élongation du centre d'inertie G s'écrit : x = Xm sin (2πNt + φ). On dit alors que le pendule
  élastique effectue des oscillations forcées imposées par le moteur qui joue le rôle d'excitateur. »
- **Conclusion** (voir Encadrés) ; Remarque : « La dénomination résonateur sera justifiée plus loin. »

**2. Influence de la fréquence de l'excitateur sur l'amplitude** (p.172)
- **Manipulation** : dispositif Fig.1 sans enregistrement (Fig.4 « Palet (S) sans le système
  d'enregistement » [sic]) ; N part de la plus petite valeur possible : amplitude très faible ; N croissant :
  Xm de plus en plus grande ; près d'une valeur légèrement inférieure à No, Xm augmente beaucoup plus ;
  au-delà, Xm rechute puis décroît modérément. (Aucune valeur numérique, aucun tableau ni courbe Xm(N).)
- **Questions** : « 1°) Est-ce que les observations et les constatations faites ne sont pas semblables à
  des constatations faites dans une étude antérieure ? Dans l'affirmative, rappeler cette étude ainsi que
  les constatations qui lui sont spécifiques. 2°) Justifier la qualification du pendule comme étant un
  résonateur. 3°) Comparer la valeur de la fréquence à laquelle se produit le phénomène de résonance
  d'élongation avec la valeur de la fréquence propre du résonateur. »
- **Conclusion** : voir Encadrés (résonance d'élongation, Nr).

**3. Influence de l'amortissement** (p.172–174)
- **Expérience 1** : voile (plaque rectangulaire perpendiculaire à l'axe du banc) fixée sur le palet
  (Fig.5 « Palet (S) avec voile ») : mêmes constatations, amplitude à la résonance inférieure au cas sans
  voile, Nr encore plus petite (toujours légèrement < No).
- **Expérience 2** : plaque un peu plus grande : résonance avec amplitude beaucoup moins remarquable, Nr
  plus petite que dans le deuxième cas, toujours légèrement < No.
- **Expérience 3** : plaque de grandes dimensions : oscillations à peine remarquables, amplitude
  pratiquement constante (ou diminuant légèrement) quand la fréquence augmente.
- **Remarque** : réalisable avec un pendule élastique vertical, amortissement dans l'air ou dans un liquide,
  avec ou sans rondelle (Fig.6 « Pendule élastique vertical » : ressort vertical, règle, masse plongeant
  dans une éprouvette, moteur en bas relié par un fil passant sur une poulie).
- **Questions** : « 1°) En s'aidant des résultats de l'étude expérimentale faite, comparer l'influence de
  l'amortissement sur les oscillations sinusoïdales forcées d'un pendule élastique avec l'influence du
  facteur de même type sur le circuit RLC série en régime sinusoïdal forcé (chapitre 4). 2°) Dans le cas de
  l'expérience 3, le régime forcé du pendule élastique est dit linéaire. Justifier cette qualification. »
- **Interprétation** (p.173–174) : amortissement très faible (sans voile) → amplitude Xmo à la résonance
  très grande, diminuant considérablement dès que N s'écarte de Nr : résonance « aiguë » ; amortissement
  moyen (« plaque de petites dimensions ») → Xm1 < Xmo, diminution modérée avec l'écart à Nr1 ;
  amortissement important (« plaque de dimensions moyennes comme celle de l'expérience 2 ») → amplitude
  moins sensible à la fréquence : résonance « floue » ; amortissement très important → très petite
  amplitude pratiquement indépendante de N, pas de résonance : régime « linéaire ». [? Le manuel associe
  l'« amortissement moyen » à une « plaque de petites dimensions » et l'« amortissement important » à
  l'expérience 2 ; correspondance exp. 1/2/3 ↔ moyen/important/très important, à suivre telle quelle.]
- **Conclusion** : voir Encadrés.

**4. Étude théorique** (p.174–176) — repère galiléen (O, i⃗) lié au laboratoire (Fig.7 « Choix du repère
d'étude » : palet G, forces P⃗, R⃗, T⃗, f⃗, F⃗ ; axe x) ; O position de repos de G, x élongation entre +Xm et
−Xm. « Cependant, pour développer cette étude, on ne va pas procéder par l'application de la RFD. On va
plutôt mettre à profit l'analogie formelle mécanique-électrique, dégagée à la fin de l'étude des
oscillations libres (page 149). »
- **4.1 Nature et vitesse** (p.174–175) : à F = Fm sin2πNt on associe u = Um sin2πNt ; tableau d'analogie
  (voir Encadrés) ; circuit analogue Fig.8 « Circuit RLC série soumis à la tension excitatrice
  u = Um sinωt » (GBF, K, Ro, bobine (L, r), C ; points A, B, D, E). Équation électrique → équation en x →
  solution particulière x = Xm sin(ωt + φx) → v = ωXm sin(ωt + φx + π/2).
  **Questions** (p.175) : « Refaire la même étude qui consiste en la détermination de x(t) et de v(t) en
  procédant comme suit : 1°) a - Par recours à l'analogie formelle électrique-mécanique, écrire, en la
  vitesse v du centre d'inertie G du palet, l'équation différentielle régissant les oscillations forcées du
  pendule élastique. b - Ecrire l'expression de la vitesse instantanée v(t). 2°) De l'expression de v(t)
  déduire celle de x(t). »
- **4.2 Amplitude** (p.175) : Xm par analogie avec Qm (voir Encadrés). **Questions** (p.176) : « Par
  analogie avec l'expression de la valeur maximale Im de l'intensité du courant oscillant dans un circuit
  RLC série en régime forcé sinusoïdal, montrer qu'en régime mécanique semblable, la valeur maximale Vm de
  la vitesse du centre d'inertie G du palet du pendule élastique s'écrit : Vm = Fm / √(h²ω² + (mω − k/ω)²) »
  [sic : « h²ω² » sous le radical dans cette question ; l'Essentiel et l'exercice 9 écrivent « h² »].
- **4.3 Résonances** (p.176) : tableaux d'analogie (voir Encadrés). **Questions** : « 1°) Montrer que la
  résonance d'élongation devient impossible pour les valeurs de h supérieures à une valeur limite
  ho = mωo√2. 2°) Montrer que si h était nul, la résonance aurait lieu pour ω = ωo avec une amplitude Xm qui
  tendrait vers l'infini. Commenter ce cas idéal. »

**5. Puissance mécanique moyenne** (p.177) — tableau d'analogie (voir Encadrés).

**6. Importance des oscillations forcées et de la résonance** (p.177–179) — texte documentaire :
- *Marées* (Fig.9) : oscillations forcées de grandes quantités d'eau, excitateurs la lune et le soleil ;
  période propre de la baie proche de la période des marées (« de l'ordre de 12 heures ») → résonance ;
  marées hautes « de dix mètres et même plus » à l'entrée d'une baie contre « de l'ordre de 30 cm » en
  haute mer ; centrale marémotrice.
- *Acoustique* : caisses des instruments à cordes et l'air contenu entrent en résonance (renforcement des
  notes) ; la caisse = oscillateur de période propre dépendant de sa forme ; membrane de haut-parleur :
  vibrations forcées devant correspondre à une résonance « floue ».
- *Industrie* : partie tournante mal équilibrée = excitateur par trépidations ; ruptures possibles quand
  la fréquence de rotation avoisine une fréquence propre ; bruits de carrosserie (amplitude plus grande si
  pièces desserrées, amortissement plus faible) ; masselotte de plomb sur la jante ; paniers de machines à
  laver suspendus à des amortisseurs ; supports amortisseurs des machines-outils. *Exemple d'illustration* :
  gyroscope à lames (Fig.10) — stator à lamelles d'acier d'inégales longueurs, rotor = disque percé d'un
  petit trou près du pourtour (centre d'inertie hors de l'axe → trépidations), lancé par une ficelle ; en
  ralentissant, les lamelles entrent en résonance une à une, la plus courte d'abord (fréquence propre la
  plus grande).
- *Ouvrages* : ponts suspendus comme résonateurs (tourbillons d'une tornade) ; renvoi à « En savoir plus ».

### Encadrés, lois et relations (VERBATIM, vérifiés sur l'image de leur page)

> **Conclusion 1** (p.171) — « Etant soumis à des excitations périodiques, le pendule élastique effectue
> des oscillations forcées sinusoïdales de période égale à celle de l'excitateur. L'oscillateur qu'est le
> pendule élastique est appelé résonateur. »

> **Conclusion 2** (p.172) — « En régime sinusoïdal forcé, l'amplitude Xm des oscillations d'un pendule
> élastique dépend de la fréquence N des excitations. Elle atteint sa valeur la plus élevée à une fréquence
> Nr légèrement inférieure à la fréquence propre No du pendule : on dit qu'il y a résonance d'élongation.
> Nr est appelée fréquence de résonance. »

> **Conclusion 3** (p.174) — « Pour une fréquence d'excitation donnée, l'amplitude des oscillations forcées
> d'un pendule élastique est d'autant plus petite que l'amortissement est plus important. Avec un faible
> amortissement, la résonance est aiguë. Avec un amortissement important, la résonance est floue. La
> fréquence de résonance est inférieure à la fréquence propre du pendule élastique. Cependant, l'écart entre
> ces fréquences est d'autant plus remarquable que l'amortissement est plus important. »

> **Tableau d'analogie** (p.174) — Oscillateur électrique ↔ Oscillateur mécanique : q ↔ x ; i = dq/dt ↔
> v = dx/dt ; l ↔ m ; r ↔ h ; 1/C ↔ k ; u = Um sin2πNt ↔ F = Fm sin2πNt. [Imprimé « l » et « r » minuscules
> dans le tableau ; le texte voisin écrit L et R.]

> **Équations** (p.175) — électrique : « L d²q/dt² + R dq/dt + q/C = Um sin ωt, avec ω = 2πN » ; « ce qui
> donne par analogie, comme équation différentielle en x : m d²x/dt² + h dx/dt + kx = Fm sin ωt. » ;
> « Une telle équation différentielle admet comme solution particulière : x = xm sin(ωt + φx), ce qui
> explique les oscillations sinusoïdales de (S) à la fréquence N de l'excitateur, en régime permanent. » ;
> « v = ωXm sin(ωt + φx + π/2) » ; « v = Vm sin(ωt + φv), avec Vm = ω.Xm et φv = φx + π/2 rad. »

> **Conclusion 4.1** (p.175) — « Etant régies par l'équation différentielle :
> m d²x/dt² + h dx/dt + kx = Fm sinωt ⇔ m dv/dt + hv + k ∫vdt = Fm sinωt, les oscillations forcées d'un
> pendule élastique évoluent sinusoïdalement au cours du temps à la pulsation ω de l'excitateur.
> x = Xm sin(ωt + φx) ⇔ v = Vm sin(ωt + φv), avec Vm = ωXm et φv = φx + π/2 rad. »

> **Amplitude** (p.175, Xm encadré) — « On a : Qm = Um / √(R²ω² + (Lω² − 1/C)²), d'où :
> Xm = Fm / √(h²ω² + (mω² − k)²) » ; « Donc, comme pour Qm, l'amplitude Xm dépend de la pulsation et, par
> suite, de la fréquence N de l'excitateur. » [Signe « = » après Qm absent à l'impression.]

> **Résonance d'élongation** (p.176, tableau) — Fréquence de résonance : résonance de charge
> Nr = √(No² − R²/(8π²L²)) ; résonance d'élongation Nr = √(No² − h²/(8π²m²)). Texte : « La résonance
> d'élongation se manifeste bien à une fréquence Nr de l'excitateur légèrement inférieure de la fréquence
> propre No du résonateur, et ce, à cause du terme h²/(8π²m²) dû au cœfficient de frottement non nul h. De
> plus, l'écart (No − Nr) augmente avec ce terme. D'autre part, l'amortissement influe sur l'amplitude des
> oscillations : plus h est grand, plus Xm est petite. »

> **Résonance de vitesse** (p.176, tableau) — résonance d'intensité : Nr = No, Im = Um/R ; résonance
> [de] vitesse : Nr = No, Vm = Fm/h (« Valeur maximale de la grandeur oscillante »).

> **Puissance moyenne** (p.177, tableau) — Puissance électrique moyenne ↔ Puissance mécanique moyenne :
> p = (UmIm/2) cosφ, avec φ = φi − φu ↔ p = (FmVm/2) cosφ, avec φ = φv − φF ; cosφ = R/Z ↔ cosφ = h/Z ;
> Um = ZIm ↔ « Um = ZVm » [sic, lire Fm = ZVm ; cf. ex. 9 Z = Fm/Vm] ; P = ½RIm² ↔ P = ½hVm².

> **L'essentiel** (p.180, VERBATIM) —
> « ▪ En régime forcé, le dispositif d'entretien des oscillations d'un pendule élastique constitue
> l'excitateur tandis que le pendule constitue le résonateur.
> ▪ La fréquence des oscillations forcées d'un pendule élastique est égale à celle de l'excitateur.
> ▪ En présence de frottements visqueux, les oscillations sinusoïdales forcées d'un pendule élastique sont
> régies par l'équation différentielle en x : [m d²/dt² + h dx/dt + kx = F] [sic, « x » manquant au premier
> terme], ce qui équivaut à l'équation en v : [m dv/dt + hv + k∫vdt = F] avec F = Fm sinωt, valeur algébrique
> de la force excitatrice.
> ▪ En régime sinusoïdal forcé, le résonateur oscille en retard de phase par rapport à l'excitateur avec une
> amplitude Xm qui dépend de la fréquence N de l'excitateur : [Xm = Fm / √(4h²π²N² + (k − 4mπ²N²)²)]
> ▪ De même, la vitesse maximale Vm = ωXm dépend de la fréquence N de l'oscillateur :
> [Vm = Fm / √(h² + (mω k/ω)²)] [sic, signe « − » entre mω et k/ω absent à l'impression]
> ▪ En régime sinusoïdal forcé la résonance d'élongation se produit à la fréquence :
> [Nr = √(No² − h²/(8π²L²))] [sic, « L² » imprimé pour m² ; cf. p.176]. Cependant, la résonance de vitesse se
> produit à la fréquence [Nr = No]
> ▪ La résonance est d'autant plus aiguë que l'amortissement est faible.
> ▪ Dans le cas d'un amortissement fort, la résonance est floue. Lorsque h dépasse la valeur limite
> [hl = mωo√2], la résonance devient impossible.
> ▪ En régime sinusoïdal forcé, la puissance mécanique moyenne est donnée par la relation : [P = ½hVm²] »
> (Formules encadrées en vert ; notées ici entre crochets.)

### Exercices résolus

- **Exercice résolu 1** (p.181–182) — ressort k = 40 N.m⁻¹, extrémité B reliée indirectement à un
  excentrique ; palet (S) m = 100 g en A, plaque rectangulaire fixée (frottements visqueux et faibles) ;
  banc à coussin d'air horizontal ; force excitatrice sinusoïdale Fm, ω = 2πN ; enregistrement x(mm) (crête
  ±6 mm, x = +6 mm à t = 0, quadrillage, axe gradué 0,5 et 1 s). 1°) rôles du moteur+excentrique et du
  système {palet–ressort} ; 2°) à N1 : a) N1 et Xm ; b) x(t) ; 3°) montrer qu'à une fréquence N2 > N1 le
  palet oscille de nouveau avec la même amplitude ; 4°) à N = No, Xm = 15 mm, calculer h ; Fm = 0,15 N.
  **Solution** : 1°) moteur+excentrique = excitateur, {palet–ressort} = résonateur ; 2°) a) T = 0.5 s,
  « N1 vaut 2 Hz », « Xm = 6 mm » ; b) à t = 0, x = Xm sinφx = Xm ⇒ φx = π/2 rad ; ω = 2πN = 4π rad.s⁻¹ ;
  « x(t) = 6.10⁻³ sin (4πt + π/2) » ; 3°) frottements faibles ⇒ résonance légèrement en dessous de No,
  « No = 1/2 √(k/m) » [sic, π absent au dénominateur] « soit numériquement : No = 3,18 Hz. Or, N1 < No. Donc,
  (S) oscillera de nouveau avec la même amplitude Xm = 6 mm à une fréquence N2 > No et par suite, supérieure
  à N1. » ; 4°) par analogie avec Qm : h²ω² = (Fm/Xm)² − (mω² − k)² ; « Autre méthode plus astucieuse : A
  N = N0, c'est la résonance de vitesse qui est caractérisée par Vm = Fm/h = 2πN0Xm, d'où : h = Fm/(2πNoXm).
  A.N. : h = 0,5 N.s.m⁻¹. »
- **Exercice résolu 2** (p.182) — voiture sur piste saharienne, vitesse constante, bosses espacées de
  d = 20 m ; m = 1000 kg (voiture + conducteur). 1°) voiture assimilée à un système {solide ; ressort}
  oscillant verticalement : montrer qu'il faut éviter une vitesse critique vc ; calculer vc pour
  k = 4.10⁴ N.m⁻¹ ; 2°) rôle des amortisseurs. **Solution** : T = d/v ; période propre « To = 2 √(m/k) »
  [sic, π absent] ; résonance pour T = To, v = vc : « d/vc = 2 √(m/k), d'où : vc = d/2 √(k/m) » [sic, π
  absent ; la valeur numérique correspond à d/(2π)·√(k/m)] ; « vc = 20,14 m.s⁻¹ ou vc = 72,5 km.h⁻¹ » ;
  2°) les amortisseurs absorbent une partie de l'énergie des oscillations, l'amplitude des secousses
  diminue → meilleure tenue de route, plus de sécurité.

### Exercices à résoudre (p.183–186) ; réponses du manuel p.317

**Tests rapides des acquis**
- **1 Vrai ou faux** (8 items, p.183) : 1- le ressort est l'excitateur, le solide le résonateur ; 2- la
  période des oscillations forcées est imposée par l'excitateur ; 3- en régime forcé le pendule peut osciller
  avec sa période propre ; 4- la résonance d'élongation a lieu chaque fois que N = fréquence propre ; 5- x
  toujours en retard de phase sur F ; 6- l'élongation n'est maximale qu'à la résonance ; 7- à la résonance
  d'élongation, Xm augmente avec l'amortissement ; 8- résonance d'autant plus aiguë que l'amortissement est
  faible. (Pas de réponse imprimée.)
- **2 QCM** (6 questions, une ou plusieurs justes, p.183) : 1- l'élongation est a- toujours en retard sur
  sa vitesse / b- toujours en retard sur F / c- alternativement en avance et en retard sur F ; 2- à la
  résonance d'élongation Xm est a- maximale seulement en valeur absolue / b- la plus élevée / c-
  indépendante de l'amortissement ; 3- à la résonance d'élongation la période du pendule a- n'est pas égale
  à celle de l'excitateur / b- ne dépend que de la période propre / c- dépend du coefficient de frottement ;
  4- Xm est a- d'autant plus grande que l'amortissement est plus important / b- d'autant plus grande que N
  est proche de la fréquence propre / c- d'autant plus petite que la masse est grande ; 5- la résonance
  d'élongation a- n'est possible que si la période propre est très petite / b- peut être obtenue avec
  n'importe quel h / c- est d'autant plus aiguë que l'amortissement est faible ; 6- d'après l'analogie a-
  on peut définir l'impédance mécanique / b- à la résonance d'intensité correspond une résonance
  d'élongation mécanique / c- la puissance mécanique moyenne est constante à la résonance d'élongation.
  (Pas de réponse imprimée.)

**Exercices d'application**
- **3** (p.184) : ressort k = 50 N.m⁻¹, m = 100 g, pendule horizontal excité. 1°) excitateur/résonateur ;
  2°) To ; 3°) risque si N proche de la fréquence propre. — Réponse p.317 : « 2°) To = 0,28 s ; 3) Risque
  de rupture ».
- **4** (p.184) : m = 200 g, k = 5 N.m⁻¹ ; x = 0,025 sinπ(1,2.t + 0,75). 1°) Xm, φx, N ; 2°) a) No ; b)
  comparer N à No, oscillations forcées ? fréquence de l'excitateur. — Pas de réponse imprimée.
- **5** (p.184) : bosses espacées de d = 60 cm, voiture à v constante. 1°) période de passage d'une bosse à
  la suivante, fréquence ; 2°) a) excitateur/résonateur ; b) No = 5 Hz : montrer l'existence d'une vitesse
  vo de résonance (fréquence de résonance admise = fréquence propre). — Réponse : « 1°) T = d/v ; N = v/d
  2°) b) vo = 3 m.s⁻¹ ».

**Exercices de synthèse**
- **6** (p.184–185) : (S) masse m, ressort k, frottement f⃗ = −hv⃗, force F(t) = Fmax sin(2πNt + φF) i⃗.
  1°) Xm(Fm, k, h) par analogie ; 2°) enregistrement x(t) = Xm sin(2πNt + φx), x(cm) crête ±5, x = +5 à
  t = 0, « T = 0,14 π (s) » ; a) deux oscillations = un tour du cylindre : tours par minute ; Xm, N, φx ;
  b) m = 98 g, k = 20 N.m⁻¹ : montrer résonance de vitesse ; c) en déduire m d²x/dt² + kx = 0 ; d) Fm, φF,
  puissance moyenne, h = 1,8 kg.s⁻¹. — Réponse : « 2°) a) 68,2 tr.min⁻¹ ; 5 cm ; 2.27 Hz ; π/2 rad b)
  To = T, résonance de vitesse ; d) Fm = 1,29 N ; φF = 0 rad ; P = 0,46 W ».
- **7** (p.185) : m = 51 g sur banc à coussin d'air, extrémité du ressort en translation sinusoïdale
  (disque + moteur de fréquence N) ; à 1,25 tr.s⁻¹ amplitude maximale 4,8 cm. 1°) proposer un montage
  d'enregistrement ; 2°) excitateur/résonateur ; 3°) a) période ; b) raideur approchée ; 4°) palette dans
  l'eau : amplitude 2,4 cm, a) interpréter, b) avec de l'huile ? ; 5°) Nr : a) phénomène ; b) période et
  amplitude dépendent-elles du liquide ? — Réponse : « 3) a) 0,8 s, b) 3,14 N.m⁻¹ ».
- **8** (p.185–186) : pendule {m, k} horizontal excité par moteur + excentrique. 1°) type d'oscillations,
  période ; 2°) To = 0,46 s : phénomène si T voisine de 0,46 s ; 3°) T = To, amplitude 4 cm : a) Vm ; b) h ;
  Fm = 0,25 N. — Pas de réponse imprimée.
- **9** (p.186) : (S) m, ressort k, f⃗ = −hv⃗, F = Fm sinωt. 1°) équation différentielle par analogie ;
  2°) par la construction de Fresnel analogue au RLC : montrer « Z = Fm/Vm = √(h² + (mω − k/ω)²) » et
  « tgφ = (mω − k/ω)/h » (déphasage entre F et v) ; 3°) v(t, Fm, Z, φ) ; 4°) x(t) ; 5°) ω de résonance de
  vitesse et déphasage v/F alors ; 6°) montrer que Xm est maximale quand « Y = [m²ω⁴ + (h² − 2mk)ω² + k²] »
  est minimale ; ωr ; vérifier ωr < ωo ; existence d'un h au-delà duquel plus de résonance d'élongation.
  — Pas de réponse imprimée.

**Etude de texte**
- **10** (p.186) : « le salaire de la peur » (H.-G. Clouzot) : camion de nitroglycérine sur « tôle
  ondulée ». 1°) phénomène ; 2°) m = 10 tonnes, suspensions affaissées de 1,2 mm sous une charge de
  6,5 tonnes : a) raideur équivalente ; b) période et fréquence ; 3°) bosses espacées de d = 0,70 m :
  vitesse la plus critique ; 4°) l'affirmation (rouler très lentement ou très vite) est-elle justifiée ?
  — Pas de réponse imprimée.

**En savoir plus** (p.187) — « Dangers de la résonance » : suspension de voiture modélisée par ressort +
masse ; pistes sahariennes ondulées, amortisseurs à huile (à gaz sur les motos) ; Tacoma Narrow Bridge
(Puget Sound, novembre 1940, cinq mois après ouverture, rafales périodiques) ; pont suspendu d'Angers sur
la Maine (16 avril 1850, troupe au pas cadencé) ; vérins amortisseurs des tabliers ; tour Taipei 101 (2004,
508 m, 101 étages, boule d'acier de 800 tonnes entre les 88ᵉ et 92ᵉ étages). Photos du pont de Tacoma
avant/après rupture. **Fiche technique** : aucune dans ce chapitre.

### Bornes de scope

✅ **Inclus**
- Vocabulaire : excitateur / résonateur ; oscillations libres vs forcées ; régime permanent ; résonance
  d'élongation, fréquence de résonance Nr ; résonance de vitesse ; résonance aiguë / floue ; régime forcé
  « linéaire » (amortissement très important, pas de résonance).
- Expérimental qualitatif : pendule élastique horizontal sur banc à coussin d'air entraîné par moteur +
  excentrique (ou pendule vertical, amortissement par voile/plaque, liquide, rondelle) ; lecture d'un
  enregistrement x(t) (période, fréquence, amplitude, phase initiale) ; montage potentiométrique cité.
- Fréquence des oscillations forcées = fréquence de l'excitateur ; x = Xm sin(ωt + φx), v = Vm sin(ωt + φv),
  Vm = ωXm, φv = φx + π/2.
- Équations différentielles en x et en v obtenues **par analogie formelle électrique-mécanique** (q↔x,
  i↔v, L↔m, R↔h, 1/C↔k, u↔F) — pas par la RFD.
- Xm = Fm/√(h²ω² + (mω² − k)²) (et sa forme en N), Vm = Fm/√(h² + (mω − k/ω)²), impédance mécanique
  Z = Fm/Vm, tgφ = (mω − k/ω)/h (ex. 9), cosφ = h/Z.
- Résonance d'élongation : Nr = √(No² − h²/(8π²m²)) < No ; écart No − Nr croît avec h ; Xm décroît quand h
  croît ; limite h = mωo√2 au-delà de laquelle pas de résonance ; cas idéal h = 0 (Xm → ∞ à ω = ωo).
- Résonance de vitesse : Nr = No, Vm = Fm/h ; déphasage entre v et F demandé à l'ex. 9, 5° ; calcul de h par
  h = Fm/(2πNoXm).
- Puissance mécanique moyenne P = (FmVm/2)cosφ = ½hVm².
- Calcul de No = (1/2π)√(k/m), To = 2π√(m/k) ; vitesse critique sur bosses : T = d/v, résonance si T = To.
- Applications documentaires : marées, caisses de résonance, haut-parleur (résonance floue), machines
  tournantes (masselotte, amortisseurs), gyroscope à lames, ponts (Tacoma, Angers), Taipei 101.

⛔ **Exclu / non traité dans le chapitre**
- Établissement des équations par la RFD (explicitement écarté au §4) ; résolution générale de l'équation
  différentielle (régime transitoire) ; seule la solution particulière sinusoïdale est donnée.
- Construction de Fresnel mécanique en cours : n'apparaît **que** dans l'exercice 9 (par analogie avec le
  RLC) ; aucune construction tracée dans le cours.
- Démonstration de la formule de Nr et de la limite hl : laissées en « Questions » (et ex. 9, 6°) via
  minimisation de Y ; aucun calcul de dérivée dans le cours.
- Expression explicite du déphasage φx − φF (tg en fonction de x) : annoncée dans les Objectifs mais
  **non écrite** dans le cours ; seul le « retard de phase » de l'élongation sur l'excitateur est affirmé
  (Essentiel) et tgφ entre F et v figure à l'exercice 9. [?]
- Facteur de qualité / bande passante mécanique : absents (aucune mention).
- Courbes de résonance Xm(N) tracées ou tableaux de mesures : absents (descriptions qualitatives seulement).
- Énergie mécanique de l'oscillateur forcé, oscillateurs couplés, résonance d'autres systèmes (pendule
  pesant, torsion) : absents.
- Appareillage : seuls banc à coussin d'air, moteur à excentrique, stylet + cylindre enregistreur,
  montage potentiométrique (sulfate de cuivre), ordinateur / oscilloscope à mémoire ; pas de capteur
  détaillé ni de logiciel nommé.

### Lecture

- **Couche texte** : p.168–187 (20 pages) et p.316–318 ; la p.316 ne contient aucune réponse du chapitre 6
  (chapitres 1–4), la p.318 est une liste de sites web (sans réponse) ; les réponses du chapitre 6 sont en
  p.317.
- **Lues sur l'image** (21 pages) : p.168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
  181, 182, 183, 184, 185, 186, 187, 317 (110 dpi ; p.175, 176, 177, 180, 182, 186 relues à 170 dpi ;
  Fig.2 p.170 et graphe de l'ex. 6 p.185 recadrés à 250 dpi).
- **Sondage / écarts texte↔image** constatés (pages les plus denses : 175, 176, 177, 180, 182, 186) :
  p.175 fractions et dérivées éclatées (d²q/dt², Xm illisible : « h22 + (m2 k)2 ») ; p.176 Vm et Nr
  illisibles (« No2 8 2L2 », π perdu) et h_o = mωo√2 rendu « mo 2 » ; p.177 tableau de puissance déstructuré
  (indices φi, φu, φv, φF éparpillés) ; p.180 formules encadrées Xm(N), Vm, P **absentes** de la couche
  texte, hl absent ; p.182 π et racines perdus (« No = 1 k, 2 m », vc) ; p.186 Z et tgφ illisibles, flèches
  de vecteurs déplacées ; p.184 « F(t) = Fmax sin(2Nt + F) » (π, φ perdus) ; p.317 l'image confirme la
  ventilation des réponses ch.6 (« 7. 3) a) 0,8 s ») ; p.170 Fig.2 (amplitude 3 cm, départ à 0) non
  exploitable en texte.
- **Doutes / coquilles signalées [?]** : bandeau p.170 « électriques » ; tableau p.174 « l », « r »
  minuscules ; p.175 « = » manquant après Qm et « x = xm » (minuscule) ; p.176 question Vm avec « h²ω² »
  (vs « h² » ailleurs) ; p.177 « Um = ZVm » côté mécanique ; Essentiel p.180 : « m d²/dt² » sans x, Vm sans
  signe « − », Nr avec « L² » au lieu de m², limite notée « hl » (« ho » en p.176) ; ex. résolus p.182 :
  π absent dans No, To et vc (valeurs numériques cohérentes avec 2π) ; correspondance amortissement
  moyen/important ↔ expériences 1/2 incohérente (p.173–174) ; objectif « déphasage entre F et x » non
  traité explicitement ; aucune réponse imprimée pour les tests 1–2 et les exercices 4, 8, 9, 10 ; la
  fréquence propre du pendule de la manipulation 1 (m = 100 g, k = 6.5 N.m⁻¹) n'est pas donnée par le
  manuel ; ex. 6 : réponse « φF = 0 rad » alors que φx = π/2 et φv = φx + π/2 = π, v et F en phase à la résonance de vitesse donneraient φF = π [? réponse du manuel à ne pas reprendre sans vérification].

## 2.7 Chapitre 7 — Ondes mécaniques progressives (manuel 223433, p.188–225)

**Ouverture de partie « ONDES ONDES ONDES » (p.188–189)** — photos légendées : houle et surfers ;
tsunami (« n'est perceptible qu'au niveau des côtes […] vagues d'un à plusieurs dizaines de mètres ») ;
spectacle de son et de lumière (« tous les deux, des phénomènes ondulatoires ») ; Grand Nuage de
Magellan (diffraction) ; cartographie sonore d'une ville. **Sommaire de la partie** (p.189, vu sur
l'image) : I. Ondes mécaniques progressives (1. Propagation d'un ébranlement ; 2. Propagation d'une
onde sinusoïdale entretenue) · II. Nature ondulatoire de la lumière (1. Diffraction mécanique et
lumineuse ; 2. Dispersion de la lumière) — la partie II est le chapitre 8, hors de cette section.

**Page d'ouverture du chapitre (p.191)** — « ONDES MECANIQUES PROGRESSIVES 7 ». Photo de vagues,
légende : « Les vagues constituent un exemple de propagation d'ondes dans un milieu élastique. »
Questions d'accroche : « ◆ D'où provient l'énergie des vagues ? ◆ Le déferlement des vagues
correspond-il à un déplacement de matière ou d'énergie ? ◆ Nos oreilles perçoivent des sons.
Qu'est-ce qui fait qu'ils nous parviennent et pourquoi les sons émis et ceux qu'on perçoit sont les
mêmes ? »

**Objectifs (p.190, verbatim)** — « ◆ Distinguer entre une onde transversale et une onde
longitudinale. ◆ Reconnaître que la propagation d'une onde est due à une propagation d'énergie sans
transport de matière. ◆ Réaliser une expérience illustrant la propagation d'une onde sinusoïdale dans
un milieu homogène et isotrope. ◆ Identifier dans un milieu de propagation donné, les propriétés dont
dépend la célérité d'une onde. ◆ Etablir l'équation horaire du mouvement d'un point donné du milieu de
propagation connaissant celle de la source d'onde progressive et représenter graphiquement le
diagramme du mouvement de ce point. ◆ Représenter graphiquement l'aspect à un instant donné, du milieu
(ou d'une coupe du milieu) de propagation d'une onde progressive. ◆ Reconnaître la double périodicité
d'une onde sinusoïdale. »

**Prérequis (p.190, lus sur l'image)** — SAVOIR : définir un phénomène périodique ; définir la période
T et la fréquence N d'un phénomène périodique ; écrire la relation N = 1/T ; définir une grandeur
sinusoïdale ; définir la pulsation et l'amplitude d'une grandeur sinusoïdale ; écrire la relation
T = 2π/ω (ou N = ω/2π). SAVOIR FAIRE : utiliser l'oscilloscope ; appliquer les relations N = 1/T et
T = 2π/ω (ou ω = 2πN) ; représenter graphiquement une grandeur sinusoïdale en fonction du temps ;
mesurer les durées et les vitesses à l'aide de photocapteurs.

**Plan du chapitre** (titres numérotés du corps) : introduction (caillou dans une nappe d'eau, p.192) ·
**1. Propagation d'un ébranlement** (1.1 milieu unidimentionnel [sic] ; 1.2 milieu bidimentionnel ;
1.3 milieu tridimentionnel ; 1.4 célérité d'un ébranlement) · **2. Propagation d'une onde sinusoïdale
entretenue** (2.1 généralités sur l'onde entretenue ; 2.2 onde progressive le long d'une corde
élastique tendue — étude expérimentale, étude théorique ; 2.3 onde sinusoïdale le long d'un ressort ;
2.4 onde sinusoïdale à la surface de l'eau ; 2.5 le son, exemple d'onde progressive à trois
dimensions) · L'essentiel (p.210) · Exercices : exercice résolu (p.211–213), Tests rapides des acquis
(ex. 1–2, p.214), Exercices d'application (ex. 3–6, p.215–216), Exercices de synthèse (ex. 7–16,
p.216–221) · Fiche technique n°1 (p.222) · Fiche technique n°2 (p.223) · En savoir plus (p.224–225).

### Cours — Activités / manipulations

**Introduction (p.192)** — « En jetant un caillou dans une nappe d'eau calme, on provoque une
déformation de courte durée à la surface d'impact. […] Comment peut-on expliquer l'élargissement
progressif de ces rides circulaires […] ? »

**1.1 Milieu unidimensionnel (p.192–193)**
- **Expérience 1** (p.192) : longue corde élastique tendue horizontalement sur le sol ; mouvement de
  va-et-vient rapide imprimé à l'extrémité O. Fig.1 : corde à t₀ = 0, t₁ > 0, t₂ > t₁, t₃ > t₂, la
  bosse se déplace vers la droite (« Chaque point de la corde se soulève verticlament » [sic]).
- **Expérience 2** (p.192–193) : premières spires non jointives d'un ressort tendu horizontalement,
  comprimées puis lâchées. Fig.2 : ressort aux dates 0, t₁, t₂ (zone comprimée qui avance ; repères a,
  P, b).
- Questions (p.193) : 1°) comparer direction de déplacement de l'ébranlement et des points de la corde ;
  2°) même comparaison pour le ressort.
- Interprétation : chaque point « reproduit le mouvement de l'extrémité O avec un certain retard » ;
  corde → ébranlement **transversal** ; ressort (élongation selon l'axe du ressort) → **longitudinal**.

**1.2 Milieu bidimensionnel (p.193–194)**
- **Manipulation** : goutte d'eau sur la surface d'une cuve à ondes → ride circulaire (Fig.3 : cercles
  centrés en S à t₁, t₂ > t₁, t₃ > t₂) ; morceau de liège en M : « petit déplacement vertical sur
  place, sans s'éloigner de sa position initiale ».
- Questions : 1°) transversal ou longitudinal ? 2°) dans combien de directions ? 3°) y a-t-il
  déplacement d'une quantité d'eau à partir de S ?
- Interprétation : propagation dans toutes les directions de la surface ; point repéré par (x, y) →
  ébranlement à deux dimensions ; tous les points d'une ride atteints au même instant ; « la
  propagation de ce dernier se fait avec une transmission d'énergie, sans déplacement de matière.
  C'est pour cette raison qu'il est impropre de parler de déplacement d'un ébranlement. »

**1.3 Milieu tridimensionnel (p.194)**
- Exemples : un acteur chante une note entendue au balcon, à l'avant de la scène, dans les coulisses ;
  poste radio sous une cloche où l'on fait le vide → son inaudible.
- Questions : 1°) l'ébranlement sonore est-il transversal ou longitudinal ? 2°) le son se propage-t-il
  dans le vide ?
- Interprétation : « Les vibrations longitudinales des molécules de gaz (l'air par exemple) permettent
  la transmission du son […]. Dans le vide, le son ne peut pas se propager. »

**1.4 Célérité d'un ébranlement (p.195–198)**
- **Manipulation — échelle de perroquet** (Fig.4 photo, Fig.5 schéma : fil de torsion vertical,
  barreaux horizontaux, deux capteurs devant deux barreaux distants de d, reliés à un « mesureur de
  vitesse ») : masselottes à 2 cm de l'axe ; barreau supérieur tourné d'un angle α puis abandonné.
  Tableau 1 : d (m) = 0,23 / 0,30 / 0,40 / 0,54 → v (m.s⁻¹) = 0,48 / 0,49 / 0,48 / 0,49.
  Angle α′ > α : valeurs « pratiquement les mêmes ». Masselottes déplacées (symétriques, inertie
  modifiée) : tableau 2 : d = 0,23 / 0,30 / 0,40 / 0,54 → v = 0,28 / 0,29 / 0,28 / 0,28.
- Questions (p.196) : 1°) montrer que la célérité est constante dans ces milieux homogènes ; 2°) la
  célérité dépend-elle a) de l'amplitude ; b) des caractéristiques du milieu ?
- Interprétation : célérité constante ; indépendante de l'amplitude ; dépendante de l'inertie.
- **Autres constatations** (p.197) : la célérité augmente avec la tension du fil de torsion ; la
  vitesse du son dépend de la compressibilité du milieu, « plus grande dans les solides que dans les
  liquides et les gaz » ; tableau des célérités (m.s⁻¹) : ébranlement à la surface de l'eau 0,3 ; le
  long d'une échelle de perroquet 1 ; le long d'une corde 10 ; sonore dans l'air à 20 °C 342 ; sonore
  dans l'eau à 20 °C 1500 ; sonore dans l'acier 5000 ; sismique 8000.
- **Remarque — tableau comparatif** (p.197–198) « Déplacement d'un mobile » / « Propagation d'un
  ébranlement » : trajectoire précise / toutes les directions à partir d'une source ; transport de
  matière / transport d'énergie ; ralenti par les frottements / « peut être amorti, mais cet
  amortissement porte davantage sur son amplitude que sur sa célérité » ; plus facile dans le vide que
  dans un gaz, impossible dans les solides / « ne se propage pas dans le vide. Il se propage plus vite
  dans les liquides que dans les gaz et fréquemment plus vite dans les solides que dans les liquides » ;
  vitesse dépendant des conditions initiales / célérité dépendant des propriétés du milieu.

**2.1 Généralités (p.198)** — texte : houles, vagues, son, tremblements de terre = émission régulière
d'ébranlements identiques. Définitions (voir Encadrés). Au laboratoire, milieux finis limités « par une
matière absorbante (coton, feutre, plaque métallique cintrée …) afin de pouvoir les assimiler à des
milieux ouverts ».

**2.2 Corde élastique tendue (p.199–205)**
- **Mise en évidence** (p.199, Fig.6 : lame vibrante – O – corde élastique – A – pelote de coton) :
  vibreur = lame d'acier excitée par un électro-aimant alimenté en tension alternative sinusoïdale ;
  corde vue comme une « bandelette rectangulaire floue de largeur double de l'amplitude de vibration de
  l'extrémité O » ; picotement au doigt. Questions : 1°) bandelette floue ? 2°) rôle de la pelote de
  coton ? 3°) justifier « onde transversale ».
- **Mouvement d'un point M — analyse optique** (p.199–200, Fig.7 : électro-aimant, lame vibrante,
  diaphragme au niveau de M, lentille L, source lumineuse S, miroir tournant, écran avec sinusoïde,
  extrémité fixe A). Questions : 1°) que représente la sinusoïde d'ombre ? 2°) comparer le mouvement
  d'un point au mouvement de O. Interprétation : chaque point (sauf A) reproduit le mouvement de O
  « avec la même amplitude et un certain retard ».
- **Aspect instantané — stroboscope** (p.200–202) : Te = p.T (p ∈ ℕ*) → sinusoïde immobile de période
  D (Fig.8) ; Te légèrement > p.T → mouvement apparent lent dans le sens réel ; Te légèrement < p.T →
  sens contraire. Questions : expliquer a) l'immobilité apparente ; b) le mouvement apparent.
  Interprétation : pendant Te chaque point fait p oscillations complètes ; « Tous les points
  équidistants de k.D (k ∈ ℕ*) ont le même état de mouvement » ; D = longueur d'onde λ ; Fig.9a/9b
  (déplacement apparent MM′, « Sens réel de la prorogation » [sic] / « Sens apparent »).
- **Étude théorique** (p.202–205) : repère (O, i⃗, j⃗), O = extrémité attachée au vibreur, point M
  d'abscisse x (Fig.10). Équation horaire, déphasage, points en phase, en quadrature, aspect de la
  corde, front d'onde (voir Encadrés).
  Question (p.204) : « Déterminer les abscisses des points de la corde vibrant en opposition de phase
  avec la source. » Question (p.204) : « Montrer que les points de la corde vibrant en quadrature
  retard de phase par rapport à la source sont définis par leur position de repos d'abscisse :
  x = (4k+1)λ/4, avec k ∈ ℕ. » Fig.11 : photo de la corde à un instant donné devant une règle.

**2.3 Ressort (p.205–206)** — ressort à spires non jointives tendu verticalement par un solide
suspendu ; extrémité supérieure S attachée à un vibreur (vibrations verticales sinusoïdales de période
T) ; partie inférieure plongée dans un récipient d'eau (Fig.12, point A). Lumière ordinaire : flou.
Stroboscope : Te = T → immobile, zones alternativement comprimées et dilatées ; Te légèrement > T →
progression lente de S vers A. Questions : 1°) but de l'immersion dans l'eau ? 2°) aspect en lumière
ordinaire ? 3°) observation pour a) Te = kT ; b) Te légèrement < ou > kT ? 4°) nature de l'onde ?
5°) les spires restent-elles équidistantes ? Interprétation : non-équidistance des spires ; onde
**longitudinale** ; si ys(t) = a sin(ωt), « en absence de tout amortissement : yM(t) = a sin(ωt − 2πx/λ) ».

**2.4 Surface de l'eau (p.207–208)** — vibreur à fourche à pointe unique, cuve à ondes, point S,
fréquence N ; stroboscope de fréquence Ne : Ne = N → crêtes et creux circulaires concentriques
immobiles (cercles brillants/sombres sur le verre dépoli, Fig.13 photo) ; Ne légèrement diminuée →
rides qui paraissent progresser en s'éloignant de la source. Questions : 1°) la célérité est-elle la
même dans toutes les directions ? 2°) montrer qualitativement que, frottement nul, l'amplitude diminue
avec la distance à S. Étude théorique : rides « superficielles, circulaires et transversales » ;
points à même distance r de S en phase et de même amplitude ; cercles lieux des points en phase
équidistants de λ (Fig.14). Remarque : dilution d'énergie ; réglette verticale → rides rectilignes
parallèles à la réglette, distantes de λ (Fig.15).

**2.5 Le son (p.208–209)** — haut-parleur alimenté par un GBF, microphone (M) très sensible, voies Y₁
et Y₂ d'un oscilloscope bicourbe (Fig.16a photo) ; (C₁) = vibrations de la membrane du HP, (C₂) = du
microphone, même fréquence N (Fig.16b : deux sinusoïdes décalées). En approchant/éloignant le micro :
amplitude qui augmente ou diminue, décalage horaire passant « régulièrement plusieurs fois de 0 à
T/2 » ; micro déplacé à distance r constante : (C₂) identique et stable. Questions : 1°) constatation
montrant que le son est une onde tridimensionnelle ? 2°) transversale ou longitudinale ? 3°) expliquer
les variations d'amplitude de C₂ ; 4°) longueur de déplacement du micro au bout de laquelle le
décalage varie de T/2 ?

### Encadrés, définitions et relations (VERBATIM, vérifiés sur l'image de leur page)

> **Ébranlement / milieu élastique** (p.192, texte du corps, non encadré) — « La déformation de courte durée, imposée par le
> caillou à une nappe d'eau calme est un ébranlement. […] On appelle milieu élastique, tout milieu qui
> reprend de lui-même sa forme initiale après avoir subi une déformation brève. »

> **Conclusion 1.1–1.3** (p.195, encadré) — « Un ébranlement est une déformation de courte durée
> imposée localement à un milieu élastique. Le milieu de propagation d'un ébranlement peut être
> unidimensionnel (corde élastique, ressort), bidimensionnel (surface d'un liquide) ou tridimensionnel
> (l'air ou tout autre fluide). Selon sa direction de propagation et celle du déplacement des points
> matériels du milieu de propagation, un ébranlement peut être transversal ou longitudinal. La
> propagation d'un ébranlement est due à une transmission d'énergie d'un point du milieu de propagation
> vers d'autres. »

> **Célérité** (p.195, texte du corps, non encadré) — « La propagation d'un ébranlement se fait avec une vitesse v appelée vitesse
> de propagation ou célérité de l'ébranlement. Du fait que cette propagation ne correspond pas à un
> déplacement de matière mais plutôt à un transport d'énergie, la célérité v correspond à une vitesse
> de propagation de l'énergie. »

> **Conclusion 1.4** (p.197, encadré) — « La célérité d'un ébranlement dépend de la nature du milieu
> matériel dans lequel il se propage et de ses propriétés. Ainsi, le long d'une corde élastique, la
> célérité d'un ébranlement est d'autant plus grande que la corde est plus tendue. Plus l'inertie d'un
> milieu de propagation est grande, plus la célérité de l'ébranlement est faible... »

> **Définition (onde)** (p.198, encadré vert) — « On appelle onde (du latin unda) le phénomène
> résultant de la propagation d'une succession d'ébranlements dans un milieu donné. »
> **Célérité d'une onde mécanique** — « […] l'onde est caractérisée par une célérité v (ou vitesse de
> propagation) qui dépend des propriétés du milieu élastique homogène. Plus précisément, la célérité
> d'une onde est celle des ébranlements qui la constituent. »
> **Onde transversale et onde longitudinale** — « Le caractère transversal ou longitudinal d'une onde
> est fonction de celui des ébranlements correspondants. […] »
> **Ondes progressives** — « Lorsque le milieu de propagation est ouvert, c'est-à-dire illimité, les
> ondes progressent en s'éloignant indéfiniment de la source. De telles ondes sont dites
> progressives. »

> **Conclusion (corde)** (p.200, encadré) — « Les vibrations imposées à l'extrémité d'une corde
> élastique tendue sont transmises aux différents points de celle-ci. Le phénomène qui en résulte
> constitue une onde transversale. Au cours de la propagation d'une onde transversale sinusoïdale le
> long d'une corde élastique, chacun des points de cette corde (à part l'extrémité fixe A) vibre
> sinusoïdalement avec la même amplitude que la source (en négligeant l'amortissement). »

> **Double périodicité** (p.202, encadré) — « La propagation d'une onde est caractérisée par deux
> périodicités à la fois : - une périodicité dans le temps appelée périodicité temporelle. La période T
> est celle de la source. - une périodicité dans l'espace, appelée périodicité spatiale. La période
> spatiale λ, contrairement à la période T, ne dépend pas seulement de la source mais dépend aussi du
> milieu de propagation. La période spatiale λ est la longueur d'onde, elle représente la distance
> parcourue par l'onde pendant une durée égale à la période temporelle T.
> **λ = v.T , soit λ = v/N**
> En effet, la période temporelle T de l'onde est la durée au bout de laquelle l'onde se propage d'une
> longueur λ telle que tous les points du milieu de propagation se retrouvent dans le même état
> vibratoire, d'où le nom de longueur d'onde. »

> **Équation horaire d'un point de la corde** (p.203) — « A tout instant t, l'onde […] impose au point
> M une élongation y(t) égale à l'élongation qu'a eue l'extrémité source S à l'instant (t − θ),
> l'amortissement étant supposé nul. La durée θ désigne le temps mis par l'onde pour se propager de S à
> M. yM(t) = ys(t − θ) or ys(t) = a sin(ωt + φs). Avec un choix convenable de l'origine des temps, on
> aura φs = 0. ys(t) = a sin(ωt), d'où yM(t) = a sin ω(t − θ). θ = x/v ; v : célérité de l'onde et
> ω = 2π/T ; T : période de l'onde. Ainsi : yM(t) = a sin[2π(t/T − x/(vT))]. Or : λ = v.T : Longueur
> d'onde, d'où : yM(t) = a sin[2π(t/T − x/λ)]. »

> **Conclusion** (p.203, encadré) — « Au cours de la propagation d'une onde sinusoïdale entretenue le
> long d'une corde élastique, tout point M de la corde, d'abscisse x par rapport à la source, vibre
> sinusoïdalement avec une période T égale à celle de la source S, mais avec une phase initiale dont la
> valeur est fonction de sa position sur la corde, au repos. »

> **Déphasage par rapport à la source** (p.203) — « Si la source commence à vibrer à t = 0 en allant
> dans le sens positif des élongations, on a : ys(t) = a sin(ωt). yM(t) = a sin(ωt − 2πx/λ). C'est de
> la forme yM(t) = a sin(ωt + φM) avec φM = − 2πx/λ. Le déphasage entre les élongations yM(t) et ys(t),
> noté Δφ, est (φM − φs) ; Δφ = − 2πx/λ. »
> **Remarque** — « Ce résultat reste valable dans le cas général où l'armortissement [sic] n'est pas
> négligeable et où la phase initiale n'est pas nulle. ys(t) = aO sin(ωt + φs) ;
> yM(t) = a sin(ωt + φs − 2πx/λ) ; avec a < aO. Ainsi, Δφ est une fonction de l'abscisse x du point M
> par rapport à la source. »

> **Points en concordance de phase avec la source** (p.204) — « ys(t)/as = yM(t)/a, soit :
> sin(ωt + φs) = sin(ωt − 2πx/λ + φs) ∀t, ce qui donne φs = φM + 2kπ ; avec φM = −2πx/λ + φs
> (k : entier), soit Δφ = − 2kπ, ce qui conduit à : x = kλ, où k est un entier positif. Soit ℓ la
> longueur de la corde au repos. On a : x < ℓ. Donc, k < ℓ/λ. Les points de la corde qui vibrent en
> phase avec la source sont situés au repos à des distances égales à un nombre entier de longueurs
> d'onde la source S. Leur nombre est limité par la longueur de la corde. »

> **Points en quadrature avance de phase avec la source** (p.204) — « Un point M de la corde vibre en
> quadrature avance de phase la source lorsqu'à tout instant t, son élongation est telle que :
> yS(t) = yM(t − T/4), soit : a sin(ωt + φs) = a sin[ω(t − T/4) + φM], ce qui donne
> φS = φM − π/2 + 2kπ, avec k un entier positif. D'où : Δφ = − (4k − 1)π/2, ce qui conduit à :
> x = (4k − 1)λ/4, avec k un entier positif. Les points de la corde qui vibrent en quadrature avance de
> phase par rapport à la source sont situés au repos à λ/4 ayant [sic, ?] les points qui vibrent en
> phase avec la source. »

> **Aspect de la corde à un instant t donné** (p.205) — « Pour un point M donné, à tout instant t :
> yM(t) = a sin(ωt − 2πx/λ) dans le cas où φs = 0, ce qui entraîne qu'à un instant t donné, on peut
> écrire : pour tout point M, yt(x) = a sin(2πx/λ − ωt + π). Ainsi, pour t donné, yt(x) est fonction
> sinusoïdale de x, de période λ et de phase initiale (− ωt + π). La courbe représentant yt(x) donne
> l'aspect de la corde à un instant t considéré (Fig.11). Elle est appelée par certains "sinusoïde des
> espaces". »
> **Remarque (front d'onde)** — « Si les vibrations de la source commencent à t = 0 et que l'instant t
> choisi est de l'ordre de quelques périodes seulement, il se peut qu'à cet instant l'onde n'a pas
> atteint encore l'autre extrémité de la corde. Il faut alors chercher la position xf du front d'onde.
> Pour ce, il suffit de calculer la distance parcourue par l'onde entre l'instant t = 0 et l'instant t
> choisi. xf = v.t, ce qui équivaut à : xf = n.λ, en posant n = t/T. »

> **Remarque (surface de l'eau)** (p.208) — « L'amplitude des ondes qui progressent à la surface de
> l'eau décroît en s'éloignant de la source même si l'amortissement est supposé nul. Cette décroissance
> est due au fait que l'énergie mécanique cédée à l'onde par la source de vibrations se répartit de
> proche en proche sur une quantité de liquide de plus en plus grande quand elle progresse à la surface
> de l'eau. C'est le phénomène de dilution d'énergie. »

> **Conclusion (son)** (p.209, encadré) — « Le son est de nature vibratoire. C'est une onde mécanique,
> appelée onde sonore et plus particulièrement acoustique lorsqu'elle est susceptible d'être perçue par
> l'oreille de l'homme. L'onde sonore émise par une source ponctuelle (approximation du haut-parleur)
> est une onde progressive sphérique mais qui s'atténue en s'éloignant de la source à cause de la
> dilution de l'énergie. »

> **L'essentiel** (p.210, verbatim) — « ■ On appelle onde, le phénomène résultant de la propagation
> d'une succession d'ébranlements dans un milieu donné. ■ Une onde est dite transversale si la
> direction des déformations auxquelles elle est due est perpendiculaire à la direction de sa
> propagation. ■ Une onde est dite longitudinale si la direction des déformations auxquelles elle est
> due est parallèle à la direction de sa propagation. ■ La propagation d'une onde correspond à un
> transport d'énergie sans déplacement de matière. ■ La célérité (ou vitesse de propagation) d'une onde
> dépend de la nature du milieu de propagation et de ses propriétés. ■ Toute onde se propageant dans un
> milieu ouvert est progressive. Elle est caractérisée par une double périodicité spatiale et
> temporelle. ■ La période temporelle T de l'onde est liée à la période spatiale λ par la relation :
> [λ = v.T], avec v la célérité de l'onde. »

### Exercice résolu (p.211–213)

**Énoncé** — Extrémité libre O d'une lame vibrant à N = 100 Hz ; corde élastique l = 0,6 m ; onde
progressive sinusoïdale transversale non amortie, a = 5 mm, phase initiale nulle, v = 12 m.s⁻¹.
1°) équation horaire de M au repos à x = 21 cm et comparaison avec la source ; 2°) diagrammes des
mouvements de la source et de M dans un même système d'axes ; 3°) lieu et nombre des points en
quadrature avance de phase ; 4°) aspect de la corde à t₁ = 3,25.10⁻² s, puis à t₂ = 3,75.10⁻² s.

**Solution** — 1°) yM(t) = y₀(t − θ), θ = x/v ; yM(t) = a sin(ωt − 2πx/λ), φ = −2πx/λ ; λ = v/N,
A.N. λ = 12 cm, φ = −7π/2 = (−4π + π/2) rad ; **yM(t) = 5.10⁻³ sin(200πt + π/2)** : même amplitude,
quadrature avance. 2°) M ne vibre qu'à partir de t₁ = θ ; θ = x/v, x = 7λ/4, θ = 7T/4 = 1,75 T ; pour
t < 7T/4, yM = 0 ; pour t > 7T/4, yM(t) = a sin(ωt + π/2) ; diagramme de M = translation de θ de celui
de la source (graphe : source en noir de 0 à 4T, M en rose à partir de 1,75 T). 3°) Δφ = −2πx/λ =
−(4k − 1)π/2 → **x = (4k − 1)λ/4** ; x ≤ l → k ≤ l/λ + 1/4 ; l/λ = 5 → k ≤ 5,25, k ∈ ℕ* → k ∈ {1, 2, 3,
4, 5} ; tableau x (cm) = 9 / 21 / 33 / 45 / 57 (M à 21 cm en fait partie). 4°) x₁ = v t₁ = λ t₁/T,
t₁/T = 3,25 → x₁ = 3,25 λ < l = 5λ : front d'onde x_f1 ; pour x > x_f1, y = 0 (brin F₁A au repos) ;
pour x < x_f1, y_t1(x) = a sin(ωt₁ − 2πx/λ), ωt₁ = 6,5π rad → **y_t1(x) = a cos(2πx/λ)** ; graphe
(p.213) de 0 à x_f1 = 3,25 λ, A à 5λ. Remarques : M (x = 1,75 λ) a bien y = 0 à t₁ = 3,25 T ; méthode
rapide : extrapoler la sinusoïde de période λ depuis le front jusqu'à la source. t₂ : (t₂ − t₁)/T = 1/2
→ l'onde progresse de λ/2 ; **x_f2 = x_f1 + λ/2** = 3,75 λ ; aspect à t₂ dessiné (trait plein) avec
celui de t₁ (pointillés).

### Exercices à résoudre (p.214–221) — réponses du manuel p.317

**Tests rapides des acquis**
- **1. Vrai ou faux** (10 items) : onde mécanique dans le vide ; ébranlement transporte de l'énergie ;
  célérité indépendante du milieu ; onde sonore dans le vide ; λ = distance parcourue pendant T ;
  propagation = déplacement de matière ; célérité constante en milieu homogène ; onde à la surface d'un
  liquide transversale ; onde sonore longitudinale ; mobile = matière / onde = énergie. (Pas de
  réponse p.317.)
- **2. QCM** : I. phénomène ondulatoire associé à un déplacement de matière / d'énergie / des deux ;
  II. vitesse de l'ébranlement (caillou) dépend de l'énergie initiale / la taille du caillou / la
  profondeur de l'eau ; III. corde OA, N = 100 Hz, stroboscope Ne = 49 Hz : sinusoïde fixe / lente de
  O vers A / lente de A vers O ; IV. N = 50 Hz, v = 0,25 m.s⁻¹, distance entre deux points en phase :
  5 / 10 / 15 mm. (Pas de réponse p.317.)

**Exercices d'application**
- **3** : y = a sin(100πt), v = 10 m.s⁻¹, amortissement nul. 1°) N et λ ; 2°) a) aspect à t₁ = 0,02 s et
  t₂ = 0,05 s (S part dans le sens positif à t = 0) ; b) état vibratoire de M₁ (d₁ = 10 cm) et M₂
  (d₂ = 40 cm) ; 3°) aspect sous stroboscope Ne = 25, 49, 51 Hz. — Rép. : N = 50 Hz, λ = 0,2 m ; M₁
  opposition, M₂ en phase ; 25 Hz immobilité, 49 Hz ralenti sens réel, 51 Hz ralenti sens inverse.
- **4** : N = 50 Hz, a = 0,5 cm, lame part de l'équilibre vers le haut ; v = 1 m.s⁻¹, pas de réflexion.
  1°) équation de S ; 2°) a) équation de M à d ; b) d = 3 cm, comparer ; 3°) courbes yS(t), yM(t) ;
  4°) aspect à t₁ = 0,03 s et t₂ = 0,035 s. — Rép. : yS = 5.10⁻³ sin100πt ; yM = 5.10⁻³ sin(100πt −
  2πd/λ) ; d = 3 cm : yM = 5.10⁻³ sin(100πt − π).
- **5** : N = 100 Hz, a = 5 mm, corde très longue ; lame part de l'équilibre sens positif ; à
  t = 6,5.10⁻² s, M (x = 32,5 cm) entre en vibration. 1°) a) v ; b) λ ; 2°) a) équation de M ;
  b) graphe de 0 à 0,1 s ; c) instants d'élongation maximale, premier instant t₀. — Rép. : v = 5 m.s⁻¹ ;
  λ = 5.10⁻² m ; yM = 2.10⁻³ sin(200πt − π) [amplitude imprimée 2.10⁻³, cf. doutes] ; t = 6,75 T + kT.
- **6** : N = 50 Hz, source S, t₀ = 0, surface de l'eau ; coupe à t₁ (figure : sinusoïde de A à B,
  S au milieu, yS(t₁) = 0) ; AB = 3,0 cm, amplitude 4 mm. 1°) λ ; 2°) v ; 3°) t₁ ; 4°) ys(t) ; 5°) nombre
  de points en opposition de phase avec S à t₁, schéma ; 6°) coupe à t₂ = 6,25.10⁻² s. — Rép. :
  λ = 5.10⁻³ m ; v = 0,25 m.s⁻¹ ; t₁ = 6.10⁻² s ; yS = 4.10⁻³ sin(100πt + π) ; cercles de rayons λ/2,
  3λ/2, 5λ/2.

**Exercices de synthèse**
- **7** : cuve à ondes, source ponctuelle en O (amplitude a, fréquence N), bords absorbants, pas
  d'amortissement ; Fig.1 photo de rides, A et B sur deux crêtes, d = 24 mm ; Fig.2 : yM(t) d'un point
  M à d′ de O (échelles 2.10⁻³ m, 5.10⁻³ s). 1°) a) comment voir les rides immobiles ; b) λ ; 2°) a) yM(t) ;
  b) v ; c) yO(t) ; 3°) coupe selon x′x à t₀ = 0,045 s ; 4°) points en phase avec la source à t₀. — Rép. :
  λ = 8.10⁻³ m ; yM = 2.10⁻³ sin(100πt) ; v = 0,4 m.s⁻¹ ; yO = 2.10⁻³ sin(100πt + π) ; deux cercles de
  rayons λ et 2λ.
- **8** : lame en S, corde sur poulie + solide, dispositif absorbant ; ys(t) = a sin(ωt + φ), a = 3 mm,
  démarrage t₀ = 0. 1°) a) éclairage continu ; b) stroboscope Ne légèrement < N ; 2°) Fig.2 : aspect à
  t₁ = 0,025 s, front en A, OA = 0,75 m : a) λ, v, N ; b) équation de S ;
  c) yA(t) ; d) graphe de yA. — Rép. : λ = 0,3 m ; v = 30 m.s⁻¹ ; N = 100 Hz ; yS = 3.10⁻³ sin(200πt) ;
  yA = 3.10⁻³ sin(200πt − π).
- **9** : I- corde infinie, vibrations transversales à partir de t = 0, pas d'amortissement ; courbes
  (I) (diagramme d'un point A, 1 div → 2,5.10⁻³ s) et (II) (aspect à t₁, 1 div → 5 cm), amplitude 4 mm.
  1°) identifier, T, λ, a ; 2°) v, xA, t₁ ; 3°) équations de S et A ; 4°) a) aspect à t₂ = 2,5.10⁻² s ;
  b) points d'élongation −a/2 se déplaçant dans le sens négatif ; c) nombre et abscisses des points en
  quadrature retard. II- pointe S, point O de l'eau, yO(t) = 10⁻³ sin(628t) : 1°) yM(t) ; 2°) v sachant
  que la plus petite distance entre 2 points en quadrature est d = 1 mm ; 3°) coupes à t₂ = 0,035 s et
  t₃ = 0,040 s ; 4°) fréquence des éclairs pour l'immobilité, plus grande possible ; un éclair de moins
  par seconde → sens apparent. — Rép. : T = 0,01 s ; λ = 0,2 m ; v = 20 m.s⁻¹ ; xA = 0,40 m ;
  t₁ = 0,02 s ; yS = yA = 4.10⁻³ sin(200πt) ; 4°c) 3 points x = 5λ/12 + kλ (k = 0, 1, 2) ; II :
  yM = 10⁻³ sin(628t − 2πx/λ) ; v = 0,4 m.s⁻¹ ; Ne = N/k, k = 1 : Ne = N = 100 Hz.
- **10** : corde L = 2 m, coton à l'extrémité ; lame part de l'équilibre à t = 0 ; Fig.1 : yM1(t)
  (cm ; t en 10⁻² s ; démarre vers 5,5, amplitude 0,5) ; Fig.2 : aspect à t₀ (x en 10⁻¹ m, front vers
  5,5). 1°) a) N et λ ; b) v ; c) x₁ et t₀ ; 2°) mouvements de S et M₁ ; 3°) instants où M₁ passe par
  2,5.10⁻³ m dans le sens positif entre 0 et 0,14 s ; 4°) abscisses des points à 2,5.10⁻³ m allant dans
  le sens négatif à t₀. — Rép. : N = 50 Hz ; λ = 0,2 m ; v = 10 m.s⁻¹ ; x₁ = 0,55 m ; t₀ = 0,055 s ;
  S et M₁ en quadrature ; t = (6,75.10⁻² + 0,02k) s, t₁ = 6,75.10⁻² s ; 3 points x = λ/8 + kλ (k = 0, 1, 2).
- **11** : deux microphones M₁, M₂ sur l'axe d'un HP, d = 34 cm, N = 2000 Hz, v = 340 m.s⁻¹, écran 10 ×
  8 divisions. 1°) a) base de temps pour 2 périodes ; b) pourquoi l'amplitude voie 2 < voie 1 ;
  c) oscillogramme ; 2°) a) N = 1 kHz, d = 17 cm : oscillogramme ; b) M₂ éloigné, oscillogramme analogue
  à 1° : d et base de temps. — Rép. : 10⁻⁴ s/div ; dilution de l'énergie ; d = 34 cm, 2.10⁻⁴ s/div.
- **12** Mesure de la célérité d'une onde sonore : micros M₁, M₂ sur YA, YB (Fig.1 : GBF, HP, règle,
  oscilloscope) ; 2 périodes sur 10 div, 0,4 ms/div ; positions successives en phase x₂ (cm) = 68,0 /
  136,0 / 204,0 / 272,0 / 340,0. 1°) fréquence ; 2°) λ ; 3°) v. — Rép. : N = 500 Hz ; λ = 0,68 m ;
  v = 340 m.s⁻¹.
- **13** : HP et micro M ; 1°) tensions visualisées ; 2°) fréquence (2 périodes, 10 div, 0,2 ms/div) ;
  3°) positions en phase x₁ = 4,5 cm, x₂ = 38,5 cm : λ ; 4°) v. — Rép. (étiquetées b, c, d) :
  N = 1000 Hz ; λ = 0,34 m ; v = 340 m.s⁻¹.
- **14** : GBF N = 1,47 kHz sur voie A, micro à d du HP sur voie B (Fig.1 schéma, Fig.2 oscillogramme
  de deux sinusoïdes décalées). 1°) a) durée de balayage ; b) décalage θ, temps de propagation en
  fonction de θ et N ; 2°) k = 100 mV/div : amplitudes, pourquoi différentes ; 3°) d₂ − d₁ = 23,0 cm
  (deux positions successives en phase) : λ et v ; 4°) d entre 40 et 60 cm : valeur ; 5°) la célérité
  change-t-elle avec la fréquence ? — Rép. : « T ≃ 68 ms » [?], s ≃ 0,1 ms/div ; θ ≃ 0,15 ms,
  Δt = n.T + θ = n/f + θ ; UR = 300 mV, UB = 250 mV ; λ = d₂ − d₁ = 23 cm, v = λ.f = 338 m.s⁻¹ ;
  d = v.Δt = λ.n + λ.f.θ = 23.n + 5,1 (cm), d = 51,1 cm ; « Célérité constante, l'air est un milieu non
  dispersif. »
- **15** : source ponctuelle en S, Ym = 3 mm, ys(t) = Ym sin(2πNt + π), pas de réflexion ni
  d'amortissement ; coupe à t₁ = 0,2 s (échelle 3 mm vertical / 4 mm horizontal, points A et B de part
  et d'autre de S). 1°) observation en lumière ordinaire ; 2°) a) λ ; b) v puis N ; 3°) a) équation
  de M d'abscisse x ; b) comparer A et B. (Pas de réponse p.317.)
- **16** Étude de texte « Quand la Terre tremble... » (d'après « La Recherche » ; d'après un sujet de
  baccalauréat, session principale de juin 2009) : ondes P (compression-détente « à la manière d'un
  accordéon », ~6 km.s⁻¹ dans la croûte) et ondes S (cisaillement, « deux fois plus lentes mais environ
  cinq fois plus fortes ») ; amortissement en s'éloignant du foyer. 1°) deux passages où l'auteur
  confond vibrations et ondes ; 2°) phrase montrant le caractère transversal/longitudinal de S et P ;
  3°) pourquoi les ondes S nous secouent horizontalement. (Pas de réponse p.317.)

### Fiches techniques et « En savoir plus »

- **Fiche technique n°1** (p.222) — méthode d'analyse optique : diaphragme unifente F au niveau de M,
  faisceau parallèle, ombre de M réfléchie par un miroir tournant à vitesse constante → sinusoïde sur
  l'écran (E) (Fig.1 = Fig.7).
- **Fiche technique n°2** (p.223) — stroboscopie : éclairs de période Te / fréquence Ne ; persistance
  rétinienne 0,1 s (intérêt au-delà de 10 Hz) ; disque à pastille noire à 20 tr.s⁻¹ éclairé à Ne =
  20 Hz → immobile ; « Il y a immobilité apparente chaque fois que : Te = k T (avec k un entier
  naturel) » ; ralenti apparent dans le sens réel si Te très légèrement > T (ou kT), sens contraire si
  très légèrement < T (ou kT).
- **En savoir plus** (p.224–225, source techno-science.net) — propriétés des ondes (onde oscillante,
  solitaire/mascaret, acoustique, de choc, électromagnétique ; vague sans courant ; instruments à
  corde ; onde de pression), vitesses de phase et de groupe, A(x⃗, t) = Ao sin(ωt − k⃗·x⃗ + φ), vecteur
  d'onde k = 2π/λ, ω = 2πν = 2π/T, c = λ/T = ω/k, séries/transformée de Fourier. Lecture culturelle.

### Bornes de scope

✅ **Inclus**
- Notions : ébranlement ; milieu élastique ; milieu de propagation uni-, bi-, tridimensionnel ;
  ébranlement/onde transversal(e) et longitudinal(e) (corde, ressort, surface de l'eau, son, ondes
  sismiques P/S en étude de texte) ; transport d'énergie sans transport de matière ; pas de
  propagation mécanique dans le vide ; célérité, constante en milieu homogène, indépendante de
  l'amplitude, dépendante du milieu (tension de la corde, inertie, compressibilité ; ordres de grandeur
  du tableau p.197) ; différences mobile / ébranlement ; onde = succession d'ébranlements ; onde
  entretenue, onde progressive (milieu ouvert, matière absorbante) ; double périodicité, T (source) et
  λ (source + milieu) ; λ = v.T = v/N ; dilution d'énergie (amplitude qui décroît avec la distance pour
  les ondes circulaires/sphériques) ; rides circulaires et rectilignes ; onde sonore progressive
  sphérique ; air milieu non dispersif (réponse ex.14).
- Méthodes/calculs : yM(t) = ys(t − θ), θ = x/v ; yM(t) = a sin(ωt + φs − 2πx/λ) ; Δφ = −2πx/λ ;
  points en phase (x = kλ), en opposition (question du cours), en quadrature avance (x = (4k − 1)λ/4)
  et retard (x = (4k + 1)λ/4) ; dénombrement de ces points avec x ≤ l (ou à l'intérieur du front) ;
  diagramme du mouvement d'un point (translation de θ, y = 0 avant l'arrivée du front) ; aspect
  yt(x) = a sin(2πx/λ − ωt + π), front d'onde xf = v.t = n.λ, aspect par extrapolation depuis le front,
  aspect à t₂ déduit de t₁ par avance de v(t₂ − t₁) ; coupe de la surface de l'eau ; lecture de λ, T,
  amplitude, v sur un diagramme temporel et un aspect spatial ; détermination de t₁, xA, du front ;
  instants où un point atteint une élongation donnée dans un sens donné ; points d'une élongation
  donnée se déplaçant dans un sens donné ; stroboscopie : Te = kT (Ne = N/k) immobilité, Te légèrement
  >/< kT ralenti sens réel/inverse ; mesure de λ et v du son par positions successives en phase d'un
  micro ; lecture d'oscillogramme (base de temps, sensibilité, décalage horaire θ, Δt = nT + θ).
- Appareillage : corde + lame vibrante/électro-aimant + pelote de coton ; ressort vertical + récipient
  d'eau ; échelle de perroquet + capteurs + mesureur de vitesse ; cuve à ondes, fourche à pointe,
  réglette ; stroboscope électronique ; analyse optique (diaphragme, miroir tournant) ; GBF,
  haut-parleur, microphone(s), oscilloscope bicourbe.

⛔ **Exclu** (absent du chapitre ou cantonné à « En savoir plus »)
- Diffraction, dispersion, nature ondulatoire de la lumière (chapitre 8) ; ondes électromagnétiques.
- Réflexion, ondes stationnaires, interférences (les dispositifs absorbants sont là pour les éviter).
- Formule quantitative de la célérité (v = √(F/μ) ou autre) : la dépendance à la tension / l'inertie /
  la compressibilité est seulement qualitative.
- Vitesse de phase / de groupe, vecteur d'onde k, nombre d'onde, notation A(x⃗, t) = Ao sin(ωt − k·x + φ),
  séries et transformée de Fourier, onde solitaire, onde de choc (lecture « En savoir plus » seulement).
- Amortissement quantitatif (seule la remarque a < aO), énergie transportée calculée, intensité sonore,
  décibels, effet Doppler, hauteur/timbre.
- Ondes sismiques au-delà de l'étude de texte (pas de calcul de distance à l'épicentre).

### Lecture

- **Couche texte** (pdftotext -layout) : p.188–225 en entier, réponses p.316–318 (chap. 7 en p.317 ;
  p.316 = chap. 1–4, p.318 = sites web, rubrique « Ondes »).
- **Pages lues sur l'image** (36) : 189, 190, 191, 192, 193, 195, 196, 197, 198, 199, 200, 201, 202,
  203 (r170), 204 (r170), 205 (r170), 206, 207, 208, 209, 210, 211 (r170), 212 (r170), 213, 214, 215,
  216 (r150), 217 (r150), 218 (r150), 219, 220 (r150), 221, 222, 223, 225, 317 (r200).
  Non vues sur image (prose seule, sans formule exploitée) : 188, 194, 224.
- **Sondage image (≥ 1/10, pages les plus denses)** : p.203, 204, 205, 211, 212, 213, 317. Écarts
  texte/image constatés : couche texte inutilisable pour toutes les formules de p.203–205, 211–212
  (ω, θ, φ, π, λ, fractions et indices perdus : « yM (t ) = a sin(t  ) », « Δ = - (4k - 1) ») ;
  **p.213 : la couche texte ne contient que « λ 2λ 3λ λ »** alors que l'image porte toute la fin de la
  solution (aspects à t₁ et t₂, x_f2 = x_f1 + λ/2, remarques) ; p.204 « x < l.. » / « ℓ » ; p.190
  relations des prérequis éclatées ; p.317 « Tb 68 ms », « θ b 0,15 ms » = « ≃ » sur l'image ;
  tableaux p.196–197 corrects en texte ; fig. p.216–218 (sinusoïdes, échelles) absentes du texte.
- **Doutes [?]**
  1. p.204 : « situés au repos à λ/4 **ayant** les points qui vibrent en phase » — mot imprimé tel quel
     (probablement « avant »), à ne pas citer comme règle.
  2. Ex.5 : énoncé a = 5 mm, réponse p.317 yM(t) = **2.10⁻³** sin(200πt − π) — incohérence d'amplitude
     dans le manuel.
  3. Ex.14 1°a : réponse « T ≃ 68 ms » alors que N = 1,47 kHz (T ≈ 0,68 ms) ; la question demande la
     « durée de balayage » — réponse probablement fautive ou mal libellée.
  4. Ex.13 : réponses étiquetées b), c), d) pour des questions numérotées 2°, 3°, 4°.
  5. Ex.7 : la source est en O mais l'énoncé parle ensuite de « provenant de S » et « en phase avec la
     source S » ; ex.10 et 15 notent la longueur d'onde « l » ; ex.15 renvoie à une « figure 5 »
     (unique figure).
  6. Pas de réponses au manuel pour les ex.1, 2, 15, 16 et pour plusieurs sous-questions (ex.3 2°a et
     4°, ex.4 3°–4°, ex.6 6°, ex.7 3°, ex.8 1° et 2°d, ex.9 4°a–b et II-3°).
  7. QCM 2-III (N = 100 Hz, Ne = 49 Hz) : non corrigé par le manuel ; à résoudre par l'auteur avec la
     règle Te légèrement > kT, sans réponse imprimée.
  8. Coquilles d'impression relevées (non corrigées dans les citations) : « unidimentionnel »,
     « verticlament », « prorogation », « armortissement », « sebleraient ».

## 2.8 Chapitre 8 — Nature ondulatoire de la lumière (manuel 223433, p.226–243)

**Page d'ouverture du chapitre (p.227)** — « NATURE ONDULATOIRE DE LA LUMIÈRE 8 ». Deux photos
légendées : « Image obtenue par holographie (procédé de photographie en trois dimensions) » ;
papillon bleu, « Certaines couleurs d'un papillon sont dues à des phénomènes physiques lumineux. »
Questions d'accroche (verbatim) : « ◆ Lorsqu'il rencontre sur son trajet un fil très fin ou un cheveu,
un faisceau de lumière laser subit un phénomène avec lequel on mesure les diamètres de tels obstacles.
Qu'est-ce que ce phénomène ? ◆ Est-il possible de faire subir à une lumière laser le phénomène de
dispersion ? Pourquoi ? »

**Objectifs (p.226, verbatim, vus sur l'image)** — « ◆ Justifier le caractère ondulatoire de la
lumière à partir d'expériences de diffraction d'ondes mécaniques et d'ondes lumineuses. ◆ Préciser
l'influence, sur le phénomène de diffraction, du quotient λ/a (λ étant la longueur d'onde et a la
largeur de la fente). ◆ Réaliser des expériences de dispersion des ondes lumineuses. ◆ Montrer que la
lumière blanche est constituée d'une infinité de radiations monochromatiques. ◆ Distinguer un milieu
dispersif d'un milieu non dispersif. »

**Prérequis (p.226)** — SAVOIR : « Définir une onde mécanique rectiligne. » ; « Définir le phénomène de
dispersion de la lumière blanche. » SAVOIR FAIRE : « Reconnaître une onde mécanique rectiligne. » ;
« Utiliser un stroboscope. » ; « Mesurer la longueur d'onde λ d'une onde plane progressive. » ;
« Utiliser une source Laser. » ; « Reconnaître le phénomène de dispersion de la lumière blanche. »

**Plan du chapitre** (titres numérotés du corps) : introduction (p.228) · **1. La diffraction**
(1.1 Diffraction d'une onde mécanique ; 1.2 Diffraction de la lumière — avec « Caractéristiques d'une
onde lumineuse » ; 1.3 Influence du quotient (λ/a) sur le phénomène de diffraction — cas de l'onde
mécanique, cas de l'onde lumineuse) · **2. Dispersion de la lumière** (2.1 Dispersion de la lumière
blanche par un prisme ; 2.2 Milieu dispersif et milieu non dispersif) · L'essentiel (p.237) ·
Exercices : exercice résolu (p.238–239), Tests rapides des acquis (ex. 1–2, p.240), Exercices
d'application (ex. 3–6, p.241), Exercices de synthèse (ex. 7–10, p.241–242) · En savoir plus (p.243).
Pas de fiche technique dans ce chapitre.

**Introduction (p.228, verbatim)** — « On a vu que lorsque le milieu de propagation est ouvert, toute
onde mécanique qui s'y propage est progressive. Dans ce chapitre, on se propose d'étudier le
comportement d'une telle onde à la rencontre d'un obstacle ou au niveau d'une fente très petite
(d'une largeur de quelques cm). On traitera aussi le cas d'un faisceau lumineux qui passe à travers une
fente fine (d'une largeur de quelques dixièmes de mm). »

### Cours — Activités / manipulations

**1.1 Diffraction d'une onde mécanique (p.228–229)**
- **Manipulation** : cuve à ondes remplie d'eau, lame vibrante **L** produisant une onde progressive
  plane ; deux éléments plans en plexiglas placés à une distance d de L forment une ouverture F de
  petite largeur **a** (Fig.1 : schéma vu de dessus, lame L à gauche, fente F de largeur a). Entre la
  lame et F : rides rectilignes. Au-delà de F :
  - a = 4 cm : « des rides rectilignes présentant une légère déformation au voisinage des bords »
    (Fig.2a, légende « Forme des rides pour a > λ ») ;
  - a = 1,5 cm : « des rides circulaires dans une zone triangulaire de sommet I milieu de la fente F »
    (Fig.2b, « pour a ≃ λ ») ;
  - a = 0,5 cm : « des rides quasiment circulaires de centre commun I » (Fig.2c, « pour a < λ »).
- **Questions** : 1°) nature de l'onde incidente sur F ; 2°) observation montrant qu'il émerge de F une
  onde différente de l'onde incidente, préciser la différence ; 3°) comparer λ (incidente) et λ'
  (émergente) par les distances entre rides consécutives ; 4°) comparer λ à a dans chaque cas.
- **Interprétation** (p.229) : « A son passage à travers la fente F, l'onde rectiligne de longueur
  d'onde λ se transforme en une onde circulaire de même longueur d'onde. Cette transformation qui se
  produit lorsque la largeur a de la fente F a une valeur comparable à celle de la longueur d'onde λ de
  l'onde incidente, est le phénomène de diffraction. L'onde qui en résulte est appelée onde
  diffractée. »
- **Remarque** : un obstacle de même largeur a donne le même phénomène (Fig.3 : « Diffraction d'une
  onde par un obstacle de largeur a », photo de cuve à ondes, obstacle vert).

**1.2 Diffraction de la lumière (p.229–231)**
- **Manipulation** : source laser (S), lumière rouge **λ = 633 nm**, écran E à une distance d de la
  source ; tache lumineuse sur E (Fig.4a haut : laser → faisceau → écran, « écran vu de face » : petit
  point). On interpose un diaphragme muni d'une fente rectangulaire F de largeur a réglable (Fig.4a
  bas : « Obstacle », faisceau élargi, écran vu de face : tache centrale de largeur L et taches
  latérales alignées horizontalement) :
  - a = 0,6 mm : « une figure étalée horizontalement, constituée d'un ensemble de taches brillantes
    séparées par des zones sombres. La tache centrale de largeur L est la plus brillante » ;
  - a = 0,3 mm : figure semblable, tache centrale de largeur L' plus grande ; « Plus précisément,
    L' = 2 L » (Fig.4b, photo).
- **Remarques** : 1 - un obstacle de même largeur donne encore une diffraction ; 2 - une fente
  circulaire de diamètre convenable donne « des taches circulaires concentriques, appelées anneaux de
  diffraction » (Fig.4c, « Figure de diffraction par un trou »).
- **Questions** : 1°) comparer a et λ ; 2°) les taches ont-elles la même largeur ? 3°) comment se
  présentent les taches latérales par rapport à la tache centrale ? 4°) effet de la forme de la fente ?
  5°) le principe de propagation rectiligne explique-t-il le phénomène ?
- **Interprétation** (p.230) : résultats qui « mettent en défaut le principe de propagation rectiligne
  de la lumière » ; phénomène semblable à celui de l'onde mécanique : diffraction. « Ainsi, une source
  laser éclairant une fente fine, donne sur un écran E, placé à une distance D de la fente, une figure
  étalée horizontalement appelée figure de diffraction. Elle est constituée d'une tache centrale
  lumineuse brillante, de largeur L, entourée de part et d'autre par des taches latérales brillantes.
  Ces taches brillantes sont séparées les unes des autres par des zones sombres. Ces taches sont
  appelées franges de diffraction. La largeur L de la tache centrale, pour une lumière donnée, dépend de
  celle de la fente. Ainsi, en diminuant la valeur de a, la largeur L de la tache centrale augmente.
  Les figures de diffraction qui se forment sur un écran E dépendent de la forme de la fente. Elles
  présentent les mêmes symétries de la fente (rectangulaire ou circulaire). »

**1.3 Influence du quotient (λ/a) (p.231–233)**
- **Cas de l'onde mécanique — Manipulation** : montage de la Fig.1, fréquence N de la lame constante,
  a = 1,5 cm fixe. Épaisseur d'eau e₁ : au-delà de F, rides circulaires dans une zone triangulaire de
  sommet I, pas de perturbation à l'extérieur (Fig.5a, « pour a ≃ λ ») ; épaisseur **e₂ = 3.e₁** :
  rides quasiment circulaires de centre I (Fig.5b, « pour a < λ »).
  Questions : 1°) variation de λ en fonction de la profondeur e ; 2°) comparer λ et a pour chaque e ;
  3°) facteurs qui influent sur la diffraction.
  Interprétation (p.232) : « la longueur d'onde λ augmente avec la profondeur de l'eau » ; « pour une
  valeur fixe a de la fente, le phénomène de diffraction est d'autant plus marqué que la longueur d'onde
  λ est plus grande. »
- **Cas de l'onde lumineuse — Manipulation** (p.232) : montage de la Fig.4a, écran E à **D = 2 m** de
  la fente ; papier millimétré collé sur E. Fig.6a : photo de la figure de diffraction. On fait varier
  a et on mesure L : « La largeur L représente la distance entre les milieux des bandes sombres qui
  entourent la tache centrale et l'angle θ représente la demi-largeur angulaire de la tache centrale »
  (Fig.6b : depuis le point I de la fente, angle θ entre l'axe et le bord de la tache de largeur L).
  - Tableau 1 (lumière rouge λR) : a (10⁻³ m) 0,10 / 0,15 / 0,20 / 0,25 / 0,30 ;
    L (10⁻³ m) 25 / 17 / 12 / 10 / 8.
  - Tableau 2 (lumière verte λV) : a (10⁻³ m) 0,10 / 0,15 / 0,20 / 0,25 / 0,30 ;
    L (10⁻³ m) 21 / 14 / 10 / 8 / 7.
  Questions (p.233) : 1°) influence de a sur L ; 2°) variation de L, puis de θ, en fonction de λ.
  Interprétation : « La Largeur L de la tache centrale ainsi que la demi-largeur angulaire θ de la tache
  centrale dépendent de la largeur a de la fente F. – Pour une valeur fixe de a, la largeur L de la
  tache centrale dépend de la longueur d'onde λ de la source d'éclairement. En effet, sachant que λR et
  plus grande que λV d'une part et que, d'après l'étude expérimentale, LR est plus grande que LV d'autre
  part, on déduit que L est d'autant plus grande que λ est plus petite. » **[?] contradiction interne,
  voir Doutes n°1.**

**2.1 Dispersion de la lumière blanche par un prisme (p.233–235)**
- Phrase d'introduction : « Un faisceau de lumière émis par une source laser peut subir une réfraction
  lorsqu'il traverse la surface de séparation de deux milieux transparents. »
- **Manipulation 1** : source laser (He-Ne) de longueur d'onde λ, écran E à une distance d, prisme en
  verre d'indice n ; on observe la déviation D du faisceau et le déplacement de la tache (Fig.7 :
  « Déviation d'un faisceau de lumière monochromatique », S → prisme → écran E, angle D entre la
  direction initiale en pointillés et le faisceau émergent).
  Questions (p.234) : 1°) interpréter la déviation D ; 2°) principe de propagation rectiligne vérifié ?
  3°) rappeler les lois de Descartes pour la réfraction.
- **Manipulation 2** : même dispositif avec source de lumière blanche, lentille convergente et fente F
  (ordre : source, fente, lentille, prisme, écran) ; en tournant le prisme, « un spectre coloré bordé de
  rouge et de violet, rappelant les couleurs de l'arc-en-ciel. C'est le spectre visible de la lumière
  blanche » (Fig.8 : bande continue violet → rouge).
  Questions : 1°) la lumière blanche subit-elle une déviation ? 2°) source des différentes couleurs ?
  3°) peut-on caractériser la lumière blanche par une longueur d'onde λ ?
- **Interprétation** : « La déviation D du faisceau est due à la double réfraction air/verre/air. » ;
  la lumière blanche sous une incidence i donne « un spectre formé par une infinité de lumières de
  couleurs différentes, limité par la lumière rouge d'un côté et la lumière violette de l'autre côté.
  C'est le phénomène de dispersion de la lumière blanche. » ; « spectre continu appelé spectre visible
  de la lumière blanche ».

**2.2 Milieu dispersif et milieu non dispersif (p.235–236)**
- **Manipulation** : dispositif du 2.1 avec filtres de couleurs (rouge, jaune, vert … et bleu), même
  source, même angle d'incidence i ; on note l'angle de déviation D pour chaque filtre. Fig.9
  (« Dispersion de la lumière blanche par un prisme ») : prisme en verre, rayons émergents rouge (le
  moins dévié), vert, bleu (le plus dévié).
- **Questions** : 1°) la déviation dépend-elle de l'indice n ? 2°) les radiations sont-elles déviées
  du même angle sous la même incidence ? 3°) radiation la plus déviée ?
- **Interprétation** (p.236) : « Ainsi, le bleu est plus dévié que le rouge et le vert. […] La
  dispersion de la lumière blanche est due au fait que l'indice n de réfraction du prisme n'est pas
  constant, et qu'il augmente en passant de la lumière rouge à la lumière bleue. Le prisme dans ce cas
  est un milieu dispersif. » Tableau (vu sur l'image) :

  | Couleur | ν (10¹⁴ Hz) | λ (10⁻⁶ m) | Indice n |
  |---|---|---|---|
  | Bleu sombre | 6,92 | 0,433 | 1,528 |
  | Bleu vert | 6,18 | 0,485 | 1,520 |
  | Jaune | 5,10 | 0,588 | 1,517 |
  | Rouge | 4,57 | 0,656 | 1,514 |
  | Rouge sombre | 3,91 | 0,767 | 1,511 |

- **Remarque** : « l'indice de réfraction du verre est d'environ 1,5 dans tout le domaine visible, car
  sa dispersion produit une augmentation de (0,006) pour chaque diminution de dix picomètres (10 pm) de
  la longueur d'onde. » **[?] voir Doutes n°3.** « En général, on appellera milieu dispersif pour une
  onde de fréquence N (ou ν) tout milieu où la célérité v de cette onde ne dépend pas uniquement des
  propriétés du milieu de propagation, mais dépend aussi de la fréquence N (ou ν) de l'onde. Dans le cas
  contraire où la célérité v de l'onde est indépendante de la fréquence N (ou ν), le milieu est dit non
  dispersif. L'air est un exemple de milieu non dispersif. »

### Encadrés, définitions et relations (VERBATIM, vérifiés sur l'image de leur page)

**Conclusion 1.1 (p.229)** — « Au niveau d'une fente ou d'un obstacle de largeur a d'une valeur
comparable à celle de sa longueur d'onde λ, l'onde mécanique subit le phénomène de diffraction.
La diffraction est la modification du trajet d'une onde et par suite de sa forme, au voisinage d'une
fente ou d'un obstacle.
En subissant la diffraction, une onde initialement plane se propage après franchissement de la fente ou
de l'obstacle, suivant plusieurs directions situées de part et d'autre de la direction d'incidence. »

**Conclusion 1.2 (p.231)** — « Au niveau d'une fente fine ou d'un obstacle de largeur a très petite (de
quelques dixièmes de mm), un faisceau de lumière (lumière rouge par exemple, émise par une source laser)
subit le phénomène de diffraction. La forme étalée de la figure de diffraction ne peut être expliquée
par le principe de propagation rectiligne de la lumière. Par rapprochement avec la diffraction d'une
onde mécanique, la propagation de la lumière dans un milieu transparent ou dans le vide peut être
considérée comme étant la propagation d'une onde appelée onde lumineuse. »

**Caractéristiques d'une onde lumineuse (p.231)** — « Comme l'onde mécanique, l'onde lumineuse, est
caractérisée par une période temporelle T et une période spatiale λ. – Dans le vide, toutes les ondes
lumineuses se propagent à la célérité **c = 3.10⁸ m.s⁻¹**. La relation entre λ et T s'écrit :
**λ vide = c.T**. » Remarque : « La célérité des ondes lumineuses dans l'air est assimilée avec une
bonne approximation à leur célérité dans le vide. »

**Conclusion 1.3, onde mécanique (p.232)** — « Une onde plane rectiligne, de longueur d'onde λ, qui se
propage à la surface d'un liquide et qui traverse une fente F de largeur a ne subit pas une déformation
appréciable tant que la valeur de a est très grande devant celle de λ. Par conséquent, le phénomène de
diffraction est imperceptible. Cependant, pour des valeurs de a comparables à celle de λ, le phénomène
de diffraction est appréciable. Ainsi, le phénomène de diffraction dépend du quotient **λ/a**. »

**Conclusion 1.3, générale (p.233)** — « Une onde mécanique ou lumineuse de longueur d'onde λ subit une
diffraction à la rencontre d'une fente ou d'un obstacle, de largeur a d'une valeur comparable à celle
de λ. La perception du phénomène de diffraction de l'onde dépend de la valeur du quotient (**λ/a**). »

**Conclusion 2.1 (p.235)** — « La lumière blanche résulte de la superposition d'une infinité de lumières
de couleurs différentes allant du rouge au violet. Ainsi, la lumière blanche est appelée lumière
polychromatique car elle est constituée de plusieurs, voire une infinité de lumières colorées ou
radiations. Chaque radiation est caractérisée par une fréquence ν et une longueur d'onde dans le vide
λ₀. Une lumière constituée d'une seule radiation est appelée lumière monochromatique. Les différentes
radiations constituant la lumière blanche ne sont pas déviées du même angle D par un prisme d'indice n,
c'est le phénomène de dispersion de la lumière. Ainsi, la déviation d'une radiation lumineuse
monochromatique par un prisme d'indice n, dépend de sa fréquence ν. »

**Conclusion 2.2 (p.236, lue à 200 dpi)** — « Chaque radiation lumineuse monochromatique de fréquence ν
est caractérisée par une longueur d'onde dans le vide **λ₀ = c/ν**.
En pénétrant dans un milieu transparent d'indice n, où la célérité de la lumière est **v = c/n**, sa
longueur d'onde devient **λ = v/ν = c/(n.ν) = λ₀/n**.
Le phénomène de dispersion de la lumière est la variation de sa célérité v dans un milieu transparent
d'indice n, en fonction de sa fréquence ν.
Ainsi, la déviation d'une radiation lumineuse monochromatique par un prisme en verre d'indice n dépend
de sa fréquence ν.
Tout milieu transparent d'indice de réfraction n, où la célérité d'une radiation lumineuse dépend de sa
fréquence est appelé milieu dispersif.
Le verre est un exemple de milieu dispersif. »

**L'essentiel (p.237, verbatim)** —
- « La diffraction d'une onde est la modification de son trajet et par suite sa forme au voisinage
  d'une ouverture ou d'un obstacle de dimensions comparables à sa longueur d'onde.
- La diffraction d'une onde se fait sans changement de sa longueur d'onde.
- Un faisceau de lumière est décrit comme étant une onde appelée onde lumineuse.
- Le phénomène de diffraction dépend du quotient λ/a, λ étant la longueur d'onde et a l'ouverture de
  la fente.
- Une lumière monochromatique est une onde progressive sinusoïdale caractérisée par sa fréquence ν et
  sa longueur d'onde λ₀ dans le vide.
- Une lumière polychromatique est constituée de plusieurs radiations.
- La lumière blanche est une lumière polychromatique.
- Le phénomène de dispersion de la lumière est la variation de sa célérité v dans un milieu
  transparent d'indice n, en fonction de sa fréquence ν.
- On appelle milieu dispersif tout milieu dans lequel la célérité v d'une onde lumineuse dépend de sa
  fréquence. »

### Exercice résolu (p.238–239)

**Énoncé** — Lumière monochromatique **λ = 0,525 μm**, fente fine rectangulaire de largeur réglable a,
écran E à **D = 3 m**. Tableau : a (mm) 0,10 / 0,14 / 0,20 / 0,25 ; L (mm) 31,5 / 22,5 / 16,0 / 12,5.
1°) Décrire brièvement la figure de diffraction. 2°) a) influence de a sur L ; b) influence qualitative
de a sur la netteté. 3°) avec a = 0,1 mm, écran placé à D' = 1 m : montrer que la figure devient moins
nette. 4°) fente remplacée par un cheveu de diamètre d = 0,20 mm : valeur de L avec D = 3 m, justifiée.

**Solution** — 1°) figure étalée horizontalement, tache centrale brillante de largeur L entourée de
taches lumineuses séparées par des zones sombres (schéma : laser, fente, « taches de diffraction sur un
axe horizontal »). 2°) a) « si a augmente, L diminue. » b) « La figure de diffraction est d'autant plus
nette que la tache centrale est plus large. Or, L diminue quand a augmente. Donc, plus la fente et fine
(θ plus petite), plus la figure de diffraction est nette. » **[?] voir Doutes n°2.** 3°) « En maintenant
la largeur a de la fente fixe et en diminuant D, la demi-largeur angulaire θ de la tache centrale ne
change pas tandis que sa largeur L devient plus petite » (schéma : fente, angle θ, demi-largeurs L/2 à
D et L'/2 à D') ⇒ moins nette. 4°) le cheveu donne « exactement la même figure de diffraction que celle
obtenue avec une fente de largeur a égale à d » ; tableau : a = 0,20 mm ⇒ **L = 16 mm**.

### Exercices à résoudre (p.240–242) — réponses du manuel p.317

**Tests rapides des acquis** (aucune réponse au manuel)
- **Ex.1 Vrai/faux** (9 items) : ondes transversales et diffraction ; dispersion comme preuve du
  caractère ondulatoire ; diffraction et impossibilité d'isoler un rayon lumineux ; milieu dispersif si
  la célérité ne dépend que de ses propriétés ; lumière blanche seule lumière polychromatique
  dispersable ; diffraction sur un obstacle de l'ordre de λ ; diffraction sans influence sur λ ; air
  non dispersif comme le vide ; verre dispersif car vitesse dépendant de la fréquence.
- **Ex.2 QCM** (6 items, une ou plusieurs réponses) : I ce que met en évidence la diffraction ; II
  conditions (λ du même ordre que a / λ ≪ a / λ/a > 1) ; III figure d'une fente (anneaux / taches
  étalées perpendiculairement / parallèlement à la fente) ; IV L augmente avec λ / ne dépend pas de D /
  diminue quand a augmente ; V célérité dans un milieu dispersif dépend « uniquement » de … ; VI même
  célérité dans l'air parce que l'air … (dispersif / transparent / même indice pour toutes les
  radiations).

**Exercices d'application**
- **Ex.3** — fente circulaire de diamètre a, D = 4,5 m ; rayon r de la tache centrale :
  a (10⁻⁴ m) 4,9 / 6,2 / 8,2 / 12,0 ; r (10⁻³ m) 7,5 / 6,0 / 4,5 / 3,0. 1°) décrire la figure ;
  2°) montrer que la figure est d'autant plus nette que la fente est plus fine. Pas de réponse au manuel.
- **Ex.4** — digue de largeur l = 30 m (ouverture vers une baie), vagues parallèles λ = 80 m ;
  propagation au-delà, schéma, nature du phénomène ; vagues λ = 5 m. Réponse : « 1°) rides
  circulaires, 3°) diffraction, 4°) λ << l, pas de diffraction. »
- **Ex.5** — laser λ, fente de largeur a, écran E perpendiculaire ; schématiser la figure ; définir θ
  « caractérisant la tache centrale » ; influence de a sur θ ; schéma montrant que L augmente avec D
  tandis que θ reste constante. Pas de réponse au manuel.
- **Ex.6** — faisceau monochromatique, prisme d'indice n, incidence i : définir l'indice ; lois pour
  tracer le faisceau émergent ; tracé sur la figure (prisme, écran E incliné) ; observation sur E ;
  cas de la lumière blanche. Réponse : « 1°) n=c/v, 2°) sin(i₁)=n.sin(i₂), 4°) une tache, 5°) oui, on
  obtient le spectre de la lumière blanche. »

**Exercices de synthèse**
- **Ex.7** — fente de largeur a réglable, λ = 0,63 μm, D = 1 m. 1°) lumière monochromatique ;
  2°) a = 0,1 mm : a) décrire, b) justifier en comparant L et a ; 3°) L' pour λb = 0,46 μm ;
  4°) pourquoi plus facile en rouge qu'en bleu ; 5°) a = 2 mm observable ? Réponse : « 1°) Une seule
  radiation, 2°)a) Tache centrale de largeur L, b) λ/a = 6,3.10⁻⁶ < 0,174, 3°) L' = 9,2.10⁻³ m,
  4°) L' < L, 5°) L = 0,63.10⁻³ m, on mesure difficilement L. » **[?] Doutes n°4–5.**
- **Ex.8** — figure reproduite, D = 2 m, a = 100 μm, λ = 0,675 μm (laser) ; figure : X₁ = 2,7 cm
  (tache centrale), X₂ = 5,5 cm, X₃ = 8 cm. 1°) schéma du dispositif ; 2°) relation entre X₁ et θ ;
  3°) comparer largeur centrale / latérale ; 4°) comparer avec λ = 450 nm. Réponse : « 2°) θ₁ = X₁/2D,
  4°) X₁ = 2λ.D/a = 1,8.10⁻² m. »
- **Ex.9** — rayon monochromatique, i = 30°, point I de la face plane d'un hémicylindre en plexiglas
  (figure : S, normale N, I). 1°) lois de Descartes ; 2°) rφ (jaune, nφ = 1,485) ; 3°) montrer
  D = iφ − rφ ; 4°) rB (bleu, nB = 1,520) ; 5°) lumière jaune + bleue : tracé, angle entre les rayons,
  phénomène. Réponse : « 1°) n₁sin(i₁) = n₂sin(i₂), 2°) sin(rj) = sin(i)/nj, rj = 19,67°, 3°) ij > rj
  par la suite D = ij – rj = 10,3°. 4°) rb = 19,2° et D' = 10,8°, ainsi la radiation bleue est la plus
  déviée, la dispersion de la lumière. »
- **Ex.10** — texte « La houle… » (d'après Hachette Multimédia 2000) ; glossaire houle, cap,
  promontoire, jetée ; expliquer la diffraction des vagues au niveau d'une baie, d'un cap, d'une île ;
  partie de jetée responsable de la pénétration des vagues dans un port. Pas de réponse au manuel.

### Fiche technique et « En savoir plus »

- Pas de fiche technique dans le chapitre.
- **En savoir plus (p.243)** — « L'interprétation du phénomène de diffraction avec la théorie des
  ondelettes » : surface d'onde Σt, sources secondaires de Huygens émettant des ondelettes circulaires
  de rayon v.T, superposition donnant Σt+T ; si a très petite devant λ, F assimilée à une source
  secondaire unique (Fig.1–3) ; encadré biographique Christian Huygens (1629-1695), « Traité de
  lumière » (1678). Lecture seule.

### Bornes de scope

**✅ Inclus**
- Diffraction d'une onde mécanique en cuve à ondes (fente ou obstacle) : rides rectilignes → circulaires,
  conservation de λ, onde diffractée ; comparaison qualitative a > λ / a ≃ λ / a < λ.
- Influence de λ (via la profondeur d'eau : λ augmente avec la profondeur) et de a ; dépendance au
  quotient λ/a, lecture qualitative (« marqué », « imperceptible », « appréciable »).
- Diffraction de la lumière laser par une fente fine, un obstacle (fil, cheveu), un trou : description
  de la figure (tache centrale plus large et plus brillante, taches latérales, zones sombres, étalement
  perpendiculaire à la fente — figure étalée horizontalement pour une fente verticale, anneaux pour un
  trou) ; mise en défaut de la propagation rectiligne ; onde lumineuse.
- Grandeurs : largeur L de la tache centrale (entre milieux des bandes sombres), demi-largeur angulaire
  θ ; L diminue quand a augmente ; L augmente avec D à θ constant ; netteté liée à la largeur de la
  tache centrale ; équivalence fente de largeur a / cheveu ou fil de diamètre d = a ; lecture de
  tableaux de mesures (a, L) et interpolation directe.
- Relations : c = 3.10⁸ m.s⁻¹ ; λ vide = c.T ; λ₀ = c/ν ; v = c/n ; λ = v/ν = c/(n.ν) = λ₀/n ;
  célérité dans l'air ≈ célérité dans le vide.
- Dans les exercices et leurs réponses seulement (p.241–242, 317) : θ₁ = X₁/2D (petits angles) et
  X₁ = 2λ.D/a (ex.8 4°), calcul de L' pour une autre λ (ex.7 3°) ; lois de Descartes
  n₁sin(i₁) = n₂sin(i₂) et calcul d'un angle de réfraction ; déviation D = i − r à la face plane d'un
  hémicylindre ; indice n = c/v. **[?] statut à trancher, voir Doutes n°6.**
- Dispersion : prisme, double réfraction air/verre/air, déviation D ; spectre continu de la lumière
  blanche (rouge → violet) ; lumière monochromatique / polychromatique ; radiation caractérisée par ν et
  λ₀ ; laser monochromatique (une tache, pas de spectre) ; le bleu plus dévié que le rouge ; n du verre
  croît du rouge au bleu (tableau ν, λ, n) ; milieu dispersif (verre) / non dispersif (air, vide)
  défini par la dépendance de la célérité à la fréquence.
- Application aux vagues : digue, baie, cap, île, jetée (ex.4, ex.10).

**⛔ Exclu**
- Formule de la diffraction énoncée dans le cours (θ = λ/a ou sin θ = λ/a) : elle n'apparaît **pas**
  dans le cours ; ne pas l'enseigner comme loi du chapitre (voir Doutes n°6 pour l'usage dans les
  réponses). Pas de calcul de la position des minima d'ordre k, pas d'intensité de la figure, pas de
  formule pour les anneaux (1,22 λ/a).
- Interférences (fentes d'Young, interfrange), réseaux, holographie, iridescence du papillon (photos
  d'accroche seulement), polarisation.
- Formules du prisme (A = r + r', D = i + i' − A, minimum de déviation), loi de Cauchy, calcul de
  l'indice en fonction de λ.
- Théorie des ondelettes de Huygens : lecture « En savoir plus » seulement, non évaluable.
- Énergie du photon, aspect corpusculaire (chapitre 9), spectres de raies.
- Appareillage : cuve à ondes, lame vibrante, laser He-Ne, diaphragme à fente réglable, papier
  millimétré, prisme, lentille convergente, filtres colorés — **stroboscope** cité en prérequis
  seulement ; pas de spectroscope à réseau (chap. 9).

### Lecture

- **Couche texte** (pdftotext -layout) : p.226–243 en entier ; réponses p.316–318 (chap. 8 en p.317,
  colonne droite ; p.316 = chap. 1–4 ; p.318 = sites web, rubrique « Ondes » : liens diffraction et
  spectre).
- **Pages lues sur l'image** (19) : 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236 (et 200 dpi
  pour la conclusion), 237, 238, 239, 240, 241, 242 (et 250 dpi pour la figure de l'ex.8), 243,
  317 (200 dpi, colonne chap. 8). Aucune page du chapitre non vue sur image.
- **Sondage image (≥ 1/10, pages les plus denses)** : p.232, 236, 237, 242, 317. Écarts texte/image
  constatés : le quotient λ/a est rendu « **h** / a » dans la couche texte p.233 et p.237 (image : λ) ;
  ν (nu) rendu « V » / « Vx » p.235–237 ; conclusion p.236 illisible en texte (« λ = v = … = λ0 . »
  éclaté, λ₀ = c/ν perdu) ; Fig.2b/5a « a b λ » = « a ≃ λ » ; « 3.108 m.s-1 » = 3.10⁸ ; exposants des
  tableaux (10-3, 1014) ; légendes de la figure de l'ex.8 (X₁ = 2,7 cm, X₂ = 5,5 cm, X₃ = 8 cm)
  absentes du texte ; indices φ / j de l'ex.9 ; tableaux p.232, 236, 238, 241 corrects en texte.
- **Doutes [?]**
  1. **p.233, Interprétation** : « λR et plus grande que λV » et « LR est plus grande que LV », puis
     « on déduit que L est d'autant plus grande que λ est plus **petite** » — conclusion contraire aux
     données (tableaux 1 et 2 : L rouge > L vert) et à la réponse ex.7 4°) « L' < L » (bleu vs rouge) ; à ne pas reprendre telle quelle
     (la conclusion cohérente avec les mesures serait « plus grande »). Coquilles « et » pour « est »,
     « fonte » pour « fente ».
  2. **p.239, solution 2°b** : « plus la fente et fine (θ plus petite) » — une fente plus fine donne une
     tache plus large donc θ plus grand ; parenthèse fautive dans le manuel.
  3. **p.236, Remarque** : « augmentation de (0,006) pour chaque diminution de dix picomètres » —
     incompatible avec le tableau (n passe de 1,511 à 1,528 sur ~334 nm) ; chiffre à ne pas utiliser.
  4. **Ex.7 2°b, réponse** : « λ/a = 6,3.10⁻⁶ < 0,174 » — avec λ = 0,63 μm et a = 0,1 mm, λ/a =
     6,3.10⁻³ ; l'origine de « 0,174 » n'est pas expliquée, et la question demande de comparer L à a.
     Réponse inexploitable telle quelle.
  5. **Ex.7 5°, réponse** « L = 0,63.10⁻³ m » et 3°) « L' = 9,2.10⁻³ m » supposent L = 2λD/a, non énoncée
     dans le cours (cohérent numériquement avec cette relation).
  6. **Relation L = 2λD/a / θ ≈ L/2D** : absente du cours (qualitatif seulement), utilisée par les
     réponses des ex.7 et 8. À décider par l'humain : la traiter comme hors cours (exclue) ou comme
     savoir-faire d'exercice. Fiche actuelle : inclus « dans les exercices seulement ».
  7. 1.2 : source à une distance « d » de l'écran dans la manipulation, puis « distance D de la fente »
     dans l'interprétation (deux grandeurs différentes, non confondre).
  8. Pas de réponses au manuel pour les ex.1, 2, 3, 5, 10, ni pour ex.4 2°, ex.6 3°, ex.7 (texte
     partiel), ex.8 1° et 3°, ex.9 5°.
  9. Ex.9 : indice « φ » dans l'énoncé (jaune), « j » dans les réponses ; même grandeur.
  10. Coquilles relevées (non corrigées dans les citations) : « mécnique » (Fig.1), « Figue de
      diffraction » (Fig.6a), « réfaction » (ex.6), « ci-desous » (ex.8), « diffaction »,
      « caactérisée » (p.239), « circualire », « donde », « supersosition », « intrépatation »,
      « Islance » (p.243).

## 2.9 Chapitre 9 — Spectre atomique (manuel 223433, p.244–269)

**Ouverture de partie (p.244–245)** — « Physique atomique et nucléaire » : photo du spectre solaire
(« Un des jolis spectres lumineux qui éclairent les chercheurs sur les confins de l'Univers » ; légende
« Détails du spectre solaire montrant que celui-ci renferme des raies d'absorption »), cœur de réacteur,
explosions (bombe H, bombe atomique). Sommaire de la partie : I. Spectre atomique (1. Energie des systèmes
en interaction ; 2. Quantification de l'énergie ; 3. Spectres lumineux ; 4. Spectre de l'atome d'hydrogène ;
5. Applications) · II. Noyau atomique · III. Réactions nucléaires (chap. 10–11, hors de cette fiche).

**Page d'ouverture du chapitre (p.247)** — « 9 · SPECTRE ATOMIQUE », photo de la nébuleuse du Crabe ;
bandeau : « L'analyse de la lumière émise par les corps célestes est un moyen d'investigation précieux en
astrophysique. Les couleurs de cette image de la nébuleuse du crabe révèlent sa nature physique. »
Questions d'accroche (verbatim) :
- « L'analyse de la lumière émise par un objet quelconque peut-elle nous renseigner sur sa composition
  chimique, sa température ou sa vitesse s'il est en mouvement ? »
- « Comment peut-on identifier un élément chimique à partir de l'analyse de son spectre lumineux ? »
- « On dit que le spectre d'émission d'un atome constitue sa «carte d'identité». Pourquoi ? »

**Objectifs (p.246, verbatim)** — Décrire une expérience qui montre que l'énergie de l'atome est
quantifiée. · Calculer l'énergie de l'atome d'hydrogène en joule et en électron-volt. · Distinguer un
spectre d'émission d'un spectre d'absorption. · Appliquer la relation ΔE = h.ν. · Identifier un élément
chimique à partir de son spectre d'émission ou d'absorption. · Utiliser le spectre de la lumière émise par
une étoile pour reconnaître certains de ses constituants.

**Prérequis (p.246)** — *Savoir* : définir la force d'interaction gravitationnelle ; définir la force
d'interaction électrique ou coulombienne ; énoncer le principe de conservation de l'énergie ; définir les
grandeurs caractéristiques d'une onde (période, fréquence, longueur d'onde) ; donner les règles de
répartition des électrons d'un atome sur les différents niveaux d'énergie. *Savoir-faire* : utiliser un
prisme pour analyser une lumière ; appliquer le principe de conservation de l'énergie ; convertir en
électron-volt une énergie exprimée en joule et inversement ; appliquer la RFD au mouvement d'un satellite ;
distinguer lumière monochromatique et polychromatique ; répartir les électrons d'un atome sur les niveaux
d'énergie.

**Plan du chapitre** (titres du manuel) : introduction (p.248 : lumière blanche polychromatique, sept
couleurs ; « Qu'en est-il pour le spectre obtenu par la dispersion d'une lumière émise par une lampe à
vapeur de sodium ou de mercure (lampes d'éclairage public) ? ») ·
1 Energie des systèmes en interaction (1.1 Cas d'un système macroscopique ; 1.2 Cas d'un système
microscopique : l'atome) · 2 La quantification de l'énergie (2.1 Expérience de Franck et Hertz (1914) ;
2.2 Niveaux d'énergie d'un atome) · 3 Spectres lumineux (3.1 Spectre visible de la lumière blanche
(rappel) ; 3.2 Spectre d'émission ; 3.3 Spectre d'absorption) · 4 Spectres de l'atome d'hydrogène
(4.1 Notion de photon ; 4.2 Modèle de Bohr de l'atome d'hydrogène ; 4.3 Énergie de l'atome d'hydrogène ;
4.4 Interprétation des raies d'émission ; 4.5 Interprétation des raies d'absorption) · 5 Applications
(5.1 En chimie ; 5.2 En astrophysique) · L'essentiel (p.262) · Exercices (exercice résolu p.263 ; exercices
à résoudre 1–10 p.264–267) · En savoir plus « Les modèles de l'atome » (p.268–269).

### Cours — Activités / études (chaque bloc : Questions → Interprétation → Conclusion)

**1.1 Système macroscopique {Terre-Satellite}** (p.248) — énergie mécanique = cinétique + potentielle ;
loi de gravitation (vue en 3e année) ; Fig.1 « Interaction gravitationnelle » (T et S sur un axe, vecteurs
u_TS, F_S/T, F_T/S). Relation (image) : **F⃗_T/S = − G (m M / r²) u⃗_TS = − F⃗_S/T** ; u⃗_TS vecteur
directeur unitaire de l'axe joignant (T) et (S), G constante de gravitation universelle, r distance
satellite–Terre.
Questions : 1°) comment modifier l'énergie mécanique de ce système ? 2°) les orbites sont-elles limitées à
des distances fixes ? 3°) un avion en vol peut-il changer d'altitude ?
Interprétation : il faut fournir une énergie W au système ; satellites placés sur une très large gamme de
distances ; « Toutes les valeurs de l'énergie W sont permises » ; ordres de grandeur : satellites
d'observation à quelques centaines de km, géostationnaires à plusieurs dizaines de milliers de km, Lune à
plusieurs centaines de milliers de km ; un avion peut changer d'altitude à tout moment.
**Conclusion (p.249)** : « Lorsqu'un système macroscopique interagit avec l'extérieur, l'énergie du système
peut varier de façon continue. »

**1.2 Système microscopique : l'atome** (p.249–250) — cohésion noyau-électron par la force coulombienne ;
atome à un électron (hydrogène), noyau ponctuel en A, électron en B (Fig.2 « Interactions
coulombiennes »). Relation (image) : **F⃗_A/B = k (q_A q_B / r²) u⃗_AB = − k (e² / r²) u⃗_AB = − F⃗_B/A** ;
u⃗_AB vecteur unitaire de l'axe noyau-électron, e charge élémentaire, r distance noyau-électron,
**k = 9.10⁹ N.m².C⁻²**. Analogie → modèle « planétaire » de Rutherford (orbites circulaires).
Questions : 1°) les électrons subissent-ils une accélération ? caractéristiques ? 2°) loi de Maxwell
« toute particule chargée électriquement et accélérée rayonne de l'énergie » : a) effet sur le mouvement de
l'électron ; b) l'énergie du système {noyau-électron} est-elle conservée ?
Interprétation : l'électron rayonne, perd de l'énergie, se rapproche du noyau et finit par « s'écraser » ;
l'atome ne serait pas stable.
**Conclusion (p.250)** : « Par application des lois de la mécanique newtonienne on ne peut pas interpréter
l'interaction électron- noyau au niveau de l'atome. »

**2.1 Expérience de Franck et Hertz (1914)** (p.250–251) — bombardement de vapeur de mercure sous faible
pression par un faisceau d'électrons. Dispositif simplifié (Fig.4, schéma : enceinte ovale « Gaz à faible
pression », « canon à électrons » à gauche, « analysateur » à droite) : enceinte à vapeur de Hg faible
pression ; canon à électrons (électrons de même énergie cinétique Ec) ; capteur analyseur comptant les
électrons qui l'atteignent avec une énergie cinétique donnée. Fig.3 : portraits de J. Franck et G. Hertz.
Principe : on fait varier Ec (tension accélératrice) ; courbe N_C/N_e = f(E_C), N_C nombre d'électrons par
unité de temps comptés sur l'analyseur, N_e nombre émis par le canon. **Fig.5** (image) : palier
N_C/N_e = 1 pour Ec < 4,9 eV, chute brutale à Ec = 4,9 eV, puis palier plus bas (< 1) jusqu'à la fin du
graphe (axe Ec en eV, seule graduation 4,9).
Questions : 1°) allure de la courbe, comparer N_C et N_e pour Ec < 4,9 eV et Ec > 4,9 eV ; 2°) interpréter
la chute du rapport pour Ec = 4,9 eV, sachant qu'un atome peut se trouver dans un état excité.
Interprétation : Ec < 4,9 eV → N_C/N_e = 1, chocs **élastiques** (sans cession d'énergie) ; Ec ≥ 4,9 eV →
N_C/N_e < 1, chocs **inélastiques**, l'électron cède 4,9 eV à l'atome ; « l'atome de mercure ne peut prendre
qu'une énergie bien déterminée, telle que 4,9 eV ».
**Conclusion (p.251)** : « Lors de la collision d'un atome avec un électron d'énergie cinétique Ec,
l'électron peut lui céder de l'énergie. Cette énergie transférée ne peut prendre que des valeurs
particulières. L'expérience de Franck et Hertz met en évidence la quantification du transfert d'énergie
entre un atome et le milieu extérieur. »

**2.2 Niveaux d'énergie d'un atome** (p.252) — Hypothèses de Bohr (inspiré de Planck ; Fig.6a Bohr,
Fig.6b Planck) : « Les variations d'énergie de l'atome sont quantifiées. » « L'atome ne peut exister que
dans certains états d'énergie bien définis. » Niveaux d'énergie : l'énergie d'un atome ne peut prendre que
certaines valeurs particulières appelées niveaux d'énergie ; l'ensemble des niveaux associés à un atome est
unique ; schématisés par des paliers E = cte sur un axe des énergies (Fig.7 : E₁ niveau fondamental, E₂,
E₃… niveaux excités). **État fondamental** = niveau le plus bas (état le plus stable) ; niveaux supérieurs =
**états excités** ; passage de E_p à E_n = **transition** (p, n entiers numéros des états).
Questions : 1°) pourquoi « état excité » ? 2°) a) pour passer du fondamental à un état excité, l'atome
cède-t-il ou absorbe-t-il de l'énergie ? b) toute énergie suffit-elle ? sinon, son expression en fonction
des énergies des deux niveaux.
**Conclusion (p.252)** : « L'énergie d'un atome est quantifiée : elle ne peut prendre que des valeurs
discrètes caractéristiques de l'atome. Chacune entre elles représente alors un niveau d'énergie En. Dans son
état fondamental, un atome est au plus bas niveau d'énergie. Grâce à un apport d'énergie de l'extérieur, un
atome peut se trouver dans un état excité. »

**3 Spectres lumineux** (p.253) — spectromètre : disperse une lumière polychromatique ; observé à l'œil nu
= **spectroscope** ; élément essentiel = **disperseur** : **réseau** (Fig.8a ; fentes très fines et très
serrées gravées sur une plaque de verre, décomposition par diffraction « entre autres ») ou **prisme**
(Fig.8b). Remarque : spectre sur pellicule photographique → **spectrographe**.
**3.1 Rappel** : lumière blanche + prisme → spectre continu (couleurs de l'arc-en-ciel) sur écran E. Fig.9
(schéma : lumière blanche, fente, lentille L, prisme, lentille L', écran ; rouge le moins dévié, jaune,
violet le plus dévié).

**3.2 Spectre d'émission** (p.253–254) — Dispositif (Fig.10a, photo) : source S (lampe spectrale à vapeur
de mercure ou d'hydrogène, Fig.10b), condenseur C, fente rectangulaire F, lentille L, réseau R, écran E.
Lampe Hg → spectre de raies Fig.11a ; lampe à hydrogène → Fig.11b (image : 4 raies, violet, bleu-violet,
bleu-vert, rouge).
Questions : 1°) a) décrire les spectres ; b) les comparer entre eux, puis avec celui de la lumière blanche ;
2°) en déduire qu'à chaque élément chimique correspond un spectre bien défini.
Interprétation : spectre discontinu, bandes fines multicolores sur fond sombre = **spectre de raies** ;
lampe à vapeur d'atomes identiques → **spectre d'émission**, caractéristique de l'élément. Hydrogène :
quatre raies « Hα de couleur rouge orangée, Hβ de couleur bleue, Hγ de couleur indigo et Hδ de couleur
violette ».
**Conclusion (p.254)** : « Tout élément chimique est caractérisé par un spectre de raies appelé spectre
d'émission. »

**3.3 Spectre d'absorption** (p.254–256) — même montage, vapeur de sodium interposée entre condenseur et
fente (« on fait brûler du sodium ») ; Fig.12 (photo : « lame de verre + alcool + eau salée » entre C et F ;
légende imprimée « Dispositif expérimental permettant d'obtenir un spectre d'émision » [sic]). Spectres
(images) : Fig.13 absorption du sodium (spectre continu, une raie noire dans le jaune) ; Fig.14a absorption
du mercure ; Fig.14b absorption de l'hydrogène.
Questions : 1°) décrire Fig.13, comparer à Fig.9 ; 2) effet de la vapeur de sodium ; 3) comparer Fig.13,
14a, 14b ; 4) comparer 11a/14a et 11b/14b en nature, nombre et disposition relative des raies.
Interprétation : le gaz absorbe les radiations dont les énergies peuvent mettre les atomes dans des états
excités → spectre de la lumière blanche avec raies noires (**cannelures**) = spectre d'absorption ; « le
spectre d'absorption du sodium présente une raie noire (Fig.13), celui de l'hydrogène quatre raies noires
(Fig.14b) ».
**Conclusion (p.256)** : « En plus du spectre d'émission, les atomes d'un élément chimique donné sont
caractérisés par un spectre d'absorption. Le spectre d'absorption atomique d'un élément chimique est le
spectre continu de la lumière blanche qui lui manque les raies correspondant aux radiations absorbées par
les atomes de cet élément chimique. Les cannelures d'un spectre d'absorption sont superposables aux raies
du spectre d'émission du même élément chimique. Le spectre d'émission ou d'absorption constitue « la carte
d'identité » de l'élément chimique. »
Remarque : passage émission → absorption = **renversement des raies** (raie brillante → raie noire au même
endroit) ; Fig.15 spectres d'émission et d'absorption de l'hydrogène superposés.

**4.1 Notion de photon** (p.256) — diffraction = nature ondulatoire, insuffisante pour interpréter le
spectre d'émission ; radiation de longueur d'onde λ = flux de particules non chargées et sans masse,
**photons**. Relation (image) : **W = h.c/λ = h.ν**, h constante de Planck, **h = 6,62.10⁻³⁴ J.s**.
Remarque : « L'énergie d'un photon est appelée quantum d'énergie. »

**4.2 Modèle de Bohr de l'atome d'hydrogène** (p.256, postulats verbatim) :
- « Le noyau est supposé fixe dans l'atome car sa masse est 1836 fois plus grande que celle de l'électron. »
- « L'électron ne peut graviter autour du noyau que sur des orbites circulaires bien déterminées. Ces
  orbites quantifiées sont dites stationnaires. »
- « L'électron n'échange de l'énergie avec l'extérieur que lors de son passage d'une orbite stationnaire à
  une autre. »

**4.3 Énergie de l'atome d'hydrogène** (p.257) — Bohr établit En en fonction de Eo (énergie de l'état
fondamental). Formule imprimée (image, zoom 300 dpi) : « En = En/n² ; avec Eo = 13,6 eV et n un entier
natuel non nul » [coquille : signe « − » absent et « En » au numérateur ; forme correcte donnée par
l'Essentiel, l'exercice résolu et les exercices : **En = − E0/n²**]. « En est exprimé en eV. 1 eV =
1,6.10⁻¹⁹ J. »
- n = 1 : E₁ = −13,6 eV, niveau d'énergie minimale ou niveau fondamental, état le plus stable ;
- n > 1 : −13,6 eV < En < 0, l'un des états excités ;
- n → ∞ : En(∞) = 0, atome ionisé, proton et électron séparés.
Énergie d'ionisation : il faut fournir au moins 13,6 eV à l'atome pris dans son état fondamental ; l'électron
est séparé avec une énergie cinétique nulle.
**Fig.16** (image) « Niveaux d'énergie de l'atome d'hydrogène » : axe Énergie (eV) ; 0 (État ionisé, mention
« −∞ » sur le trait [sic]) ; −Eo/25 (n=5) ; −Eo/16 (n=4) ; −Eo/9 (n=3) ; −Eo/4 (n=2) ; −Eo (n=1, niveau
(ou état) fondamental) ; n = 2…5 « Niveaux (ou états) excités » ; flèche n=2 → n=1 étiquetée
« ΔE2,1 = E1 − E2 = h ν2,1 ».

**4.4 Interprétation des raies d'émission** (p.258–259) — relations (image) :
- apport d'énergie (rayonnement, collision avec un atome ou une particule) : passage n → p (p > n), l'atome
  absorbe juste **ΔEn,p = Ep − En = −13,6/p² + 13,6/n² = 13,6 (1/n² − 1/p²)** ;
- désexcitation p → n (p > n) : restitue **ΔEp,n = En − Ep** en émettant un photon d'énergie
  **hν = − ΔEp,n**.
Questions : 1°) calculer ΔE2,1 = (E1 − E2), ν2,1, λ2,1 ; domaine ? de même pour toutes les transitions vers
n = 1 ? 2) ΔE3,2 = E2 − E3 = h ν3,2, ν3,2, λ3,2 ; domaine ? de même vers n = 2 ? 3) montrer que les raies
d'émission « observées sur la figure 16 » correspondent aux transitions aboutissant à n = 2 [?] ; 4) domaine
des transitions aboutissant à n = 3, 4, 5.
Interprétation : **ΔEp,n = Eo (1/n² − 1/p²) = hνp,n** (image) ;
- n = 1, p = 2 : ΔE2,1 = E2 − E1 = 10,2 eV = 16,32.10⁻¹⁹ J ; ν2,1 = 2,4.10¹⁵ Hz ; λ2,1 = c/ν2,1 = 121 nm ;
  pour tout p > 2, νp,1 > ν2,1 → **série de Lyman**, « série de raies invisibles » (UV) ;
- vers n = 2 : **ΔEp,2 = − Eo (1/2² − 1/p²)** ; p = 3 : ΔE3,2 = E2 − E3 = − 1,88 eV = − 3,02.10⁻¹⁹ J,
  ν3,2 = 4,5.10¹⁴ Hz, λ3,2 = 656 nm (Hα rouge orangée) ; λ4,2 = 486 nm (Hβ), λ5,2 = 434 nm (Hγ),
  λ6,2 = 410 nm (Hδ) → **série de Balmer**.
Question : montrer par un calcul similaire que les transitions aboutissant à n = 4, 5 ou 6 donnent des
radiations infrarouges. Séries infrarouges : retour vers n = 3 **Paschen**, n = 4 **Brackett**, n = 5
**Pfund**. Fig.17 (image) : diagramme n = 1…6 et n = ∞, flèches groupées Lyman (→1), Balmer (→2), Paschen
(→3), Bracket[t] (→4), Pfund (→5).

**4.5 Interprétation des raies d'absorption** (p.259–260) — atome dans l'état En recevant un photon hν :
- énergie insuffisante pour ioniser : si elle correspond exactement à une transition En → Ep (p > n), la
  radiation est absorbée, **ΔEn,p = Ep – En = hν** (raie noire à la fréquence ν) ; sinon le photon n'est pas
  absorbé mais **diffusé** (renvoyé avec la même énergie dans une direction a priori quelconque) ;
- énergie ≥ énergie d'ionisation Ei : le photon peut être absorbé ; une partie ionise l'atome, le reste est
  transféré en énergie cinétique à l'électron éjecté ; « un photon d'énergie quelconque peut être absorbé
  par l'atome d'hydrogène pourvu que cette énergie soit au minimum égale à l'énergie d'ionisation ».

**5 Applications** (p.260–261)
- **5.1 En chimie** : le spectre d'une source = ensemble des spectres de ses éléments → analyse élémentaire ;
  alliage passé à l'arc électrique : position des raies → identification, intensités → pourcentages ;
  spectres d'absorption → identification des molécules.
- **5.2 En astrophysique** : régions internes très chaudes → spectre continu ; régions superficielles plus
  froides → absorbant ; spectre d'étoile = continu + nombreuses raies noires (Fig.18). Renseigne sur :
  **température** (plus l'étoile est chaude, plus son spectre s'étend vers le violet ; étoiles froides
  presque invisibles 1000 °C, rouges Bételgeuse 2500 °C, jaunes Soleil 5500 °C, blanches Sirius 10000 °C,
  bleues Rigel 20000 °C) ; **composition chimique** (raies d'absorption des couches superficielles ; raies
  d'autant plus noires que l'élément est plus abondant ; Fig.19 spectre solaire, absorption par la
  chromosphère : H, He, Na, Fe, Hg…) ; **vitesse** (effet **Doppler-Fizeau** : étoile qui s'éloigne →
  fréquence diminue, longueur d'onde augmente, déplacement vers le rouge ; qui se rapproche → vers le
  violet ; la mesure de Δν conduit à la vitesse — qualitatif, aucune formule).

### Encadrés, lois, relations (vérifiés sur l'image)
- F⃗_T/S = − G (mM/r²) u⃗_TS = − F⃗_S/T (p.248) ; F⃗_A/B = k (q_A q_B/r²) u⃗_AB = − k (e²/r²) u⃗_AB = − F⃗_B/A,
  k = 9.10⁹ N.m².C⁻² (p.249).
- W = h.c/λ = h.ν ; h = 6,62.10⁻³⁴ J.s (p.256).
- En = −E0/n² (eV), E0 = 13,6 eV, n ≥ 1 ; 1 eV = 1,6.10⁻¹⁹ J (p.257 [coquille], p.262).
- ΔEn,p = Ep − En = 13,6(1/n² − 1/p²) ; ΔEp,n = En − Ep ; hν = −ΔEp,n (p.258) ; ΔEp,n = Eo(1/n² − 1/p²) = hνp,n
  (p.258) ; ΔEp,2 = −Eo(1/2² − 1/p²) (p.258).
- Valeurs : Hg, transfert 4,9 eV (Franck-Hertz) ; H : 10,2 eV ; 121 nm ; 656 / 486 / 434 / 410 nm.

### L'essentiel (p.262, verbatim, encadrés lus sur l'image)
- « L'énergie de l'atome est **quantifiée**, c'est-à-dire qu'elle ne peut prendre qu'une suite de valeurs
  discrètes. »
- « Dans son état fondamental (état le plus stable), un atome est à son plus bas niveau d'énergie. En lui
  apportant de l'énergie, un atome peut se trouver dans l'un de ses états excités. »
- « On appelle transition atomique tout passage de l'atome d'un niveau d'énergie à un autre. »
- « Lors de l'absorption d'un photon d'énergie hν, l'atome passe d'un niveau d'énergie En à un niveau
  d'énergie Ep supérieure. L'énergie de l'atome varie de [ΔEn,p = Ep − En = hν]. »
- « Lors de l'émission d'un photon d'énergie hν, l'atome passe d'un niveau d'énergie Ep à un niveau d'énergie
  En inférieure. L'énergie de l'atome varie de [ΔEp,n = En − Ep = − hν]. »
- « L'énergie quantifiée de l'atome d'hydrogène est : [En = − E0/n²] en eV, avec n nombre entier supérieur
  ou égal à 1 et E0 = 13,6 eV. »
- « Toute radiation lumineuse de fréquence ν est émise sous forme d'un flux de photons, particules sans
  masse et d'énergie élémentaire W = hν. »
- « Dans un spectre d'émission ou d'absorption, chaque raie représente une transition d'un niveau Ep à un
  niveau En produite par l'émission ou l'absorption d'un photon de fréquence ν telle que : [|Ep − En| = hν]. »
- « Le spectre d'émission ou d'absorption d'un atome constitue «sa carte d'identité». »

### Exercice résolu (p.263)
Énoncé : En = − 13,6/n² (en eV). 1°) E1, E2, E3 ; 2°) nom du premier niveau ; 3°) pour quel n En est nulle,
état de l'atome ; 4°) fréquence émise de E2 à E1 ; 5°) longueur d'onde, domaine spectral. Données :
h = 6,62.10⁻³⁴ J.s, c = 3.10⁸ m.s⁻¹, 1 eV = 1,6.10⁻¹⁹ J.
Solution : 1°) E1 = − 13,60 eV, E2 = − 3,40 eV, E3 = − 1,51 eV ; 2°) niveau fondamental ; 3°) n → ∞, atome
ionisé (H⁺) ; 4°) hν2,1 = E2 − E1, ν2,1 = (E2 − E1)/h, A.N. ν2,1 = 2,46.10¹⁵ Hz ; 5°) ν2,1 = c/λ2,1 ⇔
λ2,1 = c/ν2,1, A.N. λ2,1 = 122 nm, ultraviolet (U.V).

### Exercices à résoudre (p.264–267 ; réponses p.317)
**Tests rapides des acquis**
1. *Vrai/faux* (7 items) : quantification expliquée par la mécanique de Newton ; énergie variant de façon
   continue ; énergie du fondamental maximale ; fournir Ep − En pour aller de En à Ep ; photon ionisant H
   fondamental d'énergie > 13,6 eV ; fondamental pour n → ∞ ; quanta 6 eV, 12,7 eV, 15 eV fournis à H
   fondamental, « 6 eV et 12,7 eV sont absorbés ». — Pas de réponse au manuel.
2. *QCM* (une ou plusieurs justes, 6 items) : énergie de l'atome (quantifiée / discontinue / quelconque) ;
   fréquences émises vs absorbées par un gaz (égales / différentes / plus grandes) ; atome fondamental peut
   (émettre / absorber un photon / émettre plusieurs) ; deux éléments différents (même spectre d'absorption /
   jamais le même spectre / même spectre d'émission) ; énergie minimale d'ionisation de H (15 / 13,6 /
   10,4 eV) ; fréquence νn,p émise de En vers Ep (a h(En − Ep) ; b h/(En − Ep) ; c (En − Ep)/h). — Pas de
   réponse au manuel.
**Exercices d'application**
3. H fondamental peut-il absorber 1°) un photon de 8,8 eV ? 2°) un photon λ = 632 nm ? Données E1 = −13,6 ;
   E2 = −3,4 ; E3 = −1,51 ; E4 = −0,85 eV. — Rép. : 1°) non ; 2°) non.
4. Mercure : E3 = −2,72 ; E2 = −3,4 ; E1 = −4,99 ; E0 = −10,45 eV (fondamental). 1°) énergies des photons
   E3→E1 et E2→E0 (eV et J) ; 2°) λ3,1 et λ2,0 ; 3°) dispositif d'observation d'un spectre de raies
   d'émission. — Rép. (étiquettes du manuel) : E4,2 = 2,27 eV = 3,63.10⁻¹⁹ J, E3,1 = 7,05 eV = 11,28.10⁻¹⁹ J ;
   λ4,2 = 547 nm, λ3,1 = 176 nm ; spectroscope à réseau [indices décalés, cf. Lecture].
**Exercices de synthèse**
5. En = −E0/n², E0 = 13,6 eV. 1°) énergies du fondamental, des trois premiers excités, de l'état ionisé ;
   diagramme ; 2°) quanta a) 6 eV b) 12,75 eV c) 18 eV fournis au fondamental : absorbés ? état ? 3°) λ dans
   le vide pour amener l'atome à n = 4 ; 4°) photon ionisant, électron émis avec une vitesse v : fréquence du
   photon incident (données h, c, 1 eV, m_e = 9,1.10⁻³¹ kg). — Rép. : E1 = −13,6 ; E2 = −3,4 ; E3 = −1,5 ;
   E4 = −0,85 ; E∞ = 0 ; 2°) c) ionisé ; λ4,1 = 97,3 nm ; νi = 3,29.10¹⁵ Hz.
6. Même relation. a) n au fondamental ; b) pourquoi des spectres de raies ; c) énergie d'ionisation (eV) ;
   d) λ pour aller du fondamental à n = 4, domaine ; e) λ émise lors de n = 2 → n = 1. — Rép. : n = 1 ;
   Ei = 13,6 eV ; λ4,1 = 97,3 nm ; λ2,1 = 121,7 nm.
7. En = −13,6/n². a) énergie d'ionisation ; b) Ec minimale d'un électron excitant par choc n=1 → n=2 ;
   c) λ du retour au fondamental ; d) relation littérale de la fréquence pour n > 2 → n = 2, série, plus
   grande λ. — Rép. : Ei = 13,6 eV ; E2,1 = 10,2 eV ; λ2,1 = 121,7 nm ; νn,2 = (En − E2)/h, série de Balmer,
   λ3,2 = 656,7 nm.
8. Diagramme « figure 1 » (image) : niveaux 0 ; −0,38 (n=6) ; −0,58 (n=5) ; −0,85 (n=4) ; −1,51 (n=3) ;
   −3,4 eV (n=2). 1°) a) niveau E = 0 ; b) énergie du fondamental ; c) énergie d'ionisation ; 2°) flèches
   des transitions de Balmer et leurs énergies ; 3°) plus petite λ émise vers n = 2, visible ? (limites
   400–800 nm). — Rép. : ionisation ; E1 = −13,6 eV ; Ei = 13,6 eV ; λ6,2 = 411 nm.
9. Désexcitation E2 → E1, λ21 = 1,216.10⁻⁷ m, En = −E0/n² (E0 > 0). 1°) signification du signe négatif ;
   2°) expliciter E2, E1, relation avec ν21 ; 3°) E0 en J puis en eV ; transitions E3 → E1 (λ31) et E3 → E2
   (λ32) : calculer λ31 et ν31 ; relation entre ν31, ν32, ν21 ; calculer ν32. — Rép. : ν2,1 = 3/4.Eo/h ;
   ν3,2 = ν3,1 − ν2,1.
10. *Étude de texte* « Les quasars, des astres très lointains » (raie d'absorption Lyman alpha à 121,5 nm,
   nuages intergalactiques « cent mille fois mois [moins] denses qu'une bulle de savon »). 1°) intérêt des
   quasars ; 2°) schéma Ea, Eb (Eb > Ea) de l'émission et bilan énergétique ; 3°) domaine de Lyman alpha
   (UV / visible / IR). Données h, c, 1 eV, En = −E0/n². — Pas de réponse au manuel.

**En savoir plus (p.268–269)** — « Les modèles de l'atome » : chronologie 1675 (Picard) → 1854 (Geissler,
Plücker) → 1897 (Thomson, électron) → 1900 (Planck) → 1911 (Rutherford, feuille d'or) → 1913 (Bohr) → 1914
(Franck et Hertz valident Bohr) → 1924 (de Broglie) → 1926 (Schrödinger) → 1928 (Dirac) ; nuage de
probabilité, fonction d'onde. Culture, hors évaluation.

### Bornes de scope
✅ **Inclus**
- Variation continue de l'énergie d'un système macroscopique vs échec de la mécanique newtonienne pour
  l'atome (modèle planétaire de Rutherford, rayonnement d'une charge accélérée — qualitatif) ; expressions
  vectorielles des forces gravitationnelle et coulombienne comme rappel.
- Expérience de Franck et Hertz (vapeur de Hg, seuil 4,9 eV, chocs élastiques/inélastiques, lecture de la
  courbe N_C/N_e = f(Ec)) — qualitative, sans circuit électrique détaillé.
- Hypothèses/postulats de Bohr ; niveaux d'énergie, état fondamental, états excités, état ionisé,
  transition, diagramme de niveaux (lecture et tracé).
- Photon : W = hν = hc/λ ; quantum ; conversions eV ↔ J (1 eV = 1,6.10⁻¹⁹ J), h = 6,62.10⁻³⁴ J.s,
  c = 3.10⁸ m.s⁻¹.
- Hydrogène : En = −E0/n² (E0 = 13,6 eV) ; calcul de En, de ΔE = |Ep − En| = hν, de ν et λ pour une
  transition ; énergie d'ionisation 13,6 eV ; ΔE = E0(1/n² − 1/p²).
- Séries Lyman (UV), Balmer (visible : Hα 656, Hβ 486, Hγ 434, Hδ 410 nm), Paschen, Brackett, Pfund (IR) ;
  domaine UV / visible (400–800 nm, valeur des exercices) / IR.
- Conditions d'absorption : photon absorbé seulement s'il correspond exactement à une transition (sinon
  diffusé) ; au-delà de Ei, absorption avec électron éjecté portant l'excédent en énergie cinétique (Ex.5
  4° : hν = Ei + ½mv², via m_e).
- Excitation par choc électronique : Ec minimale = ΔE (Ex.7 b).
- Spectres continu / d'émission (raies) / d'absorption (cannelures), renversement des raies, « carte
  d'identité » ; identification d'un élément par superposition de raies.
- Appareillage : spectroscope, spectrographe, spectromètre ; disperseur réseau ou prisme ; montage S, C, F,
  L, R, E ; lampe spectrale (Hg, H) ; vapeur de sodium.
- Applications : analyse élémentaire (alliage à l'arc), spectre stellaire (température par extension vers le
  violet, composition, abondance par noirceur des raies, spectre solaire/chromosphère), effet Doppler-Fizeau
  qualitatif (rouge = éloignement, violet = rapprochement).
- Niveaux d'autres atomes (Hg) donnés numériquement dans l'énoncé.

⛔ **Exclu**
- Démonstration de En = −E0/n² (rayon de Bohr, quantification du moment cinétique, rn = n²r1) : absente.
- Constante de Rydberg, formule de Balmer/Ritz nommée, 1/λ = R_H(…) : absentes.
- Formule quantitative de l'effet Doppler (Δν/ν = v/c) ; calcul de vitesse d'étoile ; loi de Wien /
  corps noir quantitative : absents (température seulement qualitative).
- Relation du réseau (sin θ = kλ/a…) et dispersion quantitative du prisme (traitées au chap. 8 ou absentes).
- Effet photoélectrique, travail d'extraction ; laser / émission stimulée ; fluorescence ; spectres
  moléculaires détaillés.
- Atomes polyélectroniques au-delà de niveaux donnés ; spin, nombres quantiques ℓ, m ; mécanique
  ondulatoire (Schrödinger, de Broglie, Dirac — seulement « En savoir plus »).
- Dispositif électrique de Franck-Hertz (grille, tension retardatrice, courbe I = f(U) à plusieurs pics) :
  le manuel ne donne qu'une courbe à un seul seuil.
- Noyau, radioactivité, énergie de liaison (chap. 10–11).

### Lecture
- **Couche texte** : p.244–269 intégralement, plus p.316–318 (réponses ; p.316 = chap. 1–4, p.318 = sites
  web, rien pour le chap. 9 ; réponses du chap. 9 en p.317 colonne droite).
- **Image (110 dpi)** : p.246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261,
  262, 263, 264, 265, 266, 267, 317 — **23 pages** ; zooms 220–300 dpi : p.257 (formule En), p.317
  (réponses chap. 9). Non vues en image : p.244, 245 (ouverture de partie), 268, 269 (prose « En savoir
  plus »).
- **Sondage / écarts texte → image constatés** : toutes les relations vectorielles (p.248–249) absentes ou
  vides dans la couche texte ; « W = h. c = h. » (p.256) sans λ ni ν ; « En = /n2 » (p.257) ; formules de
  4.4 (p.258) désarticulées ; encadrés de l'Essentiel (p.262) rendus sans signe « − » pour En ; QCM 6
  (p.264) fractions éclatées ; Ex.4 (p.265) colonnes entrelacées ; Ex.9 « λ21 » et « E2 → E1 » (flèches)
  perdus ; Fig.5, 7, 16, 17 et diagramme de l'Ex.8 (valeurs −0,38/−0,58/−0,85/−1,51/−3,4) uniquement sur
  l'image ; indices et exposants (10⁻¹⁹, 10¹⁵, ν2,1) aplatis partout.
- **Doutes / coquilles du manuel [?]**
  - p.257 : formule imprimée « En = En/n² » sans signe moins — retenu En = −E0/n² (Essentiel p.262 et
    exercices).
  - Signes incohérents : Q1 p.258 « ΔE2,1 = (E1 − E2) », Fig.16 « ΔE2,1 = E1 − E2 = hν2,1 » vs
    interprétation « ΔE2,1 = E2 − E1 = 10,2 eV » ; p.259 « ΔE3,2 = E2 − E3 = −1,88 eV » (négatif) ; à
    harmoniser par |Ep − En| = hν (Essentiel).
  - Valeurs arrondies divergentes : λ2,1 = 121 nm (cours) / 122 nm (exercice résolu) / 121,7 nm
    (réponses) ; ν2,1 = 2,4.10¹⁵ / 2,46.10¹⁵ Hz ; Hδ 410 nm (cours) vs λ6,2 = 411 nm (rép. Ex.8).
  - p.258 Q3 renvoie aux « raies d'émission observées sur la figure 16 » — la figure 16 est le diagramme de
    niveaux ; les raies observées sont celles de la Fig.11b [?].
  - Fig.12 légendée « spectre d'émision » alors qu'elle illustre l'absorption ; le montage photographié
    (lame de verre + alcool + eau salée) diffère du texte (« on fait brûler du sodium »).
  - Ex.4 : réponses étiquetées E4,2/E3,1, λ4,2/λ3,1 alors que l'énoncé demande E3→E1 et E2→E0 (valeurs
    2,27 eV et 7,05 eV cohérentes avec E3 − E1 et E2 − E0) ; l'énoncé donne aussi E2 = −3,4 eV pour le
    mercure (même valeur que H n=2) [?].
  - Ex.5 4°) : « vitesse v » sans valeur numérique ; la réponse νi = 3,29.10¹⁵ Hz correspond au seuil
    (13,6 eV/h), soit v = 0 [?].
  - Ex.9 3°) : symbole λ31 manquant dans « émet une radiation de longueur d'onde [ ] de même » (image).
  - Ex.1, 2, 10 et Ex.6 b), Ex.8 2°) : pas de réponse au manuel. Ex.1 item 7 et Ex.5 2°) : le manuel ne
    tranche pas explicitement (rép. Ex.5 2° : seulement « c) ionisé »).
  - p.252 : dates de Bohr imprimées « (1855-1962) » [coquille probable, non reprise]. Ex.10 « mois denses »
    pour « moins denses ».
  - Fig.17 : « Bracket » imprimé dans le diagramme, « Brackett » dans le texte.

## 2.10 Chapitre 10 — Le noyau atomique (manuel 223433, p.270–283)

Partie « Physique atomique et nucléaire » (bandeau de toutes les pages). Réponses du chapitre : p.317
(colonne droite, bloc « Chapitre 10 ») ; p.316 (chapitres 1 à 4) et p.318 (« Sites Web intéressants »)
ne contiennent rien de propre au chapitre 10.

**Page objectifs / prérequis (p.270)** — encadrés lus sur l'image.
- **Objectifs** : « Appliquer la relation d'Einstein : E = mc². » · « Evaluer en u et en MeV.c⁻², le défaut
  de masse résultant de la formation d'un noyau. » · « Evaluer l'énergie de liaison d'un noyau et son
  énergie de liaison par nucléon. » · « Comparer la stabilité de deux ou plusieurs noyaux connaissant les
  valeurs de leur énergie de liaison par nucléon. »
- **Prérequis — SAVOIR** : citer les ordres de grandeur de la masse et de la dimension d'un noyau ;
  énumérer les constituants d'un noyau ; définir un élément chimique ; définir les isotopes d'un élément
  chimique ; définir le nombre de masse et le nombre de charge ; définir l'interaction forte.
- **Prérequis — SAVOIR FAIRE** : convertir, en électron-volts, une énergie exprimée en joules et
  inversement ; écrire le symbole d'un noyau atomique connaissant sa composition et inversement ;
  reconnaître des isotopes ; expliquer la cohésion du noyau atomique.

**Page d'ouverture (p.271)** — « LE NOYAU ATOMIQUE » / « 10 ». Deux photos (cyclotron vu de l'extérieur ;
intérieur à électrodes en « D » avec une règle posée dessus), légende : « Le cyclotron est un exemple
d'accélérateur de particules utilisé au laboratoire pour le développement des recherches sur le noyau
atomique. » Questions d'accroche :
- « Que signifie la formule emblématique (E = mc²) citée couramment pour évoquer Einsteïn ? »
- « Qu'est-ce qui rend certains noyaux atomiques naturels plus ou moins stables que d'autres ? »
- « Qu'est-ce qui fait de l'uranium un élément chimique précieux dans le domaine du nucléaire ? »
  (Cette 3ᵉ question n'est pas reprise dans le chapitre ; l'uranium n'y apparaît que comme exemple de
  noyau lourd.)

**Introduction (p.272, titre « NOYAU ATOMIQUE »)** : « On sait que l'atome, cette plus petite entité
insécable de la matière et électriquement neutre, est constitué d'une partie centrale chargée
positivement (le noyau) et d'un cortège de très petites particules chargées négativement et en mouvement
rapide et incessant (les électrons). Ce chapitre a pour objet l'étude du noyau : structure, cohésion et
stabilité. »

**Plan du chapitre** (titres numérotés du manuel) :
1. Structure et cohésion du noyau (Rappels) — p.272–273
2. Équivalence masse-énergie — 2.1 Défaut de masse (p.273–274) ; 2.2 L'énergie de masse (p.274–275)
3. Stabilité du noyau — 3.1 Énergie de liaison (p.275–276) ; 3.2 Énergie de liaison par nucléon (p.276) ;
   3.3 Influence du nombre de masse (p.276–277)
- puis « L'essentiel » (p.278) · « Exercices » : Exercice résolu (p.279) ; Exercices à résoudre — Tests
  rapides des acquis : 1 Items « vrai ou faux », 2 QCM (p.280) ; Exercices d'application 3 à 7 (p.281) ;
  Exercices de synthèse 8 à 12 (p.281–282) · « En savoir plus » (p.283).

### Cours — activités et contenus

**1 STRUCTURE ET COHÉSION DU NOYAU (Rappels)** (p.272–273)
- **Activité (tableau + questions), p.272** — « Dans le tableau ci-dessous, on donne les masses de quatre
  atomes et celles de leurs noyaux » (tableau lu sur l'image) :

  | Atome ou noyau | Symbole | Masse du noyau (10⁻²⁷ kg) | Masse de l'atome (10⁻²⁷ kg) |
  |---|---|---|---|
  | Hélium 4 | ⁴₂He | 6,6447 | 6,6465 |
  | Carbone 12 | ¹²₆C | 19,9211 | 19,9266 |
  | Carbone 14 | ¹⁴₆C | 23,2476 | 23,2531 |
  | Uranium 235 | ²³⁵₉₂U | 390,1989 | 390,3021 |

  Questions : 1°) comparer les masses des atomes avec celles de leurs noyaux, conclure ; 2°) a) quels
  nombres de particules désigne-t-on par Z et A dans le symbole ᴬ_Z X ; b) pourquoi appelle-t-on Z nombre
  de charge et A nombre de masse ; c) le nombre de charge Z d'un noyau peut-il être différent du numéro
  atomique de l'élément correspondant ? 3°) qu'est-ce qui différencie les noyaux de carbone du tableau ?
  4°) « Malgré la répulsion due aux forces électrostatiques s'exerçant entre les protons, le noyau est un
  édifice stable de protons et de neutrons. Expliquer le caractère répulsif de cette interaction électrique
  ainsi que la cohésion du noyau. »
- **Contenu (conclusion du manuel), p.272–273, verbatim** :
  - « Le noyau atomique est constitué de protons et de neutrons appelés nucléons. On caractérise le noyau
    par le nombre de masse A, nombre total de ses nucléons et par le nombre de charge Z, nombre total des
    protons, d'où le symbole ᴬ_Z X. »
  - « Le noyau est d'une dimension 100000 fois plus petite que celle de l'atome dont le rayon est de
    l'ordre de 100 pm. Malgré sa petitesse, il renferme la quasitotalité de la masse de l'atome dont il
    fait partie. »
  - « Il existe des noyaux de même nombre de charge Z mais de nombre de masse A différents : ce sont les
    noyaux d'isotopes de numéro atomique Z. Un élément chimique naturel peut exister sous la forme d'un
    mélange isotopique de composition bien déterminée. »
  - « La cohésion du noyau est due à une interaction forte qui permet de maintenir les protons ensemble
    malgré leur répulsion. L'expérience montre que des forces nucléaires (forces de courte portée)
    s'exercent entre tous les nucléons du noyau indépendamment de leur nature (protons ou neutrons). A une
    même distance, ces forces attractives sont 100 fois plus intenses que les forces coulombiennes
    répulsives. C'est pour cette raison que les forces nucléaires gouvernent le noyau atomique dont elles
    assurent sa cohésion. »
  - **Remarque** : « La notation symbolique ᴬ_Z X est utilisée aussi pour représenter les particules
    élémentaires. Ainsi, le propton [sic] est représenté par ¹₁p, le neutron par ¹₀n. »

**2 ÉQUIVALENCE MASSE-ÉNERGIE**

**2.1 Défaut de masse** (p.273–274)
- **Exemple (activité), p.273** : noyau de lithium ⁷₃Li de masse m₀ = 7,01435 u, initialement au repos.
  Questions : 1°) sachant que l'unité de masse (u) est par définition le douzième de la masse d'un atome de
  carbone 12, montrer qu'elle est égale à 1,66.10⁻²⁷ kg ; 2°) a) calculer en u la masse totale m de ses
  nucléons à l'état libre et au repos ; b) comparer m₀ à m ; 3°) calculer Δm = m − m₀ ; 4°) « Δm = m − m₀
  s'appelle le défaut de masse du noyau. Justifier cette appellation. » Données : m_C (atome de
  carbone 12) = 19,93.10⁻²⁷ kg ; m_p = 1,007276 u ; m_n = 1,008665 u. (Pas de valeur numérique de
  réponse imprimée.)
- **Conclusion du manuel (p.274)** : « la masse m₀ d'un noyau, immobile, est inférieure à la masse totale
  m de ses nucléons pris séparément et au repos, ce qui nous laisse penser que la formation d'un noyau en
  ses nucléons pris isolément s'accompagne d'une perte de masse Δm = m − m₀ c'est le défaut de masse. »
  [sic : « formation d'un noyau en ses nucléons »]
- **Encadré Définition (p.274, verbatim, vérifié sur l'image)** : « Le défaut de masse Δm d'un noyau est
  égal à la masse de ses nucléons, pris séparément et au repos, diminuée de la masse du noyau.
  Pour un noyau de symbole ᴬ_Z X :
  **Δm( X ) = Zm_p + (A-Z)m_n − m_X**
  ou [sic] m_X est la masse du noyau, m_p celle du proton et m_n celle du neutron. »
- **Remarque** : « D'après cette définition, le défaut de masse est une grandeur positive. »

**2.2 L'énergie de masse** (p.274–275)
- Question d'introduction : « Un noyau n'étant constitué que de protons et de neutrons, on s'attendait à ce
  que sa masse soit simplement égale à celle de ses constituants. Mais ce n'est pas le cas : l'apparition
  d'un défaut de masse notable est fort surprenant. En quoi est convertie la masse manquante ? »
- **Principe d'Einstein (verbatim, en gras italique sur l'image)** : « Pour Einstein, la masse est une forme
  d'énergie potentielle. Il postula, en 1905, le principe suivant : “Tout corps au repos dans un référentiel
  donné possède du seul fait de sa masse m, une énergie potentielle appelée énergie de masse donnée par la
  relation : **E₀ = m c²** où c représente la célérité de la lumière dans le vide” »
- « Cette relation, connue sous le nom de relation d'Einstein, traduit une équivalence entre la masse et
  l'énergie : de l'énergie peut se transformer en masse, c'est-à-dire se matérialiser sous forme de
  particule ; inversement la masse peut être convertie en énergie. Par conséquent, tout défaut de masse
  équivaut à une variation d'énergie potentielle de masse : **ΔE = Δmc²**. »
- Encart portrait : « Albert Einstein (1879-1955) : l'un des grands esprits scientifiques. Il publia, en 1905
  entre autres, les bases de la théorie de la relativité ; Il obtient le prix Nobel en 1921 et il est élu
  savant du siècle en 2000. »
- **Remarque (p.275)** : « Vu que l'unité usuelle de l'énergie est le MeV, d'après la relation d'Einstein,
  la masse m a la dimension d'une énergie par c² : c'est le MeV.c⁻². En particulier, 1u vaut environ
  931.5 MeV.c⁻². »

**3 STABILITÉ DU NOYAU** (p.275–277)
- Introduction : « Tout noyau a une masse m au repos, dans un référentiel donné, inférieure à la masse
  totale de ses constituants (nucléons). Par conséquent, ce défaut de masse qui varie d'un noyau à l'autre
  a-t-il une influence sur leur stabilité ? »

**3.1 Énergie de liaison** (p.275–276)
- **Encadré Définition (verbatim)** : « L'énergie de liaison, notée E_ℓ, est l'énergie qu'il faut fournir à
  un noyau au repos pour le dissocier en nucléons isolés et immobiles. »
- **Question (activité)** : « En utilisant la relation d'Einstein et le principe de la conservation de
  l'énergie, montrer que l'énergie de liaison d'un noyau ᴬ_Z X s'écrit : E_ℓ = Δm.c². »
- **Mise en évidence (démonstration du manuel, formules lues sur l'image)** : dissociation de ᴬ_Z X en ses
  nucléons, toutes les particules au repos (« leur énergie de liaison [sic, lire : leur énergie] est
  purement de masse ») ;
  avant : E₁ = m_X.c² (énergie de masse du noyau) ; après : E₂ = Z.E_p + (A-Z).E_n (énergie de masse des
  nucléons) ; or E_p = m_p.c² et E_n = m_n.c², d'où E₂ = (Z m_p + (A-Z) m_n).c² ; vu que
  Z m_p + (A-Z) m_n > m_X, E₂ > E₁, donc E₁ ne peut être l'énergie totale du noyau ; « Le plus qu'il faut
  ajouter est l'énergie E_ℓ qu'il faut apporter de l'extérieur afin de pouvoir dissocier le noyau. » ;
  conservation de l'énergie : **E_ℓ + E₁ = E₂**, d'où E_ℓ = E₂ − E₁,
  **E_ℓ = (Z m_p + (A − Z) m_n).c² − m_X.c² = Δm(X).c²**.
  « Ainsi, l'énergie de liaison d'un noyau est la différence entre la somme des énergies de masse de ses
  nucléons pris séparément et son énergie de masse. »
- **Encadré Conclusion (verbatim)** : « L'énergie de liaison d'un noyau est une traduction énergétique de son
  défaut de masse : **E_ℓ = Δm.c²**. »

**3.2 Énergie de liaison par nucléon** (p.276)
- Motivation : « on ne peut se fier à la valeur de l'énergie de liaison parce que tous les noyaux n'ont pas
  le même nombre de nucléons. On recourt à l'énergie de liaison par nucléon. »
- **Encadré Définition (verbatim)** : « L'énergie de liaison par nucléon, notée E_ℓ/A est l'énergie moyenne
  de liaison E_ℓ par nucléon. »
- **Propriété (verbatim)** : « L'énergie de liaison E_ℓ d'un noyau est pratiquement proportionnelle au nombre
  total A des nucléons constitutifs. Alors, E_ℓ/A peut se calculer comme étant le quotient de l'énergie de
  liaison E_ℓ par le nombre de masse A. » — **E_ℓ / A = E_ℓ / A** (fraction : E_ℓ sur A).

**3.3 Influence du nombre de masse** (p.276–277)
- **Figure : courbe d'Aston (p.276, lue sur l'image, zoom 220 dpi)** : ordonnée « E_ℓ / A (MeV) » de 0 à 9,
  **valeurs positives** (courbe tracée « en cloche » vers le haut) ; abscisse A de 0 à ~205 (graduations
  40, 80, 120, 160, 200). Noyaux étiquetés : ²₁H (≈ 1 MeV), ⁶₃Li (≈ 6,7), ¹²₆C (≈ 7,7), ¹⁶₈O (≈ 8),
  ⁵⁶₂₆Fe (≈ 8,7–8,8, sommet), ¹²⁰₅₀Sn (≈ 8,5), ¹⁸⁴₇₄W (≈ 8,1), ²⁰⁸₈₂Pb (≈ 7,9) ; un pic aigu vers
  A ≈ 4 (≈ 7) et un autre vers A ≈ 12–14 (≈ 8,4). (Valeurs lues à l'œil sur la grille : approximatives.)
- Texte (verbatim, p.277) : « La courbe d'Aston est caractérisée par : – un niveau zéro de l'énergie
  correspondant aux nucléons séparés et au repos. – un minimum d'énergie (30 < A < 80) correspondant aux
  noyaux dont les nucléons sont les plus liés, donc les plus stables. Ainsi, la courbe d'Aston permet
  d'illustrer la stabilité relative des noyaux. Les noyaux légers (A < 20) et les noyaux lourds (A > 190)
  sont instables car ils ont une faible énergie de liaison par nucléon tandis que les noyaux de nombre de
  masse moyen (voisin de 60) sont stables parce qu'ils ont l'énergie de liaison par nucléon la plus
  élevée. » [? « minimum d'énergie » se rapporte à une courbe −E_ℓ/A ; la courbe imprimée est en +E_ℓ/A et
  présente un MAXIMUM — incohérence interne du manuel, voir Doutes.]
- **Exemple** : « Ayant un nombre de masse A = 56, l'isotope du fer est très stable, ce qui explique sa très
  grande abondance (91,68%) dans la nature. »
- **Remarque** : « Etant particulièrement stables, les cinq noyaux légers vérifiant A = 2Z font
  l'exception. »
- **Encadré Conclusion (verbatim)** : « Un noyau est d'autant plus stable que son énergie de liaison par
  nucléon est plus grande. Les noyaux naturels les plus stables sont ceux de nombre de masse voisin de 60 :
  7,8 MeV < E_ℓ /A < 8,8 MeV. »

### L'essentiel (p.278, verbatim, chaque formule encadrée vérifiée sur l'image, zoom 220 dpi)

- « Une particule de masse m, au repos dans un référentiel donné, a une énergie de masse :
  **E₀ = m c²** avec c la célérité de la lumière dans le vide. C'est la relation d'Einstein. »
- « La relation d'Einstein traduit l'équivalence masse-énergie. »
- « La masse est une forme d'énergie potentielle. »
- « La dissociation d'un noyau au repos ᴬ_Z X en nucléons séparés s'accompagne d'un défaut de masse :
  **Δm = Zm_p + (A − Z)m_n − m(ᴬ_Z X) équivalent à ΔE = Δmc²**. »
- « Le MeV et le MeV.c⁻² sont des unités respectivement d'énergie et de masse, adoptées à l'échelle du noyau
  de l'atome. » — encadré **1u = 931,5 MeV.c⁻²**
- « L'énergie de liaison d'un noyau ᴬ_Z X est l'énergie qu'il faut lui fournir quand il est au repos dans un
  référentiel donné, pour le dissocier en nucléons séparés et au repos dans le même référentiel. » —
  encadré **E(ᴬ_Z X) = Δm(ᴬ_Z X).c²** [sic : « E » sans indice ℓ dans l'encadré]
- « L'énergie de liaison par nucléon varie avec le nombre de masse A. Plus elle est élevée, plus le noyau est
  stable. » — encadré **E_ℓ / A(ᴬ_Z X) = [E_ℓ / A(ᴬ_Z X)] / A = Δm.c² / A** [sic : le numérateur de la
  fraction centrale est imprimé « E_ℓ / A(ᴬ_Z X) » au lieu de « E_ℓ(ᴬ_Z X) » — coquille ; transcrire
  E_ℓ/A = E_ℓ/A … = Δm.c²/A au sens de la propriété 3.2]
- « Les noyaux les plus stables sont ceux dont le nombre des nucléons constitutifs est voisin de 60, ils ont
  une énergie de liaison par nucléon de l'ordre de 8 MeV. »

### Exercice résolu (p.279)

**Énoncé** : noyau de radon ²²²₈₆Rn, m = 221,97028 u. 1°) a) signification de 86 et 222 ; b) composition ;
c) en déduire, en u, la masse des nucléons séparés. 2°) défaut de masse en u. 3°) a) énergie de liaison en
MeV ; b) énergie de liaison par nucléon en MeV. 4°) « L'énergie de liaison de l'uranium 238 est
E_ℓ = 1801,5 MeV. Montrer que l'uranium 238 est moins stable que le radon 222 bien que son énergie de
liaison est plus grande. » Données : 1u = 1,66.10⁻²⁷ kg = 931,5 MeV.c⁻² ; m_p = 1,00728 u ;
m_n = 1,00867 u.
**Solution** : 1°) a) 86 = nombre de charge Z, 222 = nombre de masse A ; b) 86 protons ; N = A − Z = 136
neutrons ; c) m = 86 m_p + 136 m_n ; A.N : m = 223,80529 u [? le calcul avec les données donne
223,80520 u]. 2°) Δm = m − m(²²²₈₆Rn) ; A.N : Δm = 1,83501 u. 3°) a) E_ℓ = Δm.c² ; E_ℓ = 1709,3 MeV ;
b) E_ℓ/A(²²²₈₆Rn) = E_ℓ(Rn)/222 ; A.N : 7,7 MeV. 4°) « Pour comparer les stabilités des deux noyaux, on
compare leurs énergies de liaison par nucléon et non leurs énergies de liaison. » E_ℓ/A(U) = E_ℓ(U)/238
= 7,57 MeV ; E_ℓ/A(Rn) > E_ℓ/A(U), donc le radon 222 est plus stable que l'uranium 238.

### Exercices à résoudre (p.280–282)

Aucune réponse imprimée pour les tests rapides (ex. 1 et 2). Les réponses p.317 sont numérotées 3 à 9 ;
leur contenu montre que **les n°8 et 9 de p.317 répondent aux exercices 10 (lanthane) et 11 (magnésium)**
— décalage de numérotation du manuel ; les exercices 8, 9 et 12 n'ont pas de réponse.

**1 Items « vrai ou faux »** (p.280) : 1- Le MeV.c⁻² est une unité de masse utilisée à l'échelle de
l'univers. 2- L'argon 40 et le potassium 40 sont des isotopes. 3- Les noyaux de deux isotopes ont la même
valeur de l'énergie de liaison par nucléon. 4- La masse d'un noyau est égale à la somme des masses de ses
nucléons libres et au repos. 5- La valeur de l'énergie de liaison d'un noyau lourd est plus grande que celle
d'un noyau léger. 6- Plus son énergie de liaison est élevée, plus le noyau est stable. 7- Entre deux noyaux,
celui qui a l'énergie de liaison moyenne par nucléon la plus faible est le plus stable. 8- La courbe d'Aston
permet de comparer la stabilité d'un noyau à celle d'un autre. 9- Tous les noyaux légers ayant un nombre de
masse A < 20 sont instables. 10- Tous les noyaux lourds ayant A > 200 sont instables. (Sans corrigé.)

**2 QCM** (p.280, « la (ou les) proposition(s) juste(s) ») : I- L'interaction forte : a- ne s'exerce pas
entre les neutrons, b- est de très courte portée, c- est de nature gravitationnelle. II- La masse d'une
particule : a- n'est une forme d'énergie que lorsqu'elle est en mouvement, b- est une forme d'énergie
potentielle, c- est une forme d'énergie cinétique. III- E_ℓ/A(²³⁸U, Z = 92) = 7,57 MeV, E_ℓ/A(bore 10,
Z = 5) = 6,48 MeV ; U 238 plus stable parce que : a- masse supérieure, b- son E_ℓ/A est la plus grande,
c- plus grand nombre de nucléons, d- son énergie de liaison est la plus grande. IV- Isotopes : même nombre
de a- protons, b- nucléons, c- neutrons, d- charge. V- Plus stable que : a- E_ℓ/A plus élevée, b- E_ℓ plus
élevée, c- défaut de masse plus faible. VI- L'énergie de liaison est : a- l'énergie libérée par le noyau
lorsqu'il se forme à partir de ses nucléons libres et au repos, b- l'énergie qu'il faut fournir à ce noyau
au repos … pour le dissocier en ses constituants au repos dans le même référentiel, c- l'énergie
équivalente au défaut de masse du noyau. (Sans corrigé.)

**Exercices d'application** — données communes : 1u = 1,66.10⁻²⁷ kg = 931,5 MeV.c⁻² ; m_p = 1,00728 u ;
m_n = 1,00867 u ; nombre d'Avogadro 𝒩 = 6,022.10²³.
- **Ex. 3** : masse en u d'un noyau ⁴₂He d'énergie de masse E₀ = 3727,4 MeV. — Réponse : m = 4,0015 u.
- **Ex. 4** : énergie de masse en MeV de ²³⁸₉₂U de masse m = 3,952.10⁻²⁵ kg. — Réponse :
  E₀ = 22,23.10⁴ MeV. [? réponse cohérente avec c = 3.10⁸ m.s⁻¹ et 1 MeV = 1,6.10⁻¹³ J, valeurs non
  données ; via 1u = 1,66.10⁻²⁷ kg = 931,5 MeV.c⁻² on obtient ≈ 22,18.10⁴ MeV]
- **Ex. 5** : isotopes ⁸⁵₃₇Rb (84,89144 u) et ⁸⁹₃₇Rb (88,89193 u) ; 1°) définir l'énergie de liaison ;
  2°) énergies de liaison puis par nucléon ; 3°) comparer les stabilités. — Réponses : E₈₅ = 739,685 MeV ;
  E₈₉ = 771,53 MeV ; E₈₅/A = 8,7 MeV ; E₈₉/A = 8,67 MeV ; Rb(85) plus stable que Rb(89).
- **Ex. 6** : ⁴₂He (noyau m₁ = 4,0015 u) ; 1°) composition ; 2°) défaut de masse ; 3°) énergie à fournir pour
  libérer ses nucléons ; 4°) avec ³He (m₂ = 3,0149 u) et ⁶He (m₃ = 6,0178 u), classer les trois isotopes
  « suivant leurs stabilité relative croissante ». — Réponses : 2p et 2n ; Δm = 0,0304 u ;
  E = 28,3176 MeV ; « He(4) > He(6) > He(3) » [ordre DÉCROISSANT imprimé alors que la question demande
  l'ordre croissant : même classement, sens inverse].
- **Ex. 7** : ²³⁸U (Z = 92), m = 238,0508 u ; 1°) symbole et composition ; 2°) énergie de liaison ;
  3°) E_ℓ/A en MeV ; 4°) énergie W en joules pour dissocier une mole d'uranium 238. — Réponses :
  E = 1755,67 MeV ; E/A = 7,377 MeV ; W = 1,7.10¹⁴ J. [L'exercice résolu donne pour U 238
  E_ℓ = 1801,5 MeV et E_ℓ/A = 7,57 MeV : valeurs différentes de celles de l'ex. 7 — à ne pas mélanger.]

**Exercices de synthèse**
- **Ex. 8** (p.281) : noyaux ¹⁶₈O (m₁ = 15,9950 u) et ⁴₂He (m₂ = 4,0026 u) ; 1°) E_ℓ/A de chacun ;
  2°) lequel est le plus stable ; 3°) courbe d'Aston fournie (même allure que p.276, sans étiquettes,
  ordonnée E_ℓ/A (MeV) 0–9, A 0–200) : la reproduire, y situer O et He, la position confirme-t-elle 2°) ?
  — Pas de réponse au manuel. [? m₂ = 4,0026 u est la masse de l'ATOME d'hélium 4, alors que l'ex. 6
  donne le noyau à 4,0015 u ; 15,9950 u est aussi une masse atomique]
- **Ex. 9** (p.282) : 1°) avec la courbe d'Aston de l'ex. 8, zone des noyaux les plus stables, en déduire le
  plus stable ; 2°) ¹²C et ²³⁸U : a) donner leur E_ℓ/A (lecture graphique) ; b) calculer leur énergie de
  liaison, en déduire que l'énergie de liaison ne permet pas de comparer leur stabilité. — Pas de réponse.
- **Ex. 10** (p.282) : 1°) définir l'énergie de liaison ; 2°) a) énergie de liaison de ¹³⁹₅₇La en joules
  puis en MeV ; b) E_ℓ/A ; 3°) courbe d'Aston assimilée, pour A ≥ 80, à une droite D : y = aA + b ;
  a) calculer y pour ⁸⁰₃₄Se et ²³⁵₉₂U, en déduire a et b ; b) vérifier la compatibilité avec 2°) à 0,1 MeV
  près. Données : m_La = 138,9060 u, m_U = 235,0439 u, m_Se = 79,9165 u. — Réponses (n°8 p.317) :
  E = 1136,337 MeV = 1818,14.10⁻¹³ J ; E/A = 8,175 MeV ; y_Se = 8,5 MeV ; y_U = 7,395 MeV ;
  y = −7,13.10⁻³ A + 9,07.
- **Ex. 11** (p.282) : magnésium, 12 protons et 12 neutrons, m_Mg = 23,97868 u ; 1°) symbole ;
  2°) expression de E_Mg en fonction de m_Mg et c ; 3°) E_p et E_n en MeV ; 4°) montrer que
  **E_ℓ = 12(E_p + E_n) − E_Mg** et la calculer en MeV. — Réponses (n°9 p.317) : E_Mg = m_Mg c² ;
  E_p = 938,28 MeV ; E_n = 939,576 MeV (valeur de E_ℓ non imprimée).
- **Ex. 12 — Étude de texte « Les noyaux naturels stables »** (p.282) : diagramme N = A − Z (0–150) en
  fonction de Z (0–90) : nuage des noyaux stables au-dessus de la droite Z = N, qui s'en écarte quand Z
  croît (lu sur l'image). Texte : interactions intranucléaires de rayon d'action très faible (« de l'ordre
  du fermi ») et à « décroissance exponentielle avec la distance entre nucléons » ; « un noyau stable, au
  delà de Z = 20, doit avoir un excès de neutrons (N > Z). Néanmoins, cette condition cesse d'être valable
  pour les noyaux de nombre charge au delà de 83. » Donnée : 1 fermi = 10⁻¹⁵ m. Questions : 1°) parmi les
  deux types d'interactions, celles de courte portée ; 2°) combinaisons de nucléons formant un noyau stable ;
  3°) pourquoi tout noyau vérifiant Z > N est qualifié d'instable ? — Pas de réponse.

### En savoir plus (p.283)

« De l'histoire du noyau atomique » : Rutherford (1911, feuille d'or et particules alpha, modèle planétaire ;
protons 1919), Chadwick (neutron, 1932) ; ≈ 260 noyaux stables (Z de 1 à 83, bismuth) ; radioactivité comme
retour à l'équilibre neutrons/protons ; accélérateurs (années 1930), ≈ 3000 noyaux observés, noyaux exotiques.
(Lecture culturelle, non évaluée ; pas de fiche technique dans ce chapitre.)

### Bornes de scope observées (chapitre 10)

- ✅ INCLUS :
  - **Structure du noyau** (rappels) : protons, neutrons, nucléons ; A (nombre de masse), Z (nombre de
    charge), N = A − Z ; symbole ᴬ_Z X, y compris ¹₁p et ¹₀n ; écrire un symbole depuis la composition et
    inversement ; ordres de grandeur (noyau 10⁵ fois plus petit que l'atome, rayon atomique ≈ 100 pm ;
    quasi-totalité de la masse) ; **isotopes** (même Z, A différents), mélange isotopique.
  - **Cohésion** : interaction forte attractive, courte portée (de l'ordre du fermi), indépendante de la
    nature des nucléons, 100 fois plus intense que la répulsion coulombienne à même distance (qualitatif).
  - **Unité de masse atomique** : u = 1/12 de la masse d'un atome de ¹²C = 1,66.10⁻²⁷ kg ;
    **1u = 931,5 MeV.c⁻²** ; MeV.c⁻² comme unité de masse.
  - **Défaut de masse** Δm = Zm_p + (A−Z)m_n − m_X (en u et en MeV.c⁻²), grandeur positive.
  - **Relation d'Einstein** E₀ = mc² (énergie de masse d'une particule au repos), ΔE = Δmc² ; calcul
    d'énergies de masse (MeV ↔ u ↔ kg ↔ J) ; E_p = m_p c², E_n = m_n c².
  - **Énergie de liaison** E_ℓ = Δm.c² (définition + démonstration par conservation de l'énergie) ;
    expression E_ℓ = Z E_p + (A−Z) E_n − E_X ; conversion MeV ↔ J ; énergie pour une mole (Avogadro, ex. 7).
  - **Énergie de liaison par nucléon** E_ℓ/A ; comparaison de stabilité par E_ℓ/A et non par E_ℓ
    (exercice résolu, ex. 9).
  - **Courbe d'Aston** (lecture qualitative et graphique) : zones A < 20 et A > 190 instables, A voisin de 60
    les plus stables (7,8 MeV < E_ℓ/A < 8,8 MeV, ordre 8 MeV), fer 56 ; exception des 5 noyaux légers
    A = 2Z ; situer un noyau sur la courbe ; modélisation affine y = aA + b pour A ≥ 80 (ex. 10 seulement).
  - **Diagramme (N, Z)** des noyaux stables et règle qualitative N > Z au-delà de Z = 20, limite Z = 83
    (étude de texte, ex. 12 seulement).
- ⛔ EXCLU (non traité dans ce chapitre) :
  - **Radioactivité** (α, β⁻, β⁺, γ), lois de conservation, loi de décroissance, demi-vie, activité —
    citée seulement dans « En savoir plus » ; relève du chapitre 11 « Réactions nucléaires ».
  - **Fission, fusion, énergie libérée par une réaction nucléaire**, bilan Q d'une réaction, centrales
    nucléaires, rôle de l'uranium (la 3ᵉ question d'accroche n'est pas traitée).
  - **Calcul avec la masse des électrons / passage masse atomique ↔ masse du noyau** : le tableau p.272
    ne sert qu'à une comparaison qualitative ; aucun calcul ne retranche Z m_e.
  - **Expression quantitative de l'interaction forte**, potentiel nucléaire, modèles du noyau (goutte
    liquide, formule de Weizsäcker, couches), relation N/Z quantitative.
  - **Relativité au-delà de E₀ = mc²** : énergie cinétique relativiste, quantité de mouvement, E² = p²c² + m²c⁴.
  - **Fonctionnement du cyclotron / des accélérateurs** et détecteurs (photos et lecture culturelle seules).
  - **Appareillage expérimental** : aucune manipulation ni fiche technique dans ce chapitre (cours
    entièrement par activités documentaires et calculs).
  - Valeurs de c et de la charge élémentaire : **non fournies** dans les « on donne » du chapitre
    (conversion J ↔ eV supposée connue, prérequis p.270).

### Doutes [?]

1. **Courbe d'Aston (p.276–277)** : le texte parle d'« un niveau zéro de l'énergie » et d'« un minimum
   d'énergie (30 < A < 80) » (lecture d'une courbe −E_ℓ/A), alors que la figure trace +E_ℓ/A avec un
   **maximum**. Côté auteur : présenter la courbe telle qu'imprimée (E_ℓ/A > 0, maximum vers A ≈ 60) et
   ne pas reprendre « minimum » sans expliquer le signe.
2. **Bornes de zones incohérentes** : « 30 < A < 80 » (minimum), « A voisin de 60 », « A < 20 » / « A > 190 »
   (p.277) mais V/F 10 « A > 200 » (p.280) ; l'Essentiel dit « de l'ordre de 8 MeV » et la conclusion
   « 7,8 MeV < E_ℓ/A < 8,8 MeV ».
3. **Essentiel p.278** : encadré E(ᴬ_Z X) sans indice ℓ ; fraction centrale « E_ℓ / A(X) / A » (coquille
   pour E_ℓ(X)/A).
4. **Numérotation des réponses p.317** : n°8 et 9 = exercices 10 et 11 ; ex. 8, 9, 12 et tests rapides sans
   corrigé.
5. **Ex. 6 4°)** : réponse donnée dans l'ordre décroissant pour une question en ordre croissant.
6. **Ex. 4** : réponse 22,23.10⁴ MeV obtenue avec c et e non donnés ; avec 1u = 931,5 MeV.c⁻² ≈ 22,18.10⁴ MeV.
7. **Ex. 8** : masses 4,0026 u et 15,9950 u = masses atomiques (cf. ex. 6 : noyau ⁴He = 4,0015 u).
8. **Exercice résolu** : m = 223,80529 u imprimé, 223,80520 u par le calcul (écart de 9.10⁻⁵ u, propagé
   dans Δm = 1,83501 u ; avec Δm = 1,83492 u on obtient E_ℓ = 1709,2 MeV, au lieu des 1709,3 MeV imprimés ; E_ℓ/A = 7,7 MeV est inchangé).
9. **Valeurs de U 238 divergentes** : exercice résolu (E_ℓ = 1801,5 MeV ; 7,57 MeV ; QCM III aussi 7,57 MeV)
   vs ex. 7 (1755,67 MeV ; 7,377 MeV, avec m = 238,0508 u). Ne pas réutiliser l'une avec les données de
   l'autre.
10. **Activité lithium (p.273)** : m_p et m_n donnés à 6 décimales (1,007276 / 1,008665 u) contre 5 décimales
    partout ailleurs (1,00728 / 1,00867 u) — conserver les valeurs propres à chaque énoncé.
11. Valeurs lues sur la courbe d'Aston (ⁿX ≈ …) : approximations à l'œil, non imprimées en nombres.

### Lecture

- **Pages lues en couche texte** (`/root/.cache/yqa-manuels/223433/txt/pNNN.txt`) : 270 à 283 (14 pages) et
  316, 317, 318.
- **Pages lues sur l'image** (110 dpi, `pdftoppm`) : **15** — 270, 271, 272, 273, 274, 275, 276, 277, 278,
  279, 280, 281, 282, 283, 317 ; plus 3 zooms à 220 dpi : courbe d'Aston p.276, encadrés de l'Essentiel
  p.278, bloc « Chapitre 10 » p.317. Non vues sur l'image : 316 et 318 (aucun contenu du chapitre 10,
  vérifié en couche texte).
- **Sondage image** : 100 % des pages du chapitre (14/14), dont les plus denses 272, 275, 276, 278, 279,
  281, 282. **Écarts texte/image constatés** :
  p.270 exposants perdus (« mc2 », « MeV.c-2 ») ; p.272 tableau éclaté (symboles ⁴₂He, ¹²₆C, ¹⁴₆C, ²³⁵₉₂U
  sur trois lignes, indices séparés des lettres), « A X / Z » cassé ; p.273 ¹₁p / ¹₀n rendus « 1 / 1p,
  01n », « 73 Li » ; p.274 indices de Δm(X) = Zm_p + (A−Z)m_n − m_X aplatis, E₀ = mc² en « Eo = m c2 » ;
  p.275 E_ℓ rendu « El » (indice ℓ perdu), ᴬ_Z X éclaté ; p.276 fraction « E_ℓ / A = E_ℓ/A » réduite à
  « E / A = E A » et **courbe d'Aston entièrement absente** de la couche texte ; p.278 tous les Δ perdus
  (« m = Zmp… », « E = mc 2 », « E( AZ X) = m( AZ X).c 2 ») et indices ℓ perdus — sans l'image, l'Essentiel
  serait faux ; p.279 solution : « m = m  m(222 86 Rn) » (Δ et signe moins perdus), fractions E_ℓ(Rn)/222
  et E_ℓ(U)/238 désarticulées, coquilles « charrge », « noyyau », « RN » ; p.280 « énegie » (sic aussi sur
  l'image) ; p.281 colonnes entremêlées (ex. 5 « 5 89 » mêle numéro et nombre de masse du Rb 89 ; ex. 3/7/8
  intercalés), courbe d'Aston de l'ex. 8 absente, 𝒩 d'Avogadro rendu « N » ; p.282 diagramme N = f(Z)
  absent (seules « N=A-Z » et « Z=N » subsistent), symboles ⁸⁰₃₄Se / ²³⁵₉₂U / ¹³⁹₅₇La éclatés ; p.317
  indices « E85/A », « He(4) » rendus correctement mais Δ de « Δm = 0,0304 u » conservé — seule page de
  réponses sans écart bloquant. Aucun écart ne change le sens des définitions en prose ; toutes les
  formules et figures de cette fiche viennent de l'image.

## 2.11 Chapitre 11 — Réactions nucléaires (manuel 223433, p.284–315)

Partie « Physique atomique et nucléaire » (bandeau de toutes les pages). Réponses du chapitre : p.317
(colonne droite, bloc « Chapitre 11 », exercices 4, 5, 6, 8, 10, 11 seulement) ; p.316 (chapitres 1 à 4)
ne contient rien du chapitre 11 ; p.318 (« Sites Web intéressants ») liste 11 sites sous la rubrique
« Physique atomique et nucléaire » (CEA, datation, familles radioactives…), sans contenu propre.

**Page objectifs / prérequis (p.284)** — encadrés lus sur l'image.
- **Objectifs** : « Justifier l'émission de rayonnements radioactifs. » · « Ecrire les équations des
  réactions nucléaires spontanées et celles des réactions nucléaires provoquées. » · « Appliquer la loi de
  désintégration pour des durées multiples de la période du radioélément. » · « Calculer l'activité d'un
  échantillon radioactif. » · « Distinguer les réactions nucléaires spontanées des réactions nucléaires
  provoquées. » · « Distinguer la fission de la fusion nucléaire. » · « Justifier la variation d'énergie
  accompagnant la fission et la fusion nucléaires. » · « Evaluer l'énergie libérée au cours des réactions
  nucléaires de fission et de fusion. »
- **Prérequis — SAVOIR** : donner la structure d'un atome ; définir les isotopes d'un élément chimique ;
  donner la composition du noyau atomique ; énumérer les caractéristiques des nucléons ; définir l'énergie
  de liaison d'un noyau et son énergie de liaison par nucléon ; définir un photon.
- **Prérequis — SAVOIR FAIRE** : reconnaître les isotopes ; écrire le symbole d'un noyau atomique
  connaissant sa composition et inversement ; évaluer, en u et en MeV.c⁻², le défaut de masse résultant de
  la formation d'un noyau ; calculer l'énergie de liaison d'un noyau et son énergie de liaison par nucléon ;
  comparer la stabilité de deux ou de plusieurs noyaux, connaissant les valeurs de leur énergie de liaison
  par nucléon. (= acquis du chapitre 10.)

**Page d'ouverture (p.285)** — « REACTIONS NUCLÉAIRES » / « 11 ». Trois photos (appareil d'imagerie
médicale ; site de centrale ; centrale avec tour de refroidissement), encadré : « En même temps que le
"nucléaire" est utilisé à des fins pacifiques, comme pour produire de l'électricité ou pour faire de
l'imagerie médicale, il peut avoir des effets catastrophiques pour la nature et l'humanité. » Questions
d'accroche :
- « Quel est le principe de datation des éruptions volcaniques ainsi que des momies pharaoniques ? »
- « En quoi diffère la centrale d'électricité thermonucléaire de la centrale thermique classique ? »
- « Qu'est-ce qu'un réacteur nucléaire ? »
- « En quoi consistait l'accident survenu le 26 avril 1986 dans la centrale thermonucléaire de la ville de
  Tchernobyl en Ukraine ? En quoi consiste la gravité de cet accident et quelles sont ses conséquences
  néfastes pour le considérer jusqu'à maintenant comme étant la plus grande catastrophe du nucléaire
  civil ? » (Les questions 2 et 4 ne sont traitées que dans « En savoir plus », p.314–315.)

**Introduction (p.286, titre « REACTIONS NUCLÉAIRES »)** : « Selon leur énergie de liaison par nucléon,
certains noyaux sont stables et gardent indéfiniment la même composition. D'autres sont instables et se
transforment spontanément en émettant un rayonnement. Ces noyaux sont dits radioactifs. On parlera alors
de réactions nucléaires spontanées du fait que ces transformations nucléaires se produisent sans
intervention d'agent extérieur. Il est possible également de provoquer la transformation d'un ou de
plusieurs noyaux, relativement stables en d'autres noyaux. On parlera alors de réaction nucléaire
provoquée. […] »

**Plan du chapitre** (titres du manuel ; deux grandes parties à numérotation propre) :
- **RÉACTIONS NUCLÉAIRES SPONTANÉES — RADIOACTIVITÉ**
  1. Le phénomène de radioactivité (p.286–287)
  2. Les différents types de rayonnements radioactifs — 2.1 Mise en évidence expérimentale (p.287–288) ;
     2.2 Propriétés des rayonnements radioactifs (p.288–290)
  3. Mécanismes nucléaires (p.290) — 3.1 Mécanisme de la radioactivité α (p.291) ; 3.2 … β⁻ (p.291–292) ;
     3.3 … β⁺ (p.292) ; 3.4 Émission γ (p.292, + Remarque « notion de famille radioactive »)
  4. Évolution temporelle de la radioactivité — 4.1 Décroissance radioactive (p.293) ; 4.2 Activité d'une
     source radioactive (p.293–294) ; 4.3 Période radioactive (p.294) ; 4.4 Application : datation par le
     carbone 14 (p.294–295)
- **RÉACTIONS NUCLÉAIRES PROVOQUÉES** (p.295)
  1. La réaction de fission — 1.1 Définition ; 1.2 Production d'une réaction de fission (p.295–296) ;
     1.3 Équation générale d'une réaction de fission (p.296–297) ; 1.4 Énergie libérée par la fission (p.297)
  2. La réaction « du » fusion [sic, titre p.298] — 2.1 Définition ; 2.2 Production d'une réaction de
     fusion ; 2.3 Énergie libérée par la fusion (p.298–299)
  3. Applications des réactions de fission et de fusion — 3.1 Énergie du soleil (p.299) ; 3.2 Énergie
     nucléaire (réacteurs, bombe A, bombe H) (p.300)
- puis « L'essentiel » (p.301) · « Exercices » : Exercice résolu (p.302–305) ; Exercices à résoudre —
  Tests rapides des acquis : 1 Items « vrai ou faux », 2 QCM (p.306–307) ; Exercices d'application 3 à 11
  (p.307–308) ; Exercices de synthèse 12 à 17 (p.309–311) · « En savoir plus » (p.312–315).

### Cours — activités et contenus

**1 LE PHÉNOMÈNE DE RADIOACTIVITÉ** (p.286–287)
- **Activité documentaire (p.286)** — texte historique : 1896 Becquerel (après les rayons X de Roentgen,
  1895) découvre par hasard l'impression de plaques photographiques rangées dans un tiroir obscur avec du
  sulfate double de potassium et d'uranium ; refait l'expérience avec des composés d'uranium non
  fluorescents (positive) ; « rayons uraniques ». Début 1898, Marie Curie : la pechblende émet plus que
  l'uranium ; isole le polonium avec Pierre Curie (juillet 1898), donne le nom de radioactivité ; décembre
  1898 : le radium. 1934 : Irène et Frédéric Joliot-Curie, radioactivité artificielle (plaque d'aluminium
  bombardée de particules α). Photos : Becquerel (1852-1908) ; Pierre et Marie Curie ; Irène et Frédéric
  Joliot-Curie.
  Questions (p.287) : 1°) qu'est-ce qui a amené Becquerel à supposer un rayonnement pénétrant ? 2°) qu'est-ce
  qui montre que c'est Marie Curie et non Becquerel qui a découvert la radioactivité ? 3°) qu'est-ce qu'un
  corps radioactif d'après le texte ? 4°) quand la radioactivité est-elle dite artificielle ? (Pas de
  réponse rédigée ; suivie de la Définition.)

**2 LES DIFFÉRENTS TYPES DE RAYONNEMENTS RADIOACTIFS** (p.287–290)
- **2.1 Expérience (p.287)** — vers 1899, Becquerel : une partie du rayonnement porte de l'électricité.
  Dispositif : sel de radium au fond d'une cavité étroite d'un cylindre de plomb à parois épaisses ; écran E
  perpendiculaire à l'axe ; entre les deux, champ électrique OU magnétique uniforme ; trois points d'impact
  A, B, C. Fig.1 (champ magnétique B⃗ ⊗ rentrant, région circulaire) : A dévié vers le haut, C non dévié
  (dans l'axe), B dévié vers le bas. Fig.2 (champ électrique E⃗ entre une plaque « − − − » en haut et
  « + + + » en bas) : même disposition A (haut), C (axe), B (bas).
  Questions : 1°) qu'est-ce qui montre l'émission de trois rayonnements différents ? 2°) d'après la
  disposition des impacts, montrer que le radium émet des particules chargées positivement et d'autres
  négativement ; 3°) identifier le troisième type.
  **Interprétation (p.288)** : A ← charges positives, rayonnement α, noyaux d'hélium (hélions) ⁴₂He ;
  B ← charges négatives, rayonnement β⁻, électrons ⁰₋₁e ; C ← non dévié, photons de très courte longueur
  d'onde (de l'ordre de 10⁻⁴ nm), rayonnement γ. Conclusion : voir « Encadrés ».
- **2.2 Propriétés (p.288–290)** (prose, valeurs lues sur l'image) :
  - Pouvoir d'ionisation et de pénétration (Fig.3 : papier / aluminium / plomb-béton-acier) : α émises à
    ~20000 km.s⁻¹, très ionisantes, très peu pénétrantes, arrêtées par des plaques très minces
    d'aluminium, une feuille de papier ou quelques centimètres d'air ; β⁻ jusqu'à 290000 km.s⁻¹, moins
    ionisantes, plus pénétrantes, arrêtées par un écran de plexiglas ou une plaque d'aluminium de ~7 mm ;
    β⁺ : pouvoirs identiques à β⁻ ; γ : peu ionisant, très pénétrant, traverse un bloc de plomb, d'acier
    ou de béton de ~20 cm.
  - Impression d'une plaque photographique ; luminescence d'un écran au sulfure de zinc (scintillations) ;
    ionisation des gaz (électroscope déchargé quel que soit le signe ; compteur Geiger-Muller, Fig.4).
  - Indépendance de la pression et de la température (« à condition qu'elle ne soit pas excessivement
    élevée »).
  - La radioactivité est un phénomène nucléaire (même activité quel que soit le corps simple/composé et
    l'état physique ; mêmes propriétés chimiques des isotopes) → « il n'est pas nécessaire d'isoler un
    élément radioactif pour utiliser son rayonnement ». APPLICATION : traceurs.
  - Effets biologiques : ionisation, ADN modifié → cellule cancéreuse ; **irradiation** (exposition à un
    rayonnement inhabituel pendant une durée limitée, ex. radiographie ; dépend de la fraîcheur de la
    source, de la durée et de la fréquence d'exposition) / **contamination** (échantillon absorbé par
    l'organisme ; accidentelle — ingestion, respiration — ou volontaire — imagerie médicale).

**3 MÉCANISMES NUCLÉAIRES** (p.290–292)
- **Question (p.290)** : équations (1) ²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He et (2) ¹⁴₆C → ⁰₋₁e + ¹⁴₇N ; comparer
  nombres de charge et de masse avant/après, en déduire les règles. Réponse : lois de conservation (voir
  « Encadrés »).
- **3.1 α (p.291)** — Question : écrire l'équation générale (« radioactivité a » [sic]). Démarche :
  ᴬ_Z X → ⁴₂He + ᴬ'_Z' Y ; Z = 2 + Z' d'où Z' = Z − 2 ; A = 4 + A' d'où A' = A − 4. Exemples :
  ²¹⁰₈₄Po → ⁴₂He + ²⁰⁶₈₂Pb ; ²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn ; ²³⁸₉₂U → ⁴₂He + ²³⁴₉₀Th.
- **3.2 β⁻ (p.291)** — ¹₀n → ¹₁p + ⁰₋₁e ; exemples : ²¹⁰₈₃Bi → ⁰₋₁e + ²¹⁰₈₄Po ; ¹⁴₆C → ⁰₋₁e + ¹⁴₇N ;
  ⁶⁰₂₇Co → ⁰₋₁e + ⁶⁰₂₈Ni ; ¹²₅B → ⁰₋₁e + ¹²₆C.
- **3.3 β⁺ (p.292)** — exemples : ³⁰₁₅P → ³⁰₁₄Si + ⁰₁e ; ¹¹₆C → ¹¹₅B + ⁰₁e. Question : « Expliquer
  l'origine de la particule ⁰₁e. » Interprétation : ¹₁p → ¹₀n + ⁰₁e.
- **3.4 Émission γ (p.292)** — ᴬ_Z Y* (noyau excité) → ᴬ_Z Y + γ. Remarque « famille radioactive » :
  ²³⁸₉₂U → … → isotope stable ²⁰⁶₈₂Pb.
- **Notation** : le manuel écrit le positon ⁰₁e (indice « 1 », sans « + ») et l'électron ⁰₋₁e ; **aucun
  neutrino / antineutrino** n'apparaît dans les équations β.

**4 ÉVOLUTION TEMPORELLE DE LA RADIOACTIVITÉ** (p.293–295)
- **4.1 Questions (p.293)** : échantillon de N₀ noyaux à t = 0, N à t > 0. 1°) comparer N à N₀ ;
  2°) « dN la variation moyenne de N entre t et t + dt […] On admet que dN s'écrit : dN = − λNdt, avec λ une
  constante positive. » a) justifier le signe (−) ; b) montrer que N = N₀e^(−λt). Réponse rédigée : N < N₀ ;
  dN = nombre moyen de noyaux qui se désintègrent pendant dt ; λ constante radioactive, en s⁻¹ ;
  intégration de dN/N = − λdt : ln N = − λt + C ; à t = 0, ln N₀ = C ; ln N = − λt + ln N₀ ;
  ln(N/N₀) = − λt ⇒ N = N₀e^(−λt). Fig.5 : courbe N(t) décroissante, N₀/2 à T, N₀/4 à 2T.
- **4.2 Activité (p.293–294)** : définition + loi de décroissance de l'activité (voir « Encadrés ») ;
  Fig.6 : A(t), A₀/2 à T, A₀/4 à 2T.
- **4.3 Période (p.294)** : définition + T = ln2/λ = 0.693/λ ; période de 10⁻¹⁵ s à 10²³ s. **Tableau
  (lu sur l'image)** :

  | Noyau radioactif | ²¹⁴₈₄Po | ²¹⁴₈₃Bi | ¹²³₅₃I | ¹³⁷₅₅Cs | ¹⁴₆C | ²³⁸₉₂U |
  |---|---|---|---|---|---|---|
  | Période ou demi-vie | 1,5 10⁻⁴ s | 19,7 min | 13,2 heures | 30,2 ans | 5730 ans | 4,5 10⁹ ans |

- **4.4 Datation par le carbone 14 (p.294–295)** : les organismes assimilent ¹²₆C et ¹⁴₆C en proportion
  constante ; à la mort l'assimilation s'arrête ; ¹⁴₆C, β⁻, période 5730 ans ⇒ le rapport ¹⁴₆C/¹²₆C diminue.
  **Questions (p.295)** : charbon de bois d'une grotte, 1,6 désintégrations par minute contre 11,5 par
  minute pour un échantillon de même masse de bois récemment coupé. 1°) montrer que
  t = − (T/0,693)·ln(A/A₀), T période de ¹⁴₆C, A₀ et A activités à t₀ = 0 et t > 0 ; 2°) T = 5730 ans,
  calculer t. (Valeur numérique **non imprimée** par le manuel.) Remarque : pour des échantillons plus
  vieux, uranium 238 → âge de la Terre estimé à 4,6 milliards d'années.

**RÉACTIONS NUCLÉAIRES PROVOQUÉES** (p.295–300) — intro : fission mise en évidence en 1938, première
fusion en 1952 (bombe H).
- **1.1–1.2 Fission (p.295–296)** : définition (voir « Encadrés ») ; noyaux d'uranium et de plutonium
  bombardés « le plus souvent par des neutrons lents » ; le neutron, neutre, ne subit pas de répulsion ;
  noyau cible excité et déformé (Fig.7a) ; noyau le plus utilisé ²³⁵U, aussi ²³³U et ²³⁹Pu ; noyaux
  **fissiles** ; 2 ou 3 neutrons émis → **réaction en chaîne** (Fig.7b : arbre neutron → noyau père →
  noyaux fils + neutrons) ; non contrôlée → bombe A ; contrôlée (énergie libérée par unité de temps
  constante) → réacteur.
- **1.3 Questions (p.296–297)** : ᴬ_Z X + ¹₀n → ᴬ¹_Z₁X₁ + ᴬ²_Z₂X₂ + k neutrons. 1°) a) relations entre Z,
  Z₁, Z₂ et entre A, A₁, A₂, k ; b) équation générale. 2°) fission de ²³⁵U → ¹⁴⁰₅₅Cs + ⁹³_Z₂X₂ + k neutrons :
  a) calculer Z₂ et identifier X₂ (tableau : Brome Br 35, Krypton Kr 36, Rubidium Rb 37, Strontium Sr 38) ;
  b) déterminer k. Réponse (exemples) : ¹₀n + ²³⁵₉₂U → ¹⁴⁰₅₅Cs + ⁹³₃₇Rb + 3¹₀n « (objet de la question
  2°) » ; ¹₀n + ²³⁵₉₂U → ⁹⁴₃₈Sr + ¹⁴⁰₅₄Xe + 2¹₀n ; ¹₀n + ²³⁵₉₂U → ⁹⁵₃₉Y + ¹³⁸₅₃I + 3¹₀n.
- **1.4 Énergie libérée par la fission (p.297)** — Question : montrer avec ¹₀n + ²³⁵₉₂U → ⁹⁵₃₈Sr + ¹³⁹₅₄Xe +
  2¹₀n qu'une fission libère, suite au défaut de masse Δm, une importante énergie E. Rédaction : E = Δm.c² ;
  Δm = {m(²³⁵₉₂U) + m(¹₀n)} − {m(⁹⁵₃₈Sr) + m(¹³⁹₅₄Xe) + 2 m(¹₀n)} ; données : m(²³⁵₉₂U) = 234,9934 u
  (1u = 931,5 MeV.c⁻²), m(¹³⁹₅₄Xe) = 138,8888 u, m(⁹⁵₃₈Sr) = 94,8064 u, m(¹₀n) = 1,0087 u ; « la perte de
  masse qui accompagne la réaction est 0,2115 u, soit 197 MeV.c⁻² » ; rapportée à une mole d'atomes
  ≈ 2.10¹³ J ou 5,5.10⁶ kWh (Fig.8 centrale). **[?] Incohérence du manuel** : avec les masses imprimées,
  Δm = 236,0021 − 235,7126 = 0,2895 u (≈ 270 MeV), pas 0,2115 u ; ne pas reprendre ces données telles
  quelles dans un item.
- **2.1–2.2 Fusion (p.298)** : définition ; exemple ²₁H + ³₁H → ⁴₂He + ¹₀n (Fig.9) ; difficulté = répulsion
  électrostatique ; température de l'ordre de 10⁸ K (« une centaine de millions de degrés ») ; première
  bombe H, 1952 (Fig.10 : 31 octobre 1952), océan Pacifique.
- **2.3 Énergie libérée par la fusion (p.298–299)** — Questions : 1°) énergie E libérée par la formation
  d'un ⁴₂He par fusion de ²₁H et ³₁H ; 2°) la comparer à celle de la fission de ²³⁵₉₂U (§1) ; 3°) peut-on
  s'appuyer sur cette comparaison pour dire si la fusion est plus ou moins exoénergétique, et pourquoi ?
  Rédaction : Δm = {m(²₁H) + m(³₁H)} − {m(⁴₂He) + m(¹₀n)} avec m(²₁H) = 2,01355 u, m(³₁H) = 3,01550 u,
  m(⁴₂He) = 4,00150 u, m(¹₀n) = 1,00867 u ; Δm = 1,8880·10⁻² u, soit 17,6 MeV, « alors qu'une fission libère
  environ 200 MeV. Cependant, ramenée au nombre de nucléons (5 pour cette fusion et 236 pour la fission),
  cette énergie libérée par fusion est environ cinq fois plus importante que celle d'une fission. » [Le
  rapport calculé avec ces nombres vaut ≈ 4,2 ; « environ cinq » est du manuel.] Fusion contrôlée
  seulement ~1 microseconde → pas d'utilisation constructive à présent.
- **3.1 Énergie du soleil (p.299)** — étapes (lues sur l'image) : ¹₁H + ¹₁H → ²₁H + ⁰₁e ;
  ¹₁H + ²₁H → ³₂He ; ³₂He + ³₂He → ⁴₂He + ¹₁H + ¹₁H ; bilan 4¹₁H → ⁴₂He + 2⁰₁e ; ~20 millions de degrés ;
  24,7 MeV par noyau d'hélium formé ; la Terre reçoit en moyenne 1 kW par m² au sol ; utilisations
  directes : chauffe-eau (effet de serre), turboalternateurs, photopiles.
- **3.2 Énergie nucléaire (p.300)** — réacteurs (fission contrôlée ; ²³⁵U et ²³⁹Pu ; propulsion de navires,
  sous-marins, réseau électrique ; production de radio-isotopes), Fig.11 « Schéma de principe d'un réacteur
  à eau sous pression » (barres de commande, cuve, cœur, pressuriseur, générateur de vapeur, caloporteur
  chaud 320 °C / froid 280 °C, turbine, alternateur, condenseur, refroidisseur) ; bombe A (fission non
  contrôlée ; ²³⁵U sur Hiroshima le 6 août 1945, ²³⁹Pu sur Nagasaki le 9 août 1945, Fig.12) ; bombe H
  (fusion non contrôlée amorcée par une bombe atomique).

### Encadrés, définitions, lois (VERBATIM, vérifiés sur l'image de leur page)

> **Définition** (p.287, encadré vert) — « La radioactivité est la transformation spontanée d'un noyau
> atomique instable en noyau d'une autre espèce chimique, avec émission de rayonnement. Un tel noyau est
> dit radioactif ; il est appelé parfois improprement radioélément. »

> **Conclusion** (p.288, encadré orange) — « • Le rayonnement α est constitué par des particules α
> (noyaux d'hélium ou hélions) de symbole ⁴₂He. • Le rayonnement β⁻ est constitué par des électrons de
> symbole ⁰₋₁e. • La rayonnement γ est constitué de photons. L'étude des particules émises par certains
> radioéléments artificiels révèle l'existence d'une autre particule déviée en sens inverse à l'électron
> mais de même masse. Cette particule a été identifiée à un électron positif ou positon (on dit aussi
> positron) ⁰₁e. Le rayonnement correspondant est le rayonnement β⁺. »

> **Lois de conservation** (p.290, prose en gras) — « En fait, la radioactivité obéit aux lois de
> conservation suivantes : - Conservation de l'énergie totale - Conservation de la quantité de mouvement
> (hors programme) - Conservation du nombre de charge : la charge électrique totale du système se
> conserve (loi de SODDY). - Conservation du nombre de masse : la somme des nombres de nucléons des noyaux
> formés est égale à la somme des nombres de nucléons des noyaux initiaux. »

> **Radioactivité α** (p.291, équation encadrée) — « Ainsi, l'équation bilan d'une transformation
> radioactive α (ou désintégration α) s'écrit : ᴬ_Z X → ⁴₂He + ᴬ⁻⁴_Z₋₂ Y » ; « Le noyau X désintégré est
> appelé noyau père ; le noyau Y formé est appelé noyau fils. » Remarque : « La radioactivité α concerne
> les noyaux lourds, noyaux instables à cause d'un excès de nucléons (A > 200). »

> **Radioactivité β⁻** (p.291) — « La radioactivité β⁻ correspond à la désintégration d'un noyau ᴬ_Z X en un
> noyau ᴬ'_Z' Y avec émission d'électron. Comme dans le noyau il n'y a pas d'électrons, un neutron se
> transforme au sein du noyau en un proton qui y demeure et un électron qui est éjecté selon l'équation
> bilan : ¹₀n → ¹₁p + ⁰₋₁e » ; équation encadrée : « ᴬ_Z X → ⁰₋₁e + ᴬ_Z₊₁ Y ». Remarque (p.292) : « La
> radioactivité β⁻ est caractéristique des noyaux présentant un excès de neutrons. »

> **Radioactivité β⁺** (p.292) — « La radioactivité β⁺ correspond à la désintégration d'un noyau ᴬ_Z X en
> un noyau ᴬ'_Z' Y avec émission d'un positon ⁰₁e selon l'équation bilan : ᴬ_Z X → ⁰₁e + ᴬ_Z₋₁ Y »
> (encadrée). Interprétation : « Comme le noyau ne contient pas de positons, un proton se transforme au
> sein du noyau en un neutron qui y demeure et un positon qui est expulsé selon l'équation bilan :
> ¹₁p → ¹₀n + ⁰₁e. La radioactivité β⁺ est caractéristique des noyaux présentant un excès de protons. Or,
> de tels noyaux n'existent pas dans la nature ; ils sont produits au laboratoire. On dit qu'il s'agit
> d'une radioactivité artificielle. »

> **Émission γ** (p.292) — « Le rayonnement γ est dû à l'obtention à un état excité du noyau formé par
> radioactivité α ou β. En fait, il est émis avec le retour de ce noyau à son état fondamental selon le
> schéma suivant : ᴬ_Z Y* (noyau excité) → ᴬ_Z Y + γ. Les rayons γ étant très pénétrants, ils sont utiles
> et dangereux à la fois. En revanche, les rayonnements α et β sont moins dangereux puisqu'ils sont
> rapidement arrêtés. »

> **Famille radioactive** (p.292, Remarque) — « La radioactivité entraîne la transformation d'un noyau en
> un autre. Si ce dernier est lui même radioactif, il se désintégrera à son tour et ainsi de suite jusqu'à
> ce que le noyau obtenu soit stable. L'ensemble de ces noyaux constitue la famille radioactive du noyau
> ascendant appelé noyau père. La famille la plus connue est celle de l'uranium ²³⁸₉₂U qui conduit à
> l'isotope stable ²⁰⁶₈₂Pb du plomb. »

> **Loi de décroissance radioactive** (p.293) — « dN = − λNdt » (admis dans l'encadré Questions ; seule N = N₀e^(−λt) est encadrée) ; « Par intégration de la
> relation : dN/N = − λdt, on obtient : ln N = − λt + C […] d'où : ln(N/N₀) = − λt, ce qui conduit à :
> N = N₀e^(−λt). Cette relation exprime la loi de décroissance radioactive (Fig 5). » ; « Etant une
> caractéristique de l'élément radioactif, λ est appelée constante radioactive. Ayant la dimension de
> l'inverse d'un temps, elle est exprimée en s⁻¹. »

> **Définition (activité)** (p.293, encadré vert) — « On appelle activité d'une substance radioactive,
> notée A, le nombre de désintégrations qu'elle subit pendant une seconde. »

> **Loi de décroissance de l'activité** (p.294) — « D'après sa définition, l'activité s'écrit :
> A = − dN/dt. Or, dN = − λNdt. Donc, A = λN. Sachant que N = N₀e^(−λt), il vient : A = λN₀e^(−λt).
> λN₀ = A₀ activité à l'instant t = 0, on a finalement : A = A₀e^(−λt) » (encadrée). « L'activité s'exprime
> en becquerel (Bq). Un becquerel correspond à une désintégration par seconde. »

> **Définition (période)** (p.294, encadré vert) — « On appelle période radioactive ou demi-vie d'une
> substance radioactive, la durée T au bout de laquelle le nombre de noyaux radioactifs initialement
> présents dans un échantillon de cette substance diminue de moitié. » Suite : « A l'instant t = T, on a :
> N = N₀/2 = N₀e^(−λT), ce qui entraîne : 1/2 = e^(−λT). D'où : T = ln2/λ = 0.693/λ » ; « Comme la constante
> radioactive λ, la période est une caractéristique du noyau radioactif ; elle peut varier de 10⁻¹⁵ s à
> 10²³ s. »

> **Définition (fission)** (p.295) — « La réaction de fission est une réaction nucléaire au cours de
> laquelle un noyau lourd se scinde en deux noyaux plus légers et de masses comparables. »

> **Équation générale de la fission** (p.297, encadrée) — « ¹₀n + ᴬ_Z X → ᴬ¹_Z₁X₁ + ᴬ²_Z₂X₂ + k¹₀n telle
> que : Z₁ + Z₂ = Z, A₁ + A₂ + k = A. »
>
> [?] Erreur du manuel : avec le neutron incident, le bilan des nombres de masse est A₁ + A₂ + k = A + 1
> (exemples p.297 : 140 + 93 + 3 = 236).

> **Énergie libérée** (p.297) — « D'après la loi de conservation de l'énergie totale du système de
> particules mises en jeu, on a : E = Δm.c². »

> **Définition (fusion)** (p.298) — « La fusion est une réaction nucléaire au cours de laquelle deux noyaux
> légers s'unissent pour former un noyau plus lourd. »

> **Réacteur nucléaire** (p.300) — « Un réacteur nucléaire est un appareil servant à réaliser des réactions
> de fission contrôlées. »

### L'essentiel (p.301, verbatim, lu sur l'image)

> ■ Une réaction nucléaire est une transformation au cours de laquelle un ou plusieurs noyau(x) se
> désintègre(nt) en donnant un ou plusieurs noyau(x) nouveau(x) et éventuellement une ou plusieurs
> particules.
> ■ Une réaction nucléaire peut être spontanée ou provoquée. Dans les deux cas, elle peut être symbolisée
> par une équation qui obéït aux lois de conservation du nombre de masse et du nombre de charge.
> ■ La radioactivité est la transformation spontanée d'un noyau en un autre plus stable avec émission d'un
> rayonnement.
> ■ On distingue trois types de radioactivités : • la radioactivité α (émission d'une particule α : noyau
> d'atome d'hélium ⁴₂He), • la radioactivité β⁻ (émission d'un électron ⁰₋₁e), • la radioactivité β⁺
> (émission d'un positon ⁰₁e)
> ■ L'émission γ est un phénomène corrélatif qui se produit chaque fois qu'un noyau fils est obtenu à l'état
> excité.
> ■ La loi de décroissance radioactive est : **N = N₀ e^(−λt)** (encadré), avec N₀, le nombre de noyaux
> présents dans l'échantillon à l'instant t = 0 et λ la constante radioactive.
> ■ La demi vie (ou période radioactive) T d'une substance radioactive est la durée au bout de laquelle le
> nombre de noyaux initialement présents diminue de moitié. **T = ln2/λ** (encadré)
> ■ L'activité A d'une substance radioactive est donnée par le nombre moyen de désintégrations par unité de
> temps, A = A₀e^(−λt) où A₀ désigne l'activité à l'instant t = 0.
> ■ A cause du défaut de masse qui en résulte, une réaction nucléaire libère de l'énergie.
> ■ Un noyau lourd subit une réaction de fission lorsque, sous l'action d'un neutron lent, il se scinde en
> deux noyaux de masses comparables.
> ■ La fusion est une réaction nucléaire au cours de laquelle des noyaux très légers fusionnent en un noyau
> moins léger.
> ■ Les énergies libérées par les réactions nucléaires sont énormes ; toutefois, l'énergie libérée par la
> fusion est plus grande que celle libérée par la fission.

(Écart interne : la définition de la radioactivité de l'Essentiel dit « en un autre plus stable », celle
de la p.287 « en noyau d'une autre espèce chimique ». La dernière puce n'ajoute pas « par nucléon »,
précision donnée seulement p.299.)

### Exercice résolu (p.302–305)

**Énoncé.** I – 1°) ²³⁵₉₂U + ¹₀n → ⁹⁴_Z Sr + ᴬ₅₄Xe + 2¹₀n : déterminer A et Z en précisant les lois.
2°) ²³⁸₉₂U capte un neutron rapide → uranium 239 radioactif ; deux désintégrations β⁻ successives →
plutonium : écrire les équations, nombres de masse et de charge du Pu. 3°) a) ²³⁴₉₂U radioactif α : équation,
identifier X (tableau : ⁴₂He 4,0015 u ; ²³⁶₉₃Np 235,9956 ; ²³⁴₉₂U 233,9904 ; ²³¹₉₁Pa 230,9860 ; ²³⁰₉₀Th
229,9737) ; b) énergie libérée en MeV et en joule par un noyau, puis par 1 g ; c) énergie répartie en
énergie cinétique entre X et α, rapport des Ec = inverse du rapport des masses : Ec(α), Ec(X), vitesse de α ;
d) certaines α ont en réalité Ec = 13 MeV, écart expliqué par l'émission γ : énergie de chaque photon et
longueur d'onde λ. II – ²³⁸₉₂U → ²⁰⁶₈₂Pb + xα + yβ⁻ (intermédiaires négligés). 1°) x et y. 2°) à t = 0 pas
de plomb ; N₀, N (U restant), N' (Pb) : a) N' en fonction de t, λ, N ; b) âge en fonction de T et de N'/N,
« On pourra supposer t << T et pour ε petit, on prendra e^ε ≈ 1 + ε » ; c) 1 g d'U 238 et 10 mg de plomb :
âge. Données : T(²³⁸₉₂U) = 4,5 10⁹ ans ; M(U) = 238 g.mol⁻¹ ; M(Pb) = 206 g.mol⁻¹ ; ln2 = 0,693 ;
1 u = 931,5 MeV.c⁻² ; « 1 MeV = 1,6 10⁻¹⁹ J » [coquille du manuel : lire 1,6 10⁻¹³ J, valeur effectivement
utilisée dans la solution] ; 𝒩 = 6,02.10²³ ; h = 6,62.10⁻³⁴ J.s ; c = 3.10⁸ m.s⁻¹.

**Solution.** I-1°) 235 + 1 = 94 + A + 2 → A = 140 ; 92 = Z + 54 → Z = 38. 2°) ²³⁹₉₂U → ⁰₋₁e + ²³⁹₉₃X ;
²³⁹₉₃X → ⁰₋₁e + ²³⁹₉₄Pu (X = neptunium Np, « à l'aide du tableau périodique »). 3°) a) ²³⁴₉₂U → ⁴₂He + ᴬ_Z X,
A = 230, Z = 90 : ²³⁰₉₀Th. b) Δm = 233,9904 − [4,0015 + 229,9737] = 1,52.10⁻² u ≈ 14,16 MeV.c⁻² ;
W₁ = 14,16 MeV, soit 2,26.10⁻¹² J ; W = (m𝒩/M)·W₁ = 3,64.10²² MeV, soit 5,8.10⁹ J. c) W = Ec(α) + Ec(Th) (1) ;
Ec(α)/Ec(Th) = m_Th/m_α ; Ec(α) = m_Th·Ec(Th)/m_α (2) ; Ec(Th)[1 + m_Th/m_α] = W, d'où (encadré)
Ec(Th) = m_α/(m_α + m_Th)·W et Ec(α) = m_Th/(m_α + m_Th)·W ; Ec(Th) = 0.242 MeV ; Ec(α) = 13.918 MeV ;
Ec(α)/W·100 = 98,2 % ; Ec(α) = ½m_α v_α² d'où ‖v⃗_α‖ = √(2Ec(α)/m_α) = 2,59.10⁷ m.s⁻¹. d) Eγ = 13,918 −
13,000 = 0,918 MeV ; Eγ = hc/λ d'où λ = hc/Eγ = 1,35.10⁻¹² m. II-1°) 238 = 206 + 4x et 92 = 82 + 2x − y →
x = 8, y = 6. 2°) a) N' = N(e^(λt) − 1) (encadré) ; b) N'/N = e^(λt) − 1 = e^((ln2/T)t) − 1 ≈ (ln2/T)t,
d'où t = (N'/N)·(T/ln2) ; c) N = m_U𝒩/M_U, N' = m_Pb𝒩/M_Pb, t = (m_Pb/m_U)(M_U/M_Pb)(T/ln2) =
75.10⁶ ans.

### Exercices à résoudre (p.306–311)

**1 Items « vrai ou faux » (p.306)** — 10 items : 1- radioactivité = transformation nucléaire spontanée ;
2- toujours une transformation lente ; 3- nombre de noyaux désintégrés ne dépend que du temps ;
4- activité proportionnelle au temps ; 5- demi-vie = durée au bout de laquelle la masse d'un échantillon
diminue de moitié ; 6- conservation de la charge totale et du nombre total de nucléons toujours
respectées ; 7- fission et fusion sont spontanées ; 8- bombe H : fusion amorcée par une fission ;
9- énergie du soleil : fusion transformant ¹₁H en ⁴₂He ; 10- γ beaucoup plus pénétrant que α et β, provoque
de nombreuses ionisations, très dangereux. (Pas de corrigé.)

**2 QCM (p.306–307)** — « la (ou les) proposition(s) juste(s) » : I réaction nucléaire et catalyseur /
pression / « ne dépend pas des facteurs habituels » ; II radioactivité : phénomène nucléaire / dépend de la
combinaison chimique / même pour tous les isotopes ; III spontanée / provoquée / selon le cas ; IV loi :
N = N₀e^(−λt) / N = N₀e^(λt) / N = N₀(1 − e^(−λt)) ; V période : diminue de moitié / du quart / augmente de
la moitié ; VI conservation : nucléons seulement / charge seulement / les deux ; VII même nombre de noyaux,
demi-vie plus courte → activité initiale supérieure / inférieure / égale ; VIII γ en médecine (sans
précaution / gammathérapie avec précautions / jamais) ; IX fission (capture d'un neutron par un noyau lourd
qui se scinde / noyau de masse plus importante / faible énergie) ; X fusion (noyau plus stable / noyau de
masse plus faible et libère de l'énergie / toujours un noyau unique). (Pas de corrigé.)

**Exercices d'application (p.307–308)**
- **3** — tableau à compléter A ²¹⁴Po (neutrons 130), B ²¹⁰Pb (Z = 82), C Bi (A = 210, Z = 83), D Po
  (A = 210, N = 126), E Pb (Z = 82, N = 124) ; compléter A → B, B → C, C → D, D → E et identifier la
  particule émise. (Pas de réponse au manuel.)
- **4** — ²³⁸U → ²²⁶₈₈Ra par x α et y β⁻ ; ²²⁶Ra → ²⁰⁶₈₂Pb par x' α et y' β⁻. Réponse : x = 3, y = 2,
  x' = 5, y' = 4.
- **5** — ²¹⁸₈₄Po → ᴬ_Z Pb + α ; 1°) équation et lois ; 2°) le noyau ᴬ_Z Pb est radioactif de période T ; un échantillon de ᴬ_Z Pb de
  masse m₀ = 40 mg à t = 0 n'en contient plus que m = 10 mg 54 minutes plus tard (imprimé « t = 0,54 minutes », cf. doute 3) :
  T et λ de ce noyau. Réponse : ²¹⁸₈₄Po → ⁴₂He + ²¹⁴₈₂Pb ; T = 27 min ; λ = 4,27.10⁻⁴ s⁻¹. (D'après Bacc.
  juin 2004, session principale, section sport.)
- **6** — ²²⁶₈₈Ra → α + ᴬ_Z Rn ; M(α) = 4,0015 u ; M(Rn) = 221,9703 u ; M(Ra) = 225,9771 u ;
  1u = 1,66 10⁻²⁷ kg ; c = 3 10⁸ m.s⁻¹ : énergie libérée. Réponse : ²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn ;
  W = 7,9.10⁻¹³ J.
- **7** — Bethe et Critchfield (1938), énergie du soleil : (1) ⁰₋₁e + 2¹₁H → X ; (2) X + ¹₁H → Y ;
  (3) Y + ⁴₂He → Z ; (4) Z + ⁰₋₁e → T ; (5) T + ¹₁H → 2⁴₂He ; 1°) équilibrer et identifier X, Y, Z, T
  (extrait de tableau périodique H … He / Li Be B C N O F Ne) ; 2°) bilan, type de réaction. (Pas de
  réponse.)
- **8** — 1°) ²³⁵₉₂U + ¹₀n → ¹⁴⁶ₓLa + ⁸⁷₃₅Br + y¹₀n : a) x et y ; b) origine de l'énergie. 2°) ²³⁸₉₂U + X →
  ²³⁹₉₂U ; ²³⁹₉₂U → ²³⁹₉₃Np + Y ; ²³⁹₉₃Np → ᴬ_Z Pu + Y : a) X, Y ; b) A, Z. Réponse : x = 57, y = 3 ; défaut
  de masse ; X neutron ¹₀n, Y électron ⁰₋₁e ; A = 239, Z = 94.
- **9** — fusion en deux étapes : ⁶₃Li + ¹₀n → ⁴₂He + X ; ²₁H + X → ⁴₂He + Y ; 1°) X et Y ; 2°) équation
  bilan. (Pas de réponse.)
- **10** — 1°) a) ²³⁸₉₂U capture un neutron sans rayonnement ; b) désintégration vers ²³⁹₉₄Pu, nombre et
  nature des particules ; 2°) ¹₀n + ²³⁵₉₂U → ᴬ₃₈Sr + ¹⁴⁰_Z Xe + 2¹₀n : a) A, Z ; b) type. Réponse :
  ²³⁸₉₂U + ¹₀n → ²³⁹₉₂U ; ²³⁹₉₂U → 2⁰₋₁e + ²³⁹₉₄Pu ; A = 94, Z = 54 ; fission.
- **11** — ⁷⁷₃₅Br émetteur β⁺ → isotope du sélénium (γ éventuel), période 57 h, imagerie médicale ;
  1°) équation ; 2°) λ ; 3°) A₀ = 5,7.10¹⁵ Bq : N₀. Réponse : ⁷⁷₃₅Br → ⁰₁e + ⁷⁷₃₄Se ; 3,38.10⁻⁶ s⁻¹ ;
  1,68.10²¹.

**Exercices de synthèse (p.309–311)** — aucune réponse au manuel (p.317 s'arrête à l'exercice 11).
- **12** — A : ²¹⁰₈₄Po α → plomb ; énergie entièrement cinétique, rapport des Ec = inverse du rapport des
  masses : Ec(α), Ec(Pb) en MeV, vitesses ; M(α) = 4,0015 u, M(²¹⁰₈₄Po) = 209,9368 u, M(²⁰⁶₈₂Pb) =
  205,9295 u, 1 u = 931,5 MeV.c⁻², c = 3·10⁸ m.s⁻¹. B : ¹³⁷₅₅Cs β⁻ → ᴬ_Z Ba (fondamental ou excité). I-1°)
  A, Z, équation ; 2°) énergie en MeV et J (m(⁰₋₁e) = 5,5.10⁻⁴ u, Cs 136,8768 u, Ba 136,8743 u ;
  1 eV = 1,6.10⁻¹⁹ J), formes de cette énergie sans calcul. II- λ = 8,4.10⁻¹⁰ s⁻¹ : T en s et en années.
- **13** — carbone : ¹²C 98,9 %, ¹³C 1,1 %, ¹⁴C (T = 5730 années) ; 1°) relation λ–T ; 2°) 13,6 désintégrations
  par minute et par gramme dans le cycle du CO₂ ; bois d'un navire Viking mesuré en 1983 : 12 désintégrations
  par minute et par gramme : année d'abattage ; 3°) rapport isotopique ¹²C/¹⁴C du carbone du cycle. Données :
  1 année = 365 jours ; 𝒩 = 6,02.10²³ mol⁻¹.
- **14** — ²²⁶₈₈Ra → α + ᴬ_Z X (isotope du radon) ; 1°) équation et règles ; 2°) tableau t (h) 0 à 200 par
  pas de 20 / ln N : 6,90 ; 6,75 ; 6,60 ; 6,45 ; 6,30 ; 6,15 ; 6,00 ; 5,85 ; 5,70 ; 5,55 ; 5,40 — a) tracer
  ln N = f(t) ; b) loi de décroissance ; c) T en jours ; 3°) rapport Ec(noyau)/Ec(α) = inverse du rapport des
  masses, remarque ; 4°) énergie libérée 4,5 MeV entièrement cinétique : vitesse de α ; 5°) radiation de
  λ = 2,5.10⁻¹¹ m : a) interpréter ; b) Ec(α) compte tenu du photon. Données : He 4,0015 u ; radon
  221,9771 u ; 1 u = 1,67.10⁻²⁷ kg ; c = 3.10⁸ m.s⁻¹ ; h = 6,63.10⁻³⁴ J.s ; 1 eV = 1,6.10⁻¹⁹ J. (D'après
  Bacc. juin 1997.)
- **15** — scintigraphie, traceur / marqueur (gammacaméra) : I-1°) iode 123 produit par deutons ²₁H sur
  ¹²²₅₂Te : équation ; 2°) ¹³¹₅₃I (T = 8 jours) émetteur β⁻ et γ → xénon : équation, énergie en MeV
  (m(¹³¹₅₃I) = 130,87705 u ; m(Xe) = 130,87545 u ; m(⁰₋₁e) = 5,486.10⁻⁴ u ; 1u = 931,5 MeV.c⁻²) ;
  3°) activité après 24 h en fonction de A₀. II-1°) ¹²³I émetteur γ pur, T' = 13,2 h, A = 6,4.10⁶ Bq :
  tracer A(t) aux points T, 2T, 3T, 4T… ; 2°) activité graphique au bout de 4 h, puis à 24 h.
- **16** — ⁶⁰₂₇Co β⁻, T = 5,27 ans, noyau fils excité, désexcitation par deux rayonnements 1,6.10⁻¹² m et
  1,8.10⁻¹² m (bombe à cobalt). 1°) équations de désintégration et de désexcitation ; 2°) durée pour perdre
  90 % de l'activité ; 3°) chaque électron 4,5.10⁻¹⁴ J, activité 1,7.10¹⁸ Bq, 10 % des électrons vers la
  cible : énergie par unité de temps ; 4°) énergie pour 0,8 s ; 5°) comparaison avec 10 s près d'une source
  de ~10¹⁴ Bq jugée dangereuse.
- **17** — Étude de texte (découverte de Becquerel, 26 février 1896, sulfate double d'uranium, plaques
  développées quatre jours plus tard ; 1898, Pierre Curie propose le mot radioactivité ; citation de Jean
  Becquerel). Questions : part du hasard / perspicacité ; nature du rayonnement invisible ; nom donné par
  Becquerel ; pourquoi c'est une propriété de l'élément uranium.

### En savoir plus (p.312–315)

Une ligne par rubrique : **Usages médicaux** (scintigraphie à l'iode 123, radioprotection : écrans,
combinaisons, durée, distance ; Fig.1a/1b) · **Rayonnements et santé** (pénétration α quelques µm, β
quelques mm, γ indirectement ionisant ; irradiation / contamination ; dose énergétique en gray, 1 Gy =
1 J.kg⁻¹ ; équivalent de dose en sievert, facteur Q : α 20, β 1, γ 1, X 1 ; effets somatiques précoces /
tardifs, fœto-embryonnaires (> 0,05 Sv) ; tableau « Effet d'une dose sur l'homme » < 1, 1–2, 2–5, 5–9,
> 9 Sv, d'après EDF) · **Énergie nucléaire et électricité** (centrale thermique vs nucléaire ; cœur =
combustible + modérateur + caloporteur ; barres de réglage et de sécurité ; gaine, cuve, enceinte de
confinement ; Tchernobyl 26 avril 1986 : une trentaine de morts, contamination au césium 137, 130000
habitants évacués ; Fig.2–3).

### Bornes de scope observées (chapitre 11)

- ✅ INCLUS (cours) : radioactivité (définition, caractère spontané, nucléaire, indépendance de P et T,
  noyau père / fils) ; **α, β⁻, β⁺, γ** : nature (⁴₂He, ⁰₋₁e, ⁰₁e, photons), déviation dans un champ
  électrique ou magnétique (lecture qualitative du signe de charge, sans calcul de trajectoire), pouvoirs
  d'ionisation et de pénétration (ordres de grandeur : papier/air, ~7 mm d'aluminium, ~20 cm de plomb) ;
  **lois de conservation du nombre de charge (Soddy) et du nombre de masse**, conservation de l'énergie
  totale ; équations-bilans α (A − 4, Z − 2), β⁻ (Z + 1), β⁺ (Z − 1), désexcitation γ (Y* → Y + γ) ;
  transformations n → p + e⁻ et p → n + e⁺ ; famille radioactive (U 238 → Pb 206), recherche de x α et y β⁻
  par conservation ; **loi de décroissance** dN = − λNdt (admise), N = N₀e^(−λt), constante radioactive λ
  (s⁻¹) ; **activité** A = − dN/dt = λN = A₀e^(−λt), becquerel ; **période** T = ln2/λ, lecture N₀/2, N₀/4
  à T, 2T (durées multiples de T), courbes N(t) et A(t) ; **datation au carbone 14** (t = −(T/ln2)·ln(A/A₀)) ;
  **fission** (neutron lent, noyaux fissiles ²³⁵U, ²³³U, ²³⁹Pu, réaction en chaîne contrôlée / non contrôlée,
  équation générale Z₁ + Z₂ = Z, A₁ + A₂ + k = A + 1 ; le manuel imprime « = A », coquille) ; **fusion** (²H + ³H, 10⁸ K, répulsion électrostatique) ;
  **énergie libérée E = Δm.c²** avec Δm en u et 1 u = 931,5 MeV.c⁻² (MeV et J ; par noyau, par gramme, par
  mole) ; comparaison fission / fusion **par nucléon** ; cycle proton-proton du soleil ; réacteurs, bombe A,
  bombe H (descriptif).
- ✅ INCLUS (mobilisé en exercice résolu / exercices seulement) : répartition de l'énergie libérée en
  énergie cinétique selon « rapport des Ec = inverse du rapport des masses » (donné dans l'énoncé),
  Ec = ½mv² (non relativiste) ; énergie d'un photon Eγ = hc/λ (prérequis ch. 9–10) et énergie γ =
  différence d'Ec ; datation U/Pb avec N' = N(e^(λt) − 1) et approximation e^ε ≈ 1 + ε ; nombre de noyaux
  N = m𝒩/M ; tracé de ln N = f(t) et lecture de la pente ; activité et énergie transmise par unité de temps
  (ex. 16) ; durée pour perdre un pourcentage d'activité.
- ⛔ EXCLU : **conservation de la quantité de mouvement** (« hors programme », p.290 — la répartition des Ec
  est toujours donnée, jamais démontrée) ; **neutrino / antineutrino** (absents de toutes les équations β) ;
  **capture électronique** et radioactivité « β⁺ naturelle » (le manuel affirme que les noyaux à excès de
  protons n'existent pas dans la nature) ; calcul de trajectoires des particules dans les champs ; courbe
  d'Aston et énergie de liaison (chapitre 10, prérequis) ; **dosimétrie** (gray, sievert, facteur Q :
  « En savoir plus » seulement, aucun exercice) ; technologie détaillée des réacteurs (modérateur,
  caloporteur, barres : « En savoir plus ») ; énergie cinétique relativiste ; constante de temps τ = 1/λ et
  vie moyenne (non nommées) ; démonstration de l'équation différentielle (dN = − λNdt est **admis**) ;
  séries de désintégration couplées / équilibre séculaire.
- Appareillage cité : écran, cylindre de plomb, champ E ou B (Fig.1–2), écrans papier / aluminium /
  plomb-béton-acier (Fig.3), électroscope, compteur Geiger-Muller (Fig.4), plaque photographique, écran au
  sulfure de zinc, gammacaméra (ex. 15).

### Doutes [?]

1. **p.297, énergie de fission** : « perte de masse 0,2115 u, soit 197 MeV.c⁻² » incompatible avec les
   masses imprimées (calcul : 0,2895 u). Ne pas réutiliser ce jeu de données ; garder l'ordre de grandeur
   « ~200 MeV » (repris p.299).
2. **p.303, données de l'exercice résolu** : « 1 MeV = 1,6 10⁻¹⁹ J » (coquille ; la solution utilise
   1,6.10⁻¹³ J : 14,16 MeV = 2,26.10⁻¹² J).
3. **p.307, ex. 5** : « à un instant de date t = 0,54 minutes plus tard » — lu comme « t = 0 ; 54 minutes
   plus tard » (cohérent avec la réponse T = 27 min, deux périodes de 40 à 10 mg).
4. **p.299** : « environ cinq fois » (17,6/5 contre 200/236 donne ≈ 4,2).
5. **p.305** : dans (2), « Ec(α) = m_Th Ec(Th)/m_a » (indice « a » pour α, coquille typographique).
6. **Ex. 6 vs ex. 14** : masse du radon 222 donnée 221,9703 u (ex. 6) puis 221,9771 u (ex. 14), identique
   à la partie décimale de la masse du radium de l'ex. 6 (225,9771 u) — possible erreur de saisie.
7. **Ex. 7** : équations (1) et (4) écrites avec ⁰₋₁e en **réactif** (capture d'électron) ; transcrites telles
   quelles, à ne pas « corriger » vers un cycle CNO standard (β⁺).
8. Titre « LA RÉACTION DU FUSION » (p.298), « DÉFINITON » (p.295), « ENERIGIE » (p.300),
   « SOURCE RADIATIVE » (p.293, titre 4.2) : coquilles de titres.
9. Programme officiel non consulté ici (R-3) : le statut au programme des notions vues seulement en exercice
   (répartition des Ec, datation U/Pb, Eγ = hc/λ) reste à confirmer.
10. Réponses absentes : ex. 1, 2, 3, 7, 9 et 12 à 17 ; activité « datation » (p.295) sans valeur numérique.
11. p.297, équation générale de la fission : « A₁ + A₂ + k = A » faux ; lire A + 1.

### Lecture

- **Pages lues par la couche texte** (prose) : 284 à 318 (les 35 pages), via
  `/root/.cache/yqa-manuels/223433/txt/pNNN.txt`.
- **Pages lues sur l'image** (110 dpi, `pdftoppm`) : **32 sur 32 du chapitre** — 284, 285, 286, 287, 288,
  289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309,
  310, 311, 312, 313, 314, 315 ; **+ p.317** (bloc « Chapitre 11 », zoom 200 dpi). p.316 et p.318 lues en
  texte seulement (aucun contenu du chapitre 11 hors liste de sites). **Total : 33 images.**
- **Sondage image (≥ 1 page sur 10, parmi les plus denses)** : fait sur la totalité ; pages les plus denses
  291, 294, 297, 302–305, 307–310, 317. **Écarts couche texte / image constatés** : p.290 équation (2)
  rendue « 14 / 4 C » et flèches perdues ; p.291 indices/exposants disloqués (« AZ -2- 4 Y » pour ᴬ⁻⁴_Z₋₂Y) ;
  p.292 exemples β⁺ (³⁰₁₅P → ³⁰₁₄Si) brouillés, γ perdu dans Y* → Y + γ ; p.293 « ln » rendu « n »,
  λ perdu dans dN/N = − λdt et ln(N/N₀) ; p.294 T = ln2/λ = 0.693/λ sans λ, tableau des périodes décalé ;
  p.295 formule de datation sans « ln » ; p.297 équations de fission et indices des masses ; p.299 Δ rendu
  « D » ; p.305 formules de l'exercice résolu illisibles (« Ec () », « 98, 2 0 0 », « r .t v ») ; p.306 QCM IV
  « e − h t » au lieu de e^(−λt) ; p.307 tableau de l'ex. 3 brouillé ; p.308 ex. 7 équation (4) « Z+ eT 0 -1 » ;
  p.309 « c = 3 u 10 m.s-1 », signe de β⁻ perdu (ex. 12 B) ; p.310 λ = 2,5.10⁻¹¹ m éclaté ; p.317 équations
  de réponse (ex. 5, 6, 10, 11) disloquées. Pages de prose (284, 286, 289, 300, 312–315) : pas d'écart de
  fond. Aucune formule de cette fiche n'a été prise à la couche texte seule.

## 3. Audit R-7 (2026-11-05)

Relecture indépendante (auditeur en contexte vierge, opus) de chaque chapitre **contre le PDF lui-même** : 100 % des encadrés, lois et relations transcrits confrontés à l'image de la page, 100 % du plan, et le reste par sondage (≥ 15 % des pages, souvent bien plus). Aucun chapitre n'a atteint le seuil d'escalade (3 erreurs substantielles sur la fiche). Corrections appliquées par un correcteur sur l'image de la page, puis revérifiées par un second auditeur opus.

| Chapitre | Pages sondées en image | Corrections fiche |
|---|---|---|
| 1 | 17 | 0 |
| 2 | 17 | 1 |
| 3 | 17 | 1 |
| 4 | 21 | 0 |
| 5 | 19 | 0 |
| 6 | 14 | 0 |
| 7 | 18 | 1 |
| 8 | 11 | 0 |
| 9 | 15 | 0 |
| 10 | 13 | 1 |
| 11 | 17 | 4 |

Total : 8 corrections, 179 pages sondées en image par les auditeurs (sur 318), en plus des pages lues en image par les lecteurs (toutes les pages à formule, encadré, tableau ou figure exploitée).
