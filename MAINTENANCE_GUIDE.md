# Website Maintenance Guide - Complete Overview

**Purpose**: Central reference for all website maintenance activities
**Status**: Phase 4 - Ongoing Maintenance & Growth
**Last Updated**: November 2025

---

## Quick Reference: Maintenance Schedule

| Frequency | Task | Time | Document |
|-----------|------|------|----------|
| **Weekly** | Review automated PRs | 10-15 min | `AUTOMATION_GUIDE.md` |
| **Monthly** | Check analytics & SEO | 15-20 min | `SEO_GUIDE.md` |
| **Quarterly** | Content audit | 2-3 hours | `QUARTERLY_AUDIT.md` |
| **As needed** | Blog posts | 1-2 hours | `BLOG_POSTING_GUIDE.md` |
| **Annual** | Strategic review | 4-6 hours | `ANNUAL_REVIEW.md` |

**Total Annual Time Commitment**: ~30-40 hours/year (average <1 hour/week)

---

## Overview: Maintenance Philosophy

Your website is now **highly automated** and requires minimal ongoing effort compared to manual maintenance:

**Before automation**: ~2-3 hours/week (100-150 hours/year)
**After automation**: ~30-40 hours/year (75% reduction)

**Key principles**:
1. **Automation first**: Let GitHub Actions handle routine updates
2. **Quarterly audits**: Systematic reviews prevent content decay
3. **Strategic annual planning**: Align website with career goals
4. **Quality over quantity**: Focus on high-impact updates

---

## WEEKLY MAINTENANCE (10-15 min)

### Monday Morning Routine

**Task**: Review automated pull requests from GitHub Actions workflows

**Schedule**: Every Monday morning (workflows run at 08:00 and 08:30 UTC)

**Steps**:

1. **Check GitHub notifications**
   - Go to https://github.com/[your-username]/[repo-name]/pulls
   - Look for automated PRs (labeled "automated")

2. **Review publication sync PR** (from 08:00 UTC run)
   - Check new publications added to `_bibliography/papers.bib`
   - Verify titles, authors, years are correct
   - Optionally add `keywords` field for thematic filtering
   - **Merge** if looks good, **Close** if prefer manual management

3. **Review social feed PR** (from 08:30 UTC run)
   - Check new posts in `_data/social_staging.yml`
   - Copy interesting posts to `_data/social_curated.yml`
   - **Merge** to update staging feed

4. **Monitor for errors**
   - If PR not created: Check Actions tab for workflow failures
   - Common issues: Rate limiting (wait 24 hrs), no changes detected (expected)

**Reference**: See `AUTOMATION_GUIDE.md` for detailed workflow documentation

**When to skip**: No PRs means no new publications or posts (expected some weeks)

---

## MONTHLY MAINTENANCE (15-20 min)

### First Monday of Each Month

**Task**: Analytics and SEO check

**Steps**:

1. **Google Analytics Review** (10 min)
   - Go to https://analytics.google.com
   - Check last month's traffic:
     - Total visitors: _____
     - Top pages: _____
     - Traffic sources: _____
   - Note any unusual spikes or drops
   - Identify which content is performing well

2. **Google Search Console** (5 min, if set up)
   - Go to https://search.google.com/search-console
   - Check search performance:
     - Top queries: _____
     - Average position: _____
     - CTR: _____%
   - Fix any coverage errors
   - Monitor mobile usability

3. **Quick link check** (5 min)
   - Review GitHub Actions "Broken Links" workflow results
   - Fix any reported broken links
   - Test 2-3 random external links manually

**Reference**: See `SEO_GUIDE.md` for detailed SEO monitoring instructions

**Actions based on data**:
- High traffic to software page → Highlight new packages
- Low engagement on teaching page → Add more resources
- Search ranking drop → Review meta descriptions, add content

---

## QUARTERLY MAINTENANCE (2-3 hours)

### First Week of Each Quarter (Jan, Apr, Jul, Oct)

**Task**: Comprehensive content audit and updates

**Use checklist**: `QUARTERLY_AUDIT.md` (complete document)

**Summary of tasks**:

1. **Team updates** (30 min)
   - Update student/postdoc information
   - Move graduates to alumni section
   - Verify all photos are professional quality

2. **Publications** (30-45 min)
   - Add new publications since last quarter
   - Update metrics (h-index, citations)
   - Rotate featured publications

3. **Funding & grants** (20-30 min)
   - Add new grants awarded
   - Update funding summary metrics
   - Move completed grants to archive

4. **Software** (15-20 min)
   - Check for package version updates
   - Add new software releases
   - Verify all links work

5. **Research themes** (15 min)
   - Update active projects
   - Add new collaborations
   - Highlight recent achievements

6. **Blog post** (20-30 min)
   - Write quarterly lab update (see `BLOG_POSTING_GUIDE.md`)
   - Cross-post to Twitter/LinkedIn
   - Update homepage news items

7. **Link checking** (15-20 min)
   - Test all external links
   - Check internal navigation
   - Review GitHub Actions workflow results

8. **Analytics review** (15-20 min)
   - Review quarterly trends
   - Identify top-performing content
   - Adjust strategy based on data

9. **Technical maintenance** (10-15 min)
   - Check GitHub Actions health
   - Test local build (optional)
   - Update dependencies if needed

10. **Final review & commit** (10 min)
    - Proofread all changes
    - Test mobile responsiveness
    - Git commit and push

**Reference**: See `QUARTERLY_AUDIT.md` for complete detailed checklist

**Efficiency tips**:
- Block out 2-3 hours of uninterrupted time
- Use quarterly audit template (copy from `QUARTERLY_AUDIT.md`)
- Set calendar reminder for first Monday of Jan, Apr, Jul, Oct
- Track time to optimize future audits

---

## AS-NEEDED MAINTENANCE

### Blog Posts for Major Announcements

**When to post**:
- Major grant awarded ($500K+)
- Significant publication (high-impact journal, major methodology)
- Student graduation or major award
- Conference organization or keynote talk
- Software release with significant new features

**Time**: 1-2 hours per post

**Process**:
1. Use helper script: `./bin/new-update.sh "Title"`
2. Write 300-800 word post (see `BLOG_POSTING_GUIDE.md`)
3. Include links to related pages (publications, software, funding)
4. Add excerpt separator for homepage preview
5. Commit and push
6. Cross-post to Twitter/LinkedIn

**Reference**: See `BLOG_POSTING_GUIDE.md` for complete posting guide

---

## ANNUAL MAINTENANCE (4-6 hours)

### Start of Academic Year (August/September)

**Task**: Strategic review and planning

**Use template**: `ANNUAL_REVIEW.md` (complete document)

**Summary of tasks**:

1. **Goals assessment** (60-90 min)
   - Review effectiveness in recruitment, visibility, collaboration
   - Track metrics year-over-year (traffic, citations, downloads)
   - Assess alignment with career goals

2. **Content audit** (90-120 min)
   - Review all major pages (research, software, funding, teaching)
   - Ask strategic questions:
     - Are research themes still accurate?
     - Is homepage narrative current?
     - New software tools to feature?
     - Should we reorganize content?

3. **Competitive analysis** (45-60 min)
   - Review 5-10 peer lab websites
   - Identify best practices to adopt
   - Assess differentiation and positioning

4. **Technical & design review** (30-45 min)
   - Evaluate navigation and structure
   - Assess visual design and branding
   - Test mobile and accessibility

5. **Analytics & SEO** (30-45 min)
   - Annual traffic summary
   - SEO performance review
   - Citation and backlink analysis

6. **New initiatives** (60-90 min)
   - Set priorities for coming year
   - Decide on interactive elements (Shiny apps, videos)
   - Budget and resource planning

7. **Action plan** (30 min)
   - Prioritize major updates for next year
   - Set success metrics
   - Schedule projects by quarter

**Reference**: See `ANNUAL_REVIEW.md` for complete strategic review template

**Outcome**: Action plan for coming year with quarterly priorities

---

## Maintenance by Role/Responsibility

### If You Do All Maintenance Yourself

**Recommended approach**:
- **Weekly** (10-15 min): Review automated PRs - do yourself
- **Monthly** (15-20 min): Analytics check - do yourself
- **Quarterly** (2-3 hours): Content audit - do yourself or with student help
- **Quarterly** (1-2 hours): Blog posts - do yourself
- **Annual** (4-6 hours): Strategic review - do yourself

**Total**: ~30-40 hours/year

### If You Delegate to Students

**Recommended delegation**:

**Student can do**:
- Review automated PRs (with your approval)
- Monthly link checking
- Draft quarterly blog posts (you edit and approve)
- Update team page (student info, photos)
- Update publications (add to BibTeX)
- Update software versions

**You should do**:
- Final approval of all PRs and posts
- Strategic content decisions (featured pubs, funding disclosure)
- Quarterly audit review (student drafts, you approve)
- Annual strategic review

**Training time**: 2-3 hours initially to train student
**Ongoing**: Review student work 15-30 min/week

**Benefits**:
- Reduces your time to ~20-30 hours/year
- Trains student in web development and science communication
- Ensures website stays current without your constant attention

### If You Hire Professional Help

**What to outsource**:
- **Designer**: Visual refresh, custom graphics ($1000-3000)
- **Developer**: Interactive elements, Shiny apps ($2000-5000)
- **Photographer**: Professional team photos ($500-1000)
- **Writer**: Blog post drafting, content editing ($1000-3000)

**What to keep in-house**:
- Strategic decisions (research themes, messaging)
- Content updates (publications, grants, team)
- Final approval of all changes

---

## Documentation Reference Guide

Your website now has comprehensive documentation for all maintenance activities:

### Core Guides

1. **`MAINTENANCE_GUIDE.md`** (this file)
   - Overview of all maintenance activities
   - Quick reference for schedules and responsibilities
   - Delegation and outsourcing guidance

2. **`AUTOMATION_GUIDE.md`**
   - GitHub Actions workflows documentation
   - Weekly PR review process
   - Troubleshooting automation issues
   - Advanced customization options

3. **`QUARTERLY_AUDIT.md`**
   - Complete quarterly audit checklist
   - Section-by-section update instructions
   - File tracking (which files to update)
   - Efficiency tips and time tracking

4. **`ANNUAL_REVIEW.md`**
   - Strategic review template
   - Competitive analysis framework
   - Goal-setting and success metrics
   - Action planning for coming year

5. **`BLOG_POSTING_GUIDE.md`**
   - Blog posting schedule and workflow
   - Content templates for different post types
   - Cross-posting to social media
   - Review checklist

6. **`SEO_GUIDE.md`**
   - SEO optimizations completed
   - Ongoing SEO maintenance (monthly, quarterly)
   - Google Search Console setup
   - Keywords strategy and monitoring

### Phase Summary Documents

7. **`PHASE_1_SUMMARY.md`** (if created)
   - Typography, software, team profiles deliverables

8. **`PHASE_2_SUMMARY.md`**
   - Research themes, funding, publications, blog deliverables
   - User review checklist

9. **`PHASE_3_SUMMARY.md`**
   - Teaching, automation, SEO deliverables
   - Impact assessment (6.5/10 → 9.0/10)

### Reference Documents

10. **`ACTION_ITEMS.md`**
    - Running list of user decisions needed
    - Phase completion status
    - Priority summary (high/medium/low)

11. **`plan.md`**
    - Original strategic plan from senior faculty reviewer
    - Reference for goals and recommendations

12. **`PLACEHOLDER_PHOTOS_NEEDED.md`** (Phase 1)
    - Team members needing professional photos
    - Photo guidelines and specifications

---

## Common Scenarios & Solutions

### Scenario 1: Too Busy to Maintain

**Problem**: Don't have 2-3 hours for quarterly audit

**Solution**:
- Skip quarterly audit 1-2 times (rely on automation)
- Do mini-audit (30 min): Just update team, add recent pubs, write short blog post
- Catch up during annual review (plan for extra time)

**Risk**: Content becomes stale, but automation keeps core up-to-date

### Scenario 2: Automation Not Working

**Problem**: No PRs appearing on Mondays

**Solutions**:
1. Check GitHub Actions tab for workflow run status
2. Look for error messages (rate limiting, permissions)
3. Manually trigger workflow: Actions → [Workflow Name] → Run workflow
4. Consult `AUTOMATION_GUIDE.md` troubleshooting section
5. If persistent: Disable workflows, return to manual updates

### Scenario 3: Website Redesign Needed

**Problem**: Visual design feels outdated or doesn't reflect brand

**Solution**:
- Include in annual review as major priority
- Budget for professional designer ($1000-3000)
- Or: Use student designer ($200-500)
- Timeline: 2-3 months (design → implementation → testing)
- Defer other major updates during redesign

### Scenario 4: Major Career Change

**Problem**: New position, research direction, or institution

**Solution**:
- Schedule out-of-cycle strategic review (use `ANNUAL_REVIEW.md`)
- Update homepage narrative immediately
- Revise research themes as needed
- Consider full rebrand if institution changed
- Timeline: 1-2 weeks for major overhaul

### Scenario 5: No Time for Annual Review

**Problem**: 4-6 hours seems like too much

**Solution**:
- Do mini-review (2 hours): Focus on Parts 1, 2, 6 only
  - Goals assessment (60 min)
  - Content audit - research themes only (30 min)
  - Action plan for next year (30 min)
- Skip competitive analysis, detailed design review
- Catch up every 2-3 years with full review

---

## Success Metrics: How to Know It's Working

### Website Health Indicators

**Green flags** (website is healthy):
- ✅ Automated PRs merging successfully each week
- ✅ Website traffic stable or growing year-over-year
- ✅ Receiving inquiries from prospective students referencing website
- ✅ Collaborators mentioning finding you via website
- ✅ No broken links in quarterly audits
- ✅ Blog posts published at least quarterly
- ✅ Content is current (publications/grants from last 12 months)

**Yellow flags** (needs attention):
- ⚠️ Traffic declining >20% year-over-year (check SEO, add content)
- ⚠️ Automation workflows failing frequently (troubleshoot, may need to disable)
- ⚠️ Missing 2+ quarterly audits (content getting stale)
- ⚠️ Team photos >3 years old (update with fresh photos)
- ⚠️ No blog posts in 6+ months (write update, shows activity)

**Red flags** (urgent action needed):
- 🚨 Major grants/papers not listed (add immediately - represents your work)
- 🚨 Graduated students still listed as current (update team page)
- 🚨 Broken links to publications/software (damages credibility)
- 🚨 Website down or build failing (fix GitHub Pages deployment)
- 🚨 Receiving zero inquiries from website (reassess strategy in annual review)

### ROI Assessment

**Is website worth the time?**

Track these annually to assess return on investment:

**Positive indicators**:
- Recruited desired PhD students who found you via website
- Collaboration invitations mentioning website
- Software downloads increasing (website drives traffic to packages)
- Media inquiries referencing website
- Invited talks mentioning finding you online

**If ROI is low**:
- Reduce maintenance frequency (skip quarterly audits, just do annual)
- Rely more heavily on automation
- Simplify content (fewer pages, less detail)
- Consider whether website is necessary (some fields don't need one)

---

## Optimization Tips

### Time-Saving Strategies

1. **Batch similar tasks**
   - Update all team info at once (not piecemeal)
   - Add multiple publications in one sitting
   - Review all links together (not page-by-page)

2. **Use automation fully**
   - Let GitHub Actions handle publications sync
   - Don't manually check for new papers (let workflow do it)
   - Trust automation (only intervene if errors)

3. **Templates and checklists**
   - Copy quarterly audit checklist each time (don't start from scratch)
   - Use blog post templates (speeds writing)
   - Standard commit message format

4. **Delegate appropriately**
   - Students can draft blog posts, update team page
   - You approve final content
   - Saves 50-75% of your time

5. **Prioritize impact**
   - Focus on high-traffic pages (homepage, software, publications)
   - Deprioritize rarely-visited pages
   - Update what matters most to your goals

### Quality-Saving Strategies

1. **Consistent voice**
   - Establish tone guidelines (professional but approachable)
   - Use same writing style across pages
   - Review all content for consistency in annual review

2. **Proofread before commit**
   - Always preview changes locally if possible
   - Check for typos, broken formatting
   - Test links before pushing

3. **Mobile testing**
   - Check new content on phone before publishing
   - Verify images scale correctly
   - Test navigation on small screens

4. **Peer review**
   - Ask colleague or student to review major changes
   - Get feedback on homepage narrative
   - External perspective valuable for clarity

---

## Phase 4 Ongoing Maintenance Checklist

Use this as your master checklist going forward:

### ✅ Setup Complete (One-Time)

- [x] Phases 1-3 implemented
- [x] Automation workflows configured
- [x] SEO optimized (Schema.org, meta descriptions)
- [x] Documentation created (all guides)
- [ ] Google Search Console set up (recommended)
- [ ] Professional team photos obtained (if needed)

### 🔄 Weekly (10-15 min)

- [ ] Review automated PRs (publications, social feed)
- [ ] Merge or close PRs
- [ ] Monitor for workflow errors

### 📅 Monthly (15-20 min)

- [ ] Check Google Analytics (traffic, top pages)
- [ ] Review Google Search Console (search performance)
- [ ] Quick link check (automated + manual spot check)

### 📊 Quarterly (2-3 hours)

- [ ] Complete `QUARTERLY_AUDIT.md` checklist
- [ ] Write quarterly blog post
- [ ] Update team, publications, funding, software
- [ ] Review analytics trends
- [ ] Git commit all changes

### 📝 As Needed (1-2 hours)

- [ ] Blog posts for major announcements
- [ ] Add new team members
- [ ] Update homepage for major news

### 🎯 Annual (4-6 hours)

- [ ] Complete `ANNUAL_REVIEW.md` strategic review
- [ ] Set priorities for coming year
- [ ] Competitive analysis
- [ ] Plan major updates (interactive elements, redesign)

---

## Getting Help

### When You Need Assistance

**Technical Issues**:
- GitHub Actions not working → Consult `AUTOMATION_GUIDE.md`
- Jekyll build errors → Check logs in GitHub Actions, search Jekyll docs
- Git issues → Basic Git tutorials online

**Content Issues**:
- What to highlight → Use `ANNUAL_REVIEW.md` to guide decisions
- SEO underperforming → Review `SEO_GUIDE.md` recommendations
- Low engagement → Analyze Google Analytics, adjust content

**Strategic Issues**:
- Career alignment → Revisit goals in `ANNUAL_REVIEW.md`
- Competitive positioning → Do peer website review
- ROI concerns → Track metrics, assess if website serving goals

### Resources

**Documentation (This Repo)**:
- All guides in root directory (`.md` files)
- Reference `ACTION_ITEMS.md` for current status

**External Resources**:
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [al-folio Theme Docs](https://github.com/alshedivat/al-folio)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Google Analytics Help](https://support.google.com/analytics)

**UNC Resources**:
- UNC Communications (for photo services, news coverage)
- Gillings IT Support (for technical issues)
- Lineberger Communications (for major announcements)

---

## Conclusion: Sustainable Maintenance

Your website is now **optimized for sustainability**:

**Low maintenance burden**: ~30-40 hours/year (75% reduction)
**High automation**: Weekly tasks mostly automated
**Clear processes**: Documented checklists for all maintenance
**Strategic alignment**: Annual review ensures website supports career goals

**The key to success**: Stick to the schedule. Set calendar reminders and block time for quarterly audits and annual reviews. Consistency prevents content decay and keeps your website professional and current.

---

**Questions?** Review relevant guide or contact Dr. Rashid ([naim@unc.edu](mailto:naim@unc.edu))

**Last Updated**: November 2025
**Next Quarterly Audit**: January 2026
**Next Annual Review**: August/September 2026
