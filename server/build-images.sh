#!/usr/bin/env bash

BUILD_DIR="/tmp/docker"

function build_image() {
	IMG=$1
	[[ -d $BUILD_DIR ]] && rm -r $BUILD_DIR
	mkdir -p $BUILD_DIR
	cp $IMG/* /tmp/docker
	docker build --force-rm --rm -t sugarcub-$IMG $BUILD_DIR
	rm -r $BUILD_DIR
}


build_image "base"
build_image "python"
build_image "console"
build_image "gunicorn"
#build_image "celery"
build_image "nginx"
#build_image "postgresql"
#build_image "redis"

mkdir -p shared/nginx-sites
cp manage-deploy.sh shared/
cp nginx-template.conf shared/
