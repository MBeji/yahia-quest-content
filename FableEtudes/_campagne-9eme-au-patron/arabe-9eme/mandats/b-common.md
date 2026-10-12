# Mandat commun — arabe 9ᵉ (`content/arabic/`) au patron de notion, fidèle aux manuels RÉVISÉS

Corpus `/home/user/yahia-quest-content` (moteur `/home/user/yahia-quest-arena`, lien `content` → corpus ; les contrôles se lancent DEPUIS LE MOTEUR). Élèves de 9ᵉ de base (14–15 ans), année de concours.

## Sources (R-5) — déjà lues pour toi, À L'IMAGE
- Manuel de grammaire révisé **101908 « النّحو العربي — كتاب اللّغة »** (programme de septembre 2006) : une note fidèle par leçon dans `/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/lecture/L<page>.md` (خلاصة VERBATIM, مدخل, التّطبيقات, métalangage, exemples, bornes ✅/⛔, coquilles) et quatre tableaux d'écart `ecart-1..4.md`. **Lis EN ENTIER les notes de TES leçons et la partie de l'écart qui te concerne.**
- Manuel de textes **101909 « أنوار »** (tout entier tourné vers le حجاج) : `…/ar9/lecture-n/plan.md`, `appareil.md`, `ecart-n.md` (avec ce qu'évaluent 11 sujets du concours national).
- Le PDF lui-même si une note te laisse un doute : `/root/.cache/yqa-manuels/101908P00.pdf` / `101909P00.pdf` — scans purs : `pdftoppm -r 150 -f N -l N -png <pdf> /tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/pages/p` puis LIS l'image (couche texte inutilisable).
- Fiche : `content/programmes-officiels/programme/9eme-base/arabe.md` (§2 bis : le manuel révisé ; elle contient quelques erreurs de lecture relevées par la tranche 4 — la note `L*.md` fait foi).

## Arbitrages du propriétaire (2026-10-09) — à appliquer
1. **La grammaire suit le manuel 101908** ; chaque chapitre sert ses leçons, dans son métalangage.
2. **Métalangage du manuel** dans le cours ET dans les items (ex. « حكم المنادى الرّفع », « حرف الشّرط », « عناصر الزّيادة », « الأطروحة المدحوضة », « سيرورة الحجاج ») ; le terme classique au plus UNE fois en note (« ويُسمّى في كتب النّحو … »), jamais attendu par un item.
3. **Ce que le manuel de 9ᵉ n'enseigne pas** (notions classiques du collège, taxonomies de بلاغة absentes, إعراب détaillé quand la leçon n'en parle pas…) : retiré des items ; gardé au plus dans un encadré final « 🚀 للتوسّع (خارج كتاب التّاسعة) » — reconnaissance, sans règle à apprendre, sans `piege`/`verifie`, sans item.
4. **Ne reprends aucune coquille du manuel** (elles sont listées dans les notes) ; signale-les si le cours en a hérité.

## Le patron (cours.md, EN ARABE)
Titre `# ⚔️ …` et accroche `> 💡 «…»`. Une section `## emoji عنوان` par notion (en général une par leçon, ou par règle quand la leçon en porte plusieurs), dans l'ordre : situation concrète + question (≥ 2 lignes, AVANT toute règle — souvent la situation du نصّ الانطلاق du manuel, REFORMULÉE) → `::: definition` → voir (tableau, exemples contrastés) → `::: exemple` pas à pas, chaque pas dit **لأنّ** → `::: piege الخطأ الشائع` (vraie erreur d'élève, montrée puis corrigée) → `::: propriete`/`::: methode` APRÈS l'exemple, avec un cas-limite → `::: verifie` jumeau (`---` puis réponse raisonnée) → `::: retenir`. ≤ 60 lignes de contenu par section. `resume.md` en miroir (une puce par section). Exemples : les tiens (inspirés des situations du manuel, jamais recopiés sur plusieurs lignes), vocalisés là où la حركة est l'enjeu ; vers classiques du domaine public autorisés, textes d'auteurs modernes du manuel NON recopiés. Référentiels : `.claude/skills/content-cours/SKILL.md`, `.claude/skills/content-engine/references/course-explanation.md` (LE PATRON), `course-quality.md`, `language-track.md`, `quality-bar.md`, `math-and-notation.md` (chiffres occidentaux), `correction-cle-longue.md`. Maquette en arabe : `content/arabic/13-at-tasghir/` (déjà au patron et fidèle au manuel).

## Items
`mcq`, 4 options, UNE seule juste (vérifie qu'aucun distracteur n'est défendable : vocalisation ambiguë, deux analyses possibles, variante admise par le manuel), distracteurs = erreurs réelles, explication qui dit pourquoi la bonne est bonne ET pourquoi l'erreur tentante est fausse ; clé jamais strictement l'option la plus longue ; clés réparties a/b/c/d ; pas de renvoi positionnel (« (أ) ») ; pas de `**` dans prompt/explication ; chaque notion testée enseignée dans CE cours ; métalangage du manuel. Pas de `misconceptionTag` ni de `coursePitfalls` (étape suivante).

## chapter.json
`sources` : le manuel en PREMIER (« النّحو العربي — كتاب اللّغة، السّنة التّاسعة من التّعليم الأساسي (المركز الوطني البيداغوجي) — 101908 — الدّرس N «…»، ص a–b »), puis 101909 s'il sert, puis les sources existantes utiles ; `"manuel": {"code": "101908", "pages": "a-b, c-d"}` (ou 101909 pour 07–10). `title`/`description` qui disent le contenu ; `displayOrder` donné par ton brief ; **ne change jamais un slug**.

## Contrôles (depuis `/home/user/yahia-quest-arena`)
`npm run -s content:check` ; `npm run -s content:qa 2>&1 | grep "arabic/<ton NN>-"` → ZÉRO erreur, ZÉRO avertissement é35 ; `npm run -s content:tranche -- --subject arabic --chapters <NN>` → clé strictement la plus longue ≤ 1 ; `npx prettier --ignore-path /dev/null --write` puis `--check` sur ton dossier (config du moteur). D'autres agents travaillent en parallèle : ne touche qu'à TES dossiers ; si `content:check` bute sur un dossier voisin inachevé, dis-le et contrôle le tien. **Ne touche jamais `11-annales-subur`** (confié à l'étude 36). Aucune écriture git.

## Limite d'usage
Le quota est partagé : **écris tes fichiers au fil de l'eau** (cours d'abord, puis chaque fichier d'items dès qu'il est prêt), pour qu'une coupure ne fasse rien perdre.

## Rapport final (court, en français)
Leçons → sections ; ajouté / retiré (et où va le hors-manuel) ; items écrits ou réécrits par fichier ; contrôles ; doutes.
