#!/usr/bin/env bash
# Create a timestamped post that mirrors short social updates.
# Usage: bin/new-update.sh "Title of Update" [YYYY-MM-DD]

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 \"Title of Update\" [YYYY-MM-DD]" >&2
  exit 1
fi

TITLE=$1
DATE=${2:-$(date +"%Y-%m-%d")}

if ! [[ $DATE =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
  echo "Invalid date: $DATE (expected YYYY-MM-DD)" >&2
  exit 1
fi

SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-|-$//g')
POST_PATH="_posts/${DATE}-${SLUG}.md"

if [[ -f "$POST_PATH" ]]; then
  echo "File already exists: $POST_PATH" >&2
  exit 1
fi

cat <<EOF > "$POST_PATH"
---
layout: post
title: "${TITLE}"
description: ""
categories: [update]
tags: [update]
excerpt_separator: <!--more-->
---

<!-- Paste the same blurb you used on social. -->

Intro sentence or two that mirrors the social update.<!--more-->

Add optional supporting detail, slides, or a link:

- [Resource title](https://example.com)
- Next steps or call-to-action.
EOF

echo "New update drafted at $POST_PATH"
