# Changelog

All notable changes to the Rashid Lab website are documented in this file.

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
