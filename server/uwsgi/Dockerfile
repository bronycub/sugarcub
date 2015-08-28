FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

WORKDIR /

RUN apt-get install -y wget                                              \
	&& wget http://projects.unbit.it/downloads/uwsgi-2.0.11.1.tar.gz     \
	&& tar -xf uwsgi-2.0.11.1.tar.gz                                     \
	&& mv uwsgi-2.0.11.1 uwsgi-build                                     \
	&& cd uwsgi-build                                                    \
	&& make PROFILE=nolang                                               \
	&& PYTHON=python3.4 ./uwsgi --build-plugin "plugins/python python34" \
	&& PYTHON=python2.7 ./uwsgi --build-plugin "plugins/python python27"

WORKDIR /uwsgi-build

CMD ./uwsgi --emperor '/shared/*/uwsgi.ini' --uid 33
