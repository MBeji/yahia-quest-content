"""Ajoute (idempotent) la ligne sources[] des sujets officiels aux chapter.json donnés (un seul diff d'une ligne)."""
import json, sys
OLD = "Calibré sur des devoirs et des sujets d'examen publics (étude 27, T2′, aucune reprise) — carte de veille : programmes-officiels/sources-externes/web-9eme-base-math/fiche.md"
NEW = "Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-9eme-base-math/fiche.md"
LINE = "Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/math/"
for p in sys.argv[1:]:
    raw = open(p, encoding='utf-8').read(); j = json.loads(raw)
    assert json.dumps(j, ensure_ascii=False, indent=2) + '\n' == raw, 'format non reproduit ' + p
    src = j.setdefault('sources', [])
    if OLD in src:                      # la ligne des devoirs : les sujets d'examen ont leur propre ligne ci-dessous
        src[src.index(OLD)] = NEW; print('ligne devoirs alignée :', p)
    if LINE in src:
        print('déjà présente :', p)
        open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=2) + '\n'); continue
    src.append(LINE)
    open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    print('ajoutée :', p)
