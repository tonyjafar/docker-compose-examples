FROM golang:latest

ARG mysql_user
ARG mysql_pass

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y git wget \
    && go get github.com/graphql-go/graphql \
    github.com/go-sql-driver/mysql \
    github.com/op/go-logging \
    github.com/disintegration/imaging \
    github.com/satori/go.uuid \
    golang.org/x/crypto/bcrypt \
    && git clone https://github.com/tonyjafar/Image_blog_go.git \
    && cd Image_blog_go \
    && touch conf.json \
    && echo '{\n\t"username": "user_init",\n\t"password": "pass_init",\n\t"ipaddress": "mysql_con",\n\t"port": "3306",\n\t"database": "image_blog"\n}' >> conf.json \
    && sed -i  "s/\"username\": \"user_init\",/\"username\": \"$mysql_user\",/g" conf.json \
    && sed -i  "s/\"password\": \"pass_init\",/\"password\": \"$mysql_pass\",/g" conf.json \
    && mkdir -p data/thumb && mkdir data/videos \
    && go build \
    && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

EXPOSE 8000
WORKDIR /go/Image_blog_go
CMD [ "./Image_blog_go" ]