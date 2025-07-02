FROM python:3.12.6-alpine

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia os arquivos da aplicação para o contêiner.
COPY app.py .

# Instala a biblioteca Flask.
RUN pip install Flask

# A porta 5000 deve ser exposta no Dockerfile.
EXPOSE 5000

# O comando padrão para rodar a aplicação Flask.
# rodar na porta 5000
CMD ["python", "app.py"]