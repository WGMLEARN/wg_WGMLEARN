# scripts/fetch_docs.py
import os
import re
import urllib.request
from datetime import datetime

import html2text

DOC_ID = os.environ.get("GOOGLE_DOC_ID")
if not DOC_ID:
    raise ValueError("GOOGLE_DOC_ID environment variable is missing.")

EXPORT_URL = f"https://docs.google.com/document/d/{DOC_ID}/export?format=html"
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Fetch Google Doc HTML
req = urllib.request.Request(EXPORT_URL, headers={"User-Agent": "Mozilla/5.0"})
html_content = urllib.request.urlopen(req).read().decode("utf-8")

# 2. Convert to Markdown
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.body_width = 0  # Do not wrap lines
markdown_content = converter.handle(html_content)

# 3. Split sections by top-level H1 headings: # Title
# Matches lines starting with '# '
sections = re.split(r"(?m)^#\s+(.+)$", markdown_content)

# sections[0] contains any text before the first heading
# Following elements alternate: [heading_title, section_body, heading_title, section_body, ...]
today = datetime.now().strftime("%Y-%m-%d")

if len(sections) < 2:
    # Fallback if no H1 headings exist: save everything as a single post
    filename = f"{today}-google-doc-content.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(
            f"---\nlayout: post\ntitle: Google Doc Import\ndate: {today}\n---\n\n"
            + markdown_content
        )
    print(f"Created fallback single file: {filepath}")
else:
    for i in range(1, len(sections), 2):
        title = sections[i].strip()
        body = sections[i + 1].strip()

        # Create a URL-safe slug from the heading
        slug = re.sub(r"[^\w\s-]", "", title).strip().lower()
        slug = re.sub(r"[-\s]+", "-", slug)

        filename = f"{today}-{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        front_matter = f"""---
layout: post
title: "{title}"
date: {today}
---

"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(front_matter + body + "\n")

        print(f"Generated: {filepath}")
