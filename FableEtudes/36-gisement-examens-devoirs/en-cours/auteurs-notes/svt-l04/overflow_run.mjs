// Lance check-overflow.mjs du moteur avec le Chromium disponible ici (révision 1194) : on greffe executablePath sur chromium.launch.
import { createRequire } from "node:module";
const require = createRequire("/home/user/yahia-quest-arena/package.json");
const pw = require("playwright");
const orig = pw.chromium.launch.bind(pw.chromium);
pw.chromium.launch = (opts = {}) => orig({ ...opts, executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args: ["--no-sandbox", ...(opts.args || [])] });
process.argv = [process.argv[0], "/home/user/yahia-quest-arena/scripts/content/svg/check-overflow.mjs", ...process.argv.slice(2)];
await import("file:///home/user/yahia-quest-arena/scripts/content/svg/check-overflow.mjs");
