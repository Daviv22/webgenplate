from pathlib import Path

TEMPLATE_HTML_FILE = Path('boilerplates/boilerplate_html.txt')

def insert_boilerplate(directory):
    destiny = directory / 'index.html'
    destiny.write_text(TEMPLATE_HTML_FILE.read_text())

def create_project():
    base = Path('teste')

    for folder in ["js", "css", "assets"]:
        (base / folder).mkdir(parents=True, exist_ok=True)

    (base / 'README.md').touch()

    insert_boilerplate(base)

create_project()
