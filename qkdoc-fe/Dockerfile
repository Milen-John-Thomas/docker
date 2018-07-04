FROM alpine:3.7

RUN apk update && \
        apk add python \
        py-pip \
	python-dev \
	bash \
	openrc \
	gcc \
	py-setuptools  \
	nginx \
	musl-dev \
	py-mysqldb 
RUN pip install --upgrade pip
RUN pip install supervisor \
        gunicorn 
#RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && apk update && \
#        apk add nginx && \
#        rm -rf /var/cache/apk/*

RUN mkdir -p /opt/requirements/
ADD docker-deps/requirements.txt /opt/requirements/
RUN pip install -r /opt/requirements/requirements.txt

RUN rm -f /etc/nginx/conf.d/default.conf
ADD docker-deps/nginx/nginx.conf /etc/nginx/nginx.conf
ADD docker-deps/nginx/qkdoc_fe.conf /etc/nginx/conf.d/qkdoc_fe.conf
ADD docker-deps/supervisord.conf /etc/supervisor/supervisord.conf

ADD mm-qkdocmma /var/www/

EXPOSE 80 8000

CMD ["/usr/bin/supervisord"]
