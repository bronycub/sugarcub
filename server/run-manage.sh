#!/usr/bin/env bash

case $1 in
	add|a)
		;;
	deploy|d)
		;;
	*)
		;;
esac

docker run -v $(pwd)/shared:/shared -i --name console --rm sugarcub-console -c "./manage-deploy.sh $*"
RETURN=$?

case $1 in
	add|a)
		docker kill -s HUP nginx
		exit $RETURN
		;;
	deploy|d)
		exit $RETURN
		;;
	*)
		;;
esac
