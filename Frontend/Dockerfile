FROM node:alpine
WORKDIR /frontend
COPY package*.json ./
RUN npm install --force
COPY . .
CMD ["npm","start"]