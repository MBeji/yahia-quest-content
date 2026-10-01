#!/usr/bin/env python3
"""usage: mksnap.py <id> -> snapshots/9web.edunet.tn/<id>.txt from officiel/<id>.md (front matter removed, quote/list marks removed)."""
import sys, re
SP = "/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/gisement/9eme-sciences-vie-terre"
id_ = sys.argv[1]
md = open(f"{SP}/officiel/{id_}.md", encoding="utf-8").read()
m = re.match(r"^---\n.*?\n---\n", md, re.S)
body = md[m.end():] if m else md
lines = []
for l in body.splitlines():
    l = re.sub(r"^\s*>\s?", "", l)          # citation
    l = re.sub(r"^(\s*)- ", r"\1", l)        # puces
    lines.append(l.rstrip())
txt = "\n".join(lines).strip() + "\n"
txt = re.sub(r"\n{3,}", "\n\n", txt)
open(f"{SP}/snapshots/9web.edunet.tn/{id_}.txt", "w", encoding="utf-8").write(txt)
print(f"snapshot {id_}.txt : {len(txt)} caractères")
