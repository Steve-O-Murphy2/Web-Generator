from pathlib import Path
import shutil

import markdown
from jinja2 import Environment, FileSystemLoader

# Project directories
CONTENT_DIR = Path("content")
STATIC_DIR = Path("static")
OUTPUT_DIR = Path("site")
TEMPLATE_DIR = Path("templates")

# Start with a clean output directory
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)

OUTPUT_DIR.mkdir()

# Copy static assets
shutil.copytree(STATIC_DIR, OUTPUT_DIR, dirs_exist_ok=True)

# Load the Jinja template
# Environment is jinja
environment = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
# Template is jinja
template = environment.get_template("page.html")

# Build each Markdown file
# markdown_file is a pathlib thing.
for markdown_file in CONTENT_DIR.rglob("*.md"):
    markdown_text = markdown_file.read_text(encoding="utf-8")

    # markdodwn is from the markdown lib
    # convert the file to html
    html_content = markdown.markdown(markdown_text)

    page_title = markdown_file.stem.replace("-", " ").title()

    rendered_html = template.render(
        title=page_title,
        author="Stevie",
        date="July 30, 2026",
        content=html_content,
    )

    output_file = OUTPUT_DIR / f"{markdown_file.stem}.html"
    output_file.write_text(rendered_html, encoding="utf-8")

    print(f"Generated {output_file}")