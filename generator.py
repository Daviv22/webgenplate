from pathlib import Path

TEMPLATE_HTML_FILE = Path('boilerplates/html_boilerplate.txt')

def basic_project(base):
    for folder in ["js", "css", "assets"]:
        (base / folder).mkdir(parents=True, exist_ok=True)

    insert_boilerplate(base)

COMMANDS = {
    "basic": basic_project
}
def insert_boilerplate(directory):
    destiny = directory / 'index.html'
    destiny.write_text(TEMPLATE_HTML_FILE.read_text())

def create_project(directory, template):
    base = Path(directory)

    template_type = COMMANDS.get(template)

    if template_type:
        template_type(base)
    else:
        return

    (base / 'README.md').touch()

