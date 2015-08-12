FROM debian:jessie
MAINTAINER matthias.devlamynck@mailoo.org

ENV DEPLOY_TYPE=prod

RUN apt-get update                   \
	&& apt-get install -y apt-utils  \
	&& apt-get upgrade -y            \
	&& mkdir /shared
