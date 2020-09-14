FROM python:3.7-buster

RUN \
  echo "deb https://deb.nodesource.com/node_14.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs jq && \
  pip3 install -U pip setuptools  && \
  npm i -g npm@^6 && \
  rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . .
RUN npm i

CMD ["/bin/sh", "-c", "./node_modules/.bin/serverless deploy -s $STAGE -r $AWS_REGION"]
#CMD ["/bin/bash"]
