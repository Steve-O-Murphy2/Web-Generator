# Python Static Site Generator

A small static-site generator built with Python. It converts Markdown files into HTML pages using Python-Markdown and Jinja2, and copies static assets into the generated site.

# What you'll build 

In this tutorial, you'll build a simple static site generator (SSG) that converts Markdown files into complete HTML pages. 

# Why an SSG? 

Well, without an SSG you find yourself hand-coding HTML, which can be tedious and error-prone. This is especially true for large sites with many pages. What you do instead is create content using Markdown then convert the Markdown to HTML.

You'll use several Python libraries: `Python-Markdown` to convert Markdown to HTML, `Jinja2` to render HTML templates, `pathlib` to work with files and directories, and `shutil` to copy static assets into the finished site. 

You will also learn a bit about Python libraries and some programming best practices.

To get the most out of this tutorial it would be nice to have Markdown coding experience. You can learn more about Markdown by visiting <https://www.markdownguide.org/>.
# Project setup 

Install libraries: `python -m pip install Markdown Jinja2`

Create the following directories and files. You will add content to the files throughout the course of the tutorial.
``` shell
project root /
    content /
      about.md
      first-post.md
      index.md
    site /       
    static /
      style.css    
    templates /
      page.html      
    build.py
```
* **content/** Markdown source files 
* **static/** Files copied unchanged to the output
* **templates/** Jinja templates used to generate HTML 
* **site/** Generated website files
* **build.py** Build script

The `site` directory contains generated files, so you won't add files to it manually.

# Simplest example

Before you build the entire site, let's start with the smallest useful piece of the process--converting Markdown text to HTML.
Open `build.py`, add the following content, and run the script.
``` python

import markdown

markdown_text = """\
# My First Blog Post

This is my **first page**.

- Item one
- Item two
"""

html = markdown.markdown(markdown_text)

print(html)
```
Console output:
``` html
<h1>My First Blog Post</h1>
<p>This is my <strong>first page</strong>.</p>
<ul>
<li>Item one</li>
<li>Item two</li>
</ul>
```
What just happened? Markdown is defined in the `markdown_text` variable and is embedded between two triple quotation marks, then passed to the `markdown.markdown` function, which converts a markdown string to HTML and return HTML as a Unicode string.

<div style="width:80%; padding:6px; border-radius:5px; border:1px solid powderblue; border-left: 5px solid powderblue" >
Note: If you are new to Python libraries, The dot (.) accesses an attribute of an object. Here, `markdown` is the package, and `markdown` after the dot is an attribute of that package that refers to the `markdown()` function.
</div>


# Convert Markdown defined in a separate file
Now you’ll step it up a bit and put Markdown in a separate file then  convert it to HTML.

You begin by converting the `first-post.md `file. You’ll keep it simple and print the HTML to the console.
Open `first-post.md` and add this content:
``` 
# My First Blog Post
This is my first page.
```
Open `build.py` and completely replace the content with this:
``` python

from pathlib import Path
import markdown
markdown_file = Path(__file__).parent / "content" / "first-post.md"
markdown_text = markdown_file.read_text(encoding="utf-8")
html = markdown.markdown(markdown_text)

print(html)
```
Run `build.py`. The console should now contain this: 
``` html
<h1>Welcome</h1>
<p>This is my first page.</p>
```
Here’s a rundown of the script.
1.	Gets the path to the Markdown file and read the contents into markdown_text.
2.	Converts the text to html by calling markdown.markdown.
3.	Prints the html.
Cool, and pretty fun.
If you are not familiar with `pathlib` and `Path`-- `Path` gives you an expressive and portable way to locate and work with files.
# Build one page 

### What is Jinja?

Think of a Jinja template as a blueprint for a web page. The template contains mostly ordinary HTML, but it also includes placeholders and simple expressions that Jinja replaces with real values when your program runs. Rather than writing a separate HTML file for every page, you define the shared layout once and let Jinja insert the unique content for each page during the build process.

So far you have simply converted a simple Markdown file to HTML using the markdown library. Now you will use templates. You will create the template, add realistic content to a Markdown file, then process the file using markdown and jinja2 functionality.
You will use functionality provided by jinja2.
## Create the Jinja template

The template is HTML with embedded Jinja variables, which are enclosed in `{{}}`. 
For example, this displays the document title  in the HTML `title` tag: `<title>{{ title }}</title>`

The `page.html` file is the template, so open it and add the following to it:
``` html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>{{ title }}</h1>

            <p>
                <strong>Author:</strong> {{ author }}<br>
                <strong>Published:</strong> {{ date }}
            </p>
            <hr>
        </header>
        <main>
            {{ content | safe }}
        </main>
    </body>
</html>
```
### Modify the first-post.md file

Open `first-post.md` and completely replace its contents with the following:
``` 
# My First Blog Post

Welcome to my first blog post! This page is written in **Markdown**, a lightweight markup language that's easy to read and write.

## Why Markdown?

Markdown lets you focus on your content instead of HTML tags. It's widely used for:

- Documentation
- Blog posts
- Project READMEs
- Knowledge bases

## A Short Example

Here's a simple **Python** function:

```python
def greet(name):
    return f"Hello, {name}!"
```

When our static site generator builds this page, the code block will be converted into HTML automatically.


### Modify and run the build script

Open `build.py` and completely replace its contents with this:
``` python
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
```
Run `build.py`. Your console should now contain HTML that aligns with the page.html template:
``` html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>First Post</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>First Post</h1>
            <p>
                <strong>Author:</strong> Stevie<br>
                <strong>Published:</strong> July 30, 2026
            </p>
            <hr>
        </header>
        <main>
            <h1>My First Blog Post</h1>
<p>Welcome to my first blog post! This page is written in <strong>Markdown</strong>, a lightweight markup language that's easy to read and write.</p>
<h2>Why Markdown?</h2>
<p>Markdown lets you focus on your content instead of HTML tags. It's widely used for:</p>
<ul>
<li>Documentation</li>
<li>Blog posts</li>
<li>Project READMEs</li>
<li>Knowledge bases</li>
</ul>
<h2>A Short Example</h2>
<p>Here's a simple <strong>Python</strong> function:</p>
<p><code>python
def greet(name):
    return f"Hello, {name}!"</code></p>
<p>When our static site generator builds this page, the code block will be converted into HTML automatically.</p>
<h2>Learn More</h2>
<p>You can learn more about Markdown by visiting <a href="https://www.markdownguide.org/">https://www.markdownguide.org/</a>.</p>
<p>Happy writing!</p>
        </main>
    </body>
</html>
```
### What happened in the script?

Several things happen in `build.py`.
`Environment` creates its own form of file path for locating and loading templates, in this case `page.html`. 
`template.render` creates HTML by receiving parameters information: title, author, date, and content.
If you look at page.html, you see corresponding variables in double curly brace pairs like this`{{ }}` for title, author, date, and content. These are placeholders into which the `template.render` function places content.
# Build all pages 

At this point, you learned how to convert markdown to HTML using Markdown library and use a Template along with Jinja to convert a single page,  but now you need to build an entire site.
Our site will contain several pages that all share the same overall structure. Each page will  have the same <head> section, stylesheet, navigation, and footer, while only the main content changes. You will use the `page.html` template that you’ve already seen, and you will modify `build.py` to convert all markdown files.

As a preview, here is the pipeline:
```
Delete previous output

↓

Create output directory

↓

Copy static assets

↓

Find every Markdown file

↓

Convert Markdown → HTML

↓

Render HTML into Jinja template

↓

Write output HTML
```

## Add content to other Markdown files

Open `index.md` and add this content:
``` shell
# Welcome

Welcome to my website! This site was generated with a **Python static site generator**.

The site's content is written in Markdown, converted to HTML using Python-Markdown, and rendered into a page template with Jinja2.

## Pages

- [About](about.html)
- [My First Blog Post](first-post.html)

## Why a Static Site?

Static sites are:

- Fast to load
- Easy to deploy
- Secure because they don't require a server-side application
- Simple to maintain

Thanks for visiting!
```
Open `about.md` and add this content:
``` shell
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
```
Finally, replace the content in `build.py` with this code:
``` python
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
for markdown_file in CONTENT_DIR.glob("*.md"):
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
```
Run `build.py`. You will see that the site directory has one HTML file per Markdown file.
## How the build script works

Let’s unpack the code in `build.py`.
### Step 1 – Define project directories

Project directories are defined using functionality from the ` Path` library. Markdown files are in the `content` directory. The code defines the `CONTENT_DIR` variable as that location: 
CONTENT_DIR = Path("content")

`Path("content")` creates a path to the content directory relative to the current working directory.

`STATIC_DIR` contains files that will be copied to the final output location and not be converted to HTML.

`OUTPUT_DIR` defines the output location, and `TEMPLATE_DIR` is the  path to the templates.

### Step 2 – Remove the contents of the output directory

The script removes the `OUTPUT_DIR` contents:
`shutil.rmtree (OUTPUT_DIR)` 
`shutil` is a convenience library for working with directories.
### Step 3 – Copy static assets 

The script copies `STATIC_DIR` contents to the `OUTPUT_DIR`:
shutil.copytree(STATIC_DIR, OUTPUT_DIR, dirs_exist_ok=True)
Files in the `static` directory are copied unchanged.
### Step 4 – Convert each Markdown file to HTML

The script runs a `for in` loop:
``` python
for markdown_file in CONTENT_DIR.glob("*.md"):
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
```
The loop:
1.	Acquires each markdown file in the CONTENT_DIR using the `glob` method. The `*.md` argument is a glob pattern that matches files ending in `.md`. 

2.	Reads the contents of the Markdown file.
The `markdown_file`is a path variable that includes functionality for reading its contents:
`markdown_text = markdown_file.read_text(encoding="utf-8")`
Note: `read_text` includes functionality for opening, reading, and closing a file in a single call.

3.	Converts Markdown to HTML and define the HTML file name:
``` python
html_content = markdown.markdown(markdown_text)
page_title = markdown_file.stem.replace("-", " ").title()
```

4.	Renders the template as HTML and store it in the `rendered_html` variable.
`template.render` passes variables to the template, the template has corresponding variables: `title`, `author`, `date`, and `content`.

5.	Defines the output_file name and write the content as an HTML file in the OUTPUT_DIR.
``` python
output_file = OUTPUT_DIR / f"{markdown_file.stem}.html"
output_file.write_text(rendered_html, encoding="utf-8")
```

At this point in real life, you would be ready to upload your `site` folder to your server.

Note: If you are new to Python `for in` loops, think of it this way:  Each iteration of the loop places a Path object representing the current file into `markdown_file`.

# Refactor the script

Currently, the script performs everything in one monolithic block, so you are going to "pythonify" the script by breaking it into functions, where each function has a specific duty. This gives each function a clear responsibility and makes the code easier to understand, test, and maintain. You will create the following functions:
``` python
build_site()
find_markdown_files()
convert_markdown()
render_page()
copy_static()
```
Replace the content in `build.py` with this code:
``` python
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
```

If you run the script, it will produce the same output as before refactoring.

## Refactored script walk-through
You’ve already about the project directories and removing the `OUTPUT_DIR`, so now let’s analyze the rest of the script.

`build_site()` is the driver. It removes the `OUTPUT_DIR,` then calls: 

`find_markdown_files()`—returns a list of `Path` objects representing the Markdown files in the "content" directory.

`convert_markdown()`—converts the Markdown in one file to HTML and returns the HTML.

`render_page()`—Plugs the page_title and HTML into the template file `page.html`, creates the HTML file name, then writes the HTML to the file. It also hard-codes the `author` and `date` placeholders. Contains a link to the CSS file. `render_page()` runs in a loop, writing HTML for each Markdown file to the `site` directory.

`copy_static()`—Copies everything in the `static`directory  to the `site` directory. In this case `style.css` is the only file copied, but other files such as images like the company logo, fonts, or even JavaScript files could possibly be added to the `static` directory.

When you open a page, the styles are applied to it and you have a very nice-looking site.

# What’s next?
Right now you can only open HTML pages individually, there are no navigation controls, and author and date are hard-coded. You’ll fix that in our next lesson.
You will add YAML to the start of our markdown files that will allow the build script to dynamical get the “author” and “date” variables to pass to the template.render function.

For now, the page links in `index.html` are hard-coded. In the next installment, you'll have the generator create them automatically.
You will also add “previous article” and “next article” to the footer of each HTML page.
