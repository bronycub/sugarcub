#!/usr/bin/env bash
set -e

export DEPLOY_TYPE=prod

python3 ./manage.py migrate --noinput ; \
python3 ./manage.py collectstatic --noinput ; \
python3 ./manage.py compilemessages ; \

for i in agenda core users 
do
	cd $i
	python3 ../manage.py compilemessages
	cd -
done

uwsgi '/srv/app/code/uwsgi.ini'
