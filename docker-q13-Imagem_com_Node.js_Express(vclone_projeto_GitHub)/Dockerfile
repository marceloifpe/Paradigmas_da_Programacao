# 13/Dockerfile
# Use uma imagem oficial do Node.js.
FROM node:18-alpine

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Clone diretamente do GitHub esse projeto.
# Usamos `git` para clonar o repositório. O `apk add git` instala o git no Alpine.
RUN apk add --no-cache git && \
    git clone https://github.com/eMahtab/node-express-hello-world .

# Instale as dependências com o comando npm install.
RUN npm install

# A porta 3000 deve ser exposta via EXPOSE.
EXPOSE 3000

# Use CMD para rodar o comando npm start (que inicia o servidor).
CMD ["npm", "start"]