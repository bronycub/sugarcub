#!/usr/bin/env bash
set -x

if [ $# -ge 1 ] ; then
	COMMIT_ID="$1"
else
	echo 'No commit id was given, nothing to deploy'
	exit 1
fi

if [ -L $0 ] ; then
    DIR=$(dirname $(readlink -f $0))
else
    DIR=$(dirname $0)
fi

cd "$DIR"

docker-compose -p sugarcub build
systemctl reload sugarcub
