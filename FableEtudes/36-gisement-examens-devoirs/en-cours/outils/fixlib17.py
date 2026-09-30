import json, glob, re
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
REG = json.load(open(SP + '/misc-main.json', encoding='utf-8'))
def mk(base):
    def path(n): return glob.glob(base + n + '-*.json')[0]
    def load(n):
        p = path(n); raw = open(p, encoding='utf8').read(); return p, raw, json.loads(raw)
    return path, load
def save(p, raw, d):
    indent = 2 if '\n  "' in raw else None
    out = json.dumps(d, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
    json.loads(out)
    open(p, 'w', encoding='utf8').write(out)
def sub(q, field, old, new):
    t = q[field]; n = t.count(old); assert n == 1, (field, n, old[:90]); q[field] = t.replace(old, new)
def opt(q, oid): return [o for o in q['options'] if o['id'] == oid][0]
def setopt(q, oid, text, tag='KEEP'):
    o = opt(q, oid); o['text'] = text
    if tag is None: o.pop('misconceptionTag', None)
    elif tag != 'KEEP': assert tag in REG, tag; o['misconceptionTag'] = tag
def tag(q, oid, t):
    if t is None: opt(q, oid).pop('misconceptionTag', None)
    else: assert t in REG, t; opt(q, oid)['misconceptionTag'] = t
