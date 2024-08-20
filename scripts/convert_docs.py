from os import walk, makedirs
from os.path import join, abspath, dirname as _dirname
from shutil import rmtree, copy
from markdown import markdown
from functools import reduce
import sys

DOCUMENT_FOLDER = abspath(join(__file__, "..", "..", "docs"))
OUTPUT_FOLDER_NAME = "html"
OUTPUT_FOLDER = join(DOCUMENT_FOLDER, OUTPUT_FOLDER_NAME)
STYLE = abspath(join(__file__, "..", "styles.css"))

HTML_TEMPLATE = """
<!DOCTYPE html><html><head><link rel="stylesheet" href="styles.css"></head><body>{html_content}</body></html>
"""

excluded = (OUTPUT_FOLDER_NAME, "source_codes")

rmtree(OUTPUT_FOLDER, True)

for dirname, _, filenames in walk(DOCUMENT_FOLDER):
    if dirname in excluded:
        continue
    for filename in filenames:
        if not filename.endswith(".md"):
            continue
        file = abspath(join(dirname, filename))
        output = abspath(
            join(DOCUMENT_FOLDER, OUTPUT_FOLDER_NAME, filename[:-3] + ".html")
        )
        makedirs(_dirname(output), exist_ok=True)
        with open(file, "r") as file:
            contents = markdown(file.read(), extensions=['extra', 'toc'])
        with open(output, "w") as file:
            file.write(HTML_TEMPLATE.format(html_content=contents))

copy(STYLE, OUTPUT_FOLDER)
