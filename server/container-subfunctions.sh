#!/usr/bin/env bash

source utils.sh

GIT_PATH="/shared/sugarcub"
MAILMAN_PATH="/shared/mailman"

# ---- Global ----

function run_virtualenv()
{
	set +o nounset
	. /shared/dev/env/bin/activate

	if [[ $# -gt 0 ]]
	then
		/bin/bash -c "$*"
	else
		/bin/bash
	fi

	deactivate
	set -o nounset
}

# ---- Build ----

function create_main_repo()
{
	[[ -d "$GIT_PATH" ]] || { git clone $MASTER_GIT_URL "$GIT_PATH" --mirror || die $BUILD_GIT_CLONE_ERROR "can't clone the master git repo"; }
}

function create_mailman_repo()
{
	[[ -d "$MAILMAN_PATH" ]] || { git clone $MAILMAN_GIT_URL "$MAILMAN_PATH" || die $BUILD_GIT_CLONE_ERROR "can't clone the mailman git repo"; }
}

function setup_mailman()
{
	create_mailman_repo

	cd "$MAILMAN_PATH"
	[[ -d env ]] && { set -o nounset; return 0; } || true
	set +o nounset
	virtualenv env
	. env/bin/activate

	cp /shared/settings_local.py /shared/mailman/mailman_web/
	tr -cd "[:graph:]" < /dev/urandom | head -c 512 > /shared/mailman/.secret
	sed -e '7s/development/production/' -i /shared/mailman/buildout.cfg
	pip install zc.buildout
	buildout
	cat /shared/mailman.cfg >> /shared/mailman/deployment/mailman.cfg
	./bin/mailman-post-update
	./bin/mailman-web-django-admin collectstatic --noinput

	deactivate
	set -o nounset
}

# ---- Deploy ----

function update_main_repo()
{
	cd "$GIT_PATH"      \
	&& git fetch --all  \
	&& git fetch --tags \
	|| die $DEPLOY_GIT_UPDATE_ERROR "can't update the master git repo"
}

function install_last_commit()
{
	set +o nounset

	cd $GIT_PATH
	FOLDER_NAME="$(date +%Y-%m-%d-%H-%M-%S)-$(git rev-parse --short dev)"
	[[ $FOLDER_NAME == -* || $FOLDER_NAME == *- ]] && die $DEPLOY_LAST_COMMIT_SETUP_ERROR "can't determine folder name"
	[[ -e $FOLDER_NAME ]] && die $DEPLOY_LAST_COMMIT_SETUP_ERROR "there is already a file named $FOLDER_NAME"

	echo "Installing in $FOLDER_NAME"

	trap "rm /shared/$INSTANCE/$FOLDER_NAME -rf; die $DEPLOY_LAST_COMMIT_SETUP_ERROR 'error during commit code setup'" ERR

	mkdir -p /shared/$INSTANCE/$FOLDER_NAME/{code,static}    \
	&& cd /shared/$INSTANCE/$FOLDER_NAME/code                \
	&& git clone file://$GIT_PATH -b dev --depth 1 .         \
	                                                         \
	&& virtualenv ../env -p python3                          \
	&& . ../env/bin/activate                                 \
	&& pip install -r dependencies.txt                       \
	                                                         \
	&& chmod u+x manage.py                                   \
	&& ./manage.py migrate --noinput                         \
	&& ./manage.py compilemessages                           \
	&& ./manage.py collectstatic --noinput

	APPS=$(python3 <<<"from sugarcub import settings; print(','.join(settings.PROJECT_APPS))")
	for i in $(echo $APPS | sed -e 's/,/ /g')
	do
		pushd $i
		[ -d locale ] && ../manage.py compilemessages
		popd
	done

	trap - ERR

	deactivate

	set -o nounset
}

function first_install_setup()
{
	echo "Creating new instance $INSTANCE"
	
	[[ -d /shared/$INSTANCE && $(ls -A -1 | wc -l) -ne 0 ]] && die $INSTANCE_ALREADY_EXISTS "instance already exists"
	
	mkdir -p /shared/$INSTANCE/{logs,media,database}                                 \
	&& (tr -cd "[:graph:]" < /dev/urandom | head -c 512 > /shared/$INSTANCE/.secret) \
	&& (printf "$HOST" > /shared/$INSTANCE/host)                                     \
	&& cp /shared/nginx-template.conf /shared/nginx-sites/$INSTANCE.conf             \
	&& sed -e "s/INSTANCE/$INSTANCE/g" -i /shared/nginx-sites/$INSTANCE.conf         \
	&& sed -e "s/HOST/$HOST/g" -i /shared/nginx-sites/$INSTANCE.conf                 \
	&& cp /shared/uwsgi-template.ini /shared/$INSTANCE/uwsgi-first-deploy.ini        \
	&& sed -e "s/INSTANCE/$INSTANCE/g" -i /shared/$INSTANCE/uwsgi-first-deploy.ini   \
	|| die $DEPLOY_FIRST_INSTALL_ERROR 'setup instance folder and common configuration'
}

function validate_deploy()
{
	echo "Validating $FOLDER_NAME for $INSTANCE"
	cd /shared/$INSTANCE/

	# Atomic symlink change
	ln -s $FOLDER_NAME new-current
	mv -T new-current current

	touch /shared/$INSTANCE/uwsgi.ini || true
}

# ---- Main commands ----

function finalyse_setup()
{
	create_main_repo
	setup_mailman
	mkdir -p /shared/{nginx-{sites,ssl},logs,dev/{static,media}}
	cp /shared/nginx-mailman.conf /shared/nginx-sites
	cd /shared/nginx-ssl
	[[ -f /shared/nginx-ssl/server.crt ]] || openssl req -new -x509 -nodes -out server.crt -keyout server.key
}

function create_instance()
{
	INSTANCE=$1
	HOST=$2
	first_install_setup
	deploy $INSTANCE
	mv /shared/$INSTANCE/uwsgi-first-deploy.ini /shared/$INSTANCE/uwsgi.ini
}

function deploy()
{
	INSTANCE=$1
	[[ -d /shared/$INSTANCE && $(ls -A -1 | wc -l) -ne 0 ]] || die $INSTANCE_DOESNT_EXIST "$INSTANCE doesn't exist or is empty, make sure you to run add before calling deploy"
	
	update_main_repo
	install_last_commit
	validate_deploy
}

function start_dev()
{
	[[ -d "/shared/dev/env" ]] || { virtualenv "/shared/dev/env" -p python3 && run_virtualenv 'pip' 'install' '-r' '/shared/dev/code/dependencies.txt'; }
	
	export DEPLOY_TYPE=dev
	cd /shared/dev/code
	run_virtualenv 'exec' './manage.py' 'runserver' '0.0.0.0:8000'
}

# ---- Entry point ----

ACTION=$1
shift

case $ACTION in
	finalyse_setup)
		finalyse_setup
		;;
	create_instance)
		create_instance "$@"
		;;
	deploy)
		deploy "$@"
		;;
	run_virtualenv)
		export DEPLOY_TYPE=dev
		cd /shared/dev/code
		run_virtualenv "$@"
		;;
	start_dev)
		start_dev "$@"
		;;
esac

exit 0
