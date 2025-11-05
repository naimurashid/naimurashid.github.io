#!/bin/bash
# Create a new lab update post
# Usage: ./bin/new-update.sh "Title" [YYYY-MM-DD]

TITLE="$1"
DATE="${2:-$(date +%Y-%m-%d)}"

if [ -z "$TITLE" ]; then
    echo "Usage: $0 \"Title\" [YYYY-MM-DD]"
    echo "Example: $0 \"Lab Updates Q4 2025\""
    echo "Example: $0 \"New Grant Awarded\" 2025-11-04"
    exit 1
fi

# Slugify title for filename
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')
FILENAME="_posts/${DATE}-${SLUG}.md"

# Create post from template
cat > "$FILENAME" << EOF
---
layout: post
title: "$TITLE"
date: $DATE
description: Brief description for the update
tags: lab-updates
categories: updates
---

## Summary

Brief summary of the update (this will appear in previews).

<!-- excerpt-separator -->

## Details

Full details of the update go here.

### Section 1

Content here.

### Section 2

More content.

---

*Posted by Naim Rashid on $(date -d "$DATE" +"%B %d, %Y" 2>/dev/null || date -j -f "%Y-%m-%d" "$DATE" +"%B %d, %Y" 2>/dev/null || echo "$DATE")*
EOF

echo "Created: $FILENAME"
echo "Edit the file to add your content, then commit and push."
