Faculty Website Review & Strategic Action Plan

Perspective: Senior Biostatistics Faculty Member in Cancer Research
Part 1: The Purpose of an Academic Website in Our Field

As a senior faculty member in biostatistics with cancer research applications, I can tell you that your website serves multiple critical strategic functions:
Grant Acquisition & Funding

    First impression for program officers: NIH/NCI program officers often Google you before reviewing proposals
    Demonstrates productivity: Active software repositories, recent publications, and funded projects signal viability
    Shows collaborative infrastructure: Team composition and multi-institutional projects demonstrate capacity
    Validates expertise:Methodological focus areas need to align with grant aims

Research Dissemination & Impact

    Software adoption: R packages/tools need visibility for citations and user base growth
    Reproducible research: GitHub links and vignettes increase transparency and trust
    Collaboration recruitment: Other investigators find you through web searches for specific methods
    Altmetrics boost: Easy-to-find publications get more citations

Teaching & Mentorship

    Student recruitment: PhD applicants evaluate lab culture and research opportunities
    Postdoc hiring: Career placement records and current projects attract top candidates
    Course visibility: Materials demonstrate pedagogical contributions for teaching awards

Career Advancement & Recognition

    Promotion packets: External reviewers consult your site
    Named professorships: Search committees assess breadth and impact
    Award nominations: Colleagues use your site to write nomination letters
    Editorial boards: Journal editors evaluate expertise areas

Professional Service & Visibility

    Conference invitations: Organizers find speakers through web searches
    Consulting opportunities: Industry partners identify expertise
    Media requests: Journalists seek expert commentary
    Community building: Students see your work and join the field

Part 2: Review of Current Rashid Lab Website

Let me examine what you have now...
Bashgit log origin/claude/list-all-b-011CUoRixndogJtBRfpRWUjL --oneline -5
b185e88 Remove SCISSORS from publication highlights
48ad775 Implement review feedback and enhance site content
80b4492 Refine site narrative and expand team profiles... +2 lines
Bashgit diff ecb21bd..origin/claude/list-all-b-011CUoRixndogJtBRfpRWUjL --stat | tail -20
 bin/sync_publications.py                           | 143 +++++++
 requirements.txt                                   |   4 +
 59 files changed, 1776 insertions(+), 540 deletions(-)... +17 lines
Current Strengths ✅

Based on my review and the analysis in this thread:

    Strong Technical Foundation
        Modern GitHub Pages platform (version controlled, reproducible)
        Clean al-folio theme (widely used in academia)
        Automated publication syncing capability
        Google Analytics enabled for traffic tracking

    Good Content Coverage
        Team profiles with photos and bios
        Publications integrated via Jekyll-Scholar
        News/announcements section
        Project descriptions (glmmPen, PurIST)
        Contact information and office hours

    Professional Presentation
        Unified color scheme and branding
        Rashid Lab logo prominently displayed
        Responsive design
        Social media integration

    Recent Enhancements (on evaluation branch)
        Expanded team member profiles (7 new members)
        Publication highlights feature
        Gillings news integration
        Hero panel with key metrics ($28M ADAPT, 25 grants, 50+ pubs)
        Custom styling for visual impact

Critical Gaps ⚠️

Missing Elements that Hurt Your Strategic Goals:

    No Software/Tools Showcase
        You mentioned repositories in earlier analysis, but no prominent software page
        No links to GitHub packages (glmmPen, PurIST should have CRAN/GitHub badges)
        Missing tutorials, vignettes, or documentation links
        Impact: Reduces software citations and adoption

    Weak Research Narrative
        No clear thematic research areas diagram
        Projects page not in navigation initially (fixed in recent commit)
        No visual representation of methodological expertise
        Impact: Collaborators can't quickly assess fit

    Incomplete Team Information
        Some team members have placeholder images (dinelka.jpg, jialiu.jpg, tyler.jpg are 2KB - placeholders)
        No alumni section with career outcomes
        Impact: Reduces perceived mentoring success for recruitment

    Limited Funding Visibility
        No grants page or funding acknowledgments section (beyond hero panel)
        Impact: Misses opportunity to demonstrate sustained productivity

    Teaching Materials Absent
        Teaching page exists but content unclear
        No course materials, syllabi, or student resources
        Impact: Reduces teaching portfolio evidence

    Technical Inconsistencies
        Font consistency issues (detailed in previous analysis)
        Duplicate CSS definitions in _custom.scss
        No explicit font-family declarations
        Impact: Unprofessional appearance, maintenance difficulty

Part 3: Synthesis of Recommendations from This Thread
From Competitor Analysis:

Leading biostatistics labs show these must-haves:

    Software prominently featured (80%+ of sites)
        GitHub repository links
        CRAN badges
        Interactive Shiny apps
        Documentation/tutorials

    Clear research themes (60%+ use visual diagrams)
        3-5 major research areas
        Methods + applications clearly stated
        Visual organization (quadrants, themes)

    Team showcase with outcomes (90%+ of sites)
        Current members with photos
        Alumni section tracking placements
        Demonstrates mentoring success

    Recent activity signals (50%+ of sites)
        News section updated regularly
        Recent publications highlighted
        Job postings for active labs

From Design Analysis:

Typography & Visual Issues:

    Fragmented font scale (0.9rem, 0.95rem, 1.05rem increments)
    Duplicate CSS definitions with conflicts
    Missing explicit font-family declarations
    Inconsistent color values (hardcoded vs. variables)

Structural Issues:

    Homepage custom components disconnected from rest of site
    Inconsistent grid systems across components
    Mixed border and shadow patterns

Part 4: Strategic Action Plan

As a senior colleague, here's what I recommend—prioritized by impact:
PHASE 1: Critical Fixes (Week 1-2) — Foundation
Action 1.1: Fix Typography System ⭐⭐⭐

Why: Professional appearance is non-negotiable. Current inconsistencies signal "unfinished work."

Tasks:

    Add explicit font declarations to _sass/_base.scss:

    body {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
      font-family: 'Roboto Slab', 'Roboto', serif;
    }

    Consolidate _sass/_custom.scss:
        Remove duplicate .publication-highlights definitions (there are 2)
        Standardize font sizes to core scale: 0.875rem, 1rem, 1.125rem, 1.25rem, 1.5rem, 2rem
        Replace hardcoded colors with CSS variables

    Create color variables for blues:

    --global-primary-blue: #204c89;
    --global-accent-blue: #0b4ea2;

Deliverable: Clean, maintainable CSS with consistent typography Time: 4-6 hours
Action 1.2: Add Software/Tools Page ⭐⭐⭐

Why: This is the #1 missing piece compared to peer institutions. Software is your research currency.

Tasks:

    Create _pages/software.md:

    ---
    layout: page
    title: software
    permalink: /software/
    nav: true
    nav_order: 4
    ---

    ## R Packages

    ### glmmPen
    [![CRAN](https://www.r-pkg.org/badges/version/glmmPen)](https://cran.r-project.org/package=glmmPen)
    [![GitHub](https://img.shields.io/github/stars/...)](...)

    Penalized generalized linear mixed models...

    - [CRAN](link)
    - [GitHub](link)
    - [Documentation](link)
    - [Vignette](link)

    ### PurIST
    [Similar structure]

    ## Web Applications
    [Shiny apps if any]

    ## Code Repositories
    [GitHub org or notable repos]

    Add badges using shields.io

    Link from homepage hero panel

Deliverable: Prominent software showcase Time: 3-4 hours
Action 1.3: Complete Team Member Profiles ⭐⭐

Why: Placeholder images hurt credibility. Current state suggests disorganization.

Tasks:

    Replace placeholder images:
        dinelka.jpg (2KB → actual photo)
        jialiu.jpg (2KB → actual photo)
        tyler.jpg (14KB but check if adequate quality)

    Add alumni section to _pages/team.md:

    ## Alumni

    ### Postdoctoral Fellows
    - **Dr. [Name]** - Now Assistant Professor, [University]
    - **Dr. [Name]** - Senior Statistician, [Company]

    ### PhD Students
    - **Dr. [Name]** (2023) - Now [position]

    Ensure all current members have complete profiles

Deliverable: Professional, complete team page Time: 2-3 hours (+ time to get photos)
PHASE 2: Content Enhancement (Week 3-4) — Impact
Action 2.1: Create Research Themes Visualization ⭐⭐⭐

Why: 60% of top labs use visual research organization. Makes expertise immediately clear.

Tasks:

    Design 4-quadrant research diagram (like BayesRx example):
        Quadrant 1: Penalized mixed models & high-dimensional inference
        Quadrant 2: Adaptive clinical trial design
        Quadrant 3: Multi-omic integration & cancer genomics
        Quadrant 4: Machine learning for precision oncology

    Create visual in PowerPoint/Figma

    Add to homepage after hero panel

    Link quadrants to relevant projects/publications

Deliverable: Clear research identity Time: 4-5 hours
Action 2.2: Add Funding/Grants Page ⭐⭐

Why: Demonstrates sustained productivity and capacity. Important for collaborators and promotion.

Tasks:

    Create _pages/funding.md:
        Current grants (title, agency, role, amount, years)
        Completed grants
        Total funding secured

    Organize by:
        Active funding
        Completed projects
        Collaborative grants

Example structure:

## Active Funding

### ARPA-H ADAPT Platform
- **Amount**: $28M (total program)
- **Role**: Statistical Lead
- **Period**: 2024-2029
- **Focus**: Adaptive platform trial for metastatic breast cancer

### NCI SPORE - Pancreatic Cancer
- **Amount**: [amount]
- **Role**: Biostatistics Core Co-Director
...

Deliverable: Comprehensive funding record Time: 3-4 hours
Action 2.3: Enhance Publications Page ⭐⭐

Why: Current page is auto-generated list. Needs curation for impact.

Tasks:

    Add featured/selected publications section at top

    Group by theme (not just year):
        Clinical Trials Methodology
        Penalized Mixed Models
        Cancer Genomics
        Machine Learning

    Add paper statistics to homepage:
        Google Scholar h-index
        Total citations
        Update regularly via automation

Deliverable: Curated, impactful publications showcase Time: 2-3 hours
Action 2.4: Create Research Blog/Updates ⭐

Why: Shows active lab. Good for SEO and engagement.

Tasks:

    Start quarterly lab updates:
        New publications
        Software releases
        Grants awarded
        Student/postdoc achievements
        Conference presentations

    Add to existing blog structure

    Cross-post to Twitter/LinkedIn

Deliverable: Active research presence Time: 1-2 hours/quarter ongoing
PHASE 3: Advanced Features (Week 5-8) — Excellence
Action 3.1: Add Teaching Materials Page ⭐

Why: Demonstrates pedagogical contributions for teaching awards and tenure/promotion.

Tasks:

    Populate _pages/teaching.md:
        Course listings (BIOS xxx, titles)
        Syllabi (if public)
        Lecture notes or slides (selected)
        Student resources
        Mentoring philosophy

    Add links to:
        Workshops/short courses
        Tutorial videos
        Software documentation as teaching tool

Deliverable: Complete teaching portfolio Time: 3-4 hours
Action 3.2: Implement Automation ⭐

Why: You've added scripts but not enabled workflows. Reduces maintenance burden.

Tasks:

    Enable GitHub Actions workflows:
        .github/workflows/sync-publications.yml (already created)
        .github/workflows/fetch-social.yml (already created)

    Test automation:
        Publications auto-update from BibTeX/API
        Social feed auto-updates

    Schedule:
        Weekly: Check for new publications
        Monthly: Update metrics

Deliverable: Self-maintaining content Time: 4-5 hours setup + testing
Action 3.3: Add Interactive Elements ⭐

Why: Modern, engaging. Differentiates from static sites.

Tasks:

    Create Shiny apps for key methods (if not existing):
        glmmPen simulator/demonstrator
        Sample size calculator
        Interactive visualizations

    Embed in software page

    Link from relevant publications

Deliverable: Interactive research tools Time: 10-15 hours per app (substantial effort)
Action 3.4: Optimize for Search & Metrics ⭐

Why: Discoverability matters. You have Google Analytics but not optimized.

Tasks:

    Add structured data markup:
        Schema.org Person
        Schema.org Organization
        Scholarly articles metadata

    Optimize meta descriptions for key pages

    Add alt text to all images

    Create XML sitemap (Jekyll plugin already enabled)

    Submit to Google Scholar profile

Deliverable: Better SEO and discoverability Time: 3-4 hours
PHASE 4: Maintenance & Growth (Ongoing)
Action 4.1: Quarterly Content Audit ⭐⭐

Schedule: First week of each quarter

Checklist:

    Update team member photos/info
    Add recent publications to highlights
    Update funding page with new grants
    Archive old news items
    Check all external links
    Review software version badges
    Update metrics (citations, h-index)

Time: 2-3 hours/quarter
Action 4.2: Annual Strategic Review ⭐⭐

Schedule: Start of academic year

Questions:

    Are research themes still accurate?
    Is the homepage narrative current?
    Are there new software tools to feature?
    Should we reorganize content structure?
    What are competitors doing differently?
    Have we added new service roles?

Time: 4-6 hours/year
Implementation Timeline
Immediate (This Week)

    Fix typography system (Action 1.1)
    Get placeholder photos replaced (Action 1.3)

Short-term (Weeks 1-4)

    Create software page (Action 1.2)
    Add alumni section (Action 1.3)
    Create research themes visualization (Action 2.1)
    Build funding page (Action 2.2)

Medium-term (Weeks 5-8)

    Enhance publications page (Action 2.3)
    Populate teaching page (Action 3.1)
    Enable automation workflows (Action 3.2)
    Optimize for SEO (Action 3.4)

Ongoing

    Quarterly blog posts (Action 2.4)
    Quarterly content audits (Action 4.1)
    Annual strategic reviews (Action 4.2)

Priority Matrix

| Action | Impact | Effort | Priority | Do When | |--------|--------|--------|----------|---------| | Fix typography (1.1) | High | Low | P0 | Week 1 | | Software page (1.2) | Very High | Low | P0 | Week 1 | | Replace placeholder photos (1.3) | High | Low | P0 | Week 1 | | Research themes viz (2.1) | High | Medium | P1 | Week 2 | | Funding page (2.2) | High | Low | P1 | Week 2 | | Alumni section (1.3b) | Medium | Low | P2 | Week 3 | | Publications enhancement (2.3) | Medium | Low | P2 | Week 3 | | Teaching page (3.1) | Medium | Medium | P2 | Week 4 | | Enable automation (3.2) | Medium | Medium | P2 | Week 5 | | SEO optimization (3.4) | Medium | Medium | P3 | Week 6 | | Blog posts (2.4) | Low | Low | P3 | Quarterly | | Interactive apps (3.3) | High | Very High | P4 | Long-term |
Expected Outcomes

After Phase 1 (4 weeks):

    Professional, polished appearance
    Software properly showcased (major boost for adoption/citations)
    Complete team presentation
    Clear research identity

After Phase 2 (8 weeks):

    Demonstrates funding track record
    Enhanced publication impact
    Regular content updates

After Phase 3 (3 months):

    Teaching portfolio complete
    Automated maintenance
    Improved discoverability
    Modern, interactive elements

Measurable Success:

    Software downloads/citations: Track CRAN downloads, GitHub stars
    Web traffic: Google Analytics - aim for 20%+ increase
    Collaboration inquiries: Monitor contact form submissions
    Student applications: Track PhD/postdoc inquiries
    Grant success: Reference site in biosketches
    Professional invitations: Speaking requests, editorial boards

Resources Needed

Personnel:

    Web manager (you or delegate): 4-6 hours/week for 2 months, then 2 hours/month
    Team members: Provide updated photos, bios (1 hour each)
    Students: Can help with blog posts, testing

Tools:

    GitHub Pages (free)
    Image editing software (free: GIMP, Photoshop)
    Diagram creation (free: draw.io, Canva)
    Badge generators (free: shields.io)

Budget:

    $0 (all free tools)
    Optional: Professional photographer for team photos ($500-1000)
    Optional: Web designer for research diagram ($500-1500)

My Professional Assessment

As a senior colleague who has served on dozens of promotion and hiring committees, reviewed hundreds of grants, and maintained my own site for 15 years:
Your current site is: 6.5/10

    Strengths: Clean design, good foundation, recent content push
    Weaknesses: Missing software showcase, incomplete team, typography issues

With these changes: 9/10

    Would rank in top 20% of biostatistics faculty sites
    Strong software presence (critical for methods researchers)
    Clear research narrative
    Complete professional portfolio
    Demonstrates active, productive lab

Bottom Line

You have a solid foundation but critical gaps that are hurting you right now:

    No prominent software = reduced citations (your primary research output!)
    Placeholder photos = looks unfinished (bad first impression)
    Typography issues = unprofessional (easy fix, high impact)

The good news: Most issues are low-effort, high-impact fixes. You can achieve major improvements in 2-4 weeks.

Start with Week 1 priorities:

    Fix typography (4-6 hours)
    Create software page (3-4 hours)
    Replace placeholder photos (2 hours + photo collection)

These three actions alone will transform your site from "good" to "excellent."

Success looks like: A colleague mentions finding your glmmPen package and using it in their NIH grant. A postdoc candidate references your ADAPT work from the funding page. A student emails about PhD opportunities after exploring your research themes. That's when you know your website is working.

Let me know which phase you'd like to tackle first, and I can provide more detailed technical guidance.

thank you. Please place this detailed phased plan into a .md file and commit it and push to this current branch.

I'll create a comprehensive markdown file with the phased plan and commit it to the current branch.
