## Steps to start the Stack:

```
# clone the repo
$git clone https://github.com/tonyjafar/docker-compose-examples.git
$cd docker-compose-examples/image_blog_docker
#build and run
$export mysql_user=test && export mysql_pass=test1cd && docker-compose up -d --build
#stop the stack
$docker-compose stop
#start again
$docker-compose start
```
then you can access ther server in browser http://localhost:8000
