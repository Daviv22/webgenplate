# webgenplate

CLI tool para geração de templates de projetos web simples. Com um único comando, o **webgenplate** cria a estrutura de pastas e arquivos necessários para começar um projeto front-end do zero.

## Estrutura gerada

Ao criar um projeto, a seguinte estrutura é gerada automaticamente:

```
meu-projeto/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── assets/
└── README.md
```

O `index.html` já vem com um boilerplate HTML5 básico, com os links para o CSS e o script JS configurados.

## Instalação

Requer Python 3.10 ou superior.

Clone o repositório e instale o pacote com `pip`:

```bash
git clone https://github.com/seu-usuario/webgenplate.git
cd webgenplate
pip install .
```

## Uso

```bash
webgenplate <nome-do-diretório> [--template TEMPLATE]
```

### Argumentos

| Argumento | Descrição |
|---|---|
| `nome-do-diretório` | Nome da pasta onde o projeto será criado |
| `--template` | Template a ser usado (padrão: `basic`) |

### Exemplo

```bash
webgenplate meu-projeto
```

Isso criará a pasta `meu-projeto/` no diretório atual com toda a estrutura do template básico.

## Templates disponíveis

| Template | Descrição |
|---|---|
| `basic` | Estrutura HTML/CSS/JS com boilerplate HTML5 |

## Desenvolvimento

Para instalar em modo editável:

```bash
pip install -e .
```

## Autor

Davi Vitorino