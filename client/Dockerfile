FROM node:18

WORKDIR /user/src/app

COPY package.json .
COPY node_modules .
RUN yarn install
COPY . .

EXPOSE 3000
CMD ["yarn", "start"]