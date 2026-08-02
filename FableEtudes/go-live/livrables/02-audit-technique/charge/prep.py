# C2/S2 — prépare le jeu de données des tests de charge (TEST uniquement).
# - crée N comptes de charge (admin API, email_confirm) -> trigger handle_new_user crée le profil
# - récupère un JWT par compte (password grant, throttlé, backoff sur 429)
# - extrait M exercices culture-generale + corrigés (SQL direct, service path)
# - écrit data/run-data.json consommé par k6-main.js
# Garde anti-prod identique à q.py. Secrets jamais imprimés.
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

import psycopg

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENV = r"D:\11-coding\YahiaAcademy\yahia-quest-arena\.env.test"
N_USERS = 40
N_EXERCISES = 30
EMAIL_TPL = "load{:03d}@e2e.na9ranal3ab.test"

env = {}
for line in open(ENV, encoding="utf-8"):
    m = re.match(r'^([A-Z0-9_]+)\s*=\s*"?([^"\n]*)"?\s*$', line)
    if m:
        env[m.group(1)] = m.group(2)

URL = env["SUPABASE_URL"].rstrip("/")
ANON = env["SUPABASE_PUBLISHABLE_KEY"]
SERVICE = env["SUPABASE_SERVICE_ROLE_KEY"]
PASSWORD = env["E2E_USER_PASSWORD"]
DB = env["TEST_SUPABASE_DB_URL"]
if "fasrenmmrkqjoobrztbp" in URL or "fasrenmmrkqjoobrztbp" in DB:
    sys.exit("Refusing: production")
if "sslmode" not in DB:
    DB += ("&" if "?" in DB else "?") + "sslmode=require"


def call(path, payload=None, key=ANON, bearer=None, method=None):
    req = urllib.request.Request(
        URL + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        method=method or ("POST" if payload is not None else "GET"),
    )
    req.add_header("apikey", key)
    req.add_header("Authorization", f"Bearer {bearer or key}")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read() or "null")


# 1) comptes de charge
created = existing = 0
for i in range(1, N_USERS + 1):
    email = EMAIL_TPL.format(i)
    try:
        call("/auth/v1/admin/users", {"email": email, "password": PASSWORD, "email_confirm": True}, key=SERVICE)
        created += 1
    except urllib.error.HTTPError as e:
        if e.code in (422, 400):  # already exists
            existing += 1
        else:
            raise
print(f"users: {created} created, {existing} existing")

# 2) tokens (throttlé ; backoff sur 429)
users = []
for i in range(1, N_USERS + 1):
    email = EMAIL_TPL.format(i)
    while True:
        try:
            tok = call("/auth/v1/token?grant_type=password", {"email": email, "password": PASSWORD})
            users.append({"email": email, "id": tok["user"]["id"], "token": tok["access_token"]})
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"  429 sur token ({email}) — backoff 65s")
                time.sleep(65)
            else:
                raise
    time.sleep(0.1)
print(f"tokens: {len(users)}")

# 3) corpus exercices + corrigés (culture-generale = libre, hors gate quiz école)
conn = psycopg.connect(DB)
cur = conn.cursor()
cur.execute(
    """
    SELECT e.id, q.id, q.correct_option
    FROM exercises e
    JOIN chapters c ON c.id = e.chapter_id
    JOIN subjects s ON s.id = c.subject_id
    JOIN questions q ON q.exercise_id = e.id
    WHERE s.theme_id = 'culture-generale'
    ORDER BY e.id, q.id
    """
)
by_ex = {}
for ex_id, q_id, correct in cur.fetchall():
    by_ex.setdefault(str(ex_id), []).append({"questionId": str(q_id), "choice": correct})
conn.close()
exercises = [
    {"id": ex_id, "n": len(answers), "answers": answers}
    for ex_id, answers in list(by_ex.items())[:N_EXERCISES]
]
print(f"exercises: {len(exercises)} (questions/exo: min {min(e['n'] for e in exercises)}, max {max(e['n'] for e in exercises)})")

out = pathlib.Path(__file__).parent / "data" / "run-data.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"url": URL, "anon": ANON, "users": users, "exercises": exercises}))
print(f"written: {out} (tokens TTL 1h — relancer prep avant chaque campagne)")
