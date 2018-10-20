# Registry

## Definition

Un registre est un système de stockage contenant des images Docker nommées, disponibles dans différentes versions étiquetées.
Différents registry proposé par Docker sont disponible :

- Docker hub (Par Défaut)
    - Registry officiel hebergé par Docker
- Docker Registry
    - Solution Open Source
- Docker Trsuted Registry
    - Solution commerciale
    - Disponible avec Docker-EE standard / avancé

Il existe aussi d'autre providers hors Docker comme :
- Amazon EC2 container registry
- Google Container Registry
- GitLab Container registry
- etc ...


### Docker hub

**Installer une image depuis le docker hub :**
```
docker pull <IMAGE_NAME>
```

**Pusher son image sur son propre repository**
Il faut d'abord se logger 
```
docker login
```
```
docker push <USER>/<IMAGE_NAME>:[VERSION]
```

### Docker Registry
Il faut une connexion TLS pour communiqué avec notre Docker Registry (sauf si on est en localhost)

Pour la partie TLS (je vais surement créer une Dockerfile) : https://www.youtube.com/watch?v=SEpR35HZ_hQ&t=498s

Je vais poursuivre l'exemple en localhost

```bash
# Installer le registry 
docker pull registry

# Créer le conteneur
docker container run -d -p 5000:5000 regsitry

# Installer notre image debian par exemple:
docker pull debian:stable-slim

# Tagger l'image debian pour correspondre au format de notre registry (<IP|HOSTNAME>/<PORT>/<NAME>:[VERSION])
docker tag debian:stable-slim localhost:5000/debian

# Upload l'image sur notre registry
docker push localhost:5000/debian
```

- **lister les images dans le registry :**
```
curl localhost:5000/v2/_catalog
Output : {"repositories":["debian"]}
```

- **lister les images dans le registry :**
```
curl localhost:5000/v2/debian/tags/list
Output : {"name":"debian","tags":["latest"]}
```

### Docker Trusted Registry
**Avantage :**
- Support commercial
- Intégration LDAP/AD
- Selection du backend de stockage (S3, Azure, Google Cloud Storage, etc ...)
