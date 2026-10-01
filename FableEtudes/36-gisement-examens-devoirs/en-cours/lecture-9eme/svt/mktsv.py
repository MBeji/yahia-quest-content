#!/usr/bin/env python3
"""usage: mktsv.py <id> < rows.txt  ; rows.txt = one row per line, columns separated by ' || ' -> writes lines/<id>.tsv with tabs."""
import sys
SP = "/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/gisement/9eme-sciences-vie-terre"
id_ = sys.argv[1]
out = []
for raw in sys.stdin.read().splitlines():
    if not raw.strip():
        continue
    cols = [c.strip() for c in raw.split(" || ")]
    if len(cols) != 10:
        sys.exit(f"ligne à {len(cols)} colonnes : {raw[:60]}")
    out.append("\t".join(cols))
open(f"{SP}/lines/{id_}.tsv", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{len(out)} ligne(s) -> lines/{id_}.tsv")
