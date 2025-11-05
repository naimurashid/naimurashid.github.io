# SEO Optimization Guide

## Overview

This guide documents SEO (Search Engine Optimization) enhancements implemented for the Rashid Lab website and provides maintenance recommendations.

---

## Completed SEO Optimizations

### 1. Structured Data (Schema.org) ✅

**What**: Machine-readable metadata about your website for search engines

**Implementation**: Enabled in `_config.yml` (line 67):
```yaml
serve_schema_org: true # Include Schema.org in the HTML head (ENABLED for SEO)
```

**Benefits**:
- Improved search result snippets (rich snippets)
- Better understanding by Google Scholar, Google Search
- Enhanced appearance in search results with structured information

**What's Included** (al-folio theme provides):
- Person schema with name, affiliation, contact info
- Organization schema for UNC affiliation
- WebPage schema for each page
- ScholarlyArticle schema for publications (via Jekyll-Scholar)

**Verification**:
1. Visit [Google Rich Results Test](https://search.google.com/test/rich-results)
2. Enter your website URL: `https://naimurashid.github.io`
3. Verify structured data is detected correctly

---

### 2. Meta Descriptions ✅

**What**: Short summaries that appear in search results under page titles

**Implementation**: Added optimized descriptions to key pages:

**Site-wide** (`_config.yml`, line 11):
```yaml
description: >
  Rashid Lab at UNC Chapel Hill develops statistical methods for precision oncology,
  adaptive clinical trials, and cancer genomics. We specialize in Bayesian adaptive
  trial design, penalized regression for high-dimensional data, and machine learning
  for biomarker discovery.
```

**Page-specific**:
- **Publications** (line 5): "75+ peer-reviewed publications in biostatistics, clinical trials, and cancer genomics. h-index 28, 5000+ citations in precision oncology and adaptive trial design."
- **Funding** (line 5): "$60M+ research funding for adaptive clinical trials, cancer genomics, and precision oncology from ARPA-H, NCI, DOD, and other federal agencies"
- **Software** (line 4): "Open-source software packages and tools for statistical genomics and cancer research"
- **Research** (line 4): "Statistical methods development for precision oncology and cancer genomics"
- **Teaching** (line 5): "Courses, workshops, and mentoring in biostatistics and statistical computing"

**Best Practices**:
- 150-160 characters optimal length
- Include primary keywords (biostatistics, clinical trials, cancer genomics)
- Be specific and descriptive
- Avoid generic phrases

**Verification**:
1. View page source (Right-click → View Page Source)
2. Look for `<meta name="description" content="...">` in `<head>`
3. Preview in [Google SERP Simulator](https://www.highervisibility.com/seo/tools/serp-snippet-optimizer/)

---

### 3. Open Graph Meta Tags ✅

**What**: Enhanced social media previews (Twitter, LinkedIn, Facebook)

**Implementation**: Already enabled in `_config.yml` (line 66):
```yaml
serve_og_meta: true # Include Open Graph meta tags in the HTML head
og_image: /assets/img/RashidLabMainLogo2400x1800.jpeg
```

**What This Provides**:
- `og:title`: Page title
- `og:description`: Page description
- `og:image`: Preview image (logo)
- `og:url`: Canonical URL
- `og:type`: website/article

**Benefits**:
- Professional link previews on Twitter/LinkedIn
- Increased click-through rates from social media
- Consistent branding across platforms

**Verification**:
1. [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
2. [Twitter Card Validator](https://cards-dev.twitter.com/validator)
3. [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)

---

### 4. Keywords & Analytics ✅

**Implementation**: Configured in `_config.yml`:

**Keywords** (line 15):
```yaml
keywords: Biostatistics, Cancer, AI, Machine Learning, Clinical Trials
```

**Google Analytics** (line 122):
```yaml
google_analytics: G-8PZVKQGFGK
```

**Google Scholar** (line 97):
```yaml
scholar_userid: 3Cz_lcEAAAAJ
```

**Benefits**:
- Traffic monitoring and insights
- Understanding user behavior
- Academic citation tracking

**Next Steps**:
- [ ] Set up Google Search Console verification (line 127)
- [ ] Add `google_site_verification` code
- [ ] Submit XML sitemap

---

### 5. XML Sitemap ✅

**What**: Machine-readable list of all pages for search engine crawling

**Implementation**: Jekyll automatically generates sitemap at:
- `https://naimurashid.github.io/sitemap.xml`

**Verification**:
1. Visit `https://naimurashid.github.io/sitemap.xml` (should show XML file)
2. Check it includes all major pages:
   - About/Home
   - Publications
   - Research
   - Software
   - Funding
   - Teaching
   - Team
   - Blog posts

**Submission**:
- [ ] [Google Search Console](https://search.google.com/search-console): Submit sitemap URL
- [ ] [Bing Webmaster Tools](https://www.bing.com/webmasters): Submit sitemap URL

---

## Image Alt Text Checklist

**What**: Descriptive text for images, critical for accessibility and SEO

**Why Important**:
- Screen readers for visually impaired users
- SEO benefit (images indexed with descriptions)
- Fallback when images fail to load
- ADA/WCAG compliance

### Current Status

**Team Photos** (`_pages/team.md` and `_pages/about.md`):
- [ ] Verify all team member photos have alt text
- [ ] Format: `![Photo of Dr. Naim Rashid](path/to/image.jpg)`
- [ ] Alumni photos: Use "Photo of [Name], [Position]"

**Logo & Branding**:
- [ ] Main logo: `![Rashid Lab logo](...)`
- [ ] UNC affiliation logos: `![UNC Lineberger Comprehensive Cancer Center logo](...)`

**Software Badges**:
- ✅ CRAN badges: Auto-generated with alt text via Shields.io
- ✅ GitHub badges: Auto-generated with alt text

**Research Diagrams** (if added):
- [ ] Use descriptive alt text: `![Four research themes diagram showing penalized models, adaptive trials, genomics, and machine learning](...)`

### How to Add Alt Text

**Markdown**:
```markdown
![Descriptive alt text here](/path/to/image.jpg)
```

**HTML**:
```html
<img src="/path/to/image.jpg" alt="Descriptive alt text here">
```

**Best Practices**:
- Be specific and descriptive
- Include context (who, what, where)
- Avoid "image of" or "picture of" (implied)
- For decorative images, use `alt=""`
- For complex diagrams, provide longer description in caption

---

## Ongoing SEO Maintenance

### Monthly Tasks

**Check Google Analytics** (15 min):
- [ ] Review traffic sources
- [ ] Identify top-performing pages
- [ ] Check for broken links (404 errors)
- [ ] Monitor search queries (Search Console)

**Update Meta Descriptions** (as needed):
- [ ] When adding new major pages
- [ ] When research focus shifts
- [ ] When new grants/publications significantly change narrative

### Quarterly Tasks

**Verify Structured Data** (10 min):
- [ ] Run [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Fix any schema errors
- [ ] Update affiliation if changed

**Check Search Rankings** (15 min):
- [ ] Google your name + "biostatistics"
- [ ] Google "adaptive clinical trials UNC"
- [ ] Google "statistical genomics cancer"
- [ ] Monitor ranking changes

**Image Audit** (20 min):
- [ ] Verify all new images have alt text
- [ ] Check image load times (optimize if >500KB)
- [ ] Ensure team photos are current

### Annual Tasks

**Comprehensive SEO Audit** (2-3 hours):
- [ ] Review all page titles and descriptions
- [ ] Update keywords if research focus changed
- [ ] Check backlinks (who links to your site?)
- [ ] Analyze competitor websites
- [ ] Review Google Search Console insights
- [ ] Submit updated sitemap

---

## Technical SEO Best Practices

### Page Titles

**Format**: `[Page Name] | Naim Rashid | UNC Biostatistics`

**Current Implementation** (al-folio handles automatically):
- Home: "Naim Rashid | UNC Biostatistics"
- Publications: "Publications | Naim Rashid | UNC Biostatistics"
- Research: "Research | Naim Rashid | UNC Biostatistics"

**Best Practices**:
- Keep under 60 characters (avoids truncation)
- Put most important keywords first
- Be unique for each page

### URL Structure

**Current**: Clean, semantic URLs ✅
- `/publications/`
- `/research/`
- `/software/`
- `/funding/`
- `/teaching/`
- `/team/`
- `/blog/2025/lab-updates-q4-2025/`

**Why This Is Good**:
- Human-readable
- Descriptive (keywords in URL)
- Consistent structure
- No unnecessary parameters

### Mobile Responsiveness ✅

**Status**: al-folio theme is mobile-responsive by default

**Verification**:
1. [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
2. Test on actual mobile devices
3. Check responsive breakpoints

### Page Load Speed

**Current**: GitHub Pages is reasonably fast

**Optimization Opportunities**:
- [ ] Compress images (use JPEG for photos, PNG for logos)
- [ ] Lazy-load images below the fold
- [ ] Minimize CSS/JS if build time becomes an issue

**Testing**:
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- Target: 80+ score on mobile and desktop

---

## Google Search Console Setup

**Recommended Next Step**: Verify site ownership with Google

### Steps

1. **Visit** [Google Search Console](https://search.google.com/search-console)

2. **Add Property**: `https://naimurashid.github.io`

3. **Verify Ownership** (HTML tag method):
   - Google will provide a meta tag like:
     ```html
     <meta name="google-site-verification" content="XXXXXXXXX" />
     ```
   - Add to `_config.yml`:
     ```yaml
     google_site_verification: XXXXXXXXX
     ```
   - Commit and push changes
   - Click "Verify" in Search Console

4. **Submit Sitemap**:
   - In Search Console, go to Sitemaps
   - Add sitemap URL: `https://naimurashid.github.io/sitemap.xml`
   - Submit

5. **Monitor**:
   - Search performance (clicks, impressions, CTR)
   - Coverage issues (crawl errors)
   - Mobile usability
   - Core Web Vitals

---

## Academic-Specific SEO

### Google Scholar

**Current Configuration** (`_config.yml`):
```yaml
scholar_userid: 3Cz_lcEAAAAJ
```

**Recommendations**:
- ✅ Keep profile updated with recent publications
- [ ] Ensure website URL is listed in profile
- [ ] Link publications to website when possible
- [ ] Use consistent author name across all papers

### ORCID Integration

**Current**: Not configured

**Recommendation** (optional):
```yaml
orcid_id: 0000-0000-0000-0000  # Your ORCID ID
```

**Benefits**:
- Standardized researcher identification
- Auto-linking publications across systems
- Improved academic discoverability

### ResearchGate, Semantic Scholar

**Current**: Not configured

**Recommendation**: Claim profiles and link to website:
- [ResearchGate](https://www.researchgate.net/)
- [Semantic Scholar](https://www.semanticscholar.org/)

---

## Keywords Strategy

### Primary Keywords (High Priority)

Focus on these in titles, descriptions, and content:

**Methodological**:
- Bayesian adaptive trial design
- Penalized regression
- High-dimensional inference
- Statistical genomics
- Machine learning for oncology

**Applied**:
- Precision oncology
- Cancer subtyping
- Biomarker discovery
- Clinical trial design
- Multi-omic integration

**Institutional**:
- UNC biostatistics
- UNC Lineberger
- Chapel Hill cancer research

### Long-Tail Keywords (Medium Priority)

More specific, less competitive:
- "Adaptive platform trials metastatic breast cancer"
- "Penalized generalized linear mixed models R package"
- "Tumor microenvironment deconvolution methods"
- "Missing data imputation machine learning"

### Monitoring Keyword Performance

**Tools**:
- Google Search Console: "Performance" → "Queries"
- Google Analytics: "Acquisition" → "Organic Search"

**Goal**: Rank in top 10 for:
- "Naim Rashid biostatistics" (✅ likely already #1)
- "Adaptive trials UNC" (target)
- "Statistical genomics cancer" (competitive, long-term goal)

---

## Content Strategy for SEO

### Blog Posts as SEO Drivers

**Why**: Fresh, keyword-rich content improves rankings

**Quarterly Lab Updates** (see `BLOG_POSTING_GUIDE.md`):
- Use descriptive titles with keywords
- Example: "Rashid Lab Awarded $28M ARPA-H ADAPT Platform Trial for Bayesian Adaptive Design"
- Include internal links to research/software/publications pages
- Aim for 800-1200 words (good length for indexing)

**Cross-Linking Strategy**:
- Link from blog posts to relevant pages
- Link from research page to software page
- Link from publications to related blog posts

### External Backlinks

**What**: Links to your site from other websites (major ranking factor)

**Current Sources**:
- UNC Biostatistics faculty directory
- UNC Lineberger member profile
- GitHub profile
- Google Scholar profile

**Opportunities to Gain More**:
- [ ] Add website to email signature
- [ ] Include in conference presentation slides
- [ ] Link from R package documentation
- [ ] Collaborate and get cited in others' blogs
- [ ] UNC news articles (request link back)

---

## Success Metrics

### Track Monthly

- **Organic search traffic**: Goal +20% over 6 months
- **Average session duration**: Goal >2 minutes
- **Bounce rate**: Goal <60%
- **Pages per session**: Goal >2

### Track Quarterly

- **Search rankings**: Monitor top 5 keywords
- **Backlinks**: Use [Ahrefs Free Backlink Checker](https://ahrefs.com/backlink-checker)
- **Domain authority**: Use [Moz Free Domain SEO Checker](https://moz.com/domain-analysis)

### Track Annually

- **Publication page views**: Correlate with citation increases
- **Software downloads**: Track CRAN/GitHub downloads, check for spikes after web updates
- **Contact form inquiries**: Track student/collaborator interest

---

## Common SEO Pitfalls to Avoid

❌ **Don't**:
- Keyword stuff (repeating keywords unnaturally)
- Use duplicate meta descriptions across pages
- Neglect mobile optimization
- Ignore page load speed
- Forget to update content regularly

✅ **Do**:
- Write naturally for humans first, search engines second
- Keep content fresh (quarterly blog posts help)
- Use descriptive, unique titles and descriptions
- Build quality backlinks (not quantity)
- Monitor and adapt based on analytics

---

## Resources

### SEO Tools (Free)

- [Google Search Console](https://search.google.com/search-console)
- [Google Analytics](https://analytics.google.com/)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Ahrefs Free SEO Tools](https://ahrefs.com/free-seo-tools)
- [Moz Free SEO Tools](https://moz.com/free-seo-tools)

### SEO Guides for Academics

- [Google Scholar Best Practices](https://scholar.google.com/intl/en/scholar/inclusion.html)
- [Schema.org for Scholarly Articles](https://schema.org/ScholarlyArticle)
- [Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Last Updated**: November 2025

**Next Review**: February 2026 (quarterly check)

**Questions?** Contact Dr. Rashid ([naim@unc.edu](mailto:naim@unc.edu))
