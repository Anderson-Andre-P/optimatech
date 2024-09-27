# Dockerfile
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API
COPY API/ ./API

# Copia o arquivo .env
COPY .env .

# Comando para rodar a aplicação
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
