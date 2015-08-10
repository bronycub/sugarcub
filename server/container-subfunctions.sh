#!/usr/bin/env bash

source utils.sh

GIT_PATH="/shared/sugarcub"

# ---- Build ----

function create_main_repo()
{
	[[ -d "$GIT_PATH" ]] || { git clone $MASTER_GIT_URL "$GIT_PATH" --mirror || die $BUILD_GIT_CLONE_ERROR "can't clone the master git repo"; }
}


function set_files_owner()
{
	chmod 33 . -R
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

	trap "rm $FOLDER_NAME -rf; die $DEPLOY_LAST_COMMIT_SETUP_ERROR 'error during commit code setup'" ERR

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
	set_files_owner
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
esac

