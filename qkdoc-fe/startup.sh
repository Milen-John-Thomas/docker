#!/bin/bash

cd /var/www/mm-qk-doc-fe && source  /opt/scripts/conf/env_conf.txt && echo "starting the Qk-Doc FE" && /usr/bin/gunicorn --name Qk-Doc-FE --bind 0.0.0.0:8000 Qkdoc_patient.wsgi:application --worker-class eventlet --workers 4 --worker-connections 50 --error-logfile /var/log/nginx/qkdoc_error.log --access-logfile /var/log/nginx/qkdoc_access.log --pid /var/run/gunicorn.pid

/usr/sbin/nginx
