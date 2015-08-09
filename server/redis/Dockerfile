FROM sugarcub-base
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y redis-server

ENTRYPOINT redis-server /shared/redis.conf
