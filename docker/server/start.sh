#!/bin/sh

cd /code

if [ ! -e /code/db.sqlite3 ]; then
	python manage.py migrate
	python manage.py loaddata fixtures/*.yaml
	rm -f /firstrun.tag
fi

echo "Starting gulp watch task"
echo "Starting Django server on *:8000"
python manage.py runserver 0.0.0.0:8000 & gulp watch
