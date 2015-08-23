FROM sugarcub-base
MAINTAINER matthias.devlamynck@mailoo.org

RUN apt-get install -y \
		nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN rm -r /etc/nginx/sites-enabled \
	&& ln -s -f /shared/nginx-sites /etc/nginx/sites-enabled \
	&& ln -s -f /shared/nginx-ssl /etc/nginx/ssl

EXPOSE 80

ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]
