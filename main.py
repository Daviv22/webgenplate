from pathlib import Path

def insert_boilerplate(directory):
    with open('boilerplates/boilerplate_html.txt', 'r') as origin:
        with open(f'{directory}/index.html', 'a') as destiny:
            for line in origin:
                destiny.write(line)

def create_project():
    base = Path('.')

    for folder in ["js", "css", "assets"]:
        (base / folder).mkdir(parents=True, exist_ok=True)

    (base / 'README.md').touch()

    arquivo = (base / 'index.html')
    arquivo.touch()
    insert_boilerplate(base)

create_project()
