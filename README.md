# Desafio API Django (SampleMed)

Aplicação Django 4.x containerizada para consumo da API [JSONPlaceholder](https://jsonplaceholder.typicode.com/). 🎯

Este projeto é uma aplicação Django que consome a API pública JSONPlaceholder (endpoint `/posts`), armazena os dados em um banco de dados PostgreSQL 15 e os exibe no Django Admin.

O projeto utiliza Docker e Docker Compose para criar um ambiente de desenvolvimento 100% reproduzível.

---

## Tabela de Conteúdos

- [Pré-requisitos](#pré-requisitos)
- [Como Rodar (Docker)](#como-rodar-docker-recomendado)
- [Comandos Úteis](#comandos-úteis)
- [Troubleshooting (Solução de Problemas)](#troubleshooting-solução-de-problemas)

---

## Pré-requisitos

- Git
- Docker (recomendado para desenvolvimento e execução)
- Docker Compose (geralmente incluído no Docker Desktop)

---

## Como Rodar (Docker Recomendado)

Este projeto é configurado para rodar inteiramente com Docker Compose. O arquivo `docker-compose.yml` gerencia a aplicação e o banco de dados.

**1. Clone o Repositório**
```bash
git clone [URL-DO-SEU-REPOSITORIO]
cd [NOME-DA-PASTA-DO-PROJETO]

**2. Suba os Containers**
 O Docker Compose fará todo o trabalho: construir a imagem do Django, iniciar o banco de dados Postgres (com as credenciais definidas no docker-compose.yml) e aplicar as migrações automaticamente.
```bash
docker compose up --build

Comandos Úteis**
Execute todos os comandos de gerenciamento do Django (como createsuperuser) usando docker compose exec
```bash
docker compose exec web python manage.py createsuperuser

**Popular o Banco com Posts da API**
Comando utilizado para buscar os dados no JSONPlaceholder
```bash
docker compose exec web python manage.py fetch_posts

**Troubleshooting**
Não consigo conectar ao http://127.0.0.1:8000/admin/

Verifique se os containers estão rodando com docker ps.

Verifique os logs do Gunicorn no terminal do docker compose up.

Verifique se a linha ALLOWED_HOSTS no config/settings.py inclui '127.0.0.1' e 'localhost'.

Não consigo logar no /admin/

O banco de dados do Docker é novo e está vazio. Você precisa criar um novo super-usuário.

Rode: docker compose exec web python manage.py createsuperuser