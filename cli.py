import argparse
from generator import  create_project

parser = argparse.ArgumentParser(description="Script para automatização de projetos")

parser.add_argument('directory_name', type=str, help='Nome do diretório onde o projeto será criado')

args = parser.parse_args()

create_project(args.directory_name)