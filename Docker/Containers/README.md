# Les conteneurs

- **Créer un conteneur :**
```
root@docker:~# docker  run -ti debian
-i : interagir avec le conteneur
-t : garder le même terminal ouvert
--name : nom du conteneur
--rm : Supprime le conteneur après l’avoir quitter
```

- **Visualiser les conteneurs :**
```
root@docker:~# docker ps -a
-a : afficher tous les conteneurs
```

- **Raccourcis pour quitter un conteneur sans le détruire :**
```
Ctrl + P + Q
```

- **Exécuter une commande dans un conteneur :**
```
root@docker:~# docker exec <conteneurID>  /bin/bash -c 'ls /var/www/html'
```

- **Astuce pour se connecter en permanence sur le terminal d'un conteneur:**
```
root@docker:~# docker exec -ti <conteneurID>  /bin/bash 
```

- **Retourner à un conteneur déjà crée :**
```
root@docker:~# docker attach <conteneurID> 
```

- **Stopper et supprimer un conteneur :**
```
root@docker:~# docker stop <conteneurID> 
root@docker:~# docker rm <conteneurID> 
```

- **Démarrer un conteneur (de 0) qui a été stop :**
```
root@docker:~# docker start <conteneurID> 
```

- **Mettre en pause et récupérer un conteneur :**
```
root@docker:~# docker pause <conteneurID> 
root@docker:~# docker unpause <conteneurID> 
```

- **Commiter un conteneur (passer d’un conteneur à une image docker) :**
```
root@docker:~# docker commit <conteneurID> <imageNAME>
```

# Les Mappages:

### Les ports

- **Mapper le port 80 du conteneur en port 8080 :**
```
root@docker:~# docker run --name apache_kinos -d -p 8080:80 httpd
-d : Exécute le conteneur en arrière-plan et imprimer l'ID du conteneur
```

### Les volumes

Les données dans les containeurs sont éphémères, une des solutions serait de mapper un dossier(volume) d’un conteneur vers un dossier(volume) de notre machine local (voir un SAN)
```
root@docker:~# docker run -d --name < conteneurNAME > -p 8080:80 -v ~/data/:/usr/share/nginx/html/ nginx
```
Sur mon dossier en local /data j’ai un fichier index.html et chaque changement de ce fichier affectera les containeurs qui map ce volume.



## Les links :
Permet de lier plusieurs conteneurs entre eux, ici par exemple le linkage entre wordpress + mysql.

- **Création du conteneur mysql :**
```
root@docker:~# docker run --name db -d -e MYSQL_ROOT_PASSWORD=password -d mysql
```

- **Création du conteneur wordpress + linkage :**
```
root@docker:~# docker run --name <conteneurNAME> --link db db -p 8080:80 -d wordpress
--link : Ajouter un lien à un autre conteneur
```
