#!/bin/bash

set -x

python manage.py migrate --noinput || exit 1
python manage.py collectstatic --noinput || exit 1
cp -r /app/collected_static/. /static/ || exit 1

exec "$@"