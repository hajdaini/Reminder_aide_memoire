## Centos

Lien de téléchargement de nano : https://www.nano-editor.org/download.php

``` 
wget http://lien/ nano-x.y.z.tar.gz 
tar -zxvf nano-x.y.z.tar.gz
yum install gcc
yum install ncurses-devel
cd nano-x.y.z/
./configure --prefix=/usr
make
make install
``` 

Fichier de config : https://manpages.debian.org/unstable/nano/nanorc.5.en.html 
couleurs des fichiers : https://github.com/scopatz/nanorc 
Mon fichier config dans ~/.nanorc est **nanorc**
 
Mes fichiers de couleurs des fichiers dans /usr/share/nano/ est **nano.zip**
 
