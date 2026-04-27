# Brand System — naimurashid.github.io

This document is the consolidated reference for the typography, color, and
component system used across the site. It supersedes any inline CSS
comments and the earlier per-phase design docs.

## Stack

| Layer | What | Where |
|---|---|---|
| **Source** | al-folio Jekyll theme | upstream |
| **Tokens** | CSS custom properties (`--rl-*`) | `_sass/custom/_tokens.scss` |
| **Type system** | Source Serif 4, Inter, JetBrains Mono via Google Fonts | `_includes/head.html` |
| **Components** | One SCSS partial per component family | `_sass/custom/_*.scss` |
| **Theme switch** | `html[data-theme='dark']` rewrites the same tokens | `_tokens.scss` |
| **Bootstrap** | Still loaded — overridden where needed | upstream `_layouts/default.liquid` |

## Tokens

All defined in `_sass/custom/_tokens.scss`. Light mode at `:root`, dark
mode under `html[data-theme='dark']`. **Never use a hex literal in any
component partial — always reference a token.**

### Type tokens

```
--rl-font-serif:    "Source Serif 4", Georgia, serif      (headings, lede)
--rl-font-sans:     "Inter", system-ui, sans-serif        (body)
--rl-font-mono:     "JetBrains Mono", ui-monospace, monospace (eyebrows, chips)

--rl-text-xs:       12px       (eyebrows, chips, table headers)
--rl-text-sm:       14px       (body small, captions)
--rl-text-base:     16px       (body default)
--rl-text-md:       18px       (lede, paper titles)
--rl-text-lg:       22px       (h3)
--rl-text-xl:       28px       (h2)
--rl-text-2xl:      36px       (h1, post title)

--rl-leading-tight:  1.2       (display, headings)
--rl-leading-normal: 1.55      (body)
```

### Color tokens

```
--rl-bg:             page background (white / near-black)
--rl-bg-subtle:      card / chip / code background
--rl-border:         hairline rule
--rl-border-strong:  active hairline (focus, selected)

--rl-text:           body text
--rl-text-muted:     captions, eyebrows, dates
--rl-heading:        navy in light, off-white in dark

--rl-link:           link default
--rl-link-hover:     link hover
```

### Spacing & shape

```
--rl-space-1 .. --rl-space-8    4px → 64px geometric scale
--rl-radius-sm:    4px
--rl-radius-md:    8px
--rl-shadow-sm:    one-layer hairline shadow
```

## Component partials

Each partial scopes its rules under a single root selector — never
declares bare-tag rules at the document root.

| Partial | Root selector(s) | Phase |
|---|---|---|
| `_tokens` | `:root`, `html[data-theme='dark']` | 1 |
| `_post-prose` | `.post > article > h*, p, ul, …` | 4 |
| `_software-page` | `.software-page`, `.software-card` | 2c |
| `_software-detail` | `.software-detail__*` | 2c |
| `_research-page` | `.research-page`, `.research-grid` | 2a |
| `_grant-card` | `.grant-card`, `.grant-detail__*` | 2b |
| `_funding-stats` | `.funding-stats__*` | 2b |
| `_publications` | `.publications` | 5 |
| `_award-list` | `.post .award-year`, `.post .award-list` | 5 |
| `_hero-panel-audit` | `.hero-panel--academic`, `.hero-panel__*` | 5 |
| `_blog-post` | `.post > article.post-content` | 5 |
| `_cv-page` | `.cv` | 5 |
| `_dark-mode` | `html[data-theme='dark'] …` | 5 |

## Typographic registers (use these names in code review)

The system has four canonical registers. Pick one when introducing any
new text style — don't invent a fifth.

### 1. Display
- `--rl-font-serif`, `--rl-text-2xl` or `--rl-text-xl`, weight 600,
  `--rl-leading-tight`, slight negative tracking
- Used for: page titles, h1, h2, paper titles, section titles
- Color: `--rl-heading`

### 2. Body
- `--rl-font-sans`, `--rl-text-base` or `--rl-text-sm`, weight 400,
  `--rl-leading-normal`
- Used for: paragraphs, list items, table cells, descriptive prose
- Color: `--rl-text`

### 3. Lede
- `--rl-font-serif`, `--rl-text-md`, weight 400, line-height 1.6,
  measure cap 64ch (75ch on blog posts)
- Used for: opening paragraphs, hero panel summary, page intros
- Color: `--rl-text`

### 4. Eyebrow
- `--rl-font-mono`, `--rl-text-xs`, weight 500,
  `letter-spacing: 0.08em`, `text-transform: uppercase`
- Used for: dates, labels, kicker lines, navigation
- Color: `--rl-text-muted`
- Visual variants: bare text, bordered chip, full bg pill

## Decision rules for adding new components

1. **Does it already have a register?** If the new thing is text — pick
   one of the four registers. Don't invent new sizes or weights.
2. **Does it need a wrapper class?** If the new thing is an inline
   eyebrow or chip inside existing markdown content (e.g. `award-year`),
   add a class to the markdown rather than introducing a new selector
   that depends on `<strong>` or `<em>` semantics.
3. **Does the partial already exist?** Most partials are scoped to a
   single page or component family. If the new rule belongs in an
   existing scope, add it there. Only create a new partial if the rule
   set is large enough to warrant its own file (~50 lines or more).
4. **Light + dark.** All new components must work in both themes. If
   tokens cover it, no extra rule. If a bootstrap default leaks through,
   add an override under `_dark-mode.scss`.

## Out-of-band: hardcoded hexes

The repo had ~25 hex literals before Phase 1. The remaining instances
(check via `grep -rn '#[0-9A-Fa-f]\{3,6\}' _sass/custom/`) should always
be zero. If you see one, replace with the appropriate token.

The only exception is `_tokens.scss` itself, where the tokens are
*defined* with hex literals.

## Phase history

| Phase | Branch | Scope |
|---|---|---|
| 1 | `phase-1-academic-rebase` | Token system + base typography |
| 2a | `phase-2a-research` | Research page card grid |
| 2b | `phase-2b-funding` | Grant card + funding-stats inline lede |
| 2c | `phase-2c-software` | Software page card grid + detail layout |
| 4 | `phase-4-post-prose` | Post-layout shared prose typography |
| 5 | `phase-5-system-wrap` | Publications, awards, CV, blog, hero-panel, dark-mode |

Each phase ships as one PR off `master`. Merge in the order above to
keep token references resolved.

## Testing

```bash
bundle exec jekyll serve
```

Visit:
- `/` (home)
- `/about/` (hero panel + selected awards + service)
- `/research/` (interest cards + lede)
- `/research/<topic>/` (topic detail)
- `/software/` (software cards)
- `/software/<package>/` (software detail)
- `/publications/` (bib entries + venue chips)
- `/cv/` (CV cards)
- `/blog/` (post index)
- `/blog/<any-post>/` (post layout)
- `/funding/` (grant cards + funding-stats)

Toggle the theme switch on every page. Resize to 600px wide. Print
preview the CV. None of these should expose untokenized chrome.
