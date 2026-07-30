# 📜 Résumé : Calcul dans ℝ

<svg viewBox="0 0 340 200">
  <rect x="5" y="5" width="330" height="190" rx="8" fill="#eef2ff" stroke="#0f172a" stroke-width="2"/>
  <rect x="33" y="25" width="274" height="150" rx="7" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/>
  <rect x="61" y="45" width="218" height="110" rx="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/>
  <rect x="89" y="65" width="162" height="70" rx="5" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>
  <rect x="117" y="82" width="106" height="36" rx="5" fill="#fdba74" stroke="#0f172a" stroke-width="2"/>
  <g font-size="15" font-weight="700" fill="#0f172a" text-anchor="middle">
    <text x="19" y="110">ℝ</text>
    <text x="47" y="110">ℚ</text>
    <text x="75" y="110">𝔻</text>
    <text x="103" y="110">ℤ</text>
    <text x="140" y="105">ℕ</text>
  </g>
  <g font-size="12" fill="#0f172a" text-anchor="middle">
    <text x="200" y="19">π ; √5</text>
    <text x="200" y="39">2/3 ; 1/3</text>
    <text x="200" y="59">2,5 ; 0,625</text>
    <text x="200" y="78">−4 ; −63/7</text>
    <text x="185" y="105">0 ; 1 ; 12</text>
  </g>
</svg>

- **Ensembles de nombres** : ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ. Un décimal s'écrit a/10ⁿ (5/8 = 0,625 est décimal, 1/3 ne l'est pas) ; √5 et π sont irrationnels. **ℚ ⊄ 𝔻.**
- **Proportionnalité et pourcentages** : deux grandeurs proportionnelles sont liées par un **coefficient de proportionnalité** constant (ressort : 9 mm pour 15 g, soit 9/15 = 0,6 mm par gramme, donc 30 mm pour 50 g). Appliquer t % = multiplier par 1 + t/100 (ou 1 − t/100). Prix TTC = prix HT × (1 + t/100). Les pourcentages successifs se **multiplient** : +10 % puis +20 % donne 1,10 × 1,20 = 1,32, soit +32 %.
- **Identités remarquables** : (a ± b)² = a² ± 2ab + b² ; (a − b)(a + b) = a² − b² ; (a ± b)³ = a³ ± 3a²b + 3ab² ± b³ ; a³ ∓ b³ = (a ∓ b)(a² ± ab + b²). Factoriser = facteur commun d'abord, identité ensuite.
- **Comparer / encadrer** : si 0 < a < 1 alors a² < a < √a et 1/a > 1 ; si a > 1 alors √a < a < a² et 1/a < 1. Multiplier un encadrement par un négatif **renverse** les inégalités. Inégalités clés : 2xy ≤ x² + y² (**tous** réels, c'est (x − y)² ≥ 0), x + 1/x ≥ 2 et x/y + y/x ≥ 2 (réels strictement positifs ; minimum 2 en x = 1), (a + b)/2 ≥ √(ab), et √(a + b) < √a + √b.
- **Inégalité triangulaire** : |x + y| ≤ |x| + |y| pour tous réels (égalité si x et y sont de même signe : |7 + (−3)| = 4 ≤ 10 = |7| + |−3|, mais |7 + 3| = 10). Lecture géométrique : le chemin direct est le plus court, donc **AB ≤ AC + CB** pour trois points A, B, C (égalité si C ∈ [AB]).
- **Radicaux** : rationaliser par la quantité conjuguée — 1/(3 + √2) = (3 − √2)/7 ; radical double — √(14 − 6√5) = 3 − √5 ; télescopage — 1/(√k + √(k+1)) = √(k+1) − √k. **√(x²) = |x|.** Héron : A = √(p(p − a)(p − b)(p − c)).
- **Valeur absolue** : |x| = x si x ≥ 0, −x sinon ; |√3 − 2| = 2 − √3. |A| = |B| ⇔ A = B ou A = −B. |x − a| < r ⇔ a − r < x < a + r. Distance : AB = |x_B − x_A|.
- **Approximations** : a est une valeur approchée de b à 10ⁿ près si |b − a| ≤ 10ⁿ (par défaut si a < b, par excès si a > b) ; l'arrondi est la plus proche des deux. **Écriture scientifique** a × 10ⁿ avec 1 ≤ |a| < 10 ; **ordre de grandeur** = b × 10ⁿ avec b l'arrondi de a à l'unité.
