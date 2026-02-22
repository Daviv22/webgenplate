from pathlib import Path

BOILERPLATE_HTML_FILE = Path(__file__).parent / "boilerplates" / "html_boilerplate.txt"

def basic_project(base):
    for folder in ["js", "css", "assets"]:
        (base / folder).mkdir(parents=True, exist_ok=True)

    insert_boilerplate(base)

COMMANDS = {
    "basic": basic_project
}
def insert_boilerplate(directory):
    destiny = directory / 'index.html'
    destiny.write_text(BOILERPLATE_HTML_FILE.read_text())

def create_project(directory, template):
    base = Path(directory)

    template_type = COMMANDS.get(template)

    template_type(base)

    (base / 'README.md').touch()

