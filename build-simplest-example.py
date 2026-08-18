import markdown

markdown_text = """\
# My First Blog Post

This is my **first page**.

- Item one
- Item two
"""

html = markdown.markdown(markdown_text)

print(html)
