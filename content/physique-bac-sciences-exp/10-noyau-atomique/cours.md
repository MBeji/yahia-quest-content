# ⚛️ Le noyau atomique — peser le noyau, mesurer sa cohésion

> 💡 «Un noyau pèse moins que la somme de ses morceaux : la masse qui manque est l'énergie qui les retient ensemble.»

Au centre de l'atome, le noyau est minuscule et pourtant il concentre presque toute la masse. Dans ce chapitre, tu apprends à le décrire (ses nucléons, ses isotopes), à comprendre pourquoi il ne se disloque pas, puis à le **peser** : sa masse est inférieure à celle de ses constituants, et la relation d'Einstein transforme cette différence en une énergie, qui dit si un noyau est solidement lié. Huit notions te mènent de la composition du noyau à la courbe d'Aston et au diagramme des noyaux stables. On suppose acquis les constituants de l'atome et la conversion entre joule et électron-volt.

Sauf indication contraire, on utilise : m_p = 1,00728 u ; m_n = 1,00867 u ; 1 u = 1,66 × 10⁻²⁷ kg = 931,5 MeV·c⁻² ; c = 3,00 × 10⁸ m/s ; 1 MeV = 1,60 × 10⁻¹³ J.

## 🧱 Le noyau, ses nucléons et ses isotopes

Au centre de l'atome, le noyau renferme la quasi-totalité de sa masse, alors que son rayon est environ 100 000 fois plus petit que celui de l'atome (de l'ordre de 100 pm).
Comment désigner un noyau sans ambiguïté ? Et le chlore du sel de cuisine est-il fait d'un seul type de noyau ?

::: definition
**Noyau, nucléons, isotopes** — Le noyau est formé de **nucléons** : des **protons** (notés ¹₁p) et des **neutrons** (notés ¹₀n). On note ᴬ_Z X le noyau de l'élément X, où :

- A est le **nombre de masse**, le nombre total de nucléons ;
- Z est le **nombre de charge**, le nombre de protons (le numéro atomique de l'élément) ;
- N = A − Z est le nombre de neutrons.

Des noyaux de même Z et de A différents sont des **isotopes** : un élément naturel peut être un mélange d'isotopes.
:::

::: exemple Lire et écrire le symbole d'un noyau (chlore 35 et 37, fer 56)

1. Pour ³⁵₁₇Cl : Z = 17 donne 17 protons, A = 35 donne 35 nucléons, donc N = 35 − 17 = 18 neutrons, car tout nucléon qui n'est pas un proton est un neutron.
2. Pour ³⁷₁₇Cl : Z = 17 comme avant, A = 37, donc N = 37 − 17 = 20. Même nombre de protons (même élément), deux neutrons de plus : ces deux noyaux sont des isotopes du chlore.
3. Un noyau de 26 protons et 30 neutrons a A = 26 + 30 = 56 nucléons. Z = 26 identifie l'élément fer : son symbole est ⁵⁶₂₆Fe.
4. Ordre de grandeur : le rayon de l'atome est de l'ordre de 100 pm = 10⁻¹⁰ m ; divisé par 10⁵, celui du noyau est de l'ordre de 10⁻¹⁵ m, soit 1 fm (un fermi).

:::

::: piege
**Erreur : lire A comme le nombre de neutrons.** Pour ³⁷₁₇Cl, on pourrait annoncer 37 neutrons. Mais 37 compte tous les nucléons, protons compris : N = 37 − 17 = 20 (étape 2). L'erreur tente parce que A est le nombre le plus visible du symbole. Le contrôle est Z + N = A : 17 + 20 = 37.
:::

::: propriete
**Ce qui reste vrai** — A = Z + N pour tout noyau. Deux isotopes ont le même Z, donc le même élément chimique, et diffèrent par leur nombre de neutrons N et leur masse. Cas limite : le noyau de l'hydrogène ordinaire, ¹₁H, est un proton seul, avec N = 0.
:::

::: verifie À toi : le zinc
Donner la composition du noyau ⁶⁴₃₀Zn, puis dire si ⁶⁶₃₀Zn en est un isotope.

---

⁶⁴₃₀Zn : Z = 30 donne 30 protons, et N = 64 − 30 = 34 neutrons. ⁶⁶₃₀Zn a le même Z = 30, donc le même élément, mais A = 66 : N = 66 − 30 = 36. Même nombre de protons et nombre de neutrons différent : c'est bien un isotope.
:::

::: retenir
Un noyau ᴬ_Z X contient Z protons et N = A − Z neutrons ; des isotopes ont le même Z et des A différents.
:::

## 🧲 La cohésion du noyau : l'interaction forte

Dans le noyau d'hélium ⁴₂He, deux protons sont séparés par une distance de l'ordre du fermi. Deux charges positives aussi proches se repoussent violemment, et pourtant le noyau tient.
Quelle force retient les nucléons ensemble, et agit-elle seulement sur les protons ?

::: definition
**Interaction forte** — C'est la force **attractive** qui s'exerce entre nucléons voisins, **quelle que soit leur nature** (proton–proton, proton–neutron, neutron–neutron). Sa portée est **très courte**, de l'ordre du fermi (1 fm = 10⁻¹⁵ m). À la distance qui sépare deux nucléons voisins, elle est environ 100 fois plus intense que la répulsion électrique entre deux protons : elle assure la cohésion du noyau.
:::

::: figure Trois paires de nucléons voisins : l'attraction forte (flèches vertes) existe dans les trois paires, la répulsion électrique (flèches rouges) seulement entre les deux protons ; les longueurs des flèches ne sont pas à l'échelle (au contact, la flèche verte est environ 100 fois plus grande que la rouge)
<svg viewBox="0 0 340 170"><title>Trois paires de nucléons voisins : proton-proton, proton-neutron, neutron-neutron ; flèches vertes d'attraction forte dans chaque paire, flèches rouges de répulsion électrique seulement entre les deux protons</title><text x="60.0" y="22.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p – p</text><circle cx="41.0" cy="88.0" r="17" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/><text x="41.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p</text><circle cx="79.0" cy="88.0" r="17" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/><text x="79.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p</text><line x1="30.0" y1="54.0" x2="48.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="54.0,54.0 48.0,56.7 48.0,51.3" fill="#0f6e56"/><line x1="90.0" y1="54.0" x2="72.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="66.0,54.0 72.0,51.3 72.0,56.7" fill="#0f6e56"/><text x="60.0" y="46.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">forte</text><line x1="52.0" y1="122.0" x2="39.0" y2="122.0" stroke="#b91c1c" stroke-width="1.6" stroke-linecap="round"/><polygon points="34.0,122.0 39.0,119.8 39.0,124.2" fill="#b91c1c"/><line x1="68.0" y1="122.0" x2="81.0" y2="122.0" stroke="#b91c1c" stroke-width="1.6" stroke-linecap="round"/><polygon points="86.0,122.0 81.0,124.2 81.0,119.8" fill="#b91c1c"/><text x="60.0" y="142.0" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">électrique</text><text x="170.0" y="22.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p – n</text><circle cx="151.0" cy="88.0" r="17" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/><text x="151.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p</text><circle cx="189.0" cy="88.0" r="17" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8"/><text x="189.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n</text><line x1="140.0" y1="54.0" x2="158.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="164.0,54.0 158.0,56.7 158.0,51.3" fill="#0f6e56"/><line x1="200.0" y1="54.0" x2="182.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="176.0,54.0 182.0,51.3 182.0,56.7" fill="#0f6e56"/><text x="170.0" y="46.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">forte</text><text x="280.0" y="22.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n – n</text><circle cx="261.0" cy="88.0" r="17" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8"/><text x="261.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n</text><circle cx="299.0" cy="88.0" r="17" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8"/><text x="299.0" y="93.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n</text><line x1="250.0" y1="54.0" x2="268.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="274.0,54.0 268.0,56.7 268.0,51.3" fill="#0f6e56"/><line x1="310.0" y1="54.0" x2="292.0" y2="54.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="286.0,54.0 292.0,51.3 292.0,56.7" fill="#0f6e56"/><text x="280.0" y="46.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">forte</text></svg>
:::

Sur la figure, la paire p – p porte à la fois une attraction forte et une répulsion électrique ; les paires p – n et n – n n'ont que l'attraction forte, puisqu'un neutron n'a pas de charge.

::: exemple Les interactions dans le noyau d'hélium ⁴₂He (2 protons, 2 neutrons)

1. Le noyau compte 4 nucléons, donc 4 × 3 / 2 = 6 paires : chaque nucléon se couple aux 3 autres, et on compte chaque paire une seule fois.
2. Types de paires : 1 paire p – p, 1 paire n – n et 2 × 2 = 4 paires p – n, soit 1 + 1 + 4 = 6 paires ✓.
3. L'interaction forte est attractive dans les 6 paires, puisqu'elle ne dépend pas de la nature des nucléons.
4. La répulsion électrique n'existe que dans l'unique paire p – p : les neutrons, sans charge, n'en subissent aucune.
5. Bilan : la paire de protons est 100 fois plus attirée que repoussée, et les cinq autres paires ne font que s'attirer : le noyau est lié.

:::

::: piege
**Erreur : croire que l'interaction forte ne s'exerce qu'entre protons.** Dans ⁴₂He, on omettrait alors la paire n – n et les quatre paires p – n (étape 3). L'erreur tente parce que cette force est présentée comme celle qui compense la répulsion entre protons. Mais elle ne « voit » pas la charge : elle agit entre tous les nucléons voisins.
:::

::: propriete
**Ce qui reste vrai** — L'interaction forte est attractive, indépendante de la charge, et de très courte portée : au-delà de quelques fermis, son effet est négligeable. Elle n'est ni électrique (l'interaction électrique repousse les protons) ni gravitationnelle (bien trop faible à cette échelle). Cas limite : deux protons éloignés de plusieurs fermis ne s'attirent plus par l'interaction forte, mais se repoussent encore, car la répulsion électrique est de longue portée.
:::

::: verifie À toi : l'hélium 3
Le noyau ³₂He compte 2 protons et 1 neutron. Combien de paires de nucléons contient-il, et quelles interactions s'exercent dans chaque type de paire ?

---

Il y a 3 × 2 / 2 = 3 paires : 1 paire p – p et 2 paires p – n (aucune paire n – n, car il n'y a qu'un neutron). Dans la paire p – p s'exercent l'attraction forte et la répulsion électrique ; dans chacune des deux paires p – n, seulement l'attraction forte, car le neutron n'a pas de charge. L'attraction forte agit donc dans les 3 paires.
:::

::: retenir
L'interaction forte est attractive, de très courte portée et indépendante de la nature des nucléons : elle l'emporte sur la répulsion électrique entre protons voisins.
:::

## ⚖️ Le défaut de masse

On mesure la masse d'un proton libre, 1,00728 u, et celle d'un neutron libre, 1,00867 u, en unité de masse atomique u (définie ci-dessous). Le noyau de deutérium ²₁H, formé d'un proton et d'un neutron, a pour masse 2,01355 u.
Le noyau pèse-t-il autant que ses deux constituants pris séparément ?

::: definition
**Unité de masse atomique** — 1 u est le douzième de la masse d'un atome de carbone 12. Comme un atome de carbone 12 a pour masse 19,93 × 10⁻²⁷ kg, 1 u = 19,93 × 10⁻²⁷ / 12 = 1,66 × 10⁻²⁷ kg.
:::

::: definition
**Défaut de masse** — Le défaut de masse Δm d'un noyau ᴬ_Z X, de masse m_X, est la masse de ses nucléons pris séparément et au repos, diminuée de la masse du noyau :

$$ Δm = Z·m_p + (A − Z)·m_n − m_X $$
:::

::: exemple Du deutérium à l'azote 14

1. Deutérium : les nucléons séparés pèsent 1,00728 + 1,00867 = 2,01595 u.
2. Le noyau pèse 2,01355 u, donc Δm = 2,01595 − 2,01355 = 0,00240 u, car on retranche la masse du noyau à celle de ses constituants.
3. Contrôle du signe : Δm > 0, le noyau est plus léger que ses nucléons séparés ✓.
4. Azote 14, ¹⁴₇N, de masse 13,99923 u : 7 protons et 14 − 7 = 7 neutrons, donc 7 × 1,00728 + 7 × 1,00867 = 7,05096 + 7,06069 = 14,11165 u, et Δm = 14,11165 − 13,99923 = 0,11242 u.
5. En kilogrammes : 0,11242 × 1,66 × 10⁻²⁷ = 1,87 × 10⁻²⁸ kg, car 1 u = 1,66 × 10⁻²⁷ kg.

:::

::: piege
**Erreur : écrire Δm = m_X − (masse des nucléons).** Pour le deutérium, on trouverait −0,00240 u (étape 2). L'erreur tente parce qu'on calcule souvent « final moins initial ». Mais le défaut de masse d'un noyau de plusieurs nucléons est positif : on retranche la masse du noyau à celle des nucléons séparés.
:::

::: propriete
**Ce qui reste vrai** — Pour un noyau de plusieurs nucléons, Δm > 0 : la masse du noyau est inférieure à celle de ses nucléons séparés et au repos. Δm s'exprime en u, en kg ou en MeV·c⁻². Cas limite : un noyau d'un seul nucléon, comme ¹₁H (un proton), a Δm = 1·m_p + 0·m_n − m_p = 0.
:::

::: verifie À toi : le calcium 40
Calculer le défaut de masse du noyau ⁴⁰₂₀Ca, de masse 39,95162 u.

---

⁴⁰₂₀Ca compte 20 protons et 40 − 20 = 20 neutrons. Les nucléons séparés pèsent 20 × 1,00728 + 20 × 1,00867 = 20,1456 + 20,1734 = 40,3190 u, donc Δm = 40,3190 − 39,95162 = 0,36738 u. Le signe est positif, comme il se doit.
:::

::: retenir
Δm = Z·m_p + (A − Z)·m_n − m_X est positif pour un noyau de plusieurs nucléons : il pèse moins que ses nucléons séparés.
:::

## ⚡ L'énergie de masse : la relation d'Einstein

Le noyau de deutérium est plus léger de 0,00240 u que son proton et son neutron. Une masse qui manque ne disparaît pas sans laisser de trace : en 1905, Einstein affirme que la masse est elle-même une forme d'énergie.
Quelle énergie représente ce défaut de masse de 0,00240 u ?

::: definition
**Énergie de masse** — Une particule de masse m, au repos dans un référentiel, possède du seul fait de sa masse une énergie potentielle E₀, avec c la célérité de la lumière dans le vide :

$$ E₀ = m·c² $$

Toute variation de masse Δm s'accompagne d'une variation d'énergie :

$$ ΔE = Δm·c² $$
:::

::: definition
**Unités** — Avec m en kg et c en m/s, E est en joules. À l'échelle du noyau, on exprime l'énergie en MeV (1 MeV = 1,60 × 10⁻¹³ J) et la masse en MeV·c⁻², ce qui donne :

$$ 1 u = 931,5 MeV·c⁻² $$

Une particule de m unités de masse atomique a donc une énergie de masse de m × 931,5 MeV.
:::

| Masse                       | Énergie de masse E₀ = m·c² |
| --------------------------- | -------------------------- |
| 1 kg                        | 9,00 × 10¹⁶ J              |
| 1 u                         | 931,5 MeV                  |
| un proton (1,00728 u)       | 938,3 MeV                  |

Dans le tableau, la colonne de droite se lit aussi comme une masse en MeV·c⁻² : un proton pèse 938,3 MeV·c⁻², et c'est cette valeur qui, multipliée par c², donne son énergie.

::: exemple Quelle énergie pour le défaut de masse du deutérium ? (Δm = 0,00240 u)

1. Δm = 0,00240 × 931,5 = 2,24 MeV·c⁻², car 1 u = 931,5 MeV·c⁻².
2. ΔE = Δm·c² = 2,24 MeV·c⁻² × c² = 2,24 MeV : le c² de l'unité compense celui de la relation.
3. En joules : 2,24 × 1,60 × 10⁻¹³ = 3,58 × 10⁻¹³ J, car 1 MeV = 1,60 × 10⁻¹³ J.
4. Autre chemin par le kilogramme : Δm = 0,00240 × 1,66 × 10⁻²⁷ = 3,98 × 10⁻³⁰ kg, puis ΔE = 3,98 × 10⁻³⁰ × (3,00 × 10⁸)² = 3,59 × 10⁻¹³ J : même valeur, à l'arrondi près ✓.
5. Une masse courante : pour m = 1,0 mg = 1,0 × 10⁻⁶ kg, E₀ = 1,0 × 10⁻⁶ × (3,00 × 10⁸)² = 9,0 × 10¹⁰ J, car m doit être en kg.

:::

::: piege
**Erreur : reporter m en grammes (ou oublier le carré de c).** Avec m = 1,0 mg écrit 1,0 × 10⁻³ g, on trouverait 9,0 × 10¹³ J, mille fois trop (étape 5). L'erreur tente parce que le gramme est l'unité usuelle de masse. Mais la relation donne des joules seulement si m est en kilogrammes et c en mètres par seconde.
:::

::: propriete
**Ce qui reste vrai** — La masse est une forme d'énergie : E₀ = m·c², ΔE = Δm·c², et E (en MeV) = m (en u) × 931,5. Cas limite d'arrondi : le chemin par le kilogramme donne 1,66 × 10⁻²⁷ × (3,00 × 10⁸)² / 1,60 × 10⁻¹³ ≈ 934 MeV, soit environ 0,2 % de plus que 931,5 : ce petit écart vient des arrondis de 1,66, de 3,00 et de 1,60. On retient 931,5 MeV·c⁻² pour 1 u.
:::

::: verifie À toi : l'électron
La masse d'un électron est 9,11 × 10⁻³¹ kg. Calculer son énergie de masse en joules, puis en MeV.

---

E₀ = m·c² = 9,11 × 10⁻³¹ × (3,00 × 10⁸)² = 8,20 × 10⁻¹⁴ J, avec m en kg et c en m/s. Pour passer en MeV, on divise par 1,60 × 10⁻¹³ J par MeV : 8,20 × 10⁻¹⁴ / 1,60 × 10⁻¹³ = 0,512 MeV.
:::

::: retenir
E₀ = m·c² et ΔE = Δm·c² ; avec 1 u = 931,5 MeV·c⁻², une masse de m unités a l'énergie m × 931,5 MeV.
:::

## 🔗 L'énergie de liaison

Reprenons le deutérium : son défaut de masse de 0,00240 u équivaut à 2,24 MeV. Imaginons séparer le proton et le neutron et les immobiliser loin l'un de l'autre.
Faut-il fournir de l'énergie au noyau, ou en reçoit-on ? Et combien ?

::: definition
**Énergie de liaison** — L'énergie de liaison E_ℓ d'un noyau est l'énergie qu'il faut fournir à ce noyau, au repos, pour le dissocier en nucléons isolés et au repos. Elle est la traduction énergétique du défaut de masse :

$$ E_ℓ = Δm·c² $$

Avec E_p = m_p·c², E_n = m_n·c² et E_X = m_X·c², cela s'écrit aussi :

$$ E_ℓ = Z·E_p + (A − Z)·E_n − E_X $$
:::

::: figure Diagramme d'énergie d'un noyau : le niveau des nucléons séparés et au repos (E₂) est plus haut que celui du noyau au repos (E₁) ; la marche entre les deux est l'énergie de liaison à fournir ; les hauteurs ne sont pas à l'échelle
<svg viewBox="0 0 340 200"><title>Diagramme d'énergie : le niveau des nucléons séparés et au repos E2 est au-dessus du niveau du noyau au repos E1 ; l'écart est l'énergie de liaison E_l = Δm·c²</title><line x1="40.0" y1="185.0" x2="40.0" y2="22.0" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="40.0,16.0 42.7,22.0 37.3,22.0" fill="#0f172a"/><text x="40.0" y="11.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">énergie</text><line x1="70.0" y1="52.0" x2="320.0" y2="52.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><line x1="70.0" y1="150.0" x2="320.0" y2="150.0" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><text x="195.0" y="42.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">nucléons séparés, au repos : E₂</text><text x="195.0" y="172.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">noyau au repos : E₁ = m_X·c²</text><line x1="110.0" y1="146.0" x2="110.0" y2="64.0" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/><polygon points="110.0,56.0 113.6,64.0 106.4,64.0" fill="#b45309"/><text x="122.0" y="106.0" text-anchor="start" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E_ℓ = Δm·c²</text><text x="122.0" y="122.0" text-anchor="start" font-size="11" font-weight="400" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(énergie à fournir)</text></svg>
:::

Sur le schéma, la flèche orange est la marche entre E₁ et E₂ : elle représente E_ℓ, puisque la conservation de l'énergie impose E₁ + E_ℓ = E₂.

::: exemple Du deutérium à l'azote 14

1. Deutérium : E_ℓ = Δm × 931,5 = 0,00240 × 931,5 = 2,24 MeV : il faut fournir au moins 2,24 MeV pour séparer le proton et le neutron.
2. Azote 14, avec Δm = 0,11242 u (notion précédente) : E_ℓ = 0,11242 × 931,5 = 104,7 MeV.
3. Contrôle par les énergies de masse : E_p = 1,00728 × 931,5 = 938,28 MeV, E_n = 1,00867 × 931,5 = 939,58 MeV et E_X = 13,99923 × 931,5 = 13 040,28 MeV, donc E_ℓ = 7 × 938,28 + 7 × 939,58 − 13 040,28 = 104,7 MeV ✓.
4. Interprétation : pour séparer les 14 nucléons au repos, il faut apporter au minimum 104,7 MeV, car l'énergie des nucléons séparés dépasse de E_ℓ celle du noyau.

:::

::: piege
**Erreur : prendre l'énergie de masse du noyau pour son énergie de liaison.** Pour l'azote 14, E_X = m_X·c² = 13 040,28 MeV, contre E_ℓ = 104,7 MeV (étape 3) : un rapport de plus de 100. L'erreur tente parce qu'on parle d'« énergie du noyau ». Mais E_ℓ est seulement l'écart entre deux niveaux, soit ici 0,8 % de l'énergie de masse des nucléons séparés.
:::

::: propriete
**Ce qui reste vrai** — E_ℓ = Δm·c² est positive pour un noyau de plusieurs nucléons et s'obtient en MeV par E_ℓ = Δm (en u) × 931,5. Pour une mole de noyaux, il suffit de multiplier par la constante d'Avogadro 𝒩 = 6,02 × 10²³ mol⁻¹. Cas limite : pour ¹⁴₇N, une mole demande 104,7 × 1,60 × 10⁻¹³ × 6,02 × 10²³ = 1,01 × 10¹³ J, une énergie macroscopique alors que 104,7 MeV est minuscule.
:::

::: verifie À toi : l'oxygène 16
Calculer l'énergie de liaison du noyau ¹⁶₈O, de masse 15,99053 u, en MeV.

---

¹⁶₈O compte 8 protons et 8 neutrons : 8 × 1,00728 + 8 × 1,00867 = 16,1276 u. Donc Δm = 16,1276 − 15,99053 = 0,13707 u, et E_ℓ = Δm × 931,5 = 0,13707 × 931,5 = 127,7 MeV.
:::

::: retenir
E_ℓ = Δm·c² : c'est l'énergie à fournir à un noyau au repos pour le dissocier en nucléons isolés et au repos.
:::

## 📏 L'énergie de liaison par nucléon : comparer la stabilité

Le fer ⁵⁶Fe a une énergie de liaison de 492,5 MeV et le plomb ²⁰⁸Pb de 1 637,3 MeV, plus de trois fois plus. Le plomb a aussi plus de nucléons à retenir.
Le plomb est-il pour autant plus solidement lié que le fer ?

::: definition
**Énergie de liaison par nucléon** — L'énergie de liaison par nucléon E_ℓ/A est l'énergie de liaison moyenne par nucléon du noyau :

$$ E_ℓ / A = Δm·c² / A $$

Plus E_ℓ/A est grande, plus les nucléons sont fortement liés et plus le noyau est **stable**.
:::

::: exemple Fer 56 contre plomb 208 (m_Fe = 55,92067 u ; m_Pb = 207,93167 u)

1. Fer : 26 protons et 30 neutrons, donc Δm = 26 × 1,00728 + 30 × 1,00867 − 55,92067 = 56,44938 − 55,92067 = 0,52871 u.
2. E_ℓ(Fe) = 0,52871 × 931,5 = 492,5 MeV, puis E_ℓ/A = 492,5 / 56 = 8,79 MeV.
3. Plomb : 82 protons et 126 neutrons, donc Δm = 209,68938 − 207,93167 = 1,75771 u, E_ℓ(Pb) = 1,75771 × 931,5 = 1 637,3 MeV et E_ℓ/A = 1 637,3 / 208 = 7,87 MeV.
4. Comparaison : E_ℓ(Pb) est plus grande, mais E_ℓ/A(Fe) = 8,79 MeV dépasse E_ℓ/A(Pb) = 7,87 MeV : le fer est plus stable, car chacun de ses nucléons est en moyenne mieux lié.

:::

::: piege
**Erreur : comparer la stabilité de deux noyaux avec leurs énergies de liaison.** On conclurait que le plomb est le plus stable (étape 4). L'erreur tente parce qu'une énergie de liaison plus grande semble signifier « plus lié ». Mais E_ℓ est un total qui croît avec le nombre de nucléons : deux noyaux de A différents se comparent avec l'énergie par nucléon.
:::

::: propriete
**Ce qui reste vrai** — L'énergie de liaison est à peu près proportionnelle à A, donc E_ℓ/A varie peu d'un noyau à l'autre, de l'ordre de 8 MeV pour la plupart. Un noyau est d'autant plus stable que son E_ℓ/A est grande. Cas limite : pour deux noyaux de même A, comparer E_ℓ ou E_ℓ/A donne le même classement.
:::

::: verifie À toi : aluminium contre plomb
On donne E_ℓ(²⁷Al) = 225,1 MeV et E_ℓ(²⁰⁸Pb) = 1 637,3 MeV. Lequel est le plus stable ?

---

Les nombres de nucléons diffèrent, donc on compare E_ℓ/A. Pour ²⁷Al : 225,1 / 27 = 8,34 MeV. Pour ²⁰⁸Pb : 1 637,3 / 208 = 7,87 MeV. L'aluminium a la plus grande énergie par nucléon : il est plus stable, bien que son énergie de liaison soit plus de sept fois plus petite.
:::

::: retenir
Plus E_ℓ/A = Δm·c² / A est grande, plus le noyau est stable ; on compare deux noyaux avec E_ℓ/A, jamais avec E_ℓ.
:::

## 📈 La courbe d'Aston

Nous avons obtenu E_ℓ = 104,7 MeV pour ¹⁴N, soit E_ℓ/A = 7,48 MeV, puis E_ℓ/A = 8,79 MeV pour ⁵⁶Fe et 7,87 MeV pour ²⁰⁸Pb. Plaçons tous les noyaux connus sur un même graphique, avec A en abscisse et E_ℓ/A en ordonnée.
Quelle forme dessinent-ils, et où se trouvent les noyaux les plus stables ?

::: definition
**Courbe d'Aston** — C'est le graphique de E_ℓ/A (en MeV, positive) en fonction du nombre de masse A. Elle présente trois zones :

- pour A < 20 environ, E_ℓ/A est plus petite et croît très vite avec A ;
- vers A ≈ 60, elle atteint son maximum (≈ 8,8 MeV, au voisinage du fer ⁵⁶Fe) ; les noyaux de nombre de masse voisin de 60 ont 7,8 MeV < E_ℓ/A < 8,8 MeV (« de l'ordre de 8 MeV ») : ce sont les plus stables ;
- au-delà de A ≈ 60, elle décroît lentement : pour A > 190 environ, les noyaux lourds sont nettement moins liés.
:::

::: figure Courbe d'Aston (valeurs arrondies) : E_ℓ/A en MeV en fonction de A ; le maximum se trouve vers le fer ⁵⁶Fe, le plomb et l'uranium sont plus bas, et le noyau d'hélium ⁴He forme un pic au-dessus de ses voisins légers
<svg viewBox="0 0 340 236"><title>Courbe d'Aston : énergie de liaison par nucléon en fonction du nombre de masse, avec un maximum vers A = 56 (fer) et une décroissance lente pour les noyaux lourds</title><line x1="46.0" y1="178.7" x2="326.0" y2="178.7" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="182.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="46.0" y1="161.3" x2="326.0" y2="161.3" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="165.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="46.0" y1="144.0" x2="326.0" y2="144.0" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="148.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="46.0" y1="126.7" x2="326.0" y2="126.7" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="130.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="46.0" y1="109.3" x2="326.0" y2="109.3" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="113.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="46.0" y1="92.0" x2="326.0" y2="92.0" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="96.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="46.0" y1="74.7" x2="326.0" y2="74.7" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="78.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><line x1="46.0" y1="57.3" x2="326.0" y2="57.3" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="61.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="46.0" y1="40.0" x2="326.0" y2="40.0" stroke="#cbd5e1" stroke-width="0.8" stroke-linecap="round"/><text x="40.0" y="44.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">9</text><text x="40.0" y="200.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="46.0" y1="196.0" x2="326.0" y2="196.0" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="46.0" y1="196.0" x2="46.0" y2="30.0" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,196 324,192.5 324,199.5" fill="#0f172a"/><polygon points="46,24 42.5,32 49.5,32" fill="#0f172a"/><line x1="46.0" y1="196.0" x2="46.0" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="46.0" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="92.7" y1="196.0" x2="92.7" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="92.7" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="139.3" y1="196.0" x2="139.3" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="139.3" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="186.0" y1="196.0" x2="186.0" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="186.0" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="232.7" y1="196.0" x2="232.7" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="232.7" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">160</text><line x1="279.3" y1="196.0" x2="279.3" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="279.3" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">200</text><line x1="326.0" y1="196.0" x2="326.0" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="326.0" y="213.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">240</text><text x="326.0" y="225.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="54.0" y="13.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E_ℓ/A (MeV)</text><polyline points="47.2,196.0 48.3,176.9 49.5,150.9 53.0,104.1 56.5,83.3 60.0,62.5 64.7,57.3 69.3,57.3 77.5,51.6 92.7,47.8 111.3,43.6 139.3,45.0 186.0,48.5 232.7,54.2 288.7,59.6 323.7,64.8" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="50.7" cy="73.5" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><circle cx="64.7" cy="57.3" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><circle cx="111.3" cy="43.6" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><circle cx="186.0" cy="48.5" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><circle cx="288.7" cy="59.6" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><circle cx="323.7" cy="64.8" r="3.6" fill="#b45309" stroke="#0f172a" stroke-width="1"/><line x1="54.7" y1="76.5" x2="90.7" y2="107.5" stroke="#94a3b8" stroke-width="1" stroke-linecap="round"/><text x="104.7" y="117.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">⁴He</text><line x1="68.7" y1="61.3" x2="94.7" y2="79.3" stroke="#94a3b8" stroke-width="1" stroke-linecap="round"/><text x="108.7" y="87.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">¹⁶O</text><text x="111.3" y="34.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">⁵⁶Fe</text><text x="186.0" y="39.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">¹²⁰Sn</text><text x="288.7" y="50.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">²⁰⁸Pb</text><text x="319.7" y="83.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">²³⁸U</text></svg>
:::

Sur la courbe, chaque point est un noyau : son abscisse est A, son ordonnée est E_ℓ/A, et le sommet de la courbe est le point du fer ⁵⁶Fe. Certains documents tracent −E_ℓ/A : la courbe est alors retournée et le noyau le plus stable est au minimum ; ici on trace E_ℓ/A, et il est au maximum.

::: exemple Lire la courbe d'Aston (valeurs lues sur la grille, à 0,1 MeV près)

1. On lit E_ℓ/A ≈ 8,0 MeV pour ¹⁶O, ≈ 8,8 MeV pour ⁵⁶Fe et ≈ 7,9 MeV pour ²⁰⁸Pb.
2. Par stabilité décroissante : ⁵⁶Fe, puis ¹⁶O, puis ²⁰⁸Pb, car plus l'ordonnée est grande, plus le noyau est stable.
3. Pour ²³⁸U, on lit environ 7,6 MeV : il est moins lié que ⁵⁶Fe, bien qu'il ait beaucoup plus de nucléons.
4. Le noyau ⁴He, qui vérifie A = 2Z, forme un pic au-dessus de ses voisins légers (≈ 7,1 MeV, contre ≈ 2,6 MeV pour ³He et ≈ 5,3 MeV pour ⁶Li) : il est particulièrement stable. D'autres noyaux légers tels que A = 2Z (¹²C, ¹⁶O) sont aussi plus liés que leurs voisins immédiats, ce que l'échelle de la figure ne montre pas.
5. Le fer 56 est aussi très abondant : l'isotope ⁵⁶Fe représente plus de 90 % du fer naturel, ce qui s'accorde avec sa grande stabilité.

:::

::: piege
**Erreur : lire la courbe comme « plus A est grand, plus le noyau est stable ».** On classerait alors ²⁰⁸Pb avant ⁵⁶Fe (étapes 2 et 3). L'erreur tente parce que l'énergie de liaison E_ℓ augmente bien avec A. Mais la stabilité se lit sur la hauteur de la courbe, pas sur l'abscisse : le maximum est vers A ≈ 60.
:::

::: propriete
**Ce qui reste vrai** — Les noyaux de nombre de masse voisin de 60 ont la plus grande E_ℓ/A (entre 7,8 et 8,8 MeV) : ce sont les plus stables. Les noyaux légers (A < 20) et les noyaux lourds (A > 190) ont une E_ℓ/A plus faible. Cas limite : la courbe n'est pas monotone, deux noyaux de A différents peuvent avoir la même hauteur, comme ⁴⁰Ca et ¹²⁰Sn, tous deux autour de 8,5 MeV ; E_ℓ/A seule ne permet donc pas de retrouver A.
:::

::: verifie À toi : trois noyaux sur la courbe
D'après la courbe, classer ¹⁶O, ⁵⁶Fe et ²³⁸U par stabilité croissante.

---

On lit E_ℓ/A ≈ 7,6 MeV pour ²³⁸U, ≈ 8,0 MeV pour ¹⁶O et ≈ 8,8 MeV pour ⁵⁶Fe. Plus E_ℓ/A est grande, plus le noyau est stable, donc l'ordre croissant de stabilité est ²³⁸U, puis ¹⁶O, puis ⁵⁶Fe.
:::

::: retenir
La courbe d'Aston passe par un maximum (≈ 8,8 MeV) vers A ≈ 60 : les noyaux les plus stables sont ceux du fer, les noyaux légers et lourds sont moins liés.
:::

## 🧮 Les noyaux stables dans le diagramme (N, Z)

Il n'existe qu'environ 260 noyaux stables, et aucun au-delà du bismuth (Z = 83). Plaçons chacun au point d'abscisse Z et d'ordonnée N = A − Z.
Ces points suivent-ils la droite N = Z, c'est-à-dire autant de neutrons que de protons ?

::: propriete
**Diagramme (N, Z) des noyaux stables** — Pour Z inférieur ou voisin de 20, les noyaux stables ont N voisin de Z. Au-delà de Z = 20, un noyau stable a un excès de neutrons (N > Z), et cet excès augmente avec Z. Au-delà de Z = 83, aucun noyau n'est stable.
:::

::: figure Diagramme (Z, N) de quatre noyaux stables : les points s'écartent de la droite pointillée N = Z, vers le haut, quand Z augmente
<svg viewBox="0 0 340 236"><title>Diagramme (Z, N) de noyaux stables : calcium 40, fer 56, étain 120 et plomb 208 ; les points s'éloignent de la droite N = Z vers le haut quand Z augmente</title><line x1="46.0" y1="200.0" x2="326.0" y2="200.0" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="46.0" y1="200.0" x2="46.0" y2="16.0" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,200 324,196.5 324,203.5" fill="#0f172a"/><polygon points="46,10 42.5,18 49.5,18" fill="#0f172a"/><line x1="46.0" y1="200.0" x2="46.0" y2="204.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="46.0" y="217.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="108.2" y1="200.0" x2="108.2" y2="204.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="108.2" y="217.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="170.4" y1="200.0" x2="170.4" y2="204.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="170.4" y="217.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="232.7" y1="200.0" x2="232.7" y2="204.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="232.7" y="217.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="294.9" y1="200.0" x2="294.9" y2="204.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="294.9" y="217.0" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="42.0" y1="200.0" x2="46.0" y2="200.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="39.0" y="204.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="42.0" y1="140.7" x2="46.0" y2="140.7" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="39.0" y="144.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="42.0" y1="81.3" x2="46.0" y2="81.3" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="39.0" y="85.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="42.0" y1="22.0" x2="46.0" y2="22.0" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><text x="39.0" y="26.0" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">150</text><text x="326.0" y="229.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Z</text><text x="56.0" y="12.0" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><line x1="46.0" y1="200.0" x2="326.0" y2="93.2" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/><text x="317.8" y="85.2" text-anchor="end" font-size="12" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N = Z</text><circle cx="108.2" cy="176.3" r="3.8" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="114.2" y="194.3" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">⁴⁰Ca</text><circle cx="126.9" cy="164.4" r="3.8" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="118.9" y="156.4" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">⁵⁶Fe</text><circle cx="201.6" cy="116.9" r="3.8" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="193.6" y="108.9" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">¹²⁰Sn</text><circle cx="301.1" cy="50.5" r="3.8" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="293.1" y="46.5" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">²⁰⁸Pb</text></svg>
:::

Sur la figure, ⁴⁰Ca est sur la droite N = Z, tandis que ²⁰⁸Pb est bien au-dessus : sa hauteur N = 126 dépasse largement son abscisse Z = 82.

::: exemple Mesurer l'excès de neutrons (calcium 40, fer 56, étain 120, plomb 208)

1. ⁴⁰₂₀Ca : N = 40 − 20 = 20 = Z, le point est sur la droite N = Z, à la limite Z = 20.
2. ⁵⁶₂₆Fe : N = 56 − 26 = 30, donc N − Z = 4 : le point passe au-dessus de la droite.
3. ¹²⁰₅₀Sn : N = 70, donc N − Z = 20 et N / Z = 70 / 50 = 1,4.
4. ²⁰⁸₈₂Pb : N = 126, donc N − Z = 44 et N / Z = 126 / 82 = 1,54 : l'excès de neutrons grandit avec Z.
5. Explication : l'interaction forte n'agit que sur les voisins immédiats, alors que la répulsion électrique agit entre tous les protons du noyau ; plus Z est grand, plus il faut de neutrons, qui attirent sans repousser.

:::

::: piege
**Erreur : croire que les noyaux stables ont toujours autant de neutrons que de protons.** On attendrait N = 82 pour ²⁰⁸₈₂Pb, au lieu de N = 126 (étape 4). L'erreur tente parce que les noyaux légers, comme ⁴⁰Ca, vérifient N = Z (étape 1). Mais au-delà de Z = 20 cette égalité cesse : il faut un excès de neutrons.
:::

::: propriete
**Ce qui reste vrai** — Pour Z ≤ 20 environ, N est voisin de Z ; pour Z > 20, N > Z avec un excès croissant ; pour Z > 83, aucun noyau stable. Cas limite : un noyau de Z > 20 avec N ≤ Z n'est pas stable, quel que soit son A.
:::

::: verifie À toi : un noyau de zinc
Le noyau ⁶⁴₃₀Zn est stable. Un noyau de zinc avec 28 neutrons pourrait-il l'être ? Justifier.

---

Pour ⁶⁴₃₀Zn, N = 64 − 30 = 34 > Z = 30 : l'excès de 4 neutrons est celui qu'on attend pour Z > 20. Avec 28 neutrons, on aurait N = 28 < Z = 30 : il manquerait des neutrons pour compenser la répulsion électrique entre les 30 protons, donc ce noyau ne serait pas stable.
:::

::: retenir
Les noyaux stables légers ont N voisin de Z ; au-delà de Z = 20 il leur faut un excès de neutrons (N > Z), et aucun noyau n'est stable au-delà de Z = 83.
:::

> 🏆 Quête franchie, héros ! Tu sais écrire et lire le symbole d'un noyau, expliquer sa cohésion par l'interaction forte, calculer un défaut de masse, le convertir en énergie avec la relation d'Einstein, déterminer l'énergie de liaison d'un noyau, comparer deux noyaux par l'énergie de liaison par nucléon, lire la courbe d'Aston et situer les noyaux stables dans le diagramme (N, Z). Les réactions nucléaires t'attendent au chapitre suivant.
