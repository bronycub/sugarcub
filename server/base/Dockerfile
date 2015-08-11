FROM debian:jessie
MAINTAINER matthias.devlamynck@mailoo.org

ENV DEPLOY_TYPE=prod

RUN apt-get update                           \
	&& apt-get install -y apt-utils locales  \
	&& apt-get upgrade -y                    \
	&& mkdir /shared

RUN echo 'C.UTF-8' >> /etc/default/locale
