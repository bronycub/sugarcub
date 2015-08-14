FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y        \
		dovecot-common                                       \
	&& ln -sf /shared/maildirs /home                         \ 
	&& ln -sf /shared/dovecot.conf /etc/dovecot/dovecot.conf

EXPOSE 143

ENTRYPOINT dovecot -F
