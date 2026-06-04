# ROADMAP.md

## Task 1 — Create project scaffold: index.html, style.css, assets/logo.svg, CHANGELOG.md
- **Instruction:** Create the bare-bones file structure (empty or minimal `index.html`, `style.css`, `assets/logo.svg` placeholder, and `CHANGELOG.md`) so the project matches the layout described in the spec.
- **Relevant context:** CLAUDE.md § Project structure
- **Dependencies:** none
- **Blocked by open questions:** none

---

## Task 2 — Build the HTML skeleton with all required sections (no styling)
- **Instruction:** Write `index.html` with semantic HTML sections in order — header/hero, how-it-works, supported-marketplaces, affiliate-disclosure, about/contact, and footer — using real copy from the spec (no lorem ipsum), and include a placeholder email form with a visible note that the Mailchimp embed will replace it.
- **Relevant context:** CLAUDE.md § Content requirements (all subsections), § Email signup, § Open questions #1 and #3
- **Dependencies:** Task 1
- **Blocked by open questions:** Open question #3 (contact email) — use a visible placeholder like `contact@hagglingwizard.com` and note it must be replaced before go-live.

---

## Task 3 — Write mobile-first CSS for layout and typography
- **Instruction:** Write `style.css` with a mobile-first responsive layout covering the full page — system font stack, readable line lengths, section spacing, and a breakpoint for desktop — with no external fonts, no CSS framework, and no JavaScript.
- **Relevant context:** CLAUDE.md § Design constraints
- **Dependencies:** Task 2
- **Blocked by open questions:** none

---

## Task 4 — Polish visual design: hero emphasis, step cards, marketplace list, footer
- **Instruction:** Refine `style.css` so the hero headline and CTA are prominent, the three how-it-works steps are visually distinct cards or numbered items, the marketplace list is clean, and the footer contains the copyright line and privacy policy link.
- **Relevant context:** CLAUDE.md § Content requirements, § Design constraints
- **Dependencies:** Task 3
- **Blocked by open questions:** none

---

## Task 5 — Create privacy.html (minimal plain-text privacy policy)
- **Instruction:** Create `privacy.html` as a plain HTML page covering: email collection via signup form, no cookies or tracking, and affiliate link disclosure — written in plain language without legalese.
- **Relevant context:** CLAUDE.md § Open questions #2, § Footer, § Affiliate disclosure
- **Dependencies:** Task 2 (footer must link to `/privacy.html`)
- **Blocked by open questions:** Open question #2 — this task resolves it; no external input needed.

---

## Task 6 — Replace email form placeholder with Mailchimp embed
- **Instruction:** Replace the placeholder form in `index.html` with the Mailchimp embedded signup embed code (email-only, label "Get notified when we launch"), removing the placeholder note.
- **Relevant context:** CLAUDE.md § Email signup, § Open questions #1
- **Dependencies:** Task 2
- **Blocked by open questions:** **BLOCKED — Open question #1**: Mailchimp account and audience list must be created first; embed code comes from the Mailchimp dashboard.

---

## Task 7 — Final pre-launch audit: affiliate compliance, copy, and live check
- **Instruction:** Review the live page at hagglingwizard.com against every affiliate requirement in the spec — affiliate disclosure visible, marketplaces named correctly, no lorem ipsum, contact email set, privacy policy linked — and fix any gaps.
- **Relevant context:** CLAUDE.md § Affiliate program requirements, § Content requirements, § Open questions #3
- **Dependencies:** Tasks 2–6 (all content must be final)
- **Blocked by open questions:** Open question #3 (contact email must be resolved before this task can be marked complete).
