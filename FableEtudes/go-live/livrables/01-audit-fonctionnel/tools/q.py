# C1 audit SQL helper: run a read query (or --exec statement) against TEST.
# Usage:
#   python q.py "select ..."            -> prints rows
#   python q.py --exec "update ..."     -> runs DML, prints rowcount
# Never points at prod (guard). Secrets stay in .env.test (never echoed).
import re
import sys

import psycopg

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENV = r"D:\11-coding\YahiaAcademy\yahia-quest-arena\.env.test"
env = {}
for line in open(ENV, encoding="utf-8"):
    m = re.match(r'^([A-Z0-9_]+)\s*=\s*"?([^"\n]*)"?\s*$', line)
    if m:
        env[m.group(1)] = m.group(2)
url = env["TEST_SUPABASE_DB_URL"]
if "fasrenmmrkqjoobrztbp" in url:
    sys.exit("Refusing: production")
if "sslmode" not in url:
    url += ("&" if "?" in url else "?") + "sslmode=require"

args = sys.argv[1:]
is_exec = args and args[0] == "--exec"
if is_exec:
    args = args[1:]
sql = args[0]

conn = psycopg.connect(url)
conn.autocommit = True
cur = conn.cursor()
cur.execute(sql)
if is_exec:
    print(f"rowcount={cur.rowcount}")
else:
    cols = [d.name for d in cur.description] if cur.description else []
    print(" | ".join(cols))
    for row in cur.fetchall():
        print(" | ".join("" if v is None else str(v) for v in row))
conn.close()
