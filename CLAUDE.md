# CLAUDE.md — Haggling Wizard Landing Page

## Instructions for Claude Code

Read this entire file before doing anything else. Do not write any code yet.

### Task 0 — produce ROADMAP.md

Your only job right now is to produce a `ROADMAP.md` file in the project root. Then stop.

`ROADMAP.md` must:
- Break the project into sequential numbered tasks (e.g. `Task 1`, `Task 2`, ...)
- Keep each task small enough to be completed in a single focused session
- Write each task description in one clear sentence usable as a direct implementation instruction
- List any files or sections of this spec that are relevant context for that task
- Note hard dependencies (e.g. "requires Task 3 to be complete")
- Flag tasks that are blocked by the open questions at the bottom of this spec

Do not group tasks into phases or add commentary. A flat numbered list with the fields above is enough.

### Rule for all tasks (including this one)

One task per session. When a task is complete:
1. All new code has unit tests where applicable (HTML/CSS has no unit tests; skip this check for pure markup tasks)
2. All tests pass
3. The project renders correctly in a browser without errors

Stop after confirming these three. Do not begin the next task.

At the end of every task:
- Append an entry to CHANGELOG.md (task number, date, files changed, one sentence why)
- If the change affects copy or structure visible to visitors, update README.md accordingly

---

## What this repo is

A static HTML/CSS landing page for hagglingwizard.com, hosted on GitHub Pages.
Its only purpose is to present the product clearly enough to:
1. Pass affiliate program review (AbeBooks/Impact Radius, Biblio/Awin, eBay Partner Network)
2. Collect email signups from interested users before the app launches

This is NOT the Flask application. There is no backend, no JavaScript framework, no build step.
When the Flask app is ready and deployed to Railway, the DNS for hagglingwizard.com will be
pointed away from GitHub Pages. This repo will then be archived or redirected.

---

## Project structure

```
haggling-wizard-landing/
├── index.html          # Single page, all content
├── style.css           # Stylesheet (no frameworks, no preprocessors)
├── assets/
│   └── logo.svg        # Logo placeholder — replace with real asset when ready
├── CHANGELOG.md
└── README.md
```

---

## Content requirements

The page must include all of the following. Affiliate programs will look for these.

### Required sections (in order)

1. **Header / hero**
   - Product name: Haggling Wizard
   - One-line description: "Price alerts for out-of-print RPG and D&D books"
   - Email signup form (Mailchimp embed — see open questions)
   - No placeholder lorem ipsum anywhere on the page at launch

2. **How it works**
   - Three steps, concisely written:
     1. Add books to your wishlist
     2. We scan second-hand marketplaces daily
     3. You get an email when a deal appears

3. **Supported marketplaces**
   - eBay
   - AbeBooks
   - Biblio
   - Do not mention sites not yet integrated

4. **Affiliate disclosure**
   - Required by all three affiliate programs
   - Must state clearly: links to partner sites may earn a commission
   - Must be visible without scrolling on desktop OR present in the footer
   - Plain language, not legalese

5. **About / contact**
   - One paragraph: who built this and why (personal collector project)
   - Contact email address

6. **Footer**
   - Privacy policy link (see open questions — can be a placeholder page at /privacy.html)
   - Affiliate disclosure (if not in body)
   - © Haggling Wizard [year]

---

## Design constraints

- Mobile-first, responsive layout
- No JavaScript frameworks, no CSS frameworks (Tailwind, Bootstrap, etc.)
- Vanilla CSS only
- No external fonts (use system font stack)
- Page must load fast on a slow connection — no large images at launch
- No cookies, no tracking pixels, no analytics at launch (simplifies privacy policy)

---

## Affiliate program requirements

Each program will review this page before approving the application.
The following are known requirements; do not remove or obscure them.

| Program | Platform | Key requirement |
|---|---|---|
| eBay Partner Network | ebay.com/partner | Affiliate disclosure visible on page |
| AbeBooks | Impact Radius | Site must describe how affiliate links will be used |
| Biblio | Awin | Active site with relevant content; disclosure required |

The page must be live and publicly accessible at hagglingwizard.com before submitting applications.

---

## Email signup

Use a Mailchimp embedded signup form (free tier is sufficient).
The form should collect email address only — no name, no other fields.
Label: "Get notified when we launch"

See open questions — Mailchimp account and list must be created before this task can be completed.
If not yet created, use an HTML form placeholder with a visible note that the embed will replace it.

---

## Open questions (flag before implementing the affected task)

1. Mailchimp account and audience list — must be created at mailchimp.com before the email signup
   form can be embedded. The embed code is generated in the Mailchimp dashboard.
2. Privacy policy — a minimal privacy policy page (/privacy.html) is needed. It should cover:
   email collection via signup form, no cookies/tracking, affiliate link disclosure.
   This can be a plain text page at launch.
3. Contact email — decide what address to display publicly (not your personal address).
   A catch-all at hagglingwizard.com (via a service like Improvmx) is recommended.
