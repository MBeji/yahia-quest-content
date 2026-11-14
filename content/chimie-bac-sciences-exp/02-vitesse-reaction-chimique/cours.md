# ⏱️ Vitesse d'une réaction chimique — mettre un nombre sur la rapidité

> 💡 «Une réaction ne se dit pas seulement “rapide” ou “lente” : on la chronomètre, on trace sa courbe, et la pente de cette courbe est sa vitesse.»

Un comprimé effervescent disparaît en une minute dans un verre d'eau, alors qu'un clou rouille pendant des mois : comment mettre un nombre sur cette différence ? Sept notions te donnent les outils : comparer la rapidité de deux transformations, suivre l'avancement x au fil du temps, la vitesse moyenne, la vitesse instantanée, la relation avec les concentrations, le suivi par le volume d'un gaz, et l'évolution de la vitesse au cours du temps. On suppose acquis l'avancement x, le tableau descriptif, le réactif limitant et le temps de demi-réaction (chapitre 1), ainsi que la dérivée et la tangente à une courbe (mathématiques).

## 🧪 Comparer la rapidité de deux transformations

Deux béchers contiennent chacun un mélange d'eau oxygénée, d'ions iodure et d'acide : H₂O₂ + 2 I⁻ + 2 H₃O⁺ → I₂ + 4 H₂O. On y a ajouté 2,0 mL de thiosulfate de sodium à 2,0·10⁻² mol·L⁻¹ et de l'empois d'amidon. Tant qu'il reste du thiosulfate, il consomme le diiode dès qu'il se forme ; l'amidon devient bleu-noir à l'instant précis où le thiosulfate est épuisé. Le bleu apparaît après 40 s dans le bécher S₁, après 25 s dans S₂.
Quelle transformation est la plus rapide, et pourquoi la comparaison est-elle équitable ?

::: definition
**Comparer la rapidité** — Pour comparer deux transformations, on fixe l'une des deux grandeurs et on compare l'autre : soit la variation d'avancement Δx pour une même durée Δt, soit la durée Δt pour une même variation d'avancement Δx. La plus rapide est celle qui atteint le plus grand Δx pendant la même durée, ou le même Δx en la plus courte durée.
:::

| bécher | thiosulfate ajouté        | durée avant le bleu |
| ------ | ------------------------- | ------------------- |
| S₁     | 2,0 mL à 2,0·10⁻² mol·L⁻¹ | 40 s                |
| S₂     | 2,0 mL à 2,0·10⁻² mol·L⁻¹ | 25 s                |

Les deux béchers reçoivent la même quantité de thiosulfate : l'apparition du bleu marque donc le même avancement dans les deux, et seules les durées diffèrent.

::: exemple Comparer S₁ et S₂ à avancement égal

1. Dans chaque bécher, n(S₂O₃²⁻) = C·V = 2,0·10⁻² × 2,0·10⁻³ = 4,0·10⁻⁵ mol, car on connaît la concentration et le volume versé.
2. Le diiode formé réagit selon I₂ + 2 S₂O₃²⁻ → S₄O₆²⁻ + 2 I⁻ : il faut 2 mol de thiosulfate pour 1 mol de diiode, donc 4,0·10⁻⁵ mol de thiosulfate consomment 2,0·10⁻⁵ mol de I₂.
3. Le bleu apparaît quand le thiosulfate est épuisé : le diiode formé a alors exactement compensé ce qui a été consommé, donc n(I₂) = 2,0·10⁻⁵ mol. Le coefficient de I₂ vaut 1, d'où x = 2,0·10⁻⁵ mol dans S₁ comme dans S₂.
4. Même Δx : 25 s dans S₂ contre 40 s dans S₁. Le même avancement est atteint plus tôt dans S₂, qui est la transformation la plus rapide.
5. Contrôle : S₁ gagne 2,0·10⁻⁵/40 = 5,0·10⁻⁷ mol d'avancement par seconde, S₂ gagne 2,0·10⁻⁵/25 = 8,0·10⁻⁷ mol par seconde : S₂ avance plus vite, ce que la notion 3 formalisera.

:::

::: piege
**Erreur : comparer deux durées quand l'avancement n'est pas le même.** Un bécher S₃ reçoit 4,0 mL du même thiosulfate : le bleu y apparaît après 50 s, plus tard que dans S₁ (40 s). Conclure « S₃ est plus lent » est faux : S₃ a atteint x = 4,0·10⁻⁵ mol, deux fois plus qu'à la fin de S₁, soit 4,0·10⁻⁵/50 = 8,0·10⁻⁷ mol par seconde, plus que les 5,0·10⁻⁷ de S₁. L'erreur tente parce que « la durée la plus courte gagne » est vraie, mais seulement à Δx égal.
:::

::: propriete
**Rapidité et avancement** — À Δx égal, la transformation la plus rapide est celle de plus courte durée ; à Δt égal, c'est celle de plus grand Δx. Si ni l'un ni l'autre n'est égal, on calcule Δx/Δt pour chacune (notion 3).
Cas limite : deux mélanges qui contiennent les mêmes quantités de réactif limitant atteignent le même avancement final, quelle que soit leur rapidité. L'avancement final ne dit rien de la vitesse ; seul le temps mis pour l'atteindre en dit quelque chose.
:::

::: verifie À toi : même durée, avancements différents
Deux comprimés effervescents A et B sont plongés au même instant dans deux verres identiques. Après 30 s, A a dégagé 2,4·10⁻⁴ mol de CO₂ et B 3,6·10⁻⁴ mol (le coefficient de CO₂ vaut 1 dans l'équation). Quelle transformation est la plus rapide ?

---

Le coefficient de CO₂ vaut 1, donc x = n(CO₂) : Δx_A = 2,4·10⁻⁴ mol et Δx_B = 3,6·10⁻⁴ mol. La durée est la même (30 s), donc on compare Δx : B a progressé davantage, B est la transformation la plus rapide.
:::

::: retenir
On compare la rapidité à avancement égal (la plus courte durée gagne) ou à durée égale (le plus grand Δx gagne) ; sinon on calcule Δx/Δt.
:::

## 📊 L'avancement x et le tableau descriptif au fil du temps

On mélange 20,0 mL d'eau oxygénée à 5,0·10⁻² mol·L⁻¹, 30,0 mL d'iodure de potassium à 0,20 mol·L⁻¹ et 10,0 mL d'acide sulfurique en excès : le volume est V = 60,0 mL = 6,0·10⁻² L. On ne peut pas peser le diiode seconde après seconde, mais on peut le doser à un instant donné.
Comment passer d'une seule mesure, n(I₂), à la quantité de chaque espèce à cet instant ?

::: definition
**Avancement volumique** — Si les espèces forment une seule phase de volume V constant, l'avancement volumique est y = x/V, en mol·L⁻¹. Il relie l'avancement x (en mol, qui compte la progression de la réaction) aux concentrations.
:::

Le tableau descriptif de H₂O₂ + 2 I⁻ + 2 H₃O⁺ → I₂ + 4 H₂O s'écrit, en quantités de matière :

|                     | H₂O₂         | 2 I⁻          | 2 H₃O⁺ | I₂  | 4 H₂O   |
| ------------------- | ------------ | ------------- | ------ | --- | ------- |
| état initial (mol)  | 1,0·10⁻³     | 6,0·10⁻³      | excès  | 0   | solvant |
| à l'instant t (mol) | 1,0·10⁻³ − x | 6,0·10⁻³ − 2x | excès  | x   | solvant |

La ligne « à l'instant t » ne contient que la lettre x : connaître x, c'est connaître tout le système, et chaque coefficient de l'équation multiplie x.

::: exemple Reconstituer le système à partir de n(I₂)

1. Quantités initiales : n(H₂O₂) = 5,0·10⁻² × 20,0·10⁻³ = 1,0·10⁻³ mol et n(I⁻) = 0,20 × 30,0·10⁻³ = 6,0·10⁻³ mol, car n = C·V.
2. À t = 6,0 min, le dosage donne n(I₂) = 4,5·10⁻⁴ mol. Le coefficient de I₂ vaut 1 et il n'y en avait pas au départ, donc x = 4,5·10⁻⁴ mol.
3. n(H₂O₂) = 1,0·10⁻³ − x = 5,5·10⁻⁴ mol (coefficient 1) et n(I⁻) = 6,0·10⁻³ − 2x = 5,1·10⁻³ mol (coefficient 2).
4. y = x/V = 4,5·10⁻⁴ / 6,0·10⁻² = 7,5·10⁻³ mol·L⁻¹ et [H₂O₂] = 5,5·10⁻⁴ / 6,0·10⁻² ≈ 9,2·10⁻³ mol·L⁻¹.
5. Contrôle : [H₂O₂] initiale = 1,0·10⁻³ / 6,0·10⁻² ≈ 1,7·10⁻² mol·L⁻¹, et 1,7·10⁻² − 7,5·10⁻³ ≈ 9,2·10⁻³ mol·L⁻¹ ✓.

:::

::: piege
**Erreur : oublier le coefficient stœchiométrique.** Écrire n(I⁻) = 6,0·10⁻³ − x = 5,55·10⁻³ mol donne un résultat faux : le bon calcul est 6,0·10⁻³ − 2x = 5,1·10⁻³ mol. L'erreur tente parce que la ligne de H₂O₂ se lit « − x » et qu'on recopie le même geste. Chaque espèce porte son propre coefficient devant x.
:::

::: propriete
**Quantités et avancement** — Pour a A + b B → c C + d D, avec C et D absents au départ : n(A) = nᵢ(A) − a·x, n(B) = nᵢ(B) − b·x, n(C) = c·x, n(D) = d·x. On en déduit x = (nᵢ(A) − n(A))/a = n(C)/c. À volume constant, [A] = [A]ᵢ − a·y et [C] = c·y.
Cas limite : l'avancement maximal est celui du réactif limitant. Ici H₂O₂ s'épuise pour x = 1,0·10⁻³ mol, alors que I⁻ permettrait 6,0·10⁻³/2 = 3,0·10⁻³ mol : x_max = 1,0·10⁻³ mol. Une espèce en excès ou le solvant n'est pas suivie.
:::

::: verifie À toi : même méthode, autres quantités
Un mélange contient nᵢ(H₂O₂) = 2,4·10⁻³ mol et nᵢ(I⁻) = 1,0·10⁻² mol (acide en excès). À l'instant t, n(I₂) = 7,0·10⁻⁴ mol. Que valent n(H₂O₂) et n(I⁻) ?

---

Le coefficient de I₂ vaut 1 : x = 7,0·10⁻⁴ mol. H₂O₂ a pour coefficient 1 : n(H₂O₂) = 2,4·10⁻³ − 7,0·10⁻⁴ = 1,7·10⁻³ mol. I⁻ a pour coefficient 2 : n(I⁻) = 1,0·10⁻² − 2 × 7,0·10⁻⁴ = 8,6·10⁻³ mol.
:::

::: retenir
Chaque quantité vaut sa valeur initiale ± (coefficient × x), et l'avancement volumique y = x/V donne les concentrations ; x_max est celui du réactif limitant.
:::

## ⏳ La vitesse moyenne d'une réaction

On refait l'expérience avec 8,0·10⁻³ mol d'eau oxygénée (réactif limitant) dans V = 100 mL, et on relève l'avancement x = n(I₂) :

| t (min)  | 0   | 5   | 10  | 20  | 30  | 40  |
| -------- | --- | --- | --- | --- | --- | --- |
| x (mmol) | 0   | 2,3 | 4,0 | 6,0 | 7,0 | 7,5 |

Entre 0 et 10 min, x gagne 4,0 mmol ; entre 20 et 30 min, il n'en gagne que 1,0 pour la même durée.
Comment exprimer cette différence par un nombre ?

::: definition
**Vitesse moyenne** — Entre deux instants t₁ et t₂, la vitesse moyenne de la réaction est v_moy(t₁ ; t₂) = (x(t₂) − x(t₁)) / (t₂ − t₁) = Δx/Δt. Elle est positive et s'exprime en mol·s⁻¹ dans le système international (mol·min⁻¹ en usage courant).
Pour une seule phase de volume V constant, la vitesse volumique moyenne est v_volmoy(t₁ ; t₂) = v_moy(t₁ ; t₂)/V, en mol·L⁻¹·s⁻¹ ou mol·L⁻¹·min⁻¹.
:::

::: figure La sécante (M₁M₂) relie deux points de la courbe : sa pente Δx/Δt est la vitesse moyenne entre t₁ = 10 min et t₂ = 30 min
<svg viewBox="0 0 340 236"><title>Courbe x(t) et sécante (M₁M₂)</title><line x1="54.0" y1="26" x2="54.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="114.4" y1="26" x2="114.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="174.9" y1="26" x2="174.9" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="295.8" y1="26" x2="295.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190.0" x2="326" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="153.6" x2="326" y2="153.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="117.1" x2="326" y2="117.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="80.7" x2="326" y2="80.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="44.2" x2="326" y2="44.2" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="114.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="174.9" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="295.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="157.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="121.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="84.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="48.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><polyline points="54.0,190.0 57.0,185.0 60.0,180.2 63.1,175.6 66.1,171.1 69.1,166.8 72.1,162.6 75.2,158.6 78.2,154.7 81.2,150.9 84.2,147.3 87.2,143.8 90.3,140.4 93.3,137.1 96.3,134.0 99.3,130.9 102.4,127.9 105.4,125.1 108.4,122.3 111.4,119.7 114.4,117.1 117.5,114.6 120.5,112.2 123.5,109.9 126.5,107.7 129.6,105.5 132.6,103.4 135.6,101.4 138.6,99.5 141.6,97.6 144.7,95.8 147.7,94.0 150.7,92.3 153.7,90.7 156.8,89.1 159.8,87.6 162.8,86.1 165.8,84.7 168.8,83.3 171.9,82.0 174.9,80.7 177.9,79.4 180.9,78.2 184.0,77.1 187.0,75.9 190.0,74.9 193.0,73.8 196.0,72.8 199.1,71.8 202.1,70.9 205.1,70.0 208.1,69.1 211.2,68.3 214.2,67.4 217.2,66.7 220.2,65.9 223.2,65.2 226.3,64.4 229.3,63.8 232.3,63.1 235.3,62.4 238.4,61.8 241.4,61.2 244.4,60.6 247.4,60.1 250.4,59.5 253.5,59.0 256.5,58.5 259.5,58.0 262.5,57.6 265.6,57.1 268.6,56.7 271.6,56.2 274.6,55.8 277.6,55.4 280.7,55.1 283.7,54.7 286.7,54.3 289.7,54.0 292.8,53.7 295.8,53.3 298.8,53.0 301.8,52.7 304.8,52.4 307.9,52.2 310.9,51.9 313.9,51.6 316.9,51.4 320.0,51.1 323.0,50.9 326.0,50.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="72.1" y1="136.2" x2="283.7" y2="40.6" stroke="#c2410c" stroke-width="1.8"/><line x1="114.4" y1="117.1" x2="235.3" y2="117.1" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="235.3" y1="117.1" x2="235.3" y2="62.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="114.4" cy="117.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="235.3" cy="62.4" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><text x="102.4" y="109.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M₁</text><text x="221.3" y="54.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M₂</text><text x="174.9" y="133.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Δt = 20 min</text><text x="241.3" y="89.8" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Δx = 3,0 mmol</text></svg>
:::

Sur la figure, la sécante (M₁M₂) relie M₁(10 ; 4,0) et M₂(30 ; 7,0) : Δt = 20 min, Δx = 3,0 mmol, donc v_moy(10 ; 30) = 3,0/20 = 0,15 mmol·min⁻¹, qui est exactement la pente de cette sécante.

::: exemple Deux intervalles de même durée

1. On lit dans le tableau x(0) = 0, x(10) = 4,0 mmol, x(20) = 6,0 mmol et x(30) = 7,0 mmol.
2. v_moy(0 ; 10) = (4,0 − 0)/(10 − 0) = 0,40 mmol·min⁻¹ = 4,0·10⁻⁴ mol·min⁻¹, car on divise l'avancement gagné par la durée.
3. v_moy(20 ; 30) = (7,0 − 6,0)/(30 − 20) = 0,10 mmol·min⁻¹ : quatre fois moins pour la même durée, la réaction ralentit.
4. v_volmoy(0 ; 10) = v_moy/V = 4,0·10⁻⁴ / 0,100 = 4,0·10⁻³ mol·L⁻¹·min⁻¹, car la vitesse volumique se rapporte à 1 L de mélange.
5. En unité SI : 4,0·10⁻⁴ mol·min⁻¹ ÷ 60 s·min⁻¹ ≈ 6,7·10⁻⁶ mol·s⁻¹.

:::

::: piege
**Erreur : diviser x(t₂) par t₂.** Sur [10 ; 30], x(30)/30 = 7,0/30 ≈ 0,23 mmol·min⁻¹ au lieu des 0,15 trouvés avec Δx/Δt. L'erreur tente parce que x(t₂) « est la valeur au bout », mais elle contient l'avancement gagné avant t₁, qui n'appartient pas à l'intervalle. Il faut retrancher x(t₁) et diviser par la durée t₂ − t₁.
:::

::: propriete
**Vitesse moyenne et sécante** — v_moy(t₁ ; t₂) est le coefficient directeur de la sécante à la courbe x(t) aux points d'abscisses t₁ et t₂. Pour lire une pente avec précision, on prend deux points éloignés de cette droite. La valeur dépend de l'intervalle choisi : ici 0,40, 0,20, 0,10 mmol·min⁻¹ sur trois intervalles consécutifs de 10 min.
Cas limite : l'intervalle [0 ; t₁/₂], où t₁/₂ est le temps de demi-réaction (x = x_f/2, avec x_f = x_max pour une transformation totale ; ici 10 min), donne v_moy(0 ; t₁/₂) = x_max/(2·t₁/₂) = 8,0/20 = 0,40 mmol·min⁻¹.
:::

::: verifie À toi : un autre intervalle
Avec le même tableau, calculer v_moy(20 ; 40) en mmol·min⁻¹, puis v_volmoy(20 ; 40) en mol·L⁻¹·min⁻¹ (V = 0,100 L).

---

v_moy(20 ; 40) = (7,5 − 6,0)/(40 − 20) = 1,5/20 = 0,075 mmol·min⁻¹ = 7,5·10⁻⁵ mol·min⁻¹. On divise par V : v_volmoy = 7,5·10⁻⁵ / 0,100 = 7,5·10⁻⁴ mol·L⁻¹·min⁻¹.
:::

::: retenir
v_moy(t₁ ; t₂) = Δx/Δt est la pente de la sécante, en mol·s⁻¹ ; divisée par V, elle donne la vitesse volumique moyenne en mol·L⁻¹·s⁻¹.
:::

## 🎯 La vitesse instantanée : la tangente

Reprenons le suivi précédent à t₁ = 10 min, et resserrons l'intervalle vers la droite :

| t₂ (min)                    | 30   | 20   | 14   | 11   |
| --------------------------- | ---- | ---- | ---- | ---- |
| v_moy(10 ; t₂) (mmol·min⁻¹) | 0,15 | 0,20 | 0,24 | 0,27 |

Les valeurs se stabilisent près de 0,28 quand t₂ se rapproche de 10 min.
Que vaut la vitesse à un instant précis, et comment la lire sur la courbe ?

::: definition
**Vitesse instantanée** — La vitesse instantanée à l'instant t₁ est la limite de la vitesse moyenne quand t₂ tend vers t₁ : v(t₁) = lim v_moy(t₁ ; t₂) = dx/dt à l'instant t₁. À un instant t quelconque, v(t) = dx/dt, positive, en mol·s⁻¹.
Pour une seule phase de volume V constant, la vitesse volumique instantanée est v_vol(t) = (1/V)·dx/dt = dy/dt.
:::

::: figure La tangente (T) en M touche la courbe : sa pente, lue avec les points A et B, est la vitesse instantanée à t = 10 min
<svg viewBox="0 0 340 236"><title>Courbe x(t) et tangente (T) au point M d'abscisse 10 min</title><line x1="54.0" y1="26" x2="54.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="114.4" y1="26" x2="114.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="174.9" y1="26" x2="174.9" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="295.8" y1="26" x2="295.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190.0" x2="326" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="153.6" x2="326" y2="153.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="117.1" x2="326" y2="117.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="80.7" x2="326" y2="80.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="44.2" x2="326" y2="44.2" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="114.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="174.9" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="295.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="157.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="121.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="84.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="48.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><polyline points="54.0,190.0 57.0,185.0 60.0,180.2 63.1,175.6 66.1,171.1 69.1,166.8 72.1,162.6 75.2,158.6 78.2,154.7 81.2,150.9 84.2,147.3 87.2,143.8 90.3,140.4 93.3,137.1 96.3,134.0 99.3,130.9 102.4,127.9 105.4,125.1 108.4,122.3 111.4,119.7 114.4,117.1 117.5,114.6 120.5,112.2 123.5,109.9 126.5,107.7 129.6,105.5 132.6,103.4 135.6,101.4 138.6,99.5 141.6,97.6 144.7,95.8 147.7,94.0 150.7,92.3 153.7,90.7 156.8,89.1 159.8,87.6 162.8,86.1 165.8,84.7 168.8,83.3 171.9,82.0 174.9,80.7 177.9,79.4 180.9,78.2 184.0,77.1 187.0,75.9 190.0,74.9 193.0,73.8 196.0,72.8 199.1,71.8 202.1,70.9 205.1,70.0 208.1,69.1 211.2,68.3 214.2,67.4 217.2,66.7 220.2,65.9 223.2,65.2 226.3,64.4 229.3,63.8 232.3,63.1 235.3,62.4 238.4,61.8 241.4,61.2 244.4,60.6 247.4,60.1 250.4,59.5 253.5,59.0 256.5,58.5 259.5,58.0 262.5,57.6 265.6,57.1 268.6,56.7 271.6,56.2 274.6,55.8 277.6,55.4 280.7,55.1 283.7,54.7 286.7,54.3 289.7,54.0 292.8,53.7 295.8,53.3 298.8,53.0 301.8,52.7 304.8,52.4 307.9,52.2 310.9,51.9 313.9,51.6 316.9,51.4 320.0,51.1 323.0,50.9 326.0,50.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="54.0" y1="168.1" x2="187.0" y2="55.9" stroke="#c2410c" stroke-width="2"/><line x1="54.0" y1="168.1" x2="174.9" y2="168.1" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="174.9" y1="168.1" x2="174.9" y2="66.1" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="54.0" cy="168.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="174.9" cy="66.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="114.4" cy="117.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="174.9" cy="168.1" r="2.8" fill="#94a3b8" stroke="#ffffff" stroke-width="1"/><text x="65.0" y="182.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="164.9" y="58.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="184.9" y="182.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="124.4" y="131.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="193.0" y="53.9" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(T)</text></svg>
:::

Sur la figure, la sécante tend vers la tangente (T) à la courbe en M quand t₂ tend vers t₁ : la vitesse à l'instant de M est la pente de (T), calculée avec les deux points A et B pris sur la tangente.

::: exemple Lire v(10 min) sur la tangente

1. On trace la tangente (T) en M(10 ; 4,0). Elle passe par A(0 ; 1,2) et B(20 ; 6,8), deux points éloignés pour une lecture précise.
2. v(10) = (x_B − x_A)/(t_B − t_A) = (6,8 − 1,2)/(20 − 0) = 0,28 mmol·min⁻¹ = 2,8·10⁻⁴ mol·min⁻¹, car la vitesse est le coefficient directeur de la tangente.
3. v_vol(10) = 2,8·10⁻⁴ / 0,100 = 2,8·10⁻³ mol·L⁻¹·min⁻¹, en divisant par V.
4. En unité SI : 2,8·10⁻⁴ / 60 ≈ 4,7·10⁻⁶ mol·s⁻¹.
5. Contrôle : 0,28 est compris entre v_moy(0 ; 10) = 0,40 et v_moy(10 ; 30) = 0,15, comme la courbe qui se redresse puis s'aplatit.

:::

::: piege
**Erreur : prendre des points de la courbe au lieu de points de la tangente.** Avec l'origine O et M(10 ; 4,0), on calcule 4,0/10 = 0,40 mmol·min⁻¹ : c'est la vitesse moyenne sur [0 ; 10], pas la vitesse à t = 10 min (0,28). L'erreur tente parce que M et O sont faciles à lire ; mais la droite (OM) est une sécante, et seule la tangente donne la vitesse instantanée.
:::

::: propriete
**Vitesse et tangente** — v(t₁) est le coefficient directeur de la tangente à la courbe x(t) au point d'abscisse t₁, calculé sur deux points A et B de la tangente. Pour la tracer, on peut procéder « au jugé » ou par la méthode de la corde : on place N et P d'abscisses t₁ − Δt et t₁ + Δt (Δt petit), puis on mène par M la parallèle à (NP). La tangente est difficile à tracer exactement : la valeur lue est peu précise.
Cas limite : la tangente à l'origine donne la vitesse initiale v(0).
:::

::: verifie À toi : la vitesse à un autre instant
Sur la même courbe, la tangente en t = 20 min passe par A(0 ; 3,2) et B(40 ; 8,8) (valeurs lues, en mmol). Calculer v(20) en mmol·min⁻¹, puis v_vol(20) en mol·L⁻¹·min⁻¹ (V = 0,100 L).

---

v(20) = (8,8 − 3,2)/(40 − 0) = 5,6/40 = 0,14 mmol·min⁻¹ = 1,4·10⁻⁴ mol·min⁻¹, pente de la tangente. Puis v_vol(20) = 1,4·10⁻⁴ / 0,100 = 1,4·10⁻³ mol·L⁻¹·min⁻¹. C'est la moitié de v(10) = 0,28 : la vitesse a diminué.
:::

::: retenir
v(t₁) = dx/dt est la pente de la tangente en t₁ (limite de v_moy), en mol·s⁻¹ ; v_vol = v/V = dy/dt.
:::

## ⚖️ Vitesse et concentrations

Dans la réaction S₂O₈²⁻ + 2 I⁻ → I₂ + 2 SO₄²⁻, menée dans V = 50,0 mL constant, on suit [I₂] au cours du temps : à t = 15 min, la tangente à la courbe [I₂](t) a pour pente 6,0·10⁻³ mol·L⁻¹·min⁻¹.
Que valent les pentes des courbes des trois autres espèces, et la vitesse volumique ?

::: definition
**Vitesse volumique et concentrations** — Pour a A + b B → c C + d D, en une seule phase de volume V constant : v_vol(t) = (1/V)·v(t) = −(1/a)·d[A]/dt = −(1/b)·d[B]/dt = (1/c)·d[C]/dt = (1/d)·d[D]/dt.
:::

| espèce                       | S₂O₈²⁻  | I⁻        | I₂       | SO₄²⁻     |
| ---------------------------- | ------- | --------- | -------- | --------- |
| coefficient                  | 1       | 2         | 1        | 2         |
| concentration                | diminue | diminue   | augmente | augmente  |
| d[ ]/dt en fonction de v_vol | − v_vol | − 2 v_vol | + v_vol  | + 2 v_vol |

Le signe dit le sens (réactif qui disparaît, produit qui apparaît) et le coefficient dit le rythme.

::: exemple Passer de [I₂](t) aux autres espèces

1. Avec y = x/V, le tableau en concentrations donne [S₂O₈²⁻] = C₁ − y, [I⁻] = C₂ − 2y, [I₂] = y et [SO₄²⁻] = 2y, où C₁ et C₂ sont les concentrations initiales.
2. On dérive : C₁ et C₂ sont constantes (dérivée nulle), donc d[S₂O₈²⁻]/dt = − dy/dt, d[I⁻]/dt = − 2 dy/dt, d[I₂]/dt = dy/dt et d[SO₄²⁻]/dt = 2 dy/dt.
3. Comme [I₂] = y, v_vol(15 min) = d[I₂]/dt = 6,0·10⁻³ mol·L⁻¹·min⁻¹.
4. On en déduit d[S₂O₈²⁻]/dt = − 6,0·10⁻³, d[I⁻]/dt = − 1,2·10⁻² et d[SO₄²⁻]/dt = + 1,2·10⁻² mol·L⁻¹·min⁻¹.
5. v = V·v_vol = 5,0·10⁻² × 6,0·10⁻³ = 3,0·10⁻⁴ mol·min⁻¹. En unité SI de volume : 6,0·10⁻³ mol·L⁻¹·min⁻¹ = 6,0 mol·m⁻³·min⁻¹ = 0,10 mol·m⁻³·s⁻¹ (1 mol·L⁻¹ = 10³ mol·m⁻³, puis ÷ 60).

:::

::: piege
**Erreur : écrire v_vol = − d[I⁻]/dt.** On obtiendrait 1,2·10⁻² mol·L⁻¹·min⁻¹, deux fois trop : la bonne relation est v_vol = − (1/2)·d[I⁻]/dt = 6,0·10⁻³. L'erreur tente parce que I⁻ est un réactif comme S₂O₈²⁻ ; mais il en disparaît 2 mol quand la réaction avance de 1 mol, et le facteur 1/b rétablit la vitesse de la réaction.
:::

::: propriete
**Signe et indépendance du volume** — La concentration d'un réactif diminue (sa dérivée est négative) et celle d'un produit augmente (dérivée positive) : le signe moins devant les réactifs rend v_vol positive. La vitesse volumique ne dépend pas du volume : deux prélèvements de 50 mL et de 100 mL du même mélange ont à tout instant les mêmes concentrations, donc la même v_vol, alors que v = V·v_vol est deux fois plus grande pour 100 mL.
Cas limite : pour une espèce de coefficient 1 présente seulement après le départ, comme I₂ ici, d[I₂]/dt est directement v_vol.
:::

::: verifie À toi : une autre équation
Dans l'enceinte rigide d'une réaction gazeuse 4 NH₃ + 5 O₂ → 4 NO + 6 H₂O, on mesure à un instant d[NO]/dt = 1,2·10⁻³ mol·L⁻¹·s⁻¹. Calculer v_vol, puis d[O₂]/dt.

---

Le coefficient de NO vaut 4 : v_vol = (1/4)·d[NO]/dt = 3,0·10⁻⁴ mol·L⁻¹·s⁻¹. O₂ est un réactif de coefficient 5 : d[O₂]/dt = − 5·v_vol = − 1,5·10⁻³ mol·L⁻¹·s⁻¹, négative car O₂ disparaît.
:::

::: retenir
v_vol = − (1/a)·d[A]/dt pour un réactif et (1/c)·d[C]/dt pour un produit : on divise la pente par le coefficient, et v_vol est indépendante de V.
:::

## 🎈 Suivre une réaction par le volume d'un gaz

On place 0,12 g de ruban de magnésium dans V = 50,0 mL d'acide chlorhydrique à 0,50 mol·L⁻¹ ; le dihydrogène est recueilli dans une éprouvette graduée, et on lit le volume V(H₂) au cours du temps (volume molaire V_m = 24 L·mol⁻¹ dans les conditions de l'expérience) :

| t (s)      | 0   | 10  | 20  | 40  | 60  | 80  |
| ---------- | --- | --- | --- | --- | --- | --- |
| V(H₂) (mL) | 0   | 35  | 60  | 90  | 105 | 112 |

Le volume d'un gaz peut-il tenir lieu d'avancement, et comment en tirer la vitesse volumique ?

::: definition
**Avancement et volume de gaz** — Si le gaz G a pour coefficient 1 et n'existe pas au départ, x = n(G) = V(G)/V_m. La vitesse volumique s'écrit alors v_vol(t) = (1/V)·dx/dt = (1/(V·V_m))·dV(G)/dt, où V est le volume du mélange réactionnel (la solution) et non celui du gaz.
:::

::: figure La tangente en M à la courbe V(H₂)(t) : sa pente, lue avec les points A et B, vaut dV(H₂)/dt à t = 20 s
<svg viewBox="0 0 340 236"><title>Courbe V(H₂)(t) et tangente au point M d'abscisse 20 s</title><line x1="54.0" y1="26" x2="54.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="108.4" y1="26" x2="108.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="162.8" y1="26" x2="162.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="217.2" y1="26" x2="217.2" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="271.6" y1="26" x2="271.6" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190.0" x2="326" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="164.8" x2="326" y2="164.8" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="139.5" x2="326" y2="139.5" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="114.3" x2="326" y2="114.3" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="89.1" x2="326" y2="89.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="63.8" x2="326" y2="63.8" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="38.6" x2="326" y2="38.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="108.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="162.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="217.2" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="271.6" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="168.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="48.0" y="143.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="48.0" y="118.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="48.0" y="93.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><text x="48.0" y="67.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><text x="48.0" y="42.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V(H₂) (mL)</text><polyline points="54.0,190.0 57.0,184.3 60.0,178.8 63.1,173.5 66.1,168.4 69.1,163.5 72.1,158.8 75.2,154.2 78.2,149.9 81.2,145.7 84.2,141.6 87.2,137.7 90.3,134.0 93.3,130.4 96.3,126.9 99.3,123.6 102.4,120.4 105.4,117.3 108.4,114.3 111.4,111.4 114.4,108.7 117.5,106.0 120.5,103.5 123.5,101.1 126.5,98.7 129.6,96.4 132.6,94.2 135.6,92.1 138.6,90.1 141.6,88.2 144.7,86.3 147.7,84.5 150.7,82.8 153.7,81.1 156.8,79.5 159.8,77.9 162.8,76.5 165.8,75.0 168.8,73.7 171.9,72.3 174.9,71.1 177.9,69.8 180.9,68.7 184.0,67.5 187.0,66.4 190.0,65.4 193.0,64.4 196.0,63.4 199.1,62.5 202.1,61.6 205.1,60.7 208.1,59.9 211.2,59.1 214.2,58.3 217.2,57.5 220.2,56.8 223.2,56.1 226.3,55.5 229.3,54.8 232.3,54.2 235.3,53.6 238.4,53.1 241.4,52.5 244.4,52.0 247.4,51.5 250.4,51.0 253.5,50.5 256.5,50.1 259.5,49.7 262.5,49.2 265.6,48.8 268.6,48.4 271.6,48.1 274.6,47.7 277.6,47.4 280.7,47.0 283.7,46.7 286.7,46.4 289.7,46.1 292.8,45.8 295.8,45.6 298.8,45.3 301.8,45.1 304.8,44.8 307.9,44.6 310.9,44.4 313.9,44.1 316.9,43.9 320.0,43.7 323.0,43.5 326.0,43.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="54.0" y1="167.3" x2="184.6" y2="40.1" stroke="#c2410c" stroke-width="2"/><line x1="54.0" y1="167.3" x2="162.8" y2="167.3" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="162.8" y1="167.3" x2="162.8" y2="61.3" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="54.0" cy="167.3" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="162.8" cy="61.3" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="108.4" cy="114.3" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="162.8" cy="167.3" r="2.8" fill="#94a3b8" stroke="#ffffff" stroke-width="1"/><text x="66.0" y="181.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="152.8" y="53.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="172.8" y="181.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="120.4" y="128.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="190.6" y="44.1" text-anchor="start" font-size="11" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text></svg>
:::

Sur la figure, la pente de la tangente en M est dV(H₂)/dt, en mL·s⁻¹ ; il reste à diviser par V_m et par V, en litres.

::: exemple De la tangente à la vitesse volumique

1. Équation : Mg + 2 H₃O⁺ → Mg²⁺ + H₂(g) + 2 H₂O. n(Mg) = 0,12/24 = 5,0·10⁻³ mol (M = 24 g·mol⁻¹) et n(H₃O⁺) = 0,50 × 0,0500 = 2,5·10⁻² mol, supérieur aux 2 × 5,0·10⁻³ mol nécessaires : Mg est limitant, x_max = 5,0·10⁻³ mol, soit V_max(H₂) = 5,0·10⁻³ × 24 = 0,12 L = 120 mL, valeur vers laquelle tendent les mesures du tableau.
2. À t = 20 s, V(H₂) = 60 mL donc x = 60·10⁻³/24 = 2,5·10⁻³ mol, la moitié de x_max.
3. La tangente en M(20 ; 60) passe par A(0 ; 18) et B(40 ; 102) : dV/dt = (102 − 18)/(40 − 0) = 2,1 mL·s⁻¹ = 2,1·10⁻³ L·s⁻¹.
4. v = dx/dt = (1/V_m)·dV/dt = 2,1·10⁻³ / 24 = 8,75·10⁻⁵ ≈ 8,8·10⁻⁵ mol·s⁻¹.
5. v_vol = v/V = 8,75·10⁻⁵ / 0,0500 = 1,75·10⁻³ ≈ 1,8·10⁻³ mol·L⁻¹·s⁻¹.

:::

::: piege
**Erreur : garder les millilitres.** Avec dV/dt = 2,1 mL·s⁻¹ non converti, on calcule 2,1/(24 × 0,0500) = 1,75 mol·L⁻¹·s⁻¹, mille fois trop grand. L'erreur tente parce que la pente se lit en mL·s⁻¹ sur la figure ; mais V_m est en L·mol⁻¹ et V en litres : on convertit le volume de gaz en litres avant de diviser.
:::

::: propriete
**Suivi par un gaz** — Si l'équation produit c moles de gaz G par unité d'avancement, x = V(G)/(c·V_m) ; avec c = 1, x = V(G)/V_m. Alors v_vol = (1/(V·V_m))·dV(G)/dt, la pente de la tangente étant en L·s⁻¹ et V en L.
Cas limite : à t = 0, V(G) = 0 donc x = 0, mais la tangente à l'origine donne la vitesse initiale, non nulle. V_m dépend de la température et de la pression : l'énoncé la donne.
:::

::: verifie À toi : même chaîne, autre gaz
CaCO₃(s) + 2 H₃O⁺ → Ca²⁺ + CO₂(g) + 3 H₂O dans V = 50,0 mL. À l'instant t₁, la tangente à la courbe V(CO₂) = f(t) a pour pente 1,2 mL·s⁻¹ (V_m = 24 L·mol⁻¹). Calculer v_vol(t₁).

---

Le coefficient de CO₂ vaut 1 : dx/dt = (1/V_m)·dV/dt = 1,2·10⁻³ L·s⁻¹ / 24 L·mol⁻¹ = 5,0·10⁻⁵ mol·s⁻¹ (on a converti mL en L). Puis v_vol = (dx/dt)/V = 5,0·10⁻⁵ / 0,0500 = 1,0·10⁻³ mol·L⁻¹·s⁻¹.
:::

::: retenir
Pour un gaz de coefficient 1 : x = V(G)/V_m et v_vol = (1/(V·V_m))·dV(G)/dt, en litres, avec V le volume de la solution.
:::

## 📉 Comment la vitesse évolue au cours du temps

Reprenons le suivi du début (x_max = 8,0 mmol) et calculons la vitesse moyenne sur des intervalles consécutifs de 10 min :

| intervalle (min)   | [0 ; 10] | [10 ; 20] | [20 ; 30] | [30 ; 40] |
| ------------------ | -------- | --------- | --------- | --------- |
| v_moy (mmol·min⁻¹) | 0,40     | 0,20      | 0,10      | 0,05      |

La vitesse est-elle constante ? Où est-elle maximale ? Et y a-t-il un instant où la vitesse instantanée vaut la vitesse moyenne d'un intervalle donné ?

::: figure Trois tangentes de plus en plus plates (pentes en mmol·min⁻¹) : la vitesse diminue au cours du temps
<svg viewBox="0 0 340 236"><title>Courbe x(t) avec trois tangentes en t = 0, t = 10 min et t = 30 min</title><line x1="54.0" y1="26" x2="54.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="114.4" y1="26" x2="114.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="174.9" y1="26" x2="174.9" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="295.8" y1="26" x2="295.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190.0" x2="326" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="153.6" x2="326" y2="153.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="117.1" x2="326" y2="117.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="80.7" x2="326" y2="80.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="44.2" x2="326" y2="44.2" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="114.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="174.9" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="295.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="157.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="121.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="84.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="48.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><polyline points="54.0,190.0 57.0,185.0 60.0,180.2 63.1,175.6 66.1,171.1 69.1,166.8 72.1,162.6 75.2,158.6 78.2,154.7 81.2,150.9 84.2,147.3 87.2,143.8 90.3,140.4 93.3,137.1 96.3,134.0 99.3,130.9 102.4,127.9 105.4,125.1 108.4,122.3 111.4,119.7 114.4,117.1 117.5,114.6 120.5,112.2 123.5,109.9 126.5,107.7 129.6,105.5 132.6,103.4 135.6,101.4 138.6,99.5 141.6,97.6 144.7,95.8 147.7,94.0 150.7,92.3 153.7,90.7 156.8,89.1 159.8,87.6 162.8,86.1 165.8,84.7 168.8,83.3 171.9,82.0 174.9,80.7 177.9,79.4 180.9,78.2 184.0,77.1 187.0,75.9 190.0,74.9 193.0,73.8 196.0,72.8 199.1,71.8 202.1,70.9 205.1,70.0 208.1,69.1 211.2,68.3 214.2,67.4 217.2,66.7 220.2,65.9 223.2,65.2 226.3,64.4 229.3,63.8 232.3,63.1 235.3,62.4 238.4,61.8 241.4,61.2 244.4,60.6 247.4,60.1 250.4,59.5 253.5,59.0 256.5,58.5 259.5,58.0 262.5,57.6 265.6,57.1 268.6,56.7 271.6,56.2 274.6,55.8 277.6,55.4 280.7,55.1 283.7,54.7 286.7,54.3 289.7,54.0 292.8,53.7 295.8,53.3 298.8,53.0 301.8,52.7 304.8,52.4 307.9,52.2 310.9,51.9 313.9,51.6 316.9,51.4 320.0,51.1 323.0,50.9 326.0,50.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="54.0" y1="190.0" x2="126.5" y2="69.7" stroke="#c2410c" stroke-width="2"/><line x1="66.1" y1="157.9" x2="162.8" y2="76.3" stroke="#c2410c" stroke-width="2"/><line x1="174.9" y1="75.2" x2="295.8" y2="49.7" stroke="#c2410c" stroke-width="2"/><circle cx="54.0" cy="190.0" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="114.4" cy="117.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="235.3" cy="62.4" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><text x="111.4" y="73.4" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,55</text><text x="146" y="84" text-anchor="end" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,28</text><text x="235.3" y="43.7" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,07</text></svg>
:::

Sur la figure, les trois tangentes sont tracées en t = 0, t = 10 min et t = 30 min, avec leurs pentes en mmol·min⁻¹ : elles s'aplatissent de plus en plus, et la courbe se rapproche du palier x_max.

::: exemple Lire l'évolution de v

1. Tangente en t = 0 : elle passe par O(0 ; 0) et (10 ; 5,5), donc v(0) = 5,5/10 = 0,55 mmol·min⁻¹. En t = 10 min, la tangente de la notion précédente donne 0,28. En t = 30 min, elle passe par (20 ; 6,3) et (40 ; 7,7), donc v(30) = 1,4/20 = 0,07 mmol·min⁻¹.
2. 0,55 > 0,28 > 0,07 : la vitesse diminue au cours du temps et son maximum est atteint à t = 0, là où la tangente est la plus raide.
3. Vers le palier x_max = 8,0 mmol, la tangente devient horizontale : sa pente tend vers 0, donc v tend vers 0 quand la transformation s'achève.

:::

::: piege
**Erreur : croire que v(0) = 0 parce que x(0) = 0.** Écrire « x(0) = 0 donc v(0) = 0 » confond la valeur de x avec sa pente. La tangente à l'origine passe par O et (10 ; 5,5) : v(0) = 0,55 mmol·min⁻¹, la valeur maximale. L'erreur tente parce que la courbe démarre de zéro ; mais la vitesse est la pente de x(t), pas sa hauteur.
:::

::: figure La tangente en P est parallèle à la sécante entre t = 0 et t = 30 min : en t* la vitesse instantanée égale la vitesse moyenne
<svg viewBox="0 0 340 236"><title>Sécante entre t = 0 et t = 30 min et tangente parallèle au point P d'abscisse t*</title><line x1="54.0" y1="26" x2="54.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="114.4" y1="26" x2="114.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26" x2="144.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="174.9" y1="26" x2="174.9" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="295.8" y1="26" x2="295.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190.0" x2="326" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="153.6" x2="326" y2="153.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="117.1" x2="326" y2="117.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="80.7" x2="326" y2="80.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="44.2" x2="326" y2="44.2" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="114.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text><text x="174.9" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="295.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="157.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="121.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="84.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="48.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><polyline points="54.0,190.0 57.0,185.0 60.0,180.2 63.1,175.6 66.1,171.1 69.1,166.8 72.1,162.6 75.2,158.6 78.2,154.7 81.2,150.9 84.2,147.3 87.2,143.8 90.3,140.4 93.3,137.1 96.3,134.0 99.3,130.9 102.4,127.9 105.4,125.1 108.4,122.3 111.4,119.7 114.4,117.1 117.5,114.6 120.5,112.2 123.5,109.9 126.5,107.7 129.6,105.5 132.6,103.4 135.6,101.4 138.6,99.5 141.6,97.6 144.7,95.8 147.7,94.0 150.7,92.3 153.7,90.7 156.8,89.1 159.8,87.6 162.8,86.1 165.8,84.7 168.8,83.3 171.9,82.0 174.9,80.7 177.9,79.4 180.9,78.2 184.0,77.1 187.0,75.9 190.0,74.9 193.0,73.8 196.0,72.8 199.1,71.8 202.1,70.9 205.1,70.0 208.1,69.1 211.2,68.3 214.2,67.4 217.2,66.7 220.2,65.9 223.2,65.2 226.3,64.4 229.3,63.8 232.3,63.1 235.3,62.4 238.4,61.8 241.4,61.2 244.4,60.6 247.4,60.1 250.4,59.5 253.5,59.0 256.5,58.5 259.5,58.0 262.5,57.6 265.6,57.1 268.6,56.7 271.6,56.2 274.6,55.8 277.6,55.4 280.7,55.1 283.7,54.7 286.7,54.3 289.7,54.0 292.8,53.7 295.8,53.3 298.8,53.0 301.8,52.7 304.8,52.4 307.9,52.2 310.9,51.9 313.9,51.6 316.9,51.4 320.0,51.1 323.0,50.9 326.0,50.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="54.0" y1="190.0" x2="235.3" y2="62.4" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 3"/><line x1="78.2" y1="141.7" x2="180.9" y2="69.4" stroke="#c2410c" stroke-width="2"/><line x1="129.6" y1="190.0" x2="129.6" y2="105.5" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/><circle cx="129.6" cy="105.5" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="235.3" cy="62.4" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="54.0" cy="190.0" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><text x="119.6" y="97.5" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text><text x="120.6" y="184.0" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t*</text><text x="231.3" y="86.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sécante</text></svg>
:::

Cherchons maintenant l'instant où v(t) vaut la vitesse moyenne sur [0 ; 30]. Sur la figure, la sécante joint l'origine au point d'abscisse 30 min, et la tangente parallèle touche la courbe au point P d'abscisse t*.

::: exemple Quand la vitesse instantanée égale la moyenne

1. v_moy(0 ; 30) = (7,0 − 0)/(30 − 0) ≈ 0,23 mmol·min⁻¹, c'est la pente de la sécante.
2. On trace la tangente parallèle à cette sécante : deux droites parallèles ont la même pente, donc au point de contact v(t*) = 0,23 mmol·min⁻¹. La lecture donne t* ≈ 12,5 min.
3. Ce t* est avant le milieu 15 min : à 15 min, la tangente est déjà moins raide que la sécante (v(15) ≈ 0,20 < 0,23), car la vitesse chute plus vite au début qu'à la fin.

:::

::: propriete
**Évolution de la vitesse** — Pour les transformations étudiées dans ce chapitre, la vitesse est maximale à t = 0, puis diminue et tend vers 0 à la fin. Entre deux instants t₁ et t₂, il existe au moins un instant t* de ]t₁ ; t₂[ où v(t*) = v_moy(t₁ ; t₂) : la tangente est alors parallèle à la sécante.
Cas limite : le temps de demi-réaction t₁/₂ (x = x_f/2, avec x_f = x_max pour une transformation totale ; ici 10 min) n'est pas la durée totale : à 40 min, x = 7,5 mmol, soit 94 % de x_max, et la réaction se poursuit après t₁/₂.
:::

::: verifie À toi : lire la décroissance sur des mesures
Une autre réaction donne : t = 0 ; 4 ; 8 ; 12 min et x = 0 ; 3,0 ; 5,0 ; 6,5 mmol. Calculer v_moy sur [0 ; 4], [4 ; 8] et [8 ; 12], puis dire comment la vitesse évolue.

---

v_moy(0 ; 4) = 3,0/4 = 0,75 ; v_moy(4 ; 8) = (5,0 − 3,0)/4 = 0,50 ; v_moy(8 ; 12) = (6,5 − 5,0)/4 ≈ 0,38 mmol·min⁻¹. Les trois valeurs diminuent : la vitesse décroît au cours de la transformation, comme pour la courbe étudiée.
:::

::: retenir
Pour les transformations étudiées dans ce chapitre, la vitesse est maximale à t = 0 puis décroît vers 0, et v_moy(t₁ ; t₂) est atteinte en un instant intermédiaire où la tangente est parallèle à la sécante.
:::

> 🏆 Tu sais désormais chronométrer une réaction : une pente pour la moyenne, une tangente pour l'instant, et une division par le coefficient pour passer d'une espèce à l'autre. Le chapitre suivant dira ce qui fait aller plus vite ou plus lentement.
