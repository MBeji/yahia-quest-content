# 📜 Résumé : Probabilité sur un ensemble fini

- **Événements et probabilité** : Ω est l'univers, un événement est une partie de Ω ; p(Ω) = 1 et p(A̅) = 1 − p(A) ; p(A ∪ B) = p(A) + p(B) − p(A ∩ B), la somme simple seulement pour des événements incompatibles (A ∩ B = ∅).
- **Probabilité uniforme** : si les événements élémentaires sont équiprobables, p(A) = card A / card Ω ; on compte les couples ou les tirages équiprobables, pas des valeurs comme les sommes {2, …, 12} qui ne le sont pas.
- **Dénombrer les tirages** : avec remise nᵖ, sans remise Aₙᵖ = n(n − 1)…(n − p + 1), simultané Cₙᵖ = Aₙᵖ / p! ; favorables et possibles se comptent de la même façon, et « au moins un » passe par le contraire.
- **Probabilité conditionnelle** : p(A/B) = p(A ∩ B) / p(B) avec p(B) ≠ 0, on divise par la probabilité de ce qu'on sait ; p(A̅ / B) = 1 − p(A/B), et p(A/B) n'est pas p(B/A).
- **Événements indépendants** : A et B sont indépendants si p(A ∩ B) = p(A) × p(B), ce qui équivaut à p(A/B) = p(A) ; A̅ et B̅ le sont alors aussi, et deux événements incompatibles de probabilités non nulles ne sont jamais indépendants.
- **Probabilités composées et arbre pondéré** : p(A ∩ B) = p(A) × p(B/A) et p(A ∩ B ∩ C) = p(A) × p(B/A) × p(C/(A ∩ B)) ; sur un arbre, on multiplie le long d'un chemin et les branches d'un même nœud ont une somme égale à 1.
- **Probabilités totales** : si A₁, …, Aₙ forment une partition de Ω, p(B) = Σ p(Aₖ) × p(B/Aₖ) ; on additionne les chemins qui aboutissent à B, avec des taux pondérés par les poids et non moyennés.
- **Formule de Bayes** : p(B/A) = p(B) × p(A/B) / [p(B) × p(A/B) + p(B̅) × p(A/B̅)], soit p(B ∩ A) / p(A) avec p(A) par les probabilités totales ; elle remonte de l'effet à la cause et ne se confond pas avec p(A/B).
