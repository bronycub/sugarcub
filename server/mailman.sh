#!/usr/bin/env bash

trap '/shared/mailman/bin/mailman stop ; exit $?' TERM

rm /shared/mailman/var/locks/*
/shared/mailman/bin/mailman start &

/shared/mailman/bin/mailman-web-django-admin runserver 0.0.0.0:8000
