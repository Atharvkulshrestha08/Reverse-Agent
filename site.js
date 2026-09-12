/**
 * AegisAgent AI — Enterprise Shared Client Utilities
 * Handles scroll progress, oval navigation, back-to-top, cookie consent,
 * Ctrl+K site search, copy to clipboard, password visibility, and UTM tracking.
 */

// 1. Scroll Progress Bar & Back-to-Top Button
function initScrollFeatures() {
  const progressBar = document.getElementById("scrollProgressBar");
  const backToTop = document.getElementById("backToTopBtn");

  window.addEventListener("scroll", () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    
    if (progressBar) {
      progressBar.style.width = scrolled + "%";
    }

    if (backToTop) {
      if (winScroll > 320) {
        backToTop.classList.add("visible");
      } else {
        backToTop.classList.remove("visible");
      }
    }
  });

  if (backToTop) {
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
}

// 2. Dark Simple Cookie Consent Banner
function initCookieConsent() {
  const existing = localStorage.getItem("aegis_cookie_consent");
  const banner = document.getElementById("cookieConsentBanner");
  if (!banner) return;

  if (existing) {
    banner.style.display = "none";
  } else {
    banner.style.display = "flex";
  }
}

function acceptCookies() {
  localStorage.setItem("aegis_cookie_consent", "accepted");
  const banner = document.getElementById("cookieConsentBanner");
  if (banner) banner.style.display = "none";
}

function declineCookies() {
  localStorage.setItem("aegis_cookie_consent", "essential_only");
  const banner = document.getElementById("cookieConsentBanner");
  if (banner) banner.style.display = "none";
}

// 3. Site Search Modal (Ctrl+K or Command+K)
const SEARCH_INDEX = [
  { title: "Home (Executive Overview)", url: "/", desc: "Autonomous AI Flight Recorder & Attestation Rail overview." },
  { title: "Interactive Underwriting App", url: "/app", desc: "Live dynamic credit dossier execution and 6ms cryptographic verification." },
  { title: "Regulatory Audit Hub", url: "/audit", desc: "EU AI Act Article 12, RBI Digital Lending, Merkle logs, and audit packs." },
  { title: "Institutional Case Studies", url: "/case-studies", desc: "Real deployment proofs in SME lending, HealthTech triage, and claims fraud." },
  { title: "Enterprise Waitlist", url: "/waitlist", desc: "Request pilot deployment and CVM attestation cluster access." },
  { title: "About Team & Project", url: "/about", desc: "Atharv Kulshrestha, Team VLC, RKGIT AKTU, and CooL SDK mission." },
  { title: "Contact & SLA Guarantees", url: "/contact", desc: "Subpoena hotline, enterprise SLA (< 15 min), and office directions." },
  { title: "Privacy Policy (DPDP Act)", url: "/privacy", desc: "Data minimization, zero customer PII storage, salted multihashes." },
  { title: "5-Slide Pitch Deck", url: "/presentation", desc: "Official Reverse Hackathon 5-slide presentation with PDF export." }
];

function openSiteSearch() {
  const modal = document.getElementById("siteSearchModal");
  const input = document.getElementById("siteSearchInput");
  if (modal) {
    modal.classList.add("active");
    if (input) {
      input.value = "";
      renderSearchResults("");
      input.focus();
    }
  }
}

function closeSiteSearch() {
  const modal = document.getElementById("siteSearchModal");
  if (modal) modal.classList.remove("active");
}

function renderSearchResults(query) {
  const resultsContainer = document.getElementById("siteSearchResults");
  if (!resultsContainer) return;

  const q = query.trim().toLowerCase();
  const matched = q === "" 
    ? SEARCH_INDEX.slice(0, 5) 
    : SEARCH_INDEX.filter(item => item.title.toLowerCase().includes(q) || item.desc.toLowerCase().includes(q));

  if (matched.length === 0) {
    resultsContainer.innerHTML = `<div class="p-4 text-center text-xs text-cream/60">No pages matched "${query}". Try "audit", "app", or "privacy".</div>`;
    return;
  }

  resultsContainer.innerHTML = matched.map(item => `
    <a href="${item.url}" class="block p-3 rounded-lg hover:bg-forest transition border border-transparent hover:border-gold/30 text-left">
      <div class="font-serif font-bold text-sm text-gold">${item.title}</div>
      <div class="text-xs text-cream/70 mt-0.5">${item.desc}</div>
    </a>
  `).join("");
}

// 4. One-Click Copy Utility with Tooltip
function copyToClipboard(text, btnEl) {
  navigator.clipboard.writeText(text).then(() => {
    if (!btnEl) return;
    const originalHtml = btnEl.innerHTML;
    btnEl.innerHTML = `<span class="text-emerald-400">✓ Copied!</span>`;
    btnEl.classList.add("border-emerald-500");
    setTimeout(() => {
      btnEl.innerHTML = originalHtml;
      btnEl.classList.remove("border-emerald-500");
    }, 2000);
  }).catch(err => {
    console.error("Copy failed:", err);
  });
}

// 5. Secret / Password Visibility Toggle
function toggleSecretVisibility(inputId, btnId) {
  const input = document.getElementById(inputId);
  const btn = document.getElementById(btnId);
  if (!input) return;

  if (input.type === "password") {
    input.type = "text";
    if (btn) btn.innerText = "🔒 Hide";
  } else {
    input.type = "password";
    if (btn) btn.innerText = "👁️ Show";
  }
}

// 6. UTM Tracking Parameter Extraction
function captureUtmParams() {
  const params = new URLSearchParams(window.location.search);
  const utm = {};
  ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"].forEach(key => {
    if (params.has(key)) {
      utm[key] = params.get(key);
    }
  });
  if (Object.keys(utm).length > 0) {
    sessionStorage.setItem("aegis_utm", JSON.stringify(utm));
  }
}

function getStoredUtmParams() {
  try {
    return JSON.parse(sessionStorage.getItem("aegis_utm")) || {};
  } catch (e) {
    return {};
  }
}

// 7. Global Keyboard Listeners (Cmd/Ctrl + K)
window.addEventListener("keydown", (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    openSiteSearch();
  }
  if (e.key === "Escape") {
    closeSiteSearch();
  }
});

// Initialize on DOM Ready
window.addEventListener("DOMContentLoaded", () => {
  initScrollFeatures();
  initCookieConsent();
  captureUtmParams();

  const searchInput = document.getElementById("siteSearchInput");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      renderSearchResults(e.target.value);
    });
  }
});
