# C3 security probe harness — exercises the PUBLIC PostgREST API as a normal
# authenticated user (so RLS + grants apply, unlike direct SQL). Confirms/refutes
# each candidate vector end-to-end. TEST project only (prod-guarded).
#
# Run: D:\11-coding\YahiaAcademy\.venv\Scripts\python.exe probe.py
import json
import re
import sys
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENV = r"D:\11-coding\YahiaAcademy\yahia-quest-arena\.env.test"
PROD_REF = "fasrenmmrkqjoobrztbp"
PREMIUM_UID = "661e4e2e-a4e1-41f8-a391-67d3d4385370"  # student.premium (target for IDOR/link)
FK_EXERCISE = "458c297a-6ea2-522c-9a6c-6dc0c6c7267b"  # a real exercise (english subject)
FK_SUBJECT = "english"

env = {}
for line in open(ENV, encoding="utf-8"):
    m = re.match(r'^([A-Z0-9_]+)\s*=\s*"?([^"\n]*)"?\s*$', line)
    if m:
        env[m.group(1)] = m.group(2)
URL = env.get("SUPABASE_URL") or env.get("VITE_SUPABASE_URL")
KEY = env.get("VITE_SUPABASE_PUBLISHABLE_KEY") or env.get("SUPABASE_PUBLISHABLE_KEY")
PWD = env.get("E2E_USER_PASSWORD")
if not (URL and KEY and PWD):
    sys.exit("incomplete .env.test")
if PROD_REF in URL:
    sys.exit("Refusing: production")


def http(method, path, token=None, body=None, prefer=None):
    url = URL + path
    headers = {"apikey": KEY, "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    if prefer:
        headers["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:  # noqa
        return -1, str(e)


def signin(email):
    st, txt = http(
        "POST",
        "/auth/v1/token?grant_type=password",
        body={"email": email, "password": PWD},
    )
    if st != 200:
        sys.exit(f"signin {email} failed: {st} {txt[:200]}")
    j = json.loads(txt)
    return j["access_token"], j["user"]["id"]


def verdict(is_vuln):
    return "❌ VULNERABLE" if is_vuln else "✅ blocked/secure"


token, uid = signin("student.free@e2e.na9ranal3ab.test")
print(f"# signed in as student.free  uid={uid}\n")

# P1 — Forge attempts (GAP-016): inflated xp_earned via direct INSERT.
st, txt = http(
    "POST",
    "/rest/v1/attempts",
    token,
    body={
        "user_id": uid,
        "exercise_id": FK_EXERCISE,
        "subject_id": FK_SUBJECT,
        "correct_count": 6,
        "total_count": 6,
        "score_pct": 100,
        "duration_seconds": 60,
        "xp_earned": 99999,
        "completed_at": "2026-06-10T12:00:00Z",
    },
    prefer="return=representation",
)
forged = st in (200, 201)
print(f"P1 forge attempts (xp_earned=99999)        HTTP {st}  {verdict(forged)}")
if not forged:
    print(f"   -> {txt[:160]}")

# P2 — Direct profile inflation (xp/coins) — expected blocked (no UPDATE grant).
st, txt = http(
    "PATCH", f"/rest/v1/profiles?id=eq.{uid}", token,
    body={"xp": 999999, "yahia_coins": 999999}, prefer="return=representation",
)
prof_vuln = st in (200, 204) and txt.strip() not in ("", "[]")
print(f"P2 inflate own profile xp/coins            HTTP {st}  {verdict(prof_vuln)}")
if prof_vuln:
    print(f"   -> {txt[:160]}")

# P3 — Self-escalate role to admin — expected blocked (trigger).
st, txt = http(
    "PATCH", f"/rest/v1/profiles?id=eq.{uid}", token,
    body={"role": "admin"}, prefer="return=representation",
)
role_vuln = st in (200, 204) and '"role":"admin"' in txt.replace(" ", "")
print(f"P3 self-escalate role=admin                HTTP {st}  {verdict(role_vuln)}")

# P4 — Self-grant premium entitlement — expected blocked (no INSERT grant).
st, txt = http(
    "POST", "/rest/v1/parcours_entitlements", token,
    body={"user_id": uid, "parcours_id": "concours-9eme", "source": "purchase"},
)
ent_vuln = st in (200, 201)
print(f"P4 self-grant premium entitlement          HTTP {st}  {verdict(ent_vuln)}")

# P5 — Self-link as parent to another student (PII + family pack) — expect blocked.
st, txt = http(
    "POST", "/rest/v1/parent_student_links", token,
    body={"parent_user_id": uid, "student_user_id": PREMIUM_UID, "is_active": True},
)
link_vuln = st in (200, 201)
print(f"P5 self-link to another student            HTTP {st}  {verdict(link_vuln)}")

# P6 — IDOR: read another user's profile.
st, txt = http("GET", f"/rest/v1/profiles?id=eq.{PREMIUM_UID}&select=id,role,xp", token)
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
idor_prof = len(rows) > 0
print(f"P6 IDOR read another profile               HTTP {st}  rows={len(rows)}  {verdict(idor_prof)}")

# P7 — IDOR: read another user's entitlements.
st, txt = http("GET", f"/rest/v1/parcours_entitlements?user_id=eq.{PREMIUM_UID}", token)
rows = json.loads(txt) if st == 200 and txt.startswith("[") else []
idor_ent = len(rows) > 0
print(f"P7 IDOR read another's entitlements        HTTP {st}  rows={len(rows)}  {verdict(idor_ent)}")

# P8 — Direct call to the XP minter award_xp — expected blocked (revoked).
st, txt = http("POST", "/rest/v1/rpc/award_xp", token, body={"p_user": uid, "p_xp": 99999})
mint_vuln = st in (200, 204)
print(f"P8 direct rpc/award_xp (mint XP)           HTTP {st}  {verdict(mint_vuln)}")

# P9 — Direct call to admin_grant_parcours as non-admin — expect internal denial.
st, txt = http(
    "POST", "/rest/v1/rpc/admin_grant_parcours", token,
    body={"p_user": uid, "p_parcours": "concours-9eme"},
)
admin_vuln = st in (200, 204)
print(f"P9 non-admin calls admin_grant_parcours    HTTP {st}  {verdict(admin_vuln)}")
if not admin_vuln:
    print(f"   -> denial: {txt[:120]}")

# P10 — Forge an exercise_session then complete it (forge progression).
st, txt = http(
    "POST", "/rest/v1/exercise_sessions", token,
    body={"user_id": uid, "exercise_id": FK_EXERCISE}, prefer="return=representation",
)
sess_vuln = st in (200, 201)
print(f"P10 forge exercise_session                 HTTP {st}  {verdict(sess_vuln)}")

print("\n# NOTE: forged rows (if any) are on TEST; rerun fix-test-seed.py to reset.")
