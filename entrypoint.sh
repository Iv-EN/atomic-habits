#!/bin/bash

set -x

python manage.py migrate --noinput &&\
python manage.py collectstatic --noinput &&\
cp -r collected_static/. /static/

exec "$@"