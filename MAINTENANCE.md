# Site Maintenance Helpers

## Social feed

- Run `bin/fetch_social_posts.py --verbose` (or wait for the “Fetch Social Posts” GitHub Action) to populate `_data/social_staging.yml` with the past two years of posts from the RSS feeds listed in `_data/social_sources.yml`.
- Review `_data/social_staging.yml` and copy the entries you want live into `_data/social_curated.yml`; those curated items drive the homepage feed.
- Update `_data/social_sources.yml` if you change handles or swap RSS providers (e.g., Nitter instance, Bluesky handle). For LinkedIn, export your posts from *Settings & Privacy → Data privacy → Get a copy of your data → Posts* and run `bin/import_linkedin_posts.py --csv path/to/Shares.csv --verbose` to merge them into the staging file.
- The automated workflow lives in `.github/workflows/fetch-social.yml` and opens a weekly PR so you can approve new highlights on your schedule.

## Quick update posts

- Use `bin/new-update.sh "Title"` to scaffold a short `_posts/` entry mirroring a social blurb.
- Pass an explicit date for back-dated content: `bin/new-update.sh "Talk at JSM" 2024-08-03`.
- Each template includes an `excerpt_separator` so the homepage teaser stays tight.

## Publications sync

- Install Python deps once: `pip install -r requirements.txt`.
- Run `bin/sync_publications.py --verbose` to refresh `_bibliography/papers.bib` (defaults to Scholar ID `3Cz_lcEAAAAJ`).
- Optionally override the ID with `bin/sync_publications.py --author-id <OTHER_ID>` or by exporting `SCHOLAR_AUTHOR_ID`.
- GitHub Actions automation lives in `.github/workflows/sync-publications.yml`; add a repo secret `GSCHOLAR_AUTHOR_ID` if you prefer not to use the baked-in default, and ensure the default `GITHUB_TOKEN` (or a PAT with `contents`/`pull_requests` scope) is available so the workflow can open its weekly PR.

## Image pipeline

- `bundle exec jekyll build` now expects ImageMagick (`convert`) in PATH for responsive images.
- Keep member headshots under `assets/img/` with consistent framing; alt text falls back to the member name but you can override via `profile.image_alt`.

## Team badges

- Map `profile.team-position` values to Bootstrap badges using `_config.yml` → `team_badges`.
- Add new keys (lowercase) for additional statuses; the badge styling lives in `_sass/_custom.scss`.
