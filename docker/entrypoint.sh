#!/bin/bash

set -e

python manage.py migrate

if [ -f modules/fixtures/modules.json ]; then
  python manage.py loaddata modules/fixtures/modules.json
fi

exec python manage.py runserver 0.0.0.0:8000