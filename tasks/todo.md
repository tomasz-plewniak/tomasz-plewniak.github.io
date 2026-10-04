# TODO: Proof-First Portfolio

Task list target for the Proof-First Portfolio plan. Full plan: `tasks/plan.md`.

> **Verification note:** this repo has **no build step and no automated tests**. "Verification" here means serving the site and checking in a real browser (Chrome DevTools). Optional markup lint via `npx --yes html-validate index.html`. Serve with `python3 -m http.server 8000`.

---

## Phase 1: Foundation & Risk Reduction

### Task 1: Impact-facts inventory + NDA boundary
**Description:** Build a private working note mapping every existing achievement bullet in `index.html` to a publishable fact or metric, and document the confidentiality boundary per employer (Beqom, OrderYOYO/TDP, EPAM, Elettric80). Identifies 3 candidate case studies. This front-loads the real risk (content), not the code.

**Acceptance criteria:**
- [x] Each experience bullet (`index.html:290`–`393`) has an associated non-confidential fact/outcome or an explicit "cannot publish" note
- [x] NDA boundary documented per employer (relative outcomes only; no artifacts)
- [x] 3 candidate anonymized projects identified, each with a Problem/Constraint/Decision/Outcome skeleton

**Verification:**
- [ ] Human reviews the inventory and signs off on what is publishable (`[confirm]` items in the note)
- [x] Working note is **not committed** to the repo (added to `.gitignore`)

**Dependencies:** None
**Files likely touched:** `tasks/impact-facts.md` (local working note — gitignored, not committed)
**Estimated scope:** XS

### Task 2: ~~One-click PDF resume~~ — REMOVED
**Status:** Cancelled at the user's request. The hero Download PDF button, its `window.print()` JS listener, and all related CSS (`hero-actions`, `hero-cta-secondary`) were reverted to the original single CTA. The existing print stylesheet is unchanged.

---

## Checkpoint: Foundation
- [ ] Every hero/experience claim has a confirmed, publishable fact
- [ ] Human reviews the publishable-metric list before proceeding

---

## Phase 2: Quantify & Prove (core)

### Task 3: Quantify hero + experience bullets
**Description:** Rewrite the hero summary and every experience bullet to carry concrete scale or outcome, using the Task 1 inventory. Replace adjective-driven claims ("robust", "high-performance") with specifics.

**Acceptance criteria:**
- [x] Hero contains at least one specific, non-confidential flagship outcome (relative/directional — no absolute figures)
- [x] Each of the 3 most recent roles (TDP, Beqom, EPAM) has ≥1 outcome-forward bullet *(scope change: 2016–2019 roles keep their existing concrete descriptions rather than adding redundant bullets)*
- [x] No bullet relies solely on adjectives
- [x] All claims stay within the approved Task 1 list (no new specifics invented)

**Verification:**
- [x] Diff reviewed against the inventory
- [ ] Human sign-off on wording *(user)*
- [ ] Render check at 320px for overflow *(user)*

**Dependencies:** Task 1
**Files likely touched:** `index.html`
**Estimated scope:** M (single file, content-heavy)

### Task 4: Projects section scaffold
**Description:** Add `<section id="projects">` between Experience and Education, with 3 empty case-study cards following existing patterns; wire up nav, scroll-spy, and scroll-reveal.

**Acceptance criteria:**
- [x] Section renders with 3 cards, reusing `section-header` + card styling
- [x] Each card has slots: title, Problem, Constraint, Decision, Outcome, tech pills, conceptual inline-SVG diagram (no external links — NDA)
- [x] Nav gains a "Work" link; scroll-spy highlights it
- [x] Scroll-reveal observer includes the new cards
- [ ] Mobile nav (320px) still opens/closes with 4 links *(user)*

**Verification:**
- [ ] Serve and scroll: confirm reveal animation + active link
- [ ] No console errors
- [ ] `npx --yes html-validate index.html` (optional)

**Dependencies:** None (placeholder content)
**Files likely touched:** `index.html`, `style.css`
**Estimated scope:** M

### Task 5: Author 3 case-study cards
**Description:** Fill the scaffold with 3 real case studies from the Task 1 material, each with a small inline-SVG architecture diagram.

**Acceptance criteria:**
- [x] 3 cards filled; each tells Problem → Constraint → Decision → Outcome, anonymized *(draft relative copy, pending human review)*
- [x] Each has a distinct conceptual inline-SVG diagram (our own; no external assets, screenshots, or links)
- [x] Tech pills match the actual stack
- [x] No unapproved or confidential figures/identifiers

**Verification:**
- [ ] Human review of the 3 narratives *(user)*
- [ ] Render + responsive check *(user)*
- [x] SVG given an accessible name (`role="img"` + `aria-label`)

**Dependencies:** Tasks 1, 4
**Files likely touched:** `index.html`
**Estimated scope:** M (single file, content-heavy)

---

## Checkpoint: Core
- [ ] `#projects` renders and animates like existing sections
- [ ] Nav highlight + scroll-spy include `#projects`
- [ ] Each case study follows Problem → Constraint → Decision → Outcome
- [ ] Human reviews the 3 case studies before CTA work

---

## Phase 3: Convert & Verify

### Task 6: Primary CTA + consulting path
**Description:** Establish one visually dominant primary CTA in the hero and a quieter secondary path for consulting inquiries; reduce competing actions so the page has a clear next step.

**Acceptance criteria:**
- [x] Exactly one visually dominant primary CTA in hero ("Get in touch", mailto)
- [x] Secondary, lower-emphasis action (Download PDF) — *consulting shares the primary email path; no separate booking channel yet*
- [x] Redundant email contact chip removed so chips don't compete with the primary
- [x] Footer CTA aligns with the same primary action (Email)

**Verification:**
- [ ] Visual hierarchy check (only one primary button) *(user)*
- [x] Keyboard + focus states (native button/link; global `:focus-visible`)
- [x] Link targets valid (mailto)

**Dependencies:** Tasks 3, 5
**Files likely touched:** `index.html`, `style.css`
**Estimated scope:** S

### Task 7: Accessibility, responsive, print & analytics QA
**Description:** Final verification pass across accessibility, responsiveness, print output, performance, and analytics events.

**Acceptance criteria:**
- [ ] No new Lighthouse/axe a11y violations
- [ ] Layout correct at 320 / 768 / 1280; no horizontal scroll
- [ ] Print preview clean
- [ ] gtag click events fire for CTA + Download (`gtag` wired at `index.html:105`)
- [ ] Lighthouse performance not regressed vs current baseline

**Verification:**
- [x] Static pass: single `<h1>`, no heading-level jumps, all links have accessible text, markup balanced
- [ ] Chrome DevTools Lighthouse run (a11y + perf) *(user)*
- [ ] Keyboard-only walkthrough *(user)*
- [ ] Network/GA debug check for event fires *(user)*

**Dependencies:** Tasks 2, 6
**Files likely touched:** `index.html`, `style.css`
**Estimated scope:** S

---

## Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] No console errors; Lighthouse a11y/perf not regressed
- [ ] Ready for review

---

## Parallelization Notes
- **Must be sequential:** Tasks 3, 4, 5, 6 all edit `index.html` — do not run concurrently.
- **Safe to parallelize:** Task 2 (PDF) is independent, but it also touches `index.html`'s hero, so land it before Task 6.
- **Coordination:** Task 5 depends on Task 1 (content) and Task 4 (structure) — define both first.
