from pathlib import Path
import shutil

import markdown
from jinja2 import Environment, FileSystemLoader

# Project directories
CONTENT_DIR = Path("content")
STATIC_DIR = Path("static")
OUTPUT_DIR = Path("site")
TEMPLATE_DIR = Path("templates")

def build_site():

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir()

    markdown_files = find_markdown_files()

    for markdown_file in markdown_files:
        html = convert_markdown(markdown_file)
        render_page(markdown_file, html)

    copy_static()

def find_markdown_files():
    return CONTENT_DIR.glob("*.md")

def convert_markdown(markdown_file):
    markdown_text = markdown_file.read_text(encoding="utf-8")
    return markdown.markdown(markdown_text)

def render_page(markdown_file, html):
    environment = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = environment.get_template("page.html")
    page_title = markdown_file.stem.replace("-", " ").title()
    rendered = template.render(
        title=page_title,
        author="Stevie",
        date="July 30, 2026",
        content=html,
    )
    output_file = OUTPUT_DIR / f"{markdown_file.stem}.html"
    output_file.write_text(rendered, encoding="utf-8")

def copy_static():
    shutil.copytree(STATIC_DIR, OUTPUT_DIR, dirs_exist_ok=True)

if __name__ == "__main__":
    build_site()