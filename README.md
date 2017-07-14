[![Build Status](https://travis-ci.org/Art-Sign/Art-Sign.svg?branch=master)](https://travis-ci.org/Art-Sign/Art-Sign)

# Art-Sign

Back-end du site Art-Sign, fonctionnant avec Python 3.4 et Django 1.11.

---

## Utilisation

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

## Utilisation de Docker

Un environnement [Docker](https://docs.docker.com/) et [Docker compose](https://docs.docker.com/compose/) est mis en place pour unifier les environnements de développement. Ce système comprends une image ainsi qu'une installation de gulp permettant de compiler Sass.

**Construction de l'image**
```
$ docker-compose build
```
L'installation des dépendances Python s'éfféctuent durant cette étape sur la base du fichier `/docker/server/requirement.txt`. Il fuat actualiser ce fichier et reconstruir l'image des qu'une dépendance est ajoutée.

**Démarrer le container** (serveur local et watch gulp)
```
$ docker-compose up
```

Le premier démarrage effectue les migrations et l'ajout des fixtures si le fichier `db.sqlite3` n'existe pas puis le serveur se démarre sur [http://localhost:8000/](http://localhost:8000/). Toutes les modifications apportés aux fichiers Sass seront automatiquement pris en compte lors de la sauvegarde.

Pour démarrer le container en arrière plan ajoutez le paramètre `-d`.

**Arret du container**
```
$ docker-compose stop
```
Cette commande est utile si le container a été démarré en arrière plan. Si le container est au premier plan, un simple `ctrl`+`C` suffit à l'arrèter.

**Demarrage d'un bash dans le container**
```
$ docker-compose exec server /bin/bash
```

**Affiche les logs du serveur**
```
$ docker-compose logs
```
le paramètre `-f` permet de conserver les logs au premier plan.