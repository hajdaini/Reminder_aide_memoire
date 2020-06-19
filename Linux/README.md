# Commandes Shell

- [Manuel](#manuel)
- [Commandes fichiers](#commandes-fichiers)
- [Compression et décompression](#compression-et-décompression)
- [Utilisateurs, groupes et droits](#utilisateurs-groupes-et-droits)
- [Processus](#processus)
- [Recherche](#recherche)
- [Réseaux](#réseaux)
- [Mise à jour](#mise-à-jour)
- [Info système](#info-système)
- [Transférer des fichiers](#transférer-des-fichiers)
- [Autres](#autres)
- [Commandes à éviter](#commandes-à-éviter)

## Manuel

|NOM|DESCRIPTION|
|:--|:--|
| **`man <commande>` :** <br> => **`-k <keyword>`**|Afficher le manuel d'une commande/fonction |

## Commandes fichiers

|NOM|DESCRIPTION|
|:--|:--|
|**`cat <path>`**| Afficher le contenu d'un fichier sur la sortie standard|
|**`cd <path>`**|Changer de répertoire|
|**`cp <path>`**|Copier des fichiers et des répertoires|
|**`ln -s <path> <path_symlink>`**|Créer des liens entre fichiers|
|**`rm <path>`**|Effacer des fichiers ou répertoires avec l'option **`-r`**|
|**`mv`**|Déplacer ou renommer un fichier et des répertoire|
|**`ls <path>`**|Lister (afficher) le contenu d'un répertoire|
|**`pwd`**|Récupérer le nom du répertoire courant|
|**`touch <file>`**|Modifier l'horodatage d'un fichier (peut aussi en créer)|
|**`file <path>`**|Déterminer le type d'un fichier|
|**`mkdir <rep>`**|Créer des répertoires|
|**`more <file>`**|Se déplacer depuis le début d'un texte, écran par écran|
|**`less <file>`**|Comme la commande **`more`** mais plus flexible avec raccourcis vim|
|**`uniq <file>` <br> => `-d` :** Afficher uniquement les lignes dupliquées|Afficher les lignes d'un fichier sans lignes dupliquées|
|**`head -n <num> <file>`** |Afficher uniquement les 'num' premières lignes d'un fichier|
|**`tail <file>`** <br> => **`-n <num>`** <br> => **`-n + num` :** depuis la ligne `num` <br> => **`-f` :** lecture stream jusqu'au `Ctrl+C`|Afficher les 10 dernières lignes d'un fichier|
|**`sort <file>` <br> => `-r` :** ordre décroissant <br> => **`-n` :** ordre numérique|Trier les lignes d'un fichier texte|
|**`wc` <br> => `-l`:** ligne <br> => **`-w` :** mot <br> => **`-c` :** caractère|Afficher le nombre d'octets, de mots et de lignes d'un fichier|
|**`diff <old_file> <new_file>` <br> => `-r`** : comparer des répertoires |Trouver les différences entre des fichiers|
|**`cut <file>` <br> => `-d';'` :** délimiteur <br> => **`-d';' -f5` :** 5eme champ <br> => **`-d';-f2,10'` :** 2ème et 10ème champ <br> => **`-d';' -f3-` :** 3ème jusqu'à la fin|Supprimer une partie de chaque ligne d'un fichier|
|**`sed`** <br> => **`-i`** : modifier le fichier directement <br> => **`sed 's/^old/new/gi' <filename>`**|Filtrer et transformer du texte|
|**`awk '{print $1}' <filename>`**|Appliquer un certain nombre d'actions sur un fichier|
|**`ls | xargs rm`** <br> **`ls | xargs -I{} rm -rf '{}'`**(`-I{}`  = remplacer par '{}' <br> **`-t` :** afficher avant d'exécuter|La sortie d'une commande est transmise en tant qu'argument d'entrée à une autre commande|

## Compression et décompression 

> gzip compresse mieux que Bzip2 mais est plus lent à la dé/compression

|NOM|DESCRIPTION|
|:--|:--|
|**`tar [options] name.tar[.gz or .bz2] [chemin]`** <br> => **`c` :** créer <br> => **`x` :** extraire <br> => **`f` :** nom de l'archive  <br> => **`t` :** contenu de l'archive <br> => **`v` :** verbose <br> => **`z` :** gzip <br> => **`j` :** Bzip2 | Utilitaire GNU de gestion d'archives TAR|
|**`zip [options] name.zip [chemin]`** <br> => **`-r`** : répertoire |Créer et compresser des archives ZIP|
|**`unzip`**|Lister, tester et extraire des fichiers compressés dans une archive ZIP|


## Utilisateurs, groupes et droits

|NOM|DESCRIPTION|
|:--|:--|
|**`adduser <username>`**|Ajouter un nouvel utilisateur|
|**`deluser <username>`**<br> => **`-r` :** supprimer aussi le dossier utilisateur/messagerie|Supprimer un utilisateur|
|**`addgroup`**|Ajouter un nouveau groupe|
|**`chown <username>:<group> <path>`** <br> => **`-R` :** récursive|Modifier le propriétaire et le groupe d'un fichier|
|**`chmod <rights> <path>`** <br> => **`4/r `:** Read <br> => **`2/w `:** Write <br> => **`1/x `:** Execute <br> => **`0 `:** denied|Modifier les autorisations d'accès à un fichier|
|**`usermod`** <br> => **`-G`** : modifier le groupe <br> => **`-G -a`** : ajouter à un groupe <br> => **`-l`** : modifier le nom|Modifier les informations d'un utilisateur|
|**`groups <username>`**|Afficher les groupes d'un utilisateur|
|**`id <username>`**|Afficher les UIDs et GIDs d'un utilisateur|
|**`w`**|`Afficher les utilisateurs connectés et leur activité|
|**`whoami`**|Afficher l'utilisateur à qui vous êtes connecté|
|**`passwd`**|Modifier le mot de passe d'un utilisateur|
|**`last [username|shutdown|reboot]`** <br> => **`-n <nbr>`**|Afficher les dernières connexions sur le système|


## Processus

|NOM|DESCRIPTION|
|:--|:--|
|**`ps aux`**|Afficher l'état des processus en cours|
|**`top`** <br> => **`e` :** Modifier l'unité de stockage (à lancer après `top`)|Lister les processus (avec mise à jour toutes les X secondes)|
|**`kill <signal> <pid>`** <br> => **`9` :** tuer le processus |Envoyer un signal à un processus|
|**`killall <name>`**|Envoyer un signal à des processus indiqués par leurs noms|
|**`nohup <software>`**|Permet à un processus de vivre lorsque le terminal est tué|
|**`<cmd> &`**|Basculer en arrière plan le processus lancé|
|**`Ctrl+Z`**|Stopper la tâche en cours à reprendre avec **`fg`** ou **`bg`**|
|**`jobs`**|Afficher les tâches en cours d'exécution et leur état|
|**`bg [%job_id]`**|Basculer une tâche en arrière-plan|
|**`fg [%job_id]`**|Basculer une tâche au premier-plan (devient la tâche en cours)|

## Recherche

|NOM|DESCRIPTION|
|:--|:--|
|**`locate <filename>`**|Rechercher des fichiers depuis une bdd interne (maj toute les 24h)|
|**`updatedb`**|Mise à jour de la bdd interne de la commande `locate`|
|**`find <path> -name <pattern>`** <br> => **`-iname`** : ignorer la casse <br> => **`-type [-d -f]`** : recherche  par fichiers ou que répertoires <br> => **`-size <+5M>`** : recherche par taille <br> => **`-perm <777>`** : recherche par droit <br> => **`-delete`**  |Rechercher des fichiers dans une hiérarchie de répertoires|
|**`grep <word> <path>`** <br> => **`-r`** : récursive <br> => **`-i`** : ignorer la casse <br> => **`-E ^regex$`** : expression régulière <br> => **`-A` <num>** : afficher les `num` prochaines lignes|Afficher les lignes correspondant à un motif donné|
|**whereis**|Rechercher les fichiers exécutables, les sources et les pages de manuel d'une commande|

## Réseaux

|NOM|DESCRIPTION|
|:--|:--|
|**`host <ip or domain>`**|Chercher des noms de machine à l'aide d'un serveur de domaine|
|**`dig <domain>`**|Obtenir des informations DNS sur une nom de domaine|
|**`hostname`** : afficher le nom d'hôte de la machine<br> => **`-i` :** afficher l'IP de l'hôte <br> => **`-I` :** afficher les IPs de l'hôte <br> => **`--fqdn`** <br> => **`hostname <new_hostname>` :** Changer le hostname |afficher ou modifier des infos sur le nom d'hôte du système|
|**`ip`** <br> => **`a` :** afficher l'IPv4 et 6 d'une interface <br> => **`a show <interface>` :** filtrer une interface  <br> => **`link ls up` :** afficher que les interfaces "up"  <br> => **`a [add|del] IP/24 dev <interface>` :** Dé/Assigner une adresse IP à une interface  <br> => **`link set dev  <interface> [up|down]` :** Dé/Assigner une adresse IP à une interface |Afficher/manipuler le routage, les périphériques réseau, les interfaces et les tunnels|
|**`iptables`**|Filtrer les paquets IP et NAT (pare-feu)|
|**`traceroute <ip or domain>`**|Afficher la trace des paquets routés vers l'hôte réseau|
|**`whois <ip or domain>`**|Afficher les informations d'un domaine|
|**`ping <ip or domain>`**|Envoyer des datagrammes à un hôte sur le réseau|
|**`ss`** <br> => **`-l` :** Affiche uniquement les sockets d'écoute <br> => **`-p` :** Afficher le nom processus utilisant le socket.<br> => **`-n` :** N'essaie pas de résoudre le hostname <br> => **`-t` :** socket tpc <br> => **`-u` :** socket udp <br> => **`-x` :** socket unix <br> => **`-s` :** afficher les stats des sockets |Analyser les sockets|
|**`wget <url>`**|Télécharger un fichier depuis le Web|

## Mise à jour

|NOM|DESCRIPTION|
|:--|:--|
|**`apt`** <br> => **`update`** <br> => **`upgrade`**  <br> => **`install <package>`** <br> => **`info <package>`** <br> => **`remove <package>`** <br> => **`purge <package>`** <br> => **`list --installed`**|Utilitaire d'APT pour la manipulation de paquets|
|**`apt-get`**|Utilitaire d'APT pour la manipulation de paquets dans des scripts|
|**`aptitude`**|Interface haut-niveau de gestion de paquets|
|**`dpkg`** <br> => **`-i <deb package>`:**  installer <br> => **`-R *.deb`:**  installation récursive <br> => **`-r <package_name>` :** supprimer <br> => **`-P <package_name>` :** purger|Gérer des paquets DEB|

## Info système

|NOM|DESCRIPTION|
|:--|:--|
|**`uname -a`**|Afficher les informations du système linux|
|**`uptime`**|Afficher le temps depuis lequel la machine est démarrée|
|**`date`**|Afficher ou configurer la date et l'heure du système|
|**`cal`**|Montrer le mois-ci dans un calendrier|
|**`df -h`**|Afficher la quantité d'espace occupé par les systèmes de fichiers|
|**`du -sh <path>`**|Afficher les statistiques sur l'utilisation du disque|
|**`free -h`**|Afficher la quantité de mémoire libre et utilisée par le système|
|**`mount <device> <path>`**|Monter un système de fichiers|
|**`umount <device>`**|Démonter des systèmes de fichiers|
|**`fdisk`** <br> => **`-l` :** lister les partitions <br> => **`<device>` :** modifier la partition|Manipuler des tables de partitions|

## Transférer des fichiers

|NOM|DESCRIPTION|
|:--|:--|
|**`scp path/to/local_file remote_host:path/to/remote_file`** <br> => <br> => **`scp remote_host:path/to/remote_file path/to/local_directory`**|Copier des fichiers vers une machine distante|

## Autres

|NOM|DESCRIPTION|
|:--|:--|
|**`watch -n <nbr> <cmd>`**|Répéter une commande toute les `nbr` seconde|

## Commandes à éviter

Ces commandes ne sont pas sécurisées, plus maintenues et/ou devenues obsolètes :

+ arp
+ ftp
+ ifconfig
+ ifdown
+ ifup
+ iptunnel
+ iwconfig
+ nameif
+ netstat
+ rcp
+ route
+ telnet
+ nslookup
