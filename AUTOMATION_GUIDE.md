# Website Automation Guide

## Overview

Your website includes **GitHub Actions workflows** that automatically update content on a weekly schedule, reducing manual maintenance burden. This guide explains what's automated, how it works, and what you need to do.

---

## Automated Workflows

### 1. Publication Sync (`sync-publications.yml`)

**Purpose**: Automatically fetch publications from your Google Scholar profile and update the BibTeX bibliography.

**Schedule**: Every Monday at 08:00 UTC (3:00 AM EST / 4:00 AM EDT)

**What It Does**:
1. Fetches publication data from Google Scholar (ID: `3Cz_lcEAAAAJ`)
2. Updates `_bibliography/papers.bib` with new publications
3. Creates a pull request for your review
4. Labels the PR as "automated"

**Configuration**:
- **Google Scholar ID**: Currently uses `3Cz_lcEAAAAJ` (hardcoded as default)
- **Custom ID**: Set GitHub secret `GSCHOLAR_AUTHOR_ID` to override
- **Script**: `bin/sync_publications.py`
- **Dependencies**: Defined in `requirements.txt` (scholarly, bibtexparser)

**Your Action Required**:
- **Weekly**: Review automated pull requests
- **Approve & Merge**: If publications look correct
- **Edit if needed**: Manually edit BibTeX entries before merging (e.g., add keywords, fix formatting)
- **Close**: If you prefer manual bibliography management

**Manual Trigger**:
```bash
# From GitHub UI: Actions → Sync Publications → Run workflow
# Or via GitHub CLI:
gh workflow run sync-publications.yml
```

---

### 2. Social Feed Refresh (`fetch-social.yml`)

**Purpose**: Fetch recent social media posts (Twitter/X, LinkedIn) to display on your website.

**Schedule**: Every Monday at 08:30 UTC (3:30 AM EST / 4:30 AM EDT)

**What It Does**:
1. Fetches recent posts from configured social accounts
2. Updates `_data/social_staging.yml` with staging feed
3. Creates a pull request for your review
4. Lets you select which posts to feature in `_data/social_curated.yml`

**Configuration**:
- **Script**: `bin/fetch_social_posts.py`
- **Social accounts**: Twitter/LinkedIn handles in script configuration
- **Dependencies**: Defined in `requirements.txt` (feedparser, PyYAML)

**Your Action Required**:
- **Weekly**: Review automated pull requests
- **Curate**: Copy select posts from `social_staging.yml` to `social_curated.yml`
- **Approve & Merge**: After curation
- **Note**: Staging file is overwritten each week; curated file is manual

**Manual Trigger**:
```bash
# From GitHub UI: Actions → Fetch Social Posts → Run workflow
# Or via GitHub CLI:
gh workflow run fetch-social.yml
```

---

## Setup Checklist

### Initial Setup (One-Time)

- [x] Workflows already created in `.github/workflows/`
- [x] Python scripts already created in `bin/`
- [x] Dependencies already defined in `requirements.txt`
- [ ] **Test workflows**: Run manually to verify they work
- [ ] **Set GitHub secrets** (optional):
  - `GSCHOLAR_AUTHOR_ID`: Your Google Scholar ID if different from default

### Weekly Maintenance (Ongoing)

**Every Monday**:
1. Check GitHub for automated pull requests (usually 2):
   - "Sync publications from Google Scholar"
   - "Refresh social staging feed"

2. Review publication sync PR:
   - Verify new publications are correct
   - Add `keywords` field if using thematic filtering (see `BLOG_POSTING_GUIDE.md`)
   - Approve and merge, or close if not needed

3. Review social feed PR:
   - Copy interesting posts from `_data/social_staging.yml` to `_data/social_curated.yml`
   - Approve and merge

**Estimated time**: 10-15 minutes/week

---

## Workflow Details

### Publication Sync Script (`bin/sync_publications.py`)

**How It Works**:
1. Uses `scholarly` Python library to query Google Scholar API
2. Fetches publications for author ID: `3Cz_lcEAAAAJ`
3. Converts to BibTeX format
4. Merges with existing `_bibliography/papers.bib` (preserves manual edits)
5. Sorts by year (descending)

**Customization**:
- Edit `bin/sync_publications.py` to:
  - Change which fields are included
  - Add custom BibTeX fields
  - Filter publications by year or type
  - Adjust formatting

**Limitations**:
- Google Scholar API can be rate-limited
- Some publications may have incomplete metadata
- Manual curation still recommended for:
  - Keywords for thematic filtering
  - Correcting author names
  - Adding DOI links if missing
  - Marking featured publications

### Social Feed Script (`bin/fetch_social_posts.py`)

**How It Works**:
1. Fetches RSS/API feeds from configured social accounts
2. Parses posts and extracts metadata
3. Writes to YAML format for Jekyll consumption
4. Separates staging (auto-updated) from curated (manual selection)

**Customization**:
- Edit `bin/fetch_social_posts.py` to:
  - Add/remove social accounts
  - Change post count limits
  - Filter by hashtags or keywords
  - Adjust date ranges

---

## Testing Workflows

### Test Publication Sync

```bash
# Install dependencies
pip install -r requirements.txt

# Run script locally
python bin/sync_publications.py --dest _bibliography/papers.bib --verbose

# Check output
git diff _bibliography/papers.bib
```

### Test Social Feed Refresh

```bash
# Run script locally
python bin/fetch_social_posts.py --verbose

# Check output
cat _data/social_staging.yml
```

### Test on GitHub Actions

1. Go to **Actions** tab in GitHub repository
2. Select workflow (e.g., "Sync Publications")
3. Click **Run workflow** → **Run workflow**
4. Monitor execution logs
5. Review pull request created by workflow

---

## Disabling Automation

If you prefer manual updates, you can disable workflows:

### Option 1: Disable via GitHub UI
1. Go to **Settings** → **Actions** → **General**
2. Under "Actions permissions", select "Disable actions"

### Option 2: Disable Individual Workflows
1. Go to **Actions** tab
2. Select workflow (e.g., "Sync Publications")
3. Click **⋯** (three dots) → **Disable workflow**

### Option 3: Remove Schedule Trigger
Edit `.github/workflows/sync-publications.yml` and `.github/workflows/fetch-social.yml`:

```yaml
on:
  workflow_dispatch:  # Keep manual trigger
  # schedule:         # Comment out schedule
  #   - cron: "..."
```

This allows manual triggering but prevents automatic weekly runs.

---

## Troubleshooting

### Workflow Fails with "Rate Limited"

**Problem**: Google Scholar API rate limits exceeded

**Solution**:
- Wait 24 hours and re-run manually
- Reduce frequency (change cron to bi-weekly or monthly)
- Add delays in script

### Pull Request Not Created

**Problem**: Workflow runs but no PR appears

**Possible Causes**:
- No new publications found (no changes to commit)
- Permissions issue (check workflow permissions)
- GitHub API rate limit

**Check**:
1. View workflow logs in Actions tab
2. Look for "No changes detected" or error messages

### Publications Missing Metadata

**Problem**: Synced publications lack DOI, keywords, or other fields

**Solution**:
- This is expected; Google Scholar metadata is incomplete
- Manually edit `_bibliography/papers.bib` after merging PR
- Add fields: `keywords`, `doi`, `url`, `abstract`

### Script Dependencies Not Installed

**Problem**: Workflow fails with "ModuleNotFoundError"

**Solution**:
- Verify `requirements.txt` includes all dependencies
- Check Python version (workflows use 3.11)
- Re-run workflow (may be transient GitHub Actions issue)

---

## Advanced Customization

### Change Sync Frequency

Edit `.github/workflows/sync-publications.yml`:

```yaml
schedule:
  - cron: "0 8 * * 1"  # Weekly (Mondays at 08:00 UTC)
  # - cron: "0 8 1 * *"  # Monthly (1st of month at 08:00 UTC)
  # - cron: "0 8 1,15 * *"  # Bi-weekly (1st and 15th at 08:00 UTC)
```

**Cron syntax**: `minute hour day-of-month month day-of-week`

### Add Google Scholar Author ID as Secret

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `GSCHOLAR_AUTHOR_ID`
4. Value: Your Google Scholar ID (e.g., `3Cz_lcEAAAAJ`)
5. Click **Add secret**

Workflow will now use your custom ID instead of hardcoded default.

### Customize Publication Sync Behavior

Edit `bin/sync_publications.py`:

```python
# Example: Only sync publications from last 5 years
current_year = datetime.now().year
pubs = [p for p in pubs if p.get('year', 0) >= current_year - 5]

# Example: Auto-add keywords based on title
if 'clinical trial' in p.get('title', '').lower():
    p['keywords'] = 'trials'
```

### Add Notifications

To get notified when PRs are created, enable GitHub notifications:
1. **Watch** repository (top right)
2. **Settings** → **Notifications**
3. Choose email or web notifications for pull requests

---

## Benefits of Automation

✅ **Reduced maintenance burden**: 10-15 min/week vs. 1-2 hours/month manual updates
✅ **Fresh content**: Publications updated automatically, improving SEO
✅ **Consistent schedule**: Weekly updates without remembering to do it
✅ **Version control**: All changes via PR, easy to review and rollback
✅ **Reproducible**: Scripts documented, no manual copy-paste errors

---

## Related Documentation

- **Blog posting**: See `BLOG_POSTING_GUIDE.md` for quarterly lab updates
- **Quarterly maintenance**: See `ACTION_ITEMS.md` for full content audit checklist
- **Phase 4 plan**: See `plan.md` for ongoing maintenance strategy

---

**Last Updated**: November 2025

**Questions?** Contact Dr. Rashid ([naim@unc.edu](mailto:naim@unc.edu)) or consult GitHub Actions documentation.
