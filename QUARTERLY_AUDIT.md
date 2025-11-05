# Quarterly Content Audit Checklist

**Schedule**: First week of each quarter (January, April, July, October)
**Estimated Time**: 2-3 hours
**Last Completed**: [Date]
**Next Due**: [Date]

---

## Overview

This quarterly audit ensures your website stays current with recent achievements, accurate information, and working links. Complete this checklist at the start of each quarter (Jan, Apr, Jul, Oct).

---

## PART 1: Team Updates (30 min)

### Current Team Members

- [ ] **Check team member photos** (`_pages/team.md`)
  - [ ] All photos are professional quality (>14KB)
  - [ ] No placeholder images (2.2KB generic photos)
  - [ ] Photos are current (within last 2 years)
  - [ ] Alt text is descriptive for all photos

- [ ] **Verify team member information**
  - [ ] Current students: Names, start years, research topics
  - [ ] Postdocs: Names, affiliations, projects
  - [ ] Staff: Names, titles, roles

- [ ] **Update student progress**
  - [ ] Dissertation topics accurate
  - [ ] Recent milestones (prelim exams, proposals, defenses)
  - [ ] Conference presentations or awards

### Alumni Section

- [ ] **New graduates** (if any this quarter)
  - [ ] Move from "Current" to "Alumni" section
  - [ ] Add graduation year and degree
  - [ ] Add first position after graduation
  - [ ] Update count: "X PhD graduates (2016-2024)" → update year range

- [ ] **Alumni updates** (optional)
  - [ ] Check LinkedIn for career moves
  - [ ] Update positions if significantly changed
  - [ ] Add notable achievements (promotions, awards)

**Files to Update**: `_pages/team.md`, `_pages/teaching.md` (mentoring section)

---

## PART 2: Publications Updates (30-45 min)

### Recent Publications

- [ ] **Add new publications** since last quarter
  - [ ] Check Google Scholar for recent papers
  - [ ] Review automated sync PRs (if using workflows)
  - [ ] Manually add any missing publications to `_bibliography/papers.bib`

- [ ] **Update publication highlights** (`_pages/about.md`)
  - [ ] Select 3-5 most recent/impactful papers
  - [ ] Update year range if needed
  - [ ] Ensure links to DOIs work

- [ ] **Add keywords for thematic filtering** (optional)
  - [ ] Tag publications with: `trials`, `mixed-models`, `genomics`, `machine-learning`, `epigenomics`
  - [ ] Enables thematic browsing on publications page

### Metrics Update

- [ ] **Google Scholar metrics** (`_pages/publications.md`)
  - [ ] Current h-index: _____ (update if changed)
  - [ ] Total citations: _____ (update if milestone reached: 5K → 6K, etc.)
  - [ ] Publications count: _____ (update if 75+ → 80+, etc.)

- [ ] **Featured publications** (`_pages/publications.md`)
  - [ ] Rotate to feature recent high-impact papers
  - [ ] Ensure at least one paper from last 12 months is featured

**Files to Update**: `_bibliography/papers.bib`, `_pages/publications.md`, `_pages/about.md`

---

## PART 3: Funding & Grants Updates (20-30 min)

### New Grants

- [ ] **Add new awards** since last quarter (`_pages/funding.md`)
  - [ ] Grant title, agency, award amount
  - [ ] Period of performance
  - [ ] Role (PI, Co-PI, Co-I, Core Leader)
  - [ ] Brief description
  - [ ] Link to news coverage if available

- [ ] **Update grant status**
  - [ ] Move completed grants from "Active" to "Completed" section
  - [ ] Update end dates if extended
  - [ ] Note any renewals or supplements

### Funding Summary

- [ ] **Recalculate funding metrics** (top of funding page)
  - [ ] Largest single award: $_____ (update if new large grant)
  - [ ] Total active grants: _____ (count)
  - [ ] Combined active funding: $_____ (sum all active)
  - [ ] SPORE Core leadership roles: _____ (count)

**Files to Update**: `_pages/funding.md`

---

## PART 4: Software & Tools Updates (15-20 min)

### Package Updates

- [ ] **Check CRAN packages** for new versions
  - [ ] glmmPen: Current version _____
  - [ ] epigraHMM: Current version _____
  - [ ] dlglm: Current version _____
  - [ ] Other packages: _____

- [ ] **Update version badges** (auto-update via shields.io)
  - [ ] Verify badges are displaying correctly
  - [ ] Check for any deprecated packages

- [ ] **Add new software** (if released this quarter)
  - [ ] Package name and description
  - [ ] CRAN/GitHub/Bioconductor links
  - [ ] Citation and DOI
  - [ ] Vignettes and documentation links

### Documentation Links

- [ ] **Test all software links** (`_pages/software.md`)
  - [ ] CRAN package pages load
  - [ ] GitHub repositories accessible
  - [ ] Documentation links work
  - [ ] Publication DOIs resolve correctly

**Files to Update**: `_pages/software.md`

---

## PART 5: Research Themes Updates (15 min)

### Thematic Content

- [ ] **Review research themes** (`_pages/research.md`)
  - [ ] Are all 4 themes still active?
  - [ ] Any new major projects to highlight?
  - [ ] Update "Active Trials" section with current status

- [ ] **Update collaborations**
  - [ ] New collaborators or institutions
  - [ ] Major consortium memberships

- [ ] **Highlight recent grants/publications** in relevant themes
  - [ ] Add to "Key Contributions" sections
  - [ ] Link to new software or funding pages

**Files to Update**: `_pages/research.md`

---

## PART 6: News & Blog Updates (20-30 min)

### Quarterly Blog Post

- [ ] **Write quarterly lab update** (see `BLOG_POSTING_GUIDE.md`)
  - [ ] New publications (methodology + collaborative)
  - [ ] Grant awards or renewals
  - [ ] Student/postdoc achievements
  - [ ] Software releases
  - [ ] Upcoming conferences and talks
  - [ ] Collaborative highlights
  - [ ] Recruitment announcements

- [ ] **Use blog helper script**:
  ```bash
  ./bin/new-update.sh "Lab Updates Q[X] [YEAR]"
  ```

- [ ] **Cross-post to social media**
  - [ ] Twitter/X thread (2-3 tweets)
  - [ ] LinkedIn post (300-500 words)
  - [ ] Tag collaborators and institutions

### Archive Old News

- [ ] **Homepage news items** (`_pages/about.md`)
  - [ ] Keep only last 3-6 months of news
  - [ ] Move older items to blog archive
  - [ ] Ensure "Recent Highlights" section is current

**Files to Update**: `_posts/YYYY-MM-DD-lab-updates-qX-YYYY.md`, `_pages/about.md`

---

## PART 7: Link Checking (15-20 min)

### External Links

- [ ] **Test all external links** on key pages
  - [ ] About/Homepage: UNC affiliations, collaborator links
  - [ ] Publications: DOI links, journal pages
  - [ ] Software: CRAN, GitHub, documentation
  - [ ] Funding: News coverage, agency websites
  - [ ] Teaching: Course websites, external resources
  - [ ] Team: LinkedIn profiles, personal websites

- [ ] **Check internal links**
  - [ ] Navigation menu links work
  - [ ] Cross-page references (research → software → publications)
  - [ ] Blog post internal links

### Automated Link Checking

- [ ] **Review GitHub Actions "Broken Links" workflow results**
  - [ ] Check workflow runs in Actions tab
  - [ ] Fix any reported broken links
  - [ ] Update or remove outdated references

**Tools**:
- Manual checking
- GitHub Actions: `.github/workflows/broken-links.yml`
- Online: [W3C Link Checker](https://validator.w3.org/checklink)

---

## PART 8: Metrics & Analytics Review (15-20 min)

### Google Analytics

- [ ] **Review traffic for last quarter**
  - [ ] Total visitors: _____
  - [ ] Top pages: _____
  - [ ] Traffic sources (organic, direct, referral)
  - [ ] Average session duration: _____

- [ ] **Identify trends**
  - [ ] Which pages are most popular?
  - [ ] Any unexpected spikes or drops?
  - [ ] Where are visitors coming from?

### Google Search Console (if set up)

- [ ] **Search performance**
  - [ ] Top search queries
  - [ ] Average position for key terms
  - [ ] Click-through rate (CTR)

- [ ] **Coverage issues**
  - [ ] Any crawl errors?
  - [ ] Pages excluded from index?
  - [ ] Mobile usability issues?

**Actions Based on Data**:
- If certain pages have high traffic: Keep content fresh
- If search rankings dropped: Review SEO, add content
- If software page popular: Highlight new packages

---

## PART 9: Technical Maintenance (10-15 min)

### GitHub Actions Workflows

- [ ] **Review automated PRs from last quarter**
  - [ ] How many publication sync PRs? _____
  - [ ] How many merged vs. closed? _____
  - [ ] Any workflow failures?

- [ ] **Check workflow health**
  - [ ] Recent runs successful
  - [ ] No rate limiting issues
  - [ ] Dependencies up to date

### Jekyll Build

- [ ] **Test local build** (optional but recommended)
  ```bash
  bundle exec jekyll serve
  ```
  - [ ] No build errors
  - [ ] All pages render correctly
  - [ ] No deprecated warnings

### Dependencies

- [ ] **Update Ruby gems** (if needed)
  ```bash
  bundle update
  ```

- [ ] **Update Python packages** (for automation scripts)
  ```bash
  pip install -r requirements.txt --upgrade
  ```

**Note**: Only update if you encounter issues. Jekyll and GitHub Pages handle most updates automatically.

---

## PART 10: Final Review (10 min)

### Quality Check

- [ ] **Proofread recent changes**
  - [ ] No typos in new content
  - [ ] Proper formatting (markdown, links)
  - [ ] Dates are accurate

- [ ] **Mobile responsiveness**
  - [ ] Check site on mobile device
  - [ ] Verify new content displays well
  - [ ] Navigation works on small screens

- [ ] **Accessibility**
  - [ ] All new images have alt text
  - [ ] Headings are hierarchical (H2 → H3, not H2 → H4)
  - [ ] Links are descriptive (not "click here")

### Commit Changes

- [ ] **Git commit all updates**
  ```bash
  git add .
  git commit -m "Quarterly content audit Q[X] [YEAR]

  - Updated team: [changes]
  - Added publications: [titles]
  - New grants: [awards]
  - Software updates: [versions]
  - Quarterly blog post
  "
  git push
  ```

- [ ] **Verify deployment**
  - [ ] GitHub Pages build successful
  - [ ] Changes visible on live site (allow 1-2 min)

---

## Quarterly Audit Schedule

### Q1 (January)

**Focus**: Start of year updates
- [ ] Annual metrics reset (new year)
- [ ] Teaching page updates (new semester courses)
- [ ] Recruitment announcements (PhD admissions)

### Q2 (April)

**Focus**: Spring accomplishments
- [ ] Add spring conference presentations
- [ ] Update student defenses/graduations (May/June)
- [ ] Summer research announcements

### Q3 (July)

**Focus**: Mid-year review
- [ ] Update funding page (July 1 grants)
- [ ] Software releases (mid-year updates)
- [ ] Fall recruitment preview

### Q4 (October)

**Focus**: Year-end accomplishments
- [ ] Highlight major grants awarded
- [ ] Update publications (end-of-year push)
- [ ] Plan for annual strategic review (next quarter)

---

## Quick Reference: Files to Update Each Quarter

### Always Update
- `_bibliography/papers.bib` - New publications
- `_pages/publications.md` - Metrics, featured papers
- `_posts/YYYY-MM-DD-lab-updates-qX-YYYY.md` - New blog post

### Often Update
- `_pages/team.md` - Student progress, new members
- `_pages/funding.md` - New grants, completed grants
- `_pages/software.md` - New packages, version updates

### Sometimes Update
- `_pages/research.md` - Major new projects
- `_pages/teaching.md` - New courses, student graduations
- `_pages/about.md` - Homepage highlights, news items

### Rarely Update
- `_config.yml` - Site settings (only if major changes)
- `_sass/_custom.scss` - Styling (only if design changes)

---

## Tracking Your Progress

**Use this table to track completion**:

| Quarter | Date Completed | Time Taken | Major Updates | Notes |
|---------|---------------|------------|---------------|-------|
| Q1 2026 | | | | |
| Q2 2026 | | | | |
| Q3 2026 | | | | |
| Q4 2026 | | | | |

**Tips for Efficiency**:
- Set a calendar reminder for the first Monday of each quarter
- Block out 2-3 hours of uninterrupted time
- Work through checklist sequentially (don't skip sections)
- Use automated tools (link checkers, Google Analytics)
- Keep notes on what took longest (streamline next time)

---

## Questions or Issues?

- **Technical problems**: Consult `AUTOMATION_GUIDE.md`, `SEO_GUIDE.md`
- **Blog posting**: See `BLOG_POSTING_GUIDE.md`
- **Strategic decisions**: Schedule annual review (see `ANNUAL_REVIEW.md`)

---

**Last Updated**: November 2025
**Next Review**: January 2026 (Q1 audit)
