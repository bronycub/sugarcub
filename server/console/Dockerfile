FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y     \
		git                \
	&& mkdir -p /var/www   \
	&& chown 33 /var/www

WORKDIR /shared

USER 33

ENTRYPOINT ["/bin/bash"]
