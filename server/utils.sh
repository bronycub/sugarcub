#!/usr/bin/env bash

# Fail on unset vars
set -o nounset
set -o errexit

# ---- Return Codes ----

# Global
MISSING_PARAMETER_ERROR=0
SYSTEM_NOT_BUILT=1

# Instance
INSTANCE_DOESNT_EXIST=2
INSTANCE_ALREADY_EXISTS=3

# Build
BUILD_ERROR=4
BUILD_GIT_CLONE_ERROR=5

# Deploy
DEPLOY_GIT_UPDATE_ERROR=6
DEPLOY_FIRST_INSTALL_ERROR=7
DEPLOY_LAST_COMMIT_SETUP_ERROR=8

# Services
SERVICES_START_ERROR=9

# ---- Configuration ----

MASTER_GIT_URL="http://gitlab.com/mdevlamynck/sugarcub.git"

# ---- Utils ----

function die()
{
	echo "FAILED: $2" >&2
	exit $1
}
