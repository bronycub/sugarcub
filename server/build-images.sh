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
build_image "nginx"
build_image "redis"
#build_image "postgresql"
build_image "python"
build_image "console"
build_image "dev"
build_image "uwsgi"
#build_image "celery"

mkdir -p shared/{nginx-sites,logs}
cp manage-deploy.sh shared/
cp uwsgi-template.ini shared/
cp nginx-template.conf shared/
cp redis.conf shared/
