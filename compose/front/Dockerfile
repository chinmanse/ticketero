FROM node:18.12

WORKDIR /app
RUN mkdir /app/.next
RUN mkdir /app/node_modules

COPY ./compose/front/package.json /app/package.json
# COPY ./frontend/package.json /app/package.json
# COPY ./frontend/yarn.lock /app/yarn.lock
# COPY ./frontend/next.config.js /app/next.config.js

RUN npm install
# RUN npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

# RUN npm run build

RUN ls ./.next
RUN ls ./node_modules

EXPOSE 3000

# CMD ["npm", "run", "dev"]
CMD npm run start
# CMD ["npm", "run", "dev", "--", "--poll 1000"]
# CMD ["npm", "run", "dev:watch"]