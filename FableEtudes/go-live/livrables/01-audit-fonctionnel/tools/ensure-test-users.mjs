/**
 * C1 audit tool — ensure the 4 e2e accounts exist in the TEST project's auth.
 * Workaround for the broken repo seed (admin_grant_parcours raises 'Unauthorized'
 * for any service key since the entitlements pivot 20260608120000 — see GAP-011).
 * Auth admin API only (works fine with the sb_secret key); roles & entitlements
 * are applied by fix-test-seed.py (direct SQL). Idempotent.
 *
 * Run:  node go-live/livrables/01-audit-fonctionnel/tools/ensure-test-users.mjs
 */
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";

const REPO = "D:/11-coding/YahiaAcademy/yahia-quest-arena";
const require = createRequire(`${REPO}/package.json`);
const { createClient } = require("@supabase/supabase-js");

const env = {};
for (const line of readFileSync(`${REPO}/.env.test`, "utf8").split(/\r?\n/)) {
  const m = line.match(/^([A-Z0-9_]+)\s*=\s*"?([^"]*)"?\s*$/);
  if (m) env[m[1]] = m[2];
}
const URL = env.SUPABASE_URL;
const KEY = env.SUPABASE_SERVICE_ROLE_KEY;
const PASSWORD = env.E2E_USER_PASSWORD;
if (!URL || !KEY || !PASSWORD) throw new Error("Incomplete .env.test");
if (URL.includes("fasrenmmrkqjoobrztbp")) throw new Error("Refusing: this is PRODUCTION");

const admin = createClient(URL, KEY, { auth: { persistSession: false } });

const USERS = [
  { email: "student.free@e2e.na9ranal3ab.test", display: "Free Student" },
  { email: "student.premium@e2e.na9ranal3ab.test", display: "Premium Student" },
  { email: "parent@e2e.na9ranal3ab.test", display: "Test Parent" },
  { email: "admin@e2e.na9ranal3ab.test", display: "Test Admin" },
];

async function findUserByEmail(email) {
  for (let page = 1; page <= 20; page++) {
    const { data, error } = await admin.auth.admin.listUsers({ page, perPage: 200 });
    if (error) throw error;
    const found = data.users.find((u) => u.email?.toLowerCase() === email.toLowerCase());
    if (found) return found;
    if (data.users.length < 200) break;
  }
  return null;
}

const ids = {};
for (const u of USERS) {
  const existing = await findUserByEmail(u.email);
  if (existing) {
    const { error } = await admin.auth.admin.updateUserById(existing.id, {
      password: PASSWORD,
      email_confirm: true,
      user_metadata: { display_name: u.display },
    });
    if (error) throw error;
    ids[u.email] = existing.id;
    console.log(`= ${u.email} (existing)`);
  } else {
    const { data, error } = await admin.auth.admin.createUser({
      email: u.email,
      password: PASSWORD,
      email_confirm: true,
      user_metadata: { display_name: u.display },
    });
    if (error) throw error;
    ids[u.email] = data.user.id;
    console.log(`+ ${u.email} (created)`);
  }
}
console.log(JSON.stringify(ids, null, 2));
