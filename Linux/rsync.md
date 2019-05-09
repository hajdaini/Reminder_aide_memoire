# rsync

[Documentation](https://linux.die.net/man/1/rsync)

## Commandes

```sh
rsync -av SOURCE DEST
```

```sh
# Copie du contenu du dossier Demo1 vers Demo2
rsyn -av ./Demo1/ ./Demo2

# Copie du dossier Demo1 vers Demo2
rsyn -av ./Demo1 ./Demo2

# ssh
rsync -av ./src_directory user@host:~/dst_directory

# Change de port ssh
rsync -av ./src_directory -e 'ssh -p 3333' user@host:~/dst_directory

# Simuler l'execution de rsync (-n ou --dry-run)
rsyn -av --dry-run ./Demo1 ./Demo2

# Supprimer les fichiers non présent dans le dossier source (UTILISER --dry-run AVANT)
rsyn -av --delete ./Demo1 ./Demo2

# Exclure des fichiers ou dossier
rsync -a --exclude=*.sql --exclude=.git --exclude 'folder' ./src_directory user@host.com:~/dst_directory

# Inclure un fichier d'exclusion
rsync -a --exclude-from='exclude-file.txt' src_directory/ dst_directory/
```

exclude-file.txt

```
file1.txt
dir1/*
dir2
```
- **- h :** Pour "humanize". Les unités (octects) seront convertis en Kilo/Méga/Giga Octects au besoin, pour une meilleur lisibilité.

- **- P :** racourci vers --progress et --partials
  - **--progress** : montre l'avancement pendant le transfert (avec -v, affiche la progression de chaque fichier)
  - **--partial** :conserve les fichiers partiellement transférés

- **- z :** compresser avant d'envoyer (Pas besoin si fichiers non volumineux)



## Information

La drapeau **-a** ou **--archive** est un raccourci vers les drapeaux **-rlptgoD** :

- **-r :** pour une copie récursive (dossiers)
- **-l :** copie les liens symboliques.
- **-p :** conserve les permissions.
- **-t :** conserve les date de modifications .
- **-g :** conserve le groupe auquel appartient le fichier.
- **-o :** conserve le propriétaire auquel appartient le fichier.
- **-D :** préserve les fichiers spéciaux et les fichier devices.
