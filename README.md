<div align="center">

# Django Wikipedia

[Instalação](#instalação) • [Funcionalidades](#funcionalidades) • [Estrutura do Projeto](#estrutura-do-projeto)

![Python](https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-conteúdo-000000?logo=markdown&logoColor=white)
![Status](https://img.shields.io/badge/status-projeto%20acad%C3%AAmico-yellow)

</div>

---

### Sumário
- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)

# Introdução

**Django Wikipedia** é uma enciclopédia digital construída em **Django**, inspirada na Wikipedia. É o Projeto 1 (Wiki) do curso **CS50W — Web Programming with Python and JavaScript**, de Harvard, onde os artigos são escritos em Markdown e convertidos em HTML para exibição.

# Funcionalidades

- Listagem de todas as entradas (páginas) da enciclopédia;
- Busca por título, com correspondência exata e por substring;
- Visualização de uma entrada, com o conteúdo Markdown convertido em HTML;
- Criação de novas entradas;
- Edição de entradas já existentes;
- Exibição de uma página aleatória da enciclopédia.

# Pré-requisitos

- **Python 3**;
- **pip**, para instalar as dependências.

# Instalação

Clone o repositório e acesse a pasta do projeto (dentro da estrutura de pastas do curso CS50):

```sh
git clone https://github.com/cmarinho-dev/django-wikipedia.git
cd django-wikipedia
```

Instale as dependências:

```sh
pip install -r REQUIREMENTS.txt
```

Aplique as migrações do banco e suba o servidor de desenvolvimento do Django:

```sh
python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` no navegador.

# Estrutura do Projeto

```
wiki/
├── encyclopedia/     # App Django: views, urls, templates e lógica da enciclopédia
├── entries/          # Arquivos Markdown com o conteúdo das entradas
├── wiki/              # Configurações do projeto Django (settings, urls raiz)
├── manage.py          # Utilitário de linha de comando do Django
└── REQUIREMENTS.txt   # Dependências do projeto
```

---

<div align="center">

Projeto do CS50W (Harvard) — Enciclopédia construída com Django.

</div>
