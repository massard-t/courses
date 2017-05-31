- [English](#English)
- [French](#French)

# English

## My first container

Beware, there will be a bit of code !

### The app

You'll need to do a very basic REST API (choose your own language,
but I highly suggest python with Flask, as it is quite easy to do)
allowing you to hit the following [routes](#routes).

### The database

Chose your favourite SQL database, and create the following [tables](#tables).
You'll have to create a custom user for the DB access.

### Containers

You'll have to do 2 containers, one for the API, linked to the DB.
The DB shouldn't have any exposed ports on localhost.
The API *has* to be accessible from port 6500 on localhost.

### How to send your work

Make a pull request, code your project, I highly suggest doing a deploy script (bash, python, ruby, ansible...) or Makefile.
Your Dockerfile(s) have to be the lightest possible.

You should look up best practices, the cleaner your code, and Dockerfile, the more you'll learn about this wonderful tool.

### Possible bonuses

- Configuration based on environment variable at run
- More routes
- A proxy
- Whatever you want that is related to this project, really.

# French

## Mon premier container

Attention, il y aura un peu de code à rédiger!

### L'application

Vous allez devoir faire une API REST tres simple, le langage est libre,
mais je suggere fortement d'utiliser du python, avec le framework Flask.
Le but est de mettre en place les [routes](#routes) decrites plus bas.

### La Base de donnee

Choisissez votre DB SQL preferee, et mettre en place les [tables](#tables) suivantes.
Pensez a ajouter un user custom pour l'acces a la DB.

### Les conteneurs

Vous allez devoir deployer 2 conteneurs. Le premier, pour la DB, et un autre, pour l'API, lie a la DB.
La DB ne doit pas exposer de ports sur l'host.
L'API *doit* etre accessible depuis le port 6500 sur l'host.

### Le rendu

Faites un fork, codez votre projet, puis faites une pull request sur le depot original.
Je vous suggere de faire un script de deploiement (en bash, python, ruby, via ansible) ou un Makefile.
Votre, ou vos Dockerfile(s), devront etre le plus leger possible.

Regardez et cherchez les best practices de Docker. Plus vous gratterez, meilleure sera votre maitrise de ce magnifique outil.

### Bonus potentiels

- Configuration basee sur des variables d'environement a configurer au run
- Plus de routes
- Un proxy
- Tout ce qui vous semble interessant a ajouter au projet.


## Examples

### routes
```bash
$ curl http://localhost:6500/users
[{'name': 'Mark', 'job': 'Developper'}, {'name': 'Peter', 'job': 'HR'}, {'name': 'Boris', 'job': 'CEO'}]
```

```bash
$ curl http://localhost:6500/jobs
[{'id': 1, 'title': 'Developper'}, {'id': 2, 'title': 'CTO'}, ...]
```

```bash
$ curl -XPOST http://localhost:6500/jobs -d "{'title': 'DevOps'}"
{'message': 'ok'}
```

```bash
$ curl -XDELETE http://localhost:6500/jobs -d "{'title': 'Front end'}" | grep -i status
Status: 204
```

### tables

tablename | content
------|------
jobs | job's id, job title
users | user's name, and his job's id

