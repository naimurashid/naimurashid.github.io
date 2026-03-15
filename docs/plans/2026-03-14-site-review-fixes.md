# Site Review Fixes — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix all verified factual errors, broken references, stale dates, and inconsistencies identified during the site review audit.

**Architecture:** Edits to YAML data files, Markdown content pages, BibTeX bibliography keys in member frontmatter, and project page `{% cite %}` tags. No layout/template changes needed. No new files beyond optional news entries.

**Tech Stack:** Jekyll (al-folio theme), Liquid templates, BibTeX (`_bibliography/papers.bib`), YAML data files (`_data/`)

---

## Priority Tier 1: Factual Errors & Broken Content

### Task 1: Fix broken BibTeX citation keys in project pages

Two project pages use `{% cite %}` tags referencing BibTeX keys that don't exist in `papers.bib`, producing "(missing reference)" in the built site.

**Files:**
- Modify: `_projects/purist.md:33`
- Modify: `_projects/glmmpen.md:23`

**Step 1: Fix PurIST project citation key**

In `_projects/purist.md` line 33, change:
```
*Key reference:* {% cite rashid2020purity %}
```
to:
```
*Key reference:* {% cite purity2020 %}
```

The correct key in `papers.bib` is `purity2020` (line 44), not `rashid2020purity`.

**Step 2: Fix glmmPen project citation key**

In `_projects/glmmpen.md` line 23, change:
```
- *Penalized GLMMs:* {% cite heiling2021b %}
```
to:
```
- *Penalized GLMMs:* {% cite glmmpen2024 %}
```

The correct key in `papers.bib` is `glmmpen2024` (line 347). The key `heiling2021b` does not exist.

**Step 3: Verify**

Run: `grep -r "missing reference" _site/projects/ 2>/dev/null` after next build.
Expected: No matches.

**Step 4: Commit**

```bash
git add _projects/purist.md _projects/glmmpen.md
git commit -m "fix: correct broken BibTeX citation keys in project pages"
```

---

### Task 2: Fix broken BibTeX keys in member profile frontmatter

Five member profiles reference BibTeX keys in their `lab_publications` frontmatter that don't exist in `papers.bib`. The `about.liquid` layout uses `{% reference pubkey %}` which silently produces "(missing reference)".

**Files:**
- Modify: `_members/about_david.md:31,38,43` (3 broken keys)
- Modify: `_members/about_hillary.md:31,38,43,50` (4 broken keys)
- Modify: `_members/about_pedro.md:31,38` (2 broken keys)
- Modify: `_members/about_scott.md:31,38` (2 broken keys)
- Modify: `_members/about_amber.md:30` (1 broken key)

**Key mapping (broken → correct in `papers.bib`):**

| Member | Broken Key | Correct Key | Evidence |
|--------|-----------|-------------|----------|
| David | `lim2020` | `modelbased2021` | Title: "Model-based feature selection and clustering" (line 363) |
| David | `lim2021` | `handling2021` | Title: "Handling non-ignorably missing features" (line 402) — OR `unsupervised2025` (line 442) for the published version |
| David | `lim2022` | `deeply2024` | Title: "Deeply learned generalized linear models" (line 542) |
| Hillary | `heiling2021b` | `glmmpen2024` | Title: "glmmpen: High dimensional penalized..." (line 347) |
| Hillary | `heiling2021estimating` | `estimating2023` | Title: "Estimating cell type composition..." (line 499) |
| Hillary | `heiling2023efficient` | `efficient2024` | Title: "Efficient computation of high-dimensional..." (line 466) |
| Hillary | `heiling2023survival` | `efficient2025` | Title: "Efficient Computation...Piecewise Constant Hazard" (line 523) |
| Pedro | `baldoni2019improved` | `improved2019` | Title: "Improved detection of epigenomic marks" (line 679) |
| Pedro | `Baldoni864124` | `efficient2022` | Title: "Efficient detection and classification of epigenomic changes" (line 647) — OR `epigrahmmepigenomic2020` (line 894) for the epigraHMM paper |
| Scott | `van2020differential` | `differential2020` | Title: "Differential transcript usage" (line 663) |
| Scott | `van2021compression` | `compression2021` | Title: "Compression of quantification uncertainty" (line 394) |
| Amber | `van2020differential` | `differential2024` | Same paper, published version (line 631) — Amber is listed as first author on this version |

**Step 1: Fix David Lim's keys**

In `_members/about_david.md`, replace the `lab_publications` keys:
- Line 31: `lim2020` → `modelbased2021`
- Line 38: `lim2021` → `unsupervised2025`
- Line 43: `lim2022` → `deeply2024`

**Step 2: Fix Hillary Heiling's keys**

In `_members/about_hillary.md`, replace:
- Line 31: `heiling2021b` → `glmmpen2024`
- Line 38: `heiling2021estimating` → `estimating2023`
- Line 43: `heiling2023efficient` → `efficient2024`
- Line 50: `heiling2023survival` → `efficient2025`

**Step 3: Fix Pedro Baldoni's keys**

In `_members/about_pedro.md`, replace:
- Line 31: `baldoni2019improved` → `improved2019`
- Line 38: `Baldoni864124` → `efficient2022`

**Step 4: Fix Scott Van Buren's keys**

In `_members/about_scott.md`, replace:
- Line 31: `van2020differential` → `differential2020`
- Line 38: `van2021compression` → `compression2021`
- Also line 44: `van2020differential` → `differential2020` (in `publications:` block)

**Step 5: Fix Amber Young's key**

In `_members/about_amber.md`, replace:
- Line 30: `van2020differential` → `differential2024`

**Step 6: Verify**

Run: `grep -r "missing reference" _site/members/ 2>/dev/null` after next build.
Expected: No matches.

**Step 7: Commit**

```bash
git add _members/about_david.md _members/about_hillary.md _members/about_pedro.md _members/about_scott.md _members/about_amber.md
git commit -m "fix: correct broken BibTeX keys in member profile frontmatter"
```

---

### Task 3: Add missing 2025 Gillings Award to CV data

The award appears on the About page (line 207) but is missing from `_data/cv.yml`.

**Files:**
- Modify: `_data/cv.yml:46-51`

**Step 1: Add award entry**

In `_data/cv.yml`, insert a new year entry before the existing 2024 entry (after line 48, before line 49):

```yaml
- title: Honors and Awards
  type: time_table
  contents:
    - year: 2025
      items:
        - Gillings Research Excellence Award, Gillings School of Global Public Health
    - year: 2024
      items:
        - James E. Grizzle Distinguished Alumnus Award, Department of Biostatistics, Gillings School of Global Public Health
```

**Step 2: Commit**

```bash
git add _data/cv.yml
git commit -m "fix: add 2025 Gillings Research Excellence Award to CV data"
```

---

### Task 4: Reconcile editorial service dates

AOAS and Nature Medicine dates differ between `_data/cv.yml` and the About/Publications pages.

| Role | cv.yml | about.md | publications.md |
|------|--------|----------|-----------------|
| AOAS AE | 2022–present | 2023– | 2023– |
| Nature Medicine | 2023–present | 2024– | 2024– |

**Decision needed from PI:** Which dates are correct? The CV says earlier dates. This plan assumes the CV dates are correct (they're more likely to reflect formal appointment dates), but **verify with PI before executing**.

**Files:**
- Modify: `_pages/about.md:222-223`
- Modify: `_pages/publications.md:18` (if editorial dates appear there)

**Step 1: Update About page to match CV (if CV is authoritative)**

In `_pages/about.md`:
- Line 222: Change `Nature Medicine Statistical Advisory Panel (2024-)` to `Nature Medicine Statistical Advisory Panel (2023-)`
- Line 223: Change `Associate Editor, Annals of Applied Statistics (2023-)` to `Associate Editor, Annals of Applied Statistics (2022-)`

**Step 2: Update Publications page similarly**

Check `_pages/publications.md` line 18 for the same references and update to match.

**Step 3: Commit**

```bash
git add _pages/about.md _pages/publications.md
git commit -m "fix: reconcile editorial service dates to match CV records"
```

---

### Task 5: Update stale project milestone dates

Three projects on the Projects page reference Fall/Oct 2025 milestones that are now past.

**Files:**
- Modify: `_pages/projects.md:35,48,61`

**Step 1: Update DeSurv milestone**

Line 35: Change:
```html
<li><strong>Milestone:</strong> Manuscript + CRAN submission · Fall 2025</li>
```
to:
```html
<li><strong>Milestone:</strong> Manuscript + CRAN submission · In progress</li>
```

**Step 2: Update ADAPT Statistical Hub milestone**

Line 48: Change:
```html
<li><strong>Milestone:</strong> CRAN packages · Oct 2025</li>
```
to:
```html
<li><strong>Milestone:</strong> CRAN packages · In progress</li>
```

**Step 3: Update TrialMatch LLM milestone**

Line 61: Change:
```html
<li><strong>Milestone:</strong> Clinic pilot across GI clinics · Fall 2025</li>
```
to:
```html
<li><strong>Milestone:</strong> Clinic pilot across GI clinics · In progress</li>
```

**Note:** The PI should provide actual current statuses. "In progress" is a safe placeholder that doesn't look stale.

**Step 4: Commit**

```bash
git add _pages/projects.md
git commit -m "fix: update stale Fall 2025 milestone dates on projects page"
```

---

### Task 6: Fix dead code.google.com links for legacy tools

ZINBA and hmmcov link to `code.google.com`, which was shut down in 2016.

**Files:**
- Modify: `_pages/software.md:99-100`

**Step 1: Update links to note archival**

Line 99-100: Change:
```html
<li><strong>ZINBA</strong> – Zero-inflated negative binomial algorithm detecting NGS-enriched regions. (<a href="https://code.google.com/p/zinba">Project</a>)</li>
<li><strong>hmmcov</strong> – HMM / AR-HMM procedures with variable selection for epigenetic enrichment. (<a href="https://code.google.com/p/hmmcov">Project</a>)</li>
```
to:
```html
<li><strong>ZINBA</strong> – Zero-inflated negative binomial algorithm detecting NGS-enriched regions. (Archived; formerly hosted on Google Code)</li>
<li><strong>hmmcov</strong> – HMM / AR-HMM procedures with variable selection for epigenetic enrichment. (Archived; formerly hosted on Google Code)</li>
```

**Step 2: Commit**

```bash
git add _pages/software.md
git commit -m "fix: replace dead code.google.com links with archived note"
```

---

### Task 7: Remove duplicate "For Prospective PhD Students" section on Teaching page

Two sections share the identical `<h2>For Prospective PhD Students</h2>` heading. The second (lines 149-153) only repeats the admissions link which is already accessible from the main section.

**Files:**
- Modify: `_pages/teaching.md:149-153`

**Step 1: Remove the duplicate section**

Delete lines 149-153:
```html
<section class="page-section">
  <h2>For Prospective PhD Students</h2>
  <p>Apply through the <a href="https://sph.unc.edu/bios/biostatistics/admissions/" target="_blank" rel="noopener">UNC Biostatistics PhD program</a>. Prospective students interested in the lab can email <a href="mailto:naim@unc.edu">naim@unc.edu</a> with questions about research directions, lab culture, or training philosophy.</p>
  <p><strong>For current UNC Biostatistics PhD trainees:</strong> Email directly to discuss joining the lab or participating in collaborative projects.</p>
</section>
```

**Step 2: Add the admissions link to the main section**

Append at the end of the main "For Prospective PhD Students" section (before the closing `</section>` at line 147), add:

```html
  <p class="mt-3">Apply through the <a href="https://sph.unc.edu/bios/biostatistics/admissions/" target="_blank" rel="noopener">UNC Biostatistics PhD program</a>. Prospective students interested in the lab can email <a href="mailto:naim@unc.edu">naim@unc.edu</a> with questions about research directions, lab culture, or training philosophy. <strong>Current UNC Biostatistics PhD trainees:</strong> email directly to discuss joining the lab or participating in collaborative projects.</p>
```

**Step 3: Commit**

```bash
git add _pages/teaching.md
git commit -m "fix: merge duplicate 'For Prospective PhD Students' sections on teaching page"
```

---

## Priority Tier 2: Clarifications & Consistency

### Task 8: Clarify ARPA-H funding figures site-wide

The `$30M` figure in `_data/metrics.yml` is used in the funding page overview via template variable, while `$28,120,143` appears as the specific TBCRC EVOLVE-BDT grant amount. Other pages use `$28M`. The relationship between these numbers is never explained.

**Files:**
- Modify: `_data/metrics.yml:28`
- Modify: `_pages/funding.md:18` (add parenthetical clarification)

**Step 1: Add clarifying parenthetical on funding page**

In `_pages/funding.md` line 18, change:
```html
<li>Co-PI and Statistical Member for ARPA-H ADAPT ({{ site.data.metrics.funding.arpa_h_total }} metastatic breast cancer platform trial, {{ site.data.metrics.funding.arpa_h_period }})</li>
```
to:
```html
<li>Co-PI and Statistical Member for ARPA-H ADAPT ({{ site.data.metrics.funding.arpa_h_total }} program; $28M to UNC for metastatic breast cancer platform trial, {{ site.data.metrics.funding.arpa_h_period }})</li>
```

**Step 2: Commit**

```bash
git add _pages/funding.md
git commit -m "fix: clarify ARPA-H ADAPT funding figures ($30M program vs $28M UNC share)"
```

---

## Priority Tier 3: Content Improvements (Lower Priority)

### Task 9: Add student achievement news entries

The `_news/` directory has 4 entries — none highlighting students. This is an easy win for prospective student recruitment.

**Files:**
- Create: `_news/YYYY-MM-DD-student-achievement.md` (1-2 entries)

**Step 1: Gather material from PI**

Ask PI for 1-2 recent student achievements to highlight. Good candidates:
- Euphy Wu PhD defense / graduation
- Amber Young awards, conference presentations
- Hillary Heiling or David Lim job placements
- Any student paper acceptances

**Step 2: Create news entries**

Example format (based on existing entries):
```markdown
---
layout: post
date: 2026-MM-DD
inline: true
related_posts: false
tags: [lab]
---

[Student Name] [achievement description].
```

**Step 3: Commit**

```bash
git add _news/
git commit -m "content: add student achievement news entries"
```

---

### Task 10: Add Euphy Wu LinkedIn link (if available)

All other alumni have LinkedIn links. Euphy's profile (`_members/about_euphy.md`) lacks one.

**Files:**
- Modify: `_members/about_euphy.md:24` (add linkedin field after email)

**Step 1: Obtain LinkedIn URL from PI or Euphy**

**Step 2: Add to profile frontmatter**

After line 24 (`email: euphyw@live.unc.edu`), add:
```yaml
    linkedin: [euphy-wu-linkedin-slug]
```

**Step 3: Commit**

```bash
git add _members/about_euphy.md
git commit -m "content: add LinkedIn link for Euphy Wu alumni profile"
```

---

## Claims Evaluated as NOT NECESSARY (No Action)

These claims from the review were verified as false or unnecessary:

| Claim | Why No Action |
|-------|--------------|
| CC-4: Copyright year mismatch | Footer uses `{{ site.time \| date: '%Y' }}` — fully dynamic |
| 1c: "Collaboration-Driven Methodology" is boilerplate | Prose already mentions Lineberger, specific methods, concrete context |
| 1d: Invited talks lack concrete findings | Talks already describe specific methods (RL, NMF-survival, LLM tools) |
| 4a: Research page needs more technical depth | Research page already has CLIA certification, patient counts, VAE-GLM details |
| 8c: Footer copyright year wrong | Same as CC-4 — dynamic |
| CC-2: Author name should be bold not italic | al-folio convention is italic `<em>` highlighting; this is standard |
| 1a: Reduce 3 CTAs to 2 | Subjective design preference; 3 buttons is normal |
| 1b: Three-column section duplicates Research | About version is already higher-level; serves as visual index |
| 2b: PhD training intro is bare | Section already has distinctive research areas listed + email contact |
| 4c: D3.js map may not render | Has graceful fallback message if JS unavailable |

---

## Execution Order

Tasks 1-7 can be done in any order (independent). Recommended sequence:

1. **Tasks 1-2** (broken references) — highest visibility fixes
2. **Tasks 3-4** (CV/date errors) — factual accuracy, *Task 4 needs PI input*
3. **Task 5** (stale dates) — *may need PI input for actual statuses*
4. **Tasks 6-7** (dead links, teaching duplicate) — straightforward
5. **Task 8** (funding clarification) — *may need PI input on exact figures*
6. **Tasks 9-10** (content additions) — *need PI input for content/URLs*

**PI-dependent tasks:** 4, 5 (specific statuses), 8 (confirm figures), 9, 10
