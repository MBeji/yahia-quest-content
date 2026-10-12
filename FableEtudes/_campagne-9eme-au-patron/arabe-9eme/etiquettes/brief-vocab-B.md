# Mandat — phase 1 des tags (niveau 3) : le VOCABULAIRE D'ERREURS de l'arabe 9ᵉ

Tu ne modifies AUCUN fichier du corpus. Tu produis une proposition de registre, que l'orchestrateur fusionnera dans `content/misconceptions.json`.

## Contexte (à lire)
- Règle de décision et format : `/home/user/wt-arabe/.claude/skills/content-engine/references/content-schema.md` §« Optional `misconceptionTag` per distractor » et « La règle de décision — tagger ou laisser muet » (portes R1/R2/R3, seuil ≥ 3 questions distinctes, une phrase adressée à l'élève, 100 % n'est pas la cible). Et `course-explanation.md` (R-5 / C-5 : chaque `::: piege` du cours nomme une erreur, déclarée dans `chapter.json → coursePitfalls` et portée par au moins un distracteur du chapitre).
- Registre réel : `content/misconceptions.json` — il contient déjà **122 ids `arabe.*`** (écrits pour l'arabe 6ᵉ : `arabe.fi3l.*`, `arabe.maqsur.*`, `arabe.hamza.*`, `arabe.nawasikh.*`, `arabe.i3rab.*`, `arabe.jumla.*`…). **RÉUTILISE un id existant chaque fois que son libellé dit exactement l'erreur** ; n'en crée un neuf que pour une erreur qu'aucun ne dit. Modèle de `coursePitfalls` : `content/arabic-6eme/*/chapter.json`.

## Ta matière — PARTIE B (12, 05, 13, 14, 09, 10, 07, 08 : le صرف, le حجاج, la rhétorique ; PLUS 01, 06, 11)
arabe 9ᵉ, matière `arabic` (`content/arabic/`). **Tu traites ces 8 chapitres, PLUS `01-i3rab-wal-bina`, `06-al-mushtaqqat` et `11-annales-subur` (ajout du 2026-10-12 : l'armement `coursePattern: "notion"` exige des `coursePitfalls` sur les 19 chapitres ; 01 et 06 sont des révisions hors livre, 11 les annales — pour eux, réutilise d'abord les ids des parties A et B)** : `12-al-maqsur-wal-manqus-wal-mamdud`, `05-sarf-al-mizan`, `13-at-tasghir`, `14-an-nisba-wal-masdar-as-sinai` (manuel de grammaire 101908, notes `/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/lecture-101908/L*.md`), `09-al-intaj-al-kitabi`, `10-fahm-wa-intaj`, `07-as-suwar-al-bayania`, `08-al-muhassinat-al-badi3ia` (manuel de textes 101909, notes `…/arabe-9eme/lecture-101909/`). Un premier agent a déjà établi le vocabulaire des 8 chapitres de grammaire : **lis d'abord `…/arabe-9eme/etiquettes/vocab-arabe9-A.json` et `…/arabe-9eme/etiquettes/map-arabe9-A.md` et RÉUTILISE ces ids** chaque fois que l'erreur est la même ; n'ajoute que des ids neufs, jamais un doublon de sens. **Ordre** : traite `07` et `08` EN DERNIER et relis-les à ce moment-là (un auditeur les corrige en parallèle ; ne les modifie pas).

## Travail
1. Lis TOUS les `cours.md` de tes 8 chapitres (surtout les blocs `::: piege`) et TOUS leurs items (`quiz.json`, `exercices/*.json` : options fausses + explications).
2. Établis le vocabulaire fermé des erreurs RÉCURRENTES :
   - chaque `piege` d'un cours doit avoir son id (c'est C-5) — sauf s'il est vraiment isolé et qu'aucun distracteur ne le porte (dis-le) ;
   - ajoute les erreurs qui reviennent dans ≥ 3 questions distinctes comme distracteur reconstructible ;
   - une erreur = UNE phrase adressée à l'élève, à la 2ᵉ personne (« تظنّ… », « تقرأ… », « تخلط… »), précise, jamais vague ; elle nomme l'erreur ET la règle juste, dans le **métalangage du manuel** (« حكم المنادى الرّفع », « حرف الشّرط », « عناصر الزّيادة », « الأطروحة المدحوضة », « سيرورة الحجاج »…).
3. Ids : `arabe.<domaine>.<erreur-en-kebab>` (minuscules ASCII, chiffres, tirets ; translittération simple comme les ids existants), stables et parlants. Domaines suggérés pour les notions neuves : `rabt` (أدوات الرّبط, العلاقات بين الجمل), `hadhf`, `nida`, `talab` (دعاء, أمر, نهي), `istifham`, `shart`, `zaman` (صيغ الفعل, الحروف المقترنة, المفعول فيه, الحال), `adad`, `mazid`, `tasghir`, `nisba`, `hijaj`, `sura` (تشبيه, استعارة, حقيقة / مجاز), `badi3` (طباق, سجع) — réutilise `nawasikh`, `maqsur`, `hamza`… quand ils existent. Pas de doublon de sens entre deux ids (ni avec un id existant).
4. Pour chaque id NEUF : `subject` = `"arabe"`, `labels` { `ar`, `fr`, `en` } — la même phrase dans les trois langues, courte (≤ 160 caractères chacune), l'arabe vocalisé là où la حركة est l'enjeu ; pas de `competency`.

## Livrables
- `/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/vocab-arabe9-B.json` : un objet JSON `{ "<id>": { "subject": "arabe", "labels": { "ar": "…", "fr": "…", "en": "…" } }, … }` des SEULS ids neufs (JSON valide, 2 espaces).
- `/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/map-arabe9-B.md` : pour chaque id utilisé (neuf OU réutilisé) — les chapitres et le `piege` qui l'énonce (s'il y en a un), et 2 à 5 exemples de distracteurs qui le portent (fichier#question → option) ; des règles de précédence quand deux ids se touchent ; une section « pièges sans id » (avec la raison) et « erreurs vues < 3 fois » (non retenues) ; et un tableau « coursePitfalls proposés par chapitre » (ids + colonne C-5 : porté par un distracteur du chapitre ? ✓ / ✗). Signale tout chapitre sans candidat — et pour CHACUN des 11 chapitres, propose au moins un `coursePitfalls` dont l'id est porté par un distracteur du chapitre (sinon dis précisément pourquoi c'est impossible).

Écris tes deux fichiers AU FIL DE L'EAU (chapitre après chapitre) : le quota est partagé, une coupure ne doit rien perdre.

## Rapport (court, en français)
Nombre d'ids neufs et réutilisés ; couverture attendue (combien de `piege` ont un id ; estimation grossière du nombre de distracteurs taguables) ; doutes. Ignore les notions des encadrés « 🚀 للتوسّع » (elles n'ont pas d'item).
