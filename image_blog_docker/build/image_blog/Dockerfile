FROM golang:latest as builder

ARG mysql_user
ARG mysql_pass
ARG s3_bucket
ARG aws_region

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y git wget \
    && git clone https://github.com/tonyjafar/Image_blog_go.git \
    && cd Image_blog_go \
    && touch conf.json \
    && printf '{\n\t"username": "user_init",\n\t"password": "pass_init",\n\t"ipaddress": "mysql_con",\n\t"port": "3306",\n\t"database": "image_blog"\n\t"s3_bucket": "BUCKET_NAME",\n\t"aws_region": "AWS_REGION"\n}' >> conf.json \
    && sed -i  "s/\"username\": \"user_init\",/\"username\": \"$mysql_user\",/g" conf.json \
    && sed -i  "s/\"password\": \"pass_init\",/\"password\": \"$mysql_pass\",/g" conf.json \
    && sed -i "s/\"aws_bucket\": \"BUCKET_NAME\",/\"s3_bucket\": \"$s3_bucket\",/g" conf.json \
    && sed -i "s/\"aws_region\": \"AWS_REGION\",/\"aws_region\": \"$aws_region\"/g" conf.json \
    && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

FROM debian:10-slim
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
EXPOSE 8000
WORKDIR /go/Image_blog_go
COPY image_blog .
RUN chmod +x image_blog
COPY --from=builder /go/Image_blog_go/wait-for-it.sh .
COPY --from=builder /go/Image_blog_go/conf.json .
COPY --from=builder /go/Image_blog_go/templates templates
COPY --from=builder /go/Image_blog_go/static static
CMD [ "./image_blog" ]
