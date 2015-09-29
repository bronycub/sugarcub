FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y                \
		postfix                                                      \
	&& ln -sf /shared/maildirs /home                                 \
	&& ln -sf /shared/main.cf /etc/postfix/main.cf                   \
	&& cp /etc/services /var/spool/postfix/etc/services              \
	&& cp /etc/resolv.conf /var/spool/postfix/etc/resolv.conf

EXPOSE 25

RUN echo 'sugarcub.org' > /etc/hostname

ENTRYPOINT /shared/postfix.sh
