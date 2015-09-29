#!/usr/bin/env bash

trap '/shared/mailman/bin/mailman stop ; exit $?' TERM

rm /shared/mailman/var/locks/*
cd /shared/mailman
/shared/mailman/bin/mailman start &

/uwsgi-build/uwsgi /shared/uwsgi-mailman.ini
