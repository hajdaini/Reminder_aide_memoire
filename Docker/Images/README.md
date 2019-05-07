# Les images Docker

- **Voir les commandes pour l’administration des images :**

  ```shell
  docker | grep --color image
  ```

- **Rechercher une image (on peut savoir si c’est une officielle ou pas) sur le dockerhub :**

  ```shell
  docker search debian
  --filter "is-official=true" : Rechercher que les images officielles
  ```

- **Récupérer une image**

  ```shell
  docker pull debian
  ```

- **Vérifier les images disponibles :**

  ```shell
  docker images
  ```

- **Supprimer une image (option - -force pour forcer la suppression) :**

  ```shell
  docker rmi <imageID> 
  ```

- **Sauvegarde une image :**

  ```shell
  docker save <imageID>  -o /tmp/debian.tar
  ```

- **Charger une image depuis un tar :**

  ```shell
  docker load -i /tmp/debian.tar
  ```
  