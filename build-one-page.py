from jinja2 import Environment, FileSystemLoader
import markdown
from pathlib import Path

def main():
    environment = Environment(loader=FileSystemLoader(Path("templates")))
    template = environment.get_template("page.html")
    markdown_file = Path("content") / "first-post.md"
    markdown_text = markdown_file.read_text(encoding="utf-8")
    page_title = "First Post"
    html_content = markdown.markdown(markdown_text)
    rendered_html = template.render(
            title=page_title,
            author="Stevie",
            date="July 30, 2026",
            content=html_content,
        )
    print(rendered_html)

if __name__ == "__main__":
    main()