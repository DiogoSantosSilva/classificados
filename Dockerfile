# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt /app/

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação para o container
COPY . /app/

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para rodar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
