# API Central de erros - Projeto final aceleradev python 2020

Projeto final do aceleradev python da [Codenation](https://www.codenation.dev/) em parceria com a [Stone Payments](https://www.stone.com.br/).

![Banner](assets/Banner.jpg)

## Overview

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

## :pushpin: Getting Started

### :key: Requirements

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)

### :minidisc: Installation

```bash
# clonando o repositório
git clone https://github.com/foschieraanderson/central-de-erros.git
```

## :hammer_and_wrench: Setup

- Gere uma secret_key para o seu projeto através do seu terminal
  
  ```bash
  # gerando SECRET_KEY
    $ python -c "import secrets; print(secrets.token_urlsafe())"
  ```
- Entrando no diretório do projeto edite o arquivo **docker-compose.yml**
  
  ```bash
  # Entrando no diretório
    $ cd central-de-erros/

  # Editando o arquivo docker-compose.yml

    # Cole a sua secret_key gerado aqui
    - SECRET_KEY=YOUR_SECRET_KEY
    # Configure os credencias do banco de dados
    - POSTGRES_NAME=DB_NAME
    - POSTGRES_USER=DB_USER
    - POSTGRES_PASSWORD=DB_PASSWORD

  ```

- Rodando o projeto
  ```bash
  # Execute o seguinte comando no seu terminal

  $ docker-compose up -d 

## :camera: Screenshot

![Central de Erros](assets/API-Central-de-Erros.jpg)

## :desktop_computer: Technologies

* [Docker](https://www.docker.com)
* [Python](https://www.python.org)
* [Django](https://www.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org)
* [JWT - Json Web Token](https://jwt.io)
* [Pytest](https://docs.pytest.org/en/stable)
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.5)
* [Swagger](https://swagger.io)
* [Whitenoise](http://whitenoise.evans.io/en/stable)
* [Gunicorn](https://gunicorn.org)

## :page_with_curl: Licence
This project is under the MIT license. See the [LICENSE](./LICENSE) for more information.

---

<h4 align="center"> <em>&lt;/&gt;</em> <a href="https://github.com/foschieraanderson" target="_blank">foschieraanderson</a> </h4>