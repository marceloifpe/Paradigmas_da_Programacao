# 14/Dockerfile
# Crie uma imagem baseada no ubuntu
FROM ubuntu:latest

# Atualiza os pacotes e instala a linguagem python3 e pip.
# Adicionamos `locales` e configuramos o locale para evitar warnings comuns no Python/Ubuntu.
RUN apt-get update && \
    apt-get install -y python3 python3-pip locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Define o diretório de trabalho.
WORKDIR /app

# Copia o script para o contêiner.
COPY process.py .

# Instala a dependência necessária (por exemplo, pandas se desejar).
# Embora o script acima não use pandas para o "Processing data...",
# instalamos para cumprir a regra de "dependências necessárias".
RUN pip3 install pandas

# O container executa o script process.py.
CMD ["python3", "process.py"]