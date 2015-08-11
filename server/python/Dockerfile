FROM sugarcub-base
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y     \
		gettext            \
		pandoc             \
		build-essential    \
		python3            \
		python3-dev        \
		python3-pip        \
		libevent-dev       \
		python-virtualenv  \
		sqlite

ENV  PIP_DOWNLOAD_CACHE=/shared/.pip
