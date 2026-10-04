# Implementation Plan: Proof-First Portfolio

## Overview
Turn an already-polished but generic one-page portfolio into a site that *proves* its claims. Three moves: inject quantified impact into the hero and experience bullets, add a Projects section of 3 case-study cards (Problem → Constraint → Decision → Outcome) with small inline-SVG diagrams, and establish a clear conversion path (single primary CTA). The design and the vanilla HTML/CSS/JS stack stay unchanged.

## Architecture Decisions
- **No build step, no framework.** Extends the existing `index.html` + `style.css` directly. This is a hard user constraint and also the site's performance advantage.
- **Projects section follows existing patterns.** New `<section id="projects">` reuses the `section` / `section-header` / `timeline-item`-style card structure and existing inline-SVG icon conventions (`index.html:168`, `index.html:279`). No new assets.
- **Inline SVG for diagrams.** Consistent with the site's existing inline SVGs; keeps zero external requests and stays crisp at any resolution.
- **No downloadable PDF.** A print-to-PDF button was prototyped in Task 2 and then removed at the user's request; the site relies on the browser's native print if a PDF is ever needed. The existing print stylesheet is unchanged.
- **Verification is manual and browser-based.** The repo has no test runner and a deliberate no-build constraint; per TDD scope, static content changes are exempt from RED/GREEN. Interactive behavior (nav toggle, scroll-spy, scroll-reveal, back-to-top) is verified by hand in a browser — see Task 7. No test tooling is introduced.
- **Ordered audiences, not equal service.** Depth/proof targets engineers + hiring managers; the PDF targets recruiters; a secondary link targets consulting leads. One primary CTA only — the root fix for "reads generic."
- **Content-first sequencing.** The real risk is content (publishable, non-confidential detail and case-study material), not code. It is front-loaded so we fail fast if material isn't available.
- **Relative outcomes + anonymized case studies (NDA constraint).** No absolute employer metrics and no shareable artifacts, so every claim uses directional or specific-but-non-confidential language, and case studies are anonymized with conceptual inline-SVG diagrams (never screenshots or links to real systems).

## Task List

### Phase 1: Foundation & Risk Reduction
- [ ] Task 1: Impact-facts inventory + NDA boundary
- [~] Task 2: ~~One-click PDF resume~~ *(removed at user request)*

### Checkpoint: Foundation
- [ ] Every hero/experience claim has a confirmed, publishable fact or is queued for Task 3
- [ ] Human reviews publishable-metric list before any rewriting

### Phase 2: Quantify & Prove (core)
- [ ] Task 3: Quantify hero + experience bullets
- [ ] Task 4: Projects section scaffold (markup, styles, nav, scroll-spy)
- [ ] Task 5: Author 3 case-study cards

### Checkpoint: Core
- [ ] New `#projects` section renders and animates like existing sections
- [ ] Nav highlight + scroll-spy include `#projects`
- [ ] Every case study follows Problem → Constraint → Decision → Outcome
- [ ] Human reviews the 3 case studies before CTA work

### Phase 3: Convert & Verify
- [ ] Task 6: Primary CTA + consulting path
- [ ] Task 7: Accessibility, responsive, print & analytics QA pass

### Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] No console errors, Lighthouse a11y/perf not regressed
- [ ] Ready for review

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| Beqom/OrderYOYO metrics are NDA-bound | High | **Confirmed.** Use relative/specific-but-non-confidential outcomes only; anonymize case studies; conceptual diagrams, no screenshots/links |
| No 3 projects have shareable artifacts | High | **Confirmed NDA.** Anonymize all 3; reduce to 2 strong cards if material is thin |
| Extra section bloats the page / hurts performance | Medium | Reuse existing markup; no new assets; Lighthouse check in Task 7 |
| ~~`window.print()` PDF looks poor~~ | — | Resolved: PDF option removed |
| Adding a 4th nav item crowds mobile nav | Low | Verify at 320px in Task 4; existing hamburger handles overflow |

## Open Questions
- ~~What metric granularity can you publish?~~ **Resolved:** relative outcomes only — no absolute figures.
- Which single action is the primary conversion — interview interest or consulting inquiry? (Needed before Task 6.)
- ~~Do you have shareable project artifacts?~~ **Resolved:** none — case studies are anonymized.
- Is your GitHub profile strong enough to act as the one public proof point, or is all depth NDA'd?

## Explicitly Out of Scope (from idea phase)
Blog / Engineering Notes, interactive diagrams, one-screen rewrite, design/CSS overhaul, any framework or build step, serving all four audiences equally.
