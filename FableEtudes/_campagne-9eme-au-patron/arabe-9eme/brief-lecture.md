# Mandat — Arabe 9ᵉ, LOT A : lire À L'IMAGE une tranche du manuel élève RÉVISÉ 101908 et confronter les chapitres

Corpus `/home/user/yahia-quest-content` (moteur `/home/user/yahia-quest-arena`, lien `content`). Matière `content/arabic/` (arabe 9ᵉ, 14 chapitres, patron écrit mais jamais confronté au manuel révisé). Fiche : `content/programmes-officiels/programme/9eme-base/arabe.md` — lis §2 bis (le manuel révisé 101908, sa liste de 26 leçons, ce qui est déjà transcrit) et §6.

Source : **manuel élève 101908 (édition révisée, programme de septembre 2006)** : `/root/.cache/yqa-manuels/101908P00.pdf`, 176 p. C'est un **scan pur** : la couche texte est vide — rends chaque page en image (`pdftoppm -r 110 -f N -l N -png /root/.cache/yqa-manuels/101908P00.pdf /tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/pages/p` ; crée le dossier ; relis à 200 dpi en recadrant si un encadré est petit) et LIS-LA. Chaque leçon a quatre أركان : نصّ انطلاق → مدخل → **خلاصة** → تمارين. **Toutes les pages de ta tranche**, sans extrapoler.

## Livrables (dans `/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/lecture/`)
Une note par leçon `L<page de début>.md` : titre exact ; pages ; la **خلاصة VERBATIM et vocalisée** ; ce que le مدخل construit (les questions qu'il pose, les notions qu'il nomme et que la خلاصة ne reprend pas) ; le **métalangage exact** ; les exemples types (2–6) ; les exercices (consignes résumées, ce qu'ils exigent) ; les **bornes** (✅ enseigné / ⛔ absent mais qu'on pourrait croire au programme) ; coquilles.
Puis `ecart-<ta tranche>.md` : pour chaque leçon de ta tranche, le(s) chapitre(s) de `content/arabic/` qui la servent (lis leurs `cours.md` et un échantillon d'items), avec : servi pleinement / partiellement / pas du tout ; ce que le chapitre enseigne autrement que le manuel (métalangage, classement, règle) ; ce que le chapitre teste et que la leçon n'enseigne pas en 9ᵉ.

## Règles
Ne modifie AUCUN fichier du corpus. Aucune écriture git. « Établi » = lu sur la page (cite-la). Rapport final en français, court : pages lues (toutes ?), leçons, principaux écarts.
