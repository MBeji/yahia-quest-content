// C2/S2 — tests de charge vs TEST (jamais prod). Cibles D1 :
//   100 utilisateurs simultanés (navigation), pic 500 soumissions/h,
//   p95 < 1 s sur submit_exercise_attempt, p95 < 2 s sur les lectures dashboard.
// Modes (env MODE) : smoke (sanité, ~40 s) · target (validation D1, ~5 min)
//                  · stress (écritures ×5 = 2500/h, ~4 min)
// Usage : ./bin/k6.exe run -e MODE=target --summary-export data/summary-target.json k6-main.js
import http from "k6/http";
import { check, sleep } from "k6";
import { SharedArray } from "k6/data";

const DATA = JSON.parse(open("./data/run-data.json"));
if (DATA.url.includes("fasrenmmrkqjoobrztbp")) throw new Error("Refusing: production");

const users = new SharedArray("users", () => DATA.users);
const exercises = new SharedArray("exercises", () => DATA.exercises);
const MODE = __ENV.MODE || "smoke";

const SCENARIOS = {
  smoke: {
    browse: { executor: "constant-vus", vus: 2, duration: "30s", exec: "browse" },
    quests: {
      executor: "per-vu-iterations", vus: 2, iterations: 1, maxDuration: "40s", exec: "quest",
    },
  },
  target: {
    browse: {
      executor: "ramping-vus", exec: "browse",
      stages: [
        { duration: "45s", target: 100 },
        { duration: "3m30s", target: 100 },
        { duration: "15s", target: 0 },
      ],
    },
    quests: {
      // 9/min ≈ 540/h, légèrement au-dessus du pic D1 (500/h)
      executor: "constant-arrival-rate", exec: "quest",
      rate: 9, timeUnit: "1m", duration: "4m30s",
      preAllocatedVUs: 15, maxVUs: 40,
    },
  },
  stress: {
    browse: {
      executor: "constant-vus", vus: 100, duration: "3m30s", exec: "browse",
    },
    quests: {
      // ×5 le pic D1 : ~2500/h ≈ 42/min — cherche le plafond
      executor: "constant-arrival-rate", exec: "quest",
      rate: 42, timeUnit: "1m", duration: "3m30s",
      preAllocatedVUs: 40, maxVUs: 80,
    },
  },
};

export const options = {
  scenarios: SCENARIOS[MODE],
  thresholds: {
    // Cibles D1
    "http_req_duration{op:submit}": ["p(95)<1000"],
    "http_req_duration{op:dashboard}": ["p(95)<2000"],
    "http_req_duration{op:leaderboard}": ["p(95)<2000"],
    "checks": ["rate>0.98"],
  },
  summaryTrendStats: ["avg", "med", "p(90)", "p(95)", "p(99)", "max"],
};

function headers(token, tags) {
  return {
    headers: {
      apikey: DATA.anon,
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
      Prefer: "return=representation",
    },
    tags,
  };
}

function user() {
  return users[(__VU - 1) % users.length];
}

// Reproduit getDashboardPrimary (4 requêtes en parallèle, comme le Promise.all
// du server fn) puis le leaderboard (profiles triés par xp).
export function browse() {
  const u = user();
  const uid = u.id; // l'app tire l'uid du JWT — pas d'appel auth par page
  const base = `${DATA.url}/rest/v1`;
  const h = headers(u.token, { op: "dashboard" });
  const res = http.batch([
    ["GET", `${base}/profiles?select=*&id=eq.${uid}`, null, h],
    ["GET", `${base}/subjects?select=*&order=display_order`, null, h],
    [
      "GET",
      `${base}/attempts?select=subject_id,score_pct,xp_earned,completed_at,exercise_id&user_id=eq.${uid}&order=completed_at.desc&limit=20`,
      null,
      h,
    ],
    ["GET", `${base}/attempts?select=subject_id,score_pct,xp_earned&user_id=eq.${uid}`, null, h],
  ]);
  check(res[0], { "dashboard 200": (r) => r.status === 200 });
  check(res[1], { "subjects 200": (r) => r.status === 200 });

  sleep(1 + Math.random() * 2);

  const lb = http.get(
    `${base}/profiles?select=id,display_name,hero_class,level,xp,current_streak,avatar_tier&order=xp.desc&limit=50`,
    headers(u.token, { op: "leaderboard" }),
  );
  check(lb, { "leaderboard 200": (r) => r.status === 200 });

  sleep(1 + Math.random() * 3);
}

// Parcours de quête réel : start_exercise_session -> temps de lecture
// (>= 4 s/question pour passer le gate anti-rush) -> submit_exercise_attempt.
export function quest() {
  const u = users[Math.floor(Math.random() * users.length)];
  const ex = exercises[Math.floor(Math.random() * exercises.length)];
  const base = `${DATA.url}/rest/v1/rpc`;

  const start = http.post(
    `${base}/start_exercise_session`,
    JSON.stringify({ p_exercise_id: ex.id }),
    headers(u.token, { op: "start" }),
  );
  const ok = check(start, { "start 200": (r) => r.status === 200 });
  if (!ok) return;
  const sessionId = JSON.parse(start.body)[0].session_id;

  sleep(ex.n * 4 + 1 + Math.random() * 3); // gate anti-rush : >= 4 s/question

  const submit = http.post(
    `${base}/submit_exercise_attempt`,
    JSON.stringify({ p_session_id: sessionId, p_exercise_id: ex.id, p_answers: ex.answers }),
    headers(u.token, { op: "submit" }),
  );
  check(submit, {
    "submit 200": (r) => r.status === 200,
    "submit scored": (r) => r.status === 200 && JSON.parse(r.body).scorePct !== undefined,
  });
}
