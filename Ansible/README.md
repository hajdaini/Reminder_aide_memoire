# Concepts Ansible

- **Playbooks** : Des fichiers YAML pour définir les tâches sur des hôtes cibles.
- **Ad-hoc Commands** : Commandes ponctuelles depuis la ligne de commande.
- **Inventaire (Inventory)** : Liste d'hôtes cibles définie dans un fichier ou générée dynamiquement.
- **Host** : Hôte cible pour l'exécution des tâches.
- **Tasks** : Actions à exécuter sur les hôtes cibles dans un Playbook.
- **Modules Ansible** : Composants pour des actions spécifiques sur les hôtes.
- **Facts** : Informations sur les hôtes cibles, telles que les détails système.
- **Rôles** : Ensembles structurés de Playbooks, variables et fichiers réutilisables.
- **Template** : Génération dynamique de fichiers avec Jinja2.
- **Filtres Jinja2** : Utilisés pour formater les données dans les Playbooks.
- **Handlers** : Tâches déclenchées en réponse à des modifications.
- **Vault (Ansible Vault)** : Outil pour chiffrer des données sensibles.


```yaml
---
- hosts: web_servers  # Concept : Host
  tasks:
    - name: Install Nginx  # Concept : Tasks
      apt:
        name: nginx
        state: present

    - name: Start Nginx
      service:
        name: nginx
        state: started

- hosts: database_servers
  tasks:
    - name: Install PostgreSQL
      yum:
        name: postgresql
        state: present
      become: yes

    - name: Configure PostgreSQL
      template:  # Concept : Template
        src: postgresql.conf.j2
        dest: /etc/postgresql.conf

- hosts: app_servers
  roles:
    - common  # Concept : Roles
    - web_server

- hosts: web_servers
  tasks:
    - name: Update DNS Records  # Concept : Handlers
      command: /usr/bin/update_dns
      notify: Restart Network

  handlers:
    - name: Restart Network
      service:
        name: network
        state: restarted

- hosts: web_servers
  tasks:
    - name: Execute Jinja2 Filter  # Concept : Filtres Jinja2
      command: echo "{{ 'Hello, World!' | upper }}"
```

## Structure du Projet Ansible

```text
my-ansible-project/
├── ansible.cfg
├── inventory/
│   ├── hosts
│   ├── group_vars/
│   │   ├── group1.yml
│   │   ├── group2.yml
│   ├── host_vars/
│   │   ├── host1.yml
│   │   ├── host2.yml
├── roles/
│   ├── role1/
│   │   ├── tasks/
│   │   │   ├── main.yml
│   │   ├── templates/
│   │   ├── vars/
│   │   ├── defaults/
│   ├── role2/
│   │   ├── tasks/
│   │   │   ├── main.yml
│   │   ├── templates/
│   │   ├── vars/
│   │   ├── defaults/
├── playbook.yml
└── files/
    ├── file1.txt
    ├── file2.txt
```

- `ansible.cfg` : Fichier de configuration global pour Ansible.
- `inventory/` : Répertoire contenant la configuration de l'inventaire.
  - `hosts` : Fichier d'inventaire principal pour définir les hôtes cibles.
  - `group_vars/` : Dossier pour les variables spécifiques aux groupes d'hôtes.
  - `host_vars/` : Dossier pour les variables spécifiques aux hôtes individuels.
- `roles/` : Répertoire contenant les rôles Ansible réutilisables.
  - `role1/` : Premier exemple de rôle.
    - `tasks/` : Dossier pour les tâches spécifiques au rôle.
    - `templates/` : Dossier pour les modèles de fichiers.
    - `vars/` : Dossier pour les variables spécifiques au rôle.
    - `defaults/` : Dossier pour les valeurs par défaut des variables.
  - `role2/` : Deuxième exemple de rôle (structuré de la même manière que role1).
- `playbooks` : Fichier le playbook Ansible.
- `files/` : Répertoire pour les fichiers statiques à copier sur les hôtes cibles.