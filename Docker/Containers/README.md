# Les conteneurs

## Definition

Un conteneur est un processus isolé qui a sa propre vision du système il est construit à partir de namespaces (ce qu'il va voir) et cgroups (ce qu'il va utiliser en terme de ressources)

### Les namespaces :
Les namespaces permettent de créer des groupes de processus isolés du reste de la machine, c'est l'outil de base pour création des containers sous Linux. Ces namespaces permettent un bonne isolation des containers dans Docker.

- **PID :** isolation de l'espace des processus
- **UTS :** pour avoir son propre hostname
- **IPC :** qui permet d'isoler les Communications Inter-Processus
- **NET :** chaque conteneur peut avoir sa propre interface réseau, son ip, ses règles de filtrage
- **MOUNT :** monter un systeme de fichier propre au processus différent du système de fichier de la machine hôte
- **IPC :** isole les coummunications inter processus
- **USER :** mapping des UID/GID entre l'hôte et le conteneur (donne un accés root dans le conteneur sans qu'il soit root sur la machine hôte)
- **CGROUPS :** fonctionnalité du noyau Linux pour limiter, compter et isoler l'utilisation des ressources (processeur, mémoire, utilisation disque, etc.) d'un processus

***Bonus :*** Mon petit script pour collecter les informations sur les namespaces d'un conteneur : https://github.com/Hajdaini/Docker/tree/master/Scripts/Bash/namespace


# Commandes

- **Créer un conteneur :**
```
root@docker:~# docker  run -ti debian
-i : interagir avec le conteneur
-t : interagir avec le conteneur
-d : Lancer le conteneur en background
--name : nom du conteneur
--rm : Supprime automatiquement le conteneur après l’avoir quitté
```

- **Visualiser les conteneurs :**
```
root@docker:~# docker ps -a
-a : afficher tous les conteneurs peu importe leur état
```

- **Raccourcis pour quitter un conteneur sans le détruire (état EXIT) :**
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

- **Voir les sorties/erreurs d'un conteneur (STDOUT d'un terminal de conteneur par exemple)**
```
root@docker:~# docker logs <conteneurID>
-f : suivre en permanence les logs de conteneurs (correspond à tail -f)
-t : affiche date et l'heure de reception
```

# Les Mappages:

## Les ports

- **Mapper le port 80 du conteneur en port 8080 :**
```
root@docker:~# docker run --name apache_kinos -d -p 8080:80 httpd
-d : Exécute le conteneur en arrière-plan et imprimer l'ID du conteneur
```

## Les volumes

Les données dans les containeurs sont éphémères, une des solutions serait de mapper un dossier(volume) d’un conteneur vers un dossier(volume) de notre machine local (voir un SAN)
```
root@docker:~# docker run -d --name < conteneurNAME > -p 8080:80 -v ~/data/:/usr/share/nginx/html/ nginx
```
Sur mon dossier en local /data j’ai un fichier index.html et chaque changement de ce fichier affectera les containeurs qui map ce volume.



## Les links :

Permet de lier plusieurs conteneurs entre eux, ici par exemple on va lier le conteneur mysql avec wordpress

- **Création du conteneur mysql :**
```
root@docker:~# docker run --name db -d -e MYSQL_ROOT_PASSWORD=password -d mysql
```

- **Création du conteneur wordpress + liaison :**
```
root@docker:~# docker run --name <conteneurNAME> --link db db -p 8080:80 -d wordpress
--link : Ajouter un lien à un autre conteneur
```
