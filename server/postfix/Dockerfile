FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
		postfix        \
	&& ln -sf /shared/postfix-supervisord.conf /etc/supervisord.conf \
	&& ln -sf /shared/main.cf /etc/postfix/main.cf \
	&& pip2 install supervisor supervisor-stdout syslog-stdout

EXPOSE 25

ENTRYPOINT supervisord
