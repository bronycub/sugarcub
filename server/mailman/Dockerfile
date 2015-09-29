FROM sugarcub-uwsgi
MAINTAINER matthias.devlamynck@mailoo.org

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y postfix

USER 33

WORKDIR /shared

EXPOSE 8001 8024

ENTRYPOINT /shared/mailman.sh
