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