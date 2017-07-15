#!/bin/sh

cd /code

if [ ! -e /code/db.sqlite3 ]; then
	echo "Installing dev database"
	python manage.py migrate
	python manage.py loaddata fixtures/*.yaml
	rm -f /firstrun.tag
fi

if [ ! -e /code/node_modules ]; then
	echo "Installing node (gulp) dependancies"
	npm install
fi

echo "Starting gulp watch task"
echo "Starting Django server on *:8000"
python manage.py runserver 0.0.0.0:8000 & gulp watch
