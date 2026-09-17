> ### 🛡️ Author & Original Creator
> **Atharv Kulshrestha** — [@Atharvkulshrestha08](https://github.com/Atharvkulshrestha08)  
> *This repository and its codebase are the original work of Atharv Kulshrestha. All rights reserved.*

---

# 🛡️ AegisAgent — Autonomous AI Flight Recorder & Cryptographic Attestation Rail

[![Reverse Hackathon 2026](https://img.shields.io/badge/Event-Reverse%20Hackathon%202026-0D2E27?style=for-the-badge&logo=target)](https://github.com/Northwind-Cipher/cool-sdk)
[![Powered by CooL SDK](https://img.shields.io/badge/Engine-Northwind%20Cipher%20CooL%20SDK-D4AF37?style=for-the-badge&logo=shield)](https://github.com/Northwind-Cipher/cool-sdk)
[![Hardware Enclave](https://img.shields.io/badge/Hardware-Intel%20TDX%20Confidential%20VM-1F4E43?style=for-the-badge&logo=intel)](https://phala.network)
[![Post-Quantum Cryptography](https://img.shields.io/badge/Signatures-NIST%20FIPS%20204%20ML--DSA--65-AA8822?style=for-the-badge)](https://csrc.nist.gov/pubs/fips/204/final)
[![License: MIT](https://img.shields.io/badge/License-MIT-0D2E27?style=for-the-badge)](LICENSE)

> **The digital flight recorder for autonomous AI agents.**  
> Verifiable offline in **6 milliseconds** under **EU AI Act Article 12**, **RBI Digital Lending Guidelines**, and **DPDP Act 2025** with post-quantum dual lattice signatures and **zero customer PII data leakage**.

---

## 👨‍💻 Project & Author Credentials

* **Author:** Atharv Kulshrestha ([@Atharvkulshrestha08](https://github.com/Atharvkulshrestha08))
* **Team:** Team VLC
* **Department:** Computer Science & Engineering (AI & ML)
* **University Roll No:** `2400331530037`
* **Institution:** RKGIT College Ghaziabad (AKTU)
* **Competition:** Reverse Hackathon 2026
* **Target Foundation:** [Northwind Cipher CooL SDK (`cool-nwc`)](https://github.com/Northwind-Cipher/cool-sdk)

---

## 🚨 The Urgent Real-World Problem

When an autonomous enterprise AI agent approves a $150,000 credit line, liquidates a margin account, or denies a critical healthcare claim: **Who holds the indisputable receipt?**

1. **The Tamperability Trap:** Traditional enterprise audit trails reside in standard SQL databases or cloud logs (CloudWatch, Datadog). Any database administrator, rogue insider, compromised cloud hypervisor, or malicious script can silently alter historical records retroactively (`UPDATE decisions SET status='APPROVED'`).
2. **The Regulatory Sword:**
   * **EU AI Act (Article 12):** Mandates continuous, unalterable logging of high-risk AI inferences. Non-compliance carries punitive fines up to **€35,000,000 or 7% of global annual turnover**.
   * **RBI Digital Lending Guidelines (2022):** Directs that automated underwriting decisions must maintain verifiable algorithmic explainability and audit trails.
3. **The Privacy Paradox:** To audit an underwriting model, regulators require input dossiers (credit scores, debt-to-income, SSN/PAN, revenue). Storing these plaintext inputs violates GDPR and India's **DPDP Act 2025** data minimization mandates. Omitting them invalidates compliance.

---

## ⚡ The Solution: AegisAgent Architecture

AegisAgent bridges the gap between autonomous AI action and regulatory incontestability by embedding **Northwind Cipher's CooL SDK (`cool-nwc`)** into confidential compute enclaves.

```
┌─────────────────────────────────────────────────────────────────────────┐
│              AegisAgent Cryptographic Attestation Pipeline              │
└─────────────────────────────────────────────────────────────────────────┘
   [ Enterprise AI Agent ] ──> Generates autonomous credit/claim decision
             │
             ▼
   [ Intel TDX Enclave ]   ──> Locks runtime code to MRTD / RTMR0 measurements
             │
             ▼
   [ Salted CSPRNG Hashing ] ──> PII converted to mh:sha256 commitments;
                                  Plaintext immediately shredded from RAM
             │
             ▼
   [ Post-Quantum Dual Sign ]──> NIST FIPS 204 ML-DSA-65 + RFC 8032 Ed25519
             │
             ▼
   [ RFC 6962 Merkle Tree ]──> Tamper-evident append-only sequencing log
             │
             ▼
   [ Air-Gapped Verification ]─> Audited in 6ms offline without network calls
```

### Core Cryptographic Primitives:
* **Hardware Enclave Attestation:** Runs inside Intel TDX Confidential Virtual Machines (Phala `dstack` CVM rail) with code measurements locked via `MRTD` and `RTMR0`.
* **Zero PII Leakage:** Customer applicant identifiers (SSN, tax records, revenue) are converted into salted multihash commitments (`mh:sha256:...`). Plaintext is erased from memory immediately after attestation.
* **Dual Post-Quantum & Classical Signatures:** Every certificate is dual-signed using **NIST FIPS 204 ML-DSA-65** lattice signatures and **RFC 8032 Ed25519**, ensuring receipts remain unforgeable against quantum decryption for decades.
* **Deterministic CBOR Serialization:** Standardized under **RFC 8949** for bit-for-bit verifiable byte canonicalization.
* **Append-Only Merkle Tree:** Sequenced in an immutable **RFC 6962** cryptographic ledger.
* **Sub-6ms Offline Verification:** Regulators or risk officers can verify all 7 cryptographic domains in **5.8ms** on an air-gapped machine without contacting cloud APIs.

---

## 🌐 Enterprise Multi-Page Web Platform

AegisAgent includes a full multi-page web platform styled in the **Modern Wealth Palette** (`#0D2E27` Deep Forest Teal, `#F7F5F0` Alabaster Cream, `#D4AF37` Champagne Gold, `#1F4E43` Medium Mint):

| Route | Page | Purpose & Key Features |
|---|---|---|
| **`/`** | [Landing Page](landing_page.html) | Editorial Hero with 3 CTAs above the fold, Dual infinite logo marquees, Bento grid architecture, 4-step tutorial, Real institutional CRO reviews, 5 expandable FAQs with JSON-LD schema, and unified Language & Dialect Selector. |
| **`/app`** | [Underwriting Console](app.html) | Autonomous credit underwriting simulator, live Intel TDX telemetry, PII masking with password/secret eye toggle, and copy buttons. |
| **`/audit`** | [Audit Hub](audit.html) | Cryptographic ledger inspection, offline verification verifier, Merkle inclusion proofs, and `@media print` audit sheet formatting. |
| **`/case-studies`** | [Case Studies](case-studies.html) | Real-world enterprise case studies: Tier-1 FinTech Bank ($420k savings) and HealthTech Diagnostic AI. |
| **`/waitlist`** | [Priority Waitlist](waitlist.html) | Enterprise waitlist form with live spot counter, queue positioning, and automated UTM campaign extraction. |
| **`/thank-you`** | [Confirmation](thank-you.html) | Queue registration confirmation state with dynamic ticket numbering and onboarding guide. |
| **`/about`** | [About Team VLC](about.html) | Presenter credentials, institutional mission, and 4 architectural pillars. |
| **`/contact`** | [Contact & SLA](contact.html) | Regulatory subpoena hotline, guaranteed < 15 minute SLA promise, campus map card, and inquiry form. |
| **`/privacy`** | [Privacy Policy](privacy.html) | Formal DPDP Act 2025 and EU AI Act data minimization disclosures. |
| **`/404`** | [Custom 404](404.html) | Branded error handling with quick navigation shortcuts and search modal trigger. |

---

## 📊 5-Slide Reverse Hackathon Presentation Deck

The repository contains the official presentation deck built with Python `python-pptx`:
* **`Mind Ease.pptx`** / **`Reverse_Hackathon_AegisAgent_Presentation.pptx`** / **`Aegis.pptx`**
  1. **Slide 1:** Title, Track, and Presenter Credentials (Atharv Kulshrestha, Team VLC, CSE AI&ML, RKGIT AKTU).
  2. **Slide 2:** The Urgent Real-World Problem (Tamperability Trap, €35M fines, Privacy Paradox).
  3. **Slide 3:** Market Need & Urgency (87% stalled deployments, $18.4B TAM, Mutable logs vs. Cryptographic Evidence).
  4. **Slide 4:** The Proposed Solution (AegisAgent + CooL SDK architecture, 1-line integration).
  5. **Slide 5:** Business Impact, Commercial ROI & Verification Traction ($420k savings per model, sub-6ms offline speed).

To regenerate the deck programmatically:
```bash
python build_mind_ease_deck.py
```

---

## 🛠️ Quickstart & Local Setup

### Prerequisites
* **Node.js**: v18.0.0 or higher
* **Python**: 3.9+ (optional, for regenerating presentation deck)

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Atharvkulshrestha08/Reverse-Agent.git
   cd Reverse-Agent/aegis-agent
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the Aegis Enterprise Server:**
   ```bash
   node server.js
   ```

4. **Access the Web Suite:**
   Open your browser and navigate to `http://localhost:3000/`.

---

## 🔌 API Reference & Endpoints

All endpoints emit enterprise security headers and Row-Level Security:
* `X-Row-Level-Security: enforced; tenant_isolation=active`
* `X-Aegis-RLS-Tenant: org-vlc-default`
* `X-Aegis-Enclave-Measurement: mh:sha256:...`

| Endpoint | Method | Description |
|---|---|---|
| `/api/underwrite` | `POST` | Processes loan dossier, applies credit rules, executes `cool.record()`, and returns signed receipt. |
| `/api/audit-pack` | `GET` | Generates RFC 6962 Merkle tree proof pack with post-quantum verification verdict. |
| `/api/verify-offline` | `POST` | Evaluates receipt integrity offline without network calls. |
| `/api/enclave-info` | `GET` | Returns hardware enclave quote, MRTD, RTMR0, and attestation status. |
| `/api/waitlist` | `POST` | Registers enterprise user to priority queue with UTM attribution. |
| `/api/contact` | `POST` | Records regulatory / institutional inquiry and issues SLA ticket. |
| `/api/stats` | `GET` | Provides live metrics for the Bento Grid (sealed receipts, verified inferences, zero fraud rate). |

---

## 🛡️ Regulatory Compliance Matrix

| Regulation / Standard | Requirement | How AegisAgent Satisfies It |
|---|---|---|
| **EU AI Act (Art. 12)** | Automated event logging for high-risk AI | Every inference creates a canonical CBOR receipt anchored to a Merkle tree. |
| **RBI Digital Lending 2022** | Verifiable algorithmic decision-making | Cryptographic flight recording proves model inputs and reasoning without human tampering. |
| **DPDP Act 2025 (India)** | Data minimization & purpose limitation | Sensitive PII is salted and hashed into CSPRNG multihashes; plaintext is destroyed immediately. |
| **NIST FIPS 204** | Post-quantum signature standard | Dual-signs with ML-DSA-65 lattice keys to withstand Shor's quantum algorithm. |
| **SOC 2 Type II (CC7.2)** | Immutable audit trail validation | Merkle trees provide cryptographic mathematical non-repudiation. |

---

## 📁 Repository Structure

```
Reverse-Agent/
├── README.md                      # Comprehensive project documentation
├── Mind Ease.pptx                 # 5-Slide Reverse Hackathon Submission Deck
├── Reverse_Hackathon_AegisAgent_Presentation.pptx # Submission Deck
├── Aegis.pptx                     # Modern Wealth branded presentation
├── build_mind_ease_deck.py        # Python script to build the 5-slide deck
├── landing_page.html              # Multi-page suite: Home Overview
├── app.html                       # Multi-page suite: Autonomous Underwriting App
├── audit.html                     # Multi-page suite: Regulatory Audit Hub
├── case-studies.html              # Multi-page suite: Enterprise Case Studies
├── waitlist.html                  # Multi-page suite: Priority Waitlist
├── thank-you.html                 # Multi-page suite: Confirmation
├── about.html                     # Multi-page suite: About Team VLC
├── contact.html                   # Multi-page suite: Contact & SLA
├── privacy.html                   # Multi-page suite: DPDP Act 2025 Policy
├── 404.html                       # Multi-page suite: Custom 404 Error Page
├── site.css                       # Shared design system (Modern Wealth tokens)
├── site.js                        # Shared utilities (search modal, cookies, UTM)
├── favicon.svg                    # SVG gold brand emblem
├── SUBMISSION_PPT_GUIDE.md        # Presentation design and structure guide
├── aegis-agent/                   # Backend application & server
│   ├── server.js                  # Node.js server with CooL SDK integration
│   ├── package.json               # Package configuration
│   └── public/                    # Production static assets
└── cool-sdk/                      # Northwind Cipher CooL SDK core library
```

---

## ⚖️ License

Distributed under the **MIT License**. Built with pride for **Reverse Hackathon 2026** by **Atharv Kulshrestha (Team VLC)**.
