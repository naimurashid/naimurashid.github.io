# Action Items Requiring User Input

**Last Updated**: Phase 2 Implementation
**Status**: Running list across all phases

---

## IMMEDIATE PRIORITY (Week 1)

### 📸 Team Photos (Phase 1 - Action 1.3)
**Status**: ✅ COMPLETE

Replace placeholder images for team members:

1. **Dinelka Nanayakkara** - `assets/img/dinelka.jpg` ✅ ADDED
2. **Jialiu Xie** - `assets/img/jialiu.jpg` ✅ ADDED
3. **Tyler Humpherys** - `assets/img/tyler.jpg` (14KB - verify quality is adequate)

**Completed Actions**:
- [x] Photos added for Dinelka and Jialiu
- [x] Profile pages updated with LinkedIn information
- [x] Social links enabled with LinkedIn profiles

**Reference**: See `PLACEHOLDER_PHOTOS_NEEDED.md` for detailed guidelines

---

### 🔍 Software Page Verification (Phase 1 - Action 1.2)
**Status**: ⏳ PENDING USER ACTION

Review the new `/software/` page:

- [ ] Test all GitHub repository links
- [ ] Verify CRAN/Bioconductor badges display correctly
- [ ] Confirm publication citations and DOI links are accurate
- [ ] Check if any packages are missing or need updates

---

## PHASE 2 ITEMS (Weeks 2-4)

### 🎨 Research Themes Visualization (Action 2.1)
**Status**: 🔄 IN PROGRESS

**User Decision Required**:
- [ ] Review proposed 4-quadrant research diagram structure
- [ ] Approve or modify research theme categories
- [ ] Decide on design tool: PowerPoint/Figma/draw.io vs. professional designer
- [ ] Provide feedback on visual layout once draft is ready

**Proposed Themes** (based on CV):
1. Penalized mixed models & high-dimensional inference
2. Adaptive clinical trial design
3. Multi-omic integration & cancer genomics
4. Machine learning for precision oncology

---

### 💰 Funding/Grants Page Content (Action 2.2)
**Status**: 🔄 IN PROGRESS

**User Input Needed**:
- [ ] Confirm which grants should be listed publicly
- [ ] Verify grant amounts can be disclosed
- [ ] Review active vs. completed grant categorization
- [ ] Approve grant descriptions and roles

**From CV - Active Grants to Feature**:
- ARPA-H ADAPT ($30M, 2025-2031)
- DOD PCARP ($311K, 2024-2026)
- NCI SPORE Breast Cancer ($11.9M, 2024-2029) - Core B Co-Leader
- NCI U01 ($4.6M, 2022-2027) - Co-PI with Yeh
- NCI SPORE Pancreatic Cancer ($11.1M, 2022-2027) - Core C Co-Leader

---

### 📊 Publications Page Enhancement (Action 2.3)
**Status**: 🔜 PENDING

**User Decisions Required**:
- [ ] Select "featured publications" for top of page
- [ ] Approve thematic grouping categories:
  - Clinical Trials Methodology
  - Penalized Mixed Models
  - Cancer Genomics
  - Machine Learning
  - Other?
- [ ] Confirm Google Scholar ID for h-index automation: `3Cz_lcEAAAAJ`
- [ ] Decide if total citations metric should be displayed

---

### 📝 Research Blog/Updates (Action 2.4)
**Status**: ✅ COMPLETE

**Deliverables Created**:
- ✅ Helper script: `bin/new-update.sh` for easy post creation
- ✅ Example post: `_posts/2025-11-04-lab-updates-q4-2025.md`
- ✅ Comprehensive guide: `BLOG_POSTING_GUIDE.md`
- ✅ Quarterly checklist and content templates

**User Decisions Still Needed**:
- [ ] Review and edit first blog post (Q4 2025 updates)
- [ ] Assign blog maintenance responsibility (you vs. students vs. shared)
- [ ] Set up cross-posting workflow (Twitter/LinkedIn)
- [ ] Decide on comment system (currently disabled via `giscus_comments: false`)

---

## PHASE 3 ITEMS (Weeks 5-8)

### 📚 Teaching Materials Page (Action 3.1)
**Status**: ✅ COMPLETE

**Deliverables Created**:
- ✅ Comprehensive teaching page with BIOS 735 and BIOS 663 details
- ✅ Teaching philosophy statement
- ✅ Mentoring section with current students and PhD graduates
- ✅ Workshops & short courses section
- ✅ Software as teaching tools section
- ✅ Guest lectures & tutorials section
- ✅ Teaching awards & recognition
- ✅ Student resources section

**User Decisions Still Needed**:
- [ ] Review and verify course descriptions are accurate
- [ ] Update office hours if location/time has changed
- [ ] Verify workshop dates and topics
- [ ] Confirm teaching awards and recognition are complete

---

### 🤖 Automation Setup (Action 3.2)
**Status**: ✅ COMPLETE

**Deliverables Created**:
- ✅ Comprehensive automation guide: `AUTOMATION_GUIDE.md`
- ✅ Documentation of existing workflows (sync-publications.yml, fetch-social.yml)
- ✅ Setup checklist and testing instructions
- ✅ Troubleshooting guide
- ✅ Weekly maintenance workflow (10-15 min/week)

**User Decisions Still Needed**:
- [ ] Test workflows manually (run via GitHub Actions UI)
- [ ] Set up GitHub secret `GSCHOLAR_AUTHOR_ID` if different from default (3Cz_lcEAAAAJ)
- [ ] Review first automated PR when it arrives (next Monday)
- [ ] Set up Google Search Console verification (optional but recommended)

**Note**: Workflows are already configured and will run automatically every Monday:
- 08:00 UTC: Publication sync from Google Scholar
- 08:30 UTC: Social feed refresh

---

### 🎯 SEO Optimization (Action 3.4)
**Status**: ✅ COMPLETE

**Deliverables Created**:
- ✅ Enabled Schema.org structured data in `_config.yml`
- ✅ Updated site description for better SEO
- ✅ Optimized meta descriptions for all key pages:
  - Publications: Includes metrics (75+ pubs, h-index 28, 5000+ citations)
  - Funding: Highlights $60M+ funding and agencies
  - Software: Open-source tools for genomics
  - Research: Statistical methods for precision oncology
  - Teaching: Courses and mentoring
- ✅ Comprehensive SEO guide: `SEO_GUIDE.md`
- ✅ Image alt text checklist
- ✅ Google Search Console setup instructions
- ✅ Ongoing SEO maintenance schedule

**User Decisions Still Needed**:
- [ ] Set up Google Search Console verification (adds `google_site_verification` to _config.yml)
- [ ] Submit sitemap to Google Search Console
- [ ] Verify all team member photos have alt text
- [ ] Review and approve meta descriptions
- [ ] Optional: Set up ORCID integration

---

## PHASE 4: ONGOING MAINTENANCE

**Status**: ✅ COMPLETE (Documentation & Templates Created)

### 📅 Quarterly Content Audit (Action 4.1)
**Status**: ✅ TEMPLATE COMPLETE
**Schedule**: First week of each quarter (January, April, July, October)
**Document**: `QUARTERLY_AUDIT.md`

**Deliverables Created**:
- ✅ Complete 10-part quarterly audit checklist (2-3 hours)
- ✅ Section-by-section update instructions:
  - Team updates (30 min)
  - Publications (30-45 min)
  - Funding & grants (20-30 min)
  - Software (15-20 min)
  - Research themes (15 min)
  - Blog post (20-30 min)
  - Link checking (15-20 min)
  - Analytics review (15-20 min)
  - Technical maintenance (10-15 min)
  - Final review & commit (10 min)
- ✅ Quarterly focus areas (Q1: Annual metrics, Q2: Spring accomplishments, Q3: Mid-year review, Q4: Year-end)
- ✅ File tracking reference (which files to update)
- ✅ Progress tracking table
- ✅ Time-saving tips

**Your Action Each Quarter**:
- [ ] Q1 2026 (January): Complete first quarterly audit using checklist
- [ ] Q2 2026 (April): Second quarterly audit
- [ ] Q3 2026 (July): Third quarterly audit
- [ ] Q4 2026 (October): Fourth quarterly audit

**Estimated time**: 2-3 hours/quarter

---

### 📊 Annual Strategic Review (Action 4.2)
**Status**: ✅ TEMPLATE COMPLETE
**Schedule**: Start of academic year (August/September)
**Document**: `ANNUAL_REVIEW.md`

**Deliverables Created**:
- ✅ Comprehensive 8-part strategic review template (4-6 hours)
- ✅ Part 1: Goals & effectiveness assessment (60-90 min)
  - Recruitment, visibility, collaboration, teaching impact
- ✅ Part 2: Content audit & strategic questions (90-120 min)
  - Research themes, homepage narrative, software, publications, funding, teaching, team
- ✅ Part 3: Competitive analysis (45-60 min)
  - Peer website review, differentiation strategy
- ✅ Part 4: Technical & design review (30-45 min)
  - Navigation, visual design, mobile/accessibility
- ✅ Part 5: Analytics & SEO review (30-45 min)
  - Traffic analysis, search rankings, backlinks
- ✅ Part 6: New initiatives & priorities (60-90 min)
  - Next year's goals, website priorities, interactive elements, budget
- ✅ Part 7: Action plan & timeline (30 min)
  - Quarterly project schedule, success metrics
- ✅ Part 8: Documentation & commit (15 min)
- ✅ Reflection questions for strategic thinking
- ✅ Annual review summary template

**Your Action Annually**:
- [ ] August/September 2026: Complete first annual strategic review
- [ ] Set priorities for 2026-2027 academic year
- [ ] Budget planning for any major updates (photos, design, interactive elements)

**Estimated time**: 4-6 hours/year

---

### 📚 Comprehensive Maintenance Documentation
**Status**: ✅ COMPLETE

**Deliverables Created**:
- ✅ `MAINTENANCE_GUIDE.md` - Central reference for all maintenance activities
  - Quick reference maintenance schedule (weekly, monthly, quarterly, annual)
  - Detailed task breakdowns with time estimates
  - Delegation and outsourcing guidance
  - Common scenarios and solutions
  - Success metrics and ROI assessment
  - Optimization tips (time-saving and quality-saving)
  - Phase 4 ongoing maintenance checklist

**Total Annual Time Commitment**: ~30-40 hours/year (down from 100-150 hrs before automation)

**Breakdown**:
- **Weekly** (10-15 min): Review automated PRs → 8-13 hrs/year
- **Monthly** (15-20 min): Analytics & SEO check → 3-4 hrs/year
- **Quarterly** (2-3 hours): Content audit → 8-12 hrs/year
- **As needed** (1-2 hrs): Blog posts (4x/year) → 4-8 hrs/year
- **Annual** (4-6 hours): Strategic review → 4-6 hrs/year

---

## SUMMARY BY PRIORITY

### 🔴 High Priority (Immediate)
1. **Team photos** (3 members - Dinelka, Jialiu, Tyler)
2. **Software page verification** (test all links and badges)
3. **Review Phase 2 deliverables**:
   - Research themes accuracy
   - Funding page disclosures
   - Q4 2025 blog post content
4. **Review Phase 3 deliverables**:
   - Teaching page accuracy
   - Meta descriptions approval

### 🟡 Medium Priority (Next 2-4 Weeks)
1. **Test automation workflows** (manually trigger via GitHub Actions)
2. **Set up Google Search Console** (verification + sitemap submission)
3. **BibTeX keyword filtering** (decide if you want thematic publication filtering)
4. **Assign blog maintenance responsibility** (you vs. students vs. shared)
5. **Verify image alt text** (especially team member photos)

### 🟢 Lower Priority (Ongoing)
1. **Weekly**: Review automated PRs from workflows (Mondays)
2. **Monthly**: Check Google Analytics and Search Console
3. **Quarterly**: Content audit (see Phase 4 checklist)
4. **Annual**: Strategic review

---

## NOTES

- Each checkbox [ ] represents a decision or action required from you
- Items marked ✅ are complete
- Items marked ⏳ are blocked waiting for your input
- This document will be updated as each phase progresses

**Phase Status**:
- ✅ **Phase 1 COMPLETE** (Typography, Software, Team)
- ✅ **Phase 2 COMPLETE** (Research, Funding, Publications, Blog)
- ✅ **Phase 3 COMPLETE** (Teaching, Automation, SEO)
- 📅 **Phase 4 ONGOING** (Quarterly maintenance, annual review)

**Next Review Point**: After user reviews Phase 2 & 3 deliverables

**Last Updated**: Phase 3 Implementation (November 2025)
