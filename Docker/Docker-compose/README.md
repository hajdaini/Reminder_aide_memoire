# Docker-compose

## Definition

Pour orchestrer nos conteneurs nous allons utiliser un outil fournit par docker : docker compose. Cet outil permet de configurer vos conteneurs via un fichier yml. Ce qui permet d'éviter d'avoir à taper des lignes de commandes très longues, mais aussi un partage plus aisé d'une configuration basée sur plusieurs conteneurs

## Example 1

Je crée un volume nginx-volume
```
[root@docker _data]# docker volume create nginx-volume
```

Je fais en sorte que un volume mon volume pointe vers nginx-volume avec l'utilitaire ***external***
```yaml
version: '3.3'

services:
  web:
    container_name: nginx_test
    image: nginx
    ports:
      - 8000:80
    volumes: 
      - web-site:/usr/share/nginx/html
volumes: 
  web-site:
    external:
      name: nginx-volume
```

```
[root@docker test]# docker volume ls
DRIVER              VOLUME NAME
local               nginx-volume
```

```
[root@docker test]# docker volume inspect nginx-volume
[
    {
        "CreatedAt": "2018-10-21T15:44:41+02:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/nginx-volume/_data",
        "Name": "nginx-volume",
        "Options": {},
        "Scope": "local"
    }
]
```

## Example 2

```yaml
version: '3.3'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
volumes:
    db_data:
  ```

- **version 3.3** : version de docker-compose (La syntaxe évolue entre les versions)

- **services**: Cette partie défini les différents containers qui vont être créés

### db

- **container_name :** le nom du conteneur

- **image :** utilisation de l'image mysql:5.7

- **restart :** la variable restart a pour valeur par défaut ‘no’. Elle accepte également ‘on-failure’, ‘unless-stopped’ et ‘always’. Si vous êtes sur une installation locale je recommande de commenter cette ligne (ou la supprimer) pour éviter que les conteneurs ne démarrent au démarrage de votre PC.

- **volumes :** va créer un volume db_data (on peut faire le voir avec la commande ***docker volume ls*** et avoir plus d'information avec ***docker volume inspect <VOLUME_NAME>***

- **environnement :** ces variables dépendent de l’image utilisée. Ici on utilise celle de MYSQL


### wordpress
- **depends_on :** cette ligne permet d’indiquer à Docker qu’il doit lier le conteneur ‘wordpress’ au conteneur ‘db’

- **environnement :** notez ici surtout le WORDPRESS_DB_HOST qui sert à faire pointer le conteneur wordpress vers le bon conteneur de base de donnée, sur le bon port.


## Run
```
docker-compose up -d
```
