install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

reset:
	python manage.py reset

shell:
	python manage.py shell

test:
	python manage.py test
