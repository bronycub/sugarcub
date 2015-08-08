#!/usr/bin/env bash

echo $INSTANCE
. /shared/$INSTANCE/current/env/bin/activate
exec gunicorn -b unix:/shared/$INSTANCE/gunicorn.sock --chdir /shared/$INSTANCE/current/code/ --log-file /shared/$INSTANCE/logs/gunicorn.log sugarcub.wsgi
