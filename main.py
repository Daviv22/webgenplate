from pathlib import Path

def create_project():
    path = Path('.')

    (path / 'js').mkdir(parents=True, exist_ok=True)
    (path / 'assets').mkdir(parents=True, exist_ok=True)
    (path / 'css').mkdir(parents=True, exist_ok=True)
    (path / 'README.md').touch()

    arquivo = (path / 'index.html')
    arquivo.touch()

create_project()
