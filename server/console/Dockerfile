FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y     \
		git                \
		xvfb               \
		iceweasel          \
		iceweasel-l10n-fr  \
	&& mkdir -p /var/www   \
	&& chown 33 /var/www

ENV LANG=fr

WORKDIR /shared

USER 33

ENTRYPOINT ["/bin/bash"]
