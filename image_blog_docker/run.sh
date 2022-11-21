#!/bin/sh

aws s3 --profile XXXXX cp s3://XXXXX/image_blog build/image_blog/
aws s3 --profile XXXXX cp s3://XXXXX/blog.sql dump/

export mysql_user='xxxx'
export mysql_pass='xxxx'
export s3_bucket='xxxx'
export aws_region='xxxx'
export AWS_ACCESS_KEY_ID='xxxxx'
export AWS_SECRET_ACCESS_KEY='xxxxxxxxxxxxxx'
export DOCKER_DEFAULT_PLATFORM=linux/amd64


cp build/image_blog/image_blog .

docker-compose up -d --build
