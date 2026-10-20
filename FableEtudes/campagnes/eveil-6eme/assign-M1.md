# Carte d’affectation M1 — éveil scientifique 6ᵉ, chapitres `09`, `12`, `01` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 12 missions (10 d’examen, 2 de devoir), 115 questions ; 2 auteurs : `09` + `12` d’un côté, `01` de l’autre (en parallèle, chapitres disjoints). Skills : `content-ecole-tn`, puis `prof-eveil-primaire` (calibre les étages, jamais plus que le programme de 6ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/eveil/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend un support (ou une situation) et ses consignes, découpés en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne la phrase OFFICIELLE de la transcription qu'elle lit (consigne et énoncé tels qu'imprimés, coquilles incluses sauf celles que la carte nomme) ; une consigne ouverte (« أفسّر », « أعلّل », « أصلح كلّ خطأ », « أقترح تجربة ») devient un QCM de l'explication ou de la correction, un `ordering` (étapes d'un protocole, trajet), un `matching` (légende ↔ nom, tableau) ou un `multi` (relevés, vrai/faux motivés) ; `short_answer` seulement pour UN terme du معجم avec ses `acceptedAnswers` ; aucun tracé n'est demandé à la main : un tracé de rayon, de flèche ou d'aiguille devient « quel dessin est exact ? » (QCM visuel) ; figures, schémas d'expériences et tableaux refaits en SVG, vrais, SANS donner la clé ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Chiffres du ملفّ du guide (78 %, 21 %, 2 : 1, 55 %, 1/6, 5 millions…) : enrichissement seulement, JAMAIS une clé ni un distracteur (V1) ; les quatre valeurs permises sont 1/5 d'oxygène, 1 L d'air ≈ 1,3 g, eau = 2/3 du corps, 120 jours (fiche §4 bis, point 4). Sont enseignés, donc exerçables : les plaquettes (V2 révisé), les huit directions (V5) ; l'« intensité » du courant n'est pas exigible (V3) ; la potabilisation est une lecture de schéma sans clé de mémorisation (V4). Chaque DÉFAUT d'énoncé que la carte nomme est corrigé dans la reprise, comme la carte le dit, et l'explication le signale. Étiquettes : `misconceptionTag` du registre `eveil.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/eveil/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-eveil/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject eveil-scientifique-6eme` (0 erreur), `content:tranche -- --subject eveil-scientifique-6eme --changed --fresh --strict-longest`.

**🔁 À REVÉRIFIER AU LANCEMENT (E-12).** Les 12 chapitres d'éveil seront mis à niveau sur la fiche programme APRÈS ce plan (cours au patron, exercices, étiquettes). Tous les « Ne pas redemander » de cette carte sont établis sur les exercices TELS QU'ILS SONT AU 2026-10-20 (état du 28 septembre : 5 fichiers de 6 questions à choix + un quiz de 5 questions par chapitre, tous des QCM) : ils sont PROVISOIRES. Au lancement de chaque mission, relis les exercices et le cours du chapitre tel qu'il sera alors, refais le croisement question par question, et mets la liste à jour avant d'écrire. Les numéros de fichiers (`06`, `07`, …) supposent que les chapitres ont `01`–`05` : si la mise à niveau ajoute un fichier, décale. Si un item que la carte cible (plaquettes, huit directions, sang décanté, sonnerie, monoxyde de carbone…) n'est pas enseigné par le chapitre mis à niveau, arrête-toi et signale-le : la mission ne part pas avant le cours.

**Ordre de travail** : (1) les ids d’étiquette neufs que tu poses ; (2) les missions du chapitre, dans l’ordre de la carte ; (3) les gates. **Départ du lot** : seulement quand ses chapitres ont été mis à niveau sur la fiche (E-11).


## Chapitre `09-oeil-vision` — العين: تركيبتها والرّؤية وعيوبها

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.vision.organes-protecteurs-inutiles` (Tu crois que les sourcils et les cils ne servent qu'à décore) | `eveil.vision.pupille-et-iris-confondues` (Tu confonds la pupille et l'iris : la pupille est le trou no) | `eveil.vision.cristallin-et-vitre-confondus` (Tu confonds le cristallin et l'humeur vitrée : le cristallin) | `eveil.vision.lentilles-inversees` (Tu inverses les deux lentilles : la convexe (comme le crista) | `eveil.lum.oeil-emet-la-lumiere` (Tu crois que l'œil envoie de la lumière vers les objets : la) | `eveil.vision.myopie-et-hypermetropie-inversees` (Tu inverses myopie et hypermétropie : le myope voit bien de ) | `eveil.vision.linge-d-autrui-sans-risque` (Tu crois qu'utiliser la serviette ou le mouchoir d'un autre )

### m001 → `exercices/06-exams-2008-2013-schemas-de-loeil-defaut-lentille-legendes.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2013 ⭐⭐⭐: … ») : Concours 2008 · 2012 · 2013 · des schémas d'œil : le défaut, la lentille, les légendes
- Registre : id `C14#2a` ; sources `C14#2a, C14#2b, C15#2a, C19#2a`
- Sources : C14 (session 2013), support 2, consignes 1 et 2 ; C15 (session 2012), support 2 ; C19 (session 2008), support 2 — transcriptions `2013-unique.md`, `2012-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2013 · ألاحظ الرسم وأتمّم بما يناسب (« هذه عينٌ مصابة بـ ........ » sous chacun des deux schémas ① et ②)
  - 2013 · أكمل وأفسّر : يتمّ تعديل الرؤية في الحالة (1) بعدسة ........ لأنّ ........ / يتمّ تعديل الرؤية في الحالة (2) بعدسة ........ لأنّ ........
  - 2012 · أُصلحُ الخطأ على الرسم 2 إنْ وُجِدَ (le schéma ① est titré « عين الممرّض بعد التعديل »)
  - 2008 · أتمّم الرّسم التّالي بكتابة اسم كلّ جزء ووظيفته.
- Étapes prévues :
  - 2013 (support 2, consigne 1) : deux schémas d'œil où les rayons se croisent devant ou derrière la rétine ; dire le défaut de chaque œil d'après le lieu de l'image (derrière la rétine = hypermétropie ; devant = myopie), figures refaites en SVG — QCM par schéma — 2 q
  - 2013 (consigne 2) : la lentille qui corrige chaque cas (convergente/محدّبة pour l'image derrière, divergente/مقعّرة pour l'image devant) et la raison (elle rapproche ou éloigne le point de convergence) — QCM de la lentille, QCM de la justification — 2 q
  - 2012 (support 2) : un adulte éloigne la poche qu'il veut lire (hypermétropie) ; choisir le schéma corrigé (lentille convergente devant l'œil, rayons qui convergent sur la rétine) parmi trois — QCM visuel, puis QCM du rôle de la lentille — 2 q
  - 2008 (support 2) : trois parties de l'œil désignées par des traits de repère (cornée, pupille/iris, cristallin, rétine… au choix de l'auteur, parmi celles du manuel) ; relier le nom et la fonction — matching nom ↔ fonction, puis QCM sur un nom et QCM sur une fonction — 3 q
- Pièges (étiquette à porter par un distracteur) :
  - inverser image devant et derrière la rétine — ligne C14#2a (d2)
  - inverser verre convergent et divergent — ligne C14#2b (d2)
  - dessiner l'image du mauvais côté de la rétine — ligne C15#2a (d3)
  - confondre rôle de la cornée et rôle de la rétine — ligne C19#2a (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `09/03-revision#5`, `09/03-revision#6`, `09/02-boss#6`, `09/04-defi#5`, `09/05-entrainement#6`, `09/01-pratique#6`, `09/03-revision#2`, `09/quiz#3`, `09/quiz#5`
- Note : Hypermétropie = image derrière la rétine, lentille CONVERGENTE ; myopie = image devant, lentille DIVERGENTE (le patron l'enseigne ainsi ; l'erreur du manuel p.23 n'est pas reprise). Pour la poche éloignée de 2012, ne pas écrire « presbytie » (◐ de la fiche) : l'élève de 6ᵉ dit « il voit mal de près ». Les schémas du sujet 2013 ont des « lignes croisées » : l'auteur refait des figures vraies et sans clé. Sessions : 2013, 2012, 2008.

### m002 → `exercices/07-exams-2015-2018-hypermetropie-lentille-pupille.json` · d3 boss 120/30 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2015–2018 ⭐⭐⭐: … ») : Concours 2015 · 2018 · l'hypermétropie du grand-père, la lentille, la pupille
- Registre : id `C09#6` ; sources `C09#6, C09#7, C09#8, C12#6a, C12#6b`
- Sources : C09 (session 2018), support 3, consignes 1 à 3 ; C12 (session 2015), support 6, consignes 1 et 2 — transcriptions `2018-unique.md`, `2015-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2018 · فسّر عيب الرّؤية الّذي يشتكي منه الجدّ بالاستناد إلى خصائص الأوساط الشّفّافة ومسارات الضّوء. (support : le grand-père reconnaît un renard de très loin mais ne lit pas le nom de l'appelant, à cause de sa « طول النّظر »)
  - 2018 · جسّد هذه الظاهرة على الرسم التالي. (coupe d'œil : قرنيّة، عدسة، شبكيّة، عصب بصريّ ; une flèche pour l'objet)
  - 2018 · سمّ العدسة الملائمة لإصلاح عيب الرّؤية وارسمها.
  - 2015 · أعلّل هذا الاستعمال (l'aïeul lit l'ordonnance avec des lunettes à deux verres concaves)
  - 2015 · أفسّر الاختلاف بين الصورتين 1 و 2 اللتين تمثّلان عيني نور في ظرفين مختلفين.
- Étapes prévues :
  - 2018 (consigne 1) : « طول النّظر » = hypermétropie ; l'explication par les milieux transparents et le trajet de la lumière (l'image se forme derrière la rétine) — QCM du défaut, QCM de l'explication, QCM du lieu de l'image — 3 q
  - 2018 (consigne 2) : tracer le trajet de la lumière dans l'œil hypermétrope — QCM visuel (quatre coupes d'œil en SVG, une seule juste) — 2 q
  - 2018 (consigne 3) : nom de la lentille et sa coupe — QCM du nom (convergente/محدّبة), QCM visuel de la coupe. DÉFAUT DU SUJET : la clé attendue par le sujet 2018 suit l'erreur du manuel p.23 (lentille concave pour l'hypermétropie) ; la mission retient la science juste (convergente) et le dit dans l'explication — 2 q
  - 2015 (consigne 2) : deux photos de pupille (grande, petite) ; la pupille se dilate à la faible lumière et se resserre à la forte lumière — QCM de la cause, QCM de la conséquence (quantité de lumière qui entre) — 2 q
  - 2015 (consigne 1) : lunettes à verres concaves : le défaut corrigé est la myopie — 1 QCM. DÉFAUT DU SUJET : le texte fait lire l'ordonnance avec ces verres ; un myope n'en a pas besoin pour lire de près. La question est reformulée : « de quel défaut corrige-t-on avec des verres concaves ? », sans le mot « lire » — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - placer l'image sur la rétine — ligne C09#6 (d3)
  - faire converger les rayons sur la rétine — ligne C09#7 (d3)
  - confondre lentille convergente et divergente — ligne C09#8 (d2)
  - confondre verre convergent et verre divergent — ligne C12#6a (d2)
  - relier la taille de la pupille à la distance et non à la lumière — ligne C12#6b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `09/03-revision#5`, `09/03-revision#6`, `09/02-boss#6`, `09/04-defi#5`, `09/04-defi#6`, `09/05-entrainement#5`, `09/05-entrainement#6`, `09/quiz#2`, `09/quiz#5`
- Note : Deux défauts du sujet à corriger (E-5) : la lentille de l'hypermétropie (2018) et la lecture avec des verres concaves (2015). L'ordre des questions suit le sujet. Le grand-père « reconnaît un renard de loin et ne lit pas de près » : c'est bien l'hypermétropie du manuel (lecture de près difficile).


## Chapitre `12-dhaw` — الضّوء: انتثارُه وانعكاسُه وانكسارُه

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.lum.oeil-emet-la-lumiere` (Tu crois que l'œil envoie de la lumière vers les objets : la) | `eveil.lum.objet-eclaire-pris-pour-source` (Tu prends pour une source de lumière un objet qui ne fait qu) | `eveil.lum.ombre-expliquee-par-la-distance` (Tu expliques l'ombre par la distance ou la taille de la pièc) | `eveil.lum.transparent-et-translucide-confondus` (Tu confonds transparent et translucide : le transparent lais) | `eveil.lum.phenomenes-lumineux-confondus` (Tu confonds réflexion (surface polie, une direction), diffus) | `eveil.lum.objet-croit-deforme-par-l-eau` (Tu crois que l'objet lui-même change dans l'eau (bâton cassé) | `eveil.lum.reflexion-par-opacite` (Tu crois que le miroir réfléchit parce qu'il est transparent)

### m003 → `exercices/06-exams-2016-2017-refraction-definition-et-rayons.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2016–2017 ⭐⭐⭐: … ») : Concours 2016 · 2017 · la réfraction : la définition, le poisson, les rayons
- Registre : id `C10#4c` ; sources `C10#4c, C10#4d, C11#4a, C11#4b`
- Sources : C10 (session 2017), support 4, consignes 3 et 4 ; C11 (session 2016), support 4, consignes 1 et 2 — transcriptions `2017-unique.md`, `2016-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2017 · أصلح الكلمات المسطّرة في النصّ لأحصل على استنتاج في علاقة بالظّاهرة المقترحة. (« __انعكاس__ الضّوء هو __انتشار__ في مسار الأشعّة الضّوئيّة المارّة من وسط شفّاف إلى وسط شفّاف آخر يختلف عنه من حيث __الكتلة__ »)
  - 2017 · أرسم الشّعاع المنكسر أو الوارد في كلّ وضعيّة من الوضعيّات التّالية : (trois situations ; la 3 comporte une couche d'eau entre deux couches d'air)
  - 2016 · تسرّب خطأ عند رسم السمكة في موقعها الحقيقي، أصلحه فوق الرّسم.
  - 2016 · أتخيّر ممّا يلي الإفادة التي اعتمدتها في إصلاح الخطأ.
- Étapes prévues :
  - 2017 (consigne 3) : corriger les trois mots soulignés (انكسار ; تغيّر/انحراف ; الشفافية) — un QCM par mot, chaque leurre est le mot voisin du cours (انعكاس, انتثار, اللون) — 3 q — 3 q
  - 2017 (consigne 4) : trois situations air/eau ; choisir le tracé exact du rayon manquant (se rapproche de la normale en entrant dans l'eau, s'en écarte en sortant ; la lame d'eau entre deux couches d'air : le rayon revient parallèle à sa direction d'entrée) — trois QCM visuels (figures SVG vraies) — 3 q
  - 2016 (consigne 1) : position vraie et position apparente du poisson : choisir la figure corrigée — QCM visuel, puis QCM « pourquoi le poisson paraît plus proche de la surface » — 2 q
  - 2016 (consigne 2) : choisir l'énoncé qui justifie la correction. DÉFAUT DU SUJET : les deux propositions imprimées disent « de l'air vers l'eau », alors que la lumière du poisson va de l'eau vers l'air ; la mission écrit « عند مروره من الماء إلى الهواء فيبتعد عن الناظم » contre « فيقترب من الناظم » — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - échanger réflexion et réfraction — ligne C10#4c (d2)
  - tracer le rayon sans le dévier ou du mauvais côté de la normale — ligne C10#4d (d3)
  - tracer le rayon sans tenir compte de la déviation à la surface — ligne C11#4a (d3)
  - confondre le sens air-eau et eau-air — ligne C11#4b (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `12/quiz#3`, `12/03-revision#3`, `12/02-boss#4`, `12/04-defi#1`, `12/04-defi#4`, `12/05-entrainement#4`, `12/05-entrainement#5`
- Note : Le 4d (2017) est la ligne la plus dure du chapitre (d3). Les rayons sont qualitatifs : jamais d'angle mesuré, ni de loi chiffrée (⛔ Descartes). Le mot « الكتلة » du sujet 2017 est une erreur voulue à corriger en « الشفافية ». Placer la normale en pointillés sur chaque figure.

### m004 → `exercices/07-exams-2008-2012-reflexion-miroir-rayons-et-definitions.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2012 ⭐⭐⭐: … ») : Concours 2008 · 2009 · 2012 · la réflexion sur un miroir : tracés et définitions
- Registre : id `C15#5a` ; sources `C15#5a, C15#5b, C18#5a, C19#6a`
- Sources : C15 (session 2012), support 5, consignes 1 et 2 ; C18 (session 2009), support 5 ; C19 (session 2008), support 6 — transcriptions `2012-unique.md`, `2009-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2012 · أَرْسُمُ الشعاع الناقص في كلّ حالة : (a : rayon incident oblique ; b : rayon incident confondu avec la normale ; c : rayon réfléchi donné, incident à tracer)
  - 2012 · أُصلحُ العبارة المسطّرة عند الاقتضاء : « __الانعكاس__ : هو تغيّر في مسار الضوء عند انتقاله من وسط شفّاف إلى وسط آخر مختلف من حيث الشفافيّة. / __الانكسار__ : يَنْتُجُ عن اصطدام الضوء بجسم عاتم. »
  - 2009 · أتأمّل الرّسمين وأشطب الخطأ في كلّ منهما وأقوم بالإصلاح. (miroir plan ; surface d'eau)
  - 2008 · أتمّم رسم الشّعاع الضّوئي في كلّ وضعيّة وأُكتب اسم الظّاهرة النّاتجة عن انحراف الضّوء. (miroir poli ; eau)
- Étapes prévues :
  - 2012 (consigne 1) : trois cas de miroir plan ; choisir le rayon manquant (le rayon réfléchi repart de l'autre côté de la normale ; le rayon qui arrive sur la normale revient sur lui-même ; pour le cas c, retrouver l'incident) — trois QCM visuels — 3 q
  - 2012 (consigne 2) : les deux définitions soulignées sont échangées ; dire laquelle va à la réflexion et laquelle à la réfraction — deux QCM — 2 q
  - 2009 (support 5) : deux schémas à erreur de tracé (le rayon réfléchi tracé sur la normale ; l'autre du mauvais côté) ; repérer l'erreur, choisir le schéma corrigé — QCM de l'erreur, QCM visuel — 2 q
  - 2008 (support 6) : miroir poli → réflexion ; eau → réfraction : nommer le phénomène de chaque situation et choisir le tracé — QCM visuel, matching situation ↔ phénomène — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - ne pas respecter le retour du rayon perpendiculaire sur lui-même — ligne C15#5a (d2)
  - échanger réflexion et réfraction — ligne C15#5b (d2)
  - ne pas respecter l'égalité des angles de réflexion — ligne C18#5a (d3)
  - confondre réflexion et réfraction — ligne C19#6a (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `12/quiz#2`, `12/quiz#3`, `12/01-pratique#6`, `12/02-boss#2`, `12/02-boss#3`, `12/02-boss#6`, `12/04-defi#1`, `12/04-defi#2`, `12/04-defi#5`
- Note : ◐ de la fiche : l'égalité des angles d'incidence et de réflexion n'est enseignée que qualitativement (⛔ lois chiffrées). Aucune question ne mesure un angle ; les options de tracé ne se distinguent que par le côté de la normale et le retour du rayon perpendiculaire (voir E-9). 2009 : l'énoncé dit « deux schémas », l'un sur miroir plan, l'autre sur l'eau.


## Chapitre `01-air` — الهواء والاحتراق

**Étiquettes déjà en usage dans ce chapitre** (état du 2026-10-20, à rafraîchir après la mise à niveau) : `eveil.air.vivant-aquatique-sans-air` (Tu crois qu'un être vivant qui vit dans l'eau ou sous la ter) | `eveil.gaz.test-mal-associe` (Tu associes un gaz au mauvais test : l'eau de chaux se troub) | `eveil.air.dilatation-contraction-inversees` (Tu inverses les effets de la température : l'air chauffé se ) | `eveil.air.azote-entretient-combustion` (Tu crois que l'azote (nitrogène) joue un rôle dans la combus) | `eveil.air.reactifs-et-produits-inverses` (Tu confonds ce qui entre dans la combustion (matière, oxygèn) | `eveil.air.air-confondu-avec-oxygene` (Tu confonds l'air et l'oxygène : l'oxygène n'est qu'un cinqu) | `eveil.air.meche-ou-cire-solide-brule` (Tu crois que c'est la mèche, ou la cire solide ou liquide, q)

### m005 → `exercices/06-exam-2025-deux-bocaux-bougie-et-glace.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2025 ⭐⭐⭐: … ») : Concours 2025 · situation 1 · les deux bocaux : une bougie, de la glace
- Registre : id `C02#1` ; sources `C02#1, C02#2, C02#3, C02#4`
- Sources : C02 (session 2025), situation 1 entière — transcriptions `2025-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - كمّل الجدول بكتابة العبارة المناسبة (أكبر من ، أصغر من، تساوي) للمقارنة بين نسب الغازات في الإناءين. (نسبة غاز الأكسيجين / النتروجين / ثاني أكسيد الكربون في الإناء 1 ........ نسبة ... في الإناء 2)
  - فسّر سبب صعود الماء الملوّن في الأنبوب 2 .
  - بيّن أنّ كمّيّة الماء بالإناء 1 بعد انطفاء الشمعة، تقدّر بحوالي 20 صل. (bocaux de 100 صل)
  - أصلح الخطأ في الإفادة التّالية. (ساهم احتراق الشمعة في ظهور مكوّنين إضافيّين في الإناء 1: هما بخار الماء وهباب الفحم.)
- Étapes prévues :
  - consigne 1 : comparer O₂, N₂ et CO₂ entre le bocal à la bougie et le bocal refroidi — matching trois lignes ↔ {أكبر من, أصغر من, تساوي}, puis QCM « pourquoi la part d'azote ne change pas » — 2 q
  - consigne 2-أ : le bocal 2 est plongé dans l'eau glacée, l'air se refroidit et se contracte, l'eau colorée monte dans le tube — QCM de la cause (contraction), QCM du leurre « l'oxygène a été consommé » — 2 q
  - consigne 2-ب : volume d'eau monté dans le tube 1 ≈ 20 صل — numeric (20), puis QCM de la justification. DÉFAUT DU MANUEL repris par le sujet : voir E-4 ; l'énoncé demande « environ » et rappelle que l'oxygène fait environ un cinquième du volume de l'air ; il ne dit jamais que la bougie a consommé tout l'oxygène — 2 q
  - consigne 3 : l'erreur de l'énoncé (la suie) et la bonne paire (بخار الماء et ثاني أكسيد الكربون) — QCM de l'erreur, QCM de la correction — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - croire que la combustion change la part d'azote — ligne C02#1 (d2)
  - invoquer la consommation d'oxygène au lieu de la contraction du gaz refroidi — ligne C02#2 (d2)
  - oublier la fraction d'oxygène dans l'air — ligne C02#3 (d3)
  - citer la suie au lieu du dioxyde de carbone — ligne C02#4 (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/03-revision#2`, `01/04-defi#3`, `01/02-boss#5`, `01/quiz#3`, `01/quiz#4`, `01/quiz#5`
- Note : Les données du sujet sont gardées (deux bocaux de 100 صل, tube 1 et tube 2, eau colorée). Le bocal 2 ne contient pas de bougie : sa composition ne change pas, c'est le piège de la consigne 1. Le chiffre « 20 صل » est la lecture du sujet ; il suppose l'approximation de classe du cinquième (E-4).

### m006 → `exercices/07-exams-2019-2021-refroidir-chauffer-peser-lair.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2019–2021 ⭐⭐⭐: … ») : Concours 2019 · 2020 · 2021 · refroidir, chauffer et peser l'air
- Registre : id `C06#9` ; sources `C06#9, C06#10, C06#11, C07#6, C08#10`
- Sources : C06 (session 2021), situation intégrative, support 1, consignes 2-أ, 2-ب et 3 ; C07 (session 2020), situation 2, consigne 3 ; C08 (session 2019), situation intégrative, support 2, consigne 1-أ — transcriptions `2021-unique.md`, `2020-unique.md`, `2019-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2021 · أتأمّل التّجربة وأفسّر سبب صعود الماء الملوّن في الأنبوب بعد إضافة الماء والثّلج إلى الإناء البلّوري وفق ما هو مبيّن بالرّسم التّالي.
  - 2021 · أفسّر ما يحدث لو أعدنا التّجربة السّابقة ووضعنا في الإناء البلّوري ماء ساخنا بدل الماء والثّلج.
  - 2021 · أفسّر التّمشّي الّذي اعتمدته ندى في تحديد كتلة 1 ل من الهواء انطلاقا من التّجربة التّالية. (356,6 غ avant ; 354 غ après ; bouteille de 2 ل)
  - 2020 · أتأمّل الوثيقة التّالية وأعلّل أنّ الغاز الّذي تحويه الكرة ليس الهواء. (615,3 غ ; سحب 1 ل من الغاز ; 613,5 غ)
  - 2019 · أعلّل سبب خروج فقاقيع الهواء بذكر خاصّيّة الهواء المبيّنة بالتّجربة التّالية. (دورق، إناء بلّوري، ماء، موقد غازيّ)
- Étapes prévues :
  - 2021 (2-أ) : le montage refroidi : contraction de l'air, l'eau colorée monte dans le tube — QCM de la cause, QCM du leurre « aspiration » — 2 q
  - 2021 (2-ب) : l'eau chaude à la place de la glace : l'air se dilate, des bulles sortent par le tube — QCM de la prévision — 1 q
  - 2021 (3) : pesée de 1 ل d'air : 356,6 − 354 = 2,6 غ pour 2 ل, donc 1,3 غ pour 1 ل — ordering des temps du protocole, numeric de la perte de masse (2,6), numeric de la masse de 1 ل (1,3) — 3 q
  - 2020 (3) : le ballon perd 1,8 غ pour 1 ل de gaz (615,3 − 613,5) ; la valeur de référence de l'air est 1,3 غ par litre ; donc le gaz n'est pas de l'air — numeric (1,8), QCM de la comparaison et de la conclusion — 2 q
  - 2019 (1-أ) : les bulles qui sortent du flacon chauffé : l'air chauffé se dilate — QCM de la propriété (dilatation, pas compression) — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - invoquer l'aspiration au lieu de la contraction du gaz — ligne C06#9 (d2)
  - prédire la même montée qu'au refroidissement — ligne C06#10 (d2)
  - oublier de diviser la perte de masse par le volume — ligne C06#11 (d3)
  - oublier la valeur de référence de l'air — ligne C07#6 (d3)
  - invoquer la compression au lieu de la dilatation — ligne C08#10 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/01-pratique#3`, `01/01-pratique#5`, `01/03-revision#4`, `01/04-defi#2`, `01/04-defi#3`
- Note : Le « 1,3 g par litre » est une des quatre valeurs chiffrées du manuel (fiche §4 bis, point 4) : c'est une clé permise. Données gardées telles qu'imprimées (356,6 ; 354 ; 615,3 ; 613,5). Placement au `01` pour les trois sessions. Le ballon (2020) est le même geste que la bouteille de 2021 : deux angles (perte de masse d'un volume connu / comparaison avec la référence).

### m007 → `exercices/08-exams-2020-2024-bougie-sous-le-tube-un-cinquieme-doxygene.json` · d3 boss 120/30 · 11 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2020–2024 ⭐⭐⭐: … ») : Concours 2020 · 2023 · 2024 · la bougie sous le tube : un cinquième d'oxygène
- Registre : id `C03#7` ; sources `C03#7, C03#8, C04#16, C04#17, C07#7, C07#8, C07#9`
- Sources : C03 (session 2024), situation 2, expérience 2, consignes 3-أ et 3-ب ; C04 (session 2023), situation intégrative, support 4 ; C07 (session 2020), situation intégrative, consignes 1 à 3 — transcriptions `2024-unique.md`, `2023-unique.md`, `2020-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2024 · تأمّل الرّسم وضع العلامة (x) أمام الإجابة المناسبة : تنطفئ الشمعة عندما يرتفع مستوى سطح الماء داخل الأنبوب إلى : (التّدريجة-1 … التّدريجة-4)
  - 2024 · علّل إجابتك.
  - 2023 · أكتب "نعم" أو "لا" أمام كلّ إفادة. (يمثّل حجم غاز الأكسجين حوالي خمس حجم الهواء. / يمثّل حجم غاز الأكسجين حوالي ربع حجم غاز النّتروجين في الهواء.)
  - 2023 · أصف تجربة تعلّل إجابتي.
  - 2020 · أضع العلامة (x) أمام الإفادة السّليمة. (نسبة غاز النّيتروجين في الهواء هي 78%. / للهواء شكل خاصّ وحجم خاصّ. / هباب الفحم من نواتج الاحتراق غير التّامّ.)
  - 2020 · أتأمّل التّجربة ثمّ أجب عن الأسئلة التّالية : أعلّل سبب انطفاء الشّمعة / أعلّل سبب صعود الماء في الأنبوب / أصلح الاستنتاج التّالي ليتلاءم مع نتائج التّجربة السّابقة : تمثّل نسبة غاز الأكسجين حوالي 80 % من حجم الهواء.
  - 2020 · أصلح الخطأ الوارد في الإفادة التّالية : عند تسخين الهواء، يزداد حجمه وكتلته.
- Étapes prévues :
  - 2024 (3-أ, 3-ب) : le tube gradué : à quelle graduation le niveau est-il quand la bougie s'éteint, et pourquoi (le gaz restant ne l'entretient plus) — figure refaite avec des graduations de l'auteur, QCM de la graduation, QCM de la justification — 2 q
  - 2023 (4-أ) : deux énoncés sur la part de l'oxygène dans l'air — « نعم/لا ». DÉFAUT : « ربع حجم النتروجين » est une valeur dérivée, non nommée par la fiche ; l'énoncé est reformulé « ربع حجم الهواء » (faux, piège du quart) — multi ou deux QCM — 2 q
  - 2023 (4-ب) : décrire une expérience qui justifie la part d'oxygène : ordre des temps (bougie sur un flotteur, tube retourné dans l'eau, observation du niveau) — ordering, QCM de la conclusion — 2 q
  - 2020 (1) : trois énoncés à marquer — l'air n'a ni forme ni volume propres ; la suie vient de la combustion incomplète ; la part de l'azote en pourcentage est remplacée par « l'oxygène est environ le cinquième du volume de l'air » (V1) — multi — 1 q
  - 2020 (2) : la bougie s'éteint (l'oxygène ne suffit plus), l'eau monte (le gaz consommé laisse de la place) ; corriger « 80 % » en « environ un cinquième » — deux QCM de cause, un QCM de correction — 3 q
  - 2020 (3) : l'air chauffé se dilate : son volume augmente, sa masse ne change pas — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - croire que la bougie s'éteint dès que l'eau monte — ligne C03#7 (d2)
  - oublier que le gaz produit reste dans l'enceinte — ligne C03#8 (d3)
  - penser que la part de l'oxygène est le quart de l'air — ligne C04#16 (d2)
  - oublier de mesurer le gaz consommé — ligne C04#17 (d2)
  - croire que l'air a un volume propre — ligne C07#7 (d2)
  - surestimer la part d'oxygène — ligne C07#8 (d3)
  - penser que la masse augmente avec la chaleur — ligne C07#9 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/quiz#3`, `01/quiz#5`, `01/03-revision#2`, `01/02-boss#4`, `01/04-defi#4`, `01/01-pratique#5`, `01/03-revision#4`
- Note : DÉFAUT DU MANUEL (fiche §4 bis, point 1) : le manuel et le sujet lisent le cinquième d'oxygène dans l'eau montée sous la bougie. La mission l'emploie comme lecture de classe et écrit « environ » : l'explication précise que la bougie s'éteint avant d'avoir consommé tout l'oxygène (voir E-4). Les pourcentages 78 % et 80 % de 2020 ne sont jamais une clé (V1). Le sujet 2024 ne donne pas la hauteur du tube : l'auteur fixe ses graduations de manière cohérente (le cinquième de l'air d'origine).

### m008 → `exercices/09-exams-2019-2026-bruleur-flamme-complete-ou-incomplete.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2019–2026 ⭐⭐⭐: … ») : Concours 2019 · 2022 · 2023 · 2026 · le brûleur et la flamme : combustion complète ou incomplète
- Registre : id `C01#1` ; sources `C01#1, C01#2, C04#18, C05#14, C05#15, C08#9`
- Sources : C01 (session 2026), situation 1, activité 1 ; C04 (session 2023), situation intégrative, support 5 ; C05 (session 2022), situation intégrative, support 3, consignes 3-2-أ et 3-2-ب ; C08 (session 2019), situation intégrative, support 1, consigne 2 — transcriptions `2026-unique.md`, `2023-unique.md`, `2022-unique.md`, `2019-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2026 · أكتبُ " صواب " أو " خطأ " أمام كلّ إفادة. (من نواتج الاحتراق في الصورة 1 ثاني أكسيد الكربون و هباب الفحم. / من نواتج الاحتراق في الصورة 2 ثاني أكسيد الكربون وبخار الماء. / كمّيّة الهواء في الصورة 2 كافية لحرق الغاز بالموقد.)
  - 2026 · صُغْ استنتاجا مناسبا للصّورة 3.
  - 2023 · أصلح كلّ خطأ ورد في الإفادة التّالية ثمّ أعلّل إجابتي. (لتفادي ظهور المادّة السّوداء النّاتجة عن احتراق تامّ لغاز البوتان عدّل الأطفال ضابط هواء الموقد، فساعد ذلك على توفير كمّيّة أكبر من غاز البوتان.)
  - 2022 · أربط بسهم بين نوع الاحتراق وبين الإفادة التي تناسبه. (من نواتجه أحادي أكسيد الكربون. / لهبه أزرق. / لهبه أصفر.)
  - 2022 · أثناء عمليّة الاحتراق، نلاحظ أحيانا تغيّر لون اللّهب من الأزرق إلى الأصفر. أفسّر ذلك.
  - 2019 · أفسّر لفراس الفرق بين الاحتراق التّامّ والاحتراق غير التّامّ في علاقة بغاز الأكسجين.
- Étapes prévues :
  - 2026 (consigne 1) : trois affirmations sur le brûleur (trou d'air libre, doigt sur le trou). DÉFAUT : la première affirmation (suie en flamme bleue) suit l'erreur du manuel ; l'auteur REFORMULE les trois énoncés avec la science juste (flamme bleue = combustion complète : dioxyde de carbone et vapeur d'eau, pas de suie ; flamme jaune = air insuffisant, suie et monoxyde) et n'emploie pas l'énoncé imprimé comme clé — multi (vrai/faux motivé) + QCM — 2 q
  - 2026 (consigne 2) : trou d'air complètement bouché, le brûleur s'éteint : conclusion « pas d'air, donc pas d'oxygène, donc pas de combustion » (et non l'observation « la flamme disparaît ») — QCM de la conclusion — 1 q
  - 2023 (support 5) : la matière noire vient d'une combustion INCOMPLÈTE ; pour l'éviter on laisse entrer plus d'air (pas plus de gaz) — QCM de l'erreur sur « complète », QCM de l'erreur sur « plus de gaz », QCM de la justification — 3 q
  - 2022 (3-2-أ) : relier complète/incomplète aux trois énoncés — matching ; (3-2-ب) la flamme passe du bleu au jaune quand l'air devient insuffisant — QCM — 2 q
  - 2019 (consigne 2) : la différence entre combustion complète et incomplète selon l'oxygène (assez ou pas assez) — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - croire que la suie accompagne toute flamme / confondre air suffisant et insuffisant — ligne C01#1 (d2)
  - décrire l'observation au lieu de conclure — ligne C01#2 (d2)
  - confondre combustion complète et incomplète / augmenter le gaz au lieu de l'air — ligne C04#18 (d3)
  - associer flamme jaune à combustion complète — ligne C05#14 (d2)
  - accuser la quantité de gaz plutôt que celle d'air — ligne C05#15 (d2)
  - ne pas relier la suie au manque d'oxygène — ligne C08#9 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/04-defi#6`, `01/05-entrainement#4`, `01/02-boss#5`, `01/04-defi#5`, `01/quiz#2`
- Note : Trois défauts à ne pas reprendre tels quels : la suie en flamme bleue (2026, 1ʳᵉ affirmation), la 2ᵉ affirmation de 2026 (« dioxyde et vapeur » pour une flamme jaune est vraie mais incomplète : l'auteur la précise), et « ضابط هواء » du brûleur 2023 (le mot est celui du sujet, à garder). Monoxyde de carbone : nommé par les sujets 2022 et 2024 et par le corrigé du guide ; le patron ne le pose pas encore (voir E-7). Les lignes C07#5 et C08#11 (mêmes gestes) ne sont pas reprises.

### m009 → `exercices/10-exams-2008-2024-elements-produits-et-preuves-de-la-combustion.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2008–2024 ⭐⭐⭐: … ») : Concours 2008 · 2010 · 2018 · 2019 · 2020 · 2024 · les éléments d'une combustion, ses produits et leurs preuves
- Registre : id `C17#5a` ; sources `C17#5a, C19#4a, C19#4b, C08#8, C03#9, C07#4, C09#11`
- Sources : C17 (session 2010), support 5 ; C19 (session 2008), support 4, consignes 1 et 2 ; C08 (session 2019), situation intégrative, support 1, consigne 1 ; C03 (session 2024), situation intégrative, support 1 ; C07 (session 2020), situation 2, consigne 1 ; C09 (session 2018), support 4, consigne 1 — transcriptions `2024-unique.md`, `2020-unique.md`, `2019-unique.md`, `2018-unique.md`, `2010-unique.md`, `2008-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2010 · أقرأ المعطيات التالية وأكتبها في الجدول حسب المطلوب : الحطب – ثنائي أكسيد الكربون – الحرارة – الأكسجين – بخار الماء – هباب الفحم.
  - 2008 · أكمل الرّسم التّالي بكتابة بقيّة العناصر النّاتجة عن عمليّة الاحتراق.
  - 2008 · تخيّر التّعليل الصّحيح بوضع العلامة (×) في التّربيعة المناسبة. يتمّ الكشف عن وجود ثنائي أكسيد الكربون خلال عمليّة الاحتراق بـ :
  - 2019 · أسطّر العنصر الدّخيل في كلّ مجموعة. (نواتج عمليّة الاحتراق التّامّ ; العناصر المتدخّلة في عمليّة الاحتراق)
  - 2024 · سمِّ ممّا سبق العناصر الدّالّة على عمليّة الاحتراق غير التّامّ وفسّر سبب ظهورها.
  - 2020 · أعمّر فراغات الجدول التّالي حسب ما تتطلّبه كلّ وضعيّة من الوضعيّتين التّاليتين : (احتراق الشّمعة : تنكيس أنبوب بارد على لهب شمعة → قطرات من الماء على الجدار الدّاخلي للأنبوب → النّاتج المراد إثباته ; الوضعيّة 2 → هباب الفحم)
  - 2018 · أذكر تجربة تثبت أنّ هباب الفحم من نواتج عمليّة الاحتراق.
- Étapes prévues :
  - 2010 : classer six éléments entre « intervenants » et « produits ». DÉFAUT : « الحرارة » est à la fois ce qui intervient (source de chaleur) et ce qui sort ; la mission écrit « مصدر حرارة » pour l'intervenant et « حرارة » pour le produit — matching ; QCM sur la chaleur — 2 q
  - 2008 (1) : compléter le schéma du bec à gaz par les produits (بخار الماء, ثاني أكسيد الكربون) — multi ; (2) le test du dioxyde de carbone : l'eau de chaux se trouble (ni la soucoupe noircie, ni la détonation) — QCM — 2 q
  - 2019 (consigne 1) : l'intrus du groupe des produits (l'oxygène) et du groupe des éléments intervenants (le dioxyde de carbone) — deux QCM — 2 q
  - 2024 : la suie et le monoxyde de carbone signent la combustion incomplète, faute d'oxygène — QCM des éléments, QCM de la cause — 2 q
  - 2020 (1) : un tube froid sur la flamme se couvre de gouttelettes → vapeur d'eau ; un dépôt noir sur une surface froide → suie — matching observation ↔ produit, QCM de la deuxième expérience — 2 q
  - 2018 (4-1) : l'expérience qui prouve la suie : une soucoupe froide tenue au-dessus de la flamme jaune se noircit — ordering des temps, QCM du résultat attendu — 2 q
- Pièges (étiquette à porter par un distracteur) :
  - classer la chaleur des deux côtés — ligne C17#5a (d1)
  - omettre la vapeur d'eau — ligne C19#4a (d1)
  - confondre test à l'eau de chaux et test du dihydrogène — ligne C19#4b (d2)
  - confondre produit et réactif de combustion — ligne C08#8 (d1)
  - citer le dioxyde de carbone parmi les produits de l'incomplète — ligne C03#9 (d2)
  - ne pas relier une observation au produit prouvé — ligne C07#4 (d3)
  - oublier la surface froide pour recueillir le dépôt — ligne C09#11 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/02-boss#5`, `01/04-defi#6`, `01/04-defi#5`, `01/quiz#4`, `01/05-entrainement#6`
- Note : Sept lignes de six sessions : la mission est un tableau d'ensemble de la combustion (ce qui y entre, ce qui en sort, comment on le prouve). Le test du dihydrogène de 2008 n'est qu'un leurre. Étage d3 parce que la ligne de 2020 (tableau d'expériences) l'est. Le monoxyde de carbone : voir E-7. La zone de la flamme (2009, 2015) n'est PAS reprise (◐ contradictoire).

### m010 → `exercices/11-exams-2013-2023-proprietes-et-composants-de-lair.json` · d3 boss 120/30 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرات 2013–2023 ⭐⭐⭐: … ») : Concours 2013 · 2015 · 2022 · 2023 · les propriétés et les composants de l'air
- Registre : id `C04#7` ; sources `C04#7, C04#8, C04#9, C05#5, C12#2a, C14#4b`
- Sources : C04 (session 2023), situation 2, supports 1 et 2 ; C05 (session 2022), situation 2, support 1 ; C12 (session 2015), support 2 ; C14 (session 2013), support 4, consigne 2 — transcriptions `2023-unique.md`, `2022-unique.md`, `2015-unique.md`, `2013-unique.md`
- Phrases officielles à reprendre (consignes et énoncés imprimés, session en tête) :
  - 2023 · أذكر مكوّن الهواء الذي نتَجَ عنه ظهور قطيرات ماء على الواجهة الدّاخليّة لزجاج السيّارة. / أفسّر ظهور قطيرات ماء على الواجهة الدّاخليّة لزجاج السيّارة.
  - 2023 · أذكر ثلاث خاصّيّات للهواء يمكن إثباتها من خلال هذه التّجربة. (منفاخ يدوي، إطار مطّاطي)
  - 2022 · أكتب "صواب" أو "خطأ" أمام كلّ إفادة. (في الهواء، تمثّل نسبة غاز النيتروجين أربعة أضعاف غاز الأكسجين تقريبا. / الهواء قابل للانتشار وغير قابل للانضغاط. / يتقلّص الهواء بارتفاع درجة حرارته.)
  - 2015 · أتأمّل الجدول وأساعد نور على تذكّر خاصّيات الهواء ومكوّناته : (قُطيرات على الجدار الخارجيّ للكأس المملوءة مشروبا باردا ; انتفاخ البالونة المتّصلة بقارورة في ماء حارّ ; ارتفاع المنطاد إثر إشعال موقده)
  - 2013 · أكمل الإفادات التالية بالتعليل المناسب : (bougie sous une cloche : يرتفع مستوى الماء داخل إناء الزجاج لأنّ ........ ; air chaud d'un sèche-cheveux : تظهر فقاقيع هوائيّة في الماء لأنّ ........ ; glace sur le ballon : يصعد قليل من الماء داخل الأنبوب لأنّ ........)
- Étapes prévues :
  - 2023 (1) : le composant de l'air qui donne les gouttelettes (la vapeur d'eau) ; la raison (la vapeur au contact d'une vitre froide se condense) — QCM, QCM — 2 q
  - 2023 (2) : la pompe et le pneu montrent trois propriétés de l'air (il se comprime, il occupe un espace, il remplit un récipient/se diffuse) — multi — 1 q
  - 2022 : trois énoncés vrai/faux : l'air est compressible ; il se contracte quand on le refroidit (donc « يتقلّص بارتفاع الحرارة » est faux) ; la part d'azote en multiples de l'oxygène est reformulée « الأكسجين خمس الهواء » (V1) — multi, QCM — 2 q
  - 2015 : trois phénomènes du quotidien à rattacher à une propriété ou à un composant (buée sur un verre froid : vapeur d'eau ; ballon sur une bouteille chauffée : dilatation ; montgolfière : l'air chaud se dilate) — matching, QCM « propriété ou composant ? » — 2 q
  - 2013 (consigne 2) : trois explications : le niveau d'eau monte sous la cloche parce que le gaz consommé laisse de la place (DÉFAUT du manuel, E-4) ; l'air chaud se dilate et sort en bulles ; la glace refroidit l'air qui se contracte — trois QCM — 3 q
- Pièges (étiquette à porter par un distracteur) :
  - citer le dioxyde de carbone — ligne C04#7 (d1)
  - parler de fuite ou de pluie — ligne C04#8 (d2)
  - oublier la compressibilité — ligne C04#9 (d1)
  - penser que l'air n'est pas compressible — ligne C05#5 (d2)
  - confondre propriété de l'air et composant de l'air — ligne C12#2a (d2)
  - confondre dilatation de l'air et consommation de l'oxygène — ligne C14#4b (d3)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/01-pratique#2`, `01/01-pratique#4`, `01/01-pratique#5`, `01/03-revision#4`, `01/04-defi#3`, `01/05-entrainement#2`, `01/quiz#1`, `01/quiz#2`
- Note : La condensation (C04#7, C04#8) est étiquetée `HP:condensation` par le lecteur, mais le patron l'enseigne déjà (01/01-pratique#4) : à garder (E-7). Le sujet 2015 donne un tableau à deux colonnes (phénomène | propriété ou composants) : le refaire lisible. Le sujet 2022 est le seul à employer « ضعف » pour le rapport de l'azote à l'oxygène.

### m011 → `exercices/12-devoir-un-feu-conditions-etat-tirage.json` · d3 boss 120/30 · 9 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐⭐: … ») : Un feu : les conditions, l'état du combustible, le tirage, l'étouffement
- Registre : id `D02#1` ; sources `D02#1, D02#2, D02#3, D02#4, D02#5, D02#6, D02#13, D03#1, D03#3, D03#4, D03#5`
- Cartes : devoir B (T1, école primaire), exercices 1 à 6 et 13 ; devoir A (T1, école primaire) : version jumelle de B, comptée une fois ; devoir C (T1, école primaire), exercices 1, 3, 4, 5 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D02#1 (d1) : nommer les conditions réunies qui permettent à un combustible de brûler
  - D02#2 (d3) : expliquer un malaise collectif par un gaz toxique d'une combustion en local clos
  - D02#3 (d1) : compléter une phrase sur l'état que prend un corps pour brûler
  - D02#4 (d2) : classer des corps en deux colonnes selon leur combustion directe ou non
  - D02#5 (d2) : expliquer pourquoi un liquide s'enflamme à l'approche d'une flamme
  - D02#6 (d2) : corriger l'erreur dans une définition des conditions de combustion
  - D02#13 (d2) : remettre en ordre les étapes de la combustion d'une bougie
  - D03#1 (d2) : expliquer le rôle d'ouvertures et d'un conduit dans l'entretien d'un feu
  - D03#3 (d2) : désigner le combustible qui brûle d'abord et justifier par son état
  - D03#4 (d2) : proposer un moyen d'étouffer un feu en le conservant et le justifier
  - D03#5 (d1) : compléter une synthèse sur les conditions et la vitesse d'une combustion
- Étapes prévues :
  - Les conditions réunies pour qu'un combustible brûle (combustible, comburant, chaleur) ; corriger une définition qui confond l'oxygène et le dioxyde de carbone — QCM, QCM — 2 q
  - L'état du combustible : un solide ou un liquide brûle sous forme de gaz/vapeur ; classer des corps selon qu'ils brûlent directement ou non ; pourquoi un liquide s'enflamme à l'approche d'une flamme (sa vapeur) ; quel combustible brûle d'abord dans un mélange, et pourquoi — matching, QCM, QCM — 3 q
  - Le tirage : le rôle des ouvertures et d'un conduit (renouveler le comburant) ; étouffer un feu en l'isolant de l'air, et non en retirant le combustible — QCM, QCM — 2 q
  - Les étapes de la combustion d'une bougie, dans l'ordre (fusion, montée par la mèche, vaporisation, combustion, lumière) : cinq temps — ordering — 1 q
  - Un malaise collectif dans une pièce close autour d'un feu de charbon : le gaz toxique d'une combustion incomplète (le monoxyde de carbone), et non « le manque d'air seul » — QCM — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - oublier le comburant ou la chaleur — ligne D02#1 (d1)
  - incriminer le manque d'air seul — ligne D02#2 (d3)
  - croire qu'un solide brûle tel quel — ligne D02#3 (d1)
  - ranger un solide parmi les gaz inflammables — ligne D02#4 (d2)
  - ignorer la vapeur émise par le liquide — ligne D02#5 (d2)
  - confondre oxygène et gaz carbonique — ligne D02#6 (d2)
  - placer l'éclairage avant la vaporisation — ligne D02#13 (d2)
  - oublier le renouvellement du comburant — ligne D03#1 (d2)
  - supposer que le solide s'enflamme le premier — ligne D03#3 (d2)
  - retirer le combustible au lieu d'isoler l'air — ligne D03#4 (d2)
  - omettre la chaleur parmi les conditions — ligne D03#5 (d1)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/01-pratique#6`, `01/03-revision#3`, `01/03-revision#5`, `01/03-revision#6`, `01/03-revision#1`, `01/05-entrainement#1`, `01/05-entrainement#3`, `01/05-entrainement#4`, `01/05-entrainement#5`, `01/02-boss#6`
- Note : Salle blanche. Gestes absents des missions d'examen : l'état du combustible (vaporisation avant combustion), le tirage, l'étouffement d'un feu, l'ordre en cinq temps. D01 est le jumeau de D02 (même énoncé, sans la question du bouchon) : les mêmes lignes ne comptent qu'une fois. La question sur les zones de la flamme (D02#14) n'est pas reprise (◐ contradictoire). Le patron a un ordre en trois temps (05#5) : ici cinq temps.

### m012 → `exercices/13-devoir-experiences-sur-lair.json` · d3 boss 120/30 · 10 questions · régime **devoir**

- Titre de travail (arabe : « 📝 ⭐⭐⭐: … ») : Expériences sur l'air : décrire, interpréter, corriger la conclusion
- Registre : id `D02#9` ; sources `D02#9, D02#10, D03#2, D03#7, D03#8, D03#10, D03#12, D03#13, D05#1, D06#5, D06#6`
- Cartes : devoir B (T1, école primaire), exercices 9, 10 ; devoir C (T1, école primaire), exercices 2, 7, 8, 10, 12, 13 ; devoir E (T2, école primaire), exercice 1 ; devoir F (T2, école primaire), exercices 5, 6 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D02#9 (d2) : justifier qu'on ne peut pas ôter un bouchon d'un flacon fermé sans outil
  - D02#10 (d1) : prévoir le comportement de l'air enfermé quand on pousse un piston
  - D03#2 (d1) : expliquer par une propriété de l'air la perception d'une odeur à distance
  - D03#7 (d2) : associer chaque situation de gonflage de pneu à une propriété de l'air
  - D03#8 (d2) : justifier un moindre gonflage en saison chaude par une dilatation
  - D03#10 (d1) : nommer trois gaz d'après leurs propriétés caractéristiques
  - D03#12 (d2) : corriger la conclusion d'une expérience de dilatation de l'air chauffé
  - D03#13 (d3) : corriger la conclusion d'une expérience de bougie sous cloche sur liquide
  - D05#1 (d3) : compléter trois conclusions d'expériences sur l'air par la bonne explication
  - D06#5 (d2) : décrire une expérience montrant que l'air se comprime
  - D06#6 (d2) : décrire une expérience montrant que l'air se dilate et se contracte
- Étapes prévues :
  - Un flacon fermé qu'on ne peut pas ouvrir sans outil ; un piston qu'on pousse : l'air enfermé résiste et ne disparaît pas — QCM, QCM — 2 q
  - L'odeur perçue à distance (l'air diffuse) ; le gonflage d'un pneu en saison chaude (dilatation) — QCM, QCM — 2 q
  - Trois conclusions d'expériences à corriger : air chauffé (plus léger), bougie sous une cloche sur un liquide (le gaz consommé laisse de la place, ce n'est pas le gaz carbonique), compression/dilatation (ne jamais invoquer l'air « consommé » pour une dilatation) — trois QCM — 3 q
  - Décrire l'expérience qui montre que l'air se comprime et celle qui montre qu'il se dilate ou se contracte : choisir le protocole qui donne un résultat observable — deux QCM — 2 q
  - Reconnaître trois gaz d'après leurs propriétés caractéristiques (le dioxygène rallume un brin incandescent, le dioxyde de carbone trouble l'eau de chaux, le diazote n'entretient pas la combustion) — matching — 1 q
- Pièges (étiquette à porter par un distracteur) :
  - oublier que l'air enfermé résiste — ligne D02#9 (d2)
  - penser que l'air disparaît — ligne D02#10 (d1)
  - croire que l'odeur voyage seule — ligne D03#2 (d1)
  - confondre propriété de masse et de diffusion — ligne D03#7 (d2)
  - attribuer à la pression extérieure seule — ligne D03#8 (d2)
  - confondre dioxygène et diazote — ligne D03#10 (d1)
  - oublier que l'air chaud est plus léger — ligne D03#12 (d2)
  - attribuer au gaz carbonique la consommation — ligne D03#13 (d3)
  - invoquer l'air consommé pour une dilatation — ligne D05#1 (d3)
  - décrire sans résultat observé — ligne D06#5 (d2)
  - oublier le rôle de la température — ligne D06#6 (d2)
- Ne pas redemander (🔁 PROVISOIRE, à revérifier au lancement : le chapitre est mis à niveau après ce plan) : `01/01-pratique#2`, `01/01-pratique#5`, `01/03-revision#4`, `01/04-defi#2`, `01/04-defi#3`, `01/05-entrainement#2`, `01/quiz#1`, `01/quiz#4`
- Note : Salle blanche. Les expériences à conclusion fautive à corriger sont le geste du devoir (trois lignes d'expériences à l'état d'archétype). Aucune donnée numérique de masse volumique n'est fournie par ces devoirs : la masse de deux litres d'air (D03#9) n'est pas reprise. Attention au recouvrement avec la mission « refroidir, chauffer, peser » : ici ce sont les raisonnements du quotidien et la correction de conclusions, pas la pesée.
