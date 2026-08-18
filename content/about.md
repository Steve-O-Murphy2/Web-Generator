# About This Site

This site was built with Python as a simple example of a static site generator.

The site's content is written in Markdown. The build script converts the Markdown files to HTML and uses a Jinja template to create complete web pages.

## About the Project

The generator uses a few Python libraries:

- **Python-Markdown** converts Markdown to HTML.
- **Jinja2** combines the generated HTML with an HTML template.
- **pathlib** works with files and directories.
- **shutil** copies static assets such as CSS files.

The goal isn't to build a full-featured publishing system. It's to demonstrate how a few focused Python tools can work together to automate the process of creating a website.

## What's Next?

This project can be extended in many ways, including automatically generating navigation, adding article metadata, and supporting more sophisticated templates.