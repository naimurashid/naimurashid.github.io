# Changelog

All notable changes to the Rashid Lab website are documented in this file.

## [2026-08-12] - Content Refresh

### Changed (round 3, same day) — readability pass
- **Talks grid locked to two columns** (was auto-fit, could resolve to 1/2/3 depending on viewport); single column below 640px
- **Publication abstracts un-justified** — the base theme's `.hidden` abstract expander used `text-align: justify`, producing word-spacing rivers in a narrow measure
- **64ch prose measure extended to `.page-section` wrappers** — funding/software/teaching pages wrap markdown in sections that escaped the `.post > article` measure cap, so lists ran ~105 characters per line
- **Micro-type floor enforced at 12px** — team-card role badges were 0.65rem (10.4px); `.focus-card__badge` and `.page-intro__eyebrow` were 0.72rem
- **Talk-card venue legibility** — long uppercase mono venue strings bumped 12px → 13px with tighter tracking and looser line-height
- **`text-wrap: balance` on card titles and section headings** so two-line titles split evenly instead of orphaning one word
- All in `_sass/custom/_hotfixes-r2.scss` section 6

### Changed (round 2, same day)
- **Talks section reworked to four featured cards, compact list removed.** Published two more decks to `rashidlab/talks` (FDA CDRH OSEL "When Biomarkers, Assays, and Protocols Co-evolve", May 2026; Lineberger Innovate Cancer Data Science Symposium "Leveraging AI in Biomarker-Driven Trial Design", January 12, 2026) as self-contained HTML. All four cards now have View slides buttons; the six talks without materials were dropped from the page (they remain in the CV). Card layout made consistent in `_hotfixes-r2.scss`: meta stacks vertically (date pill, then venue), cards are flex columns with actions pinned to the bottom, buttons sit side by side.

### Added
- **Two 2026 invited talks** to the about-page talks list, both with "View slides" links to the public decks in `rashidlab/talks`:
  - "Adaptive Trial Design for the RAS-Inhibitor Era" (NCI GI SPORE Meeting, June 2026)
  - "Staying in the Driver's Seat: Calibrating AI Use in Statistical Research, Training, and Practice" (ASA StatsUp.AI webinar, May 2026), with a link to the companion resources repo
- **DeCAF paper** (Peng et al., Cell Reports Medicine 2026, `10.1016/j.xcrm.2026.102611`) added to `_bibliography/papers.bib` (`selected: true`) and `_data/publication_highlights.yml`
- **Three news items**: StatsUp.AI webinar (May 2026), GI SPORE talk (June 2026), Amber Young PhD + Natera (Aug 2026)
- **Five 2025-2026 invited talks from the CV** (May 2026 compile) added to the talks list: V Scholar Summit panel, FDA CDRH OSEL AI Seminar, ARPA-H ADAPT Program Meetings (Phoenix 2026, DC 2025), Lineberger Data Science Symposium; JHU October 2025 talk title aligned with the CV

### Changed
- **Co-Investigator funding portfolio synced to the June 2026 other support document** (cpos-2414070, certified 2026-06-11): added 8 active awards missing from the page (Human Cancer Metabolome Atlas R01, male breast tumor R37, EGFR basal PDAC R01, PREDICT-RD, TBCRC 059/ETHAN, DOD spatial reprogramming, Komen ADC, Gateway/Rochester FOLFIRINOX subaward) and moved 7 ended awards (Lustgarten PRO-CLAIM, ACS RSG, Komen OG, R37-C247676, three R01s ending 2025) from Active to Completed
- **Amber Young moved to alumni**: `_members/about_amber.md` regrouped to Former Students with Alumni badge, position Biostatistician at Natera, bio rewritten past-tense with DeSurv dissertation summary; added to teaching-page placements (advisee count 5 → 6, co-advisor list gains Li); software-page contributor line updated
- **DeSurv corrected across software/projects pages**: description fixed from "de-biased survival estimators" to survival-guided NMF (Cox-supervised factorization), GitHub link fixed from nonexistent `naimurashid/DeSurv` to `rashidlab/DeSurv`, added `rashidlab/DeSurv-paper` reproducibility link, status pill In Development → GitHub, year 2025 → 2026

### Fixed
- **Broken member profile links on `/projects/`** — hardcoded `/members/about_X/` trailing-slash URLs 404 on GitHub Pages (member pages render as `about_X.html`); dropped the trailing slashes
- **Removed stale legacy stubs** `_pages/about_amber.md` and `_pages/about_euphy.md` (orphaned duplicates of `_members/` profiles, still rendering "Current Student" pages)

## [2026-04-27] - Post-Phase-7 Polish

### Changed
- **Site `max_width` 1120px → 1080px → 1024px → 992px → 960px → 920px**. Iterative site-wide tightening to reduce visual sprawl on wide monitors. Empirical 3-col → 2-col breakpoint on the most-constrained grid (`.project-grid` with minmax(320px, 1fr)) is at 858px, so 920 retains a 62px safety buffer. 3-col card grids on `/software/`, `/projects/`, `/funding/` continue to render with cards at ~280px each. (Commits `8bf913dd`, plus follow-up tightening.)

### Fixed
- **Polish round (commit `bea9a47d`)** — four small alignment fixes added to `_hotfixes-r2.scss`:
  - `/about/` hero: tighter gap between paired `.hero-panel__lead` paragraphs (12px vs 24px) using `:has(+ .hero-panel__lead)`
  - `/software/` `.software-card h3::before` (decorative navy-gradient 8x8 circle): added 8px right-margin so the bullet doesn't sit flush against the title
  - `/software/` meta pills row: locked all pills to a uniform height (was 25/25/33 — trailing pill rendered taller despite identical markup)
  - `/software/` Hex sticker download links inside `.software-card__links`: switched from inline-flex to plain inline + dropped the `↓` arrow, so they baseline with sibling regular links
- **About page hero rendering as one merged paragraph** — Kramdown collapses adjacent HTML block elements without an empty-line boundary; added the blank line so the two `.hero-panel__lead` paragraphs render as separate `<p>` elements (commit `41768590`)
- **Dark-mode toggle was silently no-op'ing on click** (commit `a60c4555`). Root cause traced to commit `fb8b0328` (the original "force reflow on toggle" fix), which accessed `document.body.style` unconditionally. Since `applyTheme()` runs from `initTheme()` during `<head>` parsing — when `document.body` is null — that line threw a `TypeError`, aborting `initTheme()` before it could register the toggle's click listener. Every cold page load left the toggle button without a handler. Three layered fixes in `assets/js/theme.js`: (1) guard the body-bg recompute behind `if (document.body)`, (2) bind the click handler via multiple lifecycle events (immediate / DOMContentLoaded / window.load) with a `dataset.rlToggleBound` flag for idempotence, (3) replace the synchronous `offsetHeight` recompute with a two-frame `requestAnimationFrame` cycle. Also sets `color-scheme` on `documentElement` so the browser UA chrome (scrollbars, form controls) follows the theme.
- **`.talks-section` dark-mode regression** (caught in post-Phase-7 spot-check) — was rendering with `rgba(255, 255, 255, 0.9)` background and `--global-shadow-lg` lift in dark mode. Now flips to `--rl-bg-subtle` + hairline border + `--rl-shadow-sm` under `html[data-theme="dark"]` (commit `ac9d41a4`)

### Added
- **Hero "Recent News" stack** — three-row hairline list at the bottom of the about hero text column, auto-pulling the most recent non-inline items from `_news/`
  - Header matches `.hero-panel__tagline` register (IBM Plex Mono 12px 500, muted, 0.08em tracking, uppercase)
  - Hairline-rule separator above the section
  - Row format: `[mono date] [serif title link]` separated by hairlines

### Changed
- **About hero lead paragraph** trimmed and linked
  - Added hyperlink to UNC Gillings School of Global Public Health (`https://sph.unc.edu/`)
  - Removed redundant 3rd sentence (~25 words restating sentence 2)
- **Software cards** drop inline hex-mark badges in the card head
  - The 56×64 hex stickers next to each h3 forced the head row to 66px (vs. ~30px without). Now removed; downloadable SVGs remain in `assets/img/hex/` and are still linked in each card's link cluster.

### Technical Details
- Commits: `c2a6ee89`, `250cee05`, `9d52f7ea`, `7d637af5`
- New partial: `_sass/custom/_hero-recent.scss`
- Hero asymmetry between text col and aside (with portrait loaded): closed from ~254px to ~134px

---

## [2026-04-27] - Phase 7

### Added
- **Hotfixes Round 2** (`_sass/custom/_hotfixes-r2.scss`)
  - `/blog/` listing — `.header-bar h1` capped at `--rl-text-2xl`, post titles Source Serif 22px, `.post-meta` and `.post-tags` IBM Plex Mono uppercase
  - `/team/` — `.team-group-block__header h3` Source Serif 22px (was Archivo 20px); `.team-member-card` resting shadow tightened to `--rl-shadow-sm`
  - `/repositories/` — `.repositories` flex container `gap: var(--rl-space-4)` (was 0)
- **Dark-mode fixes pass** (`_sass/custom/_dark-mode-fixes.scss`)
  - `.news-card`, `.social-feed__card`, `.publication-highlights__card` flip to `--rl-bg-subtle` in dark mode (were stuck on cream/white via `var(--global-neutral-light)` / `var(--global-bg, #fff)`)
  - `#bibsearch.bibsearch-form-input` flips bg/text/border in dark mode
  - `#diagram-legend` overrides inline `style="background:#f8f9fa"` via `!important`
  - `#back-to-top` bg from `rgba(255,255,255,0.5)` → `rgba(255,255,255,0.08)`
  - Lift shadows on `.software-card`, `.talk-card`, `.recognition-card`, etc. normalized to `--rl-shadow-sm`

### Fixed
- **Sass mixed-decls deprecation** in `_sass/custom/_components.scss:108` (declaration after nested rules wrapped in `& {}`)
- **Blog header bar** rendered "al-folio" / theme tagline as page title — `_config.yml` `blog_name` and `blog_description` cleared, hides the entire `<div class="header-bar">` block per the template's existing if-guard

### Technical Details
- Commits: `4171409b`, `7b8738a3`, `1d12685e`, `86c17e36`
- All dark-mode rules scoped under `html[data-theme="dark"]` so light mode is unchanged
- Cascade order: `hotfixes-r1 → hotfixes-r2 → dark-mode-fixes` (each round loaded after surfaces it fixes)

---

## [2026-04-27] - Phase 6: Hotfixes + Imagery

### Added
- **Imagery pass** (`_sass/custom/_figures.scss`, `assets/img/hex/{baton,desurv,evolvetrial,purist}.svg`)
  - Hairline-bordered figure treatment for `.post figure` / `.post-content > figure`
  - Source Serif 4 italic `figcaption` with mono "Figure N." eyebrow
  - `.software-card__download` styling (mono caps with ↓ glyph)
  - 4 downloadable hex SVGs at 174×200 viewBox (R-community 5.08×5.87cm spec)
- **Hex sticker download links** wired into PurIST, BATON, evolveTrial, deSurv card link clusters

### Fixed (Hotfixes Round 1)
- **Hero panel padding** (`/about/`) restored from `1.5rem 0 2rem` (zero horizontal) to `var(--rl-space-6)` — picture no longer sits flush at the right edge
- **Hero panel lead** switched from `--rl-font-serif` to `--rl-font-sans` so register matches body text on every other page
- **Publications venue badges** regain Carolina-blue tint (Phase 5 had neutralized them to a near-invisible chip)
- **Software card head→desc gap** locked via `0 0 var(--rl-space-3)` margin; hex sticker clamped to 56px max
- **Projects + Funding pages** flattened to RL token system: drop gradient backgrounds, `translateY` hovers, entry animations, accent `::before` stripes, and emoji-prefixed badges. Stage stripes replaced with calm 3px left borders. `.grant-card--featured` gets a 3px Carolina left border.

### Technical Details
- Commits: `a893f701`, `9ff89de3`, `b4f220fc`, `f13201bd`
- New partial loaded as the trailing override: `_sass/custom/_hotfixes-r1.scss`
- Apply scripts: `apply-phase-6-hotfixes-r1.sh`, `apply-phase-6-imagery.sh`

---

## [2026-04-23] - Phase 5: System Wrap

### Added
- **Publications page typography** (`_sass/custom/_publications.scss`) — `.title` / `.author` / `.periodical` / `.links`
- **Award-list eyebrow chip pattern** (`_sass/custom/_award-list.scss`) — applied to `/about/` Selected Awards section (markup converted from markdown bullets to `<ul class="award-list">` HTML)
- **Hero-panel-academic token alignment** (`_sass/custom/_hero-panel-audit.scss`)
- **Blog post rhythm** (`_sass/custom/_blog-post.scss`) for `post.liquid` layout
- **CV page typography** (`_sass/custom/_cv-page.scss`) for `cv.liquid` layout
- **Dark-mode hygiene catch-all** — full rewrite of `_sass/custom/_dark-mode.scss` to a token-aware system (419 → 89 net lines after consolidation)
- **`BRAND_SYSTEM.md`** root-level consolidated reference

### Fixed
- **Theme toggle stale-paint bug** — `assets/js/theme.js` now forces a reflow (`void document.body.offsetHeight`) after setting `data-theme` so body/cards repaint immediately
- **Dark-mode footer** was inverting *backwards* (navy → light gray); pointed at `--rl-bg-subtle` so it stays dark

### Technical Details
- Commits: `6c0a46a0`, `ca87bc95`, `fb8b0328`
- Apply script: `apply-phase-5-system-wrap.sh`

---

## [2026-04-23] - Phase 4: Post-Prose Typography

### Added
- `_sass/custom/_post-prose.scss` — extends Phase 2a token-driven typography from grant/software card interiors out to the prose body of every page using `layout: page` / `layout: about`
- Selectors use the direct-child combinator (`>`) so styles do not ripple into nested cards (`.grant-card`, `.software-card`, `.talk-card`, `.hero-panel`)
- Scope: `.post article > h2`/`> h3`/`> h4`/`> p`/`> ul`/`> ol`, plus `.talk-card` interior typography matching grant-card register

### Technical Details
- Commit: `15975032`
- Apply script: `apply-phase-4-post-prose.sh`

---

## [2026-04-23] - Phase 2c: Software-Page Polish

### Added
- `_sass/custom/_software-card.scss` — four-slot internal card layout: `__head`, `__desc`, `__meta` (mono pills), `__refs`, `__links`
- Status pills with single accent dots: CRAN blue, Bioconductor teal, Carolina clinical, amber in-development
- `.software-page__lede` opening sentence treatment (Source Serif 22px)

### Changed
- `_pages/software.md` rewritten to four-slot card structure (138 → 178 lines)

### Technical Details
- Commits: `5583df18`, `072e013c`
- Apply script: `apply-phase-2c-software-polish.sh`
- Note: apply script unintentionally committed a `.bak` backup; cleanup commit `072e013c` removed it

---

## [2026-04-23] - Phase 2b: Hex-Mark System

### Added
- `_includes/hex-mark.html` — reusable Liquid include for inline SVG hex marks
- `_sass/custom/_hex-mark.scss` — sizing/color treatment
- Hex mark calls integrated into `_pages/software.md` (subsequently removed in 2026-04-27 polish; downloadable SVGs retained)

### Technical Details
- Commit: `73c543e3`
- Apply script: `apply-phase-2b-hex-marks.sh`

---

## [2026-04-23] - Phase 2a: Page Typography

### Added
- `_sass/custom/_page-typography.scss` — interior typography pass for `.grant-card` and `.software-card` on `/funding/` and `/software/`
- Card titles → Source Serif 4 22px / 600 (was Archivo 18px / 700)
- Grant detail values → IBM Plex Mono with `font-variant-numeric: tabular-nums` so dollar amounts and date ranges line up vertically
- Software-card metadata labels → mono eyebrows; nested patents list gets a 2px left rule

### Technical Details
- Commit: `d7b6641a`
- Apply script: `apply-phase-2a-page-typography.sh`

---

## [2026-04-23] - Phase 1: Academic Brand Rebase

### Added
- **Design tokens** (`_sass/custom/_tokens.scss`) — single source of truth for color, type, spacing, radius, shadow; emitted as CSS custom properties so dark mode can swap them without recompile
- **Component placeholders** (`_sass/custom/_components.scss`) — `%rl-card` / `%rl-pill` / `%rl-eyebrow` extended by 14 card classes via `@extend`
- **Decorative-chrome neutralizer** (`_sass/custom/_neutralize.scss`) — kills radial/linear gradients, role-colored pathway borders, hover translateY lifts, staggered fadeInUp animations, gradient H2 underline bars

### Changed
- **Google Fonts** — Open Sans + Libre Baskerville → Archivo + Source Serif 4 + IBM Plex Mono (via `_config.yml` `google_fonts` URL; `head.liquid` reads it through a Liquid template variable)
- **Page width** — `max_width` 930px → 1120px
- **Progressbar** — disabled (`enable_progressbar: false`)
- **Sass-level brand variables** expanded in `_sass/custom/_variables.scss`

### Technical Details
- Commit: `f7103bab`
- Apply script: `apply-phase-1-brand-refresh.sh`

---

## [2026-01-31] - Team Photo Cropping Fix

### Fixed
- **Team member photos no longer crop heads** - Changed aspect ratio from 1:1 (square) to 4:5 (portrait)
- Photos for Euphy Wu, David Lim, and others now display full heads without cropping

### Technical Details
- Added `object-position: top center` to prioritize showing top of images
- Changed `.team-member-card__media` from `aspect-ratio: 1` to `aspect-ratio: 4 / 5`
- Portrait aspect ratio provides 25% more vertical space for face visibility

---

## [2026-01-31] - Cross-Page Aesthetic Consistency

### Added
- **Unified hero sections** across Team, Research, Teaching, and Projects pages with gradient backgrounds and page-specific accent colors
- **Eyebrow badges** for section labels (e.g., "Overview", "Stage 1", "People") providing consistent visual hierarchy
- **Team page enhancements**
  - Team callout section with green accent border for PhD recruitment info
  - Team member cards with hover effects, social badges (LinkedIn, GitHub, Website)
  - Group headers with member count badges
- **Software page enhancements**
  - Software card grid with blue bullet indicators
  - Styled package lists for R packages and legacy tools
- **Projects page enhancements**
  - Stage-based emoji badges: 🔨 develop, 🧪 pilot, ✅ adopt, 📖 story
  - Project cards with accent borders matching development stage
  - Collaboration callout section
- **Funding page enhancements**
  - Grant cards with featured styling and warm accent top border
  - Leadership grid with role descriptions
  - Funding accordion for expandable sections
  - Timeline cards with role badges (PI, Co-PI, Core Co-Director)
- **Publications page enhancements**
  - Theme filter pills with active state styling
  - Collapsible publication sections with arrow indicators
- **Research page enhancements**
  - Focus area cards with left border accents
  - Focus chips for publications and features
  - Plain language descriptions in italics
- **Teaching page enhancements**
  - Outcomes section styling
  - Training expectations grid
- **Page CTA sections** with accent border variants (student, usage, collaboration)
- **Staggered fade-in animations** for cards across all pages
- **Full dark mode support** for all new components

### Changed
- Extended `_sass/custom/_aesthetic-refinements.scss` from ~835 to ~2380 lines
- Standardized card hover effects (translateY lift + enhanced shadow)
- Consistent section spacing and alternating backgrounds
- Responsive breakpoints for mobile across all new components

### Technical Details
- CSS architecture uses BEM-style naming (e.g., `team-member-card__body`, `project-card__badge--pilot`)
- All styles centralized in single SCSS file for maintainability
- CSS custom properties (variables) used for color consistency
- Animations respect `prefers-reduced-motion` media query

---

## [2026-01-31] - About Page Aesthetic Refinements

### Added
- **Navigate by Role cards** with subtle gradient background tints and Tabler icons
  - Students: school icon, green accent
  - Collaborators: stethoscope icon, blue accent
  - Funders: certificate icon, teal accent
- **Quick Links** with icons (flask, code, building-bank)
- **Equal-height social feed cards** for LinkedIn/news sections
- **Publication badge vertical alignment** improvements
- **Focus card list items** with gradient bullet points
- **Hero panel CTA** with improved button hierarchy
- **Link arrow styles** with hover animation
- **Subtle fade-in animations** with staggered delays

### Changed
- Set `max_author_limit: 5` in `_config.yml` for cleaner publication lists
- Added icons to pathway cards in `_pages/about.md`
- Created `_sass/custom/_aesthetic-refinements.scss` (835 lines)
- Updated `_sass/_custom.scss` to import aesthetic refinements

---

## [2026-01-31] - Publication DOI and Citation Fixes

### Fixed
- Resolved "(missing reference)" text appearing on publications page
- Fixed broken DOI links for multiple papers
- Restored colored journal badges on about page

### Added
- Created `_data/venues.yml` with journal colors for publication badges
- Added verified DOIs to `_bibliography/papers.bib` using PubMed lookup
- Added `abbr` fields to papers.bib for journal badge display

### Changed
- Shortened ADAPT Cancer Cell paper author list for readability
