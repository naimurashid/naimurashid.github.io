# Lab Updates Blog Posting Guide

## Overview

The Rashid Lab maintains a **quarterly blog** to share research updates, grant awards, publications, team achievements, and upcoming events. This keeps the website active, improves SEO, and engages prospective students, collaborators, and the broader community.

---

## Posting Schedule

### Recommended Frequency
- **Quarterly lab updates**: First week of each quarter (Jan, Apr, Jul, Oct)
- **Major announcements**: As they occur (grants, awards, publications)
- **Event summaries**: After conferences, workshops, or talks

### Quarterly Update Checklist
Use this as a template for each quarterly post:

- [ ] New publications (methodology + collaborative)
- [ ] Grant awards or renewals
- [ ] Student/postdoc achievements (defenses, awards, presentations)
- [ ] Software releases or updates
- [ ] Upcoming conferences and talks
- [ ] Collaborative highlights
- [ ] Recruitment announcements

---

## Creating a New Post

### Option 1: Use the Helper Script

```bash
# Create a new post with today's date
./bin/new-update.sh "Title of Your Post"

# Create a post with a specific date
./bin/new-update.sh "Lab Updates Q1 2026" 2026-01-05
```

This creates a file in `_posts/` with the correct naming convention and front matter.

### Option 2: Manual Creation

1. Create a file in `_posts/` with format: `YYYY-MM-DD-title-slug.md`
2. Add front matter (see template below)
3. Write your content in Markdown
4. Commit and push to deploy

---

## Post Template

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
description: Brief one-line description (appears in previews)
tags: lab-updates grants publications team
categories: updates
giscus_comments: false
---

## Summary

Brief summary paragraph (this will appear in the homepage feed and previews).

<!-- excerpt-separator -->

## Section 1

Full content starts here after the excerpt separator.

### Subsection

More details...

---

*Posted by Naim Rashid on [Date]*
```

### Front Matter Fields

- **layout**: Always use `post`
- **title**: Post title (will appear as page heading)
- **date**: Post date in YYYY-MM-DD format
- **description**: One-line summary for meta tags and previews
- **tags**: Space-separated keywords (e.g., `lab-updates grants publications`)
- **categories**: Primary category (usually `updates`)
- **giscus_comments**: Set to `false` to disable comments, `true` to enable

### Excerpt Separator

Use `<!-- excerpt-separator -->` to mark where the preview ends and full content begins. Everything before this will show in the homepage news feed.

---

## Content Guidelines

### Structure

1. **Summary** (1-2 paragraphs)
   - Hook the reader with key highlights
   - This appears in homepage feed and previews

2. **Main Sections**
   - Use `##` for major sections
   - Use `###` for subsections
   - Keep sections focused and scannable

3. **Links and References**
   - Link to relevant pages (publications, funding, team profiles)
   - Link to external news coverage when available
   - Use Markdown link syntax: `[text](url)`

4. **Images** (optional)
   - Place images in `assets/img/posts/`
   - Reference with: `![Alt text](/assets/img/posts/filename.jpg)`
   - Keep file sizes reasonable (<500KB)

### Tone

- Professional but approachable
- Celebrate achievements without excessive hype
- Acknowledge collaborators and team contributions
- Use active voice: "We published..." not "A paper was published..."

### Length

- **Quarterly updates**: 800-1200 words
- **Quick updates**: 300-500 words
- **Major announcements**: 400-600 words

---

## Content Ideas

### Regular Features

**New Publications**
```markdown
### Recent Publications

**Author et al. (2025)** published "Title" in *Journal* XX(X):pages.
This work [brief 1-2 sentence summary of impact].

[Read the paper →](DOI link)
```

**Grant Awards**
```markdown
### Major Grant Awarded

We are thrilled to announce our new **[Agency] [Program]** award ($XXX,XXX)
for "[Project Title]". This [duration]-year project will [goals].

Key aims:
- Aim 1
- Aim 2
- Aim 3

[Read more →](news link if available)
```

**Team Achievements**
```markdown
### Student Achievements

**[Student Name]** presented their work on [topic] at [conference],
winning [award] in the [category] section. Congratulations!

**[Student Name]** successfully defended their dissertation on [topic]
and will join [institution] as a [position].
```

**Software Releases**
```markdown
### Software Update: [Package Name] v[X.Y.Z]

[Lead Developer] released an updated version of **[package]** featuring:
- New feature 1
- Performance improvement 2
- Bug fix 3

[CRAN/GitHub link]
```

---

## Cross-Posting

After publishing a blog post, consider cross-posting summaries to:

### Twitter/X
- Share a 2-3 tweet thread summarizing key points
- Include link to full post
- Tag collaborators and institutions
- Example: "Excited to share our Q4 lab updates! 🧬📊 New @ARPAH ADAPT trial ($28M), DOD award, and recent pubs. Thanks to amazing team @UNC_Lineberger [link]"

### LinkedIn
- Post a longer summary (300-500 words)
- Include 1-2 images
- Tag co-authors and institutions
- Link to full blog post

### Department/School Channels
- Share major announcements with:
  - UNC Biostatistics communications team
  - Gillings School news office
  - Lineberger communications

---

## Review Process

### Before Publishing

- [ ] Proofread for typos and grammar
- [ ] Verify all links work
- [ ] Check that excerpt separator is placed correctly
- [ ] Ensure front matter is complete
- [ ] Preview locally if possible: `bundle exec jekyll serve`

### After Publishing

- [ ] Verify post appears correctly on website
- [ ] Share on social media
- [ ] Notify team members mentioned in the post
- [ ] Update homepage news if not automatically displayed

---

## Examples

See the example post in `_posts/2025-11-04-lab-updates-q4-2025.md` for a comprehensive quarterly update template.

### Good Examples from Peer Labs

Browse these biostatistics/genomics lab blogs for inspiration:
- BayesRx Lab (Jen Bryan)
- Love Lab (Mike Love)
- Ritchie Lab (Marylyn Ritchie)
- Noble Lab (William Noble)

---

## Maintenance

### Quarterly Audit (Same as Site Maintenance)

- Review recent posts for broken links
- Archive very old posts if needed
- Update recurring content (e.g., recruitment announcements)
- Ensure post categories and tags are consistent

---

## Questions?

Contact Dr. Rashid ([naim@unc.edu](mailto:naim@unc.edu)) or consult the Jekyll documentation:
- [Jekyll Posts Guide](https://jekyllrb.com/docs/posts/)
- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/)

---

**Last Updated**: November 2025
