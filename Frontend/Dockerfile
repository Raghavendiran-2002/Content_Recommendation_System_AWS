# Stage 1
FROM node:14 as build-stage

COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Stage 2
FROM nginx:1.17.0-alpine

COPY --from=build-stage /build /usr/share/nginx/html
EXPOSE 8081

CMD nginx -g 'daemon off;'