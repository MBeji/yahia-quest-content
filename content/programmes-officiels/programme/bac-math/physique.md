<!-- Fiche de transcription DIFFÉRENTIELLE — profil ecole-secondaire (procédure `campagne`, étape 3).
     Source unique : manuel élève officiel CNP 223432P00 (320 p.), physique, 4ème année section
     Mathématiques. Aucun guide enseignant au corpus pour ce couple ⇒ le manuel élève fait référence.
     Lu le 2026-11-06 depuis le Drive `cnp-officiel` : couche texte page par page (pdftotext -layout) et
     vérification sur l'image de chaque page à formule, encadré, tableau, oscillogramme ou schéma
     exploité ; page PDF = page imprimée. Même collection CNP que le manuel Sciences expérimentales
     (223433) : la fiche `bac-sciences-exp/physique.md` sert de référence et seul l'écart est transcrit. -->

# Physique — Bac Mathématiques (`bac-math`) · manuel officiel CNP

> **Sources (Drive `cnp-officiel`, `manuels/secondaire/c4/eleve/`)** :
>
> - **Manuel élève** : code **223432P00** (320 p.), un seul tome — 11 chapitres en trois thèmes ;
>   réponses aux exercices p.318–320.
> - **Guide enseignant** : _aucun au corpus pour ce couple_ ⇒ le **manuel élève fait référence**.
> - **Référence différentielle** : `programme/bac-sciences-exp/physique.md` (manuel 223433, 318 p.,
>   même découpage en onze chapitres). Là où une page est identique, la section l'écrit
>   « identique à 223433 p.X » ; chaque valeur, exercice ou paragraphe qui change est relevé.
> - **Langue d'enseignement** : **fr**. **subject id** : `physique-bac-math` · **gradeSlug** : `bac-math`.
> - **Notation** : chiffres occidentaux 0-9, unités SI, puissances de 10 ; « Log » désigne le
>   logarithme népérien comme dans le manuel ; les formules perdues par la couche texte sont rétablies
>   sur l'image de la page.

## 1. Cadre & compétences

Année du **baccalauréat**, section Mathématiques. L'avant-propos (p.3) est mot pour mot celui du manuel
Sciences expérimentales (il y est écrit « conforme au programme officiel 4e Sciences expérimentales ») :
onze chapitres sur les trois thèmes du programme (Évolution de systèmes — Ondes — Physique atomique et
nucléaire), avec la même structure par chapitre (objectifs et prérequis, activités, « L'essentiel »,
exercice résolu, exercices avec réponses en fin d'ouvrage). Le manuel Mathématiques diffère par ses
pagination, certaines données numériques et certains exercices : voir « Écart avec Sciences
expérimentales » dans chaque section.

## 2. Plan annuel (carte des chapitres)

> Statut de transcription par chapitre — `generation` = transcrit à profondeur de génération
> (chaque activité et exercice décrit, encadrés verbatim ; ici sous forme différentielle). La couverture de
> pages réelle vit dans `suivi/bac-math.json`.

| #   | Thème | Chapitre | pages (PDF = imprimées) | profondeur |
| --- | ----- | -------- | ----------------------- | ---------- |
| 1 | Évolution de systèmes | Le condensateur ; le dipôle RC | 10–41 | `generation` |
| 2 | Évolution de systèmes | La bobine ; le dipôle RL | 42–77 | `generation` |
| 3 | Évolution de systèmes | Oscillations électriques libres | 78–109 | `generation` |
| 4 | Évolution de systèmes | Oscillations électriques forcées en régime sinusoïdal | 110–137 | `generation` |
| 5 | Évolution de systèmes | Oscillations libres d'un pendule élastique | 138–161 | `generation` |
| 6 | Évolution de systèmes | Oscillations mécaniques forcées en régime sinusoïdal | 162–183 | `generation` |
| 7 | Ondes | Ondes mécaniques progressives | 184–217 | `generation` |
| 8 | Ondes | Interactions onde-matière ; nature ondulatoire de la lumière | 218–247 | `generation` |
| 9 | Physique atomique et nucléaire | Spectre atomique | 248–271 | `generation` |
| 10 | Physique atomique et nucléaire | Le noyau atomique | 272–285 | `generation` |
| 11 | Physique atomique et nucléaire | Réactions nucléaires | 286–317 | `generation` |

## 2.1 Chapitre 1 — Le condensateur ; le dipôle RC (manuel 223432, p.10–41)

> **Constat d'ensemble (vérifié pixel à pixel)** : les 32 pages 10–41 de ce manuel **Mathématiques** (223432P00)
> sont **identiques à celles du manuel Sciences expérimentales 223433P00** (mêmes numéros de pages, même texte,
> mêmes figures, mêmes données, mêmes exercices). Couche texte : 0 mot de différence sur p.10–40 ; p.31 : 2 lignes
> de formule (rendu des exposants). Rendu 110 dpi comparé page à page : 0 pixel de différence (seuil 60/255) sur
> 31 pages ; p.31 : 463 px dans l'encadré de la loi u_C(t) = E(1 − e^{−t/τ}), relu à 220 dpi dans les deux
> manuels = **même formule**, seule la crénelure des glyphes (indice, fraction) diffère. Réponses p.318 (chap. 1 :
> ex. 3 à 9) = celles de 223433 p.316, mot pour mot. **Toute la section de référence
> (`bac-sciences-exp/physique.md` l.55-584) s'applique donc telle quelle ; elle est reprise ci-dessous sous forme
> compacte, et chaque encadré a été relu sur l'image de CE manuel (pages listées en « Lecture »).**
> Notation : « Log » = logarithme népérien (p.30, p.33) ; le manuel écrit u_C / uc, Q_o / Q₀, I_o / I₀ indifféremment.

Partie « Évolution de systèmes ». Deux leçons : « LE CONDENSATEUR » (p.12–20), « LE DIPÔLE RC » (p.21–30) ;
puis « L'essentiel » (p.31), « Exercices » (p.32–37, dont l'exercice résolu p.32–33), « Fiche technique »
(p.38–39), « En savoir plus » (p.40–41). Ouverture p.11 (appareil photo à flash).

**Objectifs (p.10, VERBATIM)** — « Réaliser la charge et la décharge d'un condensateur. » · « Reconnaitre que
l'intensité i du courant électrique est une grandeur algébrique. » · « Déterminer à l'aide de la courbe de charge
d'un condensateur, la valeur de la capacité C. » · « Déterminer graphiquement la constante de temps τ = RC d'un
dipôle RC, à partir des courbes de réponse u_C(t) ou i(t). » · « Établir l'équation différentielle régissant, au
cours du phénomène de charge d'un condensateur : - la charge instantanée q(t) du condensateur, - la tension u(t) à
ses bornes, - l'intensité i(t) du courant transitoire parcourant le circuit. » · « Calculer l'énergie emmagasinée
par un condensateur. »

**Prérequis (p.10)** — SAVOIR : définir l'intensité du courant électrique, la tension (ou d.d.p) électrique, la
quantité d'électricité, un résistor ; écrire Q = I.Δt ; énoncer la loi des mailles, la loi des noeuds, la loi
d'Ohm relative à un résistor, la loi d'Ohm relative à un générateur. SAVOIR FAIRE : distinguer tension continue /
variable ; utiliser un oscilloscope bicourbe ; calculer Q = I.Δt ; reconnaître une tension variable alternative,
une tension en créneaux ; appliquer la loi d'Ohm (résistor, générateur) et la loi des mailles.

**Ouverture (p.11, VERBATIM)** — « L'éclair lumineux de très forte intensité d'une lampe flasch d'un appareil
photo se produit grâce à un condensateur. » · « Le condensateur est un composant électrique connu comme un
réservoir d'énergie. De quelle forme d'énergie s'agit-il et qu'est-ce qui confère au condensateur cette
propriété ? » · « Quel est le principe de fonctionnement du flash d'un appareil photo ? »

**Plan** — LE CONDENSATEUR : 1 Définition et exemples (1.1, 1.2) · 2 Charge et décharge (p.13) · 3 Charge d'un
condensateur (p.14 ; 3.1 caractère algébrique de i ; 3.2 charge q ; 3.3 relation i–q) · 4 Relation q–u_C
(p.15–17) · 5 Capacité d'un condensateur plan (p.18) · 6 Tension de service et de claquage (p.19) · 7 Énergie
emmagasinée (p.19–20 ; 7.1 réservoir d'énergie ; 7.2 expression). LE DIPÔLE RC : 1 Réponse à un échelon de tension
(1.1 expérimentale, p.21 ; 1.2 théorique, p.22–24) · 2 Décharge dans un résistor (p.24 ; 2.1, 2.2) · 3 Influence
des grandeurs caractéristiques (p.26 ; 3.1 R ; 3.2 C ; 3.3 constante de temps, p.28–30).

### Cours — manipulations et questions (identique à 223433 p.12–30 ; relevé complet)

- **Histoire (p.12, VERBATIM)** — « Le condensateur est un terme introduit en 1782 par Volta (physicien italien,
  1745-1827) après avoir constaté que l'électricité “se condense” sur les surfaces en regard de deux conducteurs
  quand on les approche l'un de l'autre. » Diélectriques cités : air, papier imbibé d'huile de paraffine,
  céramique (oxyde de titane, titanates), mica, téflon, polyéthène, alumine. Types (Fig.2) : à air ; à diélectrique
  solide (feuilles métalliques minces roulées) ; électrochimiques (armatures en aluminium, diélectrique = couche
  d'alumine déposée par électrolyse).
- **§2 Manipulation charge/décharge (p.13–14)** — Fig.3 : générateur E, galvanomètre balistique G, résistor R,
  commutateur K (1/2), armatures A, B. K en 2 d'abord : rien ; K en 1 : déviation α dans le sens 1 puis retour à
  zéro (Fig.4a) ; ouvrir/refermer : rien (« chargé ») ; K en 2 : même angle α dans le sens 2, retour lent à zéro
  (Fig.4b) ; rien ensuite (« déchargé »). Questions : « 1°) Peut-on décharger un condensateur non chargé ? […]
  2°) Expliquer les phénomènes de charge et de décharge d'un condensateur et en déduire si l'on peut recharger un
  condensateur déchargé. » Interprétation : position 1, A et B neutres reliés aux pôles (+) et (−), électrons de A
  vers (+) et de (−) vers B, charges +q sur A, −q sur B, (V_A − V_B) = tension du générateur ; position 2,
  électrons de B vers A à travers R jusqu'à neutralité. **Conclusion (VERBATIM)** : « Le condensateur est un
  composant électrique capable de stocker des charges électriques. » [Image Fig.3 : R n'est que dans la branche de
  la position 2 ; G est en série avec le condensateur, hors de la branche R.]
- **§3.1 Manipulation i algébrique (p.14–15)** — Fig.5 : générateur idéal E, R, condensateur, K, deux DEL D1 et D2
  tête-bêche, voltmètre aux bornes du condensateur, voie Y sur u_R ; Fig.6 : u_R > 0 décroissant vers 0 (K en 1)
  puis u_R < 0 croissant vers 0 (K en 2). Questions : « 1°) Montrer que lorsque le commutateur K est dans la
  position 1, la diode D1 seulement s'allume, tandis que lorsqu'il est dans la position 2, c'est seulement D2 qui
  s'allume. 2°) […] u_R=Ri, montrer graphiquement qu i est positive et décroissante pendant la charge, négative et
  croissante pendant la décharge. » Interprétation : sens positif de la Fig.5 ; i > 0 en charge (D1), i < 0 en
  décharge (D2).
- **§4 Manipulation courant constant (p.15–17)** — Fig.8 : générateur de courant, K1, ampèremètre, condensateur
  en série ; voltmètre numérique + K2 aux bornes du condensateur ; q = I.t ; fermer puis rouvrir K2 avant mesure ;
  mesure toutes les 5 s. **I = 0,144 mA** :

  | t (s) | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
  |---|---|---|---|---|---|---|---|
  | u_C (V) | 0 | 1,5 | 3 | 4,6 | 6,1 | 7,6 | 9,2 |

  Questions (p.16) : « 1°) Que se passe-t-il quand on ferme K2 ? Quelle est l'indication du voltmètre ? 2°) Avant
  de fermer K2, le voltmètre peut indiquer une tension non nulle. Expliquer cette possibilité. 3°) […] montrer que
  la charge q augmente avec u_C. 4°) […] figure 9 […] Montrer graphiquement que u_C = kt où k est une constante que
  l'on calculera. 5°) Déterminer la relation entre la charge q du condensateur et la tension u_C à ses bornes. »
  Interprétation : Fig.9 droite par l'origine, **u_C = kt avec k = 0,3 V.s⁻¹** ; u_C = k q/I, d'où q = (I/k)u_C ;
  I/k constante notée C. Remarque : un autre condensateur → même proportionnalité, autre C. (C numérique non
  calculé par le manuel.)
- **§6 (p.19)** — Question d'entrée (VERBATIM) : « En plus de la valeur de la capacité du condensateur, le
  constructeur indique généralement sur le boitier deux valeurs différentes de tensions électriques, que
  représentent-elles? » q = C.u ne peut croître indéfiniment ; étincelles à travers le diélectrique, troué s'il
  est autre que l'air ou le vide ; « le condensateur a claqué ».
- **§7.1 + Expérience complémentaire (p.19–20)** — décharge sans générateur → réservoir d'énergie. Fig.11 :
  générateur de tension continue E réglable, condensateur de très grande capacité C, petit moteur M, K (1 puis 2) :
  le moteur tourne puis s'arrête spontanément. Questions : « 1°) Qu'est ce qui montre dans cette expérience que
  le condensateur est un réservoir d'énergie? 2°) Quelle est l'opération avec laquelle le condensateur est devenu
  ce réservoir d'énergie?. 3°) Expliquer la petite durée de rotation du moteur. »
- **RC intro (p.21, VERBATIM)** — « Le dipôle RC est constitué d'un résistor de résistance R associé en série avec
  un condensateur de capacité C. On se propose d'étudier la variation de la charge q du condensateur en fonction
  du temps dans un tel dipôle lorsque la tension à ses bornes passe brusquement de zéro à une valeur constante E
  ou inversement. L'évolution brusque de la tension constitue l'échelon de tension. »
- **RC §1.1 (p.21)** — Fig.12 (C, R, générateur E, K 1/2) ; Fig.13 : points D, A, B (masse en B), Y1 en D, Y2 en A
  (flèches u_DA, u_AB) ; oscilloscope numérique à mémoire ; K en 1 → Fig.14 (une courbe croissante à palier).
  Questions : « 1°) Identifier la courbe obtenue sur la voie Y1 de l'oscilloscope et celle obtenue sur la voie Y2.
  2°) La charge du condensateur est-elle instantanée ? » Interprétation : u_C = 0 avant ; K en 1 → u_DB = E ;
  u_AB croît jusqu'à E ; q = C u_AB évolue de même.
- **RC §1.2 (p.22–24)** — Fig.15 circuit de charge. Remarque p.23 : à défaut d'oscilloscope à mémoire, GBF en
  créneaux à la place du générateur continu. Fig.19–20 : générateur à **masse flottante** (ou secteur via
  transformateur d'isolement), masse en A, Y1 : u_DA = Ri, Y2 : u_AB (bouton INV) ; oscillogrammes (1) décroissant,
  (2) croissant. Question p.24 : « Dans la figure 20, montrer que l'oscillogramme (1) représente la tension u_DA
  aux bornes du résistor et que l'oscillogramme (2) représente la tension u_AB aux bornes du condensateur. »
- **RC §2.1 (p.24)** — condensateur chargé, K en 2 (Fig.13), Y2 → Fig.21 (u_C décroissant). Questions : « 1°)
  Expliquer l'allure de u_C(t). 2°) La décharge du condensateur est-elle instantanée? » Énergie dissipée dans R.
- **RC §2.2 (p.24–26)** — Fig.22. Remarque p.26 (Fig.26–27) : visualisation simultanée en décharge, générateur à
  masse flottante, Y1 = u_DA (positive en charge, devenue négative), Y2 = u_AB (u_BA changée de signe, positive,
  décroît vers 0).
- **RC §3.1 influence de R (p.26–27)** — montage Fig.13, B à la masse, A sur Y1 (u_C), D sur Y2 (Fig.28). **E = 6 V ;
  C = 1 μF ; R1 = 5, R2 = 10, R3 = 15, R4 = 20 kΩ** ; 5 ms/div, 1 V/div ; Fig.29a–d. Questions : tableau R (kΩ) 5 /
  10 / 15 / 20 — t (ms) pour u_C = 4 V (cases vides) ; influence qualitative de R ; montrer t ∝ R.
- **RC §3.2 influence de C (p.28)** — R = 10 kΩ ; **C1 = 0,5 ; C2 = 2 ; C3 = 5 ; C4 = 10 μF** ; 1 V/div ; 5 ms/div
  (Fig.30a,b) et 50 ms/div (Fig.30c,d) ; même tableau (u_C = 4 V) ; montrer t ∝ C. Remarque : « Les mêmes
  expériences, faites avec la décharge d'un condensateur, conduisent aux mêmes résultats. »
- **RC §3.3 (p.28–30)** — t ∝ R et ∝ C → ∝ RC = « constante de temps, notée τ » ; dimension : R = tension/intensité,
  C = charge/tension → RC = charge/intensité = un temps. Questions : p.28 « Tant au cours de la charge qu'au cours
  de la décharge, u_C(t) est une fonction exponentielle du temps d'exposant (- t/τ). En déduire que τ = RC ne peut
  avoir effectivement que la dimension d'un temps. » ; p.30 « Montrer que l'intersection de la tangente à la
  courbe i(t) avec l'axe des abscisses donne t = τ (Fig.35a et Fig.35b) » ; p.30 « Montrer que les mêmes durées
  4,6 τ et 6,9 τ sont indispensables pour décharger complètement un condensateur respectivement à 1 % et à 1 ‰
  près. »

### Encadrés, définitions, lois et relations (VERBATIM — relus sur l'image de ce manuel)

> **Définition (1.1, p.12)** — « Un condensateur est un composant électrique constitué de deux plaques conductrices
> trés faiblement espacées et séparées par un isolant électrique. Les plaques sont désignées par les armatures du
> condensateur et le matériau isolant est appelé diélectrique. Le condensateur est symboliquement représenté par
> deux traits parallèles qui représentent les armatures (Fig.1). » […] « Étant un dipôle électrocinétique, le
> condensateur a deux bornes reliées directement à ses armatures. Dans le cas où les armatres sont planes et
> parallèles, le condensateur est dit plan. »

> **Conclusion (§3.1, p.15)** — « L'intensité du courant électrique est une grandeur algébrique. Elle est
> positive si le courant circule dans le sens arbitraire choisi et négative si le courant circule dans le sens
> contraire. »

> **Définition (§3.2, p.15)** — « On appelle charge q d'un condensateur, la charge de l'une de ses armatures
> choisie conventionnellement, celle vers laquelle est orienté le sens positif du courant. » (note : « Ne pas
> confondre entre la charge q d'un condensateur et le phénomène de charge » ; Fig.7 : i vers A portant +q, B −q.)

> **Relation i–q (§3.3, p.15)** — « […] Entre les instants t et t+Δt, le courant circulant dans le sens positif,
> transporte la quantité d'électricité Δq>0, ce qui fait augmenter la charge de l'armature A de Δq. L'intensité du
> courant étant la quantité d'électricité transportée (ou traversant une section droite) par unité de temps, on
> a : » **i(t) = lim_{Δt→0} Δq/Δt = dq/dt**

> **Relation charge–tension (§4, p.17)** — « On a ainsi : » **q = C u_C**

> **Capacité (p.17)** — « La charge q d'un condensateur est proportionnelle à la tension u_C à ses bornes : q = C u_C.
> Le facteur de proportionnalité C est une grandeur qui caractérise l'aptitude du condensateur à emmagasiner une
> charge électrique q lorsqu'il est soumis à une tension u_C, appelée capacité du condensateur. C ne dépend que des
> caractéristiques géométriques du condensateur et de la nature du diélectrique. »

> **Unité (p.17)** — « La capacité C d'un condensateur est une grandeur mesurable. Dans le système international
> d'unités, elle s'exprime en Farad (F). Le farad est la capacité d'un condensateur qui, soumis à une différence de
> potentiel de 1 V, prend une charge de 1 C. » « […] le farad est une grande unité de capacité. » 1 mF = 10⁻³ F ;
> 1 μF = 10⁻⁶ F ; 1 nF = 10⁻⁹ F ; 1 pF = 10⁻¹² F ; 1 fF = 10⁻¹⁵ F. Note : unité dédiée à Michael Faraday
> (physicien et chimiste anglais, 1791-1867). Ordres de grandeur : électrochimique μF - F ; mica, céramique pF - nF ;
> papier μF ; tantale 0,1 μF - 0,01 μF ; polypropylène nF - μF.

> **Condensateur plan (§5, p.18)** — « La capacité d'un condensateur plan est proportionnelle à la surface S des
> armatures en regard et inversement proportionnelle à l'écartement e de ses armatures (Fig.10). On peut écrire : »
> **C = ε S/e** — « Le facteur de proportinnalité ε est une constante qui ne dépend que de la nature du
> diélectrique, on l'appelle permittivité absolue du diélectrique. Dans le système international d'unités, ε
> s'exprime en farads par mètre. La permittivité ε_o du vide est : » **ε_o = 1/(36π.10⁹) (F.m⁻¹)** — « La
> permittivité de l'air est pratiquement égale à celle du vide. Tous les autres diélectriques ont une permittivité
> absolue plus grande que celle du vide. » « […] permittivité relative ε_r d'un diélectrique comme étant le
> rapport de sa permittivité absolue sur la permittivité du vide : » **ε_r = ε/ε₀ d'où C = ε_r ε_o S/e**.
> Tableau (ε_r ; ε en 10⁻¹¹ F.m⁻¹) : Vide, air 1 ; 0,885 · Papier paraffiné 2 - 2,5 ; 1,8 - 2,2 · Polystyrène 2 - 3 ;
> 1,8 - 2,7 · Verre 4 - 7 ; 3,5 - 6,2 · Mica 5 - 8 ; 4,4 - 7,1 · Céramique 15 - 2500 ; 13,2 - 2200.

> **Tension de claquage (§6, p.19)** — « On appelle tension de claquage d'un condensateur la plus petite tension
> (en valeur absolue) faisant jaillir une étincelle entre les armatures du condensateur. » « Ainsi, pour éviter de détériorer un
> condensateur, il faut éviter d'appliquer à ses bornes une tension de valeur absolue voisine de la valeur de la tension de
> claquage indiquée par le constructeur. » « La deuxième valeur de
> tension indiquée sur le boitier d'un condensateur est appelée tension de service, elle est d'une valeur nettement
> inférieure à celle de claquage, c'est la tension nominale du composant. »

> **Conclusion (§7.1, p.20)** — « Le condensateur est un réservoir d'énergie potentielle électrique (ou
> électrostatique). Cette énergie se manifeste, lors de la décharge du condensateur, en se transformant en énergie
> thermique dans les différents conducteurs, en énergie cinétique dans un moteur, en énergie lumineuse dans une
> diode LED par exemple... »

> **Énergie (§7.2, p.20)** — « L'énergie électrostatique emmagasinée par un condensateur de capacité C, chargé sous
> une tension u, s'exprime par : » **E_C = ½ C u²** — « Avec C en farad et u en volt, E_C s'exprime en joule. En
> utilisant la relation q = C.u, on obtient d'autres expressions de E_C soit : » **E_C = q²/(2C) = ½ q u** (donnée,
> non démontrée).

> **Conclusion (RC §1.1, p.21)** — « La réponse d'un dipôle RC à un échelon de tension est la charge du
> condensateur. N'étant pas instantanée, celle-ci constitue un phénomène transitoire. »

> **Mise en équation — charge (p.22)** — « En régime transitoire et pendant que le condensateur se charge, le
> circuit de la figure 12 est équivalent à celui de la figure 15. Appliquons la loi des mailles à ce circuit :
> u_DA + u_AB − E = 0, soit : Ri + u_C − E = 0. Or, i = dq/dt = C du_C/dt, d'où : **u_C + RC du_C/dt = E (1)** ou
> bien : **du_C/dt + (1/τ) u_C = E/τ  avec τ = RC**, équation différentielle en u_C avec second membre non nul. Avec
> u_C = q/C et i = dq/dt, la même équation différentielle s'écrit : **dq/dt + (1/τ) q = E/R (2)** ou
> **i + (1/τ) ∫ i dt = E/R (3).** »

> **u_C(t) — charge (p.22)** — « La solution de l'équation différentielle (1) est de la forme : u_C(t) = B + Ae^{−αt}
> où A, B et α sont des constantes à déterminer. A t = 0, u_C = A + B = 0, d'où B = − A. Il vient
> u_C(t) = A(e^{−αt} − 1). La dérivée […] du_C/dt = − αAe^{−αt}. En remplaçant du_C/dt par son expression dans
> l'équation (1), on trouve : A(e^{−αt} − 1) − ατAe^{−αt} = E ; ce qui donne : − A + (1 − ατ)Ae^{−αt} = E. En
> égalisant membre à membre cette équation qui doit être satisfaite pour toute valeur de t, on obtient : A = − E et
> 1 − ατ = 0 d'où α = 1/τ. Ainsi, avec A = − E et α = 1/τ, la tension aux bornes du condensateur s'écrit :
> **u_C(t) = E(1 − e^{−t/τ})** » (Fig.16 : croissante, asymptote E.)

> **q(t) — charge (p.23)** — « q(t) = C.u_C(t), d'où : **q(t) = Q₀(1 − e^{−t/τ}) avec Q₀ = CE.** » « Lorsque t tend
> vers l'infini u_C(t) tend vers E et q vers q_o, le condensateur porte sa charge maximale. » (Fig.17.)

> **i(t) — charge (p.23)** — « On a i = dq/dt. En remplaçant q par son expression, on trouve i(t) = (Q_o/τ) e^{−t/τ}
> ou encore : **i(t) = I_o e^{−t/τ} avec I_o = E/R** » ; « L'intensité i du courant est alors positive au cours de
> la charge du condensateur, résultat attendu du fait que le sens positif du courant est orienté vers l'armature
> située dans le circuit du côté du pôle positif du générateur. » (Fig.18.)

> **Conclusion (RC §2.1, p.24)** — « Dans un dipôle RC, un condensateur chargé se décharge progressivement dans le
> résistor. »

> **Mise en équation — décharge (p.24–25)** — « […] à l'instant t = 0, la tension à ses bornes est égale à E. […]
> u_C + u_R = 0 et u_R = Ri d'où u_C + Ri = 0. Or, i = dq/dt et q = Cu_C, on aura : **u_C + RC du_C/dt = 0** ou
> bien **du_C/dt + (1/τ) u_C = 0 (4).** On obtient une équation différentielle en u_C sans second membre. On
> obtient aussi les équations différentielles (5) et (6) respectivement en q et en i : **dq/dt + (1/τ) q = 0 (5) ;
> i + (1/τ) ∫ i dt = 0 (6).** »

> **u_C(t) — décharge (p.25)** — « La solution de l'équation différentielle (4) est de la forme : u_C(t) = A e^{−αt}
> où les constantes A et α sont déterminées par les conditions initiales : A t = 0, u_C = E, d'où A = E. En
> remplaçant u_C et du_C/dt par leurs expressions dans (4), on obtient : − α A e^{−αt} + (1/τ) A e^{−αt} = 0, ce
> qui entraine : (− α + 1/τ)A e^{−αt} = 0 ∀t. D'où − α + 1/τ = 0, ce qui donne : α = 1/τ. Il vient finalement :
> **u_C(t) = E e^{−t/τ}** » (Fig.23.)

> **q(t) — décharge (p.25)** — « **q(t) = Q_o e^{−t/τ} avec Q_o = CE** » ; « Lorsque t tend vers l'infini, q tend
> vers zéro ; le condensateur est déchargé. » (Fig.24.)

> **i(t) — décharge (p.26)** — « On a : i = dq/dt, donc : i(t) = − (E/R) e^{−t/τ} ou encore :
> **i(t) = − I_o e^{−t/τ} avec I_o = E/R** » ; « On note bien pour i(t) le signe contraire de celui de l'intensité
> du courant de charge, c'est à dire que le courant de décharge circule dans le sens contraire de celui de charge
> (Fig.25). » (Fig.25 : i part de −I_o, croît vers 0 ; note : le générateur doit être à masse flottante.)

> **Constante de temps (p.28)** — **τ = RC : constante de temps**

> **Définition (p.29)** — « La constante de temps τ est une grandeur caractéristique du dipôle RC, elle renseigne
> sur la rapidité avec laquelle s'établit la tension u_C = E entre les armatures du condensateur. La charge et la
> décharge du condensateur sont d'autant plus rapides que la constatnte de temps τ est plus petite. »

> **Détermination de τ (p.29)** — « Par calcul direct : Connaissant les valeurs de C et de R, on peut calculer
> directement la valeur de la constante de temps τ = RC. » · « Détermination graphique (première méthode) : Pour
> déterminer τ, on trace la tangente à la courbe de charge ou de décharge u_C(t) au point d'abscisse t = 0. Cette
> tangente a pour équation u_C = a t, a étant son coefficient directeur dont la valeur est donnée par :
> a = (du_C/dt)_{t=0}. Or : du_C/dt = (E/τ) e^{−t/τ}, alors (du_C/dt)_{t=0} = E/τ. Finalement, l'équation de la
> tangente s'écrit : u_C = E t/τ. L'intersection de cette tangente avec la droite u_C = E donne t = τ (fig.31). »
> Remarque : « La même méthode […] s'applique à la courbe de décharge. L'intersection de la tangente à la courbe
> u_C(t) à l'origine avec l'axe des abscisses donne t = τ (fig.32). » · « Détermination graphique (deuxième
> méthode) : Dans le cas de la charge du condensateur, en remplaçant t par τ dans l'expression de u_C(t), on
> obtient : u_C = E(1−e⁻¹) = 0,63 E. Donc, par lecture graphique de l'abscisse du point de la courbe u_C(t)
> d'ordonnée 0,63E, on obtient la valeur de τ (Fig.33). τ correspond donc au temps nécessaire pour charger un
> condensateur à 63%. Dans le cas de la décharge, […] on obtient u_C = E e⁻¹ = 0,37E. τ est alors l'abscisse du
> point de la courbe u_C(t) d'ordonnée 0,37E (Fig.34). » Remarque : « On peut déterminer τ en traçant la tangente
> à la courbe i(t) au point d'abscisse t = 0. »

> **Intérêt pratique de τ (p.30)** — u_C n'atteint E (charge) ou 0 (décharge) qu'au bout de durées infinies, « ce
> qui n'est pas physiquement pratique. On admet alors que le condensateur est complètement chargé ou déchargé quand
> la différence relative entre la valeur atteinte par u_C et la valeur asymptotique E (pour la charge) ou zéro
> (pour la décharge) ne dépasse pas 1%. Pour la charge par exemple : (E − u_C)/E ≤ 1% ce qui signifie que
> E − u_C ≤ 0,01 E d'où u_C ≥ 0,99 E. Or, u_C = E(1 − e^{−t/τ}). Donc, pour t_c = t_charge, on a : 0,99E =
> E(1 − e^{−t/τ}) d'où 0,99 = (1 − e^{−t/τ}), ce qui entraine e^{−t/τ} = 0,01, d'où Log e^{−t/τ} = Log 0,01 ou bien
> t_c/τ = 2Log10 = 4,6, d'où **t_c ≃ 5 τ**. Quand l'étude se veut plus précise, on exige une erreur relative ne
> dépassant pas 1‰. Avec un calcul semblable au précédent, on aboutit à t_c = 6,9 τ ≃ 7 τ pour avoir u_C = 0,999 E. »

> **Récapitulation (p.30)** — Durée t : 0 | τ | 4,6 τ | 6,9 τ ; Charge u_C : 0 | 0,63 E | 0,99 E | 0,999 E ;
> Décharge u_C : E | 0,37 E | 0,01 E | 0,001 E.

### L'essentiel (p.31, VERBATIM)

« ■ Un condensateur est un ensemble de deux plaques conductrices séparées par un isolant. Il se charge lorsqu'on
établit entre ses bornes une tension continue et se décharge lorsqu'on le ferme sur un récepteur. ■ En désignant
par q la charge portée par l'armature du condensateur vers laquelle est orienté le sens positif du courant, on a :
**i = dq/dt** ■ La capacité C est une grandeur mesurable caractérisant la faculté d'un condensateur à stocker une
charge q sous une tension u : **q = C.u** ■ La capacité C d'un condensateur plan est proportionnelle à la surface S
en regard des armatures et inversement proportionnelle à la distance e qui les sépare : **C = ε S/e** [imprimé « e »
à la place de ε dans l'élément gauche : coquille, lire ε] où ε est la permittivité absolue du diélectrique. ■ Sous
une tension u, un condensateur de capacité C emmagasine une énergie potentielle électrique : **E_C = ½ C u²**
■ Toute décharge d'un condensateur s'explique par une restitution d'énergie emmagasinée. ■ Un dipôle RC soumis à
un échelon de tension E répond par une évolution de la tension u_C aux bornes du condensateur régie par la loi :
**u_C(t) = E(1 − e^{−t/τ})** où τ = RC est la constante de temps du dipôle. ■ Quand un dipôle RC chargé est fermé
sur lui même, la tension u_C aux bornes du condensateur, initialement égale à E, évolue selon la loi :
**u_C(t) = E e^{−t/τ}** ■ La constante de temps τ = RC renseigne sur la rapidité de la charge et de la décharge du
condensateur. »

### Exercice résolu (p.32–33)

**Énoncé** — Fig.1 : générateur E, R1, K (1 : charge à travers R1 ; 2 : décharge dans R2), condensateur C ;
acquisition par ordinateur. « 1°) En plaçant le commutateur dans la position 1, on obtient la courbe u_C(t) de la
figure 2. a) Interpréter l'allure […]. b) Déterminer graphiquement le temps mis par le condensateur pour se
charger. Pour cela on suppose que le condensateur est complètement chargé quand u_C = E à 1% près. 2°) On bascule
le commutateur dans la position 2, le condensateur se décharge complètement dans le résistor de résistance
R2 = 1 kΩ au bout d'une durée t = 250 ms. La courbe de décharge u_C(t) est représentée sur la figure 3.
a) Interpréter […]. b) Déterminer graphiquement la constante de temps τ2 et en déduire la valeur de la capacité C
du condensateur. 3°) Déterminer la valeur de la résistance R1. » (Fig.2 : u_C de 0 à 6 V, t en s ; Fig.3 : part de
6 V, t 50 … 200 ms ; E = 6 V se lit sur les figures.)
**Solution** — 1°a) u_C + u_R1 − E = 0 → τ1 du_C/dt + u_C = E, τ1 = R1C ; u_C(t) = E(1 − e^{−t/τ1}). 1°b)
u_C(θ) = 0,99E → θ/τ1 = 2 log10, θ = 4,6 τ1 ≃ 5 τ1 ; tangente à l'origine → **τ1 = 0,1 s, θ = 0,5 s**. 2°a) u_C +
u_R2 = 0 → τ2 du_C/dt + u_C = 0 [imprimé « où τ1 = R2C » : coquille, lire τ2] ; u_C(t) = E e^{−t/τ2}. 2°b) tangente →
**τ2 = 50 ms** ; C = τ2/R2 = **50 μF**. 3°) R1 = τ1/C = **2 kΩ**.

### Exercices à résoudre (p.34–37) — 13 exercices (identiques à 223433)

- **Ex. 1 — V/F** (p.34), 9 items : q = CU ; caractérisé par sa capacité ; « ne restitue jamais la même quantité
  d'énergie emmagasinée » ; i = dq/dt ; i maximale au début de la charge et nulle à la fin ; i_max de charge = E/R ;
  « au début de la décharge, i nulle » ; τ par tangente à l'origine de la décharge u_C(t) ; « Un condensateur de
  charge 2q emmagasine l'énergie : E_C = q²/2C ». Pas de réponse.
- **Ex. 2 — QCM** (p.34), 6 items : I. 5 s à 1,2 mA → Q = a- 8.10⁻³ C / b- 6.10⁻³ C / c- 5.10⁻³ C ; II. q
  quadruplée si tension ×2 / tension ×4 / capacité ÷4 ; III. C = 10 μF, τ = 2 ms → R = 20 Ω / 200 Ω / 2000 Ω ;
  IV. τ = durée de charge complète / à moitié chargé / chargé à 63 % ; V. ralentir la décharge avec R réglable :
  diminuer R / augmenter τ en augmentant R / diminuer τ en diminuant R ; VI. énergie doublée si on double q / C / u.
  Pas de réponse.
- **Ex. 3** (p.35) : plan, S = 1 m², ε_r = 8, e = 0,1 mm ; 1°) C ; 2°) énergie sous 50 V. Rép. p.318 : **0.7 μF ;
  8.8 10⁻³ J** [?].
- **Ex. 4** : C = 20 μF, générateur de courant I = 1,8 μA ; 1°) q après 10 s ; 2°) a) u_AB, b) énergie à t = 10 s.
  Rép. : **18 μC [imprimé « μc »] ; 0.9 V ; 8.1 10⁻⁶ J**.
- **Ex. 5** : C = 3 μF, R = 80 kΩ, E = 12 V ; 1°) τ ; 2°) après 2 s : a) u_C, b) i. Rép. : **0.24 s ; 12 V ;
  3.6 10⁻⁸ A**.
- **Ex. 6** : E = 6 V, C = 2 μF, R = 10 kΩ, K ; 1°) i à la fermeture ; 2°) τ ; 3°) durée pour u_C = 0,99E ;
  4°) allure de u_C(t). Rép. : **6 10⁻⁴ A ; 20 ms ; 92 ms**.
- **Ex. 7** : R = 100 Ω, E = 5 V ; t (μs) 0 ; 0,5 ; 1 ; 1,5 ; 2 ; 3 ; 4 ; 5 — u_C (V) 0 ; 2,2 ; 3,3 ; 4 ; 4,3 ; 4,7 ;
  4,8 ; 4,9 ; 1°) schéma ; 2°) graphe ; 3°) τ ; 4°) C. Rép. : **3°) 1 μs ; 4°) 10⁻⁸ F**.
- **Ex. 8** : « 0,12 dq/dt + q = 12.10⁻⁵ » (E + dipôle RC) ; 1°) τ ; 2°) E = 12 V → R ; 3°) C. Rép. : **0.12 s ; 12 kΩ ;
  10 μF**.
- **Ex. 9** (synthèse, p.35–36) : E, R, C = 10 μF en série ; 1°) schéma et connexions oscilloscope pour u_C et u_R ;
  2°) identifier les oscillogrammes (Courbe (a) croissante vers 12 V, Courbe (b) décroissante depuis 12 V ; u (V)
  0–12 par 2, t (ms) 100–400) ; 3°) E, τ ; 4°) R. Rép. : **3°) 12 V, 150 ms ; 4°) 15 kΩ**.
- **Ex. 10** (p.36) : C = 22 μF, E = 6 V (alimentation stabilisée), R = 1 kΩ, condensateur déchargé, K fermé à t = 0 ;
  1°) q charge de l'armature B, sens positif pour i = dq/dt ; 2°) équation différentielle en q ; 3°) q(t) =
  α.(1 − e^{−t/β}) : a) α, β (expressions, valeurs) ; b) i(t) ; 4°) a) t_{1/2} pour q = ½CE, comparer à τ ; b)
  instant où q = CE/4. Pas de réponse.
- **Ex. 11** (p.36–37) : C, R en série, K (1 : générateur ; 2 : décharge), points A, B, G, interface + ordinateur ;
  K en 1 depuis longtemps ; courbe u (V) décroissante depuis 5 V, t (ms) 0–80 ; 1°) état à t = 0 (K en 2) ; 2°) la
  courbe ; 3°) manipulation ; 4°) signe de i en décharge ; 5°) relations i–u_BG, q_A–u_AB, i–q_A, u_BG–u_AB ;
  6°) montrer (1/α) du_AB/dt + U_AB = 0 [imprimé « U_AB »], α en fonction des caractéristiques. Pas de réponse.
- **Ex. 12** (p.37) : C = 5 μF chargé sous u_AB = U_o > 0, inséré dans un circuit (C et R en parallèle, voie Y en A,
  B à la masse, K) ; réglages 2,5 ms/div et 2 V/div ; 1°) équation différentielle en u_AB ; 2°) R1 = 500 Ω → courbe 1,
  R2 → courbe 2 (même graphe, axes sans valeurs chiffrées) : a) U_o ; b) résistance la plus grande, méthode et
  calcul de R2 ; 3°) a) énergie emmagasinée ; b) énergie E1 dissipée par effet Joule dans R1 ; c) E1 varie-t-elle
  si R1 → R2 ? Pas de réponse.
- **Ex. 13 — Étude de texte « Le défibrillateur cardiaque »** (p.37) : « circuit à choc exponentiel tronqué »,
  C = 32.10⁻⁶ F, U ≈ 5 kV, libération en « une dizaine de millisecondes », résistance du thorax ≈ 75 Ω (adulte) ;
  1°) assimiler à un circuit RC ; 2°) τ ; 3°) ordre de grandeur de l'énergie ; 4°) expliquer « circuit à choc
  exponentiel tronqué ». Pas de réponse.

**Fiche technique (p.38–39)** — « Mesure d'une tension continue aux bornes d'un condensateur » : résistance R_v du
voltmètre décharge le condensateur (constante R_vC ; numérique ≈ 10 MΩ ; aiguille ≈ 20 kΩ/V soit 200 kΩ sur 10 V ;
ex. C = 5600 μF → 56000 s ; suiveur TL081 ≈ 10¹² Ω, ex. C = 10 nF → 10⁴ s) ; oscilloscope (1 MΩ, 50 pF), R = 20 kΩ,
C = 125 nF : u = R_osc/(R + R_osc)·E(1 − e^{−t/τ}), τ = R·R_osc/(R + R_osc)·C, erreur 2 % ; R_oscC = 125 ms →
décharge non enregistrable sans suiveur ; montage via u_C = E − u_R (d'après web.ac-reims.fr).
**En savoir plus (p.40–41)** — « La foudre et les paratonnerres » : nuage–Terre comme énorme condensateur,
ionisation de l'air vers 10 000 V par cm, paratonnerres, précautions (d'après Encarta 2006).

### Écart avec Sciences expérimentales (223433)

- **Ce que ce manuel ajoute** : **rien** dans le chapitre 1 (aucune notion, activité, figure, donnée, exercice ou
  réponse en plus).
- **Ce qu'il retire** : **rien**. Mêmes 32 pages (10–41), mêmes 13 exercices, mêmes 7 réponses (ex. 3–9), même
  exercice résolu, même fiche technique et même « En savoir plus ».
- **Écarts constatés hors contenu** : (i) pagination des réponses : p.**318** (320 p. au total) au lieu de p.316 ;
  (ii) p.31, rendu typographique de l'encadré de la loi u_C(t) (glyphes), sans changement de formule ; (iii) l'avant-
  propos p.3 de ce manuel « Mathématiques » dit « conforme au programme officiel 4e Sciences expérimentales et publié
  en septembre 2009 » (le texte de l'avant-propos du manuel Sciences exp. dit « de 4e année Sciences Expérimentales ») : la
  couverture (p.1) porte bien « Mathématiques » ; le programme officiel Mathématiques n'étant pas au corpus (R-3),
  l'identité du chapitre avec 223433 est constatée sur le manuel, non sur le programme ; (iv) le sommaire (p.4–5)
  situe les ouvertures de chapitre aux p.11, 43, 79, 111, 139, 163… (les chapitres suivants, hors périmètre ici,
  ne sont pas comparés).

### Bornes de scope (chapitre 1, section Mathématiques)

- ✅ **INCLUS** (mêmes bornes que Sciences exp., le contenu étant identique) :
  - Condensateur : définition (armatures, diélectrique), symbole, condensateur plan ; types usuels (air, diélectrique
    solide roulé, électrochimique) ; ordres de grandeur de C par type.
  - Charge et décharge qualitatives (galvanomètre balistique, électrons, +q / −q) ; le condensateur stocke des charges.
  - Intensité algébrique (sens positif arbitraire ; DEL tête-bêche ; signe de u_R = Ri) ; charge q d'un condensateur ;
    **i = dq/dt**.
  - Charge à **courant constant** : q = I.t, u_C = kt, **q = C u_C**, C = I/k ; **farad** et sous-multiples
    mF, μF, nF, pF, fF.
  - **C = εS/e**, ε₀ = 1/(36π·10⁹) F.m⁻¹, **ε_r = ε/ε₀**, C = ε_r ε₀ S/e ; tableau de permittivités.
  - Tension de claquage, tension de service (nominale).
  - Énergie : réservoir d'énergie potentielle électrique ; **E_C = ½Cu² = q²/2C = ½qu** (formule donnée) ; énergie
    dissipée par effet Joule = énergie emmagasinée (ex. 12).
  - Dipôle RC : échelon, phénomène transitoire ; **équations différentielles** par la loi des mailles en u_C, q, i
    (avec ∫ i dt), charge et décharge ; résolution par **solution de forme imposée** B + Ae^{−αt} / Ae^{−αt} et
    identification (conditions initiales, « pour toute valeur de t ») ; identification α, β ou τ, R, C sur une
    équation numérique (ex. 8, ex. 10).
  - **u_C(t), q(t), i(t)** en charge (Q₀ = CE, I₀ = E/R, i > 0) et en décharge (i = −I₀e^{−t/τ}, i < 0) ; allures ;
    calcul à un instant donné ; instant où q atteint une fraction de CE (ex. 10, passage au Log).
  - Oscilloscope numérique / à mémoire (voies Y1/Y2, masse, bouton INV, masse flottante, u_DA = Ri image de i) ;
    GBF en créneaux (mention) ; acquisition par ordinateur.
  - Influence de R et de C (lecture d'oscillogrammes, t ∝ R, t ∝ C) ; **τ = RC**, dimension d'un temps ; τ par calcul,
    **tangente à l'origine** (u_C charge/décharge, i(t)), lecture **0,63 E / 0,37 E** ; **4,6 τ ≃ 5 τ (1 %)**,
    **6,9 τ ≃ 7 τ (1 ‰)** ; tableau récapitulatif.
  - Calculs types : C d'un condensateur plan, q = It, u = q/C, E_C ; τ, R, C ; I₀ = E/R ; lecture graphique de E et
    τ ; application au flash et au défibrillateur.
- ⛔ **EXCLU** (absent du chapitre) :
  - Associations de condensateurs (série/parallèle), capacité équivalente.
  - Champ électrique entre armatures, force électrostatique, densité d'énergie ; démonstration de C = εS/e ;
    **démonstration de E_C = ½Cu²** (formule seulement donnée).
  - Séparation des variables / intégration de l'équation différentielle (seule la solution de forme imposée est
    utilisée) ; notation « ln » (le manuel écrit « Log »).
  - Réponse à un signal créneau étudiée quantitativement (remarque seulement) ; régime sinusoïdal ; dipôles RL et
    RLC (chapitres suivants).
  - Influence de E sur la durée de charge ; demi-vie t_{1/2} = τ·Log2 en résultat de cours (exercice 10 seulement).
  - Suiveur de tension, impédance d'entrée de l'oscilloscope, résistance interne du voltmètre : fiche technique
    seulement ; foudre et paratonnerres : lecture.

### Lecture

- **Couche texte lue** (`/root/.cache/yqa-manuels/223432/txt/pNNN.txt`) : p.1, 3, 4, 5, 10 à 41 (les 32 pages) et
  318 (réponses du chapitre 1 : ex. 3 à 9 ; le reste de la page = chapitres 2 à 6). Comparaison mécanique mot à mot
  avec 223433 p.10–41 : identique (hors 2 lignes de formule p.31).
- **Pages vues sur image (110 dpi, PDF 223432P00)** : **20** — 4, 13, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 29,
  30, 33, 35, 36, 37 (pleine page) ; 31 (pleine page 110 dpi, et encadré à 220 dpi, dans les deux manuels) ; 318 (recadrage 200 dpi, réponses
  du chapitre 1). **Comparaison image intégrale** : les 32 pages 10–41 rendues à 110 dpi pour 223432 et 223433 et
  différenciées par script (seuil 60/255) : 0 pixel de différence sur 31 pages, 463 px sur p.31 (encadré de la loi
  u_C(t)), lui-même relu. Les pages non revues une à une (10, 11, 12, 14, 19, 24, 27, 28, 32, 34, 38, 39, 40, 41) sont
  donc **pixel-identiques** aux pages de 223433 que la section de référence a lues sur image (R-7 de celle-ci).
- **Sondage ≥ 1 page sur 10 parmi les plus denses** : fait sur 10 pages denses (15, 18, 22, 25, 29, 30, 31, 33,
  35, 36) ; aucun écart avec la section de référence. **Écarts couche texte / image** (ceux de la référence, tous
  retrouvés) : p.15 l'encadré i(t) = lim Δq/Δt = dq/dt n'existe que sur l'image ; p.18 ε, ε₀, ε_r perdus ; p.22–25
  α, τ, exposants −t/τ, ∫, ∀ perdus ; p.29–30 (du_C/dt)_{t=0}, ≤, ≥, ≃, « 1 ‰ » dégradés ; p.35 ex. 8
  « 12.10⁵ » en texte, **12.10⁻⁵** sur l'image ; p.36 q = CE/4 éclaté ; p.37 ex. 11 6°) α perdu ; p.318 réponses
  lisibles mais colonnes entremêlées avec les chapitres 2–6.
- **Doutes [?]** :
  1. **Réponse ex. 3 2°)** : imprimé « 8.8 10⁻³ J » (vérifié sur l'image p.318) ; recalcul : C = 8 × 8,85·10⁻¹² × 1 /
     10⁻⁴ ≈ 0,71 μF, ½ C u² (u = 50 V) ≈ 8,8·10⁻⁴ J → facteur 10 probable dans le manuel ; ne pas reprendre tel quel.
  2. **Exercice résolu 2°a)** : « où τ1 = R2C » = coquille, lire τ2 = R2C (image p.33).
  3. **L'essentiel** : « C = e S/e » = coquille, lire ε — coquille vérifiée sur l'image pleine page de 223432 p.31.
  4. Ex. 11 6°) : « U_AB » majuscule = coquille probable pour u_AB (image p.37).
  5. Ex. 12 : graphe sans aucune valeur chiffrée sur les axes (courbes 1 et 2 seulement) ; U_o et R2 non lisibles
     sur la figure ; aucune réponse fournie (la courbe 2 reste au-dessus de la courbe 1 ⇒ R2 > R1, déduction).
  6. Réponses fournies seulement pour les ex. 3 à 9 ; ex. 1, 2, 10–13 sans réponse ; tableaux des §3.1 et §3.2
     (u_C = 4 V) laissés vides ; C de la manipulation §4 non calculé.
  7. Fig.3 (p.13) : R ne figure que dans la branche de la position 2 (confirmé sur l'image de 223432) ; le texte ne
     précise pas sa place.
  8. Fig.13–14 (p.21) : Y1 en D (u_DB = E), Y2 en A (u_AB) ; Fig.14 ne montre qu'une courbe croissante à palier ;
     identification des voies à confirmer par l'enseignant.
  9. Le programme officiel de la section **Mathématiques** n'est pas au corpus (R-3) : l'avant-propos du manuel
     renvoie par erreur apparente au programme « Sciences expérimentales » ; présence de E_C = q²/2C, C = εS/e et de
     la fiche technique au programme Mathématiques non vérifiée ; bornes établies sur le manuel seul.

## 2.2 Chapitre 2 — La bobine ; le dipôle RL (manuel 223432, p.42–77)

**Constat d'ensemble (comparaison page à page avec 223433, p.42–77)** : le chapitre est **le même texte, les mêmes
figures, les mêmes valeurs, les mêmes exercices, dans le même ordre et sur les mêmes numéros de page** que celui du
manuel Sciences expérimentales (section « 2.2 » de `bac-sciences-exp/physique.md`, validée R-7). Mesure faite : les 36
pages p.42–77 de 223432 et de 223433 rendues en PNG à 80 dpi et comparées pixel à pixel → **32 pages sans écart
de contenu** (p.44, 46, 52, 56 : écarts de rendu ≤ 10 %) ; 4 pages diffèrent (p.63, 64, 65, 67) **uniquement par la composition typographique** (voir
« Écart »). Toute la section ci-dessous vaut donc « identique à 223433 p.X » ; elle est néanmoins transcrite en
compact, chaque encadré relu sur l'image de 223432 (liste en « Lecture »). Seule la page des réponses change de
numéro : **p.318** (chapitre 2, colonne de gauche + début de la colonne centrale) au lieu de p.316 dans 223433 ; le
contenu des réponses est identique.

Bandeau courant : « Evolution de systèmes ◆ La bobine ; le dipôle RL ». Deux parties : « L'INDUCTION
ÉLECTROMAGNÉTIQUE » (p.44–56, §1 à 6) et « LE DIPÔLE RL » (p.57–66, §1 à 3), puis L'essentiel (p.67), Exercice résolu
(p.68–70), Exercices (p.71–76), En savoir plus (p.77). Pas de « fiche technique ».

**Page d'ouverture (p.43)** — identique à 223433 p.43 : « LA BOBINE / LE DIPÔLE RL », photo de transformateur ;
accroches : « ◆ Pourquoi, les transformateurs ne peuvent pas être utilisés en courant continu ? ◆ Comment
fonctionnent les ralentisseurs électromagnétiques des véhicules “poids lourds” ? » (réponses §6.2 p.56 et p.77).

**Objectifs (p.42, lus sur l'image)** — « ◆ Mettre en évidence expérimentalement le phénomène d'induction
électromagnétique. ◆ Appliquer la loi de Lenz. ◆ Reconnaître les facteurs dont dépend la f.e.m. d'auto-induction. ◆
Calculer l'énergie emmagasinée dans un solénoïde. ◆ Établir, pour un dipôle RL soumis à un échelon de tension,
l'équation différentielle qui régit les variations de l'intensité i du courant parcourant la bobine en fonction du
temps. ◆ Déterminer graphiquement la constante de temps τ = L/R à partir des courbes de réponse u_L(t) ou i(t) d'un
dipôle RL. »

**Prérequis (p.42)** — SAVOIR : « Définir un champ magnétique. Définir une ligne de champ magnétique. Définir le
vecteur champ magnétique. Définir un champ magnétique uniforme. Enumérer les caractéristiques d'un hamp magnétique
créé par un courant continu circulaire (solénoïde). » (« hamp » : coquille imprimée.) — SAVOIR FAIRE : « Identifier
les pôles d'un aimant et les faces d'une bobine. Mettre en évidence expérimentalement l'existence d'un champ
magnétique. Déterminer les caractéristiques d'un vecteur champ magnétique. Reconnaître un champ magnétique uniforme à
partir de la forme de son spectre. »

**Plan** (titres lus dans le corps ; identique à 223433) :
- *L'induction électromagnétique* — 1 Le phénomène (1.1 courant induit par déplacement relatif aimant-bobine ; 1.2
  autre mode de production) · 2 Loi de Lenz · 3 La f.e.m. d'induction · 4 L'auto-induction (4.1 mise en évidence ;
  4.2 la f.e.m. d'auto-induction ; 4.3 facteurs dont dépend l'inductance ; 4.4 relation tension-intensité) · 5 Énergie
  magnétique emmagasinée dans une bobine · 6 Applications (6.1 alternateurs ; 6.2 transformateurs).
- *Le dipôle RL* — 1 Réponse à un échelon de tension (1.1 expérimental ; 1.2 théorique) · 2 Rupture du courant (2.1
  expérimental ; 2.2 théorique) · 3 Influence des grandeurs caractéristiques (3.1 de R ; 3.2 de L ; 3.3 constante de
  temps).
- L'essentiel (p.67) · Exercice résolu (p.68–70) · Tests rapides (ex.1–2, p.71) · Exercices d'application (ex.3–9,
  p.72–73) · Exercices de synthèse (ex.10–14, p.74–76) · En savoir plus (p.77).

Texte d'introduction (p.44, identique) : « Une bobine est un dipôle électrocinétique constitué d'un enroulement dans
le même sens, de fil conducteur recouvert d'un vernis isolant. De ce fait, elle a une résistance électrique interne.
Un tel dipôle placé dans un circuit électrique, se comporte-t-il alors comme un résistor vis à vis du courant
électrique ? La bobine est-elle, comme le condensateur, un réservoir d'énergie ? »

### Partie A — L'induction électromagnétique : manipulations (identiques à 223433 p.44–56)

- **1.1 Exp.1** (p.44, Fig.1–2) — bobine fermée sur milliampèremètre à zéro central ; approcher / éloigner un pôle
  d'un aimant : déviation d'un sens / du sens contraire, retour à zéro à l'arrêt ; idem en déplaçant la bobine.
  **Exp.2** (p.44–45, Fig.3–4) — bobine (B1) sur résistor R, oscilloscope à mémoire, u_R(t) : approche du pôle nord →
  impulsion négative (4a), éloignement → impulsion positive (4b) ; approche plus rapide → pic plus prononcé. Questions
  1°–3°. Conclusion (p.45) : « Avec un déplacement relatif bobine-aimant, on peut produire un courant électrique dans
  la bobine en circuit fermé. Un tel courant électrique est appelé courant induit, alors que l'aimant est appelé
  inducteur. L'intensité du courant induit est d'autant plus grande que le déplacement relatif bobine-aimant est plus
  rapide. »
- **1.2** (p.45–46, Fig.5–6) — (B1) dans un solénoïde (B2) alimenté par GBF ; u_R(t) sur Y1, u(t) sur Y2 : tension
  sinusoïdale aux bornes de (B2) → tension de forme semblable aux bornes de (B1) ; générateur continu : « il ne se passe
  plus rien dans la bobine (B1), une fois le courant y est établi ». Constatation : « La variation de l'intensité du
  courant électrique dans une bobine produit un courant induit dans une autre bobine en circuit fermé à proximité de
  la première. Le courant électrique variable, qui est à l'origine du courant induit, est appelé courant inducteur,
  tandis que le circuit dans lequel il circule est appelé circuit inducteur. »
- **2 Loi de Lenz** (p.46–48, Fig.7a–d ; image p.47 vue) — pôle sud : approche (7a) → impulsion **positive** (7c) ;
  éloignement (7b) → impulsion **négative** (7d). Questions 1°–4° (signe de u_R, vecteur b⃗ du courant induit, nom de
  la face, comparaison 4a/4b, opposition à la cause). Tableau p.47 (lu sur l'image) : « Sens de B⃗ : de l'aimant vers
  la bobine | de la bobine vers l'aimant » ; « Valeur de B⃗ : ‖B⃗‖ augmente » ; « Sens du courant induit : La bobine
  présente sa face nord au pôle nord de l'aimant | La bobine présente sa face sud au pôle sud de l'aimant » ; « Effets
  : La bobine présente à l'aimant la face de même nom que le pôle de l'aimant qui est de son côté : répulsion
  bobine-aimant ⇕ Ayant le sens contraire de celui de B⃗, le vecteur champ b⃗ créé par le courant induit s'oppose à
  l'augmentation de ‖B⃗‖. » Éloignement (p.48) : attraction aimant-bobine, b⃗ plutôt de même sens que B⃗ « afin de
  compenser la diminution de la valeur de ce dernier » ; « Le champ magnétique créé par le courant induit est appelé
  champ induit. » [p.47 : « le vecteur champ inducteur b⃗ » en minuscule, coquille de notation.]
- **3 f.e.m. d'induction** (p.48) — courant induit sans générateur : « une f.e.m. délocalisée ; elle est là, partout
  dans le circuit induit. Elle prend naissance dans le circuit avec la cause et cesse avec la cause. Si le circuit
  induit est ouvert, la f.e.m. se manifeste par l'apparition d'une tension à ses bornes. Cette force électromotrice
  est appelée force électromotrice d'induction ou force électromotrice induite. »
- **4.1 Auto-induction** (p.48–49, Fig.8) — (R ajustable + lampe L1) ∥ (bobine à noyau de fer doux + lampe L2),
  lampes identiques, R = résistance de la bobine ; fermeture : L1 brille tout de suite, L2 atteint l'éclat maximal
  « qu'avec un retard de quelques millièmes de secondes ». Questions 1°–2°. Termes : auto-induction, f.e.m.
  d'auto-induction (auto-induite).
- **4.2 f.e.m. d'auto-induction** (p.49–51, Fig.9–11) — R₀, bobine longue (r négligeable devant R₀), GBF à masse
  flottante ; u_AB (Y1) triangulaire, u_BC (Y2, bouton INV) carrée. u_AB = R₀ i ; u_BC = −e + r i ≃ −e ; sur [nT,
  nT+T/2] u_BC = +U₀ donc e = −U₀, sur [nT+T/2, (n+1)T] u_BC = −U₀ donc e = +U₀ (1) ; u_AB = a₁t + b₁, a₂ = −a₁, di/dt
  = ± a₁/R₀ (2) ; « e/(di/dt) = −U₀R₀/a₁ » ; « e = − L di/dt, où L = U₀R₀/a₁ est une constante positive appelée
  inductance » (image p.51 vue).
- **4.3 Facteurs de L** (p.51–52, Fig.12a–d) — même manipulation, fréquence changée, quatre bobines :
  (B1) N=500, ℓ=20 cm, D=10 cm ; (B2) 500, 30, 10 ; (B3) 500, 20, 15 ; (B4) 250, 20, 10 (tableau lu sur l'image p.51).
  Questions : L augmente avec N, diminue quand ℓ augmente ; influence de la section ; dépendance en fréquence.
- **4.4 Tension-intensité** (p.53, Fig.13–14) — modèle (L en série avec r) ; u_AB = u_AC + u_CB = −e + r i, e = −L di/dt
  ⇒ encadré « u_AB = L di/dt + r i » ; coupure brusque : L di/dt prépondérant.
- **5 Énergie magnétique** (p.53–56, Fig.15 ; images p.54–55 vues) — bobine L = 10 mH, générateur E = 6 V, diode D,
  condensateur C = 5 μF, voltmètre numérique, milliampèremètre ; K fermé : I = 240 mA, tension nulle aux bornes de C ;
  après ouverture u_AM négative. Questions 1°–5° (p.54). u_NM = r i + L di/dt ; permanent : u_NM = r i (Joule) ; « p =
  + u_NM.i, ce qui donne : p = r.i² + Li di/dt » ; encart p.55 : « p = ri² + Li di/dt = ri² + d/dt(½Li²) ; ri² :
  puissance dissipée par effet Joule ; d/dt(½Li²) : puissance magnétique p_L ; Or p_L = dE_L/dt. Donc, E_L = ½L.i² ».
  Ouverture : la bobine restitue toute son énergie au condensateur, la diode l'empêche de se décharger dans la bobine.
  Étincelle de rupture (p.55–56) : durée de transfert « de l'ordre de 1ms », tension très élevée, ionisation de l'air ;
  précautions (condensateurs) ; allumeurs de cuisinières à gaz, soudage à l'arc, amorçage de tube néon.
- **6 Applications** (p.56) — 6.1 alternateur (énergie mécanique → électrique ; induit mobile / fixe ; alternateur de
  voiture Fig.16 : induit fixe = stator, inducteur = aimant cylindrique multipolaire = rotor). 6.2 transformateur
  (Fig.17) : « quadripôle qui permet d'abaisser ou d'augmenter une tension alternative » ; inopérant en continu car
  « le primaire créerait un champ magnétique constant au cours du temps. Par conséquent, il ne pourrait rien induire
  dans le secondaire. »

### Partie B — Le dipôle RL : manipulations (identiques à 223433 p.57–66)

Définition (p.57) : « On appelle dipôle RL l'association en série d'une bobine d'inductance L, de résistance r et d'un
résistor de résistance R₀, R étant la résistance totale R₀+r du dipôle. »

- **1.1 Établissement, expérience** (p.57–58, Fig.18–20) — E = 6 V, bobine L = 0,1 H, r = 10 Ω, R₀ = 40 Ω, diode D
  (montée en inverse en dérivation sur bobine + R₀), voie Y1 en A, Y2 en B ; chronogrammes (1) u_AM palier, (2) u_BM
  exponentielle. Questions 1°–6° (i, I₀ comparée à E/R, retard, r = 0, rôle de la diode). En permanent la bobine se
  comporte « comme un résistor de résistance égale à sa résistance interne r. Si r = 0, uAB = 0 », d'où u_R₀ = E.
- **1.2 Établissement, théorie** (p.58–60, Fig.21–23 ; image p.59 vue) — u_AB + u_BM = E (1) ; « L di/dt + Ri = E (2),
  avec R = R₀ + r » ; analogie avec « du_C/dt + (1/τ)u_C = E/τ (équation (1) de la page 22) » ; solution proposée
  Ae^(−αt) + B ; i(0) = 0 ⇒ A = −B ; t → ∞ : A = −E/R ; α = 1/τ. u_AB(t) = E e^(−t/τ) + r(E/R)(1 − e^(−t/τ)) ; u_AB(0)
  = E ; limite (r/R)E ; r = 0 : u_AB = E e^(−t/τ) → 0. Questions : brancher pour voir u_AB ; vérifier Fig.23.
- **2.1 Rupture, expérience** (p.61, Fig.24) — régime permanent établi puis K ouvert : u_R₀ décroît exponentiellement ;
  courant transitoire dans le circuit bobine + résistor + diode, « dans le même sens » qu'avant. Sans diode :
  étincelle ; « Exemple : Avec L = 1 H, I = 500 mA, e = −L di/dt ≃ −L Δi/Δt. Δt ≃ 1 ms, ce qui donne e ≃ 500 V ! »
  (renvoi « paragraphe 5 de la première partie … page 54 »).
- **2.2 Rupture, théorie** (p.62, Fig.25–27 ; image vue) — u_AB + u_BM = 0 (1) ; di/dt + (1/τ)i = 0 (2) ; i = A e^(−αt),
  A = I₀ = E/R, α = 1/τ ; i(t) = (E/R)e^(−t/τ). Questions : montrer par deux méthodes u_AB = (r/R − 1)E e^(−t/τ) ;
  vérifier Fig.27 (u_AB part de −R₀E/R vers 0) ; si r = 0, u_AB passe de 0 à (−E).
- **3.1 Influence de R** (p.63, Fig.28a–d ; vue) — L = 0,2 H ; R₁ = 210 Ω, R₂ = 230 Ω, R₃ = 270 Ω, R₄ = 350 Ω ; « 1
  ms/div » et « 1 V/div » ; tableau R (Ω) 210 / 230 / 270 / 350, t (ms) vide, u_R₀ = 4 V ; montrer t inversement
  proportionnelle à R (p.64). Tableau non rempli.
- **3.2 Influence de L** (p.64, Fig.29a–d ; vue) — bobine d'inductance réglable (« Bobine dépourvue de tout noyau de
  fer doux »), R = 210 Ω constante (R₀ ajusté) ; L = 0,10 / 0,13 / 0,15 / 0,20 H ; « 0,5 ms/div » et « 1 V/div » ;
  tableau t (ms) vide ; montrer t proportionnelle à L.
- **3.3 Constante de temps** (p.65–66 ; vues) — voir Encadrés.

### Encadrés (VERBATIM, vérifiés sur l'image de 223432)

> **Loi de Lenz** (p.48) — « Le courant induit a un sens tel qu'il s'oppose par ses effets à la cause qui lui donne
> naissance. »

> **Conclusion** (p.46) — « Toute variation de champ magnétique crée dans un circuit électrique fermé situé à
> proximité du champ, un courant électrique appelé courant induit : c'est le phénomène d'induction
> électromagnétique. Le courant induit est d'autant plus intense que la variation locale des caractéristiques du
> champ inducteur est plus rapide. Le sens du vecteur champ magnétique inducteur est un facteur dont dépend le sens du
> courant induit. »

> **Conclusion** (p.49) — « Une bobine ne se comporte pas comme un conducteur ohmique. Placée dans un circuit fermé,
> elle s'oppose aux variations de l'intensité du courant électrique qui y circule. »

> **Définition** (p.51, vue) — « L'inductance est une grandeur caratérisant l'aptitude d'une bobine à modérer les
> variations de tout courant électrique qui y circule. Dans le système international d'unités, l'inductance s'exprime
> en henry (H). » Note : « Nom dédié au physicien américain Joseph Henry (1797-1878) ». (« caratérisant » : coquille.)

> **Signe** (p.51, vue) — « Dans l'expression (− L di/dt), le signe (−) traduit la loi de Lenz : − Quand i croît,
> L.di/dt > 0. Donc, e < 0 : la f.e.m. d'auto-induction s'oppose à l'augmentation de l'intensité du courant. − Quand i
> décroît, L.di/dt < 0. Donc, e > 0 : la f.e.m. d'auto-induction s'oppose à la diminution de l'intensité du courant. »

> **Conclusion : Expression de la f.e.m. d'auto-induction** (p.51, vue) — « Toute bobine d'inductance L parcourue par
> un courant électrique d'intensité i variable est le siège d'une force électromotrice appelée force électromotrice
> auto-induite (ou d'auto-induction) e = − L di/dt. »

> **Conclusion** (p.52) — « L'inductance d'une bobine ne dépend que de ses caractéristiques géométriques, à savoir le
> nombre total de spires, la longueur et la section moyenne, d'où sa qualification d'inductance propre. »
> **Remarques** (p.52) — « Les bobines usuelles ont une inductance nettement inférieure à 1 H. Exemple : un solénoïde
> de 150 spires, de 15 cm de longueur et de 3 cm de diamètre a une inductance L = 140 μH, — L'introduction d'un
> barreau de fer doux dans un solénoïde fait augmenter la valeur de son inductance L. Mais, dans ces conditions,
> l'expression e = − L di/dt n'est plus valable. — Du fait que la f.e.m. auto-induite est due à l'inductance L de la
> bobine, toute bobine d'inductance L non nulle est qualifiée de bobine inductive. Si en plus, sa résistance est
> nulle, elle est dite purement inductive. »

> **Tension aux bornes d'une bobine** (p.53) — « u_AB = L di/dt + r i » (sens positif de A vers B).

> **Énergie magnétique** (p.55, vue) — « On montre que l'énergie magnétique emmagasinée dans une bobine d'inductance L
> s'écrit : E_L = ½L.i² ». Suite : « Si |i| diminue, p_L = L.di/dt diminue, ce qui signifie que l'énergie magnétique
> diminue : la bobine restitue à l'extérieur un peu de l'énergie qu'elle a emmagasinée avec l'augmentation de |i|,
> elle joue ainsi le rôle de générateur. » [p_L = L.di/dt imprimé sans le facteur i [?].]
> **Conclusion** (p.55) — « Tant qu'elle est parcourue par un courant électrique, la bobine inductive est un
> réservoir d'énergie dite magnétique. »
> **Remarque** (p.55) — « L'énergie magnétique ne peut rester stockée dans une bobine en l'absence de courant. Par
> contre, l'énergie potentielle électrique reste stockée dans le condensateur même hors circuit. Donc, le condensateur
> est un réservoir permanent d'énergie, tandis que la bobine en est un réservoir temporaire. »

> **Conclusion** (p.58) — « La réponse d'un dipôle RL à un échelon de tension E est un courant continu d'intensité I₀
> = E/R. Celui-ci ne s'établit pas instantanément à cause de l'inductance L de la bobine. Autrement dit, la bobine
> s'oppose à l'établissement du courant électrique dans la portion de circuit où elle se trouve insérée. »

> **Équation différentielle** (p.59, vue) — « di/dt + (1/τ) i = E/L (3), avec τ = L/R » ; « Cette équation
> différentielle régit l'évolution dans le temps de l'intensité i du courant circulant dans le dipôle RL soumis à un
> échelon de tension E. » **Solution** (p.59) — « i(t) = (E/R)(1 − e^(−t/τ)), avec τ = L/R ».

> **Conclusion** (p.60) — « La réponse d'un dipôle RL en courant est constituée de deux régimes: un régime
> transitoire au cours duquel l'intensité augmente en exponentielle à partir de la valeur zéro en tendant vers la
> valeur I₀ = E/R et un régime permanent caractérisé par un courant continu d'intensité I₀. »
> **Conclusion** (p.60) — « Quand on soumet un dipôle RL à un échelon de tension E, il apparaît instantanément aux
> bornes de la bobine une tension égale à E mais qui décroît selon un régime transitoire pour s'annuler si la
> résistance de la bobine est nulle. »

> **Conclusion** (p.61) — « Lors de la rupture du courant dans un circuit comportant une bobine, celle-ci a pour effet
> d'assurer la continuité du courant électrique par une annulation progressive de son intensité. »

> **Rupture** (p.62, vue) — « di/dt + (1/τ).i = 0 (2), avec τ = L/R » ; « i(t) = (E/R)e^(−t/τ) » avec « R = R₀ + r et
> τ = L/R ».

> **Constante de temps** (p.65, vue) — « Donc, la durée d'établissement du courant dans le circuit est proportionnelle
> au quotient L/R. De ce fait, le quotient L/R est appelé constante de temps du dipôle RL ; on la note τ. »
> Remarque : « On sait que la résistance R a la dimension du quotient d'une tension par une intensité de courant et que
> L a celle de U.t/I. Donc le quotient L/R a la dimension d'un temps, ce qui justifie encore son appéllation de
> constante de temps. » Encadré : « τ = L/R : constante de temps ».
> **Définition** (p.65) — « La constante de temps τ est une grandeur caractéristique du dipôle RL, elle renseigne sur
> le retard avec lequel s'établit le régime permanent ou la rupture du courant dans le dipôle. τ ayant la dimension
> d'un temps, elle s'exprime en secondes. »

> **Détermination de τ** (p.65–66, vues) — « Les méthodes possibles pour déterminer la constante de temps sont les
> mêmes que celles utilisées dans le cas du dipôle RC. » ▸ *Par calcul direct* : τ = L/R. ▸ *Détermination graphique
> (1ère méthode)* : « Sur la courbe de i(t) représentant l'établissement du régime permanent, on trace la tangente au
> point d'abscisse t = 0 s [p.65 : « t = 0s »]. L'abscisse du point d'intersection de la tangente avec l'asymptote
> I₀ = E/R est τ. (Fig.30) » Justification : « k = di/dt (t = 0) = I₀/τ » ; tangente « i(t) = (I₀/τ) t » ;
> « i(t) = (I₀/τ)t = I₀, d'où t = τ ». Remarque : même méthode pour la rupture : « la tangente à l'origine des temps
> coupe l'axe des abscisses au point d'abscisse τ (Fig.31) ». ▸ *2ème méthode* : « i(τ) = (E/R)(1 − e^(−1)) = 0,63
> E/R », abscisse du point d'ordonnée 0,63 E/R (Fig.32) ; rupture : « i(τ) = (E/R)e^(−1) = 0,37 E/R » (Fig.33).

### L'essentiel (p.67, verbatim, vu sur l'image)

« ■ Une bobine est un dipôle électrocinétique constitué généralement par un enroulement cylindrique dans le même
sens, de fil conducteur recouvert d'une gaine isolante. ■ Toute variation de champ magnétique à proximité d'une bobine
en circuit fermé produit un courant électrique appelé courant induit. ■ Loi de Lenz : Le courant induit a un sens tel
qu'il s'oppose par ses effets à la cause qui lui donne naissance. ■ Tout courant induit est dû à une f.e.m. délocalisée
appelée f.e.m. d'induction. ■ Toute bobine parcourue par un courant variable d'intensité i est le siège d'une f.e.m.
d'auto-induction : e = − L di/dt, où L est l'inductance de la bobine. ■ L'auto-induction traduit l'opposition d'une
bobine à toute variation de courant. ■ Pour une bobine d'inductance L, de résistance interne r, parcourue de sa borne A
à sa borne B par un courant variable d'intensité i, la tension à ses bornes s'écrit: u_AB = L di/dt + ri ■ L'énergie
magnétique emmagasinée dans une bobine parcourue par un courant d'intensité i s'exprime : E_L = ½Li² ■ L'inductance
d'une bobine est une grandeur caractérisant sa faculté d'emmagasiner de l'énergie magnétique. ■ Etant liée à
l'intensité du courant, l'énergie magnétique stockée par une bobine est transférée à l'extérieur du circuit avec la
rupture du courant. ■ Un dipôle RL soumis à un échelon de tension de valeur E est parcouru par un courant continu qui
ne s'établit pas brusquement, mais à la suite d'un régime transitoire, selon la loi : i(t) = (E/R)(1 − e^(−t/τ)) où τ
= L/R est la constante de temps du dipôle RL. ■ Lors de la rupture du courant dans un circuit comportant une bobine,
l'intensité i du courant ne s'annule pas brusquement, mais en diminuant de manière continue selon la loi : i(t) =
(E/R)e^(−t/τ) »

### Exercice résolu (p.68–70 ; identique à 223433 ; p.70 vue)

Énoncé : série E = 6 V, K, bobine (L, r), résistor R₀ = 140 Ω ; oscillogramme Fig.1 : montée exponentielle, 2 ms/div,
1 V/div. 1°) choisir entre schéma 1 (R₀ entre K et la bobine) et 2 (R₀ entre la bobine et M, masse en M), ajouter les
connexions ; 2°) expliquer l'allure ; 3°) a) montrer « du/dt + (1/τ)u = (R₀/L)E, où τ = L/R avec R = R₀ + r » ; b)
solution u = Ae^(−αt) + B : A, B, α ; 4°) τ, r, L graphiquement ; 5°) i(t).
Solution : 1°) schéma 2, B relié à l'entrée Y (oscilloscope = tensions, u = R₀ i, borne à la masse). 2°) i ne croît que
progressivement. 3°a) u_AB + u_BM + u_MA = 0 ⇒ u + ri + L di/dt = E ⇒ « du/dt + (R/L)u = (R₀/L)E » ; b) B = −A ;
« B/τ = (R₀/L)E, d'où B = (R₀/R)E » ; α = 1/τ ; « u = (R₀/R)E(1 − e^(−t/τ)) ». 4°) « U₀ = (R₀/R)E … r = (E/U₀ −
1)R₀ » ; « U₀ = 5,6 V » ; « r = 10 Ω » ; « u(τ) = U₀(1 − 1/e) = 0,632 U₀ = 3,45 V » puis « En portant u = 3.54V » ;
« τ = 2 ms » ; L = τR : « L = 300 mH ». 5°) « i = I₀(1 − e^(−t/τ)) avec I₀ = E/R = 0,04 A ». [Coquilles : p.69
« B/α » pour B/τ ; p.70 « 3,45 V » puis « 3,54V » — 0,632 × 5,6 = 3,54, valeur de l'oscillogramme.]

### Tests rapides (p.71 ; identique à 223433, texte seul — aucune réponse au corrigé)

- **Ex.1 Vrai/faux** (8 items) : bobine dans champ variable ⇒ f.e.m. induite ; toute variation de courant ⇒ f.e.m.
  induite ; noyau de fer doux fait diminuer L ; abaisser une tension continue par transformateur ; τ caractérise la
  durée du transitoire ; augmenter la durée du transitoire en augmentant R ; à l'établissement la tension bobine
  diminue vers une limite ; à l'ouverture i sans discontinuité.
- **Ex.2 QCM** : I bobine inductive (a. s'oppose aux variations de la tension / b. de l'intensité / c. équivaut en
  continu à un résistor r) ; II u_AB pour i de B vers A (a. L.i + r.i ; b. L.di/dt + r.i ; c. −L.di/dt − r.i ; d.
  −(dL/dt).i − r.i) ; III L dépend de (tension / caractéristiques géométriques / intensité) ; IV bobine purement
  inductive, sa tension (augmente sans cesse / tend vers zéro / prend instantanément E / tend vers une constante < E) ;
  V i (augmente vers E/R / diminue vers zéro / prend directement E/R).

### Exercices d'application (p.72–73 ; identiques à 223433 ; p.73 vue) — réponses p.318

- **Ex.3** — 4 schémas (N ou S en regard, approche/éloignement) : sens du courant induit, face en regard.
  Réponse : « a- Nord , b- Sud , c- Sud ; d- Nord. »
- **Ex.4** — approche du pôle nord : champ induit, sens du courant ; pôle sud éloigné : champ inducteur et induit,
  sens. Réponse : « 1°) a) Bp et Ba sont opposés., b) La règle du bonhomme d'Ampère. 2°) a) Bp et Ba ont le même sens,
  b) La règle du bonhomme d'Ampère. »
- **Ex.5** — L = 40 mH ; e(t) créneau : 240 mV sur [0, 5 ms], −400 mV sur [5, 8 ms]. 1°) di/dt = −e/L ; 2°) −6 A.s⁻¹
  puis 10 A.s⁻¹ ; 3°) i(t) décroissante sur [0, 5 ms], croissante sur [5, 8 ms] (i(5 ms) = 0).
- **Ex.6** — L = 470 mH, r = 10 Ω, i = 0,006 t² (A→B). 1°) « u_AB = (12.L.t + 6.r.t²).10⁻³ V » ; 2°) à t = 10 s : «
  u_AB ≃ 6,06 V ».
- **Ex.7** — L = 0,1 H, r négligeable ; i(t) dents de scie 0 → 120 mA en 40 ms, retour à 0 à 50 ms (Fig.2). 1°) [0, 40
  ms] u_AB = 3L ; [40, 50 ms] u_AB = −12.L ; 2°) 0,3 V puis −1,2 V (10 ms/div, 0,5 V/div).
- **Ex.8** — montage Fig.18-type (A→Y1, B→Y2, M masse). Réponses : i tend vers I₀ ; I₀ = E/(r + R₀) ; di/dt + (R/L)i
  = E/L ; A = E/R ; α = R/L ; τ = L/R ; « pour t = 5.τ le régime permanent s'établit ». [6° : symbole de τ manquant à
  l'impression, image p.73 vue.]
- **Ex.9** — U = 12 V, L = 100 mH, R = 120 Ω, r nulle. Réponses : I₀ = E/R = 0,1 A ; τ = L/R = 0,83 ms.

### Exercices de synthèse (p.74–76 ; identiques à 223433) — réponses p.318

- **Ex.10** — E = 6 V, bobine (L, r = 10 Ω), R = 200 Ω ; acquisition u_AB, u_BC. Réponses : courbe 1 : u_BC, courbe 2 :
  u_AB ; I₀ = E/(r + R) = 28,6 mA ; I₀ = u_BC/R ≃ 28,5 mA ; méthode de la tangente ; τ = 2,5.10⁻³ s ; L = τ(r + R) =
  0,53 H (9° sans réponse).
- **Ex.11** — bobine (L, r) + r' = 50 Ω, E = 6 V ; u_r' → ≈ 5 V. Réponses : I₀ = u_r'/r' = 0,1 A ; « r' = 10 ? »
  (lire r = 10 Ω, image p.318 vue) ; τ ≃ 10⁻³ s ; L = (r + r')τ = 60 mH ; W = 0,3 mJ.
- **Ex.12** — rupture, i décroît de 50 mA (0–55 ms) ; R = r + R₀ = 50 Ω. Réponses : I₀ = 50 mA ; tangente : τ = 22 ms ;
  b) « i(t₁/₂) = I₀/2 → τ = 22 ms » (image p.318) ; L = R.τ = 1,1 H ; « e ≃ 3,3 V » [?].
- **Ex.13** — E = 6 V, r = 2 Ω ; bobine L = 1,8 H, R = 8 Ω ; moteur + diode en dérivation ; m = 20 g, h = 18,5 cm, g =
  9,8 N.kg⁻¹. Réponses : I = E/(R + r) = 0,6 A, i de A vers B ; à l'ouverture, diode passante ; W = m.g.h = 36,3.10⁻³
  J ; W_m = ½L.I² = 324.10⁻³ J ; rendement 11,2 %.
- **Ex.14 Étude de texte « La cuisson par induction »** (p.76) — casserole chauffée par courants induits dans sa paroi
  (« noyau » de la bobine source), effet Joule ; 4 questions, sans réponse au corrigé.
- **En savoir plus (p.77)** — « Les pouvoirs de l'induction électromagnétique » : plaque à induction, courants de
  Foucault, ralentisseurs électromagnétiques des poids lourds ; lecture seule.

### Écart avec Sciences expérimentales (223433)

- **Contenu : aucun.** Aucune notion, activité, manipulation, valeur numérique, exercice, énoncé ou réponse n'est ajouté
  ou retiré. Même chapitre, mêmes pages (42–77), mêmes figures 1 à 33, mêmes exercices 1 à 14, même exercice résolu,
  même page d'ouverture, mêmes encadrés. Toutes les valeurs (E = 6 V, L = 0,1 H, r = 10 Ω, R₀ = 40 Ω ; 210/230/270/350
  Ω ; 0,10/0,13/0,15/0,20 H ; 240 mA ; 10 mH ; 5 μF ; 140 μH ; 500 V ; exercice résolu 5,6 V/10 Ω/2 ms/300 mH/0,04 A…)
  sont identiques à celles de 223433.
- **Écarts de forme seulement (4 pages, rendu pixel différent, texte inchangé)** : p.63 (« horizontalement : 1
  ms/div » espacé différemment) ; p.64 (« 0,5 ms/div » et « 1 V/div » : espaces) ; p.65 (« t = 0s » sans espace dans
  223432, « t = 0 s » dans 223433 ; fractions L/R recomposées) ; p.67 (L'essentiel : fractions i(t) = E/R(…) recomposées,
  même contenu). Couche texte : glyphes de formules différents sur p.42, 50, 59–62, 65, 67–70 (mêmes équations à
  l'image, pixel-identiques).
- **Numéro de la page des réponses** : p.318 (« Chapitre 2 », colonne de gauche) au lieu de p.316 ; réponses
  identiques, y compris la coquille « r' = 10 ? » et « e ≃ 3,3 V ». Le manuel 223432 compte 320 pages (223433 : 318).
- **Retire / ajoute** : rien. Le chapitre est le même pour les sections Mathématiques et Sciences expérimentales.

### Bornes de scope (section Mathématiques)

✅ **Inclus** (identique à la section Sciences expérimentales)
- Induction électromagnétique **qualitative** : courant induit par déplacement relatif aimant-bobine ou par courant
  variable voisin ; inducteur / induit, champ inducteur / induit ; rôle de la rapidité de variation et du sens du champ.
- **Loi de Lenz** : sens du courant induit, face présentée à l'aimant, répulsion à l'approche / attraction à
  l'éloignement, b⃗ opposé ou de même sens que B⃗ ; bonhomme d'Ampère (corrigé ex.4) ; signe de u_R sur oscillogramme.
- f.e.m. d'induction délocalisée ; **auto-induction** ; **e = − L di/dt** ; signe selon i croît/décroît ; inductance L
  (henry), dépend de N, ℓ, section (qualitatif) ; fer doux augmente L ; bobine inductive / purement inductive ;
  ordres de grandeur (≪ 1 H, 140 μH).
- Symbole et modèle d'une bobine ; **u_AB = L di/dt + r i** ; calcul de u_AB à partir d'un i(t) donné ; di/dt à partir
  de e(t) en créneaux ; tracé par morceaux.
- Puissance p = ri² + d/dt(½Li²) ; **E_L = ½ L i²** ; bobine = réservoir temporaire ; rôle de la diode ; étincelle de
  rupture, e ≈ L Δi/Δt.
- Alternateur et transformateur, qualitatif (transformateur : alternatif seulement).
- Dipôle RL : échelon de tension, régimes transitoire/permanent, I₀ = E/R, bobine ≡ r en permanent ; **di/dt +
  (1/τ)i = E/L** ; résolution par la forme Ae^(−αt) + B ; **i(t) = (E/R)(1 − e^(−t/τ))** ; u_bobine(t) ; équation en
  u_R₀ (exercice résolu).
- **Rupture** : di/dt + (1/τ)i = 0 ; **i(t) = (E/R)e^(−t/τ)** ; u_AB = (r/R − 1)E e^(−t/τ) ; continuité de i.
- **τ = L/R** : influence de R (t ∝ 1/R), de L (t ∝ L) ; homogénéité ; calcul direct, tangente à l'origine
  (établissement et rupture), 0,63 E/R et 0,37 E/R ; régime permanent à t = 5τ (corrigé ex.8).
- Exploitation d'oscillogrammes : u_AM, u_BM, u_bobine ; U₀, I₀, τ, r, L, énergie ; branchement (masse, voie, INV,
  masse flottante).

⛔ **Exclu** (absent du chapitre dans ce manuel aussi)
- Flux magnétique Φ, loi de Faraday e = −dΦ/dt, formule L = μ₀N²S/ℓ (aucune formule de L en N, ℓ, S) ; pas de μ₀.
- Force de Laplace, rails de Laplace, f.e.m. de mouvement.
- Calcul quantitatif sur alternateurs / transformateurs (rapport de transformation) ; courants de Foucault seulement en
  lecture (p.77).
- Inductances en série/parallèle, mutuelle inductance, bobine à noyau (e = −L di/dt « n'est plus valable »).
- Régime sinusoïdal forcé, impédance, oscillations RLC (chap.3–4) ; dipôle RC hors rappels (chap.1).
- Résolution générale d'équations différentielles ; t½ = τ ln 2 (non enseigné ; utilisé implicitement par le corrigé ex.12 2°b) ; énergie Joule du transitoire par intégrale.
- Aucun contenu spécifique à la section Mathématiques (pas de développement supplémentaire sur L, pas de calcul
  d'intégrale) n'est présent dans ce chapitre.

### Lecture

- **Couche texte** : p.42–77 lues par comparaison mot à mot avec 223433 (mêmes pages ; p.66 et p.73 sans texte) ;
  p.318 (réponses) lue en texte et sur l'image.
- **Comparaison pixel** : p.42–77 de 223432 et de 223433 rendues à 80 dpi et différenciées : 32 pages à écart nul ; 4
  pages (63, 64, 65, 67) à écart typographique.
- **Pages vues sur l'image de 223432 (14)** : p.42, 47, 51, 55, 59, 62, 63, 64, 65, 66, 67, 70, 73, 318 (+ p.63 de
  223433 pour comparaison, non comptée). Les 22 autres pages (p.43–46, 48–50, 52–54, 56–58, 60–61, 68–69, 71–72,
  74–77) ne sont pas revues individuellement sur l'image ici : elles sont pixel-identiques à celles de 223433 déjà
  vues et validées R-7 (p.43–76 vues, p.77 texte).
- **Sondage** : 14 pages vues sur 36 (> 1 sur 10), toutes parmi les plus denses (formules p.51, 55, 59, 62, 66, 70 ;
  tableaux p.47, 51 ; figures p.63–64, 66 ; encadrés p.65, 67 ; exercices p.73 ; réponses p.318). Écarts constatés
  texte → image : fractions, exposants et indices perdus par la couche texte (p.50–51, 59–62, 65–66, 69–70) ; p.66 et
  p.73 sans texte ; signes des impulsions Fig.4/7 et courbes Fig.12, 19, 23, 27 et graphes des ex.5, 7, 10–12 lisibles
  seulement sur l'image (non revues ici : reprises de 223433 par identité pixel).
- **Doutes [?]** (tous hérités à l'identique de 223433) : (1) p.54–55 u_AM / u_AB pour la tension du condensateur ;
  (2) p.55 « p_L = L.di/dt » sans i ; (3) p.47 « champ inducteur b⃗ » en minuscule ; (4) p.69–70 « B/α » et « 3,45 V /
  3,54V » ; (5) réponse ex.12 « e ≃ 3,3 V » (R·I₀ = 2,5 V attendu) ; (6) réponse ex.11 «
  r' = 10 ? » ; (7) ex.8 6° symbole de τ absent ; (8) p.61 renvoi « page 54 » (le §5 commence p.53) ; (9) tableaux
  p.63–64 non remplis ; (10) ex.1, 2, 10 9°) et 14 sans réponse au corrigé.

## 2.3 Chapitre 3 — Oscillations électriques libres (manuel 223432, p.78–109)

**Constat central** : les 32 pages du chapitre sont **identiques, page pour page, à celles du manuel Sciences expérimentales 223433** (mêmes numéros de page 78–109, mêmes textes, mêmes figures, mêmes valeurs numériques, mêmes exercices 1 à 12 dans le même ordre). Seul le **bandeau** de couverture/collection diffère (« Mathématiques »). Les **réponses aux exercices** sont au même contenu, mais **p.318** (colonne « Chapitre 3 ») et non p.316 comme dans 223433. Ce qui suit est donc compact : « identique à 223433 p.X » vaut transcription de la section de référence (`bac-sciences-exp/physique.md`, § 2.3, lignes 1103-1515), relue ici contre l'image de chaque page.

**Partie** : « Evolution de systèmes » (bandeau). Deux parties titrées : « OSCILLATIONS ÉLECTRIQUES LIBRES AMORTIES » (p.80–87), « LES OSCILLATIONS ÉLECTRIQUES LIBRES NON AMORTIES » (p.88–94) ; « L'essentiel » (p.95) ; « Exercices » : résolu p.96–99, à résoudre p.100–106 ; « Fiche technique » p.107–109.

**Page d'ouverture (p.79)** — identique à 223433 p.79 : montre à quartz, légende « Le quartz impose sa fréquence propre aux oscillations ; une montre électronique y gagne en précision. » ; questions d'accroche : « Que désigne-t-on par les expressions “oscillations électriques”, “oscillateur électrique”, “circuit oscillant”...? » ; « Est-ce que le courant alternatif est un phénomène oscillatoire ? »

### Objectifs (p.78) — identique à 223433 p.78 (verbatim, vérifié sur l'image)
Réaliser un montage permettant de suivre les oscillations libres d'un circuit RLC série. · Reconnaître le régime pseudopériodique et le régime apèriodique. · Reconnaître le facteur responsable de l'amortissement. · Reconnaître les grandeurs oscillantes d'un circuit RLC série. · Etablir l'équation différentielle des oscillations libres d'un circuit RLC série. · Interpréter la diminution de l'amplitude des oscillations libres d'un circuit RLC série par le transfert d'énergie de l'oscillateur vers le milieu extérieur. · Ecrire l'expression d'une grandeur oscillante en régime libre non amorti. · Définir la pulsation propre ω₀ et la période propre T₀ d'un oscillateur RLC non amorti. · Exprimer T₀ en fonction de L et de C. · Déterminer la période, l'amplitude et la phase initiale d'une grandeur oscillante sinusoïdale d'un circuit RLC série non amorti. · Démontrer la conservation de l'énergie totale d'un oscillateur LC. · Interpréter le cas particuler des oscillations libres non amorties.

### Prérequis (p.78) — identique à 223433 p.78
SAVOIR : Définir un phénomène périodique. · Définir la période T et la fréquence N d'un phénomène périodique. · Ecrire la relation N = 1/T. · Ecrire la relation i = dq/dt. · Ecrire l'expression de la tension : aux bornes d'un condensateur u = q/c ; aux bornes d'une bobine u = ri + L di/dt. · Exprimer l'énergie potentielle électrique E_C emmagasinée par un condensateur. · Exprimer l'énergie magnétique E_L emmagasinée par une bobine. — SAVOIR FAIRE : Reconnaître un phénomène périodique. · Distinguer entre période et fréquence d'un phénomène périodique. · Utiliser la relation i = dq/dt. · Expliquer la charge et la décharge d'un condensateur. · Expliquer le phènomène d'auto-indution. · Distinguer entre transfert et transformation d'énergie. · Appliquer la loi des mailles.

### Plan (titres numérotés du manuel) — identique à 223433
- *Oscillations électriques libres amorties* (p.80) — intro : « Que se passera-t-il si l'on décharge le condensateur dans une bobine sachant que celle-ci emmagasine aussi de l'énergie? » 1. Production d'oscillations libres amorties (p.80) · 2. Influence de l'amortissement (p.83) · 3. Équation différentielle régissant l'évolution d'un circuit RLC série en régime libre (p.85) · 4. Énergie totale d'un oscillateur RLC série (p.85).
- *Les oscillations électriques libres non amorties* (p.88) — intro : « … l'oscillateur LC non amorti est un cas idéal parce qu'il est impossible de le réaliser dans la pratique » ; étude « uniquement, par une étude théorique ». 1. Nature des oscillations libres non amorties (p.88) : 1.1 Évolution de la charge du condensateur (+ Simulation des oscillations, p.89) ; 1.2 Période et fréquence des oscillations (p.90) ; 1.3 Amplitude et phase initiale (p.90) · 2. Énergie totale d'un oscillateur LC (p.92) : 2.1 Conservation de l'énergie totale ; 2.2 Évolution des énergies électrique et magnétique (p.93).

### Cours — manipulations, questions, interprétations

**A.1 Production d'oscillations libres amorties (p.80–83) — identique à 223433 p.80–83.**
- Manipulation (p.80, Fig.1) : générateur idéal E = 5 V ; C = 0,5 μF ; résistor R₀ réglable fixé à **R₀ = 100 Ω** ; bobine L = 1 H, r = 12,5 Ω ; commutateur K (position 1 = charge, 2 = décharge dans la bobine en série avec R₀) ; voie Y₁ : u_C = u_NM, voie Y₂ : u_R₀ = u_AM ; oscilloscope à mémoire ; Fig.2 : oscillogrammes ① et ② (sinusoïdes amorties décalées).
- Questions 1°–7° (p.80–81) : chronogramme en position 1 ; ① = u_C ⇒ q(t) ; ② ⇒ i(t) dans MNKA ; sens de « oscillations de q et de i » et pourquoi « amorties » ; comparer les intervalles T entre extrêmums de u_C et u_R₀ ; comparer les maximums (amortissement) et pourquoi « pseudopériodiques » ; interpréter q(t), i(t).
- Interprétation (p.81–82, Fig.3, 4a–4d, 5) : à t₀ = 0 u_C0 = E, Q₀ = CE ; courant de B vers A, sens négatif ; |i| ne passe pas instantanément de 0 à I_m « à cause de la f.e.m. auto-induite » ; à t₁ = T/4 condensateur déchargé mais i ne s'annule pas (e = − L di/dt) ⇒ charge +q < 0 sur A ; à t₂ = T/2 charges +Q₁ < 0, −Q₁ > 0, courant régénéré dans le sens positif ; à T : +Q₂ ; 3T/2 : Q₃ < 0 ; 2T : Q₄ > 0 ; Q₀ > |Q₁| > Q₂ > |Q₃| : « la résistance totale R du circuit (R₀ + r) s'oppose incessamment à la circulation du courant » ; « De telles oscillations sont dites amorties. De plus, ces oscillations sont dites libres du fait qu'elles se produisent dans le circuit RLC série bien que celui-ci ne soit fermé sur aucun générateur. » ; extrêmums à intervalles égaux, amplitude décroissante ⇒ « pseudopériodiques ». « On dit qu'un tel courant alternatif est un phénomène oscillatoire. »

**A.2 Influence de l'amortissement (p.83–85) — identique à 223433 p.83–85.**
- Manipulation (Fig.6a–6f) : R₀ = 100 Ω, 500 Ω, 1000 Ω (oscillations de moins en moins nombreuses), 3 kΩ, 4 kΩ, 5 kΩ (plus d'oscillation, retour de plus en plus lent). Questions 1°–3° : influence de R sur amortissement et pseudopériode ; conditions pour que le RLC oscille librement ; comparer 6.d, 6.e, 6.f (durée du retour à l'état d'équilibre).
- Analyse (p.84) : R₀ augmente ⇒ oscillations de plus en plus amorties (« le nombre total des oscillations diminue »), pseudopériode T « augmente légèrement » (6a–6c) ; R₀ élevée : « simple décharge du condensateur ; celle-ci demande une durée aussi longue que la résistance R₀ est plus grande : un tel régime non oscillatoire est dit apériodique » (6d–6f).
- Remarques (p.84) : 1- régime apériodique de la plus petite valeur élevée de R = « régime critique », « expérimentalement, il est difficile de le mettre en évidence » ; 2- à la limite d'un amortissement nul (absence du résistor, bobine de très petite r) « le régime pseudopériodique devient périodique (Fig.7) » ; l'étude fait l'objet de la 2ᵉ partie.

**A.3 Équation différentielle (p.85)** — identique à 223433 p.85 (Fig.8 ; loi des mailles ; voir Encadrés).

**A.4 Énergie totale d'un oscillateur RLC série (p.85–87) — identique à 223433 p.85–87.** Manipulation : interface d'acquisition (« console VTT par exemple »), R₀ = 100 Ω (Fig.9, u_C de 5 V, t 0–12 ms) puis R₀ = 500 Ω (Fig.10) ; tableur : E_C = ½C·u_C², E_L = ½(L/R₀²)·u_R₀², E = E_C + E_L ; Fig.11a/11b (axe « En(μJ) » 0 à 0,6). Questions 1°–4° (p.86) : zéros/maxima de E_C, E_L à intervalles T/2 ; E = E_C + E_L ; transformations mutuelles ; influence [de la résistance] sur la vitesse de diminution de E. Interprétation (p.86–87) : dE/dt = −Ri² ; énergie transformée en énergie thermique par effet Joule, dissipation d'autant plus rapide que R est grande, « système non conservatif » ; entre nT et nT + T/4 E_C → E_L, entre nT + T/4 et nT + T/2 E_L → E_C ; transformations « pas intégrales » (à chaque transfert une partie est transférée par chaleur au milieu extérieur).

**B.1.1 Évolution de la charge (p.88–89) — identique à 223433 p.88–89.** Fig.12 : C chargé fermé sur une bobine « supposée purement inductive ». Simulation (Fig.13) : L = 10 mH, C = 100 μF, Q_m = 6.10⁻⁴ C ; champs de l'écran « U = 6 V, C = 100 μF, L = 10 mH, Q₀ = 0,6 mC » ; échelles 1 V/div, 1 ms/div (vu sur l'image).
**B.1.2 Période et fréquence (p.90)** — identique à 223433 p.90. Questions : 1°) avec la Fig.13, T₀ puis N₀ ; 2°) vérifier T₀ = 2π√(LC). Remarque : T₀ = 6,28 ms, « très inférieure à la seconde ».
**B.1.3 Amplitude et phase initiale (p.90–92)** — identique à 223433 p.90–92. 2ᵉ simulation Q′_m = 9.10⁻⁴ C (Fig.14 : « U = 9 V, C = 100 μF, L = 10 mH, Q′₀ = 0,9 mC ») ; q(0) = Q₀ ⇒ sinφ = 1 ⇒ φ = π/2 rad. Questions p.92 : 1°) montrer i(t) = ω₀Q_m cos(ω₀t + π/2) ; 2°) i(t) = I_m sin(ω₀t + φ), préciser I_m et φ.
**B.2.1 Conservation de l'énergie (p.92–93)** — identique à 223433 p.92–93. Questions : 1°) comparer E à l'énergie transférée initialement, prévisible ? ; 2°) E = ½L·I_m² sachant I_m = ω₀Q_m et LCω₀² = 1 ; 3°) montrer par dE/dt que E est constante, cas particulier de dE/dt = −Ri².
**B.2.2 Évolution des énergies (p.93–94)** — identique à 223433 p.93–94. Fig.15 (q et i, graduations T₀/4, T₀/2, 3T₀/4, T₀) ; à t = 0 E = E_Cmax = Q_m²/2C ; à T₀/4 E = E_Lmax = ½LI_m² ; « la bobine joue le rôle de générateur en chargeant progressivement le condensateur » ; « transformation mutuelle … mais sans aucune perte ». Fig.16 : C = 0,47 μF, L = 0,1 H, U₀ = 5 V, E₀ en palier à 5,875 μJ, graduations 0,34 ; 0,68 ; 1,02 ; 1,36 ms (vu sur l'image). Questions p.94 : 1°) interpréter les oscillations non amorties (R nulle) ; 2°) a) E_C, E_L périodiques, b) périodes comparées entre elles et à T₀, c) E relevée vs E₀ ; 3°) E_C = (Q_m²/4C)(1 + cos 2ω₀t), E_L = ¼LI_m²(1 − cos 2ω₀t) avec q = Q_m cos ω₀t, E constante.

### Encadrés, lois, relations (VERBATIM, relus sur l'image de leur page ; strictement identiques à 223433)

> **Conclusion** (p.83) — « Un circuit constitué d'un dipôle RL série fermé sur un condensateur initialement chargé peut être le siège d'oscillations électriques amorties. De telles oscillations qui s'effectuent d'elles mêmes sans intervention de l'extérieur sont dites libres. Les oscillations libres amorties sont des oscillations pseudopériodiques de pseudopériode T. »

> **Conclusion** (p.85) — « Un circuit RLC série fermé, avec le condensateur initialement chargé, ne peut osciller librement que lorsque l'amortissement est faible. Plus la résistance du circuit est grande, plus la pseudopériode est grande et plus le retour de l'oscillateur à son état d'équilibre est rapide. Avec des valeurs élevées de R, le régime n'est plus oscillatoire, il est apériodique » [?] (contredit l'analyse p.84 : voir Doutes).

> **Équation différentielle RLC série** (p.85) — « u_C + u_b + u_R₀ = 0, ce qui signifie q/C + (ri + L di/dt) + R₀i = 0. D'où : L di/dt + (r + R₀)i + q/C = 0. (1) Or, i = dq/dt. Donc, (1) s'écrit : L d²q/dt² + (r + R₀) dq/dt + q/C = 0 ou bien d²q/dt² + ((r + R₀)/L) dq/dt + (1/LC) q = 0 »

> **Énergies** (p.86) — « E_C = ½ C.u_C² » ; « E_L = ½ (L/R₀²).u_R₀² » ; « E = E_C + E_L ».

> **Non-conservation** (p.86) — « dE/dt = d/dt(q²/2C + (L/2)i²) = (q/C)(dq/dt) + Li di/dt = i(L di/dt + q/C). Or l'équation différentielle peut s'écrire : L di/dt + q/C + Ri = 0, ce qui donne L di/dt + q/C = − Ri, d'où **dE/dt = − Ri²** » (encadré). Encadré latéral : « La vitesse de variation de l'énergie totale d'un système dE/dt n'est autre que la puissance instantanée p du même système : p = dE/dt ».

> **Oscillateur LC** (p.88) — « u_C + u_L = 0, ce qui signifie q/C + L di/dt = 0. Or i = dq/dt, d'où d²q/dt² + ω₀²q = 0 avec ω₀² = 1/LC : constante positive ». « On admet que la solution générale d'une telle équation différentielle est de la forme : q(t)=Q_m sin(ω₀t + φ). ω₀ : pulsation des oscillations de la charge q, exprimée en radians par seconde (rad.s⁻¹). Q_m : amplitude des oscillations de la charge q, exprimée en coulombs (C). φ : phase initiale de la charge q, exprimée en radians (rad). φ(t) = ωt + φ : phase à l'instant t, exprimée en radians (rad) » (indice o absent de « ωt » dans l'imprimé). Vérification (p.88–89) : d²q/dt² = − ω₀²q ⇒ « − ω₀²q + (1/LC)q = 0 », « q(1/LC − ω₀²) = 0 quel que soit q », « ω₀ = 1/√LC ».

> **Conclusion** (p.89) — « La charge q du condensateur d'un circuit LC (circuit RLC série non amorti) oscille sinusoïdalement au cours du temps avec la pulsation ω₀ = 1/√LC. Ne dépendant que des grandeurs L et C caractéristiques du circuit, la pulsation des oscillations libres non amorties est qualifiée de pulsation propre de l'oscillateur. »

> **Période et fréquence propres** (p.90) — « La pulsation ω₀ étant propre à l'oscillateur, la période des oscillations T₀ = 2π/ω₀ est appelée période propre. » Encadré : **T₀ = 2π√LC**. « De même, la fréquence des oscillations N₀ = 1/T₀ est appelée fréquence propre des oscillations. » Encadré : **N₀ = 1/(2π√LC)**.

> **Conclusion** (p.91) — « L'amplitude et la phase initiale des oscillations libres d'un circuit RLC série non amorti ne dépendent que des conditions initiales. Toutefois, la valeur de l'amplitude est tributaire de la valeur de la charge initiale du condensateur, tandis que la valeur de la phase initiale est fonction du choix arbitraire de l'origine des temps. »

> **Conservation** (p.92) — « E = E_C + E_L = (1/2C)q² + ½Li². Avec q = Q_m sin(ω₀t + π/2), i = dq/dt = Q_mω₀ cos(ω₀t + π/2). Donc, E = (1/2C)(Q_m cosω₀t)² + ½L(− Q_mω₀ sin ω₀t)². E = (Q_m²/2C)cos²(ω₀t) + ½Lω₀²Q_m² sin²(ω₀t). Or, ω₀² = 1/LC, il vient : E = (Q_m²/2C)[(cos²(ω₀t) + sin²(ω₀t)] On sait que (cos²ω₀t + sin²ω₀t = 1) quel que soit t. Donc, E = (1/2C)Q_m². Q_m et C étant des constantes, E reste constante au cours du temps : on dit que l'énergie totale de l'oscillateur LC se conserve. »

> **Conclusion** (p.93) — « L'oscillateur RLC série en régime libre non amorti est un système conservatif. Son énergie est proportionnelle au carré de l'amplitude de la grandeur oscillante q(t) ou i(t). » Encadré : **E = Q_m²/2C = ½ L.I_m² = ½ C U_Cm²**.

> **Conclusion** (p.94) — « Les oscillations libres d'un circuit RLC série non amorti sont dues aux transformations mutuelles et intégrales de ses énergies électrostatique et magnétique : l'énergie totale du système est transférée continuellement de manière intégrale du condensateur à la bobine et inversement. »

### L'essentiel (p.95, verbatim, identique à 223433 p.95)
- « L'évolution de la charge du condensateur d'un circuit RLC série est régie en régime libre par l'équation différentielle : **d²q/dt² + (R/L) dq/dt + (1/LC) q = 0** »
- « Un circuit RLC série auquel on a transféré initialement de l'énergie peut être le siège d'oscillations électriques libres amorties, c'est le régime pseudo-périodique. »
- « Les oscillations libres d'un circuit RLC série sont d'autant plus amorties et leur pseudopériode est d'autant plus grande que la résistance R du circuit est plus grande. Pour des valeurs suffisamment élevées de la résistance R, c'est le régime apériodique. »
- « Si la résistance d'un circuit RLC série est nulle, les oscillations libres ne sont plus amorties, elles sont sinusoïdales, c'est le régime périodique. »
- « La période propre d'un oscillateur RLC série s'exprime : **T₀ = 2π√LC** »
- « La pseudo-période des oscillations libres amorties d'un circuit RLC série est légèrement supérieure à T₀. »
- « Les oscillations libres d'un circuit RLC série sont dues aux transformations mutuelles de ses énergies électrostatique et magnétique. »
- « En régime libre, l'énergie totale d'un circuit RLC série ne se conserve que si sa résistance électrique est nulle. »

### Exercice résolu (p.96–99) — identique à 223433 p.96–99
Énoncé : E = 5 V (idéal), C = 1 μF, bobine L = 10 mH et r, R = 90 Ω, oscilloscope à mémoire, interrupteur (Fig.1 : E, R, K en série, puis C ∥ bobine entre A et B ; Y₁ en A). 1°) r = 0 : a) K fermé : tension nulle aux bornes de la bobine, charge du condensateur, I₀ ; b) à l'ouverture de K (t = 0) : description qualitative, équation différentielle en u, avec u = U_m sin(ω₀t + φ) et ω₀ = 1/√LC calculée : U_m et φ, q(t) et i(t) ; c) origine et valeur de l'énergie. 2°) Fig.2 (oscillogramme u_AB, 1 V/div, 0,2 ms/div, palier avant 0 puis oscillations amorties, t₁ et t₂ à deux maxima successifs) : a) montrer par deux méthodes que r ≠ 0 ; b) r ; c) pseudo-période T vs T₀ ; d) variation algébrique de l'énergie entre t₁ et t₂.
Solution : 1°a) u₁ = ri + L di/dt, régime permanent ⇒ u₁ = r·i = 0 V ; u_AB = − q/C = 0 ⇒ « la charge q est nulle » ; condensateur = interrupteur ouvert ; loi de Pouillet **I₀ = E/R** ; **I₀ = 55,5 mA**. 1°b) loi de Lenz : le courant continue dans le même sens ; « le circuit RLC série est le siège d'oscillations libres non amorties » ; u_C + u_L = 0 ; u − L di/dt = 0 ; i = dq/dt, q = − C·u ⇒ i = − C du/dt ⇒ **d²u/dt² + (1/LC)u = 0** ; **ω₀ = 1/√LC = 10⁴ rad.s⁻¹** ; u(0) = U_m sinφ = 0 ⇒ φ = 0 ou π ; i(0) = − CU_mω₀cosφ = I₀ > 0 ⇒ cosφ < 0 ⇒ **φ = π rad** ; **U_m = I₀/(Cω₀) ≃ 5,55 V** ; **u(t) = 5,55 sin(10⁴t + π)** ; **q = 5,55.10⁻⁶ sin(10⁴t)** ; i = CU_mω₀ sin(ω₀t + φ − π/2), I_m = I₀ = 55,5 mA, **i = 55,5 sin(10⁴t + π/2)** en mA. 1°c) E conservée = énergie magnétique initiale **E = ½L.I₀²** = **1,54.10⁻⁵ J**. 2°a) méthode 1 : diminution de l'amplitude due à r ; méthode 2 : pour t < 0 u = 0,5 V = u_AB ≠ 0 ⇒ r = u_AB/I′₀ non nulle. 2°b) I′₀ = E/(R + r) ⇒ **r = u.R/(E − u)** = **10 Ω**. 2°c) T = t₂ − t₁ ≈ 3,25 div × 0,2 ms = **0,65 ms** ; T₀ = 2π/ω₀ = **0,628 ms** ⇒ « T est légèrement supérieure à T₀ ». 2°d) U_m1 = 5 V, U_m2 = 4,5 V ; **E₂ − E₁ = ½C(U_m2² − U_m1²) = − 2,375.10⁻⁶ J**.

### Exercices à résoudre (p.100–106) — énoncés identiques à 223433 ; réponses p.318 (colonne « Chapitre 3 »), identiques à celles de 223433 p.316
**Tests rapides** — **1 Vrai/Faux** (p.100) : 1- décharge dans une bobine identique à celle dans un résistor ; 2- pseudo-période légèrement inférieure à T₀ ; 3- RLC transfère son énergie d'autant plus vite que R est grande ; 4- pseudo-périodique : nombre d'oscillations augmente quand la pseudo-période augmente ; 5- oscillations libres d'un RLC amorti dues à des transformations intégrales. **2 QCM** (p.100) : I- amortissement dû à a capacité, b inductance, c résistance du résistor, d résistance de la bobine, e résistance totale ; II- décharge dans une bobine purement inductive : a périodiques, b sinusoïdales amorties, c pseudo-périodiques non amorties, d incessantes ; III- T₀ : a 2π√(L/C), b 2π√(1/LC), c 2π√LC ; IV- un RLC ne peut entrer en oscillations libres : a sans transfert initial d'énergie, b sans transfert sans cesse d'énergie, c sans qu'il transfère lui-même de l'énergie à l'extérieur, d sans transformations mutuelles. (Pas de corrigé pour 1, 2.)
**Application** —
- **3** (p.100–101) : bobine (r, L), C = 15 μF, pile E = 4,5 V, R = 1 kΩ, acquisition de u_C (Fig.2 : 1 V, 20 ms) ; 1°) phénomène ; 2°) énergie à t = 0 et après deux oscillations, transformations sur une pseudopériode ; 3°) équation en u_C si r nulle ; 4°) ω₀, T₀, T ≈ T₀ ⇒ L. Rép. : 1°) oscillations libres amorties ; 2°) E = 1,52.10⁻⁴ J ; 4°) L = 2,67 H.
- **4** (p.101) : L = 1 H, R, C = 1 μF ; graphes u_C et E_C (échelle « 1ms », ordonnées non graduées) ; 1°) R non nulle ; 2°) T ; 3°) vs T₀ ; 4°) T_E ; 5°) comparer. Rép. : 1°) l'amplitude décroît ; 2°) T = 6,5 ms ; 3°) T₀ = 6,28 ms ; 4°) T_E = 3,3 ms ; 5°) T = 2T_E.
- **5** (p.101) : C = 0,47 μF chargé sous 5 V, L = 44 mH, résistance nulle ; 1°a) équation en u_C, T₀ ; b) u_C(t) ; c) q(t) ; 2°) C′ = 4C, L′ = L/2 : T′₀ en fonction de T₀. Pas de corrigé.
- **6** (p.102) : d²q/dt² + (1/LC)q = 0 (1), Q₀ = 4.10⁻⁴ C ; 1°) énergie totale ; 2°) retrouver (1) par conservation de l'énergie ; 3°) vérifier q = Q_m sin(ω₀t + φ) ; 4°) T₀ ; 5°) constantes de q(t) ; C = 30 μF, L = 0,1 H. Pas de corrigé.
- **7** (p.102) : C = 1,16 μF, L = 0,35 H, r ; T = 4,4 ms ; graphe u(V) (−2 à 2), maxima 1 à 7 ; 1°) T vs T₀ ; 2°) énergie électrique en t₁ et t₇ ; 3°a) énergie magnétique et totale aux mêmes instants ; b) conclure. Rép. : 1°) T₀ = 4,0 ms, T = 4,4 ms, T > T₀ ; 2°) E₁ = 1,485 μJ, E₇ = 0,145 μJ ; 3°b) l'énergie totale diminue.
**Synthèse** —
- **8** (p.102–103) : E = 6 V, C = 20 μF, L = 0,8 H (r nulle), deux R = 20 Ω, K₁, K₂. A- K₁ fermé : 1°) phénomène (voie 1) ; 2°) schéma, sens du courant, signes des charges, flèche u₁ ; 3°) Fig.2 (u₁ de 0 à 6 V, t en ms, graduations 1 à 4) : τ graphique, C avec R = 20 Ω ; 4°) τ du₁/dt + u₁ = E : a- retrouver, b- u₁ = E[1 − exp(−t/τ)], u₁(5τ), conclure. B- K₁ ouvert, K₂ fermé : Fig.3 (5 ms/div ; 1 V/div pour u₁ ; 0,2 mV/div pour u₂) : 1°) attribuer les courbes ; 2°) équation de u₂(t) ; 3°) T vs T₀ ; 4°) Fig.4 et 5 : L augmentée ou R augmentée. Pas de corrigé. [Mobilise le dipôle RC du chapitre 1.]
- **9** (p.103–104) : C = 10 μF chargé sous U₀ = 3 V ; 1°) charge et énergie ; 2°) relié à t = 0 à L = 0,1 H, résistance nulle : a) schéma, allure à l'oscilloscope ; b) interprétation énergétique ; c) équation en u_C ; d) relation T₀, C, L pour u_C = U_m sin(ω₀t + φ) ; e) U_m, φ ; f) instants de |i| maximale ; 3°) r non nulle, oscillogramme 10 ms/div : a- T vs T₀ ; b- pourquoi un oscilloscope à mémoire ; c- énergie thermique dissipée entre t₀ = 0 et t₁ = T. Rép. : 1°) Q₀ = 3.10⁻⁵ C ; 2°b) « Voir cours page 2° » ; d) U_m = 3 V, φ = π/2 rad ; 2°f) t_k = 0,75 T₀ + kT₀ ; 3°a) T > T₀ ; 3°c) W_J = 32,2 μJ.
- **10** (p.104) : vérifier L = 0,2 H ; C = 0,5 μF chargé sous E = 6 V, décharge dans la bobine ; graphe u(V) de 6 V, t de 0 à 50 ms ; 1°) pourquoi pseudopériodique ; 2°a) équation en u ; b) forme d²u/dt² + (1/τ) du/dt + ω₀²u = 0 : expliciter τ, dimension, signification, τ approché ⇒ L (R = 20 Ω) ; c) écart relatif (L_exp − L)/L. Rép. : 1°) l'amplitude diminue ; 2°b) L = 0,255 H ; 25 %.
- **11** (p.104–105) : E = 6 V, C = 50 μF, R = 30 kΩ (charge), R₀ = 5 Ω, bobine L ; 1°) charge (Fig.2 : courbes (1) croissante, (2) décroissante, u de 0 à ~6 V, t de 0 à 4 s) : a) courbe de u_C ; b) charge finale ; c) τ (63 %) ; d) i à t = τ ; 2°) K en position 2 : Fig.3 (u_C sur Y₁, u_R₀ sur Y₂ ; 5 ms/div ; 1 V/div Y₁ ; 250 mV/div Y₂ ; points P et Q) : a) E_C, E_L en P et Q ; b) comparer les énergies totales. Rép. (p.318) : 1°a) « A t=0, u_C = E, donc (2) correspond à u_C » [?] ; 1°c) τ = 0,7 s [?] ; 1°d) i ≃ 158 μA [?].
- **12 Étude de texte — Capteur d'humidité** (p.105–106) : hygrométrie ; capteurs résistifs vs capacitifs (« humidistances ») ; condensateur plan C ≈ 120 pF, diélectrique polymère (permittivité variant avec l'humidité, Fig.1) inséré dans un RLC série (Fig.2) ; −10 °C à +40 °C ; 10 à 100 %HR ; réponse ~30 s. 1°) pourquoi « hygroscopique » ; 2°) variation de N₀ ; 3°) « Sachant que la valeur de C est à 40% HR et que … N₀ = 31850 Hz », L = 200 mH : taux d'humidité. Pas de corrigé.

### Fiche technique (p.107–109) — identique à 223433 p.107–109
« Visualisation d'un régime transitoire avec un oscilloscope analogique » : générateur de créneaux ±U₀ = ±5 V (Fig.1, 2), demi-période T_e/2 < θ_p = 0,1 s et très supérieure à T ; conditions T₀ << T_e ⇒ LC << T_e², T_e < θ_p ⇒ « LC << θ_p² = 10⁻² s² » ; Remarque : demi-période des créneaux dix fois plus grande que la constante de temps du dipôle RC ou RL ; entrée d'oscilloscope ≡ R_osc = 1 MΩ ∥ C_osc (16 à 47 pF) ; équation LC d²u_C/dt² + [(R₀ + r)C + L/R_osc] du_C/dt + (1 + (R₀ + r)/R_osc) u_C = u ; conditions « R/R_osc << 1 » et « L/((R₀ + r)C) << R_osc = 10⁶ Ω » ; encadré « LC << 10⁻² s² » ; exemples L = 10 mH, C = 100 μF, R₀ + r = 20 Ω (LC = 10⁻⁶, L/((R₀+r)C) = 5 Ω : « très bon choix ») vs L = 1 H, C = 1 μF (5.10⁴ Ω : « mauvais choix »). Pas de rubrique « En savoir plus ».

### Écart avec Sciences expérimentales
- **Ce que ce manuel ajoute : rien** dans le chapitre 3. Aucune notion, activité, manipulation, exercice ni encadré supplémentaire ; pas d'analogie mécanique, pas de résolution de l'équation amortie, pas de facteur de qualité, pas d'entretien des oscillations (résistance négative), pas de Fresnel, pas de condition R² vs 4L/C.
- **Ce que ce manuel retire : rien.** Les douze exercices (1 V/F, 2 QCM, 3–12), l'exercice résolu et la Fiche technique sont tous présents, avec les mêmes données (E = 5 V, C = 0,5 μF, R₀ = 100 Ω, L = 1 H, r = 12,5 Ω ; L = 10 mH, C = 100 μF ; C = 0,47 μF, L = 0,1 H, U₀ = 5 V ; ex. 3 à 12 inchangés).
- **Seules différences constatées** : (i) bandeau « Mathématiques » (page de titre) ; (ii) corrigés du chapitre 3 en **p.318** (vs p.316 dans 223433), contenu identique (y compris les corrigés douteux de l'ex. 11 et le renvoi tronqué de l'ex. 9) ; (iii) pagination des pages 316–317 hors chapitre (contenu nucléaire dans 223432, corrigés dans 223433) : sans objet pour le chapitre. Sur la couche texte, 17 pages ont des différences de caractères (symboles ω/φ/π, espaces, puces « • » vs « ∞ », « μ » vs « ∝ ») : encodage de police, aucune différence de contenu confirmée sur l'image.
- Conséquence pour les bornes : le **contenu du chapitre est le même qu'en Sciences expérimentales** ; toute différence de programme entre sections (profondeur de traitement, coefficients, exigences à l'examen) ne se lit **pas** dans ce manuel et doit venir du programme officiel ou des sujets de Bac section Mathématiques [?].

### Bornes de scope (chapitre 3, section Mathématiques)
- ✅ INCLUS (identique à `bac-sciences-exp`) :
  - Décharge d'un condensateur chargé dans une bobine (L ; r) + résistor R₀ : circuit RLC série libre ; visualisation u_C (image de q par q = Cu_C) et u_R₀ (image de i par u_R₀ = R₀i) à l'oscilloscope à mémoire ou par acquisition informatisée.
  - Vocabulaire : oscillations libres, amorties, pseudopériodiques, pseudopériode T ; régimes pseudopériodique, apériodique, (critique, cité seulement), périodique (R nulle) ; amortissement dû à la résistance totale R = R₀ + r.
  - Influence qualitative de R ; T légèrement supérieure à T₀ ; T ≈ T₀ pour un faible amortissement.
  - Équation différentielle par la loi des mailles en q (d²q/dt² + (R/L)dq/dt + (1/LC)q = 0), aussi en u (exercices, q = ± Cu selon l'orientation) ; forme d²u/dt² + (1/τ)du/dt + ω₀²u = 0 (ex. 10).
  - Énergies E_C = ½Cu_C² = q²/2C, E_L = ½Li², E = E_C + E_L ; dE/dt = − Ri² ; p = dE/dt ; effet Joule, système non conservatif ; transformations mutuelles non intégrales ; ½C(U_m2² − U_m1²) ; énergie thermique sur une oscillation.
  - Oscillateur LC : d²q/dt² + ω₀²q = 0, ω₀² = 1/LC ; solution **admise** q = Q_m sin(ω₀t + φ) et vérification ; ω₀ = 1/√LC, T₀ = 2π√LC, N₀ = 1/(2π√LC) ; amplitude et phase par les conditions initiales (sinφ, signe de cosφ via i(0)) ; i = dq/dt = I_m sin(ω₀t + φ + π/2), I_m = ω₀Q_m ; instants où |i| est maximale.
  - Conservation E = Q_m²/2C = ½LI_m² = ½CU_Cm² ; E_C = (Q_m²/4C)(1 + cos 2ω₀t), E_L = ¼LI_m²(1 − cos 2ω₀t) ; période des énergies = T₀/2 (T = 2T_E).
  - Lecture d'oscillogrammes ; calculs T₀, L, C à partir de T ; T′₀ après changement de L et C ; capteur capacitif (N₀ ⇒ C).
  - Rappels des chapitres 1–2 : I₀ = E/R, bobine idéale en régime permanent, loi de Lenz, dipôle RC (τ, 63 %, u = E(1 − e^(−t/τ))) dans les ex. 8 et 11.
- ⛔ EXCLU (absent du chapitre de ce manuel Mathématiques, comme de l'autre) :
  - **Résolution** de l'équation différentielle amortie (pas de q(t) amorti, pas d'exponentielle × sinus, pas de décrément logarithmique, pas de facteur de qualité Q — chapitre 4) ; résistance critique chiffrée (régime critique seulement nommé) ; aucune condition R² vs 4L/C.
  - Oscillations forcées, résonance, impédance, générateur sinusoïdal (chapitre 4) ; entretien des oscillations (résistance négative, amplificateur).
  - Démonstration de la solution générale (admise) ; pas de Fresnel ; écriture en sinus comme forme du cours.
  - Analogie mécanique avec le pendule élastique (chapitre 5) : absente ici.
  - Appareillage : oscilloscope analogique et impédance d'entrée de l'oscilloscope = Fiche technique uniquement (hors cours).
  - Aucun approfondissement propre à la section Mathématiques dans ce chapitre (aucun exercice supplémentaire, aucune généralisation) [?].

### Lecture
- **Couche texte** (pdftotext -layout) : p.78 à 109 (les 32 pages) + p.316–320 ; comparaison automatique page par page avec 223433 (espaces normalisés) : 15 pages identiques au caractère près (78–81, 83–87, 93, 97, 101, 103, 105, 106), 17 avec écarts de glyphes seulement (82, 88–92, 94–96, 98–100, 102, 104, 107–109), aucun écart de mots ou de chiffres relevé dans les diffs.
- **Pages vues sur l'image** (110 dpi) : **33** — 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 318. Les 32 pages du chapitre ont toutes été vues (sondage = totalité, plus denses : 85, 86, 88, 92, 94, 97, 98, 104, 108, 318). Pas de zoom 200 dpi ; p.316–317 et 319–320 en texte seulement (hors chapitre 3).
- **Écarts texte / image constatés** (comme pour 223433) : symboles grecs et √ supprimés (« o = 1/LC », « To = 2 LC ») ; équations éclatées (p.85, 86, 108) ; E_L = ½(L/R₀²)u_R₀² illisible (p.86) ; signe « − » de (1 − cos 2ω₀t) perdu (p.94) ; φ = π (p.98) et sinφ (p.91) perdus ; 1/τ de l'ex. 10 perdu (p.104) ; θ_p rendu « p » (p.107) ; valeurs des champs des Fig.13/14 et échelles des oscillogrammes seulement sur l'image.
- **Doutes [?]** (tous hérités à l'identique de 223433) :
  - [?] Contradiction p.84 (« durée aussi longue que R₀ est plus grande ») vs Conclusion p.85 (« retour … rapide ») : ne pas enseigner la phrase de la conclusion telle quelle.
  - [?] Ex. 11, corrigé p.318 : « A t=0, u_C = E, donc (2) correspond à u_C » contredit la Fig.2 (courbe (1) croissante part de 0) ; τ = 0,7 s incompatible avec RC = 30 kΩ × 50 μF = 1,5 s ; i ≃ 158 μA en découle : corrigé à ne pas reprendre sans re-résolution.
  - [?] Fig.11a/11b (p.86) : axe « En(μJ) » 0–0,6 alors que ½·0,5 μF·(5 V)² = 6,25 μJ ; aucune valeur numérique à en tirer.
  - [?] p.86 question 4° : complément (« de la résistance ») absent ; p.87 coquille « t₂ = nT + T/4 et t₂ = nT + T/2 » ; p.88 « φ(t) = ωt + φ » (indice o absent) ; p.107 Fig.1 abscisses « T₀/2 », « T₀ » pour la période T_e du créneau.
  - [?] Ex. 9 corrigé « Voir cours page 2° » (renvoi tronqué) ; W_J = 32,2 μJ non vérifiable sur la figure (pas de sensibilité verticale).
  - [?] Ex. 12 3° : « Sachant que la valeur de C est à 40% HR » : phrase incomplète, aucune loi C(%HR) ; non résoluble tel qu'imprimé.
  - [?] Ex. 4 : résistance de la bobine notée R (et non r) ; ex. 8 : 0,2 mV/div pour u₂ (recopié tel quel).
  - [?] Bornes au programme officiel non vérifiées ici (R-3) : place du régime critique et de la Fiche technique ; et toute différence de programme entre section Mathématiques et Sciences expérimentales sur ce chapitre (le manuel n'en montre aucune).

## 2.4 Chapitre 4 — Oscillations électriques forcées en régime sinusoïdal (manuel 223432, p.110–137)

**Rubrique** (bandeau) : « Evolution de systèmes ◆ Oscillations électriques forcées en régime sinusoïdal ». Le chapitre occupe **28 pages** (p.110–137) contre 34 dans 223433 ; la p.138 ouvre le chapitre 5 (pendule élastique). Notation du manuel : la phase initiale de i est notée **φ** (et non φᵢ), il n'y a aucune charge q(t) dans ce chapitre. Numérotation des figures propre à ce manuel (Fig.1–12 du cours ; Fig.1–5 de l'exercice résolu).

**Page d'ouverture (p.111)** — identique à 223433 p.111 (guitare électrique, même légende inclinée « …microphones électromagnétiques. Grâce à la résonance électrique, le son amplifié prime sur la résonance naturelle de la caisse. », mêmes deux questions d'accroche sur la recherche d'une chaîne radio/TV et la « résonance électrique »).

**Objectifs (p.110)** (verbatim, 9 puces) :
- Distinguer, en régime forcé, le résonateur de l'excitateur.
- Visualiser simultanément à l'oscilloscope la tension excitatrice u(t) et l'intensité du courant i(t).
- Mesurer l'amplitude et la fréquence d'une grandeur oscillante en régime forcé sinusoïdal.
- Déterminer le déphasage entre la tension excitatrice u(t) et l'intensité du courant i(t).
- Mettre en évidence expérimentalement le phénomène de résonance d'intensité.
- Établir l'expression de l'intensité maximale Iₘ du courant oscillant en fonction de la fréquence des excitations.
- Interpréter théoriquement le phénomène de résonance.
- Calculer la puissance moyenne absorbée par un oscillateur électrique.
- Expliquer l'importance du facteur de puissance dans les transformations de l'énergie électrique.
(Écart avec 223433 : ni « résonance de charge », ni « équation différentielle en i(t) ou q(t) », ni « déduire Qₘ ».)

**Prérequis (p.110)** — identiques à 223433 p.110 : SAVOIR : définir un oscillateur ; caractériser une grandeur sinusoïdale par période, amplitude, phase initiale ; T = 2π/ω et N = 1/T ; valeurs maximale Iₘ et efficace I de l'intensité alternative ; Uₘ et U de la tension alternative ; Iₘ = I√2 et Uₘ = U√2 ; E_c = q²/2C et E_L = ½ L.i². SAVOIR FAIRE : reconnaître un oscillateur ; visualiser à l'oscilloscope une tension, une intensité ; déterminer graphiquement période et amplitude ; calculer la période propre d'un RLC série ; établir l'équation différentielle des oscillations libres d'un RLC série par la loi des mailles ; calculer l'énergie totale d'un oscillateur RLC série. (Formules lues sur l'image.)

**Plan du chapitre** (pas de sommaire imprimé ; titres lus dans le corps) : introduction (p.112) · **1** Réponse d'un circuit RLC série à une tension sinusoïdale (1.1 Production d'oscillations forcées, p.112–114 ; 1.2 Déphasage, p.114–115) · **2** Influence de la fréquence d'excitation sur la réponse d'un circuit RLC série (p.115–119 : manipulation, interprétation théorique par Fresnel, résonance d'intensité) · **3** Influence de la résistance totale du circuit sur la résonance (p.119–120) · **4** Le phénomène de surtension (p.120–121) · **5** Applications de la résonance (p.121–122) · **6** Puissance moyenne et facteur de puissance (6.1 instantanée ; 6.2 moyenne ; 6.3 résonance de puissance ; 6.4 transfert de puissance moyenne ; 6.5 importance du facteur de puissance cosφ ; p.122–125) · L'essentiel (p.126) · Exercices : exercice résolu (p.127–129), Exercices à résoudre (p.130–135 : tests rapides 1–2, application 3–11, synthèse 12–15, étude de texte 16) · Fiche technique « Construction de Fresnel » (p.136) · En savoir plus (p.137). Réponses : p.318 (chapitre 4, colonne droite).
(Titre de la p.112 imprimé « OSCILLATIONS ÉLECTIRQUES FORCÉES » — même coquille que 223433.)

### Cours — Manipulations, questions, conclusions

**Introduction (p.112)** — identique à 223433 p.112 : « On a vu dans le chapitre précédent que si un circuit RLC série peut effectuer des oscillations libres, celles-ci cessent plus au moins rapidement à cause de l'amortissement dû à sa résistance. Quel sera l'effet de l'application d'une tension sinusoïdale aux bornes d'un tel oscillateur, une simple compensation de l'amortissement ou plus ? »

**1.1 Production d'oscillations forcées — Manipulation (p.112–113)**
- Dispositif identique à 223433 p.112 (Fig.1 : GBF entre A et M, K, C, (L, r), Ro entre B et M ; M à la masse, A → Y1, B → Y2) : u(t) = Uₘ.sinωt, Uₘ constante ; Ro réglable, C = 0,47 μF, L = 0,2 H, r = 12,5 Ω ; N = 400 Hz, Uₘ = 2 V, Ro = 50 Ω « par exemple » ; K ouvert → oscillogramme (1) seul ; K fermé → oscillogrammes (1) et (2) stables (Fig.2), 1 ms/div ; série de mesures de U_Rom en fonction de Uₘ à 400 Hz → Fig.3 (droite passant par l'origine, U_Rom en ordonnée 0–0,8 V, Uₘ en abscisse 0–4 V, point final lu ≈ (4 V ; 0,6 V) : lecture graphique, non donnée).
- **Retiré par rapport à 223433** : le second montage (condensateur côté masse, voie Y2 sur D), l'oscillogramme de u_C et la figure correspondante, donc toute mesure de Qₘ.
- **Questions (4, au lieu de 6)** : 1°) Comparer la forme de l'oscillogramme représentant i(t) à celle de u(t). 2°) Mesurer la fréquence N de i(t) et la comparer à celle de u(t). 3°) Comparer la fréquence N à la fréquence propre No de l'oscillateur. 4°) a) À l'aide de la courbe de la figure 3, montrer que Uₘ = kU_Rom, où k est une constante que l'on calculera. b) Montrer que la tension maximale Uₘ peut s'écrire en fonction de l'intensité maximale Iₘ sous la forme Uₘ = Z Iₘ où Z est une constante dont on déterminera la dimension. (Aucune réponse imprimée. Contrôle non imprimé : lecture (4 V ; 0,6 V) ⇒ k ≈ 6,7.)
- **Commentaire (p.113)** (verbatim) : « L'analyse des oscillogrammes de la figure 2 montre que, comme celle de u(t), la courbe représentant i(t) varie sinusoïdalement au cours du temps. De plus, il y a constamment le même décalage horaire entre les deux oscillogrammes. Par conséquent, l'intensité i(t) varie avec la même fréquence que la tension u(t) imposée par le GBF et non avec la fréquence propre du circuit RLC série : les oscillations imposées par le GBF ne sont plus libres, elles sont forcées. Ainsi, le GBF a joué le rôle d'excitateur. La forme linéaire de la courbe représentant U_Rom en fonction de Uₘ montre que le quotient Uₘ/Iₘ est une constante qui ne dépend que des caractéristiques de l'oscillateur. On l'appelle impédance du circuit et on la note Z. » — **Retiré** : la phrase de 223433 « Ayant la dimension d'une résistance électrique, l'impédance s'exprime en ohm (Ω) » (la dimension « d'une résistance » reste dite dans la Conclusion ci-dessous).

**Interprétation théorique (p.113–114)** (verbatim) — « Pour le circuit utilisé précédemment, la loi des mailles s'écrit : u_BM + u_DB + u_AD + (−u_AM) = 0, d'où u_AM = u_BM + u_DB + u_AD. Donc, u_AM = Ro.i + r.i + L di/dt + q/C, soit u_AM = Ro.i + r.i + L di/dt + q/C [ligne imprimée deux fois]. Or, q = ∫i.dt. Donc, u_AM = R.i + L di/dt + (1/C)∫i.dt, où R = Ro + r et ω = 2πN. Une telle équation différentielle à second membre non nul admet comme solution particulière celle du régime permanent : i(t) = Iₘsin(ωt + φ). » 
> **Remarque** (p.114, verbatim) : « La solution générale faisant apparaître de plus le régime transitoire qui ne dure qu'une très petite fraction de seconde est hors programme. » **[NOUVEAU — absent de 223433]**
> **Conclusion (p.114)** : « La réponse d'un circuit RLC série à une tension sinusoïdale est un courant alternatif sinusoïdal y oscillant : – à la fréquence N de la tension excitatrice, – avec une amplitude Iₘ = Uₘ/Z, où Z est une grandeur physique ayant la dimension d'une résistance appelée impédance du circuit RLC série. »
(Seule l'équation en i(t) est établie ; **pas d'équation en q(t)**, pas de relation Qₘ = Iₘ/2πN.)

**1.2 Déphasage (p.114–115)** — Définition, exemples (Fig.4a concordance, 4b opposition, 5a quadrature retard, 5b quadrature avance), 4 questions et Conclusion **identiques à 223433 p.115–116** pour le fond (voir ci-dessous les encadrés). Questions : 1°) justifier qualitativement concordance / opposition de phase ; 2°) a) concordance ⇒ Δφ = 2kπ rad (k entier relatif) ; b) opposition ⇒ Δφ = (π + 2kπ) rad ; 3°) « dans les cas de la figure 7 » [sic : ce sont les figures 5a/5b] où Δt = T/4, quadrature de phase ; u₂ en quadrature retard sur u₁ (fig. « 7a »), en quadrature avance (fig. « 7b ») : expliquer par le calcul de Δφ ; 4°) déduire |Δφ| = (2π/T)Δt. **Retiré** : le paragraphe 1.2.2 (déphasage i / q : φᵢ − φ_q = π/2) et sa question.
> **Définition (p.114)** : « On appelle déphasage entre deux fonctions sinusoïdales de phases initiales φ₁ et φ₂ et de même période, la différence de phase Δφ = (φ₂ − φ₁) ou (φ₁ − φ₂). »
> **Conclusion (p.115)** : « A tout décalage horaire Δt entre deux fonctions sinusoïdales y₁(t) et y₂(t) isochrones (de même péride T), représentées dans le même système d'axes, est associé un déphasage Δφ tel que : |Δφ| = (2π/T)Δt. – Si Δt = 0, Δφ = 0 : les deux fonctions sont en concordance de phase. – Si Δt = T/2, Δφ = ± π rad : les deux fonctions sont en opposition de phase. – Si Δt = T/4, Δφ = ± π/2 rad : les deux fonctions sont en quadrature de phase. Si le déphasage (φ₂ − φ₁) est positif, y₂(t) est en avance de phase par rapport à y₁(t) et inversement. »

**2 Influence de la fréquence d'excitation — Manipulation (p.115–116)**
- Montage de la figure 1, u(t) = Uₘsin2πNt, Uₘ = 2 V. En faisant varier N : u_Ro(t) garde la même forme sinusoïdale, U_Rom et le décalage horaire Δt par rapport à u(t) changent. Mesures de Iₘ et de Δt (entre u et i) en fonction de N → **Fig.6a** (Iₘ en mA, axe 0–32, N 0–700 Hz : pic ≈ 32 mA vers 520 Hz) et **Fig.6b** (phase initiale φ de i en rad en fonction de N : positive aux basses fréquences, nulle vers 520 Hz, négative au-delà ; plateaux aux deux extrémités) — **Fig.6b NOUVELLE**. Remarque : « Il est pratique aussi de suivre à l'aide d'un ampèremètre l'évolution de l'intensité efficace I en fonction de la fréquence N. » (même remarque que 223433). Valeurs lues sur graphiques, non imprimées. **Retiré** : mesure de la tension u_C et de Qₘ, Fig.8 (ampèremètre + voltmètre) et courbe Qₘ(N) de 223433.
- **Questions** : 1°) Montrer que, dans les conditions de l'expérience réalisée, la valeur de la phase initiale φ est égale à la valeur du déphasage entre i et u. [NOUVELLE] 2°) Décrire la forme particulière de la courbe représentant Iₘ en fonction de N. 3°) a) Déterminer graphiquement la valeur de la fréquence N pour laquelle Iₘ est à sa valeur la plus élevée I_mo et la comparer à la fréquence propre No de l'oscillateur. b) Relever I_mo et la valeur correspondante φ₀ de φ. c) Calculer l'impédance Z qu'a le circuit RLC dans ce cas particulier et la comparer à sa résistance totale (Ro + r). (Pas de réponse imprimée. Contrôle non imprimé : No = 1/(2π√LC) ≈ 519 Hz pour L = 0,2 H, C = 0,47 μF ; Uₘ/(Ro + r) = 32 mA pour Ro = 50 Ω, ce qui rend la Fig.6a cohérente avec Ro = 50 Ω, valeur non redite en §2.)
> **Conclusion (p.116)** (verbatim) : « En régime forcé sinusoïdal, l'intensité maximale Iₘ et la phase initiale φ du courant oscillant dans un circuit RLC série dépendent de la fréquence N de la tension excitatrice et des grandeurs R, L et C caractéristiques de l'oscillateur. La réponse d'un circuit RLC série à une tension sinusoïdale de fréquence N égale à la fréquence propre No du circuit est un courant oscillant en phase avec la tension excitatrice et avec l'intensité maximale la plus élevée : c'est la résonance d'intensité. A la résonance d'intensité, le circuit RLC série se comporte comme un résistor de résistance R. » (Plus de mention d'une résonance de charge.)

**Interprétation théorique — Fresnel (p.116–118)** (renvoi « fiche technique de fin de chapitre (p.136) » : correct ici) — mêmes étapes que 223433 p.118, notation φ. 
> (p.116–117, verbatim) « On a : Ri + L di/dt + (1/C)∫i.dt = Uₘ sinωt, avec R = Ro + r ; i(t) = Iₘ sin(ωt + φ). di/dt = ωIₘ sin(ωt + φ + π/2) ; ∫i.dt = (Iₘ/ω) sin(ωt + φ − π/2) + cte. Il vient alors : RIₘ sin(ωt + φ) + LωIₘ sin(ωt + φ + π/2) + (Iₘ/Cω) sin(ωt + φ − π/2) + cte/C = Uₘ sin(ωt). Étant une fonction sinusoïdale, Uₘ sinωt ne peut être qu'une somme de fonctions sinusoïdales. Donc, cte = 0. ● RIₘ sin(ωt + φ) ↦ OA⃗₁ [RIₘ, φ] ● LωIₘ sin(ωt + φ + π/2) ↦ OA⃗₂ [LωIₘ, φ + π/2] ● (Iₘ/Cω) sin(ωt + φ − π/2) ↦ OA⃗₃ [Iₘ/Cω, φ − π/2] ● Uₘ sinωt ↦ OA⃗ [Uₘ, 0] tel que : OA⃗ = OA⃗₁ + OA⃗₂ + OA⃗₃. Les vecteurs de Fresnel OA⃗₂ et OA⃗₃ étant de sens contraires, il en résulte trois constructions possibles : ● ‖OA⃗₂‖ > ‖OA⃗₃‖, cas correspondant à Lω > 1/Cω c'est-à-dire N > No : construction de la figure 7a. ● ‖OA⃗₂‖ < ‖OA⃗₃‖, cas Lω < 1/Cω c'est-à-dire N < No : figure 7b. ● ‖OA⃗₂‖ = ‖OA⃗₃‖, cas Lω = 1/Cω c'est-à-dire N = No : figure 7c. »
> (Fig.7a/7b/7c : Uₘ horizontal (φ = 0, « u »), R.Iₘ, LωIₘ, Iₘ/Cω, angle φ ; 7c : R.Iₘ confondu avec Uₘ, « u ; i ».)
> (p.117, encadrés, verbatim) « Dans le cas général, on a : Uₘ² = (RIₘ)² + (LωIₘ − Iₘ/Cω)², d'où Uₘ = √(R² + (Lω − 1/Cω)²) Iₘ. Donc, **Iₘ = Uₘ / √(R² + (Lω − 1/Cω)²)**, soit : Iₘ = Uₘ/Z avec **Z = √(R² + (Lω − 1/Cω)²)**. D'après le cas de la figure 7a, Lω > 1/Cω, on a φ < 0, ça signifie que l'intensité i(t) du courant est en retard de phase par rapport à la tension excitatrice u(t) : le circuit RLC série est dit **inductif**. D'après le cas de la figure 7b, Lω < 1/Cω, on a φ > 0, ça signifie que l'intensité i(t) du courant est en avance de phase par rapport à la tension excitatrice u(t) : le circuit RLC série est dit **capacitif**. D'après les constructions précédentes, on a : **|tgφ| = |Lω − 1/Cω| / R**. »
> (p.118) « En tenant compte de la dépendance du signe de φ de celui de (Lω − 1/Cω), la phase initiale φ de i est telle que : **tgφ = (1/Cω − Lω)/R, avec −π/2 rad < φ < π/2 rad**. » Remarque : « Le déphasage φ entre i et u peut être aussi caractérisé par : **cos φ = R/Z** ».
> **Résonance d'intensité (p.118)** (verbatim) : « L'impédance du circuit s'écrit Z = √(R² + (Lω − 1/Cω)²). ∞ Aux très basses pulsations ainsi qu'aux pulsations beaucoup plus élèvées que la pulsation propre ωo de l'oscillateur, l'écart entre Lω et 1/Cω augmente. Par suite, l'impédance Z devient de plus en plus grande. Donc, dans l'un ou dans l'autre cas, Iₘ(ω) = Uₘ/Z → 0, ce qui signifie que la réponse du circuit RLC série devient de plus en plus faible. Cette réponse s'améliore lorsque Z prend une valeur modérée, ce qui n'est possible qu'avec des valeurs comparables de Lω et de 1/Cω. Dans le cas particulier où Lω = 1/Cω, obtenu avec ω = ωo = 1/√LC : ∞ l'impédance Z est minimale : Z = R. Par conséquent, l'intensité maximale prend sa valeur la plus élevée **I_m0 = Uₘ/R** : c'est la résonance d'intensité. ∞ tgφ = (1/Cω − Lω)/R = 0, ce qui signifie qu'à la résonance, la tension u et l'intensité i sont en phase. » Remarque : « L'appellation d'un oscillateur en régime forcé comme étant un résonateur revient au phénomène de résonance. »
> **Conclusion (p.119)** : « La réponse d'un circuit RLC série à une tension sinusoïdale de fréquence N égale à la fréquence propre No du circuit est un courant oscillant en phase avec la tension excitatrice et avec l'intensité maximale la plus élevée : c'est la résonance d'intensité. **N = No = 1/(2π√LC) : Résonance d'intensité ⇔ { Iₘ est la plus élevée ; u et i sont en phase }** »
(Identique à 223433 p.118–121 pour Iₘ, Z, φ, cosφ, résonance d'intensité ; **retirés** : Qₘ = Iₘ/ω, φ_q = φᵢ − π/2, −π < φ_q < 0, toute la « résonance de charge » (étude de g(ω), ω₁² = 1/LC − R²/2L², Nr) et la conclusion théorique double intensité/charge.)

**3 Influence de la résistance totale — Manipulation (p.119)** — « On refait l'étude expérimentale du paragraphe 2 (p.115), toujours avec L = 0,2 H et C = 0,47 μF, mais en fixant R0 successivement aux valeurs R02 = 20 Ω et R03 = 200 Ω. » **[VALEURS DIFFÉRENTES : 223433 prend Ro₁ = 50 Ω, Ro₂ = 200 Ω, Ro₃ = 1000 Ω ; ici deux valeurs seulement, 20 Ω et 200 Ω.]** Résultats : courbes de résonance d'intensité (1) et (2) de la Fig.8a (R02 et R03 ; Iₘ 0–32 mA ; (1) pic très pointu ≈ 32 mA vers 520 Hz, (2) pic très aplati ≈ 10 mA) ; courbes (a) et (b) de la Fig.8b (phase initiale φ de i en fonction de N, pour R02 et R03 : chute de φ de + à − autour de 520 Hz, plus raide pour (a)).
- **Questions** : 1°) Comparer les allures des courbes de résonance (1) et (2) entre elles et avec celle de la courbe de la figure 6a ; en déduire l'influence de la résistance totale du circuit sur la résonance. 2°) Pour les valeurs R02 et R03 de R0, déterminer graphiquement : a) la valeur de la fréquence de résonance ; b) le déphasage φ correspondant entre l'intensité i et la tension d'alimentation u. (Pas de réponse imprimée.)
- **Interprétation (p.119)** (verbatim) : « A la résonance d'intensité, on a I_mo = Uₘ/R. Cela signifie que l'importance de la résonance dépend de l'ordre de grandeur de R, donc de Ro car R = Ro + r : I_mo est d'autant plus grande que R est plus petite. – Si R est très petite, le maximum de Iₘ est très élevé, ce qui se traduit par un pic de résonance très pointu (courbe (1) de la figure 8a) : c'est la résonance aiguë. – Si R est grande, I_mo est faible, ce qui se traduit par un pic de résonance très peu prononcé (courbe (2) de la figure 8a) : c'est la résonance floue. »
> **Conclusion (p.120)** : « La résonance d'intensité de courant d'un oscillateur RLC série est d'autant plus aiguë que l'amortissement est faible. Cependant, quel que soit l'amortissement, la fréquence de résonance reste toujours égale à la fréquence propre du résonateur. »
(**Retirés** vs 223433 : courbes Qₘ (Fig.11b), résonance « très floue », résonance de charge, « résonance impossible » si R² − 2L/C > 0, « réponse linéaire », Conclusion §3 sur la fréquence de résonance de charge.)
[?] **Fig.8a** : la courbe (1) est identique à la courbe de la Fig.6a (pic ≈ 32 mA), alors que le texte l'attribue à R02 = 20 Ω ; or Uₘ/(Ro + r) = 2/32,5 ≈ 61 mA pour Ro = 20 Ω, et ≈ 32 mA pour Ro = 50 Ω. La courbe (2) ≈ 10 mA est cohérente avec Ro = 200 Ω (≈ 9,4 mA). Lecture graphique à 200 dpi ; ne pas faire lire la valeur du pic de (1) comme donnée.

**4 Le phénomène de surtension — Manipulation (p.120)** — identique à 223433 p.125 : fig.1, L = 0,2 H, C = 0,47 μF, Uₘ = 2 V, N = No = 520 Hz ; tableau Ro (Ω) 20 / 50 / 200 → U_Cm (V) 40 / 21 / 6,5. Questions identiques (1°) tableau à compléter Q = U_Cm/Uₘ ; 2°) Q « facteur de surtension à la résonance », justifier ; 3°) a) Q en fonction de R, L, C, b) valeurs théoriques pour 20, 50, 200 Ω ; 4°) précaution pour un facteur de surtension modéré). Pas de réponse imprimée. (Contrôle non imprimé : Q = (1/(Ro + r))√(L/C) ≈ 20,1 ; 10,4 ; 3,07 contre 20 ; 10,5 ; 3,25 mesurés.)
> **Expression de Q (p.120–121)**, **Remarque** (Fig.9 : diagramme de Fresnel, U horizontal, RₒI, rI, LωₒI, U_Bobine, I/(Cωₒ) = U_C) et **Conclusion** — identiques mot pour mot à 223433 p.126 : « Pour une pulsation ω égale à la pulsation propre ωo, U_C = Io/Cωo et Io = U/(Ro + r). D'où : **Q = 1/((Ro + r)Cωo)** (1). Or, 1/Cωo = Lωo. Donc, Q s'exprime autrement comme suit : **Q = Lωo/(Ro + r)** (2). En remplaçant ωo par 1/√LC dans (1) par exemple, il vient : Q = (1/((Ro + r)C))√LC. Donc : **Q = (1/(Ro + r))√(L/C)**. Donc, le facteur de surtension Q augmente quand l'inductance L augmente et lorsque la capacité C et la résistance R du circuit diminuent. S'il est trop élevé, la surtension devient dangereuse tant pour l'utilisateur que pour les composants du circuit ou les appareils d'une manière générale : elle peut provoquer le claquage du condensateur et des étincelles entre les spires de la bobine, d'où le risque d'électrocution. » — Remarque : « A la résonance d'intensité : U = (Ro + r)I et U_Bobine = √(r² + (Lωo)²) I. Si la valeur de l'inductance L est telle que, Lωo >> (Ro + r), la valeur de la tension efficace aux bornes de la bobine sera plus grande que la valeur de la tension efficace d'alimentation. Donc, il y a aussi risque de surtension aux bornes de la bobine (Fig.9). » — Conclusion : « – A la résonance d'intensité d'un circuit RLC série, il peut surgir aux bornes du condensateur, une surtension caractérisée par le facteur : **Q = (1/(Ro + r))√(L/C)** – Le facteur de surtension Q est d'autant plus grand que la résonance est plus aiguë. – Une surtension élevée peut entraîner des conséquences néfastes. »

**5 Applications de la résonance (p.121–122)** — identique à 223433 p.127 : oscillateurs à quartz, haut-parleur et microphone électrodynamique, réception d'émissions radiophoniques ; poste radio ordinaire = résonance aiguë (accorder la fréquence propre de l'oscillateur RLC série du récepteur avec la fréquence de la station) ; chaîne « haute fidélité » = résonance floue (courbes « les plus aplaties possibles » dans le domaine audible, pour restituer les timbres).

**6 Puissance moyenne et facteur de puissance (p.122–125)** — pas de manipulation ; identique à 223433 p.127–130 pour le fond (numéros de figures différents : Fig.10 dipôle D, Fig.11 P(N) — pic ≈ 60 mW vers 520 Hz, axe 0,8 → 64 mW, lecture graphique — Fig.12 résonances aiguë/floue de P(N)). Phrase d'introduction : « Dans ce paragraphe, on se propose d'étudier le bilan énergétique des oscillations forcées d'un circuit RLC série en régime sinusoïdal. » Différence mineure en 6.1 : « Étant générale, cette expression est applicable au circuit RLC série. »
> **6.1 (p.122)** (verbatim) : « En appliquant à ses bornes A et B une tension sinusoïdale de basse fréquence u(t) = U√2 sinωt, un dipôle D (Fig.10) sera parcouru par un courant d'intensité sinusoïdale i(t) = I√2 sin(ωt + φ) et recevra, à tout instant, une puissance électrique : p(t) = u(t).i(t). […] p = u.i = U√2 sin(ωt).I√2 sin(ωt + φ) = 2U.I.sin(ωt + φ)sin(ωt). En appliquant […] la relation trigonométrique sin a.sin b = ½[cos(a − b) − cos(a + b)], on aboutit à : **p = UIcosφ − UIcos(2ωt + φ).** On constate que la puissance instantanée est la somme algébrique du terme constant « UIcosφ » et du terme « − UIcos(2ωt + φ) » évoluant périodiquement au cours du temps avec une fréquence double de celle de u et de i, ce qui rend p(t) périodique de période Tp = T/2. Ainsi, pendant une demi oscillation de i, cos(2ωt + φ) varie entre +1 et −1. Par conséquent, p peut être positive et le dipôle RLC série est effectivement un récepteur. Puis, elle peut devenir négative et le même dipôle se comporte alors comme un générateur. Cependant, pour déterminer le bilan, ces constatations restent insuffisantes. »
> **6.2 Définition (p.122–123)** : « La puissance moyenne d'un dipôle D est la valeur moyenne prise par sa puissance instantanée p(t) sur une très grande durée Δt (tendant vers l'infini). Lorsque p(t) est périodique(⊙), il est équivalent de prendre Δt égale à une période. On note la puissance électrique moyenne P et on l'appelle aussi en régime forcé sinusoïdal, puissance électrique active ou réelle. Comme toute puissance, la puissance moyenne s'exprime en watt (W) et se mesure avec un wattmètre. » Note marginale ⊙ : « Le cas unique qui figure dans le programme est celui du régime sinusoïdal forcé. »
> **Expression de P (p.123)** : « Lorsque la puissance instantanée p(t) est périodique, sa valeur moyenne P sur une période Tp s'écrit : **P = (1/Tp) ∫_{kTp}^{(k+1)Tp} p(t)dt** où k est un entier naturel. En régime sinusoïdal, on vient de trouver : p(t) = UIcosφ − UIcos(2ωt + φ). Donc, P = (1/Tp)∫UIcosφ dt − (1/Tp)∫UIcos(2ωt + φ)dt. Ce qui donne : P = (UIcosφ/Tp)[t] − (UI/2ωTp)[sin(2ωt + φ)]. La fonction sin(2ωt + φ) étant périodique de période Tp = π/ω, on a : [sin(2ωt + φ)]_{kTp}^{(k+1)Tp} = 0. Cependant, [t]_{kTp}^{(k+1)Tp} = Tp. Il vient donc : **P = UIcosφ**. Cette forme générale de l'expression de la puissance moyenne est indépendante de la nature du dipôle. Étant semblable à l'expression de la puissance consommée en courant continu, le produit UI intervenant dans l'expression de P est appelé **puissance apparente** du dipôle. La puissance apparente s'exprime en volt-ampère (V.A). Le facteur **cosφ** auquel la puissance moyenne est proportionnelle s'appelle **facteur de puissance**. Pour le circuit RLC série, cosφ = R/Z. Donc, ce facteur est toujours positif. Par suite, la puissance moyenne est positive, ce qui veut dire que le circuit RLC série se comporte dans l'ensemble comme un dipôle passif. » (p.124) « D'autre part, on a U = Z.I, d'où : **P = R.I²**. Ainsi, on montre que la puissance active d'un circuit RLC série est due à sa résistance totale R : c'est une puissance consommée par effet Joule. En d'autres termes, la puissance moyenne dissipée dans le circuit sert à compenser l'amortissement : en moyenne, l'énergie transférée de l'excitateur à l'oscillateur sert, lorsque le régime oscillatoire est établi, à compenser les pertes par effet Joule. »
> **6.3 Résonance de puissance (p.124)** : « La puissance moyenne (P = RI²) d'un circuit RLC série est proportionnelle au carré de l'intensité efficace du courant oscillant dans le circuit. il s'en suit une résonance de puissance à chaque fois qu'il y a résonance d'intensité (Fig.11). A la résonance d'intensité, P est maximale, ce qui est en accord avec la condition (cosφ = 1) établie précédemment. »
> **6.4 Transfert de puissance moyenne (p.124)** : « La puissance moyenne fournie par le GBF au circuit RLC série en régime forcé sinusoïdal est : **P = R U²/Z² = RU² / (R² + (Lω − 1/Cω)²)**. Discutons cette relation dans les deux cas extrêmes d'amortissement. – Si l'amortissement est important, lorsque ω tend vers zéro ou ω est très grand, la puissance transférée est quasiment nulle. Mais, au voisinage de ωo, P devient égale à U²/R. Le transfert de puissance s'effectue alors quelle que soit la fréquence mais il reste faible. Par conséquent, l'amplitude des oscillations est faible. C'est ce qui justifie la résonance floue (Fig.12). – Si l'amortissement est faible, le transfert de puissance est important. Par conséquent, l'amplitude des oscillations est élevée. C'est ce qui justifie la résonance aiguë (Fig.12). »
> **6.5 Importance du facteur de puissance cosφ (p.124–125)** : « Dans toute installation électrique, la tension d'alimentation est imposée par le réseau de distribution de la STEG. Tout appareil de l'installation est caractérisé par sa puissance nominale, puissance moyenne en fonctionnement normal. En marche, il sera parcouru par un courant d'intensité efficace : **I = P/(U cosφ)**. Le courant électrique débité provoque un échauffement par effet Joule des câbles de la ligne de transport d'électricité. Par conséquent, de la puissance est perdue et, en grande partie, la perte est à la charge de la STEG : c'est la perte en ligne. Comment minimiser la perte en ligne ? Si l'on désigne par Po la puissance moyenne perdue par effet Joule dans la ligne d'alimentation de résistance Ro, on a : Po = RoI², soit : **Po = Ro P²/(U²cos²φ)**. P et U étant imposées, pour minimiser Po, il faut chercher à minimiser Ro et augmenter cosφ. Les possibilités de diminution de Ro sont limitées. En effet, l'opération demande l'augmentation du diamètre des câbles électriques, ce qui augmente leurs poids. Par conséquent, les lignes et leur infrastructure coûteront beaucoup plus cher. Ainsi, la seule solution pratique pour rendre minimales les pertes par effet Joule est d'augmenter le facteur de puissance cosφ. Pour ce, on exige qu'une installation électrique ait un facteur de puissance élevé (cosφ > 0,8). »
> **Conclusion (p.125)** : « La puissance moyenne d'un circuit RLC série est dissipée par effet Joule. Cette dissipation se fait à n'importe quelle fréquence mais elle est d'autant plus importante que la résistance est plus grande. A la résonance d'intensité, correspond une résonance de puissance : la puissance moyenne de l'oscillateur RLC série est dans ces conditions la plus élevée. »

### L'essentiel (p.126, verbatim)

- Comme en régime libre non amorti, les oscillations forcées d'un circuit RLC série sont sinusoïdales mais de fréquence imposée par l'excitateur.
- La réponse d'un circuit RLC série à une tension excitatrice sinusoïdale de fréquence N est un courant électrique d'intensité sinusoïdale de valeur maximale Iₘ et de phase initiale φ dépendant de la fréquence des excitations et des grandeurs électriques R, L et C caractéristiques de l'oscillateur : **Iₘ = Uₘ / √(R² + (Lω − 1/Cω)²)** ; **tgφ = (1/Cω − Lω)/R**.
- En régime forcé sinusoïdal, selon que le circuit RLC série, est capacitif (1/Cω > Lω) ou bien inductif (Lω > 1/Cω), l'intensité i du courant électrique y oscille en avance de phase ou bien en retard de phase par rapport à la tension excitatrice u. [juste ; cohérent avec p.117]
- En régime forcé sinusoïdal, la valeur maximale de l'intensité du courant est d'autant plus élevée que l'amortissement est plus faible.
- La résonance d'intensité est obtenue pour une fréquence d'excitations égale à la fréquence propre de l'oscillateur. Dans ces conditions, i oscille en phase avec u.
- La résonance d'intensité d'un circuit RLC série peut être accompagnée d'une surtension aux bornes du condensateur, caractérisée par un quotient Q > 1 appelé dans ces conditions facteur de surtension : **Q = U_C/U**.
- En régime sinusoïdal forcé, la puissance moyenne P d'un circuit RLC série est la valeur moyenne prise par sa puissance instantanée p(t) durant une période : **P = UIcosφ = RI²**.
- Comme la résonance d'intensité, la résonance de puissance est obtenue pour une fréquence d'excitations égale à la fréquence propre de l'oscillateur.
- Les pertes par effet Joule sont d'autant plus faibles que le facteur de puissance est plus grand.
(**Écart** : l'Essentiel de 223433 contient la formule de Qₘ (fautive à l'impression), le déphasage de q et la résonance de charge : tout cela disparaît ; **la coquille de 223433 est absente** — ici capacitif/inductif ↔ avance/retard est juste.)

### Exercice résolu (p.127–129) — **identique à 223433 p.132–134 sauf trois points (listés plus bas)**

**Énoncé** : condensateur C, bobine B (L), résistor Ro = 81,5 Ω en série ; GBF u(t) sinusoïdale, Uₘ = 6 V, N réglable (Fig.1 : GBF entre A et B ; K, Ro entre B et D ; bobine (L, r) entre D et E ; C entre E et A). 1°) a) point (A ou B) à relier à la masse pour visualiser u(t) et u_Ro ; b) schéma des branchements. 2°) N₁ ; Fig.2 : 0,5 ms/div, voie u(t) 2 V/div, voie u_Ro 1 V/div : a) identifier u(t) ; b) N₁ et Iₘ graphiquement ; c) Z ; d) déphasage graphique entre i et u, en déduire que la bobine a une résistance interne non nulle, la calculer. 3) Autre fréquence N₂, on visualise u(t) et u_C(t) : a) masse ; b) schéma ; c) Fig.3, 1 ms/div, 2 V/div sur Y1 et Y2 : identifier u_C(t) ; d) fréquence de u_C(t) et son déphasage par rapport à u(t) ; **e) montrer que l'oscillateur RLC série est en résonance d'intensité** ; f) facteur de surtension, danger ? ; g) calculer C et L.
**Solution** : 1°a) masse au point B (côté résistor) ; b) A → Y1 (ou Y2), D → Y2 (ou Y1) (Fig.4). 2°a) Uₘ = 6 V à 2 V/div : l'oscillogramme (1) « dont les crêtes sont distantes de 6 div » est u(t). b) u_Ro = Ro.i ⇒ même fréquence ; T₁ sur 6 divisions à 0,5 ms/div ⇒ T₁ = 3 ms, **N₁ ≈ 333 Hz** ; 2 div ↔ U_Rom, 1 div ↔ 1 V ⇒ U_Rom = 2 V ⇒ **Iₘ = U_Rom/Ro = 24,5 mA**. c) **Z = Uₘ/Iₘ = 244,9 Ω ≈ 245 Ω**. d) Δφ = φᵢ − φ_u ; Δt = T/6 et π rad ↔ T/2 ⇒ |Δφ| = π/3 ; maxima de u_Ro après ceux de u ⇒ **Δφ = −π/3 rad** ; cosφ = R/Z ⇒ R = Z.cosφ = 122,5 Ω > Ro = 81,5 Ω ⇒ **r = R − Ro = 41 Ω**. 3°a) masse au point A (Fig.5) ; b) B → Y1 (ou Y2), E → Y2 (ou Y1). c) (1) seul d'amplitude 6 V = u(t) ; (2) = u_C(t). d) **N₂ = 167 Hz** ; maxima de u atteints T/4 avant ceux de u_C ⇒ u_C en quadrature retard : **φ_uC − φ_u = −π/2 rad**. e) i = dq/dt ⇒ φᵢ = φ_q + π/2 ; u_C = q/C ⇒ φ_uC = φ_q ; donc φᵢ = φ_uC + π/2 ; φ_u − (φᵢ − π/2) = π/2 ⇒ **φ_u − φᵢ = 0** : résonance d'intensité. f) Q = U_Cm/Uₘ ; U_Cm = 7 V ⇒ **Q ≈ 1,17** ; « Q étant très peu supérieur à l'unité du fait que U_Cm est très légèrement supérieure à Uₘ, on ne court aucun danger. » g) résonance d'intensité : Q = 1/(RCω₂) ⇒ C = 1/(RQω₂), ω₂ = 2πN₂ ⇒ **C = 6,68 μF** (imprimé « 6,68 ∝F ») ; N₂ = 1/(2π√LC) ⇒ L = 1/(4π²N₂²C) ⇒ **L = 137 mH**.
Écarts avec l'ER de 223433 : (i) **3°e) ne demande plus « ou bien en résonance de charge »** ; la solution ne conclut plus que sur la résonance d'intensité ; (ii) la solution **ne calcule pas Qₘ** (pas de « En déduire Qₘ » en 2°b, pas de Qₘ = 11,7.10⁻⁶ C) ; (iii) mise en page des figures (Fig.1 dessinée avec C en bas). Coquilles conservées : « 3) » sans « ° » dans l'énoncé ; la solution 3°f renvoie à « la question 2.c » pour U_Rom (déterminée en 2.b) ; « crêtes distantes de 6 div » (= amplitude crête-à-crête) ; « 6,68 ∝F ». [?] La ligne 1°a, « au point B », lue sur l'image : le GBF est entre B (haut) et A (bas).

### Exercices à résoudre (p.130–135) — réponses p.318 (colonne droite « Chapitre 4 »)

**Tests rapides des acquis (p.130)** — pas de réponse imprimée.
- **1 Items « vrai ou faux »** : **identiques à 223433** (8 items : oscillations forcées « libres » ; fréquence forcée = propre possible ; résonance d'intensité si u en phase avec i ; si impédance maximale ; Q augmente avec la résistance ; puissance moyenne du condensateur nulle ; résonance de puissance = résonance d'intensité ; diminuer le facteur de puissance pour minimiser les pertes Joule).
- **2 QCM** : I, II, IV, V **identiques à 223433** (I : a- impédance minimale ; b- fréquence imposée = propre ; c- impédance = résistance du résistor ; d- i et u en phase. II : a- quadrature avance sur u_C ; b- quadrature retard sur la bobine ; c- phase avec u_R ; d- phase avec u du RLC. IV : a- baisse de la fréquence de résonance ; b- baisse de l'amplitude maximale de i ; c- hausse de la puissance moyenne maximale. V : a- 2πLN₀/R ; b- U_L/U quel que soit N ; c- (1/R)√(C/L) [sic, √(C/L) et non √(L/C)] ; d- U_C/U à la résonance d'intensité). **III DIFFÉRENT** : « Dans un circuit RLC série alimenté par une tension sinusoïdale u de fréquence N réglable, l'intensité du courant oscille en retard de phase par rapport à u : a- quelle que soit la valeur de N ; b- pour N = No (fréquence propre de l'oscillateur) ; c- pour N > No. » (223433 : III = condition de résonance de charge, absente ici).

**Exercices d'application (p.131–134)**
- **3** (p.131) : circuit d'accord radio, N = 16233 Hz, L = 10⁻⁴ H ; valeur de C ? Réponse : **C = 9,5.10⁻⁷ F**. [?] contrôle : 1/(4π²N²L) = 9,6.10⁻⁷ F ; la réponse imprimée est donnée telle quelle (identique à 223433).
- **4** : C et bobine (L, r) en série, u(t) = 30√2 sinωt, ω = 2000 rad.s⁻¹ : I = 600 mA, U₁ (bobine) = 30 V, U₂ (condensateur) = 30 V ; i = Iₘsin(ωt + φ). 1°) Fresnel : φ, r, L, C ; 2°) comparer ω et ωo par leur quotient, sens de variation de ω pour la résonance d'intensité. (Pas de réponse.) — identique à 223433.
- **5** : C = 20 μF, R = 20 Ω, L = 0,55 H, r = 12,5 Ω ; u(t) = 100√2 sin2πNt, N = 48 Hz. 1°) Z sans démonstration, la calculer ; 2°) I en fonction de Z ; 3°) circuit équivalent à (R + r) : a) N = No, la calculer ; b) Zo et Io. Réponses : **2°) I = U/Z ; 3°a) N = 48 Hz ; 3°b) Z₀ = 32,5 Ω ; I₀ = 3,077 A**. — identique.
- **6** : R, L, C série, U efficace, ω réglable, ampèremètre. 1°) Fresnel : Z et déphasage en fonction de ω, R, L, C ; 2°) a) allure I = f(ω), phénomène ; b) ωo dépend-elle de R, L, C ? expression en fonction de deux des trois grandeurs ; c) Z et déphasage pour ω = ωo. Réponses : **2°a) Résonance d'intensité ; 2°b) ω₀ ne dépend que de L et de C ; 2°c) Z = R et Δφ = 0**. — identique.
- **7** : bobine (L, r), C = 0,5 μF, U = 2 V ; No = 2325 Hz, Io = 130 mA. 1°) caractéristiques de la bobine ; 2°) facteur de surtension et puissance moyenne maximale. Réponses : **1°) r = 15,4 Ω ; 2°) Q = 10,445 ; P = 0,26 W**. — identique. [?] contrôle : r = U/Io = 15,4 Ω et P = U·Io = 0,26 W sont cohérents ; en revanche 1/(rCω₀) donne ≈ 8,9 et non 10,445 : la valeur imprimée de Q est à re-résoudre, ne pas la reprendre sans contrôle (même réponse dans 223433).
- **8** (p.132) : portion MN : C et bobine (L, r) ; I = 0,20 A ; U_MN = 120 V, U_MP = 160 V, U_PN = 56 V (P : jonction bobine-condensateur). 1°) impédances de la bobine et du condensateur, r ; 2°) déphasage de u_MN par rapport à i ; 3°) ωo = 250 rad.s⁻¹ en phase : a) L et C ; b) ω et N ; c) puissance moyenne ; 4°) montrer que I = 0,20 A pour une deuxième pulsation ω' (à calculer) ; 5°) comparer les puissances à ω, ωo, ω'. (Pas de réponse.) — identique.
- **9** : R = 50 Ω, C = 1 μF, L réglable (résistance négligeable), u(t) = 10√2 sin(100πt). 1°) équation différentielle en i ; 2°) i(t) = Iₘsin(100πt + φ) : a) Lo pour la résonance d'intensité ; b) surtension aux bornes du condensateur ; 2°) [second « 2° », = 3° d'après la réponse] tension de rupture Uo = 100 V : L à ne pas dépasser. Réponses : **2°a) Lo = 1 H ; 2°b) Q = 6,28 > 1 ; 3°) L < 1,6 H**. — identique. [?] Contrôle : avec C = 1 μF et ω = 100π, Lo = 1/(Cω²) ≈ 10,1 H (pas 1 H) ; les réponses imprimées sont cohérentes avec C = 10 μF. Même énoncé et mêmes réponses dans 223433 : incohérence du manuel, à ne pas trancher ici.
- **10** : résistor, C, bobine purement inductive L ; R résistance totale ; u_AB = Uₘsinωt, U constante, ω réglable ; wattmètre. 1°) à ω = ωo, Po en fonction de U et R ; énergie Eo reçue pendant une période (U, R, ωo) ; 2°) à la résonance, E_t = E_L + E_C en fonction du temps, constante, en fonction de L, U, R ; que devient l'énergie reçue ? 3°) E_t/Eo en fonction de Q. Réponses : **1°) E₀ = 2πU²/ωoR ; 2°) E_t = LU²/R² ; 3°) E_t/E₀ = Q/2π**. — identique.
- **11** (p.133) : R = 300 Ω, C = 3 μF, bobine (L, r) ; u(t) sur Y1 (4 V/div), u_R(t) sur Y2 (2 V/div), 1 ms/div ; à N = No, deux sinusoïdes en phase. 1°) phénomène observé ; 2°) L et r. Réponse : **2°) L = 0,135 H ; r = 60 Ω**. Lecture de la figure (300 dpi) : T ≈ 4 div = 4 ms (No ≈ 250 Hz, d'où L = 1/(4π²No²C) ≈ 0,135 H), amplitudes ≈ 1,5 div (Y1, donc ≈ 6 V) et ≈ 2,5 div (Y2, flèche « voie Y2 » sur la plus grande, donc ≈ 5 V) ⇒ Uₘ/U_Rm = (R + r)/R = 1,2 ⇒ r = 60 Ω ✓. [?] valeurs en divisions = lectures graphiques ; dans 223433 la fiche signalait « Y2 de plus faible amplitude » : ici la plus grande courbe en divisions est Y2, la plus faible en volts.

**Exercices de synthèse (p.133–135)**
- **12** (p.133) : condensateur « EFD-CPM13B, Capacité 1,2 MF, Tolérence 10 %, Tension maximale 160 V » ; circuit : GBF U = 2 V, R = 10 Ω, bobine L = 58 mH (r), condensateur, voltmètre, ampèremètre. 1°) schéma (vérifier U = 2 V constante, mesurer I) ; 2°) à N = 610 Hz, I maximale = 96,7 mA : a) fréquence propre ; b) C, quelle indication à la place de « MF » ; c) valeur dans la tolérance ? (Pas de réponse.) — = ex.13 de 223433.
- **13** (p.133–134) : R = 40 Ω, C, bobine (L, r) ; u(t) = 10√2 sin(2πNt). 1°) à No : U_R = 9,6 V et u_C(t) = U_c√2 sin(318πt − π/2), U_c = 36 V : a) résonance d'intensité ; b) Io ; C, L, r ; Q ; c) montrer u_c² = −Q²u² + 2U_c² ; d) énergie totale en fonction de u et u_c, conservation. (Pas de réponse.) — = ex.14 de 223433.
- **14** (p.134) : U = 10 V, R = 100 Ω, C = 0,5 μF, bobine r = 100 Ω, L = 50 mH. 1°) N₁ = 318 Hz : a) Z₁ ; b) I₁ ; c) P₁ ; d) φ₁ de u par rapport à i, grandeur en avance, caractère (résistif, capacitif, inductif) ; 2°) diagramme de Fresnel à l'échelle ; 3°) N = No : a) que devient le diagramme ; b) Zo, Io, Po. (Pas de réponse.) — = ex.15 de 223433.
- **15** (p.134–135) : générateur 0–10 V, fréquence « de 5 à 5 kHz » [sic], ampèremètre, deux voltmètres, bobine (L, r), condensateur C, boîte de résistances 0–1,1 kΩ, oscilloscope bicourbe. 1°) schéma ; 2°) U = 5 V, tableau N (Hz) / I (mA) : 100/1,6 ; 200/3,4 ; 300/5,7 ; 400/8,9 ; 500/15,1 ; 600/27,6 ; 700/47,0 ; 800/31,5 ; 900/20,5 ; 1000/14,6 ; 1100/11,7 ; 1200/9,8 ; 1300/8,5 ; 1400/7,6 ; a) tracer I = f(N) (1 cm ↔ 100 Hz ; 1 cm ↔ 2,5 mA) ; b) No ; c) résistance totale ; 3°) a) branchements (u voie A, intensité voie B) ; b) à N = No, oscillogramme (voie A 2 V/div, voie B 1 V/div, 0,2 ms/div ; deux sinusoïdes en phase) : quelle courbe est celle de la voie A ; R réglable puis r ; c) U_C maximale = 21,5 V : C ; d) L. (Pas de réponse.) — = ex.16 de 223433. Figure (300 dpi) : deux sinusoïdes en phase d'amplitudes ≈ 1,5 div (courbe 1) et ≈ 2,5 div (courbe 2) ; [?] lectures graphiques ; la période lue (≈ 8 div = 1,6 ms) ne colle pas exactement avec le maximum du tableau (47 mA à 700 Hz, No un peu au-dessus), ne pas en tirer de valeur.
- **16 Étude de texte** (p.135) « Le facteur de puissance » : facteur de puissance = efficacité d'une installation à consommer la puissance ; mauvais facteur → pertes en ligne, capacité gaspillée ; tarification STEG incitant à un facteur très élevé ; « La puissance apparente que le réseau de la STEG fournit se décompose en une puissance active et une puissance réactive. » (active = équipements produisant de la chaleur ; réactive = création de champs magnétiques, moteurs, compresseurs) ; condensateurs montés dans l'installation pour réduire l'écart puissance moyenne / apparente. Questions : 1°) qu'est-ce qu'un mauvais facteur de puissance, qu'est-ce qui fait augmenter les pertes en ligne ; 2°) avantages d'un facteur de puissance élevé ; 3°) démontrer l'amélioration du facteur de puissance par insertion de condensateurs. (Pas de réponse.) — = ex.18 de 223433.

**Exercices absents de 223433 → présents seulement là** : ex.12 (courbes Qₘ(N), Iₘ(N), Nr, C, R : réponses « 4°a) courbe (2) ; No = 210 Hz ; Nr = 205 Hz ; C = 5,75 μF ; R = 40,5 Ω ») et ex.17 (R, C, L = 1 H, résonance de charge, chronogrammes, q(t)) **n'existent pas dans 223432**. La numérotation des exercices de synthèse décale donc de 1 (12 → 13 de 223433) puis de 2 (16 → 18).

**Fiche technique (p.136)** — « Construction de Fresnel » : identique à 223433 p.142 (somme de fonctions sinusoïdales isochrones yₖ = aₖsin(ωt + φₖ) ; vecteur de Fresnel OA⃗ de module a, origine O, tournant à ω dans le sens trigonométrique, angle φ avec (O, i⃗) à t = 0 ; projection sur (O, j⃗) = y ; yₖ ↦ OA⃗ₖ[aₖ, φₖ], y = Σyₖ ↦ OA⃗ = ΣOA⃗ₖ ⇒ OA⃗[a, φ] ; Fig.1–4). **En savoir plus (p.137)** — « Générateur de courant haute fréquence » : identique à 223433 p.143 (appareil vers 1895, bobine de Ruhmkorff, décharge oscillante des condensateurs, Tesla, d'Arsonval 1893, résonateur du docteur Oudin ; source www.patrimoine.polytechnique.fr). Culture, hors évaluation.

### Réponses imprimées (p.318, colonne « Chapitre 4 », vues sur image)
3. C = 9,5.10⁻⁷ F · 5. 2°) I = U/Z ; 3°a) N = 48 Hz ; 3°b) Z₀ = 32,5 Ω ; I₀ = 3,077 A · 6. 2°a) Résonance d'intensité ; 2°b) ω₀ ne dépend que de L et de C ; 2°c) Z = R et Δφ = 0 · 7. 1°) r = 15,4 Ω ; 2°) Q = 10,445 ; P = 0,26 W · 9. 2°a) Lo = 1 H ; 2°b) Q = 6,28 > 1 ; 3°) L < 1,6 H · 10. 1°) Eo = 2πU²/ωoR ; 2°) Et = LU²/R² ; 3°) Et/Eo = Q/2π · 11. 2°) L = 0,135 H ; r = 60 Ω. (Aucune réponse imprimée pour 1, 2, 4, 8, 12–16 ; les p.319–320 ne contiennent rien du chapitre 4 : réponses d'autres chapitres et sites Web.) Les réponses de 223433 aux ex.3, 5, 6, 7, 9, 10, 11 sont **mot pour mot les mêmes** ; celle de l'ex.12 de 223433 n'a pas d'équivalent.

### Écart avec Sciences expérimentales (223433)

**Ce que ce manuel RETIRE** (tout ce qui touche à la charge q et à la résonance de charge) :
- objectifs « résonance de charge », « équation différentielle en i(t) ou q(t) », « déduire Qₘ » ;
- 1.1 : second montage (u_C à l'oscilloscope), Fig.4/5 de 223433, questions 1°, 2°, 4°, 6° de 223433, Qₘ = Iₘ/2πN, équation différentielle **en q(t)**, la phrase « s'exprime en ohm (Ω) » ;
- 1.2.2 (déphasage i / q : φᵢ = φ_q + π/2, quadrature avance de i sur q) ;
- §2 : mesures de U_C, courbe Qₘ(N), N₂ de la résonance de charge, Qₘ = Iₘ/ω = Uₘ/√(R²ω² + (1/C − Lω²)²), φ_q = φᵢ − π/2 et −π < φ_q < 0, **résonance de charge** (g(ω), ω₁² = 1/LC − R²/2L², Nr = √(N₀² − R²/8π²L²) < No), conclusion théorique double ;
- §3 : courbes Qₘ, Q_mo, résonance « très floue » (R = 1000 Ω), « résonance impossible », « réponse linéaire », conclusion sur Nr ;
- L'essentiel : Qₘ, φ_q, résonance de charge ; ex. résolu : « ou bien en résonance de charge » et le calcul de Qₘ ;
- QCM III de 223433 (résonance de charge, N₀ > R/(2πL√2) etc.), **ex.12 et ex.17 de 223433** (Qₘ/Iₘ, Nr, résonance de charge) ; chapitre ramené de 34 à 28 pages.

**Ce que ce manuel AJOUTE** (absent de 223433) :
- **Fig.6b** : courbe de la phase initiale φ de i en fonction de N (§2), **Fig.8b** : φ(N) pour deux résistances (§3) ; question 1° de §2 « montrer que φ est égale au déphasage entre i et u » ; question 3°b « relever I_mo et φ₀ » ; question 2°b de §3 « déterminer graphiquement le déphasage φ à la résonance » ;
- **Remarque p.114** : le régime transitoire / la solution générale de l'équation différentielle est **hors programme** (explicite ici ; dans 223433 ce n'était qu'une absence) ;
- renvoi correct à la fiche technique (p.136), L'essentiel correct sur capacitif/inductif, et **QCM III** nouveau (i en retard de phase sur u : a- quel que soit N, b- N = No, c- N > No) ;
- §3 : jeu de résistances **Ro = 20 Ω et 200 Ω** (223433 : 50, 200, 1000 Ω) et seulement deux courbes (a)/(b) de phase.

**Identique à 223433** (relever seulement) : p.111 ; prérequis ; introduction ; montage Fig.1 et valeurs (C = 0,47 μF, L = 0,2 H, r = 12,5 Ω, 400 Hz, 2 V, 50 Ω) ; définition/exemples/questions/conclusion du déphasage ; construction de Fresnel (Iₘ, Z, tgφ, cosφ, inductif/capacitif) ; résonance d'intensité ; §4 surtension (tableau 40 / 21 / 6,5 V à No = 520 Hz) ; §5 applications ; §6 puissance (p(t), P = UIcosφ = RI², puissance apparente V.A, cosφ = R/Z, résonance de puissance, P = RU²/Z², Po = RoP²/(U²cos²φ), cosφ > 0,8) ; exercice résolu (mêmes valeurs numériques) ; tests V/F, QCM I/II/IV/V ; ex. 3 à 11 et leurs réponses ; ex. 12 à 15 (= 13 à 16 de 223433) ; étude de texte ; fiche technique ; en savoir plus.

### Bornes de scope (chapitre 4, section Mathématiques)

- ✅ **INCLUS** : distinction **excitateur (GBF) / résonateur (RLC série)** ; visualisation à l'oscilloscope bicourbe de u et u_Ro (choix de la masse : côté résistor), u_Ro image de i ; lecture d'oscillogrammes (période, fréquence, amplitude, décalage horaire, sensibilités ms/div et V/div) ; **fréquence imposée par l'excitateur** (oscillations forcées, non libres) ; **impédance** Z = Uₘ/Iₘ = U/I (Ω) ; **équation différentielle en i(t)** par la loi des mailles : L di/dt + (Ro + r)i + (1/C)∫i.dt = u (établie, non résolue ; seule la solution permanente i = Iₘsin(ωt + φ) est admise ; régime transitoire **hors programme**) ; **déphasage** Δφ, |Δφ| = (2π/T)Δt, concordance, opposition, quadrature avance/retard ; **construction de Fresnel** (trois cas Lω ≷ 1/Cω, circuit inductif / capacitif), Iₘ = Uₘ/√(R² + (Lω − 1/Cω)²), Z, tgφ = (1/Cω − Lω)/R avec −π/2 < φ < π/2, cosφ = R/Z ; **résonance d'intensité** (N = No = 1/(2π√LC), Z = R, I_mo = Uₘ/R, u et i en phase, circuit équivalent à un résistor R) ; courbes Iₘ(N) et φ(N) (Fig.6, 8) ; **influence de R** : résonance aiguë / floue, fréquence de résonance d'intensité indépendante de R ; **surtension** : Q = U_Cm/Uₘ = U_C/U = 1/((Ro + r)Cωo) = Lωo/(Ro + r) = (1/(Ro + r))√(L/C), dangers (claquage, étincelles, électrocution), surtension aux bornes de la bobine (U_Bobine = √(r² + (Lωo)²)I) ; **applications** (quartz, haut-parleur et microphone électrodynamique, radio ; hi-fi = résonance floue) ; **puissance instantanée** p(t) = UIcosφ − UIcos(2ωt + φ), Tp = T/2 ; **puissance moyenne** (définition, P = (1/Tp)∫p dt, P = UIcosφ = RI², W, wattmètre) ; **puissance apparente** UI (V.A) ; **facteur de puissance** cosφ = R/Z ; **résonance de puissance** ; P = RU²/Z² ; pertes en ligne Po = RoP²/(U²cos²φ), exigence cosφ > 0,8 (STEG) ; en exercices : bilan d'énergie E_L + E_C à la résonance, E_t/E₀ = Q/2π (ex.10), relation u_c² = −Q²u² + 2U_c² et conservation de l'énergie (ex.13), tracé point par point de I = f(N) (ex.15), diagramme de Fresnel à l'échelle (ex.14), tolérance d'un composant (ex.12), étude de texte sur le facteur de puissance (ex.16).
- ⛔ **EXCLU** (absent du chapitre) : **toute charge q(t) en régime forcé** : équation différentielle en q, Qₘ = Iₘ/ω, φ_q, **résonance de charge**, Nr, g(ω), « résonance impossible », « réponse linéaire », oscillogramme de u_C et mesure de Qₘ (u_C n'apparaît que dans l'exercice résolu, pour le déphasage π/2 et le facteur de surtension) ; **résolution** de l'équation différentielle et régime transitoire (hors programme, dit explicitement) ; **nombres complexes / impédance complexe / notation j** ; **bande passante**, fréquences de coupure, Q = No/ΔN ; **puissance réactive** (citée seulement dans le texte de l'ex.16, sans formule ni unité var) ; **compensation par condensateur** chiffrée (seulement « démontrer » qualitativement, ex.16, sans réponse) ; RLC **parallèle**, filtres ; régimes **non sinusoïdaux** (note marginale : « Le cas unique qui figure dans le programme est celui du régime sinusoïdal forcé ») ; **triphasé**, transformateur ; résonance **mécanique** (chapitre 5 : pendule élastique) ; réponses non imprimées (ne pas inventer de corrigé « officiel » pour les ex.1, 2, 4, 8, 12–16). Appareillage : GBF, oscilloscope bicourbe, ampèremètre, voltmètre, wattmètre, boîte de résistances ; pas d'ExAO.
- Attention auteur : un exercice de la section Sciences expérimentales qui parle de résonance de charge ou de Qₘ **ne doit pas être repris** pour la section Mathématiques sur la foi de la fiche 223433 ; la fiche de scope fait foi.

### Lecture

- **Couche texte** : p.110 à 138 (jusqu'à l'ouverture du chapitre 5, pour borner) et p.318–320, via `/root/.cache/yqa-manuels/223432/txt/pNNN.txt` ; comparaison mot à mot (couche texte) des p.127–136 avec 223433 p.132–142 (exercice résolu, tests, exercices), et par recherche de phrases pour le reste du cours.
- **Pages lues sur l'image** (110 dpi) : **29** — 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 318 ; zooms 200–300 dpi : p.115 (Fig.6a/6b), p.119 (Fig.8a/8b), p.133 (oscillogramme ex.11), p.135 (oscillogramme ex.15), recadrages de p.127 et p.128 (Fig.2/3 de l'ER, cadrage partiel, lues surtout à 110 dpi).
- **Sondage image** : toutes les pages du chapitre, dont les plus denses 117, 118, 123, 124, 126, 128, 129, 130. **Écarts texte/image** : p.110 « T = 2π/ω », √2 perdus ; p.113–118 ∫, fractions, φ, π, racines, tous les vecteurs de Fresnel perdus (« sin t ») ; p.118 « tg φ » sans φ ni π ; p.119 encadré N = No ⇔ { } rendu « "$ » ; p.121 √(L/C) ; p.122–123 √2, intégrales, bornes kTp/(k+1)Tp ; p.126 formules Iₘ et tgφ ; p.129 φ, π/3, π/2, « ∝F » ; p.130 QCM V (fractions, racines) ; p.131–134 « 30√2 », « 10√2 », « 318πt − π/2 ». Aucun écart non résolu après lecture image.
- **Doutes signalés [?]** : (1) p.114 : « figure 7 / 7a / 7b » pour les figures 5a/5b ; (2) p.113 : ligne « soit u_AM = … » imprimée deux fois ; (3) légende Fig.3 « Tracé de Uₘ en fonction de (U_Rom) » alors que U_Rom est en ordonnée (même coquille que 223433) ; (4) §3 : R02 = 20 Ω mais la courbe (1) de la Fig.8a coïncide avec la Fig.6a (Ro implicite 50 Ω) ; (5) ex.3 : 9,5 imprimé / 9,6.10⁻⁷ F au calcul ; (6) ex.7 : Q = 10,445 imprimé / ≈ 8,9 au calcul ; (7) ex.9 : Lo = 1 H imprimé / 10,1 H pour C = 1 μF (cohérent avec C = 10 μF) ; (8) ex.9 : deux « 2°) » (le second = 3°) ; (9) ex.15 : « de 5 à 5 kHz » ; (10) ex.12 : « 1,2 MF » (piège voulu par l'énoncé, question 2°b) ; (11) ER : « crêtes distantes de 6 div », renvoi à « question 2.c » au lieu de 2.b, « 6,68 ∝F » ; (12) ex.11 et 15 : amplitudes des oscillogrammes en divisions = lectures graphiques ; (13) valeurs lues sur Fig.3, 6a, 8a, 11 (≈ (4 V ; 0,6 V), 32 mA, ≈ 60 mW) non données par le texte ; (14) programme officiel non consulté ici : exigibilité au Bac Mathématiques de la **surtension aux bornes de la bobine** et du **transfert de puissance P(ω)** à confirmer (R-3) ; les contrôles de calcul marqués « non imprimé » sont de l'auteur de cette fiche, pas du manuel.

## 2.5 Chapitre 5 — Oscillations libres d'un pendule élastique (manuel 223432, p.138–161)

Partie « Evolution de systèmes » (bandeau courant de chaque page). **Résultat de la comparaison : le chapitre
est identique, mot pour mot, à celui du manuel Sciences expérimentales 223433 (p.144–167) ; seule la
pagination change (page 223432 = page 223433 − 6 ; réponses : 223432 p.318 = 223433 p.317).** Vérifié
par comparaison mot à mot automatique des 24 pages de couche texte (seuls écarts : glyphes dégradés
ω₀/π/φ/« − » rendus différemment par pdftotext, numéros de page) puis relecture des 24 pages sur image.
Section de référence transcrite et validée R-7 :
`content/programmes-officiels/programme/bac-sciences-exp/physique.md` § 2.5 (l. 2032-2433). Ci-dessous, la
correspondance page à page, puis tout ce qui doit rester verbatim (relu sur l'image de CE manuel).
Notation : ω₀ imprimé tantôt « ωo », tantôt « ω0 » ; T₀ tantôt « To », tantôt « T0 » (même grandeur).
Vecteurs fléchés (P⃗, R⃗, T⃗, f⃗, i⃗, a⃗) lus sur l'image.

**Objectifs (p.138, encadré)** — verbatim, identique à 223433 p.144 :
- « A l'aide d'un enregistrement graphique, reconnaitre le régime d'oscillations libres (amorties ou non
  amorties) d'un pendule élastique. »
- « Distinguer les régimes pseudopériodique, apériodique et critique des oscillations amorties. »
- « Etablir l'équation différentielle des oscillations libres d'un pendule élastique. »
- « Mesurer la période des oscillations d'un pendule élastique. »
- « Calculer l'énergie mécanique d'un pendule élastique en régime libre. »
- « Expliquer la conservation de l'énergie mécanique d'un oscillateur non amorti. »
- « Expliquer la diminution d'amplitude des oscillations libres amorties d'un pendule élastique par la
  non conservation de son énergie mécanique. »

**Prérequis (p.138)** — identique à 223433 p.144. SAVOIR : écrire l'expression de l'énergie cinétique ;
énumérer les facteurs dont dépend l'énergie potentielle élastique ; écrire l'équation horaire d'un
mouvement rectiligne sinusoïdal ; énoncer la loi de Hooke. SAVOIR FAIRE : délimiter un système matériel ;
distinguer les forces intérieures des forces extérieures à un système ; reconnaitre la période et la
fréquence d'un mouvement périodique ; calculer la pulsation d'un mouvement rectiligne sinusoïdal ;
appliquer la relation fondamentale de la dynamique à un solide en mouvement de translation ; « Ecrire la
solution générale de toute équation différentielle de la forme d²x/dt² + kx = 0, où k est une constante
positive » ; appliquer la loi de Hooke.

**Page d'ouverture (p.139)** — identique à 223433 p.145 : « 5 — OSCILLATIONS LIBRES D'UN PENDULE
ÉLASTIQUE » ; VTT tout suspendu (« Avec son amortissur à ressort, le VTT (Vélo Tout Terrain) TS (Tout
Suspendu) donne au cycliste un confort d'utilisation supérieur dans une compétition de descente d'une
montagne. ») ; gymnaste aux anneaux (« En évitant le balancement des anneaux, le gymnaste démontre tant sa
force que son équilibre. ») ; trois questions d'accroche identiques (geysers/cœur/balancier ; ronflement
des fils aériens ; tsunami).

**Définition liminaire (p.140)** — « On désigne par pendule élastique tout système constitué d'un solide (S)
de masse m attaché à un ressort à spires non jointives, de masse négligeable et de raideur k. » [coquilles
« sonstitué », « mase » corrigées]. « Dans le présent chapitre, on s'intéresse à l'évolution d'un tel système
mécanique au cours du temps. »

**Plan du chapitre** (pas de sommaire imprimé ; titres lus dans le corps) :
- **OSCILLATIONS LIBRES NON AMORTIES** (p.140–145) : 1 Mise en évidence · 2 Facteurs dont dépend la période
  (2.1 amplitude ; 2.2 masse du solide (S) ; 2.3 raideur du ressort ; 2.4 conclusion générale : expression
  de T₀) · 3 Etude théorique · 4 Energie d'un pendule élastique (4.1 cinétique ; 4.2 potentielle élastique ;
  4.3 mécanique et sa conservation ; 4.4 transformations mutuelles).
- **OSCILLATIONS LIBRES AMORTIES** (p.146–148) : 1 Etude expérimentale · 2 Etude théorique (2.1 équation
  différentielle ; 2.2 énergie mécanique et sa non conservation).
- **Analogie oscillateur mécanique / oscillateur électrique** (p.149, tableau).
- **L'essentiel** (p.150) · **Exercices** : exercice résolu (p.151–153) ; « Exercices à résoudre » : Tests
  rapides des acquis (1 vrai/faux, 2 QCM, p.154–155), Exercices d'application (3–5, p.155), Exercices de
  synthèse (6–12, p.155–158), 13 Etude de texte « Le tsunami » (p.159–160) · **En savoir plus** (p.161).
- Correspondance de pagination : 138↔144, 139↔145, 140↔146, 141↔147, 142↔148, 143↔149, 144↔150, 145↔151,
  146↔152, 147↔153, 148↔154, 149↔155, 150↔156, 151↔157, 152↔158, 153↔159, 154↔160, 155↔161, 156↔162,
  157↔163, 158↔164, 159↔165, 160↔166, 161↔167 (223432 ↔ 223433).

### Cours — Manipulations, questions, conclusions (identique à 223433 ; une ligne par bloc)

**I.1 Mise en évidence (p.140–141 ; = 223433 p.146–147)**
- **Manipulation** : pendule élastique horizontal sur banc à coussin d'air (Fig.1, photo « Oscillateur
  mécanique sur banc à coussin ») ; m = 0,1 kg ; k = 20 N.m⁻¹ ; (S) écarté de d = 2 cm de sa position
  d'équilibre dans la direction de l'axe du ressort, abandonné sans vitesse initiale. « Le solide (S)
  effectue des oscillations de part et d'autre de sa position d'équilibre (position de repos) : on dit que
  les oscillations sont libres. Le système {solide, ressort} constitue un oscillateur libre. »
  Remarque : enregistrement possible par un dispositif d'acquisition informatique.
- **Enregistrement (Fig.2, p.140)** : sinusoïde x(mm) entre +20 et −20, départ à x = +20 à t = 0 ; repère
  « 1,1 » (s) en pointillé sur le 3ᵉ minimum (2,5 oscillations en 1,1 s). [? légende imprimée erronée :
  « Fig.3 : Tracé de Um en fonction de f (URom) » — reprise d'un autre chapitre ; la figure est x(t).]
- **Questions** : 1°) a) mesurer les valeurs maximales et minimales de x, les comparer entre elles et à d ;
  b) mesurer les intervalles de temps séparant les maximums (ou minimums) successifs et les comparer ;
  2°) amorties ou non amorties, périodiques de période T₀ à préciser ; 3°) nature du mouvement de G.
- **Conclusion (encadré, p.141)** : « Les oscillations libres non amorties d'un pendule élastique sont
  rectilignes sinusoïdales. L'élongation s'écrit : x = Xm sin(2π t/T₀ + φ) » [forme imprimée
  x = Xₘ sin((2π/T₀)t + φ)]. Remarque : « Les valeurs de l'amplitude Xm et de la phase initiale φ dépendent
  des conditions initiales. »

**I.2 Facteurs dont dépend la période (p.141–143 ; = 223433 p.147–149)**
- **2.1 Amplitude** — même expérience pour différentes valeurs de d (Xm), chronomètre, durée Δt de dix
  oscillations. Tableau : Xm (cm) = 1 | 2 | 3 | 4 | 5 ; Δt (s) = 4,4 | 4,5 | 4,4 | 4,4 | 4,5 (identique).
  Remarque : réalisable avec un pendule vertical (Fig.3, schéma ressort vertical + masse ; la numérotation
  « Fig.3 » est imprimée deux fois dans le chapitre, p.140 et p.141). Questions : 1°) T₀ pour chaque Xm ;
  2°) comparer, isochronisme. **Conclusion** : « La période T₀ des oscillations libres non amorties d'un
  pendule élastique est indépendante de leur amplitude. »
- **2.2 Masse** — Tableau (identique) : m (kg) = 0,050 | 0,100 | 0,150 | 0,200 | 0,50 [? sic, vraisemblablement
  0,250] | 0,300 ; Δt = 10T₀ (s) = 3,2 | 4,4 | 5,4 | 6,3 | 7,0 | 7,7. Questions : 1°) T₀ non proportionnelle à
  m ; 2°) Fig.4 (droite T₀² (s²) = f(m) (kg) par l'origine, graduations 0,2/0,4/0,6 en ordonnée et 0,1/0,2/0,3
  en abscisse ; atteint ≈ 0,6 s² pour m = 0,3 kg, lu sur l'image) : T₀² proportionnelle à m, constante ;
  3°) relation T₀–m. **Conclusion** : « La période des oscillations libres non amorties d'un pendule
  élastique est proportionnelle à la racine carrée de la masse du solide (S). »
- **2.3 Raideur** — même solide, 100 g. Tableau (identique) : k (N.m⁻¹) = 10 | 20 | 30 | 40 | 50 ;
  Δt = 10T₀ (s) = 6,28 | 4,44 | 3,62 | 3,14 | 2,80. Questions : 1°) T₀ non inversement proportionnelle à k ;
  2°) Fig.5 (droite T₀² (10⁻² s²) = f(1/k) (10⁻² N⁻¹.m), par l'origine, ≈ 40 pour 1/k = 10 ; lu sur
  l'image) : T₀² proportionnelle à 1/k, constante ; 3°) relation T₀–k. **Conclusion** : « La période des
  oscillations libres non amorties d'un pendule élastique est inversement proportionnelle à la racine
  carrée de la raideur k du ressort. »
- **2.4 Conclusion générale (p.142–143)** — « La période d'un pendule élastique est indépendante de
  l'amplitude des oscillations, elle ne dépend que des grandeurs m et k caractéristiques du pendule, d'où sa
  qualification de période propre. Etant à la fois proportionnelle à √m et inversement proportionnelle à
  √k, la période propre d'un pendule élastique est alors proportionnelle à √(m/k), ce qui signifie
  T₀ = C√(m/k) où C est une constante dont la valeur 2π peut être déduite des résultats obtenus
  précédemment. D'où : **T₀ = 2π√(m/k)** ».

**I.3 Etude théorique (p.143 ; = 223433 p.149)**
- Forces extérieures sur (S) dans un repère lié au laboratoire : poids P⃗, réaction R⃗ du coussin d'air,
  tension T⃗ du ressort (Fig.6 : ressort horizontal, solide (C)/G, axe x′x d'origine O, vecteur i⃗).
- **Questions** : 1°) a) montrer que T⃗ = −kx·i⃗ ; b) justifier la qualification de force de rappel ;
  2°) RFD : d²x/dt² + ω₀²x = 0 avec ω₀² = k/m ; 3°) vérifier la solution générale x = Xm sin(ω₀t + φ) ;
  4°) T₀ théorique = T₀ expérimentale.
- **Conclusion (encadré)** : « Etant sinusoïdales, les oscillations libres non amorties d'un pendule
  élastique sont régies par l'équation différentielle : **d²x/dt² + ω₀²x = 0 avec ω₀² = k/m**. »

**I.4 Energie d'un pendule élastique (p.144–145 ; = 223433 p.150–151)**
- « L'énergie mécanique E du système {solide (S) + ressort} est la somme de l'énergie cinétique Ec due au
  mouvement du solide (S) et de l'énergie potentielle élastique Ep due à la déformation du ressort :
  E = Ec + Ep. »
- **4.1 Cinétique** : Ec = ½mv² ; « or, v = dx/dt = Xmω₀ cos(ω₀t + φ) d'où : Ec = ½ m Xm² ω₀² cos²(ω₀t + φ) » ;
  « Compte tenu de ω₀²m = k, il vient : **Ec = ½kXm² cos²(ω₀t + φ) = ¼kXm²[1 + cos 2(ω₀t + φ)]** » ;
  « Donc, les variations de l'énergie cinétique en fonction du temps sont périodiques de période T₀/2
  (Fig.7, cas où φ = 0) » (Fig.7 : Ec(t), maximum ½kXm² à t = 0, T₀/2, T₀).
- **4.2 Potentielle élastique** : « On a vu en deuxième année que l'énergie potentielle élastique d'un système
  matériel déformable dépend de ses caractéristiques. Pour un pendule élastique, étant une fonction de la
  raideur k du ressort et de sa déformation Δl, elle s'écrit sous la forme : » encadré **Ep = ½kΔl²**.
  Questions : 1°) Ep = ¼kXm²[1 − cos 2(ω₀t + φ)] ; 2°) courbe Ep = f(t), période T₀/2.
- **4.3 Mécanique et conservation** : E = Ec + Ep ; « E = ½kXm²[cos²(ω₀t + φ) + sin²(ω₀t + φ)]. Or,
  cos²(ω₀t + φ) + sin²(ω₀t + φ) = 1. Il vient donc : **E = ½kXm² = ½mVm²**. Ainsi,
  **E = ½mv²(t) + ½kx²(t) = cte, ∀ t**. » **Conclusion (p.145)** : « En régime libre non amorti, l'énergie
  mécanique d'un pendule élastique horizontal est constante. Par suite, un tel système est dit
  conservatif. »
- **4.4 Transformations mutuelles Ec ↔ Ep (p.145)** : passage par x = 0 avec v = ± Vm, rebroussement quand
  v = 0 et x = ± Xm ; question « Interpréter énergétiquement ces propriétés oscillatoires. » ; interprétation
  identique (x = Xm : énergie purement potentielle ; vers la position de repos Ep diminue aux dépens de Ec ;
  en x = −Xm, Ec nulle, Ep maximale, (S) rebrousse chemin). Fig.8 : E horizontale, Ep parabole de sommet en
  0, Ec parabole renversée, x de −Xm à Xm ; « l'énergie cinétique et l'énergie potentielle dont la somme est
  constante varient toujours en sens inverses ». **Conclusion** : « Les oscillations libres non amorties
  d'un pendule élastique sont auto-entretenues par les transformations mutuelles de ses énergies cinétique
  et potentielle. »

**II. Oscillations libres amorties (p.146–148 ; = 223433 p.152–154)**
- Introduction : l'amplitude diminue « à cause des facteurs dissipatifs inévitables (essentiellement les
  frottements) » ; même sur table à coussin d'air les oscillations prennent fin ; « De telles oscillations
  sont dites amorties. »
- **II.1 Etude expérimentale — Manipulation** : dispositif de la Fig.1 + palette fixée sur le solide
  perpendiculairement au déplacement, dans l'air puis dans l'eau. Chronogrammes Fig.9 (air ; repère « 1,8 s »)
  et Fig.10 (eau ; repère « 2 s »). [Lu sur l'image : chaque repère couvre 4 pseudopériodes, soit T₁ ≈ 0,45 s,
  T₂ ≈ 0,5 s — valeurs non imprimées, déduites des figures.] **Questions** (identiques) : 1°) a) évolution de
  l'amplitude, plus amorties dans l'eau que dans l'air ; b) maximums à intervalles égaux T₁ (air), T₂ (eau),
  à calculer ; 2°) comparer T₁, T₂ entre eux et avec T₀ ; 3°) « comme celles d'un circuit RLC série », les
  oscillations libres amorties sont pseudopériodiques. **Interprétation** : « Le passage du solide par la
  position d'équilibre est toujours périodique, mais le mouvement oscillatoire n'est plus périodique à cause
  de la diminution de l'amplitude. Le mouvement est dit pseudopériodique. »
- **Définitions (p.147)** : « On appelle pseudopériode la durée T qui sépare deux passages successifs du
  solide par la même position et dans le même sens. » ; « La valeur de la pseudopériode T (T₁ ou T₂) est
  voisine de celle de la période propre T₀ des oscillations : T est légèrement supérieure à T₀. » ;
  palette totalement immergée ou liquide plus visqueux (huile) : « le mouvement cesse d'être oscillatoire à
  partir d'une certaine valeur de l'amortissement : on dit qu'il est apériodique (Fig.11) » (Fig.11 : x(t)
  décroît sans osciller vers 0) ; « Pour un amortissement particulier, l'oscillateur retourne à sa position
  d'équilibre, sans osciller, en un minimum de temps : un tel régime est dit apériodique critique. »
  **Conclusion** : « Selon l'importance de l'amortissement, les oscillations d'un pendule élastique sont :
  – faiblement amorties, le régime est pseudopériodique. – fortement amorties, le régime est apériodique. »
- **II.2.1 Equation différentielle (p.147)** : forces (Fig.12) : poids P⃗, réaction R⃗, tension T⃗ = −k x i⃗
  (force de rappel), frottements « supposés de type visqueux, équivalentes à une force f⃗ de sens contraire
  au vecteur vitesse et de la forme : **f⃗ = −hv⃗**, où h est une constante positive, ne dépendant que de la
  nature du liquide visqueux, appelée coefficient de frottement. » Deuxième loi de Newton :
  P⃗ + R⃗ + T⃗ + f⃗ = ma⃗ ; projection sur x′x : −kx − h dx/dt = m d²x/dt² ; « il vient finalement :
  **m d²x/dt² + h dx/dt + kx = 0** ou encore : **d²x/dt² + (h/m) dx/dt + (k/m) x = 0 (1)** ». « Cette équation
  différentielle admet des solutions qui dépendent de la valeur de h et qui donnent les régimes mis en
  évidence expérimentalement. » (aucune solution explicite).
- **II.2.2 Energie mécanique et non conservation (p.148)** : E = ½mv² + ½kx² ; dE/dt = mv dv/dt + kx dx/dt ;
  dE/dt = (dx/dt)[m d²x/dt² + kx] ; d'après (1), m d²x/dt² + kx = −h dx/dt, d'où
  **dE/dt = −h(dx/dt)² = −hv²**, « h est une constante positive » ; dE/dt < 0 : l'énergie diminue, dissipée
  « sous forme d'énergie thermique », ce qui « ne permet pas des transformations mutuelles intégrales
  d'énergie cinétique et d'énergie potentielle », d'où la diminution de l'amplitude. **Conclusion (encadré)** :
  « Le pendule élastique soumis à des forces de frottement n'est pas conservatif. Dans le cas de frottements
  visqueux, la diminution d'énergie mécanique d'un pendule élastique est telle que : dE/dt = −hv², où h est le
  coefficient de frottement. La diminution d'énergie due aux frottements est elle-même la cause
  d'amortissement des oscillations libres. »

### Tableau — Analogie oscillateur mécanique / oscillateur électrique (p.149, lu sur l'image ; identique à 223433 p.155)

| | pendule élastique | circuit RLC série |
|---|---|---|
| Coefficient d'inertie | masse m | inductance L (imprimé « indulance ») |
| Coefficient de rappel | raideur k (imprimé « raideur » ; image : « raideur k ») | inverse de la capacité 1/C |
| Facteur dissipatif | coefficient de frottement h | résistance R |
| Grandeurs oscillantes | élongation x ; vitesse v = dx/dt | charge q ; intensité i = dq/dt |
| Éq. diff. amorties | d²x/dt² + (h/m)dx/dt + (k/m)x = 0 | d²q/dt² + (R/L)dq/dt + (1/LC)q = 0 |
| Éq. diff. non amorties | d²x/dt² + ω₀²x = 0 avec ω₀² = k/m | d²q/dt² + ω₀²q = 0 avec ω₀² = 1/LC |
| Période propre | T₀ = 2π√(m/k) | T₀ = 2π√(LC) |
| Équation horaire (non amorties) | x = Xm sin(ω₀t + φx) ou v = Vm sin(ω₀t + φv) | q = Qm sin(ω₀t + φq) ou i = Im sin(ω₀t + φi) |
| Énergies (formes générales) | potentielle élastique ½kx² ; cinétique ½mv² ; mécanique E = ½kx² + ½mv² | électrostatique ½q²/C ; magnétique ½Li² ; totale E = ½q²/C + ½Li² |
| Non amorti : se conserve | E = ½kXm² = ½mVm² = cte | E = ½Qm²/C = ½LIm² = cte |
| Amorti : diminue | dE/dt = −hv² < 0 | dE/dt = −Ri² < 0 |

### Encadrés, définitions, lois et relations (verbatim, vérifiés sur l'image de 223432)

- Pendule élastique : solide (S) de masse m + ressort à spires non jointives, de masse négligeable, de
  raideur k (p.140).
- x = Xm sin(2πt/T₀ + φ) ; Xm et φ dépendent des conditions initiales (p.141).
- T₀ indépendante de l'amplitude ; proportionnelle à √m ; inversement proportionnelle à √k ; « période
  propre » ; **T₀ = 2π√(m/k)** (p.141–143).
- T⃗ = −kx·i⃗ (force de rappel) (p.143) ; **d²x/dt² + ω₀²x = 0 avec ω₀² = k/m** ; solution générale
  x = Xm sin(ω₀t + φ) (p.143).
- Ec = ½mv² = ½kXm² cos²(ω₀t + φ) = ¼kXm²[1 + cos 2(ω₀t + φ)], période T₀/2 ; Ep = ½kΔl² (encadré) ;
  Ep = ¼kXm²[1 − cos 2(ω₀t + φ)], période T₀/2 ; E = ½kXm² = ½mVm² ; E = ½mv²(t) + ½kx²(t) = cte ∀t ;
  système conservatif (p.144–145).
- Oscillations auto-entretenues par les transformations mutuelles Ec ↔ Ep (p.145).
- Pseudopériode (définition) ; T légèrement supérieure à T₀ ; régimes pseudopériodique / apériodique /
  apériodique critique (p.146–147).
- f⃗ = −hv⃗ ; m d²x/dt² + h dx/dt + kx = 0 ⇔ d²x/dt² + (h/m)dx/dt + (k/m)x = 0 (p.147).
- dE/dt = −hv² < 0 ; non conservatif (p.148).

### L'essentiel (p.150) — verbatim (identique à 223433 p.156)

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
  – apériodique (amortissement important). » [sic : le terme en x est écrit ω₀²x, non (k/m)x.]
- « Les oscillations libres amorties d'un pendule élastique sont pseudopériodiques ; leur pseudopériode T
  est légèrement supérieure à la période propre de l'oscillateur : l'écart (T – T₀) est d'autant plus
  remarquable que l'amortissement est plus important. »
- « La diminution d'énergie due aux frottements rend les oscillations libres du pendule élastique
  amorties. »

### Exercice résolu (p.151–153 ; identique à 223433 p.157–159)

**Énoncé** : ressort à spires non jointives, masse négligeable, k = 10 N.m⁻¹, enfilé sur une tige
horizontale ; cylindre creux (C), m = 100 g, coulisse sans frottement ; abscisse x de G repérée par rapport
à O (position d'équilibre) (Fig.1 : (R), (C), (T), axe x′x, i⃗). Écarté de x₀ = 2 cm, abandonné à t₀ = 0.
1°) sans vitesse initiale : a) par le théorème du centre d'inertie, oscillations sinusoïdales de pulsation
propre ω₀ à calculer ; b) par dE/dt, système conservatif ; c) E en fonction de k et x₀, Xm1 = x₀ ;
d) équation horaire. 2°) avec v₀ = 0,2 m.s⁻¹ : a) qu'est-ce qui change (qualitatif) ; b) avec
x(t) = Xm2 sin(ω₀t + φ₂), Xm2, φ₂, Vm2 ; c) E₀₂ à t₀ = 0 ; d) retrouver énergétiquement Xm2 et Vm2.
3°) comparer les énergies mécaniques des deux expériences.
**Solution** (valeurs relevées sur l'image) :
- 1°) a) P⃗ + T⃗ + R⃗ = ma⃗ ; −kx = ma = m d²x/dt² ⇒ d²x/dt² + ω₀²x = 0 (1), ω₀² = k/m ; ω₀ = √(k/m) ;
  **ω₀ = 10 rad.s⁻¹**. b) E = ½mv² + ½kx² ; dE/dt = kx dx/dt + mv dv/dt = v[kx + m d²x/dt²] = 0 d'après (1) ⇒
  conservatif. c) E₁ = E₀₁ = ½kx₀² = ½kXm1² ⇒ **Xm1 = x₀**. d) sin φ₁ = 1, φ₁ = π/2 rad ;
  **x(t) = 0,02 sin(10t + π/2)**.
- 2°) a) E₀₂ > E₀₁ ⇒ Xm2 > Xm1 = x₀. b) v(t) = Xm2ω₀ cos(ω₀t + φ₂) ; x₀ = Xm2 sin φ₂ (1), v₀ = Xm2ω₀ cos φ₂
  (2) ; (1)/(2) : tgφ₂ = x₀ω₀/v₀ = 1 ⇒ φ₂ = π/4 ou 3π/4 ; cos φ₂ > 0 ⇒ **φ₂ = π/4 rad** ;
  Xm2 = x₀/sin φ₂ ≈ **2,83.10⁻² m** ; Vm2 = Xm2ω₀ = **0,283 m.s⁻¹**. c) E₀₂ = ½mv₀² + ½kx₀² = **4.10⁻³ J**.
  d) E₂ = ½kXm2² = E₀₂ ⇒ Xm2 = √(2E₀₂/k) ≈ 2,83.10⁻² m ; E₀₂ = ½mVm2² ⇒ Vm2 = √(2E₀₂/m) = 2√2.10⁻¹ m.s⁻¹.
- 3°) E ∝ Xm² : E₂/E₁ = Xm2²/Xm1² > 1 ⇒ E₂ > E₁. Remarque : E₂/E₁ = E₀₂/E₀₁ = 1 + (1/ω₀²)(v₀/x₀)² > 1.

### Exercices à résoudre (p.154–160) — réponses du manuel p.318 (chapitre 5 seulement sur p.318 ; p.319–320 = chap.6–11 et sites web, rien sur le chap.5)

Tout est identique à 223433 p.160–166 ; aucun énoncé, aucune donnée, aucune réponse ne change.

**Tests rapides des acquis (p.154–155)**
- **1 Items vrai ou faux** (7 items, sans réponse imprimée) : 1. au passage par l'équilibre v = Xmω₀ ;
  2. éq. diff. d²x/dt² − ω₀²x = 0 [signe moins lu sur l'image] ; 3. oscillations non amorties dans l'air ;
  4. Ec max = ½kXm² ; 5. v(t) toujours en quadrature avance sur x(t) ; 6. les frottements influent sur
  l'amplitude ; 7. la pseudopériode augmente avec l'amortissement.
- **2 QCM** (9 questions, sans réponse imprimée) : 1. T₀ : dépend de Xm / proportionnelle à m / ne dépend
  pas des conditions initiales / temps entre deux passages successifs par l'équilibre ; 2. amplitude des
  oscillations non amorties : dépend de la vitesse initiale / ne dépend que de l'écart initial / augmente ;
  3. diminution d'amplitude due : aux transformations mutuelles / aux frottements / uniquement à la
  dissipation de Ec ; 4. vitesse au passage par l'équilibre : toujours maximale / toujours nulle / maximale
  ou minimale ; 5. k = 40 N.m⁻¹, m = 100 g : T₀ = 0,62 s / 3,10 s / 0,31 s ; 6. éq. diff. sans frottement :
  d²x/dt² + (m/k)x = 0 / d²x/dt² + (k/m)x = 0 / d²x/dt² + √(k/m) x = 0 ; 7. oscillations amorties :
  pseudopériode croissante / égale à T₀ / amplitude qui diminue en raison des frottements ; 8. régime
  pseudopériodique lorsque : amortissement faible / abandon avec vitesse initiale / amplitude constante ;
  9. amplitudes 4 cm puis 3,8 cm : amplitude constante / oscillations amorties / périodiques.

**Exercices d'application (p.155)**
- **3** — pendule horizontal, m = 300 g, k = 10 N.m⁻¹, lancé depuis l'équilibre à t = 0 avec v₀ = 0,2 m.s⁻¹
  sens positif ; x(t) = Xm sin(ω₀t + φ) : Xm, ω₀, φ. Réponse p.318 : **3.46 cm, 5.77 rad.s⁻¹, 0 rad**.
- **4** — m = 0,1 kg, k = 10 N.m⁻¹, banc à coussin d'air ; allongement 2 cm, abandon sans vitesse à t₀.
  1) éq. diff. ; 2) période ; 3) x(t). Réponse p.318 : **2°) 0.628 s**.
- **5** — k = 25 N.m⁻¹, m = 0,5 kg, écart 2 cm, non amorti. 1) période propre ; 2) vitesse au passage par
  l'équilibre ; 3) évolution de l'amplitude si amorti. Réponse p.318 : **1°) 0.89 s, 2°) 0.14 m.s⁻¹, 3°) Xm diminue**.

**Exercices de synthèse (p.155–158)**
- **6** (« D'après Bac. Juin 2005 (section sport) ») — corps (C) M = 0,2 kg, ressort k = 20 N.m⁻¹, tige
  horizontale (Fig.1) ; x = 0,1 sin(ω₀t + φ), ω₀ = √(k/M). 1°) a) T₀ ; b) N₀. 2°) frottements visqueux, Fig.2
  (zoom r250 : x(m) départ 0,10, 1ᵉʳ maximum 0,06 ; graduations t « 0,8 ; 0,16 ; 0,24 ; 0,32 ») : a) T
  graphique, comparer à T₀ ; b) E₀ et E₁ à t₀ = 0 et t₁ = T ; c) comparer. Réponse p.318 : **1°) a) 0.628 s,
  b) 1.59 Hz ; 2°) a) 0.8 s, T > T₀ ; b) E₀ = 0.1 J, E₁ = 0.036 J**. [? graduations incohérentes avec la
  réponse : « 0,8 » puis 0,16, 0,24, 0,32 se lit 0,08 s, la réponse donne T = 0,8 s ; coquille d'impression
  d'un « 0,08 » probable ; fidèle à la réponse imprimée.]
- **7** — d = 2 cm, abandon sans vitesse. 1°) sans frottement : nature des oscillations ; 2°) m = 360 g,
  T₀ = 0,60 s : raideur ; 3°) vitesse maximale au passage par la position de repos. (Pas de réponse.)
- **8** — enregistrements x(t) pour trois amortissements (courbe 1 et courbe 2 sans oscillation, partant de
  0,04 m, la courbe 1 décroissant plus lentement ; courbe 3 oscillante, maxima ≈ 0,03 / 0,02 / ≈ 0,012 / 0,01 m
  vers t = 1, 2, 3, 4 s). 1°) pseudopériodiques / apériodiques ; 2°) comment obtenir un régime apériodique à
  partir d'un régime pseudopériodique ; 3°) régime critique = « retour le moins lent à l'état de repos » :
  identifier la courbe. (Pas de réponse.)
- **9** — ressort l₀ = 10 cm, allongement/raccourcissement maximal 8,5 cm. 1°) vertical, m = 0,1 kg,
  l = 15 cm : raideur k ; 2°) sur banc à coussin d'air : pulsation, période, fréquence ; 3°) x₀ = 5,5 cm,
  expression de x(t) si a) abandon sans vitesse à t = 0 ; b) lâché sans vitesse et premier passage par
  l'équilibre à t = 0 ; c) lancé à t = 0 vers les élongations croissantes avec une vitesse telle qu'il subit
  ensuite son raccourcissement maximal. (Pas de réponse ; g non donné [?].)
- **10** — m = 292 g, k = 8 N.m⁻¹, tige horizontale sans frottement. 1°) éq. diff. ; 2°) expression littérale
  de T₀ ; Fig.1 x(mm)(t) : a) Xm, T₀ graphiquement, puis φ ; b) accord de T₀ avec m et k ; 3°) Fig.2 a = f(x)
  (droite décroissante par l'origine, a (m.s⁻²) de −0,8 à 0,8, x (mm) de −20 à 20) : a) accord avec l'éq.
  diff. ; b) expression littérale du coefficient directeur, accord avec l'expérience. (Pas de réponse.)
  [? Fig.1 : graduations verticales « 20, 10, 0, −20, −40 » asymétriques ; la courbe part du maximum (20) à
  t = 0, ses minima tombent sur la ligne « −40 » ; maxima ≈ 1,25 ; ≈ 2,5 s ; amplitude réelle ambiguë.]
- **11** (« D'après Bac. juin 2004 ») — ressort vertical k = 12 N.m⁻¹, solide M = 0,304 kg dans un liquide
  visqueux, f⃗ = −hv⃗ ; stylet en A, cylindre enregistreur tournant (moteur) (Fig.1 ; enregistrement n°1 : x
  de 0,04 à −0,04 m, repères T, 2T, 3T). 1°) enregistrement n°1, hₐ = 0,2 N.s.m⁻¹, G écarté de 4 cm vers le
  bas, libéré sans vitesse ; T ≈ T₀ : a) calculer T ; b) durée d'un tour du cylindre (le diagramme n°1 =
  un seul tour). 2°) h_b = 1, h_c = 4, h_d = 6 N.s.m⁻¹ → enregistrements n°2 (oscillant), n°3 et n°4 (non
  oscillants) (Fig.2) : remplir le tableau h / nature (pseudopériodique ou apériodique). (Pas de réponse.)
  [? formule imprimée « T ≈ T₀ = 2 √(M/k) » : π absent à l'impression.]
- **12** — graphe E (10⁻⁴ J) en fonction de x (cm) : Em horizontale à 2, Ep parabole de sommet 0 coupant Em
  en x = ±2 cm. 1°) variation de E, sa valeur, amorti ou non ; 2°) domaine d'élongation ; 3°) justifier la
  forme de Ep. (Pas de réponse.)
- **13 Etude de texte « Le tsunami »** (p.159–160) — séisme de Sumatra du 26 décembre 2004 ; oscillations de
  la Terre de fréquence pouvant atteindre 3 mHz, les plus graves entre 0,3 et 3 mHz ; en plein océan,
  oscillations horizontales de périodes de 10 min (1 km d'eau) à plus de 60 min (6 km d'eau au minimum) ;
  près des côtes la période diminue et l'amplitude augmente ; vague classique de période d'au plus une
  minute ; élévation du niveau pendant 5 à 30 minutes. Questions : 1°) les trois types d'oscillations libres ;
  2°) a) ce qui montre que les oscillations de la Terre sont libres ; b) périodes minimale et maximale ;
  c) qualification de ces périodes ; 3°) ce qui montre que le tsunami est oscillatoire ; 4°) justifier la
  durée de 5 à 30 min. (Pas de réponse.) Photo d'une vague p.159.

**En savoir plus (p.161)** — « Les oscillations libres de la Terre » (d'après M. Van camp) : modes normaux
(fondamental, harmoniques) excités par les grands séismes ; périodes de quelques secondes à 54 min ;
période 20.5 min ↔ 0.001 Hz ; comparaison au « Do 256 Hertz » (18 octaves, clavier de piano : 8) et à une
corde de guitare de 300 km ; stylo qui tombe (197 Hz ; harmoniques 211, 217, 219, 287, 311 Hz) ; forces de
rappel dues à l'élasticité. Pas de fiche technique dans ce chapitre.

### Écart avec Sciences expérimentales (223433)

- **Notions, activités, exercices ajoutés par 223432 : aucun.**
- **Notions, activités, exercices retirés par 223432 : aucun.**
- **Valeurs, énoncés, réponses modifiés : aucun.** Mêmes tableaux (Δt, m, k), mêmes figures (relevées sur
  l'image : Fig.4 ≈ 0,6 s² à 0,3 kg, Fig.5 ≈ 40.10⁻² s² à 10.10⁻² N⁻¹.m, Fig.9–10 repères 1,8 s et 2 s,
  ex.6/8/10/12), même exercice résolu (ω₀ = 10 rad.s⁻¹, φ₁ = π/2, φ₂ = π/4, Xm2 ≈ 2,83.10⁻² m,
  Vm2 = 0,283 m.s⁻¹, E₀₂ = 4.10⁻³ J), mêmes 13 exercices (2 séries de tests rapides + 3 d'application + 7 de synthèse + 1 étude de texte),
  mêmes réponses (3 : 3.46 cm, 5.77 rad.s⁻¹, 0 rad ; 4 : 0.628 s ; 5 : 0.89 s, 0.14 m.s⁻¹, Xm diminue ;
  6 : 0.628 s, 1.59 Hz, 0.8 s, E₀ = 0.1 J, E₁ = 0.036 J), mêmes coquilles (légende « Fig.3 : Tracé de Um… »
  p.140, masse « 0,50 » p.141, T₀ sans π dans l'ex.11, « indulance » p.149, « Fig.3 » en double).
- **Seule différence : la pagination** (−6 pages ; réponses p.318 au lieu de p.317) ; même bandeau courant
  « Evolution de systèmes ». Le chapitre n'est pas adapté à la section Mathématiques : pas de
  complément mathématisé (pas de résolution de l'équation amortie, pas de Fresnel, pas de pendule vertical
  traité, pas d'oscillations forcées).
- Conséquence pour la génération : **la section physique/bac-math chap.5 peut reprendre telle quelle les
  objectifs, notions, exercices et bornes de la section Sciences expérimentales ; le manuel Mathématiques
  n'y ajoute rien et n'y retire rien.**

### Bornes de scope (section Mathématiques)

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
- Analogie mécanique ↔ électrique (tableau p.149, RLC série du chapitre 3).

⛔ **Exclu** (absent du chapitre)
- Résolution de l'équation amortie (aucune solution explicite, ni forme exponentielle, ni décrément
  logarithmique, ni facteur de qualité, ni valeur critique de h, ni relation T–T₀ chiffrée).
- Frottements solides (non visqueux) ; pendule pesant / pendule simple ; pendule de torsion.
- Équilibre et équation du pendule élastique vertical (position d'équilibre décalée, poids) — non traités
  en cours (l'ex.9 1°) utilise seulement l'allongement statique).
- Oscillations forcées, résonance (chapitre suivant) ; entretien des oscillations.
- Représentation de Fresnel (le manuel écrit l'élongation sous la seule forme x = Xm sin(ω₀t + φ)).
- Énergie potentielle de pesanteur dans E.
- Tout contenu « renforcé » propre à la section Mathématiques : il n'y en a aucun dans ce chapitre.

### Lecture

- **Couche texte** : p.138–161 (24 pages) lues en entier et comparées mot à mot, page à page, à 223433
  p.144–167 (script de comparaison : ratio de similarité 0,94 à 0,998 par page ; tous les écarts sont des
  glyphes dégradés — ω₀ rendu « o »/« to », π, φ, « − » rendu « < » ou perdu, fractions, symboles
  mathématiques — et les numéros de page) ; réponses : p.318 (Chapitre 5 sur p.318 ; p.317 = fin du
  chapitre Physique nucléaire, p.319–320 = chap.6–11 et sites web, rien pour le chap.5).
- **Pages vues sur l'image** (r110) : 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151,
  152, 153, 154, 155, 156, 157, 158, 159, 160, 161 (24/24) ; p.318 (r110 puis zoom r250 du bloc Chapitre 5) ;
  zoom r250 : p.156 (Fig.2 de l'ex.6). Total : **25 pages distinctes vues sur l'image** (sondage 100 % ≥ 1/10 ;
  y compris les plus denses : 143, 144, 148, 149, 152, 153).
- **Écarts texte/image constatés** : ω₀ rendu « o » ; π absent ; φ perdu (« sin(2/To t+) ») ; signe « − »
  rendu « < » ou perdu (p.147–148 : « kx h … », « = hv² ») ; fractions éclatées ; vecteurs perdus
  (« T = - kx. i », P⃗ + R⃗ + T⃗ + f⃗ = ma⃗ absents p.147 et p.152) ; Ep = ½kΔl² rendu « kl2 » ; graphiques
  et graduations absents du texte (Fig.2, 4, 5, 7–12 ; figures des ex.6, 8, 10, 11, 12) ; tableau p.149
  éclaté sur plusieurs lignes ; ordre des colonnes mélangé p.155–158 (questions 1)–3) de l'ex.4 placées dans
  la colonne de droite).
- **Doutes [?]** (tous hérités à l'identique de 223433, aucun nouveau) :
  1. p.140 : légende de la Fig.2 imprimée « Fig.3 : Tracé de Um en fonction de f (URom) » ; T₀ ≈ 0,44 s
     seulement déductible de la figure (1,1 s = 2,5 oscillations), non imprimé.
  2. p.141 : masse « 0,50 » kg dans la série 0,050…0,300 (vraisemblablement 0,250).
  3. p.146 : T₁ ≈ 0,45 s et T₂ ≈ 0,5 s déduits des repères 1,8 s et 2 s (4 pseudopériodes chacun), non imprimés.
  4. p.156 ex.6 Fig.2 : graduation « 0,8 » puis 0,16, 0,24, 0,32 ; la réponse p.318 donne T = 0,8 s (> T₀ =
     0,628 s) — incohérence d'échelle.
  5. p.157 ex.10 Fig.1 : graduations verticales 20, 10, 0, −20, −40 incohérentes (amplitude ambiguë).
  6. p.158 ex.11 : « T ≈ T₀ = 2 √(M/k) », π manquant à l'impression.
  7. ex.9 : g non donné dans l'énoncé.
  8. Aucune réponse imprimée pour les tests 1–2 ni pour les exercices 7 à 13.
  9. p.150 L'essentiel : l'équation amortie y est écrite d²x/dt² + (h/m)dx/dt + ω₀²x = 0 (ω₀²x au lieu de
     (k/m)x ; équivalent puisque ω₀² = k/m, mais différent de la forme du cours p.147 et du tableau p.149).

## 2.6 Chapitre 6 — Oscillations mécaniques forcées en régime sinusoïdal (manuel 223432, p.162–183)

**Partie** : « Evolution de systèmes » (bandeau de page). Titre de la page d'ouverture (p.163) :
« OSCILLATIONS FORCÉES D'UN PENDULE ÉLASTIQUE EN RÉGIME SINUSOÏDAL » (numéro 6). [Bandeau de la p.164
imprimé « Oscillations électriques forcées en régime sinusoïdal » : coquille, identique à 223433 ;
toutes les autres pages portent « Oscillations mécaniques forcées en régime sinusoïdal ».]
Pagination : page PDF = page imprimée. Références « 223433 p.X » = manuel Sciences expérimentales, section
déjà transcrite (`bac-sciences-exp/physique.md` § 2.6, p.168–187).

**Page d'ouverture (p.163)** — identique à 223433 p.169 : trois photos légendées (marées/tsunamis ; violoniste ;
clarinettes « graves ») et les trois questions d'accroche (formes des instruments de musique ; bruits de
carrosserie à des vitesses déterminées ; régiment interdit de traverser un pont au pas cadencé).

**Objectifs (p.162)** — « ◆ Distinguer, en régime mécanique forcé, entre l'excitateur et le résonateur. ◆ Distinguer
en mécanique, entre les oscillations libres et les oscillations forcées. ◆ Mettre en évidence la résonance
d'élongation d'un pendule élastique. ◆ Etablir l'expression de l'amplitude Xm des oscillations d'un pendule
élastique en fonction de la fréquence N de l'excitateur. ◆ Etudier l'influence de l'amortissement sur la
résonance d'élongation d'un pendule élastique. ◆ Établir l'expression du déphasage entre la force excitatrice F
et l'élongation x du solide. ◆ Interpréter théoriquement le phénomène de résonance. ◆ Distinguer une résonance
aiguë d'une résonance floue. ◆ Utiliser l'analogie formelle électrique - mécanique pour : - caractériser la
résonance de charge dans un circuit RLC série, - caractériser la résonance de vitesse d'un pendule élastique,
- exprimer la puissance mécanique moyenne d'un pendule élastique. »

**Prérequis (p.162)** — SAVOIR : « Exprimer la période propre des oscillations libres d'un pendule élastique en
fonction de ses grandeurs caractéristiques. Ecrire l'équation différentielle caractéristique des oscillations
libres d'un pendule élastique amorti ou non amorti. Exprimer la puissance électrique moyenne absorbée par un
oscillateur électrique. » SAVOIR FAIRE : « Appliquer la relation fondamentale de la dynamique à un solide en
mouvement. Associer à une fonction sinusoïdale, un vecteur de Fresnel. Faire la construction de Fresnel. Faire
l'analogie formelle entre un oscillateur mécanique amorti et un circuit RLC - série. »

**Introduction (p.164)** — identique à 223433 p.170 (« … lorsque l'apport de l'énergie se produit
périodiquement avec un dispositif approprié appelé excitateur, les oscillations mécaniques entretenues sont
dites forcées. »).

**Plan du chapitre** (titres numérotés du manuel) : 1. Production d'oscillations forcées (p.164–166) ·
2. Influence de la fréquence de l'excitateur sur l'amplitude des oscillations (p.166) · 3. Influence de
l'amortissement sur l'amplitude des oscillations (p.166–168) · 4. Étude théorique (p.168–171) : 4.1 Nature des
oscillations ; 4.2 Amplitude et phase initiale des oscillations (représentation de Fresnel) ; 4.3 Résonance
d'élongation · 5. Résonance de vitesse et résonance de charge (p.171–172, tableau d'analogie) · 6. Puissance
mécanique (p.172) · 7. Importance des oscillations mécaniques forcées et de la résonance (p.173–174) :
1- Dans la nature : phénomène des marées ; 2- En acoustique ; 3- En industrie : oscillations forcées dues aux
trépidations du rotor d'une machine tournante (+ « Exemple d'illustration », gyroscope à lames) ; 4- Dans les
ouvrages · L'essentiel (p.175) · Exercices : exercices résolus 1 et 2 (p.176–177) ; Exercices à résoudre
(p.178–181) : Tests rapides des acquis (1 vrai/faux, 2 QCM), Exercices d'application (3–5), Exercices de
synthèse (6–9), Etude de texte (10) · En savoir plus (p.182–183). Réponses aux exercices : p.318 (ch.6, ex.3 et
5) et p.319 (ch.6, ex.6 et 7). **Pas de fiche technique** dans ce chapitre.

### Cours — Manipulations (activités)

**1. Production d'oscillations forcées** (p.164–166) — **identique à 223433 p.170–171** (même dispositif Fig.1 :
palet (S) m = **100 g** sur banc à coussin d'air, ressort **k = 6,5 N.m⁻¹** [écrit « 6,5 » ici], excentrique + moteur
(M) de fréquence N réglable, stylet + cylindre enregistreur ; moteur à **N = 1,5 tr.s⁻¹** ; Fig.2 : sinusoïde
x(cm) de crête ±3, partant de 0 en croissant à t = 0, trois crêtes, période lue 2/3 s sur l'image ; Remarque
p.165 : montage potentiométrique Fig.3 « Solution aqueuse de sulfate de cuivre », sortie « Vers un ordinateur ou un
oscilloscope à mémoire », « La tension U_OM est proportionnelle à l'abscisse x du point M » ; mêmes Questions 1°)
2°) ; même Interprétation « x = Xm sin (2πNt + ϕ) »). **Seule différence : la Conclusion** (voir Encadrés,
« avec une période imposée par l'excitateur » ; 223433 : « sinusoïdales de période égale à celle de
l'excitateur »). Remarque p.166 : « La dénomination résonateur sera justifiée plus loin. »

**2. Influence de la fréquence de l'excitateur sur l'amplitude** (p.166) — **DIFFÈRE de 223433 p.172.**
- **Manipulation** : « On fait varier la fréquence de rotation du moteur et on mesure à chaque fois l'amplitude
  des oscillations du pendule élastique. Les résultats des mesures permettent de tracer la courbe de réponse
  Xm = f(N) de la figure 4. » **Fig.4** (ajoutée ici) : axes Xm (cm) gradué 0, 5, 10, 15 et N (Hz) gradué 1, 2, 3 ;
  pic unique d'environ 13 cm vers N ≈ 1,25 Hz, courbe partant d'environ 2,7 cm à N ≈ 0,1 Hz et finissant vers
  0,7 cm à N ≈ 3,2 Hz (valeurs lues à 250 dpi, approximatives ; aucune donnée numérique imprimée) [?].
- **Questions** : « 1°) Décrire la courbe de la figure 4 et en déduire l'influence de la fréquence N des
  excitations sur l'amplitude Xm des oscillations du pendule élastique. 2°) Relever la valeur de la fréquence N
  pour laquelle l'amplitude des oscillations est maximale et la comparer à la fréquence propre N0 du pendule
  élastique. 3°) La courbe de la figure 4 est appelée courbe de résonance d'élongation. Justifier cette
  qualification ainsi que la désignation du pendule élastique comme étant le résonateur. »
  (223433 : questions « étude antérieure » / « justifier la qualification de résonateur » / « comparer la
  fréquence de résonance avec la fréquence propre », sans courbe.)
- **Conclusion** : voir Encadrés (identique à 223433 p.172).
- Note de calcul de la fiche, non imprimée dans le manuel : la fréquence propre du pendule de la manipulation 1
  (m = 100 g, k = 6,5 N.m⁻¹) vaut (1/2π)√(k/m) ≈ 1,28 Hz, ce qui place le pic de Fig.4 juste sous N0 ; le manuel ne
  donne pas cette valeur [?].

**3. Influence de l'amortissement** (p.166–168) — Expériences 1, 2, 3 **identiques à 223433** pour le montage
(voile = plaque rectangulaire perpendiculaire à l'axe du banc, Fig.5 ; plaque « un peu plus grande » ; plaque
« de grandes dimensions ») ; Remarque (pendule élastique vertical, air ou liquide, avec ou sans rondelle ; **Fig.7**
ici, Fig.6 dans 223433). **Ajout : Fig.6 « Influence de l'amortissement sur l'amplitude »** — trois courbes Xm(N)
sur le même repère, (1) pic aigu d'amplitude Xm1 à Nr1, (2) pic bas d'amplitude Xm2 à Nr2 < Nr1 (les deux fréquences
sont marquées par des pointillés), (3) droite décroissante sans pic ; aucune valeur numérique.
- **Questions DIFFÉRENTES** : « 1°) Comparer les fréquences Nr1 et Nr2 et les amplitudes Xm1 et Xm2 des oscillations à
  la résonance obtenue respectivement dans les expériences 1 et 2. 2°) En déduire l'influence de l'amortissement sur
  l'amplitude et la fréquence des oscillations à la résonance. 3°) La courbe 3 ne peut être appelée courbe de
  résonance. Elle traduit plutôt un régime forcé dit linéaire. Pourquoi ? » (223433 : comparaison avec le circuit
  RLC du chapitre 4.)
- **Interprétation** (p.167) : **identique à 223433 p.173–174** (amortissement très faible → pic étroit, résonance
  « aiguë », Xm0 ; moyen, « plaque de petites dimensions » → Xm1 < Xm0, courbe 1 ; important, « plaque de dimensions
  moyennes comme celles de l'expérience 2 » → pic peu remarquable, courbe 2, résonance « floue » ; très important →
  oscillations de très petite amplitude pratiquement indépendante de N, pas de résonance, régime « linéaire »).
  [? même correspondance moyen/important ↔ exp. 1/2 que dans 223433 ; à reprendre telle quelle.]
- **Conclusion** (p.168) : **identique à 223433 p.174** (voir Encadrés).

**4. Étude théorique** (p.168–171) — **DIFFÈRE ENTIÈREMENT de 223433** (qui procède par analogie formelle sans RFD
ni Fresnel).
- **Repère** : galiléen (O, i⃗) lié au laboratoire, i⃗ unitaire de l'axe du ressort, O = position de repos de G
  (Fig.8 « Forces extérieures au palet (S) » : P⃗, R⃗, T⃗, f⃗).
- **4.1 Nature des oscillations** (p.168–169) : forces : poids P⃗, réaction R⃗ du coussin d'air, tension T⃗ du
  ressort, frottement f⃗ ; « on supposera que les frottements sont de type visqueux. Donc, on peut écrire :
  f⃗ = − h v⃗, où h est le coefficient de frottement » ; RFD : P⃗ + T⃗ + R⃗ + f⃗ = m a⃗ ; P⃗ et R⃗ se compensent ; projection
  sur (O, i⃗) : T + f = ma ; « T = − k (x − xB), où xB est l'élongation de l'extrémité B du ressort » ; d'où
  « − k (x − xB) − hv = ma » puis « m d²x/dt² + h dx/dt + kx = kxB » ; « Le second membre de cette équation a la
  même dimension qu'une force : F = kxB » ; l'ensemble {tige de guidage − fil inextensible tendu} transmet
  intégralement le mouvement sinusoïdal de l'excentrique : « xB = (XB)m sin(ωt + φB) avec ω = 2πN où N est la
  fréquence de rotation du moteur. Avec le choix φB = 0 ; on a : xB = (XB)m sin ωt. Par suite : F = Fm sin ωt
  avec Fm = k(XB)m. » « Ainsi tout se passe comme si le palet (S) est soumis directement à une force excitatrice
  F⃗ = F.i⃗. » Équation (1) : m d²x/dt² + h dx/dt + kx = Fm sin ωt. « Une telle équation différentielle admet comme
  solution particulière : x = Xm sin(ωt + φ), ce qui explique les oscillations sinusoïdales de (S) en régime
  permanent à la fréquence N de l'excitateur. » (Conclusion : voir Encadrés.)
- **4.2 Amplitude et phase initiale** (p.169–170) — « Déterminons Xm et φ à l'aide de la représentation de
  Fresnel » : x = Xm sin(ωt + φ) ; v = dx/dt = Xm ω sin(ωt + φ + π/2) ; a = d²x/dt² = Xm ω² sin(ωt + φ + π) ;
  équation (2) : m Xm ω² sin(ωt + φ + π) + h Xm ω sin(ωt + φ + π/2) + k Xm sin(ωt + φ) = Fm sin ωt ; vecteurs de
  Fresnel associés : OA1 [kXm, φ], OA2 [hXm ω, φ + π/2], OA3 [mXm ω², φ + π], OA [Fm, 0] ; « OA1 + OA2 + OA3 = OA » ;
  trois cas de construction (Fig.9a ω < ω0 ; 9b ω = ω0 ; 9c ω > ω0 ; légendes des vecteurs : kXm, hωXm, mω²Xm, Fm,
  angle φ, « axe des phases »). [Fig.9 : kXm tracé horizontal, Fm oblique le long de l'axe des phases, φ mesuré de Fm à kXm — orientation différente de OA [Fm, 0] du texte p.169 ; constructions équivalentes à une rotation près.] « On remarque que dans les trois cas, φ < 0. Donc, l'élongation x est toujours en
  retard de phase par rapport à la force excitatrice. » Cas 1 (ω < ω0) : −π/2 < φ < 0 rad ; cas 2 (ω = ω0) :
  φ = −π/2 rad ; cas 3 (ω > ω0) : −π < φ < −π/2 rad. « L'application du théorème de Pythagore dans le cas général
  donne : Fm² = (k − mω²)² Xm² + h²ω² Xm², d'où : Xm = Fm / √(h²ω² + (k − mω²)²) » (encadré) « et pour φ, on a :
  Fm² = (k − mω²)² » (encadré, imprimé tel quel [?]). **Remarque** : « le déphasage φ entre l'élongation x(t) et la
  force excitatrice F(t) peut être caractérisé par cos φ = (k − mω²)/Fm » (encadré, imprimé tel quel [?]).
- **4.3 Résonance d'élongation** (p.170–171) — démonstration dans le cours : Xm maximale quand le dénominateur
  [h²ω² + (k − mω²)²]^(1/2) est minimum, « c'est-à-dire lorsque sa dérivée par rapport à ω s'annule, soit :
  2h²ω − 4(k − mω²)mω = 0. Comme ω ≠ 0, cela entraîne : h² = 2m(k − mω²). D'où : ω² = k/m − h²/(2m²) = ω0² − h²/(2m²).
  or, ω = 2πN. Alors, N² = N0² − h²/(8π²m²) = Nr².** » « Ainsi, on montre que le phénomène de résonance se manifeste à
  une fréquence Nr de l'excitateur légèrement inférieure à la fréquence propre No du résonateur. A cause du terme dû
  au coefficient de frottement non nul h, l'écart (No − Nr) augmente avec celui-ci. D'autre part, l'amortissement
  influe sur l'amplitude des oscillations. Plus h est grand, plus Xm est petite. » **Question** : « Montrer que la
  résonance d'élongation devient impossible pour les valeurs de h supérieures à une valeur limite
  ho = mωo√2. » **Remarque** : « Dans le cas idéal où h = 0, la résonance aura lieu pour ω = ω0 avec une amplitude Xm
  qui tend vers l'infini (Fig.10) » (Fig.10 : courbe Xm(N) à pic infiniment étroit en N0).
  [Le cours ne montre pas de calcul de hl ; la question reste à l'élève. 223433 donnait la question
  « h supérieures à ho » ET « h = 0 » en deux questions ; ici une seule question + remarque.]

**5. Résonance de vitesse et résonance de charge** (p.171–172) — « Dans ce paragraphe, il n'y a pas lieu de faire
une étude systématique de la résonance de vitesse en mécanique ou de la résonance de charge en électrocinétique,
mais il s'agit de les dégager par recours à l'analogie formelle électrique – mécanique faite à la fin du chapitre
précédent tout en lui ajoutant l'analogie entre la tension excitatrice u = Um sin (ωt + φu) et la valeur algébrique
de la force excitatrice F = Fm sin (ωt + φF). Le tableau suivant rassemble les principaux résultats » — tableau
p.172 (voir Encadrés ; il ne comporte **aucune ligne « Vm = ωXm, φv = φx + π/2 »** ni ODE en v).

**6. Puissance mécanique** (p.172) — texte identique à 223433 p.177 ; tableau d'analogie (voir Encadrés), avec
« Fm = Z Vm » **correct** ici (223433 imprimait « Um = ZVm » côté mécanique).

**7. Importance des oscillations forcées et de la résonance** (p.173–174) — **identique à 223433 p.177–179**
(marées Fig.11 : lune et soleil, période propre de la baie proche de ~12 heures, marées de « dix mètres et même plus »
contre « 30 cm » en haute mer, centrale marémotrice ; acoustique : caisses des instruments à cordes, haut-parleur
« résonance floue » ; industrie : rotor mal équilibré, bruits de carrosserie, masselotte de plomb, paniers de machines
à laver, machines-outils ; « Exemple d'illustration » gyroscope à lames Fig.12 : lamelles d'acier d'inégales
longueurs, disque percé près du pourtour, ficelle, la plus courte lamelle entre en résonance la première ; ouvrages :
ponts suspendus, tornade, renvoi à « en savoir plus »). Seules différences : numéros de figures (Fig.11/12 au lieu de
9/10) et ordre de mots mineur (« domaine de fréquences audibles particulier »).

### Encadrés, lois et relations (VERBATIM, vérifiés sur l'image de leur page)

> **Conclusion 1** (p.165) — « Etant soumis à des excitations périodiques, le pendule élastique effectue des
> oscillations forcées avec une période imposée par l'excitateur. L'oscillateur (pendule élastique) est appelé
> résonateur. »

> **Conclusion 2** (p.166) — « En régime sinusoïdal forcé, l'amplitude Xm des oscillations d'un pendule élastique
> dépend de la fréquence N des excitations. Elle atteint sa valeur la plus élevée à une fréquence Nr légèrement
> inférieure à la fréquence propre N0 du pendule : on dit qu'il y a résonance d'élongation. Nr est appelée fréquence
> de résonance. »

> **Conclusion 3** (p.168) — « Pour une fréquence d'excitation donnée, l'amplitude des oscillations forcées d'un
> pendule élastique est d'autant plus petite que l'amortissement est plus important. Avec un faible amortissement la
> résonance est aiguë. Avec un amortissement important, la résonance est floue. La fréquence de résonance est
> inférieure à la fréquence propre du pendule élastique. Cependant, l'écart entre ces fréquences est d'autant plus
> remarquable que l'amortissement est plus important. »

> **Conclusion 4.1** (p.169) — « Etant régies par l'équation différentielle : m d²x/dt² + h dx/dt + kx = Fm sinωt,
> les oscillations forcées d'un pendule élastique évoluent sinusoïdalement au cours du temps à la pulsation ω de
> l'excitateur. » (pas de forme en v ni de « Vm = ωXm » ici.)

> **Équation (1)** (p.169) — m d²x/dt² + h dx/dt + kx = Fm sinωt, avec F = Fm sinωt, Fm = k(XB)m, ω = 2πN.
> **Solution particulière** : x = Xm sin(ωt + φ) (indice nu « φ », pas « φx »).

> **Amplitude** (p.170, encadré) — Xm = Fm / √(h²ω² + (k − mω²)²).
> **Remarque déphasage** (p.170, encadré) — cos φ = (k − mω²) / Fm. [? imprimé tel quel ; la construction de Fresnel
> donne (k − mω²)Xm = Fm cos φ ; le manuel écrit aussi « Fm² = (k − mω²)² » sans Xm² : ne pas corriger en silence.]

> **Conclusion 4.2** (p.170) — « En régime sinusoïdal forcé, un pendule élastique oscille toujours en retard de phase
> par rapport à la force excitatrice, avec une amplitude : Xm = Fm / √(h²ω² + (k − mω²)²) »

> **Tableau d'analogie, résonance de vitesse et de charge** (p.172) — colonnes Oscillateur électrique / Oscillateur
> mécanique :
> - Im = Um/Z, où Z = √(R² + (Lω − 1/Cω)²) (Z : impédance électrique) ↔ Vm = Fm/Z, où Z = √(h² + (mω − k/ω)²) (Z :
>   impédance mécanique) ;
> - tgφ = (1/Cω − Lω)/R avec φ = (φi − φu) ↔ tgφ = (k/ω − mω)/h avec φ = (φv − φF) ;
> - Résonance d'intensité : Im = Um/R à N = N0 ↔ Résonance de vitesse : Vm = Fm/h à N = N0 ;
> - Qm = Um / √(R²ω² + (1/C − Lω²)²) ↔ Xm = Fm / √(h²ω² + (k − mω²)²) ;
> - tgφ = Rω/(Lω² − 1/C) avec φ = (φq − φu) ↔ tgφ = hω/(mω² − k) avec φ = (φx − φF) ;
> - « Résonance de charge » à Nr = √(N0² − R²/(8π²L²)) ↔ **intitulé identique « Résonance de charge »** côté mécanique
>   (sic, c'est la résonance d'élongation) à Nr = √(N0² − h²/(8π²m²)).
> [Transcrit de l'image p.172 ; l'indice du premier tgφ électrique est « 1/Cω − Lω » au numérateur, « R » au
> dénominateur. Signes : tg(φv − φF) = (k/ω − mω)/h au tableau, mais l'exercice 9 écrit « tgφ = (mω − k/ω)/h » pour
> « le déphasage entre F et v » : sens de la différence non précisé [?].]

> **Puissance mécanique moyenne** (p.172) — Puissance électrique moyenne ↔ Puissance mécanique moyenne :
> P = (Um Im/2) cosφ, avec φ = φi − φU ↔ P = (Fm Vm/2) cosφ, avec φ = φv − φF ; cosφ = R/Z ↔ cosφ = h/Z ;
> Um = Z Im ↔ Fm = Z Vm ; P = ½ R Im² ↔ **P = ½ h Vm²**.

> **L'essentiel** (p.175, VERBATIM) —
> « ▪ En régime forcé, le dispositif d'entretien des oscillations d'un pendule élastique constitue l'excitateur
> tandis que le pendule constitue le résonateur.
> ▪ La fréquence des oscillations forcées d'un pendule élastique est égale à celle de l'excitateur.
> ▪ En présence de frottements visqueux, les oscillations sinusoïdales forcées d'un pendule élastique sont régies par
> l'équation différentielle : [m d²x/dt² + h dx/dt + kx = F] avec F = Fm sin(ωt + φF), valeur algébrique de la force
> excitatrice.
> ▪ En régime sinusoïdal forcé, le résonateur oscille en retard de phase par rapport à l'excitateur avec une amplitude
> Xm qui dépend de la fréquence N de l'excitateur : [Xm = Fm / √(4h²π²N² + (k − 4mπ²N²)²)]
> ▪ En régime sinusoïdal forcé, la résonance d'élongation se produit à la fréquence : [Nr = √(N0² − h²/(8π²m²))]
> ▪ La résonance est d'autant plus aiguë que l'amortissement est plus faible.
> ▪ Dans le cas d'un amortissement important, la résonance est floue. Lorsque h dépasse la valeur limite
> [hl = mω0√2], la résonance devient impossible.
> ▪ En régime sinusoïdal forcé, la puissance mécanique moyenne est donnée par la relation : [P = ½ h Vm²] »
> (Formules encadrées en vert, notées entre crochets.) L'Essentiel ne contient **ni Vm, ni la résonance de vitesse**
> (223433 : oui). Ici les formules sont complètes (pas de « L² » ni de signe manquant, contrairement à 223433).

### Exercices résolus

- **Exercice résolu 1** (p.176–177) — ressort k = 40 N.m⁻¹, extrémité B reliée indirectement à un excentrique fixé à un
  moteur ; palet (S) m = 100 g en A, plaque rectangulaire fixée ; banc à coussin d'air horizontal ; stylet qui
  enregistre x(t) (Fig. : crête ±6 mm, x = +6 mm à t = 0, quadrillage, axe t gradué 0,5 et 1 s). 1°) a) rôle du moteur
  muni de l'excentrique et du système {palet–ressort} ; b) fréquence et amplitude Xm ; c) écrire x(t). 2°) on fait varier N,
  tableau **N (Hz) : 1.5 · 2 · 2.5 · 2.8 · 3.1 · 3.2 · 3.3 · 3.6 · 4 · 4.5 ; Xm (mm) : 4 · 6 · 10 · 15 · 21 · 23 · 20 · 15 · 10 · 7** ;
  a) tracer Xm = f(N) ; b) Nr et comparaison avec N0 ; c) effet d'une plaque de plus grande surface.
  **Solution** : 1°) a) moteur + excentrique = excitateur, {palet–ressort} = résonateur ; b) T = 0.5 s, f = 2 Hz,
  Xm = 6 mm ; c) x(t) = Xm sin(ωt + φx) ; à t = 0, x = Xm sinφx = Xm, sinφx = 1, φx = π/2 rad ; ω = 2πN = 4π rad.s⁻¹ ;
  **x(t) = 6.10⁻³ sin(4πt + π/2)** ; 2°) a) graphe Xm = f(N) fourni (pic d'environ 23 mm vers 3,2–3,3 Hz) ; b) « Nr = 3.15 Hz » ;
  « No = (1/2π)√(k/m), soit numériquement : No = 3,18 Hz. On remarque que Nr est légèrement inférieure à No. » ;
  c) plaque plus grande → l'amortissement augmente, Xm moins important à la résonance, pic moins prononcé, résonance
  « moins auguë » [sic]. [? Nr = 3.15 Hz n'est pas lu directement sur le tableau, dont le maximum est à 3,2 Hz ; valeur du
  manuel, à reprendre telle quelle.] **Écart avec 223433** : autre énoncé (k = 40 identique, mais enregistrement ±6 mm,
  tableau N/Xm au lieu de « calculer h » ; plus de questions sur la fréquence N2 > N1, plus de Xm = 15 mm ni Fm = 0,15 N,
  plus de h = 0,5 N.s.m⁻¹) ; ici π présent dans N0 (223433 l'omettait).
- **Exercice résolu 2** (p.177) — voiture sur piste saharienne, bosses espacées de d = 20 m, m = 1000 kg, k = 4.10⁴ N.m⁻¹ :
  **identique à 223433 p.182**, avec la solution correcte : T = d/v ; To = 2π√(m/k) ; résonance à T = To ; d/vc = 2π√(m/k) d'où
  vc = (d/2π)√(k/m) ; **vc = 20,14 m.s⁻¹ ou vc = 72,5 km.h⁻¹** ; 2°) les amortisseurs absorbent une partie de l'énergie des
  oscillations, l'amplitude des secousses diminue, meilleure tenue de route et plus de sécurité. (223433 omettait π dans
  To et vc ; mêmes valeurs numériques.)

### Exercices à résoudre (p.178–181) ; réponses du manuel p.318–319

**Tests rapides des acquis** (p.178)
- **1 Vrai ou faux** (8 items) : **identique à 223433 p.183 pour les items 1 à 7** (1- le ressort est l'excitateur, le solide le
  résonateur ; 2- la période est imposée par l'excitateur ; 3- le pendule peut osciller avec sa période propre ; 4- résonance
  d'élongation chaque fois que N = fréquence propre ; 5- x toujours en retard de phase sur F ; 6- l'élongation n'est maximale
  qu'à la résonance ; 7- à la résonance d'élongation, Xm augmente avec l'amortissement). **Item 8 DIFFÈRE** : « Lorsque
  l'amortissement est faible, la courbe de résonance est caractérisée par un pic très large. » (223433 : « La résonance
  d'élongation est d'autant plus aiguë que l'amortissement est faible. » ; ici la proposition est fausse, pic « étroit »).
  Aucune réponse imprimée.
- **2 QCM** (6 questions) : identiques à 223433 p.183 (1- l'élongation est a- toujours en retard sur sa vitesse / b- toujours en
  retard sur F / c- alternativement en avance et en retard sur F ; 2- à la résonance Xm est a- maximale seulement en valeur
  absolue / b- la plus élevée / c- indépendante de l'amortissement ; 3- la période a- n'est pas égale à celle de l'excitateur /
  b- ne dépend que de la période propre / c- dépend du coefficient de frottement ; 4- Xm est a- d'autant plus grande que
  l'amortissement est plus important / b- d'autant plus grande que N est proche de la fréquence propre / c- d'autant plus
  petite que la masse est grande ; 5- la résonance d'élongation a- n'est possible que si la période propre est très petite /
  b- peut être obtenue avec n'importe quel h / c- est d'autant plus aiguë que l'amortissement est plus faible ; 6- d'après
  l'analogie a- on peut définir l'impédance mécanique / b- à la résonance d'intensité correspond une résonance d'élongation
  mécanique / c- la puissance mécanique moyenne est constante à la résonance d'élongation). Seul écart : question 2 dit « A
  la résonance » (et non « d'élongation »). Aucune réponse imprimée.

**Exercices d'application** (p.179)
- **3** : ressort k = 50 N.m⁻¹, m = 100 g, pendule horizontal avec dispositif d'excitation : **identique à 223433 p.184**.
  1°) excitateur/résonateur ; 2°) To ; 3°) risque si la fréquence imposée est proche de la fréquence propre. Réponse p.318 :
  « 2°) To = 0,28 s ; 3) Risque de rupture ».
- **4** : **DIFFÈRE** (223433 : m = 200 g, k = 5, x = 0,025 sinπ(1,2t + 0,75)). Ici : extrémité supérieure d'un ressort (R) reliée à un
  excentrique mû par un moteur de N tours par seconde, extrémité inférieure fixée à un solide (S) plongé dans un liquide
  visqueux ; tableau **N (Hz) : 1.5 · 2 · 2.5 · 2.8 · 3.1 · 3.2 · 3.3 · 3.6 · 4 · 4.5 ; Xm (cm) : 0.4 · 0.6 · 1 · 1.5 · 2.1 · 2.3 · 2 · 1.5 · 1 · 0.7**
  (mêmes nombres que le tableau de l'exercice résolu 1, en cm). 1°) tracer Xm = f(N) ; 2°) quel phénomène à N = 3.2 Hz ; 3°) en
  déduire la période des oscillations à la résonance ; 4°) modification du graphe si (S) oscille dans l'air. Pas de réponse imprimée.
- **5** : bosses espacées de d = 60 cm, voiture à v constante : **identique à 223433 p.184** (à un mot près : « ou très lentement
  ou avec une vitesse supérieure »). 1°) T = d/v et N = v/d ; 2°) a) excitateur/résonateur ; b) N0 = 5 Hz, montrer l'existence d'une
  vitesse vo de résonance (fréquence de résonance admise = fréquence propre). Réponse p.318 : « 1°) T = d/v ; N = v/d 2°) b) vo = 3 m.s-1 ».

**Exercices de synthèse** (p.179–181)
- **6** (p.179–180) : (S) masse m, ressort k, frottement f⃗ = − h v⃗, force F(t) = Fmax sin(2πNt + φF) i⃗. **1°) DIFFÈRE** : « Etablir
  que l'élongation x, sa dérivée première dx/dt et sa dérivée seconde d²x/dt² vérifient la relation : m d²x/dt² + h dx/dt + kx = F(t) »
  (223433 : « Xm en fonction de Fm, k, h par analogie »). 2°) enregistrement x(t) = Xm sin(2πNt + φx) (Fig. : x(cm), crête ±5,
  x = +5 à t = 0, « T = 0,14 π (s) » entre deux minima) : a) deux oscillations = un tour du cylindre : tours par minute ; Xmax, N, φx ;
  b) m = 98 g, k = 20 N.m⁻¹ : montrer résonance de vitesse ; c) en déduire m d²x/dt² + kx = 0 ; d) Fmax, φF, puissance moyenne,
  h = 1.8 kg.s⁻¹ — **mêmes questions 2° que 223433**. Réponse p.319 : « 2°) a) 68,2 tr.min-1 ; 5 cm ; 2.27 Hz ; π/2 rad b) To = T, résonance
  de vitesse ; d) Fm = 1,29 N ; φF = 0 rad ; P = 0,46 W ». [? « φF = 0 rad » : à la résonance de vitesse v et F sont en phase ; avec
  φx = π/2, φv = φx + π/2 = π, donc φF = π ; réponse imprimée du manuel, même doute que 223433 ; à ne pas reprendre sans
  vérification.]
- **7** (p.180) : m = 51 g sur banc à coussin d'air, extrémité du ressort en translation sinusoïdale (disque + moteur de fréquence
  N) ; à 1,25 tr.s⁻¹ amplitude maximale 4,8 cm ; 1°) montage d'enregistrement ; 2°) excitateur/résonateur ; 3°) a) période ; b) raideur
  approchée ; 4°) palette dans l'eau, amplitude 2,4 cm : a) interpréter, b) huile ; 5°) Nr : a) phénomène ; b) période et amplitude
  dépendent-elles du liquide : **identique à 223433 p.185**. Réponse p.319 : « 3) a) 0,8 s, b) 3,14 N.m-1 ».
- **8** (p.180–181) : **DIFFÈRE**. Pendule {m, k} horizontal excité par un moteur muni d'un excentrique (force périodique sur
  l'extrémité du ressort non reliée à (S)). 1°) type d'oscillations du résonateur et période ; 2°) To = 0,46 s : phénomène si la
  période de la force excitatrice devient voisine de 0,46 s ; 3°) tableau **N (Hz) : 1.2 · 1.4 · 1.6 · 1.8 · 1.9 · 2.0 · 2.1 · 2.2 · 2.3 · 2.4 · 2.5 · 2.7 ·
  2.8 · 2.9 ; Xm (cm) : 1.6 · 2.2 · 3.2 · 4.8 · 5.7 · 6.4 · 6.8 · 6.5 · 5.6 · 5.0 · 4.2 · 3.2 · 3.0 · 2.7** : a) tracer Xm = f(N) sur papier millimétré ;
  b) Nr de résonance et comparaison avec N0. (223433 : T = To, amplitude 4 cm, Vm, h avec Fm = 0,25 N.) Pas de réponse imprimée.
- **9** (p.181) : (S) m, ressort k, f⃗ = − h v⃗, F = Fm sinωt. 1°) **« Etablir l'équation » m d²x/dt² + h dx/dt + kx = Fm sinωt** (223433 :
  « par recours à l'analogie ») ; 2°) construction de Fresnel (par analogie avec le RLC série) : montrer « Z = Fm/Vm = √(h² + (mω − k/ω)²),
  où Vm est la vitesse maximale de (S) » et « tgφ = (mω − k/ω)/h » (déphasage « entre F et v ») ; 3°) v(t) en fonction de Fm, Z, φ ;
  4°) x(t) ; 5°) ω de résonance de vitesse, déphasage v/F alors ; 6°) montrer que l'amplitude est maximale (« résonance d'amplitude »)
  quand « Y = [m²ω⁴ + (h² − 2mk)ω² + k²] » est minimale (« quantité » ; 223433 : « somme », « résonance d'élongation ») ; ωr ; vérifier
  ωr < ωo ; existence d'une valeur de h « telle qu'il n'existe plus de phénomène de résonance d'amplitude ». Pas de réponse imprimée.

**Étude de texte** (p.181)
- **10** : « le salaire de la peur » (H.-G. Clouzot), camion de nitroglycérine sur « tôle ondulée » : **identique à 223433 p.186**
  (1°) phénomène ; 2°) m = 10 tonnes, suspensions affaissées de 1,2 mm sous une charge de 6,5 tonnes : a) raideur équivalente ;
  b) période et fréquence ; 3°) bosses espacées de d = 0,70 m : vitesse la plus critique ; 4°) l'affirmation (rouler soit très lentement
  soit très vite) est-elle justifiée ?). Pas de réponse imprimée.

**En savoir plus** (p.182–183) — « Dangers de la résonance » : **même contenu que 223433 p.187** (suspension de voiture modélisée
par ressort + masse ; pistes sahariennes, amortisseurs à huile / à gaz sur les motos ; Tacoma Narrow Bridge, Puget Sound,
novembre 1940, cinq mois après l'ouverture, rafales périodiques ; pont suspendu sur la Maine à Angers, 16 avril 1850, troupe au pas
cadencé ; vérins amortisseurs ; tour Taipei 101, 2004, 508 m, 101 étages, boule d'acier de 800 tonnes entre les 88ᵉ et 92ᵉ étages ;
deux photos du pont de Tacoma avant/après rupture). **Pas de fiche technique** dans ce chapitre.

### Écart avec Sciences expérimentales

**Ce que 223432 (section Mathématiques) AJOUTE :**
- **Établissement de l'équation différentielle par la RFD** (§4.1 : P⃗ + T⃗ + R⃗ + f⃗ = m a⃗, T = − k(x − xB), xB = (XB)m sin ωt,
  F = kxB, Fm = k(XB)m) — 223433 l'écarte explicitement (analogie seulement).
- **Détermination de Xm et φ par la construction de Fresnel** (§4.2, Fig.9a/b/c, théorème de Pythagore) ; expression
  du déphasage : φ < 0 dans les trois cas, x toujours en retard sur F ; intervalles de φ selon ω < ω0 / = ω0 / > ω0
  (−π/2 < φ < 0 ; φ = −π/2 ; −π < φ < −π/2) ; cos φ = (k − mω²)/Fm [?] ; tgφ = hω/(mω² − k) au tableau p.172 (223433 : seulement
  « retard de phase » affirmé, tgφ seulement à l'ex. 9).
- **Démonstration de Nr dans le cours** par dérivation du dénominateur (2h²ω − 4(k − mω²)mω = 0 → h² = 2m(k − mω²) →
  Nr² = N0² − h²/(8π²m²)) (223433 : formule donnée via analogie, démonstration en Question).
- **Courbes tracées** : Fig.4 (courbe de réponse Xm = f(N)), Fig.6 (trois courbes d'amortissement), Fig.10 (cas idéal h = 0) ;
  tableaux de mesures N/Xm dans les exercices résolus 1, application 4 et synthèse 8, avec « tracer le graphe » et lecture de Nr (223433 :
  aucune courbe, aucun tableau de mesures).
- **Tableau d'analogie complet** p.172 (Im/Vm, Z impédances, tgφ, Qm/Xm, Nr) reproduisant les deux colonnes ; mention explicite de
  l'**impédance mécanique** Z = √(h² + (mω − k/ω)²) et de Fm = Z·Vm.
- **Objectifs** : « Etablir l'expression de l'amplitude Xm en fonction de la fréquence N » ; « Interpréter théoriquement le
  phénomène de résonance » ; analogie limitée à résonance de charge / résonance de vitesse / puissance (223433 : écrire les équations
  en x ou en v, Xm et Vm en fonction de N, résonance d'élongation et de vitesse, puissance). Prérequis ajoutés : RFD, vecteur de Fresnel,
  construction de Fresnel.
- **Exercices** : nouvel exercice résolu 1 (tableau N/Xm, Nr = 3.15 Hz vs N0 = 3,18 Hz) ; application 4 (tableau avec liquide visqueux) ;
  synthèse 8 (tableau N/Xm de 14 points) ; synthèse 6 1°) et 9 1°) « Etablir » l'équation (au lieu de « par analogie ») ; V/F 8
  reformulé (« pic très large »).

**Ce que 223432 RETIRE (présent dans 223433) :**
- La **forme en vitesse** de l'équation (m dv/dt + hv + k∫v dt = F) et les relations « v = Vm sin(ωt + φv), Vm = ωXm, φv = φx + π/2 »
  (§4.1, Conclusion 4.1 et Essentiel de 223433) ; le « paragraphe » d'analogie pour obtenir x(t) et v(t) avec les questions 1°) a/b, 2°).
- Le **calcul de Vm** (question de 4.2 de 223433, formule Vm = Fm/√(h² + (mω − k/ω)²) au cours — ici seulement dans le tableau p.172) et la
  mention Vm dans l'Essentiel ; la résonance de vitesse n'est plus qu'une ligne du tableau d'analogie (« Vm = Fm/h à N = N0 »).
- Les tableaux d'analogie séparés (q↔x, i↔v, L↔m, R↔h, 1/C↔k, u↔F) et le circuit Fig.8 de 223433 (GBF, K, Ro, bobine, C).
- L'**exercice résolu 1** de 223433 (calcul de h = Fm/(2πNoXm) = 0,5 N.s.m⁻¹, N2 > N1) ; l'**application 4** (x = 0,025 sinπ(1,2t + 0,75)) ;
  la **synthèse 6 1°)** (Xm par analogie) ; la **synthèse 8 3°)** (Vm et h avec Fm = 0,25 N).
- La question « 1°) comparer avec le circuit RLC (chapitre 4) » de §3 ; la question « étude antérieure » de §2.
- La coquille « Um = ZVm » (mécanique) et les erreurs d'impression de l'Essentiel (« L² », signe « − » manquant) : corrigées ici.

**Identique (à ne pas recopier)** : page d'ouverture, introduction, §1 (sauf Conclusion 1), Conclusions 2 et 3, interprétation du §3,
§6 texte, §7 (importance : marées, acoustique, industrie, gyroscope, ouvrages), V/F 1–7, QCM 1–6, exercices 3, 5 (un mot près), 7, 10, exercice
résolu 2 (sauf π), en savoir plus, réponses 3, 5, 6, 7.

### Bornes de scope (section Mathématiques)

✅ **Inclus**
- Vocabulaire : excitateur / résonateur ; oscillations libres vs forcées ; régime permanent ; résonance d'élongation, fréquence de
  résonance Nr ; résonance de vitesse ; résonance aiguë / floue ; régime forcé « linéaire » ; impédance mécanique Z.
- Expérimental : pendule élastique horizontal sur banc à coussin d'air entraîné par moteur + excentrique (ou pendule vertical, voile/plaque,
  liquide, rondelle) ; enregistrement x(t) ; courbes de réponse Xm = f(N) ; montage potentiométrique cité.
- Fréquence des oscillations forcées = fréquence de l'excitateur ; x = Xm sin(ωt + φ) ; ODE m d²x/dt² + h dx/dt + kx = Fm sinωt **établie
  par la RFD** (f⃗ = − hv⃗, F = kxB, xB = (XB)m sinωt).
- **Construction de Fresnel** (vecteurs kXm, hωXm, mω²Xm, Fm), trois cas ω <, =, > ω0 ; Xm = Fm/√(h²ω² + (k − mω²)²) ; x toujours en
  retard de phase sur F, φ < 0 (−π/2 < φ < 0 ; −π/2 ; −π < φ < −π/2) ; cos φ = (k − mω²)/Fm [?] ; Xm(N) = Fm/√(4h²π²N² + (k − 4mπ²N²)²).
- **Démonstration de Nr** par annulation de la dérivée du dénominateur : Nr = √(N0² − h²/(8π²m²)) < N0 ; écart N0 − Nr croît avec h ;
  Xm décroît quand h croît ; limite hl = mω0√2 (donnée à l'Essentiel, à démontrer en Question/ex. 9 6°) ; cas idéal h = 0.
- Analogie formelle électrique-mécanique : tableau d'ensemble p.172 ; résonance de vitesse : Nr = N0, Vm = Fm/h ; impédance Z =
  √(h² + (mω − k/ω)²), Fm = ZVm, tgφ, cosφ = h/Z ; puissance moyenne P = (FmVm/2)cosφ = ½hVm².
- Calculs : No = (1/2π)√(k/m), To = 2π√(m/k) ; vitesse critique sur bosses T = d/v, résonance si T = To ; lecture de Nr sur un tableau ou un
  graphe Xm(N) (ex. résolu 1, ex. 4, ex. 8).
- Applications documentaires : marées, caisses de résonance, haut-parleur (résonance floue), machines tournantes, gyroscope à lames,
  ponts (Tacoma, Angers), Taipei 101.

⛔ **Exclu / non traité dans le chapitre**
- Résolution générale de l'équation différentielle (régime transitoire) ; seule la solution particulière sinusoïdale est affirmée.
- Démonstration de hl = mω0√2 : laissée en Question (et ex. 9 6°) ; aucune démonstration de Vm dans le cours.
- Forme en v de l'ODE et relation φv = φx + π/2 : **absentes** (présentes dans 223433).
- Facteur de qualité / bande passante mécanique : aucune mention.
- Énergie mécanique de l'oscillateur forcé ; oscillateurs couplés ; autres résonateurs (pendule pesant, torsion) : absents.
- Expression explicite de tgφ en fonction de x, ou de φ en fonction de N, au cours : seul cos φ = (k − mω²)/Fm figure en Remarque ; tgφ
  = hω/(mω² − k) uniquement dans le tableau d'analogie [?].
- Appareillage : seuls banc à coussin d'air, moteur à excentrique, stylet + cylindre enregistreur, montage potentiométrique (sulfate de cuivre),
  ordinateur / oscilloscope à mémoire ; pas de capteur détaillé ni de logiciel nommé.

### Lecture

- **Couche texte** : p.162–183 (22 pages) et p.318–320 ; la p.320 est une liste de sites web (sans réponse) ; les réponses du ch.6 sont
  en p.318 (ex. 3, 5) et p.319 (ex. 6, 7) ; aucune réponse pour les ex. 1, 2, 4, 8, 9, 10 ni pour les tests 1–2.
- **Lues sur l'image** (**24 pages** à 110 dpi) : p.162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178,
  179, 180, 181, 182, 183, 318, 319 ; recadrages à 250 dpi : Fig.2 (p.164), Fig.4 (p.166), Fig.6 (p.167), graphe de l'ex. 6 (p.180).
- **Sondage / écarts texte↔image** (sondage couvrant 100 % des pages, dont les plus denses : 169, 170, 172, 175, 177, 181) :
  p.168–169 la couche texte perd tous les symboles (ω, φ, π, vecteurs P⃗ R⃗ T⃗ f⃗ i⃗, « x B s'écrit … (t + B) ») ; p.170 les trois figures de
  Fresnel, les signes « − » des intervalles de φ (« π/2 < φ < 0 » rendu sans signe), cos φ et la dernière ligne « Fm² = (k − mω²)² »
  sont illisibles ou tronqués en texte ; p.171 la dérivée, N² et ho = mωo√2 dégradés ; p.172 tableau d'analogie déstructuré en texte (ordre
  des colonnes mêlé, tgφ éparpillés) ; p.175 formules encadrées (Xm(N), Nr, hl, P) absentes ou éclatées en texte ; p.176–177 formules
  de N0, To, vc perdues en texte, graphes (x(t), Xm(N)) invisibles ; p.179–181 flèches de vecteurs et formules de l'ex. 9 déplacées ; p.318–319
  les réponses ch.6 lisibles en texte et confirmées à l'image.
- **Doutes / coquilles signalées [?]** : bandeau p.164 « électriques » ; cos φ = (k − mω²)/Fm et « Fm² = (k − mω²)² » sans Xm (p.170) ;
  intitulé « Résonance de charge » sous la colonne mécanique du tableau p.172 (c'est la résonance d'élongation) ; signe de tgφ au tableau
  (« (k/ω − mω)/h » pour φv − φF) vs ex. 9 (« (mω − k/ω)/h » entre F et v) ; correspondance amortissement moyen/important ↔
  expériences 1/2 (p.167) ; Nr = 3.15 Hz non lu directement sur le tableau de l'ex. résolu 1 (max à 3,2 Hz) ; ex. 6 : « φF = 0 rad » (voir
  ci-dessus) ; « moins auguë » (ex. résolu 1) ; Fig.4 : lecture du pic ≈ 13 cm vers ≈ 1,25 Hz à 250 dpi, non confirmée par le texte ; fréquence propre
  de la manipulation 1 (1,28 Hz) non donnée par le manuel (calcul de la fiche) ; aucune réponse imprimée pour V/F, QCM, ex. 1, 2, 4, 8, 9, 10.

## 2.7 Chapitre 7 — Ondes mécaniques progressives (manuel 223432, p.184–217)

**Mode de lecture de cette section** : fiche DIFFÉRENTIELLE. Référence = section R-7 du manuel Sciences
expérimentales 223433 (`bac-sciences-exp/physique.md` § 2.7, p.188–225). Collation faite sur les 34
pages (couche texte, comparée mot à mot page par page avec 223433 en décalage de 6 pages pour
p.184–213, de 7 pour les fiches techniques) PUIS image de chacune des 34 pages + p.319.
Constat : **le cours, l'exercice résolu, les tests rapides et les exercices 3 à 14 sont identiques à
223433** (même texte, mêmes figures, mêmes données, mêmes réponses). Les seules différences réelles
sont listées en « Écart avec Sciences expérimentales ». Correspondance de pagination : p.X de 223432 =
p.X+6 de 223433 pour p.184–213 ; p.214 (ex.14 fin + ex.15) ↔ p.220–221 ; p.215–216 (fiches) ↔ p.222–223 ;
p.217 (En savoir plus) n'a pas d'équivalent.

**Pas d'ouverture de partie** (223433 p.188–189 « ONDES ONDES ONDES » + sommaire de la partie) : ici le
chapitre s'ouvre directement sur Objectifs/Prérequis (p.184) puis la page-titre (p.185). L'en-tête
courant des pages est « Ondes • Ondes mécaniques progressives ». Le chapitre suivant (p.218) est
« Interactions onde - matière » (hors de cette section, voir Bornes).

**Page-titre (p.185)** — « ONDES MECANIQUES PROGRESSIVES 7 ». Photo de vagues, légende : « Les vagues
constituent un exemple de propagation d'ondes dans un milieu élastique. » Questions d'accroche
(identiques à 223433 p.191) : « ◆ D'où provient l'énergie des vagues ? ◆ Le déferlement des vagues
correspond-il à un déplacement de matière ou d'énergie ? ◆ Nos oreilles perçoivent des sons. Qu'est-ce
qui fait qu'ils nous parviennent et pourquoi les sons émis et ceux qu'on perçoit sont les mêmes ? »

**Objectifs (p.184, verbatim, vus sur l'image)** — « ◆ Distinguer entre une onde transversale et une onde
longitudinale. ◆ Reconnaître que la propagation d'une onde est due à une propagation d'énergie sans
transport de matière. ◆ Réaliser une expérience illustrant la propagation d'une onde sinusoïdale dans
un milieu homogène et isotrope. ◆ Identifier dans un milieu de propagation donné, les propriétés dont
dépend la célérité d'une onde. ◆ Etablir l'équation horaire du mouvement d'un point donné du milieu de
propagation connaissant celle de la source d'onde progressive et représenter graphiquement le
diagramme du mouvement de ce point. ◆ Représenter graphiquement l'aspect à un instant donné, du milieu
(ou d'une coupe du milieu) de propagation d'une onde progressive. ◆ Reconnaître la double périodicité
d'une onde sinusoïdale. » (identiques à 223433 p.190.)

**Prérequis (p.184, lus sur l'image)** — SAVOIR : définir un phénomène périodique ; définir la période T
et la fréquence N d'un phénomène périodique ; écrire la relation N = 1/T ; définir une grandeur
sinusoïdale ; définir la pulsation et l'amplitude d'une grandeur sinusoïdale ; écrire la relation
T = 2π/ω (ou N = ω/2π). SAVOIR FAIRE : utiliser l'oscilloscope ; appliquer les relations N = 1/T et
T = 2π/ω (ou ω = 2πN) ; représenter graphiquement une grandeur sinusoïdale en fonction du temps ;
mesurer les durées et les vitesses à l'aide de photocapteurs. (Identiques à 223433.)

**Plan du chapitre** (titres numérotés du corps, identiques à 223433) : introduction (caillou dans une
nappe d'eau, p.186) · **1. Propagation d'un ébranlement** (1.1 milieu unidimentionnel [sic] ; 1.2 milieu
bidimentionnel ; 1.3 milieu tridimentionnel ; 1.4 célérité d'un ébranlement) · **2. Propagation d'une
onde sinusoïdale entretenue** (2.1 généralités sur l'onde entretenue ; 2.2 onde progressive le long
d'une corde élastique tendue — étude expérimentale, étude théorique ; 2.3 onde sinusoïdale le long d'un
ressort ; 2.4 onde sinusoïdale à la surface de l'eau ; 2.5 le son, exemple d'onde progressive à trois
dimensions) · L'essentiel (p.204) · Exercices : exercice résolu (p.205–207), Tests rapides des acquis
(ex. 1–2, p.208), Exercices d'application (ex. 3–6, p.209–210), Exercices de synthèse (ex. 7–15,
p.210–214) · Fiche technique n°1 (p.215) · Fiche technique n°2 (p.216) · En savoir plus (p.217).

### Cours — Activités / manipulations (identique à 223433 p.192–209, sauf pagination)

**Introduction (p.186)** — identique à 223433 p.192 (« En jetant un caillou dans une nappe d'eau calme […]
Comment peut-on expliquer l'élargissement progressif de ces rides circulaires […] ? »).

**1.1 Milieu unidimensionnel (p.186–187)** — identique à 223433 p.192–193. Expérience 1 : longue corde
élastique tendue horizontalement sur le sol, va-et-vient rapide en O, Fig.1 (corde à t₀ = 0, t₁ > 0,
t₂ > t₁, t₃ > t₂, la bosse avance ; légende « Chaque point de la corde se soulève verticlament » [sic]).
Expérience 2 : premières spires non jointives d'un ressort horizontal comprimées puis lâchées, Fig.2
(dates 0, t₁, t₂ ; repères a, P, b). Questions 1°) 2°) : comparer direction de l'ébranlement et
déplacement des points de la corde / des spires. Interprétation : corde → **transversal** ; ressort →
**longitudinal**.

**1.2 Milieu bidimensionnel (p.187–188)** — identique à 223433 p.193–194. Goutte d'eau sur cuve à ondes,
ride circulaire (Fig.3, t₁, t₂ > t₁, t₃ > t₂), morceau de liège en M (petit déplacement vertical sur
place). Questions : 1°) transversal/longitudinal ? 2°) combien de directions ? 3°) déplacement d'eau
depuis S ? Interprétation : « […] la propagation de ce dernier se fait avec une transmission d'énergie,
sans déplacement de matière. C'est pour cette raison qu'il est impropre de parler de déplacement d'un
ébranlement. »

**1.3 Milieu tridimensionnel (p.188)** — identique à 223433 p.194 (acteur au théâtre ; poste radio sous
cloche à vide ; questions : 1°) ébranlement sonore transversal ou longitudinal ? justifier ;
2°) le son se propage-t-il dans le vide ? justifier).

**1.4 Célérité d'un ébranlement (p.189–192)** — identique à 223433 p.195–198, valeurs relevées sur
l'image (p.190–191) : échelle de perroquet (Fig.4 photo, Fig.5 schéma, masselottes à 2 cm de l'axe) ;
tableau 1 : d (m) = 0,23 / 0,30 / 0,40 / 0,54 → v (m.s⁻¹) = 0,48 / 0,49 / 0,48 / 0,49 ; angle α′ > α :
valeurs « pratiquement les mêmes » ; tableau 2 (masselottes symétriques déplacées) : mêmes d → v =
0,28 / 0,29 / 0,28 / 0,28. Questions p.190 : 1°) célérité constante dans ces milieux homogènes (avec le
résultat du §1.2) ; 2°) la célérité dépend-elle a) de l'amplitude, b) des caractéristiques du milieu ?
Autres constatations p.191 : célérité croissante avec la tension du fil de torsion ; vitesse du son
dépendant de la compressibilité (« plus grande dans les solides que dans les liquides et les gaz ») ;
tableau (m.s⁻¹) : surface de l'eau 0,3 ; échelle de perroquet 1 ; corde 10 ; son dans l'air à 20 °C 342 ;
son dans l'eau à 20 °C 1500 ; son dans l'acier 5000 ; sismique 8000. Tableau « Remarque » mobile /
ébranlement (p.191–192) : trajectoire précise / toutes directions ; transport de matière / d'énergie ;
ralenti par les frottements / amorti surtout en amplitude plutôt qu'en célérité ; plus facile dans le
vide, impossible dans les solides / ne se propage pas dans le vide, plus vite dans les liquides que
dans les gaz et fréquemment plus vite dans les solides que dans les liquides ; vitesse dépendant des
conditions initiales (vitesse et accélération initiales) / célérité dépendant des propriétés du milieu.

**2.1 Généralités (p.192)** — identique à 223433 p.198 (houles, vagues, son, tremblements de terre ;
milieux finis limités par matière absorbante « coton, feutre, plaque métallique cintrée … »).

**2.2 Corde élastique tendue (p.193–199)** — identique à 223433 p.199–205 : mise en évidence (Fig.6 lame
vibrante – O – corde – A – pelote de coton ; « bandelette rectangulaire floue de largeur double de
l'amplitude de vibration de l'extrémité O » ; picotement ; questions 1°) 2°) 3°)) ; analyse optique
(Fig.7 : électro-aimant, lame, diaphragme en M, lentille L, source S, miroir tournant, écran à sinusoïde,
extrémité fixe A ; questions 1°) sinusoïde d'ombre 2°) mouvement d'un point vs O) ; aspect instantané au
stroboscope, Te = p.T (p ∈ N*) → sinusoïde immobile de période D (Fig.8), Te légèrement > p.T →
mouvement lent dans le sens réel, légèrement < p.T → sens contraire (Fig.9a/9b ; légende « Sens réel de
la prorogation » [sic]) ; étude théorique : repère (O, i⃗, j⃗), Fig.10, M d'abscisse x.
Questions du cours : p.198 « Déterminer les abscisses des points de la corde vibrant en opposition de
phase avec la source. » ; « Montrer que les points de la corde vibrant en quadrature retard de phase
par rapport à la source sont définis par leur position de repos d'abscisse x = (4k+1)λ/4, avec k ∈ N. »

**2.3 Ressort (p.199–200)** — identique à 223433 p.205–206 (ressort vertical, solide suspendu, extrémité
inférieure A dans un récipient d'eau, Fig.12 ; lumière ordinaire : flou ; Te = T : zones comprimées/dilatées
immobiles ; Te légèrement > T : progression lente de S vers A ; 5 questions ; onde **longitudinale** ;
non-équidistance des spires ; « Si ys(t) = a sin(ωt), on montre qu'en absence de tout amortissement :
yM(t) = a sin(ωt − 2πx/λ) »).

**2.4 Surface de l'eau (p.201–202)** — identique à 223433 p.207–208 (fourche à pointe unique, cuve à
ondes, Ne = N → rides circulaires immobiles (Fig.13), Ne légèrement diminuée → progression lente ;
questions 1°) célérité identique dans toutes les directions ? 2°) amplitude qui diminue avec la distance
sans frottement ; Fig.14 ; étude théorique : rides circulaires et transversales, points à même distance r de S en phase et de même amplitude, cercles concentriques équidistants de λ, régulièrement espacés de λ sous Ne = N ; remarque dilution d'énergie ; réglette → rides rectilignes, Fig.15).

**2.5 Le son (p.202–203)** — identique à 223433 p.208–209 (HP + GBF, microphone, oscilloscope bicourbe
voies Y₁/Y₂, (C₁), (C₂), Fig.16a/16b ; décalage horaire passant « régulièrement plusieurs fois de 0 à
T/2 » ; 4 questions, dont 4°) « longueur de déplacement du microphone […] au bout de laquelle le décalage
horaire […] varie de T/2 »).

### Encadrés, définitions et relations (VERBATIM, vérifiés sur l'image de leur page)

Tous identiques mot pour mot à ceux de la section 223433 §2.7 (même texte, même mise en page, lus sur
les images p.186, 189, 191, 192, 194, 196, 197, 198, 199, 202, 203, 204) ; seule la page change. Table :

- **Ébranlement / milieu élastique** (p.186, texte du corps, non encadré) — « La déformation de courte
  durée, imposée par le caillou à une nappe d'eau calme est un ébranlement. […] On appelle milieu
  élastique, tout milieu qui reprend de lui-même sa forme initiale après avoir subi une déformation
  brève. »
- **Conclusion 1.1–1.3** (p.189, encadré) — « Un ébranlement est une déformation de courte durée imposée
  localement à un milieu élastique. Le milieu de propagation d'un ébranlement peut être unidimensionnel
  (corde élastique, ressort), bidimensionnel (surface d'un liquide) ou tridimensionnel (l'air ou tout
  autre fluide). Selon sa direction de propagation et celle du déplacement des points matériels du milieu
  de propagation, un ébranlement peut être transversal ou longitudinal. La propagation d'un ébranlement
  est due à une transmission d'énergie d'un point du milieu de propagation vers d'autres. »
- **Célérité** (p.189, corps) — « La propagation d'un ébranlement se fait avec une vitesse v appelée
  vitesse de propagation ou célérité de l'ébranlement. Du fait que cette propagation ne correspond pas à
  un déplacement de matière mais plutôt à un transport d'énergie, la célérité v correspond à une vitesse
  de propagation de l'énergie. »
- **Conclusion 1.4** (p.191, encadré) — « La célérité d'un ébranlement dépend de la nature du milieu
  matériel dans lequel il se propage et de ses propriétés. Ainsi, le long d'une corde élastique, la
  célérité d'un ébranlement est d'autant plus grande que la corde est plus tendue. Plus l'inertie d'un
  milieu de propagation est grande, plus la célérité de l'ébranlement est faible... »
- **Définition (onde)** (p.192, encadré vert) — « On appelle onde (du latin unda) le phénomène résultant de
  la propagation d'une succession d'ébranlements dans un milieu donné. »
  **Célérité d'une onde mécanique** — « Comme dans le cas d'un seul ébranlement, l'onde est caractérisée
  par une célérité v (ou vitesse de propagation) qui dépend des propriétés du milieu élastique homogène.
  Plus précisément, la célérité d'une onde est celle des ébranlements qui la constituent. »
  **Onde transversale et onde longitudinale** — « Le caractère transversal ou longitudinal d'une onde est
  fonction de celui des ébranlements correspondants. Les ébranlements transversaux constituent des ondes
  transversales et les ébranlements longitudinaux constituent des ondes longitudinales. »
  **Ondes progressives** — « Lorsque le milieu de propagation est ouvert, c'est-à-dire illimité, les ondes
  progressent en s'éloignant indéfiniment de la source. De telles ondes sont dites progressives. »
- **Conclusion (corde)** (p.194, encadré) — « Les vibrations imposées à l'extrémité d'une corde élastique
  tendue sont transmises aux différents points de celle-ci. Le phénomène qui en résulte constitue une
  onde transversale. Au cours de la propagation d'une onde transversale sinusoïdale le long d'une corde
  élastique, chacun des points de cette corde (à part l'extrémité fixe A) vibre sinusoïdalement avec la
  même amplitude que la source (en négligeant l'amortissement). »
- **Double périodicité** (p.196, encadré) — « La propagation d'une onde est caractérisée par deux
  périodicités à la fois : - une périodicité dans le temps appelée périodicité temporelle. La période T
  est celle de la source. - une périodicité dans l'espace, appelée périodicité spatiale. La période
  spatiale λ, contrairement à la période T, ne dépend pas seulement de la source mais dépend aussi du
  milieu de propagation. La période spatiale λ est la longueur d'onde, elle représente la distance
  parcourue par l'onde pendant une durée égale à la période temporelle T.
  **λ = v.T , soit λ = v/N**
  En effet, la période temporelle T de l'onde est la durée au bout de laquelle l'onde se propage d'une
  longueur λ telle que tous les points du milieu de propagation se retrouvent dans le même état
  vibratoire, d'où le nom de longueur d'onde. »
- **Équation horaire d'un point de la corde** (p.197, vu sur l'image) — « A tout instant t, l'onde […]
  impose au point M une élongation y(t) égale à l'élongation qu'a eue l'extrémité source S à l'instant
  (t − θ), l'amortissement étant supposé nul. La durée θ désigne le temps mis par l'onde pour se
  propager de S à M. yM(t) = ys(t − θ) or ys(t) = a sin(ωt + φs). Avec un choix convenable de l'origine
  des temps, on aura φs = 0. ys(t) = a sin(ωt), d'où yM(t) = a sin ω(t − θ). θ = x/v ; v : célérité de
  l'onde et ω = 2π/T ; T : période de l'onde. Ainsi : yM(t) = a sin[2π(t/T − x/(vT))]. Or : λ = v.T :
  Longueur d'onde, d'où : yM(t) = a sin[2π(t/T − x/λ)]. »
- **Conclusion** (p.197, encadré) — « Au cours de la propagation d'une onde sinusoïdale entretenue le
  long d'une corde élastique, tout point M de la corde, d'abscisse x par rapport à la source, vibre
  sinusoïdalement avec une période T égale à celle de la source S, mais avec une phase initiale dont la
  valeur est fonction de sa position sur la corde, au repos. »
- **Déphasage par rapport à la source** (p.197) — « Si la source commence à vibrer à t = 0 en allant dans
  le sens positif des élongations, on a : ys(t) = a sin(ωt). yM(t) = a sin(ωt − 2πx/λ). C'est de la forme
  yM(t) = a sin(ωt + φM) avec φM = − 2πx/λ. Le déphasage entre les élongations yM(t) et ys(t), noté Δφ,
  est (φM − φs) ; Δφ = − 2πx/λ. »
  **Remarque** — « Ce résultat reste valable dans le cas général où l'amortissement n'est pas négligeable
  et où la phase initiale n'est pas nulle. ys(t) = aO sin(ωt + φs) ; yM(t) = a sin(ωt + φs − 2πx/λ) ;
  avec a < aO. Ainsi, Δφ est une fonction de l'abscisse x du point M par rapport à la source. »
  (Le manuel imprime « l'armortissement » [sic], couche texte et image.)
- **Points en concordance de phase avec la source** (p.198) — « ys(t)/as = yM(t)/a, soit :
  sin(ωt + φs) = sin(ωt − 2πx/λ + φs) ∀t, ce qui donne φs = φM + 2kπ ; avec φM = −2πx/λ + φs (k :
  entier), soit Δφ = − 2kπ, ce qui conduit à : x = kλ, où k est un entier positif. Soit ℓ la longueur de
  la corde au repos. On a : x < ℓ. Donc, k < ℓ/λ. Les points de la corde qui vibrent en phase avec la
  source sont situés au repos à des distances égales à un nombre entier de longueurs d'onde la source S.
  Leur nombre est limité par la longueur de la corde. »
- **Points en quadrature avance de phase avec la source** (p.198) — « Un point M de la corde vibre en
  quadrature avance de phase la source lorsqu'à tout instant t, son élongation est telle que :
  yS(t) = yM(t − T/4), soit : a sin(ωt + φs) = a sin[ω(t − T/4) + φM], ce qui donne
  φS = φM − π/2 + 2kπ, avec k un entier positif. D'où : Δφ = − (4k − 1)π/2, ce qui conduit à :
  x = (4k − 1)λ/4, avec k un entier positif. Les points de la corde qui vibrent en quadrature avance de
  phase par rapport à la source sont situés au repos à λ/4 ayant les points qui vibrent en phase avec la
  source. » [le mot « ayant » est bien imprimé tel quel, voir doutes]
- **Aspect de la corde à un instant t donné** (p.199) — « Pour un point M donné, à tout instant t :
  yM(t) = a sin(ωt − 2πx/λ) dans le cas où φs = 0, ce qui entraîne qu'à un instant t donné, on peut
  écrire : pour tout point M, yt(x) = a sin(2πx/λ − ωt + π). Ainsi, pour t donné, yt(x) est fonction
  sinusoïdale de x, de période λ et de phase initiale (− ωt + π). La courbe représentant yt(x) donne
  l'aspect de la corde à un instant t considéré (Fig.11). Elle est appelée par certains "sinusoïde des
  espaces". »
  **Remarque (front d'onde)** — « Si les vibrations de la source commencent à t = 0 et que l'instant t
  choisi est de l'ordre de quelques périodes seulement, il se peut qu'à cet instant l'onde n'a pas atteint
  encore l'autre extrémité de la corde. Il faut alors chercher la position xf du front d'onde. Pour ce, il
  suffit de calculer la distance parcourue par l'onde entre l'instant t = 0 et l'instant t choisi.
  xf = v.t , ce qui équivaut à : xf = n.λ, en posant n = t/T »
- **Remarque (surface de l'eau)** (p.202) — « L'amplitude des ondes qui progressent à la surface de l'eau
  décroît en s'éloignant de la source même si l'amortissement est supposé nul. Cette décroissance est due
  au fait que l'énergie mécanique cédée à l'onde par la source de vibrations se répartit de proche en
  proche sur une quantité de liquide de plus en plus grande quand elle progresse à la surface de l'eau.
  C'est le phénomène de dilution d'énergie. »
- **Conclusion (son)** (p.203, encadré) — « Le son est de nature vibratoire. C'est une onde mécanique,
  appelée onde sonore et plus particulièrement acoustique lorsqu'elle est susceptible d'être perçue par
  l'oreille de l'homme. L'onde sonore émise par une source ponctuelle (approximation du haut-parleur) est
  une onde progressive sphérique mais qui s'atténue en s'éloignant de la source à cause de la dilution
  de l'énergie. »
- **L'essentiel** (p.204, verbatim) — « ■ On appelle onde, le phénomène résultant de la propagation d'une
  succession d'ébranlements dans un milieu donné. ■ Une onde est dite transversale si la direction des
  déformations auxquelles elle est due est perpendiculaire à la direction de sa propagation. ■ Une onde
  est dite longitudinale si la direction des déformations auxquelles elle est due est parallèle à la
  direction de sa propagation. ■ La propagation d'une onde correspond à un transport d'énergie sans
  déplacement de matière. ■ La célérité (ou vitesse de propagation) d'une onde dépend de la nature du
  milieu de propagation et de ses propriétés. ■ Toute onde se propageant dans un milieu ouvert est
  progressive. Elle est caractérisée par une double périodicité spatiale et temporelle. ■ La période
  temporelle T de l'onde est liée à la période spatiale λ par la relation : [λ = v.T], avec v la célérité
  de l'onde. »

### Exercice résolu (p.205–207) — identique à 223433 p.211–213

**Énoncé** — Extrémité libre O d'une lame vibrant à N = 100 Hz ; corde élastique l = 0,6 m ; onde
progressive sinusoïdale transversale non amortie, a = 5 mm, phase initiale nulle, v = 12 m.s⁻¹.
1°) équation horaire de M au repos à x = 21 cm et comparaison avec la source ; 2°) diagrammes des
mouvements de la source et de M dans un même système d'axes ; 3°) lieu et nombre des points en
quadrature avance de phase ; 4°) aspect de la corde à t₁ = 3,25.10⁻² s, puis à t₂ = 3,75.10⁻² s.

**Solution (vue sur l'image p.205–207)** — 1°) yM(t) = y₀(t − θ), θ = x/v ; yM(t) = a sin(ωt − 2πx/λ),
φ = −2πx/λ ; λ = v/N, A.N. λ = 12 cm, φ = −7π/2 = (−4π + π/2) rad ; **yM(t) = 5.10⁻³ sin(200πt + π/2)** :
même amplitude, quadrature avance. 2°) M ne vibre qu'à partir de t₁ = θ = x/v ; x = 7λ/4, θ = 7T/4 =
1,75 T ; pour t < 7T/4, yM(t) = 0 ; pour t > 7T/4, yM(t) = a sin(ωt + π/2) ; diagramme de M = translation de
θ de celui de la source (graphe : source en noir de 0 à 4T, M en rose à partir de θ = 1,75 T). 3°) Δφ =
−2πx/λ = −(4k − 1)π/2 → **x = (4k − 1)λ/4** ; x ≤ l → k ≤ l/λ + 1/4 ; l/λ = 5 → k ≤ 5,25, k ∈ N* →
k ∈ {1, 2, 3, 4, 5} ; tableau x (cm) = 9 / 21 / 33 / 45 / 57 (M à 21 cm en fait partie). 4°) x₁ = v t₁ =
λ t₁/T, t₁/T = 3,25 → x₁ = 3,25 λ < l = 5λ : x₁ = position x_f1 du front ; pour x > x_f1, y = 0 (brin
F₁A au repos) ; pour x < x_f1, y_t1(x) = a sin(ωt₁ − 2πx/λ), ωt₁ = 6,5π rad → **y_t1(x) = a cos(2πx/λ)** ;
aspect à t₁ dessiné de 0 à x_f1 = 3,25 λ (A à 5λ). Remarques : M (x = 1,75 λ) a bien une élongation nulle
à t₁ = 3,25 T ; méthode rapide : extrapoler la sinusoïde de période λ depuis le front jusqu'à la source.
t₂ : (t₂ − t₁)/T = 1/2 → l'onde progresse de λ/2 ; **x_f2 = x_f1 + λ/2** = 3,75 λ ; aspect à t₂ (trait
plein) avec celui de t₁ (pointillés).

### Exercices à résoudre (p.208–214) — réponses du manuel p.319 (chap. 7)

(Le renvoi « p.318–320 » de la consigne : p.318 = réponses des chap. 1–6 partiels, p.319 = chap. 7 en
entier, p.320 = « Sites web intéressants » dont la rubrique « Ondes ». Seule p.319 porte le chap. 7.)

**Tests rapides des acquis (p.208)** — identiques à 223433 p.214 : **1** Vrai ou faux, 10 items (onde
mécanique dans le vide ; ébranlement transporte de l'énergie ; célérité indépendante du milieu ; onde
sonore dans le vide ; λ = distance parcourue pendant T ; propagation = déplacement de matière ; célérité
constante en milieu homogène ; onde à la surface d'un liquide transversale ; onde sonore longitudinale ;
mobile = matière / onde = énergie). **2** QCM : I. phénomène ondulatoire associé à un déplacement de
matière / d'énergie / des deux ; II. vitesse de l'ébranlement du caillou dépend de l'énergie initiale / la
taille / la profondeur de l'eau ; III. corde OA, N = 100 Hz, stroboscope Ne = 49 Hz : sinusoïde fixe /
lente de O vers A / lente de A vers O ; IV. N = 50 Hz, v = 0,25 m.s⁻¹, distance entre deux points en
phase : 5 / 10 / 15 mm. Pas de réponse p.319.

**Exercices d'application (p.209–210)** — identiques à 223433 :
- **3** : y = a sin(100πt), v = 10 m.s⁻¹, amortissement nul ; 1°) N, λ ; 2°) a) aspect à t₁ = 0,02 s et
  t₂ = 0,05 s (S part dans le sens positif à t = 0) ; b) état de M₁ (d₁ = 10 cm) et M₂ (d₂ = 40 cm) ;
  3°) aspect sous stroboscope Ne = 25, 49, 51 Hz. Rép. : N = 50 Hz, λ = 0,2 m ; M₁ et S en opposition
  de phase, M₂ et S en phase ; 25 Hz immobilité, 49 Hz ralenti sens réel, 51 Hz ralenti sens inverse.
- **4** : N = 50 Hz, a = 0,5 cm, départ de l'équilibre vers le haut, v = 1 m.s⁻¹, pas de réflexion ;
  1°) équation de S ; 2°) a) équation de M à d ; b) d = 3 cm, comparer ; 3°) courbes yS(t), yM(t) ;
  4°) aspect à t₁ = 0,03 s et t₂ = 0,035 s. Rép. : yS = 5.10⁻³ sin100πt ; yM = 5.10⁻³ sin(100πt − 2πd/λ) ;
  d = 3 cm : yM = 5.10⁻³ sin(100πt − π).
- **5** : N = 100 Hz, a = 5 mm, corde très longue ; départ de l'équilibre sens positif ; à t = 6,5.10⁻² s
  M (x = 32,5 cm) entre en vibration ; 1°) a) v ; b) λ ; 2°) a) équation de M ; b) graphe de 0 à 0,1 s ;
  c) instants d'élongation maximale, premier instant t₀. Rép. : v = 5 m.s⁻¹ ; λ = 5.10⁻² m ;
  yM = 2.10⁻³ sin(200πt − π) [amplitude 2.10⁻³ imprimée, voir doutes] ; t = 6,75 T + kT.
- **6** : N = 50 Hz, source S, t₀ = 0, surface de l'eau ; coupe à t₁ (sinusoïde de A à B, S au milieu,
  yS(t₁) = 0), AB = 3,0 cm, amplitude 4 mm ; 1°) λ ; 2°) v ; 3°) t₁ ; 4°) ys(t) ; 5°) nombre de points en
  opposition de phase avec S à t₁, schéma ; 6°) coupe à t₂ = 6,25.10⁻² s. Rép. : λ = 5.10⁻³ m ;
  v = 0,25 m.s⁻¹ ; t₁ = 6.10⁻² s ; yS = 4.10⁻³ sin(100πt + π) ; points sur les cercles de rayons λ/2,
  3λ/2, 5λ/2.

**Exercices de synthèse (p.210–214)** — numérotation 7 à 14 identique à 223433 ; **l'exercice 15 de
223433 (source ponctuelle, coupe à t₁ = 0,2 s) est ABSENT** ; l'étude de texte (ex.16 de 223433) devient ici
l'**exercice 15**.
- **7** : cuve à ondes, source ponctuelle en O (amplitude a, fréquence N), bords absorbants, sans
  amortissement ; Fig.1 photo de rides, A et B sur deux crêtes ; Fig.2 : yM(t) (échelles 2.10⁻³ m et
  5.10⁻³ s) ; 1°) a) rides immobiles ; b) d = 24 mm → λ ; 2°) a) yM(t) ; b) v ; c) yO(t) ; 3°) coupe selon
  x′x à t₀ = 0,045 s ; 4°) points en phase avec S à t₀. Rép. : λ = 8.10⁻³ m ; yM = 2.10⁻³ sin(100πt) ;
  v = 0,4 m.s⁻¹ ; yO = 2.10⁻³ sin(100πt + π) ; deux cercles de rayons λ et 2λ.
- **8** : lame en S, corde sur poulie + solide suspendu, dispositif absorbant côté poulie ; ys(t) =
  a sin(ωt + φ), a = 3 mm, démarrage t₀ = 0 ; 1°) a) éclairage continu ; b) stroboscope Ne légèrement < N ;
  2°) Fig.2 : aspect à t₁ = 0,025 s, front en A, OA = 0,75 m : a) λ, v, N ; b) équation de S ; c) yA(t) ;
  d) graphe. Rép. : λ = 0,3 m ; v = 30 m.s⁻¹ ; N = 100 Hz ; yS = 3.10⁻³ sin(200πt) ; yA = 3.10⁻³ sin(200πt − π).
- **9** : I- corde de longueur infinie, vibrations dès t = 0, sans amortissement ; courbes (I) (diagramme d'un
  point A ; 1 div → t = 2,5.10⁻³ s) et (II) (aspect à t₁ ; 1 div → x = 5 cm), amplitude lue 4 mm ;
  1°) identifier (I) et (II), T, λ, a ; 2°) v, xA, t₁ ; 3°) équations de S et A ; 4°) a) aspect à
  t₂ = 2,5.10⁻² s ; b) points d'élongation (−a/2) se déplaçant dans le sens négatif ; c) nombre et
  abscisses des points en quadrature retard. II- pointe S, point O de l'eau, yO(t) = 10⁻³ sin(628t) :
  1°) yM(t), OM = x ; 2°) v sachant que la plus petite distance entre deux points en quadrature est
  d = 1 mm ; 3°) coupes à t₂ = 0,035 s et t₃ = 0,040 s ; 4°) fréquence des éclairs pour l'immobilité, la
  plus grande ; un éclair de moins par seconde → sens apparent. Rép. : T = 0,01 s ; λ = 0,2 m ;
  v = 20 m.s⁻¹ ; xA = 0,40 m ; t₁ = 0,02 s ; yS = 4.10⁻³ sin(200πt), yA = 4.10⁻³ sin(200πt) ;
  4°c) 3 points x = 5λ/12 + kλ (k = 0, 1, 2) ; II : yM = 10⁻³ sin(628t − 2πx/λ) ; v = 0,4 m.s⁻¹ ;
  immobilité Ne = N/k, k = 1 : Ne = N = 100 Hz.
- **10** : corde L = 2 m, force de tension et coton à l'autre extrémité ; lame part de l'équilibre à t = 0 ;
  Fig.1 : yM1(t) (cm ; t en 10⁻² s ; départ vers 5,5, amplitude 0,5) ; Fig.2 : aspect à t₀ (x en 10⁻¹ m,
  front vers 5,5) ; 1°) a) N, λ ; b) v ; c) x₁ et t₀ ; 2°) mouvements de S et M₁ ; 3°) instants où M₁ passe
  par 2,5.10⁻³ m dans le sens positif entre 0 et 0,14 s ; 4°) abscisses des points à 2,5.10⁻³ m allant
  dans le sens négatif à t₀. Rép. : N = 50 Hz ; λ = 0,2 m ; v = 10 m.s⁻¹ ; x₁ = 0,55 m ; t₀ = 0,055 s ;
  S et M₁ en quadrature ; t = (6,75.10⁻² + 0,02k) s, t₁ = 6,75.10⁻² s ; 3 points x = λ/8 + kλ
  (k = 0, 1, 2).
- **11** : deux microphones M₁, M₂ sur l'axe d'un HP, d = 34 cm, N = 2000 Hz, v = 340 m.s⁻¹, écran 10 × 8
  divisions ; 1°) a) base de temps pour 2 périodes ; b) pourquoi l'amplitude voie 2 < voie 1 ;
  c) oscillogramme ; 2°) a) N = 1 kHz, d = 17 cm : oscillogramme ; b) M₂ éloigné, oscillogramme analogue à
  1° : d et nouvelle base de temps. Rép. : 10⁻⁴ s/div ; dilution de l'énergie ; d = 34 cm, 2.10⁻⁴ s/div.
- **12** Mesure de la célérité d'une onde sonore : micros M₁, M₂ sur YA, YB (Fig.1 : GBF, HP, règle,
  oscilloscope) ; 2 périodes sur 10 div, 0,4 ms/div ; positions successives en phase x₂ (cm) = 68,0 /
  136,0 / 204,0 / 272,0 / 340,0 ; 1°) fréquence ; 2°) λ ; 3°) v. Rép. : N = 500 Hz ; λ = 0,68 m ;
  v = 340 m.s⁻¹.
- **13** : HP et micro M (figure de branchement) ; 1°) tensions visualisées ; 2°) fréquence (2 périodes,
  10 div, 0,2 ms/div) ; 3°) positions en phase x₁ = 4,5 cm, x₂ = 38,5 cm : λ ; 4°) v. Rép. (étiquetées b,
  c, d) : N = 1000 Hz ; λ = 0,34 m ; v = 340 m.s⁻¹.
- **14** : GBF N = 1,47 kHz sur voie A, micro à d du HP sur voie B (Fig.1 schéma ; Fig.2 oscillogramme de
  deux sinusoïdes décalées) ; 1°) a) durée de balayage ; b) décalage θ, temps de propagation en fonction
  de θ et N ; 2°) k = 100 mV/div : amplitudes, pourquoi différentes ; 3°) d₂ − d₁ = 23,0 cm (deux positions
  successives en phase) : λ et v ; 4°) d entre 40 et 60 cm : valeur ; 5°) la célérité change-t-elle avec la
  fréquence ? Rép. : « T ≃ 68 ms » [?], s ≃ 0,1 ms/div ; θ ≃ 0,15 ms, Δt = n.T + θ = n/f + θ ;
  UR = 300 mV, UB = 250 mV ; λ = d₂ − d₁ = 23 cm, v = λ.f = 338 m.s⁻¹ ; d = v.Δt = v(n/f + θ) =
  λ.n + λ.f.θ = 23.n + 5,1 (cm), d = 51,1 cm ; « Célérité constante, l'air est un milieu non dispersif. »
- **15 (= ex.16 de 223433)** Étude de texte « Quand la Terre tremble... » (d'après « La Recherche » ;
  d'après un sujet de baccalauréat, session principale de juin 2009), texte identique à 223433 : ondes P
  (compression-détente « à la manière d'un accordéon », ~6 km.s⁻¹ dans la croûte) et ondes S (cisaillement,
  « deux fois plus lentes mais environ cinq fois plus fortes ») ; amortissement en s'éloignant du foyer ;
  1°) deux passages où l'auteur confond vibrations et ondes ; 2°) phrase montrant le caractère
  transversal/longitudinal de S et P ; 3°) pourquoi les ondes S nous secouent horizontalement. Pas de
  réponse p.319.

### Fiches techniques et « En savoir plus »

- **Fiche technique n°1** (p.215) — identique à 223433 p.222 : méthode d'analyse optique d'un phénomène
  périodique (diaphragme unifente F au niveau de M, faisceau parallèle, ombre de M réfléchie par un miroir
  tournant à vitesse constante → sinusoïde sur l'écran (E) ; Fig.1 = Fig.7).
- **Fiche technique n°2** (p.216) — identique à 223433 p.223 : stroboscopie (éclairs de période Te, fréquence
  Ne ; persistance rétinienne 0,1 s, intérêt au-delà de 10 Hz ; disque à pastille noire à 20 tr.s⁻¹ éclairé à
  Ne = 20 Hz → immobile, Fig.2 t = 0 s, T, 2T, 3T) ; « Il y a immobilité apparente chaque fois que :
  Te = k T (avec k un entier naturel) » ; ralenti apparent dans le sens réel si Te très légèrement
  supérieure à T (ou kT), sens contraire si très légèrement inférieure à T (ou kT).
- **En savoir plus (p.217) — DIFFÉRENT de 223433** : « L'énergie et la houle » (Encyclopédie « Science et
  Vie »). Le vent crée des vagues ; succession de vagues régulières = la houle ; caractérisée par sa
  « hauteur » H (m), sa période T (s) et sa longueur d'onde λ (schéma H et L). « Une houle courte de période
  3 secondes et de hauteur 0,6 mètres a une puissance de 1 kW. La puissance d'une houle longue avec
  H = 7,5 m et T = 11 s est à peu près 600 fois plus élevée que celle de cette houle courte. » « Houlomotrices »
  (captage de l'énergie des vagues) : forme dégradée de l'énergie éolienne, donc moins dense, mais
  propagation sur de très longues distances sans trop de perte ; étude de la fin des années 1970 en France :
  en moyenne 30 kW/m aux endroits les plus exposés, 10 à 20 kW/m ailleurs ; projet d'usine houlomotrice en
  Espagne ; « pas encore de technologie gagnante (winning technology) ». Lecture culturelle, aucune
  question ni calcul exigible.

### Écart avec Sciences expérimentales

**Ce que le manuel Mathématiques AJOUTE**
- Notions : AUCUNE notion de cours ajoutée (cours §1–2, définitions, relations, L'essentiel : identiques).
- Activités : AUCUNE activité ou manipulation ajoutée.
- Exercices : AUCUN exercice ajouté (aucune valeur numérique nouvelle dans ex.1–14, exercice résolu inclus).
- Seul ajout de contenu : la page **En savoir plus « L'énergie et la houle »** (p.217), lecture culturelle
  (puissance de la houle, houlomotrices) — aucune relation, aucun exercice, hors scope d'évaluation ;
  elle fait écho à la question d'accroche « D'où provient l'énergie des vagues ? ».

**Ce que le manuel Mathématiques RETIRE (par rapport à 223433)**
- L'ouverture de partie « ONDES ONDES ONDES » (223433 p.188–189 : photos, sommaire de partie) ; le chapitre
  s'ouvre directement sur Objectifs/Prérequis.
- L'**exercice 15** de 223433 (source ponctuelle S, Ym = 3 mm, ys(t) = Ym sin(2πNt + π), coupe à t₁ = 0,2 s,
  points A et B ; sans réponse imprimée) : absent ; l'étude de texte passe du n°16 au **n°15**.
- La page « En savoir plus » de 223433 (p.224–225, techno-science.net : vitesses de phase et de groupe,
  vecteur d'onde k, Fourier, onde solitaire, onde de choc…) est REMPLACÉE par « L'énergie et la houle ».
- Conséquence : 223433 compte 10 exercices de synthèse (7–16), 223432 en compte 9 (7–15) ; le total
  d'exercices à résoudre passe de 16 à 15 (+ l'exercice résolu).
- Pagination : chapitre p.184–217 (34 p.) au lieu de p.188–225 (38 p.) ; réponses p.319 au lieu de p.317.

**Identique mot pour mot** (relevé page par page, couche texte puis image) : objectifs, prérequis,
introduction, 1.1 à 1.4 (tableaux de l'échelle de perroquet 0,48/0,49/0,48/0,49 et 0,28/0,29/0,28/0,28 ;
tableau des célérités ; tableau mobile/ébranlement), 2.1 à 2.5, tous les encadrés, L'essentiel, l'exercice
résolu et sa solution, tests rapides, ex.3–14 (énoncés et réponses p.319), étude de texte, fiches
techniques n°1 et n°2. Seules différences constatées au niveau du texte brut : le rendu des glyphes de
formules par pdftotext (p.184, 197–200, 205–206) ; non pertinent, résolu sur l'image.

### Bornes de scope — section Mathématiques (ce manuel : 223432P00)

✅ **Inclus** (identique à la section Sciences expérimentales ; tout ce qui figure ci-dessus)
- Notions : ébranlement ; milieu élastique ; milieu de propagation uni-, bi-, tridimensionnel ;
  ébranlement/onde transversal(e) et longitudinal(e) (corde, ressort, surface de l'eau, son, ondes
  sismiques P/S en étude de texte) ; transport d'énergie sans transport de matière ; pas de propagation
  mécanique dans le vide ; célérité, constante en milieu homogène, indépendante de l'amplitude, dépendante
  du milieu (tension, inertie, compressibilité ; ordres de grandeur du tableau p.191) ; différences mobile /
  ébranlement ; onde = succession d'ébranlements ; onde entretenue, onde progressive (milieu ouvert,
  matière absorbante) ; double périodicité, T (source) et λ (source + milieu) ; λ = v.T = v/N ; dilution
  d'énergie ; rides circulaires et rectilignes ; onde sonore progressive sphérique ; air milieu non
  dispersif (réponse ex.14).
- Méthodes/calculs : yM(t) = ys(t − θ), θ = x/v ; yM(t) = a sin(ωt + φs − 2πx/λ) ; Δφ = −2πx/λ ; points en
  phase (x = kλ), en opposition (question du cours p.198), en quadrature avance (x = (4k − 1)λ/4) et retard
  (x = (4k + 1)λ/4, question p.198) ; dénombrement avec x ≤ l ; diagramme du mouvement d'un point
  (translation de θ, y = 0 avant l'arrivée du front) ; aspect yt(x) = a sin(2πx/λ − ωt + π), front d'onde
  xf = v.t = n.λ, extrapolation depuis le front, aspect à t₂ déduit de t₁ ; coupe de la surface de l'eau ;
  lecture de λ, T, amplitude, v sur diagramme temporel et aspect spatial ; instants d'élongation donnée
  dans un sens donné ; stroboscopie (Te = kT, Ne = N/k immobilité ; Te légèrement >/< kT ralenti sens
  réel/inverse ; persistance rétinienne 0,1 s) ; mesure de λ et v du son par positions successives en
  phase d'un micro ; lecture d'oscillogramme (base de temps, sensibilité, décalage θ, Δt = nT + θ).
- Appareillage : corde + lame vibrante/électro-aimant + pelote de coton ; ressort vertical + récipient
  d'eau ; échelle de perroquet + capteurs + mesureur de vitesse ; cuve à ondes, fourche à pointe, réglette ;
  stroboscope électronique ; analyse optique (diaphragme, miroir tournant) ; GBF, HP, microphone(s),
  oscilloscope bicourbe.

⛔ **Exclu** (absent du chapitre 7 de 223432, ou cantonné à la lecture culturelle p.217)
- Diffraction, réflexion, réfraction, dispersion d'ondes mécaniques, milieu dispersif / non dispersif
  comme notion de cours, nature ondulatoire de la lumière : objet du chapitre 8 « Interactions onde -
  matière » (p.218, objectifs : diffraction, rapport λ/a, réflexion/réfraction/dispersion mécaniques,
  lumière blanche, milieu dispersif) — hors de cette section ; ondes électromagnétiques.
- Réflexion, ondes stationnaires, interférences (les dispositifs absorbants les évitent).
- Formule quantitative de la célérité (v = √(F/μ) ou autre) : dépendance seulement qualitative.
- Calculs d'énergie, de puissance ou de rendement de la houle (p.217 : chiffres cités à titre culturel
  seulement : 1 kW, ≈ 600 fois, 30 kW/m, 10–20 kW/m, H = 7,5 m, T = 11 s) ; énergie transportée calculée,
  intensité sonore, décibels, effet Doppler, hauteur/timbre ; amortissement quantitatif (seule la
  remarque a < aO).
- Vitesse de phase/de groupe, vecteur d'onde, séries de Fourier, onde solitaire, onde de choc : absents de
  ce manuel (ils n'étaient que dans le « En savoir plus » de 223433 remplacé ici).
- Ondes sismiques au-delà de l'étude de texte (pas de calcul de distance à l'épicentre).

### Lecture

- **Couche texte** (pdftotext -layout) : p.184–217 en entier (34 pages), réponses p.317–320 (chap. 7 en p.319 ;
  p.318 = chap. 1–6, p.320 = sites web). Comparaison mécanique mot à mot avec 223433 p.190–223 : écarts
  nuls sauf glyphes de formules et les différences listées plus haut (ex.15, En savoir plus, ouverture
  de partie).
- **Pages vues sur l'image** (**35**) : 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197
  (r140), 198 (r140), 199 (r140), 200, 201, 202, 203, 204, 205 (r140), 206 (r140), 207, 208, 209, 210,
  211 (r140), 212 (r140), 213, 214 (r140), 215, 216, 217, 319 (r140). Toutes les pages du chapitre ont donc
  été vues sur l'image (pas seulement les pages à formule) ; aucune page lue en couche texte seule.
- **Sondage image (≥ 1/10, pages les plus denses)** : p.197, 198, 199, 205, 206, 207, 214, 319 (formules,
  solution complète, réponses). Écarts texte/image constatés : couche texte inutilisable pour toutes les
  formules de p.184, 197–200 et 205–206 (ω, θ, φ, π, λ, fractions, indices perdus : « yM (t ) = a sin(t  ) »,
  « Δ = - (4k - 1) ») ; **p.207 : la couche texte ne contient que « λ 2λ 3λ λ »** alors que l'image porte
  la fin de la solution (aspects à t₁ et t₂, x_f2 = x_f1 + λ/2, remarques) ; p.198 « x < l.. » / « ℓ » et
  « λ/4 ayant » ; p.319 « Tb 68 ms », « θ b 0,15 ms » = « ≃ » sur l'image ; tableaux p.190–191 corrects en
  texte ; figures p.210–214 (sinusoïdes, échelles, oscillogramme, schéma de branchement) absentes du texte.
- **Valeurs numériques vérifiées sur l'image identiques à 223433** : tableaux p.190–191 ; exercice résolu
  (λ = 12 cm, x = 9/21/33/45/57 cm, 3,25 λ, 3,75 λ) ; ex.7 échelles 2.10⁻³ m et 5.10⁻³ s ; ex.9 échelles 2,5.10⁻³ s
  et 5 cm ; ex.12 tableau 68,0…340,0 cm ; ex.13 x₁ = 4,5 cm, x₂ = 38,5 cm ; ex.14 d₂ − d₁ = 23,0 cm ;
  réponses p.319 ligne à ligne.
- **Doutes [?]**
  1. p.198 : « situés au repos à λ/4 **ayant** les points qui vibrent en phase » — mot imprimé tel quel
     (probablement « avant »), à ne pas citer comme règle.
  2. Ex.5 : énoncé a = 5 mm, réponse p.319 yM(t) = **2.10⁻³** sin(200πt − π) — incohérence d'amplitude du
     manuel.
  3. Ex.14 1°a : réponse « T ≃ 68 ms » alors que N = 1,47 kHz (T ≈ 0,68 ms) ; la question demande la « durée
     de balayage » — réponse probablement fautive ou mal libellée .
  4. Ex.13 : réponses étiquetées b), c), d) pour des questions numérotées 2°, 3°, 4°.
  5. Ex.7 : source en O dans l'énoncé puis « provenant de S » et « source S » ; ex.10 note la longueur d'onde
     « l » ; ex.9 II-2° la note « d » pour la plus petite distance en quadrature.
  6. Pas de réponses imprimées pour les ex.1, 2, 15 (étude de texte) et plusieurs sous-questions (ex.3 2°a et
     4°, ex.4 3°–4°, ex.6 6°, ex.7 3°, ex.8 1° et 2°d, ex.9 4°a–b et II-3°).
  7. QCM 2-III (N = 100 Hz, Ne = 49 Hz) : non corrigé ; à résoudre avec la règle Te légèrement > kT (sans
     réponse imprimée) ; le même cas est corrigé à l'ex.3 3° (49 Hz : ralenti dans le sens réel).
  8. Coquilles d'impression (non corrigées dans les citations) : « unidimentionnel », « verticlament »,
     « prorogation », « tridimentionnel », « sebleraient », « abcisse », « mouvents », « négtaif », « intant »,
     « longtitudinale », « horizontalment », « oscillospcope », « blilité », « armortissement ».
  9. Ex.10 énoncé « 4°) […] se déplaceront dans le sens négtaif […] à l'intant to » : coquilles seulement.

## 2.8 Chapitre 8 — Interactions onde-matière ; nature ondulatoire de la lumière (manuel 223432, p.218–247)

Section différentielle : référence = `bac-sciences-exp/physique.md` §2.8 (manuel 223433, p.226–243). « Identique à 223433 p.X »
signifie texte vérifié mot à mot par comparaison de couches texte (diff) ; les valeurs, figures et formules ont été relues sur
l'image du manuel 223432. Pagination : page PDF = page imprimée.

**Titrage du manuel** : page d'ouverture p.219 « NATURE ONDULATOIRE DE LA LUMIÈRE 8 » ; entête courant et titre du corps
(p.220) « Interactions onde-matière » (Ondes • Interactions onde-matière). Les deux titres désignent le même chapitre.

**Objectifs (p.218, verbatim, vus sur l'image)** — « ◆ Justifier le caractère ondulatoire de la lumière à partir d'expériences de
diffraction d'ondes mécaniques et d'ondes lumineuses. ◆ Préciser l'influence, sur le phénomène de diffraction, du quotient λ/a (λ
étant la longueur d'onde et a la largeur de la fente). ◆ Réaliser des expériences de réflexion, de réfraction et de dispersion
d'ondes mécaniques. ◆ Montrer que la lumière blanche est constituée d'une infinité de radiations monochromatiques. ◆ Distinguer
un milieu dispersif d'un milieu non dispersif. » (223433 : la troisième puce est « Réaliser des expériences de dispersion des ondes lumineuses ».)

**Prérequis (p.218)** — SAVOIR : « Définir une onde mécanique rectiligne. » ; « Définir la réflexion et la réfraction de la lumière. » ;
« Enoncer les lois de Descartes relatives à la réflexion et à la réfraction de la lumière. » ; « Définir le phénomène de dispersion de
la lumière blanche. » SAVOIR FAIRE : « Reconnaître une onde mécanique rectiligne. » ; « Utiliser un stroboscope. » ; « Mesurer la
longueur d'onde λ d'une onde plane progressive. » ; « Utiliser une source Laser. » ; « Appliquer le lois de Descartes relatives à la
réflexion et à la réfraction de la lumière. » ; « Reconnaître le phénomène de dispersion de la lumière blanche. »
(223433 : prérequis réflexion/réfraction/Descartes absents.)

**Page d'ouverture (p.219)** — photo d'arbre à contre-jour (légende : « Les rayons solaires donnent, à travers les branches
d'arbres, une lumière diffusée dans toutes les directions. »). Questions d'accroche (verbatim) : « ◆ Qu'est-ce qui fait que le son
puisse contourner les corps de dimensions habituelles ? ◆ Comment une chauve-souris peut-elle détecter un papillon nocturne dans
l'obscurité totale ? ◆ Comment un papillon nocturne peut-il neutraliser le système de détection d'une chauve-souris ? » (≠ 223433 :
holographie / papillon bleu / laser sur un cheveu.) Aucune réponse dans le chapitre à ces questions.

**Plan du chapitre** (titres numérotés) : introduction (p.220) · **1. La diffraction** (1.1 d'une onde mécanique p.220–221 ; 1.2 de la
lumière p.221–223 avec « Caractéristiques d'une onde lumineuse » ; 1.3 Influence du quotient λ/a p.223–226 — onde mécanique,
onde lumineuse) · **2. La réflexion** (2.1 d'un ébranlement p.226–227 ; 2.2 d'une onde p.228–230 — onde plane, onde sphérique) ·
**3. La réfraction d'une onde mécanique** (3.1 l'onde transmise p.230–231 ; 3.2 l'onde réfractée p.231–233) · **4. La dispersion**
(4.1 de la lumière p.234–235 ; 4.2 des ondes mécaniques p.235–236 ; 4.3 milieu dispersif et non dispersif p.237–238) · L'essentiel
(p.239) · Exercices : exercice résolu (p.240–241), tests rapides (ex.1–2, p.242), exercices d'application (ex.3–8, p.243–244),
exercices de synthèse (ex.9–14, p.244–246) · En savoir plus (p.247). Réponses : p.319 (colonne « Chapitre 8 », sous les chap. 7 ; bas
de la colonne gauche, suite en haut de la colonne droite). Pas de fiche technique dans ce chapitre.

**Introduction (p.220)** — identique à 223433 p.228 (mot à mot).

### Cours — Activités / manipulations

**1.1 Diffraction d'une onde mécanique (p.220–221)** — identique à 223433 p.228–229 : cuve à ondes, lame L, ouverture F de largeur a ;
a = 4 cm (rides rectilignes, légère déformation aux bords, Fig.2a « a > λ ») ; a = 1,5 cm (rides circulaires dans une zone
triangulaire de sommet I, Fig.2b « a ≃ λ ») ; a = 0,5 cm (rides quasi circulaires de centre I, Fig.2c « a < λ ») ; mêmes 4 questions ;
même interprétation (onde rectiligne → circulaire de même λ ; onde diffractée) ; même remarque Fig.3 (obstacle) ; même
Conclusion (cf. encadrés).

**1.2 Diffraction de la lumière (p.221–223)** — identique à 223433 p.229–231 : laser rouge λ = 633 nm, écran à une distance d ;
fente rectangulaire de largeur a réglable ; a = 0,6 mm (figure étalée horizontalement, tache centrale L la plus brillante) ;
a = 0,3 mm (L' = 2 L) ; remarques (obstacle ; fente circulaire → anneaux de diffraction, Fig.4c) ; mêmes 5 questions ; même
interprétation (met en défaut la propagation rectiligne ; figure de diffraction, tache centrale de largeur L, franges de
diffraction ; L augmente quand a diminue ; symétries de la fente) ; même Conclusion et mêmes « Caractéristiques d'une onde
lumineuse » (c = 3.10⁸ m.s⁻¹ ; λ vide = c.T ; air ≈ vide).

**1.3 Influence du quotient λ/a (p.223–226)**
- **Onde mécanique (p.223–224)** — identique à 223433 p.231–232 (a = 1,5 cm fixe ; e₁ puis e₂ = 3.e₁ ; Fig.5a « a ≃ λ », 5b
  « a < λ » ; 3 questions ; « λ augmente avec la profondeur de l'eau » ; « d'autant plus marqué que λ est plus grande »). **Une
  seule variante** : Conclusion p.224 « tant que la valeur de a est **grande** devant celle de λ » (223433 : « très grande »).
- **Onde lumineuse — manipulation (p.224)** : D = 2 m, papier millimétré ; L = distance entre les milieux des bandes sombres qui
  entourent la tache centrale (Fig.6b : angle θ, demi-largeur angulaire de la raie centrale, I au centre de la fente, L à l'écran).
  **Tableaux 1 et 2 : mêmes mesures qu'en 223433 mais avec une ligne 1/a en plus** — a (10⁻³ m) 0,10 / 0,15 / 0,20 / 0,25 / 0,30 ;
  1/a (10³ m⁻¹) 10,0 / 6,7 / 5,0 / 4,0 / 3,3 ; L rouge λR (10⁻³ m) 25 / 17 / 12 / 10 / 8 ; L vert λV (10⁻³ m) 21 / 14 / 10 / 8 / 7.
- **Fig.7 (p.225)** : courbes L (10⁻³ m) en fonction de 1/a (10³ m⁻¹), deux droites issues de l'origine, λR au-dessus de λV
  (rouge atteint 25 pour 1/a = 10 ; vert ≈ 21).
  **Questions (p.225), verbatim (orthographe du manuel)** : « 1°) La largeur a de la fente a-t-elle une inflence sur la largeur L de
  la tache centrale de diffraction ? 2°) Par exploitation des courbes de la figure 7, donner une relation simple entre L et a.
  3°) A partir de la figure 6b, montrer que l'angle θ correspondant à la demi-largeur angulaire de la raie centrale est donné par la
  relation : θ = L/2D. 4°) Préciser la variation de L et par suite celle de θ en fonction de la longueur d'onde λ. »
- **Interprétation (p.225–226) — NOUVEAU par rapport à 223433, quantitatif** : « L'étude expérimentale […] montre que la largeur L
  de la tache centrale […] dépend de la largeur a de la fente F. La droite linéaire représentant L en fonction de l'inverse de a
  (Fig.7) montre que : L = k/a, avec k une constante positive. De plus, la pente de la droite obtenue avec le laser rouge est plus
  grande que celle de la droite obtenue avec le laser vert. Donc, le coefficient k augmente avec λ. On montre théoriquement,
  qu'avec une fente rectangulaire, on a : k = 2Dλ. Cette relation peut être vérifiée par le calcul de la pente de chacune des deux
  droites de la figure 7 sachant que λR = 633 nm et λV = 532 nm. De ce fait, la largeur L de la tache centrale de la figure de
  diffraction s'écrit : L = 2Dλ/a. Par recours à la construction schématique de la figure 6b, la demi-largeur angulaire s'écrit :
  tan θ = L/2D. La distance D étant très grande devant la largeur L de la tache centrale, θ reste très faible. Donc, on peut
  assimiler, avec une bonne approximation, sa valeur à celle de sa tangente. Par suite, on a : θ = L/2D. Or, L = 2Dλ/a, d'où :
  θ = λ/a, ce qui signifie que la diffraction est d'autant plus marquée avec une tache centrale plus large que le rapport
  θ = λ/a est plus grand. » (vu sur l'image à 200 dpi). La phrase fautive de 223433 (« L est d'autant plus grande que λ est plus
  petite ») n'existe pas ici : conclusion cohérente (k augmente avec λ).

**2.1 Réflexion d'un ébranlement (p.226–227)** — NOUVEAU. Ondoscope d'extrémités A et B ; ébranlement d'amplitude a (une torsion)
appliqué en A, se propage vers B. (i) B libre : ébranlement réfléchi vers A (Fig.8a, même sens de déformation) ; (ii) B fixe :
ébranlement réfléchi de sens contraire (Fig.8b). Questions : 1°) expliquer l'apparition des ébranlements de B vers A ; 2°) comparer
l'ébranlement A→B et B→A : a) amplitude, b) direction et sens du déplacement, c) signe de l'élongation.
Interprétation : ébranlement incident (1) / réfléchi (2) ; « Un ébranlement réfléchi est caractérisé par : une amplitude
comparable à celle de l'ébranlement incident ; le même sens de déformation […] lorsqu'il apparaît au niveau d'une extrémité libre
et un sens de déformation contraire […] quand il se manifeste au niveau d'une extrémité fixe. »

**2.2 Réflexion d'une onde (p.228–230)** — NOUVEAU.
- **Onde plane (p.228–229)** : cuve à ondes, lame L parallèle à un bord, plaque plastique triangulaire P partiellement immergée
  (Fig.9a), rides rectilignes incidentes et réfléchies (Fig.9b, 9c : S, I, N, R). Questions : 1°) P absorbe-t-elle les ondes ?
  2°) repérer onde incidente / réfléchie sur la Fig.9b ; 3°) la réflexion modifie-t-elle λ ? 4°) mesurer i = (SI, IN) et
  i' = (RI, IN) et comparer. Interprétation : λ' égale à λ, direction de propagation différente.
- **Onde sphérique — onde sonore (p.229–230)** : émetteur E (haut-parleur) relié à un générateur BF (signal de haute fréquence ;
  onde sonore sensiblement unidirectionnelle), récepteur R (microphone) relié à un oscilloscope, plaque de polystyrène = écran
  absorbant, côté lisse d'un obstacle plan (Fig.10) ; i = (EI, IN) = 30° fixé, i' = (RI, IN) varie ; amplitude U de la tension :
  i' (°) 0 / 5 / 15 / 20 / 25 / 30 / 35 / 40 / 45 / 55 / 60 / 70 / 80 / 90 ↔ U (mV) 0,48 / 0,60 / 0,78 / 0,84 / 0,90 / 0,92 / 0,89 /
  0,85 / 0,78 / 0,59 / 0,49 / 0,38 / 0,16 / 0,10 (maximum 0,92 mV pour i' = 30°). Remarque : « Pour limiter le phénomène de
  diffraction, il faut travailler avec des fréquences de l'ordre du mégahertz. » Questions : 1°) l'obstacle modifie-t-il la
  direction de propagation de l'onde incidente ? 2°) forme de l'onde reçue par R, justifier ; 3°) valeur de i' donnant
  l'amplitude maximale, résultat prévisible ? 4°) comment éviter la diffraction ?
  Interprétation : amplitude maximale quand i = i'.

**3.1 L'onde transmise (p.230–231)** — NOUVEAU. Cuve à ondes, lame L, plaque rectangulaire en plexiglas P de faible épaisseur
posée à plat côté opposé à L (Fig.11) : milieu 1 d'épaisseur e₁, milieu 2 d'épaisseur e₂, e₁ > e₂ ; surface de séparation notée σ ;
éclairage stroboscopique Ne = N : deux séries de rides immobiles, rectilignes, équidistantes, plus serrées dans le milieu 2
(Fig.12, λ₁ et λ₂). Questions : 1°) l'onde subit-elle un changement en passant de 1 à 2 ? 2°) la profondeur a-t-elle un effet sur la
célérité v ? 3°) comparer les longueurs d'onde. Interprétation : direction et forme inchangées ; λ₂ < λ₁ ; « la célérité v de
l'onde progressive qui se propage dans l'eau est la plus grande dans la zone la plus profonde ».

**3.2 L'onde réfractée (p.231–233)** — NOUVEAU. Plaque trapézoïdale : surface de séparation plane faisant un angle non nul avec la
source L (Fig.13a). Observation en éclairage stroboscopique : milieu 1 rides équidistantes immobiles parallèles à L ; milieu 2 rides
plus rapprochées et de direction différente ; « une cassure de ces rides » à la surface de séparation. Questions : 1°) la direction
de la surface de séparation agit-elle sur la direction de l'onde transmise ? 2°) λ modifiée ? 3°) mesurer l'angle de l'onde
incidente avec la normale, le comparer à celui de l'onde transmise avec la même normale. Interprétation : onde réfractée, changement
de λ et de direction ; angle d'incidence i₁, angle de réfraction i₂ ; I et I' intersections de deux rides consécutives avec la
surface (Fig.13b). Démonstration (p.233, vue sur l'image) : dans le triangle HII' : II'.sin(i₁) = λ₁ (1) ; dans H'II' :
II'.sin(i₂) = λ₂ (2) ; rapport : λ₁/λ₂ = sin(i₁)/sin(i₂) (3) ; (3) s'écrit λ₁.sin(i₂) = λ₂.sin(i₁) (4) ; avec λ₁ = v₁.T,
λ₂ = v₂.T : sin(i₁)/v₁ = sin(i₂)/v₂ ; « Ainsi, on retrouve la seconde loi de Descartes relative à la réfraction. »

**4.1 Dispersion de la lumière (p.234–235)** — identique à 223433 p.233–234 (§2.1) : introduction (réfraction d'un faisceau laser),
manipulation 1 laser He-Ne + prisme en verre d'indice n, écran à distance d, déviation D (Fig.14) ; 3 questions ; manipulation 2
lumière blanche + lentille convergente + fente, spectre « bordé de rouge et de violet » (Fig.15) ; 3 questions ; interprétation
(double réfraction air/verre/air ; spectre continu) ; Conclusion identique (cf. encadrés). Numérotation des figures seulement :
Fig.14/15 (223433 : 7/8). Question 3°) de la première série : « Rappeler les lois de Descartes pour la réfraction. »

**4.2 Dispersion des ondes mécaniques (p.235–236)** — NOUVEAU. Cuve à ondes, lame vibrante L, stroboscope de fréquence réglable Ne
= N (rides immobiles, distance entre deux rides consécutives = λ) ; N varie ; tableau : N (Hz) 10 / 20 / 30 ; λ (10⁻³ m)
21 / 11 / 8 ; célérité v (m.s⁻¹) 0,21 / 0,22 / 0,24. Questions : 1°) changement de nature de l'onde quand N change ? 2°) nature du
milieu modifiée par N ? 3°) la célérité à la surface de l'eau est-elle indépendante de sa fréquence ? Interprétation : « la célérité v
d'une onde mécanique dans un milieu de propagation tel que l'eau ne dépend pas uniquement de ses propriétés, mais dépend aussi de
la fréquence N de l'onde. C'est le phénomène de dispersion. » Exemple (bateau) : « Un observateur sur le rivage verra d'abord
arriver des vagues très espacées (grandes longueurs d'onde) puis ensuite des vagues moins espacées […] les plus rapides se détachent
à l'avant de la perturbation. » Conclusion (cf. encadrés).

**4.3 Milieu dispersif et non dispersif (p.237–238)** — identique à 223433 p.235–236 sur : manipulation avec filtres de couleur (même
angle d'incidence i, angle de déviation D par filtre ; Fig.16 : rouge le moins dévié, vert, bleu le plus dévié), 3 questions,
interprétation (« le bleu est plus dévié que le rouge et le vert » ; indice n du prisme non constant, augmente du rouge au bleu ;
prisme = milieu dispersif), **même tableau** (bleu sombre 6,92 / 0,433 / 1,528 ; bleu vert 6,18 / 0,485 / 1,520 ; jaune 5,10 /
0,588 / 1,517 ; rouge 4,57 / 0,656 / 1,514 ; rouge sombre 3,91 / 0,767 / 1,511 ; colonnes ν (10¹⁴ Hz), λ (10⁻⁶ m), n), **même remarque**
« augmentation de (0,006) pour chaque diminution de dix picomètres (10 pm) » (cf. doute 8). Écarts : (a) la phrase « En général, tant
pour les ondes mécaniques que pour les ondes lumineuses, on appellera milieu dispersif pour une onde de fréquence N (ou ν) tout
milieu où la célérité v de cette onde ne dépend pas uniquement des propriétés du milieu de propagation, mais dépend aussi de la
fréquence N (ou ν) de l'onde. Dans le cas contraire où la célérité v de l'onde est indépendante de la fréquence N (ou ν), le milieu
est dit non dispersif. » est placée, en 223433 p.236, entre la Remarque (0,006) et l'encadré, et en 223432 **après** l'encadré (p.238) ; elle y commence par « En général, tant pour les ondes mécaniques que pour les ondes lumineuses, … » (incise absente de 223433) ; (b) la remarque finale
devient : « L'air est un exemple de milieu non dispersif pour les ondes sonores. En effet, des ondes sonores de fréquences
différentes se propagent dans l'air avec la même célérité. Par conséquent, deux notes de musique de hauteurs différentes émises
simultanément par deux instruments sont perçues par l'auditeur au même instant. » (223433 : seulement « L'air est un exemple de
milieu non dispersif. » — pas de justification par les ondes sonores).

### Encadrés, définitions et relations (VERBATIM, chacun vérifié sur l'image de sa page)

**Conclusion 1.1 (p.221)** — identique à 223433 p.229 : « Au niveau d'une fente ou d'un obstacle de largeur a d'une valeur comparable à
celle de sa longueur d'onde λ, l'onde mécanique subit le phénomène de diffraction. La diffraction est la modification du trajet d'une
onde et par suite de sa forme, au voisinage d'une fente ou d'un obstacle. En subissant la diffraction, une onde initialement plane se
propage après franchissement de la fente ou de l'obstacle, suivant plusieurs directions situées de part et d'autre de la direction
d'incidence. »

**Conclusion 1.2 (p.223)** et **Caractéristiques d'une onde lumineuse (p.223)** — identiques à 223433 p.231 (c = 3.10⁸ m.s⁻¹ ;
λ vide = c.T ; remarque air ≈ vide).

**Conclusion 1.3, onde mécanique (p.224)** — « Une onde plane rectiligne, de longueur d'onde λ, qui se propage à la surface d'un
liquide et qui traverse une fente F de largeur a ne subit pas une déformation appréciable tant que la valeur de a est grande devant
celle de λ. Par conséquent, le phénomène de la diffraction est imperceptible. Cependant, pour des valeurs de a comparables à celle
de λ, le phénomène de diffraction est appréciable. Ainsi le phénomène de diffraction dépend du quotient λ/a. »

**Conclusion 1.3, générale (p.226)** — « Une onde mécanique ou lumineuse de longueur d'onde λ subit une diffraction à la rencontre
d'une fente ou d'un obstacle, de largeur a d'une valeur comparable à celle de λ. La perception du phénomène de diffraction de
l'onde dépend de la valeur du quotient (λ/a). » (identique à 223433.)

**Relations quantitatives du cours (p.225–226, hors encadré, dans l'interprétation 1.3)** : L = k/a ; k = 2Dλ ; L = 2Dλ/a ;
tan θ = L/2D ; θ ≈ tan θ = L/2D (petits angles, D ≫ L) ; θ = λ/a.

**Conclusion 2.1 (p.227)** — « Un ébranlement incident, d'amplitude a, subit une réflexion au niveau d'une extrémité du milieu de
propagation et donne lieu à un ébranlement réfléchi. La réflexion d'un ébranlement sur une extrémité libre se fait avec la même
amplitude a et sans changement de signe. Par contre, sur une extrémité fixe, la réflexion d'un ébranlement se fait avec un
changement de signe. »

**Conclusion 2.2, onde plane (p.229)** — « Une onde incidente progressive plane, d'angle d'incidence i, de longueur d'onde λ qui se
propage dans un milieu de propagation, subit une réflexion au niveau d'un obstacle plan (plaque de plastique...) et donne
naissance à une onde progressive plane réfléchie de longueur d'onde λ' et d'angle de réflexion i' tels que : λ = λ' et i = i'. Ce
résultat nous rappelle la deuxième loi de Descartes, relative à la réflexion d'un rayon lumineux qui tombe sur un miroir plan sous
une incidence i. »

**Conclusion 2.2, onde sonore (p.230)** — « Une onde sonore subit une réflexion à la rencontre d'un obstacle réfléchissant de grande
dimension et donne naissance à une onde réfléchie. En chaque point d'incidence, on peut vérifier les lois de Descartes pour la
réflexion. Ainsi, l'angle d'incidence i de l'onde sonore est égal à son angle de réflexion i'. Les dimensions de l'obstacle doivent
être très supérieures à la longueur d'onde dans l'air de l'onde sonore incidente. Dans le cas contraire, l'onde incidente contourne
l'obstacle et c'est le phénomène de diffraction qui aura lieu. »

**Conclusion 3.1 (p.231)** — « Le passage d'une onde progressive d'un milieu vers un autre se produit avec changement de célérité
mais sans changement de direction lorsque cette onde arrive à la surface de séparation des deux milieux de propagation suivant une
direction perpendiculaire à cette surface. On dit qu'il s'agit d'une simple transmission. L'onde est dite alors onde transmise. »

**Conclusion 3.2 (p.233)** — « Au niveau de la surface de séparation de deux milieux de propagation, l'onde mécanique subit un
changement de direction de propagation : c'est le phénomène de réfraction. La réfraction d'une onde mécanique se fait avec un
changement de sa longueur d'onde λ. La réfraction d'une onde mécanique est régie par la relation de Descartes : λ₁ sin(i₂) =
λ₂.sin(i₁). Où : λ₁ et λ₂ sont respectivement les longueurs d'onde de l'onde incidente et de l'onde réfléchie ; i₁ et i₂ sont
respectivement l'angle d'incidence et l'angle de réflexion. » (« réfléchie » / « réflexion » sont des fautes du manuel pour
« réfractée » / « réfraction » : doute 1.)

**Conclusion 4.1 (p.235)** — identique à 223433 p.235 (« La lumière blanche résulte de la superposition d'une infinité de lumières de
couleurs différentes allant du rouge au violet […] la déviation d'une radiation lumineuse monochromatique par un prisme d'indice n,
dépend de sa fréquence ν. »).

**Conclusion 4.2 (p.236)** — « Quand la célérité v d'une onde mécanique dans un milieu de propagation donné ne dépend pas uniquement
de la nature de ce milieu, mais dépend aussi de sa fréquence N, on dit qu'il s'agit du phénomène de dispersion d'onde mécanique. »

**Conclusion 4.3 (p.238, lue à 200 dpi)** — « Chaque radiation lumineuse monochromatique de fréquence ν est caractérisée par une
longueur d'onde dans le vide λ₀ = c/ν. En pénétrant dans un milieu transparent d'indice n, où la célérité de la lumière est
v = c/n, sa longueur d'onde devient λ = v/ν = c/(n.ν) = λ₀/n. Le phénomène de dispersion de la lumière est la variation de sa
célérité v dans un milieu transparent d'indice n, en fonction de sa fréquence ν. Ainsi, la déviation d'une radiation lumineuse
monochromatique par un prisme en verre d'indice n dépend de sa fréquence ν. Tout milieu transparent d'indice de réfraction n, où
la célérité d'une radiation lumineuse dépend de sa fréquence est appelé milieu dispersif. Le verre est un exemple de milieu
dispersif. » (identique à 223433 p.236.)

**L'essentiel (p.239, verbatim, vu sur l'image)** — 11 puces : « La diffraction d'une onde est la modification de son trajet et par
suite sa forme au voisinage d'une ouverture ou d'un obstacle de dimensions comparables à sa longueur d'onde. » · « La diffraction
d'une onde se fait sans changement de sa longueur d'onde. » · « Un faisceau de lumière est décrit comme étant une onde appelée
onde lumineuse. » · « Le phénomène de diffraction dépend du quotient λ/a, λ étant la longueur d'onde et a l'ouverture de la
fente. » · « Une lumière monochromatique est une onde progressive sinusoïdale caractérisée par sa fréquence ν et sa longueur
d'onde λ₀ dans le vide. » · « Une lumière polychromatique est constituée de plusieurs radiations. » · « La lumière blanche est une
lumière polychromatique. » · **« Une onde mécanique, comme une onde lumineuse, peut subir le phénomène de réflexion à la rencontre
d'un obstacle plan. »** (nouvelle) · **« La réfraction d'une onde mécanique est le changement de sa longueur d'onde et de sa
direction de propagation, au niveau de la surface de séparation de deux milieux de propagation. »** (nouvelle) · « Le phénomène de
dispersion de la lumière est la variation de sa célérité v dans un milieu transparent d'indice n, en fonction de sa fréquence ν. » ·
« On appelle milieu dispersif tout milieu dans lequel la célérité v d'une onde **périodique** dépend de sa fréquence. »
(223433 : « onde lumineuse »).

### Exercice résolu (p.240–241) — DIFFÉRENT de 223433

**Énoncé (p.240)** — Faisceau monochromatique de longueur d'onde λ (**inconnue**), fente fine rectangulaire de largeur réglable a,
écran E à D = 3 m. Tableau : a (mm) 0,10 / 0,14 / 0,20 / 0,25 ; L (mm) 31,5 / 22,5 / 16,0 / 12,5 (mêmes valeurs qu'en 223433).
1°) décrire brièvement la figure ; 2°) tracer L en fonction de 1/a et calculer sa pente ; 3°) relation entre L et λ ; 4°) valeur de
λ ; 5°) un cheveu de diamètre d remplace la fente, L' = 1,5 cm : calculer d de deux manières.
**Solution (p.240–241)** — 1°) figure étalée horizontalement, tache centrale brillante de largeur L entourée de taches séparées par des
zones sombres (Fig.1 : laser, fente, « taches de diffraction sur un axe horizontal ») ; 2°) droite linéaire, L = k/a =
3,15.10⁻⁶/a (1) (graphe : L (10⁻³ m) de 0 à ≈ 32 pour 1/a de 0 à 10 (10³ m⁻¹)) ; 3°) L = 2.λD/a (2) ; 4°) par identification
2.λ.D = k, λ = k/2D, A.N. λ = 525.10⁻⁹ m ; 5°) 1re méthode : L' = 2.λD/d, d = 2λD/L', A.N. d = 0,21.10⁻³ m = 0,21 mm ; 2e méthode :
lecture sur la courbe L = f(1/a) de l'abscisse 1/d correspondant à L' = 1,5 cm. (Vérification de cohérence : 3,15.10⁻⁶/(2×3) =
5,25.10⁻⁷ m ; 2×525.10⁻⁹×3/0,015 = 2,1.10⁻⁴ m.)

### Exercices à résoudre (p.242–246) — réponses du manuel p.319 (chapitre 8)

**Tests rapides des acquis (p.242)** — aucune réponse au manuel.
- **Ex.1 Vrai/faux** (8 items) : 1 la diffraction n'a pas d'influence sur λ de l'onde incidente ; 2 changement de fréquence lors du
  passage d'une onde d'un milieu à un autre ; 3 on ne peut pas obtenir d'ondes réfléchies à partir d'ondes circulaires ; 4 la direction
  d'une onde plane subit une modification chaque fois que l'onde rencontre un obstacle ; 5 la diffraction de la lumière met en
  évidence l'impossibilité d'isoler un rayon lumineux ; 6 la célérité de la lumière est indépendante de la nature du milieu ;
  7 la réflexion d'un ébranlement à l'extrémité libre d'une corde élastique se fait avec changement de signe ; 8 l'eau est un milieu
  dispersif pour les ondes lumineuses. (223433 : 9 items différents.)
- **Ex.2 QCM** (6 items, « la (ou les) proposition(s) juste(s) ») : I diffraction observée pour a- λ/a > 1, b- **λ/a² = 1** (image),
  c- λ/a < 1 ; II L liée à θ par a- θ = L/D, b- θ = L/2D, c- θ = D/2L (D distance fente-écran) ; III L et L' (tache latérale) : a- L =
  2.L', b- L = L', c- L = L'/2 ; IV dans un milieu dispersif la célérité est fonction uniquement de a- la fréquence, b- la nature du
  milieu, c- la fréquence et la nature du milieu ; V indice n : a- n = c/v, b- n = v/c, c- n = c.v ; VI en pénétrant dans un milieu
  d'indice n, une radiation de longueur d'onde λ₀ subit un changement de a- sa fréquence, b- sa longueur d'onde, c- sa couleur.

**Exercices d'application (p.243–244)**
- **Ex.3** — cuve à ondes, onde rectiligne progressive, obstacle empêchant toute propagation au-delà, angle α = 30° avec la direction
  de propagation ; distance entre deux crêtes d = 4,0 cm ; N = 12,5 Hz. 1°) angle d'incidence i ; 2°) célérité de l'onde incidente ;
  3°) schéma, direction de l'onde réfléchie, i et r. Réponse : « 1°) 60°, 2°) 0,5 m.s⁻¹, 3°) r = 60°. »
- **Ex.4** — digue de largeur l = 30 m entre une baie et la mer, vagues parallèles à la digue, λ = 80 m (Fig.2) ; 1°) propagation au-delà ;
  2°) schéma ; 3°) nature du phénomène ; 4°) vagues λ = 5 m. Réponse : « 1°) λ >> l, 2°) rides circulaires, 3°) diffraction,
  4°) l << λ, pas de diffraction. » (énoncé identique à 223433 ex.4 ; voir doute 6 sur l'écriture de l'inégalité.)
- **Ex.5** — cuve à ondes, plaque de verre délimitant deux zones (z₁) et (z₂) de hauteurs d'eau différentes (Fig.3) ; vibreur S₁S₂
  parallèle au petit côté, onde plane N = 40 Hz, dans (z₁) v₁ = 36 cm.s⁻¹. 1°) l'onde subit-elle un changement, quel phénomène ?
  2°) v₂ = 29 cm.s⁻¹ : calculer λ₂ ; 3°) reproduire la figure et représenter l'onde transmise en (z₂). Réponse : « 1°) oui,
  2°) λ₂ = v₂/N₂ = v₁/N₂ = 7,25.10⁻³ m. » (7,25.10⁻³ m = 0,29/40 ; « v₁/N₂ » est une coquille du manuel pour v₂/N.)
- **Ex.6** — cuve à ondes partagée par une plaque de plexiglas en deux zones d'épaisseurs e₁ = 2,5 cm et e₂ = 1,5 cm (Fig.4), onde plane,
  surface de séparation parallèle à L. 1°) l'onde incidente : a) subit-elle un changement ? b) quel phénomène ? 2°) v = √(g.e) en
  milieu peu profond (N = 25 Hz, g = 10 m.s⁻²) : a) λ₁ et λ₂ ; b) comparer λ₂ à λ₁ ; 3°) allure de la surface en éclairage
  stroboscopique, Ne = N ; 4°) l'eau est-elle un milieu dispersif pour les ondes mécaniques ? justifier. Réponse : « 1°) a)-Oui,
  b)-transmission avec changement de célérité, 2°)a)-λ₁ = v₂/N = 2.10⁻²m, λ₂ = v₂/N = 1,5.10⁻²m, b) λ₂ < λ₁, 4°) non, car v₂ ≠ v₁, pour
  N = Cte. » (voir doute 3.) Valeurs recalculées : v₁ = 0,5 m.s⁻¹, v₂ ≈ 0,387 m.s⁻¹.
- **Ex.7** — deux zones d'épaisseur d'eau différente : v₁ = 0,30 m.s⁻¹, v₂ = 0,25 m.s⁻¹, vibreur 20 Hz, onde rectiligne arrivant sous
  i₁ = 30°. 1°) λ de l'onde incidente ; 2°) λ de l'onde réfractée ; 3°) seconde loi de Descartes : angle de réfraction i₂ ;
  4°) schéma sans tenir compte de la réflexion. Réponse : « 1°) λ₁ = v₁/N = 2.10⁻²m, 2°) λ₂ = v₂/N = 1,33.10⁻²m, 3°) sin(i₂) =
  v₂ sin(i₁)/v₁ ce qui donne i₂ = 19,47°. » **[?] incohérent avec l'énoncé : voir doute 2.**
- **Ex.8** — faisceau monochromatique λ traversant un prisme d'indice n sous l'incidence i (Fig.5 : prisme, faisceau incident,
  écran E incliné). 1°) définir l'indice de réfraction d'un milieu transparent ; 2°) rappeler les lois qui permettent de tracer la
  marche du faisceau émergent ; 3°) reproduire la Fig.5 et tracer le faisceau émergent ; 4°) observation sur E, phénomène ;
  5°) faisceau de lumière blanche : la figure change-t-elle ? Réponse : « 1°) n = c/v, 2°) sin(i₁) = n.sin(i₂), 4°) une tache, 5°) oui,
  on obtient le spectre de la lumière blanche. » (= 223433 ex.6.)

**Exercices de synthèse (p.244–246)**
- **Ex.9** — fente de largeur a réglable, λ = 0,63 μm, D = 1 m ; « La largeur L de la tache centrale […] est donnée par la relation
  L = 2.D.λ/a avec D la distance entre l'écran E et la fente » (relation DONNÉE dans l'énoncé). 1°) lumière monochromatique ?
  2°) a = 0,1 mm : a) décrire, b) justifier en comparant L et a ; 3°) L' pour λb = 0,46 μm ; 4°) pourquoi plus facile en rouge qu'en
  bleu ; 5°) a = 2 mm, phénomène observable ? Réponse : « 1°) Une seule radiation, 2°)a) Tache centrale de largeur L, b)
  λ/a = 6,3.10⁻⁶ < 0,174, 3°) L' = 9,2.10⁻³ m, 4°) L' < L, 5°) L = 0,63.10⁻³ m, on mesure difficilement L. » (= 223433 ex.7 +
  relation donnée ; doute 4.) Valeurs recalculées : L(0,1 mm) = 1,26.10⁻² m ; L' = 9,2.10⁻³ m ; L(2 mm) = 6,3.10⁻⁴ m.
- **Ex.10** — laser λ, fente de largeur a, écran E perpendiculaire. 1°) relation entre λ et a permettant l'observation de la diffraction ;
  2°) schéma de la figure ; 3°) définir l'écart angulaire θ de la tache centrale ; 4°) relation entre θ, L et D ; 5°) expression de L
  en fonction de D, a, λ ; 6°) λ pour a = 60 μm, L = 4,2 cm, D = 2,0 m. Réponse : « 1°) θ = λ/a, 4°) θ = L/2D, 5°) L = 2λ.D/a,
  6°) λ = L.a/2D, λ = 0,63 μm. » (pas de réponse à 2°, 3°.)
- **Ex.11** — faisceau parallèle monochromatique λ, fente circulaire de diamètre a, D = 4,5 m ; a (10⁻⁴ m) 4,9 / 6,2 / 8,2 / 12,0 ;
  rayon r de la tache centrale (10⁻³ m) 7,5 / 6,0 / 4,5 / 3,0 (mêmes données que 223433 ex.3). 1°) tracer r en fonction de 1/a ;
  2°) équation de la courbe ; 3°) schéma, relation entre D, r et θ ; 4°) « Dans le cas d'une fente circulaire, θ = 1,22.λ/a » (donnée de
  l'énoncé) : montrer que r = 1,22.λ.D/a ; 5°) λ. Réponse : « 1°) Une droite, 2°) r = k/a = 36,7.10⁻⁷/a, 4°) θ = 1,22.λ/a, θ = r/a,
  r = 1,22.λD/a, 5°) λ = 0,67 μm. » (« θ = r/a » tel qu'imprimé, vu à 200 dpi ; voir doute 5.)
- **Ex.12** — figure de diffraction (Fig.6) sur un écran à D = 2 m d'une fente a = 100 μm, laser de λ inconnue ; sur la figure :
  x₁ = 2,7 cm (tache centrale), x₂ = 5,5 cm, x₃ = 8 cm (cotes lues sur l'image). 1°) schéma du dispositif ; 2°) relation entre la
  largeur X₁ et θ ; 3°) relation entre θ, λ et a ; 4°) déterminer λ ; 5°) comparer tache centrale et tache latérale ; 6°) largeur de la
  tache centrale avec λ = 450 nm. Réponse : « 2°) θ₁ = X₁/2D, 3-θ₁ = λ/a, 4°) λ = a.X₁/2D = 0,675 μm, 5°) L₁ = 2,7.10⁻² m,
  L₂ = 1,4.10⁻² m, L₁ = 2L₂, 6°) X₁ = 2λ.D/a = 1,8.10⁻² m. » (≈ 223433 ex.8 mais λ y était donnée ; ici λ est à déterminer.)
- **Ex.13** — faisceau étroit monochromatique, i = 30° au point I de la face plane d'un hémicylindre en plexiglas (Fig.7 : S, normale N, I,
  face plane verticale, partie courbe à droite). 1°) lois de Descartes pour la réfraction ; 2°) r_j (jaune, n_j = 1,485) ; 3°) montrer
  D = i_j − r_j ; 4°) r_B (bleu, n_B = 1,520) ; 5°) lumière jaune + bleue : tracé, angle entre les rayons, phénomène. Réponse :
  « 1°) n₁sin(i₁) = n₂sin(i₂), 2°) sin(r_j) = sin(i)/n_j, r_j = 19,67°, 3°) i_j > r_j par la suite D = i_j − r_j = 10,3°. 4°) r_b = 19,2°
  et D' = 10,8°, ainsi la radiation bleue est la plus déviée, la dispersion de la lumière. » (= 223433 ex.9 ; mêmes valeurs.)
- **Ex.14 Étude de texte (p.246) « Les ondes sonores dans une pièce vide »** — texte : diffraction sonore dès que l'onde atteint le
  bord d'un obstacle ou passe par une ouverture ; « prépondérant si la longueur d'onde du son est du même ordre de grandeur que les
  dimensions des objets » ; pièce vide : les ondes se réfléchissent sur les murs, « on dit que la pièce résonne » ; meubles de
  l'ordre du mètre : « elle résonne moins. La diffraction commence à masquer la réflexion » ; tissu sur les murs, tapis, tentures :
  « Le phénomène de diffraction l'emporte sur celui de la réflexion ». Questions : 1°) dans quel cas la diffraction des ondes
  sonores est-elle appréciable dans une pièce meublée ? 2°) comment atténuer la « résonance » d'une pièce ? 3°) effet du tissu sur les
  murs ? 4°) dans un amphithéâtre, comment éviter la réflexion des ondes sonores ? Pas de réponse au manuel.

### Fiche technique et « En savoir plus »
- Pas de fiche technique dans le chapitre.
- **En savoir plus (p.247)** — « L'interprétation du phénomène de diffraction avec la théorie des ondelettes » : identique à 223433
  p.243 (surface d'onde Σt, sources secondaires de Huygens, ondelettes circulaires de rayon v.T, Σt+T ; a très petite devant λ :
  F source secondaire unique, Fig.1–3 ; encadré Christian Huygens 1629-1695, « Traité de lumière » 1678). Lecture seule.

### Écart avec Sciences expérimentales (223433)

**Ce que 223432 AJOUTE**
- **Réflexion** (§2, p.226–230) : réflexion d'un ébranlement (extrémité libre / fixe : même signe / signe contraire, même amplitude) ;
  réflexion d'une onde plane (λ = λ', i = i', rappel de la 2e loi de Descartes) ; réflexion d'une onde sonore sur un obstacle plan
  (tableau amplitude U / i', maximum pour i = i' = 30° ; dimensions de l'obstacle ≫ λ ; fréquences de l'ordre du MHz pour limiter la
  diffraction). Matériel : ondoscope, plaque plastique, haut-parleur/microphone, GBF, oscilloscope, écran de polystyrène.
- **Réfraction d'une onde mécanique** (§3, p.230–233) : onde transmise (changement de célérité sans changement de direction, λ₂ < λ₁
  pour la zone moins profonde) ; onde réfractée ; démonstration λ₁ sin(i₂) = λ₂ sin(i₁), d'où sin(i₁)/v₁ = sin(i₂)/v₂ (2e loi de Descartes).
- **Dispersion des ondes mécaniques** (§4.2, p.235–236) : tableau N / λ / v à la surface de l'eau (célérité qui croît avec la
  fréquence : 0,21 ; 0,22 ; 0,24 m.s⁻¹) ; exemple du bateau ; définition générale du milieu dispersif étendue aux ondes mécaniques ;
  air non dispersif pour le son (deux notes perçues au même instant).
- **Diffraction de la lumière quantitative dans le cours** (p.224–226) : ligne 1/a des tableaux 1–2 ; Fig.7 (L en fonction de 1/a) ;
  L = k/a ; k = 2Dλ ; L = 2Dλ/a ; tan θ = L/2D ; θ = L/2D ; θ = λ/a (λR = 633 nm, λV = 532 nm). En 223433 ces relations
  n'apparaissaient que dans les réponses d'exercices.
- Ouverture et accroche différentes (p.218–219) ; prérequis et objectif sur réflexion/réfraction/Descartes ; deux puces d'« L'essentiel »
  (réflexion, réfraction) ; dernière puce « onde périodique ».
- **Exercice résolu** refondu (λ à déterminer, pente k = 3,15.10⁻⁶, L' = 1,5 cm, cheveu par deux méthodes).
- **Exercices** : ex.3, 5, 6, 7 (réflexion et réfraction d'ondes mécaniques : angle d'incidence, célérités, longueurs d'onde, v = √(g.e),
  Descartes i₂) ; ex.10 (établissement de θ = L/2D et L = 2Dλ/a, calcul de λ) ; ex.11 (courbe r en fonction de 1/a, θ = 1,22.λ/a
  fournie, r = 1,22.λ.D/a) ; ex.14 (étude de texte sur le son dans une pièce) ; relation L = 2Dλ/a donnée dans l'énoncé de l'ex.9 ;
  ex.12 : λ à déterminer.

**Ce que 223432 RETIRE ou remplace**
- L'interprétation fautive de 223433 p.233 (« L est d'autant plus grande que λ est plus petite ») : remplacée par une analyse
  par la pente k, cohérente. La question « 2°) variation de L, puis de θ, en fonction de λ » devient la question 4° (p.225).
- Onde lumineuse §1.3 (p.224) : 223433 (p.232) définit θ dès la manipulation (« et l'angle θ représente la demi-largeur angulaire de la tache centrale ») ; 223432 retire ce membre de phrase et introduit θ par la question 3°.
- Page d'ouverture 223433 (holographie, papillon bleu, laser sur cheveu / dispersion du laser) ; objectif « Réaliser des expériences
  de dispersion des ondes lumineuses » (devient « …de réflexion, de réfraction et de dispersion d'ondes mécaniques »).
- Exercice résolu 223433 (λ = 0,525 μm donnée, effet de D' = 1 m sur la netteté, cheveu d = 0,20 mm → L = 16 mm) ; tests rapides
  223433 (Ex.1 à 9 items, Ex.2 QCM différent) ; ex.5 (définition de θ, L augmente avec D) ; ex.10 « La houle » (baie, cap, île, jetée,
  Hachette 2000) ; ex.3 de 223433 (fente circulaire, r en fonction de a) repris en ex.11 avec questions différentes.
- Fiches : pas d'écart (pas de fiche technique dans l'un ni l'autre) ; « En savoir plus » identique.
- Identiques : introduction, §1.1, §1.2, §1.3 onde mécanique (sauf « très grande » → « grande »), §4.1, tableau ν/λ/n du prisme et sa
  remarque (0,006/10 pm), conclusion 4.3, ex.4 (digue), ex.8 prisme (= 223433 ex.6), ex.13 hémicylindre (= ex.9) ; ex.9 (= ex.7 avec
  relation donnée) ; ex.12 (≈ ex.8).

### Bornes de scope (section Mathématiques)

**✅ Inclus**
- Diffraction d'une onde mécanique (cuve à ondes, fente ou obstacle) : rides rectilignes → circulaires, λ conservée, onde
  diffractée ; comparaisons qualitatives a > λ / a ≃ λ / a < λ ; influence de λ (profondeur d'eau) ; dépendance au quotient λ/a.
- Diffraction de la lumière (laser, fente, fil/cheveu, trou) : figure de diffraction, franges, anneaux, mise en défaut de la
  propagation rectiligne, onde lumineuse (T, λ, c = 3.10⁸ m.s⁻¹, λ vide = c.T, air ≈ vide).
- **Quantitatif (inclus pour cette section, énoncé dans le cours p.225–226)** : L = k/a ; k = 2Dλ ; L = 2Dλ/a (fente rectangulaire,
  tache centrale) ; tan θ = L/2D ; θ ≈ L/2D (petits angles) ; θ = λ/a ; tracé et pente de L = f(1/a) ; détermination de λ, de a, du
  diamètre d'un fil/cheveu par L = 2Dλ/a ; comparaison tache centrale / latérale (L = 2L') ; lecture de tableaux (a, L, 1/a).
- Réflexion : d'un ébranlement (extrémité libre : même signe ; fixe : signe contraire ; même amplitude) ; d'une onde plane (λ = λ',
  i = i') ; d'une onde sonore (angle d'incidence = angle de réflexion ; obstacle ≫ λ).
- Réfraction d'une onde mécanique : transmission (changement de célérité, pas de changement de direction, incidence normale) ;
  onde réfractée ; λ₁ sin(i₂) = λ₂ sin(i₁) et sin(i₁)/v₁ = sin(i₂)/v₂ ; calculs de λ = v/N, de i₂ ; v = √(g.e) (milieu peu profond,
  donnée de l'énoncé ex.6).
- Dispersion : prisme, double réfraction, déviation D, spectre continu (rouge → violet), lumière monochromatique / polychromatique,
  radiation caractérisée par ν et λ₀ ; λ₀ = c/ν, v = c/n, λ = v/ν = c/(nν) = λ₀/n ; n du verre croît du rouge au bleu (tableau) ;
  milieu dispersif (verre ; eau pour les ondes de surface, p.236) / non dispersif (air pour le son).
- Dans les exercices : lois de Descartes (n₁sin i₁ = n₂sin i₂), déviation D = i − r au hémicylindre, indice n = c/v, calculs de L'
  pour une autre λ, application aux vagues (digue, baie) et au son dans une pièce (ex.14).

**⛔ Exclu**
- θ = 1,22.λ/a (fente circulaire) : donnée dans l'énoncé de l'ex.11 uniquement, jamais dans le cours ; ne pas en faire une loi.
  Pas de position des minima d'ordre k, pas d'intensité, pas de formule des anneaux autre que celle fournie en ex.11.
- Interférences (fentes d'Young, interfrange), réseaux, polarisation, holographie, iridescence.
- Formules du prisme (A = r + r', D = i + i' − A, déviation minimale), loi de Cauchy, calcul de n en fonction de λ ; la remarque
  « 0,006 pour 10 pm » (doute 8).
- Théorie des ondelettes de Huygens (« En savoir plus », lecture seule, non évaluable).
- Énergie du photon, aspect corpusculaire, spectres de raies (chap. 9) ; ondes stationnaires et résonance (autres chapitres) ;
  effet Doppler.
- Appareillage : ondoscope, cuve à ondes, stroboscope (utilisation en prérequis), laser He-Ne, diaphragme, oscilloscope/GBF
  (ex. de réflexion sonore : données seulement), prisme, lentille, filtres.

### Lecture

- **Couche texte** (pdftotext -layout) : p.218–247 en entier ; réponses p.317–320 (chap. 8 : p.319 ; p.318 = chap. 1–7 ; p.320 = sites
  web). Comparaison automatique (diff mot à mot) des p.220–226 et p.234–238 de 223432 avec les p.228–236 de 223433, pour établir
  les passages identiques.
- **Pages vues sur l'image** (31, à 110 dpi) : 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234,
  235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247 et 319. **Toutes les pages du chapitre (218–247) sont vues sur
  image.**
- **Sondage à haute résolution (≥ 1 page sur 10, pages les plus denses)** : p.226 (relations θ = λ/a, 200 dpi), p.238 (conclusion
  4.3, 200 dpi), p.242 (QCM I, 220 dpi), p.319 (réponses du chap. 8, 200 dpi, colonnes gauche et droite) — 4 pages sur 31.
- **Écarts couche texte / image constatés** : λ/a rendu « - / a » (p.218, 224, 226, 239) ; ν (nu) rendu « V » ou « Vx » (p.235–239) ;
  conclusion p.238 en texte : « - 0 = c / * » (λ₀ = c/ν perdu) ; formules p.225–226 (L = 2Dλ/a, tan θ = L/2D, θ = λ/a) rendues
  « 2D- », « tan  = L » ; p.242 QCM I : « λ/a² = 1 » rendu comme « λ/a2 =1 » ; Fig.2b/5a « a b λ » = « a ≃ λ » ; tableaux avec
  exposants (10⁻³, 10³, 10¹⁴) ; Fig.6 (ex.12) : cotes x₁ = 2,7 cm, x₂ = 5,5 cm, x₃ = 8 cm absentes du texte (visibles sur l'image
  seule) ; p.319 : « n_j » / « r_j » indices et r_b ; la p.319 en texte mêle les colonnes (ex.8–13 en début de colonne droite).
- **Doutes [?]**
  1. **p.233, Conclusion 3.2** : « l'onde réfléchie » et « l'angle de réflexion » désignent en réalité l'onde réfractée et l'angle de
     réfraction (i₂) ; coquille du manuel, à ne pas reprendre. Autres coquilles de la même page : « La relatrion (3) »,
     « retouve ».
  2. **Ex.7, réponses incompatibles avec l'énoncé** (image p.244 et p.319) : énoncé v₁ = 0,30 m.s⁻¹, v₂ = 0,25 m.s⁻¹, N = 20 Hz ;
     réponses λ₁ = 2.10⁻² m, λ₂ = 1,33.10⁻² m, i₂ = 19,47°, qui correspondent à N = 15 Hz et v₂ = 0,20 m.s⁻¹. Valeurs de
     l'énoncé recalculées (hors manuel) : λ₁ = 1,5.10⁻² m, λ₂ = 1,25.10⁻² m, i₂ ≈ 24,6°. Ne pas reprendre la réponse du manuel ;
     la méthode (λ = v/N ; sin i₂ = v₂.sin i₁/v₁) est correcte.
  3. **Ex.6** : réponse imprimée « λ₁ = v₂/N » (coquille pour v₁/N) ; 4°) « non, car v₂ ≠ v₁, pour N = Cte » : argumentation
     discutable (deux profondeurs ≠ deux fréquences) et en tension avec le §4.2 qui déclare l'eau dispersive (v dépend de N, p.236).
     Valeurs numériques exactes pour v = √(g.e), N = 25 Hz : λ₁ = 2.10⁻² m, λ₂ ≈ 1,55.10⁻² m (manuel : 1,5.10⁻²).
  4. **Ex.9 2°b, réponse** « λ/a = 6,3.10⁻⁶ < 0,174 » : avec λ = 0,63 μm et a = 0,1 mm, λ/a = 6,3.10⁻³ ; l'origine de 0,174 n'est pas
     expliquée dans le manuel ; la question demande de comparer L à a (L = 1,26.10⁻² m ≫ a). Réponse inexploitable telle quelle.
  5. **Ex.11 3°/4°, réponse p.319** : imprimée « θ = r/a » (lecture image 200 dpi) alors que la relation géométrique est θ = r/D
     (D = 4,5 m ; le résultat r = 1,22.λD/a du manuel est cohérent avec θ = r/D). Coquille probable ; ne pas reprendre.
     θ = 1,22.λ/a est donnée par l'énoncé (hors cours).
  6. **Ex.4** : réponse 1°) « λ >> l » et 4°) « l << λ » : pour 4°) (λ = 5 m, l = 30 m) la bonne comparaison est λ << l ; le manuel écrit
     « l << λ ». Pas de diffraction notable dans ce second cas : la conclusion (« pas de diffraction ») est juste, l'écriture de
     l'inégalité est inversée.
  7. **Ex.2 QCM I, proposition b** « λ/a² = 1 » (image 220 dpi, a au carré) : formulation étrange (coquille probable de λ/a = 1) ;
     pas de réponse au manuel.
  8. **p.238, Remarque** : « augmentation de (0,006) pour chaque diminution de dix picomètres » — incompatible avec le tableau (n de
     1,511 à 1,528 sur ≈ 334 nm) ; chiffre identique à 223433, à ne pas utiliser.
  9. **Pas de réponses au manuel** pour : ex.1, ex.2, ex.14 ; ex.5 3° ; ex.6 3° ; ex.7 4° ; ex.8 3° ; ex.9 2°b (inexploitable), 4°
     partielle ; ex.10 2°, 3° ; ex.11 1° (« une droite » seulement), 3° ; ex.12 1° ; ex.13 5° (tracé).
  10. **Ex.12, Fig.6** : cotes x₁ = 2,7 cm, x₂ = 5,5 cm, x₃ = 8 cm. La réponse 5°) L₂ = 1,4.10⁻² m (largeur d'une tache latérale)
      suppose que x₂ − x₁ = 2,8 cm correspond à deux taches latérales (déduit par recoupement, le manuel ne le dit pas) ; L₁ = 2L₂
      (≈ : 2,7 ≈ 2 × 1,4).
  11. **Ex.3** : le manuel donne i = 60° pour α = 30° (angle de l'obstacle avec la direction de propagation) ; i est l'angle entre la
      direction de propagation et la normale à l'obstacle — formulation à vérifier avant d'écrire une question.
  12. **Fig.7 (p.225)** : droites tracées à la main ; λR = 633 nm, λV = 532 nm donnent k = 2Dλ = 2,53.10⁻⁶ et 2,13.10⁻⁶ m² (pour
      D = 2 m), cohérents avec L = 25.10⁻³ m et ≈ 21.10⁻³ m à 1/a = 10.10³ m⁻¹ (valeurs recalculées, hors manuel). Dans le tableau 2,
      l'écart L(0,15) = 14, L(0,30) = 7 est cohérent à l'arrondi.
  13. **Typos du manuel non corrigées dans les citations** : « inflence » (p.225), « Figue de diffraction » (Fig.6a), « mécnique »
      (Fig.1), « diffrac-tion », « entrain » (p.227), « mlieux » (Fig.13b), « réfaction » (ex.8), « réfaction » (ex.8 1°), « Fi 14 »
      (Fig.14), « intrépatation », « Islance », « circualire », « supersosition » (p.247), « ci-desous ».

## 2.9 Chapitre 9 — Spectre atomique (manuel 223432, p.248–271)

> Section DIFFÉRENTIELLE. Règle de correspondance constatée (comparaison page à page du texte ET des images
> au pixel près, cf. « Lecture ») : **page 223432 = page 223433 + 2** pour tout le chapitre (223433 p.246–269
> ↔ 223432 p.248–271). Le contenu est **identique, mot pour mot et figure pour figure**, à la section déjà
> transcrite et validée `bac-sciences-exp/physique.md` § 2.9 (manuel 223433, p.244–269). Les renvois
> « identique à 223433 p.X » ci-dessous valent donc pour la page 223432 p.(X+2). Les seules différences réelles
> sont listées dans « Écart avec Sciences expérimentales ».

**Pas d'ouverture de partie dans 223432** : les p.246–247 de ce manuel sont la fin du chapitre 8
(exercice 14 « Étude de texte : Les ondes sonores dans une pièce vide » ; « En savoir plus » : théorie des
ondelettes de Huygens) et le chapitre 9 s'ouvre directement p.248. Le sommaire de la partie « Physique
atomique et nucléaire » (I. Spectre atomique … ; II. Noyau atomique ; III. Réactions nucléaires) n'existe pas
ici en double page ; le chapitre 9 est celui de la partie « Physique atomique et nucléaire » (bandeau de
page « Physique atomique et nucléaire ◆ Spectre atomique »).

**Objectifs (p.248, verbatim)** — identique à 223433 p.246 : Décrire une expérience qui montre que l'énergie de
l'atome est quantifiée. · Calculer l'énergie de l'atome d'hydrogène en joule et en électron-volt. · Distinguer
un spectre d'émission d'un spectre d'absorption. · Appliquer la relation ΔE = h.ν. · Identifier un élément
chimique à partir de son spectre d'émission ou d'absorption. · Utiliser le spectre de la lumière émise par une
étoile pour reconnaître certains de ses constituants.

**Prérequis (p.248)** — identique à 223433 p.246. *Savoir* : définir la force d'interaction gravitationnelle ;
définir la force d'interaction électrique ou coulombienne ; énoncer le principe de conservation de l'énergie ;
définir les grandeurs caractéristiques d'une onde (période, fréquence, longueur d'onde) ; donner les règles de
répartition des électrons d'un atome sur les différents niveaux d'énergie. *Savoir-faire* : utiliser un prisme
pour analyser une lumière ; appliquer la conservation de l'énergie ; convertir en eV une énergie en J et
inversement ; appliquer la RFD au mouvement d'un satellite ; distinguer lumière monochromatique et
polychromatique ; répartir les électrons d'un atome sur les niveaux d'énergie.

**Page d'ouverture (p.249)** — « 9 · SPECTRE ATOMIQUE », photo de la nébuleuse du Crabe, bandeau et trois
questions d'accroche : identiques à 223433 p.247 (la composition « nébuleuse du crabe » est au même
emplacement ; les trois questions : analyse de la lumière → composition chimique, température, vitesse ;
identification d'un élément par son spectre ; spectre d'émission = « carte d'identité »).

**Plan du chapitre** (titres du manuel, identiques à 223433) : introduction p.250 (lumière blanche
polychromatique, sept couleurs ; « Qu'en est-il pour le spectre obtenu par la dispersion d'une lumière émise
par une lampe à vapeur de sodium ou de mercure (lampes d'éclairage public) ? ») ·
1 Énergie des systèmes en interaction (1.1 système macroscopique p.250–251 ; 1.2 système microscopique :
l'atome p.251–252) · 2 La quantification de l'énergie (2.1 expérience de Franck et Hertz (1914) p.252–253 ;
2.2 niveaux d'énergie d'un atome p.254) · 3 Spectres lumineux (p.255 ; 3.1 rappel ; 3.2 spectre d'émission
p.255–256 ; 3.3 spectre d'absorption p.256–258) · 4 Spectres de l'atome d'hydrogène (4.1 notion de photon
p.258 ; 4.2 modèle de Bohr p.258 ; 4.3 énergie de l'atome d'hydrogène p.259 ; 4.4 interprétation des raies
d'émission p.260–261 ; 4.5 interprétation des raies d'absorption p.261–262) · 5 Applications (5.1 en chimie
p.262 ; 5.2 en astrophysique p.262–263) · L'essentiel p.264 · Exercices : résolu p.265, à résoudre 1–10
p.266–269 · En savoir plus « Les modèles de l'atome » p.270–271 · réponses p.319.

### Cours — activités / études (identiques à 223433 ; une à trois lignes chacune)

- **1.1 {Terre-Satellite}** (p.250–251) — identique à 223433 p.248–249 : énergie mécanique = cinétique +
  potentielle ; Fig.1 ; relation (image) **F⃗_T/S = − G (m M / r²) u⃗_TS = − F⃗_S/T** ; 3 questions (modifier
  l'énergie, orbites à distances fixes ?, avion qui change d'altitude ?) ; ordres de grandeur (centaines de km ;
  dizaines de milliers de km ; Lune centaines de milliers de km) ; « Toutes les valeurs de l'énergie W sont
  permises ». **Conclusion (p.251)** : « Lorsqu'un système macroscopique interagit avec l'extérieur, l'énergie du
  système peut varier de façon continue. »
- **1.2 L'atome** (p.251–252) — identique à 223433 p.249–250 : relation (image) **F⃗_A/B = k (q_A q_B / r²) u⃗_AB
  = − k (e² / r²) u⃗_AB = − F⃗_B/A**, **k = 9.10⁹ N.m².C⁻²** ; modèle planétaire de Rutherford ; loi de Maxwell
  « toute particule chargée électriquement et accélérée rayonne de l'énergie » → l'électron perd de l'énergie.
  **Conclusion (p.252)** : « Par application des lois de la mécanique newtonienne on ne peut pas interpréter
  l'interaction électron-noyau au niveau de l'atome. »
- **2.1 Franck et Hertz** (p.252–253) — identique à 223433 p.250–251 : vapeur de mercure à faible pression ;
  canon à électrons, analyseur ; courbe N_C/N_e = f(E_C) (Fig.5) : N_C/N_e = 1 pour E_C < 4,9 eV, chute à
  E_C = 4,9 eV ; chocs élastiques / inélastiques ; l'atome de mercure ne prend qu'une énergie déterminée, 4,9 eV.
  **Conclusion (p.253)** : quantification du transfert d'énergie entre un atome et le milieu extérieur.
- **2.2 Niveaux d'énergie** (p.254) — identique à 223433 p.252 : hypothèses de Bohr (« Les variations d'énergie
  de l'atome sont quantifiées. » « L'atome ne peut exister que dans certains états d'énergie bien définis. »),
  niveaux d'énergie, fondamental, excités, transition (Fig.7). **Conclusion** : « L'énergie d'un atome est
  quantifiée : elle ne peut prendre que des valeurs discrètes caractéristiques de l'atome. Chacune entre elles
  représente alors un niveau d'énergie En. Dans son état fondamental, un atome est au plus bas niveau
  d'énergie. Grâce à un apport d'énergie de l'extérieur, un atome peut se trouver dans un état excité. »
- **3 Spectres lumineux** (p.255) — identique à 223433 p.253 : spectroscope, disperseur réseau (Fig.8a) ou prisme
  (Fig.8b), spectrographe ; 3.1 spectre continu de la lumière blanche (Fig.9).
- **3.2 Spectre d'émission** (p.255–256) — identique à 223433 p.253–254 : montage S, C, F, L, R, E (Fig.10) ;
  lampes Hg (Fig.11a) et H (Fig.11b) ; spectre de raies ; Hα rouge orangée, Hβ bleue, Hγ indigo, Hδ violette.
  **Conclusion (p.256)** : « Tout élément chimique est caractérisé par un spectre de raies appelé spectre
  d'émission. »
- **3.3 Spectre d'absorption** (p.256–258) — identique à 223433 p.254–256 : vapeur de sodium entre C et F
  (Fig.12 légendée « spectre d'émision » [sic], photo : lame de verre + alcool + eau salée), Fig.13 (raie noire du
  sodium), Fig.14a/b ; cannelures ; **Conclusion (p.258)** : spectre d'absorption = spectre continu auquel
  manquent les raies absorbées ; cannelures superposables aux raies d'émission ; « Le spectre d'émission ou
  d'absorption constitue « la carte d'identité » de l'élément chimique. » ; renversement des raies (Fig.15).
- **4.1 Photon** (p.258) — identique : **W = h.c/λ = h.ν**, **h = 6,62.10⁻³⁴ J.s** ; « L'énergie d'un photon est
  appelée quantum d'énergie. » (relation lue sur l'image : W = h·c/λ = h·ν.)
- **4.2 Modèle de Bohr** (p.258) — postulats verbatim (identiques à 223433 p.256) :
  « Le noyau est supposé fixe dans l'atome car sa masse est 1836 fois plus grande que celle de l'électron. » ·
  « L'électron ne peut graviter autour du noyau que sur des orbites circulaires bien déterminées. Ces orbites
  quantifiées sont dites stationnaires. » · « L'électron n'échange de l'énergie avec l'extérieur que lors de son
  passage d'une orbite stationnaire à une autre. »
- **4.3 Énergie de l'atome d'hydrogène** (p.259) — identique à 223433 p.257, **coquille comprise** : la formule
  imprimée (image) est « En = En/n² ; avec Eo = 13,6 eV et n un entier natuel non nul » (signe « − » absent,
  « En » au numérateur) ; forme correcte **En = − E0/n²** donnée par L'essentiel p.264, l'exercice résolu p.265 et
  tous les exercices. « En est exprimé en eV. 1 eV = 1,6.10⁻¹⁹ J. » ; n = 1 : E₁ = − 13,6 eV (fondamental, état le
  plus stable) ; n > 1 : − 13,6 eV < En < 0 (excité) ; n → ∞ : En(∞) = 0, atome ionisé ; énergie d'ionisation
  13,6 eV (électron séparé, énergie cinétique nulle). Fig.16 (niveaux : 0 « État ionisé » ; −Eo/25 n=5 ;
  −Eo/16 n=4 ; −Eo/9 n=3 ; −Eo/4 n=2 ; −Eo n=1 « Niveau (ou état) fondamental » ; flèche n=2→n=1 étiquetée
  « ΔE2,1 = E1 − E2 = h ν2,1 »).
- **4.4 Raies d'émission** (p.260–261) — identique à 223433 p.258–259 ; relations (image, relues p.260) :
  **ΔEn,p = Ep − En = −13,6/p² + 13,6/n² = 13,6 (1/n² − 1/p²)** (absorption n → p, p > n) ; désexcitation
  p → n : **ΔEp,n = En − Ep**, photon d'énergie **hν = − ΔEp,n** ; **ΔEp,n = Eo (1/n² − 1/p²) = hνp,n** ;
  **ΔEp,2 = − Eo (1/2² − 1/p²)**. Valeurs : n=1,p=2 : ΔE2,1 = E2 − E1 = 10,2 eV = 16,32.10⁻¹⁹ J ;
  ν2,1 = 2,4.10¹⁵ Hz ; λ2,1 = c/ν2,1 = 121 nm (Lyman, UV, « série de raies invisibles ») ; p=3, n=2 :
  ΔE3,2 = E2 − E3 = − 1,88 eV = − 3,02.10⁻¹⁹ J, ν3,2 = 4,5.10¹⁴ Hz, λ3,2 = 656 nm (Hα) ; λ4,2 = 486 nm (Hβ),
  λ5,2 = 434 nm (Hγ), λ6,2 = 410 nm (Hδ) → série de Balmer ; boîte « Questions » p.261 : « Montrer par un calcul
  similaire que les transitions qui aboutissent aux niveaux excités n = 4 ou n = 5 ou n = 6 donnent des radiations
  qui se trouvent dans l'infrarouge » ; infrarouge : Paschen (→3), Brackett (→4), Pfund (→5)
  (Fig.17 : diagramme n = 1…6, ∞ ; « Bracket » dans l'image, « Brackett » dans le texte). Les 4 questions de la
  boîte sont les mêmes (dont la Q3 qui renvoie à « la figure 16 »).
- **4.5 Raies d'absorption** (p.261–262) — identique à 223433 p.259–260 : si hν = Ep − En exactement → absorbé
  (raie noire, ΔEn,p = Ep – En = hν) sinon diffusé ; si hν ≥ énergie d'ionisation Ei → absorbé, reste en énergie
  cinétique de l'électron éjecté ; « un photon d'énergie quelconque peut être absorbé par l'atome d'hydrogène
  pourvu que cette énergie soit au minimum égale à l'énergie d'ionisation ».
- **5.1 En chimie** (p.262) — identique à 223433 p.260 : analyse élémentaire d'un alliage à l'arc électrique
  (position des raies → éléments, intensités → pourcentages) ; spectres d'absorption → identification des molécules.
- **5.2 En astrophysique** (p.262–263) — identique à 223433 p.260–261 : spectre d'étoile = continu + raies noires
  (Fig.18) ; température (étoiles : presque invisibles 1000 °C, Bételgeuse rouge 2500 °C, Soleil jaune 5500 °C,
  Sirius blanche 10000 °C, Rigel bleue 20000 °C) ; composition chimique (raies d'absorption, Fig.19 spectre
  solaire/chromosphère) ; vitesse (effet Doppler-Fizeau, qualitatif : s'éloigne → rouge, se rapproche → violet).

### Encadrés, lois, relations (verbatim, vérifiés sur l'image de 223432)
- F⃗_T/S = − G (mM/r²) u⃗_TS = − F⃗_S/T (p.250) ; F⃗_A/B = k (q_A q_B/r²) u⃗_AB = − k (e²/r²) u⃗_AB = − F⃗_B/A,
  k = 9.10⁹ N.m².C⁻² (p.251).
- W = h.c/λ = h.ν ; h = 6,62.10⁻³⁴ J.s (p.258).
- En = −E0/n² (eV), E0 = 13,6 eV, n entier ≥ 1 ; 1 eV = 1,6.10⁻¹⁹ J (p.259 [coquille imprimée « En/n² »],
  p.264, p.265).
- ΔEn,p = Ep − En = 13,6(1/n² − 1/p²) ; ΔEp,n = En − Ep ; hν = −ΔEp,n ; ΔEp,n = Eo(1/n² − 1/p²) = hνp,n ;
  ΔEp,2 = −Eo(1/2² − 1/p²) (p.260).
- νn,p (exercice résolu) : ν2,1 = (E2 − E1)/h (p.265).
- Valeurs : Hg, transfert 4,9 eV ; H : 10,2 eV ; 121 nm ; 656 / 486 / 434 / 410 nm.

### L'essentiel (p.264, verbatim, encadrés lus sur l'image ; identique à 223433 p.262)
- « L'énergie de l'atome est **quantifiée**, c'est-à-dire qu'elle ne peut prendre qu'une suite de valeurs discrètes. »
- « Dans son état fondamental (état le plus stable), un atome est à son plus bas niveau d'énergie. En lui
  apportant de l'énergie, un atome peut se trouver dans l'un de ses états excités. »
- « On appelle transition atomique tout passage de l'atome d'un niveau d'énergie à un autre. »
- « Lors de l'absorption d'un photon d'énergie hν, l'atome passe d'un niveau d'énergie En à un niveau d'énergie
  Ep supérieure. L'énergie de l'atome varie de [ΔEn,p = Ep − En = hν]. »
- « Lors de l'émission d'un photon d'énergie hν, l'atome passe d'un niveau d'énergie Ep à un niveau d'énergie En
  inférieure. L'énergie de l'atome varie de [ΔEp,n = En − Ep = − hν]. »
- « L'énergie quantifiée de l'atome d'hydrogène est : [En = − E0/n²] en eV, avec n nombre entier supérieur ou
  égal à 1 et E0 = 13,6 eV. »
- « Toute radiation lumineuse de fréquence ν est émise sous forme d'un flux de photons, particules sans masse et
  d'énergie élémentaire W = hν. »
- « Dans un spectre d'émission ou d'absorption, chaque raie représente une transition d'un niveau Ep à un niveau
  En produite par l'émission ou l'absorption d'un photon de fréquence ν telle que : [|Ep − En| = hν]. »
- « Le spectre d'émission ou d'absorption d'un atome constitue «sa carte d'identité». »

### Exercice résolu (p.265 ; identique à 223433 p.263 — énoncé et solution relus sur l'image)
En = − 13,6/n² (en eV). 1°) E1, E2, E3 ; 2°) nom du premier niveau ; 3°) n pour lequel En est nulle, état de
l'atome ; 4°) fréquence émise de E2 à E1 ; 5°) longueur d'onde et domaine spectral. Données h = 6,62.10⁻³⁴ J.s,
c = 3.10⁸ m.s⁻¹, 1 eV = 1,6.10⁻¹⁹ J. Solution : E1 = − 13,60 eV, E2 = − 3,40 eV, E3 = − 1,51 eV ; niveau
fondamental ; n → ∞, atome ionisé (H⁺) ; hν2,1 = E2 − E1, ν2,1 = (E2 − E1)/h = 2,46.10¹⁵ Hz ;
λ2,1 = c/ν2,1 = 122 nm, ultraviolet (la page 223432 imprime « (UV) », 223433 « (U.V) » : seule différence).

### Exercices à résoudre (p.266–269 ; réponses p.319, colonne droite, rubrique « Chapitre 9 ») — tous identiques à 223433 p.264–267
1. *Vrai/faux* (7 items, p.266) — mêmes 7 propositions ; pas de réponse au manuel.
2. *QCM* (6 items, p.266) — mêmes ; item 6 : a) νn,p = h(En − Ep) ; b) h/(En − Ep) ; c) (En − Ep)/h ; pas de réponse.
3. (p.267) H fondamental peut-il absorber 1°) un photon de 8,8 eV ? 2°) un photon λ = 632 nm ? Données E1 = −13,6 ;
   E2 = −3,4 ; E3 = −1,51 ; E4 = −0,85 eV, h, c, 1 eV. — Rép. : 1°) (non) ; 2°) (non).
4. (p.267) Mercure : E3 = −2,72 ; E2 = −3,4 ; E1 = −4,99 ; E0 = −10,45 eV (fondamental). 1°) énergies des photons
   E3→E1 et E2→E0 (eV et J) ; 2°) λ3,1 et λ2,0 ; 3°) dispositif d'observation d'un spectre de raies d'émission. —
   Rép. (étiquettes imprimées) : E4,2 = 2,27 eV = 3,63.10⁻¹⁹ J, E3,1 = 7,05 eV = 11,28.10⁻¹⁹ J ; λ4,2 = 547 nm,
   λ3,1 = 176 nm ; spectroscope à réseau.
5. (p.267) En = −E0/n², E0 = 13,6 eV. 1°) énergies du fondamental, des trois premiers excités, de l'état ionisé,
   diagramme ; 2°) quanta a) 6 eV b) 12,75 eV c) 18 eV au fondamental : absorbés ? état ? 3°) λ dans le vide pour
   n = 4 ; 4°) photon ionisant, électron émis avec une vitesse v : fréquence (h, c, 1 eV, m = 9,1.10⁻³¹ kg). —
   Rép. : E1 = −13,6 ; E2 = −3,4 ; E3 = −1,5 ; E4 = −0,85 eV ; E∞ = 0 ; 2°) c) ionisé ; 3°) λ4,1 = 97,3 nm ;
   4°) νi = 3,29.10¹⁵ Hz.
6. (p.267–268) Même relation. a) n au fondamental ; b) pourquoi des spectres de raies ; c) énergie d'ionisation ;
   d) λ du fondamental à n = 4, domaine ; e) λ émise de n = 2 à n = 1. — Rép. : a) n = 1 ; c) Ei = 13,6 eV ;
   d) λ4,1 = 97,3 nm ; e) λ2,1 = 121,7 nm (pas de réponse pour b).
7. (p.268) En = −13,6/n². a) énergie d'ionisation ; b) Ec minimale d'un électron excitant par choc n=1 → n=2 ;
   c) λ du retour au fondamental ; d) relation littérale de la fréquence n > 2 → n = 2, série, plus grande λ. —
   Rép. : a) Ei = 13,6 eV ; b) E2,1 = 10,2 eV ; c) λ2,1 = 121,7 nm ; d) νn,2 = (En − E2)/h, série de Balmer,
   λ3,2 = 656,7 nm.
8. (p.268) Diagramme « figure 1 » (image, relu) : 0 ; −0,38 (n=6) ; −0,58 (n=5) ; −0,85 (n=4) ; −1,51 (n=3) ;
   −3,4 eV (n=2). 1°) a) E = 0 ; b) fondamental ; c) ionisation ; 2°) flèches des transitions de Balmer et leurs
   énergies ; 3°) plus petite λ émise vers n = 2, visible ? (400–800 nm). — Rép. : 1°) a) ionisation ; b) E1 = −13,6 eV ;
   c) Ei = 13,6 eV ; 3°) λ6,2 = 411 nm (pas de réponse pour 2°).
9. (p.268–269) Désexcitation E2 → E1, λ21 = 1,216.10⁻⁷ m, En = −E0/n² (E0 > 0). 1°) signification du signe
   négatif ; 2°) expliciter E2, E1, relation avec ν21 ; 3°) E0 en J puis eV ; E3 → E1 (λ31, ν31) et E3 → E2 (λ32) ;
   relation entre ν31, ν32, ν21 ; calculer ν32. — Rép. : 2°) ν2,1 = 3/4.Eo/h ; 3°) ν3,2 = ν3,1 − ν2,1.
10. *Étude de texte* « Les quasars, des astres très lointains » (p.269 ; raie d'absorption Lyman alpha à 121,5 nm ;
   « cent mille fois mois denses qu'une bulle de savon » [sic]). 1°) intérêt des quasars ; 2°) schéma Ea, Eb
   (Eb > Ea) et bilan énergétique ; 3°) domaine de Lyman alpha (ultraviolet / visible / infrarouge, tableau à
   cocher). Données h, c, 1 eV, En = −E0/n². — Pas de réponse au manuel.

**En savoir plus (p.270–271)** — « Les modèles de l'atome » : chronologie 1675 (Picard) → 1854 (Geissler, Plücker)
→ 1897 (Thomson) → 1900 (Planck) → 1911 (Rutherford) → 1913 (Bohr) → 1914 (Franck et Hertz valident Bohr) →
1924 (de Broglie) → 1926 (Schrödinger) → 1928 (Dirac) ; nuages de probabilité, fonction d'onde. Identique à
223433 p.268–269. Culture, hors évaluation.

### Écart avec Sciences expérimentales (223433)
**Ce manuel n'ajoute aucune notion, activité ni exercice et n'en retire aucun** dans le chapitre 9 : mêmes sections
1–5, mêmes activités et questions, mêmes valeurs numériques, mêmes 10 exercices + exercice résolu, mêmes réponses,
mêmes coquilles. Constaté par comparaison mot à mot du texte (22 paires de pages) et différence d'image au pixel
près (même mise en page, offset +2). Différences relevées, toutes de forme :
1. **Pas de double page d'ouverture de partie** (223433 p.244–245 : photos spectre solaire, réacteur, explosions,
   sommaire de la partie) : absente de 223432 ; les p.246–247 sont la fin du chapitre 8.
2. **Pagination** : tout le chapitre décalé de +2 ; réponses du chapitre 9 en **p.319** (223433 : p.317).
3. Exercice résolu p.265 : « (UV) » au lieu de « (U.V) » ; Fig.1 p.250 : légende dans un cadre plus haut ;
   p.252 césure « électron-noyau » ; p.254 « hypothèses suivantes » réordonné par la couche texte : même texte.
   « J.s » / « Js » dans les données de l'Ex.5 : même sens.
Aucune différence de valeur, de formule, de consigne ni de réponse. Donc **aucun écart de contenu par rapport à la
section Sciences expérimentales ; le manuel Mathématiques ne contient pas plus que Sciences expérimentales sur ce
chapitre** (ni formule quantitative de l'effet Doppler, ni constante de Rydberg, ni démonstration de En).

### Bornes de scope (section Mathématiques)
Le manuel étant identique, les bornes sont celles de la section 223433 ; rien dans 223432 ne les élargit ni ne
les réduit [?] — le programme officiel de la section Mathématiques peut être plus exigeant que le manuel : ne pas
inférer au-delà de ce qui est imprimé.
✅ **Inclus**
- Variation continue de l'énergie d'un système macroscopique vs échec de la mécanique newtonienne pour l'atome
  (modèle planétaire de Rutherford, rayonnement d'une charge accélérée — qualitatif) ; expressions vectorielles
  des forces gravitationnelle et coulombienne comme rappel.
- Expérience de Franck et Hertz (vapeur de Hg, seuil 4,9 eV, chocs élastiques/inélastiques, lecture de la courbe
  N_C/N_e = f(Ec)) — qualitative, sans circuit électrique détaillé.
- Hypothèses/postulats de Bohr ; niveaux d'énergie, fondamental, excités, état ionisé, transition, diagramme de
  niveaux (lecture et tracé).
- Photon : W = hν = hc/λ ; quantum ; conversions eV ↔ J (1 eV = 1,6.10⁻¹⁹ J), h = 6,62.10⁻³⁴ J.s, c = 3.10⁸ m.s⁻¹.
- Hydrogène : En = −E0/n² (E0 = 13,6 eV) ; calcul de En, de ΔE = |Ep − En| = hν, de ν et λ pour une transition ;
  énergie d'ionisation 13,6 eV ; ΔE = E0(1/n² − 1/p²).
- Séries Lyman (UV), Balmer (visible : Hα 656, Hβ 486, Hγ 434, Hδ 410 nm), Paschen, Brackett, Pfund (IR) ;
  domaines UV / visible (400–800 nm, valeur des exercices) / IR.
- Conditions d'absorption : absorbé seulement si correspondance exacte (sinon diffusé) ; au-delà de Ei, absorption
  avec électron éjecté (Ex.5 4° : hν = Ei + ½mv², via m = 9,1.10⁻³¹ kg).
- Excitation par choc électronique : Ec minimale = ΔE (Ex.7 b).
- Spectres continu / d'émission (raies) / d'absorption (cannelures), renversement des raies, « carte d'identité » ;
  identification d'un élément par superposition de raies.
- Appareillage : spectroscope, spectrographe, spectromètre ; disperseur réseau ou prisme ; montage S, C, F, L, R, E ;
  lampes spectrales (Hg, H) ; vapeur de sodium.
- Applications : analyse élémentaire (alliage à l'arc), spectre stellaire (température par extension vers le violet,
  composition, abondance par noirceur des raies, spectre solaire/chromosphère), Doppler-Fizeau qualitatif.
- Niveaux d'autres atomes (Hg) donnés numériquement dans l'énoncé.
⛔ **Exclu**
- Démonstration de En = −E0/n² (rayon de Bohr, quantification du moment cinétique, rn = n²r1) : absente.
- Constante de Rydberg, formule de Balmer/Ritz nommée, 1/λ = R_H(…) : absentes.
- Formule quantitative de l'effet Doppler (Δν/ν = v/c) ; calcul de vitesse d'étoile ; loi de Wien/corps noir : absents.
- Relation du réseau et dispersion quantitative du prisme (chap. 8 ou absentes).
- Effet photoélectrique, travail d'extraction ; laser / émission stimulée ; fluorescence ; spectres moléculaires.
- Atomes polyélectroniques au-delà de niveaux donnés ; spin, nombres quantiques ; mécanique ondulatoire
  (Schrödinger, de Broglie, Dirac — seulement « En savoir plus »).
- Dispositif électrique de Franck-Hertz (grille, tension retardatrice, courbe I = f(U) à plusieurs pics).
- Noyau, radioactivité, énergie de liaison (chapitres 10–11 de ce manuel, fiche à part).

### Lecture
- **Couche texte (pdftotext)** : p.244–271 intégralement (p.244–247 = fin du chapitre 8, lues pour constater
  l'absence d'ouverture de partie), p.003 (sommaire/avant-propos), p.318–320 (réponses ; p.318 = chap. 1–8 début,
  p.319 = chap. 7–11 dont **chap. 9 en colonne droite**, p.320 = sites web, rien de spécifique au chap. 9).
- **Comparaison automatique** (hors ma lecture visuelle) : pour les 22 paires p.250–271 ↔ 223433 p.248–269,
  différence mot à mot de la couche texte (écarts : numéros de page, césures, « J.s »/« Js », « (UV) »/« (U.V) »,
  signes dégradés) et différence d'image 110 dpi au pixel (seuil 60/255) : les pages p.248, 249, 251, 253, 255, 256,
  257, 258, 261, 262, 263, 264, 266, 267, 268, 269, 270, 271 ne diffèrent que par le numéro de page en pied ;
  p.250, 252, 254, 259, 260, 265 ont de petites différences de mise en page, examinées côte à côte (légende de la
  Fig.1 plus haute, césure, filet de cadre, « (UV) »), sans effet sur le contenu.
- **Pages vues sur image (110 dpi, lecture directe)** — **19 pages** : p.250, 251, 252 (zone utile, côte à côte
  avec 223433), 254 (idem), 256, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 269, 270, 271, **319** (zoom 200 dpi
  de la colonne du chap. 9). S'y ajoutent des découpes côte à côte 223432/223433 des p.259, 260, 265 et la p.248 de
  223433. **Non lues visuellement** : p.248, 249, 253, 255, 257, 263 de 223432 (couche texte lue ; image
  pixel-identique à 223433 p.246, 247, 251, 253, 255, 261, dont la section de référence a lu la page sur image) ;
  Fig.5, 8–10, 12–15, 18, 19 (schémas/photos) donc décrites d'après la section de référence et la couche texte.
- **Sondage** : > 1 page sur 10 parmi les plus denses (p.259, 260, 264, 265, 267, 268, 269 = pages à formules/encadrés/
  exercices) lues sur image, plus zoom p.319 ; écarts texte → image : relations vectorielles (p.250–251) absentes ou
  vides dans la couche texte ; « W = h. c = h. » (p.258) ; « En = /n2 » (p.259) ; formules de 4.4 (p.260)
  désarticulées ; QCM 6 (p.266) fractions éclatées ; données de l'Ex.4–5 entrelacées (p.267) ; flèches « E2 → E1 »
  et λ21/λ31 perdus (p.268–269) ; Fig.7, 16, 17 et diagramme Ex.8 uniquement sur l'image ; indices et exposants
  aplatis partout.
- **Doutes / coquilles du manuel [?]** (toutes identiques à 223433)
  - p.259 : formule imprimée « En = En/n² » sans signe moins, « natuel » — retenu En = −E0/n² (L'essentiel p.264,
    exercice résolu p.265, exercices).
  - Signes incohérents : Q1 p.260 « ΔE2,1 = (E1 − E2) », Fig.16 « ΔE2,1 = E1 − E2 = hν2,1 » vs interprétation
    « ΔE2,1 = E2 − E1 = 10,2 eV » ; ΔE3,2 = E2 − E3 = −1,88 eV (négatif) ; harmoniser par |Ep − En| = hν.
  - Arrondis divergents : λ2,1 = 121 nm (cours) / 122 nm (résolu) / 121,7 nm (réponses) ; ν2,1 = 2,4.10¹⁵ /
    2,46.10¹⁵ Hz ; Hδ 410 nm (cours) vs λ6,2 = 411 nm (rép. Ex.8).
  - p.260 Q3 renvoie aux « raies d'émission observées sur la figure 16 » (la figure 16 est le diagramme de niveaux ;
    les raies observées sont celles de la Fig.11b) [?].
  - Fig.12 légendée « spectre d'émision » alors qu'elle illustre l'absorption ; le montage photographié (lame de
    verre + alcool + eau salée) diffère du texte (« on fait brûler du sodium »).
  - Ex.4 : réponses étiquetées E4,2/E3,1, λ4,2/λ3,1 alors que l'énoncé demande E3→E1 et E2→E0 (valeurs 2,27 eV et
    7,05 eV cohérentes avec E3 − E1 et E2 − E0 ; 2,27 eV = E3 − E1 = −2,72 + 4,99 ; 7,05 eV = E2 − E0 = −3,4 + 10,45) ;
    l'énoncé donne E2 = −3,4 eV pour le mercure (même valeur que H n=2) [?].
  - Ex.5 4°) : « vitesse v » sans valeur ; la réponse νi = 3,29.10¹⁵ Hz correspond au seuil (13,6 eV/h, soit v = 0) [?].
  - Ex.9 3°) : symbole λ31 manquant dans « émet une radiation de longueur d'onde [ ] de même » (image).
  - Pas de réponse au manuel pour Ex.1, 2, 10, Ex.6 b), Ex.8 2°) ; Ex.5 2°) : seulement « c) ionisé ».
  - p.254 : dates de Bohr « (1855-1962) » [coquille probable, non reprise]. Ex.10 « mois denses » pour « moins denses ».
  - Fig.17 : « Bracket » dans le diagramme, « Brackett » dans le texte.
  - [?] Réponses du chap. 9 : un manuel « Mathématiques » identique à « Sciences expérimentales » sur ce chapitre
    — aucune raison interne d'y voir une différence de programme ; à ne signaler que si un document officiel
    (programme) en établit une.

## 2.10 Chapitre 10 — Le noyau atomique (manuel 223432, p.272–285)

Partie « Physique atomique et nucléaire » (bandeau de toutes les pages). Réponses du chapitre : p.319
(colonne droite, bloc « Chapitre 10 ») ; p.318 (chapitres 1 à 6) et p.320 (« Sites Web ») ne contiennent
rien de propre au chapitre 10 (p.320 ne cite qu'un lien CEA « dossier_noyau »).

**Constat général (vérifié page par page)** : ce chapitre est **le même chapitre, mot pour mot, que le
chapitre 10 du manuel Sciences expérimentales 223433 (p.270–283)**, décalé de **+2 pages** (objectifs
p.272 au lieu de p.270 ; réponses p.319 au lieu de p.317). Contrôle : comparaison des 14 pages du chapitre
en couche texte (diff ligne à ligne) ET en image (diff pixel à 110 dpi, tolérance de contraste) ; seules
différences relevées : numéros de page, saut de ligne de l'encadré « Objectifs » (p.272), et la
ponctuation « 931,5 » (p.277 ici) contre « 931.5 » (223433 p.275). Toutes les valeurs numériques, tous les
énoncés, tous les encadrés, les figures et les réponses sont identiques. Section de référence, déjà
transcrite et validée R-7 : `bac-sciences-exp/physique.md` § 2.10 (lignes 4094-4475) — **les doutes [?] de
cette section valent tels quels ici** (reportés en fin de fiche).
Concordance de pages (223432 → 223433) : 272→270 · 273→271 · 274→272 · 275→273 · 276→274 · 277→275 ·
278→276 · 279→277 · 280→278 · 281→279 · 282→280 · 283→281 · 284→282 · 285→283 · 319→317.

**Page objectifs / prérequis (p.272)** — encadrés lus sur l'image ; identique à 223433 p.270.
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

**Page d'ouverture (p.273)** — identique à 223433 p.271 : « LE NOYAU ATOMIQUE » / « 10 » ; deux photos de
cyclotron, légende « Le cyclotron est un exemple d'accélérateur de particules utilisé au laboratoire pour
le développement des recherches sur le noyau atomique. » ; trois questions d'accroche : « Que signifie la
formule emblématique (E = mc²) citée couramment pour évoquer Einsteïn ? » · « Qu'est-ce qui rend certains
noyaux atomiques naturels plus ou moins stables que d'autres ? » · « Qu'est-ce qui fait de l'uranium un
élément chimique précieux dans le domaine du nucléaire ? » (3ᵉ question non reprise dans le chapitre).

**Introduction (p.274)** : « On sait que l'atome, cette plus petite entité insécable de la matière et
électriquement neutre, est constitué d'une partie centrale chargée positivement (le noyau) et d'un cortège
de très petites particules chargées négativement et en mouvement rapide et incessant (les électrons). Ce
chapitre a pour objet l'étude du noyau : structure, cohésion et stabilité. »

**Plan** (identique à 223433) : 1 Structure et cohésion du noyau (Rappels) p.274–275 · 2 Équivalence
masse-énergie : 2.1 Défaut de masse (p.275–276), 2.2 L'énergie de masse (p.276–277) · 3 Stabilité du noyau :
3.1 Énergie de liaison (p.277–278), 3.2 Énergie de liaison par nucléon (p.278), 3.3 Influence du nombre de
masse (p.278–279) · L'essentiel p.280 · Exercices : Exercice résolu p.281 ; Exercices à résoudre : Tests
rapides des acquis (1 Items « vrai ou faux », 2 QCM) p.282, Exercices d'application 3 à 7 p.283,
Exercices de synthèse 8 à 12 p.283–284 · En savoir plus p.285.

### Cours — activités et contenus (identique à 223433 p.272–277 ; seules les valeurs et paragraphes utiles sont relevés)

**1 STRUCTURE ET COHÉSION DU NOYAU (Rappels)** (p.274–275 ; identique à 223433 p.272–273)
- **Activité p.274** : tableau « masses de quatre atomes et de leurs noyaux » (lu sur l'image) :
  ⁴₂He noyau 6,6447 / atome 6,6465 ; ¹²₆C 19,9211 / 19,9266 ; ¹⁴₆C 23,2476 / 23,2531 ; ²³⁵₉₂U 390,1989 /
  390,3021 (toutes en 10⁻²⁷ kg). Questions 1°) comparer masses d'atomes et de noyaux, conclure ; 2°) a) sens
  de Z et A dans ᴬ_Z X ; b) pourquoi « nombre de charge » / « nombre de masse » ; c) Z du noyau ≠ numéro
  atomique ? 3°) ce qui différencie les noyaux de carbone ; 4°) caractère répulsif de l'interaction
  électrique et cohésion du noyau.
- **Contenu (verbatim, p.274–275)** : « Le noyau atomique est constitué de protons et de neutrons appelés
  nucléons. On caractérise le noyau par le nombre de masse A, nombre total de ses nucléons et par le nombre
  de charge Z, nombre total des protons, d'où le symbole ᴬ_Z X. » · « Le noyau est d'une dimension 100000
  fois plus petite que celle de l'atome dont le rayon est de l'ordre de 100 pm. Malgré sa petitesse, il
  renferme la quasitotalité de la masse de l'atome dont il fait partie. » · « Il existe des noyaux de même
  nombre de charge Z mais de nombre de masse A différents : ce sont les noyaux d'isotopes de numéro
  atomique Z. Un élément chimique naturel peut exister sous la forme d'un mélange isotopique de composition
  bien déterminée. » · « La cohésion du noyau est due à une interaction forte qui permet de maintenir les
  protons ensemble malgré leur répulsion. L'expérience montre que des forces nucléaires (forces de courte
  portée) s'exercent entre tous les nucléons du noyau indépendamment de leur nature (protons ou neutrons).
  A une même distance, ces forces attractives sont 100 fois plus intenses que les forces coulombiennes
  répulsives. C'est pour cette raison que les forces nucléaires gouvernent le noyau atomique dont elles
  assurent sa cohésion. »
  **Remarque** : « La notation symbolique ᴬ_Z X est utilisée aussi pour représenter les particules
  élémentaires. Ainsi, le propton [sic] est représenté par ¹₁p, le neutron par ¹₀n. »

**2.1 Défaut de masse** (p.275–276)
- **Exemple + Questions (p.275)** : noyau de lithium ⁷₃Li, m₀ = 7,01435 u, initialement au repos. 1°) montrer que
  1 u = 1,66.10⁻²⁷ kg (u = douzième de la masse d'un atome de ¹²C) ; 2°) a) masse totale m des nucléons
  libres au repos, en u ; b) comparer m₀ et m ; 3°) Δm = m − m₀ ; 4°) justifier l'appellation « défaut de
  masse ». Données : m_C (atome de ¹²C) = 19,93.10⁻²⁷ kg ; m_p = 1,007276 u ; m_n = 1,008665 u. (Pas de
  réponse imprimée ; 6 décimales ici, 5 décimales ailleurs.)
- **Conclusion (p.276)** : « la masse m₀ d'un noyau, immobile, est inférieure à la masse totale m de ses
  nucléons pris séparément et au repos, ce qui nous laisse penser que la formation d'un noyau en ses
  nucléons pris isolément s'accompagne d'une perte de masse Δm = m − m₀ c'est le défaut de masse. » [sic]
- **Encadré Définition (p.276, verbatim, vérifié sur l'image)** : « Le défaut de masse Δm d'un noyau est
  égal à la masse de ses nucléons, pris séparément et au repos, diminuée de la masse du noyau. Pour un noyau
  de symbole ᴬ_Z X : **Δm( X ) = Zm_p + (A-Z)m_n − m_X** ou [sic] m_X est la masse du noyau, m_p celle du
  proton et m_n celle du neutron. » — **Remarque** : « D'après cette définition, le défaut de masse est une
  grandeur positive. »

**2.2 L'énergie de masse** (p.276–277)
- Question d'introduction : « … En quoi est convertie la masse manquante ? » (texte identique 223433 p.274).
- **Principe d'Einstein (p.276, verbatim, gras italique sur l'image)** : « Pour Einstein, la masse est une
  forme d'énergie potentielle. Il postula, en 1905, le principe suivant : “Tout corps au repos dans un
  référentiel donné possède du seul fait de sa masse m, une énergie potentielle appelée énergie de masse
  donnée par la relation : **E₀ = m c²** où c représente la célérité de la lumière dans le vide” »
- « Cette relation, connue sous le nom de relation d'Einstein, traduit une équivalence entre la masse et
  l'énergie : de l'énergie peut se transformer en masse, c'est-à-dire se matérialiser sous forme de
  particule ; inversement la masse peut être convertie en énergie. Par conséquent, tout défaut de masse
  équivaut à une variation d'énergie potentielle de masse : **ΔE = Δmc²**. » — Encart portrait Einstein
  (1879-1955 ; relativité 1905 ; Nobel 1921 ; « savant du siècle » en 2000).
- **Remarque (p.277)** : « Vu que l'unité usuelle de l'énergie est le MeV, d'après la relation d'Einstein,
  la masse m a la dimension d'une énergie par c² : c'est le MeV.c⁻². En particulier, 1u vaut environ
  **931,5** MeV.c⁻². » (ponctuation : virgule ici, point « 931.5 » dans 223433 p.275 — même valeur.)

**3 STABILITÉ DU NOYAU** (p.277–279 ; identique à 223433 p.275–277)
- Introduction : « Tout noyau a une masse m au repos, dans un référentiel donné, inférieure à la masse
  totale de ses constituants (nucléons). Par conséquent, ce défaut de masse qui varie d'un noyau à l'autre
  a-t-il une influence sur leur stabilité ? »

**3.1 Énergie de liaison** (p.277–278)
- **Encadré Définition (verbatim)** : « L'énergie de liaison, notée E_ℓ, est l'énergie qu'il faut fournir à
  un noyau au repos pour le dissocier en nucléons isolés et immobiles. »
- **Question (activité)** : « En utilisant la relation d'Einstein et le principe de la conservation de
  l'énergie, montrer que l'énergie de liaison d'un noyau ᴬ_Z X s'écrit : E_ℓ = Δm.c². »
- **Mise en évidence (p.277–278, formules lues sur l'image)** : dissociation de ᴬ_Z X en ses nucléons, toutes
  particules au repos (« leur énergie de liaison [sic] est purement de masse ») ; avant : E₁ = m_X.c² ;
  après : E₂ = Z.E_p + (A-Z).E_n, avec E_p = m_p.c² et E_n = m_n.c², d'où E₂ = (Z m_p + (A-Z) m_n).c² ;
  Z m_p + (A-Z) m_n > m_X donc E₂ > E₁ ; « Le plus qu'il faut ajouter est l'énergie E_ℓ qu'il faut apporter
  de l'extérieur afin de pouvoir dissocier le noyau. » ; conservation : **E_ℓ + E₁ = E₂**, « D'où :
  E_ℓ = E₂ − E₁ qui peut s'écrire E_ℓ = (Z m_p + (A − Z) m_n).c² − m_X.c² = Δm(X).c². Ainsi, l'énergie de
  liaison d'un noyau est la différence entre la somme des énergies de masse de ses nucléons pris séparément
  et son énergie de masse. »
- **Encadré Conclusion (p.278, verbatim)** : « L'énergie de liaison d'un noyau est une traduction
  énergétique de son défaut de masse : **E_ℓ = Δm.c²**. »

**3.2 Énergie de liaison par nucléon** (p.278)
- Motivation : « Pour évaluer la stabilité d'un noyau et la comparer à celle des autres noyaux, on ne peut se
  fier à la valeur de l'énergie de liaison parce que tous les noyaux n'ont pas le même nombre de nucléons.
  On recourt à l'énergie de liaison par nucléon. »
- **Encadré Définition (verbatim)** : « L'énergie de liaison par nucléon, notée E_ℓ/A est l'énergie moyenne
  de liaison E_ℓ par nucléon. » **Propriété** : « L'énergie de liaison E_ℓ d'un noyau est pratiquement
  proportionnelle au nombre total A des nucléons constitutifs. Alors, E_ℓ/A peut se calculer comme étant le
  quotient de l'énergie de liaison E_ℓ par le nombre de masse A. » — **E_ℓ / A = E_ℓ / A** (fraction E_ℓ
  sur A).

**3.3 Influence du nombre de masse** (p.278–279)
- **Figure courbe d'Aston (p.278, lue sur l'image)** : identique à 223433 p.276 (comparaison pixel à
  pixel : même tracé, mêmes étiquettes). Ordonnée « E_ℓ / A (MeV) » 0–9, valeurs positives, courbe en
  cloche ; abscisse A (graduations 40, 80, 120, 160, 200) ; noyaux étiquetés ²₁H, ⁶₃Li, ¹²₆C, ¹⁶₈O,
  ⁵⁶₂₆Fe, ¹²⁰₅₀Sn, ¹⁸⁴₇₄W, ²⁰⁸₈₂Pb. Valeurs lues à l'œil (approximatives, non imprimées) : ²H ≈ 1 ;
  ⁶Li ≈ 6,7 ; ¹²C ≈ 7,7 ; ¹⁶O ≈ 8 ; ⁵⁶Fe ≈ 8,7–8,8 (sommet) ; ¹²⁰Sn ≈ 8,5 ; ¹⁸⁴W ≈ 8,1 ; ²⁰⁸Pb ≈ 7,9.
- Texte introductif : « Parmi les études quantitatives faites sur l'évolution de E_ℓ/A en fonction de A, on
  retient celle illustrée par la courbe de la figure ci-dessous connue sous le nom de courbe d'Aston. »
- **Texte (p.279, verbatim)** : « La courbe d'Aston est caractérisée par : – un niveau zéro de l'énergie
  correspondant aux nucléons séparés et au repos. – un minimum d'énergie (30 < A < 80) correspondant aux
  noyaux dont les nucléons sont les plus liés, donc les plus stables. Ainsi, la courbe d'Aston permet
  d'illustrer la stabilité relative des noyaux. Les noyaux légers (A < 20) et les noyaux lourds (A > 190)
  sont instables car ils ont une faible énergie de liaison par nucléon tandis que les noyaux de nombre de
  masse moyen (voisin de 60) sont stables parce qu'ils ont l'énergie de liaison par nucléon la plus
  élevée. » [? « minimum d'énergie » vs courbe imprimée à MAXIMUM : voir Doutes 1]
- **Exemple** : « Ayant un nombre de masse A = 56, l'isotope du fer est très stable, ce qui explique sa très
  grande abondance (91,68%) dans la nature. » — **Remarque** : « Etant particulièrement stables, les cinq
  noyaux légers vérifiant A = 2Z font l'exception. »
- **Encadré Conclusion (verbatim)** : « Un noyau est d'autant plus stable que son énergie de liaison par
  nucléon est plus grande. Les noyaux naturels les plus stables sont ceux de nombre de masse voisin de 60 :
  7,8 MeV < E_ℓ /A < 8,8 MeV. »

### L'essentiel (p.280, verbatim, chaque formule encadrée vérifiée sur l'image)

- « Une particule de masse m, au repos dans un référentiel donné, a une énergie de masse :
  **E₀ = m c²** avec c la célérité de la lumière dans le vide. C'est la relation d'Einstein. »
- « La relation d'Einstein traduit l'équivalence masse-énergie. » · « La masse est une forme d'énergie
  potentielle. »
- « La dissociation d'un noyau au repos ᴬ_Z X en nucléons séparés s'accompagne d'un défaut de masse :
  **Δm = Zm_p + (A − Z)m_n − m(ᴬ_Z X) équivalent à ΔE = Δmc²**. »
- « Le MeV et le MeV.c⁻² sont des unités respectivement d'énergie et de masse, adoptées à l'échelle du noyau
  de l'atome. » — encadré **1u = 931,5 MeV.c⁻²**
- « L'énergie de liaison d'un noyau ᴬ_Z X est l'énergie qu'il faut lui fournir quand il est au repos dans un
  référentiel donné, pour le dissocier en nucléons séparés et au repos dans le même référentiel. » —
  encadré **E(ᴬ_Z X) = Δm(ᴬ_Z X).c²** [sic : « E » sans indice ℓ]
- « L'énergie de liaison par nucléon varie avec le nombre de masse A. Plus elle est élevée, plus le noyau est
  stable. » — encadré **E_ℓ / A(ᴬ_Z X) = [E_ℓ / A(ᴬ_Z X)] / A = Δm.c² / A** [sic : numérateur de la fraction
  centrale imprimé « E_ℓ / A(X) » au lieu de « E_ℓ(X) » — coquille ; sens : E_ℓ/A = E_ℓ/A = Δm.c²/A]
- « Les noyaux les plus stables sont ceux dont le nombre des nucléons constitutifs est voisin de 60, ils ont
  une énergie de liaison par nucléon de l'ordre de 8 MeV. »
  (Les trois derniers encadrés : même rendu que 223433 p.278, vérifié par comparaison d'images.)

### Exercice résolu (p.281 ; identique à 223433 p.279)

**Énoncé** : noyau de radon ²²²₈₆Rn, m = 221,97028 u. 1°) a) signification de 86 et 222 ; b) composition ;
c) masse des nucléons séparés, en u. 2°) défaut de masse en u. 3°) a) énergie de liaison en MeV ; b) énergie
de liaison par nucléon en MeV. 4°) « L'énergie de liaison de l'uranium 238 est E_ℓ = 1801,5 MeV. Montrer que
l'uranium 238 est moins stable que le radon 222 bien que son énergie de liaison est plus grande. »
Données : 1u = 1,66.10⁻²⁷ kg = 931,5 MeV.c⁻² ; m_p = 1,00728 u ; m_n = 1,00867 u.
**Solution** : 1°) a) 86 = nombre de charge Z, 222 = nombre de masse A ; b) 86 protons ; N = A − Z = 136
neutrons ; c) m = 86 m_p + 136 m_n = 223,80529 u [? calcul : 223,80520 u]. 2°) Δm = m − m(Rn) = 1,83501 u.
3°) a) E_ℓ = Δm.c² = 1709,3 MeV ; b) E_ℓ/A(Rn) = E_ℓ(Rn)/222 = 7,7 MeV. 4°) « Pour comparer les stabilités
des deux noyaux, on compare leurs énergies de liaison par nucléon et non leurs énergies de liaison. »
E_ℓ/A(U) = E_ℓ(U)/238 = 7,57 MeV ; E_ℓ/A(Rn) > E_ℓ/A(U) : « le radon 222 est plus stable que l'uranium
238 ».

### Exercices à résoudre (p.282–284 ; énoncés, données et réponses identiques à 223433 p.280–282, p.317 → p.319)

Aucune réponse imprimée pour les tests rapides (ex. 1 et 2). Réponses p.319 numérotées 3 à 9 ; **les n°8 et 9
de p.319 répondent aux exercices 10 (lanthane) et 11 (magnésium)** (même décalage de numérotation que
223433) ; ex. 8, 9, 12 sans réponse.

**1 Items « vrai ou faux »** (p.282) — 10 items, identiques : 1- MeV.c⁻² unité de masse « à l'échelle de
l'univers » · 2- argon 40 / potassium 40 isotopes · 3- isotopes : même E_ℓ/A · 4- masse du noyau = somme des
masses des nucléons libres au repos · 5- E_ℓ d'un noyau lourd > celle d'un léger · 6- plus E_ℓ élevée, plus
stable · 7- plus faible E_ℓ/A = plus stable · 8- la courbe d'Aston compare les stabilités · 9- tous les
noyaux A < 20 instables · 10- tous les noyaux lourds A > 200 instables. (Sans corrigé.)

**2 QCM** (p.282, « la (ou les) proposition(s) juste(s) ») — 6 questions I à VI, identiques : I interaction
forte (a- pas entre neutrons, b- très courte portée, c- gravitationnelle) · II masse d'une particule
(a- énergie seulement en mouvement, b- énergie potentielle, c- énergie cinétique [« énégie » sic]) ·
III ²³⁸U (Z = 92) E_ℓ/A = 7,57 MeV, bore 10 (Z = 5) = 6,48 MeV, U plus stable parce que a- masse supérieure,
b- E_ℓ/A la plus grande, c- plus de nucléons, d- E_ℓ la plus grande · IV isotopes : même nombre de
a- protons, b- nucléons, c- neutrons, d- charge · V plus stable si a- E_ℓ/A plus élevée, b- E_ℓ plus
élevée, c- défaut de masse plus faible · VI énergie de liaison = a- énergie libérée à la formation depuis des
nucléons libres au repos, b- énergie à fournir au noyau au repos pour le dissocier en constituants au repos,
c- énergie équivalente au défaut de masse. (Sans corrigé.)

**Exercices d'application (p.283)** — données communes : 1u = 1,66.10⁻²⁷ kg = 931,5 MeV.c⁻² ; m_p = 1,00728 u ;
m_n = 1,00867 u ; 𝒩 = 6,022.10²³.
- **Ex. 3** : masse en u d'un noyau ⁴₂He d'énergie de masse E₀ = 3727,4 MeV. — Rép. p.319 : m = 4,0015 u.
- **Ex. 4** : énergie de masse en MeV de ²³⁸₉₂U, m = 3,952.10⁻²⁵ kg. — Rép. : E₀ = 22,23.10⁴ MeV [? voir 6].
- **Ex. 5** : ⁸⁵₃₇Rb (84,89144 u) et ⁸⁹₃₇Rb (88,89193 u) ; 1°) définir E_ℓ ; 2°) E_ℓ puis E_ℓ/A ; 3°) comparer.
  — Rép. : E₈₅ = 739,685 MeV ; E₈₉ = 771,53 MeV ; E₈₅/A = 8,7 MeV ; E₈₉/A = 8,67 MeV ; Rb(85) plus stable.
- **Ex. 6** : atome ⁴₂He, noyau m₁ = 4,0015 u ; 1°) composition ; 2°) Δm ; 3°) énergie à fournir pour libérer
  ses nucléons ; 4°) avec ³He (m₂ = 3,0149 u) et ⁶He (m₃ = 6,0178 u), classer par stabilité « relative
  croissante ». — Rép. : 2p et 2n ; Δm = 0,0304 u ; E = 28,3176 MeV ; « He(4) > He(6) > He(3) » [ordre
  décroissant imprimé pour une question croissante].
- **Ex. 7** : ²³⁸U (Z = 92), m = 238,0508 u ; 1°) symbole, composition ; 2°) E_ℓ ; 3°) E_ℓ/A ; 4°) énergie W en J
  pour dissocier une mole. — Rép. : E = 1755,67 MeV ; E/A = 7,377 MeV ; W = 1,7.10¹⁴ J. [≠ valeurs de
  l'exercice résolu : 1801,5 MeV et 7,57 MeV.]

**Exercices de synthèse**
- **Ex. 8** (p.283) : noyaux ¹⁶₈O (m₁ = 15,9950 u) et ⁴₂He (m₂ = 4,0026 u) ; 1°) E_ℓ/A ; 2°) plus stable ;
  3°) courbe d'Aston fournie (ordonnée « E_ℓ/A (MeV) » 0–9, A 0–200, sans étiquettes de noyaux) : la
  reproduire, y situer O et He, confirme-t-elle 2°) ? — Pas de réponse. [? masses atomiques, cf. Doutes 7]
- **Ex. 9** (p.284) : 1°) avec la courbe de l'exercice précédent, zone des noyaux les plus stables, en
  déduire le plus stable ; 2°) ¹²C et ²³⁸U : a) E_ℓ/A ; b) E_ℓ, en déduire que E_ℓ ne permet pas de comparer
  leurs stabilités. — Pas de réponse.
- **Ex. 10** (p.284) : 1°) définir E_ℓ ; 2°) a) E_ℓ de ¹³⁹₅₇La en J puis MeV ; b) E_ℓ/A ; 3°) courbe d'Aston
  assimilée à une droite D : y = aA + b pour A ≥ 80 ; a) y pour ⁸⁰₃₄Se et ²³⁵₉₂U, en déduire a et b ;
  b) compatibilité avec 2°b) à 0,1 MeV près. Données : m_La = 138,9060 u, m_U = 235,0439 u,
  m_Se = 79,9165 u. — Rép. (« 8 » p.319) : E = 1136,337 MeV = 1818,14.10⁻¹³ J ; E/A = 8,175 MeV ;
  y_Se = 8,5 MeV ; y_U = 7,395 MeV ; y = −7,13.10⁻³ A + 9,07.
- **Ex. 11** (p.284) : magnésium, 12 protons et 12 neutrons, m_Mg = 23,97868 u ; 1°) symbole du magnésium 24 ;
  2°) E_Mg en fonction de m_Mg et c ; 3°) E_p et E_n en MeV ; 4°) montrer E_ℓ = 12(E_p + E_n) − E_Mg et la
  calculer en MeV. — Rép. (« 9 » p.319) : E_Mg = m_Mg c² ; E_p = 938,28 MeV ; E_n = 939,576 MeV (E_ℓ non
  imprimée).
- **Ex. 12 — Étude de texte « Les noyaux naturels stables »** (p.284) : diagramme N = A − Z (0–150) en
  fonction de Z (0–90), nuage de noyaux stables au-dessus de la droite « Z = N » (lu sur l'image). Texte :
  interactions intranucléaires « de l'ordre du fermi », décroissance exponentielle avec la distance ; « un
  noyau stable, au delà de Z = 20, doit avoir un excès de neutrons (N > Z). Néanmoins, cette condition cesse
  d'être valable pour les noyaux de nombre charge au delà de 83. » Donnée : 1 fermi = 10⁻¹⁵ m. Questions :
  1°) interactions de courte portée ; 2°) combinaisons formant un noyau stable ; 3°) pourquoi Z > N =
  instable. — Pas de réponse.

### En savoir plus (p.285 ; identique à 223433 p.283)

« De l'histoire du noyau atomique » : Rutherford (1911, feuille d'or, particules alpha, modèle planétaire ;
protons 1919), Chadwick (neutron, 1932) ; ≈ 260 noyaux stables (Z de 1 à 83, bismuth) ; radioactivité comme
retour à l'équilibre ; accélérateurs (années 1930), ≈ 3000 noyaux observés, noyaux exotiques. Lecture
culturelle, non évaluée ; aucune fiche technique dans ce chapitre.

### Écart avec Sciences expérimentales

- **Notions : aucune ajoutée, aucune retirée.** Les 4 objectifs, les prérequis, le plan, les définitions,
  lois et relations (Δm, E₀ = mc², ΔE = Δmc², 1u = 931,5 MeV.c⁻², E_ℓ = Δm.c², E_ℓ/A, courbe d'Aston,
  7,8 MeV < E_ℓ/A < 8,8 MeV), l'exercice résolu, les 12 exercices et leurs réponses sont identiques à ceux de
  223433.
- **Activités / manipulations : aucune ajoutée ni retirée** (même activité tableau p.274, même activité
  lithium p.275, mêmes questions documentaires).
- **Exercices : aucun ajouté, aucun retiré, aucune valeur modifiée** (mêmes numéros 1 à 12, mêmes données,
  mêmes réponses, mêmes anomalies de numérotation).
- **Seuls écarts constatés** : (1) pagination +2 (272–285 / réponses p.319 au lieu de 270–283 / p.317) ;
  (2) saut de ligne différent dans l'encadré « Objectifs » (« … énergie de / liaison par nucléon » au lieu de
  « … énergie de liaison par / nucléon ») ; (3) « 931,5 MeV.c⁻² » avec virgule dans la remarque p.277 (« 931.5 »
  avec point dans 223433 p.275 ; l'encadré de l'Essentiel porte la virgule dans les deux manuels) ;
  (4) micro-différences de rendu raster sans contenu (courbe d'Aston p.278, encadrés de l'Essentiel p.280)
  — vérifié visuellement côte à côte : mêmes tracés, mêmes étiquettes, mêmes coquilles.
- Le chapitre de la section Mathématiques ne comporte donc **rien de plus approfondi** (pas de calcul
  relativiste, pas de bilan de réaction, pas de radioactivité) : ces thèmes relèvent, ici aussi, du chapitre
  suivant (« Réactions nucléaires », bandeau p.316/319, début p.286).

### Bornes de scope — section Mathématiques (= celles de Sciences expérimentales)

- ✅ INCLUS :
  - **Structure du noyau** (rappels) : protons, neutrons, nucléons ; A, Z, N = A − Z ; symbole ᴬ_Z X dont ¹₁p
    et ¹₀n ; ordres de grandeur (noyau 10⁵ fois plus petit que l'atome, rayon atomique ≈ 100 pm ;
    quasi-totalité de la masse) ; isotopes, mélange isotopique.
  - **Cohésion** : interaction forte attractive, courte portée (de l'ordre du fermi), indépendante de la
    nature des nucléons, 100 fois plus intense que la répulsion coulombienne à même distance (qualitatif).
  - **Unité de masse atomique** : u = 1/12 de la masse d'un atome de ¹²C = 1,66.10⁻²⁷ kg ;
    1u = 931,5 MeV.c⁻² ; MeV.c⁻² comme unité de masse.
  - **Défaut de masse** Δm = Zm_p + (A−Z)m_n − m_X (en u et MeV.c⁻²), grandeur positive.
  - **Relation d'Einstein** E₀ = mc², ΔE = Δmc² ; énergies de masse (MeV ↔ u ↔ kg ↔ J) ; E_p = m_p c²,
    E_n = m_n c².
  - **Énergie de liaison** E_ℓ = Δm.c² (définition + démonstration par conservation de l'énergie) ;
    E_ℓ = Z E_p + (A−Z) E_n − E_X ; conversion MeV ↔ J ; énergie pour une mole (Avogadro, ex. 7).
  - **Énergie de liaison par nucléon** ; comparaison de stabilité par E_ℓ/A et non par E_ℓ (exercice résolu,
    ex. 9).
  - **Courbe d'Aston** (lecture qualitative et graphique) : A < 20 et A > 190 instables, A voisin de 60 les
    plus stables (7,8 < E_ℓ/A < 8,8 MeV, ordre 8 MeV), fer 56 ; exception des 5 noyaux légers A = 2Z ;
    modélisation affine y = aA + b pour A ≥ 80 (ex. 10 seulement).
  - **Diagramme (N, Z)** des noyaux stables, règle qualitative N > Z au-delà de Z = 20, limite Z = 83
    (étude de texte, ex. 12 seulement).
- ⛔ EXCLU (non traité) :
  - Radioactivité (α, β⁻, β⁺, γ), lois de conservation, décroissance, demi-vie, activité (citée seulement
    dans « En savoir plus ») ; fission, fusion, énergie libérée d'une réaction, centrales, rôle de l'uranium
    (3ᵉ question d'accroche non traitée).
  - Masse des électrons / passage masse atomique ↔ masse du noyau (le tableau p.274 ne sert qu'à une
    comparaison qualitative ; aucun calcul ne retranche Z m_e).
  - Expression quantitative de l'interaction forte, potentiel nucléaire, modèles du noyau (goutte liquide,
    Weizsäcker, couches), relation N/Z quantitative.
  - Relativité au-delà de E₀ = mc² (énergie cinétique relativiste, quantité de mouvement, E² = p²c² + m²c⁴).
  - Fonctionnement du cyclotron / des accélérateurs et détecteurs (photos et lecture culturelle seules).
  - Appareillage expérimental : aucune manipulation ni fiche technique dans ce chapitre.
  - Valeurs de c et de la charge élémentaire non fournies dans les « on donne » (conversion J ↔ eV supposée
    connue, prérequis p.272).

### Lecture

- **Pages lues en couche texte** (`/root/.cache/yqa-manuels/223432/txt/pNNN.txt`) : 272 à 285 (14 pages) et
  318, 319, 320 ; plus diff ligne à ligne des 14 pages contre 223433 p.270–283 (aucune différence de
  contenu) et diff des réponses p.319 / p.317.
- **Pages lues sur l'image** (110 dpi, `pdftoppm`) : **15** — 272, 273, 274, 275, 276, 277, 278, 279, 280,
  281, 282, 283, 284, 285, 319 ; plus les 14 pages correspondantes de 223433 (270–283) rendues à 110 dpi et
  comparées pixel à pixel (seuil de contraste 60/255), zones divergentes (p.272 encadré objectifs ; p.278 et
  p.280 courbe et encadrés) revues en découpes côte à côte. Non vues sur l'image : 318 et 320 (aucun contenu du
  chapitre 10, vérifié en couche texte).
- **Sondage image** : 100 % des pages du chapitre (14/14), dont les plus denses 274, 277, 278, 280, 281, 283,
  284. **Écarts texte/image constatés** (même nature que 223433) : p.272 exposants perdus ; p.274 tableau
  éclaté et « A X / Z » cassé ; p.275 ¹₁p / ¹₀n et ⁷₃Li éclatés ; p.276 indices de Δm(X) aplatis, « Eo » ;
  p.277 E_ℓ rendu « El » ; p.278 fraction E_ℓ/A absente de la couche texte et **courbe d'Aston entièrement
  absente** ; p.280 tous les Δ perdus (« m = Zmp… ») et fraction centrale de l'encadré E_ℓ/A absente — sans
  l'image l'Essentiel serait faux ; p.281 « m = m  m(222 86 Rn) » (Δ et signe moins perdus), fractions
  désarticulées ; p.283 colonnes entremêlées, courbe d'Aston de l'ex. 8 absente, 𝒩 d'Avogadro rendu « N » ;
  p.284 diagramme N = f(Z) absent ; p.319 réponses correctes mais artefact « rsif. » parasite (sans effet).
  Aucun écart ne change le sens des définitions en prose ; toutes les formules et figures de cette fiche
  viennent de l'image.

### Doutes [?] (hérités à l'identique de 223433)

1. **Courbe d'Aston (p.278–279)** : texte « un niveau zéro de l'énergie » et « un minimum d'énergie
   (30 < A < 80) » (lecture de −E_ℓ/A) alors que la figure trace +E_ℓ/A avec un maximum vers A ≈ 60.
   Présenter la courbe telle qu'imprimée sans reprendre « minimum » sans expliquer le signe.
2. **Bornes de zones** : « 30 < A < 80 », « voisin de 60 », « A < 20 » / « A > 190 » (p.279) mais V/F 10
   « A > 200 » ; Essentiel « de l'ordre de 8 MeV » vs conclusion « 7,8 < E_ℓ/A < 8,8 MeV ».
3. **Essentiel p.280** : encadré E(ᴬ_Z X) sans indice ℓ ; numérateur central « E_ℓ / A(X) » (coquille pour
   E_ℓ(X)).
4. **Numérotation des réponses p.319** : n°8 et 9 = exercices 10 et 11 ; ex. 8, 9, 12 et tests rapides sans
   corrigé.
5. **Ex. 6 4°)** : réponse en ordre décroissant pour une question en ordre croissant.
6. **Ex. 4** : 22,23.10⁴ MeV obtenu avec c et e non donnés ; via 1u = 931,5 MeV.c⁻² on trouve ≈ 22,18.10⁴ MeV.
7. **Ex. 8** : 4,0026 u et 15,9950 u sont des masses atomiques (ex. 6 : noyau ⁴He = 4,0015 u).
8. **Exercice résolu** : m = 223,80529 u imprimé, 223,80520 u par le calcul ; Δm = 1,83501 u et
   E_ℓ = 1709,3 MeV imprimés (1709,2 avec 1,83492 u) ; E_ℓ/A = 7,7 MeV inchangé.
9. **U 238 divergent** : exercice résolu / QCM III (1801,5 MeV ; 7,57 MeV) vs ex. 7 (1755,67 MeV ;
   7,377 MeV, m = 238,0508 u) — ne pas mélanger.
10. **Exemple lithium (p.275)** : m_p, m_n à 6 décimales (1,007276 / 1,008665 u) contre 5 ailleurs — garder les
    valeurs propres à chaque énoncé.
11. Valeurs lues sur la courbe d'Aston : approximations à l'œil, non imprimées.
12. Aucun doute nouveau propre à 223432 ; la divergence « 931,5 » / « 931.5 » est typographique.

## 2.11 Chapitre 11 — Réactions nucléaires (manuel 223432, p.286–317)

Partie « Physique atomique et nucléaire » (bandeau de toutes les pages). Réponses du chapitre : **p.319**
(colonne droite, bloc « Chapitre 11 » : exercices 4, 5, 6, 8, 10, 11 seulement) ; p.318 (chapitres 1 à 7)
ne contient rien du chapitre 11 ; p.320 (« Sites Web intéressants ») liste 11 sites sous « Physique
atomique et nucléaire », sans contenu propre.

**Constat central** : ce chapitre est, texte, figures, exercices et réponses, le **même** que le chapitre 11 du
manuel 223433 (section Sciences expérimentales, p.284–315), décalé de **+2 pages** (223432 p.N = 223433 p.N−2).
Comparaison mécanique des 32 pages (mots de la couche texte, page à page) : seuls écarts = numéros de page et
coupures de mots en fin de ligne ; plus relecture de chaque page sur image (liste en « Lecture »). Une seule
variante de contenu relevée (voir « Écart »). Par défaut, tout ce qui suit est donc « identique à 223433 p.(N−2) »
avec la correspondance de pages ci-dessous ; les encadrés et formules sont néanmoins recopiés ici verbatim,
lus sur l'image 223432.

Correspondance : 223432 p.286 = 223433 p.284 (objectifs/prérequis) ; 287 = 285 (ouverture) ; 288 = 286 ;
289 = 287 ; 290 = 288 ; 291 = 289 ; 292 = 290 ; 293 = 291 ; 294 = 292 ; 295 = 293 ; 296 = 294 ; 297 = 295 ;
298 = 296 ; 299 = 297 ; 300 = 298 ; 301 = 299 ; 302 = 300 ; 303 = 301 (L'essentiel) ; 304–307 = 302–305
(exercice résolu) ; 308–309 = 306–307 (tests, application) ; 310 = 308 ; 311–313 = 309–311 (synthèse) ;
314–317 = 312–315 (En savoir plus) ; 319 = 317 (réponses).

**Page objectifs / prérequis (p.286)** — identique à 223433 p.284, lu sur l'image.
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

**Ouverture (p.287)** — identique à 223433 p.285 : trois photos (appareil de scintigraphie, site de
Tchernobyl, centrale thermonucléaire), légende « En même temps que le "nucléaire" est utilisé à des fins
pacifiques, comme pour produire de l'électricité ou pour faire de l'imagerie médicale, il peut avoir des effets
catastrophiques pour la nature et l'humanité. » ; 4 questions d'accroche : principe de datation (éruptions
volcaniques, momies pharaoniques) ; différence centrale thermonucléaire / centrale thermique classique ;
« Qu'est-ce qu'un réacteur nucléaire ? » ; accident de Tchernobyl du 26 avril 1986 (les questions 2 et 4 ne sont
traitées que dans « En savoir plus », p.316–317).

**Introduction (p.288, titre « REACTIONS NUCLÉAIRES »)** : « Selon leur énergie de liaison par nucléon,
certains noyaux sont stables et gardent indéfiniment la même composition. D'autres sont instables et se
transforment spontanément en émettant un rayonnement. Ces noyaux sont dits radioactifs. On parlera alors de
réactions nucléaires spontanées du fait que ces transformations nucléaires se produisent sans intervention
d'agent extérieur. Il est possible également de provoquer la transformation d'un ou de plusieurs noyaux,
relativement stables en d'autres noyaux. On parlera alors de réaction nucléaire provoquée. Pour le grand
public, le nucléaire est un mot qui symbolise le progrès scientifique et technologique d'un pays. Mais, il est
aussi synonyme de danger, source de méfiance et porteur d'inquiétude. Pourtant, l'explication des processus
mis en jeu est relativement simple. »

**Plan du chapitre** (titres du manuel ; deux grandes parties à numérotation propre) :
- **RÉACTIONS NUCLÉAIRES SPONTANÉES — RADIOACTIVITÉ**
  1. Le phénomène de radioactivité (p.288–289)
  2. Les différents types de rayonnements radioactifs — 2.1 Mise en évidence expérimentale (p.289–290) ;
     2.2 Propriétés des rayonnements radioactifs (p.290–292)
  3. Mécanismes nucléaires (p.292) — 3.1 α (p.293) ; 3.2 β⁻ (p.293–294) ; 3.3 β⁺ (p.294) ; 3.4 Émission γ
     (p.294, + Remarque « notion de famille radioactive »)
  4. Évolution temporelle de la radioactivité — 4.1 Décroissance radioactive (p.295) ; 4.2 Activité d'une
     source radioactive (p.295–296) ; 4.3 Période radioactive (p.296) ; 4.4 Application : datation par le
     carbone 14 (p.296–297)
- **RÉACTIONS NUCLÉAIRES PROVOQUÉES** (p.297)
  1. La réaction de fission — 1.1 Définition ; 1.2 Production (p.297–298) ; 1.3 Équation générale
     (p.298–299) ; 1.4 Énergie libérée (p.299)
  2. La réaction « du » fusion [sic] — 2.1 Définition ; 2.2 Production ; 2.3 Énergie libérée (p.300–301)
  3. Applications des réactions de fission et de fusion — 3.1 Énergie du soleil (p.301) ; 3.2 Énergie
     nucléaire (réacteurs, bombe A, bombe H) (p.302)
- puis « L'essentiel » (p.303) · « Exercices » : Exercice résolu (p.304–307) ; Exercices à résoudre — Tests
  rapides des acquis : 1 « vrai ou faux », 2 QCM (p.308–309) ; Exercices d'application 3 à 11 (p.309–310) ;
  Exercices de synthèse 12 à 17 (p.311–313) · « En savoir plus » (p.314–317).

### Cours — activités et contenus (identique à 223433 ; pages 223432 entre parenthèses)

**1 LE PHÉNOMÈNE DE RADIOACTIVITÉ** (p.288–289)
- **Activité documentaire (p.288)** : texte historique — 1896 Becquerel (après les rayons X de Roentgen, 1895),
  plaques photographiques avec du sulfate double de potassium et d'uranium, « rayons uraniques » ; début 1898
  Marie Curie (pechblende, polonium avec Pierre Curie en juillet 1898, nom « radioactivité », radium en
  décembre 1898) ; 1934 Irène et Frédéric Joliot-Curie, radioactivité artificielle (plaque d'aluminium
  bombardée de particules α). Photos : Becquerel (1852-1908), Pierre et Marie Curie, Irène et Frédéric Joliot
  Curie. Questions (p.289) : 1°) ce qui a amené Becquerel à supposer un rayonnement pénétrant ; 2°) ce qui
  montre que Marie Curie, non Becquerel, a découvert la radioactivité ; 3°) corps radioactif d'après le texte ;
  4°) quand la radioactivité est dite artificielle. (Pas de réponse rédigée.)

**2 LES DIFFÉRENTS TYPES DE RAYONNEMENTS RADIOACTIFS** (p.289–292)
- **2.1 Expérience (p.289)** : vers 1899 Becquerel ; sel de radium au fond d'une cavité étroite d'un cylindre de
  plomb à parois épaisses ; écran E perpendiculaire à l'axe ; champ électrique OU magnétique uniforme entre les
  deux ; trois points d'impact A, B, C. Fig.1 (champ magnétique B⃗ ⊗) et Fig.2 (champ E⃗, plaques « − − − » en haut,
  « + + + » en bas) : A dévié vers le haut, C dans l'axe, B dévié vers le bas. Questions : 1°) trois rayonnements
  différents ; 2°) particules positives et négatives d'après les impacts ; 3°) troisième type.
  **Interprétation (p.290)** : A ← charges positives, rayonnement α, noyaux d'hélium (hélions) ⁴₂He ; B ←
  charges négatives, rayonnement β⁻, électrons ⁰₋₁e ; C ← non dévié, photons de très courte longueur d'onde
  (de l'ordre de 10⁻⁴ nm), rayonnement γ.
- **2.2 Propriétés (p.290–292)** : α ~20000 km.s⁻¹, très ionisantes, très peu pénétrantes (plaques très minces
  d'aluminium, feuille de papier, quelques cm d'air) ; β⁻ jusqu'à 290000 km.s⁻¹, moins ionisantes, plus
  pénétrantes (plexiglas ou aluminium de ~7 mm) ; β⁺ : pouvoirs identiques à β⁻ ; γ peu ionisant, très
  pénétrant (plomb, acier ou béton de ~20 cm), Fig.3 ; plaque photographique ; scintillations d'un écran au
  sulfure de zinc ; ionisation des gaz (électroscope, compteur Geiger-Muller, Fig.4) ; indépendance de la
  pression et de la température (« à condition qu'elle ne soit pas excessivement élevée ») ; phénomène nucléaire
  (« il n'est pas nécessaire d'isoler un élément radioactif pour utiliser son rayonnement ») ; APPLICATION :
  traceurs ; effets biologiques (ionisation, ADN, cellule cancéreuse) ; **irradiation** / **contamination**
  (accidentelle ou volontaire, imagerie médicale) définies p.292.

**3 MÉCANISMES NUCLÉAIRES** (p.292–294)
- **Question (p.292)** : (1) ²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He ; (2) ¹⁴₆C → ⁰₋₁e + ¹⁴₇N ; comparer nombres de charge et de
  masse, en déduire les règles. Réponse : lois de conservation (voir « Encadrés »).
- **3.1 α (p.293)** : Question « écrire l'équation générale » ; ᴬ_Z X → ⁴₂He + ᴬ'_Z' Y ; Z = 2 + Z' ; A = 4 + A' ;
  exemples ²¹⁰₈₄Po → ⁴₂He + ²⁰⁶₈₂Pb ; ²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn ; ²³⁸₉₂U → ⁴₂He + ²³⁴₉₀Th.
- **3.2 β⁻ (p.293)** : ¹₀n → ¹₁p + ⁰₋₁e ; exemples ²¹⁰₈₃Bi → ⁰₋₁e + ²¹⁰₈₄Po ; ¹⁴₆C → ⁰₋₁e + ¹⁴₇N ;
  ⁶⁰₂₇Co → ⁰₋₁e + ⁶⁰₂₈Ni ; ¹²₅B → ⁰₋₁e + ¹²₆C.
- **3.3 β⁺ (p.294)** : exemples ³⁰₁₅P → ³⁰₁₄Si + ⁰₁e ; ¹¹₆C → ¹¹₅B + ⁰₁e ; Question « expliquer l'origine de la
  particule ⁰₁e » ; interprétation ¹₁p → ¹₀n + ⁰₁e.
- **3.4 γ (p.294)** : ᴬ_Z Y* (noyau excité) → ᴬ_Z Y + γ. Remarque « famille radioactive » (U 238 → Pb 206).
- **Notation** : positon ⁰₁e (indice « 1 », sans « + ») ; électron ⁰₋₁e ; **aucun neutrino / antineutrino**.

**4 ÉVOLUTION TEMPORELLE DE LA RADIOACTIVITÉ** (p.295–297)
- **4.1 (p.295)** : N₀ noyaux à t = 0, N à t > 0 ; Questions : 1°) comparer N à N₀ ; 2°) « On admet que dN s'écrit :
  dN = − λNdt, avec λ une constante positive » ; a) signe (−) ; b) montrer N = N₀e^(−λt). Réponse rédigée : N < N₀ ;
  dN = nombre moyen de noyaux désintégrés pendant dt ; λ constante radioactive en s⁻¹ ; dN/N = − λdt ;
  ln N = − λt + C ; à t = 0, ln N₀ = C ; ln(N/N₀) = − λt ; N = N₀e^(−λt). Fig.5 : N(t), N₀/2 à T, N₀/4 à 2T.
- **4.2 Activité (p.295–296)** : définition + loi (voir « Encadrés ») ; Fig.6 : A(t), A₀/2 à T, A₀/4 à 2T.
- **4.3 Période (p.296)** : définition, T = ln2/λ = 0.693/λ ; de 10⁻¹⁵ s à 10²³ s. **Tableau (image)** :

  | Noyau radioactif | ²¹⁴₈₄Po | ²¹⁴₈₃Bi | ¹²³₅₃I | ¹³⁷₅₅Cs | ¹⁴₆C | ²³⁸₉₂U |
  |---|---|---|---|---|---|---|
  | Période ou demi-vie | 1,5 10⁻⁴ s | 19,7 min | 13,2 heures | 30,2 ans | 5730 ans | 4,5 10⁹ ans |

- **4.4 Datation par le carbone 14 (p.296–297)** : ¹²₆C et ¹⁴₆C en proportion relative constante dans l'organisme
  vivant ; à la mort ¹⁴₆C ne se renouvelle plus ; β⁻, période 5730 ans ; le rapport ¹⁴₆C/¹²₆C diminue. **Questions
  (p.297)** : charbon de bois, 1,6 désintégrations par minute contre 11,5 pour un échantillon de même masse de
  bois récemment coupé ; 1°) montrer t = − (T/0,693)·ln(A/A₀) ; 2°) T = 5730 ans, calculer t (valeur **non
  imprimée**). Remarque : uranium 238, âge de la Terre estimé à 4,6 milliards d'années.

**RÉACTIONS NUCLÉAIRES PROVOQUÉES** (p.297–302) — « En 1938, on avait abouti à la mise en évidence de la
fission et en 1952, on avait réalisé la première fusion nucléaire (bombe H). »
- **1.1–1.2 Fission (p.297–298)** : définition (« Encadrés ») ; « le plus souvent par des neutrons lents » ; le
  neutron ne subit pas de répulsion ; noyau excité et déformé (Fig.7a) ; noyau le plus utilisé ²³⁵U, aussi ²³³U
  et ²³⁹Pu ; noyaux **fissiles** ; « émission de deux ou trois neutrons » → **réaction en chaîne** (Fig.7b) ;
  non contrôlée → bombe A ; contrôlée → réacteur de centrale.
- **1.3 Questions (p.298–299)** : ᴬ_Z X + ¹₀n → ᴬ¹_Z₁X₁ + ᴬ²_Z₂X₂ + k neutrons ; 1°) a) relations Z/Z₁/Z₂ et
  A/A₁/A₂/k ; b) équation générale ; 2°) ²³⁵U → ¹⁴⁰₅₅Cs + ⁹³_Z₂X₂ + k neutrons : a) Z₂ et X₂ (tableau Br 35, Kr 36,
  Rb 37, Sr 38) ; b) k. Exemples : ¹₀n + ²³⁵₉₂U → ¹⁴⁰₅₅Cs + ⁹³₃₇Rb + 3¹₀n (« objet de la question 2° ») ; → ⁹⁴₃₈Sr +
  ¹⁴⁰₅₄Xe + 2¹₀n ; → ⁹⁵₃₉Y + ¹³⁸₅₃I + 3¹₀n.
- **1.4 Énergie libérée (p.299)** : ¹₀n + ²³⁵₉₂U → ⁹⁵₃₈Sr + ¹³⁹₅₄Xe + 2¹₀n ; E = Δm.c² ; Δm = {m(²³⁵₉₂U) + m(¹₀n)} −
  {m(⁹⁵₃₈Sr) + m(¹³⁹₅₄Xe) + 2 m(¹₀n)} ; m(²³⁵₉₂U) = 234,9934 u (1u = 931,5 MeV.c⁻²), m(¹³⁹₅₄Xe) = 138,8888 u,
  m(⁹⁵₃₈Sr) = 94,8064 u, m(¹₀n) = 1,0087 u ; « la perte de masse qui accompagne la réaction est 0,2115 u, soit
  197 MeV.c⁻² » ; par mole ≈ 2.10¹³ J ou 5,5.10⁶ kWh (Fig.8). **[?]** incohérent : les masses imprimées donnent
  236,0021 − 235,7126 = 0,2895 u (≈ 270 MeV) ; ne pas réutiliser ces données.
- **2 Fusion (p.300–301)** : définition ; ²₁H + ³₁H → ⁴₂He + ¹₀n (Fig.9) ; répulsion électrostatique ; ~10⁸ K
  (« une centaine de millions de degrés ») ; première bombe H, américains, 1952, océan Pacifique (Fig.10 :
  31 octobre 1952). 2.3 Questions : 1°) énergie E de formation de ⁴₂He ; 2°) comparaison avec la fission de ²³⁵U ;
  3°) fusion plus ou moins exoénergétique que la fission, et pourquoi. Rédaction (p.301) : E = Δm.c² ;
  Δm = {m(²₁H) + m(³₁H)} − {m(⁴₂He) + m(¹₀n)} ; m(²₁H) = 2,01355 u, m(³₁H) = 3,01550 u, m(⁴₂He) = 4,00150 u,
  m(¹₀n) = 1,00867 u ; « Δm = 1,888·10⁻² u, soit une libération d'énergie de 17,6 MeV, alors qu'une fission libère
  environ 200 MeV. Cependant, ramenée au nombre de nucléons (5 pour cette fusion et 236 pour la fission), cette
  énergie libérée par fusion est environ cinq fois plus importante que celle d'une fission. » [?] 200/236 → 17,6/5
  donne ≈ 4,2, « environ cinq » est du manuel. Fusion contrôlée ~1 microseconde → pas d'utilisation constructive.
- **3.1 Soleil (p.301)** : ¹₁H + ¹₁H → ²₁H + ⁰₁e ; ¹₁H + ²₁H → ³₂He ; ³₂He + ³₂He → ⁴₂He + ¹₁H + ¹₁H ; bilan
  4¹₁H → ⁴₂He + 2⁰₁e ; ~20 millions de degrés ; 24,7 MeV par noyau d'hélium formé ; 1 kW par m² au sol ;
  chauffe-eau (effet de serre), turboalternateurs, photopiles.
- **3.2 Énergie nucléaire (p.302)** : réacteurs (fission contrôlée ; ²³⁵U et ²³⁹Pu ; propulsion, réseau
  électrique ; noyaux radioactifs d'usage scientifique, industriel ou médical) ; Fig.11 réacteur à eau sous
  pression (caloporteur chaud 320 °C / froid 280 °C) ; bombe A (²³⁵U Hiroshima 6 août 1945, ²³⁹Pu Nagasaki 9 août
  1945, Fig.12) ; bombe H (fusion non contrôlée amorcée par une bombe atomique).

### Encadrés, définitions, lois (VERBATIM, vérifiés sur l'image 223432)

> **Définition** (p.289, encadré vert) — « La radioactivité est la transformation spontanée d'un noyau
> atomique instable en noyau d'une autre espèce chimique, avec émission de rayonnement. Un tel noyau est
> dit radioactif ; il est appelé parfois improprement radioélément. »

> **Conclusion** (p.290, encadré orange) — « • Le rayonnement α est constitué par des particules α (noyaux
> d'hélium ou hélions) de symbole ⁴₂He. • Le rayonnement β⁻ est constitué par des électrons de symbole ⁰₋₁e.
> • La rayonnement γ est constitué de photons. L'étude des particules émises par certains radioéléments
> artificiels révèle l'existence d'une autre particule déviée en sens inverse à l'électron mais de même masse.
> Cette particule a été identifiée à un électron positif ou positon (on dit aussi positron) ⁰₁e. Le
> rayonnement correspondant est le rayonnement β⁺. »

> **Lois de conservation** (p.292, prose en gras) — « Dans chacune des équations (1) et (2) écrites ci-dessus,
> on constate qu'il y a conservation du nombre de charge et du nombre de masse. En fait, la radioactivité
> obéit aux lois de conservation suivantes : - Conservation de l'énergie totale - Conservation de la quantité
> de mouvement (hors programme) - Conservation du nombre de charge : la charge électrique totale du système se
> conserve (loi de SODDY). - Conservation du nombre de masse : la somme des nombres de nucléons des noyaux
> formés est égale à la somme des nombres de nucléons des noyaux initiaux. »

> **Radioactivité α** (p.293) — « Ainsi, l'équation bilan d'une transformation radioactive α (ou désintégration
> α) s'écrit : ᴬ_Z X → ⁴₂He + ᴬ⁻⁴_Z₋₂ Y » (encadrée) ; « Le noyau X désintégré est appelé noyau père ; le noyau Y
> formé est appelé noyau fils. » Remarque : « La radioactivité α concerne les noyaux lourds, noyaux instables à
> cause d'un excès de nucléons (A > 200). »

> **Radioactivité β⁻** (p.293) — « La radioactivité β⁻ correspond à la désintégration d'un noyau ᴬ_Z X en un noyau
> ᴬ'_Z' Y avec émission d'électron. Comme dans le noyau il n'y a pas d'électrons, un neutron se transforme au sein
> du noyau en un proton qui y demeure et un électron qui est éjecté selon l'équation bilan : ¹₀n → ¹₁p + ⁰₋₁e » ;
> équation encadrée : « ᴬ_Z X → ⁰₋₁e + ᴬ_Z₊₁ Y ». Remarque (p.294) : « La radioactivité β⁻ est caractéristique des
> noyaux présentant un excès de neutrons. »

> **Radioactivité β⁺** (p.294) — « La radioactivité β⁺ correspond à la désintégration d'un noyau ᴬ_Z X en un noyau
> ᴬ'_Z' Y avec émission d'un positon ⁰₁e selon l'équation bilan : ᴬ_Z X → ⁰₁e + ᴬ_Z₋₁ Y » (encadrée).
> « Comme le noyau ne contient pas de positons, un proton se transforme au sein du noyau en un neutron qui y
> demeure et un positon qui est expulsé selon l'équation bilan : ¹₁p → ¹₀n + ⁰₁e. La radioactivité β⁺ est
> caractéristique des noyaux présentant un excès de protons. Or, de tels noyaux n'existent pas dans la nature ;
> ils sont produits au laboratoire. On dit qu'il s'agit d'une radioactivité artificielle. »

> **Émission γ** (p.294) — « Le rayonnement γ est dû à l'obtention à un état excité du noyau formé par
> radioactivité α ou β. En fait, il est émis avec le retour de ce noyau à son état fondamental selon le schéma
> suivant : ᴬ_Z Y* (noyau excité) → ᴬ_Z Y + γ. Les rayons γ étant très pénétrants, ils sont utiles et dangereux à
> la fois. En revanche, les rayonnements α et β sont moins dangereux puisqu'ils sont rapidement arrêtés. »

> **Famille radioactive** (p.294, Remarque) — « La radioactivité entraîne la transformation d'un noyau en un
> autre. Si ce dernier est lui même radioactif, il se désintégrera à son tour et ainsi de suite jusqu'à ce que
> le noyau obtenu soit stable. L'ensemble de ces noyaux constitue la famille radioactive du noyau ascendant
> appelé noyau père. La famille la plus connue est celle de l'uranium ²³⁸₉₂U qui conduit à l'isotope stable
> ²⁰⁶₈₂Pb du plomb. »

> **Loi de décroissance radioactive** (p.295) — « Par intégration de la relation : dN/N = − λdt, on obtient :
> ln N = − λt + C […] d'où : ln(N/N₀) = − λt, ce qui conduit à : N = N₀e^(−λt) [encadré]. Cette relation exprime
> la loi de décroissance radioactive (Fig 5). » ; « Etant une caractéristique de l'élément radioactif, λ est
> appelée constante radioactive. Ayant la dimension de l'inverse d'un temps, elle est exprimée en s⁻¹. »
> (dN = − λNdt est admis dans l'énoncé de la Question.)

> **Définition (activité)** (p.295, encadré vert) — « On appelle activité d'une substance radioactive, notée A,
> le nombre de désintégrations qu'elle subit pendant une seconde. »

> **Loi de décroissance de l'activité** (p.296) — « D'après sa définition, l'activité s'écrit : A = − dN/dt. Or,
> dN = − λNdt. Donc, A = λN. Sachant que N = N₀e^(−λt), il vient : A = λ N₀e^(−λt). λN₀ = A₀ activité à l'instant
> t = 0, on a finalement : A = A₀e^(−λt) » (encadrée). « L'activité s'exprime en becquerel (Bq). Un becquerel
> correspond à une désintégration par seconde. »

> **Définition (période)** (p.296, encadré vert) — « On appelle période radioactive ou demi-vie d'une substance
> radioactive, la durée T au bout de laquelle le nombre de noyaux radioactifs initialement présents dans un
> échantillon de cette substance diminue de moitié. » Suite : « A l'instant t = T, on a : N = N₀/2 = N₀e^(−λT), ce
> qui entraîne : 1/2 = e^(−λT). D'où : T = ln2/λ = 0.693/λ » ; « Comme la constante radioactive λ, la période est une
> caractéristique du noyau radioactif ; elle peut varier de 10⁻¹⁵ s à 10²³ s. »

> **Définition (fission)** (p.297) — « La réaction de fission est une réaction nucléaire au cours de laquelle un
> noyau lourd se scinde en deux noyaux plus légers et de masses comparables. »

> **Équation générale de la fission** (p.299, encadrée) — « ¹₀n + ᴬ_Z X → ᴬ¹_Z₁X₁ + ᴬ²_Z₂X₂ + k¹₀n telle que :
> Z₁ + Z₂ = Z, A₁ + A₂ + k = A. »
> [?] Erreur du manuel : avec le neutron incident, A₁ + A₂ + k = A + 1 (exemples p.299 : 140 + 93 + 3 = 236).

> **Énergie libérée** (p.299) — « D'après la loi de conservation de l'énergie totale du système de particules
> mises en jeu, on a : E = Δm.c². »

> **Définition (fusion)** (p.300) — « La fusion est une réaction nucléaire au cours de laquelle deux noyaux
> légers s'unissent pour former un noyau plus lourd. »

> **Réacteur nucléaire** (p.302) — « Un réacteur nucléaire est un appareil servant à réaliser des réactions de
> fission contrôlées. »

### L'essentiel (p.303, verbatim, lu sur l'image)

> ■ Une réaction nucléaire est une transformation au cours de laquelle un ou plusieurs noyau(x) se
> désintègre(nt) en donnant un ou plusieurs noyau(x) nouveau(x) et éventuellement une ou plusieurs particules.
> ■ Une réaction nucléaire peut être spontanée ou provoquée. Dans les deux cas, elle peut être symbolisée par
> une équation qui obéït aux lois de conservation du nombre de masse et du nombre de charge.
> ■ La radioactivité est la transformation spontanée d'un noyau en un autre plus stable avec émission d'un
> rayonnement.
> ■ On distingue trois types de radioactivités : • la radioactivité α (émission d'une particule α : noyau
> d'atome d'hélium ⁴₂He), • la radioactivité β⁻ (émission d'un électron ⁰₋₁e), • la radioactivité β⁺ (émission
> d'un positon ⁰₁e)
> ■ L'émission γ est un phénomène corrélatif qui se produit chaque fois qu'un noyau fils est obtenu à l'état
> excité.
> ■ La loi de décroissance radioactive est : **N = N₀ e^(−λt)** (encadré), avec N₀, le nombre de noyaux présents
> dans l'échantillon à l'instant t = 0 et λ la constante radioactive.
> ■ La demi vie (ou période radioactive) T d'une substance radioactive est la durée au bout de laquelle le
> nombre de noyaux initialement présents diminue de moitié. **T = ln2/λ** (encadré)
> ■ L'activité A d'une substance radioactive est donnée par le nombre moyen de désintégrations par unité de
> temps, A = A₀e^(−λt) où A₀ désigne l'activité à l'instant t = 0.
> ■ A cause du défaut de masse qui en résulte, une réaction nucléaire libère de l'énergie.
> ■ Un noyau lourd subit une réaction de fission lorsque, sous l'action d'un neutron lent, il se scinde en deux
> noyaux de masses comparables.
> ■ La fusion est une réaction nucléaire au cours de laquelle des noyaux très légers fusionnent en un noyau
> moins léger.
> ■ Les énergies libérées par les réactions nucléaires sont énormes ; toutefois, l'énergie libérée par la
> fusion est plus grande que celle libérée par la fission.

### Exercice résolu (p.304–307) — identique à 223433 p.302–305

**Énoncé (p.304–305).** I – 1°) ²³⁵₉₂U + ¹₀n → ⁹⁴_Z Sr + ᴬ₅₄Xe + 2¹₀n : A et Z, lois utilisées. 2°) ²³⁸₉₂U capte un
neutron rapide → U 239 radioactif ; deux β⁻ successives → plutonium : équations, nombres de masse et de charge du
Pu. 3°) a) ²³⁴₉₂U radioactif α : équation, identifier X (tableau : ⁴₂He 4,0015 u ; ²³⁶₉₃Np 235,9956 ; ²³⁴₉₂U 233,9904 ;
²³¹₉₁Pa 230,9860 ; ²³⁰₉₀Th 229,9737) ; b) énergie libérée en MeV et en J par un noyau, puis par 1 g ;
c) énergie répartie en énergie cinétique entre X et α, rapport des Ec = inverse du rapport des masses : Ec(α), Ec(X),
vitesse de α ; d) certaines α ont Ec = 13 MeV, écart expliqué par l'émission γ : énergie des photons et longueur
d'onde λ. II – ²³⁸₉₂U → ²⁰⁶₈₂Pb + xα + yβ⁻ (noyaux intermédiaires négligés) : 1°) x et y ; 2°) à t = 0 pas de plomb ;
N₀, N, N' : a) N' en fonction de t, λ, N ; b) âge en fonction de T et de N'/N (« On pourra supposer t << T et pour ε
petit, on prendra e^ε ≈ 1 + ε ») ; c) 1 g d'U 238 et 10 mg de plomb : âge. Données : T(²³⁸₉₂U) = 4,5 10⁹ ans ;
M(U) = 238 g.mol⁻¹ ; M(Pb) = 206 g.mol⁻¹ ; ln2 = 0,693 ; 1 u = 931,5 MeV.c⁻² ; « 1 MeV = 1,6 10⁻¹⁹ J » [coquille :
la solution utilise 1,6.10⁻¹³ J] ; 𝒩 = 6,02.10²³ ; h = 6,62.10⁻³⁴ J.s ; c = 3.10⁸ m.s⁻¹.

**Solution (p.306–307).** I-1°) 235 + 1 = 94 + A + 2 → A = 140 ; 92 = Z + 54 → Z = 38. 2°) ²³⁹₉₂U → ⁰₋₁e + ²³⁹₉₃X ;
²³⁹₉₃X → ⁰₋₁e + ²³⁹₉₄Pu (X = neptunium Np). 3°) a) ²³⁴₉₂U → ⁴₂He + ᴬ_Z X, A = 230, Z = 90 : ²³⁰₉₀Th. b) Δm = 233,9904 −
[4,0015 + 229,9737] = 1,52.10⁻² u ≈ 14,16 MeV.c⁻² ; W₁ = 14,16 MeV, soit 2,26.10⁻¹² J ; W = (m𝒩/M)·W₁ = 3,64.10²² MeV, soit
5,8.10⁹ J. c) W = Ec(α) + Ec(Th) (1) ; Ec(α)/Ec(Th) = m_Th/m_α ; Ec(α) = m_Th·Ec(Th)/m_a (2) [indice « a » : coquille] ;
Ec(Th)[1 + m_Th/m_α] = W d'où (encadré) Ec(Th) = m_α/(m_α + m_Th)·W et Ec(α) = m_Th/(m_α + m_Th)·W ; Ec(Th) = 0.242 MeV ;
Ec(α) = 13.918 MeV ; Ec(α)/W·100 = 98,2 % ; Ec(α) = ½m_α v_α² d'où ‖v⃗_α‖ = √(2Ec(α)/m_α) = 2,59.10⁷ m.s⁻¹. d) Eγ = 13,918 −
13,000 = 0,918 MeV ; Eγ = hc/λ d'où λ = hc/Eγ = 1,35.10⁻¹² m. II-1°) 238 = 206 + 4x et 92 = 82 + 2x − y → x = 8, y = 6.
2°) a) N' = N(e^(λt) − 1) (encadré) ; b) N'/N = e^(λt) − 1 = e^((ln2/T)t) − 1 ≈ (ln2/T)t, d'où t = (N'/N)·(T/ln2) ;
c) N = m_U𝒩/M_U, N' = m_Pb𝒩/M_Pb, t = (m_Pb/m_U)(M_U/M_Pb)(T/ln2) = 75.10⁶ ans.

### Exercices à résoudre (p.308–313) — identiques à 223433 p.306–311 (énoncés, données, figures)

**1 « vrai ou faux » (p.308)** — 10 items : radioactivité transformation nucléaire spontanée ; toujours lente ;
noyaux désintégrés ne dépendent que du temps ; activité proportionnelle au temps ; demi-vie = durée au bout de
laquelle la masse diminue de moitié ; conservation de la charge et du nombre de nucléons toujours respectées ;
fission et fusion spontanées ; bombe H amorcée par une fission ; énergie du soleil ¹₁H → ⁴₂He ; γ beaucoup plus
pénétrant que α et β, nombreuses ionisations, très dangereux. (Pas de corrigé.)

**2 QCM (p.308–309)** — I à X : réaction nucléaire et catalyseur/pression ; radioactivité phénomène nucléaire ;
spontanée/provoquée ; loi N = N₀e^(−λt) / N₀e^(λt) / N₀(1 − e^(−λt)) ; période (moitié / quart / augmente de la
moitié) ; conservation (nucléons / charge / les deux) ; même N, demi-vie plus courte → activité initiale
supérieure/inférieure/égale ; γ en médecine ; fission ; fusion. (Pas de corrigé.)

**Application (p.309–310)**
- **3** — tableau A ²¹⁴Po (N = 130), B ²¹⁰Pb (Z = 82), C Bi (A = 210, Z = 83), D Po (A = 210, N = 126), E Pb
  (Z = 82, N = 124) ; compléter A → B, B → C, C → D, D → E, particule émise. (Pas de réponse.)
- **4** — ²³⁸U → ²²⁶₈₈Ra (x α, y β⁻) ; ²²⁶Ra → ²⁰⁶₈₂Pb (x' α, y' β⁻). Réponse p.319 : x = 3, y = 2, x' = 5, y' = 4.
- **5** — ²¹⁸₈₄Po → ᴬ_Z Pb + α ; 1°) équation et lois ; 2°) m₀ = 40 mg, « à un instant de date t = 0,54 minutes plus
  tard » m = 10 mg [?] : T et λ. Réponse : ²¹⁸₈₄Po → ⁴₂He + ²¹⁴₈₂Pb ; T = 27 min ; λ = 4.27.10⁻⁴ s⁻¹ (« D'après Bacc.
  Juin 2004. Session principale. Section sport »).
- **6** — ²²⁶₈₈Ra → α + ᴬ_Z Rn ; M(α) = 4,0015 u ; M(Rn) = 221,9703 u ; M(Ra) = 225,9771 u ; 1u = 1,66 10⁻²⁷ kg ;
  c = 3 10⁸ m.s⁻¹ : énergie libérée. Réponse : ²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn ; W = 7.9 10⁻¹³ J.
- **7** — Bethe et Critchfield (1938) : (1) ⁰₋₁e + 2¹₁H → X ; (2) X + ¹₁H → Y ; (3) Y + ⁴₂He → Z ; (4) Z + ⁰₋₁e → T ;
  (5) T + ¹₁H → 2⁴₂He ; équilibrer, identifier X, Y, Z, T (tableau H … He / Li Be B C N O F Ne) ; bilan et type de
  réaction. (Pas de réponse ; ⁰₋₁e en réactif aux équations (1) et (4), transcrit tel quel.)
- **8** — 1°) ²³⁵₉₂U + ¹₀n → ¹⁴⁶ₓLa + ⁸⁷₃₅Br + y¹₀n : a) x, y ; b) origine de l'énergie ; 2°) ²³⁸U + X → ²³⁹U ;
  ²³⁹U → ²³⁹Np + Y ; ²³⁹Np → ᴬ_Z Pu + Y : a) X, Y ; b) A, Z. Réponse : x = 57, y = 3 ; défaut de masse ; X neutron
  ¹₀n, Y électron ⁰₋₁e ; A = 239, Z = 94.
- **9** — ⁶₃Li + ¹₀n → ⁴₂He + X ; ²₁H + X → ⁴₂He + Y ; X, Y ; équation bilan. (Pas de réponse.)
- **10** — 1°) a) ²³⁸U + n sans rayonnement ; b) → ²³⁹₉₄Pu, nombre et nature des particules ; 2°) ¹₀n + ²³⁵₉₂U → ᴬ₃₈Sr +
  ¹⁴⁰_Z Xe + 2¹₀n : A, Z, type. Réponse : ²³⁸₉₂U + ¹₀n → ²³⁹₉₂U ; ²³⁹₉₂U → 2⁰₋₁e + ²³⁹₉₄Pu ; A = 94, Z = 54 ; fission.
- **11** — ⁷⁷₃₅Br émetteur β⁺ → isotope du sélénium, période 57 h : 1°) équation ; 2°) λ ; 3°) A₀ = 5,7.10¹⁵ Bq : N₀.
  Réponse : ⁷⁷₃₅Br → ⁰₁e + ⁷⁷₃₄Se ; 3.38 10⁻⁶ s⁻¹ ; 1.68 10²¹.

**Synthèse (p.311–313)** — aucune réponse au manuel (p.319 s'arrête à l'exercice 11).
- **12** — A : ²¹⁰₈₄Po α → plomb ; énergie entièrement cinétique, Ec inverse du rapport des masses : Ec(α), Ec(Pb) en
  MeV, vitesses ; M(α) = 4,0015 u, M(²¹⁰₈₄Po) = 209,9368 u, M(²⁰⁶₈₂Pb) = 205,9295 u, 1 u = 931,5 MeV.c⁻², c = 3·10⁸ m.s⁻¹.
  B : ¹³⁷₅₅Cs β⁻ → ᴬ_Z Ba (état fondamental ou excité). I-1°) A, Z, équation ; 2°) énergie en MeV et J (m(⁰₋₁e) = 5,5.10⁻⁴ u,
  Cs 136,8768 u, Ba 136,8743 u ; 1 eV = 1,6.10⁻¹⁹ J), formes de cette énergie ; II- λ = 8,4.10⁻¹⁰ s⁻¹ : T en s et en années.
- **13** — carbone : ¹²C 98,9 %, ¹³C 1,1 %, ¹⁴C (T = 5730 années) ; 1°) relation λ–T ; 2°) 13,6 désintégrations par minute
  et par gramme dans le cycle du CO₂ ; bois de navire Viking mesuré en 1983 : 12 par minute et par gramme : année
  d'abattage ; 3°) rapport isotopique ¹²C/¹⁴C. Données : 1 année = 365 jours ; 𝒩 = 6,02.10²³ mol⁻¹.
- **14** — ²²⁶₈₈Ra → α + ᴬ_Z X (radon) ; 1°) équation et règles ; 2°) tableau t (h) 0 à 200 par pas de 20 / ln N : 6,90 ; 6,75 ;
  6,60 ; 6,45 ; 6,30 ; 6,15 ; 6,00 ; 5,85 ; 5,70 ; 5,55 ; 5,40 — a) tracer ln N = f(t) ; b) loi ; c) T en jours ; 3°) rapport
  Ec(noyau)/Ec(α) = inverse des masses ; 4°) énergie libérée 4,5 MeV, vitesse de α ; 5°) λ = 2,5.10⁻¹¹ m : a) interpréter ;
  b) Ec(α) compte tenu du photon. Données : He 4,0015 u ; radon 221,9771 u [?] (ex. 6 : 221,9703 u) ; 1 u = 1,67.10⁻²⁷ kg ;
  c = 3.10⁸ m.s⁻¹ ; h = 6,63.10⁻³⁴ J.s ; 1 eV = 1,6.10⁻¹⁹ J (D'après Bacc. Juin 1997).
- **15** — scintigraphie (gammacaméra) : I-1°) ¹²³I produit par deutons ²₁H sur ¹²²₅₂Te : équation ; 2°) ¹³¹₅₃I (T = 8 jours)
  β⁻ et γ → xénon : équation, énergie en MeV (m(¹³¹₅₃I) = 130,87705 u ; m(Xe) = 130,87545 u ; m(⁰₋₁e) = 5,486.10⁻⁴ u ;
  1u = 931,5 MeV.c⁻²) ; 3°) activité après 24 h en fonction de A₀. II-1°) ¹²³I γ pur, T' = 13,2 h, A = 6,4.10⁶ Bq : tracer A(t)
  aux points T, 2T, 3T, 4T… ; 2°) activité graphique au bout de 4 h, puis à 24 h.
- **16** — ⁶⁰₂₇Co β⁻, T = 5,27 ans, noyau fils excité, deux rayonnements 1,6.10⁻¹² m et 1,8.10⁻¹² m (bombe à cobalt) ; 1°)
  équations de désintégration et de désexcitation ; 2°) durée pour perdre 90 % de l'activité ; 3°) électron 4,5.10⁻¹⁴ J,
  activité 1,7.10¹⁸ Bq, 10 % vers la cible : énergie par unité de temps ; 4°) énergie pour 0,8 s ; 5°) comparaison avec 10 s
  près d'une source de ~10¹⁴ Bq jugée dangereuse.
- **17** — Étude de texte (Becquerel, 26 février 1896, sulfate double d'uranium, plaques développées quatre jours plus
  tard ; 1898 Pierre Curie propose « radioactivité » ; citation de Jean Becquerel). Questions 1°) part du hasard et de la
  perspicacité ; 2°) nature du rayonnement invisible ; 3°) nom donné par Becquerel ; 4) pourquoi c'est une propriété de
  l'élément uranium.

### En savoir plus (p.314–317) — identique à 223433 p.312–315

Usages médicaux (scintigraphie à l'iode 123, radioprotection) · Rayonnements et santé (pénétration α quelques µm,
β quelques mm, γ indirectement ionisant ; irradiation / contamination ; dose énergétique en gray, 1 Gy = 1J.kg⁻¹ ;
équivalent de dose en sievert, Q (Sv.Gy⁻¹) : α 20, β 1, γ 1, x 1 ; effets somatiques précoces/tardifs, foeto-embryonnaires
(> 0.05 Sv) ; tableau « Effet d'une dose sur l'homme ( très simplifié) » < 1, 1–2, 2–5, 5–9, > 9 Sv, d'après Electricité de
France) · Énergie nucléaire et électricité (centrale thermique vs nucléaire ; cœur = combustible + modérateur + fluide
caloporteur ; barres de réglage et de sécurité ; gaine, cuve, enceinte de confinement ; Tchernobyl « en Ukraine
(Russie) » 26 avril 1986 : une trentaine de morts, césium 137, 130000 habitants évacués ; Fig.2–3). Aucun exercice.

### Écart avec Sciences expérimentales (223433)

- **Ce que ce manuel ajoute** : **rien** — aucune notion, activité, exercice, figure ou réponse supplémentaire
  (les 17 exercices, leurs données et les réponses 4, 5, 6, 8, 10, 11 sont identiques ; mêmes coquilles du manuel :
  « 1 MeV = 1,6 10⁻¹⁹ J », « A₁ + A₂ + k = A », « t = 0,54 minutes », titres « DU FUSION », « m_a »).
- **Ce que ce manuel retire** : **rien**.
- **Seule variante de contenu relevée** : p.301 (= 223433 p.299), « Δm = **1,888**·10⁻² u » ici contre « 1,888**0**·10⁻² u »
  dans 223433 (même valeur, un zéro final de moins ; le rapport 17,6 MeV est inchangé). Autres variantes : uniquement
  mise en page (numérotation +2 pages ; réponses du chapitre p.319 au lieu de p.317 ; coupures de mots de fin de
  ligne ).
- Conséquence : la section 2.11 de `bac-sciences-exp/physique.md` (L.4476–4993) s'applique telle quelle au Bac
  Mathématiques, avec la table de pages ci-dessus ; la différence de section ne tient qu'aux ⛔/✅ de scope
  (ci-dessous), à confirmer contre le programme officiel (R-3, non consulté ici).

### Bornes de scope (section Mathématiques) — transposées du manuel, programme officiel non consulté

- ✅ INCLUS (cours) : radioactivité (définition, spontanée, nucléaire, indépendante de P et T, noyau père/fils) ;
  **α, β⁻, β⁺, γ** : nature (⁴₂He, ⁰₋₁e, ⁰₁e, photons), déviation en champ E ou B (lecture qualitative du signe de charge),
  pouvoirs d'ionisation et de pénétration (ordres de grandeur) ; **lois de conservation du nombre de charge (Soddy) et
  du nombre de masse**, conservation de l'énergie totale ; équations-bilans α (A − 4, Z − 2), β⁻ (Z + 1), β⁺ (Z − 1),
  désexcitation γ ; n → p + e⁻, p → n + e⁺ ; famille radioactive, recherche de x α et y β⁻ ; **loi de décroissance**
  dN = − λNdt (admise), N = N₀e^(−λt), λ (s⁻¹) ; **activité** A = − dN/dt = λN = A₀e^(−λt), becquerel ; **période**
  T = ln2/λ, durées multiples de T, courbes N(t) et A(t) ; **datation au carbone 14** (t = −(T/ln2)·ln(A/A₀)) ; **fission**
  (neutron lent, fissiles ²³⁵U/²³³U/²³⁹Pu, réaction en chaîne, équation générale, A₁ + A₂ + k = A + 1) ; **fusion**
  (²H + ³H, 10⁸ K) ; **E = Δm.c²** (u, MeV.c⁻², MeV, J ; par noyau, par gramme, par mole) ; comparaison fission/fusion
  par nucléon ; cycle du soleil ; réacteurs, bombe A, bombe H (descriptif).
- ✅ INCLUS (mobilisé en exercice résolu / exercices) : répartition de l'énergie cinétique (rapport inverse des masses,
  donné dans l'énoncé), Ec = ½mv² ; Eγ = hc/λ ; datation U/Pb avec N' = N(e^(λt) − 1) et e^ε ≈ 1 + ε ; N = m𝒩/M ; tracé de
  ln N = f(t) ; activité et énergie par unité de temps (ex. 16) ; durée pour perdre un pourcentage d'activité.
- ⛔ EXCLU : **conservation de la quantité de mouvement** (« hors programme », p.292) ; **neutrino/antineutrino** (absents) ;
  **capture électronique**, β⁺ naturelle (le manuel dit que ces noyaux n'existent pas dans la nature) ; calcul de
  trajectoires dans les champs ; courbe d'Aston et énergie de liaison (chapitre 10, prérequis) ; **dosimétrie** (gray,
  sievert, Q : « En savoir plus » seulement) ; technologie détaillée des réacteurs (« En savoir plus ») ; énergie cinétique
  relativiste ; constante de temps τ = 1/λ et vie moyenne (non nommées) ; démonstration de dN = − λNdt (admis) ; séries
  couplées / équilibre séculaire.

### Lecture

- **Couche texte** : pages 286 à 320 lues (les 35 pages), `/root/.cache/yqa-manuels/223432/txt/pNNN.txt`, et comparées
  mot à mot, page par page, à `223433/txt/p(N−2).txt` (p.286–317 ; p.318–319 : blocs « Réponses » — contenu du chapitre 11
  identique ; p.320 = p.318 de 223433).
- **Pages vues sur image** (110 dpi, `pdftoppm`) : **32 sur 32 du chapitre** — 286, 287, 288, 289, 290, 291, 292, 293, 294,
  295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317 ;
  **+ p.319** (zoom 150 dpi sur le bloc « Chapitre 11 », réponses 4 à 11 relues) **+ 223433 p.299 (image, comparaison de la
  ligne Δm)**. **Total : 34 images** (33 de 223432 + 1 de 223433). p.318 et p.320 lues en texte seulement (aucun contenu du
  chapitre 11 hors liste de sites).
- **Sondage** : fait sur la totalité du chapitre ; pages les plus denses relues : 293–296, 299, 301, 304–307, 309–312, 319.
  **Écarts couche texte / image** : formules, indices, ln, λ, Δ (rendu « D » sur p.301/306), flèches, équations de réponse
  p.319 disloquées en texte ; aucune formule de cette fiche n'est prise à la couche texte seule. Écart de fond texte ↔ 223433 :
  aucun, hors « 1,888 / 1,8880 » (p.301).
- **Doutes [?]** (tous hérités du manuel, présents à l'identique dans 223433) : (1) p.299 perte de masse 0,2115 u / 197 MeV
  incompatible avec les masses imprimées (0,2895 u) ; (2) p.305 « 1 MeV = 1,6 10⁻¹⁹ J » (solution : 10⁻¹³) ; (3) p.309 ex. 5
  « t = 0,54 minutes » lu « t = 0 ; 54 minutes plus tard » ; (4) p.301 « environ cinq fois » (≈ 4,2) ; (5) p.307 « m_a » ;
  (6) masse du radon 221,9703 u (ex. 6) vs 221,9771 u (ex. 14) ; (7) ex. 7 ⁰₋₁e en réactif ; (8) coquilles de titres
  (« DU FUSION », « DÉFINITON », « ENERIGIE », « SOURCE RADIATIVE ») ; (9) p.299 « A₁ + A₂ + k = A » (lire A + 1) ;
  (10) réponses absentes : ex. 1, 2, 3, 7, 9, 12 à 17 et valeur numérique de la datation p.297 ; (11) programme officiel
  Bac Mathématiques non consulté (R-3) : statut des notions vues seulement en exercice (répartition des Ec, U/Pb, Eγ = hc/λ) à
  confirmer . Ce manuel ne contient aucune notion absente de 223433.

## 3. Audit R-7 (2026-11-06)

Relecture indépendante (auditeur en contexte vierge, opus) de chaque chapitre **contre le PDF lui-même** : 100 % des encadrés, lois et relations transcrits confrontés à l'image de la page, 100 % du plan, et le reste par sondage, en priorité les écarts annoncés avec Sciences expérimentales. Corrections appliquées par un correcteur sur l'image de la page, puis revérifiées par un second auditeur opus.

| Chapitre | Pages sondées en image | Corrections fiche |
|---|---|---|
| 01 condensateur-dipole-rc | 16 | 3 |
| 02 bobine-dipole-rl | 16 | 3 |
| 03 oscillations-electriques-libres | 8 | 0 |
| 04 oscillations-electriques-forcees | 16 | 0 |
| 05 oscillations-libres-pendule-elastique | 12 | 0 |
| 06 oscillations-mecaniques-forcees | 14 | 1 |
| 07 ondes-mecaniques-progressives | 17 | 2 |
| 08 nature-ondulatoire-lumiere | 21 | 2 |
| 09 Spectre atomique | 11 | n/d |
| 10 | n/d | n/d |
| 11 | n/d | n/d |

Total : 11 corrections, 131 pages sondées en image par les auditeurs (sur 320).
