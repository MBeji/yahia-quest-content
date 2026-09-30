"""Ajoute (idempotent) la ligne sources[] des sujets officiels aux chapter.json donnés (un seul diff d'une ligne)."""
import json, sys
LINE = "Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/math/"
for p in sys.argv[1:]:
    raw = open(p, encoding='utf-8').read(); j = json.loads(raw)
    assert json.dumps(j, ensure_ascii=False, indent=2) + '\n' == raw, 'format non reproduit ' + p
    if LINE in j.setdefault('sources', []):
        print('déjà présente :', p); continue
    j['sources'].append(LINE)
    open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    print('ajoutée :', p)
