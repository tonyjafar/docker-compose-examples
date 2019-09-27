FROM golang:latest as builder

ARG mysql_user
ARG mysql_pass

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y git wget \
    && go get github.com/graphql-go/graphql \
    github.com/go-sql-driver/mysql \
    gopkg.in/natefinch/lumberjack.v2 \
    github.com/disintegration/imaging \
    github.com/gofrs/uuid \
    golang.org/x/crypto/bcrypt \
    && git clone https://github.com/tonyjafar/Image_blog_go.git \
    && cd Image_blog_go \
    && touch conf.json \
    && echo '{\n\t"username": "user_init",\n\t"password": "pass_init",\n\t"ipaddress": "mysql_con",\n\t"port": "3306",\n\t"database": "image_blog"\n}' >> conf.json \
    && sed -i  "s/\"username\": \"user_init\",/\"username\": \"$mysql_user\",/g" conf.json \
    && sed -i  "s/\"password\": \"pass_init\",/\"password\": \"$mysql_pass\",/g" conf.json \
    && go build \
    && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

FROM debian:10-slim
EXPOSE 8000
WORKDIR /go/Image_blog_go
COPY --from=builder /go/Image_blog_go/Image_blog_go .
COPY --from=builder /go/Image_blog_go/wait-for-it.sh .
COPY --from=builder /go/Image_blog_go/conf.json .
COPY --from=builder /go/Image_blog_go/templates templates
COPY --from=builder /go/Image_blog_go/static static
CMD [ "./Image_blog_go" ]
