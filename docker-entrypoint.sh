#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres"

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

exec "$@"