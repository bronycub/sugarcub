#!/bin/bash

export HOST_IP=`/sbin/ip route|awk '/default/ { print $3 }'`

python3 ./manage.py compilemessages && \
	python3 ./manage.py collectstatic --noinput && \
	python3 ./manage.py migrate --noinput && \
	uwsgi --ini /srv/app/code/uwsgi.ini
