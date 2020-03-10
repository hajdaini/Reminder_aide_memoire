# Docker Shortcuts

- 1 [Aide et informations](#Aideetinformations)
- 2 [Images](#Images)
- 3 [Dockerfile](#Dockerfile)
- 4 [Conteneurs](#Conteneurs)
  - 4.1 [Communs](#Communs)
  - 4.2 [Debug](#Debug)
- 5 [Docker Compose](#DockerCompose)
- 6 [Volumes](#Volumes)
- 7 [Réseau Docker](#RseauDocker)
- 8 [Docker Machine](#DockerMachine)
  - 8.1 [Les nœuds](#nodes)
  - 8.2 [Les services](#services)
  - 8.3 [Les stacks](#stacks)

##  1. <a name='Aideetinformations'></a>Aide et informations

- Afficher de l'aide

  ```docker
  docker help
  docker <sous-commande> --help
  ```

- Afficher des informations sur l'installation de Docker

  ```docker
  docker --version
  docker version
  docker info
  ```

---

##  2. <a name='Images'></a>Images

- Lister des images Docker

  ```docker
  docker image ls
  # ou
  docker images
  ```

- Supprimer une image Docker

   ```docker
   docker images rmi <IMAGE_ID ou IMAGE_NAME>
       -f ou --force : forcer la suppression
   ```

- Supprimer tous les images Docker

  ```docker
  docker rmi -f $(docker images -q)
  ```

- Rechercher une image depuis le Docker Hub Registry

  ```docker
  docker search ubuntu
      --filter "is-official=true" : Afficher que les images officielles
  ```

- Télécharger une image depuis le Docker hub Registry

  ```docker
  docker pull <IMAGE_NAME>  - prendra par défaut le tag latest
  ```

---

##  3. <a name='Dockerfile'></a>Dockerfile

- **FROM** : Définit l'image de base qui sera utilisée par les instructions suivantes.

- **LABEL** : Ajoute des métadonnées à l'image avec un système de clés-valeurs, permet par exemple d'indiquer à l'utilisateur l'auteur du Dockerfile.

- **ARG** : Variables temporaires qu'on peut utiliser dans un Dockerfile.

- **ENV** : Variables d'environnements utilisables dans votre Dockerfile et conteneur.

- **RUN** : Exécute des commandes Linux ou Windows lors de la création de l'image. Chaque instruction **RUN**  va créer une couche en cache qui sera réutilisée dans le cas de modification ultérieure du Dockerfile.

- **COPY** : Permet de copier des fichiers depuis notre machine locale vers le conteneur Docker.

- **ADD** : Même chose que COPY mais prend en charge des liens ou des archives (si le format est reconnu, alors il sera décompressé à la volée).

- **ENTRYPOINT** : comme son nom l'indique, c'est le point d'entrée de votre conteneur, en d'autres termes, c'est la commande qui sera toujours exécutée au démarrage du conteneur. Il prend la forme de tableau JSON (ex** :  **CMD** ["cmd1","cmd1"]) ou de texte.

- **CMD** : Spécifie les arguments qui seront envoyés au **ENTRYPOINT**, (on peut aussi l'utiliser pour lancer des commandes par défaut lors du démarrage d'un conteneur). Si il est utilisé pour fournir des arguments par défaut pour l'instruction **ENTRYPOINT**, alors les instructions  **CMD** et **ENTRYPOINT** doivent être spécifiées au format de tableau JSON.

- **WORKDIR** : Définit le répertoire de travail qui sera utilisé pour le lancement des commandes  **CMD** et/ou **ENTRYPOINT** et ça sera aussi le dossier courant lors du démarrage du conteneur.

- **EXPOSE** : Expose un port.

- **VOLUMES** : Crée un point de montage qui permettra de persister les données.

- **USER** : Désigne quel est l'utilisateur qui lancera les prochaines instructions **RUN** ,  **CMD** ou **ENTRYPOINT** (par défaut c'est l'utilisateur root).

***Exemple :***


```Dockerfile
# --------------- DÉBUT COUCHE OS -------------------
FROM debian:stable-slim
# --------------- FIN COUCHE OS ---------------------


# MÉTADONNÉES DE L'IMAGE
LABEL version="1.0" maintainer="AJDAINI Hatim <ajdaini.hatim@gmail.com>"


# VARIABLES TEMPORAIRES
ARG APT_FLAGS="-q -y"
ARG DOCUMENTROOT="/var/www/html"



# --------------- DÉBUT COUCHE APACHE ---------------
RUN apt-get update -y && \
    apt-get install ${APT_FLAGS} apache2
# --------------- FIN COUCHE APACHE -----------------



# --------------- DÉBUT COUCHE MYSQL ----------------
RUN apt-get install ${APT_FLAGS} mysql-server

COPY db/articles.sql /
# --------------- FIN COUCHE MYSQL ------------------



# --------------- DÉBUT COUCHE PHP ------------------
RUN apt-get install ${APT_FLAGS} \
    php-mysql \
    php && \
    rm -f ${DOCUMENTROOT}/index.html && \
    apt-get autoclean -y

COPY app ${DOCUMENTROOT}
# --------------- FIN COUCHE PHP --------------------


# OUVERTURE DU PORT HTTP
EXPOSE 443
EXPOSE 80: 8080

# RAJOUT DES SOURCES DANS LE CONTENEUR
VOLUME /local/path:${DOCUMENTROOT}


# RÉPERTOIRE DE TRAVAIL
WORKDIR  ${DOCUMENTROOT}


# DÉMARRAGE DES SERVICES LORS DE L'EXÉCUTION DE L'IMAGE
ENTRYPOINT service mysql start && mysql < /articles.sql && apache2ctl -D FOREGROUND
```



---

##  4. <a name='Conteneurs'></a>Conteneurs

###  4.1. <a name='Communs'></a>Communs

- Exécuter une image Docker

  ```docker
  docker run <CONTAINER_ID ou CONTAINER_NAME>
      -t ou --tty : Allouer un pseudo TTY
      --interactive ou -i : Garder un STDIN ouvert
      --detach ou -d : Exécuter le conteneur en arrière-plan
      --name : Attribuer un nom au conteneur
      --expose: Exposer un port ou une plage de ports
      -p ou --publish : Mapper un port  "<PORT_CIBLE:PORT_SOURCE>"
      --rm : Supprimer automatiquement le conteneur quand on le quitte
  ```

- Lister des conteneurs en état running Docker :

  ```docker
  docker container ls
  # ou
  docker ps
      -a ou --all : Afficher tous les conteneurs peut-importe leur état
  ```

- Supprimer un conteneur Docker

  ```docker
  docker rm <CONTAINER_ID ou CONTAINER_NAME>
      -f ou --force : forcer la suppression
  ```

- Supprimer tous les conteneurs Docker

  ```docker
  docker rm -f $(docker ps -aq)
  ```

- Exécuter une commande dans un conteneur Docker

  ```docker
  docker exec <CONTAINER_ID ou CONTAINER_NAME> <COMMAND_NAME>
      -t ou --tty : Allouer un pseudo TTY
      -i ou --interactive : Garder un STDIN ouvert
      -d ou --detach : lancer la commande en arrière plan
  ```

- Transformer un conteneur en image

  ```docker
  docker commit <CONTAINER_NAME ou CONTAINER_ID> <NEW IMAGENAME>
      -a ou --author <string> : Nom de l'auteur (ex "John Hannibal Smith <hannibal@a-team.com>")
      -m ou --message <string> : Message du commit
  ```

###  4.2. <a name='Debug'></a>Debug


- Récupérer des informations de bas niveau d'un conteneur ou d'une image

  ```docker
  docker inspect <CONTAINER_ID ou CONTAINER_NAME ou IMAGE_NAME ou IMAGE_ID>
    -f ou --format : formater le résultat
  ```

- Afficher en temps réels les statistiques des différentes
  ressources consommées par votre conteneur en mode streaming  

  ```docker
  docker stats <CONTAINER_ID ou CONTAINER_NAME>
    -f ou --format : formater le résultat
    --no-stream : désactiver le mode streaming
  ```

- Visualiser des informations sur les différentes couche de votre image

  ```docker
  docker history <IMAGE_NAME ou IMAGE_ID>
    -f ou --format : formater le résultat
  ```

- Examiner les logs d'un conteneur

  ```docker
  docker logs <CONTAINER_ID ou CONTAINER_NAME>
    -f : suivre en permanence les logs du conteneur
    -t : afficher la date et l'heure de la réception de la ligne de log
    --tail <NOMBRE DE LIGNE> = nombre de lignes à afficher à partir de la fin (par défaut "all")
  ```

---

##  5. <a name='DockerCompose'></a>Docker Compose

- Exécuter les services du docker-compose.yml

  ```docker
  docker-compose up
    -d : Exécuter les conteneurs en arrière-plan
  ```

- Lister des conteneurs du Docker Compose

  ```docker
  docker-compose ls
    -a ou --all : afficher aussi les conteneurs stoppés
  ```

- Sorties/erreurs des conteneurs du Docker Compose

  ```docker
  docker-compose logs
    -f : suivre en permanence les logs du conteneur
    -t : afficher la date et l'heure de la réception de la ligne de log
    --tail=<NOMBRE DE LIGNE> = nombre de lignes à afficher à partir de la fin pour chaque conteneur.
  ```

- Tuer les conteneurs du Docker Compose

  ```docker
  docker-compose kill
  ```

- Stopper les conteneurs du Docker Compose

  ```docker
  docker-compose stop
    -t ou --timeout : spécifier un timeout en seconde avant le stop (par défaut : 10s)
  ```

- Démarrer les conteneurs du Docker Compose

  ```docker
  docker-compose start
  ```

- Arrêtez les conteneurs et supprimer les conteneurs, réseaux, volumes, et les images

  ```docker
  docker-compose down
    -t ou --timeout : spécifier un timeout en seconde avant la suppression (par défaut : 10s)
  ```

- Supprimer des conteneurs stoppés du Docker Compose

  ```docker
  docker-compose rm
    -f ou --force : forcer la suppression
  ```

- Lister les images utilisées dans le docker-compose.yml

  ```docker
  docker-compose images
  ```

---

##  6. <a name='Volumes'></a>Volumes

- Créer une volume
docker volume create <VOLUME NAME>

- Lister les volumes

  ```docker
  docker volume ls
  ```

- Supprimer un ou plusieurs volume(s)

  ```docker
  docker volume rm <VOLUME NAME>
      -f ou --force : forcer la suppression
  ```

- Récolter des informations sur une volume

  ```docker
  docker volume inspect <VOLUME NAME>
  ```

- Supprimer tous les volumes locaux non inutilisés

  ```docker
  docker volume prune
      -f ou --force : forcer la suppression
  ```

- Supprimer un conteneur Docker avec le/les volumes associés

  ```docker
  docker rm -v <CONTAINER_ID ou CONTAINER_NAME>
    -f ou --force : forcer la suppression
    -v ou --volume : supprime les volumes associés au conteneur
  ```

---

##  7. <a name='RseauDocker'></a>Réseau Docker

Les types de drivers :
- **`driver none`** : interdire toute communication interne et externe
- **`driver host`** : utiliser la même interface que l'hôte
- **`driver overlay`** : réseau distribué entre plusieurs hôtes possédant le moteur Docker
- **`driver macvlan`** : attribuer une adresse MAC à un conteneur (apparaît comme un périphérique physique)

- Créer un réseau docker

  ```docker
  docker network create --driver <DRIVER TYPE> <NETWORK NAME>
  ```

- Lister les réseaux docker

  ```docker
  docker network ls
  ```

- Supprimer un ou plusieurs réseau(x) docker

  ```docker
  docker network rm <NETWORK NAME>
  ```

- Récolter des informations sur un réseau docker

  ```docker
  docker network inspect <NETWORK NAME>
    -v ou --verbose : mode verbose pour un meilleur diagnostique
  ```

- Supprimer tous les réseaux docker non inutilisés

  ```docker
  docker network prune
    -f ou --force : forcer la suppression
  ```

- Connecter un conteneur à un réseau docker

  ```docker
  docker network connect <NETWORK NAME> <CONTAINER NAME>
  ```

- Déconnecter un conteneur à réseau docker

  ```docker
  docker network disconnect <NETWORK NAME> <CONTAINER NAME>
    -f ou --force : forcer la déconnexion
  ```

- Démarrer un conteneur et le connecter à un réseau docker

  ```docker
  docker run --network <NETWORK NAME> <IMAGE NAME>
  ```

---

##  8. <a name='DockerMachine'></a>Docker Machine

- Créer une machine Docker

  ```docker
  docker-machine create -d <DRIVER NAME> <MACHINE NAME>
    -d ou --driver : choisir un driver
  ```

- Rendre une machine Docker active

  ```docker
  eval $(docker-machine env <MACHINE NAME>)
  ```

- Lister les machines Docker

  ```docker
  docker-machine ls
  ```

- Vérifier quelle est la machine Docker active dans le shell courant

  ```docker
  docker-machine active
  ```

- Supprimer un ou plusieurs machine(s) Docker

  ```docker
  docker-machine rm <MACHINE NAME>
    -f ou --force : forcer la suppression
  ```

- Se connecter en ssh sur une machine Docker

  ```docker
  docker-machine ssh <MACHINE NAME>
  ```

- Stopper une machine Docker

  ```docker
  docker-machine stop <MACHINE NAME>
  ```

- Démarrer une machine Docker

  ```docker
  docker-machine start <MACHINE NAME>

- Redémarrer une machine Docker

  ```docker
  docker-machine restart <MACHINE NAME>
  ```

- Récolter des informations sur une machine Docker

  ```docker
  docker-machine inspect <MACHINE NAME>
  ```

- Récupérer les variables d'environnements d'une machine Docker

  ```docker
  docker-machine env <MACHINE NAME>
  ```

- Mettre à niveau une machine Docker vers la dernière version de Docker

  ```docker
  docker-machine upgrade <MACHINE NAME>  
  ```

---

## Docker Swarm

- Gestion du cluster Swarm

  ```docker
  docker swarm
  ```

- Gestion des conteneurs uni-service

  ```docker
  docker service
  ```

- Gestion des conteneurs multi-services

  ```docker
  docker stack
  ```


- Gestion des nœuds

  ```docker
  docker node
  ```

- Activer le mode Swarm

  ```docker
  docker swarm init
  ```

- Joindre une machine au cluster Swarm

  ```docker
  docker swarm join --token <token> <myvm ip>:<port>
  ```

###  8.1. <a name='nodes'></a>Les nœuds

- Lister les différents nœuds de votre Swarm 

  ```docker
  docker node ls
  ```

- Inspecter un nœud

  ```docker
  docker node inspect <NODE NAME> 
      --pretty : meilleur effet visuel
  ```

- Retirer un nœud de votre Swarm (ne supprime pas la VM)

  ```docker
  docker node rm <NODE NAME>
      -f ou --force : forcer la suppression
    ```

###  8.2. <a name='services'></a>Les services

- Créer un service

  ```docker
  docker service create <IMAGE NAME>
      --name : nom du service
    --replicas <number> : nombre de tâches
    --publish published=<cible>,target=<source> : mapper un port
    --restart-condition=<conditon> : condition de redémarrage en cas d'erreur
    --limit-memory <number> : limiter l'utilisation de la mémoire
    --limit-cpu <number> : limiter l'utilisation du CPU
    ```

- Visualiser l'état d'avancement de vos services Swarm 

  ```docker
  docker service ls
  ```

- lister les différentes tâches de votre service 

  ```docker
  docker service ps <SERVICE NAME>
  ```

- Mise en échelle des répliques de votre service

  ```docker
  docker service scale <SERVICE NAME>=<NUMBER>
  ```

- Mise à jour de des conteneurs de votre service

  ```docker
  docker service update --image <IMAGE NAME>:<TAG> <SERVICE NAME>
  ```

- Supprimer un service

  ```docker
  docker service rm flaskc
  ```

###  8.3. <a name='stacks'></a>Les stacks


- Déployer une nouvelle pile ou met à jour une pile existante

  ```docker
  docker stack deploy -c <Docker Compose File> <STACK NAME>
  ```

- Lister tous les services de votre pile

  ```docker
  docker stack services <STACK NAME>
  ```

- Répertorier les tâches de la pile

  ```docker
  docker stack ps <STACK NAME>
  ```

- Supprimer tous les services de votre pile

  ```docker
  docker stack rm <STACK NAME>
  ```

- Lister le nombre de services de votre pile

  ```docker
  docker stack ls
  ```
