import { pathToFileURL } from "node:url";
const { chromium } = await import(pathToFileURL("/home/user/eng-gisement/node_modules/playwright/index.mjs").href);
const [,,src,dst,w]=process.argv;
const b=await chromium.launch({executablePath:"/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args:["--no-sandbox"]}); const pg=await b.newPage({viewport:{width:Number(w||760),height:600},deviceScaleFactor:2});
await pg.goto("file://"+src); await pg.screenshot({path:dst,fullPage:true}); await b.close();
