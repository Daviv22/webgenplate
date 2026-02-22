import argparse
from .generator import create_project

def main():
    parser = argparse.ArgumentParser(
        description="Script para automatização de projetos"
    )

    parser.add_argument(
        'directory_name',
        type=str,
        help='Nome do diretório onde o projeto será criado'
    )

    parser.add_argument(
        '--template',
        type=str,
        choices=['basic'],
        default='basic',
        help='Template do projeto'
    )
    args = parser.parse_args()

    create_project(args.directory_name, args.template)