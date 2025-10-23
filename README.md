# Desafio API Django (SampleMed)

Aplicação Django 4.x containerizada que consome a API JSONPlaceholder e expõe os dados via RESTful API. 🎯

Este projeto utiliza Django REST Framework para expor os dados coletados em endpoints JSON, e é configurado com Docker/Docker Compose e PostgreSQL, seguindo as boas práticas de variáveis de ambiente (.env).

---

## Tabela de Conteúdos

- [Pré-requisitos](#pré-requisitos)
- [Como Rodar (Docker)](#como-rodar-docker-recomendado)
- [Endpoints da API](#endpoints-da-api)
- [Comandos Úteis](#comandos-úteis)
- [Troubleshooting (Solução de Problemas)](#troubleshooting-solução-de-problemas)

---

## Pré-requisitos

- Git
- Docker (recomendado para desenvolvimento e execução)
- Docker Compose (geralmente incluído no Docker Desktop)

---

## Como Rodar (Docker Recomendado)

Este projeto é configurado para rodar inteiramente com Docker Compose, lendo as configurações de um arquivo `.env`.

**1. Clone o Repositório**
```bash
git clone [URL-DO-SEU-REPOSITORIO]
cd [NOME-DA-PASTA-DO-PROJETO]

2. Configure as Variáveis de Ambiente Copie o arquivo de exemplo para criar seu arquivo de configuração local.
```bash
cp .env-sample .env

3. Suba os Containers O Docker Compose fará todo o trabalho: construir a imagem, iniciar o banco de dados e aplicar as migrações.
```bash
docker compose up --build
O servidor estará rodando em http://127.0.0.1:8000/.

---

Endpoints da API
A API RESTful expõe os posts coletados.

Listar todos os Posts: GET /api/posts/

URL: http://127.0.0.1:8000/api/posts/

Detalhar um Post: GET /api/posts/<id>/

Exemplo: http://127.0.0.1:8000/api/posts/1/

---

Comandos Úteis
Execute todos os comandos de gerenciamento do Django usando docker compose exec.

Criar um Super-Usuário (Acessar o /admin/)
```bash
docker compose exec web python manage.py createsuperuser
(Acesse o admin em: https://www.google.com/search?q=http://127.0.0.1:8000/admin/)

Popular o Banco com Posts da API Externa Este é o comando customizado para buscar dados da JSONPlaceholder.
```bash
docker compose exec web python manage.py fetch_posts

---

Troubleshooting (Solução de Problemas)
Não consigo logar no /admin/

O banco de dados do Docker é novo e está vazio. Você precisa criar um novo super-usuário (veja Comandos Úteis).

A lista de "Posts" no Admin ou na API está vazia

O banco está vazio. Você precisa popular os dados da API.

Rode: docker compose exec web python manage.py fetch_posts