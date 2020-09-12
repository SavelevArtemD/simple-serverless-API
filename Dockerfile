FROM node:14.10

WORKDIR /app
COPY . .
RUN npm i

CMD ["sls", "deploy", "-s", "$STAGE", "-r", "$AWS_REGION"]
