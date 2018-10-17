# Debug

- **Avoir des informations sur un conteneur ou une image : :**
```
root@docker:~# docker inspect <conteneurID> /<imageID> 
```
Filtrer l’output de la commande inspect : https://docs.docker.com/engine/reference/commandline/inspect/#get-an-instances-mac-address

- **Afficher en live les ressources consommées par le conteneur :**
```
root@docker:~# docker stats <conteneurID> 
```
