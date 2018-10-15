```Dockerfile
FROM debian:stable-slim

ARG VERSION="1.0.3"
ARG APT_FLAGS="-q -y"

ENV LANG="en_US.UTF-8"

LABEL maintainer="NOM Prenom <test@gmail.com>" \
      version="$VERSION-debian-testing" \
      description="ROS2 for java" \
      # il y'a d'autres option pour le maintainer

RUN apt-get update && \
    apt-get install ${APT_FLAGS} \
    curl \
    wget \
    apt-utils \
    apache2 \
    && apt-get autoclean

ADD index.html /var/www/html

# Si le volume ne map nulle part alors utiliser la commande docker inspect <DOCKER_CONTAINER>
VOLUME /local/path:/container_path/data

EXPOSE 80:8080 # on peut choisir de mapper un port
EXPOSE 443 # ou de ne pas mapper un port

# La prochaine commande utilisera ce répertoire de travail.
WORKDIR  /etc/apache

ENTRYPOINT ["/usr/sbin/apache2ctl, "-D",]
CMD ["FOREGROUND"] # on peut mettre les arguments d'ENTRYPOINT dans CMD comme ici
```

- **FROM :** permet de définir depuis quelle base votre image ve être créée
- **MAINTAINER :** indique la personne qui a créé ou maintient ce Dockerfile
- **ARG :**  : variable qu'on peut utiliser dans un Dockerfile
- **RUN :** permet d'exécuter une commande lors du build (création) de l'image. Chaque instruction RUN va créer un Layer qui sera utilisé dans le cas de modification ultérieur de votre Dockerfile.
- **COPY :** permet de copier des fichiers depuis la machine de contrôle vers la machine hôte
- **ADD :** comme COPY mais on peut utiliser des liens ou des archives qui si le format est reconnu sera décompressé à la volée. Utile pour copier des sources d’applications.
- **EXPOSE :** permet d'exposer un port du container vers l'extérieur
- **CMD :** détermine la commande qui sera exécutée lorsque le container démarrera cette clé est unique et s'il y en a plusieurs seule la dernière sera utilisée. Cette option peut être surchargé par la commande docker run.
- **ENTRYPOINT :** permet d'ajouter une commande qui sera exécutée lors de la création du conteneur. Contrairement à CMD ENTRYPOINT ne peut pas être surchargé par la commande “docker run”.  Info importante les arguments passés lors de la commande “docker run” seront utilisés en arguments à la commande spécifiée dans l’instruction ENTRYPOINT
- **WORKDIR :** définit le répertoire de travail qui sera utilisé pour le lancement des commandes ENTRYPOINT et/ou CMD et sera le dossier on sera par défaut une fois le conteneur démarré
- **ENV :** permet de définir des variables d'environnements dans notre conteneur (taper la commande env dans le conteneur pour la voir) mais elles peuvent aussi être utilisé dans le Dockerfile.
- **VOLUMES :** permet de créer un point de montage qui permettra de persister les données. On pourra alors choisir de monter ce volume dans un dossier spécifique en utilisant la commande `run -v :
- **USER :** désigne quel utilisateur lancera les prochaines instructions RUN, CMD ou ENTRYPOINT 

Création de l’image depuis le dockerfile :
```
root@docker:~# docker build -t <IMAGE_NAME> .
```
