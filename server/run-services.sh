#!/usr/bin/env bash

docker rm -f nginx
docker run -v $(pwd)/shared:/shared -p 80:80 -d --name nginx sugarcub-nginx

for i in $(find shared -name 'current')
do
	INSTANCE=$(echo $i | cut -d/ -f2)
	docker rm -f $INSTANCE-gunicorn
	docker run -v $(pwd)/shared:/shared -d -e INSTANCE=$INSTANCE --name $INSTANCE-gunicorn sugarcub-gunicorn
done
