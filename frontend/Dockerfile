
FROM timbru31/java-node:latest as build

WORKDIR /app

COPY ./ /app/

RUN mkdir /backend/specification

COPY ../backend/specification/openapi.yaml /backend/specification/openapi.yaml

RUN npm install

RUN npm run generate:api

RUN npm run build-prod

FROM nginx:latest

COPY --from=build /app/dist/frontend /usr/share/nginx/html

EXPOSE 80