# Exemple

```Dockerfile
FROM debian:stable-slim

ARG VERSION="1.0.3"
ARG APT_FLAGS="-q -y"

ENV LANG="en_US.UTF-8"

LABEL maintainer="NOM Prenom <test@gmail.com>" \
      version="$VERSION-debian-testing" \
      description="blabla" \
      # il y'a d'autres option pour le maintainer

RUN apt-get update && \
    apt-get install ${APT_FLAGS} \
    curl \
    wget \
    apt-utils \
    apache2 \
    && apt-get autoclean

ADD index.html /var/www/html

# Si aucun mappage n'est spécifi alors il faut utiliser la commande docker inspect <DOCKER_CONTAINER> pour connaitre vers ou le volume pointe
VOLUME /local/path:/container_path/data

EXPOSE 80:8080 # on peut choisir de mapper un port
EXPOSE 443 # ou de ne pas mapper un port :)

# La prochaine commande utilisera ce répertoire de travail.
WORKDIR  /etc/apache

ENTRYPOINT ["/usr/sbin/apache2ctl, "-D",]
CMD ["FOREGROUND"] # on peut mettre les arguments d'ENTRYPOINT dans CMD comme ici
```
# Définitions

- **FROM :** Permet de définir depuis quelle base l'image va être créée
- **MAINTAINER :** Indique la personne qui a créé ou maintient ce Dockerfile
- **ARG :** Variable qu'on peut utiliser dans un Dockerfile
- **ENV :** Permet de définir des variables d'environnements dans notre conteneur (taper la commande ***env*** dans le conteneur pour voir la viariable) mais elles peuvent aussi être utilisé dans le Dockerfile
- **RUN :** Permet d'exécuter une commande lors de la création de l'image. Chaque instruction RUN va créer un layer qui sera utilisé dans le cas de modification ultérieur du Dockerfile.
- **COPY :** Permet de copier des fichiers depuis notre machine vers le conteneur
- **ADD :** Même chose que COPY mais on peut utiliser des liens ou des archives (si le format est reconnu sera décompressé à la volée) 
- **EXPOSE :** Permet d'exposer un port du container vers l'extérieur
- **CMD :** Détermine la commande qui sera exécutée lorsque le container démarrera cette clé est unique et s'il y en a plusieurs seule la dernière sera utilisée. Cette option peut être surchargé à la fin de la commande ***docker run***
- **ENTRYPOINT :** Permet d'ajouter une commande qui sera exécutée lors du démarrage du container. Contrairement à CMD ENTRYPOINT ne peut pas être surchargé par la commande ***docker run***. Par contre les arguments passés lors de la commande ***docker run*** seront utilisés en arguments à la commande spécifiée dans l’instruction ENTRYPOINT
- **WORKDIR :** Définis le répertoire de travail qui sera utilisé pour le lancement des commandes ENTRYPOINT et/ou CMD et sera aussi le dossier courant quand le conteneur démarrera
- **VOLUMES :** Permet de créer un point de montage qui permettra de persister les données
- **USER :** désigne quel utilisateur lancera les prochaines instructions RUN, CMD ou ENTRYPOINT 

**Création d’image depuis un Dockerfile :**

```shell
docker build -t <IMAGE_NAME> .
```
