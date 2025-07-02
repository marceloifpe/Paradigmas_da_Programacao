# Use uma imagem oficial do Python.
FROM python:3.12.6-alpine

# Define o diretório de trabalho dentro do contêiner.
# Todos os comandos subsequentes (COPY, RUN, CMD) serão executados a partir deste diretório.
WORKDIR /app

# Copia o script hello.py do seu computador (host) para o diretório /app no contêiner.
COPY hello.py .

# Define o comando padrão que será executado quando o contêiner for iniciado.
# Isso irá rodar o script Python.
CMD ["python", "hello.py"]