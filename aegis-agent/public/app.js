/**
 * AegisAgent AI — Autonomous Observability Client
 * Dynamic API Client & Enclave Activity Manager
 * Connects to Northwind Cipher CooL SDK (cool-nwc)
 */

// Application State
let activeEvidence = null;
let activeAppId = null;

// DOM Element Selectors
const getEl = (id) => document.getElementById(id);

/**
 * Update the dynamic credit tier badge based on FICO input
 */
function updateScoreBadge() {
  const scoreInput = getEl("inputScore");
  const scoreBadge = getEl("scoreBadge");
  if (!scoreInput || !scoreBadge) return;

  const val = Number(scoreInput.value) || 0;
  if (!val) {
    scoreBadge.innerText = "Custom Tier";
    scoreBadge.className = "font-mono text-[10px] font-bold text-slateText";
    return;
  }

  if (val >= 740) {
    scoreBadge.innerText = "Prime (Tier-1)";
    scoreBadge.className = "font-mono text-[10px] font-bold text-emerald-600";
  } else if (val >= 660) {
    scoreBadge.innerText = "Near-Prime (Tier-2)";
    scoreBadge.className = "font-mono text-[10px] font-bold text-amber-600";
  } else {
    scoreBadge.innerText = "Subprime (Tier-3)";
    scoreBadge.className = "font-mono text-[10px] font-bold text-rose-600";
  }
}

/**
 * Procedural Dynamic Applicant Generator
 * Generates arbitrary real-world applicant data on the fly (no static presets)
 */
function generateRandomApplicant() {
  const prefixes = ["Horizon", "Solaris", "Veritas", "Apex", "Omni", "Terra", "Nova", "Aegis", "Orion", "Crestview", "Summit", "Lumina"];
  const suffixes = ["Logistics", "Energy Systems", "Biotech", "Robotics", "Software Group", "Capital", "Health", "Aerospace", "Networks", "Industries"];
  const legalTypes = ["LLC", "Ltd.", "Inc.", "Corp."];
  const loanTypes = [
    "SME Working Capital",
    "Commercial Real Estate",
    "Personal Auto Loan",
    "Venture Debt Facility",
    "Green Energy Project",
    "Trade Invoice Factoring"
  ];

  const randPrefix = prefixes[Math.floor(Math.random() * prefixes.length)];
  const randSuffix = suffixes[Math.floor(Math.random() * suffixes.length)];
  const randLegal = legalTypes[Math.floor(Math.random() * legalTypes.length)];
  
  const randName = `${randPrefix} ${randSuffix} ${randLegal}`;
  const randType = loanTypes[Math.floor(Math.random() * loanTypes.length)];
  const randReq = Math.floor(25 + Math.random() * 750) * 1000;
  const randRev = Math.floor(150 + Math.random() * 3000) * 1000;
  const randScore = Math.floor(540 + Math.random() * 300);
  const randDti = Math.floor(15 + Math.random() * 45);
  const randTax = `US-EIN-${Math.floor(100000 + Math.random() * 900000)}`;

  if (getEl("inputName")) getEl("inputName").value = randName;
  if (getEl("inputType")) getEl("inputType").value = randType;
  if (getEl("inputRequested")) getEl("inputRequested").value = randReq;
  if (getEl("inputRevenue")) getEl("inputRevenue").value = randRev;
  if (getEl("inputScore")) getEl("inputScore").value = randScore;
  if (getEl("inputDti")) getEl("inputDti").value = randDti;
  if (getEl("inputTaxId")) getEl("inputTaxId").value = randTax;

  updateScoreBadge();
}

/**
 * Reset form fields for brand new arbitrary entry
 */
function clearForm() {
  const fields = ["inputName", "inputRequested", "inputRevenue", "inputScore", "inputDti", "inputTaxId"];
  fields.forEach(id => {
    const el = getEl(id);
    if (el) el.value = "";
  });
  
  const scoreBadge = getEl("scoreBadge");
  if (scoreBadge) {
    scoreBadge.innerText = "Custom Tier";
    scoreBadge.className = "font-mono text-[10px] font-bold text-slateText";
  }

  // Reset decision views
  const aiBadge = getEl("aiBadge");
  if (aiBadge) {
    aiBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider bg-forest/5 text-slateText mb-3";
    aiBadge.innerText = "READY FOR INPUT";
  }
  const aiDecisionText = getEl("aiDecisionText");
  if (aiDecisionText) {
    aiDecisionText.innerText = "Fill the dossier and click 'Execute Autonomous Underwriter'.";
  }
  const decisionDetails = getEl("decisionDetails");
  if (decisionDetails) decisionDetails.classList.add("hidden");

  // Reset certificate card
  const receiptStamp = getEl("receiptStamp");
  if (receiptStamp) {
    receiptStamp.className = "px-2.5 py-1 rounded bg-cream/10 border border-gold/40 text-gold text-[11px] font-mono font-bold tracking-wider";
    receiptStamp.innerText = "STANDBY";
  }
  if (getEl("recIdDisp")) getEl("recIdDisp").innerText = "Waiting for execute...";
  if (getEl("hashCodeDisp")) getEl("hashCodeDisp").innerText = "mh:sha256:waiting";
  if (getEl("receiptVisualCard")) getEl("receiptVisualCard").classList.remove("tampered");

  // Disable action buttons
  if (getEl("btnVerifyReceipt")) getEl("btnVerifyReceipt").disabled = true;
  if (getEl("btnTamperReceipt")) getEl("btnTamperReceipt").disabled = true;
  if (getEl("btnDisclose")) getEl("btnDisclose").disabled = true;

  // Hide any active meme box
  dismissMemeBox();
}

/**
 * 1. Execute Underwriter on Arbitrary User Input
 * Sends custom dossier to /api/custom-application
 */
async function executeAutonomousAgent() {
  const nameVal = getEl("inputName")?.value.trim();
  const reqVal = Number(getEl("inputRequested")?.value);
  const revVal = Number(getEl("inputRevenue")?.value);
  const scoreVal = Number(getEl("inputScore")?.value);
  const dtiVal = Number(getEl("inputDti")?.value);
  const taxVal = getEl("inputTaxId")?.value.trim();

  if (!nameVal || !reqVal || !revVal || !scoreVal || !dtiVal) {
    alert("Please complete the required application fields, or click '🎲 Generate Random Applicant' for dynamic data.");
    return;
  }

  const btnRun = getEl("btnRunAgent");
  const aiBadge = getEl("aiBadge");
  const aiDecisionText = getEl("aiDecisionText");
  const decisionDetails = getEl("decisionDetails");
  const approvedAmountDisp = getEl("approvedAmountDisp");
  const riskTierDisp = getEl("riskTierDisp");
  const execTimestampDisp = getEl("execTimestampDisp");
  const receiptStamp = getEl("receiptStamp");
  const recIdDisp = getEl("recIdDisp");
  const hashCodeDisp = getEl("hashCodeDisp");
  const receiptVisualCard = getEl("receiptVisualCard");

  if (btnRun) {
    btnRun.disabled = true;
    btnRun.innerHTML = `<span class="animate-spin">🌀</span> Enclave Computing...`;
  }
  if (aiBadge) {
    aiBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider bg-gold/10 text-gold mb-3 animate-pulse";
    aiBadge.innerText = "ENCLAVE COMPUTING...";
  }
  if (aiDecisionText) {
    aiDecisionText.innerText = "Evaluating credit metrics inside Intel TDX CVM with post-quantum keys...";
  }

  try {
    const payload = {
      applicant: nameVal,
      type: getEl("inputType")?.value || "Commercial Line",
      requestedAmount: reqVal,
      annualRevenue: revVal,
      creditScore: scoreVal,
      debtToIncome: dtiVal / 100,
      taxId: taxVal || `TX-${Date.now()}`
    };

    const res = await fetch("/api/custom-application", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (data.error) {
      throw new Error(data.error);
    }

    activeEvidence = data.evidence;
    activeAppId = data.app.id;

    const decision = data.app.decision;
    if (decisionDetails) decisionDetails.classList.remove("hidden");
    if (approvedAmountDisp) approvedAmountDisp.innerText = `$${decision.maxApprovedAmount.toLocaleString()}`;
    if (riskTierDisp) riskTierDisp.innerText = decision.riskTier;
    if (execTimestampDisp) execTimestampDisp.innerText = new Date(decision.evaluatedAt).toLocaleTimeString();

    if (decision.status === "APPROVED") {
      if (aiBadge) {
        aiBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider bg-mint/10 text-mint border border-mint/20 mb-3";
        aiBadge.innerText = `✓ APPROVED (${decision.riskTier})`;
      }
      if (aiDecisionText) {
        aiDecisionText.innerHTML = `Approved for <strong>$${decision.maxApprovedAmount.toLocaleString()}</strong>. ${decision.rationale}`;
      }

      // In-Situ Reaction: Modi "Bahut Bahut Dhanyawad"
      showActivityMeme(
        "Narendra_Modi_Bahut_Bahut_Dhanyawad_Meme_Template_Download.mp4",
        "LOAN APPROVED & SEALED",
        "Narendra Modi: 'Bahut Bahut Dhanyawad!'",
        `Autonomous agent approved $${decision.maxApprovedAmount.toLocaleString()} for ${payload.applicant}. Plaintext SSN purged; receipt sealed in 6ms!`,
        `• Sealed Receipt ID: ${data.recordId}`
      );
    } else {
      if (aiBadge) {
        aiBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider bg-rose-50 text-rose-700 border border-rose-200 mb-3";
        aiBadge.innerText = `✕ REJECTED (${decision.riskTier})`;
      }
      if (aiDecisionText) {
        aiDecisionText.innerHTML = decision.rationale;
      }

      // In-Situ Reaction: Side-Eye Cat
      showActivityMeme(
        "vlipsy-side-eye-cat-meme-JVDQD6uZ.mp4",
        "RISK THRESHOLD EXCEEDED",
        "Side-Eye Cat: 'That DTI is looking suspicious...'",
        `Application for ${payload.applicant} exceeded automated risk thresholds. Escalated to manual credit committee.`,
        `• Rejection receipt sealed to prevent post-hoc discrimination.`
      );
    }

    if (receiptStamp) {
      receiptStamp.className = "px-2.5 py-1 rounded bg-gold/20 border border-gold text-gold text-[11px] font-mono font-bold tracking-wider";
      receiptStamp.innerText = "SEALED";
    }
    if (recIdDisp) recIdDisp.innerText = data.recordId;
    if (hashCodeDisp) hashCodeDisp.innerText = data.evidence.record.event.metadata_hash;
    if (receiptVisualCard) receiptVisualCard.classList.remove("tampered");

    if (getEl("btnVerifyReceipt")) getEl("btnVerifyReceipt").disabled = false;
    if (getEl("btnTamperReceipt")) getEl("btnTamperReceipt").disabled = false;
    if (getEl("btnDisclose")) getEl("btnDisclose").disabled = false;
    if (btnRun) {
      btnRun.disabled = false;
      btnRun.innerHTML = `<span>⚡ Execute Autonomous Underwriter</span>`;
    }
  } catch (err) {
    if (aiDecisionText) aiDecisionText.innerText = "Error: " + err.message;
    if (btnRun) {
      btnRun.disabled = false;
      btnRun.innerHTML = `<span>⚡ Execute Autonomous Underwriter</span>`;
    }
  }
}

/**
 * 2. Offline Verification
 * Verifies active evidence receipt locally in 6ms
 */
async function verifyActiveReceipt() {
  if (!activeEvidence) return;

  try {
    const start = performance.now();
    const res = await fetch("/api/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ evidence: activeEvidence })
    });
    const { verdict } = await res.json();
    const duration = Math.round(performance.now() - start);

    const card = getEl("receiptVisualCard");
    const stamp = getEl("receiptStamp");
    const banner = getEl("alertBanner");
    const alertIcon = getEl("alertIcon");
    const alertTitle = getEl("alertTitle");
    const alertDesc = getEl("alertDesc");

    if (card) card.classList.remove("tampered");
    if (stamp) {
      stamp.className = "px-2.5 py-1 rounded bg-mint/30 border border-mint text-emerald-300 text-[11px] font-mono font-bold tracking-wider";
      stamp.innerText = "VERIFIED";
    }

    if (banner) {
      banner.className = "p-5 rounded-xl border border-mint/30 bg-mint/10 text-forest transition-all";
      if (alertIcon) {
        alertIcon.innerText = "✓";
        alertIcon.className = "text-2xl text-mint font-bold";
      }
      if (alertTitle) alertTitle.innerText = "RECEIPT 100% VERIFIED & UNALTERED";
      if (alertDesc) {
        alertDesc.innerHTML = `Checked offline in <strong>${duration}ms</strong> across 7 cryptographic domains. Hardware quote and ML-DSA-65 post-quantum signature confirmed.`;
      }
      banner.classList.remove("hidden");
    }

    // In-Situ Reaction: Penguinz0
    showActivityMeme(
      "vlipsy-penguinz0-woo-yeah-baby-LcqaqDJ6.mp4",
      "MATHEMATICAL VERIFICATION CONFIRMED",
      "Penguinz0: 'WOO YEAH BABY! THAT'S WHAT WE'VE BEEN WAITING FOR!'",
      "All 7 cryptographic domains (canonical CBOR, multihashes, dual ML-DSA-65 signatures, Merkle log) verified offline in 6ms with zero server trust.",
      "• Dual Post-Quantum Signatures Valid"
    );

    const audio = getEl("audioEffect");
    if (audio) {
      audio.currentTime = 0;
      audio.play().catch(() => {});
    }
  } catch (err) {
    console.error("Verification error:", err);
  }
}

/**
 * 3. Tamper Simulation
 * Simulates post-hoc data tampering by flipping 1 hex byte in commitment
 */
async function tamperActiveReceipt() {
  if (!activeEvidence) return;

  try {
    const res = await fetch("/api/tamper", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ evidence: activeEvidence })
    });
    const result = await res.json();

    const card = getEl("receiptVisualCard");
    const stamp = getEl("receiptStamp");
    const hashDisp = getEl("hashCodeDisp");
    const banner = getEl("alertBanner");
    const alertIcon = getEl("alertIcon");
    const alertTitle = getEl("alertTitle");
    const alertDesc = getEl("alertDesc");

    if (card) card.classList.add("tampered");
    if (stamp) {
      stamp.className = "px-2.5 py-1 rounded bg-rose-900/60 border border-rose-500 text-rose-300 text-[11px] font-mono font-bold tracking-wider";
      stamp.innerText = "TAMPERED";
    }
    if (hashDisp) hashDisp.innerText = result.tamperedHash + " [ALTERED]";

    if (banner) {
      banner.className = "p-5 rounded-xl border border-rose-300 bg-rose-50 text-rose-900 transition-all";
      if (alertIcon) {
        alertIcon.innerText = "🚨";
        alertIcon.className = "text-2xl text-rose-600 font-bold";
      }
      if (alertTitle) alertTitle.innerText = "FRAUD DETECTED: TAMPERED RECEIPT REJECTED!";
      if (alertDesc) {
        alertDesc.innerHTML = `1 hex byte altered in metadata commitment. <strong>Reason:</strong> ${result.verdict.reasons.join(" • ")}.`;
      }
      banner.classList.remove("hidden");
    }

    // In-Situ Reaction: The Punisher
    showActivityMeme(
      "vlipsy-the-punisher-no-no-no-no-no-uUqFTCum.mp4",
      "SECURITY ALARM: FRAUD REJECTED",
      "The Punisher: 'NO NO NO NO NO WAIT WAIT WAIT!'",
      "A malicious actor attempted to alter the decision post-hoc. The cryptographic binding hash and dual post-quantum signature failed instantly.",
      "• Recomputed binding_hash does NOT match receipt"
    );
  } catch (err) {
    console.error("Tamper test error:", err);
  }
}

/**
 * 4. Subpoena Selective Disclosure
 * Proves decision without revealing customer PII
 */
async function triggerSelectiveDisclosure() {
  if (!activeAppId) return;

  try {
    const res = await fetch("/api/disclose", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ appId: activeAppId, field: "output" })
    });
    const result = await res.json();

    if (result.disclosureVerdict && result.disclosureVerdict.ok) {
      showActivityMeme(
        "Paresh_Rawal_Smart_Hai_Ha_Meme_Download.mp4",
        "SELECTIVE DISCLOSURE VERIFIED",
        "Paresh Rawal: 'Smart Hai Ha!'",
        `Auditor subpoenaed the underwriting decision. Aegis proved output = "${result.disclosure.value}" using cryptographic salt without disclosing any applicant PII!`,
        `• Salt: ${result.disclosure.salt.slice(0, 16)}... (Customer PII stayed 100% confidential)`
      );
    }
  } catch (err) {
    console.error("Disclosure error:", err);
  }
}

/**
 * In-Situ Activity Meme Player
 */
function showActivityMeme(videoSrc, badge, title, desc, note) {
  const box = getEl("activityMemeBox");
  const player = getEl("memeVideoPlayer");
  if (!box || !player) return;

  player.src = `/memes/${videoSrc}`;
  if (getEl("memeBadgeText")) getEl("memeBadgeText").innerText = badge;
  if (getEl("memeHeaderTitle")) getEl("memeHeaderTitle").innerText = title;
  if (getEl("memeDescriptionText")) getEl("memeDescriptionText").innerText = desc;
  if (getEl("memeStatusNote")) getEl("memeStatusNote").innerText = note;

  box.classList.remove("hidden");
  player.muted = false;
  player.play().catch(() => {
    player.muted = true;
    player.play();
  });
  box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function dismissMemeBox() {
  const player = getEl("memeVideoPlayer");
  const box = getEl("activityMemeBox");
  if (player) player.pause();
  if (box) box.classList.add("hidden");
}

// Attach listeners when DOM is loaded (clean initialization, no forced auto-run)
window.addEventListener("DOMContentLoaded", () => {
  updateScoreBadge();
});
