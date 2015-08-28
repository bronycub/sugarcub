FROM sugarcub-base
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y                     \
		gettext                            \
		pandoc                             \
		build-essential                    \
		python3                            \
		python3-dev                        \
		python3-pip                        \
		python-dev                         \
		python-pip                         \
		libevent-dev                       \
		python-virtualenv                  \
		sqlite                             \
        npm                                \
    && npm install -g less                 \
	&& ln -s /usr/bin/nodejs /usr/bin/node \
	&& pip2 install syslog-stdout

ENV  PIP_DOWNLOAD_CACHE=/shared/.pip
