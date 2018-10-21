# Docker-machine

## Definition

Docker Machine est un outil qui vous permet d'installer Docker Engine sur des hôtes virtuels et de gérer les hôtes à l'aide de commandes docker-machine. 
Vous pouvez l'utiliser pour créer des hôtes avec le Docker Engine sur votre ordinateur Mac ou Windows local, sur le réseau de votre entreprise, dans votre centre de données ou sur des fournisseurs de cloud, tels qu'Azure, AWS ou Digital Ocean.

## Commandes

- **Condition pour créer une docker-Machine :**
    - Activer la virtualisation sur son CPU
    - La machine sur laquelle on a installé le docker avoir au préalable VirtualBox de préinstallé (si c'est le driver est virtualbox) même chose pour Hyper-V VMWare etc. …

Un driver est la plateforme sur le quel on va créer nos machines docker (exemple VirtualBox), tous les drivers sont disponibles ici : https://docs.docker.com/machine/drivers/ 
- **Création d’un hôte docker pour un driver de type virtualbox :**
```
root@docker:~#  docker-machine create -d "virtualbox" <hostNAME>
--virtualbox-disk-size "10000"
--virtualbox-memory "512"
```
- **Supprimer un hôte :**
```
root@docker:~#  docker-machine rm <hostNAME>
```
- **Lister les hôtes avec certaines informations :**
```
root@docker:~#  docker-machine ls
```
- **Démarrer/stopper un hôte :**
```
root@docker:~#  docker-machine start/stop <hostNAME>
```
- **Avoir des informations sur un hôte :**
Il existe aussi la command (ip, url, config, status, version)
```
root@docker:~#  docker-machine inspect <hostNAME>
```
- **Upgrader le moteur de DOCKER sur l’hôte (stop la machine temporairement) :**
```
root@docker:~#  docker-machine upgrade <hostNAME>
```
- **Se connecter à un hôte :**
```
root@docker:~#  docker-machine ssh <hostNAME>
```
- **Copier des fichiers depuis des machines :**
```
root@docker:~#  docker-machine scp <path> <hostNAME>:<path> 
root@docker:~#  docker-machine scp <hostNAME>:<path> <path>
```

Une fois qu’on est connecté sur le hôte docker on peut alors manipuler des images et des conteneurs.