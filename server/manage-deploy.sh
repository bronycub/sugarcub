#!/usr/bin/env bash

# ---- Return Codes ----

MISSING_PARAMETER_ERROR=1
FIRST_SETUP_ERROR=2
UPDATE_MAIN_REPO_ERROR=3
INSTALL_LAST_COMMIT_ERROR=4
INSTANCE_DOESNT_EXIST=5
INSTANCE_ALREADY_EXIST=6

# ---- Global Vars ----

FOLDER_NAME=""

# ---- Utils ----

function print_failure()
{
    echo "$1"
    exit $2
}

# ---- General ----

function create_main_repo()
{
    [[ -d /shared/sugarcub ]] || git clone http://gitlab.com/mdevlamynck/sugarcub.git /shared/sugarcub --mirror
}

function update_main_repo()
{
    echo "	Getting last commit ..."

    create_main_repo

    cd /shared/sugarcub
    git fetch --all
    git fetch --tags
}

# ---- Per instance ----

function install_last_commit()
{
    cd /shared/sugarcub
    FOLDER_NAME="$(date +%Y-%m-%d-%H-%M-%S)-$(git rev-parse --short dev)"
    [[ $FOLDER_NAME == -* || $FOLDER_NAME == *- ]] && (echo "FAIL: can't determine folder name" && return 1)
    [[ -e $FOLDER_NAME ]] && (echo "FAIL: there is already a file named $FOLDER_NAME" && return 1)

    echo "	Installing in $FOLDER_NAME"

    mkdir -p /shared/$INSTANCE/$FOLDER_NAME/{code,static}        \
        && cd /shared/$INSTANCE/$FOLDER_NAME/code                \
        && git clone file:///shared/sugarcub -b dev --depth 1 .  \
        \
        && virtualenv ../env -p python3                          \
        && . ../env/bin/activate                                 \
        && pip install -r dependencies.txt                       \
        \
        && chmod u+x manage.py                                   \
        && ./manage.py migrate --noinput                         \
        && ./manage.py compilemessages                           \
        && ./manage.py collectstatic --noinput                   \
        || (echo 'FAIL: error during commit code setup' && return 1)

    deactivate
}

function first_install_setup()
{
    echo "	Creating new instance $INSTANCE"

    [[ -d /shared/$INSTANCE && $(ls -A -1 | wc -l) -ne 0 ]] && print_failure "FAIL: instance already exists" $INSTANCE_ALREADY_EXISTS

    mkdir -p /shared/$INSTANCE/{logs,media,database}                                     \
        && (tr -cd "[:graph:]" < /dev/urandom | head -c 512 > /shared/$INSTANCE/.secret) \
        && (printf "$HOST" > /shared/$INSTANCE/host)                                     \
		&& cp /shared/nginx-template.conf /shared/nginx-sites/$INSTANCE.conf             \
		&& sed -e "s/INSTANCE/$INSTANCE/g" -i /shared/nginx-sites/$INSTANCE.conf         \
		&& sed -e "s/HOST/$HOST/g" -i /shared/nginx-sites/$INSTANCE.conf                 \
		&& cp /shared/uwsgi-template.ini /shared/$INSTANCE/uwsgi-first-deploy.ini        \
		&& sed -e "s/INSTANCE/$INSTANCE/g" -i /shared/$INSTANCE/uwsgi-first-deploy.ini   \
	|| (echo 'FAIL: setup instance folder and common configuration' && return 1)
}

function validate_deploy()
{
    echo "	Validating $FOLDER_NAME for $INSTANCE"
	cd /shared/$INSTANCE/
	# Atomic symlink change
    ln -s $FOLDER_NAME new-current
	mv -T new-current current
	touch shared/$INSTANCE/uwsgi.ini
}

# ---- Main commands ----

function create_instance()
{
    echo "Deploying $INSTANCE ..."

    first_install_setup || exit $FIRST_SETUP_ERROR
    deploy
	mv /shared/$INSTANCE/uwsgi-first-deploy.ini /shared/$INSTANCE/uwsgi.ini
}

function deploy()
{
    echo "Deploying $INSTANCE ..."
    [[ -d /shared/$INSTANCE && $(ls -A -1 | wc -l) -ne 0 ]] || print_failure "FAIL: $INSTANCE doesn't exist or is empty, make sure you to run add before calling deploy" $INSTANCE_DOESNT_EXIST

    update_main_repo || exit $UPDATE_MAIN_REPO_ERROR

    install_last_commit && validate_deploy || exit $INSTALL_LAST_COMMIT_ERROR
}

function display_help()
{
    echo \
"
Usage:
    $0 [a|add] [instance] [host]
    $0 [d|deploy] [instance]

If called without parameters, print this help.

Commands:
    a, add         setup and deploy a new instance with the given parameters :
                   [host] url the instance will be reachable from

    d, deploy      deploy the last commit of sugarcub for the given instance
                   (must exists first, use add to create a new instance)

Return codes:
    $MISSING_PARAMETER_ERROR the given command requires a parameter not provided
    $FIRST_SETUP_ERROR can't determine folder name (problem with the main repo ?)
    $UPDATE_MAIN_REPO_ERROR can't update the main repo
    $INSTALL_LAST_COMMIT_ERROR the folder for the new commit already exists
    $INSTANCE_DOESNT_EXIST the given instance doesn't exist or is empty
    $INSTANCE_ALREADY_EXIST the given instance already exists
"
exit 0
}

# ---- Entry point ----

ACTION=$1

[[ -n $ACTION ]] || display_help

case $ACTION in
    add|a)
        INSTANCE=$2
        HOST=$3
        [[ -z $INSTANCE ]] && print_failure "missing parameter [instance], see help" $MISSING_PARAMETER_ERROR
        [[ -z $HOST ]] && print_failure "missing parameter [host], see help" $MISSING_PARAMETER_ERROR
        create_instance
        ;;
    deploy|d)
        INSTANCE=$2
        [[ -z $INSTANCE ]] && print_failure "missing parameter [instance], see help" $MISSING_PARAMETER_ERROR
        deploy
        ;;
    *)
        display_help
        ;;
esac

exit 0
