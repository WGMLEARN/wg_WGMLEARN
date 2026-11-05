"""Import meeting Google Docs into meeting-specific Jekyll posts.

Each meeting is declared in docs/_data/meetings.json. The document_env value
names the environment variable that contains that meeting's Google Doc ID.
Within each document, every Heading 1 becomes one generated Jekyll post.
"""

import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from uuid import uuid4

import html2text
from bs4 import BeautifulSoup, NavigableString

ROOT_DIR = Path(__file__).resolve().parent.parent
MEETINGS_FILE = Path(
    os.environ.get("MEETINGS_FILE", ROOT_DIR / "docs" / "_data" / "meetings.json")
)
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", ROOT_DIR / "docs" / "_posts"))


def load_meetings():
    """Return configured meetings, validating their required metadata."""
    try:
        meetings = json.loads(MEETINGS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Meeting registry not found: {MEETINGS_FILE}"
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Meeting registry is not valid JSON: {MEETINGS_FILE}"
        ) from error

    required_fields = {"id", "title", "date", "permalink", "document_env"}
    for meeting in meetings:
        missing_fields = required_fields - meeting.keys()
        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise ValueError(
                f"Meeting {meeting.get('id', '<unknown>')} is missing: {missing}"
            )
    return meetings


def get_document_markdown(meeting):
    """Download a meeting document and convert its HTML export to Markdown."""
    document_env = meeting["document_env"]
    document_id = os.environ.get(document_env)
    if not document_id:
        raise ValueError(
            f"{document_env} is missing for meeting '{meeting['id']}'. "
            "Set the corresponding GitHub Actions secret."
        )

    export_url = f"https://docs.google.com/document/d/{document_id}/export?format=html"
    request = urllib.request.Request(export_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request) as response:
            html_content = response.read().decode("utf-8")
    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Could not download the Google Doc for meeting '{meeting['id']}'. "
            "Ensure the document is accessible to the workflow."
        ) from error

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.body_width = 0
    return converter.handle(html_content)


def convert_html_to_markdown(html_content: str) -> str:
    """Convert HTML to Markdown while preserving tables as HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    tables = {}

    for table in soup.find_all("table"):
        if table.find_parent("table"):
            continue  # Preserve nested tables as part of their parent.

        token = f"WGMTABLE{uuid4().hex.upper()}END"
        tables[token] = str(table)
        table.replace_with(NavigableString(f"\n\n{token}\n\n"))

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False

    markdown = converter.handle(str(soup)).strip()
    for token, table_html in tables.items():
        markdown = markdown.replace(token, f"\n\n{table_html}\n\n")

    return markdown.strip()


def slugify(value):
    """Create a URL-safe slug suitable for filenames and permalinks."""
    slug = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", slug) or "section"


def write_post(meeting, title, body, section_order):
    """Write one stable, meeting-scoped Jekyll post."""
    slug = slugify(title)
    section_id = f"{section_order:02d}-{slug}"
    filename = f"{meeting['date']}-{meeting['id']}-{section_id}.md"
    permalink = f"{meeting['permalink'].rstrip('/')}/{section_id}/"
    filepath = OUTPUT_DIR / filename

    front_matter = {
        "layout": "group",
        "title": title,
        "heading": title,
        "date": meeting["date"],
        "meeting_id": meeting["id"],
        "meeting_title": meeting["title"],
        "meeting_date": meeting["date"],
        "section_order": section_order,
        "permalink": permalink,
    }
    yaml_lines = "\n".join(
        f"{key}: {json.dumps(value, ensure_ascii=False)}"
        for key, value in front_matter.items()
    )
    filepath.write_text(f"---\n{yaml_lines}\n---\n\n{body.strip()}\n", encoding="utf-8")
    print(f"Generated: {filepath}")


def import_meeting(meeting):
    """Split one meeting document into posts using Heading 1 sections."""
    markdown_content = get_document_markdown(meeting)
    sections = re.split(r"(?m)^#\s+(.+)$", markdown_content)

    if len(sections) < 2:
        write_post(meeting, "Meeting document", markdown_content, 1)
        return

    for section_order, index in enumerate(range(1, len(sections), 2), start=1):
        write_post(meeting, sections[index].strip(), sections[index + 1], section_order)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for meeting in load_meetings():
        import_meeting(meeting)


if __name__ == "__main__":
    main()
