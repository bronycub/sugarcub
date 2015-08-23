#!/usr/bin/env bash

cd $(dirname $0)
source utils.sh

# ---- Configuration ----

BASE_FOLDER="$(pwd)"
DEV_FOLDER="$BASE_FOLDER/.."
if [[ -d $DEV_FOLDER/.git ]]
then
	SHARED_FOLDER="$BASE_FOLDER/../../shared"
else
	SHARED_FOLDER="$BASE_FOLDER/shared"
fi

# ---- Global vars ----

GIT_PATH="$SHARED_FOLDER/sugarcub"

# ---- Utils ----

function run_container()
{
	docker run -v "$SHARED_FOLDER:/shared" -i --rm sugarcub-console -c "./container-subfunctions.sh $*" || exit $?
}

# ---- Build ----

BUILD_DIR="/tmp/docker"

function build_image()
{
	IMG=$1
	if [[ -d $BUILD_DIR ]]
	then
		rm -r $BUILD_DIR
	fi

	mkdir -p $BUILD_DIR                                         \
	&& cp $IMG/* /tmp/docker                                    \
	&& docker build --force-rm --rm -t sugarcub-$IMG $BUILD_DIR \
	&& rm -r $BUILD_DIR
}

function clean_images()
{
	docker rmi $(docker images | grep '<none>' | sed -e 's/ \+/ /g' | cut -d ' ' -f 3) || true
}

function finalyse_setup()
{
	run_container "finalyse_setup"
}

# ---- Deploy ----

function update_main_repo()
{
	run_container "update_main_repo"
}

# ---- Services ----

SERVICES="redis uwsgi postfix mailman nginx"

function services_start()
{
	for i in $SERVICES
	do
		PORT_MAPPING=""
		case $i in
			nginx)
				PORT_MAPPING="-p 80:80 -p 443:443"
				;;
			postfix)
				PORT_MAPPING="-p 25:25"
				;;
		esac

		docker run $PORT_MAPPING -v "$SHARED_FOLDER:/shared" -d --name sugarcub-$i sugarcub-$i || die $SERVICES_START_ERROR "can't start service $i"
	done
}

function services_stop()
{
	for i in $SERVICES
	do
		docker rm -f sugarcub-$i || echo "can't stop service $i" >&2
	done
}

function services_restart()
{
	services_stop
	services_start
}

# ---- Main commands ----

function build_setup()
{
	echo "Building setup"

	# "postgresql" "celery" "dev"
	for i in "base" "nginx" "redis" "python" "console" "uwsgi" "postfix" "mailman"
	do
		build_image "$i" || die $BUILD_ERROR "can't build image $i"
	done

	mkdir -p "$SHARED_FOLDER" \
	&& chmod a+rwx $SHARED_FOLDER \
	&& cp manage-deploy.sh uwsgi-template.ini nginx-template.conf redis.conf container-subfunctions.sh utils.sh postfix.sh mailman.sh main.cf settings_local.py uwsgi-mailman.ini nginx-mailman.conf "$SHARED_FOLDER" \
	&& finalyse_setup \
	|| die $BUILD_ERROR "can't setup shared folder"

	[[ $# -ge 1 && $1 == '-f' ]] && services_restart
	docker rm -f sugarcub-dev || true

	clean_images
}

function create_instance()
{
	[[ $# -ge 2 ]] || display_help

	run_container "create_instance" "$@"
	docker kill -s HUP sugarcub-nginx || true
}

function deploy_instance()
{
	[[ $# -ge 1 ]] || display_help

	run_container "deploy" "$@"
}

#function list_deploys()
#{
#}
#
#function rollback_instance()
#{
#}
#
#function manage_config()
#{
#}

function manage_dev()
{
	XSOCK="/tmp/.X11-unix/X0"

	[[ -d $DEV_FOLDER/.git ]] || die $DEV_NOT_DEV_SETUP "You don't seem to be running in a dev environement"
	if [[ $# -ge 1 ]]
	then
		ACTION=$1
		shift
		SERVICES="redis"

		case $ACTION in
			start)
				services_start
				docker run -p 8000:8000 -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -d --name sugarcub-dev sugarcub-console -c "./container-subfunctions.sh start_dev" || die $SERVICES_START_ERROR "can't start service $i"
				;;
			stop)
				docker rm -f sugarcub-dev || true
				services_stop
				;;
			restart)
				docker rm -f sugarcub-dev || true
				services_restart
				docker run -p 8000:8000 -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -d --name sugarcub-dev sugarcub-console -c "./container-subfunctions.sh start_dev" || die $SERVICES_START_ERROR "can't start service $i"
				;;
			test)
				if [[ $# -ge 2 && $2 == '-s' ]]
				then
					shift
					trap 'xhost - ; exit $?' ERR
					xhost +local:
					docker run -v "$XSOCK:$XSOCK" -e DISPLAY=unix$DISPLAY -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -i --rm sugarcub-console -c "./container-subfunctions.sh run_virtualenv LANG=fr py.test $*" || exit $?
					trap - ERR
				else
					docker run -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -i --rm sugarcub-console -c "./container-subfunctions.sh run_virtualenv LANG=fr xvfb-run py.test $*" || exit $?
				fi
				;;
			*)
				docker run -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -it --rm sugarcub-console -c "./container-subfunctions.sh run_virtualenv $ACTION $*" || exit $?
				;;
		esac
	else
		docker run -v "$SHARED_FOLDER:/shared" -v "$DEV_FOLDER:/shared/dev/code" -it --rm sugarcub-console || exit $?
	fi
}

function manage_services()
{
	[[ $# -ge 1 ]] || display_help

	case $1 in
		start)
			services_start
			;;
		stop)
			services_stop
			;;
		restart)
			services_restart
			;;
		*)
			display_help
			;;
	esac
}

#function print_logs()
#{
#}

function display_help()
{
	echo \
"
Usage:
    $0 <b|build> [-f]
    $0 <a|add> <instance> <host>
    $0 <d|deploy> <instance>
    $0 <L|list> [instance]
    $0 <r|rollback> <instance> [deploy]
    $0 <c|config> [instance] [key=value] ...
    $0 <D|dev> [start|stop|restart|test [-s]|wathever command you want]
    $0 <s|services> <start|stop|restart>
    $0 <l|logs> <type> [instance] [-f]

If called without parameters, print this help.

Commands:
    b, build       build and setup the various containers and files needed
                   may be run again to update the setup
                   with -f, replace containers once the updated one are built
                   (this will start the containers even if they weren't running)

    a, add         setup and deploy a new instance with the given parameters :
                   (deploy only once all paramaters are set,
                    see config to set paramaters and deploy to actualy deploy)
                   [host] url the instance will be reachable from
    
    d, deploy      deploy the last commit of sugarcub for the given instance
                   (must exists first, use add to create a new instance)
                   (all parameters must be set, see config)

    L, list        list existing deploys for the given instance or all if none given
                   -c only print the current deploy

    r, rollback    change the current deploy for the given instance to the given deploy
                   or the previous one if none given
    
    c, config      show / change configurations values
                   if [instance] is specified, work on the givent instance settings,
                   else work on global settings
                   if no key=value is given, show the current configuration,
                   else update the given keys with the given values
    
    D, dev         without parameters, open a shell in the container
                   with start, stop or restart, respectively start, stop or restart the dev server
                   with test, run the test suite, with -s, show the browser during functional tests
                   with anything else, run wathever you gave in the container
				   without any paramaters, run a console for you
    
    s, services    respectively start, stop or restart the services
    
    l, logs        print the log file of given service, optionally for given instance
                   with -f, follow the logs instead of printing the whole log 
    
Return codes:
    global:
        $MISSING_PARAMETER_ERROR the given command requires a parameter not provided
        $SYSTEM_NOT_BUILT the build command wasn't called or the setup is broken

    instance:
        $INSTANCE_DOESNT_EXIST the given instance doesn't exist or is empty
		$INSTANCE_ALREADY_EXISTS the given already exist and can't be created

    build:
        $BUILD_ERROR an error occured while building the setup
        $BUILD_GIT_CLONE_ERROR can't clone the master git repo

    add:
        $DEPLOY_FIRST_INSTALL_ERROR can't setup the new instance
        $DEPLOY_LAST_COMMIT_SETUP_ERROR can't setup the last commit

    deploy:
        $DEPLOY_GIT_UPDATE_ERROR can't update the master git repo
        $DEPLOY_LAST_COMMIT_SETUP_ERROR can't setup the last commit

    list:
    rollback:
    config:
    dev:
    services:
        $SERVICES_START_ERROR can't start a service

    logs:
"
	exit 0
}

# ---- Entry point ----

[[ $# -ge 1 ]] && ACTION=$1 || display_help
shift

[[ -n $ACTION ]] || display_help

case $ACTION in
	build|b)
		build_setup "$@"
		;;
	add|a)
		create_instance "$@"
		;;
	deploy|d)
		deploy_instance "$@"
		;;
	list|L)
		list_deploys "$@"
		;;
	rollback|r)
		rollback_instance "$@"
		;;
	config|c)
		manage_config "$@"
		;;
	dev|D)
		manage_dev "$@"
		;;
	services|s)
		manage_services "$@"
		;;
	logs|l)
		print_logs "$@"
		;;
	*)
		display_help
		;;
esac

exit 0
