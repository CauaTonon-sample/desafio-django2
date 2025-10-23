FROM python:3.11-slim

# 2. Configurações de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Atualiza os pacotes e instala as dependências de build (gcc)
# e as bibliotecas C de desenvolvimento do Postgres (libpq-dev)
RUN apt-get update \
    && apt-get install -y \
       gcc \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Nota: "config.wsgi:application" aponta para o arquivo wsgi.py dentro da pasta config
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]