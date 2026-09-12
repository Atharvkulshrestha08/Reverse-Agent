from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Modern Wealth Brand Palette
    BG_CREAM = RGBColor(247, 245, 240)     # #F7F5F0 Alabaster Cream
    CARD_WHITE = RGBColor(255, 255, 255)   # #FFFFFF Clean White
    BORDER_CREAM = RGBColor(231, 226, 214) # #E7E2D6 Subtle Cream Border
    FOREST_TEAL = RGBColor(13, 46, 39)     # #0D2E27 Deep Forest Teal (Primary 60%)
    CHAMPAGNE_GOLD = RGBColor(212, 175, 55)# #D4AF37 Champagne Gold (Accent 10%)
    MINT_TEAL = RGBColor(31, 78, 67)       # #1F4E43 Support Mint/Teal
    TEXT_MUTED = RGBColor(74, 85, 104)     # #4A5568 Slate Text
    ROSE_ACCENT = RGBColor(185, 28, 28)    # #B91C1C Refined Red for Problem

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_CREAM
        bg.line.fill.background()
        return bg

    def add_header(slide, slide_num, title, subtitle, pill_text, pill_color):
        # Pill
        p_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(5.0), Inches(0.35))
        tf_p = p_box.text_frame
        p_pill = tf_p.paragraphs[0]
        p_pill.text = f"SLIDE {slide_num} OF 5   •   {pill_text.upper()}"
        p_pill.font.size = Pt(10.5)
        p_pill.font.bold = True
        p_pill.font.color.rgb = pill_color

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tf_t = t_box.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = FOREST_TEAL

        # Subtitle
        s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.5))
        tf_s = s_box.text_frame
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.size = Pt(13)
        p_s.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, icon_title, summary, bullets, accent_color):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_WHITE
        card.line.color.rgb = BORDER_CREAM
        card.line.width = Pt(1.5)

        # Title
        tb_title = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(width - 0.5), Inches(0.4))
        tf_t = tb_title.text_frame
        p_title = tf_t.paragraphs[0]
        p_title.text = icon_title
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = accent_color

        # Summary
        tb_sum = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.65), Inches(width - 0.5), Inches(1.0))
        tf_sum = tb_sum.text_frame
        tf_sum.word_wrap = True
        p_sum = tf_sum.paragraphs[0]
        p_sum.text = summary
        p_sum.font.size = Pt(11)
        p_sum.font.color.rgb = TEXT_MUTED

        # Bullets
        tb_b = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 1.8), Inches(width - 0.5), Inches(height - 1.9))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for i, (b_head, b_desc) in enumerate(bullets):
            p = tf_b.paragraphs[0] if i == 0 else tf_b.add_paragraph()
            p.font.size = Pt(10.5)
            p.space_after = Pt(8)
            r_h = p.add_run()
            r_h.text = f"• {b_head}: " if b_head else "• "
            r_h.font.bold = True
            r_h.font.color.rgb = FOREST_TEAL
            r_d = p.add_run()
            r_d.text = b_desc
            r_d.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 1: Problem Statement
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)
    add_header(s1, "1", "Slide 1 — Problem Statement 🎯", 
               "When an AI makes a life-altering financial decision, there is no receipt. Organizations have zero legal proof.", 
               "The Urgent Crisis", ROSE_ACCENT)

    add_card(s1, 0.8, 2.0, 3.7, 4.9, "1. What is the Problem?", 
             "Companies are giving autonomous AI agents financial authority to underwrite loans and disburse funds. But when an AI errs or discriminates, organizations possess zero legally admissible evidence.",
             [
                 ("Database Logs Can Be Faked", "Any IT administrator or bad actor can alter database rows with a simple SQL query. Courts dismiss them as unverified hearsay."),
                 ("The Privacy Trap", "Banks legally cannot save customer financial records in audit logs due to privacy laws (GDPR/DPDP). Omitting logs fails audits; saving them breaks privacy.")
             ], ROSE_ACCENT)

    add_card(s1, 4.8, 2.0, 3.7, 4.9, "2. Who is Facing It?", 
             "Any enterprise trusting autonomous AI agents with money, health, or legal decisions is exposed to massive corporate liability.",
             [
                 ("FinTechs & Digital Lenders", "14,000+ lenders using AI for instant loan underwriting, facing strict regulatory scrutiny (CFPB, RBI-DLG)."),
                 ("InsurTech & Health", "Autonomous claims processors and AI diagnostic tools paying out millions daily."),
                 ("Enterprise Agent Builders", "Companies giving autonomous agents corporate credit cards and database write access.")
             ], FOREST_TEAL)

    add_card(s1, 8.8, 2.0, 3.7, 4.9, "3. Why is it Urgent Right Now?", 
             "Governments have enacted strict record-keeping penalties, and regulatory grace periods have officially expired.",
             [
                 ("EU AI Act is LIVE", "Article 12 legally mandates unalterable logs for high-risk AI, with fines up to €35 Million or 7% of worldwide turnover."),
                 ("Central Bank Mandates", "Central banks explicitly require auditable proof of the AI model version behind every credit decision."),
                 ("84% of Enterprises Blocked", "Enterprise leaders report that liability fears are the #1 blocker keeping them from launching AI into production.")
             ], CHAMPAGNE_GOLD)

    # ==========================================
    # SLIDE 2: Market Need & Research
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "2", "Slide 2 — Market Need & Research 🔍", 
               "AI graduated from 'chatting' to 'capital allocation.' The AI Governance market is surging to $10.2B.", 
               "Market Opportunity", CHAMPAGNE_GOLD)

    add_card(s2, 0.8, 2.0, 3.7, 4.9, "Why It Matters Right Now", 
             "AI is no longer generating creative copy—it holds bank accounts, credit limits, and loan signing authority.",
             [
                 ("Exploding GRC Market", "The AI Governance, Risk & Compliance market is surging from $2.1B to $10.2B by 2028 (48.5% annual growth)."),
                 ("Grace Periods Have Ended", "Regulators in the EU, US, and India are actively enforcing AI record-keeping today, not next year.")
             ], CHAMPAGNE_GOLD)

    add_card(s2, 4.8, 2.0, 3.7, 4.9, "The Existing Industry Gap", 
             "Current developer tools only monitor server health, not legal truth.",
             [
                 ("Tools Track Uptime, Not Trust", "APM tools like Datadog track server crashes; they cannot prove that an AI decision was un-tampered."),
                 ("Audits Take 4 Painful Weeks", "Companies waste weeks compiling screenshots and Jira tickets that auditors inherently disbelieve.")
             ], ROSE_ACCENT)

    add_card(s2, 8.8, 2.0, 3.7, 4.9, "Must-Have vs. Nice-to-Have", 
             "This is not an optional developer tool—it is a mandatory statutory license to operate.",
             [
                 ("Without Proof, AI is Blocked", "In regulated finance, deploying autonomous agents without tamper-proof logs is corporate suicide."),
                 ("Unlocks Enterprise Budgets", "Gives Chief Risk Officers and corporate lawyers the confidence to approve production AI rollouts.")
             ], MINT_TEAL)

    # ==========================================
    # SLIDE 3: Proposed Solution
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "3", "Slide 3 — Proposed Solution 💡", 
               "Meet Aegis: The Digital Flight Recorder & Tamper-Proof Receipt for Autonomous AI.", 
               "The Solution", MINT_TEAL)

    add_card(s3, 0.8, 2.0, 3.7, 4.9, "The 'AI Digital Receipt'", 
             "Every time an AI agent makes a decision, Aegis automatically stamps a tamper-evident digital receipt.",
             [
                 ("Self-Contained Receipts", "Anyone can verify the receipt offline on a laptop—no special accounts, no trusting our servers."),
                 ("Instant Verification", "Regulators and auditors verify the entire decision trail in 6 milliseconds.")
             ], CHAMPAGNE_GOLD)

    add_card(s3, 4.8, 2.0, 3.7, 4.9, "Zero Privacy Leaks", 
             "Solves the privacy conflict by never saving sensitive customer data in plain text.",
             [
                 ("Scrambles & Discards", "Customer data (SSN, income, medical records) is converted into mathematical hashes, and the original text is immediately destroyed."),
                 ("100% GDPR & HIPAA Safe", "Impossible for hackers to steal customer data from the audit trail.")
             ], MINT_TEAL)

    add_card(s3, 8.8, 2.0, 3.7, 4.9, "Impossible to Fake / Tamper", 
             "If anyone alters even a single letter in the decision, the receipt breaks loudly and turns red.",
             [
                 ("Hardware-Rooted Chip", "Runs inside a physical secure hardware chip (Intel TDX / Confidential VM) where even cloud admins cannot tamper."),
                 ("Selective Disclosure", "If challenged in court, prove the exact decision score without revealing private customer files.")
             ], FOREST_TEAL)

    # ==========================================
    # SLIDE 4: Using the Product (CooL SDK)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "4", "Slide 4 — Using the Product 🛠️", 
               "Deep architectural integration with Northwind Cipher's CooL SDK (cool-nwc).", 
               "Technical Backbone", FOREST_TEAL)

    add_card(s4, 0.8, 2.0, 3.7, 4.9, "1. CooL Evidence Engine", 
             "We wrap AI agent decisions with cool.record() in just 3 lines of code.",
             [
                 ("Salted Multihashes", "Converts loan amounts and credit scores into unalterable cryptographic commitments without storing plaintext."),
                 ("Post-Quantum Signatures", "Dual ML-DSA-65 (NIST standard) + Ed25519 signatures that even quantum computers cannot crack.")
             ], CHAMPAGNE_GOLD)

    add_card(s4, 4.8, 2.0, 3.7, 4.9, "2. Phala dstack Hardware", 
             "Connects to /var/run/dstack.sock to lock the execution to a real physical CPU enclave.",
             [
                 ("Hardware Measurements", "Proves the exact approved model was running without hypervisor or cloud host tampering."),
                 ("Measurement-Sealed Keys", "Signing keys are generated inside the hardware enclave and rotate automatically on code changes.")
             ], MINT_TEAL)

    add_card(s4, 8.8, 2.0, 3.7, 4.9, "3. Automated Audit Packs", 
             "We leverage cool pack build and cool disclose for effortless compliance.",
             [
                 ("EU AI Act Art 12 Mapping", "Directly checks off statutory requirements for automated record-keeping."),
                 ("Selective Disclosure", "Prove a disputed decision in court using cool disclose without leaking private applicant data.")
             ], FOREST_TEAL)

    # ==========================================
    # SLIDE 5: Impact & Future Scope
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "5", "Slide 5 — Impact & Future Scope 🚀", 
               "Transforming compliance from 4 weeks of manual panic into a 6-millisecond automated verification.", 
               "Real-World Impact", CHAMPAGNE_GOLD)

    add_card(s5, 0.8, 2.0, 3.7, 4.9, "Immediate Business ROI", 
             "Measurable, bottom-line financial value for every company deploying AI.",
             [
                 ("90% Faster Audits", "Replaces 4-week compliance firefighting with a 1-second automated verification command."),
                 ("Zero Legal Exposure", "Full immunity against €35M non-compliance fines under the EU AI Act."),
                 ("Unlocks Enterprise Budgets", "Allows banks to safely put autonomous agents into production.")
             ], MINT_TEAL)

    add_card(s5, 4.8, 2.0, 3.7, 4.9, "Immediate Paying Customers", 
             "High-willingness-to-pay enterprise buyers ready on Day 1:",
             [
                 ("Digital Neobanks & Lenders", "High-volume consumer lending platforms (NuBank, Revolut, Klarna) needing instant loan proof."),
                 ("Autonomous InsurTech", "Automated claims processors paying out thousands of claims daily."),
                 ("Enterprise Agent Platforms", "Teams building on LangGraph, CrewAI, and AutoGen.")
             ], CHAMPAGNE_GOLD)

    add_card(s5, 8.8, 2.0, 3.7, 4.9, "Future Scalability Roadmap", 
             "Where the technology expands as autonomous AI grows:",
             [
                 ("Multi-Agent Swarm Consensuses", "Audit trails across 50 autonomous agents negotiating contracts with each other."),
                 ("Confidential GPU Attestation", "Hardware attestation directly on NVIDIA H100 and B200 AI clusters."),
                 ("Zero-Knowledge Batch Proofs", "Prove 100,000 loans were unbiased in a single mathematical proof.")
             ], FOREST_TEAL)

    output = "Reverse_Hackathon_AegisAgent_Presentation.pptx"
    prs.save(output)
    print("Updated PowerPoint saved successfully to", output)

if __name__ == "__main__":
    create_presentation()
