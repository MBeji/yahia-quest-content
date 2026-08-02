# C3 — post-GAP-020 verification: the answer key is masked from direct client reads,
# yet the legitimate correction is still available via the gated get_attempt_review
# RPC after a completed submit. TEST only.
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
URL = env["SUPABASE_URL"]
KEY = env["VITE_SUPABASE_PUBLISHABLE_KEY"]
PWD = env["E2E_USER_PASSWORD"]
if "fasrenmmrkqjoobrztbp" in URL:
    sys.exit("prod")

IQ_EXERCISE = "f4549597-d9ab-5f0a-a973-b7ec0c361a4c"  # free IQ theme, no quiz/premium gate


def http(method, path, token=None, body=None, prefer=None):
    headers = {"apikey": KEY, "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    if prefer:
        headers["Prefer"] = prefer
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
uid = json.loads(__import__("base64").b64decode(token.split(".")[1] + "==").decode())["sub"]

# 1) The answer key must NOT be directly readable anymore (GAP-020).
st, _ = http("GET", f"/rest/v1/questions?select=correct_option&exercise_id=eq.{IQ_EXERCISE}", token)
print(f"1) read questions.correct_option directly   HTTP {st}  "
      + ("✅ blocked (masked)" if st == 403 else "❌ STILL READABLE"))

# Question text/options stay readable (the app needs them).
st, txt = http("GET", f"/rest/v1/questions?select=id,prompt,options&exercise_id=eq.{IQ_EXERCISE}", token)
qids = [q["id"] for q in (json.loads(txt) if st == 200 else [])]
print(f"2) read id/prompt/options (app needs these) HTTP {st}  rows={len(qids)}  "
      + ("✅ allowed" if st == 200 and qids else "❌ broke the app"))

# 3) Legit flow: create a session, submit via the RPC (any answers), then fetch the
#    correction via the gated get_attempt_review RPC.
st, txt = http("POST", "/rest/v1/exercise_sessions", token,
               body={"user_id": uid, "exercise_id": IQ_EXERCISE}, prefer="return=representation")
session_id = json.loads(txt)[0]["id"]
answers = [{"questionId": q, "choice": "a"} for q in qids]
st, _ = http("POST", "/rest/v1/rpc/submit_exercise_attempt", token,
             body={"p_session_id": session_id, "p_exercise_id": IQ_EXERCISE, "p_answers": answers})
print(f"3) legit submit via RPC                     HTTP {st}  "
      + ("✅ works" if st in (200, 204) else "❌ BROKEN"))

# 4) The correction is available to the owner via the gated RPC (after submit).
st, txt = http("POST", "/rest/v1/rpc/get_attempt_review", token, body={"p_session_id": session_id})
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
has_key = rows and rows[0].get("correct_option")
print(f"4) get_attempt_review (gated correction)    HTTP {st}  rows={len(rows)}  "
      + ("✅ correction available to owner" if has_key else "❌ no correction"))

# 5) Another user cannot read the correction for this session (ownership gate).
st2, txt2 = http("POST", "/auth/v1/token?grant_type=password",
                 body={"email": "parent@e2e.na9ranal3ab.test", "password": PWD})
other = json.loads(txt2)["access_token"]
st, txt = http("POST", "/rest/v1/rpc/get_attempt_review", other, body={"p_session_id": session_id})
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
print(f"5) other user reads this session's review   HTTP {st}  rows={len(rows)}  "
      + ("✅ blocked (not owner)" if len(rows) == 0 else "❌ LEAK"))
