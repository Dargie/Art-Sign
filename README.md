[![Build Status](https://travis-ci.org/Art-Sign/Art-Sign.svg?branch=master)](https://travis-ci.org/Art-Sign/Art-Sign)

# Art-Sign

Back-end du site Art-Sign, fonctionnant avec Python 3.4 et Django 1.11.


---

Pour lancer le serveur en local :
```
$ python manage.py runserver
```
Pour installer les dépendances :
```
$ pip install -r requirements.txt
```
Pour appliquer les migrations, et créer la base de données :
```
$ python manage.py migrate
```
Pour installer les fixtures, et peupler votre base de données :
```
$ python manage.py loaddata fixtures/*.yaml
```
6 billets et 3 évenements seront alors créés en base.
