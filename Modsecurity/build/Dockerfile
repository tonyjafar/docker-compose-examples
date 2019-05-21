FROM debian:latest
ARG apr_ver=1.6.5
ARG apr_util_ver=1.6.1
ARG apache_ver=2.4.38
ARG mod_ver=2.9.3
ARG rule_ver=3.1.0
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget libapr1 libapr1-dev build-essential expat libexpat1-dev libpcre3-dev libssl-dev \
libxml2-dev ca-certificates
RUN mkdir /usr/src/apache && chown `whoami` /usr/src/apache
WORKDIR /usr/src/apache
RUN wget  https://www-eu.apache.org/dist/apr/apr-${apr_ver}.tar.bz2 && tar -xvjf apr-${apr_ver}.tar.bz2
WORKDIR /usr/src/apache/apr-${apr_ver}
RUN ./configure --with-crypto --prefix=/usr/local/apr/ && make && make install
WORKDIR /usr/src/apache
RUN wget  https://www-eu.apache.org/dist/apr/apr-util-${apr_util_ver}.tar.bz2 && tar -xvjf apr-util-${apr_util_ver}.tar.bz2
WORKDIR /usr/src/apache/apr-util-${apr_util_ver}
RUN ./configure --with-crypto --prefix=/usr/local/apr/ --with-apr=/usr/local/apr/ && make && make install
WORKDIR /usr/src/apache
RUN wget  https://www-eu.apache.org/dist/httpd/httpd-${apache_ver}.tar.bz2 && tar -xvjf httpd-${apache_ver}.tar.bz2
WORKDIR /usr/src/apache/httpd-${apache_ver}
RUN ./configure --prefix=/opt/apache-${apache_ver}  --with-apr=/usr/local/apr/bin/apr-1-config \
--with-apr-util=/usr/local/apr/bin/apu-1-config \
--enable-mpms-shared=event \
--enable-mods-shared=all \
--enable-ssl --enable-so \
--enable-nonportable-atomics=yes && make clean && make install && chown -R `whoami` /opt/apache-${apache_ver} \
&& ln -s /opt/apache-${apache_ver} /apache && chown `whoami` --no-dereference /apache
RUN mkdir -p /usr/src/modsecurity && chown `whoami` /usr/src/modsecurity
WORKDIR /usr/src/modsecurity/
RUN wget  https://www.modsecurity.org/tarball/${mod_ver}/modsecurity-${mod_ver}.tar.gz && tar -xvzf modsecurity-${mod_ver}.tar.gz
WORKDIR /usr/src/modsecurity/modsecurity-${mod_ver}
RUN ./configure --with-apxs=/apache/bin/apxs \
--with-apr=/usr/local/apr/bin/apr-1-config \
--with-pcre=/usr/bin/pcre-config && make && make install && chown `whoami` /apache/modules/mod_security2.so
WORKDIR /apache/conf
RUN wget  https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/v${rule_ver}.tar.gz &&  tar xvzf v${rule_ver}.tar.gz
RUN ln -s owasp-modsecurity-crs-${rule_ver} /apache/conf/crs && cp crs/crs-setup.conf.example crs/crs-setup.conf && rm v${rule_ver}.tar.gz
WORKDIR /apache
EXPOSE 80 443
CMD [ "/apache/bin/httpd", "-X" ]
