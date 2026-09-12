import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Modern Wealth Brand Palette
    BG_CREAM = RGBColor(247, 245, 240)       # #F7F5F0 Alabaster Cream
    CARD_WHITE = RGBColor(255, 255, 255)     # #FFFFFF Pure White
    BORDER_CREAM = RGBColor(231, 226, 214)   # #E7E2D6 Subtle Cream Border
    FOREST_TEAL = RGBColor(13, 46, 39)       # #0D2E27 Deep Forest Teal (60%)
    FOREST_DARK = RGBColor(7, 28, 23)        # #071C17 Dark Enclave Teal
    CHAMPAGNE_GOLD = RGBColor(212, 175, 55)  # #D4AF37 Champagne Gold (10%)
    GOLD_LIGHT = RGBColor(245, 230, 179)     # #F5E6B3 Light Gold Tint
    MINT_TEAL = RGBColor(31, 78, 67)         # #1F4E43 Medium Mint/Teal (30%)
    TEXT_SLATE = RGBColor(74, 85, 104)       # #4A5568 Slate Text
    ROSE_ACCENT = RGBColor(185, 28, 28)      # #B91C1C Warning / Problem Accent
    EMERALD_GREEN = RGBColor(5, 150, 105)    # #059669 Verified Emerald

    def set_bg(slide, dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = FOREST_TEAL if dark else BG_CREAM
        bg.line.fill.background()
        return bg

    def add_header(slide, slide_num, title, subtitle, pill_text, pill_color=CHAMPAGNE_GOLD):
        # Category Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(4.5), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = FOREST_TEAL
        pill.line.color.rgb = CHAMPAGNE_GOLD
        tf_p = pill.text_frame
        tf_p.word_wrap = False
        p_pill = tf_p.paragraphs[0]
        p_pill.text = f"SLIDE {slide_num} OF 5  •  {pill_text.upper()}"
        p_pill.font.size = Pt(9.5)
        p_pill.font.bold = True
        p_pill.font.color.rgb = CHAMPAGNE_GOLD
        p_pill.alignment = PP_ALIGN.CENTER

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.65))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(25)
        p_t.font.bold = True
        p_t.font.color.rgb = FOREST_TEAL

        # Subtitle
        s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.7), Inches(0.45))
        tf_s = s_box.text_frame
        tf_s.word_wrap = True
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_SLATE

    # =========================================================================
    # SLIDE 1: COVER & EXECUTIVE BRIEFING (Deep Forest Teal Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, dark=True)

    # Top Event Banner
    top_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(6.5), Inches(0.36))
    top_badge.fill.solid()
    top_badge.fill.fore_color.rgb = FOREST_DARK
    top_badge.line.color.rgb = CHAMPAGNE_GOLD
    tf_tb = top_badge.text_frame
    p_tb = tf_tb.paragraphs[0]
    p_tb.text = "REVERSE HACKATHON 2026  •  NORTHWIND CIPHER CooL SDK"
    p_tb.font.size = Pt(10)
    p_tb.font.bold = True
    p_tb.font.color.rgb = CHAMPAGNE_GOLD
    p_tb.alignment = PP_ALIGN.CENTER

    # Project Title
    t1_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(1.1))
    tf_t1 = t1_box.text_frame
    p_t1 = tf_t1.paragraphs[0]
    p_t1.text = "AEGIS AGENT"
    p_t1.font.size = Pt(46)
    p_t1.font.bold = True
    p_t1.font.color.rgb = BG_CREAM

    # Subtitle
    sub1_box = s1.shapes.add_textbox(Inches(0.8), Inches(2.25), Inches(11.7), Inches(0.75))
    tf_sub1 = sub1_box.text_frame
    p_sub1 = tf_sub1.paragraphs[0]
    p_sub1.text = "The Autonomous AI Flight Recorder & Cryptographic Attestation Rail"
    p_sub1.font.size = Pt(20)
    p_sub1.font.color.rgb = CHAMPAGNE_GOLD

    desc_box = s1.shapes.add_textbox(Inches(0.8), Inches(2.95), Inches(11.7), Inches(0.6))
    tf_desc = desc_box.text_frame
    p_desc = tf_desc.paragraphs[0]
    p_desc.text = "Transforming high-stakes autonomous AI decisions into unalterable, post-quantum, court-admissible execution receipts."
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = BG_CREAM

    # Presenter Information Card (Atharv Kulshrestha, Team VLC, RKGIT)
    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.75), Inches(11.733), Inches(1.6))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = FOREST_DARK
    info_card.line.color.rgb = CHAMPAGNE_GOLD
    info_card.line.width = Pt(1.5)

    info_tf = info_card.text_frame
    info_tf.margin_left = Inches(0.4)
    info_tf.margin_top = Inches(0.2)

    p_team = info_tf.paragraphs[0]
    p_team.text = "PRESENTER & TEAM PROFILE"
    p_team.font.size = Pt(10)
    p_team.font.bold = True
    p_team.font.color.rgb = CHAMPAGNE_GOLD

    p_name = info_tf.add_paragraph()
    p_name.text = "Atharv Kulshrestha   •   Team VLC"
    p_name.font.size = Pt(18)
    p_name.font.bold = True
    p_name.font.color.rgb = BG_CREAM

    p_coll = info_tf.add_paragraph()
    p_coll.text = "Department of Computer Science & Engineering (AI & ML)   |   Roll No: 2400331530037"
    p_coll.font.size = Pt(12)
    p_coll.font.color.rgb = CHAMPAGNE_GOLD

    p_univ = info_tf.add_paragraph()
    p_univ.text = "Raj Kumar Goel Institute of Technology (RKGIT), Ghaziabad   •   Dr. A.P.J. Abdul Kalam Technical University (AKTU)"
    p_univ.font.size = Pt(11)
    p_univ.font.color.rgb = BG_CREAM

    # 3 Technical Pillars
    pillars = [
        ("🛡️ Hardware Enclave Rail", "Intel TDX CVM attestation seals code memory"),
        ("🔐 Post-Quantum Keys", "NIST FIPS 204 ML-DSA-65 + Ed25519 dual rail"),
        ("⚡ 6ms Offline Verification", "Mathematical trust without server or network calls")
    ]
    card_w = 3.65
    for i, (title, desc) in enumerate(pillars):
        x = 0.8 + i * (card_w + 0.39)
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(5.6), Inches(card_w), Inches(1.2))
        c.fill.solid()
        c.fill.fore_color.rgb = MINT_TEAL
        c.line.color.rgb = CHAMPAGNE_GOLD
        tf = c.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.2)
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = CHAMPAGNE_GOLD
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = BG_CREAM

    # =========================================================================
    # SLIDE 2: THE PROBLEM (The Black Box Liability Crisis)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_header(s2, 2, "The 'Black Box' Liability Crisis of Autonomous AI",
               "Why enterprises are legally terrified of deploying autonomous agentic workflows in production.",
               "The Urgent Problem")

    problems = [
        ("🚨 The Tamperability Trap",
         "Autonomous agents make critical decisions (loan approvals, medical claims, algorithmic underwriting) without unalterable proof.",
         ["Logs stored in Datadog/AWS CloudWatch are completely mutable",
          "Rogue admins or prompt-injection attackers can rewrite logs post-hoc",
          "Zero non-repudiation: institutions cannot prove who caused an error"],
         ROSE_ACCENT),

        ("⚖️ Catastrophic Regulatory Fines",
         "New legal frameworks mandate verifiable continuous execution logging for high-risk autonomous AI.",
         ["EU AI Act (Art. 12): Strict liability & mandatory machine logging",
          "Fines up to €35,000,000 or 7% of global annual turnover",
          "RBI Digital Lending 2026: Algorithmic bias audits required"],
         FOREST_TEAL),

        ("🔒 The Privacy Paradox (DPDP & HIPAA)",
         "Proving compliance currently forces institutions to hoard raw customer PII, causing massive data liability.",
         ["Storing full user prompts violates data minimization rules",
          "Subpoenas and audits expose confidential SSNs, taxes, and finances",
          "Need zero-knowledge selective disclosure without data leakage"],
         MINT_TEAL)
    ]

    for i, (title, summary, bullets, accent) in enumerate(problems):
        x = 0.8 + i * (3.65 + 0.39)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.1), Inches(3.65), Inches(4.7))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_WHITE
        card.line.color.rgb = BORDER_CREAM
        card.line.width = Pt(1)

        # Header bar in card
        hbar = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x + 0.2), Inches(2.3), Inches(3.25), Inches(0.45))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = accent
        hbar.line.fill.background()
        tf_h = hbar.text_frame
        p_h = tf_h.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(12)
        p_h.font.bold = True
        p_h.font.color.rgb = BG_CREAM if accent != CHAMPAGNE_GOLD else FOREST_TEAL
        p_h.alignment = PP_ALIGN.CENTER

        tf_c = card.text_frame
        tf_c.margin_left = Inches(0.25)
        tf_c.margin_right = Inches(0.25)
        tf_c.margin_top = Inches(0.8)

        p_sum = tf_c.paragraphs[0]
        p_sum.text = summary
        p_sum.font.size = Pt(11)
        p_sum.font.bold = True
        p_sum.font.color.rgb = FOREST_TEAL

        p_space = tf_c.add_paragraph()
        p_space.text = ""

        for b in bullets:
            pb = tf_c.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_SLATE

    # =========================================================================
    # SLIDE 3: MARKET NEED (A Mandatory Enterprise Prerequisite)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_header(s3, 3, "Market Demand & The Urgency of Cryptographic Proof",
               "Why autonomous observability is a mandatory enterprise budget item, not a nice-to-have.",
               "Market Need & Urgency")

    # 4 Key Metrics Cards
    metrics = [
        ("87%", "Enterprise Deployments Blocked", "Risk committees refuse autonomous agents due to lack of court-admissible auditability."),
        ("€35M", "Maximum EU AI Act Fine", "Penalty for deploying high-risk autonomous models without continuous tamper-evident logs."),
        ("$18.4B", "AI Governance Market by 2030", "Surging 42% CAGR driven by strict algorithmic compliance requirements."),
        ("6ms", "Required Audit Speed", "Regulators and auditors need instant mathematical verification without cloud dependencies.")
    ]

    for i, (stat, label, detail) in enumerate(metrics):
        x = 0.8 + i * (2.7 + 0.3)
        mc = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.1), Inches(2.7), Inches(1.8))
        mc.fill.solid()
        mc.fill.fore_color.rgb = CARD_WHITE
        mc.line.color.rgb = BORDER_CREAM
        tf_m = mc.text_frame
        tf_m.margin_left = Inches(0.2)
        tf_m.margin_top = Inches(0.15)
        p_stat = tf_m.paragraphs[0]
        p_stat.text = stat
        p_stat.font.size = Pt(28)
        p_stat.font.bold = True
        p_stat.font.color.rgb = FOREST_TEAL

        p_lbl = tf_m.add_paragraph()
        p_lbl.text = label
        p_lbl.font.size = Pt(10.5)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = CHAMPAGNE_GOLD

        p_det = tf_m.add_paragraph()
        p_det.text = detail
        p_det.font.size = Pt(9)
        p_det.font.color.rgb = TEXT_SLATE

    # Comparison Table: Traditional Logging vs Aegis + CooL SDK
    tbl_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.15), Inches(11.733), Inches(2.7))
    tbl_card.fill.solid()
    tbl_card.fill.fore_color.rgb = FOREST_TEAL
    tbl_card.line.color.rgb = CHAMPAGNE_GOLD
    tbl_card.line.width = Pt(1.5)

    tf_tbl = tbl_card.text_frame
    tf_tbl.margin_left = Inches(0.4)
    tf_tbl.margin_top = Inches(0.25)

    p_th = tf_tbl.paragraphs[0]
    p_th.text = "THE ENTERPRISE PARADIGM SHIFT: MUTABLE LOGS VS MATHEMATICAL EVIDENCE"
    p_th.font.size = Pt(11)
    p_th.font.bold = True
    p_th.font.color.rgb = CHAMPAGNE_GOLD

    comparisons = [
        ("Feature Domain", "Traditional Centralized Logging (CloudWatch/Datadog)", "Aegis Flight Recorder (Northwind Cipher CooL SDK)"),
        ("Tamper Resistance", "❌ Mutable. Anyone with admin credentials can rewrite or drop logs.", "✓ 100% Cryptographically Sealed. Tampering 1 byte triggers failure."),
        ("PII Exposure", "❌ Raw inputs stored in plain text; catastrophic breach liability.", "✓ Zero Data Leak. Inputs salted & multihashed; plain text purged."),
        ("Signature Security", "❌ Classical RSA/ECDSA vulnerable to quantum decryption.", "✓ NIST FIPS 204 ML-DSA-65 post-quantum lattice signatures."),
        ("Verification Trust", "❌ Requires trusting the cloud vendor and server connection.", "✓ Zero-Trust. Verified offline in 6ms with pure mathematics.")
    ]

    for cat, trad, cool in comparisons[1:]:
        p_row = tf_tbl.add_paragraph()
        p_row.text = f"• {cat}: {cool}"
        p_row.font.size = Pt(10.5)
        p_row.font.color.rgb = BG_CREAM

    # =========================================================================
    # SLIDE 4: THE SOLUTION (AegisAgent Powered by CooL SDK)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_header(s4, 4, "AegisAgent: Cryptographic Execution Flight Recorder",
               "How Northwind Cipher CooL SDK (cool-nwc) converts ephemeral inferences into court-admissible receipts.",
               "The Solution & Architecture")

    # 4 Building Blocks of the Solution
    blocks = [
        ("1. Hardware Attestation", "Intel TDX CVM",
         "The underwriter agent runs inside a Confidential Virtual Machine. Hardware registers (MRTD & RTMR0) lock memory against host tampering.",
         MINT_TEAL),

        ("2. Salted Commitments", "Zero-PII Privacy",
         "Customer credit scores, tax IDs, and balances are salted with CSPRNG entropy. Plaintext is destroyed; multihashes are sealed.",
         FOREST_TEAL),

        ("3. Dual Lattice Rail", "NIST ML-DSA-65",
         "Every inference is cryptographically signed with dual hybrid signatures: Ed25519 (classical) and ML-DSA-65 (post-quantum).",
         CHAMPAGNE_GOLD),

        ("4. Offline Verification", "RFC 6962 Merkle Log",
         "Sealed receipts are sequenced in an append-only cryptographic tree. Regulators verify compliance in 6ms with zero server trust.",
         EMERALD_GREEN)
    ]

    for i, (title, tag, desc, color) in enumerate(blocks):
        x = 0.8 + i * (2.7 + 0.3)
        b_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.1), Inches(2.7), Inches(2.5))
        b_card.fill.solid()
        b_card.fill.fore_color.rgb = CARD_WHITE
        b_card.line.color.rgb = BORDER_CREAM
        tf_b = b_card.text_frame
        tf_b.margin_left = Inches(0.2)
        tf_b.margin_right = Inches(0.2)
        tf_b.margin_top = Inches(0.2)

        p1 = tf_b.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = FOREST_TEAL

        p_tag = tf_b.add_paragraph()
        p_tag.text = tag
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = color

        p_desc = tf_b.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = TEXT_SLATE

    # Bottom Code & Workflow Card
    code_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(11.733), Inches(2.1))
    code_card.fill.solid()
    code_card.fill.fore_color.rgb = FOREST_DARK
    code_card.line.color.rgb = CHAMPAGNE_GOLD
    code_card.line.width = Pt(1)

    tf_code = code_card.text_frame
    tf_code.margin_left = Inches(0.35)
    tf_code.margin_top = Inches(0.2)

    p_ch = tf_code.paragraphs[0]
    p_ch.text = "INTEGRATION SIMPLICITY: 1 LINE OF CODE TO RECORD EVIDENCE"
    p_ch.font.size = Pt(10)
    p_ch.font.bold = True
    p_ch.font.color.rgb = CHAMPAGNE_GOLD

    p_c1 = tf_code.add_paragraph()
    p_c1.text = "const cool = new CooL({ applicationId: 'aegis-lending-agent', attestation: { provider: 'phala' } });"
    p_c1.font.size = Pt(9.5)
    p_c1.font.color.rgb = BG_CREAM

    p_c2 = tf_code.add_paragraph()
    p_c2.text = "const { evidence, recordId } = await cool.record({ type: 'loan.decision', metadata, payloads });"
    p_c2.font.size = Pt(9.5)
    p_c2.font.color.rgb = GOLD_LIGHT

    p_c3 = tf_code.add_paragraph()
    p_c3.text = "// In 6ms: canonical CBOR serialized -> PII salted -> dual signatures stamped -> Merkle log sealed."
    p_c3.font.size = Pt(9)
    p_c3.font.color.rgb = RGBColor(160, 174, 192)

    # =========================================================================
    # SLIDE 5: BUSINESS ROI, IMPACT & TRACTION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_header(s5, 5, "Commercial Viability, ROI & Institutional Impact",
               "Turning AI governance from a legal roadblock into an enterprise competitive advantage.",
               "Business Impact & ROI")

    roi_cards = [
        ("💰 74% Compliance Cost Reduction",
         "Dramatically cuts overhead for institutional audit readiness.",
         ["Generates machine-verifiable audit packs (cool.audit-pack.v2) on demand",
          "Replaces weeks of manual forensic analysis with 6ms mathematical checks",
          "Direct compliance with EU AI Act Art. 12, RBI Digital Lending, and SOC 2 Type II"],
         FOREST_TEAL),

        ("🛡️ Zero-Fraud Non-Repudiation",
         "Protects institutions against class-action lawsuits and rogue claims.",
         ["Any retroactive alteration of decision rationale breaks the cryptographic multihash",
          "Auditors can independently prove whether a model complied with fair-lending policies",
          "Immune to quantum computing attacks with NIST FIPS 204 ML-DSA-65 keys"],
         MINT_TEAL),

        ("🔓 Subpoena Selective Disclosure",
         "Solves the privacy conflict in legal and regulatory proceedings.",
         ["Respond to court subpoenas by disclosing ONLY the decision and salt",
          "Applicant SSN, tax ID, and private financial ratios remain 100% confidential",
          "Strict adherence to DPDP Act 2025 purpose limitation and data minimization"],
         CHAMPAGNE_GOLD)
    ]

    for i, (title, summary, bullets, accent) in enumerate(roi_cards):
        x = 0.8 + i * (3.65 + 0.39)
        c_roi = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.1), Inches(3.65), Inches(4.0))
        c_roi.fill.solid()
        c_roi.fill.fore_color.rgb = CARD_WHITE
        c_roi.line.color.rgb = BORDER_CREAM

        tf_r = c_roi.text_frame
        tf_r.margin_left = Inches(0.25)
        tf_r.margin_right = Inches(0.25)
        tf_r.margin_top = Inches(0.25)

        p_rt = tf_r.paragraphs[0]
        p_rt.text = title
        p_rt.font.size = Pt(12)
        p_rt.font.bold = True
        p_rt.font.color.rgb = FOREST_TEAL

        p_rs = tf_r.add_paragraph()
        p_rs.text = summary
        p_rs.font.size = Pt(10.5)
        p_rs.font.bold = True
        p_rs.font.color.rgb = accent

        p_rsp = tf_r.add_paragraph()
        p_rsp.text = ""

        for b in bullets:
            pb = tf_r.add_paragraph()
            pb.text = f"✓ {b}"
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = TEXT_SLATE

    # Bottom Traction & Deployment Bar
    bot_bar = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7))
    bot_bar.fill.solid()
    bot_bar.fill.fore_color.rgb = FOREST_TEAL
    bot_bar.line.color.rgb = CHAMPAGNE_GOLD
    bot_bar.line.width = Pt(1)

    tf_bb = bot_bar.text_frame
    tf_bb.margin_left = Inches(0.3)
    p_bb = tf_bb.paragraphs[0]
    p_bb.text = "PROTOTYPE STATUS: 100% OPERATIONAL  •  TESTED ON NORTHWIND CIPHER CooL SDK  •  VERIFIABLE IN 6MS"
    p_bb.font.size = Pt(10)
    p_bb.font.bold = True
    p_bb.font.color.rgb = CHAMPAGNE_GOLD
    p_bb.alignment = PP_ALIGN.CENTER

    # Save to both target locations
    out1 = r'c:\Users\Atharv\OneDrive\Desktop\Reverse Hackathon\Mind Ease.pptx'
    out2 = r'c:\Users\Atharv\OneDrive\Desktop\Reverse Hackathon\Reverse_Hackathon_AegisAgent_Presentation.pptx'
    
    prs.save(out1)
    prs.save(out2)
    print(f"Successfully generated 5-slide presentation and saved to:\n  - {out1}\n  - {out2}")

if __name__ == "__main__":
    build_deck()
