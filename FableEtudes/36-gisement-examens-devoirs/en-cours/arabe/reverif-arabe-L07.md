# Re-vérification L07 — `12/exercices/07-devoir-al-ism-al-manqus.json`

Commit vérifié : `b9c11892` (corrections d'audit), comparé à `11f2f8c5`. Dans le chapitre 12, seul le fichier L07 a changé.
Les autres fichiers du diff appartiennent aux chapitres 09 et 10 (L06) et n'ont pas été examinés. Journal de l'auteur :
`auteurs-notes/ar-devoirs-v2/CORRECTIONS.md`. Aucune écriture dans `content/`, aucune opération git.

## Gates et anti-copie

| contrôle | résultat |
|---|---|
| `content:gisement:controle -- --sources …/devoirs-snapshots/arabic <fichier>` | 6 textes ; plage ≥ 8 mots : 0 ; ≥ 6 mots : 0 ; données communes : 0 ✓ |
| `content:check` | 0 erreur ✓ |
| `content:qa:strict` | 0 erreur ; aucun avertissement sur `arabic/12` ✓ |
| `content:tranche -- --subject arabic --chapters 12` | clé strictement la plus longue 0/41 ; paires proches 0 ; gabarits 0 ✓ |

## Correctifs

| point | état | constat |
|---|---|---|
| M-1 Q2 supprimée | ✓ | 6 questions ; plus rien de 12/01 Q6 ni du quiz Q4 |
| M-2 Q4 « اشتقَّ اسمَ الفاعلِ » | ✓ | impératif, comme dans le cours |
| M-3 nouvelle Q6 | ✓ | texte du rapport repris mot pour mot (prompt, 6 options, clé a/c/f, explication) |
| M-4 Q7 c et d, explication | ✓ | texte du rapport repris mot pour mot ; étiquettes c `manqus-ya`, d `fa3il-maf3ul-ma3na` |
| Q5 a étiquetée | ✓ | `arabe.sinf.akhir-khalt` ; c reste muette, plan 2×2 intact |
| m-2 Q3 « مقدَّرة » | ✓ | remplacé par « ولا تظهرُ الضمّةُ على يائِه » |
| m-1 `sources[]` | non fait, décision du pilote | le pilote l'ajoute à la livraison |
| m-4 « ببانٍ » | non fait, décision du pilote | refusé à dessein : la consigne exclut la préposition |
| m-6 étiquette de Q7 d | non fait, décision du pilote | `fa3il-maf3ul-ma3na` reste acceptable |
| m-3, m-5, m-7 | consignés | rien à changer dans le fichier |

## Re-résolution à l'aveugle

**Q6 (multi, d3).** Il faut retenir les verbes dont la dernière lettre est faible, puis former leur participe actif.
« استقصى » donne مُستقصٍ (manqus) ; « نجا » donne ناجٍ (manqus, alif final) ; « اشترى » donne مُشترٍ (manqus).
« استقامَ » est أجوف et donne مُستقيم ; « اشتدَّ » est مضاعف et donne مُشتدّ ; « انتصرَ » est un verbe sain et donne
مُنتصِر. Ma réponse est a, c, f, comme la clé. ✓ L'explication est juste de bout en bout. La question n'a aucune étiquette,
ce qui est conforme pour un multi.

**Q7 (mcq, d3).** Le participe actif de « ألقى » est مُلقٍ. Après « إلى », il est nakira au génitif, donc a « استمعنا إلى مُلقٍ بارعٍ »
est la seule écriture juste. Les trois autres sont fausses :
- b « حضرَ مُلقيٌ » garde la ya au nominatif ;
- c « رأينا مُلقٍ بارعًا » supprime la ya à l'accusatif (il faudrait « مُلقيًا ») ;
- d « مُلقًى » est le participe passif.

Ma réponse est a, comme la clé. ✓ Les étiquettes de b et c correspondent exactement aux deux branches du libellé
`manqus-ya`. L'explication est juste.

Questions inchangées (Q1, Q3, Q4, Q5) : je les ai relues, les clés sont toujours justes. Les points du § 2 de l'audit sur
la normalisation des `short_answer` restent valables.

## Vote, fuites et rampe

- **Vote, Q7.** Longueurs sans diacritiques : a 37, b 30, c 32, d 37. La clé n'est pas strictement la plus longue. Chaque
  option a son propre cadre. La forme « مُلقٍ » est en a et c, le cas nominatif en b et d. Aucun vote ne désigne a.
  Les mêmes mesures valent pour Q5 (quatre options de 36 caractères, votes 2/2).
- **Vote, Q6.** Options de 5 à 8 caractères. Le schème ne trahit pas la clé : استفعل est en a (clé) et b (non-clé) ;
  افتعل en d, e (non-clés) et f (clé). Avec 3 bonnes réponses sur 6, le nombre ne se devine pas.
- **Fuites.** L'ordre d'émission est Q1 (d2), puis Q3, Q4, Q5, Q6, Q7 (d3, tri stable).
  - L'explication de Q6 ne cite aucun verbe de schème أفعل : la fuite par analogie vers « ألقى ← مُلقٍ » a disparu.
  - Le doublon de fait Q5 → Q6 est levé : Q6 ne demande plus de classer le participe passif.
  - Les explications de Q1, Q3, Q4 et Q5 énoncent la règle du cours, mais ne donnent la clé d'aucune question suivante.
  - Q7, dernière question, ne fuit vers rien.
  - Aucune fuite vers les missions publiées du 12 ni vers `m026` ou `m031`.
- **Rampe.** 2 → 3, sans recul. Étage d3, `boss` 120/30, `displayOrder` 7. Avec 6 questions, la mission est au minimum
  d'un boss.

## Verdict

**Conforme, bon pour la livraison.** 6 questions, 0 clé fausse, 0 défaut majeur restant. Restent deux réserves,
déjà tranchées par le pilote : la ligne `sources[]` du `chapter.json`, que le pilote ajoute à la livraison, et la
télémétrie de Q4 qui mêle deux erreurs (limite du moteur, consignée).
