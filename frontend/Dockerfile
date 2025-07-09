FROM node:18-alpine
WORKDIR /app
# copy files from build context (fixed path)
COPY ./package.json ./yarn.lock ./
RUN yarn install
COPY . .
CMD ["yarn", "start"]
