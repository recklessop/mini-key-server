#!/usr/bin/env bash

export FLASK_APP="keyserver.py"

# initialise db
python -m flask initdb > /dev/null 2>&1
# add user
python -m flask create-user "$1" "$2" > /dev/null 2>&1

# start app
python keyserver.py
