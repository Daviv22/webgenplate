from pathlib import Path

def insert_boilerplate(directory):
    with open('boilerplate_html.txt', 'r') as origin:
        with open(f'{directory}/index.html', 'a') as destiny:
            for line in origin:
                destiny.write(line)

def create_project():
    path = Path('teste')

    (path / 'js').mkdir(parents=True, exist_ok=True)
    (path / 'assets').mkdir(parents=True, exist_ok=True)
    (path / 'css').mkdir(parents=True, exist_ok=True)
    (path / 'README.md').touch()

    arquivo = (path / 'index.html')
    arquivo.touch()
    insert_boilerplate(path)

create_project()
