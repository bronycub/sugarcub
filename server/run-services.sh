#!/usr/bin/env bash

docker rm -f nginx
docker run -v $(pwd)/shared:/shared -p 80:80 -d --name nginx sugarcub-nginx

docker rm -f uwsgi
docker run -v $(pwd)/shared:/shared -d --name uwsgi sugarcub-uwsgi
