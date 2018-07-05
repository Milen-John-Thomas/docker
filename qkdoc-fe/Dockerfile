FROM alpine:3.7

RUN apk --no-cache update && \
        apk add python \
        py-pip \
	python-dev \
	bash \
	openrc \
	gcc \
	py-setuptools  \
	musl-dev \
	py-mysqldb
 
RUN pip install --upgrade pip
RUN pip install supervisor 
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && apk update && \
        apk add nginx && \
        rm -rf /var/cache/apk/*

RUN mkdir -p /opt/scripts/conf/
RUN mkdir -p /opt/requirements/
ADD docker-deps/env_conf.txt /opt/scripts/conf/env_conf.txt
ADD docker-deps/requirements.txt /opt/requirements/
RUN pip install -r /opt/requirements/requirements.txt

RUN rm -f /etc/nginx/conf.d/default.conf
ADD docker-deps/nginx/nginx.conf /etc/nginx/nginx.conf
ADD docker-deps/nginx/qkdoc_fe.conf /etc/nginx/conf.d/qkdoc_fe.conf
ADD docker-deps/supervisord.conf /etc/supervisor/supervisord.conf

COPY startup.sh /opt/startup.sh
RUN chmod 755 /opt/startup.sh
ADD mm-qkdocmma /var/www/

EXPOSE 80 8000


CMD ["/usr/bin/supervisord"]
ENTRYPOINT ["/opt/startup.sh"]
