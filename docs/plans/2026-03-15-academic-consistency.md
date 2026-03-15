# Academic Consistency Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make all navbar pages consistent with the academic style established on the main page — remove marketing hero banners, eyebrow labels, CTA buttons, badges/chips, and corporate patterns while keeping cards only where they organize structured data.

**Architecture:** Each page gets the same treatment: (1) remove hero banner, (2) strip marketing decorations from remaining elements, (3) convert prose-in-cards to plain markdown, (4) keep cards only for structured data (grants, projects, software). CSS cleanup at the end.

**Design principle from main page:** Transparent backgrounds, no decorative gradients, plain markdown for prose, subdued styling, simple text links instead of CTA buttons.

---

### Task 1: Team Page

**Files:**
- Modify: `_pages/team.md`

**Changes:**

1. **Remove hero banner** (lines 12-20): Delete the entire `section-hero--team` block with "Lab Ecosystem" eyebrow, h1, and marketing lede.

2. **Simplify callout** (lines 22-29): Replace the `team-callout` box with a plain paragraph under a markdown heading:
   ```markdown
   ## PhD Training Opportunities

   The lab welcomes PhD students interested in adaptive trial design, cancer genomics, machine learning for missing data, and precision oncology software development. Apply through the [UNC Biostatistics PhD program](https://sph.unc.edu/bios/biostatistics/admissions/). Prospective students can email [naim@unc.edu](mailto:naim@unc.edu) with questions about research directions and lab culture.
   ```

3. **Remove page-intro eyebrow/title** (lines 34-38): Delete the `page-intro__eyebrow` ("People"), `page-intro__title` ("Team roster"), and `page-intro__lede` paragraph. The team member cards follow directly.

4. **Keep**: Member cards (structured data with photo, role, links). Keep badge pills for team-position labels (Alumni, PhD Student) — these serve a functional purpose, not a decorative one.

**Step 1:** Make edits to `_pages/team.md`
**Step 2:** Build site, verify no errors: `bundle exec jekyll build 2>&1 | grep -i error`
**Step 3:** Commit: `git commit -m "simplify team page: remove hero, callout, eyebrow"`

---

### Task 2: Research Page

**Files:**
- Modify: `_pages/research.md`

**Changes:**

1. **Remove hero banner** (lines 11-23): Delete entire `section-hero--research` block with "Research Program" eyebrow, h1, marketing lede, and CTA buttons.

2. **Simplify Research Program Overview** (lines 25-49): Keep the three research area descriptions (they're substantive) but strip the decorative wrapper. Convert from `research-focus` card layout to plain markdown:
   ```markdown
   ## Research Overview

   Current work focuses on three interconnected areas:

   ### Clinical-Grade Tumor Subtyping
   PurIST, developed in collaboration with the Yeh laboratory, enables single-sample pancreatic cancer classification...

   ### Deep Learning for Non-Ignorable Missingness
   NIMIWAE and dlGLM frameworks bridge variational autoencoders...

   ### Adaptive Platforms with Late-Arriving Biomarkers
   Bayesian response-adaptive designs that integrate ctDNA...
   ```

3. **Simplify Selected Projects** (lines 51-108): Remove eyebrow ("Translational Work"), badges (`focus-card__badge`), chips (`focus-chip`), and arrow links (`link-arrow`). Keep the project descriptions as plain markdown sections under `## Selected Projects`. Mention publication venues inline rather than as chips.

4. **Keep research diagram** (lines 110-113): Leave as-is.

5. **Convert pillar-card sections to markdown** (lines 115-151): Replace "Cross-Cutting Methodological Innovations" pillar cards and "Collaborative Network" pillar cards with plain markdown lists.

6. **Remove page-cta** (lines 153-155): Delete the "Interested in PhD research?" CTA box. This info is already on the Teaching page.

**Step 1:** Make edits to `_pages/research.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify research page: remove hero, badges, chips, CTAs"`

---

### Task 3: Projects Page

**Files:**
- Modify: `_pages/projects.md`

**Changes:**

1. **Remove hero banner** (lines 11-23): Delete entire `section-hero--projects` block with "Build Tracker" eyebrow, h1, lede, and CTA buttons.

2. **Remove stage eyebrows** (lines 26, 71, 104): Remove `page-intro__eyebrow` labels ("Stage 1", "Stage 2", "Stage 3", "Journeys"). Replace with plain markdown headings:
   - "Stage 1 / In development" → `## In Development`
   - "Stage 2 / Pilot deployment" → `## Pilot Deployment`
   - "Stage 3 / Community adoption" → `## Deployed Software`

3. **Keep project cards** but strip badges: Remove `project-card__badge` elements (the colored topic tags). The project titles and descriptions already communicate the topic. Keep the `project-meta` lists (Lead, Milestone, Status) — these are structured data.

4. **Remove "Journeys" section** (lines 136-156): Delete the "Code-to-clinic stories" section entirely. This is corporate storytelling and the PurIST story is already told on the main page.

5. **Simplify collaboration section** (lines 158-166): Convert to plain markdown:
   ```markdown
   ## Collaboration & Access

   Projects are co-developed with Gillings trainees, UNC Lineberger oncologists, and cooperative group collaborators. See [repositories](/repositories/) for code, or email [naim@unc.edu](mailto:naim@unc.edu) about pilot access.
   ```

6. **Remove arrow links** (`link-arrow` class with "→" suffix): Replace with plain links.

**Step 1:** Make edits to `_pages/projects.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify projects page: remove hero, stage labels, journey cards"`

---

### Task 4: Teaching Page

**Files:**
- Modify: `_pages/teaching.md`

**Changes:**

1. **Remove hero banner** (lines 10-21): Delete entire `section-hero--teaching` block.

2. **Simplify courses section** (lines 23-56): Remove eyebrow ("Course lineup") and `page-intro__title`. Remove `focus-card__badge` labels and `focus-chip` elements. Convert to plain markdown with ### headings per course:
   ```markdown
   ## Courses

   ### BIOS 667 · Applied Longitudinal Data Analysis
   GEEs, mixed models, joint modeling, and missing-data tactics...

   ### BIOS 735 · Statistical Computing
   Machine learning, git/GitHub, simulation, optimization...
   [Course site](https://biodatascience.github.io/statcomp/)

   ### Reproducible Oncology Analytics Workshop
   Git, Quarto notebooks, and genomic-study case studies...
   ```

3. **Simplify Mentoring & Student Outcomes** (lines 58-87): Remove `focus-card__badge` labels ("Academic Positions", "Industry Positions"). Keep the student placement lists but as plain markdown.

4. **Keep "For Prospective PhD Students" cards** (lines 89-148): These cards organize genuinely structured info (Technical Skills, Meeting Structure, Authorship, Funding, Research Scope, Lab Environment) that benefits from card layout. **But strip the badges** — remove `focus-card__badge` labels. The h4 headings already describe each card.

5. **Remove section-lede** styling: Convert to plain paragraphs.

**Step 1:** Make edits to `_pages/teaching.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify teaching page: remove hero, badges, chips"`

---

### Task 5: Software Page

**Files:**
- Modify: `_pages/software.md`

**Changes:**

1. **Remove page-intro eyebrow** (lines 10-17): Remove eyebrow ("Overview") and `page-intro__title`. Replace with a simple introductory paragraph (no special styling).

2. **Keep software cards**: These organize structured data (package name, description, links, papers). Leave them.

3. **Remove page-cta** (lines 119-121): Delete "Using these tools?" CTA box. The contact info is in the Support section below.

4. **Simplify Support section** (lines 123-127): Already mostly plain markdown. Remove the `page-section--alt` wrapper.

**Step 1:** Make edits to `_pages/software.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify software page: remove eyebrow and CTA"`

---

### Task 6: Funding Page

**Files:**
- Modify: `_pages/funding.md`

**Changes:**

1. **Remove page-intro eyebrow** (lines 10-22): Remove eyebrow ("Overview") and `page-intro__title` ("Funding Portfolio"). Replace with a brief plain intro paragraph.

2. **Keep grant cards**: These organize structured financial data (amount, period, role). Keep them. **But remove "Active" badges** — every listed grant is active, so these are redundant.

3. **Keep leadership cards**: These organize structured role descriptions.

4. **Remove page-cta** (lines 192-194): Delete "Interested in collaboration?" CTA box. Contact info is available through the nav.

**Step 1:** Make edits to `_pages/funding.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify funding page: remove eyebrow, badges, CTA"`

---

### Task 7: Publications Page

**Files:**
- Modify: `_pages/publications.md`

**Changes:**

1. **Remove page-intro eyebrow** (lines 12-19): Remove eyebrow ("Overview") and `page-intro__title` ("Publication Portfolio"). Keep the introductory paragraph about editorial roles but as plain text.

2. **Everything else stays**: The publication listing with theme filters and collapsible sections is already academic.

**Step 1:** Make edits to `_pages/publications.md`
**Step 2:** Build site, verify no errors
**Step 3:** Commit: `git commit -m "simplify publications page: remove eyebrow"`

---

### Task 8: CSS Cleanup for Section Heroes

**Files:**
- Modify: `_sass/_custom.scss`
- Modify: `_sass/custom/_dark-mode.scss`

**Changes:**

1. **Neutralize section-hero styles**: Since all section-hero blocks are being removed from content, add a safety fallback that makes any remaining `.section-hero` elements render with transparent background, no decorative elements (matching the academic hero-panel treatment).

2. **Tone down remaining card styles**: For cards we're keeping (grant-card, software-card, project-card), ensure they use subtle borders and minimal shadows (consistent with the hero-panel aside treatment). No background gradients.

3. **Remove page-cta styles** or neutralize them since all page CTAs are being removed.

4. **Dark mode**: Verify the section-hero dark mode entries still work (they reference `.section-hero` which we may leave in CSS even though HTML is removed).

**Step 1:** Make CSS edits
**Step 2:** Build site, verify all pages render correctly
**Step 3:** Commit: `git commit -m "tone down card styles and clean up unused hero CSS"`

---

### Task 9: Final Verification

**Steps:**
1. Build site: `bundle exec jekyll build 2>&1 | grep -i error`
2. Start server: `bundle exec jekyll serve --host 127.0.0.1 --port 4000`
3. Visually verify each page:
   - / (main page — should be unchanged)
   - /team.html
   - /research/
   - /projects/
   - /software/
   - /teaching/
   - /funding/
   - /publications/
4. Check dark mode on each page
5. Check mobile responsiveness (narrow viewport)
6. Commit any fixes
