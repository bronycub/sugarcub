FROM sugarcub-uwsgi
MAINTAINER matthias.devlamynck@mailoo.org

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y postfix

WORKDIR /shared

EXPOSE 8001

ENTRYPOINT /shared/mailman.sh
