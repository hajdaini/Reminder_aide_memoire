# Services Google Cloud Platform (GCP)

- **Google Compute Engine (GCE) :**
  - Types:
    - Standard (n1-standard) : Équilibrage CPU et mémoire.
    - Optimisé mémoire (n1-highmem) : Plus de mémoire par CPU.
    - Optimisé calcul (n1-highcpu) : Plus de CPU par rapport à la mémoire.

- **Google Kubernetes Engine (GKE) :**
  - Types:
    - Standard : Déploiement de clusters de base.
    - Autogéré : Contrôle total sur le cluster Kubernetes.

- **Google Cloud Storage :**
  - Types:
    - Stockage standard (Standard Storage) : Accès fréquent aux données.
    - Stockage Nearline : Données moins fréquemment utilisées.
    - Stockage Coldline : Données archivées à coût réduit.
    - Stockage Archive : Stockage minimal pour données archivées.
  - Fonctionnalités : Contrôle d'accès basé sur des politiques, versioning.

- **Google Cloud SQL :**
  - Prise en charge de MySQL, PostgreSQL, SQL Server.

- **Google Cloud Functions :**
  - Types:
    - Fonctions déclenchées par des événements (ex. : Cloud Pub/Sub).
    - Fonctions HTTP pour des points de terminaison RESTful.

- **Google Cloud DNS :**
  - Types:
    - Zone DNS publique : gérer les domaines DNS publics
    - Zone DNS privée : service de domaine DNS privé pour les réseaux VPC dans GCP

- **Google Cloud IAM :**
  - Types d'utilisateurs:
    - Utilisateurs et groupes : Comptes individuels et collections d'utilisateurs.
    - Service Accounts : Identités pour applications et services.
  - Autorisations:
    - Permissions : Autorisations pour des actions spécifiques, comme "compute.instances.start".
    - Rôles : Ensembles de permissions, par exemple, le rôle "Viewer" pour voir sans modifier.
    - Politiques : Associations d'utilisateurs ou groupes avec des rôles pour définir les autorisations.

- **Virtual Private Cloud (VPC) :**
  - Types:
    - Réseau VPC personnalisé : VPC standard
    - Réseau VPC partagé (Shared VPC) : Partagez des ressources réseau entre projets.
  - Fonctionnalités:
    - Subnet:
    - Routes: routage pour diriger le trafic entre ressources.
    - Firewall Rules: Contrôle du trafic entrant et sortant avec des règles basées sur l'adresse IP, le port, etc.

- **Cloud Load Balancing (CLB) :**
  - Types:
    - HTTP(S) : Équilibrage de charge HTTP(S) pour les applications Web.
    - TCP/UDP : Équilibrage de charge basé sur TCP/UDP pour d'autres protocoles.

- **Google Container Registry (GCR) :**
  - Types de conteneurs : Stockage et gestion d'images Docker.
  - Fonctionnalités : Stockage et distribution d'images Docker, intégration avec Kubernetes, sécurité des images de conteneurs.

- **Google Cloud Logging (Stackdriver Logging) :**
  - Gestion des logs des ressources GCP

- **Google Cloud Monitoring (Stackdriver Monitoring) :**
  - Surveillance des métriques des ressources GCP



## IAM Hierarchy for GCP Networks and Resources

```text
├── Organization
│   ├── Folder A
│   │   ├── Project 1
│   │   │   ├── Cloud DNS
│   │   │   ├── VPC A
│   │   │   │   ├── Subnet 1
│   │   │   │   │   ├── GCE Frontend Instance
│   │   │   │   │   ├── Routes
│   │   │   │   │   ├── Firewall Rules
│   │   │   │   │   ├── ...
│   │   │   │   ├── Subnet 2
│   │   │   │   │   ├── GCE Backend Instance
│   │   │   │   │   ├── Routes
│   │   │   │   │   ├── Firewall Rules
│   │   │   │   │   ├── Load Balancers
│   │   │   │   │   ├── Cloud SQL
│   │   │   │   │   │   ├── MySQL Databases
│   │   │   │   │   ├── ...
│   │   │   │   ├── ...
│   │   │   ├── Cloud Storage Buckets
│   │   │   ├── Cloud Functions
│   │   │   ├── ...
│   │   │   ├── ...
│   │   ├── Project 2
│   │   ├── ...
│   ├── Folder B
│   │   ├── Project 3
│   │   │   ├── VPC B
│   │   │   │   ├── Subnet 3
│   │   │   │   │   ├── ...
│   │   │   │   ├── ...
│   │   │   ├── ...
│   │   ├── ...
│   ├── ...
```