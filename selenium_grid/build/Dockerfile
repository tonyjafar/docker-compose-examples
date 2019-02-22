FROM ubuntu:latest
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget ca-certificates default-jdk \
firefox fonts-liberation libappindicator3-1 libxss1 xdg-utils
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb
RUN mkdir -p /opt/selenium
EXPOSE 4444
WORKDIR /opt/selenium
CMD [ "java","-jar", "selenium-server-standalone-3.141.59.jar" ]
