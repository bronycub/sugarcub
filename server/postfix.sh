#!/usr/bin/env bash

trap 'postfix stop ; exit $?' TERM

postfix start &

/usr/local/bin/syslog-stdout.py
