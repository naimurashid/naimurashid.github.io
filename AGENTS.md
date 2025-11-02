# Repository Guidelines

## Project Structure & Module Organization
This site runs on the al-folio Jekyll theme. Content lives in `_pages/` for standalone sections, `_posts/` for dated updates, `_projects/`, `_members/`, and `_news/` for collection-driven pages, and `_data/` for YAML-driven listings. Layouts and partials are in `_layouts/` and `_includes/`, while styling sits in `_sass/` and `assets/`. Site-wide configuration belongs in `_config.yml`; treat `bin/` scripts and `docker-compose*.yml` as operational tooling.

## Build, Test, and Development Commands
Install Ruby gems with `bundle install` and JavaScript tooling with `npm install`. Run `bundle exec jekyll serve --livereload` for local previews and `bundle exec jekyll build` for production-ready output. Use `bundle exec jekyll doctor` before committing to catch configuration issues. `npx prettier --write .` keeps Liquid, HTML, Markdown, and JSON formatting consistent.

## Coding Style & Naming Conventions
Follow two-space indentation for Liquid, HTML, and YAML. Front matter keys should stay lowercase with hyphenated multiword values (e.g., `title:`, `nav-title:`). Name blog posts `YYYY-MM-DD-slug.md`; collection items match their collection folder (`_projects/project-name.md`). Favor descriptive asset names like `assets/img/profile-2024.jpg`. Run the bundled Prettier plugin for Liquid templates to normalize filters and tag spacing.

## Testing Guidelines
Always verify `bundle exec jekyll build` completes without warnings before opening a PR. For quick health checks, `bundle exec jekyll doctor` highlights missing data or broken includes. When editing typography or layouts, spot-check the generated `_site/` output in multiple breakpoints. Run `npx prettier --check .` to ensure formatting stays clean; fix violations with the write command above.

## Commit & Pull Request Guidelines
Match the existing short, imperative commit style (`Update about.md`, `Add cv download link`). Group related changes and avoid bundling unrelated content edits with styling tweaks. PRs should describe the change scope, highlight any new configuration flags, and link to relevant issues or preview URLs. Include before/after screenshots for visual updates and note any manual steps (e.g., running `bin/deploy`) reviewers should repeat.

## Deployment & Environment Notes
Use `bin/deploy` for GitHub Pages releases; it enforces a clean worktree and pushes the built site to `gh-pages`. For containerized previews, `docker-compose up --build` reproduces the production stack without touching local gems. Set `JEKYLL_ENV=production` when validating SEO metadata or asset pipelines to mirror deployed behavior.
