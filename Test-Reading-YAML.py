from pathlib import Path
import shutil
import yaml


def read_markdown(path: Path):
    """Read a Markdown file and extract its YAML front matter."""

    text = path.read_text(encoding="utf-8")

    # Default metadata
    metadata = {}
    content = text

    if text.startswith("---"):
        _, yaml_text, content = text.split("---", maxsplit=2)
        metadata = yaml.safe_load(yaml_text)

    return metadata, content.strip()


metadata, markdown_text = read_markdown(Path("content/Test-File-With-YAML.md"))

print(metadata)
print()
print(markdown_text)