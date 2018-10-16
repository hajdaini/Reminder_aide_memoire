# Les images Docker

**Voir les commandes pour l’administration des images :**
```
root@docker:~# docker | grep --color image
```
**Rechercher une image (on peut savoir si c’est une officielle ou pas) sur le dockerhub :**
```
root@docker:~# docker search debian
--filter "is-official=true" : Rechercher que les images officielles
```
**Récupérer une image**
```
root@docker:~# docker pull debian
```
**Vérifier les images disponibles :**
```
root@docker:~# docker images
```
**Supprimer une image (option - -force pour forcer la suppression) :**
```
root@docker:~# docker rmi <imageID> 
```
**Sauvegarde une image :**
```
root@docker:~# docker save <imageID>  -o /tmp/debian.tar
```
**Charger une image depuis un tar :**
```
root@docker:~# docker load -i /tmp/debian.tar
```
