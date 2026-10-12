#!/usr/bin/env python3
"""Dump compact d'un fichier exercice/quiz (JSON) : titre, entête, et par question prompt (svg abrégé), options, clé, étiquettes.
Usage : python3 -I dump.py fichier.json [--svg] [--expl]
"""
import json, re, sys

def short_svg(s, keep):
    if keep:
        return s
    return re.sub(r'<svg.*?</svg>', lambda m: '[SVG %d car.]' % len(m.group(0)), s, flags=re.S)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    keep_svg = '--svg' in sys.argv
    show_expl = '--expl' in sys.argv
    for path in args:
        d = json.load(open(path, encoding='utf-8'))
        print('=' * 100)
        print(path)
        hdr = {k: d[k] for k in d if k not in ('questions',)}
        print('HEADER', json.dumps(hdr, ensure_ascii=False))
        for i, q in enumerate(d['questions'], 1):
            t = q.get('type', 'mcq')
            print('-' * 80)
            print('Q%d [%s] d%s' % (i, t, q.get('difficulty')))
            print('  PROMPT:', short_svg(q['prompt'], keep_svg).replace('\n', '\n          '))
            key = q.get('correctOption')
            ak = q.get('answerKey')
            for o in q.get('options', []):
                mark = ''
                if t == 'mcq' and o['id'] == key:
                    mark = ' <== CLE'
                elif t == 'multi' and ak and o['id'] in ak.get('correct', []):
                    mark = ' <== VRAI'
                tag = o.get('misconceptionTag')
                print('   (%s) %s%s%s' % (o['id'], short_svg(o['text'], keep_svg).replace('\n', ' // '), mark, ('  [tag: %s]' % tag) if tag else ''))
            if ak:
                print('  ANSWERKEY:', json.dumps(ak, ensure_ascii=False))
            if show_expl:
                print('  EXPL:', short_svg(q.get('explanation', ''), keep_svg).replace('\n', '\n        '))

main()
