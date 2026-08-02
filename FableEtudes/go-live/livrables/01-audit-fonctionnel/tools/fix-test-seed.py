# C1 audit tool - apply roles + premium entitlements + gameplay reset on the TEST
# project via DIRECT SQL (TEST_SUPABASE_DB_URL). This is the sanctioned escape
# hatch: prevent_role_escalation allows role writes when request.jwt.claims is
# NULL (direct SQL), and direct SQL bypasses the broken admin_grant_parcours
# guard (GAP-011). Replicates scripts/e2e/{seed-test-users,reset-gameplay}.mjs.
# Idempotent. NEVER points at prod (guard below).
#
# Run: D:\11-coding\YahiaAcademy\.venv\Scripts\python.exe fix-test-seed.py [--no-reset]
import re
import sys

import psycopg

ENV_PATH = r"D:\11-coding\YahiaAcademy\yahia-quest-arena\.env.test"
PROD_REF = "fasrenmmrkqjoobrztbp"

env = {}
with open(ENV_PATH, encoding="utf-8") as f:
    for line in f:
        m = re.match(r'^([A-Z0-9_]+)\s*=\s*"?([^"\n]*)"?\s*$', line)
        if m:
            env[m.group(1)] = m.group(2)

url = env["TEST_SUPABASE_DB_URL"]
if PROD_REF in url or PROD_REF in env.get("SUPABASE_URL", ""):
    sys.exit("Refusing: production project detected")
if "sslmode" not in url:
    url += ("&" if "?" in url else "?") + "sslmode=require"

USERS = {
    "student.free@e2e.na9ranal3ab.test": ("student", "Free Student", False),
    "student.premium@e2e.na9ranal3ab.test": ("student", "Premium Student", True),
    "parent@e2e.na9ranal3ab.test": ("parent", "Test Parent", False),
    "admin@e2e.na9ranal3ab.test": ("admin", "Test Admin", False),
}
PREMIUM_PARCOURS = ["concours-9eme", "concours-6eme"]
GAMEPLAY_TABLES = [
    "attempts", "dungeon_run_questions", "dungeon_runs",
    "spaced_repetition_schedule", "daily_objectives", "weekly_quests",
    "difficulty_adaptation", "student_badges", "inventory_items",
    "exercise_assignments", "rate_limit_events",
]

do_reset = "--no-reset" not in sys.argv

conn = psycopg.connect(url)
conn.autocommit = True
cur = conn.cursor()

print("== roles ==")
for email, (role, display, _premium) in USERS.items():
    cur.execute(
        """UPDATE public.profiles p SET role = %s, display_name = %s
           FROM auth.users u WHERE u.id = p.id AND u.email = %s""",
        (role, display, email),
    )
    if cur.rowcount == 0:
        cur.execute(
            """INSERT INTO public.profiles (id, display_name, role)
               SELECT id, %s, %s FROM auth.users WHERE email = %s
               ON CONFLICT (id) DO UPDATE SET role = EXCLUDED.role""",
            (display, role, email),
        )
        print(f"  + profile inserted for {email} ({role})")
    else:
        print(f"  = {email} -> {role}")

print("== premium entitlements ==")
cur.execute("SELECT id FROM auth.users WHERE email = %s",
            ("student.premium@e2e.na9ranal3ab.test",))
row = cur.fetchone()
if not row:
    sys.exit("student.premium not found in auth.users - run ensure-test-users.mjs first")
uid = row[0]
for pid in PREMIUM_PARCOURS:
    cur.execute(
        """INSERT INTO public.parcours_entitlements (user_id, parcours_id, source, expires_at)
           SELECT %s, %s, 'purchase', NULL
           WHERE NOT EXISTS (
             SELECT 1 FROM public.parcours_entitlements e
             WHERE e.user_id = %s AND e.parcours_id = %s
               AND e.revoked_at IS NULL
               AND (e.expires_at IS NULL OR e.expires_at > now()))""",
        (uid, pid, uid, pid),
    )
    print(f"  {'+' if cur.rowcount else '='} {pid}")

if do_reset:
    print("== gameplay reset (mirror of reset-gameplay.mjs) ==")
    for t in GAMEPLAY_TABLES:
        try:
            cur.execute(f'DELETE FROM public."{t}"')
            print(f"  - cleared {t} ({cur.rowcount})")
        except psycopg.Error as e:
            print(f"  - skip {t} ({e.sqlstate})")
    cur.execute(
        """UPDATE public.profiles SET xp = 0, level = 1, yahia_coins = 0,
           current_streak = 0, longest_streak = 0, last_active_date = NULL,
           avatar_slug = NULL"""
    )
    print(f"  - reset profiles progression ({cur.rowcount})")

print("== verification ==")
cur.execute(
    """SELECT u.email, p.role, COALESCE(p.current_parcours_id,'-')
       FROM auth.users u JOIN public.profiles p ON p.id = u.id
       WHERE u.email LIKE %s ORDER BY u.email""", ("%e2e.na9ranal3ab.test",))
for r in cur.fetchall():
    print(f"  user {r[0]}  role={r[1]}  parcours={r[2]}")
cur.execute(
    """SELECT e.parcours_id, e.source, e.expires_at IS NULL, e.revoked_at IS NULL
       FROM public.parcours_entitlements e WHERE e.user_id = %s""", (uid,))
for r in cur.fetchall():
    print(f"  entitlement {r[0]} source={r[1]} perpetual={r[2]} live={r[3]}")
for t in ("themes", "grades", "subjects", "chapters", "exercises", "questions",
          "parcours", "shop_items", "badges"):
    cur.execute(f'SELECT count(*) FROM public."{t}"')
    print(f"  count {t}: {cur.fetchone()[0]}")

conn.close()
print("OK")
