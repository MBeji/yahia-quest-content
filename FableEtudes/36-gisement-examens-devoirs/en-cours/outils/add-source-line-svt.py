"""Ajoute (idempotent) la ligne sources[] des sujets officiels de SVT 9ᵉ aux chapter.json donnés, SANS reformater le fichier :
seule la ligne `"sources": [],` (ou le dernier élément d'une liste existante) change — les chapter.json de SVT ne sont pas
reproductibles par json.dumps (mise en forme du dépôt), donc on édite le texte et on vérifie le résultat à l'analyse."""
import json, sys
LINE = "Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/"
for p in sys.argv[1:]:
    raw = open(p, encoding='utf-8').read(); j = json.loads(raw)
    src = j.get('sources', [])
    if LINE in src:
        print('déjà présente :', p); continue
    lit = json.dumps(LINE, ensure_ascii=False)
    if src == [] and raw.count('"sources": [],') == 1:
        new = raw.replace('"sources": [],', '"sources": [\n    ' + lit + '\n  ],', 1)
    elif src and raw.count('"sources": [') == 1:
        # liste non vide : on ajoute après le dernier élément (mise en forme « un élément par ligne »)
        i = raw.index('"sources": [')
        k = raw.index('\n  ]', i)
        new = raw[:k] + ',\n    ' + lit + raw[k:]
    else:
        sys.exit('mise en forme de sources[] non reconnue : ' + p)
    j2 = json.loads(new)
    assert j2['sources'] == src + [LINE], ('sources inattendues', p)
    assert {k: v for k, v in j2.items() if k != 'sources'} == {k: v for k, v in j.items() if k != 'sources'}, ('autre clé modifiée', p)
    open(p, 'w', encoding='utf-8').write(new)
    print('ajoutée :', p)
