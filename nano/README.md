## Pré-requis

**Supprimer la version actuelle de nano !**

## Install

Lien de téléchargement de nano : https://www.nano-editor.org/download.php

``` 
wget http://lien/ nano-x.y.z.tar.gz 
tar -zxvf nano-x.y.z.tar.gz
``` 

**centos :**
``` 
yum install gcc ncurses-devel
``` 

**debian :**
``` 
apt-get install gcc libncurses5-dev
``` 

``` 
cd nano-x.y.z/
./configure --prefix=/usr
make
make install
``` 

### Config :

- Renommer le fichier de config **nanorc** en **.nanorc** et le mettre dans <i>~/</i>
```
mv nanorc ~/.nanorc
```
- Dezipper et deplacer les fichiers de coloration syntaxique de **nano.zip** dans <i>/usr/share/nano/</i> 
```
cd /usr/share/nano/
rm -f *.nanorc
wget <lien>
unzip nano.zip
mv * ..
```
### Problème :
C'est possible d'avoir l'erreur suivante : 
```
root@vps615208:/home/debian# nano test.txt
-bash: /bin/nano: No such file or directory
```
Il suffit de recopier le fichier les binaires de nano 
```
cp /usr/bin/nano /bin/
```

### Inspiration et Doc :

- Fichier de config : https://manpages.debian.org/unstable/nano/nanorc.5.en.html 
- Coloration syntaxique : https://github.com/scopatz/nanorc 
 
### Screenshot

<img src="looking.jpg">
