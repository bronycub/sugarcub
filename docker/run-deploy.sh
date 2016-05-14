#!/usr/bin/env bash
set -x

if [ $# -ge 1 ] ; then
	COMMIT_ID="$1"
else
	echo 'No commit id was given, nothing to deploy'
	exit 1
fi

USER='root'
HOST='195.154.77.200'
BASE_DIR='/var/www/sugarcub'

if [ -L $0 ] ; then
    DIR=$(dirname $(readlink -f $0))
else
    DIR=$(dirname $0)
fi

cd "$DIR"

ssh $USER@$HOST "mkdir -p $BASE_DIR"
scp ./deploy.sh $USER@$HOST:"$BASE_DIR"
scp ../docker-compose.yml ../docker-compose.prod.yml $USER@$HOST:"$BASE_DIR"
ssh $USER@$HOST "chmod u+x $BASE_DIR/deploy.sh"
ssh $USER@$HOST "$BASE_DIR"/deploy.sh "$COMMIT_ID"
