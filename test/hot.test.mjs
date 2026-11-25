// Raman Fox: Foxhole's hot config channel (src/hot.ts) is switched off. Nothing is fetched, a hot.json kept on disk is
// never read, and the built-in values hold.
import assert from "node:assert";
import { mkdirSync, mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const home = mkdtempSync(join(tmpdir(), "ramanfox-hot-"));
process.env.HOME = home;
process.env.USERPROFILE = home;
mkdirSync(join(home, ".config", "foxhole-vpn"), { recursive: true });
writeFileSync(join(home, ".config", "foxhole-vpn", "hot.json"), JSON.stringify({ data: { issued: new Date().toISOString(), notice: "x" }, sig: "x" }));

const { HOT_DISABLED, hot, newNotice, refreshHot } = await import("../dist/hot.js");
assert.equal(HOT_DISABLED, true);
const realFetch = globalThis.fetch;
let fetched = 0;
globalThis.fetch = (...a) => (fetched++, realFetch(...a));
await refreshHot();
globalThis.fetch = realFetch;
assert.equal(fetched, 0, "nothing fetched");
assert.equal(hot(), null, "the built-in values");
assert.equal(newNotice(), null, "no notice");
console.log("ok - hot config off: nothing fetched, nothing read, the built-in values hold");
