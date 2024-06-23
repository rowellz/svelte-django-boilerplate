FROM node:18.0.0

WORKDIR /my-app

COPY ./frontend/package.json ./

RUN npm install

COPY ./frontend .

EXPOSE 5173

CMD ["npm", "run", "dev"]
