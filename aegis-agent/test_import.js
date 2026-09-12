import { CooL, verifyEvidence } from "cool-nwc";
import { buildAuditPack, disclose, verifyDisclosure } from "cool-nwc/phala";

console.log("Imports successful!");
const cool = new CooL({ applicationId: "test-app" });
const { evidence } = await cool.record({
  type: "test.event",
  metadata: { test: true },
  payloads: { secret: "confidential-data" }
});
const verdict = await verifyEvidence(evidence);
console.log("Verdict OK:", verdict.ok);
await cool.close();
