# C3 probe (round 2) — confirm the answer-key leak (S-4) and premium-content reach (S-3)
# as a normal authenticated student via PostgREST. TEST only.
import json
import re
import sys
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENV = r"D:\11-coding\YahiaAcademy\yahia-quest-arena\.env.test"
env = {}
for line in open(ENV, encoding="utf-8"):
    m = re.match(r'^([A-Z0-9_]+)\s*=\s*"?([^"\n]*)"?\s*$', line)
    if m:
        env[m.group(1)] = m.group(2)
URL = env.get("SUPABASE_URL")
KEY = env.get("VITE_SUPABASE_PUBLISHABLE_KEY")
PWD = env.get("E2E_USER_PASSWORD")
if "fasrenmmrkqjoobrztbp" in URL:
    sys.exit("prod")

QUIZ_EXERCISE = "c4f248a7-393a-5c6d-b4af-90311f1ae35d"  # english Present Tenses quiz
PREMIUM_BOSS = "458c297a-6ea2-522c-9a6c-6dc0c6c7267b"   # difficulty-3 boss (premium-gated)


def http(method, path, token=None, body=None):
    headers = {"apikey": KEY, "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(URL + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


st, txt = http("POST", "/auth/v1/token?grant_type=password",
               body={"email": "student.free@e2e.na9ranal3ab.test", "password": PWD})
token = json.loads(txt)["access_token"]

# S-4 — read the answer key directly (correct_option) for the quiz's questions.
st, txt = http("GET", f"/rest/v1/questions?select=id,correct_option&exercise_id=eq.{QUIZ_EXERCISE}", token)
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
has_keys = [r for r in rows if r.get("correct_option")]
print(f"S-4 read questions.correct_option (quiz)   HTTP {st}  rows={len(rows)}  with_answer={len(has_keys)}  "
      + ("❌ ANSWER KEY LEAKED" if has_keys else "✅ hidden"))
if has_keys:
    print(f"   -> sample: {has_keys[0]}")

# S-3 — read the answer key for a PREMIUM difficulty-3 boss (free student, no entitlement).
st, txt = http("GET", f"/rest/v1/questions?select=id,correct_option&exercise_id=eq.{PREMIUM_BOSS}", token)
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
has_keys = [r for r in rows if r.get("correct_option")]
print(f"S-3 read premium boss answer key (no entl) HTTP {st}  rows={len(rows)}  with_answer={len(has_keys)}  "
      + ("❌ PREMIUM CONTENT + KEY LEAKED" if has_keys else "✅ hidden"))
