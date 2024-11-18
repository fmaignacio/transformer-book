import os
import pathlib

def create_project_structure():
    # Estrutura do projeto
    directories = [
        # Código fonte
        "src/models",
        "src/utils",
        "src/training",

        # Notebooks
        "notebooks/local",
        "notebooks/colab",

        # Dados
        "data/raw",
        "data/processed",
        "data/results",

        # Livro
        "book/content/cap1",
        "book/content/cap2",

        # Testes
        "tests"
    ]

    # Criar diretórios
    for dir_path in directories:
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

    # Arquivos iniciais
    files = {
        # Arquivos Python
        "src/__init__.py": "",
        "src/models/__init__.py": "",
        "src/utils/__init__.py": "",
        "src/training/__init__.py": "",
        "tests/__init__.py": "",

        # Arquivo de requisitos
        "requirements.txt": """numpy>=1.19.2
tensorflow>=2.8.0
matplotlib>=3.3.2
seaborn>=0.11.0
jupyter>=1.0.0
jupyterlab>=3.0.0
jupyter-book>=0.13.1
pandas>=1.1.3
scikit-learn>=0.23.2
""",

        # README
        "README.md": """# Transformer Book

Um guia completo sobre a arquitetura Transformer.

## Estrutura do Projeto
- `src/`: Código fonte
- `notebooks/`: Jupyter notebooks
- `data/`: Dados e resultados
- `book/`: Conteúdo do livro
- `tests/`: Testes unitários
""",

        # .gitignore
        ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtualenv
venv/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# PyCharm
.idea/

# Dados
data/raw/*
data/processed/*
data/results/*

# Mac
.DS_Store

# Book
book/_build/
""",

        # Arquivo inicial do transformer
        "src/models/transformer.py": """import tensorflow as tf

class Transformer(tf.keras.Model):
    def __init__(self):
        super(Transformer, self).__init__()
        # TODO: Implementar

    def call(self, inputs):
        # TODO: Implementar
        pass
""",

        # Arquivo de utilidades
        "src/utils/visualization.py": """import matplotlib.pyplot as plt
import seaborn as sns

def plot_attention(attention_weights):
    plt.figure(figsize=(10, 8))
    sns.heatmap(attention_weights, annot=True)
    plt.show()
""",

        # Arquivo de configuração do Jupyter Book
        "book/_config.yml": """title: Entendendo o Transformer
author: Seu Nome
logo: images/logo.png
execute:
  execute_notebooks: force
""",

        # Índice do livro
        "book/_toc.yml": """format: jb-book
root: intro
parts:
  - caption: Fundamentos
    chapters:
    - file: cap1/index

  - caption: Transformer
    chapters:
    - file: cap2/index
"""
    }

    # Criar arquivos
    for file_path, content in files.items():
        # Garantir que o diretório pai existe
        parent_dir = os.path.dirname(file_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        # Criar arquivo com conteúdo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    create_project_structure()
    print("Estrutura do projeto criada com sucesso!")