from pathlib import Path
import markdown
markdown_file = Path(__file__).parent / "content" / "first-post.md"
markdown_text = markdown_file.read_text(encoding="utf-8")
html = markdown.markdown(markdown_text)

print(html)