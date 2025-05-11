#!/bin/bash

set -x

python manage.py migrate --noinput || exit 1

exec "$@"